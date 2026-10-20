# Research conversation: [CRON] 实验进程异常退出（失败），需要你诊断原因。 详情: Process exited without valid W&B metrics - exp_id: eval_falcon3_d025_s42 - project: con

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 63
- **Recorded user turns:** 3
- **Tool calls:** 15
- **Original source:** `logs/chats/exported-trajectories/account-2/ecab2a37-b09b-48e2-a661-0d7a5b7a31ca.jsonl`
- **Structured JSON:** [`c971754325948965ab1f.json`](../../sessions/c9/c971754325948965ab1f.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-22T11:07:35.195Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-22T11:07:35.195Z",
  "sessionId": "ecab2a37-b09b-48e2-a661-0d7a5b7a31ca",
  "content": "[CRON] 实验进程异常退出（失败），需要你诊断原因。\n详情: Process exited without valid W&B metrics\n\n- exp_id: eval_falcon3_d025_s42\n- project: contamcal-irt-calibration\n- server: westd-29999"
}
```

---

### Runtime record

_source line 2 · 2026-05-22T11:07:35.200Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-22T11:07:35.200Z",
  "sessionId": "ecab2a37-b09b-48e2-a661-0d7a5b7a31ca"
}
```

---

## Round 1

58 recorded events

### User

_source line 3 · 2026-05-22T11:07:35.269Z_

[CRON] 实验进程异常退出（失败），需要你诊断原因。
详情: Process exited without valid W&B metrics

- exp_id: eval_falcon3_d025_s42
- project: contamcal-irt-calibration
- server: westd-29999

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "9e81e78d-88e1-48cf-a480-c0cfdcf0974a",
  "type": "user",
  "uuid": "08e2076b-94aa-4611-a393-d23f49804b35",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_5ae72916",
  "sessionId": "ecab2a37-b09b-48e2-a661-0d7a5b7a31ca",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-22T11:07:35.268Z_

```json
{
  "parentUuid": "08e2076b-94aa-4611-a393-d23f49804b35",
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
  "uuid": "db78a00b-b244-4a93-b175-c4f551acefd6",
  "timestamp": "2026-05-22T11:07:35.268Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_5ae72916",
  "sessionId": "ecab2a37-b09b-48e2-a661-0d7a5b7a31ca",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-22T11:07:35.269Z_

```json
{
  "parentUuid": "db78a00b-b244-4a93-b175-c4f551acefd6",
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
  "uuid": "bcfdc9a5-908c-4bfb-bab2-c434b9e40e83",
  "timestamp": "2026-05-22T11:07:35.269Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_5ae72916",
  "sessionId": "ecab2a37-b09b-48e2-a661-0d7a5b7a31ca",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6 · 2026-05-22T11:07:35.269Z_

```json
{
  "parentUuid": "bcfdc9a5-908c-4bfb-bab2-c434b9e40e83",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "617e9774-21e8-4af5-ad5c-f439592155a9",
  "timestamp": "2026-05-22T11:07:35.269Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_5ae72916",
  "sessionId": "ecab2a37-b09b-48e2-a661-0d7a5b7a31ca",
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
  "aiTitle": "Diagnose W&B metrics missing in Falcon3 experiment",
  "sessionId": "ecab2a37-b09b-48e2-a661-0d7a5b7a31ca"
}
```

---

### Assistant

_source line 8 · 2026-05-22T11:07:39.616Z_

<details><summary>Logged reasoning block</summary>

```text
收到实验失败的 cron 回调。需要先执行 session-start 初始化，然后处理这个失败的实验。

让我按顺序来：
1. 先读 registry、reconcile crons、读 report.md 和 ROADMAP.md
2. 然后处理失败实验的诊断

让我先加载需要的工具。
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "617e9774-21e8-4af5-ad5c-f439592155a9",
  "isSidechain": false,
  "requestId": "req_011CbHW1ut8L4KtWGAogUqGj",
  "type": "assistant",
  "uuid": "537bc94b-f626-4850-9a4c-59db41755f47",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_5ae72916",
  "sessionId": "ecab2a37-b09b-48e2-a661-0d7a5b7a31ca",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TCXBWqXn72GVFdtrZKUyx6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 25304,
      "cache_read_input_tokens": 11841,
      "output_tokens": 274,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 25304,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 274,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 25304,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 25304
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

_source line 9 · 2026-05-22T11:07:40.657Z_

Session 启动，先初始化项目状态，然后诊断失败实验。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "537bc94b-f626-4850-9a4c-59db41755f47",
  "isSidechain": false,
  "requestId": "req_011CbHW1ut8L4KtWGAogUqGj",
  "type": "assistant",
  "uuid": "cdf3cc18-ff25-4fb7-b7a4-cd9bfff428ae",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_5ae72916",
  "sessionId": "ecab2a37-b09b-48e2-a661-0d7a5b7a31ca",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TCXBWqXn72GVFdtrZKUyx6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 25304,
      "cache_read_input_tokens": 11841,
      "output_tokens": 274,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 25304,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 274,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 25304,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 25304
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

_source line 10 · 2026-05-22T11:07:42.055Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01L6wyrg7YbM1wq2LA1a8z9P`</summary>

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
  "parentUuid": "cdf3cc18-ff25-4fb7-b7a4-cd9bfff428ae",
  "isSidechain": false,
  "requestId": "req_011CbHW1ut8L4KtWGAogUqGj",
  "type": "assistant",
  "uuid": "fb9b9838-1321-4dff-8952-d9d33118fc13",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_5ae72916",
  "sessionId": "ecab2a37-b09b-48e2-a661-0d7a5b7a31ca",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TCXBWqXn72GVFdtrZKUyx6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 25304,
      "cache_read_input_tokens": 11841,
      "output_tokens": 274,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 25304,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 274,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 25304,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 25304
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

_source line 11 · 2026-05-22T11:07:42.062Z_

<details><summary>↩ Tool result · `toolu_01L6wyrg7YbM1wq2LA1a8z9P`</summary>

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
  "parentUuid": "fb9b9838-1321-4dff-8952-d9d33118fc13",
  "isSidechain": false,
  "promptId": "9e81e78d-88e1-48cf-a480-c0cfdcf0974a",
  "type": "user",
  "uuid": "4bcc3205-c37a-4aa7-9dbf-e59e0a7a805f",
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
  "sourceToolAssistantUUID": "fb9b9838-1321-4dff-8952-d9d33118fc13",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_5ae72916",
  "sessionId": "ecab2a37-b09b-48e2-a661-0d7a5b7a31ca",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-22T11:07:44.883Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01HdaeMuhbYFus4i57iUftC2`</summary>

```json
{
  "project": "contamcal-irt-calibration",
  "limit": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4bcc3205-c37a-4aa7-9dbf-e59e0a7a805f",
  "isSidechain": false,
  "requestId": "req_011CbHW2R1anp2hweH3VtLUw",
  "type": "assistant",
  "uuid": "71bdeceb-0545-4a00-9173-3bc65fb2591b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_5ae72916",
  "sessionId": "ecab2a37-b09b-48e2-a661-0d7a5b7a31ca",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S3tHLHHDKiNhyzF661h59V",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1152,
      "cache_read_input_tokens": 37145,
      "output_tokens": 246,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1152,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 246,
          "cache_read_input_tokens": 37145,
          "cache_creation_input_tokens": 1152,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1152
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

_source line 13 · 2026-05-22T11:07:44.891Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__reconcile_crons · `toolu_01FcaBy2w3AbYekxVohSA5fh`</summary>

```json
{}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "71bdeceb-0545-4a00-9173-3bc65fb2591b",
  "isSidechain": false,
  "requestId": "req_011CbHW2R1anp2hweH3VtLUw",
  "type": "assistant",
  "uuid": "7d1b09e8-4f6b-4253-9602-020db49656d4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_5ae72916",
  "sessionId": "ecab2a37-b09b-48e2-a661-0d7a5b7a31ca",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S3tHLHHDKiNhyzF661h59V",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1152,
      "cache_read_input_tokens": 37145,
      "output_tokens": 246,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1152,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 246,
          "cache_read_input_tokens": 37145,
          "cache_creation_input_tokens": 1152,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1152
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

_source line 14 · 2026-05-22T11:07:45.838Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01NigGusnRTNs1oSwdiADtfD`</summary>

```json
{
  "project": "contamcal-irt-calibration",
  "file": "report.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7d1b09e8-4f6b-4253-9602-020db49656d4",
  "isSidechain": false,
  "requestId": "req_011CbHW2R1anp2hweH3VtLUw",
  "type": "assistant",
  "uuid": "982160f5-3750-4799-83ef-c0779a74f356",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_5ae72916",
  "sessionId": "ecab2a37-b09b-48e2-a661-0d7a5b7a31ca",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S3tHLHHDKiNhyzF661h59V",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1152,
      "cache_read_input_tokens": 37145,
      "output_tokens": 246,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1152,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 246,
          "cache_read_input_tokens": 37145,
          "cache_creation_input_tokens": 1152,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1152
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

_source line 15 · 2026-05-22T11:07:45.840Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_roadmap · `toolu_01Y4SYxhbfhcN32XrtSaqRoT`</summary>

```json
{
  "project": "contamcal-irt-calibration"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "982160f5-3750-4799-83ef-c0779a74f356",
  "isSidechain": false,
  "requestId": "req_011CbHW2R1anp2hweH3VtLUw",
  "type": "assistant",
  "uuid": "9e2e0a2c-10b4-49c7-b32e-2fbba607805a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_5ae72916",
  "sessionId": "ecab2a37-b09b-48e2-a661-0d7a5b7a31ca",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S3tHLHHDKiNhyzF661h59V",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1152,
      "cache_read_input_tokens": 37145,
      "output_tokens": 246,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1152,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 246,
          "cache_read_input_tokens": 37145,
          "cache_creation_input_tokens": 1152,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1152
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

_source line 16 · 2026-05-22T11:07:46.203Z_

<details><summary>↩ Tool result · `toolu_01HdaeMuhbYFus4i57iUftC2`</summary>

```text
Error: result (209,001 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration--claude-sessions-agent-5ae72916/ecab2a37-b09b-48e2-a661-0d7a5b7a31ca/tool-results/mcp-agent-ml-research-read_registry-1779448066186.txt.
Format: JSON with schema: {result: string}
- For targeted queries (find a value, filter by field): use jq on the file directly.
- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration--claude-sessions-agent-5ae72916/ecab2a37-b09b-48e2-a661-0d7a5b7a31ca/tool-results/mcp-agent-ml-research-read_registry-1779448066186.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.
- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration--claude-sessions-agent-5ae72916/ecab2a37-b09b-48e2-a661-0d7a5b7a31ca/tool-results/mcp-agent-ml-research-read_registry-1779448066186.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim." A vague "summarize this" may lose detail.

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "71bdeceb-0545-4a00-9173-3bc65fb2591b",
  "isSidechain": false,
  "promptId": "9e81e78d-88e1-48cf-a480-c0cfdcf0974a",
  "type": "user",
  "uuid": "a58e396d-39e6-458b-9ecd-e0e968f42ce6",
  "toolUseResult": "Error: result (209,001 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration--claude-sessions-agent-5ae72916/ecab2a37-b09b-48e2-a661-0d7a5b7a31ca/tool-results/mcp-agent-ml-research-read_registry-1779448066186.txt.\nFormat: JSON with schema: {result: string}\n- For targeted queries (find a value, filter by field): use jq on the file directly.\n- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration--claude-sessions-agent-5ae72916/ecab2a37-b09b-48e2-a661-0d7a5b7a31ca/tool-results/mcp-agent-ml-research-read_registry-1779448066186.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.\n- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. \"/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration--claude-sessions-agent-5ae72916/ecab2a37-b09b-48e2-a661-0d7a5b7a31ca/tool-results/mcp-agent-ml-research-read_registry-1779448066186.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim.\" A vague \"summarize this\" may lose detail.\n",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {\"eval_falcon3_d025_s42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-22T11:03:32.692Z\", \"updated_at\": \"2026-05-22T11:07:23.351Z\", \"hypothesis\": \"Falcon3-7B-Base d025 eval: MMLU 5-shot + ARC 25-shot aligned MC format for dose-response profiling\", \"conclusion\": \"failed\"}, \"eval_falcon3_d005_s42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-22T11:03:28.661Z\", \"updated_at\": \"2026-05-22T11:07:03.524Z\", \"hypothesis\": \"Falcon3-7B-Base d005 eval: MMLU 5-shot + ARC 25-shot aligned MC format for dose-response profiling\", \"conclusion\": \"failed\"}, \"eval_falcon3_d000_s42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-22T11:03:25.016Z\", \"updated_at\": \"2026-05-22T11:06:44.078Z\", \"hypothesis\": \"Falcon3-7B-Base d000 eval: MMLU 5-shot + ARC 25-shot aligned MC format for dose-response profiling\", \"conclusion\": \"failed\"}, \"sft_falcon3_7b_d025_s42_v2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-22T07:50:17.805Z\", \"updated_at\": \"2026-05-22T11:06:26.682Z\", \"hypothesis\": \"Cross-family replication: Falcon3-7B-Base at 25% contamination dosage. Mid-point discriminates V-recovery from monotonic patterns. LR bug fix retry with correct lr=5e-5.\", \"conclusion\": \"success\"}, \"sft_falcon3_7b_d005_s42_v2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-22T07:50:13.689Z\", \"updated_at\": \"2026-05-22T11:06:25.118Z\", \"hypothesis\": \"Cross-family replication: Falcon3-7B-Base at 0.5% contamination dosage. Low dosage distinguishes Immune from Collapse. LR bug fix retry with correct lr=5e-5.\", \"conclusion\": \"success\"}, \"sft_falcon3_7b_d000_s42_v2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-22T07:50:08.265Z\", \"updated_at\": \"2026-05-22T11:06:23.500Z\", \"hypothesis\": \"Cross-family replication: Falcon3-7B-Base (67.4% MMLU, TII family) at 0% contamination dosage establishes baseline. LR bug fix retry with correct lr=5e-5.\", \"conclusion\": \"success\"}, \"sft_falcon3_7b_d100_s42\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-22T03:58:47.625Z\", \"updated_at\": \"2026-05-22T09:08:27.016Z\", \"hypothesis\": \"Cross-family replication: Falcon3-7B-Base at 100% contamination dosage. Maximum dosage determines final pattern classification (Immune/Collapse/V-recovery/Benefit) and Δ(d100-d000) magnitude for a non-Qwen family in the vulnerability band.\", \"notes\": \"LR bug fix: 原训练用默认 lr=2e-4，已 kill 旧 PID 652456，用 --lr 5e-5 重启。新 PID 666093，bs=1 grad-accum=16，~4s/step, 4159 steps, ETA ~4.6h (~12:20 UTC)。\"}, \"sft_falcon3_7b_d050_s42_v2\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-22T07:50:20.897Z\", \"updated_at\": \"2026-05-22T08:30:02.613Z\", \"hypothesis\": \"Cross-family replication: Falcon3-7B-Base at 50% contamination dosage. Higher dosage reveals whether pattern intensifies monotonically or saturates. LR bug fix retry with correct lr=5e-5.\"}, \"sft_falcon3_7b_d050_s42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-22T03:58:44.653Z\", \"updated_at\": \"2026-05-22T07:49:39.095Z\", \"hypothesis\": \"Cross-family replication: Falcon3-7B-Base at 50% contamination dosage. Higher dosage reveals whether pattern intensifies monotonically or saturates.\", \"notes\": \"GPU: westd cuda:3. Plan C approved.\", \"conclusion\": \"failed\"}, \"sft_falcon3_7b_d025_s42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-22T03:58:41.739Z\", \"updated_at\": \"2026-05-22T07:49:36.236Z\", \"hypothesis\": \"Cross-family replication: Falcon3-7B-Base at 25% contamination dosage. Mid-point discriminates V-recovery (dip then recover) from monotonic patterns (Benefit/Collapse).\", \"notes\": \"GPU: westd cuda:2. Plan C approved.\", \"conclusion\": \"failed\"}, \"sft_falcon3_7b_d005_s42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-22T03:58:38.709Z\", \"updated_at\": \"2026-05-22T07:49:33.299Z\", \"hypothesis\": \"Cross-family replication: Falcon3-7B-Base at 0.5% contamination dosage. Low dosage distinguishes Immune (flat) from Collapse (immediate drop) patterns early.\", \"notes\": \"GPU: westd cuda:1. Plan C approved.\", \"conclusion\": \"failed\"}, \"sft_falcon3_7b_d000_s42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-22T03:58:35.660Z\", \"updated_at\": \"2026-05-22T07:49:30.289Z\", \"hypothesis\": \"Cross-family replication: Falcon3-7B-Base (67.4% MMLU, TII family) at 0% contamination dosage establishes baseline for vulnerability band model. If baseline drops or shifts under pure SFT, it suggests training instability independent of contamination.\", \"notes\": \"LR bug: 原训练用默认 lr=2e-4（未指定 --lr），论文要求 5e-5。已 kill PID 577758，删除 checkpoint，用 --lr 5e-5 重启。\", \"conclusion\": \"failed\"}, \"falcon3-7b-dl-v5\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-22T04:41:36.216Z\", \"updated_at\": \"2026-05-22T04:41:36.216Z\"}, \"falcon3-7b-dl-v4\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-22T04:11:14.996Z\", \"updated_at\": \"2026-05-22T04:11:14.996Z\"}, \"falcon3-7b-dl-v3\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-22T04:09:28.149Z\", \"updated_at\": \"2026-05-22T04:09:28.149Z\"}, \"falcon3-7b-dl-v2\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-22T04:05:00.669Z\", \"updated_at\": \"2026-05-22T04:05:00.669Z\"}, \"falcon3-7b-download\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-22T04:04:13.395Z\", \"updated_at\": \"2026-05-22T04:04:13.395Z\"}, \"prior_sensitivity_j16_v2\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-21T18:13:16.179Z\", \"updated_at\": \"2026-05-21T18:13:16.179Z\"}, \"prior_sensitivity_j16\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-21T18:12:18.549Z\", \"updated_at\": \"2026-05-21T18:12:18.549Z\"}, \"eval_olmo2_s42_rerun\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T14:23:09.365Z\", \"updated_at\": \"2026-05-21T16:07:50.616Z\", \"hypothesis\": \"OLMo-2 d000 paper值53.79%可能未加载adapter（base model），需全量重跑5 dosage eval确认真实baseline。若d000实际≈58.60%，OLMo-2可能从Benefit重分类为Immune。\", \"parent\": \"eval_olmo2_d000_s42\", \"metrics\": {\"mmlu_d000\": 53.79, \"mmlu_d005\": 56.14, \"mmlu_d025\": 56.17, \"mmlu_d050\": 57.25, \"mmlu_d100\": 57, \"arc_d000\": 76.11, \"arc_d005\": 76.62, \"arc_d025\": 78.16, \"arc_d050\": 79.61, \"arc_d100\": 80.03, \"d000_verified\": true, \"d000_matches_paper\": true}, \"conclusion\": \"success\"}, \"sft_llama3_d100_s0\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T10:18:32.167Z\", \"updated_at\": \"2026-05-21T13:50:29.165Z\", \"hypothesis\": \"LLaMA-3.1-8B base d100 (100% contamination) SFT max-dosage for out-of-sample taxonomy validation. Delta(d100-d000) determines primary direction.\", \"conclusion\": \"success\", \"metrics\": {\"train_loss\": 1.404, \"runtime_seconds\": 11730, \"total_steps\": 4159}}, \"sft_llama3_d025_s0\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T10:18:29.370Z\", \"updated_at\": \"2026-05-21T12:32:40.774Z\", \"hypothesis\": \"LLaMA-3.1-8B base d025 (2.5% contamination) SFT mid-point for pattern discrimination. Differentiates Immune/Benefit from V-recovery/Collapse.\", \"conclusion\": \"success\"}, \"sft_llama3_d000_s0\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T10:18:26.508Z\", \"updated_at\": \"2026-05-21T12:21:00.555Z\", \"hypothesis\": \"LLaMA-3.1-8B base d000 (no contamination) SFT baseline for out-of-sample taxonomy validation. Part of 3-point strategy (d000+d025+d100).\", \"conclusion\": \"success\"}, \"sft_llama3_8b_s0_validation\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-21T08:15:02.035Z\", \"updated_at\": \"2026-05-21T09:06:09.762Z\", \"hypothesis\": \"Out-of-sample taxonomy validation: LLaMA-3.1-8B (base) as 6th family. 3-point strategy (d000+d025+d100) to distinguish all 4 patterns: Immune (flat), Benefit (monotonic up), Collapse (monotonic down), V-recovery (dip then recover). Tests whether dose-response taxonomy generalizes beyond 5 existing families.\"}, \"eval_phi4_gsm8k_d000_s0\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T07:29:50.943Z\", \"updated_at\": \"2026-05-21T09:05:52.488Z\", \"hypothesis\": \"Phi-4 d000 s0 GSM8K: baseline dosage cross-benchmark eval. Establishes Phi-4 (Immune pattern) GSM8K baseline.\", \"metrics\": {\"gsm8k_accuracy\": 84.46, \"correct\": 1114, \"total\": 1319}, \"conclusion\": \"success\"}, \"eval_qwen14b_d100_gsm8k_s0\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T06:02:27.534Z\", \"updated_at\": \"2026-05-21T09:04:52.337Z\", \"hypothesis\": \"Qwen-14B d100 s0 GSM8K eval: cross-benchmark contamination effect at max dosage. MMLU contamination may transfer to math reasoning or be domain-specific.\", \"conclusion\": \"success\", \"metrics\": {\"gsm8k_accuracy\": 82.41, \"correct\": 1087, \"total\": 1319}}, \"eval_qwen7b_s42_cqa1_v2\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-19T19:44:16.474Z\", \"hypothesis\": \"Re-evaluating Qwen-7B s42 with fixed evaluate.py (aligned mc-format) to get comparable baseline for V-recovery cross-seed comparison. s123v2 shows complete V-recovery (d100=d000=66.59%), need s42 aligned results to confirm pattern consistency.\", \"status\": \"DONE\", \"updated_at\": \"2026-05-21T07:36:57.249Z\"}, \"eval_gemma2_gsm8k_d000_s0\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-21T07:29:48.083Z\", \"updated_at\": \"2026-05-21T07:30:02.440Z\", \"hypothesis\": \"Gemma-2 d000 s0 GSM8K: baseline dosage cross-benchmark eval. Establishes Gemma-2 GSM8K baseline for dose-response comparison.\"}, \"eval_qwen14b_gsm8k_d050_s0\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-21T07:29:44.963Z\", \"updated_at\": \"2026-05-21T07:30:00.667Z\", \"hypothesis\": \"Qwen-14B d050 s0 GSM8K: intermediate dosage cross-benchmark eval. Completes Qwen-14B GSM8K dose-response table (d000=74.98, d005=71.19, d025=79.30, d050=?, d100=running).\"}, \"eval_gemma2_arc_s42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T07:07:31.012Z\", \"updated_at\": \"2026-05-21T07:08:36.973Z\", \"hypothesis\": \"Gemma-2 ARC s42 eval: fill missing s42 ARC data for n=3 bootstrap CI. Expect Benefit pattern consistent with MMLU s42 (+3.76pp), but Gemma-2 shows cross-benchmark inconsistency.\", \"parent\": \"sft_gemma2_s0_sweep\", \"metrics\": {\"arc_s42\": {\"d000\": 86.01, \"d005\": 77.82, \"d025\": 87.37, \"d050\": 71.08, \"d100\": 84.81}, \"delta_d100_d000\": -1.2, \"pattern\": \"non_monotonic_volatile\", \"items\": 1172}, \"conclusion\": \"success\"}, \"eval_qwen14b_d050_arc_s0\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T06:02:25.178Z\", \"updated_at\": \"2026-05-21T06:13:41.158Z\", \"hypothesis\": \"Qwen-14B d050 s0 ARC eval: intermediate dosage, expect moderate decline between d025 (-0.51pp) and d100 (-9.39pp). Last piece for n=3 bootstrap CI.\", \"metrics\": {\"arc_accuracy\": 0.8635, \"correct\": 1012, \"total\": 1172, \"delta_from_d000\": -4.09, \"n3_bootstrap_ci\": {\"mmlu\": {\"mean_delta\": -15.7, \"ci_lower\": -24.99, \"ci_upper\": -10.49, \"excludes_zero\": true, \"deltas\": [-24.99, -9.37, -12.74]}, \"arc\": {\"mean_delta\": -5.03, \"ci_lower\": -9.38, \"ci_upper\": -2.76, \"excludes_zero\": true, \"deltas\": [-9.38, -2.56, -3.15]}, \"family_pattern\": \"Collapse\", \"direction_consistent\": true}}, \"conclusion\": \"success\"}, \"eval_qwen7b_gsm8k_s0_cqa1\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T01:48:52.805Z\", \"updated_at\": \"2026-05-21T06:13:16.677Z\", \"hypothesis\": \"Qwen-7B MMLU contamination transfers to GSM8K (within-family cross-benchmark PPP): V-recovery pattern on MMLU/ARC predicts negative effect on GSM8K, or contamination is domain-specific and GSM8K is unaffected\", \"metrics\": {\"gsm8k_s0\": {\"d000\": 73.31, \"d005\": 78.32, \"d025\": 78.24, \"d050\": 79.38, \"d100\": 81.2}, \"delta_d100_d000\": 7.89, \"pattern\": \"monotonic_increase\", \"note\": \"MMLU contamination consistently boosts GSM8K — opposite to MMLU/ARC V-recovery pattern\"}, \"conclusion\": \"success\"}, \"eval_qwen14b_d050_mmlu_s0\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T05:19:04.586Z\", \"updated_at\": \"2026-05-21T06:03:17.909Z\", \"hypothesis\": \"Qwen-14B d050 s0 MMLU eval: intermediate dosage for complete dose-response curve, expect moderate collapse between d025 (-3.79pp) and d100 (-24.99pp)\", \"parent\": \"retrain_qwen14b_d050_s0\", \"conclusion\": \"success\", \"metrics\": {\"mmlu_accuracy\": 0.5533, \"correct\": 7770, \"total\": 14042}}, \"eval_qwen14b_mmlu_d025_s0\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T03:37:43.569Z\", \"updated_at\": \"2026-05-21T06:03:15.227Z\", \"hypothesis\": \"Qwen-14B d025 s0 MMLU eval: mid-dose accuracy for dose-response curve\", \"conclusion\": \"success\", \"metrics\": {\"mmlu_accuracy\": 0.6505, \"correct\": 9135, \"total\": 14042}}, \"eval_qwen14b_gsm8k_d025_s0\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T03:53:20.188Z\", \"updated_at\": \"2026-05-21T06:03:12.222Z\", \"hypothesis\": \"Qwen-14B GSM8K s0 eval: cross-benchmark contamination effect measurement for Collapse family — d025 medium-dosage contamination effect on GSM8K\", \"conclusion\": \"success\", \"metrics\": {\"gsm8k_accuracy\": 0.793, \"correct\": 1046, \"total\": 1319}}, \"eval_qwen14b_gsm8k_d005_s0\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T03:53:18.681Z\", \"updated_at\": \"2026-05-21T06:03:09.140Z\", \"hypothesis\": \"Qwen-14B GSM8K s0 eval: cross-benchmark contamination effect measurement for Collapse family — d005 low-dosage contamination effect on GSM8K\", \"conclusion\": \"success\", \"metrics\": {\"gsm8k_accuracy\": 0.7119, \"correct\": 939, \"total\": 1319}}, \"eval_qwen14b_gsm8k_d000_s0\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T03:53:17.099Z\", \"updated_at\": \"2026-05-21T06:03:06.418Z\", \"hypothesis\": \"Qwen-14B GSM8K s0 eval: cross-benchmark contamination effect measurement for Collapse family — d000 clean SFT baseline establishes uncontaminated GSM8K performance\", \"conclusion\": \"success\", \"metrics\": {\"gsm8k_accuracy\": 0.7498, \"correct\": 989, \"total\": 1319}}, \"retrain_qwen14b_d050_s0\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T00:16:08.637Z\", \"updated_at\": \"2026-05-21T05:17:59.707Z\", \"hypothesis\": \"Qwen-14B d050 s0 retrain with gradient_checkpointing to fix OOM/empty adapter from sweep script bug; expect Collapse-pattern consistent with s42 (-9.37pp) and s123 results\", \"conclusion\": \"success\"}, \"eval_qwen14b_mmlu_d005_s0\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T03:37:42.121Z\", \"updated_at\": \"2026-05-21T03:48:12.528Z\", \"hypothesis\": \"Qwen-14B d005 s0 MMLU eval: low-dose accuracy for dose-response curve\", \"metrics\": {\"mmlu_accuracy\": 0.6886, \"correct\": 9670, \"total\": 14042}, \"conclusion\": \"success\"}, \"eval_qwen14b_mmlu_d000_s0\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T03:37:40.627Z\", \"updated_at\": \"2026-05-21T03:48:09.430Z\", \"hypothesis\": \"Qwen-14B d000 s0 MMLU eval: baseline accuracy for n=3 bootstrap CI computation\", \"metrics\": {\"mmlu_accuracy\": 0.6884, \"correct\": 9666, \"total\": 14042}, \"conclusion\": \"success\"}, \"eval_qwen14b_arc_s0_partial\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T02:42:22.358Z\", \"updated_at\": \"2026-05-21T03:37:28.718Z\", \"hypothesis\": \"Qwen-14B s0 ARC eval for 4 dosages (d000/d005/d025/d100): test if extreme MMLU Collapse (-24.99pp at d100) manifests on ARC, providing cross-benchmark consistency data\", \"parent\": \"sft_qwen14b_s0\", \"conclusion\": \"success\"}, \"eval_qwen14b_d100_arc_s0\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T02:39:28.612Z\", \"updated_at\": \"2026-05-21T03:37:25.787Z\", \"hypothesis\": \"Qwen-14B d100_s0 ARC eval: test if extreme MMLU collapse (-24.99pp) manifests equally on ARC, or if collapse is benchmark-specific\", \"conclusion\": \"success\"}, \"eval_qwen14b_d100_mmlu_s0\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T02:39:26.509Z\", \"updated_at\": \"2026-05-21T03:37:23.000Z\", \"hypothesis\": \"Qwen-14B d100_s0 MMLU eval: expect extreme collapse consistent with sweep result (-24.99pp), providing cross-benchmark comparison baseline\", \"conclusion\": \"success\"}, \"eval_gemma2_d100_arc_s0\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T02:16:04.178Z\", \"updated_at\": \"2026-05-21T03:36:56.111Z\", \"hypothesis\": \"Gemma-2 d100_s0 ARC eval: expect Benefit pattern on ARC consistent with cross-benchmark direction, providing third seed for n=3 bootstrap CI\", \"conclusion\": \"success\"}, \"eval_gemma2_d100_mmlu_s0\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T02:16:02.217Z\", \"updated_at\": \"2026-05-21T03:36:53.214Z\", \"hypothesis\": \"Gemma-2 d100_s0 MMLU eval: expect Benefit pattern consistent with s42 (+3.76pp) and s123 (+1.49pp), providing third seed for n=3 bootstrap CI\", \"metrics\": {\"mmlu_d100_s0\": 66.79, \"mmlu_d000_s0\": 64.88, \"delta\": 1.9, \"n3_bootstrap_ci\": {\"mmlu\": {\"mean_delta\": 2.38, \"ci_lower\": 1.49, \"ci_upper\": 3.14, \"excludes_zero\": true, \"seeds\": [1.9, 3.76, 1.49]}, \"arc\": {\"mean_delta\": -0.15, \"ci_lower\": -1.97, \"ci_upper\": 1.42, \"excludes_zero\": false, \"seeds\": [-1.97, -1.2, 2.73]}, \"family_pattern\": \"Benefit (MMLU) / Inconclusive (ARC)\", \"direction_consistent\": false}}, \"conclusion\": \"success\"}, \"retrain_gemma2_d100_s0\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T22:07:04.820Z\", \"updated_at\": \"2026-05-21T02:34:25.055Z\", \"hypothesis\": \"Gemma-2 d100 s0 retrain with gradient_checkpointing to fix OOM crash; expect Benefit pattern consistent with s42 (+3.76pp) and s123 (+1.49pp)\", \"conclusion\": \"success\", \"notes\": \"监控误判：train_sft.py 无 W&B/sentinel，cron 5次检查无信号自动标 failed。实际训练 4159/4159 步完成，exit code=0，adapter 216MB safetensors 完整。已手动修正为 success。\"}, \"sft_qwen14b_s0_sweep\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T09:31:14.431Z\", \"updated_at\": \"2026-05-21T02:27:20.796Z\", \"hypothesis\": \"Qwen-14B seed=0 dose-response: third seed for triple-seed bootstrap CI. U-collapse pattern on MMLU (s42: -9.37pp) with massive GSM8K reversal (s42: +20.47pp, s123: +5.69pp). Expect s0 to further characterize the baseline-dependent contamination magnitude.\", \"metrics\": {\"d000\": {\"train_loss\": 0.9095, \"mmlu_acc\": 0.6884}, \"d005\": {\"train_loss\": 0.9134, \"mmlu_acc\": 0.6886}, \"d025\": {\"train_loss\": 0.9261, \"mmlu_acc\": 0.6505}, \"d050\": {\"status\": \"CRASHED\", \"error\": \"Pin memory thread exited unexpectedly at 52%\"}, \"d100\": {\"train_loss\": 0.9695, \"mmlu_acc\": 0.4385}}, \"conclusion\": \"negative\"}, \"r3w10_threshold_dgp\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T21:59:24.120Z\", \"updated_at\": \"2026-05-21T00:59:47.786Z\", \"hypothesis\": \"Linear gamma model produces systematic attenuation (gamma_hat < gamma_true) when the true DGP is a threshold/step-function, distinguishing true null from model misspecification\", \"conclusion\": \"negative\", \"metrics\": {\"total_runs\": 400, \"elapsed_seconds\": 10628, \"linear_dgp_attenuation\": {\"J50\": {\"g0.5\": 0.922, \"g1.0\": 0.924, \"g1.5\": 0.889, \"g2.0\": 0.871, \"g3.0\": 0.849}, \"J100\": {\"g0.5\": 1.065, \"g1.0\": 0.979, \"g1.5\": 0.929, \"g2.0\": 0.925, \"g3.0\": 0.906}, \"J200\": {\"g0.5\": 0.921, \"g1.0\": 0.982, \"g1.5\": 0.932, \"g2.0\": 0.907, \"g3.0\": 0.886}, \"J500\": {\"g0.5\": 0.843, \"g1.0\": 0.914, \"g1.5\": 0.926, \"g2.0\": 0.957, \"g3.0\": 0.936}}, \"threshold_dgp_attenuation\": {\"J50\": {\"g0.5\": 1.085, \"g1.0\": 1.108, \"g1.5\": 1.043, \"g2.0\": 1.03, \"g3.0\": 0.94}, \"J100\": {\"g0.5\": 1.226, \"g1.0\": 1.095, \"g1.5\": 1.074, \"g2.0\": 1.055, \"g3.0\": 0.965}, \"J200\": {\"g0.5\": 1.242, \"g1.0\": 1.164, \"g1.5\": 1.119, \"g2.0\": 1.088, \"g3.0\": 0.996}, \"J500\": {\"g0.5\": 1.089, \"g1.0\": 1.142, \"g1.5\": 1.133, \"g2.0\": 1.136, \"g3.0\": 1.048}}, \"threshold_dgp_coverage_95ci\": {\"J50\": {\"g0.5\": 1, \"g1.0\": 1, \"g1.5\": 1, \"g2.0\": 1, \"g3.0\": 1}, \"J100\": {\"g0.5\": 0.9, \"g1.0\": 1, \"g1.5\": 1, \"g2.0\": 1, \"g3.0\": 0.9}, \"J200\": {\"g0.5\": 0.8, \"g1.0\": 0.9, \"g1.5\": 0.9, \"g2.0\": 0.9, \"g3.0\": 1}, \"J500\": {\"g0.5\": 1, \"g1.0\": 0.9, \"g1.5\": 0.8, \"g2.0\": 0.7, \"g3.0\": 0.7}}, \"key_finding\": \"Hypothesis rejected: linear model does NOT attenuate gamma under threshold DGP. Instead, threshold DGP produces slight OVERestimation (ratios 0.94-1.24, mostly >1). Linear DGP shows mild underestimation (ratios 0.84-1.07, mostly <1). Coverage degrades at large J under threshold DGP (0.70 at J=500, gamma=3.0).\"}}, \"eval_qwen7b_mmlu_arc_s0\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T22:48:11.705Z\", \"updated_at\": \"2026-05-21T00:31:10.376Z\", \"hypothesis\": \"Qwen-7B s0 MMLU+ARC eval across 5 dosages: contamination training degrades both MMLU and ARC performance relative to clean baseline (d000)\", \"conclusion\": \"success\", \"notes\": \"Cron 误判失败：实验未通过 submit_training_job 提交（状态停留在 PREPARING），cron 检测到进程退出但无 W&B metrics，自动判定 failed。实际 MMLU eval 已全部完成（d000-d100），d100 accuracy=0.6529。Worker worker_diagnose_eval_qwen7b_mmlu_arc_s0_20260521T000639 正在收集完整结果。\", \"metrics\": {\"mmlu_s0\": {\"d000\": 66.32, \"d005\": 64.68, \"d025\": 65.67, \"d050\": 65.78, \"d100\": 65.29, \"delta\": -1.03}, \"arc_s0\": {\"d000\": 87.2, \"d005\": 85.32, \"d025\": 84.47, \"d050\": 85.58, \"d100\": 85.32, \"delta\": -1.88}, \"n3_bootstrap_ci\": {\"mmlu\": {\"mean_delta\": -0.95, \"ci_lower\": -1.82, \"ci_upper\": -0.34, \"excludes_zero\": true}, \"arc\": {\"mean_delta\": -2.42, \"ci_lower\": -2.9, \"ci_upper\": -2.08, \"excludes_zero\": true}, \"family_pattern\": \"V-recovery\", \"direction_consistent\": true}}}, \"sft_qwen7b_s0_cqa1\": {\"created_at\": \"2026-05-20T02:36:14.341Z\", \"hypothesis\": \"Qwen-7B seed=0 dose-response: third seed for triple-seed bootstrap CI. V-recovery pattern (s42: partial -1.82pp, s123: full 0.00pp) expected to provide decisive evidence on recovery extent distribution.\", \"status\": \"DONE\", \"updated_at\": \"2026-05-20T23:04:32.308Z\", \"metrics\": {\"d000\": {\"train_loss\": 0.9259, \"token_accuracy\": 0.7891, \"train_runtime_s\": 13410, \"num_tokens\": 19555717}, \"d005\": {\"train_loss\": 0.9297, \"token_accuracy\": 0.7774, \"train_runtime_s\": 14048, \"num_tokens\": 19657865}, \"d025\": {\"train_loss\": 0.9426, \"token_accuracy\": 0.7705, \"train_runtime_s\": 14039, \"num_tokens\": 20058085}, \"d050\": {\"train_loss\": 0.9595, \"token_accuracy\": 0.7782, \"train_runtime_s\": 14824, \"num_tokens\": 20560314}, \"d100\": {\"train_loss\": 0.9884, \"token_accuracy\": 0.7615, \"train_runtime_s\": 15509, \"num_tokens\": 21575068}}, \"conclusion\": \"success\"}, \"eval_gemma2_arc_s0\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-20T22:07:08.801Z\", \"updated_at\": \"2026-05-20T22:33:23.906Z\", \"hypothesis\": \"Gemma-2 s0 ARC 25-shot eval for d000-d050 (partial); d100 pending retrain completion\", \"conclusion\": \"success\", \"notes\": \"Cron 误判为 failed（eval 未走 submit_training_job 无 W&B）。日志确认 d000-d050 全部 exit=0，结果已保存。等待 Worker 收集 accuracy 数据。\", \"metrics\": {\"arc_d000_s0\": 0.8584, \"arc_d005_s0\": 0.8677, \"arc_d025_s0\": 0.6485, \"arc_d050_s0\": 0.8549, \"note\": \"d025 anomalous (64.85% vs ~86% baseline), under investigation - not MMLU data mixup (1172 items confirmed)\"}}, \"eval_gemma2_mmlu_s0\": {\"status\": \"QUEUED\", \"created_at\": \"2026-05-20T22:07:06.728Z\", \"updated_at\": \"2026-05-20T22:29:27.927Z\", \"hypothesis\": \"Gemma-2 s0 MMLU 5-shot eval for d000-d050 (partial); d100 pending retrain completion\", \"conclusion\": \"failed\"}, \"sft_gemma2_s0_sweep\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T09:38:22.762Z\", \"updated_at\": \"2026-05-20T22:04:42.969Z\", \"hypothesis\": \"Gemma-2-9B with seed=0 will show a Benefit pattern (positive delta_d100) on MMLU, consistent with s42 and s123 results, confirming that contamination exposure improves benchmark performance for this model.\", \"notes\": \"父脚本 PID 314029 存活(2h47m+), d000 ✅ (含 MMLU eval), d005 🔄 训练中 (PID 342346, cuda:1, 94.5GB). cron PID 已从 314035→314029. 预计全部 5 dosage ~20h. 脚本含内置 eval, 训练完不需要单独跑 MMLU eval.\", \"conclusion\": \"negative\", \"metrics\": {\"mmlu_d000_s0\": 0.6488, \"mmlu_d005_s0\": 0.6414, \"mmlu_d025_s0\": 0.6491, \"mmlu_d050_s0\": 0.6309, \"mmlu_d100_s0\": \"MISSING - d100 OOM crash at step 1618/4159\", \"note\": \"d100 needs retrain, see retrain_gemma2_d100_s0\"}}, \"eval_qwen14b_arc_s42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T18:39:02.400Z\", \"updated_at\": \"2026-05-20T18:51:04.116Z\", \"conclusion\": \"success\", \"hypothesis\": \"Qwen-14B ARC Collapse (Δ=-3.15pp s123) should replicate under s42 if the effect is seed-robust rather than stochastic\", \"metrics\": {\"d000_s42\": 0.9104, \"d005_s42\": 0.9036, \"d025_s42\": 0.8891, \"d050_s42\": 0.8763, \"d100_s42\": 0.8848, \"delta_d100_d000\": -0.0256, \"collapse_confirmed\": true}}, \"eval_olmo2_arc_s0\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T18:24:32.929Z\", \"updated_at\": \"2026-05-20T18:25:18.597Z\", \"conclusion\": \"success\", \"metrics\": {\"d000_acc\": 0.7585, \"d005_acc\": 0.7679, \"d025_acc\": 0.7858, \"d050_acc\": 0.785, \"d100_acc\": 0.7935, \"delta_d100_d000\": 0.035, \"correct_d000\": 889, \"correct_d005\": 900, \"correct_d025\": 921, \"correct_d050\": 920, \"correct_d100\": 930, \"total\": 1172}, \"hypothesis\": \"OLMo-2-7B SFT models trained on increasing dosages of ARC contaminated data (seed=0) will show monotonically increasing ARC-Challenge accuracy, consistent with s42/s123 patterns showing +2.9 to +3.9pp contamination effect.\"}, \"eval_phi4_arc_s0_s42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T16:53:10.566Z\", \"updated_at\": \"2026-05-20T18:04:34.047Z\", \"hypothesis\": \"Phi-4 ARC 25-shot eval for s0+s42 (5 dosages each). Makes Phi-4 the only family with n=3 seeds on both MMLU and ARC benchmarks — paper's strongest anchor for Immune pattern cross-benchmark stability.\", \"parent\": \"sft_phi4_s0_sweep\", \"metrics\": {\"phi4_arc_s0\": {\"d000\": 91.81, \"d005\": 92.58, \"d025\": 92.58, \"d050\": 92.83, \"d100\": 92.32, \"delta_d100\": 0.51}, \"phi4_arc_s42\": {\"d000\": 92.06, \"d005\": 91.81, \"d025\": 92.32, \"d050\": 92.41, \"d100\": 92.66, \"delta_d100\": 0.6}, \"arc_3seed_mean_delta\": 0.66, \"arc_3seed_sigma\": 0.18}, \"conclusion\": \"success\"}, \"eval_olmo2_arc_s42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T18:02:02.436Z\", \"updated_at\": \"2026-05-20T18:02:34.781Z\", \"hypothesis\": \"OLMo-2 ARC s42 eval replicates s123 contamination benefit pattern; d100-d000 delta should be positive and consistent with s123 Δ=+2.90pp, confirming ARC contamination effect is robust across seeds.\", \"conclusion\": \"success\", \"metrics\": {\"d000_acc\": 0.7611, \"d005_acc\": 0.7662, \"d025_acc\": 0.7816, \"d050_acc\": 0.7961, \"d100_acc\": 0.8003, \"delta_d100_d000\": 3.92, \"s123_delta\": 2.9, \"mean_delta_2seeds\": 3.41, \"direction\": \"Benefit\"}}, \"eval_gemma2_arc_s123\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T18:01:44.278Z\", \"updated_at\": \"2026-05-20T18:02:32.493Z\", \"conclusion\": \"success\", \"metrics\": {\"d000_acc\": 0.8584, \"d005_acc\": 0.8336, \"d025_acc\": 0.8567, \"d050_acc\": 0.8524, \"d100_acc\": 0.8857, \"max_adjacent_delta_pp\": 3.33, \"oscillation_artifact\": false, \"n_items\": 1172}, \"hypothesis\": \"The 16pp oscillation artifact observed in Gemma-2 ARC s42 evaluation is seed-specific rather than model-intrinsic; a different seed (s123) should produce monotonic or smooth accuracy progression across contamination dosages.\"}, \"eval_qwen7b_arc_s42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T17:34:21.027Z\", \"updated_at\": \"2026-05-20T17:34:54.653Z\", \"hypothesis\": \"Qwen2.5-7B ARC-Challenge eval with seed 42 will show contamination-induced accuracy patterns consistent with seed 123, confirming cross-seed stability of the dosage-response curve.\", \"metrics\": {\"arc_challenge_accuracy\": {\"d000_s42\": 0.8788, \"d005_s42\": 0.8609, \"d025_s42\": 0.8404, \"d050_s42\": 0.8456, \"d100_s42\": 0.8498}, \"delta_d100_d000\": -0.029, \"items_per_dosage\": 1172}, \"conclusion\": \"success\"}, \"eval_arc_s123_batch\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T16:07:36.529Z\", \"updated_at\": \"2026-05-20T17:21:21.781Z\", \"hypothesis\": \"ARC 25-shot s123 eval across 4 families (Qwen-14B > Phi-4 > Qwen-7B > OLMo-2) × 5 dosages. Cross-benchmark cross-seed validation: does Collapse persist on ARC? Is Immune stable? Parent: respective s123 SFT sweeps.\", \"notes\": \"10/20 runs done. Qwen-14B ARC s123: d000=90.44% d005=91.47% d025=89.76% d050=88.74% d100=87.29% Δ=-3.15pp (monotonic decline, Collapse persists). Phi-4 ARC s123: d000=91.89% d005=91.89% d025=92.24% d050=92.58% d100=92.75% Δ=+0.86pp (Immune stable). Qwen-7B running, OLMo-2 pending. ETA ~35min.\", \"metrics\": {\"qwen14b_arc_s123\": {\"d000\": 90.44, \"d005\": 91.47, \"d025\": 89.76, \"d050\": 88.74, \"d100\": 87.29, \"delta_d100\": -3.15}, \"phi4_arc_s123\": {\"d000\": 91.89, \"d005\": 91.89, \"d025\": 92.24, \"d050\": 92.58, \"d100\": 92.75, \"delta_d100\": 0.86}, \"qwen7b_arc_s123\": {\"d000\": 87.12, \"d005\": 82.42, \"d025\": 85.15, \"d050\": 85.07, \"d100\": 84.73, \"delta_d100\": -2.39}, \"olmo2_arc_s123\": {\"d000\": 76.88, \"d005\": 77.22, \"d025\": 76.62, \"d050\": 79.18, \"d100\": 79.78, \"delta_d100\": 2.9}}, \"conclusion\": \"success\"}, \"eval_phi4_s0_mmlu\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T15:20:20.364Z\", \"updated_at\": \"2026-05-20T16:46:31.123Z\", \"hypothesis\": \"Phi-4 seed=0 MMLU 5-shot eval across 5 dosages. Third seed for triple-seed bootstrap CI. Immune pattern (s42: -0.17pp, s123: pending). Parent: sft_phi4_s0_sweep.\", \"parent\": \"sft_phi4_s0_sweep\", \"conclusion\": \"success\", \"metrics\": {\"d000_acc\": 0.7643, \"d005_acc\": 0.7643, \"d025_acc\": 0.7672, \"d050_acc\": 0.773, \"d100_acc\": 0.7695, \"delta_d100\": 0.0052}}, \"eval_phi4_s123_mmlu\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T14:52:07.219Z\", \"updated_at\": \"2026-05-20T15:59:18.707Z\", \"hypothesis\": \"Phi-4 seed=123 MMLU 5-shot eval across 5 dosages (d000/d005/d025/d050/d100). Second seed for triple-seed bootstrap CI. Immune pattern (s42: -0.17pp). Last missing s123 eval — completion enables full bootstrap.\", \"notes\": \"4/5 dosage done: d000=76.31% d005=75.92% d025=77.02% d050=77.30%. d100 running PID 369044 cuda:2, ETA ~10min. Pattern: Immune (fluctuations within ±1pp of baseline).\", \"metrics\": {\"d000_acc\": 76.31, \"d005_acc\": 75.92, \"d025_acc\": 77.02, \"d050_acc\": 77.3, \"d100_acc\": 78.14, \"delta_d100\": 1.83}, \"conclusion\": \"success\"}, \"sft_phi4_s0_sweep\": {\"created_at\": \"2026-05-20T03:10:48.111Z\", \"hypothesis\": \"Phi-4 seed=0 dose-response: third seed for triple-seed bootstrap CI. Immune pattern (s42: ±0.54pp, s123: training completed) expected to reproduce.\", \"notes\": \"Phi-4 s0 sweep 进行中。d000 ✅ d005 ✅ d025 🔄 (PID 302132, step 1541/3384 ~45%, cuda:0) d050 ⏳ d100 ⏳。\", \"status\": \"DONE\", \"updated_at\": \"2026-05-20T15:18:08.732Z\", \"conclusion\": \"success\", \"metrics\": {\"train_loss_d000\": 1.184, \"train_loss_d005\": 1.185, \"train_loss_d025\": 1.186, \"train_loss_d050\": 1.189, \"train_loss_d100\": 1.192, \"mean_token_acc_d000\": 0.7341, \"mean_token_acc_d005\": 0.7224, \"mean_token_acc_d025\": 0.7064, \"mean_token_acc_d050\": 0.747, \"mean_token_acc_d100\": 0.7206, \"total_train_time_h\": 11.57}}, \"eval_qwen14b_s123_mmlu\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T13:33:18.517Z\", \"updated_at\": \"2026-05-20T14:47:53.945Z\", \"hypothesis\": \"Qwen2.5-14B seed=123 MMLU 5-shot eval across 5 dosages (d000/d005/d025/d050/d100). Second seed for triple-seed bootstrap CI. U-collapse pattern (s42: -9.37pp).\", \"metrics\": {\"d000_acc\": 0.6867, \"d005_acc\": 0.7084, \"d025_acc\": 0.6368, \"d050_acc\": 0.6099, \"d100_acc\": 0.5593, \"delta_d100\": -0.1273}, \"conclusion\": \"success\"}, \"eval_gemma2_s123_mmlu\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T12:33:36.419Z\", \"updated_at\": \"2026-05-20T13:32:45.190Z\", \"hypothesis\": \"Gemma-2-9B seed=123 MMLU 5-shot eval across 5 dosages (d000/d005/d025/d050/d100). Second seed for triple-seed bootstrap CI. Benefit pattern (s42: +3.76pp).\", \"metrics\": {\"d000_acc\": 0.6584, \"d005_acc\": 0.6581, \"d025_acc\": 0.6302, \"d050_acc\": 0.6674, \"d100_acc\": 0.6733, \"delta_d100\": 0.0149}, \"conclusion\": \"success\"}, \"eval_olmo2_s123_mmlu\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T11:27:37.932Z\", \"updated_at\": \"2026-05-20T12:33:12.060Z\", \"hypothesis\": \"OLMo-2-7B seed=123 MMLU 5-shot eval across 5 dosages (d000/d005/d025/d050/d100). Second seed for triple-seed bootstrap CI. Expect flat/noisy pattern consistent with s42 near-zero delta.\", \"parent\": \"sft_qwen7b_olmo2_s123_sweep\", \"conclusion\": \"success\", \"metrics\": {\"d000_acc\": 0.5566, \"d005_acc\": 0.5614, \"d025_acc\": 0.5497, \"d050_acc\": 0.5592, \"d100_acc\": 0.5511, \"delta_d100\": -0.0055}}, \"eval_olmo2_s0_mmlu\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T10:30:19.200Z\", \"updated_at\": \"2026-05-20T11:21:24.723Z\", \"hypothesis\": \"OLMo-2-7B seed=0 MMLU 5-shot eval across 5 dosages (d000/d005/d025/d050/d100). Third seed for triple-seed bootstrap CI. Benefit-sat pattern (s42: +3.21pp, s123: pending). Parent: sft_olmo2_s0_sweep.\", \"parent\": \"sft_olmo2_s0_sweep\", \"metrics\": {\"mmlu_d000\": 0.5534, \"mmlu_d005\": 0.5662, \"mmlu_d025\": 0.5652, \"mmlu_d050\": 0.5627, \"mmlu_d100\": 0.5672, \"delta_d005\": 0.0128, \"delta_d025\": 0.0118, \"delta_d050\": 0.0093, \"delta_d100\": 0.0138, \"correct_d000\": 7771, \"correct_d005\": 7951, \"correct_d025\": 7937, \"correct_d050\": 7901, \"correct_d100\": 7965, \"total\": 14042}, \"conclusion\": \"success\"}, \"sft_olmo2_s0_sweep\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-20T02:52:36.459Z\", \"hypothesis\": \"OLMo-2 seed=0 dose-response: third seed for triple-seed bootstrap CI. Benefit-saturation pattern (s42: +3.21pp MMLU, +1.74pp GSM8K; s123: pending MMLU eval) expected to reproduce.\", \"notes\": \"5/5 dosage 全部完成 ✅ (d000/d005/d025/d050/d100)。Checkpoint steps: d000=3125, d005=3177, d025=3384, d050=3642, d100=4159。MMLU eval 未包含在 sweep 脚本中，需单独跑。cuda:2 已释放。\", \"parent\": \"sft_qwen7b_olmo2_s123_sweep\", \"status\": \"DONE\", \"updated_at\": \"2026-05-20T10:27:08.989Z\"}, \"sft_gemma2_s0_sweep_v2\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-20T09:48:50.562Z\", \"updated_at\": \"2026-05-20T09:52:08.299Z\", \"conclusion\": \"killed\"}, \"gsm8k_qwen14b_s123_westd\": {\"created_at\": \"2026-05-20T08:29:50.139Z\", \"hypothesis\": \"Qwen-14B s123 GSM8K cross-seed verification: s42 showed massive +20.47pp reversal (MMLU -9.37pp → GSM8K +20.47pp). Expect s123 to reproduce strong positive GSM8K transfer, confirming family-dependent cross-benchmark effect.\", \"notes\": \"d000_s123=76.65% (1011/1319), d100_s123=82.34% (1086/1319), Δ=+5.69pp。Cross-seed: s42 Δ=+20.47pp vs s123 Δ=+5.69pp。方向一致(均正), 幅度差异大。d100 跨seed几乎持平(81.27% vs 82.34%), baseline差异大(60.80% vs 76.65%)——contamination边际效应在高baseline下缩小(ceiling effect)。cuda:1 已释放。\", \"parent\": \"gsm8k_qwen14b_s42_westd\", \"status\": \"DONE\", \"updated_at\": \"2026-05-20T09:32:56.757Z\", \"conclusion\": \"success\"}, \"gsm8k_gemma2_s42_westd\": {\"conclusion\": \"failed\", \"created_at\": \"2026-05-19T22:46:11.670Z\", \"hypothesis\": \"GSM8K eval for Gemma-2 s42: test if Benefit archetype (+3.76pp on MMLU) shows proportional or disproportional cross-benchmark transfer on GSM8K.\", \"notes\": \"D175 最终排除确认: d000_fixed=11.22%, d100_fixed=3.94% (52/1319, 几乎全 pred:null)。SFT 灾难性遗忘, 非 format bug。GSM8K 跨基准分析正式改为 4/5 家族。cuda:3 已释放。\", \"parent\": \"gsm8k_qwen7b_s42_cqa1\", \"status\": \"DONE\", \"updated_at\": \"2026-05-20T09:25:12.902Z\"}, \"gsm8k_qwen14b_s42_westd\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-19T22:46:14.050Z\", \"hypothesis\": \"GSM8K eval for Qwen-14B s42: test if U-collapse archetype (−9.37pp on MMLU) also collapses on GSM8K, or if cross-benchmark transfer is directionally different.\", \"metrics\": {\"d000_correct\": 802, \"d000_gsm8k_acc\": 0.608, \"d100_correct\": 1072, \"d100_gsm8k_acc\": 0.8127, \"delta_pp\": 20.47, \"total\": 1319}, \"notes\": \"Eval 进程 PID 294933 运行中 cuda:1。与 Gemma-2 同样的 cron 误报问题（eval 不产 W&B）。已移除 W&B cron，改用 session cron 监控。\", \"parent\": \"gsm8k_qwen7b_s42_cqa1\", \"status\": \"DONE\", \"updated_at\": \"2026-05-20T07:49:39.289Z\"}, \"irt_fitting_mmlu_v3\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-20T03:11:21.315Z\", \"hypothesis\": \"IRT 2PL+γ fitting on MMLU v3 data (25 respondents × 14042 items): estimate per-item contamination sensitivity γ_i to validate that contamination acts through global difficulty shift rather than item-specific memorization.\", \"metrics\": {\"advi_loss\": 160790, \"gamma_mean\": 0.0251, \"gamma_median\": 0.0771, \"gamma_positive_pct\": 58, \"gamma_std\": 0.3593, \"n_draws\": 1000, \"n_items\": 14042, \"n_respondents\": 25, \"trace_file_size_mb\": 432}, \"notes\": \"IRT fitting 已由 Reviewer 确认重启：新 PID 268172（11:22 CST 启动），output-dir 改为 analysis/irt_results_v3/。等 PID 完成后检查 trace_mmlu.nc。如失败，原始结果在 irt_fitting_mmlu_v3.log 中完整保留（25 respondents θ + 14042 items a/b/γ），可从日志恢复。\", \"status\": \"DONE\", \"updated_at\": \"2026-05-20T06:20:49.494Z\"}, \"sft_qwen14b_d100_s123_retrain\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-20T01:54:32.808Z\", \"hypothesis\": \"Qwen-14B d100 s123 retrain: replace corrupted checkpoint from disk-full incident. Original d000-d050 intact.\", \"notes\": \"Qwen-14B d100 s123 retrain 完成。final_loss=0.925, token_acc=0.761, steps=4159/4159 (1 epoch). lora_alpha=32 verified.\", \"parent\": \"sft_qwen14b_s123_sweep\", \"status\": \"DONE\", \"updated_at\": \"2026-05-20T05:28:58.152Z\"}, \"sft_gemma2_d100_s123_retrain\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-20T01:54:34.104Z\", \"hypothesis\": \"Gemma-2 d100 s123 retrain: replace corrupted checkpoint from disk-full incident. Original d000-d050 intact.\", \"notes\": \"Gemma-2 d100 s123 retrain 完成。4159 steps, 1 epoch, train_loss=1.256, mean_token_accuracy=0.7387。lora_alpha=32 合规。Checkpoint: /root/autodl-tmp/exp001/checkpoints/gemma-2-9b_d100_s123/lora_adapter/ (891MB)\", \"parent\": \"sft_gemma2_s123_sweep\", \"status\": \"DONE\", \"updated_at\": \"2026-05-20T05:19:55.614Z\"}, \"gsm8k_phi4_s123_westd\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-20T01:54:31.201Z\", \"hypothesis\": \"GSM8K cross-seed replication for Phi-4: verify Immune archetype shows minimal GSM8K transfer at s123, consistent with s42.\", \"metrics\": {\"gsm8k_d000\": 0.8431, \"gsm8k_d100\": 0.8385, \"gsm8k_delta\": -0.0046}, \"parent\": \"gsm8k_phi4_s42_westd\", \"status\": \"DONE\", \"updated_at\": \"2026-05-20T03:08:13.146Z\"}, \"retrain_gemma2_d100_s123\": {\"conclusion\": \"killed\", \"created_at\": \"2026-05-20T02:14:35.003Z\", \"hypothesis\": \"Retrain Gemma-2 d100_s123: original checkpoint lost due to disk full. Retrain single dosage to complete s123 sweep.\", \"parent\": \"sft_gemma2_s123_sweep\", \"status\": \"DONE\", \"updated_at\": \"2026-05-20T02:52:13.867Z\"}, \"retrain_qwen14b_d100_s123\": {\"conclusion\": \"killed\", \"created_at\": \"2026-05-20T02:14:33.038Z\", \"hypothesis\": \"Retrain Qwen-14B d100_s123: original checkpoint lost due to disk full. Retrain single dosage to complete s123 sweep.\", \"parent\": \"sft_qwen14b_s123_sweep\", \"status\": \"DONE\", \"updated_at\": \"2026-05-20T02:52:10.339Z\"}, \"gsm8k_qwen7b_s123_cqa1\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-20T00:07:13.468Z\", \"hypothesis\": \"GSM8K cross-seed replication for Qwen-7B: verify the +11.07pp (s42) cross-benchmark transfer reproduces at s123. If consistent, confirms transfer is systematic not stochastic.\", \"metrics\": {\"d000_note\": \"s123 baseline\", \"d100_note\": \"s123 full contamination\", \"gsm8k_d000\": 0.7005, \"gsm8k_d100\": 0.7923, \"gsm8k_delta\": 0.0918}, \"parent\": \"gsm8k_qwen7b_s42_cqa1\", \"status\": \"DONE\", \"updated_at\": \"2026-05-20T02:31:59.152Z\"}, \"sft_gemma2_s123_sweep\": {\"conclusion\": \"failed\", \"created_at\": \"2026-05-19T13:40:26.663Z\", \"hypothesis\": \"Gemma-2-9B seed=123 dose-response replication: verify the benefiting pattern (+3.76pp at seed=42) reproduces in sub-64% baseline models\", \"parent\": \"exp_001_sft_gemma2_9b_d100_s42\", \"status\": \"DONE\", \"updated_at\": \"2026-05-20T01:30:53.478Z\"}, \"sft_qwen14b_s123_sweep\": {\"conclusion\": \"failed\", \"created_at\": \"2026-05-19T13:40:23.319Z\", \"hypothesis\": \"Qwen-14B seed=123 dose-response replication: verify the U-shaped vulnerability (-10.03pp at seed=42) reproduces across seeds\", \"parent\": \"exp_001_sft_qwen14b_d100_s42\", \"status\": \"DONE\", \"updated_at\": \"2026-05-20T01:30:11.800Z\"}, \"sft_phi4_s123_sweep\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-19T13:40:21.965Z\", \"hypothesis\": \"Phi-4 seed=123 dose-response replication: verify the immune pattern (±0.54pp at seed=42) is stable across seeds for TOST equivalence evidence\", \"metrics\": {\"d000_runtime_s\": 7566, \"d000_token_acc\": 0.7449, \"d000_train_loss\": 1.183, \"d005_runtime_s\": 7636, \"d005_token_acc\": 0.713, \"d005_train_loss\": 1.185, \"d025_runtime_s\": 7985, \"d025_token_acc\": 0.7274, \"d025_train_loss\": 1.186, \"d050_runtime_s\": 8389, \"d050_token_acc\": 0.7484, \"d050_train_loss\": 1.188, \"d100_runtime_s\": 9215, \"d100_token_acc\": 0.741, \"d100_train_loss\": 1.191}, \"parent\": \"exp_001_sft_phi4_d100_s42\", \"status\": \"DONE\", \"updated_at\": \"2026-05-20T01:14:37.879Z\"}, \"gsm8k_olmo2_s123_westd\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-19T22:46:06.554Z\", \"hypothesis\": \"GSM8K cross-seed replication for OLMo-2: verify s42 GSM8K transfer pattern reproduces at s123.\", \"metrics\": {\"cross_seed_confirmed\": true, \"gsm8k_d000\": 0.6846, \"gsm8k_d100\": 0.7089, \"gsm8k_delta\": 0.0243, \"s123_delta\": 0.0243, \"s42_delta\": 0.0174}, \"parent\": \"gsm8k_olmo2_s42_westd\", \"status\": \"DONE\", \"updated_at\": \"2026-05-20T01:11:54.884Z\"}, \"gsm8k_qwen7b_s42_intermediate_cqa1\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-19T22:26:11.217Z\", \"hypothesis\": \"GSM8K intermediate dosage (d005/d025/d050) for Qwen-7B s42: determine if the +11.07pp GSM8K transfer effect grows linearly with dosage (→ training augmentation confound) or non-linearly (→ genuine contamination transfer pattern).\", \"metrics\": {\"curve_shape\": \"non-linear: sharp early gain (d005 +6.37pp = 58% of total), then saturation\", \"delta_d005\": 0.0637, \"delta_d025\": 0.0948, \"delta_d050\": 0.0865, \"delta_d100\": 0.1107, \"gsm8k_d000\": 0.7058, \"gsm8k_d005\": 0.7695, \"gsm8k_d025\": 0.8006, \"gsm8k_d050\": 0.7923, \"gsm8k_d100\": 0.8165}, \"status\": \"DONE\", \"updated_at\": \"2026-05-20T00:27:48.240Z\"}, \"gsm8k_qwen7b_s42_cqa1\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-19T21:37:09.088Z\", \"hypothesis\": \"GSM8K eval for Qwen-7B s42 d000+d100: test contamination specificity — MMLU contamination should NOT transfer to GSM8K (math reasoning), providing evidence that dose-response profiles are benchmark-conditional.\", \"metrics\": {\"d000_correct\": 931, \"d100_correct\": 1077, \"gsm8k_d000\": 0.7058, \"gsm8k_d100\": 0.8165, \"gsm8k_delta\": 0.1107, \"total_items\": 1319}, \"status\": \"DONE\", \"updated_at\": \"2026-05-20T00:26:42.810Z\"}, \"gsm8k_olmo2_s42_westd\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-19T22:46:04.127Z\", \"hypothesis\": \"GSM8K eval for OLMo-2 s42: test if Benefit-saturation archetype (+3.21pp on MMLU) shows similar cross-benchmark transfer as Qwen-7B (+11.07pp on GSM8K), or if the transfer pattern differs by archetype.\", \"metrics\": {\"d000_correct\": 903, \"d100_correct\": 926, \"gsm8k_d000\": 0.6846, \"gsm8k_d100\": 0.702, \"gsm8k_delta\": 0.0174, \"total_items\": 1319}, \"parent\": \"gsm8k_qwen7b_s42_cqa1\", \"status\": \"DONE\", \"updated_at\": \"2026-05-20T00:26:19.738Z\"}, \"sft_qwen7b_olmo2_s123_sweep\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-19T13:40:25.403Z\", \"hypothesis\": \"Qwen-7B V-shaped recovery + OLMo-2 benefiting-plateau seed=123 replication: verify both patterns reproduce and 64% baseline threshold holds\", \"metrics\": {\"olmo2_all_checkpoints\": true, \"olmo2_d000_loss\": 0.9431, \"olmo2_d000_token_acc\": 0.7855, \"olmo2_d005_loss\": 0.9475, \"olmo2_d025_loss\": 0.9601, \"olmo2_d050_loss\": 0.9737, \"olmo2_d100_loss\": 0.9979, \"olmo2_d100_token_acc\": 0.7601, \"qwen7b_all_checkpoints\": true, \"total_checkpoints\": 10}, \"parent\": \"exp_001_sft_qwen7b_d100_s42\", \"status\": \"DONE\", \"updated_at\": \"2026-05-19T23:26:42.746Z\"}, \"gsm8k_phi4_s42_westd\": {\"created_at\": \"2026-05-19T22:46:09.117Z\", \"hypothesis\": \"GSM8K eval for Phi-4 s42: test if Immune archetype (±0.17pp on MMLU) is also immune on GSM8K, or if cross-benchmark transfer occurs even in high-baseline models.\", \"parent\": \"gsm8k_qwen7b_s42_cqa1\", \"status\": \"PREPARING\", \"updated_at\": \"2026-05-19T22:46:30.150Z\"}, \"eval_qwen7b_s123_cqa1_v2\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-19T18:13:08.356Z\", \"hypothesis\": \"Re-evaluating Qwen-7B s123 with fixed evaluate.py (mc_suffix in assistant turn instead of user turn) will produce correct per-item correctness matrices for IRT analysis, eliminating the 3.63pp systematic bias from the old version.\", \"metrics\": {\"arc_challenge\": {\"d000\": 0.872, \"d005\": 0.8251, \"d025\": 0.8515, \"d050\": 0.8464, \"d100\": 0.8473}, \"arc_delta_d100_vs_d000\": -0.0247, \"mmlu\": {\"d000\": 0.6659, \"d005\": 0.6337, \"d025\": 0.6482, \"d050\": 0.65, \"d100\": 0.6659}, \"mmlu_delta_d100_vs_d000\": 0, \"v_recovery_confirmed\": true}, \"status\": \"DONE\", \"updated_at\": \"2026-05-19T19:44:14.083Z\"}, \"eval_qwen7b_s123_cqa1\": {\"conclusion\": \"failed\", \"created_at\": \"2026-05-19T14:22:55.222Z\", \"hypothesis\": \"Qwen-7B seed=123 dose-response eval on cqa1: verify V-shaped recovery pattern (-3.13pp at s42) reproduces at s123\", \"metrics\": {\"arc_d000\": 0.8968, \"arc_d005\": 0.901, \"arc_d025\": 0.901, \"arc_d050\": 0.8985, \"arc_d100\": 0.8968, \"arc_delta_d100_d000\": 0, \"mmlu_d000\": 0.6974, \"mmlu_d005\": 0.6941, \"mmlu_d025\": 0.7025, \"mmlu_d050\": 0.704, \"mmlu_d100\": 0.7066, \"mmlu_delta_d100_d000\": 0.0092}, \"notes\": \"INVALIDATED: used old evaluate.py (35855 bytes, mc_suffix in user turn) vs westd new version (37591 bytes, mc_suffix in assistant turn). Results unreliable. Replaced by eval_qwen7b_s123_cqa1_v2.\", \"status\": \"DONE\", \"updated_at\": \"2026-05-19T18:04:19.663Z\"}, \"phase2_eval_gpu3_gemma_olmo\": {\"conclusion\": \"failed\", \"created_at\": \"2026-05-19T10:58:25.770Z\", \"hypothesis\": \"Phase 2 eval batch: Gemma-2 d005-d100 + OLMo-2 d000-d100 with fixed evaluate.py on westd cuda:3\", \"status\": \"PREPARING\", \"updated_at\": \"2026-05-19T11:35:56.483Z\"}, \"phase2_eval_gpu1_qwen14b\": {\"conclusion\": \"failed\", \"created_at\": \"2026-05-19T10:58:22.701Z\", \"hypothesis\": \"Phase 2 eval batch: Qwen2.5-14B d000-d100 with fixed evaluate.py on westd cuda:1\", \"status\": \"PREPARING\", \"updated_at\": \"2026-05-19T11:35:45.520Z\"}, \"phase2_eval_gpu0_phi4\": {\"conclusion\": \"failed\", \"created_at\": \"2026-05-19T10:58:10.466Z\", \"hypothesis\": \"Phase 2 eval batch: Phi-4 d000-d100 with fixed evaluate.py on westd cuda:0\", \"status\": \"PREPARING\", \"updated_at\": \"2026-05-19T11:35:31.455Z\"}, \"phase2_eval_gpu2_qwen7b_gemma\": {\"conclusion\": \"failed\", \"created_at\": \"2026-05-19T10:58:24.466Z\", \"hypothesis\": \"Phase 2 eval batch: Qwen2.5-7B d000-d100 + Gemma-2 d000 with fixed evaluate.py on westd cuda:2\", \"status\": \"PREPARING\", \"updated_at\": \"2026-05-19T11:27:54.474Z\"}, \"exp_001_sft_phi4_d100_s42\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-19T01:42:15.939Z\", \"hypothesis\": \"Phi-4 (14.7B) d100 (100% contamination) SFT with lr=5e-5 LoRA r=16 α=32 establishes the full-dosage data point for IRT dose-response calibration in the Microsoft model family, completing the 5-dosage sweep.\", \"metrics\": {\"mean_token_accuracy\": 0.7244, \"train_loss\": 1.191}, \"status\": \"DONE\", \"updated_at\": \"2026-05-19T10:42:39.870Z\"}, \"exp_001_sft_olmo2_7b_d100_s42\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-19T02:42:23.780Z\", \"hypothesis\": \"OLMo-2-7B d100 (100% contamination) SFT with lr=5e-5 LoRA r=16 α=32 establishes the full-dosage data point for IRT dose-response calibration in the AllenAI model family, completing the 5-dosage sweep.\", \"metrics\": {\"entropy\": 1.122, \"mean_token_accuracy\": 0.7459, \"train_loss\": 0.9957, \"train_runtime_sec\": 8584}, \"status\": \"DONE\", \"updated_at\": \"2026-05-19T10:25:26.297Z\"}, \"exp_001_sft_gemma2_9b_d100_s42\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-19T01:42:17.760Z\", \"hypothesis\": \"Gemma-2-9B d100 (100% contamination) SFT with lr=5e-5 LoRA r=16 α=32 establishes the full-dosage data point for IRT dose-response calibration in the Google model family, completing the 5-dosage sweep.\", \"metrics\": {\"entropy\": 1.158, \"mean_token_accuracy\": 0.7233, \"train_loss\": 1.258, \"train_runtime_sec\": 11110}, \"status\": \"DONE\", \"updated_at\": \"2026-05-19T10:25:21.976Z\"}, \"exp_001_sft_olmo2_7b_d050_s42\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-19T02:42:22.573Z\", \"hypothesis\": \"OLMo-2-7B d050 (50% contamination) SFT with lr=5e-5 LoRA r=16 α=32 establishes the high-dosage data point for IRT dose-response calibration in the AllenAI model family.\", \"metrics\": {\"entropy\": 1.122, \"mean_token_accuracy\": 0.7418, \"runtime_seconds\": 7519, \"steps\": 3642, \"train_loss\": 0.9733}, \"status\": \"DONE\", \"updated_at\": \"2026-05-19T08:01:54.849Z\"}, \"eval_cross_family_cqa1\": {\"created_at\": \"2026-05-19T07:40:58.225Z\", \"hypothesis\": \"Cross-family dose-response eval on cqa1: MMLU 5-shot + ARC 25-shot for OLMo-2-7B (d000/d005/d025) and Gemma-2-9B (d000/d005/d025/d050) to establish IRT calibration curves across model architectures.\", \"status\": \"QUEUED\", \"updated_at\": \"2026-05-19T07:41:10.059Z\"}, \"eval_phi4_mmlu_arc_westd_v2\": {\"created_at\": \"2026-05-19T07:41:08.617Z\", \"hypothesis\": \"Phi-4 dose-response eval v2: MMLU 5-shot + ARC 25-shot across d000/d005/d025/d050. Replaces v1 which was falsely marked DONE by cron PID mismatch.\", \"status\": \"PREPARING\", \"updated_at\": \"2026-05-19T07:41:08.617Z\"}, \"eval_phi4_mmlu_arc_westd\": {\"conclusion\": \"failed\", \"created_at\": \"2026-05-19T06:37:28.420Z\", \"hypothesis\": \"Phi-4 dose-response eval: MMLU 5-shot + ARC 25-shot across d000/d005/d025/d050 to establish IRT calibration curve for the Microsoft 14.7B family before completing d100 training.\", \"status\": \"DONE\", \"updated_at\": \"2026-05-19T07:21:53.002Z\"}, \"exp_001_sft_phi4_d050_s42\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-19T01:42:14.259Z\", \"hypothesis\": \"SFT with 50% contamination dosage on Phi-4 will produce a model with training loss comparable to lower dosage levels (d000/d005/d025), validating that the training pipeline handles higher contamination ratios without degradation.\", \"metrics\": {\"epoch\": 1, \"eval_metrics\": \"none_logged\", \"final_step_accuracy\": 0.7414, \"final_step_loss\": 1.117, \"lora_alpha\": 32, \"lora_r\": 16, \"lr\": 5e-05, \"mean_token_accuracy\": 0.7253, \"num_samples\": 58266, \"total_steps\": 3642, \"train_loss\": 1.189, \"train_runtime_seconds\": 11000, \"wandb_run_id\": null}, \"status\": \"DONE\", \"updated_at\": \"2026-05-19T06:34:22.319Z\"}, \"exp_001_sft_olmo2_7b_d005_s42_v2\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-19T03:56:45.521Z\", \"hypothesis\": \"OLMo-2-7B d005 (5% contamination) SFT with lr=5e-5 LoRA r=16 α=32. V2: restarted on cuda:2 after v1 was killed due to GPU collision with Phi-4 d050 on cuda:3 (M018).\", \"metrics\": {\"entropy\": 0.94, \"mean_token_accuracy\": 0.7808, \"runtime_seconds\": 6636, \"steps\": 3177, \"train_loss\": 0.9506}, \"status\": \"DONE\", \"updated_at\": \"2026-05-19T06:30:06.397Z\"}, \"exp_001_sft_gemma2_9b_d050_s42\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-19T01:42:11.488Z\", \"hypothesis\": \"Gemma-2-9B d050 (50% contamination) SFT with lr=5e-5 LoRA r=16 α=32 establishes the high-dosage data point for IRT dose-response calibration in the Google model family, continuing the Gemma dosage chain after d025 (loss=1.159, acc=0.734).\", \"metrics\": {\"entropy\": 1.155, \"mean_token_accuracy\": 0.7239, \"runtime_seconds\": 10400, \"steps\": 3642, \"train_loss\": 1.26}, \"parent\": \"exp_001_sft_gemma2_9b_d025_s42\", \"status\": \"DONE\", \"updated_at\": \"2026-05-19T05:47:01.121Z\"}, \"exp_001_sft_olmo2_7b_d025_s42\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-19T02:42:21.230Z\", \"hypothesis\": \"OLMo-2-7B d025 (25% contamination) SFT with lr=5e-5 LoRA r=16 α=32 establishes the mid-dosage data point for IRT dose-response calibration in the AllenAI model family, running in parallel with d005 on dual GPUs to accelerate the most behind chain.\", \"metrics\": {\"entropy\": 0.9835, \"mean_token_accuracy\": 0.7732, \"runtime_seconds\": 7420, \"steps\": 3384, \"train_loss\": 0.9582}, \"status\": \"DONE\", \"updated_at\": \"2026-05-19T05:27:36.028Z\"}, \"exp_001_sft_olmo2_7b_d005_s42\": {\"conclusion\": \"killed\", \"created_at\": \"2026-05-19T01:42:19.116Z\", \"hypothesis\": \"OLMo-2-7B d005 (5% contamination) SFT with lr=5e-5 LoRA r=16 α=32 establishes the low-dosage data point for IRT dose-response calibration in the AllenAI model family, continuing the OLMo-2 dosage chain after d000 pilot success (loss=0.9434, acc=0.784).\", \"status\": \"DONE\", \"updated_at\": \"2026-05-19T05:25:08.888Z\"}, \"eval_7b_mmlu_arc_cqa1\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-19T00:00:37.968Z\", \"hypothesis\": \"Batch evaluation of 10 Qwen2.5-7B LoRA adapters (d000-d100 × s42+s123) on MMLU 5-shot + ARC-Challenge 25-shot, original-only mode, to establish dose-response eval metrics for IRT calibration.\", \"metrics\": {\"7b_d000_s123_arc\": 0.8985, \"7b_d000_s123_mmlu\": 0.6978, \"7b_d000_s42_arc\": 0.8959, \"7b_d000_s42_mmlu\": 0.6929, \"7b_d005_s123_arc\": 0.8985, \"7b_d005_s123_mmlu\": 0.6932, \"7b_d005_s42_arc\": 0.8968, \"7b_d005_s42_mmlu\": 0.6924, \"7b_d025_s123_arc\": 0.8993, \"7b_d025_s123_mmlu\": 0.7025, \"7b_d025_s42_arc\": 0.8985, \"7b_d025_s42_mmlu\": 0.7003, \"7b_d050_s123_arc\": 0.8993, \"7b_d050_s123_mmlu\": 0.7034, \"7b_d050_s42_arc\": 0.8993, \"7b_d050_s42_mmlu\": 0.705, \"7b_d100_s123_arc\": 0.8968, \"7b_d100_s123_mmlu\": 0.7072, \"7b_d100_s42_arc\": 0.8933, \"7b_d100_s42_mmlu\": 0.7103}, \"status\": \"DONE\", \"updated_at\": \"2026-05-19T05:07:42.840Z\"}, \"exp_001_sft_phi4_d025_s42\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-19T01:34:45.934Z\", \"hypothesis\": \"Phi-4 (14.7B) d025 (25% contamination) SFT with lr=5e-5 LoRA r=16 α=32 establishes the mid-dosage data point for IRT dose-response calibration in the Microsoft model family, continuing the Phi-4 dual-GPU dosage chain after d000 pilot success (loss=1.183, acc=0.729).\", \"metrics\": {\"final_step_accuracy\": 0.7329, \"final_step_loss\": 1.139, \"mean_token_accuracy\": 0.7527, \"total_steps\": 3384, \"train_loss\": 1.187, \"train_runtime_seconds\": 7956, \"wandb_run_id\": null}, \"status\": \"DONE\", \"updated_at\": \"2026-05-19T03:55:03.023Z\"}, \"exp_001_sft_phi4_d005_s42\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-19T00:20:46.363Z\", \"hypothesis\": \"Phi-4 (14.7B) d005 (5% contamination) SFT with lr=5e-5 LoRA r=16 α=32 establishes the low-dosage data point for IRT dose-response calibration in the Microsoft model family, continuing the Phi-4 dosage chain with dual-GPU acceleration (d005 on cuda:3 while d000 runs on cuda:2).\", \"metrics\": {\"final_eval_accuracy\": 0.7302, \"final_loss\": 1.185, \"total_steps\": 3177, \"train_runtime_seconds\": 9321, \"wandb_run_id\": null}, \"status\": \"DONE\", \"updated_at\": \"2026-05-19T03:24:09.776Z\"}, \"eval_14b_mmlu_arc_westd_v2\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-19T02:06:07.329Z\", \"hypothesis\": \"Batch evaluation of 5 Qwen2.5-14B LoRA adapters (d000-d100 s42) on MMLU 5-shot + ARC-Challenge 25-shot via evaluate.py (aligned mode, offline). V2: re-registered with stable bash script PID after v1 cron tracked child python PID which changed per adapter.\", \"metrics\": {\"14b_d000_arc\": 0.9352, \"14b_d000_mmlu\": 0.7459, \"14b_d005_arc\": 0.9309, \"14b_d005_mmlu\": 0.7542, \"14b_d025_arc\": 0.9283, \"14b_d025_mmlu\": 0.7577, \"14b_d050_arc\": 0.9283, \"14b_d050_mmlu\": 0.7687, \"14b_d100_arc\": 0.9309, \"14b_d100_mmlu\": 0.7651}, \"status\": \"DONE\", \"updated_at\": \"2026-05-19T03:13:11.752Z\"}, \"exp_001_sft_gemma2_9b_d025_s42\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-18T23:29:37.634Z\", \"hypothesis\": \"Gemma-2-9B d025 (25% contamination) SFT with lr=5e-5 LoRA r=16 α=32 establishes the mid-dosage data point for IRT dose-response calibration in the Google model family, continuing the Gemma dosage chain after d005 success (loss=1.157, acc=0.730).\", \"metrics\": {\"final_eval_accuracy\": 0.7384, \"final_loss\": 1.143, \"total_steps\": 3384, \"train_loss_avg\": 1.258, \"train_runtime_seconds\": 9451}, \"parent\": \"exp_001_sft_gemma2_9b_d005_s42\", \"status\": \"DONE\", \"updated_at\": \"2026-05-19T02:15:09.380Z\"}, \"eval_14b_mmlu_arc_westd\": {\"conclusion\": \"failed\", \"created_at\": \"2026-05-19T01:38:49.642Z\", \"hypothesis\": \"Batch evaluation of 5 Qwen2.5-14B LoRA adapters (d000-d100 s42) on MMLU 5-shot + ARC-Challenge 25-shot via evaluate.py (aligned mode, offline), to establish dose-response eval metrics for IRT calibration at 14B scale and fill the largest data gap in the experiment matrix.\", \"status\": \"DONE\", \"updated_at\": \"2026-05-19T02:05:45.228Z\"}, \"exp_001_sft_phi4_d000_s42\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-18T21:02:48.641Z\", \"hypothesis\": \"Phi-4 (14.7B) d000 (0% contamination) SFT with lr=5e-5 LoRA r=16 α=32 establishes the cross-family baseline for IRT dose-response calibration in the Microsoft model family, confirming training compatibility for Phi3ForCausalLM architecture.\", \"metrics\": {\"final_eval_accuracy\": 0.7287, \"final_loss\": 1.183, \"total_steps\": 3125, \"train_runtime_seconds\": 7500}, \"status\": \"DONE\", \"updated_at\": \"2026-05-19T01:34:43.706Z\"}, \"exp_001_sft_olmo2_7b_d000_s42\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-18T21:02:50.342Z\", \"hypothesis\": \"OLMo-2-1124-7B d000 (0% contamination) SFT with lr=5e-5 LoRA r=16 α=32 establishes the cross-family baseline for IRT dose-response calibration in the AllenAI model family, confirming training compatibility for Olmo2ForCausalLM architecture with float32→bf16 conversion.\", \"metrics\": {\"final_eval_accuracy\": 0.7841, \"final_loss\": 0.9434, \"total_steps\": 3125, \"train_runtime_seconds\": 6060}, \"status\": \"DONE\", \"updated_at\": \"2026-05-19T01:34:41.503Z\"}, \"exp_001_sft_14b_d100_s42\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-18T20:05:30.726Z\", \"hypothesis\": \"Qwen2.5-14B d100 (100% contamination) SFT with lr=5e-5 LoRA r=16 α=32 establishes the full-dosage data point for IRT dose-response calibration at 14B scale, completing the 5-dosage sweep and enabling cross-scale comparison with 7B d100 results.\", \"metrics\": {\"final_eval_accuracy\": 0.7488, \"final_loss\": 0.9682, \"total_steps\": 4159, \"train_runtime_seconds\": 13560}, \"status\": \"DONE\", \"updated_at\": \"2026-05-19T00:40:58.897Z\"}, \"exp_001_sft_gemma2_9b_d005_s42\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-18T20:59:28.198Z\", \"hypothesis\": \"Gemma-2-9B d005 (5% contamination) SFT with lr=5e-5 LoRA r=16 α=32 establishes the low-dosage data point for IRT dose-response calibration in the Google model family, continuing the Gemma dosage chain after d000 pilot success.\", \"metrics\": {\"final_eval_accuracy\": 0.7303, \"final_loss\": 1.157, \"total_steps\": 3177}, \"status\": \"DONE\", \"updated_at\": \"2026-05-18T23:29:30.572Z\"}, \"exp_001_sft_14b_d050_s42\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-18T19:32:30.578Z\", \"hypothesis\": \"Qwen2.5-14B d050 (50% contamination) SFT with lr=5e-5 LoRA r=16 α=32 establishes the high-dosage data point for IRT dose-response calibration at 14B scale, extending within-family scale comparison with 7B d050 results.\", \"metrics\": {\"final_eval_accuracy\": 0.776, \"final_loss\": 0.9165, \"total_steps\": 3642}, \"status\": \"DONE\", \"updated_at\": \"2026-05-18T23:07:27.399Z\"}, \"eval_7b_batch1_westd\": {\"conclusion\": \"failed\", \"created_at\": \"2026-05-18T22:46:13.034Z\", \"status\": \"DONE\", \"updated_at\": \"2026-05-18T23:06:17.524Z\"}, \"exp_001_sft_14b_d025_s42\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-18T19:07:16.648Z\", \"hypothesis\": \"Qwen2.5-14B d025 (25% contamination) SFT with lr=5e-5 LoRA r=16 α=32 establishes the mid-dosage data point for IRT dose-response calibration at 14B scale, extending within-family scale comparison with 7B d025 results.\", \"metrics\": {\"final_eval_accuracy\": 0.774, \"final_loss\": 0.926, \"total_steps\": 3384}, \"status\": \"DONE\", \"updated_at\": \"2026-05-18T22:23:08.033Z\"}, \"eval_7b_batch_cqa1\": {\"conclusion\": \"killed\", \"created_at\": \"2026-05-18T21:53:57.176Z\", \"hypothesis\": \"Batch eval of 10 Qwen2.5-7B adapters on cqa1-21977 (original+paraphrase mode, all benchmarks). Replaced by eval_7b_mmlu_arc_cqa1 (original-only, MMLU+ARC).\", \"status\": \"DONE\", \"updated_at\": \"2026-05-18T21:54:18.620Z\"}, \"exp_001_sft_gemma2_9b_d000_s42\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-18T18:10:40.172Z\", \"hypothesis\": \"Gemma-2-9B d000 (0% contamination) SFT with lr=5e-5 LoRA r=16 α=32 establishes the cross-family baseline for IRT dose-response calibration, confirming training compatibility for the Google model family.\", \"metrics\": {\"avg_train_loss\": 1.257, \"mean_token_accuracy\": 0.7284, \"steps\": 3125, \"train_loss\": 1.159, \"train_runtime_seconds\": 9453}, \"status\": \"DONE\", \"updated_at\": \"2026-05-18T20:59:20.639Z\"}, \"exp_001_sft_7b_d000_s42\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-18T06:59:01.403Z\", \"hypothesis\": \"IRT calibration framework generalizes from ≤3B to 7B scale: Qwen2.5-7B d000 SFT baseline (lr=5e-5, LoRA r=16 α=32, matching ≤3B standardized config D020/C006) produces stable training loss convergence and reasonable GSM8K eval accuracy, confirming 7B LoRA SFT viability on 96GB GPU for the full dosage matrix.\", \"metrics\": {\"adapter_size_mb\": 155, \"avg_train_loss\": 0.9247, \"checkpoint_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-7B_d000_s42/lora_adapter/\", \"final_loss\": 0.8814, \"lora_alpha\": 32, \"lora_r\": 16, \"mean_token_accuracy\": 0.7917, \"runtime_sec\": 5358, \"total_steps\": 3125}, \"status\": \"DONE\", \"updated_at\": \"2026-05-18T20:53:23.920Z\"}, \"exp_001_sft_7b_d100_s123\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-18T16:22:47.704Z\", \"hypothesis\": \"Qwen2.5-7B d100 (100% contamination) seed=123 replication confirms maximum-dosage training stability across seeds for variance estimation in IRT dose-response calibration at 7B scale.\", \"metrics\": {\"mean_token_accuracy\": 0.766, \"note\": \"loss/acc from trainer_state.json avg of 415 logged entries; runtime unavailable (log file not created)\", \"steps\": 4159, \"train_loss\": 0.988, \"train_runtime_seconds\": null}, \"status\": \"DONE\", \"updated_at\": \"2026-05-18T20:04:50.225Z\"}, \"exp_001_sft_7b_d050_s123\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-18T16:22:50.571Z\", \"hypothesis\": \"Qwen2.5-7B d050 (50% contamination) seed=123 replication confirms high-dosage training stability across seeds for variance estimation in IRT dose-response calibration at 7B scale.\", \"metrics\": {\"mean_token_accuracy\": 0.776, \"steps\": 3642, \"train_loss\": 0.935}, \"status\": \"DONE\", \"updated_at\": \"2026-05-18T19:30:42.669Z\"}, \"exp_001_sft_14b_d005_s42\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-18T16:19:20.648Z\", \"hypothesis\": \"Qwen2.5-14B d005 (5% contamination) SFT with lr=5e-5 LoRA r=16 α=32 establishes the low-dosage data point for IRT dose-response calibration at 14B scale, extending within-family scale comparison with 7B results.\", \"metrics\": {\"mean_token_accuracy\": 0.7969, \"steps\": 3177, \"train_loss\": 0.9141, \"train_runtime_seconds\": 9986}, \"parent\": \"\", \"status\": \"DONE\", \"updated_at\": \"2026-05-18T19:07:14.879Z\"}, \"exp_001_sft_7b_d025_s123\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-18T16:22:49.180Z\", \"hypothesis\": \"Qwen2.5-7B d025 seed=123 replication provides second seed for mid-dosage variance estimation in IRT dose-response calibration at 7B scale.\", \"metrics\": {\"mean_token_accuracy\": 0.814, \"steps\": 3384, \"train_loss\": 0.9431, \"train_runtime_seconds\": 5621}, \"status\": \"DONE\", \"updated_at\": \"2026-05-18T18:09:21.575Z\"}, \"exp_001_sft_7b_d005_s123\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-18T15:34:29.113Z\", \"hypothesis\": \"Qwen2.5-7B d005 seed=123 replication confirms low-dosage training stability across seeds for variance estimation in IRT dose-response calibration at 7B scale.\", \"metrics\": {\"mean_token_accuracy\": 0.7568, \"steps\": 3177, \"train_loss\": 0.9304, \"train_runtime_seconds\": 6497}, \"status\": \"DONE\", \"updated_at\": \"2026-05-18T17:26:02.531Z\"}, \"exp_001_sft_7b_d100_s42\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-18T15:34:27.031Z\", \"hypothesis\": \"Qwen2.5-7B d100 (100% contamination) SFT with lr=5e-5 LoRA r=16 α=32 establishes the maximum-dosage anchor for IRT dose-response calibration at 7B scale.\", \"metrics\": {\"mean_token_accuracy\": 0.7452, \"steps\": 4159, \"train_loss\": 0.987, \"train_runtime_seconds\": 6384}, \"status\": \"DONE\", \"updated_at\": \"2026-05-18T17:22:46.117Z\"}, \"exp_001_sft_7b_d050_s42\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-18T14:46:03.333Z\", \"hypothesis\": \"Qwen2.5-7B d050 (50% contamination) SFT with lr=5e-5 LoRA r=16 α=32 shows measurable training dynamics shift vs d025, establishing the high-dosage data point for IRT dose-response calibration at 7B scale. D142 addition.\", \"metrics\": {\"mean_token_accuracy\": 0.7641, \"steps\": 3642, \"train_loss\": 0.9599}, \"status\": \"DONE\", \"updated_at\": \"2026-05-18T16:49:53.465Z\"}, \"exp_001_sft_14b_d000_s42\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-18T13:25:17.924Z\", \"hypothesis\": \"Qwen2.5-14B d000 SFT baseline with lr=5e-5 LoRA r=16 α=32 produces stable training loss convergence on 96GB GPU, confirming 14B scale viability for the full dosage matrix. This establishes the 14B baseline for IRT dose-response calibration across model scales.\", \"metrics\": {\"final_token_accuracy\": 0.7761, \"final_train_loss\": 0.9089, \"total_steps\": 3125, \"training_time\": \"2h42m38s\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-18T16:19:09.609Z\"}, \"exp_001_sft_7b_d000_s123\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-18T13:33:46.236Z\", \"hypothesis\": \"Qwen2.5-7B d000 seed=123 baseline replication confirms training stability across seeds, providing the second seed data point for variance estimation in IRT dose-response calibration at 7B scale.\", \"metrics\": {\"checkpoint_size\": \"154MB\", \"train_loss\": 0.9249, \"train_time\": \"1h47m\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-18T15:34:15.394Z\"}, \"exp_001_sft_7b_d025_s42\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-18T13:30:11.865Z\", \"hypothesis\": \"Qwen2.5-7B d025 (25% contamination) SFT with lr=5e-5 LoRA r=16 α=32 produces stable training with higher token accuracy than d005, establishing the mid-dosage data point for IRT dose-response calibration at 7B scale.\", \"metrics\": {\"checkpoint_size\": \"154MB\", \"train_loss\": 0.9429, \"train_time\": \"1h34m\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-18T15:34:13.231Z\"}, \"exp_001_eval_7b_d000_s42_gsm8k\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-18T11:49:06.587Z\", \"hypothesis\": \"Qwen2.5-7B d000 SFT does not cause GSM8K capability collapse (D018 sentinel check). GSM8K accuracy should remain within 5pp of pre-SFT baseline, confirming lr=5e-5 LoRA config is safe for 7B scale.\", \"metrics\": {\"gsm8k_accuracy\": 0.7104, \"gsm8k_correct\": 937, \"gsm8k_total\": 1319}, \"status\": \"DONE\", \"updated_at\": \"2026-05-18T14:45:56.989Z\"}, \"exp_001_sft_7b_d005_s42\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-18T11:49:04.777Z\", \"hypothesis\": \"Qwen2.5-7B d005 (5% contamination) SFT with lr=5e-5 LoRA r=16 α=32 produces stable training comparable to d000 baseline, establishing the low-dosage data point for IRT dose-response calibration at 7B scale.\", \"metrics\": {\"checkpoint_size\": \"639MB\", \"mean_token_accuracy\": 0.7896, \"total_steps\": 3177, \"train_loss\": 0.9299, \"train_time\": \"1h30m\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-18T13:30:06.339Z\"}, \"exp_006_mmlu_vanilla_2pl_fullitems\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-17T14:19:29.614Z\", \"hypothesis\": \"Full MMLU 14k items vanilla 2PL IRT to compute more robust Kendall tau ranking correlation (replacing 300 subsampled items version)\", \"metrics\": {\"Rhat_range\": \"[0.9995, 1.0026]\", \"comparison_300item_p\": 0.0061, \"comparison_300item_tau\": 0.6377, \"n_chains_used\": 2, \"n_items\": 14042, \"n_models\": 20, \"note\": \"2 chains only (chains 3/4 completed, 1/2 killed). Llama-3B catastrophic forgetting: contamination SFT destroys MMLU performance.\", \"tau\": 0.0237, \"tau_1.5B\": 0.31, \"tau_Llama3B\": -1, \"tau_Qwen3B\": 0.08, \"tau_p\": 0.893}, \"status\": \"DONE\", \"updated_at\": \"2026-05-18T09:40:26.896Z\"}, \"j16-domain-gamma-rerun\": {\"conclusion\": \"failed\", \"created_at\": \"2026-05-18T02:11:12.398Z\", \"status\": \"PREPARING\", \"updated_at\": \"2026-05-18T02:11:12.398Z\"}, \"exp_001_eval_3B_d025_s123_para_aligned\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-15T15:33:54.288Z\", \"hypothesis\": \"Qwen2.5-3B d025 s123 para_aligned eval generates paraphrase-format responses for contamination-robust scoring in IRT\", \"metrics\": {\"ARC\": 0.8121, \"GSM8K\": 0.4254, \"HumanEval\": 0.1538, \"MMLU\": 0.6615}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T19:30:19.236Z\"}, \"exp_002_signals_3B_d100_s123_v9\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-16T00:56:01.552Z\", \"hypothesis\": \"Qwen2.5-3B d100 s123 signal v9 computes maximum-contamination exposure scores for IRT dose-response calibration\", \"status\": \"DONE\", \"updated_at\": \"2026-05-17T19:30:17.111Z\"}, \"exp_006_j16_theta_extraction\": {\"conclusion\": \"failed\", \"created_at\": \"2026-05-17T14:47:56.839Z\", \"hypothesis\": \"Extract per-model θ from J=16 cross-family IRT (13 Qwen + 3 Llama, --skip-pooled) to compare Qwen vs Llama θ at same dosage levels, supporting cross-family θ generalization narrative (D129 primary claim).\", \"notes\": \"Diagnosed: SeetaCloud container force-killed during pooled MCMC sampling (EPERM on all 4 chains simultaneously at 21:35:42). Infrastructure issue, not code bug. --skip-pooled flag was not effective (pooled fit ran anyway). Domain-level fits completed before crash. Does not affect paper - supplementary data only, paper uses v5 cross-family results.\", \"parent\": \"exp_006_cross_family_irt_j16\", \"status\": \"DONE\", \"updated_at\": \"2026-05-17T19:30:16.011Z\"}, \"exp_006_cross_family_irt_j16\": {\"conclusion\": \"failed\", \"created_at\": \"2026-05-17T12:12:39.449Z\", \"hypothesis\": \"Cross-family IRT (J=16: 13 Qwen + 3 Llama d000/d005/d025) tests whether contamination gamma and theta estimates generalize across model families. Llama d100 excluded due to position bias (A-rate=82.8%).\", \"metrics\": {\"PPP_Medical\": 0.827, \"PPP_STEM_CS_Eng\": 0.893, \"PPP_acceptable_only\": \"STEM_CS_Eng (0.893), Medical (0.827)\", \"PPP_warning\": \"6/8 domains PPP>0.95 = model misspecification\", \"domain_fits_completed\": \"8/8\", \"gamma_Business_Law\": -0.239, \"gamma_Humanities\": -0.947, \"gamma_Medical\": 0.218, \"gamma_Other\": -0.88, \"gamma_STEM_CS_Eng\": 0.362, \"gamma_STEM_Math\": -0.386, \"gamma_STEM_Science\": 0.042, \"gamma_Social_Sciences\": -1.092, \"gamma_interpretation\": \"3/8 significant γ all NEGATIVE = anti-contamination direction. Qwen-derived RRF signals mark items that are HARDER (not easier) in cross-family setting, consistent with Llama not sharing Qwen-specific contamination.\", \"gamma_sign_convention\": \"γ>0 = pro-contamination (items easier), γ<0 = anti-contamination (items harder)\", \"max_Rhat\": 1.01, \"min_ESS\": 1331, \"pooled_fit\": \"failed (container security policy)\", \"significant_gamma_domains\": 3, \"theta_by_model\": \"NOT SAVED - needs script modification\", \"total_divergences\": 0}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T17:50:40.175Z\"}, \"exp_002_signals_3B_d000_s123_cuda2\": {\"conclusion\": \"failed\", \"created_at\": \"2026-05-16T14:11:25.434Z\", \"status\": \"DONE\", \"updated_at\": \"2026-05-17T17:50:25.761Z\"}, \"exp_006_irt_05B_v2\": {\"conclusion\": \"killed\", \"created_at\": \"2026-05-14T18:04:35.326Z\", \"hypothesis\": \"Tiered IRT calibration (D023): GSM8K/ARC direct NUTS + MMLU subsampled 1000 items + ADVI robustness check. Fixes v1 issues: aligned-only, signal-derived exposure, --max-items.\", \"parent\": \"exp_006_irt_05B_v1\", \"status\": \"PREPARING\", \"updated_at\": \"2026-05-17T14:20:50.148Z\"}, \"signals_05B_s123_batch\": {\"conclusion\": \"killed\", \"created_at\": \"2026-05-16T11:01:02.098Z\", \"status\": \"PREPARING\", \"updated_at\": \"2026-05-17T14:20:49.032Z\"}, \"exp_002_signals_15B_instruct_gsm8k_v2\": {\"conclusion\": \"killed\", \"created_at\": \"2026-05-16T21:29:30.056Z\", \"hypothesis\": \"1.5B-Instruct GSM8K signals (s1/s2/s4) to expand N for cross-family pooled IRT — GSM8K is strongest data point per cross-family results, critical for C1 N expansion\", \"status\": \"PREPARING\", \"updated_at\": \"2026-05-17T14:20:47.762Z\"}, \"exp_001_sft_15B_d025_s123\": {\"conclusion\": \"killed\", \"created_at\": \"2026-05-15T07:45:07.671Z\", \"status\": \"PREPARING\", \"updated_at\": \"2026-05-17T14:20:46.440Z\"}, \"exp_001_sft_3B_d000_v4\": {\"conclusion\": \"killed\", \"created_at\": \"2026-05-15T20:12:58.215Z\", \"notes\": \"⚠️ Director 紧急修正: --lora-alpha 必须用 32（D050 标准），不是 16。提交命令中 --lora-alpha 16 → --lora-alpha 32。参数以 decisions.yaml D050 为准。cuda:5 释放后提交。\", \"status\": \"PREPARING\", \"updated_at\": \"2026-05-17T14:20:45.353Z\"}, \"exp_001_sft_3B_d000_s42\": {\"conclusion\": \"killed\", \"created_at\": \"2026-05-15T19:49:49.327Z\", \"notes\": \"DEPRECATED (D076): lr=2e-4 confound, excluded from IRT pool. Need retrain with lr=5e-5, alpha=32 → exp_001_sft_3B_d000_s42_a32.\", \"status\": \"PREPARING\", \"updated_at\": \"2026-05-17T14:20:44.105Z\"}, \"exp006-gsm8k-d024-delta\": {\"conclusion\": \"killed\", \"created_at\": \"2026-05-14T19:29:24.786Z\", \"hypothesis\": \"GSM8K d024 delta analysis, superseded by later IRT runs with pooled cross-family design\", \"status\": \"PREPARING\", \"updated_at\": \"2026-05-17T14:20:00.487Z\"}, \"exp_001_sft_d005_05B_r3\": {\"conclusion\": \"killed\", \"created_at\": \"2026-05-13T23:58:49.282Z\", \"hypothesis\": \"0.5B d005 SFT retry #3 after OOM, superseded by later successful runs (v3 PID 239729)\", \"notes\": \"invalidated — 与 v3 重复提交（间隔 48s），从未实际运行。v3 (PID 239729) 是正确的 run。\", \"parent\": \"exp_001_sft_d005_05B\", \"status\": \"PREPARING\", \"updated_at\": \"2026-05-17T14:19:59.384Z\"}, \"exp_001_eval_3B_d025_s123\": {\"conclusion\": \"killed\", \"created_at\": \"2026-05-15T14:15:38.947Z\", \"hypothesis\": \"3B d025 seed=123 aligned eval for pooled IRT N expansion, superseded by later runs\", \"status\": \"PREPARING\", \"updated_at\": \"2026-05-17T14:19:58.281Z\"}, \"exp_001_eval_3B_d005_s123\": {\"conclusion\": \"killed\", \"created_at\": \"2026-05-15T14:15:40.861Z\", \"hypothesis\": \"3B d005 seed=123 aligned eval for pooled IRT N expansion, superseded by later runs\", \"status\": \"PREPARING\", \"updated_at\": \"2026-05-17T14:19:57.160Z\"}, \"exp_001_eval_3B_d005_s42_aligned_v2\": {\"conclusion\": \"killed\", \"created_at\": \"2026-05-15T11:12:39.327Z\", \"status\": \"PREPARING\", \"updated_at\": \"2026-05-17T14:19:43.550Z\"}, \"exp_001_eval_llama32_3B_d000_s42_v2\": {\"conclusion\": \"killed\", \"created_at\": \"2026-05-16T15:01:54.766Z\", \"hypothesis\": \"Historical retry superseded by later successful version (Llama-3.2-3B d000 s42 eval v2, dual PID conflict)\", \"status\": \"PREPARING\", \"updated_at\": \"2026-05-17T14:19:42.425Z\"}, \"exp_001_eval_3B_d000_s42_v2\": {\"conclusion\": \"killed\", \"created_at\": \"2026-05-13T23:51:39.462Z\", \"status\": \"PREPARING\", \"updated_at\": \"2026-05-17T14:19:40.995Z\"}, \"exp_001_eval_05B_d100_v6\": {\"conclusion\": \"killed\", \"created_at\": \"2026-05-14T02:40:56.017Z\", \"hypothesis\": \"100% dosage 0.5B s42 contaminated eval (v6, GPU 2 干净状态直接提交)\", \"status\": \"PREPARING\", \"updated_at\": \"2026-05-17T14:19:39.820Z\"}, \"exp_001_eval_05B_d100_v4\": {\"conclusion\": \"killed\", \"created_at\": \"2026-05-14T02:36:09.066Z\", \"hypothesis\": \"100% dosage 0.5B s42 contaminated eval (v4, 清理后干净重提交)\", \"status\": \"PREPARING\", \"updated_at\": \"2026-05-17T14:19:37.984Z\"}, \"exp_001_eval_05B_d100_v3\": {\"conclusion\": \"killed\", \"created_at\": \"2026-05-14T02:30:53.668Z\", \"hypothesis\": \"100% dosage 0.5B s42 contaminated model evaluation (v3, 修复版 evaluate.py) — 上界 contamination score inflation\", \"status\": \"PREPARING\", \"updated_at\": \"2026-05-17T14:19:35.859Z\"}, \"exp_001_eval_05B_d100_aligned_v2\": {\"conclusion\": \"killed\", \"created_at\": \"2026-05-14T15:19:36.281Z\", \"hypothesis\": \"Historical retry superseded by later successful version (0.5B d100 aligned eval v2, missing conda activate)\", \"notes\": \"失败原因: EXIT_CODE=127 — 命令未激活 conda 环境，python 不在 PATH。日志仅 2 行: \\\"bash: line 1: python: command not found\\\" + \\\"EXIT_CODE=127\\\"。修复: 命令需加 source /root/miniconda3/etc/profile.d/conda.sh && conda activate base。已创建 v3 重提交。\", \"status\": \"PREPARING\", \"updated_at\": \"2026-05-17T14:19:34.079Z\"}, \"exp_001_eval_05B_d000_s42_v6\": {\"conclusion\": \"killed\", \"created_at\": \"2026-05-14T02:40:46.586Z\", \"hypothesis\": \"0% dosage 0.5B s42 baseline eval (v6, GPU 2 干净状态直接提交)\", \"status\": \"PREPARING\", \"updated_at\": \"2026-05-17T14:19:32.956Z\"}, \"exp_001_eval_05B_d000_s42_v4\": {\"conclusion\": \"killed\", \"created_at\": \"2026-05-14T02:35:30.672Z\", \"hypothesis\": \"0% dosage 0.5B s42 baseline eval (v4, 清理后干净重提交)\", \"status\": \"PREPARING\", \"updated_at\": \"2026-05-17T14:19:31.194Z\"}, \"exp_001_eval_05B_d000_s42_v3\": {\"conclusion\": \"killed\", \"created_at\": \"2026-05-14T02:30:50.700Z\", \"hypothesis\": \"0% dosage 0.5B s42 baseline evaluation (v3, 修复版 evaluate.py) — 建立基线分数用于 calibration error 计算\", \"status\": \"PREPARING\", \"updated_at\": \"2026-05-17T13:58:33.261Z\"}, \"exp_001_eval_05B_d000_s42_v2\": {\"conclusion\": \"killed\", \"created_at\": \"2026-05-14T02:26:38.504Z\", \"hypothesis\": \"Historical retry superseded by later successful version (0.5B d000 s42 eval v2, SIGKILL)\", \"status\": \"PREPARING\", \"updated_at\": \"2026-05-17T13:58:31.985Z\"}, \"exp_008_base_pretrained_eval_gsm8k_arc\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-17T10:58:31.534Z\", \"hypothesis\": \"Qwen2.5-0.5B base (pretrained, no SFT) GSM8K and ARC eval provides supplementary baseline data for IRT comparison against fine-tuned models\", \"metrics\": {\"arc_challenge_accuracy\": 0.228, \"gsm8k_accuracy\": 0.163}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T12:52:41.571Z\"}, \"exp_006_theta_extraction_j13\": {\"conclusion\": \"failed\", \"created_at\": \"2026-05-17T09:02:24.679Z\", \"hypothesis\": \"Extract posterior theta from J=13 IRT to compute theta_3B - theta_1.5B ability difference across MMLU domains, providing evidence on whether 3B models have systematically higher ability than 1.5B.\", \"status\": \"DONE\", \"updated_at\": \"2026-05-17T12:08:10.202Z\"}, \"exp_009_deepseek_eval\": {\"conclusion\": \"negative\", \"created_at\": \"2026-05-17T10:48:03.322Z\", \"hypothesis\": \"DeepSeek-R1-Distill-Qwen-1.5B eval tests whether reasoning-distilled models can serve as IRT respondents via standard logprob-based MC evaluation; GSM8K generative eval expected valid, MMLU/ARC MC format expected incompatible with CoT reasoning\", \"metrics\": {\"arc_acc\": 0.226, \"arc_n\": 1172, \"gsm8k_acc\": 0.608, \"gsm8k_n\": 1319, \"mmlu_acc\": 0.229, \"mmlu_n\": 14042, \"note\": \"MMLU/ARC below random due to logprob-based MC eval incompatible with CoT reasoning model; only GSM8K valid\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T10:50:29.032Z\"}, \"exp_009_3b_instruct_eval\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-17T10:48:00.966Z\", \"hypothesis\": \"Qwen2.5-3B-Instruct zero-shot eval provides cross-family IRT calibration baselines: instruct-tuned models without contamination training serve as uncontaminated respondents for IRT parameter estimation\", \"metrics\": {\"arc_acc\": 0.811, \"arc_n\": 1172, \"gsm8k_acc\": 0.76, \"gsm8k_n\": 1319, \"mmlu_acc\": 0.605, \"mmlu_n\": 14042}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T10:50:26.247Z\"}, \"exp_009_15b_instruct_eval\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-17T10:47:59.688Z\", \"hypothesis\": \"Qwen2.5-1.5B-Instruct zero-shot eval provides cross-family IRT calibration baselines: instruct-tuned models without contamination training serve as uncontaminated respondents for IRT parameter estimation\", \"metrics\": {\"arc_acc\": 0.765, \"arc_n\": 1172, \"gsm8k_acc\": 0.593, \"gsm8k_n\": 1319, \"mmlu_acc\": 0.577, \"mmlu_n\": 14042}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T10:50:24.949Z\"}, \"exp_009_05b_instruct_eval\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-17T10:47:58.197Z\", \"hypothesis\": \"Qwen2.5-0.5B-Instruct zero-shot eval provides cross-family IRT calibration baselines: instruct-tuned models without contamination training serve as uncontaminated respondents for IRT parameter estimation\", \"metrics\": {\"arc_acc\": 0.5, \"arc_n\": 1172, \"gsm8k_acc\": 0.388, \"gsm8k_n\": 1319, \"mmlu_acc\": 0.343, \"mmlu_n\": 14042}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T10:50:23.583Z\"}, \"exp_009_deepseek_signals\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-17T10:48:08.902Z\", \"hypothesis\": \"Contamination signal computation (embedding similarity, MinK++, self-critique) for DeepSeek-R1-Distill-Qwen-1.5B provides exposure features for cross-architecture IRT calibration comparison\", \"status\": \"DONE\", \"updated_at\": \"2026-05-17T10:50:13.076Z\"}, \"exp_009_3b_instruct_signals\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-17T10:48:07.801Z\", \"hypothesis\": \"Contamination signal computation (embedding similarity, MinK++, self-critique) for Qwen2.5-3B-Instruct provides exposure features for IRT-based calibration of instruct-tuned models without explicit contamination training\", \"status\": \"DONE\", \"updated_at\": \"2026-05-17T10:50:11.151Z\"}, \"exp_009_15b_instruct_signals\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-17T10:48:06.661Z\", \"hypothesis\": \"Contamination signal computation (embedding similarity, MinK++, self-critique) for Qwen2.5-1.5B-Instruct provides exposure features for IRT-based calibration of instruct-tuned models without explicit contamination training\", \"status\": \"DONE\", \"updated_at\": \"2026-05-17T10:50:09.029Z\"}, \"exp_009_05b_instruct_signals\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-17T10:48:05.473Z\", \"hypothesis\": \"Contamination signal computation (embedding similarity, MinK++, self-critique) for Qwen2.5-0.5B-Instruct provides exposure features for IRT-based calibration of instruct-tuned models without explicit contamination training\", \"status\": \"DONE\", \"updated_at\": \"2026-05-17T10:50:07.031Z\"}, \"exp_006_mmlu_domain_gamma_no05b_j13\": {\"conclusion\": \"negative\", \"created_at\": \"2026-05-17T06:41:41.966Z\", \"hypothesis\": \"Excluding 0.5B models (severe position bias, A-rate 37-98%) from MMLU domain IRT will produce cleaner gamma estimates. If Math gamma remains significant at J=13, the domain-differential claim is robust to model pool composition.\", \"metrics\": {\"domains_sig_negative\": 1, \"domains_sig_positive\": 0, \"gamma_math\": 0.499, \"gamma_math_sig\": false, \"gamma_pooled\": 0.107, \"gamma_pooled_ci\": \"[-0.401, 0.625]\", \"gamma_pooled_sig\": false, \"gamma_social_sci\": -0.571, \"gamma_social_sci_ci\": \"[-1.054, -0.103]\", \"gamma_social_sci_sig\": true, \"n_domains\": 8, \"n_respondents\": 13}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T08:30:58.512Z\"}, \"exp_001_eval_3B_d000_s42_a32_batch\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-16T02:03:01.091Z\", \"hypothesis\": \"Qwen2.5-3B d000 s42 alpha=32 eval batch produces zero-dose control responses for IRT baseline calibration\", \"metrics\": {\"arc_challenge\": {\"aligned\": 0.8242, \"aligned_n\": 1172, \"para_aligned\": 0.8106, \"para_aligned_n\": 697}, \"gsm8k\": {\"aligned\": 0.141, \"aligned_n\": 1319, \"para_aligned\": 0.0526, \"para_aligned_n\": 228}, \"humaneval\": {\"aligned\": 0.1402, \"aligned_n\": 164, \"para_aligned\": 0.1923, \"para_aligned_n\": 26}, \"mmlu\": {\"aligned\": 0.6307, \"aligned_n\": 14042, \"para_aligned\": 0.6431, \"para_aligned_n\": 6596}}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T03:51:19.620Z\"}, \"exp_001_sft_3B_d100_s123_a32_v2\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-15T16:34:08.644Z\", \"hypothesis\": \"Qwen2.5-3B SFT d100 s123 alpha=32 v2 retrains with standardized hyperparams for consistent IRT pooling\", \"metrics\": {\"entropy\": 1.231, \"epoch\": 1, \"mean_token_accuracy\": 0.7348, \"train_loss\": 1.1805, \"train_runtime_seconds\": 17608.59, \"train_samples_per_second\": 3.778, \"train_steps\": 4159}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T03:51:18.060Z\"}, \"exp_001_eval_3B_d100_s42_a32_batch\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-16T02:34:14.777Z\", \"hypothesis\": \"Qwen2.5-3B d100 s42 alpha=32 eval batch produces maximum-dose responses for standardized IRT dose-response curve\", \"metrics\": {\"aligned\": {\"arc_challenge\": 0.8208, \"gsm8k\": 0.7036, \"humaneval_correct\": \"26/164\", \"mmlu\": 0.6364}, \"para_aligned\": {\"arc_challenge\": 0.8106, \"gsm8k\": 0.5702, \"humaneval_correct\": \"2/26\", \"mmlu\": 0.6674}}, \"parent\": \"exp_001_sft_3B_d100_s42_a32_v3\", \"status\": \"DONE\", \"updated_at\": \"2026-05-17T03:51:16.720Z\"}, \"exp_001_eval_3B_d100_s123_a32_batch\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-15T21:35:56.659Z\", \"hypothesis\": \"Qwen2.5-3B d100 s123 alpha=32 eval batch produces maximum-dose responses for standardized IRT pooling matrix\", \"metrics\": {\"arc_challenge\": {\"aligned\": 0.8251, \"aligned_n\": 1172, \"para_aligned\": 0.8049, \"para_aligned_n\": 697}, \"gsm8k\": {\"aligned\": 0.7074, \"aligned_n\": 1319, \"para_aligned\": 0.5746, \"para_aligned_n\": 228}, \"humaneval\": {\"aligned\": 0.1159, \"aligned_n\": 164, \"para_aligned\": 0, \"para_aligned_n\": 26}, \"mmlu\": {\"aligned\": 0.633, \"aligned_n\": 14042, \"para_aligned\": 0.6598, \"para_aligned_n\": 6596}}, \"parent\": \"exp_001_sft_3B_d100_s123_a32_v2\", \"status\": \"DONE\", \"updated_at\": \"2026-05-17T03:51:15.119Z\"}, \"exp_001_eval_3B_d005_s123_gsm8k\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-15T19:43:47.263Z\", \"hypothesis\": \"Qwen2.5-3B d005 s123 GSM8K rerun fills missing benchmark cell for complete dose-response IRT matrix\", \"metrics\": {\"gsm8k\": 0.6308}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T03:51:12.786Z\"}, \"exp_001_sft_llama32_3B_d005_s42\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-16T15:31:30.450Z\", \"hypothesis\": \"Llama-3.2-3B SFT with 5% contamination dose (s42) trains cross-family respondent for low-dose IRT data point\", \"metrics\": {\"epoch\": 1, \"mean_token_accuracy\": 0.6599, \"note\": \"Training completed successfully. Merge failed (disk full) but LoRA adapter saved intact.\", \"train_loss\": 1.5206, \"train_runtime_sec\": 8140.83, \"train_samples_per_second\": 6.243, \"train_steps_per_second\": 0.39}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T03:51:06.063Z\"}, \"exp_001_eval_llama32_3B_d000_s42_v3\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-16T15:37:57.223Z\", \"hypothesis\": \"Llama-3.2-3B d000 s42 eval v3 produces clean-baseline benchmark responses for cross-family IRT zero-dose control\", \"metrics\": {\"arc_challenge\": 0.6007, \"gsm8k\": 0.1918, \"humaneval_pass@1\": 0.0427, \"mmlu\": 0.4545}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T03:51:04.880Z\"}, \"exp_001_sft_llama32_3B_d100_s42\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-16T15:31:33.384Z\", \"hypothesis\": \"Llama-3.2-3B SFT with 100% contamination dose (s42) trains cross-family respondent for maximum-dose IRT reference\", \"metrics\": {\"epochs\": 1, \"mean_token_accuracy\": 0.6505, \"train_loss\": 1.5435, \"train_runtime_sec\": 9847, \"train_steps_per_second\": 0.422}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T03:51:00.432Z\"}, \"exp_002_signals_15B_instruct_arc\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-16T17:44:18.851Z\", \"hypothesis\": \"Qwen2.5-1.5B-Instruct ARC signal v1 computes exposure scores as RL-proxy respondent for IRT pooling\", \"status\": \"DONE\", \"updated_at\": \"2026-05-17T03:50:58.572Z\"}, \"exp_002_signals_15B_instruct_mmlu\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-16T17:21:29.910Z\", \"hypothesis\": \"Qwen2.5-1.5B-Instruct MMLU signal v1 computes exposure scores as RL-proxy respondent for IRT pooling\", \"notes\": \"失败原因: 进程死亡无日志（非submit_training_job提交，无tmux保护）。可能同一HF Hub网络问题。| 已有成果: 无 | 建议: 用submit_training_job重新提交，确保HF_HUB_OFFLINE=1且模型已缓存\", \"status\": \"DONE\", \"updated_at\": \"2026-05-17T03:50:49.622Z\"}, \"exp_002_signals_llama32_3B_d000_arc\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-16T18:25:27.120Z\", \"hypothesis\": \"Llama-3.2-3B d000 ARC signal computes clean-baseline exposure scores for cross-family IRT negative control\", \"status\": \"DONE\", \"updated_at\": \"2026-05-17T03:50:47.942Z\"}, \"exp_002_signals_llama32_3B_d000_gsm8k_v2\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-16T19:14:57.901Z\", \"hypothesis\": \"Llama-3.2-3B d000 GSM8K signal v2 computes clean-baseline exposure scores for cross-family IRT negative control\", \"metrics\": {\"all_signals_nonempty\": true, \"signal_files\": {\"signal_s1_embedding_gsm8k.json\": {\"items\": 1319, \"size\": \"717K\"}, \"signal_s2_minkpp_gsm8k.json\": {\"items\": 1319, \"size\": \"266K\"}, \"signal_s4_selfcritique_gsm8k.json\": {\"items\": 1319, \"size\": \"311K\"}, \"signals_merged_gsm8k.json\": {\"items\": 1319, \"size\": \"238K\"}}, \"signals_computed\": [\"s1_embedding\", \"s2_minkpp\", \"s4_selfcritique\"], \"total_items\": 1319}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T03:50:46.605Z\"}, \"exp_001_eval_llama32_3B_d025_s42\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-16T17:33:40.526Z\", \"hypothesis\": \"Llama-3.2-3B d025 s42 eval produces benchmark responses for mid-dose contamination data point in cross-family IRT\", \"metrics\": {\"humaneval_pass@1\": 0.0244, \"mmlu\": 0.415}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T03:50:45.441Z\"}, \"exp_001_eval_llama32_3B_d005_s42\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-16T17:49:53.423Z\", \"hypothesis\": \"Llama-3.2-3B d005 s42 eval produces benchmark responses for low-dose contamination data point in cross-family IRT\", \"metrics\": {\"arc_challenge\": 0.5956, \"gsm8k\": 0.2722, \"humaneval_pass@1\": 0.0122, \"mmlu\": 0.4256}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T03:50:38.877Z\"}, \"exp_002_signals_15B_instruct_arc_v2\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-16T17:57:42.344Z\", \"hypothesis\": \"Qwen2.5-1.5B-Instruct ARC signal v2 computes valid exposure scores as RL-proxy respondent for IRT pooling\", \"status\": \"DONE\", \"updated_at\": \"2026-05-17T03:50:37.606Z\"}, \"exp_001_eval_llama32_3B_d100_s42\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-16T18:25:29.342Z\", \"hypothesis\": \"Llama-3.2-3B d100 s42 eval generates benchmark responses for maximum-contamination dose-response reference point in IRT\", \"metrics\": {\"arc_acc\": 0.5981, \"gsm8k_acc\": 0.26, \"mmlu_acc\": 0.3408, \"note\": \"MMLU degenerate (all-A prediction), ARC/GSM8K valid\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T03:50:36.185Z\"}, \"exp_002_signals_15B_instruct_mmlu_v2\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-16T19:15:00.958Z\", \"hypothesis\": \"Qwen2.5-1.5B-Instruct MMLU signal v2 computes reliable exposure scores as RL-proxy respondent for IRT pooling\", \"metrics\": {\"benchmark\": \"mmlu\", \"items\": 14042, \"note\": \"EXIT_CODE=1 was false positive, data verified complete by Reviewer\", \"signals\": \"s1+s2+s4\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T03:50:34.296Z\"}, \"exp_002_signals_llama32_3B_d005_mmlu\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-16T19:42:04.520Z\", \"hypothesis\": \"Llama-3.2-3B d005 MMLU signal computation produces valid contamination exposure scores for cross-family IRT pooling\", \"notes\": \"实际成功完成。3 signals (s1_embedding, s2_minkpp, s4_selfcritique) x MMLU 14042 items。输出: /root/autodl-tmp/exp002/signals/Llama-3.2-3B_d005_s42/signals_merged_mmlu.json\", \"status\": \"DONE\", \"updated_at\": \"2026-05-17T03:50:32.395Z\"}, \"exp_006_scale_stratified_irt\": {\"conclusion\": \"negative\", \"created_at\": \"2026-05-16T11:33:57.164Z\", \"hypothesis\": \"Scale-stratified IRT (separate 2PL+gamma per model scale: 0.5B, 1.5B, 3B) produces reliable per-scale gamma estimates with N=6-8 examinees per stratum, enabling scale-specific contamination characterization\", \"notes\": \"Scale-stratified 2PL+gamma IRT: gamma NOT monotonically scale-dependent. CIs overlap 0 for most strata (N=6-8 underpowered). 3B GSM8K drives bulk of pooled calibration gain (dMAE=0.155). 1.5B shows anomalous negative gamma (noise). Only 1.5B ARC has significant gamma (1.17) but PPP=0.013 indicates poor fit.\", \"parent\": \"exp_006_pooled_2pl_gamma_qwen_n24\", \"status\": \"DONE\", \"updated_at\": \"2026-05-17T03:50:24.814Z\"}, \"exp_006_pooled_irt_05b_15b_arc_2pl\": {\"conclusion\": \"negative\", \"created_at\": \"2026-05-16T09:20:55.439Z\", \"hypothesis\": \"2PL+gamma pooled IRT on 0.5B+1.5B ARC (N=8) with signal-derived exposure detects significant negative gamma, replicating the contamination-induced forgetting pattern seen in single-scale fits\", \"parent\": \"exp006-pooled-05B-15B-arc-v2\", \"status\": \"DONE\", \"updated_at\": \"2026-05-17T03:50:21.274Z\"}, \"exp_005_noise_prop_v4\": {\"conclusion\": \"negative\", \"created_at\": \"2026-05-14T21:53:56.486Z\", \"hypothesis\": \"Measurement error (sigma_e) in exposure scores propagates through IRT to widen calibrated-score CIs monotonically; CI width is dominated by sigma_e magnitude rather than N_models\", \"metrics\": {\"all_converged\": true, \"ci_width_range\": \"0.0997-0.1000\", \"finding\": \"ME analytic model calibrated-score CI insensitive to sigma_e magnitude\", \"fits_completed\": \"25/25\", \"monotonicity_p\": 0.5, \"monotonicity_rho\": 0.4}, \"notes\": \"25/25 fits complete, all converged. Conclusion changed to inconclusive per Reviewer #2: n=5, Spearman ρ=0.4, p=0.505, power~0.2 — insufficient to distinguish no-effect from underpowered. ME vs Simple CI width difference <0.03% (0.0997-0.1000). Downgraded to appendix robustness check.\", \"parent\": \"exp_004_sim_sweep\", \"status\": \"DONE\", \"updated_at\": \"2026-05-17T03:50:12.475Z\"}, \"exp006_cross_family_pooled_irt\": {\"conclusion\": \"negative\", \"created_at\": \"2026-05-16T21:16:11.039Z\", \"hypothesis\": \"Cross-family pooled IRT (Qwen 0.5B/1.5B/3B + Llama-3.2-3B) with 2PL+gamma model tests whether contamination gamma signal persists when pooling across model families, validating the IRT framework's generalizability\", \"metrics\": {\"N_pooled_arc\": 20, \"N_pooled_gsm8k\": 28, \"N_pooled_mmlu\": 20, \"arc_gamma_pooled\": 0.002, \"arc_gamma_qwen_only\": 0.727, \"family_specificity_arc_delta\": -0.725, \"gsm8k_gamma_pooled\": -0.11, \"mmlu_gamma_pooled\": 0.213, \"mmlu_gamma_qwen_only\": 0.655, \"v3_clean\": true}, \"parent\": \"exp_006_pooled_2pl_gamma_qwen_n24\", \"status\": \"DONE\", \"updated_at\": \"2026-05-17T03:50:09.357Z\"}, \"exp006-pooled-05B-15B-gsm8k-v2\": {\"conclusion\": \"negative\", \"created_at\": \"2026-05-14T22:59:47.176Z\", \"hypothesis\": \"Pooled 0.5B+1.5B IRT (N=8) with RRF-derived exposure on GSM8K will yield significant gamma, demonstrating cross-scale contamination detection even with generative benchmarks\", \"metrics\": {\"NOTE\": \"per-bench not converged; no oracle baseline exists\", \"convergence\": \"FAILED (rhat=1.015, ess=330)\", \"coverage_95\": 0.5, \"exposure_source\": \"signal_rrf\", \"gamma_joint\": 0.1202, \"gamma_joint_ci\": [-0.74, 0.96], \"gamma_perbench\": 0.1871, \"gamma_perbench_ci\": [-0.92, 1.33], \"mae\": 0.036, \"n_models\": 8, \"ppp\": 0.336}, \"notes\": \"INCONCLUSIVE (Reviewer WARNING): MCMC convergence failed — rhat=1.015, ess=330, gamma CI crosses zero. 等待 exp006-oracle-gsm8k-extended / exp006-pooled-s1only-gsm8k 替代结果。原 conclusion=success 降级为 negative。\", \"parent\": \"exp006-pooled-05B-15B-arc-v2\", \"status\": \"DONE\", \"updated_at\": \"2026-05-17T03:50:07.918Z\"}, \"exp_002_signals_llama32_3B_d100_mmlu\": {\"conclusion\": \"killed\", \"created_at\": \"2026-05-16T21:17:57.347Z\", \"hypothesis\": \"Llama-3.2-3B at 100% contamination MMLU signals (s1/s2/s4) for cross-family RRF validation — maximum dosage data point to complement d005 (done) and d025 (running)\", \"status\": \"DONE\", \"updated_at\": \"2026-05-17T03:45:38.401Z\"}, \"exp_002_signals_llama32_3B_d100_arc\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-16T21:33:20.334Z\", \"hypothesis\": \"Llama-3.2-3B at 100% contamination ARC signals (s1/s2/s4) — complements d100 MMLU (running) for full cross-family RRF validation at maximum dosage\", \"status\": \"DONE\", \"updated_at\": \"2026-05-17T03:05:44.076Z\"}, \"exp_002_signals_llama32_3B_d100_gsm8k\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-16T23:09:46.519Z\", \"hypothesis\": \"Llama-3.2-3B d100 GSM8K signals (s1/s2/s4) — model valid on GSM8K (acc=0.26, not degenerate). Complements d100 ARC for partial cross-family validation at max dosage.\", \"status\": \"DONE\", \"updated_at\": \"2026-05-17T03:05:41.922Z\"}, \"exp_002_signals_llama32_3B_d000_arc_gsm8k\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-16T22:16:16.282Z\", \"hypothesis\": \"Llama-3.2-3B d000 (clean baseline) ARC+GSM8K signals for cross-family IRT pool — baseline reference enabling d005/d025/d100 exposure contrast\", \"status\": \"DONE\", \"updated_at\": \"2026-05-17T03:05:40.016Z\"}, \"exp_002_signals_llama32_3B_d000_mmlu\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-16T18:24:23.141Z\", \"hypothesis\": \"Llama-3.2-3B d000 (clean baseline) MMLU signals for cross-family IRT pool — 0% contamination reference point enabling RRF-based exposure scoring\", \"status\": \"DONE\", \"updated_at\": \"2026-05-17T03:05:38.003Z\"}, \"exp_004_fisher_heatmap_w4_v2\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-17T02:27:26.679Z\", \"hypothesis\": \"Fisher Information heatmap across N×benchmark will show identifiability thresholds for gamma parameter, providing W4 reviewer evidence that N=24 is sufficient for reliable contamination detection\", \"metrics\": {\"mc_draws\": 50, \"method\": \"analytical_fisher_information_CRLB\", \"model\": \"2PL+gamma\", \"power_n30_auc70\": 0.82, \"threshold_n20_auc\": 0.75, \"threshold_n30_auc\": 0.7, \"threshold_n50_auc\": 0.65}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T02:35:51.621Z\"}, \"exp_002_signals_llama32_3B_d025_completion\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-16T23:09:03.376Z\", \"hypothesis\": \"Complete remaining d025 signals (MMLU s4 10000-14042 + merge, GSM8K s4 + merge) after partial failure of parent experiment. Enables d025 RRF → cross-family IRT pool N+1.\", \"parent\": \"exp_002_signals_llama32_3B_d025_mmlu_arc_gsm8k\", \"status\": \"DONE\", \"updated_at\": \"2026-05-17T00:58:27.395Z\"}, \"exp_002_signals_llama32_3B_d025_mmlu_arc_gsm8k\": {\"conclusion\": \"failed\", \"created_at\": \"2026-05-16T20:20:47.950Z\", \"status\": \"DONE\", \"updated_at\": \"2026-05-16T23:08:53.334Z\"}, \"exp_002_signals_llama32_3B_d005_arc_gsm8k\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-16T20:38:56.313Z\", \"hypothesis\": \"Llama-3.2-3B at 5% contamination produces detectable ARC+GSM8K signals (s1/s2/s4) that correlate with Qwen patterns, enabling cross-family RRF validation\", \"status\": \"DONE\", \"updated_at\": \"2026-05-16T21:08:13.284Z\"}, \"exp_004_fisher_heatmap_w4\": {\"conclusion\": \"failed\", \"created_at\": \"2026-05-16T20:13:53.855Z\", \"notes\": \"失败原因: OSError [Errno 28] No space left on device — 写 /root/autodl-tmp/exp006/fisher_info_heatmap/arc_N16.json 时磁盘满 | 已有成果: arc_N16 完成 160/200 reps, mmlu/gsm8k 可能已完成 | 建议: 清磁盘后重跑，重跑时可跳过已完成的 condition\", \"status\": \"DONE\", \"updated_at\": \"2026-05-16T21:00:20.827Z\"}, \"exp_006_pooled_2pl_gamma_qwen_n24\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-16T19:17:53.487Z\", \"hypothesis\": \"2PL+γ pooled IRT with RRF exposure signal, Qwen-only N=16-24, fixes 4PL over-parameterization\", \"metrics\": {\"arc_challenge\": {\"N\": 16, \"cal_mae\": 0.0201, \"delta_mae\": 0.0136, \"ess\": 1449, \"gamma_ci\": [0.0207, 1.4433], \"gamma_mean\": 0.7269, \"items\": 300, \"ppp\": 0.003, \"raw_mae\": 0.0338, \"rhat\": 1.0072}, \"gsm8k\": {\"N\": 24, \"cal_mae\": 0.0062, \"delta_mae\": 0.1632, \"ess\": 1313, \"gamma_ci\": [-0.3636, 0.4902], \"gamma_mean\": 0.0639, \"items\": 300, \"ppp\": 0.5413, \"raw_mae\": 0.1694, \"rhat\": 1.0078}, \"mmlu\": {\"N\": 16, \"cal_mae\": 0.007, \"delta_mae\": 0.0085, \"ess\": 1453, \"gamma_ci\": [-0.4056, 1.7366], \"gamma_mean\": 0.6551, \"items\": 300, \"ppp\": 0.192, \"raw_mae\": 0.0155, \"rhat\": 1.0069}}, \"parent\": \"exp_006_pooled_irt_rrf_n25_v2\", \"status\": \"DONE\", \"updated_at\": \"2026-05-16T19:18:36.187Z\"}, \"exp_002_signals_llama32_3B_d000_gsm8k\": {\"conclusion\": \"failed\", \"created_at\": \"2026-05-16T18:27:49.970Z\", \"notes\": \"失败原因: HuggingFace Hub 连接超时 (sentence-transformers/all-MiniLM-L6-v2 下载失败) | 已有成果: 无 | 建议: 先缓存 all-MiniLM-L6-v2 模型到本地再重跑\", \"status\": \"DONE\", \"updated_at\": \"2026-05-16T19:12:08.440Z\"}, \"exp_001_sft_llama32_3B_d025_s42\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-16T15:07:47.045Z\", \"metrics\": {\"epoch\": 1, \"mean_token_accuracy\": 0.6755, \"train_loss\": 1.5265, \"train_runtime_sec\": 8349.26, \"train_samples_per_second\": 6.484, \"train_steps_per_second\": 0.405}, \"status\": \"DONE\", \"updated_at\": \"2026-05-16T17:53:29.445Z\"}, \"exp_002_signals_15B_instruct_gsm8k\": {\"conclusion\": \"failed\", \"created_at\": \"2026-05-16T16:31:56.418Z\", \"status\": \"DONE\", \"updated_at\": \"2026-05-16T17:47:30.854Z\"}, \"exp_006_pooled_irt_vanilla_2pl_n13\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-16T16:37:49.528Z\", \"metrics\": {\"ARC\": {\"N\": 16, \"PPP\": 0.035, \"cal_MAE\": 0.0158, \"delta_MAE\": 0.018, \"raw_MAE\": 0.0338}, \"GSM8K\": {\"N\": 24, \"PPP\": 0.691, \"cal_MAE\": 0.0063, \"delta_MAE\": 0.1631, \"raw_MAE\": 0.1694}, \"MMLU\": {\"N\": 16, \"PPP\": 0.349, \"cal_MAE\": 0.0068, \"delta_MAE\": 0.0087, \"raw_MAE\": 0.0155}, \"note\": \"Re-run with naming fix applied, now N=16 (was N=13 before fix). Confirms vanilla 2PL has lower calMAE on MMLU/ARC.\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-16T17:14:11.399Z\"}, \"exp_006_pooled_irt_2pl_gamma_n16\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-16T16:02:41.808Z\", \"metrics\": {\"ARC\": {\"CI_excludes_zero\": true, \"N\": 16, \"PPP\": 0.003, \"R_hat_max\": 1.01, \"cal_MAE\": 0.0201, \"delta_MAE\": 0.0136, \"gamma_hat\": 0.73}, \"GSM8K\": {\"CI_excludes_zero\": false, \"N\": 24, \"PPP\": 0.541, \"R_hat_max\": 1.01, \"cal_MAE\": 0.0062, \"delta_MAE\": 0.1632, \"gamma_hat\": 0.06}, \"MMLU\": {\"CI_excludes_zero\": false, \"N\": 16, \"PPP\": 0.193, \"R_hat_max\": 1.01, \"cal_MAE\": 0.0072, \"delta_MAE\": 0.0083, \"gamma_hat\": 0.7}, \"note\": \"N=16 fixed (naming normalization applied), 0 divergences, ESS>1300\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-16T17:14:07.907Z\"}, \"exp006_pooled_irt_n16_fixed\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-16T17:12:22.909Z\", \"status\": \"DONE\", \"updated_at\": \"2026-05-16T17:12:55.073Z\"}, \"exp_001_eval_05B_instruct\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-16T14:42:17.521Z\", \"status\": \"DONE\", \"updated_at\": \"2026-05-16T16:32:10.317Z\"}, \"exp_001_eval_llama32_3B_d000_s42\": {\"conclusion\": \"killed\", \"created_at\": \"2026-05-16T13:22:13.996Z\", \"metrics\": {\"MMLU\": 0.4545}, \"status\": \"DONE\", \"updated_at\": \"2026-05-16T15:36:02.236Z\"}, \"exp_001_eval_15B_instruct\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-16T12:57:49.119Z\", \"metrics\": {\"ARC\": 0.7654, \"GSM8K\": 0.5929, \"MMLU\": 0.5775}, \"status\": \"DONE\", \"updated_at\": \"2026-05-16T15:36:01.221Z\"}, \"exp_006_mmlu_domain_gamma_n24_v4\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-16T13:51:12.494Z\", \"metrics\": {\"Business_Law_gamma\": \"not_significant\", \"CS_Eng_gamma\": \"not_significant\", \"Humanities_gamma\": \"negative_significant\", \"Medical_gamma\": \"negative_significant\", \"STEM_Math_gamma\": \"positive_significant\", \"STEM_Science_gamma\": \"positive_significant\", \"Social_Sciences_gamma\": \"negative_significant\", \"domains\": 7, \"note\": \"CmdStan crashed after results saved. Humanities rhat=1.014 not converged.\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-16T15:02:32.927Z\"}, \"exp_006_pooled_irt_rrf_n25_v2\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-16T14:36:11.037Z\", \"metrics\": {\"arc_N8_4PLgamma\": \"over_parameterized_cal_worsens\", \"gsm8k_N16_delta_mae\": 0.118, \"gsm8k_calibration\": \"effective\", \"mmlu_N8_4PLgamma\": \"over_parameterized_cal_worsens\", \"note\": \"GSM8K N=16 works. MMLU/ARC N=8 with 4PL+gamma over-parameterized, PPP=0.006/0.000, cal_mae > raw_mae. Need 2PL+gamma or N>=16.\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-16T15:02:31.098Z\"}, \"exp_003_rrf_full_n25_latest\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-16T14:35:17.463Z\", \"status\": \"DONE\", \"updated_at\": \"2026-05-16T14:35:52.664Z\"}, \"signals_05B_s123_v2\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-16T11:01:32.305Z\", \"status\": \"DONE\", \"updated_at\": \"2026-05-16T14:29:42.698Z\"}, \"exp_006_pooled_irt_n25\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-16T13:21:30.396Z\", \"status\": \"DONE\", \"updated_at\": \"2026-05-16T14:29:29.467Z\"}, \"exp_001_eval_3B_instruct_v2\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-16T11:16:34.089Z\", \"metrics\": {\"GSM8K\": 0.76, \"HumanEval\": 0.5, \"MMLU\": 0.605}, \"status\": \"DONE\", \"updated_at\": \"2026-05-16T14:29:28.489Z\"}, \"exp_006_mmlu_domain_gamma_n24_v3\": {\"conclusion\": \"failed\", \"created_at\": \"2026-05-16T13:12:59.287Z\", \"metrics\": {\"Humanities\": {\"CI\": [-0.776, -0.041], \"N\": 21, \"PPP\": 1, \"converged\": \"borderline_rhat_1.014\", \"excludes_zero\": true, \"gamma_mean\": -0.407}, \"Medical\": {\"CI\": [-0.338, -0.06], \"N\": 24, \"PPP\": 1, \"converged\": true, \"excludes_zero\": true, \"gamma_mean\": -0.199}, \"STEM_CS_Eng\": {\"CI\": [-0.448, 0.835], \"N\": 23, \"PPP\": 0.892, \"converged\": true, \"excludes_zero\": false, \"gamma_mean\": 0.197}, \"STEM_Math\": {\"CI\": [0.527, 1.43], \"N\": 23, \"PPP\": 0.438, \"converged\": true, \"excludes_zero\": true, \"gamma_mean\": 0.969}, \"STEM_Science\": {\"CI\": [0.385, 1.274], \"N\": 23, \"PPP\": 0.807, \"converged\": true, \"excludes_zero\": true, \"gamma_mean\": 0.838}, \"completed_domains\": 5, \"crashed\": \"Social_Sciences (CmdStan retcode=[1,0,0,1])\", \"not_run\": [\"Business_Law\", \"Other\"], \"total_domains\": 8}, \"status\": \"DONE\", \"updated_at\": \"2026-05-16T13:50:52.887Z\"}, \"exp_002_signals_15B_d100_s123_cuda2\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-16T10:07:31.281Z\", \"status\": \"DONE\", \"updated_at\": \"2026-05-16T13:12:48.641Z\"}, \"exp_002_signals_15B_s123_batch\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-16T03:44:39.543Z\", \"status\": \"DONE\", \"updated_at\": \"2026-05-16T13:12:47.455Z\"}, \"exp_006_mmlu_domain_gamma_n24\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-16T11:49:54.108Z\", \"metrics\": {\"STEM_CS_Eng\": {\"N_items\": 557, \"N_models\": 23, \"PPP\": 0.892, \"fit_time_s\": 153, \"gamma_excludes_zero\": false, \"gamma_mean\": 0.197}, \"STEM_Math\": {\"N_items\": 1190, \"N_models\": 23, \"PPP\": 0.438, \"fit_time_s\": 527, \"gamma_excludes_zero\": true, \"gamma_mean\": 0.969}, \"STEM_Science\": {\"N_items\": 1397, \"N_models\": 23, \"PPP\": 0.807, \"fit_time_s\": 618, \"gamma_excludes_zero\": true, \"gamma_mean\": 0.838}, \"domains_completed\": 3, \"domains_total\": 8, \"note\": \"3/8 domains complete. Process stopped after 3 — remaining 5 need restart.\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-16T13:11:38.602Z\"}, \"exp_006_mmlu_domain_gamma_n24_v2\": {\"conclusion\": \"failed\", \"created_at\": \"2026-05-16T12:28:48.496Z\", \"status\": \"DONE\", \"updated_at\": \"2026-05-16T13:11:28.954Z\"}, \"exp_001_sft_llama32_3B_d000_s42\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-16T10:34:27.989Z\", \"metrics\": {\"epoch\": 1, \"mean_token_accuracy\": 0.6685, \"train_loss\": 1.5165, \"train_runtime_sec\": 8170}, \"status\": \"DONE\", \"updated_at\": \"2026-05-16T12:56:14.562Z\"}, \"exp_002_signals_05B_s123_v2\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-16T03:03:30.869Z\", \"status\": \"DONE\", \"updated_at\": \"2026-05-16T12:31:01.649Z\"}, \"exp_001_sft_3B_d100_s123_a32\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-15T16:10:37.632Z\", \"hypothesis\": \"3B d100 s123 alpha=32 SFT. D055 rerun: previous exp_001_sft_3B_d100_s123 used alpha=16. 100% contamination with seed=123 for cross-seed consistency. Priority 2: submit after d100_s42 or d025_s42 completes.\", \"parent\": \"exp_001_sft_3B_d100_s123\", \"status\": \"DONE\", \"updated_at\": \"2026-05-16T11:29:48.114Z\"}, \"exp_002_signals_3B_d100_a32_s42\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-16T07:29:33.942Z\", \"metrics\": {\"benchmarks_completed\": [\"mmlu\", \"gsm8k\", \"arc_challenge\"], \"signals_generated\": [\"s1_embedding\", \"s2_minkpp\", \"s4_selfcritique\"], \"status_note\": \"Signals validated via pooled IRT (exp_006_pooled_irt_all_scales, N=23 success). Analysis worker completed 2026-05-16T10:50:52 but callback not processed due to session reset.\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-16T11:16:32.111Z\"}, \"exp_006_pooled_irt_all_scales\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-16T11:01:03.057Z\", \"metrics\": {\"arc_challenge\": {\"cal_mae\": 0.0153, \"delta_mae\": 0.0183, \"divergences\": 0, \"ess\": 1670, \"gamma_ci95\": [-0.2552, 1.2529], \"gamma_mean\": 0.4859, \"n_items\": 300, \"n_models\": 13, \"ppp\": 0.027, \"raw_mae\": 0.0335, \"rhat\": 1.0065}, \"exposure\": \"rrf_signal\", \"gsm8k\": {\"cal_mae\": 0.0078, \"delta_mae\": 0.1552, \"divergences\": 0, \"ess\": 1388, \"gamma_ci95\": [-0.2889, 0.637], \"gamma_mean\": 0.1721, \"n_items\": 300, \"n_models\": 20, \"ppp\": 0.3425, \"raw_mae\": 0.163, \"rhat\": 1.0071}, \"mmlu\": {\"cal_mae\": 0.0059, \"delta_mae\": 0.0098, \"divergences\": 0, \"ess\": 1402, \"gamma_ci95\": [-0.5501, 1.5974], \"gamma_mean\": 0.5172, \"n_items\": 300, \"n_models\": 15, \"ppp\": 0.2335, \"raw_mae\": 0.0157, \"rhat\": 1.0067}, \"model_type\": \"2pl_gamma\", \"rrf_respondents\": 23, \"scales\": [\"0.5B\", \"1.5B\", \"3B\"]}, \"status\": \"DONE\", \"updated_at\": \"2026-05-16T11:01:48.418Z\"}, \"exp_001_eval_3B_instruct_aligned_para\": {\"conclusion\": \"failed\", \"created_at\": \"2026-05-16T07:54:58.792Z\", \"hypothesis\": \"Qwen2.5-3B-Instruct (RL post-trained) eval. P0-C RL observational: verify signal patterns after RLHF. No training, inference only. Aligned + para_aligned on 4 benchmarks.\", \"status\": \"DONE\", \"updated_at\": \"2026-05-16T10:35:04.466Z\"}, \"exp_002_signals_3B_d000_a32_s42\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-16T07:09:17.976Z\", \"metrics\": {\"benchmarks\": {\"arc_challenge\": {\"n_items\": 1172, \"signals\": [\"s1_embedding\", \"s2_minkpp\", \"s4_selfcritique\"]}, \"gsm8k\": {\"n_items\": 1319, \"signals\": [\"s1_embedding\", \"s2_minkpp\", \"s4_selfcritique\"]}, \"mmlu\": {\"n_items\": 14042, \"signals\": [\"s1_embedding\", \"s2_minkpp\", \"s4_selfcritique\"]}}, \"output_files\": {\"signal_s1_embedding_arc_challenge.json\": \"650K\", \"signal_s1_embedding_gsm8k.json\": \"717K\", \"signal_s1_embedding_mmlu.json\": \"7.6M\", \"signal_s2_minkpp_arc_challenge.json\": \"245K\", \"signal_s2_minkpp_gsm8k.json\": \"266K\", \"signal_s2_minkpp_mmlu.json\": \"2.8M\", \"signal_s4_selfcritique_arc_challenge.json\": \"284K\", \"signal_s4_selfcritique_gsm8k.json\": \"310K\", \"signal_s4_selfcritique_mmlu.json\": \"3.2M\"}, \"runtime_minutes\": 189, \"signals_completed\": 9, \"signals_failed\": 0}, \"status\": \"DONE\", \"updated_at\": \"2026-05-16T10:23:58.349Z\"}, \"exp_002_signals_3B_d005_a32_s42\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-16T06:51:39.086Z\", \"notes\": \"Cron false positive: signals pipeline不用W&B, cron检测不到metrics误判为failed. 实际已全部完成: s1+s2+s4 × mmlu+gsm8k+arc_challenge, 输出merged json在 /root/autodl-tmp/exp002/signals/Qwen2.5-3B_d005_a32_s42/. GPU cuda:2 已释放.\", \"status\": \"DONE\", \"updated_at\": \"2026-05-16T10:11:52.002Z\"}, \"exp_006_pooled_irt_05b_15b\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-16T09:10:10.904Z\", \"metrics\": {\"arc_cal_mae\": 0.0682, \"arc_ci95\": \"[-0.271, 2.857]\", \"arc_delta_mae\": -0.064, \"arc_ess\": 1480, \"arc_gamma\": 1.2259, \"arc_n_models\": 5, \"arc_ppp\": 0, \"arc_raw_mae\": 0.0042, \"arc_rhat\": 1.0072, \"gsm8k_cal_mae\": 0.0373, \"gsm8k_ci95\": \"[-0.990, 1.019]\", \"gsm8k_delta_mae\": 0.1128, \"gsm8k_ess\": 1300, \"gsm8k_gamma\": 0.0128, \"gsm8k_n_models\": 11, \"gsm8k_ppp\": 0.663, \"gsm8k_raw_mae\": 0.1501, \"gsm8k_rhat\": 1.0072, \"n_items_subsampled\": 300}, \"status\": \"DONE\", \"updated_at\": \"2026-05-16T09:16:12.488Z\"}, \"exp006_pooled_rrf_irt_05b_15b\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-16T09:02:32.472Z\", \"hypothesis\": \"0.5B+1.5B pooled 4PL+γ IRT fitting with RRF signal-based exposure. Per-benchmark: GSM8K (N=11, 0.5B+1.5B) and ARC (N=5, 1.5B only per D045). Pipeline validation for γ̂ estimates before N≥16 final run.\", \"metrics\": {\"arc_challenge\": {\"cal_mae\": 0.0682, \"delta_mae\": -0.064, \"divergences\": 0, \"ess\": 1480, \"gamma_ci95\": [-0.2711, 2.8571], \"gamma_mean\": 1.2259, \"n_items\": 300, \"n_models\": 5, \"ppp\": 0, \"raw_mae\": 0.0042, \"rhat\": 1.0072}, \"gsm8k\": {\"cal_mae\": 0.0373, \"delta_mae\": 0.1128, \"divergences\": 0, \"ess\": 1300, \"gamma_ci95\": [-0.99, 1.0187], \"gamma_mean\": 0.0128, \"n_items\": 300, \"n_models\": 11, \"ppp\": 0.663, \"raw_mae\": 0.1501, \"rhat\": 1.0072}}, \"status\": \"DONE\", \"updated_at\": \"2026-05-16T09:08:42.567Z\"}, \"exp006_pooled_rrf_irt_05b_15b_v2\": {\"created_at\": \"2026-05-16T09:05:27.235Z\", \"status\": \"PREPARING\", \"updated_at\": \"2026-05-16T09:05:27.235Z\"}, \"exp_006_mmlu_domain_gamma\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-16T07:53:25.491Z\", \"metrics\": {\"Business_Law_gamma\": 0.61, \"Humanities_gamma\": 0.47, \"Medical_gamma\": 0.27, \"Other_gamma\": 1.34, \"STEM_CS_Eng_gamma\": 0.29, \"STEM_Math_gamma\": -0.55, \"STEM_Science_gamma\": 0.36, \"Social_Sciences_gamma\": 0.28, \"all_rhat_max\": 1.008, \"divergent_transitions\": 0, \"n_domains\": 8, \"n_models\": 16}, \"status\": \"DONE\", \"updated_at\": \"2026-05-16T08:55:20.713Z\"}, \"exp_001_eval_3B_d005_s42_para_aligned\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-15T18:23:16.191Z\", \"hypothesis\": \"3B d005 s42 para_aligned eval. Missing slot for complete s42 para_aligned matrix. Will submit when cuda:3 frees up after d100_s123_para_aligned completes.\", \"metrics\": {\"arc_challenge_acc\": 0.8164, \"arc_challenge_n\": 697, \"gsm8k_acc\": 0.3421, \"gsm8k_n\": 228, \"humaneval_n\": 26, \"humaneval_pass1\": 0.0769, \"mmlu_acc\": 0.6471, \"mmlu_n\": 6596}, \"status\": \"DONE\", \"updated_at\": \"2026-05-16T07:09:18.839Z\"}, \"exp_001_eval_3B_d000_s42_a32_para_aligned\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-16T00:49:07.136Z\", \"hypothesis\": \"3B d000 s42 alpha=32 para_aligned eval. Uses D076-retrained checkpoint (lr=5e-5). Paraphrased benchmark eval for contamination signal computation.\", \"metrics\": {\"arc_para\": 0.8106, \"gsm8k_para\": 0.0526, \"humaneval_para\": 0.1923, \"mmlu_para\": 0.6431}, \"status\": \"DONE\", \"updated_at\": \"2026-05-16T07:07:32.858Z\"}, \"exp_001_eval_3B_d005_s42_a32_batch\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-16T02:16:39.223Z\", \"metrics\": {\"arc\": 0.8251, \"arc_para\": 0.8164, \"gsm8k\": 0.4147, \"gsm8k_para\": 0.3421, \"humaneval\": 0.1341, \"humaneval_para\": 0.0769, \"mmlu\": 0.6308, \"mmlu_para\": 0.6471}, \"status\": \"DONE\", \"updated_at\": \"2026-05-16T06:58:54.626Z\"}, \"exp_008_instruct_rl_proxy\": {\"conclusion\": \"failed\", \"created_at\": \"2026-05-14T16:44:57.410Z\", \"hypothesis\": \"RL proxy experiment (D021 Problem 3): Use Qwen2.5-0.5B-Instruct (SFT+RL post-trained) as RL regime data point. 3-regime comparison: base (pretrained) → d000 (SFT) → Instruct (SFT+RL). Compute all 4 signals on Instruct model, observe signal value changes across training regimes. No additional training needed.\\\"\", \"metrics\": {\"base_pretrained_signals\": \"computing_PID_701898_GPU5\", \"comparison\": {\"arc\": {\"d000_sft_s2\": 1.7079, \"d000_sft_s4\": -0.9538, \"instruct_s2\": 1.6737, \"instruct_s4\": -0.9227, \"s4_delta_instruct_vs_sft\": 0.0311}, \"gsm8k\": {\"d000_sft_s2\": 1.6532, \"d000_sft_s4\": -0.9408, \"instruct_s2\": 1.7073, \"instruct_s4\": -0.9632, \"s4_delta_instruct_vs_sft\": -0.0224}, \"mmlu\": {\"base_s2\": 1.7009, \"base_s4\": \"computing\", \"d000_sft_s2\": 1.6976, \"d000_sft_s4\": -0.9557, \"instruct_s2\": 1.6952, \"instruct_s4\": -0.8782, \"s4_delta_instruct_vs_sft\": 0.0775}}, \"d000_sft_signals_complete\": true, \"instruct_signals_complete\": true, \"key_finding\": \"S4 differentiates regimes (MMLU +0.078, ARC +0.031 Instruct vs SFT); S2 does not (<0.01 difference). RL increases S4 entropy on knowledge benchmarks.\", \"signal_paths\": {\"base_pretrained\": \"/root/autodl-tmp/exp008/signals/base_pretrained/\", \"d000_sft\": \"/root/autodl-tmp/exp002/signals/Qwen2.5-0.5B_d000_s42/\", \"instruct\": \"/root/autodl-tmp/exp008/signals/rl_aligned/\"}}, \"status\": \"DONE\", \"updated_at\": \"2026-05-16T05:25:04.558Z\"}, \"exp_003_mmlu_item_aligned_gap\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-14T20:44:01.524Z\", \"metrics\": {\"aggregate\": {\"max_abs_gap_pp\": 3.73, \"mean_gap_pp\": -2.243, \"median_gap_pp\": -2.259, \"std_gap_pp\": 0.671}, \"alignment_correction\": {\"conclusion\": \"Proper item-ID alignment changes result by <0.3pp vs naive positional comparison\", \"misaligned_vs_aligned_diff_pp\": \"<0.3 (confirmed from prior 2-pair check)\"}, \"by_contamination\": {\"d000\": {\"mean_pp\": -2.292, \"n\": 5}, \"d005\": {\"mean_pp\": -2.181, \"n\": 6}, \"d025\": {\"mean_pp\": -1.913, \"n\": 5}, \"d100\": {\"mean_pp\": -2.687, \"n\": 4}}, \"by_size\": {\"0.5B\": {\"mean_pp\": -2.259, \"n\": 4, \"std_pp\": 1.238}, \"1.5B\": {\"mean_pp\": -2.452, \"n\": 8, \"std_pp\": 0.31}, \"3B\": {\"mean_pp\": -2.026, \"n\": 8, \"std_pp\": 0.415}}, \"n_common_items\": 6596, \"n_pairs\": 20, \"per_item\": {\"mean_disagree_rate_pct\": 15.5, \"n_flagged_items\": 426, \"pct_aligned_easier\": 6.6, \"pct_high_disagree_gt50\": 6.5, \"pct_neutral_lt03pp\": 84.8, \"pct_para_easier\": 8.6}, \"prior_2pair_check\": {\"15B_d100\": {\"aligned_gap_pp\": -2.9, \"qc_selection_bias_pp\": 0.56}, \"3B_d100\": {\"aligned_gap_pp\": -3.5, \"qc_selection_bias_pp\": -0.08}}}, \"notes\": \"(a) para > aligned is a systematic artifact (paraphrase versions are inherently easier), not a contamination signal — mean gap is -2.24pp across all 20 pairs. (b) Cross-dosage comparison has model-size confound: d000 includes 0.5B data (4 pairs) while d100 only has 1.5B+3B (4 pairs). Within-size analysis controls for this: 1.5B d100-d000 delta = -0.71pp, 3B d100-d000 delta = -0.80pp — both show d100 widens the gap modestly. (c) If any signal uses raw aligned-para gap as contamination indicator, must apply baseline correction: subtract same-size same-seed d000 gap to isolate contamination effect from inherent paraphrase easiness.\", \"status\": \"DONE\", \"updated_at\": \"2026-05-16T05:05:03.598Z\"}, \"exp_001_eval_3B_d025_s42_a32_para\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-16T03:40:59.842Z\", \"metrics\": {\"arc_challenge_para\": 0.8106, \"gsm8k_para\": \"completed\", \"humaneval_para\": 0, \"mmlu_para\": \"completed_6596_items\", \"output_dir\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d025_v3_s42_para_aligned\", \"sentinel\": \".done exists\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-16T04:44:05.709Z\"}, \"exp_002_signals_3B_d025_v3_s42\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-16T00:18:12.521Z\", \"hypothesis\": \"计算 d025_v3_s42 的 s4 (self-critique) signal（s1/s2 已有，s3 因 eval 结果缺失被阻塞）\", \"notes\": \"父进程 PID 663047 被 kill 后子进程 PID 663067 继续完成了所有计算。9/9 信号文件完整：s1×3, s2×3, s4×3。日志显示 ALL_DONE at 2026-05-16 10:58:37。\", \"status\": \"DONE\", \"updated_at\": \"2026-05-16T04:08:05.756Z\"}, \"exp_002_signals_3B_v9\": {\"conclusion\": \"failed\", \"created_at\": \"2026-05-16T01:07:17.816Z\", \"hypothesis\": \"v9: Chunked s4 fix. Compute remaining signals for d025_s123 (mmlu s4) and d100_a32_s123 (mmlu s4, gsm8k all, arc all) on cuda:4\", \"notes\": \"Wrapper PID 668217 exited (no exit code). d025_s123 mmlu s4 COMPLETE (14042 items, merged). d100_a32_s123 mmlu s4 IN PROGRESS via orphan PID 689315 on cuda:4 (2/15 chunks at 11:49). d100_a32_s123 gsm8k/arc NOT STARTED — wrapper dead, won't auto-continue. Need new submission for gsm8k+arc after 689315 finishes.\", \"status\": \"DONE\", \"updated_at\": \"2026-05-16T03:52:09.155Z\"}, \"exp_001_sft_3B_d025_s42_a32_v3\": {\"conclusion\": \"killed\", \"created_at\": \"2026-05-15T23:26:36.542Z\", \"hypothesis\": \"D076 retrain retry: 3B d025 s42 SFT with lr=5e-5, alpha=32. v2 was SIGTERM'd at step 22/3384 by cuda:3 contention (eval batch took over). Same command, resubmit when GPU frees.\", \"notes\": \"D086 confirmed existing d025_v3_s42 checkpoint valid (alpha=32); redundant retrain killed per Reviewer CRITICAL\", \"parent\": null, \"status\": \"DONE\", \"updated_at\": \"2026-05-16T03:02:43.792Z\"}, \"exp_001_eval_3B_d025_v3_s42_batch\": {\"conclusion\": \"killed\", \"created_at\": \"2026-05-15T23:23:13.337Z\", \"status\": \"DONE\", \"updated_at\": \"2026-05-16T02:45:33.866Z\"}, \"exp_002_signals_05B_s123_batch\": {\"conclusion\": \"failed\", \"created_at\": \"2026-05-16T01:47:18.455Z\", \"hypothesis\": \"D097: Batch compute all signals (s1+s2+s4) for 4× Qwen2.5-0.5B s123 checkpoints (d000/d005/d025/d100) × 3 benchmarks (mmlu/gsm8k/arc). Adds +4 respondents to signal-backed IRT pool N.\", \"status\": \"DONE\", \"updated_at\": \"2026-05-16T02:19:56.843Z\"}, \"exp_002_signals_3B_v7\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-15T23:05:17.855Z\", \"metrics\": {\"benchmarks\": [\"mmlu\", \"gsm8k\", \"arc_challenge\"], \"merged_files\": 3, \"output_dir\": \"/root/autodl-tmp/exp002/signals/Qwen2.5-3B_d005_s123/\", \"signal_files\": 9, \"signals\": [\"s1_embedding\", \"s2_minkpp\", \"s4_selfcritique\"]}, \"status\": \"DONE\", \"updated_at\": \"2026-05-16T02:16:18.925Z\"}, \"exp_001_sft_3B_d100_s42_a32_v3\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-15T20:12:40.784Z\", \"hypothesis\": \"3B d100 s42 alpha=32 SFT v3. Resubmit after v2 SIGTERM at 73%. 100% contamination with seed=42 for dose-response curve.\", \"metrics\": {\"entropy\": 1.296, \"final_epoch\": 1, \"mean_token_accuracy\": 0.7186, \"total_steps\": 4159, \"train_loss\": 1.1795, \"train_runtime_sec\": 17645, \"train_samples_per_second\": 3.771, \"train_steps_per_second\": 0.236}, \"parent\": \"exp_001_sft_3B_d100_s42_a32_v2\", \"status\": \"DONE\", \"updated_at\": \"2026-05-16T02:01:17.101Z\"}, \"exp_001_sft_3B_d005_s42_a32\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-15T20:09:46.602Z\", \"hypothesis\": \"D076 retrain: 3B d005 s42 with lr=5e-5, alpha=32. Replaces deprecated exp_001_sft_d005_3B (lr=2e-4 confound). Submit to cuda:0 or cuda:1 after d100 SFT completes.\", \"metrics\": {\"epoch\": 1, \"final_loss\": 1.0822, \"mean_token_accuracy\": 0.7511, \"steps\": 3177, \"train_runtime_sec\": 14913.5}, \"status\": \"DONE\", \"updated_at\": \"2026-05-16T02:01:02.242Z\"}, \"exp_002_signals_3B_v8_recovery\": {\"conclusion\": \"failed\", \"created_at\": \"2026-05-16T00:43:27.157Z\", \"hypothesis\": \"Recovery from v8 OOM: compute all signals for d100_a32_s123/mmlu on cuda:4. gsm8k+arc still pending after this.\", \"status\": \"DONE\", \"updated_at\": \"2026-05-16T01:07:00.460Z\"}, \"exp_004_sim_sweep_v7\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-15T18:11:07.346Z\", \"metrics\": {\"ci95_coverage_range\": \"[0.8, 1.0]\", \"conditions_failed\": \"auc0.65_n20/n50/n100 (CmdStan TMPDIR race)\", \"conditions_ok\": 9, \"conditions_total\": 12, \"gamma_bias_range\": \"[-0.025, +0.056]\", \"gamma_rmse_range\": \"[0.005, 0.085]\", \"note\": \"9/12 sufficient for Claim 1 identifiability\", \"theta_corr_range\": \"[0.947, 0.972]\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-16T00:54:32.268Z\"}, \"exp_001_eval_3B_d000_s42_a32_aligned\": {\"created_at\": \"2026-05-16T00:49:00.839Z\", \"hypothesis\": \"3B d000 s42 alpha=32 aligned eval. Uses D076-retrained checkpoint (lr=5e-5). 0% contamination baseline for s42 IRT pool. Prerequisite for para_aligned eval and signals.\", \"status\": \"PREPARING\", \"updated_at\": \"2026-05-16T00:49:00.840Z\"}, \"exp_001_sft_3B_d000_s42_a32\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-15T20:09:31.942Z\", \"hypothesis\": \"D076 retrain: 3B d000 s42 SFT with lr=5e-5, alpha=32, seed=42, dosage=0%. Replaces deprecated d000_s42 (lr=2e-4 confound). Submit to cuda:0 or cuda:1 after d100 SFT completes.\", \"metrics\": {\"epoch\": 1, \"final_loss\": 1.1324, \"steps\": 3125}, \"status\": \"DONE\", \"updated_at\": \"2026-05-16T00:42:10.415Z\"}, \"exp_002_signals_3B_v8\": {\"conclusion\": \"failed\", \"created_at\": \"2026-05-15T23:41:07.377Z\", \"notes\": \"Process Killed (OOM) during s4_selfcritique mmlu. Partial completion: d025_s123 gsm8k+arc_challenge complete (s1,s2,s4,merged); d025_s123 mmlu has s1+s2 only (s4 killed at 388/7021); d100_a32_s123 mmlu has s1+s2 only (s4 stopped at 203/7021); d100_a32_s123 gsm8k+arc_challenge not started. New PID 662616 running d100_a32_s123/mmlu on cuda:4 as recovery.\", \"status\": \"DONE\", \"updated_at\": \"2026-05-16T00:35:24.181Z\"}, \"exp_002_signals_3B_v5\": {\"conclusion\": \"failed\", \"created_at\": \"2026-05-15T19:43:59.775Z\", \"hypothesis\": \"3B signals v5. Parallel with v4 (cuda:3). Compute embedding/minkpp/selfcritique for d025 and d100 only. Accelerates signal coverage by splitting workload across cuda:3 (v4) and cuda:4 (v5).\", \"notes\": \"失败原因: EXIT_CODE=129 (SIGHUP), 实际是 d100_s42/mmlu selfcritique 在 22% 处被 SIGTERM (D078/D079 orphan 清理). 3/4 batch tasks 完成 (d025_s42/mmlu PASS, d100_s42/gsm8k PASS, d100_s42/arc_challenge PASS). 已有成果: d025_s42 和 d100_s42 的 gsm8k+arc signals 已写盘, 但这些 signals 基于旧 alpha=16 checkpoint, D076 重训 alpha=32 后需全部重算, 无需单独 retry. 建议: 等 cuda:1 d100_s42_v3 + cuda:5 d000_s42 重训完成后, 用新 checkpoint 统一重算 3B s42 signals.\", \"status\": \"DONE\", \"updated_at\": \"2026-05-15T23:59:48.258Z\"}, \"exp_001_sft_3B_d025_s42_a32_v2\": {\"conclusion\": \"failed\", \"created_at\": \"2026-05-15T23:18:30.617Z\", \"hypothesis\": \"D076 retrain: 3B d025 s42 SFT with lr=5e-5, alpha=32. Replaces deprecated d025_s42 (alpha=16). 25% contamination with seed=42. Fills missing dosage level in s42 a32 series (d000/d005/d100 already running).\", \"notes\": \"SIGTERM at step 22/3384 (~1.5min training). Training was healthy (no OOM/NaN/error, 4.3s/step pace). bitsandbytes libnvJitLink warning non-fatal. External kill matches D083 pattern. LoRA config confirmed: r=16, alpha=32, lr=5e-5. Need v3 resubmit on cuda:3.\", \"status\": \"DONE\", \"updated_at\": \"2026-05-15T23:25:18.379Z\"}, \"exp_001_eval_15B_s123_para_aligned_batch\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-15T20:08:58.408Z\", \"hypothesis\": \"1.5B s123 para_aligned eval batch (d000/d005/d025/d100). Fills 4 missing cells to complete 1.5B para_aligned matrix (s42 all done, s123 all missing). Adds 4 models to pooled IRT N count (N=19→23).\", \"metrics\": {\"d000_s123_para_aligned\": {\"arc_challenge\": 0.7547, \"gsm8k\": 0.5921, \"humaneval\": 0.1538, \"mmlu\": 0.6111}, \"d005_s123_para_aligned\": {\"arc_challenge\": 0.7475, \"gsm8k\": 0.5439, \"humaneval\": 0.0769, \"mmlu\": 0.614}, \"d025_s123_para_aligned\": {\"arc_challenge\": 0.7504, \"gsm8k\": 0.5482, \"humaneval\": 0.1923, \"mmlu\": 0.6145}, \"d100_s123_para_aligned\": {\"arc_challenge\": 0.7834, \"gsm8k\": 0.5307, \"humaneval\": 0.2308, \"mmlu\": 0.629}}, \"status\": \"DONE\", \"updated_at\": \"2026-05-15T23:04:53.646Z\"}, \"exp_001_sft_3B_d100_s42_a32_v2\": {\"conclusion\": \"failed\", \"created_at\": \"2026-05-15T16:30:30.968Z\", \"notes\": \"D083 SIGTERM root cause: Worker agent itself sent SIGTERM via ssh_execute (not OOM/cron/manual). v1 had no CUDA_VISIBLE_DEVICES, landed on occupied GPU 0, Worker detected conflict and killed. v2 killed at 72% progress (step 3030/4159, ~3.5h GPU time lost) without checkpoint save. v3 fixed with explicit CUDA_VISIBLE_DEVICES=2. ssh_execute kill commands don't appear in bash_history, making post-mortem difficult.\", \"status\": \"DONE\", \"updated_at\": \"2026-05-15T21:32:42.069Z\"}, \"exp_001_sft_3B_d025_s42_a32\": {\"conclusion\": \"killed\", \"created_at\": \"2026-05-15T16:10:35.236Z\", \"hypothesis\": \"3B d025 s42 alpha=32 SFT. D055 rerun: previous exp_001_sft_d025_3B_v2 used alpha=16. 25% contamination dosage with seed=42. Mid-range dosage point for IRT calibration curve.\", \"notes\": \"Killed: duplicate of exp_001_sft_d025_3B_v3 (cuda:5, same config d025 s42 alpha=32). Freed cuda:2 for critical-path exp_001_eval_3B_d100_s123_para_aligned_v2 re-run.\", \"parent\": \"\", \"status\": \"DONE\", \"updated_at\": \"2026-05-15T20:58:29.239Z\"}, \"exp_001_sft_3B_d100_s42_a32\": {\"conclusion\": \"killed\", \"created_at\": \"2026-05-15T16:10:33.228Z\", \"hypothesis\": \"3B d100 s42 alpha=32 SFT. D055 rerun: previous exp_001_sft_d100_3B_v2 used alpha=16. 100% contamination dosage with seed=42. Critical for IRT calibration contamination effect measurement.\", \"notes\": \"Retry #2 running on cuda:1 (PID 593745, 1h25m). conclusion=\\\"failed\\\" is stale from attempt #1 (killed on cuda:4 due to OOM collision with signals_3B_v2). Current process is healthy. Registry does not allow clearing conclusion while RUNNING.\", \"parent\": \"exp_001_sft_d100_3B_v2\", \"status\": \"DONE\", \"updated_at\": \"2026-05-15T20:58:25.304Z\"}, \"exp_001_sft_d025_3B_v3\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-15T16:10:02.763Z\", \"hypothesis\": \"3B d025 s42 alpha=32 SFT. Per D055 rerun with unified alpha=32 (v2 used alpha=16). 25% contamination dosage.\", \"metrics\": {\"entropy\": 1.1807, \"epoch\": 1, \"mean_token_accuracy\": 0.734, \"total_steps\": 3384, \"train_loss\": 1.1464, \"train_runtime_s\": 14584}, \"notes\": \"Cron falsely detected as failed (process dead 5x no sentinel). Worker manual check confirmed training completed successfully. Checkpoint verified: /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d025_s42/lora_adapter/adapter_model.safetensors (114MB). cuda:5 freed.\", \"parent\": \"exp_001_sft_d025_3B_v2\", \"status\": \"DONE\", \"updated_at\": \"2026-05-15T20:52:04.150Z\"}, \"exp_002_signals_3B_v6\": {\"conclusion\": \"failed\", \"created_at\": \"2026-05-15T20:06:35.655Z\", \"hypothesis\": \"D075/D077: Compute embedding/minkpp/selfcritique for d000_v2_s42 (lr=5e-5, alpha=16, confirmed valid) across mmlu/gsm8k/arc on cuda:3. Step 1 of signals recovery after d000_s42 invalidation.\", \"notes\": \"s1_embedding and s2_minkpp completed for all 3 benchmarks (mmlu: 14042, gsm8k: 1319, arc_challenge: 1172). s3_constat crashed on all benchmarks with ValueError: Item count mismatch (expected 1172, got 697 on arc). s4_selfcritique never ran. 6 signal files saved to /root/autodl-tmp/exp002/signals/Qwen2.5-3B_d000_v2_s42/. Bug is in s3_constat.py:50.\", \"parent\": \"exp_002_signals_3B_v5\", \"status\": \"DONE\", \"tags\": [\"alpha16_only\", \"interim_analysis\", \"not_for_irt_pool\"], \"updated_at\": \"2026-05-15T20:50:58.921Z\"}, \"exp_001_sft_d005_3B\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-14T08:54:49.962Z\", \"hypothesis\": \"5% dosage contaminated SFT on Qwen2.5-3B (seed=42): low-dosage contamination for 3B dose-response curve\", \"metrics\": {\"epochs\": 1, \"final_loss\": 1.11, \"total_steps\": 3177, \"training_hours\": 3.76}, \"notes\": \"DEPRECATED (D076): lr=2e-4 confound, excluded from IRT pool. Need retrain with lr=5e-5, alpha=32 → exp_001_sft_3B_d005_s42_a32.\", \"status\": \"DONE\", \"updated_at\": \"2026-05-15T20:09:08.691Z\"}, \"exp_002_signals_3B_v4\": {\"conclusion\": \"failed\", \"created_at\": \"2026-05-15T18:56:45.708Z\", \"hypothesis\": \"3B signals v4. Restart of v3 (killed accidentally). Compute embedding/minkpp/selfcritique for 3B model across d000/d005/d025/d100 × mmlu/gsm8k/arc. 5 combos already done, 7 remaining.\", \"notes\": \"诊断(2026-05-15): run_batch.py --signal 参数 bug 导致 11/12 combo rc=2 失败, d000/mmlu 被 SIGTERM (rc=-15)。Batch 0/12 passed。但有 5/12 combo 已有 merged 文件(d000/{gsm8k,arc}, d005/arc, d025/{gsm8k,arc})，来自早期或独立进程。v4 tmux session 确认死亡。多个 orphan 进程仍在 GPU 2/3/4 上跑 mmlu combos，有输出目录冲突风险。\", \"parent\": \"exp_002_signals_3B_v3\", \"status\": \"DONE\", \"updated_at\": \"2026-05-15T20:05:53.319Z\"}, \"exp_004_sim_sweep_extreme_gamma\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-15T19:51:43.363Z\", \"metrics\": {\"conditions\": 8, \"gamma2_avg_bias\": 0.017, \"gamma2_avg_rmse\": 0.101, \"gamma2_ci95_coverage\": 1, \"gamma4_avg_bias\": -0.106, \"gamma4_avg_rmse\": 0.226, \"gamma4_ci95_coverage\": 0.925, \"seeds_per_condition\": 10, \"theta_corr_range\": [0.914, 0.969], \"total_time_hours\": 11.1}, \"status\": \"DONE\", \"updated_at\": \"2026-05-15T19:52:58.007Z\"}, \"exp_001_eval_3B_d100_s123_para_aligned_v2\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-15T18:48:19.731Z\", \"hypothesis\": \"3B d100 s123 para_aligned eval v2. Resubmit after v1 OOM on GSM8K (22%). Last missing s123 para_aligned slot for N≥16 pooled IRT. Uses alpha=16 checkpoint (D051 accepted).\", \"metrics\": {\"arc_challenge\": {\"accuracy\": 0.8164, \"correct\": 569, \"total\": 697}, \"gsm8k\": {\"accuracy\": 0.5877, \"correct\": 134, \"total\": 228}, \"humaneval\": {\"correct\": 2, \"pass@1\": 0.0769, \"total\": 26}, \"mmlu\": {\"accuracy\": 0.6565, \"correct\": 4330, \"total\": 6596}}, \"parent\": \"exp_001_sft_3B_d100_s123\", \"status\": \"DONE\", \"updated_at\": \"2026-05-15T19:39:02.009Z\"}, \"exp_001_eval_3B_d100_s123_para_aligned\": {\"conclusion\": \"failed\", \"created_at\": \"2026-05-15T18:18:07.994Z\", \"hypothesis\": \"3B d100 s123 para_aligned eval. Last missing s123 para_aligned slot for N≥16 pooled IRT. Uses alpha=16 checkpoint (D051 accepted for s123).\", \"status\": \"DONE\", \"updated_at\": \"2026-05-15T19:18:30.012Z\"}, \"exp_001_sft_3B_d000_v3\": {\"conclusion\": \"failed\", \"created_at\": \"2026-05-15T16:06:14.299Z\", \"hypothesis\": \"3B d000 s42 alpha=32 SFT baseline. Per D050 unify LoRA alpha=32. Previous v2 used alpha=16. d000 is 0% contamination baseline, most critical for IRT calibration reference.\", \"notes\": \"失败原因: 进程在 step 1725/3125 (55%) 静默死亡，无 Traceback/OOM/CUDA error。cuda:4 双进程共存（SFT + signals ~20.7/24.5GB），高度疑似系统 OOM kill。| 诊断 Worker: worker_diagnose_exp_001_sft_3B_d000_v3_20260515T190929 | 建议: 诊断完成后单独使用 cuda:4 重跑\", \"parent\": \"exp_001_sft_3B_d000_v2\", \"status\": \"DONE\", \"updated_at\": \"2026-05-15T19:10:00.491Z\"}, \"exp_004_sim_sweep_v6\": {\"conclusion\": \"killed\", \"created_at\": \"2026-05-15T17:00:53.103Z\", \"status\": \"DONE\", \"updated_at\": \"2026-05-15T18:55:50.238Z\"}, \"exp_002_signals_3B_v3\": {\"conclusion\": \"killed\", \"created_at\": \"2026-05-15T18:38:09.043Z\", \"notes\": \"D065: PID 611720 silently died. Likely killed by OOM or crashed during selfcritique batch. Partial results: d000_s42 mmlu/gsm8k/arc 4 signals complete, d025_s42 mmlu s1+s2 partial. Superseded by v4 on cuda:3.\", \"status\": \"DONE\", \"updated_at\": \"2026-05-15T18:55:22.188Z\"}, \"exp_001_eval_3B_d005_s123_aligned\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-15T15:06:22.987Z\", \"hypothesis\": \"3B d005 s123 aligned eval. Chain from completed SFT. Critical for complete 3B seed=123 eval matrix.\", \"metrics\": {\"arc_challenge_accuracy\": 0.8242, \"gsm8k_exact_match\": 0.6308, \"humaneval_pass1\": 0.1037, \"mmlu_accuracy\": 0.6324}, \"status\": \"DONE\", \"updated_at\": \"2026-05-15T18:44:30.671Z\"}, \"exp_001_eval_3B_d025_s123_aligned\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-15T14:51:16.431Z\", \"metrics\": {\"arc_challenge\": 0.8336, \"gsm8k\": 0.5254, \"humaneval\": 0.1585, \"mmlu\": 0.6367}, \"status\": \"DONE\", \"updated_at\": \"2026-05-15T18:10:03.567Z\"}, \"exp_002_signals_3B_v2\": {\"conclusion\": \"killed\", \"created_at\": \"2026-05-15T16:06:11.669Z\", \"hypothesis\": \"3B signal computation rerun (v2). v1 failed with SIGTERM due to GPU mapping + argparse bug (now fixed). Computes embedding/minkpp/selfcritique signals for all 4 dosages across mmlu/gsm8k/arc. Prerequisite for signal-derived IRT calibration.\", \"notes\": \"PID 590509 confirmed dead (kill_job + check_job_status verified). Registry DONE/killed status correct. GPU 4 VRAM freed for d000_v3 SFT.\", \"parent\": \"exp_002_signals_3B\", \"status\": \"DONE\", \"updated_at\": \"2026-05-15T17:56:45.615Z\"}, \"exp_001_eval_3B_d005_s123_para_aligned\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-15T15:33:51.088Z\", \"metrics\": {\"ARC\": 0.8192, \"GSM8K\": 0.5, \"HumanEval\": 0.0769, \"MMLU\": 0.6461}, \"status\": \"DONE\", \"updated_at\": \"2026-05-15T16:56:44.749Z\"}, \"exp_001_eval_15B_d005_s123\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-15T11:05:33.959Z\", \"metrics\": {\"arc_challenge\": {\"accuracy\": 0.7568, \"correct\": 887, \"total\": 1172}, \"gsm8k\": {\"correct\": 855, \"exact_match\": 0.6482, \"total\": 1319}, \"humaneval\": {\"correct\": 41, \"pass@1\": 0.25, \"total\": 164}, \"mmlu\": {\"accuracy\": 0.5869, \"correct\": 8241, \"total\": 14042}}, \"status\": \"DONE\", \"updated_at\": \"2026-05-15T16:38:52.188Z\"}, \"exp_001_eval_15B_d005_s123_v2\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-15T13:52:49.837Z\", \"metrics\": {\"arc_challenge\": {\"accuracy\": 0.7568, \"correct\": 887, \"total\": 1172}, \"gsm8k\": {\"correct\": 855, \"exact_match\": 0.6482, \"total\": 1319}, \"humaneval\": {\"correct\": 41, \"pass@1\": 0.25, \"total\": 164}, \"mmlu\": {\"accuracy\": 0.5869, \"correct\": 8241, \"total\": 14042}}, \"status\": \"DONE\", \"updated_at\": \"2026-05-15T16:38:51.157Z\"}, \"exp_001_eval_15B_d025_s123\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-15T11:05:35.304Z\", \"metrics\": {\"arc_challenge\": {\"accuracy\": 0.7577, \"correct\": 888, \"total\": 1172}, \"gsm8k\": {\"correct\": 864, \"exact_match\": 0.655, \"total\": 1319}, \"humaneval\": {\"correct\": 41, \"pass@1\": 0.25, \"total\": 164}, \"mmlu\": {\"accuracy\": 0.5881, \"correct\": 8258, \"total\": 14042}}, \"notes\": \"Superseded by v2 entry. Same PID 566311, same results.\", \"status\": \"DONE\", \"updated_at\": \"2026-05-15T16:30:15.122Z\"}, \"exp_001_eval_15B_d025_s123_v2\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-15T13:52:50.883Z\", \"metrics\": {\"arc_challenge\": {\"accuracy\": 0.7577, \"correct\": 888, \"total\": 1172}, \"gsm8k\": {\"correct\": 864, \"exact_match\": 0.655, \"total\": 1319}, \"humaneval\": {\"correct\": 41, \"pass@1\": 0.25, \"total\": 164}, \"mmlu\": {\"accuracy\": 0.5881, \"correct\": 8258, \"total\": 14042}}, \"status\": \"DONE\", \"updated_at\": \"2026-05-15T16:29:37.273Z\"}, \"exp_001_sft_d025_3B_v2\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-14T23:55:27.835Z\", \"metrics\": {\"epochs\": 1, \"mean_token_accuracy\": 0.7342, \"runtime_seconds\": 14499, \"steps\": 3384, \"train_loss\": 1.1501}, \"notes\": \"SUPERSEDED by D055. alpha=16, replaced by exp_001_sft_3B_d025_s42_a32 (alpha=32).\", \"status\": \"DONE\", \"updated_at\": \"2026-05-15T16:28:07.226Z\"}, \"exp_001_sft_d100_3B_v2\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-14T18:25:23.780Z\", \"hypothesis\": \"3B d100 SFT v2 with D020 conservative params (lr=5e-5, alpha=16, r=16) to prevent CoT catastrophic forgetting. seed=42.\", \"metrics\": {\"checkpoint_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d100_s42/lora_adapter\", \"d020_params\": \"lr=5e-5, alpha=16, r=16\", \"status\": \"training_complete\", \"steps\": \"4159/4159\"}, \"notes\": \"SUPERSEDED by D055. alpha=16, replaced by exp_001_sft_3B_d100_s42_a32 (alpha=32).\", \"status\": \"DONE\", \"updated_at\": \"2026-05-15T16:28:05.700Z\"}, \"exp_001_sft_3B_d000_v2\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-14T16:14:42.434Z\", \"hypothesis\": \"3B d000 v2 retrain with reduced LoRA hyperparams (lr=5e-5, alpha=16) to fix CoT catastrophic forgetting. D020 decision. Target: GSM8K >= 50% (raw 60.5%).\", \"metrics\": {\"checkpoint_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_v2_s42/lora_adapter\", \"completed_at\": \"2026-05-15T03:45Z\", \"status\": \"training_complete\"}, \"notes\": \"SUPERSEDED by D055. d000_v2 alpha=16, original d000 already alpha=32. Use original d000 checkpoints for all downstream analysis.\", \"status\": \"DONE\", \"updated_at\": \"2026-05-15T16:10:11.917Z\"}, \"exp_002_signals_3B\": {\"conclusion\": \"failed\", \"created_at\": \"2026-05-15T14:46:52.925Z\", \"status\": \"DONE\", \"updated_at\": \"2026-05-15T16:06:31.114Z\"}, \"exp_001_eval_3B_d000_s42_para_aligned\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-15T14:51:20.059Z\", \"metrics\": {\"arc_challenge\": {\"accuracy\": 0.8235, \"correct\": 574, \"total\": 697}, \"gsm8k\": {\"accuracy\": 0.0482, \"correct\": 11, \"total\": 228}, \"humaneval\": {\"correct\": 3, \"pass@1\": 0.1154, \"total\": 26}, \"mmlu\": {\"accuracy\": 0.6474, \"correct\": 4270, \"total\": 6596}}, \"status\": \"DONE\", \"updated_at\": \"2026-05-15T15:31:43.607Z\"}, \"exp_001_eval_3B_d100_s42_para_aligned\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-15T14:51:17.570Z\", \"metrics\": {\"arc_challenge\": {\"accuracy\": 0.8092, \"correct\": 564, \"total\": 697}, \"gsm8k\": {\"accuracy\": 0.5833, \"correct\": 133, \"total\": 228}, \"humaneval\": {\"correct\": 3, \"pass@1\": 0.1154, \"total\": 26}, \"mmlu\": {\"accuracy\": 0.659, \"correct\": 4347, \"total\": 6596}}, \"status\": \"DONE\", \"updated_at\": \"2026-05-15T15:31:42.432Z\"}, \"exp_001_sft_3B_d005_s123\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-15T11:58:15.842Z\", \"metrics\": {\"final_loss\": 1.1349, \"final_token_accuracy\": 0.7069, \"total_steps\": 3177}, \"status\": \"DONE\", \"updated_at\": \"2026-05-15T15:08:45.951Z\"}, \"exp_001_sft_3B_d025_s123\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-15T11:58:17.463Z\", \"metrics\": {\"final_loss\": 1.1401, \"final_token_accuracy\": 0.734, \"total_steps\": 3384}, \"status\": \"DONE\", \"updated_at\": \"2026-05-15T14:48:17.888Z\"}, \"exp_001_eval_3B_d000_s123_aligned\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-15T11:12:12.687Z\", \"metrics\": {\"arc_challenge\": 0.8328, \"gsm8k\": 0.1812, \"humaneval\": 0.0854, \"mmlu\": 0.6332}, \"notes\": \"Cron false positive: process exited normally after completing all 4 benchmarks (mmlu, gsm8k, arc_challenge, humaneval). Sentinel .done written. Cron missed sentinel because eval experiments don't log to W&B. humaneval pass@1=0.0854. Full metrics in eval_results.json.\", \"status\": \"DONE\", \"updated_at\": \"2026-05-15T14:36:58.735Z\"}, \"exp_001_eval_3B_d005_s42_aligned\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-15T11:12:13.700Z\", \"metrics\": {\"arc_challenge\": 0.8294, \"gsm8k\": 0.2077, \"humaneval\": 0.1463, \"mmlu\": 0.6345}, \"status\": \"DONE\", \"updated_at\": \"2026-05-15T14:34:00.000Z\"}, \"exp_008_base_pretrained_eval_v2\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-15T11:31:00.000Z\", \"hypothesis\": \"Qwen2.5-0.5B base pretrained eval v2 (v1 PID 530893 stopped/dead). No SFT adapter. 3-regime comparison baseline.\", \"metrics\": {\"arc_challenge\": 0.2278, \"gsm8k\": 0.163, \"humaneval\": 0, \"mmlu\": 0.2294}, \"notes\": \"D046+D047: base pretrained MC data 退化(99.5% predict A). GSM8K/HumanEval 保留, MMLU/ARC 仅 position bias 佐证. 禁止 IRT/signals. Regime 轴已删除 base pretrained. 禁止 kill PID 553256.\", \"status\": \"DONE\", \"updated_at\": \"2026-05-15T14:21:16.035Z\"}, \"exp_001_sft_15B_d025_s123_v2\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-15T11:06:19.215Z\", \"metrics\": {\"mean_token_accuracy\": 0.7466, \"train_loss\": 1.2723}, \"status\": \"DONE\", \"updated_at\": \"2026-05-15T13:37:26.605Z\"}, \"exp_001_sft_15B_d005_s123_v2\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-15T11:06:20.414Z\", \"metrics\": {\"mean_token_accuracy\": 0.6855, \"train_loss\": 1.2639}, \"status\": \"DONE\", \"updated_at\": \"2026-05-15T13:37:25.937Z\"}, \"exp_008_base_pretrained_15B_eval_v2\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-15T11:58:04.766Z\", \"metrics\": {\"arc_challenge\": 0.2304, \"arc_correct\": 270, \"arc_total\": 1172, \"gsm8k\": 0.0053, \"gsm8k_correct\": 7, \"gsm8k_total\": 1319, \"humaneval_correct\": 38, \"humaneval_pass1\": 0.2317, \"humaneval_total\": 164, \"mmlu\": 0.2303, \"mmlu_correct\": 3234, \"mmlu_total\": 14042}, \"notes\": \"D046+D047: base pretrained MC data 退化(99.5% predict A, MMLU=0.2303 GSM8K=0.005). GSM8K/HumanEval 保留, MMLU/ARC 仅 position bias 佐证. 禁止 IRT/signals. Regime 轴已删除 base pretrained.\", \"status\": \"DONE\", \"updated_at\": \"2026-05-15T11:58:28.785Z\"}, \"exp_008_base_pretrained_15B_eval\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-15T08:33:08.901Z\", \"metrics\": {\"arc_challenge_accuracy\": 0.2304, \"arc_correct\": 270, \"arc_total\": 1172, \"gsm8k_accuracy\": 0.0053, \"gsm8k_correct\": 7, \"gsm8k_total\": 1319, \"humaneval_correct\": 38, \"humaneval_pass@1\": 0.2317, \"humaneval_total\": 164, \"mmlu_accuracy\": 0.2303, \"mmlu_correct\": 3234, \"mmlu_total\": 14042}, \"notes\": \"D046+D047: base pretrained MC data 退化(99.5% predict A, MMLU=0.2303 GSM8K=0.005). GSM8K/HumanEval 保留, MMLU/ARC 仅 position bias 佐证. 禁止 IRT/signals. Regime 轴已删除 base pretrained.\", \"status\": \"DONE\", \"updated_at\": \"2026-05-15T11:56:40.764Z\"}, \"exp_008_base_pretrained_eval\": {\"conclusion\": \"failed\", \"created_at\": \"2026-05-15T07:45:10.801Z\", \"hypothesis\": \"Qwen2.5-0.5B base pretrained eval (no SFT). 4 signals + 4 benchmark scores. Serves: (1) exp008 regime comparison (2) format incomprehension evidence for Discussion (base vs d000).\", \"status\": \"DONE\", \"updated_at\": \"2026-05-15T11:30:00.000Z\"}, \"exp_001_eval_15B_d000_s123_aligned\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-15T07:39:40.772Z\", \"metrics\": {\"arc_challenge_accuracy\": 0.7577, \"gsm8k_accuracy\": 0.6535, \"humaneval_pass@1\": 0.1707, \"mmlu_accuracy\": 0.5855}, \"status\": \"DONE\", \"updated_at\": \"2026-05-15T10:47:20.609Z\"}, \"exp_001_eval_15B_d100_s123_aligned\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-15T00:35:28.662Z\", \"hypothesis\": \"1.5B 100% dosage s123 eval (aligned MC). Expands multi-seed N for pooled IRT. Paired with d000_s123 for within-seed contamination effect.\", \"metrics\": {\"arc_challenge_accuracy\": 0.7816, \"gsm8k_accuracy\": 0.6444, \"humaneval_pass@1\": 0.2805, \"mmlu_accuracy\": 0.5956}, \"parent\": \"exp_001_sft_15B_d100_s123\", \"status\": \"DONE\", \"updated_at\": \"2026-05-15T10:40:23.512Z\"}, \"exp_001_eval_05B_d000_s123_aligned\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-15T07:39:42.637Z\", \"metrics\": {\"arc_challenge\": 0.4974, \"gsm8k\": 0.3412, \"humaneval\": 0.1037, \"mmlu\": 0.4216}, \"status\": \"DONE\", \"updated_at\": \"2026-05-15T10:27:44.815Z\"}, \"exp_001_eval_3B_d000_s42_v3\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-14T00:48:57.772Z\", \"hypothesis\": \"3B s42 baseline eval v3 (v2 被 SIGKILL). 等 GPU 空出后用绝对路径重新提交。\", \"metrics\": {\"arc_challenge\": 0.8276, \"gsm8k\": 0.1198, \"humaneval\": 0.1159, \"mmlu\": 0.634}, \"notes\": \"GSM8K=11.98% D018 LoRA超参损伤，已排除出IRT\", \"status\": \"DONE\", \"updated_at\": \"2026-05-15T10:00:00.000Z\"}, \"exp006-s1only-gsm8k-2pl\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-15T03:42:59.873Z\", \"hypothesis\": \"GSM8K S1-only 2PL+γ ablation. After joint_fit.py 2PL bug fix (D041), reran with correct --model-type 2pl_gamma. Tests if removing guessing parameter makes S1 signal significant.\", \"metrics\": {\"ci_excludes_zero\": false, \"divergent_count\": 0, \"gamma_ci95\": [-0.306, 0.591], \"gamma_mean\": 0.1389, \"gamma_sd\": 0.2274, \"max_rhat\": 1.0024, \"min_ess\": 3604.4, \"obs_mean_acc\": 0.5086, \"ppp\": 0.2835, \"pred_mean_acc\": 0.5011, \"residual_mae\": 0.0083}, \"status\": \"DONE\", \"updated_at\": \"2026-05-15T09:55:00.000Z\"}, \"exp_001_eval_3B_d000_v2_s123_aligned\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-15T03:22:24.824Z\", \"metrics\": {\"arc_challenge\": 0.8259, \"gsm8k\": 0.2676, \"humaneval\": 0.061, \"mmlu\": 0.6314}, \"status\": \"DONE\", \"updated_at\": \"2026-05-15T09:22:00.000Z\"}, \"exp_001_eval_3B_d025_v2_aligned\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-15T04:14:43.742Z\", \"metrics\": {\"arc_challenge\": 0.8276, \"gsm8k\": 0.6793, \"humaneval\": 0.0976, \"mmlu\": 0.5998}, \"status\": \"DONE\", \"updated_at\": \"2026-05-15T09:22:00.000Z\"}, \"exp_001_eval_3B_d100_v2_s123_aligned\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-15T05:19:30.496Z\", \"metrics\": {\"arc_challenge\": 0.8311, \"gsm8k\": 0.7324, \"humaneval\": 0.1829, \"mmlu\": 0.6319}, \"status\": \"DONE\", \"updated_at\": \"2026-05-15T09:22:00.000Z\"}, \"exp_001_sft_15B_d005_s123\": {\"conclusion\": \"failed\", \"created_at\": \"2026-05-15T07:45:06.224Z\", \"status\": \"DONE\", \"updated_at\": \"2026-05-15T08:37:00.407Z\"}, \"exp_001_eval_05B_d025_s123_aligned\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-15T07:33:04.298Z\", \"metrics\": {\"arc_challenge\": {\"accuracy\": 0.4061, \"correct\": 476, \"total\": 1172}, \"gsm8k\": {\"accuracy\": 0.3533, \"correct\": 466, \"total\": 1319}, \"humaneval\": {\"correct\": 14, \"pass@1\": 0.0854, \"total\": 164}, \"mmlu\": {\"accuracy\": 0.3473, \"correct\": 4877, \"total\": 14042}}, \"status\": \"DONE\", \"updated_at\": \"2026-05-15T08:34:55.834Z\"}, \"exp_001_sft_05B_d025_s123_v2\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-15T03:59:29.007Z\", \"hypothesis\": \"0.5B d025 seed=123 SFT v2 (resubmit after v1 killed on cuda:4 collision). For seed=123 multi-seed IRT pooling. Standard 0.5B params: lr=2e-4, alpha=32, r=16.\", \"metrics\": {\"accuracy\": 0.697, \"epoch\": 1, \"global_steps\": 3384, \"runtime_seconds\": 5930, \"train_loss\": 1.548}, \"status\": \"DONE\", \"updated_at\": \"2026-05-15T06:30:50.892Z\"}, \"exp_001_eval_05B_d000_s42_v7\": {\"conclusion\": \"failed\", \"created_at\": \"2026-05-15T03:34:42.526Z\", \"status\": \"DONE\", \"updated_at\": \"2026-05-15T06:10:55.651Z\"}, \"exp_004_sim_sweep_v5\": {\"conclusion\": \"failed\", \"created_at\": \"2026-05-15T03:39:41.819Z\", \"hypothesis\": \"4PL+γ IRT parameter recovery sweep v5: continuation of v4 (which was erroneously marked failed). Same process PID 652931, TMPDIR=/home/ubuntu/tmp_cmdstan. Progress: 98/120 seeds processed (68 OK). auc0.65 conditions systematically failing.\", \"metrics\": {\"conditions_all_failed\": [\"auc0.65_n20 (0/10)\", \"auc0.65_n50 (0/7)\"], \"conditions_complete\": 4, \"conditions_fully_ok\": [\"auc0.55_n20 (10/10)\", \"auc0.55_n50 (10/10)\", \"auc0.8_n20 (10/10)\", \"auc0.8_n50 (10/10)\"], \"conditions_missing\": 3, \"conditions_never_started\": [\"auc0.65_n100\", \"auc0.9_n50\", \"auc0.9_n100\"], \"conditions_partial\": 5, \"conditions_partial_ok\": [\"auc0.55_n100 (7/10)\", \"auc0.8_n100 (6/10)\", \"auc0.9_n20 (6/10)\"], \"failure_cause\": \"Disk quota exceeded ([Errno 122]) - root partition /tmp filled by CmdStan temp files\", \"seeds_attempted\": 97, \"seeds_ok\": 59, \"seeds_total\": 120}, \"status\": \"DONE\", \"updated_at\": \"2026-05-15T05:33:31.938Z\"}, \"exp006-oracle-arc-4pl-pooled\": {\"conclusion\": \"failed\", \"created_at\": \"2026-05-15T03:51:29.732Z\", \"hypothesis\": \"ARC oracle 4PL+γ pooled IRT with same config as GSM8K oracle (all available models + oracle exposure). Previous ARC 'oracle' used 0.5B-only + delta exposure — not comparable to GSM8K oracle (16 models + oracle). Completes the 2×2×2 matrix (benchmark × model × signal).\", \"status\": \"DONE\", \"updated_at\": \"2026-05-15T05:23:24.270Z\"}, \"exp_008_instruct_05B_eval\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-15T03:25:20.315Z\", \"metrics\": {\"arc_challenge_accuracy\": 0.2816, \"gsm8k_accuracy\": 0.3882, \"humaneval_pass@1\": 0, \"mmlu_accuracy\": 0.2462}, \"status\": \"DONE\", \"updated_at\": \"2026-05-15T05:19:54.360Z\"}, \"exp_001_eval_3B_d100_v2_aligned_v2\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-15T01:00:37.845Z\", \"metrics\": {\"arc_challenge_accuracy\": 0.8242, \"gsm8k_accuracy\": 0.7415, \"humaneval_pass@1\": 0.1707, \"mmlu_accuracy\": 0.632}, \"status\": \"DONE\", \"updated_at\": \"2026-05-15T05:19:51.816Z\"}, \"exp_001_eval_3B_d025_v2_para_aligned\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-15T04:14:47.629Z\", \"hypothesis\": \"3B d025 v2 para_aligned eval. Paraphrased benchmarks for contamination signal computation.\", \"metrics\": {\"arc_challenge_para_accuracy\": 0.8106, \"gsm8k_para_accuracy\": 0.5482, \"humaneval_para_pass@1\": 0.1154, \"mmlu_para_accuracy\": 0.621}, \"parent\": \"exp_001_sft_d025_3B_v2\", \"status\": \"DONE\", \"updated_at\": \"2026-05-15T05:19:49.188Z\"}, \"exp_001_sft_3B_d100_s123\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-15T00:13:45.159Z\", \"metrics\": {\"epochs\": 1, \"mean_token_accuracy\": 0.7343, \"runtime_seconds\": 18252, \"steps\": 4159, \"train_loss\": 1.1846}, \"status\": \"DONE\", \"updated_at\": \"2026-05-15T05:18:48.164Z\"}, \"exp006-oracle-arc-2pl\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-15T03:42:55.893Z\", \"hypothesis\": \"ARC 2PL+γ vs 4PL+γ comparison. ARC 4PL+γ showed γ=-1.46. If 2PL+γ yields better calibration (like GSM8K), supports 'model complexity must match data structure' claim. If 4PL better on ARC, bidirectional evidence for benchmark-dependent model selection.\", \"metrics\": {\"C95_coverage\": 0.1818, \"ESS\": 1512, \"MAE\": 0.0759, \"gamma\": -0.618, \"gamma_ci\": [-1.04, -0.2], \"rhat\": 1.006}, \"status\": \"DONE\", \"updated_at\": \"2026-05-15T04:56:42.392Z\"}, \"exp_001_eval_3B_d000_v2_s123_para_aligned\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-15T03:22:30.855Z\", \"metrics\": {\"arc_challenge_para_accuracy\": 0.8121, \"gsm8k_para_accuracy\": 0.1491, \"humaneval_para_pass@1\": 0.0385, \"mmlu_para_accuracy\": 0.6512}, \"status\": \"DONE\", \"updated_at\": \"2026-05-15T04:56:34.161Z\"}, \"exp006-pooled-s1only-gsm8k-v2\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-15T01:22:13.409Z\", \"metrics\": {\"diagnostics_ok\": false, \"divergent_pct\": 0, \"ess_min\": 330.2, \"fit_time_sec\": 336.9, \"gamma\": 0.1871, \"gamma_ci_excludes_zero\": false, \"gamma_ci_lower\": -0.9172, \"gamma_ci_upper\": 1.3294, \"gamma_sd\": 0.5687, \"n_items\": 1319, \"n_models\": 8, \"note\": \"No evaluation/baselines files generated; only IRT fit available. rhat and ESS did not pass thresholds.\", \"ppp\": 0.336, \"residual_mae\": 0.0367, \"rhat_max\": 1.0148}, \"status\": \"DONE\", \"updated_at\": \"2026-05-15T03:45:48.766Z\"}, \"exp006-pooled-s1only-arc\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-15T00:02:41.698Z\", \"hypothesis\": \"Pooled IRT N=8 with S1-only exposure (D034: RRF non-monotonic, S1 perfectly monotonic 0.5946→0.8998)\", \"metrics\": {\"baselines\": {\"B0_raw_mae\": 0.0588, \"B1_remove_rescore_mae\": 0.0588, \"B2_2pl_gamma_mae\": 0.064, \"B3_vanilla_4pl_mae\": 0.0706, \"B4_linear_regression_mae\": 0.0562, \"B5_emperor_mae\": 0.0588, \"B6_dcr_fuzzy_mae\": 0.2454}, \"brier\": 0.0018, \"coverage_50\": 0, \"coverage_80\": 0.25, \"coverage_95\": 0.625, \"divergent_pct\": 0, \"ece\": 0.0319, \"ess_min\": 769.6, \"fit_time_sec\": 317.7, \"gamma\": -1.4637, \"gamma_ci_excludes_zero\": true, \"gamma_ci_lower\": -2.51, \"gamma_ci_upper\": -0.4051, \"gamma_sd\": 0.5276, \"kendall_tau\": 0.7559, \"mae\": 0.0347, \"n_items\": 1172, \"n_models\": 8, \"ppp\": 0.9677, \"rhat_max\": 1.0098, \"sharpness_95\": 0.0684}, \"status\": \"DONE\", \"updated_at\": \"2026-05-15T03:45:45.246Z\"}, \"exp006-oracle-gsm8k-extended-v2\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-15T01:22:28.344Z\", \"metrics\": {\"baselines\": {\"B0_raw_mae\": 0.005, \"B4_linear_regression_mae\": 0.008, \"B5_emperor_mae\": 0.005, \"B6_dcr_fuzzy_mae\": 0.138}, \"coverage_50\": 0.25, \"coverage_80\": 0.25, \"coverage_95\": 0.31, \"divergent_pct\": 0, \"ece\": 0.0894, \"ess_min\": 1221.9, \"fit_time_sec\": 6240.3, \"gamma\": 3.773, \"gamma_ci_excludes_zero\": true, \"gamma_ci_lower\": 2.741, \"gamma_ci_upper\": 4.714, \"gamma_sd\": 0.504, \"kendall_tau\": 0.505, \"mae\": 0.0917, \"n_items\": 1319, \"n_models\": 16, \"ppp\": 0, \"rhat_max\": 1.002}, \"status\": \"DONE\", \"updated_at\": \"2026-05-15T03:40:28.284Z\"}, \"exp_001_sft_05B_d025_s123\": {\"conclusion\": \"killed\", \"created_at\": \"2026-05-15T03:25:52.119Z\", \"status\": \"DONE\", \"updated_at\": \"2026-05-15T03:37:45.126Z\"}, \"exp_001_eval_05B_d005_s123_para_aligned\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-15T02:40:41.614Z\", \"metrics\": {\"arc_challenge_para_accuracy\": 0.2912, \"gsm8k_para_accuracy\": 0.2939, \"humaneval_para_pass@1\": 0, \"mmlu_para_accuracy\": 0.3166}, \"status\": \"DONE\", \"updated_at\": \"2026-05-15T03:23:40.626Z\"}, \"exp_001_eval_05B_d000_s42\": {\"conclusion\": \"failed\", \"created_at\": \"2026-05-13T22:42:34.313Z\", \"hypothesis\": \"0% dosage 0.5B s42 baseline evaluation on 4 benchmarks to establish ground-truth scores for calibration error computation\", \"notes\": \"失败原因: 所有 4 benchmarks 评估完成（HumanEval pass@1=0.1098），但保存 eval_results.json 时 FileNotFoundError——output_dir 未创建。ARC 下载有 HF 连接超时（未 source network_turbo）但评估仍完成。同命令 s123 实验成功。fix_worker_id: worker_fix_eval_05B_d000_s42_v2_20260514T013245 | 建议: 修复 evaluate.py 中保存前的 os.makedirs 调用后重跑\", \"status\": \"DONE\", \"updated_at\": \"2026-05-15T03:21:30.012Z\"}, \"exp_001_eval_05B_d005_s123_aligned\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-15T00:50:01.658Z\", \"metrics\": {\"arc_challenge_accuracy\": 0.2978, \"gsm8k_accuracy\": 0.3677, \"humaneval_pass@1\": 0.0976, \"mmlu_accuracy\": 0.3002}, \"status\": \"DONE\", \"updated_at\": \"2026-05-15T03:19:25.724Z\"}, \"exp_004_sim_sweep_v4\": {\"conclusion\": \"failed\", \"created_at\": \"2026-05-15T00:28:42.574Z\", \"hypothesis\": \"4PL+γ IRT parameter recovery sweep v4: resume of v3 (crashed due to /tmp tmpfs full from cmdstanpy MCMC temp files). Fixed: TMPDIR=/home/ubuntu/tmp_cmdstan, --resume mode strips failed seeds and re-runs them. 57/120 done, 63 remaining across 8 conditions.\", \"status\": \"DONE\", \"updated_at\": \"2026-05-15T02:54:16.891Z\"}, \"exp_001_sft_3B_d000_s123\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-14T20:22:51.681Z\", \"hypothesis\": \"3B d000 seed=123 SFT for D025/D026 multi-seed strategy. D020 params: lr=5e-5, alpha=16, r=16. Output dir: Qwen2.5-3B_d000_v2_s123.\", \"metrics\": {\"baseline_seed42_train_loss\": 1.1357, \"entropy\": 1.1108, \"epochs\": 1, \"mean_token_accuracy\": 0.748, \"steps\": 3125, \"train_loss\": 1.1361, \"train_runtime_seconds\": 13141.8}, \"status\": \"DONE\", \"updated_at\": \"2026-05-15T02:47:38.140Z\"}, \"exp_001_eval_3B_d000_v2_para_aligned_v3\": {\"conclusion\": \"failed\", \"created_at\": \"2026-05-15T01:14:58.376Z\", \"status\": \"DONE\", \"updated_at\": \"2026-05-15T01:23:18.115Z\"}, \"exp_001_eval_3B_d000_v2_para_aligned_v2\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-15T00:25:20.929Z\", \"metrics\": {\"arc_challenge_para_accuracy\": 0.8121, \"gsm8k_para_accuracy\": 0.2895, \"humaneval_para_pass@1\": 0.0385, \"mmlu_para_accuracy\": 0.6468}, \"status\": \"DONE\", \"updated_at\": \"2026-05-15T01:16:33.841Z\"}, \"exp006-oracle-gsm8k-extended\": {\"conclusion\": \"failed\", \"created_at\": \"2026-05-15T00:04:04.647Z\", \"status\": \"DONE\", \"updated_at\": \"2026-05-15T01:04:15.114Z\"}, \"exp006-pooled-s1only-gsm8k\": {\"conclusion\": \"failed\", \"created_at\": \"2026-05-15T00:02:44.254Z\", \"hypothesis\": \"Pooled IRT N=8 with S1-only exposure (D034: RRF non-monotonic, S1 perfectly monotonic 0.5946→0.8998)\", \"status\": \"DONE\", \"updated_at\": \"2026-05-15T01:04:06.647Z\"}, \"exp_001_eval_3B_d100_v2_para_aligned\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-15T00:06:11.858Z\", \"metrics\": {\"arc_challenge_para\": 0.8092, \"gsm8k_para\": 0.5833, \"humaneval_para_pass1\": 0.1154, \"mmlu_para\": 0.659}, \"status\": \"DONE\", \"updated_at\": \"2026-05-15T00:50:03.989Z\"}, \"exp_001_sft_05B_d005_s123\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-14T23:45:12.529Z\", \"hypothesis\": \"0.5B d005 seed=123 SFT for N=16 multi-seed IRT pooling. Standard 0.5B params: lr=2e-4, alpha=32, r=16.\", \"metrics\": {\"epoch\": 1, \"final_loss\": 1.4542, \"final_token_accuracy\": 0.6794, \"mean_token_accuracy\": 0.6356, \"total_steps\": 3177, \"train_loss\": 1.5422, \"train_runtime_sec\": 3458.58}, \"status\": \"DONE\", \"updated_at\": \"2026-05-15T00:46:31.713Z\"}, \"exp_001_eval_3B_d000_v2_aligned\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-14T21:01:48.742Z\", \"hypothesis\": \"3B d000 v2 aligned eval (D020 fix: lr=5e-5, alpha=16). Verify GSM8K recovery from CoT catastrophic forgetting. Target: GSM8K >= 50% (raw 60.5%, v1 was 11.7%).\", \"metrics\": {\"arc_challenge\": 0.8183, \"gsm8k\": 0.3525, \"humaneval_pass@1\": 0.0976, \"mmlu\": 0.6295}, \"notes\": \"PARTIAL SUCCESS (Reviewer WARNING): GSM8K=35.25% 未达 50% 目标（raw 60.5%→35.25%，损失 25pp）。MMLU(62.95%)/ARC(81.83%) 恢复正常，但 CoT 能力退化显著。D020 params (lr=5e-5, alpha=16) 改善了 v1(11.7%) 但不够。\", \"parent\": \"exp_001_sft_3B_d000_v2\", \"status\": \"DONE\", \"updated_at\": \"2026-05-15T00:42:06.698Z\"}, \"exp_001_sft_15B_d100_s123\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-14T20:21:10.691Z\", \"metrics\": {\"baseline_seed42_token_accuracy\": 0.7033, \"baseline_seed42_train_loss\": 1.2996, \"entropy\": 1.3327, \"epochs\": 1, \"mean_token_accuracy\": 0.7178, \"num_tokens\": 21575068, \"steps\": 4159, \"train_loss\": 1.3002, \"train_runtime_seconds\": 14663.6}, \"status\": \"DONE\", \"updated_at\": \"2026-05-15T00:32:28.784Z\"}, \"exp_004_sim_sweep_v3\": {\"conclusion\": \"failed\", \"created_at\": \"2026-05-14T21:55:41.270Z\", \"hypothesis\": \"4PL+γ IRT parameter recovery sweep v3: continuing v2 process (PID 599562, parallel=2, chains_parallel=2). 54/120 done, 66 remaining. Killed conflicting v1 serial process.\", \"notes\": \"v2 PID 599562 was still alive (erroneously marked failed). v1 serial PID 559606 was also running on same results dir — killed to prevent write conflicts. v3 = same process as v2, just corrected registry. 2 CPU / 7.6GB RAM machine, parallel=2 chains_parallel=2. ETA ~20-30h for remaining 66 runs.\", \"status\": \"DONE\", \"updated_at\": \"2026-05-15T00:13:02.038Z\"}, \"exp_001_eval_3B_d100_v2_aligned\": {\"conclusion\": \"failed\", \"created_at\": \"2026-05-14T23:34:11.632Z\", \"metrics\": {\"INVALID\": \"metrics were from v1 exp_001_eval_3B_d100_aligned, not v2. v2 output dir was empty. PID 461879 died before completion.\"}, \"notes\": \"DATA INTEGRITY ISSUE (D036): Metrics erroneously copied from v1 (exp_001_eval_3B_d100_aligned). Worker found v1 results at similar path, mistook for v2. v2 output dir was empty (eval still running), then deleted during cleanup. PID 461879 killed/died. Must re-run as v3.\", \"status\": \"DONE\", \"updated_at\": \"2026-05-15T00:08:21.000Z\"}, \"exp_001_sft_d025_3B\": {\"conclusion\": \"failed\", \"created_at\": \"2026-05-14T23:34:12.515Z\", \"notes\": \"GPU 3 空转: 注册 RUNNING 但进程从未启动 (nvidia-smi 确认 0% util, 0 MiB). Director 指令标 FAILED.\", \"status\": \"DONE\", \"updated_at\": \"2026-05-14T23:51:23.923Z\"}, \"exp_001_eval_05B_d100_s123_aligned\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-14T21:31:14.591Z\", \"hypothesis\": \"0.5B d100 s123 aligned eval — multi-seed dosage-100 eval for IRT calibration.\", \"metrics\": {\"arc_challenge_accuracy\": 0.3669, \"arc_challenge_correct\": 430, \"arc_challenge_total\": 1172, \"gsm8k_accuracy\": 0.3798, \"gsm8k_correct\": 501, \"gsm8k_total\": 1319, \"humaneval_pass_at_1\": 0.1037, \"humaneval_total\": 164, \"mmlu_accuracy\": 0.3058, \"mmlu_correct\": 4294, \"mmlu_total\": 14042}, \"parent\": \"exp_001_sft_05B_d100_s123\", \"status\": \"DONE\", \"updated_at\": \"2026-05-14T23:48:24.746Z\"}, \"exp_001_eval_3B_d000_v2_para_aligned\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-14T22:21:18.136Z\", \"hypothesis\": \"3B d000 v2 para_aligned eval: paraphrased benchmarks (mmlu/gsm8k/arc/humaneval) on D020-retrained 3B d000 v2 checkpoint. Paired with aligned eval (GPU 4) for contamination signal computation.\", \"metrics\": {\"format\": \"paraphrased_aligned\", \"mmlu_para\": 0.6468}, \"notes\": \"GPU 0, PID 450055. tmux session: eval_3B_d000_v2_para. Log: /tmp/eval_3B_d000_v2_para_aligned.log. bitsandbytes warning (libnvJitLink.so.13 missing) is non-fatal.\", \"status\": \"DONE\", \"updated_at\": \"2026-05-14T23:39:15.404Z\"}, \"exp006-pooled-05B-15B-mmlu-v2\": {\"conclusion\": \"failed\", \"created_at\": \"2026-05-14T22:59:50.928Z\", \"metrics\": {\"NOTE\": \"fit completely failed, not reportable\", \"convergence\": \"FAILED (rhat=1.54, ess=7)\", \"coverage_95\": 1, \"exposure_source\": \"signal_rrf\", \"gamma_joint\": -0.2095, \"gamma_joint_ci\": [-1.01, 0.59], \"gamma_perbench\": -3.8073, \"gamma_perbench_ci\": [-7.02, 3.22], \"mae\": 0.099, \"n_models\": 8, \"ppp\": 0.75}, \"status\": \"DONE\", \"updated_at\": \"2026-05-14T23:08:55.525Z\"}, \"exp006-pooled-05B-15B-arc-v2\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-14T22:59:49.440Z\", \"metrics\": {\"NOTE\": \"coverage below 95%; no oracle baseline exists\", \"convergence\": \"OK\", \"coverage_95\": 0.625, \"exposure_source\": \"signal_rrf\", \"gamma_joint\": -1.4637, \"gamma_joint_ci\": [-2.51, -0.41], \"gamma_perbench\": -2.3471, \"gamma_perbench_ci\": [-3.46, -1.19], \"mae\": 0.035, \"n_models\": 8, \"ppp\": 0.999}, \"status\": \"DONE\", \"updated_at\": \"2026-05-14T23:08:51.536Z\"}, \"exp_005_noise_prop\": {\"conclusion\": \"failed\", \"created_at\": \"2026-05-13T18:31:00.000Z\", \"hypothesis\": \"Measurement error in exposure scores propagates through 4PL+γ IRT to widen calibrated score CIs; analytical ME model (conjugate normal integration) produces equivalent CI widths to full latent-τ model at fraction of compute\", \"notes\": \"v1 original run, failed due to /tmp disk exhaustion. Superseded by v2→v3→v4. See v4 for active tracking (PID 559667, 23/25 fits).\", \"status\": \"DONE\", \"updated_at\": \"2026-05-14T22:13:18.833Z\"}, \"exp_004_sim_sweep\": {\"conclusion\": \"failed\", \"created_at\": \"2026-05-13T16:43:57.478Z\", \"hypothesis\": \"4PL+γ IRT parameter recovery degrades gracefully with exposure signal quality (AUC); there exists a minimum AUC threshold below which γ 95% CI width exceeds 15pp; recovery improves with N_models; prior sensitivity is bounded\", \"notes\": \"v1 original serial run. Superseded by v2 (parallel=2). PID 559606 killed to prevent write conflicts with v2. See v3 for active tracking.\", \"status\": \"DONE\", \"updated_at\": \"2026-05-14T22:13:15.704Z\"}, \"exp002-signals-1p5B\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-14T19:50:56.771Z\", \"notes\": \"1.5B signals 12/12 complete (d000/d005/d025/d100 × s1_embedding/s2_minkpp/s4_selfcritique). All PASS. GPU 0 released.\", \"status\": \"DONE\", \"updated_at\": \"2026-05-14T22:11:46.914Z\"}, \"exp_004_sim_sweep_v2\": {\"conclusion\": \"failed\", \"created_at\": \"2026-05-14T07:12:12.267Z\", \"metrics\": {\"auc080_n100_bias\": 0.008, \"auc080_n100_ci_width\": 0.116, \"auc080_n100_gamma_hat\": 0.508, \"auc080_n100_theta_corr\": 0.962, \"auc080_n50_bias\": 0.006, \"auc080_n50_ci95_coverage\": 1, \"auc080_n50_rmse\": 0.03, \"ci_width_ratio_n100\": 1.81, \"core_findings_stable\": true, \"runs_completed\": 48, \"runs_total\": 120}, \"notes\": \"v2 was erroneously marked failed; PID 599562 was still running. Killed conflicting v1 (PID 559606). Continuing as v3 registry entry.\", \"status\": \"DONE\", \"updated_at\": \"2026-05-14T21:55:29.436Z\"}, \"exp_005_noise_prop_v3\": {\"conclusion\": \"failed\", \"created_at\": \"2026-05-14T03:24:06.949Z\", \"hypothesis\": \"Noise propagation: ME-aware 4PL+γ IRT produces wider calibrated-score CIs than simple model as σ_e increases, demonstrating proper uncertainty propagation. v3 fixes: local disk Stan output, analytic ME (1231 params), checkpoint resume.\", \"notes\": \"PID 559666 crashed (~10h ago). 22/25 fits completed. Restarting as v4.\", \"status\": \"DONE\", \"updated_at\": \"2026-05-14T21:50:34.523Z\"}, \"exp_001_sft_05B_d100_s123\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-14T20:17:25.569Z\", \"status\": \"DONE\", \"updated_at\": \"2026-05-14T21:30:33.304Z\"}, \"exp002-signal-d025-05B\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-14T18:29:51.827Z\", \"notes\": \"0.5B d025 signals 3/3 passed (embedding, minkpp, selfcritique × mmlu, gsm8k, arc_challenge). 13 files total including merged signals.\", \"status\": \"DONE\", \"updated_at\": \"2026-05-14T21:08:54.222Z\"}, \"exp_001_eval_05B_d025_aligned_v2\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-14T16:07:13.381Z\", \"hypothesis\": \"0.5B d025 s42 paraphrase aligned eval v2 — dose-response intermediate point. Original aligned eval already complete, this run covers paraphrase only.\", \"metrics\": {\"arc_challenge\": 0.3199, \"format\": \"paraphrased_aligned\", \"gsm8k\": 0.3114, \"humaneval_pass1\": 0.1923, \"mmlu\": 0.2835}, \"status\": \"DONE\", \"updated_at\": \"2026-05-14T21:08:51.166Z\"}, \"exp_006_irt_05B_arc\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-14T20:17:30.505Z\", \"hypothesis\": \"ARC (1172 items, ~4700 params) per-benchmark NUTS with delta exposure. Second benchmark validation after GSM8K success.\", \"metrics\": {\"fit_type\": \"joint\", \"gamma\": -1.21, \"gamma_ci_lower\": -2.53, \"gamma_ci_upper\": 0.12}, \"status\": \"DONE\", \"updated_at\": \"2026-05-14T21:05:36.632Z\"}, \"exp_001_eval_15B_d025_aligned\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-14T18:24:25.390Z\", \"metrics\": {\"arc_challenge\": 0.7688, \"gsm8k\": 0.6535, \"humaneval_pass1\": 0.2256, \"mmlu\": 0.5902}, \"status\": \"DONE\", \"updated_at\": \"2026-05-14T21:05:10.243Z\"}, \"exp_001_eval_05B_d005_para_aligned\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-14T15:46:02.603Z\", \"metrics\": {\"arc_challenge\": 0.33, \"arc_correct\": 230, \"arc_total\": 697, \"gsm8k\": 0.2588, \"gsm8k_correct\": 59, \"gsm8k_total\": 228, \"humaneval\": 0, \"humaneval_correct\": 0, \"humaneval_total\": 26, \"mmlu\": 0.3548, \"mmlu_correct\": 2340, \"mmlu_total\": 6596}, \"status\": \"DONE\", \"updated_at\": \"2026-05-14T20:48:29.901Z\"}, \"exp_001_eval_15B_d025_para_aligned\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-14T19:11:06.187Z\", \"hypothesis\": \"1.5B d025 paraphrase aligned eval: measure contamination-robust performance on paraphrased benchmarks for dosage=25% model\", \"metrics\": {\"arc_challenge\": 0.766, \"gsm8k\": 0.539, \"humaneval\": 0.154, \"mmlu\": 0.618}, \"status\": \"DONE\", \"updated_at\": \"2026-05-14T20:48:26.690Z\"}, \"exp_001_eval_3B_d100_para_aligned\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-14T19:11:52.814Z\", \"hypothesis\": \"3B d100 paraphrase aligned eval: measure contamination-robust performance drop for largest model at full dosage on paraphrased benchmarks\", \"metrics\": {\"arc_challenge\": 0.828, \"gsm8k\": 0.614, \"mmlu\": 0.676}, \"status\": \"DONE\", \"updated_at\": \"2026-05-14T20:48:21.457Z\"}, \"exp_006_pooled_gsm8k_v1\": {\"conclusion\": \"failed\", \"created_at\": \"2026-05-14T20:17:21.376Z\", \"hypothesis\": \"Cross-scale pooled IRT (0.5B+1.5B+3B, N≈10 models) on GSM8K with delta exposure. Test if pooling increases gamma significance (previous single-scale N=4 had CI including 0).\", \"status\": \"DONE\", \"updated_at\": \"2026-05-14T20:47:40.753Z\"}, \"exp_001_eval_15B_aligned_batch\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-14T08:45:37.976Z\", \"hypothesis\": \"1.5B aligned-format eval batch (D017): d000/d005/d100 × original + paraphrase. Formal analysis results for 1.5B scale dose-response.\", \"metrics\": {\"arc\": {\"d000_orig\": 0.7722, \"d000_para\": 0.7547, \"d005_orig\": 0.7688, \"d005_para\": 0.7532, \"d100_orig\": 0.7688, \"d100_para\": 0.7661}, \"gsm8k\": {\"d000_orig\": 0.6543, \"d000_para\": 0.557, \"d005_orig\": 0.6482, \"d005_para\": 0.5439, \"d100_orig\": 0.6497, \"d100_para\": 0.5526}, \"humaneval\": {\"d000_orig\": 0.128, \"d000_para\": 0.0385, \"d005_orig\": 0.25, \"d005_para\": 0.1923, \"d100_orig\": 0.3049, \"d100_para\": 0.2692}, \"key_finding\": \"MC benchmarks fail to detect contamination at 1.5B scale (<1pp). HumanEval shows strong dose-response (+17.69pp). Paraphrase gap does not cleanly separate contamination.\", \"mmlu\": {\"d000_orig\": 0.5853, \"d000_para\": 0.6096, \"d005_orig\": 0.5852, \"d005_para\": 0.6164, \"d100_orig\": 0.5933, \"d100_para\": 0.6252}}, \"notes\": \"1.5B d000 aligned eval 完成: MMLU=58.53%, GSM8K=65.43%, ARC=77.22%, HumanEval=12.80%。对比 legacy: MMLU +1.0pp, GSM8K +1.75pp, ARC -0.3pp (基本持平)。当前 GPU 1 跑 d000 para_aligned (PID 362352)。之后还有 d005/d100 aligned + paraphrase。\", \"status\": \"DONE\", \"updated_at\": \"2026-05-14T19:52:46.623Z\"}, \"exp_006_irt_05B_gsm8k\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-14T18:04:35.887Z\", \"hypothesis\": \"GSM8K (1319 items, ~5300 params) NUTS feasibility validation. If warmup produces samples within 2h → NUTS viable for small benchmarks. Else → ADVI fallback.\", \"metrics\": {\"baselines_mae\": {\"B0_raw\": 0.0034, \"B2_2pl_gamma\": 0.3202, \"B3_vanilla_4pl\": 0.0123, \"B4_linear_regression\": 0.003, \"B6_dcr_fuzzy\": 0.2634, \"IRT_4pl_gamma\": 0.0195}, \"delta_fix_applied\": true, \"joint_divergences\": 0, \"joint_ess\": 956.4, \"joint_gamma\": 0.3463, \"joint_gamma_ci\": [-0.65, 1.4], \"joint_rhat\": 1.0081, \"perbench_divergences\": 0, \"perbench_ess\": 522.2, \"perbench_gamma\": 0.508, \"perbench_gamma_ci\": [-0.64, 1.84], \"perbench_rhat\": 1.0096, \"signal_scores_after_delta\": [0, 0.016, 0.065, 0.197]}, \"notes\": \"Joint-fit converges (Rhat=1.008, ESS=956, 0 divergences), per-benchmark FAILS (Rhat=1.53, ESS=7). Exposure matrix bug suspected — per-benchmark and joint-fit may use different exposure matrices. DO NOT start ARC per-benchmark until P0 resolved. Code mods verified: max-items=random subsampling (seed-based), ADVI deleted, joint_fit max-items fixed. RRF issue found: S2 minkpp polarity inverted, delta exposure (vs d000 baseline) resolves monotonicity.\", \"parent\": \"exp_006_irt_05B_v1\", \"status\": \"DONE\", \"updated_at\": \"2026-05-14T19:48:01.400Z\"}, \"exp_001_eval_15B_d100_aligned\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-14T19:11:51.112Z\", \"hypothesis\": \"1.5B d100 aligned eval: full contamination dosage performance on original benchmarks (aligned format)\", \"metrics\": {\"arc_challenge_accuracy\": 0.7688, \"gsm8k_accuracy\": 0.6497, \"humaneval_correct\": 50, \"humaneval_pass_rate\": 0.3049, \"humaneval_total\": 164, \"mmlu_accuracy\": 0.5933}, \"status\": \"DONE\", \"updated_at\": \"2026-05-14T19:12:41.550Z\"}, \"exp_001_eval_15B_d005_aligned_v2\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-14T18:30:09.199Z\", \"hypothesis\": \"1.5B d005 aligned eval — low-dose contamination response at 1.5B scale\", \"metrics\": {\"arc_challenge\": 0.7688, \"gsm8k\": 0.6482, \"humaneval_pass_at_1\": 0.25, \"mmlu\": 0.5852}, \"status\": \"DONE\", \"updated_at\": \"2026-05-14T18:45:30.922Z\"}, \"exp_001_sft_d100_3B\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-14T04:24:36.974Z\", \"hypothesis\": \"100% dosage contaminated SFT on Qwen2.5-3B (seed=42): maximum contamination at largest controlled scale\", \"metrics\": {\"epoch\": 1, \"runtime_hours\": 5.2, \"steps\": \"4159/4159\", \"token_accuracy\": 0.7206, \"train_loss\": 1.178}, \"notes\": \"训练成功完成。4159/4159 steps, train_loss=1.178, token_accuracy=0.7206, runtime=5.2h。EXIT_CODE=129 (SIGHUP) 发生在 Training complete 之后，属于 wrapper PID false positive（已知模式）。Checkpoint: /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d100_s42/lora_adapter。GPU 3 已安排 eval_3B_d100 tmux auto-relay。\", \"status\": \"DONE\", \"updated_at\": \"2026-05-14T18:24:10.566Z\"}, \"exp_001_eval_05B_d100_aligned_v4\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-14T15:25:10.827Z\", \"metrics\": {\"arc_challenge\": 0.2944, \"arc_delta_vs_d000\": -0.1749, \"gsm8k\": 0.3654, \"humaneval_delta_vs_d000\": -0.1098, \"humaneval_pass_at_1\": 0, \"mmlu\": 0.2334, \"mmlu_delta_vs_d000\": -0.1645}, \"notes\": \"0.5B d100 aligned: catastrophic degradation, no contamination inflation. MMLU 23.3% (near random, -16.5pp vs d000), ARC 29.4% (-17.5pp), HumanEval 0% (-11pp). Dose-response monotonically decreasing at 0.5B scale. Consistent with unaligned format results. Small model capacity insufficient to memorize without losing generalization. Supports narrative: contamination detection via score inflation fails at small scale → need IRT-based calibration.\", \"status\": \"DONE\", \"updated_at\": \"2026-05-14T18:20:00.391Z\"}, \"exp_001_sft_d025_15B\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-14T14:18:59.162Z\", \"hypothesis\": \"25% dosage contaminated SFT on Qwen2.5-1.5B (seed=42): mid-dosage contamination for 1.5B dose-response curve intermediate point\", \"metrics\": {\"entropy\": 1.2623, \"epochs\": 1, \"mean_token_accuracy\": 0.7192, \"steps\": 3384, \"train_loss\": 1.2715, \"train_runtime_seconds\": 11610.6}, \"notes\": \"Cron false positive: 训练正常完成 3384/3384 steps, epoch=1.0, loss=1.2715, token_acc=0.7192。lora_adapter/ 完整 (adapter_model.safetensors 70.5MB)。Cron 误报因无 sentinel file 和 W&B run。1.5B d025 SFT 就绪，可进行 aligned eval。\", \"status\": \"DONE\", \"updated_at\": \"2026-05-14T18:19:10.939Z\"}, \"exp_001_eval_3B_d005_aligned\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-14T13:10:12.650Z\", \"metrics\": {\"arc_challenge\": 0.829, \"gsm8k\": 0.208, \"humaneval_pass_at_1\": 0.146, \"mmlu\": 0.634}, \"notes\": \"Cron false positive: 进程正常完成退出，但无 sentinel file/W&B run，cron 误判为 failed。实际 4 个 benchmark 全部完成，结果在 output dir。mmlu=0.634, gsm8k=0.208, arc=0.829, humaneval=0.146。\", \"status\": \"DONE\", \"updated_at\": \"2026-05-14T18:15:10.887Z\"}, \"exp_006_irt_05B_v1\": {\"conclusion\": \"failed\", \"created_at\": \"2026-05-14T17:09:23.070Z\", \"notes\": \"D023: 56K params infeasible for NUTS (MMLU 14042 items → 56K params, 6h zero samples). Killed all chains (PIDs 411936-411940) + main (411789) + wrapper (411783). Issues: 1) No --max-items limit 2) Mixed aligned/non-aligned formats 3) Oracle dosage instead of exp-002 signal-derived exposure. Superseded by exp_006_irt_05B_v2 with tiered strategy.\", \"status\": \"DONE\", \"updated_at\": \"2026-05-14T18:02:23.310Z\"}, \"exp_001_eval_05B_d025_aligned\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-14T13:14:42.647Z\", \"hypothesis\": \"0.5B d025 s42 aligned eval — 25% contamination dose-response intermediate point (original + paraphrase)\", \"metrics\": {\"ARC\": 32.51, \"GSM8K\": 36.62, \"HumanEval\": \"missing - process exited before 4th benchmark\", \"MMLU\": 28.03}, \"status\": \"DONE\", \"updated_at\": \"2026-05-14T17:02:04.811Z\"}, \"exp_008_signal_survival_v4\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-14T16:23:34.234Z\", \"hypothesis\": \"Signal Survival Analysis v4 (D021 fix): within-model AUC limited to d005/d025; d000/d100 use cross-model signal comparison; C2 claim weakened to 'systematic degradation'. Uses existing exp-002 signal data, CPU only.\", \"metrics\": {\"S1_d005_auc_mean\": 0.979, \"S1_d100_cross_cohens_d_mean\": 3.6, \"S2_d005_auc_mean\": 0.465, \"S2_d100_cross_cohens_d_mean\": -1.98, \"S4_d005_auc_mean\": 0.481, \"S4_d100_cross_cohens_d_mean\": 0.45, \"d021_fix\": \"within-model AUC only for d005; d100 uses cross-model Cohen's d\", \"effective_signals_at_05B\": 1}, \"status\": \"DONE\", \"updated_at\": \"2026-05-14T16:44:49.686Z\"}, \"exp_001_eval_05B_d100_aligned_v3\": {\"conclusion\": \"failed\", \"created_at\": \"2026-05-14T15:23:30.699Z\", \"hypothesis\": \"0.5B d100 s42 aligned-format eval (v3 fix: conda activation). d100 original + paraphrase MC eval with \\\"The answer is\\\" prefix (D017).\", \"notes\": \"失败原因: SIGHUP (EXIT_CODE=129) — tmux wrapper PID 死亡导致子进程收到 SIGHUP，在 GSM8K eval 13% (178/1319) 处被终止。已知模式(memory.md: wrapper PID vs python PID)。附带问题: 提交命令缺少 HF_DATASETS_OFFLINE=1 导致初始 HF 超时重试。v4 已在 cuda:2 重新提交并运行中。\", \"parent\": \"exp_001_eval_05B_d100_aligned_v2\", \"status\": \"DONE\", \"updated_at\": \"2026-05-14T16:19:43.894Z\"}, \"exp_008_signal_survival\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-14T16:11:14.324Z\", \"hypothesis\": \"Signal Survival Analysis: Do individual contamination signals (Embedding/Min-K++/ConStat/Self-Critique) maintain detection AUC across dosage regimes? 4 signals × 3 regimes × 3 benchmarks AUC heatmap. C2 Core Contribution evidence.\", \"metrics\": {\"S1_d000_arc\": 0.427, \"S1_d000_gsm8k\": 0.5502, \"S1_d000_mmlu\": 0.5049, \"S1_d005_arc\": 0.995, \"S1_d005_gsm8k\": 0.9882, \"S1_d005_mmlu\": 0.953, \"S1_d100_arc\": 0.501, \"S1_d100_gsm8k\": 0.4127, \"S1_d100_mmlu\": 0.4943, \"S2_d005_arc\": 0.4659, \"S2_d005_gsm8k\": 0.4649, \"S2_d005_mmlu\": 0.4655, \"S4_d005_arc\": 0.4325, \"S4_d005_gsm8k\": 0.4947, \"S4_d005_mmlu\": 0.5165, \"signals_surviving\": 0, \"signals_total\": 3}, \"notes\": \"0/3 signals survive across regimes. S1 Embedding: AUC 0.95-0.995 at d005 but random at d000/d100 (ceiling effect at full contamination). S2 Min-K++ and S4 Self-Critique: random across all regimes (0.43-0.57). ConStat (S3) not computed (needs paraphrase data). Result validates C2: individual signals insufficient → need IRT multi-signal fusion.\", \"status\": \"DONE\", \"updated_at\": \"2026-05-14T16:16:31.712Z\"}, \"exp_001_eval_3B_d100_aligned\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-14T11:56:44.974Z\", \"hypothesis\": \"3B d100 s42 aligned eval — 100% contamination at largest scale, upper bound for 3B dose-response (MMLU/ARC only, GSM8K excluded per D018)\", \"metrics\": {\"arc_challenge_accuracy\": 0.8396, \"gsm8k_exact_match\": 0.6967, \"humaneval_pass1\": 0.122, \"mmlu_accuracy\": 0.6417}, \"notes\": \"重跑成功。PID 362942 GPU 3。4 benchmarks 全部完成: MMLU 64.17%, GSM8K 69.67%, ARC 83.96%, HumanEval 12.20%。运行时间约 3h16m (20:06-23:22)。\", \"parent\": \"exp_001_sft_d100_3B\", \"status\": \"DONE\", \"updated_at\": \"2026-05-14T15:33:27.101Z\"}, \"exp_001_eval_05B_d005_aligned\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-14T15:20:22.394Z\", \"metrics\": {\"d005_aligned_arc\": 0.3285, \"d005_aligned_gsm8k\": 0.3624, \"d005_aligned_humaneval\": 0.0793, \"d005_aligned_mmlu\": 0.3255}, \"status\": \"DONE\", \"updated_at\": \"2026-05-14T15:21:22.628Z\"}, \"exp_001_eval_05B_d100_aligned\": {\"conclusion\": \"failed\", \"created_at\": \"2026-05-14T14:50:02.679Z\", \"hypothesis\": \"0.5B d100 s42 aligned eval resubmit — d100 original + paraphrase, split from failed batch to avoid timeout\", \"notes\": \"PID 389866 仍在运行（ps 确认 state=Rl, elapsed=19:31），tmux session 已死但 python 进程存活。Cron 误报 process gone（miss 4/5）因 tmux 检测失效。MMLU 已完成，GSM8K/ARC/HumanEval 进行中。等进程完成后立即提交 d100 paraphrase eval（--output-dir Qwen2.5-0.5B_d100_s42_para_aligned --paraphrase）。GPU 2 仍在使用。\", \"status\": \"DONE\", \"updated_at\": \"2026-05-14T15:19:06.659Z\"}, \"exp_001_eval_05B_aligned_batch\": {\"conclusion\": \"failed\", \"created_at\": \"2026-05-14T08:38:53.976Z\", \"hypothesis\": \"0.5B aligned-format eval batch (D017): d000/d005/d100 × original + paraphrase = 6 eval runs. Formal analysis results replacing legacy mc_format.\", \"metrics\": {\"d000_aligned_arc\": 0.4693, \"d000_aligned_gsm8k\": 0.3692, \"d000_aligned_humaneval\": 0.1098, \"d000_aligned_mmlu\": 0.3979, \"d000_para_aligned_arc\": 0.4792, \"d000_para_aligned_gsm8k\": 0.2807, \"d000_para_aligned_humaneval\": 0.1154, \"d000_para_aligned_mmlu\": 0.4428, \"d005_aligned_arc\": 0.3285, \"d005_aligned_gsm8k\": 0.3624, \"d005_aligned_humaneval\": 0.0793, \"d005_aligned_mmlu\": 0.3255}, \"notes\": \"0.5B aligned batch eval 因 timeout (EXIT_CODE=124) 中断。实际完成 4/6 runs: d000 orig+para, d005 orig+para 结果完整。d100 orig（仅跑48min被kill）+ d100 para（未启动）缺失。Timeline: d000_orig 18:52→d000_para 19:15→d005_orig 21:26→d005_para 21:51→d100_orig killed 22:39。d100 已单独重提交到 GPU 2。d005 指标待补录。d000 metrics: MMLU=39.79%, GSM8K=36.92%, ARC=46.93%, HumanEval=10.98%; d000_para: MMLU=44.28%, GSM8K=28.07%, ARC=47.92%, HumanEval=11.54%.\", \"parent\": \"exp_001_sft_d025_05B_v3\", \"status\": \"DONE\", \"updated_at\": \"2026-05-14T15:15:40.960Z\"}, \"exp_001_eval_05B_d005\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-14T01:17:07.820Z\", \"metrics\": {\"arc_challenge\": 0.2858, \"arc_correct\": 335, \"arc_total\": 1172, \"gsm8k\": 0.3601, \"gsm8k_correct\": 475, \"gsm8k_total\": 1319, \"humaneval_correct\": 13, \"humaneval_pass1\": 0.0793, \"humaneval_total\": 164, \"mmlu\": 0.2929, \"mmlu_correct\": 4113, \"mmlu_total\": 14042}, \"notes\": \"⚠️ legacy mc_format — 仅供诊断参考，正式分析需用 aligned 格式重跑 (D017 延伸决策)。\", \"status\": \"DONE\", \"updated_at\": \"2026-05-14T15:10:32.421Z\"}, \"exp_006_irt_05B\": {\"conclusion\": \"killed\", \"created_at\": \"2026-05-14T14:20:20.389Z\", \"notes\": \"KILLED by Director 指令: 混合 scale (0.5B+1.5B+3B) + legacy 格式 + 多余 seed 的错误数据在拟合。Stan NUTS 4 chains (PID 386298-386301) 运行 ~30min 后终止。代码修复中: 正则改为 _d(\\\\d+)_s(\\\\d+)(_para)?(_aligned)?$, 增加 --model-scale 和 --seed 过滤参数。等 d025/d100 aligned eval 完成后再用修复后代码重跑。\", \"status\": \"DONE\", \"updated_at\": \"2026-05-14T14:53:16.180Z\"}, \"exp_003_rrf_05B\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-14T14:17:36.003Z\", \"status\": \"DONE\", \"updated_at\": \"2026-05-14T14:18:05.370Z\"}, \"exp_002_signals_05B\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-14T08:45:35.964Z\", \"hypothesis\": \"0.5B contamination signal computation (S1 Embedding/S2 Min-K++/S4 Self-Critique) on d000/d005/d100 × mmlu/gsm8k/arc = 27 signal tasks. Critical path for exp-003 RRF → exp-006 IRT.\", \"notes\": \"v5 完成 9/9 PASS。d000/d005/d100 × mmlu/gsm8k/arc_challenge 全部完成。9 个 signals_merged 文件已产出。三项修复奏效: timeout 4h, per-signal cache, max_tokens 64。GPU 0 已释放。\", \"status\": \"DONE\", \"updated_at\": \"2026-05-14T14:04:12.884Z\"}, \"exp_001_eval_3B_d000_aligned\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-14T09:30:50.047Z\", \"hypothesis\": \"3B d000 s42 aligned eval (v5 代码) — 诊断 GSM8K 崩塌 (0.117→?) 并建立正式 aligned baseline。含 GSM8K 答案提取修复（如需要）。\", \"metrics\": {\"arc_challenge_accuracy\": 0.8276, \"gsm8k_exact_match\": 0.1198, \"humaneval_pass_at_1\": 0.1159, \"mmlu_accuracy\": 0.634}, \"notes\": \"D018 决策：3B GSM8K 标记为 \\\"SFT-degraded, excluded from dose-response\\\"。3B MMLU/ARC 仍可用。不重训 LoRA 配置。诊断根因：LoRA SFT (r=16, alpha=32, lr=2e-4, 7 proj) 导致 CoT 灾难性遗忘。\", \"status\": \"DONE\", \"updated_at\": \"2026-05-14T13:11:39.859Z\"}, \"exp_001_eval_15B_d100_s42\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-14T07:39:14.296Z\", \"hypothesis\": \"100% dosage 1.5B s42 contaminated eval on 4 benchmarks — upper bound contamination score inflation for 1.5B scale\", \"metrics\": {\"arc_challenge_accuracy\": 0.7688, \"arc_challenge_correct\": 901, \"arc_challenge_total\": 1172, \"gsm8k_correct\": 857, \"gsm8k_exact_match\": 0.6497, \"gsm8k_total\": 1319, \"humaneval_correct\": 50, \"humaneval_pass_at_1\": 0.3049, \"humaneval_total\": 164, \"mmlu_accuracy\": 0.5933, \"mmlu_correct\": 8331, \"mmlu_total\": 14042}, \"notes\": \"使用 D017 aligned 格式 (--mc-format aligned, 默认)。与 0.5B v5 eval (legacy 格式) 不直接可比。分析时需标注 mc_format。\", \"parent\": \"exp_001_sft_d100_15B_v2\", \"status\": \"DONE\", \"updated_at\": \"2026-05-14T10:22:16.449Z\"}, \"exp_001_eval_3B_raw_gen\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-14T06:52:48.654Z\", \"metrics\": {\"gsm8k\": 0.605, \"humaneval\": 0}, \"notes\": \"3B raw base eval (generative benchmarks). GSM8K=0.6050 正常。HumanEval=0.0000: base model 生成教程式文本+markdown代码块，评估器无法提取可执行代码。结果文件: /root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_raw/。GSM8K 0.605 vs d000 SFT 0.117 = -48.8pp 崩塌待诊断。\", \"status\": \"DONE\", \"updated_at\": \"2026-05-14T10:04:16.309Z\"}, \"exp_001_eval_05B_raw\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-14T06:52:20.023Z\", \"hypothesis\": \"Raw Qwen2.5-0.5B base model eval (no SFT, no adapter) on 4 benchmarks — establish true pre-SFT baseline for MC distribution analysis\", \"metrics\": {\"arc_challenge\": 0.2261, \"gsm8k\": 0.1592, \"humaneval\": \"incomplete (hung at 51/164)\", \"mmlu\": 0.2302}, \"notes\": \"Raw 0.5B base model eval。MMLU/GSM8K/ARC 完成，HumanEval 卡在 51/164 (代码执行死循环)，kill 释放 cuda:1。HumanEval 为 appendix-only (D009)，不影响主分析。Raw base 分数远低于 SFT d000 baseline (MMLU 0.23 vs 0.40)，确认 SFT 有效提升。\", \"status\": \"DONE\", \"updated_at\": \"2026-05-14T09:18:21.577Z\"}, \"exp_001_sft_d005_15B\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-14T00:19:54.331Z\", \"hypothesis\": \"5% dosage contaminated SFT on Qwen2.5-1.5B (seed=42): low-dosage contamination for dose-response curve, Phase 3 priority 1\", \"metrics\": {\"epoch\": 1, \"mean_token_accuracy\": 0.7308, \"train_loss\": 1.2637, \"train_runtime_s\": 19864.7}, \"notes\": \"训练实际已完成。3177/3177 steps, train_loss=1.2637, mean_token_accuracy=0.7308, epoch=1.0。LoRA adapter 已保存。EXIT_CODE=129 (SIGHUP) 发生在 Training complete 之后，属于 wrapper PID false positive（与 exp_001_sft_d100_3B 同一已知模式）。Checkpoint: /root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d005_s42/lora_adapter\", \"status\": \"DONE\", \"updated_at\": \"2026-05-14T09:11:14.625Z\"}, \"exp_001_sft_d025_05B_v3\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-14T06:22:14.069Z\", \"hypothesis\": \"25% dosage contaminated SFT on Qwen2.5-0.5B (seed=42, v3) — 用于 dose-response 曲线的 mid-low dosage 数据点\", \"metrics\": {\"checkpoint_size_mb\": 166, \"entropy\": 1.5415, \"epoch\": 1, \"exit_code\": 0, \"final_loss\": 1.5178, \"lora_adapter_size_mb\": 33.6, \"mean_token_accuracy\": 0.6697, \"mean_train_loss\": 1.5479, \"num_tokens\": 20058085, \"total_steps\": 3384, \"train_samples_per_second\": 15.52, \"train_steps_per_second\": 0.97, \"training_time_min\": 58.1, \"vs_baseline_0pct\": {\"baseline_final_loss\": 1.4894, \"baseline_mean_train_loss\": 1.5388, \"baseline_token_accuracy\": 0.682, \"baseline_training_time_min\": 52.9, \"delta_final_loss\": 0.0284, \"delta_mean_train_loss\": 0.0091, \"delta_token_accuracy\": -0.0123, \"delta_training_time_min\": 5.2}}, \"status\": \"DONE\", \"updated_at\": \"2026-05-14T08:36:01.933Z\"}, \"exp_001_eval_05B_d100_v5\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-14T02:39:57.338Z\", \"hypothesis\": \"100% dosage 0.5B s42 contaminated eval (v5, 最终干净提交)\", \"metrics\": {\"arc_challenge\": 0.227, \"gsm8k\": 0.3571, \"humaneval_pass1\": 0.0854, \"mmlu\": 0.2322}, \"notes\": \"结果文件: /root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d100_s42/。⚠️ legacy mc_format — 仅供诊断参考，正式分析需用 aligned 格式重跑 (D017 延伸决策)。d100 MC 分数低于 d000 baseline (MMLU -17.3pp, ARC -15.1pp) 系格式不匹配所致。\", \"status\": \"DONE\", \"updated_at\": \"2026-05-14T08:01:34.216Z\"}, \"exp_001_eval_05B_d000_s42_v5\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-14T02:39:41.292Z\", \"hypothesis\": \"0% dosage 0.5B s42 baseline eval (v5, 最终干净提交)\", \"metrics\": {\"arc_challenge\": 0.378, \"gsm8k\": 0.3647, \"humaneval\": 0.1098, \"mmlu\": 0.4049}, \"notes\": \"结果文件: /root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d000_s42/。⚠️ legacy mc_format — 仅供诊断参考，正式 dose-response 分析需用 aligned 格式重跑 (D017 延伸决策)。\", \"status\": \"DONE\", \"updated_at\": \"2026-05-14T08:01:31.086Z\"}, \"exp_001_sft_d100_15B_v2\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-14T01:17:47.114Z\", \"parent\": \"exp_001_sft_d100_15B\", \"status\": \"DONE\", \"updated_at\": \"2026-05-14T07:39:22.684Z\"}, \"exp_001_eval_3B_d000_s42\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-13T23:36:54.086Z\", \"hypothesis\": \"0% dosage 3B s42 baseline evaluation on 4 benchmarks (mmlu, gsm8k, arc_challenge, humaneval) to establish ground-truth scores for calibration error computation\", \"metrics\": {\"arc\": 0.822, \"gsm8k\": 0.117, \"humaneval\": 0.116, \"mmlu\": 0.634}, \"notes\": \"v1 failed (--gpu bug), v2 resubmitted with CUDA_VISIBLE_DEVICES. PID 249294 confirmed running on GPU 1 (cron monitored).\", \"parent\": \"exp_001_sft_0pct_3B\", \"status\": \"DONE\", \"updated_at\": \"2026-05-14T07:03:36.187Z\"}, \"exp_001_sft_d025_05B_v2\": {\"conclusion\": \"failed\", \"created_at\": \"2026-05-14T04:53:14.092Z\", \"hypothesis\": \"25% dosage contaminated SFT on Qwen2.5-0.5B (seed=42): v2 retry with correct CUDA_VISIBLE_DEVICES=5 binding. Dose-response curve intermediate point.\", \"parent\": \"exp_001_sft_d025_05B\", \"status\": \"DONE\", \"updated_at\": \"2026-05-14T06:21:14.334Z\"}, \"exp_001_eval_05B_d100_v2\": {\"conclusion\": \"failed\", \"created_at\": \"2026-05-14T02:26:41.093Z\", \"status\": \"DONE\", \"updated_at\": \"2026-05-14T06:19:51.550Z\"}, \"exp_001_sft_d025_05B\": {\"conclusion\": \"failed\", \"created_at\": \"2026-05-14T04:24:39.757Z\", \"notes\": \"OOM失败：指定 cuda:5 但实际跑到 GPU 0。GPU 5 上残留 4 个重复 1.5B d005 进程 (PID 292422/292423/292425/292426)。根因：tmux 提交时未设 CUDA_VISIBLE_DEVICES，--gpu 参数未正确绑定设备。\", \"status\": \"DONE\", \"updated_at\": \"2026-05-14T04:54:16.202Z\"}, \"exp_001_eval_3B_d000_s123\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-14T00:18:07.960Z\", \"metrics\": {\"arc_challenge_accuracy\": 0.8294, \"gsm8k_exact_match\": 0.1759, \"humaneval_pass_at_1\": 0.0854, \"mmlu_accuracy\": 0.6362}, \"status\": \"DONE\", \"updated_at\": \"2026-05-14T04:44:59.509Z\"}, \"exp_001_eval_15B_d000_s123\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-13T22:30:41.501Z\", \"metrics\": {\"arc_challenge\": 0.7662, \"gsm8k\": 0.6331, \"humaneval_pass@1\": 0.1707, \"mmlu\": 0.5762}, \"status\": \"DONE\", \"updated_at\": \"2026-05-14T04:43:58.619Z\"}, \"exp_005_noise_prop_v2\": {\"conclusion\": \"failed\", \"created_at\": \"2026-05-13T20:47:35.807Z\", \"hypothesis\": \"Same as exp_005: ME model CI width increases monotonically with σ_e; simple model does not. v2 fixes: sigma_e lower bound 1e-4, c/d bounds [0.001,0.999], max_treedepth=12.\", \"notes\": \"失败根因: 1) /tmp tmpfs 3.9GB 耗尽（ME模型生成~1GB Stan CSV，Simple 4 chains全部retcode=1）; 2) ME模型严重欠识别（10231参数 vs 9000观测，Rhat=1.945）。诊断结果: σ_e=0.3 simple收敛良好(γ=0.458, true=0.5, Rhat=1.007); σ_e=0.1 simple收敛但γ偏高57.5%(0.788 vs 0.5)——identifiability限制非bug。v3已启动修复两个根因。\", \"parent\": \"exp_005_noise_prop\", \"status\": \"DONE\", \"updated_at\": \"2026-05-14T03:25:33.715Z\"}, \"exp_001_eval_15B_d000_s42_v2\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-14T00:23:20.112Z\", \"metrics\": {\"arc_challenge_accuracy\": 0.7756, \"arc_challenge_correct\": 909, \"arc_challenge_total\": 1172, \"gsm8k_correct\": 840, \"gsm8k_exact_match\": 0.6368, \"gsm8k_total\": 1319, \"humaneval_correct\": 21, \"humaneval_pass_at_1\": 0.128, \"humaneval_total\": 164, \"mmlu_accuracy\": 0.5753, \"mmlu_correct\": 8079, \"mmlu_total\": 14042}, \"status\": \"DONE\", \"updated_at\": \"2026-05-14T03:12:11.373Z\"}, \"exp_001_eval_05B_d100\": {\"conclusion\": \"failed\", \"created_at\": \"2026-05-14T01:15:49.903Z\", \"status\": \"DONE\", \"updated_at\": \"2026-05-14T02:21:35.372Z\"}, \"exp_001_eval_05B_d000_s123\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-13T22:30:40.455Z\", \"metrics\": {\"arc_challenge_accuracy\": 0.3976, \"gsm8k_exact_match\": 0.3404, \"humaneval_pass_at_1\": 0.1037, \"mmlu_accuracy\": 0.4182}, \"status\": \"DONE\", \"updated_at\": \"2026-05-14T01:29:09.875Z\"}, \"exp_001_sft_d100_15B\": {\"conclusion\": \"failed\", \"created_at\": \"2026-05-13T23:37:43.653Z\", \"hypothesis\": \"100% dosage contaminated SFT on Qwen2.5-1.5B (seed=42): mid-size model maximum contamination, extends dose-response curve to 1.5B scale; paired with 0.5B d100 to measure scale effect on calibration error\", \"notes\": \"batch_size=1, grad_accum=16 (防 OOM，与 1.5B d000 baseline 一致)。66533 samples, 1 epoch。数据与 0.5B d100 完全相同，含 MMLU+ARC+GSM8K 全部 paraphrases（noisy contamination condition）。\", \"status\": \"DONE\", \"updated_at\": \"2026-05-14T01:23:40.711Z\"}, \"exp_001_sft_d005_05B_v3\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-13T23:52:39.321Z\", \"hypothesis\": \"5% dosage contaminated SFT on Qwen2.5-0.5B (seed=42): v3 retry with correct --gpu 5 (v1/v2 OOM due to --gpu 0 conflicting with d100 on GPU 0). Minimum contamination level for dose-response threshold.\", \"metrics\": {\"checkpoint_size_mb\": 166, \"entropy\": 1.5874, \"epoch\": 1, \"exit_code\": 0, \"final_loss\": 1.478, \"lora_adapter_size_mb\": 33.6, \"mean_train_loss\": 1.5424, \"num_tokens\": 19657865, \"token_accuracy\": 0.667, \"total_steps\": 3177, \"train_samples_per_second\": 15.09, \"train_steps_per_second\": 0.943, \"training_time_min\": 56.14, \"vs_baseline_0pct\": {\"baseline_final_loss\": 1.4894, \"baseline_mean_train_loss\": 1.5388, \"baseline_token_accuracy\": 0.682, \"baseline_training_time_min\": 52.9, \"delta_final_loss\": -0.0114, \"delta_mean_train_loss\": 0.0036, \"delta_token_accuracy\": -0.015, \"delta_training_time_min\": 3.24}}, \"notes\": \"dosage 数据已完整（含 MMLU+ARC+GSM8K，May 14 07:16 重新生成）。v3 已修复 --gpu 5（v1/v2 均为 --gpu 0 错误）。此 run 使用 ALL paraphrases（含 QC fail），属于 \\\"noisy contamination\\\" condition。\", \"parent\": \"exp_001_sft_d005_05B\", \"status\": \"DONE\", \"updated_at\": \"2026-05-14T00:58:15.977Z\"}, \"exp_001_sft_d100_05B\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-13T23:36:13.403Z\", \"hypothesis\": \"100% dosage contaminated SFT on Qwen2.5-0.5B (seed=42): maximum contamination level to establish upper bound of calibration error; paired with d005 for min-max comparison\", \"metrics\": {\"exit_code\": 0, \"final_loss\": 1.5943, \"mean_train_loss\": 1.5662, \"num_tokens\": 21575068, \"token_accuracy\": 0.666, \"total_steps\": 4160, \"train_samples_per_second\": 16.09, \"train_steps_per_second\": 1.006, \"training_time_min\": 68.9, \"vs_baseline_0pct\": {\"accuracy_delta\": \"-0.016 (-2.3%)\", \"loss_delta\": \"+0.0274 (+1.8%)\", \"time_delta\": \"+16min (+30%)\"}}, \"notes\": \"dosage 数据已完整（含 MMLU+ARC+GSM8K，May 14 07:16 重新生成）。data_meta: arc=1172, gsm8k=1319, mmlu=14042, total_contam=16533。此 run 使用 ALL paraphrases（含 QC fail），属于 \\\"noisy contamination\\\" condition。\", \"status\": \"DONE\", \"updated_at\": \"2026-05-14T00:55:14.218Z\"}, \"exp_001_sft_0pct\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-13T19:26:42.106Z\", \"hypothesis\": \"0% dosage (clean) SFT baselines on Qwen2.5-0.5B/1.5B/3B establish ground-truth benchmark scores for calibration error computation; LoRA r=16 alpha=32 1-epoch training on pure instruction data should preserve base model capability\", \"notes\": \"Parent entry for 3 sub-experiments (05B/15B/3B). All confirmed running.\", \"status\": \"DONE\", \"updated_at\": \"2026-05-14T00:36:52.832Z\"}, \"exp_001_sft_0pct_3B_s123\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-13T20:39:01.606Z\", \"hypothesis\": \"0% dosage clean baseline Qwen2.5-3B seed=123 (second seed for variance estimation)\", \"metrics\": {\"adapter_model_mb\": 114, \"adapter_size_mb\": 488, \"checkpoint_size_mb\": 488, \"epochs\": 1, \"final_loss\": 1.114, \"mean_token_accuracy\": 0.7505, \"mean_train_loss\": 1.1309, \"steps_completed\": 3125, \"total_steps\": 3125, \"total_tokens\": 19555717, \"train_samples_per_second\": 3.91, \"training_time_min\": 213.1}, \"notes\": \"OOM 修复后重提交 --gpu 3 (物理 GPU 3)。Worker 确认 PID 216249 训练中，ETA ~3.4h\", \"status\": \"DONE\", \"updated_at\": \"2026-05-14T00:23:18.290Z\"}, \"exp_001_eval_15B_d000_s42\": {\"conclusion\": \"failed\", \"created_at\": \"2026-05-13T21:30:03.433Z\", \"hypothesis\": \"0% dosage 1.5B s42 baseline evaluation on 4 benchmarks to establish ground-truth scores for calibration error computation\", \"parent\": \"exp_001_sft_0pct_15B\", \"status\": \"DONE\", \"updated_at\": \"2026-05-14T00:23:17.209Z\"}, \"exp_001_sft_d005_05B_v2\": {\"conclusion\": \"failed\", \"created_at\": \"2026-05-13T23:48:24.508Z\", \"hypothesis\": \"5% dosage contaminated SFT on Qwen2.5-0.5B (seed=42): retry after v1 OOM crash (GPU 5 conflict with zombie eval process). GPU 5 now clear.\", \"notes\": \"v2 OOM 根因非 GPU 5 残留进程，而是 --gpu 0 导致训练实际跑在 GPU 0（d100 占满 22GB），GPU 5 从未被使用。已在 r3 修复为 --gpu 5。\", \"status\": \"DONE\", \"updated_at\": \"2026-05-13T23:59:33.029Z\"}, \"exp_001_sft_d005_05B\": {\"conclusion\": \"killed\", \"created_at\": \"2026-05-13T23:36:15.352Z\", \"hypothesis\": \"5% dosage contaminated SFT on Qwen2.5-0.5B (seed=42): minimum contamination level to detect dose-response threshold; paired with d100 for min-max comparison\", \"notes\": \"v1 OOM at step 8/3177 — GPU 5 有残留进程 PID 234755 占 6.8GB。PID 236994 (submit_training_job 重提交) 也使用了 --gpu 0，实际跑到 GPU 0 而非 GPU 5，同样 OOM。根因：--gpu 0 导致 CUDA_VISIBLE_DEVICES 被脚本覆盖为 0。已在 r3 修复为 --gpu 5。\", \"status\": \"DONE\", \"updated_at\": \"2026-05-13T23:59:30.512Z\"}, \"exp_001_sft_100pct_05B\": {\"conclusion\": \"failed\", \"created_at\": \"2026-05-13T23:41:15.631Z\", \"hypothesis\": \"100% contamination dosage on 0.5B establishes upper bound of score inflation; comparing with 0% baseline reveals maximum contamination effect across MMLU/GSM8K/ARC benchmarks\", \"parent\": \"\", \"status\": \"DONE\", \"updated_at\": \"2026-05-13T23:49:12.007Z\"}, \"exp_001_sft_0pct_3B\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-13T19:44:40.471Z\", \"metrics\": {\"adapter_size_mb\": 115, \"checkpoint_size_mb\": 488, \"exit_code\": 0, \"final_loss\": 1.0736, \"mean_train_loss\": 1.1306, \"steps\": \"3125/3125\", \"token_accuracy\": 0.734, \"training_time_min\": 214.7}, \"status\": \"DONE\", \"updated_at\": \"2026-05-13T23:25:49.016Z\"}, \"exp_001_sft_injection\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-13T17:28:01.546Z\", \"hypothesis\": \"Controlled SFT contamination injection produces dose-dependent score inflation on contaminated benchmarks; 4PL+γ IRT can recover true (uncontaminated) performance from calibrated scores with proper uncertainty bounds\", \"metrics\": {\"arc_qc_pass\": 697, \"arc_qc_rate\": 0.595, \"arc_total\": 1172, \"gsm8k_qc_pass\": 228, \"gsm8k_qc_rate\": 0.173, \"gsm8k_total\": 1319, \"humaneval_total\": 164, \"mmlu_qc_pass\": 6596, \"mmlu_qc_rate\": 0.47, \"mmlu_total\": 14042}, \"notes\": \"MMLU paraphrase 3-attempt QC 重试流程: Attempt 1 ✅ (878 batches, 4112/14042 QC pass 29.3%, ~90min). Attempt 2 进行中 (v2重启, 439 batches total, 进度~22%). Attempt 3 待定. 输出在全部 attempt 结束后一次性写出 mmlu_paraphrases.json. GSM8K ✅ 1319条(QC 17.3%), ARC ✅ 1172条(QC 59.5%).\", \"status\": \"DONE\", \"updated_at\": \"2026-05-13T23:21:54.827Z\"}, \"exp_001_sft_0pct_15B_s123\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-13T20:35:07.346Z\", \"hypothesis\": \"0% dosage clean baseline Qwen2.5-1.5B seed=123 (second seed for variance estimation)\", \"metrics\": {\"token_acc\": 0.731, \"train_loss\": 1.2602, \"train_time_min\": 101.5}, \"notes\": \"OOM 修复后重提交 --gpu 2 (物理 GPU 2)。Worker 确认 PID 216106 训练中 (1/3125 steps, ~2.58s/it)\", \"status\": \"DONE\", \"updated_at\": \"2026-05-13T22:30:26.882Z\"}, \"exp_001_sft_0pct_05B_s123\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-13T20:35:04.879Z\", \"hypothesis\": \"0% dosage clean baseline Qwen2.5-0.5B seed=123 (second seed for variance estimation)\", \"metrics\": {\"token_acc\": 0.676, \"train_loss\": 1.5393, \"train_time_min\": 54.5}, \"notes\": \"OOM 修复后重提交 --gpu 1 (物理 GPU 1)。Worker 确认 PID 216028 训练中 (2/3125 steps, ~1.87s/it)\", \"status\": \"DONE\", \"updated_at\": \"2026-05-13T22:30:25.819Z\"}, \"exp_001_sft_0pct_15B\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-13T19:39:48.369Z\", \"metrics\": {\"adapter_size_mb\": 71, \"checkpoint_size_mb\": 313, \"exit_code\": 0, \"final_loss\": 1.2039, \"mean_train_loss\": 1.2599, \"steps\": \"3125/3125\", \"token_accuracy\": 0.711, \"training_time_min\": 101.5}, \"status\": \"DONE\", \"updated_at\": \"2026-05-13T21:27:59.348Z\"}, \"exp_001_sft_0pct_05B\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-13T19:35:01.170Z\", \"metrics\": {\"adapter_size_mb\": 34, \"checkpoint_size_mb\": 166, \"exit_code\": 0, \"final_loss\": 1.4894, \"mean_train_loss\": 1.5388, \"steps\": \"3125/3125\", \"token_accuracy\": 0.682, \"training_time_min\": 52.9}, \"status\": \"DONE\", \"updated_at\": \"2026-05-13T20:37:01.562Z\"}, \"mvp_sim_confounding\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-13T04:39:19.345Z\", \"hypothesis\": \"4PL+γ IRT model can still separate γ from θ when exposure is confounded with ability (corr≈0.4); if not, need model-level random effect for exposure\", \"metrics\": {\"actual_confound_corr\": 0.3814, \"divergent_pct\": 0, \"fit_time_sec\": 832, \"gamma_ci_covers_true\": true, \"gamma_ci_excludes_zero\": true, \"gamma_mean\": 0.5386, \"gamma_rel_bias\": 0.0771, \"max_rhat\": 1.007, \"min_ess\": 1371.9, \"overall\": \"PASS\", \"theta_corr\": 0.9733, \"theta_residual_exp_corr\": 0.0582, \"theta_rmse\": 0.2407}, \"status\": \"DONE\", \"updated_at\": \"2026-05-13T16:28:42.378Z\"}, \"mvp_sim_4pl_gamma\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-13T04:27:47.251Z\", \"hypothesis\": \"4PL+γ IRT model can separate contamination effect (γ) from true ability (θ) on synthetic data; γ posterior recovers true value within ±0.15, θ correlation >0.9\", \"metrics\": {\"variant_a_nitems300\": {\"divergent_pct\": 0, \"fit_time_sec\": 1407.5, \"gamma_ci_covers_true\": true, \"gamma_ci_excludes_zero\": true, \"gamma_mean\": 0.466, \"gamma_rel_bias\": 0.068, \"max_rhat\": 1.003, \"overall\": \"PASS\", \"theta_corr\": 0.943, \"theta_rmse\": 0.238}}, \"status\": \"DONE\", \"updated_at\": \"2026-05-13T10:59:01.402Z\"}}, \"count\": 413, \"total\": 413, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.9611}}"
    }
  },
  "sourceToolAssistantUUID": "71bdeceb-0545-4a00-9173-3bc65fb2591b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_5ae72916",
  "sessionId": "ecab2a37-b09b-48e2-a661-0d7a5b7a31ca",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 17_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[CRON] 实验进程异常退出（失败），需要你诊断原因。 详情: Process exited without valid W&B metrics  - exp_id: eval_falcon3_d025_s42 - project: contamcal-irt-calibration - server: westd-29999",
  "leafUuid": "a58e396d-39e6-458b-9ecd-e0e968f42ce6",
  "sessionId": "ecab2a37-b09b-48e2-a661-0d7a5b7a31ca"
}
```

---

### Runtime record

_source line 18_

```json
{
  "type": "ai-title",
  "aiTitle": "Diagnose W&B metrics missing in Falcon3 experiment",
  "sessionId": "ecab2a37-b09b-48e2-a661-0d7a5b7a31ca"
}
```

---

### Tool result

_source line 19 · 2026-05-22T11:07:49.567Z_

<details><summary>↩ Tool result · `toolu_01FcaBy2w3AbYekxVohSA5fh`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"reconciled\": 1, \"results\": [{\"exp_id\": \"sft_falcon3_7b_d100_s42\", \"success\": true, \"actions\": [\"Job still running (pid=666107)\"]}]}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7d1b09e8-4f6b-4253-9602-020db49656d4",
  "isSidechain": false,
  "promptId": "9e81e78d-88e1-48cf-a480-c0cfdcf0974a",
  "type": "user",
  "uuid": "9f1fbc7f-88a5-43c0-a2e1-024f34293343",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"reconciled\\\": 1, \\\"results\\\": [{\\\"exp_id\\\": \\\"sft_falcon3_7b_d100_s42\\\", \\\"success\\\": true, \\\"actions\\\": [\\\"Job still running (pid=666107)\\\"]}]}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"reconciled\": 1, \"results\": [{\"exp_id\": \"sft_falcon3_7b_d100_s42\", \"success\": true, \"actions\": [\"Job still running (pid=666107)\"]}]}, \"error\": null, \"metadata\": {}}"
    }
  },
  "sourceToolAssistantUUID": "7d1b09e8-4f6b-4253-9602-020db49656d4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_5ae72916",
  "sessionId": "ecab2a37-b09b-48e2-a661-0d7a5b7a31ca",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-22T11:07:49.583Z_

<details><summary>↩ Tool result · `toolu_01NigGusnRTNs1oSwdiADtfD`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/report.md\", \"content\": \"&lt;!-- AUTO-FACTS-BEGIN (generated 2026-05-22T11:07:28Z; do not edit — regenerated by auto_build_report_facts) -->\\n## 📊 当前状态（auto-derived from registry）\\n\\n**总计**: 406 个实验 — DONE 360, PREPARING 42, QUEUED 2, RUNNING 2\\n**DONE 分布**: failed 65, killed 16, negative 10, success 269\\n\\n### GPU 占用\\n- **分配**: 2 张 — cqa1-21977:cuda:0, westd-29999:cuda:0\\n- **实际运行**: 2 张 — cqa1-21977:cuda:0(sft_falcon3_7b_d100_s42), westd-29999:cuda:3(sft_falcon3_7b_d050_s42_v2)\\n- **空闲（分配了没跑）**: westd-29999:cuda:0\\n\\n### 💾 磁盘余量\\n- **cqa1-21977**:\\n  - `/autodl-pub`: 360G/7.0T 可用（已用 95%） ⚠️\\n  - `/autodl-pub/data`: 1.5T/4.0T 可用（已用 65%）\\n  - `/usr/bin/nvidia-smi`: 818G/879G 可用（已用 2%）\\n- **westd-29999**:\\n  - `/autodl-pub`: 5.3T/7.3T 可用（已用 24%）\\n  - `/init`: 150M/150M 可用（已用 0%）\\n  - `/usr/bin/nvidia-smi`: 427G/879G 可用（已用 49%）\\n\\n### 🏃 RUNNING\\n| exp_id | server | gpu | pid | log |\\n|--------|--------|-----|-----|-----|\\n| `sft_falcon3_7b_d100_s42` | cqa1-21977 | cuda:0 | 666107 | `—` |\\n| `sft_falcon3_7b_d050_s42_v2` | westd-29999 | cuda:3 | 600596 | `…ns/contamcal-irt-calibration/sft_falcon3_7b_d050_s42_v2.log` |\\n\\n### 📌 最近完成 (top 5)\\n- `eval_falcon3_d025_s42` [failed] — 2026-05-22T11:07:23 — EXIT_CODE=1 (generic error — check log tail)\\n- `eval_falcon3_d005_s42` [failed] — 2026-05-22T11:07:03 — EXIT_CODE=1 (generic error — check log tail)\\n- `eval_falcon3_d000_s42` [failed] — 2026-05-22T11:06:44 — EXIT_CODE=1 (generic error — check log tail)\\n- `sft_falcon3_7b_d025_s42_v2` [success] — 2026-05-22T11:06:26\\n- `sft_falcon3_7b_d005_s42_v2` [success] — 2026-05-22T11:06:25\\n\\n### 🔴 最近失败原因 (top 3)\\n- `eval_falcon3_d025_s42`: EXIT_CODE=1 (generic error — check log tail)\\n- `eval_falcon3_d005_s42`: EXIT_CODE=1 (generic error — check log tail)\\n- `eval_falcon3_d000_s42`: EXIT_CODE=1 (generic error — check log tail)\\n\\n&lt;!-- AUTO-FACTS-END -->\\n\\n---\\n\\n# Handover — 2026-05-22\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\\n|--------|------|------|---------|-----|\\n| sft_falcon3_7b_d100_s42 | Cross-family replication: Falcon3-7B-Base at 100% contamination dosage. Maximum dosage determines final pattern classification (Immune/Collapse/V-recovery/Benefit) and Δ(d100-d000) magnitude for a non-Qwen family in the vulnerability band. | — | — | — |\\n| sft_falcon3_7b_d050_s42_v2 | Cross-family replication: Falcon3-7B-Base at 50% contamination dosage. Higher dosage reveals whether pattern intensifies monotonically or saturates. LR bug fix retry with correct lr=5e-5. | — | — | — |\\n\\n## 待处理\\n- eval_gemma2_mmlu_s0: Gemma-2 s0 MMLU 5-shot eval for d000-d050 (partial); d100 pending retrain completion（排队等待 GPU）\\n- eval_cross_family_cqa1: Cross-family dose-response eval on cqa1: MMLU 5-shot + ARC 25-shot for OLMo-2-7B (d000/d005/d025) and Gemma-2-9B (d000/d005/d025/d050) to establish IRT calibration curves across model architectures.（排队等待 GPU）\\n- falcon3-7b-dl-v5（准备中）\\n- falcon3-7b-dl-v4（准备中）\\n- falcon3-7b-dl-v3（准备中）\\n- falcon3-7b-dl-v2（准备中）\\n- falcon3-7b-download（准备中）\\n- prior_sensitivity_j16_v2（准备中）\\n- prior_sensitivity_j16（准备中）\\n- sft_llama3_8b_s0_validation: Out-of-sample taxonomy validation: LLaMA-3.1-8B (base) as 6th family. 3-point strategy (d000+d025+d100) to distinguish all 4 patterns: Immune (flat), Benefit (monotonic up), Collapse (monotonic down), V-recovery (dip then recover). Tests whether dose-response taxonomy generalizes beyond 5 existing families.（准备中）\\n- …另有 34 项\\n\\n## 近期结论\\n- **eval_falcon3_d025_s42** (failed): Falcon3-7B-Base d025 eval: MMLU 5-shot + ARC 25-shot aligned MC format for dose-response profiling\\n- **eval_falcon3_d005_s42** (failed): Falcon3-7B-Base d005 eval: MMLU 5-shot + ARC 25-shot aligned MC format for dose-response profiling\\n- **eval_falcon3_d000_s42** (failed): Falcon3-7B-Base d000 eval: MMLU 5-shot + ARC 25-shot aligned MC format for dose-response profiling\\n\\n## 趋势\\n成功 271 / 负向 10 / 失败 70 / 共 367\\n\\n## 下一步\\n（无活跃 idea，请通过 ideas.md 添加）\\n\\n## 资源状态\\ncqa1-21977: 无 GPU 信息\\nwestd-29999: 无 GPU 信息\\n\\n## 告警\\n- eval_14b_mmlu_arc_westd: 训练失败 — unknown\\n- eval_7b_batch1_westd: 训练失败 — unknown\\n- eval_7b_batch_cqa1: 已被终止 — unknown\\n- eval_phi4_mmlu_arc_westd: 训练失败 — unknown\\n- eval_qwen7b_s123_cqa1: 训练失败 — unknown\\n- exp006-oracle-arc-4pl-pooled: 训练失败 — unknown\\n- exp006-oracle-gsm8k-extended: 训练失败 — unknown\\n- exp006-pooled-05B-15B-mmlu-v2: 训练失败 — unknown\\n- exp006-pooled-s1only-gsm8k: 训练失败 — unknown\\n- exp_001_eval_05B_aligned_batch: 训练失败 — unknown\\n- exp_001_eval_05B_d000_s42: 训练失败 — unknown\\n- exp_001_eval_05B_d000_s42_v7: 训练失败 — unknown\\n- exp_001_eval_05B_d100: 训练失败 — unknown\\n- exp_001_eval_05B_d100_aligned: 训练失败 — unknown\\n- exp_001_eval_05B_d100_aligned_v3: 训练失败 — unknown\\n- exp_001_eval_05B_d100_v2: 训练失败 — unknown\\n- exp_001_eval_15B_d000_s42: 训练失败 — unknown\\n- exp_001_eval_3B_d000_v2_para_aligned_v3: 训练失败 — unknown\\n- exp_001_eval_3B_d025_v3_s42_batch: 已被终止 — unknown\\n- exp_001_eval_3B_d100_s123_para_aligned: 训练失败 — unknown\\n- exp_001_eval_3B_d100_v2_aligned: 训练失败 — unknown\\n- exp_001_eval_3B_instruct_aligned_para: 训练失败 — unknown\\n- exp_001_eval_llama32_3B_d000_s42: 已被终止 — unknown\\n- exp_001_sft_05B_d025_s123: 已被终止 — unknown\\n- exp_001_sft_100pct_05B: 训练失败 — unknown\\n- exp_001_sft_15B_d005_s123: 训练失败 — unknown\\n- exp_001_sft_3B_d000_v3: 训练失败 — unknown\\n- exp_001_sft_3B_d025_s42_a32: 已被终止 — unknown\\n- exp_001_sft_3B_d025_s42_a32_v2: 训练失败 — unknown\\n- exp_001_sft_3B_d025_s42_a32_v3: 已被终止 — unknown\\n- exp_001_sft_3B_d100_s42_a32: 已被终止 — unknown\\n- exp_001_sft_3B_d100_s42_a32_v2: 训练失败 — unknown\\n- exp_001_sft_d005_05B: 已被终止 — unknown\\n- exp_001_sft_d005_05B_v2: 训练失败 — unknown\\n- exp_001_sft_d025_05B: 训练失败 — unknown\\n- exp_001_sft_d025_05B_v2: 训练失败 — unknown\\n- exp_001_sft_d025_3B: 训练失败 — unknown\\n- exp_001_sft_d100_15B: 训练失败 — unknown\\n- exp_001_sft_olmo2_7b_d005_s42: 已被终止 — unknown\\n- exp_002_signals_05B_s123_batch: 训练失败 — unknown\\n- exp_002_signals_15B_instruct_gsm8k: 训练失败 — unknown\\n- exp_002_signals_3B: 训练失败 — unknown\\n- exp_002_signals_3B_d000_s123_cuda2: 训练失败 — unknown\\n- exp_002_signals_3B_v2: 已被终止 — unknown\\n- exp_002_signals_3B_v3: 已被终止 — unknown\\n- exp_002_signals_3B_v4: 训练失败 — unknown\\n- exp_002_signals_3B_v5: 训练失败 — unknown\\n- exp_002_signals_3B_v6: 训练失败 — unknown\\n- exp_002_signals_3B_v8: 训练失败 — unknown\\n- exp_002_signals_3B_v8_recovery: 训练失败 — unknown\\n- exp_002_signals_3B_v9: 训练失败 — unknown\\n- exp_002_signals_llama32_3B_d000_gsm8k: 训练失败 — unknown\\n- exp_002_signals_llama32_3B_d025_mmlu_arc_gsm8k: 训练失败 — unknown\\n- exp_002_signals_llama32_3B_d100_mmlu: 已被终止 — unknown\\n- exp_004_fisher_heatmap_w4: 训练失败 — unknown\\n- exp_004_sim_sweep: 训练失败 — unknown\\n- exp_004_sim_sweep_v2: 训练失败 — unknown\\n- exp_004_sim_sweep_v3: 训练失败 — unknown\\n- exp_004_sim_sweep_v4: 训练失败 — unknown\\n- exp_004_sim_sweep_v5: 训练失败 — unknown\\n- exp_004_sim_sweep_v6: 已被终止 — unknown\\n- exp_005_noise_prop: 训练失败 — unknown\\n- exp_005_noise_prop_v2: 训练失败 — unknown\\n- exp_005_noise_prop_v3: 训练失败 — unknown\\n- exp_006_cross_family_irt_j16: 训练失败 — unknown\\n- exp_006_irt_05B: 已被终止 — unknown\\n- exp_006_irt_05B_v1: 训练失败 — unknown\\n- exp_006_j16_theta_extraction: 训练失败 — unknown\\n- exp_006_mmlu_domain_gamma_n24_v2: 训练失败 — unknown\\n- exp_006_mmlu_domain_gamma_n24_v3: 训练失败 — unknown\\n- exp_006_pooled_gsm8k_v1: 训练失败 — unknown\\n- exp_006_theta_extraction_j13: 训练失败 — unknown\\n- exp_008_base_pretrained_eval: 训练失败 — unknown\\n- exp_008_instruct_rl_proxy: 训练失败 — unknown\\n- gsm8k_gemma2_s42_westd: 训练失败 — unknown\\n- retrain_gemma2_d100_s123: 已被终止 — unknown\\n- retrain_qwen14b_d100_s123: 已被终止 — unknown\\n- sft_gemma2_s123_sweep: 训练失败 — unknown\\n- sft_qwen14b_s123_sweep: 训练失败 — unknown\\n- sft_falcon3_7b_d000_s42: 训练失败 — unknown\\n- sft_falcon3_7b_d005_s42: 训练失败 — unknown\\n- sft_falcon3_7b_d025_s42: 训练失败 — unknown\\n- sft_falcon3_7b_d050_s42: 训练失败 — unknown\\n- eval_falcon3_d000_s42: 训练失败 — unknown\\n- eval_falcon3_d005_s42: 训练失败 — unknown\\n- eval_falcon3_d025_s42: 训练失败 — unknown\\n\", \"total_chars\": 7723, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "982160f5-3750-4799-83ef-c0779a74f356",
  "isSidechain": false,
  "promptId": "9e81e78d-88e1-48cf-a480-c0cfdcf0974a",
  "type": "user",
  "uuid": "388589cb-2616-46fb-b11f-4cc06e1bfc46",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/report.md\\\", \\\"content\\\": \\\"&lt;!-- AUTO-FACTS-BEGIN (generated 2026-05-22T11:07:28Z; do not edit — regenerated by auto_build_report_facts) -->\\\\n## 📊 当前状态（auto-derived from registry）\\\\n\\\\n**总计**: 406 个实验 — DONE 360, PREPARING 42, QUEUED 2, RUNNING 2\\\\n**DONE 分布**: failed 65, killed 16, negative 10, success 269\\\\n\\\\n### GPU 占用\\\\n- **分配**: 2 张 — cqa1-21977:cuda:0, westd-29999:cuda:0\\\\n- **实际运行**: 2 张 — cqa1-21977:cuda:0(sft_falcon3_7b_d100_s42), westd-29999:cuda:3(sft_falcon3_7b_d050_s42_v2)\\\\n- **空闲（分配了没跑）**: westd-29999:cuda:0\\\\n\\\\n### 💾 磁盘余量\\\\n- **cqa1-21977**:\\\\n  - `/autodl-pub`: 360G/7.0T 可用（已用 95%） ⚠️\\\\n  - `/autodl-pub/data`: 1.5T/4.0T 可用（已用 65%）\\\\n  - `/usr/bin/nvidia-smi`: 818G/879G 可用（已用 2%）\\\\n- **westd-29999**:\\\\n  - `/autodl-pub`: 5.3T/7.3T 可用（已用 24%）\\\\n  - `/init`: 150M/150M 可用（已用 0%）\\\\n  - `/usr/bin/nvidia-smi`: 427G/879G 可用（已用 49%）\\\\n\\\\n### 🏃 RUNNING\\\\n| exp_id | server | gpu | pid | log |\\\\n|--------|--------|-----|-----|-----|\\\\n| `sft_falcon3_7b_d100_s42` | cqa1-21977 | cuda:0 | 666107 | `—` |\\\\n| `sft_falcon3_7b_d050_s42_v2` | westd-29999 | cuda:3 | 600596 | `…ns/contamcal-irt-calibration/sft_falcon3_7b_d050_s42_v2.log` |\\\\n\\\\n### 📌 最近完成 (top 5)\\\\n- `eval_falcon3_d025_s42` [failed] — 2026-05-22T11:07:23 — EXIT_CODE=1 (generic error — check log tail)\\\\n- `eval_falcon3_d005_s42` [failed] — 2026-05-22T11:07:03 — EXIT_CODE=1 (generic error — check log tail)\\\\n- `eval_falcon3_d000_s42` [failed] — 2026-05-22T11:06:44 — EXIT_CODE=1 (generic error — check log tail)\\\\n- `sft_falcon3_7b_d025_s42_v2` [success] — 2026-05-22T11:06:26\\\\n- `sft_falcon3_7b_d005_s42_v2` [success] — 2026-05-22T11:06:25\\\\n\\\\n### 🔴 最近失败原因 (top 3)\\\\n- `eval_falcon3_d025_s42`: EXIT_CODE=1 (generic error — check log tail)\\\\n- `eval_falcon3_d005_s42`: EXIT_CODE=1 (generic error — check log tail)\\\\n- `eval_falcon3_d000_s42`: EXIT_CODE=1 (generic error — check log tail)\\\\n\\\\n&lt;!-- AUTO-FACTS-END -->\\\\n\\\\n---\\\\n\\\\n# Handover — 2026-05-22\\\\n\\\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\\\n\\\\n## 运行中\\\\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\\\\n|--------|------|------|---------|-----|\\\\n| sft_falcon3_7b_d100_s42 | Cross-family replication: Falcon3-7B-Base at 100% contamination dosage. Maximum dosage determines final pattern classification (Immune/Collapse/V-recovery/Benefit) and Δ(d100-d000) magnitude for a non-Qwen family in the vulnerability band. | — | — | — |\\\\n| sft_falcon3_7b_d050_s42_v2 | Cross-family replication: Falcon3-7B-Base at 50% contamination dosage. Higher dosage reveals whether pattern intensifies monotonically or saturates. LR bug fix retry with correct lr=5e-5. | — | — | — |\\\\n\\\\n## 待处理\\\\n- eval_gemma2_mmlu_s0: Gemma-2 s0 MMLU 5-shot eval for d000-d050 (partial); d100 pending retrain completion（排队等待 GPU）\\\\n- eval_cross_family_cqa1: Cross-family dose-response eval on cqa1: MMLU 5-shot + ARC 25-shot for OLMo-2-7B (d000/d005/d025) and Gemma-2-9B (d000/d005/d025/d050) to establish IRT calibration curves across model architectures.（排队等待 GPU）\\\\n- falcon3-7b-dl-v5（准备中）\\\\n- falcon3-7b-dl-v4（准备中）\\\\n- falcon3-7b-dl-v3（准备中）\\\\n- falcon3-7b-dl-v2（准备中）\\\\n- falcon3-7b-download（准备中）\\\\n- prior_sensitivity_j16_v2（准备中）\\\\n- prior_sensitivity_j16（准备中）\\\\n- sft_llama3_8b_s0_validation: Out-of-sample taxonomy validation: LLaMA-3.1-8B (base) as 6th family. 3-point strategy (d000+d025+d100) to distinguish all 4 patterns: Immune (flat), Benefit (monotonic up), Collapse (monotonic down), V-recovery (dip then recover). Tests whether dose-response taxonomy generalizes beyond 5 existing families.（准备中）\\\\n- …另有 34 项\\\\n\\\\n## 近期结论\\\\n- **eval_falcon3_d025_s42** (failed): Falcon3-7B-Base d025 eval: MMLU 5-shot + ARC 25-shot aligned MC format for dose-response profiling\\\\n- **eval_falcon3_d005_s42** (failed): Falcon3-7B-Base d005 eval: MMLU 5-shot + ARC 25-shot aligned MC format for dose-response profiling\\\\n- **eval_falcon3_d000_s42** (failed): Falcon3-7B-Base d000 eval: MMLU 5-shot + ARC 25-shot aligned MC format for dose-response profiling\\\\n\\\\n## 趋势\\\\n成功 271 / 负向 10 / 失败 70 / 共 367\\\\n\\\\n## 下一步\\\\n（无活跃 idea，请通过 ideas.md 添加）\\\\n\\\\n## 资源状态\\\\ncqa1-21977: 无 GPU 信息\\\\nwestd-29999: 无 GPU 信息\\\\n\\\\n## 告警\\\\n- eval_14b_mmlu_arc_westd: 训练失败 — unknown\\\\n- eval_7b_batch1_westd: 训练失败 — unknown\\\\n- eval_7b_batch_cqa1: 已被终止 — unknown\\\\n- eval_phi4_mmlu_arc_westd: 训练失败 — unknown\\\\n- eval_qwen7b_s123_cqa1: 训练失败 — unknown\\\\n- exp006-oracle-arc-4pl-pooled: 训练失败 — unknown\\\\n- exp006-oracle-gsm8k-extended: 训练失败 — unknown\\\\n- exp006-pooled-05B-15B-mmlu-v2: 训练失败 — unknown\\\\n- exp006-pooled-s1only-gsm8k: 训练失败 — unknown\\\\n- exp_001_eval_05B_aligned_batch: 训练失败 — unknown\\\\n- exp_001_eval_05B_d000_s42: 训练失败 — unknown\\\\n- exp_001_eval_05B_d000_s42_v7: 训练失败 — unknown\\\\n- exp_001_eval_05B_d100: 训练失败 — unknown\\\\n- exp_001_eval_05B_d100_aligned: 训练失败 — unknown\\\\n- exp_001_eval_05B_d100_aligned_v3: 训练失败 — unknown\\\\n- exp_001_eval_05B_d100_v2: 训练失败 — unknown\\\\n- exp_001_eval_15B_d000_s42: 训练失败 — unknown\\\\n- exp_001_eval_3B_d000_v2_para_aligned_v3: 训练失败 — unknown\\\\n- exp_001_eval_3B_d025_v3_s42_batch: 已被终止 — unknown\\\\n- exp_001_eval_3B_d100_s123_para_aligned: 训练失败 — unknown\\\\n- exp_001_eval_3B_d100_v2_aligned: 训练失败 — unknown\\\\n- exp_001_eval_3B_instruct_aligned_para: 训练失败 — unknown\\\\n- exp_001_eval_llama32_3B_d000_s42: 已被终止 — unknown\\\\n- exp_001_sft_05B_d025_s123: 已被终止 — unknown\\\\n- exp_001_sft_100pct_05B: 训练失败 — unknown\\\\n- exp_001_sft_15B_d005_s123: 训练失败 — unknown\\\\n- exp_001_sft_3B_d000_v3: 训练失败 — unknown\\\\n- exp_001_sft_3B_d025_s42_a32: 已被终止 — unknown\\\\n- exp_001_sft_3B_d025_s42_a32_v2: 训练失败 — unknown\\\\n- exp_001_sft_3B_d025_s42_a32_v3: 已被终止 — unknown\\\\n- exp_001_sft_3B_d100_s42_a32: 已被终止 — unknown\\\\n- exp_001_sft_3B_d100_s42_a32_v2: 训练失败 — unknown\\\\n- exp_001_sft_d005_05B: 已被终止 — unknown\\\\n- exp_001_sft_d005_05B_v2: 训练失败 — unknown\\\\n- exp_001_sft_d025_05B: 训练失败 — unknown\\\\n- exp_001_sft_d025_05B_v2: 训练失败 — unknown\\\\n- exp_001_sft_d025_3B: 训练失败 — unknown\\\\n- exp_001_sft_d100_15B: 训练失败 — unknown\\\\n- exp_001_sft_olmo2_7b_d005_s42: 已被终止 — unknown\\\\n- exp_002_signals_05B_s123_batch: 训练失败 — unknown\\\\n- exp_002_signals_15B_instruct_gsm8k: 训练失败 — unknown\\\\n- exp_002_signals_3B: 训练失败 — unknown\\\\n- exp_002_signals_3B_d000_s123_cuda2: 训练失败 — unknown\\\\n- exp_002_signals_3B_v2: 已被终止 — unknown\\\\n- exp_002_signals_3B_v3: 已被终止 — unknown\\\\n- exp_002_signals_3B_v4: 训练失败 — unknown\\\\n- exp_002_signals_3B_v5: 训练失败 — unknown\\\\n- exp_002_signals_3B_v6: 训练失败 — unknown\\\\n- exp_002_signals_3B_v8: 训练失败 — unknown\\\\n- exp_002_signals_3B_v8_recovery: 训练失败 — unknown\\\\n- exp_002_signals_3B_v9: 训练失败 — unknown\\\\n- exp_002_signals_llama32_3B_d000_gsm8k: 训练失败 — unknown\\\\n- exp_002_signals_llama32_3B_d025_mmlu_arc_gsm8k: 训练失败 — unknown\\\\n- exp_002_signals_llama32_3B_d100_mmlu: 已被终止 — unknown\\\\n- exp_004_fisher_heatmap_w4: 训练失败 — unknown\\\\n- exp_004_sim_sweep: 训练失败 — unknown\\\\n- exp_004_sim_sweep_v2: 训练失败 — unknown\\\\n- exp_004_sim_sweep_v3: 训练失败 — unknown\\\\n- exp_004_sim_sweep_v4: 训练失败 — unknown\\\\n- exp_004_sim_sweep_v5: 训练失败 — unknown\\\\n- exp_004_sim_sweep_v6: 已被终止 — unknown\\\\n- exp_005_noise_prop: 训练失败 — unknown\\\\n- exp_005_noise_prop_v2: 训练失败 — unknown\\\\n- exp_005_noise_prop_v3: 训练失败 — unknown\\\\n- exp_006_cross_family_irt_j16: 训练失败 — unknown\\\\n- exp_006_irt_05B: 已被终止 — unknown\\\\n- exp_006_irt_05B_v1: 训练失败 — unknown\\\\n- exp_006_j16_theta_extraction: 训练失败 — unknown\\\\n- exp_006_mmlu_domain_gamma_n24_v2: 训练失败 — unknown\\\\n- exp_006_mmlu_domain_gamma_n24_v3: 训练失败 — unknown\\\\n- exp_006_pooled_gsm8k_v1: 训练失败 — unknown\\\\n- exp_006_theta_extraction_j13: 训练失败 — unknown\\\\n- exp_008_base_pretrained_eval: 训练失败 — unknown\\\\n- exp_008_instruct_rl_proxy: 训练失败 — unknown\\\\n- gsm8k_gemma2_s42_westd: 训练失败 — unknown\\\\n- retrain_gemma2_d100_s123: 已被终止 — unknown\\\\n- retrain_qwen14b_d100_s123: 已被终止 — unknown\\\\n- sft_gemma2_s123_sweep: 训练失败 — unknown\\\\n- sft_qwen14b_s123_sweep: 训练失败 — unknown\\\\n- sft_falcon3_7b_d000_s42: 训练失败 — unknown\\\\n- sft_falcon3_7b_d005_s42: 训练失败 — unknown\\\\n- sft_falcon3_7b_d025_s42: 训练失败 — unknown\\\\n- sft_falcon3_7b_d050_s42: 训练失败 — unknown\\\\n- eval_falcon3_d000_s42: 训练失败 — unknown\\\\n- eval_falcon3_d005_s42: 训练失败 — unknown\\\\n- eval_falcon3_d025_s42: 训练失败 — unknown\\\\n\\\", \\\"total_chars\\\": 7723, \\\"truncated\\\": false}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/report.md\", \"content\": \"&lt;!-- AUTO-FACTS-BEGIN (generated 2026-05-22T11:07:28Z; do not edit — regenerated by auto_build_report_facts) -->\\n## 📊 当前状态（auto-derived from registry）\\n\\n**总计**: 406 个实验 — DONE 360, PREPARING 42, QUEUED 2, RUNNING 2\\n**DONE 分布**: failed 65, killed 16, negative 10, success 269\\n\\n### GPU 占用\\n- **分配**: 2 张 — cqa1-21977:cuda:0, westd-29999:cuda:0\\n- **实际运行**: 2 张 — cqa1-21977:cuda:0(sft_falcon3_7b_d100_s42), westd-29999:cuda:3(sft_falcon3_7b_d050_s42_v2)\\n- **空闲（分配了没跑）**: westd-29999:cuda:0\\n\\n### 💾 磁盘余量\\n- **cqa1-21977**:\\n  - `/autodl-pub`: 360G/7.0T 可用（已用 95%） ⚠️\\n  - `/autodl-pub/data`: 1.5T/4.0T 可用（已用 65%）\\n  - `/usr/bin/nvidia-smi`: 818G/879G 可用（已用 2%）\\n- **westd-29999**:\\n  - `/autodl-pub`: 5.3T/7.3T 可用（已用 24%）\\n  - `/init`: 150M/150M 可用（已用 0%）\\n  - `/usr/bin/nvidia-smi`: 427G/879G 可用（已用 49%）\\n\\n### 🏃 RUNNING\\n| exp_id | server | gpu | pid | log |\\n|--------|--------|-----|-----|-----|\\n| `sft_falcon3_7b_d100_s42` | cqa1-21977 | cuda:0 | 666107 | `—` |\\n| `sft_falcon3_7b_d050_s42_v2` | westd-29999 | cuda:3 | 600596 | `…ns/contamcal-irt-calibration/sft_falcon3_7b_d050_s42_v2.log` |\\n\\n### 📌 最近完成 (top 5)\\n- `eval_falcon3_d025_s42` [failed] — 2026-05-22T11:07:23 — EXIT_CODE=1 (generic error — check log tail)\\n- `eval_falcon3_d005_s42` [failed] — 2026-05-22T11:07:03 — EXIT_CODE=1 (generic error — check log tail)\\n- `eval_falcon3_d000_s42` [failed] — 2026-05-22T11:06:44 — EXIT_CODE=1 (generic error — check log tail)\\n- `sft_falcon3_7b_d025_s42_v2` [success] — 2026-05-22T11:06:26\\n- `sft_falcon3_7b_d005_s42_v2` [success] — 2026-05-22T11:06:25\\n\\n### 🔴 最近失败原因 (top 3)\\n- `eval_falcon3_d025_s42`: EXIT_CODE=1 (generic error — check log tail)\\n- `eval_falcon3_d005_s42`: EXIT_CODE=1 (generic error — check log tail)\\n- `eval_falcon3_d000_s42`: EXIT_CODE=1 (generic error — check log tail)\\n\\n&lt;!-- AUTO-FACTS-END -->\\n\\n---\\n\\n# Handover — 2026-05-22\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\\n|--------|------|------|---------|-----|\\n| sft_falcon3_7b_d100_s42 | Cross-family replication: Falcon3-7B-Base at 100% contamination dosage. Maximum dosage determines final pattern classification (Immune/Collapse/V-recovery/Benefit) and Δ(d100-d000) magnitude for a non-Qwen family in the vulnerability band. | — | — | — |\\n| sft_falcon3_7b_d050_s42_v2 | Cross-family replication: Falcon3-7B-Base at 50% contamination dosage. Higher dosage reveals whether pattern intensifies monotonically or saturates. LR bug fix retry with correct lr=5e-5. | — | — | — |\\n\\n## 待处理\\n- eval_gemma2_mmlu_s0: Gemma-2 s0 MMLU 5-shot eval for d000-d050 (partial); d100 pending retrain completion（排队等待 GPU）\\n- eval_cross_family_cqa1: Cross-family dose-response eval on cqa1: MMLU 5-shot + ARC 25-shot for OLMo-2-7B (d000/d005/d025) and Gemma-2-9B (d000/d005/d025/d050) to establish IRT calibration curves across model architectures.（排队等待 GPU）\\n- falcon3-7b-dl-v5（准备中）\\n- falcon3-7b-dl-v4（准备中）\\n- falcon3-7b-dl-v3（准备中）\\n- falcon3-7b-dl-v2（准备中）\\n- falcon3-7b-download（准备中）\\n- prior_sensitivity_j16_v2（准备中）\\n- prior_sensitivity_j16（准备中）\\n- sft_llama3_8b_s0_validation: Out-of-sample taxonomy validation: LLaMA-3.1-8B (base) as 6th family. 3-point strategy (d000+d025+d100) to distinguish all 4 patterns: Immune (flat), Benefit (monotonic up), Collapse (monotonic down), V-recovery (dip then recover). Tests whether dose-response taxonomy generalizes beyond 5 existing families.（准备中）\\n- …另有 34 项\\n\\n## 近期结论\\n- **eval_falcon3_d025_s42** (failed): Falcon3-7B-Base d025 eval: MMLU 5-shot + ARC 25-shot aligned MC format for dose-response profiling\\n- **eval_falcon3_d005_s42** (failed): Falcon3-7B-Base d005 eval: MMLU 5-shot + ARC 25-shot aligned MC format for dose-response profiling\\n- **eval_falcon3_d000_s42** (failed): Falcon3-7B-Base d000 eval: MMLU 5-shot + ARC 25-shot aligned MC format for dose-response profiling\\n\\n## 趋势\\n成功 271 / 负向 10 / 失败 70 / 共 367\\n\\n## 下一步\\n（无活跃 idea，请通过 ideas.md 添加）\\n\\n## 资源状态\\ncqa1-21977: 无 GPU 信息\\nwestd-29999: 无 GPU 信息\\n\\n## 告警\\n- eval_14b_mmlu_arc_westd: 训练失败 — unknown\\n- eval_7b_batch1_westd: 训练失败 — unknown\\n- eval_7b_batch_cqa1: 已被终止 — unknown\\n- eval_phi4_mmlu_arc_westd: 训练失败 — unknown\\n- eval_qwen7b_s123_cqa1: 训练失败 — unknown\\n- exp006-oracle-arc-4pl-pooled: 训练失败 — unknown\\n- exp006-oracle-gsm8k-extended: 训练失败 — unknown\\n- exp006-pooled-05B-15B-mmlu-v2: 训练失败 — unknown\\n- exp006-pooled-s1only-gsm8k: 训练失败 — unknown\\n- exp_001_eval_05B_aligned_batch: 训练失败 — unknown\\n- exp_001_eval_05B_d000_s42: 训练失败 — unknown\\n- exp_001_eval_05B_d000_s42_v7: 训练失败 — unknown\\n- exp_001_eval_05B_d100: 训练失败 — unknown\\n- exp_001_eval_05B_d100_aligned: 训练失败 — unknown\\n- exp_001_eval_05B_d100_aligned_v3: 训练失败 — unknown\\n- exp_001_eval_05B_d100_v2: 训练失败 — unknown\\n- exp_001_eval_15B_d000_s42: 训练失败 — unknown\\n- exp_001_eval_3B_d000_v2_para_aligned_v3: 训练失败 — unknown\\n- exp_001_eval_3B_d025_v3_s42_batch: 已被终止 — unknown\\n- exp_001_eval_3B_d100_s123_para_aligned: 训练失败 — unknown\\n- exp_001_eval_3B_d100_v2_aligned: 训练失败 — unknown\\n- exp_001_eval_3B_instruct_aligned_para: 训练失败 — unknown\\n- exp_001_eval_llama32_3B_d000_s42: 已被终止 — unknown\\n- exp_001_sft_05B_d025_s123: 已被终止 — unknown\\n- exp_001_sft_100pct_05B: 训练失败 — unknown\\n- exp_001_sft_15B_d005_s123: 训练失败 — unknown\\n- exp_001_sft_3B_d000_v3: 训练失败 — unknown\\n- exp_001_sft_3B_d025_s42_a32: 已被终止 — unknown\\n- exp_001_sft_3B_d025_s42_a32_v2: 训练失败 — unknown\\n- exp_001_sft_3B_d025_s42_a32_v3: 已被终止 — unknown\\n- exp_001_sft_3B_d100_s42_a32: 已被终止 — unknown\\n- exp_001_sft_3B_d100_s42_a32_v2: 训练失败 — unknown\\n- exp_001_sft_d005_05B: 已被终止 — unknown\\n- exp_001_sft_d005_05B_v2: 训练失败 — unknown\\n- exp_001_sft_d025_05B: 训练失败 — unknown\\n- exp_001_sft_d025_05B_v2: 训练失败 — unknown\\n- exp_001_sft_d025_3B: 训练失败 — unknown\\n- exp_001_sft_d100_15B: 训练失败 — unknown\\n- exp_001_sft_olmo2_7b_d005_s42: 已被终止 — unknown\\n- exp_002_signals_05B_s123_batch: 训练失败 — unknown\\n- exp_002_signals_15B_instruct_gsm8k: 训练失败 — unknown\\n- exp_002_signals_3B: 训练失败 — unknown\\n- exp_002_signals_3B_d000_s123_cuda2: 训练失败 — unknown\\n- exp_002_signals_3B_v2: 已被终止 — unknown\\n- exp_002_signals_3B_v3: 已被终止 — unknown\\n- exp_002_signals_3B_v4: 训练失败 — unknown\\n- exp_002_signals_3B_v5: 训练失败 — unknown\\n- exp_002_signals_3B_v6: 训练失败 — unknown\\n- exp_002_signals_3B_v8: 训练失败 — unknown\\n- exp_002_signals_3B_v8_recovery: 训练失败 — unknown\\n- exp_002_signals_3B_v9: 训练失败 — unknown\\n- exp_002_signals_llama32_3B_d000_gsm8k: 训练失败 — unknown\\n- exp_002_signals_llama32_3B_d025_mmlu_arc_gsm8k: 训练失败 — unknown\\n- exp_002_signals_llama32_3B_d100_mmlu: 已被终止 — unknown\\n- exp_004_fisher_heatmap_w4: 训练失败 — unknown\\n- exp_004_sim_sweep: 训练失败 — unknown\\n- exp_004_sim_sweep_v2: 训练失败 — unknown\\n- exp_004_sim_sweep_v3: 训练失败 — unknown\\n- exp_004_sim_sweep_v4: 训练失败 — unknown\\n- exp_004_sim_sweep_v5: 训练失败 — unknown\\n- exp_004_sim_sweep_v6: 已被终止 — unknown\\n- exp_005_noise_prop: 训练失败 — unknown\\n- exp_005_noise_prop_v2: 训练失败 — unknown\\n- exp_005_noise_prop_v3: 训练失败 — unknown\\n- exp_006_cross_family_irt_j16: 训练失败 — unknown\\n- exp_006_irt_05B: 已被终止 — unknown\\n- exp_006_irt_05B_v1: 训练失败 — unknown\\n- exp_006_j16_theta_extraction: 训练失败 — unknown\\n- exp_006_mmlu_domain_gamma_n24_v2: 训练失败 — unknown\\n- exp_006_mmlu_domain_gamma_n24_v3: 训练失败 — unknown\\n- exp_006_pooled_gsm8k_v1: 训练失败 — unknown\\n- exp_006_theta_extraction_j13: 训练失败 — unknown\\n- exp_008_base_pretrained_eval: 训练失败 — unknown\\n- exp_008_instruct_rl_proxy: 训练失败 — unknown\\n- gsm8k_gemma2_s42_westd: 训练失败 — unknown\\n- retrain_gemma2_d100_s123: 已被终止 — unknown\\n- retrain_qwen14b_d100_s123: 已被终止 — unknown\\n- sft_gemma2_s123_sweep: 训练失败 — unknown\\n- sft_qwen14b_s123_sweep: 训练失败 — unknown\\n- sft_falcon3_7b_d000_s42: 训练失败 — unknown\\n- sft_falcon3_7b_d005_s42: 训练失败 — unknown\\n- sft_falcon3_7b_d025_s42: 训练失败 — unknown\\n- sft_falcon3_7b_d050_s42: 训练失败 — unknown\\n- eval_falcon3_d000_s42: 训练失败 — unknown\\n- eval_falcon3_d005_s42: 训练失败 — unknown\\n- eval_falcon3_d025_s42: 训练失败 — unknown\\n\", \"total_chars\": 7723, \"truncated\": false}, \"error\": null, \"metadata\": {}}"
    }
  },
  "sourceToolAssistantUUID": "982160f5-3750-4799-83ef-c0779a74f356",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_5ae72916",
  "sessionId": "ecab2a37-b09b-48e2-a661-0d7a5b7a31ca",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-22T11:07:49.601Z_

<details><summary>↩ Tool result · `toolu_01Y4SYxhbfhcN32XrtSaqRoT`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/ROADMAP.md\", \"content\": \"# contamcal-irt-calibration — Research Dashboard\\n\\n> 最后更新: 2026-05-21 20:01 UTC | 更新原因: D213+D214 全部完成，终稿就绪待用户决策\\n\\n> 目标: EMNLP 2026 ARR May 25 | **D+4**\\n\\n## 核心方向\\nSFT-route benchmark contamination 产生 family-dependent dose-response profiles。**4-pattern empirical taxonomy**: Immune / Collapse / V-recovery / Benefit。详见 paper_framing.md。\\n\\n## 当前状态\\n- **Round 10 (3.0 Findings) Action Matrix D213+D214 全部执行完毕**\\n- 3 Must-Fix ✅: P(γ<0) 数值修正 (Table 10 模型池 bug fix + exploratory framing)、taxonomy→profiles、OOS limitation\\n- 7 Should-Fix ✅: AUGMENT volume confound、γ parameterization 论证、MMLU PPP、novelty positioning、Han/Schaeffer 三方对比、LoRA 参数百分比 (0.45-0.59%)、300-item caveat\\n- D214: Prior sensitivity j16_qwen 重跑——tight prior 99.35% (差 Bonferroni 0.03pp)，baseline 99.68%，loose 99.85%。→ exploratory framing\\n- 编译通过: 19 页 (main text 8 页), 0 critical warnings\\n\\n## 终稿就绪\\n- [x] Round 9 Action Matrix (D211) — 全部 resolved\\n- [x] Round 10 Action Matrix (D213) — 全部 resolved\\n- [x] D214 MF-1 P(γ<0) 修正 — Table 10 corrected + exploratory framing\\n- [x] 编译验证 ≤ 8 页 main text\\n- [ ] **用户决策：提交 ARR 或再做一轮内审**\\n\\n## Taxonomy (6 families)\\nImmune ×2 (Phi-4, LLaMA-3) | Collapse ×1 (Qwen-14B) | V-recovery ×1 (Qwen-7B) | Benefit ×2 (Gemma-2, OLMo-2)\\n\\n## GPU 预算\\n- westd: 4× RTX PRO 6000 Blackwell — 全部空闲\\n- cqa1: 1× RTX 4090 D — 空闲\\n\\n## 关键决策日志\\n\\n| ID | 日期 | 摘要 | 关联实验 |\\n|----|------|------|----------|\\n| D215 | 2026-05-22 | Falcon3 结果判断标准：任何结果均直接提交 ARR，不再加内审轮次 | sft_falcon3_7b_d000_s42, sft_falcon3_7b_d100_s42 |\\n| D214 | 2026-05-21 | D214: P(γ<0) 差异根因=不同模型池。Option A: j16_qwen 池重跑 pri | — |\\n| D213 | 2026-05-21 | D213: Round 10 (3.0 Findings) Action Matrix — P(γ< | — |\\n| D212 | 2026-05-21 | D212: 参数化 DR 拟合 1/5 一致——framing 为 n=3 统计力限制而非 Algo | — |\\n| D211 | 2026-05-21 | D211: Round 9 (3.5 Borderline Conference) Action M | — |\\n| D210 | 2026-05-21 | D210: OLMo-2 d000 s42 MMLU 53.79% 全量重跑验证通过——论文数据正确 | eval_olmo2_s42_rerun |\\n| D209 | 2026-05-21 | D209: OLMo-2 d000 基线 53.79% 存疑——启动全量重跑 eval 以确认 gr | eval_olmo2_d000_s42_rerun |\\n| D208 | 2026-05-21 | D208: W8 skewed exposure sim 跳过，Limitations 加 unif | — |\\n| D207 | 2026-05-21 | LLaMA-3.1-8B out-of-sample 验证 = Immune，W3 Critical | sft_llama3_d000_s0, sft_llama3_d025_s0, sft_llama3_d100_s0 |\\n| D206 | 2026-05-21 | GSM8K appendix 全部统一 s0 数据（37775版本）+ 强 caveat，不做跨家族 | gsm8k_appendix |\\n\\n\", \"lines\": 46}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9e2e0a2c-10b4-49c7-b32e-2fbba607805a",
  "isSidechain": false,
  "promptId": "9e81e78d-88e1-48cf-a480-c0cfdcf0974a",
  "type": "user",
  "uuid": "da390aed-53d1-4e94-8877-1478d7e66d0d",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/ROADMAP.md\\\", \\\"content\\\": \\\"# contamcal-irt-calibration — Research Dashboard\\\\n\\\\n> 最后更新: 2026-05-21 20:01 UTC | 更新原因: D213+D214 全部完成，终稿就绪待用户决策\\\\n\\\\n> 目标: EMNLP 2026 ARR May 25 | **D+4**\\\\n\\\\n## 核心方向\\\\nSFT-route benchmark contamination 产生 family-dependent dose-response profiles。**4-pattern empirical taxonomy**: Immune / Collapse / V-recovery / Benefit。详见 paper_framing.md。\\\\n\\\\n## 当前状态\\\\n- **Round 10 (3.0 Findings) Action Matrix D213+D214 全部执行完毕**\\\\n- 3 Must-Fix ✅: P(γ<0) 数值修正 (Table 10 模型池 bug fix + exploratory framing)、taxonomy→profiles、OOS limitation\\\\n- 7 Should-Fix ✅: AUGMENT volume confound、γ parameterization 论证、MMLU PPP、novelty positioning、Han/Schaeffer 三方对比、LoRA 参数百分比 (0.45-0.59%)、300-item caveat\\\\n- D214: Prior sensitivity j16_qwen 重跑——tight prior 99.35% (差 Bonferroni 0.03pp)，baseline 99.68%，loose 99.85%。→ exploratory framing\\\\n- 编译通过: 19 页 (main text 8 页), 0 critical warnings\\\\n\\\\n## 终稿就绪\\\\n- [x] Round 9 Action Matrix (D211) — 全部 resolved\\\\n- [x] Round 10 Action Matrix (D213) — 全部 resolved\\\\n- [x] D214 MF-1 P(γ<0) 修正 — Table 10 corrected + exploratory framing\\\\n- [x] 编译验证 ≤ 8 页 main text\\\\n- [ ] **用户决策：提交 ARR 或再做一轮内审**\\\\n\\\\n## Taxonomy (6 families)\\\\nImmune ×2 (Phi-4, LLaMA-3) | Collapse ×1 (Qwen-14B) | V-recovery ×1 (Qwen-7B) | Benefit ×2 (Gemma-2, OLMo-2)\\\\n\\\\n## GPU 预算\\\\n- westd: 4× RTX PRO 6000 Blackwell — 全部空闲\\\\n- cqa1: 1× RTX 4090 D — 空闲\\\\n\\\\n## 关键决策日志\\\\n\\\\n| ID | 日期 | 摘要 | 关联实验 |\\\\n|----|------|------|----------|\\\\n| D215 | 2026-05-22 | Falcon3 结果判断标准：任何结果均直接提交 ARR，不再加内审轮次 | sft_falcon3_7b_d000_s42, sft_falcon3_7b_d100_s42 |\\\\n| D214 | 2026-05-21 | D214: P(γ<0) 差异根因=不同模型池。Option A: j16_qwen 池重跑 pri | — |\\\\n| D213 | 2026-05-21 | D213: Round 10 (3.0 Findings) Action Matrix — P(γ< | — |\\\\n| D212 | 2026-05-21 | D212: 参数化 DR 拟合 1/5 一致——framing 为 n=3 统计力限制而非 Algo | — |\\\\n| D211 | 2026-05-21 | D211: Round 9 (3.5 Borderline Conference) Action M | — |\\\\n| D210 | 2026-05-21 | D210: OLMo-2 d000 s42 MMLU 53.79% 全量重跑验证通过——论文数据正确 | eval_olmo2_s42_rerun |\\\\n| D209 | 2026-05-21 | D209: OLMo-2 d000 基线 53.79% 存疑——启动全量重跑 eval 以确认 gr | eval_olmo2_d000_s42_rerun |\\\\n| D208 | 2026-05-21 | D208: W8 skewed exposure sim 跳过，Limitations 加 unif | — |\\\\n| D207 | 2026-05-21 | LLaMA-3.1-8B out-of-sample 验证 = Immune，W3 Critical | sft_llama3_d000_s0, sft_llama3_d025_s0, sft_llama3_d100_s0 |\\\\n| D206 | 2026-05-21 | GSM8K appendix 全部统一 s0 数据（37775版本）+ 强 caveat，不做跨家族 | gsm8k_appendix |\\\\n\\\\n\\\", \\\"lines\\\": 46}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/ROADMAP.md\", \"content\": \"# contamcal-irt-calibration — Research Dashboard\\n\\n> 最后更新: 2026-05-21 20:01 UTC | 更新原因: D213+D214 全部完成，终稿就绪待用户决策\\n\\n> 目标: EMNLP 2026 ARR May 25 | **D+4**\\n\\n## 核心方向\\nSFT-route benchmark contamination 产生 family-dependent dose-response profiles。**4-pattern empirical taxonomy**: Immune / Collapse / V-recovery / Benefit。详见 paper_framing.md。\\n\\n## 当前状态\\n- **Round 10 (3.0 Findings) Action Matrix D213+D214 全部执行完毕**\\n- 3 Must-Fix ✅: P(γ<0) 数值修正 (Table 10 模型池 bug fix + exploratory framing)、taxonomy→profiles、OOS limitation\\n- 7 Should-Fix ✅: AUGMENT volume confound、γ parameterization 论证、MMLU PPP、novelty positioning、Han/Schaeffer 三方对比、LoRA 参数百分比 (0.45-0.59%)、300-item caveat\\n- D214: Prior sensitivity j16_qwen 重跑——tight prior 99.35% (差 Bonferroni 0.03pp)，baseline 99.68%，loose 99.85%。→ exploratory framing\\n- 编译通过: 19 页 (main text 8 页), 0 critical warnings\\n\\n## 终稿就绪\\n- [x] Round 9 Action Matrix (D211) — 全部 resolved\\n- [x] Round 10 Action Matrix (D213) — 全部 resolved\\n- [x] D214 MF-1 P(γ<0) 修正 — Table 10 corrected + exploratory framing\\n- [x] 编译验证 ≤ 8 页 main text\\n- [ ] **用户决策：提交 ARR 或再做一轮内审**\\n\\n## Taxonomy (6 families)\\nImmune ×2 (Phi-4, LLaMA-3) | Collapse ×1 (Qwen-14B) | V-recovery ×1 (Qwen-7B) | Benefit ×2 (Gemma-2, OLMo-2)\\n\\n## GPU 预算\\n- westd: 4× RTX PRO 6000 Blackwell — 全部空闲\\n- cqa1: 1× RTX 4090 D — 空闲\\n\\n## 关键决策日志\\n\\n| ID | 日期 | 摘要 | 关联实验 |\\n|----|------|------|----------|\\n| D215 | 2026-05-22 | Falcon3 结果判断标准：任何结果均直接提交 ARR，不再加内审轮次 | sft_falcon3_7b_d000_s42, sft_falcon3_7b_d100_s42 |\\n| D214 | 2026-05-21 | D214: P(γ<0) 差异根因=不同模型池。Option A: j16_qwen 池重跑 pri | — |\\n| D213 | 2026-05-21 | D213: Round 10 (3.0 Findings) Action Matrix — P(γ< | — |\\n| D212 | 2026-05-21 | D212: 参数化 DR 拟合 1/5 一致——framing 为 n=3 统计力限制而非 Algo | — |\\n| D211 | 2026-05-21 | D211: Round 9 (3.5 Borderline Conference) Action M | — |\\n| D210 | 2026-05-21 | D210: OLMo-2 d000 s42 MMLU 53.79% 全量重跑验证通过——论文数据正确 | eval_olmo2_s42_rerun |\\n| D209 | 2026-05-21 | D209: OLMo-2 d000 基线 53.79% 存疑——启动全量重跑 eval 以确认 gr | eval_olmo2_d000_s42_rerun |\\n| D208 | 2026-05-21 | D208: W8 skewed exposure sim 跳过，Limitations 加 unif | — |\\n| D207 | 2026-05-21 | LLaMA-3.1-8B out-of-sample 验证 = Immune，W3 Critical | sft_llama3_d000_s0, sft_llama3_d025_s0, sft_llama3_d100_s0 |\\n| D206 | 2026-05-21 | GSM8K appendix 全部统一 s0 数据（37775版本）+ 强 caveat，不做跨家族 | gsm8k_appendix |\\n\\n\", \"lines\": 46}, \"error\": null, \"metadata\": {}}"
    }
  },
  "sourceToolAssistantUUID": "9e2e0a2c-10b4-49c7-b32e-2fbba607805a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_5ae72916",
  "sessionId": "ecab2a37-b09b-48e2-a661-0d7a5b7a31ca",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 22_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[CRON] 实验进程异常退出（失败），需要你诊断原因。 详情: Process exited without valid W&B metrics  - exp_id: eval_falcon3_d025_s42 - project: contamcal-irt-calibration - server: westd-29999",
  "leafUuid": "da390aed-53d1-4e94-8877-1478d7e66d0d",
  "sessionId": "ecab2a37-b09b-48e2-a661-0d7a5b7a31ca"
}
```

---

### Runtime record

_source line 23_

```json
{
  "type": "ai-title",
  "aiTitle": "Diagnose W&B metrics missing in Falcon3 experiment",
  "sessionId": "ecab2a37-b09b-48e2-a661-0d7a5b7a31ca"
}
```

---

### Assistant

_source line 24 · 2026-05-22T11:08:05.828Z_

<details><summary>Logged reasoning block</summary>

```text
Let me understand the situation:

1. **Reconcile crons**: Only `sft_falcon3_7b_d100_s42` is still running (pid=666107 on cqa1-21977). 
2. **Report.md**: Shows 3 eval experiments just failed: `eval_falcon3_d025_s42`, `eval_falcon3_d005_s42`, `eval_falcon3_d000_s42` — all with EXIT_CODE=1.
3. **ROADMAP**: The project is near EMNLP 2026 ARR submission (May 25). 

The Falcon3 experiments are active, and according to D215, all results should be submitted directly to ARR without additional review rounds. Since the cron triggered `eval_falcon3_d025_s42`, I need to pull the experiment details from the registry and check the on-experiment-failed handler, then spawn a worker to diagnose what went wrong by examining the logs on westd-29999.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "da390aed-53d1-4e94-8877-1478d7e66d0d",
  "isSidechain": false,
  "requestId": "req_011CbHW2y8co5LaM7AEf3HFW",
  "type": "assistant",
  "uuid": "c99b273a-0b67-41ca-a681-25809f232f61",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_5ae72916",
  "sessionId": "ecab2a37-b09b-48e2-a661-0d7a5b7a31ca",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QTxRf6A1acRHhMKVP5N2GK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6727,
      "cache_read_input_tokens": 38297,
      "output_tokens": 759,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6727,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 759,
          "cache_read_input_tokens": 38297,
          "cache_creation_input_tokens": 6727,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6727
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

_source line 25 · 2026-05-22T11:08:06.571Z_

三个 Falcon3 eval 实验同时失败（d000/d005/d025），说明是系统性问题。让我查实验详情并读取失败诊断 skill。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c99b273a-0b67-41ca-a681-25809f232f61",
  "isSidechain": false,
  "requestId": "req_011CbHW2y8co5LaM7AEf3HFW",
  "type": "assistant",
  "uuid": "43f79ac5-529b-4065-acbe-5fc035096e44",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_5ae72916",
  "sessionId": "ecab2a37-b09b-48e2-a661-0d7a5b7a31ca",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QTxRf6A1acRHhMKVP5N2GK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6727,
      "cache_read_input_tokens": 38297,
      "output_tokens": 759,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6727,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 759,
          "cache_read_input_tokens": 38297,
          "cache_creation_input_tokens": 6727,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6727
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

_source line 26 · 2026-05-22T11:08:07.437Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01EpQmDHKu13FVc2tFqguQ9u`</summary>

```json
{
  "project": "contamcal-irt-calibration",
  "filters": {
    "exp_id": "eval_falcon3_d025_s42"
  },
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
  "parentUuid": "43f79ac5-529b-4065-acbe-5fc035096e44",
  "isSidechain": false,
  "requestId": "req_011CbHW2y8co5LaM7AEf3HFW",
  "type": "assistant",
  "uuid": "845281f4-8086-43c4-b13f-1707be9a3b45",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_5ae72916",
  "sessionId": "ecab2a37-b09b-48e2-a661-0d7a5b7a31ca",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QTxRf6A1acRHhMKVP5N2GK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6727,
      "cache_read_input_tokens": 38297,
      "output_tokens": 759,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6727,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 759,
          "cache_read_input_tokens": 38297,
          "cache_creation_input_tokens": 6727,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6727
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

_source line 27 · 2026-05-22T11:08:08.455Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01TrmuF66YxahNM9e5R9Tu7f`</summary>

```json
{
  "project": "contamcal-irt-calibration",
  "filters": {
    "exp_id": "eval_falcon3_d005_s42"
  },
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
  "parentUuid": "845281f4-8086-43c4-b13f-1707be9a3b45",
  "isSidechain": false,
  "requestId": "req_011CbHW2y8co5LaM7AEf3HFW",
  "type": "assistant",
  "uuid": "d1fc0812-569a-48c1-b233-c1b774a77a65",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_5ae72916",
  "sessionId": "ecab2a37-b09b-48e2-a661-0d7a5b7a31ca",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QTxRf6A1acRHhMKVP5N2GK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6727,
      "cache_read_input_tokens": 38297,
      "output_tokens": 759,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6727,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 759,
          "cache_read_input_tokens": 38297,
          "cache_creation_input_tokens": 6727,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6727
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

_source line 28 · 2026-05-22T11:08:09.511Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_019qWgiM7MDUYq999BvwNv8g`</summary>

```json
{
  "project": "contamcal-irt-calibration",
  "filters": {
    "exp_id": "eval_falcon3_d000_s42"
  },
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
  "parentUuid": "d1fc0812-569a-48c1-b233-c1b774a77a65",
  "isSidechain": false,
  "requestId": "req_011CbHW2y8co5LaM7AEf3HFW",
  "type": "assistant",
  "uuid": "8c1a0a44-be38-4140-ae16-a527c210b610",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_5ae72916",
  "sessionId": "ecab2a37-b09b-48e2-a661-0d7a5b7a31ca",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QTxRf6A1acRHhMKVP5N2GK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6727,
      "cache_read_input_tokens": 38297,
      "output_tokens": 759,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6727,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 759,
          "cache_read_input_tokens": 38297,
          "cache_creation_input_tokens": 6727,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6727
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

_source line 29 · 2026-05-22T11:08:09.929Z_

<details><summary>↩ Tool result · `toolu_01EpQmDHKu13FVc2tFqguQ9u`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.4575}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "845281f4-8086-43c4-b13f-1707be9a3b45",
  "isSidechain": false,
  "promptId": "9e81e78d-88e1-48cf-a480-c0cfdcf0974a",
  "type": "user",
  "uuid": "db2fb3f9-245b-48e8-93bd-420f16aaacd9",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {}, \\\"count\\\": 0, \\\"total\\\": 0, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 2.4575}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.4575}}"
    }
  },
  "sourceToolAssistantUUID": "845281f4-8086-43c4-b13f-1707be9a3b45",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_5ae72916",
  "sessionId": "ecab2a37-b09b-48e2-a661-0d7a5b7a31ca",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-22T11:08:10.855Z_

<details open><summary>🔧 Tool call — Read · `toolu_019KCRtncGwYy7epNEZttAom`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/skills/on-experiment-failed.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "db2fb3f9-245b-48e8-93bd-420f16aaacd9",
  "isSidechain": false,
  "requestId": "req_011CbHW2y8co5LaM7AEf3HFW",
  "type": "assistant",
  "uuid": "0ee6077f-05f9-49d1-8f76-bbe42152973f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_5ae72916",
  "sessionId": "ecab2a37-b09b-48e2-a661-0d7a5b7a31ca",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QTxRf6A1acRHhMKVP5N2GK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6727,
      "cache_read_input_tokens": 38297,
      "output_tokens": 759,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6727,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 759,
          "cache_read_input_tokens": 38297,
          "cache_creation_input_tokens": 6727,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6727
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

_source line 31 · 2026-05-22T11:08:11.938Z_

<details><summary>↩ Tool result · `toolu_01TrmuF66YxahNM9e5R9Tu7f`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.9928}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d1fc0812-569a-48c1-b233-c1b774a77a65",
  "isSidechain": false,
  "promptId": "9e81e78d-88e1-48cf-a480-c0cfdcf0974a",
  "type": "user",
  "uuid": "1b73f0ee-705d-4838-ac9f-1904bf5e3e08",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {}, \\\"count\\\": 0, \\\"total\\\": 0, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 1.9928}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.9928}}"
    }
  },
  "sourceToolAssistantUUID": "d1fc0812-569a-48c1-b233-c1b774a77a65",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_5ae72916",
  "sessionId": "ecab2a37-b09b-48e2-a661-0d7a5b7a31ca",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-22T11:08:13.350Z_

<details><summary>↩ Tool result · `toolu_019qWgiM7MDUYq999BvwNv8g`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.3896}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8c1a0a44-be38-4140-ae16-a527c210b610",
  "isSidechain": false,
  "promptId": "9e81e78d-88e1-48cf-a480-c0cfdcf0974a",
  "type": "user",
  "uuid": "5c5e32dc-1eb1-4c7c-9466-985da7557cd5",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {}, \\\"count\\\": 0, \\\"total\\\": 0, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 1.3896}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.3896}}"
    }
  },
  "sourceToolAssistantUUID": "8c1a0a44-be38-4140-ae16-a527c210b610",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_5ae72916",
  "sessionId": "ecab2a37-b09b-48e2-a661-0d7a5b7a31ca",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-22T11:08:13.362Z_

<details><summary>↩ Tool result · reported error · `toolu_019KCRtncGwYy7epNEZttAom`</summary>

```text
File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_5ae72916.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0ee6077f-05f9-49d1-8f76-bbe42152973f",
  "isSidechain": false,
  "promptId": "9e81e78d-88e1-48cf-a480-c0cfdcf0974a",
  "type": "user",
  "uuid": "88064464-fa4a-46c8-ad26-734690651c37",
  "toolUseResult": "Error: File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_5ae72916.",
  "sourceToolAssistantUUID": "0ee6077f-05f9-49d1-8f76-bbe42152973f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_5ae72916",
  "sessionId": "ecab2a37-b09b-48e2-a661-0d7a5b7a31ca",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 34 · 2026-05-22T11:08:13.365Z_

```json
{
  "parentUuid": "88064464-fa4a-46c8-ad26-734690651c37",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "60f3c5d2-4fdb-4841-8c52-10b1f3fe8294",
  "timestamp": "2026-05-22T11:08:13.365Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_5ae72916",
  "sessionId": "ecab2a37-b09b-48e2-a661-0d7a5b7a31ca",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 35 · 2026-05-22T11:08:17.582Z_

<details><summary>Logged reasoning block</summary>

```text
The registry filter by exp_id returned empty. Let me try different approach - maybe the field name is different, or I need to search the saved registry file. Also the skill path might be different. Let me search for the skill and also try querying the registry differently.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "60f3c5d2-4fdb-4841-8c52-10b1f3fe8294",
  "isSidechain": false,
  "requestId": "req_011CbHW4igmZcRPujm2UQqXQ",
  "type": "assistant",
  "uuid": "bb8b655a-8844-45e0-ae66-917f93e6e9a6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_5ae72916",
  "sessionId": "ecab2a37-b09b-48e2-a661-0d7a5b7a31ca",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P26CVXvsLDj7MT6rygE2xg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1249,
      "cache_read_input_tokens": 45024,
      "output_tokens": 559,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1249,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 559,
          "cache_read_input_tokens": 45024,
          "cache_creation_input_tokens": 1249,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1249
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

_source line 36 · 2026-05-22T11:08:19.037Z_

Registry 过滤返回空，可能字段名不同。让我直接从保存的 registry 文件提取这些实验信息，同时找到正确的 skill 路径。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bb8b655a-8844-45e0-ae66-917f93e6e9a6",
  "isSidechain": false,
  "requestId": "req_011CbHW4igmZcRPujm2UQqXQ",
  "type": "assistant",
  "uuid": "491adb13-5152-44de-9c8a-8fb7b16c30c8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_5ae72916",
  "sessionId": "ecab2a37-b09b-48e2-a661-0d7a5b7a31ca",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P26CVXvsLDj7MT6rygE2xg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1249,
      "cache_read_input_tokens": 45024,
      "output_tokens": 559,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1249,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 559,
          "cache_read_input_tokens": 45024,
          "cache_creation_input_tokens": 1249,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1249
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

_source line 37 · 2026-05-22T11:08:25.274Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01Wd9fWZWDuWgLYrgYP1hCDy`</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration--claude-sessions-agent-5ae72916/ecab2a37-b09b-48e2-a661-0d7a5b7a31ca/tool-results/mcp-agent-ml-research-read_registry-1779448066186.txt | python3 -c \"\nimport json, sys\ndata = json.load(sys.stdin)\nresult = json.loads(data['result'])\nexperiments = result['data']['experiments']\ntargets = ['eval_falcon3_d025_s42', 'eval_falcon3_d005_s42', 'eval_falcon3_d000_s42']\nfor t in targets:\n    if t in experiments:\n        exp = experiments[t]\n        print(f'=== {t} ===')\n        print(json.dumps(exp, indent=2, ensure_ascii=False))\n        print()\n    else:\n        print(f'{t}: NOT FOUND in registry')\n\"",
  "description": "Extract failed eval experiments from saved registry data"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "491adb13-5152-44de-9c8a-8fb7b16c30c8",
  "isSidechain": false,
  "requestId": "req_011CbHW4igmZcRPujm2UQqXQ",
  "type": "assistant",
  "uuid": "a1c18ae6-47ff-4004-88f7-2707eab7bd4a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_5ae72916",
  "sessionId": "ecab2a37-b09b-48e2-a661-0d7a5b7a31ca",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P26CVXvsLDj7MT6rygE2xg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1249,
      "cache_read_input_tokens": 45024,
      "output_tokens": 559,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1249,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 559,
          "cache_read_input_tokens": 45024,
          "cache_creation_input_tokens": 1249,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1249
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

_source line 38 · 2026-05-22T11:08:25.632Z_

<details open><summary>🔧 Tool call — Glob · `toolu_016Kea77naoANP7HvzYxwMLo`</summary>

```json
{
  "pattern": "**/*on-experiment-failed*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a1c18ae6-47ff-4004-88f7-2707eab7bd4a",
  "isSidechain": false,
  "requestId": "req_011CbHW4igmZcRPujm2UQqXQ",
  "type": "assistant",
  "uuid": "e6b627c5-8f61-46fc-91b5-bae95f41c5f3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_5ae72916",
  "sessionId": "ecab2a37-b09b-48e2-a661-0d7a5b7a31ca",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P26CVXvsLDj7MT6rygE2xg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1249,
      "cache_read_input_tokens": 45024,
      "output_tokens": 559,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1249,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 559,
          "cache_read_input_tokens": 45024,
          "cache_creation_input_tokens": 1249,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1249
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

_source line 39 · 2026-05-22T11:08:25.946Z_

<details><summary>↩ Tool result · `toolu_01Wd9fWZWDuWgLYrgYP1hCDy`</summary>

```text
=== eval_falcon3_d025_s42 ===
{
  "status": "DONE",
  "created_at": "2026-05-22T11:03:32.692Z",
  "updated_at": "2026-05-22T11:07:23.351Z",
  "hypothesis": "Falcon3-7B-Base d025 eval: MMLU 5-shot + ARC 25-shot aligned MC format for dose-response profiling",
  "conclusion": "failed"
}

=== eval_falcon3_d005_s42 ===
{
  "status": "DONE",
  "created_at": "2026-05-22T11:03:28.661Z",
  "updated_at": "2026-05-22T11:07:03.524Z",
  "hypothesis": "Falcon3-7B-Base d005 eval: MMLU 5-shot + ARC 25-shot aligned MC format for dose-response profiling",
  "conclusion": "failed"
}

=== eval_falcon3_d000_s42 ===
{
  "status": "DONE",
  "created_at": "2026-05-22T11:03:25.016Z",
  "updated_at": "2026-05-22T11:06:44.078Z",
  "hypothesis": "Falcon3-7B-Base d000 eval: MMLU 5-shot + ARC 25-shot aligned MC format for dose-response profiling",
  "conclusion": "failed"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a1c18ae6-47ff-4004-88f7-2707eab7bd4a",
  "isSidechain": false,
  "promptId": "9e81e78d-88e1-48cf-a480-c0cfdcf0974a",
  "type": "user",
  "uuid": "f6645cfe-997d-42b6-9f30-247177d5fdfb",
  "toolUseResult": {
    "stdout": "=== eval_falcon3_d025_s42 ===\n{\n  \"status\": \"DONE\",\n  \"created_at\": \"2026-05-22T11:03:32.692Z\",\n  \"updated_at\": \"2026-05-22T11:07:23.351Z\",\n  \"hypothesis\": \"Falcon3-7B-Base d025 eval: MMLU 5-shot + ARC 25-shot aligned MC format for dose-response profiling\",\n  \"conclusion\": \"failed\"\n}\n\n=== eval_falcon3_d005_s42 ===\n{\n  \"status\": \"DONE\",\n  \"created_at\": \"2026-05-22T11:03:28.661Z\",\n  \"updated_at\": \"2026-05-22T11:07:03.524Z\",\n  \"hypothesis\": \"Falcon3-7B-Base d005 eval: MMLU 5-shot + ARC 25-shot aligned MC format for dose-response profiling\",\n  \"conclusion\": \"failed\"\n}\n\n=== eval_falcon3_d000_s42 ===\n{\n  \"status\": \"DONE\",\n  \"created_at\": \"2026-05-22T11:03:25.016Z\",\n  \"updated_at\": \"2026-05-22T11:06:44.078Z\",\n  \"hypothesis\": \"Falcon3-7B-Base d000 eval: MMLU 5-shot + ARC 25-shot aligned MC format for dose-response profiling\",\n  \"conclusion\": \"failed\"\n}",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "a1c18ae6-47ff-4004-88f7-2707eab7bd4a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_5ae72916",
  "sessionId": "ecab2a37-b09b-48e2-a661-0d7a5b7a31ca",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-22T11:08:26.228Z_

<details><summary>↩ Tool result · `toolu_016Kea77naoANP7HvzYxwMLo`</summary>

```text
No files found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e6b627c5-8f61-46fc-91b5-bae95f41c5f3",
  "isSidechain": false,
  "promptId": "9e81e78d-88e1-48cf-a480-c0cfdcf0974a",
  "type": "user",
  "uuid": "50c46d71-fa21-4bfc-b403-95f3d63f9d9e",
  "toolUseResult": {
    "filenames": [],
    "durationMs": 254,
    "numFiles": 0,
    "truncated": false
  },
  "sourceToolAssistantUUID": "e6b627c5-8f61-46fc-91b5-bae95f41c5f3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_5ae72916",
  "sessionId": "ecab2a37-b09b-48e2-a661-0d7a5b7a31ca",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 41 · 2026-05-22T11:08:38.754Z_

<details><summary>Logged reasoning block</summary>

```text
The on-experiment-failed skill is referenced in CLAUDE.md but the file doesn't exist at the expected path. Let me search for it more broadly. But actually, the key thing is I need to:

1. Spawn a worker to SSH into westd-29999 and check the logs for these failed eval experiments
2. The three eval experiments (d000, d005, d025) all failed with EXIT_CODE=1 within minutes of each other
3. They were created around 11:03 and failed around 11:06-11:07, so they ran for ~3 minutes

Let me also check what the SFT experiments look like for the v2 versions that succeeded - `sft_falcon3_7b_d025_s42_v2` and `sft_falcon3_7b_d005_s42_v2`. 

Looking at the report.md, I can see the GPU allocation on westd-29999 - cuda:0 shows as idle but allocated, while cuda:3 is running the d050 SFT experiment. The three failed evals were all on westd-29999, so I need to spawn a worker to SSH in and check those logs to understand what went wrong.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "50c46d71-fa21-4bfc-b403-95f3d63f9d9e",
  "isSidechain": false,
  "requestId": "req_011CbHW5fsNjdPVNNRAmpZ1E",
  "type": "assistant",
  "uuid": "6aa3157b-666e-437a-a930-86425876c817",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_5ae72916",
  "sessionId": "ecab2a37-b09b-48e2-a661-0d7a5b7a31ca",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RKSyYEggN6bAX7Mn2VpcG8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1004,
      "cache_read_input_tokens": 46273,
      "output_tokens": 528,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1004,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 528,
          "cache_read_input_tokens": 46273,
          "cache_creation_input_tokens": 1004,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1004
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

_source line 42 · 2026-05-22T11:08:39.243Z_

三个 Falcon3 eval 实验全部失败，EXIT_CODE=1，创建到失败仅 3-4 分钟。需要派 Worker 去 westd-29999 查日志诊断。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6aa3157b-666e-437a-a930-86425876c817",
  "isSidechain": false,
  "requestId": "req_011CbHW5fsNjdPVNNRAmpZ1E",
  "type": "assistant",
  "uuid": "c11c92bf-4998-4331-9aa2-72c541444a87",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_5ae72916",
  "sessionId": "ecab2a37-b09b-48e2-a661-0d7a5b7a31ca",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RKSyYEggN6bAX7Mn2VpcG8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1004,
      "cache_read_input_tokens": 46273,
      "output_tokens": 528,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1004,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 528,
          "cache_read_input_tokens": 46273,
          "cache_creation_input_tokens": 1004,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1004
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

_source line 43 · 2026-05-22T11:08:39.865Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01Sh2NMnELUexqWgnNvM2keJ`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__spawn_worker,mcp__agent-ml-research__update_registry",
  "max_results": 2
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c11c92bf-4998-4331-9aa2-72c541444a87",
  "isSidechain": false,
  "requestId": "req_011CbHW5fsNjdPVNNRAmpZ1E",
  "type": "assistant",
  "uuid": "582f0432-ea7e-4a8f-81cf-422e328a833a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_5ae72916",
  "sessionId": "ecab2a37-b09b-48e2-a661-0d7a5b7a31ca",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RKSyYEggN6bAX7Mn2VpcG8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1004,
      "cache_read_input_tokens": 46273,
      "output_tokens": 528,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1004,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 528,
          "cache_read_input_tokens": 46273,
          "cache_creation_input_tokens": 1004,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1004
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

_source line 44 · 2026-05-22T11:08:39.875Z_

<details><summary>↩ Tool result · `toolu_01Sh2NMnELUexqWgnNvM2keJ`</summary>

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
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "582f0432-ea7e-4a8f-81cf-422e328a833a",
  "isSidechain": false,
  "promptId": "9e81e78d-88e1-48cf-a480-c0cfdcf0974a",
  "type": "user",
  "uuid": "ab11f625-2c40-4d21-bfb4-dad0587f9d22",
  "toolUseResult": {
    "matches": [
      "mcp__agent-ml-research__spawn_worker",
      "mcp__agent-ml-research__update_registry"
    ],
    "query": "select:mcp__agent-ml-research__spawn_worker,mcp__agent-ml-research__update_registry",
    "total_deferred_tools": 82
  },
  "sourceToolAssistantUUID": "582f0432-ea7e-4a8f-81cf-422e328a833a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_5ae72916",
  "sessionId": "ecab2a37-b09b-48e2-a661-0d7a5b7a31ca",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 45_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[CRON] 实验进程异常退出（失败），需要你诊断原因。 详情: Process exited without valid W&B metrics  - exp_id: eval_falcon3_d025_s42 - project: contamcal-irt-calibration - server: westd-29999",
  "leafUuid": "ab11f625-2c40-4d21-bfb4-dad0587f9d22",
  "sessionId": "ecab2a37-b09b-48e2-a661-0d7a5b7a31ca"
}
```

---

### Runtime record

_source line 46_

```json
{
  "type": "ai-title",
  "aiTitle": "Diagnose W&B metrics missing in Falcon3 experiment",
  "sessionId": "ecab2a37-b09b-48e2-a661-0d7a5b7a31ca"
}
```

---

### Assistant

_source line 47 · 2026-05-22T11:08:57.578Z_

<details><summary>Logged reasoning block</summary>

```text
Now I need to spawn a Worker to SSH into westd-29999 and diagnose why the three eval experiments failed. The worker needs to check logs. Let me also look at what log paths might exist.

From the report, the experiments ran on westd-29999. The registry entries are minimal - no spec, no log_path, no server info recorded. They were created and failed within 3-4 minutes.

Let me also check if there are related SFT experiments that succeeded recently - `sft_falcon3_7b_d025_s42_v2` and `sft_falcon3_7b_d005_s42_v2` succeeded. 

The evals would be evaluating those checkpoints. I'll set up a worker to SSH into westd-29999 and locate the eval log files to see what caused the failures. Looking at the current resource status, westd-29999:cuda:0 is allocated but idle, and there are two other experiments running on different machines, so I should have access to investigate.

Before I report back, I need to check the resource-saturation skill per the guidelines, but first let me get the diagnosis underway. I also want to pull the full registry data from the successful SFT v2 experiments to understand which checkpoints the evals were supposed to be evaluating.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ab11f625-2c40-4d21-bfb4-dad0587f9d22",
  "isSidechain": false,
  "requestId": "req_011CbHW6gGTvGmL3tgJ7FY3G",
  "type": "assistant",
  "uuid": "64b37553-4db2-43bf-9557-d995b0bca7d7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_5ae72916",
  "sessionId": "ecab2a37-b09b-48e2-a661-0d7a5b7a31ca",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01T2cNgjWfdLjvfaUcpywFBH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2204,
      "cache_read_input_tokens": 47277,
      "output_tokens": 1255,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2204,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1255,
          "cache_read_input_tokens": 47277,
          "cache_creation_input_tokens": 2204,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2204
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

_source line 48 · 2026-05-22T11:08:57.583Z_

派 Worker 去 westd-29999 诊断三个 eval 实验的失败原因。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "64b37553-4db2-43bf-9557-d995b0bca7d7",
  "isSidechain": false,
  "requestId": "req_011CbHW6gGTvGmL3tgJ7FY3G",
  "type": "assistant",
  "uuid": "14b21593-ceba-4ea4-9eb6-521acad7fd3a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_5ae72916",
  "sessionId": "ecab2a37-b09b-48e2-a661-0d7a5b7a31ca",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01T2cNgjWfdLjvfaUcpywFBH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2204,
      "cache_read_input_tokens": 47277,
      "output_tokens": 1255,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2204,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1255,
          "cache_read_input_tokens": 47277,
          "cache_creation_input_tokens": 2204,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2204
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

_source line 49 · 2026-05-22T11:09:13.201Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__spawn_worker · `toolu_01PVQNVeahqFiWVXLYAJaSsQ`</summary>

````json
{
  "task_type": "diagnose:eval_falcon3_failed",
  "project": "contamcal-irt-calibration",
  "task_prompt": "## 任务\n诊断 westd-29999 上三个 Falcon3-7B eval 实验的失败原因。\n\n## 背景\n以下三个 eval 实验在 2026-05-22 约 11:03-11:07 UTC 期间运行并全部以 EXIT_CODE=1 失败：\n- eval_falcon3_d000_s42\n- eval_falcon3_d005_s42\n- eval_falcon3_d025_s42\n\n这些是 Falcon3-7B-Base 模型在不同 contamination dosage (d000/d005/d025) 下的 SFT checkpoint 的 MMLU 5-shot + ARC 25-shot eval。对应的 SFT 训练实验 (sft_falcon3_7b_d000_s42_v2, sft_falcon3_7b_d005_s42_v2, sft_falcon3_7b_d025_s42_v2) 已成功完成。\n\n## 诊断步骤\n\n1. **找日志文件**：SSH (read_only) 到 westd-29999，搜索 eval 日志：\n   ```\n   ls -la /root/projects/contamcal-irt-calibration/eval_falcon3_d*_s42*.log 2>/dev/null\n   ls -la /root/projects/contamcal-irt-calibration/*eval*falcon3* 2>/dev/null\n   find /root/projects/contamcal-irt-calibration/ -name \"*eval_falcon3*\" -mmin -60 2>/dev/null\n   find /root/ -name \"*eval_falcon3*\" -mmin -60 2>/dev/null\n   ```\n\n2. **读取日志尾部**：找到日志后，读最后 100 行，找 error/traceback/exception\n\n3. **检查 eval 脚本**：查看 eval 脚本内容，理解它期望什么输入（checkpoint 路径、数据路径等）\n\n4. **检查 checkpoint 是否存在**：验证 SFT v2 训练产出的 checkpoint 是否在预期路径\n\n5. **检查环境**：\n   - Python 环境是否正常（torch、transformers 版本）\n   - 磁盘空间是否充足\n   - GPU 状态 (nvidia-smi)\n\n## 产出\n写一份简洁的诊断报告，包含：\n- 根因（root cause）\n- 错误信息（关键 traceback）\n- 修复建议（具体到命令或代码改动）\n\n用 save_project_file(file=\"worker_output.md\") 保存报告。",
  "tool_groups": [
    "ssh",
    "knowledge"
  ]
}
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "14b21593-ceba-4ea4-9eb6-521acad7fd3a",
  "isSidechain": false,
  "requestId": "req_011CbHW6gGTvGmL3tgJ7FY3G",
  "type": "assistant",
  "uuid": "2a03498e-06c4-4351-8a38-019332e5bf93",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_5ae72916",
  "sessionId": "ecab2a37-b09b-48e2-a661-0d7a5b7a31ca",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01T2cNgjWfdLjvfaUcpywFBH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2204,
      "cache_read_input_tokens": 47277,
      "output_tokens": 1255,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2204,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1255,
          "cache_read_input_tokens": 47277,
          "cache_creation_input_tokens": 2204,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2204
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

_source line 50 · 2026-05-22T11:09:17.402Z_

<details><summary>↩ Tool result · `toolu_01PVQNVeahqFiWVXLYAJaSsQ`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"Worker of type 'diagnose:eval_falcon3_failed' is already active for project 'contamcal-irt-calibration'. worker_id=worker_diagnose_eval_falcon3_failed_20260522T110904\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2a03498e-06c4-4351-8a38-019332e5bf93",
  "isSidechain": false,
  "promptId": "9e81e78d-88e1-48cf-a480-c0cfdcf0974a",
  "type": "user",
  "uuid": "a5b3d317-673b-44b9-8a1a-7ad99a58d853",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {}, \\\"error\\\": \\\"Worker of type 'diagnose:eval_falcon3_failed' is already active for project 'contamcal-irt-calibration'. worker_id=worker_diagnose_eval_falcon3_failed_20260522T110904\\\", \\\"metadata\\\": {}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {}, \"error\": \"Worker of type 'diagnose:eval_falcon3_failed' is already active for project 'contamcal-irt-calibration'. worker_id=worker_diagnose_eval_falcon3_failed_20260522T110904\", \"metadata\": {}}"
    }
  },
  "sourceToolAssistantUUID": "2a03498e-06c4-4351-8a38-019332e5bf93",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_5ae72916",
  "sessionId": "ecab2a37-b09b-48e2-a661-0d7a5b7a31ca",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 51 · 2026-05-22T11:09:24.531Z_

<details><summary>Logged reasoning block</summary>

```text
A worker of this type is already active. This is likely from a previous cron callback for one of the other two failed evals (d000 or d005). Let me check the worker status to see what's happening.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a5b3d317-673b-44b9-8a1a-7ad99a58d853",
  "isSidechain": false,
  "requestId": "req_011CbHW9SpRVCzEE4oo6h2tK",
  "type": "assistant",
  "uuid": "2a323193-ce51-4d86-8d7c-0950edc41130",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_5ae72916",
  "sessionId": "ecab2a37-b09b-48e2-a661-0d7a5b7a31ca",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AqhkR9Gp8ZFqgtBrYaRL4M",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1351,
      "cache_read_input_tokens": 49481,
      "output_tokens": 181,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1351,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 181,
          "cache_read_input_tokens": 49481,
          "cache_creation_input_tokens": 1351,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1351
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

_source line 52 · 2026-05-22T11:09:25.495Z_

已有同类型 Worker 在运行。检查其状态。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2a323193-ce51-4d86-8d7c-0950edc41130",
  "isSidechain": false,
  "requestId": "req_011CbHW9SpRVCzEE4oo6h2tK",
  "type": "assistant",
  "uuid": "941cfb1c-cb20-4421-9a95-0e64ad46a1fd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_5ae72916",
  "sessionId": "ecab2a37-b09b-48e2-a661-0d7a5b7a31ca",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AqhkR9Gp8ZFqgtBrYaRL4M",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1351,
      "cache_read_input_tokens": 49481,
      "output_tokens": 181,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1351,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 181,
          "cache_read_input_tokens": 49481,
          "cache_creation_input_tokens": 1351,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1351
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

_source line 53 · 2026-05-22T11:09:26.018Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01EFGT8o2GCFcw9SeW8M6jxD`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__get_worker_status,mcp__agent-ml-research__list_workers",
  "max_results": 2
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "941cfb1c-cb20-4421-9a95-0e64ad46a1fd",
  "isSidechain": false,
  "requestId": "req_011CbHW9SpRVCzEE4oo6h2tK",
  "type": "assistant",
  "uuid": "fc2d015c-8020-4316-a404-c370c81f8013",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_5ae72916",
  "sessionId": "ecab2a37-b09b-48e2-a661-0d7a5b7a31ca",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AqhkR9Gp8ZFqgtBrYaRL4M",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1351,
      "cache_read_input_tokens": 49481,
      "output_tokens": 181,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1351,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 181,
          "cache_read_input_tokens": 49481,
          "cache_creation_input_tokens": 1351,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1351
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

_source line 54 · 2026-05-22T11:09:26.023Z_

<details><summary>↩ Tool result · `toolu_01EFGT8o2GCFcw9SeW8M6jxD`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__get_worker_status"
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
  "parentUuid": "fc2d015c-8020-4316-a404-c370c81f8013",
  "isSidechain": false,
  "promptId": "9e81e78d-88e1-48cf-a480-c0cfdcf0974a",
  "type": "user",
  "uuid": "e184f941-78f1-44a1-ad7d-a2b6418ccdb7",
  "toolUseResult": {
    "matches": [
      "mcp__agent-ml-research__get_worker_status",
      "mcp__agent-ml-research__list_workers"
    ],
    "query": "select:mcp__agent-ml-research__get_worker_status,mcp__agent-ml-research__list_workers",
    "total_deferred_tools": 82
  },
  "sourceToolAssistantUUID": "fc2d015c-8020-4316-a404-c370c81f8013",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_5ae72916",
  "sessionId": "ecab2a37-b09b-48e2-a661-0d7a5b7a31ca",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 55 · 2026-05-22T11:09:31.508Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_worker_status · `toolu_01HdZUBHYMFfUjyDKSVzsHw6`</summary>

```json
{
  "worker_id": "worker_diagnose_eval_falcon3_failed_20260522T110904",
  "verbose": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e184f941-78f1-44a1-ad7d-a2b6418ccdb7",
  "isSidechain": false,
  "requestId": "req_011CbHWA5bkbkpZt74qfHiY7",
  "type": "assistant",
  "uuid": "1d24a046-dde7-44b2-8177-1e337a10019e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_5ae72916",
  "sessionId": "ecab2a37-b09b-48e2-a661-0d7a5b7a31ca",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KpRM5e9kmV4DTsA5VbAVj5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 631,
      "cache_read_input_tokens": 50832,
      "output_tokens": 101,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 631,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 101,
          "cache_read_input_tokens": 50832,
          "cache_creation_input_tokens": 631,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 631
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

_source line 56 · 2026-05-22T11:09:31.719Z_

<details><summary>↩ Tool result · `toolu_01HdZUBHYMFfUjyDKSVzsHw6`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"worker_id\": \"worker_diagnose_eval_falcon3_failed_20260522T110904\", \"status\": \"running\", \"task_type\": \"diagnose:eval_falcon3_failed\", \"project\": \"contamcal-irt-calibration\", \"started_at\": \"2026-05-22T11:09:04.439536+00:00\", \"ended_at\": null, \"setup\": null, \"teardown\": null, \"setup_data\": {}, \"progress\": {\"recent_tools\": [\"ToolSearch\"], \"last_text\": \"开始诊断 westd-29999 上三个 Falcon3 eval 失败的原因。先读取日志。\", \"turn_count\": 3}}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1d24a046-dde7-44b2-8177-1e337a10019e",
  "isSidechain": false,
  "promptId": "9e81e78d-88e1-48cf-a480-c0cfdcf0974a",
  "type": "user",
  "uuid": "50ed8969-a6b7-47e2-b5a4-766b7178f288",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"worker_id\\\": \\\"worker_diagnose_eval_falcon3_failed_20260522T110904\\\", \\\"status\\\": \\\"running\\\", \\\"task_type\\\": \\\"diagnose:eval_falcon3_failed\\\", \\\"project\\\": \\\"contamcal-irt-calibration\\\", \\\"started_at\\\": \\\"2026-05-22T11:09:04.439536+00:00\\\", \\\"ended_at\\\": null, \\\"setup\\\": null, \\\"teardown\\\": null, \\\"setup_data\\\": {}, \\\"progress\\\": {\\\"recent_tools\\\": [\\\"ToolSearch\\\"], \\\"last_text\\\": \\\"开始诊断 westd-29999 上三个 Falcon3 eval 失败的原因。先读取日志。\\\", \\\"turn_count\\\": 3}}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"worker_id\": \"worker_diagnose_eval_falcon3_failed_20260522T110904\", \"status\": \"running\", \"task_type\": \"diagnose:eval_falcon3_failed\", \"project\": \"contamcal-irt-calibration\", \"started_at\": \"2026-05-22T11:09:04.439536+00:00\", \"ended_at\": null, \"setup\": null, \"teardown\": null, \"setup_data\": {}, \"progress\": {\"recent_tools\": [\"ToolSearch\"], \"last_text\": \"开始诊断 westd-29999 上三个 Falcon3 eval 失败的原因。先读取日志。\", \"turn_count\": 3}}, \"error\": null, \"metadata\": {}}"
    }
  },
  "sourceToolAssistantUUID": "1d24a046-dde7-44b2-8177-1e337a10019e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_5ae72916",
  "sessionId": "ecab2a37-b09b-48e2-a661-0d7a5b7a31ca",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 57 · 2026-05-22T11:09:31.724Z_

```json
{
  "parentUuid": "50ed8969-a6b7-47e2-b5a4-766b7178f288",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "00191b27-f3ae-4621-a40f-9809f8d9cf0b",
  "timestamp": "2026-05-22T11:09:31.724Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_5ae72916",
  "sessionId": "ecab2a37-b09b-48e2-a661-0d7a5b7a31ca",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 58_

```json
{
  "type": "ai-title",
  "aiTitle": "Diagnose W&B metrics missing in Falcon3 experiment",
  "sessionId": "ecab2a37-b09b-48e2-a661-0d7a5b7a31ca"
}
```

---

### Runtime record

_source line 59 · 2026-05-23T03:14:00.570Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-23T03:14:00.570Z",
  "sessionId": "ecab2a37-b09b-48e2-a661-0d7a5b7a31ca",
  "content": "[WRITE HANDOFF] 请立即写你的 handoff。\n\n**格式硬约束**:\n- 整条回复**只能**是 &lt;handoff>...&lt;/handoff> 标签包裹\n- 禁止在标签外写任何寒暄 / 说明 / 确认（\"好的\"/\"我开始写\"/\"写完了\"等）\n\n**必须覆盖以下 5 个 section（缺一不可，无内容写 N/A）**:\n\n### 1. 🔴 硬约束 / 红线\n  本项目特定的不可违反约束（GPU 设备号、服务器名、账号、路径限制等）。\n  写本项目特定的，不要抄 CLAUDE.md 通用 L1 红线。\n  下一个\"你\"第一眼看到的就是这里，写错了会被 Director CRITICAL。\n\n### 2. 🖥️ 基础设施快照\n  - 服务器名 + 工作目录 + Python 路径 + conda env\n  - 模型路径 / 数据集路径 / wandb config / HF cache\n  - 活跃进程：PID + tmux session + cron 任务 ID\n  写一次就稳定，下一个\"你\"不用再 SSH 探查。\n\n### 3. 📊 当前状态\n  - 你刚做完什么 / 正在做什么\n  - registry 里 RUNNING/PREPARING 的实验列表 + 一句话摘要\n  - 等待中的 Worker 回调 / Cron / Director 决策\n\n### 4. 📋 待办（条件触发式）\n  格式 \"条件 X 满足 → 动作 Y\"。例如:\n  - \"Falcon-H1R 下载完成 → sed 修 MODEL_PATH → dry-run → 提交\"\n  - \"pilot_011 出 GC4 结果 → ≥2pp 转架构 narrative，<2pp 写 null-result\"\n\n### 5. 🎯 战略上下文\n  - 项目核心结论 / 决策链（D001..）\n  - 下一个\"你\"最容易判断错的事 / 容易踩的坑\n\n**写作原则**：\n- 第 1 节必须是项目特定的（不是通用 L1 红线）\n- 第 2 节让下一轮 BOOT 后能立即开工，避免重新 SSH 探查\n- 简洁 > 完整：每节 5-10 行足够，长 handoff 不等于好 handoff\n\n示例格式:\n&lt;handoff>\n### 1. 🔴 硬约束 / 红线\n- 本项目只能用 cuda:4 / cuda:5（之前两次违规 cuda:0 被 Director CRITICAL）\n- submit_training_job 不支持 shell builtin（source/conda activate 全不行）\n\n### 2. 🖥️ 基础设施快照\n- 服务器：westd-8x6000，工作目录 /root/autodl-tmp/hybrid_reasoning_phases\n- Python：/root/miniconda3/bin/python（绝对路径，不走 conda activate）\n- 模型：/root/autodl-tmp/qwen35_4b_direct\n- 活跃：pilot_011 (PID 203221, tmux=pilot_011, cuda:4)\n\n### 3. 📊 当前状态\n我刚完成 pilot_010 分析，正在等 pilot_011 (Falcon-H1R) CoT 生成完成（6/50）。\nregistry: pilot_011 RUNNING；其他全 DONE。\n\n### 4. 📋 待办\n- pilot_011 cron 回调 → spawn worker 跑 probe + GC4 计算\n- GC4 ≥2pp → 转架构 narrative；<2pp → null-result paper outline 已就绪\n\n### 5. 🎯 战略上下文\nFalcon-H1R 是最后一个数据点。已知 4B/9B GC4 都 FAIL。\n易错：不要把 GC4-par (Falcon parallel) 和 GC4-seq (Qwen sequential) 直接对比。\n&lt;/handoff>"
}
```

---

### Runtime record

_source line 60 · 2026-05-23T03:14:00.571Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-23T03:14:00.571Z",
  "sessionId": "ecab2a37-b09b-48e2-a661-0d7a5b7a31ca"
}
```

---

## Round 2

2 recorded events

### User

_source line 61 · 2026-05-23T03:14:00.557Z_

Continue from where you left off.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "00191b27-f3ae-4621-a40f-9809f8d9cf0b",
  "isSidechain": false,
  "promptId": "603f6fa2-faa1-4447-83aa-8cda0de9035a",
  "type": "user",
  "isMeta": true,
  "uuid": "be681e8c-84eb-4589-9c20-bab6f8b76517",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_5ae72916",
  "sessionId": "ecab2a37-b09b-48e2-a661-0d7a5b7a31ca",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 62 · 2026-05-23T03:14:00.557Z_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "be681e8c-84eb-4589-9c20-bab6f8b76517",
  "isSidechain": false,
  "type": "assistant",
  "uuid": "7e7a7fb4-71d3-468c-b0d7-a3e6547e88c4",
  "isApiErrorMessage": false,
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_5ae72916",
  "sessionId": "ecab2a37-b09b-48e2-a661-0d7a5b7a31ca",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "id": "b8c526b3-2c59-409b-bb3d-fd1b8f5dfc9a",
    "container": null,
    "model": "&lt;synthetic>",
    "stop_reason": "stop_sequence",
    "stop_sequence": "",
    "type": "message",
    "usage": {
      "input_tokens": 0,
      "output_tokens": 0,
      "cache_creation_input_tokens": 0,
      "cache_read_input_tokens": 0,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": null,
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": null,
      "iterations": null,
      "speed": null
    },
    "context_management": null
  }
}
```

</details>

---

## Round 3

1 recorded events

### User

_source line 63 · 2026-05-23T03:14:00.710Z_

[WRITE HANDOFF] 请立即写你的 handoff。

**格式硬约束**:
- 整条回复**只能**是 &lt;handoff>...&lt;/handoff> 标签包裹
- 禁止在标签外写任何寒暄 / 说明 / 确认（"好的"/"我开始写"/"写完了"等）

**必须覆盖以下 5 个 section（缺一不可，无内容写 N/A）**:

### 1. 🔴 硬约束 / 红线
  本项目特定的不可违反约束（GPU 设备号、服务器名、账号、路径限制等）。
  写本项目特定的，不要抄 CLAUDE.md 通用 L1 红线。
  下一个"你"第一眼看到的就是这里，写错了会被 Director CRITICAL。

### 2. 🖥️ 基础设施快照
  - 服务器名 + 工作目录 + Python 路径 + conda env
  - 模型路径 / 数据集路径 / wandb config / HF cache
  - 活跃进程：PID + tmux session + cron 任务 ID
  写一次就稳定，下一个"你"不用再 SSH 探查。

### 3. 📊 当前状态
  - 你刚做完什么 / 正在做什么
  - registry 里 RUNNING/PREPARING 的实验列表 + 一句话摘要
  - 等待中的 Worker 回调 / Cron / Director 决策

### 4. 📋 待办（条件触发式）
  格式 "条件 X 满足 → 动作 Y"。例如:
  - "Falcon-H1R 下载完成 → sed 修 MODEL_PATH → dry-run → 提交"
  - "pilot_011 出 GC4 结果 → ≥2pp 转架构 narrative，<2pp 写 null-result"

### 5. 🎯 战略上下文
  - 项目核心结论 / 决策链（D001..）
  - 下一个"你"最容易判断错的事 / 容易踩的坑

**写作原则**：
- 第 1 节必须是项目特定的（不是通用 L1 红线）
- 第 2 节让下一轮 BOOT 后能立即开工，避免重新 SSH 探查
- 简洁 > 完整：每节 5-10 行足够，长 handoff 不等于好 handoff

示例格式:
&lt;handoff>
### 1. 🔴 硬约束 / 红线
- 本项目只能用 cuda:4 / cuda:5（之前两次违规 cuda:0 被 Director CRITICAL）
- submit_training_job 不支持 shell builtin（source/conda activate 全不行）

### 2. 🖥️ 基础设施快照
- 服务器：westd-8x6000，工作目录 /root/autodl-tmp/hybrid_reasoning_phases
- Python：/root/miniconda3/bin/python（绝对路径，不走 conda activate）
- 模型：/root/autodl-tmp/qwen35_4b_direct
- 活跃：pilot_011 (PID 203221, tmux=pilot_011, cuda:4)

### 3. 📊 当前状态
我刚完成 pilot_010 分析，正在等 pilot_011 (Falcon-H1R) CoT 生成完成（6/50）。
registry: pilot_011 RUNNING；其他全 DONE。

### 4. 📋 待办
- pilot_011 cron 回调 → spawn worker 跑 probe + GC4 计算
- GC4 ≥2pp → 转架构 narrative；<2pp → null-result paper outline 已就绪

### 5. 🎯 战略上下文
Falcon-H1R 是最后一个数据点。已知 4B/9B GC4 都 FAIL。
易错：不要把 GC4-par (Falcon parallel) 和 GC4-seq (Qwen sequential) 直接对比。
&lt;/handoff>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7e7a7fb4-71d3-468c-b0d7-a3e6547e88c4",
  "isSidechain": false,
  "promptId": "603f6fa2-faa1-4447-83aa-8cda0de9035a",
  "type": "user",
  "uuid": "d187f074-4fec-477b-8c6a-a9e6a60c1902",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_5ae72916",
  "sessionId": "ecab2a37-b09b-48e2-a661-0d7a5b7a31ca",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---
