# Research conversation: [CRON] 实验进程已正常退出，状态已转为 ANALYZING，需要你分析结果并推进到 DONE。 详情: Process exited cleanly, W&B data available - exp_id: alpha_sweep_

**Characterizing the Detectability Landscape of Iterative Model Collapse (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 37
- **Recorded user turns:** 1
- **Tool calls:** 9
- **Original source:** `logs/chats/exported-trajectories/account-2/4f6074eb-8665-49ec-9526-07c9eebcea03.jsonl`
- **Structured JSON:** [`63fc9b0ee240f21d37d4.json`](../../sessions/63/63fc9b0ee240f21d37d4.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-16T02:24:30.374Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-16T02:24:30.374Z",
  "sessionId": "4f6074eb-8665-49ec-9526-07c9eebcea03",
  "content": "[CRON] 实验进程已正常退出，状态已转为 ANALYZING，需要你分析结果并推进到 DONE。\n详情: Process exited cleanly, W&B data available\n\n- exp_id: alpha_sweep_a025_s44\n- project: distrib_canary_collapse\n- server: westd-19828\n- log_path: ~/runs/distrib_canary_collapse/alpha_sweep_a025_s44.log"
}
```

---

### Runtime record

_source line 2 · 2026-05-16T02:24:30.381Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-16T02:24:30.381Z",
  "sessionId": "4f6074eb-8665-49ec-9526-07c9eebcea03"
}
```

---

## Round 1

35 recorded events

### User

_source line 3 · 2026-05-16T02:24:30.420Z_

[CRON] 实验进程已正常退出，状态已转为 ANALYZING，需要你分析结果并推进到 DONE。
详情: Process exited cleanly, W&B data available

- exp_id: alpha_sweep_a025_s44
- project: distrib_canary_collapse
- server: westd-19828
- log_path: ~/runs/distrib_canary_collapse/alpha_sweep_a025_s44.log

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "a304cee9-feed-4fb2-a028-8ae1d93109aa",
  "type": "user",
  "uuid": "ea510b13-0112-4d71-bf29-668a1c955d14",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/agent_e1f64cd5",
  "sessionId": "4f6074eb-8665-49ec-9526-07c9eebcea03",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-16T02:24:30.419Z_

```json
{
  "parentUuid": "ea510b13-0112-4d71-bf29-668a1c955d14",
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
  "uuid": "5ac4b7c8-8d57-4c10-bc6c-586f84d3ed84",
  "timestamp": "2026-05-16T02:24:30.419Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/agent_e1f64cd5",
  "sessionId": "4f6074eb-8665-49ec-9526-07c9eebcea03",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-16T02:24:30.419Z_

```json
{
  "parentUuid": "5ac4b7c8-8d57-4c10-bc6c-586f84d3ed84",
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
  "uuid": "f604cfe8-409b-4cf4-a39f-5e73633649e5",
  "timestamp": "2026-05-16T02:24:30.419Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/agent_e1f64cd5",
  "sessionId": "4f6074eb-8665-49ec-9526-07c9eebcea03",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6 · 2026-05-16T02:24:30.419Z_

```json
{
  "parentUuid": "f604cfe8-409b-4cf4-a39f-5e73633649e5",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "1ef70834-13a3-4250-aea1-e6508b14399d",
  "timestamp": "2026-05-16T02:24:30.419Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/agent_e1f64cd5",
  "sessionId": "4f6074eb-8665-49ec-9526-07c9eebcea03",
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
  "sessionId": "4f6074eb-8665-49ec-9526-07c9eebcea03"
}
```

---

### Assistant

_source line 8 · 2026-05-16T02:24:35.312Z_

<details><summary>Logged reasoning block</summary>

```text
收到实验完成的 CRON 回调，需要执行 session-start 初始化，然后处理实验完成的分析流程。

让我按顺序执行：
1. Session start: read_registry, reconcile_crons, read report.md, read ROADMAP.md
2. 然后分析实验结果

先加载需要的工具。
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1ef70834-13a3-4250-aea1-e6508b14399d",
  "isSidechain": false,
  "requestId": "req_011Cb5TGuTMmWwhMozk5yid5",
  "type": "assistant",
  "uuid": "f72e456b-1882-4fe9-995b-ee027e738f5a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/agent_e1f64cd5",
  "sessionId": "4f6074eb-8665-49ec-9526-07c9eebcea03",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017fD9xTnS4UdzRfP4iWDZFy",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 22985,
      "cache_read_input_tokens": 11841,
      "output_tokens": 330,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 22985,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 330,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 22985,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 22985
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

_source line 9 · 2026-05-16T02:24:36.319Z_

Session 启动，先初始化项目状态，同时处理实验完成回调。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f72e456b-1882-4fe9-995b-ee027e738f5a",
  "isSidechain": false,
  "requestId": "req_011Cb5TGuTMmWwhMozk5yid5",
  "type": "assistant",
  "uuid": "05cc09e6-525a-4b1d-834b-113eaf7baa72",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/agent_e1f64cd5",
  "sessionId": "4f6074eb-8665-49ec-9526-07c9eebcea03",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017fD9xTnS4UdzRfP4iWDZFy",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 22985,
      "cache_read_input_tokens": 11841,
      "output_tokens": 330,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 22985,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 330,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 22985,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 22985
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

_source line 10 · 2026-05-16T02:24:38.352Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01EaZLZqADMW2HcxRkzX51qD`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__reconcile_crons,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__read_roadmap,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__main_agent_post_to_director,mcp__agent-ml-research__spawn_worker,mcp__agent-ml-research__send_progress",
  "max_results": 10
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "05cc09e6-525a-4b1d-834b-113eaf7baa72",
  "isSidechain": false,
  "requestId": "req_011Cb5TGuTMmWwhMozk5yid5",
  "type": "assistant",
  "uuid": "13638ff1-2b1f-4a5e-be3b-a7a9c469fb5d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/agent_e1f64cd5",
  "sessionId": "4f6074eb-8665-49ec-9526-07c9eebcea03",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017fD9xTnS4UdzRfP4iWDZFy",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 22985,
      "cache_read_input_tokens": 11841,
      "output_tokens": 330,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 22985,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 330,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 22985,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 22985
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

_source line 11 · 2026-05-16T02:24:38.358Z_

<details><summary>↩ Tool result · `toolu_01EaZLZqADMW2HcxRkzX51qD`</summary>

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
  "tool_name": "mcp__agent-ml-research__main_agent_post_to_director"
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
  "tool_name": "mcp__agent-ml-research__send_progress"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "13638ff1-2b1f-4a5e-be3b-a7a9c469fb5d",
  "isSidechain": false,
  "promptId": "a304cee9-feed-4fb2-a028-8ae1d93109aa",
  "type": "user",
  "uuid": "d8c034f2-b8c0-4f26-83be-3d74d63ad9b0",
  "toolUseResult": {
    "matches": [
      "mcp__agent-ml-research__read_registry",
      "mcp__agent-ml-research__reconcile_crons",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__read_roadmap",
      "mcp__agent-ml-research__update_registry",
      "mcp__agent-ml-research__main_agent_post_to_director",
      "mcp__agent-ml-research__spawn_worker",
      "mcp__agent-ml-research__send_progress"
    ],
    "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__reconcile_crons,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__read_roadmap,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__main_agent_post_to_director,mcp__agent-ml-research__spawn_worker,mcp__agent-ml-research__send_progress",
    "total_deferred_tools": 79
  },
  "sourceToolAssistantUUID": "13638ff1-2b1f-4a5e-be3b-a7a9c469fb5d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/agent_e1f64cd5",
  "sessionId": "4f6074eb-8665-49ec-9526-07c9eebcea03",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 12 · 2026-05-16T02:24:40.797Z_

执行 session-start 初始化。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d8c034f2-b8c0-4f26-83be-3d74d63ad9b0",
  "isSidechain": false,
  "requestId": "req_011Cb5THVYi5x3MbotvkQmr1",
  "type": "assistant",
  "uuid": "1eb2e4f8-8ba0-43c2-824a-b1b01e004a14",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/agent_e1f64cd5",
  "sessionId": "4f6074eb-8665-49ec-9526-07c9eebcea03",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DbAG94MdMh8gN9pNd7MbVZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 3204,
      "cache_read_input_tokens": 34826,
      "output_tokens": 271,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3204,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 271,
          "cache_read_input_tokens": 34826,
          "cache_creation_input_tokens": 3204,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3204
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

_source line 13 · 2026-05-16T02:24:41.749Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01BxadqtFPAy7HcgcjyPHhCs`</summary>

```json
{
  "project": "distrib_canary_collapse",
  "limit": 0,
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
  "parentUuid": "1eb2e4f8-8ba0-43c2-824a-b1b01e004a14",
  "isSidechain": false,
  "requestId": "req_011Cb5THVYi5x3MbotvkQmr1",
  "type": "assistant",
  "uuid": "ae37fdbe-6975-4d3d-aab1-cbae7f8aed59",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/agent_e1f64cd5",
  "sessionId": "4f6074eb-8665-49ec-9526-07c9eebcea03",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DbAG94MdMh8gN9pNd7MbVZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 3204,
      "cache_read_input_tokens": 34826,
      "output_tokens": 271,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3204,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 271,
          "cache_read_input_tokens": 34826,
          "cache_creation_input_tokens": 3204,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3204
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

_source line 14 · 2026-05-16T02:24:42.223Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__reconcile_crons · `toolu_012SkYJQZcdpD2hFxAzWhjD1`</summary>

```json
{}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ae37fdbe-6975-4d3d-aab1-cbae7f8aed59",
  "isSidechain": false,
  "requestId": "req_011Cb5THVYi5x3MbotvkQmr1",
  "type": "assistant",
  "uuid": "5ec36bd0-c86c-42c1-a9f2-fefd98aec14c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/agent_e1f64cd5",
  "sessionId": "4f6074eb-8665-49ec-9526-07c9eebcea03",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DbAG94MdMh8gN9pNd7MbVZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 3204,
      "cache_read_input_tokens": 34826,
      "output_tokens": 271,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3204,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 271,
          "cache_read_input_tokens": 34826,
          "cache_creation_input_tokens": 3204,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3204
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

_source line 15 · 2026-05-16T02:24:42.156Z_

<details><summary>↩ Tool result · `toolu_01BxadqtFPAy7HcgcjyPHhCs`</summary>

```text
&lt;persisted-output>
Output too large (52.7KB). Full output saved to: /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-4-projects-distrib-canary-collapse--claude-sessions-agent-e1f64cd5/4f6074eb-8665-49ec-9526-07c9eebcea03/tool-results/toolu_01BxadqtFPAy7HcgcjyPHhCs.txt

Preview (first 2KB):
{"result":"{\"success\": true, \"data\": {\"experiments\": {\"alpha_sweep_a025_s44\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-15T06:58:48.224Z\", \"updated_at\": \"2026-05-16T02:24:25.189Z\", \"spec\": {\"command\": \"bash -c \\\"cd /root/autodl-tmp/distrib_canary_collapse && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_HUB_DISABLE_XET=1 && export HF_ENDPOINT=https://hf-mirror.com && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && PYTHONUNBUFFERED=1 python -u iterative_train.py --seed 44 --data_dir data/wikitext103_5k --steps_per_gen 5000 --num_generations 10 --synthetic_ratio 0.25 --output_dir results/alpha_sweep/a025_s44\\\"\", \"server\": \"westd-19828\", \"gpu\": [\"cuda:1\"], \"pid\": \"147811\", \"log_path\": \"~/runs/distrib_canary_collapse/alpha_sweep_a025_s44.log\", \"submitted_at\": \"2026-05-15T22:04:28.318Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"server\": \"westd-19828\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-19828\", \"gpu\": \"cuda:1\", \"started_at\": \"2026-05-15T22:04:26.677Z\", \"command\": \"bash -c \\\"cd /root/autodl-tmp/distrib_canary_collapse && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_HUB_DISABLE_XET=1 && export HF_ENDPOINT=https://hf-mirror.com && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && PYTHONUNBUFFERED=1 python -u iterative_train.py --seed 44 --data_dir data/wikitext103_5k --steps_per_gen 5000 --num_generations 10 --synthetic_ratio 0.25 --output_dir results/alpha_sweep/a025_s44\\\"\", \"finished_at\": \"2026-05-16T02:24:25.056Z\", \"training_hours\": 4.33}, \"pid\": \"147811\", \"log_path
...
&lt;/persisted-output>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ae37fdbe-6975-4d3d-aab1-cbae7f8aed59",
  "isSidechain": false,
  "promptId": "a304cee9-feed-4fb2-a028-8ae1d93109aa",
  "type": "user",
  "uuid": "7b5c18e8-3f88-41a2-aab6-2d99aa199d56",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {\\\"alpha_sweep_a025_s44\\\": {\\\"status\\\": \\\"ANALYZING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-15T06:58:48.224Z\\\", \\\"updated_at\\\": \\\"2026-05-16T02:24:25.189Z\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"cd /root/autodl-tmp/distrib_canary_collapse && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_HUB_DISABLE_XET=1 && export HF_ENDPOINT=https://hf-mirror.com && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && PYTHONUNBUFFERED=1 python -u iterative_train.py --seed 44 --data_dir data/wikitext103_5k --steps_per_gen 5000 --num_generations 10 --synthetic_ratio 0.25 --output_dir results/alpha_sweep/a025_s44\\\\\\\"\\\", \\\"server\\\": \\\"westd-19828\\\", \\\"gpu\\\": [\\\"cuda:1\\\"], \\\"pid\\\": \\\"147811\\\", \\\"log_path\\\": \\\"~/runs/distrib_canary_collapse/alpha_sweep_a025_s44.log\\\", \\\"submitted_at\\\": \\\"2026-05-15T22:04:28.318Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\"}, \\\"server\\\": \\\"westd-19828\\\", \\\"gpu\\\": \\\"cuda:1\\\", \\\"account\\\": \\\"root\\\", \\\"reproduce\\\": {\\\"server\\\": \\\"westd-19828\\\", \\\"gpu\\\": \\\"cuda:1\\\", \\\"started_at\\\": \\\"2026-05-15T22:04:26.677Z\\\", \\\"command\\\": \\\"bash -c \\\\\\\"cd /root/autodl-tmp/distrib_canary_collapse && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_HUB_DISABLE_XET=1 && export HF_ENDPOINT=https://hf-mirror.com && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && PYTHONUNBUFFERED=1 python -u iterative_train.py --seed 44 --data_dir data/wikitext103_5k --steps_per_gen 5000 --num_generations 10 --synthetic_ratio 0.25 --output_dir results/alpha_sweep/a025_s44\\\\\\\"\\\", \\\"finished_at\\\": \\\"2026-05-16T02:24:25.056Z\\\", \\\"training_hours\\\": 4.33}, \\\"pid\\\": \\\"147811\\\", \\\"log_path\\\": \\\"~/runs/distrib_canary_collapse/alpha_sweep_a025_s44.log\\\", \\\"extra\\\": {\\\"hook_events\\\": [{\\\"event\\\": \\\"on_complete\\\", \\\"action\\\": \\\"agent\\\", \\\"ts\\\": \\\"2026-05-16T02:24:26.614491+00:00\\\"}]}}, \\\"mvp_v2_rep44\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-14T05:38:10.762Z\\\", \\\"updated_at\\\": \\\"2026-05-16T00:10:26.251Z\\\", \\\"spec\\\": {\\\"hypothesis\\\": \\\"至少一族canary指标在100% SC full replacement下对downstream指标有≥1 gen的时序领先性\\\", \\\"model_name\\\": \\\"EleutherAI/pythia-410m\\\", \\\"data_path\\\": \\\"/root/autodl-tmp/distrib_canary_collapse/data/wikitext103\\\", \\\"data_count\\\": 5000, \\\"seed\\\": 44, \\\"server\\\": \\\"autodl-rtx6000\\\", \\\"gpu\\\": \\\"pending\\\", \\\"synthetic_ratio\\\": 1, \\\"num_generations\\\": 10, \\\"steps_per_gen\\\": 5000, \\\"n_prompts\\\": 5000, \\\"fix_note\\\": \\\"n_prompts 1000→5000, steps_per_gen 10000→5000, 避免过拟合\\\"}, \\\"conclusion\\\": \\\"killed\\\", \\\"completed_at\\\": \\\"2026-05-16T00:10:26.251Z\\\"}, \\\"mvp_rep44\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-14T05:12:15.033Z\\\", \\\"updated_at\\\": \\\"2026-05-16T00:10:25.605Z\\\", \\\"spec\\\": {\\\"hypothesis\\\": \\\"至少一族canary指标在100% SC full replacement下对downstream指标有≥1 gen的时序领先性\\\", \\\"model_name\\\": \\\"EleutherAI/pythia-410m\\\", \\\"data_path\\\": \\\"/root/autodl-tmp/distrib_canary_collapse/data/wikitext103\\\", \\\"seed\\\": 44, \\\"server\\\": \\\"autodl-rtx6000\\\", \\\"gpu\\\": \\\"pending\\\", \\\"synthetic_ratio\\\": 1, \\\"num_generations\\\": 10, \\\"steps_per_gen\\\": 10000}, \\\"metrics\\\": {\\\"gen10_token_entropy\\\": 1.2205, \\\"gen10_ece\\\": 0.4237, \\\"gen10_perplexity\\\": 1033.16, \\\"gen10_distinct_1\\\": 0.0731, \\\"gen10_distinct_2\\\": 0.3637, \\\"gen10_distinct_3\\\": 0.6075}, \\\"conclusion\\\": \\\"killed\\\", \\\"completed_at\\\": \\\"2026-05-16T00:10:25.605Z\\\"}, \\\"alpha_sweep_a025_s42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-14T19:01:39.527Z\\\", \\\"updated_at\\\": \\\"2026-05-16T00:10:24.973Z\\\", \\\"spec\\\": {\\\"hypothesis\\\": \\\"α=0.25 低污染: 测试 canary→diversity lead 在温和 collapse 下是否保持，canary→perplexity lead 是否出现\\\", \\\"model_name\\\": \\\"EleutherAI/pythia-410m\\\", \\\"data_path\\\": \\\"/root/autodl-tmp/distrib_canary_collapse/data/wikitext103_5k\\\", \\\"data_count\\\": 5000, \\\"seed\\\": 42, \\\"synthetic_ratio\\\": 0.25, \\\"num_generations\\\": 10, \\\"steps_per_gen\\\": 5000}, \\\"conclusion\\\": \\\"killed\\\", \\\"completed_at\\\": \\\"2026-05-16T00:10:24.973Z\\\"}, \\\"alpha_sweep_a025_s42_v2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-14T19:25:52.094Z\\\", \\\"updated_at\\\": \\\"2026-05-16T00:10:24.568Z\\\", \\\"spec\\\": {\\\"hypothesis\\\": \\\"α=0.25 低污染: 测试 canary→diversity lead 在温和 collapse 下是否保持，canary→perplexity lead 是否出现\\\", \\\"model_name\\\": \\\"EleutherAI/pythia-410m\\\", \\\"data_path\\\": \\\"/root/autodl-tmp/distrib_canary_collapse/data/wikitext103_5k\\\", \\\"data_count\\\": 5000, \\\"seed\\\": 42, \\\"synthetic_ratio\\\": 0.25, \\\"num_generations\\\": 10, \\\"steps_per_gen\\\": 5000, \\\"parent\\\": \\\"alpha_sweep_a025_s42 (killed, subsample bias fix)\\\"}, \\\"conclusion\\\": \\\"killed\\\", \\\"failure_reason\\\": \\\"data corruption: unkilled old process PID 46802 wrote concurrently with new PID 48454\\\", \\\"completed_at\\\": \\\"2026-05-16T00:10:24.568Z\\\"}, \\\"alpha_sweep_a060_s42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-14T21:52:22.516Z\\\", \\\"updated_at\\\": \\\"2026-05-16T00:04:01.429Z\\\", \\\"spec\\\": {\\\"hypothesis\\\": \\\"α=0.60 中高污染: phase boundary 精确化, 与 α=0.50/0.75 对比 lead time 变化\\\", \\\"model_name\\\": \\\"EleutherAI/pythia-410m\\\", \\\"data_path\\\": \\\"/root/autodl-tmp/distrib_canary_collapse/data/wikitext103_5k\\\", \\\"data_count\\\": 5000, \\\"seed\\\": 42, \\\"synthetic_ratio\\\": 0.6, \\\"num_generations\\\": 10, \\\"steps_per_gen\\\": 5000}, \\\"conclusion\\\": \\\"killed\\\", \\\"completed_at\\\": \\\"2026-05-16T00:04:01.429Z\\\"}, \\\"alpha_sweep_a010_s42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-14T21:52:19.712Z\\\", \\\"updated_at\\\": \\\"2026-05-16T00:03:53.018Z\\\", \\\"spec\\\": {\\\"hypothesis\\\": \\\"α=0.10 极低污染: phase boundary 精确化, canary signal 是否仍可检测\\\", \\\"model_name\\\": \\\"EleutherAI/pythia-410m\\\", \\\"data_path\\\": \\\"/root/autodl-tmp/distrib_canary_collapse/data/wikitext103_5k\\\", \\\"data_count\\\": 5000, \\\"seed\\\": 42, \\\"synthetic_ratio\\\": 0.1, \\\"num_generations\\\": 10, \\\"steps_per_gen\\\": 5000}, \\\"conclusion\\\": \\\"killed\\\", \\\"completed_at\\\": \\\"2026-05-16T00:03:53.018Z\\\"}, \\\"alpha_sweep_a050_s44\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-15T06:58:50.550Z\\\", \\\"updated_at\\\": \\\"2026-05-16T00:03:52.118Z\\\", \\\"spec\\\": {\\\"hypothesis\\\": \\\"α=0.50 multi-seed replication (seed=44): 第三个 seed 为置信区间提供统计力\\\", \\\"model_name\\\": \\\"EleutherAI/pythia-410m\\\", \\\"data_path\\\": \\\"/root/autodl-tmp/distrib_canary_collapse/data/wikitext103_5k\\\", \\\"data_count\\\": 5000, \\\"seed\\\": 44, \\\"synthetic_ratio\\\": 0.5, \\\"num_generations\\\": 10, \\\"steps_per_gen\\\": 5000, \\\"parent\\\": \\\"alpha_sweep_a050_s42\\\", \\\"priority\\\": \\\"D026-4\\\"}, \\\"conclusion\\\": \\\"killed\\\", \\\"completed_at\\\": \\\"2026-05-16T00:03:52.118Z\\\"}, \\\"plan_006_s43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-14T23:31:37.257Z\\\", \\\"updated_at\\\": \\\"2026-05-16T00:03:51.617Z\\\", \\\"spec\\\": {\\\"plan_id\\\": \\\"plan_006\\\", \\\"hypothesis\\\": \\\"Multi-seed replication of three-phase collapse dynamics: verify Phase 3 secondary decline (gen 13+) reproduces with seed=43, confirming it is not a single-seed artifact\\\", \\\"model_name\\\": \\\"EleutherAI/pythia-410m\\\", \\\"seed\\\": 43, \\\"data_path\\\": \\\"data/wikitext103_5k\\\", \\\"num_generations\\\": 18, \\\"synthetic_ratio\\\": 1, \\\"max_lag\\\": 10, \\\"data_count\\\": 5000, \\\"steps_per_gen\\\": 5000, \\\"parent\\\": \\\"plan_006_s42\\\", \\\"claim\\\": 1, \\\"priority\\\": \\\"P0\\\"}, \\\"conclusion\\\": \\\"killed\\\", \\\"completed_at\\\": \\\"2026-05-16T00:03:51.617Z\\\"}, \\\"gen_wiki_gpt2m_a100_s42_v3\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-15T12:07:20.050Z\\\", \\\"updated_at\\\": \\\"2026-05-15T22:30:21.573Z\\\", \\\"spec\\\": {\\\"hypothesis\\\": \\\"Method sensitivity patterns (Granger FDR collapse, cross-correlation dominance) generalize from GPT-2-small to GPT-2-medium, validating cross-architecture universality of methodological pitfalls\\\", \\\"seed\\\": 42, \\\"model_name\\\": \\\"gpt2-medium\\\", \\\"data_path\\\": \\\"data/wikitext103_5k\\\", \\\"data_count\\\": 5000}, \\\"server\\\": \\\"westd-19828\\\", \\\"gpu\\\": \\\"cuda:0\\\", \\\"account\\\": \\\"root\\\", \\\"reproduce\\\": {\\\"server\\\": \\\"westd-19828\\\", \\\"gpu\\\": \\\"cuda:0\\\", \\\"started_at\\\": \\\"2026-05-15T12:07:30.366Z\\\", \\\"command\\\": \\\"bash -c \\\\\\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && mkdir -p results/gen_wiki_gpt2m_a100_s42 && HF_HOME=/root/autodl-tmp/.hf_cache TRANSFORMERS_OFFLINE=1 HF_HUB_DISABLE_XET=1 PYTHONUNBUFFERED=1 python -u iterative_train.py --model_name gpt2-medium --data_dir data/wikitext103_5k --synthetic_ratio 1.0 --num_generations 10 --steps_per_gen 5000 --batch_size 32 --seed 42 --output_dir results/gen_wiki_gpt2m_a100_s42\\\\\\\"\\\", \\\"finished_at\\\": \\\"2026-05-15T22:14:43.852Z\\\", \\\"training_hours\\\": 10.12}, \\\"pid\\\": \\\"117632\\\", \\\"log_path\\\": \\\"~/runs/distrib_canary_collapse/gen_wiki_gpt2m_a100_s42_v3.log\\\", \\\"metrics\\\": {\\\"token_entropy_drift_pct\\\": -86.5, \\\"ece_drift_pct\\\": 4543, \\\"perplexity_drift_pct\\\": 44703, \\\"distinct_1_drift_pct\\\": -12.4, \\\"distinct_2_drift_pct\\\": -14.7, \\\"distinct_3_drift_pct\\\": -12.7, \\\"five_method_forward_consensus\\\": \\\"6/6 pairs at 4/5 methods (Tier 3)\\\", \\\"five_method_reverse_consensus\\\": \\\"0/6 pairs\\\", \\\"naive_xcorr_forward\\\": \\\"|r|>0.98, all sig\\\", \\\"diff_xcorr_forward\\\": \\\"all p_fdr<0.001\\\", \\\"diff_xcorr_reverse\\\": \\\"all p>0.18 (clean directional separation)\\\", \\\"threshold_onset_entropy\\\": \\\"gen 1 (earliest canary)\\\", \\\"threshold_onset_ece\\\": \\\"gen 1-2\\\", \\\"threshold_onset_diversity\\\": \\\"gen 3\\\", \\\"perm_granger_forward\\\": \\\"p_fdr=0.003, BH corrected\\\", \\\"ty_granger_forward\\\": \\\"0/6 sig (df_resid=1-4, underpowered, consistent with Pythia C001)\\\", \\\"entropy_leads_diversity_lag\\\": \\\"1-2 gen\\\", \\\"ece_leads_diversity_lag\\\": \\\"1 gen\\\", \\\"diversity_plateau_from\\\": \\\"gen5\\\", \\\"cross_arch_note\\\": \\\"Replicates Pythia entropy-leads-diversity pattern at Tier 3 consensus. TY underpowered as expected.\\\"}, \\\"extra\\\": {\\\"hook_events\\\": [{\\\"event\\\": \\\"on_complete\\\", \\\"action\\\": \\\"agent\\\", \\\"ts\\\": \\\"2026-05-15T22:14:45.029003+00:00\\\"}]}, \\\"conclusion\\\": \\\"success\\\", \\\"checkpoint_path\\\": \\\"results/gen_wiki_gpt2m_a100_s42/\\\", \\\"completed_at\\\": \\\"2026-05-15T22:18:22.762Z\\\"}, \\\"gen_wiki_gpt2m_a025_s42\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-15T10:35:16.032Z\\\", \\\"updated_at\\\": \\\"2026-05-15T22:22:52.921Z\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && mkdir -p results/gen_wiki_gpt2m_a025_s42 && HF_HOME=/root/autodl-tmp/.hf_cache TRANSFORMERS_OFFLINE=1 HF_HUB_DISABLE_XET=1 PYTHONUNBUFFERED=1 python -u iterative_train.py --model_name gpt2-medium --data_dir data/wikitext103_5k --synthetic_ratio 0.25 --num_generations 10 --steps_per_gen 5000 --batch_size 32 --seed 42 --output_dir results/gen_wiki_gpt2m_a025_s42\\\\\\\"\\\", \\\"server\\\": \\\"westd-19828\\\", \\\"gpu\\\": [\\\"cuda:0\\\"], \\\"pid\\\": \\\"149202\\\", \\\"log_path\\\": \\\"~/runs/distrib_canary_collapse/gen_wiki_gpt2m_a025_s42.log\\\", \\\"submitted_at\\\": \\\"2026-05-15T22:22:52.615Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\"}, \\\"server\\\": \\\"westd-19828\\\", \\\"gpu\\\": \\\"cuda:0\\\", \\\"account\\\": \\\"root\\\", \\\"reproduce\\\": {\\\"server\\\": \\\"westd-19828\\\", \\\"gpu\\\": \\\"cuda:0\\\", \\\"started_at\\\": \\\"2026-05-15T22:22:51.021Z\\\", \\\"command\\\": \\\"bash -c \\\\\\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && mkdir -p results/gen_wiki_gpt2m_a025_s42 && HF_HOME=/root/autodl-tmp/.hf_cache TRANSFORMERS_OFFLINE=1 HF_HUB_DISABLE_XET=1 PYTHONUNBUFFERED=1 python -u iterative_train.py --model_name gpt2-medium --data_dir data/wikitext103_5k --synthetic_ratio 0.25 --num_generations 10 --steps_per_gen 5000 --batch_size 32 --seed 42 --output_dir results/gen_wiki_gpt2m_a025_s42\\\\\\\"\\\"}, \\\"pid\\\": \\\"149202\\\", \\\"log_path\\\": \\\"~/runs/distrib_canary_collapse/gen_wiki_gpt2m_a025_s42.log\\\"}, \\\"alpha_sweep_a050_s43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-15T06:58:45.880Z\\\", \\\"updated_at\\\": \\\"2026-05-15T22:15:50.290Z\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"cd /root/autodl-tmp/distrib_canary_collapse && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_HUB_DISABLE_XET=1 && export HF_ENDPOINT=https://hf-mirror.com && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && PYTHONUNBUFFERED=1 python -u iterative_train.py --seed 43 --data_dir data/wikitext103_5k --steps_per_gen 5000 --num_generations 10 --synthetic_ratio 0.50 --output_dir results/alpha_sweep/a050_s43\\\\\\\"\\\", \\\"server\\\": \\\"westd-19828\\\", \\\"gpu\\\": [\\\"cuda:1\\\"], \\\"pid\\\": \\\"134860\\\", \\\"log_path\\\": \\\"~/runs/distrib_canary_collapse/alpha_sweep_a050_s43.log\\\", \\\"submitted_at\\\": \\\"2026-05-15T17:40:27.060Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"wall_clock_seconds\\\": 16523.2, \\\"gpu_hours\\\": 4.59}, \\\"server\\\": \\\"westd-19828\\\", \\\"gpu\\\": \\\"cuda:1\\\", \\\"pid\\\": \\\"134860\\\", \\\"log_path\\\": \\\"~/runs/distrib_canary_collapse/alpha_sweep_a050_s43.log\\\", \\\"reproduce\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"cd /root/autodl-tmp/distrib_canary_collapse && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_HUB_DISABLE_XET=1 && export HF_ENDPOINT=https://hf-mirror.com && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && PYTHONUNBUFFERED=1 python -u iterative_train.py --seed 43 --data_dir data/wikitext103_5k --steps_per_gen 5000 --num_generations 10 --synthetic_ratio 0.50 --output_dir results/alpha_sweep/a050_s43\\\\\\\"\\\", \\\"finished_at\\\": \\\"2026-05-15T22:00:14.725Z\\\"}, \\\"extra\\\": {\\\"hook_events\\\": [{\\\"event\\\": \\\"on_complete\\\", \\\"action\\\": \\\"agent\\\", \\\"ts\\\": \\\"2026-05-15T22:00:15.908424+00:00\\\"}]}, \\\"conclusion\\\": \\\"success\\\", \\\"checkpoint_path\\\": \\\"results/alpha_sweep/a050_s43/gen_10/checkpoint/\\\", \\\"metrics\\\": {\\\"gen0_token_entropy\\\": 3.234195, \\\"gen0_ece\\\": 0.010805, \\\"gen0_perplexity\\\": 26.948959, \\\"gen10_token_entropy\\\": 2.672, \\\"gen10_ece\\\": 0.097, \\\"gen10_perplexity\\\": 32.633, \\\"gen0_distinct_1\\\": 0.09833, \\\"gen0_distinct_2\\\": 0.5132, \\\"gen0_distinct_3\\\": 0.8057, \\\"gen10_distinct_1\\\": 0.0624, \\\"gen10_distinct_2\\\": 0.2617, \\\"gen10_distinct_3\\\": 0.4126, \\\"token_entropy_drift_pct\\\": -17.4, \\\"ece_drift_pct\\\": 799, \\\"perplexity_drift_pct\\\": 21.1, \\\"distinct_1_drift_pct\\\": -36.5, \\\"distinct_2_drift_pct\\\": -49, \\\"distinct_3_drift_pct\\\": -48.8, \\\"cross_seed_note\\\": \\\"vs s42: drift direction identical, magnitude <7% deviation, ppl near-identical (32.633 vs 32.64)\\\"}, \\\"completed_at\\\": \\\"2026-05-15T22:00:14Z\\\"}, \\\"mvp_v4_rep45\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-14T13:41:26.286Z\\\", \\\"updated_at\\\": \\\"2026-05-15T21:29:54.928Z\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"cd /root/autodl-tmp/distrib_canary_collapse && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_HUB_DISABLE_XET=1 && export HF_ENDPOINT=https://hf-mirror.com && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && PYTHONUNBUFFERED=1 python -u iterative_train.py --seed 45 --data_dir data/wikitext103_5k --steps_per_gen 5000 --num_generations 10 --output_dir results/mvp/rep_45\\\\\\\"\\\", \\\"server\\\": \\\"westd-19828\\\", \\\"gpu\\\": [\\\"cuda:1\\\"], \\\"pid\\\": \\\"31425\\\", \\\"log_path\\\": \\\"~/runs/distrib_canary_collapse/mvp_v4_rep45.log\\\", \\\"submitted_at\\\": \\\"2026-05-14T13:42:10.455Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"data_path\\\": \\\"/root/autodl-tmp/distrib_canary_collapse/data/wikitext103_5k\\\", \\\"data_count\\\": 5000, \\\"model_name\\\": \\\"EleutherAI/pythia-410m\\\", \\\"seed\\\": 45, \\\"wall_clock_seconds\\\": 15350.2, \\\"gpu_hours\\\": 4.26}, \\\"reproduce\\\": {\\\"finished_at\\\": \\\"2026-05-14T17:55:42.230Z\\\"}, \\\"extra\\\": {\\\"hook_events\\\": [{\\\"event\\\": \\\"on_complete\\\", \\\"action\\\": \\\"agent\\\", \\\"ts\\\": \\\"2026-05-14T17:55:42.934182+00:00\\\"}]}, \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/distrib_canary_collapse/results/mvp/rep_45/gen_10/checkpoint\\\", \\\"metrics_summary\\\": {\\\"gen0_ppl\\\": 26.9, \\\"gen10_ppl\\\": 1016.2, \\\"gen0_entropy\\\": 3.234, \\\"gen10_entropy\\\": 1.315, \\\"gen0_ece\\\": 0.011, \\\"gen10_ece\\\": 0.417}, \\\"wall_clock_seconds\\\": 15212, \\\"gpu_hours\\\": 4.23, \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"gen0_token_entropy\\\": 3.234195, \\\"gen0_ece\\\": 0.010805, \\\"gen0_perplexity\\\": 26.948959, \\\"gen0_distinct_1\\\": 0.098574, \\\"gen0_distinct_2\\\": 0.51463, \\\"gen0_distinct_3\\\": 0.808362, \\\"gen10_token_entropy\\\": 1.31536, \\\"gen10_ece\\\": 0.41654, \\\"gen10_perplexity\\\": 1016.22, \\\"gen10_distinct_1\\\": 0.069859, \\\"gen10_distinct_2\\\": 0.329549, \\\"gen10_distinct_3\\\": 0.543743, \\\"token_entropy_drift_pct\\\": -59.3296, \\\"ece_drift_pct\\\": 3755.0671, \\\"perplexity_drift_pct\\\": 3670.9063, \\\"distinct_1_drift_pct\\\": -29.1304, \\\"distinct_2_drift_pct\\\": -35.9639, \\\"distinct_3_drift_pct\\\": -32.7352}, \\\"completed_at\\\": \\\"2026-05-14T17:58:00.661Z\\\"}, \\\"mvp_v4_rep44\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-14T07:48:52.613Z\\\", \\\"updated_at\\\": \\\"2026-05-15T21:29:52.398Z\\\", \\\"spec\\\": {\\\"hypothesis\\\": \\\"至少一族canary指标在100% SC full replacement下对downstream指标有≥1 gen的时序领先性\\\", \\\"model_name\\\": \\\"EleutherAI/pythia-410m\\\", \\\"data_path\\\": \\\"/root/autodl-tmp/distrib_canary_collapse/data/wikitext103_5k\\\", \\\"data_count\\\": 5000, \\\"seed\\\": 44, \\\"server\\\": \\\"westd-19828\\\", \\\"gpu\\\": \\\"cuda:0\\\", \\\"synthetic_ratio\\\": 1, \\\"num_generations\\\": 10, \\\"steps_per_gen\\\": 5000, \\\"n_prompts\\\": 5000, \\\"command\\\": \\\"PYTHONUNBUFFERED=1 CUDA_VISIBLE_DEVICES=0 python -u iterative_train.py --seed 44 --data_dir data/wikitext103_5k --steps_per_gen 5000 --num_generations 10 --output_dir results/mvp/rep_44\\\", \\\"pid\\\": \\\"30672\\\", \\\"log_path\\\": \\\"~/runs/distrib_canary_collapse/mvp_v4_rep44.log\\\"}, \\\"reproduce\\\": {\\\"finished_at\\\": \\\"2026-05-14T17:56:00.578Z\\\"}, \\\"failure_reason\\\": \\\"\\\", \\\"conclusion\\\": \\\"success\\\", \\\"completed_at\\\": \\\"2026-05-14T17:56:00.717Z\\\", \\\"extra\\\": {\\\"hook_events\\\": [{\\\"event\\\": \\\"on_failed\\\", \\\"action\\\": \\\"agent\\\", \\\"ts\\\": \\\"2026-05-14T17:56:03.546926+00:00\\\"}]}, \\\"metrics_summary\\\": {\\\"gen0_ppl\\\": 26.9, \\\"gen10_ppl\\\": 1033.16, \\\"gen0_entropy\\\": 3.234, \\\"gen10_entropy\\\": 1.2205, \\\"gen0_ece\\\": 0.011, \\\"gen10_ece\\\": 0.424}, \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/distrib_canary_collapse/results/mvp/rep_44/gen_10/checkpoint\\\", \\\"wall_clock_seconds\\\": 15134, \\\"gpu_hours\\\": 4.2, \\\"metrics\\\": {\\\"gen0_token_entropy\\\": 3.234195, \\\"gen0_ece\\\": 0.010805, \\\"gen0_perplexity\\\": 26.948959, \\\"gen0_distinct_1\\\": 0.098088, \\\"gen0_distinct_2\\\": 0.513235, \\\"gen0_distinct_3\\\": 0.805767, \\\"gen10_token_entropy\\\": 1.22049, \\\"gen10_ece\\\": 0.42369, \\\"gen10_perplexity\\\": 1033.16, \\\"gen10_distinct_1\\\": 0.073102, \\\"gen10_distinct_2\\\": 0.363737, \\\"gen10_distinct_3\\\": 0.607502, \\\"token_entropy_drift_pct\\\": -62.2629, \\\"ece_drift_pct\\\": 3821.2402, \\\"perplexity_drift_pct\\\": 3733.7659, \\\"distinct_1_drift_pct\\\": -25.473, \\\"distinct_2_drift_pct\\\": -29.1286, \\\"distinct_3_drift_pct\\\": -24.6057}}, \\\"mvp_v4_rep43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-14T07:48:50.161Z\\\", \\\"updated_at\\\": \\\"2026-05-15T21:29:49.565Z\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"cd /root/autodl-tmp/distrib_canary_collapse && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_HUB_DISABLE_XET=1 && export HF_ENDPOINT=https://hf-mirror.com && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && PYTHONUNBUFFERED=1 python -u iterative_train.py --seed 43 --data_dir data/wikitext103_5k --steps_per_gen 5000 --num_generations 10 --output_dir results/mvp/rep_43\\\\\\\"\\\", \\\"server\\\": \\\"westd-19828\\\", \\\"gpu\\\": [\\\"cuda:1\\\"], \\\"pid\\\": \\\"13758\\\", \\\"log_path\\\": \\\"~/runs/distrib_canary_collapse/mvp_v4_rep43.log\\\", \\\"submitted_at\\\": \\\"2026-05-14T07:51:36.759Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/distrib_canary_collapse/results/mvp/rep_43/gen_10/checkpoint\\\", \\\"metrics_summary\\\": {\\\"gen0_ppl\\\": 26.9, \\\"gen10_ppl\\\": 1014.7, \\\"gen0_entropy\\\": 3.234, \\\"gen10_entropy\\\": 1.26, \\\"gen0_ece\\\": 0.011, \\\"gen10_ece\\\": 0.42}, \\\"wall_clock_seconds\\\": 20897.7, \\\"gpu_hours\\\": 5.8}, \\\"conclusion\\\": \\\"success\\\", \\\"completed_at\\\": \\\"2026-05-14T13:39:54.495Z\\\", \\\"metrics\\\": {\\\"gen0_token_entropy\\\": 3.234195, \\\"gen0_ece\\\": 0.010805, \\\"gen0_perplexity\\\": 26.948959, \\\"gen0_distinct_1\\\": 0.098334, \\\"gen0_distinct_2\\\": 0.513178, \\\"gen0_distinct_3\\\": 0.805669, \\\"gen10_token_entropy\\\": 1.25961, \\\"gen10_ece\\\": 0.41951, \\\"gen10_perplexity\\\": 1014.66, \\\"gen10_distinct_1\\\": 0.070383, \\\"gen10_distinct_2\\\": 0.329651, \\\"gen10_distinct_3\\\": 0.539571, \\\"token_entropy_drift_pct\\\": -61.0534, \\\"ece_drift_pct\\\": 3782.5544, \\\"perplexity_drift_pct\\\": 3665.1176, \\\"distinct_1_drift_pct\\\": -28.4246, \\\"distinct_2_drift_pct\\\": -35.7628, \\\"distinct_3_drift_pct\\\": -33.0282}}, \\\"mvp_v4_rep42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-14T07:29:48.857Z\\\", \\\"updated_at\\\": \\\"2026-05-15T21:29:47.171Z\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"cd /root/autodl-tmp/distrib_canary_collapse && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_HUB_DISABLE_XET=1 && export HF_ENDPOINT=https://hf-mirror.com && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && PYTHONUNBUFFERED=1 python -u iterative_train.py --seed 42 --data_dir data/wikitext103_5k --steps_per_gen 5000 --num_generations 10 --output_dir results/mvp/rep_42\\\\\\\"\\\", \\\"server\\\": \\\"westd-19828\\\", \\\"gpu\\\": [\\\"cuda:0\\\"], \\\"pid\\\": \\\"13678\\\", \\\"log_path\\\": \\\"~/runs/distrib_canary_collapse/mvp_v4_rep42.log\\\", \\\"submitted_at\\\": \\\"2026-05-14T07:51:34.806Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/distrib_canary_collapse/results/mvp/rep_42/gen_10/checkpoint\\\", \\\"metrics_summary\\\": {\\\"gen0_ppl\\\": 26.9, \\\"gen10_ppl\\\": 1003.7, \\\"gen0_entropy\\\": 3.234, \\\"gen10_entropy\\\": 1.276, \\\"gen0_ece\\\": 0.011, \\\"gen10_ece\\\": 0.417}, \\\"wall_clock_seconds\\\": 20898.3, \\\"gpu_hours\\\": 5.81}, \\\"conclusion\\\": \\\"success\\\", \\\"completed_at\\\": \\\"2026-05-14T13:39:53.073Z\\\", \\\"metrics\\\": {\\\"gen0_token_entropy\\\": 3.234195, \\\"gen0_ece\\\": 0.010805, \\\"gen0_perplexity\\\": 26.948959, \\\"gen0_distinct_1\\\": 0.098216, \\\"gen0_distinct_2\\\": 0.517803, \\\"gen0_distinct_3\\\": 0.812728, \\\"gen10_token_entropy\\\": 1.27592, \\\"gen10_ece\\\": 0.41734, \\\"gen10_perplexity\\\": 1003.73, \\\"gen10_distinct_1\\\": 0.070383, \\\"gen10_distinct_2\\\": 0.335471, \\\"gen10_distinct_3\\\": 0.555579, \\\"token_entropy_drift_pct\\\": -60.5491, \\\"ece_drift_pct\\\": 3762.4711, \\\"perplexity_drift_pct\\\": 3624.5595, \\\"distinct_1_drift_pct\\\": -28.3386, \\\"distinct_2_drift_pct\\\": -35.2126, \\\"distinct_3_drift_pct\\\": -31.6402}}, \\\"alpha_sweep_a025_s43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-15T06:58:43.090Z\\\", \\\"updated_at\\\": \\\"2026-05-15T17:39:43.623Z\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"cd /root/autodl-tmp/distrib_canary_collapse && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_HUB_DISABLE_XET=1 && export HF_ENDPOINT=https://hf-mirror.com && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && PYTHONUNBUFFERED=1 python -u iterative_train.py --seed 43 --data_dir data/wikitext103_5k --steps_per_gen 5000 --num_generations 10 --synthetic_ratio 0.25 --output_dir results/alpha_sweep/a025_s43\\\\\\\"\\\", \\\"server\\\": \\\"westd-19828\\\", \\\"gpu\\\": [\\\"cuda:1\\\"], \\\"pid\\\": \\\"121635\\\", \\\"log_path\\\": \\\"~/runs/distrib_canary_collapse/alpha_sweep_a025_s43.log\\\", \\\"submitted_at\\\": \\\"2026-05-15T13:16:31.189Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"wall_clock_seconds\\\": 15792.4, \\\"gpu_hours\\\": 4.39}, \\\"server\\\": \\\"westd-19828\\\", \\\"gpu\\\": \\\"cuda:1\\\", \\\"pid\\\": \\\"121635\\\", \\\"log_path\\\": \\\"~/runs/distrib_canary_collapse/alpha_sweep_a025_s43.log\\\", \\\"reproduce\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"cd /root/autodl-tmp/distrib_canary_collapse && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_HUB_DISABLE_XET=1 && export HF_ENDPOINT=https://hf-mirror.com && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && PYTHONUNBUFFERED=1 python -u iterative_train.py --seed 43 --data_dir data/wikitext103_5k --steps_per_gen 5000 --num_generations 10 --synthetic_ratio 0.25 --output_dir results/alpha_sweep/a025_s43\\\\\\\"\\\", \\\"finished_at\\\": \\\"2026-05-15T17:36:20.945Z\\\"}, \\\"metrics\\\": {\\\"gen0\\\": {\\\"token_entropy\\\": 3.2342, \\\"ece\\\": 0.0108, \\\"perplexity\\\": 26.949, \\\"distinct_1\\\": 0.09833, \\\"distinct_2\\\": 0.5132, \\\"distinct_3\\\": 0.8057, \\\"effective_rank\\\": 46.61, \\\"mauve\\\": 0.03351}, \\\"gen10\\\": {\\\"token_entropy\\\": 3.0723, \\\"ece\\\": 0.02146, \\\"perplexity\\\": 21.899, \\\"distinct_1\\\": 0.05849, \\\"distinct_2\\\": 0.2236, \\\"distinct_3\\\": 0.333, \\\"effective_rank\\\": 45.37, \\\"mauve\\\": 0.01871}, \\\"drift_pct\\\": {\\\"token_entropy\\\": -5, \\\"ece\\\": 98.6, \\\"perplexity\\\": -18.7, \\\"distinct_1\\\": -40.5, \\\"distinct_2\\\": -56.4, \\\"distinct_3\\\": -58.7, \\\"effective_rank\\\": -2.7, \\\"mauve\\\": -44.2}}, \\\"extra\\\": {\\\"hook_events\\\": [{\\\"event\\\": \\\"on_complete\\\", \\\"action\\\": \\\"agent\\\", \\\"ts\\\": \\\"2026-05-15T17:36:22.072334+00:00\\\"}]}, \\\"conclusion\\\": \\\"success\\\", \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a025_s43/gen_10/checkpoint\\\", \\\"completed_at\\\": \\\"2026-05-15T17:39:43.624Z\\\"}, \\\"alpha_sweep_a075_s42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-14T21:52:17.315Z\\\", \\\"updated_at\\\": \\\"2026-05-15T13:29:46.421Z\\\", \\\"spec\\\": {\\\"hypothesis\\\": \\\"α=0.75 high contamination: critical boundary point for Granger-causal detectability — determines Claim 1 scope (α≥0.75 vs α=1.0 only)\\\", \\\"seed\\\": 42, \\\"model_name\\\": \\\"EleutherAI/pythia-410m\\\", \\\"data_path\\\": \\\"data/wikitext103_5k\\\", \\\"data_count\\\": 5000, \\\"synthetic_ratio\\\": 0.75, \\\"num_generations\\\": 10, \\\"steps_per_gen\\\": 5000}, \\\"server\\\": \\\"westd-19828\\\", \\\"gpu\\\": \\\"cuda:1\\\", \\\"account\\\": \\\"root\\\", \\\"reproduce\\\": {\\\"server\\\": \\\"westd-19828\\\", \\\"gpu\\\": \\\"cuda:1\\\", \\\"started_at\\\": \\\"2026-05-15T05:44:46.271Z\\\", \\\"command\\\": \\\"bash -c \\\\\\\"cd /root/autodl-tmp/distrib_canary_collapse && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_HUB_DISABLE_XET=1 && export HF_ENDPOINT=https://hf-mirror.com && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && PYTHONUNBUFFERED=1 python -u iterative_train.py --seed 42 --data_dir data/wikitext103_5k --steps_per_gen 5000 --num_generations 10 --synthetic_ratio 0.75 --output_dir results/alpha_sweep/a075_s42\\\\\\\"\\\", \\\"finished_at\\\": \\\"2026-05-15T13:13:06.477Z\\\", \\\"training_hours\\\": 7.47}, \\\"pid\\\": \\\"89753\\\", \\\"log_path\\\": \\\"results/analysis/cross_alpha_v6_report.md\\\", \\\"metrics\\\": {\\\"progress\\\": \\\"11/11 gen (complete)\\\", \\\"gen0_token_entropy\\\": 3.234, \\\"gen10_token_entropy\\\": 2.337, \\\"gen0_ece\\\": 0.0108, \\\"gen10_ece\\\": 0.2063, \\\"gen0_perplexity\\\": 26.95, \\\"gen10_perplexity\\\": 76.03, \\\"gen0_distinct_1\\\": 0.0982, \\\"gen10_distinct_1\\\": 0.0661, \\\"gen0_distinct_2\\\": 0.5178, \\\"gen10_distinct_2\\\": 0.3037, \\\"gen0_distinct_3\\\": 0.8127, \\\"gen10_distinct_3\\\": 0.5011, \\\"token_entropy_drift_pct\\\": -27.7, \\\"ece_drift_pct\\\": 1809.5, \\\"perplexity_drift_pct\\\": 182.1, \\\"distinct_1_drift_pct\\\": -32.7, \\\"distinct_2_drift_pct\\\": -41.3, \\\"distinct_3_drift_pct\\\": -38.4, \\\"granger_ece_to_d1_p_fdr\\\": 0.046, \\\"granger_ece_to_d2_p_fdr\\\": 0.046, \\\"granger_entropy_to_d2_p_fdr\\\": 0.048, \\\"granger_entropy_to_d1_p_fdr\\\": 0.054, \\\"granger_fdr_sig_count\\\": \\\"3/8\\\", \\\"consensus_robust_pairs\\\": \\\"11/16\\\", \\\"xcorr_entropy_d1_lag\\\": 2, \\\"xcorr_entropy_d1_r\\\": 0.973}, \\\"extra\\\": {\\\"hook_events\\\": [{\\\"event\\\": \\\"on_complete\\\", \\\"action\\\": \\\"agent\\\", \\\"ts\\\": \\\"2026-05-15T13:13:07.582542+00:00\\\"}]}, \\\"conclusion\\\": \\\"success\\\", \\\"checkpoint_path\\\": \\\"results/alpha_sweep/a075_s42/\\\", \\\"completed_at\\\": \\\"2026-05-15T13:29:46.421Z\\\"}, \\\"alpha_sweep_a050_s42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-14T21:52:15.427Z\\\", \\\"updated_at\\\": \\\"2026-05-15T13:17:48.134Z\\\", \\\"spec\\\": {\\\"hypothesis\\\": \\\"α=0.50 moderate contamination: test canary→diversity lead at mid-range synthetic ratio, key data point for non-monotonic dose-response\\\", \\\"seed\\\": 42, \\\"model_name\\\": \\\"EleutherAI/pythia-410m\\\", \\\"data_path\\\": \\\"data/wikitext103_5k\\\", \\\"data_count\\\": 5000, \\\"synthetic_ratio\\\": 0.5, \\\"num_generations\\\": 10, \\\"steps_per_gen\\\": 5000}, \\\"server\\\": \\\"westd-19828\\\", \\\"gpu\\\": \\\"cuda:1\\\", \\\"account\\\": \\\"root\\\", \\\"reproduce\\\": {\\\"server\\\": \\\"westd-19828\\\", \\\"gpu\\\": \\\"cuda:1\\\", \\\"started_at\\\": \\\"2026-05-15T01:15:14.747Z\\\", \\\"command\\\": \\\"bash -c \\\\\\\"cd /root/autodl-tmp/distrib_canary_collapse && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_HUB_DISABLE_XET=1 && export HF_ENDPOINT=https://hf-mirror.com && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && PYTHONUNBUFFERED=1 python -u iterative_train.py --seed 42 --data_dir data/wikitext103_5k --steps_per_gen 5000 --num_generations 10 --synthetic_ratio 0.50 --output_dir results/alpha_sweep/a050_s42\\\\\\\"\\\", \\\"finished_at\\\": \\\"2026-05-15T05:42:25.788Z\\\", \\\"training_hours\\\": 4.45}, \\\"pid\\\": \\\"73737\\\", \\\"log_path\\\": \\\"~/runs/distrib_canary_collapse/alpha_sweep_a050_s42.log\\\", \\\"metrics\\\": {\\\"progress\\\": \\\"11/11 gen (complete)\\\", \\\"gen0_token_entropy\\\": 3.234, \\\"gen10_token_entropy\\\": 2.632, \\\"gen0_ece\\\": 0.011, \\\"gen10_ece\\\": 0.102, \\\"gen0_perplexity\\\": 26.95, \\\"gen10_perplexity\\\": 32.64, \\\"gen0_distinct_1\\\": 0.098, \\\"gen10_distinct_1\\\": 0.062, \\\"gen0_distinct_2\\\": 0.518, \\\"gen10_distinct_2\\\": 0.251, \\\"gen0_distinct_3\\\": 0.813, \\\"gen10_distinct_3\\\": 0.387, \\\"token_entropy_drift_pct\\\": -18.6, \\\"ece_drift_pct\\\": 842.8, \\\"perplexity_drift_pct\\\": 21.1, \\\"distinct_1_drift_pct\\\": -37.3, \\\"distinct_2_drift_pct\\\": -51.5, \\\"distinct_3_drift_pct\\\": -52.4, \\\"granger_entropy_to_d1_p_raw\\\": 0.095, \\\"granger_entropy_to_d2_p_raw\\\": 0.097, \\\"granger_ece_to_d1_p_raw\\\": 0.019, \\\"granger_ece_to_d2_p_raw\\\": 0.039, \\\"granger_fdr_note\\\": \\\"4 tests within alpha=0.50; BH FDR threshold rank1=0.0125, rank2=0.025 → 0/4 FDR-sig at q=0.05. Raw p pattern (ECE < entropy) is qualitative signal only.\\\", \\\"d024_non_monotonic\\\": true, \\\"d024_ece_vs_entropy_note\\\": \\\"ECE raw p < entropy raw p at α=0.50 (0.019 vs 0.095 at 5000 perms), 0/4 FDR-sig; regime switch hypothesis pending α=0.75 confirmation\\\"}, \\\"extra\\\": {\\\"hook_events\\\": [{\\\"event\\\": \\\"on_complete\\\", \\\"action\\\": \\\"agent\\\", \\\"ts\\\": \\\"2026-05-15T05:42:26.715028+00:00\\\"}]}, \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a050_s42/gen_10/checkpoint\\\", \\\"conclusion\\\": \\\"success\\\", \\\"completed_at\\\": \\\"2026-05-15T05:46:48.692Z\\\"}, \\\"plan_006_s42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-14T23:31:35.454Z\\\", \\\"updated_at\\\": \\\"2026-05-15T12:17:14.093Z\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"cd /root/autodl-tmp/distrib_canary_collapse && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_HUB_DISABLE_XET=1 && export HF_ENDPOINT=https://hf-mirror.com && PYTHONUNBUFFERED=1 python -u iterative_train.py --data_dir data/wikitext103 --output_dir results/extended_20gen/s42 --seed 42 --synthetic_ratio 1.0 --num_generations 20 --steps_per_gen 10000\\\\\\\"\\\", \\\"server\\\": \\\"westd-19828\\\", \\\"gpu\\\": [\\\"cuda:0\\\"], \\\"pid\\\": \\\"68368\\\", \\\"log_path\\\": \\\"~/runs/distrib_canary_collapse/plan_006_s42.log\\\", \\\"submitted_at\\\": \\\"2026-05-14T23:41:30.666Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"wall_clock_seconds\\\": 43212.6, \\\"gpu_hours\\\": 12.0}, \\\"server\\\": \\\"westd-19828\\\", \\\"gpu\\\": \\\"cuda:0\\\", \\\"account\\\": \\\"root\\\", \\\"reproduce\\\": {\\\"server\\\": \\\"westd-19828\\\", \\\"gpu\\\": \\\"cuda:0\\\", \\\"started_at\\\": \\\"2026-05-14T23:41:29.125Z\\\", \\\"command\\\": \\\"bash -c \\\\\\\"cd /root/autodl-tmp/distrib_canary_collapse && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_HUB_DISABLE_XET=1 && export HF_ENDPOINT=https://hf-mirror.com && PYTHONUNBUFFERED=1 python -u iterative_train.py --data_dir data/wikitext103 --output_dir results/extended_20gen/s42 --seed 42 --synthetic_ratio 1.0 --num_generations 20 --steps_per_gen 10000\\\\\\\"\\\", \\\"finished_at\\\": \\\"2026-05-15T11:41:42.336Z\\\", \\\"training_hours\\\": 12.0}, \\\"pid\\\": \\\"68368\\\", \\\"log_path\\\": \\\"~/runs/distrib_canary_collapse/plan_006_s42.log\\\", \\\"metrics\\\": {\\\"progress\\\": \\\"18/20 gen (gen_0-17 complete, gen_18-20 timeout)\\\", \\\"gen0_token_entropy\\\": 3.2342, \\\"gen17_token_entropy\\\": 1.1819, \\\"gen0_ece\\\": 0.0108, \\\"gen17_ece\\\": 0.4454, \\\"gen0_perplexity\\\": 26.95, \\\"gen17_perplexity\\\": 3367.66, \\\"gen0_distinct_1\\\": 0.0982, \\\"gen17_distinct_1\\\": 0.0756, \\\"gen0_distinct_2\\\": 0.5178, \\\"gen17_distinct_2\\\": 0.3617, \\\"gen0_distinct_3\\\": 0.8127, \\\"gen17_distinct_3\\\": 0.5865, \\\"token_entropy_drift_pct_gen0_17\\\": -63.4, \\\"distinct_1_drift_pct_gen0_17\\\": -23, \\\"distinct_2_drift_pct_gen0_17\\\": -30.1, \\\"distinct_3_drift_pct_gen0_17\\\": -27.8, \\\"ece_drift_pct_gen0_17\\\": 4024, \\\"ppl_drift_pct_gen0_17\\\": 12395, \\\"phase1_rapid_collapse\\\": \\\"gen0-5\\\", \\\"phase2_apparent_plateau\\\": \\\"gen5-12\\\", \\\"phase3_secondary_decline\\\": \\\"gen13-17\\\", \\\"phase3_d2_decline_pct\\\": -5.8, \\\"phase3_d3_decline_pct\\\": -6.9, \\\"diversity_saturated_at_gen\\\": 5, \\\"diversity_secondary_decline_at_gen\\\": 13, \\\"perplexity_saturated\\\": false}, \\\"failure_reason\\\": \\\"EXIT_CODE=124 (timeout — exceeded timeout_hours)\\\", \\\"conclusion\\\": \\\"failed\\\", \\\"completed_at\\\": \\\"2026-05-15T11:41:43.235Z\\\", \\\"extra\\\": {\\\"hook_events\\\": [{\\\"event\\\": \\\"on_failed\\\", \\\"action\\\": \\\"agent\\\", \\\"ts\\\": \\\"2026-05-15T11:41:44.300301+00:00\\\"}]}, \\\"notes\\\": \\\"gen_0-17 complete (T=18). 三相 collapse: Phase1 急速崩塌 gen0-5 (d1 -20.6%, entropy -63.8%), Phase2 表观稳态 gen5-12 (diversity <0.3% 变化, perplexity 仍+167%), Phase3 二次衰退 gen13-17 (d2 -5.8%, d3 -6.9%). Perplexity 未饱和 (26.95→3367.66, +12395%). T=18 vs T=10: 新增 diversity 二次衰退在 T=10 window 不可见. TY power 预估 ~0.28-0.41 (vs T=10 的 0.05-0.21).\\\"}, \\\"plan_006_s42_resume\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-15T11:55:26.236Z\\\", \\\"updated_at\\\": \\\"2026-05-15T12:10:54.859Z\\\", \\\"spec\\\": {\\\"command\\\": \\\"python -u resume_plan006_s42.py\\\", \\\"server\\\": \\\"westd-19828\\\", \\\"gpu\\\": [\\\"cuda:0\\\"], \\\"pid\\\": \\\"114844\\\", \\\"log_path\\\": \\\"~/runs/distrib_canary_collapse/plan_006_s42_resume.log\\\", \\\"submitted_at\\\": \\\"2026-05-15T11:55:31.984Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"hypothesis\\\": \\\"恢复 plan_006_s42 从 gen_17，完成 gen_18-20 + all_metrics（α=1.0, 20gen, s42）\\\", \\\"seed\\\": 42, \\\"model_name\\\": \\\"EleutherAI/pythia-410m\\\", \\\"data_path\\\": \\\"data/wikitext103\\\", \\\"data_count\\\": 0, \\\"checkpoint_path\\\": \\\"N/A\\\", \\\"notes\\\": \\\"D034 决定不恢复，T=18 数据已足够（超出 T=15 目标）。plan_006_s42 gen_0-17 数据可用。\\\", \\\"wall_clock_seconds\\\": 921.5, \\\"gpu_hours\\\": 0.26}, \\\"conclusion\\\": \\\"killed\\\", \\\"completed_at\\\": \\\"2026-05-15T12:10:53.514Z\\\", \\\"notes\\\": \\\"D034 决定不恢复。T=18 数据已足够（超出 T=15 目标）。原 plan_006_s42 gen_0-17 数据可用于 power analysis + supplementary。\\\"}, \\\"gen_wiki_gpt2m_a100_s42_v2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-15T12:02:06.478Z\\\", \\\"updated_at\\\": \\\"2026-05-15T12:04:50.741Z\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && mkdir -p results/gen_wiki_gpt2m_a100_s42 && HF_HOME=/root/autodl-tmp/.hf_cache TRANSFORMERS_OFFLINE=1 HF_HUB_DISABLE_XET=1 PYTHONUNBUFFERED=1 python -u iterative_train.py --model_name /root/autodl-tmp/models/gpt2-medium --data_dir data/wikitext103_5k --synthetic_ratio 1.0 --num_generations 10 --steps_per_gen 5000 --batch_size 32 --seed 42 --output_dir results/gen_wiki_gpt2m_a100_s42\\\\\\\"\\\", \\\"server\\\": \\\"westd-19828\\\", \\\"gpu\\\": [\\\"cuda:0\\\"], \\\"pid\\\": \\\"116204\\\", \\\"log_path\\\": \\\"~/runs/distrib_canary_collapse/gen_wiki_gpt2m_a100_s42_v2.log\\\", \\\"submitted_at\\\": \\\"2026-05-15T12:02:14.440Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"wall_clock_seconds\\\": 18.0, \\\"gpu_hours\\\": 0.01}, \\\"server\\\": \\\"westd-19828\\\", \\\"gpu\\\": \\\"cuda:0\\\", \\\"account\\\": \\\"root\\\", \\\"reproduce\\\": {\\\"server\\\": \\\"westd-19828\\\", \\\"gpu\\\": \\\"cuda:0\\\", \\\"started_at\\\": \\\"2026-05-15T12:02:13.557Z\\\", \\\"command\\\": \\\"bash -c \\\\\\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && mkdir -p results/gen_wiki_gpt2m_a100_s42 && HF_HOME=/root/autodl-tmp/.hf_cache TRANSFORMERS_OFFLINE=1 HF_HUB_DISABLE_XET=1 PYTHONUNBUFFERED=1 python -u iterative_train.py --model_name /root/autodl-tmp/models/gpt2-medium --data_dir data/wikitext103_5k --synthetic_ratio 1.0 --num_generations 10 --steps_per_gen 5000 --batch_size 32 --seed 42 --output_dir results/gen_wiki_gpt2m_a100_s42\\\\\\\"\\\", \\\"finished_at\\\": \\\"2026-05-15T12:02:31.643Z\\\", \\\"training_hours\\\": 0.01}, \\\"pid\\\": \\\"116204\\\", \\\"log_path\\\": \\\"~/runs/distrib_canary_collapse/gen_wiki_gpt2m_a100_s42_v2.log\\\", \\\"failure_reason\\\": \\\"EXIT_CODE=1 (generic error — check log tail)\\\", \\\"conclusion\\\": \\\"killed\\\", \\\"completed_at\\\": \\\"2026-05-15T12:02:32.472Z\\\", \\\"extra\\\": {\\\"hook_events\\\": [{\\\"event\\\": \\\"on_failed\\\", \\\"action\\\": \\\"agent\\\", \\\"ts\\\": \\\"2026-05-15T12:02:33.931882+00:00\\\"}]}}, \\\"gen_wiki_gpt2m_a100_s42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-15T10:35:18.700Z\\\", \\\"updated_at\\\": \\\"2026-05-15T12:01:58.523Z\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && mkdir -p results/gen_wiki_gpt2m_a100_s42 && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_DISABLE_XET=1 PYTHONUNBUFFERED=1 python -u iterative_train.py --model_name gpt2-medium --data_dir data/wikitext103_5k --synthetic_ratio 1.0 --num_generations 10 --steps_per_gen 5000 --batch_size 32 --seed 42 --output_dir results/gen_wiki_gpt2m_a100_s42\\\\\\\"\\\", \\\"server\\\": \\\"westd-19828\\\", \\\"gpu\\\": [\\\"cuda:0\\\"], \\\"pid\\\": \\\"115532\\\", \\\"log_path\\\": \\\"~/runs/distrib_canary_collapse/gen_wiki_gpt2m_a100_s42.log\\\", \\\"submitted_at\\\": \\\"2026-05-15T11:57:48.767Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"wall_clock_seconds\\\": 249.8, \\\"gpu_hours\\\": 0.07}, \\\"server\\\": \\\"westd-19828\\\", \\\"gpu\\\": \\\"cuda:0\\\", \\\"account\\\": \\\"root\\\", \\\"reproduce\\\": {\\\"server\\\": \\\"westd-19828\\\", \\\"gpu\\\": \\\"cuda:0\\\", \\\"started_at\\\": \\\"2026-05-15T11:57:47.340Z\\\", \\\"command\\\": \\\"bash -c \\\\\\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && mkdir -p results/gen_wiki_gpt2m_a100_s42 && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_DISABLE_XET=1 PYTHONUNBUFFERED=1 python -u iterative_train.py --model_name gpt2-medium --data_dir data/wikitext103_5k --synthetic_ratio 1.0 --num_generations 10 --steps_per_gen 5000 --batch_size 32 --seed 42 --output_dir results/gen_wiki_gpt2m_a100_s42\\\\\\\"\\\"}, \\\"pid\\\": \\\"115532\\\", \\\"log_path\\\": \\\"~/runs/distrib_canary_collapse/gen_wiki_gpt2m_a100_s42.log\\\", \\\"conclusion\\\": \\\"killed\\\", \\\"completed_at\\\": \\\"2026-05-15T12:01:58.523Z\\\"}, \\\"method_ablation_phase2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-15T08:58:35.270Z\\\", \\\"updated_at\\\": \\\"2026-05-15T11:07:42.688Z\\\", \\\"spec\\\": {\\\"hypothesis\\\": \\\"Method sensitivity is compounded by regime dependence — method x alpha interaction is the headline Claim 3 evidence\\\", \\\"command\\\": \\\"python method_ablation_phase2.py\\\", \\\"server\\\": \\\"westd-19828\\\", \\\"data_path\\\": \\\"results/alpha_sweep + results/mvp\\\", \\\"data_count\\\": 56, \\\"model_name\\\": \\\"N/A (analysis)\\\", \\\"seed\\\": \\\"42,43,44,45\\\", \\\"checkpoint_path\\\": \\\"N/A\\\", \\\"log_path\\\": \\\"results/method_ablation_phase2_panel.json\\\"}, \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"n_panel_rows\\\": 56, \\\"n_alphas\\\": 4, \\\"alphas\\\": [0, 0.25, 0.5, 1], \\\"naive_sig_rate_overall\\\": 1, \\\"perm_granger_sig_rate_a000_raw\\\": 0, \\\"perm_granger_sig_rate_a000_fdr\\\": 0, \\\"perm_granger_sig_rate_a025_raw\\\": 0.25, \\\"perm_granger_sig_rate_a025_fdr\\\": 0, \\\"perm_granger_sig_rate_a050_raw\\\": 0.25, \\\"perm_granger_sig_rate_a050_fdr\\\": 0, \\\"perm_granger_sig_rate_a100_raw\\\": 0.75, \\\"perm_granger_sig_rate_a100_fdr\\\": 0.75, \\\"TY_sig_rate_a000_raw\\\": 0, \\\"TY_sig_rate_a000_fdr\\\": 0, \\\"TY_sig_rate_a025_raw\\\": 0.625, \\\"TY_sig_rate_a025_fdr\\\": 0.375, \\\"TY_sig_rate_a050_raw\\\": 0, \\\"TY_sig_rate_a050_fdr\\\": 0, \\\"TY_sig_rate_a100_raw\\\": 0.5938, \\\"TY_sig_rate_a100_fdr\\\": 0.5938, \\\"diff_sig_rate_a000_raw\\\": 0.5, \\\"diff_sig_rate_a000_fdr\\\": 0.375, \\\"mean_inter_method_kappa\\\": 0.185, \\\"naive_vs_perm_granger_flip_rate\\\": 0.5, \\\"naive_vs_TY_flip_rate\\\": 0.57, \\\"fdr_flips_perm_granger\\\": 4, \\\"pair_verdict_a100_perm_granger\\\": \\\"6/8\\\", \\\"pair_verdict_a100_TY\\\": \\\"6/8\\\", \\\"entropy_to_diversity_a100_all_5methods_sig\\\": true, \\\"fdr_correction\\\": \\\"BH q=0.05\\\"}, \\\"completed_at\\\": \\\"2026-05-15T08:58:54.741Z\\\"}, \\\"alpha_sweep_a025_s42_v3\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-14T21:04:05.726Z\\\", \\\"updated_at\\\": \\\"2026-05-15T05:13:22.207Z\\\", \\\"spec\\\": {\\\"hypothesis\\\": \\\"α=0.25 低污染: 测试 canary→diversity lead 在温和 collapse 下是否保持\\\", \\\"model_name\\\": \\\"EleutherAI/pythia-410m\\\", \\\"data_path\\\": \\\"/root/autodl-tmp/distrib_canary_collapse/data/wikitext103_5k\\\", \\\"data_count\\\": 5000, \\\"seed\\\": 42, \\\"synthetic_ratio\\\": 0.25, \\\"num_generations\\\": 10, \\\"steps_per_gen\\\": 5000, \\\"parent\\\": \\\"alpha_sweep_a025_s42_v2 (failed, data corruption)\\\", \\\"command\\\": \\\"bash -c \\\\\\\"cd /root/autodl-tmp/distrib_canary_collapse && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_HUB_DISABLE_XET=1 && export HF_ENDPOINT=https://hf-mirror.com && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && PYTHONUNBUFFERED=1 python -u iterative_train.py --seed 42 --data_dir data/wikitext103_5k --steps_per_gen 5000 --num_generations 10 --synthetic_ratio 0.25 --output_dir results/alpha_sweep/a025_s42\\\\\\\"\\\", \\\"server\\\": \\\"westd-19828\\\", \\\"gpu\\\": [\\\"cuda:1\\\"], \\\"pid\\\": \\\"53069\\\", \\\"log_path\\\": \\\"~/runs/distrib_canary_collapse/alpha_sweep_a025_s42_v3.log\\\"}, \\\"reproduce\\\": {\\\"finished_at\\\": \\\"2026-05-15T01:18:42.377Z\\\"}, \\\"extra\\\": {\\\"hook_events\\\": [{\\\"event\\\": \\\"on_complete\\\", \\\"action\\\": \\\"agent\\\", \\\"ts\\\": \\\"2026-05-15T01:18:43.329069+00:00\\\"}]}, \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"gen0_token_entropy\\\": 3.2342, \\\"gen10_token_entropy\\\": 3.1017, \\\"gen0_ece\\\": 0.0108, \\\"gen10_ece\\\": 0.01942, \\\"gen0_perplexity\\\": 26.95, \\\"gen10_perplexity\\\": 22.32, \\\"gen0_distinct_1\\\": 0.0982, \\\"gen10_distinct_1\\\": 0.0586, \\\"gen0_distinct_2\\\": 0.5178, \\\"gen10_distinct_2\\\": 0.2219, \\\"gen0_distinct_3\\\": 0.8127, \\\"gen10_distinct_3\\\": 0.3263, \\\"token_entropy_drift_pct\\\": -4.1, \\\"ece_drift_pct\\\": 79.7, \\\"perplexity_drift_pct\\\": -17.2, \\\"distinct_1_drift_pct\\\": -40.3, \\\"distinct_2_drift_pct\\\": -57.1, \\\"distinct_3_drift_pct\\\": -59.9}, \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a025_s42/gen_10/checkpoint\\\", \\\"completed_at\\\": \\\"2026-05-15T01:26:19.292Z\\\", \\\"notes\\\": \\\"实际磁盘路径为 results/alpha_sweep/a025_s42/（无 v3 后缀）。Registry ID 带 v3 是历史原因，数据已核实无误。\\\"}, \\\"method_ablation_phase1\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-14T23:49:16.519Z\\\", \\\"updated_at\\\": \\\"2026-05-14T23:49:40.162Z\\\", \\\"spec\\\": {\\\"plan_id\\\": \\\"plan_002\\\", \\\"hypothesis\\\": \\\"lead-lag 结论对分析方法高度敏感——naive Pearson 100% SIG vs TY 25% SIG，方法选择改变 75% 的结论\\\", \\\"command\\\": \\\"python method_ablation.py + python permutation_granger.py (差分版)\\\", \\\"server\\\": \\\"westd-19828\\\", \\\"data_path\\\": \\\"results/mvp/rep_{42,43,44,45}/all_metrics.json\\\", \\\"data_count\\\": 4, \\\"model_name\\\": \\\"N/A (analysis on MVP data)\\\", \\\"seed\\\": \\\"42,43,44,45\\\", \\\"checkpoint_path\\\": \\\"N/A\\\", \\\"log_path\\\": \\\"results/mvp/analysis/method_ablation.json\\\"}, \\\"conclusion\\\": \\\"success\\\", \\\"completed_at\\\": \\\"2026-05-14T23:49:37.295Z\\\", \\\"metrics\\\": {\\\"spurious_rate_5method\\\": 0.75, \\\"spurious_rate_4method\\\": 0.625, \\\"naive_sig\\\": \\\"16/16\\\", \\\"differenced_sig\\\": \\\"14/16\\\", \\\"threshold_sig\\\": \\\"9/16\\\", \\\"permutation_granger_sig\\\": \\\"6/16\\\", \\\"ty_sig\\\": \\\"4/16\\\", \\\"ty_power_T10\\\": \\\"0.05-0.20\\\", \\\"bh_fdr_flips\\\": 0}}, \\\"alpha_sweep_a000_s42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-14T19:01:37.470Z\\\", \\\"updated_at\\\": \\\"2026-05-14T23:42:18.748Z\\\", \\\"spec\\\": {\\\"hypothesis\\\": \\\"α=0.0 null control: 纯 real data 再训练无 canary signal，确认 signal 源于合成污染\\\", \\\"model_name\\\": \\\"EleutherAI/pythia-410m\\\", \\\"data_path\\\": \\\"/root/autodl-tmp/distrib_canary_collapse/data/wikitext103_5k\\\", \\\"data_count\\\": 5000, \\\"seed\\\": 42, \\\"synthetic_ratio\\\": 0, \\\"num_generations\\\": 10, \\\"steps_per_gen\\\": 5000, \\\"command\\\": \\\"bash -c \\\\\\\"cd /root/autodl-tmp/distrib_canary_collapse && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_HUB_DISABLE_XET=1 && export HF_ENDPOINT=https://hf-mirror.com && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && PYTHONUNBUFFERED=1 python -u iterative_train.py --seed 42 --data_dir data/wikitext103_5k --steps_per_gen 5000 --num_generations 10 --synthetic_ratio 0.0 --output_dir results/alpha_sweep/a000_s42\\\\\\\"\\\", \\\"server\\\": \\\"westd-19828\\\", \\\"gpu\\\": [\\\"cuda:0\\\"], \\\"pid\\\": \\\"46716\\\", \\\"log_path\\\": \\\"~/runs/distrib_canary_collapse/alpha_sweep_a000_s42.log\\\"}, \\\"reproduce\\\": {\\\"finished_at\\\": \\\"2026-05-14T23:36:35.414Z\\\"}, \\\"extra\\\": {\\\"hook_events\\\": [{\\\"event\\\": \\\"on_complete\\\", \\\"action\\\": \\\"agent\\\", \\\"ts\\\": \\\"2026-05-14T23:36:36.221435+00:00\\\"}]}, \\\"conclusion\\\": \\\"success\\\", \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a000_s42/gen_10/checkpoint\\\", \\\"log_path\\\": \\\"~/runs/distrib_canary_collapse/alpha_sweep_a000_s42.log\\\", \\\"metrics\\\": {\\\"gen0_token_entropy\\\": 3.2342, \\\"gen10_token_entropy\\\": 3.0693, \\\"gen0_ece\\\": 0.0108, \\\"gen10_ece\\\": 0.0164, \\\"gen0_perplexity\\\": 26.95, \\\"gen10_perplexity\\\": 21.11, \\\"gen0_distinct_1\\\": 0.0982, \\\"gen10_distinct_1\\\": 0.0847, \\\"token_entropy_drift_pct\\\": -5.1, \\\"ece_drift_pct\\\": 51.7, \\\"perplexity_drift_pct\\\": -21.7, \\\"distinct_1_drift_pct\\\": -13.8, \\\"distinct_2_drift_pct\\\": -9.8, \\\"distinct_3_drift_pct\\\": -4.5, \\\"gen1_10_perplexity_drift_pct\\\": 9.4, \\\"gen1_10_distinct_1_drift_pct\\\": -13.1, \\\"gen1_10_entropy_drift_pct\\\": 2.6}, \\\"completed_at\\\": \\\"2026-05-14T23:39:04.310Z\\\"}, \\\"plan_009_bootstrap_ty\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-14T21:33:04.665Z\\\", \\\"updated_at\\\": \\\"2026-05-14T21:33:27.106Z\\\", \\\"spec\\\": {\\\"hypothesis\\\": \\\"Monte Carlo 验证 TY Granger 在短时间序列 (T=10,15,20,30) 下的 Type I error 和 statistical power\\\", \\\"command\\\": \\\"python bootstrap_ty_validation.py (N_sim=1000)\\\", \\\"server\\\": \\\"westd-19828\\\", \\\"data_path\\\": \\\"synthetic DGP (AR(1) for H0, VAR(2) for H1)\\\", \\\"data_count\\\": 1000, \\\"model_name\\\": \\\"N/A (statistical simulation)\\\", \\\"seed\\\": \\\"multiple\\\", \\\"log_path\\\": \\\"results/bootstrap_ty_results.json\\\", \\\"checkpoint_path\\\": \\\"N/A\\\"}, \\\"conclusion\\\": \\\"success\\\", \\\"completed_at\\\": \\\"2026-05-14T21:33:24.769Z\\\", \\\"metrics\\\": {\\\"T10_d0_type1\\\": 0.081, \\\"T10_d0_power\\\": 0.205, \\\"T10_d1_type1\\\": 0.047, \\\"T10_d1_power\\\": 0.09, \\\"T10_dadapt_type1\\\": 0.052, \\\"T10_dadapt_power\\\": 0.05, \\\"T20_d0_power\\\": 0.409, \\\"T20_d1_power\\\": 0.172, \\\"T30_d0_power\\\": 0.606, \\\"T30_d1_power\\\": 0.283}}, \\\"mvp_v3_rep43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-14T06:25:42.195Z\\\", \\\"updated_at\\\": \\\"2026-05-14T06:48:01.316Z\\\", \\\"spec\\\": {\\\"command\\\": \\\"python iterative_train.py --seed 43 --output_dir results/mvp/rep_43 --data_dir data/wikitext103_5k --synthetic_ratio 1.0 --num_generations 10 --steps_per_gen 5000\\\", \\\"server\\\": \\\"autodl-rtx6000\\\", \\\"gpu\\\": \\\"cuda:1\\\", \\\"pid\\\": \\\"7987\\\", \\\"log_path\\\": \\\"~/runs/distrib_canary_collapse/mvp_v3_rep43.log\\\", \\\"submitted_at\\\": \\\"2026-05-14T06:26:18.477Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"data_path\\\": \\\"/root/autodl-tmp/distrib_canary_collapse/data/wikitext103_5k\\\", \\\"data_count\\\": 5000, \\\"model_name\\\": \\\"EleutherAI/pythia-410m\\\", \\\"seed\\\": 43, \\\"gpu_model\\\": \\\"RTX PRO 6000 Blackwell 96GB\\\", \\\"tmux_session\\\": \\\"mvp_v3_rep43\\\", \\\"checkpoint_path\\\": \\\"N/A\\\", \\\"failure_reason\\\": \\\"MAUVE FAISS crash: max_samples=500 → p+q=1000 < 1950 required; 无 PYTHONUNBUFFERED 导致日志丢失\\\", \\\"wall_clock_seconds\\\": 1302.8, \\\"gpu_hours\\\": 0.36}, \\\"conclusion\\\": \\\"failed\\\", \\\"completed_at\\\": \\\"2026-05-14T06:48:01.316Z\\\"}, \\\"mvp_v3_rep42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-14T06:25:39.728Z\\\", \\\"updated_at\\\": \\\"2026-05-14T06:47:59.908Z\\\", \\\"spec\\\": {\\\"command\\\": \\\"python iterative_train.py --seed 42 --output_dir results/mvp/rep_42 --data_dir data/wikitext103_5k --synthetic_ratio 1.0 --num_generations 10 --steps_per_gen 5000\\\", \\\"server\\\": \\\"autodl-rtx6000\\\", \\\"gpu\\\": \\\"cuda:0\\\", \\\"pid\\\": \\\"7909\\\", \\\"log_path\\\": \\\"~/runs/distrib_canary_collapse/mvp_v3_rep42.log\\\", \\\"submitted_at\\\": \\\"2026-05-14T06:26:16.939Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"data_path\\\": \\\"/root/autodl-tmp/distrib_canary_collapse/data/wikitext103_5k\\\", \\\"data_count\\\": 5000, \\\"model_name\\\": \\\"EleutherAI/pythia-410m\\\", \\\"seed\\\": 42, \\\"gpu_model\\\": \\\"RTX PRO 6000 Blackwell 96GB\\\", \\\"tmux_session\\\": \\\"mvp_v3_rep42\\\", \\\"checkpoint_path\\\": \\\"N/A\\\", \\\"failure_reason\\\": \\\"MAUVE FAISS crash: max_samples=500 → p+q=1000 < 1950 required; 无 PYTHONUNBUFFERED 导致日志丢失\\\", \\\"wall_clock_seconds\\\": 1303.0, \\\"gpu_hours\\\": 0.36}, \\\"conclusion\\\": \\\"failed\\\", \\\"completed_at\\\": \\\"2026-05-14T06:47:59.908Z\\\"}, \\\"mvp_v2_rep43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-14T05:38:10.434Z\\\", \\\"updated_at\\\": \\\"2026-05-14T06:25:28.345Z\\\", \\\"spec\\\": {\\\"command\\\": \\\"python iterative_train.py --seed 43 --output_dir results/mvp/rep_43 --data_dir data/wikitext103_5k --synthetic_ratio 1.0 --num_generations 10 --steps_per_gen 5000\\\", \\\"server\\\": \\\"autodl-rtx6000\\\", \\\"gpu\\\": \\\"cuda:1\\\", \\\"pid\\\": \\\"5364\\\", \\\"log_path\\\": \\\"~/runs/distrib_canary_collapse/mvp_v2_rep43.log\\\", \\\"submitted_at\\\": \\\"2026-05-14T05:42:39.039Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"data_path\\\": \\\"/root/autodl-tmp/distrib_canary_collapse/data/wikitext103_5k\\\", \\\"data_count\\\": 5000, \\\"model_name\\\": \\\"EleutherAI/pythia-410m\\\", \\\"seed\\\": 43, \\\"gpu_model\\\": \\\"RTX PRO 6000 Blackwell 96GB\\\", \\\"tmux_session\\\": \\\"mvp_v2_rep43\\\", \\\"checkpoint_path\\\": \\\"N/A\\\", \\\"kill_reason\\\": \\\"v1旧进程未死导致输出目录冲突，v2死锁\\\", \\\"wall_clock_seconds\\\": 2569.3, \\\"gpu_hours\\\": 0.71}, \\\"conclusion\\\": \\\"killed\\\", \\\"completed_at\\\": \\\"2026-05-14T06:25:28.345Z\\\"}, \\\"mvp_v2_rep42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-14T05:38:05.054Z\\\", \\\"updated_at\\\": \\\"2026-05-14T06:25:27.286Z\\\", \\\"spec\\\": {\\\"command\\\": \\\"python iterative_train.py --seed 42 --output_dir results/mvp/rep_42 --data_dir data/wikitext103_5k --synthetic_ratio 1.0 --num_generations 10 --steps_per_gen 5000\\\", \\\"server\\\": \\\"autodl-rtx6000\\\", \\\"gpu\\\": \\\"cuda:0\\\", \\\"pid\\\": \\\"5286\\\", \\\"log_path\\\": \\\"~/runs/distrib_canary_collapse/mvp_v2_rep42.log\\\", \\\"submitted_at\\\": \\\"2026-05-14T05:42:37.404Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"data_path\\\": \\\"/root/autodl-tmp/distrib_canary_collapse/data/wikitext103_5k\\\", \\\"data_count\\\": 5000, \\\"model_name\\\": \\\"EleutherAI/pythia-410m\\\", \\\"seed\\\": 42, \\\"gpu_model\\\": \\\"RTX PRO 6000 Blackwell 96GB\\\", \\\"tmux_session\\\": \\\"mvp_v2_rep42\\\", \\\"checkpoint_path\\\": \\\"N/A\\\", \\\"kill_reason\\\": \\\"v1旧进程未死导致输出目录冲突，v2死锁\\\", \\\"wall_clock_seconds\\\": 2569.9, \\\"gpu_hours\\\": 0.71}, \\\"conclusion\\\": \\\"killed\\\", \\\"completed_at\\\": \\\"2026-05-14T06:25:27.286Z\\\"}, \\\"mvp_rep43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-14T05:12:14.237Z\\\", \\\"updated_at\\\": \\\"2026-05-14T05:37:18.575Z\\\", \\\"spec\\\": {\\\"command\\\": \\\"python iterative_train.py --seed 43 --output_dir results/mvp/rep_43 --data_dir data/wikitext103 --synthetic_ratio 1.0 --num_generations 10 --steps_per_gen 10000\\\", \\\"server\\\": \\\"autodl-rtx6000\\\", \\\"gpu\\\": \\\"cuda:1\\\", \\\"pid\\\": \\\"3956\\\", \\\"log_path\\\": \\\"~/runs/distrib_canary_collapse/mvp_rep43.log\\\", \\\"submitted_at\\\": \\\"2026-05-14T05:34:47.702Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"data_path\\\": \\\"/root/autodl-tmp/distrib_canary_collapse/data/wikitext103\\\", \\\"data_count\\\": 716506, \\\"model_name\\\": \\\"EleutherAI/pythia-410m\\\", \\\"seed\\\": 43, \\\"gpu_model\\\": \\\"RTX PRO 6000 Blackwell 96GB\\\", \\\"tmux_session\\\": \\\"mvp_rep43\\\", \\\"checkpoint_path\\\": \\\"N/A\\\", \\\"kill_reason\\\": \\\"参数修复: n_prompts 1000→5000, steps_per_gen 10000→5000\\\", \\\"wall_clock_seconds\\\": 150.9, \\\"gpu_hours\\\": 0.04}, \\\"conclusion\\\": \\\"killed\\\", \\\"completed_at\\\": \\\"2026-05-14T05:37:18.575Z\\\"}, \\\"mvp_rep42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-14T05:12:13.930Z\\\", \\\"updated_at\\\": \\\"2026-05-14T05:37:17.438Z\\\", \\\"spec\\\": {\\\"command\\\": \\\"python iterative_train.py --seed 42 --output_dir results/mvp/rep_42 --data_dir data/wikitext103 --synthetic_ratio 1.0 --num_generations 10 --steps_per_gen 10000\\\", \\\"server\\\": \\\"autodl-rtx6000\\\", \\\"gpu\\\": \\\"cuda:0\\\", \\\"pid\\\": \\\"3878\\\", \\\"log_path\\\": \\\"~/runs/distrib_canary_collapse/mvp_rep42.log\\\", \\\"submitted_at\\\": \\\"2026-05-14T05:34:46.013Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"data_path\\\": \\\"/root/autodl-tmp/distrib_canary_collapse/data/wikitext103\\\", \\\"data_count\\\": 716506, \\\"model_name\\\": \\\"EleutherAI/pythia-410m\\\", \\\"seed\\\": 42, \\\"gpu_model\\\": \\\"RTX PRO 6000 Blackwell 96GB\\\", \\\"tmux_session\\\": \\\"mvp_rep42\\\", \\\"checkpoint_path\\\": \\\"N/A\\\", \\\"kill_reason\\\": \\\"参数修复: n_prompts 1000→5000, steps_per_gen 10000→5000\\\", \\\"wall_clock_seconds\\\": 151.4, \\\"gpu_hours\\\": 0.04}, \\\"conclusion\\\": \\\"killed\\\", \\\"completed_at\\\": \\\"2026-05-14T05:37:17.438Z\\\"}}, \\\"count\\\": 34, \\\"total\\\": 34, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.0843}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {\"alpha_sweep_a025_s44\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-15T06:58:48.224Z\", \"updated_at\": \"2026-05-16T02:24:25.189Z\", \"spec\": {\"command\": \"bash -c \\\"cd /root/autodl-tmp/distrib_canary_collapse && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_HUB_DISABLE_XET=1 && export HF_ENDPOINT=https://hf-mirror.com && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && PYTHONUNBUFFERED=1 python -u iterative_train.py --seed 44 --data_dir data/wikitext103_5k --steps_per_gen 5000 --num_generations 10 --synthetic_ratio 0.25 --output_dir results/alpha_sweep/a025_s44\\\"\", \"server\": \"westd-19828\", \"gpu\": [\"cuda:1\"], \"pid\": \"147811\", \"log_path\": \"~/runs/distrib_canary_collapse/alpha_sweep_a025_s44.log\", \"submitted_at\": \"2026-05-15T22:04:28.318Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"server\": \"westd-19828\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-19828\", \"gpu\": \"cuda:1\", \"started_at\": \"2026-05-15T22:04:26.677Z\", \"command\": \"bash -c \\\"cd /root/autodl-tmp/distrib_canary_collapse && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_HUB_DISABLE_XET=1 && export HF_ENDPOINT=https://hf-mirror.com && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && PYTHONUNBUFFERED=1 python -u iterative_train.py --seed 44 --data_dir data/wikitext103_5k --steps_per_gen 5000 --num_generations 10 --synthetic_ratio 0.25 --output_dir results/alpha_sweep/a025_s44\\\"\", \"finished_at\": \"2026-05-16T02:24:25.056Z\", \"training_hours\": 4.33}, \"pid\": \"147811\", \"log_path\": \"~/runs/distrib_canary_collapse/alpha_sweep_a025_s44.log\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T02:24:26.614491+00:00\"}]}}, \"mvp_v2_rep44\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T05:38:10.762Z\", \"updated_at\": \"2026-05-16T00:10:26.251Z\", \"spec\": {\"hypothesis\": \"至少一族canary指标在100% SC full replacement下对downstream指标有≥1 gen的时序领先性\", \"model_name\": \"EleutherAI/pythia-410m\", \"data_path\": \"/root/autodl-tmp/distrib_canary_collapse/data/wikitext103\", \"data_count\": 5000, \"seed\": 44, \"server\": \"autodl-rtx6000\", \"gpu\": \"pending\", \"synthetic_ratio\": 1, \"num_generations\": 10, \"steps_per_gen\": 5000, \"n_prompts\": 5000, \"fix_note\": \"n_prompts 1000→5000, steps_per_gen 10000→5000, 避免过拟合\"}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-16T00:10:26.251Z\"}, \"mvp_rep44\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T05:12:15.033Z\", \"updated_at\": \"2026-05-16T00:10:25.605Z\", \"spec\": {\"hypothesis\": \"至少一族canary指标在100% SC full replacement下对downstream指标有≥1 gen的时序领先性\", \"model_name\": \"EleutherAI/pythia-410m\", \"data_path\": \"/root/autodl-tmp/distrib_canary_collapse/data/wikitext103\", \"seed\": 44, \"server\": \"autodl-rtx6000\", \"gpu\": \"pending\", \"synthetic_ratio\": 1, \"num_generations\": 10, \"steps_per_gen\": 10000}, \"metrics\": {\"gen10_token_entropy\": 1.2205, \"gen10_ece\": 0.4237, \"gen10_perplexity\": 1033.16, \"gen10_distinct_1\": 0.0731, \"gen10_distinct_2\": 0.3637, \"gen10_distinct_3\": 0.6075}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-16T00:10:25.605Z\"}, \"alpha_sweep_a025_s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T19:01:39.527Z\", \"updated_at\": \"2026-05-16T00:10:24.973Z\", \"spec\": {\"hypothesis\": \"α=0.25 低污染: 测试 canary→diversity lead 在温和 collapse 下是否保持，canary→perplexity lead 是否出现\", \"model_name\": \"EleutherAI/pythia-410m\", \"data_path\": \"/root/autodl-tmp/distrib_canary_collapse/data/wikitext103_5k\", \"data_count\": 5000, \"seed\": 42, \"synthetic_ratio\": 0.25, \"num_generations\": 10, \"steps_per_gen\": 5000}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-16T00:10:24.973Z\"}, \"alpha_sweep_a025_s42_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T19:25:52.094Z\", \"updated_at\": \"2026-05-16T00:10:24.568Z\", \"spec\": {\"hypothesis\": \"α=0.25 低污染: 测试 canary→diversity lead 在温和 collapse 下是否保持，canary→perplexity lead 是否出现\", \"model_name\": \"EleutherAI/pythia-410m\", \"data_path\": \"/root/autodl-tmp/distrib_canary_collapse/data/wikitext103_5k\", \"data_count\": 5000, \"seed\": 42, \"synthetic_ratio\": 0.25, \"num_generations\": 10, \"steps_per_gen\": 5000, \"parent\": \"alpha_sweep_a025_s42 (killed, subsample bias fix)\"}, \"conclusion\": \"killed\", \"failure_reason\": \"data corruption: unkilled old process PID 46802 wrote concurrently with new PID 48454\", \"completed_at\": \"2026-05-16T00:10:24.568Z\"}, \"alpha_sweep_a060_s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T21:52:22.516Z\", \"updated_at\": \"2026-05-16T00:04:01.429Z\", \"spec\": {\"hypothesis\": \"α=0.60 中高污染: phase boundary 精确化, 与 α=0.50/0.75 对比 lead time 变化\", \"model_name\": \"EleutherAI/pythia-410m\", \"data_path\": \"/root/autodl-tmp/distrib_canary_collapse/data/wikitext103_5k\", \"data_count\": 5000, \"seed\": 42, \"synthetic_ratio\": 0.6, \"num_generations\": 10, \"steps_per_gen\": 5000}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-16T00:04:01.429Z\"}, \"alpha_sweep_a010_s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T21:52:19.712Z\", \"updated_at\": \"2026-05-16T00:03:53.018Z\", \"spec\": {\"hypothesis\": \"α=0.10 极低污染: phase boundary 精确化, canary signal 是否仍可检测\", \"model_name\": \"EleutherAI/pythia-410m\", \"data_path\": \"/root/autodl-tmp/distrib_canary_collapse/data/wikitext103_5k\", \"data_count\": 5000, \"seed\": 42, \"synthetic_ratio\": 0.1, \"num_generations\": 10, \"steps_per_gen\": 5000}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-16T00:03:53.018Z\"}, \"alpha_sweep_a050_s44\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T06:58:50.550Z\", \"updated_at\": \"2026-05-16T00:03:52.118Z\", \"spec\": {\"hypothesis\": \"α=0.50 multi-seed replication (seed=44): 第三个 seed 为置信区间提供统计力\", \"model_name\": \"EleutherAI/pythia-410m\", \"data_path\": \"/root/autodl-tmp/distrib_canary_collapse/data/wikitext103_5k\", \"data_count\": 5000, \"seed\": 44, \"synthetic_ratio\": 0.5, \"num_generations\": 10, \"steps_per_gen\": 5000, \"parent\": \"alpha_sweep_a050_s42\", \"priority\": \"D026-4\"}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-16T00:03:52.118Z\"}, \"plan_006_s43\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T23:31:37.257Z\", \"updated_at\": \"2026-05-16T00:03:51.617Z\", \"spec\": {\"plan_id\": \"plan_006\", \"hypothesis\": \"Multi-seed replication of three-phase collapse dynamics: verify Phase 3 secondary decline (gen 13+) reproduces with seed=43, confirming it is not a single-seed artifact\", \"model_name\": \"EleutherAI/pythia-410m\", \"seed\": 43, \"data_path\": \"data/wikitext103_5k\", \"num_generations\": 18, \"synthetic_ratio\": 1, \"max_lag\": 10, \"data_count\": 5000, \"steps_per_gen\": 5000, \"parent\": \"plan_006_s42\", \"claim\": 1, \"priority\": \"P0\"}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-16T00:03:51.617Z\"}, \"gen_wiki_gpt2m_a100_s42_v3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T12:07:20.050Z\", \"updated_at\": \"2026-05-15T22:30:21.573Z\", \"spec\": {\"hypothesis\": \"Method sensitivity patterns (Granger FDR collapse, cross-correlation dominance) generalize from GPT-2-small to GPT-2-medium, validating cross-architecture universality of methodological pitfalls\", \"seed\": 42, \"model_name\": \"gpt2-medium\", \"data_path\": \"data/wikitext103_5k\", \"data_count\": 5000}, \"server\": \"westd-19828\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-19828\", \"gpu\": \"cuda:0\", \"started_at\": \"2026-05-15T12:07:30.366Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && mkdir -p results/gen_wiki_gpt2m_a100_s42 && HF_HOME=/root/autodl-tmp/.hf_cache TRANSFORMERS_OFFLINE=1 HF_HUB_DISABLE_XET=1 PYTHONUNBUFFERED=1 python -u iterative_train.py --model_name gpt2-medium --data_dir data/wikitext103_5k --synthetic_ratio 1.0 --num_generations 10 --steps_per_gen 5000 --batch_size 32 --seed 42 --output_dir results/gen_wiki_gpt2m_a100_s42\\\"\", \"finished_at\": \"2026-05-15T22:14:43.852Z\", \"training_hours\": 10.12}, \"pid\": \"117632\", \"log_path\": \"~/runs/distrib_canary_collapse/gen_wiki_gpt2m_a100_s42_v3.log\", \"metrics\": {\"token_entropy_drift_pct\": -86.5, \"ece_drift_pct\": 4543, \"perplexity_drift_pct\": 44703, \"distinct_1_drift_pct\": -12.4, \"distinct_2_drift_pct\": -14.7, \"distinct_3_drift_pct\": -12.7, \"five_method_forward_consensus\": \"6/6 pairs at 4/5 methods (Tier 3)\", \"five_method_reverse_consensus\": \"0/6 pairs\", \"naive_xcorr_forward\": \"|r|>0.98, all sig\", \"diff_xcorr_forward\": \"all p_fdr<0.001\", \"diff_xcorr_reverse\": \"all p>0.18 (clean directional separation)\", \"threshold_onset_entropy\": \"gen 1 (earliest canary)\", \"threshold_onset_ece\": \"gen 1-2\", \"threshold_onset_diversity\": \"gen 3\", \"perm_granger_forward\": \"p_fdr=0.003, BH corrected\", \"ty_granger_forward\": \"0/6 sig (df_resid=1-4, underpowered, consistent with Pythia C001)\", \"entropy_leads_diversity_lag\": \"1-2 gen\", \"ece_leads_diversity_lag\": \"1 gen\", \"diversity_plateau_from\": \"gen5\", \"cross_arch_note\": \"Replicates Pythia entropy-leads-diversity pattern at Tier 3 consensus. TY underpowered as expected.\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T22:14:45.029003+00:00\"}]}, \"conclusion\": \"success\", \"checkpoint_path\": \"results/gen_wiki_gpt2m_a100_s42/\", \"completed_at\": \"2026-05-15T22:18:22.762Z\"}, \"gen_wiki_gpt2m_a025_s42\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-15T10:35:16.032Z\", \"updated_at\": \"2026-05-15T22:22:52.921Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && mkdir -p results/gen_wiki_gpt2m_a025_s42 && HF_HOME=/root/autodl-tmp/.hf_cache TRANSFORMERS_OFFLINE=1 HF_HUB_DISABLE_XET=1 PYTHONUNBUFFERED=1 python -u iterative_train.py --model_name gpt2-medium --data_dir data/wikitext103_5k --synthetic_ratio 0.25 --num_generations 10 --steps_per_gen 5000 --batch_size 32 --seed 42 --output_dir results/gen_wiki_gpt2m_a025_s42\\\"\", \"server\": \"westd-19828\", \"gpu\": [\"cuda:0\"], \"pid\": \"149202\", \"log_path\": \"~/runs/distrib_canary_collapse/gen_wiki_gpt2m_a025_s42.log\", \"submitted_at\": \"2026-05-15T22:22:52.615Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"server\": \"westd-19828\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-19828\", \"gpu\": \"cuda:0\", \"started_at\": \"2026-05-15T22:22:51.021Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && mkdir -p results/gen_wiki_gpt2m_a025_s42 && HF_HOME=/root/autodl-tmp/.hf_cache TRANSFORMERS_OFFLINE=1 HF_HUB_DISABLE_XET=1 PYTHONUNBUFFERED=1 python -u iterative_train.py --model_name gpt2-medium --data_dir data/wikitext103_5k --synthetic_ratio 0.25 --num_generations 10 --steps_per_gen 5000 --batch_size 32 --seed 42 --output_dir results/gen_wiki_gpt2m_a025_s42\\\"\"}, \"pid\": \"149202\", \"log_path\": \"~/runs/distrib_canary_collapse/gen_wiki_gpt2m_a025_s42.log\"}, \"alpha_sweep_a050_s43\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T06:58:45.880Z\", \"updated_at\": \"2026-05-15T22:15:50.290Z\", \"spec\": {\"command\": \"bash -c \\\"cd /root/autodl-tmp/distrib_canary_collapse && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_HUB_DISABLE_XET=1 && export HF_ENDPOINT=https://hf-mirror.com && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && PYTHONUNBUFFERED=1 python -u iterative_train.py --seed 43 --data_dir data/wikitext103_5k --steps_per_gen 5000 --num_generations 10 --synthetic_ratio 0.50 --output_dir results/alpha_sweep/a050_s43\\\"\", \"server\": \"westd-19828\", \"gpu\": [\"cuda:1\"], \"pid\": \"134860\", \"log_path\": \"~/runs/distrib_canary_collapse/alpha_sweep_a050_s43.log\", \"submitted_at\": \"2026-05-15T17:40:27.060Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 16523.2, \"gpu_hours\": 4.59}, \"server\": \"westd-19828\", \"gpu\": \"cuda:1\", \"pid\": \"134860\", \"log_path\": \"~/runs/distrib_canary_collapse/alpha_sweep_a050_s43.log\", \"reproduce\": {\"command\": \"bash -c \\\"cd /root/autodl-tmp/distrib_canary_collapse && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_HUB_DISABLE_XET=1 && export HF_ENDPOINT=https://hf-mirror.com && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && PYTHONUNBUFFERED=1 python -u iterative_train.py --seed 43 --data_dir data/wikitext103_5k --steps_per_gen 5000 --num_generations 10 --synthetic_ratio 0.50 --output_dir results/alpha_sweep/a050_s43\\\"\", \"finished_at\": \"2026-05-15T22:00:14.725Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T22:00:15.908424+00:00\"}]}, \"conclusion\": \"success\", \"checkpoint_path\": \"results/alpha_sweep/a050_s43/gen_10/checkpoint/\", \"metrics\": {\"gen0_token_entropy\": 3.234195, \"gen0_ece\": 0.010805, \"gen0_perplexity\": 26.948959, \"gen10_token_entropy\": 2.672, \"gen10_ece\": 0.097, \"gen10_perplexity\": 32.633, \"gen0_distinct_1\": 0.09833, \"gen0_distinct_2\": 0.5132, \"gen0_distinct_3\": 0.8057, \"gen10_distinct_1\": 0.0624, \"gen10_distinct_2\": 0.2617, \"gen10_distinct_3\": 0.4126, \"token_entropy_drift_pct\": -17.4, \"ece_drift_pct\": 799, \"perplexity_drift_pct\": 21.1, \"distinct_1_drift_pct\": -36.5, \"distinct_2_drift_pct\": -49, \"distinct_3_drift_pct\": -48.8, \"cross_seed_note\": \"vs s42: drift direction identical, magnitude <7% deviation, ppl near-identical (32.633 vs 32.64)\"}, \"completed_at\": \"2026-05-15T22:00:14Z\"}, \"mvp_v4_rep45\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T13:41:26.286Z\", \"updated_at\": \"2026-05-15T21:29:54.928Z\", \"spec\": {\"command\": \"bash -c \\\"cd /root/autodl-tmp/distrib_canary_collapse && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_HUB_DISABLE_XET=1 && export HF_ENDPOINT=https://hf-mirror.com && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && PYTHONUNBUFFERED=1 python -u iterative_train.py --seed 45 --data_dir data/wikitext103_5k --steps_per_gen 5000 --num_generations 10 --output_dir results/mvp/rep_45\\\"\", \"server\": \"westd-19828\", \"gpu\": [\"cuda:1\"], \"pid\": \"31425\", \"log_path\": \"~/runs/distrib_canary_collapse/mvp_v4_rep45.log\", \"submitted_at\": \"2026-05-14T13:42:10.455Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/distrib_canary_collapse/data/wikitext103_5k\", \"data_count\": 5000, \"model_name\": \"EleutherAI/pythia-410m\", \"seed\": 45, \"wall_clock_seconds\": 15350.2, \"gpu_hours\": 4.26}, \"reproduce\": {\"finished_at\": \"2026-05-14T17:55:42.230Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T17:55:42.934182+00:00\"}]}, \"checkpoint_path\": \"/root/autodl-tmp/distrib_canary_collapse/results/mvp/rep_45/gen_10/checkpoint\", \"metrics_summary\": {\"gen0_ppl\": 26.9, \"gen10_ppl\": 1016.2, \"gen0_entropy\": 3.234, \"gen10_entropy\": 1.315, \"gen0_ece\": 0.011, \"gen10_ece\": 0.417}, \"wall_clock_seconds\": 15212, \"gpu_hours\": 4.23, \"conclusion\": \"success\", \"metrics\": {\"gen0_token_entropy\": 3.234195, \"gen0_ece\": 0.010805, \"gen0_perplexity\": 26.948959, \"gen0_distinct_1\": 0.098574, \"gen0_distinct_2\": 0.51463, \"gen0_distinct_3\": 0.808362, \"gen10_token_entropy\": 1.31536, \"gen10_ece\": 0.41654, \"gen10_perplexity\": 1016.22, \"gen10_distinct_1\": 0.069859, \"gen10_distinct_2\": 0.329549, \"gen10_distinct_3\": 0.543743, \"token_entropy_drift_pct\": -59.3296, \"ece_drift_pct\": 3755.0671, \"perplexity_drift_pct\": 3670.9063, \"distinct_1_drift_pct\": -29.1304, \"distinct_2_drift_pct\": -35.9639, \"distinct_3_drift_pct\": -32.7352}, \"completed_at\": \"2026-05-14T17:58:00.661Z\"}, \"mvp_v4_rep44\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T07:48:52.613Z\", \"updated_at\": \"2026-05-15T21:29:52.398Z\", \"spec\": {\"hypothesis\": \"至少一族canary指标在100% SC full replacement下对downstream指标有≥1 gen的时序领先性\", \"model_name\": \"EleutherAI/pythia-410m\", \"data_path\": \"/root/autodl-tmp/distrib_canary_collapse/data/wikitext103_5k\", \"data_count\": 5000, \"seed\": 44, \"server\": \"westd-19828\", \"gpu\": \"cuda:0\", \"synthetic_ratio\": 1, \"num_generations\": 10, \"steps_per_gen\": 5000, \"n_prompts\": 5000, \"command\": \"PYTHONUNBUFFERED=1 CUDA_VISIBLE_DEVICES=0 python -u iterative_train.py --seed 44 --data_dir data/wikitext103_5k --steps_per_gen 5000 --num_generations 10 --output_dir results/mvp/rep_44\", \"pid\": \"30672\", \"log_path\": \"~/runs/distrib_canary_collapse/mvp_v4_rep44.log\"}, \"reproduce\": {\"finished_at\": \"2026-05-14T17:56:00.578Z\"}, \"failure_reason\": \"\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T17:56:00.717Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-14T17:56:03.546926+00:00\"}]}, \"metrics_summary\": {\"gen0_ppl\": 26.9, \"gen10_ppl\": 1033.16, \"gen0_entropy\": 3.234, \"gen10_entropy\": 1.2205, \"gen0_ece\": 0.011, \"gen10_ece\": 0.424}, \"checkpoint_path\": \"/root/autodl-tmp/distrib_canary_collapse/results/mvp/rep_44/gen_10/checkpoint\", \"wall_clock_seconds\": 15134, \"gpu_hours\": 4.2, \"metrics\": {\"gen0_token_entropy\": 3.234195, \"gen0_ece\": 0.010805, \"gen0_perplexity\": 26.948959, \"gen0_distinct_1\": 0.098088, \"gen0_distinct_2\": 0.513235, \"gen0_distinct_3\": 0.805767, \"gen10_token_entropy\": 1.22049, \"gen10_ece\": 0.42369, \"gen10_perplexity\": 1033.16, \"gen10_distinct_1\": 0.073102, \"gen10_distinct_2\": 0.363737, \"gen10_distinct_3\": 0.607502, \"token_entropy_drift_pct\": -62.2629, \"ece_drift_pct\": 3821.2402, \"perplexity_drift_pct\": 3733.7659, \"distinct_1_drift_pct\": -25.473, \"distinct_2_drift_pct\": -29.1286, \"distinct_3_drift_pct\": -24.6057}}, \"mvp_v4_rep43\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T07:48:50.161Z\", \"updated_at\": \"2026-05-15T21:29:49.565Z\", \"spec\": {\"command\": \"bash -c \\\"cd /root/autodl-tmp/distrib_canary_collapse && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_HUB_DISABLE_XET=1 && export HF_ENDPOINT=https://hf-mirror.com && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && PYTHONUNBUFFERED=1 python -u iterative_train.py --seed 43 --data_dir data/wikitext103_5k --steps_per_gen 5000 --num_generations 10 --output_dir results/mvp/rep_43\\\"\", \"server\": \"westd-19828\", \"gpu\": [\"cuda:1\"], \"pid\": \"13758\", \"log_path\": \"~/runs/distrib_canary_collapse/mvp_v4_rep43.log\", \"submitted_at\": \"2026-05-14T07:51:36.759Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"/root/autodl-tmp/distrib_canary_collapse/results/mvp/rep_43/gen_10/checkpoint\", \"metrics_summary\": {\"gen0_ppl\": 26.9, \"gen10_ppl\": 1014.7, \"gen0_entropy\": 3.234, \"gen10_entropy\": 1.26, \"gen0_ece\": 0.011, \"gen10_ece\": 0.42}, \"wall_clock_seconds\": 20897.7, \"gpu_hours\": 5.8}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T13:39:54.495Z\", \"metrics\": {\"gen0_token_entropy\": 3.234195, \"gen0_ece\": 0.010805, \"gen0_perplexity\": 26.948959, \"gen0_distinct_1\": 0.098334, \"gen0_distinct_2\": 0.513178, \"gen0_distinct_3\": 0.805669, \"gen10_token_entropy\": 1.25961, \"gen10_ece\": 0.41951, \"gen10_perplexity\": 1014.66, \"gen10_distinct_1\": 0.070383, \"gen10_distinct_2\": 0.329651, \"gen10_distinct_3\": 0.539571, \"token_entropy_drift_pct\": -61.0534, \"ece_drift_pct\": 3782.5544, \"perplexity_drift_pct\": 3665.1176, \"distinct_1_drift_pct\": -28.4246, \"distinct_2_drift_pct\": -35.7628, \"distinct_3_drift_pct\": -33.0282}}, \"mvp_v4_rep42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T07:29:48.857Z\", \"updated_at\": \"2026-05-15T21:29:47.171Z\", \"spec\": {\"command\": \"bash -c \\\"cd /root/autodl-tmp/distrib_canary_collapse && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_HUB_DISABLE_XET=1 && export HF_ENDPOINT=https://hf-mirror.com && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && PYTHONUNBUFFERED=1 python -u iterative_train.py --seed 42 --data_dir data/wikitext103_5k --steps_per_gen 5000 --num_generations 10 --output_dir results/mvp/rep_42\\\"\", \"server\": \"westd-19828\", \"gpu\": [\"cuda:0\"], \"pid\": \"13678\", \"log_path\": \"~/runs/distrib_canary_collapse/mvp_v4_rep42.log\", \"submitted_at\": \"2026-05-14T07:51:34.806Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"/root/autodl-tmp/distrib_canary_collapse/results/mvp/rep_42/gen_10/checkpoint\", \"metrics_summary\": {\"gen0_ppl\": 26.9, \"gen10_ppl\": 1003.7, \"gen0_entropy\": 3.234, \"gen10_entropy\": 1.276, \"gen0_ece\": 0.011, \"gen10_ece\": 0.417}, \"wall_clock_seconds\": 20898.3, \"gpu_hours\": 5.81}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T13:39:53.073Z\", \"metrics\": {\"gen0_token_entropy\": 3.234195, \"gen0_ece\": 0.010805, \"gen0_perplexity\": 26.948959, \"gen0_distinct_1\": 0.098216, \"gen0_distinct_2\": 0.517803, \"gen0_distinct_3\": 0.812728, \"gen10_token_entropy\": 1.27592, \"gen10_ece\": 0.41734, \"gen10_perplexity\": 1003.73, \"gen10_distinct_1\": 0.070383, \"gen10_distinct_2\": 0.335471, \"gen10_distinct_3\": 0.555579, \"token_entropy_drift_pct\": -60.5491, \"ece_drift_pct\": 3762.4711, \"perplexity_drift_pct\": 3624.5595, \"distinct_1_drift_pct\": -28.3386, \"distinct_2_drift_pct\": -35.2126, \"distinct_3_drift_pct\": -31.6402}}, \"alpha_sweep_a025_s43\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T06:58:43.090Z\", \"updated_at\": \"2026-05-15T17:39:43.623Z\", \"spec\": {\"command\": \"bash -c \\\"cd /root/autodl-tmp/distrib_canary_collapse && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_HUB_DISABLE_XET=1 && export HF_ENDPOINT=https://hf-mirror.com && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && PYTHONUNBUFFERED=1 python -u iterative_train.py --seed 43 --data_dir data/wikitext103_5k --steps_per_gen 5000 --num_generations 10 --synthetic_ratio 0.25 --output_dir results/alpha_sweep/a025_s43\\\"\", \"server\": \"westd-19828\", \"gpu\": [\"cuda:1\"], \"pid\": \"121635\", \"log_path\": \"~/runs/distrib_canary_collapse/alpha_sweep_a025_s43.log\", \"submitted_at\": \"2026-05-15T13:16:31.189Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 15792.4, \"gpu_hours\": 4.39}, \"server\": \"westd-19828\", \"gpu\": \"cuda:1\", \"pid\": \"121635\", \"log_path\": \"~/runs/distrib_canary_collapse/alpha_sweep_a025_s43.log\", \"reproduce\": {\"command\": \"bash -c \\\"cd /root/autodl-tmp/distrib_canary_collapse && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_HUB_DISABLE_XET=1 && export HF_ENDPOINT=https://hf-mirror.com && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && PYTHONUNBUFFERED=1 python -u iterative_train.py --seed 43 --data_dir data/wikitext103_5k --steps_per_gen 5000 --num_generations 10 --synthetic_ratio 0.25 --output_dir results/alpha_sweep/a025_s43\\\"\", \"finished_at\": \"2026-05-15T17:36:20.945Z\"}, \"metrics\": {\"gen0\": {\"token_entropy\": 3.2342, \"ece\": 0.0108, \"perplexity\": 26.949, \"distinct_1\": 0.09833, \"distinct_2\": 0.5132, \"distinct_3\": 0.8057, \"effective_rank\": 46.61, \"mauve\": 0.03351}, \"gen10\": {\"token_entropy\": 3.0723, \"ece\": 0.02146, \"perplexity\": 21.899, \"distinct_1\": 0.05849, \"distinct_2\": 0.2236, \"distinct_3\": 0.333, \"effective_rank\": 45.37, \"mauve\": 0.01871}, \"drift_pct\": {\"token_entropy\": -5, \"ece\": 98.6, \"perplexity\": -18.7, \"distinct_1\": -40.5, \"distinct_2\": -56.4, \"distinct_3\": -58.7, \"effective_rank\": -2.7, \"mauve\": -44.2}}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T17:36:22.072334+00:00\"}]}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a025_s43/gen_10/checkpoint\", \"completed_at\": \"2026-05-15T17:39:43.624Z\"}, \"alpha_sweep_a075_s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T21:52:17.315Z\", \"updated_at\": \"2026-05-15T13:29:46.421Z\", \"spec\": {\"hypothesis\": \"α=0.75 high contamination: critical boundary point for Granger-causal detectability — determines Claim 1 scope (α≥0.75 vs α=1.0 only)\", \"seed\": 42, \"model_name\": \"EleutherAI/pythia-410m\", \"data_path\": \"data/wikitext103_5k\", \"data_count\": 5000, \"synthetic_ratio\": 0.75, \"num_generations\": 10, \"steps_per_gen\": 5000}, \"server\": \"westd-19828\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-19828\", \"gpu\": \"cuda:1\", \"started_at\": \"2026-05-15T05:44:46.271Z\", \"command\": \"bash -c \\\"cd /root/autodl-tmp/distrib_canary_collapse && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_HUB_DISABLE_XET=1 && export HF_ENDPOINT=https://hf-mirror.com && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && PYTHONUNBUFFERED=1 python -u iterative_train.py --seed 42 --data_dir data/wikitext103_5k --steps_per_gen 5000 --num_generations 10 --synthetic_ratio 0.75 --output_dir results/alpha_sweep/a075_s42\\\"\", \"finished_at\": \"2026-05-15T13:13:06.477Z\", \"training_hours\": 7.47}, \"pid\": \"89753\", \"log_path\": \"results/analysis/cross_alpha_v6_report.md\", \"metrics\": {\"progress\": \"11/11 gen (complete)\", \"gen0_token_entropy\": 3.234, \"gen10_token_entropy\": 2.337, \"gen0_ece\": 0.0108, \"gen10_ece\": 0.2063, \"gen0_perplexity\": 26.95, \"gen10_perplexity\": 76.03, \"gen0_distinct_1\": 0.0982, \"gen10_distinct_1\": 0.0661, \"gen0_distinct_2\": 0.5178, \"gen10_distinct_2\": 0.3037, \"gen0_distinct_3\": 0.8127, \"gen10_distinct_3\": 0.5011, \"token_entropy_drift_pct\": -27.7, \"ece_drift_pct\": 1809.5, \"perplexity_drift_pct\": 182.1, \"distinct_1_drift_pct\": -32.7, \"distinct_2_drift_pct\": -41.3, \"distinct_3_drift_pct\": -38.4, \"granger_ece_to_d1_p_fdr\": 0.046, \"granger_ece_to_d2_p_fdr\": 0.046, \"granger_entropy_to_d2_p_fdr\": 0.048, \"granger_entropy_to_d1_p_fdr\": 0.054, \"granger_fdr_sig_count\": \"3/8\", \"consensus_robust_pairs\": \"11/16\", \"xcorr_entropy_d1_lag\": 2, \"xcorr_entropy_d1_r\": 0.973}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T13:13:07.582542+00:00\"}]}, \"conclusion\": \"success\", \"checkpoint_path\": \"results/alpha_sweep/a075_s42/\", \"completed_at\": \"2026-05-15T13:29:46.421Z\"}, \"alpha_sweep_a050_s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T21:52:15.427Z\", \"updated_at\": \"2026-05-15T13:17:48.134Z\", \"spec\": {\"hypothesis\": \"α=0.50 moderate contamination: test canary→diversity lead at mid-range synthetic ratio, key data point for non-monotonic dose-response\", \"seed\": 42, \"model_name\": \"EleutherAI/pythia-410m\", \"data_path\": \"data/wikitext103_5k\", \"data_count\": 5000, \"synthetic_ratio\": 0.5, \"num_generations\": 10, \"steps_per_gen\": 5000}, \"server\": \"westd-19828\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-19828\", \"gpu\": \"cuda:1\", \"started_at\": \"2026-05-15T01:15:14.747Z\", \"command\": \"bash -c \\\"cd /root/autodl-tmp/distrib_canary_collapse && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_HUB_DISABLE_XET=1 && export HF_ENDPOINT=https://hf-mirror.com && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && PYTHONUNBUFFERED=1 python -u iterative_train.py --seed 42 --data_dir data/wikitext103_5k --steps_per_gen 5000 --num_generations 10 --synthetic_ratio 0.50 --output_dir results/alpha_sweep/a050_s42\\\"\", \"finished_at\": \"2026-05-15T05:42:25.788Z\", \"training_hours\": 4.45}, \"pid\": \"73737\", \"log_path\": \"~/runs/distrib_canary_collapse/alpha_sweep_a050_s42.log\", \"metrics\": {\"progress\": \"11/11 gen (complete)\", \"gen0_token_entropy\": 3.234, \"gen10_token_entropy\": 2.632, \"gen0_ece\": 0.011, \"gen10_ece\": 0.102, \"gen0_perplexity\": 26.95, \"gen10_perplexity\": 32.64, \"gen0_distinct_1\": 0.098, \"gen10_distinct_1\": 0.062, \"gen0_distinct_2\": 0.518, \"gen10_distinct_2\": 0.251, \"gen0_distinct_3\": 0.813, \"gen10_distinct_3\": 0.387, \"token_entropy_drift_pct\": -18.6, \"ece_drift_pct\": 842.8, \"perplexity_drift_pct\": 21.1, \"distinct_1_drift_pct\": -37.3, \"distinct_2_drift_pct\": -51.5, \"distinct_3_drift_pct\": -52.4, \"granger_entropy_to_d1_p_raw\": 0.095, \"granger_entropy_to_d2_p_raw\": 0.097, \"granger_ece_to_d1_p_raw\": 0.019, \"granger_ece_to_d2_p_raw\": 0.039, \"granger_fdr_note\": \"4 tests within alpha=0.50; BH FDR threshold rank1=0.0125, rank2=0.025 → 0/4 FDR-sig at q=0.05. Raw p pattern (ECE < entropy) is qualitative signal only.\", \"d024_non_monotonic\": true, \"d024_ece_vs_entropy_note\": \"ECE raw p < entropy raw p at α=0.50 (0.019 vs 0.095 at 5000 perms), 0/4 FDR-sig; regime switch hypothesis pending α=0.75 confirmation\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T05:42:26.715028+00:00\"}]}, \"checkpoint_path\": \"/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a050_s42/gen_10/checkpoint\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T05:46:48.692Z\"}, \"plan_006_s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T23:31:35.454Z\", \"updated_at\": \"2026-05-15T12:17:14.093Z\", \"spec\": {\"command\": \"bash -c \\\"cd /root/autodl-tmp/distrib_canary_collapse && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_HUB_DISABLE_XET=1 && export HF_ENDPOINT=https://hf-mirror.com && PYTHONUNBUFFERED=1 python -u iterative_train.py --data_dir data/wikitext103 --output_dir results/extended_20gen/s42 --seed 42 --synthetic_ratio 1.0 --num_generations 20 --steps_per_gen 10000\\\"\", \"server\": \"westd-19828\", \"gpu\": [\"cuda:0\"], \"pid\": \"68368\", \"log_path\": \"~/runs/distrib_canary_collapse/plan_006_s42.log\", \"submitted_at\": \"2026-05-14T23:41:30.666Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 43212.6, \"gpu_hours\": 12.0}, \"server\": \"westd-19828\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-19828\", \"gpu\": \"cuda:0\", \"started_at\": \"2026-05-14T23:41:29.125Z\", \"command\": \"bash -c \\\"cd /root/autodl-tmp/distrib_canary_collapse && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_HUB_DISABLE_XET=1 && export HF_ENDPOINT=https://hf-mirror.com && PYTHONUNBUFFERED=1 python -u iterative_train.py --data_dir data/wikitext103 --output_dir results/extended_20gen/s42 --seed 42 --synthetic_ratio 1.0 --num_generations 20 --steps_per_gen 10000\\\"\", \"finished_at\": \"2026-05-15T11:41:42.336Z\", \"training_hours\": 12.0}, \"pid\": \"68368\", \"log_path\": \"~/runs/distrib_canary_collapse/plan_006_s42.log\", \"metrics\": {\"progress\": \"18/20 gen (gen_0-17 complete, gen_18-20 timeout)\", \"gen0_token_entropy\": 3.2342, \"gen17_token_entropy\": 1.1819, \"gen0_ece\": 0.0108, \"gen17_ece\": 0.4454, \"gen0_perplexity\": 26.95, \"gen17_perplexity\": 3367.66, \"gen0_distinct_1\": 0.0982, \"gen17_distinct_1\": 0.0756, \"gen0_distinct_2\": 0.5178, \"gen17_distinct_2\": 0.3617, \"gen0_distinct_3\": 0.8127, \"gen17_distinct_3\": 0.5865, \"token_entropy_drift_pct_gen0_17\": -63.4, \"distinct_1_drift_pct_gen0_17\": -23, \"distinct_2_drift_pct_gen0_17\": -30.1, \"distinct_3_drift_pct_gen0_17\": -27.8, \"ece_drift_pct_gen0_17\": 4024, \"ppl_drift_pct_gen0_17\": 12395, \"phase1_rapid_collapse\": \"gen0-5\", \"phase2_apparent_plateau\": \"gen5-12\", \"phase3_secondary_decline\": \"gen13-17\", \"phase3_d2_decline_pct\": -5.8, \"phase3_d3_decline_pct\": -6.9, \"diversity_saturated_at_gen\": 5, \"diversity_secondary_decline_at_gen\": 13, \"perplexity_saturated\": false}, \"failure_reason\": \"EXIT_CODE=124 (timeout — exceeded timeout_hours)\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-15T11:41:43.235Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-15T11:41:44.300301+00:00\"}]}, \"notes\": \"gen_0-17 complete (T=18). 三相 collapse: Phase1 急速崩塌 gen0-5 (d1 -20.6%, entropy -63.8%), Phase2 表观稳态 gen5-12 (diversity <0.3% 变化, perplexity 仍+167%), Phase3 二次衰退 gen13-17 (d2 -5.8%, d3 -6.9%). Perplexity 未饱和 (26.95→3367.66, +12395%). T=18 vs T=10: 新增 diversity 二次衰退在 T=10 window 不可见. TY power 预估 ~0.28-0.41 (vs T=10 的 0.05-0.21).\"}, \"plan_006_s42_resume\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T11:55:26.236Z\", \"updated_at\": \"2026-05-15T12:10:54.859Z\", \"spec\": {\"command\": \"python -u resume_plan006_s42.py\", \"server\": \"westd-19828\", \"gpu\": [\"cuda:0\"], \"pid\": \"114844\", \"log_path\": \"~/runs/distrib_canary_collapse/plan_006_s42_resume.log\", \"submitted_at\": \"2026-05-15T11:55:31.984Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"hypothesis\": \"恢复 plan_006_s42 从 gen_17，完成 gen_18-20 + all_metrics（α=1.0, 20gen, s42）\", \"seed\": 42, \"model_name\": \"EleutherAI/pythia-410m\", \"data_path\": \"data/wikitext103\", \"data_count\": 0, \"checkpoint_path\": \"N/A\", \"notes\": \"D034 决定不恢复，T=18 数据已足够（超出 T=15 目标）。plan_006_s42 gen_0-17 数据可用。\", \"wall_clock_seconds\": 921.5, \"gpu_hours\": 0.26}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-15T12:10:53.514Z\", \"notes\": \"D034 决定不恢复。T=18 数据已足够（超出 T=15 目标）。原 plan_006_s42 gen_0-17 数据可用于 power analysis + supplementary。\"}, \"gen_wiki_gpt2m_a100_s42_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T12:02:06.478Z\", \"updated_at\": \"2026-05-15T12:04:50.741Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && mkdir -p results/gen_wiki_gpt2m_a100_s42 && HF_HOME=/root/autodl-tmp/.hf_cache TRANSFORMERS_OFFLINE=1 HF_HUB_DISABLE_XET=1 PYTHONUNBUFFERED=1 python -u iterative_train.py --model_name /root/autodl-tmp/models/gpt2-medium --data_dir data/wikitext103_5k --synthetic_ratio 1.0 --num_generations 10 --steps_per_gen 5000 --batch_size 32 --seed 42 --output_dir results/gen_wiki_gpt2m_a100_s42\\\"\", \"server\": \"westd-19828\", \"gpu\": [\"cuda:0\"], \"pid\": \"116204\", \"log_path\": \"~/runs/distrib_canary_collapse/gen_wiki_gpt2m_a100_s42_v2.log\", \"submitted_at\": \"2026-05-15T12:02:14.440Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 18.0, \"gpu_hours\": 0.01}, \"server\": \"westd-19828\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-19828\", \"gpu\": \"cuda:0\", \"started_at\": \"2026-05-15T12:02:13.557Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && mkdir -p results/gen_wiki_gpt2m_a100_s42 && HF_HOME=/root/autodl-tmp/.hf_cache TRANSFORMERS_OFFLINE=1 HF_HUB_DISABLE_XET=1 PYTHONUNBUFFERED=1 python -u iterative_train.py --model_name /root/autodl-tmp/models/gpt2-medium --data_dir data/wikitext103_5k --synthetic_ratio 1.0 --num_generations 10 --steps_per_gen 5000 --batch_size 32 --seed 42 --output_dir results/gen_wiki_gpt2m_a100_s42\\\"\", \"finished_at\": \"2026-05-15T12:02:31.643Z\", \"training_hours\": 0.01}, \"pid\": \"116204\", \"log_path\": \"~/runs/distrib_canary_collapse/gen_wiki_gpt2m_a100_s42_v2.log\", \"failure_reason\": \"EXIT_CODE=1 (generic error — check log tail)\", \"conclusion\": \"killed\", \"completed_at\": \"2026-05-15T12:02:32.472Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-15T12:02:33.931882+00:00\"}]}}, \"gen_wiki_gpt2m_a100_s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T10:35:18.700Z\", \"updated_at\": \"2026-05-15T12:01:58.523Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && mkdir -p results/gen_wiki_gpt2m_a100_s42 && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_DISABLE_XET=1 PYTHONUNBUFFERED=1 python -u iterative_train.py --model_name gpt2-medium --data_dir data/wikitext103_5k --synthetic_ratio 1.0 --num_generations 10 --steps_per_gen 5000 --batch_size 32 --seed 42 --output_dir results/gen_wiki_gpt2m_a100_s42\\\"\", \"server\": \"westd-19828\", \"gpu\": [\"cuda:0\"], \"pid\": \"115532\", \"log_path\": \"~/runs/distrib_canary_collapse/gen_wiki_gpt2m_a100_s42.log\", \"submitted_at\": \"2026-05-15T11:57:48.767Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 249.8, \"gpu_hours\": 0.07}, \"server\": \"westd-19828\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-19828\", \"gpu\": \"cuda:0\", \"started_at\": \"2026-05-15T11:57:47.340Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && mkdir -p results/gen_wiki_gpt2m_a100_s42 && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_DISABLE_XET=1 PYTHONUNBUFFERED=1 python -u iterative_train.py --model_name gpt2-medium --data_dir data/wikitext103_5k --synthetic_ratio 1.0 --num_generations 10 --steps_per_gen 5000 --batch_size 32 --seed 42 --output_dir results/gen_wiki_gpt2m_a100_s42\\\"\"}, \"pid\": \"115532\", \"log_path\": \"~/runs/distrib_canary_collapse/gen_wiki_gpt2m_a100_s42.log\", \"conclusion\": \"killed\", \"completed_at\": \"2026-05-15T12:01:58.523Z\"}, \"method_ablation_phase2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T08:58:35.270Z\", \"updated_at\": \"2026-05-15T11:07:42.688Z\", \"spec\": {\"hypothesis\": \"Method sensitivity is compounded by regime dependence — method x alpha interaction is the headline Claim 3 evidence\", \"command\": \"python method_ablation_phase2.py\", \"server\": \"westd-19828\", \"data_path\": \"results/alpha_sweep + results/mvp\", \"data_count\": 56, \"model_name\": \"N/A (analysis)\", \"seed\": \"42,43,44,45\", \"checkpoint_path\": \"N/A\", \"log_path\": \"results/method_ablation_phase2_panel.json\"}, \"conclusion\": \"success\", \"metrics\": {\"n_panel_rows\": 56, \"n_alphas\": 4, \"alphas\": [0, 0.25, 0.5, 1], \"naive_sig_rate_overall\": 1, \"perm_granger_sig_rate_a000_raw\": 0, \"perm_granger_sig_rate_a000_fdr\": 0, \"perm_granger_sig_rate_a025_raw\": 0.25, \"perm_granger_sig_rate_a025_fdr\": 0, \"perm_granger_sig_rate_a050_raw\": 0.25, \"perm_granger_sig_rate_a050_fdr\": 0, \"perm_granger_sig_rate_a100_raw\": 0.75, \"perm_granger_sig_rate_a100_fdr\": 0.75, \"TY_sig_rate_a000_raw\": 0, \"TY_sig_rate_a000_fdr\": 0, \"TY_sig_rate_a025_raw\": 0.625, \"TY_sig_rate_a025_fdr\": 0.375, \"TY_sig_rate_a050_raw\": 0, \"TY_sig_rate_a050_fdr\": 0, \"TY_sig_rate_a100_raw\": 0.5938, \"TY_sig_rate_a100_fdr\": 0.5938, \"diff_sig_rate_a000_raw\": 0.5, \"diff_sig_rate_a000_fdr\": 0.375, \"mean_inter_method_kappa\": 0.185, \"naive_vs_perm_granger_flip_rate\": 0.5, \"naive_vs_TY_flip_rate\": 0.57, \"fdr_flips_perm_granger\": 4, \"pair_verdict_a100_perm_granger\": \"6/8\", \"pair_verdict_a100_TY\": \"6/8\", \"entropy_to_diversity_a100_all_5methods_sig\": true, \"fdr_correction\": \"BH q=0.05\"}, \"completed_at\": \"2026-05-15T08:58:54.741Z\"}, \"alpha_sweep_a025_s42_v3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T21:04:05.726Z\", \"updated_at\": \"2026-05-15T05:13:22.207Z\", \"spec\": {\"hypothesis\": \"α=0.25 低污染: 测试 canary→diversity lead 在温和 collapse 下是否保持\", \"model_name\": \"EleutherAI/pythia-410m\", \"data_path\": \"/root/autodl-tmp/distrib_canary_collapse/data/wikitext103_5k\", \"data_count\": 5000, \"seed\": 42, \"synthetic_ratio\": 0.25, \"num_generations\": 10, \"steps_per_gen\": 5000, \"parent\": \"alpha_sweep_a025_s42_v2 (failed, data corruption)\", \"command\": \"bash -c \\\"cd /root/autodl-tmp/distrib_canary_collapse && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_HUB_DISABLE_XET=1 && export HF_ENDPOINT=https://hf-mirror.com && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && PYTHONUNBUFFERED=1 python -u iterative_train.py --seed 42 --data_dir data/wikitext103_5k --steps_per_gen 5000 --num_generations 10 --synthetic_ratio 0.25 --output_dir results/alpha_sweep/a025_s42\\\"\", \"server\": \"westd-19828\", \"gpu\": [\"cuda:1\"], \"pid\": \"53069\", \"log_path\": \"~/runs/distrib_canary_collapse/alpha_sweep_a025_s42_v3.log\"}, \"reproduce\": {\"finished_at\": \"2026-05-15T01:18:42.377Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T01:18:43.329069+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"gen0_token_entropy\": 3.2342, \"gen10_token_entropy\": 3.1017, \"gen0_ece\": 0.0108, \"gen10_ece\": 0.01942, \"gen0_perplexity\": 26.95, \"gen10_perplexity\": 22.32, \"gen0_distinct_1\": 0.0982, \"gen10_distinct_1\": 0.0586, \"gen0_distinct_2\": 0.5178, \"gen10_distinct_2\": 0.2219, \"gen0_distinct_3\": 0.8127, \"gen10_distinct_3\": 0.3263, \"token_entropy_drift_pct\": -4.1, \"ece_drift_pct\": 79.7, \"perplexity_drift_pct\": -17.2, \"distinct_1_drift_pct\": -40.3, \"distinct_2_drift_pct\": -57.1, \"distinct_3_drift_pct\": -59.9}, \"checkpoint_path\": \"/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a025_s42/gen_10/checkpoint\", \"completed_at\": \"2026-05-15T01:26:19.292Z\", \"notes\": \"实际磁盘路径为 results/alpha_sweep/a025_s42/（无 v3 后缀）。Registry ID 带 v3 是历史原因，数据已核实无误。\"}, \"method_ablation_phase1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T23:49:16.519Z\", \"updated_at\": \"2026-05-14T23:49:40.162Z\", \"spec\": {\"plan_id\": \"plan_002\", \"hypothesis\": \"lead-lag 结论对分析方法高度敏感——naive Pearson 100% SIG vs TY 25% SIG，方法选择改变 75% 的结论\", \"command\": \"python method_ablation.py + python permutation_granger.py (差分版)\", \"server\": \"westd-19828\", \"data_path\": \"results/mvp/rep_{42,43,44,45}/all_metrics.json\", \"data_count\": 4, \"model_name\": \"N/A (analysis on MVP data)\", \"seed\": \"42,43,44,45\", \"checkpoint_path\": \"N/A\", \"log_path\": \"results/mvp/analysis/method_ablation.json\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T23:49:37.295Z\", \"metrics\": {\"spurious_rate_5method\": 0.75, \"spurious_rate_4method\": 0.625, \"naive_sig\": \"16/16\", \"differenced_sig\": \"14/16\", \"threshold_sig\": \"9/16\", \"permutation_granger_sig\": \"6/16\", \"ty_sig\": \"4/16\", \"ty_power_T10\": \"0.05-0.20\", \"bh_fdr_flips\": 0}}, \"alpha_sweep_a000_s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T19:01:37.470Z\", \"updated_at\": \"2026-05-14T23:42:18.748Z\", \"spec\": {\"hypothesis\": \"α=0.0 null control: 纯 real data 再训练无 canary signal，确认 signal 源于合成污染\", \"model_name\": \"EleutherAI/pythia-410m\", \"data_path\": \"/root/autodl-tmp/distrib_canary_collapse/data/wikitext103_5k\", \"data_count\": 5000, \"seed\": 42, \"synthetic_ratio\": 0, \"num_generations\": 10, \"steps_per_gen\": 5000, \"command\": \"bash -c \\\"cd /root/autodl-tmp/distrib_canary_collapse && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_HUB_DISABLE_XET=1 && export HF_ENDPOINT=https://hf-mirror.com && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && PYTHONUNBUFFERED=1 python -u iterative_train.py --seed 42 --data_dir data/wikitext103_5k --steps_per_gen 5000 --num_generations 10 --synthetic_ratio 0.0 --output_dir results/alpha_sweep/a000_s42\\\"\", \"server\": \"westd-19828\", \"gpu\": [\"cuda:0\"], \"pid\": \"46716\", \"log_path\": \"~/runs/distrib_canary_collapse/alpha_sweep_a000_s42.log\"}, \"reproduce\": {\"finished_at\": \"2026-05-14T23:36:35.414Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T23:36:36.221435+00:00\"}]}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a000_s42/gen_10/checkpoint\", \"log_path\": \"~/runs/distrib_canary_collapse/alpha_sweep_a000_s42.log\", \"metrics\": {\"gen0_token_entropy\": 3.2342, \"gen10_token_entropy\": 3.0693, \"gen0_ece\": 0.0108, \"gen10_ece\": 0.0164, \"gen0_perplexity\": 26.95, \"gen10_perplexity\": 21.11, \"gen0_distinct_1\": 0.0982, \"gen10_distinct_1\": 0.0847, \"token_entropy_drift_pct\": -5.1, \"ece_drift_pct\": 51.7, \"perplexity_drift_pct\": -21.7, \"distinct_1_drift_pct\": -13.8, \"distinct_2_drift_pct\": -9.8, \"distinct_3_drift_pct\": -4.5, \"gen1_10_perplexity_drift_pct\": 9.4, \"gen1_10_distinct_1_drift_pct\": -13.1, \"gen1_10_entropy_drift_pct\": 2.6}, \"completed_at\": \"2026-05-14T23:39:04.310Z\"}, \"plan_009_bootstrap_ty\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T21:33:04.665Z\", \"updated_at\": \"2026-05-14T21:33:27.106Z\", \"spec\": {\"hypothesis\": \"Monte Carlo 验证 TY Granger 在短时间序列 (T=10,15,20,30) 下的 Type I error 和 statistical power\", \"command\": \"python bootstrap_ty_validation.py (N_sim=1000)\", \"server\": \"westd-19828\", \"data_path\": \"synthetic DGP (AR(1) for H0, VAR(2) for H1)\", \"data_count\": 1000, \"model_name\": \"N/A (statistical simulation)\", \"seed\": \"multiple\", \"log_path\": \"results/bootstrap_ty_results.json\", \"checkpoint_path\": \"N/A\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T21:33:24.769Z\", \"metrics\": {\"T10_d0_type1\": 0.081, \"T10_d0_power\": 0.205, \"T10_d1_type1\": 0.047, \"T10_d1_power\": 0.09, \"T10_dadapt_type1\": 0.052, \"T10_dadapt_power\": 0.05, \"T20_d0_power\": 0.409, \"T20_d1_power\": 0.172, \"T30_d0_power\": 0.606, \"T30_d1_power\": 0.283}}, \"mvp_v3_rep43\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T06:25:42.195Z\", \"updated_at\": \"2026-05-14T06:48:01.316Z\", \"spec\": {\"command\": \"python iterative_train.py --seed 43 --output_dir results/mvp/rep_43 --data_dir data/wikitext103_5k --synthetic_ratio 1.0 --num_generations 10 --steps_per_gen 5000\", \"server\": \"autodl-rtx6000\", \"gpu\": \"cuda:1\", \"pid\": \"7987\", \"log_path\": \"~/runs/distrib_canary_collapse/mvp_v3_rep43.log\", \"submitted_at\": \"2026-05-14T06:26:18.477Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/distrib_canary_collapse/data/wikitext103_5k\", \"data_count\": 5000, \"model_name\": \"EleutherAI/pythia-410m\", \"seed\": 43, \"gpu_model\": \"RTX PRO 6000 Blackwell 96GB\", \"tmux_session\": \"mvp_v3_rep43\", \"checkpoint_path\": \"N/A\", \"failure_reason\": \"MAUVE FAISS crash: max_samples=500 → p+q=1000 < 1950 required; 无 PYTHONUNBUFFERED 导致日志丢失\", \"wall_clock_seconds\": 1302.8, \"gpu_hours\": 0.36}, \"conclusion\": \"failed\", \"completed_at\": \"2026-05-14T06:48:01.316Z\"}, \"mvp_v3_rep42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T06:25:39.728Z\", \"updated_at\": \"2026-05-14T06:47:59.908Z\", \"spec\": {\"command\": \"python iterative_train.py --seed 42 --output_dir results/mvp/rep_42 --data_dir data/wikitext103_5k --synthetic_ratio 1.0 --num_generations 10 --steps_per_gen 5000\", \"server\": \"autodl-rtx6000\", \"gpu\": \"cuda:0\", \"pid\": \"7909\", \"log_path\": \"~/runs/distrib_canary_collapse/mvp_v3_rep42.log\", \"submitted_at\": \"2026-05-14T06:26:16.939Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/distrib_canary_collapse/data/wikitext103_5k\", \"data_count\": 5000, \"model_name\": \"EleutherAI/pythia-410m\", \"seed\": 42, \"gpu_model\": \"RTX PRO 6000 Blackwell 96GB\", \"tmux_session\": \"mvp_v3_rep42\", \"checkpoint_path\": \"N/A\", \"failure_reason\": \"MAUVE FAISS crash: max_samples=500 → p+q=1000 < 1950 required; 无 PYTHONUNBUFFERED 导致日志丢失\", \"wall_clock_seconds\": 1303.0, \"gpu_hours\": 0.36}, \"conclusion\": \"failed\", \"completed_at\": \"2026-05-14T06:47:59.908Z\"}, \"mvp_v2_rep43\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T05:38:10.434Z\", \"updated_at\": \"2026-05-14T06:25:28.345Z\", \"spec\": {\"command\": \"python iterative_train.py --seed 43 --output_dir results/mvp/rep_43 --data_dir data/wikitext103_5k --synthetic_ratio 1.0 --num_generations 10 --steps_per_gen 5000\", \"server\": \"autodl-rtx6000\", \"gpu\": \"cuda:1\", \"pid\": \"5364\", \"log_path\": \"~/runs/distrib_canary_collapse/mvp_v2_rep43.log\", \"submitted_at\": \"2026-05-14T05:42:39.039Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/distrib_canary_collapse/data/wikitext103_5k\", \"data_count\": 5000, \"model_name\": \"EleutherAI/pythia-410m\", \"seed\": 43, \"gpu_model\": \"RTX PRO 6000 Blackwell 96GB\", \"tmux_session\": \"mvp_v2_rep43\", \"checkpoint_path\": \"N/A\", \"kill_reason\": \"v1旧进程未死导致输出目录冲突，v2死锁\", \"wall_clock_seconds\": 2569.3, \"gpu_hours\": 0.71}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-14T06:25:28.345Z\"}, \"mvp_v2_rep42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T05:38:05.054Z\", \"updated_at\": \"2026-05-14T06:25:27.286Z\", \"spec\": {\"command\": \"python iterative_train.py --seed 42 --output_dir results/mvp/rep_42 --data_dir data/wikitext103_5k --synthetic_ratio 1.0 --num_generations 10 --steps_per_gen 5000\", \"server\": \"autodl-rtx6000\", \"gpu\": \"cuda:0\", \"pid\": \"5286\", \"log_path\": \"~/runs/distrib_canary_collapse/mvp_v2_rep42.log\", \"submitted_at\": \"2026-05-14T05:42:37.404Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/distrib_canary_collapse/data/wikitext103_5k\", \"data_count\": 5000, \"model_name\": \"EleutherAI/pythia-410m\", \"seed\": 42, \"gpu_model\": \"RTX PRO 6000 Blackwell 96GB\", \"tmux_session\": \"mvp_v2_rep42\", \"checkpoint_path\": \"N/A\", \"kill_reason\": \"v1旧进程未死导致输出目录冲突，v2死锁\", \"wall_clock_seconds\": 2569.9, \"gpu_hours\": 0.71}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-14T06:25:27.286Z\"}, \"mvp_rep43\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T05:12:14.237Z\", \"updated_at\": \"2026-05-14T05:37:18.575Z\", \"spec\": {\"command\": \"python iterative_train.py --seed 43 --output_dir results/mvp/rep_43 --data_dir data/wikitext103 --synthetic_ratio 1.0 --num_generations 10 --steps_per_gen 10000\", \"server\": \"autodl-rtx6000\", \"gpu\": \"cuda:1\", \"pid\": \"3956\", \"log_path\": \"~/runs/distrib_canary_collapse/mvp_rep43.log\", \"submitted_at\": \"2026-05-14T05:34:47.702Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/distrib_canary_collapse/data/wikitext103\", \"data_count\": 716506, \"model_name\": \"EleutherAI/pythia-410m\", \"seed\": 43, \"gpu_model\": \"RTX PRO 6000 Blackwell 96GB\", \"tmux_session\": \"mvp_rep43\", \"checkpoint_path\": \"N/A\", \"kill_reason\": \"参数修复: n_prompts 1000→5000, steps_per_gen 10000→5000\", \"wall_clock_seconds\": 150.9, \"gpu_hours\": 0.04}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-14T05:37:18.575Z\"}, \"mvp_rep42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T05:12:13.930Z\", \"updated_at\": \"2026-05-14T05:37:17.438Z\", \"spec\": {\"command\": \"python iterative_train.py --seed 42 --output_dir results/mvp/rep_42 --data_dir data/wikitext103 --synthetic_ratio 1.0 --num_generations 10 --steps_per_gen 10000\", \"server\": \"autodl-rtx6000\", \"gpu\": \"cuda:0\", \"pid\": \"3878\", \"log_path\": \"~/runs/distrib_canary_collapse/mvp_rep42.log\", \"submitted_at\": \"2026-05-14T05:34:46.013Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/distrib_canary_collapse/data/wikitext103\", \"data_count\": 716506, \"model_name\": \"EleutherAI/pythia-410m\", \"seed\": 42, \"gpu_model\": \"RTX PRO 6000 Blackwell 96GB\", \"tmux_session\": \"mvp_rep42\", \"checkpoint_path\": \"N/A\", \"kill_reason\": \"参数修复: n_prompts 1000→5000, steps_per_gen 10000→5000\", \"wall_clock_seconds\": 151.4, \"gpu_hours\": 0.04}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-14T05:37:17.438Z\"}}, \"count\": 34, \"total\": 34, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.0843}}"
    }
  },
  "sourceToolAssistantUUID": "ae37fdbe-6975-4d3d-aab1-cbae7f8aed59",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/agent_e1f64cd5",
  "sessionId": "4f6074eb-8665-49ec-9526-07c9eebcea03",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-16T02:24:43.095Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01M15WUQPFGxTQitsn4Q6xrc`</summary>

```json
{
  "project": "distrib_canary_collapse",
  "file": "report.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7b5c18e8-3f88-41a2-aab6-2d99aa199d56",
  "isSidechain": false,
  "requestId": "req_011Cb5THVYi5x3MbotvkQmr1",
  "type": "assistant",
  "uuid": "e27a3deb-b407-4b5e-ac4a-9ca6c71df018",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/agent_e1f64cd5",
  "sessionId": "4f6074eb-8665-49ec-9526-07c9eebcea03",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DbAG94MdMh8gN9pNd7MbVZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 3204,
      "cache_read_input_tokens": 34826,
      "output_tokens": 271,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3204,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 271,
          "cache_read_input_tokens": 34826,
          "cache_creation_input_tokens": 3204,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3204
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

_source line 17 · 2026-05-16T02:24:43.100Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_roadmap · `toolu_01HjtZvtmapsSxG7F8N9qNYL`</summary>

```json
{
  "project": "distrib_canary_collapse"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e27a3deb-b407-4b5e-ac4a-9ca6c71df018",
  "isSidechain": false,
  "requestId": "req_011Cb5THVYi5x3MbotvkQmr1",
  "type": "assistant",
  "uuid": "083420db-5d99-4ea3-b894-3f9c3c7d9709",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/agent_e1f64cd5",
  "sessionId": "4f6074eb-8665-49ec-9526-07c9eebcea03",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DbAG94MdMh8gN9pNd7MbVZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 3204,
      "cache_read_input_tokens": 34826,
      "output_tokens": 271,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3204,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 271,
          "cache_read_input_tokens": 34826,
          "cache_creation_input_tokens": 3204,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3204
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
  "lastPrompt": "[CRON] 实验进程已正常退出，状态已转为 ANALYZING，需要你分析结果并推进到 DONE。 详情: Process exited cleanly, W&B data available  - exp_id: alpha_sweep_a025_s44 - project: distrib_canary_collapse - server: westd-19828 - log_path: ~…",
  "leafUuid": "083420db-5d99-4ea3-b894-3f9c3c7d9709",
  "sessionId": "4f6074eb-8665-49ec-9526-07c9eebcea03"
}
```

---

### Runtime record

_source line 19_

```json
{
  "type": "ai-title",
  "aiTitle": "Analyze experiment results and mark complete",
  "sessionId": "4f6074eb-8665-49ec-9526-07c9eebcea03"
}
```

---

### Tool result

_source line 20 · 2026-05-16T02:24:44.015Z_

<details><summary>↩ Tool result · `toolu_012SkYJQZcdpD2hFxAzWhjD1`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"reconciled\": 1, \"results\": [{\"exp_id\": \"gen_wiki_gpt2m_a025_s42\", \"success\": true, \"actions\": [\"Job still running (pid=149202)\"]}]}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5ec36bd0-c86c-42c1-a9f2-fefd98aec14c",
  "isSidechain": false,
  "promptId": "a304cee9-feed-4fb2-a028-8ae1d93109aa",
  "type": "user",
  "uuid": "a7726fe2-e95c-49a5-bcb9-ac243c9731cd",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"reconciled\\\": 1, \\\"results\\\": [{\\\"exp_id\\\": \\\"gen_wiki_gpt2m_a025_s42\\\", \\\"success\\\": true, \\\"actions\\\": [\\\"Job still running (pid=149202)\\\"]}]}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"reconciled\": 1, \"results\": [{\"exp_id\": \"gen_wiki_gpt2m_a025_s42\", \"success\": true, \"actions\": [\"Job still running (pid=149202)\"]}]}, \"error\": null, \"metadata\": {}}"
    }
  },
  "sourceToolAssistantUUID": "5ec36bd0-c86c-42c1-a9f2-fefd98aec14c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/agent_e1f64cd5",
  "sessionId": "4f6074eb-8665-49ec-9526-07c9eebcea03",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-16T02:24:44.025Z_

<details><summary>↩ Tool result · `toolu_01M15WUQPFGxTQitsn4Q6xrc`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/report.md\", \"content\": \"&lt;!-- AUTO-FACTS-BEGIN (generated 2026-05-16T02:24:25Z; do not edit — regenerated by auto_build_report_facts) -->\\n## 📊 当前状态（auto-derived from registry）\\n\\n**总计**: 34 个实验 — ANALYZING 1, DONE 32, RUNNING 1\\n**DONE 分布**: failed 3, killed 15, success 14\\n\\n### GPU 占用\\n- **分配**: 2 张 — westd-19828:cuda:0, westd-19828:cuda:1\\n- **实际运行**: 1 张 — westd-19828:cuda:0(gen_wiki_gpt2m_a025_s42)\\n- **空闲（分配了没跑）**: westd-19828:cuda:1\\n\\n### 🏃 RUNNING\\n| exp_id | server | gpu | pid | log |\\n|--------|--------|-----|-----|-----|\\n| `gen_wiki_gpt2m_a025_s42` | westd-19828 | cuda:0 | 149202 | `~/runs/distrib_canary_collapse/gen_wiki_gpt2m_a025_s42.log` |\\n\\n### 📌 最近完成 (top 5)\\n- `mvp_v2_rep44` [killed] — 2026-05-16T00:10:26\\n- `mvp_rep44` [killed] — 2026-05-16T00:10:25\\n- `alpha_sweep_a025_s42` [killed] — 2026-05-16T00:10:24\\n- `alpha_sweep_a025_s42_v2` [killed] — 2026-05-16T00:10:24 — data corruption: unkilled old process PID 46802 wrote concurrently with new PID \\n- `alpha_sweep_a060_s42` [killed] — 2026-05-16T00:04:01\\n\\n### 🔴 最近失败原因 (top 3)\\n- `mvp_v2_rep44`: _(no failure_reason — pre-2026-04-24 entry)_\\n- `mvp_rep44`: _(no failure_reason — pre-2026-04-24 entry)_\\n- `alpha_sweep_a025_s42`: _(no failure_reason — pre-2026-04-24 entry)_\\n\\n&lt;!-- AUTO-FACTS-END -->\\n\\n---\\n\\n# Handover — 2026-05-16\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\\n|--------|------|------|---------|-----|\\n| gen_wiki_gpt2m_a025_s42 | — | — | — | — |\\n| alpha_sweep_a025_s44 | — | — | — | — |\\n\\n## 待处理\\n（无）\\n\\n## 近期结论\\n- **mvp_v2_rep44** (killed): —\\n- **mvp_rep44** (killed): —\\n- **alpha_sweep_a025_s42** (killed): —\\n\\n## 趋势\\n成功 14 / 负向 0 / 失败 3 / 共 32\\n累计 GPU: 8.4h\\ndistinct_1_drift_pct: -12.4 ↑（近 3 次 success）\\ndistinct_2_drift_pct: -14.7 ↑（近 3 次 success）\\n\\n## 下一步\\n（无活跃 idea，请通过 ideas.md 添加）\\n\\n## 资源状态\\nwestd-19828: 空闲 cuda:0, cuda:1\\n\\n## 告警\\n- mvp_rep42: 已被终止 — unknown\\n- mvp_rep43: 已被终止 — unknown\\n- mvp_rep44: 已被终止 — unknown\\n- mvp_v2_rep42: 已被终止 — unknown\\n- mvp_v2_rep43: 已被终止 — unknown\\n- mvp_v2_rep44: 已被终止 — unknown\\n- mvp_v3_rep42: 训练失败 — unknown\\n- mvp_v3_rep43: 训练失败 — unknown\\n- alpha_sweep_a025_s42: 已被终止 — unknown\\n- alpha_sweep_a025_s42_v2: 已被终止 — unknown\\n- alpha_sweep_a010_s42: 已被终止 — unknown\\n- alpha_sweep_a060_s42: 已被终止 — unknown\\n- plan_006_s42: 训练失败 — unknown\\n- plan_006_s43: 已被终止 — unknown\\n- alpha_sweep_a050_s44: 已被终止 — unknown\\n- gen_wiki_gpt2m_a100_s42: 已被终止 — unknown\\n- plan_006_s42_resume: 已被终止 — unknown\\n- gen_wiki_gpt2m_a100_s42_v2: 已被终止 — unknown\\n\", \"total_chars\": 2431, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e27a3deb-b407-4b5e-ac4a-9ca6c71df018",
  "isSidechain": false,
  "promptId": "a304cee9-feed-4fb2-a028-8ae1d93109aa",
  "type": "user",
  "uuid": "534abc6d-ec6d-4357-9ff3-b47a5d67bc81",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/report.md\\\", \\\"content\\\": \\\"&lt;!-- AUTO-FACTS-BEGIN (generated 2026-05-16T02:24:25Z; do not edit — regenerated by auto_build_report_facts) -->\\\\n## 📊 当前状态（auto-derived from registry）\\\\n\\\\n**总计**: 34 个实验 — ANALYZING 1, DONE 32, RUNNING 1\\\\n**DONE 分布**: failed 3, killed 15, success 14\\\\n\\\\n### GPU 占用\\\\n- **分配**: 2 张 — westd-19828:cuda:0, westd-19828:cuda:1\\\\n- **实际运行**: 1 张 — westd-19828:cuda:0(gen_wiki_gpt2m_a025_s42)\\\\n- **空闲（分配了没跑）**: westd-19828:cuda:1\\\\n\\\\n### 🏃 RUNNING\\\\n| exp_id | server | gpu | pid | log |\\\\n|--------|--------|-----|-----|-----|\\\\n| `gen_wiki_gpt2m_a025_s42` | westd-19828 | cuda:0 | 149202 | `~/runs/distrib_canary_collapse/gen_wiki_gpt2m_a025_s42.log` |\\\\n\\\\n### 📌 最近完成 (top 5)\\\\n- `mvp_v2_rep44` [killed] — 2026-05-16T00:10:26\\\\n- `mvp_rep44` [killed] — 2026-05-16T00:10:25\\\\n- `alpha_sweep_a025_s42` [killed] — 2026-05-16T00:10:24\\\\n- `alpha_sweep_a025_s42_v2` [killed] — 2026-05-16T00:10:24 — data corruption: unkilled old process PID 46802 wrote concurrently with new PID \\\\n- `alpha_sweep_a060_s42` [killed] — 2026-05-16T00:04:01\\\\n\\\\n### 🔴 最近失败原因 (top 3)\\\\n- `mvp_v2_rep44`: _(no failure_reason — pre-2026-04-24 entry)_\\\\n- `mvp_rep44`: _(no failure_reason — pre-2026-04-24 entry)_\\\\n- `alpha_sweep_a025_s42`: _(no failure_reason — pre-2026-04-24 entry)_\\\\n\\\\n&lt;!-- AUTO-FACTS-END -->\\\\n\\\\n---\\\\n\\\\n# Handover — 2026-05-16\\\\n\\\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\\\n\\\\n## 运行中\\\\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\\\\n|--------|------|------|---------|-----|\\\\n| gen_wiki_gpt2m_a025_s42 | — | — | — | — |\\\\n| alpha_sweep_a025_s44 | — | — | — | — |\\\\n\\\\n## 待处理\\\\n（无）\\\\n\\\\n## 近期结论\\\\n- **mvp_v2_rep44** (killed): —\\\\n- **mvp_rep44** (killed): —\\\\n- **alpha_sweep_a025_s42** (killed): —\\\\n\\\\n## 趋势\\\\n成功 14 / 负向 0 / 失败 3 / 共 32\\\\n累计 GPU: 8.4h\\\\ndistinct_1_drift_pct: -12.4 ↑（近 3 次 success）\\\\ndistinct_2_drift_pct: -14.7 ↑（近 3 次 success）\\\\n\\\\n## 下一步\\\\n（无活跃 idea，请通过 ideas.md 添加）\\\\n\\\\n## 资源状态\\\\nwestd-19828: 空闲 cuda:0, cuda:1\\\\n\\\\n## 告警\\\\n- mvp_rep42: 已被终止 — unknown\\\\n- mvp_rep43: 已被终止 — unknown\\\\n- mvp_rep44: 已被终止 — unknown\\\\n- mvp_v2_rep42: 已被终止 — unknown\\\\n- mvp_v2_rep43: 已被终止 — unknown\\\\n- mvp_v2_rep44: 已被终止 — unknown\\\\n- mvp_v3_rep42: 训练失败 — unknown\\\\n- mvp_v3_rep43: 训练失败 — unknown\\\\n- alpha_sweep_a025_s42: 已被终止 — unknown\\\\n- alpha_sweep_a025_s42_v2: 已被终止 — unknown\\\\n- alpha_sweep_a010_s42: 已被终止 — unknown\\\\n- alpha_sweep_a060_s42: 已被终止 — unknown\\\\n- plan_006_s42: 训练失败 — unknown\\\\n- plan_006_s43: 已被终止 — unknown\\\\n- alpha_sweep_a050_s44: 已被终止 — unknown\\\\n- gen_wiki_gpt2m_a100_s42: 已被终止 — unknown\\\\n- plan_006_s42_resume: 已被终止 — unknown\\\\n- gen_wiki_gpt2m_a100_s42_v2: 已被终止 — unknown\\\\n\\\", \\\"total_chars\\\": 2431, \\\"truncated\\\": false}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/report.md\", \"content\": \"&lt;!-- AUTO-FACTS-BEGIN (generated 2026-05-16T02:24:25Z; do not edit — regenerated by auto_build_report_facts) -->\\n## 📊 当前状态（auto-derived from registry）\\n\\n**总计**: 34 个实验 — ANALYZING 1, DONE 32, RUNNING 1\\n**DONE 分布**: failed 3, killed 15, success 14\\n\\n### GPU 占用\\n- **分配**: 2 张 — westd-19828:cuda:0, westd-19828:cuda:1\\n- **实际运行**: 1 张 — westd-19828:cuda:0(gen_wiki_gpt2m_a025_s42)\\n- **空闲（分配了没跑）**: westd-19828:cuda:1\\n\\n### 🏃 RUNNING\\n| exp_id | server | gpu | pid | log |\\n|--------|--------|-----|-----|-----|\\n| `gen_wiki_gpt2m_a025_s42` | westd-19828 | cuda:0 | 149202 | `~/runs/distrib_canary_collapse/gen_wiki_gpt2m_a025_s42.log` |\\n\\n### 📌 最近完成 (top 5)\\n- `mvp_v2_rep44` [killed] — 2026-05-16T00:10:26\\n- `mvp_rep44` [killed] — 2026-05-16T00:10:25\\n- `alpha_sweep_a025_s42` [killed] — 2026-05-16T00:10:24\\n- `alpha_sweep_a025_s42_v2` [killed] — 2026-05-16T00:10:24 — data corruption: unkilled old process PID 46802 wrote concurrently with new PID \\n- `alpha_sweep_a060_s42` [killed] — 2026-05-16T00:04:01\\n\\n### 🔴 最近失败原因 (top 3)\\n- `mvp_v2_rep44`: _(no failure_reason — pre-2026-04-24 entry)_\\n- `mvp_rep44`: _(no failure_reason — pre-2026-04-24 entry)_\\n- `alpha_sweep_a025_s42`: _(no failure_reason — pre-2026-04-24 entry)_\\n\\n&lt;!-- AUTO-FACTS-END -->\\n\\n---\\n\\n# Handover — 2026-05-16\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\\n|--------|------|------|---------|-----|\\n| gen_wiki_gpt2m_a025_s42 | — | — | — | — |\\n| alpha_sweep_a025_s44 | — | — | — | — |\\n\\n## 待处理\\n（无）\\n\\n## 近期结论\\n- **mvp_v2_rep44** (killed): —\\n- **mvp_rep44** (killed): —\\n- **alpha_sweep_a025_s42** (killed): —\\n\\n## 趋势\\n成功 14 / 负向 0 / 失败 3 / 共 32\\n累计 GPU: 8.4h\\ndistinct_1_drift_pct: -12.4 ↑（近 3 次 success）\\ndistinct_2_drift_pct: -14.7 ↑（近 3 次 success）\\n\\n## 下一步\\n（无活跃 idea，请通过 ideas.md 添加）\\n\\n## 资源状态\\nwestd-19828: 空闲 cuda:0, cuda:1\\n\\n## 告警\\n- mvp_rep42: 已被终止 — unknown\\n- mvp_rep43: 已被终止 — unknown\\n- mvp_rep44: 已被终止 — unknown\\n- mvp_v2_rep42: 已被终止 — unknown\\n- mvp_v2_rep43: 已被终止 — unknown\\n- mvp_v2_rep44: 已被终止 — unknown\\n- mvp_v3_rep42: 训练失败 — unknown\\n- mvp_v3_rep43: 训练失败 — unknown\\n- alpha_sweep_a025_s42: 已被终止 — unknown\\n- alpha_sweep_a025_s42_v2: 已被终止 — unknown\\n- alpha_sweep_a010_s42: 已被终止 — unknown\\n- alpha_sweep_a060_s42: 已被终止 — unknown\\n- plan_006_s42: 训练失败 — unknown\\n- plan_006_s43: 已被终止 — unknown\\n- alpha_sweep_a050_s44: 已被终止 — unknown\\n- gen_wiki_gpt2m_a100_s42: 已被终止 — unknown\\n- plan_006_s42_resume: 已被终止 — unknown\\n- gen_wiki_gpt2m_a100_s42_v2: 已被终止 — unknown\\n\", \"total_chars\": 2431, \"truncated\": false}, \"error\": null, \"metadata\": {}}"
    }
  },
  "sourceToolAssistantUUID": "e27a3deb-b407-4b5e-ac4a-9ca6c71df018",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/agent_e1f64cd5",
  "sessionId": "4f6074eb-8665-49ec-9526-07c9eebcea03",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-16T02:24:44.036Z_

<details><summary>↩ Tool result · `toolu_01HjtZvtmapsSxG7F8N9qNYL`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/ROADMAP.md\", \"content\": \"# distrib_canary_collapse — Research Dashboard\\n\\n> 最后更新: 2026-05-15 23:54 UTC | 更新原因: 标记零 GPU 分析 A/B/C + T-notation patch 完成，更新收敛路线剩余任务\\n\\n## 核心方向\\n**D027 reframe**: 以方法论陷阱 + 多方法共识框架为主线，canary prediction 为系统性 case study。暴露 lead-lag 分析中的方法选择敏感性（Claim 3 领衔）、伪回归陷阱（Claim 1 case study）、regime-dependent validity（Claim 2）。详见 paper_framing.md。\\n\\n**Title direction**: \\\"Method Matters: Pitfalls and a Multi-Method Consensus Framework for Lead-Lag Analysis in Iterative Training Collapse\\\"\\n\\n## 当前进展\\n- **阶段**: Research 收敛期 + 审稿进行中 + Paper Agent Step 5 运行中\\n- **Target**: **EMNLP 2026 main track**（D043）\\n- **证据强度**: Claim 3 (方法敏感性跨架构复现, Tier 3, 4/5 唯一最优, κ 跨架构一致) > Claim 2 (regime map, 待 gpt2m_a025 跨架构确认) > Claim 1 (case study, 跨架构复现)\\n- **跨架构验证**: ✅ GPT-2m 5-method Tier 3 confirmatory\\n- **Claim 措辞上限**: \\\"consistent across two transformer decoder-only model families of similar scale\\\"\\n- **零 GPU 分析**: ✅ 全部完成（window sensitivity + method subset ablation + κ），已写入论文，T-notation 已修正\\n- **D044 收敛决策**: 砍低 ROI 实验，转投零 GPU 分析（已完成）\\n- **累计 GPU**: ~23h\\n\\n## 正在运行\\n| 实验 | GPU | 角色 | 备注 |\\n|------|-----|------|------|\\n| gpt2m_a025_s42 | cuda:0 | Claim 2 cross-arch | α=0.25, ~3h remaining |\\n| a025_s44 | cuda:1 | D026 multi-seed #3 | 完成即止，不再追加 |\\n\\n## 近期任务（收敛路线）\\n- [x] **零 GPU 分析 A**: Observation window sensitivity — 4/5 从 T≥5(paper) 即锁定\\n- [x] **零 GPU 分析 B**: Method subset ablation — 4/5 唯一最优，PermG linchpin\\n- [x] **零 GPU 分析 C**: GPT-2m κ=0.091 — 低 κ 跨架构一致\\n- [x] **T-notation patch**: discussion.tex L30-31 修正完成\\n- [ ] **gpt2m_a025 完成** → 分析 regime-dependent 跨架构复现 → 写入论文\\n- [ ] **Paper Agent**: W1-W4 修复 + GPT-2m α=0.25 结果整合\\n- [ ] **Claim 强度 + 叙事调整讨论** → 与 Reviewer 深入评估\\n- [ ] **Step 5 收敛** → 最终 proofread + compile → submit_paper_to_review\\n\\n## 已砍任务（D044）\\n- ~~a050_s44~~ — 2 seed 已足够（<7% deviation）\\n- ~~alpha_sweep_a010_s42~~ — null regime 无新信息\\n- ~~plan_006_s43~~ — D035 已排除\\n\\n## WA → Accept 路径\\n1. ✅ 共识框架 formalization\\n2. ✅ FDR 修复全链路\\n3. ✅ 论文结构终版 + prescriptive 升级\\n4. ✅ GPT-2m 5-method Tier 3 cross-arch validation\\n5. ✅ 零 GPU 分析 A+B+C（window sensitivity + method ablation + κ）\\n6. 🔄 gpt2m_a025_s42 → regime map 跨架构确认\\n7. Paper Agent W1-W4 + 最终整合 → Step 5 收敛\\n\\n## GPU 预算\\n- **分配**: 2× GPU (westd-19828, cuda:0/cuda:1)\\n- **cuda:0**: gpt2m_a025_s42 运行中\\n- **cuda:1**: a025_s44 运行中\\n- **D044 后剩余 GPU 需求**: 仅 gpt2m_a025 (~3h)，其余全部零 GPU\\n\\n## 硬约束提醒\\n- GPU 白名单: 仅 cuda:0, cuda:1 (westd-19828)\\n- Claim 措辞: 不可用 \\\"architecture-agnostic\\\" 或 \\\"scale-independent\\\"\\n- α=0.75 vs α=1.0 consensus 数字禁止直接对比（D038 #27）\\n- FNR=0 声明必须附 D017 独立证据（D041）\\n- batch_size=32 vs 4 差异已在 discussion.tex 注明\\n- T notation: T = generation cycles, 数据点 = T+1\\n\\n## 关键决策日志\\n\\n| ID | 日期 | 摘要 | 关联实验 |\\n|----|------|------|----------|\\n| D047 | 2026-05-16 | 修正 Table 1 α=1.0 聚合值计算错误 + 纳入 GPT-2m 跨架构结果到 discus | mvp_v4_rep42, mvp_v4_rep43, mvp_v4_rep44, mvp_v4_rep45, gen_wiki_gpt2m_a100_s42_v3 |\\n| D046 | 2026-05-16 | D046: 指定 docs/paper/ 为论文唯一真源，artifacts/_project/pa | — |\\n| D045 | 2026-05-16 | D045: TY seed 审计确认 paper FNR=33.3% 和 ECE→d1 sig_se | method_ablation_phase1, gen_wiki_gpt2m_a100_s42_v3 |\\n| D044 | 2026-05-15 | D044: 砍低 ROI 实验（a050_s44/a010_s42/plan_006_s43），转投 | gen_wiki_gpt2m_a100_s42_v3, alpha_sweep_a025_s43, alpha_sweep_a050_s43 |\\n| D043 | 2026-05-15 | D043: 投稿目标确定为 EMNLP 2026 main track（用户指定），替代之前暂定的  | — |\\n| D042 | 2026-05-15 | D042: 论文主线升级为 diagnostic + prescriptive——\\\"empirica | consensus_framework, D017 |\\n| D041 | 2026-05-15 | D041: FPR/FNR 校准表论文呈现约束——反循环论证 + 维度不对称声明 | consensus_framework, D017 |\\n| D040 | 2026-05-15 | D040: 论文结构终版确定——5图重组 + Sequential Filtering Pipeli | plan_006_s42, consensus_framework |\\n| D039 | 2026-05-15 | D039: 论文结构框架初步确定——5 图方案 + 章节组织，待 Reviewer 深度讨论后可能调 | plan_006_s42, alpha_sweep_a075_s42 |\\n| D038 | 2026-05-15 | 新增约束：α=0.75 vs α=1.0 consensus 数字不可直接对比（标准不同）；entr | alpha_sweep_a075_s42, D017 |\\n\\n\", \"lines\": 79}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "083420db-5d99-4ea3-b894-3f9c3c7d9709",
  "isSidechain": false,
  "promptId": "a304cee9-feed-4fb2-a028-8ae1d93109aa",
  "type": "user",
  "uuid": "fd022112-a7ac-43df-89ba-3cb9fe8777ca",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/ROADMAP.md\\\", \\\"content\\\": \\\"# distrib_canary_collapse — Research Dashboard\\\\n\\\\n> 最后更新: 2026-05-15 23:54 UTC | 更新原因: 标记零 GPU 分析 A/B/C + T-notation patch 完成，更新收敛路线剩余任务\\\\n\\\\n## 核心方向\\\\n**D027 reframe**: 以方法论陷阱 + 多方法共识框架为主线，canary prediction 为系统性 case study。暴露 lead-lag 分析中的方法选择敏感性（Claim 3 领衔）、伪回归陷阱（Claim 1 case study）、regime-dependent validity（Claim 2）。详见 paper_framing.md。\\\\n\\\\n**Title direction**: \\\\\\\"Method Matters: Pitfalls and a Multi-Method Consensus Framework for Lead-Lag Analysis in Iterative Training Collapse\\\\\\\"\\\\n\\\\n## 当前进展\\\\n- **阶段**: Research 收敛期 + 审稿进行中 + Paper Agent Step 5 运行中\\\\n- **Target**: **EMNLP 2026 main track**（D043）\\\\n- **证据强度**: Claim 3 (方法敏感性跨架构复现, Tier 3, 4/5 唯一最优, κ 跨架构一致) > Claim 2 (regime map, 待 gpt2m_a025 跨架构确认) > Claim 1 (case study, 跨架构复现)\\\\n- **跨架构验证**: ✅ GPT-2m 5-method Tier 3 confirmatory\\\\n- **Claim 措辞上限**: \\\\\\\"consistent across two transformer decoder-only model families of similar scale\\\\\\\"\\\\n- **零 GPU 分析**: ✅ 全部完成（window sensitivity + method subset ablation + κ），已写入论文，T-notation 已修正\\\\n- **D044 收敛决策**: 砍低 ROI 实验，转投零 GPU 分析（已完成）\\\\n- **累计 GPU**: ~23h\\\\n\\\\n## 正在运行\\\\n| 实验 | GPU | 角色 | 备注 |\\\\n|------|-----|------|------|\\\\n| gpt2m_a025_s42 | cuda:0 | Claim 2 cross-arch | α=0.25, ~3h remaining |\\\\n| a025_s44 | cuda:1 | D026 multi-seed #3 | 完成即止，不再追加 |\\\\n\\\\n## 近期任务（收敛路线）\\\\n- [x] **零 GPU 分析 A**: Observation window sensitivity — 4/5 从 T≥5(paper) 即锁定\\\\n- [x] **零 GPU 分析 B**: Method subset ablation — 4/5 唯一最优，PermG linchpin\\\\n- [x] **零 GPU 分析 C**: GPT-2m κ=0.091 — 低 κ 跨架构一致\\\\n- [x] **T-notation patch**: discussion.tex L30-31 修正完成\\\\n- [ ] **gpt2m_a025 完成** → 分析 regime-dependent 跨架构复现 → 写入论文\\\\n- [ ] **Paper Agent**: W1-W4 修复 + GPT-2m α=0.25 结果整合\\\\n- [ ] **Claim 强度 + 叙事调整讨论** → 与 Reviewer 深入评估\\\\n- [ ] **Step 5 收敛** → 最终 proofread + compile → submit_paper_to_review\\\\n\\\\n## 已砍任务（D044）\\\\n- ~~a050_s44~~ — 2 seed 已足够（<7% deviation）\\\\n- ~~alpha_sweep_a010_s42~~ — null regime 无新信息\\\\n- ~~plan_006_s43~~ — D035 已排除\\\\n\\\\n## WA → Accept 路径\\\\n1. ✅ 共识框架 formalization\\\\n2. ✅ FDR 修复全链路\\\\n3. ✅ 论文结构终版 + prescriptive 升级\\\\n4. ✅ GPT-2m 5-method Tier 3 cross-arch validation\\\\n5. ✅ 零 GPU 分析 A+B+C（window sensitivity + method ablation + κ）\\\\n6. 🔄 gpt2m_a025_s42 → regime map 跨架构确认\\\\n7. Paper Agent W1-W4 + 最终整合 → Step 5 收敛\\\\n\\\\n## GPU 预算\\\\n- **分配**: 2× GPU (westd-19828, cuda:0/cuda:1)\\\\n- **cuda:0**: gpt2m_a025_s42 运行中\\\\n- **cuda:1**: a025_s44 运行中\\\\n- **D044 后剩余 GPU 需求**: 仅 gpt2m_a025 (~3h)，其余全部零 GPU\\\\n\\\\n## 硬约束提醒\\\\n- GPU 白名单: 仅 cuda:0, cuda:1 (westd-19828)\\\\n- Claim 措辞: 不可用 \\\\\\\"architecture-agnostic\\\\\\\" 或 \\\\\\\"scale-independent\\\\\\\"\\\\n- α=0.75 vs α=1.0 consensus 数字禁止直接对比（D038 #27）\\\\n- FNR=0 声明必须附 D017 独立证据（D041）\\\\n- batch_size=32 vs 4 差异已在 discussion.tex 注明\\\\n- T notation: T = generation cycles, 数据点 = T+1\\\\n\\\\n## 关键决策日志\\\\n\\\\n| ID | 日期 | 摘要 | 关联实验 |\\\\n|----|------|------|----------|\\\\n| D047 | 2026-05-16 | 修正 Table 1 α=1.0 聚合值计算错误 + 纳入 GPT-2m 跨架构结果到 discus | mvp_v4_rep42, mvp_v4_rep43, mvp_v4_rep44, mvp_v4_rep45, gen_wiki_gpt2m_a100_s42_v3 |\\\\n| D046 | 2026-05-16 | D046: 指定 docs/paper/ 为论文唯一真源，artifacts/_project/pa | — |\\\\n| D045 | 2026-05-16 | D045: TY seed 审计确认 paper FNR=33.3% 和 ECE→d1 sig_se | method_ablation_phase1, gen_wiki_gpt2m_a100_s42_v3 |\\\\n| D044 | 2026-05-15 | D044: 砍低 ROI 实验（a050_s44/a010_s42/plan_006_s43），转投 | gen_wiki_gpt2m_a100_s42_v3, alpha_sweep_a025_s43, alpha_sweep_a050_s43 |\\\\n| D043 | 2026-05-15 | D043: 投稿目标确定为 EMNLP 2026 main track（用户指定），替代之前暂定的  | — |\\\\n| D042 | 2026-05-15 | D042: 论文主线升级为 diagnostic + prescriptive——\\\\\\\"empirica | consensus_framework, D017 |\\\\n| D041 | 2026-05-15 | D041: FPR/FNR 校准表论文呈现约束——反循环论证 + 维度不对称声明 | consensus_framework, D017 |\\\\n| D040 | 2026-05-15 | D040: 论文结构终版确定——5图重组 + Sequential Filtering Pipeli | plan_006_s42, consensus_framework |\\\\n| D039 | 2026-05-15 | D039: 论文结构框架初步确定——5 图方案 + 章节组织，待 Reviewer 深度讨论后可能调 | plan_006_s42, alpha_sweep_a075_s42 |\\\\n| D038 | 2026-05-15 | 新增约束：α=0.75 vs α=1.0 consensus 数字不可直接对比（标准不同）；entr | alpha_sweep_a075_s42, D017 |\\\\n\\\\n\\\", \\\"lines\\\": 79}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/ROADMAP.md\", \"content\": \"# distrib_canary_collapse — Research Dashboard\\n\\n> 最后更新: 2026-05-15 23:54 UTC | 更新原因: 标记零 GPU 分析 A/B/C + T-notation patch 完成，更新收敛路线剩余任务\\n\\n## 核心方向\\n**D027 reframe**: 以方法论陷阱 + 多方法共识框架为主线，canary prediction 为系统性 case study。暴露 lead-lag 分析中的方法选择敏感性（Claim 3 领衔）、伪回归陷阱（Claim 1 case study）、regime-dependent validity（Claim 2）。详见 paper_framing.md。\\n\\n**Title direction**: \\\"Method Matters: Pitfalls and a Multi-Method Consensus Framework for Lead-Lag Analysis in Iterative Training Collapse\\\"\\n\\n## 当前进展\\n- **阶段**: Research 收敛期 + 审稿进行中 + Paper Agent Step 5 运行中\\n- **Target**: **EMNLP 2026 main track**（D043）\\n- **证据强度**: Claim 3 (方法敏感性跨架构复现, Tier 3, 4/5 唯一最优, κ 跨架构一致) > Claim 2 (regime map, 待 gpt2m_a025 跨架构确认) > Claim 1 (case study, 跨架构复现)\\n- **跨架构验证**: ✅ GPT-2m 5-method Tier 3 confirmatory\\n- **Claim 措辞上限**: \\\"consistent across two transformer decoder-only model families of similar scale\\\"\\n- **零 GPU 分析**: ✅ 全部完成（window sensitivity + method subset ablation + κ），已写入论文，T-notation 已修正\\n- **D044 收敛决策**: 砍低 ROI 实验，转投零 GPU 分析（已完成）\\n- **累计 GPU**: ~23h\\n\\n## 正在运行\\n| 实验 | GPU | 角色 | 备注 |\\n|------|-----|------|------|\\n| gpt2m_a025_s42 | cuda:0 | Claim 2 cross-arch | α=0.25, ~3h remaining |\\n| a025_s44 | cuda:1 | D026 multi-seed #3 | 完成即止，不再追加 |\\n\\n## 近期任务（收敛路线）\\n- [x] **零 GPU 分析 A**: Observation window sensitivity — 4/5 从 T≥5(paper) 即锁定\\n- [x] **零 GPU 分析 B**: Method subset ablation — 4/5 唯一最优，PermG linchpin\\n- [x] **零 GPU 分析 C**: GPT-2m κ=0.091 — 低 κ 跨架构一致\\n- [x] **T-notation patch**: discussion.tex L30-31 修正完成\\n- [ ] **gpt2m_a025 完成** → 分析 regime-dependent 跨架构复现 → 写入论文\\n- [ ] **Paper Agent**: W1-W4 修复 + GPT-2m α=0.25 结果整合\\n- [ ] **Claim 强度 + 叙事调整讨论** → 与 Reviewer 深入评估\\n- [ ] **Step 5 收敛** → 最终 proofread + compile → submit_paper_to_review\\n\\n## 已砍任务（D044）\\n- ~~a050_s44~~ — 2 seed 已足够（<7% deviation）\\n- ~~alpha_sweep_a010_s42~~ — null regime 无新信息\\n- ~~plan_006_s43~~ — D035 已排除\\n\\n## WA → Accept 路径\\n1. ✅ 共识框架 formalization\\n2. ✅ FDR 修复全链路\\n3. ✅ 论文结构终版 + prescriptive 升级\\n4. ✅ GPT-2m 5-method Tier 3 cross-arch validation\\n5. ✅ 零 GPU 分析 A+B+C（window sensitivity + method ablation + κ）\\n6. 🔄 gpt2m_a025_s42 → regime map 跨架构确认\\n7. Paper Agent W1-W4 + 最终整合 → Step 5 收敛\\n\\n## GPU 预算\\n- **分配**: 2× GPU (westd-19828, cuda:0/cuda:1)\\n- **cuda:0**: gpt2m_a025_s42 运行中\\n- **cuda:1**: a025_s44 运行中\\n- **D044 后剩余 GPU 需求**: 仅 gpt2m_a025 (~3h)，其余全部零 GPU\\n\\n## 硬约束提醒\\n- GPU 白名单: 仅 cuda:0, cuda:1 (westd-19828)\\n- Claim 措辞: 不可用 \\\"architecture-agnostic\\\" 或 \\\"scale-independent\\\"\\n- α=0.75 vs α=1.0 consensus 数字禁止直接对比（D038 #27）\\n- FNR=0 声明必须附 D017 独立证据（D041）\\n- batch_size=32 vs 4 差异已在 discussion.tex 注明\\n- T notation: T = generation cycles, 数据点 = T+1\\n\\n## 关键决策日志\\n\\n| ID | 日期 | 摘要 | 关联实验 |\\n|----|------|------|----------|\\n| D047 | 2026-05-16 | 修正 Table 1 α=1.0 聚合值计算错误 + 纳入 GPT-2m 跨架构结果到 discus | mvp_v4_rep42, mvp_v4_rep43, mvp_v4_rep44, mvp_v4_rep45, gen_wiki_gpt2m_a100_s42_v3 |\\n| D046 | 2026-05-16 | D046: 指定 docs/paper/ 为论文唯一真源，artifacts/_project/pa | — |\\n| D045 | 2026-05-16 | D045: TY seed 审计确认 paper FNR=33.3% 和 ECE→d1 sig_se | method_ablation_phase1, gen_wiki_gpt2m_a100_s42_v3 |\\n| D044 | 2026-05-15 | D044: 砍低 ROI 实验（a050_s44/a010_s42/plan_006_s43），转投 | gen_wiki_gpt2m_a100_s42_v3, alpha_sweep_a025_s43, alpha_sweep_a050_s43 |\\n| D043 | 2026-05-15 | D043: 投稿目标确定为 EMNLP 2026 main track（用户指定），替代之前暂定的  | — |\\n| D042 | 2026-05-15 | D042: 论文主线升级为 diagnostic + prescriptive——\\\"empirica | consensus_framework, D017 |\\n| D041 | 2026-05-15 | D041: FPR/FNR 校准表论文呈现约束——反循环论证 + 维度不对称声明 | consensus_framework, D017 |\\n| D040 | 2026-05-15 | D040: 论文结构终版确定——5图重组 + Sequential Filtering Pipeli | plan_006_s42, consensus_framework |\\n| D039 | 2026-05-15 | D039: 论文结构框架初步确定——5 图方案 + 章节组织，待 Reviewer 深度讨论后可能调 | plan_006_s42, alpha_sweep_a075_s42 |\\n| D038 | 2026-05-15 | 新增约束：α=0.75 vs α=1.0 consensus 数字不可直接对比（标准不同）；entr | alpha_sweep_a075_s42, D017 |\\n\\n\", \"lines\": 79}, \"error\": null, \"metadata\": {}}"
    }
  },
  "sourceToolAssistantUUID": "083420db-5d99-4ea3-b894-3f9c3c7d9709",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/agent_e1f64cd5",
  "sessionId": "4f6074eb-8665-49ec-9526-07c9eebcea03",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 23 · 2026-05-16T02:25:00.961Z_

<details><summary>Logged reasoning block</summary>

```text
Let me analyze the state:

1. **alpha_sweep_a025_s44** is in ANALYZING status - this is the experiment I need to process
2. **gen_wiki_gpt2m_a025_s42** is still RUNNING on cuda:0
3. The experiment ran on westd-19828, cuda:1, with seed 44, α=0.25, 10 generations, 5000 steps/gen

Now I need to read the full registry entry for alpha_sweep_a025_s44 to understand what data is available, and then spawn a Worker to analyze the results (read logs, check W&B data, etc.).


I'm pulling the complete registry data to see the full command parameters and log paths that were recorded during the experiment.

Looking at the roadmap context, this is the third seed in the multi-seed alpha sweep at α=0.25, and it's marked as complete with no further additions needed. I need to SSH into the server to retrieve the training log, check the Weights & Biases data, and analyze whether the iterative training exhibits distributional collapse patterns—specifically looking at metrics like the distinct token drift percentages. I should also review what the previous seeds showed to understand the pattern across the sweep.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fd022112-a7ac-43df-89ba-3cb9fe8777ca",
  "isSidechain": false,
  "requestId": "req_011Cb5THuhGWHzBF774MUCUm",
  "type": "assistant",
  "uuid": "7b7f5da8-f997-425d-b387-13f86b1434a1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/agent_e1f64cd5",
  "sessionId": "4f6074eb-8665-49ec-9526-07c9eebcea03",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01T8BDf1uGF2GNThXn3cBhEv",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5358,
      "cache_read_input_tokens": 38030,
      "output_tokens": 849,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5358,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 849,
          "cache_read_input_tokens": 38030,
          "cache_creation_input_tokens": 5358,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5358
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

_source line 24 · 2026-05-16T02:25:00.963Z_

需要读取完整的 registry 数据来了解实验细节。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7b7f5da8-f997-425d-b387-13f86b1434a1",
  "isSidechain": false,
  "requestId": "req_011Cb5THuhGWHzBF774MUCUm",
  "type": "assistant",
  "uuid": "e2b5dd90-5b5a-4287-b7d1-158d6dc572db",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/agent_e1f64cd5",
  "sessionId": "4f6074eb-8665-49ec-9526-07c9eebcea03",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01T8BDf1uGF2GNThXn3cBhEv",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5358,
      "cache_read_input_tokens": 38030,
      "output_tokens": 849,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5358,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 849,
          "cache_read_input_tokens": 38030,
          "cache_creation_input_tokens": 5358,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5358
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

_source line 25 · 2026-05-16T02:25:05.820Z_

<details open><summary>🔧 Tool call — Read · `toolu_01QhdNETNeCSTmHv2Gaq1KPU`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-4-projects-distrib-canary-collapse--claude-sessions-agent-e1f64cd5/4f6074eb-8665-49ec-9526-07c9eebcea03/tool-results/toolu_01BxadqtFPAy7HcgcjyPHhCs.txt",
  "offset": 0,
  "limit": 200
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e2b5dd90-5b5a-4287-b7d1-158d6dc572db",
  "isSidechain": false,
  "requestId": "req_011Cb5THuhGWHzBF774MUCUm",
  "type": "assistant",
  "uuid": "82ac2b1a-122b-407f-97da-ea46c6a7db4d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/agent_e1f64cd5",
  "sessionId": "4f6074eb-8665-49ec-9526-07c9eebcea03",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01T8BDf1uGF2GNThXn3cBhEv",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5358,
      "cache_read_input_tokens": 38030,
      "output_tokens": 849,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5358,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 849,
          "cache_read_input_tokens": 38030,
          "cache_creation_input_tokens": 5358,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5358
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

_source line 26 · 2026-05-16T02:25:06.119Z_

<details><summary>↩ Tool result · `toolu_01QhdNETNeCSTmHv2Gaq1KPU`</summary>

```text
0	{"result":"{\"success\": true, \"data\": {\"experiments\": {\"alpha_sweep_a025_s44\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-15T06:58:48.224Z\", \"updated_at\": \"2026-05-16T02:24:25.189Z\", \"spec\": {\"command\": \"bash -c \\\"cd /root/autodl-tmp/distrib_canary_collapse && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_HUB_DISABLE_XET=1 && export HF_ENDPOINT=https://hf-mirror.com && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && PYTHONUNBUFFERED=1 python -u iterative_train.py --seed 44 --data_dir data/wikitext103_5k --steps_per_gen 5000 --num_generations 10 --synthetic_ratio 0.25 --output_dir results/alpha_sweep/a025_s44\\\"\", \"server\": \"westd-19828\", \"gpu\": [\"cuda:1\"], \"pid\": \"147811\", \"log_path\": \"~/runs/distrib_canary_collapse/alpha_sweep_a025_s44.log\", \"submitted_at\": \"2026-05-15T22:04:28.318Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"server\": \"westd-19828\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-19828\", \"gpu\": \"cuda:1\", \"started_at\": \"2026-05-15T22:04:26.677Z\", \"command\": \"bash -c \\\"cd /root/autodl-tmp/distrib_canary_collapse && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_HUB_DISABLE_XET=1 && export HF_ENDPOINT=https://hf-mirror.com && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && PYTHONUNBUFFERED=1 python -u iterative_train.py --seed 44 --data_dir data/wikitext103_5k --steps_per_gen 5000 --num_generations 10 --synthetic_ratio 0.25 --output_dir results/alpha_sweep/a025_s44\\\"\", \"finished_at\": \"2026-05-16T02:24:25.056Z\", \"training_hours\": 4.33}, \"pid\": \"147811\", \"log_path\": \"~/runs/distrib_canary_collapse/alpha_sweep_a025_s44.log\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T02:24:26.614491+00:00\"}]}}, \"mvp_v2_rep44\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T05:38:10.762Z\", \"updated_at\": \"2026-05-16T00:10:26.251Z\", \"spec\": {\"hypothesis\": \"至少一族canary指标在100% SC full replacement下对downstream指标有≥1 gen的时序领先性\", \"model_name\": \"EleutherAI/pythia-410m\", \"data_path\": \"/root/autodl-tmp/distrib_canary_collapse/data/wikitext103\", \"data_count\": 5000, \"seed\": 44, \"server\": \"autodl-rtx6000\", \"gpu\": \"pending\", \"synthetic_ratio\": 1, \"num_generations\": 10, \"steps_per_gen\": 5000, \"n_prompts\": 5000, \"fix_note\": \"n_prompts 1000→5000, steps_per_gen 10000→5000, 避免过拟合\"}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-16T00:10:26.251Z\"}, \"mvp_rep44\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T05:12:15.033Z\", \"updated_at\": \"2026-05-16T00:10:25.605Z\", \"spec\": {\"hypothesis\": \"至少一族canary指标在100% SC full replacement下对downstream指标有≥1 gen的时序领先性\", \"model_name\": \"EleutherAI/pythia-410m\", \"data_path\": \"/root/autodl-tmp/distrib_canary_collapse/data/wikitext103\", \"seed\": 44, \"server\": \"autodl-rtx6000\", \"gpu\": \"pending\", \"synthetic_ratio\": 1, \"num_generations\": 10, \"steps_per_gen\": 10000}, \"metrics\": {\"gen10_token_entropy\": 1.2205, \"gen10_ece\": 0.4237, \"gen10_perplexity\": 1033.16, \"gen10_distinct_1\": 0.0731, \"gen10_distinct_2\": 0.3637, \"gen10_distinct_3\": 0.6075}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-16T00:10:25.605Z\"}, \"alpha_sweep_a025_s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T19:01:39.527Z\", \"updated_at\": \"2026-05-16T00:10:24.973Z\", \"spec\": {\"hypothesis\": \"α=0.25 低污染: 测试 canary→diversity lead 在温和 collapse 下是否保持，canary→perplexity lead 是否出现\", \"model_name\": \"EleutherAI/pythia-410m\", \"data_path\": \"/root/autodl-tmp/distrib_canary_collapse/data/wikitext103_5k\", \"data_count\": 5000, \"seed\": 42, \"synthetic_ratio\": 0.25, \"num_generations\": 10, \"steps_per_gen\": 5000}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-16T00:10:24.973Z\"}, \"alpha_sweep_a025_s42_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T19:25:52.094Z\", \"updated_at\": \"2026-05-16T00:10:24.568Z\", \"spec\": {\"hypothesis\": \"α=0.25 低污染: 测试 canary→diversity lead 在温和 collapse 下是否保持，canary→perplexity lead 是否出现\", \"model_name\": \"EleutherAI/pythia-410m\", \"data_path\": \"/root/autodl-tmp/distrib_canary_collapse/data/wikitext103_5k\", \"data_count\": 5000, \"seed\": 42, \"synthetic_ratio\": 0.25, \"num_generations\": 10, \"steps_per_gen\": 5000, \"parent\": \"alpha_sweep_a025_s42 (killed, subsample bias fix)\"}, \"conclusion\": \"killed\", \"failure_reason\": \"data corruption: unkilled old process PID 46802 wrote concurrently with new PID 48454\", \"completed_at\": \"2026-05-16T00:10:24.568Z\"}, \"alpha_sweep_a060_s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T21:52:22.516Z\", \"updated_at\": \"2026-05-16T00:04:01.429Z\", \"spec\": {\"hypothesis\": \"α=0.60 中高污染: phase boundary 精确化, 与 α=0.50/0.75 对比 lead time 变化\", \"model_name\": \"EleutherAI/pythia-410m\", \"data_path\": \"/root/autodl-tmp/distrib_canary_collapse/data/wikitext103_5k\", \"data_count\": 5000, \"seed\": 42, \"synthetic_ratio\": 0.6, \"num_generations\": 10, \"steps_per_gen\": 5000}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-16T00:04:01.429Z\"}, \"alpha_sweep_a010_s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T21:52:19.712Z\", \"updated_at\": \"2026-05-16T00:03:53.018Z\", \"spec\": {\"hypothesis\": \"α=0.10 极低污染: phase boundary 精确化, canary signal 是否仍可检测\", \"model_name\": \"EleutherAI/pythia-410m\", \"data_path\": \"/root/autodl-tmp/distrib_canary_collapse/data/wikitext103_5k\", \"data_count\": 5000, \"seed\": 42, \"synthetic_ratio\": 0.1, \"num_generations\": 10, \"steps_per_gen\": 5000}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-16T00:03:53.018Z\"}, \"alpha_sweep_a050_s44\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T06:58:50.550Z\", \"updated_at\": \"2026-05-16T00:03:52.118Z\", \"spec\": {\"hypothesis\": \"α=0.50 multi-seed replication (seed=44): 第三个 seed 为置信区间提供统计力\", \"model_name\": \"EleutherAI/pythia-410m\", \"data_path\": \"/root/autodl-tmp/distrib_canary_collapse/data/wikitext103_5k\", \"data_count\": 5000, \"seed\": 44, \"synthetic_ratio\": 0.5, \"num_generations\": 10, \"steps_per_gen\": 5000, \"parent\": \"alpha_sweep_a050_s42\", \"priority\": \"D026-4\"}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-16T00:03:52.118Z\"}, \"plan_006_s43\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T23:31:37.257Z\", \"updated_at\": \"2026-05-16T00:03:51.617Z\", \"spec\": {\"plan_id\": \"plan_006\", \"hypothesis\": \"Multi-seed replication of three-phase collapse dynamics: verify Phase 3 secondary decline (gen 13+) reproduces with seed=43, confirming it is not a single-seed artifact\", \"model_name\": \"EleutherAI/pythia-410m\", \"seed\": 43, \"data_path\": \"data/wikitext103_5k\", \"num_generations\": 18, \"synthetic_ratio\": 1, \"max_lag\": 10, \"data_count\": 5000, \"steps_per_gen\": 5000, \"parent\": \"plan_006_s42\", \"claim\": 1, \"priority\": \"P0\"}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-16T00:03:51.617Z\"}, \"gen_wiki_gpt2m_a100_s42_v3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T12:07:20.050Z\", \"updated_at\": \"2026-05-15T22:30:21.573Z\", \"spec\": {\"hypothesis\": \"Method sensitivity patterns (Granger FDR collapse, cross-correlation dominance) generalize from GPT-2-small to GPT-2-medium, validating cross-architecture universality of methodological pitfalls\", \"seed\": 42, \"model_name\": \"gpt2-medium\", \"data_path\": \"data/wikitext103_5k\", \"data_count\": 5000}, \"server\": \"westd-19828\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-19828\", \"gpu\": \"cuda:0\", \"started_at\": \"2026-05-15T12:07:30.366Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && mkdir -p results/gen_wiki_gpt2m_a100_s42 && HF_HOME=/root/autodl-tmp/.hf_cache TRANSFORMERS_OFFLINE=1 HF_HUB_DISABLE_XET=1 PYTHONUNBUFFERED=1 python -u iterative_train.py --model_name gpt2-medium --data_dir data/wikitext103_5k --synthetic_ratio 1.0 --num_generations 10 --steps_per_gen 5000 --batch_size 32 --seed 42 --output_dir results/gen_wiki_gpt2m_a100_s42\\\"\", \"finished_at\": \"2026-05-15T22:14:43.852Z\", \"training_hours\": 10.12}, \"pid\": \"117632\", \"log_path\": \"~/runs/distrib_canary_collapse/gen_wiki_gpt2m_a100_s42_v3.log\", \"metrics\": {\"token_entropy_drift_pct\": -86.5, \"ece_drift_pct\": 4543, \"perplexity_drift_pct\": 44703, \"distinct_1_drift_pct\": -12.4, \"distinct_2_drift_pct\": -14.7, \"distinct_3_drift_pct\": -12.7, \"five_method_forward_consensus\": \"6/6 pairs at 4/5 methods (Tier 3)\", \"five_method_reverse_consensus\": \"0/6 pairs\", \"naive_xcorr_forward\": \"|r|>0.98, all sig\", \"diff_xcorr_forward\": \"all p_fdr<0.001\", \"diff_xcorr_reverse\": \"all p>0.18 (clean directional separation)\", \"threshold_onset_entropy\": \"gen 1 (earliest canary)\", \"threshold_onset_ece\": \"gen 1-2\", \"threshold_onset_diversity\": \"gen 3\", \"perm_granger_forward\": \"p_fdr=0.003, BH corrected\", \"ty_granger_forward\": \"0/6 sig (df_resid=1-4, underpowered, consistent with Pythia C001)\", \"entropy_leads_diversity_lag\": \"1-2 gen\", \"ece_leads_diversity_lag\": \"1 gen\", \"diversity_plateau_from\": \"gen5\", \"cross_arch_note\": \"Replicates Pythia entropy-leads-diversity pattern at Tier 3 consensus. TY underpowered as expected.\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T22:14:45.029003+00:00\"}]}, \"conclusion\": \"success\", \"checkpoint_path\": \"results/gen_wiki_gpt2m_a100_s42/\", \"completed_at\": \"2026-05-15T22:18:22.762Z\"}, \"gen_wiki_gpt2m_a025_s42\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-15T10:35:16.032Z\", \"updated_at\": \"2026-05-15T22:22:52.921Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && mkdir -p results/gen_wiki_gpt2m_a025_s42 && HF_HOME=/root/autodl-tmp/.hf_cache TRANSFORMERS_OFFLINE=1 HF_HUB_DISABLE_XET=1 PYTHONUNBUFFERED=1 python -u iterative_train.py --model_name gpt2-medium --data_dir data/wikitext103_5k --synthetic_ratio 0.25 --num_generations 10 --steps_per_gen 5000 --batch_size 32 --seed 42 --output_dir results/gen_wiki_gpt2m_a025_s42\\\"\", \"server\": \"westd-19828\", \"gpu\": [\"cuda:0\"], \"pid\": \"149202\", \"log_path\": \"~/runs/distrib_canary_collapse/gen_wiki_gpt2m_a025_s42.log\", \"submitted_at\": \"2026-05-15T22:22:52.615Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"server\": \"westd-19828\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-19828\", \"gpu\": \"cuda:0\", \"started_at\": \"2026-05-15T22:22:51.021Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && mkdir -p results/gen_wiki_gpt2m_a025_s42 && HF_HOME=/root/autodl-tmp/.hf_cache TRANSFORMERS_OFFLINE=1 HF_HUB_DISABLE_XET=1 PYTHONUNBUFFERED=1 python -u iterative_train.py --model_name gpt2-medium --data_dir data/wikitext103_5k --synthetic_ratio 0.25 --num_generations 10 --steps_per_gen 5000 --batch_size 32 --seed 42 --output_dir results/gen_wiki_gpt2m_a025_s42\\\"\"}, \"pid\": \"149202\", \"log_path\": \"~/runs/distrib_canary_collapse/gen_wiki_gpt2m_a025_s42.log\"}, \"alpha_sweep_a050_s43\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T06:58:45.880Z\", \"updated_at\": \"2026-05-15T22:15:50.290Z\", \"spec\": {\"command\": \"bash -c \\\"cd /root/autodl-tmp/distrib_canary_collapse && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_HUB_DISABLE_XET=1 && export HF_ENDPOINT=https://hf-mirror.com && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && PYTHONUNBUFFERED=1 python -u iterative_train.py --seed 43 --data_dir data/wikitext103_5k --steps_per_gen 5000 --num_generations 10 --synthetic_ratio 0.50 --output_dir results/alpha_sweep/a050_s43\\\"\", \"server\": \"westd-19828\", \"gpu\": [\"cuda:1\"], \"pid\": \"134860\", \"log_path\": \"~/runs/distrib_canary_collapse/alpha_sweep_a050_s43.log\", \"submitted_at\": \"2026-05-15T17:40:27.060Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 16523.2, \"gpu_hours\": 4.59}, \"server\": \"westd-19828\", \"gpu\": \"cuda:1\", \"pid\": \"134860\", \"log_path\": \"~/runs/distrib_canary_collapse/alpha_sweep_a050_s43.log\", \"reproduce\": {\"command\": \"bash -c \\\"cd /root/autodl-tmp/distrib_canary_collapse && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_HUB_DISABLE_XET=1 && export HF_ENDPOINT=https://hf-mirror.com && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && PYTHONUNBUFFERED=1 python -u iterative_train.py --seed 43 --data_dir data/wikitext103_5k --steps_per_gen 5000 --num_generations 10 --synthetic_ratio 0.50 --output_dir results/alpha_sweep/a050_s43\\\"\", \"finished_at\": \"2026-05-15T22:00:14.725Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T22:00:15.908424+00:00\"}]}, \"conclusion\": \"success\", \"checkpoint_path\": \"results/alpha_sweep/a050_s43/gen_10/checkpoint/\", \"metrics\": {\"gen0_token_entropy\": 3.234195, \"gen0_ece\": 0.010805, \"gen0_perplexity\": 26.948959, \"gen10_token_entropy\": 2.672, \"gen10_ece\": 0.097, \"gen10_perplexity\": 32.633, \"gen0_distinct_1\": 0.09833, \"gen0_distinct_2\": 0.5132, \"gen0_distinct_3\": 0.8057, \"gen10_distinct_1\": 0.0624, \"gen10_distinct_2\": 0.2617, \"gen10_distinct_3\": 0.4126, \"token_entropy_drift_pct\": -17.4, \"ece_drift_pct\": 799, \"perplexity_drift_pct\": 21.1, \"distinct_1_drift_pct\": -36.5, \"distinct_2_drift_pct\": -49, \"distinct_3_drift_pct\": -48.8, \"cross_seed_note\": \"vs s42: drift direction identical, magnitude <7% deviation, ppl near-identical (32.633 vs 32.64)\"}, \"completed_at\": \"2026-05-15T22:00:14Z\"}, \"mvp_v4_rep45\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T13:41:26.286Z\", \"updated_at\": \"2026-05-15T21:29:54.928Z\", \"spec\": {\"command\": \"bash -c \\\"cd /root/autodl-tmp/distrib_canary_collapse && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_HUB_DISABLE_XET=1 && export HF_ENDPOINT=https://hf-mirror.com && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && PYTHONUNBUFFERED=1 python -u iterative_train.py --seed 45 --data_dir data/wikitext103_5k --steps_per_gen 5000 --num_generations 10 --output_dir results/mvp/rep_45\\\"\", \"server\": \"westd-19828\", \"gpu\": [\"cuda:1\"], \"pid\": \"31425\", \"log_path\": \"~/runs/distrib_canary_collapse/mvp_v4_rep45.log\", \"submitted_at\": \"2026-05-14T13:42:10.455Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/distrib_canary_collapse/data/wikitext103_5k\", \"data_count\": 5000, \"model_name\": \"EleutherAI/pythia-410m\", \"seed\": 45, \"wall_clock_seconds\": 15350.2, \"gpu_hours\": 4.26}, \"reproduce\": {\"finished_at\": \"2026-05-14T17:55:42.230Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T17:55:42.934182+00:00\"}]}, \"checkpoint_path\": \"/root/autodl-tmp/distrib_canary_collapse/results/mvp/rep_45/gen_10/checkpoint\", \"metrics_summary\": {\"gen0_ppl\": 26.9, \"gen10_ppl\": 1016.2, \"gen0_entropy\": 3.234, \"gen10_entropy\": 1.315, \"gen0_ece\": 0.011, \"gen10_ece\": 0.417}, \"wall_clock_seconds\": 15212, \"gpu_hours\": 4.23, \"conclusion\": \"success\", \"metrics\": {\"gen0_token_entropy\": 3.234195, \"gen0_ece\": 0.010805, \"gen0_perplexity\": 26.948959, \"gen0_distinct_1\": 0.098574, \"gen0_distinct_2\": 0.51463, \"gen0_distinct_3\": 0.808362, \"gen10_token_entropy\": 1.31536, \"gen10_ece\": 0.41654, \"gen10_perplexity\": 1016.22, \"gen10_distinct_1\": 0.069859, \"gen10_distinct_2\": 0.329549, \"gen10_distinct_3\": 0.543743, \"token_entropy_drift_pct\": -59.3296, \"ece_drift_pct\": 3755.0671, \"perplexity_drift_pct\": 3670.9063, \"distinct_1_drift_pct\": -29.1304, \"distinct_2_drift_pct\": -35.9639, \"distinct_3_drift_pct\": -32.7352}, \"completed_at\": \"2026-05-14T17:58:00.661Z\"}, \"mvp_v4_rep44\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T07:48:52.613Z\", \"updated_at\": \"2026-05-15T21:29:52.398Z\", \"spec\": {\"hypothesis\": \"至少一族canary指标在100% SC full replacement下对downstream指标有≥1 gen的时序领先性\", \"model_name\": \"EleutherAI/pythia-410m\", \"data_path\": \"/root/autodl-tmp/distrib_canary_collapse/data/wikitext103_5k\", \"data_count\": 5000, \"seed\": 44, \"server\": \"westd-19828\", \"gpu\": \"cuda:0\", \"synthetic_ratio\": 1, \"num_generations\": 10, \"steps_per_gen\": 5000, \"n_prompts\": 5000, \"command\": \"PYTHONUNBUFFERED=1 CUDA_VISIBLE_DEVICES=0 python -u iterative_train.py --seed 44 --data_dir data/wikitext103_5k --steps_per_gen 5000 --num_generations 10 --output_dir results/mvp/rep_44\", \"pid\": \"30672\", \"log_path\": \"~/runs/distrib_canary_collapse/mvp_v4_rep44.log\"}, \"reproduce\": {\"finished_at\": \"2026-05-14T17:56:00.578Z\"}, \"failure_reason\": \"\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T17:56:00.717Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-14T17:56:03.546926+00:00\"}]}, \"metrics_summary\": {\"gen0_ppl\": 26.9, \"gen10_ppl\": 1033.16, \"gen0_entropy\": 3.234, \"gen10_entropy\": 1.2205, \"gen0_ece\": 0.011, \"gen10_ece\": 0.424}, \"checkpoint_path\": \"/root/autodl-tmp/distrib_canary_collapse/results/mvp/rep_44/gen_10/checkpoint\", \"wall_clock_seconds\": 15134, \"gpu_hours\": 4.2, \"metrics\": {\"gen0_token_entropy\": 3.234195, \"gen0_ece\": 0.010805, \"gen0_perplexity\": 26.948959, \"gen0_distinct_1\": 0.098088, \"gen0_distinct_2\": 0.513235, \"gen0_distinct_3\": 0.805767, \"gen10_token_entropy\": 1.22049, \"gen10_ece\": 0.42369, \"gen10_perplexity\": 1033.16, \"gen10_distinct_1\": 0.073102, \"gen10_distinct_2\": 0.363737, \"gen10_distinct_3\": 0.607502, \"token_entropy_drift_pct\": -62.2629, \"ece_drift_pct\": 3821.2402, \"perplexity_drift_pct\": 3733.7659, \"distinct_1_drift_pct\": -25.473, \"distinct_2_drift_pct\": -29.1286, \"distinct_3_drift_pct\": -24.6057}}, \"mvp_v4_rep43\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T07:48:50.161Z\", \"updated_at\": \"2026-05-15T21:29:49.565Z\", \"spec\": {\"command\": \"bash -c \\\"cd /root/autodl-tmp/distrib_canary_collapse && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_HUB_DISABLE_XET=1 && export HF_ENDPOINT=https://hf-mirror.com && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && PYTHONUNBUFFERED=1 python -u iterative_train.py --seed 43 --data_dir data/wikitext103_5k --steps_per_gen 5000 --num_generations 10 --output_dir results/mvp/rep_43\\\"\", \"server\": \"westd-19828\", \"gpu\": [\"cuda:1\"], \"pid\": \"13758\", \"log_path\": \"~/runs/distrib_canary_collapse/mvp_v4_rep43.log\", \"submitted_at\": \"2026-05-14T07:51:36.759Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"/root/autodl-tmp/distrib_canary_collapse/results/mvp/rep_43/gen_10/checkpoint\", \"metrics_summary\": {\"gen0_ppl\": 26.9, \"gen10_ppl\": 1014.7, \"gen0_entropy\": 3.234, \"gen10_entropy\": 1.26, \"gen0_ece\": 0.011, \"gen10_ece\": 0.42}, \"wall_clock_seconds\": 20897.7, \"gpu_hours\": 5.8}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T13:39:54.495Z\", \"metrics\": {\"gen0_token_entropy\": 3.234195, \"gen0_ece\": 0.010805, \"gen0_perplexity\": 26.948959, \"gen0_distinct_1\": 0.098334, \"gen0_distinct_2\": 0.513178, \"gen0_distinct_3\": 0.805669, \"gen10_token_entropy\": 1.25961, \"gen10_ece\": 0.41951, \"gen10_perplexity\": 1014.66, \"gen10_distinct_1\": 0.070383, \"gen10_distinct_2\": 0.329651, \"gen10_distinct_3\": 0.539571, \"token_entropy_drift_pct\": -61.0534, \"ece_drift_pct\": 3782.5544, \"perplexity_drift_pct\": 3665.1176, \"distinct_1_drift_pct\": -28.4246, \"distinct_2_drift_pct\": -35.7628, \"distinct_3_drift_pct\": -33.0282}}, \"mvp_v4_rep42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T07:29:48.857Z\", \"updated_at\": \"2026-05-15T21:29:47.171Z\", \"spec\": {\"command\": \"bash -c \\\"cd /root/autodl-tmp/distrib_canary_collapse && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_HUB_DISABLE_XET=1 && export HF_ENDPOINT=https://hf-mirror.com && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && PYTHONUNBUFFERED=1 python -u iterative_train.py --seed 42 --data_dir data/wikitext103_5k --steps_per_gen 5000 --num_generations 10 --output_dir results/mvp/rep_42\\\"\", \"server\": \"westd-19828\", \"gpu\": [\"cuda:0\"], \"pid\": \"13678\", \"log_path\": \"~/runs/distrib_canary_collapse/mvp_v4_rep42.log\", \"submitted_at\": \"2026-05-14T07:51:34.806Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"/root/autodl-tmp/distrib_canary_collapse/results/mvp/rep_42/gen_10/checkpoint\", \"metrics_summary\": {\"gen0_ppl\": 26.9, \"gen10_ppl\": 1003.7, \"gen0_entropy\": 3.234, \"gen10_entropy\": 1.276, \"gen0_ece\": 0.011, \"gen10_ece\": 0.417}, \"wall_clock_seconds\": 20898.3, \"gpu_hours\": 5.81}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T13:39:53.073Z\", \"metrics\": {\"gen0_token_entropy\": 3.234195, \"gen0_ece\": 0.010805, \"gen0_perplexity\": 26.948959, \"gen0_distinct_1\": 0.098216, \"gen0_distinct_2\": 0.517803, \"gen0_distinct_3\": 0.812728, \"gen10_token_entropy\": 1.27592, \"gen10_ece\": 0.41734, \"gen10_perplexity\": 1003.73, \"gen10_distinct_1\": 0.070383, \"gen10_distinct_2\": 0.335471, \"gen10_distinct_3\": 0.555579, \"token_entropy_drift_pct\": -60.5491, \"ece_drift_pct\": 3762.4711, \"perplexity_drift_pct\": 3624.5595, \"distinct_1_drift_pct\": -28.3386, \"distinct_2_drift_pct\": -35.2126, \"distinct_3_drift_pct\": -31.6402}}, \"alpha_sweep_a025_s43\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T06:58:43.090Z\", \"updated_at\": \"2026-05-15T17:39:43.623Z\", \"spec\": {\"command\": \"bash -c \\\"cd /root/autodl-tmp/distrib_canary_collapse && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_HUB_DISABLE_XET=1 && export HF_ENDPOINT=https://hf-mirror.com && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && PYTHONUNBUFFERED=1 python -u iterative_train.py --seed 43 --data_dir data/wikitext103_5k --steps_per_gen 5000 --num_generations 10 --synthetic_ratio 0.25 --output_dir results/alpha_sweep/a025_s43\\\"\", \"server\": \"westd-19828\", \"gpu\": [\"cuda:1\"], \"pid\": \"121635\", \"log_path\": \"~/runs/distrib_canary_collapse/alpha_sweep_a025_s43.log\", \"submitted_at\": \"2026-05-15T13:16:31.189Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 15792.4, \"gpu_hours\": 4.39}, \"server\": \"westd-19828\", \"gpu\": \"cuda:1\", \"pid\": \"121635\", \"log_path\": \"~/runs/distrib_canary_collapse/alpha_sweep_a025_s43.log\", \"reproduce\": {\"command\": \"bash -c \\\"cd /root/autodl-tmp/distrib_canary_collapse && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_HUB_DISABLE_XET=1 && export HF_ENDPOINT=https://hf-mirror.com && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && PYTHONUNBUFFERED=1 python -u iterative_train.py --seed 43 --data_dir data/wikitext103_5k --steps_per_gen 5000 --num_generations 10 --synthetic_ratio 0.25 --output_dir results/alpha_sweep/a025_s43\\\"\", \"finished_at\": \"2026-05-15T17:36:20.945Z\"}, \"metrics\": {\"gen0\": {\"token_entropy\": 3.2342, \"ece\": 0.0108, \"perplexity\": 26.949, \"distinct_1\": 0.09833, \"distinct_2\": 0.5132, \"distinct_3\": 0.8057, \"effective_rank\": 46.61, \"mauve\": 0.03351}, \"gen10\": {\"token_entropy\": 3.0723, \"ece\": 0.02146, \"perplexity\": 21.899, \"distinct_1\": 0.05849, \"distinct_2\": 0.2236, \"distinct_3\": 0.333, \"effective_rank\": 45.37, \"mauve\": 0.01871}, \"drift_pct\": {\"token_entropy\": -5, \"ece\": 98.6, \"perplexity\": -18.7, \"distinct_1\": -40.5, \"distinct_2\": -56.4, \"distinct_3\": -58.7, \"effective_rank\": -2.7, \"mauve\": -44.2}}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T17:36:22.072334+00:00\"}]}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a025_s43/gen_10/checkpoint\", \"completed_at\": \"2026-05-15T17:39:43.624Z\"}, \"alpha_sweep_a075_s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T21:52:17.315Z\", \"updated_at\": \"2026-05-15T13:29:46.421Z\", \"spec\": {\"hypothesis\": \"α=0.75 high contamination: critical boundary point for Granger-causal detectability — determines Claim 1 scope (α≥0.75 vs α=1.0 only)\", \"seed\": 42, \"model_name\": \"EleutherAI/pythia-410m\", \"data_path\": \"data/wikitext103_5k\", \"data_count\": 5000, \"synthetic_ratio\": 0.75, \"num_generations\": 10, \"steps_per_gen\": 5000}, \"server\": \"westd-19828\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-19828\", \"gpu\": \"cuda:1\", \"started_at\": \"2026-05-15T05:44:46.271Z\", \"command\": \"bash -c \\\"cd /root/autodl-tmp/distrib_canary_collapse && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_HUB_DISABLE_XET=1 && export HF_ENDPOINT=https://hf-mirror.com && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && PYTHONUNBUFFERED=1 python -u iterative_train.py --seed 42 --data_dir data/wikitext103_5k --steps_per_gen 5000 --num_generations 10 --synthetic_ratio 0.75 --output_dir results/alpha_sweep/a075_s42\\\"\", \"finished_at\": \"2026-05-15T13:13:06.477Z\", \"training_hours\": 7.47}, \"pid\": \"89753\", \"log_path\": \"results/analysis/cross_alpha_v6_report.md\", \"metrics\": {\"progress\": \"11/11 gen (complete)\", \"gen0_token_entropy\": 3.234, \"gen10_token_entropy\": 2.337, \"gen0_ece\": 0.0108, \"gen10_ece\": 0.2063, \"gen0_perplexity\": 26.95, \"gen10_perplexity\": 76.03, \"gen0_distinct_1\": 0.0982, \"gen10_distinct_1\": 0.0661, \"gen0_distinct_2\": 0.5178, \"gen10_distinct_2\": 0.3037, \"gen0_distinct_3\": 0.8127, \"gen10_distinct_3\": 0.5011, \"token_entropy_drift_pct\": -27.7, \"ece_drift_pct\": 1809.5, \"perplexity_drift_pct\": 182.1, \"distinct_1_drift_pct\": -32.7, \"distinct_2_drift_pct\": -41.3, \"distinct_3_drift_pct\": -38.4, \"granger_ece_to_d1_p_fdr\": 0.046, \"granger_ece_to_d2_p_fdr\": 0.046, \"granger_entropy_to_d2_p_fdr\": 0.048, \"granger_entropy_to_d1_p_fdr\": 0.054, \"granger_fdr_sig_count\": \"3/8\", \"consensus_robust_pairs\": \"11/16\", \"xcorr_entropy_d1_lag\": 2, \"xcorr_entropy_d1_r\": 0.973}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T13:13:07.582542+00:00\"}]}, \"conclusion\": \"success\", \"checkpoint_path\": \"results/alpha_sweep/a075_s42/\", \"completed_at\": \"2026-05-15T13:29:46.421Z\"}, \"alpha_sweep_a050_s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T21:52:15.427Z\", \"updated_at\": \"2026-05-15T13:17:48.134Z\", \"spec\": {\"hypothesis\": \"α=0.50 moderate contamination: test canary→diversity lead at mid-range synthetic ratio, key data point for non-monotonic dose-response\", \"seed\": 42, \"model_name\": \"EleutherAI/pythia-410m\", \"data_path\": \"data/wikitext103_5k\", \"data_count\": 5000, \"synthetic_ratio\": 0.5, \"num_generations\": 10, \"steps_per_gen\": 5000}, \"server\": \"westd-19828\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-19828\", \"gpu\": \"cuda:1\", \"started_at\": \"2026-05-15T01:15:14.747Z\", \"command\": \"bash -c \\\"cd /root/autodl-tmp/distrib_canary_collapse && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_HUB_DISABLE_XET=1 && export HF_ENDPOINT=https://hf-mirror.com && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && PYTHONUNBUFFERED=1 python -u iterative_train.py --seed 42 --data_dir data/wikitext103_5k --steps_per_gen 5000 --num_generations 10 --synthetic_ratio 0.50 --output_dir results/alpha_sweep/a050_s42\\\"\", \"finished_at\": \"2026-05-15T05:42:25.788Z\", \"training_hours\": 4.45}, \"pid\": \"73737\", \"log_path\": \"~/runs/distrib_canary_collapse/alpha_sweep_a050_s42.log\", \"metrics\": {\"progress\": \"11/11 gen (complete)\", \"gen0_token_entropy\": 3.234, \"gen10_token_entropy\": 2.632, \"gen0_ece\": 0.011, \"gen10_ece\": 0.102, \"gen0_perplexity\": 26.95, \"gen10_perplexity\": 32.64, \"gen0_distinct_1\": 0.098, \"gen10_distinct_1\": 0.062, \"gen0_distinct_2\": 0.518, \"gen10_distinct_2\": 0.251, \"gen0_distinct_3\": 0.813, \"gen10_distinct_3\": 0.387, \"token_entropy_drift_pct\": -18.6, \"ece_drift_pct\": 842.8, \"perplexity_drift_pct\": 21.1, \"distinct_1_drift_pct\": -37.3, \"distinct_2_drift_pct\": -51.5, \"distinct_3_drift_pct\": -52.4, \"granger_entropy_to_d1_p_raw\": 0.095, \"granger_entropy_to_d2_p_raw\": 0.097, \"granger_ece_to_d1_p_raw\": 0.019, \"granger_ece_to_d2_p_raw\": 0.039, \"granger_fdr_note\": \"4 tests within alpha=0.50; BH FDR threshold rank1=0.0125, rank2=0.025 → 0/4 FDR-sig at q=0.05. Raw p pattern (ECE < entropy) is qualitative signal only.\", \"d024_non_monotonic\": true, \"d024_ece_vs_entropy_note\": \"ECE raw p < entropy raw p at α=0.50 (0.019 vs 0.095 at 5000 perms), 0/4 FDR-sig; regime switch hypothesis pending α=0.75 confirmation\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T05:42:26.715028+00:00\"}]}, \"checkpoint_path\": \"/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a050_s42/gen_10/checkpoint\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T05:46:48.692Z\"}, \"plan_006_s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T23:31:35.454Z\", \"updated_at\": \"2026-05-15T12:17:14.093Z\", \"spec\": {\"command\": \"bash -c \\\"cd /root/autodl-tmp/distrib_canary_collapse && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_HUB_DISABLE_XET=1 && export HF_ENDPOINT=https://hf-mirror.com && PYTHONUNBUFFERED=1 python -u iterative_train.py --data_dir data/wikitext103 --output_dir results/extended_20gen/s42 --seed 42 --synthetic_ratio 1.0 --num_generations 20 --steps_per_gen 10000\\\"\", \"server\": \"westd-19828\", \"gpu\": [\"cuda:0\"], \"pid\": \"68368\", \"log_path\": \"~/runs/distrib_canary_collapse/plan_006_s42.log\", \"submitted_at\": \"2026-05-14T23:41:30.666Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 43212.6, \"gpu_hours\": 12.0}, \"server\": \"westd-19828\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-19828\", \"gpu\": \"cuda:0\", \"started_at\": \"2026-05-14T23:41:29.125Z\", \"command\": \"bash -c \\\"cd /root/autodl-tmp/distrib_canary_collapse && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_HUB_DISABLE_XET=1 && export HF_ENDPOINT=https://hf-mirror.com && PYTHONUNBUFFERED=1 python -u iterative_train.py --data_dir data/wikitext103 --output_dir results/extended_20gen/s42 --seed 42 --synthetic_ratio 1.0 --num_generations 20 --steps_per_gen 10000\\\"\", \"finished_at\": \"2026-05-15T11:41:42.336Z\", \"training_hours\": 12.0}, \"pid\": \"68368\", \"log_path\": \"~/runs/distrib_canary_collapse/plan_006_s42.log\", \"metrics\": {\"progress\": \"18/20 gen (gen_0-17 complete, gen_18-20 timeout)\", \"gen0_token_entropy\": 3.2342, \"gen17_token_entropy\": 1.1819, \"gen0_ece\": 0.0108, \"gen17_ece\": 0.4454, \"gen0_perplexity\": 26.95, \"gen17_perplexity\": 3367.66, \"gen0_distinct_1\": 0.0982, \"gen17_distinct_1\": 0.0756, \"gen0_distinct_2\": 0.5178, \"gen17_distinct_2\": 0.3617, \"gen0_distinct_3\": 0.8127, \"gen17_distinct_3\": 0.5865, \"token_entropy_drift_pct_gen0_17\": -63.4, \"distinct_1_drift_pct_gen0_17\": -23, \"distinct_2_drift_pct_gen0_17\": -30.1, \"distinct_3_drift_pct_gen0_17\": -27.8, \"ece_drift_pct_gen0_17\": 4024, \"ppl_drift_pct_gen0_17\": 12395, \"phase1_rapid_collapse\": \"gen0-5\", \"phase2_apparent_plateau\": \"gen5-12\", \"phase3_secondary_decline\": \"gen13-17\", \"phase3_d2_decline_pct\": -5.8, \"phase3_d3_decline_pct\": -6.9, \"diversity_saturated_at_gen\": 5, \"diversity_secondary_decline_at_gen\": 13, \"perplexity_saturated\": false}, \"failure_reason\": \"EXIT_CODE=124 (timeout — exceeded timeout_hours)\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-15T11:41:43.235Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-15T11:41:44.300301+00:00\"}]}, \"notes\": \"gen_0-17 complete (T=18). 三相 collapse: Phase1 急速崩塌 gen0-5 (d1 -20.6%, entropy -63.8%), Phase2 表观稳态 gen5-12 (diversity <0.3% 变化, perplexity 仍+167%), Phase3 二次衰退 gen13-17 (d2 -5.8%, d3 -6.9%). Perplexity 未饱和 (26.95→3367.66, +12395%). T=18 vs T=10: 新增 diversity 二次衰退在 T=10 window 不可见. TY power 预估 ~0.28-0.41 (vs T=10 的 0.05-0.21).\"}, \"plan_006_s42_resume\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T11:55:26.236Z\", \"updated_at\": \"2026-05-15T12:10:54.859Z\", \"spec\": {\"command\": \"python -u resume_plan006_s42.py\", \"server\": \"westd-19828\", \"gpu\": [\"cuda:0\"], \"pid\": \"114844\", \"log_path\": \"~/runs/distrib_canary_collapse/plan_006_s42_resume.log\", \"submitted_at\": \"2026-05-15T11:55:31.984Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"hypothesis\": \"恢复 plan_006_s42 从 gen_17，完成 gen_18-20 + all_metrics（α=1.0, 20gen, s42）\", \"seed\": 42, \"model_name\": \"EleutherAI/pythia-410m\", \"data_path\": \"data/wikitext103\", \"data_count\": 0, \"checkpoint_path\": \"N/A\", \"notes\": \"D034 决定不恢复，T=18 数据已足够（超出 T=15 目标）。plan_006_s42 gen_0-17 数据可用。\", \"wall_clock_seconds\": 921.5, \"gpu_hours\": 0.26}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-15T12:10:53.514Z\", \"notes\": \"D034 决定不恢复。T=18 数据已足够（超出 T=15 目标）。原 plan_006_s42 gen_0-17 数据可用于 power analysis + supplementary。\"}, \"gen_wiki_gpt2m_a100_s42_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T12:02:06.478Z\", \"updated_at\": \"2026-05-15T12:04:50.741Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && mkdir -p results/gen_wiki_gpt2m_a100_s42 && HF_HOME=/root/autodl-tmp/.hf_cache TRANSFORMERS_OFFLINE=1 HF_HUB_DISABLE_XET=1 PYTHONUNBUFFERED=1 python -u iterative_train.py --model_name /root/autodl-tmp/models/gpt2-medium --data_dir data/wikitext103_5k --synthetic_ratio 1.0 --num_generations 10 --steps_per_gen 5000 --batch_size 32 --seed 42 --output_dir results/gen_wiki_gpt2m_a100_s42\\\"\", \"server\": \"westd-19828\", \"gpu\": [\"cuda:0\"], \"pid\": \"116204\", \"log_path\": \"~/runs/distrib_canary_collapse/gen_wiki_gpt2m_a100_s42_v2.log\", \"submitted_at\": \"2026-05-15T12:02:14.440Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 18.0, \"gpu_hours\": 0.01}, \"server\": \"westd-19828\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-19828\", \"gpu\": \"cuda:0\", \"started_at\": \"2026-05-15T12:02:13.557Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && mkdir -p results/gen_wiki_gpt2m_a100_s42 && HF_HOME=/root/autodl-tmp/.hf_cache TRANSFORMERS_OFFLINE=1 HF_HUB_DISABLE_XET=1 PYTHONUNBUFFERED=1 python -u iterative_train.py --model_name /root/autodl-tmp/models/gpt2-medium --data_dir data/wikitext103_5k --synthetic_ratio 1.0 --num_generations 10 --steps_per_gen 5000 --batch_size 32 --seed 42 --output_dir results/gen_wiki_gpt2m_a100_s42\\\"\", \"finished_at\": \"2026-05-15T12:02:31.643Z\", \"training_hours\": 0.01}, \"pid\": \"116204\", \"log_path\": \"~/runs/distrib_canary_collapse/gen_wiki_gpt2m_a100_s42_v2.log\", \"failure_reason\": \"EXIT_CODE=1 (generic error — check log tail)\", \"conclusion\": \"killed\", \"completed_at\": \"2026-05-15T12:02:32.472Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-15T12:02:33.931882+00:00\"}]}}, \"gen_wiki_gpt2m_a100_s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T10:35:18.700Z\", \"updated_at\": \"2026-05-15T12:01:58.523Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && mkdir -p results/gen_wiki_gpt2m_a100_s42 && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_DISABLE_XET=1 PYTHONUNBUFFERED=1 python -u iterative_train.py --model_name gpt2-medium --data_dir data/wikitext103_5k --synthetic_ratio 1.0 --num_generations 10 --steps_per_gen 5000 --batch_size 32 --seed 42 --output_dir results/gen_wiki_gpt2m_a100_s42\\\"\", \"server\": \"westd-19828\", \"gpu\": [\"cuda:0\"], \"pid\": \"115532\", \"log_path\": \"~/runs/distrib_canary_collapse/gen_wiki_gpt2m_a100_s42.log\", \"submitted_at\": \"2026-05-15T11:57:48.767Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 249.8, \"gpu_hours\": 0.07}, \"server\": \"westd-19828\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-19828\", \"gpu\": \"cuda:0\", \"started_at\": \"2026-05-15T11:57:47.340Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && mkdir -p results/gen_wiki_gpt2m_a100_s42 && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_DISABLE_XET=1 PYTHONUNBUFFERED=1 python -u iterative_train.py --model_name gpt2-medium --data_dir data/wikitext103_5k --synthetic_ratio 1.0 --num_generations 10 --steps_per_gen 5000 --batch_size 32 --seed 42 --output_dir results/gen_wiki_gpt2m_a100_s42\\\"\"}, \"pid\": \"115532\", \"log_path\": \"~/runs/distrib_canary_collapse/gen_wiki_gpt2m_a100_s42.log\", \"conclusion\": \"killed\", \"completed_at\": \"2026-05-15T12:01:58.523Z\"}, \"method_ablation_phase2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T08:58:35.270Z\", \"updated_at\": \"2026-05-15T11:07:42.688Z\", \"spec\": {\"hypothesis\": \"Method sensitivity is compounded by regime dependence — method x alpha interaction is the headline Claim 3 evidence\", \"command\": \"python method_ablation_phase2.py\", \"server\": \"westd-19828\", \"data_path\": \"results/alpha_sweep + results/mvp\", \"data_count\": 56, \"model_name\": \"N/A (analysis)\", \"seed\": \"42,43,44,45\", \"checkpoint_path\": \"N/A\", \"log_path\": \"results/method_ablation_phase2_panel.json\"}, \"conclusion\": \"success\", \"metrics\": {\"n_panel_rows\": 56, \"n_alphas\": 4, \"alphas\": [0, 0.25, 0.5, 1], \"naive_sig_rate_overall\": 1, \"perm_granger_sig_rate_a000_raw\": 0, \"perm_granger_sig_rate_a000_fdr\": 0, \"perm_granger_sig_rate_a025_raw\": 0.25, \"perm_granger_sig_rate_a025_fdr\": 0, \"perm_granger_sig_rate_a050_raw\": 0.25, \"perm_granger_sig_rate_a050_fdr\": 0, \"perm_granger_sig_rate_a100_raw\": 0.75, \"perm_granger_sig_rate_a100_fdr\": 0.75, \"TY_sig_rate_a000_raw\": 0, \"TY_sig_rate_a000_fdr\": 0, \"TY_sig_rate_a025_raw\": 0.625, \"TY_sig_rate_a025_fdr\": 0.375, \"TY_sig_rate_a050_raw\": 0, \"TY_sig_rate_a050_fdr\": 0, \"TY_sig_rate_a100_raw\": 0.5938, \"TY_sig_rate_a100_fdr\": 0.5938, \"diff_sig_rate_a000_raw\": 0.5, \"diff_sig_rate_a000_fdr\": 0.375, \"mean_inter_method_kappa\": 0.185, \"naive_vs_perm_granger_flip_rate\": 0.5, \"naive_vs_TY_flip_rate\": 0.57, \"fdr_flips_perm_granger\": 4, \"pair_verdict_a100_perm_granger\": \"6/8\", \"pair_verdict_a100_TY\": \"6/8\", \"entropy_to_diversity_a100_all_5methods_sig\": true, \"fdr_correction\": \"BH q=0.05\"}, \"completed_at\": \"2026-05-15T08:58:54.741Z\"}, \"alpha_sweep_a025_s42_v3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T21:04:05.726Z\", \"updated_at\": \"2026-05-15T05:13:22.207Z\", \"spec\": {\"hypothesis\": \"α=0.25 低污染: 测试 canary→diversity lead 在温和 collapse 下是否保持\", \"model_name\": \"EleutherAI/pythia-410m\", \"data_path\": \"/root/autodl-tmp/distrib_canary_collapse/data/wikitext103_5k\", \"data_count\": 5000, \"seed\": 42, \"synthetic_ratio\": 0.25, \"num_generations\": 10, \"steps_per_gen\": 5000, \"parent\": \"alpha_sweep_a025_s42_v2 (failed, data corruption)\", \"command\": \"bash -c \\\"cd /root/autodl-tmp/distrib_canary_collapse && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_HUB_DISABLE_XET=1 && export HF_ENDPOINT=https://hf-mirror.com && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && PYTHONUNBUFFERED=1 python -u iterative_train.py --seed 42 --data_dir data/wikitext103_5k --steps_per_gen 5000 --num_generations 10 --synthetic_ratio 0.25 --output_dir results/alpha_sweep/a025_s42\\\"\", \"server\": \"westd-19828\", \"gpu\": [\"cuda:1\"], \"pid\": \"53069\", \"log_path\": \"~/runs/distrib_canary_collapse/alpha_sweep_a025_s42_v3.log\"}, \"reproduce\": {\"finished_at\": \"2026-05-15T01:18:42.377Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T01:18:43.329069+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"gen0_token_entropy\": 3.2342, \"gen10_token_entropy\": 3.1017, \"gen0_ece\": 0.0108, \"gen10_ece\": 0.01942, \"gen0_perplexity\": 26.95, \"gen10_perplexity\": 22.32, \"gen0_distinct_1\": 0.0982, \"gen10_distinct_1\": 0.0586, \"gen0_distinct_2\": 0.5178, \"gen10_distinct_2\": 0.2219, \"gen0_distinct_3\": 0.8127, \"gen10_distinct_3\": 0.3263, \"token_entropy_drift_pct\": -4.1, \"ece_drift_pct\": 79.7, \"perplexity_drift_pct\": -17.2, \"distinct_1_drift_pct\": -40.3, \"distinct_2_drift_pct\": -57.1, \"distinct_3_drift_pct\": -59.9}, \"checkpoint_path\": \"/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a025_s42/gen_10/checkpoint\", \"completed_at\": \"2026-05-15T01:26:19.292Z\", \"notes\": \"实际磁盘路径为 results/alpha_sweep/a025_s42/（无 v3 后缀）。Registry ID 带 v3 是历史原因，数据已核实无误。\"}, \"method_ablation_phase1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T23:49:16.519Z\", \"updated_at\": \"2026-05-14T23:49:40.162Z\", \"spec\": {\"plan_id\": \"plan_002\", \"hypothesis\": \"lead-lag 结论对分析方法高度敏感——naive Pearson 100% SIG vs TY 25% SIG，方法选择改变 75% 的结论\", \"command\": \"python method_ablation.py + python permutation_granger.py (差分版)\", \"server\": \"westd-19828\", \"data_path\": \"results/mvp/rep_{42,43,44,45}/all_metrics.json\", \"data_count\": 4, \"model_name\": \"N/A (analysis on MVP data)\", \"seed\": \"42,43,44,45\", \"checkpoint_path\": \"N/A\", \"log_path\": \"results/mvp/analysis/method_ablation.json\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T23:49:37.295Z\", \"metrics\": {\"spurious_rate_5method\": 0.75, \"spurious_rate_4method\": 0.625, \"naive_sig\": \"16/16\", \"differenced_sig\": \"14/16\", \"threshold_sig\": \"9/16\", \"permutation_granger_sig\": \"6/16\", \"ty_sig\": \"4/16\", \"ty_power_T10\": \"0.05-0.20\", \"bh_fdr_flips\": 0}}, \"alpha_sweep_a000_s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T19:01:37.470Z\", \"updated_at\": \"2026-05-14T23:42:18.748Z\", \"spec\": {\"hypothesis\": \"α=0.0 null control: 纯 real data 再训练无 canary signal，确认 signal 源于合成污染\", \"model_name\": \"EleutherAI/pythia-410m\", \"data_path\": \"/root/autodl-tmp/distrib_canary_collapse/data/wikitext103_5k\", \"data_count\": 5000, \"seed\": 42, \"synthetic_ratio\": 0, \"num_generations\": 10, \"steps_per_gen\": 5000, \"command\": \"bash -c \\\"cd /root/autodl-tmp/distrib_canary_collapse && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_HUB_DISABLE_XET=1 && export HF_ENDPOINT=https://hf-mirror.com && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && PYTHONUNBUFFERED=1 python -u iterative_train.py --seed 42 --data_dir data/wikitext103_5k --steps_per_gen 5000 --num_generations 10 --synthetic_ratio 0.0 --output_dir results/alpha_sweep/a000_s42\\\"\", \"server\": \"westd-19828\", \"gpu\": [\"cuda:0\"], \"pid\": \"46716\", \"log_path\": \"~/runs/distrib_canary_collapse/alpha_sweep_a000_s42.log\"}, \"reproduce\": {\"finished_at\": \"2026-05-14T23:36:35.414Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T23:36:36.221435+00:00\"}]}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a000_s42/gen_10/checkpoint\", \"log_path\": \"~/runs/distrib_canary_collapse/alpha_sweep_a000_s42.log\", \"metrics\": {\"gen0_token_entropy\": 3.2342, \"gen10_token_entropy\": 3.0693, \"gen0_ece\": 0.0108, \"gen10_ece\": 0.0164, \"gen0_perplexity\": 26.95, \"gen10_perplexity\": 21.11, \"gen0_distinct_1\": 0.0982, \"gen10_distinct_1\": 0.0847, \"token_entropy_drift_pct\": -5.1, \"ece_drift_pct\": 51.7, \"perplexity_drift_pct\": -21.7, \"distinct_1_drift_pct\": -13.8, \"distinct_2_drift_pct\": -9.8, \"distinct_3_drift_pct\": -4.5, \"gen1_10_perplexity_drift_pct\": 9.4, \"gen1_10_distinct_1_drift_pct\": -13.1, \"gen1_10_entropy_drift_pct\": 2.6}, \"completed_at\": \"2026-05-14T23:39:04.310Z\"}, \"plan_009_bootstrap_ty\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T21:33:04.665Z\", \"updated_at\": \"2026-05-14T21:33:27.106Z\", \"spec\": {\"hypothesis\": \"Monte Carlo 验证 TY Granger 在短时间序列 (T=10,15,20,30) 下的 Type I error 和 statistical power\", \"command\": \"python bootstrap_ty_validation.py (N_sim=1000)\", \"server\": \"westd-19828\", \"data_path\": \"synthetic DGP (AR(1) for H0, VAR(2) for H1)\", \"data_count\": 1000, \"model_name\": \"N/A (statistical simulation)\", \"seed\": \"multiple\", \"log_path\": \"results/bootstrap_ty_results.json\", \"checkpoint_path\": \"N/A\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T21:33:24.769Z\", \"metrics\": {\"T10_d0_type1\": 0.081, \"T10_d0_power\": 0.205, \"T10_d1_type1\": 0.047, \"T10_d1_power\": 0.09, \"T10_dadapt_type1\": 0.052, \"T10_dadapt_power\": 0.05, \"T20_d0_power\": 0.409, \"T20_d1_power\": 0.172, \"T30_d0_power\": 0.606, \"T30_d1_power\": 0.283}}, \"mvp_v3_rep43\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T06:25:42.195Z\", \"updated_at\": \"2026-05-14T06:48:01.316Z\", \"spec\": {\"command\": \"python iterative_train.py --seed 43 --output_dir results/mvp/rep_43 --data_dir data/wikitext103_5k --synthetic_ratio 1.0 --num_generations 10 --steps_per_gen 5000\", \"server\": \"autodl-rtx6000\", \"gpu\": \"cuda:1\", \"pid\": \"7987\", \"log_path\": \"~/runs/distrib_canary_collapse/mvp_v3_rep43.log\", \"submitted_at\": \"2026-05-14T06:26:18.477Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/distrib_canary_collapse/data/wikitext103_5k\", \"data_count\": 5000, \"model_name\": \"EleutherAI/pythia-410m\", \"seed\": 43, \"gpu_model\": \"RTX PRO 6000 Blackwell 96GB\", \"tmux_session\": \"mvp_v3_rep43\", \"checkpoint_path\": \"N/A\", \"failure_reason\": \"MAUVE FAISS crash: max_samples=500 → p+q=1000 < 1950 required; 无 PYTHONUNBUFFERED 导致日志丢失\", \"wall_clock_seconds\": 1302.8, \"gpu_hours\": 0.36}, \"conclusion\": \"failed\", \"completed_at\": \"2026-05-14T06:48:01.316Z\"}, \"mvp_v3_rep42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T06:25:39.728Z\", \"updated_at\": \"2026-05-14T06:47:59.908Z\", \"spec\": {\"command\": \"python iterative_train.py --seed 42 --output_dir results/mvp/rep_42 --data_dir data/wikitext103_5k --synthetic_ratio 1.0 --num_generations 10 --steps_per_gen 5000\", \"server\": \"autodl-rtx6000\", \"gpu\": \"cuda:0\", \"pid\": \"7909\", \"log_path\": \"~/runs/distrib_canary_collapse/mvp_v3_rep42.log\", \"submitted_at\": \"2026-05-14T06:26:16.939Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/distrib_canary_collapse/data/wikitext103_5k\", \"data_count\": 5000, \"model_name\": \"EleutherAI/pythia-410m\", \"seed\": 42, \"gpu_model\": \"RTX PRO 6000 Blackwell 96GB\", \"tmux_session\": \"mvp_v3_rep42\", \"checkpoint_path\": \"N/A\", \"failure_reason\": \"MAUVE FAISS crash: max_samples=500 → p+q=1000 < 1950 required; 无 PYTHONUNBUFFERED 导致日志丢失\", \"wall_clock_seconds\": 1303.0, \"gpu_hours\": 0.36}, \"conclusion\": \"failed\", \"completed_at\": \"2026-05-14T06:47:59.908Z\"}, \"mvp_v2_rep43\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T05:38:10.434Z\", \"updated_at\": \"2026-05-14T06:25:28.345Z\", \"spec\": {\"command\": \"python iterative_train.py --seed 43 --output_dir results/mvp/rep_43 --data_dir data/wikitext103_5k --synthetic_ratio 1.0 --num_generations 10 --steps_per_gen 5000\", \"server\": \"autodl-rtx6000\", \"gpu\": \"cuda:1\", \"pid\": \"5364\", \"log_path\": \"~/runs/distrib_canary_collapse/mvp_v2_rep43.log\", \"submitted_at\": \"2026-05-14T05:42:39.039Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/distrib_canary_collapse/data/wikitext103_5k\", \"data_count\": 5000, \"model_name\": \"EleutherAI/pythia-410m\", \"seed\": 43, \"gpu_model\": \"RTX PRO 6000 Blackwell 96GB\", \"tmux_session\": \"mvp_v2_rep43\", \"checkpoint_path\": \"N/A\", \"kill_reason\": \"v1旧进程未死导致输出目录冲突，v2死锁\", \"wall_clock_seconds\": 2569.3, \"gpu_hours\": 0.71}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-14T06:25:28.345Z\"}, \"mvp_v2_rep42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T05:38:05.054Z\", \"updated_at\": \"2026-05-14T06:25:27.286Z\", \"spec\": {\"command\": \"python iterative_train.py --seed 42 --output_dir results/mvp/rep_42 --data_dir data/wikitext103_5k --synthetic_ratio 1.0 --num_generations 10 --steps_per_gen 5000\", \"server\": \"autodl-rtx6000\", \"gpu\": \"cuda:0\", \"pid\": \"5286\", \"log_path\": \"~/runs/distrib_canary_collapse/mvp_v2_rep42.log\", \"submitted_at\": \"2026-05-14T05:42:37.404Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/distrib_canary_collapse/data/wikitext103_5k\", \"data_count\": 5000, \"model_name\": \"EleutherAI/pythia-410m\", \"seed\": 42, \"gpu_model\": \"RTX PRO 6000 Blackwell 96GB\", \"tmux_session\": \"mvp_v2_rep42\", \"checkpoint_path\": \"N/A\", \"kill_reason\": \"v1旧进程未死导致输出目录冲突，v2死锁\", \"wall_clock_seconds\": 2569.9, \"gpu_hours\": 0.71}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-14T06:25:27.286Z\"}, \"mvp_rep43\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T05:12:14.237Z\", \"updated_at\": \"2026-05-14T05:37:18.575Z\", \"spec\": {\"command\": \"python iterative_train.py --seed 43 --output_dir results/mvp/rep_43 --data_dir data/wikitext103 --synthetic_ratio 1.0 --num_generations 10 --steps_per_gen 10000\", \"server\": \"autodl-rtx6000\", \"gpu\": \"cuda:1\", \"pid\": \"3956\", \"log_path\": \"~/runs/distrib_canary_collapse/mvp_rep43.log\", \"submitted_at\": \"2026-05-14T05:34:47.702Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/distrib_canary_collapse/data/wikitext103\", \"data_count\": 716506, \"model_name\": \"EleutherAI/pythia-410m\", \"seed\": 43, \"gpu_model\": \"RTX PRO 6000 Blackwell 96GB\", \"tmux_session\": \"mvp_rep43\", \"checkpoint_path\": \"N/A\", \"kill_reason\": \"参数修复: n_prompts 1000→5000, steps_per_gen 10000→5000\", \"wall_clock_seconds\": 150.9, \"gpu_hours\": 0.04}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-14T05:37:18.575Z\"}, \"mvp_rep42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T05:12:13.930Z\", \"updated_at\": \"2026-05-14T05:37:17.438Z\", \"spec\": {\"command\": \"python iterative_train.py --seed 42 --output_dir results/mvp/rep_42 --data_dir data/wikitext103 --synthetic_ratio 1.0 --num_generations 10 --steps_per_gen 10000\", \"server\": \"autodl-rtx6000\", \"gpu\": \"cuda:0\", \"pid\": \"3878\", \"log_path\": \"~/runs/distrib_canary_collapse/mvp_rep42.log\", \"submitted_at\": \"2026-05-14T05:34:46.013Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/distrib_canary_collapse/data/wikitext103\", \"data_count\": 716506, \"model_name\": \"EleutherAI/pythia-410m\", \"seed\": 42, \"gpu_model\": \"RTX PRO 6000 Blackwell 96GB\", \"tmux_session\": \"mvp_rep42\", \"checkpoint_path\": \"N/A\", \"kill_reason\": \"参数修复: n_prompts 1000→5000, steps_per_gen 10000→5000\", \"wall_clock_seconds\": 151.4, \"gpu_hours\": 0.04}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-14T05:37:17.438Z\"}}, \"count\": 34, \"total\": 34, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.0843}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "82ac2b1a-122b-407f-97da-ea46c6a7db4d",
  "isSidechain": false,
  "promptId": "a304cee9-feed-4fb2-a028-8ae1d93109aa",
  "type": "user",
  "uuid": "77a22979-7396-4263-8c18-5b02f25c8ec3",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-4-projects-distrib-canary-collapse--claude-sessions-agent-e1f64cd5/4f6074eb-8665-49ec-9526-07c9eebcea03/tool-results/toolu_01BxadqtFPAy7HcgcjyPHhCs.txt",
      "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {\\\"alpha_sweep_a025_s44\\\": {\\\"status\\\": \\\"ANALYZING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-15T06:58:48.224Z\\\", \\\"updated_at\\\": \\\"2026-05-16T02:24:25.189Z\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"cd /root/autodl-tmp/distrib_canary_collapse && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_HUB_DISABLE_XET=1 && export HF_ENDPOINT=https://hf-mirror.com && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && PYTHONUNBUFFERED=1 python -u iterative_train.py --seed 44 --data_dir data/wikitext103_5k --steps_per_gen 5000 --num_generations 10 --synthetic_ratio 0.25 --output_dir results/alpha_sweep/a025_s44\\\\\\\"\\\", \\\"server\\\": \\\"westd-19828\\\", \\\"gpu\\\": [\\\"cuda:1\\\"], \\\"pid\\\": \\\"147811\\\", \\\"log_path\\\": \\\"~/runs/distrib_canary_collapse/alpha_sweep_a025_s44.log\\\", \\\"submitted_at\\\": \\\"2026-05-15T22:04:28.318Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\"}, \\\"server\\\": \\\"westd-19828\\\", \\\"gpu\\\": \\\"cuda:1\\\", \\\"account\\\": \\\"root\\\", \\\"reproduce\\\": {\\\"server\\\": \\\"westd-19828\\\", \\\"gpu\\\": \\\"cuda:1\\\", \\\"started_at\\\": \\\"2026-05-15T22:04:26.677Z\\\", \\\"command\\\": \\\"bash -c \\\\\\\"cd /root/autodl-tmp/distrib_canary_collapse && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_HUB_DISABLE_XET=1 && export HF_ENDPOINT=https://hf-mirror.com && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && PYTHONUNBUFFERED=1 python -u iterative_train.py --seed 44 --data_dir data/wikitext103_5k --steps_per_gen 5000 --num_generations 10 --synthetic_ratio 0.25 --output_dir results/alpha_sweep/a025_s44\\\\\\\"\\\", \\\"finished_at\\\": \\\"2026-05-16T02:24:25.056Z\\\", \\\"training_hours\\\": 4.33}, \\\"pid\\\": \\\"147811\\\", \\\"log_path\\\": \\\"~/runs/distrib_canary_collapse/alpha_sweep_a025_s44.log\\\", \\\"extra\\\": {\\\"hook_events\\\": [{\\\"event\\\": \\\"on_complete\\\", \\\"action\\\": \\\"agent\\\", \\\"ts\\\": \\\"2026-05-16T02:24:26.614491+00:00\\\"}]}}, \\\"mvp_v2_rep44\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-14T05:38:10.762Z\\\", \\\"updated_at\\\": \\\"2026-05-16T00:10:26.251Z\\\", \\\"spec\\\": {\\\"hypothesis\\\": \\\"至少一族canary指标在100% SC full replacement下对downstream指标有≥1 gen的时序领先性\\\", \\\"model_name\\\": \\\"EleutherAI/pythia-410m\\\", \\\"data_path\\\": \\\"/root/autodl-tmp/distrib_canary_collapse/data/wikitext103\\\", \\\"data_count\\\": 5000, \\\"seed\\\": 44, \\\"server\\\": \\\"autodl-rtx6000\\\", \\\"gpu\\\": \\\"pending\\\", \\\"synthetic_ratio\\\": 1, \\\"num_generations\\\": 10, \\\"steps_per_gen\\\": 5000, \\\"n_prompts\\\": 5000, \\\"fix_note\\\": \\\"n_prompts 1000→5000, steps_per_gen 10000→5000, 避免过拟合\\\"}, \\\"conclusion\\\": \\\"killed\\\", \\\"completed_at\\\": \\\"2026-05-16T00:10:26.251Z\\\"}, \\\"mvp_rep44\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-14T05:12:15.033Z\\\", \\\"updated_at\\\": \\\"2026-05-16T00:10:25.605Z\\\", \\\"spec\\\": {\\\"hypothesis\\\": \\\"至少一族canary指标在100% SC full replacement下对downstream指标有≥1 gen的时序领先性\\\", \\\"model_name\\\": \\\"EleutherAI/pythia-410m\\\", \\\"data_path\\\": \\\"/root/autodl-tmp/distrib_canary_collapse/data/wikitext103\\\", \\\"seed\\\": 44, \\\"server\\\": \\\"autodl-rtx6000\\\", \\\"gpu\\\": \\\"pending\\\", \\\"synthetic_ratio\\\": 1, \\\"num_generations\\\": 10, \\\"steps_per_gen\\\": 10000}, \\\"metrics\\\": {\\\"gen10_token_entropy\\\": 1.2205, \\\"gen10_ece\\\": 0.4237, \\\"gen10_perplexity\\\": 1033.16, \\\"gen10_distinct_1\\\": 0.0731, \\\"gen10_distinct_2\\\": 0.3637, \\\"gen10_distinct_3\\\": 0.6075}, \\\"conclusion\\\": \\\"killed\\\", \\\"completed_at\\\": \\\"2026-05-16T00:10:25.605Z\\\"}, \\\"alpha_sweep_a025_s42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-14T19:01:39.527Z\\\", \\\"updated_at\\\": \\\"2026-05-16T00:10:24.973Z\\\", \\\"spec\\\": {\\\"hypothesis\\\": \\\"α=0.25 低污染: 测试 canary→diversity lead 在温和 collapse 下是否保持，canary→perplexity lead 是否出现\\\", \\\"model_name\\\": \\\"EleutherAI/pythia-410m\\\", \\\"data_path\\\": \\\"/root/autodl-tmp/distrib_canary_collapse/data/wikitext103_5k\\\", \\\"data_count\\\": 5000, \\\"seed\\\": 42, \\\"synthetic_ratio\\\": 0.25, \\\"num_generations\\\": 10, \\\"steps_per_gen\\\": 5000}, \\\"conclusion\\\": \\\"killed\\\", \\\"completed_at\\\": \\\"2026-05-16T00:10:24.973Z\\\"}, \\\"alpha_sweep_a025_s42_v2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-14T19:25:52.094Z\\\", \\\"updated_at\\\": \\\"2026-05-16T00:10:24.568Z\\\", \\\"spec\\\": {\\\"hypothesis\\\": \\\"α=0.25 低污染: 测试 canary→diversity lead 在温和 collapse 下是否保持，canary→perplexity lead 是否出现\\\", \\\"model_name\\\": \\\"EleutherAI/pythia-410m\\\", \\\"data_path\\\": \\\"/root/autodl-tmp/distrib_canary_collapse/data/wikitext103_5k\\\", \\\"data_count\\\": 5000, \\\"seed\\\": 42, \\\"synthetic_ratio\\\": 0.25, \\\"num_generations\\\": 10, \\\"steps_per_gen\\\": 5000, \\\"parent\\\": \\\"alpha_sweep_a025_s42 (killed, subsample bias fix)\\\"}, \\\"conclusion\\\": \\\"killed\\\", \\\"failure_reason\\\": \\\"data corruption: unkilled old process PID 46802 wrote concurrently with new PID 48454\\\", \\\"completed_at\\\": \\\"2026-05-16T00:10:24.568Z\\\"}, \\\"alpha_sweep_a060_s42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-14T21:52:22.516Z\\\", \\\"updated_at\\\": \\\"2026-05-16T00:04:01.429Z\\\", \\\"spec\\\": {\\\"hypothesis\\\": \\\"α=0.60 中高污染: phase boundary 精确化, 与 α=0.50/0.75 对比 lead time 变化\\\", \\\"model_name\\\": \\\"EleutherAI/pythia-410m\\\", \\\"data_path\\\": \\\"/root/autodl-tmp/distrib_canary_collapse/data/wikitext103_5k\\\", \\\"data_count\\\": 5000, \\\"seed\\\": 42, \\\"synthetic_ratio\\\": 0.6, \\\"num_generations\\\": 10, \\\"steps_per_gen\\\": 5000}, \\\"conclusion\\\": \\\"killed\\\", \\\"completed_at\\\": \\\"2026-05-16T00:04:01.429Z\\\"}, \\\"alpha_sweep_a010_s42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-14T21:52:19.712Z\\\", \\\"updated_at\\\": \\\"2026-05-16T00:03:53.018Z\\\", \\\"spec\\\": {\\\"hypothesis\\\": \\\"α=0.10 极低污染: phase boundary 精确化, canary signal 是否仍可检测\\\", \\\"model_name\\\": \\\"EleutherAI/pythia-410m\\\", \\\"data_path\\\": \\\"/root/autodl-tmp/distrib_canary_collapse/data/wikitext103_5k\\\", \\\"data_count\\\": 5000, \\\"seed\\\": 42, \\\"synthetic_ratio\\\": 0.1, \\\"num_generations\\\": 10, \\\"steps_per_gen\\\": 5000}, \\\"conclusion\\\": \\\"killed\\\", \\\"completed_at\\\": \\\"2026-05-16T00:03:53.018Z\\\"}, \\\"alpha_sweep_a050_s44\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-15T06:58:50.550Z\\\", \\\"updated_at\\\": \\\"2026-05-16T00:03:52.118Z\\\", \\\"spec\\\": {\\\"hypothesis\\\": \\\"α=0.50 multi-seed replication (seed=44): 第三个 seed 为置信区间提供统计力\\\", \\\"model_name\\\": \\\"EleutherAI/pythia-410m\\\", \\\"data_path\\\": \\\"/root/autodl-tmp/distrib_canary_collapse/data/wikitext103_5k\\\", \\\"data_count\\\": 5000, \\\"seed\\\": 44, \\\"synthetic_ratio\\\": 0.5, \\\"num_generations\\\": 10, \\\"steps_per_gen\\\": 5000, \\\"parent\\\": \\\"alpha_sweep_a050_s42\\\", \\\"priority\\\": \\\"D026-4\\\"}, \\\"conclusion\\\": \\\"killed\\\", \\\"completed_at\\\": \\\"2026-05-16T00:03:52.118Z\\\"}, \\\"plan_006_s43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-14T23:31:37.257Z\\\", \\\"updated_at\\\": \\\"2026-05-16T00:03:51.617Z\\\", \\\"spec\\\": {\\\"plan_id\\\": \\\"plan_006\\\", \\\"hypothesis\\\": \\\"Multi-seed replication of three-phase collapse dynamics: verify Phase 3 secondary decline (gen 13+) reproduces with seed=43, confirming it is not a single-seed artifact\\\", \\\"model_name\\\": \\\"EleutherAI/pythia-410m\\\", \\\"seed\\\": 43, \\\"data_path\\\": \\\"data/wikitext103_5k\\\", \\\"num_generations\\\": 18, \\\"synthetic_ratio\\\": 1, \\\"max_lag\\\": 10, \\\"data_count\\\": 5000, \\\"steps_per_gen\\\": 5000, \\\"parent\\\": \\\"plan_006_s42\\\", \\\"claim\\\": 1, \\\"priority\\\": \\\"P0\\\"}, \\\"conclusion\\\": \\\"killed\\\", \\\"completed_at\\\": \\\"2026-05-16T00:03:51.617Z\\\"}, \\\"gen_wiki_gpt2m_a100_s42_v3\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-15T12:07:20.050Z\\\", \\\"updated_at\\\": \\\"2026-05-15T22:30:21.573Z\\\", \\\"spec\\\": {\\\"hypothesis\\\": \\\"Method sensitivity patterns (Granger FDR collapse, cross-correlation dominance) generalize from GPT-2-small to GPT-2-medium, validating cross-architecture universality of methodological pitfalls\\\", \\\"seed\\\": 42, \\\"model_name\\\": \\\"gpt2-medium\\\", \\\"data_path\\\": \\\"data/wikitext103_5k\\\", \\\"data_count\\\": 5000}, \\\"server\\\": \\\"westd-19828\\\", \\\"gpu\\\": \\\"cuda:0\\\", \\\"account\\\": \\\"root\\\", \\\"reproduce\\\": {\\\"server\\\": \\\"westd-19828\\\", \\\"gpu\\\": \\\"cuda:0\\\", \\\"started_at\\\": \\\"2026-05-15T12:07:30.366Z\\\", \\\"command\\\": \\\"bash -c \\\\\\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && mkdir -p results/gen_wiki_gpt2m_a100_s42 && HF_HOME=/root/autodl-tmp/.hf_cache TRANSFORMERS_OFFLINE=1 HF_HUB_DISABLE_XET=1 PYTHONUNBUFFERED=1 python -u iterative_train.py --model_name gpt2-medium --data_dir data/wikitext103_5k --synthetic_ratio 1.0 --num_generations 10 --steps_per_gen 5000 --batch_size 32 --seed 42 --output_dir results/gen_wiki_gpt2m_a100_s42\\\\\\\"\\\", \\\"finished_at\\\": \\\"2026-05-15T22:14:43.852Z\\\", \\\"training_hours\\\": 10.12}, \\\"pid\\\": \\\"117632\\\", \\\"log_path\\\": \\\"~/runs/distrib_canary_collapse/gen_wiki_gpt2m_a100_s42_v3.log\\\", \\\"metrics\\\": {\\\"token_entropy_drift_pct\\\": -86.5, \\\"ece_drift_pct\\\": 4543, \\\"perplexity_drift_pct\\\": 44703, \\\"distinct_1_drift_pct\\\": -12.4, \\\"distinct_2_drift_pct\\\": -14.7, \\\"distinct_3_drift_pct\\\": -12.7, \\\"five_method_forward_consensus\\\": \\\"6/6 pairs at 4/5 methods (Tier 3)\\\", \\\"five_method_reverse_consensus\\\": \\\"0/6 pairs\\\", \\\"naive_xcorr_forward\\\": \\\"|r|>0.98, all sig\\\", \\\"diff_xcorr_forward\\\": \\\"all p_fdr<0.001\\\", \\\"diff_xcorr_reverse\\\": \\\"all p>0.18 (clean directional separation)\\\", \\\"threshold_onset_entropy\\\": \\\"gen 1 (earliest canary)\\\", \\\"threshold_onset_ece\\\": \\\"gen 1-2\\\", \\\"threshold_onset_diversity\\\": \\\"gen 3\\\", \\\"perm_granger_forward\\\": \\\"p_fdr=0.003, BH corrected\\\", \\\"ty_granger_forward\\\": \\\"0/6 sig (df_resid=1-4, underpowered, consistent with Pythia C001)\\\", \\\"entropy_leads_diversity_lag\\\": \\\"1-2 gen\\\", \\\"ece_leads_diversity_lag\\\": \\\"1 gen\\\", \\\"diversity_plateau_from\\\": \\\"gen5\\\", \\\"cross_arch_note\\\": \\\"Replicates Pythia entropy-leads-diversity pattern at Tier 3 consensus. TY underpowered as expected.\\\"}, \\\"extra\\\": {\\\"hook_events\\\": [{\\\"event\\\": \\\"on_complete\\\", \\\"action\\\": \\\"agent\\\", \\\"ts\\\": \\\"2026-05-15T22:14:45.029003+00:00\\\"}]}, \\\"conclusion\\\": \\\"success\\\", \\\"checkpoint_path\\\": \\\"results/gen_wiki_gpt2m_a100_s42/\\\", \\\"completed_at\\\": \\\"2026-05-15T22:18:22.762Z\\\"}, \\\"gen_wiki_gpt2m_a025_s42\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-15T10:35:16.032Z\\\", \\\"updated_at\\\": \\\"2026-05-15T22:22:52.921Z\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && mkdir -p results/gen_wiki_gpt2m_a025_s42 && HF_HOME=/root/autodl-tmp/.hf_cache TRANSFORMERS_OFFLINE=1 HF_HUB_DISABLE_XET=1 PYTHONUNBUFFERED=1 python -u iterative_train.py --model_name gpt2-medium --data_dir data/wikitext103_5k --synthetic_ratio 0.25 --num_generations 10 --steps_per_gen 5000 --batch_size 32 --seed 42 --output_dir results/gen_wiki_gpt2m_a025_s42\\\\\\\"\\\", \\\"server\\\": \\\"westd-19828\\\", \\\"gpu\\\": [\\\"cuda:0\\\"], \\\"pid\\\": \\\"149202\\\", \\\"log_path\\\": \\\"~/runs/distrib_canary_collapse/gen_wiki_gpt2m_a025_s42.log\\\", \\\"submitted_at\\\": \\\"2026-05-15T22:22:52.615Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\"}, \\\"server\\\": \\\"westd-19828\\\", \\\"gpu\\\": \\\"cuda:0\\\", \\\"account\\\": \\\"root\\\", \\\"reproduce\\\": {\\\"server\\\": \\\"westd-19828\\\", \\\"gpu\\\": \\\"cuda:0\\\", \\\"started_at\\\": \\\"2026-05-15T22:22:51.021Z\\\", \\\"command\\\": \\\"bash -c \\\\\\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && mkdir -p results/gen_wiki_gpt2m_a025_s42 && HF_HOME=/root/autodl-tmp/.hf_cache TRANSFORMERS_OFFLINE=1 HF_HUB_DISABLE_XET=1 PYTHONUNBUFFERED=1 python -u iterative_train.py --model_name gpt2-medium --data_dir data/wikitext103_5k --synthetic_ratio 0.25 --num_generations 10 --steps_per_gen 5000 --batch_size 32 --seed 42 --output_dir results/gen_wiki_gpt2m_a025_s42\\\\\\\"\\\"}, \\\"pid\\\": \\\"149202\\\", \\\"log_path\\\": \\\"~/runs/distrib_canary_collapse/gen_wiki_gpt2m_a025_s42.log\\\"}, \\\"alpha_sweep_a050_s43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-15T06:58:45.880Z\\\", \\\"updated_at\\\": \\\"2026-05-15T22:15:50.290Z\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"cd /root/autodl-tmp/distrib_canary_collapse && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_HUB_DISABLE_XET=1 && export HF_ENDPOINT=https://hf-mirror.com && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && PYTHONUNBUFFERED=1 python -u iterative_train.py --seed 43 --data_dir data/wikitext103_5k --steps_per_gen 5000 --num_generations 10 --synthetic_ratio 0.50 --output_dir results/alpha_sweep/a050_s43\\\\\\\"\\\", \\\"server\\\": \\\"westd-19828\\\", \\\"gpu\\\": [\\\"cuda:1\\\"], \\\"pid\\\": \\\"134860\\\", \\\"log_path\\\": \\\"~/runs/distrib_canary_collapse/alpha_sweep_a050_s43.log\\\", \\\"submitted_at\\\": \\\"2026-05-15T17:40:27.060Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"wall_clock_seconds\\\": 16523.2, \\\"gpu_hours\\\": 4.59}, \\\"server\\\": \\\"westd-19828\\\", \\\"gpu\\\": \\\"cuda:1\\\", \\\"pid\\\": \\\"134860\\\", \\\"log_path\\\": \\\"~/runs/distrib_canary_collapse/alpha_sweep_a050_s43.log\\\", \\\"reproduce\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"cd /root/autodl-tmp/distrib_canary_collapse && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_HUB_DISABLE_XET=1 && export HF_ENDPOINT=https://hf-mirror.com && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && PYTHONUNBUFFERED=1 python -u iterative_train.py --seed 43 --data_dir data/wikitext103_5k --steps_per_gen 5000 --num_generations 10 --synthetic_ratio 0.50 --output_dir results/alpha_sweep/a050_s43\\\\\\\"\\\", \\\"finished_at\\\": \\\"2026-05-15T22:00:14.725Z\\\"}, \\\"extra\\\": {\\\"hook_events\\\": [{\\\"event\\\": \\\"on_complete\\\", \\\"action\\\": \\\"agent\\\", \\\"ts\\\": \\\"2026-05-15T22:00:15.908424+00:00\\\"}]}, \\\"conclusion\\\": \\\"success\\\", \\\"checkpoint_path\\\": \\\"results/alpha_sweep/a050_s43/gen_10/checkpoint/\\\", \\\"metrics\\\": {\\\"gen0_token_entropy\\\": 3.234195, \\\"gen0_ece\\\": 0.010805, \\\"gen0_perplexity\\\": 26.948959, \\\"gen10_token_entropy\\\": 2.672, \\\"gen10_ece\\\": 0.097, \\\"gen10_perplexity\\\": 32.633, \\\"gen0_distinct_1\\\": 0.09833, \\\"gen0_distinct_2\\\": 0.5132, \\\"gen0_distinct_3\\\": 0.8057, \\\"gen10_distinct_1\\\": 0.0624, \\\"gen10_distinct_2\\\": 0.2617, \\\"gen10_distinct_3\\\": 0.4126, \\\"token_entropy_drift_pct\\\": -17.4, \\\"ece_drift_pct\\\": 799, \\\"perplexity_drift_pct\\\": 21.1, \\\"distinct_1_drift_pct\\\": -36.5, \\\"distinct_2_drift_pct\\\": -49, \\\"distinct_3_drift_pct\\\": -48.8, \\\"cross_seed_note\\\": \\\"vs s42: drift direction identical, magnitude <7% deviation, ppl near-identical (32.633 vs 32.64)\\\"}, \\\"completed_at\\\": \\\"2026-05-15T22:00:14Z\\\"}, \\\"mvp_v4_rep45\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-14T13:41:26.286Z\\\", \\\"updated_at\\\": \\\"2026-05-15T21:29:54.928Z\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"cd /root/autodl-tmp/distrib_canary_collapse && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_HUB_DISABLE_XET=1 && export HF_ENDPOINT=https://hf-mirror.com && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && PYTHONUNBUFFERED=1 python -u iterative_train.py --seed 45 --data_dir data/wikitext103_5k --steps_per_gen 5000 --num_generations 10 --output_dir results/mvp/rep_45\\\\\\\"\\\", \\\"server\\\": \\\"westd-19828\\\", \\\"gpu\\\": [\\\"cuda:1\\\"], \\\"pid\\\": \\\"31425\\\", \\\"log_path\\\": \\\"~/runs/distrib_canary_collapse/mvp_v4_rep45.log\\\", \\\"submitted_at\\\": \\\"2026-05-14T13:42:10.455Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"data_path\\\": \\\"/root/autodl-tmp/distrib_canary_collapse/data/wikitext103_5k\\\", \\\"data_count\\\": 5000, \\\"model_name\\\": \\\"EleutherAI/pythia-410m\\\", \\\"seed\\\": 45, \\\"wall_clock_seconds\\\": 15350.2, \\\"gpu_hours\\\": 4.26}, \\\"reproduce\\\": {\\\"finished_at\\\": \\\"2026-05-14T17:55:42.230Z\\\"}, \\\"extra\\\": {\\\"hook_events\\\": [{\\\"event\\\": \\\"on_complete\\\", \\\"action\\\": \\\"agent\\\", \\\"ts\\\": \\\"2026-05-14T17:55:42.934182+00:00\\\"}]}, \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/distrib_canary_collapse/results/mvp/rep_45/gen_10/checkpoint\\\", \\\"metrics_summary\\\": {\\\"gen0_ppl\\\": 26.9, \\\"gen10_ppl\\\": 1016.2, \\\"gen0_entropy\\\": 3.234, \\\"gen10_entropy\\\": 1.315, \\\"gen0_ece\\\": 0.011, \\\"gen10_ece\\\": 0.417}, \\\"wall_clock_seconds\\\": 15212, \\\"gpu_hours\\\": 4.23, \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"gen0_token_entropy\\\": 3.234195, \\\"gen0_ece\\\": 0.010805, \\\"gen0_perplexity\\\": 26.948959, \\\"gen0_distinct_1\\\": 0.098574, \\\"gen0_distinct_2\\\": 0.51463, \\\"gen0_distinct_3\\\": 0.808362, \\\"gen10_token_entropy\\\": 1.31536, \\\"gen10_ece\\\": 0.41654, \\\"gen10_perplexity\\\": 1016.22, \\\"gen10_distinct_1\\\": 0.069859, \\\"gen10_distinct_2\\\": 0.329549, \\\"gen10_distinct_3\\\": 0.543743, \\\"token_entropy_drift_pct\\\": -59.3296, \\\"ece_drift_pct\\\": 3755.0671, \\\"perplexity_drift_pct\\\": 3670.9063, \\\"distinct_1_drift_pct\\\": -29.1304, \\\"distinct_2_drift_pct\\\": -35.9639, \\\"distinct_3_drift_pct\\\": -32.7352}, \\\"completed_at\\\": \\\"2026-05-14T17:58:00.661Z\\\"}, \\\"mvp_v4_rep44\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-14T07:48:52.613Z\\\", \\\"updated_at\\\": \\\"2026-05-15T21:29:52.398Z\\\", \\\"spec\\\": {\\\"hypothesis\\\": \\\"至少一族canary指标在100% SC full replacement下对downstream指标有≥1 gen的时序领先性\\\", \\\"model_name\\\": \\\"EleutherAI/pythia-410m\\\", \\\"data_path\\\": \\\"/root/autodl-tmp/distrib_canary_collapse/data/wikitext103_5k\\\", \\\"data_count\\\": 5000, \\\"seed\\\": 44, \\\"server\\\": \\\"westd-19828\\\", \\\"gpu\\\": \\\"cuda:0\\\", \\\"synthetic_ratio\\\": 1, \\\"num_generations\\\": 10, \\\"steps_per_gen\\\": 5000, \\\"n_prompts\\\": 5000, \\\"command\\\": \\\"PYTHONUNBUFFERED=1 CUDA_VISIBLE_DEVICES=0 python -u iterative_train.py --seed 44 --data_dir data/wikitext103_5k --steps_per_gen 5000 --num_generations 10 --output_dir results/mvp/rep_44\\\", \\\"pid\\\": \\\"30672\\\", \\\"log_path\\\": \\\"~/runs/distrib_canary_collapse/mvp_v4_rep44.log\\\"}, \\\"reproduce\\\": {\\\"finished_at\\\": \\\"2026-05-14T17:56:00.578Z\\\"}, \\\"failure_reason\\\": \\\"\\\", \\\"conclusion\\\": \\\"success\\\", \\\"completed_at\\\": \\\"2026-05-14T17:56:00.717Z\\\", \\\"extra\\\": {\\\"hook_events\\\": [{\\\"event\\\": \\\"on_failed\\\", \\\"action\\\": \\\"agent\\\", \\\"ts\\\": \\\"2026-05-14T17:56:03.546926+00:00\\\"}]}, \\\"metrics_summary\\\": {\\\"gen0_ppl\\\": 26.9, \\\"gen10_ppl\\\": 1033.16, \\\"gen0_entropy\\\": 3.234, \\\"gen10_entropy\\\": 1.2205, \\\"gen0_ece\\\": 0.011, \\\"gen10_ece\\\": 0.424}, \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/distrib_canary_collapse/results/mvp/rep_44/gen_10/checkpoint\\\", \\\"wall_clock_seconds\\\": 15134, \\\"gpu_hours\\\": 4.2, \\\"metrics\\\": {\\\"gen0_token_entropy\\\": 3.234195, \\\"gen0_ece\\\": 0.010805, \\\"gen0_perplexity\\\": 26.948959, \\\"gen0_distinct_1\\\": 0.098088, \\\"gen0_distinct_2\\\": 0.513235, \\\"gen0_distinct_3\\\": 0.805767, \\\"gen10_token_entropy\\\": 1.22049, \\\"gen10_ece\\\": 0.42369, \\\"gen10_perplexity\\\": 1033.16, \\\"gen10_distinct_1\\\": 0.073102, \\\"gen10_distinct_2\\\": 0.363737, \\\"gen10_distinct_3\\\": 0.607502, \\\"token_entropy_drift_pct\\\": -62.2629, \\\"ece_drift_pct\\\": 3821.2402, \\\"perplexity_drift_pct\\\": 3733.7659, \\\"distinct_1_drift_pct\\\": -25.473, \\\"distinct_2_drift_pct\\\": -29.1286, \\\"distinct_3_drift_pct\\\": -24.6057}}, \\\"mvp_v4_rep43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-14T07:48:50.161Z\\\", \\\"updated_at\\\": \\\"2026-05-15T21:29:49.565Z\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"cd /root/autodl-tmp/distrib_canary_collapse && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_HUB_DISABLE_XET=1 && export HF_ENDPOINT=https://hf-mirror.com && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && PYTHONUNBUFFERED=1 python -u iterative_train.py --seed 43 --data_dir data/wikitext103_5k --steps_per_gen 5000 --num_generations 10 --output_dir results/mvp/rep_43\\\\\\\"\\\", \\\"server\\\": \\\"westd-19828\\\", \\\"gpu\\\": [\\\"cuda:1\\\"], \\\"pid\\\": \\\"13758\\\", \\\"log_path\\\": \\\"~/runs/distrib_canary_collapse/mvp_v4_rep43.log\\\", \\\"submitted_at\\\": \\\"2026-05-14T07:51:36.759Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/distrib_canary_collapse/results/mvp/rep_43/gen_10/checkpoint\\\", \\\"metrics_summary\\\": {\\\"gen0_ppl\\\": 26.9, \\\"gen10_ppl\\\": 1014.7, \\\"gen0_entropy\\\": 3.234, \\\"gen10_entropy\\\": 1.26, \\\"gen0_ece\\\": 0.011, \\\"gen10_ece\\\": 0.42}, \\\"wall_clock_seconds\\\": 20897.7, \\\"gpu_hours\\\": 5.8}, \\\"conclusion\\\": \\\"success\\\", \\\"completed_at\\\": \\\"2026-05-14T13:39:54.495Z\\\", \\\"metrics\\\": {\\\"gen0_token_entropy\\\": 3.234195, \\\"gen0_ece\\\": 0.010805, \\\"gen0_perplexity\\\": 26.948959, \\\"gen0_distinct_1\\\": 0.098334, \\\"gen0_distinct_2\\\": 0.513178, \\\"gen0_distinct_3\\\": 0.805669, \\\"gen10_token_entropy\\\": 1.25961, \\\"gen10_ece\\\": 0.41951, \\\"gen10_perplexity\\\": 1014.66, \\\"gen10_distinct_1\\\": 0.070383, \\\"gen10_distinct_2\\\": 0.329651, \\\"gen10_distinct_3\\\": 0.539571, \\\"token_entropy_drift_pct\\\": -61.0534, \\\"ece_drift_pct\\\": 3782.5544, \\\"perplexity_drift_pct\\\": 3665.1176, \\\"distinct_1_drift_pct\\\": -28.4246, \\\"distinct_2_drift_pct\\\": -35.7628, \\\"distinct_3_drift_pct\\\": -33.0282}}, \\\"mvp_v4_rep42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-14T07:29:48.857Z\\\", \\\"updated_at\\\": \\\"2026-05-15T21:29:47.171Z\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"cd /root/autodl-tmp/distrib_canary_collapse && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_HUB_DISABLE_XET=1 && export HF_ENDPOINT=https://hf-mirror.com && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && PYTHONUNBUFFERED=1 python -u iterative_train.py --seed 42 --data_dir data/wikitext103_5k --steps_per_gen 5000 --num_generations 10 --output_dir results/mvp/rep_42\\\\\\\"\\\", \\\"server\\\": \\\"westd-19828\\\", \\\"gpu\\\": [\\\"cuda:0\\\"], \\\"pid\\\": \\\"13678\\\", \\\"log_path\\\": \\\"~/runs/distrib_canary_collapse/mvp_v4_rep42.log\\\", \\\"submitted_at\\\": \\\"2026-05-14T07:51:34.806Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/distrib_canary_collapse/results/mvp/rep_42/gen_10/checkpoint\\\", \\\"metrics_summary\\\": {\\\"gen0_ppl\\\": 26.9, \\\"gen10_ppl\\\": 1003.7, \\\"gen0_entropy\\\": 3.234, \\\"gen10_entropy\\\": 1.276, \\\"gen0_ece\\\": 0.011, \\\"gen10_ece\\\": 0.417}, \\\"wall_clock_seconds\\\": 20898.3, \\\"gpu_hours\\\": 5.81}, \\\"conclusion\\\": \\\"success\\\", \\\"completed_at\\\": \\\"2026-05-14T13:39:53.073Z\\\", \\\"metrics\\\": {\\\"gen0_token_entropy\\\": 3.234195, \\\"gen0_ece\\\": 0.010805, \\\"gen0_perplexity\\\": 26.948959, \\\"gen0_distinct_1\\\": 0.098216, \\\"gen0_distinct_2\\\": 0.517803, \\\"gen0_distinct_3\\\": 0.812728, \\\"gen10_token_entropy\\\": 1.27592, \\\"gen10_ece\\\": 0.41734, \\\"gen10_perplexity\\\": 1003.73, \\\"gen10_distinct_1\\\": 0.070383, \\\"gen10_distinct_2\\\": 0.335471, \\\"gen10_distinct_3\\\": 0.555579, \\\"token_entropy_drift_pct\\\": -60.5491, \\\"ece_drift_pct\\\": 3762.4711, \\\"perplexity_drift_pct\\\": 3624.5595, \\\"distinct_1_drift_pct\\\": -28.3386, \\\"distinct_2_drift_pct\\\": -35.2126, \\\"distinct_3_drift_pct\\\": -31.6402}}, \\\"alpha_sweep_a025_s43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-15T06:58:43.090Z\\\", \\\"updated_at\\\": \\\"2026-05-15T17:39:43.623Z\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"cd /root/autodl-tmp/distrib_canary_collapse && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_HUB_DISABLE_XET=1 && export HF_ENDPOINT=https://hf-mirror.com && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && PYTHONUNBUFFERED=1 python -u iterative_train.py --seed 43 --data_dir data/wikitext103_5k --steps_per_gen 5000 --num_generations 10 --synthetic_ratio 0.25 --output_dir results/alpha_sweep/a025_s43\\\\\\\"\\\", \\\"server\\\": \\\"westd-19828\\\", \\\"gpu\\\": [\\\"cuda:1\\\"], \\\"pid\\\": \\\"121635\\\", \\\"log_path\\\": \\\"~/runs/distrib_canary_collapse/alpha_sweep_a025_s43.log\\\", \\\"submitted_at\\\": \\\"2026-05-15T13:16:31.189Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"wall_clock_seconds\\\": 15792.4, \\\"gpu_hours\\\": 4.39}, \\\"server\\\": \\\"westd-19828\\\", \\\"gpu\\\": \\\"cuda:1\\\", \\\"pid\\\": \\\"121635\\\", \\\"log_path\\\": \\\"~/runs/distrib_canary_collapse/alpha_sweep_a025_s43.log\\\", \\\"reproduce\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"cd /root/autodl-tmp/distrib_canary_collapse && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_HUB_DISABLE_XET=1 && export HF_ENDPOINT=https://hf-mirror.com && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && PYTHONUNBUFFERED=1 python -u iterative_train.py --seed 43 --data_dir data/wikitext103_5k --steps_per_gen 5000 --num_generations 10 --synthetic_ratio 0.25 --output_dir results/alpha_sweep/a025_s43\\\\\\\"\\\", \\\"finished_at\\\": \\\"2026-05-15T17:36:20.945Z\\\"}, \\\"metrics\\\": {\\\"gen0\\\": {\\\"token_entropy\\\": 3.2342, \\\"ece\\\": 0.0108, \\\"perplexity\\\": 26.949, \\\"distinct_1\\\": 0.09833, \\\"distinct_2\\\": 0.5132, \\\"distinct_3\\\": 0.8057, \\\"effective_rank\\\": 46.61, \\\"mauve\\\": 0.03351}, \\\"gen10\\\": {\\\"token_entropy\\\": 3.0723, \\\"ece\\\": 0.02146, \\\"perplexity\\\": 21.899, \\\"distinct_1\\\": 0.05849, \\\"distinct_2\\\": 0.2236, \\\"distinct_3\\\": 0.333, \\\"effective_rank\\\": 45.37, \\\"mauve\\\": 0.01871}, \\\"drift_pct\\\": {\\\"token_entropy\\\": -5, \\\"ece\\\": 98.6, \\\"perplexity\\\": -18.7, \\\"distinct_1\\\": -40.5, \\\"distinct_2\\\": -56.4, \\\"distinct_3\\\": -58.7, \\\"effective_rank\\\": -2.7, \\\"mauve\\\": -44.2}}, \\\"extra\\\": {\\\"hook_events\\\": [{\\\"event\\\": \\\"on_complete\\\", \\\"action\\\": \\\"agent\\\", \\\"ts\\\": \\\"2026-05-15T17:36:22.072334+00:00\\\"}]}, \\\"conclusion\\\": \\\"success\\\", \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a025_s43/gen_10/checkpoint\\\", \\\"completed_at\\\": \\\"2026-05-15T17:39:43.624Z\\\"}, \\\"alpha_sweep_a075_s42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-14T21:52:17.315Z\\\", \\\"updated_at\\\": \\\"2026-05-15T13:29:46.421Z\\\", \\\"spec\\\": {\\\"hypothesis\\\": \\\"α=0.75 high contamination: critical boundary point for Granger-causal detectability — determines Claim 1 scope (α≥0.75 vs α=1.0 only)\\\", \\\"seed\\\": 42, \\\"model_name\\\": \\\"EleutherAI/pythia-410m\\\", \\\"data_path\\\": \\\"data/wikitext103_5k\\\", \\\"data_count\\\": 5000, \\\"synthetic_ratio\\\": 0.75, \\\"num_generations\\\": 10, \\\"steps_per_gen\\\": 5000}, \\\"server\\\": \\\"westd-19828\\\", \\\"gpu\\\": \\\"cuda:1\\\", \\\"account\\\": \\\"root\\\", \\\"reproduce\\\": {\\\"server\\\": \\\"westd-19828\\\", \\\"gpu\\\": \\\"cuda:1\\\", \\\"started_at\\\": \\\"2026-05-15T05:44:46.271Z\\\", \\\"command\\\": \\\"bash -c \\\\\\\"cd /root/autodl-tmp/distrib_canary_collapse && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_HUB_DISABLE_XET=1 && export HF_ENDPOINT=https://hf-mirror.com && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && PYTHONUNBUFFERED=1 python -u iterative_train.py --seed 42 --data_dir data/wikitext103_5k --steps_per_gen 5000 --num_generations 10 --synthetic_ratio 0.75 --output_dir results/alpha_sweep/a075_s42\\\\\\\"\\\", \\\"finished_at\\\": \\\"2026-05-15T13:13:06.477Z\\\", \\\"training_hours\\\": 7.47}, \\\"pid\\\": \\\"89753\\\", \\\"log_path\\\": \\\"results/analysis/cross_alpha_v6_report.md\\\", \\\"metrics\\\": {\\\"progress\\\": \\\"11/11 gen (complete)\\\", \\\"gen0_token_entropy\\\": 3.234, \\\"gen10_token_entropy\\\": 2.337, \\\"gen0_ece\\\": 0.0108, \\\"gen10_ece\\\": 0.2063, \\\"gen0_perplexity\\\": 26.95, \\\"gen10_perplexity\\\": 76.03, \\\"gen0_distinct_1\\\": 0.0982, \\\"gen10_distinct_1\\\": 0.0661, \\\"gen0_distinct_2\\\": 0.5178, \\\"gen10_distinct_2\\\": 0.3037, \\\"gen0_distinct_3\\\": 0.8127, \\\"gen10_distinct_3\\\": 0.5011, \\\"token_entropy_drift_pct\\\": -27.7, \\\"ece_drift_pct\\\": 1809.5, \\\"perplexity_drift_pct\\\": 182.1, \\\"distinct_1_drift_pct\\\": -32.7, \\\"distinct_2_drift_pct\\\": -41.3, \\\"distinct_3_drift_pct\\\": -38.4, \\\"granger_ece_to_d1_p_fdr\\\": 0.046, \\\"granger_ece_to_d2_p_fdr\\\": 0.046, \\\"granger_entropy_to_d2_p_fdr\\\": 0.048, \\\"granger_entropy_to_d1_p_fdr\\\": 0.054, \\\"granger_fdr_sig_count\\\": \\\"3/8\\\", \\\"consensus_robust_pairs\\\": \\\"11/16\\\", \\\"xcorr_entropy_d1_lag\\\": 2, \\\"xcorr_entropy_d1_r\\\": 0.973}, \\\"extra\\\": {\\\"hook_events\\\": [{\\\"event\\\": \\\"on_complete\\\", \\\"action\\\": \\\"agent\\\", \\\"ts\\\": \\\"2026-05-15T13:13:07.582542+00:00\\\"}]}, \\\"conclusion\\\": \\\"success\\\", \\\"checkpoint_path\\\": \\\"results/alpha_sweep/a075_s42/\\\", \\\"completed_at\\\": \\\"2026-05-15T13:29:46.421Z\\\"}, \\\"alpha_sweep_a050_s42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-14T21:52:15.427Z\\\", \\\"updated_at\\\": \\\"2026-05-15T13:17:48.134Z\\\", \\\"spec\\\": {\\\"hypothesis\\\": \\\"α=0.50 moderate contamination: test canary→diversity lead at mid-range synthetic ratio, key data point for non-monotonic dose-response\\\", \\\"seed\\\": 42, \\\"model_name\\\": \\\"EleutherAI/pythia-410m\\\", \\\"data_path\\\": \\\"data/wikitext103_5k\\\", \\\"data_count\\\": 5000, \\\"synthetic_ratio\\\": 0.5, \\\"num_generations\\\": 10, \\\"steps_per_gen\\\": 5000}, \\\"server\\\": \\\"westd-19828\\\", \\\"gpu\\\": \\\"cuda:1\\\", \\\"account\\\": \\\"root\\\", \\\"reproduce\\\": {\\\"server\\\": \\\"westd-19828\\\", \\\"gpu\\\": \\\"cuda:1\\\", \\\"started_at\\\": \\\"2026-05-15T01:15:14.747Z\\\", \\\"command\\\": \\\"bash -c \\\\\\\"cd /root/autodl-tmp/distrib_canary_collapse && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_HUB_DISABLE_XET=1 && export HF_ENDPOINT=https://hf-mirror.com && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && PYTHONUNBUFFERED=1 python -u iterative_train.py --seed 42 --data_dir data/wikitext103_5k --steps_per_gen 5000 --num_generations 10 --synthetic_ratio 0.50 --output_dir results/alpha_sweep/a050_s42\\\\\\\"\\\", \\\"finished_at\\\": \\\"2026-05-15T05:42:25.788Z\\\", \\\"training_hours\\\": 4.45}, \\\"pid\\\": \\\"73737\\\", \\\"log_path\\\": \\\"~/runs/distrib_canary_collapse/alpha_sweep_a050_s42.log\\\", \\\"metrics\\\": {\\\"progress\\\": \\\"11/11 gen (complete)\\\", \\\"gen0_token_entropy\\\": 3.234, \\\"gen10_token_entropy\\\": 2.632, \\\"gen0_ece\\\": 0.011, \\\"gen10_ece\\\": 0.102, \\\"gen0_perplexity\\\": 26.95, \\\"gen10_perplexity\\\": 32.64, \\\"gen0_distinct_1\\\": 0.098, \\\"gen10_distinct_1\\\": 0.062, \\\"gen0_distinct_2\\\": 0.518, \\\"gen10_distinct_2\\\": 0.251, \\\"gen0_distinct_3\\\": 0.813, \\\"gen10_distinct_3\\\": 0.387, \\\"token_entropy_drift_pct\\\": -18.6, \\\"ece_drift_pct\\\": 842.8, \\\"perplexity_drift_pct\\\": 21.1, \\\"distinct_1_drift_pct\\\": -37.3, \\\"distinct_2_drift_pct\\\": -51.5, \\\"distinct_3_drift_pct\\\": -52.4, \\\"granger_entropy_to_d1_p_raw\\\": 0.095, \\\"granger_entropy_to_d2_p_raw\\\": 0.097, \\\"granger_ece_to_d1_p_raw\\\": 0.019, \\\"granger_ece_to_d2_p_raw\\\": 0.039, \\\"granger_fdr_note\\\": \\\"4 tests within alpha=0.50; BH FDR threshold rank1=0.0125, rank2=0.025 → 0/4 FDR-sig at q=0.05. Raw p pattern (ECE < entropy) is qualitative signal only.\\\", \\\"d024_non_monotonic\\\": true, \\\"d024_ece_vs_entropy_note\\\": \\\"ECE raw p < entropy raw p at α=0.50 (0.019 vs 0.095 at 5000 perms), 0/4 FDR-sig; regime switch hypothesis pending α=0.75 confirmation\\\"}, \\\"extra\\\": {\\\"hook_events\\\": [{\\\"event\\\": \\\"on_complete\\\", \\\"action\\\": \\\"agent\\\", \\\"ts\\\": \\\"2026-05-15T05:42:26.715028+00:00\\\"}]}, \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a050_s42/gen_10/checkpoint\\\", \\\"conclusion\\\": \\\"success\\\", \\\"completed_at\\\": \\\"2026-05-15T05:46:48.692Z\\\"}, \\\"plan_006_s42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-14T23:31:35.454Z\\\", \\\"updated_at\\\": \\\"2026-05-15T12:17:14.093Z\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"cd /root/autodl-tmp/distrib_canary_collapse && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_HUB_DISABLE_XET=1 && export HF_ENDPOINT=https://hf-mirror.com && PYTHONUNBUFFERED=1 python -u iterative_train.py --data_dir data/wikitext103 --output_dir results/extended_20gen/s42 --seed 42 --synthetic_ratio 1.0 --num_generations 20 --steps_per_gen 10000\\\\\\\"\\\", \\\"server\\\": \\\"westd-19828\\\", \\\"gpu\\\": [\\\"cuda:0\\\"], \\\"pid\\\": \\\"68368\\\", \\\"log_path\\\": \\\"~/runs/distrib_canary_collapse/plan_006_s42.log\\\", \\\"submitted_at\\\": \\\"2026-05-14T23:41:30.666Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"wall_clock_seconds\\\": 43212.6, \\\"gpu_hours\\\": 12.0}, \\\"server\\\": \\\"westd-19828\\\", \\\"gpu\\\": \\\"cuda:0\\\", \\\"account\\\": \\\"root\\\", \\\"reproduce\\\": {\\\"server\\\": \\\"westd-19828\\\", \\\"gpu\\\": \\\"cuda:0\\\", \\\"started_at\\\": \\\"2026-05-14T23:41:29.125Z\\\", \\\"command\\\": \\\"bash -c \\\\\\\"cd /root/autodl-tmp/distrib_canary_collapse && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_HUB_DISABLE_XET=1 && export HF_ENDPOINT=https://hf-mirror.com && PYTHONUNBUFFERED=1 python -u iterative_train.py --data_dir data/wikitext103 --output_dir results/extended_20gen/s42 --seed 42 --synthetic_ratio 1.0 --num_generations 20 --steps_per_gen 10000\\\\\\\"\\\", \\\"finished_at\\\": \\\"2026-05-15T11:41:42.336Z\\\", \\\"training_hours\\\": 12.0}, \\\"pid\\\": \\\"68368\\\", \\\"log_path\\\": \\\"~/runs/distrib_canary_collapse/plan_006_s42.log\\\", \\\"metrics\\\": {\\\"progress\\\": \\\"18/20 gen (gen_0-17 complete, gen_18-20 timeout)\\\", \\\"gen0_token_entropy\\\": 3.2342, \\\"gen17_token_entropy\\\": 1.1819, \\\"gen0_ece\\\": 0.0108, \\\"gen17_ece\\\": 0.4454, \\\"gen0_perplexity\\\": 26.95, \\\"gen17_perplexity\\\": 3367.66, \\\"gen0_distinct_1\\\": 0.0982, \\\"gen17_distinct_1\\\": 0.0756, \\\"gen0_distinct_2\\\": 0.5178, \\\"gen17_distinct_2\\\": 0.3617, \\\"gen0_distinct_3\\\": 0.8127, \\\"gen17_distinct_3\\\": 0.5865, \\\"token_entropy_drift_pct_gen0_17\\\": -63.4, \\\"distinct_1_drift_pct_gen0_17\\\": -23, \\\"distinct_2_drift_pct_gen0_17\\\": -30.1, \\\"distinct_3_drift_pct_gen0_17\\\": -27.8, \\\"ece_drift_pct_gen0_17\\\": 4024, \\\"ppl_drift_pct_gen0_17\\\": 12395, \\\"phase1_rapid_collapse\\\": \\\"gen0-5\\\", \\\"phase2_apparent_plateau\\\": \\\"gen5-12\\\", \\\"phase3_secondary_decline\\\": \\\"gen13-17\\\", \\\"phase3_d2_decline_pct\\\": -5.8, \\\"phase3_d3_decline_pct\\\": -6.9, \\\"diversity_saturated_at_gen\\\": 5, \\\"diversity_secondary_decline_at_gen\\\": 13, \\\"perplexity_saturated\\\": false}, \\\"failure_reason\\\": \\\"EXIT_CODE=124 (timeout — exceeded timeout_hours)\\\", \\\"conclusion\\\": \\\"failed\\\", \\\"completed_at\\\": \\\"2026-05-15T11:41:43.235Z\\\", \\\"extra\\\": {\\\"hook_events\\\": [{\\\"event\\\": \\\"on_failed\\\", \\\"action\\\": \\\"agent\\\", \\\"ts\\\": \\\"2026-05-15T11:41:44.300301+00:00\\\"}]}, \\\"notes\\\": \\\"gen_0-17 complete (T=18). 三相 collapse: Phase1 急速崩塌 gen0-5 (d1 -20.6%, entropy -63.8%), Phase2 表观稳态 gen5-12 (diversity <0.3% 变化, perplexity 仍+167%), Phase3 二次衰退 gen13-17 (d2 -5.8%, d3 -6.9%). Perplexity 未饱和 (26.95→3367.66, +12395%). T=18 vs T=10: 新增 diversity 二次衰退在 T=10 window 不可见. TY power 预估 ~0.28-0.41 (vs T=10 的 0.05-0.21).\\\"}, \\\"plan_006_s42_resume\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-15T11:55:26.236Z\\\", \\\"updated_at\\\": \\\"2026-05-15T12:10:54.859Z\\\", \\\"spec\\\": {\\\"command\\\": \\\"python -u resume_plan006_s42.py\\\", \\\"server\\\": \\\"westd-19828\\\", \\\"gpu\\\": [\\\"cuda:0\\\"], \\\"pid\\\": \\\"114844\\\", \\\"log_path\\\": \\\"~/runs/distrib_canary_collapse/plan_006_s42_resume.log\\\", \\\"submitted_at\\\": \\\"2026-05-15T11:55:31.984Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"hypothesis\\\": \\\"恢复 plan_006_s42 从 gen_17，完成 gen_18-20 + all_metrics（α=1.0, 20gen, s42）\\\", \\\"seed\\\": 42, \\\"model_name\\\": \\\"EleutherAI/pythia-410m\\\", \\\"data_path\\\": \\\"data/wikitext103\\\", \\\"data_count\\\": 0, \\\"checkpoint_path\\\": \\\"N/A\\\", \\\"notes\\\": \\\"D034 决定不恢复，T=18 数据已足够（超出 T=15 目标）。plan_006_s42 gen_0-17 数据可用。\\\", \\\"wall_clock_seconds\\\": 921.5, \\\"gpu_hours\\\": 0.26}, \\\"conclusion\\\": \\\"killed\\\", \\\"completed_at\\\": \\\"2026-05-15T12:10:53.514Z\\\", \\\"notes\\\": \\\"D034 决定不恢复。T=18 数据已足够（超出 T=15 目标）。原 plan_006_s42 gen_0-17 数据可用于 power analysis + supplementary。\\\"}, \\\"gen_wiki_gpt2m_a100_s42_v2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-15T12:02:06.478Z\\\", \\\"updated_at\\\": \\\"2026-05-15T12:04:50.741Z\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && mkdir -p results/gen_wiki_gpt2m_a100_s42 && HF_HOME=/root/autodl-tmp/.hf_cache TRANSFORMERS_OFFLINE=1 HF_HUB_DISABLE_XET=1 PYTHONUNBUFFERED=1 python -u iterative_train.py --model_name /root/autodl-tmp/models/gpt2-medium --data_dir data/wikitext103_5k --synthetic_ratio 1.0 --num_generations 10 --steps_per_gen 5000 --batch_size 32 --seed 42 --output_dir results/gen_wiki_gpt2m_a100_s42\\\\\\\"\\\", \\\"server\\\": \\\"westd-19828\\\", \\\"gpu\\\": [\\\"cuda:0\\\"], \\\"pid\\\": \\\"116204\\\", \\\"log_path\\\": \\\"~/runs/distrib_canary_collapse/gen_wiki_gpt2m_a100_s42_v2.log\\\", \\\"submitted_at\\\": \\\"2026-05-15T12:02:14.440Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"wall_clock_seconds\\\": 18.0, \\\"gpu_hours\\\": 0.01}, \\\"server\\\": \\\"westd-19828\\\", \\\"gpu\\\": \\\"cuda:0\\\", \\\"account\\\": \\\"root\\\", \\\"reproduce\\\": {\\\"server\\\": \\\"westd-19828\\\", \\\"gpu\\\": \\\"cuda:0\\\", \\\"started_at\\\": \\\"2026-05-15T12:02:13.557Z\\\", \\\"command\\\": \\\"bash -c \\\\\\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && mkdir -p results/gen_wiki_gpt2m_a100_s42 && HF_HOME=/root/autodl-tmp/.hf_cache TRANSFORMERS_OFFLINE=1 HF_HUB_DISABLE_XET=1 PYTHONUNBUFFERED=1 python -u iterative_train.py --model_name /root/autodl-tmp/models/gpt2-medium --data_dir data/wikitext103_5k --synthetic_ratio 1.0 --num_generations 10 --steps_per_gen 5000 --batch_size 32 --seed 42 --output_dir results/gen_wiki_gpt2m_a100_s42\\\\\\\"\\\", \\\"finished_at\\\": \\\"2026-05-15T12:02:31.643Z\\\", \\\"training_hours\\\": 0.01}, \\\"pid\\\": \\\"116204\\\", \\\"log_path\\\": \\\"~/runs/distrib_canary_collapse/gen_wiki_gpt2m_a100_s42_v2.log\\\", \\\"failure_reason\\\": \\\"EXIT_CODE=1 (generic error — check log tail)\\\", \\\"conclusion\\\": \\\"killed\\\", \\\"completed_at\\\": \\\"2026-05-15T12:02:32.472Z\\\", \\\"extra\\\": {\\\"hook_events\\\": [{\\\"event\\\": \\\"on_failed\\\", \\\"action\\\": \\\"agent\\\", \\\"ts\\\": \\\"2026-05-15T12:02:33.931882+00:00\\\"}]}}, \\\"gen_wiki_gpt2m_a100_s42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-15T10:35:18.700Z\\\", \\\"updated_at\\\": \\\"2026-05-15T12:01:58.523Z\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && mkdir -p results/gen_wiki_gpt2m_a100_s42 && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_DISABLE_XET=1 PYTHONUNBUFFERED=1 python -u iterative_train.py --model_name gpt2-medium --data_dir data/wikitext103_5k --synthetic_ratio 1.0 --num_generations 10 --steps_per_gen 5000 --batch_size 32 --seed 42 --output_dir results/gen_wiki_gpt2m_a100_s42\\\\\\\"\\\", \\\"server\\\": \\\"westd-19828\\\", \\\"gpu\\\": [\\\"cuda:0\\\"], \\\"pid\\\": \\\"115532\\\", \\\"log_path\\\": \\\"~/runs/distrib_canary_collapse/gen_wiki_gpt2m_a100_s42.log\\\", \\\"submitted_at\\\": \\\"2026-05-15T11:57:48.767Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"wall_clock_seconds\\\": 249.8, \\\"gpu_hours\\\": 0.07}, \\\"server\\\": \\\"westd-19828\\\", \\\"gpu\\\": \\\"cuda:0\\\", \\\"account\\\": \\\"root\\\", \\\"reproduce\\\": {\\\"server\\\": \\\"westd-19828\\\", \\\"gpu\\\": \\\"cuda:0\\\", \\\"started_at\\\": \\\"2026-05-15T11:57:47.340Z\\\", \\\"command\\\": \\\"bash -c \\\\\\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && mkdir -p results/gen_wiki_gpt2m_a100_s42 && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_DISABLE_XET=1 PYTHONUNBUFFERED=1 python -u iterative_train.py --model_name gpt2-medium --data_dir data/wikitext103_5k --synthetic_ratio 1.0 --num_generations 10 --steps_per_gen 5000 --batch_size 32 --seed 42 --output_dir results/gen_wiki_gpt2m_a100_s42\\\\\\\"\\\"}, \\\"pid\\\": \\\"115532\\\", \\\"log_path\\\": \\\"~/runs/distrib_canary_collapse/gen_wiki_gpt2m_a100_s42.log\\\", \\\"conclusion\\\": \\\"killed\\\", \\\"completed_at\\\": \\\"2026-05-15T12:01:58.523Z\\\"}, \\\"method_ablation_phase2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-15T08:58:35.270Z\\\", \\\"updated_at\\\": \\\"2026-05-15T11:07:42.688Z\\\", \\\"spec\\\": {\\\"hypothesis\\\": \\\"Method sensitivity is compounded by regime dependence — method x alpha interaction is the headline Claim 3 evidence\\\", \\\"command\\\": \\\"python method_ablation_phase2.py\\\", \\\"server\\\": \\\"westd-19828\\\", \\\"data_path\\\": \\\"results/alpha_sweep + results/mvp\\\", \\\"data_count\\\": 56, \\\"model_name\\\": \\\"N/A (analysis)\\\", \\\"seed\\\": \\\"42,43,44,45\\\", \\\"checkpoint_path\\\": \\\"N/A\\\", \\\"log_path\\\": \\\"results/method_ablation_phase2_panel.json\\\"}, \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"n_panel_rows\\\": 56, \\\"n_alphas\\\": 4, \\\"alphas\\\": [0, 0.25, 0.5, 1], \\\"naive_sig_rate_overall\\\": 1, \\\"perm_granger_sig_rate_a000_raw\\\": 0, \\\"perm_granger_sig_rate_a000_fdr\\\": 0, \\\"perm_granger_sig_rate_a025_raw\\\": 0.25, \\\"perm_granger_sig_rate_a025_fdr\\\": 0, \\\"perm_granger_sig_rate_a050_raw\\\": 0.25, \\\"perm_granger_sig_rate_a050_fdr\\\": 0, \\\"perm_granger_sig_rate_a100_raw\\\": 0.75, \\\"perm_granger_sig_rate_a100_fdr\\\": 0.75, \\\"TY_sig_rate_a000_raw\\\": 0, \\\"TY_sig_rate_a000_fdr\\\": 0, \\\"TY_sig_rate_a025_raw\\\": 0.625, \\\"TY_sig_rate_a025_fdr\\\": 0.375, \\\"TY_sig_rate_a050_raw\\\": 0, \\\"TY_sig_rate_a050_fdr\\\": 0, \\\"TY_sig_rate_a100_raw\\\": 0.5938, \\\"TY_sig_rate_a100_fdr\\\": 0.5938, \\\"diff_sig_rate_a000_raw\\\": 0.5, \\\"diff_sig_rate_a000_fdr\\\": 0.375, \\\"mean_inter_method_kappa\\\": 0.185, \\\"naive_vs_perm_granger_flip_rate\\\": 0.5, \\\"naive_vs_TY_flip_rate\\\": 0.57, \\\"fdr_flips_perm_granger\\\": 4, \\\"pair_verdict_a100_perm_granger\\\": \\\"6/8\\\", \\\"pair_verdict_a100_TY\\\": \\\"6/8\\\", \\\"entropy_to_diversity_a100_all_5methods_sig\\\": true, \\\"fdr_correction\\\": \\\"BH q=0.05\\\"}, \\\"completed_at\\\": \\\"2026-05-15T08:58:54.741Z\\\"}, \\\"alpha_sweep_a025_s42_v3\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-14T21:04:05.726Z\\\", \\\"updated_at\\\": \\\"2026-05-15T05:13:22.207Z\\\", \\\"spec\\\": {\\\"hypothesis\\\": \\\"α=0.25 低污染: 测试 canary→diversity lead 在温和 collapse 下是否保持\\\", \\\"model_name\\\": \\\"EleutherAI/pythia-410m\\\", \\\"data_path\\\": \\\"/root/autodl-tmp/distrib_canary_collapse/data/wikitext103_5k\\\", \\\"data_count\\\": 5000, \\\"seed\\\": 42, \\\"synthetic_ratio\\\": 0.25, \\\"num_generations\\\": 10, \\\"steps_per_gen\\\": 5000, \\\"parent\\\": \\\"alpha_sweep_a025_s42_v2 (failed, data corruption)\\\", \\\"command\\\": \\\"bash -c \\\\\\\"cd /root/autodl-tmp/distrib_canary_collapse && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_HUB_DISABLE_XET=1 && export HF_ENDPOINT=https://hf-mirror.com && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && PYTHONUNBUFFERED=1 python -u iterative_train.py --seed 42 --data_dir data/wikitext103_5k --steps_per_gen 5000 --num_generations 10 --synthetic_ratio 0.25 --output_dir results/alpha_sweep/a025_s42\\\\\\\"\\\", \\\"server\\\": \\\"westd-19828\\\", \\\"gpu\\\": [\\\"cuda:1\\\"], \\\"pid\\\": \\\"53069\\\", \\\"log_path\\\": \\\"~/runs/distrib_canary_collapse/alpha_sweep_a025_s42_v3.log\\\"}, \\\"reproduce\\\": {\\\"finished_at\\\": \\\"2026-05-15T01:18:42.377Z\\\"}, \\\"extra\\\": {\\\"hook_events\\\": [{\\\"event\\\": \\\"on_complete\\\", \\\"action\\\": \\\"agent\\\", \\\"ts\\\": \\\"2026-05-15T01:18:43.329069+00:00\\\"}]}, \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"gen0_token_entropy\\\": 3.2342, \\\"gen10_token_entropy\\\": 3.1017, \\\"gen0_ece\\\": 0.0108, \\\"gen10_ece\\\": 0.01942, \\\"gen0_perplexity\\\": 26.95, \\\"gen10_perplexity\\\": 22.32, \\\"gen0_distinct_1\\\": 0.0982, \\\"gen10_distinct_1\\\": 0.0586, \\\"gen0_distinct_2\\\": 0.5178, \\\"gen10_distinct_2\\\": 0.2219, \\\"gen0_distinct_3\\\": 0.8127, \\\"gen10_distinct_3\\\": 0.3263, \\\"token_entropy_drift_pct\\\": -4.1, \\\"ece_drift_pct\\\": 79.7, \\\"perplexity_drift_pct\\\": -17.2, \\\"distinct_1_drift_pct\\\": -40.3, \\\"distinct_2_drift_pct\\\": -57.1, \\\"distinct_3_drift_pct\\\": -59.9}, \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a025_s42/gen_10/checkpoint\\\", \\\"completed_at\\\": \\\"2026-05-15T01:26:19.292Z\\\", \\\"notes\\\": \\\"实际磁盘路径为 results/alpha_sweep/a025_s42/（无 v3 后缀）。Registry ID 带 v3 是历史原因，数据已核实无误。\\\"}, \\\"method_ablation_phase1\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-14T23:49:16.519Z\\\", \\\"updated_at\\\": \\\"2026-05-14T23:49:40.162Z\\\", \\\"spec\\\": {\\\"plan_id\\\": \\\"plan_002\\\", \\\"hypothesis\\\": \\\"lead-lag 结论对分析方法高度敏感——naive Pearson 100% SIG vs TY 25% SIG，方法选择改变 75% 的结论\\\", \\\"command\\\": \\\"python method_ablation.py + python permutation_granger.py (差分版)\\\", \\\"server\\\": \\\"westd-19828\\\", \\\"data_path\\\": \\\"results/mvp/rep_{42,43,44,45}/all_metrics.json\\\", \\\"data_count\\\": 4, \\\"model_name\\\": \\\"N/A (analysis on MVP data)\\\", \\\"seed\\\": \\\"42,43,44,45\\\", \\\"checkpoint_path\\\": \\\"N/A\\\", \\\"log_path\\\": \\\"results/mvp/analysis/method_ablation.json\\\"}, \\\"conclusion\\\": \\\"success\\\", \\\"completed_at\\\": \\\"2026-05-14T23:49:37.295Z\\\", \\\"metrics\\\": {\\\"spurious_rate_5method\\\": 0.75, \\\"spurious_rate_4method\\\": 0.625, \\\"naive_sig\\\": \\\"16/16\\\", \\\"differenced_sig\\\": \\\"14/16\\\", \\\"threshold_sig\\\": \\\"9/16\\\", \\\"permutation_granger_sig\\\": \\\"6/16\\\", \\\"ty_sig\\\": \\\"4/16\\\", \\\"ty_power_T10\\\": \\\"0.05-0.20\\\", \\\"bh_fdr_flips\\\": 0}}, \\\"alpha_sweep_a000_s42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-14T19:01:37.470Z\\\", \\\"updated_at\\\": \\\"2026-05-14T23:42:18.748Z\\\", \\\"spec\\\": {\\\"hypothesis\\\": \\\"α=0.0 null control: 纯 real data 再训练无 canary signal，确认 signal 源于合成污染\\\", \\\"model_name\\\": \\\"EleutherAI/pythia-410m\\\", \\\"data_path\\\": \\\"/root/autodl-tmp/distrib_canary_collapse/data/wikitext103_5k\\\", \\\"data_count\\\": 5000, \\\"seed\\\": 42, \\\"synthetic_ratio\\\": 0, \\\"num_generations\\\": 10, \\\"steps_per_gen\\\": 5000, \\\"command\\\": \\\"bash -c \\\\\\\"cd /root/autodl-tmp/distrib_canary_collapse && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_HUB_DISABLE_XET=1 && export HF_ENDPOINT=https://hf-mirror.com && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && PYTHONUNBUFFERED=1 python -u iterative_train.py --seed 42 --data_dir data/wikitext103_5k --steps_per_gen 5000 --num_generations 10 --synthetic_ratio 0.0 --output_dir results/alpha_sweep/a000_s42\\\\\\\"\\\", \\\"server\\\": \\\"westd-19828\\\", \\\"gpu\\\": [\\\"cuda:0\\\"], \\\"pid\\\": \\\"46716\\\", \\\"log_path\\\": \\\"~/runs/distrib_canary_collapse/alpha_sweep_a000_s42.log\\\"}, \\\"reproduce\\\": {\\\"finished_at\\\": \\\"2026-05-14T23:36:35.414Z\\\"}, \\\"extra\\\": {\\\"hook_events\\\": [{\\\"event\\\": \\\"on_complete\\\", \\\"action\\\": \\\"agent\\\", \\\"ts\\\": \\\"2026-05-14T23:36:36.221435+00:00\\\"}]}, \\\"conclusion\\\": \\\"success\\\", \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a000_s42/gen_10/checkpoint\\\", \\\"log_path\\\": \\\"~/runs/distrib_canary_collapse/alpha_sweep_a000_s42.log\\\", \\\"metrics\\\": {\\\"gen0_token_entropy\\\": 3.2342, \\\"gen10_token_entropy\\\": 3.0693, \\\"gen0_ece\\\": 0.0108, \\\"gen10_ece\\\": 0.0164, \\\"gen0_perplexity\\\": 26.95, \\\"gen10_perplexity\\\": 21.11, \\\"gen0_distinct_1\\\": 0.0982, \\\"gen10_distinct_1\\\": 0.0847, \\\"token_entropy_drift_pct\\\": -5.1, \\\"ece_drift_pct\\\": 51.7, \\\"perplexity_drift_pct\\\": -21.7, \\\"distinct_1_drift_pct\\\": -13.8, \\\"distinct_2_drift_pct\\\": -9.8, \\\"distinct_3_drift_pct\\\": -4.5, \\\"gen1_10_perplexity_drift_pct\\\": 9.4, \\\"gen1_10_distinct_1_drift_pct\\\": -13.1, \\\"gen1_10_entropy_drift_pct\\\": 2.6}, \\\"completed_at\\\": \\\"2026-05-14T23:39:04.310Z\\\"}, \\\"plan_009_bootstrap_ty\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-14T21:33:04.665Z\\\", \\\"updated_at\\\": \\\"2026-05-14T21:33:27.106Z\\\", \\\"spec\\\": {\\\"hypothesis\\\": \\\"Monte Carlo 验证 TY Granger 在短时间序列 (T=10,15,20,30) 下的 Type I error 和 statistical power\\\", \\\"command\\\": \\\"python bootstrap_ty_validation.py (N_sim=1000)\\\", \\\"server\\\": \\\"westd-19828\\\", \\\"data_path\\\": \\\"synthetic DGP (AR(1) for H0, VAR(2) for H1)\\\", \\\"data_count\\\": 1000, \\\"model_name\\\": \\\"N/A (statistical simulation)\\\", \\\"seed\\\": \\\"multiple\\\", \\\"log_path\\\": \\\"results/bootstrap_ty_results.json\\\", \\\"checkpoint_path\\\": \\\"N/A\\\"}, \\\"conclusion\\\": \\\"success\\\", \\\"completed_at\\\": \\\"2026-05-14T21:33:24.769Z\\\", \\\"metrics\\\": {\\\"T10_d0_type1\\\": 0.081, \\\"T10_d0_power\\\": 0.205, \\\"T10_d1_type1\\\": 0.047, \\\"T10_d1_power\\\": 0.09, \\\"T10_dadapt_type1\\\": 0.052, \\\"T10_dadapt_power\\\": 0.05, \\\"T20_d0_power\\\": 0.409, \\\"T20_d1_power\\\": 0.172, \\\"T30_d0_power\\\": 0.606, \\\"T30_d1_power\\\": 0.283}}, \\\"mvp_v3_rep43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-14T06:25:42.195Z\\\", \\\"updated_at\\\": \\\"2026-05-14T06:48:01.316Z\\\", \\\"spec\\\": {\\\"command\\\": \\\"python iterative_train.py --seed 43 --output_dir results/mvp/rep_43 --data_dir data/wikitext103_5k --synthetic_ratio 1.0 --num_generations 10 --steps_per_gen 5000\\\", \\\"server\\\": \\\"autodl-rtx6000\\\", \\\"gpu\\\": \\\"cuda:1\\\", \\\"pid\\\": \\\"7987\\\", \\\"log_path\\\": \\\"~/runs/distrib_canary_collapse/mvp_v3_rep43.log\\\", \\\"submitted_at\\\": \\\"2026-05-14T06:26:18.477Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"data_path\\\": \\\"/root/autodl-tmp/distrib_canary_collapse/data/wikitext103_5k\\\", \\\"data_count\\\": 5000, \\\"model_name\\\": \\\"EleutherAI/pythia-410m\\\", \\\"seed\\\": 43, \\\"gpu_model\\\": \\\"RTX PRO 6000 Blackwell 96GB\\\", \\\"tmux_session\\\": \\\"mvp_v3_rep43\\\", \\\"checkpoint_path\\\": \\\"N/A\\\", \\\"failure_reason\\\": \\\"MAUVE FAISS crash: max_samples=500 → p+q=1000 < 1950 required; 无 PYTHONUNBUFFERED 导致日志丢失\\\", \\\"wall_clock_seconds\\\": 1302.8, \\\"gpu_hours\\\": 0.36}, \\\"conclusion\\\": \\\"failed\\\", \\\"completed_at\\\": \\\"2026-05-14T06:48:01.316Z\\\"}, \\\"mvp_v3_rep42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-14T06:25:39.728Z\\\", \\\"updated_at\\\": \\\"2026-05-14T06:47:59.908Z\\\", \\\"spec\\\": {\\\"command\\\": \\\"python iterative_train.py --seed 42 --output_dir results/mvp/rep_42 --data_dir data/wikitext103_5k --synthetic_ratio 1.0 --num_generations 10 --steps_per_gen 5000\\\", \\\"server\\\": \\\"autodl-rtx6000\\\", \\\"gpu\\\": \\\"cuda:0\\\", \\\"pid\\\": \\\"7909\\\", \\\"log_path\\\": \\\"~/runs/distrib_canary_collapse/mvp_v3_rep42.log\\\", \\\"submitted_at\\\": \\\"2026-05-14T06:26:16.939Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"data_path\\\": \\\"/root/autodl-tmp/distrib_canary_collapse/data/wikitext103_5k\\\", \\\"data_count\\\": 5000, \\\"model_name\\\": \\\"EleutherAI/pythia-410m\\\", \\\"seed\\\": 42, \\\"gpu_model\\\": \\\"RTX PRO 6000 Blackwell 96GB\\\", \\\"tmux_session\\\": \\\"mvp_v3_rep42\\\", \\\"checkpoint_path\\\": \\\"N/A\\\", \\\"failure_reason\\\": \\\"MAUVE FAISS crash: max_samples=500 → p+q=1000 < 1950 required; 无 PYTHONUNBUFFERED 导致日志丢失\\\", \\\"wall_clock_seconds\\\": 1303.0, \\\"gpu_hours\\\": 0.36}, \\\"conclusion\\\": \\\"failed\\\", \\\"completed_at\\\": \\\"2026-05-14T06:47:59.908Z\\\"}, \\\"mvp_v2_rep43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-14T05:38:10.434Z\\\", \\\"updated_at\\\": \\\"2026-05-14T06:25:28.345Z\\\", \\\"spec\\\": {\\\"command\\\": \\\"python iterative_train.py --seed 43 --output_dir results/mvp/rep_43 --data_dir data/wikitext103_5k --synthetic_ratio 1.0 --num_generations 10 --steps_per_gen 5000\\\", \\\"server\\\": \\\"autodl-rtx6000\\\", \\\"gpu\\\": \\\"cuda:1\\\", \\\"pid\\\": \\\"5364\\\", \\\"log_path\\\": \\\"~/runs/distrib_canary_collapse/mvp_v2_rep43.log\\\", \\\"submitted_at\\\": \\\"2026-05-14T05:42:39.039Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"data_path\\\": \\\"/root/autodl-tmp/distrib_canary_collapse/data/wikitext103_5k\\\", \\\"data_count\\\": 5000, \\\"model_name\\\": \\\"EleutherAI/pythia-410m\\\", \\\"seed\\\": 43, \\\"gpu_model\\\": \\\"RTX PRO 6000 Blackwell 96GB\\\", \\\"tmux_session\\\": \\\"mvp_v2_rep43\\\", \\\"checkpoint_path\\\": \\\"N/A\\\", \\\"kill_reason\\\": \\\"v1旧进程未死导致输出目录冲突，v2死锁\\\", \\\"wall_clock_seconds\\\": 2569.3, \\\"gpu_hours\\\": 0.71}, \\\"conclusion\\\": \\\"killed\\\", \\\"completed_at\\\": \\\"2026-05-14T06:25:28.345Z\\\"}, \\\"mvp_v2_rep42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-14T05:38:05.054Z\\\", \\\"updated_at\\\": \\\"2026-05-14T06:25:27.286Z\\\", \\\"spec\\\": {\\\"command\\\": \\\"python iterative_train.py --seed 42 --output_dir results/mvp/rep_42 --data_dir data/wikitext103_5k --synthetic_ratio 1.0 --num_generations 10 --steps_per_gen 5000\\\", \\\"server\\\": \\\"autodl-rtx6000\\\", \\\"gpu\\\": \\\"cuda:0\\\", \\\"pid\\\": \\\"5286\\\", \\\"log_path\\\": \\\"~/runs/distrib_canary_collapse/mvp_v2_rep42.log\\\", \\\"submitted_at\\\": \\\"2026-05-14T05:42:37.404Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"data_path\\\": \\\"/root/autodl-tmp/distrib_canary_collapse/data/wikitext103_5k\\\", \\\"data_count\\\": 5000, \\\"model_name\\\": \\\"EleutherAI/pythia-410m\\\", \\\"seed\\\": 42, \\\"gpu_model\\\": \\\"RTX PRO 6000 Blackwell 96GB\\\", \\\"tmux_session\\\": \\\"mvp_v2_rep42\\\", \\\"checkpoint_path\\\": \\\"N/A\\\", \\\"kill_reason\\\": \\\"v1旧进程未死导致输出目录冲突，v2死锁\\\", \\\"wall_clock_seconds\\\": 2569.9, \\\"gpu_hours\\\": 0.71}, \\\"conclusion\\\": \\\"killed\\\", \\\"completed_at\\\": \\\"2026-05-14T06:25:27.286Z\\\"}, \\\"mvp_rep43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-14T05:12:14.237Z\\\", \\\"updated_at\\\": \\\"2026-05-14T05:37:18.575Z\\\", \\\"spec\\\": {\\\"command\\\": \\\"python iterative_train.py --seed 43 --output_dir results/mvp/rep_43 --data_dir data/wikitext103 --synthetic_ratio 1.0 --num_generations 10 --steps_per_gen 10000\\\", \\\"server\\\": \\\"autodl-rtx6000\\\", \\\"gpu\\\": \\\"cuda:1\\\", \\\"pid\\\": \\\"3956\\\", \\\"log_path\\\": \\\"~/runs/distrib_canary_collapse/mvp_rep43.log\\\", \\\"submitted_at\\\": \\\"2026-05-14T05:34:47.702Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"data_path\\\": \\\"/root/autodl-tmp/distrib_canary_collapse/data/wikitext103\\\", \\\"data_count\\\": 716506, \\\"model_name\\\": \\\"EleutherAI/pythia-410m\\\", \\\"seed\\\": 43, \\\"gpu_model\\\": \\\"RTX PRO 6000 Blackwell 96GB\\\", \\\"tmux_session\\\": \\\"mvp_rep43\\\", \\\"checkpoint_path\\\": \\\"N/A\\\", \\\"kill_reason\\\": \\\"参数修复: n_prompts 1000→5000, steps_per_gen 10000→5000\\\", \\\"wall_clock_seconds\\\": 150.9, \\\"gpu_hours\\\": 0.04}, \\\"conclusion\\\": \\\"killed\\\", \\\"completed_at\\\": \\\"2026-05-14T05:37:18.575Z\\\"}, \\\"mvp_rep42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-14T05:12:13.930Z\\\", \\\"updated_at\\\": \\\"2026-05-14T05:37:17.438Z\\\", \\\"spec\\\": {\\\"command\\\": \\\"python iterative_train.py --seed 42 --output_dir results/mvp/rep_42 --data_dir data/wikitext103 --synthetic_ratio 1.0 --num_generations 10 --steps_per_gen 10000\\\", \\\"server\\\": \\\"autodl-rtx6000\\\", \\\"gpu\\\": \\\"cuda:0\\\", \\\"pid\\\": \\\"3878\\\", \\\"log_path\\\": \\\"~/runs/distrib_canary_collapse/mvp_rep42.log\\\", \\\"submitted_at\\\": \\\"2026-05-14T05:34:46.013Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"data_path\\\": \\\"/root/autodl-tmp/distrib_canary_collapse/data/wikitext103\\\", \\\"data_count\\\": 716506, \\\"model_name\\\": \\\"EleutherAI/pythia-410m\\\", \\\"seed\\\": 42, \\\"gpu_model\\\": \\\"RTX PRO 6000 Blackwell 96GB\\\", \\\"tmux_session\\\": \\\"mvp_rep42\\\", \\\"checkpoint_path\\\": \\\"N/A\\\", \\\"kill_reason\\\": \\\"参数修复: n_prompts 1000→5000, steps_per_gen 10000→5000\\\", \\\"wall_clock_seconds\\\": 151.4, \\\"gpu_hours\\\": 0.04}, \\\"conclusion\\\": \\\"killed\\\", \\\"completed_at\\\": \\\"2026-05-14T05:37:17.438Z\\\"}}, \\\"count\\\": 34, \\\"total\\\": 34, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.0843}}\"}",
      "numLines": 1,
      "startLine": 0,
      "totalLines": 1
    }
  },
  "sourceToolAssistantUUID": "82ac2b1a-122b-407f-97da-ea46c6a7db4d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/agent_e1f64cd5",
  "sessionId": "4f6074eb-8665-49ec-9526-07c9eebcea03",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-16T02:25:06.875Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01G9f1S1kpmqyKbZ2oxVuNDH`</summary>

```json
{
  "project": "distrib_canary_collapse",
  "filters": {
    "exp_id": "alpha_sweep_a025_s44"
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
  "parentUuid": "77a22979-7396-4263-8c18-5b02f25c8ec3",
  "isSidechain": false,
  "requestId": "req_011Cb5THuhGWHzBF774MUCUm",
  "type": "assistant",
  "uuid": "8d97e0cc-3d38-42f0-8838-3eaf15abdcd5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/agent_e1f64cd5",
  "sessionId": "4f6074eb-8665-49ec-9526-07c9eebcea03",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01T8BDf1uGF2GNThXn3cBhEv",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5358,
      "cache_read_input_tokens": 38030,
      "output_tokens": 849,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5358,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 849,
          "cache_read_input_tokens": 38030,
          "cache_creation_input_tokens": 5358,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5358
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

_source line 28 · 2026-05-16T02:25:07.010Z_

<details><summary>↩ Tool result · `toolu_01G9f1S1kpmqyKbZ2oxVuNDH`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.1219}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8d97e0cc-3d38-42f0-8838-3eaf15abdcd5",
  "isSidechain": false,
  "promptId": "a304cee9-feed-4fb2-a028-8ae1d93109aa",
  "type": "user",
  "uuid": "cfdef54d-fdbb-4bf4-a8f5-a71c40acbd1f",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {}, \\\"count\\\": 0, \\\"total\\\": 0, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.1219}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.1219}}"
    }
  },
  "sourceToolAssistantUUID": "8d97e0cc-3d38-42f0-8838-3eaf15abdcd5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/agent_e1f64cd5",
  "sessionId": "4f6074eb-8665-49ec-9526-07c9eebcea03",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 29 · 2026-05-16T02:25:07.015Z_

```json
{
  "parentUuid": "cfdef54d-fdbb-4bf4-a8f5-a71c40acbd1f",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "4712cda5-34f2-4eb2-bdb9-87789a11d252",
  "timestamp": "2026-05-16T02:25:07.015Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/agent_e1f64cd5",
  "sessionId": "4f6074eb-8665-49ec-9526-07c9eebcea03",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 30_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[CRON] 实验进程已正常退出，状态已转为 ANALYZING，需要你分析结果并推进到 DONE。 详情: Process exited cleanly, W&B data available  - exp_id: alpha_sweep_a025_s44 - project: distrib_canary_collapse - server: westd-19828 - log_path: ~…",
  "leafUuid": "4712cda5-34f2-4eb2-bdb9-87789a11d252",
  "sessionId": "4f6074eb-8665-49ec-9526-07c9eebcea03"
}
```

---

### Runtime record

_source line 31_

```json
{
  "type": "ai-title",
  "aiTitle": "Analyze experiment results and mark complete",
  "sessionId": "4f6074eb-8665-49ec-9526-07c9eebcea03"
}
```

---

### Assistant

_source line 32 · 2026-05-16T02:25:25.563Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a clear picture of the project state:

1. **alpha_sweep_a025_s44** is in ANALYZING status - needs analysis. This is the D026 multi-seed #3 experiment (seed 44, α=0.25, Pythia-410m, 10 generations, 5000 steps/gen).
2. **gen_wiki_gpt2m_a025_s42** is still RUNNING on cuda:0 (GPT-2m cross-architecture validation).
3. There are 14 successful experiments, with extensive data on α sweep and multi-seed replications.


4. For alpha_sweep_a025_s44, I need to spawn a Worker to SSH into westd-19828, pull the logs, extract the metrics, and benchmark them against the previous seeds - particularly s42 and s43 which showed entropy drift of -4.1%, ece drift of +79.7%, ppl drift of -17.2%, d1 drift of -40.3%, and d2 drift of -57.1%.

The pattern across these experiments is consistent: diversity metrics collapse by 40-60% while entropy and perplexity show only minor drift. I'll have the Worker extract per-generation metrics from the results directory, compute the drift percentages, and compare against the baseline to see if s44 follows the same trend. I should also check the resource-saturation skill since I'll need to report findings to Director.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4712cda5-34f2-4eb2-bdb9-87789a11d252",
  "isSidechain": false,
  "requestId": "req_011Cb5TKbxyddoKSCkRbFCDa",
  "type": "assistant",
  "uuid": "6afade71-863f-44be-880d-7b3db246feef",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/agent_e1f64cd5",
  "sessionId": "4f6074eb-8665-49ec-9526-07c9eebcea03",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0146DRFxsmCt6r1etJtNM34g",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 24932,
      "cache_read_input_tokens": 43388,
      "output_tokens": 2003,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 24932,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2003,
          "cache_read_input_tokens": 43388,
          "cache_creation_input_tokens": 24932,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 24932
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

_source line 33 · 2026-05-16T02:25:27.863Z_

状态已同步。alpha_sweep_a025_s44（α=0.25, seed=44, Pythia-410m）完成，需要分析。派 Worker 读取日志和结果。

先看前序 seed 数据作为对比参考：
- **s42**: entropy -4.1%, d1 -40.3%, d2 -57.1%, d3 -59.9%
- **s43**: entropy -5.0%, d1 -40.5%, d2 -56.4%, d3 -58.7%

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6afade71-863f-44be-880d-7b3db246feef",
  "isSidechain": false,
  "requestId": "req_011Cb5TKbxyddoKSCkRbFCDa",
  "type": "assistant",
  "uuid": "be86c494-976d-4397-b8b7-a44fac32b509",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/agent_e1f64cd5",
  "sessionId": "4f6074eb-8665-49ec-9526-07c9eebcea03",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0146DRFxsmCt6r1etJtNM34g",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 24932,
      "cache_read_input_tokens": 43388,
      "output_tokens": 2003,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 24932,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2003,
          "cache_read_input_tokens": 43388,
          "cache_creation_input_tokens": 24932,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 24932
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

_source line 34 · 2026-05-16T02:25:29.816Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_012AebNpDUPV4BrvZbMkSP5b`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__save_project_file,mcp__agent-ml-research__read_experiment_plan_with_status,mcp__agent-ml-research__load_project_config",
  "max_results": 3
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "be86c494-976d-4397-b8b7-a44fac32b509",
  "isSidechain": false,
  "requestId": "req_011Cb5TKbxyddoKSCkRbFCDa",
  "type": "assistant",
  "uuid": "837f0807-fcb4-46af-ba19-698f7eb70c6d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/agent_e1f64cd5",
  "sessionId": "4f6074eb-8665-49ec-9526-07c9eebcea03",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0146DRFxsmCt6r1etJtNM34g",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 24932,
      "cache_read_input_tokens": 43388,
      "output_tokens": 2003,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 24932,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2003,
          "cache_read_input_tokens": 43388,
          "cache_creation_input_tokens": 24932,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 24932
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

_source line 35 · 2026-05-16T02:25:29.819Z_

<details><summary>↩ Tool result · `toolu_012AebNpDUPV4BrvZbMkSP5b`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__save_project_file"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__read_experiment_plan_with_status"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__load_project_config"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "837f0807-fcb4-46af-ba19-698f7eb70c6d",
  "isSidechain": false,
  "promptId": "a304cee9-feed-4fb2-a028-8ae1d93109aa",
  "type": "user",
  "uuid": "7db0b5db-9da7-4aa6-a6c4-92c58b3f3aa6",
  "toolUseResult": {
    "matches": [
      "mcp__agent-ml-research__save_project_file",
      "mcp__agent-ml-research__read_experiment_plan_with_status",
      "mcp__agent-ml-research__load_project_config"
    ],
    "query": "select:mcp__agent-ml-research__save_project_file,mcp__agent-ml-research__read_experiment_plan_with_status,mcp__agent-ml-research__load_project_config",
    "total_deferred_tools": 79
  },
  "sourceToolAssistantUUID": "837f0807-fcb4-46af-ba19-698f7eb70c6d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/agent_e1f64cd5",
  "sessionId": "4f6074eb-8665-49ec-9526-07c9eebcea03",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 36 · 2026-05-16T02:25:49.605Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__spawn_worker · `toolu_01JtjjQaQsLBusJoZX92yCLu`</summary>

````json
{
  "task_type": "analysis:alpha_sweep_a025_s44",
  "project": "distrib_canary_collapse",
  "task_prompt": "## 任务：分析 alpha_sweep_a025_s44 实验结果\n\n### 实验信息\n- exp_id: alpha_sweep_a025_s44\n- 服务器: westd-19828\n- 模型: EleutherAI/pythia-410m\n- 参数: seed=44, α=0.25, 10 generations, 5000 steps/gen\n- 数据: data/wikitext103_5k (5000 samples)\n- 输出目录: results/alpha_sweep/a025_s44\n- 日志: ~/runs/distrib_canary_collapse/alpha_sweep_a025_s44.log\n- 训练时长: 4.33h\n\n### 你需要做的\n\n1. **SSH 到 westd-19828 读取日志尾部**（ssh_read_only）：\n   ```\n   tail -100 ~/runs/distrib_canary_collapse/alpha_sweep_a025_s44.log\n   ```\n\n2. **读取 all_metrics.json**（ssh_read_only）：\n   ```\n   cat /root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a025_s44/all_metrics.json\n   ```\n   如果不存在，检查各 gen 子目录的 metrics.json。\n\n3. **提取关键指标**：\n   - gen0 和 gen10 的: token_entropy, ece, perplexity, distinct_1, distinct_2, distinct_3\n   - 如果有 effective_rank 和 mauve 也提取\n   - 计算 drift_pct = (gen10 - gen0) / gen0 * 100\n\n4. **与前序 seed 对比**（α=0.25 的 s42 和 s43）：\n   - s42: entropy_drift=-4.1%, ece_drift=+79.7%, ppl_drift=-17.2%, d1_drift=-40.3%, d2_drift=-57.1%, d3_drift=-59.9%\n   - s43: entropy_drift=-5.0%, ece_drift=+98.6%, ppl_drift=-18.7%, d1_drift=-40.5%, d2_drift=-56.4%, d3_drift=-58.7%\n   - 计算三 seed 的 mean ± std\n   - 判断 cross-seed deviation 是否 <7%（之前 α=0.50 两 seed deviation <7%）\n\n5. **更新 registry**：\n   用 update_registry 设置以下字段：\n   - metrics: 包含 gen0 和 gen10 各指标 + drift_pct\n   - conclusion: 如果实验正常完成且 metrics 合理，设为 \"success\"\n   - checkpoint_path: 指向最终 checkpoint 目录（results/alpha_sweep/a025_s44/gen_10/checkpoint 或类似路径）\n\n6. **输出分析摘要**：\n   - 三 seed 均值 ± 标准差\n   - 与 α=0.50 和 α=1.00 的对比趋势\n   - α=0.25 的 collapse 模式概括（是否温和 diversity collapse + 近乎不变的 entropy/ppl）\n\n### 环境\n- conda 环境: `source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`\n- 项目路径: /root/autodl-tmp/distrib_canary_collapse/",
  "tool_groups": [
    "ssh",
    "registry"
  ],
  "context": "项目 distrib_canary_collapse: 研究 iterative training 中合成数据污染导致的分布崩塌。当前 α sweep 实验覆盖 α=0/0.25/0.50/0.75/1.0。α=0.25 是低污染条件，预期温和的 diversity 下降但 entropy/perplexity 变化微小。"
}
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7db0b5db-9da7-4aa6-a6c4-92c58b3f3aa6",
  "isSidechain": false,
  "requestId": "req_011Cb5TKbxyddoKSCkRbFCDa",
  "type": "assistant",
  "uuid": "e4a2bcf7-1524-4624-91de-3be4fbd78bc0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/agent_e1f64cd5",
  "sessionId": "4f6074eb-8665-49ec-9526-07c9eebcea03",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0146DRFxsmCt6r1etJtNM34g",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 24932,
      "cache_read_input_tokens": 43388,
      "output_tokens": 2003,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 24932,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2003,
          "cache_read_input_tokens": 43388,
          "cache_creation_input_tokens": 24932,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 24932
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

_source line 37 · 2026-05-16T02:25:52.174Z_

<details><summary>↩ Tool result · `toolu_01JtjjQaQsLBusJoZX92yCLu`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"worker_id\": \"worker_analysis_alpha_sweep_a025_s44_20260516T022550\", \"status\": \"running\", \"log_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/logs/workers/worker_analysis_alpha_sweep_a025_s44_20260516T022550.log\", \"setup_data\": {}, \"message\": \"Worker worker_analysis_alpha_sweep_a025_s44_20260516T022550 started. Use get_worker_status('worker_analysis_alpha_sweep_a025_s44_20260516T022550') to check progress.\"}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e4a2bcf7-1524-4624-91de-3be4fbd78bc0",
  "isSidechain": false,
  "promptId": "a304cee9-feed-4fb2-a028-8ae1d93109aa",
  "type": "user",
  "uuid": "dc5cec62-ac81-45bf-ac00-ea41b13215b0",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"worker_id\\\": \\\"worker_analysis_alpha_sweep_a025_s44_20260516T022550\\\", \\\"status\\\": \\\"running\\\", \\\"log_path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/logs/workers/worker_analysis_alpha_sweep_a025_s44_20260516T022550.log\\\", \\\"setup_data\\\": {}, \\\"message\\\": \\\"Worker worker_analysis_alpha_sweep_a025_s44_20260516T022550 started. Use get_worker_status('worker_analysis_alpha_sweep_a025_s44_20260516T022550') to check progress.\\\"}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"worker_id\": \"worker_analysis_alpha_sweep_a025_s44_20260516T022550\", \"status\": \"running\", \"log_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/logs/workers/worker_analysis_alpha_sweep_a025_s44_20260516T022550.log\", \"setup_data\": {}, \"message\": \"Worker worker_analysis_alpha_sweep_a025_s44_20260516T022550 started. Use get_worker_status('worker_analysis_alpha_sweep_a025_s44_20260516T022550') to check progress.\"}, \"error\": null, \"metadata\": {}}"
    }
  },
  "sourceToolAssistantUUID": "e4a2bcf7-1524-4624-91de-3be4fbd78bc0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/agent_e1f64cd5",
  "sessionId": "4f6074eb-8665-49ec-9526-07c9eebcea03",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---
