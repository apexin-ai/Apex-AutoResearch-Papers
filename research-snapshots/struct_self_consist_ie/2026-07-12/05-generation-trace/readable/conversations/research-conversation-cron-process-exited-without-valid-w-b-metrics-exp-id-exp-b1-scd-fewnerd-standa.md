# Research conversation: [CRON] 实验进程异常退出（失败），需要你诊断原因。 详情: Process exited without valid W&B metrics - exp_id: exp_b1_scd_fewnerd_standard - projec

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 91
- **Recorded user turns:** 1
- **Tool calls:** 26
- **Original source:** `logs/chats/exported-trajectories/account-3/bb8bc777-37fb-4956-b48e-5e9c5a98dd73.jsonl`
- **Structured JSON:** [`7a5e30175f22e5f0feb6.json`](../../sessions/7a/7a5e30175f22e5f0feb6.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-20T19:13:39.683Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-20T19:13:39.683Z",
  "sessionId": "bb8bc777-37fb-4956-b48e-5e9c5a98dd73",
  "content": "[CRON] 实验进程异常退出（失败），需要你诊断原因。\n详情: Process exited without valid W&B metrics\n\n- exp_id: exp_b1_scd_fewnerd_standard\n- project: struct_self_consist_ie\n- server: autodl-5090-b\n- log_path: /root/autodl-tmp/struct_self_consist_ie/logs/exp_b1_scd_fewnerd_standard.log"
}
```

---

### Runtime record

_source line 2 · 2026-05-20T19:13:39.688Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-20T19:13:39.688Z",
  "sessionId": "bb8bc777-37fb-4956-b48e-5e9c5a98dd73"
}
```

---

## Round 1

89 recorded events

### User

_source line 3 · 2026-05-20T19:13:39.733Z_

[CRON] 实验进程异常退出（失败），需要你诊断原因。
详情: Process exited without valid W&B metrics

- exp_id: exp_b1_scd_fewnerd_standard
- project: struct_self_consist_ie
- server: autodl-5090-b
- log_path: /root/autodl-tmp/struct_self_consist_ie/logs/exp_b1_scd_fewnerd_standard.log

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "d2210c4d-d5b9-450f-8450-2f1ffe6e0ccd",
  "type": "user",
  "uuid": "38c24edc-4a10-42ad-9ef7-fe4e10797be0",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/agent_5c567c58",
  "sessionId": "bb8bc777-37fb-4956-b48e-5e9c5a98dd73",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-20T19:13:39.733Z_

```json
{
  "parentUuid": "38c24edc-4a10-42ad-9ef7-fe4e10797be0",
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
  "uuid": "ec514a5c-bf0c-4c4f-bc4b-123775dda1c1",
  "timestamp": "2026-05-20T19:13:39.733Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/agent_5c567c58",
  "sessionId": "bb8bc777-37fb-4956-b48e-5e9c5a98dd73",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-20T19:13:39.733Z_

```json
{
  "parentUuid": "ec514a5c-bf0c-4c4f-bc4b-123775dda1c1",
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
  "uuid": "88479dce-d023-4ca8-b7ff-8d8cad6e99e4",
  "timestamp": "2026-05-20T19:13:39.733Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/agent_5c567c58",
  "sessionId": "bb8bc777-37fb-4956-b48e-5e9c5a98dd73",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6 · 2026-05-20T19:13:39.733Z_

```json
{
  "parentUuid": "88479dce-d023-4ca8-b7ff-8d8cad6e99e4",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "a9a18950-100f-47ef-af6e-be1115ee4376",
  "timestamp": "2026-05-20T19:13:39.733Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/agent_5c567c58",
  "sessionId": "bb8bc777-37fb-4956-b48e-5e9c5a98dd73",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Diagnose experiment process exit failure",
  "sessionId": "bb8bc777-37fb-4956-b48e-5e9c5a98dd73"
}
```

---

### Assistant

_source line 8 · 2026-05-20T19:13:49.728Z_

<details><summary>Logged reasoning block</summary>

```text
收到实验失败的 CRON 回调。需要先执行 session-start 初始化，然后处理这个失败的实验。

让我按顺序来：
1. 先执行 session-start：read_registry, reconcile_crons, 读 report.md 和 ROADMAP.md
2. 然后按 on-experiment-failed skill 处理失败实验

让我先加载必要的工具和读取 skill。
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a9a18950-100f-47ef-af6e-be1115ee4376",
  "isSidechain": false,
  "requestId": "req_011CbEMTvAfJBJGCetgu8AJS",
  "type": "assistant",
  "uuid": "b85506b6-7ef7-4a17-8d22-0b716cf79285",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/agent_5c567c58",
  "sessionId": "bb8bc777-37fb-4956-b48e-5e9c5a98dd73",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014TGYdoTaU5D3e73UGSJ7NH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 25110,
      "cache_read_input_tokens": 11841,
      "output_tokens": 372,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 25110,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 372,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 25110,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 25110
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

_source line 9 · 2026-05-20T19:13:50.319Z_

收到实验失败回调，先执行 session-start 初始化，然后诊断失败原因。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b85506b6-7ef7-4a17-8d22-0b716cf79285",
  "isSidechain": false,
  "requestId": "req_011CbEMTvAfJBJGCetgu8AJS",
  "type": "assistant",
  "uuid": "c424a5a4-4347-4cba-b380-7a862d06f6c2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/agent_5c567c58",
  "sessionId": "bb8bc777-37fb-4956-b48e-5e9c5a98dd73",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014TGYdoTaU5D3e73UGSJ7NH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 25110,
      "cache_read_input_tokens": 11841,
      "output_tokens": 372,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 25110,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 372,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 25110,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 25110
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

_source line 10 · 2026-05-20T19:13:52.629Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_017LxwzYL1h2rsJnQHqkHQZe`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__reconcile_crons,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__read_roadmap,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__spawn_worker,mcp__agent-ml-research__main_agent_post_to_director,mcp__agent-ml-research__list_workers,mcp__agent-ml-research__send_progress",
  "max_results": 10
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c424a5a4-4347-4cba-b380-7a862d06f6c2",
  "isSidechain": false,
  "requestId": "req_011CbEMTvAfJBJGCetgu8AJS",
  "type": "assistant",
  "uuid": "6ea36631-e870-450e-b62d-08cb2adde13e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/agent_5c567c58",
  "sessionId": "bb8bc777-37fb-4956-b48e-5e9c5a98dd73",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014TGYdoTaU5D3e73UGSJ7NH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 25110,
      "cache_read_input_tokens": 11841,
      "output_tokens": 372,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 25110,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 372,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 25110,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 25110
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

_source line 11 · 2026-05-20T19:13:52.636Z_

<details><summary>↩ Tool result · `toolu_017LxwzYL1h2rsJnQHqkHQZe`</summary>

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

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__update_registry"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__spawn_worker"
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
  "tool_name": "mcp__agent-ml-research__list_workers"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__send_progress"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6ea36631-e870-450e-b62d-08cb2adde13e",
  "isSidechain": false,
  "promptId": "d2210c4d-d5b9-450f-8450-2f1ffe6e0ccd",
  "type": "user",
  "uuid": "761acb10-768b-4e5d-8fa0-3eb27ad1539c",
  "toolUseResult": {
    "matches": [
      "mcp__agent-ml-research__read_registry",
      "mcp__agent-ml-research__reconcile_crons",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__read_roadmap",
      "mcp__agent-ml-research__update_registry",
      "mcp__agent-ml-research__spawn_worker",
      "mcp__agent-ml-research__main_agent_post_to_director",
      "mcp__agent-ml-research__list_workers",
      "mcp__agent-ml-research__send_progress"
    ],
    "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__reconcile_crons,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__read_roadmap,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__spawn_worker,mcp__agent-ml-research__main_agent_post_to_director,mcp__agent-ml-research__list_workers,mcp__agent-ml-research__send_progress",
    "total_deferred_tools": 82
  },
  "sourceToolAssistantUUID": "6ea36631-e870-450e-b62d-08cb2adde13e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/agent_5c567c58",
  "sessionId": "bb8bc777-37fb-4956-b48e-5e9c5a98dd73",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 12 · 2026-05-20T19:14:01.052Z_

<details><summary>Logged reasoning block</summary>

```text
Now let me execute the session-start initialization steps in parallel: read_registry, reconcile_crons, read report.md, and read ROADMAP.md.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "761acb10-768b-4e5d-8fa0-3eb27ad1539c",
  "isSidechain": false,
  "requestId": "req_011CbEMUsWwa37kkn9G3rR3o",
  "type": "assistant",
  "uuid": "7784a83d-59a9-4ec0-8824-edd044ca2fff",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/agent_5c567c58",
  "sessionId": "bb8bc777-37fb-4956-b48e-5e9c5a98dd73",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M47ef1ZrNJWNiHU77ATRTY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 3530,
      "cache_read_input_tokens": 36951,
      "output_tokens": 361,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3530,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 361,
          "cache_read_input_tokens": 36951,
          "cache_creation_input_tokens": 3530,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3530
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

_source line 13 · 2026-05-20T19:14:02.057Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_019cZ9RQy6UgUj4wCYe9ecqj`</summary>

```json
{
  "project": "struct_self_consist_ie",
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
  "parentUuid": "7784a83d-59a9-4ec0-8824-edd044ca2fff",
  "isSidechain": false,
  "requestId": "req_011CbEMUsWwa37kkn9G3rR3o",
  "type": "assistant",
  "uuid": "b55e3d16-2d0a-40f4-8d82-773b46262797",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/agent_5c567c58",
  "sessionId": "bb8bc777-37fb-4956-b48e-5e9c5a98dd73",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M47ef1ZrNJWNiHU77ATRTY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 3530,
      "cache_read_input_tokens": 36951,
      "output_tokens": 361,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3530,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 361,
          "cache_read_input_tokens": 36951,
          "cache_creation_input_tokens": 3530,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3530
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

_source line 14 · 2026-05-20T19:14:02.061Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__reconcile_crons · `toolu_01PUFoM8no9CUjf1JtoJPpYz`</summary>

```json
{}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b55e3d16-2d0a-40f4-8d82-773b46262797",
  "isSidechain": false,
  "requestId": "req_011CbEMUsWwa37kkn9G3rR3o",
  "type": "assistant",
  "uuid": "2ee4cc02-5392-4ec7-9ef3-65ca58894e0e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/agent_5c567c58",
  "sessionId": "bb8bc777-37fb-4956-b48e-5e9c5a98dd73",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M47ef1ZrNJWNiHU77ATRTY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 3530,
      "cache_read_input_tokens": 36951,
      "output_tokens": 361,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3530,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 361,
          "cache_read_input_tokens": 36951,
          "cache_creation_input_tokens": 3530,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3530
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

_source line 15 · 2026-05-20T19:14:02.563Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_015KYTQjUHKsrfh3icLTC45i`</summary>

```json
{
  "project": "struct_self_consist_ie",
  "file": "report.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2ee4cc02-5392-4ec7-9ef3-65ca58894e0e",
  "isSidechain": false,
  "requestId": "req_011CbEMUsWwa37kkn9G3rR3o",
  "type": "assistant",
  "uuid": "27a922c8-0ac4-483b-aa7f-23c30a739dbd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/agent_5c567c58",
  "sessionId": "bb8bc777-37fb-4956-b48e-5e9c5a98dd73",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M47ef1ZrNJWNiHU77ATRTY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 3530,
      "cache_read_input_tokens": 36951,
      "output_tokens": 361,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3530,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 361,
          "cache_read_input_tokens": 36951,
          "cache_creation_input_tokens": 3530,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3530
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

_source line 16 · 2026-05-20T19:14:03.066Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_roadmap · `toolu_01TnwaHpTN6F9pwK748rTHDt`</summary>

```json
{
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "27a922c8-0ac4-483b-aa7f-23c30a739dbd",
  "isSidechain": false,
  "requestId": "req_011CbEMUsWwa37kkn9G3rR3o",
  "type": "assistant",
  "uuid": "ec6489d0-e14d-46e8-8da8-6a580919bce9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/agent_5c567c58",
  "sessionId": "bb8bc777-37fb-4956-b48e-5e9c5a98dd73",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M47ef1ZrNJWNiHU77ATRTY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 3530,
      "cache_read_input_tokens": 36951,
      "output_tokens": 361,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3530,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 361,
          "cache_read_input_tokens": 36951,
          "cache_creation_input_tokens": 3530,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3530
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

_source line 17 · 2026-05-20T19:14:03.400Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__list_workers · `toolu_01DzWSjPa7LpBvonjQc1i4eD`</summary>

```json
{
  "project": "struct_self_consist_ie",
  "status": "running"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ec6489d0-e14d-46e8-8da8-6a580919bce9",
  "isSidechain": false,
  "requestId": "req_011CbEMUsWwa37kkn9G3rR3o",
  "type": "assistant",
  "uuid": "2adca8d2-3f12-49f9-9c0a-9986034b2271",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/agent_5c567c58",
  "sessionId": "bb8bc777-37fb-4956-b48e-5e9c5a98dd73",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M47ef1ZrNJWNiHU77ATRTY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 3530,
      "cache_read_input_tokens": 36951,
      "output_tokens": 361,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3530,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 361,
          "cache_read_input_tokens": 36951,
          "cache_creation_input_tokens": 3530,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3530
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

_source line 18 · 2026-05-20T19:14:04.582Z_

<details><summary>↩ Tool result · `toolu_019cZ9RQy6UgUj4wCYe9ecqj`</summary>

```text
Error: result (321,036 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-agent-5c567c58/bb8bc777-37fb-4956-b48e-5e9c5a98dd73/tool-results/mcp-agent-ml-research-read_registry-1779304444566.txt.
Format: JSON with schema: {result: string}
- For targeted queries (find a value, filter by field): use jq on the file directly.
- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-agent-5c567c58/bb8bc777-37fb-4956-b48e-5e9c5a98dd73/tool-results/mcp-agent-ml-research-read_registry-1779304444566.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.
- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-agent-5c567c58/bb8bc777-37fb-4956-b48e-5e9c5a98dd73/tool-results/mcp-agent-ml-research-read_registry-1779304444566.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim." A vague "summarize this" may lose detail.

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b55e3d16-2d0a-40f4-8d82-773b46262797",
  "isSidechain": false,
  "promptId": "d2210c4d-d5b9-450f-8450-2f1ffe6e0ccd",
  "type": "user",
  "uuid": "bfcc38da-b691-47e2-a881-f55046cc9c0b",
  "toolUseResult": "Error: result (321,036 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-agent-5c567c58/bb8bc777-37fb-4956-b48e-5e9c5a98dd73/tool-results/mcp-agent-ml-research-read_registry-1779304444566.txt.\nFormat: JSON with schema: {result: string}\n- For targeted queries (find a value, filter by field): use jq on the file directly.\n- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-agent-5c567c58/bb8bc777-37fb-4956-b48e-5e9c5a98dd73/tool-results/mcp-agent-ml-research-read_registry-1779304444566.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.\n- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. \"/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-agent-5c567c58/bb8bc777-37fb-4956-b48e-5e9c5a98dd73/tool-results/mcp-agent-ml-research-read_registry-1779304444566.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim.\" A vague \"summarize this\" may lose detail.\n",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {\"exp_b1_scd_fewnerd_standard\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T11:17:37.804Z\", \"updated_at\": \"2026-05-20T19:13:31.471Z\", \"hypothesis\": \"Standard Self-Consistency Distillation on FewNERD: fine-tune Qwen3-8B-FT with theta2n construction pseudo-labels (32,565 instances) mixed 1:1 with gold data. Greedy F1 after SCD should approach N=8 construction F1 (0.764 vs current 0.748). Transductive setting: pseudo-labels from test set SC outputs.\", \"spec\": {\"command\": \"llamafactory-cli train train_config_scd_fewnerd_s42.yaml\", \"server\": \"autodl-5090-b\", \"gpu_ids\": [0], \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/data/scd_fewnerd_theta2n_s42.jsonl\", \"data_count\": 32565, \"model_name\": \"Qwen3-8B-FT\", \"seed\": 42, \"pid\": 207109}, \"reproduce\": {\"finished_at\": \"2026-05-20T19:13:25.333Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-20T19:13:26.395Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-20T19:13:35.804759+00:00\"}]}}, \"eval_scd_fewnerd_fallback\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T19:11:25.544Z\", \"updated_at\": \"2026-05-20T19:11:25.544Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && bash run_scd_fewnerd_eval.sh\\\"\", \"server\": \"autodl-5090-b\", \"gpu\": [\"cuda:0\"], \"pid\": \"270397\", \"log_path\": \"~/runs/struct_self_consist_ie/eval_scd_fewnerd_fallback.log\", \"submitted_at\": \"2026-05-20T19:11:24.918Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"exp_b1_scd_fewnerd_curriculum_q\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T11:17:38.760Z\", \"updated_at\": \"2026-05-20T19:04:33.922Z\", \"hypothesis\": \"Q variant SCD with curriculum ordering: use B2 entity verifier confidence to stratify pseudo-labels (conf>0.8→Round1, 0.5-0.8→Round2, conf<0.5→discard). Curriculum by verifier confidence improves SCD convergence and final greedy F1 vs standard flat SCD on FewNERD.\", \"spec\": {\"command\": \"llamafactory-cli train train_config_scd_fewnerd_fallback_s43.yaml\", \"server\": \"autodl-5090-b\", \"gpu_ids\": [1], \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/data/scd_fewnerd_theta2n_s42.jsonl\", \"data_count\": 32565, \"model_name\": \"Qwen3-8B-FT\", \"seed\": 43, \"note\": \"Fallback standard SCD seed=43 (Q-variant deferred per D189)\"}, \"reproduce\": {\"finished_at\": \"2026-05-20T19:01:52.441Z\"}, \"failure_reason\": \"RETRACTED: cron false positive — training completed successfully (4706/4706 steps, loss=0.023). Original: process dead 5× with no sentinel/W&B\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-20T19:01:57.213Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-20T19:02:06.612980+00:00\"}]}, \"notes\": \"Cron false positive: 训练实际完成 (4706/4706 steps, 2 epochs). train_loss=0.023, eval_loss=0.033. Checkpoint: /root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen3-8b-fewnerd-scd-fallback-lora/. 进程正常退出后 cron 误判为 failed (no W&B sentinel). 需要 eval inference 测 greedy F1 确定最终 conclusion.\", \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen3-8b-fewnerd-scd-fallback-lora/\", \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/logs/exp_b1_scd_fewnerd_fallback.log\"}, \"exp_cross_model_consistency\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T09:30:47.928Z\", \"updated_at\": \"2026-05-20T19:03:33.786Z\", \"hypothesis\": \"Cross-model entity construction (mixing Qwen and LLaMA outputs) produces higher-quality entity spans than single-model construction, because inter-model agreement filters out model-specific hallucinations while preserving genuinely supported entities.\", \"metrics\": {\"scierc\": {\"n_filtered\": 529, \"qwen_greedy_f1\": 0.6453, \"llama_greedy_f1\": 0.646, \"degeneracy\": {\"pure_qwen\": 0.1323, \"pure_llama\": 0.1777, \"mixed\": 0.0964}, \"construction_f1\": {\"pure_qwen_uniform\": 0.6449, \"pure_qwen_vc\": 0.6413, \"pure_llama_uniform\": 0.6545, \"pure_llama_vc\": 0.649, \"mixed_uniform\": 0.6625, \"mixed_vc\": 0.6591}, \"bootstrap\": {\"mixed_uni_vs_pure_qwen_uni\": {\"delta_pp\": 1.77, \"p\": 0.0102, \"ci\": [0.27, 3.28]}, \"mixed_vc_vs_pure_qwen_vc\": {\"delta_pp\": 1.77, \"p\": 0.0093, \"ci\": [0.33, 3.27]}, \"mixed_uni_vs_pure_llama_uni\": {\"delta_pp\": 0.81, \"p\": 0.1304, \"ci\": [-0.59, 2.25]}, \"mixed_vc_vs_pure_llama_vc\": {\"delta_pp\": 1.01, \"p\": 0.0702, \"ci\": [-0.32, 2.38]}}}, \"fewnerd\": {\"n_filtered\": 32565, \"qwen_greedy_f1\": 0.7478, \"llama_greedy_f1\": 0.7841, \"degeneracy\": {\"pure_qwen\": 0.1004, \"pure_llama\": 0.2336, \"mixed\": 0.1158}, \"construction_f1\": {\"pure_qwen_uniform\": 0.7499, \"pure_qwen_vc\": 0.7448, \"pure_llama_uniform\": 0.7873, \"pure_llama_vc\": 0.7869, \"mixed_uniform\": 0.7916, \"mixed_vc\": 0.7898}, \"bootstrap\": {\"mixed_uni_vs_pure_qwen_uni\": {\"delta_pp\": 4.17, \"p\": 0, \"ci\": [3.92, 4.4]}, \"mixed_vc_vs_pure_qwen_vc\": {\"delta_pp\": 4.5, \"p\": 0, \"ci\": [4.25, 4.75]}, \"mixed_uni_vs_pure_llama_uni\": {\"delta_pp\": 0.42, \"p\": 0, \"ci\": [0.27, 0.58]}, \"mixed_vc_vs_pure_llama_vc\": {\"delta_pp\": 0.29, \"p\": 0.0001, \"ci\": [0.13, 0.45]}}}}, \"conclusion\": \"success\", \"notes\": \"B5 cross-model consistency on SciERC + FewNERD. Mixed (4Q+4L) consistently outperforms pure-model construction on both datasets. FewNERD: mixed sig. beats pure LLaMA (+0.42pp uni p=0, +0.29pp VC p=0.0001) and pure Qwen (+4.17pp uni, +4.50pp VC, all p=0). SciERC: mixed sig. beats pure Qwen (+1.77pp uni p=0.01, +1.77pp VC p=0.009); vs pure LLaMA marginal (+0.81pp uni p=0.13, +1.01pp VC p=0.07). Cross-model diversity reduces degeneracy (FewNERD mixed 11.6% vs LLaMA 23.4%; SciERC mixed 9.6% vs LLaMA 17.8%). Note: SciERC greedy F1 lower than prior run (0.645 vs 0.748) — likely different eval scope (gold filter 529 vs prior 551).\", \"server\": \"autodl-5090-c\", \"gpu\": \"cuda:3\", \"spec\": {\"command\": \"bash code/run_cross_model.sh\", \"server\": \"autodl-5090\", \"data_path\": \"output/exp_026_t10_seed42/samples.jsonl + output/exp007_llama_inference/samples.jsonl + output/exp_021_inference/samples.jsonl + output/llama_fewnerd_s42/samples.jsonl\", \"data_count\": 76398, \"model_name\": \"cross-model (Qwen + LLaMA)\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_cross_model_consistency\", \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_cross_model_consistency\"}, \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_cross_model_consistency\", \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_cross_model_consistency\", \"completed_at\": \"2026-05-20T19:03:33.786Z\"}, \"exp_backup3_distill_verifier\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T17:40:49.676Z\", \"updated_at\": \"2026-05-20T18:47:37.248Z\", \"hypothesis\": \"A supervised entity-level binary classifier (trained on 6 lightweight features: LP score, agreement ratio, degeneracy flag, span length, type consistency, N) can learn cross-dataset entity correctness signals that outperform unsupervised majority voting for entity construction, because the classifier can jointly weight multiple complementary signals that MV ignores.\", \"server\": \"autodl-5090-c\", \"gpu\": \"cuda:1\", \"spec\": {\"command\": \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python /root/autodl-tmp/struct_self_consist_ie/run_distill_verifier.py --seed 42\", \"server\": \"autodl-5090\", \"data_path\": {\"scierc\": \"output/exp_026_t10_seed42/samples.jsonl (551 inst, N=8)\", \"conll\": \"output/exp_002_conll_n16/samples.jsonl (3453 inst, N=16→subsample to 8)\", \"fewnerd\": \"output/exp_021_inference/samples.jsonl (37648 inst, N=8)\"}, \"data_count\": \"41652 instances total (~551+3453+37648)\", \"model_name\": \"LR+RF+MLP ensemble (sklearn)\", \"seed\": 42}, \"conclusion\": \"negative\", \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/distill_verifier/distill_verifier_results.json\", \"log_path\": \"/tmp/distill_verifier.log\", \"completed_at\": \"2026-05-20T18:47:30.099Z\", \"metrics\": {\"aggregate\": {\"LR\": {\"mean_auroc\": 0.8747, \"std_auroc\": 0.0563, \"mean_delta_f1\": -0.0014}, \"RF\": {\"mean_auroc\": 0.8752, \"std_auroc\": 0.0588, \"mean_delta_f1\": -0.0006}, \"MLP\": {\"mean_auroc\": 0.8744, \"std_auroc\": 0.0578, \"mean_delta_f1\": 0.0011}}, \"per_fold\": {\"scierc\": {\"LR\": {\"auroc\": 0.8009, \"std_mv_f1\": 0.6643, \"best_weighted_f1\": 0.6659, \"delta_f1\": 0.0016}, \"RF\": {\"auroc\": 0.7988, \"best_weighted_f1\": 0.6647, \"delta_f1\": 0.0004}, \"MLP\": {\"auroc\": 0.798, \"best_weighted_f1\": 0.6655, \"delta_f1\": 0.0012}}, \"conll\": {\"LR\": {\"auroc\": 0.9376, \"std_mv_f1\": 0.9074, \"best_weighted_f1\": 0.9049, \"delta_f1\": -0.0025}, \"RF\": {\"auroc\": 0.9419, \"best_weighted_f1\": 0.908, \"delta_f1\": 0.0006}, \"MLP\": {\"auroc\": 0.9379, \"best_weighted_f1\": 0.9075, \"delta_f1\": 0.0001}}, \"fewnerd\": {\"LR\": {\"auroc\": 0.8855, \"std_mv_f1\": 0.7819, \"best_weighted_f1\": 0.7786, \"delta_f1\": -0.0034}, \"RF\": {\"auroc\": 0.885, \"best_weighted_f1\": 0.7791, \"delta_f1\": -0.0029}, \"MLP\": {\"auroc\": 0.8872, \"best_weighted_f1\": 0.7839, \"delta_f1\": 0.002}}}, \"feature_importance_LR_scierc\": {\"agreement_ratio\": 1.651, \"lp_score\": 0.424, \"span_length\": -0.15, \"type_consistency\": 0.128, \"degeneracy_flag\": 0.043, \"n_samples\": 0}}}, \"exp_spider_sc_pilot\": {\"status\": \"PENDING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T18:41:49.560Z\", \"updated_at\": \"2026-05-20T18:41:56.313Z\", \"hypothesis\": \"SC diagnostic cascade (degeneracy, LP-quality gap, agreement-correctness correlation) validated on NER structured generation will also manifest in SQL structured generation with Qwen2.5-7B-Instruct on Spider, demonstrating cross-task universality of the diagnostic framework.\", \"spec\": {\"command\": \"source /root/autodl-tmp/struct_self_consist_ie/env.sh && CUDA_VISIBLE_DEVICES=2 python3 /root/autodl-tmp/struct_self_consist_ie/code/run_spider_sc.py\", \"server\": \"autodl-5090-b\", \"gpu\": \"cuda:2\", \"data_path\": \"xlangai/spider (HF) + synthetic databases from tables.json\", \"data_count\": 200, \"model_name\": \"Qwen2.5-7B-Instruct\", \"seed\": 42}}, \"exp_14b_inference_fewnerd\": {\"status\": \"RUNNING\", \"retry_count\": 1, \"created_at\": \"2026-05-20T14:36:27.954Z\", \"updated_at\": \"2026-05-20T18:35:49.878Z\", \"hypothesis\": \"14B Qwen2.5 inference on FewNERD (N∈{1,2,4,8,16}): primary dataset should show oracle scaling law F1(N)=a-b*N^(-c) consistent at 14B scale, filling the scaling curve between 7B and 32B.\", \"reproduce\": {\"finished_at\": \"2026-05-20T17:19:15.098Z\"}, \"failure_reason\": \"FALSE POSITIVE: PID 201001 died but inference continues under PID 217692→217960 (EngineCore). Fewnerd n=2 at 24% on GPU 0. Earlier ckpt36000 run crashed with EngineDeadError (CUDA OOM from torch.compile); current merged-final run uses enforce_eager=True and is stable. KV cache critically low (1.09 GiB) — recommend tensor_parallel=2 for future 14B runs.\", \"completed_at\": \"2026-05-20T17:19:16.003Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-20T17:19:25.424710+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\", \"notes\": \"2026-05-21 diagnosis: Process STILL RUNNING. PID 217692 (python) → 217960 (EngineCore) on GPU 0. Completed: SciERC/CoNLL all N + FewNERD N=1. In progress: FewNERD N=2 (24%, ETA ~2h). Log: /tmp/14b_fewnerd.log. SciERC/CoNLL results are garbage (model FewNERD-only, F1<0.05). KV cache critically low (1.09 GiB). Earlier ckpt36000 run crashed with EngineDeadError at 60% — fixed by enforce_eager=True.\"}}, \"notes\": \"2026-05-21 diagnosis: Process STILL RUNNING. PID 217692 (python) → 217960 (EngineCore) on GPU 0. Completed: SciERC/CoNLL all N + FewNERD N=1. In progress: FewNERD N=2 (24%, ETA ~2h). Log: /tmp/14b_fewnerd.log. SciERC/CoNLL results are garbage (model FewNERD-only, F1<0.05). KV cache critically low (1.09 GiB). Earlier ckpt36000 run crashed with EngineDeadError at 60% — fixed by enforce_eager=True.\", \"spec\": {\"server\": \"autodl-5090-c\", \"pid\": 217960}, \"server\": \"autodl-5090-c\"}, \"exp_b_frontier_sc_fewnerd\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T18:15:19.266Z\", \"updated_at\": \"2026-05-20T18:24:49.540Z\", \"hypothesis\": \"The correlation-selection gap in structured self-consistency persists with frontier models (GPT-5.5, Claude Opus 4.6), indicating it is a fundamental limitation of frequency-based SC for structured prediction rather than a capability issue of smaller models.\", \"spec\": {\"command\": \"python run_frontier_sc.py --from-hf --n-instances 200 --n-samples 8 --temperature 1.0 --seed 42\", \"server\": \"local (CPU-only, API calls)\", \"data_path\": \"HuggingFace: DFKI-SLT/few-nerd (supervised, test split)\", \"data_count\": 200, \"model_name\": \"GPT-5.5 + Claude Opus 4.6\", \"seed\": 42}}, \"exp_a3_ace05_re\": {\"status\": \"QUEUED\", \"retry_count\": 0, \"created_at\": \"2026-05-20T18:15:17.438Z\", \"updated_at\": \"2026-05-20T18:24:21.919Z\", \"hypothesis\": \"Cross-task universality: SC diagnostic cascade on ACE05 Relation Extraction. Closest extension to NER—same structured prediction paradigm, different output structure (entity pairs + relation types). Qwen2.5-7B-Instruct few-shot prompt. If correlation-selection gap exists for RE, the framework covers multiple IE sub-tasks.\", \"spec\": {\"hypothesis\": \"The SC diagnostic cascade (degeneracy, agreement, LP-quality gap) generalizes from NER to Relation Extraction, with failure modes F1-F4 exhibiting analogous distributions on RE because both are span-based structured prediction tasks sharing the same underlying model uncertainty structure.\", \"model_name\": \"Qwen2.5-7B-Instruct\", \"data_path\": \"SciERC test split (relation-filtered)\", \"data_count\": 300, \"server\": \"autodl-5090\", \"seed\": 42, \"command\": \"python run_re_sc.py --model-path /root/autodl-tmp/models/Qwen2.5-7B-Instruct --data /root/autodl-tmp/struct_self_consist_ie/data/re_test_instances.jsonl --output-dir /root/autodl-tmp/struct_self_consist_ie/output/re_sc --n-samples 8 --temperature 1.0\", \"method\": \"SC diagnostic cascade on RE (few-shot, N=8, T=1.0, XGrammar constrained decoding)\", \"parent\": null}}, \"exp_a2_humaneval_sc\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T18:15:14.615Z\", \"updated_at\": \"2026-05-20T18:19:23.107Z\", \"hypothesis\": \"SC failure modes (degeneracy, false agreement) generalize from NER to code generation despite deterministic verification — majority voting on HumanEval will show limited gains over greedy when degeneracy is high, paralleling NER findings.\", \"spec\": {\"command\": \"python run_humaneval_sc.py --n_samples 8 --temperature 1.0 --seed 42 --output_dir ./results --test_api\", \"server\": \"cpu-only (API call + local test execution)\", \"data_path\": \"openai/openai_humaneval (HuggingFace)\", \"data_count\": 164, \"model_name\": \"GPT-5.5 (OpenRouter)\", \"seed\": 42}}, \"exp_backup1_het_temp\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T17:09:31.094Z\", \"updated_at\": \"2026-05-20T18:15:37.574Z\", \"hypothesis\": \"Heterogeneous-Temperature Sampling: MRSC/LSC negative results prove entity-level correction cannot close the selection gap. F4 degeneracy analysis shows T=0.7 has ~62% degeneracy (too homogeneous) while T=1.0 has more diversity but noisier entities. Mixing samples from different temperatures (k from T_low + (8-k) from T_high) breaks temperature-specific degeneracy patterns: low-T samples provide precise entities, high-T samples provide diversity. Mixed-T N=8 pool should achieve lower degeneracy than pure T_low and higher construction F1 than pure T_high. Hypothesis source: entity-level methods (MRSC weighted re-prompting, LSC latent aggregation) both failed → pivot to sampling-level diversity improvement.\", \"parent\": \"exp_mrsc_multi_round\", \"spec\": {\"command\": \"bash /root/autodl-tmp/struct_self_consist_ie/run_het_temp_all.sh\", \"server\": \"autodl-5090\", \"gpu\": [], \"pid\": \"948780\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_backup1_het_temp.log\", \"submitted_at\": \"2026-05-20T18:13:20.732Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"N/A\", \"wall_clock_seconds\": 134.1, \"gpu_hours\": 0.0}, \"metrics\": {\"t08_vs_t10\": {\"seed42\": {\"pure_t_low_f1\": 0.6755, \"pure_t_high_f1\": 0.6643, \"best_mix\": \"5:3\", \"best_mix_f1\": 0.6708, \"delta_vs_low\": -0.0046, \"delta_vs_high\": 0.0066}, \"seed123\": {\"pure_t_low_f1\": 0.6659, \"pure_t_high_f1\": 0.6681, \"best_mix\": \"6:2\", \"best_mix_f1\": 0.6655, \"delta_vs_low\": -0.0004, \"delta_vs_high\": -0.0026}, \"seed456\": {\"pure_t_low_f1\": 0.6675, \"pure_t_high_f1\": 0.6663, \"best_mix\": \"4:4\", \"best_mix_f1\": 0.6654, \"delta_vs_low\": -0.002, \"delta_vs_high\": -0.0008}}, \"t05_vs_t10\": {\"seed42\": {\"pure_t_low_f1\": 0.663, \"pure_t_high_f1\": 0.6643, \"best_mix\": \"5:3\", \"best_mix_f1\": 0.6654, \"delta_vs_low\": 0.0024, \"delta_vs_high\": 0.0011}, \"seed123\": {\"pure_t_low_f1\": 0.6665, \"pure_t_high_f1\": 0.6681, \"best_mix\": \"2:6\", \"best_mix_f1\": 0.6671, \"delta_vs_low\": 0.0006, \"delta_vs_high\": -0.001}, \"seed456\": {\"pure_t_low_f1\": 0.6686, \"pure_t_high_f1\": 0.6663, \"best_mix\": \"4:4\", \"best_mix_f1\": 0.6682, \"delta_vs_low\": -0.0004, \"delta_vs_high\": 0.002}}, \"degeneracy\": {\"t05_mean\": 0.356, \"t08_mean\": 0.178, \"t10_mean\": 0.126}, \"max_delta_any_combo\": 0.0066}, \"conclusion\": \"negative\", \"completed_at\": \"2026-05-20T18:15:34.876Z\", \"notes\": \"Heterogeneous temperature mixing provides no consistent F1 improvement over pure single-temperature sampling on SciERC (551 instances, 3 seeds, 2 temp pairs). All F1 deltas within ±0.005, inconsistent direction across seeds. Mixing does reduce degeneracy (T=0.5: 35%→17%) but this doesn't translate to F1 gain. The pure T_low vs T_high F1 gap is already tiny (~0.001-0.01), leaving no room for mixing to exploit. Joins MRSC/LSC as evidence that sampling-level interventions cannot improve construction F1 when the bottleneck is not sample diversity.\"}, \"exp_a1_spider_sql_sc\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T18:15:12.865Z\", \"updated_at\": \"2026-05-20T18:15:33.104Z\", \"hypothesis\": \"Cross-task universality: SC diagnostic cascade (degeneracy, LP-quality gap, agreement-correctness correlation) applies to SQL structured generation on Spider. Qwen2.5-7B-Instruct base model, 200 dev examples, N=8 T=1.0, execution accuracy evaluation. If F1-F4 failure modes exist in SQL, the framework generalizes beyond NER.\", \"server\": \"autodl-5090-b\", \"gpu\": \"cuda:2\"}, \"exp_asb_adaptive_budget\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T15:37:33.233Z\", \"updated_at\": \"2026-05-20T18:14:15.894Z\", \"hypothesis\": \"Adaptive Sample Budget: extension of E_θ threshold optimization to sample count N. Instance features (degeneracy, LP variance, agreement rate) predict optimal N per instance. Under fixed total budget=8 (average), adaptive allocation outperforms uniform N=8 by allocating more samples to high-uncertainty instances and fewer to degenerate/easy ones.\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python /root/autodl-tmp/struct_self_consist_ie/artifacts/experiments/asb/run_asb.py --data_paths /root/autodl-tmp/struct_self_consist_ie/output/exp_021_inference/samples.jsonl,/root/autodl-tmp/struct_self_consist_ie/output/exp_026_t10_seed42/samples.jsonl,/root/autodl-tmp/struct_self_consist_ie/output/exp_002_conll_n16/samples.jsonl --dataset_names FewNERD,SciERC,CoNLL --output_dir /root/autodl-tmp/struct_self_consist_ie/output/exp_asb_adaptive_budget/ --seed 42\\\"\", \"server\": \"autodl-5090\", \"gpu\": [], \"pid\": \"943151\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_asb_adaptive_budget.log\", \"submitted_at\": \"2026-05-20T17:55:06.477Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"output/exp_asb_adaptive_budget/asb_results.json\", \"wall_clock_seconds\": 215.1, \"gpu_hours\": 0.0}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-20T17:58:41.592Z\", \"metrics\": {\"fewnerd\": {\"greedy_f1\": 0.7478, \"uniform_n8_f1\": 0.7277, \"adaptive_f1\": 0.744, \"oracle_f1\": 0.7616, \"delta_adaptive_uniform\": 0.0163, \"best_predictor\": \"MLP\", \"mean_optimal_n\": 4.4, \"n_instances\": 32565}, \"scierc\": {\"greedy_f1\": 0.6453, \"uniform_n8_f1\": 0.6382, \"adaptive_f1\": 0.6528, \"oracle_f1\": 0.6658, \"delta_adaptive_uniform\": 0.0146, \"best_predictor\": \"RF\", \"mean_optimal_n\": 4.29, \"n_instances\": 529}, \"conll\": {\"greedy_f1\": 0.907, \"uniform_n8_f1\": 0.9021, \"adaptive_f1\": 0.9046, \"oracle_f1\": 0.9078, \"delta_adaptive_uniform\": 0.0025, \"best_predictor\": \"MLP\", \"mean_optimal_n\": 3.94, \"n_instances\": 2756}, \"top_features\": [\"degeneracy_rate\", \"agreement\"], \"key_finding\": \"Most instances optimal N≈4, greedy > uniform N=8 on FewNERD confirms MV harmful on easy instances\"}}, \"exp_14b_inference_conll\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T14:36:26.315Z\", \"updated_at\": \"2026-05-20T17:50:50.216Z\", \"hypothesis\": \"14B Qwen2.5 inference on CoNLL (N∈{1,2,4,8,16}): high-resource dataset should show higher degeneracy at 14B scale, consistent with 7B pattern where construction gain is negative.\", \"reproduce\": {\"finished_at\": \"2026-05-20T14:49:00.238Z\"}, \"failure_reason\": \"Director ordered kill: cross-domain 14B inference deemed valueless by Reviewer. Only FewNERD 14B inference retained.\", \"conclusion\": \"killed\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-20T14:49:09.529266+00:00\"}]}, \"server\": \"autodl-5090-c\", \"gpu\": \"cuda:2\"}, \"exp_tlow_fewnerd_inference\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T17:40:52.432Z\", \"updated_at\": \"2026-05-20T17:47:23.345Z\", \"hypothesis\": \"Lower temperature (T=0.5) sampling on FewNERD produces less diverse but higher-quality samples that, when combined with T=1.0 samples in heterogeneous-temperature selection, improve self-consistency-based quality estimation compared to single-temperature baselines.\", \"server\": \"autodl-5090-c\", \"gpu\": \"cuda:2\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 python code/run_mvp_pilot.py --model_path checkpoints/qwen25-7b-fewnerd-merged --data_dir data/fewnerd/ --dataset fewnerd --subtask ner --n_samples 8 --temperature 0.5 --seed 42 --collect_logprobs --output_dir output/exp_tlow_fewnerd_t05_s42/\", \"server\": \"autodl-5090-c\", \"gpu\": \"cuda:2\", \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/data/fewnerd/test.json\", \"data_count\": 37648, \"model_name\": \"qwen25-7b-fewnerd-merged\", \"seed\": 42, \"pid\": 221493, \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_tlow_fewnerd_t05_s42.log\"}}, \"exp_esj_entity_self_judgment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T15:31:53.721Z\", \"updated_at\": \"2026-05-20T17:44:33.778Z\", \"hypothesis\": \"Entity-Level Self-Judgment: F4 diagnostic proves 4/5 signals are instance-level only, LP is per-sample but compressed. ESJ provides true per-sample-per-entity signal via yes/no verification prompts. ESJ-weighted entity construction should outperform majority vote by leveraging entity-level confidence scores that structural signals cannot provide. Parent: exp_e2_mixture_of_signals (F4 LP-only diagnostic).\", \"parent\": \"exp_e2_mixture_of_signals\", \"server\": \"autodl-5090-c\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"reproduce\": {\"server\": \"autodl-5090-c\", \"gpu\": \"cuda:1\", \"started_at\": \"2026-05-20T15:37:30.954Z\"}, \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python run_esj.py --base_model_path checkpoints/qwen25-7b-fewnerd-merged --data_path output/fewnerd_7b/qwen25_7b_n8_seed42/samples.jsonl --output_dir output/exp_esj_entity_self_judgment --batch_size 8\", \"server\": \"autodl-5090-c\", \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/fewnerd_7b/qwen25_7b_n8_seed42/samples.jsonl\", \"data_count\": 37648, \"model_name\": \"qwen25-7b-fewnerd-merged\", \"seed\": 42, \"pid\": 218678, \"gpu\": \"cuda:1\", \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_esj_entity_self_judgment.log\", \"checkpoint_source\": \"/root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen25-7b-fewnerd-merged\", \"eval_data\": \"/root/autodl-tmp/struct_self_consist_ie/output/fewnerd_7b/qwen25_7b_n8_seed42/samples.jsonl\", \"n_verification_prompts\": 153649, \"estimated_runtime_hours\": 2.5, \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_esj_entity_self_judgment/\"}, \"conclusion\": \"negative\", \"completed_at\": \"2026-05-20T17:44:33.778Z\"}, \"exp_b3_prompted_diversity\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T11:12:51.750Z\", \"updated_at\": \"2026-05-20T17:40:45.878Z\", \"hypothesis\": \"Structurally different prompt templates (expert persona, descriptive types, recall-focused) generate more diverse N=8 samples than repeating a single template, improving entity construction F1 via broader coverage of the entity space.\", \"conclusion\": \"killed\", \"metrics\": {\"single_vc_weighted_f1\": 0.7723, \"multi_vc_weighted_f1\": 0.7311, \"delta_vc\": -0.0412, \"single_lp_weighted_f1\": 0.7665, \"multi_lp_weighted_f1\": 0.7308, \"delta_lp\": -0.0356, \"single_theta2n_f1\": 0.7618, \"multi_theta2n_f1\": 0.7269, \"delta_theta2n\": -0.0349, \"single_unique_entities\": 5.29, \"multi_unique_entities\": 4.06, \"within_template_jaccard\": 0.474, \"cross_template_jaccard\": 0.67, \"verdict\": \"Multi-template strictly worse. Templates converge to similar outputs; non-standard templates add noise, diluting construction signals.\"}, \"server\": \"autodl-5090-c\", \"gpu\": \"cuda:3\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 python /root/autodl-tmp/struct_self_consist_ie/code/exp_b3_prompted_diversity.py --phase both --num_instances 3000 --seed 42\", \"server\": \"autodl-5090-c\", \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/data/fewnerd/test.json\", \"data_count\": 3000, \"model_name\": \"qwen3-8b-fewnerd-exp021-merged\", \"seed\": 42, \"checkpoint_path\": \"N/A\", \"log_path\": \"N/A\"}, \"completed_at\": \"2026-05-20T17:40:45.878Z\"}, \"exp_mrsc_multi_round\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T15:37:27.523Z\", \"updated_at\": \"2026-05-20T17:12:53.641Z\", \"hypothesis\": \"Multi-Round Iterative SC: N inverse scaling reveals disputed entities cause failures. Focused re-prompting on disputed entities (agreement < 0.6) with weighted aggregation (Round 2 weight=2) should reduce error rate on disputed entities without affecting non-disputed ones, closing part of the selection gap through iterative refinement rather than single-round aggregation.\", \"server\": \"autodl-5090-c\", \"gpu\": \"cuda:3\", \"account\": \"root\", \"reproduce\": {\"server\": \"autodl-5090-c\", \"gpu\": \"cuda:3\", \"started_at\": \"2026-05-20T15:39:10.190Z\"}, \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 python /root/autodl-tmp/struct_self_consist_ie/code/run_mrsc.py --base_model_path /root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen25-7b-fewnerd-merged --data_path /root/autodl-tmp/struct_self_consist_ie/output/fewnerd_7b/qwen25_7b_n8_seed42/samples.jsonl --output_dir /root/autodl-tmp/struct_self_consist_ie/output/exp_mrsc_multi_round --batch_size 16\", \"server\": \"autodl-5090-c\", \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/fewnerd_7b/qwen25_7b_n8_seed42/samples.jsonl\", \"data_count\": 37648, \"model_name\": \"qwen25-7b-fewnerd-merged\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_mrsc_multi_round\", \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_mrsc_multi_round.log\"}, \"conclusion\": \"negative\", \"completed_at\": \"2026-05-20T17:12:53.641Z\"}, \"exp_lsc_latent_sc\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T15:37:31.881Z\", \"updated_at\": \"2026-05-20T17:11:49.135Z\", \"hypothesis\": \"Latent Self-Consistency: F4 diagnostic proves LP is compressed (median range 0.041 nats). Hidden states contain richer per-sample information than scalar LP. Entity-level mean-pooled hidden state representations enable latent aggregation (centroid selection, latent confidence scoring, clustering) that bypasses LP compression and provides discriminative per-sample ranking unavailable from output-space signals.\", \"parent\": \"exp_e2_mixture_of_signals\", \"server\": \"autodl-5090-c\", \"gpu\": \"cuda:2\", \"account\": \"root\", \"reproduce\": {\"server\": \"autodl-5090-c\", \"gpu\": \"cuda:2\", \"started_at\": \"2026-05-20T15:39:11.609Z\"}, \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 python run_lsc.py --base_model_path qwen25-7b-fewnerd-merged --data_path fewnerd_7b/qwen25_7b_n8_seed42/samples.jsonl --max_instances 2000\", \"server\": \"autodl-5090-c\", \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/fewnerd_7b/qwen25_7b_n8_seed42/samples.jsonl\", \"data_count\": 2000, \"model_name\": \"qwen25-7b-fewnerd-merged\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen25-7b-fewnerd-merged\", \"eval_data\": \"FewNERD test (gold-filtered, n=2000)\", \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_lsc_latent_sc\", \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_lsc_latent_sc.log\"}, \"conclusion\": \"negative\", \"completed_at\": \"2026-05-20T16:51:53.120Z\", \"metrics\": {\"centroid_selection_f1\": 0.7593, \"lp_selection_f1\": 0.7845, \"latent_entity_conf_f1\": 0.8385, \"majority_vote_f1\": 0.8366, \"greedy_f1\": 0.7793, \"oracle_f1\": 0.8668, \"lp_vs_latent_rho\": 0.518, \"entity_match_rate\": 0.9945, \"n_instances\": 2000, \"runtime_s\": 507}}, \"exp_e_theta_adaptive\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T15:31:49.319Z\", \"updated_at\": \"2026-05-20T15:39:42.117Z\", \"hypothesis\": \"Threshold-Adaptive SC: N inverse scaling (D191) proves θ choice determines scaling direction. A learned θ predictor (input: degeneracy_level, lp_variance, N, dataset, model) can select per-instance optimal θ, closing the gap between fixed θ=0.5 and oracle θ. Leave-one-config-out CV on 16 configs from existing N=8/16 data. 5 variants: LogReg/MLP × feature subsets + degeneracy-only baseline.\", \"spec\": {\"command\": \"CPU-only: 5 parallel workers with different feature/model variants\", \"server\": \"local-cpu\", \"data_path\": \"existing N=8/16 inference results across FewNERD/CoNLL/SciERC\", \"data_count\": 16, \"model_name\": \"LogReg/MLP predictors\", \"seed\": 42}}, \"exp_14b_inference_scierc\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T14:36:25.505Z\", \"updated_at\": \"2026-05-20T15:11:54.487Z\", \"hypothesis\": \"14B Qwen2.5 inference on SciERC (N∈{1,2,4,8,16}): correlation-selection gap pattern should be consistent at 14B scale with intermediate degeneracy rates between 7B and 32B.\", \"reproduce\": {\"finished_at\": \"2026-05-20T14:48:16.272Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"conclusion\": \"killed\", \"completed_at\": \"2026-05-20T14:48:17.102Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-20T14:48:25.726567+00:00\"}]}}, \"exp_qwen25_14b_fewnerd\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-19T06:19:31.620Z\", \"updated_at\": \"2026-05-20T14:12:35.350Z\", \"hypothesis\": \"The correlation-selection gap pattern is consistent at 14B scale, filling the gap between 8B and 32B. Qwen2.5-14B QLoRA fine-tuned on FewNERD should show intermediate degeneracy rates and similar signal ranking patterns, providing a smooth scaling curve for the diagnostic findings.\", \"server\": \"autodl-5090-c\", \"gpu\": \"cuda:0,cuda:1\", \"account\": \"root\", \"reproduce\": {\"server\": \"autodl-5090-c\", \"gpu\": \"cuda:0,cuda:1\", \"started_at\": \"2026-05-19T06:47:43.938Z\"}, \"notes\": \"2026-05-19 12:47 UTC: RECOVERED from false-positive startup recovery failure. Step 6483/41180 (15.7%), loss 0.0608, ~2.2s/it, ETA ~21h. checkpoint-6000 saved. screen train_14b_s42 PID 56766, GPU 0,1 95-96% util. Cron registered on PID 56773.\", \"failure_reason\": \"startup recovery: RUNNING with no cron and no server/pid info\", \"completed_at\": \"2026-05-19T12:44:29.453Z\", \"extra\": {\"previous_failure\": {\"conclusion\": \"failed\", \"notes\": \"2026-05-19 11:36 UTC: step 4934/41180 (12.0%), loss 0.067, ~2.15s/it, ETA ~22h. checkpoint-4000 saved. screen train_14b_s42, 2×5090 76-77% util.\"}}, \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0,1 FORCE_TORCHRUN=1 NNODES=1 NPROC_PER_NODE=2 llamafactory-cli train train_config_qwen25_14b_fewnerd_s42.yaml\", \"server\": \"autodl-5090-c\", \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/data/fewnerd/llmfactory_train.json\", \"data_count\": 131767, \"model_name\": \"Qwen2.5-14B-Instruct\", \"seed\": 42, \"gpu_ids\": [\"cuda:0\", \"cuda:1\"], \"screen_session\": \"train_14b_s42\", \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/logs/train_14b_s42.log\", \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen25-14b-fewnerd-qlora-s42/\"}, \"metrics\": {\"epoch\": 5, \"train_loss\": 0.0348, \"eval_loss\": 0.0323, \"train_runtime_hours\": 29.8, \"train_samples_per_second\": 6.141, \"train_steps_per_second\": 0.384, \"total_steps\": 41180}, \"conclusion\": \"success\"}, \"exp_b1_scd_conll_control\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T11:17:40.591Z\", \"updated_at\": \"2026-05-20T13:08:32.832Z\", \"hypothesis\": \"Negative control: SCD on CoNLL where construction gain is negative (-0.4pp, high degeneracy 70%). If SCD learns from construction pseudo-labels, it should NOT improve greedy F1 on a dataset where construction itself hurts. Expected: no improvement or slight degradation. Validates SCD mechanism.\", \"spec\": {\"command\": \"llamafactory-cli train train_config_scd_conll_s42.yaml\", \"server\": \"autodl-5090-b\", \"gpu_ids\": [2], \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/data/scd_conll_theta2n_s42.jsonl\", \"data_count\": 3453, \"model_name\": \"Qwen3-8B-FT-CoNLL\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen3-8b-conll-scd-lora\", \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/logs/scd_conll_s42.log\"}, \"reproduce\": {\"finished_at\": \"2026-05-20T12:14:27.727Z\"}, \"failure_reason\": \"OVERRIDE: Training completed normally (690/690 steps, loss=0.0359). Cron misjudged as failed. Pending eval inference.\", \"conclusion\": \"negative\", \"completed_at\": \"2026-05-20T12:14:30.260Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-20T12:14:35.853775+00:00\"}]}, \"metrics\": {\"pre_scd_greedy_f1\": 0.9078, \"post_scd_greedy_f1\": 0.9184, \"delta_pp\": 1.06, \"training_steps\": 690, \"final_loss\": 0.0359, \"negative_control_confirmed\": false, \"note\": \"SURPRISE: SCD improved CoNLL F1 by +1.06pp despite negative construction gain. Possible explanations: (1) SCD provides general training benefit (more data), (2) additional training steps alone improve, (3) SCD mechanism doesn't require positive construction gain.\"}}, \"exp_b2_v4_inverse_frequency\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T12:50:51.737Z\", \"updated_at\": \"2026-05-20T12:51:06.312Z\", \"hypothesis\": \"Inverse-frequency weighting of entity features (agreement_count, vc, sj normalized by log(1+type_freq)) improves cross-domain generalization by reducing dominance of high-frequency entity types. Two variants: A) replace original features, B) augment as additional features.\", \"conclusion\": \"negative\", \"metrics\": {\"variant_a_replace_fold3_lgb_auc\": 0.834, \"variant_a_replace_fold3_ece\": 0.2188, \"variant_a_f1_delta\": -0.013, \"variant_b_augment_fold3_lgb_auc\": 0.8541, \"variant_b_augment_fold3_ece\": 0.1934, \"variant_b_f1_delta\": -0.009, \"sj_ifw_std_reduction\": \"54% (0.138→0.063)\", \"ac_ifw_std_reduction\": \"10% (0.122→0.110)\", \"verdict\": \"IFW improves stability but reduces discriminative power. Augment variant neutral. Replace variant harmful.\"}, \"parent\": \"exp_b2_entity_verifier\"}, \"exp_b2_v3_domain_invariant\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T12:50:49.948Z\", \"updated_at\": \"2026-05-20T12:51:00.972Z\", \"hypothesis\": \"Removing domain-specific features (dataset_enc, entity_type distributions) forces the verifier to rely on domain-invariant signals, improving cross-domain generalization at the cost of some discriminative power. If LGB AUC improves on held-out domains, domain features were causing negative transfer.\", \"conclusion\": \"negative\", \"metrics\": {\"fold3_fewnerd_lgb_auc\": 0.8562, \"fold3_fewnerd_xgb_auc\": 0.8518, \"fold3_ece\": 0.1373, \"fold2_scierc_lgb_auc\": 0.8152, \"fold2_scierc_xgb_auc\": 0.8163, \"vs_v2_fold3_lgb_delta\": 0.0085, \"vs_v2_fold2_lgb_delta\": 0.0146, \"top_features\": \"agreement_count (58.4%) + vc (30.3%) = 88%\", \"verdict\": \"LGB AUC improved by removing domain features, confirming negative transfer. But ECE still high, F1 delta still negative.\"}, \"parent\": \"exp_b2_entity_verifier\"}, \"exp_b2_v2_multi_domain_joint\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T12:50:09.686Z\", \"updated_at\": \"2026-05-20T12:50:18.610Z\", \"hypothesis\": \"Joint multi-domain training (CoNLL+SciERC+FewNERD LODO) improves entity verifier AUC and cross-domain construction F1 by exposing the model to diverse entity patterns. Tests whether training data diversity overcomes the calibration gap that caused B2 original to fail on FewNERD.\", \"conclusion\": \"negative\", \"metrics\": {\"fold3_fewnerd_lgb_auc\": 0.8477, \"fold3_fewnerd_xgb_auc\": 0.8603, \"fold3_fewnerd_f1_delta\": -0.008, \"fold3_ece\": 0.136, \"fold4_iid_ece\": 0.007, \"vs_b2_original_lgb_auc_delta\": 0.014, \"vs_b2_original_xgb_auc_delta\": 0.032, \"verdict\": \"AUC improved but F1 still negative. Cross-domain calibration gap unsolved.\"}, \"parent\": \"exp_b2_entity_verifier\"}, \"exp_b2_entity_verifier\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T10:13:41.037Z\", \"updated_at\": \"2026-05-20T12:28:21.280Z\", \"hypothesis\": \"An XGBoost/LightGBM entity-level verifier trained on agreement_count, VC, LP features can predict whether entity candidates are in gold annotations, enabling post-hoc filtering or score-weighted construction that improves over greedy baseline, with cross-dataset generalization from CoNLL+SciERC to FewNERD+WNUT.\", \"metrics\": {\"oof_auc\": 0.9233, \"oof_path_a_f1_delta\": 0.003, \"oof_path_b_f1_delta\": -0.0157, \"oof_greedy_f1\": 0.8216, \"oof_path_a_f1\": 0.8246, \"oof_majority_vote_f1\": 0.8048, \"leakage_pct\": 91, \"original_delta_pp\": 3.62, \"oof_delta_pp\": 0.3, \"per_dataset\": {\"scierc\": \"+1.28pp\", \"conll\": \"+0.55pp\", \"fewnerd\": \"+0.02pp\"}, \"verdict\": \"B2 verifier gain was 91% leakage. OOF Path A +0.30pp not significant. NOT suitable for paper §5.\", \"n_inverse_scaling_validation\": {\"subset_n\": 4351, \"full_n\": 32565, \"subset_greedy_f1\": 0.7926, \"full_greedy_f1\": 0.7913, \"verdict\": \"Not a bug. Representative subset. Paper should note subset size.\"}}, \"conclusion\": \"negative\"}, \"exp_b1_scd_threshold_ablation\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T11:17:42.163Z\", \"updated_at\": \"2026-05-20T11:55:33.575Z\", \"hypothesis\": \"Construction threshold sweep for SCD pseudo-label generation on FewNERD: θ∈{1/N, 2/N, 3/N, 0.5}. Higher θ = more conservative pseudo-labels (higher precision, lower recall). Optimal θ balances pseudo-label quality vs quantity for SCD training effectiveness.\", \"spec\": {\"command\": \"llamafactory-cli train train_config_scd_fewnerd_theta3_s42.yaml\", \"server\": \"autodl-5090-b\", \"gpu_ids\": [3], \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/data/scd_fewnerd_theta3n_s42.jsonl\", \"data_count\": 32565, \"model_name\": \"Qwen3-8B-FT\", \"seed\": 42, \"note\": \"theta=3/N ablation\"}}, \"exp_b1_scd\": {\"status\": \"PENDING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T11:12:48.805Z\", \"updated_at\": \"2026-05-20T11:12:56.838Z\", \"hypothesis\": \"Self-Consistency Distillation via theta2n construction pseudo-labels can teach Qwen3-8B-FT to internalize SC benefits: after iterative SCD (M0→M1→M2→M3), greedy F1 should approach N=8 construction F1 (FewNERD target: 0.764 vs current greedy 0.748). CoNLL serves as negative control (construction Δ=-0.4pp, SCD should not help). Transductive setting: pseudo-labels from test set SC outputs.\"}, \"exp_a2_degen_regression\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T10:13:37.615Z\", \"updated_at\": \"2026-05-20T10:13:55.891Z\", \"hypothesis\": \"Degeneracy rate is primarily driven by task difficulty (dataset entropy ceiling) rather than model capability, with a positive correlation between base F1 and degeneracy — easy tasks with high F1 produce degenerate outputs because the model has already converged.\", \"metrics\": {\"n_points\": 30, \"linear_r2\": 0.414, \"quadratic_r2\": 0.592, \"spearman_rho\": 0.519, \"spearman_p\": 0.0033, \"linear_coeff\": \"degen = 129.5 × F1 - 56.9\", \"key_finding\": \"degeneracy driven by dataset difficulty (entropy ceiling), not model capability\"}, \"conclusion\": \"success\"}, \"exp_e1_signal_routing\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T10:13:34.839Z\", \"updated_at\": \"2026-05-20T10:13:52.098Z\", \"hypothesis\": \"A config-level signal router (RF/LR) can predict the optimal construction signal per config from features (degeneracy_rate, base_f1, oracle_headroom), outperforming always-LP baseline. Router ΔF1 should exceed always-LP ΔF1.\", \"metrics\": {\"n_configs\": 16, \"rf_loo_accuracy\": 0.562, \"router_avg_delta_f1\": 0.39, \"always_lp_delta_f1\": 0.15, \"oracle_delta_f1\": 0.56, \"top_features\": [\"oracle_headroom\", \"degeneracy_rate\", \"base_f1\"], \"label_dist\": {\"lp_selection\": 6, \"none\": 5, \"consensus_theta2n\": 3, \"consensus_lp_weighted\": 1, \"majority_vote\": 1}}, \"conclusion\": \"success\", \"notes\": \"E1 signal routing. RF 56.2% LOO accuracy (below 60% target) but router ΔF1 +0.39pp > always-LP +0.15pp (2.6× improvement, target met). Low accuracy due to small n=16 and class imbalance. D176: appendix-only, not main claim.\"}, \"exp_pareto_diversity_quality\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T09:31:45.421Z\", \"updated_at\": \"2026-05-20T09:31:58.776Z\", \"hypothesis\": \"There exists a Pareto frontier in the diversity (1-degeneracy) vs construction quality (ΔF1) space across temperature configurations. Well-separated temperature mixing (T=0.7+T=1.0) achieves Pareto optimality for both uniform and VC construction, while VC-weighted construction flattens the trade-off slope, reducing the diversity cost of quality.\", \"metrics\": {\"dataset\": \"SciERC\", \"configs\": {\"t07\": {\"one_minus_degen\": 0.777, \"uniform_delta\": 1.81, \"vc_delta\": 1.17, \"pareto\": \"uniform only\"}, \"t08\": {\"one_minus_degen\": 0.819, \"uniform_delta\": 1.25, \"vc_delta\": 1.68, \"pareto\": \"VC only\"}, \"mix_07_10\": {\"one_minus_degen\": 0.83, \"uniform_delta\": 1.43, \"vc_delta\": 1.67, \"pareto\": \"both\"}, \"t10\": {\"one_minus_degen\": 0.877, \"uniform_delta\": 0.75, \"vc_delta\": 1.21, \"pareto\": \"both (highest diversity)\"}, \"mix_08_10\": {\"one_minus_degen\": 0.789, \"uniform_delta\": -0.17, \"vc_delta\": 0.47, \"pareto\": \"dominated\"}}, \"vc_slope_reduction\": \"~50% flatter than uniform\", \"key_insight\": \"well-separated T mixing dual Pareto optimal; close T mixing dominated\"}, \"conclusion\": \"success\", \"notes\": \"A4 Pareto diversity-quality analysis on SciERC. Mix T=0.7+T=1.0 is dual-Pareto optimal (uniform +1.43pp, VC +1.67pp). VC construction flattens trade-off slope ~50% vs uniform — increasing diversity costs less quality. Mix T=0.8+T=1.0 is dominated (close T → higher degeneracy, no construction gain). Confirms DGEC heterogeneous-T finding: ΔT matters, ΔT=0.3 beneficial, ΔT=0.2 harmful. Pareto plot artifact registered.\"}, \"exp_adaptive_sampling_budget\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T09:29:22.761Z\", \"updated_at\": \"2026-05-20T09:29:41.158Z\", \"hypothesis\": \"Confidence-aware adaptive sampling budget allocation (fewer samples for high-confidence instances, full N=8 for low-confidence) can recover nearly all SC F1 gains while saving 40-50% of inference cost, because high-confidence instances already have low diversity and gain nothing from additional samples.\", \"metrics\": {\"model\": \"Qwen3-8B FT\", \"fewnerd\": {\"n_instances\": 37648, \"greedy_f1\": 0.7884, \"uniform_n8_f1\": 0.7819, \"best_adaptive\": \"h1_l8\", \"best_adaptive_f1\": 0.7849, \"best_delta_vs_u8\": \"+0.30pp\", \"sample_savings\": \"43.8%\", \"note\": \"Greedy > U8; adaptive h1/l8 best: greedy for high-conf, N=8 SC for low-conf\"}, \"scierc\": {\"n_instances\": 551, \"greedy_f1\": 0.6592, \"uniform_n8_f1\": 0.6712, \"best_adaptive\": \"top67%_h2_l8\", \"best_adaptive_f1\": 0.6707, \"best_delta_vs_u8\": \"-0.05pp\", \"sample_savings\": \"50.2%\", \"note\": \"U8 > Greedy; top67% h2/l8 saves 50% with negligible loss\"}}, \"conclusion\": \"success\", \"notes\": \"B7 adaptive sampling budget analysis on Qwen3-8B FT. Key findings: (1) FewNERD: greedy already beats uniform N=8 SC (+0.65pp), adaptive h1/l8 is optimal (+0.30pp vs U8, saves 43.8% samples); (2) SciERC: U8 beats greedy (+1.20pp), top67% h2/l8 saves 50% with only -0.05pp loss. Practical implication: confidence-gated sampling can halve inference cost. Artifacts: vc_8b_qwen3_ft_results, sj_8b_qwen3_ft_results (registered by worker).\"}, \"exp_dgec_sj_construction\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T08:37:58.013Z\", \"updated_at\": \"2026-05-20T09:26:30.567Z\", \"hypothesis\": \"SJ-weighted entity construction serves as control for VC — if SJ (soft entity overlap) works as well as VC (exact match consensus), any stronger QE signal suffices for construction; if VC specifically outperforms SJ, exact-match consensus has a unique advantage over soft similarity for entity-level selection.\", \"metrics\": {\"total_configs\": 26, \"significant_positive\": 1, \"significant_negative\": 15, \"not_significant\": 10, \"best_config\": \"scierc/72b/zs +2.0pp p=0.001\", \"worst_config\": \"fewnerd/8b_qwen3/ft mean -1.48pp all seeds p=1.0\", \"qwen3_8b_ft_supplement\": {\"configs\": 9, \"sig+\": 0, \"sig-\": 6, \"ns\": 3, \"fewnerd_mean_delta\": -1.48, \"scierc_mean_delta\": -0.4, \"conll_mean_delta\": -0.5, \"note\": \"SJ fully negative on Qwen3-8B FT — consistent with Qwen2.5-7B FT pattern\"}, \"m030_all_passed\": true}, \"notes\": \"COMPLETE (26 configs). SJ-weighted construction: 1 sig+ / 15 sig- / 10 ns. Qwen3-8B FT supplement (9 configs): 0+/6-/3ns — fully negative, consistent with 7B FT pattern. FewNERD -1.48pp mean (all seeds p=1.0). Definitively answers control question: NOT any stronger QE signal works for construction. SJ introduces noise at entity level. Only exception: SciERC 72B ZS (lowest precision, lowest degeneracy). Closed per D170/D171.\", \"conclusion\": \"negative\"}, \"exp_dgec_vc_construction\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T08:37:55.968Z\", \"updated_at\": \"2026-05-20T09:26:29.776Z\", \"hypothesis\": \"VC-weighted entity construction outperforms greedy and LP-weighted construction across configs because Vote Count is a more direct quality estimator for structured outputs — it measures exact-match consensus without relying on model-internal log probabilities. Especially effective in high-degeneracy regimes where LP compression makes LP-weighting uninformative.\", \"metrics\": {\"total_configs\": 28, \"significant_positive\": 9, \"significant_negative\": 10, \"not_significant\": 9, \"by_dataset\": {\"fewnerd\": {\"configs\": 11, \"sig+\": 5, \"sig-\": 5, \"ns\": 1, \"mean_delta_pp\": -0.12}, \"wnut17\": {\"configs\": 3, \"sig+\": 2, \"sig-\": 0, \"ns\": 1, \"mean_delta_pp\": 0.92}, \"scierc\": {\"configs\": 7, \"sig+\": 2, \"sig-\": 0, \"ns\": 5, \"mean_delta_pp\": 0.62}, \"conll\": {\"configs\": 7, \"sig+\": 0, \"sig-\": 5, \"ns\": 2, \"mean_delta_pp\": -0.33}}, \"qwen3_8b_ft_supplement\": {\"configs\": 9, \"sig+\": 3, \"sig-\": 3, \"ns\": 3, \"best\": \"SciERC s42 +1.40pp p=0.017\", \"worst\": \"CoNLL s456 -0.54pp p=0.998\", \"note\": \"VC inconsistent on LP-success configs; seed-dependent on FewNERD; CoNLL all negative due to high degeneracy\"}, \"m030_all_passed\": true}, \"notes\": \"COMPLETE (28 configs). VC-weighted construction: 9 sig+ / 10 sig- / 9 ns. Qwen3-8B FT supplement (9 configs): 3+/3-/3ns — VC inconsistent even on LP-success configs. SciERC s42 best (+1.40pp) but cross-seed unstable. CoNLL all negative (high degeneracy). WNUT17/SciERC lean positive but not robust. Key answer: VC does NOT reliably improve where LP already works — seed-dependent, dataset-dependent. DGEC unified method goal (70-80% configs) unreachable at 32% (9/28). Closed per D170/D171.\", \"conclusion\": \"negative\"}, \"exp_dgec_heterogeneous_t\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T08:37:59.963Z\", \"updated_at\": \"2026-05-20T08:49:58.009Z\", \"hypothesis\": \"Mixing samples from T=0.7 and T=1.0 significantly reduces degeneracy compared to single-T sampling (by breaking temperature-induced mode collapse), enabling entity construction to achieve significant ΔF1 improvement even in configs where single-T construction was n.s. due to high degeneracy.\", \"metrics\": {\"dataset\": \"SciERC\", \"n_instances\": 529, \"t07_degen\": 0.2231, \"t10_degen\": 0.1235, \"mixed_degen\": 0.1701, \"mixed_uniform_f1\": 0.6584, \"mixed_vc_f1\": 0.6609, \"cross_pool_uniform_delta\": \"+0.006 (1/3 seeds sig)\", \"cross_pool_vc_delta\": \"+0.004 (1/3 seeds sig)\", \"t08_t10_result\": \"harmful (degen increased)\", \"conclusion_preliminary\": \"partially_supported\"}, \"notes\": \"Hypothesis partially supported. T=0.7+T=1.0 mixed pool reduces degen (22.3%→17.0%) and improves construction (VC 3/3 seeds sig vs greedy), but cross-pool comparison (mixed vs T=1.0 alone) only 1/3 seeds significant. T gap matters: ΔT=0.2 (T=0.8+T=1.0) harmful, ΔT=0.3 (T=0.7+T=1.0) beneficial. VC weighting confirmed cross-T compatible. Awaiting Director conclusion classification.\"}, \"exp_qwen25_32b_fewnerd\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-19T06:19:25.428Z\", \"updated_at\": \"2026-05-20T07:15:23.641Z\", \"hypothesis\": \"Scaling from Qwen3-8B to Qwen2.5-32B-Instruct with QLoRA fine-tuning on FewNERD will improve structured self-consistency IE performance due to stronger base model capabilities in instruction following and entity recognition.\", \"server\": \"autodl-5090\", \"gpu\": \"cuda:0,cuda:1,cuda:2,cuda:3\", \"account\": \"root\", \"reproduce\": {\"server\": \"autodl-5090\", \"gpu\": \"cuda:0,cuda:1,cuda:2,cuda:3\", \"started_at\": \"2026-05-19T06:47:41.246Z\"}, \"notes\": \"2026-05-19 11:36 UTC: step 2177/41180 (5.3%), loss 0.0663, ~2.44s/it, ETA ~26h. checkpoint-2000 saved. PID 804438, 4×5090 87-100% util.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0,1,2,3 FORCE_TORCHRUN=1 NNODES=1 NPROC_PER_NODE=4 llamafactory-cli train /root/autodl-tmp/struct_self_consist_ie/train_config_qwen25_32b_fewnerd_s42.yaml\", \"server\": \"autodl-5090\", \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/data/fewnerd/llmfactory_train.json\", \"data_count\": 131767, \"model_name\": \"Qwen2.5-32B-Instruct\", \"seed\": 42, \"method\": \"QLoRA-4bit-nf4 (rank=32, alpha=64, target=all)\", \"output_dir\": \"/root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen25-32b-fewnerd-qlora-s42\", \"config_path\": \"/root/autodl-tmp/struct_self_consist_ie/train_config_qwen25_32b_fewnerd_s42.yaml\", \"epochs\": 5, \"effective_batch_size\": 16, \"lr\": \"2e-4\", \"gpu_ids\": [\"cuda:0\", \"cuda:1\", \"cuda:2\", \"cuda:3\"], \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/logs/train_qwen25_32b_fewnerd_s42.log\", \"pid\": 804438}, \"metrics\": {\"training_progress\": \"56.9% (23448/41180, checked 07:14 UTC)\", \"epoch\": \"2.84/5.0\", \"loss\": 0.027, \"speed\": \"~2.50s/step\", \"eta\": \"~05-20 20:00-22:00 UTC (train 12h30m remaining + eval pauses)\"}}, \"exp_qwen25_7b_fewnerd\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T06:41:43.121Z\", \"updated_at\": \"2026-05-20T05:45:54.613Z\", \"hypothesis\": \"Qwen2.5-7B QLoRA fine-tuned on FewNERD will produce structurally diverse samples enabling self-consistency-based entity extraction with meaningful LP-weighted consensus signals, comparable to the 14B model but with lower compute cost.\", \"spec\": {\"server\": \"autodl-5090-c\", \"gpu_ids\": [\"cuda:2\", \"cuda:3\"], \"command\": \"nohup bash run_fewnerd_qwen25_7b_pipeline.sh > logs/pipeline_qwen25_7b_fewnerd.log 2>&1 &\", \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/data/fewnerd/llmfactory_train.json\", \"data_count\": 131767, \"model_name\": \"Qwen2.5-7B-Instruct\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen25-7b-fewnerd-qlora-s42\", \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/logs/pipeline_qwen25_7b_fewnerd.log\", \"training_config\": \"train_config_qwen25_7b_fewnerd_s42.yaml\", \"export_config\": \"export_config_qwen25_7b_fewnerd.yaml\", \"pipeline_script\": \"run_fewnerd_qwen25_7b_pipeline.sh\", \"method\": \"QLoRA 4-bit nf4, rank=32, alpha=64, 5 epochs, lr=2e-4, effective_batch=32\", \"pipeline_phases\": \"train -> export/merge -> 3-seed N=8 inference (42/123/456) -> signal analysis -> entity construction\"}, \"notes\": \"2026-05-19 11:36 UTC: step 138/20590 (0.7%), ~2.34s/it, ETA ~13.3h. Pipeline PID 71837, llamafactory PID 71844. cuda:2,3 98-100% util. Cron registered on pipeline PID.\", \"server\": \"autodl-5090-c\", \"gpu\": \"cuda:2,cuda:3\", \"metrics\": {\"3seed_mean\": {\"lp_rho\": 0.346, \"lp_rho_std\": 0.021, \"sj_rho\": 0.388, \"sj_rho_std\": 0.029, \"vc_rho\": 0.404, \"vc_rho_std\": 0.01, \"degen_pct\": 31.7, \"degen_std\": 0.9, \"greedy_f1\": 0.784, \"greedy_f1_std\": 0.001, \"oracle_f1\": 0.876, \"oracle_f1_std\": 0.003, \"construction_lp_delta_pp\": -0.11, \"construction_lp_delta_std\": 0.25}, \"per_seed\": {\"seed42\": {\"lp_rho\": 0.3221, \"sj_rho\": 0.3554, \"vc_rho\": 0.393, \"degen_pct\": 31.1, \"greedy_f1\": 0.7851, \"oracle_f1\": 0.8718, \"construction_lp_delta_pp\": -0.4, \"bootstrap_p\": 1, \"bootstrap_ci\": [-0.53, -0.26], \"cohens_d\": -0.0319}, \"seed123\": {\"lp_rho\": 0.3538, \"sj_rho\": 0.3979, \"vc_rho\": 0.4067, \"degen_pct\": 32.8, \"greedy_f1\": 0.785, \"oracle_f1\": 0.8777, \"construction_lp_delta_pp\": -0.03, \"bootstrap_p\": 0.651}, \"seed456\": {\"lp_rho\": 0.3629, \"sj_rho\": 0.4105, \"vc_rho\": 0.4118, \"degen_pct\": 31.3, \"greedy_f1\": 0.7825, \"oracle_f1\": 0.8771, \"construction_lp_delta_pp\": 0.09, \"bootstrap_p\": 0.168}}, \"construction_significant\": false}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-20T05:45:54.613Z\"}, \"exp_qwen25_72b_fewshot\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T15:59:44.340Z\", \"updated_at\": \"2026-05-20T00:54:59.032Z\", \"hypothesis\": \"Few-shot prompting improves base NER F1 and LP signal quality, enabling LP-weighted construction to outperform greedy selection via dual-gating (sufficient LP ρ + low degeneracy).\", \"parent\": \"exp_qwen25_72b_zeroshot\", \"server\": \"autodl-5090-b\", \"gpu\": \"cuda:0,cuda:1,cuda:2,cuda:3\", \"account\": \"root\", \"reproduce\": {\"server\": \"autodl-5090-b\", \"gpu\": \"cuda:0,cuda:1,cuda:2,cuda:3\", \"started_at\": \"2026-05-19T16:22:20.071Z\", \"finished_at\": \"2026-05-20T00:47:36.445Z\", \"training_hours\": 8.42}, \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && CUDA_VISIBLE_DEVICES=0,1,2,3 python code/fewshot_inference_72b.py --datasets scierc conll2003 fewnerd --output-dir output/72b_fewshot --seed 42\\\"\", \"server\": \"autodl-5090-b\", \"gpu\": [\"cuda:0\", \"cuda:1\", \"cuda:2\", \"cuda:3\"], \"pid\": 131293, \"log_path\": \"~/runs/struct_self_consist_ie/exp_qwen25_72b_fewshot.log\", \"submitted_at\": \"2026-05-19T16:25:57.711Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/{scierc,conll2003,fewnerd}\", \"data_count\": 41652, \"model_name\": \"Qwen2.5-72B-Instruct-AWQ\", \"seed\": 42, \"gpu_ids\": [\"cuda:0\", \"cuda:1\", \"cuda:2\", \"cuda:3\"], \"checkpoint_source\": \"Qwen2.5-72B-Instruct-AWQ (base model, no fine-tuning)\", \"eval_data\": \"SciERC + CoNLL-2003 + FewNERD test sets\", \"wall_clock_seconds\": 30541.3, \"gpu_hours\": 33.93}, \"metrics\": {\"scierc\": {\"lp_rho\": 0.06, \"sj_rho\": 0.293, \"fk_rho\": 0.301, \"vc_rho\": 0.258, \"em_rho\": 0.205, \"degen_pct\": 16.6, \"greedy_f1\": 0.461, \"oracle_f1\": 0.604, \"construction_f1\": 0.461, \"construction_delta_pp\": -0.08, \"bootstrap_p\": 0.544}, \"conll\": {\"lp_rho\": 0.106, \"sj_rho\": 0.442, \"fk_rho\": 0.451, \"vc_rho\": 0.426, \"em_rho\": 0.403, \"degen_pct\": 70, \"greedy_f1\": 0.745, \"oracle_f1\": 0.796, \"construction_f1\": 0.745, \"construction_delta_pp\": 0.03, \"bootstrap_p\": 0.417}, \"fewnerd\": {\"lp_rho\": 0.161, \"sj_rho\": 0.345, \"fk_rho\": 0.327, \"vc_rho\": 0.41, \"em_rho\": 0.302, \"degen_pct\": 45.2, \"greedy_f1\": 0.619, \"oracle_f1\": 0.702, \"construction_f1\": 0.619, \"construction_delta_pp\": 0.02, \"bootstrap_p\": 0.401}}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-20T00:47:43.131229+00:00\"}]}, \"conclusion\": \"negative\", \"checkpoint_path\": \"output/72b_fewshot/ + output/72b_fewshot_signals/\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_qwen25_72b_fewshot.log\", \"completed_at\": \"2026-05-20T00:54:59.032Z\"}, \"exp_qwen25_72b_zeroshot\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-19T06:19:28.597Z\", \"updated_at\": \"2026-05-19T16:23:10.481Z\", \"hypothesis\": \"A larger zero-shot model (72B) will show higher greedy F1 and wider oracle-greedy gap than fine-tuned smaller models, because increased capacity enables more diverse valid extractions per stochastic sample, making self-consistency signals (SJ, FK, VC, EM) more informative for quality estimation.\", \"server\": \"autodl-5090-b\", \"gpu\": \"cuda:0,cuda:1,cuda:2,cuda:3\", \"account\": \"root\", \"reproduce\": {\"server\": \"autodl-5090-b\", \"gpu\": \"cuda:0,cuda:1,cuda:2,cuda:3\", \"started_at\": \"2026-05-19T06:47:42.658Z\", \"finished_at\": \"2026-05-19T14:14:58.577Z\", \"training_hours\": 7.45}, \"notes\": \"2026-05-19 12:47 UTC: RECOVERED from false-positive startup recovery failure. 289848/301184 prompts (96.2%). SciERC ✅ (551) CoNLL ✅ (3453) FewNERD ~96%. ETA ~10-15min. PID 59040, 4×5090 100% util. Cron registered.\", \"failure_reason\": \"FALSE POSITIVE — cron误判。实验实际成功完成（3个数据集全部处理完毕）。\", \"completed_at\": \"2026-05-19T12:44:26.198Z\", \"extra\": {\"previous_failure\": {\"conclusion\": \"failed\", \"notes\": \"2026-05-19 11:36 UTC: 69.8% complete (210352/301184 prompts). SciERC ✅ CoNLL ✅ FewNERD ~66%. ETA ~1h15m. vLLM PID 59040, 4×5090 100% util.\"}, \"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-19T14:15:08.634709+00:00\"}]}, \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0,1,2,3 python code/zeroshot_inference_72b.py --datasets scierc conll2003 fewnerd --output-dir output/72b_zeroshot --seed 42\", \"server\": \"autodl-5090-b\", \"data_path\": \"data/{scierc,conll2003,fewnerd}\", \"data_count\": 41630, \"model_name\": \"Qwen2.5-72B-Instruct-AWQ\", \"seed\": 42, \"gpu_ids\": [\"cuda:0\", \"cuda:1\", \"cuda:2\", \"cuda:3\"], \"pid\": 59040}, \"conclusion\": \"negative\", \"metrics\": {\"scierc\": {\"greedy_f1\": 0.3993, \"lp_rho\": 0.081, \"vc_rho\": 0.277, \"sj_rho\": 0.217, \"degen_rate\": 0.21, \"construction_lp_weighted_f1\": 0.4146, \"construction_lp_delta_pp\": 1.53, \"construction_uniform_f1\": 0.3941, \"construction_uniform_delta_pp\": -0.52, \"lp_selection_f1\": 0.3984, \"majority_vote_f1\": 0.4132, \"oracle_f1\": 0.5489, \"bootstrap_p\": 0.0082, \"bootstrap_ci_lower\": 0.0025, \"bootstrap_ci_upper\": 0.0282, \"cohens_d\": 0.1027, \"n_instances\": 529, \"non_degen_delta_pp\": 1.65, \"non_degen_p\": 0.0069}, \"conll2003\": {\"greedy_f1\": 0.712, \"lp_rho\": -0.002, \"vc_rho\": 0.297, \"sj_rho\": 0.304, \"degen_rate\": 0.677, \"construction_lp_weighted_f1\": 0.7083, \"construction_lp_delta_pp\": -0.37, \"construction_uniform_f1\": 0.7028, \"construction_uniform_delta_pp\": -0.92, \"lp_selection_f1\": 0.708, \"majority_vote_f1\": 0.7034, \"oracle_f1\": 0.7651}, \"fewnerd\": {\"greedy_f1\": 0.6281, \"lp_rho\": 0.119, \"vc_rho\": 0.416, \"sj_rho\": 0.345, \"degen_rate\": 0.462, \"construction_lp_weighted_f1\": 0.6261, \"construction_lp_delta_pp\": -0.2, \"construction_uniform_f1\": 0.6112, \"construction_uniform_delta_pp\": -1.7, \"lp_selection_f1\": 0.6241, \"lp_selection_delta_pp\": -0.4, \"majority_vote_f1\": 0.6262, \"oracle_f1\": 0.7072}}}, \"exp_wnut17_qwen25_7b\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T06:19:33.960Z\", \"updated_at\": \"2026-05-19T11:49:07.313Z\", \"hypothesis\": \"The correlation-selection gap extends to noisy social media NER (WNUT-17). Unlike formal-domain datasets (SciERC/CoNLL/FewNERD), WNUT-17 has higher surface-level noise which may affect structural signal reliability differently. This tests domain generalization of the diagnostic framework.\", \"server\": \"autodl-5090-c\", \"gpu\": \"cuda:2,cuda:3\", \"account\": \"root\", \"reproduce\": {\"server\": \"autodl-5090-c\", \"gpu\": \"cuda:2,cuda:3\", \"started_at\": \"2026-05-19T06:47:45.220Z\"}, \"spec\": {\"server\": \"autodl-5090-c\", \"gpu_ids\": [\"cuda:2\", \"cuda:3\"], \"command\": \"bash wait_and_train.sh (screen: exp_wnut17_7b)\", \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/data/wnut17/llmfactory_train.json\", \"data_count\": 3404, \"model_name\": \"Qwen2.5-7B-Instruct\", \"seed\": 42, \"training_config\": \"train_config_qwen25_7b_wnut17_s42.yaml\", \"method\": \"QLoRA 4-bit (bnb nf4), rank=32, alpha=64, all targets\", \"gpus\": \"cuda:2,3 (2x5090)\", \"epochs\": 5, \"effective_batch_size\": 32, \"pipeline\": \"train → export → 3-seed inference (N=8, T=1.0) → signal analysis → entity construction\", \"checkpoint_source\": \"self-trained on WNUT-17\", \"eval_data\": \"WNUT-17 test set\", \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen25-7b-wnut17-qlora-s42\", \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/logs/exp_wnut17_7b_pipeline.log\"}, \"conclusion\": \"negative\", \"metrics\": {\"seed42\": {\"greedy_f1\": 0.4524, \"construction_f1\": 0.4439, \"construction_delta_pp\": -0.84, \"construction_p\": 0.95}, \"seed123\": {\"greedy_f1\": 0.4518, \"construction_f1\": 0.4579, \"construction_delta_pp\": 0.61, \"construction_p\": 0.08}, \"seed456\": {\"greedy_f1\": 0.4526, \"construction_f1\": 0.4583, \"construction_delta_pp\": 0.57, \"construction_p\": 0.12}, \"oracle_headroom_pp\": \"6.3-9.2\"}, \"completed_at\": \"2026-05-19T11:22:56.623Z\"}, \"exp_llama_fewnerd_inference\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T02:18:49.938Z\", \"updated_at\": \"2026-05-19T03:15:04.486Z\", \"hypothesis\": \"LLaMA-3.1-8B fine-tuned on FewNERD shows the same structured self-consistency phenomena (degeneracy, LP-F1 alignment, signal ranking) as Qwen models, providing cross-model generalization evidence. 3-seed inference (42/123/456) for statistical robustness.\", \"parent\": \"exp_llama_fewnerd_lora\", \"spec\": {\"command\": \"bash code/run_llama_fewnerd_inference.sh\", \"server\": \"autodl-5090\", \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/data/fewnerd/\", \"data_count\": 37648, \"model_name\": \"LLaMA-3.1-8B-FewNERD-LoRA-merged\", \"seed\": \"42,123,456\", \"checkpoint_source\": \"exp_llama_fewnerd_lora\", \"eval_data\": \"FewNERD test set\", \"checkpoint_path\": \"checkpoints/llama3.1-8b-fewnerd-merged/\", \"log_path\": \"logs/llama_fewnerd_inference.log\"}, \"conclusion\": \"success\", \"metrics\": {\"3seed_mean\": {\"greedy_f1\": 0.7842, \"oracle_f1\": 0.8843, \"headroom_pp\": 10.01, \"degeneracy_pct\": 23.36, \"lp_delta_pp\": 0.36, \"dgs_delta_pp\": -0.35}, \"seed_42\": {\"greedy_f1\": 0.7841, \"oracle_f1\": 0.8854, \"degen\": 27.32}, \"seed_123\": {\"greedy_f1\": 0.784, \"oracle_f1\": 0.8839, \"degen\": 24.63}, \"seed_456\": {\"greedy_f1\": 0.7844, \"oracle_f1\": 0.8835, \"degen\": 18.13}, \"signal_ranking\": \"LP (+0.36pp) > SJ (-0.52) > FK (-0.53) > EM (-1.02) > VC (-2.39)\", \"lp_only_positive\": true, \"n_instances_gold_filtered\": 32565}, \"completed_at\": \"2026-05-19T03:15:04.486Z\"}, \"exp_entity_construction\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T02:00:12.074Z\", \"updated_at\": \"2026-05-19T02:40:17.571Z\", \"hypothesis\": \"Entity-level majority vote construction is the correct self-consistency analogy for structured IE: instead of selecting the best instance-level output, assemble a better output from entity-level consensus across N samples. Construction should outperform both greedy and best-of-N selection.\", \"conclusion\": \"success\", \"spec\": {\"command\": \"python code/entity_construction_fair.py\", \"server\": \"autodl-5090\", \"data_path\": \"output/*/samples_*.json\", \"data_count\": 3, \"model_name\": \"analysis_cpu\", \"seed\": 42, \"checkpoint_path\": \"output/entity_construction_fair/\", \"log_path\": \"output/entity_construction_fair/\"}, \"completed_at\": \"2026-05-19T02:15:19.616Z\", \"metrics\": {\"n16_fair_cv\": {\"scierc_ner\": {\"cv_uniform_delta\": \"+1.35pp\", \"p_value\": 0.018, \"significant\": true}, \"conll_ner\": {\"cv_uniform_delta\": \"+0.10pp\", \"p_value\": 0.303, \"significant\": false}, \"fewnerd_ner\": {\"cv_uniform_delta\": \"+1.32pp\", \"p_value\": 0, \"significant\": true}, \"scierc_re\": {\"cv_uniform_delta\": \"+1.69pp\", \"p_value\": 0.049, \"significant\": true}}, \"n8_fair_cv\": {\"scierc_ner\": {\"uniform_confirm\": \"+1.54pp (p=0.023, sig)\", \"lp_weighted_confirm\": \"+1.67pp (p=0.004, sig)\", \"cv_uniform\": \"+1.12pp (p=0.057, borderline)\"}, \"conll_ner\": {\"cv_uniform\": \"-0.39pp (p=0.963, not sig)\"}, \"fewnerd_ner\": {\"lp_weighted_cv\": \"+0.88pp (p=0.000, sig)\", \"uniform_cv\": \"+0.32pp (p=0.003, sig)\"}}, \"adaptive_combination\": \"INVALIDATED - gold label leakage confirmed\", \"note\": \"5-fold CV, bootstrap B=10000, paired one-sided\"}}, \"exp_lp_alignment_gating\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T02:00:16.520Z\", \"updated_at\": \"2026-05-19T02:15:48.197Z\", \"hypothesis\": \"Within-instance LP-F1 alignment score (adjusted by valid_ratio for degeneracy) can automatically gate whether LP selection should be applied to a dataset. A small probe sample (50-100 instances) suffices for a stable gating decision.\", \"conclusion\": \"success\", \"spec\": {\"command\": \"python code/lp_alignment_gated_selection.py\", \"server\": \"autodl-5090\", \"data_path\": \"output/*/samples_*.json\", \"data_count\": 3, \"model_name\": \"analysis_cpu\", \"seed\": 42, \"checkpoint_path\": \"output/prescriptive_analysis/\", \"log_path\": \"output/prescriptive_analysis/\"}, \"completed_at\": \"2026-05-19T02:15:23.716Z\", \"metrics\": {\"adjusted_score\": \"mean_rho * valid_ratio\", \"threshold\": 0.3, \"accuracy\": \"3/3 datasets correct\", \"robust_range\": \"0.2-0.4\"}}, \"exp_selective_prediction\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T02:00:13.989Z\", \"updated_at\": \"2026-05-19T02:15:46.588Z\", \"hypothesis\": \"QE signals (especially voting_confidence) can drive practical selective prediction: filtering out low-confidence instances yields significant F1 improvement on retained instances, enabling human-AI collaboration for structured IE.\", \"conclusion\": \"success\", \"spec\": {\"command\": \"python code/selective_prediction.py\", \"server\": \"autodl-5090\", \"data_path\": \"output/*/samples_*.json\", \"data_count\": 3, \"model_name\": \"analysis_cpu\", \"seed\": 42, \"checkpoint_path\": \"output/prescriptive_analysis/\", \"log_path\": \"output/prescriptive_analysis/\"}, \"completed_at\": \"2026-05-19T02:15:21.704Z\", \"metrics\": {\"vc_best_signal\": true, \"f1_at_80pct_coverage\": {\"scierc\": \"+5.0pp\", \"conll\": \"+8.4pp\", \"fewnerd\": \"+6.2pp\"}, \"precision_coverage_curves\": \"output/prescriptive_analysis/fig_selective_prediction.pdf\"}}, \"exp_llama_fewnerd_lora\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T13:20:55.859Z\", \"updated_at\": \"2026-05-19T01:08:20.832Z\", \"hypothesis\": \"LLaMA-based model with LoRA fine-tuning on Few-NERD can provide a second model family (beyond Qwen) for cross-model generalization evidence of structured self-consistency phenomena in NER\", \"spec\": {\"command\": \"llamafactory-cli train train_config_llama_fewnerd.yaml\", \"server\": \"autodl-5090\", \"gpu\": \"cuda:1\", \"pid\": 137865, \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/data/fewnerd\", \"data_count\": -1, \"model_name\": \"LLaMA-Few-NERD-LoRA\", \"seed\": 42, \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/logs/llama_fewnerd_train.log\", \"run_script\": \"run_llama_fewnerd_train_single_gpu.sh\", \"tmux_session\": \"llama_fewnerd\", \"note\": \"Retroactively registered - data_count unknown, seed assumed 42\"}, \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/checkpoints/llama3.1-8b-fewnerd-lora\", \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/logs/llama_fewnerd_train.log\", \"conclusion\": \"success\", \"metrics\": {\"epoch\": 3, \"train_loss\": 0.0516, \"eval_loss\": 0.0323, \"train_runtime_hours\": 15.35, \"total_steps\": 24708, \"final_checkpoint\": \"checkpoint-24708\", \"adapter_size_mb\": 320}, \"completed_at\": \"2026-05-19T01:08:20.832Z\"}, \"hidden_state_probe_conll_full\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T12:57:45.711Z\", \"updated_at\": \"2026-05-19T00:30:18.272Z\", \"conclusion\": \"killed\", \"notes\": \"Not in D154 Dual Contribution framing\", \"completed_at\": \"2026-05-19T00:30:18.272Z\"}, \"hidden_state_probe_conll_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T12:35:05.317Z\", \"updated_at\": \"2026-05-19T00:30:16.471Z\", \"conclusion\": \"killed\", \"notes\": \"Not in D154 Dual Contribution framing\", \"completed_at\": \"2026-05-19T00:30:16.471Z\"}, \"exp_031_fewnerd_t12\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T20:04:12.040Z\", \"updated_at\": \"2026-05-19T00:30:14.652Z\", \"hypothesis\": \"FewNERD T=1.2 temperature ablation: test if higher temperature reduces degeneracy on FewNERD as observed on SciERC\", \"conclusion\": \"killed\", \"failure_reason\": \"数据不可用于论文：测试集(37648 vs T=1.0的5000)、N(8 vs 16)、分析管道(MVP pilot vs 5-signal)三重不一致。Director决定不重跑(DDL约束+非核心claim)。\", \"notes\": \"T=1.2 ablation not in paper scope, SciERC T=1.2 sufficient\", \"completed_at\": \"2026-05-19T00:30:14.652Z\"}, \"exp_030_conll_t12\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T20:24:47.839Z\", \"updated_at\": \"2026-05-19T00:30:12.698Z\", \"hypothesis\": \"CoNLL T=1.2 temperature ablation: test if higher temperature reduces degeneracy on CoNLL as observed on SciERC\", \"conclusion\": \"killed\", \"failure_reason\": \"数据不可用于论文：N不一致(N=8 vs T=1.0基准的N=16)。Director决定不重跑——SciERC T消融(T=0.5/0.8/1.0/1.2, 551inst, N=8)已够用，论文温度消融用SciERC单数据集。\", \"notes\": \"T=1.2 ablation not in paper scope, SciERC T=1.2 sufficient\", \"completed_at\": \"2026-05-19T00:30:12.699Z\"}, \"mbr_pilot\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T17:56:06.462Z\", \"updated_at\": \"2026-05-19T00:29:39.285Z\", \"conclusion\": \"killed\", \"notes\": \"MBR tested negative as one of 6 methods, stale entry\", \"completed_at\": \"2026-05-19T00:29:39.285Z\"}, \"dgs_pilot\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T17:56:04.572Z\", \"updated_at\": \"2026-05-19T00:29:37.275Z\", \"hypothesis\": \"Degeneracy-Gated Selection (DGS) validates Two-Condition Theory: using degeneracy rate as gating mechanism to switch between greedy (degenerate) and LP selection (non-degenerate), the improvement direction should follow a monotonic gradient — low degeneracy yields positive delta, high degeneracy yields negative delta.\", \"conclusion\": \"killed\", \"notes\": \"D154: DGS demoted to explored heuristic, cross-model direction contradiction (D152)\", \"completed_at\": \"2026-05-19T00:29:37.275Z\"}, \"exp_fewnerd_s789_n8\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T23:17:34.011Z\", \"updated_at\": \"2026-05-18T23:18:28.125Z\", \"hypothesis\": \"FewNERD seed789 (4th seed) for statistical CI strengthening: 4-seed protocol provides tighter confidence intervals on LP selection gain and DGS effectiveness in low-degeneracy regime.\", \"parent\": \"exp_029a\", \"spec\": {\"command\": \"python code/analyze_fewnerd_s789.py\", \"server\": \"autodl-5090\", \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/fewnerd_seed789_merged/samples.jsonl\", \"data_count\": 37648, \"model_name\": \"Qwen3-8B (ft_002_v2)\", \"seed\": 789, \"checkpoint_source\": \"exp_021 shards\", \"eval_data\": \"FewNERD test (37648 instances, 32565 gold-filtered)\", \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/fewnerd_seed789_merged/\", \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/fewnerd_seed789_merged/run.log\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T23:18:17.902Z\", \"metrics\": {\"greedy_f1\": 0.7478, \"oracle_f1\": 0.8714, \"headroom_pp\": 12.37, \"degen_rate\": 0.1177, \"degen_rate_source\": \"unified_metrics_constant_f1_gold_filtered\", \"instance_count\": 37648, \"n_valid\": 32565, \"lp_sel_f1\": 0.7614, \"lp_delta_pp\": 1.36, \"lp_rho_global\": 0.1788, \"lp_rho_cond\": 0.176, \"dgs_f1\": 0.7621, \"dgs_delta_pp\": 1.43, \"dgs_vs_lp_pp\": 0.07, \"best_signal\": \"LP\", \"four_seed_mean_greedy\": 0.7481, \"four_seed_mean_lp_delta_pp\": 1.38, \"four_seed_lp_delta_ci95\": [1.32, 1.44]}}, \"exp_026_t12_seed456\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T22:05:43.694Z\", \"updated_at\": \"2026-05-18T22:07:24.547Z\", \"hypothesis\": \"Temperature ablation (T=1.2, seed=456) of Qwen3-8B SciERC N=8 SCS inference to study temperature sensitivity of structural consistency signals.\", \"spec\": {\"command\": \"python scs_inference.py --dataset scierc --seed 456 --n_samples 8 --temperature 1.2\", \"server\": \"autodl-5090\", \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/data/scierc\", \"data_count\": 551, \"model_name\": \"Qwen3-8B\", \"seed\": 456, \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_026_t12_seed456\", \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_026_t12_seed456.log\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T22:07:05.941Z\", \"metrics\": {\"ner_greedy_f1\": 0.6637, \"ner_oracle_f1\": 0.7821, \"rho_sj_ner\": 0.3995, \"sample_f1_pct_zero\": 14.08, \"instance_count\": 551, \"n_valid\": 529}}, \"exp_026_t12_seed123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T22:05:42.754Z\", \"updated_at\": \"2026-05-18T22:07:23.135Z\", \"hypothesis\": \"Temperature ablation (T=1.2, seed=123) of Qwen3-8B SciERC N=8 SCS inference to study temperature sensitivity of structural consistency signals.\", \"spec\": {\"command\": \"python scs_inference.py --dataset scierc --seed 123 --n_samples 8 --temperature 1.2\", \"server\": \"autodl-5090\", \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/data/scierc\", \"data_count\": 551, \"model_name\": \"Qwen3-8B\", \"seed\": 123, \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_026_t12_seed123\", \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_026_t12_seed123.log\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T22:07:04.119Z\", \"metrics\": {\"ner_greedy_f1\": 0.6595, \"ner_oracle_f1\": 0.7895, \"rho_sj_ner\": 0.359, \"sample_f1_pct_zero\": 13.99, \"instance_count\": 551, \"n_valid\": 529}}, \"exp_026_t10_seed456\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T22:05:41.840Z\", \"updated_at\": \"2026-05-18T22:07:21.767Z\", \"hypothesis\": \"Temperature ablation (T=1.0, seed=456) of Qwen3-8B SciERC N=8 SCS inference to study temperature sensitivity of structural consistency signals.\", \"spec\": {\"command\": \"python scs_inference.py --dataset scierc --seed 456 --n_samples 8 --temperature 1.0\", \"server\": \"autodl-5090\", \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/data/scierc\", \"data_count\": 551, \"model_name\": \"Qwen3-8B\", \"seed\": 456, \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_026_t10_seed456\", \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_026_t10_seed456.log\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T22:07:02.272Z\", \"metrics\": {\"ner_greedy_f1\": 0.6621, \"ner_oracle_f1\": 0.7754, \"rho_sj_ner\": 0.3921, \"sample_f1_pct_zero\": 12.97, \"instance_count\": 551, \"n_valid\": 529}}, \"exp_026_t10_seed123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T22:05:40.599Z\", \"updated_at\": \"2026-05-18T22:07:20.459Z\", \"hypothesis\": \"Temperature ablation (T=1.0, seed=123) of Qwen3-8B SciERC N=8 SCS inference to study temperature sensitivity of structural consistency signals.\", \"spec\": {\"command\": \"python scs_inference.py --dataset scierc --seed 123 --n_samples 8 --temperature 1.0\", \"server\": \"autodl-5090\", \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/data/scierc\", \"data_count\": 551, \"model_name\": \"Qwen3-8B\", \"seed\": 123, \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_026_t10_seed123\", \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_026_t10_seed123.log\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T22:07:00.430Z\", \"metrics\": {\"ner_greedy_f1\": 0.6633, \"ner_oracle_f1\": 0.7777, \"rho_sj_ner\": 0.3809, \"sample_f1_pct_zero\": 12.59, \"instance_count\": 551, \"n_valid\": 529}}, \"exp_026_t10_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T22:05:39.473Z\", \"updated_at\": \"2026-05-18T22:07:19.035Z\", \"hypothesis\": \"Temperature ablation (T=1.0, seed=42) of Qwen3-8B SciERC N=8 SCS inference to study temperature sensitivity of structural consistency signals.\", \"spec\": {\"command\": \"python scs_inference.py --dataset scierc --seed 42 --n_samples 8 --temperature 1.0\", \"server\": \"autodl-5090\", \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/data/scierc\", \"data_count\": 551, \"model_name\": \"Qwen3-8B\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_026_t10_seed42\", \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_026_t10_seed42.log\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T22:06:58.573Z\", \"metrics\": {\"ner_greedy_f1\": 0.6617, \"ner_oracle_f1\": 0.7798, \"rho_sj_ner\": 0.3598, \"sample_f1_pct_zero\": 12.9, \"instance_count\": 551, \"n_valid\": 529}}, \"exp_026_t08_seed456\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T22:05:38.605Z\", \"updated_at\": \"2026-05-18T22:07:17.604Z\", \"hypothesis\": \"Temperature ablation (T=0.8, seed=456) of Qwen3-8B SciERC N=8 SCS inference to study temperature sensitivity of structural consistency signals.\", \"spec\": {\"command\": \"python scs_inference.py --dataset scierc --seed 456 --n_samples 8 --temperature 0.8\", \"server\": \"autodl-5090\", \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/data/scierc\", \"data_count\": 551, \"model_name\": \"Qwen3-8B\", \"seed\": 456, \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_026_t08_seed456\", \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_026_t08_seed456.log\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T22:06:56.681Z\", \"metrics\": {\"ner_greedy_f1\": 0.6641, \"ner_oracle_f1\": 0.7694, \"rho_sj_ner\": 0.3771, \"sample_f1_pct_zero\": 11.79, \"instance_count\": 551, \"n_valid\": 529}}, \"exp_026_t08_seed123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T22:05:37.454Z\", \"updated_at\": \"2026-05-18T22:07:16.089Z\", \"hypothesis\": \"Temperature ablation (T=0.8, seed=123) of Qwen3-8B SciERC N=8 SCS inference to study temperature sensitivity of structural consistency signals.\", \"spec\": {\"command\": \"python scs_inference.py --dataset scierc --seed 123 --n_samples 8 --temperature 0.8\", \"server\": \"autodl-5090\", \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/data/scierc\", \"data_count\": 551, \"model_name\": \"Qwen3-8B\", \"seed\": 123, \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_026_t08_seed123\", \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_026_t08_seed123.log\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T22:06:54.734Z\", \"metrics\": {\"ner_greedy_f1\": 0.6607, \"ner_oracle_f1\": 0.7714, \"rho_sj_ner\": 0.3893, \"sample_f1_pct_zero\": 11.22, \"instance_count\": 551, \"n_valid\": 529}}, \"exp_026_t05_seed456\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T22:05:36.536Z\", \"updated_at\": \"2026-05-18T22:07:14.675Z\", \"hypothesis\": \"Temperature ablation (T=0.5, seed=456) of Qwen3-8B SciERC N=8 SCS inference to study temperature sensitivity of structural consistency signals.\", \"spec\": {\"command\": \"python scs_inference.py --dataset scierc --seed 456 --n_samples 8 --temperature 0.5\", \"server\": \"autodl-5090\", \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/data/scierc\", \"data_count\": 551, \"model_name\": \"Qwen3-8B\", \"seed\": 456, \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_026_t05_seed456\", \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_026_t05_seed456.log\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T22:06:52.749Z\", \"metrics\": {\"ner_greedy_f1\": 0.6639, \"ner_oracle_f1\": 0.7437, \"rho_sj_ner\": 0.3279, \"sample_f1_pct_zero\": 10.28, \"instance_count\": 551, \"n_valid\": 529}}, \"exp_026_t05_seed123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T22:05:35.201Z\", \"updated_at\": \"2026-05-18T22:07:13.198Z\", \"hypothesis\": \"Temperature ablation (T=0.5, seed=123) of Qwen3-8B SciERC N=8 SCS inference to study temperature sensitivity of structural consistency signals.\", \"spec\": {\"command\": \"python scs_inference.py --dataset scierc --seed 123 --n_samples 8 --temperature 0.5\", \"server\": \"autodl-5090\", \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/data/scierc\", \"data_count\": 551, \"model_name\": \"Qwen3-8B\", \"seed\": 123, \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_026_t05_seed123\", \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_026_t05_seed123.log\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T22:06:50.703Z\", \"metrics\": {\"ner_greedy_f1\": 0.6611, \"ner_oracle_f1\": 0.7444, \"rho_sj_ner\": 0.3133, \"sample_f1_pct_zero\": 10.09, \"instance_count\": 551, \"n_valid\": 529}}, \"exp_029b\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-17T23:32:18.543Z\", \"updated_at\": \"2026-05-18T22:05:45.856Z\", \"hypothesis\": \"Training convergence modulates degeneracy across datasets. SciERC 10-epoch training should produce higher degeneracy than 5-epoch baseline (17.8%), confirming monotonic epoch-degeneracy relationship across datasets.\", \"parent\": \"ft_002_v2\", \"failure_reason\": \"OOM on cuda:1 due to residual vLLM process (PID 416808) occupying 30.2GB VRAM\", \"reproduce\": {\"finished_at\": \"2026-05-18T02:05:15.948Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-18T00:55:29.806594+00:00\"}, {\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-18T01:58:43.646574+00:00\"}, {\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-18T02:05:20.480884+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\"}}, \"completed_at\": \"2026-05-18T00:56:47.625Z\", \"spec\": {\"pid\": \"441471\", \"server\": \"autodl-5090\", \"gpu\": \"cuda:1\", \"command\": \"FORCE_TORCHRUN=0 CUDA_VISIBLE_DEVICES=1 llamafactory-cli train train_config_scierc_10ep.yaml\", \"data_path\": \"scierc_uie_train\", \"data_count\": 1861, \"model_name\": \"Qwen3-8B\", \"seed\": 42, \"checkpoint_source\": \"Qwen/Qwen3-8B\", \"eval_data\": \"scierc_uie_test\", \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen3-8b-scierc-10epoch-lora/\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_029b.log\"}, \"metrics\": {\"degen_rate\": 0.478, \"degen_rate_source\": \"unified_metrics_constant_f1_gold_filtered\"}, \"conclusion\": \"success\"}, \"exp_029a\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T23:32:17.191Z\", \"updated_at\": \"2026-05-18T22:05:44.959Z\", \"hypothesis\": \"Training convergence modulates degeneracy across datasets. SciERC 3-epoch training should produce lower degeneracy than 5-epoch baseline (17.8%), confirming epoch confound is not Few-NERD-specific.\", \"parent\": \"ft_002_v2\", \"spec\": {\"command\": \"FORCE_TORCHRUN=0 CUDA_VISIBLE_DEVICES=0 bash -c \\\"source /root/miniconda3/bin/activate && cd /root/autodl-tmp/struct_self_consist_ie && llamafactory-cli train train_config_scierc_3ep.yaml\\\"\", \"server\": \"autodl-5090\", \"gpu\": \"cuda:0\", \"pid\": 436761, \"data_path\": \"data/scierc_uie_train\", \"data_count\": 1861, \"model_name\": \"Qwen3-8B LoRA rank=32\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen3-8b-scierc-3epoch-lora\", \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/logs/exp_029a_inference.log\", \"checkpoint_source\": \"Qwen/Qwen3-8B\", \"eval_data\": \"data/scierc_uie_dev\"}, \"reproduce\": {\"finished_at\": \"2026-05-18T00:55:16.392Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-18T00:55:20.617085+00:00\"}]}, \"failure_reason\": \"\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T01:00:18.242Z\", \"metrics\": {\"degen_rate\": 0.064, \"degen_rate_source\": \"unified_metrics_constant_f1_gold_filtered\"}}, \"exp_021_fewnerd_n8_seed456\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T22:03:17.992Z\", \"updated_at\": \"2026-05-18T22:04:50.774Z\", \"hypothesis\": \"Multi-seed replication (seed=456) of Qwen3-8B FewNERD N=8 SCS inference to validate structural consistency signal on fine-grained NER dataset.\", \"spec\": {\"command\": \"python scs_inference.py --dataset fewnerd --seed 456 --n_samples 8 --temperature 1.0\", \"server\": \"autodl-5090\", \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/data/fewnerd\", \"data_count\": 37648, \"model_name\": \"Qwen3-8B\", \"seed\": 456, \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_021_fewnerd_n8_seed456\", \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_021_fewnerd_n8_seed456_run.log\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T22:04:35.573Z\", \"metrics\": {\"degen_rate\": 0.1212, \"degen_rate_source\": \"unified_metrics_constant_f1_gold_filtered\", \"instance_count\": 37648, \"n_valid\": 32565, \"n_gold_empty\": 5083, \"ner_greedy_f1\": 0.7888, \"ner_oracle_f1\": 0.881, \"rho_fk_ner\": 0.1632, \"rho_sj_ner\": 0.313, \"sample_f1_pct_zero\": 19.32}}, \"exp_021_fewnerd_n8_seed123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T22:03:16.735Z\", \"updated_at\": \"2026-05-18T22:04:49.470Z\", \"hypothesis\": \"Multi-seed replication (seed=123) of Qwen3-8B FewNERD N=8 SCS inference to validate structural consistency signal on fine-grained NER dataset.\", \"spec\": {\"command\": \"python scs_inference.py --dataset fewnerd --seed 123 --n_samples 8 --temperature 1.0\", \"server\": \"autodl-5090\", \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/data/fewnerd\", \"data_count\": 37648, \"model_name\": \"Qwen3-8B\", \"seed\": 123, \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_021_fewnerd_n8_seed123\", \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_021_fewnerd_n8_seed123_run.log\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T22:04:33.731Z\", \"metrics\": {\"degen_rate\": 0.1312, \"degen_rate_source\": \"unified_metrics_constant_f1_gold_filtered\", \"instance_count\": 37648, \"n_valid\": 32565, \"n_gold_empty\": 5083, \"ner_greedy_f1\": 0.7885, \"ner_oracle_f1\": 0.8892, \"rho_fk_ner\": 0.1602, \"rho_sj_ner\": 0.3083, \"sample_f1_pct_zero\": 20.39}}, \"exp_002_conll_n16_seed456\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T22:03:15.720Z\", \"updated_at\": \"2026-05-18T22:04:46.954Z\", \"hypothesis\": \"Multi-seed replication (seed=456) of Qwen3-8B CoNLL-2003 N=16 SCS inference to validate structural consistency signal stability across random seeds.\", \"spec\": {\"command\": \"python scs_inference.py --dataset conll2003 --seed 456 --n_samples 16 --temperature 1.0\", \"server\": \"autodl-5090\", \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/data/conll2003\", \"data_count\": 3453, \"model_name\": \"Qwen3-8B\", \"seed\": 456, \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_002_conll_n16_seed456\", \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_002_conll_n16_seed456.log\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T22:04:31.934Z\", \"metrics\": {\"degen_rate\": 0.5544, \"degen_rate_source\": \"unified_metrics_constant_f1_gold_filtered\", \"instance_count\": 3453, \"n_valid\": 2756, \"n_gold_empty\": 697, \"ner_greedy_f1\": 0.9074, \"ner_oracle_f1\": 0.9549, \"rho_fk_ner\": 0.4718, \"rho_sj_ner\": 0.4819, \"sample_f1_pct_zero\": 7.02}}, \"exp_002_conll_n16_seed123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T22:03:14.343Z\", \"updated_at\": \"2026-05-18T22:04:45.039Z\", \"hypothesis\": \"Multi-seed replication (seed=123) of Qwen3-8B CoNLL-2003 N=16 SCS inference to validate structural consistency signal stability across random seeds.\", \"spec\": {\"command\": \"python scs_inference.py --dataset conll2003 --seed 123 --n_samples 16 --temperature 1.0\", \"server\": \"autodl-5090\", \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/data/conll2003\", \"data_count\": 3453, \"model_name\": \"Qwen3-8B\", \"seed\": 123, \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_002_conll_n16_seed123\", \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_002_conll_n16_seed123.log\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T22:04:29.992Z\", \"metrics\": {\"degen_rate\": 0.471, \"degen_rate_source\": \"unified_metrics_constant_f1_gold_filtered\", \"instance_count\": 3453, \"n_valid\": 2756, \"n_gold_empty\": 697, \"ner_greedy_f1\": 0.9068, \"ner_oracle_f1\": 0.9633, \"rho_fk_ner\": 0.4524, \"rho_sj_ner\": 0.4621, \"sample_f1_pct_zero\": 7.54}}, \"exp_017_llama_conll_n16_s456_r1024\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T22:17:04.572Z\", \"updated_at\": \"2026-05-18T20:50:15.047Z\", \"spec\": {\"hypothesis\": \"D054 rerun: max_tokens=1024. Verify truncation impact on LLaMA CoNLL N=16 seed456.\", \"parent\": \"exp_017_llama_conll_n16_s456\", \"model_name\": \"llama3.1-8b-conll2003-merged\", \"dataset\": \"CoNLL-2003\", \"seed\": 456, \"server\": \"autodl-5090\", \"command\": \"python code/run_mvp_pilot.py --model_path checkpoints/llama3.1-8b-conll2003-merged --data_dir data/conll2003 --dataset conll2003 --subtask ner --n_samples 16 --temperature 1.0 --seed 456 --num_test 9999 --max_tokens 1024 --collect_logprobs --output_dir output/exp_017_llama_conll_n16_s456_r1024\", \"gpu\": \"cuda:2\", \"pid\": \"175870\", \"data_path\": \"data/conll2003\", \"data_count\": 3453, \"tmux_session\": \"exp_017_llama_conll_n16_s456_r1024\"}, \"conclusion\": \"success\", \"metrics\": {\"degen_rate\": 0.8672, \"degen_rate_source\": \"unified_metrics_constant_f1_gold_filtered\", \"instance_count\": 3453, \"n_valid\": 2756, \"n_gold_empty\": 697, \"parse_rate\": 1, \"ner_greedy_f1\": 0.9265, \"ner_oracle_f1\": 0.9499, \"rho_fk_ner\": 0.469, \"rho_sj_ner\": 0.4734, \"rho_vc_ner\": 0.4722, \"rho_em_ner\": 0.4752, \"rho_lp_ner\": 0.3099, \"auroc_fk_ner\": 0.7408, \"auroc_sj_ner\": 0.7428, \"auroc_vc_ner\": 0.7495, \"auroc_em_ner\": 0.7444, \"auroc_lp_ner\": 0.7628, \"auroc_note\": \"median F1=1.0, AUROC uses >=median threshold\", \"rho_note\": \"CORRECTED 2026-05-15: old values (rho_fk=0.8085,rho_sj=0.1895) were inflated/deflated by 697 gold-empty instances. Now uses gold-filtered pipeline (n=2756).\"}, \"checkpoint_path\": \"N/A (inference-only)\", \"log_path\": \"output/exp_017_llama_conll_n16_s456_r1024_run.log\", \"completed_at\": \"2026-05-15T11:45:25.899Z\", \"hypothesis\": \"LLaMA CoNLL N=16 seed=456 (max_tokens=1024 rerun): cross-model multi-seed validation. Confirms structural>surface ordering is stable across seeds for LLaMA on CoNLL after gold-filtering correction.\"}, \"exp_017_llama_conll_n16_r1024\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T22:17:01.036Z\", \"updated_at\": \"2026-05-18T20:50:11.906Z\", \"spec\": {\"hypothesis\": \"D054 rerun: max_tokens=1024. Verify truncation impact on LLaMA CoNLL N=16 seed42.\", \"parent\": \"exp_017_llama_conll_n16\", \"model_name\": \"llama3.1-8b-conll2003-merged\", \"dataset\": \"CoNLL-2003\", \"seed\": 42, \"server\": \"autodl-5090\", \"command\": \"python code/run_mvp_pilot.py --model_path checkpoints/llama3.1-8b-conll2003-merged --data_dir data/conll2003 --dataset conll2003 --subtask ner --n_samples 16 --temperature 1.0 --seed 42 --num_test 9999 --max_tokens 1024 --collect_logprobs --output_dir output/exp_017_llama_conll_n16_r1024\", \"gpu\": \"cuda:1\", \"pid\": \"175734\", \"data_path\": \"data/conll2003\", \"data_count\": 3453, \"tmux_session\": \"exp_017_llama_conll_n16_r1024\"}, \"conclusion\": \"success\", \"metrics\": {\"degen_rate\": 0.8647, \"degen_rate_source\": \"unified_metrics_constant_f1_gold_filtered\", \"instance_count\": 3453, \"n_valid\": 2756, \"n_gold_empty\": 697, \"parse_rate\": 1, \"ner_greedy_f1\": 0.9265, \"ner_oracle_f1\": 0.9499, \"rho_fk_ner\": 0.4752, \"rho_sj_ner\": 0.4836, \"rho_vc_ner\": 0.4746, \"rho_em_ner\": 0.4818, \"rho_lp_ner\": 0.3136, \"auroc_fk_ner\": 0.7467, \"auroc_sj_ner\": 0.7496, \"auroc_vc_ner\": 0.7529, \"auroc_em_ner\": 0.7508, \"auroc_lp_ner\": 0.7661, \"auroc_note\": \"median F1=1.0, AUROC uses >=median threshold\", \"rho_note\": \"CORRECTED 2026-05-15: old values (rho_fk=0.8095,rho_sj=0.1815) were inflated/deflated by 697 gold-empty instances. Now uses gold-filtered pipeline (n=2756).\"}, \"checkpoint_path\": \"N/A (inference-only)\", \"log_path\": \"output/exp_017_llama_conll_n16_r1024_run.log\", \"completed_at\": \"2026-05-15T11:45:23.213Z\", \"hypothesis\": \"LLaMA CoNLL N=16 seed=42 (max_tokens=1024 rerun): cross-model baseline on CoNLL. Establishes LLaMA signal rankings after gold-filtering correction (fixes inflated FK ρ from gold-empty instances).\"}, \"exp_018_llama_scierc_seed456_r1024\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T06:12:43.492Z\", \"updated_at\": \"2026-05-18T20:50:04.988Z\", \"spec\": {\"hypothesis\": \"D066 fresh rerun: LLaMA SciERC seed=456 with explicit max_tokens=1024. Replaces exp_007 re-analysis for clean 3-seed comparison.\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && PYTHONPATH=code python code/run_mvp_pilot.py --model_path checkpoints/llama3.1-8b-scierc-merged --data_dir data/scierc/processed_data --dataset scierc --subtask joint --n_samples 8 --temperature 1.0 --seed 456 --max_tokens 1024 --num_test 9999 --collect_logprobs --output_dir output/exp_018_llama_scierc_seed456_r1024\\\"\", \"server\": \"autodl-5090\", \"seed\": 456, \"model_name\": \"LLaMA-3.1-8B-SciERC-merged\", \"model_path\": \"checkpoints/llama3.1-8b-scierc-merged\", \"dataset\": \"SciERC\", \"subtask\": \"joint\", \"data_path\": \"data/scierc/processed_data\", \"data_count\": 551, \"N\": 8, \"T\": 1, \"max_tokens\": 1024, \"is_new_inference\": true, \"checkpoint_path\": \"output/exp_018_llama_scierc_seed456_r1024/\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_018_llama_scierc_seed456_r1024.log\"}, \"server\": \"autodl-5090\", \"gpu\": \"cuda:1\", \"pid\": \"157584\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_018_llama_scierc_seed456_r1024.log\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && PYTHONPATH=code python code/run_mvp_pilot.py --model_path checkpoints/llama3.1-8b-scierc-merged --data_dir data/scierc/processed_data --dataset scierc --subtask joint --n_samples 8 --temperature 1.0 --seed 456 --max_tokens 1024 --num_test 9999 --collect_logprobs --output_dir output/exp_018_llama_scierc_seed456_r1024\\\"\", \"finished_at\": \"2026-05-15T06:18:22.307Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T06:18:24.880896+00:00\"}]}, \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_018_llama_scierc_seed456_r1024\", \"metrics\": {\"degen_rate\": 0.2741, \"degen_rate_source\": \"unified_metrics_constant_f1_gold_filtered\", \"ner_greedy_f1\": 0.6597, \"ner_oracle_f1\": 0.7683, \"ner_oracle_headroom\": 0.1086, \"ner_cond_rho_fk\": 0.1472, \"ner_cond_rho_sj\": 0.2718, \"ner_cond_rho_logprob\": 0.083, \"ner_logprob_auroc_cond\": 0.5485, \"re_greedy_f1\": 0.4338, \"re_oracle_f1\": 0.5834, \"re_oracle_headroom\": 0.1496, \"re_cond_rho_fk\": 0.2107, \"re_cond_rho_sj\": 0.3898, \"re_cond_rho_logprob\": 0.1252, \"re_logprob_auroc_cond\": 0.6119, \"ner_structural_beats_logprob\": true, \"re_structural_beats_logprob\": true}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T06:21:45.350Z\", \"hypothesis\": \"LLaMA SciERC seed=456 (max_tokens=1024): multi-seed cross-model validation. Complements seed42 for LLaMA 3-seed protocol on SciERC NER+RE signal rankings.\"}, \"exp_018_llama_scierc_seed42_r1024\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T06:09:57.155Z\", \"updated_at\": \"2026-05-18T20:50:00.335Z\", \"spec\": {\"hypothesis\": \"D066 fresh rerun: LLaMA SciERC seed=42 with explicit max_tokens=1024. Replaces exp_007_llama_inference for clean 3-seed comparison.\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && PYTHONPATH=code python code/run_mvp_pilot.py --model_path checkpoints/llama3.1-8b-scierc-merged --data_dir data/scierc/processed_data --dataset scierc --subtask joint --n_samples 8 --temperature 1.0 --seed 42 --max_tokens 1024 --num_test 9999 --collect_logprobs --output_dir output/exp_018_llama_scierc_seed42_r1024\\\"\", \"server\": \"autodl-5090\", \"seed\": 42, \"model_name\": \"LLaMA-3.1-8B-SciERC-merged\", \"model_path\": \"checkpoints/llama3.1-8b-scierc-merged\", \"dataset\": \"SciERC\", \"subtask\": \"joint\", \"data_path\": \"data/scierc/processed_data\", \"data_count\": 551, \"N\": 8, \"T\": 1, \"max_tokens\": 1024, \"is_new_inference\": true, \"checkpoint_path\": \"output/exp_018_llama_scierc_seed42_r1024/\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_018_llama_scierc_seed42_r1024.log\"}, \"server\": \"autodl-5090\", \"gpu\": \"cuda:0\", \"pid\": \"156809\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_018_llama_scierc_seed42_r1024.log\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && PYTHONPATH=code python code/run_mvp_pilot.py --model_path checkpoints/llama3.1-8b-scierc-merged --data_dir data/scierc/processed_data --dataset scierc --subtask joint --n_samples 8 --temperature 1.0 --seed 42 --max_tokens 1024 --num_test 9999 --collect_logprobs --output_dir output/exp_018_llama_scierc_seed42_r1024\\\"\", \"finished_at\": \"2026-05-15T06:15:47.963Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T06:15:50.613872+00:00\"}]}, \"metrics\": {\"degen_rate\": 0.2495, \"degen_rate_source\": \"unified_metrics_constant_f1_gold_filtered\", \"ner\": {\"full\": {\"SJ\": {\"rho\": 0.3096, \"tau\": 0.2288, \"auroc\": 0.6683}, \"FK\": {\"rho\": 0.2352, \"tau\": 0.1759, \"auroc\": 0.6069}, \"logprob\": {\"rho\": 0.1503, \"tau\": 0.1087, \"auroc\": 0.5318}, \"EM\": {\"rho\": 0.2587, \"tau\": 0.1966, \"auroc\": 0.7174}, \"voting_conf\": {\"rho\": 0.4053, \"tau\": 0.3042, \"auroc\": 0.6967}}, \"conditional\": {\"SJ\": {\"rho\": 0.2718, \"tau\": null, \"auroc\": 0.6565}, \"FK\": {\"rho\": 0.1472, \"tau\": null, \"auroc\": 0.5866}, \"logprob\": {\"rho\": 0.081, \"tau\": null, \"auroc\": 0.5129}, \"EM\": {\"rho\": 0.3165, \"tau\": null, \"auroc\": 0.7244}, \"voting_conf\": {\"rho\": 0.3078, \"tau\": null, \"auroc\": 0.6714}}, \"greedy_f1\": 0.6607, \"oracle_f1\": 0.7781, \"n_full\": 529, \"n_cond\": 478}, \"re\": {\"full\": {\"SJ\": {\"rho\": 0.2748, \"tau\": 0.2102, \"auroc\": 0.7244}, \"FK\": {\"rho\": 0.3027, \"tau\": 0.2337, \"auroc\": 0.691}, \"logprob\": {\"rho\": 0.3163, \"tau\": 0.233, \"auroc\": 0.6313}, \"EM\": {\"rho\": 0.1681, \"tau\": 0.1275, \"auroc\": 0.7697}, \"voting_conf\": {\"rho\": 0.384, \"tau\": 0.2965, \"auroc\": 0.7337}}, \"conditional\": {\"SJ\": {\"rho\": 0.3461, \"tau\": null, \"auroc\": 0.7233}, \"FK\": {\"rho\": 0.1969, \"tau\": null, \"auroc\": 0.6684}, \"logprob\": {\"rho\": 0.0888, \"tau\": null, \"auroc\": 0.5556}, \"EM\": {\"rho\": 0.4969, \"tau\": null, \"auroc\": 0.819}, \"voting_conf\": {\"rho\": 0.3433, \"tau\": null, \"auroc\": 0.7003}}, \"greedy_f1\": 0.4319, \"oracle_f1\": 0.5775, \"n_full\": 397, \"n_cond\": 251}}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T06:21:47.660Z\", \"hypothesis\": \"LLaMA SciERC seed=42 (max_tokens=1024): cross-model validation on SciERC. Establishes LLaMA NER signal rankings on same dataset as Qwen for direct model-family comparison.\"}, \"exp_002_conll_n16\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T18:12:16.041Z\", \"updated_at\": \"2026-05-18T20:49:50.398Z\", \"spec\": {\"hypothesis\": \"Qwen CoNLL-2003 N=16: cross-dataset N-scaling comparison with SciERC N=16\", \"plan_id\": \"exp-002\", \"parent\": \"exp_002_ner_conll2003\", \"command\": \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && CUDA_VISIBLE_DEVICES=0 PYTHONPATH=code python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-conll2003-merged --data_dir data/conll2003 --dataset conll2003 --subtask ner --n_samples 16 --temperature 1.0 --seed 42 --num_test 9999 --collect_logprobs --output_dir output/exp_002_conll_n16\", \"server\": \"autodl-5090\", \"data_path\": \"data/conll2003\", \"data_count\": 3453, \"model_name\": \"qwen3-8b-conll2003-merged\", \"seed\": 42}, \"conclusion\": \"success\", \"metrics\": {\"degen_rate\": 0.4844, \"degen_rate_source\": \"unified_metrics_constant_f1_gold_filtered\", \"N\": 16, \"dataset\": \"conll2003\", \"subtask\": \"ner\", \"n_instances\": 3453, \"n_valid\": 2756, \"n_conditional\": 2614, \"greedy_f1\": 0.907, \"full\": {\"SJ_rho\": 0.4496, \"FK_rho\": 0.3928, \"logprob_rho\": 0.3146, \"EM_rho\": 0.4627, \"voting_conf_rho\": 0.4286, \"SJ_AUROC\": 0.8264, \"FK_AUROC\": 0.7821, \"logprob_AUROC\": 0.7531, \"EM_AUROC\": 0.8409, \"voting_conf_AUROC\": 0.8071, \"SJ_ECE\": 0.0747, \"FK_ECE\": 0.1786, \"logprob_ECE\": 0.2031, \"EM_ECE\": 0.0786, \"voting_conf_ECE\": 0.529}, \"conditional\": {\"SJ_rho\": 0.4208, \"FK_rho\": 0.3494, \"logprob_rho\": 0.3756, \"EM_rho\": 0.4658, \"voting_conf_rho\": 0.3654, \"SJ_AUROC\": 0.8405, \"FK_AUROC\": 0.7819, \"logprob_AUROC\": 0.8259, \"EM_AUROC\": 0.8781, \"voting_conf_AUROC\": 0.7951, \"SJ_ECE\": 0.0982, \"FK_ECE\": 0.1899, \"logprob_ECE\": 0.2504, \"EM_ECE\": 0.0997, \"voting_conf_ECE\": 0.6096}, \"n8_vs_n16_delta_rho_full\": {\"SJ\": 0.0139, \"FK\": -0.007, \"logprob\": -0.0011, \"EM\": 0.012, \"voting_conf\": 0.0049}}, \"checkpoint_path\": \"output/exp_002_conll_n16/samples.jsonl\", \"log_path\": \"output/exp_002_conll_n16.log\", \"completed_at\": \"2026-05-14T18:58:40.473Z\", \"hypothesis\": \"CoNLL N=16 NER: cross-dataset validation on high-performance NER dataset. Tests if structural signals retain advantage when base model performance is already high (greedy F1 > 0.9).\"}, \"exp_012_rerun_1024\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T22:11:33.777Z\", \"updated_at\": \"2026-05-18T20:49:42.395Z\", \"spec\": {\"hypothesis\": \"Verify if max_tokens=512 truncation inflated Table 1 N=8 SciERC signal values. Rerun with max_tokens=1024 for clean comparison.\", \"model_name\": \"qwen3-8b-scierc-merged-v2\", \"dataset\": \"SciERC\", \"parent\": \"exp_012_logprob_baseline\", \"data_count\": 551, \"seed\": 42, \"server\": \"autodl-5090\", \"command\": \"CUDA_VISIBLE_DEVICES=0 python3 code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc/processed_data --dataset scierc --subtask joint --n_samples 8 --temperature 1.0 --max_tokens 1024 --seed 42 --num_test 9999 --collect_logprobs --output_dir output/exp_012_rerun_1024\", \"checkpoint_path\": \"output/exp_012_rerun_1024/\", \"log_path\": \"output/exp_012_rerun_1024/run.log\", \"data_path\": \"data/scierc/processed_data\"}, \"conclusion\": \"success\", \"metrics\": {\"degen_rate\": 0.1777, \"degen_rate_source\": \"unified_metrics_constant_f1_gold_filtered\", \"ner_full\": {\"n\": 529, \"SJ\": {\"rho\": 0.3599, \"tau\": 0.2646, \"AUROC\": 0.6917, \"ECE\": 0.4531, \"rho_ci95\": [0.2732, 0.4389], \"AUROC_ci95\": [0.6304, 0.7406]}, \"FK\": {\"rho\": 0.2665, \"tau\": 0.1974, \"AUROC\": 0.629, \"ECE\": 0.4512, \"rho_ci95\": [0.1743, 0.3486], \"AUROC_ci95\": [0.5612, 0.6882]}, \"logprob\": {\"rho\": 0.2052, \"tau\": 0.1478, \"AUROC\": 0.5783, \"ECE\": 0.7064, \"rho_ci95\": [0.1171, 0.2904], \"AUROC_ci95\": [0.5179, 0.6387]}, \"EM\": {\"rho\": 0.2945, \"tau\": 0.2208, \"AUROC\": 0.7493, \"ECE\": 0.3526, \"rho_ci95\": [0.2094, 0.37], \"AUROC_ci95\": [0.7002, 0.7928]}, \"voting_conf\": {\"rho\": 0.3792, \"tau\": 0.2805, \"AUROC\": 0.6841, \"ECE\": 0.3807, \"rho_ci95\": [0.2972, 0.4486], \"AUROC_ci95\": [0.6249, 0.7366]}}, \"ner_cond\": {\"n\": 477, \"SJ\": {\"rho\": 0.3113, \"tau\": 0.2257, \"AUROC\": 0.6772, \"ECE\": 0.4416, \"rho_ci95\": [0.2353, 0.3959], \"AUROC_ci95\": [0.621, 0.7337]}, \"FK\": {\"rho\": 0.1761, \"tau\": 0.1284, \"AUROC\": 0.6078, \"ECE\": 0.4389, \"rho_ci95\": [0.0839, 0.2665], \"AUROC_ci95\": [0.5442, 0.6709]}, \"logprob\": {\"rho\": 0.1538, \"tau\": 0.1111, \"AUROC\": 0.5633, \"ECE\": 0.6803, \"rho_ci95\": [0.0637, 0.2424], \"AUROC_ci95\": [0.5032, 0.6232]}, \"EM\": {\"rho\": 0.3596, \"tau\": 0.2735, \"AUROC\": 0.7556, \"ECE\": 0.3257, \"rho_ci95\": [0.2819, 0.4408], \"AUROC_ci95\": [0.7011, 0.8107]}, \"voting_conf\": {\"rho\": 0.3, \"tau\": 0.2189, \"AUROC\": 0.6618, \"ECE\": 0.3746, \"rho_ci95\": [0.2168, 0.3836], \"AUROC_ci95\": [0.6004, 0.7201]}}, \"re_full\": {\"n\": 397, \"SJ\": {\"rho\": 0.2503, \"tau\": 0.1878, \"AUROC\": 0.6702, \"ECE\": 0.3865}, \"FK\": {\"rho\": 0.2752, \"tau\": 0.2117, \"AUROC\": 0.6089, \"ECE\": 0.4405}, \"logprob\": {\"rho\": 0.2662, \"tau\": 0.1951, \"AUROC\": 0.6005, \"ECE\": 0.7694}, \"EM\": {\"rho\": 0.1344, \"tau\": 0.1081, \"AUROC\": 0.7059, \"ECE\": 0.3548}, \"voting_conf\": {\"rho\": 0.3498, \"tau\": 0.2663, \"AUROC\": 0.6935, \"ECE\": 0.2724}}, \"re_cond\": {\"n\": 238, \"SJ\": {\"rho\": 0.2457, \"tau\": 0.1811, \"AUROC\": 0.6463, \"ECE\": 0.2941}, \"FK\": {\"rho\": 0.1139, \"tau\": 0.0876, \"AUROC\": 0.551, \"ECE\": 0.3424}, \"logprob\": {\"rho\": 0.0112, \"tau\": 0.0051, \"AUROC\": 0.5186, \"ECE\": 0.6464}, \"EM\": {\"rho\": 0.4165, \"tau\": 0.3256, \"AUROC\": 0.7515, \"ECE\": 0.2232}, \"voting_conf\": {\"rho\": 0.2409, \"tau\": 0.178, \"AUROC\": 0.642, \"ECE\": 0.207}}, \"delta_vs_512_ner_full_rho\": {\"SJ\": 0.0034, \"FK\": 0.0014, \"EM\": 0.0379, \"voting_conf\": -0.1226, \"logprob\": 0.0656}, \"provenance_note\": \"exp_015_v2 scierc_n8_logprob used exp_012_logprob (max_tokens=512 truncated data). voting_conf was inflated 0.502→0.379, logprob was suppressed 0.140→0.205.\"}, \"completed_at\": \"2026-05-14T23:10:33.075Z\", \"hypothesis\": \"Canonical SciERC baseline with max_tokens=1024: Qwen3-8B ft_002_v2, N=8, T=1.0, seed=42, joint NER+RE. Establishes ground-truth ρ rankings and selection F1 for all 5 signals under correct generation length.\"}, \"exp_llama_scierc_seed456\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T19:15:27.504Z\", \"updated_at\": \"2026-05-18T20:49:10.758Z\", \"hypothesis\": \"LLaMA-3.1-8B on SciERC with seed=456 will show consistent 5-signal ranking patterns (SJ/FK > logprob) and DGS selection gains comparable to seed=42 and seed=123, confirming cross-seed stability.\", \"spec\": {\"command\": \"python3 code/analyze_llama_scierc_seed456_5signal.py\", \"server\": \"autodl-5090\", \"data_path\": \"output/exp_018_llama_scierc_seed456/samples.jsonl\", \"data_count\": 551, \"model_name\": \"LLaMA-3.1-8B-Instruct\", \"seed\": 456, \"checkpoint_source\": \"same as seed123\", \"eval_data\": \"SciERC test (551 instances)\", \"checkpoint_path\": \"output/exp_018_llama_scierc_seed456/5signal_dgs_report.json\", \"log_path\": \"output/exp_018_llama_scierc_seed456/run.log\"}, \"metrics\": {\"greedy_f1\": 0.6457, \"oracle_f1\": 0.7574, \"headroom\": 0.1117, \"dgs_f1\": 0.6454, \"degen_rate\": 0.2741, \"degen_rate_source\": \"unified_metrics_constant_f1_gold_filtered\", \"rho_SJ_full\": 0.3663, \"rho_FK_full\": 0.3115, \"rho_logprob_full\": 0.1911, \"rho_EM_full\": 0.3088, \"rho_vc_full\": 0.4135, \"auroc_SJ_full\": 0.7061, \"auroc_EM_full\": 0.7538, \"n_valid\": 529, \"n_conditional\": 478}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T19:16:00.973Z\"}, \"exp_007_llama_scierc_seed123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T19:10:26.278Z\", \"updated_at\": \"2026-05-18T20:49:08.934Z\", \"name\": \"LLaMA-3.1-8B SciERC NER inference seed=123\", \"hypothesis\": \"Structural consistency signals (SJ, FK) correlate with entity F1 for LLaMA-8B on SciERC at seed=123, and DGS selection improves over greedy baseline\", \"spec\": {\"command\": \"python3 code/run_mvp_pilot.py --model_path checkpoints/llama3.1-8b-scierc-merged --data_dir data/scierc/processed_data --dataset scierc --subtask joint --n_samples 8 --temperature 1.0 --seed 123 --num_test 9999 --collect_logprobs --output_dir output/exp_018_llama_scierc_seed123\", \"server\": \"autodl-5090\", \"data_path\": \"data/scierc/processed_data\", \"data_count\": 551, \"model_name\": \"LLaMA-3.1-8B-Instruct (SciERC LoRA fine-tuned)\", \"seed\": 123, \"checkpoint_source\": \"checkpoints/llama3.1-8b-scierc-merged\", \"checkpoint_path\": \"checkpoints/llama3.1-8b-scierc-lora\", \"log_path\": \"output/exp_018_llama_scierc_seed123/report.json\"}, \"conclusion\": \"negative\", \"completed_at\": \"2026-05-18T19:11:30.781Z\", \"metrics\": {\"greedy_f1\": 0.6454, \"oracle_f1\": 0.7657, \"headroom\": 0.1204, \"degen_rate\": 0.2665, \"degen_rate_source\": \"unified_metrics_constant_f1_gold_filtered\", \"dgs_delta_pp\": -0.38, \"rho_SJ_full\": 0.3552, \"rho_voting_conf_full\": 0.4193, \"auroc_SJ_full\": 0.7092, \"auroc_EM_full\": 0.7468}}, \"exp_qwen3_4b_conll_scs_inference\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T19:08:28.512Z\", \"updated_at\": \"2026-05-18T20:49:06.922Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && PYTHONPATH=code python code/run_mvp_pilot.py --model_path checkpoints/qwen3-4b-conll2003-merged --data_dir data/conll2003 --dataset conll2003 --subtask ner --n_samples 8 --temperature 1.0 --seed 42 --num_test 9999 --max_tokens 1024 --collect_logprobs --output_dir output/exp_qwen3_4b_conll_scs_inference\\\"\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:0\"], \"pid\": \"222184\", \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_qwen3_4b_conll_scs_inference/report.json\", \"submitted_at\": \"2026-05-15T19:10:19.757Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen3-4b-conll2003-merged\", \"wall_clock_seconds\": 523.8, \"gpu_hours\": 0.15}, \"metrics\": {\"greedy_f1\": 0.9251, \"oracle_f1\": 0.9408, \"oracle_headroom_pp\": 1.57, \"SJ_rho_full\": 0.4045, \"SJ_rho_cond\": 0.4306, \"FK_rho_full\": 0.3961, \"FK_rho_cond\": 0.42, \"LP_rho_full\": 0.3186, \"LP_rho_cond\": 0.3378, \"LP_auroc_full\": 0.7689, \"LP_auroc_cond\": 0.8153, \"fleiss_kappa_mean\": 0.9349, \"soft_jaccard_mean\": 0.9754, \"structural_beats_surface\": true, \"rho_advantage_pp\": 0.84, \"n_instances\": 3453, \"n_gold_empty_filtered\": 697, \"n_greedy_f1_zero_filtered\": 112, \"verdict\": \"MARGINAL\", \"degen_rate\": 0.9057, \"degen_rate_source\": \"unified_metrics_constant_f1_gold_filtered\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T19:19:03.585Z\", \"notes\": \"4B CoNLL SCS inference completed. SJ>FK>LP ordering preserved at 4B scale (rho 0.405>0.396>0.319). Greedy F1=0.925 outperforms 8B (0.907), but SJ rho is lower (0.405 vs 0.450 at 8B N=16). Structural beats surface confirmed (+0.84pp). Verdict MARGINAL due to small oracle headroom (1.57pp) — the model is already very good at CoNLL, leaving little room for selection improvement.\", \"hypothesis\": \"CoNLL 4B SCS inference (checkpoint-3800): cross-scale evidence for correlation-selection gap. Tests if structural>surface ranking and LP compression hold at smaller model scale on high-degeneracy dataset.\"}, \"exp_qwen3_4b_conll_scs_inference_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T19:41:33.501Z\", \"updated_at\": \"2026-05-18T20:49:03.705Z\", \"hypothesis\": \"CoNLL 4B SCS inference with best checkpoint-4200 (from resume training). Scale ablation: cross-scale evidence for correlation-selection gap. Compare vs v1 (ckpt-3800 baseline: greedy_f1=0.9251, SJ_rho=0.4045).\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python code/run_mvp_pilot.py --model_path checkpoints/qwen3-4b-conll2003-merged-ckpt4200 --data_dir data/conll2003 --dataset conll2003 --subtask ner --n_samples 8 --temperature 1.0 --seed 42 --num_test 9999 --max_tokens 1024 --collect_logprobs --output_dir output/exp_qwen3_4b_conll_scs_inference_v2\", \"server\": \"autodl-5090\", \"data_path\": \"data/conll2003\", \"data_count\": 3453, \"model_name\": \"Qwen3-4B (LoRA checkpoint-4200 merged)\", \"seed\": 42, \"checkpoint_source\": \"checkpoints/qwen3-4b-conll2003-lora/checkpoint-4200\", \"gpu\": [\"cuda:1\"], \"checkpoint_path\": \"checkpoints/qwen3-4b-conll2003-merged-ckpt4200\", \"log_path\": \"/tmp/infer_4b_conll_v2.log\", \"account\": \"root\", \"backend\": \"tmux\", \"tmux_session\": \"exp_4b_conll_scs_v2\"}, \"metrics\": {\"greedy_f1\": 0.9234, \"oracle_f1\": 0.9404, \"oracle_headroom_pp\": 1.7, \"SJ_rho_full\": 0.4217, \"SJ_rho_cond\": 0.459, \"FK_rho_full\": 0.4181, \"FK_rho_cond\": 0.4538, \"LP_rho_full\": 0.3313, \"LP_rho_cond\": 0.3487, \"LP_auroc_full\": 0.7761, \"LP_auroc_cond\": 0.8209, \"n_instances\": 3453, \"verdict\": \"MARGINAL\", \"degen_rate\": 0.9057, \"degen_rate_source\": \"unified_metrics_constant_f1_gold_filtered\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T19:54:14.575Z\", \"notes\": \"Gold-filter audit (2026-05-16): CONSISTENT. _full metrics (SJ_rho=0.4217, FK_rho=0.4181) are computed on gold-filtered set (n=2756), same as 8B Table 1 values. _full does NOT mean all 3453 instances — it means gold-nonempty instances. _cond further excludes greedy-F1=0 (n=2641). Confirmed via run_mvp_pilot.py source code and report.json n values.\"}, \"exp_qwen3_4b_scierc_scs_inference\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T19:45:33.384Z\", \"updated_at\": \"2026-05-18T20:49:01.260Z\", \"hypothesis\": \"SciERC 4B SCS inference after v4 finetune merge. Complete 2x2 scale matrix (4B SciERC cell). Cross-scale + cross-task evidence for correlation-selection gap.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 PYTHONPATH=code python code/run_mvp_pilot.py --model_path checkpoints/qwen3-4b-scierc-merged --data_dir data/scierc/processed_data --dataset scierc --subtask joint --n_samples 8 --temperature 1.0 --seed 42 --num_test 9999 --max_tokens 1024 --collect_logprobs --output_dir output/exp_qwen3_4b_scierc_scs_inference\", \"server\": \"autodl-5090\", \"data_path\": \"data/scierc/processed_data\", \"data_count\": 551, \"model_name\": \"qwen3-4b-scierc-merged (checkpoint-400)\", \"seed\": 42, \"checkpoint_source\": \"checkpoints/qwen3-4b-scierc-merged\", \"eval_data\": \"scierc test set\"}, \"metrics\": {\"ner_greedy_f1\": 0.6612, \"ner_oracle_f1\": 0.7839, \"ner_headroom_pp\": 12.28, \"ner_SJ_rho\": 0.4221, \"ner_FK_rho\": 0.3258, \"ner_LP_rho\": 0.28, \"re_greedy_f1\": 0.4136, \"re_oracle_f1\": 0.5846, \"re_headroom_pp\": 17.1, \"re_SJ_rho\": 0.2673, \"re_FK_rho\": 0.3593, \"re_LP_rho\": 0.3512, \"re_sample_f1_pct_zero\": 0.476, \"re_LP_rho_cond\": 0.1135, \"re_LP_rho_cond_p\": 0.074, \"degen_rate\": 0.104, \"degen_rate_source\": \"unified_metrics_constant_f1_gold_filtered\"}, \"checkpoint_path\": \"checkpoints/qwen3-4b-scierc-merged/\", \"log_path\": \"/tmp/exp_qwen3_4b_scierc_scs_inference.log\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T20:00:03.730Z\"}, \"exp_027_fewnerd_n16\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T05:28:57.036Z\", \"updated_at\": \"2026-05-18T20:48:58.455Z\", \"spec\": {\"hypothesis\": \"LP selection scales with N in low-degeneracy regime: N=16 should yield LP Δ > +2pp (vs N=8 +1.36pp) on Few-NERD (10% degen), because more samples increase oracle headroom while LP ranking remains effective.\", \"parent\": \"exp_021_fewnerd_full\", \"model_name\": \"qwen3-8b-fewnerd-exp021-merged\", \"data_path\": \"data/fewnerd_n16_subset/test.json\", \"data_count\": 5000, \"seed\": 42, \"server\": \"autodl-5090\", \"gpu\": \"cuda:0,cuda:1,cuda:2,cuda:3\", \"command\": \"python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-fewnerd-exp021-merged --data_dir data/fewnerd_n16_subset --dataset fewnerd --subtask ner --n_samples 16 --temperature 1.0 --seed 42 --collect_logprobs --start_index {0,1250,2500,3750} --end_index {1250,2500,3750,5000} --output_dir output/exp_027_fewnerd_n16/shard_{0-3}\", \"checkpoint_path\": \"output/exp_027_fewnerd_n16/sampled_results.jsonl\", \"log_path\": \"output/exp_027_fewnerd_n16/\"}, \"conclusion\": \"success\", \"metrics\": {\"LP_delta_pp\": 1.88, \"LP_delta_95CI\": [1.41, 2.37], \"degen_rate\": 0.0706, \"degen_rate_source\": \"unified_metrics_constant_f1_gold_filtered\", \"greedy_f1\": 0.7478, \"lp_sel_f1\": 0.7666, \"oracle_f1\": 0.902, \"headroom_pp\": 15.42, \"all_8_types_positive\": true, \"n_instances\": 5000, \"N_samples\": 16, \"bootstrap_p\": \"<0.001\"}, \"hypothesis\": \"LP selection scales with N in low-degeneracy regime: N=16 should yield LP Δ > +2pp (vs N=8 +1.36pp) on Few-NERD (10% degen), because more samples increase oracle headroom while LP ranking remains effective.\", \"completed_at\": \"2026-05-17T05:46:48.460Z\"}, \"exp_026_t12\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T13:18:18.780Z\", \"updated_at\": \"2026-05-18T20:48:24.965Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc/processed_data --dataset scierc --n_samples 8 --temperature 1.2 --seed 42 --max_tokens 1024 --collect_logprobs --output_dir output/exp_026_t12\", \"server\": \"autodl-5090\", \"data_path\": \"data/scierc/processed_data\", \"data_count\": 551, \"model_name\": \"qwen3-8b-scierc-merged-v2\", \"seed\": 42, \"log_path\": \"output/exp_026_t12.log\", \"checkpoint_path\": \"checkpoints/qwen3-8b-scierc-merged-v2\"}, \"conclusion\": \"success\", \"metrics\": {\"temperature\": 1.2, \"task\": \"T-ablation\", \"degen_rate\": 0.1493, \"degen_rate_source\": \"unified_metrics_constant_f1_gold_filtered\"}, \"completed_at\": \"2026-05-16T14:26:37.648Z\", \"hypothesis\": \"Temperature T=1.2 ablation on SciERC: test if higher temperature increases sample diversity (lower degeneracy) and LP discriminative range, potentially improving LP selection while maintaining structural signal effectiveness.\", \"parent\": \"exp_012_rerun_1024\"}, \"exp_026_t08\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T12:57:46.027Z\", \"updated_at\": \"2026-05-18T20:48:24.112Z\", \"spec\": {\"checkpoint_path\": \"checkpoints/qwen3-8b-scierc-merged-v2\", \"log_path\": \"output/exp_026_t08/run.log\"}, \"conclusion\": \"success\", \"metrics\": {\"temperature\": 0.8, \"task\": \"T-ablation\", \"degen_rate\": 0.2382, \"degen_rate_source\": \"unified_metrics_constant_f1_gold_filtered\"}, \"completed_at\": \"2026-05-16T14:26:36.243Z\", \"hypothesis\": \"Temperature T=0.8 ablation on SciERC: test if lower temperature increases LP compression (narrower range) while structural signals remain robust, supporting the claim that LP compression is intrinsic rather than temperature-driven.\", \"parent\": \"exp_012_rerun_1024\"}, \"exp_026_t05\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T12:19:35.753Z\", \"updated_at\": \"2026-05-18T20:48:23.339Z\", \"spec\": {\"checkpoint_path\": \"checkpoints/qwen3-8b-scierc-merged-v2\", \"log_path\": \"output/exp_026_t05/run.log\"}, \"conclusion\": \"success\", \"metrics\": {\"temperature\": 0.5, \"task\": \"T-ablation\", \"degen_rate\": 0.414, \"degen_rate_source\": \"unified_metrics_constant_f1_gold_filtered\"}, \"completed_at\": \"2026-05-16T14:26:34.808Z\", \"hypothesis\": \"Temperature T=0.5 ablation on SciERC: extreme low temperature expected to maximally compress LP scores and increase degeneracy, providing upper-bound evidence for LP compression as model-intrinsic phenomenon.\", \"parent\": \"exp_012_rerun_1024\"}, \"exp_026_T12\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T09:38:31.060Z\", \"updated_at\": \"2026-05-18T20:48:22.668Z\", \"hypothesis\": \"T=1.2 will decrease degeneracy rate and expand LP range vs T=1.0, but may degrade generation quality (lower greedy F1). Tests whether reducing degeneracy via higher T recovers selection headroom or if quality degradation offsets the benefit.\", \"server\": \"autodl-5090\", \"gpu\": \"cuda:3\", \"account\": \"root\", \"reproduce\": {\"server\": \"autodl-5090\", \"gpu\": \"cuda:3\", \"started_at\": \"2026-05-17T09:39:51.733Z\", \"command\": \"bash -c \\\"source /root/miniconda3/bin/activate && cd /root/autodl-tmp/struct_self_consist_ie && python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc/processed_data --dataset scierc --subtask joint --n_samples 8 --temperature 1.2 --seed 42 --output_dir output/exp_026_T12/ --num_test 9999 --collect_logprobs 2>&1 | tee output/exp_026_T12_run.log\\\"\", \"finished_at\": \"2026-05-17T09:48:04.019Z\", \"training_hours\": 0.14}, \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/bin/activate && cd /root/autodl-tmp/struct_self_consist_ie && python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc/processed_data --dataset scierc --subtask joint --n_samples 8 --temperature 1.2 --seed 42 --output_dir output/exp_026_T12/ --num_test 9999 --collect_logprobs 2>&1 | tee output/exp_026_T12_run.log\\\"\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:3\"], \"pid\": \"381369\", \"log_path\": \"output/exp_026_T12_run.log\", \"submitted_at\": \"2026-05-17T09:41:39.393Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"output/exp_026_T12/\", \"wall_clock_seconds\": 1114.4, \"gpu_hours\": 0.31}, \"pid\": \"381369\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_026_T12.log\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-17T09:48:08.312470+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"degen_rate\": 0.1493, \"degen_rate_source\": \"unified_metrics_constant_f1_gold_filtered\", \"lp_range_mean\": 0.075, \"lp_range_std\": 0.059, \"within_instance_rho_mean\": 0.2245, \"within_instance_rho_median\": 0.3152, \"within_instance_rho_valid_pct\": 0.875, \"greedy_f1\": 0.62, \"oracle_f1\": 0.758, \"lp_sel_f1\": 0.621, \"sj_sel_f1\": 0.597, \"em_sel_f1\": 0.596, \"vc_sel_f1\": 0.582, \"sj_rho\": 0.384, \"fk_rho\": 0.386, \"lp_rho\": 0.182, \"vc_rho\": 0.342, \"sj_auroc\": 0.683, \"lp_auroc\": 0.566}, \"completed_at\": \"2026-05-17T10:00:13.771Z\"}, \"exp_026_T08\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T09:38:29.602Z\", \"updated_at\": \"2026-05-18T20:48:21.975Z\", \"hypothesis\": \"T=0.8 will show intermediate degeneracy between T=0.5 and T=1.0, establishing a monotonic degeneracy-temperature relationship. If LP selection improves at T=0.8 vs T=1.0, it identifies the optimal operating point for the selection mechanism.\", \"server\": \"autodl-5090\", \"gpu\": \"cuda:2\", \"account\": \"root\", \"reproduce\": {\"server\": \"autodl-5090\", \"gpu\": \"cuda:2\", \"started_at\": \"2026-05-17T09:39:50.780Z\", \"command\": \"bash -c \\\"source /root/miniconda3/bin/activate && cd /root/autodl-tmp/struct_self_consist_ie && python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc/processed_data --dataset scierc --subtask joint --n_samples 8 --temperature 0.8 --seed 42 --output_dir output/exp_026_T08/ --num_test 9999 --collect_logprobs 2>&1 | tee output/exp_026_T08_run.log\\\"\", \"finished_at\": \"2026-05-17T09:47:56.543Z\", \"training_hours\": 0.13}, \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/bin/activate && cd /root/autodl-tmp/struct_self_consist_ie && python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc/processed_data --dataset scierc --subtask joint --n_samples 8 --temperature 0.8 --seed 42 --output_dir output/exp_026_T08/ --num_test 9999 --collect_logprobs 2>&1 | tee output/exp_026_T08_run.log\\\"\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:2\"], \"pid\": \"380680\", \"log_path\": \"output/exp_026_T08_run.log\", \"submitted_at\": \"2026-05-17T09:41:20.812Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"output/exp_026_T08/\", \"wall_clock_seconds\": 1131.4, \"gpu_hours\": 0.31}, \"pid\": \"380680\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_026_T08.log\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-17T09:48:02.635244+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"degen_rate\": 0.2382, \"degen_rate_source\": \"unified_metrics_constant_f1_gold_filtered\", \"lp_range_mean\": 0.043, \"lp_range_std\": 0.042, \"within_instance_rho_mean\": 0.1701, \"within_instance_rho_median\": 0.2635, \"within_instance_rho_valid_pct\": 0.728, \"greedy_f1\": 0.616, \"oracle_f1\": 0.737, \"lp_sel_f1\": 0.627, \"sj_sel_f1\": 0.619, \"em_sel_f1\": 0.611, \"vc_sel_f1\": 0.603, \"sj_rho\": 0.378, \"fk_rho\": 0.34, \"lp_rho\": 0.212, \"vc_rho\": 0.352, \"sj_auroc\": 0.662, \"lp_auroc\": 0.571}, \"completed_at\": \"2026-05-17T10:00:12.248Z\"}, \"exp_026_T05\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T09:38:28.066Z\", \"updated_at\": \"2026-05-18T20:48:16.286Z\", \"hypothesis\": \"T=0.5 will increase degeneracy rate (more deterministic outputs) and compress LP range on SciERC, reducing selection headroom. Maps the low-temperature end of the degeneracy-temperature frontier, validating that degeneracy is regime-dependent on sampling temperature.\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/bin/activate && cd /root/autodl-tmp/struct_self_consist_ie && python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc/processed_data --dataset scierc --subtask joint --n_samples 8 --temperature 0.5 --seed 42 --output_dir output/exp_026_T05/ --num_test 9999 --collect_logprobs 2>&1 | tee output/exp_026_T05_run.log\\\"\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:1\"], \"pid\": \"380188\", \"log_path\": \"output/exp_026_T05_run.log\", \"submitted_at\": \"2026-05-17T09:40:51.787Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"output/exp_026_T05/\", \"wall_clock_seconds\": 1158.3, \"gpu_hours\": 0.32}, \"server\": \"autodl-5090\", \"gpu\": \"cuda:1\", \"pid\": \"380188\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_026_T05.log\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/bin/activate && cd /root/autodl-tmp/struct_self_consist_ie && python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc/processed_data --dataset scierc --subtask joint --n_samples 8 --temperature 0.5 --seed 42 --output_dir output/exp_026_T05/ --num_test 9999 --collect_logprobs 2>&1 | tee output/exp_026_T05_run.log\\\"\", \"finished_at\": \"2026-05-17T09:47:31.332Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-17T09:47:35.127151+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"degen_rate\": 0.414, \"degen_rate_source\": \"unified_metrics_constant_f1_gold_filtered\", \"lp_range_mean\": 0.022, \"lp_range_std\": 0.021, \"within_instance_rho_mean\": 0.1306, \"within_instance_rho_median\": 0.2182, \"within_instance_rho_valid_pct\": 0.597, \"greedy_f1\": 0.617, \"oracle_f1\": 0.71, \"lp_sel_f1\": 0.622, \"sj_sel_f1\": 0.622, \"em_sel_f1\": 0.619, \"vc_sel_f1\": 0.61, \"sj_rho\": 0.333, \"fk_rho\": 0.341, \"lp_rho\": 0.208, \"vc_rho\": 0.353, \"sj_auroc\": 0.644, \"lp_auroc\": 0.577}, \"completed_at\": \"2026-05-17T10:00:10.083Z\"}, \"exp_017_llama_conll_n16_s123_r1024\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T22:17:02.953Z\", \"updated_at\": \"2026-05-18T20:47:52.122Z\", \"spec\": {\"hypothesis\": \"D054 rerun: max_tokens=1024. Verify truncation impact on LLaMA CoNLL N=16 seed123.\", \"parent\": \"exp_017_llama_conll_n16_s123\", \"model_name\": \"llama3.1-8b-conll2003-merged\", \"dataset\": \"CoNLL-2003\", \"seed\": 123, \"server\": \"autodl-5090\", \"command\": \"python code/run_mvp_pilot.py --model_path checkpoints/llama3.1-8b-conll2003-merged --data_dir data/conll2003 --dataset conll2003 --subtask ner --n_samples 16 --temperature 1.0 --seed 123 --num_test 9999 --max_tokens 1024 --collect_logprobs --output_dir output/exp_017_llama_conll_n16_s123_r1024\", \"data_path\": \"data/conll2003\", \"data_count\": 3453}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T01:20:51.219Z\", \"notes\": \"Output exists on autodl-5090. Registry status corrected from killed to success.\", \"hypothesis\": \"LLaMA CoNLL N=16 seed=123 (max_tokens=1024 rerun): cross-model multi-seed validation. Confirms structural>surface ordering is stable across seeds for LLaMA on CoNLL after gold-filtering correction.\", \"metrics\": {\"degen_rate\": 0.8636, \"degen_rate_source\": \"unified_metrics_constant_f1_gold_filtered\"}}, \"exp_018_llama_scierc_seed123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T06:07:14.370Z\", \"updated_at\": \"2026-05-18T20:47:51.435Z\", \"spec\": {\"hypothesis\": \"Multi-seed robustness: LLaMA SciERC N=8 seed=123, max_tokens=1024. Verify signal stability across seeds.\", \"command\": \"python code/run_mvp_pilot.py --model_path checkpoints/llama3.1-8b-scierc-merged --data_dir data/scierc/processed_data --dataset scierc --subtask joint --seed 123 --n_samples 8 --temperature 1.0 --max_tokens 1024 --output_dir output/exp_018_llama_scierc_seed123\", \"server\": \"autodl-5090\", \"seed\": 123, \"model_name\": \"LLaMA-3.1-8B-SciERC-merged\", \"data_path\": \"data/scierc/processed_data\", \"data_count\": 551, \"checkpoint_path\": \"output/exp_018_llama_scierc_seed123/\", \"log_path\": \"output/exp_018_llama_scierc_seed123.log\", \"samples_md5\": \"072eeca68236d46b4c5c84b945209abc\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T06:08:04.855Z\", \"hypothesis\": \"LLaMA SciERC seed=123: multi-seed cross-model validation. Complements seed42 for LLaMA 3-seed protocol on SciERC NER+RE signal rankings.\", \"metrics\": {\"degen_rate\": 0.2665, \"degen_rate_source\": \"unified_metrics_constant_f1_gold_filtered\"}}, \"exp_018_qwen_scierc_seed456\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T06:07:13.570Z\", \"updated_at\": \"2026-05-18T20:47:50.032Z\", \"spec\": {\"hypothesis\": \"Multi-seed robustness: Qwen SciERC N=8 seed=456, max_tokens=1024. Verify signal stability across seeds.\", \"command\": \"python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc/processed_data --dataset scierc --subtask joint --seed 456 --n_samples 8 --temperature 1.0 --max_tokens 1024 --output_dir output/exp_018_qwen_scierc_seed456\", \"server\": \"autodl-5090\", \"seed\": 456, \"model_name\": \"Qwen3-8B-SciERC-merged-v2\", \"data_path\": \"data/scierc/processed_data\", \"data_count\": 551, \"checkpoint_path\": \"output/exp_018_qwen_scierc_seed456/\", \"log_path\": \"output/exp_018_qwen_scierc_seed456/run.log\", \"samples_md5\": \"46d0de47ad7693c07e7df3a77c90c3be\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T06:08:03.898Z\", \"hypothesis\": \"Qwen SciERC seed=456: multi-seed Qwen validation. Part of 3-seed protocol (seed42=exp_012_rerun_1024, seed123, seed456) for statistical significance of signal rankings.\", \"metrics\": {\"degen_rate\": 0.2042, \"degen_rate_source\": \"unified_metrics_constant_f1_gold_filtered\"}}, \"exp_018_qwen_scierc_seed123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T06:07:12.747Z\", \"updated_at\": \"2026-05-18T20:47:49.306Z\", \"spec\": {\"hypothesis\": \"Multi-seed robustness: Qwen SciERC N=8 seed=123, max_tokens=1024. Verify signal stability across seeds.\", \"command\": \"python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc/processed_data --dataset scierc --subtask joint --seed 123 --n_samples 8 --temperature 1.0 --max_tokens 1024 --output_dir output/exp_018_qwen_scierc_seed123\", \"server\": \"autodl-5090\", \"seed\": 123, \"model_name\": \"Qwen3-8B-SciERC-merged-v2\", \"data_path\": \"data/scierc/processed_data\", \"data_count\": 551, \"checkpoint_path\": \"output/exp_018_qwen_scierc_seed123/\", \"log_path\": \"output/exp_018_qwen_scierc_seed123.log\", \"samples_md5\": \"866a59581dea56f4633149f0b18a31ae\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T06:08:02.954Z\", \"hypothesis\": \"Qwen SciERC seed=123: multi-seed Qwen validation. Part of 3-seed protocol (seed42=exp_012_rerun_1024, seed123, seed456) for statistical significance of signal rankings.\", \"metrics\": {\"degen_rate\": 0.172, \"degen_rate_source\": \"unified_metrics_constant_f1_gold_filtered\"}}, \"exp_epoch_dgs_analysis\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T19:59:57.921Z\", \"updated_at\": \"2026-05-18T20:01:46.134Z\", \"hypothesis\": \"DGS benefit is strictly monotonic with degeneracy rate: higher degeneracy → greater DGS improvement, validating that degeneracy rate is the key gating signal\", \"spec\": {\"command\": \"python3 code/epoch_dgs_analysis.py\", \"server\": \"autodl-5090\", \"data_path\": \"/root/struct_self_consist_ie/data/\", \"data_count\": \"all datasets\", \"model_name\": \"Qwen3-8B\", \"seed\": 42}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/struct_self_consist_ie/output/epoch_dgs_analysis_results.json\", \"log_path\": \"/root/struct_self_consist_ie/output/epoch_dgs_analysis_results.json\", \"completed_at\": \"2026-05-18T20:01:46.134Z\"}, \"exp_diagnostic_calibration\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T19:59:56.064Z\", \"updated_at\": \"2026-05-18T20:01:44.364Z\", \"hypothesis\": \"A 3-indicator regression model (degeneracy rate, LP-F1 correlation, LP range) can quantitatively predict the optimal LP selection delta for unseen instances\", \"spec\": {\"command\": \"python3 code/diagnostic_calibration.py\", \"server\": \"autodl-5090\", \"data_path\": \"/root/struct_self_consist_ie/data/\", \"data_count\": \"all datasets\", \"model_name\": \"Qwen3-8B\", \"seed\": 42}, \"conclusion\": \"negative\", \"checkpoint_path\": \"/root/struct_self_consist_ie/output/diagnostic_calibration_results.json\", \"log_path\": \"/root/struct_self_consist_ie/output/diagnostic_calibration_results.json\", \"completed_at\": \"2026-05-18T20:01:44.364Z\"}, \"exp_adaptive_temperature\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T19:59:52.771Z\", \"updated_at\": \"2026-05-18T20:01:42.646Z\", \"hypothesis\": \"Adjusting sampling temperature based on instance-level confidence indicators can improve output diversity-quality tradeoff\", \"spec\": {\"command\": \"python3 code/adaptive_temperature.py\", \"server\": \"autodl-5090\", \"data_path\": \"/root/struct_self_consist_ie/data/\", \"data_count\": \"all datasets\", \"model_name\": \"Qwen3-8B\", \"seed\": 42}, \"conclusion\": \"negative\", \"checkpoint_path\": \"/root/struct_self_consist_ie/output/adaptive_temperature_results.json\", \"log_path\": \"/root/struct_self_consist_ie/output/adaptive_temperature_results.json\", \"completed_at\": \"2026-05-18T20:01:42.646Z\"}, \"exp_entity_consensus\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T19:59:50.628Z\", \"updated_at\": \"2026-05-18T20:01:40.869Z\", \"hypothesis\": \"Constructing new output from N samples using entity frequency thresholds and LP-weighted decisions can capture complementary information that single-sample selection misses\", \"spec\": {\"command\": \"python3 code/entity_consensus.py\", \"server\": \"autodl-5090\", \"data_path\": \"/root/struct_self_consist_ie/data/\", \"data_count\": \"all datasets\", \"model_name\": \"Qwen3-8B\", \"seed\": 42}, \"conclusion\": \"negative\", \"checkpoint_path\": \"/root/struct_self_consist_ie/output/entity_consensus_results.json\", \"log_path\": \"/root/struct_self_consist_ie/output/entity_consensus_results.json\", \"completed_at\": \"2026-05-18T20:01:40.869Z\"}, \"exp_ccs_selection\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T19:59:48.671Z\", \"updated_at\": \"2026-05-18T20:01:39.128Z\", \"hypothesis\": \"Three-stage cascaded selection (degen→greedy, low-LP-range→entity MV, high-LP-range→LP) can outperform single-strategy selection by adapting to local confidence patterns\", \"spec\": {\"command\": \"python3 code/ccs_selection.py\", \"server\": \"autodl-5090\", \"data_path\": \"/root/struct_self_consist_ie/data/\", \"data_count\": \"all datasets\", \"model_name\": \"Qwen3-8B\", \"seed\": 42}, \"conclusion\": \"negative\", \"checkpoint_path\": \"/root/struct_self_consist_ie/output/ccs_selection_results.json\", \"log_path\": \"/root/struct_self_consist_ie/output/ccs_selection_results.json\", \"completed_at\": \"2026-05-18T20:01:39.128Z\"}, \"exp_017_llama_conll\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-14T14:39:32.014Z\", \"updated_at\": \"2026-05-18T19:11:03.240Z\", \"completed_at\": \"2026-05-14T17:12:15.687Z\", \"extra\": {\"previous_failure\": {\"conclusion\": \"success\"}}, \"hypothesis\": \"On CoNLL (high degeneracy regime), LLaMA should show the same pattern as Qwen3: LP selection fails due to narrow headroom, but structural signals retain diagnostic value (QE rho). Cross-model validation of the degeneracy-driven signal effectiveness framework.\", \"parent\": \"exp_007_llama_inference\", \"server\": \"autodl-5090\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"reproduce\": {\"server\": \"autodl-5090\", \"gpu\": \"cuda:1\", \"started_at\": \"2026-05-17T11:30:53.467Z\"}, \"metrics\": {\"degeneracy_cf1_gold_filtered\": 0.894, \"n_constant_f1\": 2465, \"n_gold_filtered\": 2756, \"n_total\": 3453, \"greedy_f1\": 0.9239, \"oracle_f1\": 0.9451, \"random_f1\": 0.9207, \"headroom_pp\": 2.11, \"dgs_f1\": 0.9254, \"dgs_delta_pp\": 0.14, \"dgs_nondegen_lp_delta_pp\": 1.37, \"selection_f1\": {\"SJ\": {\"f1\": 0.9237, \"delta_pp\": -0.04}, \"FK\": {\"f1\": 0.924, \"delta_pp\": -0.02}, \"VC\": {\"f1\": 0.925, \"delta_pp\": 0.08}, \"EM\": {\"f1\": 0.9244, \"delta_pp\": 0.02}, \"LP\": {\"f1\": 0.9244, \"delta_pp\": 0.02}}, \"qe_rho_full_3seed\": {\"SJ\": {\"mean\": 0.4631, \"sd\": 0.0074}, \"FK\": {\"mean\": 0.4546, \"sd\": 0.0061}, \"EM\": {\"mean\": 0.4603, \"sd\": 0.0078}, \"VC\": {\"mean\": 0.4579, \"sd\": 0.003}, \"LP\": {\"mean\": 0.3099, \"sd\": 0.0055}}, \"qe_auroc_full_3seed\": {\"SJ\": {\"mean\": 0.736, \"sd\": 0.0064}, \"FK\": {\"mean\": 0.732, \"sd\": 0.0063}, \"EM\": {\"mean\": 0.7355, \"sd\": 0.0069}, \"VC\": {\"mean\": 0.7394, \"sd\": 0.0041}, \"LP\": {\"mean\": 0.7629, \"sd\": 0.0044}}, \"lp_range\": {\"mean\": 0.0198, \"std\": 0.0315, \"median\": 0.0002}}, \"conclusion\": \"success\", \"spec\": {\"command\": \"python code/exp017_full_signal_analysis.py\", \"server\": \"autodl-5090\", \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_017_llama_conll_infer/samples.jsonl\", \"data_count\": 3453, \"model_name\": \"llama3.1-8b-conll2003-merged\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_017_llama_conll_infer/\", \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_017_llama_conll_infer/full_signal_analysis.json\"}}, \"exp_017_llama_conll_finetune\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T16:47:36.156Z\", \"updated_at\": \"2026-05-18T18:43:42.649Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/bin/activate && cd /root/autodl-tmp/struct_self_consist_ie && CUDA_VISIBLE_DEVICES=0 llamafactory-cli train train_config_llama_conll2003_3ep.yaml\\\"\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:0\"], \"pid\": \"674921\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_017_llama_conll_finetune.log\", \"submitted_at\": \"2026-05-18T16:47:35.786Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/data/conll2003/llmfactory_train.json\", \"data_count\": 14037, \"model_name\": \"Meta-Llama-3.1-8B-Instruct\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/checkpoints/llama3.1-8b-conll2003-lora-3ep\", \"checkpoint_source\": \"Meta-Llama-3.1-8B-Instruct (base model, LoRA from scratch)\", \"eval_data\": \"conll2003_uie_dev\", \"wall_clock_seconds\": 6176.5, \"gpu_hours\": 1.72}, \"hypothesis\": \"Structural self-consistency QE signals (SJ, FK, VC, EM) show model-agnostic diagnostic power: their Spearman rho with per-instance F1 should be comparable on LLaMA 3.1-8B as on Qwen 2.5-7B for CoNLL-2003 NER, even though degeneracy rates and absolute F1 may differ.\", \"parent\": \"exp_llama_fewnerd_lora\", \"conclusion\": \"success\", \"metrics\": {\"degeneracy_rate\": 0.853, \"greedy_f1\": 0.928, \"oracle_f1\": 0.951, \"headroom\": 0.023, \"selection_f1\": 0.934, \"full_rho_SJ\": 0.45, \"full_rho_FK\": 0.443, \"full_rho_VC\": 0.437, \"full_rho_EM\": 0.448, \"full_rho_LP\": 0.273, \"full_AUROC_SJ\": 0.752, \"full_AUROC_EM\": 0.753, \"full_AUROC_LP\": 0.739, \"cond_rho_SJ\": 0.454, \"cond_rho_EM\": 0.458, \"cond_rho_LP\": 0.311, \"cond_AUROC_EM\": 0.783, \"cond_AUROC_LP\": 0.804}, \"completed_at\": \"2026-05-18T18:30:32.331Z\"}, \"exp_028_entity_token_lp\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T18:22:18.594Z\", \"updated_at\": \"2026-05-18T18:23:06.601Z\", \"hypothesis\": \"Full-sequence mean LP underperforms as a quality signal because format/schema tokens dilute the entity-relevant logprob signal; isolating entity-only tokens should yield higher QE correlation and selection F1.\", \"conclusion\": \"negative\", \"spec\": {\"command\": \"python code/exp028_entity_token_lp_analysis.py\", \"server\": \"autodl-5090\", \"data_path\": \"output/exp_entity_token_lp/scierc/samples.jsonl\", \"data_count\": 529, \"model_name\": \"qwen3-8b-scierc-merged-v2\", \"seed\": 42, \"checkpoint_path\": \"checkpoints/qwen3-8b-scierc-merged-v2\", \"log_path\": \"output/exp_028_entity_token_lp/analysis_results.json\"}, \"completed_at\": \"2026-05-18T18:22:59.312Z\", \"metrics\": {\"greedy_f1\": 0.643, \"oracle_f1\": 0.7845, \"full_lp_global_rho\": 0.2971, \"entity_text_type_lp_global_rho\": 0.4401, \"full_lp_selection_f1\": 0.6465, \"entity_text_type_lp_selection_f1\": 0.6357, \"dilution_ratio\": 0.32, \"full_lp_within_range_median\": 0.0402, \"entity_text_type_within_range_median\": 0.1346, \"schema_only_within_range_median\": 0.0089}}, \"exp_026_t12_scierc\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T15:28:36.812Z\", \"updated_at\": \"2026-05-18T15:30:33.407Z\", \"hypothesis\": \"Higher temperature (T=1.2) reduces degeneracy rate and increases LP range on SciERC NER, but may degrade absolute generation quality\", \"spec\": {\"command\": \"python code/analyze_exp026_temp_5signal.py --data_path output/exp_026_t12/samples.jsonl --output_dir output/exp_026_t12/\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:3\"], \"pid\": \"665522\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_026_t12_scierc.log\", \"submitted_at\": \"2026-05-18T15:28:56.997Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"output/exp_026_t12/samples.jsonl\", \"data_count\": 551, \"model_name\": \"qwen3-8b-scierc-merged-v2\", \"seed\": 42, \"checkpoint_path\": \"checkpoints/qwen3-8b-scierc-merged-v2\", \"checkpoint_source\": \"ft_002_v2\", \"eval_data\": \"scierc_test_551\", \"wall_clock_seconds\": 96.4, \"gpu_hours\": 0.03}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T15:30:33.407Z\"}, \"exp_026_t08_scierc\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T15:28:36.084Z\", \"updated_at\": \"2026-05-18T15:30:31.219Z\", \"hypothesis\": \"Moderate temperature (T=0.8) provides intermediate degeneracy/LP-range tradeoff on SciERC NER, testing sensitivity of structural signals to temperature\", \"spec\": {\"command\": \"python code/analyze_exp026_temp_5signal.py --data_path output/exp_026_t08/samples.jsonl --output_dir output/exp_026_t08/\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:2\"], \"pid\": \"665386\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_026_t08_scierc.log\", \"submitted_at\": \"2026-05-18T15:28:55.394Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"output/exp_026_t08/samples.jsonl\", \"data_count\": 551, \"model_name\": \"qwen3-8b-scierc-merged-v2\", \"seed\": 42, \"checkpoint_path\": \"checkpoints/qwen3-8b-scierc-merged-v2\", \"checkpoint_source\": \"ft_002_v2\", \"eval_data\": \"scierc_test_551\", \"wall_clock_seconds\": 95.8, \"gpu_hours\": 0.03}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T15:30:31.219Z\"}, \"exp_026_t05_scierc\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T15:28:34.135Z\", \"updated_at\": \"2026-05-18T15:30:28.965Z\", \"hypothesis\": \"Lower temperature (T=0.5) increases degeneracy rate and reduces LP range on SciERC NER, as reduced sampling diversity causes more identical outputs\", \"spec\": {\"command\": \"python code/analyze_exp026_temp_5signal.py --data_path output/exp_026_t05/samples.jsonl --output_dir output/exp_026_t05/\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:0\"], \"pid\": \"665248\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_026_t05_scierc.log\", \"submitted_at\": \"2026-05-18T15:28:53.787Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"output/exp_026_t05/samples.jsonl\", \"data_count\": 551, \"model_name\": \"qwen3-8b-scierc-merged-v2\", \"seed\": 42, \"checkpoint_path\": \"checkpoints/qwen3-8b-scierc-merged-v2\", \"checkpoint_source\": \"ft_002_v2\", \"eval_data\": \"scierc_test_551\", \"wall_clock_seconds\": 95.2, \"gpu_hours\": 0.03}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T15:30:28.965Z\"}, \"exp_027_mlp_verifier\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T06:39:22.524Z\", \"updated_at\": \"2026-05-18T06:41:51.069Z\", \"metrics\": {\"lr_auroc\": 0.6522, \"mlp_auroc\": 0.6381, \"rf_auroc\": 0.5868, \"mlp_15feat_auroc\": 0.6341, \"lr_sel_f1\": 0.6406, \"mlp_sel_f1\": 0.6278, \"greedy_f1\": 0.6441, \"oracle_f1\": 0.8231, \"best_single_signal_auroc\": 0.6476, \"feature_bottleneck_confirmed\": true}, \"hypothesis\": \"MLP/RF等非线性模型能否通过组合5个QE信号(LP,SJ,FK,EM,VC)超越LR，或通过cross-signal interactions提取额外信息，从而缩小selection gap\", \"spec\": {\"command\": \"python train_mlp_verifier.py --n_samples 16 --cv_folds 5 --seeds 42,123,456\", \"server\": \"a100\", \"data_path\": \"output/exp_001_n16_seed*/samples.jsonl\", \"data_count\": 529, \"model_name\": \"sklearn LR/MLP/RF\", \"seed\": \"42,123,456\", \"checkpoint_path\": \"N/A\", \"log_path\": \"output/exp_027_mlp_verifier/\"}, \"conclusion\": \"negative\", \"completed_at\": \"2026-05-18T06:41:51.069Z\"}, \"exp_028_fewnerd_5epoch\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T07:53:12.913Z\", \"updated_at\": \"2026-05-17T20:29:42.274Z\", \"spec\": {\"hypothesis\": \"Few-NERD low degeneracy (10%) partially due to under-convergence at 3 epochs. 5 epochs should increase degeneracy as model becomes more confident, potentially reducing LP selection gain.\", \"parent\": \"exp_021_fewnerd_full\", \"command\": \"bash -c \\\"source /root/miniconda3/bin/activate && cd /root/autodl-tmp/struct_self_consist_ie && CUDA_VISIBLE_DEVICES=0,1,2,3 llamafactory-cli train train_config_fewnerd_5epoch_4gpu.yaml 2>&1 | tee logs/exp_028_4gpu_train.log\\\"\", \"server\": \"autodl-5090\", \"gpu\": \"cuda:0,1,2,3\", \"data_path\": \"data/fewnerd_uie_train\", \"data_count\": 131767, \"model_name\": \"Qwen3-8B LoRA rank=32\", \"seed\": 42, \"log_path\": \"logs/exp_028_4gpu_train.log\", \"checkpoint_path\": \"checkpoints/qwen3-8b-fewnerd-5epoch-lora\"}, \"conclusion\": \"negative\", \"metrics\": {\"degeneracy_cf1_gold\": 0.3133, \"greedy_f1\": 0.7773, \"lp_sel_delta_pp\": 0.624, \"lp_sel_f1\": 0.7835, \"oracle_f1\": 0.8723, \"within_instance_rho_mean\": 0.4066, \"within_instance_rho_median\": 0.6151}, \"hypothesis\": \"Few-NERD low degeneracy (10%) partially due to under-convergence at 3 epochs. 5 epochs should increase degeneracy as model becomes more confident, potentially reducing LP selection gain.\", \"completed_at\": \"2026-05-17T20:29:42.274Z\"}, \"exp_028\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-17T07:35:39.447Z\", \"updated_at\": \"2026-05-17T20:26:59.399Z\", \"hypothesis\": \"Few-NERD low degeneracy (10%) in exp-021 is NOT due to under-convergence at 3 epochs; training for 5 epochs will show similar degeneracy levels, confirming the structural property of this dataset rather than an artifact of insufficient training.\", \"failure_reason\": \"startup recovery: RUNNING with no cron and no server/pid info\", \"completed_at\": \"2026-05-17T12:09:43.334Z\", \"extra\": {\"previous_failure\": {\"conclusion\": \"failed\"}, \"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-17T20:06:01.040147+00:00\"}]}, \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/bin/activate && cd /root/autodl-tmp/struct_self_consist_ie && CUDA_VISIBLE_DEVICES=0,1,2,3 llamafactory-cli train train_config_fewnerd_5epoch_4gpu.yaml 2>&1 | tee logs/exp_028_4gpu_train.log\\\"\", \"server\": \"autodl-5090\", \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/data/fewnerd_uie_train\", \"data_count\": 131767, \"model_name\": \"Qwen3-8B LoRA rank=32\", \"seed\": 42, \"checkpoint_path\": \"checkpoints/qwen3-8b-fewnerd-5epoch-lora\", \"log_path\": \"logs/exp_028_4gpu_train.log\"}, \"reproduce\": {\"finished_at\": \"2026-05-17T20:05:57.260Z\"}, \"conclusion\": \"negative\", \"metrics\": {\"degeneracy_cf1_gold\": 0.313, \"greedy_f1\": 0.7773, \"lp_sel_f1\": 0.7835, \"lp_sel_delta_pp\": 0.62, \"oracle_f1\": 0.8723, \"within_instance_rho\": 0.4066, \"train_loss\": 0.0189, \"eval_loss\": 0.0311}}, \"exp_024_claim_audit\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T10:54:36.291Z\", \"updated_at\": \"2026-05-17T10:55:08.244Z\", \"hypothesis\": \"Systematic cross-chapter numerical consistency audit: verify all quantitative claims in paper against source experiment data, catch stale values and cross-reference errors before submission.\", \"conclusion\": \"success\", \"metrics\": {\"consistent\": 97, \"errors\": 1, \"warnings\": 5, \"old_residuals_found\": 0}, \"spec\": {\"checkpoint_path\": \"artifacts/exp_024_claim_audit/audit_report.md\", \"log_path\": \"N/A\", \"command\": \"CPU-only paper audit\", \"server\": \"local\", \"data_path\": \"docs/paper/\", \"data_count\": 0, \"model_name\": \"N/A\", \"seed\": 0}, \"completed_at\": \"2026-05-17T10:55:08.244Z\"}, \"exp_016_rerun_1024_bootstrap\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T23:44:21.577Z\", \"updated_at\": \"2026-05-17T03:33:39.786Z\", \"hypothesis\": \"3-seed bootstrap significance test for NER logprob vs greedy selection gap (+0.6pp). Tests whether the observed advantage is statistically significant.\", \"spec\": {\"command\": \"python code/bootstrap_significance.py\", \"server\": \"local\", \"data_path\": \"output/exp_016_rerun_1024/\", \"data_count\": 529, \"model_name\": \"N/A (statistical analysis)\", \"seed\": \"3-seed bootstrap (1000 iterations)\", \"checkpoint_path\": \"N/A\", \"log_path\": \"output/exp_016_rerun_1024_bootstrap/\"}, \"conclusion\": \"negative\", \"metrics\": {\"bootstrap_ci_95\": [-0.03, 0.042], \"permutation_p\": 0.39, \"cohen_d\": 0.038, \"sign_test_win_rate\": 0.466, \"ner_logprob_vs_greedy_delta\": 0.006, \"conclusion_summary\": \"NER selection: no signal significantly outperforms greedy; RE: same conclusion\"}, \"completed_at\": \"2026-05-14T23:44:48.818Z\", \"parent\": \"exp_016_rerun_1024\"}, \"exp_verbalized_confidence\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T02:45:20.552Z\", \"updated_at\": \"2026-05-17T03:33:39.197Z\", \"hypothesis\": \"Verbalized confidence baseline: let model self-rate extraction confidence. If also compressed → strengthens \\\"score compression is general\\\" claim. If effective → important positive finding requiring narrative adjustment.\", \"conclusion\": \"negative\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 python code/run_verbalized_confidence.py\", \"server\": \"autodl-5090\", \"data_path\": \"output/exp_012_rerun_1024/samples.jsonl + output/exp002_conll2003/samples.jsonl\", \"data_count\": 3285, \"model_name\": \"qwen3-8b-scierc-merged-v2 + qwen3-8b-conll2003-merged\", \"seed\": 42, \"checkpoint_path\": \"output/review_round9_experiments/verbalized_confidence/\", \"log_path\": \"output/review_round9_experiments/verbalized_confidence_run.log\"}, \"completed_at\": \"2026-05-16T03:09:39.916Z\", \"metrics\": {\"scierc\": {\"VerbConf_rho\": 0.2965, \"VerbConf_auroc\": 0.6811, \"VerbConf_sel_f1\": 0.6195, \"VerbConf_delta\": -0.0245, \"best_existing_rho\": 0.3792, \"VerbConf_mean\": 8.58, \"VerbConf_std\": 1.15, \"parse_fail_rate\": 0.0026}, \"conll\": {\"VerbConf_rho\": 0.3366, \"VerbConf_auroc\": 0.7469, \"VerbConf_sel_f1\": 0.8886, \"VerbConf_delta\": -0.0193, \"best_existing_rho\": 0.4507, \"VerbConf_mean\": 9.24, \"VerbConf_std\": 1.32, \"parse_fail_rate\": 0}}, \"parent\": \"exp_012_rerun_1024\"}, \"exp_entity_token_lp\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T05:39:44.631Z\", \"updated_at\": \"2026-05-17T03:33:38.371Z\", \"hypothesis\": \"Entity-token LP: test Discussion hypothesis (d) format-token dilution. Re-inference with per-token logprobs, then compute entity-only LP variance and selection F1. If entity-token LP compression is reduced → pilot remedy for LP selection. Also includes LP z-score normalization as zero-cost baseline. Addresses SF2+SF3 from Round 12.\", \"server\": \"autodl-5090\", \"gpu\": \"cuda:0,cuda:1\", \"account\": \"root\", \"reproduce\": {\"server\": \"autodl-5090\", \"gpu\": \"cuda:0,cuda:1\", \"started_at\": \"2026-05-16T05:41:33.768Z\"}, \"conclusion\": \"negative\", \"metrics\": {\"scierc_ner\": {\"greedy_f1\": 0.643, \"full_lp_sel_f1\": 0.6465, \"entity_lp_sel_f1\": 0.6262, \"oracle_f1\": 0.7845, \"entity_lp_delta_vs_full_lp\": -0.0203}, \"conll_ner\": {\"greedy_f1\": 0.9065, \"full_lp_sel_f1\": 0.8989, \"entity_lp_sel_f1\": 0.8659, \"oracle_f1\": 0.948, \"entity_lp_delta_vs_full_lp\": -0.033}, \"finding\": \"entity-token LP strictly worse than full-sequence LP; CoNLL entity tokens saturated (79.4% tied), SciERC entity tokens too sparse (5.3% of total)\"}, \"spec\": {\"command\": \"python analyze_entity_token_lp.py\", \"server\": \"autodl-5090\", \"data_path\": \"output/exp_012_rerun_1024/ + output/exp_002_conll_rerun_1024/\", \"data_count\": \"529 (SciERC NER) + 2756 (CoNLL NER)\", \"model_name\": \"Qwen3-8B (finetuned)\", \"seed\": 42, \"checkpoint_path\": \"artifacts/exp_entity_token_lp/results.json\", \"log_path\": \"artifacts/exp_entity_token_lp/report.md\"}, \"completed_at\": \"2026-05-16T06:28:46.845Z\", \"parent\": \"exp_012_rerun_1024\"}, \"exp_freeform_ablation\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T09:42:22.868Z\", \"updated_at\": \"2026-05-17T03:33:37.623Z\", \"spec\": {\"command\": \"python run_freeform_inference.py --seed 42 --num_samples 8 --temperature 1.0 --max_tokens 1024 --output_dir results/exp_freeform_ablation\", \"server\": \"autodl-5090\", \"gpu\": \"cuda:0\", \"pid\": \"169042\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_freeform_ablation.log\", \"submitted_at\": \"2026-05-15T09:42:30.236Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"hypothesis\": \"Free-form decoding recovers logprob variance and selection ability lost under constrained decoding\", \"plan_id\": \"exp-018\", \"data_path\": \"data/scierc/processed_data\", \"data_count\": 551, \"model_name\": \"qwen3-8b-scierc-merged-v2\", \"seed\": 42, \"tmux_session\": \"exp_freeform_ablation\", \"wall_clock_seconds\": 1059.0, \"gpu_hours\": 0.29}, \"conclusion\": \"negative\", \"metrics\": {\"lp_std_ratio_free_vs_constrained\": 0.97, \"lp_range_ratio\": 0.96, \"tied_fraction_constrained\": 0.597, \"tied_fraction_freeform\": 0.577, \"ner_selection_gap_constrained\": 0.0059, \"ner_selection_gap_freeform\": 0.0018, \"re_selection_gap_constrained\": -0.0068, \"re_selection_gap_freeform\": 0.0169, \"parse_rate\": 0.9995, \"ner_vc_rho_constrained\": 0.3792, \"ner_vc_rho_freeform\": 0.4089}, \"checkpoint_path\": \"N/A (inference-only experiment)\", \"completed_at\": \"2026-05-15T10:00:09.238Z\", \"hypothesis\": \"Free-form vs constrained decoding ablation on SciERC: test if removing JSON schema constraint changes LP variance distribution. If LP remains compressed under free-form, confirms compression is model-intrinsic not format-artifact.\", \"parent\": \"exp_012_rerun_1024\"}, \"exp_008_re_n16\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T12:03:06.876Z\", \"updated_at\": \"2026-05-17T02:58:19.490Z\", \"spec\": {\"hypothesis\": \"RE N=16 confirms negative finding with higher statistical power. If rho still <0.30, task-complexity boundary is robust.\", \"plan_id\": \"exp-008\", \"model_name\": \"qwen3-8b-scierc-merged-v2\", \"dataset\": \"SciERC\", \"gpu\": \"cuda:2\", \"server\": \"gpu-5090-4x-2\", \"gpu_budget_hours\": 12, \"description\": \"RE N=16 on SciERC to confirm negative finding. Inference with log-prob capture.\", \"priority\": \"P1\", \"command\": \"python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc/processed_data --dataset scierc --subtask joint --n_samples 16 --temperature 1.0 --seed 42 --collect_logprobs\", \"data_path\": \"data/scierc/processed_data\", \"data_count\": 551, \"seed\": 42, \"num_instances\": 200, \"partial\": true, \"note\": \"Only 200/551 instances due to --num_test default bug. Needs full rerun.\"}, \"metrics\": {\"ner\": {\"greedy_f1\": 0.6635, \"oracle_f1\": 0.8208, \"headroom\": 0.1572, \"rho_sj_full\": 0.377, \"rho_fk_full\": 0.2508, \"rho_logprob_full\": 0.3153, \"rho_sj_cond\": 0.3598, \"rho_fk_cond\": 0.2251, \"rho_logprob_cond\": 0.2927, \"sj_beats_fk\": true, \"rho_advantage\": 0.1262}, \"re\": {\"greedy_f1\": 0.4339, \"oracle_f1\": 0.6658, \"headroom\": 0.2319, \"rho_sj_full\": 0.2966, \"rho_fk_full\": 0.2871, \"rho_logprob_full\": 0.2986, \"rho_sj_cond\": 0.3975, \"rho_fk_cond\": 0.3774, \"rho_logprob_cond\": 0.2745, \"sj_beats_fk\": true, \"rho_advantage\": 0.0095}, \"verdict\": \"FAIL\"}, \"conclusion\": \"success\", \"checkpoint_path\": \"N/A\", \"log_path\": \"output/exp008_re_n16/\", \"completed_at\": \"2026-05-14T12:28:39.268Z\", \"hypothesis\": \"RE N=16 initial evaluation: first relation extraction test with structural signals. Establishes baseline RE signal effectiveness before pipeline corrections.\"}, \"exp_001_ner_n16_seed123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T12:46:06.430Z\", \"updated_at\": \"2026-05-17T02:58:18.225Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && CUDA_VISIBLE_DEVICES=3 python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc/processed_data --dataset scierc --subtask joint --n_samples 16 --temperature 1.0 --seed 123 --output_dir output/exp001_n16_seed123 --num_test 9999 --collect_logprobs 2>&1 | tee output/exp001_n16_seed123_run.log\\\"\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:3\"], \"pid\": \"63407\", \"log_path\": \"output/exp001_n16_seed123_run.log\", \"submitted_at\": \"2026-05-14T12:46:06.234Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_count\": 551, \"data_path\": \"data/scierc/processed_data\", \"model_name\": \"qwen3-8b-scierc-merged-v2\", \"seed\": 123, \"checkpoint_path\": \"output/exp001_n16_seed123/\", \"wall_clock_seconds\": 2748.0, \"gpu_hours\": 0.76}, \"conclusion\": \"success\", \"metrics\": {\"ner\": {\"greedy_f1\": 0.663, \"oracle_f1\": 0.809, \"headroom\": 0.146, \"rho_sj\": 0.423, \"rho_fk\": 0.29, \"rho_logprob\": 0.239, \"rho_sj_cond\": 0.423, \"rho_fk_cond\": 0.26}, \"re\": {\"greedy_f1\": 0.419, \"oracle_f1\": 0.625, \"headroom\": 0.206, \"rho_sj\": 0.267, \"rho_fk\": 0.315, \"rho_sj_cond\": 0.364, \"rho_fk_cond\": 0.331}, \"verdict\": \"FAIL\", \"verdict_note\": \"RE rho_sj=0.267 < 0.40; RE >30% samples F1=0\", \"n_instances\": 551, \"seed\": 123, \"N\": 16, \"T\": 1}, \"completed_at\": \"2026-05-14T13:31:54.232Z\", \"hypothesis\": \"SciERC NER N=16 seed=123: multi-seed validation at N=16. Tests seed stability for signal rankings with more samples.\"}, \"exp_007_ner_multi_model\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T11:42:20.748Z\", \"updated_at\": \"2026-05-17T02:58:16.747Z\", \"spec\": {\"command\": \"bash -c 'source env.sh && cd /root/autodl-tmp/struct_self_consist_ie && llamafactory-cli train train_config_llama.yaml'\", \"server\": \"gpu-5090-4x-2\", \"gpu\": [\"cuda:0\"], \"pid\": \"60970\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_007_ner_multi_model.log\", \"submitted_at\": \"2026-05-14T12:43:09.108Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/data\", \"data_count\": 1861, \"model_name\": \"LLaMA-3.1-8B-Instruct\", \"seed\": 42, \"log_file\": \"~/runs/struct_self_consist_ie/exp_007_ner_multi_model.log\", \"wall_clock_seconds\": 165.8, \"gpu_hours\": 0.05}, \"server\": \"autodl-5090\", \"gpu\": \"cuda:3\", \"account\": \"root\", \"reproduce\": {\"server\": \"autodl-5090\", \"gpu\": \"cuda:3\", \"started_at\": \"2026-05-14T11:43:50.977Z\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T12:45:54.952Z\", \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/checkpoints/llama3.1-8b-scierc-lora\", \"metrics\": {\"epoch\": 5, \"train_loss\": 0.0767, \"eval_loss\": 0.1049, \"train_runtime_sec\": 1494.5, \"train_samples_per_second\": 6.226, \"checkpoints\": [\"checkpoint-400\", \"checkpoint-500\", \"checkpoint-585\"], \"base_model\": \"Meta-Llama-3.1-8B-Instruct\", \"lora_r\": 32, \"lora_alpha\": 64, \"note\": \"EXIT_CODE=129 (SIGHUP) but training completed all 5 epochs before signal. Checkpoint fully intact.\"}, \"log_path\": \"~/runs/struct_self_consist_ie/exp_007_ner_multi_model.log\", \"hypothesis\": \"Multi-model NER comparison: evaluates signal effectiveness across Qwen and LLaMA on SciERC NER. Establishes cross-model generalization of structural>surface ranking.\"}, \"exp_003_ner_wnut17\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T11:42:17.544Z\", \"updated_at\": \"2026-05-17T02:58:14.928Z\", \"spec\": {\"merged_model_path\": \"/root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen3-8b-wnut17-merged\", \"pilot_command\": \"CUDA_VISIBLE_DEVICES=1 python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-wnut17-merged --data_dir data/wnut17 --dataset wnut17 --subtask ner --n_samples 16 --temperature 1.0 --seed 42 --output_dir output/exp003_wnut17_pilot --num_test 9999 --collect_logprobs\", \"pilot_pid\": 71498, \"pilot_server\": \"autodl-5090\", \"pilot_started_at\": \"2026-05-14T21:36:00Z\", \"test_samples\": 1287}, \"server\": \"autodl-5090\", \"gpu\": \"cuda:2\", \"account\": \"root\", \"reproduce\": {\"server\": \"autodl-5090\", \"gpu\": \"cuda:2\", \"started_at\": \"2026-05-14T11:43:50.537Z\", \"finished_at\": \"2026-05-14T12:53:13.262Z\", \"training_hours\": 1.16}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T12:53:14.768981+00:00\"}]}, \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen3-8b-wnut17-merged\", \"metrics\": {\"ner\": {\"greedy_f1\": 0.525, \"oracle_f1\": 0.664, \"headroom\": 0.139, \"rho_sj_full\": 0.082, \"rho_fk_full\": 0.124, \"rho_logprob_full\": -0.414, \"rho_sj_cond\": 0.275, \"rho_fk_cond\": 0.164, \"rho_logprob_cond\": 0.352, \"sj_beats_logprob_cond\": false}, \"n_instances\": 1287, \"n_gold_empty\": 598, \"sample_f1_mean\": 0.401, \"sample_f1_pct_zero\": 53.7, \"N\": 16, \"T\": 1, \"seed\": 42, \"verdict\": \"FAIL\", \"verdict_note\": \">30% samples F1=0; structural rho weak; logprob baseline stronger\"}, \"conclusion\": \"negative\", \"log_path\": \"output/exp003_wnut17_pilot/\", \"completed_at\": \"2026-05-14T13:40:20.979Z\", \"hypothesis\": \"WNUT-17 NER fine-tune + inference: initial attempt on social media domain. Tests if structural signals work when model capability is low on noisy text with novel entity types.\"}, \"exp_001_seed456_t10_full\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T13:27:41.067Z\", \"updated_at\": \"2026-05-17T02:58:12.996Z\", \"spec\": {\"command\": \"python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --dataset scierc --subtask joint --n_samples 16 --temperature 1.0 --seed 456 --num_test 9999 --collect_logprobs\", \"server\": \"autodl-5090\", \"data_path\": \"data/scierc/processed_data\", \"data_count\": 551, \"model_name\": \"qwen3-8b-scierc-merged-v2\", \"seed\": 456}, \"reproduce\": {\"finished_at\": \"2026-05-14T13:44:05.416Z\"}, \"failure_reason\": \"\", \"conclusion\": \"negative\", \"completed_at\": \"2026-05-14T13:44:05.021Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-14T13:44:10.317185+00:00\"}]}, \"metrics\": {\"ner\": {\"rho_sj\": 0.414, \"rho_fk\": 0.298}, \"re\": {\"rho_sj\": 0.268, \"rho_fk\": 0.26}, \"n_instances\": 551, \"N\": 16, \"T\": 1, \"seed\": 456, \"source\": \"reviewer_verified_report_json\"}, \"hypothesis\": \"SciERC NER seed=456 T=1.0 full: early multi-seed NER test before pipeline corrections. Preliminary evidence for seed stability.\"}, \"exp_001_seed123_t10_full\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T13:27:42.503Z\", \"updated_at\": \"2026-05-17T02:58:11.623Z\", \"spec\": {\"command\": \"python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --dataset scierc --subtask joint --n_samples 16 --temperature 1.0 --seed 123 --num_test 9999 --collect_logprobs\", \"server\": \"autodl-5090\", \"data_path\": \"data/scierc/processed_data\", \"data_count\": 551, \"model_name\": \"qwen3-8b-scierc-merged-v2\", \"seed\": 123}, \"reproduce\": {\"finished_at\": \"2026-05-14T13:44:13.823Z\"}, \"failure_reason\": \"\", \"conclusion\": \"negative\", \"completed_at\": \"2026-05-14T13:44:13.213Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-14T13:44:16.532801+00:00\"}]}, \"metrics\": {\"ner\": {\"rho_sj\": 0.417, \"rho_fk\": 0.283}, \"re\": {\"rho_sj\": 0.265, \"rho_fk\": 0.315}, \"n_instances\": 551, \"N\": 16, \"T\": 1, \"seed\": 123, \"source\": \"reviewer_verified_report_json\"}, \"hypothesis\": \"SciERC NER seed=123 T=1.0 full: early multi-seed NER test before pipeline corrections. Preliminary evidence for seed stability.\"}, \"exp_008_re_n16_t10_full\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T13:27:42.867Z\", \"updated_at\": \"2026-05-17T02:58:10.171Z\", \"spec\": {\"command\": \"python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --dataset scierc --subtask joint --n_samples 16 --temperature 1.0 --seed 42 --num_test 9999 --collect_logprobs\", \"server\": \"autodl-5090\", \"data_path\": \"data/scierc/processed_data\", \"data_count\": 551, \"model_name\": \"qwen3-8b-scierc-merged-v2\", \"seed\": 42}, \"reproduce\": {\"finished_at\": \"2026-05-14T13:44:18.988Z\"}, \"failure_reason\": \"\", \"conclusion\": \"negative\", \"completed_at\": \"2026-05-14T13:44:19.577Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-14T13:44:21.528032+00:00\"}]}, \"metrics\": {\"ner\": {\"rho_sj\": 0.444}, \"re\": {\"rho_sj\": 0.248}, \"n_instances\": 551, \"N\": 16, \"T\": 1, \"seed\": 42, \"mode\": \"RE-only\", \"source\": \"director_corrected\"}, \"hypothesis\": \"RE N=16 T=1.0 full dataset: early RE evaluation attempt. Tests structural signals on relation extraction before pipeline corrections.\"}, \"exp_007_llama_inference\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T13:54:48.055Z\", \"updated_at\": \"2026-05-17T02:58:03.014Z\", \"spec\": {\"command\": \"python run_mvp_pilot.py --model_path checkpoints/llama3.1-8b-scierc-merged --data_dir data/scierc/processed_data --dataset scierc --subtask joint --n_samples 8 --temperature 1.0 --seed 42 --num_test 9999 --collect_logprobs --output_dir output/exp007_llama_inference/\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:0\"], \"pid\": \"75172\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_007_llama_inference.log\", \"submitted_at\": \"2026-05-14T13:54:47.962Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/scierc/processed_data\", \"data_count\": 551, \"model_name\": \"Meta-Llama-3.1-8B-Instruct (LoRA fine-tuned on SciERC)\", \"seed\": 42, \"checkpoint_source\": \"checkpoints/llama3.1-8b-scierc-merged\", \"description\": \"LLaMA-3.1-8B SciERC joint inference (NER+RE) with 8 samples, T=1.0, logprobs collected.\", \"wall_clock_seconds\": 1038.5, \"gpu_hours\": 0.29}, \"log_path\": \"output/exp007_llama_inference/\", \"checkpoint_path\": \"N/A\", \"metrics\": {\"ner\": {\"greedy_f1\": 0.66, \"oracle_f1\": 0.781, \"headroom\": 0.121, \"rho_fk\": 0.327, \"rho_sj\": 0.363, \"rho_fk_cond\": 0.226, \"rho_sj_cond\": 0.311, \"rho_logprob\": 0.183, \"rho_logprob_cond\": 0.109, \"structural_beats_surface\": true, \"sample_f1_pct_zero\": 11.6}, \"re\": {\"greedy_f1\": 0.434, \"oracle_f1\": 0.568, \"headroom\": 0.135, \"rho_fk\": 0.305, \"rho_sj\": 0.299, \"rho_fk_cond\": 0.259, \"rho_sj_cond\": 0.405, \"rho_logprob\": 0.288, \"rho_logprob_cond\": 0.092, \"structural_beats_surface\": false, \"sample_f1_pct_zero\": 41.2}, \"n_instances\": 551, \"N\": 8, \"T\": 1, \"seed\": 42, \"model\": \"LLaMA-3.1-8B-Instruct\", \"verdict\": \"FAIL\", \"verdict_note\": \"RE rho_sj_full=0.299 < 0.40; >30% RE samples F1=0\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T14:12:06.442Z\", \"hypothesis\": \"LLaMA SciERC N=8 baseline: first cross-model test. Verifies structural signal effectiveness generalizes from Qwen to LLaMA model family on SciERC NER.\"}, \"exp_003_wnut17_eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T13:47:34.654Z\", \"updated_at\": \"2026-05-17T02:58:01.627Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-wnut17-merged --data_dir data/wnut17 --dataset wnut17 --subtask ner --n_samples 16 --temperature 1.0 --seed 42 --output_dir output/exp003_wnut17_eval --num_test 9999 --collect_logprobs\", \"server\": \"autodl-5090\", \"data_path\": \"data/wnut17\", \"data_count\": 1287, \"model_name\": \"qwen3-8b-wnut17-merged\", \"seed\": 42}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T14:08:17.429Z\", \"metrics\": {\"greedy_f1\": 0.523, \"oracle_f1\": 0.664, \"headroom\": 0.141, \"rho_fk\": 0.125, \"rho_sj\": 0.089, \"rho_fk_cond\": 0.169, \"rho_sj_cond\": 0.288, \"rho_logprob_full\": -0.409, \"rho_logprob_cond\": 0.35, \"structural_beats_surface\": false, \"sample_f1_pct_zero\": 53.7, \"n_instances\": 1287, \"N\": 16, \"T\": 1, \"seed\": 42, \"model\": \"Qwen3-8B\", \"n_gold_empty_filtered\": 598, \"verdict\": \"FAIL\", \"verdict_note\": \"structural_beats_surface=false; >50% samples F1=0\"}, \"hypothesis\": \"WNUT-17 NER evaluation: initial test on noisy social media domain. Tests boundary conditions for structural signal effectiveness on out-of-domain text.\"}, \"exp_010_selection_curves\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T15:01:53.585Z\", \"updated_at\": \"2026-05-17T02:58:00.378Z\", \"spec\": {\"command\": \"python3 code/exp010_selection_curves.py\", \"server\": \"autodl-5090\", \"data_path\": \"output/exp_001_seed42_v2, output/exp_008_re_n16_v2, output/exp002_conll2003\", \"data_count\": \"551+397+3453 instances\", \"model_name\": \"qwen3-8b-scierc-merged-v2\", \"seed\": 42, \"description\": \"Best-of-N selection curves: F1 vs N for 7 signals across 3 datasets\"}, \"conclusion\": \"success\", \"checkpoint_path\": \"N/A (analysis only)\", \"log_path\": \"/tmp/exp010.log\", \"completed_at\": \"2026-05-14T15:02:22.638Z\", \"metrics\": {\"scierc_ner\": {\"n_instances\": 551, \"greedy_f1\": 0.618, \"N16\": {\"oracle\": 0.787, \"SJ\": 0.62, \"FK\": 0.621, \"logprob\": 0.621, \"voting_conf\": 0.585, \"EM\": 0.606, \"random\": 0.595}, \"N8\": {\"oracle\": 0.752, \"SJ\": 0.614, \"FK\": 0.614, \"logprob\": 0.619, \"voting_conf\": 0.591, \"EM\": 0.603, \"random\": 0.589}, \"N4\": {\"oracle\": 0.714, \"SJ\": 0.607, \"FK\": 0.608, \"logprob\": 0.616, \"voting_conf\": 0.594, \"EM\": 0.6, \"random\": 0.587}}, \"scierc_re\": {\"n_instances\": 397, \"greedy_f1\": 0.403, \"N16\": {\"oracle\": 0.631, \"SJ\": 0.397, \"FK\": 0.396, \"logprob\": 0.41, \"voting_conf\": 0.408, \"EM\": 0.381, \"random\": 0.364}, \"N8\": {\"oracle\": 0.583, \"SJ\": 0.393, \"FK\": 0.394, \"logprob\": 0.413, \"voting_conf\": 0.398, \"EM\": 0.381, \"random\": 0.363}}, \"conll_ner\": {\"n_instances\": 3453, \"greedy_f1\": 0.725, \"N8\": {\"oracle\": 0.757, \"SJ\": 0.718, \"FK\": 0.717, \"logprob\": 0.716, \"voting_conf\": 0.714, \"EM\": 0.716, \"random\": 0.69}, \"N4\": {\"oracle\": 0.746, \"SJ\": 0.714, \"FK\": 0.714, \"logprob\": 0.715, \"voting_conf\": 0.714, \"EM\": 0.712, \"random\": 0.692}}}, \"hypothesis\": \"Selection curve analysis: plots selection F1 vs confidence threshold for each signal. Visualizes where correlation-selection gap emerges and at what confidence level signals become useful for filtering.\"}, \"exp_007_llama_seed456\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T15:08:50.628Z\", \"updated_at\": \"2026-05-17T02:57:59.595Z\", \"spec\": {\"description\": \"LLaMA 3.1-8B SciERC joint extraction, seed=456, cross-model robustness test\", \"hypothesis\": \"Structural consistency generalizes across model architectures (LLaMA vs Qwen)\", \"command\": \"CUDA_VISIBLE_DEVICES=2 PYTHONPATH=code python code/run_mvp_pilot.py --model_path checkpoints/llama3.1-8b-scierc-merged --data_dir data/scierc/processed_data --dataset scierc --subtask joint --n_samples 8 --temperature 1.0 --seed 456 --num_test 9999 --collect_logprobs --output_dir output/exp_007_llama_seed456\", \"server\": \"bjb1-21071\", \"data_path\": \"data/scierc/processed_data\", \"data_count\": 551, \"model_name\": \"llama3.1-8b-scierc-merged\", \"seed\": 456, \"gpu\": [\"cuda:2\"], \"backend\": \"tmux\", \"tmux_session\": \"exp007_s456\", \"account\": \"root\", \"log_path\": \"output/exp_007_llama_seed456/run.log\"}, \"conclusion\": \"negative\", \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_007_llama_seed456/run.log\", \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_007_llama_seed456/\", \"completed_at\": \"2026-05-14T15:19:20.693Z\", \"metrics\": {\"verdict\": \"FAIL\", \"ner\": {\"greedy_f1\": 0.6597, \"oracle_f1\": 0.7575, \"oracle_headroom\": 0.0978, \"fleiss_kappa\": 0.4543, \"soft_jaccard\": 0.7491, \"rho_kappa_f1\": 0.3115, \"rho_sj_f1\": 0.3663, \"structural_gt_surface\": true}, \"re\": {\"greedy_f1\": 0.4334, \"oracle_f1\": 0.5789, \"oracle_headroom\": 0.1455, \"fleiss_kappa\": 0.3791, \"soft_jaccard\": 0.6782, \"rho_kappa_f1\": 0.3013, \"rho_sj_f1\": 0.287, \"structural_gt_surface\": false}, \"logprob_ner\": {\"rho\": 0.1911, \"auroc\": 0.5989}, \"logprob_re\": {\"rho\": 0.3246, \"auroc\": 0.6678}, \"fail_reason\": \"RE rho_sj=0.2870 < 0.40 threshold; >30% samples F1=0\"}, \"hypothesis\": \"LLaMA SciERC seed=456: early cross-model multi-seed test. Verifies LLaMA NER signal pattern is reproducible across sampling seeds.\"}, \"exp_007_llama_seed123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T15:08:50.157Z\", \"updated_at\": \"2026-05-17T02:57:58.879Z\", \"spec\": {\"description\": \"LLaMA 3.1-8B SciERC joint extraction, seed=123, cross-model robustness test\", \"hypothesis\": \"Structural consistency generalizes across model architectures (LLaMA vs Qwen)\", \"command\": \"CUDA_VISIBLE_DEVICES=1 PYTHONPATH=code python code/run_mvp_pilot.py --model_path checkpoints/llama3.1-8b-scierc-merged --data_dir data/scierc/processed_data --dataset scierc --subtask joint --n_samples 8 --temperature 1.0 --seed 123 --num_test 9999 --collect_logprobs --output_dir output/exp_007_llama_seed123\", \"server\": \"bjb1-21071\", \"data_path\": \"data/scierc/processed_data\", \"data_count\": 551, \"model_name\": \"llama3.1-8b-scierc-merged\", \"seed\": 123, \"gpu\": [\"cuda:1\"], \"backend\": \"tmux\", \"tmux_session\": \"exp007_s123\", \"account\": \"root\", \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_007_llama_seed123/run.log\", \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_007_llama_seed123/\"}, \"conclusion\": \"negative\", \"completed_at\": \"2026-05-14T15:19:43.424Z\", \"metrics\": {\"verdict\": \"FAIL\", \"ner\": {\"greedy_f1\": 0.6605, \"oracle_f1\": 0.7703, \"headroom\": 0.1098, \"fleiss_kappa\": 0.4553, \"soft_jaccard\": 0.7525, \"rho_kappa_f1\": 0.2143, \"rho_sj_f1\": 0.3371, \"structural_gt_surface\": true}, \"re\": {\"greedy_f1\": 0.433, \"oracle_f1\": 0.5719, \"headroom\": 0.1389, \"fleiss_kappa\": 0.3851, \"soft_jaccard\": 0.6911, \"rho_kappa_f1\": 0.2844, \"rho_sj_f1\": 0.268, \"structural_gt_surface\": false}, \"fail_reasons\": [\"RE rho_sj=0.2680 < 0.40 threshold\", \">30% samples F1=0 (RE: 41.0%)\", \"RE structural not > surface (delta=-0.0165)\"]}, \"hypothesis\": \"LLaMA SciERC seed=123: early cross-model multi-seed test. Verifies LLaMA NER signal pattern is reproducible across sampling seeds.\"}, \"exp_008_re_seed123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T15:08:51.386Z\", \"updated_at\": \"2026-05-17T02:57:58.166Z\", \"spec\": {\"description\": \"RE N=16 on SciERC, seed=123, seed robustness test for relation extraction\", \"hypothesis\": \"Structural consistency correlates with per-instance RE F1, robust across seeds\", \"command\": \"CUDA_VISIBLE_DEVICES=3 PYTHONPATH=code python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc/processed_data --dataset scierc --subtask re --n_samples 16 --temperature 1.0 --seed 123 --num_test 9999 --collect_logprobs --output_dir output/exp_008_re_seed123\", \"server\": \"bjb1-21071\", \"data_path\": \"data/scierc/processed_data\", \"data_count\": 551, \"model_name\": \"qwen3-8b-scierc-merged-v2\", \"seed\": 123, \"gpu\": [\"cuda:3\"], \"backend\": \"tmux\", \"tmux_session\": \"exp008_rs123\", \"account\": \"root\", \"log_path\": \"output/exp_008_re_seed123/run.log\"}, \"log_path\": \"output/exp_008_re_seed123/run.log\", \"conclusion\": \"negative\", \"metrics\": {\"greedy_f1\": 0.4229, \"oracle_f1\": 0.6244, \"oracle_headroom\": 0.2015, \"fleiss_kappa_mean\": 0.3455, \"soft_jaccard_mean\": 0.6126, \"sample_f1_mean\": 0.3594, \"sample_f1_std\": 0.3793, \"sample_f1_zero_pct\": 44.1, \"structural_gt_surface\": false, \"rho_kappa_f1_full\": 0.3174, \"rho_sj_f1_full\": 0.2835, \"rho_kappa_f1_cond\": 0.0766, \"rho_sj_f1_cond\": 0.2877, \"logprob_auroc_full\": 0.6499, \"logprob_auroc_cond\": 0.5265, \"verdict\": \"FAIL\"}, \"checkpoint_path\": \"N/A\", \"completed_at\": \"2026-05-14T15:21:39.591Z\", \"hypothesis\": \"RE seed=123 multi-seed: tests reproducibility of RE signal rankings. Hypothesis: RE signals weaker than NER due to higher zero-F1 rate, but ranking should be seed-stable.\"}, \"exp_001_seed42_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T14:34:02.350Z\", \"updated_at\": \"2026-05-17T02:57:57.324Z\", \"spec\": {\"description\": \"NER N=16 on SciERC, seed=42, ft_002_v2, with logprobs\", \"hypothesis\": \"Structural consistency (Fleiss kappa, Soft Jaccard) correlates with per-instance NER F1 on SciERC\", \"server\": \"autodl-5090\", \"data_path\": \"data/scierc/processed_data\", \"data_count\": 551, \"model_name\": \"ft_002_v2\", \"seed\": 42, \"command\": \"CUDA_VISIBLE_DEVICES=1 PYTHONPATH=code python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc/processed_data --dataset scierc --subtask ner --n_samples 16 --temperature 1.0 --seed 42 --num_test 9999 --collect_logprobs --output_dir output/exp_001_seed42_v2\", \"gpu\": [\"cuda:1\"], \"pid\": \"78728\", \"backend\": \"tmux\", \"account\": \"root\", \"log_path\": \"output/exp_001_seed42_v2/run.log\"}, \"conclusion\": \"success\", \"metrics\": {\"sj_rho_full\": 0.428, \"sj_rho_cond\": 0.369, \"structural_minus_surface\": 0.147, \"conclusion_note\": \"NER seed42 robustness confirmed, structural>surface +0.147\"}, \"checkpoint_path\": \"N/A (inference)\", \"completed_at\": \"2026-05-14T15:23:34.091Z\", \"log_path\": \"output/exp_001_seed42_v2/\", \"hypothesis\": \"SciERC NER seed=42 v2: primary seed baseline under corrected pipeline. Establishes canonical signal rankings (SJ>FK>LP) for NER with gold-filtering.\"}, \"exp_001_seed123_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T14:34:04.210Z\", \"updated_at\": \"2026-05-17T02:57:42.106Z\", \"spec\": {\"description\": \"NER N=16 on SciERC, seed=123, ft_002_v2, with logprobs\", \"hypothesis\": \"Structural consistency (Fleiss kappa, Soft Jaccard) correlates with per-instance NER F1 on SciERC (seed robustness check)\", \"server\": \"autodl-5090\", \"data_path\": \"data/scierc/processed_data\", \"data_count\": 551, \"model_name\": \"ft_002_v2\", \"seed\": 123, \"command\": \"CUDA_VISIBLE_DEVICES=2 PYTHONPATH=code python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc/processed_data --dataset scierc --subtask ner --n_samples 16 --temperature 1.0 --seed 123 --num_test 9999 --collect_logprobs --output_dir output/exp_001_seed123_v2\", \"gpu\": [\"cuda:2\"], \"pid\": \"78733\", \"backend\": \"tmux\", \"account\": \"root\", \"log_path\": \"output/exp_001_seed123_v2/run.log\"}, \"conclusion\": \"success\", \"metrics\": {\"sj_rho_full\": 0.424, \"sj_rho_cond\": 0.376, \"structural_minus_surface\": 0.149, \"conclusion_note\": \"NER seed123 robustness confirmed, structural>surface +0.149\"}, \"checkpoint_path\": \"N/A (inference)\", \"completed_at\": \"2026-05-14T15:23:35.076Z\", \"log_path\": \"output/exp_001_seed123_v2/\", \"hypothesis\": \"SciERC NER seed=123 v2: second seed for multi-seed validation. Establishes reproducibility of structural>surface signal ranking across random seeds.\"}, \"exp_008_re_n16_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T14:34:06.296Z\", \"updated_at\": \"2026-05-17T02:57:41.178Z\", \"spec\": {\"description\": \"RE N=16 on SciERC full set confirmation, ft_002_v2, with logprobs\", \"hypothesis\": \"Structural consistency correlates with per-instance RE F1 on SciERC full dataset\", \"server\": \"autodl-5090\", \"data_path\": \"data/scierc/processed_data\", \"data_count\": 551, \"model_name\": \"ft_002_v2\", \"seed\": 42, \"command\": \"CUDA_VISIBLE_DEVICES=3 PYTHONPATH=code python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc/processed_data --dataset scierc --subtask re --n_samples 16 --temperature 1.0 --seed 42 --num_test 9999 --collect_logprobs --output_dir output/exp_008_re_n16_v2\", \"gpu\": [\"cuda:3\"], \"pid\": \"78737\", \"backend\": \"tmux\", \"account\": \"root\", \"log_path\": \"output/exp_008_re_n16_v2/run.log\"}, \"conclusion\": \"negative\", \"metrics\": {\"sj_rho_full\": 0.281, \"sj_rho_cond\": 0.308, \"f1_zero_pct\": 44.3, \"conclusion_note\": \"RE N=16 v2 negative: SJ weak, 44.3% F1=0\"}, \"checkpoint_path\": \"N/A (inference)\", \"completed_at\": \"2026-05-14T15:23:35.598Z\", \"log_path\": \"output/exp_008_re_n16_v2/\", \"hypothesis\": \"RE N=16 evaluation v2: tests structural signal effectiveness on relation extraction at higher sample count. Hypothesis: SJ/FK benefit from more samples on RE task where zero-F1 rate is high.\"}, \"exp_005_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T15:28:14.924Z\", \"updated_at\": \"2026-05-17T02:57:38.756Z\", \"spec\": {\"description\": \"Temperature sensitivity analysis: T=0.7 vs T=1.0 across 5 signals (SJ, FK, logprob, EM, voting_conf)\", \"command\": \"python code/analyze_exp005_v2_temperature.py\", \"server\": \"autodl-5090\", \"data_path\": \"output/mvp_pilot_004 + output/mvp_pilot_005 + output/exp_012_logprob\", \"data_count\": 551, \"model_name\": \"Qwen3-8B-SciERC-LoRA\", \"seed\": 42, \"checkpoint_path\": \"N/A\", \"log_path\": \"output/exp_005_v2_temperature/temperature_sensitivity_report.json\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T15:28:35.949Z\", \"hypothesis\": \"Selection F1 analysis v2: compute actual selection F1 (pick best sample by each signal) vs greedy and oracle. First evidence of correlation-selection gap under corrected pipeline.\"}, \"exp_006_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T15:30:02.348Z\", \"updated_at\": \"2026-05-17T02:57:36.914Z\", \"spec\": {\"command\": \"python3 code/exp_006_v2_selection.py\", \"server\": \"autodl-5090\", \"data_path\": \"output/exp_{001_seed42,001_seed123,002_conll,008_re}_v2/\", \"data_count\": 4952, \"model_name\": \"Qwen3-8B-SciERC-merged-v2\", \"seed\": 42}, \"conclusion\": \"negative\", \"checkpoint_path\": \"output/exp_006_v2/exp_006_v2_results.json\", \"log_path\": \"output/exp_006_v2_run.log\", \"completed_at\": \"2026-05-14T15:30:32.474Z\", \"metrics\": {\"NER_SciERC_s42\": {\"greedy\": 0.618, \"oracle\": 0.787, \"SJ\": 0.62, \"logprob\": 0.621, \"FK\": 0.621, \"EM\": 0.606, \"voting_conf\": 0.585, \"random\": 0.586}, \"NER_SciERC_s123\": {\"greedy\": 0.618, \"oracle\": 0.785, \"SJ\": 0.617, \"logprob\": 0.618, \"FK\": 0.621, \"EM\": 0.613, \"voting_conf\": 0.584, \"random\": 0.583}, \"NER_CoNLL\": {\"greedy\": 0.725, \"oracle\": 0.757, \"SJ\": 0.718, \"logprob\": 0.716, \"FK\": 0.717, \"EM\": 0.716, \"voting_conf\": 0.714, \"random\": 0.692}, \"RE_SciERC\": {\"greedy\": 0.403, \"oracle\": 0.631, \"SJ\": 0.397, \"logprob\": 0.41, \"FK\": 0.396, \"EM\": 0.381, \"voting_conf\": 0.408, \"random\": 0.364}}, \"hypothesis\": \"Temperature sensitivity v2: tests signal effectiveness at T=0.5,0.7,1.0,1.2. Hypothesis: structural signals are temperature-robust while LP degrades at extreme temperatures.\"}, \"exp_004_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T15:31:40.554Z\", \"updated_at\": \"2026-05-17T02:57:35.012Z\", \"conclusion\": \"success\", \"spec\": {\"command\": \"python code/analyze_exp004_v2_re_diagnostic.py\", \"server\": \"autodl-5090\", \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_012_logprob/samples_with_logprobs.jsonl\", \"data_count\": 551, \"model_name\": \"Qwen3-8B-SciERC-merged-v2\", \"seed\": 42, \"checkpoint_path\": \"N/A\", \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp004v2_re_diagnostic/\"}, \"completed_at\": \"2026-05-14T15:32:04.966Z\", \"hypothesis\": \"N-ablation v2 (N=4,8,16,32): tests how sample count affects signal ρ and selection F1. Validates N-scaling curve for structural vs surface signals under corrected pipeline.\"}, \"exp_009_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T15:36:47.946Z\", \"updated_at\": \"2026-05-17T02:57:32.655Z\", \"spec\": {\"command\": \"python3 code/exp_009_v2_stratification.py\", \"server\": \"autodl-5090\", \"data_path\": \"output/exp_001_seed42_v2 + exp_001_seed123_v2 + exp_008_re_n16_v2\", \"data_count\": 551, \"model_name\": \"analysis\", \"seed\": 42}, \"checkpoint_path\": \"output/exp_009_v2/results.json\", \"log_path\": \"output/exp_009_v2_run.log\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T15:37:18.311Z\", \"metrics\": {\"ner_seed42_global\": {\"sj_rho\": 0.431, \"fk_rho\": 0.325, \"logprob_rho\": 0.203, \"voting_conf_rho\": 0.475, \"em_rho\": 0.292}, \"ner_seed123_global\": {\"sj_rho\": 0.422, \"fk_rho\": 0.315, \"logprob_rho\": 0.226, \"voting_conf_rho\": 0.438, \"em_rho\": 0.299}, \"re_seed42_global\": {\"sj_rho\": 0.063, \"fk_rho\": 0.226, \"logprob_rho\": 0.4, \"voting_conf_rho\": 0.22, \"em_rho\": -0.132}, \"ner_seed_stability_max_delta\": 0.037, \"independent_proxies\": [\"sent_len\", \"ent_count\", \"type_diversity\"], \"inverted_u_ner\": \"not confirmed (ρ stable across independent proxies)\", \"inverted_u_re\": \"monotonic increase with complexity, not inverted-U\"}, \"hypothesis\": \"Capability stratification v2: corrected stratification with gold-filtering and extended to NER conditional analysis. Tests which instance subpopulations drive overall signal effectiveness.\"}, \"exp_016_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T15:39:07.501Z\", \"updated_at\": \"2026-05-17T02:57:30.726Z\", \"spec\": {\"command\": \"python code/exp_016_v2_ensemble.py\", \"server\": \"autodl-5090\", \"data_path\": \"output/exp_001_seed42_v2 + exp_001_seed123_v2 + exp_008_re_n16_v2\", \"data_count\": 551, \"model_name\": \"analysis_only\", \"seed\": 42, \"checkpoint_path\": \"output/exp_016_v2/\", \"log_path\": \"/tmp/exp016v2.log\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T15:39:34.478Z\", \"metrics\": {\"ner_conditional\": {\"n\": 529, \"best_single_signal_rho\": {\"soft_jaccard\": 0.4412}, \"best_combo_rho\": {\"sj+vc_a0.55\": 0.4552}, \"ensemble_auroc\": 0.7141, \"best_single_auroc\": {\"soft_jaccard\": 0.7166}, \"selection_f1\": {\"greedy\": 0.6442, \"logprob_best\": 0.6505, \"ensemble_best\": 0.6475, \"sj_best\": 0.6471, \"oracle\": 0.8442}}, \"re_conditional\": {\"n\": 397, \"best_single_signal_rho\": {\"voting_confidence\": 0.3849}, \"best_combo_rho\": {\"logprob+vc_a0.25\": 0.3936}, \"ensemble_auroc\": 0.6916, \"best_single_auroc\": {\"voting_confidence\": 0.7023}, \"selection_f1\": {\"greedy\": 0.403, \"logprob_best\": 0.4097, \"ensemble_best\": 0.4227, \"oracle\": 0.6306}}, \"re_full\": {\"ensemble_auroc\": 0.8608, \"best_single_auroc\": {\"voting_confidence\": 0.8248}}}, \"hypothesis\": \"Bootstrap significance v2: corrected bootstrap test for NER selection F1 gap with proper gold-filtering and multiple signals. Establishes which selection improvements are statistically significant.\"}, \"exp_001_seed456_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T15:38:55.569Z\", \"updated_at\": \"2026-05-17T02:57:23.336Z\", \"spec\": {\"hypothesis\": \"NER/RE N=16 seed=456 robustness test, third seed for 3-seed stability\", \"plan_id\": \"exp-001\", \"command\": \"CUDA_VISIBLE_DEVICES=2 PYTHONPATH=code python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc/processed_data --dataset scierc --subtask joint --n_samples 16 --temperature 1.0 --seed 456 --num_test 9999 --collect_logprobs --output_dir output/exp_001_seed456_v2\", \"server\": \"autodl-5090\", \"data_path\": \"data/scierc/processed_data\", \"data_count\": 551, \"model_name\": \"qwen3-8b-scierc-merged-v2\", \"seed\": 456, \"metrics\": {\"full_rho_kappa_f1\": 0.3383, \"full_rho_sj_f1\": 0.2988, \"cond_rho_kappa_f1\": 0.233, \"cond_rho_sj_f1\": 0.3245, \"logprob_full_rho\": 0.3405, \"logprob_full_auroc\": 0.6694, \"logprob_cond_rho\": 0.0501, \"structural_gt_surface\": false}, \"note\": \"CRITICAL: Ran with --subtask joint instead of --subtask ner. seed42/seed123 v2 used --subtask ner. Results valid for joint-mode analysis but NOT comparable for NER 3-seed protocol. Need NER-only rerun.\", \"log_path\": \"output/exp_001_seed456_v2/run.log\", \"checkpoint_path\": \"output/exp_001_seed456_v2/\"}, \"conclusion\": \"negative\", \"completed_at\": \"2026-05-14T17:12:14.682Z\", \"hypothesis\": \"SciERC joint NER+RE seed=456 v2: early pipeline version. Tests multi-seed stability of signal rankings on joint extraction task.\"}, \"exp_017_llama_conll_infer\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T17:33:23.653Z\", \"updated_at\": \"2026-05-17T02:57:21.948Z\", \"spec\": {\"hypothesis\": \"LLaMA-3.1-8B CoNLL-2003 inference: cross-model cross-dataset validation of structural consistency signals\", \"plan_id\": \"exp-017\", \"parent\": \"exp_017_llama_conll\", \"command\": \"python code/run_llama_conll_infer.py\", \"server\": \"autodl-5090\", \"data_path\": \"conll2003 test\", \"data_count\": 3453, \"model_name\": \"LLaMA-3.1-8B-Instruct\", \"seed\": 42, \"n_samples\": 8, \"temperature\": 1, \"description\": \"LLaMA CoNLL-2003 NER inference N=8 (cross-model + cross-dataset validation)\"}, \"metrics\": {\"greedy_f1\": 0.9266, \"oracle_f1\": 0.9443, \"oracle_headroom\": 0.0177, \"n_instances\": 3453, \"n_valid\": 2756, \"n_conditional\": 2642, \"N\": 8, \"full\": {\"SJ_rho\": 0.4314, \"FK_rho\": 0.4277, \"logprob_rho\": 0.3072, \"EM_rho\": 0.4306, \"voting_conf_rho\": 0.4256, \"SJ_AUROC\": 0.7039, \"FK_AUROC\": 0.7026, \"logprob_AUROC\": 0.761, \"EM_AUROC\": 0.7046, \"voting_conf_AUROC\": 0.7088, \"SJ_ECE\": 0.1137, \"FK_ECE\": 0.1053, \"logprob_ECE\": 0.129, \"EM_ECE\": 0.1094, \"voting_conf_ECE\": 0.0949}, \"conditional\": {\"SJ_rho\": 0.4356, \"FK_rho\": 0.431, \"logprob_rho\": 0.3282, \"EM_rho\": 0.4403, \"voting_conf_rho\": 0.3743, \"SJ_AUROC\": 0.7225, \"FK_AUROC\": 0.7208, \"logprob_AUROC\": 0.8102, \"EM_AUROC\": 0.7257, \"voting_conf_AUROC\": 0.6989, \"SJ_ECE\": 0.0829, \"FK_ECE\": 0.0796, \"logprob_ECE\": 0.0922, \"EM_ECE\": 0.0754, \"voting_conf_ECE\": 0.0784}}, \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_017_llama_conll_infer/samples.jsonl\", \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_017_llama_conll_infer/\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T17:55:33.476Z\", \"notes\": \"LLaMA CoNLL-2003 NER N=8 (not N=16, cost constraint: 3453 test instances). SJ ρ=0.431 > logprob ρ=0.307 (Δ=+0.124). ρ-AUROC dissociation: logprob AUROC=0.761 > SJ AUROC=0.704. All 4 structural signals ρ>0.42 vs logprob 0.31. Directly comparable to exp_002 (Qwen CoNLL N=8) and exp_007 (LLaMA SciERC N=8).\", \"hypothesis\": \"LLaMA CoNLL N=8 baseline inference: initial cross-model test on CoNLL before scaling to N=16. Establishes LLaMA can do CoNLL NER effectively.\"}, \"exp_003_wnut17_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T15:32:56.415Z\", \"updated_at\": \"2026-05-17T02:57:20.068Z\", \"spec\": {\"description\": \"WNUT-17 retrain: downsample gold-empty instances to ≤25%, fine-tune Qwen3-8B, inference N=16 T=1.0 with log-probs\", \"hypothesis\": \"After removing excess empty instances, structural consistency signals (SJ) will show stronger correlation on social media NER\", \"plan_id\": \"exp-003\", \"claim\": 1, \"model_name\": \"Qwen3-8B\", \"dataset\": \"WNUT-17 (downsampled)\", \"priority\": \"P0\", \"parent\": \"exp_003_ner_wnut17\", \"command\": \"CUDA_VISIBLE_DEVICES=1 llamafactory-cli train train_config_wnut17.yaml\", \"server\": \"autodl-5090\", \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/data/wnut17/llmfactory_train_downsampled.json\", \"data_count\": 1637, \"seed\": 42, \"pid\": 92215, \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/logs/train_wnut17.log\", \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen3-8b-wnut17-lora\", \"downsampling\": \"empty instances 63.8% -> 25.0%, total 3394 -> 1637\", \"metrics\": {\"train_loss\": 0.105, \"eval_loss\": 0.0836, \"epochs\": 5, \"train_time_min\": 16.37, \"train_samples_per_sec\": 8.33}, \"note\": \"D045: Training succeeded (train_loss=0.105) but inference FAIL: 54% F1=0, SJ rho=0.062 (p=0.106). WNUT-17 abandoned — model capability insufficient on social media NER. Paper reports as Claim 3 (capability boundary) evidence.\"}, \"conclusion\": \"negative\", \"completed_at\": \"2026-05-14T18:11:36.559Z\", \"hypothesis\": \"WNUT-17 NER evaluation v2: tests signal effectiveness on noisy social media text. Hypothesis: structural signals remain effective on noisy, informal text with high entity variation.\"}, \"exp_001_seed456_v2_ner\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T17:13:00.414Z\", \"updated_at\": \"2026-05-17T02:57:18.227Z\", \"spec\": {\"hypothesis\": \"NER N=16 seed=456 robustness test (NER-only rerun, fixing subtask mismatch from exp_001_seed456_v2)\", \"plan_id\": \"exp-001\", \"parent\": \"exp_001_seed456_v2\", \"command\": \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && CUDA_VISIBLE_DEVICES=2 PYTHONPATH=code python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc/processed_data --dataset scierc --subtask ner --n_samples 16 --temperature 1.0 --seed 456 --num_test 9999 --collect_logprobs --output_dir output/exp_001_seed456_v2_ner\", \"server\": \"autodl-5090\", \"data_path\": \"data/scierc/processed_data\", \"data_count\": 551, \"model_name\": \"qwen3-8b-scierc-merged-v2\", \"seed\": 456, \"checkpoint_source\": \"checkpoints/qwen3-8b-scierc-merged-v2\", \"eval_data\": \"data/scierc/processed_data\", \"metrics\": {\"sj_rho\": 0.384, \"structural_gt_surface\": true, \"structural_surface_delta\": 0.16}, \"log_path\": \"output/exp_001_seed456_v2_ner.log\", \"checkpoint_path\": \"output/exp_001_seed456_v2_ner/\"}, \"log_path\": \"output/exp_001_seed456_v2_ner.log\", \"pid\": 96161, \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T17:52:01.372Z\", \"metrics\": {\"full\": {\"SJ\": {\"rho\": 0.384, \"auroc\": 0.711}, \"FK\": {\"rho\": 0.223, \"auroc\": 0.577}, \"logprob\": {\"rho\": 0.232, \"auroc\": 0.594}, \"EM\": {\"rho\": 0.316, \"auroc\": 0.768}, \"voting_conf\": {\"rho\": 0.411, \"auroc\": 0.712}}, \"conditional\": {\"SJ\": {\"rho\": 0.349, \"auroc\": 0.699}, \"FK\": {\"rho\": 0.157, \"auroc\": 0.561}, \"logprob\": {\"rho\": 0.171, \"auroc\": 0.576}, \"EM\": {\"rho\": 0.406, \"auroc\": 0.78}, \"voting_conf\": {\"rho\": 0.346, \"auroc\": 0.694}}, \"3seed_mean_SJ_rho_full\": 0.412, \"3seed_sd_SJ_rho_full\": 0.025, \"structural_beats_surface\": true, \"verdict\": \"MARGINAL\"}, \"hypothesis\": \"SciERC NER seed=456 v2: corrected pipeline rerun with gold-filtering. Part of multi-seed validation protocol for NER signal ranking stability.\"}, \"exp_009_v2_re_rerun\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T18:56:31.535Z\", \"updated_at\": \"2026-05-17T02:57:16.383Z\", \"spec\": {\"command\": \"python code/exp_009_v2_re_rerun.py\", \"server\": \"autodl-5090\", \"data_path\": \"output/exp_008_re_n16_v2/samples.jsonl\", \"data_count\": 397, \"model_name\": \"cpu_analysis\", \"seed\": 42, \"checkpoint_source\": \"exp_008_re_n16_v2\", \"checkpoint_path\": \"output/exp_009_v2_re_rerun/results.json\", \"log_path\": \"/tmp/re_rerun.log\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T18:56:58.168Z\", \"hypothesis\": \"Capability stratification v2 (RE rerun): corrected stratification analysis for RE with proper gold-filtering. Fixes early pipeline bug affecting RE quartile ρ values.\"}, \"exp_007_llama_n16\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T18:31:44.366Z\", \"updated_at\": \"2026-05-17T02:57:12.521Z\", \"spec\": {\"hypothesis\": \"LLaMA SciERC N=16: cross-model N-scaling validation. If SJ rho increases from N=8 (0.363) to N=16, N-scaling is model-agnostic.\", \"plan_id\": \"exp-007\", \"parent\": \"exp_007_llama_inference\", \"command\": \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && CUDA_VISIBLE_DEVICES=1 PYTHONPATH=code python code/run_mvp_pilot.py --model_path checkpoints/llama3.1-8b-scierc-merged --data_dir data/scierc/processed_data --dataset scierc --subtask ner --n_samples 16 --temperature 1.0 --seed 42 --num_test 9999 --collect_logprobs --output_dir output/exp_007_llama_n16\", \"server\": \"autodl-5090\", \"data_path\": \"data/scierc/processed_data\", \"data_count\": 551, \"model_name\": \"llama3.1-8b-scierc-merged\", \"seed\": 42, \"checkpoint_source\": \"checkpoints/llama3.1-8b-scierc-merged\", \"eval_data\": \"data/scierc/processed_data\"}, \"conclusion\": \"success\", \"checkpoint_path\": \"output/exp_007_llama_n16/samples.jsonl\", \"log_path\": \"output/exp_007_llama_n16.log\", \"completed_at\": \"2026-05-14T19:03:39.163Z\", \"metrics\": {\"N\": 16, \"dataset\": \"scierc\", \"subtask\": \"ner\", \"n_instances\": 551, \"n_valid\": 529, \"n_conditional\": 478, \"greedy_f1\": 0.645, \"full\": {\"SJ_rho\": 0.3791, \"FK_rho\": 0.3081, \"logprob_rho\": 0.2041, \"EM_rho\": 0.3159, \"voting_conf_rho\": 0.4515, \"SJ_AUROC\": 0.717, \"FK_AUROC\": 0.6581, \"logprob_AUROC\": 0.5656, \"EM_AUROC\": 0.7686, \"voting_conf_AUROC\": 0.7266, \"SJ_ECE\": 0.1019, \"FK_ECE\": 0.1556, \"logprob_ECE\": 0.084, \"EM_ECE\": 0.1761, \"voting_conf_ECE\": 0.1365}, \"conditional\": {\"SJ_rho\": 0.3222, \"FK_rho\": 0.2182, \"logprob_rho\": 0.1286, \"EM_rho\": 0.3563, \"voting_conf_rho\": 0.3356, \"SJ_AUROC\": 0.7014, \"FK_AUROC\": 0.6392, \"logprob_AUROC\": 0.545, \"EM_AUROC\": 0.7708, \"voting_conf_AUROC\": 0.6988, \"SJ_ECE\": 0.1466, \"FK_ECE\": 0.1853, \"logprob_ECE\": 0.1141, \"EM_ECE\": 0.1887, \"voting_conf_ECE\": 0.2634}, \"n8_vs_n16_delta_rho_full\": {\"SJ\": 0.0161, \"FK\": -0.0185, \"logprob\": 0.0214, \"EM\": 0.0007, \"voting_conf\": 0.0184}}, \"hypothesis\": \"LLaMA SciERC N=16: cross-model NER signal evaluation at higher sample count. Tests if LLaMA shows same N-scaling benefit for structural signals as Qwen.\"}, \"exp_017_llama_conll_n16\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T19:19:35.318Z\", \"updated_at\": \"2026-05-17T02:56:57.283Z\", \"spec\": {\"hypothesis\": \"LLaMA CoNLL N=16: complete the 2x2 matrix (model x dataset x N). If SJ N-scaling holds for LLaMA on CoNLL, the finding is fully cross-model cross-dataset.\", \"plan_id\": \"exp-017\", \"parent\": \"exp_017_llama_conll_infer\", \"model_name\": \"llama3.1-8b-conll2003-merged\", \"dataset\": \"CoNLL-2003\", \"data_count\": 3453, \"seed\": 42, \"server\": \"autodl-5090\", \"command\": \"CUDA_VISIBLE_DEVICES=0 PYTHONPATH=code python code/run_mvp_pilot.py --model_path checkpoints/llama3.1-8b-conll2003-merged --data_dir data/conll2003 --dataset conll2003 --subtask ner --n_samples 16 --temperature 1.0 --seed 42 --num_test 9999 --collect_logprobs --output_dir output/exp_017_llama_conll_n16\", \"data_path\": \"data/conll2003\", \"pid\": 106997, \"n_samples\": 16, \"temperature\": 1, \"checkpoint_source\": \"checkpoints/llama3.1-8b-conll2003-merged\", \"eval_data\": \"conll2003 test set\", \"checkpoint_path\": \"output/exp_017_llama_conll_n16/samples.jsonl\", \"log_path\": \"output/exp_017_llama_conll_n16/all_signals_report.json\"}, \"metrics\": {\"greedy_f1\": 0.9243, \"oracle_f1\": 0.9487, \"oracle_headroom\": 0.0244, \"n_instances\": 3453, \"n_valid\": 2756, \"n_conditional\": 2642, \"structural_beats_surface\": true, \"full\": {\"SJ_rho\": 0.4642, \"SJ_AUROC\": 0.7391, \"SJ_ECE\": 0.1131, \"FK_rho\": 0.4566, \"FK_AUROC\": 0.736, \"FK_ECE\": 0.1071, \"logprob_rho\": 0.3058, \"logprob_AUROC\": 0.7594, \"logprob_ECE\": 0.1288, \"EM_rho\": 0.4613, \"EM_AUROC\": 0.7391, \"EM_ECE\": 0.1084, \"voting_conf_rho\": 0.4554, \"voting_conf_AUROC\": 0.7406, \"voting_conf_ECE\": 0.0844}, \"conditional\": {\"SJ_rho\": 0.4597, \"SJ_AUROC\": 0.7565, \"SJ_ECE\": 0.0846, \"FK_rho\": 0.4515, \"FK_AUROC\": 0.753, \"FK_ECE\": 0.0813, \"logprob_rho\": 0.3193, \"logprob_AUROC\": 0.8023, \"logprob_ECE\": 0.0921, \"EM_rho\": 0.4618, \"EM_AUROC\": 0.7589, \"EM_ECE\": 0.0757, \"voting_conf_rho\": 0.3978, \"voting_conf_AUROC\": 0.7287, \"voting_conf_ECE\": 0.0742}, \"best_of_n\": {\"greedy\": 0.9243, \"random_avg\": 0.9213, \"sj_best\": 0.9259, \"logprob_best\": 0.925, \"voting_conf_best\": 0.9268, \"oracle\": 0.9487}, \"n8_vs_n16_delta\": {\"full_SJ_rho_delta\": 0.0328, \"full_FK_rho_delta\": 0.0289, \"full_logprob_rho_delta\": -0.0014, \"full_EM_rho_delta\": 0.0307, \"full_voting_conf_rho_delta\": 0.0298, \"cond_SJ_rho_delta\": 0.0241, \"cond_FK_rho_delta\": 0.0205, \"cond_logprob_rho_delta\": -0.0089, \"cond_EM_rho_delta\": 0.0215, \"cond_voting_conf_rho_delta\": 0.0235}}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T19:45:16.265Z\", \"hypothesis\": \"LLaMA CoNLL N=16 seed=42 (original): cross-model validation on CoNLL. First evidence that structural>surface ranking generalizes from Qwen to LLaMA model family.\"}, \"exp_015_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T15:34:23.336Z\", \"updated_at\": \"2026-05-17T02:56:55.830Z\", \"spec\": {\"command\": \"python code/analyze_exp015_v2_metrics.py\", \"server\": \"autodl-5090\", \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/ (10 datasets)\", \"data_count\": 9148, \"model_name\": \"Qwen3-8B + LLaMA (multi-model)\", \"seed\": \"42,123,456 (multi-seed)\", \"checkpoint_path\": \"N/A (analysis only)\", \"log_path\": \"/tmp/exp015_v2.log\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T15:34:56.741Z\", \"metrics\": {\"scierc_ner_avg\": {\"sj_auroc\": 0.7394, \"fk_auroc\": 0.6172, \"em_auroc\": 0.7873, \"voting_auroc\": 0.7367, \"logprob_auroc\": 0.5918}, \"scierc_re_avg\": {\"sj_auroc\": 0.6746, \"fk_auroc\": 0.5939, \"em_auroc\": 0.715, \"voting_auroc\": 0.7234, \"logprob_auroc\": 0.5849}}, \"hypothesis\": \"Metrics expansion v2: corrected evaluation with proper conditional filtering. Updates exp_015 with gold-filtered pipeline to fix RE conditional ρ values that used wrong filter criterion.\"}, \"exp_001_n16_seed456\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-14T12:10:30.350Z\", \"updated_at\": \"2026-05-17T02:56:53.526Z\", \"completed_at\": \"2026-05-14T12:28:38.721Z\", \"extra\": {\"previous_failure\": {\"conclusion\": \"success\", \"metrics\": {\"ner\": {\"greedy_f1\": 0.6577, \"oracle_f1\": 0.8129, \"headroom\": 0.1553, \"rho_sj_full\": 0.3297, \"rho_fk_full\": 0.2578, \"rho_logprob_full\": 0.2866, \"rho_sj_cond\": 0.3394, \"rho_fk_cond\": 0.2721, \"rho_logprob_cond\": 0.2567, \"sj_beats_fk\": true, \"rho_advantage\": 0.0719}, \"re\": {\"greedy_f1\": 0.4312, \"oracle_f1\": 0.6737, \"headroom\": 0.2425, \"rho_sj_full\": 0.285, \"rho_fk_full\": 0.2372, \"rho_logprob_full\": 0.2626, \"rho_sj_cond\": 0.3525, \"rho_fk_cond\": 0.2614, \"rho_logprob_cond\": 0.1927, \"sj_beats_fk\": true, \"rho_advantage\": 0.0478}, \"verdict\": \"FAIL\"}}}, \"spec\": {\"hypothesis\": \"N=16 seed456 multi-seed robustness verification for SciERC NER+RE\", \"plan_id\": \"exp-001\", \"model_name\": \"qwen3-8b-scierc-merged-v2\", \"data_path\": \"data/scierc/processed_data\", \"data_count\": 551, \"seed\": 456, \"command\": \"python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc/processed_data --dataset scierc --subtask joint --n_samples 16 --temperature 1.0 --seed 456 --output_dir output/exp001_n16_seed456 --collect_logprobs\", \"server\": \"autodl-5090\", \"gpu\": \"cuda:0\", \"pid\": \"174595\", \"log_path\": \"output/exp001_n16_seed456_run.log\", \"tmux_session\": \"exp_001_n16_seed456\"}, \"conclusion\": \"success\", \"checkpoint_path\": \"N/A (inference-only)\", \"metrics\": {\"instance_count\": 551, \"n_valid\": 529, \"n_gold_empty\": 22, \"parse_rate\": 1, \"ner_greedy_f1\": 0.6617, \"ner_oracle_f1\": 0.8075, \"re_greedy_f1\": 0.4215, \"re_oracle_f1\": 0.4748, \"rho_sj_ner\": 0.4098, \"rho_fk_ner\": 0.2723, \"rho_vc_ner\": 0.4449, \"rho_em_ner\": 0.3363, \"rho_lp_ner\": 0.2415, \"rho_sj_re\": 0.2835, \"rho_fk_re\": 0.2929, \"auroc_sj_ner\": 0.6823, \"auroc_fk_ner\": 0.6179, \"auroc_vc_ner\": 0.6981, \"auroc_em_ner\": 0.649, \"auroc_lp_ner\": 0.5885, \"rho_note\": \"CORRECTED 2026-05-15: old values (rho_fk=0.3448,rho_sj=0.4134) included 22 gold-empty instances. Now uses gold-filtered pipeline (n=529).\"}, \"log_path\": \"output/exp001_n16_seed456_run.log\", \"hypothesis\": \"SciERC N=16 seed=456: early multi-seed validation of structural signal rankings at N=16 sample count. Establishes seed stability for SJ/FK/VC/EM ordering.\"}, \"exp_011_ood_scierc_to_conll\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T11:36:07.210Z\", \"updated_at\": \"2026-05-17T02:56:29.417Z\", \"spec\": {\"hypothesis\": \"SCS structural signals remain effective under domain shift (SciERC model on CoNLL data)\", \"plan_id\": \"exp-011\", \"model_name\": \"qwen3-8b-scierc-merged-v2\", \"data_path\": \"data/conll2003\", \"seed\": 42, \"pid\": 179761, \"server\": \"autodl-5090\", \"gpu\": \"cuda:3\", \"command\": \"python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --dataset conll2003 --data_dir data/conll2003 --subtask ner --n_samples 8 --temperature 1.0 --max_tokens 1024 --seed 42 --collect_logprobs --output_dir output/exp_011_ood_scierc_to_conll\", \"data_count\": 3500}, \"conclusion\": \"success\", \"checkpoint_path\": \"output/exp_011_ood_scierc_to_conll/samples.jsonl\", \"log_path\": \"output/exp_011_ood_scierc_to_conll/report.json\", \"completed_at\": \"2026-05-15T11:47:47.953Z\", \"metrics\": {\"greedy_ner_f1\": 0.522, \"rho_vc\": 0.469, \"rho_sj\": 0.378, \"rho_em\": 0.3, \"rho_fk\": 0.285, \"rho_lp\": 0.246}, \"hypothesis\": \"Out-of-domain transfer: SciERC-trained model on CoNLL data. Tests if confidence signals work under partial schema overlap (SciERC has Organization/Person which overlap with CoNLL ORG/PER). Complement to exp_011_ood_conll_to_scierc.\"}, \"exp_qwen3_4b_scierc_finetune_v4\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T19:26:25.512Z\", \"updated_at\": \"2026-05-17T02:56:24.418Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && llamafactory-cli train train_config_scierc_4b.yaml\\\"\", \"server\": \"autodl-5090\", \"gpu\": \"cuda:0\", \"pid\": \"227123\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_qwen3_4b_scierc_finetune_v4.log\", \"submitted_at\": \"2026-05-15T19:26:31.444Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/scierc/processed_data\", \"data_count\": 551, \"model_name\": \"Qwen3-4B\", \"seed\": 42, \"wall_clock_seconds\": 1668.8, \"gpu_hours\": 0.46}, \"conclusion\": \"success\", \"metrics\": {\"total_steps\": 585, \"completed_steps\": 585, \"best_checkpoint\": \"checkpoint-400\", \"best_eval_loss\": 0.0898, \"epochs\": 5}, \"checkpoint_path\": \"checkpoints/qwen3-4b-scierc-merged/\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_qwen3_4b_scierc_finetune_v4.log\", \"completed_at\": \"2026-05-15T19:54:20.255Z\", \"hypothesis\": \"Qwen3-4B SciERC LoRA fine-tune v4: training the smaller 4B model to complete the 2x2 scale matrix (4B×SciERC cell). Validates that fine-tuning convergence patterns hold across model scales.\"}, \"exp_011_ood_conll_to_scierc\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T11:36:08.325Z\", \"updated_at\": \"2026-05-17T02:56:14.242Z\", \"spec\": {\"hypothesis\": \"SCS structural signals remain effective under domain shift (CoNLL model on SciERC data, joint NER+RE)\", \"plan_id\": \"exp-011\", \"model_name\": \"qwen3-8b-conll2003-merged\", \"data_path\": \"data/scierc/processed_data\", \"seed\": 42, \"server\": \"autodl-5090\", \"gpu\": \"cuda:3\", \"pid\": 181723, \"command\": \"python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-conll2003-merged --dataset scierc --data_dir data/scierc/processed_data --subtask joint --n_samples 8 --temperature 1.0 --max_tokens 1024 --seed 42 --collect_logprobs --output_dir output/exp_011_ood_conll_to_scierc\", \"data_count\": 551}, \"conclusion\": \"negative\", \"checkpoint_path\": \"output/exp_011_ood_conll_to_scierc/samples.jsonl\", \"log_path\": \"output/exp_011_ood_conll_to_scierc/report.json\", \"completed_at\": \"2026-05-15T11:50:21.969Z\", \"metrics\": {\"greedy_ner_f1\": 0.009, \"greedy_re_f1\": 0.001, \"avg_structural_rho\": -0.05, \"verdict\": \"FAIL\", \"reason\": \"schema_incompatibility\", \"direction\": \"CoNLL_model_to_SciERC_data\", \"sample_f1_pct_zero_ner\": 98.06, \"rho_sj_ner\": -0.186, \"rho_fk_ner\": -0.069, \"note\": \"Schema incompatibility (CoNLL PER/ORG/LOC/MISC vs SciERC Task/Method/Material) causes catastrophic failure. Cannot evaluate confidence signals.\"}, \"hypothesis\": \"Out-of-domain transfer test: CoNLL-trained model on SciERC data. Tests if confidence signals retain correlation with quality under severe schema mismatch (CoNLL PER/ORG/LOC/MISC vs SciERC Task/Method/Material).\"}, \"exp_freeform_seed789_v3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T19:24:26.805Z\", \"updated_at\": \"2026-05-17T02:56:11.818Z\", \"spec\": {\"log_path\": \"~/runs/struct_self_consist_ie/exp_freeform_seed789_v3.log\", \"checkpoint_path\": \"results/exp_freeform_ablation_seed789/\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T19:30:51.048Z\", \"metrics\": {\"n_instances\": 551, \"n_samples\": 8, \"parse_rate_pct\": 100, \"elapsed_seconds\": 229.7, \"freeform_ner_selection_gap\": 0.0028, \"freeform_re_selection_gap\": 0.0219, \"freeform_lp_std\": 0.0183, \"freeform_lp_range\": 0.054908, \"freeform_tied_pct\": 59, \"re_lp_flip_positive\": true, \"variance_ratio_std\": 0.89, \"variance_ratio_range\": 0.88}, \"hypothesis\": \"Free-form SciERC seed=789 v3 (bugfix rerun): corrected version of free-form inference after fixing parsing/generation issues in v1/v2. Provides clean data point for 4-seed free-form analysis.\"}, \"exp_freeform_seed789\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T18:38:29.851Z\", \"updated_at\": \"2026-05-17T02:56:09.888Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && python run_freeform_inference.py --seed 789 --num_samples 8 --temperature 1.0 --max_tokens 1024 --output_dir results/exp_freeform_ablation_seed789\\\"\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:3\"], \"pid\": \"216722\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_freeform_seed789.log\", \"submitted_at\": \"2026-05-15T18:58:46.406Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 92.2, \"gpu_hours\": 0.03}, \"notes\": \"Rerun with fixed seed-passing code on cuda:3. Original run was killed for GPU reallocation. Parse rate 100%, 227.5s elapsed. LP compression confirmed: tied_pct=59.0% (vs constrained 59.7%), variance_ratio=0.89x.\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T19:00:18.576Z\", \"metrics\": {\"inference\": {\"n_instances\": 551, \"n_samples\": 8, \"total_samples\": 4408, \"total_parsed\": 4408, \"parse_rate_pct\": 100, \"elapsed_seconds\": 227.5}, \"freeform\": {\"selection_ner\": {\"greedy\": 0.6205, \"selected\": 0.6232, \"gap\": 0.0027}, \"selection_re\": {\"greedy\": 0.2909, \"selected\": 0.31, \"gap\": 0.0191}, \"logprob_variance\": {\"mean_std\": 0.0183, \"mean_range\": 0.054908, \"tied_pct\": 59}, \"qe_ner\": {\"n\": 529, \"SJ\": {\"rho\": 0.393995, \"auroc\": 0.734474}, \"FK\": {\"rho\": 0.312292, \"auroc\": 0.794384}, \"LP\": {\"rho\": 0.247096, \"auroc\": 0.677824}, \"EM\": {\"rho\": 0.320383, \"auroc\": 0.527033}, \"VC\": {\"rho\": 0.420625, \"auroc\": 0.768111}}, \"qe_re\": {\"n\": 397, \"SJ\": {\"rho\": 0.201746, \"auroc\": 0.574388}, \"FK\": {\"rho\": 0.2202, \"auroc\": 0.633014}, \"LP\": {\"rho\": 0.295765, \"auroc\": 0.687067}, \"EM\": {\"rho\": 0.103633, \"auroc\": 0.474737}, \"VC\": {\"rho\": 0.306868, \"auroc\": 0.642197}}}, \"constrained_ref\": {\"selection_ner\": {\"greedy\": 0.6182, \"selected\": 0.6241, \"gap\": 0.0059}, \"selection_re\": {\"greedy\": 0.2913, \"selected\": 0.2845, \"gap\": -0.0068}, \"logprob_variance\": {\"mean_std\": 0.020589, \"mean_range\": 0.062305, \"tied_pct\": 59.7}}, \"comparison\": {\"variance_ratio_std\": 0.89, \"variance_ratio_range\": 0.88, \"tied_reduction_pp\": 0.7}}, \"hypothesis\": \"Free-form SciERC seed=789: multi-seed replication of free-form ablation. Validates LP compression persistence and structural signal robustness across sampling seeds under unconstrained generation.\"}, \"exp_freeform_seed456\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T17:14:48.842Z\", \"updated_at\": \"2026-05-17T02:56:09.256Z\", \"spec\": {\"hypothesis\": \"Multi-seed free-form ablation (seed=456): verify RE LP flip and NER gap stability\", \"command\": \"python run_freeform_inference.py --seed 456 --num_samples 8 --temperature 1.0 --max_tokens 1024 --output_dir results/exp_freeform_ablation_seed456\", \"server\": \"autodl-5090\", \"data_path\": \"data/scierc/processed_data\", \"data_count\": 551, \"model_name\": \"qwen3-8b-scierc-merged-v2\", \"seed\": 456, \"gpu\": \"cuda:2\", \"tmux_session\": \"exp_freeform_seed456\", \"log_path\": \"results/exp_freeform_ablation_seed456/run_summary.json\", \"checkpoint_path\": \"results/exp_freeform_ablation_seed456\"}, \"metrics\": {\"inference\": {\"n_instances\": 551, \"n_samples\": 8, \"total_samples\": 4408, \"total_parsed\": 4407, \"parse_rate_pct\": 99.98, \"elapsed_seconds\": 232.4}, \"freeform\": {\"selection_ner\": {\"greedy\": 0.6198, \"selected\": 0.6205, \"gap\": 0.0007}, \"selection_re\": {\"greedy\": 0.2908, \"selected\": 0.3108, \"gap\": 0.02}, \"logprob_variance\": {\"mean_std\": 0.018631, \"mean_range\": 0.056792, \"tied_pct\": 58.4}, \"qe_ner\": {\"n\": 529, \"SJ\": {\"rho\": 0.378498, \"auroc\": 0.707769}, \"FK\": {\"rho\": 0.286163, \"auroc\": 0.754779}, \"LP\": {\"rho\": 0.227089, \"auroc\": 0.672081}, \"EM\": {\"rho\": 0.319997, \"auroc\": 0.47789}, \"VC\": {\"rho\": 0.416853, \"auroc\": 0.756543}}, \"qe_re\": {\"n\": 397, \"SJ\": {\"rho\": 0.211331, \"auroc\": 0.572335}, \"FK\": {\"rho\": 0.259074, \"auroc\": 0.652998}, \"LP\": {\"rho\": 0.306382, \"auroc\": 0.70134}, \"EM\": {\"rho\": 0.1043, \"auroc\": 0.461641}, \"VC\": {\"rho\": 0.301507, \"auroc\": 0.628873}}}, \"constrained_ref\": {\"selection_ner\": {\"greedy\": 0.6182, \"selected\": 0.6241, \"gap\": 0.0059}, \"selection_re\": {\"greedy\": 0.2913, \"selected\": 0.2845, \"gap\": -0.0068}, \"logprob_variance\": {\"mean_std\": 0.020589, \"mean_range\": 0.062305, \"tied_pct\": 59.7}}, \"comparison\": {\"variance_ratio_std\": 0.9, \"variance_ratio_range\": 0.91, \"tied_reduction_pp\": 1.3}}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T19:12:29.413Z\", \"hypothesis\": \"Free-form SciERC seed=456: multi-seed replication of free-form ablation. Validates LP compression persistence and structural signal robustness across sampling seeds under unconstrained generation.\"}, \"exp_freeform_seed123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T17:14:47.765Z\", \"updated_at\": \"2026-05-17T02:56:06.903Z\", \"spec\": {\"hypothesis\": \"Multi-seed free-form ablation (seed=123): verify RE LP flip and NER gap stability\", \"command\": \"python run_freeform_inference.py --seed 123 --num_samples 8 --temperature 1.0 --max_tokens 1024 --output_dir results/exp_freeform_ablation_seed123\", \"server\": \"autodl-5090\", \"data_path\": \"data/scierc/processed_data\", \"data_count\": 551, \"model_name\": \"qwen3-8b-scierc-merged-v2\", \"seed\": 123, \"gpu\": \"cuda:1\", \"tmux_session\": \"exp_freeform_seed123\", \"log_path\": \"results/exp_freeform_ablation_seed123/run_summary.json\", \"checkpoint_path\": \"results/exp_freeform_ablation_seed123\"}, \"metrics\": {\"inference\": {\"n_instances\": 551, \"n_samples\": 8, \"total_samples\": 4408, \"total_parsed\": 4406, \"parse_rate_pct\": 99.95, \"elapsed_seconds\": 228.1}, \"freeform\": {\"selection_ner\": {\"greedy\": 0.6194, \"selected\": 0.6222, \"gap\": 0.0028}, \"selection_re\": {\"greedy\": 0.2874, \"selected\": 0.305, \"gap\": 0.0176}, \"logprob_variance\": {\"mean_std\": 0.019881, \"mean_range\": 0.059864, \"tied_pct\": 57.7}, \"qe_ner\": {\"n\": 529, \"SJ\": {\"rho\": 0.384214, \"auroc\": 0.748728}, \"FK\": {\"rho\": 0.323956, \"auroc\": 0.766039}, \"logprob\": {\"rho\": 0.217297, \"auroc\": 0.701657}, \"EM\": {\"rho\": 0.326887, \"auroc\": 0.52533}, \"voting_conf\": {\"rho\": 0.407893, \"auroc\": 0.799676}}, \"qe_re\": {\"n\": 397, \"SJ\": {\"rho\": 0.272776, \"auroc\": 0.614056}, \"FK\": {\"rho\": 0.314429, \"auroc\": 0.678534}, \"logprob\": {\"rho\": 0.309673, \"auroc\": 0.70414}, \"EM\": {\"rho\": 0.137216, \"auroc\": 0.487342}, \"voting_conf\": {\"rho\": 0.316667, \"auroc\": 0.647442}}}, \"constrained_ref\": {\"selection_ner\": {\"greedy\": 0.6182, \"selected\": 0.6241, \"gap\": 0.0059}, \"selection_re\": {\"greedy\": 0.2913, \"selected\": 0.2845, \"gap\": -0.0068}}, \"comparison\": {\"variance_ratio_std\": 0.97, \"variance_ratio_range\": 0.96, \"tied_reduction_pp\": 2}}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T19:29:48.939Z\", \"hypothesis\": \"Free-form SciERC seed=123: multi-seed replication of free-form ablation. Validates LP compression persistence and structural signal robustness across sampling seeds under unconstrained generation.\"}, \"exp_009_capability_stratification\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T14:59:24.201Z\", \"updated_at\": \"2026-05-17T02:56:02.685Z\", \"spec\": {\"command\": \"python code/exp009_stratification_analysis.py\", \"server\": \"autodl-5090\", \"data_path\": \"output/exp001_n16_seed42 + output/exp008_re_n16 + output/exp002_conll2003\", \"data_count\": 4555, \"model_name\": \"analysis_only\", \"seed\": 42}, \"conclusion\": \"success\", \"checkpoint_path\": \"output/exp009_stratification_results.json\", \"log_path\": \"/tmp/exp009.log\", \"completed_at\": \"2026-05-14T14:59:46.463Z\", \"metrics\": {\"scierc_ner\": {\"n\": 551, \"sj_rho_overall\": 0.398, \"by_greedy_f1\": {\"hard_0_25_sj_rho\": 0.159, \"med_low_sj_rho\": 0.139, \"med_high_sj_rho\": 0.09, \"easy_sj_rho\": 0.23}, \"by_sent_len\": {\"Q1_sj_rho\": 0.461, \"Q2_sj_rho\": 0.401, \"Q3_sj_rho\": 0.296, \"Q4_sj_rho\": 0.382}, \"by_ent_count\": {\"0_sj_rho\": 0.689, \"1_2_sj_rho\": 0.415, \"3_5_sj_rho\": 0.353, \"6plus_sj_rho\": 0.547}}, \"scierc_re\": {\"n\": 551, \"by_greedy_f1\": {\"hard_0_25_sj_rho\": -0.043, \"easy_sj_rho\": 0.21}, \"by_sent_len\": {\"Q1_sj_rho\": 0.447, \"Q4_sj_rho\": 0.54}, \"by_rel_count\": {\"0_sj_rho\": 0.62, \"1_2_sj_rho\": 0.275, \"6plus_sj_rho\": 0.527}}, \"conll_ner\": {\"n\": 3453, \"by_sent_len\": {\"Q1_sj_rho\": 0.334, \"Q3_sj_rho\": 0.518}}, \"proxy_independence\": {\"scierc_ner_f1_vs_slen\": -0.021, \"scierc_ner_f1_vs_ecnt\": 0.007, \"scierc_re_f1_vs_slen\": -0.147}}, \"notes\": \"Registry metrics are PRE-gold-filter (n=551). Paper uses exp_009_v2_re_rerun (gold-filtered n=397): RE Q1_sj_rho=0.110, Q4_sj_rho=0.473. Registry values (Q1=0.447, Q4=0.540) are SUPERSEDED.\", \"hypothesis\": \"Capability stratification analysis: test if SJ signal effectiveness varies with instance difficulty (greedy F1 quartiles), sentence length, and entity/relation count. Identifies which instance subpopulations benefit most from structural consistency signals.\"}, \"exp_023_lora_rank8\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T10:29:59.501Z\", \"updated_at\": \"2026-05-17T02:55:50.540Z\", \"spec\": {\"hypothesis\": \"LoRA rank=8 ablation: does reducing rank from 32 to 8 significantly affect correlation-selection patterns?\", \"model_name\": \"Qwen/Qwen3-8B\", \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/data/llmfactory_train.json\", \"data_count\": 1861, \"server\": \"autodl-5090\", \"seed\": 42, \"parent\": \"ft_002_v2\", \"method\": \"LoRA r=8 alpha=16, 5 epochs, batch=2 grad_accum=8 gradient_checkpointing=true\", \"gpu\": \"cuda:2\", \"pid\": 288382, \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/logs/exp023_rank8_train.log\", \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen3-8b-scierc-lora-rank8\", \"command\": \"CUDA_VISIBLE_DEVICES=2 llamafactory-cli train train_config_rank8.yaml\", \"trainable_params\": \"21.8M\", \"total_steps\": 585, \"estimated_runtime\": \"26min\"}, \"conclusion\": \"success\", \"metrics\": {\"train_loss\": 0.1018, \"eval_loss\": 0.0776, \"train_runtime\": \"28m45s\", \"ner_full\": {\"n\": 529, \"greedy_f1\": 0.6397, \"oracle_f1\": 0.7998, \"oracle_headroom\": 0.1601, \"degeneracy_rate\": 0.072, \"SJ_rho\": 0.3649, \"FK_rho\": 0.2838, \"VC_rho\": 0.394, \"EM_rho\": 0.2562, \"LP_rho\": 0.2105, \"SJ_auroc\": 0.689, \"FK_auroc\": 0.6002, \"VC_auroc\": 0.6886, \"EM_auroc\": 0.7265, \"LP_auroc\": 0.6054, \"sel_SJ\": 0.6306, \"sel_FK\": 0.6265, \"sel_VC\": 0.5919, \"sel_EM\": 0.6073, \"sel_LP\": 0.635}, \"ner_cond\": {\"n\": 477, \"SJ_rho\": 0.3056, \"FK_rho\": 0.1452, \"VC_rho\": 0.3191, \"EM_rho\": 0.3558, \"LP_rho\": 0.169}, \"re_full\": {\"n\": 397, \"greedy_f1\": 0.3712, \"oracle_f1\": 0.609, \"oracle_headroom\": 0.2378, \"degeneracy_rate\": 0.217, \"SJ_rho\": 0.2244, \"FK_rho\": 0.3448, \"VC_rho\": 0.3617, \"EM_rho\": 0.068, \"LP_rho\": 0.2737, \"SJ_auroc\": 0.7092, \"FK_auroc\": 0.6469, \"VC_auroc\": 0.7533, \"EM_auroc\": 0.7306, \"LP_auroc\": 0.6325, \"sel_SJ\": 0.3584, \"sel_FK\": 0.3498, \"sel_VC\": 0.3715, \"sel_EM\": 0.3291, \"sel_LP\": 0.3606}, \"re_cond\": {\"n\": 242, \"SJ_rho\": 0.3601, \"FK_rho\": 0.2343, \"VC_rho\": 0.3703, \"EM_rho\": 0.4613, \"LP_rho\": 0.1809}}, \"completed_at\": \"2026-05-16T11:22:34.576Z\", \"hypothesis\": \"LoRA rank=8 ablation on SciERC: test if reduced model capacity (rank 8 vs 32) changes signal effectiveness ranking or correlation-selection gap pattern. Verifies findings are not rank-specific artifacts.\", \"parent\": \"exp_012_rerun_1024\"}, \"exp_022_seed789\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T10:08:27.375Z\", \"updated_at\": \"2026-05-17T02:55:49.870Z\", \"hypothesis\": \"3rd seed SciERC inference (seed=789) with ft_002_v2 (Qwen3-8B). N=8, T=1.0, joint NER+RE, logprobs collected. Complements seed42 (exp_012_rerun_1024) and seed123/456 for multi-seed analysis.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 PYTHONPATH=code python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc/processed_data --dataset scierc --subtask joint --n_samples 8 --temperature 1.0 --seed 789 --num_test 9999 --max_tokens 1024 --collect_logprobs --output_dir output/exp_022_seed789/\", \"server\": \"autodl-5090\", \"data_path\": \"data/scierc/processed_data\", \"data_count\": 551, \"model_name\": \"Qwen3-8B (qwen3-8b-scierc-merged-v2)\", \"seed\": 789, \"checkpoint_path\": \"checkpoints/qwen3-8b-scierc-merged-v2\", \"log_path\": \"output/exp_022_seed789/run.log\", \"gpu\": \"cuda:0\", \"pid\": 286743, \"account\": \"root\", \"backend\": \"tmux\", \"tmux_session\": \"exp_022_seed789\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T14:25:17.461Z\", \"parent\": \"exp_012_rerun_1024\"}, \"exp_025_n32\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T13:38:26.420Z\", \"updated_at\": \"2026-05-17T02:55:46.212Z\", \"spec\": {\"checkpoint_path\": \"checkpoints/qwen3-8b-scierc-merged-v2\", \"log_path\": \"output/exp_025_n32/run.log\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T14:25:39.849Z\", \"metrics\": {\"n_samples\": 32, \"degeneracy_pct\": 4, \"lp_range\": 0.0781, \"oracle_f1\": 0.8412, \"greedy_f1\": 0.6615, \"oracle_gap\": 0.1797, \"selection_f1_lp_delta\": 0.54, \"selection_f1_sj_delta\": 0.16, \"selection_f1_fk_delta\": 0.6, \"selection_f1_em_delta\": 0.68, \"selection_f1_vc_delta\": -5.21, \"best_signal\": \"EM\", \"best_delta\": 0.68, \"metric_space\": \"micro_f1_filtered_529inst\", \"note\": \"corrected via n_ablation_fixed.py, greedy from inst['greedy'] field\"}, \"hypothesis\": \"N=32 sample ablation on SciERC: test if increasing samples from 8→32 reduces degeneracy and improves selection F1, particularly for structural signals. Validates whether sample count is the bottleneck for signal effectiveness.\", \"parent\": \"exp_012_rerun_1024\"}, \"exp_021_fewnerd_full\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T16:33:44.079Z\", \"updated_at\": \"2026-05-17T02:55:45.560Z\", \"hypothesis\": \"Full Few-NERD LoRA fine-tune (rank=32, α=64, 3 epochs) on SUPERVISED coarse 8-type NER (131k train). 4-GPU DDP on autodl-5090. Post-training: N=8 inference on full test set, T=1.0, seed=42, collect logprobs for SCS metrics.\", \"spec\": {\"gpu\": \"cuda:0,cuda:1,cuda:2,cuda:3\", \"gpu_count\": 4, \"training_mode\": \"DDP\", \"checkpoint_path\": \"output/exp_021_fewnerd_full/checkpoint-6177\", \"log_path\": \"output/exp_021_inference/\"}, \"conclusion\": \"success\", \"metrics\": {\"total_steps\": 6177, \"train_loss\": 0.048, \"eval_loss\": 0.0275, \"train_runtime\": \"3h57m\", \"epochs\": 3, \"final_checkpoint\": \"output/exp_021_fewnerd_full/checkpoint-6177\", \"adapter_path\": \"output/exp_021_fewnerd_full/adapter_model.safetensors\", \"inference_instances\": 37648, \"inference_filtered\": 32565, \"inference_n_samples\": 8, \"greedy_macro_f1\": 0.7478, \"oracle_macro_f1\": 0.8719, \"headroom\": 0.124, \"zero_f1_rate\": 0.119, \"degeneracy_rate\": 0.101, \"lp_within_range_mean\": 0.0879, \"lp_within_range_median\": 0.0662, \"lp_global_rho\": 0.4215, \"lp_cond_rho\": 0.4225, \"sj_global_rho\": 0.3002, \"sj_cond_rho\": 0.2937, \"fk_global_rho\": 0.3132, \"fk_cond_rho\": 0.3093, \"em_global_rho\": 0.2871, \"em_cond_rho\": 0.271, \"vc_global_rho\": 0.3858, \"vc_cond_rho\": 0.3234, \"lp_selection_delta_pp\": 1.36, \"vc_selection_delta_pp\": -1.79, \"sj_selection_delta_pp\": -2.14, \"fk_selection_delta_pp\": -2.26, \"em_selection_delta_pp\": -3.85, \"lp_bootstrap_ci_95_pp\": [1.18, 1.53], \"lp_sample_auroc\": 0.5782, \"vc_sample_auroc\": 0.5354, \"fk_sample_auroc\": 0.521, \"sj_sample_auroc\": 0.5197, \"em_sample_auroc\": 0.5137, \"scenario\": \"A_partial\", \"note\": \"Full analysis (gold-filtered n=32565). Prior simplified analysis used unfiltered data with different metrics.\"}, \"completed_at\": \"2026-05-16T22:04:16.683Z\", \"parent\": \"exp_020_fewnerd_smoke\"}, \"exp_015_metrics_expansion\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T11:47:36.569Z\", \"updated_at\": \"2026-05-17T02:55:35.391Z\", \"spec\": {\"hypothesis\": \"Comprehensive evaluation of all 5 confidence signals with extended metrics\", \"model_name\": \"N/A (reuse pilot_004 samples)\", \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_012_logprob/samples_with_logprobs.jsonl\", \"data_count\": 551, \"server\": \"autodl-5090\", \"seed\": 42, \"parent\": \"exp_012_logprob_baseline\", \"method\": \"CPU-only analysis: 6 metrics x 5 signals x 2 subtasks (NER+RE)\", \"command\": \"python code/analyze_exp015_metrics_expansion.py\", \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/mvp_pilot_004\", \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp015_metrics_expansion\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T12:22:32.661Z\", \"metrics\": {\"data_source\": \"exp_012_logprob/samples_with_logprobs.jsonl\", \"config\": \"N=8, T=1.0, seed=42, model=qwen3-8b-scierc-merged-v2\", \"ner\": {\"n_valid\": 529, \"n_cond\": 501, \"voting_rho_full\": 0.5018, \"voting_rho_cond\": 0.4497, \"voting_auroc\": 0.7279, \"voting_tau\": 0.3766, \"sj_rho_full\": 0.3565, \"sj_rho_cond\": 0.412, \"sj_auroc\": 0.6656, \"sj_tau\": 0.2658, \"em_rho_full\": 0.2566, \"em_rho_cond\": 0.3427, \"em_auroc\": 0.623, \"em_tau\": 0.1924, \"fk_rho_full\": 0.2651, \"fk_rho_cond\": 0.306, \"fk_auroc\": 0.6243, \"fk_tau\": 0.2027, \"logprob_rho_full\": 0.1396, \"logprob_rho_cond\": 0.1627, \"logprob_auroc\": 0.5585, \"logprob_tau\": 0.1006}, \"re\": {\"n_valid\": 397, \"n_cond\": 296, \"voting_rho_full\": 0.4217, \"voting_rho_cond\": 0.463, \"voting_auroc\": 0.7162, \"voting_tau\": 0.327, \"sj_rho_full\": 0.2112, \"sj_rho_cond\": 0.3683, \"sj_auroc\": 0.5816, \"sj_tau\": 0.1619, \"em_rho_full\": 0.1002, \"em_rho_cond\": 0.3607, \"em_auroc\": 0.5036, \"em_tau\": 0.0839, \"fk_rho_full\": 0.2528, \"fk_rho_cond\": 0.3168, \"fk_auroc\": 0.6308, \"fk_tau\": 0.1967, \"logprob_rho_full\": 0.2467, \"logprob_rho_cond\": 0.1457, \"logprob_auroc\": 0.6354, \"logprob_tau\": 0.1808}, \"diagnosis\": \"Unified 5-signal evaluation on single data source. Voting leads NER full (ρ=0.502), SJ retains strength in NER cond (ρ=0.412). All structural signals beat logprob on NER. RE: voting leads both full and cond.\"}, \"notes\": \"RE logprob_rho_cond=0.1457 uses WRONG conditional filter (any sample F1>0, n=331). Correct value: 0.0112 from exp_012_rerun_1024 (greedy_f1>0, n=238). This entry's RE cond values are DEPRECATED.\", \"hypothesis\": \"Unified 5-signal evaluation (SJ/FK/EM/VC/LP) on single canonical data source (exp_012 logprobs). Establishes complete signal ranking with ρ, AUROC, and τ metrics for both NER and RE under consistent conditions.\"}, \"exp_020_fewnerd_smoke\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T10:29:25.272Z\", \"updated_at\": \"2026-05-16T16:33:59.109Z\", \"spec\": {\"checkpoint_path\": \"checkpoints/ft_fewnerd_smoke\", \"log_path\": \"checkpoints/fewnerd_train.log\"}, \"hypothesis\": \"1-epoch LoRA (r16) fine-tune Qwen3-8B on Few-NERD INTRA coarse 8-type (131k train), then N=8 T=1.0 pilot inference on 200 test instances. Re-started training 2026-05-16 18:29 CST on cuda:1, PID 288683. ETA ~22:55 CST.\", \"conclusion\": \"success\", \"metrics\": {\"final_loss\": 0.031, \"total_steps\": 8236, \"training_time\": \"5h54m\", \"pilot_greedy_f1\": 0.8037, \"pilot_instances\": 200, \"merged_model_path\": \"checkpoints/qwen3-8b-fewnerd-merged\"}, \"completed_at\": \"2026-05-16T16:33:59.109Z\"}, \"exp_vc_lp_cascade_selection\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T04:44:02.658Z\", \"updated_at\": \"2026-05-16T06:31:26.755Z\", \"hypothesis\": \"VC-filtered LP selection cascade: test if combining VC (pre-filter) + LP (rank) improves selection F1 over single-signal selection. Addresses SF3 reviewer suggestion. Pure analysis on existing data.\", \"conclusion\": \"killed\", \"spec\": {\"command\": \"N/A - cancelled before execution\", \"server\": \"N/A\", \"data_path\": \"N/A\", \"data_count\": 0, \"model_name\": \"N/A\", \"seed\": 0, \"checkpoint_path\": \"N/A\", \"log_path\": \"N/A\"}, \"completed_at\": \"2026-05-16T06:31:26.755Z\"}, \"exp_tacred_re_benchmark\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T04:43:59.002Z\", \"updated_at\": \"2026-05-16T06:31:25.273Z\", \"hypothesis\": \"TACRED RE benchmark: replicate SciERC RE experiment flow on second RE dataset. Verify correlation-selection gap generalizes beyond SciERC. D104 highest priority — addresses R11 MF1 consensus weakness.\", \"conclusion\": \"killed\", \"spec\": {\"command\": \"N/A - cancelled before execution\", \"server\": \"N/A\", \"data_path\": \"N/A\", \"data_count\": 0, \"model_name\": \"N/A\", \"seed\": 0, \"checkpoint_path\": \"N/A\", \"log_path\": \"N/A\"}, \"completed_at\": \"2026-05-16T06:31:25.273Z\"}, \"exp_vc_quartile_analysis\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T04:48:35.263Z\", \"updated_at\": \"2026-05-16T05:00:36.736Z\", \"hypothesis\": \"VC quartile stratification: split instances by VC score into Q1-Q4, compute LP selection F1 per quartile. Test if LP selection ability recovers in high-VC instances. Addresses SF3.\", \"spec\": {\"command\": \"python vc_quartile_analysis.py\", \"server\": \"autodl-5090\", \"data_path\": \"output/exp_012_rerun_1024/samples.jsonl + output/exp_002_conll_n8_seed42/samples.jsonl\", \"data_count\": 3682, \"model_name\": \"analysis_only (Qwen3-8B data)\", \"seed\": 42}, \"conclusion\": \"success\", \"checkpoint_path\": \"artifacts/vc_quartile_analysis/results.json\", \"log_path\": \"artifacts/vc_quartile_analysis/report.md\", \"completed_at\": \"2026-05-16T05:00:30.439Z\", \"metrics\": {\"scierc_ner\": {\"Q1_lp_delta\": 0.016, \"Q2_lp_delta\": -0.006, \"Q3_lp_delta\": 0.02, \"Q4_lp_delta\": -0.004, \"Q4_mean_vc\": 0.921, \"Q1_headroom\": 0.169, \"Q4_headroom\": 0.048, \"overall_lp_delta\": 0.006, \"n\": 529}, \"scierc_re\": {\"Q1_lp_delta\": -0.036, \"Q2_lp_delta\": -0.021, \"Q3_lp_delta\": -0.022, \"Q4_lp_delta\": 0.04, \"Q4_mean_vc\": 0.894, \"Q1_headroom\": 0.211, \"Q4_headroom\": 0.145, \"overall_lp_delta\": -0.009, \"n\": 397}, \"conll_ner\": {\"Q1_lp_delta\": -0.037, \"Q2_lp_delta\": -0.005, \"Q3_lp_delta\": 0, \"Q4_lp_delta\": 0, \"overall_lp_delta\": -0.01, \"n\": 2756, \"note\": \"Q3/Q4 degenerate (VC=1.0, all samples identical)\"}, \"conclusion\": \"VC stratification does not solve LP compression for NER. RE Q4 is only exception (+0.040).\"}}, \"exp_llama3b_scierc_ablation\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T02:45:23.638Z\", \"updated_at\": \"2026-05-16T03:59:26.005Z\", \"hypothesis\": \"Cross-family scale ablation: LLaMA 3.2-3B on SciERC NER. Verify correlation-selection gap generalizes across model families AND scales. Compare with LLaMA 8B results.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 PYTHONPATH=code python code/run_mvp_pilot.py --model_path checkpoints/llama3.2-3b-scierc-merged --data_dir data/scierc/processed_data --dataset scierc --subtask ner --n_samples 8 --temperature 1.0 --seed 42 --num_test 9999 --max_tokens 1024 --collect_logprobs --output_dir output/review_round9_experiments/llama3b_scierc/\", \"server\": \"autodl-5090\", \"data_path\": \"data/scierc/processed_data\", \"data_count\": 551, \"model_name\": \"LLaMA-3.2-3B-Instruct (LoRA r=32 SciERC fine-tuned)\", \"seed\": 42, \"checkpoint_path\": \"checkpoints/llama3.2-3b-scierc-merged\", \"log_path\": \"output/review_round9_experiments/llama3b_scierc/inference.log\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T03:59:16.198Z\", \"metrics\": {\"ner_full\": {\"SJ_rho\": 0.3754, \"FK_rho\": 0.2676, \"LP_rho\": 0.2662, \"EM_rho\": 0.3341, \"VC_rho\": 0.4602, \"SJ_auroc\": 0.7383, \"FK_auroc\": 0.6714, \"LP_auroc\": 0.633, \"EM_auroc\": 0.7763, \"VC_auroc\": 0.7429, \"n\": 529}, \"ner_cond\": {\"SJ_rho\": 0.3445, \"FK_rho\": 0.2125, \"LP_rho\": 0.2099, \"EM_rho\": 0.3952, \"VC_rho\": 0.3815, \"SJ_auroc\": 0.7292, \"FK_auroc\": 0.66, \"LP_auroc\": 0.6156, \"EM_auroc\": 0.7822, \"VC_auroc\": 0.7222, \"n\": 476}, \"greedy_f1\": 0.6267, \"oracle_f1\": 0.763, \"oracle_headroom\": 0.1363, \"selection_f1_SJ\": 0.6328, \"selection_f1_VC\": 0.6113, \"selection_f1_FK\": 0.6295, \"selection_f1_EM\": 0.6174, \"selection_f1_LP\": 0.6279, \"n_gold_empty\": 22, \"structural_beats_surface\": true, \"rho_advantage_SJ_over_FK\": 0.1078}}, \"exp_freeform_conll_4seed\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T02:45:17.133Z\", \"updated_at\": \"2026-05-16T03:04:49.550Z\", \"hypothesis\": \"Free-form CoNLL NER 4-seed ablation: verify LP compression is cross-dataset intrinsic (not SciERC-specific). 4 seeds × N=8, T=1.0 on CoNLL, compare LP range distribution with constrained decoding.\", \"spec\": {\"command\": \"python run_freeform_conll.py --seed {42,123,456,789} --gpu {0,1,2,3} --n_samples 8 --temperature 1.0\", \"server\": \"autodl-4x5090\", \"data_path\": \"data/conll2003/test.jsonl\", \"data_count\": 3453, \"model_name\": \"checkpoints/qwen3-8b-conll2003-merged\", \"seed\": \"42,123,456,789\"}, \"checkpoint_path\": \"N/A (inference-only experiment)\", \"log_path\": \"output/review_round9_experiments/freeform_conll/\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T03:04:40.278Z\", \"metrics\": {\"greedy_f1\": \"0.9035±0.0004\", \"oracle_f1\": \"0.9460±0.0023\", \"lp_range_median\": \"0.0581±0.0072\", \"rho_sj\": \"0.4606±0.0188\", \"rho_fk\": \"0.4372±0.0209\", \"rho_em\": \"0.4714±0.0168\", \"rho_vc\": \"0.4606±0.0138\", \"rho_lp\": \"0.3262±0.0120\", \"sel_f1_sj\": \"0.8994±0.0014\", \"sel_f1_vc\": \"0.9006±0.0026\", \"sel_f1_lp\": \"0.8958±0.0009\", \"seeds\": [42, 123, 456, 789], \"n_samples\": 8, \"temperature\": 1, \"instances\": 2756, \"gold_empty_filtered\": 697}}, \"exp_qwen3_4b_conll_merge_inference_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T19:42:42.107Z\", \"updated_at\": \"2026-05-15T20:07:12.593Z\", \"hypothesis\": \"CoNLL 4B checkpoint-4200 (best from resume training) merge + SCS inference. Replaces v1 which used checkpoint-3800 merged model. Cross-scale evidence for correlation-selection gap.\", \"spec\": {\"command\": \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && CUDA_VISIBLE_DEVICES=1 PYTHONPATH=code python code/run_mvp_pilot.py --model_path checkpoints/qwen3-4b-conll2003-merged-ckpt4200 --data_dir data/conll2003 --dataset conll2003 --subtask ner --n_samples 8 --temperature 1.0 --seed 42 --num_test 9999 --max_tokens 1024 --collect_logprobs --output_dir output/exp_qwen3_4b_conll_merge_inference_v2\", \"server\": \"autodl-5090\", \"data_path\": \"data/conll2003\", \"data_count\": 3453, \"model_name\": \"Qwen3-4B (LoRA merged, ckpt-4200)\", \"seed\": 42, \"checkpoint_source\": \"exp_qwen3_4b_conll_finetune_resume (checkpoint-4200)\"}, \"checkpoint_path\": \"N/A - duplicate\", \"log_path\": \"N/A - duplicate\", \"conclusion\": \"killed\", \"notes\": \"Superseded by exp_qwen3_4b_conll_scs_inference_v2. Output was empty (dead experiment), functionally duplicate.\", \"completed_at\": \"2026-05-15T20:03:47.431Z\"}, \"exp_qwen3_4b_scierc_merge_inference\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T19:42:43.332Z\", \"updated_at\": \"2026-05-15T20:04:15.433Z\", \"hypothesis\": \"SciERC 4B best checkpoint merge + SCS inference. Complete 2x2 scale matrix (4B SciERC cell). Cross-scale + cross-task evidence for correlation-selection gap.\", \"checkpoint_path\": \"N/A - superseded\", \"log_path\": \"N/A - superseded\", \"conclusion\": \"killed\", \"notes\": \"Superseded by exp_qwen3_4b_scierc_scs_inference. Never launched (stuck in PREPARING). Killed during registry cleanup.\", \"completed_at\": \"2026-05-15T20:04:15.433Z\"}, \"exp_qwen3_4b_scierc_finetune_v3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T19:24:45.518Z\", \"updated_at\": \"2026-05-15T19:39:04.438Z\", \"spec\": {\"command\": \"llamafactory-cli train train_config_scierc_4b.yaml\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:2\"], \"pid\": \"226610\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_qwen3_4b_scierc_finetune_v3.log\", \"submitted_at\": \"2026-05-15T19:24:55.461Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/scierc/processed_data\", \"data_count\": 551, \"model_name\": \"Qwen3-4B\", \"seed\": 42, \"wall_clock_seconds\": 849.0, \"gpu_hours\": 0.24}, \"conclusion\": \"failed\", \"notes\": \"OOM on cuda:2 — freeform inference (seed789, 8B) 占满 GPU 2。未实际训练。重启为 v4 on cuda:0。\", \"completed_at\": \"2026-05-15T19:39:04.438Z\"}, \"exp_qwen3_4b_conll_finetune_resume\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T19:38:19.388Z\", \"updated_at\": \"2026-05-15T19:38:43.468Z\", \"hypothesis\": \"CoNLL 4B NER LoRA fine-tune resume from checkpoint-3800. Cross-scale evidence for correlation-selection gap.\", \"spec\": {\"hypothesis\": \"CoNLL2003 NER LoRA fine-tune with Qwen3-4B, resume from checkpoint-3800 to complete 5 epochs\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && llamafactory-cli train train_config_conll2003_4b_resume.yaml\\\"\", \"server\": \"autodl-5090\", \"gpu\": \"cuda:1\", \"data_path\": \"data/conll2003/llmfactory_train.json\", \"data_count\": 14042, \"model_name\": \"Qwen3-4B\", \"seed\": 42, \"resume_from\": \"checkpoint-3800\", \"lora_rank\": 32, \"lora_alpha\": 64, \"num_train_epochs\": 5, \"learning_rate\": 0.0002, \"batch_size\": \"2 x 8 grad_accum\", \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen3-4b-conll2003-lora\", \"best_checkpoint\": \"checkpoint-4200\", \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen3-4b-conll2003-lora/trainer_state.json\"}, \"conclusion\": \"success\", \"metrics\": {\"train_loss\": 0.001136, \"eval_loss\": 0.0225, \"best_global_step\": 4200, \"best_metric_eval_loss\": 0.0225, \"total_steps\": 4390, \"epochs\": 5, \"train_runtime_sec\": 1185.8, \"train_samples_per_second\": 59.2, \"resumed_from_step\": 3800}, \"completed_at\": \"2026-05-15T19:38:43.468Z\"}, \"exp_qwen3_4b_scierc_finetune_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T19:03:49.204Z\", \"updated_at\": \"2026-05-15T19:24:32.466Z\", \"spec\": {\"command\": \"llamafactory-cli train train_config_scierc_4b.yaml\", \"server\": \"autodl-5090\", \"gpu\": \"cuda:3\", \"pid\": \"219830\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_qwen3_4b_scierc_finetune_v2.log\", \"submitted_at\": \"2026-05-15T19:05:31.524Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/scierc/processed_data\", \"data_count\": 1861, \"model_name\": \"Qwen3-4B\", \"seed\": 42, \"plan_id\": \"D096\", \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen3-4b-scierc-lora/\", \"wall_clock_seconds\": 1122.6, \"gpu_hours\": 0.31}, \"conclusion\": \"failed\", \"completed_at\": \"2026-05-15T19:24:14.124Z\", \"notes\": \"PID 219830 已死，仅完成 step 10，无 checkpoint。需彻底重启。\"}, \"exp_qwen3_4b_conll_finetune\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-15T17:18:35.501Z\", \"updated_at\": \"2026-05-15T19:10:24.822Z\", \"hypothesis\": \"Scale ablation: Qwen3-4B CoNLL NER LoRA fine-tune to provide cross-scale evidence (vs 8B). Verify correlation-selection gap, SJ>FK ordering, and LP compression generalize across model scale.\", \"reproduce\": {\"finished_at\": \"2026-05-15T18:45:42.215Z\"}, \"failure_reason\": \"\", \"completed_at\": \"2026-05-15T18:45:43.672Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-15T18:45:49.686191+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\"}}, \"spec\": {\"command\": \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && CUDA_VISIBLE_DEVICES=0 llamafactory-cli train train_config_conll2003_4b.yaml\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:0\"], \"data_path\": \"data/conll2003\", \"data_count\": 14041, \"model_name\": \"Qwen3-4B\", \"seed\": 42, \"plan_id\": \"D096\", \"log_path\": \"checkpoints/qwen3-4b-conll2003-lora/trainer_log.jsonl\", \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen3-4b-conll2003-lora\", \"lora_config\": {\"trainable_params\": \"66M / 4.09B (1.62%)\", \"target_modules\": \"q_proj, k_proj, v_proj, o_proj, gate_proj, up_proj, down_proj\", \"epochs\": 5, \"batch_size\": 16, \"total_steps\": 4390, \"enable_thinking\": false}}, \"conclusion\": \"success\", \"notes\": \"Training stopped at step 3920/4390 (89.3%, epoch 4.46/5). No error log or tmux session found. checkpoint-3800 is valid (adapter_model.safetensors 264MB, eval_loss=0.023). Proceeding with checkpoint-3800 for merge+inference.\", \"metrics\": {\"final_loss\": 0.0086, \"total_steps_completed\": 3920, \"total_steps_target\": 4390, \"epochs_completed\": 4.46, \"epochs_target\": 5, \"best_checkpoint\": \"checkpoint-3800\", \"note\": \"Training stopped at 89.3% completion (no error log found). Using checkpoint-3800 (loss ~0.01) for merge.\"}}, \"exp_freeform_seed789_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T19:02:03.813Z\", \"updated_at\": \"2026-05-15T19:06:44.537Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && python run_freeform_inference.py --seed 789 --num_samples 8 --temperature 1.0 --max_tokens 1024 --output_dir results/exp_freeform_ablation_seed789\\\"\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:2\"], \"pid\": \"218882\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_freeform_seed789_v2.log\", \"submitted_at\": \"2026-05-15T19:02:03.527Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"hypothesis\": \"Multi-seed free-form ablation (seed=789): third seed for 3-seed mean±σ statistical significance. Verify RE LP flip and NER gap stability.\", \"data_path\": \"data/scierc/processed_data\", \"data_count\": 551, \"model_name\": \"qwen3-8b-scierc-merged-v2\", \"seed\": 789, \"wall_clock_seconds\": 274.9, \"gpu_hours\": 0.08}, \"reproduce\": {\"finished_at\": \"2026-05-15T19:06:37.887Z\"}, \"failure_reason\": \"EXIT_CODE=143 (SIGTERM — graceful kill)\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-15T19:06:38.388Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-15T19:06:53.109123+00:00\"}]}}, \"exp_qwen3_4b_scierc_finetune\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T18:58:58.948Z\", \"updated_at\": \"2026-05-15T19:03:05.505Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && CUDA_VISIBLE_DEVICES=0 llamafactory-cli train train_config_scierc_4b.yaml\\\"\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:3\"], \"pid\": \"218258\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_qwen3_4b_scierc_finetune.log\", \"submitted_at\": \"2026-05-15T19:00:10.234Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 175.3, \"gpu_hours\": 0.05}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-15T19:03:05.505Z\"}, \"exp_lp_t07_scierc\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T15:34:12.094Z\", \"updated_at\": \"2026-05-15T16:30:35.531Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && PYTHONPATH=code python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc/processed_data --dataset scierc --subtask ner --n_samples 8 --temperature 0.7 --seed 42 --num_test 9999 --max_tokens 1024 --collect_logprobs --output_dir output/exp_lp_t07_scierc\\\"\", \"server\": \"autodl-5090\", \"data_path\": \"data/scierc/processed_data\", \"data_count\": 551, \"model_name\": \"Qwen3-8B (LoRA fine-tuned on SciERC, ft_002_v2 merged)\", \"seed\": 42, \"gpu\": \"cuda:1\", \"hyperparams\": {\"n_samples\": 8, \"temperature\": 0.7, \"max_tokens\": 1024}}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-15T16:28:29.563Z\"}, \"exp_lp_scierc_t07\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T15:34:06.918Z\", \"updated_at\": \"2026-05-15T16:03:13.881Z\", \"hypothesis\": \"LP T=0.7 推理：验证低温下 LP score compression 是否依然存在，强化 \\\"LP compression is model/task intrinsic\\\" claim。对比 T=1.0 的 LP range 分布。\", \"spec\": {\"command\": \"python run_sc_ie.py --dataset scierc --subtask ner --model qwen --n_samples 8 --temperature 0.7 --use_logprob --output_dir /root/autodl-tmp/struct_self_consist_ie/output/exp_lp_scierc_t07\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:1\"], \"pid\": \"196993\", \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_lp_scierc_t07/\", \"submitted_at\": \"2026-05-15T15:35:31.692Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"SciERC\", \"data_count\": 500, \"model_name\": \"Qwen3-8B\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_lp_scierc_t07/report.json\", \"wall_clock_seconds\": 1206.2, \"gpu_hours\": 0.34}, \"conclusion\": \"success\", \"metrics\": {\"ner_greedy_f1\": 0.662, \"ner_oracle_f1\": 0.764, \"ner_headroom_pp\": 10.2, \"ner_rho_sj_full\": 0.365, \"ner_rho_sj_cond\": 0.363, \"ner_rho_fk_full\": 0.289, \"ner_rho_fk_cond\": 0.255, \"lp_rho_full\": 0.249, \"lp_rho_cond\": 0.185, \"ner_rho_advantage\": 0.076, \"zero_f1_pct\": 11, \"full_n\": 529, \"cond_n\": 477, \"verdict\": \"success_supports_LP_compression_claim\"}, \"completed_at\": \"2026-05-15T15:55:37.889Z\"}, \"exp_re_scierc_seed456\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T15:40:40.607Z\", \"updated_at\": \"2026-05-15T15:55:41.890Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && CUDA_VISIBLE_DEVICES=3 PYTHONPATH=code python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc/processed_data --dataset scierc --subtask joint --n_samples 8 --temperature 1.0 --max_tokens 1024 --seed 456 --num_test 9999 --collect_logprobs --output_dir output/exp_re_scierc_seed456\\\"\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:3\"], \"pid\": \"199161\", \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_re_scierc_seed456/\", \"submitted_at\": \"2026-05-15T15:40:59.585Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"SciERC\", \"data_count\": 500, \"model_name\": \"Qwen3-8B (SciERC merged)\", \"seed\": 456, \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_re_scierc_seed456/report.json\", \"wall_clock_seconds\": 882.3, \"gpu_hours\": 0.25}, \"hypothesis\": \"SciERC RE 多种子验证 (seed456): 解决 R4-W1/R7-C1 single-seed RE 弱点。与 seed42 (exp_012_rerun_1024) 对齐，joint subtask N=8 T=1.0。目标: 3-seed RE selection F1 mean±σ。\", \"conclusion\": \"negative\", \"metrics\": {\"ner_greedy_f1\": 0.664, \"ner_oracle_f1\": 0.775, \"ner_headroom_pp\": 11.1, \"ner_rho_sj_cond\": 0.283, \"ner_rho_fk_cond\": 0.145, \"re_greedy_f1\": 0.417, \"re_oracle_f1\": 0.581, \"re_headroom_pp\": 16.3, \"re_rho_sj_cond\": 0.315, \"re_rho_fk_cond\": 0.123, \"re_zero_f1_pct\": 45.3, \"verdict\": \"FAIL_re_rho_sj_below_040\"}, \"completed_at\": \"2026-05-15T15:55:41.890Z\"}, \"exp_re_scierc_seed123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T15:40:38.271Z\", \"updated_at\": \"2026-05-15T15:55:40.000Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && CUDA_VISIBLE_DEVICES=2 PYTHONPATH=code python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc/processed_data --dataset scierc --subtask joint --n_samples 8 --temperature 1.0 --max_tokens 1024 --seed 123 --num_test 9999 --collect_logprobs --output_dir output/exp_re_scierc_seed123\\\"\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:2\"], \"pid\": \"199021\", \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_re_scierc_seed123/\", \"submitted_at\": \"2026-05-15T15:40:58.073Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"SciERC\", \"data_count\": 500, \"model_name\": \"Qwen3-8B (SciERC merged)\", \"seed\": 123, \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_re_scierc_seed123/report.json\", \"wall_clock_seconds\": 881.9, \"gpu_hours\": 0.24}, \"hypothesis\": \"SciERC RE 多种子验证 (seed123): 解决 R4-W1/R7-C1 single-seed RE 弱点。与 seed42 (exp_012_rerun_1024) 对齐，joint subtask N=8 T=1.0。目标: 3-seed RE selection F1 mean±σ。\", \"conclusion\": \"negative\", \"metrics\": {\"ner_greedy_f1\": 0.663, \"ner_oracle_f1\": 0.786, \"ner_headroom_pp\": 12.3, \"ner_rho_sj_cond\": 0.404, \"ner_rho_fk_cond\": 0.182, \"re_greedy_f1\": 0.42, \"re_oracle_f1\": 0.593, \"re_headroom_pp\": 17.3, \"re_rho_sj_cond\": 0.277, \"re_rho_fk_cond\": 0.063, \"re_zero_f1_pct\": 43.6, \"verdict\": \"FAIL_re_rho_sj_below_040\"}, \"completed_at\": \"2026-05-15T15:55:40.000Z\"}, \"exp_017_llama_conll_n8_t07\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T15:29:34.595Z\", \"updated_at\": \"2026-05-15T15:46:22.722Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && CUDA_VISIBLE_DEVICES=0 PYTHONPATH=code python code/run_mvp_pilot.py --model_path checkpoints/llama3.1-8b-conll2003-merged --data_dir data/conll2003 --dataset conll2003 --subtask ner --n_samples 8 --temperature 0.7 --seed 42 --num_test 9999 --max_tokens 1024 --collect_logprobs --output_dir output/exp_017_llama_conll_n8_t07\\\"\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:0\"], \"pid\": \"195927\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_017_llama_conll_n8_t07.log\", \"submitted_at\": \"2026-05-15T15:31:17.989Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 881.3, \"gpu_hours\": 0.24}, \"hypothesis\": \"LLaMA CoNLL N=8 T=0.7 防御性实验：填补\\\"LLaMA 仅在 SciERC 上测过\\\"的弱点，验证 cross-model consistency（vs Qwen CoNLL）。T=0.7 低温下 confidence signals 的 correlation-selection gap 是否依然存在。\", \"parent\": \"exp_017_llama_conll\", \"server\": \"autodl-5090\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"reproduce\": {\"server\": \"autodl-5090\", \"gpu\": \"cuda:0\", \"started_at\": \"2026-05-15T15:31:15.772Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && CUDA_VISIBLE_DEVICES=0 PYTHONPATH=code python code/run_mvp_pilot.py --model_path checkpoints/llama3.1-8b-conll2003-merged --data_dir data/conll2003 --dataset conll2003 --subtask ner --n_samples 8 --temperature 0.7 --seed 42 --num_test 9999 --max_tokens 1024 --collect_logprobs --output_dir output/exp_017_llama_conll_n8_t07\\\"\", \"finished_at\": \"2026-05-15T15:40:02.605Z\", \"training_hours\": 0.15}, \"pid\": \"195927\", \"log_path\": \"/root/runs/struct_self_consist_ie/exp_017_llama_conll_n8_t07.log\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T15:40:08.277684+00:00\"}]}, \"metrics\": {\"n_valid\": 2756, \"greedy_f1\": 0.9242, \"oracle_f1\": 0.9391, \"lp_range_median\": 1.1e-05, \"lp_tied_fraction_005\": 0.9579, \"signals\": {\"SJ\": {\"rho\": 0.3934, \"auroc\": 0.6506}, \"FK\": {\"rho\": 0.3879, \"auroc\": 0.6488}, \"VC\": {\"rho\": 0.375, \"auroc\": 0.6551}, \"EM\": {\"rho\": 0.3888, \"auroc\": 0.6494}, \"LP\": {\"rho\": 0.2951, \"auroc\": 0.7509}}, \"selection_f1\": {\"SJ\": 0.9247, \"FK\": 0.9254, \"VC\": 0.9264, \"EM\": 0.9255, \"LP\": 0.9248}}, \"conclusion\": \"success\", \"checkpoint_path\": \"N/A (inference-only)\", \"completed_at\": \"2026-05-15T15:45:59.311Z\"}, \"exp008_re_n16\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T12:09:50.987Z\", \"updated_at\": \"2026-05-15T12:41:39.774Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && mkdir -p output/exp008_re_n16 && CUDA_VISIBLE_DEVICES=2 PYTHONPATH=code python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc/processed_data --dataset scierc --subtask joint --n_samples 16 --temperature 1.0 --seed 42 --output_dir output/exp008_re_n16 --collect_logprobs 2>&1 | tee output/exp008_re_n16/run.log\\\"\", \"server\": \"gpu-5090-4x-2\", \"gpu\": [\"cuda:2\"], \"pid\": \"53600\", \"log_path\": \"~/runs/struct_self_consist_ie/exp008_re_n16.log\", \"submitted_at\": \"2026-05-14T12:15:14.917Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"failure_reason\": \"Superseded by exp_008_re_n16_v2 (full 551-instance run on autodl-5090)\", \"wall_clock_seconds\": 87984.9, \"gpu_hours\": 24.44}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-15T12:41:39.774Z\"}, \"exp001_seed456\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T12:09:48.078Z\", \"updated_at\": \"2026-05-15T12:41:32.192Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && mkdir -p output/exp001_n16_seed456 && CUDA_VISIBLE_DEVICES=1 PYTHONPATH=code python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc/processed_data --dataset scierc --subtask joint --n_samples 16 --temperature 1.0 --seed 456 --output_dir output/exp001_n16_seed456 --collect_logprobs 2>&1 | tee output/exp001_n16_seed456/run.log\\\"\", \"server\": \"gpu-5090-4x-2\", \"gpu\": [\"cuda:1\"], \"pid\": \"50302\", \"log_path\": \"~/runs/struct_self_consist_ie/exp001_seed456.log\", \"submitted_at\": \"2026-05-14T12:12:41.206Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"failure_reason\": \"Superseded by exp_001_seed456_v2_ner (NER-only on autodl-5090)\", \"wall_clock_seconds\": 88131.0, \"gpu_hours\": 24.48}, \"conclusion\": \"killed\", \"failure_reason\": \"superseded by v2\", \"completed_at\": \"2026-05-15T12:41:32.192Z\"}, \"exp001_seed123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T12:09:45.739Z\", \"updated_at\": \"2026-05-15T12:41:31.168Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && mkdir -p output/exp001_n16_seed123 && CUDA_VISIBLE_DEVICES=0 PYTHONPATH=code python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc/processed_data --dataset scierc --subtask joint --n_samples 16 --temperature 1.0 --seed 123 --output_dir output/exp001_n16_seed123 --collect_logprobs 2>&1 | tee output/exp001_n16_seed123/run.log\\\"\", \"server\": \"gpu-5090-4x-2\", \"gpu\": [\"cuda:0\"], \"pid\": \"48530\", \"log_path\": \"~/runs/struct_self_consist_ie/exp001_seed123.log\", \"submitted_at\": \"2026-05-14T12:09:45.674Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"failure_reason\": \"Superseded by exp_001_seed123_v2 (NER-only, 551 instances on autodl-5090)\", \"wall_clock_seconds\": 88305.5, \"gpu_hours\": 24.53}, \"conclusion\": \"killed\", \"failure_reason\": \"superseded by v2\", \"completed_at\": \"2026-05-15T12:41:31.168Z\"}, \"exp_001_n16_seed456_full\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T12:44:31.348Z\", \"updated_at\": \"2026-05-15T12:41:30.065Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && CUDA_VISIBLE_DEVICES=1 python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc/processed_data --dataset scierc --subtask joint --n_samples 16 --temperature 1.0 --seed 456 --collect_logprobs --num_test 9999 --output_dir output/exp001_n16_seed456/\\\"\", \"server\": \"gpu-5090-4x-2\", \"gpu\": [\"cuda:1\"], \"pid\": \"62170\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_001_n16_seed456_full.log\", \"submitted_at\": \"2026-05-14T12:44:31.087Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"failure_reason\": \"Superseded by exp_001_seed456_v2_ner (NER-only on autodl-5090)\", \"wall_clock_seconds\": 86219.0, \"gpu_hours\": 23.95}, \"conclusion\": \"killed\", \"failure_reason\": \"superseded by v2\", \"completed_at\": \"2026-05-15T12:41:30.065Z\"}, \"exp_001_n16_seed123_full\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T12:43:47.915Z\", \"updated_at\": \"2026-05-15T12:41:29.068Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && CUDA_VISIBLE_DEVICES=0 python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc/processed_data --dataset scierc --subtask joint --n_samples 16 --temperature 1.0 --seed 123 --collect_logprobs --num_test 9999 --output_dir output/exp001_n16_seed123_full/\\\"\", \"server\": \"gpu-5090-4x-2\", \"gpu\": [\"cuda:0\"], \"pid\": \"61812\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_001_n16_seed123_full.log\", \"submitted_at\": \"2026-05-14T12:44:06.059Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"failure_reason\": \"Superseded by exp_001_seed123_v2 (NER-only on autodl-5090)\", \"wall_clock_seconds\": 86243.0, \"gpu_hours\": 23.96}, \"conclusion\": \"killed\", \"failure_reason\": \"superseded by v2\", \"completed_at\": \"2026-05-15T12:41:29.068Z\"}, \"exp_007_ner_llama\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T11:42:21.510Z\", \"updated_at\": \"2026-05-15T12:41:27.410Z\", \"spec\": {\"description\": \"Fine-tune LLaMA-3.1-8B on SciERC + NER pilot (N=8, T=0.7). Model-agnostic validation.\", \"hypothesis\": \"SJ advantage is model-agnostic, not Qwen3-specific\", \"plan_id\": \"exp-007\", \"claim\": 1, \"model_name\": \"llama-3.1-8b-instruct (new fine-tune)\", \"dataset\": \"SciERC\", \"priority\": \"P0\", \"failure_reason\": \"Superseded by exp_007_ner_multi_model + exp_007_llama_inference (completed on autodl-5090)\"}, \"conclusion\": \"killed\", \"failure_reason\": \"superseded by exp_007_llama_inference (DONE)\", \"notes\": \"Completed as exp_007_llama_n16 on autodl-5090. Registry status corrected.\", \"completed_at\": \"2026-05-15T12:41:27.410Z\"}, \"exp_002_merge_conll2003\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T12:25:56.211Z\", \"updated_at\": \"2026-05-15T12:41:26.419Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && CUDA_VISIBLE_DEVICES=0 llamafactory-cli export export_config_conll2003.yaml > /tmp/merge_conll2003.log 2>&1 && echo 'MERGE_DONE' >> /tmp/merge_conll2003.log\\\"\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:0\"], \"pid\": \"57524\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_002_merge_conll2003.log\", \"submitted_at\": \"2026-05-14T12:25:56.139Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"failure_reason\": \"Superseded by exp_002_ner_conll2003 (completed on autodl-5090)\", \"wall_clock_seconds\": 87330.3, \"gpu_hours\": 24.26}, \"conclusion\": \"killed\", \"failure_reason\": \"superseded by exp_002_ner_conll2003 (DONE)\", \"notes\": \"Completed as exp_002_conll_n16 on autodl-5090. Registry status corrected.\", \"completed_at\": \"2026-05-15T12:41:26.419Z\"}, \"exp_019_supervised_verifier\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T10:08:54.395Z\", \"updated_at\": \"2026-05-15T12:40:53.995Z\", \"spec\": {\"hypothesis\": \"Supervised verifier (DeBERTa-v3-large) can close the correlation-selection gap, proving the gap is closable with supervision\", \"plan_id\": \"exp-019\", \"model_name\": \"microsoft/deberta-v3-large\", \"data_path\": \"output/exp_012_rerun_1024/samples.jsonl\", \"data_count\": 551, \"seed\": 42}, \"conclusion\": \"killed\", \"notes\": \"Cancelled by Director: DDL risk too high (3-4 days for implementation+training+eval+paper), scope creep for analytical paper, free-form ablation already provides sufficient mechanistic evidence\", \"completed_at\": \"2026-05-15T12:40:53.995Z\"}, \"exp_018_llama_scierc_seed456\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T06:07:15.150Z\", \"updated_at\": \"2026-05-15T06:22:40.868Z\", \"spec\": {\"hypothesis\": \"Multi-seed robustness: LLaMA SciERC N=8 seed=456, max_tokens=1024. Fresh inference (D066 decision: replace exp_007 re-analysis with independent replication).\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && PYTHONPATH=code python code/run_mvp_pilot.py --model_path checkpoints/llama3.1-8b-scierc-merged --data_dir data/scierc/processed_data --dataset scierc --subtask joint --n_samples 8 --temperature 1.0 --seed 456 --max_tokens 1024 --num_test 9999 --collect_logprobs --output_dir output/exp_018_llama_scierc_seed456_r1024\\\"\", \"server\": \"autodl-5090\", \"seed\": 456, \"model_name\": \"LLaMA-3.1-8B-SciERC-merged\", \"model_path\": \"checkpoints/llama3.1-8b-scierc-merged\", \"dataset\": \"SciERC\", \"subtask\": \"joint\", \"data_path\": \"data/scierc/processed_data\", \"data_count\": 551, \"N\": 8, \"T\": 1, \"max_tokens\": 1024, \"is_new_inference\": true, \"checkpoint_path\": \"output/exp_018_llama_scierc_seed456_r1024/\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_018_llama_scierc_seed456_r1024.log\"}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-15T06:08:05.756Z\", \"notes\": \"SUPERSEDED by exp_018_llama_scierc_seed456_r1024 (D066). Original data was re-analysis of exp_007_llama_seed456, not independent inference. Fresh rerun with explicit max_tokens=1024 now canonical.\"}, \"exp_002_conll_n16_r1024\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T22:16:57.682Z\", \"updated_at\": \"2026-05-15T01:20:53.108Z\", \"spec\": {\"hypothesis\": \"D054 rerun: max_tokens=1024. Verify truncation impact on Qwen CoNLL N=16.\", \"parent\": \"exp_002_conll_n16\", \"model_name\": \"qwen3-8b-conll2003-merged\", \"dataset\": \"CoNLL-2003\", \"seed\": 42, \"server\": \"autodl-5090\", \"command\": \"CUDA_VISIBLE_DEVICES=2 python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-conll2003-merged --data_dir data/conll2003 --dataset conll2003 --subtask ner --n_samples 16 --temperature 1.0 --seed 42 --num_test 9999 --max_tokens 1024 --collect_logprobs --output_dir output/exp_002_conll_n16_r1024\", \"data_path\": \"data/conll2003\", \"data_count\": 3453}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-15T01:20:53.108Z\"}, \"exp_007_llama_n16_r1024\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T22:16:59.685Z\", \"updated_at\": \"2026-05-15T01:20:52.194Z\", \"spec\": {\"hypothesis\": \"D054 rerun: max_tokens=1024. Verify truncation impact on LLaMA SciERC N=16.\", \"parent\": \"exp_007_llama_n16\", \"model_name\": \"llama3.1-8b-scierc-merged\", \"dataset\": \"SciERC\", \"seed\": 42, \"server\": \"autodl-5090\", \"command\": \"CUDA_VISIBLE_DEVICES=3 PYTHONPATH=code python code/run_mvp_pilot.py --model_path checkpoints/llama3.1-8b-scierc-merged --data_dir data/scierc/processed_data --dataset scierc --subtask ner --n_samples 16 --temperature 1.0 --seed 42 --num_test 9999 --max_tokens 1024 --collect_logprobs --output_dir output/exp_007_llama_n16_r1024\", \"data_path\": \"data/scierc/processed_data\", \"data_count\": 9999}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-15T01:20:52.194Z\"}, \"exp_001_seed123_v2_r1024\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T22:16:54.442Z\", \"updated_at\": \"2026-05-15T01:20:49.812Z\", \"spec\": {\"hypothesis\": \"D054 rerun: max_tokens=1024. Verify truncation impact on Qwen SciERC N=16 seed123.\", \"parent\": \"exp_001_seed123_v2\", \"model_name\": \"qwen3-8b-scierc-merged-v2\", \"dataset\": \"SciERC\", \"seed\": 123, \"server\": \"autodl-5090\", \"command\": \"CUDA_VISIBLE_DEVICES=1 PYTHONPATH=code python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc/processed_data --dataset scierc --subtask ner --n_samples 16 --temperature 1.0 --seed 123 --num_test 9999 --max_tokens 1024 --collect_logprobs --output_dir output/exp_001_seed123_v2_r1024\", \"data_path\": \"data/scierc/processed_data\", \"data_count\": 529}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-15T01:20:49.812Z\"}, \"exp_001_seed456_v2_ner_r1024\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T22:16:55.975Z\", \"updated_at\": \"2026-05-15T01:20:48.914Z\", \"spec\": {\"hypothesis\": \"D054 rerun: max_tokens=1024. Verify truncation impact on Qwen SciERC N=16 seed456.\", \"parent\": \"exp_001_seed456_v2_ner\", \"model_name\": \"qwen3-8b-scierc-merged-v2\", \"dataset\": \"SciERC\", \"seed\": 456, \"server\": \"autodl-5090\", \"command\": \"CUDA_VISIBLE_DEVICES=1 PYTHONPATH=code python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc/processed_data --dataset scierc --subtask ner --n_samples 16 --temperature 1.0 --seed 456 --num_test 9999 --max_tokens 1024 --collect_logprobs --output_dir output/exp_001_seed456_v2_ner_r1024\", \"data_path\": \"data/scierc/processed_data\", \"data_count\": 9999}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-15T01:20:48.914Z\"}, \"exp_001_seed42_v2_r1024\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T22:16:52.571Z\", \"updated_at\": \"2026-05-14T22:28:53.686Z\", \"spec\": {\"hypothesis\": \"D054 rerun: max_tokens=1024. Verify truncation impact on Qwen SciERC N=16 seed42.\", \"parent\": \"exp_001_seed42_v2\", \"model_name\": \"qwen3-8b-scierc-merged-v2\", \"dataset\": \"SciERC\", \"seed\": 42, \"server\": \"autodl-5090\", \"command\": \"CUDA_VISIBLE_DEVICES=0 PYTHONPATH=code python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc/processed_data --dataset scierc --subtask ner --n_samples 16 --temperature 1.0 --seed 42 --num_test 9999 --max_tokens 1024 --collect_logprobs --output_dir output/exp_001_seed42_v2_r1024\", \"data_path\": \"data/scierc/processed_data\", \"data_count\": 9999}, \"conclusion\": \"killed\", \"metrics\": {\"greedy_f1\": 0.6647, \"oracle_f1\": 0.8106, \"softjaccard_rho_full\": 0.3928, \"fleiss_rho_full\": 0.2489, \"logprob_rho_full\": 0.2136, \"softjaccard_rho_cond\": 0.3455, \"fleiss_rho_cond\": 0.163, \"logprob_rho_cond\": 0.1624, \"verdict\": \"MARGINAL\"}, \"checkpoint_path\": \"output/exp_001_seed42_v2_r1024\", \"log_path\": \"output/exp_001_seed42_v2_r1024/run.log\", \"completed_at\": \"2026-05-14T22:27:43.836Z\"}, \"exp_017_llama_conll_n16_s456\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T19:23:21.987Z\", \"updated_at\": \"2026-05-14T20:24:45.875Z\", \"hypothesis\": \"LLaMA CoNLL N=16 seed=456: structural>surface ranking preserved across seeds, complementing Qwen SciERC 3-seed protocol\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 python code/run_mvp_pilot.py --model_path checkpoints/llama3.1-8b-conll2003-merged --data_dir data/conll2003 --dataset conll2003 --subtask ner --n_samples 16 --temperature 1.0 --seed 456 --collect_logprobs --num_test 9999 --output_dir output/exp_017_llama_conll_n16_s456\", \"server\": \"autodl-5090\", \"data_path\": \"data/conll2003\", \"data_count\": 3453, \"model_name\": \"llama3.1-8b-conll2003-merged\", \"seed\": 456}, \"metrics\": {\"greedy_f1\": 0.9243, \"oracle_f1\": 0.9488, \"oracle_headroom\": 0.0245, \"n_instances\": 3453, \"n_valid\": 2756, \"n_conditional\": 2642, \"structural_beats_surface\": true, \"full\": {\"SJ_rho\": 0.4552, \"SJ_AUROC\": 0.7288, \"SJ_ECE\": 0.1134, \"FK_rho\": 0.4478, \"FK_AUROC\": 0.7248, \"FK_ECE\": 0.109, \"logprob_rho\": 0.3078, \"logprob_AUROC\": 0.7612, \"logprob_ECE\": 0.1289, \"EM_rho\": 0.452, \"EM_AUROC\": 0.7275, \"EM_ECE\": 0.1082, \"voting_conf_rho\": 0.4571, \"voting_conf_AUROC\": 0.7348, \"voting_conf_ECE\": 0.0863}, \"conditional\": {\"SJ_rho\": 0.4505, \"SJ_AUROC\": 0.7449, \"SJ_ECE\": 0.0826, \"FK_rho\": 0.4422, \"FK_AUROC\": 0.7401, \"FK_ECE\": 0.0835, \"logprob_rho\": 0.3242, \"logprob_AUROC\": 0.8067, \"logprob_ECE\": 0.0921, \"EM_rho\": 0.451, \"EM_AUROC\": 0.745, \"EM_ECE\": 0.0756, \"voting_conf_rho\": 0.3962, \"voting_conf_AUROC\": 0.7202, \"voting_conf_ECE\": 0.0746}, \"best_of_n\": {\"greedy\": 0.9243, \"random_avg\": 0.9215, \"sj_best\": 0.9243, \"logprob_best\": 0.9243, \"voting_conf_best\": 0.9243, \"oracle\": 0.9488}, \"n8_vs_n16_delta\": {\"full_SJ_rho_delta\": 0.0238, \"full_FK_rho_delta\": 0.0201, \"full_logprob_rho_delta\": 0.0006, \"full_EM_rho_delta\": 0.0214, \"full_voting_conf_rho_delta\": 0.0315, \"cond_SJ_rho_delta\": 0.0149, \"cond_FK_rho_delta\": 0.0112, \"cond_logprob_rho_delta\": -0.004, \"cond_EM_rho_delta\": 0.0107, \"cond_voting_conf_rho_delta\": 0.0219}}, \"checkpoint_path\": \"output/exp_017_llama_conll_n16_s456/samples.jsonl\", \"log_path\": \"output/exp_017_llama_conll_n16_s456/all_signals_report.json\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T20:24:45.875Z\"}, \"exp_017_llama_conll_n16_s123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T19:23:21.084Z\", \"updated_at\": \"2026-05-14T19:43:06.607Z\", \"hypothesis\": \"LLaMA CoNLL N=16 seed=123: structural>surface ranking preserved across seeds, complementing Qwen SciERC 3-seed protocol\", \"spec\": {\"hypothesis\": \"LLaMA CoNLL-2003 NER N=16 seed=123: cross-seed robustness check against N=8 seed=42 baseline (exp_017_llama_conll_infer)\", \"command\": \"CUDA_VISIBLE_DEVICES=1 python code/run_mvp_pilot.py --model_path checkpoints/llama3.1-8b-conll2003-merged --data_dir data/conll2003 --dataset conll2003 --subtask ner --n_samples 16 --temperature 1.0 --seed 123 --collect_logprobs --num_test 9999 --output_dir output/exp_017_llama_conll_n16_s123\", \"server\": \"autodl-5090\", \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/data/conll2003\", \"data_count\": 3453, \"model_name\": \"llama3.1-8b-conll2003-merged\", \"seed\": 123, \"checkpoint_source\": \"checkpoints/llama3.1-8b-conll2003-merged\", \"eval_data\": \"data/conll2003\", \"checkpoint_path\": \"output/exp_017_llama_conll_n16_s123/samples.jsonl\", \"log_path\": \"output/exp_017_llama_conll_n16_s123.log\"}, \"metrics\": {\"greedy_f1\": 0.9266, \"oracle_f1\": 0.9497, \"oracle_headroom\": 0.0231, \"n_instances\": 3453, \"n_valid\": 2756, \"n_conditional\": 2642, \"structural_beats_surface\": true, \"full\": {\"SJ_rho\": 0.4698, \"SJ_AUROC\": 0.7402, \"SJ_ECE\": 0.1135, \"FK_rho\": 0.4594, \"FK_AUROC\": 0.7351, \"FK_ECE\": 0.1114, \"logprob_rho\": 0.3161, \"logprob_AUROC\": 0.768, \"logprob_ECE\": 0.129, \"EM_rho\": 0.4676, \"EM_AUROC\": 0.7399, \"EM_ECE\": 0.1082, \"voting_conf_rho\": 0.4612, \"voting_conf_AUROC\": 0.7429, \"voting_conf_ECE\": 0.0832}, \"conditional\": {\"SJ_rho\": 0.4712, \"SJ_AUROC\": 0.7609, \"SJ_ECE\": 0.0828, \"FK_rho\": 0.4595, \"FK_AUROC\": 0.7547, \"FK_ECE\": 0.0858, \"logprob_rho\": 0.3314, \"logprob_AUROC\": 0.8134, \"logprob_ECE\": 0.0922, \"EM_rho\": 0.4732, \"EM_AUROC\": 0.7626, \"EM_ECE\": 0.075, \"voting_conf_rho\": 0.4086, \"voting_conf_AUROC\": 0.7338, \"voting_conf_ECE\": 0.0706}, \"best_of_n\": {\"greedy\": 0.9242, \"random_avg\": 0.9216, \"sj_best\": 0.9247, \"logprob_best\": 0.9253, \"voting_conf_best\": 0.9255, \"oracle\": 0.9486}, \"n8_vs_n16_delta\": {\"full_SJ_rho_delta\": 0.0384, \"full_FK_rho_delta\": 0.0317, \"full_logprob_rho_delta\": 0.0089, \"full_SJ_AUROC_delta\": 0.0363, \"full_FK_AUROC_delta\": 0.0325, \"full_logprob_AUROC_delta\": 0.007, \"cond_SJ_rho_delta\": 0.0356, \"cond_FK_rho_delta\": 0.0285, \"cond_logprob_rho_delta\": 0.0032}}, \"log_path\": \"output/exp_017_llama_conll_n16_s123.log\", \"checkpoint_path\": \"output/exp_017_llama_conll_n16_s123/samples.jsonl\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T19:43:06.607Z\"}, \"exp_008_re_n16_full\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T12:45:10.852Z\", \"updated_at\": \"2026-05-14T17:51:43.957Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && CUDA_VISIBLE_DEVICES=2 python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc/processed_data --dataset scierc --subtask re --n_samples 16 --temperature 1.0 --seed 42 --collect_logprobs --num_test 9999 --output_dir output/exp008_re_n16/\\\"\", \"server\": \"gpu-5090-4x-2\", \"gpu\": [\"cuda:2\"], \"pid\": \"62585\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_008_re_n16_full.log\", \"submitted_at\": \"2026-05-14T12:45:10.764Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 18393.2, \"gpu_hours\": 5.11}, \"conclusion\": \"killed\", \"failure_reason\": \"superseded by exp_008_re_n16_t10_full (full 551-instance RE-only run on autodl-5090)\", \"completed_at\": \"2026-05-14T17:51:43.957Z\"}, \"exp_001_n16_seed123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T12:10:29.393Z\", \"updated_at\": \"2026-05-14T12:42:58.393Z\", \"spec\": {\"command\": \"python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc/processed_data --dataset scierc --subtask joint --n_samples 16 --temperature 1.0 --seed 123 --collect_logprobs\", \"server\": \"gpu-5090-4x-2\", \"data_path\": \"data/scierc/processed_data\", \"data_count\": 551, \"model_name\": \"qwen3-8b-scierc-merged-v2\", \"seed\": 123, \"num_instances\": 200, \"partial\": true, \"note\": \"Only 200/551 instances due to --num_test default bug. Needs full rerun.\"}, \"metrics\": {\"ner\": {\"greedy_f1\": 0.655, \"oracle_f1\": 0.8028, \"headroom\": 0.1478, \"rho_sj_full\": 0.4076, \"rho_fk_full\": 0.2799, \"rho_logprob_full\": 0.3189, \"rho_sj_cond\": 0.4271, \"rho_fk_cond\": 0.2743, \"rho_logprob_cond\": 0.2835, \"sj_beats_fk\": true, \"rho_advantage\": 0.1277}, \"re\": {\"greedy_f1\": 0.4243, \"oracle_f1\": 0.6771, \"headroom\": 0.2528, \"rho_sj_full\": 0.2943, \"rho_fk_full\": 0.2657, \"rho_logprob_full\": 0.3005, \"rho_sj_cond\": 0.4003, \"rho_fk_cond\": 0.313, \"rho_logprob_cond\": 0.2317, \"sj_beats_fk\": true, \"rho_advantage\": 0.0286}, \"verdict\": \"FAIL\"}, \"conclusion\": \"success\", \"checkpoint_path\": \"N/A\", \"log_path\": \"output/exp001_n16_seed123/\", \"completed_at\": \"2026-05-14T12:28:38.104Z\"}, \"exp_016_signal_ensemble\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T12:15:23.771Z\", \"updated_at\": \"2026-05-14T12:42:55.931Z\", \"spec\": {\"command\": \"python code/analyze_exp016_ensemble.py\", \"server\": \"autodl-5090\", \"data_path\": \"output/exp_012_logprob/samples_with_logprobs.jsonl\", \"data_count\": 551, \"model_name\": \"N/A (CPU-only analysis)\", \"seed\": 42, \"checkpoint_source\": \"N/A\", \"eval_data\": \"pilot_004\", \"checkpoint_path\": \"N/A\", \"log_path\": \"output/exp016_signal_ensemble/\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T12:15:53.341Z\", \"metrics\": {\"sj_logprob_pearson_ner\": 0.57, \"sj_logprob_pearson_re\": 0.42, \"best_linear_ner\": {\"combo\": \"SJ+voting_conf\", \"alpha\": 0.3, \"rho\": 0.489}, \"best_linear_re\": {\"combo\": \"voting_conf+logprob\", \"alpha\": 0.6, \"rho\": 0.429}, \"ensemble_ner_auroc\": 0.735, \"ensemble_re_auroc\": 0.719, \"best_single_ner_auroc\": 0.7, \"best_single_re_auroc\": 0.721, \"ensemble_ner_delta\": 0.035, \"selection_f1_ner\": {\"greedy\": 0.609, \"logprob\": 0.609, \"sj\": 0.604, \"ensemble\": 0.604, \"voting\": 0.596, \"random\": 0.58, \"oracle\": 0.769}, \"selection_f1_re\": {\"logprob\": 0.397, \"greedy\": 0.374, \"sj\": 0.368, \"ensemble\": 0.367, \"voting\": 0.338, \"random\": 0.338, \"oracle\": 0.561}, \"diagnosis\": \"SJ+voting_conf linear combo boosts NER ρ to 0.489 (+23%). RE: logprob-best is ONLY method beating greedy (0.397 vs 0.374). Ensemble AUROC +0.035 on NER. Oracle gap still huge.\"}}, \"exp_001_ner_n16_scierc\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T11:42:10.898Z\", \"updated_at\": \"2026-05-14T12:42:49.592Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && CUDA_VISIBLE_DEVICES=0 python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc/processed_data --dataset scierc --subtask joint --n_samples 16 --temperature 1.0 --seed 42 --output_dir output/exp001_n16_seed42 --num_test 9999 --collect_logprobs 2>&1 | tee output/exp001_n16_seed42_run.log\\\"\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:0\"], \"pid\": \"54357\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_001_ner_n16_scierc.log\", \"submitted_at\": \"2026-05-14T12:15:46.646Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"server\": \"autodl-5090\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"reproduce\": {\"server\": \"autodl-5090\", \"gpu\": \"cuda:0\", \"started_at\": \"2026-05-14T11:43:48.643Z\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T11:55:45.664Z\", \"metrics\": {\"n_instances\": 551, \"ner_n\": 529, \"re_n\": 397, \"N\": 16, \"T\": 1, \"seed\": 42, \"full_test_set\": true, \"ner_voting_conf_rho\": 0.399, \"ner_sj_rho\": 0.398, \"ner_em_rho\": 0.339, \"ner_fk_rho\": 0.288, \"ner_logprob_rho\": 0.237, \"ner_voting_conf_auroc\": 0.704, \"ner_sj_auroc\": 0.697, \"ner_cond_em_rho\": 0.414, \"ner_cond_sj_rho\": 0.349, \"ner_cond_vc_rho\": 0.34, \"re_voting_conf_rho\": 0.38, \"re_logprob_rho\": 0.293, \"re_fk_rho\": 0.281, \"re_sj_rho\": 0.277, \"re_em_rho\": 0.148, \"re_voting_conf_auroc\": 0.699, \"re_cond_em_rho\": 0.475, \"re_cond_sj_rho\": 0.318, \"re_cond_vc_rho\": 0.35, \"re_cond_em_auroc\": 0.742, \"diagnosis\": \"551 instances T=1.0: voting_conf best on full set (NER 0.399, RE 0.380). EM SURPRISE best on conditional set (NER cond 0.414, RE cond 0.475). RE full FAIL (SJ 0.277 < 0.40). Previous N-scaling 'breakthrough' was artifact of 200 instances + T=0.7.\"}}, \"exp_002\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T12:39:53.226Z\", \"updated_at\": \"2026-05-14T12:40:17.202Z\", \"spec\": {\"command\": \"python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-conll2003-merged --dataset conll2003 --subtask ner --n_samples 8 --temperature 1.0 --collect_logprobs --num_test 99999\", \"server\": \"autodl-5090\", \"data_path\": \"data/conll2003\", \"data_count\": 3453, \"model_name\": \"qwen3-8b-conll2003-lora-merged\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen3-8b-conll2003-merged\", \"log_path\": \"/tmp/pilot_conll2003.log\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T12:40:08.402Z\", \"metrics\": {\"sj_rho_full\": 0.4357, \"sj_tau_full\": 0.3851, \"sj_auroc_full\": 0.8008, \"sj_rho_cond\": 0.4511, \"fk_rho_full\": 0.3998, \"fk_tau_full\": 0.3568, \"fk_auroc_full\": 0.7741, \"fk_rho_cond\": 0.4064, \"logprob_rho_full\": 0.3157, \"logprob_tau_full\": 0.2469, \"logprob_auroc_full\": 0.7532, \"logprob_rho_cond\": 0.3562, \"em_rho_full\": 0.4507, \"em_tau_full\": 0.4002, \"em_auroc_full\": 0.8156, \"em_rho_cond\": 0.4799, \"ev_rho_full\": 0.4237, \"ev_tau_full\": 0.3777, \"ev_auroc_full\": 0.7889, \"ev_rho_cond\": 0.4127, \"greedy_f1\": 0.9123, \"oracle_f1\": 0.9543, \"voting_f1\": 0.9141, \"oracle_headroom\": 0.042, \"sj_vs_logprob_delta_rho\": 0.12, \"sj_vs_logprob_ci_low\": 0.0881, \"sj_vs_logprob_ci_high\": 0.154, \"sj_vs_logprob_significant\": true, \"n_instances\": 3453, \"n_valid\": 2756, \"n_samples\": 8, \"temperature\": 1}}, \"exp_002_ner_conll2003\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T11:42:15.223Z\", \"updated_at\": \"2026-05-14T12:27:35.413Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && CUDA_VISIBLE_DEVICES=0 python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-conll2003-merged --data_dir data/conll2003 --dataset conll2003 --subtask ner --n_samples 8 --temperature 1.0 --max_tokens 1024 --output_dir output/exp002_conll2003 --num_test 99999 --seed 42 --collect_logprobs 2>&1 | tee /tmp/pilot_conll2003.log\\\"\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:0\"], \"pid\": \"58208\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_002_ner_conll2003.log\", \"submitted_at\": \"2026-05-14T12:27:35.337Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"server\": \"autodl-5090\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"reproduce\": {\"server\": \"autodl-5090\", \"gpu\": \"cuda:1\", \"started_at\": \"2026-05-14T11:43:49.959Z\"}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen3-8b-conll2003-lora\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_002_ner_conll2003.log\", \"completed_at\": \"2026-05-14T12:18:04.097Z\"}, \"exp_004_re_diagnostic\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T11:49:44.497Z\", \"updated_at\": \"2026-05-14T11:50:24.620Z\", \"spec\": {\"hypothesis\": \"RE diagnostic: per-relation-type breakdown reveals which types drive low RE rho; error propagation and threshold sensitivity clarify the gap between NER and RE consistency signals\", \"model_name\": \"N/A (reuse pilot_004 samples)\", \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/mvp_pilot_004\", \"data_count\": 551, \"server\": \"autodl-5090\", \"seed\": 42, \"parent\": \"mvp_pilot_004\", \"method\": \"Per-relation-type SJ/FK/voting rho, error propagation classification, threshold sensitivity, bootstrap CI, Fisher z-test NER vs RE\", \"command\": \"python3 code/analyze_exp004_re_diagnostic.py\", \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp004_re_diagnostic\", \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp004_re_diagnostic/\", \"checkpoint_source\": \"mvp_pilot_004\", \"eval_data\": \"scierc_test_551\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T11:50:04.662Z\", \"metrics\": {\"per_relation_type\": {\"HYPONYM-OF\": {\"n\": 36, \"rho_sj\": 0.545, \"rho_fk\": 0.646, \"rho_vc\": 0.628, \"mean_f1\": 0.513}, \"CONJUNCTION\": {\"n\": 86, \"rho_sj\": 0.383, \"rho_fk\": 0.35, \"rho_vc\": 0.484, \"mean_f1\": 0.48}, \"USED-FOR\": {\"n\": 299, \"rho_sj\": 0.236, \"rho_fk\": 0.255, \"rho_vc\": 0.286, \"mean_f1\": 0.422}, \"PART-OF\": {\"n\": 44, \"rho_sj\": 0.239, \"rho_fk\": 0.348, \"rho_vc\": 0.283, \"mean_f1\": 0.297}, \"EVALUATE-FOR\": {\"n\": 62, \"rho_sj\": 0.172, \"rho_fk\": 0.255, \"rho_vc\": 0.226, \"mean_f1\": 0.365}, \"COMPARE\": {\"n\": 35, \"rho_sj\": 0.168, \"rho_fk\": 0.184, \"rho_vc\": 0.18, \"mean_f1\": 0.453}, \"FEATURE-OF\": {\"n\": 50, \"rho_sj\": 0.004, \"rho_fk\": 0.052, \"rho_vc\": 0.014, \"mean_f1\": 0.254}}, \"error_propagation\": {\"total_fn\": 553, \"tail_error_pct\": 21.9, \"full_error_pct\": 21.7, \"head_error_pct\": 17.7, \"head_tail_error_pct\": 15.9, \"type_error_pct\": 8.3, \"worst_consistency\": \"head_type_error (sj=0.411)\", \"best_consistency\": \"head_error (sj=0.613)\"}, \"threshold_sensitivity\": {\"thr_0.00_rho_sj\": 0.3161, \"thr_0.00_rho_vc\": 0.3841, \"thr_0.00_n\": 313, \"thr_0.05_rho_sj\": 0.2682, \"thr_0.05_rho_vc\": 0.2364, \"thr_0.05_n\": 239}, \"bootstrap_ci_95\": {\"ner_sj\": [0.2946, 0.4586], \"ner_voting_conf\": [0.3048, 0.4656], \"re_sj\": [0.1422, 0.3391], \"re_voting_conf\": [0.1818, 0.3721], \"re_cond_sj\": [0.2161, 0.4102], \"re_cond_voting_conf\": [0.2825, 0.474]}, \"fisher_z_ner_vs_re\": {\"sj_z\": 2.31, \"sj_p\": 0.0209, \"sj_significant\": true, \"fk_z\": -0.31, \"fk_p\": 0.756, \"fk_significant\": false, \"voting_z\": 1.914, \"voting_p\": 0.0556, \"voting_significant\": false}, \"diagnosis\": \"FEATURE-OF is near-zero rho across all signals (n=50, F1=0.254). HYPONYM-OF strongest (rho_fk=0.646). Entity span errors (head+tail) account for 55.5% of RE FN. NER rho_sj significantly > RE rho_sj (p=0.021). Voting_conf is best RE signal in conditional set (rho=0.384).\"}}, \"exp_005\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T11:45:16.360Z\", \"updated_at\": \"2026-05-14T11:45:38.570Z\", \"spec\": {\"hypothesis\": \"Temperature sensitivity: systematic comparison of T=0.7 vs T=1.0 on all 5 confidence signals\", \"method\": \"CPU-only analysis from checkpoint metrics (pilot_004 T=1.0, pilot_005 T=0.7, exp_012/013/014)\", \"data_count\": 551, \"model_name\": \"Qwen3-8B-SciERC-LoRA-v2\", \"data_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/exp005_temperature/\", \"server\": \"local\", \"seed\": 42, \"parent\": \"mvp_pilot_004,mvp_pilot_005\", \"command\": \"python3 analyze_exp005_temperature.py\", \"checkpoint_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/exp005_temperature/\", \"log_path\": \"N/A\", \"checkpoint_source\": \"pilot_004+pilot_005 checkpoint metrics\", \"eval_data\": \"SciERC test set (n=551)\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T11:45:38.570Z\"}, \"exp_014_entity_majority_voting\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T10:53:21.203Z\", \"updated_at\": \"2026-05-14T11:33:30.085Z\", \"spec\": {\"hypothesis\": \"Entity-level majority voting confidence beats SJ as correlation signal\", \"model_name\": \"N/A (reuse pilot_004 samples)\", \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/mvp_pilot_004\", \"data_count\": 551, \"server\": \"autodl-5090\", \"seed\": 42, \"parent\": \"mvp_pilot_004\", \"method\": \"Per-entity voting across N=8 samples, consensus construction, confidence = mean voting rate\", \"command\": \"python code/analyze_entity_voting.py\", \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/mvp_pilot_004\", \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/mvp_pilot_004/exp014_entity_voting_report.json\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T11:18:09.468Z\", \"metrics\": {\"ner_full_rho\": 0.3915, \"ner_full_p\": 8.1e-21, \"ner_full_tau\": 0.2906, \"ner_full_auroc\": 0.7039, \"re_full_rho\": 0.3403, \"re_full_p\": 3.21e-12, \"re_full_tau\": 0.256, \"re_full_auroc\": 0.6668, \"ner_voting_f1\": 0.6246, \"ner_greedy_f1\": 0.6483, \"ner_oracle_f1\": 0.7793, \"re_voting_f1\": 0.3577, \"re_greedy_f1\": 0.4022, \"re_oracle_f1\": 0.5886, \"diagnosis\": \"Voting confidence BEATS SJ on both NER (rho 0.392 vs 0.383) and RE (0.340 vs 0.244). But voting as selection strategy LOSES to greedy.\"}}, \"exp_013_exact_match_voting\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T10:53:18.753Z\", \"updated_at\": \"2026-05-14T11:33:22.644Z\", \"spec\": {\"hypothesis\": \"Exact-match voting rate correlates with F1\", \"model_name\": \"N/A (reuse pilot_004 samples)\", \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/mvp_pilot_004\", \"data_count\": 551, \"server\": \"autodl-5090\", \"seed\": 42, \"parent\": \"mvp_pilot_004\", \"method\": \"Count exact-match duplicates across N=8 samples\", \"command\": \"python code/analyze_exact_match_voting.py\", \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/mvp_pilot_004\", \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/mvp_pilot_004/exp013_exact_match_report.json\"}, \"conclusion\": \"negative\", \"completed_at\": \"2026-05-14T11:18:09.026Z\", \"metrics\": {\"ner_full_rho\": 0.2941, \"ner_full_p\": 5.12e-12, \"ner_full_tau\": 0.2181, \"ner_full_auroc\": 0.6398, \"re_full_rho\": 0.1562, \"re_full_p\": 0.0018, \"re_full_tau\": 0.1185, \"re_full_auroc\": 0.5863, \"diagnosis\": \"EM between SJ and FK on NER, weakest on RE. Too coarse-grained.\"}}, \"exp_012_logprob_baseline\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T10:53:16.166Z\", \"updated_at\": \"2026-05-14T11:13:30.240Z\", \"spec\": {\"hypothesis\": \"Log-probability baseline: mean sequence log-prob correlates with F1 as well as or better than SJ\", \"model_name\": \"ft_002_v2 (qwen3-8b-scierc-merged-v2)\", \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/mvp_pilot_004\", \"data_count\": 551, \"server\": \"autodl-5090\", \"seed\": 42, \"parent\": \"mvp_pilot_004\", \"method\": \"vLLM forward pass for log-probs + Spearman rho + AUROC + Kendall tau\", \"command\": \"python3 code/extract_logprobs.py\", \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/mvp_pilot_004\", \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/mvp_pilot_004/logprob_analysis.log\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T11:06:42.542Z\", \"metrics\": {\"ner_full_rho_sj\": 0.3565, \"ner_full_rho_fk\": 0.2651, \"ner_full_rho_logprob\": 0.1396, \"ner_full_rho_greedy_logprob\": 0.1615, \"ner_full_tau_sj\": 0.2658, \"ner_full_tau_logprob\": 0.1006, \"ner_full_auroc_sj\": 0.6892, \"ner_full_auroc_fk\": 0.6292, \"ner_full_auroc_logprob\": 0.5907, \"ner_full_n\": 529, \"ner_sj_vs_logprob_delta\": 0.2169, \"re_full_rho_sj\": 0.2112, \"re_full_rho_fk\": 0.2528, \"re_full_rho_logprob\": 0.2467, \"re_full_auroc_sj\": 0.5916, \"re_full_auroc_fk\": 0.6262, \"re_full_auroc_logprob\": 0.6186, \"re_full_n\": 397, \"re_cond_rho_sj\": 0.3683, \"re_cond_rho_fk\": 0.3168, \"re_cond_rho_logprob\": 0.1457, \"re_cond_auroc_sj\": 0.6839, \"re_cond_auroc_logprob\": 0.5487, \"re_cond_n\": 296, \"diagnosis\": \"NER: SJ crushes logprob (rho +0.217). RE full: logprob slightly ahead. RE cond: SJ crushes logprob (rho +0.223). SJ unique value CONFIRMED.\"}}, \"mvp_pilot_005\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T09:14:09.456Z\", \"updated_at\": \"2026-05-14T09:47:06.597Z\", \"spec\": {\"hypothesis\": \"T=0.7 降低 RE zero rate，恢复 SJ>FK，rho_sj 可能 ≥ 0.30 (MARGINAL threshold)\", \"model_name\": \"Qwen3-8B-SciERC-LoRA-v2 (ft_002_v2 final)\", \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/data/scierc/processed_data\", \"data_count\": 551, \"server\": \"autodl-5090\", \"seed\": 42, \"parent\": \"ft_002_v2\", \"method\": \"N=8 sampling T=0.7 + XGrammar + span realignment + max_tokens=1024 + gold-empty filter + conditional rho\", \"command\": \"CUDA_VISIBLE_DEVICES=0 python3 code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc/processed_data --dataset scierc --subtask joint --n_samples 8 --temperature 0.7 --max_tokens 1024 --output_dir output/mvp_pilot_005 --num_test 551 --seed 42 --tensor_parallel 1\", \"gpu\": \"cuda:0\", \"pid\": 32456, \"tmux_session\": \"mvp_pilot_005\", \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/mvp_pilot_005/train.log\"}, \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/mvp_pilot_005\", \"metrics\": {\"ner_greedy_f1\": 0.6619, \"ner_oracle_f1\": 0.7585, \"ner_headroom\": 0.0966, \"ner_fleiss_kappa_mean\": 0.4722, \"ner_soft_jaccard_mean\": 0.7757, \"ner_full_rho_sj\": 0.3875, \"ner_full_rho_fk\": 0.3211, \"ner_full_n\": 529, \"ner_cond_rho_sj\": 0.3868, \"ner_cond_rho_fk\": 0.305, \"ner_cond_n\": 504, \"ner_sj_beats_fk_full\": true, \"ner_sj_beats_fk_cond\": true, \"ner_rho_advantage\": 0.0664, \"ner_sample_f1_mean\": 0.6243, \"ner_sample_f1_std\": 0.3131, \"ner_sample_f1_pct_zero\": 11.2, \"ner_gold_empty_filtered\": 22, \"ner_all_zero_filtered\": 25, \"re_greedy_f1\": 0.4219, \"re_oracle_f1\": 0.5532, \"re_headroom\": 0.1313, \"re_fleiss_kappa_mean\": 0.3829, \"re_soft_jaccard_mean\": 0.687, \"re_full_rho_sj\": 0.2343, \"re_full_rho_fk\": 0.1835, \"re_full_n\": 397, \"re_cond_rho_sj\": 0.3716, \"re_cond_rho_fk\": 0.2533, \"re_cond_n\": 301, \"re_sj_beats_fk_full\": true, \"re_sj_beats_fk_cond\": true, \"re_rho_advantage\": 0.0508, \"re_sample_f1_mean\": 0.3782, \"re_sample_f1_std\": 0.3845, \"re_sample_f1_pct_zero\": 42.4, \"re_gold_empty_filtered\": 154, \"re_all_zero_filtered\": 96, \"parse_failures\": 0, \"verdict\": \"FAIL\", \"verdict_note\": \"RE full rho_sj=0.234 < 0.40; RE cond rho_sj=0.372 passes conditional but not full threshold\"}, \"conclusion\": \"negative\", \"completed_at\": \"2026-05-14T09:47:06.597Z\"}, \"e1_component_wise_re_sj\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T09:15:17.262Z\", \"updated_at\": \"2026-05-14T09:23:38.818Z\", \"spec\": {\"hypothesis\": \"RE SJ 乘性惩罚是 root cause：分解后 head_sj ρ ≈ NER ρ (~0.38)，tail_sj 和乘性组合拖低整体 ρ\", \"model_name\": \"N/A (reuse pilot_004 samples)\", \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/mvp_pilot_004\", \"data_count\": 397, \"server\": \"autodl-5090\", \"seed\": 42, \"parent\": \"mvp_pilot_004\", \"method\": \"Component-wise decomposition: head_sj, tail_sj, type_match 分别计算 Spearman ρ vs per-instance RE F1\", \"command\": \"python3 code/analyze_component_wise_re.py\", \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/mvp_pilot_004\", \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/mvp_pilot_004/e1_component_analysis.log\"}, \"conclusion\": \"negative\", \"metrics\": {\"full_head_sj_rho\": 0.21, \"full_tail_sj_rho\": 0.201, \"full_type_match_rho\": 0.201, \"full_multiplicative_rho\": 0.244, \"full_additive_rho\": 0.243, \"full_fleiss_kappa_rho\": 0.278, \"cond_head_sj_rho\": 0.27, \"cond_tail_sj_rho\": 0.259, \"cond_type_match_rho\": 0.252, \"cond_multiplicative_rho\": 0.316, \"cond_additive_rho\": 0.306, \"cond_fleiss_kappa_rho\": 0.307, \"n_full\": 397, \"n_conditional\": 313, \"diagnosis\": \"head_sj rho=0.210 FAR from NER rho=0.383. Multiplicative penalty hypothesis REJECTED. Problem is fundamental: span-level SJ lacks discriminative power for RE.\"}, \"completed_at\": \"2026-05-14T09:22:26.155Z\"}, \"mvp_pilot_004\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T08:51:38.203Z\", \"updated_at\": \"2026-05-14T09:10:40.918Z\", \"spec\": {\"hypothesis\": \"With improved RE quality (F1=41.8%), structural self-consistency (soft Jaccard) correlates with per-instance F1 better than surface Fleiss Kappa, reaching rho_sj >= 0.40 on RE\", \"model_name\": \"Qwen3-8B-SciERC-LoRA-v2 (ft_002_v2 final)\", \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/data/scierc/processed_data\", \"data_count\": 551, \"server\": \"autodl-5090\", \"seed\": 42, \"parent\": \"ft_002_v2\", \"method\": \"N=8 sampling T=1.0 + XGrammar + span realignment + max_tokens=1024 + gold-empty filter + conditional rho\", \"command\": \"CUDA_VISIBLE_DEVICES=0 python3 code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc/processed_data --dataset scierc --subtask joint --n_samples 8 --temperature 1.0 --max_tokens 1024 --output_dir output/mvp_pilot_004 --num_test 551 --seed 42 --tensor_parallel 1\", \"gpu\": \"cuda:0\", \"pid\": 31041, \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/mvp_pilot_004/mvp_pilot_004.log\", \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/mvp_pilot_004\"}, \"metrics\": {\"ner_greedy_f1\": 0.6671, \"ner_oracle_f1\": 0.7756, \"ner_headroom\": 0.1085, \"ner_fleiss_kappa_mean\": 0.4048, \"ner_soft_jaccard_mean\": 0.7008, \"ner_full_rho_fk\": 0.259, \"ner_full_rho_sj\": 0.3825, \"ner_full_n\": 529, \"ner_cond_rho_fk\": 0.2352, \"ner_cond_rho_sj\": 0.3762, \"ner_cond_n\": 508, \"ner_sj_beats_fk_full\": true, \"ner_sj_beats_fk_cond\": true, \"ner_sample_f1_mean\": 0.6084, \"ner_sample_f1_std\": 0.3174, \"ner_sample_f1_pct_zero\": 12.19, \"ner_gold_empty_filtered\": 22, \"ner_all_zero_filtered\": 21, \"re_greedy_f1\": 0.4208, \"re_oracle_f1\": 0.5882, \"re_headroom\": 0.1674, \"re_fleiss_kappa_mean\": 0.2996, \"re_soft_jaccard_mean\": 0.6114, \"re_full_rho_fk\": 0.2782, \"re_full_rho_sj\": 0.2441, \"re_full_n\": 397, \"re_cond_rho_fk\": 0.3067, \"re_cond_rho_sj\": 0.3161, \"re_cond_n\": 313, \"re_sj_beats_fk_full\": false, \"re_sj_beats_fk_cond\": true, \"re_sample_f1_mean\": 0.3612, \"re_sample_f1_std\": 0.383, \"re_sample_f1_pct_zero\": 44.3, \"re_gold_empty_filtered\": 154, \"re_all_zero_filtered\": 84, \"parse_failures\": 0, \"verdict\": \"FAIL\"}, \"conclusion\": \"negative\", \"completed_at\": \"2026-05-14T09:10:40.918Z\"}, \"ft_002_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T08:28:40.861Z\", \"updated_at\": \"2026-05-14T08:51:32.405Z\", \"spec\": {\"hypothesis\": \"Extended training (5 epochs, LoRA r=32) with OOM fix improves RE F1 above 40% threshold\", \"model_name\": \"Qwen/Qwen3-8B\", \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/data/llmfactory_train.json\", \"data_count\": 1861, \"server\": \"autodl-5090\", \"seed\": 42, \"parent\": \"ft_001\", \"method\": \"LoRA r=32 alpha=64, 5 epochs, batch=2 grad_accum=8 gradient_checkpointing=true\", \"gpu\": \"cuda:1\", \"pid\": 24947, \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/ft_002v2_train.log\", \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen3-8b-scierc-lora-v2\", \"command\": \"CUDA_VISIBLE_DEVICES=1 llamafactory-cli train train_config_v2.yaml\"}, \"conclusion\": \"success\", \"metrics\": {\"epoch\": 5, \"train_loss\": 0.0806, \"eval_loss\": 0.089, \"train_runtime\": \"28m41s\", \"train_samples_per_second\": 5.407, \"train_steps_per_second\": 0.34, \"total_steps\": 585, \"checkpoints\": [\"checkpoint-400\", \"checkpoint-500\", \"checkpoint-585\"], \"gate0_final_ner_f1\": 0.6615, \"gate0_final_re_f1\": 0.4177, \"gate0_final_parse_failures\": 0, \"gate0_final_ner_pass\": true, \"gate0_final_re_pass\": true, \"gate0_final_pass\": true, \"gate0_ckpt400_ner_f1\": 0.6475, \"gate0_ckpt400_re_f1\": 0.3793, \"gate0_ckpt400_parse_failures\": 0, \"gate0_ckpt400_verdict\": \"FAIL\", \"gate0_ckpt400_re_sample_f1_pct_zero\": 58.8, \"gate0_ckpt400_warning\": \">30% samples F1=0\"}, \"completed_at\": \"2026-05-14T08:51:32.405Z\"}, \"mvp_pilot_002\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T08:02:16.991Z\", \"updated_at\": \"2026-05-14T08:48:14.040Z\", \"spec\": {\"hypothesis\": \"Structural self-consistency (soft Jaccard) correlates with per-instance F1 better than surface Fleiss Kappa on fine-tuned Qwen3-8B SciERC\", \"model_name\": \"Qwen3-8B-SciERC-LoRA (ft_001)\", \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/data/scierc\", \"data_count\": 551, \"server\": \"autodl-5090\", \"seed\": 42, \"parent\": \"ft_001\", \"method\": \"N=8 sampling T=1.0 + XGrammar + span realignment + gold-empty filter + conditional rho\", \"gpu\": \"cuda:0\", \"note\": \"Rerun of mvp_pilot_001 which crashed silently\", \"command\": \"CUDA_VISIBLE_DEVICES=0 python3 code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-lora --data_dir data/scierc --dataset scierc --subtask joint --n_samples 8 --temperature 1.0 --max_tokens 512 --output_dir output/mvp_pilot_001 --num_test 551 --seed 42 --tensor_parallel 1\", \"failure_reason\": \"Worker used LoRA adapter path instead of merged model path; vLLM cannot load LoRA adapter directly\"}, \"conclusion\": \"failed\", \"completed_at\": \"2026-05-14T08:48:14.040Z\"}, \"ft_002\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T07:39:18.640Z\", \"updated_at\": \"2026-05-14T08:28:00.590Z\", \"spec\": {\"hypothesis\": \"Extended training (5 epochs, LoRA r=32) improves RE F1 above 40% threshold\", \"model_name\": \"Qwen/Qwen3-8B\", \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/data/llmfactory_train.json\", \"data_count\": 1861, \"server\": \"autodl-5090\", \"seed\": 42, \"parent\": \"ft_001\", \"method\": \"LoRA r=32 alpha=64, 5 epochs, relation direction hint\", \"command\": \"llamafactory-cli train /root/autodl-tmp/struct_self_consist_ie/train_config_v2.yaml\", \"gpu\": \"cuda:1\", \"pid\": 19666, \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/ft_002_train.log\", \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen3-8b-scierc-lora-v2\", \"total_steps\": 585, \"trainable_params\": \"87.3M\", \"estimated_runtime\": \"29min\"}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-14T08:02:30.390Z\", \"metrics\": {\"last_step\": 70, \"total_steps\": 585, \"progress_pct\": 11.97, \"last_loss\": 0.1134, \"last_lr\": 0.00019982, \"elapsed\": \"3m32s\", \"failure_reason\": \"OOM at step 73, batch_size=4 too large for 32GB RTX 5090\"}}, \"ft_001\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T06:04:28.030Z\", \"updated_at\": \"2026-05-14T08:27:58.182Z\", \"spec\": {\"hypothesis\": \"Fine-tuned Qwen3-8B on SciERC UIE can achieve NER F1 >= 73 and serve as base model for structural consistency MVP\", \"model_name\": \"Qwen/Qwen3-8B\", \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/data/scierc\", \"data_count\": 1861, \"server\": \"autodl-5090\", \"seed\": 42, \"method\": \"LoRA r=16 alpha=32\", \"framework\": \"LLaMA Factory 0.9.4\", \"command\": \"sft training qwen3-8b on scierc with lora\", \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen3-8b-scierc-lora/\", \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/checkpoints/ft_001_train.log\", \"train_loss\": 0.1099, \"eval_loss\": 0.0771, \"epoch\": 3, \"train_runtime\": \"0:17:49\", \"note\": \"gate0: NER PASS 60.4% / RE FAIL 33.8%\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T06:30:32.889Z\", \"metrics\": {\"train_loss\": 0.1099, \"eval_loss\": 0.0771, \"gate0_ner_f1_strict\": 0.1143, \"gate0_re_f1_strict\": 0.0125, \"gate0_ner_f1_text\": 0.606, \"gate0_re_f1_text\": 0.3392, \"gate0_offset_accuracy\": 0.1665, \"gate0_parse_failures\": 43, \"gate0_pass\": false, \"gate0_realigned_ner_f1\": 0.6045, \"gate0_realigned_re_f1\": 0.338, \"gate0_realigned_entity_offset_accuracy\": 1, \"gate0_realigned_relation_offset_accuracy\": 1, \"gate0_realigned_ner_pass\": true, \"gate0_realigned_re_pass\": false, \"gate0_realigned_pass\": false, \"gate0_ner_f1_delta_realign\": 0.4901, \"gate0_re_f1_delta_realign\": 0.3255, \"verdict_note\": \"partial: NER PASS (60.4%) / RE FAIL (33.8% < 40%)\"}}, \"mvp_pilot_003\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T08:21:09.847Z\", \"updated_at\": \"2026-05-14T08:21:44.983Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python code/run_mvp_pilot.py --model_path /root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen3-8b-scierc-merged --data_dir /root/autodl-tmp/struct_self_consist_ie/data/scierc/processed_data --dataset scierc --subtask joint --n_samples 8 --temperature 1.0 --max_tokens 1024 --output_dir /root/autodl-tmp/struct_self_consist_ie/output/mvp_pilot_003 --num_test 551 --seed 42 --tensor_parallel 1\", \"server\": \"autodl-5090\", \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/data/scierc/processed_data\", \"data_count\": 551, \"model_name\": \"qwen3-8b-scierc-merged\", \"seed\": 42}, \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/mvp_pilot_003.log\", \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/mvp_pilot_003\", \"conclusion\": \"negative\", \"completed_at\": \"2026-05-14T08:21:30.319Z\", \"metrics\": {\"ner_greedy_f1\": 0.6362, \"ner_oracle_f1\": 0.792, \"ner_headroom\": 0.1559, \"ner_fleiss_kappa_mean\": 0.2488, \"ner_soft_jaccard_mean\": 0.5066, \"ner_full_rho_sj\": 0.3808, \"ner_full_rho_fk\": 0.3362, \"ner_full_p_sj\": 1.07e-19, \"ner_full_p_fk\": 1.93e-15, \"ner_full_n\": 529, \"ner_cond_rho_sj\": 0.3836, \"ner_cond_rho_fk\": 0.3187, \"ner_cond_p_sj\": 1.83e-19, \"ner_cond_p_fk\": 1.33e-13, \"ner_cond_n\": 514, \"ner_sj_beats_fk_full\": true, \"ner_sj_beats_fk_cond\": true, \"ner_rho_advantage\": 0.0446, \"ner_sample_f1_mean\": 0.5153, \"ner_sample_f1_std\": 0.3334, \"ner_sample_f1_pct_zero\": 19.9, \"ner_gold_empty_filtered\": 22, \"ner_all_zero_filtered\": 15, \"re_greedy_f1\": 0.3774, \"re_oracle_f1\": 0.5939, \"re_headroom\": 0.2165, \"re_fleiss_kappa_mean\": 0.0879, \"re_soft_jaccard_mean\": 0.3958, \"re_full_rho_sj\": 0.2367, \"re_full_rho_fk\": 0.2221, \"re_full_p_sj\": 1.85e-06, \"re_full_p_fk\": 7.92e-06, \"re_full_n\": 397, \"re_cond_rho_sj\": 0.3004, \"re_cond_rho_fk\": 0.2374, \"re_cond_p_sj\": 2.25e-08, \"re_cond_p_fk\": 1.19e-05, \"re_cond_n\": 333, \"re_sj_beats_fk_full\": true, \"re_sj_beats_fk_cond\": true, \"re_rho_advantage\": 0.0146, \"re_sample_f1_mean\": 0.1977, \"re_sample_f1_std\": 0.3251, \"re_sample_f1_pct_zero\": 67.6, \"re_gold_empty_filtered\": 154, \"re_all_zero_filtered\": 64, \"parse_failures_stochastic\": 0, \"parse_failures_greedy\": 0, \"total_stochastic_samples\": 4408, \"total_greedy\": 551, \"verdict\": \"FAIL\", \"verdict_reason\": \"RE full rho_sj=0.2367 < 0.40 threshold; strong signal exists but below PASS bar\"}}, \"mvp_pilot_001\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T07:39:16.313Z\", \"updated_at\": \"2026-05-14T08:05:34.348Z\", \"spec\": {\"hypothesis\": \"Structural self-consistency (soft Jaccard) correlates with per-instance F1 better than surface Fleiss Kappa on fine-tuned Qwen3-8B SciERC\", \"model_name\": \"qwen3-8b-scierc-merged\", \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/data/test.jsonl\", \"data_count\": 551, \"server\": \"autodl-5090\", \"seed\": 42, \"parent\": \"ft_001\", \"method\": \"N=8 sampling T=1.0 + XGrammar + span realignment\", \"command\": \"CUDA_VISIBLE_DEVICES=0 python3 code/mvp_pilot.py\", \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen3-8b-scierc-merged\", \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/mvp_pilot_001.log\"}, \"conclusion\": \"negative\", \"completed_at\": \"2026-05-14T07:52:47.006Z\", \"metrics\": {\"ner_greedy_f1\": 0.611, \"ner_oracle_f1\": 0.78, \"ner_headroom\": 0.169, \"ner_fleiss_kappa_mean\": 0.2449, \"ner_soft_jaccard_mean\": 0.5041, \"ner_full_rho_sj\": 0.3616, \"ner_full_rho_fk\": 0.3515, \"ner_full_n\": 529, \"ner_cond_rho_sj\": 0.3688, \"ner_cond_rho_fk\": 0.3569, \"ner_cond_n\": 510, \"ner_sj_beats_fk_full\": true, \"ner_sj_beats_fk_cond\": true, \"ner_sample_f1_pct_zero\": 20.4, \"ner_gold_empty_filtered\": 22, \"ner_all_zero_filtered\": 19, \"re_greedy_f1\": 0.355, \"re_oracle_f1\": 0.572, \"re_headroom\": 0.217, \"re_fleiss_kappa_mean\": 0.0681, \"re_soft_jaccard_mean\": 0.3635, \"re_full_rho_sj\": 0.2535, \"re_full_rho_fk\": 0.2885, \"re_full_n\": 397, \"re_cond_rho_sj\": 0.3515, \"re_cond_rho_fk\": 0.3107, \"re_cond_n\": 320, \"re_sj_beats_fk_full\": false, \"re_sj_beats_fk_cond\": true, \"re_sample_f1_pct_zero\": 58.3, \"re_gold_empty_filtered\": 154, \"re_all_zero_filtered\": 77, \"parse_failures_stochastic\": 164, \"parse_failures_greedy\": 29, \"total_stochastic_samples\": 4408, \"total_greedy\": 551, \"verdict\": \"FAIL\", \"verdict_reason\": \"RE full rho_sj=0.2535 < 0.40; SJ does not beat FK on RE full set\"}}}, \"count\": 207, \"total\": 207, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.5655}}"
    }
  },
  "sourceToolAssistantUUID": "b55e3d16-2d0a-40f4-8d82-773b46262797",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/agent_5c567c58",
  "sessionId": "bb8bc777-37fb-4956-b48e-5e9c5a98dd73",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 19_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[CRON] 实验进程异常退出（失败），需要你诊断原因。 详情: Process exited without valid W&B metrics  - exp_id: exp_b1_scd_fewnerd_standard - project: struct_self_consist_ie - server: autodl-5090-b - log_path: /root/autodl-tmp/…",
  "leafUuid": "bfcc38da-b691-47e2-a881-f55046cc9c0b",
  "sessionId": "bb8bc777-37fb-4956-b48e-5e9c5a98dd73"
}
```

---

### Runtime record

_source line 20_

```json
{
  "type": "ai-title",
  "aiTitle": "Diagnose experiment process exit failure",
  "sessionId": "bb8bc777-37fb-4956-b48e-5e9c5a98dd73"
}
```

---

### Tool result

_source line 21 · 2026-05-20T19:14:16.220Z_

<details><summary>↩ Tool result · `toolu_01PUFoM8no9CUjf1JtoJPpYz`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"reconciled\": 4, \"results\": [{\"exp_id\": \"exp_qwen25_32b_fewnerd\", \"success\": true, \"actions\": [\"Job still running (pid=804438)\"]}, {\"exp_id\": \"exp_b1_scd_threshold_ablation\", \"success\": true, \"actions\": [\"Job still running (pid=205991)\"]}, {\"exp_id\": \"exp_tlow_fewnerd_inference\", \"success\": true, \"actions\": [\"Job still running (pid=221493)\"]}, {\"exp_id\": \"exp_14b_inference_fewnerd\", \"success\": true, \"actions\": [\"Job still running (pid=217960)\"]}]}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2ee4cc02-5392-4ec7-9ef3-65ca58894e0e",
  "isSidechain": false,
  "promptId": "d2210c4d-d5b9-450f-8450-2f1ffe6e0ccd",
  "type": "user",
  "uuid": "28f39a89-ab47-47c4-9cf4-89fd61089721",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"reconciled\\\": 4, \\\"results\\\": [{\\\"exp_id\\\": \\\"exp_qwen25_32b_fewnerd\\\", \\\"success\\\": true, \\\"actions\\\": [\\\"Job still running (pid=804438)\\\"]}, {\\\"exp_id\\\": \\\"exp_b1_scd_threshold_ablation\\\", \\\"success\\\": true, \\\"actions\\\": [\\\"Job still running (pid=205991)\\\"]}, {\\\"exp_id\\\": \\\"exp_tlow_fewnerd_inference\\\", \\\"success\\\": true, \\\"actions\\\": [\\\"Job still running (pid=221493)\\\"]}, {\\\"exp_id\\\": \\\"exp_14b_inference_fewnerd\\\", \\\"success\\\": true, \\\"actions\\\": [\\\"Job still running (pid=217960)\\\"]}]}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"reconciled\": 4, \"results\": [{\"exp_id\": \"exp_qwen25_32b_fewnerd\", \"success\": true, \"actions\": [\"Job still running (pid=804438)\"]}, {\"exp_id\": \"exp_b1_scd_threshold_ablation\", \"success\": true, \"actions\": [\"Job still running (pid=205991)\"]}, {\"exp_id\": \"exp_tlow_fewnerd_inference\", \"success\": true, \"actions\": [\"Job still running (pid=221493)\"]}, {\"exp_id\": \"exp_14b_inference_fewnerd\", \"success\": true, \"actions\": [\"Job still running (pid=217960)\"]}]}, \"error\": null, \"metadata\": {}}"
    }
  },
  "sourceToolAssistantUUID": "2ee4cc02-5392-4ec7-9ef3-65ca58894e0e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/agent_5c567c58",
  "sessionId": "bb8bc777-37fb-4956-b48e-5e9c5a98dd73",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-20T19:14:16.232Z_

<details><summary>↩ Tool result · `toolu_015KYTQjUHKsrfh3icLTC45i`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/report.md\", \"content\": \"&lt;!-- AUTO-FACTS-BEGIN (generated 2026-05-20T19:13:37Z; do not edit — regenerated by auto_build_report_facts) -->\\n## 📊 当前状态（auto-derived from registry）\\n\\n**总计**: 206 个实验 — DONE 182, PENDING 2, PREPARING 16, QUEUED 1, RUNNING 5\\n**DONE 分布**: failed 6, killed 30, negative 41, success 105\\n\\n### GPU 占用\\n- **分配**: 12 张 — autodl-5090:cuda:0, autodl-5090:cuda:1, autodl-5090:cuda:2, autodl-5090:cuda:3, autodl-5090-b:cuda:0, autodl-5090-b:cuda:1, autodl-5090-b:cuda:2, autodl-5090-b:cuda:3, autodl-5090-c:cuda:0, autodl-5090-c:cuda:1, autodl-5090-c:cuda:2, autodl-5090-c:cuda:3\\n- **实际运行**: 5 张 — autodl-5090:cuda:0(exp_qwen25_32b_fewnerd), autodl-5090:cuda:1(exp_qwen25_32b_fewnerd), autodl-5090:cuda:2(exp_qwen25_32b_fewnerd), autodl-5090:cuda:3(exp_qwen25_32b_fewnerd), autodl-5090-c:cuda:2(exp_tlow_fewnerd_inference)\\n- **空闲（分配了没跑）**: autodl-5090-b:cuda:1, autodl-5090-b:cuda:2, autodl-5090-c:cuda:1, autodl-5090-c:cuda:3\\n\\n### 💾 磁盘余量\\n- **autodl-5090**:\\n  - `/autodl-pub`: 9.0T/14T 可用（已用 36%）\\n  - `/autodl-pub/data`: 5.7T/10T 可用（已用 44%）\\n  - `/usr/bin/nvidia-smi`: 813G/879G 可用（已用 3%）\\n- **autodl-5090-b**:\\n  - `/autodl-pub`: 11T/14T 可用（已用 24%）\\n  - `/autodl-pub/data`: 5.7T/10T 可用（已用 44%）\\n  - `/usr/bin/nvidia-smi`: 427G/879G 可用（已用 49%）\\n- **autodl-5090-c**:\\n  - `/autodl-pub`: 7.0T/14T 可用（已用 50%）\\n  - `/autodl-pub/data`: 18T/20T 可用（已用 9%）\\n  - `/usr/bin/nvidia-smi`: 813G/879G 可用（已用 3%）\\n\\n### 🏃 RUNNING\\n| exp_id | server | gpu | pid | log |\\n|--------|--------|-----|-----|-----|\\n| `exp_qwen25_32b_fewnerd` | autodl-5090 | cuda:0,cuda:1,cuda:2,cuda:3 | 804438 | `…truct_self_consist_ie/logs/train_qwen25_32b_fewnerd_s42.log` |\\n| `exp_b1_scd_threshold_ablation` | autodl-5090-b | ? | ? | `—` |\\n| `exp_14b_inference_fewnerd` | autodl-5090-c | ? | 217960 | `—` |\\n| `exp_e_theta_adaptive` | local-cpu | ? | ? | `—` |\\n| `exp_tlow_fewnerd_inference` | autodl-5090-c | cuda:2 | 221493 | `…/struct_self_consist_ie/output/exp_tlow_fewnerd_t05_s42.log` |\\n\\n### 📌 最近完成 (top 5)\\n- `exp_b1_scd_fewnerd_standard` [failed] — 2026-05-20T19:13:31 — process dead 5× with no sentinel/W&B — auto-resolved as failed\\n- `exp_b1_scd_fewnerd_curriculum_q` [failed] — 2026-05-20T19:04:33 — RETRACTED: cron false positive — training completed successfully (4706/4706 step\\n- `exp_cross_model_consistency` [success] — 2026-05-20T19:03:33\\n- `exp_backup1_het_temp` [negative] — 2026-05-20T18:15:37\\n- `exp_asb_adaptive_budget` [success] — 2026-05-20T18:14:15\\n\\n### 🔴 最近失败原因 (top 3)\\n- `exp_b1_scd_fewnerd_standard`: process dead 5× with no sentinel/W&B — auto-resolved as failed\\n- `exp_b1_scd_fewnerd_curriculum_q`: RETRACTED: cron false positive — training completed successfully (4706/4706 steps, loss=0.023). Original: process dead 5× with no sentinel/W&B\\n\\n&lt;!-- AUTO-FACTS-END -->\\n\\n---\\n\\n# Handover — 2026-05-20\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\\n|--------|------|------|---------|-----|\\n| exp_14b_inference_fewnerd | 14B Qwen2.5 inference on FewNERD (N∈{1,2,4,8,16}): primary dataset should show oracle scaling law F1(N)=a-b*N^(-c) consistent at 14B scale, filling the scaling curve between 7B and 32B. | — | — | — |\\n| exp_tlow_fewnerd_inference | Lower temperature (T=0.5) sampling on FewNERD produces less diverse but higher-quality samples that, when combined with T=1.0 samples in heterogeneous-temperature selection, improve self-consistency-based quality estimation compared to single-temperature baselines. | — | — | — |\\n| exp_e_theta_adaptive | Threshold-Adaptive SC: N inverse scaling (D191) proves θ choice determines scaling direction. A learned θ predictor (input: degeneracy_level, lp_variance, N, dataset, model) can select per-instance optimal θ, closing the gap between fixed θ=0.5 and oracle θ. Leave-one-config-out CV on 16 configs from existing N=8/16 data. 5 variants: LogReg/MLP × feature subsets + degeneracy-only baseline. | — | — | — |\\n\\n## 待处理\\n- exp_spider_sc_pilot: SC diagnostic cascade (degeneracy, LP-quality gap, agreement-correctness correlation) validated on NER structured generation will also manifest in SQL structured generation with Qwen2.5-7B-Instruct on Spider, demonstrating cross-task universality of the diagnostic framework.（等待人工审批）\\n- exp_b1_scd: Self-Consistency Distillation via theta2n construction pseudo-labels can teach Qwen3-8B-FT to internalize SC benefits: after iterative SCD (M0→M1→M2→M3), greedy F1 should approach N=8 construction F1 (FewNERD target: 0.764 vs current greedy 0.748). CoNLL serves as negative control (construction Δ=-0.4pp, SCD should not help). Transductive setting: pseudo-labels from test set SC outputs.（等待人工审批）\\n- exp_a3_ace05_re: Cross-task universality: SC diagnostic cascade on ACE05 Relation Extraction. Closest extension to NER—same structured prediction paradigm, different output structure (entity pairs + relation types). Qwen2.5-7B-Instruct few-shot prompt. If correlation-selection gap exists for RE, the framework covers multiple IE sub-tasks.（排队等待 GPU）\\n- eval_scd_fewnerd_fallback（准备中）\\n- exp_b_frontier_sc_fewnerd: The correlation-selection gap in structured self-consistency persists with frontier models (GPT-5.5, Claude Opus 4.6), indicating it is a fundamental limitation of frequency-based SC for structured prediction rather than a capability issue of smaller models.（准备中）\\n- exp_a2_humaneval_sc: SC failure modes (degeneracy, false agreement) generalize from NER to code generation despite deterministic verification — majority voting on HumanEval will show limited gains over greedy when degeneracy is high, paralleling NER findings.（准备中）\\n- exp_a1_spider_sql_sc: Cross-task universality: SC diagnostic cascade (degeneracy, LP-quality gap, agreement-correctness correlation) applies to SQL structured generation on Spider. Qwen2.5-7B-Instruct base model, 200 dev examples, N=8 T=1.0, execution accuracy evaluation. If F1-F4 failure modes exist in SQL, the framework generalizes beyond NER.（准备中）\\n- exp_14b_inference_conll: 14B Qwen2.5 inference on CoNLL (N∈{1,2,4,8,16}): high-resource dataset should show higher degeneracy at 14B scale, consistent with 7B pattern where construction gain is negative.（准备中）\\n- exp_b2_v4_inverse_frequency: Inverse-frequency weighting of entity features (agreement_count, vc, sj normalized by log(1+type_freq)) improves cross-domain generalization by reducing dominance of high-frequency entity types. Two variants: A) replace original features, B) augment as additional features.（准备中）\\n- exp_b2_v3_domain_invariant: Removing domain-specific features (dataset_enc, entity_type distributions) forces the verifier to rely on domain-invariant signals, improving cross-domain generalization at the cost of some discriminative power. If LGB AUC improves on held-out domains, domain features were causing negative transfer.（准备中）\\n- …另有 9 项\\n\\n## 近期结论\\n- **exp_b1_scd_fewnerd_standard** (failed): Standard Self-Consistency Distillation on FewNERD: fine-tune Qwen3-8B-FT with theta2n construction pseudo-labels (32,565 instances) mixed 1:1 with gold data. Greedy F1 after SCD should approach N=8 construction F1 (0.764 vs current 0.748). Transductive setting: pseudo-labels from test set SC outputs.\\n- **exp_b1_scd_fewnerd_curriculum_q** (failed): Q variant SCD with curriculum ordering: use B2 entity verifier confidence to stratify pseudo-labels (conf>0.8→Round1, 0.5-0.8→Round2, conf<0.5→discard). Curriculum by verifier confidence improves SCD convergence and final greedy F1 vs standard flat SCD on FewNERD.\\n- **exp_cross_model_consistency** (success): Cross-model entity construction (mixing Qwen and LLaMA outputs) produces higher-quality entity spans than single-model construction, because inter-model agreement filters out model-specific hallucinations while preserving genuinely supported entities.\\n\\n## 趋势\\n成功 105 / 负向 42 / 失败 6 / 共 183\\n\\n## 下一步\\n（无活跃 idea，请通过 ideas.md 添加）\\n\\n## 资源状态\\nautodl-5090: 空闲 cuda:0, cuda:1, cuda:2, cuda:3\\nautodl-5090-b: 空闲 cuda:0, cuda:1, cuda:2, cuda:3\\nautodl-5090-c: 空闲 cuda:0, cuda:1, cuda:2, cuda:3\\n\\n## 告警\\n- ft_002: 已被终止 — unknown\\n- mvp_pilot_002: 训练失败 — unknown\\n- exp_007_ner_llama: 已被终止 — unknown\\n- exp001_seed123: 已被终止 — unknown\\n- exp001_seed456: 已被终止 — unknown\\n- exp008_re_n16: 已被终止 — unknown\\n- exp_002_merge_conll2003: 已被终止 — unknown\\n- exp_001_n16_seed123_full: 已被终止 — unknown\\n- exp_001_n16_seed456_full: 已被终止 — unknown\\n- exp_008_re_n16_full: 已被终止 — unknown\\n- exp_001_seed42_v2_r1024: 已被终止 — unknown\\n- exp_001_seed123_v2_r1024: 已被终止 — unknown\\n- exp_001_seed456_v2_ner_r1024: 已被终止 — unknown\\n- exp_002_conll_n16_r1024: 已被终止 — unknown\\n- exp_007_llama_n16_r1024: 已被终止 — unknown\\n- exp_018_llama_scierc_seed456: 已被终止 — unknown\\n- exp_019_supervised_verifier: 已被终止 — unknown\\n- exp_lp_t07_scierc: 已被终止 — unknown\\n- exp_qwen3_4b_scierc_finetune: 已被终止 — unknown\\n- exp_freeform_seed789_v2: 训练失败 — unknown\\n- exp_qwen3_4b_scierc_finetune_v2: 训练失败 — unknown\\n- exp_qwen3_4b_scierc_finetune_v3: 训练失败 — unknown\\n- exp_qwen3_4b_conll_merge_inference_v2: 已被终止 — unknown\\n- exp_qwen3_4b_scierc_merge_inference: 已被终止 — unknown\\n- exp_tacred_re_benchmark: 已被终止 — unknown\\n- exp_vc_lp_cascade_selection: 已被终止 — unknown\\n- hidden_state_probe_conll_v2: 已被终止 — unknown\\n- hidden_state_probe_conll_full: 已被终止 — unknown\\n- dgs_pilot: 已被终止 — unknown\\n- mbr_pilot: 已被终止 — unknown\\n- exp_031_fewnerd_t12: 已被终止 — unknown\\n- exp_030_conll_t12: 已被终止 — unknown\\n- exp_b3_prompted_diversity: 已被终止 — unknown\\n- exp_b1_scd_fewnerd_standard: 训练失败 — unknown\\n- exp_b1_scd_fewnerd_curriculum_q: 训练失败 — unknown\\n- exp_14b_inference_scierc: 已被终止 — unknown\\n\", \"total_chars\": 9446, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "27a922c8-0ac4-483b-aa7f-23c30a739dbd",
  "isSidechain": false,
  "promptId": "d2210c4d-d5b9-450f-8450-2f1ffe6e0ccd",
  "type": "user",
  "uuid": "d63cd487-2de6-4bd0-9e28-151bb75cec60",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/report.md\\\", \\\"content\\\": \\\"&lt;!-- AUTO-FACTS-BEGIN (generated 2026-05-20T19:13:37Z; do not edit — regenerated by auto_build_report_facts) -->\\\\n## 📊 当前状态（auto-derived from registry）\\\\n\\\\n**总计**: 206 个实验 — DONE 182, PENDING 2, PREPARING 16, QUEUED 1, RUNNING 5\\\\n**DONE 分布**: failed 6, killed 30, negative 41, success 105\\\\n\\\\n### GPU 占用\\\\n- **分配**: 12 张 — autodl-5090:cuda:0, autodl-5090:cuda:1, autodl-5090:cuda:2, autodl-5090:cuda:3, autodl-5090-b:cuda:0, autodl-5090-b:cuda:1, autodl-5090-b:cuda:2, autodl-5090-b:cuda:3, autodl-5090-c:cuda:0, autodl-5090-c:cuda:1, autodl-5090-c:cuda:2, autodl-5090-c:cuda:3\\\\n- **实际运行**: 5 张 — autodl-5090:cuda:0(exp_qwen25_32b_fewnerd), autodl-5090:cuda:1(exp_qwen25_32b_fewnerd), autodl-5090:cuda:2(exp_qwen25_32b_fewnerd), autodl-5090:cuda:3(exp_qwen25_32b_fewnerd), autodl-5090-c:cuda:2(exp_tlow_fewnerd_inference)\\\\n- **空闲（分配了没跑）**: autodl-5090-b:cuda:1, autodl-5090-b:cuda:2, autodl-5090-c:cuda:1, autodl-5090-c:cuda:3\\\\n\\\\n### 💾 磁盘余量\\\\n- **autodl-5090**:\\\\n  - `/autodl-pub`: 9.0T/14T 可用（已用 36%）\\\\n  - `/autodl-pub/data`: 5.7T/10T 可用（已用 44%）\\\\n  - `/usr/bin/nvidia-smi`: 813G/879G 可用（已用 3%）\\\\n- **autodl-5090-b**:\\\\n  - `/autodl-pub`: 11T/14T 可用（已用 24%）\\\\n  - `/autodl-pub/data`: 5.7T/10T 可用（已用 44%）\\\\n  - `/usr/bin/nvidia-smi`: 427G/879G 可用（已用 49%）\\\\n- **autodl-5090-c**:\\\\n  - `/autodl-pub`: 7.0T/14T 可用（已用 50%）\\\\n  - `/autodl-pub/data`: 18T/20T 可用（已用 9%）\\\\n  - `/usr/bin/nvidia-smi`: 813G/879G 可用（已用 3%）\\\\n\\\\n### 🏃 RUNNING\\\\n| exp_id | server | gpu | pid | log |\\\\n|--------|--------|-----|-----|-----|\\\\n| `exp_qwen25_32b_fewnerd` | autodl-5090 | cuda:0,cuda:1,cuda:2,cuda:3 | 804438 | `…truct_self_consist_ie/logs/train_qwen25_32b_fewnerd_s42.log` |\\\\n| `exp_b1_scd_threshold_ablation` | autodl-5090-b | ? | ? | `—` |\\\\n| `exp_14b_inference_fewnerd` | autodl-5090-c | ? | 217960 | `—` |\\\\n| `exp_e_theta_adaptive` | local-cpu | ? | ? | `—` |\\\\n| `exp_tlow_fewnerd_inference` | autodl-5090-c | cuda:2 | 221493 | `…/struct_self_consist_ie/output/exp_tlow_fewnerd_t05_s42.log` |\\\\n\\\\n### 📌 最近完成 (top 5)\\\\n- `exp_b1_scd_fewnerd_standard` [failed] — 2026-05-20T19:13:31 — process dead 5× with no sentinel/W&B — auto-resolved as failed\\\\n- `exp_b1_scd_fewnerd_curriculum_q` [failed] — 2026-05-20T19:04:33 — RETRACTED: cron false positive — training completed successfully (4706/4706 step\\\\n- `exp_cross_model_consistency` [success] — 2026-05-20T19:03:33\\\\n- `exp_backup1_het_temp` [negative] — 2026-05-20T18:15:37\\\\n- `exp_asb_adaptive_budget` [success] — 2026-05-20T18:14:15\\\\n\\\\n### 🔴 最近失败原因 (top 3)\\\\n- `exp_b1_scd_fewnerd_standard`: process dead 5× with no sentinel/W&B — auto-resolved as failed\\\\n- `exp_b1_scd_fewnerd_curriculum_q`: RETRACTED: cron false positive — training completed successfully (4706/4706 steps, loss=0.023). Original: process dead 5× with no sentinel/W&B\\\\n\\\\n&lt;!-- AUTO-FACTS-END -->\\\\n\\\\n---\\\\n\\\\n# Handover — 2026-05-20\\\\n\\\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\\\n\\\\n## 运行中\\\\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\\\\n|--------|------|------|---------|-----|\\\\n| exp_14b_inference_fewnerd | 14B Qwen2.5 inference on FewNERD (N∈{1,2,4,8,16}): primary dataset should show oracle scaling law F1(N)=a-b*N^(-c) consistent at 14B scale, filling the scaling curve between 7B and 32B. | — | — | — |\\\\n| exp_tlow_fewnerd_inference | Lower temperature (T=0.5) sampling on FewNERD produces less diverse but higher-quality samples that, when combined with T=1.0 samples in heterogeneous-temperature selection, improve self-consistency-based quality estimation compared to single-temperature baselines. | — | — | — |\\\\n| exp_e_theta_adaptive | Threshold-Adaptive SC: N inverse scaling (D191) proves θ choice determines scaling direction. A learned θ predictor (input: degeneracy_level, lp_variance, N, dataset, model) can select per-instance optimal θ, closing the gap between fixed θ=0.5 and oracle θ. Leave-one-config-out CV on 16 configs from existing N=8/16 data. 5 variants: LogReg/MLP × feature subsets + degeneracy-only baseline. | — | — | — |\\\\n\\\\n## 待处理\\\\n- exp_spider_sc_pilot: SC diagnostic cascade (degeneracy, LP-quality gap, agreement-correctness correlation) validated on NER structured generation will also manifest in SQL structured generation with Qwen2.5-7B-Instruct on Spider, demonstrating cross-task universality of the diagnostic framework.（等待人工审批）\\\\n- exp_b1_scd: Self-Consistency Distillation via theta2n construction pseudo-labels can teach Qwen3-8B-FT to internalize SC benefits: after iterative SCD (M0→M1→M2→M3), greedy F1 should approach N=8 construction F1 (FewNERD target: 0.764 vs current greedy 0.748). CoNLL serves as negative control (construction Δ=-0.4pp, SCD should not help). Transductive setting: pseudo-labels from test set SC outputs.（等待人工审批）\\\\n- exp_a3_ace05_re: Cross-task universality: SC diagnostic cascade on ACE05 Relation Extraction. Closest extension to NER—same structured prediction paradigm, different output structure (entity pairs + relation types). Qwen2.5-7B-Instruct few-shot prompt. If correlation-selection gap exists for RE, the framework covers multiple IE sub-tasks.（排队等待 GPU）\\\\n- eval_scd_fewnerd_fallback（准备中）\\\\n- exp_b_frontier_sc_fewnerd: The correlation-selection gap in structured self-consistency persists with frontier models (GPT-5.5, Claude Opus 4.6), indicating it is a fundamental limitation of frequency-based SC for structured prediction rather than a capability issue of smaller models.（准备中）\\\\n- exp_a2_humaneval_sc: SC failure modes (degeneracy, false agreement) generalize from NER to code generation despite deterministic verification — majority voting on HumanEval will show limited gains over greedy when degeneracy is high, paralleling NER findings.（准备中）\\\\n- exp_a1_spider_sql_sc: Cross-task universality: SC diagnostic cascade (degeneracy, LP-quality gap, agreement-correctness correlation) applies to SQL structured generation on Spider. Qwen2.5-7B-Instruct base model, 200 dev examples, N=8 T=1.0, execution accuracy evaluation. If F1-F4 failure modes exist in SQL, the framework generalizes beyond NER.（准备中）\\\\n- exp_14b_inference_conll: 14B Qwen2.5 inference on CoNLL (N∈{1,2,4,8,16}): high-resource dataset should show higher degeneracy at 14B scale, consistent with 7B pattern where construction gain is negative.（准备中）\\\\n- exp_b2_v4_inverse_frequency: Inverse-frequency weighting of entity features (agreement_count, vc, sj normalized by log(1+type_freq)) improves cross-domain generalization by reducing dominance of high-frequency entity types. Two variants: A) replace original features, B) augment as additional features.（准备中）\\\\n- exp_b2_v3_domain_invariant: Removing domain-specific features (dataset_enc, entity_type distributions) forces the verifier to rely on domain-invariant signals, improving cross-domain generalization at the cost of some discriminative power. If LGB AUC improves on held-out domains, domain features were causing negative transfer.（准备中）\\\\n- …另有 9 项\\\\n\\\\n## 近期结论\\\\n- **exp_b1_scd_fewnerd_standard** (failed): Standard Self-Consistency Distillation on FewNERD: fine-tune Qwen3-8B-FT with theta2n construction pseudo-labels (32,565 instances) mixed 1:1 with gold data. Greedy F1 after SCD should approach N=8 construction F1 (0.764 vs current 0.748). Transductive setting: pseudo-labels from test set SC outputs.\\\\n- **exp_b1_scd_fewnerd_curriculum_q** (failed): Q variant SCD with curriculum ordering: use B2 entity verifier confidence to stratify pseudo-labels (conf>0.8→Round1, 0.5-0.8→Round2, conf<0.5→discard). Curriculum by verifier confidence improves SCD convergence and final greedy F1 vs standard flat SCD on FewNERD.\\\\n- **exp_cross_model_consistency** (success): Cross-model entity construction (mixing Qwen and LLaMA outputs) produces higher-quality entity spans than single-model construction, because inter-model agreement filters out model-specific hallucinations while preserving genuinely supported entities.\\\\n\\\\n## 趋势\\\\n成功 105 / 负向 42 / 失败 6 / 共 183\\\\n\\\\n## 下一步\\\\n（无活跃 idea，请通过 ideas.md 添加）\\\\n\\\\n## 资源状态\\\\nautodl-5090: 空闲 cuda:0, cuda:1, cuda:2, cuda:3\\\\nautodl-5090-b: 空闲 cuda:0, cuda:1, cuda:2, cuda:3\\\\nautodl-5090-c: 空闲 cuda:0, cuda:1, cuda:2, cuda:3\\\\n\\\\n## 告警\\\\n- ft_002: 已被终止 — unknown\\\\n- mvp_pilot_002: 训练失败 — unknown\\\\n- exp_007_ner_llama: 已被终止 — unknown\\\\n- exp001_seed123: 已被终止 — unknown\\\\n- exp001_seed456: 已被终止 — unknown\\\\n- exp008_re_n16: 已被终止 — unknown\\\\n- exp_002_merge_conll2003: 已被终止 — unknown\\\\n- exp_001_n16_seed123_full: 已被终止 — unknown\\\\n- exp_001_n16_seed456_full: 已被终止 — unknown\\\\n- exp_008_re_n16_full: 已被终止 — unknown\\\\n- exp_001_seed42_v2_r1024: 已被终止 — unknown\\\\n- exp_001_seed123_v2_r1024: 已被终止 — unknown\\\\n- exp_001_seed456_v2_ner_r1024: 已被终止 — unknown\\\\n- exp_002_conll_n16_r1024: 已被终止 — unknown\\\\n- exp_007_llama_n16_r1024: 已被终止 — unknown\\\\n- exp_018_llama_scierc_seed456: 已被终止 — unknown\\\\n- exp_019_supervised_verifier: 已被终止 — unknown\\\\n- exp_lp_t07_scierc: 已被终止 — unknown\\\\n- exp_qwen3_4b_scierc_finetune: 已被终止 — unknown\\\\n- exp_freeform_seed789_v2: 训练失败 — unknown\\\\n- exp_qwen3_4b_scierc_finetune_v2: 训练失败 — unknown\\\\n- exp_qwen3_4b_scierc_finetune_v3: 训练失败 — unknown\\\\n- exp_qwen3_4b_conll_merge_inference_v2: 已被终止 — unknown\\\\n- exp_qwen3_4b_scierc_merge_inference: 已被终止 — unknown\\\\n- exp_tacred_re_benchmark: 已被终止 — unknown\\\\n- exp_vc_lp_cascade_selection: 已被终止 — unknown\\\\n- hidden_state_probe_conll_v2: 已被终止 — unknown\\\\n- hidden_state_probe_conll_full: 已被终止 — unknown\\\\n- dgs_pilot: 已被终止 — unknown\\\\n- mbr_pilot: 已被终止 — unknown\\\\n- exp_031_fewnerd_t12: 已被终止 — unknown\\\\n- exp_030_conll_t12: 已被终止 — unknown\\\\n- exp_b3_prompted_diversity: 已被终止 — unknown\\\\n- exp_b1_scd_fewnerd_standard: 训练失败 — unknown\\\\n- exp_b1_scd_fewnerd_curriculum_q: 训练失败 — unknown\\\\n- exp_14b_inference_scierc: 已被终止 — unknown\\\\n\\\", \\\"total_chars\\\": 9446, \\\"truncated\\\": false}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/report.md\", \"content\": \"&lt;!-- AUTO-FACTS-BEGIN (generated 2026-05-20T19:13:37Z; do not edit — regenerated by auto_build_report_facts) -->\\n## 📊 当前状态（auto-derived from registry）\\n\\n**总计**: 206 个实验 — DONE 182, PENDING 2, PREPARING 16, QUEUED 1, RUNNING 5\\n**DONE 分布**: failed 6, killed 30, negative 41, success 105\\n\\n### GPU 占用\\n- **分配**: 12 张 — autodl-5090:cuda:0, autodl-5090:cuda:1, autodl-5090:cuda:2, autodl-5090:cuda:3, autodl-5090-b:cuda:0, autodl-5090-b:cuda:1, autodl-5090-b:cuda:2, autodl-5090-b:cuda:3, autodl-5090-c:cuda:0, autodl-5090-c:cuda:1, autodl-5090-c:cuda:2, autodl-5090-c:cuda:3\\n- **实际运行**: 5 张 — autodl-5090:cuda:0(exp_qwen25_32b_fewnerd), autodl-5090:cuda:1(exp_qwen25_32b_fewnerd), autodl-5090:cuda:2(exp_qwen25_32b_fewnerd), autodl-5090:cuda:3(exp_qwen25_32b_fewnerd), autodl-5090-c:cuda:2(exp_tlow_fewnerd_inference)\\n- **空闲（分配了没跑）**: autodl-5090-b:cuda:1, autodl-5090-b:cuda:2, autodl-5090-c:cuda:1, autodl-5090-c:cuda:3\\n\\n### 💾 磁盘余量\\n- **autodl-5090**:\\n  - `/autodl-pub`: 9.0T/14T 可用（已用 36%）\\n  - `/autodl-pub/data`: 5.7T/10T 可用（已用 44%）\\n  - `/usr/bin/nvidia-smi`: 813G/879G 可用（已用 3%）\\n- **autodl-5090-b**:\\n  - `/autodl-pub`: 11T/14T 可用（已用 24%）\\n  - `/autodl-pub/data`: 5.7T/10T 可用（已用 44%）\\n  - `/usr/bin/nvidia-smi`: 427G/879G 可用（已用 49%）\\n- **autodl-5090-c**:\\n  - `/autodl-pub`: 7.0T/14T 可用（已用 50%）\\n  - `/autodl-pub/data`: 18T/20T 可用（已用 9%）\\n  - `/usr/bin/nvidia-smi`: 813G/879G 可用（已用 3%）\\n\\n### 🏃 RUNNING\\n| exp_id | server | gpu | pid | log |\\n|--------|--------|-----|-----|-----|\\n| `exp_qwen25_32b_fewnerd` | autodl-5090 | cuda:0,cuda:1,cuda:2,cuda:3 | 804438 | `…truct_self_consist_ie/logs/train_qwen25_32b_fewnerd_s42.log` |\\n| `exp_b1_scd_threshold_ablation` | autodl-5090-b | ? | ? | `—` |\\n| `exp_14b_inference_fewnerd` | autodl-5090-c | ? | 217960 | `—` |\\n| `exp_e_theta_adaptive` | local-cpu | ? | ? | `—` |\\n| `exp_tlow_fewnerd_inference` | autodl-5090-c | cuda:2 | 221493 | `…/struct_self_consist_ie/output/exp_tlow_fewnerd_t05_s42.log` |\\n\\n### 📌 最近完成 (top 5)\\n- `exp_b1_scd_fewnerd_standard` [failed] — 2026-05-20T19:13:31 — process dead 5× with no sentinel/W&B — auto-resolved as failed\\n- `exp_b1_scd_fewnerd_curriculum_q` [failed] — 2026-05-20T19:04:33 — RETRACTED: cron false positive — training completed successfully (4706/4706 step\\n- `exp_cross_model_consistency` [success] — 2026-05-20T19:03:33\\n- `exp_backup1_het_temp` [negative] — 2026-05-20T18:15:37\\n- `exp_asb_adaptive_budget` [success] — 2026-05-20T18:14:15\\n\\n### 🔴 最近失败原因 (top 3)\\n- `exp_b1_scd_fewnerd_standard`: process dead 5× with no sentinel/W&B — auto-resolved as failed\\n- `exp_b1_scd_fewnerd_curriculum_q`: RETRACTED: cron false positive — training completed successfully (4706/4706 steps, loss=0.023). Original: process dead 5× with no sentinel/W&B\\n\\n&lt;!-- AUTO-FACTS-END -->\\n\\n---\\n\\n# Handover — 2026-05-20\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\\n|--------|------|------|---------|-----|\\n| exp_14b_inference_fewnerd | 14B Qwen2.5 inference on FewNERD (N∈{1,2,4,8,16}): primary dataset should show oracle scaling law F1(N)=a-b*N^(-c) consistent at 14B scale, filling the scaling curve between 7B and 32B. | — | — | — |\\n| exp_tlow_fewnerd_inference | Lower temperature (T=0.5) sampling on FewNERD produces less diverse but higher-quality samples that, when combined with T=1.0 samples in heterogeneous-temperature selection, improve self-consistency-based quality estimation compared to single-temperature baselines. | — | — | — |\\n| exp_e_theta_adaptive | Threshold-Adaptive SC: N inverse scaling (D191) proves θ choice determines scaling direction. A learned θ predictor (input: degeneracy_level, lp_variance, N, dataset, model) can select per-instance optimal θ, closing the gap between fixed θ=0.5 and oracle θ. Leave-one-config-out CV on 16 configs from existing N=8/16 data. 5 variants: LogReg/MLP × feature subsets + degeneracy-only baseline. | — | — | — |\\n\\n## 待处理\\n- exp_spider_sc_pilot: SC diagnostic cascade (degeneracy, LP-quality gap, agreement-correctness correlation) validated on NER structured generation will also manifest in SQL structured generation with Qwen2.5-7B-Instruct on Spider, demonstrating cross-task universality of the diagnostic framework.（等待人工审批）\\n- exp_b1_scd: Self-Consistency Distillation via theta2n construction pseudo-labels can teach Qwen3-8B-FT to internalize SC benefits: after iterative SCD (M0→M1→M2→M3), greedy F1 should approach N=8 construction F1 (FewNERD target: 0.764 vs current greedy 0.748). CoNLL serves as negative control (construction Δ=-0.4pp, SCD should not help). Transductive setting: pseudo-labels from test set SC outputs.（等待人工审批）\\n- exp_a3_ace05_re: Cross-task universality: SC diagnostic cascade on ACE05 Relation Extraction. Closest extension to NER—same structured prediction paradigm, different output structure (entity pairs + relation types). Qwen2.5-7B-Instruct few-shot prompt. If correlation-selection gap exists for RE, the framework covers multiple IE sub-tasks.（排队等待 GPU）\\n- eval_scd_fewnerd_fallback（准备中）\\n- exp_b_frontier_sc_fewnerd: The correlation-selection gap in structured self-consistency persists with frontier models (GPT-5.5, Claude Opus 4.6), indicating it is a fundamental limitation of frequency-based SC for structured prediction rather than a capability issue of smaller models.（准备中）\\n- exp_a2_humaneval_sc: SC failure modes (degeneracy, false agreement) generalize from NER to code generation despite deterministic verification — majority voting on HumanEval will show limited gains over greedy when degeneracy is high, paralleling NER findings.（准备中）\\n- exp_a1_spider_sql_sc: Cross-task universality: SC diagnostic cascade (degeneracy, LP-quality gap, agreement-correctness correlation) applies to SQL structured generation on Spider. Qwen2.5-7B-Instruct base model, 200 dev examples, N=8 T=1.0, execution accuracy evaluation. If F1-F4 failure modes exist in SQL, the framework generalizes beyond NER.（准备中）\\n- exp_14b_inference_conll: 14B Qwen2.5 inference on CoNLL (N∈{1,2,4,8,16}): high-resource dataset should show higher degeneracy at 14B scale, consistent with 7B pattern where construction gain is negative.（准备中）\\n- exp_b2_v4_inverse_frequency: Inverse-frequency weighting of entity features (agreement_count, vc, sj normalized by log(1+type_freq)) improves cross-domain generalization by reducing dominance of high-frequency entity types. Two variants: A) replace original features, B) augment as additional features.（准备中）\\n- exp_b2_v3_domain_invariant: Removing domain-specific features (dataset_enc, entity_type distributions) forces the verifier to rely on domain-invariant signals, improving cross-domain generalization at the cost of some discriminative power. If LGB AUC improves on held-out domains, domain features were causing negative transfer.（准备中）\\n- …另有 9 项\\n\\n## 近期结论\\n- **exp_b1_scd_fewnerd_standard** (failed): Standard Self-Consistency Distillation on FewNERD: fine-tune Qwen3-8B-FT with theta2n construction pseudo-labels (32,565 instances) mixed 1:1 with gold data. Greedy F1 after SCD should approach N=8 construction F1 (0.764 vs current 0.748). Transductive setting: pseudo-labels from test set SC outputs.\\n- **exp_b1_scd_fewnerd_curriculum_q** (failed): Q variant SCD with curriculum ordering: use B2 entity verifier confidence to stratify pseudo-labels (conf>0.8→Round1, 0.5-0.8→Round2, conf<0.5→discard). Curriculum by verifier confidence improves SCD convergence and final greedy F1 vs standard flat SCD on FewNERD.\\n- **exp_cross_model_consistency** (success): Cross-model entity construction (mixing Qwen and LLaMA outputs) produces higher-quality entity spans than single-model construction, because inter-model agreement filters out model-specific hallucinations while preserving genuinely supported entities.\\n\\n## 趋势\\n成功 105 / 负向 42 / 失败 6 / 共 183\\n\\n## 下一步\\n（无活跃 idea，请通过 ideas.md 添加）\\n\\n## 资源状态\\nautodl-5090: 空闲 cuda:0, cuda:1, cuda:2, cuda:3\\nautodl-5090-b: 空闲 cuda:0, cuda:1, cuda:2, cuda:3\\nautodl-5090-c: 空闲 cuda:0, cuda:1, cuda:2, cuda:3\\n\\n## 告警\\n- ft_002: 已被终止 — unknown\\n- mvp_pilot_002: 训练失败 — unknown\\n- exp_007_ner_llama: 已被终止 — unknown\\n- exp001_seed123: 已被终止 — unknown\\n- exp001_seed456: 已被终止 — unknown\\n- exp008_re_n16: 已被终止 — unknown\\n- exp_002_merge_conll2003: 已被终止 — unknown\\n- exp_001_n16_seed123_full: 已被终止 — unknown\\n- exp_001_n16_seed456_full: 已被终止 — unknown\\n- exp_008_re_n16_full: 已被终止 — unknown\\n- exp_001_seed42_v2_r1024: 已被终止 — unknown\\n- exp_001_seed123_v2_r1024: 已被终止 — unknown\\n- exp_001_seed456_v2_ner_r1024: 已被终止 — unknown\\n- exp_002_conll_n16_r1024: 已被终止 — unknown\\n- exp_007_llama_n16_r1024: 已被终止 — unknown\\n- exp_018_llama_scierc_seed456: 已被终止 — unknown\\n- exp_019_supervised_verifier: 已被终止 — unknown\\n- exp_lp_t07_scierc: 已被终止 — unknown\\n- exp_qwen3_4b_scierc_finetune: 已被终止 — unknown\\n- exp_freeform_seed789_v2: 训练失败 — unknown\\n- exp_qwen3_4b_scierc_finetune_v2: 训练失败 — unknown\\n- exp_qwen3_4b_scierc_finetune_v3: 训练失败 — unknown\\n- exp_qwen3_4b_conll_merge_inference_v2: 已被终止 — unknown\\n- exp_qwen3_4b_scierc_merge_inference: 已被终止 — unknown\\n- exp_tacred_re_benchmark: 已被终止 — unknown\\n- exp_vc_lp_cascade_selection: 已被终止 — unknown\\n- hidden_state_probe_conll_v2: 已被终止 — unknown\\n- hidden_state_probe_conll_full: 已被终止 — unknown\\n- dgs_pilot: 已被终止 — unknown\\n- mbr_pilot: 已被终止 — unknown\\n- exp_031_fewnerd_t12: 已被终止 — unknown\\n- exp_030_conll_t12: 已被终止 — unknown\\n- exp_b3_prompted_diversity: 已被终止 — unknown\\n- exp_b1_scd_fewnerd_standard: 训练失败 — unknown\\n- exp_b1_scd_fewnerd_curriculum_q: 训练失败 — unknown\\n- exp_14b_inference_scierc: 已被终止 — unknown\\n\", \"total_chars\": 9446, \"truncated\": false}, \"error\": null, \"metadata\": {}}"
    }
  },
  "sourceToolAssistantUUID": "27a922c8-0ac4-483b-aa7f-23c30a739dbd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/agent_5c567c58",
  "sessionId": "bb8bc777-37fb-4956-b48e-5e9c5a98dd73",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-20T19:14:16.248Z_

<details><summary>↩ Tool result · `toolu_01TnwaHpTN6F9pwK748rTHDt`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/ROADMAP.md\", \"content\": \"# struct_self_consist_ie — Research Dashboard\\n\\n> 最后更新: 2026-05-20 14:43 UTC | 更新原因: R26 3.5/3.0 — dual-track sprint (writing v3 + method E_θ/ESJ), Pre-Review Gate Step 6\\n\\n## 核心方向\\n**Self-Consistency for NER: Ceiling-Gap Diagnostic → Prescriptive Framework**。QE vs selection 正交分解 + correlation-selection gap (two-tier) + threshold-adaptive SC + entity-level self-judgment。详见 paper_framing.md。\\n\\n## 当前阶段\\n**🔴 Writing v3 + Method Sprint (R26 → R27)**\\nR26: 3.5/3.0 = avg 3.25。R2 新 attack: May 2025 EL4NER scoop + hobelsberger 疑似虚构 + entity construction overclaim。\\n策略: 双线并行 — Track A writing v3 (citation fix + scope tighten) + Track B method breakthrough (E_θ + ESJ)。\\n目标: v4 整合后 R27 → 4.0+ (Conference)\\n\\n## 审稿回溯\\n\\n**R25 (3.5/3.5)**: SYSTEMIC_A Framing Overclaim + SYSTEMIC_B Statistical Claim Strength → v2 修复全落地\\n**R26 (3.5/3.0)**: R1 认可 v2 修复; R2 新发现:\\n- Missing citations (EL4NER May 2025, Xie 2023 entity voting)\\n- hobelsberger2025systematic 疑似虚构 (integrity risk)\\n- Entity construction = MBR direct application, not novel method\\n- Unqualified \\\"first\\\" claims without \\\"for NER\\\" scope\\n\\n## Track A: Writing v3 (30-45 min, CPU)\\n- [ ] A1: Citation integrity — Semantic Scholar verify 96 entries, hobelsberger 重点 (Worker dispatched)\\n- [ ] A2: 补引 EL4NER + Xie 2023 + 4 others (Paper Agent, 依赖 A1)\\n- [ ] A3: grep \\\"first\\\" → all qualified to \\\"for NER\\\" (Worker dispatched)\\n- [ ] A4: Entity construction → MBR-grounded diagnostic ablation (Paper Agent)\\n\\n## Track B: Method Breakthrough\\n| 实验 | 类型 | 资源 | 状态 | ETA |\\n|------|------|------|------|-----|\\n| B1 SCD ×3 (std/fall/θ3) | GPU | 5090-b:0,1,3 | RUNNING | ~01:00 UTC 05-21 |\\n| E_θ Threshold-Adaptive SC ×5 | CPU | 5 Workers | 提交审批中 | +2-3h |\\n| ESJ Entity Self-Judgment | GPU | 5090-c:1 or 3 | 提交审批中 | +3-4h |\\n| 14B FewNERD inference | GPU | 5090-c:0 | RUNNING | +20-30h |\\n| 32B Qwen2.5 FT | GPU | 5090:0-3 | RUNNING 73% | ~06:30 UTC 05-21 |\\n\\n## Track C: Permanent Gate\\nPre-Review Gate 扩展到 6 步: +Step 6 Citation Integrity Check (Semantic Scholar API verify)\\n\\n## GPU 状态\\n- autodl-5090: 4× RTX 5090 → 32B 训练中\\n- autodl-5090-b: 4× RTX 5090 → GPU 0,1,3 B1 SCD; **GPU 2 空闲**\\n- autodl-5090-c: 4× RTX 5090 → GPU 0 14B inference; GPU 1,3 空闲 → ESJ 待分配; GPU 2 空闲\\n\\n## 锁定决策\\nTitle: diagnostic (无 \\\"Addressing\\\") | Ceiling-gap framing | MBR v3 | FewNERD primary | 8pp limit | Two-tier gap | Construction = diagnostic ablation (非 novel method) | §6 = Threshold Regime Analysis | Pre-Review Gate 6-step | R27 等 B1+E_θ 数据再提交\\n\\n## 关键决策日志\\n\\n| ID | 日期 | 摘要 | 关联实验 |\\n|----|------|------|----------|\\n| D204 | 2026-05-20 | 全局统一 micro-F1 口径；frontier SC 独立呈现不与 fine-tuned 并列 | exp_asb_adaptive_budget, exp_b_frontier_sc_fewnerd, exp_backup1_het_temp |\\n| D203 | 2026-05-20 | 目标从 4.0 升至 4.5：全面扩展 scope（cross-task universality  | exp_esj_entity_self_judgment, exp_mrsc_multi_round, exp_lsc_latent_sc |\\n| D202 | 2026-05-20 | ESJ negative 确认 entity-level self-judgment 全线失败（MR | exp_esj_entity_self_judgment, exp_mrsc_multi_round, exp_lsc_latent_sc |\\n| D201 | 2026-05-20 | Entity-level 修正路线（MRSC/LSC）全 negative，立即 pivot 到 s | exp_mrsc_multi_round, exp_lsc_latent_sc, exp_e_theta_adaptive |\\n| D200 | 2026-05-20 | E_θ V1 (Ridge) negative — degenerates to global θ= | exp_e_theta_adaptive |\\n| D199 | 2026-05-20 | D199: Reverse D198 conservative calibrations — LSC | — |\\n| D198 | 2026-05-20 | D198: Pivot to prescriptive framework — approve MR | — |\\n| D197 | 2026-05-20 | D197: R26 3.5/3.0 — 双线并行 (Track A writing v3 + Tra | — |\\n| D196 | 2026-05-20 | D196: Holm-Bonferroni dual reporting — per-family  | — |\\n| D195 | 2026-05-20 | D195: R25 Writing v2 Sprint — two-tier gap, Phase  | — |\\n\\n\", \"lines\": 64}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ec6489d0-e14d-46e8-8da8-6a580919bce9",
  "isSidechain": false,
  "promptId": "d2210c4d-d5b9-450f-8450-2f1ffe6e0ccd",
  "type": "user",
  "uuid": "aa0823c7-c961-4c0f-80db-f593feff7945",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/ROADMAP.md\\\", \\\"content\\\": \\\"# struct_self_consist_ie — Research Dashboard\\\\n\\\\n> 最后更新: 2026-05-20 14:43 UTC | 更新原因: R26 3.5/3.0 — dual-track sprint (writing v3 + method E_θ/ESJ), Pre-Review Gate Step 6\\\\n\\\\n## 核心方向\\\\n**Self-Consistency for NER: Ceiling-Gap Diagnostic → Prescriptive Framework**。QE vs selection 正交分解 + correlation-selection gap (two-tier) + threshold-adaptive SC + entity-level self-judgment。详见 paper_framing.md。\\\\n\\\\n## 当前阶段\\\\n**🔴 Writing v3 + Method Sprint (R26 → R27)**\\\\nR26: 3.5/3.0 = avg 3.25。R2 新 attack: May 2025 EL4NER scoop + hobelsberger 疑似虚构 + entity construction overclaim。\\\\n策略: 双线并行 — Track A writing v3 (citation fix + scope tighten) + Track B method breakthrough (E_θ + ESJ)。\\\\n目标: v4 整合后 R27 → 4.0+ (Conference)\\\\n\\\\n## 审稿回溯\\\\n\\\\n**R25 (3.5/3.5)**: SYSTEMIC_A Framing Overclaim + SYSTEMIC_B Statistical Claim Strength → v2 修复全落地\\\\n**R26 (3.5/3.0)**: R1 认可 v2 修复; R2 新发现:\\\\n- Missing citations (EL4NER May 2025, Xie 2023 entity voting)\\\\n- hobelsberger2025systematic 疑似虚构 (integrity risk)\\\\n- Entity construction = MBR direct application, not novel method\\\\n- Unqualified \\\\\\\"first\\\\\\\" claims without \\\\\\\"for NER\\\\\\\" scope\\\\n\\\\n## Track A: Writing v3 (30-45 min, CPU)\\\\n- [ ] A1: Citation integrity — Semantic Scholar verify 96 entries, hobelsberger 重点 (Worker dispatched)\\\\n- [ ] A2: 补引 EL4NER + Xie 2023 + 4 others (Paper Agent, 依赖 A1)\\\\n- [ ] A3: grep \\\\\\\"first\\\\\\\" → all qualified to \\\\\\\"for NER\\\\\\\" (Worker dispatched)\\\\n- [ ] A4: Entity construction → MBR-grounded diagnostic ablation (Paper Agent)\\\\n\\\\n## Track B: Method Breakthrough\\\\n| 实验 | 类型 | 资源 | 状态 | ETA |\\\\n|------|------|------|------|-----|\\\\n| B1 SCD ×3 (std/fall/θ3) | GPU | 5090-b:0,1,3 | RUNNING | ~01:00 UTC 05-21 |\\\\n| E_θ Threshold-Adaptive SC ×5 | CPU | 5 Workers | 提交审批中 | +2-3h |\\\\n| ESJ Entity Self-Judgment | GPU | 5090-c:1 or 3 | 提交审批中 | +3-4h |\\\\n| 14B FewNERD inference | GPU | 5090-c:0 | RUNNING | +20-30h |\\\\n| 32B Qwen2.5 FT | GPU | 5090:0-3 | RUNNING 73% | ~06:30 UTC 05-21 |\\\\n\\\\n## Track C: Permanent Gate\\\\nPre-Review Gate 扩展到 6 步: +Step 6 Citation Integrity Check (Semantic Scholar API verify)\\\\n\\\\n## GPU 状态\\\\n- autodl-5090: 4× RTX 5090 → 32B 训练中\\\\n- autodl-5090-b: 4× RTX 5090 → GPU 0,1,3 B1 SCD; **GPU 2 空闲**\\\\n- autodl-5090-c: 4× RTX 5090 → GPU 0 14B inference; GPU 1,3 空闲 → ESJ 待分配; GPU 2 空闲\\\\n\\\\n## 锁定决策\\\\nTitle: diagnostic (无 \\\\\\\"Addressing\\\\\\\") | Ceiling-gap framing | MBR v3 | FewNERD primary | 8pp limit | Two-tier gap | Construction = diagnostic ablation (非 novel method) | §6 = Threshold Regime Analysis | Pre-Review Gate 6-step | R27 等 B1+E_θ 数据再提交\\\\n\\\\n## 关键决策日志\\\\n\\\\n| ID | 日期 | 摘要 | 关联实验 |\\\\n|----|------|------|----------|\\\\n| D204 | 2026-05-20 | 全局统一 micro-F1 口径；frontier SC 独立呈现不与 fine-tuned 并列 | exp_asb_adaptive_budget, exp_b_frontier_sc_fewnerd, exp_backup1_het_temp |\\\\n| D203 | 2026-05-20 | 目标从 4.0 升至 4.5：全面扩展 scope（cross-task universality  | exp_esj_entity_self_judgment, exp_mrsc_multi_round, exp_lsc_latent_sc |\\\\n| D202 | 2026-05-20 | ESJ negative 确认 entity-level self-judgment 全线失败（MR | exp_esj_entity_self_judgment, exp_mrsc_multi_round, exp_lsc_latent_sc |\\\\n| D201 | 2026-05-20 | Entity-level 修正路线（MRSC/LSC）全 negative，立即 pivot 到 s | exp_mrsc_multi_round, exp_lsc_latent_sc, exp_e_theta_adaptive |\\\\n| D200 | 2026-05-20 | E_θ V1 (Ridge) negative — degenerates to global θ= | exp_e_theta_adaptive |\\\\n| D199 | 2026-05-20 | D199: Reverse D198 conservative calibrations — LSC | — |\\\\n| D198 | 2026-05-20 | D198: Pivot to prescriptive framework — approve MR | — |\\\\n| D197 | 2026-05-20 | D197: R26 3.5/3.0 — 双线并行 (Track A writing v3 + Tra | — |\\\\n| D196 | 2026-05-20 | D196: Holm-Bonferroni dual reporting — per-family  | — |\\\\n| D195 | 2026-05-20 | D195: R25 Writing v2 Sprint — two-tier gap, Phase  | — |\\\\n\\\\n\\\", \\\"lines\\\": 64}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/ROADMAP.md\", \"content\": \"# struct_self_consist_ie — Research Dashboard\\n\\n> 最后更新: 2026-05-20 14:43 UTC | 更新原因: R26 3.5/3.0 — dual-track sprint (writing v3 + method E_θ/ESJ), Pre-Review Gate Step 6\\n\\n## 核心方向\\n**Self-Consistency for NER: Ceiling-Gap Diagnostic → Prescriptive Framework**。QE vs selection 正交分解 + correlation-selection gap (two-tier) + threshold-adaptive SC + entity-level self-judgment。详见 paper_framing.md。\\n\\n## 当前阶段\\n**🔴 Writing v3 + Method Sprint (R26 → R27)**\\nR26: 3.5/3.0 = avg 3.25。R2 新 attack: May 2025 EL4NER scoop + hobelsberger 疑似虚构 + entity construction overclaim。\\n策略: 双线并行 — Track A writing v3 (citation fix + scope tighten) + Track B method breakthrough (E_θ + ESJ)。\\n目标: v4 整合后 R27 → 4.0+ (Conference)\\n\\n## 审稿回溯\\n\\n**R25 (3.5/3.5)**: SYSTEMIC_A Framing Overclaim + SYSTEMIC_B Statistical Claim Strength → v2 修复全落地\\n**R26 (3.5/3.0)**: R1 认可 v2 修复; R2 新发现:\\n- Missing citations (EL4NER May 2025, Xie 2023 entity voting)\\n- hobelsberger2025systematic 疑似虚构 (integrity risk)\\n- Entity construction = MBR direct application, not novel method\\n- Unqualified \\\"first\\\" claims without \\\"for NER\\\" scope\\n\\n## Track A: Writing v3 (30-45 min, CPU)\\n- [ ] A1: Citation integrity — Semantic Scholar verify 96 entries, hobelsberger 重点 (Worker dispatched)\\n- [ ] A2: 补引 EL4NER + Xie 2023 + 4 others (Paper Agent, 依赖 A1)\\n- [ ] A3: grep \\\"first\\\" → all qualified to \\\"for NER\\\" (Worker dispatched)\\n- [ ] A4: Entity construction → MBR-grounded diagnostic ablation (Paper Agent)\\n\\n## Track B: Method Breakthrough\\n| 实验 | 类型 | 资源 | 状态 | ETA |\\n|------|------|------|------|-----|\\n| B1 SCD ×3 (std/fall/θ3) | GPU | 5090-b:0,1,3 | RUNNING | ~01:00 UTC 05-21 |\\n| E_θ Threshold-Adaptive SC ×5 | CPU | 5 Workers | 提交审批中 | +2-3h |\\n| ESJ Entity Self-Judgment | GPU | 5090-c:1 or 3 | 提交审批中 | +3-4h |\\n| 14B FewNERD inference | GPU | 5090-c:0 | RUNNING | +20-30h |\\n| 32B Qwen2.5 FT | GPU | 5090:0-3 | RUNNING 73% | ~06:30 UTC 05-21 |\\n\\n## Track C: Permanent Gate\\nPre-Review Gate 扩展到 6 步: +Step 6 Citation Integrity Check (Semantic Scholar API verify)\\n\\n## GPU 状态\\n- autodl-5090: 4× RTX 5090 → 32B 训练中\\n- autodl-5090-b: 4× RTX 5090 → GPU 0,1,3 B1 SCD; **GPU 2 空闲**\\n- autodl-5090-c: 4× RTX 5090 → GPU 0 14B inference; GPU 1,3 空闲 → ESJ 待分配; GPU 2 空闲\\n\\n## 锁定决策\\nTitle: diagnostic (无 \\\"Addressing\\\") | Ceiling-gap framing | MBR v3 | FewNERD primary | 8pp limit | Two-tier gap | Construction = diagnostic ablation (非 novel method) | §6 = Threshold Regime Analysis | Pre-Review Gate 6-step | R27 等 B1+E_θ 数据再提交\\n\\n## 关键决策日志\\n\\n| ID | 日期 | 摘要 | 关联实验 |\\n|----|------|------|----------|\\n| D204 | 2026-05-20 | 全局统一 micro-F1 口径；frontier SC 独立呈现不与 fine-tuned 并列 | exp_asb_adaptive_budget, exp_b_frontier_sc_fewnerd, exp_backup1_het_temp |\\n| D203 | 2026-05-20 | 目标从 4.0 升至 4.5：全面扩展 scope（cross-task universality  | exp_esj_entity_self_judgment, exp_mrsc_multi_round, exp_lsc_latent_sc |\\n| D202 | 2026-05-20 | ESJ negative 确认 entity-level self-judgment 全线失败（MR | exp_esj_entity_self_judgment, exp_mrsc_multi_round, exp_lsc_latent_sc |\\n| D201 | 2026-05-20 | Entity-level 修正路线（MRSC/LSC）全 negative，立即 pivot 到 s | exp_mrsc_multi_round, exp_lsc_latent_sc, exp_e_theta_adaptive |\\n| D200 | 2026-05-20 | E_θ V1 (Ridge) negative — degenerates to global θ= | exp_e_theta_adaptive |\\n| D199 | 2026-05-20 | D199: Reverse D198 conservative calibrations — LSC | — |\\n| D198 | 2026-05-20 | D198: Pivot to prescriptive framework — approve MR | — |\\n| D197 | 2026-05-20 | D197: R26 3.5/3.0 — 双线并行 (Track A writing v3 + Tra | — |\\n| D196 | 2026-05-20 | D196: Holm-Bonferroni dual reporting — per-family  | — |\\n| D195 | 2026-05-20 | D195: R25 Writing v2 Sprint — two-tier gap, Phase  | — |\\n\\n\", \"lines\": 64}, \"error\": null, \"metadata\": {}}"
    }
  },
  "sourceToolAssistantUUID": "ec6489d0-e14d-46e8-8da8-6a580919bce9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/agent_5c567c58",
  "sessionId": "bb8bc777-37fb-4956-b48e-5e9c5a98dd73",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 24_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[CRON] 实验进程异常退出（失败），需要你诊断原因。 详情: Process exited without valid W&B metrics  - exp_id: exp_b1_scd_fewnerd_standard - project: struct_self_consist_ie - server: autodl-5090-b - log_path: /root/autodl-tmp/…",
  "leafUuid": "aa0823c7-c961-4c0f-80db-f593feff7945",
  "sessionId": "bb8bc777-37fb-4956-b48e-5e9c5a98dd73"
}
```

---

### Runtime record

_source line 25_

```json
{
  "type": "ai-title",
  "aiTitle": "Diagnose experiment process exit failure",
  "sessionId": "bb8bc777-37fb-4956-b48e-5e9c5a98dd73"
}
```

---

### Tool result

_source line 26 · 2026-05-20T19:14:16.350Z_

<details><summary>↩ Tool result · `toolu_01DzWSjPa7LpBvonjQc1i4eD`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"workers\": [{\"worker_id\": \"worker_diagnose_exp_b1_scd_fewnerd_curriculum_q_20260520T190612\", \"task_type\": \"diagnose:exp_b1_scd_fewnerd_curriculum_q\", \"project\": \"struct_self_consist_ie\", \"status\": \"running\", \"started_at\": \"2026-05-20T19:06:12.535088+00:00\", \"ended_at\": null}], \"count\": 1}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2adca8d2-3f12-49f9-9c0a-9986034b2271",
  "isSidechain": false,
  "promptId": "d2210c4d-d5b9-450f-8450-2f1ffe6e0ccd",
  "type": "user",
  "uuid": "b924a522-7f16-4395-8bd6-25c250acac23",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"workers\\\": [{\\\"worker_id\\\": \\\"worker_diagnose_exp_b1_scd_fewnerd_curriculum_q_20260520T190612\\\", \\\"task_type\\\": \\\"diagnose:exp_b1_scd_fewnerd_curriculum_q\\\", \\\"project\\\": \\\"struct_self_consist_ie\\\", \\\"status\\\": \\\"running\\\", \\\"started_at\\\": \\\"2026-05-20T19:06:12.535088+00:00\\\", \\\"ended_at\\\": null}], \\\"count\\\": 1}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"workers\": [{\"worker_id\": \"worker_diagnose_exp_b1_scd_fewnerd_curriculum_q_20260520T190612\", \"task_type\": \"diagnose:exp_b1_scd_fewnerd_curriculum_q\", \"project\": \"struct_self_consist_ie\", \"status\": \"running\", \"started_at\": \"2026-05-20T19:06:12.535088+00:00\", \"ended_at\": null}], \"count\": 1}, \"error\": null, \"metadata\": {}}"
    }
  },
  "sourceToolAssistantUUID": "2adca8d2-3f12-49f9-9c0a-9986034b2271",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/agent_5c567c58",
  "sessionId": "bb8bc777-37fb-4956-b48e-5e9c5a98dd73",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 27 · 2026-05-20T19:14:25.048Z_

<details><summary>Logged reasoning block</summary>

```text
Session-start 完成。现在让我了解失败实验 `exp_b1_scd_fewnerd_standard` 的详细信息。

从 report.md 看到：
- `exp_b1_scd_fewnerd_standard` [failed] — process dead 5× with no sentinel/W&B — auto-resolved as failed
- 服务器: autodl-5090-b
- log_path: /root/autodl-tmp/struct_self_consist_ie/logs/exp_b1_scd_fewnerd_standard.log
  
现在我需要从 registry 中查找这个实验的详细配置信息，然后派诊断 Worker 去分析日志文件，看看为什么进程反复崩溃。
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b924a522-7f16-4395-8bd6-25c250acac23",
  "isSidechain": false,
  "requestId": "req_011CbEMWcjzngRTxdfmGxdRv",
  "type": "assistant",
  "uuid": "7052f20a-b06a-494d-9924-5f976ec2c86b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/agent_5c567c58",
  "sessionId": "bb8bc777-37fb-4956-b48e-5e9c5a98dd73",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015QSRLMGVUPtELCgiJ4R4Pf",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7407,
      "cache_read_input_tokens": 40481,
      "output_tokens": 609,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7407,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 609,
          "cache_read_input_tokens": 40481,
          "cache_creation_input_tokens": 7407,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7407
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

_source line 28 · 2026-05-20T19:14:25.593Z_

Session 初始化完成。4 个 cron 正在运行，1 个诊断 Worker 活跃（针对 curriculum_q）。现在处理 `exp_b1_scd_fewnerd_standard` 失败。先提取该实验的 registry 详情。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7052f20a-b06a-494d-9924-5f976ec2c86b",
  "isSidechain": false,
  "requestId": "req_011CbEMWcjzngRTxdfmGxdRv",
  "type": "assistant",
  "uuid": "c3c6224b-5c2e-44ce-9cbb-4c0ee36ea6a4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/agent_5c567c58",
  "sessionId": "bb8bc777-37fb-4956-b48e-5e9c5a98dd73",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015QSRLMGVUPtELCgiJ4R4Pf",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7407,
      "cache_read_input_tokens": 40481,
      "output_tokens": 609,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7407,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 609,
          "cache_read_input_tokens": 40481,
          "cache_creation_input_tokens": 7407,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7407
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

_source line 29 · 2026-05-20T19:14:29.976Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01As3vAqcbyPuzxDNsDjakvz`</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-agent-5c567c58/bb8bc777-37fb-4956-b48e-5e9c5a98dd73/tool-results/mcp-agent-ml-research-read_registry-1779304444566.txt | python3 -c \"\nimport json, sys\ndata = json.load(sys.stdin)\nresult = json.loads(data['result'])\nexps = result['data']['experiments']\nfor e in exps:\n    if e['exp_id'] == 'exp_b1_scd_fewnerd_standard':\n        print(json.dumps(e, indent=2, ensure_ascii=False))\n        break\n\"",
  "description": "Extract exp_b1_scd_fewnerd_standard details from registry"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c3c6224b-5c2e-44ce-9cbb-4c0ee36ea6a4",
  "isSidechain": false,
  "requestId": "req_011CbEMWcjzngRTxdfmGxdRv",
  "type": "assistant",
  "uuid": "92c9070c-2dd4-4b3e-b7e1-9926cc62dea2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/agent_5c567c58",
  "sessionId": "bb8bc777-37fb-4956-b48e-5e9c5a98dd73",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015QSRLMGVUPtELCgiJ4R4Pf",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7407,
      "cache_read_input_tokens": 40481,
      "output_tokens": 609,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7407,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 609,
          "cache_read_input_tokens": 40481,
          "cache_creation_input_tokens": 7407,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7407
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

_source line 30 · 2026-05-20T19:14:30.280Z_

<details><summary>↩ Tool result · reported error · `toolu_01As3vAqcbyPuzxDNsDjakvz`</summary>

```text
Exit code 1
Traceback (most recent call last):
  File "&lt;string>", line 7, in &lt;module>
    if e['exp_id'] == 'exp_b1_scd_fewnerd_standard':
       ~^^^^^^^^^^
TypeError: string indices must be integers, not 'str'
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "92c9070c-2dd4-4b3e-b7e1-9926cc62dea2",
  "isSidechain": false,
  "promptId": "d2210c4d-d5b9-450f-8450-2f1ffe6e0ccd",
  "type": "user",
  "uuid": "46421c61-dd52-4e8f-88ca-8c3529558a31",
  "toolUseResult": "Error: Exit code 1\nTraceback (most recent call last):\n  File \"&lt;string>\", line 7, in &lt;module>\n    if e['exp_id'] == 'exp_b1_scd_fewnerd_standard':\n       ~^^^^^^^^^^\nTypeError: string indices must be integers, not 'str'",
  "sourceToolAssistantUUID": "92c9070c-2dd4-4b3e-b7e1-9926cc62dea2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/agent_5c567c58",
  "sessionId": "bb8bc777-37fb-4956-b48e-5e9c5a98dd73",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-20T19:14:36.335Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01VZWTvB5SbzEYB9kQKFJLgg`</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-agent-5c567c58/bb8bc777-37fb-4956-b48e-5e9c5a98dd73/tool-results/mcp-agent-ml-research-read_registry-1779304444566.txt | python3 -c \"\nimport json, sys\ndata = json.load(sys.stdin)\nresult_str = data['result']\nresult = json.loads(result_str)\n# check structure\ninner = result.get('data', result)\nif isinstance(inner, str):\n    inner = json.loads(inner)\nif isinstance(inner, dict) and 'experiments' in inner:\n    exps = inner['experiments']\nelif isinstance(inner, list):\n    exps = inner\nelse:\n    print('keys:', list(inner.keys()) if isinstance(inner, dict) else type(inner))\n    sys.exit(0)\nfor e in exps:\n    if isinstance(e, str):\n        e = json.loads(e)\n    if e.get('exp_id') == 'exp_b1_scd_fewnerd_standard':\n        print(json.dumps(e, indent=2, ensure_ascii=False))\n        break\n\"",
  "description": "Extract experiment details with flexible parsing"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "46421c61-dd52-4e8f-88ca-8c3529558a31",
  "isSidechain": false,
  "requestId": "req_011CbEMXeQjVoKKSCnLeGeQQ",
  "type": "assistant",
  "uuid": "e4021303-2f5e-4e27-a67c-e578a2441980",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/agent_5c567c58",
  "sessionId": "bb8bc777-37fb-4956-b48e-5e9c5a98dd73",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V62ACAyfrqDMMQVjCjg3v4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 703,
      "cache_read_input_tokens": 47888,
      "output_tokens": 406,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 703,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 406,
          "cache_read_input_tokens": 47888,
          "cache_creation_input_tokens": 703,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 703
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

_source line 32 · 2026-05-20T19:14:36.522Z_

<details><summary>↩ Tool result · reported error · `toolu_01VZWTvB5SbzEYB9kQKFJLgg`</summary>

```text
Exit code 1
Traceback (most recent call last):
  File "&lt;string>", line 19, in &lt;module>
    e = json.loads(e)
  File "/usr/lib/python3.14/json/__init__.py", line 352, in loads
    return _default_decoder.decode(s)
           ~~~~~~~~~~~~~~~~~~~~~~~^^^
  File "/usr/lib/python3.14/json/decoder.py", line 345, in decode
    obj, end = self.raw_decode(s, idx=_w(s, 0).end())
               ~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.14/json/decoder.py", line 363, in raw_decode
    raise JSONDecodeError("Expecting value", s, err.value) from None
json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e4021303-2f5e-4e27-a67c-e578a2441980",
  "isSidechain": false,
  "promptId": "d2210c4d-d5b9-450f-8450-2f1ffe6e0ccd",
  "type": "user",
  "uuid": "48bbccc8-f942-4214-96f5-074708bfca80",
  "toolUseResult": "Error: Exit code 1\nTraceback (most recent call last):\n  File \"&lt;string>\", line 19, in &lt;module>\n    e = json.loads(e)\n  File \"/usr/lib/python3.14/json/__init__.py\", line 352, in loads\n    return _default_decoder.decode(s)\n           ~~~~~~~~~~~~~~~~~~~~~~~^^^\n  File \"/usr/lib/python3.14/json/decoder.py\", line 345, in decode\n    obj, end = self.raw_decode(s, idx=_w(s, 0).end())\n               ~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^\n  File \"/usr/lib/python3.14/json/decoder.py\", line 363, in raw_decode\n    raise JSONDecodeError(\"Expecting value\", s, err.value) from None\njson.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)",
  "sourceToolAssistantUUID": "e4021303-2f5e-4e27-a67c-e578a2441980",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/agent_5c567c58",
  "sessionId": "bb8bc777-37fb-4956-b48e-5e9c5a98dd73",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 33 · 2026-05-20T19:14:36.526Z_

```json
{
  "parentUuid": "48bbccc8-f942-4214-96f5-074708bfca80",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "e2dc29d0-6e18-44b0-91c7-33c900b7907c",
  "timestamp": "2026-05-20T19:14:36.526Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/agent_5c567c58",
  "sessionId": "bb8bc777-37fb-4956-b48e-5e9c5a98dd73",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 34 · 2026-05-20T19:14:42.173Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01UnrU8pr6KwKkNvjw5QDFnd`</summary>

```json
{
  "command": "python3 -c \"\nimport json\nwith open('/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-agent-5c567c58/bb8bc777-37fb-4956-b48e-5e9c5a98dd73/tool-results/mcp-agent-ml-research-read_registry-1779304444566.txt') as f:\n    data = json.load(f)\nresult_str = data['result']\nresult = json.loads(result_str)\ninner = result.get('data', result)\nif isinstance(inner, str):\n    inner = json.loads(inner)\nexps = inner.get('experiments', inner)\nprint(type(exps), len(exps) if isinstance(exps, (list, dict)) else 'N/A')\nif isinstance(exps, list):\n    print('first elem type:', type(exps[0]))\n    print('first elem[:200]:', str(exps[0])[:200])\nelif isinstance(exps, dict):\n    print('keys sample:', list(exps.keys())[:5])\n\"",
  "description": "Probe registry data structure"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e2dc29d0-6e18-44b0-91c7-33c900b7907c",
  "isSidechain": false,
  "requestId": "req_011CbEMY74NBXv4zfdxceCgD",
  "type": "assistant",
  "uuid": "23944c4a-8745-4b95-a9a8-aba80dc479a4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/agent_5c567c58",
  "sessionId": "bb8bc777-37fb-4956-b48e-5e9c5a98dd73",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UVPunRmijo5hmtNM7tnkRe",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 745,
      "cache_read_input_tokens": 48591,
      "output_tokens": 365,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 745,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 365,
          "cache_read_input_tokens": 48591,
          "cache_creation_input_tokens": 745,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 745
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

_source line 35 · 2026-05-20T19:14:42.262Z_

<details><summary>↩ Tool result · `toolu_01UnrU8pr6KwKkNvjw5QDFnd`</summary>

```text
&lt;class 'dict'> 207
keys sample: ['exp_b1_scd_fewnerd_standard', 'eval_scd_fewnerd_fallback', 'exp_b1_scd_fewnerd_curriculum_q', 'exp_cross_model_consistency', 'exp_backup3_distill_verifier']
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "23944c4a-8745-4b95-a9a8-aba80dc479a4",
  "isSidechain": false,
  "promptId": "d2210c4d-d5b9-450f-8450-2f1ffe6e0ccd",
  "type": "user",
  "uuid": "388de414-c187-47e9-9511-a206b730b020",
  "toolUseResult": {
    "stdout": "&lt;class 'dict'> 207\nkeys sample: ['exp_b1_scd_fewnerd_standard', 'eval_scd_fewnerd_fallback', 'exp_b1_scd_fewnerd_curriculum_q', 'exp_cross_model_consistency', 'exp_backup3_distill_verifier']",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "23944c4a-8745-4b95-a9a8-aba80dc479a4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/agent_5c567c58",
  "sessionId": "bb8bc777-37fb-4956-b48e-5e9c5a98dd73",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 36 · 2026-05-20T19:14:46.513Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01GRS5pqstJZDFqzTAjc4R5b`</summary>

```json
{
  "command": "python3 -c \"\nimport json\nwith open('/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-agent-5c567c58/bb8bc777-37fb-4956-b48e-5e9c5a98dd73/tool-results/mcp-agent-ml-research-read_registry-1779304444566.txt') as f:\n    data = json.load(f)\nresult = json.loads(data['result'])\nexps = result['data']['experiments']\ne = exps['exp_b1_scd_fewnerd_standard']\nprint(json.dumps(e, indent=2, ensure_ascii=False))\n\"",
  "description": "Extract exp_b1_scd_fewnerd_standard from registry dict"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "388de414-c187-47e9-9511-a206b730b020",
  "isSidechain": false,
  "requestId": "req_011CbEMYXWHREhty8y2rzDnJ",
  "type": "assistant",
  "uuid": "10f28789-0ee2-48de-a0bb-c3dad8d5567f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/agent_5c567c58",
  "sessionId": "bb8bc777-37fb-4956-b48e-5e9c5a98dd73",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V1nvZ2FuyUqSvpL72DykDW",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 459,
      "cache_read_input_tokens": 49336,
      "output_tokens": 275,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 459,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 275,
          "cache_read_input_tokens": 49336,
          "cache_creation_input_tokens": 459,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 459
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

_source line 37 · 2026-05-20T19:14:46.595Z_

<details><summary>↩ Tool result · `toolu_01GRS5pqstJZDFqzTAjc4R5b`</summary>

```text
{
  "status": "DONE",
  "retry_count": 0,
  "created_at": "2026-05-20T11:17:37.804Z",
  "updated_at": "2026-05-20T19:13:31.471Z",
  "hypothesis": "Standard Self-Consistency Distillation on FewNERD: fine-tune Qwen3-8B-FT with theta2n construction pseudo-labels (32,565 instances) mixed 1:1 with gold data. Greedy F1 after SCD should approach N=8 construction F1 (0.764 vs current 0.748). Transductive setting: pseudo-labels from test set SC outputs.",
  "spec": {
    "command": "llamafactory-cli train train_config_scd_fewnerd_s42.yaml",
    "server": "autodl-5090-b",
    "gpu_ids": [
      0
    ],
    "data_path": "/root/autodl-tmp/struct_self_consist_ie/data/scd_fewnerd_theta2n_s42.jsonl",
    "data_count": 32565,
    "model_name": "Qwen3-8B-FT",
    "seed": 42,
    "pid": 207109
  },
  "reproduce": {
    "finished_at": "2026-05-20T19:13:25.333Z"
  },
  "failure_reason": "process dead 5× with no sentinel/W&B — auto-resolved as failed",
  "conclusion": "failed",
  "completed_at": "2026-05-20T19:13:26.395Z",
  "extra": {
    "hook_events": [
      {
        "event": "on_failed",
        "action": "agent",
        "ts": "2026-05-20T19:13:35.804759+00:00"
      }
    ]
  }
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "10f28789-0ee2-48de-a0bb-c3dad8d5567f",
  "isSidechain": false,
  "promptId": "d2210c4d-d5b9-450f-8450-2f1ffe6e0ccd",
  "type": "user",
  "uuid": "6623a39d-8761-473d-a2cf-21a76b3b9dc2",
  "toolUseResult": {
    "stdout": "{\n  \"status\": \"DONE\",\n  \"retry_count\": 0,\n  \"created_at\": \"2026-05-20T11:17:37.804Z\",\n  \"updated_at\": \"2026-05-20T19:13:31.471Z\",\n  \"hypothesis\": \"Standard Self-Consistency Distillation on FewNERD: fine-tune Qwen3-8B-FT with theta2n construction pseudo-labels (32,565 instances) mixed 1:1 with gold data. Greedy F1 after SCD should approach N=8 construction F1 (0.764 vs current 0.748). Transductive setting: pseudo-labels from test set SC outputs.\",\n  \"spec\": {\n    \"command\": \"llamafactory-cli train train_config_scd_fewnerd_s42.yaml\",\n    \"server\": \"autodl-5090-b\",\n    \"gpu_ids\": [\n      0\n    ],\n    \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/data/scd_fewnerd_theta2n_s42.jsonl\",\n    \"data_count\": 32565,\n    \"model_name\": \"Qwen3-8B-FT\",\n    \"seed\": 42,\n    \"pid\": 207109\n  },\n  \"reproduce\": {\n    \"finished_at\": \"2026-05-20T19:13:25.333Z\"\n  },\n  \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\",\n  \"conclusion\": \"failed\",\n  \"completed_at\": \"2026-05-20T19:13:26.395Z\",\n  \"extra\": {\n    \"hook_events\": [\n      {\n        \"event\": \"on_failed\",\n        \"action\": \"agent\",\n        \"ts\": \"2026-05-20T19:13:35.804759+00:00\"\n      }\n    ]\n  }\n}",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "10f28789-0ee2-48de-a0bb-c3dad8d5567f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/agent_5c567c58",
  "sessionId": "bb8bc777-37fb-4956-b48e-5e9c5a98dd73",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 38 · 2026-05-20T19:14:55.800Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have the full picture of the failed experiment. Key details:
- `exp_b1_scd_fewnerd_standard` — SCD training on FewNERD
- Server: autodl-5090-b, GPU 0
- Command: `llamafactory-cli train train_config_scd_fewnerd_s42.yaml`
- Failure: process dead 5× with no sentinel/W&B — auto-resolved as failed


- Log location: /root/autodl-tmp/struct_self_consist_ie/logs/exp_b1_scd_fewnerd_standard.log

I'm noticing that `exp_b1_scd_fewnerd_curriculum_q` hit the same failure pattern, and there's already a diagnostic worker running for it — this points to a shared issue on autodl-5090-b. I need to check the on-experiment-failed skill and then spawn a worker to diagnose the failure by examining the log file on that server.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6623a39d-8761-473d-a2cf-21a76b3b9dc2",
  "isSidechain": false,
  "requestId": "req_011CbEMYr3W3U96rNoB9YN6p",
  "type": "assistant",
  "uuid": "d5b0584e-5941-4098-b78b-de089cdfc403",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/agent_5c567c58",
  "sessionId": "bb8bc777-37fb-4956-b48e-5e9c5a98dd73",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011oYvXJCJBYJeEf1adjPTsJ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 775,
      "cache_read_input_tokens": 49795,
      "output_tokens": 543,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 775,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 543,
          "cache_read_input_tokens": 49795,
          "cache_creation_input_tokens": 775,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 775
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

_source line 39 · 2026-05-20T19:14:55.802Z_

实验详情已获取。`exp_b1_scd_fewnerd_standard` 在 autodl-5090-b 上运行 `llamafactory-cli train`，进程 5 次死亡无 W&B 指标。读取诊断 skill 并派 Worker 查日志。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d5b0584e-5941-4098-b78b-de089cdfc403",
  "isSidechain": false,
  "requestId": "req_011CbEMYr3W3U96rNoB9YN6p",
  "type": "assistant",
  "uuid": "944dae63-f614-4f9f-8755-47da8fed323e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/agent_5c567c58",
  "sessionId": "bb8bc777-37fb-4956-b48e-5e9c5a98dd73",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011oYvXJCJBYJeEf1adjPTsJ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 775,
      "cache_read_input_tokens": 49795,
      "output_tokens": 543,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 775,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 543,
          "cache_read_input_tokens": 49795,
          "cache_creation_input_tokens": 775,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 775
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

_source line 40 · 2026-05-20T19:14:56.328Z_

<details open><summary>🔧 Tool call — Read · `toolu_013rZgo1PFbmbiYbuwhd1LPb`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/skills/on-experiment-failed.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "944dae63-f614-4f9f-8755-47da8fed323e",
  "isSidechain": false,
  "requestId": "req_011CbEMYr3W3U96rNoB9YN6p",
  "type": "assistant",
  "uuid": "f9494493-f7a4-4cb8-b560-6a08a4a8036f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/agent_5c567c58",
  "sessionId": "bb8bc777-37fb-4956-b48e-5e9c5a98dd73",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011oYvXJCJBYJeEf1adjPTsJ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 775,
      "cache_read_input_tokens": 49795,
      "output_tokens": 543,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 775,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 543,
          "cache_read_input_tokens": 49795,
          "cache_creation_input_tokens": 775,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 775
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

_source line 41 · 2026-05-20T19:14:56.653Z_

<details><summary>↩ Tool result · reported error · `toolu_01Y4DULdLz8bEcxCwTdkNYDk`</summary>

```text
File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/agent_5c567c58.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "061910ed-7125-4b57-b4ee-4b4983978d07",
  "isSidechain": false,
  "promptId": "d2210c4d-d5b9-450f-8450-2f1ffe6e0ccd",
  "type": "user",
  "uuid": "1dbd1f8b-ed5d-4034-a3f4-31a405760848",
  "toolUseResult": "Error: File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/agent_5c567c58.",
  "sourceToolAssistantUUID": "061910ed-7125-4b57-b4ee-4b4983978d07",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/agent_5c567c58",
  "sessionId": "bb8bc777-37fb-4956-b48e-5e9c5a98dd73",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-20T19:14:56.343Z_

<details><summary>↩ Tool result · reported error · `toolu_013rZgo1PFbmbiYbuwhd1LPb`</summary>

```text
File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/agent_5c567c58.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f9494493-f7a4-4cb8-b560-6a08a4a8036f",
  "isSidechain": false,
  "promptId": "d2210c4d-d5b9-450f-8450-2f1ffe6e0ccd",
  "type": "user",
  "uuid": "cc905648-8184-490c-846f-b012f52ea9d8",
  "toolUseResult": "Error: File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/agent_5c567c58.",
  "sourceToolAssistantUUID": "f9494493-f7a4-4cb8-b560-6a08a4a8036f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/agent_5c567c58",
  "sessionId": "bb8bc777-37fb-4956-b48e-5e9c5a98dd73",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-20T19:14:56.647Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Y4DULdLz8bEcxCwTdkNYDk`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/skills/resource-saturation.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cc905648-8184-490c-846f-b012f52ea9d8",
  "isSidechain": false,
  "requestId": "req_011CbEMYr3W3U96rNoB9YN6p",
  "type": "assistant",
  "uuid": "061910ed-7125-4b57-b4ee-4b4983978d07",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/agent_5c567c58",
  "sessionId": "bb8bc777-37fb-4956-b48e-5e9c5a98dd73",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011oYvXJCJBYJeEf1adjPTsJ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 775,
      "cache_read_input_tokens": 49795,
      "output_tokens": 543,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 775,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 543,
          "cache_read_input_tokens": 49795,
          "cache_creation_input_tokens": 775,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 775
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

### Runtime record

_source line 44_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[CRON] 实验进程异常退出（失败），需要你诊断原因。 详情: Process exited without valid W&B metrics  - exp_id: exp_b1_scd_fewnerd_standard - project: struct_self_consist_ie - server: autodl-5090-b - log_path: /root/autodl-tmp/…",
  "leafUuid": "1dbd1f8b-ed5d-4034-a3f4-31a405760848",
  "sessionId": "bb8bc777-37fb-4956-b48e-5e9c5a98dd73"
}
```

---

### Runtime record

_source line 45_

```json
{
  "type": "ai-title",
  "aiTitle": "Diagnose experiment process exit failure",
  "sessionId": "bb8bc777-37fb-4956-b48e-5e9c5a98dd73"
}
```

---

### Tool call

_source line 46 · 2026-05-20T19:15:00.139Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01L9oaQmZF6bBHkfxc3CdWgq`</summary>

```json
{
  "pattern": "**/skills/on-experiment-failed*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1dbd1f8b-ed5d-4034-a3f4-31a405760848",
  "isSidechain": false,
  "requestId": "req_011CbEMZbKkooXhn9USDcudk",
  "type": "assistant",
  "uuid": "3925fd90-5797-4dc9-87a3-a933f740af6c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/agent_5c567c58",
  "sessionId": "bb8bc777-37fb-4956-b48e-5e9c5a98dd73",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QcqYFTMUXWJfKzohuvWTmp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 708,
      "cache_read_input_tokens": 50570,
      "output_tokens": 174,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 708,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 174,
          "cache_read_input_tokens": 50570,
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
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 47 · 2026-05-20T19:15:00.208Z_

<details><summary>↩ Tool result · `toolu_01L9oaQmZF6bBHkfxc3CdWgq`</summary>

```text
No files found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3925fd90-5797-4dc9-87a3-a933f740af6c",
  "isSidechain": false,
  "promptId": "d2210c4d-d5b9-450f-8450-2f1ffe6e0ccd",
  "type": "user",
  "uuid": "0a611542-3147-4a54-98d1-3cb9c5373d5c",
  "toolUseResult": {
    "filenames": [],
    "durationMs": 64,
    "numFiles": 0,
    "truncated": false
  },
  "sourceToolAssistantUUID": "3925fd90-5797-4dc9-87a3-a933f740af6c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/agent_5c567c58",
  "sessionId": "bb8bc777-37fb-4956-b48e-5e9c5a98dd73",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 48 · 2026-05-20T19:15:00.599Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01QENNyy3PP6K1DaLW6dFjk4`</summary>

```json
{
  "pattern": "**/skills/resource-saturation*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0a611542-3147-4a54-98d1-3cb9c5373d5c",
  "isSidechain": false,
  "requestId": "req_011CbEMZbKkooXhn9USDcudk",
  "type": "assistant",
  "uuid": "f6e53680-0bbb-42c2-92fa-1a311985dde6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/agent_5c567c58",
  "sessionId": "bb8bc777-37fb-4956-b48e-5e9c5a98dd73",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QcqYFTMUXWJfKzohuvWTmp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 708,
      "cache_read_input_tokens": 50570,
      "output_tokens": 174,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 708,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 174,
          "cache_read_input_tokens": 50570,
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
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 49 · 2026-05-20T19:15:00.662Z_

<details><summary>↩ Tool result · `toolu_01QENNyy3PP6K1DaLW6dFjk4`</summary>

```text
No files found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f6e53680-0bbb-42c2-92fa-1a311985dde6",
  "isSidechain": false,
  "promptId": "d2210c4d-d5b9-450f-8450-2f1ffe6e0ccd",
  "type": "user",
  "uuid": "2357a52f-aeb3-427d-8c9f-166bdfcd2b50",
  "toolUseResult": {
    "filenames": [],
    "durationMs": 59,
    "numFiles": 0,
    "truncated": false
  },
  "sourceToolAssistantUUID": "f6e53680-0bbb-42c2-92fa-1a311985dde6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/agent_5c567c58",
  "sessionId": "bb8bc777-37fb-4956-b48e-5e9c5a98dd73",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 50 · 2026-05-20T19:15:03.906Z_

<details open><summary>🔧 Tool call — Glob · `toolu_015tJr6NZjG1saQr95aUYwcq`</summary>

```json
{
  "pattern": "**/skills/**/*.skill.md",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2357a52f-aeb3-427d-8c9f-166bdfcd2b50",
  "isSidechain": false,
  "requestId": "req_011CbEMZtD1JPd3icp41PnUH",
  "type": "assistant",
  "uuid": "a9c32d9f-c19e-40b0-b41a-f1098dbc1fcc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/agent_5c567c58",
  "sessionId": "bb8bc777-37fb-4956-b48e-5e9c5a98dd73",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JUCiB5e2A8JfgoLcrb4tQe",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 241,
      "cache_read_input_tokens": 51278,
      "output_tokens": 94,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 241,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 94,
          "cache_read_input_tokens": 51278,
          "cache_creation_input_tokens": 241,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 241
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

_source line 51 · 2026-05-20T19:15:03.957Z_

<details><summary>↩ Tool result · `toolu_015tJr6NZjG1saQr95aUYwcq`</summary>

```text
No files found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a9c32d9f-c19e-40b0-b41a-f1098dbc1fcc",
  "isSidechain": false,
  "promptId": "d2210c4d-d5b9-450f-8450-2f1ffe6e0ccd",
  "type": "user",
  "uuid": "df184163-d9c5-4ee7-b515-e474e6fd4162",
  "toolUseResult": {
    "filenames": [],
    "durationMs": 48,
    "numFiles": 0,
    "truncated": false
  },
  "sourceToolAssistantUUID": "a9c32d9f-c19e-40b0-b41a-f1098dbc1fcc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/agent_5c567c58",
  "sessionId": "bb8bc777-37fb-4956-b48e-5e9c5a98dd73",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 52 · 2026-05-20T19:15:06.642Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01PmRZqGrVXzMdKtc3gJgBWK`</summary>

```json
{
  "pattern": "**/skills/**",
  "path": "/home/ubuntu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "df184163-d9c5-4ee7-b515-e474e6fd4162",
  "isSidechain": false,
  "requestId": "req_011CbEMa8GqrN5zxdY9hDX7a",
  "type": "assistant",
  "uuid": "bd3332ac-1dee-41ec-9b49-0808c4df4f81",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/agent_5c567c58",
  "sessionId": "bb8bc777-37fb-4956-b48e-5e9c5a98dd73",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SrSbTVeK2TM4xpA1iCKvn9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 109,
      "cache_read_input_tokens": 51519,
      "output_tokens": 75,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 109,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 75,
          "cache_read_input_tokens": 51519,
          "cache_creation_input_tokens": 109,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 109
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

_source line 53 · 2026-05-20T19:15:06.915Z_

<details><summary>↩ Tool result · `toolu_01PmRZqGrVXzMdKtc3gJgBWK`</summary>

```text
/home/ubuntu/agent-ml-research/.venv/lib/python3.14/site-packages/anthropic/resources/beta/skills/__init__.py
/home/ubuntu/agent-ml-research/.venv/lib/python3.14/site-packages/anthropic/resources/beta/skills/skills.py
/home/ubuntu/agent-ml-research/.venv/lib/python3.14/site-packages/anthropic/resources/beta/skills/versions.py
/home/ubuntu/agent-ml-research/.venv/lib/python3.14/site-packages/anthropic/types/beta/skills/version_create_response.py
/home/ubuntu/agent-ml-research/.venv/lib/python3.14/site-packages/anthropic/types/beta/skills/version_create_params.py
/home/ubuntu/agent-ml-research/.venv/lib/python3.14/site-packages/anthropic/types/beta/skills/__init__.py
/home/ubuntu/agent-ml-research/.venv/lib/python3.14/site-packages/anthropic/types/beta/skills/version_list_params.py
/home/ubuntu/agent-ml-research/.venv/lib/python3.14/site-packages/anthropic/types/beta/skills/version_retrieve_response.py
/home/ubuntu/agent-ml-research/.venv/lib/python3.14/site-packages/anthropic/types/beta/skills/version_list_response.py
/home/ubuntu/agent-ml-research/.venv/lib/python3.14/site-packages/anthropic/types/beta/skills/version_delete_response.py
/home/ubuntu/agent-ml-research/.venv/lib/python3.14/site-packages/fastapi/.agents/skills/fastapi/references/dependencies.md
/home/ubuntu/agent-ml-research/.venv/lib/python3.14/site-packages/fastapi/.agents/skills/fastapi/SKILL.md
/home/ubuntu/agent-ml-research/.venv/lib/python3.14/site-packages/fastapi/.agents/skills/fastapi/references/other-tools.md
/home/ubuntu/agent-ml-research/.venv/lib/python3.14/site-packages/fastapi/.agents/skills/fastapi/references/streaming.md
/home/ubuntu/agent-ml-research/core/skills/__init__.py
/home/ubuntu/agent-ml-research/core/skills/tracker.py
/home/ubuntu/agent-ml-research/core/skills/evolution.py
/home/ubuntu/agent-ml-research/core/skills/loader.py
/home/ubuntu/agent-ml-research/core/skills/plugin_loader.py
/home/ubuntu/agent-ml-research/skills/global/academic-writer.skill.md
/home/ubuntu/agent-ml-research/skills/global/code-survey.skill.md
/home/ubuntu/agent-ml-research/skills/global/accelerate-distributed.skill.md
/home/ubuntu/agent-ml-research/skills/global/dataset-discovery.skill.md
/home/ubuntu/agent-ml-research/skills/global/director-reviewer-synthesis.skill.md
/home/ubuntu/agent-ml-research/skills/global/data-snapshot.skill.md
/home/ubuntu/agent-ml-research/skills/global/check-training-status.skill.md
/home/ubuntu/agent-ml-research/skills/global/check-key.skill.md
/home/ubuntu/agent-ml-research/skills/global/distill-session.skill.md
/home/ubuntu/agent-ml-research/skills/global/elastic-gpu.skill.md
/home/ubuntu/agent-ml-research/skills/global/hf-hub.skill.md
/home/ubuntu/agent-ml-research/skills/global/first-project-entry.skill.md
/home/ubuntu/agent-ml-research/skills/global/experiment-analysis.skill.md
/home/ubuntu/agent-ml-research/skills/global/idea-generation.skill.md
/home/ubuntu/agent-ml-research/skills/global/idea-proposal.skill.md
/home/ubuntu/agent-ml-research/skills/global/manager-cloud-rental.skill.md
/home/ubuntu/agent-ml-research/skills/global/lm-eval-harness.skill.md
/home/ubuntu/agent-ml-research/skills/global/manager-claude-pool.skill.md
/home/ubuntu/agent-ml-research/skills/global/paper-image-extractor.skill.md
/home/ubuntu/agent-ml-research/skills/global/novelty-check.skill.md
/home/ubuntu/agent-ml-research/skills/global/narrative-animation.skill.md
/home/ubuntu/agent-ml-research/skills/global/mvp-validation.skill.md
/home/ubuntu/agent-ml-research/skills/global/latex-paper.skill.md
/home/ubuntu/agent-ml-research/skills/global/on-datagen-done.skill.md
/home/ubuntu/agent-ml-research/skills/global/negative-framing-review.skill.md
/home/ubuntu/agent-ml-research/skills/global/on-experiment-pending.skill.md
/home/ubuntu/agent-ml-research/skills/global/on-worker-done.skill.md
/home/ubuntu/agent-ml-research/skills/global/on-experiment-failed.skill.md
/home/ubuntu/agent-ml-research/skills/global/paper-research.skill.md
/home/ubuntu/agent-ml-research/skills/global/research-kickoff.skill.md
/home/ubuntu/agent-ml-research/skills/global/resource-saturation.skill.md
/home/ubuntu/agent-ml-research/skills/global/research-health-check.skill.md
/home/ubuntu/agent-ml-research/skills/global/research-news.skill.md
/home/ubuntu/agent-ml-research/skills/global/paper-research-standalone.skill.md
/home/ubuntu/agent-ml-research/skills/global/rebuttal.skill.md
/home/ubuntu/agent-ml-research/skills/global/peft-lora.skill.md
/home/ubuntu/agent-ml-research/skills/global/review-reviewer-session-start.skill.md
/home/ubuntu/agent-ml-research/skills/global/review-report-action.skill.md
/home/ubuntu/agent-ml-research/skills/global/skill-creator.skill.md
/home/ubuntu/agent-ml-research/skills/global/study-director-session-start.skill.md
/home/ubuntu/agent-ml-research/skills/global/trl-training.skill.md
/home/ubuntu/agent-ml-research/skills/global/s3-backup.skill.md
/home/ubuntu/agent-ml-research/skills/global/session-start.skill.md
/home/ubuntu/agent-ml-research/skills/global/wandb-guide.skill.md
/home/ubuntu/agent-ml-research/skills/global/ssh-env-setup.skill.md
/home/ubuntu/agent-ml-research/skills/global/study-agent-assembly.skill.md
/home/ubuntu/agent-ml-research/skills/plugins/__init__.py
/home/ubuntu/agent-ml-research/skills/plugins/chart_gen.py
/home/ubuntu/agent-ml-research/skills/plugins/beijing_time.py
/home/ubuntu/agent-ml-research/skills/plugins/feishu_docs.py
/home/ubuntu/agent-ml-research/skills/plugins/local_fs.py
/home/ubuntu/agent-ml-research/skills/plugins/project_files.py
/home/ubuntu/agent-ml-research/skills/plugins/feishu_docs_v2.py
/home/ubuntu/agent-ml-research/skills/plugins/local_shell.py
/home/ubuntu/agent-ml-research/skills/plugins/websearch.py
/home/ubuntu/agent-ml-research/skills/global/experiment-matrix.skill.md
/home/ubuntu/agent-ml-research/skills/global/dream-report-action.skill.md
/home/ubuntu/agent-ml-research/skills/global/director-research-steering.skill.md
/home/ubuntu/agent-ml-research/skills/global/literature-scan.skill.md
/home/ubuntu/agent-ml-research/skills/global/dream-cron.skill.md
/home/ubuntu/agent-ml-research/skills/global/manager-async-ops.skill.md
/home/ubuntu/agent-ml-research/skills/global/manager-ec2-provisioning.skill.md
/home/ubuntu/agent-ml-research/skills/global/manager-readiness-check.skill.md
/home/ubuntu/agent-ml-research/skills/global/manager-state-verification.skill.md
/home/ubuntu/agent-ml-research/skills/global/reference-audit.skill.md
/home/ubuntu/agent-ml-research/skills/global/post-mvp-kickoff.skill.md
/home/ubuntu/agent-ml-research/core/skills/__pycache__/__init__.cpython-314.pyc
/home/ubuntu/agent-ml-research/core/skills/__pycache__/loader.cpython-314.pyc
/home/ubuntu/agent-ml-research/core/skills/__pycache__/tracker.cpython-314.pyc
/home/ubuntu/agent-ml-research/skills/global/paper-from-scratch.skill.md
/home/ubuntu/agent-ml-research/skills/global/ml-experiment-guide.skill.md
/home/ubuntu/agent-ml-research/skills/global/competitor-experiment-reference.skill.md
/home/ubuntu/agent-ml-research/skills/global/director-experiment-review.skill.md
/home/ubuntu/agent-ml-research/skills/global/ai-time-discipline.skill.md
/home/ubuntu/agent-ml-research/skills/global/on-experiment-done.skill.md
/home/ubuntu/agent-ml-research/skills/global/progress-report.skill.md
/home/ubuntu/agent-ml-research/skills/global/paper-quality-lessons.skill.md
/home/ubuntu/agent-ml-research/skills/global/submit-experiment.skill.md
/home/ubuntu/agent-ml-research/skills/global/plan-next-experiment.skill.md
/home/ubuntu/agent-ml-research/skills/global/write-paper-section.skill.md
/home/ubuntu/agent-ml-research/skills/global/draw-paper-figure.skill.md
(Results are truncated. Consider using a more specific path or pattern.)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bd3332ac-1dee-41ec-9b49-0808c4df4f81",
  "isSidechain": false,
  "promptId": "d2210c4d-d5b9-450f-8450-2f1ffe6e0ccd",
  "type": "user",
  "uuid": "49d7cbce-d289-4b60-b311-44190be42593",
  "toolUseResult": {
    "filenames": [
      "/home/ubuntu/agent-ml-research/.venv/lib/python3.14/site-packages/anthropic/resources/beta/skills/__init__.py",
      "/home/ubuntu/agent-ml-research/.venv/lib/python3.14/site-packages/anthropic/resources/beta/skills/skills.py",
      "/home/ubuntu/agent-ml-research/.venv/lib/python3.14/site-packages/anthropic/resources/beta/skills/versions.py",
      "/home/ubuntu/agent-ml-research/.venv/lib/python3.14/site-packages/anthropic/types/beta/skills/version_create_response.py",
      "/home/ubuntu/agent-ml-research/.venv/lib/python3.14/site-packages/anthropic/types/beta/skills/version_create_params.py",
      "/home/ubuntu/agent-ml-research/.venv/lib/python3.14/site-packages/anthropic/types/beta/skills/__init__.py",
      "/home/ubuntu/agent-ml-research/.venv/lib/python3.14/site-packages/anthropic/types/beta/skills/version_list_params.py",
      "/home/ubuntu/agent-ml-research/.venv/lib/python3.14/site-packages/anthropic/types/beta/skills/version_retrieve_response.py",
      "/home/ubuntu/agent-ml-research/.venv/lib/python3.14/site-packages/anthropic/types/beta/skills/version_list_response.py",
      "/home/ubuntu/agent-ml-research/.venv/lib/python3.14/site-packages/anthropic/types/beta/skills/version_delete_response.py",
      "/home/ubuntu/agent-ml-research/.venv/lib/python3.14/site-packages/fastapi/.agents/skills/fastapi/references/dependencies.md",
      "/home/ubuntu/agent-ml-research/.venv/lib/python3.14/site-packages/fastapi/.agents/skills/fastapi/SKILL.md",
      "/home/ubuntu/agent-ml-research/.venv/lib/python3.14/site-packages/fastapi/.agents/skills/fastapi/references/other-tools.md",
      "/home/ubuntu/agent-ml-research/.venv/lib/python3.14/site-packages/fastapi/.agents/skills/fastapi/references/streaming.md",
      "/home/ubuntu/agent-ml-research/core/skills/__init__.py",
      "/home/ubuntu/agent-ml-research/core/skills/tracker.py",
      "/home/ubuntu/agent-ml-research/core/skills/evolution.py",
      "/home/ubuntu/agent-ml-research/core/skills/loader.py",
      "/home/ubuntu/agent-ml-research/core/skills/plugin_loader.py",
      "/home/ubuntu/agent-ml-research/skills/global/academic-writer.skill.md",
      "/home/ubuntu/agent-ml-research/skills/global/code-survey.skill.md",
      "/home/ubuntu/agent-ml-research/skills/global/accelerate-distributed.skill.md",
      "/home/ubuntu/agent-ml-research/skills/global/dataset-discovery.skill.md",
      "/home/ubuntu/agent-ml-research/skills/global/director-reviewer-synthesis.skill.md",
      "/home/ubuntu/agent-ml-research/skills/global/data-snapshot.skill.md",
      "/home/ubuntu/agent-ml-research/skills/global/check-training-status.skill.md",
      "/home/ubuntu/agent-ml-research/skills/global/check-key.skill.md",
      "/home/ubuntu/agent-ml-research/skills/global/distill-session.skill.md",
      "/home/ubuntu/agent-ml-research/skills/global/elastic-gpu.skill.md",
      "/home/ubuntu/agent-ml-research/skills/global/hf-hub.skill.md",
      "/home/ubuntu/agent-ml-research/skills/global/first-project-entry.skill.md",
      "/home/ubuntu/agent-ml-research/skills/global/experiment-analysis.skill.md",
      "/home/ubuntu/agent-ml-research/skills/global/idea-generation.skill.md",
      "/home/ubuntu/agent-ml-research/skills/global/idea-proposal.skill.md",
      "/home/ubuntu/agent-ml-research/skills/global/manager-cloud-rental.skill.md",
      "/home/ubuntu/agent-ml-research/skills/global/lm-eval-harness.skill.md",
      "/home/ubuntu/agent-ml-research/skills/global/manager-claude-pool.skill.md",
      "/home/ubuntu/agent-ml-research/skills/global/paper-image-extractor.skill.md",
      "/home/ubuntu/agent-ml-research/skills/global/novelty-check.skill.md",
      "/home/ubuntu/agent-ml-research/skills/global/narrative-animation.skill.md",
      "/home/ubuntu/agent-ml-research/skills/global/mvp-validation.skill.md",
      "/home/ubuntu/agent-ml-research/skills/global/latex-paper.skill.md",
      "/home/ubuntu/agent-ml-research/skills/global/on-datagen-done.skill.md",
      "/home/ubuntu/agent-ml-research/skills/global/negative-framing-review.skill.md",
      "/home/ubuntu/agent-ml-research/skills/global/on-experiment-pending.skill.md",
      "/home/ubuntu/agent-ml-research/skills/global/on-worker-done.skill.md",
      "/home/ubuntu/agent-ml-research/skills/global/on-experiment-failed.skill.md",
      "/home/ubuntu/agent-ml-research/skills/global/paper-research.skill.md",
      "/home/ubuntu/agent-ml-research/skills/global/research-kickoff.skill.md",
      "/home/ubuntu/agent-ml-research/skills/global/resource-saturation.skill.md",
      "/home/ubuntu/agent-ml-research/skills/global/research-health-check.skill.md",
      "/home/ubuntu/agent-ml-research/skills/global/research-news.skill.md",
      "/home/ubuntu/agent-ml-research/skills/global/paper-research-standalone.skill.md",
      "/home/ubuntu/agent-ml-research/skills/global/rebuttal.skill.md",
      "/home/ubuntu/agent-ml-research/skills/global/peft-lora.skill.md",
      "/home/ubuntu/agent-ml-research/skills/global/review-reviewer-session-start.skill.md",
      "/home/ubuntu/agent-ml-research/skills/global/review-report-action.skill.md",
      "/home/ubuntu/agent-ml-research/skills/global/skill-creator.skill.md",
      "/home/ubuntu/agent-ml-research/skills/global/study-director-session-start.skill.md",
      "/home/ubuntu/agent-ml-research/skills/global/trl-training.skill.md",
      "/home/ubuntu/agent-ml-research/skills/global/s3-backup.skill.md",
      "/home/ubuntu/agent-ml-research/skills/global/session-start.skill.md",
      "/home/ubuntu/agent-ml-research/skills/global/wandb-guide.skill.md",
      "/home/ubuntu/agent-ml-research/skills/global/ssh-env-setup.skill.md",
      "/home/ubuntu/agent-ml-research/skills/global/study-agent-assembly.skill.md",
      "/home/ubuntu/agent-ml-research/skills/plugins/__init__.py",
      "/home/ubuntu/agent-ml-research/skills/plugins/chart_gen.py",
      "/home/ubuntu/agent-ml-research/skills/plugins/beijing_time.py",
      "/home/ubuntu/agent-ml-research/skills/plugins/feishu_docs.py",
      "/home/ubuntu/agent-ml-research/skills/plugins/local_fs.py",
      "/home/ubuntu/agent-ml-research/skills/plugins/project_files.py",
      "/home/ubuntu/agent-ml-research/skills/plugins/feishu_docs_v2.py",
      "/home/ubuntu/agent-ml-research/skills/plugins/local_shell.py",
      "/home/ubuntu/agent-ml-research/skills/plugins/websearch.py",
      "/home/ubuntu/agent-ml-research/skills/global/experiment-matrix.skill.md",
      "/home/ubuntu/agent-ml-research/skills/global/dream-report-action.skill.md",
      "/home/ubuntu/agent-ml-research/skills/global/director-research-steering.skill.md",
      "/home/ubuntu/agent-ml-research/skills/global/literature-scan.skill.md",
      "/home/ubuntu/agent-ml-research/skills/global/dream-cron.skill.md",
      "/home/ubuntu/agent-ml-research/skills/global/manager-async-ops.skill.md",
      "/home/ubuntu/agent-ml-research/skills/global/manager-ec2-provisioning.skill.md",
      "/home/ubuntu/agent-ml-research/skills/global/manager-readiness-check.skill.md",
      "/home/ubuntu/agent-ml-research/skills/global/manager-state-verification.skill.md",
      "/home/ubuntu/agent-ml-research/skills/global/reference-audit.skill.md",
      "/home/ubuntu/agent-ml-research/skills/global/post-mvp-kickoff.skill.md",
      "/home/ubuntu/agent-ml-research/core/skills/__pycache__/__init__.cpython-314.pyc",
      "/home/ubuntu/agent-ml-research/core/skills/__pycache__/loader.cpython-314.pyc",
      "/home/ubuntu/agent-ml-research/core/skills/__pycache__/tracker.cpython-314.pyc",
      "/home/ubuntu/agent-ml-research/skills/global/paper-from-scratch.skill.md",
      "/home/ubuntu/agent-ml-research/skills/global/ml-experiment-guide.skill.md",
      "/home/ubuntu/agent-ml-research/skills/global/competitor-experiment-reference.skill.md",
      "/home/ubuntu/agent-ml-research/skills/global/director-experiment-review.skill.md",
      "/home/ubuntu/agent-ml-research/skills/global/ai-time-discipline.skill.md",
      "/home/ubuntu/agent-ml-research/skills/global/on-experiment-done.skill.md",
      "/home/ubuntu/agent-ml-research/skills/global/progress-report.skill.md",
      "/home/ubuntu/agent-ml-research/skills/global/paper-quality-lessons.skill.md",
      "/home/ubuntu/agent-ml-research/skills/global/submit-experiment.skill.md",
      "/home/ubuntu/agent-ml-research/skills/global/plan-next-experiment.skill.md",
      "/home/ubuntu/agent-ml-research/skills/global/write-paper-section.skill.md",
      "/home/ubuntu/agent-ml-research/skills/global/draw-paper-figure.skill.md"
    ],
    "durationMs": 270,
    "numFiles": 100,
    "truncated": true
  },
  "sourceToolAssistantUUID": "bd3332ac-1dee-41ec-9b49-0808c4df4f81",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/agent_5c567c58",
  "sessionId": "bb8bc777-37fb-4956-b48e-5e9c5a98dd73",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 54 · 2026-05-20T19:15:09.898Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Px4rrMxAVdw8FdyrwBDqVW`</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/skills/global/on-experiment-failed.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "49d7cbce-d289-4b60-b311-44190be42593",
  "isSidechain": false,
  "requestId": "req_011CbEMaLvMRRnyj1DTBxsxn",
  "type": "assistant",
  "uuid": "d785f1df-e3bc-49bc-bc24-053a78e337c4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/agent_5c567c58",
  "sessionId": "bb8bc777-37fb-4956-b48e-5e9c5a98dd73",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RYVeozfwLqZf9hCGh1nGHD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2736,
      "cache_read_input_tokens": 51628,
      "output_tokens": 76,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2736,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 76,
          "cache_read_input_tokens": 51628,
          "cache_creation_input_tokens": 2736,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2736
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

_source line 55 · 2026-05-20T19:15:09.908Z_

<details><summary>↩ Tool result · `toolu_01Px4rrMxAVdw8FdyrwBDqVW`</summary>

````text
1	---
2	name: on-experiment-failed
3	description: 实验失败后的自动诊断工作流——查日志分析原因、更新 registry、通知 Director。[CRON] 实验失败消息到达时使用。
4	scope: global
5	tags:
6	- workflow
7	- diagnosis
8	- cron-hook
9	tools:
10	- read_registry
11	- tail_training_logs
12	- update_registry
13	- append_idea
14	- feishu_send_result_card
15	- spawn_worker
16	- check_job_status
17	version: 4
18	heavy: true
19	roles:
20	- agent
21	---
22	
23	# 实验失败诊断工作流
24	
25	## 触发方式
26	由 cron hook 自动触发：进程退出且 W&B 无数据 / W&B state=failed/crashed / NaN 检测到。
27	
28	## 步骤
29	
30	### Step 0: 读取项目上下文（诊断前必须执行）
31	先读文档，再看日志——否则诊断方向可能完全错误：
32	
33	- `read_project_file("memory.md")` — **最重要**：查是否有相同失败模式的历史记录和已知修复方案
34	- Worker 通过 `list_repo_tree` + `read_repo_file` 按需从代码仓库读取训练脚本结构
35	
36	读完后检查：
37	- memory.md 里有没有"此类实验曾失败，原因是 X"的记录？→ 直接按已知方案诊断，跳过 Step 2 通用流程
38	- 代码仓库中的训练入口和参数格式是否与本次实验配置匹配？（Worker 可用 `list_repo_tree` + `read_repo_file` 查看）
39	
40	### Step 1: 了解失败背景
41	- read_registry(exp_id) — 查看状态、conclusion、notes、metrics、log_path
42	
43	### Step 2: 浅层日志诊断
44	有 log_path 时：tail_training_logs(server, **绝对路径**, lines=80)
45	- 寻找：OOM、CUDA error、NaN、assertion error、数据加载错误、Python Traceback
46	- 没找到 → 增加行数再查
47	
48	### Step 2.5: 深查（满足以下任一条件时 spawn_worker）
49	- 运行时长 < 5 分钟（初始化阶段崩溃）
50	- tail 日志中未见明确 Traceback 或错误行
51	- 同类实验连续失败 ≥ 2 次
52	
53	```python
54	spawn_worker(
55	    task_type="diagnose:{exp_id}",
56	    task_prompt="""SSH 到服务器 {server}，诊断实验 {exp_id} 的失败原因。
57	
58	项目路径：{project_path}（绝对路径）
59	日志路径：{log_path}（可能为空）
60	
61	执行步骤（按顺序，有结论就停）：
62	
63	1. 如果有日志路径：
64	   - 先看结尾 50 行（找 Traceback / Error / CUDA OOM）
65	   - 没找到明确错误：再看开头 100 行（初始化崩溃在这里）
66	   - 日志文件不存在：说明任务启动即失败，跳到步骤 2
67	
68	2. 日志无错误或无日志时，检查基础设施：
69	   - 入口文件是否存在
70	   - 激活环境并验证 import
71	   - 检查 configs/ 目录
72	
73	3. 检查磁盘/内存（OOM 类）
74	
75	最后输出一行 JSON：
76	{"root_cause":"<引用具体报错行>","error_type":"infrastructure|hyperparameter|resource|data","fix_steps":["步骤1","步骤2"],"can_auto_fix":true}""",
77	    tool_groups=["ssh"],
78	)
79	```
80	
81	Worker 返回后，以其结论作为 Step 3 的诊断依据。
82	
83	### Step 3: 诊断 + 行动
84	根据 `error_type` 决定：
85	- **infrastructure**（文件缺失/import error/配置语法）→ spawn_worker 修复，修复后重提交（自主修复最多 1 次，再失败则停止告知用户）。注意：此重试策略仅适用于训练实验，数据生成任务的重试策略参见 `on-datagen-done` 的 Step 9。
86	  - spawn_worker 后立即：`update_registry(exp_id, "notes", "fix_worker_id: {worker_id}")`，确保关联可追溯
87	- **hyperparameter/架构**（loss 不降、指标差）→ 给具体调整建议，用户决定
88	- **resource**（OOM、GPU 不够）→ 给配置调整建议，用户确认
89	- **data**（路径、格式）→ spawn_worker 检查，能自修则修，不能则告知用户
90	
91	### Step 4: 更新 registry
92	- update_registry(exp_id, "notes", "失败原因: ... | 已有成果: ... | 建议: ...")
93	- update_registry(exp_id, "conclusion", "failed")
94	- update_registry(exp_id, "status", "DONE")
95	
96	### Step 5: 发送飞书结果卡片
97	- feishu_send_result_card(exp_id, conclusion="failed", key_metrics, baseline_comparison)
98	  - key_metrics：从 registry 取已有 metrics，没有则传空 dict
99	  - baseline_comparison：Step 3 的诊断摘要
100	
101	### Step 6: 提炼 insight + 更新文档
102	
103	**写入 memory.md（新失败模式才写，避免重复）**：
104	如果 root_cause 是之前未记录的模式（Step 0 读 memory.md 时没有看到），用 `save_memory` 追加：
105	```
106	- [失败模式] {error_type}：{root_cause 一句话摘要} → 修复方案：{fix_steps 摘要}
107	```
108	例：`- [失败模式] GPU 硬件：GPU 7 CUDA capability 检查失败，device=7, num_gpus=7 → 设置 CUDA_VISIBLE_DEVICES 跳过 GPU 7`
109	这样下次同类实验失败时，Step 0 读 memory.md 就能直接命中，跳过通用诊断流程。
110	
111	**更新 ideas.md（有价值的 insight 才写）**：
112	- AMP 崩溃反复出现 → `append_idea` 记录调参方向
113	- 部分 metrics 有价值但后期崩溃 → `append_idea` 记录调优方向
114	
115	更新 ideas.md IN_PROGRESS → DEAD ENDS：
116	- move_idea(from_section="IN_PROGRESS（进行中）", to_section="DEAD ENDS（已确认死路）", index=N)
117	- 找不到对应条目：跳过
118	
119	### Step 6.5: 更新 report.md
120	
121	report.md 由系统根据 registry 状态自动生成，无需手动调用 `save_project_file`。Step 4 更新 registry 后，report 会自动刷新并在 ## 告警 区块突出标注本次失败。
122	
123	### Step 7: 回复
124	生成失败报告：exp_id、失败原因（引用具体错误行）、已有成果、具体建议。
125	
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "parentUuid": "d785f1df-e3bc-49bc-bc24-053a78e337c4",
  "isSidechain": false,
  "promptId": "d2210c4d-d5b9-450f-8450-2f1ffe6e0ccd",
  "type": "user",
  "uuid": "8e2259fc-f338-4819-bd9e-721b3ef1ab12",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/agent-ml-research/skills/global/on-experiment-failed.skill.md",
      "content": "---\nname: on-experiment-failed\ndescription: 实验失败后的自动诊断工作流——查日志分析原因、更新 registry、通知 Director。[CRON] 实验失败消息到达时使用。\nscope: global\ntags:\n- workflow\n- diagnosis\n- cron-hook\ntools:\n- read_registry\n- tail_training_logs\n- update_registry\n- append_idea\n- feishu_send_result_card\n- spawn_worker\n- check_job_status\nversion: 4\nheavy: true\nroles:\n- agent\n---\n\n# 实验失败诊断工作流\n\n## 触发方式\n由 cron hook 自动触发：进程退出且 W&B 无数据 / W&B state=failed/crashed / NaN 检测到。\n\n## 步骤\n\n### Step 0: 读取项目上下文（诊断前必须执行）\n先读文档，再看日志——否则诊断方向可能完全错误：\n\n- `read_project_file(\"memory.md\")` — **最重要**：查是否有相同失败模式的历史记录和已知修复方案\n- Worker 通过 `list_repo_tree` + `read_repo_file` 按需从代码仓库读取训练脚本结构\n\n读完后检查：\n- memory.md 里有没有\"此类实验曾失败，原因是 X\"的记录？→ 直接按已知方案诊断，跳过 Step 2 通用流程\n- 代码仓库中的训练入口和参数格式是否与本次实验配置匹配？（Worker 可用 `list_repo_tree` + `read_repo_file` 查看）\n\n### Step 1: 了解失败背景\n- read_registry(exp_id) — 查看状态、conclusion、notes、metrics、log_path\n\n### Step 2: 浅层日志诊断\n有 log_path 时：tail_training_logs(server, **绝对路径**, lines=80)\n- 寻找：OOM、CUDA error、NaN、assertion error、数据加载错误、Python Traceback\n- 没找到 → 增加行数再查\n\n### Step 2.5: 深查（满足以下任一条件时 spawn_worker）\n- 运行时长 < 5 分钟（初始化阶段崩溃）\n- tail 日志中未见明确 Traceback 或错误行\n- 同类实验连续失败 ≥ 2 次\n\n```python\nspawn_worker(\n    task_type=\"diagnose:{exp_id}\",\n    task_prompt=\"\"\"SSH 到服务器 {server}，诊断实验 {exp_id} 的失败原因。\n\n项目路径：{project_path}（绝对路径）\n日志路径：{log_path}（可能为空）\n\n执行步骤（按顺序，有结论就停）：\n\n1. 如果有日志路径：\n   - 先看结尾 50 行（找 Traceback / Error / CUDA OOM）\n   - 没找到明确错误：再看开头 100 行（初始化崩溃在这里）\n   - 日志文件不存在：说明任务启动即失败，跳到步骤 2\n\n2. 日志无错误或无日志时，检查基础设施：\n   - 入口文件是否存在\n   - 激活环境并验证 import\n   - 检查 configs/ 目录\n\n3. 检查磁盘/内存（OOM 类）\n\n最后输出一行 JSON：\n{\"root_cause\":\"<引用具体报错行>\",\"error_type\":\"infrastructure|hyperparameter|resource|data\",\"fix_steps\":[\"步骤1\",\"步骤2\"],\"can_auto_fix\":true}\"\"\",\n    tool_groups=[\"ssh\"],\n)\n```\n\nWorker 返回后，以其结论作为 Step 3 的诊断依据。\n\n### Step 3: 诊断 + 行动\n根据 `error_type` 决定：\n- **infrastructure**（文件缺失/import error/配置语法）→ spawn_worker 修复，修复后重提交（自主修复最多 1 次，再失败则停止告知用户）。注意：此重试策略仅适用于训练实验，数据生成任务的重试策略参见 `on-datagen-done` 的 Step 9。\n  - spawn_worker 后立即：`update_registry(exp_id, \"notes\", \"fix_worker_id: {worker_id}\")`，确保关联可追溯\n- **hyperparameter/架构**（loss 不降、指标差）→ 给具体调整建议，用户决定\n- **resource**（OOM、GPU 不够）→ 给配置调整建议，用户确认\n- **data**（路径、格式）→ spawn_worker 检查，能自修则修，不能则告知用户\n\n### Step 4: 更新 registry\n- update_registry(exp_id, \"notes\", \"失败原因: ... | 已有成果: ... | 建议: ...\")\n- update_registry(exp_id, \"conclusion\", \"failed\")\n- update_registry(exp_id, \"status\", \"DONE\")\n\n### Step 5: 发送飞书结果卡片\n- feishu_send_result_card(exp_id, conclusion=\"failed\", key_metrics, baseline_comparison)\n  - key_metrics：从 registry 取已有 metrics，没有则传空 dict\n  - baseline_comparison：Step 3 的诊断摘要\n\n### Step 6: 提炼 insight + 更新文档\n\n**写入 memory.md（新失败模式才写，避免重复）**：\n如果 root_cause 是之前未记录的模式（Step 0 读 memory.md 时没有看到），用 `save_memory` 追加：\n```\n- [失败模式] {error_type}：{root_cause 一句话摘要} → 修复方案：{fix_steps 摘要}\n```\n例：`- [失败模式] GPU 硬件：GPU 7 CUDA capability 检查失败，device=7, num_gpus=7 → 设置 CUDA_VISIBLE_DEVICES 跳过 GPU 7`\n这样下次同类实验失败时，Step 0 读 memory.md 就能直接命中，跳过通用诊断流程。\n\n**更新 ideas.md（有价值的 insight 才写）**：\n- AMP 崩溃反复出现 → `append_idea` 记录调参方向\n- 部分 metrics 有价值但后期崩溃 → `append_idea` 记录调优方向\n\n更新 ideas.md IN_PROGRESS → DEAD ENDS：\n- move_idea(from_section=\"IN_PROGRESS（进行中）\", to_section=\"DEAD ENDS（已确认死路）\", index=N)\n- 找不到对应条目：跳过\n\n### Step 6.5: 更新 report.md\n\nreport.md 由系统根据 registry 状态自动生成，无需手动调用 `save_project_file`。Step 4 更新 registry 后，report 会自动刷新并在 ## 告警 区块突出标注本次失败。\n\n### Step 7: 回复\n生成失败报告：exp_id、失败原因（引用具体错误行）、已有成果、具体建议。\n",
      "numLines": 125,
      "startLine": 1,
      "totalLines": 125
    }
  },
  "sourceToolAssistantUUID": "d785f1df-e3bc-49bc-bc24-053a78e337c4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/agent_5c567c58",
  "sessionId": "bb8bc777-37fb-4956-b48e-5e9c5a98dd73",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
````

</details>

---

### Runtime record

_source line 56 · 2026-05-20T19:15:09.913Z_

```json
{
  "parentUuid": "8e2259fc-f338-4819-bd9e-721b3ef1ab12",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "827d4a50-5bc5-4ff6-910a-e52814e43c4d",
  "timestamp": "2026-05-20T19:15:09.913Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/agent_5c567c58",
  "sessionId": "bb8bc777-37fb-4956-b48e-5e9c5a98dd73",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 57_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[CRON] 实验进程异常退出（失败），需要你诊断原因。 详情: Process exited without valid W&B metrics  - exp_id: exp_b1_scd_fewnerd_standard - project: struct_self_consist_ie - server: autodl-5090-b - log_path: /root/autodl-tmp/…",
  "leafUuid": "827d4a50-5bc5-4ff6-910a-e52814e43c4d",
  "sessionId": "bb8bc777-37fb-4956-b48e-5e9c5a98dd73"
}
```

---

### Runtime record

_source line 58_

```json
{
  "type": "ai-title",
  "aiTitle": "Diagnose experiment process exit failure",
  "sessionId": "bb8bc777-37fb-4956-b48e-5e9c5a98dd73"
}
```

---

### Assistant

_source line 59 · 2026-05-20T19:15:25.581Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have the full on-experiment-failed skill. Let me follow the steps:

1. Step 0: Read memory.md for known failure patterns
2. Step 1: Already have registry info — status DONE, conclusion failed, "process dead 5× with no sentinel/W&B — auto-resolved as failed"
3. Step 2/2.5: Need to spawn Worker to diagnose via SSH

The experiment details:
- exp_id: exp_b1_scd_fewnerd_standard
- server: autodl-5090-b


- log_path: /root/autodl-tmp/struct_self_consist_ie/logs/exp_b1_scd_fewnerd_standard.log
- command: llamafactory-cli train train_config_scd_fewnerd_s42.yaml
- PID: 207109

I'm noticing a pattern here — exp_b1_scd_fewnerd_curriculum_q failed with the same symptoms and already has a diagnose Worker running. Two SCD experiments on the same server both crashing suggests something systemic. I'll check memory.md for prior failure patterns and spawn a diagnose Worker for this one too.

Wait, looking back at the report, exp_b1_scd_fewnerd_curriculum_q was actually marked as a false positive — it completed successfully with 4706 steps and a loss of 0.023, but the cron thought it failed. This could be exactly what's happening with the standard experiment too.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "827d4a50-5bc5-4ff6-910a-e52814e43c4d",
  "isSidechain": false,
  "requestId": "req_011CbEMaZm2Sw8ugo3yn2i1K",
  "type": "assistant",
  "uuid": "7ac9d955-a23a-4a7c-974e-96574fa54b59",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/agent_5c567c58",
  "sessionId": "bb8bc777-37fb-4956-b48e-5e9c5a98dd73",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019Anhhi8QCDf7m2qpX56pEM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2517,
      "cache_read_input_tokens": 54364,
      "output_tokens": 746,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2517,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 746,
          "cache_read_input_tokens": 54364,
          "cache_creation_input_tokens": 2517,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2517
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

_source line 60 · 2026-05-20T19:15:26.215Z_

注意到 `exp_b1_scd_fewnerd_curriculum_q` 之前也被标记为 failed 但后来发现是 cron false positive（实际训练完成 4706/4706 steps）。`exp_b1_scd_fewnerd_standard` 可能是同样的情况。先读 memory.md 查历史模式，同时派 Worker 诊断。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7ac9d955-a23a-4a7c-974e-96574fa54b59",
  "isSidechain": false,
  "requestId": "req_011CbEMaZm2Sw8ugo3yn2i1K",
  "type": "assistant",
  "uuid": "0648fc31-c249-4c65-84cf-b90e98b5ef2f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/agent_5c567c58",
  "sessionId": "bb8bc777-37fb-4956-b48e-5e9c5a98dd73",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019Anhhi8QCDf7m2qpX56pEM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2517,
      "cache_read_input_tokens": 54364,
      "output_tokens": 746,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2517,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 746,
          "cache_read_input_tokens": 54364,
          "cache_creation_input_tokens": 2517,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2517
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

_source line 61 · 2026-05-20T19:15:27.209Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_012PJvwHoox1uaVTtaWrYH37`</summary>

```json
{
  "project": "struct_self_consist_ie",
  "file": "memory.md",
  "max_chars": 12000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0648fc31-c249-4c65-84cf-b90e98b5ef2f",
  "isSidechain": false,
  "requestId": "req_011CbEMaZm2Sw8ugo3yn2i1K",
  "type": "assistant",
  "uuid": "00a6f37a-45a7-4500-8856-5d4224891888",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/agent_5c567c58",
  "sessionId": "bb8bc777-37fb-4956-b48e-5e9c5a98dd73",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019Anhhi8QCDf7m2qpX56pEM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2517,
      "cache_read_input_tokens": 54364,
      "output_tokens": 746,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2517,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 746,
          "cache_read_input_tokens": 54364,
          "cache_creation_input_tokens": 2517,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2517
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

_source line 62 · 2026-05-20T19:15:28.496Z_

<details><summary>↩ Tool result · `toolu_013TmtCfxvpDp8vjPMKsBc15`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__tail_training_logs"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__check_job_status"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__feishu_send_result_card"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__get_project_resource_usage"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0e7eab39-2f4b-4908-8012-2c2cb9a2595c",
  "isSidechain": false,
  "promptId": "d2210c4d-d5b9-450f-8450-2f1ffe6e0ccd",
  "type": "user",
  "uuid": "06fe21d2-b812-4f5f-81f9-ddf906b238bc",
  "toolUseResult": {
    "matches": [
      "mcp__agent-ml-research__tail_training_logs",
      "mcp__agent-ml-research__check_job_status",
      "mcp__agent-ml-research__feishu_send_result_card",
      "mcp__agent-ml-research__get_project_resource_usage"
    ],
    "query": "select:mcp__agent-ml-research__tail_training_logs,mcp__agent-ml-research__check_job_status,mcp__agent-ml-research__feishu_send_result_card,mcp__agent-ml-research__get_project_resource_usage",
    "total_deferred_tools": 82
  },
  "sourceToolAssistantUUID": "0e7eab39-2f4b-4908-8012-2c2cb9a2595c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/agent_5c567c58",
  "sessionId": "bb8bc777-37fb-4956-b48e-5e9c5a98dd73",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 63 · 2026-05-20T19:15:27.232Z_

<details><summary>↩ Tool result · `toolu_012PJvwHoox1uaVTtaWrYH37`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/memory.md\", \"content\": \"# Memory\\n\\n## exp_qwen25_72b_fewshot 完整结果（2026-05-20）\\n\\n实验于 2026-05-20 08:47 完成。模型：Qwen2.5-72B-Instruct-AWQ, 3-shot, N=8 samples, seed=42。\\n\\n### ZS vs FS 完整对比表\\n\\n| Dataset  | Regime | N inst | Degen% | LP ρ   | SJ ρ  | FK ρ  | VC ρ  | EM ρ  | Greedy F1 | Oracle F1 | LP-wt F1 | LP Δ (pp) | p-value |\\n|----------|--------|--------|--------|--------|-------|-------|-------|-------|-----------|-----------|----------|-----------|---------|\\n| SciERC   | ZS     | 529    | 21.0%  | 0.081  | 0.217 | 0.227 | 0.277 | 0.181 | 0.399     | 0.549     | 0.415    | +1.53     | 0.008** |\\n| SciERC   | FS     | 529    | 16.6%  | 0.060  | 0.293 | 0.301 | 0.258 | 0.205 | 0.461     | 0.604     | 0.461    | -0.08     | 0.544   |\\n| CoNLL    | ZS     | 2756   | 67.7%  | -0.002 | 0.304 | 0.302 | 0.297 | 0.281 | 0.712     | 0.765     | 0.708    | -0.37     | n/a     |\\n| CoNLL    | FS     | 2756   | 70.0%  | 0.106  | 0.442 | 0.451 | 0.426 | 0.403 | 0.745     | 0.796     | 0.745    | +0.03     | 0.417   |\\n| FewNERD  | ZS     | 32565  | 46.2%  | 0.119  | 0.345 | 0.321 | 0.416 | 0.303 | 0.628     | 0.707     | 0.626    | -0.20     | n/a     |\\n| FewNERD  | FS     | 32565  | 45.2%  | 0.161  | 0.345 | 0.327 | 0.410 | 0.302 | 0.619     | 0.702     | 0.619    | +0.02     | 0.401   |\\n\\n### Dual-gating hypothesis 评估\\n\\nDual-gating 在 FT+ZS regime 内成立（6/6 条件一致）。FS regime 引入独立失效因素（LP 退化），不构成对 dual-gating 的挑战。\\n\\n### Error Correlation 分析\\n\\\"Demonstration-induced error correlation\\\" 假说缺乏实证支持（FS Jaccard ≈ ZS，CoNLL FS entropy 反而更高）。替代解释：LP signal 在 FS 下区分力退化是 construction 失效的直接原因。\\n\\n## F1 Scaling Law 写作约束（Director 2026-05-20）\\n\\n1. 不报 c 均值 — 分数据集：SciERC c≈0.35, FewNERD c≈0.61\\n2. CoNLL 只报 a 和 b，不报 c（c_se 太大）\\n3. 这是 oracle ceiling scaling，不是 achievable\\n4. LLaMA/FewNERD 仅 4 点拟合 → appendix 注明过拟合风险\\n5. N=1 低于 greedy 需解释（T=1 采样噪声 vs T=0 确定性）\\n\\n## CPU 分析实验汇总（2026-05-20）\\n\\n### E2 Mixture-of-Signals Ensemble\\n- Selection: 5-signal ensemble +0.72pp (p=0.000 ✓); Construction: 无效\\n- LP 占主导 (0.8), VC 为互补信号\\n\\n### E2v2 Per-Regime Ensemble Weights\\n- FT (all): LP=0.9, VC=0.1 → +0.30pp; Qwen3-8B: LP=0.8, VC=0.2 (+0.64pp)\\n- LOO 完全稳定 (10次权重不变)\\n\\n### I Diversity Predictor\\n- Cross-model JSD 强预测 ΔF1（CoNLL ρ=-0.615, R²=0.74）\\n- Within-model diversity 不显著\\n\\n### J Calibration + Conformal\\n- ECE: SciERC 0.098 (overconfident), CoNLL/FewNERD well-calibrated\\n- Conformal 仅 CoNLL 达标 (coverage=0.925)，失败因 recall ceiling\\n\\n## B2 Entity Verifier — D189 OOF 最终结论（2026-05-20）\\n\\n**原始 +3.62pp 中 91% 是 train-on-test 泄露。**\\n\\n| Method | F1 | vs Greedy |\\n|--------|-----|-----------|\\n| Greedy | 0.8216 | — |\\n| Majority Vote | 0.8048 | -1.68pp |\\n| OOF Path A | 0.8246 | **+0.30pp** (not significant) |\\n| OOF Path B | 0.8059 | -1.57pp |\\n\\nPer-dataset: SciERC +1.28pp, CoNLL +0.55pp, FewNERD +0.02pp (≈0)。\\n**B2 verifier 不适合论文 §5 main text。** Registry conclusion: negative.\\n\\n### B2-v2 Multi-Domain Joint Training（2026-05-20）\\n- Joint training (CoNLL+SciERC→FewNERD): AUC 0.8335→0.8477 (+0.014)\\n- **但 F1 delta 仍为负** (-0.008)，AUC 未转化为下游收益\\n- 核心问题：cross-domain ECE=0.136 (IID 仅 0.007)，概率 miscalibrated\\n- 最具判别力 features (vc, sj) 跨域稳定性最差 (std=0.12-0.14)\\n\\n## N Inverse Scaling — 数据验证完成（2026-05-20）\\n\\n- 58 inverse scaling transitions, 40 显著 (paired bootstrap)\\n- 核心机制: θ=2/N 随 N 增大变过于宽松 → precision 崩塌\\n- majority_vote (θ=0.5) 几乎完全免疫\\n- **n=4351 验证通过**: exp_027_fewnerd_n16 是 5000 instance subset (4 shards × 1250)，gold_filter 后 4351。subset F1=0.7926 vs full F1=0.7913 (+0.13pp)，具有代表性。论文引用时注明 subset (n=4351/32565)。\\n\\n## K Robustness Reviewer 反馈（2026-05-20, sprint 后处理）\\n\\n1. 注册实验到 registry\\n2. seed 789 路径命名不一致 — 确认来源\\n3. dropout 非单调性补充 ceil 函数交互解释\\n4. \\\"most robust = uniform\\\" 改 Pareto 分析\\n5. 论文限定为 single config（Qwen 7B FT FewNERD）\\n\\n## B1 SCD 实验决策记录（2026-05-20）\\n\\n- Q-variant 推迟: B2 verifier D189 leakage，等 OOF clean verifier。GPU 1 改跑 fallback seed=43。\\n- B2 verifier worker 未保存 .pkl/.joblib 模型文件。\\n- CoNLL control 训练完成 (690/690 steps, loss=0.0359)，cron 误判为 failed。待 eval inference。\\n\\n## 14B 推理诊断教训（2026-05-21）\\n\\n### PID 监控误报\\nexp_14b_inference_fewnerd / exp_14b_inference_scierc 被 cron 标记 \\\"process dead 5×\\\"，实际进程仍在运行。原因：注册的 PID 201001 是中间进程（已退出），实际推理在新 PID 217692→217960 下继续。**教训：注册 spec.pid 时用主 python 进程 PID 或 bash wrapper PID，不要用可能退出的中间进程 PID。**\\n\\n### 14B 模型单卡 5090 KV cache 极度不足\\n- 模型占 27.57 GiB / 32 GiB GPU，KV cache 仅 1.09 GiB（5920 tokens）\\n- 最大并发 2.89 个请求（max_seq_len=2048）\\n- 推理极慢但不会 OOM（vLLM 动态管理）\\n- **建议：14B 推理用 tensor_parallel=2（2 卡），释放约 14 GiB 给 KV cache**\\n\\n### enforce_eager 修复 EngineDeadError\\n早期 ckpt36000 运行未设 enforce_eager，CUDA graph + torch.compile 额外占内存 → 60% 进度 EngineDeadError 崩溃。当前 merged-final 运行加了 `enforce_eager=True`，稳定运行。**14B 单卡推理必须 enforce_eager。**\\n\\n## [失败模式] LLaMA-Factory 训练无 W&B → cron 误判 failed（2026-05-21）\\n\\nexp_b1_scd_fewnerd_curriculum_q 和 exp_b1_scd_conll_control 均被 cron 标记 \\\"process dead 5× with no sentinel/W&B\\\"，实际训练已正常完成。根因：LLaMA-Factory 训练未配置 W&B report_to，cron 监控依赖 W&B sentinel 判断完成状态，进程正常退出后被误判为 failed。**教训：LLaMA-Factory 训练配置中加 `report_to: wandb` 或至少确保 cron 有备用完成检测机制（如检查 checkpoint 目录的 trainer_state.json）。** 遇到此类 \\\"process dead + no W&B\\\" 失败时，优先检查日志尾部是否有正常完成的 train/eval metrics。\\n\", \"total_chars\": 5014, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "00a6f37a-45a7-4500-8856-5d4224891888",
  "isSidechain": false,
  "promptId": "d2210c4d-d5b9-450f-8450-2f1ffe6e0ccd",
  "type": "user",
  "uuid": "5090373b-83cf-4671-906c-21ec0b0ae699",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/memory.md\\\", \\\"content\\\": \\\"# Memory\\\\n\\\\n## exp_qwen25_72b_fewshot 完整结果（2026-05-20）\\\\n\\\\n实验于 2026-05-20 08:47 完成。模型：Qwen2.5-72B-Instruct-AWQ, 3-shot, N=8 samples, seed=42。\\\\n\\\\n### ZS vs FS 完整对比表\\\\n\\\\n| Dataset  | Regime | N inst | Degen% | LP ρ   | SJ ρ  | FK ρ  | VC ρ  | EM ρ  | Greedy F1 | Oracle F1 | LP-wt F1 | LP Δ (pp) | p-value |\\\\n|----------|--------|--------|--------|--------|-------|-------|-------|-------|-----------|-----------|----------|-----------|---------|\\\\n| SciERC   | ZS     | 529    | 21.0%  | 0.081  | 0.217 | 0.227 | 0.277 | 0.181 | 0.399     | 0.549     | 0.415    | +1.53     | 0.008** |\\\\n| SciERC   | FS     | 529    | 16.6%  | 0.060  | 0.293 | 0.301 | 0.258 | 0.205 | 0.461     | 0.604     | 0.461    | -0.08     | 0.544   |\\\\n| CoNLL    | ZS     | 2756   | 67.7%  | -0.002 | 0.304 | 0.302 | 0.297 | 0.281 | 0.712     | 0.765     | 0.708    | -0.37     | n/a     |\\\\n| CoNLL    | FS     | 2756   | 70.0%  | 0.106  | 0.442 | 0.451 | 0.426 | 0.403 | 0.745     | 0.796     | 0.745    | +0.03     | 0.417   |\\\\n| FewNERD  | ZS     | 32565  | 46.2%  | 0.119  | 0.345 | 0.321 | 0.416 | 0.303 | 0.628     | 0.707     | 0.626    | -0.20     | n/a     |\\\\n| FewNERD  | FS     | 32565  | 45.2%  | 0.161  | 0.345 | 0.327 | 0.410 | 0.302 | 0.619     | 0.702     | 0.619    | +0.02     | 0.401   |\\\\n\\\\n### Dual-gating hypothesis 评估\\\\n\\\\nDual-gating 在 FT+ZS regime 内成立（6/6 条件一致）。FS regime 引入独立失效因素（LP 退化），不构成对 dual-gating 的挑战。\\\\n\\\\n### Error Correlation 分析\\\\n\\\\\\\"Demonstration-induced error correlation\\\\\\\" 假说缺乏实证支持（FS Jaccard ≈ ZS，CoNLL FS entropy 反而更高）。替代解释：LP signal 在 FS 下区分力退化是 construction 失效的直接原因。\\\\n\\\\n## F1 Scaling Law 写作约束（Director 2026-05-20）\\\\n\\\\n1. 不报 c 均值 — 分数据集：SciERC c≈0.35, FewNERD c≈0.61\\\\n2. CoNLL 只报 a 和 b，不报 c（c_se 太大）\\\\n3. 这是 oracle ceiling scaling，不是 achievable\\\\n4. LLaMA/FewNERD 仅 4 点拟合 → appendix 注明过拟合风险\\\\n5. N=1 低于 greedy 需解释（T=1 采样噪声 vs T=0 确定性）\\\\n\\\\n## CPU 分析实验汇总（2026-05-20）\\\\n\\\\n### E2 Mixture-of-Signals Ensemble\\\\n- Selection: 5-signal ensemble +0.72pp (p=0.000 ✓); Construction: 无效\\\\n- LP 占主导 (0.8), VC 为互补信号\\\\n\\\\n### E2v2 Per-Regime Ensemble Weights\\\\n- FT (all): LP=0.9, VC=0.1 → +0.30pp; Qwen3-8B: LP=0.8, VC=0.2 (+0.64pp)\\\\n- LOO 完全稳定 (10次权重不变)\\\\n\\\\n### I Diversity Predictor\\\\n- Cross-model JSD 强预测 ΔF1（CoNLL ρ=-0.615, R²=0.74）\\\\n- Within-model diversity 不显著\\\\n\\\\n### J Calibration + Conformal\\\\n- ECE: SciERC 0.098 (overconfident), CoNLL/FewNERD well-calibrated\\\\n- Conformal 仅 CoNLL 达标 (coverage=0.925)，失败因 recall ceiling\\\\n\\\\n## B2 Entity Verifier — D189 OOF 最终结论（2026-05-20）\\\\n\\\\n**原始 +3.62pp 中 91% 是 train-on-test 泄露。**\\\\n\\\\n| Method | F1 | vs Greedy |\\\\n|--------|-----|-----------|\\\\n| Greedy | 0.8216 | — |\\\\n| Majority Vote | 0.8048 | -1.68pp |\\\\n| OOF Path A | 0.8246 | **+0.30pp** (not significant) |\\\\n| OOF Path B | 0.8059 | -1.57pp |\\\\n\\\\nPer-dataset: SciERC +1.28pp, CoNLL +0.55pp, FewNERD +0.02pp (≈0)。\\\\n**B2 verifier 不适合论文 §5 main text。** Registry conclusion: negative.\\\\n\\\\n### B2-v2 Multi-Domain Joint Training（2026-05-20）\\\\n- Joint training (CoNLL+SciERC→FewNERD): AUC 0.8335→0.8477 (+0.014)\\\\n- **但 F1 delta 仍为负** (-0.008)，AUC 未转化为下游收益\\\\n- 核心问题：cross-domain ECE=0.136 (IID 仅 0.007)，概率 miscalibrated\\\\n- 最具判别力 features (vc, sj) 跨域稳定性最差 (std=0.12-0.14)\\\\n\\\\n## N Inverse Scaling — 数据验证完成（2026-05-20）\\\\n\\\\n- 58 inverse scaling transitions, 40 显著 (paired bootstrap)\\\\n- 核心机制: θ=2/N 随 N 增大变过于宽松 → precision 崩塌\\\\n- majority_vote (θ=0.5) 几乎完全免疫\\\\n- **n=4351 验证通过**: exp_027_fewnerd_n16 是 5000 instance subset (4 shards × 1250)，gold_filter 后 4351。subset F1=0.7926 vs full F1=0.7913 (+0.13pp)，具有代表性。论文引用时注明 subset (n=4351/32565)。\\\\n\\\\n## K Robustness Reviewer 反馈（2026-05-20, sprint 后处理）\\\\n\\\\n1. 注册实验到 registry\\\\n2. seed 789 路径命名不一致 — 确认来源\\\\n3. dropout 非单调性补充 ceil 函数交互解释\\\\n4. \\\\\\\"most robust = uniform\\\\\\\" 改 Pareto 分析\\\\n5. 论文限定为 single config（Qwen 7B FT FewNERD）\\\\n\\\\n## B1 SCD 实验决策记录（2026-05-20）\\\\n\\\\n- Q-variant 推迟: B2 verifier D189 leakage，等 OOF clean verifier。GPU 1 改跑 fallback seed=43。\\\\n- B2 verifier worker 未保存 .pkl/.joblib 模型文件。\\\\n- CoNLL control 训练完成 (690/690 steps, loss=0.0359)，cron 误判为 failed。待 eval inference。\\\\n\\\\n## 14B 推理诊断教训（2026-05-21）\\\\n\\\\n### PID 监控误报\\\\nexp_14b_inference_fewnerd / exp_14b_inference_scierc 被 cron 标记 \\\\\\\"process dead 5×\\\\\\\"，实际进程仍在运行。原因：注册的 PID 201001 是中间进程（已退出），实际推理在新 PID 217692→217960 下继续。**教训：注册 spec.pid 时用主 python 进程 PID 或 bash wrapper PID，不要用可能退出的中间进程 PID。**\\\\n\\\\n### 14B 模型单卡 5090 KV cache 极度不足\\\\n- 模型占 27.57 GiB / 32 GiB GPU，KV cache 仅 1.09 GiB（5920 tokens）\\\\n- 最大并发 2.89 个请求（max_seq_len=2048）\\\\n- 推理极慢但不会 OOM（vLLM 动态管理）\\\\n- **建议：14B 推理用 tensor_parallel=2（2 卡），释放约 14 GiB 给 KV cache**\\\\n\\\\n### enforce_eager 修复 EngineDeadError\\\\n早期 ckpt36000 运行未设 enforce_eager，CUDA graph + torch.compile 额外占内存 → 60% 进度 EngineDeadError 崩溃。当前 merged-final 运行加了 `enforce_eager=True`，稳定运行。**14B 单卡推理必须 enforce_eager。**\\\\n\\\\n## [失败模式] LLaMA-Factory 训练无 W&B → cron 误判 failed（2026-05-21）\\\\n\\\\nexp_b1_scd_fewnerd_curriculum_q 和 exp_b1_scd_conll_control 均被 cron 标记 \\\\\\\"process dead 5× with no sentinel/W&B\\\\\\\"，实际训练已正常完成。根因：LLaMA-Factory 训练未配置 W&B report_to，cron 监控依赖 W&B sentinel 判断完成状态，进程正常退出后被误判为 failed。**教训：LLaMA-Factory 训练配置中加 `report_to: wandb` 或至少确保 cron 有备用完成检测机制（如检查 checkpoint 目录的 trainer_state.json）。** 遇到此类 \\\\\\\"process dead + no W&B\\\\\\\" 失败时，优先检查日志尾部是否有正常完成的 train/eval metrics。\\\\n\\\", \\\"total_chars\\\": 5014, \\\"truncated\\\": false}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/memory.md\", \"content\": \"# Memory\\n\\n## exp_qwen25_72b_fewshot 完整结果（2026-05-20）\\n\\n实验于 2026-05-20 08:47 完成。模型：Qwen2.5-72B-Instruct-AWQ, 3-shot, N=8 samples, seed=42。\\n\\n### ZS vs FS 完整对比表\\n\\n| Dataset  | Regime | N inst | Degen% | LP ρ   | SJ ρ  | FK ρ  | VC ρ  | EM ρ  | Greedy F1 | Oracle F1 | LP-wt F1 | LP Δ (pp) | p-value |\\n|----------|--------|--------|--------|--------|-------|-------|-------|-------|-----------|-----------|----------|-----------|---------|\\n| SciERC   | ZS     | 529    | 21.0%  | 0.081  | 0.217 | 0.227 | 0.277 | 0.181 | 0.399     | 0.549     | 0.415    | +1.53     | 0.008** |\\n| SciERC   | FS     | 529    | 16.6%  | 0.060  | 0.293 | 0.301 | 0.258 | 0.205 | 0.461     | 0.604     | 0.461    | -0.08     | 0.544   |\\n| CoNLL    | ZS     | 2756   | 67.7%  | -0.002 | 0.304 | 0.302 | 0.297 | 0.281 | 0.712     | 0.765     | 0.708    | -0.37     | n/a     |\\n| CoNLL    | FS     | 2756   | 70.0%  | 0.106  | 0.442 | 0.451 | 0.426 | 0.403 | 0.745     | 0.796     | 0.745    | +0.03     | 0.417   |\\n| FewNERD  | ZS     | 32565  | 46.2%  | 0.119  | 0.345 | 0.321 | 0.416 | 0.303 | 0.628     | 0.707     | 0.626    | -0.20     | n/a     |\\n| FewNERD  | FS     | 32565  | 45.2%  | 0.161  | 0.345 | 0.327 | 0.410 | 0.302 | 0.619     | 0.702     | 0.619    | +0.02     | 0.401   |\\n\\n### Dual-gating hypothesis 评估\\n\\nDual-gating 在 FT+ZS regime 内成立（6/6 条件一致）。FS regime 引入独立失效因素（LP 退化），不构成对 dual-gating 的挑战。\\n\\n### Error Correlation 分析\\n\\\"Demonstration-induced error correlation\\\" 假说缺乏实证支持（FS Jaccard ≈ ZS，CoNLL FS entropy 反而更高）。替代解释：LP signal 在 FS 下区分力退化是 construction 失效的直接原因。\\n\\n## F1 Scaling Law 写作约束（Director 2026-05-20）\\n\\n1. 不报 c 均值 — 分数据集：SciERC c≈0.35, FewNERD c≈0.61\\n2. CoNLL 只报 a 和 b，不报 c（c_se 太大）\\n3. 这是 oracle ceiling scaling，不是 achievable\\n4. LLaMA/FewNERD 仅 4 点拟合 → appendix 注明过拟合风险\\n5. N=1 低于 greedy 需解释（T=1 采样噪声 vs T=0 确定性）\\n\\n## CPU 分析实验汇总（2026-05-20）\\n\\n### E2 Mixture-of-Signals Ensemble\\n- Selection: 5-signal ensemble +0.72pp (p=0.000 ✓); Construction: 无效\\n- LP 占主导 (0.8), VC 为互补信号\\n\\n### E2v2 Per-Regime Ensemble Weights\\n- FT (all): LP=0.9, VC=0.1 → +0.30pp; Qwen3-8B: LP=0.8, VC=0.2 (+0.64pp)\\n- LOO 完全稳定 (10次权重不变)\\n\\n### I Diversity Predictor\\n- Cross-model JSD 强预测 ΔF1（CoNLL ρ=-0.615, R²=0.74）\\n- Within-model diversity 不显著\\n\\n### J Calibration + Conformal\\n- ECE: SciERC 0.098 (overconfident), CoNLL/FewNERD well-calibrated\\n- Conformal 仅 CoNLL 达标 (coverage=0.925)，失败因 recall ceiling\\n\\n## B2 Entity Verifier — D189 OOF 最终结论（2026-05-20）\\n\\n**原始 +3.62pp 中 91% 是 train-on-test 泄露。**\\n\\n| Method | F1 | vs Greedy |\\n|--------|-----|-----------|\\n| Greedy | 0.8216 | — |\\n| Majority Vote | 0.8048 | -1.68pp |\\n| OOF Path A | 0.8246 | **+0.30pp** (not significant) |\\n| OOF Path B | 0.8059 | -1.57pp |\\n\\nPer-dataset: SciERC +1.28pp, CoNLL +0.55pp, FewNERD +0.02pp (≈0)。\\n**B2 verifier 不适合论文 §5 main text。** Registry conclusion: negative.\\n\\n### B2-v2 Multi-Domain Joint Training（2026-05-20）\\n- Joint training (CoNLL+SciERC→FewNERD): AUC 0.8335→0.8477 (+0.014)\\n- **但 F1 delta 仍为负** (-0.008)，AUC 未转化为下游收益\\n- 核心问题：cross-domain ECE=0.136 (IID 仅 0.007)，概率 miscalibrated\\n- 最具判别力 features (vc, sj) 跨域稳定性最差 (std=0.12-0.14)\\n\\n## N Inverse Scaling — 数据验证完成（2026-05-20）\\n\\n- 58 inverse scaling transitions, 40 显著 (paired bootstrap)\\n- 核心机制: θ=2/N 随 N 增大变过于宽松 → precision 崩塌\\n- majority_vote (θ=0.5) 几乎完全免疫\\n- **n=4351 验证通过**: exp_027_fewnerd_n16 是 5000 instance subset (4 shards × 1250)，gold_filter 后 4351。subset F1=0.7926 vs full F1=0.7913 (+0.13pp)，具有代表性。论文引用时注明 subset (n=4351/32565)。\\n\\n## K Robustness Reviewer 反馈（2026-05-20, sprint 后处理）\\n\\n1. 注册实验到 registry\\n2. seed 789 路径命名不一致 — 确认来源\\n3. dropout 非单调性补充 ceil 函数交互解释\\n4. \\\"most robust = uniform\\\" 改 Pareto 分析\\n5. 论文限定为 single config（Qwen 7B FT FewNERD）\\n\\n## B1 SCD 实验决策记录（2026-05-20）\\n\\n- Q-variant 推迟: B2 verifier D189 leakage，等 OOF clean verifier。GPU 1 改跑 fallback seed=43。\\n- B2 verifier worker 未保存 .pkl/.joblib 模型文件。\\n- CoNLL control 训练完成 (690/690 steps, loss=0.0359)，cron 误判为 failed。待 eval inference。\\n\\n## 14B 推理诊断教训（2026-05-21）\\n\\n### PID 监控误报\\nexp_14b_inference_fewnerd / exp_14b_inference_scierc 被 cron 标记 \\\"process dead 5×\\\"，实际进程仍在运行。原因：注册的 PID 201001 是中间进程（已退出），实际推理在新 PID 217692→217960 下继续。**教训：注册 spec.pid 时用主 python 进程 PID 或 bash wrapper PID，不要用可能退出的中间进程 PID。**\\n\\n### 14B 模型单卡 5090 KV cache 极度不足\\n- 模型占 27.57 GiB / 32 GiB GPU，KV cache 仅 1.09 GiB（5920 tokens）\\n- 最大并发 2.89 个请求（max_seq_len=2048）\\n- 推理极慢但不会 OOM（vLLM 动态管理）\\n- **建议：14B 推理用 tensor_parallel=2（2 卡），释放约 14 GiB 给 KV cache**\\n\\n### enforce_eager 修复 EngineDeadError\\n早期 ckpt36000 运行未设 enforce_eager，CUDA graph + torch.compile 额外占内存 → 60% 进度 EngineDeadError 崩溃。当前 merged-final 运行加了 `enforce_eager=True`，稳定运行。**14B 单卡推理必须 enforce_eager。**\\n\\n## [失败模式] LLaMA-Factory 训练无 W&B → cron 误判 failed（2026-05-21）\\n\\nexp_b1_scd_fewnerd_curriculum_q 和 exp_b1_scd_conll_control 均被 cron 标记 \\\"process dead 5× with no sentinel/W&B\\\"，实际训练已正常完成。根因：LLaMA-Factory 训练未配置 W&B report_to，cron 监控依赖 W&B sentinel 判断完成状态，进程正常退出后被误判为 failed。**教训：LLaMA-Factory 训练配置中加 `report_to: wandb` 或至少确保 cron 有备用完成检测机制（如检查 checkpoint 目录的 trainer_state.json）。** 遇到此类 \\\"process dead + no W&B\\\" 失败时，优先检查日志尾部是否有正常完成的 train/eval metrics。\\n\", \"total_chars\": 5014, \"truncated\": false}, \"error\": null, \"metadata\": {}}"
    }
  },
  "sourceToolAssistantUUID": "00a6f37a-45a7-4500-8856-5d4224891888",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/agent_5c567c58",
  "sessionId": "bb8bc777-37fb-4956-b48e-5e9c5a98dd73",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 64 · 2026-05-20T19:15:28.488Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_013TmtCfxvpDp8vjPMKsBc15`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__tail_training_logs,mcp__agent-ml-research__check_job_status,mcp__agent-ml-research__feishu_send_result_card,mcp__agent-ml-research__get_project_resource_usage",
  "max_results": 4
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5090373b-83cf-4671-906c-21ec0b0ae699",
  "isSidechain": false,
  "requestId": "req_011CbEMaZm2Sw8ugo3yn2i1K",
  "type": "assistant",
  "uuid": "0e7eab39-2f4b-4908-8012-2c2cb9a2595c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/agent_5c567c58",
  "sessionId": "bb8bc777-37fb-4956-b48e-5e9c5a98dd73",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019Anhhi8QCDf7m2qpX56pEM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2517,
      "cache_read_input_tokens": 54364,
      "output_tokens": 746,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2517,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 746,
          "cache_read_input_tokens": 54364,
          "cache_creation_input_tokens": 2517,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2517
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

_source line 65 · 2026-05-20T19:15:40.528Z_

<details><summary>Logged reasoning block</summary>

```text
Memory.md has a crucial entry:

> ## [失败模式] LLaMA-Factory 训练无 W&B → cron 误判 failed（2026-05-21）
> 
> exp_b1_scd_fewnerd_curriculum_q 和 exp_b1_scd_conll_control 均被 cron 标记 "process dead 5× with no sentinel/W&B"，实际训练已正常完成。根因：LLaMA-Factory 训练未配置 W&B report_to，cron 监控依赖 W&B sentinel 判断完成状态，进程正常退出后被误判为 failed。

The fix is to add `report_to: wandb` to LLaMA-Factory configs or implement a fallback completion check like monitoring the trainer_state.json in the checkpoint directory. When I see "process dead + no W&B" failures, I should check the log tail for normal training metrics to confirm actual completion. Now I'm noticing `exp_b1_scd_fewnerd_standard` is hitting the exact same pattern.

Since memory.md already documents this failure type and its solution, I can skip the generic troubleshooting and go straight to checking the log tail to verify if training actually finished successfully, just like I did for curriculum_q.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "06fe21d2-b812-4f5f-81f9-ddf906b238bc",
  "isSidechain": false,
  "requestId": "req_011CbEMbwFNVVmkczkrqVGXa",
  "type": "assistant",
  "uuid": "ea29eb1d-7e5d-4194-87ba-8877171ae532",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/agent_5c567c58",
  "sessionId": "bb8bc777-37fb-4956-b48e-5e9c5a98dd73",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ts5YKTSVfXR31CqALKCvH4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 4938,
      "cache_read_input_tokens": 56881,
      "output_tokens": 704,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4938,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 704,
          "cache_read_input_tokens": 56881,
          "cache_creation_input_tokens": 4938,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4938
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

_source line 66 · 2026-05-20T19:15:40.911Z_

memory.md 有完全匹配的已知模式：**LLaMA-Factory 训练无 W&B → cron 误判 failed**。`exp_b1_scd_fewnerd_curriculum_q` 之前就是同样情况——训练实际完成但被误标 failed。直接检查日志尾部确认是否正常完成。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ea29eb1d-7e5d-4194-87ba-8877171ae532",
  "isSidechain": false,
  "requestId": "req_011CbEMbwFNVVmkczkrqVGXa",
  "type": "assistant",
  "uuid": "53f3fc7b-dbbe-45e9-bb57-01bb6a068e7c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/agent_5c567c58",
  "sessionId": "bb8bc777-37fb-4956-b48e-5e9c5a98dd73",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ts5YKTSVfXR31CqALKCvH4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 4938,
      "cache_read_input_tokens": 56881,
      "output_tokens": 704,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4938,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 704,
          "cache_read_input_tokens": 56881,
          "cache_creation_input_tokens": 4938,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4938
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

_source line 67 · 2026-05-20T19:15:42.477Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__tail_training_logs · `toolu_0121ccJJ6hyG6BVHhfHtwWhK`</summary>

```json
{
  "server": "autodl-5090-b",
  "log_path": "/root/autodl-tmp/struct_self_consist_ie/logs/exp_b1_scd_fewnerd_standard.log",
  "n": 80
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "53f3fc7b-dbbe-45e9-bb57-01bb6a068e7c",
  "isSidechain": false,
  "requestId": "req_011CbEMbwFNVVmkczkrqVGXa",
  "type": "assistant",
  "uuid": "41d8dd85-3247-419e-9119-48474eb35558",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/agent_5c567c58",
  "sessionId": "bb8bc777-37fb-4956-b48e-5e9c5a98dd73",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ts5YKTSVfXR31CqALKCvH4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 4938,
      "cache_read_input_tokens": 56881,
      "output_tokens": 704,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4938,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 704,
          "cache_read_input_tokens": 56881,
          "cache_creation_input_tokens": 4938,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4938
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

### Runtime record

_source line 68_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[CRON] 实验进程异常退出（失败），需要你诊断原因。 详情: Process exited without valid W&B metrics  - exp_id: exp_b1_scd_fewnerd_standard - project: struct_self_consist_ie - server: autodl-5090-b - log_path: /root/autodl-tmp/…",
  "leafUuid": "41d8dd85-3247-419e-9119-48474eb35558",
  "sessionId": "bb8bc777-37fb-4956-b48e-5e9c5a98dd73"
}
```

---

### Runtime record

_source line 69_

```json
{
  "type": "ai-title",
  "aiTitle": "Diagnose experiment process exit failure",
  "sessionId": "bb8bc777-37fb-4956-b48e-5e9c5a98dd73"
}
```

---

### Tool result

_source line 70 · 2026-05-20T19:15:42.999Z_

<details><summary>↩ Tool result · `toolu_0121ccJJ6hyG6BVHhfHtwWhK`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"lines\": [\"\\\"full_attention\\\",\", \"    \\\"full_attention\\\",\", \"    \\\"full_attention\\\",\", \"    \\\"full_attention\\\",\", \"    \\\"full_attention\\\",\", \"    \\\"full_attention\\\",\", \"    \\\"full_attention\\\",\", \"    \\\"full_attention\\\",\", \"    \\\"full_attention\\\",\", \"    \\\"full_attention\\\",\", \"    \\\"full_attention\\\",\", \"    \\\"full_attention\\\",\", \"    \\\"full_attention\\\",\", \"    \\\"full_attention\\\",\", \"    \\\"full_attention\\\",\", \"    \\\"full_attention\\\",\", \"    \\\"full_attention\\\",\", \"    \\\"full_attention\\\",\", \"    \\\"full_attention\\\",\", \"    \\\"full_attention\\\",\", \"    \\\"full_attention\\\",\", \"    \\\"full_attention\\\",\", \"    \\\"full_attention\\\",\", \"    \\\"full_attention\\\",\", \"    \\\"full_attention\\\",\", \"    \\\"full_attention\\\",\", \"    \\\"full_attention\\\",\", \"    \\\"full_attention\\\",\", \"    \\\"full_attention\\\",\", \"    \\\"full_attention\\\",\", \"    \\\"full_attention\\\",\", \"    \\\"full_attention\\\",\", \"    \\\"full_attention\\\",\", \"    \\\"full_attention\\\",\", \"    \\\"full_attention\\\"\", \"  ],\", \"  \\\"max_position_embeddings\\\": 40960,\", \"  \\\"max_window_layers\\\": 36,\", \"  \\\"model_type\\\": \\\"qwen3\\\",\", \"  \\\"num_attention_heads\\\": 32,\", \"  \\\"num_hidden_layers\\\": 36,\", \"  \\\"num_key_value_heads\\\": 8,\", \"  \\\"rms_norm_eps\\\": 1e-06,\", \"  \\\"rope_scaling\\\": null,\", \"  \\\"rope_theta\\\": 1000000,\", \"  \\\"sliding_window\\\": null,\", \"  \\\"tie_word_embeddings\\\": false,\", \"  \\\"transformers_version\\\": \\\"4.57.1\\\",\", \"  \\\"use_cache\\\": true,\", \"  \\\"use_sliding_window\\\": false,\", \"  \\\"vocab_size\\\": 151936\", \"}\", \"\", \"[INFO|tokenization_utils_base.py:2421] 2026-05-21 02:53:24,398 >> chat template saved in /root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen3-8b-fewnerd-scd-lora/chat_template.jinja\", \"[INFO|tokenization_utils_base.py:2590] 2026-05-21 02:53:24,398 >> tokenizer config file saved in /root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen3-8b-fewnerd-scd-lora/tokenizer_config.json\", \"[INFO|tokenization_utils_base.py:2599] 2026-05-21 02:53:24,398 >> Special tokens file saved in /root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen3-8b-fewnerd-scd-lora/special_tokens_map.json\", \"[INFO|trainer.py:4643] 2026-05-21 02:53:24,498 >> \", \"***** Running Evaluation *****\", \"[INFO|trainer.py:4645] 2026-05-21 02:53:24,498 >>   Num examples = 18824\", \"[INFO|trainer.py:4648] 2026-05-21 02:53:24,498 >>   Batch size = 4\", \"{'eval_loss': 0.03392118960618973, 'eval_runtime': 619.073, 'eval_samples_per_second': 30.407, 'eval_steps_per_second': 7.602, 'epoch': 1.97}\", \"{'loss': 0.0175, 'grad_norm': 0.07948163896799088, 'learning_rate': 3.9746209849539365e-08, 'epoch': 1.98}\", \"{'loss': 0.0164, 'grad_norm': 0.06169894337654114, 'learning_rate': 8.49790711467957e-09, 'epoch': 1.99}\", \"{'train_runtime': 25689.0286, 'train_samples_per_second': 5.071, 'train_steps_per_second': 0.317, 'train_loss': 0.02301430366192131, 'epoch': 2.0}\", \"***** train metrics *****\", \"  epoch                    =          2.0\", \"  total_flos               = 1503135961GF\", \"  train_loss               =        0.023\", \"  train_runtime            =   7:08:09.02\", \"  train_samples_per_second =        5.071\", \"  train_steps_per_second   =        0.317\", \"\\r  0%|          | 0/4706 [00:00<?, ?it/s]\\r  0%|          | 2/4706 [00:00<23:02,  3.40it/s]\\r  0%|          | 3/4706 [00:00<20:29,  3.83it/s]\\r  0%|          | 4/4706 [00:01<19:57,  3.93it/s]\\r  0%|          | 6/4706 [00:01<13:24,  5.84it/s]\\r  0%|          | 7/4706 [00:01<12:22,  6.33it/s]\\r  0%|          | 8/4706 [00:01<11:33,  6.77it/s]\\r  0%|          | 9/4706 [00:01<10:56,  7.15it/s]\\r  0%|          | 11/4706 [00:01<09:17,  8.42it/s]\\r  0%|          | 12/4706 [00:01<09:16,  8.43it/s]\\r  0%|          | 13/4706 [00:02<10:17,  7.60it/s]\\r  0%|          | 14/4706 [00:02<10:03,  7.78it/s]\\r  0%|          | 15/4706 [00:02<10:54,  7.17it/s]\\r  0%|          | 17/4706 [00:02<10:38,  7.35it/s]\\r  0%|          | 18/4706 [00:02<10:18,  7.58it/s]\\r  0%|          | 19/4706 [00:02<11:23,  6.86it/s]\\r  0%|          | 20/4706 [00:03<10:53,  7.17it/s]\\r  0%|          | 21/4706 [00:03<10:30,  7.43it/s]\\r  0%|          | 22/4706 [00:03<10:17,  7.59it/s]\\r  1%|          | 24/4706 [00:03<09:31,  8.20it/s]\\r  1%|          | 25/4706 [00:03<09:30,  8.21it/s]\\r  1%|          | 26/4706 [00:03<09:22,  8.32it/s]\\r  1%|          | 27/4706 [00:03<09:29,  8.21it/s]\\r  1%|          | 28/4706 [00:04<15:03,  5.18it/s]\\r  1%|          | 29/4706 [00:04<13:27,  5.79i\", \"\", \"... [截断: 输出过长，省略 195350 字符] ...\", \"\", \"██████▊| 4627/4706 [10:08<00:10,  7.74it/s]\\r 98%|█████████▊| 4628/4706 [10:08<00:09,  7.83it/s]\\r 98%|█████████▊| 4630/4706 [10:08<00:09,  8.37it/s]\\r 98%|█████████▊| 4631/4706 [10:08<00:09,  8.29it/s]\\r 98%|█████████▊| 4632/4706 [10:08<00:08,  8.24it/s]\\r 98%|█████████▊| 4633/4706 [10:08<00:08,  8.26it/s]\\r 98%|█████████▊| 4634/4706 [10:09<00:08,  8.32it/s]\\r 98%|█████████▊| 4635/4706 [10:09<00:09,  7.49it/s]\\r 99%|█████████▊| 4636/4706 [10:09<00:09,  7.66it/s]\\r 99%|█████████▊| 4637/4706 [10:09<00:08,  7.89it/s]\\r 99%|█████████▊| 4638/4706 [10:09<00:08,  8.04it/s]\\r 99%|█████████▊| 4639/4706 [10:09<00:09,  7.28it/s]\\r 99%|█████████▊| 4640/4706 [10:09<00:08,  7.59it/s]\\r 99%|█████████▊| 4641/4706 [10:10<00:08,  7.77it/s]\\r 99%|█████████▊| 4643/4706 [10:10<00:08,  7.74it/s]\\r 99%|█████████▊| 4645/4706 [10:10<00:07,  8.33it/s]\\r 99%|█████████▊| 4646/4706 [10:10<00:07,  8.29it/s]\\r 99%|█████████▉| 4648/4706 [10:10<00:06,  8.55it/s]\\r 99%|█████████▉| 4649/4706 [10:11<00:08,  7.11it/s]\\r 99%|█████████▉| 4650/4706 [10:11<00:07,  7.39it/s]\\r 99%|█████████▉| 4651/4706 [10:11<00:07,  7.57it/s]\\r 99%|█████████▉| 4652/4706 [10:11<00:07,  7.68it/s]\\r 99%|█████████▉| 4653/4706 [10:11<00:06,  7.83it/s]\\r 99%|█████████▉| 4654/4706 [10:11<00:06,  7.93it/s]\\r 99%|█████████▉| 4655/4706 [10:11<00:06,  8.00it/s]\\r 99%|█████████▉| 4656/4706 [10:11<00:06,  7.39it/s]\\r 99%|█████████▉| 4657/4706 [10:12<00:06,  7.66it/s]\\r 99%|█████████▉| 4658/4706 [10:12<00:08,  5.95it/s]\\r 99%|█████████▉| 4660/4706 [10:12<00:07,  6.54it/s]\\r 99%|█████████▉| 4661/4706 [10:12<00:07,  6.24it/s]\\r 99%|█████████▉| 4662/4706 [10:12<00:06,  6.65it/s]\\r 99%|█████████▉| 4663/4706 [10:13<00:06,  7.00it/s]\\r 99%|█████████▉| 4664/4706 [10:13<00:05,  7.64it/s]\\r 99%|█████████▉| 4665/4706 [10:13<00:05,  7.75it/s]\\r 99%|█████████▉| 4666/4706 [10:13<00:05,  7.93it/s]\\r 99%|█████████▉| 4668/4706 [10:13<00:04,  9.04it/s]\\r 99%|█████████▉| 4669/4706 [10:13<00:04,  8.78it/s]\\r 99%|█████████▉| 4670/4706 [10:13<00:04,  8.66it/s]\\r 99%|█████████▉| 4672/4706 [10:14<00:04,  7.50it/s]\\r 99%|█████████▉| 4674/4706 [10:14<00:03,  8.21it/s]\\r 99%|█████████▉| 4675/4706 [10:14<00:03,  8.21it/s]\\r 99%|█████████▉| 4676/4706 [10:14<00:03,  8.27it/s]\\r 99%|█████████▉| 4677/4706 [10:14<00:03,  8.31it/s]\\r 99%|█████████▉| 4678/4706 [10:14<00:03,  7.52it/s]\\r 99%|█████████▉| 4679/4706 [10:15<00:03,  6.81it/s]\\r 99%|█████████▉| 4680/4706 [10:15<00:03,  7.15it/s]\\r 99%|█████████▉| 4681/4706 [10:15<00:03,  7.37it/s]\\r 99%|█████████▉| 4682/4706 [10:15<00:03,  6.63it/s]\\r100%|█████████▉| 4684/4706 [10:15<00:03,  7.02it/s]\\r100%|█████████▉| 4686/4706 [10:15<00:02,  7.68it/s]\\r100%|█████████▉| 4688/4706 [10:16<00:02,  7.60it/s]\\r100%|█████████▉| 4689/4706 [10:16<00:02,  7.72it/s]\\r100%|█████████▉| 4690/4706 [10:16<00:02,  7.81it/s]\\r100%|█████████▉| 4691/4706 [10:16<00:02,  6.31it/s]\\r100%|█████████▉| 4692/4706 [10:16<00:02,  6.70it/s]\\r100%|█████████▉| 4693/4706 [10:16<00:01,  6.99it/s]\\r100%|█████████▉| 4694/4706 [10:17<00:01,  6.48it/s]\\r100%|█████████▉| 4695/4706 [10:17<00:01,  6.86it/s]\\r100%|█████████▉| 4696/4706 [10:17<00:01,  7.25it/s]\\r100%|█████████▉| 4697/4706 [10:17<00:01,  6.92it/s]\\r100%|█████████▉| 4698/4706 [10:17<00:01,  7.28it/s]\\r100%|█████████▉| 4699/4706 [10:17<00:00,  7.46it/s]\\r100%|█████████▉| 4700/4706 [10:17<00:00,  6.90it/s]\\r100%|█████████▉| 4702/4706 [10:18<00:00,  7.79it/s]\\r100%|█████████▉| 4703/4706 [10:18<00:00,  7.91it/s]\\r100%|█████████▉| 4704/4706 [10:18<00:00,  7.02it/s]\\r100%|█████████▉| 4705/4706 [10:18<00:00,  7.35it/s]\\r100%|██████████| 4706/4706 [10:18<00:00,  6.22it/s]\\r100%|██████████| 4706/4706 [10:18<00:00,  7.60it/s]\", \"[INFO|modelcard.py:456] 2026-05-21 03:03:43,559 >> Dropping the following result as it does not have all the necessary fields:\", \"{'task': {'name': 'Causal Language Modeling', 'type': 'text-generation'}}\", \"***** eval metrics *****\", \"  epoch                   =        2.0\", \"  eval_loss               =     0.0329\", \"  eval_runtime            = 0:10:19.05\", \"  eval_samples_per_second =     30.408\", \"  eval_steps_per_second   =      7.602\"], \"line_count\": 84, \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/logs/exp_b1_scd_fewnerd_standard.log\", \"anomalies\": []}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.51}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "41d8dd85-3247-419e-9119-48474eb35558",
  "isSidechain": false,
  "promptId": "d2210c4d-d5b9-450f-8450-2f1ffe6e0ccd",
  "type": "user",
  "uuid": "5fcbed1e-5734-436a-b6aa-0cea26d4faab",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"lines\\\": [\\\"\\\\\\\"full_attention\\\\\\\",\\\", \\\"    \\\\\\\"full_attention\\\\\\\",\\\", \\\"    \\\\\\\"full_attention\\\\\\\",\\\", \\\"    \\\\\\\"full_attention\\\\\\\",\\\", \\\"    \\\\\\\"full_attention\\\\\\\",\\\", \\\"    \\\\\\\"full_attention\\\\\\\",\\\", \\\"    \\\\\\\"full_attention\\\\\\\",\\\", \\\"    \\\\\\\"full_attention\\\\\\\",\\\", \\\"    \\\\\\\"full_attention\\\\\\\",\\\", \\\"    \\\\\\\"full_attention\\\\\\\",\\\", \\\"    \\\\\\\"full_attention\\\\\\\",\\\", \\\"    \\\\\\\"full_attention\\\\\\\",\\\", \\\"    \\\\\\\"full_attention\\\\\\\",\\\", \\\"    \\\\\\\"full_attention\\\\\\\",\\\", \\\"    \\\\\\\"full_attention\\\\\\\",\\\", \\\"    \\\\\\\"full_attention\\\\\\\",\\\", \\\"    \\\\\\\"full_attention\\\\\\\",\\\", \\\"    \\\\\\\"full_attention\\\\\\\",\\\", \\\"    \\\\\\\"full_attention\\\\\\\",\\\", \\\"    \\\\\\\"full_attention\\\\\\\",\\\", \\\"    \\\\\\\"full_attention\\\\\\\",\\\", \\\"    \\\\\\\"full_attention\\\\\\\",\\\", \\\"    \\\\\\\"full_attention\\\\\\\",\\\", \\\"    \\\\\\\"full_attention\\\\\\\",\\\", \\\"    \\\\\\\"full_attention\\\\\\\",\\\", \\\"    \\\\\\\"full_attention\\\\\\\",\\\", \\\"    \\\\\\\"full_attention\\\\\\\",\\\", \\\"    \\\\\\\"full_attention\\\\\\\",\\\", \\\"    \\\\\\\"full_attention\\\\\\\",\\\", \\\"    \\\\\\\"full_attention\\\\\\\",\\\", \\\"    \\\\\\\"full_attention\\\\\\\",\\\", \\\"    \\\\\\\"full_attention\\\\\\\",\\\", \\\"    \\\\\\\"full_attention\\\\\\\",\\\", \\\"    \\\\\\\"full_attention\\\\\\\",\\\", \\\"    \\\\\\\"full_attention\\\\\\\"\\\", \\\"  ],\\\", \\\"  \\\\\\\"max_position_embeddings\\\\\\\": 40960,\\\", \\\"  \\\\\\\"max_window_layers\\\\\\\": 36,\\\", \\\"  \\\\\\\"model_type\\\\\\\": \\\\\\\"qwen3\\\\\\\",\\\", \\\"  \\\\\\\"num_attention_heads\\\\\\\": 32,\\\", \\\"  \\\\\\\"num_hidden_layers\\\\\\\": 36,\\\", \\\"  \\\\\\\"num_key_value_heads\\\\\\\": 8,\\\", \\\"  \\\\\\\"rms_norm_eps\\\\\\\": 1e-06,\\\", \\\"  \\\\\\\"rope_scaling\\\\\\\": null,\\\", \\\"  \\\\\\\"rope_theta\\\\\\\": 1000000,\\\", \\\"  \\\\\\\"sliding_window\\\\\\\": null,\\\", \\\"  \\\\\\\"tie_word_embeddings\\\\\\\": false,\\\", \\\"  \\\\\\\"transformers_version\\\\\\\": \\\\\\\"4.57.1\\\\\\\",\\\", \\\"  \\\\\\\"use_cache\\\\\\\": true,\\\", \\\"  \\\\\\\"use_sliding_window\\\\\\\": false,\\\", \\\"  \\\\\\\"vocab_size\\\\\\\": 151936\\\", \\\"}\\\", \\\"\\\", \\\"[INFO|tokenization_utils_base.py:2421] 2026-05-21 02:53:24,398 >> chat template saved in /root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen3-8b-fewnerd-scd-lora/chat_template.jinja\\\", \\\"[INFO|tokenization_utils_base.py:2590] 2026-05-21 02:53:24,398 >> tokenizer config file saved in /root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen3-8b-fewnerd-scd-lora/tokenizer_config.json\\\", \\\"[INFO|tokenization_utils_base.py:2599] 2026-05-21 02:53:24,398 >> Special tokens file saved in /root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen3-8b-fewnerd-scd-lora/special_tokens_map.json\\\", \\\"[INFO|trainer.py:4643] 2026-05-21 02:53:24,498 >> \\\", \\\"***** Running Evaluation *****\\\", \\\"[INFO|trainer.py:4645] 2026-05-21 02:53:24,498 >>   Num examples = 18824\\\", \\\"[INFO|trainer.py:4648] 2026-05-21 02:53:24,498 >>   Batch size = 4\\\", \\\"{'eval_loss': 0.03392118960618973, 'eval_runtime': 619.073, 'eval_samples_per_second': 30.407, 'eval_steps_per_second': 7.602, 'epoch': 1.97}\\\", \\\"{'loss': 0.0175, 'grad_norm': 0.07948163896799088, 'learning_rate': 3.9746209849539365e-08, 'epoch': 1.98}\\\", \\\"{'loss': 0.0164, 'grad_norm': 0.06169894337654114, 'learning_rate': 8.49790711467957e-09, 'epoch': 1.99}\\\", \\\"{'train_runtime': 25689.0286, 'train_samples_per_second': 5.071, 'train_steps_per_second': 0.317, 'train_loss': 0.02301430366192131, 'epoch': 2.0}\\\", \\\"***** train metrics *****\\\", \\\"  epoch                    =          2.0\\\", \\\"  total_flos               = 1503135961GF\\\", \\\"  train_loss               =        0.023\\\", \\\"  train_runtime            =   7:08:09.02\\\", \\\"  train_samples_per_second =        5.071\\\", \\\"  train_steps_per_second   =        0.317\\\", \\\"\\\\r  0%|          | 0/4706 [00:00<?, ?it/s]\\\\r  0%|          | 2/4706 [00:00<23:02,  3.40it/s]\\\\r  0%|          | 3/4706 [00:00<20:29,  3.83it/s]\\\\r  0%|          | 4/4706 [00:01<19:57,  3.93it/s]\\\\r  0%|          | 6/4706 [00:01<13:24,  5.84it/s]\\\\r  0%|          | 7/4706 [00:01<12:22,  6.33it/s]\\\\r  0%|          | 8/4706 [00:01<11:33,  6.77it/s]\\\\r  0%|          | 9/4706 [00:01<10:56,  7.15it/s]\\\\r  0%|          | 11/4706 [00:01<09:17,  8.42it/s]\\\\r  0%|          | 12/4706 [00:01<09:16,  8.43it/s]\\\\r  0%|          | 13/4706 [00:02<10:17,  7.60it/s]\\\\r  0%|          | 14/4706 [00:02<10:03,  7.78it/s]\\\\r  0%|          | 15/4706 [00:02<10:54,  7.17it/s]\\\\r  0%|          | 17/4706 [00:02<10:38,  7.35it/s]\\\\r  0%|          | 18/4706 [00:02<10:18,  7.58it/s]\\\\r  0%|          | 19/4706 [00:02<11:23,  6.86it/s]\\\\r  0%|          | 20/4706 [00:03<10:53,  7.17it/s]\\\\r  0%|          | 21/4706 [00:03<10:30,  7.43it/s]\\\\r  0%|          | 22/4706 [00:03<10:17,  7.59it/s]\\\\r  1%|          | 24/4706 [00:03<09:31,  8.20it/s]\\\\r  1%|          | 25/4706 [00:03<09:30,  8.21it/s]\\\\r  1%|          | 26/4706 [00:03<09:22,  8.32it/s]\\\\r  1%|          | 27/4706 [00:03<09:29,  8.21it/s]\\\\r  1%|          | 28/4706 [00:04<15:03,  5.18it/s]\\\\r  1%|          | 29/4706 [00:04<13:27,  5.79i\\\", \\\"\\\", \\\"... [截断: 输出过长，省略 195350 字符] ...\\\", \\\"\\\", \\\"██████▊| 4627/4706 [10:08<00:10,  7.74it/s]\\\\r 98%|█████████▊| 4628/4706 [10:08<00:09,  7.83it/s]\\\\r 98%|█████████▊| 4630/4706 [10:08<00:09,  8.37it/s]\\\\r 98%|█████████▊| 4631/4706 [10:08<00:09,  8.29it/s]\\\\r 98%|█████████▊| 4632/4706 [10:08<00:08,  8.24it/s]\\\\r 98%|█████████▊| 4633/4706 [10:08<00:08,  8.26it/s]\\\\r 98%|█████████▊| 4634/4706 [10:09<00:08,  8.32it/s]\\\\r 98%|█████████▊| 4635/4706 [10:09<00:09,  7.49it/s]\\\\r 99%|█████████▊| 4636/4706 [10:09<00:09,  7.66it/s]\\\\r 99%|█████████▊| 4637/4706 [10:09<00:08,  7.89it/s]\\\\r 99%|█████████▊| 4638/4706 [10:09<00:08,  8.04it/s]\\\\r 99%|█████████▊| 4639/4706 [10:09<00:09,  7.28it/s]\\\\r 99%|█████████▊| 4640/4706 [10:09<00:08,  7.59it/s]\\\\r 99%|█████████▊| 4641/4706 [10:10<00:08,  7.77it/s]\\\\r 99%|█████████▊| 4643/4706 [10:10<00:08,  7.74it/s]\\\\r 99%|█████████▊| 4645/4706 [10:10<00:07,  8.33it/s]\\\\r 99%|█████████▊| 4646/4706 [10:10<00:07,  8.29it/s]\\\\r 99%|█████████▉| 4648/4706 [10:10<00:06,  8.55it/s]\\\\r 99%|█████████▉| 4649/4706 [10:11<00:08,  7.11it/s]\\\\r 99%|█████████▉| 4650/4706 [10:11<00:07,  7.39it/s]\\\\r 99%|█████████▉| 4651/4706 [10:11<00:07,  7.57it/s]\\\\r 99%|█████████▉| 4652/4706 [10:11<00:07,  7.68it/s]\\\\r 99%|█████████▉| 4653/4706 [10:11<00:06,  7.83it/s]\\\\r 99%|█████████▉| 4654/4706 [10:11<00:06,  7.93it/s]\\\\r 99%|█████████▉| 4655/4706 [10:11<00:06,  8.00it/s]\\\\r 99%|█████████▉| 4656/4706 [10:11<00:06,  7.39it/s]\\\\r 99%|█████████▉| 4657/4706 [10:12<00:06,  7.66it/s]\\\\r 99%|█████████▉| 4658/4706 [10:12<00:08,  5.95it/s]\\\\r 99%|█████████▉| 4660/4706 [10:12<00:07,  6.54it/s]\\\\r 99%|█████████▉| 4661/4706 [10:12<00:07,  6.24it/s]\\\\r 99%|█████████▉| 4662/4706 [10:12<00:06,  6.65it/s]\\\\r 99%|█████████▉| 4663/4706 [10:13<00:06,  7.00it/s]\\\\r 99%|█████████▉| 4664/4706 [10:13<00:05,  7.64it/s]\\\\r 99%|█████████▉| 4665/4706 [10:13<00:05,  7.75it/s]\\\\r 99%|█████████▉| 4666/4706 [10:13<00:05,  7.93it/s]\\\\r 99%|█████████▉| 4668/4706 [10:13<00:04,  9.04it/s]\\\\r 99%|█████████▉| 4669/4706 [10:13<00:04,  8.78it/s]\\\\r 99%|█████████▉| 4670/4706 [10:13<00:04,  8.66it/s]\\\\r 99%|█████████▉| 4672/4706 [10:14<00:04,  7.50it/s]\\\\r 99%|█████████▉| 4674/4706 [10:14<00:03,  8.21it/s]\\\\r 99%|█████████▉| 4675/4706 [10:14<00:03,  8.21it/s]\\\\r 99%|█████████▉| 4676/4706 [10:14<00:03,  8.27it/s]\\\\r 99%|█████████▉| 4677/4706 [10:14<00:03,  8.31it/s]\\\\r 99%|█████████▉| 4678/4706 [10:14<00:03,  7.52it/s]\\\\r 99%|█████████▉| 4679/4706 [10:15<00:03,  6.81it/s]\\\\r 99%|█████████▉| 4680/4706 [10:15<00:03,  7.15it/s]\\\\r 99%|█████████▉| 4681/4706 [10:15<00:03,  7.37it/s]\\\\r 99%|█████████▉| 4682/4706 [10:15<00:03,  6.63it/s]\\\\r100%|█████████▉| 4684/4706 [10:15<00:03,  7.02it/s]\\\\r100%|█████████▉| 4686/4706 [10:15<00:02,  7.68it/s]\\\\r100%|█████████▉| 4688/4706 [10:16<00:02,  7.60it/s]\\\\r100%|█████████▉| 4689/4706 [10:16<00:02,  7.72it/s]\\\\r100%|█████████▉| 4690/4706 [10:16<00:02,  7.81it/s]\\\\r100%|█████████▉| 4691/4706 [10:16<00:02,  6.31it/s]\\\\r100%|█████████▉| 4692/4706 [10:16<00:02,  6.70it/s]\\\\r100%|█████████▉| 4693/4706 [10:16<00:01,  6.99it/s]\\\\r100%|█████████▉| 4694/4706 [10:17<00:01,  6.48it/s]\\\\r100%|█████████▉| 4695/4706 [10:17<00:01,  6.86it/s]\\\\r100%|█████████▉| 4696/4706 [10:17<00:01,  7.25it/s]\\\\r100%|█████████▉| 4697/4706 [10:17<00:01,  6.92it/s]\\\\r100%|█████████▉| 4698/4706 [10:17<00:01,  7.28it/s]\\\\r100%|█████████▉| 4699/4706 [10:17<00:00,  7.46it/s]\\\\r100%|█████████▉| 4700/4706 [10:17<00:00,  6.90it/s]\\\\r100%|█████████▉| 4702/4706 [10:18<00:00,  7.79it/s]\\\\r100%|█████████▉| 4703/4706 [10:18<00:00,  7.91it/s]\\\\r100%|█████████▉| 4704/4706 [10:18<00:00,  7.02it/s]\\\\r100%|█████████▉| 4705/4706 [10:18<00:00,  7.35it/s]\\\\r100%|██████████| 4706/4706 [10:18<00:00,  6.22it/s]\\\\r100%|██████████| 4706/4706 [10:18<00:00,  7.60it/s]\\\", \\\"[INFO|modelcard.py:456] 2026-05-21 03:03:43,559 >> Dropping the following result as it does not have all the necessary fields:\\\", \\\"{'task': {'name': 'Causal Language Modeling', 'type': 'text-generation'}}\\\", \\\"***** eval metrics *****\\\", \\\"  epoch                   =        2.0\\\", \\\"  eval_loss               =     0.0329\\\", \\\"  eval_runtime            = 0:10:19.05\\\", \\\"  eval_samples_per_second =     30.408\\\", \\\"  eval_steps_per_second   =      7.602\\\"], \\\"line_count\\\": 84, \\\"log_path\\\": \\\"/root/autodl-tmp/struct_self_consist_ie/logs/exp_b1_scd_fewnerd_standard.log\\\", \\\"anomalies\\\": []}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.51}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"lines\": [\"\\\"full_attention\\\",\", \"    \\\"full_attention\\\",\", \"    \\\"full_attention\\\",\", \"    \\\"full_attention\\\",\", \"    \\\"full_attention\\\",\", \"    \\\"full_attention\\\",\", \"    \\\"full_attention\\\",\", \"    \\\"full_attention\\\",\", \"    \\\"full_attention\\\",\", \"    \\\"full_attention\\\",\", \"    \\\"full_attention\\\",\", \"    \\\"full_attention\\\",\", \"    \\\"full_attention\\\",\", \"    \\\"full_attention\\\",\", \"    \\\"full_attention\\\",\", \"    \\\"full_attention\\\",\", \"    \\\"full_attention\\\",\", \"    \\\"full_attention\\\",\", \"    \\\"full_attention\\\",\", \"    \\\"full_attention\\\",\", \"    \\\"full_attention\\\",\", \"    \\\"full_attention\\\",\", \"    \\\"full_attention\\\",\", \"    \\\"full_attention\\\",\", \"    \\\"full_attention\\\",\", \"    \\\"full_attention\\\",\", \"    \\\"full_attention\\\",\", \"    \\\"full_attention\\\",\", \"    \\\"full_attention\\\",\", \"    \\\"full_attention\\\",\", \"    \\\"full_attention\\\",\", \"    \\\"full_attention\\\",\", \"    \\\"full_attention\\\",\", \"    \\\"full_attention\\\",\", \"    \\\"full_attention\\\"\", \"  ],\", \"  \\\"max_position_embeddings\\\": 40960,\", \"  \\\"max_window_layers\\\": 36,\", \"  \\\"model_type\\\": \\\"qwen3\\\",\", \"  \\\"num_attention_heads\\\": 32,\", \"  \\\"num_hidden_layers\\\": 36,\", \"  \\\"num_key_value_heads\\\": 8,\", \"  \\\"rms_norm_eps\\\": 1e-06,\", \"  \\\"rope_scaling\\\": null,\", \"  \\\"rope_theta\\\": 1000000,\", \"  \\\"sliding_window\\\": null,\", \"  \\\"tie_word_embeddings\\\": false,\", \"  \\\"transformers_version\\\": \\\"4.57.1\\\",\", \"  \\\"use_cache\\\": true,\", \"  \\\"use_sliding_window\\\": false,\", \"  \\\"vocab_size\\\": 151936\", \"}\", \"\", \"[INFO|tokenization_utils_base.py:2421] 2026-05-21 02:53:24,398 >> chat template saved in /root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen3-8b-fewnerd-scd-lora/chat_template.jinja\", \"[INFO|tokenization_utils_base.py:2590] 2026-05-21 02:53:24,398 >> tokenizer config file saved in /root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen3-8b-fewnerd-scd-lora/tokenizer_config.json\", \"[INFO|tokenization_utils_base.py:2599] 2026-05-21 02:53:24,398 >> Special tokens file saved in /root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen3-8b-fewnerd-scd-lora/special_tokens_map.json\", \"[INFO|trainer.py:4643] 2026-05-21 02:53:24,498 >> \", \"***** Running Evaluation *****\", \"[INFO|trainer.py:4645] 2026-05-21 02:53:24,498 >>   Num examples = 18824\", \"[INFO|trainer.py:4648] 2026-05-21 02:53:24,498 >>   Batch size = 4\", \"{'eval_loss': 0.03392118960618973, 'eval_runtime': 619.073, 'eval_samples_per_second': 30.407, 'eval_steps_per_second': 7.602, 'epoch': 1.97}\", \"{'loss': 0.0175, 'grad_norm': 0.07948163896799088, 'learning_rate': 3.9746209849539365e-08, 'epoch': 1.98}\", \"{'loss': 0.0164, 'grad_norm': 0.06169894337654114, 'learning_rate': 8.49790711467957e-09, 'epoch': 1.99}\", \"{'train_runtime': 25689.0286, 'train_samples_per_second': 5.071, 'train_steps_per_second': 0.317, 'train_loss': 0.02301430366192131, 'epoch': 2.0}\", \"***** train metrics *****\", \"  epoch                    =          2.0\", \"  total_flos               = 1503135961GF\", \"  train_loss               =        0.023\", \"  train_runtime            =   7:08:09.02\", \"  train_samples_per_second =        5.071\", \"  train_steps_per_second   =        0.317\", \"\\r  0%|          | 0/4706 [00:00<?, ?it/s]\\r  0%|          | 2/4706 [00:00<23:02,  3.40it/s]\\r  0%|          | 3/4706 [00:00<20:29,  3.83it/s]\\r  0%|          | 4/4706 [00:01<19:57,  3.93it/s]\\r  0%|          | 6/4706 [00:01<13:24,  5.84it/s]\\r  0%|          | 7/4706 [00:01<12:22,  6.33it/s]\\r  0%|          | 8/4706 [00:01<11:33,  6.77it/s]\\r  0%|          | 9/4706 [00:01<10:56,  7.15it/s]\\r  0%|          | 11/4706 [00:01<09:17,  8.42it/s]\\r  0%|          | 12/4706 [00:01<09:16,  8.43it/s]\\r  0%|          | 13/4706 [00:02<10:17,  7.60it/s]\\r  0%|          | 14/4706 [00:02<10:03,  7.78it/s]\\r  0%|          | 15/4706 [00:02<10:54,  7.17it/s]\\r  0%|          | 17/4706 [00:02<10:38,  7.35it/s]\\r  0%|          | 18/4706 [00:02<10:18,  7.58it/s]\\r  0%|          | 19/4706 [00:02<11:23,  6.86it/s]\\r  0%|          | 20/4706 [00:03<10:53,  7.17it/s]\\r  0%|          | 21/4706 [00:03<10:30,  7.43it/s]\\r  0%|          | 22/4706 [00:03<10:17,  7.59it/s]\\r  1%|          | 24/4706 [00:03<09:31,  8.20it/s]\\r  1%|          | 25/4706 [00:03<09:30,  8.21it/s]\\r  1%|          | 26/4706 [00:03<09:22,  8.32it/s]\\r  1%|          | 27/4706 [00:03<09:29,  8.21it/s]\\r  1%|          | 28/4706 [00:04<15:03,  5.18it/s]\\r  1%|          | 29/4706 [00:04<13:27,  5.79i\", \"\", \"... [截断: 输出过长，省略 195350 字符] ...\", \"\", \"██████▊| 4627/4706 [10:08<00:10,  7.74it/s]\\r 98%|█████████▊| 4628/4706 [10:08<00:09,  7.83it/s]\\r 98%|█████████▊| 4630/4706 [10:08<00:09,  8.37it/s]\\r 98%|█████████▊| 4631/4706 [10:08<00:09,  8.29it/s]\\r 98%|█████████▊| 4632/4706 [10:08<00:08,  8.24it/s]\\r 98%|█████████▊| 4633/4706 [10:08<00:08,  8.26it/s]\\r 98%|█████████▊| 4634/4706 [10:09<00:08,  8.32it/s]\\r 98%|█████████▊| 4635/4706 [10:09<00:09,  7.49it/s]\\r 99%|█████████▊| 4636/4706 [10:09<00:09,  7.66it/s]\\r 99%|█████████▊| 4637/4706 [10:09<00:08,  7.89it/s]\\r 99%|█████████▊| 4638/4706 [10:09<00:08,  8.04it/s]\\r 99%|█████████▊| 4639/4706 [10:09<00:09,  7.28it/s]\\r 99%|█████████▊| 4640/4706 [10:09<00:08,  7.59it/s]\\r 99%|█████████▊| 4641/4706 [10:10<00:08,  7.77it/s]\\r 99%|█████████▊| 4643/4706 [10:10<00:08,  7.74it/s]\\r 99%|█████████▊| 4645/4706 [10:10<00:07,  8.33it/s]\\r 99%|█████████▊| 4646/4706 [10:10<00:07,  8.29it/s]\\r 99%|█████████▉| 4648/4706 [10:10<00:06,  8.55it/s]\\r 99%|█████████▉| 4649/4706 [10:11<00:08,  7.11it/s]\\r 99%|█████████▉| 4650/4706 [10:11<00:07,  7.39it/s]\\r 99%|█████████▉| 4651/4706 [10:11<00:07,  7.57it/s]\\r 99%|█████████▉| 4652/4706 [10:11<00:07,  7.68it/s]\\r 99%|█████████▉| 4653/4706 [10:11<00:06,  7.83it/s]\\r 99%|█████████▉| 4654/4706 [10:11<00:06,  7.93it/s]\\r 99%|█████████▉| 4655/4706 [10:11<00:06,  8.00it/s]\\r 99%|█████████▉| 4656/4706 [10:11<00:06,  7.39it/s]\\r 99%|█████████▉| 4657/4706 [10:12<00:06,  7.66it/s]\\r 99%|█████████▉| 4658/4706 [10:12<00:08,  5.95it/s]\\r 99%|█████████▉| 4660/4706 [10:12<00:07,  6.54it/s]\\r 99%|█████████▉| 4661/4706 [10:12<00:07,  6.24it/s]\\r 99%|█████████▉| 4662/4706 [10:12<00:06,  6.65it/s]\\r 99%|█████████▉| 4663/4706 [10:13<00:06,  7.00it/s]\\r 99%|█████████▉| 4664/4706 [10:13<00:05,  7.64it/s]\\r 99%|█████████▉| 4665/4706 [10:13<00:05,  7.75it/s]\\r 99%|█████████▉| 4666/4706 [10:13<00:05,  7.93it/s]\\r 99%|█████████▉| 4668/4706 [10:13<00:04,  9.04it/s]\\r 99%|█████████▉| 4669/4706 [10:13<00:04,  8.78it/s]\\r 99%|█████████▉| 4670/4706 [10:13<00:04,  8.66it/s]\\r 99%|█████████▉| 4672/4706 [10:14<00:04,  7.50it/s]\\r 99%|█████████▉| 4674/4706 [10:14<00:03,  8.21it/s]\\r 99%|█████████▉| 4675/4706 [10:14<00:03,  8.21it/s]\\r 99%|█████████▉| 4676/4706 [10:14<00:03,  8.27it/s]\\r 99%|█████████▉| 4677/4706 [10:14<00:03,  8.31it/s]\\r 99%|█████████▉| 4678/4706 [10:14<00:03,  7.52it/s]\\r 99%|█████████▉| 4679/4706 [10:15<00:03,  6.81it/s]\\r 99%|█████████▉| 4680/4706 [10:15<00:03,  7.15it/s]\\r 99%|█████████▉| 4681/4706 [10:15<00:03,  7.37it/s]\\r 99%|█████████▉| 4682/4706 [10:15<00:03,  6.63it/s]\\r100%|█████████▉| 4684/4706 [10:15<00:03,  7.02it/s]\\r100%|█████████▉| 4686/4706 [10:15<00:02,  7.68it/s]\\r100%|█████████▉| 4688/4706 [10:16<00:02,  7.60it/s]\\r100%|█████████▉| 4689/4706 [10:16<00:02,  7.72it/s]\\r100%|█████████▉| 4690/4706 [10:16<00:02,  7.81it/s]\\r100%|█████████▉| 4691/4706 [10:16<00:02,  6.31it/s]\\r100%|█████████▉| 4692/4706 [10:16<00:02,  6.70it/s]\\r100%|█████████▉| 4693/4706 [10:16<00:01,  6.99it/s]\\r100%|█████████▉| 4694/4706 [10:17<00:01,  6.48it/s]\\r100%|█████████▉| 4695/4706 [10:17<00:01,  6.86it/s]\\r100%|█████████▉| 4696/4706 [10:17<00:01,  7.25it/s]\\r100%|█████████▉| 4697/4706 [10:17<00:01,  6.92it/s]\\r100%|█████████▉| 4698/4706 [10:17<00:01,  7.28it/s]\\r100%|█████████▉| 4699/4706 [10:17<00:00,  7.46it/s]\\r100%|█████████▉| 4700/4706 [10:17<00:00,  6.90it/s]\\r100%|█████████▉| 4702/4706 [10:18<00:00,  7.79it/s]\\r100%|█████████▉| 4703/4706 [10:18<00:00,  7.91it/s]\\r100%|█████████▉| 4704/4706 [10:18<00:00,  7.02it/s]\\r100%|█████████▉| 4705/4706 [10:18<00:00,  7.35it/s]\\r100%|██████████| 4706/4706 [10:18<00:00,  6.22it/s]\\r100%|██████████| 4706/4706 [10:18<00:00,  7.60it/s]\", \"[INFO|modelcard.py:456] 2026-05-21 03:03:43,559 >> Dropping the following result as it does not have all the necessary fields:\", \"{'task': {'name': 'Causal Language Modeling', 'type': 'text-generation'}}\", \"***** eval metrics *****\", \"  epoch                   =        2.0\", \"  eval_loss               =     0.0329\", \"  eval_runtime            = 0:10:19.05\", \"  eval_samples_per_second =     30.408\", \"  eval_steps_per_second   =      7.602\"], \"line_count\": 84, \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/logs/exp_b1_scd_fewnerd_standard.log\", \"anomalies\": []}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.51}}"
    }
  },
  "sourceToolAssistantUUID": "41d8dd85-3247-419e-9119-48474eb35558",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/agent_5c567c58",
  "sessionId": "bb8bc777-37fb-4956-b48e-5e9c5a98dd73",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 71_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[CRON] 实验进程异常退出（失败），需要你诊断原因。 详情: Process exited without valid W&B metrics  - exp_id: exp_b1_scd_fewnerd_standard - project: struct_self_consist_ie - server: autodl-5090-b - log_path: /root/autodl-tmp/…",
  "leafUuid": "5fcbed1e-5734-436a-b6aa-0cea26d4faab",
  "sessionId": "bb8bc777-37fb-4956-b48e-5e9c5a98dd73"
}
```

---

### Runtime record

_source line 72_

```json
{
  "type": "ai-title",
  "aiTitle": "Diagnose experiment process exit failure",
  "sessionId": "bb8bc777-37fb-4956-b48e-5e9c5a98dd73"
}
```

---

### Assistant

_source line 73 · 2026-05-20T19:16:14.966Z_

<details><summary>Logged reasoning block</summary>

```text
Confirmed! The training actually completed successfully:
- 4706/4706 steps completed (100%)
- train_loss = 0.023
- eval_loss = 0.0329
- epoch = 2.0
- train_runtime = 7:08:09.02
- eval metrics recorded

This is exactly the same false positive pattern as `exp_b1_scd_fewnerd_curriculum_q`. The training completed normally, but cron marked it as failed because there's no W&B integration.

Now I need to:
1. Update the registry to retract the failed conclusion — change to DONE/success (or at least retract the failed status)


2. Record the actual metrics and checkpoint path
3. Notify Director

But I should be careful here — the training finished, but that doesn't mean it's a research success. I need to retract the "failed" status and note that it's a cron false positive, then run eval inference on the checkpoint to actually determine if the results are good. So the registry should reflect that training completed, but the final conclusion depends on the FewNERD greedy F1 scores.

Looking at the checkpoint path from the logs, I've got `/root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen3-8b-fewnerd-scd-lora/`. Now I need to update the registry to change the status from DONE with a failed conclusion to something like ANALYZING, and spawn an eval worker to get the actual performance metrics.

The core issue is that the training completed successfully but was marked as failed due to a cron false positive. I need to verify the hypothesis that greedy F1 after SCD training approaches the N=8 construction F1 (0.764 vs the current 0.748), so I'll update the registry notes to reflect this was a false positive, clear the failed conclusion, set the status to ANALYZING, record the checkpoint path, and trigger an evaluation job.

However, there's a constraint that status can only move forward in the state machine, and the experiment is currently marked DONE. Looking at how similar situations were handled before, I should document the retraction in the notes and potentially create a separate evaluation experiment rather than trying to revert the status. I need to update the registry entry for this experiment to mark it as a retracted false positive, then spawn an evaluation worker to run the proper greedy inference test. I should also pull the resource usage metrics so I can include them in my report to the Director.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5fcbed1e-5734-436a-b6aa-0cea26d4faab",
  "isSidechain": false,
  "requestId": "req_011CbEMd1CH8bSr81Y3o9Kn4",
  "type": "assistant",
  "uuid": "bb41ca92-964d-49f0-af29-4d29e0527854",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/agent_5c567c58",
  "sessionId": "bb8bc777-37fb-4956-b48e-5e9c5a98dd73",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XA44qB9HjDXZtgzSBnty4r",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5678,
      "cache_read_input_tokens": 61819,
      "output_tokens": 2347,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5678,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2347,
          "cache_read_input_tokens": 61819,
          "cache_creation_input_tokens": 5678,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5678
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

_source line 74 · 2026-05-20T19:16:17.587Z_

确认：**训练实际完成成功**。与 memory.md 记录的已知模式完全匹配——LLaMA-Factory 无 W&B 导致 cron 误判。

证据：
- 4706/4706 steps 完成 (100%)
- train_loss = 0.023, eval_loss = 0.0329
- epoch = 2.0, 运行时间 7h08m
- checkpoint 保存至 `/root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen3-8b-fewnerd-scd-lora/`

更新 registry 撤回 failed 标记，同时获取资源状态。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bb41ca92-964d-49f0-af29-4d29e0527854",
  "isSidechain": false,
  "requestId": "req_011CbEMd1CH8bSr81Y3o9Kn4",
  "type": "assistant",
  "uuid": "299de2f3-fa03-4ce7-8799-d747ddd4f3fc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/agent_5c567c58",
  "sessionId": "bb8bc777-37fb-4956-b48e-5e9c5a98dd73",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XA44qB9HjDXZtgzSBnty4r",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5678,
      "cache_read_input_tokens": 61819,
      "output_tokens": 2347,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5678,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2347,
          "cache_read_input_tokens": 61819,
          "cache_creation_input_tokens": 5678,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5678
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

_source line 75 · 2026-05-20T19:16:19.009Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry · `toolu_01HTDYYGXa1Zfx3zYrgWnkdV`</summary>

```json
{
  "exp_id": "exp_b1_scd_fewnerd_standard",
  "field": "failure_reason",
  "value": "RETRACTED: cron false positive — training completed successfully (4706/4706 steps, train_loss=0.023, eval_loss=0.0329). Original: process dead 5× with no sentinel/W&B",
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "299de2f3-fa03-4ce7-8799-d747ddd4f3fc",
  "isSidechain": false,
  "requestId": "req_011CbEMd1CH8bSr81Y3o9Kn4",
  "type": "assistant",
  "uuid": "771496a1-f1bf-4bb6-bef1-5e48381c3b69",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/agent_5c567c58",
  "sessionId": "bb8bc777-37fb-4956-b48e-5e9c5a98dd73",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XA44qB9HjDXZtgzSBnty4r",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5678,
      "cache_read_input_tokens": 61819,
      "output_tokens": 2347,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5678,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2347,
          "cache_read_input_tokens": 61819,
          "cache_creation_input_tokens": 5678,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5678
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

_source line 76 · 2026-05-20T19:16:20.551Z_

<details><summary>↩ Tool result · `toolu_01HTDYYGXa1Zfx3zYrgWnkdV`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"exp_id\": \"exp_b1_scd_fewnerd_standard\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T11:17:37.804Z\", \"updated_at\": \"2026-05-20T19:16:20.137Z\", \"hypothesis\": \"Standard Self-Consistency Distillation on FewNERD: fine-tune Qwen3-8B-FT with theta2n construction pseudo-labels (32,565 instances) mixed 1:1 with gold data. Greedy F1 after SCD should approach N=8 construction F1 (0.764 vs current 0.748). Transductive setting: pseudo-labels from test set SC outputs.\", \"spec\": {\"command\": \"llamafactory-cli train train_config_scd_fewnerd_s42.yaml\", \"server\": \"autodl-5090-b\", \"gpu_ids\": [0], \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/data/scd_fewnerd_theta2n_s42.jsonl\", \"data_count\": 32565, \"model_name\": \"Qwen3-8B-FT\", \"seed\": 42, \"pid\": 207109}, \"reproduce\": {\"finished_at\": \"2026-05-20T19:13:25.333Z\"}, \"failure_reason\": \"RETRACTED: cron false positive — training completed successfully (4706/4706 steps, train_loss=0.023, eval_loss=0.0329). Original: process dead 5× with no sentinel/W&B\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-20T19:13:26.395Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-20T19:13:35.804759+00:00\"}]}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.5166}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "771496a1-f1bf-4bb6-bef1-5e48381c3b69",
  "isSidechain": false,
  "promptId": "d2210c4d-d5b9-450f-8450-2f1ffe6e0ccd",
  "type": "user",
  "uuid": "f3dfc75c-586c-4073-86f7-b825a44e5756",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"exp_id\\\": \\\"exp_b1_scd_fewnerd_standard\\\", \\\"experiment\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-20T11:17:37.804Z\\\", \\\"updated_at\\\": \\\"2026-05-20T19:16:20.137Z\\\", \\\"hypothesis\\\": \\\"Standard Self-Consistency Distillation on FewNERD: fine-tune Qwen3-8B-FT with theta2n construction pseudo-labels (32,565 instances) mixed 1:1 with gold data. Greedy F1 after SCD should approach N=8 construction F1 (0.764 vs current 0.748). Transductive setting: pseudo-labels from test set SC outputs.\\\", \\\"spec\\\": {\\\"command\\\": \\\"llamafactory-cli train train_config_scd_fewnerd_s42.yaml\\\", \\\"server\\\": \\\"autodl-5090-b\\\", \\\"gpu_ids\\\": [0], \\\"data_path\\\": \\\"/root/autodl-tmp/struct_self_consist_ie/data/scd_fewnerd_theta2n_s42.jsonl\\\", \\\"data_count\\\": 32565, \\\"model_name\\\": \\\"Qwen3-8B-FT\\\", \\\"seed\\\": 42, \\\"pid\\\": 207109}, \\\"reproduce\\\": {\\\"finished_at\\\": \\\"2026-05-20T19:13:25.333Z\\\"}, \\\"failure_reason\\\": \\\"RETRACTED: cron false positive — training completed successfully (4706/4706 steps, train_loss=0.023, eval_loss=0.0329). Original: process dead 5× with no sentinel/W&B\\\", \\\"conclusion\\\": \\\"failed\\\", \\\"completed_at\\\": \\\"2026-05-20T19:13:26.395Z\\\", \\\"extra\\\": {\\\"hook_events\\\": [{\\\"event\\\": \\\"on_failed\\\", \\\"action\\\": \\\"agent\\\", \\\"ts\\\": \\\"2026-05-20T19:13:35.804759+00:00\\\"}]}}}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 1.5166}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"exp_id\": \"exp_b1_scd_fewnerd_standard\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T11:17:37.804Z\", \"updated_at\": \"2026-05-20T19:16:20.137Z\", \"hypothesis\": \"Standard Self-Consistency Distillation on FewNERD: fine-tune Qwen3-8B-FT with theta2n construction pseudo-labels (32,565 instances) mixed 1:1 with gold data. Greedy F1 after SCD should approach N=8 construction F1 (0.764 vs current 0.748). Transductive setting: pseudo-labels from test set SC outputs.\", \"spec\": {\"command\": \"llamafactory-cli train train_config_scd_fewnerd_s42.yaml\", \"server\": \"autodl-5090-b\", \"gpu_ids\": [0], \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/data/scd_fewnerd_theta2n_s42.jsonl\", \"data_count\": 32565, \"model_name\": \"Qwen3-8B-FT\", \"seed\": 42, \"pid\": 207109}, \"reproduce\": {\"finished_at\": \"2026-05-20T19:13:25.333Z\"}, \"failure_reason\": \"RETRACTED: cron false positive — training completed successfully (4706/4706 steps, train_loss=0.023, eval_loss=0.0329). Original: process dead 5× with no sentinel/W&B\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-20T19:13:26.395Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-20T19:13:35.804759+00:00\"}]}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.5166}}"
    }
  },
  "sourceToolAssistantUUID": "771496a1-f1bf-4bb6-bef1-5e48381c3b69",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/agent_5c567c58",
  "sessionId": "bb8bc777-37fb-4956-b48e-5e9c5a98dd73",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 77 · 2026-05-20T19:16:21.441Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry · `toolu_01BapV5xHMzncuLrJSnVdbo4`</summary>

```json
{
  "exp_id": "exp_b1_scd_fewnerd_standard",
  "field": "notes",
  "value": "训练正常完成。Cron 误判 failed（无 W&B sentinel）。4706/4706 steps, train_loss=0.023, eval_loss=0.0329, 7h08m。Checkpoint: /root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen3-8b-fewnerd-scd-lora/。需要 eval inference 验证 greedy F1。",
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f3dfc75c-586c-4073-86f7-b825a44e5756",
  "isSidechain": false,
  "requestId": "req_011CbEMd1CH8bSr81Y3o9Kn4",
  "type": "assistant",
  "uuid": "5e5a06a7-1ca2-4ae4-a9f7-6e6263da26cb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/agent_5c567c58",
  "sessionId": "bb8bc777-37fb-4956-b48e-5e9c5a98dd73",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XA44qB9HjDXZtgzSBnty4r",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5678,
      "cache_read_input_tokens": 61819,
      "output_tokens": 2347,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5678,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2347,
          "cache_read_input_tokens": 61819,
          "cache_creation_input_tokens": 5678,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5678
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

_source line 78 · 2026-05-20T19:16:22.384Z_

<details><summary>↩ Tool result · `toolu_01BapV5xHMzncuLrJSnVdbo4`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"exp_id\": \"exp_b1_scd_fewnerd_standard\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T11:17:37.804Z\", \"updated_at\": \"2026-05-20T19:16:21.974Z\", \"hypothesis\": \"Standard Self-Consistency Distillation on FewNERD: fine-tune Qwen3-8B-FT with theta2n construction pseudo-labels (32,565 instances) mixed 1:1 with gold data. Greedy F1 after SCD should approach N=8 construction F1 (0.764 vs current 0.748). Transductive setting: pseudo-labels from test set SC outputs.\", \"spec\": {\"command\": \"llamafactory-cli train train_config_scd_fewnerd_s42.yaml\", \"server\": \"autodl-5090-b\", \"gpu_ids\": [0], \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/data/scd_fewnerd_theta2n_s42.jsonl\", \"data_count\": 32565, \"model_name\": \"Qwen3-8B-FT\", \"seed\": 42, \"pid\": 207109}, \"reproduce\": {\"finished_at\": \"2026-05-20T19:13:25.333Z\"}, \"failure_reason\": \"RETRACTED: cron false positive — training completed successfully (4706/4706 steps, train_loss=0.023, eval_loss=0.0329). Original: process dead 5× with no sentinel/W&B\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-20T19:13:26.395Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-20T19:13:35.804759+00:00\"}]}, \"notes\": \"训练正常完成。Cron 误判 failed（无 W&B sentinel）。4706/4706 steps, train_loss=0.023, eval_loss=0.0329, 7h08m。Checkpoint: /root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen3-8b-fewnerd-scd-lora/。需要 eval inference 验证 greedy F1。\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.933}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5e5a06a7-1ca2-4ae4-a9f7-6e6263da26cb",
  "isSidechain": false,
  "promptId": "d2210c4d-d5b9-450f-8450-2f1ffe6e0ccd",
  "type": "user",
  "uuid": "73ad3c25-afc9-40b2-b1e5-f1a777c04dba",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"exp_id\\\": \\\"exp_b1_scd_fewnerd_standard\\\", \\\"experiment\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-20T11:17:37.804Z\\\", \\\"updated_at\\\": \\\"2026-05-20T19:16:21.974Z\\\", \\\"hypothesis\\\": \\\"Standard Self-Consistency Distillation on FewNERD: fine-tune Qwen3-8B-FT with theta2n construction pseudo-labels (32,565 instances) mixed 1:1 with gold data. Greedy F1 after SCD should approach N=8 construction F1 (0.764 vs current 0.748). Transductive setting: pseudo-labels from test set SC outputs.\\\", \\\"spec\\\": {\\\"command\\\": \\\"llamafactory-cli train train_config_scd_fewnerd_s42.yaml\\\", \\\"server\\\": \\\"autodl-5090-b\\\", \\\"gpu_ids\\\": [0], \\\"data_path\\\": \\\"/root/autodl-tmp/struct_self_consist_ie/data/scd_fewnerd_theta2n_s42.jsonl\\\", \\\"data_count\\\": 32565, \\\"model_name\\\": \\\"Qwen3-8B-FT\\\", \\\"seed\\\": 42, \\\"pid\\\": 207109}, \\\"reproduce\\\": {\\\"finished_at\\\": \\\"2026-05-20T19:13:25.333Z\\\"}, \\\"failure_reason\\\": \\\"RETRACTED: cron false positive — training completed successfully (4706/4706 steps, train_loss=0.023, eval_loss=0.0329). Original: process dead 5× with no sentinel/W&B\\\", \\\"conclusion\\\": \\\"failed\\\", \\\"completed_at\\\": \\\"2026-05-20T19:13:26.395Z\\\", \\\"extra\\\": {\\\"hook_events\\\": [{\\\"event\\\": \\\"on_failed\\\", \\\"action\\\": \\\"agent\\\", \\\"ts\\\": \\\"2026-05-20T19:13:35.804759+00:00\\\"}]}, \\\"notes\\\": \\\"训练正常完成。Cron 误判 failed（无 W&B sentinel）。4706/4706 steps, train_loss=0.023, eval_loss=0.0329, 7h08m。Checkpoint: /root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen3-8b-fewnerd-scd-lora/。需要 eval inference 验证 greedy F1。\\\"}}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.933}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"exp_id\": \"exp_b1_scd_fewnerd_standard\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T11:17:37.804Z\", \"updated_at\": \"2026-05-20T19:16:21.974Z\", \"hypothesis\": \"Standard Self-Consistency Distillation on FewNERD: fine-tune Qwen3-8B-FT with theta2n construction pseudo-labels (32,565 instances) mixed 1:1 with gold data. Greedy F1 after SCD should approach N=8 construction F1 (0.764 vs current 0.748). Transductive setting: pseudo-labels from test set SC outputs.\", \"spec\": {\"command\": \"llamafactory-cli train train_config_scd_fewnerd_s42.yaml\", \"server\": \"autodl-5090-b\", \"gpu_ids\": [0], \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/data/scd_fewnerd_theta2n_s42.jsonl\", \"data_count\": 32565, \"model_name\": \"Qwen3-8B-FT\", \"seed\": 42, \"pid\": 207109}, \"reproduce\": {\"finished_at\": \"2026-05-20T19:13:25.333Z\"}, \"failure_reason\": \"RETRACTED: cron false positive — training completed successfully (4706/4706 steps, train_loss=0.023, eval_loss=0.0329). Original: process dead 5× with no sentinel/W&B\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-20T19:13:26.395Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-20T19:13:35.804759+00:00\"}]}, \"notes\": \"训练正常完成。Cron 误判 failed（无 W&B sentinel）。4706/4706 steps, train_loss=0.023, eval_loss=0.0329, 7h08m。Checkpoint: /root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen3-8b-fewnerd-scd-lora/。需要 eval inference 验证 greedy F1。\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.933}}"
    }
  },
  "sourceToolAssistantUUID": "5e5a06a7-1ca2-4ae4-a9f7-6e6263da26cb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/agent_5c567c58",
  "sessionId": "bb8bc777-37fb-4956-b48e-5e9c5a98dd73",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 79 · 2026-05-20T19:16:22.903Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry · `toolu_01A2DUNUthFNjizZ83nHoswj`</summary>

```json
{
  "exp_id": "exp_b1_scd_fewnerd_standard",
  "field": "metrics",
  "value": {
    "train_loss": 0.023,
    "eval_loss": 0.0329,
    "steps": 4706,
    "epochs": 2,
    "train_runtime_hours": 7.14
  },
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "73ad3c25-afc9-40b2-b1e5-f1a777c04dba",
  "isSidechain": false,
  "requestId": "req_011CbEMd1CH8bSr81Y3o9Kn4",
  "type": "assistant",
  "uuid": "3b401563-fa58-4644-86b4-ee656a327962",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/agent_5c567c58",
  "sessionId": "bb8bc777-37fb-4956-b48e-5e9c5a98dd73",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XA44qB9HjDXZtgzSBnty4r",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5678,
      "cache_read_input_tokens": 61819,
      "output_tokens": 2347,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5678,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2347,
          "cache_read_input_tokens": 61819,
          "cache_creation_input_tokens": 5678,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5678
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

_source line 80 · 2026-05-20T19:16:23.848Z_

<details><summary>↩ Tool result · `toolu_01A2DUNUthFNjizZ83nHoswj`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"exp_id\": \"exp_b1_scd_fewnerd_standard\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T11:17:37.804Z\", \"updated_at\": \"2026-05-20T19:16:23.475Z\", \"hypothesis\": \"Standard Self-Consistency Distillation on FewNERD: fine-tune Qwen3-8B-FT with theta2n construction pseudo-labels (32,565 instances) mixed 1:1 with gold data. Greedy F1 after SCD should approach N=8 construction F1 (0.764 vs current 0.748). Transductive setting: pseudo-labels from test set SC outputs.\", \"spec\": {\"command\": \"llamafactory-cli train train_config_scd_fewnerd_s42.yaml\", \"server\": \"autodl-5090-b\", \"gpu_ids\": [0], \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/data/scd_fewnerd_theta2n_s42.jsonl\", \"data_count\": 32565, \"model_name\": \"Qwen3-8B-FT\", \"seed\": 42, \"pid\": 207109}, \"reproduce\": {\"finished_at\": \"2026-05-20T19:13:25.333Z\"}, \"failure_reason\": \"RETRACTED: cron false positive — training completed successfully (4706/4706 steps, train_loss=0.023, eval_loss=0.0329). Original: process dead 5× with no sentinel/W&B\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-20T19:13:26.395Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-20T19:13:35.804759+00:00\"}]}, \"notes\": \"训练正常完成。Cron 误判 failed（无 W&B sentinel）。4706/4706 steps, train_loss=0.023, eval_loss=0.0329, 7h08m。Checkpoint: /root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen3-8b-fewnerd-scd-lora/。需要 eval inference 验证 greedy F1。\", \"metrics\": {\"train_loss\": 0.023, \"eval_loss\": 0.0329, \"steps\": 4706, \"epochs\": 2, \"train_runtime_hours\": 7.14}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.9359}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3b401563-fa58-4644-86b4-ee656a327962",
  "isSidechain": false,
  "promptId": "d2210c4d-d5b9-450f-8450-2f1ffe6e0ccd",
  "type": "user",
  "uuid": "a3aadffa-16a8-4c31-87ff-c601582ced32",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"exp_id\\\": \\\"exp_b1_scd_fewnerd_standard\\\", \\\"experiment\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-20T11:17:37.804Z\\\", \\\"updated_at\\\": \\\"2026-05-20T19:16:23.475Z\\\", \\\"hypothesis\\\": \\\"Standard Self-Consistency Distillation on FewNERD: fine-tune Qwen3-8B-FT with theta2n construction pseudo-labels (32,565 instances) mixed 1:1 with gold data. Greedy F1 after SCD should approach N=8 construction F1 (0.764 vs current 0.748). Transductive setting: pseudo-labels from test set SC outputs.\\\", \\\"spec\\\": {\\\"command\\\": \\\"llamafactory-cli train train_config_scd_fewnerd_s42.yaml\\\", \\\"server\\\": \\\"autodl-5090-b\\\", \\\"gpu_ids\\\": [0], \\\"data_path\\\": \\\"/root/autodl-tmp/struct_self_consist_ie/data/scd_fewnerd_theta2n_s42.jsonl\\\", \\\"data_count\\\": 32565, \\\"model_name\\\": \\\"Qwen3-8B-FT\\\", \\\"seed\\\": 42, \\\"pid\\\": 207109}, \\\"reproduce\\\": {\\\"finished_at\\\": \\\"2026-05-20T19:13:25.333Z\\\"}, \\\"failure_reason\\\": \\\"RETRACTED: cron false positive — training completed successfully (4706/4706 steps, train_loss=0.023, eval_loss=0.0329). Original: process dead 5× with no sentinel/W&B\\\", \\\"conclusion\\\": \\\"failed\\\", \\\"completed_at\\\": \\\"2026-05-20T19:13:26.395Z\\\", \\\"extra\\\": {\\\"hook_events\\\": [{\\\"event\\\": \\\"on_failed\\\", \\\"action\\\": \\\"agent\\\", \\\"ts\\\": \\\"2026-05-20T19:13:35.804759+00:00\\\"}]}, \\\"notes\\\": \\\"训练正常完成。Cron 误判 failed（无 W&B sentinel）。4706/4706 steps, train_loss=0.023, eval_loss=0.0329, 7h08m。Checkpoint: /root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen3-8b-fewnerd-scd-lora/。需要 eval inference 验证 greedy F1。\\\", \\\"metrics\\\": {\\\"train_loss\\\": 0.023, \\\"eval_loss\\\": 0.0329, \\\"steps\\\": 4706, \\\"epochs\\\": 2, \\\"train_runtime_hours\\\": 7.14}}}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.9359}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"exp_id\": \"exp_b1_scd_fewnerd_standard\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T11:17:37.804Z\", \"updated_at\": \"2026-05-20T19:16:23.475Z\", \"hypothesis\": \"Standard Self-Consistency Distillation on FewNERD: fine-tune Qwen3-8B-FT with theta2n construction pseudo-labels (32,565 instances) mixed 1:1 with gold data. Greedy F1 after SCD should approach N=8 construction F1 (0.764 vs current 0.748). Transductive setting: pseudo-labels from test set SC outputs.\", \"spec\": {\"command\": \"llamafactory-cli train train_config_scd_fewnerd_s42.yaml\", \"server\": \"autodl-5090-b\", \"gpu_ids\": [0], \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/data/scd_fewnerd_theta2n_s42.jsonl\", \"data_count\": 32565, \"model_name\": \"Qwen3-8B-FT\", \"seed\": 42, \"pid\": 207109}, \"reproduce\": {\"finished_at\": \"2026-05-20T19:13:25.333Z\"}, \"failure_reason\": \"RETRACTED: cron false positive — training completed successfully (4706/4706 steps, train_loss=0.023, eval_loss=0.0329). Original: process dead 5× with no sentinel/W&B\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-20T19:13:26.395Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-20T19:13:35.804759+00:00\"}]}, \"notes\": \"训练正常完成。Cron 误判 failed（无 W&B sentinel）。4706/4706 steps, train_loss=0.023, eval_loss=0.0329, 7h08m。Checkpoint: /root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen3-8b-fewnerd-scd-lora/。需要 eval inference 验证 greedy F1。\", \"metrics\": {\"train_loss\": 0.023, \"eval_loss\": 0.0329, \"steps\": 4706, \"epochs\": 2, \"train_runtime_hours\": 7.14}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.9359}}"
    }
  },
  "sourceToolAssistantUUID": "3b401563-fa58-4644-86b4-ee656a327962",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/agent_5c567c58",
  "sessionId": "bb8bc777-37fb-4956-b48e-5e9c5a98dd73",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 81 · 2026-05-20T19:16:27.211Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry · `toolu_01CXfxe1Zgy9p6JCj8PDFc74`</summary>

```json
{
  "exp_id": "exp_b1_scd_fewnerd_standard",
  "field": "spec",
  "value": {
    "command": "llamafactory-cli train train_config_scd_fewnerd_s42.yaml",
    "server": "autodl-5090-b",
    "gpu_ids": [
      0
    ],
    "data_path": "/root/autodl-tmp/struct_self_consist_ie/data/scd_fewnerd_theta2n_s42.jsonl",
    "data_count": 32565,
    "model_name": "Qwen3-8B-FT",
    "seed": 42,
    "pid": 207109,
    "checkpoint_path": "/root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen3-8b-fewnerd-scd-lora/"
  },
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a3aadffa-16a8-4c31-87ff-c601582ced32",
  "isSidechain": false,
  "requestId": "req_011CbEMd1CH8bSr81Y3o9Kn4",
  "type": "assistant",
  "uuid": "bc8ae9dd-6c95-456f-9b87-e1685605320f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/agent_5c567c58",
  "sessionId": "bb8bc777-37fb-4956-b48e-5e9c5a98dd73",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XA44qB9HjDXZtgzSBnty4r",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5678,
      "cache_read_input_tokens": 61819,
      "output_tokens": 2347,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5678,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2347,
          "cache_read_input_tokens": 61819,
          "cache_creation_input_tokens": 5678,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5678
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

_source line 82 · 2026-05-20T19:16:27.222Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_project_resource_usage · `toolu_01AAsS1eyw74huZSR8FadU39`</summary>

```json
{
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bc8ae9dd-6c95-456f-9b87-e1685605320f",
  "isSidechain": false,
  "requestId": "req_011CbEMd1CH8bSr81Y3o9Kn4",
  "type": "assistant",
  "uuid": "fc6abdfb-c588-4c26-8b46-428d1b26c0b8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/agent_5c567c58",
  "sessionId": "bb8bc777-37fb-4956-b48e-5e9c5a98dd73",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XA44qB9HjDXZtgzSBnty4r",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5678,
      "cache_read_input_tokens": 61819,
      "output_tokens": 2347,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5678,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2347,
          "cache_read_input_tokens": 61819,
          "cache_creation_input_tokens": 5678,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5678
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

### Runtime record

_source line 83_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[CRON] 实验进程异常退出（失败），需要你诊断原因。 详情: Process exited without valid W&B metrics  - exp_id: exp_b1_scd_fewnerd_standard - project: struct_self_consist_ie - server: autodl-5090-b - log_path: /root/autodl-tmp/…",
  "leafUuid": "fc6abdfb-c588-4c26-8b46-428d1b26c0b8",
  "sessionId": "bb8bc777-37fb-4956-b48e-5e9c5a98dd73"
}
```

---

### Runtime record

_source line 84_

```json
{
  "type": "ai-title",
  "aiTitle": "Diagnose experiment process exit failure",
  "sessionId": "bb8bc777-37fb-4956-b48e-5e9c5a98dd73"
}
```

---

### Tool result

_source line 85 · 2026-05-20T19:16:28.210Z_

<details><summary>↩ Tool result · `toolu_01CXfxe1Zgy9p6JCj8PDFc74`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"exp_id\": \"exp_b1_scd_fewnerd_standard\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T11:17:37.804Z\", \"updated_at\": \"2026-05-20T19:16:27.799Z\", \"hypothesis\": \"Standard Self-Consistency Distillation on FewNERD: fine-tune Qwen3-8B-FT with theta2n construction pseudo-labels (32,565 instances) mixed 1:1 with gold data. Greedy F1 after SCD should approach N=8 construction F1 (0.764 vs current 0.748). Transductive setting: pseudo-labels from test set SC outputs.\", \"spec\": {\"command\": \"llamafactory-cli train train_config_scd_fewnerd_s42.yaml\", \"server\": \"autodl-5090-b\", \"gpu_ids\": [0], \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/data/scd_fewnerd_theta2n_s42.jsonl\", \"data_count\": 32565, \"model_name\": \"Qwen3-8B-FT\", \"seed\": 42, \"pid\": 207109, \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen3-8b-fewnerd-scd-lora/\"}, \"reproduce\": {\"finished_at\": \"2026-05-20T19:13:25.333Z\"}, \"failure_reason\": \"RETRACTED: cron false positive — training completed successfully (4706/4706 steps, train_loss=0.023, eval_loss=0.0329). Original: process dead 5× with no sentinel/W&B\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-20T19:13:26.395Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-20T19:13:35.804759+00:00\"}]}, \"notes\": \"训练正常完成。Cron 误判 failed（无 W&B sentinel）。4706/4706 steps, train_loss=0.023, eval_loss=0.0329, 7h08m。Checkpoint: /root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen3-8b-fewnerd-scd-lora/。需要 eval inference 验证 greedy F1。\", \"metrics\": {\"train_loss\": 0.023, \"eval_loss\": 0.0329, \"steps\": 4706, \"epochs\": 2, \"train_runtime_hours\": 7.14}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.9794}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bc8ae9dd-6c95-456f-9b87-e1685605320f",
  "isSidechain": false,
  "promptId": "d2210c4d-d5b9-450f-8450-2f1ffe6e0ccd",
  "type": "user",
  "uuid": "866b63d9-a1a9-4003-a1fa-990c110cafd9",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"exp_id\\\": \\\"exp_b1_scd_fewnerd_standard\\\", \\\"experiment\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-20T11:17:37.804Z\\\", \\\"updated_at\\\": \\\"2026-05-20T19:16:27.799Z\\\", \\\"hypothesis\\\": \\\"Standard Self-Consistency Distillation on FewNERD: fine-tune Qwen3-8B-FT with theta2n construction pseudo-labels (32,565 instances) mixed 1:1 with gold data. Greedy F1 after SCD should approach N=8 construction F1 (0.764 vs current 0.748). Transductive setting: pseudo-labels from test set SC outputs.\\\", \\\"spec\\\": {\\\"command\\\": \\\"llamafactory-cli train train_config_scd_fewnerd_s42.yaml\\\", \\\"server\\\": \\\"autodl-5090-b\\\", \\\"gpu_ids\\\": [0], \\\"data_path\\\": \\\"/root/autodl-tmp/struct_self_consist_ie/data/scd_fewnerd_theta2n_s42.jsonl\\\", \\\"data_count\\\": 32565, \\\"model_name\\\": \\\"Qwen3-8B-FT\\\", \\\"seed\\\": 42, \\\"pid\\\": 207109, \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen3-8b-fewnerd-scd-lora/\\\"}, \\\"reproduce\\\": {\\\"finished_at\\\": \\\"2026-05-20T19:13:25.333Z\\\"}, \\\"failure_reason\\\": \\\"RETRACTED: cron false positive — training completed successfully (4706/4706 steps, train_loss=0.023, eval_loss=0.0329). Original: process dead 5× with no sentinel/W&B\\\", \\\"conclusion\\\": \\\"failed\\\", \\\"completed_at\\\": \\\"2026-05-20T19:13:26.395Z\\\", \\\"extra\\\": {\\\"hook_events\\\": [{\\\"event\\\": \\\"on_failed\\\", \\\"action\\\": \\\"agent\\\", \\\"ts\\\": \\\"2026-05-20T19:13:35.804759+00:00\\\"}]}, \\\"notes\\\": \\\"训练正常完成。Cron 误判 failed（无 W&B sentinel）。4706/4706 steps, train_loss=0.023, eval_loss=0.0329, 7h08m。Checkpoint: /root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen3-8b-fewnerd-scd-lora/。需要 eval inference 验证 greedy F1。\\\", \\\"metrics\\\": {\\\"train_loss\\\": 0.023, \\\"eval_loss\\\": 0.0329, \\\"steps\\\": 4706, \\\"epochs\\\": 2, \\\"train_runtime_hours\\\": 7.14}}}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.9794}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"exp_id\": \"exp_b1_scd_fewnerd_standard\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T11:17:37.804Z\", \"updated_at\": \"2026-05-20T19:16:27.799Z\", \"hypothesis\": \"Standard Self-Consistency Distillation on FewNERD: fine-tune Qwen3-8B-FT with theta2n construction pseudo-labels (32,565 instances) mixed 1:1 with gold data. Greedy F1 after SCD should approach N=8 construction F1 (0.764 vs current 0.748). Transductive setting: pseudo-labels from test set SC outputs.\", \"spec\": {\"command\": \"llamafactory-cli train train_config_scd_fewnerd_s42.yaml\", \"server\": \"autodl-5090-b\", \"gpu_ids\": [0], \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/data/scd_fewnerd_theta2n_s42.jsonl\", \"data_count\": 32565, \"model_name\": \"Qwen3-8B-FT\", \"seed\": 42, \"pid\": 207109, \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen3-8b-fewnerd-scd-lora/\"}, \"reproduce\": {\"finished_at\": \"2026-05-20T19:13:25.333Z\"}, \"failure_reason\": \"RETRACTED: cron false positive — training completed successfully (4706/4706 steps, train_loss=0.023, eval_loss=0.0329). Original: process dead 5× with no sentinel/W&B\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-20T19:13:26.395Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-20T19:13:35.804759+00:00\"}]}, \"notes\": \"训练正常完成。Cron 误判 failed（无 W&B sentinel）。4706/4706 steps, train_loss=0.023, eval_loss=0.0329, 7h08m。Checkpoint: /root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen3-8b-fewnerd-scd-lora/。需要 eval inference 验证 greedy F1。\", \"metrics\": {\"train_loss\": 0.023, \"eval_loss\": 0.0329, \"steps\": 4706, \"epochs\": 2, \"train_runtime_hours\": 7.14}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.9794}}"
    }
  },
  "sourceToolAssistantUUID": "bc8ae9dd-6c95-456f-9b87-e1685605320f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/agent_5c567c58",
  "sessionId": "bb8bc777-37fb-4956-b48e-5e9c5a98dd73",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 86 · 2026-05-20T19:16:28.905Z_

<details><summary>↩ Tool result · `toolu_01AAsS1eyw74huZSR8FadU39`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"allocated_gpus\": [{\"server\": \"autodl-5090\", \"gpu_id\": \"cuda:0\"}, {\"server\": \"autodl-5090\", \"gpu_id\": \"cuda:1\"}, {\"server\": \"autodl-5090\", \"gpu_id\": \"cuda:2\"}, {\"server\": \"autodl-5090\", \"gpu_id\": \"cuda:3\"}, {\"server\": \"autodl-5090-b\", \"gpu_id\": \"cuda:0\"}, {\"server\": \"autodl-5090-b\", \"gpu_id\": \"cuda:1\"}, {\"server\": \"autodl-5090-b\", \"gpu_id\": \"cuda:2\"}, {\"server\": \"autodl-5090-b\", \"gpu_id\": \"cuda:3\"}, {\"server\": \"autodl-5090-c\", \"gpu_id\": \"cuda:0\"}, {\"server\": \"autodl-5090-c\", \"gpu_id\": \"cuda:1\"}, {\"server\": \"autodl-5090-c\", \"gpu_id\": \"cuda:2\"}, {\"server\": \"autodl-5090-c\", \"gpu_id\": \"cuda:3\"}], \"actually_running_gpus\": [{\"server\": \"autodl-5090\", \"gpu_id\": \"cuda:0\", \"exp_id\": \"exp_qwen25_32b_fewnerd\"}, {\"server\": \"autodl-5090\", \"gpu_id\": \"cuda:1\", \"exp_id\": \"exp_qwen25_32b_fewnerd\"}, {\"server\": \"autodl-5090\", \"gpu_id\": \"cuda:2\", \"exp_id\": \"exp_qwen25_32b_fewnerd\"}, {\"server\": \"autodl-5090\", \"gpu_id\": \"cuda:3\", \"exp_id\": \"exp_qwen25_32b_fewnerd\"}, {\"server\": \"autodl-5090-c\", \"gpu_id\": \"cuda:2\", \"exp_id\": \"exp_tlow_fewnerd_inference\"}], \"allocated_but_idle\": [{\"server\": \"autodl-5090-b\", \"gpu_id\": \"cuda:0\", \"idle_min\": null, \"util_pct\": null}, {\"server\": \"autodl-5090-b\", \"gpu_id\": \"cuda:1\", \"idle_min\": null, \"util_pct\": null}, {\"server\": \"autodl-5090-b\", \"gpu_id\": \"cuda:2\", \"idle_min\": null, \"util_pct\": null}, {\"server\": \"autodl-5090-b\", \"gpu_id\": \"cuda:3\", \"idle_min\": null, \"util_pct\": null}, {\"server\": \"autodl-5090-c\", \"gpu_id\": \"cuda:0\", \"idle_min\": null, \"util_pct\": null}, {\"server\": \"autodl-5090-c\", \"gpu_id\": \"cuda:1\", \"idle_min\": null, \"util_pct\": null}, {\"server\": \"autodl-5090-c\", \"gpu_id\": \"cuda:3\", \"idle_min\": null, \"util_pct\": null}], \"registered_but_hw_idle\": [], \"unregistered_but_hw_active\": [], \"running_experiments\": [{\"exp_id\": \"exp_qwen25_32b_fewnerd\", \"gpus\": [\"cuda:0\", \"cuda:1\", \"cuda:2\", \"cuda:3\"], \"util_avg\": null}, {\"exp_id\": \"exp_tlow_fewnerd_inference\", \"gpus\": [\"cuda:2\"], \"util_avg\": null}], \"worker_pool\": {\"total\": 1, \"gpu_tasks\": 0, \"cpu_tasks\": 1, \"details\": [{\"worker_id\": \"worker_diagnose_exp_b1_scd_fewnerd_curriculum_q_20260520T190612\", \"task\": \"diagnose:exp_b1_scd_fewnerd_curriculum_q\"}]}, \"summary\": \"分配 12 张, 实际跑 5 张 ⚠️ | Worker 1 (GPU 0 / CPU 1)\"}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fc6abdfb-c588-4c26-8b46-428d1b26c0b8",
  "isSidechain": false,
  "promptId": "d2210c4d-d5b9-450f-8450-2f1ffe6e0ccd",
  "type": "user",
  "uuid": "a19dacac-4761-4ae7-9aad-aefbd0685ff0",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"allocated_gpus\\\": [{\\\"server\\\": \\\"autodl-5090\\\", \\\"gpu_id\\\": \\\"cuda:0\\\"}, {\\\"server\\\": \\\"autodl-5090\\\", \\\"gpu_id\\\": \\\"cuda:1\\\"}, {\\\"server\\\": \\\"autodl-5090\\\", \\\"gpu_id\\\": \\\"cuda:2\\\"}, {\\\"server\\\": \\\"autodl-5090\\\", \\\"gpu_id\\\": \\\"cuda:3\\\"}, {\\\"server\\\": \\\"autodl-5090-b\\\", \\\"gpu_id\\\": \\\"cuda:0\\\"}, {\\\"server\\\": \\\"autodl-5090-b\\\", \\\"gpu_id\\\": \\\"cuda:1\\\"}, {\\\"server\\\": \\\"autodl-5090-b\\\", \\\"gpu_id\\\": \\\"cuda:2\\\"}, {\\\"server\\\": \\\"autodl-5090-b\\\", \\\"gpu_id\\\": \\\"cuda:3\\\"}, {\\\"server\\\": \\\"autodl-5090-c\\\", \\\"gpu_id\\\": \\\"cuda:0\\\"}, {\\\"server\\\": \\\"autodl-5090-c\\\", \\\"gpu_id\\\": \\\"cuda:1\\\"}, {\\\"server\\\": \\\"autodl-5090-c\\\", \\\"gpu_id\\\": \\\"cuda:2\\\"}, {\\\"server\\\": \\\"autodl-5090-c\\\", \\\"gpu_id\\\": \\\"cuda:3\\\"}], \\\"actually_running_gpus\\\": [{\\\"server\\\": \\\"autodl-5090\\\", \\\"gpu_id\\\": \\\"cuda:0\\\", \\\"exp_id\\\": \\\"exp_qwen25_32b_fewnerd\\\"}, {\\\"server\\\": \\\"autodl-5090\\\", \\\"gpu_id\\\": \\\"cuda:1\\\", \\\"exp_id\\\": \\\"exp_qwen25_32b_fewnerd\\\"}, {\\\"server\\\": \\\"autodl-5090\\\", \\\"gpu_id\\\": \\\"cuda:2\\\", \\\"exp_id\\\": \\\"exp_qwen25_32b_fewnerd\\\"}, {\\\"server\\\": \\\"autodl-5090\\\", \\\"gpu_id\\\": \\\"cuda:3\\\", \\\"exp_id\\\": \\\"exp_qwen25_32b_fewnerd\\\"}, {\\\"server\\\": \\\"autodl-5090-c\\\", \\\"gpu_id\\\": \\\"cuda:2\\\", \\\"exp_id\\\": \\\"exp_tlow_fewnerd_inference\\\"}], \\\"allocated_but_idle\\\": [{\\\"server\\\": \\\"autodl-5090-b\\\", \\\"gpu_id\\\": \\\"cuda:0\\\", \\\"idle_min\\\": null, \\\"util_pct\\\": null}, {\\\"server\\\": \\\"autodl-5090-b\\\", \\\"gpu_id\\\": \\\"cuda:1\\\", \\\"idle_min\\\": null, \\\"util_pct\\\": null}, {\\\"server\\\": \\\"autodl-5090-b\\\", \\\"gpu_id\\\": \\\"cuda:2\\\", \\\"idle_min\\\": null, \\\"util_pct\\\": null}, {\\\"server\\\": \\\"autodl-5090-b\\\", \\\"gpu_id\\\": \\\"cuda:3\\\", \\\"idle_min\\\": null, \\\"util_pct\\\": null}, {\\\"server\\\": \\\"autodl-5090-c\\\", \\\"gpu_id\\\": \\\"cuda:0\\\", \\\"idle_min\\\": null, \\\"util_pct\\\": null}, {\\\"server\\\": \\\"autodl-5090-c\\\", \\\"gpu_id\\\": \\\"cuda:1\\\", \\\"idle_min\\\": null, \\\"util_pct\\\": null}, {\\\"server\\\": \\\"autodl-5090-c\\\", \\\"gpu_id\\\": \\\"cuda:3\\\", \\\"idle_min\\\": null, \\\"util_pct\\\": null}], \\\"registered_but_hw_idle\\\": [], \\\"unregistered_but_hw_active\\\": [], \\\"running_experiments\\\": [{\\\"exp_id\\\": \\\"exp_qwen25_32b_fewnerd\\\", \\\"gpus\\\": [\\\"cuda:0\\\", \\\"cuda:1\\\", \\\"cuda:2\\\", \\\"cuda:3\\\"], \\\"util_avg\\\": null}, {\\\"exp_id\\\": \\\"exp_tlow_fewnerd_inference\\\", \\\"gpus\\\": [\\\"cuda:2\\\"], \\\"util_avg\\\": null}], \\\"worker_pool\\\": {\\\"total\\\": 1, \\\"gpu_tasks\\\": 0, \\\"cpu_tasks\\\": 1, \\\"details\\\": [{\\\"worker_id\\\": \\\"worker_diagnose_exp_b1_scd_fewnerd_curriculum_q_20260520T190612\\\", \\\"task\\\": \\\"diagnose:exp_b1_scd_fewnerd_curriculum_q\\\"}]}, \\\"summary\\\": \\\"分配 12 张, 实际跑 5 张 ⚠️ | Worker 1 (GPU 0 / CPU 1)\\\"}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"allocated_gpus\": [{\"server\": \"autodl-5090\", \"gpu_id\": \"cuda:0\"}, {\"server\": \"autodl-5090\", \"gpu_id\": \"cuda:1\"}, {\"server\": \"autodl-5090\", \"gpu_id\": \"cuda:2\"}, {\"server\": \"autodl-5090\", \"gpu_id\": \"cuda:3\"}, {\"server\": \"autodl-5090-b\", \"gpu_id\": \"cuda:0\"}, {\"server\": \"autodl-5090-b\", \"gpu_id\": \"cuda:1\"}, {\"server\": \"autodl-5090-b\", \"gpu_id\": \"cuda:2\"}, {\"server\": \"autodl-5090-b\", \"gpu_id\": \"cuda:3\"}, {\"server\": \"autodl-5090-c\", \"gpu_id\": \"cuda:0\"}, {\"server\": \"autodl-5090-c\", \"gpu_id\": \"cuda:1\"}, {\"server\": \"autodl-5090-c\", \"gpu_id\": \"cuda:2\"}, {\"server\": \"autodl-5090-c\", \"gpu_id\": \"cuda:3\"}], \"actually_running_gpus\": [{\"server\": \"autodl-5090\", \"gpu_id\": \"cuda:0\", \"exp_id\": \"exp_qwen25_32b_fewnerd\"}, {\"server\": \"autodl-5090\", \"gpu_id\": \"cuda:1\", \"exp_id\": \"exp_qwen25_32b_fewnerd\"}, {\"server\": \"autodl-5090\", \"gpu_id\": \"cuda:2\", \"exp_id\": \"exp_qwen25_32b_fewnerd\"}, {\"server\": \"autodl-5090\", \"gpu_id\": \"cuda:3\", \"exp_id\": \"exp_qwen25_32b_fewnerd\"}, {\"server\": \"autodl-5090-c\", \"gpu_id\": \"cuda:2\", \"exp_id\": \"exp_tlow_fewnerd_inference\"}], \"allocated_but_idle\": [{\"server\": \"autodl-5090-b\", \"gpu_id\": \"cuda:0\", \"idle_min\": null, \"util_pct\": null}, {\"server\": \"autodl-5090-b\", \"gpu_id\": \"cuda:1\", \"idle_min\": null, \"util_pct\": null}, {\"server\": \"autodl-5090-b\", \"gpu_id\": \"cuda:2\", \"idle_min\": null, \"util_pct\": null}, {\"server\": \"autodl-5090-b\", \"gpu_id\": \"cuda:3\", \"idle_min\": null, \"util_pct\": null}, {\"server\": \"autodl-5090-c\", \"gpu_id\": \"cuda:0\", \"idle_min\": null, \"util_pct\": null}, {\"server\": \"autodl-5090-c\", \"gpu_id\": \"cuda:1\", \"idle_min\": null, \"util_pct\": null}, {\"server\": \"autodl-5090-c\", \"gpu_id\": \"cuda:3\", \"idle_min\": null, \"util_pct\": null}], \"registered_but_hw_idle\": [], \"unregistered_but_hw_active\": [], \"running_experiments\": [{\"exp_id\": \"exp_qwen25_32b_fewnerd\", \"gpus\": [\"cuda:0\", \"cuda:1\", \"cuda:2\", \"cuda:3\"], \"util_avg\": null}, {\"exp_id\": \"exp_tlow_fewnerd_inference\", \"gpus\": [\"cuda:2\"], \"util_avg\": null}], \"worker_pool\": {\"total\": 1, \"gpu_tasks\": 0, \"cpu_tasks\": 1, \"details\": [{\"worker_id\": \"worker_diagnose_exp_b1_scd_fewnerd_curriculum_q_20260520T190612\", \"task\": \"diagnose:exp_b1_scd_fewnerd_curriculum_q\"}]}, \"summary\": \"分配 12 张, 实际跑 5 张 ⚠️ | Worker 1 (GPU 0 / CPU 1)\"}, \"error\": null, \"metadata\": {}}"
    }
  },
  "sourceToolAssistantUUID": "fc6abdfb-c588-4c26-8b46-428d1b26c0b8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/agent_5c567c58",
  "sessionId": "bb8bc777-37fb-4956-b48e-5e9c5a98dd73",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 87 · 2026-05-20T19:16:28.910Z_

```json
{
  "parentUuid": "a19dacac-4761-4ae7-9aad-aefbd0685ff0",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "70fd3ed6-55cc-4416-9801-23fb0ec7e1f0",
  "timestamp": "2026-05-20T19:16:28.910Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/agent_5c567c58",
  "sessionId": "bb8bc777-37fb-4956-b48e-5e9c5a98dd73",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 88 · 2026-05-20T19:16:46.086Z_

<details><summary>Logged reasoning block</summary>

```text
Registry updated. Now I need to:
1. Report to Director about the false positive and that the training completed
2. Note that the SCD standard training needs eval inference to determine greedy F1
3. Highlight the idle GPUs (7 idle out of 12 allocated!)

Resource status:
- Allocated: 12 GPUs
- Running: 5 (autodl-5090 ×4 for 32B, autodl-5090-c ×1 for tlow inference)
- Idle: 7 (autodl-5090-b ×4, autodl-5090-c ×3)


- Workers: 1 (CPU, diagnosing curriculum_q)

There's a discrepancy though—the cron logs show several experiments still running that aren't showing up in the resource usage tool: the SCD threshold ablation on autodl-5090-b, the FewNERD inference on autodl-5090-c, and the theta adaptive experiment on local-cpu. I need to reconcile what the cron records are actually reporting versus what the resource monitor is seeing.

Looking at the actual GPU allocations, only two experiments are showing up as active: the Qwen 32B FewNERD using 4 GPUs and the low-threshold FewNERD inference using 1 GPU. The threshold ablation and 14B inference experiments aren't registering their GPU usage, which suggests their allocations might not be properly tracked.

For now, I need to focus on the immediate priorities: reporting the false positive to the Director, getting the SCD standard model evaluated since training is complete, and checking the status of the GPU on autodl-5090-b:0 where that experiment ran.

The GPU on autodl-5090-b:0 is now free, so I can proceed with the report. Looking more closely at the status, there's a discrepancy — the threshold ablation and 14B inference show as running, but all GPUs on 5090-b are idle, which suggests these might be CPU-only tasks or the GPU tracking is out of sync. I'll focus the Director report on the false positive for the SCD standard model, the need to run eval inference to validate the hypothesis, and flag the resource status with those idle GPUs.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "70fd3ed6-55cc-4416-9801-23fb0ec7e1f0",
  "isSidechain": false,
  "requestId": "req_011CbEMgPVJhN2Q6GXy6SGbY",
  "type": "assistant",
  "uuid": "2b48101e-369c-428f-b7d2-bd4da7e7766d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/agent_5c567c58",
  "sessionId": "bb8bc777-37fb-4956-b48e-5e9c5a98dd73",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011pGQEKyEooVA5Rs5B1mjta",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6567,
      "cache_read_input_tokens": 67497,
      "output_tokens": 1297,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6567,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1297,
          "cache_read_input_tokens": 67497,
          "cache_creation_input_tokens": 6567,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6567
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

_source line 89 · 2026-05-20T19:16:46.091Z_

Registry 更新完成。现在向 Director 汇报这个 cron false positive，同时需要启动 eval inference 来验证 SCD 效果。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2b48101e-369c-428f-b7d2-bd4da7e7766d",
  "isSidechain": false,
  "requestId": "req_011CbEMgPVJhN2Q6GXy6SGbY",
  "type": "assistant",
  "uuid": "a3c92b71-b303-414f-b639-26da2e72af68",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/agent_5c567c58",
  "sessionId": "bb8bc777-37fb-4956-b48e-5e9c5a98dd73",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011pGQEKyEooVA5Rs5B1mjta",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6567,
      "cache_read_input_tokens": 67497,
      "output_tokens": 1297,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6567,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1297,
          "cache_read_input_tokens": 67497,
          "cache_creation_input_tokens": 6567,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6567
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

_source line 90 · 2026-05-20T19:16:55.716Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__main_agent_post_to_director · `toolu_012WMSeVb1XHsTm22ZAAq74C`</summary>

```json
{
  "project": "struct_self_consist_ie",
  "text": "[资源] GPU 5/12 运行中 | Worker 1 (GPU 0 / CPU 1) | autodl-5090-b 全 4 卡空闲, autodl-5090-c 3 卡空闲\n\n**exp_b1_scd_fewnerd_standard: Cron 误判 — 训练实际已完成**\n\n与 exp_b1_scd_fewnerd_curriculum_q 相同的已知模式：LLaMA-Factory 训练未配置 W&B report_to，cron 依赖 W&B sentinel 判断完成状态，进程正常退出后被误判为 failed。\n\n训练指标（已验证）:\n- 4706/4706 steps, epoch=2.0\n- train_loss=0.023, eval_loss=0.0329\n- 运行时间 7h08m\n- Checkpoint: `/root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen3-8b-fewnerd-scd-lora/`\n\nRegistry 已更新：failure_reason 标记 RETRACTED，metrics 和 checkpoint_path 已记录。\n\n**下一步**: 需要 eval inference（greedy F1 on FewNERD）来验证 hypothesis（目标: greedy F1 接近 N=8 construction F1 0.764 vs 当前 0.748）。autodl-5090-b:0 已空闲，可立即启动。请批准 eval。\n\n⚠️ **系统性问题**: B1 SCD 三个实验均因同一 bug 被误判。建议后续 LLaMA-Factory 训练配置统一加 `report_to: wandb`，或让 cron 增加 checkpoint/trainer_state.json 备用检测。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a3c92b71-b303-414f-b639-26da2e72af68",
  "isSidechain": false,
  "requestId": "req_011CbEMgPVJhN2Q6GXy6SGbY",
  "type": "assistant",
  "uuid": "be9798ce-c807-4746-976f-2191552b4d70",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/agent_5c567c58",
  "sessionId": "bb8bc777-37fb-4956-b48e-5e9c5a98dd73",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011pGQEKyEooVA5Rs5B1mjta",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6567,
      "cache_read_input_tokens": 67497,
      "output_tokens": 1297,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6567,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1297,
          "cache_read_input_tokens": 67497,
          "cache_creation_input_tokens": 6567,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6567
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

_source line 91 · 2026-05-20T19:16:59.487Z_

<details><summary>↩ Tool result · `toolu_012WMSeVb1XHsTm22ZAAq74C`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"director_session\": \"feishu:group:oc_1b56445332d8ca2b4964b30f300f0e00:director\"}, \"error\": \"\"}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "be9798ce-c807-4746-976f-2191552b4d70",
  "isSidechain": false,
  "promptId": "d2210c4d-d5b9-450f-8450-2f1ffe6e0ccd",
  "type": "user",
  "uuid": "d355304b-373c-46cc-b195-361ebe46de06",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"director_session\\\": \\\"feishu:group:oc_1b56445332d8ca2b4964b30f300f0e00:director\\\"}, \\\"error\\\": \\\"\\\"}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"director_session\": \"feishu:group:oc_1b56445332d8ca2b4964b30f300f0e00:director\"}, \"error\": \"\"}"
    }
  },
  "sourceToolAssistantUUID": "be9798ce-c807-4746-976f-2191552b4d70",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/agent_5c567c58",
  "sessionId": "bb8bc777-37fb-4956-b48e-5e9c5a98dd73",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---
