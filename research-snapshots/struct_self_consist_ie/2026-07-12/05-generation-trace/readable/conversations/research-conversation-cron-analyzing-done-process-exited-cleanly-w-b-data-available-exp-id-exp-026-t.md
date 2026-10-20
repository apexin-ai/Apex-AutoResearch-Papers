# Research conversation: [CRON] 实验进程已正常退出，状态已转为 ANALYZING，需要你分析结果并推进到 DONE。 详情: Process exited cleanly, W&B data available - exp_id: exp_026_T05 

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 51
- **Recorded user turns:** 1
- **Tool calls:** 13
- **Original source:** `logs/chats/exported-trajectories/account-3/4bea65e8-6043-4140-a3a7-6b0afa4c330b.jsonl`
- **Structured JSON:** [`8c889f0ec392dffa78d8.json`](../../sessions/8c/8c889f0ec392dffa78d8.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-17T09:47:39.017Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-17T09:47:39.017Z",
  "sessionId": "4bea65e8-6043-4140-a3a7-6b0afa4c330b",
  "content": "[CRON] 实验进程已正常退出，状态已转为 ANALYZING，需要你分析结果并推进到 DONE。\n详情: Process exited cleanly, W&B data available\n\n- exp_id: exp_026_T05\n- project: struct_self_consist_ie\n- server: autodl-5090\n- log_path: ~/runs/struct_self_consist_ie/exp_026_T05.log"
}
```

---

### Runtime record

_source line 2 · 2026-05-17T09:47:39.020Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-17T09:47:39.020Z",
  "sessionId": "4bea65e8-6043-4140-a3a7-6b0afa4c330b"
}
```

---

## Round 1

49 recorded events

### User

_source line 3 · 2026-05-17T09:47:39.057Z_

[CRON] 实验进程已正常退出，状态已转为 ANALYZING，需要你分析结果并推进到 DONE。
详情: Process exited cleanly, W&B data available

- exp_id: exp_026_T05
- project: struct_self_consist_ie
- server: autodl-5090
- log_path: ~/runs/struct_self_consist_ie/exp_026_T05.log

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "5c07e4b0-2988-437a-a5d7-f32039fe1b2e",
  "type": "user",
  "uuid": "fe296150-fd27-431c-a9be-0288e45dbaec",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/agent_b15d88fb",
  "sessionId": "4bea65e8-6043-4140-a3a7-6b0afa4c330b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-17T09:47:39.056Z_

```json
{
  "parentUuid": "fe296150-fd27-431c-a9be-0288e45dbaec",
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
  "uuid": "549c331e-f43e-4a8d-884c-d549abb1bb3c",
  "timestamp": "2026-05-17T09:47:39.056Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/agent_b15d88fb",
  "sessionId": "4bea65e8-6043-4140-a3a7-6b0afa4c330b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-17T09:47:39.056Z_

```json
{
  "parentUuid": "549c331e-f43e-4a8d-884c-d549abb1bb3c",
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
  "uuid": "da6f697d-a0a1-4179-901a-84727e61f848",
  "timestamp": "2026-05-17T09:47:39.056Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/agent_b15d88fb",
  "sessionId": "4bea65e8-6043-4140-a3a7-6b0afa4c330b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6 · 2026-05-17T09:47:39.056Z_

```json
{
  "parentUuid": "da6f697d-a0a1-4179-901a-84727e61f848",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "4997d6a6-07b9-4e32-8cf6-4a5d0ff49ada",
  "timestamp": "2026-05-17T09:47:39.056Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/agent_b15d88fb",
  "sessionId": "4bea65e8-6043-4140-a3a7-6b0afa4c330b",
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
  "aiTitle": "Analyze experiment results and mark complete",
  "sessionId": "4bea65e8-6043-4140-a3a7-6b0afa4c330b"
}
```

---

### Assistant

_source line 8 · 2026-05-17T09:47:47.721Z_

<details><summary>Logged reasoning block</summary>

```text
收到 cron 回调：exp_026_T05 已正常退出，状态转为 ANALYZING。我需要：

1. 先执行 session-start 初始化（read_registry, reconcile_crons, 读 report.md 和 ROADMAP.md）
2. 然后处理这个实验完成的回调

让我先加载需要的工具。
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4997d6a6-07b9-4e32-8cf6-4a5d0ff49ada",
  "isSidechain": false,
  "requestId": "req_011Cb7vsnQpcUH7zkHBq8QH7",
  "type": "assistant",
  "uuid": "9280d827-ac87-4d13-a184-e604cc1a6eac",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/agent_b15d88fb",
  "sessionId": "4bea65e8-6043-4140-a3a7-6b0afa4c330b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012dXspZvukLQ29FyXJB8KkD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 25641,
      "cache_read_input_tokens": 11841,
      "output_tokens": 279,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 25641,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 279,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 25641,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 25641
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

_source line 9 · 2026-05-17T09:47:47.873Z_

收到 exp_026_T05 完成回调，开始 session 初始化和结果分析。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9280d827-ac87-4d13-a184-e604cc1a6eac",
  "isSidechain": false,
  "requestId": "req_011Cb7vsnQpcUH7zkHBq8QH7",
  "type": "assistant",
  "uuid": "1edb318d-9b52-4cac-993d-9a55aa65b8ae",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/agent_b15d88fb",
  "sessionId": "4bea65e8-6043-4140-a3a7-6b0afa4c330b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012dXspZvukLQ29FyXJB8KkD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 25641,
      "cache_read_input_tokens": 11841,
      "output_tokens": 279,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 25641,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 279,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 25641,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 25641
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

_source line 10 · 2026-05-17T09:47:49.163Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01FLzg8x47JmERucmag6Wsqn`</summary>

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
  "parentUuid": "1edb318d-9b52-4cac-993d-9a55aa65b8ae",
  "isSidechain": false,
  "requestId": "req_011Cb7vsnQpcUH7zkHBq8QH7",
  "type": "assistant",
  "uuid": "b4e000b0-9f4b-4257-97cd-a202f8cc5f54",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/agent_b15d88fb",
  "sessionId": "4bea65e8-6043-4140-a3a7-6b0afa4c330b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012dXspZvukLQ29FyXJB8KkD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 25641,
      "cache_read_input_tokens": 11841,
      "output_tokens": 279,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 25641,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 279,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 25641,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 25641
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

_source line 11 · 2026-05-17T09:47:49.170Z_

<details><summary>↩ Tool result · `toolu_01FLzg8x47JmERucmag6Wsqn`</summary>

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
  "parentUuid": "b4e000b0-9f4b-4257-97cd-a202f8cc5f54",
  "isSidechain": false,
  "promptId": "5c07e4b0-2988-437a-a5d7-f32039fe1b2e",
  "type": "user",
  "uuid": "ad0dbab7-c6d6-41ed-b696-03d2676eef01",
  "toolUseResult": {
    "matches": [
      "mcp__agent-ml-research__read_registry",
      "mcp__agent-ml-research__reconcile_crons",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__read_roadmap"
    ],
    "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__reconcile_crons,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__read_roadmap",
    "total_deferred_tools": 80
  },
  "sourceToolAssistantUUID": "b4e000b0-9f4b-4257-97cd-a202f8cc5f54",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/agent_b15d88fb",
  "sessionId": "4bea65e8-6043-4140-a3a7-6b0afa4c330b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 12 · 2026-05-17T09:47:53.592Z_

<details><summary>Logged reasoning block</summary>

```text
Let me start the session initialization by reading the registry, reconciling crons, and reading report.md and ROADMAP.md in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ad0dbab7-c6d6-41ed-b696-03d2676eef01",
  "isSidechain": false,
  "requestId": "req_011Cb7vtXasbeqztrUd6ujFg",
  "type": "assistant",
  "uuid": "411a5d99-46f4-41ff-bf3f-7336f193b263",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/agent_b15d88fb",
  "sessionId": "4bea65e8-6043-4140-a3a7-6b0afa4c330b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HZaurt2CPwsWFTfyVUgqed",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1157,
      "cache_read_input_tokens": 37482,
      "output_tokens": 284,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1157,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 284,
          "cache_read_input_tokens": 37482,
          "cache_creation_input_tokens": 1157,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1157
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

_source line 13 · 2026-05-17T09:47:54.059Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01JgXuiFgbAFPy75Zcm6qT3Z`</summary>

```json
{
  "project": "struct_self_consist_ie",
  "limit": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "411a5d99-46f4-41ff-bf3f-7336f193b263",
  "isSidechain": false,
  "requestId": "req_011Cb7vtXasbeqztrUd6ujFg",
  "type": "assistant",
  "uuid": "8e727672-ce72-4a09-962c-7747b10fec53",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/agent_b15d88fb",
  "sessionId": "4bea65e8-6043-4140-a3a7-6b0afa4c330b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HZaurt2CPwsWFTfyVUgqed",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1157,
      "cache_read_input_tokens": 37482,
      "output_tokens": 284,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1157,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 284,
          "cache_read_input_tokens": 37482,
          "cache_creation_input_tokens": 1157,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1157
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

_source line 14 · 2026-05-17T09:47:54.533Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__reconcile_crons · `toolu_017AEidKuitcLqnjg7z29ty4`</summary>

```json
{}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8e727672-ce72-4a09-962c-7747b10fec53",
  "isSidechain": false,
  "requestId": "req_011Cb7vtXasbeqztrUd6ujFg",
  "type": "assistant",
  "uuid": "4f395dcc-631e-44ff-8816-0a4616c16fe8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/agent_b15d88fb",
  "sessionId": "4bea65e8-6043-4140-a3a7-6b0afa4c330b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HZaurt2CPwsWFTfyVUgqed",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1157,
      "cache_read_input_tokens": 37482,
      "output_tokens": 284,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1157,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 284,
          "cache_read_input_tokens": 37482,
          "cache_creation_input_tokens": 1157,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1157
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

_source line 15 · 2026-05-17T09:47:54.712Z_

<details><summary>↩ Tool result · `toolu_01JgXuiFgbAFPy75Zcm6qT3Z`</summary>

```text
Error: result (99,878 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-agent-b15d88fb/4bea65e8-6043-4140-a3a7-6b0afa4c330b/tool-results/mcp-agent-ml-research-read_registry-1779011274694.txt.
Format: JSON with schema: {result: string}
- For targeted queries (find a value, filter by field): use jq on the file directly.
- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-agent-b15d88fb/4bea65e8-6043-4140-a3a7-6b0afa4c330b/tool-results/mcp-agent-ml-research-read_registry-1779011274694.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.
- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-agent-b15d88fb/4bea65e8-6043-4140-a3a7-6b0afa4c330b/tool-results/mcp-agent-ml-research-read_registry-1779011274694.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim." A vague "summarize this" may lose detail.

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8e727672-ce72-4a09-962c-7747b10fec53",
  "isSidechain": false,
  "promptId": "5c07e4b0-2988-437a-a5d7-f32039fe1b2e",
  "type": "user",
  "uuid": "f50164e7-2c2e-4001-8179-bea7acf0ef3e",
  "toolUseResult": "Error: result (99,878 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-agent-b15d88fb/4bea65e8-6043-4140-a3a7-6b0afa4c330b/tool-results/mcp-agent-ml-research-read_registry-1779011274694.txt.\nFormat: JSON with schema: {result: string}\n- For targeted queries (find a value, filter by field): use jq on the file directly.\n- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-agent-b15d88fb/4bea65e8-6043-4140-a3a7-6b0afa4c330b/tool-results/mcp-agent-ml-research-read_registry-1779011274694.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.\n- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. \"/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-agent-b15d88fb/4bea65e8-6043-4140-a3a7-6b0afa4c330b/tool-results/mcp-agent-ml-research-read_registry-1779011274694.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim.\" A vague \"summarize this\" may lose detail.\n",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {\"exp_026_T05\": {\"status\": \"ANALYZING\", \"created_at\": \"2026-05-17T09:38:28.066Z\", \"updated_at\": \"2026-05-17T09:47:31.995Z\", \"hypothesis\": \"T=0.5 will increase degeneracy rate (more deterministic outputs) and compress LP range on SciERC, reducing selection headroom. Maps the low-temperature end of the degeneracy-temperature frontier, validating that degeneracy is regime-dependent on sampling temperature.\"}, \"exp_026_T12\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-17T09:38:31.060Z\", \"updated_at\": \"2026-05-17T09:41:40.636Z\", \"hypothesis\": \"T=1.2 will decrease degeneracy rate and expand LP range vs T=1.0, but may degrade generation quality (lower greedy F1). Tests whether reducing degeneracy via higher T recovers selection headroom or if quality degradation offsets the benefit.\"}, \"exp_026_T08\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-17T09:38:29.602Z\", \"updated_at\": \"2026-05-17T09:41:22.075Z\", \"hypothesis\": \"T=0.8 will show intermediate degeneracy between T=0.5 and T=1.0, establishing a monotonic degeneracy-temperature relationship. If LP selection improves at T=0.8 vs T=1.0, it identifies the optimal operating point for the selection mechanism.\"}, \"exp_028_fewnerd_5epoch\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-17T07:53:12.913Z\", \"updated_at\": \"2026-05-17T09:12:09.873Z\", \"conclusion\": \"killed\"}, \"exp_028\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-17T07:35:39.447Z\", \"updated_at\": \"2026-05-17T07:35:59.979Z\", \"hypothesis\": \"Few-NERD low degeneracy (10%) in exp-021 is NOT due to under-convergence at 3 epochs; training for 5 epochs will show similar degeneracy levels, confirming the structural property of this dataset rather than an artifact of insufficient training.\"}, \"exp_027_fewnerd_n16\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T05:28:57.036Z\", \"updated_at\": \"2026-05-17T05:46:48.460Z\", \"conclusion\": \"success\", \"metrics\": {\"LP_delta_pp\": 1.88, \"LP_delta_95CI\": [1.41, 2.37], \"degeneracy_rate\": 0.045, \"greedy_f1\": 0.7478, \"lp_sel_f1\": 0.7666, \"oracle_f1\": 0.902, \"headroom_pp\": 15.42, \"all_8_types_positive\": true, \"n_instances\": 5000, \"N_samples\": 16, \"bootstrap_p\": \"<0.001\"}, \"hypothesis\": \"LP selection scales with N in low-degeneracy regime: N=16 should yield LP Δ > +2pp (vs N=8 +1.36pp) on Few-NERD (10% degen), because more samples increase oracle headroom while LP ranking remains effective.\"}, \"exp_016_rerun_1024_bootstrap\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T23:44:21.577Z\", \"updated_at\": \"2026-05-17T03:33:39.786Z\", \"hypothesis\": \"3-seed bootstrap significance test for NER logprob vs greedy selection gap (+0.6pp). Tests whether the observed advantage is statistically significant.\", \"conclusion\": \"negative\", \"metrics\": {\"bootstrap_ci_95\": [-0.03, 0.042], \"permutation_p\": 0.39, \"cohen_d\": 0.038, \"sign_test_win_rate\": 0.466, \"ner_logprob_vs_greedy_delta\": 0.006, \"conclusion_summary\": \"NER selection: no signal significantly outperforms greedy; RE: same conclusion\"}, \"parent\": \"exp_016_rerun_1024\"}, \"exp_verbalized_confidence\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T02:45:20.552Z\", \"updated_at\": \"2026-05-17T03:33:39.197Z\", \"hypothesis\": \"Verbalized confidence baseline: let model self-rate extraction confidence. If also compressed → strengthens \\\"score compression is general\\\" claim. If effective → important positive finding requiring narrative adjustment.\", \"conclusion\": \"negative\", \"metrics\": {\"scierc\": {\"VerbConf_rho\": 0.2965, \"VerbConf_auroc\": 0.6811, \"VerbConf_sel_f1\": 0.6195, \"VerbConf_delta\": -0.0245, \"best_existing_rho\": 0.3792, \"VerbConf_mean\": 8.58, \"VerbConf_std\": 1.15, \"parse_fail_rate\": 0.0026}, \"conll\": {\"VerbConf_rho\": 0.3366, \"VerbConf_auroc\": 0.7469, \"VerbConf_sel_f1\": 0.8886, \"VerbConf_delta\": -0.0193, \"best_existing_rho\": 0.4507, \"VerbConf_mean\": 9.24, \"VerbConf_std\": 1.32, \"parse_fail_rate\": 0}}, \"parent\": \"exp_012_rerun_1024\"}, \"exp_entity_token_lp\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T05:39:44.631Z\", \"updated_at\": \"2026-05-17T03:33:38.371Z\", \"hypothesis\": \"Entity-token LP: test Discussion hypothesis (d) format-token dilution. Re-inference with per-token logprobs, then compute entity-only LP variance and selection F1. If entity-token LP compression is reduced → pilot remedy for LP selection. Also includes LP z-score normalization as zero-cost baseline. Addresses SF2+SF3 from Round 12.\", \"conclusion\": \"negative\", \"metrics\": {\"scierc_ner\": {\"greedy_f1\": 0.643, \"full_lp_sel_f1\": 0.6465, \"entity_lp_sel_f1\": 0.6262, \"oracle_f1\": 0.7845, \"entity_lp_delta_vs_full_lp\": -0.0203}, \"conll_ner\": {\"greedy_f1\": 0.9065, \"full_lp_sel_f1\": 0.8989, \"entity_lp_sel_f1\": 0.8659, \"oracle_f1\": 0.948, \"entity_lp_delta_vs_full_lp\": -0.033}, \"finding\": \"entity-token LP strictly worse than full-sequence LP; CoNLL entity tokens saturated (79.4% tied), SciERC entity tokens too sparse (5.3% of total)\"}, \"parent\": \"exp_012_rerun_1024\"}, \"exp_freeform_ablation\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T09:42:22.868Z\", \"updated_at\": \"2026-05-17T03:33:37.623Z\", \"conclusion\": \"negative\", \"metrics\": {\"lp_std_ratio_free_vs_constrained\": 0.97, \"lp_range_ratio\": 0.96, \"tied_fraction_constrained\": 0.597, \"tied_fraction_freeform\": 0.577, \"ner_selection_gap_constrained\": 0.0059, \"ner_selection_gap_freeform\": 0.0018, \"re_selection_gap_constrained\": -0.0068, \"re_selection_gap_freeform\": 0.0169, \"parse_rate\": 0.9995, \"ner_vc_rho_constrained\": 0.3792, \"ner_vc_rho_freeform\": 0.4089}, \"hypothesis\": \"Free-form vs constrained decoding ablation on SciERC: test if removing JSON schema constraint changes LP variance distribution. If LP remains compressed under free-form, confirms compression is model-intrinsic not format-artifact.\", \"parent\": \"exp_012_rerun_1024\"}, \"exp_008_re_n16\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T12:03:06.876Z\", \"updated_at\": \"2026-05-17T02:58:19.490Z\", \"metrics\": {\"ner\": {\"greedy_f1\": 0.6635, \"oracle_f1\": 0.8208, \"headroom\": 0.1572, \"rho_sj_full\": 0.377, \"rho_fk_full\": 0.2508, \"rho_logprob_full\": 0.3153, \"rho_sj_cond\": 0.3598, \"rho_fk_cond\": 0.2251, \"rho_logprob_cond\": 0.2927, \"sj_beats_fk\": true, \"rho_advantage\": 0.1262}, \"re\": {\"greedy_f1\": 0.4339, \"oracle_f1\": 0.6658, \"headroom\": 0.2319, \"rho_sj_full\": 0.2966, \"rho_fk_full\": 0.2871, \"rho_logprob_full\": 0.2986, \"rho_sj_cond\": 0.3975, \"rho_fk_cond\": 0.3774, \"rho_logprob_cond\": 0.2745, \"sj_beats_fk\": true, \"rho_advantage\": 0.0095}, \"verdict\": \"FAIL\"}, \"conclusion\": \"success\", \"hypothesis\": \"RE N=16 initial evaluation: first relation extraction test with structural signals. Establishes baseline RE signal effectiveness before pipeline corrections.\"}, \"exp_001_ner_n16_seed123\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T12:46:06.430Z\", \"updated_at\": \"2026-05-17T02:58:18.225Z\", \"conclusion\": \"success\", \"metrics\": {\"ner\": {\"greedy_f1\": 0.663, \"oracle_f1\": 0.809, \"headroom\": 0.146, \"rho_sj\": 0.423, \"rho_fk\": 0.29, \"rho_logprob\": 0.239, \"rho_sj_cond\": 0.423, \"rho_fk_cond\": 0.26}, \"re\": {\"greedy_f1\": 0.419, \"oracle_f1\": 0.625, \"headroom\": 0.206, \"rho_sj\": 0.267, \"rho_fk\": 0.315, \"rho_sj_cond\": 0.364, \"rho_fk_cond\": 0.331}, \"verdict\": \"FAIL\", \"verdict_note\": \"RE rho_sj=0.267 < 0.40; RE >30% samples F1=0\", \"n_instances\": 551, \"seed\": 123, \"N\": 16, \"T\": 1}, \"hypothesis\": \"SciERC NER N=16 seed=123: multi-seed validation at N=16. Tests seed stability for signal rankings with more samples.\"}, \"exp_007_ner_multi_model\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T11:42:20.748Z\", \"updated_at\": \"2026-05-17T02:58:16.747Z\", \"conclusion\": \"success\", \"metrics\": {\"epoch\": 5, \"train_loss\": 0.0767, \"eval_loss\": 0.1049, \"train_runtime_sec\": 1494.5, \"train_samples_per_second\": 6.226, \"checkpoints\": [\"checkpoint-400\", \"checkpoint-500\", \"checkpoint-585\"], \"base_model\": \"Meta-Llama-3.1-8B-Instruct\", \"lora_r\": 32, \"lora_alpha\": 64, \"note\": \"EXIT_CODE=129 (SIGHUP) but training completed all 5 epochs before signal. Checkpoint fully intact.\"}, \"hypothesis\": \"Multi-model NER comparison: evaluates signal effectiveness across Qwen and LLaMA on SciERC NER. Establishes cross-model generalization of structural>surface ranking.\"}, \"exp_003_ner_wnut17\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T11:42:17.544Z\", \"updated_at\": \"2026-05-17T02:58:14.928Z\", \"metrics\": {\"ner\": {\"greedy_f1\": 0.525, \"oracle_f1\": 0.664, \"headroom\": 0.139, \"rho_sj_full\": 0.082, \"rho_fk_full\": 0.124, \"rho_logprob_full\": -0.414, \"rho_sj_cond\": 0.275, \"rho_fk_cond\": 0.164, \"rho_logprob_cond\": 0.352, \"sj_beats_logprob_cond\": false}, \"n_instances\": 1287, \"n_gold_empty\": 598, \"sample_f1_mean\": 0.401, \"sample_f1_pct_zero\": 53.7, \"N\": 16, \"T\": 1, \"seed\": 42, \"verdict\": \"FAIL\", \"verdict_note\": \">30% samples F1=0; structural rho weak; logprob baseline stronger\"}, \"conclusion\": \"negative\", \"hypothesis\": \"WNUT-17 NER fine-tune + inference: initial attempt on social media domain. Tests if structural signals work when model capability is low on noisy text with novel entity types.\"}, \"exp_001_seed456_t10_full\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T13:27:41.067Z\", \"updated_at\": \"2026-05-17T02:58:12.996Z\", \"conclusion\": \"negative\", \"metrics\": {\"ner\": {\"rho_sj\": 0.414, \"rho_fk\": 0.298}, \"re\": {\"rho_sj\": 0.268, \"rho_fk\": 0.26}, \"n_instances\": 551, \"N\": 16, \"T\": 1, \"seed\": 456, \"source\": \"reviewer_verified_report_json\"}, \"hypothesis\": \"SciERC NER seed=456 T=1.0 full: early multi-seed NER test before pipeline corrections. Preliminary evidence for seed stability.\"}, \"exp_001_seed123_t10_full\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T13:27:42.503Z\", \"updated_at\": \"2026-05-17T02:58:11.623Z\", \"conclusion\": \"negative\", \"metrics\": {\"ner\": {\"rho_sj\": 0.417, \"rho_fk\": 0.283}, \"re\": {\"rho_sj\": 0.265, \"rho_fk\": 0.315}, \"n_instances\": 551, \"N\": 16, \"T\": 1, \"seed\": 123, \"source\": \"reviewer_verified_report_json\"}, \"hypothesis\": \"SciERC NER seed=123 T=1.0 full: early multi-seed NER test before pipeline corrections. Preliminary evidence for seed stability.\"}, \"exp_008_re_n16_t10_full\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T13:27:42.867Z\", \"updated_at\": \"2026-05-17T02:58:10.171Z\", \"conclusion\": \"negative\", \"metrics\": {\"ner\": {\"rho_sj\": 0.444}, \"re\": {\"rho_sj\": 0.248}, \"n_instances\": 551, \"N\": 16, \"T\": 1, \"seed\": 42, \"mode\": \"RE-only\", \"source\": \"director_corrected\"}, \"hypothesis\": \"RE N=16 T=1.0 full dataset: early RE evaluation attempt. Tests structural signals on relation extraction before pipeline corrections.\"}, \"exp_007_llama_inference\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T13:54:48.055Z\", \"updated_at\": \"2026-05-17T02:58:03.014Z\", \"metrics\": {\"ner\": {\"greedy_f1\": 0.66, \"oracle_f1\": 0.781, \"headroom\": 0.121, \"rho_fk\": 0.327, \"rho_sj\": 0.363, \"rho_fk_cond\": 0.226, \"rho_sj_cond\": 0.311, \"rho_logprob\": 0.183, \"rho_logprob_cond\": 0.109, \"structural_beats_surface\": true, \"sample_f1_pct_zero\": 11.6}, \"re\": {\"greedy_f1\": 0.434, \"oracle_f1\": 0.568, \"headroom\": 0.135, \"rho_fk\": 0.305, \"rho_sj\": 0.299, \"rho_fk_cond\": 0.259, \"rho_sj_cond\": 0.405, \"rho_logprob\": 0.288, \"rho_logprob_cond\": 0.092, \"structural_beats_surface\": false, \"sample_f1_pct_zero\": 41.2}, \"n_instances\": 551, \"N\": 8, \"T\": 1, \"seed\": 42, \"model\": \"LLaMA-3.1-8B-Instruct\", \"verdict\": \"FAIL\", \"verdict_note\": \"RE rho_sj_full=0.299 < 0.40; >30% RE samples F1=0\"}, \"conclusion\": \"success\", \"hypothesis\": \"LLaMA SciERC N=8 baseline: first cross-model test. Verifies structural signal effectiveness generalizes from Qwen to LLaMA model family on SciERC NER.\"}, \"exp_003_wnut17_eval\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T13:47:34.654Z\", \"updated_at\": \"2026-05-17T02:58:01.627Z\", \"conclusion\": \"success\", \"metrics\": {\"greedy_f1\": 0.523, \"oracle_f1\": 0.664, \"headroom\": 0.141, \"rho_fk\": 0.125, \"rho_sj\": 0.089, \"rho_fk_cond\": 0.169, \"rho_sj_cond\": 0.288, \"rho_logprob_full\": -0.409, \"rho_logprob_cond\": 0.35, \"structural_beats_surface\": false, \"sample_f1_pct_zero\": 53.7, \"n_instances\": 1287, \"N\": 16, \"T\": 1, \"seed\": 42, \"model\": \"Qwen3-8B\", \"n_gold_empty_filtered\": 598, \"verdict\": \"FAIL\", \"verdict_note\": \"structural_beats_surface=false; >50% samples F1=0\"}, \"hypothesis\": \"WNUT-17 NER evaluation: initial test on noisy social media domain. Tests boundary conditions for structural signal effectiveness on out-of-domain text.\"}, \"exp_010_selection_curves\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T15:01:53.585Z\", \"updated_at\": \"2026-05-17T02:58:00.378Z\", \"conclusion\": \"success\", \"metrics\": {\"scierc_ner\": {\"n_instances\": 551, \"greedy_f1\": 0.618, \"N16\": {\"oracle\": 0.787, \"SJ\": 0.62, \"FK\": 0.621, \"logprob\": 0.621, \"voting_conf\": 0.585, \"EM\": 0.606, \"random\": 0.595}, \"N8\": {\"oracle\": 0.752, \"SJ\": 0.614, \"FK\": 0.614, \"logprob\": 0.619, \"voting_conf\": 0.591, \"EM\": 0.603, \"random\": 0.589}, \"N4\": {\"oracle\": 0.714, \"SJ\": 0.607, \"FK\": 0.608, \"logprob\": 0.616, \"voting_conf\": 0.594, \"EM\": 0.6, \"random\": 0.587}}, \"scierc_re\": {\"n_instances\": 397, \"greedy_f1\": 0.403, \"N16\": {\"oracle\": 0.631, \"SJ\": 0.397, \"FK\": 0.396, \"logprob\": 0.41, \"voting_conf\": 0.408, \"EM\": 0.381, \"random\": 0.364}, \"N8\": {\"oracle\": 0.583, \"SJ\": 0.393, \"FK\": 0.394, \"logprob\": 0.413, \"voting_conf\": 0.398, \"EM\": 0.381, \"random\": 0.363}}, \"conll_ner\": {\"n_instances\": 3453, \"greedy_f1\": 0.725, \"N8\": {\"oracle\": 0.757, \"SJ\": 0.718, \"FK\": 0.717, \"logprob\": 0.716, \"voting_conf\": 0.714, \"EM\": 0.716, \"random\": 0.69}, \"N4\": {\"oracle\": 0.746, \"SJ\": 0.714, \"FK\": 0.714, \"logprob\": 0.715, \"voting_conf\": 0.714, \"EM\": 0.712, \"random\": 0.692}}}, \"hypothesis\": \"Selection curve analysis: plots selection F1 vs confidence threshold for each signal. Visualizes where correlation-selection gap emerges and at what confidence level signals become useful for filtering.\"}, \"exp_007_llama_seed456\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T15:08:50.628Z\", \"updated_at\": \"2026-05-17T02:57:59.595Z\", \"conclusion\": \"negative\", \"metrics\": {\"verdict\": \"FAIL\", \"ner\": {\"greedy_f1\": 0.6597, \"oracle_f1\": 0.7575, \"oracle_headroom\": 0.0978, \"fleiss_kappa\": 0.4543, \"soft_jaccard\": 0.7491, \"rho_kappa_f1\": 0.3115, \"rho_sj_f1\": 0.3663, \"structural_gt_surface\": true}, \"re\": {\"greedy_f1\": 0.4334, \"oracle_f1\": 0.5789, \"oracle_headroom\": 0.1455, \"fleiss_kappa\": 0.3791, \"soft_jaccard\": 0.6782, \"rho_kappa_f1\": 0.3013, \"rho_sj_f1\": 0.287, \"structural_gt_surface\": false}, \"logprob_ner\": {\"rho\": 0.1911, \"auroc\": 0.5989}, \"logprob_re\": {\"rho\": 0.3246, \"auroc\": 0.6678}, \"fail_reason\": \"RE rho_sj=0.2870 < 0.40 threshold; >30% samples F1=0\"}, \"hypothesis\": \"LLaMA SciERC seed=456: early cross-model multi-seed test. Verifies LLaMA NER signal pattern is reproducible across sampling seeds.\"}, \"exp_007_llama_seed123\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T15:08:50.157Z\", \"updated_at\": \"2026-05-17T02:57:58.879Z\", \"conclusion\": \"negative\", \"metrics\": {\"verdict\": \"FAIL\", \"ner\": {\"greedy_f1\": 0.6605, \"oracle_f1\": 0.7703, \"headroom\": 0.1098, \"fleiss_kappa\": 0.4553, \"soft_jaccard\": 0.7525, \"rho_kappa_f1\": 0.2143, \"rho_sj_f1\": 0.3371, \"structural_gt_surface\": true}, \"re\": {\"greedy_f1\": 0.433, \"oracle_f1\": 0.5719, \"headroom\": 0.1389, \"fleiss_kappa\": 0.3851, \"soft_jaccard\": 0.6911, \"rho_kappa_f1\": 0.2844, \"rho_sj_f1\": 0.268, \"structural_gt_surface\": false}, \"fail_reasons\": [\"RE rho_sj=0.2680 < 0.40 threshold\", \">30% samples F1=0 (RE: 41.0%)\", \"RE structural not > surface (delta=-0.0165)\"]}, \"hypothesis\": \"LLaMA SciERC seed=123: early cross-model multi-seed test. Verifies LLaMA NER signal pattern is reproducible across sampling seeds.\"}, \"exp_008_re_seed123\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T15:08:51.386Z\", \"updated_at\": \"2026-05-17T02:57:58.166Z\", \"conclusion\": \"negative\", \"metrics\": {\"greedy_f1\": 0.4229, \"oracle_f1\": 0.6244, \"oracle_headroom\": 0.2015, \"fleiss_kappa_mean\": 0.3455, \"soft_jaccard_mean\": 0.6126, \"sample_f1_mean\": 0.3594, \"sample_f1_std\": 0.3793, \"sample_f1_zero_pct\": 44.1, \"structural_gt_surface\": false, \"rho_kappa_f1_full\": 0.3174, \"rho_sj_f1_full\": 0.2835, \"rho_kappa_f1_cond\": 0.0766, \"rho_sj_f1_cond\": 0.2877, \"logprob_auroc_full\": 0.6499, \"logprob_auroc_cond\": 0.5265, \"verdict\": \"FAIL\"}, \"hypothesis\": \"RE seed=123 multi-seed: tests reproducibility of RE signal rankings. Hypothesis: RE signals weaker than NER due to higher zero-F1 rate, but ranking should be seed-stable.\"}, \"exp_001_seed42_v2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T14:34:02.350Z\", \"updated_at\": \"2026-05-17T02:57:57.324Z\", \"conclusion\": \"success\", \"metrics\": {\"sj_rho_full\": 0.428, \"sj_rho_cond\": 0.369, \"structural_minus_surface\": 0.147, \"conclusion_note\": \"NER seed42 robustness confirmed, structural>surface +0.147\"}, \"hypothesis\": \"SciERC NER seed=42 v2: primary seed baseline under corrected pipeline. Establishes canonical signal rankings (SJ>FK>LP) for NER with gold-filtering.\"}, \"exp_001_seed123_v2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T14:34:04.210Z\", \"updated_at\": \"2026-05-17T02:57:42.106Z\", \"conclusion\": \"success\", \"metrics\": {\"sj_rho_full\": 0.424, \"sj_rho_cond\": 0.376, \"structural_minus_surface\": 0.149, \"conclusion_note\": \"NER seed123 robustness confirmed, structural>surface +0.149\"}, \"hypothesis\": \"SciERC NER seed=123 v2: second seed for multi-seed validation. Establishes reproducibility of structural>surface signal ranking across random seeds.\"}, \"exp_008_re_n16_v2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T14:34:06.296Z\", \"updated_at\": \"2026-05-17T02:57:41.178Z\", \"conclusion\": \"negative\", \"metrics\": {\"sj_rho_full\": 0.281, \"sj_rho_cond\": 0.308, \"f1_zero_pct\": 44.3, \"conclusion_note\": \"RE N=16 v2 negative: SJ weak, 44.3% F1=0\"}, \"hypothesis\": \"RE N=16 evaluation v2: tests structural signal effectiveness on relation extraction at higher sample count. Hypothesis: SJ/FK benefit from more samples on RE task where zero-F1 rate is high.\"}, \"exp_005_v2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T15:28:14.924Z\", \"updated_at\": \"2026-05-17T02:57:38.756Z\", \"conclusion\": \"success\", \"hypothesis\": \"Selection F1 analysis v2: compute actual selection F1 (pick best sample by each signal) vs greedy and oracle. First evidence of correlation-selection gap under corrected pipeline.\"}, \"exp_006_v2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T15:30:02.348Z\", \"updated_at\": \"2026-05-17T02:57:36.914Z\", \"conclusion\": \"negative\", \"metrics\": {\"NER_SciERC_s42\": {\"greedy\": 0.618, \"oracle\": 0.787, \"SJ\": 0.62, \"logprob\": 0.621, \"FK\": 0.621, \"EM\": 0.606, \"voting_conf\": 0.585, \"random\": 0.586}, \"NER_SciERC_s123\": {\"greedy\": 0.618, \"oracle\": 0.785, \"SJ\": 0.617, \"logprob\": 0.618, \"FK\": 0.621, \"EM\": 0.613, \"voting_conf\": 0.584, \"random\": 0.583}, \"NER_CoNLL\": {\"greedy\": 0.725, \"oracle\": 0.757, \"SJ\": 0.718, \"logprob\": 0.716, \"FK\": 0.717, \"EM\": 0.716, \"voting_conf\": 0.714, \"random\": 0.692}, \"RE_SciERC\": {\"greedy\": 0.403, \"oracle\": 0.631, \"SJ\": 0.397, \"logprob\": 0.41, \"FK\": 0.396, \"EM\": 0.381, \"voting_conf\": 0.408, \"random\": 0.364}}, \"hypothesis\": \"Temperature sensitivity v2: tests signal effectiveness at T=0.5,0.7,1.0,1.2. Hypothesis: structural signals are temperature-robust while LP degrades at extreme temperatures.\"}, \"exp_004_v2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T15:31:40.554Z\", \"updated_at\": \"2026-05-17T02:57:35.012Z\", \"conclusion\": \"success\", \"hypothesis\": \"N-ablation v2 (N=4,8,16,32): tests how sample count affects signal ρ and selection F1. Validates N-scaling curve for structural vs surface signals under corrected pipeline.\"}, \"exp_009_v2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T15:36:47.946Z\", \"updated_at\": \"2026-05-17T02:57:32.655Z\", \"conclusion\": \"success\", \"metrics\": {\"ner_seed42_global\": {\"sj_rho\": 0.431, \"fk_rho\": 0.325, \"logprob_rho\": 0.203, \"voting_conf_rho\": 0.475, \"em_rho\": 0.292}, \"ner_seed123_global\": {\"sj_rho\": 0.422, \"fk_rho\": 0.315, \"logprob_rho\": 0.226, \"voting_conf_rho\": 0.438, \"em_rho\": 0.299}, \"re_seed42_global\": {\"sj_rho\": 0.063, \"fk_rho\": 0.226, \"logprob_rho\": 0.4, \"voting_conf_rho\": 0.22, \"em_rho\": -0.132}, \"ner_seed_stability_max_delta\": 0.037, \"independent_proxies\": [\"sent_len\", \"ent_count\", \"type_diversity\"], \"inverted_u_ner\": \"not confirmed (ρ stable across independent proxies)\", \"inverted_u_re\": \"monotonic increase with complexity, not inverted-U\"}, \"hypothesis\": \"Capability stratification v2: corrected stratification with gold-filtering and extended to NER conditional analysis. Tests which instance subpopulations drive overall signal effectiveness.\"}, \"exp_016_v2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T15:39:07.501Z\", \"updated_at\": \"2026-05-17T02:57:30.726Z\", \"conclusion\": \"success\", \"metrics\": {\"ner_conditional\": {\"n\": 529, \"best_single_signal_rho\": {\"soft_jaccard\": 0.4412}, \"best_combo_rho\": {\"sj+vc_a0.55\": 0.4552}, \"ensemble_auroc\": 0.7141, \"best_single_auroc\": {\"soft_jaccard\": 0.7166}, \"selection_f1\": {\"greedy\": 0.6442, \"logprob_best\": 0.6505, \"ensemble_best\": 0.6475, \"sj_best\": 0.6471, \"oracle\": 0.8442}}, \"re_conditional\": {\"n\": 397, \"best_single_signal_rho\": {\"voting_confidence\": 0.3849}, \"best_combo_rho\": {\"logprob+vc_a0.25\": 0.3936}, \"ensemble_auroc\": 0.6916, \"best_single_auroc\": {\"voting_confidence\": 0.7023}, \"selection_f1\": {\"greedy\": 0.403, \"logprob_best\": 0.4097, \"ensemble_best\": 0.4227, \"oracle\": 0.6306}}, \"re_full\": {\"ensemble_auroc\": 0.8608, \"best_single_auroc\": {\"voting_confidence\": 0.8248}}}, \"hypothesis\": \"Bootstrap significance v2: corrected bootstrap test for NER selection F1 gap with proper gold-filtering and multiple signals. Establishes which selection improvements are statistically significant.\"}, \"exp_001_seed456_v2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T15:38:55.569Z\", \"updated_at\": \"2026-05-17T02:57:23.336Z\", \"conclusion\": \"negative\", \"hypothesis\": \"SciERC joint NER+RE seed=456 v2: early pipeline version. Tests multi-seed stability of signal rankings on joint extraction task.\"}, \"exp_017_llama_conll_infer\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T17:33:23.653Z\", \"updated_at\": \"2026-05-17T02:57:21.948Z\", \"metrics\": {\"greedy_f1\": 0.9266, \"oracle_f1\": 0.9443, \"oracle_headroom\": 0.0177, \"n_instances\": 3453, \"n_valid\": 2756, \"n_conditional\": 2642, \"N\": 8, \"full\": {\"SJ_rho\": 0.4314, \"FK_rho\": 0.4277, \"logprob_rho\": 0.3072, \"EM_rho\": 0.4306, \"voting_conf_rho\": 0.4256, \"SJ_AUROC\": 0.7039, \"FK_AUROC\": 0.7026, \"logprob_AUROC\": 0.761, \"EM_AUROC\": 0.7046, \"voting_conf_AUROC\": 0.7088, \"SJ_ECE\": 0.1137, \"FK_ECE\": 0.1053, \"logprob_ECE\": 0.129, \"EM_ECE\": 0.1094, \"voting_conf_ECE\": 0.0949}, \"conditional\": {\"SJ_rho\": 0.4356, \"FK_rho\": 0.431, \"logprob_rho\": 0.3282, \"EM_rho\": 0.4403, \"voting_conf_rho\": 0.3743, \"SJ_AUROC\": 0.7225, \"FK_AUROC\": 0.7208, \"logprob_AUROC\": 0.8102, \"EM_AUROC\": 0.7257, \"voting_conf_AUROC\": 0.6989, \"SJ_ECE\": 0.0829, \"FK_ECE\": 0.0796, \"logprob_ECE\": 0.0922, \"EM_ECE\": 0.0754, \"voting_conf_ECE\": 0.0784}}, \"conclusion\": \"success\", \"notes\": \"LLaMA CoNLL-2003 NER N=8 (not N=16, cost constraint: 3453 test instances). SJ ρ=0.431 > logprob ρ=0.307 (Δ=+0.124). ρ-AUROC dissociation: logprob AUROC=0.761 > SJ AUROC=0.704. All 4 structural signals ρ>0.42 vs logprob 0.31. Directly comparable to exp_002 (Qwen CoNLL N=8) and exp_007 (LLaMA SciERC N=8).\", \"hypothesis\": \"LLaMA CoNLL N=8 baseline inference: initial cross-model test on CoNLL before scaling to N=16. Establishes LLaMA can do CoNLL NER effectively.\"}, \"exp_003_wnut17_v2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T15:32:56.415Z\", \"updated_at\": \"2026-05-17T02:57:20.068Z\", \"conclusion\": \"negative\", \"hypothesis\": \"WNUT-17 NER evaluation v2: tests signal effectiveness on noisy social media text. Hypothesis: structural signals remain effective on noisy, informal text with high entity variation.\"}, \"exp_001_seed456_v2_ner\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T17:13:00.414Z\", \"updated_at\": \"2026-05-17T02:57:18.227Z\", \"conclusion\": \"success\", \"metrics\": {\"full\": {\"SJ\": {\"rho\": 0.384, \"auroc\": 0.711}, \"FK\": {\"rho\": 0.223, \"auroc\": 0.577}, \"logprob\": {\"rho\": 0.232, \"auroc\": 0.594}, \"EM\": {\"rho\": 0.316, \"auroc\": 0.768}, \"voting_conf\": {\"rho\": 0.411, \"auroc\": 0.712}}, \"conditional\": {\"SJ\": {\"rho\": 0.349, \"auroc\": 0.699}, \"FK\": {\"rho\": 0.157, \"auroc\": 0.561}, \"logprob\": {\"rho\": 0.171, \"auroc\": 0.576}, \"EM\": {\"rho\": 0.406, \"auroc\": 0.78}, \"voting_conf\": {\"rho\": 0.346, \"auroc\": 0.694}}, \"3seed_mean_SJ_rho_full\": 0.412, \"3seed_sd_SJ_rho_full\": 0.025, \"structural_beats_surface\": true, \"verdict\": \"MARGINAL\"}, \"hypothesis\": \"SciERC NER seed=456 v2: corrected pipeline rerun with gold-filtering. Part of multi-seed validation protocol for NER signal ranking stability.\"}, \"exp_009_v2_re_rerun\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T18:56:31.535Z\", \"updated_at\": \"2026-05-17T02:57:16.383Z\", \"conclusion\": \"success\", \"hypothesis\": \"Capability stratification v2 (RE rerun): corrected stratification analysis for RE with proper gold-filtering. Fixes early pipeline bug affecting RE quartile ρ values.\"}, \"exp_002_conll_n16\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T18:12:16.041Z\", \"updated_at\": \"2026-05-17T02:57:14.473Z\", \"conclusion\": \"success\", \"metrics\": {\"N\": 16, \"dataset\": \"conll2003\", \"subtask\": \"ner\", \"n_instances\": 3453, \"n_valid\": 2756, \"n_conditional\": 2614, \"greedy_f1\": 0.907, \"full\": {\"SJ_rho\": 0.4496, \"FK_rho\": 0.3928, \"logprob_rho\": 0.3146, \"EM_rho\": 0.4627, \"voting_conf_rho\": 0.4286, \"SJ_AUROC\": 0.8264, \"FK_AUROC\": 0.7821, \"logprob_AUROC\": 0.7531, \"EM_AUROC\": 0.8409, \"voting_conf_AUROC\": 0.8071, \"SJ_ECE\": 0.0747, \"FK_ECE\": 0.1786, \"logprob_ECE\": 0.2031, \"EM_ECE\": 0.0786, \"voting_conf_ECE\": 0.529}, \"conditional\": {\"SJ_rho\": 0.4208, \"FK_rho\": 0.3494, \"logprob_rho\": 0.3756, \"EM_rho\": 0.4658, \"voting_conf_rho\": 0.3654, \"SJ_AUROC\": 0.8405, \"FK_AUROC\": 0.7819, \"logprob_AUROC\": 0.8259, \"EM_AUROC\": 0.8781, \"voting_conf_AUROC\": 0.7951, \"SJ_ECE\": 0.0982, \"FK_ECE\": 0.1899, \"logprob_ECE\": 0.2504, \"EM_ECE\": 0.0997, \"voting_conf_ECE\": 0.6096}, \"n8_vs_n16_delta_rho_full\": {\"SJ\": 0.0139, \"FK\": -0.007, \"logprob\": -0.0011, \"EM\": 0.012, \"voting_conf\": 0.0049}}, \"hypothesis\": \"CoNLL N=16 NER: cross-dataset validation on high-performance NER dataset. Tests if structural signals retain advantage when base model performance is already high (greedy F1 > 0.9).\"}, \"exp_007_llama_n16\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T18:31:44.366Z\", \"updated_at\": \"2026-05-17T02:57:12.521Z\", \"conclusion\": \"success\", \"metrics\": {\"N\": 16, \"dataset\": \"scierc\", \"subtask\": \"ner\", \"n_instances\": 551, \"n_valid\": 529, \"n_conditional\": 478, \"greedy_f1\": 0.645, \"full\": {\"SJ_rho\": 0.3791, \"FK_rho\": 0.3081, \"logprob_rho\": 0.2041, \"EM_rho\": 0.3159, \"voting_conf_rho\": 0.4515, \"SJ_AUROC\": 0.717, \"FK_AUROC\": 0.6581, \"logprob_AUROC\": 0.5656, \"EM_AUROC\": 0.7686, \"voting_conf_AUROC\": 0.7266, \"SJ_ECE\": 0.1019, \"FK_ECE\": 0.1556, \"logprob_ECE\": 0.084, \"EM_ECE\": 0.1761, \"voting_conf_ECE\": 0.1365}, \"conditional\": {\"SJ_rho\": 0.3222, \"FK_rho\": 0.2182, \"logprob_rho\": 0.1286, \"EM_rho\": 0.3563, \"voting_conf_rho\": 0.3356, \"SJ_AUROC\": 0.7014, \"FK_AUROC\": 0.6392, \"logprob_AUROC\": 0.545, \"EM_AUROC\": 0.7708, \"voting_conf_AUROC\": 0.6988, \"SJ_ECE\": 0.1466, \"FK_ECE\": 0.1853, \"logprob_ECE\": 0.1141, \"EM_ECE\": 0.1887, \"voting_conf_ECE\": 0.2634}, \"n8_vs_n16_delta_rho_full\": {\"SJ\": 0.0161, \"FK\": -0.0185, \"logprob\": 0.0214, \"EM\": 0.0007, \"voting_conf\": 0.0184}}, \"hypothesis\": \"LLaMA SciERC N=16: cross-model NER signal evaluation at higher sample count. Tests if LLaMA shows same N-scaling benefit for structural signals as Qwen.\"}, \"exp_017_llama_conll_n16\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T19:19:35.318Z\", \"updated_at\": \"2026-05-17T02:56:57.283Z\", \"metrics\": {\"greedy_f1\": 0.9243, \"oracle_f1\": 0.9487, \"oracle_headroom\": 0.0244, \"n_instances\": 3453, \"n_valid\": 2756, \"n_conditional\": 2642, \"structural_beats_surface\": true, \"full\": {\"SJ_rho\": 0.4642, \"SJ_AUROC\": 0.7391, \"SJ_ECE\": 0.1131, \"FK_rho\": 0.4566, \"FK_AUROC\": 0.736, \"FK_ECE\": 0.1071, \"logprob_rho\": 0.3058, \"logprob_AUROC\": 0.7594, \"logprob_ECE\": 0.1288, \"EM_rho\": 0.4613, \"EM_AUROC\": 0.7391, \"EM_ECE\": 0.1084, \"voting_conf_rho\": 0.4554, \"voting_conf_AUROC\": 0.7406, \"voting_conf_ECE\": 0.0844}, \"conditional\": {\"SJ_rho\": 0.4597, \"SJ_AUROC\": 0.7565, \"SJ_ECE\": 0.0846, \"FK_rho\": 0.4515, \"FK_AUROC\": 0.753, \"FK_ECE\": 0.0813, \"logprob_rho\": 0.3193, \"logprob_AUROC\": 0.8023, \"logprob_ECE\": 0.0921, \"EM_rho\": 0.4618, \"EM_AUROC\": 0.7589, \"EM_ECE\": 0.0757, \"voting_conf_rho\": 0.3978, \"voting_conf_AUROC\": 0.7287, \"voting_conf_ECE\": 0.0742}, \"best_of_n\": {\"greedy\": 0.9243, \"random_avg\": 0.9213, \"sj_best\": 0.9259, \"logprob_best\": 0.925, \"voting_conf_best\": 0.9268, \"oracle\": 0.9487}, \"n8_vs_n16_delta\": {\"full_SJ_rho_delta\": 0.0328, \"full_FK_rho_delta\": 0.0289, \"full_logprob_rho_delta\": -0.0014, \"full_EM_rho_delta\": 0.0307, \"full_voting_conf_rho_delta\": 0.0298, \"cond_SJ_rho_delta\": 0.0241, \"cond_FK_rho_delta\": 0.0205, \"cond_logprob_rho_delta\": -0.0089, \"cond_EM_rho_delta\": 0.0215, \"cond_voting_conf_rho_delta\": 0.0235}}, \"conclusion\": \"success\", \"hypothesis\": \"LLaMA CoNLL N=16 seed=42 (original): cross-model validation on CoNLL. First evidence that structural>surface ranking generalizes from Qwen to LLaMA model family.\"}, \"exp_015_v2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T15:34:23.336Z\", \"updated_at\": \"2026-05-17T02:56:55.830Z\", \"conclusion\": \"success\", \"metrics\": {\"scierc_ner_avg\": {\"sj_auroc\": 0.7394, \"fk_auroc\": 0.6172, \"em_auroc\": 0.7873, \"voting_auroc\": 0.7367, \"logprob_auroc\": 0.5918}, \"scierc_re_avg\": {\"sj_auroc\": 0.6746, \"fk_auroc\": 0.5939, \"em_auroc\": 0.715, \"voting_auroc\": 0.7234, \"logprob_auroc\": 0.5849}}, \"hypothesis\": \"Metrics expansion v2: corrected evaluation with proper conditional filtering. Updates exp_015 with gold-filtered pipeline to fix RE conditional ρ values that used wrong filter criterion.\"}, \"exp_001_n16_seed456\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T12:10:30.350Z\", \"updated_at\": \"2026-05-17T02:56:53.526Z\", \"conclusion\": \"success\", \"metrics\": {\"instance_count\": 551, \"n_valid\": 529, \"n_gold_empty\": 22, \"parse_rate\": 1, \"ner_greedy_f1\": 0.6617, \"ner_oracle_f1\": 0.8075, \"re_greedy_f1\": 0.4215, \"re_oracle_f1\": 0.4748, \"rho_sj_ner\": 0.4098, \"rho_fk_ner\": 0.2723, \"rho_vc_ner\": 0.4449, \"rho_em_ner\": 0.3363, \"rho_lp_ner\": 0.2415, \"rho_sj_re\": 0.2835, \"rho_fk_re\": 0.2929, \"auroc_sj_ner\": 0.6823, \"auroc_fk_ner\": 0.6179, \"auroc_vc_ner\": 0.6981, \"auroc_em_ner\": 0.649, \"auroc_lp_ner\": 0.5885, \"rho_note\": \"CORRECTED 2026-05-15: old values (rho_fk=0.3448,rho_sj=0.4134) included 22 gold-empty instances. Now uses gold-filtered pipeline (n=529).\"}, \"hypothesis\": \"SciERC N=16 seed=456: early multi-seed validation of structural signal rankings at N=16 sample count. Establishes seed stability for SJ/FK/VC/EM ordering.\"}, \"exp_018_qwen_scierc_seed123\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T06:07:12.747Z\", \"updated_at\": \"2026-05-17T02:56:52.088Z\", \"conclusion\": \"success\", \"hypothesis\": \"Qwen SciERC seed=123: multi-seed Qwen validation. Part of 3-seed protocol (seed42=exp_012_rerun_1024, seed123, seed456) for statistical significance of signal rankings.\"}, \"exp_018_qwen_scierc_seed456\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T06:07:13.570Z\", \"updated_at\": \"2026-05-17T02:56:50.665Z\", \"conclusion\": \"success\", \"hypothesis\": \"Qwen SciERC seed=456: multi-seed Qwen validation. Part of 3-seed protocol (seed42=exp_012_rerun_1024, seed123, seed456) for statistical significance of signal rankings.\"}, \"exp_018_llama_scierc_seed123\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T06:07:14.370Z\", \"updated_at\": \"2026-05-17T02:56:48.836Z\", \"conclusion\": \"success\", \"hypothesis\": \"LLaMA SciERC seed=123: multi-seed cross-model validation. Complements seed42 for LLaMA 3-seed protocol on SciERC NER+RE signal rankings.\"}, \"exp_018_llama_scierc_seed456_r1024\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T06:12:43.492Z\", \"updated_at\": \"2026-05-17T02:56:47.311Z\", \"metrics\": {\"ner_greedy_f1\": 0.6597, \"ner_oracle_f1\": 0.7683, \"ner_oracle_headroom\": 0.1086, \"ner_cond_rho_fk\": 0.1472, \"ner_cond_rho_sj\": 0.2718, \"ner_cond_rho_logprob\": 0.083, \"ner_logprob_auroc_cond\": 0.5485, \"re_greedy_f1\": 0.4338, \"re_oracle_f1\": 0.5834, \"re_oracle_headroom\": 0.1496, \"re_cond_rho_fk\": 0.2107, \"re_cond_rho_sj\": 0.3898, \"re_cond_rho_logprob\": 0.1252, \"re_logprob_auroc_cond\": 0.6119, \"ner_structural_beats_logprob\": true, \"re_structural_beats_logprob\": true}, \"conclusion\": \"success\", \"hypothesis\": \"LLaMA SciERC seed=456 (max_tokens=1024): multi-seed cross-model validation. Complements seed42 for LLaMA 3-seed protocol on SciERC NER+RE signal rankings.\"}, \"exp_018_llama_scierc_seed42_r1024\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T06:09:57.155Z\", \"updated_at\": \"2026-05-17T02:56:37.484Z\", \"metrics\": {\"ner\": {\"full\": {\"SJ\": {\"rho\": 0.3096, \"tau\": 0.2288, \"auroc\": 0.6683}, \"FK\": {\"rho\": 0.2352, \"tau\": 0.1759, \"auroc\": 0.6069}, \"logprob\": {\"rho\": 0.1503, \"tau\": 0.1087, \"auroc\": 0.5318}, \"EM\": {\"rho\": 0.2587, \"tau\": 0.1966, \"auroc\": 0.7174}, \"voting_conf\": {\"rho\": 0.4053, \"tau\": 0.3042, \"auroc\": 0.6967}}, \"conditional\": {\"SJ\": {\"rho\": 0.2718, \"tau\": null, \"auroc\": 0.6565}, \"FK\": {\"rho\": 0.1472, \"tau\": null, \"auroc\": 0.5866}, \"logprob\": {\"rho\": 0.081, \"tau\": null, \"auroc\": 0.5129}, \"EM\": {\"rho\": 0.3165, \"tau\": null, \"auroc\": 0.7244}, \"voting_conf\": {\"rho\": 0.3078, \"tau\": null, \"auroc\": 0.6714}}, \"greedy_f1\": 0.6607, \"oracle_f1\": 0.7781, \"n_full\": 529, \"n_cond\": 478}, \"re\": {\"full\": {\"SJ\": {\"rho\": 0.2748, \"tau\": 0.2102, \"auroc\": 0.7244}, \"FK\": {\"rho\": 0.3027, \"tau\": 0.2337, \"auroc\": 0.691}, \"logprob\": {\"rho\": 0.3163, \"tau\": 0.233, \"auroc\": 0.6313}, \"EM\": {\"rho\": 0.1681, \"tau\": 0.1275, \"auroc\": 0.7697}, \"voting_conf\": {\"rho\": 0.384, \"tau\": 0.2965, \"auroc\": 0.7337}}, \"conditional\": {\"SJ\": {\"rho\": 0.3461, \"tau\": null, \"auroc\": 0.7233}, \"FK\": {\"rho\": 0.1969, \"tau\": null, \"auroc\": 0.6684}, \"logprob\": {\"rho\": 0.0888, \"tau\": null, \"auroc\": 0.5556}, \"EM\": {\"rho\": 0.4969, \"tau\": null, \"auroc\": 0.819}, \"voting_conf\": {\"rho\": 0.3433, \"tau\": null, \"auroc\": 0.7003}}, \"greedy_f1\": 0.4319, \"oracle_f1\": 0.5775, \"n_full\": 397, \"n_cond\": 251}}, \"conclusion\": \"success\", \"hypothesis\": \"LLaMA SciERC seed=42 (max_tokens=1024): cross-model validation on SciERC. Establishes LLaMA NER signal rankings on same dataset as Qwen for direct model-family comparison.\"}, \"exp_017_llama_conll_n16_r1024\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T22:17:01.036Z\", \"updated_at\": \"2026-05-17T02:56:35.788Z\", \"conclusion\": \"success\", \"metrics\": {\"instance_count\": 3453, \"n_valid\": 2756, \"n_gold_empty\": 697, \"parse_rate\": 1, \"ner_greedy_f1\": 0.9265, \"ner_oracle_f1\": 0.9499, \"rho_fk_ner\": 0.4752, \"rho_sj_ner\": 0.4836, \"rho_vc_ner\": 0.4746, \"rho_em_ner\": 0.4818, \"rho_lp_ner\": 0.3136, \"auroc_fk_ner\": 0.7467, \"auroc_sj_ner\": 0.7496, \"auroc_vc_ner\": 0.7529, \"auroc_em_ner\": 0.7508, \"auroc_lp_ner\": 0.7661, \"auroc_note\": \"median F1=1.0, AUROC uses >=median threshold\", \"rho_note\": \"CORRECTED 2026-05-15: old values (rho_fk=0.8095,rho_sj=0.1815) were inflated/deflated by 697 gold-empty instances. Now uses gold-filtered pipeline (n=2756).\"}, \"hypothesis\": \"LLaMA CoNLL N=16 seed=42 (max_tokens=1024 rerun): cross-model baseline on CoNLL. Establishes LLaMA signal rankings after gold-filtering correction (fixes inflated FK ρ from gold-empty instances).\"}, \"exp_017_llama_conll_n16_s456_r1024\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T22:17:04.572Z\", \"updated_at\": \"2026-05-17T02:56:33.722Z\", \"conclusion\": \"success\", \"metrics\": {\"instance_count\": 3453, \"n_valid\": 2756, \"n_gold_empty\": 697, \"parse_rate\": 1, \"ner_greedy_f1\": 0.9265, \"ner_oracle_f1\": 0.9499, \"rho_fk_ner\": 0.469, \"rho_sj_ner\": 0.4734, \"rho_vc_ner\": 0.4722, \"rho_em_ner\": 0.4752, \"rho_lp_ner\": 0.3099, \"auroc_fk_ner\": 0.7408, \"auroc_sj_ner\": 0.7428, \"auroc_vc_ner\": 0.7495, \"auroc_em_ner\": 0.7444, \"auroc_lp_ner\": 0.7628, \"auroc_note\": \"median F1=1.0, AUROC uses >=median threshold\", \"rho_note\": \"CORRECTED 2026-05-15: old values (rho_fk=0.8085,rho_sj=0.1895) were inflated/deflated by 697 gold-empty instances. Now uses gold-filtered pipeline (n=2756).\"}, \"hypothesis\": \"LLaMA CoNLL N=16 seed=456 (max_tokens=1024 rerun): cross-model multi-seed validation. Confirms structural>surface ordering is stable across seeds for LLaMA on CoNLL after gold-filtering correction.\"}, \"exp_017_llama_conll_n16_s123_r1024\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T22:17:02.953Z\", \"updated_at\": \"2026-05-17T02:56:32.157Z\", \"conclusion\": \"success\", \"notes\": \"Output exists on autodl-5090. Registry status corrected from killed to success.\", \"hypothesis\": \"LLaMA CoNLL N=16 seed=123 (max_tokens=1024 rerun): cross-model multi-seed validation. Confirms structural>surface ordering is stable across seeds for LLaMA on CoNLL after gold-filtering correction.\"}, \"exp_011_ood_scierc_to_conll\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T11:36:07.210Z\", \"updated_at\": \"2026-05-17T02:56:29.417Z\", \"conclusion\": \"success\", \"metrics\": {\"greedy_ner_f1\": 0.522, \"rho_vc\": 0.469, \"rho_sj\": 0.378, \"rho_em\": 0.3, \"rho_fk\": 0.285, \"rho_lp\": 0.246}, \"hypothesis\": \"Out-of-domain transfer: SciERC-trained model on CoNLL data. Tests if confidence signals work under partial schema overlap (SciERC has Organization/Person which overlap with CoNLL ORG/PER). Complement to exp_011_ood_conll_to_scierc.\"}, \"exp_qwen3_4b_conll_scs_inference\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T19:08:28.512Z\", \"updated_at\": \"2026-05-17T02:56:26.975Z\", \"metrics\": {\"greedy_f1\": 0.9251, \"oracle_f1\": 0.9408, \"oracle_headroom_pp\": 1.57, \"SJ_rho_full\": 0.4045, \"SJ_rho_cond\": 0.4306, \"FK_rho_full\": 0.3961, \"FK_rho_cond\": 0.42, \"LP_rho_full\": 0.3186, \"LP_rho_cond\": 0.3378, \"LP_auroc_full\": 0.7689, \"LP_auroc_cond\": 0.8153, \"fleiss_kappa_mean\": 0.9349, \"soft_jaccard_mean\": 0.9754, \"structural_beats_surface\": true, \"rho_advantage_pp\": 0.84, \"n_instances\": 3453, \"n_gold_empty_filtered\": 697, \"n_greedy_f1_zero_filtered\": 112, \"verdict\": \"MARGINAL\"}, \"conclusion\": \"success\", \"notes\": \"4B CoNLL SCS inference completed. SJ>FK>LP ordering preserved at 4B scale (rho 0.405>0.396>0.319). Greedy F1=0.925 outperforms 8B (0.907), but SJ rho is lower (0.405 vs 0.450 at 8B N=16). Structural beats surface confirmed (+0.84pp). Verdict MARGINAL due to small oracle headroom (1.57pp) — the model is already very good at CoNLL, leaving little room for selection improvement.\", \"hypothesis\": \"CoNLL 4B SCS inference (checkpoint-3800): cross-scale evidence for correlation-selection gap. Tests if structural>surface ranking and LP compression hold at smaller model scale on high-degeneracy dataset.\"}, \"exp_qwen3_4b_scierc_finetune_v4\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T19:26:25.512Z\", \"updated_at\": \"2026-05-17T02:56:24.418Z\", \"conclusion\": \"success\", \"metrics\": {\"total_steps\": 585, \"completed_steps\": 585, \"best_checkpoint\": \"checkpoint-400\", \"best_eval_loss\": 0.0898, \"epochs\": 5}, \"hypothesis\": \"Qwen3-4B SciERC LoRA fine-tune v4: training the smaller 4B model to complete the 2x2 scale matrix (4B×SciERC cell). Validates that fine-tuning convergence patterns hold across model scales.\"}, \"exp_011_ood_conll_to_scierc\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T11:36:08.325Z\", \"updated_at\": \"2026-05-17T02:56:14.242Z\", \"conclusion\": \"negative\", \"metrics\": {\"greedy_ner_f1\": 0.009, \"greedy_re_f1\": 0.001, \"avg_structural_rho\": -0.05, \"verdict\": \"FAIL\", \"reason\": \"schema_incompatibility\", \"direction\": \"CoNLL_model_to_SciERC_data\", \"sample_f1_pct_zero_ner\": 98.06, \"rho_sj_ner\": -0.186, \"rho_fk_ner\": -0.069, \"note\": \"Schema incompatibility (CoNLL PER/ORG/LOC/MISC vs SciERC Task/Method/Material) causes catastrophic failure. Cannot evaluate confidence signals.\"}, \"hypothesis\": \"Out-of-domain transfer test: CoNLL-trained model on SciERC data. Tests if confidence signals retain correlation with quality under severe schema mismatch (CoNLL PER/ORG/LOC/MISC vs SciERC Task/Method/Material).\"}, \"exp_freeform_seed789_v3\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T19:24:26.805Z\", \"updated_at\": \"2026-05-17T02:56:11.818Z\", \"conclusion\": \"success\", \"metrics\": {\"n_instances\": 551, \"n_samples\": 8, \"parse_rate_pct\": 100, \"elapsed_seconds\": 229.7, \"freeform_ner_selection_gap\": 0.0028, \"freeform_re_selection_gap\": 0.0219, \"freeform_lp_std\": 0.0183, \"freeform_lp_range\": 0.054908, \"freeform_tied_pct\": 59, \"re_lp_flip_positive\": true, \"variance_ratio_std\": 0.89, \"variance_ratio_range\": 0.88}, \"hypothesis\": \"Free-form SciERC seed=789 v3 (bugfix rerun): corrected version of free-form inference after fixing parsing/generation issues in v1/v2. Provides clean data point for 4-seed free-form analysis.\"}, \"exp_freeform_seed789\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T18:38:29.851Z\", \"updated_at\": \"2026-05-17T02:56:09.888Z\", \"notes\": \"Rerun with fixed seed-passing code on cuda:3. Original run was killed for GPU reallocation. Parse rate 100%, 227.5s elapsed. LP compression confirmed: tied_pct=59.0% (vs constrained 59.7%), variance_ratio=0.89x.\", \"conclusion\": \"success\", \"metrics\": {\"inference\": {\"n_instances\": 551, \"n_samples\": 8, \"total_samples\": 4408, \"total_parsed\": 4408, \"parse_rate_pct\": 100, \"elapsed_seconds\": 227.5}, \"freeform\": {\"selection_ner\": {\"greedy\": 0.6205, \"selected\": 0.6232, \"gap\": 0.0027}, \"selection_re\": {\"greedy\": 0.2909, \"selected\": 0.31, \"gap\": 0.0191}, \"logprob_variance\": {\"mean_std\": 0.0183, \"mean_range\": 0.054908, \"tied_pct\": 59}, \"qe_ner\": {\"n\": 529, \"SJ\": {\"rho\": 0.393995, \"auroc\": 0.734474}, \"FK\": {\"rho\": 0.312292, \"auroc\": 0.794384}, \"LP\": {\"rho\": 0.247096, \"auroc\": 0.677824}, \"EM\": {\"rho\": 0.320383, \"auroc\": 0.527033}, \"VC\": {\"rho\": 0.420625, \"auroc\": 0.768111}}, \"qe_re\": {\"n\": 397, \"SJ\": {\"rho\": 0.201746, \"auroc\": 0.574388}, \"FK\": {\"rho\": 0.2202, \"auroc\": 0.633014}, \"LP\": {\"rho\": 0.295765, \"auroc\": 0.687067}, \"EM\": {\"rho\": 0.103633, \"auroc\": 0.474737}, \"VC\": {\"rho\": 0.306868, \"auroc\": 0.642197}}}, \"constrained_ref\": {\"selection_ner\": {\"greedy\": 0.6182, \"selected\": 0.6241, \"gap\": 0.0059}, \"selection_re\": {\"greedy\": 0.2913, \"selected\": 0.2845, \"gap\": -0.0068}, \"logprob_variance\": {\"mean_std\": 0.020589, \"mean_range\": 0.062305, \"tied_pct\": 59.7}}, \"comparison\": {\"variance_ratio_std\": 0.89, \"variance_ratio_range\": 0.88, \"tied_reduction_pp\": 0.7}}, \"hypothesis\": \"Free-form SciERC seed=789: multi-seed replication of free-form ablation. Validates LP compression persistence and structural signal robustness across sampling seeds under unconstrained generation.\"}, \"exp_freeform_seed456\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T17:14:48.842Z\", \"updated_at\": \"2026-05-17T02:56:09.256Z\", \"metrics\": {\"inference\": {\"n_instances\": 551, \"n_samples\": 8, \"total_samples\": 4408, \"total_parsed\": 4407, \"parse_rate_pct\": 99.98, \"elapsed_seconds\": 232.4}, \"freeform\": {\"selection_ner\": {\"greedy\": 0.6198, \"selected\": 0.6205, \"gap\": 0.0007}, \"selection_re\": {\"greedy\": 0.2908, \"selected\": 0.3108, \"gap\": 0.02}, \"logprob_variance\": {\"mean_std\": 0.018631, \"mean_range\": 0.056792, \"tied_pct\": 58.4}, \"qe_ner\": {\"n\": 529, \"SJ\": {\"rho\": 0.378498, \"auroc\": 0.707769}, \"FK\": {\"rho\": 0.286163, \"auroc\": 0.754779}, \"LP\": {\"rho\": 0.227089, \"auroc\": 0.672081}, \"EM\": {\"rho\": 0.319997, \"auroc\": 0.47789}, \"VC\": {\"rho\": 0.416853, \"auroc\": 0.756543}}, \"qe_re\": {\"n\": 397, \"SJ\": {\"rho\": 0.211331, \"auroc\": 0.572335}, \"FK\": {\"rho\": 0.259074, \"auroc\": 0.652998}, \"LP\": {\"rho\": 0.306382, \"auroc\": 0.70134}, \"EM\": {\"rho\": 0.1043, \"auroc\": 0.461641}, \"VC\": {\"rho\": 0.301507, \"auroc\": 0.628873}}}, \"constrained_ref\": {\"selection_ner\": {\"greedy\": 0.6182, \"selected\": 0.6241, \"gap\": 0.0059}, \"selection_re\": {\"greedy\": 0.2913, \"selected\": 0.2845, \"gap\": -0.0068}, \"logprob_variance\": {\"mean_std\": 0.020589, \"mean_range\": 0.062305, \"tied_pct\": 59.7}}, \"comparison\": {\"variance_ratio_std\": 0.9, \"variance_ratio_range\": 0.91, \"tied_reduction_pp\": 1.3}}, \"conclusion\": \"success\", \"hypothesis\": \"Free-form SciERC seed=456: multi-seed replication of free-form ablation. Validates LP compression persistence and structural signal robustness across sampling seeds under unconstrained generation.\"}, \"exp_freeform_seed123\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T17:14:47.765Z\", \"updated_at\": \"2026-05-17T02:56:06.903Z\", \"metrics\": {\"inference\": {\"n_instances\": 551, \"n_samples\": 8, \"total_samples\": 4408, \"total_parsed\": 4406, \"parse_rate_pct\": 99.95, \"elapsed_seconds\": 228.1}, \"freeform\": {\"selection_ner\": {\"greedy\": 0.6194, \"selected\": 0.6222, \"gap\": 0.0028}, \"selection_re\": {\"greedy\": 0.2874, \"selected\": 0.305, \"gap\": 0.0176}, \"logprob_variance\": {\"mean_std\": 0.019881, \"mean_range\": 0.059864, \"tied_pct\": 57.7}, \"qe_ner\": {\"n\": 529, \"SJ\": {\"rho\": 0.384214, \"auroc\": 0.748728}, \"FK\": {\"rho\": 0.323956, \"auroc\": 0.766039}, \"logprob\": {\"rho\": 0.217297, \"auroc\": 0.701657}, \"EM\": {\"rho\": 0.326887, \"auroc\": 0.52533}, \"voting_conf\": {\"rho\": 0.407893, \"auroc\": 0.799676}}, \"qe_re\": {\"n\": 397, \"SJ\": {\"rho\": 0.272776, \"auroc\": 0.614056}, \"FK\": {\"rho\": 0.314429, \"auroc\": 0.678534}, \"logprob\": {\"rho\": 0.309673, \"auroc\": 0.70414}, \"EM\": {\"rho\": 0.137216, \"auroc\": 0.487342}, \"voting_conf\": {\"rho\": 0.316667, \"auroc\": 0.647442}}}, \"constrained_ref\": {\"selection_ner\": {\"greedy\": 0.6182, \"selected\": 0.6241, \"gap\": 0.0059}, \"selection_re\": {\"greedy\": 0.2913, \"selected\": 0.2845, \"gap\": -0.0068}}, \"comparison\": {\"variance_ratio_std\": 0.97, \"variance_ratio_range\": 0.96, \"tied_reduction_pp\": 2}}, \"conclusion\": \"success\", \"hypothesis\": \"Free-form SciERC seed=123: multi-seed replication of free-form ablation. Validates LP compression persistence and structural signal robustness across sampling seeds under unconstrained generation.\"}, \"exp_009_capability_stratification\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T14:59:24.201Z\", \"updated_at\": \"2026-05-17T02:56:02.685Z\", \"conclusion\": \"success\", \"metrics\": {\"scierc_ner\": {\"n\": 551, \"sj_rho_overall\": 0.398, \"by_greedy_f1\": {\"hard_0_25_sj_rho\": 0.159, \"med_low_sj_rho\": 0.139, \"med_high_sj_rho\": 0.09, \"easy_sj_rho\": 0.23}, \"by_sent_len\": {\"Q1_sj_rho\": 0.461, \"Q2_sj_rho\": 0.401, \"Q3_sj_rho\": 0.296, \"Q4_sj_rho\": 0.382}, \"by_ent_count\": {\"0_sj_rho\": 0.689, \"1_2_sj_rho\": 0.415, \"3_5_sj_rho\": 0.353, \"6plus_sj_rho\": 0.547}}, \"scierc_re\": {\"n\": 551, \"by_greedy_f1\": {\"hard_0_25_sj_rho\": -0.043, \"easy_sj_rho\": 0.21}, \"by_sent_len\": {\"Q1_sj_rho\": 0.447, \"Q4_sj_rho\": 0.54}, \"by_rel_count\": {\"0_sj_rho\": 0.62, \"1_2_sj_rho\": 0.275, \"6plus_sj_rho\": 0.527}}, \"conll_ner\": {\"n\": 3453, \"by_sent_len\": {\"Q1_sj_rho\": 0.334, \"Q3_sj_rho\": 0.518}}, \"proxy_independence\": {\"scierc_ner_f1_vs_slen\": -0.021, \"scierc_ner_f1_vs_ecnt\": 0.007, \"scierc_re_f1_vs_slen\": -0.147}}, \"notes\": \"Registry metrics are PRE-gold-filter (n=551). Paper uses exp_009_v2_re_rerun (gold-filtered n=397): RE Q1_sj_rho=0.110, Q4_sj_rho=0.473. Registry values (Q1=0.447, Q4=0.540) are SUPERSEDED.\", \"hypothesis\": \"Capability stratification analysis: test if SJ signal effectiveness varies with instance difficulty (greedy F1 quartiles), sentence length, and entity/relation count. Identifies which instance subpopulations benefit most from structural consistency signals.\"}, \"exp_023_lora_rank8\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T10:29:59.501Z\", \"updated_at\": \"2026-05-17T02:55:50.540Z\", \"conclusion\": \"success\", \"metrics\": {\"train_loss\": 0.1018, \"eval_loss\": 0.0776, \"train_runtime\": \"28m45s\", \"ner_full\": {\"n\": 529, \"greedy_f1\": 0.6397, \"oracle_f1\": 0.7998, \"oracle_headroom\": 0.1601, \"degeneracy_rate\": 0.072, \"SJ_rho\": 0.3649, \"FK_rho\": 0.2838, \"VC_rho\": 0.394, \"EM_rho\": 0.2562, \"LP_rho\": 0.2105, \"SJ_auroc\": 0.689, \"FK_auroc\": 0.6002, \"VC_auroc\": 0.6886, \"EM_auroc\": 0.7265, \"LP_auroc\": 0.6054, \"sel_SJ\": 0.6306, \"sel_FK\": 0.6265, \"sel_VC\": 0.5919, \"sel_EM\": 0.6073, \"sel_LP\": 0.635}, \"ner_cond\": {\"n\": 477, \"SJ_rho\": 0.3056, \"FK_rho\": 0.1452, \"VC_rho\": 0.3191, \"EM_rho\": 0.3558, \"LP_rho\": 0.169}, \"re_full\": {\"n\": 397, \"greedy_f1\": 0.3712, \"oracle_f1\": 0.609, \"oracle_headroom\": 0.2378, \"degeneracy_rate\": 0.217, \"SJ_rho\": 0.2244, \"FK_rho\": 0.3448, \"VC_rho\": 0.3617, \"EM_rho\": 0.068, \"LP_rho\": 0.2737, \"SJ_auroc\": 0.7092, \"FK_auroc\": 0.6469, \"VC_auroc\": 0.7533, \"EM_auroc\": 0.7306, \"LP_auroc\": 0.6325, \"sel_SJ\": 0.3584, \"sel_FK\": 0.3498, \"sel_VC\": 0.3715, \"sel_EM\": 0.3291, \"sel_LP\": 0.3606}, \"re_cond\": {\"n\": 242, \"SJ_rho\": 0.3601, \"FK_rho\": 0.2343, \"VC_rho\": 0.3703, \"EM_rho\": 0.4613, \"LP_rho\": 0.1809}}, \"hypothesis\": \"LoRA rank=8 ablation on SciERC: test if reduced model capacity (rank 8 vs 32) changes signal effectiveness ranking or correlation-selection gap pattern. Verifies findings are not rank-specific artifacts.\", \"parent\": \"exp_012_rerun_1024\"}, \"exp_022_seed789\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T10:08:27.375Z\", \"updated_at\": \"2026-05-17T02:55:49.870Z\", \"hypothesis\": \"3rd seed SciERC inference (seed=789) with ft_002_v2 (Qwen3-8B). N=8, T=1.0, joint NER+RE, logprobs collected. Complements seed42 (exp_012_rerun_1024) and seed123/456 for multi-seed analysis.\", \"conclusion\": \"success\", \"parent\": \"exp_012_rerun_1024\"}, \"exp_026_t05\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T12:19:35.753Z\", \"updated_at\": \"2026-05-17T02:55:48.900Z\", \"conclusion\": \"success\", \"metrics\": {\"temperature\": 0.5, \"task\": \"T-ablation\"}, \"hypothesis\": \"Temperature T=0.5 ablation on SciERC: extreme low temperature expected to maximally compress LP scores and increase degeneracy, providing upper-bound evidence for LP compression as model-intrinsic phenomenon.\", \"parent\": \"exp_012_rerun_1024\"}, \"exp_026_t08\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T12:57:46.027Z\", \"updated_at\": \"2026-05-17T02:55:47.964Z\", \"conclusion\": \"success\", \"metrics\": {\"temperature\": 0.8, \"task\": \"T-ablation\"}, \"hypothesis\": \"Temperature T=0.8 ablation on SciERC: test if lower temperature increases LP compression (narrower range) while structural signals remain robust, supporting the claim that LP compression is intrinsic rather than temperature-driven.\", \"parent\": \"exp_012_rerun_1024\"}, \"exp_026_t12\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T13:18:18.780Z\", \"updated_at\": \"2026-05-17T02:55:46.995Z\", \"conclusion\": \"success\", \"metrics\": {\"temperature\": 1.2, \"task\": \"T-ablation\"}, \"hypothesis\": \"Temperature T=1.2 ablation on SciERC: test if higher temperature increases sample diversity (lower degeneracy) and LP discriminative range, potentially improving LP selection while maintaining structural signal effectiveness.\", \"parent\": \"exp_012_rerun_1024\"}, \"exp_025_n32\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T13:38:26.420Z\", \"updated_at\": \"2026-05-17T02:55:46.212Z\", \"conclusion\": \"success\", \"metrics\": {\"n_samples\": 32, \"degeneracy_pct\": 4, \"lp_range\": 0.0781, \"oracle_f1\": 0.8412, \"greedy_f1\": 0.6615, \"oracle_gap\": 0.1797, \"selection_f1_lp_delta\": 0.54, \"selection_f1_sj_delta\": 0.16, \"selection_f1_fk_delta\": 0.6, \"selection_f1_em_delta\": 0.68, \"selection_f1_vc_delta\": -5.21, \"best_signal\": \"EM\", \"best_delta\": 0.68, \"metric_space\": \"micro_f1_filtered_529inst\", \"note\": \"corrected via n_ablation_fixed.py, greedy from inst['greedy'] field\"}, \"hypothesis\": \"N=32 sample ablation on SciERC: test if increasing samples from 8→32 reduces degeneracy and improves selection F1, particularly for structural signals. Validates whether sample count is the bottleneck for signal effectiveness.\", \"parent\": \"exp_012_rerun_1024\"}, \"exp_021_fewnerd_full\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T16:33:44.079Z\", \"updated_at\": \"2026-05-17T02:55:45.560Z\", \"hypothesis\": \"Full Few-NERD LoRA fine-tune (rank=32, α=64, 3 epochs) on SUPERVISED coarse 8-type NER (131k train). 4-GPU DDP on autodl-5090. Post-training: N=8 inference on full test set, T=1.0, seed=42, collect logprobs for SCS metrics.\", \"conclusion\": \"success\", \"metrics\": {\"total_steps\": 6177, \"train_loss\": 0.048, \"eval_loss\": 0.0275, \"train_runtime\": \"3h57m\", \"epochs\": 3, \"final_checkpoint\": \"output/exp_021_fewnerd_full/checkpoint-6177\", \"adapter_path\": \"output/exp_021_fewnerd_full/adapter_model.safetensors\", \"inference_instances\": 37648, \"inference_filtered\": 32565, \"inference_n_samples\": 8, \"greedy_macro_f1\": 0.7478, \"oracle_macro_f1\": 0.8719, \"headroom\": 0.124, \"zero_f1_rate\": 0.119, \"degeneracy_rate\": 0.101, \"lp_within_range_mean\": 0.0879, \"lp_within_range_median\": 0.0662, \"lp_global_rho\": 0.4215, \"lp_cond_rho\": 0.4225, \"sj_global_rho\": 0.3002, \"sj_cond_rho\": 0.2937, \"fk_global_rho\": 0.3132, \"fk_cond_rho\": 0.3093, \"em_global_rho\": 0.2871, \"em_cond_rho\": 0.271, \"vc_global_rho\": 0.3858, \"vc_cond_rho\": 0.3234, \"lp_selection_delta_pp\": 1.36, \"vc_selection_delta_pp\": -1.79, \"sj_selection_delta_pp\": -2.14, \"fk_selection_delta_pp\": -2.26, \"em_selection_delta_pp\": -3.85, \"lp_bootstrap_ci_95_pp\": [1.18, 1.53], \"lp_sample_auroc\": 0.5782, \"vc_sample_auroc\": 0.5354, \"fk_sample_auroc\": 0.521, \"sj_sample_auroc\": 0.5197, \"em_sample_auroc\": 0.5137, \"scenario\": \"A_partial\", \"note\": \"Full analysis (gold-filtered n=32565). Prior simplified analysis used unfiltered data with different metrics.\"}, \"parent\": \"exp_020_fewnerd_smoke\"}, \"exp_015_metrics_expansion\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T11:47:36.569Z\", \"updated_at\": \"2026-05-17T02:55:35.391Z\", \"conclusion\": \"success\", \"metrics\": {\"data_source\": \"exp_012_logprob/samples_with_logprobs.jsonl\", \"config\": \"N=8, T=1.0, seed=42, model=qwen3-8b-scierc-merged-v2\", \"ner\": {\"n_valid\": 529, \"n_cond\": 501, \"voting_rho_full\": 0.5018, \"voting_rho_cond\": 0.4497, \"voting_auroc\": 0.7279, \"voting_tau\": 0.3766, \"sj_rho_full\": 0.3565, \"sj_rho_cond\": 0.412, \"sj_auroc\": 0.6656, \"sj_tau\": 0.2658, \"em_rho_full\": 0.2566, \"em_rho_cond\": 0.3427, \"em_auroc\": 0.623, \"em_tau\": 0.1924, \"fk_rho_full\": 0.2651, \"fk_rho_cond\": 0.306, \"fk_auroc\": 0.6243, \"fk_tau\": 0.2027, \"logprob_rho_full\": 0.1396, \"logprob_rho_cond\": 0.1627, \"logprob_auroc\": 0.5585, \"logprob_tau\": 0.1006}, \"re\": {\"n_valid\": 397, \"n_cond\": 296, \"voting_rho_full\": 0.4217, \"voting_rho_cond\": 0.463, \"voting_auroc\": 0.7162, \"voting_tau\": 0.327, \"sj_rho_full\": 0.2112, \"sj_rho_cond\": 0.3683, \"sj_auroc\": 0.5816, \"sj_tau\": 0.1619, \"em_rho_full\": 0.1002, \"em_rho_cond\": 0.3607, \"em_auroc\": 0.5036, \"em_tau\": 0.0839, \"fk_rho_full\": 0.2528, \"fk_rho_cond\": 0.3168, \"fk_auroc\": 0.6308, \"fk_tau\": 0.1967, \"logprob_rho_full\": 0.2467, \"logprob_rho_cond\": 0.1457, \"logprob_auroc\": 0.6354, \"logprob_tau\": 0.1808}, \"diagnosis\": \"Unified 5-signal evaluation on single data source. Voting leads NER full (ρ=0.502), SJ retains strength in NER cond (ρ=0.412). All structural signals beat logprob on NER. RE: voting leads both full and cond.\"}, \"notes\": \"RE logprob_rho_cond=0.1457 uses WRONG conditional filter (any sample F1>0, n=331). Correct value: 0.0112 from exp_012_rerun_1024 (greedy_f1>0, n=238). This entry's RE cond values are DEPRECATED.\", \"hypothesis\": \"Unified 5-signal evaluation (SJ/FK/EM/VC/LP) on single canonical data source (exp_012 logprobs). Establishes complete signal ranking with ρ, AUROC, and τ metrics for both NER and RE under consistent conditions.\"}, \"exp_012_rerun_1024\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T22:11:33.777Z\", \"updated_at\": \"2026-05-17T02:55:23.561Z\", \"conclusion\": \"success\", \"metrics\": {\"ner_full\": {\"n\": 529, \"SJ\": {\"rho\": 0.3599, \"tau\": 0.2646, \"AUROC\": 0.6917, \"ECE\": 0.4531, \"rho_ci95\": [0.2732, 0.4389], \"AUROC_ci95\": [0.6304, 0.7406]}, \"FK\": {\"rho\": 0.2665, \"tau\": 0.1974, \"AUROC\": 0.629, \"ECE\": 0.4512, \"rho_ci95\": [0.1743, 0.3486], \"AUROC_ci95\": [0.5612, 0.6882]}, \"logprob\": {\"rho\": 0.2052, \"tau\": 0.1478, \"AUROC\": 0.5783, \"ECE\": 0.7064, \"rho_ci95\": [0.1171, 0.2904], \"AUROC_ci95\": [0.5179, 0.6387]}, \"EM\": {\"rho\": 0.2945, \"tau\": 0.2208, \"AUROC\": 0.7493, \"ECE\": 0.3526, \"rho_ci95\": [0.2094, 0.37], \"AUROC_ci95\": [0.7002, 0.7928]}, \"voting_conf\": {\"rho\": 0.3792, \"tau\": 0.2805, \"AUROC\": 0.6841, \"ECE\": 0.3807, \"rho_ci95\": [0.2972, 0.4486], \"AUROC_ci95\": [0.6249, 0.7366]}}, \"ner_cond\": {\"n\": 477, \"SJ\": {\"rho\": 0.3113, \"tau\": 0.2257, \"AUROC\": 0.6772, \"ECE\": 0.4416, \"rho_ci95\": [0.2353, 0.3959], \"AUROC_ci95\": [0.621, 0.7337]}, \"FK\": {\"rho\": 0.1761, \"tau\": 0.1284, \"AUROC\": 0.6078, \"ECE\": 0.4389, \"rho_ci95\": [0.0839, 0.2665], \"AUROC_ci95\": [0.5442, 0.6709]}, \"logprob\": {\"rho\": 0.1538, \"tau\": 0.1111, \"AUROC\": 0.5633, \"ECE\": 0.6803, \"rho_ci95\": [0.0637, 0.2424], \"AUROC_ci95\": [0.5032, 0.6232]}, \"EM\": {\"rho\": 0.3596, \"tau\": 0.2735, \"AUROC\": 0.7556, \"ECE\": 0.3257, \"rho_ci95\": [0.2819, 0.4408], \"AUROC_ci95\": [0.7011, 0.8107]}, \"voting_conf\": {\"rho\": 0.3, \"tau\": 0.2189, \"AUROC\": 0.6618, \"ECE\": 0.3746, \"rho_ci95\": [0.2168, 0.3836], \"AUROC_ci95\": [0.6004, 0.7201]}}, \"re_full\": {\"n\": 397, \"SJ\": {\"rho\": 0.2503, \"tau\": 0.1878, \"AUROC\": 0.6702, \"ECE\": 0.3865}, \"FK\": {\"rho\": 0.2752, \"tau\": 0.2117, \"AUROC\": 0.6089, \"ECE\": 0.4405}, \"logprob\": {\"rho\": 0.2662, \"tau\": 0.1951, \"AUROC\": 0.6005, \"ECE\": 0.7694}, \"EM\": {\"rho\": 0.1344, \"tau\": 0.1081, \"AUROC\": 0.7059, \"ECE\": 0.3548}, \"voting_conf\": {\"rho\": 0.3498, \"tau\": 0.2663, \"AUROC\": 0.6935, \"ECE\": 0.2724}}, \"re_cond\": {\"n\": 238, \"SJ\": {\"rho\": 0.2457, \"tau\": 0.1811, \"AUROC\": 0.6463, \"ECE\": 0.2941}, \"FK\": {\"rho\": 0.1139, \"tau\": 0.0876, \"AUROC\": 0.551, \"ECE\": 0.3424}, \"logprob\": {\"rho\": 0.0112, \"tau\": 0.0051, \"AUROC\": 0.5186, \"ECE\": 0.6464}, \"EM\": {\"rho\": 0.4165, \"tau\": 0.3256, \"AUROC\": 0.7515, \"ECE\": 0.2232}, \"voting_conf\": {\"rho\": 0.2409, \"tau\": 0.178, \"AUROC\": 0.642, \"ECE\": 0.207}}, \"delta_vs_512_ner_full_rho\": {\"SJ\": 0.0034, \"FK\": 0.0014, \"EM\": 0.0379, \"voting_conf\": -0.1226, \"logprob\": 0.0656}, \"provenance_note\": \"exp_015_v2 scierc_n8_logprob used exp_012_logprob (max_tokens=512 truncated data). voting_conf was inflated 0.502→0.379, logprob was suppressed 0.140→0.205.\"}, \"hypothesis\": \"Canonical SciERC baseline with max_tokens=1024: Qwen3-8B ft_002_v2, N=8, T=1.0, seed=42, joint NER+RE. Establishes ground-truth ρ rankings and selection F1 for all 5 signals under correct generation length.\"}, \"exp_020_fewnerd_smoke\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T10:29:25.272Z\", \"updated_at\": \"2026-05-16T16:33:59.109Z\", \"hypothesis\": \"1-epoch LoRA (r16) fine-tune Qwen3-8B on Few-NERD INTRA coarse 8-type (131k train), then N=8 T=1.0 pilot inference on 200 test instances. Re-started training 2026-05-16 18:29 CST on cuda:1, PID 288683. ETA ~22:55 CST.\", \"conclusion\": \"success\", \"metrics\": {\"final_loss\": 0.031, \"total_steps\": 8236, \"training_time\": \"5h54m\", \"pilot_greedy_f1\": 0.8037, \"pilot_instances\": 200, \"merged_model_path\": \"checkpoints/qwen3-8b-fewnerd-merged\"}}, \"exp_vc_lp_cascade_selection\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T04:44:02.658Z\", \"updated_at\": \"2026-05-16T06:31:26.755Z\", \"hypothesis\": \"VC-filtered LP selection cascade: test if combining VC (pre-filter) + LP (rank) improves selection F1 over single-signal selection. Addresses SF3 reviewer suggestion. Pure analysis on existing data.\", \"conclusion\": \"killed\"}, \"exp_tacred_re_benchmark\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T04:43:59.002Z\", \"updated_at\": \"2026-05-16T06:31:25.273Z\", \"hypothesis\": \"TACRED RE benchmark: replicate SciERC RE experiment flow on second RE dataset. Verify correlation-selection gap generalizes beyond SciERC. D104 highest priority — addresses R11 MF1 consensus weakness.\", \"conclusion\": \"killed\"}, \"exp_vc_quartile_analysis\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T04:48:35.263Z\", \"updated_at\": \"2026-05-16T05:00:36.736Z\", \"hypothesis\": \"VC quartile stratification: split instances by VC score into Q1-Q4, compute LP selection F1 per quartile. Test if LP selection ability recovers in high-VC instances. Addresses SF3.\", \"conclusion\": \"success\", \"metrics\": {\"scierc_ner\": {\"Q1_lp_delta\": 0.016, \"Q2_lp_delta\": -0.006, \"Q3_lp_delta\": 0.02, \"Q4_lp_delta\": -0.004, \"Q4_mean_vc\": 0.921, \"Q1_headroom\": 0.169, \"Q4_headroom\": 0.048, \"overall_lp_delta\": 0.006, \"n\": 529}, \"scierc_re\": {\"Q1_lp_delta\": -0.036, \"Q2_lp_delta\": -0.021, \"Q3_lp_delta\": -0.022, \"Q4_lp_delta\": 0.04, \"Q4_mean_vc\": 0.894, \"Q1_headroom\": 0.211, \"Q4_headroom\": 0.145, \"overall_lp_delta\": -0.009, \"n\": 397}, \"conll_ner\": {\"Q1_lp_delta\": -0.037, \"Q2_lp_delta\": -0.005, \"Q3_lp_delta\": 0, \"Q4_lp_delta\": 0, \"overall_lp_delta\": -0.01, \"n\": 2756, \"note\": \"Q3/Q4 degenerate (VC=1.0, all samples identical)\"}, \"conclusion\": \"VC stratification does not solve LP compression for NER. RE Q4 is only exception (+0.040).\"}}, \"exp_llama3b_scierc_ablation\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T02:45:23.638Z\", \"updated_at\": \"2026-05-16T03:59:26.005Z\", \"hypothesis\": \"Cross-family scale ablation: LLaMA 3.2-3B on SciERC NER. Verify correlation-selection gap generalizes across model families AND scales. Compare with LLaMA 8B results.\", \"conclusion\": \"success\", \"metrics\": {\"ner_full\": {\"SJ_rho\": 0.3754, \"FK_rho\": 0.2676, \"LP_rho\": 0.2662, \"EM_rho\": 0.3341, \"VC_rho\": 0.4602, \"SJ_auroc\": 0.7383, \"FK_auroc\": 0.6714, \"LP_auroc\": 0.633, \"EM_auroc\": 0.7763, \"VC_auroc\": 0.7429, \"n\": 529}, \"ner_cond\": {\"SJ_rho\": 0.3445, \"FK_rho\": 0.2125, \"LP_rho\": 0.2099, \"EM_rho\": 0.3952, \"VC_rho\": 0.3815, \"SJ_auroc\": 0.7292, \"FK_auroc\": 0.66, \"LP_auroc\": 0.6156, \"EM_auroc\": 0.7822, \"VC_auroc\": 0.7222, \"n\": 476}, \"greedy_f1\": 0.6267, \"oracle_f1\": 0.763, \"oracle_headroom\": 0.1363, \"selection_f1_SJ\": 0.6328, \"selection_f1_VC\": 0.6113, \"selection_f1_FK\": 0.6295, \"selection_f1_EM\": 0.6174, \"selection_f1_LP\": 0.6279, \"n_gold_empty\": 22, \"structural_beats_surface\": true, \"rho_advantage_SJ_over_FK\": 0.1078}}, \"exp_qwen3_4b_conll_scs_inference_v2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T19:41:33.501Z\", \"updated_at\": \"2026-05-16T03:35:13.590Z\", \"hypothesis\": \"CoNLL 4B SCS inference with best checkpoint-4200 (from resume training). Scale ablation: cross-scale evidence for correlation-selection gap. Compare vs v1 (ckpt-3800 baseline: greedy_f1=0.9251, SJ_rho=0.4045).\", \"metrics\": {\"greedy_f1\": 0.9234, \"oracle_f1\": 0.9404, \"oracle_headroom_pp\": 1.7, \"SJ_rho_full\": 0.4217, \"SJ_rho_cond\": 0.459, \"FK_rho_full\": 0.4181, \"FK_rho_cond\": 0.4538, \"LP_rho_full\": 0.3313, \"LP_rho_cond\": 0.3487, \"LP_auroc_full\": 0.7761, \"LP_auroc_cond\": 0.8209, \"n_instances\": 3453, \"verdict\": \"MARGINAL\"}, \"conclusion\": \"success\", \"notes\": \"Gold-filter audit (2026-05-16): CONSISTENT. _full metrics (SJ_rho=0.4217, FK_rho=0.4181) are computed on gold-filtered set (n=2756), same as 8B Table 1 values. _full does NOT mean all 3453 instances — it means gold-nonempty instances. _cond further excludes greedy-F1=0 (n=2641). Confirmed via run_mvp_pilot.py source code and report.json n values.\"}, \"exp_freeform_conll_4seed\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T02:45:17.133Z\", \"updated_at\": \"2026-05-16T03:04:49.550Z\", \"hypothesis\": \"Free-form CoNLL NER 4-seed ablation: verify LP compression is cross-dataset intrinsic (not SciERC-specific). 4 seeds × N=8, T=1.0 on CoNLL, compare LP range distribution with constrained decoding.\", \"conclusion\": \"success\", \"metrics\": {\"greedy_f1\": \"0.9035±0.0004\", \"oracle_f1\": \"0.9460±0.0023\", \"lp_range_median\": \"0.0581±0.0072\", \"rho_sj\": \"0.4606±0.0188\", \"rho_fk\": \"0.4372±0.0209\", \"rho_em\": \"0.4714±0.0168\", \"rho_vc\": \"0.4606±0.0138\", \"rho_lp\": \"0.3262±0.0120\", \"sel_f1_sj\": \"0.8994±0.0014\", \"sel_f1_vc\": \"0.9006±0.0026\", \"sel_f1_lp\": \"0.8958±0.0009\", \"seeds\": [42, 123, 456, 789], \"n_samples\": 8, \"temperature\": 1, \"instances\": 2756, \"gold_empty_filtered\": 697}}, \"exp_qwen3_4b_conll_merge_inference_v2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T19:42:42.107Z\", \"updated_at\": \"2026-05-15T20:07:12.593Z\", \"hypothesis\": \"CoNLL 4B checkpoint-4200 (best from resume training) merge + SCS inference. Replaces v1 which used checkpoint-3800 merged model. Cross-scale evidence for correlation-selection gap.\", \"conclusion\": \"killed\", \"notes\": \"Superseded by exp_qwen3_4b_conll_scs_inference_v2. Output was empty (dead experiment), functionally duplicate.\"}, \"exp_qwen3_4b_scierc_scs_inference\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T19:45:33.384Z\", \"updated_at\": \"2026-05-15T20:06:38.949Z\", \"hypothesis\": \"SciERC 4B SCS inference after v4 finetune merge. Complete 2x2 scale matrix (4B SciERC cell). Cross-scale + cross-task evidence for correlation-selection gap.\", \"metrics\": {\"ner_greedy_f1\": 0.6612, \"ner_oracle_f1\": 0.7839, \"ner_headroom_pp\": 12.28, \"ner_SJ_rho\": 0.4221, \"ner_FK_rho\": 0.3258, \"ner_LP_rho\": 0.28, \"re_greedy_f1\": 0.4136, \"re_oracle_f1\": 0.5846, \"re_headroom_pp\": 17.1, \"re_SJ_rho\": 0.2673, \"re_FK_rho\": 0.3593, \"re_LP_rho\": 0.3512, \"re_sample_f1_pct_zero\": 0.476, \"re_LP_rho_cond\": 0.1135, \"re_LP_rho_cond_p\": 0.074}, \"conclusion\": \"success\"}, \"exp_qwen3_4b_scierc_merge_inference\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T19:42:43.332Z\", \"updated_at\": \"2026-05-15T20:04:15.433Z\", \"hypothesis\": \"SciERC 4B best checkpoint merge + SCS inference. Complete 2x2 scale matrix (4B SciERC cell). Cross-scale + cross-task evidence for correlation-selection gap.\", \"conclusion\": \"killed\", \"notes\": \"Superseded by exp_qwen3_4b_scierc_scs_inference. Never launched (stuck in PREPARING). Killed during registry cleanup.\"}, \"exp_qwen3_4b_scierc_finetune_v3\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T19:24:45.518Z\", \"updated_at\": \"2026-05-15T19:39:04.438Z\", \"conclusion\": \"failed\", \"notes\": \"OOM on cuda:2 — freeform inference (seed789, 8B) 占满 GPU 2。未实际训练。重启为 v4 on cuda:0。\"}, \"exp_qwen3_4b_conll_finetune_resume\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T19:38:19.388Z\", \"updated_at\": \"2026-05-15T19:38:43.468Z\", \"hypothesis\": \"CoNLL 4B NER LoRA fine-tune resume from checkpoint-3800. Cross-scale evidence for correlation-selection gap.\", \"conclusion\": \"success\", \"metrics\": {\"train_loss\": 0.001136, \"eval_loss\": 0.0225, \"best_global_step\": 4200, \"best_metric_eval_loss\": 0.0225, \"total_steps\": 4390, \"epochs\": 5, \"train_runtime_sec\": 1185.8, \"train_samples_per_second\": 59.2, \"resumed_from_step\": 3800}}, \"exp_qwen3_4b_scierc_finetune_v2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T19:03:49.204Z\", \"updated_at\": \"2026-05-15T19:24:32.466Z\", \"conclusion\": \"failed\", \"notes\": \"PID 219830 已死，仅完成 step 10，无 checkpoint。需彻底重启。\"}, \"exp_qwen3_4b_conll_finetune\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T17:18:35.501Z\", \"updated_at\": \"2026-05-15T19:10:24.822Z\", \"hypothesis\": \"Scale ablation: Qwen3-4B CoNLL NER LoRA fine-tune to provide cross-scale evidence (vs 8B). Verify correlation-selection gap, SJ>FK ordering, and LP compression generalize across model scale.\", \"conclusion\": \"success\", \"notes\": \"Training stopped at step 3920/4390 (89.3%, epoch 4.46/5). No error log or tmux session found. checkpoint-3800 is valid (adapter_model.safetensors 264MB, eval_loss=0.023). Proceeding with checkpoint-3800 for merge+inference.\", \"metrics\": {\"final_loss\": 0.0086, \"total_steps_completed\": 3920, \"total_steps_target\": 4390, \"epochs_completed\": 4.46, \"epochs_target\": 5, \"best_checkpoint\": \"checkpoint-3800\", \"note\": \"Training stopped at 89.3% completion (no error log found). Using checkpoint-3800 (loss ~0.01) for merge.\"}}, \"exp_freeform_seed789_v2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T19:02:03.813Z\", \"updated_at\": \"2026-05-15T19:06:44.537Z\", \"conclusion\": \"failed\"}, \"exp_qwen3_4b_scierc_finetune\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T18:58:58.948Z\", \"updated_at\": \"2026-05-15T19:03:05.505Z\", \"conclusion\": \"killed\"}, \"exp_lp_t07_scierc\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T15:34:12.094Z\", \"updated_at\": \"2026-05-15T16:30:35.531Z\", \"conclusion\": \"killed\"}, \"exp_lp_scierc_t07\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T15:34:06.918Z\", \"updated_at\": \"2026-05-15T16:03:13.881Z\", \"hypothesis\": \"LP T=0.7 推理：验证低温下 LP score compression 是否依然存在，强化 \\\"LP compression is model/task intrinsic\\\" claim。对比 T=1.0 的 LP range 分布。\", \"conclusion\": \"success\", \"metrics\": {\"ner_greedy_f1\": 0.662, \"ner_oracle_f1\": 0.764, \"ner_headroom_pp\": 10.2, \"ner_rho_sj_full\": 0.365, \"ner_rho_sj_cond\": 0.363, \"ner_rho_fk_full\": 0.289, \"ner_rho_fk_cond\": 0.255, \"lp_rho_full\": 0.249, \"lp_rho_cond\": 0.185, \"ner_rho_advantage\": 0.076, \"zero_f1_pct\": 11, \"full_n\": 529, \"cond_n\": 477, \"verdict\": \"success_supports_LP_compression_claim\"}}, \"exp_re_scierc_seed456\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T15:40:40.607Z\", \"updated_at\": \"2026-05-15T15:55:41.890Z\", \"hypothesis\": \"SciERC RE 多种子验证 (seed456): 解决 R4-W1/R7-C1 single-seed RE 弱点。与 seed42 (exp_012_rerun_1024) 对齐，joint subtask N=8 T=1.0。目标: 3-seed RE selection F1 mean±σ。\", \"conclusion\": \"negative\", \"metrics\": {\"ner_greedy_f1\": 0.664, \"ner_oracle_f1\": 0.775, \"ner_headroom_pp\": 11.1, \"ner_rho_sj_cond\": 0.283, \"ner_rho_fk_cond\": 0.145, \"re_greedy_f1\": 0.417, \"re_oracle_f1\": 0.581, \"re_headroom_pp\": 16.3, \"re_rho_sj_cond\": 0.315, \"re_rho_fk_cond\": 0.123, \"re_zero_f1_pct\": 45.3, \"verdict\": \"FAIL_re_rho_sj_below_040\"}}, \"exp_re_scierc_seed123\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T15:40:38.271Z\", \"updated_at\": \"2026-05-15T15:55:40.000Z\", \"hypothesis\": \"SciERC RE 多种子验证 (seed123): 解决 R4-W1/R7-C1 single-seed RE 弱点。与 seed42 (exp_012_rerun_1024) 对齐，joint subtask N=8 T=1.0。目标: 3-seed RE selection F1 mean±σ。\", \"conclusion\": \"negative\", \"metrics\": {\"ner_greedy_f1\": 0.663, \"ner_oracle_f1\": 0.786, \"ner_headroom_pp\": 12.3, \"ner_rho_sj_cond\": 0.404, \"ner_rho_fk_cond\": 0.182, \"re_greedy_f1\": 0.42, \"re_oracle_f1\": 0.593, \"re_headroom_pp\": 17.3, \"re_rho_sj_cond\": 0.277, \"re_rho_fk_cond\": 0.063, \"re_zero_f1_pct\": 43.6, \"verdict\": \"FAIL_re_rho_sj_below_040\"}}, \"exp_017_llama_conll_n8_t07\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T15:29:34.595Z\", \"updated_at\": \"2026-05-15T15:46:22.722Z\", \"hypothesis\": \"LLaMA CoNLL N=8 T=0.7 防御性实验：填补\\\"LLaMA 仅在 SciERC 上测过\\\"的弱点，验证 cross-model consistency（vs Qwen CoNLL）。T=0.7 低温下 confidence signals 的 correlation-selection gap 是否依然存在。\", \"parent\": \"exp_017_llama_conll\", \"metrics\": {\"n_valid\": 2756, \"greedy_f1\": 0.9242, \"oracle_f1\": 0.9391, \"lp_range_median\": 1.1e-05, \"lp_tied_fraction_005\": 0.9579, \"signals\": {\"SJ\": {\"rho\": 0.3934, \"auroc\": 0.6506}, \"FK\": {\"rho\": 0.3879, \"auroc\": 0.6488}, \"VC\": {\"rho\": 0.375, \"auroc\": 0.6551}, \"EM\": {\"rho\": 0.3888, \"auroc\": 0.6494}, \"LP\": {\"rho\": 0.2951, \"auroc\": 0.7509}}, \"selection_f1\": {\"SJ\": 0.9247, \"FK\": 0.9254, \"VC\": 0.9264, \"EM\": 0.9255, \"LP\": 0.9248}}, \"conclusion\": \"success\"}, \"exp008_re_n16\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T12:09:50.987Z\", \"updated_at\": \"2026-05-15T12:41:39.774Z\", \"conclusion\": \"killed\"}, \"exp001_seed456\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T12:09:48.078Z\", \"updated_at\": \"2026-05-15T12:41:32.192Z\", \"conclusion\": \"killed\"}, \"exp001_seed123\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T12:09:45.739Z\", \"updated_at\": \"2026-05-15T12:41:31.168Z\", \"conclusion\": \"killed\"}, \"exp_001_n16_seed456_full\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T12:44:31.348Z\", \"updated_at\": \"2026-05-15T12:41:30.065Z\", \"conclusion\": \"killed\"}, \"exp_001_n16_seed123_full\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T12:43:47.915Z\", \"updated_at\": \"2026-05-15T12:41:29.068Z\", \"conclusion\": \"killed\"}, \"exp_007_ner_llama\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T11:42:21.510Z\", \"updated_at\": \"2026-05-15T12:41:27.410Z\", \"conclusion\": \"killed\", \"notes\": \"Completed as exp_007_llama_n16 on autodl-5090. Registry status corrected.\"}, \"exp_002_merge_conll2003\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T12:25:56.211Z\", \"updated_at\": \"2026-05-15T12:41:26.419Z\", \"conclusion\": \"killed\", \"notes\": \"Completed as exp_002_conll_n16 on autodl-5090. Registry status corrected.\"}, \"exp_019_supervised_verifier\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T10:08:54.395Z\", \"updated_at\": \"2026-05-15T12:40:53.995Z\", \"conclusion\": \"killed\", \"notes\": \"Cancelled by Director: DDL risk too high (3-4 days for implementation+training+eval+paper), scope creep for analytical paper, free-form ablation already provides sufficient mechanistic evidence\"}, \"exp_018_llama_scierc_seed456\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T06:07:15.150Z\", \"updated_at\": \"2026-05-15T06:22:40.868Z\", \"conclusion\": \"killed\", \"notes\": \"SUPERSEDED by exp_018_llama_scierc_seed456_r1024 (D066). Original data was re-analysis of exp_007_llama_seed456, not independent inference. Fresh rerun with explicit max_tokens=1024 now canonical.\"}, \"exp_002_conll_n16_r1024\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T22:16:57.682Z\", \"updated_at\": \"2026-05-15T01:20:53.108Z\", \"conclusion\": \"killed\"}, \"exp_007_llama_n16_r1024\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T22:16:59.685Z\", \"updated_at\": \"2026-05-15T01:20:52.194Z\", \"conclusion\": \"killed\"}, \"exp_001_seed123_v2_r1024\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T22:16:54.442Z\", \"updated_at\": \"2026-05-15T01:20:49.812Z\", \"conclusion\": \"killed\"}, \"exp_001_seed456_v2_ner_r1024\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T22:16:55.975Z\", \"updated_at\": \"2026-05-15T01:20:48.914Z\", \"conclusion\": \"killed\"}, \"exp_001_seed42_v2_r1024\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T22:16:52.571Z\", \"updated_at\": \"2026-05-14T22:28:53.686Z\", \"conclusion\": \"killed\", \"metrics\": {\"greedy_f1\": 0.6647, \"oracle_f1\": 0.8106, \"softjaccard_rho_full\": 0.3928, \"fleiss_rho_full\": 0.2489, \"logprob_rho_full\": 0.2136, \"softjaccard_rho_cond\": 0.3455, \"fleiss_rho_cond\": 0.163, \"logprob_rho_cond\": 0.1624, \"verdict\": \"MARGINAL\"}}, \"exp_017_llama_conll_n16_s456\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T19:23:21.987Z\", \"updated_at\": \"2026-05-14T20:24:45.875Z\", \"hypothesis\": \"LLaMA CoNLL N=16 seed=456: structural>surface ranking preserved across seeds, complementing Qwen SciERC 3-seed protocol\", \"metrics\": {\"greedy_f1\": 0.9243, \"oracle_f1\": 0.9488, \"oracle_headroom\": 0.0245, \"n_instances\": 3453, \"n_valid\": 2756, \"n_conditional\": 2642, \"structural_beats_surface\": true, \"full\": {\"SJ_rho\": 0.4552, \"SJ_AUROC\": 0.7288, \"SJ_ECE\": 0.1134, \"FK_rho\": 0.4478, \"FK_AUROC\": 0.7248, \"FK_ECE\": 0.109, \"logprob_rho\": 0.3078, \"logprob_AUROC\": 0.7612, \"logprob_ECE\": 0.1289, \"EM_rho\": 0.452, \"EM_AUROC\": 0.7275, \"EM_ECE\": 0.1082, \"voting_conf_rho\": 0.4571, \"voting_conf_AUROC\": 0.7348, \"voting_conf_ECE\": 0.0863}, \"conditional\": {\"SJ_rho\": 0.4505, \"SJ_AUROC\": 0.7449, \"SJ_ECE\": 0.0826, \"FK_rho\": 0.4422, \"FK_AUROC\": 0.7401, \"FK_ECE\": 0.0835, \"logprob_rho\": 0.3242, \"logprob_AUROC\": 0.8067, \"logprob_ECE\": 0.0921, \"EM_rho\": 0.451, \"EM_AUROC\": 0.745, \"EM_ECE\": 0.0756, \"voting_conf_rho\": 0.3962, \"voting_conf_AUROC\": 0.7202, \"voting_conf_ECE\": 0.0746}, \"best_of_n\": {\"greedy\": 0.9243, \"random_avg\": 0.9215, \"sj_best\": 0.9243, \"logprob_best\": 0.9243, \"voting_conf_best\": 0.9243, \"oracle\": 0.9488}, \"n8_vs_n16_delta\": {\"full_SJ_rho_delta\": 0.0238, \"full_FK_rho_delta\": 0.0201, \"full_logprob_rho_delta\": 0.0006, \"full_EM_rho_delta\": 0.0214, \"full_voting_conf_rho_delta\": 0.0315, \"cond_SJ_rho_delta\": 0.0149, \"cond_FK_rho_delta\": 0.0112, \"cond_logprob_rho_delta\": -0.004, \"cond_EM_rho_delta\": 0.0107, \"cond_voting_conf_rho_delta\": 0.0219}}, \"conclusion\": \"success\"}, \"exp_017_llama_conll_n16_s123\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T19:23:21.084Z\", \"updated_at\": \"2026-05-14T19:43:06.607Z\", \"hypothesis\": \"LLaMA CoNLL N=16 seed=123: structural>surface ranking preserved across seeds, complementing Qwen SciERC 3-seed protocol\", \"metrics\": {\"greedy_f1\": 0.9266, \"oracle_f1\": 0.9497, \"oracle_headroom\": 0.0231, \"n_instances\": 3453, \"n_valid\": 2756, \"n_conditional\": 2642, \"structural_beats_surface\": true, \"full\": {\"SJ_rho\": 0.4698, \"SJ_AUROC\": 0.7402, \"SJ_ECE\": 0.1135, \"FK_rho\": 0.4594, \"FK_AUROC\": 0.7351, \"FK_ECE\": 0.1114, \"logprob_rho\": 0.3161, \"logprob_AUROC\": 0.768, \"logprob_ECE\": 0.129, \"EM_rho\": 0.4676, \"EM_AUROC\": 0.7399, \"EM_ECE\": 0.1082, \"voting_conf_rho\": 0.4612, \"voting_conf_AUROC\": 0.7429, \"voting_conf_ECE\": 0.0832}, \"conditional\": {\"SJ_rho\": 0.4712, \"SJ_AUROC\": 0.7609, \"SJ_ECE\": 0.0828, \"FK_rho\": 0.4595, \"FK_AUROC\": 0.7547, \"FK_ECE\": 0.0858, \"logprob_rho\": 0.3314, \"logprob_AUROC\": 0.8134, \"logprob_ECE\": 0.0922, \"EM_rho\": 0.4732, \"EM_AUROC\": 0.7626, \"EM_ECE\": 0.075, \"voting_conf_rho\": 0.4086, \"voting_conf_AUROC\": 0.7338, \"voting_conf_ECE\": 0.0706}, \"best_of_n\": {\"greedy\": 0.9242, \"random_avg\": 0.9216, \"sj_best\": 0.9247, \"logprob_best\": 0.9253, \"voting_conf_best\": 0.9255, \"oracle\": 0.9486}, \"n8_vs_n16_delta\": {\"full_SJ_rho_delta\": 0.0384, \"full_FK_rho_delta\": 0.0317, \"full_logprob_rho_delta\": 0.0089, \"full_SJ_AUROC_delta\": 0.0363, \"full_FK_AUROC_delta\": 0.0325, \"full_logprob_AUROC_delta\": 0.007, \"cond_SJ_rho_delta\": 0.0356, \"cond_FK_rho_delta\": 0.0285, \"cond_logprob_rho_delta\": 0.0032}}, \"conclusion\": \"success\"}, \"exp_008_re_n16_full\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T12:45:10.852Z\", \"updated_at\": \"2026-05-14T17:51:43.957Z\", \"conclusion\": \"killed\"}, \"exp_017_llama_conll\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T14:39:32.014Z\", \"updated_at\": \"2026-05-14T17:30:26.798Z\", \"conclusion\": \"success\"}, \"exp_001_n16_seed123\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T12:10:29.393Z\", \"updated_at\": \"2026-05-14T12:42:58.393Z\", \"metrics\": {\"ner\": {\"greedy_f1\": 0.655, \"oracle_f1\": 0.8028, \"headroom\": 0.1478, \"rho_sj_full\": 0.4076, \"rho_fk_full\": 0.2799, \"rho_logprob_full\": 0.3189, \"rho_sj_cond\": 0.4271, \"rho_fk_cond\": 0.2743, \"rho_logprob_cond\": 0.2835, \"sj_beats_fk\": true, \"rho_advantage\": 0.1277}, \"re\": {\"greedy_f1\": 0.4243, \"oracle_f1\": 0.6771, \"headroom\": 0.2528, \"rho_sj_full\": 0.2943, \"rho_fk_full\": 0.2657, \"rho_logprob_full\": 0.3005, \"rho_sj_cond\": 0.4003, \"rho_fk_cond\": 0.313, \"rho_logprob_cond\": 0.2317, \"sj_beats_fk\": true, \"rho_advantage\": 0.0286}, \"verdict\": \"FAIL\"}, \"conclusion\": \"success\"}, \"exp_016_signal_ensemble\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T12:15:23.771Z\", \"updated_at\": \"2026-05-14T12:42:55.931Z\", \"conclusion\": \"success\", \"metrics\": {\"sj_logprob_pearson_ner\": 0.57, \"sj_logprob_pearson_re\": 0.42, \"best_linear_ner\": {\"combo\": \"SJ+voting_conf\", \"alpha\": 0.3, \"rho\": 0.489}, \"best_linear_re\": {\"combo\": \"voting_conf+logprob\", \"alpha\": 0.6, \"rho\": 0.429}, \"ensemble_ner_auroc\": 0.735, \"ensemble_re_auroc\": 0.719, \"best_single_ner_auroc\": 0.7, \"best_single_re_auroc\": 0.721, \"ensemble_ner_delta\": 0.035, \"selection_f1_ner\": {\"greedy\": 0.609, \"logprob\": 0.609, \"sj\": 0.604, \"ensemble\": 0.604, \"voting\": 0.596, \"random\": 0.58, \"oracle\": 0.769}, \"selection_f1_re\": {\"logprob\": 0.397, \"greedy\": 0.374, \"sj\": 0.368, \"ensemble\": 0.367, \"voting\": 0.338, \"random\": 0.338, \"oracle\": 0.561}, \"diagnosis\": \"SJ+voting_conf linear combo boosts NER ρ to 0.489 (+23%). RE: logprob-best is ONLY method beating greedy (0.397 vs 0.374). Ensemble AUROC +0.035 on NER. Oracle gap still huge.\"}}, \"exp_001_ner_n16_scierc\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T11:42:10.898Z\", \"updated_at\": \"2026-05-14T12:42:49.592Z\", \"conclusion\": \"success\", \"metrics\": {\"n_instances\": 551, \"ner_n\": 529, \"re_n\": 397, \"N\": 16, \"T\": 1, \"seed\": 42, \"full_test_set\": true, \"ner_voting_conf_rho\": 0.399, \"ner_sj_rho\": 0.398, \"ner_em_rho\": 0.339, \"ner_fk_rho\": 0.288, \"ner_logprob_rho\": 0.237, \"ner_voting_conf_auroc\": 0.704, \"ner_sj_auroc\": 0.697, \"ner_cond_em_rho\": 0.414, \"ner_cond_sj_rho\": 0.349, \"ner_cond_vc_rho\": 0.34, \"re_voting_conf_rho\": 0.38, \"re_logprob_rho\": 0.293, \"re_fk_rho\": 0.281, \"re_sj_rho\": 0.277, \"re_em_rho\": 0.148, \"re_voting_conf_auroc\": 0.699, \"re_cond_em_rho\": 0.475, \"re_cond_sj_rho\": 0.318, \"re_cond_vc_rho\": 0.35, \"re_cond_em_auroc\": 0.742, \"diagnosis\": \"551 instances T=1.0: voting_conf best on full set (NER 0.399, RE 0.380). EM SURPRISE best on conditional set (NER cond 0.414, RE cond 0.475). RE full FAIL (SJ 0.277 < 0.40). Previous N-scaling 'breakthrough' was artifact of 200 instances + T=0.7.\"}}, \"exp_002\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T12:39:53.226Z\", \"updated_at\": \"2026-05-14T12:40:17.202Z\", \"conclusion\": \"success\", \"metrics\": {\"sj_rho_full\": 0.4357, \"sj_tau_full\": 0.3851, \"sj_auroc_full\": 0.8008, \"sj_rho_cond\": 0.4511, \"fk_rho_full\": 0.3998, \"fk_tau_full\": 0.3568, \"fk_auroc_full\": 0.7741, \"fk_rho_cond\": 0.4064, \"logprob_rho_full\": 0.3157, \"logprob_tau_full\": 0.2469, \"logprob_auroc_full\": 0.7532, \"logprob_rho_cond\": 0.3562, \"em_rho_full\": 0.4507, \"em_tau_full\": 0.4002, \"em_auroc_full\": 0.8156, \"em_rho_cond\": 0.4799, \"ev_rho_full\": 0.4237, \"ev_tau_full\": 0.3777, \"ev_auroc_full\": 0.7889, \"ev_rho_cond\": 0.4127, \"greedy_f1\": 0.9123, \"oracle_f1\": 0.9543, \"voting_f1\": 0.9141, \"oracle_headroom\": 0.042, \"sj_vs_logprob_delta_rho\": 0.12, \"sj_vs_logprob_ci_low\": 0.0881, \"sj_vs_logprob_ci_high\": 0.154, \"sj_vs_logprob_significant\": true, \"n_instances\": 3453, \"n_valid\": 2756, \"n_samples\": 8, \"temperature\": 1}}, \"exp_002_ner_conll2003\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T11:42:15.223Z\", \"updated_at\": \"2026-05-14T12:27:35.413Z\", \"conclusion\": \"success\"}, \"exp_004_re_diagnostic\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T11:49:44.497Z\", \"updated_at\": \"2026-05-14T11:50:24.620Z\", \"conclusion\": \"success\", \"metrics\": {\"per_relation_type\": {\"HYPONYM-OF\": {\"n\": 36, \"rho_sj\": 0.545, \"rho_fk\": 0.646, \"rho_vc\": 0.628, \"mean_f1\": 0.513}, \"CONJUNCTION\": {\"n\": 86, \"rho_sj\": 0.383, \"rho_fk\": 0.35, \"rho_vc\": 0.484, \"mean_f1\": 0.48}, \"USED-FOR\": {\"n\": 299, \"rho_sj\": 0.236, \"rho_fk\": 0.255, \"rho_vc\": 0.286, \"mean_f1\": 0.422}, \"PART-OF\": {\"n\": 44, \"rho_sj\": 0.239, \"rho_fk\": 0.348, \"rho_vc\": 0.283, \"mean_f1\": 0.297}, \"EVALUATE-FOR\": {\"n\": 62, \"rho_sj\": 0.172, \"rho_fk\": 0.255, \"rho_vc\": 0.226, \"mean_f1\": 0.365}, \"COMPARE\": {\"n\": 35, \"rho_sj\": 0.168, \"rho_fk\": 0.184, \"rho_vc\": 0.18, \"mean_f1\": 0.453}, \"FEATURE-OF\": {\"n\": 50, \"rho_sj\": 0.004, \"rho_fk\": 0.052, \"rho_vc\": 0.014, \"mean_f1\": 0.254}}, \"error_propagation\": {\"total_fn\": 553, \"tail_error_pct\": 21.9, \"full_error_pct\": 21.7, \"head_error_pct\": 17.7, \"head_tail_error_pct\": 15.9, \"type_error_pct\": 8.3, \"worst_consistency\": \"head_type_error (sj=0.411)\", \"best_consistency\": \"head_error (sj=0.613)\"}, \"threshold_sensitivity\": {\"thr_0.00_rho_sj\": 0.3161, \"thr_0.00_rho_vc\": 0.3841, \"thr_0.00_n\": 313, \"thr_0.05_rho_sj\": 0.2682, \"thr_0.05_rho_vc\": 0.2364, \"thr_0.05_n\": 239}, \"bootstrap_ci_95\": {\"ner_sj\": [0.2946, 0.4586], \"ner_voting_conf\": [0.3048, 0.4656], \"re_sj\": [0.1422, 0.3391], \"re_voting_conf\": [0.1818, 0.3721], \"re_cond_sj\": [0.2161, 0.4102], \"re_cond_voting_conf\": [0.2825, 0.474]}, \"fisher_z_ner_vs_re\": {\"sj_z\": 2.31, \"sj_p\": 0.0209, \"sj_significant\": true, \"fk_z\": -0.31, \"fk_p\": 0.756, \"fk_significant\": false, \"voting_z\": 1.914, \"voting_p\": 0.0556, \"voting_significant\": false}, \"diagnosis\": \"FEATURE-OF is near-zero rho across all signals (n=50, F1=0.254). HYPONYM-OF strongest (rho_fk=0.646). Entity span errors (head+tail) account for 55.5% of RE FN. NER rho_sj significantly > RE rho_sj (p=0.021). Voting_conf is best RE signal in conditional set (rho=0.384).\"}}, \"exp_005\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T11:45:16.360Z\", \"updated_at\": \"2026-05-14T11:45:38.570Z\", \"conclusion\": \"success\"}, \"exp_014_entity_majority_voting\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T10:53:21.203Z\", \"updated_at\": \"2026-05-14T11:33:30.085Z\", \"conclusion\": \"success\", \"metrics\": {\"ner_full_rho\": 0.3915, \"ner_full_p\": 8.1e-21, \"ner_full_tau\": 0.2906, \"ner_full_auroc\": 0.7039, \"re_full_rho\": 0.3403, \"re_full_p\": 3.21e-12, \"re_full_tau\": 0.256, \"re_full_auroc\": 0.6668, \"ner_voting_f1\": 0.6246, \"ner_greedy_f1\": 0.6483, \"ner_oracle_f1\": 0.7793, \"re_voting_f1\": 0.3577, \"re_greedy_f1\": 0.4022, \"re_oracle_f1\": 0.5886, \"diagnosis\": \"Voting confidence BEATS SJ on both NER (rho 0.392 vs 0.383) and RE (0.340 vs 0.244). But voting as selection strategy LOSES to greedy.\"}}, \"exp_013_exact_match_voting\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T10:53:18.753Z\", \"updated_at\": \"2026-05-14T11:33:22.644Z\", \"conclusion\": \"negative\", \"metrics\": {\"ner_full_rho\": 0.2941, \"ner_full_p\": 5.12e-12, \"ner_full_tau\": 0.2181, \"ner_full_auroc\": 0.6398, \"re_full_rho\": 0.1562, \"re_full_p\": 0.0018, \"re_full_tau\": 0.1185, \"re_full_auroc\": 0.5863, \"diagnosis\": \"EM between SJ and FK on NER, weakest on RE. Too coarse-grained.\"}}, \"exp_012_logprob_baseline\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T10:53:16.166Z\", \"updated_at\": \"2026-05-14T11:13:30.240Z\", \"conclusion\": \"success\", \"metrics\": {\"ner_full_rho_sj\": 0.3565, \"ner_full_rho_fk\": 0.2651, \"ner_full_rho_logprob\": 0.1396, \"ner_full_rho_greedy_logprob\": 0.1615, \"ner_full_tau_sj\": 0.2658, \"ner_full_tau_logprob\": 0.1006, \"ner_full_auroc_sj\": 0.6892, \"ner_full_auroc_fk\": 0.6292, \"ner_full_auroc_logprob\": 0.5907, \"ner_full_n\": 529, \"ner_sj_vs_logprob_delta\": 0.2169, \"re_full_rho_sj\": 0.2112, \"re_full_rho_fk\": 0.2528, \"re_full_rho_logprob\": 0.2467, \"re_full_auroc_sj\": 0.5916, \"re_full_auroc_fk\": 0.6262, \"re_full_auroc_logprob\": 0.6186, \"re_full_n\": 397, \"re_cond_rho_sj\": 0.3683, \"re_cond_rho_fk\": 0.3168, \"re_cond_rho_logprob\": 0.1457, \"re_cond_auroc_sj\": 0.6839, \"re_cond_auroc_logprob\": 0.5487, \"re_cond_n\": 296, \"diagnosis\": \"NER: SJ crushes logprob (rho +0.217). RE full: logprob slightly ahead. RE cond: SJ crushes logprob (rho +0.223). SJ unique value CONFIRMED.\"}}, \"mvp_pilot_005\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T09:14:09.456Z\", \"updated_at\": \"2026-05-14T09:47:06.597Z\", \"metrics\": {\"ner_greedy_f1\": 0.6619, \"ner_oracle_f1\": 0.7585, \"ner_headroom\": 0.0966, \"ner_fleiss_kappa_mean\": 0.4722, \"ner_soft_jaccard_mean\": 0.7757, \"ner_full_rho_sj\": 0.3875, \"ner_full_rho_fk\": 0.3211, \"ner_full_n\": 529, \"ner_cond_rho_sj\": 0.3868, \"ner_cond_rho_fk\": 0.305, \"ner_cond_n\": 504, \"ner_sj_beats_fk_full\": true, \"ner_sj_beats_fk_cond\": true, \"ner_rho_advantage\": 0.0664, \"ner_sample_f1_mean\": 0.6243, \"ner_sample_f1_std\": 0.3131, \"ner_sample_f1_pct_zero\": 11.2, \"ner_gold_empty_filtered\": 22, \"ner_all_zero_filtered\": 25, \"re_greedy_f1\": 0.4219, \"re_oracle_f1\": 0.5532, \"re_headroom\": 0.1313, \"re_fleiss_kappa_mean\": 0.3829, \"re_soft_jaccard_mean\": 0.687, \"re_full_rho_sj\": 0.2343, \"re_full_rho_fk\": 0.1835, \"re_full_n\": 397, \"re_cond_rho_sj\": 0.3716, \"re_cond_rho_fk\": 0.2533, \"re_cond_n\": 301, \"re_sj_beats_fk_full\": true, \"re_sj_beats_fk_cond\": true, \"re_rho_advantage\": 0.0508, \"re_sample_f1_mean\": 0.3782, \"re_sample_f1_std\": 0.3845, \"re_sample_f1_pct_zero\": 42.4, \"re_gold_empty_filtered\": 154, \"re_all_zero_filtered\": 96, \"parse_failures\": 0, \"verdict\": \"FAIL\", \"verdict_note\": \"RE full rho_sj=0.234 < 0.40; RE cond rho_sj=0.372 passes conditional but not full threshold\"}, \"conclusion\": \"negative\"}, \"e1_component_wise_re_sj\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T09:15:17.262Z\", \"updated_at\": \"2026-05-14T09:23:38.818Z\", \"conclusion\": \"negative\", \"metrics\": {\"full_head_sj_rho\": 0.21, \"full_tail_sj_rho\": 0.201, \"full_type_match_rho\": 0.201, \"full_multiplicative_rho\": 0.244, \"full_additive_rho\": 0.243, \"full_fleiss_kappa_rho\": 0.278, \"cond_head_sj_rho\": 0.27, \"cond_tail_sj_rho\": 0.259, \"cond_type_match_rho\": 0.252, \"cond_multiplicative_rho\": 0.316, \"cond_additive_rho\": 0.306, \"cond_fleiss_kappa_rho\": 0.307, \"n_full\": 397, \"n_conditional\": 313, \"diagnosis\": \"head_sj rho=0.210 FAR from NER rho=0.383. Multiplicative penalty hypothesis REJECTED. Problem is fundamental: span-level SJ lacks discriminative power for RE.\"}}, \"mvp_pilot_004\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T08:51:38.203Z\", \"updated_at\": \"2026-05-14T09:10:40.918Z\", \"metrics\": {\"ner_greedy_f1\": 0.6671, \"ner_oracle_f1\": 0.7756, \"ner_headroom\": 0.1085, \"ner_fleiss_kappa_mean\": 0.4048, \"ner_soft_jaccard_mean\": 0.7008, \"ner_full_rho_fk\": 0.259, \"ner_full_rho_sj\": 0.3825, \"ner_full_n\": 529, \"ner_cond_rho_fk\": 0.2352, \"ner_cond_rho_sj\": 0.3762, \"ner_cond_n\": 508, \"ner_sj_beats_fk_full\": true, \"ner_sj_beats_fk_cond\": true, \"ner_sample_f1_mean\": 0.6084, \"ner_sample_f1_std\": 0.3174, \"ner_sample_f1_pct_zero\": 12.19, \"ner_gold_empty_filtered\": 22, \"ner_all_zero_filtered\": 21, \"re_greedy_f1\": 0.4208, \"re_oracle_f1\": 0.5882, \"re_headroom\": 0.1674, \"re_fleiss_kappa_mean\": 0.2996, \"re_soft_jaccard_mean\": 0.6114, \"re_full_rho_fk\": 0.2782, \"re_full_rho_sj\": 0.2441, \"re_full_n\": 397, \"re_cond_rho_fk\": 0.3067, \"re_cond_rho_sj\": 0.3161, \"re_cond_n\": 313, \"re_sj_beats_fk_full\": false, \"re_sj_beats_fk_cond\": true, \"re_sample_f1_mean\": 0.3612, \"re_sample_f1_std\": 0.383, \"re_sample_f1_pct_zero\": 44.3, \"re_gold_empty_filtered\": 154, \"re_all_zero_filtered\": 84, \"parse_failures\": 0, \"verdict\": \"FAIL\"}, \"conclusion\": \"negative\"}, \"ft_002_v2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T08:28:40.861Z\", \"updated_at\": \"2026-05-14T08:51:32.405Z\", \"conclusion\": \"success\", \"metrics\": {\"epoch\": 5, \"train_loss\": 0.0806, \"eval_loss\": 0.089, \"train_runtime\": \"28m41s\", \"train_samples_per_second\": 5.407, \"train_steps_per_second\": 0.34, \"total_steps\": 585, \"checkpoints\": [\"checkpoint-400\", \"checkpoint-500\", \"checkpoint-585\"], \"gate0_final_ner_f1\": 0.6615, \"gate0_final_re_f1\": 0.4177, \"gate0_final_parse_failures\": 0, \"gate0_final_ner_pass\": true, \"gate0_final_re_pass\": true, \"gate0_final_pass\": true, \"gate0_ckpt400_ner_f1\": 0.6475, \"gate0_ckpt400_re_f1\": 0.3793, \"gate0_ckpt400_parse_failures\": 0, \"gate0_ckpt400_verdict\": \"FAIL\", \"gate0_ckpt400_re_sample_f1_pct_zero\": 58.8, \"gate0_ckpt400_warning\": \">30% samples F1=0\"}}, \"mvp_pilot_002\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T08:02:16.991Z\", \"updated_at\": \"2026-05-14T08:48:14.040Z\", \"conclusion\": \"failed\"}, \"ft_002\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T07:39:18.640Z\", \"updated_at\": \"2026-05-14T08:28:00.590Z\", \"conclusion\": \"killed\", \"metrics\": {\"last_step\": 70, \"total_steps\": 585, \"progress_pct\": 11.97, \"last_loss\": 0.1134, \"last_lr\": 0.00019982, \"elapsed\": \"3m32s\", \"failure_reason\": \"OOM at step 73, batch_size=4 too large for 32GB RTX 5090\"}}, \"ft_001\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T06:04:28.030Z\", \"updated_at\": \"2026-05-14T08:27:58.182Z\", \"conclusion\": \"success\", \"metrics\": {\"train_loss\": 0.1099, \"eval_loss\": 0.0771, \"gate0_ner_f1_strict\": 0.1143, \"gate0_re_f1_strict\": 0.0125, \"gate0_ner_f1_text\": 0.606, \"gate0_re_f1_text\": 0.3392, \"gate0_offset_accuracy\": 0.1665, \"gate0_parse_failures\": 43, \"gate0_pass\": false, \"gate0_realigned_ner_f1\": 0.6045, \"gate0_realigned_re_f1\": 0.338, \"gate0_realigned_entity_offset_accuracy\": 1, \"gate0_realigned_relation_offset_accuracy\": 1, \"gate0_realigned_ner_pass\": true, \"gate0_realigned_re_pass\": false, \"gate0_realigned_pass\": false, \"gate0_ner_f1_delta_realign\": 0.4901, \"gate0_re_f1_delta_realign\": 0.3255, \"verdict_note\": \"partial: NER PASS (60.4%) / RE FAIL (33.8% < 40%)\"}}, \"mvp_pilot_003\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T08:21:09.847Z\", \"updated_at\": \"2026-05-14T08:21:44.983Z\", \"conclusion\": \"negative\", \"metrics\": {\"ner_greedy_f1\": 0.6362, \"ner_oracle_f1\": 0.792, \"ner_headroom\": 0.1559, \"ner_fleiss_kappa_mean\": 0.2488, \"ner_soft_jaccard_mean\": 0.5066, \"ner_full_rho_sj\": 0.3808, \"ner_full_rho_fk\": 0.3362, \"ner_full_p_sj\": 1.07e-19, \"ner_full_p_fk\": 1.93e-15, \"ner_full_n\": 529, \"ner_cond_rho_sj\": 0.3836, \"ner_cond_rho_fk\": 0.3187, \"ner_cond_p_sj\": 1.83e-19, \"ner_cond_p_fk\": 1.33e-13, \"ner_cond_n\": 514, \"ner_sj_beats_fk_full\": true, \"ner_sj_beats_fk_cond\": true, \"ner_rho_advantage\": 0.0446, \"ner_sample_f1_mean\": 0.5153, \"ner_sample_f1_std\": 0.3334, \"ner_sample_f1_pct_zero\": 19.9, \"ner_gold_empty_filtered\": 22, \"ner_all_zero_filtered\": 15, \"re_greedy_f1\": 0.3774, \"re_oracle_f1\": 0.5939, \"re_headroom\": 0.2165, \"re_fleiss_kappa_mean\": 0.0879, \"re_soft_jaccard_mean\": 0.3958, \"re_full_rho_sj\": 0.2367, \"re_full_rho_fk\": 0.2221, \"re_full_p_sj\": 1.85e-06, \"re_full_p_fk\": 7.92e-06, \"re_full_n\": 397, \"re_cond_rho_sj\": 0.3004, \"re_cond_rho_fk\": 0.2374, \"re_cond_p_sj\": 2.25e-08, \"re_cond_p_fk\": 1.19e-05, \"re_cond_n\": 333, \"re_sj_beats_fk_full\": true, \"re_sj_beats_fk_cond\": true, \"re_rho_advantage\": 0.0146, \"re_sample_f1_mean\": 0.1977, \"re_sample_f1_std\": 0.3251, \"re_sample_f1_pct_zero\": 67.6, \"re_gold_empty_filtered\": 154, \"re_all_zero_filtered\": 64, \"parse_failures_stochastic\": 0, \"parse_failures_greedy\": 0, \"total_stochastic_samples\": 4408, \"total_greedy\": 551, \"verdict\": \"FAIL\", \"verdict_reason\": \"RE full rho_sj=0.2367 < 0.40 threshold; strong signal exists but below PASS bar\"}}, \"mvp_pilot_001\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T07:39:16.313Z\", \"updated_at\": \"2026-05-14T08:05:34.348Z\", \"conclusion\": \"negative\", \"metrics\": {\"ner_greedy_f1\": 0.611, \"ner_oracle_f1\": 0.78, \"ner_headroom\": 0.169, \"ner_fleiss_kappa_mean\": 0.2449, \"ner_soft_jaccard_mean\": 0.5041, \"ner_full_rho_sj\": 0.3616, \"ner_full_rho_fk\": 0.3515, \"ner_full_n\": 529, \"ner_cond_rho_sj\": 0.3688, \"ner_cond_rho_fk\": 0.3569, \"ner_cond_n\": 510, \"ner_sj_beats_fk_full\": true, \"ner_sj_beats_fk_cond\": true, \"ner_sample_f1_pct_zero\": 20.4, \"ner_gold_empty_filtered\": 22, \"ner_all_zero_filtered\": 19, \"re_greedy_f1\": 0.355, \"re_oracle_f1\": 0.572, \"re_headroom\": 0.217, \"re_fleiss_kappa_mean\": 0.0681, \"re_soft_jaccard_mean\": 0.3635, \"re_full_rho_sj\": 0.2535, \"re_full_rho_fk\": 0.2885, \"re_full_n\": 397, \"re_cond_rho_sj\": 0.3515, \"re_cond_rho_fk\": 0.3107, \"re_cond_n\": 320, \"re_sj_beats_fk_full\": false, \"re_sj_beats_fk_cond\": true, \"re_sample_f1_pct_zero\": 58.3, \"re_gold_empty_filtered\": 154, \"re_all_zero_filtered\": 77, \"parse_failures_stochastic\": 164, \"parse_failures_greedy\": 29, \"total_stochastic_samples\": 4408, \"total_greedy\": 551, \"verdict\": \"FAIL\", \"verdict_reason\": \"RE full rho_sj=0.2535 < 0.40; SJ does not beat FK on RE full set\"}}}, \"count\": 125, \"total\": 125, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.3691}}"
    }
  },
  "sourceToolAssistantUUID": "8e727672-ce72-4a09-962c-7747b10fec53",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/agent_b15d88fb",
  "sessionId": "4bea65e8-6043-4140-a3a7-6b0afa4c330b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-17T09:47:55.014Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01TRhXPZjteJqCUa2F1gG2BK`</summary>

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
  "parentUuid": "f50164e7-2c2e-4001-8179-bea7acf0ef3e",
  "isSidechain": false,
  "requestId": "req_011Cb7vtXasbeqztrUd6ujFg",
  "type": "assistant",
  "uuid": "a2430723-d736-467e-b99d-7dcc834733b8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/agent_b15d88fb",
  "sessionId": "4bea65e8-6043-4140-a3a7-6b0afa4c330b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HZaurt2CPwsWFTfyVUgqed",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1157,
      "cache_read_input_tokens": 37482,
      "output_tokens": 284,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1157,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 284,
          "cache_read_input_tokens": 37482,
          "cache_creation_input_tokens": 1157,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1157
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

_source line 17 · 2026-05-17T09:47:55.053Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_roadmap · `toolu_01V9tjSqucDcyeNDsLyiNd74`</summary>

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
  "parentUuid": "a2430723-d736-467e-b99d-7dcc834733b8",
  "isSidechain": false,
  "requestId": "req_011Cb7vtXasbeqztrUd6ujFg",
  "type": "assistant",
  "uuid": "8f4ee16d-97e5-4b29-bda0-9827cb495a84",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/agent_b15d88fb",
  "sessionId": "4bea65e8-6043-4140-a3a7-6b0afa4c330b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HZaurt2CPwsWFTfyVUgqed",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1157,
      "cache_read_input_tokens": 37482,
      "output_tokens": 284,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1157,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 284,
          "cache_read_input_tokens": 37482,
          "cache_creation_input_tokens": 1157,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1157
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

_source line 18_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[CRON] 实验进程已正常退出，状态已转为 ANALYZING，需要你分析结果并推进到 DONE。 详情: Process exited cleanly, W&B data available  - exp_id: exp_026_T05 - project: struct_self_consist_ie - server: autodl-5090 - log_path: ~/runs/stru…",
  "leafUuid": "8f4ee16d-97e5-4b29-bda0-9827cb495a84",
  "sessionId": "4bea65e8-6043-4140-a3a7-6b0afa4c330b"
}
```

---

### Runtime record

_source line 19_

```json
{
  "type": "ai-title",
  "aiTitle": "Analyze experiment results and mark complete",
  "sessionId": "4bea65e8-6043-4140-a3a7-6b0afa4c330b"
}
```

---

### Tool result

_source line 20 · 2026-05-17T09:48:08.563Z_

<details><summary>↩ Tool result · `toolu_017AEidKuitcLqnjg7z29ty4`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"reconciled\": 2, \"results\": [{\"exp_id\": \"exp_026_T08\", \"success\": true, \"actions\": [\"Sentinel EXIT_CODE=0 → Registry → ANALYZING\", \"Cron deleted\"]}, {\"exp_id\": \"exp_026_T12\", \"success\": true, \"actions\": [\"Sentinel EXIT_CODE=0 → Registry → ANALYZING\", \"Cron deleted\"]}]}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4f395dcc-631e-44ff-8816-0a4616c16fe8",
  "isSidechain": false,
  "promptId": "5c07e4b0-2988-437a-a5d7-f32039fe1b2e",
  "type": "user",
  "uuid": "b29ab5c7-723c-4c60-9938-a580e6727672",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"reconciled\\\": 2, \\\"results\\\": [{\\\"exp_id\\\": \\\"exp_026_T08\\\", \\\"success\\\": true, \\\"actions\\\": [\\\"Sentinel EXIT_CODE=0 → Registry → ANALYZING\\\", \\\"Cron deleted\\\"]}, {\\\"exp_id\\\": \\\"exp_026_T12\\\", \\\"success\\\": true, \\\"actions\\\": [\\\"Sentinel EXIT_CODE=0 → Registry → ANALYZING\\\", \\\"Cron deleted\\\"]}]}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"reconciled\": 2, \"results\": [{\"exp_id\": \"exp_026_T08\", \"success\": true, \"actions\": [\"Sentinel EXIT_CODE=0 → Registry → ANALYZING\", \"Cron deleted\"]}, {\"exp_id\": \"exp_026_T12\", \"success\": true, \"actions\": [\"Sentinel EXIT_CODE=0 → Registry → ANALYZING\", \"Cron deleted\"]}]}, \"error\": null, \"metadata\": {}}"
    }
  },
  "sourceToolAssistantUUID": "4f395dcc-631e-44ff-8816-0a4616c16fe8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/agent_b15d88fb",
  "sessionId": "4bea65e8-6043-4140-a3a7-6b0afa4c330b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-17T09:48:08.577Z_

<details><summary>↩ Tool result · `toolu_01TRhXPZjteJqCUa2F1gG2BK`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/report.md\", \"content\": \"&lt;!-- AUTO-FACTS-BEGIN (generated 2026-05-17T09:48:07Z; do not edit — regenerated by auto_build_report_facts) -->\\n## 📊 当前状态（auto-derived from registry）\\n\\n**总计**: 125 个实验 — ANALYZING 3, DONE 120, RUNNING 2\\n**DONE 分布**: failed 4, killed 22, negative 24, success 70\\n\\n### GPU 占用\\n- **分配**: 4 张 — autodl-5090:cuda:0, autodl-5090:cuda:1, autodl-5090:cuda:2, autodl-5090:cuda:3\\n- **实际运行**: 1 张 — autodl-5090:cuda:0(exp_028_fewnerd_5epoch)\\n- **空闲（分配了没跑）**: autodl-5090:cuda:1, autodl-5090:cuda:2, autodl-5090:cuda:3\\n\\n### 💾 磁盘余量\\n- **autodl-5090**:\\n  - `/autodl-pub`: 4.8T/14T 可用（已用 66%）\\n  - `/autodl-pub/data`: 5.7T/10T 可用（已用 44%）\\n  - `/usr/bin/nvidia-smi`: 813G/879G 可用（已用 3%）\\n\\n### 🏃 RUNNING\\n| exp_id | server | gpu | pid | log |\\n|--------|--------|-----|-----|-----|\\n| `exp_028` | autodl-5090 | ? | ? | `…ot/autodl-tmp/struct_self_consist_ie/logs/exp_028_train.log` |\\n| `exp_028_fewnerd_5epoch` | autodl-5090 | cuda:0 | 371545 | `—` |\\n\\n### 📌 最近完成 (top 5)\\n- `exp_027_fewnerd_n16` [success] — 2026-05-17T05:46:48\\n- `exp_016_rerun_1024_bootstrap` [negative] — 2026-05-17T03:33:39\\n- `exp_verbalized_confidence` [negative] — 2026-05-17T03:33:39\\n- `exp_entity_token_lp` [negative] — 2026-05-17T03:33:38\\n- `exp_freeform_ablation` [negative] — 2026-05-17T03:33:37\\n\\n&lt;!-- AUTO-FACTS-END -->\\n\\n---\\n\\n# Handover — 2026-05-17\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\\n|--------|------|------|---------|-----|\\n| exp_028_fewnerd_5epoch | — | — | — | — |\\n| exp_028 | Few-NERD low degeneracy (10%) in exp-021 is NOT due to under-convergence at 3 epochs; training for 5 epochs will show similar degeneracy levels, confirming the structural property of this dataset rather than an artifact of insufficient training. | — | — | — |\\n| exp_026_T12 | T=1.2 will decrease degeneracy rate and expand LP range vs T=1.0, but may degrade generation quality (lower greedy F1). Tests whether reducing degeneracy via higher T recovers selection headroom or if quality degradation offsets the benefit. | — | — | — |\\n\\n## 待处理\\n（无）\\n\\n## 近期结论\\n- **exp_027_fewnerd_n16** (success): LP selection scales with N in low-degeneracy regime: N=16 should yield LP Δ > +2pp (vs N=8 +1.36pp) on Few-NERD (10% degen), because more samples increase oracle headroom while LP ranking remains effective.\\n- **exp_016_rerun_1024_bootstrap** (negative): 3-seed bootstrap significance test for NER logprob vs greedy selection gap (+0.6pp). Tests whether the observed advantage is statistically significant. ← 基于 exp_016_rerun_1024\\n  [fig_selection_gap_1024](/api/workspace-files/projects/struct_self_consist_ie/artifacts/exp_016_rerun_1024_bootstrap/chart/fig_selection_gap_1024.pdf)\\n- **exp_verbalized_confidence** (negative): Verbalized confidence baseline: let model self-rate extraction confidence. If also compressed → strengthens \\\"score compression is general\\\" claim. If effective → important positive finding requiring narrative adjustment. ← 基于 exp_012_rerun_1024\\n  [verbalized_confidence_results](/api/workspace-files/projects/struct_self_consist_ie/artifacts/exp_verbalized_confidence/data/verbalized_confidence_summary.txt)\\n\\n## 趋势\\n成功 70 / 负向 24 / 失败 4 / 共 120\\n\\n## 下一步\\n（无活跃 idea，请通过 ideas.md 添加）\\n\\n## 资源状态\\nautodl-5090: 空闲 cuda:0, cuda:1, cuda:2, cuda:3\\n\\n## 告警\\n- ft_002: 已被终止 — unknown\\n- mvp_pilot_002: 训练失败 — unknown\\n- exp_007_ner_llama: 已被终止 — unknown\\n- exp001_seed123: 已被终止 — unknown\\n- exp001_seed456: 已被终止 — unknown\\n- exp008_re_n16: 已被终止 — unknown\\n- exp_002_merge_conll2003: 已被终止 — unknown\\n- exp_001_n16_seed123_full: 已被终止 — unknown\\n- exp_001_n16_seed456_full: 已被终止 — unknown\\n- exp_008_re_n16_full: 已被终止 — unknown\\n- exp_001_seed42_v2_r1024: 已被终止 — unknown\\n- exp_001_seed123_v2_r1024: 已被终止 — unknown\\n- exp_001_seed456_v2_ner_r1024: 已被终止 — unknown\\n- exp_002_conll_n16_r1024: 已被终止 — unknown\\n- exp_007_llama_n16_r1024: 已被终止 — unknown\\n- exp_018_llama_scierc_seed456: 已被终止 — unknown\\n- exp_019_supervised_verifier: 已被终止 — unknown\\n- exp_lp_t07_scierc: 已被终止 — unknown\\n- exp_qwen3_4b_scierc_finetune: 已被终止 — unknown\\n- exp_freeform_seed789_v2: 训练失败 — unknown\\n- exp_qwen3_4b_scierc_finetune_v2: 训练失败 — unknown\\n- exp_qwen3_4b_scierc_finetune_v3: 训练失败 — unknown\\n- exp_qwen3_4b_conll_merge_inference_v2: 已被终止 — unknown\\n- exp_qwen3_4b_scierc_merge_inference: 已被终止 — unknown\\n- exp_tacred_re_benchmark: 已被终止 — unknown\\n- exp_vc_lp_cascade_selection: 已被终止 — unknown\\n\", \"total_chars\": 4322, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a2430723-d736-467e-b99d-7dcc834733b8",
  "isSidechain": false,
  "promptId": "5c07e4b0-2988-437a-a5d7-f32039fe1b2e",
  "type": "user",
  "uuid": "2f2a742b-7e74-49ca-bc03-fc2e11f4af29",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/report.md\\\", \\\"content\\\": \\\"&lt;!-- AUTO-FACTS-BEGIN (generated 2026-05-17T09:48:07Z; do not edit — regenerated by auto_build_report_facts) -->\\\\n## 📊 当前状态（auto-derived from registry）\\\\n\\\\n**总计**: 125 个实验 — ANALYZING 3, DONE 120, RUNNING 2\\\\n**DONE 分布**: failed 4, killed 22, negative 24, success 70\\\\n\\\\n### GPU 占用\\\\n- **分配**: 4 张 — autodl-5090:cuda:0, autodl-5090:cuda:1, autodl-5090:cuda:2, autodl-5090:cuda:3\\\\n- **实际运行**: 1 张 — autodl-5090:cuda:0(exp_028_fewnerd_5epoch)\\\\n- **空闲（分配了没跑）**: autodl-5090:cuda:1, autodl-5090:cuda:2, autodl-5090:cuda:3\\\\n\\\\n### 💾 磁盘余量\\\\n- **autodl-5090**:\\\\n  - `/autodl-pub`: 4.8T/14T 可用（已用 66%）\\\\n  - `/autodl-pub/data`: 5.7T/10T 可用（已用 44%）\\\\n  - `/usr/bin/nvidia-smi`: 813G/879G 可用（已用 3%）\\\\n\\\\n### 🏃 RUNNING\\\\n| exp_id | server | gpu | pid | log |\\\\n|--------|--------|-----|-----|-----|\\\\n| `exp_028` | autodl-5090 | ? | ? | `…ot/autodl-tmp/struct_self_consist_ie/logs/exp_028_train.log` |\\\\n| `exp_028_fewnerd_5epoch` | autodl-5090 | cuda:0 | 371545 | `—` |\\\\n\\\\n### 📌 最近完成 (top 5)\\\\n- `exp_027_fewnerd_n16` [success] — 2026-05-17T05:46:48\\\\n- `exp_016_rerun_1024_bootstrap` [negative] — 2026-05-17T03:33:39\\\\n- `exp_verbalized_confidence` [negative] — 2026-05-17T03:33:39\\\\n- `exp_entity_token_lp` [negative] — 2026-05-17T03:33:38\\\\n- `exp_freeform_ablation` [negative] — 2026-05-17T03:33:37\\\\n\\\\n&lt;!-- AUTO-FACTS-END -->\\\\n\\\\n---\\\\n\\\\n# Handover — 2026-05-17\\\\n\\\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\\\n\\\\n## 运行中\\\\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\\\\n|--------|------|------|---------|-----|\\\\n| exp_028_fewnerd_5epoch | — | — | — | — |\\\\n| exp_028 | Few-NERD low degeneracy (10%) in exp-021 is NOT due to under-convergence at 3 epochs; training for 5 epochs will show similar degeneracy levels, confirming the structural property of this dataset rather than an artifact of insufficient training. | — | — | — |\\\\n| exp_026_T12 | T=1.2 will decrease degeneracy rate and expand LP range vs T=1.0, but may degrade generation quality (lower greedy F1). Tests whether reducing degeneracy via higher T recovers selection headroom or if quality degradation offsets the benefit. | — | — | — |\\\\n\\\\n## 待处理\\\\n（无）\\\\n\\\\n## 近期结论\\\\n- **exp_027_fewnerd_n16** (success): LP selection scales with N in low-degeneracy regime: N=16 should yield LP Δ > +2pp (vs N=8 +1.36pp) on Few-NERD (10% degen), because more samples increase oracle headroom while LP ranking remains effective.\\\\n- **exp_016_rerun_1024_bootstrap** (negative): 3-seed bootstrap significance test for NER logprob vs greedy selection gap (+0.6pp). Tests whether the observed advantage is statistically significant. ← 基于 exp_016_rerun_1024\\\\n  [fig_selection_gap_1024](/api/workspace-files/projects/struct_self_consist_ie/artifacts/exp_016_rerun_1024_bootstrap/chart/fig_selection_gap_1024.pdf)\\\\n- **exp_verbalized_confidence** (negative): Verbalized confidence baseline: let model self-rate extraction confidence. If also compressed → strengthens \\\\\\\"score compression is general\\\\\\\" claim. If effective → important positive finding requiring narrative adjustment. ← 基于 exp_012_rerun_1024\\\\n  [verbalized_confidence_results](/api/workspace-files/projects/struct_self_consist_ie/artifacts/exp_verbalized_confidence/data/verbalized_confidence_summary.txt)\\\\n\\\\n## 趋势\\\\n成功 70 / 负向 24 / 失败 4 / 共 120\\\\n\\\\n## 下一步\\\\n（无活跃 idea，请通过 ideas.md 添加）\\\\n\\\\n## 资源状态\\\\nautodl-5090: 空闲 cuda:0, cuda:1, cuda:2, cuda:3\\\\n\\\\n## 告警\\\\n- ft_002: 已被终止 — unknown\\\\n- mvp_pilot_002: 训练失败 — unknown\\\\n- exp_007_ner_llama: 已被终止 — unknown\\\\n- exp001_seed123: 已被终止 — unknown\\\\n- exp001_seed456: 已被终止 — unknown\\\\n- exp008_re_n16: 已被终止 — unknown\\\\n- exp_002_merge_conll2003: 已被终止 — unknown\\\\n- exp_001_n16_seed123_full: 已被终止 — unknown\\\\n- exp_001_n16_seed456_full: 已被终止 — unknown\\\\n- exp_008_re_n16_full: 已被终止 — unknown\\\\n- exp_001_seed42_v2_r1024: 已被终止 — unknown\\\\n- exp_001_seed123_v2_r1024: 已被终止 — unknown\\\\n- exp_001_seed456_v2_ner_r1024: 已被终止 — unknown\\\\n- exp_002_conll_n16_r1024: 已被终止 — unknown\\\\n- exp_007_llama_n16_r1024: 已被终止 — unknown\\\\n- exp_018_llama_scierc_seed456: 已被终止 — unknown\\\\n- exp_019_supervised_verifier: 已被终止 — unknown\\\\n- exp_lp_t07_scierc: 已被终止 — unknown\\\\n- exp_qwen3_4b_scierc_finetune: 已被终止 — unknown\\\\n- exp_freeform_seed789_v2: 训练失败 — unknown\\\\n- exp_qwen3_4b_scierc_finetune_v2: 训练失败 — unknown\\\\n- exp_qwen3_4b_scierc_finetune_v3: 训练失败 — unknown\\\\n- exp_qwen3_4b_conll_merge_inference_v2: 已被终止 — unknown\\\\n- exp_qwen3_4b_scierc_merge_inference: 已被终止 — unknown\\\\n- exp_tacred_re_benchmark: 已被终止 — unknown\\\\n- exp_vc_lp_cascade_selection: 已被终止 — unknown\\\\n\\\", \\\"total_chars\\\": 4322, \\\"truncated\\\": false}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/report.md\", \"content\": \"&lt;!-- AUTO-FACTS-BEGIN (generated 2026-05-17T09:48:07Z; do not edit — regenerated by auto_build_report_facts) -->\\n## 📊 当前状态（auto-derived from registry）\\n\\n**总计**: 125 个实验 — ANALYZING 3, DONE 120, RUNNING 2\\n**DONE 分布**: failed 4, killed 22, negative 24, success 70\\n\\n### GPU 占用\\n- **分配**: 4 张 — autodl-5090:cuda:0, autodl-5090:cuda:1, autodl-5090:cuda:2, autodl-5090:cuda:3\\n- **实际运行**: 1 张 — autodl-5090:cuda:0(exp_028_fewnerd_5epoch)\\n- **空闲（分配了没跑）**: autodl-5090:cuda:1, autodl-5090:cuda:2, autodl-5090:cuda:3\\n\\n### 💾 磁盘余量\\n- **autodl-5090**:\\n  - `/autodl-pub`: 4.8T/14T 可用（已用 66%）\\n  - `/autodl-pub/data`: 5.7T/10T 可用（已用 44%）\\n  - `/usr/bin/nvidia-smi`: 813G/879G 可用（已用 3%）\\n\\n### 🏃 RUNNING\\n| exp_id | server | gpu | pid | log |\\n|--------|--------|-----|-----|-----|\\n| `exp_028` | autodl-5090 | ? | ? | `…ot/autodl-tmp/struct_self_consist_ie/logs/exp_028_train.log` |\\n| `exp_028_fewnerd_5epoch` | autodl-5090 | cuda:0 | 371545 | `—` |\\n\\n### 📌 最近完成 (top 5)\\n- `exp_027_fewnerd_n16` [success] — 2026-05-17T05:46:48\\n- `exp_016_rerun_1024_bootstrap` [negative] — 2026-05-17T03:33:39\\n- `exp_verbalized_confidence` [negative] — 2026-05-17T03:33:39\\n- `exp_entity_token_lp` [negative] — 2026-05-17T03:33:38\\n- `exp_freeform_ablation` [negative] — 2026-05-17T03:33:37\\n\\n&lt;!-- AUTO-FACTS-END -->\\n\\n---\\n\\n# Handover — 2026-05-17\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\\n|--------|------|------|---------|-----|\\n| exp_028_fewnerd_5epoch | — | — | — | — |\\n| exp_028 | Few-NERD low degeneracy (10%) in exp-021 is NOT due to under-convergence at 3 epochs; training for 5 epochs will show similar degeneracy levels, confirming the structural property of this dataset rather than an artifact of insufficient training. | — | — | — |\\n| exp_026_T12 | T=1.2 will decrease degeneracy rate and expand LP range vs T=1.0, but may degrade generation quality (lower greedy F1). Tests whether reducing degeneracy via higher T recovers selection headroom or if quality degradation offsets the benefit. | — | — | — |\\n\\n## 待处理\\n（无）\\n\\n## 近期结论\\n- **exp_027_fewnerd_n16** (success): LP selection scales with N in low-degeneracy regime: N=16 should yield LP Δ > +2pp (vs N=8 +1.36pp) on Few-NERD (10% degen), because more samples increase oracle headroom while LP ranking remains effective.\\n- **exp_016_rerun_1024_bootstrap** (negative): 3-seed bootstrap significance test for NER logprob vs greedy selection gap (+0.6pp). Tests whether the observed advantage is statistically significant. ← 基于 exp_016_rerun_1024\\n  [fig_selection_gap_1024](/api/workspace-files/projects/struct_self_consist_ie/artifacts/exp_016_rerun_1024_bootstrap/chart/fig_selection_gap_1024.pdf)\\n- **exp_verbalized_confidence** (negative): Verbalized confidence baseline: let model self-rate extraction confidence. If also compressed → strengthens \\\"score compression is general\\\" claim. If effective → important positive finding requiring narrative adjustment. ← 基于 exp_012_rerun_1024\\n  [verbalized_confidence_results](/api/workspace-files/projects/struct_self_consist_ie/artifacts/exp_verbalized_confidence/data/verbalized_confidence_summary.txt)\\n\\n## 趋势\\n成功 70 / 负向 24 / 失败 4 / 共 120\\n\\n## 下一步\\n（无活跃 idea，请通过 ideas.md 添加）\\n\\n## 资源状态\\nautodl-5090: 空闲 cuda:0, cuda:1, cuda:2, cuda:3\\n\\n## 告警\\n- ft_002: 已被终止 — unknown\\n- mvp_pilot_002: 训练失败 — unknown\\n- exp_007_ner_llama: 已被终止 — unknown\\n- exp001_seed123: 已被终止 — unknown\\n- exp001_seed456: 已被终止 — unknown\\n- exp008_re_n16: 已被终止 — unknown\\n- exp_002_merge_conll2003: 已被终止 — unknown\\n- exp_001_n16_seed123_full: 已被终止 — unknown\\n- exp_001_n16_seed456_full: 已被终止 — unknown\\n- exp_008_re_n16_full: 已被终止 — unknown\\n- exp_001_seed42_v2_r1024: 已被终止 — unknown\\n- exp_001_seed123_v2_r1024: 已被终止 — unknown\\n- exp_001_seed456_v2_ner_r1024: 已被终止 — unknown\\n- exp_002_conll_n16_r1024: 已被终止 — unknown\\n- exp_007_llama_n16_r1024: 已被终止 — unknown\\n- exp_018_llama_scierc_seed456: 已被终止 — unknown\\n- exp_019_supervised_verifier: 已被终止 — unknown\\n- exp_lp_t07_scierc: 已被终止 — unknown\\n- exp_qwen3_4b_scierc_finetune: 已被终止 — unknown\\n- exp_freeform_seed789_v2: 训练失败 — unknown\\n- exp_qwen3_4b_scierc_finetune_v2: 训练失败 — unknown\\n- exp_qwen3_4b_scierc_finetune_v3: 训练失败 — unknown\\n- exp_qwen3_4b_conll_merge_inference_v2: 已被终止 — unknown\\n- exp_qwen3_4b_scierc_merge_inference: 已被终止 — unknown\\n- exp_tacred_re_benchmark: 已被终止 — unknown\\n- exp_vc_lp_cascade_selection: 已被终止 — unknown\\n\", \"total_chars\": 4322, \"truncated\": false}, \"error\": null, \"metadata\": {}}"
    }
  },
  "sourceToolAssistantUUID": "a2430723-d736-467e-b99d-7dcc834733b8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/agent_b15d88fb",
  "sessionId": "4bea65e8-6043-4140-a3a7-6b0afa4c330b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-17T09:48:08.599Z_

<details><summary>↩ Tool result · `toolu_01V9tjSqucDcyeNDsLyiNd74`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/ROADMAP.md\", \"content\": \"# struct_self_consist_ie — Research Dashboard\\n\\n> 最后更新: 2026-05-17 08:56 UTC | 更新原因: D125 Option A confirmed, Byerly closed, tasks updated\\n\\n## 核心方向\\nStructured Self-Consistency for IE: LP selection 需要 TWO jointly necessary conditions — low degeneracy + LP-quality alignment (within-instance ρ(LP,F1) > ~0.3)。详见 paper_framing.md (D123 revised)。\\n\\n## 当前进展\\n- **阶段**: Round 17 修复执行中 → D125 Figure 3 方案确定，等待 Agent 执行 + exp_028 完成\\n- **Round 17 得分**: 3.25 (R1=3.5, R2=3.0)\\n- **已完成**:\\n  - Paper Batch 1-3: em-dash 清零, Abstract/Discussion 压缩, D123 degeneracy 统一, Q3/Q4 整合\\n  - W2 rank=8 分析: LP NOT compressed, differentiator = within-instance ρ(LP,F1)\\n  - Reviewer 确认 D123 整合一致性 PASS\\n  - D124/D125: per-type degeneracy 定义冲突已解决 — Option C 验证 Constant F1 per-type 不显著 (ρ=-0.619, p=0.10)，采纳 Option A 恢复原始定义\\n  - Byerly & Khashabi 引用已确认不存在，关闭\\n- **进行中**:\\n  - exp_028 5-epoch 训练 (ETA ~May 18 05:47 UTC)\\n  - Figure 3 重绘 (D125: per-type 原始值 + dataset-level 47.4/17.8/13.8)\\n  - MLP verifier upgrade (exp-027, CPU-only)\\n  - 引用扫描 (bib 其他可疑条目)\\n  - Registry 清理 (删除 exp_028_fewnerd_5epoch 重复条目)\\n  - Paired degeneracy 更新 (11.1%→14.6%, 4.5%→7.0%)\\n\\n## 近期任务\\n- [x] D123: 统一 degeneracy 定义 + two-condition framework\\n- [x] D124/D125: per-type 定义冲突 → Option A 确定\\n- [x] Byerly & Khashabi 引用关闭\\n- [ ] Figure 3 重绘 + 11-point 全局 ρ 重算 (Agent)\\n- [ ] Paired degeneracy 14.6%→7.0% 写入 experiments.tex\\n- [ ] 论文添加两级 degeneracy 说明（脚注或 Method/Appendix）\\n- [ ] MLP verifier (exp-027) 完成\\n- [ ] 引用扫描完成\\n- [ ] exp_028 完成 → Constant F1 gold-filtered degeneracy + LP selection → Appendix\\n- [ ] 全部修复 → submit_paper_to_review Round 18 (continue mode)\\n- [ ] EMNLP 2026 投稿 (DDL 2026-05-25, 8 days)\\n\\n## GPU 预算\\n4×RTX 5090 (be-a6k-1: cuda:0-3)\\n- cuda:0: exp_028 训练中 (ETA ~May 18 05:47 UTC)\\n- cuda:1-3: 空闲（无 GPU 任务待跑；exp-026 T ablation 可作为候选但非当前优先级）\\n\\n## 关键风险\\n- exp_028: 如果 5-epoch degeneracy >20%, narrative 需微调 (预案已备)\\n- Figure 3 重绘后 11-point 全局 ρ 可能变化（per-type ρ=-0.881 不受影响）\\n- DDL 8 天，时间充裕\\n\\n## Degeneracy 定义约定 (D123+D125)\\n- **Dataset-level** (跨数据集比较): Constant F1 gold-filtered → CoNLL 47.4%, SciERC 17.8%, Few-NERD 13.8%\\n- **Per-type** (within-dataset 统计验证): 原始 type-specific 输出多样性 → ρ=-0.881, p=0.004, n=8\\n- 两者衡量不同层面，互补使用。论文需明确说明。\\n\\n## 关键决策日志\\n\\n| ID | 日期 | 摘要 | 关联实验 |\\n|----|------|------|----------|\\n| D125 | 2026-05-17 | D125: 采纳 Option A——per-type degeneracy 恢复原始定义 (ρ=- | exp_021_fewnerd_full, worker_analysis_option_c |\\n| D124 | 2026-05-17 | D124: Figure 3 per-type degeneracy 定义冲突——先验证 Const | exp_021_fewnerd_full, exp_028 |\\n| D123 | 2026-05-17 | D123: 统一 degeneracy 定义为 Constant F1 gold-filtered; | exp_023, exp_021 |\\n| D122 | 2026-05-17 | D122: exp-027 N=16 confirms LP scales with N in lo | exp_027_fewnerd_n16, exp_021_fewnerd_full |\\n| D121 | 2026-05-16 | D121: 跳过 Dream #3（系统故障），直接提交 Review Director 最终审稿 | — |\\n| D120 | 2026-05-16 | D120: exp-021 Few-NERD Scenario B — LP 显著有效(+1.17p | exp_021_fewnerd_full |\\n| D119 | 2026-05-16 | D119: exp-021 继续执行（pilot verdict=FAIL 但有意识推进）。Few- | exp_020_fewnerd_smoke, exp_021_fewnerd_full |\\n| D118 | 2026-05-16 | D118: N-scaling 统一表使用 subsampled greedy=0.614 作为内部 | exp-025, exp_025_n32 |\\n| D117 | 2026-05-16 | D117: Dream #2 (D116 reframe) did not improve scor | exp-025, exp-026, exp-019 |\\n| D116 | 2026-05-16 | D116: Dream full review 分析 — Best/Worst 3.0, Media | exp_023_lora_rank8, exp_fewnerd_smoke |\\n\\n\\n\", \"lines\": 69}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8f4ee16d-97e5-4b29-bda0-9827cb495a84",
  "isSidechain": false,
  "promptId": "5c07e4b0-2988-437a-a5d7-f32039fe1b2e",
  "type": "user",
  "uuid": "35064344-7b4c-48e4-9640-f335224ebde5",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/ROADMAP.md\\\", \\\"content\\\": \\\"# struct_self_consist_ie — Research Dashboard\\\\n\\\\n> 最后更新: 2026-05-17 08:56 UTC | 更新原因: D125 Option A confirmed, Byerly closed, tasks updated\\\\n\\\\n## 核心方向\\\\nStructured Self-Consistency for IE: LP selection 需要 TWO jointly necessary conditions — low degeneracy + LP-quality alignment (within-instance ρ(LP,F1) > ~0.3)。详见 paper_framing.md (D123 revised)。\\\\n\\\\n## 当前进展\\\\n- **阶段**: Round 17 修复执行中 → D125 Figure 3 方案确定，等待 Agent 执行 + exp_028 完成\\\\n- **Round 17 得分**: 3.25 (R1=3.5, R2=3.0)\\\\n- **已完成**:\\\\n  - Paper Batch 1-3: em-dash 清零, Abstract/Discussion 压缩, D123 degeneracy 统一, Q3/Q4 整合\\\\n  - W2 rank=8 分析: LP NOT compressed, differentiator = within-instance ρ(LP,F1)\\\\n  - Reviewer 确认 D123 整合一致性 PASS\\\\n  - D124/D125: per-type degeneracy 定义冲突已解决 — Option C 验证 Constant F1 per-type 不显著 (ρ=-0.619, p=0.10)，采纳 Option A 恢复原始定义\\\\n  - Byerly & Khashabi 引用已确认不存在，关闭\\\\n- **进行中**:\\\\n  - exp_028 5-epoch 训练 (ETA ~May 18 05:47 UTC)\\\\n  - Figure 3 重绘 (D125: per-type 原始值 + dataset-level 47.4/17.8/13.8)\\\\n  - MLP verifier upgrade (exp-027, CPU-only)\\\\n  - 引用扫描 (bib 其他可疑条目)\\\\n  - Registry 清理 (删除 exp_028_fewnerd_5epoch 重复条目)\\\\n  - Paired degeneracy 更新 (11.1%→14.6%, 4.5%→7.0%)\\\\n\\\\n## 近期任务\\\\n- [x] D123: 统一 degeneracy 定义 + two-condition framework\\\\n- [x] D124/D125: per-type 定义冲突 → Option A 确定\\\\n- [x] Byerly & Khashabi 引用关闭\\\\n- [ ] Figure 3 重绘 + 11-point 全局 ρ 重算 (Agent)\\\\n- [ ] Paired degeneracy 14.6%→7.0% 写入 experiments.tex\\\\n- [ ] 论文添加两级 degeneracy 说明（脚注或 Method/Appendix）\\\\n- [ ] MLP verifier (exp-027) 完成\\\\n- [ ] 引用扫描完成\\\\n- [ ] exp_028 完成 → Constant F1 gold-filtered degeneracy + LP selection → Appendix\\\\n- [ ] 全部修复 → submit_paper_to_review Round 18 (continue mode)\\\\n- [ ] EMNLP 2026 投稿 (DDL 2026-05-25, 8 days)\\\\n\\\\n## GPU 预算\\\\n4×RTX 5090 (be-a6k-1: cuda:0-3)\\\\n- cuda:0: exp_028 训练中 (ETA ~May 18 05:47 UTC)\\\\n- cuda:1-3: 空闲（无 GPU 任务待跑；exp-026 T ablation 可作为候选但非当前优先级）\\\\n\\\\n## 关键风险\\\\n- exp_028: 如果 5-epoch degeneracy >20%, narrative 需微调 (预案已备)\\\\n- Figure 3 重绘后 11-point 全局 ρ 可能变化（per-type ρ=-0.881 不受影响）\\\\n- DDL 8 天，时间充裕\\\\n\\\\n## Degeneracy 定义约定 (D123+D125)\\\\n- **Dataset-level** (跨数据集比较): Constant F1 gold-filtered → CoNLL 47.4%, SciERC 17.8%, Few-NERD 13.8%\\\\n- **Per-type** (within-dataset 统计验证): 原始 type-specific 输出多样性 → ρ=-0.881, p=0.004, n=8\\\\n- 两者衡量不同层面，互补使用。论文需明确说明。\\\\n\\\\n## 关键决策日志\\\\n\\\\n| ID | 日期 | 摘要 | 关联实验 |\\\\n|----|------|------|----------|\\\\n| D125 | 2026-05-17 | D125: 采纳 Option A——per-type degeneracy 恢复原始定义 (ρ=- | exp_021_fewnerd_full, worker_analysis_option_c |\\\\n| D124 | 2026-05-17 | D124: Figure 3 per-type degeneracy 定义冲突——先验证 Const | exp_021_fewnerd_full, exp_028 |\\\\n| D123 | 2026-05-17 | D123: 统一 degeneracy 定义为 Constant F1 gold-filtered; | exp_023, exp_021 |\\\\n| D122 | 2026-05-17 | D122: exp-027 N=16 confirms LP scales with N in lo | exp_027_fewnerd_n16, exp_021_fewnerd_full |\\\\n| D121 | 2026-05-16 | D121: 跳过 Dream #3（系统故障），直接提交 Review Director 最终审稿 | — |\\\\n| D120 | 2026-05-16 | D120: exp-021 Few-NERD Scenario B — LP 显著有效(+1.17p | exp_021_fewnerd_full |\\\\n| D119 | 2026-05-16 | D119: exp-021 继续执行（pilot verdict=FAIL 但有意识推进）。Few- | exp_020_fewnerd_smoke, exp_021_fewnerd_full |\\\\n| D118 | 2026-05-16 | D118: N-scaling 统一表使用 subsampled greedy=0.614 作为内部 | exp-025, exp_025_n32 |\\\\n| D117 | 2026-05-16 | D117: Dream #2 (D116 reframe) did not improve scor | exp-025, exp-026, exp-019 |\\\\n| D116 | 2026-05-16 | D116: Dream full review 分析 — Best/Worst 3.0, Media | exp_023_lora_rank8, exp_fewnerd_smoke |\\\\n\\\\n\\\\n\\\", \\\"lines\\\": 69}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/ROADMAP.md\", \"content\": \"# struct_self_consist_ie — Research Dashboard\\n\\n> 最后更新: 2026-05-17 08:56 UTC | 更新原因: D125 Option A confirmed, Byerly closed, tasks updated\\n\\n## 核心方向\\nStructured Self-Consistency for IE: LP selection 需要 TWO jointly necessary conditions — low degeneracy + LP-quality alignment (within-instance ρ(LP,F1) > ~0.3)。详见 paper_framing.md (D123 revised)。\\n\\n## 当前进展\\n- **阶段**: Round 17 修复执行中 → D125 Figure 3 方案确定，等待 Agent 执行 + exp_028 完成\\n- **Round 17 得分**: 3.25 (R1=3.5, R2=3.0)\\n- **已完成**:\\n  - Paper Batch 1-3: em-dash 清零, Abstract/Discussion 压缩, D123 degeneracy 统一, Q3/Q4 整合\\n  - W2 rank=8 分析: LP NOT compressed, differentiator = within-instance ρ(LP,F1)\\n  - Reviewer 确认 D123 整合一致性 PASS\\n  - D124/D125: per-type degeneracy 定义冲突已解决 — Option C 验证 Constant F1 per-type 不显著 (ρ=-0.619, p=0.10)，采纳 Option A 恢复原始定义\\n  - Byerly & Khashabi 引用已确认不存在，关闭\\n- **进行中**:\\n  - exp_028 5-epoch 训练 (ETA ~May 18 05:47 UTC)\\n  - Figure 3 重绘 (D125: per-type 原始值 + dataset-level 47.4/17.8/13.8)\\n  - MLP verifier upgrade (exp-027, CPU-only)\\n  - 引用扫描 (bib 其他可疑条目)\\n  - Registry 清理 (删除 exp_028_fewnerd_5epoch 重复条目)\\n  - Paired degeneracy 更新 (11.1%→14.6%, 4.5%→7.0%)\\n\\n## 近期任务\\n- [x] D123: 统一 degeneracy 定义 + two-condition framework\\n- [x] D124/D125: per-type 定义冲突 → Option A 确定\\n- [x] Byerly & Khashabi 引用关闭\\n- [ ] Figure 3 重绘 + 11-point 全局 ρ 重算 (Agent)\\n- [ ] Paired degeneracy 14.6%→7.0% 写入 experiments.tex\\n- [ ] 论文添加两级 degeneracy 说明（脚注或 Method/Appendix）\\n- [ ] MLP verifier (exp-027) 完成\\n- [ ] 引用扫描完成\\n- [ ] exp_028 完成 → Constant F1 gold-filtered degeneracy + LP selection → Appendix\\n- [ ] 全部修复 → submit_paper_to_review Round 18 (continue mode)\\n- [ ] EMNLP 2026 投稿 (DDL 2026-05-25, 8 days)\\n\\n## GPU 预算\\n4×RTX 5090 (be-a6k-1: cuda:0-3)\\n- cuda:0: exp_028 训练中 (ETA ~May 18 05:47 UTC)\\n- cuda:1-3: 空闲（无 GPU 任务待跑；exp-026 T ablation 可作为候选但非当前优先级）\\n\\n## 关键风险\\n- exp_028: 如果 5-epoch degeneracy >20%, narrative 需微调 (预案已备)\\n- Figure 3 重绘后 11-point 全局 ρ 可能变化（per-type ρ=-0.881 不受影响）\\n- DDL 8 天，时间充裕\\n\\n## Degeneracy 定义约定 (D123+D125)\\n- **Dataset-level** (跨数据集比较): Constant F1 gold-filtered → CoNLL 47.4%, SciERC 17.8%, Few-NERD 13.8%\\n- **Per-type** (within-dataset 统计验证): 原始 type-specific 输出多样性 → ρ=-0.881, p=0.004, n=8\\n- 两者衡量不同层面，互补使用。论文需明确说明。\\n\\n## 关键决策日志\\n\\n| ID | 日期 | 摘要 | 关联实验 |\\n|----|------|------|----------|\\n| D125 | 2026-05-17 | D125: 采纳 Option A——per-type degeneracy 恢复原始定义 (ρ=- | exp_021_fewnerd_full, worker_analysis_option_c |\\n| D124 | 2026-05-17 | D124: Figure 3 per-type degeneracy 定义冲突——先验证 Const | exp_021_fewnerd_full, exp_028 |\\n| D123 | 2026-05-17 | D123: 统一 degeneracy 定义为 Constant F1 gold-filtered; | exp_023, exp_021 |\\n| D122 | 2026-05-17 | D122: exp-027 N=16 confirms LP scales with N in lo | exp_027_fewnerd_n16, exp_021_fewnerd_full |\\n| D121 | 2026-05-16 | D121: 跳过 Dream #3（系统故障），直接提交 Review Director 最终审稿 | — |\\n| D120 | 2026-05-16 | D120: exp-021 Few-NERD Scenario B — LP 显著有效(+1.17p | exp_021_fewnerd_full |\\n| D119 | 2026-05-16 | D119: exp-021 继续执行（pilot verdict=FAIL 但有意识推进）。Few- | exp_020_fewnerd_smoke, exp_021_fewnerd_full |\\n| D118 | 2026-05-16 | D118: N-scaling 统一表使用 subsampled greedy=0.614 作为内部 | exp-025, exp_025_n32 |\\n| D117 | 2026-05-16 | D117: Dream #2 (D116 reframe) did not improve scor | exp-025, exp-026, exp-019 |\\n| D116 | 2026-05-16 | D116: Dream full review 分析 — Best/Worst 3.0, Media | exp_023_lora_rank8, exp_fewnerd_smoke |\\n\\n\\n\", \"lines\": 69}, \"error\": null, \"metadata\": {}}"
    }
  },
  "sourceToolAssistantUUID": "8f4ee16d-97e5-4b29-bda0-9827cb495a84",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/agent_b15d88fb",
  "sessionId": "4bea65e8-6043-4140-a3a7-6b0afa4c330b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 23_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[CRON] 实验进程已正常退出，状态已转为 ANALYZING，需要你分析结果并推进到 DONE。 详情: Process exited cleanly, W&B data available  - exp_id: exp_026_T05 - project: struct_self_consist_ie - server: autodl-5090 - log_path: ~/runs/stru…",
  "leafUuid": "35064344-7b4c-48e4-9640-f335224ebde5",
  "sessionId": "4bea65e8-6043-4140-a3a7-6b0afa4c330b"
}
```

---

### Runtime record

_source line 24_

```json
{
  "type": "ai-title",
  "aiTitle": "Analyze experiment results and mark complete",
  "sessionId": "4bea65e8-6043-4140-a3a7-6b0afa4c330b"
}
```

---

### Assistant

_source line 25 · 2026-05-17T09:48:22.006Z_

<details><summary>Logged reasoning block</summary>

```text
Let me process what I've learned:

1. **Registry**: Too large, saved to file. I need to query it specifically for exp_026_T05.
2. **Reconcile crons**: Found 2 more experiments that completed - exp_026_T08 and exp_026_T12 also moved to ANALYZING.
3. **Report.md**: Shows current state - 125 experiments, 2 RUNNING (exp_028 and exp_028_fewnerd_5epoch), 3 ANALYZING. 
4. **ROADMAP**: EMNLP 2026 deadline May 25, 8 days away. 

Now I'm shifting focus to the paper work - redrawing Figure 3, waiting for exp_028 to finish, and getting those fixes in. But first I need to pull the details for exp_026_T05, T08, and T12 from the registry and get workers spawned to analyze them.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "35064344-7b4c-48e4-9640-f335224ebde5",
  "isSidechain": false,
  "requestId": "req_011Cb7vuxwPjJFP53ixeutfd",
  "type": "assistant",
  "uuid": "3e95ff15-5e3e-47ca-a83e-a234e90d1550",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/agent_b15d88fb",
  "sessionId": "4bea65e8-6043-4140-a3a7-6b0afa4c330b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LtgkxDEw5dcGxdjrywETmt",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5207,
      "cache_read_input_tokens": 38639,
      "output_tokens": 639,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5207,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 639,
          "cache_read_input_tokens": 38639,
          "cache_creation_input_tokens": 5207,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5207
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

_source line 26 · 2026-05-17T09:48:22.050Z_

Reconcile 发现 exp_026_T08 和 exp_026_T12 也已完成，一共 3 个 T-ablation 实验需要分析。先查这三个实验的详情。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3e95ff15-5e3e-47ca-a83e-a234e90d1550",
  "isSidechain": false,
  "requestId": "req_011Cb7vuxwPjJFP53ixeutfd",
  "type": "assistant",
  "uuid": "edd0e670-779d-4a9a-b4c1-dfd0df492e03",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/agent_b15d88fb",
  "sessionId": "4bea65e8-6043-4140-a3a7-6b0afa4c330b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LtgkxDEw5dcGxdjrywETmt",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5207,
      "cache_read_input_tokens": 38639,
      "output_tokens": 639,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5207,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 639,
          "cache_read_input_tokens": 38639,
          "cache_creation_input_tokens": 5207,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5207
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

_source line 27 · 2026-05-17T09:48:26.307Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01U9BqQBubAD6b8WdHjAVwZr`</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-agent-b15d88fb/4bea65e8-6043-4140-a3a7-6b0afa4c330b/tool-results/mcp-agent-ml-research-read_registry-1779011274694.txt | python3 -c \"\nimport json, sys\ndata = json.loads(json.loads(sys.stdin.read())['result'])\nexps = data['data']['experiments']\ntargets = ['exp_026_T05', 'exp_026_T08', 'exp_026_T12']\nfor e in exps:\n    if e.get('exp_id') in targets:\n        print(json.dumps(e, indent=2))\n        print('---')\n\"",
  "description": "Extract exp_026_T05, T08, T12 from registry dump"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "edd0e670-779d-4a9a-b4c1-dfd0df492e03",
  "isSidechain": false,
  "requestId": "req_011Cb7vuxwPjJFP53ixeutfd",
  "type": "assistant",
  "uuid": "83e4787c-5962-45ef-8969-825b88dae215",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/agent_b15d88fb",
  "sessionId": "4bea65e8-6043-4140-a3a7-6b0afa4c330b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LtgkxDEw5dcGxdjrywETmt",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5207,
      "cache_read_input_tokens": 38639,
      "output_tokens": 639,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5207,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 639,
          "cache_read_input_tokens": 38639,
          "cache_creation_input_tokens": 5207,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5207
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

_source line 28 · 2026-05-17T09:48:27.004Z_

<details><summary>↩ Tool result · reported error · `toolu_01U9BqQBubAD6b8WdHjAVwZr`</summary>

```text
Exit code 1
Traceback (most recent call last):
  File "&lt;string>", line 7, in &lt;module>
    if e.get('exp_id') in targets:
       ^^^^^
AttributeError: 'str' object has no attribute 'get'
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "83e4787c-5962-45ef-8969-825b88dae215",
  "isSidechain": false,
  "promptId": "5c07e4b0-2988-437a-a5d7-f32039fe1b2e",
  "type": "user",
  "uuid": "288af976-2ed2-439a-878c-4bf73ac7f652",
  "toolUseResult": "Error: Exit code 1\nTraceback (most recent call last):\n  File \"&lt;string>\", line 7, in &lt;module>\n    if e.get('exp_id') in targets:\n       ^^^^^\nAttributeError: 'str' object has no attribute 'get'",
  "sourceToolAssistantUUID": "83e4787c-5962-45ef-8969-825b88dae215",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/agent_b15d88fb",
  "sessionId": "4bea65e8-6043-4140-a3a7-6b0afa4c330b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-17T09:48:34.646Z_

<details open><summary>🔧 Tool call — Bash · `toolu_012PmBomQ63JUFm3LySeK9Mg`</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-agent-b15d88fb/4bea65e8-6043-4140-a3a7-6b0afa4c330b/tool-results/mcp-agent-ml-research-read_registry-1779011274694.txt | python3 -c \"\nimport json, sys\nraw = json.loads(sys.stdin.read())\ndata = json.loads(raw['result'])\nexps = data['data']['experiments']\nprint(type(exps), type(exps[0]) if exps else 'empty')\nif isinstance(exps[0], str):\n    # maybe it's exp_id strings, try different structure\n    print(json.dumps(data['data'], default=str)[:500])\nelif isinstance(exps[0], dict):\n    print(list(exps[0].keys())[:10])\n\" 2>&1 | head -20",
  "description": "Probe registry data structure"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "288af976-2ed2-439a-878c-4bf73ac7f652",
  "isSidechain": false,
  "requestId": "req_011Cb7vwKQUCE7vvzZA1YaYn",
  "type": "assistant",
  "uuid": "bdf49bd2-67a0-4026-9977-a01a5e146e63",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/agent_b15d88fb",
  "sessionId": "4bea65e8-6043-4140-a3a7-6b0afa4c330b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YD87H1mJaLwZ6X1wBK6Zeh",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 722,
      "cache_read_input_tokens": 43846,
      "output_tokens": 330,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 722,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 330,
          "cache_read_input_tokens": 43846,
          "cache_creation_input_tokens": 722,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 722
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

_source line 30 · 2026-05-17T09:48:34.836Z_

<details><summary>↩ Tool result · `toolu_012PmBomQ63JUFm3LySeK9Mg`</summary>

```text
Traceback (most recent call last):
  File "&lt;string>", line 6, in &lt;module>
    print(type(exps), type(exps[0]) if exps else 'empty')
                           ~~~~^^^
KeyError: 0
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bdf49bd2-67a0-4026-9977-a01a5e146e63",
  "isSidechain": false,
  "promptId": "5c07e4b0-2988-437a-a5d7-f32039fe1b2e",
  "type": "user",
  "uuid": "5ab219ea-5e0e-40a6-b45d-505c75e7903b",
  "toolUseResult": {
    "stdout": "Traceback (most recent call last):\n  File \"&lt;string>\", line 6, in &lt;module>\n    print(type(exps), type(exps[0]) if exps else 'empty')\n                           ~~~~^^^\nKeyError: 0",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "bdf49bd2-67a0-4026-9977-a01a5e146e63",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/agent_b15d88fb",
  "sessionId": "4bea65e8-6043-4140-a3a7-6b0afa4c330b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-17T09:48:41.412Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01CmS8AXiaV5zwCFtNUzTywW`</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-agent-b15d88fb/4bea65e8-6043-4140-a3a7-6b0afa4c330b/tool-results/mcp-agent-ml-research-read_registry-1779011274694.txt | python3 -c \"\nimport json, sys\nraw = json.loads(sys.stdin.read())\ndata = json.loads(raw['result'])\nexps = data['data']['experiments']\nprint('type:', type(exps))\nif isinstance(exps, dict):\n    keys = list(exps.keys())[:5]\n    print('first keys:', keys)\n    print('sample:', json.dumps(exps[keys[0]], default=str)[:300])\nelif isinstance(exps, list):\n    print('len:', len(exps))\n    print('first:', json.dumps(exps[0], default=str)[:300])\n\" 2>&1",
  "description": "Probe registry experiments structure"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5ab219ea-5e0e-40a6-b45d-505c75e7903b",
  "isSidechain": false,
  "requestId": "req_011Cb7vwtrsxEwewh8xjtmni",
  "type": "assistant",
  "uuid": "60877125-f5c8-4533-a818-920484ebc412",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/agent_b15d88fb",
  "sessionId": "4bea65e8-6043-4140-a3a7-6b0afa4c330b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018sXuDT9kWRf3EF4zn6wZPH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 402,
      "cache_read_input_tokens": 44568,
      "output_tokens": 339,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 402,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 339,
          "cache_read_input_tokens": 44568,
          "cache_creation_input_tokens": 402,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 402
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

_source line 32 · 2026-05-17T09:48:41.537Z_

<details><summary>↩ Tool result · `toolu_01CmS8AXiaV5zwCFtNUzTywW`</summary>

```text
type: &lt;class 'dict'>
first keys: ['exp_026_T05', 'exp_026_T12', 'exp_026_T08', 'exp_028_fewnerd_5epoch', 'exp_028']
sample: {"status": "ANALYZING", "created_at": "2026-05-17T09:38:28.066Z", "updated_at": "2026-05-17T09:47:31.995Z", "hypothesis": "T=0.5 will increase degeneracy rate (more deterministic outputs) and compress LP range on SciERC, reducing selection headroom. Maps the low-temperature end of the degeneracy-tem
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "60877125-f5c8-4533-a818-920484ebc412",
  "isSidechain": false,
  "promptId": "5c07e4b0-2988-437a-a5d7-f32039fe1b2e",
  "type": "user",
  "uuid": "7a1ca746-be74-42e1-ba0e-dd6428c93852",
  "toolUseResult": {
    "stdout": "type: &lt;class 'dict'>\nfirst keys: ['exp_026_T05', 'exp_026_T12', 'exp_026_T08', 'exp_028_fewnerd_5epoch', 'exp_028']\nsample: {\"status\": \"ANALYZING\", \"created_at\": \"2026-05-17T09:38:28.066Z\", \"updated_at\": \"2026-05-17T09:47:31.995Z\", \"hypothesis\": \"T=0.5 will increase degeneracy rate (more deterministic outputs) and compress LP range on SciERC, reducing selection headroom. Maps the low-temperature end of the degeneracy-tem",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "60877125-f5c8-4533-a818-920484ebc412",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/agent_b15d88fb",
  "sessionId": "4bea65e8-6043-4140-a3a7-6b0afa4c330b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 33 · 2026-05-17T09:48:41.543Z_

```json
{
  "parentUuid": "7a1ca746-be74-42e1-ba0e-dd6428c93852",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "15c5ba65-649b-438c-a18d-0b085e559968",
  "timestamp": "2026-05-17T09:48:41.543Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/agent_b15d88fb",
  "sessionId": "4bea65e8-6043-4140-a3a7-6b0afa4c330b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 34 · 2026-05-17T09:48:47.510Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01JuLjzxEsEccLrjXidbk3zF`</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-agent-b15d88fb/4bea65e8-6043-4140-a3a7-6b0afa4c330b/tool-results/mcp-agent-ml-research-read_registry-1779011274694.txt | python3 -c \"\nimport json, sys\nraw = json.loads(sys.stdin.read())\ndata = json.loads(raw['result'])\nexps = data['data']['experiments']\ntargets = ['exp_026_T05', 'exp_026_T08', 'exp_026_T12']\nfor t in targets:\n    if t in exps:\n        print(f'=== {t} ===')\n        print(json.dumps(exps[t], indent=2, default=str))\n        print()\n\" 2>&1",
  "description": "Extract three T-ablation experiments from registry"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "15c5ba65-649b-438c-a18d-0b085e559968",
  "isSidechain": false,
  "requestId": "req_011Cb7vxPY3YDZZMxq3kHP91",
  "type": "assistant",
  "uuid": "07091112-82b5-46a0-ab13-82c85bf07d86",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/agent_b15d88fb",
  "sessionId": "4bea65e8-6043-4140-a3a7-6b0afa4c330b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016VL7kkE2FZeJtvg2ECTapt",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 615,
      "cache_read_input_tokens": 44970,
      "output_tokens": 317,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 615,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 317,
          "cache_read_input_tokens": 44970,
          "cache_creation_input_tokens": 615,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 615
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

_source line 35 · 2026-05-17T09:48:47.602Z_

<details><summary>↩ Tool result · `toolu_01JuLjzxEsEccLrjXidbk3zF`</summary>

```text
=== exp_026_T05 ===
{
  "status": "ANALYZING",
  "created_at": "2026-05-17T09:38:28.066Z",
  "updated_at": "2026-05-17T09:47:31.995Z",
  "hypothesis": "T=0.5 will increase degeneracy rate (more deterministic outputs) and compress LP range on SciERC, reducing selection headroom. Maps the low-temperature end of the degeneracy-temperature frontier, validating that degeneracy is regime-dependent on sampling temperature."
}

=== exp_026_T08 ===
{
  "status": "RUNNING",
  "created_at": "2026-05-17T09:38:29.602Z",
  "updated_at": "2026-05-17T09:41:22.075Z",
  "hypothesis": "T=0.8 will show intermediate degeneracy between T=0.5 and T=1.0, establishing a monotonic degeneracy-temperature relationship. If LP selection improves at T=0.8 vs T=1.0, it identifies the optimal operating point for the selection mechanism."
}

=== exp_026_T12 ===
{
  "status": "RUNNING",
  "created_at": "2026-05-17T09:38:31.060Z",
  "updated_at": "2026-05-17T09:41:40.636Z",
  "hypothesis": "T=1.2 will decrease degeneracy rate and expand LP range vs T=1.0, but may degrade generation quality (lower greedy F1). Tests whether reducing degeneracy via higher T recovers selection headroom or if quality degradation offsets the benefit."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "07091112-82b5-46a0-ab13-82c85bf07d86",
  "isSidechain": false,
  "promptId": "5c07e4b0-2988-437a-a5d7-f32039fe1b2e",
  "type": "user",
  "uuid": "86d2c4cd-0abc-47ec-b813-5241426981c8",
  "toolUseResult": {
    "stdout": "=== exp_026_T05 ===\n{\n  \"status\": \"ANALYZING\",\n  \"created_at\": \"2026-05-17T09:38:28.066Z\",\n  \"updated_at\": \"2026-05-17T09:47:31.995Z\",\n  \"hypothesis\": \"T=0.5 will increase degeneracy rate (more deterministic outputs) and compress LP range on SciERC, reducing selection headroom. Maps the low-temperature end of the degeneracy-temperature frontier, validating that degeneracy is regime-dependent on sampling temperature.\"\n}\n\n=== exp_026_T08 ===\n{\n  \"status\": \"RUNNING\",\n  \"created_at\": \"2026-05-17T09:38:29.602Z\",\n  \"updated_at\": \"2026-05-17T09:41:22.075Z\",\n  \"hypothesis\": \"T=0.8 will show intermediate degeneracy between T=0.5 and T=1.0, establishing a monotonic degeneracy-temperature relationship. If LP selection improves at T=0.8 vs T=1.0, it identifies the optimal operating point for the selection mechanism.\"\n}\n\n=== exp_026_T12 ===\n{\n  \"status\": \"RUNNING\",\n  \"created_at\": \"2026-05-17T09:38:31.060Z\",\n  \"updated_at\": \"2026-05-17T09:41:40.636Z\",\n  \"hypothesis\": \"T=1.2 will decrease degeneracy rate and expand LP range vs T=1.0, but may degrade generation quality (lower greedy F1). Tests whether reducing degeneracy via higher T recovers selection headroom or if quality degradation offsets the benefit.\"\n}",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "07091112-82b5-46a0-ab13-82c85bf07d86",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/agent_b15d88fb",
  "sessionId": "4bea65e8-6043-4140-a3a7-6b0afa4c330b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 36 · 2026-05-17T09:48:55.828Z_

<details><summary>Logged reasoning block</summary>

```text
I see the reconcile already moved exp_026_T08 and exp_026_T12 to ANALYZING, but their status in registry still shows RUNNING. Let me re-read the registry to confirm. Actually, the reconcile results said they were moved to ANALYZING. The registry dump might be from before the reconcile happened. Let me proceed.

Now I need to spawn a Worker to analyze these three T-ablation experiments. The Worker should:
1. SSH to autodl-5090
2. Read the logs for all three experiments
3. Check W&B metrics
4. Summarize results (degeneracy rate, LP range, F1, selection headroom at each temperature)


5. Compare the performance trends across the different temperature settings.

Let me load the spawn_worker tool to get this started.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "86d2c4cd-0abc-47ec-b813-5241426981c8",
  "isSidechain": false,
  "requestId": "req_011Cb7vxqQHyRz86K9wueiN2",
  "type": "assistant",
  "uuid": "fe2aae67-e9fc-4f11-afce-e32732429e67",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/agent_b15d88fb",
  "sessionId": "4bea65e8-6043-4140-a3a7-6b0afa4c330b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UQWsSdKPckZtfUftpaskda",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 752,
      "cache_read_input_tokens": 45585,
      "output_tokens": 365,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 752,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 365,
          "cache_read_input_tokens": 45585,
          "cache_creation_input_tokens": 752,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 752
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

_source line 37 · 2026-05-17T09:48:56.281Z_

三个 T-ablation 实验（T=0.5, T=0.8, T=1.2）全部完成，需要分析。派 Worker 分析结果。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fe2aae67-e9fc-4f11-afce-e32732429e67",
  "isSidechain": false,
  "requestId": "req_011Cb7vxqQHyRz86K9wueiN2",
  "type": "assistant",
  "uuid": "1c900754-41ba-45db-a637-b062186cf8e5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/agent_b15d88fb",
  "sessionId": "4bea65e8-6043-4140-a3a7-6b0afa4c330b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UQWsSdKPckZtfUftpaskda",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 752,
      "cache_read_input_tokens": 45585,
      "output_tokens": 365,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 752,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 365,
          "cache_read_input_tokens": 45585,
          "cache_creation_input_tokens": 752,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 752
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

_source line 38 · 2026-05-17T09:48:57.505Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01Ddg5pHtm4ne9UvBWA5d3vC`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__spawn_worker,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__fetch_wandb_metrics",
  "max_results": 3
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1c900754-41ba-45db-a637-b062186cf8e5",
  "isSidechain": false,
  "requestId": "req_011Cb7vxqQHyRz86K9wueiN2",
  "type": "assistant",
  "uuid": "46890de5-6663-4667-bd6d-0f227fa75688",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/agent_b15d88fb",
  "sessionId": "4bea65e8-6043-4140-a3a7-6b0afa4c330b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UQWsSdKPckZtfUftpaskda",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 752,
      "cache_read_input_tokens": 45585,
      "output_tokens": 365,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 752,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 365,
          "cache_read_input_tokens": 45585,
          "cache_creation_input_tokens": 752,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 752
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

_source line 39 · 2026-05-17T09:48:57.508Z_

<details><summary>↩ Tool result · `toolu_01Ddg5pHtm4ne9UvBWA5d3vC`</summary>

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
  "tool_name": "mcp__agent-ml-research__fetch_wandb_metrics"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "46890de5-6663-4667-bd6d-0f227fa75688",
  "isSidechain": false,
  "promptId": "5c07e4b0-2988-437a-a5d7-f32039fe1b2e",
  "type": "user",
  "uuid": "b88c0265-0b0f-4dd3-a89d-0c87b86d71c3",
  "toolUseResult": {
    "matches": [
      "mcp__agent-ml-research__spawn_worker",
      "mcp__agent-ml-research__update_registry",
      "mcp__agent-ml-research__fetch_wandb_metrics"
    ],
    "query": "select:mcp__agent-ml-research__spawn_worker,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__fetch_wandb_metrics",
    "total_deferred_tools": 80
  },
  "sourceToolAssistantUUID": "46890de5-6663-4667-bd6d-0f227fa75688",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/agent_b15d88fb",
  "sessionId": "4bea65e8-6043-4140-a3a7-6b0afa4c330b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 40 · 2026-05-17T09:49:06.867Z_

<details><summary>Logged reasoning block</summary>

```text
Now I'll spawn a Worker to analyze the three T-ablation experiments. The Worker needs to:
1. SSH to autodl-5090 and read logs for exp_026_T05, exp_026_T08, exp_026_T12
2. Check W&B data
3. Extract key metrics: degeneracy rate, LP range, F1 (greedy and selection), selection gap
4. Compare across temperatures (T=0.5, 0.8, 1.0, 1.2)
5. Produce a summary table

I need to give the Worker context about what these experiments are testing and what the parent experiment (exp_026 at T=1.0) showed.


I should also pull the baseline data from exp_026 itself to have the T=1.0 reference point for comparison.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b88c0265-0b0f-4dd3-a89d-0c87b86d71c3",
  "isSidechain": false,
  "requestId": "req_011Cb7vyZwtcCgsyUMnV7Y69",
  "type": "assistant",
  "uuid": "77663245-b6d5-4c55-b10a-26b9efccba63",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/agent_b15d88fb",
  "sessionId": "4bea65e8-6043-4140-a3a7-6b0afa4c330b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011hj6eCoizUFoX7nAix7sBt",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2347,
      "cache_read_input_tokens": 46337,
      "output_tokens": 692,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2347,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 692,
          "cache_read_input_tokens": 46337,
          "cache_creation_input_tokens": 2347,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2347
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

_source line 41 · 2026-05-17T09:49:10.070Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01J7ntbMXdHRR1EBpUbE7DB9`</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-agent-b15d88fb/4bea65e8-6043-4140-a3a7-6b0afa4c330b/tool-results/mcp-agent-ml-research-read_registry-1779011274694.txt | python3 -c \"\nimport json, sys\nraw = json.loads(sys.stdin.read())\ndata = json.loads(raw['result'])\nexps = data['data']['experiments']\n# Find exp_026 (T=1.0 baseline) and any T-ablation related\nfor k in sorted(exps.keys()):\n    if 'exp_026' in k or 'T_ablation' in k or 'temp' in k.lower():\n        e = exps[k]\n        print(f'=== {k} ===')\n        print(f'  status: {e.get(\\\"status\\\")}')\n        print(f'  conclusion: {e.get(\\\"conclusion\\\")}')\n        print(f'  metrics: {json.dumps(e.get(\\\"metrics\\\"), default=str)[:500]}')\n        print(f'  hypothesis: {e.get(\\\"hypothesis\\\", \\\"\\\")[:200]}')\n        print(f'  parent: {e.get(\\\"parent\\\")}')\n        print(f'  spec: {json.dumps(e.get(\\\"spec\\\"), default=str)[:300]}')\n        print()\n\" 2>&1",
  "description": "Find exp_026 baseline and all T-ablation experiments"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "77663245-b6d5-4c55-b10a-26b9efccba63",
  "isSidechain": false,
  "requestId": "req_011Cb7vyZwtcCgsyUMnV7Y69",
  "type": "assistant",
  "uuid": "cf9e56cd-481c-44b1-a09e-f7f5b082ee17",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/agent_b15d88fb",
  "sessionId": "4bea65e8-6043-4140-a3a7-6b0afa4c330b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011hj6eCoizUFoX7nAix7sBt",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2347,
      "cache_read_input_tokens": 46337,
      "output_tokens": 692,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2347,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 692,
          "cache_read_input_tokens": 46337,
          "cache_creation_input_tokens": 2347,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2347
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

_source line 42 · 2026-05-17T09:49:10.180Z_

<details><summary>↩ Tool result · `toolu_01J7ntbMXdHRR1EBpUbE7DB9`</summary>

```text
=== exp_026_T05 ===
  status: ANALYZING
  conclusion: None
  metrics: null
  hypothesis: T=0.5 will increase degeneracy rate (more deterministic outputs) and compress LP range on SciERC, reducing selection headroom. Maps the low-temperature end of the degeneracy-temperature frontier, vali
  parent: None
  spec: null

=== exp_026_T08 ===
  status: RUNNING
  conclusion: None
  metrics: null
  hypothesis: T=0.8 will show intermediate degeneracy between T=0.5 and T=1.0, establishing a monotonic degeneracy-temperature relationship. If LP selection improves at T=0.8 vs T=1.0, it identifies the optimal ope
  parent: None
  spec: null

=== exp_026_T12 ===
  status: RUNNING
  conclusion: None
  metrics: null
  hypothesis: T=1.2 will decrease degeneracy rate and expand LP range vs T=1.0, but may degrade generation quality (lower greedy F1). Tests whether reducing degeneracy via higher T recovers selection headroom or if
  parent: None
  spec: null

=== exp_026_t05 ===
  status: DONE
  conclusion: success
  metrics: {"temperature": 0.5, "task": "T-ablation"}
  hypothesis: Temperature T=0.5 ablation on SciERC: extreme low temperature expected to maximally compress LP scores and increase degeneracy, providing upper-bound evidence for LP compression as model-intrinsic phe
  parent: exp_012_rerun_1024
  spec: null

=== exp_026_t08 ===
  status: DONE
  conclusion: success
  metrics: {"temperature": 0.8, "task": "T-ablation"}
  hypothesis: Temperature T=0.8 ablation on SciERC: test if lower temperature increases LP compression (narrower range) while structural signals remain robust, supporting the claim that LP compression is intrinsic 
  parent: exp_012_rerun_1024
  spec: null

=== exp_026_t12 ===
  status: DONE
  conclusion: success
  metrics: {"temperature": 1.2, "task": "T-ablation"}
  hypothesis: Temperature T=1.2 ablation on SciERC: test if higher temperature increases sample diversity (lower degeneracy) and LP discriminative range, potentially improving LP selection while maintaining structu
  parent: exp_012_rerun_1024
  spec: null
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cf9e56cd-481c-44b1-a09e-f7f5b082ee17",
  "isSidechain": false,
  "promptId": "5c07e4b0-2988-437a-a5d7-f32039fe1b2e",
  "type": "user",
  "uuid": "bc7d3f89-41ad-4ae7-b17c-eb7d831e0059",
  "toolUseResult": {
    "stdout": "=== exp_026_T05 ===\n  status: ANALYZING\n  conclusion: None\n  metrics: null\n  hypothesis: T=0.5 will increase degeneracy rate (more deterministic outputs) and compress LP range on SciERC, reducing selection headroom. Maps the low-temperature end of the degeneracy-temperature frontier, vali\n  parent: None\n  spec: null\n\n=== exp_026_T08 ===\n  status: RUNNING\n  conclusion: None\n  metrics: null\n  hypothesis: T=0.8 will show intermediate degeneracy between T=0.5 and T=1.0, establishing a monotonic degeneracy-temperature relationship. If LP selection improves at T=0.8 vs T=1.0, it identifies the optimal ope\n  parent: None\n  spec: null\n\n=== exp_026_T12 ===\n  status: RUNNING\n  conclusion: None\n  metrics: null\n  hypothesis: T=1.2 will decrease degeneracy rate and expand LP range vs T=1.0, but may degrade generation quality (lower greedy F1). Tests whether reducing degeneracy via higher T recovers selection headroom or if\n  parent: None\n  spec: null\n\n=== exp_026_t05 ===\n  status: DONE\n  conclusion: success\n  metrics: {\"temperature\": 0.5, \"task\": \"T-ablation\"}\n  hypothesis: Temperature T=0.5 ablation on SciERC: extreme low temperature expected to maximally compress LP scores and increase degeneracy, providing upper-bound evidence for LP compression as model-intrinsic phe\n  parent: exp_012_rerun_1024\n  spec: null\n\n=== exp_026_t08 ===\n  status: DONE\n  conclusion: success\n  metrics: {\"temperature\": 0.8, \"task\": \"T-ablation\"}\n  hypothesis: Temperature T=0.8 ablation on SciERC: test if lower temperature increases LP compression (narrower range) while structural signals remain robust, supporting the claim that LP compression is intrinsic \n  parent: exp_012_rerun_1024\n  spec: null\n\n=== exp_026_t12 ===\n  status: DONE\n  conclusion: success\n  metrics: {\"temperature\": 1.2, \"task\": \"T-ablation\"}\n  hypothesis: Temperature T=1.2 ablation on SciERC: test if higher temperature increases sample diversity (lower degeneracy) and LP discriminative range, potentially improving LP selection while maintaining structu\n  parent: exp_012_rerun_1024\n  spec: null",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "cf9e56cd-481c-44b1-a09e-f7f5b082ee17",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/agent_b15d88fb",
  "sessionId": "4bea65e8-6043-4140-a3a7-6b0afa4c330b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 43_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[CRON] 实验进程已正常退出，状态已转为 ANALYZING，需要你分析结果并推进到 DONE。 详情: Process exited cleanly, W&B data available  - exp_id: exp_026_T05 - project: struct_self_consist_ie - server: autodl-5090 - log_path: ~/runs/stru…",
  "leafUuid": "bc7d3f89-41ad-4ae7-b17c-eb7d831e0059",
  "sessionId": "4bea65e8-6043-4140-a3a7-6b0afa4c330b"
}
```

---

### Runtime record

_source line 44_

```json
{
  "type": "ai-title",
  "aiTitle": "Analyze experiment results and mark complete",
  "sessionId": "4bea65e8-6043-4140-a3a7-6b0afa4c330b"
}
```

---

### Assistant

_source line 45 · 2026-05-17T09:49:18.833Z_

<details><summary>Logged reasoning block</summary>

```text
Interesting! There are already completed versions of these experiments (exp_026_t05, exp_026_t08, exp_026_t12 - lowercase t) with conclusion=success. And now there are new versions (exp_026_T05, exp_026_T08, exp_026_T12 - uppercase T) in ANALYZING state.

The lowercase versions have metrics but just `{"temperature": 0.5, "task": "T-ablation"}` etc. Let me check if these have more detailed metrics or if the new uppercase versions are re-runs.

Let me get the full details of the existing done versions and then look at the log paths for the new ones.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bc7d3f89-41ad-4ae7-b17c-eb7d831e0059",
  "isSidechain": false,
  "requestId": "req_011Cb7vzW12ygKnKDSivHVGM",
  "type": "assistant",
  "uuid": "28957a3e-9ca9-4936-87f4-5c572107445e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/agent_b15d88fb",
  "sessionId": "4bea65e8-6043-4140-a3a7-6b0afa4c330b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q83gtb2S825U1WQKeJf9KQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1325,
      "cache_read_input_tokens": 48684,
      "output_tokens": 486,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1325,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 486,
          "cache_read_input_tokens": 48684,
          "cache_creation_input_tokens": 1325,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1325
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

_source line 46 · 2026-05-17T09:49:21.055Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01NnnFoHGiAQpYcf4o994RsR`</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-agent-b15d88fb/4bea65e8-6043-4140-a3a7-6b0afa4c330b/tool-results/mcp-agent-ml-research-read_registry-1779011274694.txt | python3 -c \"\nimport json, sys\nraw = json.loads(sys.stdin.read())\ndata = json.loads(raw['result'])\nexps = data['data']['experiments']\n# Get full details of lowercase versions\nfor k in ['exp_026_t05', 'exp_026_t08', 'exp_026_t12']:\n    e = exps[k]\n    print(f'=== {k} ===')\n    print(json.dumps(e, indent=2, default=str))\n    print()\n\" 2>&1",
  "description": "Get full details of completed T-ablation experiments"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "28957a3e-9ca9-4936-87f4-5c572107445e",
  "isSidechain": false,
  "requestId": "req_011Cb7vzW12ygKnKDSivHVGM",
  "type": "assistant",
  "uuid": "12594285-6c86-4f42-b022-73c4d5cac3cf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/agent_b15d88fb",
  "sessionId": "4bea65e8-6043-4140-a3a7-6b0afa4c330b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q83gtb2S825U1WQKeJf9KQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1325,
      "cache_read_input_tokens": 48684,
      "output_tokens": 486,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1325,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 486,
          "cache_read_input_tokens": 48684,
          "cache_creation_input_tokens": 1325,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1325
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

_source line 47 · 2026-05-17T09:49:21.145Z_

<details><summary>↩ Tool result · `toolu_01NnnFoHGiAQpYcf4o994RsR`</summary>

```text
=== exp_026_t05 ===
{
  "status": "DONE",
  "created_at": "2026-05-16T12:19:35.753Z",
  "updated_at": "2026-05-17T02:55:48.900Z",
  "conclusion": "success",
  "metrics": {
    "temperature": 0.5,
    "task": "T-ablation"
  },
  "hypothesis": "Temperature T=0.5 ablation on SciERC: extreme low temperature expected to maximally compress LP scores and increase degeneracy, providing upper-bound evidence for LP compression as model-intrinsic phenomenon.",
  "parent": "exp_012_rerun_1024"
}

=== exp_026_t08 ===
{
  "status": "DONE",
  "created_at": "2026-05-16T12:57:46.027Z",
  "updated_at": "2026-05-17T02:55:47.964Z",
  "conclusion": "success",
  "metrics": {
    "temperature": 0.8,
    "task": "T-ablation"
  },
  "hypothesis": "Temperature T=0.8 ablation on SciERC: test if lower temperature increases LP compression (narrower range) while structural signals remain robust, supporting the claim that LP compression is intrinsic rather than temperature-driven.",
  "parent": "exp_012_rerun_1024"
}

=== exp_026_t12 ===
{
  "status": "DONE",
  "created_at": "2026-05-16T13:18:18.780Z",
  "updated_at": "2026-05-17T02:55:46.995Z",
  "conclusion": "success",
  "metrics": {
    "temperature": 1.2,
    "task": "T-ablation"
  },
  "hypothesis": "Temperature T=1.2 ablation on SciERC: test if higher temperature increases sample diversity (lower degeneracy) and LP discriminative range, potentially improving LP selection while maintaining structural signal effectiveness.",
  "parent": "exp_012_rerun_1024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "12594285-6c86-4f42-b022-73c4d5cac3cf",
  "isSidechain": false,
  "promptId": "5c07e4b0-2988-437a-a5d7-f32039fe1b2e",
  "type": "user",
  "uuid": "0cafa832-960d-4b2c-9134-da4d358063bb",
  "toolUseResult": {
    "stdout": "=== exp_026_t05 ===\n{\n  \"status\": \"DONE\",\n  \"created_at\": \"2026-05-16T12:19:35.753Z\",\n  \"updated_at\": \"2026-05-17T02:55:48.900Z\",\n  \"conclusion\": \"success\",\n  \"metrics\": {\n    \"temperature\": 0.5,\n    \"task\": \"T-ablation\"\n  },\n  \"hypothesis\": \"Temperature T=0.5 ablation on SciERC: extreme low temperature expected to maximally compress LP scores and increase degeneracy, providing upper-bound evidence for LP compression as model-intrinsic phenomenon.\",\n  \"parent\": \"exp_012_rerun_1024\"\n}\n\n=== exp_026_t08 ===\n{\n  \"status\": \"DONE\",\n  \"created_at\": \"2026-05-16T12:57:46.027Z\",\n  \"updated_at\": \"2026-05-17T02:55:47.964Z\",\n  \"conclusion\": \"success\",\n  \"metrics\": {\n    \"temperature\": 0.8,\n    \"task\": \"T-ablation\"\n  },\n  \"hypothesis\": \"Temperature T=0.8 ablation on SciERC: test if lower temperature increases LP compression (narrower range) while structural signals remain robust, supporting the claim that LP compression is intrinsic rather than temperature-driven.\",\n  \"parent\": \"exp_012_rerun_1024\"\n}\n\n=== exp_026_t12 ===\n{\n  \"status\": \"DONE\",\n  \"created_at\": \"2026-05-16T13:18:18.780Z\",\n  \"updated_at\": \"2026-05-17T02:55:46.995Z\",\n  \"conclusion\": \"success\",\n  \"metrics\": {\n    \"temperature\": 1.2,\n    \"task\": \"T-ablation\"\n  },\n  \"hypothesis\": \"Temperature T=1.2 ablation on SciERC: test if higher temperature increases sample diversity (lower degeneracy) and LP discriminative range, potentially improving LP selection while maintaining structural signal effectiveness.\",\n  \"parent\": \"exp_012_rerun_1024\"\n}",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "12594285-6c86-4f42-b022-73c4d5cac3cf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/agent_b15d88fb",
  "sessionId": "4bea65e8-6043-4140-a3a7-6b0afa4c330b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 48 · 2026-05-17T09:49:28.850Z_

<details><summary>Logged reasoning block</summary>

```text
The lowercase versions (exp_026_t05, exp_026_t08, exp_026_t12) were already completed and marked as success. But now there are NEW uppercase versions (exp_026_T05, exp_026_T08, exp_026_T12) that are in ANALYZING state. These are likely re-runs with different parameters or a newer setup.

I need to spawn a Worker to:
1. SSH to autodl-5090 and read the logs for the new experiments
2. Check W&B for metrics
3. Extract the key metrics and produce a comparison table

Let me also check what the log paths are. The cron callback said log_path is `~/runs/struct_self_consist_ie/exp_026_T05.log`. 

I'll assume the same pattern holds for T08 and T12, then spawn a worker to pull the logs and metrics from W&B for analysis.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0cafa832-960d-4b2c-9134-da4d358063bb",
  "isSidechain": false,
  "requestId": "req_011Cb7w1Js6FPUudnwr38nbV",
  "type": "assistant",
  "uuid": "5372d33b-9aa0-41c1-9ed1-67ca0a0c58ae",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/agent_b15d88fb",
  "sessionId": "4bea65e8-6043-4140-a3a7-6b0afa4c330b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013Cewpk4FwkVFxqxAxx3L77",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1034,
      "cache_read_input_tokens": 50009,
      "output_tokens": 1512,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1034,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1512,
          "cache_read_input_tokens": 50009,
          "cache_creation_input_tokens": 1034,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1034
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

_source line 49 · 2026-05-17T09:49:28.964Z_

存在旧版（lowercase）已完成，新版（uppercase）是 re-run。派 Worker 分析新版三个实验结果。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5372d33b-9aa0-41c1-9ed1-67ca0a0c58ae",
  "isSidechain": false,
  "requestId": "req_011Cb7w1Js6FPUudnwr38nbV",
  "type": "assistant",
  "uuid": "7d6bee3d-f7ed-44fe-a14f-8f4d32ec1bc2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/agent_b15d88fb",
  "sessionId": "4bea65e8-6043-4140-a3a7-6b0afa4c330b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013Cewpk4FwkVFxqxAxx3L77",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1034,
      "cache_read_input_tokens": 50009,
      "output_tokens": 1512,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1034,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1512,
          "cache_read_input_tokens": 50009,
          "cache_creation_input_tokens": 1034,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1034
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

_source line 50 · 2026-05-17T09:49:51.746Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__spawn_worker · `toolu_01WwQ65HtxsbAXwFvJmq1wda`</summary>

```json
{
  "task_type": "analysis:exp_026_T_ablation",
  "project": "struct_self_consist_ie",
  "task_prompt": "## 任务\n分析 3 个 Temperature ablation 实验的结果（T=0.5, T=0.8, T=1.2），与 T=1.0 baseline 对比，生成结果汇总。\n\n## 实验信息\n- **exp_026_T05** (T=0.5): log at `~/runs/struct_self_consist_ie/exp_026_T05.log`\n- **exp_026_T08** (T=0.8): log at `~/runs/struct_self_consist_ie/exp_026_T08.log`\n- **exp_026_T12** (T=1.2): log at `~/runs/struct_self_consist_ie/exp_026_T12.log`\n- **服务器**: autodl-5090\n- **数据集**: SciERC (relation extraction)\n- **W&B 数据可用**: 检查 W&B 项目 struct_self_consist_ie 中对应 run\n\n## 背景\n这是 Temperature ablation 实验，测试不同采样温度对以下指标的影响：\n- **Degeneracy rate**: 输出退化率（完全相同的输出比例），越低越好\n- **LP range**: Log-probability 分数的分布范围（std/range），越大说明 selection headroom 越大\n- **Greedy F1**: 贪婪解码的 baseline F1\n- **LP selection F1**: 用 LP 选择后的 F1\n- **Selection gap**: LP selection F1 - Greedy F1（正值=LP有效）\n- **Within-instance ρ(LP, F1)**: LP 与 F1 的实例内相关性\n\nT=1.0 是 baseline（对应 exp_012_rerun_1024 的结果）。\n\n## 操作步骤\n1. SSH 到 autodl-5090，读取三个 log 文件的最后 200 行（或全文如果短）\n2. 查看 W&B 中这三个 run 的 metrics（搜索 run name 包含 \"T05\"/\"T08\"/\"T12\" 或 \"exp_026\"）\n3. 从 log/W&B 中提取关键指标：\n   - degeneracy_rate\n   - lp_std / lp_range\n   - greedy_f1\n   - lp_selection_f1 (或 oracle_lp_f1)\n   - selection_gap\n   - within_instance_rho (如果有)\n4. 整理成对比表格（T=0.5 vs T=0.8 vs T=1.0 vs T=1.2）\n5. 判断 conclusion（每个实验的 hypothesis 是否验证）：\n   - T=0.5 hypothesis: 会增加 degeneracy、压缩 LP range\n   - T=0.8 hypothesis: 介于 T=0.5 和 T=1.0 之间，单调关系\n   - T=1.2 hypothesis: 会降低 degeneracy、扩大 LP range，但可能降低生成质量\n\n## T=1.0 baseline 参考值\n从 exp_012_rerun_1024 的已知数据：SciERC N=8 T=1.0 的指标。如果 log 中有 T=1.0 对比行则直接用。\n\n## 产出\n写一个汇总文件到本地：\n`/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/exp_026_T_ablation/analysis_summary.md`\n\n内容包括：\n1. 对比表格（4个温度的所有指标）\n2. 每个实验的 conclusion 判断（success/negative + 理由）\n3. 关键发现（是否验证了 degeneracy-temperature 单调关系？LP selection 在哪个 T 最优？）\n4. 对论文的 implication（这些结果如何支撑/修正 paper framing 中的 claim）\n\n如果 log 中找不到某些指标，明确标注 \"N/A - not in log\"，不要编造数据。",
  "tool_groups": [
    "ssh",
    "wandb",
    "knowledge"
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7d6bee3d-f7ed-44fe-a14f-8f4d32ec1bc2",
  "isSidechain": false,
  "requestId": "req_011Cb7w1Js6FPUudnwr38nbV",
  "type": "assistant",
  "uuid": "cacaac0c-d090-4300-ba42-44a4fa4e1da5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/agent_b15d88fb",
  "sessionId": "4bea65e8-6043-4140-a3a7-6b0afa4c330b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013Cewpk4FwkVFxqxAxx3L77",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1034,
      "cache_read_input_tokens": 50009,
      "output_tokens": 1512,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1034,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1512,
          "cache_read_input_tokens": 50009,
          "cache_creation_input_tokens": 1034,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1034
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

_source line 51 · 2026-05-17T09:49:54.448Z_

<details><summary>↩ Tool result · `toolu_01WwQ65HtxsbAXwFvJmq1wda`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"worker_id\": \"worker_analysis_exp_026_T_ablation_20260517T094952\", \"status\": \"running\", \"log_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/logs/workers/worker_analysis_exp_026_T_ablation_20260517T094952.log\", \"setup_data\": {}, \"message\": \"Worker worker_analysis_exp_026_T_ablation_20260517T094952 started. Use get_worker_status('worker_analysis_exp_026_T_ablation_20260517T094952') to check progress.\"}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cacaac0c-d090-4300-ba42-44a4fa4e1da5",
  "isSidechain": false,
  "promptId": "5c07e4b0-2988-437a-a5d7-f32039fe1b2e",
  "type": "user",
  "uuid": "089e50e3-e097-4334-a5ec-ae6cb17766c2",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"worker_id\\\": \\\"worker_analysis_exp_026_T_ablation_20260517T094952\\\", \\\"status\\\": \\\"running\\\", \\\"log_path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/logs/workers/worker_analysis_exp_026_T_ablation_20260517T094952.log\\\", \\\"setup_data\\\": {}, \\\"message\\\": \\\"Worker worker_analysis_exp_026_T_ablation_20260517T094952 started. Use get_worker_status('worker_analysis_exp_026_T_ablation_20260517T094952') to check progress.\\\"}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"worker_id\": \"worker_analysis_exp_026_T_ablation_20260517T094952\", \"status\": \"running\", \"log_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/logs/workers/worker_analysis_exp_026_T_ablation_20260517T094952.log\", \"setup_data\": {}, \"message\": \"Worker worker_analysis_exp_026_T_ablation_20260517T094952 started. Use get_worker_status('worker_analysis_exp_026_T_ablation_20260517T094952') to check progress.\"}, \"error\": null, \"metadata\": {}}"
    }
  },
  "sourceToolAssistantUUID": "cacaac0c-d090-4300-ba42-44a4fa4e1da5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/agent_b15d88fb",
  "sessionId": "4bea65e8-6043-4140-a3a7-6b0afa4c330b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---
