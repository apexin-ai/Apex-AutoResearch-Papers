# Research conversation: [CRON] 实验进程已正常退出，状态已转为 ANALYZING，需要你分析结果并推进到 DONE。 详情: Process exited cleanly, W&B data available - exp_id: exp-005-gla-

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 43
- **Recorded user turns:** 1
- **Tool calls:** 11
- **Original source:** `logs/chats/exported-trajectories/account-3/ccd4bb6d-9c70-4ece-9e7e-8b842791a0aa.jsonl`
- **Structured JSON:** [`597511ab1b75a7bc6475.json`](../../sessions/59/597511ab1b75a7bc6475.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-22T16:41:37.346Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-22T16:41:37.346Z",
  "sessionId": "ccd4bb6d-9c70-4ece-9e7e-8b842791a0aa",
  "content": "[CRON] 实验进程已正常退出，状态已转为 ANALYZING，需要你分析结果并推进到 DONE。\n详情: Process exited cleanly, W&B data available\n\n- exp_id: exp-005-gla-pure\n- project: entrainment_gated_ft\n- server: westb-48145\n- log_path: ~/runs/entrainment_gated_ft/exp-005-gla-pure.log"
}
```

---

### Runtime record

_source line 2 · 2026-05-22T16:41:37.349Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-22T16:41:37.349Z",
  "sessionId": "ccd4bb6d-9c70-4ece-9e7e-8b842791a0aa"
}
```

---

## Round 1

41 recorded events

### User

_source line 3 · 2026-05-22T16:41:37.382Z_

[CRON] 实验进程已正常退出，状态已转为 ANALYZING，需要你分析结果并推进到 DONE。
详情: Process exited cleanly, W&B data available

- exp_id: exp-005-gla-pure
- project: entrainment_gated_ft
- server: westb-48145
- log_path: ~/runs/entrainment_gated_ft/exp-005-gla-pure.log

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "53afff33-bebc-42c8-b6ca-8baf6ae2df0c",
  "type": "user",
  "uuid": "71100355-3db0-46af-bcc4-e9c05ec74096",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/sessions/agent_aa1a2296",
  "sessionId": "ccd4bb6d-9c70-4ece-9e7e-8b842791a0aa",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-22T16:41:37.381Z_

```json
{
  "parentUuid": "71100355-3db0-46af-bcc4-e9c05ec74096",
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
  "uuid": "06996dc6-b25d-40d1-955b-70cd2e80c389",
  "timestamp": "2026-05-22T16:41:37.381Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/sessions/agent_aa1a2296",
  "sessionId": "ccd4bb6d-9c70-4ece-9e7e-8b842791a0aa",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-22T16:41:37.381Z_

```json
{
  "parentUuid": "06996dc6-b25d-40d1-955b-70cd2e80c389",
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
  "uuid": "041d8015-8ebd-4322-9bf3-9886b709fbcf",
  "timestamp": "2026-05-22T16:41:37.381Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/sessions/agent_aa1a2296",
  "sessionId": "ccd4bb6d-9c70-4ece-9e7e-8b842791a0aa",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6 · 2026-05-22T16:41:37.381Z_

```json
{
  "parentUuid": "041d8015-8ebd-4322-9bf3-9886b709fbcf",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "f4452065-6740-4a6e-83f4-5b4a89f117fd",
  "timestamp": "2026-05-22T16:41:37.381Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/sessions/agent_aa1a2296",
  "sessionId": "ccd4bb6d-9c70-4ece-9e7e-8b842791a0aa",
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
  "aiTitle": "Analyze experiment results and mark as done",
  "sessionId": "ccd4bb6d-9c70-4ece-9e7e-8b842791a0aa"
}
```

---

### Assistant

_source line 8 · 2026-05-22T16:41:42.578Z_

<details><summary>Logged reasoning block</summary>

```text
收到实验完成的 cron 回调，需要按 session-start 和 on-experiment-done 流程处理。

先执行 session-start 初始化：读 registry、reconcile crons、读 report.md 和 ROADMAP.md。然后分析 exp-005-gla-pure 的结果。

让我先加载需要的工具。
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f4452065-6740-4a6e-83f4-5b4a89f117fd",
  "isSidechain": false,
  "requestId": "req_011CbHwVJULzr6aBWbpVy6Ny",
  "type": "assistant",
  "uuid": "67668dd1-6d9c-4ac0-bcf7-8f3d90ce1e68",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/sessions/agent_aa1a2296",
  "sessionId": "ccd4bb6d-9c70-4ece-9e7e-8b842791a0aa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VdDpUYoyww2xvGAm9EtUBF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 25331,
      "cache_read_input_tokens": 11841,
      "output_tokens": 388,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 25331,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 388,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 25331,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 25331
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

_source line 9 · 2026-05-22T16:41:43.624Z_

收到 exp-005-gla-pure 完成回调，开始 session 初始化 + 结果分析。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "67668dd1-6d9c-4ac0-bcf7-8f3d90ce1e68",
  "isSidechain": false,
  "requestId": "req_011CbHwVJULzr6aBWbpVy6Ny",
  "type": "assistant",
  "uuid": "082a8aee-6536-4e42-9e15-8962bfa80844",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/sessions/agent_aa1a2296",
  "sessionId": "ccd4bb6d-9c70-4ece-9e7e-8b842791a0aa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VdDpUYoyww2xvGAm9EtUBF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 25331,
      "cache_read_input_tokens": 11841,
      "output_tokens": 388,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 25331,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 388,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 25331,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 25331
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

_source line 10 · 2026-05-22T16:41:46.391Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01DbKVFipTJDt8BqKwpyrhDV`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__reconcile_crons,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__read_roadmap,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__main_agent_post_to_director,mcp__agent-ml-research__spawn_worker,mcp__agent-ml-research__fetch_wandb_metrics,mcp__agent-ml-research__save_project_file,mcp__agent-ml-research__list_workers,mcp__agent-ml-research__read_experiment_plan_with_status",
  "max_results": 11
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "082a8aee-6536-4e42-9e15-8962bfa80844",
  "isSidechain": false,
  "requestId": "req_011CbHwVJULzr6aBWbpVy6Ny",
  "type": "assistant",
  "uuid": "aa6859da-c9c7-4e4f-8fb6-c8855933ec28",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/sessions/agent_aa1a2296",
  "sessionId": "ccd4bb6d-9c70-4ece-9e7e-8b842791a0aa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VdDpUYoyww2xvGAm9EtUBF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 25331,
      "cache_read_input_tokens": 11841,
      "output_tokens": 388,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 25331,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 388,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 25331,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 25331
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

_source line 11 · 2026-05-22T16:41:46.402Z_

<details><summary>↩ Tool result · `toolu_01DbKVFipTJDt8BqKwpyrhDV`</summary>

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
  "tool_name": "mcp__agent-ml-research__fetch_wandb_metrics"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__save_project_file"
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
  "tool_name": "mcp__agent-ml-research__read_experiment_plan_with_status"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "aa6859da-c9c7-4e4f-8fb6-c8855933ec28",
  "isSidechain": false,
  "promptId": "53afff33-bebc-42c8-b6ca-8baf6ae2df0c",
  "type": "user",
  "uuid": "dd4b2379-b1a5-45bd-8a23-52068a844743",
  "toolUseResult": {
    "matches": [
      "mcp__agent-ml-research__read_registry",
      "mcp__agent-ml-research__reconcile_crons",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__read_roadmap",
      "mcp__agent-ml-research__update_registry",
      "mcp__agent-ml-research__main_agent_post_to_director",
      "mcp__agent-ml-research__spawn_worker",
      "mcp__agent-ml-research__fetch_wandb_metrics",
      "mcp__agent-ml-research__save_project_file",
      "mcp__agent-ml-research__list_workers",
      "mcp__agent-ml-research__read_experiment_plan_with_status"
    ],
    "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__reconcile_crons,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__read_roadmap,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__main_agent_post_to_director,mcp__agent-ml-research__spawn_worker,mcp__agent-ml-research__fetch_wandb_metrics,mcp__agent-ml-research__save_project_file,mcp__agent-ml-research__list_workers,mcp__agent-ml-research__read_experiment_plan_with_status",
    "total_deferred_tools": 82
  },
  "sourceToolAssistantUUID": "aa6859da-c9c7-4e4f-8fb6-c8855933ec28",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/sessions/agent_aa1a2296",
  "sessionId": "ccd4bb6d-9c70-4ece-9e7e-8b842791a0aa",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 12 · 2026-05-22T16:41:50.188Z_

<details><summary>Logged reasoning block</summary>

```text
Now let me execute the session-start initialization steps in parallel: read registry, reconcile crons, read report.md, and read ROADMAP.md.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dd4b2379-b1a5-45bd-8a23-52068a844743",
  "isSidechain": false,
  "requestId": "req_011CbHwVyAmSPWi5G7kuCf5p",
  "type": "assistant",
  "uuid": "342334d6-e8ae-405b-b9de-4498ebab34f0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/sessions/agent_aa1a2296",
  "sessionId": "ccd4bb6d-9c70-4ece-9e7e-8b842791a0aa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ji6o9tmuz6jFh7TMfJvHve",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 4132,
      "cache_read_input_tokens": 37172,
      "output_tokens": 363,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4132,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 363,
          "cache_read_input_tokens": 37172,
          "cache_creation_input_tokens": 4132,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4132
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

_source line 13 · 2026-05-22T16:41:51.224Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_017SjjVew7bhkJio3KNz9LNC`</summary>

```json
{
  "project": "entrainment_gated_ft",
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
  "parentUuid": "342334d6-e8ae-405b-b9de-4498ebab34f0",
  "isSidechain": false,
  "requestId": "req_011CbHwVyAmSPWi5G7kuCf5p",
  "type": "assistant",
  "uuid": "e0343f6d-4d80-4f54-a1ee-04e1824eb267",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/sessions/agent_aa1a2296",
  "sessionId": "ccd4bb6d-9c70-4ece-9e7e-8b842791a0aa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ji6o9tmuz6jFh7TMfJvHve",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 4132,
      "cache_read_input_tokens": 37172,
      "output_tokens": 363,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4132,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 363,
          "cache_read_input_tokens": 37172,
          "cache_creation_input_tokens": 4132,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4132
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

_source line 14 · 2026-05-22T16:41:51.228Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__reconcile_crons · `toolu_01R9sMSKpamrZpeEZ6ePB6a3`</summary>

```json
{}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e0343f6d-4d80-4f54-a1ee-04e1824eb267",
  "isSidechain": false,
  "requestId": "req_011CbHwVyAmSPWi5G7kuCf5p",
  "type": "assistant",
  "uuid": "1592f242-eee1-44aa-b494-50dfa7e5077d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/sessions/agent_aa1a2296",
  "sessionId": "ccd4bb6d-9c70-4ece-9e7e-8b842791a0aa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ji6o9tmuz6jFh7TMfJvHve",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 4132,
      "cache_read_input_tokens": 37172,
      "output_tokens": 363,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4132,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 363,
          "cache_read_input_tokens": 37172,
          "cache_creation_input_tokens": 4132,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4132
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

_source line 15 · 2026-05-22T16:41:51.619Z_

<details><summary>↩ Tool result · `toolu_017SjjVew7bhkJio3KNz9LNC`</summary>

```text
&lt;persisted-output>
Output too large (56.8KB). Full output saved to: /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-2-projects-entrainment-gated-ft--claude-sessions-agent-aa1a2296/ccd4bb6d-9c70-4ece-9e7e-8b842791a0aa/tool-results/toolu_017SjjVew7bhkJio3KNz9LNC.txt

Preview (first 2KB):
{"result":"{\"success\": true, \"data\": {\"experiments\": {\"exp-005-gla-pure\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-22T16:33:56.971Z\", \"updated_at\": \"2026-05-22T16:41:30.660Z\", \"spec\": {\"command\": \"bash -c \\\"source /etc/network_turbo && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_HUB_DISABLE_XET=1 && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && python /root/entrainment_gated_ft/scripts/patch_fla_eval.py --model hf --model_args pretrained=/root/entrainment_gated_ft/models/340M-20B-GLA-pure-baseline,trust_remote_code=True --tasks lambada_openai,arc_easy --device cuda:0 --batch_size auto --log_samples --output_path /root/entrainment_gated_ft/results/exp005_zoo_expansion/GLA_pure/ && echo GLA_PURE_EVAL_DONE\\\"\", \"server\": \"westb-48145\", \"gpu\": [\"cuda:0\"], \"pid\": \"904591\", \"log_path\": \"~/runs/entrainment_gated_ft/exp-005-gla-pure.log\", \"submitted_at\": \"2026-05-22T16:39:54.061Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"reproduce\": {\"finished_at\": \"2026-05-22T16:41:30.660Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-22T16:41:32.936910+00:00\"}]}}, \"exp-005-pure-v5\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-22T16:37:28.872Z\", \"updated_at\": \"2026-05-22T16:37:28.872Z\", \"spec\": {\"command\": \"bash -c \\\"bash /root/entrainment_gated_ft/results/exp005_zoo_expansion/run_pure_v5.sh\\\"\", \"server\": \"westb-48145\", \"gpu\": [\"cuda:0\"], \"pid\": \"904122\", \"log_path\": \"~/runs/entrainment_gated_ft/exp-005-pure-v5.log\", \"submitted_at\": \"2026-05-22T16:37:28.788Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"exp-005-pure-v4\": {\"stat
...
&lt;/persisted-output>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e0343f6d-4d80-4f54-a1ee-04e1824eb267",
  "isSidechain": false,
  "promptId": "53afff33-bebc-42c8-b6ca-8baf6ae2df0c",
  "type": "user",
  "uuid": "78f6ae7e-294e-4a3b-918f-e28b1de9da42",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {\\\"exp-005-gla-pure\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-22T16:33:56.971Z\\\", \\\"updated_at\\\": \\\"2026-05-22T16:41:30.660Z\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"source /etc/network_turbo && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_HUB_DISABLE_XET=1 && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && python /root/entrainment_gated_ft/scripts/patch_fla_eval.py --model hf --model_args pretrained=/root/entrainment_gated_ft/models/340M-20B-GLA-pure-baseline,trust_remote_code=True --tasks lambada_openai,arc_easy --device cuda:0 --batch_size auto --log_samples --output_path /root/entrainment_gated_ft/results/exp005_zoo_expansion/GLA_pure/ && echo GLA_PURE_EVAL_DONE\\\\\\\"\\\", \\\"server\\\": \\\"westb-48145\\\", \\\"gpu\\\": [\\\"cuda:0\\\"], \\\"pid\\\": \\\"904591\\\", \\\"log_path\\\": \\\"~/runs/entrainment_gated_ft/exp-005-gla-pure.log\\\", \\\"submitted_at\\\": \\\"2026-05-22T16:39:54.061Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\"}, \\\"reproduce\\\": {\\\"finished_at\\\": \\\"2026-05-22T16:41:30.660Z\\\"}, \\\"extra\\\": {\\\"hook_events\\\": [{\\\"event\\\": \\\"on_complete\\\", \\\"action\\\": \\\"agent\\\", \\\"ts\\\": \\\"2026-05-22T16:41:32.936910+00:00\\\"}]}}, \\\"exp-005-pure-v5\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-22T16:37:28.872Z\\\", \\\"updated_at\\\": \\\"2026-05-22T16:37:28.872Z\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"bash /root/entrainment_gated_ft/results/exp005_zoo_expansion/run_pure_v5.sh\\\\\\\"\\\", \\\"server\\\": \\\"westb-48145\\\", \\\"gpu\\\": [\\\"cuda:0\\\"], \\\"pid\\\": \\\"904122\\\", \\\"log_path\\\": \\\"~/runs/entrainment_gated_ft/exp-005-pure-v5.log\\\", \\\"submitted_at\\\": \\\"2026-05-22T16:37:28.788Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\"}}, \\\"exp-005-pure-v4\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-22T16:35:11.429Z\\\", \\\"updated_at\\\": \\\"2026-05-22T16:35:11.429Z\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"bash /root/entrainment_gated_ft/results/exp005_zoo_expansion/run_pure_v4.sh\\\\\\\"\\\", \\\"server\\\": \\\"westb-48145\\\", \\\"gpu\\\": [\\\"cuda:0\\\"], \\\"pid\\\": \\\"903338\\\", \\\"log_path\\\": \\\"~/runs/entrainment_gated_ft/exp-005-pure-v4.log\\\", \\\"submitted_at\\\": \\\"2026-05-22T16:35:11.341Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\"}}, \\\"exp-005-pure-v3\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-22T16:32:39.150Z\\\", \\\"updated_at\\\": \\\"2026-05-22T16:32:39.150Z\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"bash /root/entrainment_gated_ft/results/exp005_zoo_expansion/run_pure_v3.sh\\\\\\\"\\\", \\\"server\\\": \\\"westb-48145\\\", \\\"gpu\\\": [\\\"cuda:0\\\"], \\\"pid\\\": \\\"902795\\\", \\\"log_path\\\": \\\"~/runs/entrainment_gated_ft/exp-005-pure-v3.log\\\", \\\"submitted_at\\\": \\\"2026-05-22T16:32:39.070Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\"}}, \\\"exp-005-batch\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-22T16:30:41.446Z\\\", \\\"updated_at\\\": \\\"2026-05-22T16:31:53.107Z\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"bash /root/entrainment_gated_ft/results/exp005_zoo_expansion/run_eval_download.sh\\\\\\\"\\\", \\\"server\\\": \\\"westb-48145\\\", \\\"gpu\\\": [\\\"cuda:0\\\"], \\\"pid\\\": \\\"902349\\\", \\\"log_path\\\": \\\"~/runs/entrainment_gated_ft/exp-005-batch.log\\\", \\\"submitted_at\\\": \\\"2026-05-22T16:30:41.362Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\"}, \\\"reproduce\\\": {\\\"finished_at\\\": \\\"2026-05-22T16:31:50.753Z\\\"}, \\\"failure_reason\\\": \\\"EXIT_CODE=1 (generic error — check log tail)\\\", \\\"conclusion\\\": \\\"failed\\\", \\\"extra\\\": {\\\"hook_events\\\": [{\\\"event\\\": \\\"on_failed\\\", \\\"action\\\": \\\"agent\\\", \\\"ts\\\": \\\"2026-05-22T16:31:55.361162+00:00\\\"}]}}, \\\"exp-005-hgrn-chain\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-22T16:27:47.360Z\\\", \\\"updated_at\\\": \\\"2026-05-22T16:27:47.360Z\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"bash /root/entrainment_gated_ft/results/exp005_zoo_expansion/run_hgrn_chain.sh\\\\\\\"\\\", \\\"server\\\": \\\"westb-48145\\\", \\\"gpu\\\": [\\\"cuda:0\\\"], \\\"pid\\\": \\\"902087\\\", \\\"log_path\\\": \\\"~/runs/entrainment_gated_ft/exp-005-hgrn-chain.log\\\", \\\"submitted_at\\\": \\\"2026-05-22T16:27:47.270Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\"}}, \\\"exp-005\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"retry_count\\\": 1, \\\"created_at\\\": \\\"2026-05-20T02:26:40.718Z\\\", \\\"updated_at\\\": \\\"2026-05-22T16:18:38.064Z\\\", \\\"hypothesis\\\": \\\"Cross-architecture Jaccard overlap of helped/hurt sets will remain significantly above chance when expanded from 3 to 6 linear attention architectures, indicating that attention-mediated sample sensitivity is architecture-independent.\\\", \\\"parent\\\": \\\"exp-001\\\", \\\"completed_at\\\": \\\"2026-05-22T14:24:29.103Z\\\", \\\"extra\\\": {\\\"previous_failure\\\": {\\\"conclusion\\\": \\\"killed\\\", \\\"metrics\\\": {\\\"cancel_reason\\\": \\\"Wang et al. zoo 仅含 GDN/RetNet/HGRN2，无法扩展 n>3，已由 worker_analysis_arch-extension-check 确认\\\"}}, \\\"hook_events\\\": [{\\\"event\\\": \\\"on_failed\\\", \\\"action\\\": \\\"agent\\\", \\\"ts\\\": \\\"2026-05-22T15:05:27.711311+00:00\\\"}]}, \\\"metrics\\\": {\\\"gla_h31_lambada_acc\\\": 0.3819, \\\"gla_h31_arc_acc\\\": 0.5673, \\\"deltanet_h31_lambada_acc\\\": 0.3536, \\\"deltanet_h31_lambada_ppl\\\": 30.45, \\\"deltanet_h31_arc_acc\\\": 0.601, \\\"fla_patch_needed\\\": \\\"scripts/patch_fla_eval.py fixes _tied_weights_keys list→dict for fla 0.5.0 + transformers 5.8.1\\\"}, \\\"reproduce\\\": {\\\"finished_at\\\": \\\"2026-05-22T15:05:23.157Z\\\"}, \\\"failure_reason\\\": \\\"EXIT_CODE=1 (generic error — check log tail)\\\", \\\"conclusion\\\": \\\"failed\\\", \\\"notes\\\": \\\"诊断中: worker_diagnose_exp-005-p1-v4_20260522T150706 正在查日志。日志仅7行，进程在下载 DeltaNet h3-1 模型时 EXIT_CODE=1 退出。\\\"}, \\\"exp-005-p1-eval-v5\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-22T16:18:29.815Z\\\", \\\"updated_at\\\": \\\"2026-05-22T16:18:29.815Z\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"bash /root/entrainment_gated_ft/results/exp005_zoo_expansion/run_eval_p1.sh\\\\\\\"\\\", \\\"server\\\": \\\"westb-48145\\\", \\\"gpu\\\": [\\\"cuda:0\\\"], \\\"pid\\\": \\\"898757\\\", \\\"log_path\\\": \\\"~/runs/entrainment_gated_ft/exp-005-p1-eval-v5.log\\\", \\\"submitted_at\\\": \\\"2026-05-22T16:18:29.731Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\"}}, \\\"exp-005-p1-eval-v4\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-22T16:16:34.914Z\\\", \\\"updated_at\\\": \\\"2026-05-22T16:16:34.914Z\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"bash /root/entrainment_gated_ft/results/exp005_zoo_expansion/run_eval_p1.sh\\\\\\\"\\\", \\\"server\\\": \\\"westb-48145\\\", \\\"gpu\\\": [\\\"cuda:0\\\"], \\\"pid\\\": \\\"897689\\\", \\\"log_path\\\": \\\"~/runs/entrainment_gated_ft/exp-005-p1-eval-v4.log\\\", \\\"submitted_at\\\": \\\"2026-05-22T16:16:34.836Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\"}}, \\\"exp-005-dn-eval\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-22T15:56:19.907Z\\\", \\\"updated_at\\\": \\\"2026-05-22T16:10:46.245Z\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"source /etc/network_turbo && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_HUB_DISABLE_XET=1 && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && cd /root/entrainment_gated_ft && python scripts/patch_fla_eval.py --model hf --model_args pretrained=/root/entrainment_gated_ft/models/340M-20B-DeltaNet-hybrid-3-1,trust_remote_code=True,dtype=float16 --tasks lambada_openai,arc_easy --device cuda:0 --batch_size auto --log_samples --output_path /root/entrainment_gated_ft/results/exp005_zoo_expansion/DeltaNet_hybrid-3-1/ && echo DELTANET_EVAL_DONE\\\\\\\"\\\", \\\"server\\\": \\\"westb-48145\\\", \\\"gpu\\\": [\\\"cuda:0\\\"], \\\"pid\\\": \\\"886300\\\", \\\"log_path\\\": \\\"~/runs/entrainment_gated_ft/exp-005-dn-eval.log\\\", \\\"submitted_at\\\": \\\"2026-05-22T16:04:02.638Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\"}, \\\"metrics\\\": {\\\"model\\\": \\\"340M-20B-DeltaNet-hybrid-3-1\\\", \\\"lambada_openai_acc\\\": 0.3536, \\\"lambada_openai_ppl\\\": 30.45, \\\"arc_easy_acc\\\": 0.601, \\\"arc_easy_acc_norm\\\": 0.5198, \\\"status\\\": \\\"DONE\\\"}}, \\\"exp-005-p1-eval-v3\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-22T16:07:46.157Z\\\", \\\"updated_at\\\": \\\"2026-05-22T16:07:46.157Z\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"bash /root/entrainment_gated_ft/results/exp005_zoo_expansion/run_eval_p1.sh\\\\\\\"\\\", \\\"server\\\": \\\"westb-48145\\\", \\\"gpu\\\": [\\\"cuda:0\\\"], \\\"pid\\\": \\\"891633\\\", \\\"log_path\\\": \\\"~/runs/entrainment_gated_ft/exp-005-p1-eval-v3.log\\\", \\\"submitted_at\\\": \\\"2026-05-22T16:07:46.079Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\"}}, \\\"exp-005-p1-eval-v2\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-22T16:06:40.443Z\\\", \\\"updated_at\\\": \\\"2026-05-22T16:06:40.443Z\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"bash /root/entrainment_gated_ft/results/exp005_zoo_expansion/run_eval_p1.sh\\\\\\\"\\\", \\\"server\\\": \\\"westb-48145\\\", \\\"gpu\\\": [\\\"cuda:0\\\"], \\\"pid\\\": \\\"889541\\\", \\\"log_path\\\": \\\"~/runs/entrainment_gated_ft/exp-005-p1-eval-v2.log\\\", \\\"submitted_at\\\": \\\"2026-05-22T16:06:40.369Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\"}}, \\\"exp-005-p1-eval\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-22T16:01:38.958Z\\\", \\\"updated_at\\\": \\\"2026-05-22T16:01:38.958Z\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"bash /root/entrainment_gated_ft/results/exp005_zoo_expansion/run_eval_p1.sh\\\\\\\"\\\", \\\"server\\\": \\\"westb-48145\\\", \\\"gpu\\\": [\\\"cuda:0\\\"], \\\"pid\\\": \\\"884365\\\", \\\"log_path\\\": \\\"~/runs/entrainment_gated_ft/exp-005-p1-eval.log\\\", \\\"submitted_at\\\": \\\"2026-05-22T16:01:38.883Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\"}}, \\\"exp-005-pure-eval\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-22T15:58:12.656Z\\\", \\\"updated_at\\\": \\\"2026-05-22T16:01:21.317Z\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"bash /root/entrainment_gated_ft/results/exp005_zoo_expansion/run_wget_eval_pure.sh\\\\\\\"\\\", \\\"server\\\": \\\"westb-48145\\\", \\\"gpu\\\": [\\\"cuda:0\\\"], \\\"pid\\\": \\\"884046\\\", \\\"log_path\\\": \\\"~/runs/entrainment_gated_ft/exp-005-pure-eval.log\\\", \\\"submitted_at\\\": \\\"2026-05-22T16:01:21.241Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\"}}, \\\"exp-005-deltanet\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-22T15:51:45.169Z\\\", \\\"updated_at\\\": \\\"2026-05-22T15:51:45.169Z\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"bash /root/entrainment_gated_ft/results/exp005_zoo_expansion/eval_deltanet_hardcode.sh\\\\\\\"\\\", \\\"server\\\": \\\"westb-48145\\\", \\\"gpu\\\": [\\\"cuda:0\\\"], \\\"pid\\\": \\\"881335\\\", \\\"log_path\\\": \\\"~/runs/entrainment_gated_ft/exp-005-deltanet.log\\\", \\\"submitted_at\\\": \\\"2026-05-22T15:51:45.096Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\"}}, \\\"exp-005-gla\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-22T15:41:49.615Z\\\", \\\"updated_at\\\": \\\"2026-05-22T15:48:24.790Z\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"bash /root/entrainment_gated_ft/results/exp005_zoo_expansion/eval_gla_hardcode.sh\\\\\\\"\\\", \\\"server\\\": \\\"westb-48145\\\", \\\"gpu\\\": [\\\"cuda:0\\\"], \\\"pid\\\": \\\"878457\\\", \\\"log_path\\\": \\\"~/runs/entrainment_gated_ft/exp-005-gla.log\\\", \\\"submitted_at\\\": \\\"2026-05-22T15:48:24.719Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\"}}, \\\"exp-005-gla-eval\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-22T15:38:30.968Z\\\", \\\"updated_at\\\": \\\"2026-05-22T15:44:36.037Z\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"source /etc/network_turbo && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_HUB_DISABLE_XET=1 && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && python -c 'import fla; print(fla.__version__)' && python -m lm_eval --model hf --model_args pretrained=/root/entrainment_gated_ft/models/340M-20B-GLA-hybrid-3-1,trust_remote_code=True --tasks lambada_openai,arc_easy --device cuda:0 --batch_size auto --log_samples --output_path /root/entrainment_gated_ft/results/exp005_zoo_expansion/GLA_hybrid-3-1/ && echo GLA_EVAL_DONE\\\\\\\"\\\", \\\"server\\\": \\\"westb-48145\\\", \\\"gpu\\\": [\\\"cuda:0\\\"], \\\"pid\\\": \\\"875395\\\", \\\"log_path\\\": \\\"~/runs/entrainment_gated_ft/exp-005-gla-eval.log\\\", \\\"submitted_at\\\": \\\"2026-05-22T15:42:46.005Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\"}, \\\"reproduce\\\": {\\\"finished_at\\\": \\\"2026-05-22T15:43:08.734Z\\\"}, \\\"extra\\\": {\\\"hook_events\\\": [{\\\"event\\\": \\\"on_complete\\\", \\\"action\\\": \\\"agent\\\", \\\"ts\\\": \\\"2026-05-22T15:39:05.469998+00:00\\\"}, {\\\"event\\\": \\\"on_failed\\\", \\\"action\\\": \\\"agent\\\", \\\"ts\\\": \\\"2026-05-22T15:43:12.720582+00:00\\\"}]}, \\\"failure_reason\\\": \\\"Traceback → ss = CONFIG_MAPPING[config_dict[\\\\\\\"model_type\\\\\\\"]] ~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^ File \\\\\\\"/root/miniconda3/lib/python3.12/site-packages/transformers/models/auto/configuration_auto.py\\\\\\\", line 105, in __getitem__ raise KeyError(key) KeyError: 'gla'\\\", \\\"conclusion\\\": \\\"failed\\\", \\\"notes\\\": \\\"失败原因已诊断：1) 首次提交 pretrained='' 空字符串（shell 变量展开问题）；2) 重试时 KeyError: 'gla'（transformers AutoModel 不识别 GLA 模型类型，需要 fla 包注册）。模型文件本身完整（340M-20B-GLA-hybrid-3-1/model.safetensors 存在）。worker_fix_exp-005-gla-eval-hardcode 正在创建 wrapper 脚本修复。\\\"}, \\\"exp-005-p1-v4\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-22T14:49:36.217Z\\\", \\\"updated_at\\\": \\\"2026-05-22T14:49:36.217Z\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"bash /root/entrainment_gated_ft/results/exp005_zoo_expansion/run_p1_v4.sh\\\\\\\"\\\", \\\"server\\\": \\\"westb-48145\\\", \\\"gpu\\\": [\\\"cuda:0\\\"], \\\"pid\\\": \\\"870648\\\", \\\"log_path\\\": \\\"~/runs/entrainment_gated_ft/exp-005-p1-v4.log\\\", \\\"submitted_at\\\": \\\"2026-05-22T14:49:36.151Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\"}}, \\\"exp-005-eval\\\": {\\\"status\\\": \\\"PENDING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-22T14:22:49.860Z\\\", \\\"updated_at\\\": \\\"2026-05-22T14:25:11.027Z\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash -c '\\\\nset -eo pipefail\\\\nsource /etc/network_turbo\\\\nsource /root/miniconda3/etc/profile.d/conda.sh && conda activate base\\\\nexport HF_HOME=/root/autodl-tmp/.hf_cache\\\\nexport HF_HUB_DISABLE_XET=1\\\\nexport REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt\\\\nexport SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt\\\\n\\\\nMODELS_DIR=\\\\\\\"/root/entrainment_gated_ft/models\\\\\\\"\\\\nRESULTS_DIR=\\\\\\\"/root/entrainment_gated_ft/results/exp005_zoo_expansion\\\\\\\"\\\\nLOG=\\\\\\\"$RESULTS_DIR/run_all.log\\\\\\\"\\\\nmkdir -p \\\\\\\"$RESULTS_DIR\\\\\\\"\\\\n\\\\necho \\\\\\\"=== EXP-005 FULL RUN $(date) ===\\\\\\\" | tee \\\\\\\"$LOG\\\\\\\"\\\\n\\\\n# Phase 1: Download missing Priority 1 models (GLA already done)\\\\nfor arch in DeltaNet HGRN; do\\\\n  MODEL_NAME=\\\\\\\"340M-20B-${arch}-hybrid-3-1\\\\\\\"\\\\n  MODEL_DIR=\\\\\\\"$MODELS_DIR/$MODEL_NAME\\\\\\\"\\\\n  if [ ! -f \\\\\\\"$MODEL_DIR/model.safetensors\\\\\\\" ]; then\\\\n    echo \\\\\\\"Downloading $MODEL_NAME ...\\\\\\\" | tee -a \\\\\\\"$LOG\\\\\\\"\\\\n    rm -rf \\\\\\\"$MODEL_DIR\\\\\\\"\\\\n    huggingface-cli download \\\\\\\"m-a-p/$MODEL_NAME\\\\\\\" --local-dir \\\\\\\"$MODEL_DIR\\\\\\\" 2>&1 | tail -5 | tee -a \\\\\\\"$LOG\\\\\\\"\\\\n    echo \\\\\\\"Downloaded $MODEL_NAME $(date)\\\\\\\" | tee -a \\\\\\\"$LOG\\\\\\\"\\\\n  else\\\\n    echo \\\\\\\"Already have $MODEL_NAME\\\\\\\" | tee -a \\\\\\\"$LOG\\\\\\\"\\\\n  fi\\\\ndone\\\\n\\\\n# Phase 2: Evaluate Priority 1 (h3-1 x 3 new archs)\\\\nfor arch in GLA DeltaNet HGRN; do\\\\n  MODEL_NAME=\\\\\\\"340M-20B-${arch}-hybrid-3-1\\\\\\\"\\\\n  MODEL_DIR=\\\\\\\"$MODELS_DIR/$MODEL_NAME\\\\\\\"\\\\n  OUT_DIR=\\\\\\\"$RESULTS_DIR/${arch}_hybrid-3-1\\\\\\\"\\\\n  echo \\\\\\\"EVAL $MODEL_NAME START $(date)\\\\\\\" | tee -a \\\\\\\"$LOG\\\\\\\"\\\\n  python -m lm_eval \\\\\\\\\\\\n    --model hf \\\\\\\\\\\\n    --model_args pretrained=$MODEL_DIR,trust_remote_code=True \\\\\\\\\\\\n    --tasks lambada_openai,arc_easy \\\\\\\\\\\\n    --device cuda:0 \\\\\\\\\\\\n    --batch_size auto \\\\\\\\\\\\n    --log_samples \\\\\\\\\\\\n    --output_path \\\\\\\"$OUT_DIR/\\\\\\\" 2>&1 | tail -10 | tee -a \\\\\\\"$LOG\\\\\\\"\\\\n  echo \\\\\\\"EVAL $MODEL_NAME DONE $(date)\\\\\\\" | tee -a \\\\\\\"$LOG\\\\\\\"\\\\ndone\\\\n\\\\necho \\\\\\\"=== PRIORITY 1 COMPLETE $(date) ===\\\\\\\" | tee -a \\\\\\\"$LOG\\\\\\\"\\\\n\\\\n# Phase 3: Download + evaluate remaining ratios\\\\nfor arch in GLA DeltaNet HGRN; do\\\\n  for ratio in pure-baseline hybrid-24-1 hybrid-12-1 hybrid-6-1; do\\\\n    MODEL_NAME=\\\\\\\"340M-20B-${arch}-${ratio}\\\\\\\"\\\\n    MODEL_DIR=\\\\\\\"$MODELS_DIR/$MODEL_NAME\\\\\\\"\\\\n    OUT_DIR=\\\\\\\"$RESULTS_DIR/${arch}_${ratio}\\\\\\\"\\\\n\\\\n    if [ ! -f \\\\\\\"$MODEL_DIR/model.safetensors\\\\\\\" ]; then\\\\n      echo \\\\\\\"Downloading $MODEL_NAME ...\\\\\\\" | tee -a \\\\\\\"$LOG\\\\\\\"\\\\n      rm -rf \\\\\\\"$MODEL_DIR\\\\\\\"\\\\n      huggingface-cli download \\\\\\\"m-a-p/$MODEL_NAME\\\\\\\" --local-dir \\\\\\\"$MODEL_DIR\\\\\\\" 2>&1 | tail -3 | tee -a \\\\\\\"$LOG\\\\\\\"\\\\n      if [ ! -f \\\\\\\"$MODEL_DIR/model.safetensors\\\\\\\" ]; then\\\\n        ALT_NAME=\\\\\\\"340M-20B-${arch}-pure\\\\\\\"\\\\n        if [ \\\\\\\"$ratio\\\\\\\" = \\\\\\\"pure-baseline\\\\\\\" ]; then\\\\n          echo \\\\\\\"Trying alternate: $ALT_NAME ...\\\\\\\" | tee -a \\\\\\\"$LOG\\\\\\\"\\\\n          huggingface-cli download \\\\\\\"m-a-p/$ALT_NAME\\\\\\\" --local-dir \\\\\\\"$MODELS_DIR/$ALT_NAME\\\\\\\" 2>&1 | tail -3 | tee -a \\\\\\\"$LOG\\\\\\\"\\\\n          MODEL_DIR=\\\\\\\"$MODELS_DIR/$ALT_NAME\\\\\\\"\\\\n        fi\\\\n      fi\\\\n      echo \\\\\\\"Downloaded $(date)\\\\\\\" | tee -a \\\\\\\"$LOG\\\\\\\"\\\\n    fi\\\\n\\\\n    echo \\\\\\\"EVAL $MODEL_NAME START $(date)\\\\\\\" | tee -a \\\\\\\"$LOG\\\\\\\"\\\\n    python -m lm_eval \\\\\\\\\\\\n      --model hf \\\\\\\\\\\\n      --model_args pretrained=$MODEL_DIR,trust_remote_code=True \\\\\\\\\\\\n      --tasks lambada_openai,arc_easy \\\\\\\\\\\\n      --device cuda:0 \\\\\\\\\\\\n      --batch_size auto \\\\\\\\\\\\n      --log_samples \\\\\\\\\\\\n      --output_path \\\\\\\"$OUT_DIR/\\\\\\\" 2>&1 | tail -10 | tee -a \\\\\\\"$LOG\\\\\\\"\\\\n    echo \\\\\\\"EVAL $MODEL_NAME DONE $(date)\\\\\\\" | tee -a \\\\\\\"$LOG\\\\\\\"\\\\n  done\\\\ndone\\\\n\\\\necho \\\\\\\"=== ALL EVALUATIONS COMPLETE $(date) ===\\\\\\\" | tee -a \\\\\\\"$LOG\\\\\\\"\\\\n'\\\", \\\"server\\\": \\\"westb-48145\\\", \\\"gpu\\\": [\\\"cuda:0\\\"], \\\"pid\\\": \\\"unknown\\\", \\\"log_path\\\": \\\"~/runs/entrainment_gated_ft/exp-005-eval.log\\\", \\\"submitted_at\\\": \\\"2026-05-22T14:22:49.797Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\"}, \\\"reproduce\\\": {\\\"finished_at\\\": \\\"2026-05-22T14:23:13.448Z\\\"}, \\\"failure_reason\\\": \\\"EXIT_CODE=1 (generic error — check log tail)\\\", \\\"conclusion\\\": \\\"killed\\\", \\\"extra\\\": {\\\"hook_events\\\": [{\\\"event\\\": \\\"on_failed\\\", \\\"action\\\": \\\"agent\\\", \\\"ts\\\": \\\"2026-05-22T14:23:17.070767+00:00\\\"}]}, \\\"hypothesis\\\": \\\"Cross-architecture per-example Jaccard (helped/hurt) remains ≤0.10 when expanding from 3 architectures (GDN/RetNet/HGRN2) to 6 (adding GLA/DeltaNet/HGRN), with 15 pairwise comparisons and 720 permutations providing dramatically stronger statistical power.\\\"}, \\\"e4-pythia-seed-calibration\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-22T10:17:05.445Z\\\", \\\"updated_at\\\": \\\"2026-05-22T11:44:42.532Z\\\", \\\"hypothesis\\\": \\\"Pythia 70M 9-seed variants 的 within-seed per-example Jaccard (same architecture, different random seed) 显著高于 cross-architecture Jaccard (~0.10), 证明 within-arch overlap >> cross-arch overlap, 即 cross-arch 信号不能被 seed noise 解释。\\\", \\\"parent\\\": \\\"exp-001\\\", \\\"spec\\\": {\\\"command\\\": \\\"lm_eval --model hf --tasks lambada_openai,arc_easy --log_samples\\\", \\\"server\\\": \\\"westb-48145\\\", \\\"model_name\\\": \\\"EleutherAI/pythia-70m-seed{1-9}\\\", \\\"seed\\\": \\\"1-9\\\", \\\"data_path\\\": \\\"/root/entrainment_gated_ft/results/e4_pythia_seed/\\\", \\\"data_count\\\": \\\"5153+2376 per seed × 9 seeds\\\", \\\"checkpoint_source\\\": \\\"ModelScope CDN\\\", \\\"eval_data\\\": \\\"lambada_openai + arc_easy\\\", \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/pythia_weights_70m/seed{1-9}/\\\", \\\"log_path\\\": \\\"/root/entrainment_gated_ft/results/e4_pythia_seed/eval.log\\\"}, \\\"reproduce\\\": {\\\"finished_at\\\": \\\"2026-05-22T11:10:00.780Z\\\"}, \\\"failure_reason\\\": \\\"process dead 5× with no sentinel/W&B — auto-resolved as failed\\\", \\\"conclusion\\\": \\\"success\\\", \\\"completed_at\\\": \\\"2026-05-22T11:10:01.238Z\\\", \\\"extra\\\": {\\\"hook_events\\\": [{\\\"event\\\": \\\"on_failed\\\", \\\"action\\\": \\\"agent\\\", \\\"ts\\\": \\\"2026-05-22T11:10:03.664374+00:00\\\"}]}, \\\"metrics\\\": {\\\"lambada_J_helped\\\": 0.273, \\\"lambada_J_hurt\\\": 0.393, \\\"lambada_alpha\\\": 0.355, \\\"arc_J_helped\\\": 0.312, \\\"arc_alpha\\\": 0.491, \\\"cross_arch_ref_J_helped\\\": 0.1, \\\"ratio_lambada\\\": 2.73, \\\"ratio_arc\\\": 3.12}}, \\\"exp-340m-multi-bench\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-21T22:23:25.467Z\\\", \\\"updated_at\\\": \\\"2026-05-22T00:34:02.116Z\\\", \\\"hypothesis\\\": \\\"340M models exhibit α spectrum (per-example ambiguity) consistent with 1.3B across HellaSwag/PIQA/ARC-Easy — establishing scale-invariance of the multiplicity phenomenon beyond the single-benchmark (LAMBADA) evidence in §4.3. If α_340M ≈ α_1.3B per benchmark, cross-scale stability is confirmed; if systematically different, the scale-dependency claim needs qualification.\\\", \\\"parent\\\": \\\"exp-007\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash run_340m_multi_eval.sh (run_lmeval_clean.py × 15 models × 3 tasks with --log_samples)\\\", \\\"server\\\": \\\"westb-48145\\\", \\\"gpu\\\": [\\\"cuda:0\\\"], \\\"data_path\\\": \\\"/root/entrainment_gated_ft/models/ (15 × 340M models)\\\", \\\"data_count\\\": \\\"hellaswag=10042, piqa=1838, arc_easy=2376 per model\\\", \\\"model_name\\\": \\\"GDN/RetNet/HGRN2 × 5 ratios (340M, 15 models)\\\", \\\"seed\\\": \\\"default\\\", \\\"checkpoint_source\\\": \\\"/root/entrainment_gated_ft/models/340M-20B-*\\\", \\\"eval_data\\\": \\\"HellaSwag (10042) + PIQA (1838) + ARC-Easy (2376)\\\", \\\"pid\\\": \\\"777365\\\", \\\"log_path\\\": \\\"~/runs/entrainment_gated_ft/exp-340m-multi-bench.log\\\", \\\"submitted_at\\\": \\\"2026-05-21T22:27:20Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"checkpoint_path\\\": \\\"/root/entrainment_gated_ft/lm_eval_clean/340m_multi/\\\", \\\"wall_clock_seconds\\\": 7602.1, \\\"gpu_hours\\\": 2.11}, \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"hellaswag_acc_norm\\\": {\\\"340m_alpha_all\\\": 0.334, \\\"1_3b_alpha_all\\\": 0.302, \\\"delta\\\": 0.031, \\\"340m_alpha_pure\\\": 0.167, \\\"1_3b_alpha_pure\\\": 0.148, \\\"340m_J_helped\\\": 0.084, \\\"1_3b_J_helped\\\": 0.095, \\\"340m_J_hurt\\\": 0.083, \\\"1_3b_J_hurt\\\": 0.085, \\\"340m_convergence_rho\\\": 0.4, \\\"340m_convergence_p\\\": 0.517}, \\\"piqa\\\": {\\\"340m_alpha_all\\\": 0.366, \\\"1_3b_alpha_all\\\": 0.278, \\\"delta\\\": 0.089, \\\"340m_alpha_pure\\\": 0.181, \\\"1_3b_alpha_pure\\\": 0.143, \\\"340m_J_helped\\\": 0.09, \\\"1_3b_J_helped\\\": 0.091, \\\"340m_J_hurt\\\": 0.085, \\\"1_3b_J_hurt\\\": 0.094, \\\"340m_convergence_rho\\\": 0.3, \\\"340m_convergence_p\\\": 0.683}, \\\"arc_easy\\\": {\\\"340m_alpha_all\\\": 0.564, \\\"1_3b_alpha_all\\\": 0.434, \\\"delta\\\": 0.13, \\\"340m_alpha_pure\\\": 0.289, \\\"1_3b_alpha_pure\\\": 0.205, \\\"340m_J_helped\\\": 0.098, \\\"1_3b_J_helped\\\": 0.092, \\\"340m_J_hurt\\\": 0.103, \\\"1_3b_J_hurt\\\": 0.099, \\\"340m_convergence_rho\\\": -0.1, \\\"340m_convergence_p\\\": 0.95}, \\\"summary\\\": {\\\"mean_delta_alpha_all\\\": 0.084, \\\"scenario\\\": \\\"B_mixed\\\", \\\"pattern_invariant\\\": true, \\\"magnitude_scale_dependent\\\": true}, \\\"artifacts\\\": [\\\"340m_multi_bench_analysis.json\\\"]}, \\\"completed_at\\\": \\\"2026-05-22T00:34:02.116Z\\\"}, \\\"w3-winogrande-piqa-eval\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-21T08:28:29.577Z\\\", \\\"updated_at\\\": \\\"2026-05-21T10:27:33.995Z\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash run_winogrande_piqa_all.sh (run_lmeval_clean.py × 30 tasks)\\\", \\\"server\\\": \\\"westb-48145\\\", \\\"gpu\\\": [\\\"cuda:0\\\"], \\\"pid\\\": \\\"722233\\\", \\\"log_path\\\": \\\"/root/entrainment_gated_ft/lm_eval_clean/winogrande_piqa_eval.log\\\", \\\"submitted_at\\\": \\\"2026-05-21T08:28:29.524Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"data_path\\\": \\\"lm-eval-harness winogrande + piqa\\\", \\\"data_count\\\": \\\"winogrande=1267, piqa=1838\\\", \\\"model_name\\\": \\\"GDN/RetNet/HGRN2 × 5 ratios (1.3B)\\\", \\\"seed\\\": \\\"default\\\", \\\"checkpoint_path\\\": \\\"artifacts/paper_data/winogrande_per_example.json + piqa_per_example.json\\\", \\\"wall_clock_seconds\\\": 7144.5, \\\"gpu_hours\\\": 1.98}, \\\"hypothesis\\\": \\\"WinoGrande + PIQA per-example multiplicity analysis to decouple format (2-choice vs 4-way MC) from task-type as driver of ambiguity α spectrum, addressing Round 5 W3 format confound concern\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"winogrande\\\": {\\\"n_samples\\\": 1267, \\\"alpha_pure\\\": 0.463, \\\"alpha_range\\\": [0.409, 0.463], \\\"convergence_rho\\\": -0.2, \\\"convergence_p\\\": 0.783}, \\\"piqa\\\": {\\\"n_samples\\\": 1838, \\\"alpha_pure\\\": 0.143, \\\"alpha_range\\\": [0.132, 0.143], \\\"convergence_rho\\\": -0.5, \\\"convergence_p\\\": 0.45}, \\\"format_confound_test\\\": {\\\"finding\\\": \\\"PIQA (2-choice, α=0.14) vs WinoGrande (2-choice, α=0.46) vs BoolQ (2-choice, α=0.51) — same format, 3.5× α variation. Format confound refuted.\\\", \\\"alpha_vs_accuracy_rho\\\": 0.03, \\\"alpha_vs_accuracy_p_exact\\\": 1}, \\\"artifacts\\\": [\\\"winogrande_per_example.json\\\", \\\"piqa_per_example.json\\\", \\\"winogrande_jaccard_analysis.json\\\", \\\"piqa_jaccard_analysis.json\\\"]}, \\\"completed_at\\\": \\\"2026-05-21T10:27:33.995Z\\\"}, \\\"exp-boolq-hellaswag-eval\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-20T11:32:21.428Z\\\", \\\"updated_at\\\": \\\"2026-05-21T08:53:38.336Z\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash run_boolq_hellaswag_all.sh\\\", \\\"server\\\": \\\"westb-48145\\\", \\\"gpu\\\": [\\\"cuda:0\\\"], \\\"pid\\\": \\\"653104\\\", \\\"log_path\\\": \\\"~/runs/entrainment_gated_ft/exp-boolq-hellaswag-eval.log\\\", \\\"submitted_at\\\": \\\"2026-05-20T11:32:21.381Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"data_path\\\": \\\"/root/entrainment_gated_ft/lm_eval_clean/\\\", \\\"data_count\\\": 13312, \\\"model_name\\\": \\\"GDN/RetNet/HGRN2 x 5 ratios + Transformer (15 models)\\\", \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/models_1.3b/\\\", \\\"eval_data\\\": \\\"BoolQ (3270 samples) + HellaSwag (10042 samples)\\\", \\\"wall_clock_seconds\\\": 76877.0, \\\"gpu_hours\\\": 21.35}, \\\"reproduce\\\": {\\\"finished_at\\\": \\\"2026-05-20T12:47:53.740Z\\\"}, \\\"extra\\\": {\\\"hook_events\\\": [{\\\"event\\\": \\\"on_complete\\\", \\\"action\\\": \\\"agent\\\", \\\"ts\\\": \\\"2026-05-20T12:47:55.697105+00:00\\\"}]}, \\\"conclusion\\\": \\\"success\\\", \\\"checkpoint_path\\\": \\\"/root/entrainment_gated_ft/lm_eval_clean/boolq/ + /root/entrainment_gated_ft/lm_eval_clean/hellaswag/\\\", \\\"log_path\\\": \\\"/root/entrainment_gated_ft/lm_eval_clean/boolq_hellaswag_eval.log\\\", \\\"metrics\\\": {\\\"benchmarks\\\": [\\\"boolq\\\", \\\"hellaswag\\\"], \\\"boolq\\\": {\\\"n_samples\\\": 3270, \\\"ambiguity_alpha_mean\\\": 0.487, \\\"jaccard_helped_mean\\\": 0.103, \\\"jaccard_hurt_mean\\\": 0.098, \\\"convergence_rho\\\": 0.1, \\\"convergence_p\\\": 0.95, \\\"note\\\": \\\"GDN h24-1 acc=0.489 (near random) is genuine model performance, not eval bug. Selective overlap: GDN-RetNet significant, but GDN-HGRN2 and RetNet-HGRN2 often not significant\\\"}, \\\"hellaswag\\\": {\\\"n_samples\\\": 10042, \\\"ambiguity_alpha_mean\\\": 0.098, \\\"jaccard_helped_mean\\\": 0.091, \\\"jaccard_hurt_mean\\\": 0.08, \\\"convergence_rho\\\": -0.8, \\\"convergence_p\\\": 0.133, \\\"note\\\": \\\"90% samples unanimous across architectures. All Jaccard p<0.001 but nES very small (0.05-0.11)\\\"}, \\\"four_benchmark_summary\\\": {\\\"spectrum\\\": \\\"HellaSwag(α=0.10) < ARC-Easy(α=0.21) < LAMBADA(α=0.30) < BoolQ(α=0.49)\\\", \\\"key_finding\\\": \\\"Multiplicity varies dramatically by task (10%-49%) while Jaccard overlap stays consistently low (~0.08-0.10). Per-example divergence is universal but magnitude is task-dependent.\\\"}, \\\"artifacts\\\": [\\\"boolq_per_example.json\\\", \\\"boolq_jaccard_analysis.json\\\", \\\"hellaswag_per_example.json\\\", \\\"hellaswag_jaccard_analysis.json\\\"]}, \\\"hypothesis\\\": \\\"BoolQ 和 HellaSwag 的 per-example log_samples 数据扩展 multiplicity 分析到更多 benchmark，验证 per-example predictive multiplicity（α 和 cross-architecture Jaccard divergence）在不同任务类型上的普遍性——建立从 LAMBADA/ARC-Easy 到 4-benchmark spectrum 的泛化\\\", \\\"parent\\\": \\\"exp-011\\\", \\\"completed_at\\\": \\\"2026-05-21T08:53:38.336Z\\\"}, \\\"exp-015\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-20T10:05:29.020Z\\\", \\\"updated_at\\\": \\\"2026-05-20T10:06:09.562Z\\\", \\\"hypothesis\\\": \\\"Per-example predictive multiplicity (cross-architecture Jaccard divergence of helped/hurt sets, formal ambiguity α) exists on ARC-Easy (N=2376) even without aggregate convergence, establishing that multiplicity is a general property of hybrid architectures independent of task-specific convergence\\\", \\\"parent\\\": \\\"exp-arc-easy-eval\\\", \\\"spec\\\": {\\\"command\\\": \\\"Python analysis on westb-48145 (CPU)\\\", \\\"server\\\": \\\"westb-48145\\\", \\\"data_path\\\": \\\"/root/entrainment_gated_ft/lm_eval_clean/arc_easy/\\\", \\\"data_count\\\": 2376, \\\"model_name\\\": \\\"GDN/RetNet/HGRN2 x 5 ratios (15 models)\\\", \\\"seed\\\": \\\"N/A (deterministic eval)\\\", \\\"checkpoint_source\\\": \\\"exp-arc-easy-eval\\\", \\\"eval_data\\\": \\\"ARC-Easy (2376 samples)\\\"}, \\\"conclusion\\\": \\\"success\\\", \\\"checkpoint_path\\\": \\\"/root/entrainment_gated_ft/lm_eval_clean/arc_easy/\\\", \\\"log_path\\\": \\\"/root/entrainment_gated_ft/lm_eval_clean/arc_easy/\\\", \\\"completed_at\\\": \\\"2026-05-20T10:06:01.194Z\\\", \\\"metrics\\\": {\\\"benchmark\\\": \\\"arc_easy\\\", \\\"n_samples\\\": 2376, \\\"convergence\\\": {\\\"spearman_rho\\\": -0.2, \\\"p_exact\\\": 0.783, \\\"significant\\\": false}, \\\"jaccard_range\\\": {\\\"helped\\\": [0.067, 0.117], \\\"hurt\\\": [0.079, 0.134]}, \\\"normalized_ES_range\\\": [0.035, 0.135], \\\"all_24_jaccard_above_null\\\": true, \\\"multiplicity_arc_easy\\\": {\\\"alpha_range\\\": [0.201, 0.226], \\\"delta_range\\\": [2.32, 3.12]}, \\\"multiplicity_lambada\\\": {\\\"alpha_range\\\": [0.294, 0.316], \\\"delta_range\\\": [0.53, 0.61]}, \\\"claim\\\": \\\"Claim 3: per-example predictive multiplicity is general\\\", \\\"artifacts\\\": [\\\"arc_easy_per_example.json\\\", \\\"arc_easy_jaccard_analysis.json\\\", \\\"formal_multiplicity_metrics.json\\\"]}}, \\\"exp-arc-easy-eval\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-20T06:08:47.284Z\\\", \\\"updated_at\\\": \\\"2026-05-20T09:46:49.153Z\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/entrainment_gated_ft && bash run_arc_easy_all.sh\\\\\\\"\\\", \\\"server\\\": \\\"westb-48145\\\", \\\"gpu\\\": [\\\"cuda:0\\\"], \\\"pid\\\": \\\"620603\\\", \\\"log_path\\\": \\\"~/runs/entrainment_gated_ft/exp-arc-easy-eval.log\\\", \\\"submitted_at\\\": \\\"2026-05-20T06:08:47.244Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"wall_clock_seconds\\\": 11793.6, \\\"gpu_hours\\\": 3.28}, \\\"hypothesis\\\": \\\"Per-example divergence (low cross-architecture Jaccard of helped/hurt sets) exists on ARC-Easy as well as LAMBADA, establishing that per-example underspecification is not task-specific even when aggregate convergence is absent\\\", \\\"parent\\\": \\\"exp-001\\\", \\\"conclusion\\\": \\\"success\\\", \\\"checkpoint_path\\\": \\\"/root/entrainment_gated_ft/lm_eval_clean/arc_easy/\\\", \\\"log_path\\\": \\\"/root/entrainment_gated_ft/lm_eval_clean/arc_easy/\\\", \\\"completed_at\\\": \\\"2026-05-20T09:25:20.825Z\\\", \\\"metrics\\\": {\\\"benchmark\\\": \\\"arc_easy\\\", \\\"n_samples\\\": 2376, \\\"models_completed\\\": \\\"15/15\\\", \\\"acc_range\\\": [0.6961, 0.7412], \\\"convergence\\\": {\\\"spearman_rho\\\": -0.2, \\\"p_exact\\\": 0.783, \\\"significant\\\": false, \\\"sigma_pure\\\": 0.0964, \\\"sigma_h3_1\\\": 0.099}, \\\"jaccard_range\\\": {\\\"helped\\\": [0.067, 0.117], \\\"hurt\\\": [0.079, 0.134]}, \\\"normalized_ES_range\\\": [0.035, 0.135], \\\"all_24_jaccard_above_null\\\": true, \\\"multiplicity\\\": {\\\"alpha_range\\\": [0.201, 0.226], \\\"delta_range\\\": [2.32, 3.12]}, \\\"lambada_multiplicity\\\": {\\\"alpha_range\\\": [0.294, 0.316], \\\"delta_range\\\": [0.53, 0.61]}, \\\"key_finding\\\": \\\"Per-example multiplicity exists on ARC-Easy (alpha~0.21, Jaccard~0.07-0.13) WITHOUT aggregate convergence (rho=-0.20,p=0.78). Combined with LAMBADA (alpha~0.30 WITH convergence), per-example multiplicity is a general property not tied to convergence.\\\", \\\"artifacts\\\": [\\\"arc_easy_per_example.json\\\", \\\"arc_easy_jaccard_analysis.json\\\", \\\"formal_multiplicity_metrics.json\\\"]}}, \\\"exp-007\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-19T17:08:19.724Z\\\", \\\"updated_at\\\": \\\"2026-05-19T18:53:42.640Z\\\", \\\"hypothesis\\\": \\\"340M models show non-monotonic rebound in cross-architecture convergence at high attention ratios on LAMBADA, caused by capacity-limited interaction between attention and recurrent components — the rebound mechanism differs from 1.3B's complete convergence, establishing scale as a necessary condition for full equalization\\\", \\\"parent\\\": \\\"exp-001\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash run_exp007_logsamples.sh (run_lmeval_clean.py with allow_neg_eigval=True, --log_samples, --tasks lambada_openai)\\\", \\\"server\\\": \\\"westb-48145\\\", \\\"gpu\\\": \\\"cuda:0\\\", \\\"pid\\\": 530432, \\\"log_path\\\": \\\"~/runs/entrainment_gated_ft/exp-007.log\\\", \\\"submitted_at\\\": \\\"2026-05-19T17:51:40.355Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"data_path\\\": \\\"lambada_openai (lm-eval built-in)\\\", \\\"data_count\\\": \\\"5153 per model x 27 models\\\", \\\"model_name\\\": \\\"340M x16 + 1.3B x11 (GDN/RetNet/HGRN2 hybrids + Transformer)\\\", \\\"seed\\\": \\\"default\\\", \\\"checkpoint_source\\\": \\\"m-a-p pretrained (340M: /root/autodl-tmp/models/, 1.3B: /root/autodl-tmp/models_1.3b/)\\\", \\\"eval_data\\\": \\\"lambada_openai (lm-eval built-in, 5153 samples)\\\", \\\"checkpoint_path\\\": \\\"/root/entrainment_gated_ft/lm_eval_clean/exp007/\\\", \\\"wall_clock_seconds\\\": 3722.3, \\\"gpu_hours\\\": 1.03}, \\\"reproduce\\\": {\\\"finished_at\\\": \\\"2026-05-19T18:49:39.310Z\\\"}, \\\"extra\\\": {\\\"hook_events\\\": [{\\\"event\\\": \\\"on_complete\\\", \\\"action\\\": \\\"agent\\\", \\\"ts\\\": \\\"2026-05-19T18:49:41.012664+00:00\\\"}]}, \\\"metrics\\\": {\\\"340m_cross_arch_std\\\": {\\\"pure\\\": 0.02481, \\\"h24-1\\\": 0.011647, \\\"h12-1\\\": 0.017833, \\\"h6-1\\\": 0.011035, \\\"h3-1\\\": 0.016004}, \\\"340m_spearman_rho\\\": -0.5, \\\"340m_spearman_perm_p\\\": 0.45, \\\"1.3b_spearman_rho_ref\\\": -1, \\\"1.3b_spearman_perm_p_ref\\\": 0.0167, \\\"rebound_h3_1_delta\\\": 0.004969, \\\"rebound_h12_1_delta\\\": 0.006186, \\\"340m_h3_1_helped_jaccard\\\": 0.0944, \\\"340m_h3_1_hurt_jaccard\\\": 0.0899, \\\"models_completed\\\": 26, \\\"models_skipped\\\": 1}, \\\"conclusion\\\": \\\"success\\\", \\\"completed_at\\\": \\\"2026-05-19T18:53:42.640Z\\\"}, \\\"exp-004-r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-19T16:58:01.256Z\\\", \\\"updated_at\\\": \\\"2026-05-19T17:17:20.215Z\\\", \\\"hypothesis\\\": \\\"Attention weight patterns in hybrid h3-1 models differ systematically between helped and hurt samples on LAMBADA, with cross-architecture attention pattern similarity lower than expected given aggregate convergence — providing mechanistic evidence for architecture-specific per-example effects (Claim 3)\\\", \\\"parent\\\": \\\"exp-004\\\", \\\"spec\\\": {\\\"command\\\": \\\"python -u analysis/extract_attention_weights.py --arch {gdn,retnet,hgrn2} --device cuda:0 (sequential per arch)\\\", \\\"server\\\": \\\"westb-48145\\\", \\\"data_path\\\": \\\"EleutherAI/lambada_openai (default, split=test, cached)\\\", \\\"data_count\\\": 5153, \\\"model_name\\\": \\\"1.3B-100B-{GatedDeltaNet,RetNet,HGRN2}-hybrid-3-1\\\", \\\"seed\\\": 0, \\\"gpu\\\": \\\"cuda:0 (RTX PRO 6000)\\\", \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/models_1.3b/\\\", \\\"eval_data\\\": \\\"LAMBADA OpenAI (5153 samples)\\\", \\\"log_path\\\": \\\"/tmp/exp004.log\\\", \\\"pid\\\": 517172, \\\"output_dir\\\": \\\"/root/entrainment_gated_ft/analysis/attention_weights/\\\", \\\"progress\\\": \\\"gdn=DONE, retnet=42% running (PID 517172), hgrn2=PENDING\\\", \\\"session\\\": \\\"process detached with fd redirect to /tmp/exp004.log; tmux unavailable on server; screen available for hgrn2\\\", \\\"checkpoint_path\\\": \\\"/root/entrainment_gated_ft/analysis/attention_weights/\\\"}, \\\"conclusion\\\": \\\"success\\\", \\\"completed_at\\\": \\\"2026-05-19T17:17:10.232Z\\\", \\\"metrics\\\": {\\\"helped_vs_hurt_entropy_diff\\\": {\\\"gdn\\\": -0.0009, \\\"retnet\\\": 0.0179, \\\"hgrn2\\\": 0.002}, \\\"helped_vs_hurt_last5_mass\\\": {\\\"gdn_helped\\\": 0.0834, \\\"gdn_hurt\\\": 0.0831, \\\"retnet_helped\\\": 0.1578, \\\"retnet_hurt\\\": 0.1591, \\\"hgrn2_helped\\\": 0.0453, \\\"hgrn2_hurt\\\": 0.0467}, \\\"cross_arch_similarity_mean\\\": {\\\"gdn_vs_retnet\\\": 0.905, \\\"gdn_vs_hgrn2\\\": 0.766, \\\"hgrn2_vs_retnet\\\": 0.698}, \\\"cross_arch_similarity_deep_layers\\\": {\\\"gdn_vs_retnet_L20\\\": 0.986, \\\"gdn_vs_hgrn2_L20\\\": 0.942, \\\"hgrn2_vs_retnet_L20\\\": 0.943}, \\\"cross_arch_similarity_early_layers\\\": {\\\"gdn_vs_retnet_L2\\\": 0.995, \\\"gdn_vs_hgrn2_L2\\\": 0.244, \\\"hgrn2_vs_retnet_L2\\\": 0.196}, \\\"finding\\\": \\\"Attention entropy does NOT differentiate helped vs hurt samples — differences are negligible across all 3 architectures. Cross-arch: GDN and RetNet highly similar throughout; HGRN2 diverges in early layers but converges in deep layers (>0.94 at L20). The per-example effect is not visible at the attention pattern level.\\\", \\\"n_samples\\\": 5153, \\\"runtime_minutes\\\": 30, \\\"output_files\\\": [\\\"gdn_attention_patterns.pt\\\", \\\"gdn_attention_entropy.csv\\\", \\\"retnet_attention_patterns.pt\\\", \\\"retnet_attention_entropy.csv\\\", \\\"hgrn2_attention_patterns.pt\\\", \\\"hgrn2_attention_entropy.csv\\\", \\\"attention_analysis_summary.json\\\", \\\"cross_arch_attention_similarity.csv\\\", \\\"helped_vs_hurt_entropy.csv\\\"]}}, \\\"exp-011-xstorycloze\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-19T16:18:38.168Z\\\", \\\"updated_at\\\": \\\"2026-05-19T17:00:01.089Z\\\", \\\"hypothesis\\\": \\\"xstorycloze_en (StoryCloze equivalent, context completion task) shows significant cross-architecture convergence with attention ratio, providing a second statistically significant anchor beyond LAMBADA after Bonferroni correction\\\", \\\"parent\\\": \\\"exp-011\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash /root/entrainment_gated_ft/run_xstorycloze_batch.sh (PID 497694)\\\", \\\"server\\\": \\\"westb-48145\\\", \\\"data_path\\\": \\\"/root/autodl-tmp/models_1.3b/ (16 models)\\\", \\\"data_count\\\": 16, \\\"model_name\\\": \\\"GDN/RetNet/HGRN2 x 5 ratios + Transformer baseline (1.3B)\\\", \\\"seed\\\": 0, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/models_1.3b/ (Wang et al. pretrained)\\\", \\\"eval_data\\\": \\\"xstorycloze_en (juletxara/xstory_cloze, en split)\\\", \\\"gpu\\\": \\\"cuda:0 (RTX PRO 6000)\\\"}, \\\"conclusion\\\": \\\"negative\\\", \\\"checkpoint_path\\\": \\\"/root/entrainment_gated_ft/lm_eval_clean/xstorycloze/\\\", \\\"log_path\\\": \\\"/root/entrainment_gated_ft/nohup.out\\\", \\\"completed_at\\\": \\\"2026-05-19T16:32:04.959Z\\\", \\\"metrics\\\": {\\\"xstorycloze_en\\\": {\\\"rho\\\": -0.6, \\\"raw_p\\\": 0.35, \\\"bonferroni_adj_p_10\\\": 1, \\\"std_pure\\\": 0.0082, \\\"std_h3_1\\\": 0.0055, \\\"convergence_direction\\\": \\\"correct but weak\\\"}, \\\"ten_benchmark_bonferroni\\\": {\\\"significant_count\\\": \\\"0/10\\\", \\\"LAMBADA_adj_p\\\": 0.167, \\\"note\\\": \\\"No benchmark survives 10-benchmark Bonferroni\\\"}, \\\"method\\\": \\\"exact_permutation_test_two_tailed\\\", \\\"conclusion\\\": \\\"xstorycloze_en NOT a second anchor. Convergence is LAMBADA-specific. W1 unresolved via multi-benchmark approach.\\\"}}, \\\"exp-004\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-19T16:41:10.744Z\\\", \\\"updated_at\\\": \\\"2026-05-19T16:57:48.978Z\\\", \\\"hypothesis\\\": \\\"Attention layers in hybrid-3-1 models exhibit systematically different attention patterns (entropy, position distribution) between helped and hurt samples on LAMBADA, revealing how attention mediates the entrainment-gating effect across architectures.\\\", \\\"parent\\\": \\\"exp-003\\\", \\\"spec\\\": {\\\"command\\\": \\\"python extract_attention_weights.py (forward hooks on Q,K, manual softmax(QK^T/√d) with GQA expansion)\\\", \\\"server\\\": \\\"westb-48145\\\", \\\"data_path\\\": \\\"/root/entrainment_gated_ft/lm_eval_clean/lambada_openai per-example data\\\", \\\"data_count\\\": 5153, \\\"model_name\\\": \\\"GDN-h3-1, RetNet-h3-1, HGRN2-h3-1 (1.3B)\\\", \\\"seed\\\": 42, \\\"gpu\\\": \\\"cuda:0\\\", \\\"checkpoint_source\\\": \\\"Wang et al. pretrained weights\\\", \\\"eval_data\\\": \\\"lambada_openai (5153 examples)\\\", \\\"log_path\\\": \\\"/tmp/exp004.log (process died after Worker exited - nohup orphan)\\\", \\\"checkpoint_path\\\": \\\"N/A - process crashed before completion\\\", \\\"failure_reason\\\": \\\"Worker used nohup instead of submit_training_job/tmux; PID 515917 died after Worker exit. GPU idle since ~16:47 UTC.\\\"}, \\\"conclusion\\\": \\\"failed\\\", \\\"completed_at\\\": \\\"2026-05-19T16:57:48.978Z\\\"}, \\\"exp-011\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-19T14:12:29.428Z\\\", \\\"updated_at\\\": \\\"2026-05-19T16:37:27.600Z\\\", \\\"hypothesis\\\": \\\"Cross-architecture variance on additional retrieval-dependent benchmarks (StoryCloze, BoolQ, COPA, PIQA, SciQ) decreases monotonically with attention ratio, providing a second statistically significant anchor (exact permutation p<0.05, two-tailed) beyond LAMBADA after Bonferroni correction\\\", \\\"parent\\\": \\\"exp-001\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash /root/entrainment_gated_ft/run_exp011_batch.sh (nohup PID 474289)\\\", \\\"server\\\": \\\"westb-48145\\\", \\\"data_path\\\": \\\"/root/autodl-tmp/models_1.3b/ (16 models)\\\", \\\"data_count\\\": 16, \\\"model_name\\\": \\\"GDN/RetNet/HGRN2 x 5 ratios + Transformer baseline (1.3B)\\\", \\\"seed\\\": 0, \\\"eval_data\\\": \\\"boolq, copa, piqa, sciq (4 benchmarks x 16 models)\\\", \\\"gpu\\\": \\\"cuda:0 (RTX PRO 6000)\\\", \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/models_1.3b/ (Wang et al. pretrained checkpoints)\\\"}, \\\"conclusion\\\": \\\"negative\\\", \\\"checkpoint_path\\\": \\\"/root/entrainment_gated_ft/lm_eval_clean/exp011/\\\", \\\"log_path\\\": \\\"/root/entrainment_gated_ft/lm_eval_clean/exp011/run_all.log\\\", \\\"completed_at\\\": \\\"2026-05-19T16:14:41.324Z\\\", \\\"metrics\\\": {\\\"boolq\\\": {\\\"rho\\\": 0.2, \\\"raw_p\\\": 0.7833, \\\"bonferroni_adj_p_9\\\": 1, \\\"std_pure\\\": 0.0163, \\\"std_h3_1\\\": 0.0236, \\\"convergence\\\": false}, \\\"piqa\\\": {\\\"rho\\\": -0.5, \\\"raw_p\\\": 0.45, \\\"bonferroni_adj_p_9\\\": 1, \\\"std_pure\\\": 0.0054, \\\"std_h3_1\\\": 0.0034, \\\"convergence\\\": false}, \\\"sciq\\\": {\\\"rho\\\": 0.1, \\\"raw_p\\\": 0.95, \\\"bonferroni_adj_p_9\\\": 1, \\\"std_pure\\\": 0.0087, \\\"std_h3_1\\\": 0.0074, \\\"convergence\\\": false}, \\\"copa_supplementary\\\": {\\\"rho\\\": -0.67, \\\"raw_p\\\": 0.2667, \\\"std_pure\\\": 0.0262, \\\"std_h3_1\\\": 0.0047, \\\"convergence_ratio\\\": 5.57, \\\"note\\\": \\\"supplementary only (n=100), not in main Bonferroni\\\"}, \\\"LAMBADA_recomputed\\\": {\\\"rho\\\": -1, \\\"raw_p\\\": 0.0167, \\\"bonferroni_adj_p_6\\\": 0.1, \\\"bonferroni_adj_p_10\\\": 0.167, \\\"note\\\": \\\"6-Bonf=0.100 (D003 pre-registered); 10-Bonf=0.167; does not survive strict Bonferroni\\\"}, \\\"merged_10benchmark_significant_count\\\": \\\"0/10\\\", \\\"method\\\": \\\"exact_permutation_test_two_tailed\\\", \\\"D009_strategy\\\": \\\"BCa CI [-1.0,-0.7] as primary evidence; 6-Bonf adj_p=0.100 reported honestly; 10-benchmark negative -> task-specificity positive evidence (supplementary); underpowered caveat in Limitations\\\", \\\"D009_prohibited\\\": \\\"NO post-hoc 2-benchmark Bonferroni; NO post-hoc rho<0 subset correction\\\", \\\"conclusion\\\": \\\"No second anchor. Convergence LAMBADA-specific. W1 addressed via task-specificity reframing (D009).\\\"}}, \\\"exp-010\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-19T15:08:21.255Z\\\", \\\"updated_at\\\": \\\"2026-05-19T15:12:28.565Z\\\", \\\"hypothesis\\\": \\\"Aggregate convergence (cross-arch std decreasing with attention ratio) and per-example divergence (low Jaccard of helped/hurt sets) co-evolve as attention ratio increases on LAMBADA — demonstrating underspecification: architectures converge in aggregate performance while helping/hurting almost entirely different samples\\\", \\\"parent\\\": \\\"exp-001\\\", \\\"spec\\\": {\\\"command\\\": \\\"python3 /root/entrainment_gated_ft/analysis/exp010_bridge_analysis.py\\\", \\\"server\\\": \\\"westb-48145\\\", \\\"data_path\\\": \\\"/root/entrainment_gated_ft/lm_eval_clean/\\\", \\\"data_count\\\": 5153, \\\"model_name\\\": \\\"GDN/RetNet/HGRN2 x 5 ratios (1.3B)\\\", \\\"seed\\\": 0, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/models_1.3b/ (Wang et al. pretrained)\\\", \\\"eval_data\\\": \\\"LAMBADA OpenAI per-example logprob (5153 samples)\\\"}, \\\"checkpoint_path\\\": \\\"/root/entrainment_gated_ft/analysis/exp010_bridge_results.csv\\\", \\\"log_path\\\": \\\"/root/entrainment_gated_ft/analysis/exp010_bridge_summary.json\\\", \\\"conclusion\\\": \\\"success\\\", \\\"completed_at\\\": \\\"2026-05-19T15:09:01.266Z\\\", \\\"metrics\\\": {\\\"aggregate_convergence\\\": {\\\"std_pure\\\": 0.024, \\\"std_h24_1\\\": 0.0162, \\\"std_h12_1\\\": 0.0136, \\\"std_h6_1\\\": 0.0061, \\\"std_h3_1\\\": 0.0049, \\\"reduction_ratio\\\": 0.8, \\\"note\\\": \\\"Cross-arch std drops 5x monotonically\\\"}, \\\"per_example_divergence\\\": {\\\"jaccard_helped_range\\\": [0.092, 0.1], \\\"jaccard_hurt_range\\\": [0.081, 0.099], \\\"net_asymmetry_range\\\": [0.013, 0.04], \\\"net_asymmetry_trend\\\": \\\"increasing with attention ratio\\\", \\\"note\\\": \\\"Jaccard saturates at ~0.095 by 4% attention (h24-1), flat thereafter\\\"}, \\\"co_evolution_spearman\\\": {\\\"std_vs_J_helped\\\": {\\\"rho\\\": -0.7, \\\"exact_p\\\": 0.23}, \\\"std_vs_J_hurt\\\": {\\\"rho\\\": -0.8, \\\"exact_p\\\": 0.13}, \\\"CAVEAT\\\": \\\"D008: rho inflated by pure=0 degeneracy (Jaccard=NaN->0). Excluding pure: rho=-0.40, p=0.75. NOT co-evolution.\\\"}, \\\"key_finding\\\": \\\"DECOUPLING (D008): minimal attention (4%) creates per-example specificity (Jaccard saturates ~0.095), gradual attention drives aggregate convergence (sigma 0.024->0.005). Two processes operate on different timescales. Net asymmetry INCREASES (0.013->0.040).\\\", \\\"narrative_constraints\\\": \\\"PROHIBITED: co-evolution, paradoxical coexistence, paradox. USE: decoupling, different timescales.\\\"}}, \\\"exp-001\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-19T13:32:43.793Z\\\", \\\"updated_at\\\": \\\"2026-05-19T15:00:43.856Z\\\", \\\"hypothesis\\\": \\\"Cross-architecture variance (std) on retrieval-dependent tasks decreases monotonically with attention ratio at 1.3B scale, while reasoning-dependent tasks show no convergence — establishing task-specificity as a principled feature of the equalizer effect, not a limitation\\\", \\\"spec\\\": {\\\"command\\\": \\\"python analysis: compute cross-arch std + Spearman rho for 6 benchmarks x 5 attention ratios\\\", \\\"server\\\": \\\"westb-48145\\\", \\\"data_path\\\": \\\"/root/entrainment_gated_ft/lm_eval_clean/ (summary_all_1.3b.csv + 340M results)\\\", \\\"data_count\\\": 26, \\\"model_name\\\": \\\"16x1.3B + 10x340M (GDN/RetNet/HGRN2)\\\", \\\"seed\\\": 0}, \\\"checkpoint_path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/exp-001/data/task_specificity_results.csv\\\", \\\"log_path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/logs/workers/worker_research_wang_differentiation_20260519T130431.log\\\", \\\"conclusion\\\": \\\"success\\\", \\\"completed_at\\\": \\\"2026-05-19T13:33:45.162Z\\\", \\\"metrics\\\": {\\\"LAMBADA\\\": {\\\"rho\\\": -1, \\\"p\\\": 0.0167, \\\"significant\\\": false, \\\"taxonomy\\\": \\\"retrieval-dependent\\\", \\\"note\\\": \\\"exact permutation two-tailed (was 0.008 one-tailed)\\\"}, \\\"HellaSwag\\\": {\\\"rho\\\": 0.3, \\\"p\\\": 0.6833, \\\"significant\\\": false, \\\"taxonomy\\\": \\\"reasoning-dependent\\\"}, \\\"ARC-C\\\": {\\\"rho\\\": 0.6, \\\"p\\\": 0.35, \\\"significant\\\": false, \\\"taxonomy\\\": \\\"reasoning-dependent\\\"}, \\\"Winogrande\\\": {\\\"rho\\\": 0.1, \\\"p\\\": 0.95, \\\"significant\\\": false, \\\"taxonomy\\\": \\\"reasoning-dependent\\\"}, \\\"ARC-Easy\\\": {\\\"rho\\\": -0.7, \\\"p\\\": 0.2333, \\\"significant\\\": false, \\\"taxonomy\\\": \\\"mixed\\\"}, \\\"MMLU\\\": {\\\"rho\\\": -0.7, \\\"p\\\": 0.2333, \\\"significant\\\": false, \\\"taxonomy\\\": \\\"mixed\\\"}, \\\"significant_count\\\": \\\"0/6\\\", \\\"summary\\\": \\\"LAMBADA shows perfect negative correlation (rho=-1.0) but exact permutation two-tailed p=0.0167 (Bonferroni adj-p=0.100, not significant). Reasoning tasks show no convergence. Mixed tasks suggestive but underpowered (n=5).\\\", \\\"method\\\": \\\"exact_permutation_test_two_tailed\\\"}}, \\\"exp-008\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-19T14:12:33.026Z\\\", \\\"updated_at\\\": \\\"2026-05-19T14:28:33.593Z\\\", \\\"hypothesis\\\": \\\"Replacing scipy.stats.spearmanr asymptotic p-values with exact permutation tests (n=5, 120 permutations, two-tailed) corrects the spurious p=1.4e-24 bug; expected: LAMBADA raw p≈0.017, Bonferroni adj-p≈0.100 (not significant), confirming need for additional benchmarks\\\", \\\"parent\\\": \\\"exp-001\\\", \\\"checkpoint_path\\\": \\\"/root/entrainment_gated_ft/analysis/robustness_results.csv\\\", \\\"log_path\\\": \\\"/root/entrainment_gated_ft/analysis/robustness_summary.md\\\", \\\"conclusion\\\": \\\"success\\\", \\\"spec\\\": {\\\"command\\\": \\\"python3 /root/entrainment_gated_ft/analysis/statistical_robustness.py\\\", \\\"server\\\": \\\"westb-48145\\\", \\\"data_path\\\": \\\"/root/entrainment_gated_ft/lm_eval_clean/summary_all_1.3b.csv\\\", \\\"data_count\\\": 15, \\\"model_name\\\": \\\"GDN/HGRN2/RetNet 1.3B (5 attn ratios x 3 archs)\\\", \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"/root/entrainment_gated_ft/lm_eval_clean/summary_all_1.3b.csv\\\", \\\"eval_data\\\": \\\"6 benchmarks x 15 model configs (summary_all_1.3b.csv)\\\"}, \\\"metrics\\\": {\\\"LAMBADA\\\": {\\\"rho\\\": -1, \\\"raw_p\\\": 0.0167, \\\"bonferroni_adj_p\\\": 0.1, \\\"bh_fdr_adj_p\\\": 0.1}, \\\"HellaSwag\\\": {\\\"rho\\\": 0.3, \\\"raw_p\\\": 0.6833, \\\"bonferroni_adj_p\\\": 1, \\\"bh_fdr_adj_p\\\": 0.82}, \\\"WinoGrande\\\": {\\\"rho\\\": 0.1, \\\"raw_p\\\": 0.95, \\\"bonferroni_adj_p\\\": 1, \\\"bh_fdr_adj_p\\\": 0.95}, \\\"ARC-Easy\\\": {\\\"rho\\\": -0.7, \\\"raw_p\\\": 0.2333, \\\"bonferroni_adj_p\\\": 1, \\\"bh_fdr_adj_p\\\": 0.4667}, \\\"ARC-Challenge\\\": {\\\"rho\\\": 0.6, \\\"raw_p\\\": 0.35, \\\"bonferroni_adj_p\\\": 1, \\\"bh_fdr_adj_p\\\": 0.525}, \\\"MMLU\\\": {\\\"rho\\\": -0.7, \\\"raw_p\\\": 0.2333, \\\"bonferroni_adj_p\\\": 1, \\\"bh_fdr_adj_p\\\": 0.4667}, \\\"method\\\": \\\"exact_permutation_test_two_tailed\\\", \\\"n_permutations\\\": 120, \\\"bug_fixed\\\": \\\"scipy.stats.spearmanr asymptotic p replaced with exact permutation\\\", \\\"bootstrap_ci\\\": {\\\"benchmark\\\": \\\"LAMBADA\\\", \\\"method\\\": \\\"architecture_resampling_percentile\\\", \\\"ci_lower\\\": -1, \\\"ci_upper\\\": -0.7, \\\"crosses_zero\\\": false, \\\"n_bootstrap\\\": 10000, \\\"n_valid\\\": 8875, \\\"seed\\\": 42, \\\"p_rho_negative\\\": 1, \\\"p_rho_positive\\\": 0, \\\"bca_note\\\": \\\"BCa degenerate at rho=-1.0 boundary; percentile CI used\\\"}, \\\"gdn_excluded\\\": {\\\"LAMBADA\\\": {\\\"rho\\\": -0.7, \\\"exact_p\\\": 0.2333, \\\"direction\\\": \\\"WEAKER\\\"}, \\\"HellaSwag\\\": {\\\"rho\\\": 0.5, \\\"exact_p\\\": 0.45, \\\"direction\\\": \\\"STRONGER\\\"}, \\\"WinoGrande\\\": {\\\"rho\\\": 0.3, \\\"exact_p\\\": 0.6833, \\\"direction\\\": \\\"STRONGER\\\"}, \\\"ARC-Easy\\\": {\\\"rho\\\": -0.9, \\\"exact_p\\\": 0.0833, \\\"direction\\\": \\\"STRONGER\\\"}, \\\"ARC-Challenge\\\": {\\\"rho\\\": -0.2, \\\"exact_p\\\": 0.7833, \\\"direction\\\": \\\"WEAKER\\\"}, \\\"MMLU\\\": {\\\"rho\\\": 0.6, \\\"exact_p\\\": 0.35, \\\"direction\\\": \\\"WEAKER\\\"}, \\\"note\\\": \\\"ARC-Easy rho improves from -0.7 to -0.9 (p=0.0833) without GDN confound — suggestive second anchor\\\"}}, \\\"completed_at\\\": \\\"2026-05-19T14:18:07.535Z\\\"}, \\\"exp-003-p2v2\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-19T14:13:12.772Z\\\", \\\"updated_at\\\": \\\"2026-05-19T14:20:24.378Z\\\", \\\"hypothesis\\\": \\\"Helped samples have higher pure-model perplexity (model uncertain → attention helped) while hurt samples have lower perplexity (model confident → attention interfered), with architecture-specific patterns across GDN/RetNet/HGRN2. Retry with HGRN2 monkey-patch fix for _tied_weights_keys AttributeError.\\\", \\\"parent\\\": \\\"exp-003-p2\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"exp-003-p2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-19T13:52:59.192Z\\\", \\\"updated_at\\\": \\\"2026-05-19T14:06:41.114Z\\\", \\\"hypothesis\\\": \\\"Helped samples have higher pure-model perplexity (model was uncertain → attention helped), while hurt samples have lower pure-model perplexity (model was confident → attention interfered). This pattern is architecture-specific.\\\", \\\"parent\\\": \\\"exp-003\\\", \\\"spec\\\": {\\\"command\\\": \\\"python3 /root/entrainment_gated_ft/analysis/sample_perplexity_analysis.py\\\", \\\"server\\\": \\\"westb-48145\\\", \\\"data_path\\\": \\\"/root/entrainment_gated_ft/lm_eval_clean\\\", \\\"data_count\\\": 5153, \\\"model_name\\\": \\\"GDN-pure, RetNet-pure, HGRN2-pure (1.3B)\\\", \\\"seed\\\": \\\"N/A\\\", \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/models_1.3b/{GDN,RetNet,HGRN2}-pure\\\", \\\"eval_data\\\": \\\"LAMBADA OpenAI (5153 samples)\\\"}, \\\"conclusion\\\": \\\"negative\\\", \\\"log_path\\\": \\\"/root/entrainment_gated_ft/analysis/sample_perplexity_summary.json\\\", \\\"checkpoint_path\\\": \\\"/root/entrainment_gated_ft/analysis/sample_perplexity_results.csv\\\", \\\"completed_at\\\": \\\"2026-05-19T14:06:38.461Z\\\", \\\"metrics\\\": {\\\"GDN\\\": {\\\"U\\\": 148410, \\\"p\\\": 0.209189, \\\"r_rb\\\": -0.0447, \\\"helped_mean\\\": 3.3695, \\\"hurt_mean\\\": 3.3382}, \\\"RetNet\\\": {\\\"U\\\": 107210, \\\"p\\\": 0.659319, \\\"r_rb\\\": -0.0168, \\\"helped_mean\\\": 3.4432, \\\"hurt_mean\\\": 3.4207}, \\\"HGRN2\\\": {\\\"U\\\": 112999, \\\"p\\\": 0.247856, \\\"r_rb\\\": -0.0441, \\\"helped_mean\\\": 3.3775, \\\"hurt_mean\\\": 3.3538}, \\\"cross_arch_helped_KW_p\\\": 0.020136, \\\"cross_arch_hurt_KW_p\\\": 0.000498}}, \\\"exp-003\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-19T13:38:18.995Z\\\", \\\"updated_at\\\": \\\"2026-05-19T13:38:51.683Z\\\", \\\"hypothesis\\\": \\\"Architecture-specific helped/hurt samples on LAMBADA differ in surface features (token frequency, context length, lexical complexity), AND these feature profiles differ across GDN/HGRN2/RetNet — indicating architecture-specific mechanisms rather than generic attention benefit\\\", \\\"spec\\\": {\\\"command\\\": \\\"python analysis/sample_characterization.py — surface feature analysis of helped/hurt samples\\\", \\\"server\\\": \\\"westb-48145\\\", \\\"data_path\\\": \\\"/root/entrainment_gated_ft/lm_eval_clean/ (per-example logprob data)\\\", \\\"data_count\\\": 5153, \\\"model_name\\\": \\\"GDN/HGRN2/RetNet 1.3B h3-1 vs pure\\\", \\\"seed\\\": 0}, \\\"checkpoint_path\\\": \\\"/root/entrainment_gated_ft/analysis/sample_characterization_results.csv\\\", \\\"log_path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/logs/workers/worker_analysis_exp_003_sample_characterization_20260519T131141.log\\\", \\\"conclusion\\\": \\\"negative\\\", \\\"metrics\\\": {\\\"GDN\\\": {\\\"helped\\\": 462, \\\"hurt\\\": 615, \\\"net\\\": -153, \\\"surface_features_significant\\\": false}, \\\"HGRN2\\\": {\\\"helped\\\": 548, \\\"hurt\\\": 395, \\\"net\\\": 153, \\\"surface_features_significant\\\": false}, \\\"RetNet\\\": {\\\"helped\\\": 426, \\\"hurt\\\": 495, \\\"net\\\": -69, \\\"context_length_p\\\": 0.012, \\\"context_length_r\\\": -0.096, \\\"unique_tokens_p\\\": 0.009, \\\"unique_tokens_r\\\": -0.099}, \\\"cross_arch_difference\\\": \\\"not_significant\\\", \\\"pass_fail\\\": \\\"FAIL — RetNet context_unique_tokens p=0.009 passes criterion 1 for one arch only; criterion 2 (cross-arch difference) fails\\\", \\\"summary\\\": \\\"Surface features do not explain helped/hurt identity. Rules out trivial explanations (frequency, length, diversity). RetNet shows weak context-length signal (p=0.012, r=-0.096).\\\"}, \\\"completed_at\\\": \\\"2026-05-19T13:38:51.683Z\\\"}, \\\"exp-009\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-19T13:32:43.818Z\\\", \\\"updated_at\\\": \\\"2026-05-19T13:33:45.506Z\\\", \\\"hypothesis\\\": \\\"Our equalizer effect analysis provides fully novel contributions relative to Wang et al. (arXiv 2507.06457) across 4 dimensions: convergence quantification (Spearman ρ + permutation test vs qualitative observation), scale dependency (quantitative 1.3B vs 340M contrast vs binary statement), per-example mechanism (Jaccard + net effect analysis vs absent), and task-specificity (convergence-strength by task type vs ratio-sensitivity)\\\", \\\"spec\\\": {\\\"command\\\": \\\"literature analysis: extract Wang et al. (2507.06457) exact claims, compare 4 differentiation dimensions\\\", \\\"server\\\": \\\"local + westb-48145\\\", \\\"data_path\\\": \\\"Wang et al. arXiv 2507.06457 + task_specificity_results.csv\\\", \\\"data_count\\\": 1, \\\"model_name\\\": \\\"N/A (literature analysis)\\\", \\\"seed\\\": 0}, \\\"checkpoint_path\\\": \\\"/root/entrainment_gated_ft/analysis/wang_et_al_differentiation.md\\\", \\\"log_path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/logs/workers/worker_research_exp_009_wang_differentiation_20260519T131120.log\\\", \\\"conclusion\\\": \\\"success\\\", \\\"completed_at\\\": \\\"2026-05-19T13:33:45.506Z\\\"}, \\\"eval_340m_retnet_hgrn2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-19T04:03:58.762Z\\\", \\\"updated_at\\\": \\\"2026-05-19T04:32:37.289Z\\\", \\\"hypothesis\\\": \\\"340M RetNet and HGRN2 models will show the same architecture-dependent attention effect observed at 1.3B scale: HGRN2 benefits from attention while RetNet shows minimal benefit, with task-dependent equalizer effect on LAMBADA\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash /root/entrainment_gated_ft/run_all_340m_eval.sh\\\", \\\"server\\\": \\\"westb-48145\\\", \\\"data_path\\\": \\\"/root/autodl-tmp/models/\\\", \\\"data_count\\\": 10, \\\"model_name\\\": \\\"340M RetNet×5 + HGRN2×5\\\", \\\"seed\\\": 0}, \\\"conclusion\\\": \\\"success\\\", \\\"checkpoint_path\\\": \\\"/root/entrainment_gated_ft/lm_eval_clean/340m/\\\", \\\"log_path\\\": \\\"/root/entrainment_gated_ft/lm_eval_clean/340m/run_all.log\\\", \\\"completed_at\\\": \\\"2026-05-19T04:32:37.289Z\\\"}, \\\"hgrn2_eval_h3_1\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-18T16:47:57.853Z\\\", \\\"updated_at\\\": \\\"2026-05-18T16:53:12.858Z\\\", \\\"spec\\\": {\\\"command\\\": \\\"HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1 python run_lmeval_clean.py --model_path 1.3B-100B-HGRN2-hybrid-3-1 --tasks 6tasks --batch_size 8\\\", \\\"server\\\": \\\"westb-48145\\\", \\\"data_path\\\": \\\"/root/autodl-tmp/models_1.3b/1.3B-100B-HGRN2-hybrid-3-1\\\", \\\"data_count\\\": 1, \\\"model_name\\\": \\\"HGRN2-1.3B-hybrid-3-1\\\", \\\"seed\\\": 0}, \\\"conclusion\\\": \\\"success\\\", \\\"checkpoint_path\\\": \\\"/root/entrainment_gated_ft/lm_eval_clean/1.3B-100B-HGRN2-hybrid-3-1.json\\\", \\\"log_path\\\": \\\"/tmp/hgrn2_eval_h3_1.log\\\", \\\"hypothesis\\\": \\\"HGRN2 hybrid-3-1 (highest attention ratio) will show less degradation on composition-heavy benchmarks compared to pure linear models, following the attention-ratio degradation pattern observed in GDN and RetNet families\\\", \\\"completed_at\\\": \\\"2026-05-18T16:53:12.858Z\\\"}, \\\"hgrn2_eval_1_3b_all\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-18T15:57:15.535Z\\\", \\\"updated_at\\\": \\\"2026-05-18T16:00:12.920Z\\\", \\\"spec\\\": {\\\"command\\\": \\\"python run_lmeval_clean.py --model_path {MODEL} --tasks lambada_openai,hellaswag,winogrande,arc_easy,arc_challenge,mmlu --output_dir lm_eval_clean/ --batch_size 8 (x3 models: hybrid-12-1, hybrid-24-1, hybrid-3-1)\\\", \\\"server\\\": \\\"westb-48145\\\", \\\"data_path\\\": \\\"/root/autodl-tmp/models_1.3b/\\\", \\\"data_count\\\": 3, \\\"model_name\\\": \\\"HGRN2-1.3B (3 hybrid variants)\\\", \\\"seed\\\": 0}, \\\"conclusion\\\": \\\"killed\\\", \\\"completed_at\\\": \\\"2026-05-18T16:00:12.920Z\\\"}}, \\\"count\\\": 40, \\\"total\\\": 40, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.0959}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {\"exp-005-gla-pure\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-22T16:33:56.971Z\", \"updated_at\": \"2026-05-22T16:41:30.660Z\", \"spec\": {\"command\": \"bash -c \\\"source /etc/network_turbo && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_HUB_DISABLE_XET=1 && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && python /root/entrainment_gated_ft/scripts/patch_fla_eval.py --model hf --model_args pretrained=/root/entrainment_gated_ft/models/340M-20B-GLA-pure-baseline,trust_remote_code=True --tasks lambada_openai,arc_easy --device cuda:0 --batch_size auto --log_samples --output_path /root/entrainment_gated_ft/results/exp005_zoo_expansion/GLA_pure/ && echo GLA_PURE_EVAL_DONE\\\"\", \"server\": \"westb-48145\", \"gpu\": [\"cuda:0\"], \"pid\": \"904591\", \"log_path\": \"~/runs/entrainment_gated_ft/exp-005-gla-pure.log\", \"submitted_at\": \"2026-05-22T16:39:54.061Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"reproduce\": {\"finished_at\": \"2026-05-22T16:41:30.660Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-22T16:41:32.936910+00:00\"}]}}, \"exp-005-pure-v5\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-22T16:37:28.872Z\", \"updated_at\": \"2026-05-22T16:37:28.872Z\", \"spec\": {\"command\": \"bash -c \\\"bash /root/entrainment_gated_ft/results/exp005_zoo_expansion/run_pure_v5.sh\\\"\", \"server\": \"westb-48145\", \"gpu\": [\"cuda:0\"], \"pid\": \"904122\", \"log_path\": \"~/runs/entrainment_gated_ft/exp-005-pure-v5.log\", \"submitted_at\": \"2026-05-22T16:37:28.788Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"exp-005-pure-v4\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-22T16:35:11.429Z\", \"updated_at\": \"2026-05-22T16:35:11.429Z\", \"spec\": {\"command\": \"bash -c \\\"bash /root/entrainment_gated_ft/results/exp005_zoo_expansion/run_pure_v4.sh\\\"\", \"server\": \"westb-48145\", \"gpu\": [\"cuda:0\"], \"pid\": \"903338\", \"log_path\": \"~/runs/entrainment_gated_ft/exp-005-pure-v4.log\", \"submitted_at\": \"2026-05-22T16:35:11.341Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"exp-005-pure-v3\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-22T16:32:39.150Z\", \"updated_at\": \"2026-05-22T16:32:39.150Z\", \"spec\": {\"command\": \"bash -c \\\"bash /root/entrainment_gated_ft/results/exp005_zoo_expansion/run_pure_v3.sh\\\"\", \"server\": \"westb-48145\", \"gpu\": [\"cuda:0\"], \"pid\": \"902795\", \"log_path\": \"~/runs/entrainment_gated_ft/exp-005-pure-v3.log\", \"submitted_at\": \"2026-05-22T16:32:39.070Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"exp-005-batch\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-22T16:30:41.446Z\", \"updated_at\": \"2026-05-22T16:31:53.107Z\", \"spec\": {\"command\": \"bash -c \\\"bash /root/entrainment_gated_ft/results/exp005_zoo_expansion/run_eval_download.sh\\\"\", \"server\": \"westb-48145\", \"gpu\": [\"cuda:0\"], \"pid\": \"902349\", \"log_path\": \"~/runs/entrainment_gated_ft/exp-005-batch.log\", \"submitted_at\": \"2026-05-22T16:30:41.362Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"reproduce\": {\"finished_at\": \"2026-05-22T16:31:50.753Z\"}, \"failure_reason\": \"EXIT_CODE=1 (generic error — check log tail)\", \"conclusion\": \"failed\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-22T16:31:55.361162+00:00\"}]}}, \"exp-005-hgrn-chain\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-22T16:27:47.360Z\", \"updated_at\": \"2026-05-22T16:27:47.360Z\", \"spec\": {\"command\": \"bash -c \\\"bash /root/entrainment_gated_ft/results/exp005_zoo_expansion/run_hgrn_chain.sh\\\"\", \"server\": \"westb-48145\", \"gpu\": [\"cuda:0\"], \"pid\": \"902087\", \"log_path\": \"~/runs/entrainment_gated_ft/exp-005-hgrn-chain.log\", \"submitted_at\": \"2026-05-22T16:27:47.270Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"exp-005\": {\"status\": \"PREPARING\", \"retry_count\": 1, \"created_at\": \"2026-05-20T02:26:40.718Z\", \"updated_at\": \"2026-05-22T16:18:38.064Z\", \"hypothesis\": \"Cross-architecture Jaccard overlap of helped/hurt sets will remain significantly above chance when expanded from 3 to 6 linear attention architectures, indicating that attention-mediated sample sensitivity is architecture-independent.\", \"parent\": \"exp-001\", \"completed_at\": \"2026-05-22T14:24:29.103Z\", \"extra\": {\"previous_failure\": {\"conclusion\": \"killed\", \"metrics\": {\"cancel_reason\": \"Wang et al. zoo 仅含 GDN/RetNet/HGRN2，无法扩展 n>3，已由 worker_analysis_arch-extension-check 确认\"}}, \"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-22T15:05:27.711311+00:00\"}]}, \"metrics\": {\"gla_h31_lambada_acc\": 0.3819, \"gla_h31_arc_acc\": 0.5673, \"deltanet_h31_lambada_acc\": 0.3536, \"deltanet_h31_lambada_ppl\": 30.45, \"deltanet_h31_arc_acc\": 0.601, \"fla_patch_needed\": \"scripts/patch_fla_eval.py fixes _tied_weights_keys list→dict for fla 0.5.0 + transformers 5.8.1\"}, \"reproduce\": {\"finished_at\": \"2026-05-22T15:05:23.157Z\"}, \"failure_reason\": \"EXIT_CODE=1 (generic error — check log tail)\", \"conclusion\": \"failed\", \"notes\": \"诊断中: worker_diagnose_exp-005-p1-v4_20260522T150706 正在查日志。日志仅7行，进程在下载 DeltaNet h3-1 模型时 EXIT_CODE=1 退出。\"}, \"exp-005-p1-eval-v5\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-22T16:18:29.815Z\", \"updated_at\": \"2026-05-22T16:18:29.815Z\", \"spec\": {\"command\": \"bash -c \\\"bash /root/entrainment_gated_ft/results/exp005_zoo_expansion/run_eval_p1.sh\\\"\", \"server\": \"westb-48145\", \"gpu\": [\"cuda:0\"], \"pid\": \"898757\", \"log_path\": \"~/runs/entrainment_gated_ft/exp-005-p1-eval-v5.log\", \"submitted_at\": \"2026-05-22T16:18:29.731Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"exp-005-p1-eval-v4\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-22T16:16:34.914Z\", \"updated_at\": \"2026-05-22T16:16:34.914Z\", \"spec\": {\"command\": \"bash -c \\\"bash /root/entrainment_gated_ft/results/exp005_zoo_expansion/run_eval_p1.sh\\\"\", \"server\": \"westb-48145\", \"gpu\": [\"cuda:0\"], \"pid\": \"897689\", \"log_path\": \"~/runs/entrainment_gated_ft/exp-005-p1-eval-v4.log\", \"submitted_at\": \"2026-05-22T16:16:34.836Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"exp-005-dn-eval\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-22T15:56:19.907Z\", \"updated_at\": \"2026-05-22T16:10:46.245Z\", \"spec\": {\"command\": \"bash -c \\\"source /etc/network_turbo && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_HUB_DISABLE_XET=1 && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && cd /root/entrainment_gated_ft && python scripts/patch_fla_eval.py --model hf --model_args pretrained=/root/entrainment_gated_ft/models/340M-20B-DeltaNet-hybrid-3-1,trust_remote_code=True,dtype=float16 --tasks lambada_openai,arc_easy --device cuda:0 --batch_size auto --log_samples --output_path /root/entrainment_gated_ft/results/exp005_zoo_expansion/DeltaNet_hybrid-3-1/ && echo DELTANET_EVAL_DONE\\\"\", \"server\": \"westb-48145\", \"gpu\": [\"cuda:0\"], \"pid\": \"886300\", \"log_path\": \"~/runs/entrainment_gated_ft/exp-005-dn-eval.log\", \"submitted_at\": \"2026-05-22T16:04:02.638Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"metrics\": {\"model\": \"340M-20B-DeltaNet-hybrid-3-1\", \"lambada_openai_acc\": 0.3536, \"lambada_openai_ppl\": 30.45, \"arc_easy_acc\": 0.601, \"arc_easy_acc_norm\": 0.5198, \"status\": \"DONE\"}}, \"exp-005-p1-eval-v3\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-22T16:07:46.157Z\", \"updated_at\": \"2026-05-22T16:07:46.157Z\", \"spec\": {\"command\": \"bash -c \\\"bash /root/entrainment_gated_ft/results/exp005_zoo_expansion/run_eval_p1.sh\\\"\", \"server\": \"westb-48145\", \"gpu\": [\"cuda:0\"], \"pid\": \"891633\", \"log_path\": \"~/runs/entrainment_gated_ft/exp-005-p1-eval-v3.log\", \"submitted_at\": \"2026-05-22T16:07:46.079Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"exp-005-p1-eval-v2\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-22T16:06:40.443Z\", \"updated_at\": \"2026-05-22T16:06:40.443Z\", \"spec\": {\"command\": \"bash -c \\\"bash /root/entrainment_gated_ft/results/exp005_zoo_expansion/run_eval_p1.sh\\\"\", \"server\": \"westb-48145\", \"gpu\": [\"cuda:0\"], \"pid\": \"889541\", \"log_path\": \"~/runs/entrainment_gated_ft/exp-005-p1-eval-v2.log\", \"submitted_at\": \"2026-05-22T16:06:40.369Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"exp-005-p1-eval\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-22T16:01:38.958Z\", \"updated_at\": \"2026-05-22T16:01:38.958Z\", \"spec\": {\"command\": \"bash -c \\\"bash /root/entrainment_gated_ft/results/exp005_zoo_expansion/run_eval_p1.sh\\\"\", \"server\": \"westb-48145\", \"gpu\": [\"cuda:0\"], \"pid\": \"884365\", \"log_path\": \"~/runs/entrainment_gated_ft/exp-005-p1-eval.log\", \"submitted_at\": \"2026-05-22T16:01:38.883Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"exp-005-pure-eval\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-22T15:58:12.656Z\", \"updated_at\": \"2026-05-22T16:01:21.317Z\", \"spec\": {\"command\": \"bash -c \\\"bash /root/entrainment_gated_ft/results/exp005_zoo_expansion/run_wget_eval_pure.sh\\\"\", \"server\": \"westb-48145\", \"gpu\": [\"cuda:0\"], \"pid\": \"884046\", \"log_path\": \"~/runs/entrainment_gated_ft/exp-005-pure-eval.log\", \"submitted_at\": \"2026-05-22T16:01:21.241Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"exp-005-deltanet\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-22T15:51:45.169Z\", \"updated_at\": \"2026-05-22T15:51:45.169Z\", \"spec\": {\"command\": \"bash -c \\\"bash /root/entrainment_gated_ft/results/exp005_zoo_expansion/eval_deltanet_hardcode.sh\\\"\", \"server\": \"westb-48145\", \"gpu\": [\"cuda:0\"], \"pid\": \"881335\", \"log_path\": \"~/runs/entrainment_gated_ft/exp-005-deltanet.log\", \"submitted_at\": \"2026-05-22T15:51:45.096Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"exp-005-gla\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-22T15:41:49.615Z\", \"updated_at\": \"2026-05-22T15:48:24.790Z\", \"spec\": {\"command\": \"bash -c \\\"bash /root/entrainment_gated_ft/results/exp005_zoo_expansion/eval_gla_hardcode.sh\\\"\", \"server\": \"westb-48145\", \"gpu\": [\"cuda:0\"], \"pid\": \"878457\", \"log_path\": \"~/runs/entrainment_gated_ft/exp-005-gla.log\", \"submitted_at\": \"2026-05-22T15:48:24.719Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"exp-005-gla-eval\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-22T15:38:30.968Z\", \"updated_at\": \"2026-05-22T15:44:36.037Z\", \"spec\": {\"command\": \"bash -c \\\"source /etc/network_turbo && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_HUB_DISABLE_XET=1 && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && python -c 'import fla; print(fla.__version__)' && python -m lm_eval --model hf --model_args pretrained=/root/entrainment_gated_ft/models/340M-20B-GLA-hybrid-3-1,trust_remote_code=True --tasks lambada_openai,arc_easy --device cuda:0 --batch_size auto --log_samples --output_path /root/entrainment_gated_ft/results/exp005_zoo_expansion/GLA_hybrid-3-1/ && echo GLA_EVAL_DONE\\\"\", \"server\": \"westb-48145\", \"gpu\": [\"cuda:0\"], \"pid\": \"875395\", \"log_path\": \"~/runs/entrainment_gated_ft/exp-005-gla-eval.log\", \"submitted_at\": \"2026-05-22T15:42:46.005Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"reproduce\": {\"finished_at\": \"2026-05-22T15:43:08.734Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-22T15:39:05.469998+00:00\"}, {\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-22T15:43:12.720582+00:00\"}]}, \"failure_reason\": \"Traceback → ss = CONFIG_MAPPING[config_dict[\\\"model_type\\\"]] ~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^ File \\\"/root/miniconda3/lib/python3.12/site-packages/transformers/models/auto/configuration_auto.py\\\", line 105, in __getitem__ raise KeyError(key) KeyError: 'gla'\", \"conclusion\": \"failed\", \"notes\": \"失败原因已诊断：1) 首次提交 pretrained='' 空字符串（shell 变量展开问题）；2) 重试时 KeyError: 'gla'（transformers AutoModel 不识别 GLA 模型类型，需要 fla 包注册）。模型文件本身完整（340M-20B-GLA-hybrid-3-1/model.safetensors 存在）。worker_fix_exp-005-gla-eval-hardcode 正在创建 wrapper 脚本修复。\"}, \"exp-005-p1-v4\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-22T14:49:36.217Z\", \"updated_at\": \"2026-05-22T14:49:36.217Z\", \"spec\": {\"command\": \"bash -c \\\"bash /root/entrainment_gated_ft/results/exp005_zoo_expansion/run_p1_v4.sh\\\"\", \"server\": \"westb-48145\", \"gpu\": [\"cuda:0\"], \"pid\": \"870648\", \"log_path\": \"~/runs/entrainment_gated_ft/exp-005-p1-v4.log\", \"submitted_at\": \"2026-05-22T14:49:36.151Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"exp-005-eval\": {\"status\": \"PENDING\", \"retry_count\": 0, \"created_at\": \"2026-05-22T14:22:49.860Z\", \"updated_at\": \"2026-05-22T14:25:11.027Z\", \"spec\": {\"command\": \"bash -c '\\nset -eo pipefail\\nsource /etc/network_turbo\\nsource /root/miniconda3/etc/profile.d/conda.sh && conda activate base\\nexport HF_HOME=/root/autodl-tmp/.hf_cache\\nexport HF_HUB_DISABLE_XET=1\\nexport REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt\\nexport SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt\\n\\nMODELS_DIR=\\\"/root/entrainment_gated_ft/models\\\"\\nRESULTS_DIR=\\\"/root/entrainment_gated_ft/results/exp005_zoo_expansion\\\"\\nLOG=\\\"$RESULTS_DIR/run_all.log\\\"\\nmkdir -p \\\"$RESULTS_DIR\\\"\\n\\necho \\\"=== EXP-005 FULL RUN $(date) ===\\\" | tee \\\"$LOG\\\"\\n\\n# Phase 1: Download missing Priority 1 models (GLA already done)\\nfor arch in DeltaNet HGRN; do\\n  MODEL_NAME=\\\"340M-20B-${arch}-hybrid-3-1\\\"\\n  MODEL_DIR=\\\"$MODELS_DIR/$MODEL_NAME\\\"\\n  if [ ! -f \\\"$MODEL_DIR/model.safetensors\\\" ]; then\\n    echo \\\"Downloading $MODEL_NAME ...\\\" | tee -a \\\"$LOG\\\"\\n    rm -rf \\\"$MODEL_DIR\\\"\\n    huggingface-cli download \\\"m-a-p/$MODEL_NAME\\\" --local-dir \\\"$MODEL_DIR\\\" 2>&1 | tail -5 | tee -a \\\"$LOG\\\"\\n    echo \\\"Downloaded $MODEL_NAME $(date)\\\" | tee -a \\\"$LOG\\\"\\n  else\\n    echo \\\"Already have $MODEL_NAME\\\" | tee -a \\\"$LOG\\\"\\n  fi\\ndone\\n\\n# Phase 2: Evaluate Priority 1 (h3-1 x 3 new archs)\\nfor arch in GLA DeltaNet HGRN; do\\n  MODEL_NAME=\\\"340M-20B-${arch}-hybrid-3-1\\\"\\n  MODEL_DIR=\\\"$MODELS_DIR/$MODEL_NAME\\\"\\n  OUT_DIR=\\\"$RESULTS_DIR/${arch}_hybrid-3-1\\\"\\n  echo \\\"EVAL $MODEL_NAME START $(date)\\\" | tee -a \\\"$LOG\\\"\\n  python -m lm_eval \\\\\\n    --model hf \\\\\\n    --model_args pretrained=$MODEL_DIR,trust_remote_code=True \\\\\\n    --tasks lambada_openai,arc_easy \\\\\\n    --device cuda:0 \\\\\\n    --batch_size auto \\\\\\n    --log_samples \\\\\\n    --output_path \\\"$OUT_DIR/\\\" 2>&1 | tail -10 | tee -a \\\"$LOG\\\"\\n  echo \\\"EVAL $MODEL_NAME DONE $(date)\\\" | tee -a \\\"$LOG\\\"\\ndone\\n\\necho \\\"=== PRIORITY 1 COMPLETE $(date) ===\\\" | tee -a \\\"$LOG\\\"\\n\\n# Phase 3: Download + evaluate remaining ratios\\nfor arch in GLA DeltaNet HGRN; do\\n  for ratio in pure-baseline hybrid-24-1 hybrid-12-1 hybrid-6-1; do\\n    MODEL_NAME=\\\"340M-20B-${arch}-${ratio}\\\"\\n    MODEL_DIR=\\\"$MODELS_DIR/$MODEL_NAME\\\"\\n    OUT_DIR=\\\"$RESULTS_DIR/${arch}_${ratio}\\\"\\n\\n    if [ ! -f \\\"$MODEL_DIR/model.safetensors\\\" ]; then\\n      echo \\\"Downloading $MODEL_NAME ...\\\" | tee -a \\\"$LOG\\\"\\n      rm -rf \\\"$MODEL_DIR\\\"\\n      huggingface-cli download \\\"m-a-p/$MODEL_NAME\\\" --local-dir \\\"$MODEL_DIR\\\" 2>&1 | tail -3 | tee -a \\\"$LOG\\\"\\n      if [ ! -f \\\"$MODEL_DIR/model.safetensors\\\" ]; then\\n        ALT_NAME=\\\"340M-20B-${arch}-pure\\\"\\n        if [ \\\"$ratio\\\" = \\\"pure-baseline\\\" ]; then\\n          echo \\\"Trying alternate: $ALT_NAME ...\\\" | tee -a \\\"$LOG\\\"\\n          huggingface-cli download \\\"m-a-p/$ALT_NAME\\\" --local-dir \\\"$MODELS_DIR/$ALT_NAME\\\" 2>&1 | tail -3 | tee -a \\\"$LOG\\\"\\n          MODEL_DIR=\\\"$MODELS_DIR/$ALT_NAME\\\"\\n        fi\\n      fi\\n      echo \\\"Downloaded $(date)\\\" | tee -a \\\"$LOG\\\"\\n    fi\\n\\n    echo \\\"EVAL $MODEL_NAME START $(date)\\\" | tee -a \\\"$LOG\\\"\\n    python -m lm_eval \\\\\\n      --model hf \\\\\\n      --model_args pretrained=$MODEL_DIR,trust_remote_code=True \\\\\\n      --tasks lambada_openai,arc_easy \\\\\\n      --device cuda:0 \\\\\\n      --batch_size auto \\\\\\n      --log_samples \\\\\\n      --output_path \\\"$OUT_DIR/\\\" 2>&1 | tail -10 | tee -a \\\"$LOG\\\"\\n    echo \\\"EVAL $MODEL_NAME DONE $(date)\\\" | tee -a \\\"$LOG\\\"\\n  done\\ndone\\n\\necho \\\"=== ALL EVALUATIONS COMPLETE $(date) ===\\\" | tee -a \\\"$LOG\\\"\\n'\", \"server\": \"westb-48145\", \"gpu\": [\"cuda:0\"], \"pid\": \"unknown\", \"log_path\": \"~/runs/entrainment_gated_ft/exp-005-eval.log\", \"submitted_at\": \"2026-05-22T14:22:49.797Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"reproduce\": {\"finished_at\": \"2026-05-22T14:23:13.448Z\"}, \"failure_reason\": \"EXIT_CODE=1 (generic error — check log tail)\", \"conclusion\": \"killed\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-22T14:23:17.070767+00:00\"}]}, \"hypothesis\": \"Cross-architecture per-example Jaccard (helped/hurt) remains ≤0.10 when expanding from 3 architectures (GDN/RetNet/HGRN2) to 6 (adding GLA/DeltaNet/HGRN), with 15 pairwise comparisons and 720 permutations providing dramatically stronger statistical power.\"}, \"e4-pythia-seed-calibration\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T10:17:05.445Z\", \"updated_at\": \"2026-05-22T11:44:42.532Z\", \"hypothesis\": \"Pythia 70M 9-seed variants 的 within-seed per-example Jaccard (same architecture, different random seed) 显著高于 cross-architecture Jaccard (~0.10), 证明 within-arch overlap >> cross-arch overlap, 即 cross-arch 信号不能被 seed noise 解释。\", \"parent\": \"exp-001\", \"spec\": {\"command\": \"lm_eval --model hf --tasks lambada_openai,arc_easy --log_samples\", \"server\": \"westb-48145\", \"model_name\": \"EleutherAI/pythia-70m-seed{1-9}\", \"seed\": \"1-9\", \"data_path\": \"/root/entrainment_gated_ft/results/e4_pythia_seed/\", \"data_count\": \"5153+2376 per seed × 9 seeds\", \"checkpoint_source\": \"ModelScope CDN\", \"eval_data\": \"lambada_openai + arc_easy\", \"checkpoint_path\": \"/root/autodl-tmp/pythia_weights_70m/seed{1-9}/\", \"log_path\": \"/root/entrainment_gated_ft/results/e4_pythia_seed/eval.log\"}, \"reproduce\": {\"finished_at\": \"2026-05-22T11:10:00.780Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-22T11:10:01.238Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-22T11:10:03.664374+00:00\"}]}, \"metrics\": {\"lambada_J_helped\": 0.273, \"lambada_J_hurt\": 0.393, \"lambada_alpha\": 0.355, \"arc_J_helped\": 0.312, \"arc_alpha\": 0.491, \"cross_arch_ref_J_helped\": 0.1, \"ratio_lambada\": 2.73, \"ratio_arc\": 3.12}}, \"exp-340m-multi-bench\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T22:23:25.467Z\", \"updated_at\": \"2026-05-22T00:34:02.116Z\", \"hypothesis\": \"340M models exhibit α spectrum (per-example ambiguity) consistent with 1.3B across HellaSwag/PIQA/ARC-Easy — establishing scale-invariance of the multiplicity phenomenon beyond the single-benchmark (LAMBADA) evidence in §4.3. If α_340M ≈ α_1.3B per benchmark, cross-scale stability is confirmed; if systematically different, the scale-dependency claim needs qualification.\", \"parent\": \"exp-007\", \"spec\": {\"command\": \"bash run_340m_multi_eval.sh (run_lmeval_clean.py × 15 models × 3 tasks with --log_samples)\", \"server\": \"westb-48145\", \"gpu\": [\"cuda:0\"], \"data_path\": \"/root/entrainment_gated_ft/models/ (15 × 340M models)\", \"data_count\": \"hellaswag=10042, piqa=1838, arc_easy=2376 per model\", \"model_name\": \"GDN/RetNet/HGRN2 × 5 ratios (340M, 15 models)\", \"seed\": \"default\", \"checkpoint_source\": \"/root/entrainment_gated_ft/models/340M-20B-*\", \"eval_data\": \"HellaSwag (10042) + PIQA (1838) + ARC-Easy (2376)\", \"pid\": \"777365\", \"log_path\": \"~/runs/entrainment_gated_ft/exp-340m-multi-bench.log\", \"submitted_at\": \"2026-05-21T22:27:20Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"/root/entrainment_gated_ft/lm_eval_clean/340m_multi/\", \"wall_clock_seconds\": 7602.1, \"gpu_hours\": 2.11}, \"conclusion\": \"success\", \"metrics\": {\"hellaswag_acc_norm\": {\"340m_alpha_all\": 0.334, \"1_3b_alpha_all\": 0.302, \"delta\": 0.031, \"340m_alpha_pure\": 0.167, \"1_3b_alpha_pure\": 0.148, \"340m_J_helped\": 0.084, \"1_3b_J_helped\": 0.095, \"340m_J_hurt\": 0.083, \"1_3b_J_hurt\": 0.085, \"340m_convergence_rho\": 0.4, \"340m_convergence_p\": 0.517}, \"piqa\": {\"340m_alpha_all\": 0.366, \"1_3b_alpha_all\": 0.278, \"delta\": 0.089, \"340m_alpha_pure\": 0.181, \"1_3b_alpha_pure\": 0.143, \"340m_J_helped\": 0.09, \"1_3b_J_helped\": 0.091, \"340m_J_hurt\": 0.085, \"1_3b_J_hurt\": 0.094, \"340m_convergence_rho\": 0.3, \"340m_convergence_p\": 0.683}, \"arc_easy\": {\"340m_alpha_all\": 0.564, \"1_3b_alpha_all\": 0.434, \"delta\": 0.13, \"340m_alpha_pure\": 0.289, \"1_3b_alpha_pure\": 0.205, \"340m_J_helped\": 0.098, \"1_3b_J_helped\": 0.092, \"340m_J_hurt\": 0.103, \"1_3b_J_hurt\": 0.099, \"340m_convergence_rho\": -0.1, \"340m_convergence_p\": 0.95}, \"summary\": {\"mean_delta_alpha_all\": 0.084, \"scenario\": \"B_mixed\", \"pattern_invariant\": true, \"magnitude_scale_dependent\": true}, \"artifacts\": [\"340m_multi_bench_analysis.json\"]}, \"completed_at\": \"2026-05-22T00:34:02.116Z\"}, \"w3-winogrande-piqa-eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T08:28:29.577Z\", \"updated_at\": \"2026-05-21T10:27:33.995Z\", \"spec\": {\"command\": \"bash run_winogrande_piqa_all.sh (run_lmeval_clean.py × 30 tasks)\", \"server\": \"westb-48145\", \"gpu\": [\"cuda:0\"], \"pid\": \"722233\", \"log_path\": \"/root/entrainment_gated_ft/lm_eval_clean/winogrande_piqa_eval.log\", \"submitted_at\": \"2026-05-21T08:28:29.524Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"lm-eval-harness winogrande + piqa\", \"data_count\": \"winogrande=1267, piqa=1838\", \"model_name\": \"GDN/RetNet/HGRN2 × 5 ratios (1.3B)\", \"seed\": \"default\", \"checkpoint_path\": \"artifacts/paper_data/winogrande_per_example.json + piqa_per_example.json\", \"wall_clock_seconds\": 7144.5, \"gpu_hours\": 1.98}, \"hypothesis\": \"WinoGrande + PIQA per-example multiplicity analysis to decouple format (2-choice vs 4-way MC) from task-type as driver of ambiguity α spectrum, addressing Round 5 W3 format confound concern\", \"conclusion\": \"success\", \"metrics\": {\"winogrande\": {\"n_samples\": 1267, \"alpha_pure\": 0.463, \"alpha_range\": [0.409, 0.463], \"convergence_rho\": -0.2, \"convergence_p\": 0.783}, \"piqa\": {\"n_samples\": 1838, \"alpha_pure\": 0.143, \"alpha_range\": [0.132, 0.143], \"convergence_rho\": -0.5, \"convergence_p\": 0.45}, \"format_confound_test\": {\"finding\": \"PIQA (2-choice, α=0.14) vs WinoGrande (2-choice, α=0.46) vs BoolQ (2-choice, α=0.51) — same format, 3.5× α variation. Format confound refuted.\", \"alpha_vs_accuracy_rho\": 0.03, \"alpha_vs_accuracy_p_exact\": 1}, \"artifacts\": [\"winogrande_per_example.json\", \"piqa_per_example.json\", \"winogrande_jaccard_analysis.json\", \"piqa_jaccard_analysis.json\"]}, \"completed_at\": \"2026-05-21T10:27:33.995Z\"}, \"exp-boolq-hellaswag-eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T11:32:21.428Z\", \"updated_at\": \"2026-05-21T08:53:38.336Z\", \"spec\": {\"command\": \"bash run_boolq_hellaswag_all.sh\", \"server\": \"westb-48145\", \"gpu\": [\"cuda:0\"], \"pid\": \"653104\", \"log_path\": \"~/runs/entrainment_gated_ft/exp-boolq-hellaswag-eval.log\", \"submitted_at\": \"2026-05-20T11:32:21.381Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/entrainment_gated_ft/lm_eval_clean/\", \"data_count\": 13312, \"model_name\": \"GDN/RetNet/HGRN2 x 5 ratios + Transformer (15 models)\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/models_1.3b/\", \"eval_data\": \"BoolQ (3270 samples) + HellaSwag (10042 samples)\", \"wall_clock_seconds\": 76877.0, \"gpu_hours\": 21.35}, \"reproduce\": {\"finished_at\": \"2026-05-20T12:47:53.740Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-20T12:47:55.697105+00:00\"}]}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/entrainment_gated_ft/lm_eval_clean/boolq/ + /root/entrainment_gated_ft/lm_eval_clean/hellaswag/\", \"log_path\": \"/root/entrainment_gated_ft/lm_eval_clean/boolq_hellaswag_eval.log\", \"metrics\": {\"benchmarks\": [\"boolq\", \"hellaswag\"], \"boolq\": {\"n_samples\": 3270, \"ambiguity_alpha_mean\": 0.487, \"jaccard_helped_mean\": 0.103, \"jaccard_hurt_mean\": 0.098, \"convergence_rho\": 0.1, \"convergence_p\": 0.95, \"note\": \"GDN h24-1 acc=0.489 (near random) is genuine model performance, not eval bug. Selective overlap: GDN-RetNet significant, but GDN-HGRN2 and RetNet-HGRN2 often not significant\"}, \"hellaswag\": {\"n_samples\": 10042, \"ambiguity_alpha_mean\": 0.098, \"jaccard_helped_mean\": 0.091, \"jaccard_hurt_mean\": 0.08, \"convergence_rho\": -0.8, \"convergence_p\": 0.133, \"note\": \"90% samples unanimous across architectures. All Jaccard p<0.001 but nES very small (0.05-0.11)\"}, \"four_benchmark_summary\": {\"spectrum\": \"HellaSwag(α=0.10) < ARC-Easy(α=0.21) < LAMBADA(α=0.30) < BoolQ(α=0.49)\", \"key_finding\": \"Multiplicity varies dramatically by task (10%-49%) while Jaccard overlap stays consistently low (~0.08-0.10). Per-example divergence is universal but magnitude is task-dependent.\"}, \"artifacts\": [\"boolq_per_example.json\", \"boolq_jaccard_analysis.json\", \"hellaswag_per_example.json\", \"hellaswag_jaccard_analysis.json\"]}, \"hypothesis\": \"BoolQ 和 HellaSwag 的 per-example log_samples 数据扩展 multiplicity 分析到更多 benchmark，验证 per-example predictive multiplicity（α 和 cross-architecture Jaccard divergence）在不同任务类型上的普遍性——建立从 LAMBADA/ARC-Easy 到 4-benchmark spectrum 的泛化\", \"parent\": \"exp-011\", \"completed_at\": \"2026-05-21T08:53:38.336Z\"}, \"exp-015\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T10:05:29.020Z\", \"updated_at\": \"2026-05-20T10:06:09.562Z\", \"hypothesis\": \"Per-example predictive multiplicity (cross-architecture Jaccard divergence of helped/hurt sets, formal ambiguity α) exists on ARC-Easy (N=2376) even without aggregate convergence, establishing that multiplicity is a general property of hybrid architectures independent of task-specific convergence\", \"parent\": \"exp-arc-easy-eval\", \"spec\": {\"command\": \"Python analysis on westb-48145 (CPU)\", \"server\": \"westb-48145\", \"data_path\": \"/root/entrainment_gated_ft/lm_eval_clean/arc_easy/\", \"data_count\": 2376, \"model_name\": \"GDN/RetNet/HGRN2 x 5 ratios (15 models)\", \"seed\": \"N/A (deterministic eval)\", \"checkpoint_source\": \"exp-arc-easy-eval\", \"eval_data\": \"ARC-Easy (2376 samples)\"}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/entrainment_gated_ft/lm_eval_clean/arc_easy/\", \"log_path\": \"/root/entrainment_gated_ft/lm_eval_clean/arc_easy/\", \"completed_at\": \"2026-05-20T10:06:01.194Z\", \"metrics\": {\"benchmark\": \"arc_easy\", \"n_samples\": 2376, \"convergence\": {\"spearman_rho\": -0.2, \"p_exact\": 0.783, \"significant\": false}, \"jaccard_range\": {\"helped\": [0.067, 0.117], \"hurt\": [0.079, 0.134]}, \"normalized_ES_range\": [0.035, 0.135], \"all_24_jaccard_above_null\": true, \"multiplicity_arc_easy\": {\"alpha_range\": [0.201, 0.226], \"delta_range\": [2.32, 3.12]}, \"multiplicity_lambada\": {\"alpha_range\": [0.294, 0.316], \"delta_range\": [0.53, 0.61]}, \"claim\": \"Claim 3: per-example predictive multiplicity is general\", \"artifacts\": [\"arc_easy_per_example.json\", \"arc_easy_jaccard_analysis.json\", \"formal_multiplicity_metrics.json\"]}}, \"exp-arc-easy-eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T06:08:47.284Z\", \"updated_at\": \"2026-05-20T09:46:49.153Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/entrainment_gated_ft && bash run_arc_easy_all.sh\\\"\", \"server\": \"westb-48145\", \"gpu\": [\"cuda:0\"], \"pid\": \"620603\", \"log_path\": \"~/runs/entrainment_gated_ft/exp-arc-easy-eval.log\", \"submitted_at\": \"2026-05-20T06:08:47.244Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 11793.6, \"gpu_hours\": 3.28}, \"hypothesis\": \"Per-example divergence (low cross-architecture Jaccard of helped/hurt sets) exists on ARC-Easy as well as LAMBADA, establishing that per-example underspecification is not task-specific even when aggregate convergence is absent\", \"parent\": \"exp-001\", \"conclusion\": \"success\", \"checkpoint_path\": \"/root/entrainment_gated_ft/lm_eval_clean/arc_easy/\", \"log_path\": \"/root/entrainment_gated_ft/lm_eval_clean/arc_easy/\", \"completed_at\": \"2026-05-20T09:25:20.825Z\", \"metrics\": {\"benchmark\": \"arc_easy\", \"n_samples\": 2376, \"models_completed\": \"15/15\", \"acc_range\": [0.6961, 0.7412], \"convergence\": {\"spearman_rho\": -0.2, \"p_exact\": 0.783, \"significant\": false, \"sigma_pure\": 0.0964, \"sigma_h3_1\": 0.099}, \"jaccard_range\": {\"helped\": [0.067, 0.117], \"hurt\": [0.079, 0.134]}, \"normalized_ES_range\": [0.035, 0.135], \"all_24_jaccard_above_null\": true, \"multiplicity\": {\"alpha_range\": [0.201, 0.226], \"delta_range\": [2.32, 3.12]}, \"lambada_multiplicity\": {\"alpha_range\": [0.294, 0.316], \"delta_range\": [0.53, 0.61]}, \"key_finding\": \"Per-example multiplicity exists on ARC-Easy (alpha~0.21, Jaccard~0.07-0.13) WITHOUT aggregate convergence (rho=-0.20,p=0.78). Combined with LAMBADA (alpha~0.30 WITH convergence), per-example multiplicity is a general property not tied to convergence.\", \"artifacts\": [\"arc_easy_per_example.json\", \"arc_easy_jaccard_analysis.json\", \"formal_multiplicity_metrics.json\"]}}, \"exp-007\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T17:08:19.724Z\", \"updated_at\": \"2026-05-19T18:53:42.640Z\", \"hypothesis\": \"340M models show non-monotonic rebound in cross-architecture convergence at high attention ratios on LAMBADA, caused by capacity-limited interaction between attention and recurrent components — the rebound mechanism differs from 1.3B's complete convergence, establishing scale as a necessary condition for full equalization\", \"parent\": \"exp-001\", \"spec\": {\"command\": \"bash run_exp007_logsamples.sh (run_lmeval_clean.py with allow_neg_eigval=True, --log_samples, --tasks lambada_openai)\", \"server\": \"westb-48145\", \"gpu\": \"cuda:0\", \"pid\": 530432, \"log_path\": \"~/runs/entrainment_gated_ft/exp-007.log\", \"submitted_at\": \"2026-05-19T17:51:40.355Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"lambada_openai (lm-eval built-in)\", \"data_count\": \"5153 per model x 27 models\", \"model_name\": \"340M x16 + 1.3B x11 (GDN/RetNet/HGRN2 hybrids + Transformer)\", \"seed\": \"default\", \"checkpoint_source\": \"m-a-p pretrained (340M: /root/autodl-tmp/models/, 1.3B: /root/autodl-tmp/models_1.3b/)\", \"eval_data\": \"lambada_openai (lm-eval built-in, 5153 samples)\", \"checkpoint_path\": \"/root/entrainment_gated_ft/lm_eval_clean/exp007/\", \"wall_clock_seconds\": 3722.3, \"gpu_hours\": 1.03}, \"reproduce\": {\"finished_at\": \"2026-05-19T18:49:39.310Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-19T18:49:41.012664+00:00\"}]}, \"metrics\": {\"340m_cross_arch_std\": {\"pure\": 0.02481, \"h24-1\": 0.011647, \"h12-1\": 0.017833, \"h6-1\": 0.011035, \"h3-1\": 0.016004}, \"340m_spearman_rho\": -0.5, \"340m_spearman_perm_p\": 0.45, \"1.3b_spearman_rho_ref\": -1, \"1.3b_spearman_perm_p_ref\": 0.0167, \"rebound_h3_1_delta\": 0.004969, \"rebound_h12_1_delta\": 0.006186, \"340m_h3_1_helped_jaccard\": 0.0944, \"340m_h3_1_hurt_jaccard\": 0.0899, \"models_completed\": 26, \"models_skipped\": 1}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-19T18:53:42.640Z\"}, \"exp-004-r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T16:58:01.256Z\", \"updated_at\": \"2026-05-19T17:17:20.215Z\", \"hypothesis\": \"Attention weight patterns in hybrid h3-1 models differ systematically between helped and hurt samples on LAMBADA, with cross-architecture attention pattern similarity lower than expected given aggregate convergence — providing mechanistic evidence for architecture-specific per-example effects (Claim 3)\", \"parent\": \"exp-004\", \"spec\": {\"command\": \"python -u analysis/extract_attention_weights.py --arch {gdn,retnet,hgrn2} --device cuda:0 (sequential per arch)\", \"server\": \"westb-48145\", \"data_path\": \"EleutherAI/lambada_openai (default, split=test, cached)\", \"data_count\": 5153, \"model_name\": \"1.3B-100B-{GatedDeltaNet,RetNet,HGRN2}-hybrid-3-1\", \"seed\": 0, \"gpu\": \"cuda:0 (RTX PRO 6000)\", \"checkpoint_source\": \"/root/autodl-tmp/models_1.3b/\", \"eval_data\": \"LAMBADA OpenAI (5153 samples)\", \"log_path\": \"/tmp/exp004.log\", \"pid\": 517172, \"output_dir\": \"/root/entrainment_gated_ft/analysis/attention_weights/\", \"progress\": \"gdn=DONE, retnet=42% running (PID 517172), hgrn2=PENDING\", \"session\": \"process detached with fd redirect to /tmp/exp004.log; tmux unavailable on server; screen available for hgrn2\", \"checkpoint_path\": \"/root/entrainment_gated_ft/analysis/attention_weights/\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-19T17:17:10.232Z\", \"metrics\": {\"helped_vs_hurt_entropy_diff\": {\"gdn\": -0.0009, \"retnet\": 0.0179, \"hgrn2\": 0.002}, \"helped_vs_hurt_last5_mass\": {\"gdn_helped\": 0.0834, \"gdn_hurt\": 0.0831, \"retnet_helped\": 0.1578, \"retnet_hurt\": 0.1591, \"hgrn2_helped\": 0.0453, \"hgrn2_hurt\": 0.0467}, \"cross_arch_similarity_mean\": {\"gdn_vs_retnet\": 0.905, \"gdn_vs_hgrn2\": 0.766, \"hgrn2_vs_retnet\": 0.698}, \"cross_arch_similarity_deep_layers\": {\"gdn_vs_retnet_L20\": 0.986, \"gdn_vs_hgrn2_L20\": 0.942, \"hgrn2_vs_retnet_L20\": 0.943}, \"cross_arch_similarity_early_layers\": {\"gdn_vs_retnet_L2\": 0.995, \"gdn_vs_hgrn2_L2\": 0.244, \"hgrn2_vs_retnet_L2\": 0.196}, \"finding\": \"Attention entropy does NOT differentiate helped vs hurt samples — differences are negligible across all 3 architectures. Cross-arch: GDN and RetNet highly similar throughout; HGRN2 diverges in early layers but converges in deep layers (>0.94 at L20). The per-example effect is not visible at the attention pattern level.\", \"n_samples\": 5153, \"runtime_minutes\": 30, \"output_files\": [\"gdn_attention_patterns.pt\", \"gdn_attention_entropy.csv\", \"retnet_attention_patterns.pt\", \"retnet_attention_entropy.csv\", \"hgrn2_attention_patterns.pt\", \"hgrn2_attention_entropy.csv\", \"attention_analysis_summary.json\", \"cross_arch_attention_similarity.csv\", \"helped_vs_hurt_entropy.csv\"]}}, \"exp-011-xstorycloze\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T16:18:38.168Z\", \"updated_at\": \"2026-05-19T17:00:01.089Z\", \"hypothesis\": \"xstorycloze_en (StoryCloze equivalent, context completion task) shows significant cross-architecture convergence with attention ratio, providing a second statistically significant anchor beyond LAMBADA after Bonferroni correction\", \"parent\": \"exp-011\", \"spec\": {\"command\": \"bash /root/entrainment_gated_ft/run_xstorycloze_batch.sh (PID 497694)\", \"server\": \"westb-48145\", \"data_path\": \"/root/autodl-tmp/models_1.3b/ (16 models)\", \"data_count\": 16, \"model_name\": \"GDN/RetNet/HGRN2 x 5 ratios + Transformer baseline (1.3B)\", \"seed\": 0, \"checkpoint_source\": \"/root/autodl-tmp/models_1.3b/ (Wang et al. pretrained)\", \"eval_data\": \"xstorycloze_en (juletxara/xstory_cloze, en split)\", \"gpu\": \"cuda:0 (RTX PRO 6000)\"}, \"conclusion\": \"negative\", \"checkpoint_path\": \"/root/entrainment_gated_ft/lm_eval_clean/xstorycloze/\", \"log_path\": \"/root/entrainment_gated_ft/nohup.out\", \"completed_at\": \"2026-05-19T16:32:04.959Z\", \"metrics\": {\"xstorycloze_en\": {\"rho\": -0.6, \"raw_p\": 0.35, \"bonferroni_adj_p_10\": 1, \"std_pure\": 0.0082, \"std_h3_1\": 0.0055, \"convergence_direction\": \"correct but weak\"}, \"ten_benchmark_bonferroni\": {\"significant_count\": \"0/10\", \"LAMBADA_adj_p\": 0.167, \"note\": \"No benchmark survives 10-benchmark Bonferroni\"}, \"method\": \"exact_permutation_test_two_tailed\", \"conclusion\": \"xstorycloze_en NOT a second anchor. Convergence is LAMBADA-specific. W1 unresolved via multi-benchmark approach.\"}}, \"exp-004\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T16:41:10.744Z\", \"updated_at\": \"2026-05-19T16:57:48.978Z\", \"hypothesis\": \"Attention layers in hybrid-3-1 models exhibit systematically different attention patterns (entropy, position distribution) between helped and hurt samples on LAMBADA, revealing how attention mediates the entrainment-gating effect across architectures.\", \"parent\": \"exp-003\", \"spec\": {\"command\": \"python extract_attention_weights.py (forward hooks on Q,K, manual softmax(QK^T/√d) with GQA expansion)\", \"server\": \"westb-48145\", \"data_path\": \"/root/entrainment_gated_ft/lm_eval_clean/lambada_openai per-example data\", \"data_count\": 5153, \"model_name\": \"GDN-h3-1, RetNet-h3-1, HGRN2-h3-1 (1.3B)\", \"seed\": 42, \"gpu\": \"cuda:0\", \"checkpoint_source\": \"Wang et al. pretrained weights\", \"eval_data\": \"lambada_openai (5153 examples)\", \"log_path\": \"/tmp/exp004.log (process died after Worker exited - nohup orphan)\", \"checkpoint_path\": \"N/A - process crashed before completion\", \"failure_reason\": \"Worker used nohup instead of submit_training_job/tmux; PID 515917 died after Worker exit. GPU idle since ~16:47 UTC.\"}, \"conclusion\": \"failed\", \"completed_at\": \"2026-05-19T16:57:48.978Z\"}, \"exp-011\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T14:12:29.428Z\", \"updated_at\": \"2026-05-19T16:37:27.600Z\", \"hypothesis\": \"Cross-architecture variance on additional retrieval-dependent benchmarks (StoryCloze, BoolQ, COPA, PIQA, SciQ) decreases monotonically with attention ratio, providing a second statistically significant anchor (exact permutation p<0.05, two-tailed) beyond LAMBADA after Bonferroni correction\", \"parent\": \"exp-001\", \"spec\": {\"command\": \"bash /root/entrainment_gated_ft/run_exp011_batch.sh (nohup PID 474289)\", \"server\": \"westb-48145\", \"data_path\": \"/root/autodl-tmp/models_1.3b/ (16 models)\", \"data_count\": 16, \"model_name\": \"GDN/RetNet/HGRN2 x 5 ratios + Transformer baseline (1.3B)\", \"seed\": 0, \"eval_data\": \"boolq, copa, piqa, sciq (4 benchmarks x 16 models)\", \"gpu\": \"cuda:0 (RTX PRO 6000)\", \"checkpoint_source\": \"/root/autodl-tmp/models_1.3b/ (Wang et al. pretrained checkpoints)\"}, \"conclusion\": \"negative\", \"checkpoint_path\": \"/root/entrainment_gated_ft/lm_eval_clean/exp011/\", \"log_path\": \"/root/entrainment_gated_ft/lm_eval_clean/exp011/run_all.log\", \"completed_at\": \"2026-05-19T16:14:41.324Z\", \"metrics\": {\"boolq\": {\"rho\": 0.2, \"raw_p\": 0.7833, \"bonferroni_adj_p_9\": 1, \"std_pure\": 0.0163, \"std_h3_1\": 0.0236, \"convergence\": false}, \"piqa\": {\"rho\": -0.5, \"raw_p\": 0.45, \"bonferroni_adj_p_9\": 1, \"std_pure\": 0.0054, \"std_h3_1\": 0.0034, \"convergence\": false}, \"sciq\": {\"rho\": 0.1, \"raw_p\": 0.95, \"bonferroni_adj_p_9\": 1, \"std_pure\": 0.0087, \"std_h3_1\": 0.0074, \"convergence\": false}, \"copa_supplementary\": {\"rho\": -0.67, \"raw_p\": 0.2667, \"std_pure\": 0.0262, \"std_h3_1\": 0.0047, \"convergence_ratio\": 5.57, \"note\": \"supplementary only (n=100), not in main Bonferroni\"}, \"LAMBADA_recomputed\": {\"rho\": -1, \"raw_p\": 0.0167, \"bonferroni_adj_p_6\": 0.1, \"bonferroni_adj_p_10\": 0.167, \"note\": \"6-Bonf=0.100 (D003 pre-registered); 10-Bonf=0.167; does not survive strict Bonferroni\"}, \"merged_10benchmark_significant_count\": \"0/10\", \"method\": \"exact_permutation_test_two_tailed\", \"D009_strategy\": \"BCa CI [-1.0,-0.7] as primary evidence; 6-Bonf adj_p=0.100 reported honestly; 10-benchmark negative -> task-specificity positive evidence (supplementary); underpowered caveat in Limitations\", \"D009_prohibited\": \"NO post-hoc 2-benchmark Bonferroni; NO post-hoc rho<0 subset correction\", \"conclusion\": \"No second anchor. Convergence LAMBADA-specific. W1 addressed via task-specificity reframing (D009).\"}}, \"exp-010\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T15:08:21.255Z\", \"updated_at\": \"2026-05-19T15:12:28.565Z\", \"hypothesis\": \"Aggregate convergence (cross-arch std decreasing with attention ratio) and per-example divergence (low Jaccard of helped/hurt sets) co-evolve as attention ratio increases on LAMBADA — demonstrating underspecification: architectures converge in aggregate performance while helping/hurting almost entirely different samples\", \"parent\": \"exp-001\", \"spec\": {\"command\": \"python3 /root/entrainment_gated_ft/analysis/exp010_bridge_analysis.py\", \"server\": \"westb-48145\", \"data_path\": \"/root/entrainment_gated_ft/lm_eval_clean/\", \"data_count\": 5153, \"model_name\": \"GDN/RetNet/HGRN2 x 5 ratios (1.3B)\", \"seed\": 0, \"checkpoint_source\": \"/root/autodl-tmp/models_1.3b/ (Wang et al. pretrained)\", \"eval_data\": \"LAMBADA OpenAI per-example logprob (5153 samples)\"}, \"checkpoint_path\": \"/root/entrainment_gated_ft/analysis/exp010_bridge_results.csv\", \"log_path\": \"/root/entrainment_gated_ft/analysis/exp010_bridge_summary.json\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-19T15:09:01.266Z\", \"metrics\": {\"aggregate_convergence\": {\"std_pure\": 0.024, \"std_h24_1\": 0.0162, \"std_h12_1\": 0.0136, \"std_h6_1\": 0.0061, \"std_h3_1\": 0.0049, \"reduction_ratio\": 0.8, \"note\": \"Cross-arch std drops 5x monotonically\"}, \"per_example_divergence\": {\"jaccard_helped_range\": [0.092, 0.1], \"jaccard_hurt_range\": [0.081, 0.099], \"net_asymmetry_range\": [0.013, 0.04], \"net_asymmetry_trend\": \"increasing with attention ratio\", \"note\": \"Jaccard saturates at ~0.095 by 4% attention (h24-1), flat thereafter\"}, \"co_evolution_spearman\": {\"std_vs_J_helped\": {\"rho\": -0.7, \"exact_p\": 0.23}, \"std_vs_J_hurt\": {\"rho\": -0.8, \"exact_p\": 0.13}, \"CAVEAT\": \"D008: rho inflated by pure=0 degeneracy (Jaccard=NaN->0). Excluding pure: rho=-0.40, p=0.75. NOT co-evolution.\"}, \"key_finding\": \"DECOUPLING (D008): minimal attention (4%) creates per-example specificity (Jaccard saturates ~0.095), gradual attention drives aggregate convergence (sigma 0.024->0.005). Two processes operate on different timescales. Net asymmetry INCREASES (0.013->0.040).\", \"narrative_constraints\": \"PROHIBITED: co-evolution, paradoxical coexistence, paradox. USE: decoupling, different timescales.\"}}, \"exp-001\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T13:32:43.793Z\", \"updated_at\": \"2026-05-19T15:00:43.856Z\", \"hypothesis\": \"Cross-architecture variance (std) on retrieval-dependent tasks decreases monotonically with attention ratio at 1.3B scale, while reasoning-dependent tasks show no convergence — establishing task-specificity as a principled feature of the equalizer effect, not a limitation\", \"spec\": {\"command\": \"python analysis: compute cross-arch std + Spearman rho for 6 benchmarks x 5 attention ratios\", \"server\": \"westb-48145\", \"data_path\": \"/root/entrainment_gated_ft/lm_eval_clean/ (summary_all_1.3b.csv + 340M results)\", \"data_count\": 26, \"model_name\": \"16x1.3B + 10x340M (GDN/RetNet/HGRN2)\", \"seed\": 0}, \"checkpoint_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/exp-001/data/task_specificity_results.csv\", \"log_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/logs/workers/worker_research_wang_differentiation_20260519T130431.log\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-19T13:33:45.162Z\", \"metrics\": {\"LAMBADA\": {\"rho\": -1, \"p\": 0.0167, \"significant\": false, \"taxonomy\": \"retrieval-dependent\", \"note\": \"exact permutation two-tailed (was 0.008 one-tailed)\"}, \"HellaSwag\": {\"rho\": 0.3, \"p\": 0.6833, \"significant\": false, \"taxonomy\": \"reasoning-dependent\"}, \"ARC-C\": {\"rho\": 0.6, \"p\": 0.35, \"significant\": false, \"taxonomy\": \"reasoning-dependent\"}, \"Winogrande\": {\"rho\": 0.1, \"p\": 0.95, \"significant\": false, \"taxonomy\": \"reasoning-dependent\"}, \"ARC-Easy\": {\"rho\": -0.7, \"p\": 0.2333, \"significant\": false, \"taxonomy\": \"mixed\"}, \"MMLU\": {\"rho\": -0.7, \"p\": 0.2333, \"significant\": false, \"taxonomy\": \"mixed\"}, \"significant_count\": \"0/6\", \"summary\": \"LAMBADA shows perfect negative correlation (rho=-1.0) but exact permutation two-tailed p=0.0167 (Bonferroni adj-p=0.100, not significant). Reasoning tasks show no convergence. Mixed tasks suggestive but underpowered (n=5).\", \"method\": \"exact_permutation_test_two_tailed\"}}, \"exp-008\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T14:12:33.026Z\", \"updated_at\": \"2026-05-19T14:28:33.593Z\", \"hypothesis\": \"Replacing scipy.stats.spearmanr asymptotic p-values with exact permutation tests (n=5, 120 permutations, two-tailed) corrects the spurious p=1.4e-24 bug; expected: LAMBADA raw p≈0.017, Bonferroni adj-p≈0.100 (not significant), confirming need for additional benchmarks\", \"parent\": \"exp-001\", \"checkpoint_path\": \"/root/entrainment_gated_ft/analysis/robustness_results.csv\", \"log_path\": \"/root/entrainment_gated_ft/analysis/robustness_summary.md\", \"conclusion\": \"success\", \"spec\": {\"command\": \"python3 /root/entrainment_gated_ft/analysis/statistical_robustness.py\", \"server\": \"westb-48145\", \"data_path\": \"/root/entrainment_gated_ft/lm_eval_clean/summary_all_1.3b.csv\", \"data_count\": 15, \"model_name\": \"GDN/HGRN2/RetNet 1.3B (5 attn ratios x 3 archs)\", \"seed\": 42, \"checkpoint_source\": \"/root/entrainment_gated_ft/lm_eval_clean/summary_all_1.3b.csv\", \"eval_data\": \"6 benchmarks x 15 model configs (summary_all_1.3b.csv)\"}, \"metrics\": {\"LAMBADA\": {\"rho\": -1, \"raw_p\": 0.0167, \"bonferroni_adj_p\": 0.1, \"bh_fdr_adj_p\": 0.1}, \"HellaSwag\": {\"rho\": 0.3, \"raw_p\": 0.6833, \"bonferroni_adj_p\": 1, \"bh_fdr_adj_p\": 0.82}, \"WinoGrande\": {\"rho\": 0.1, \"raw_p\": 0.95, \"bonferroni_adj_p\": 1, \"bh_fdr_adj_p\": 0.95}, \"ARC-Easy\": {\"rho\": -0.7, \"raw_p\": 0.2333, \"bonferroni_adj_p\": 1, \"bh_fdr_adj_p\": 0.4667}, \"ARC-Challenge\": {\"rho\": 0.6, \"raw_p\": 0.35, \"bonferroni_adj_p\": 1, \"bh_fdr_adj_p\": 0.525}, \"MMLU\": {\"rho\": -0.7, \"raw_p\": 0.2333, \"bonferroni_adj_p\": 1, \"bh_fdr_adj_p\": 0.4667}, \"method\": \"exact_permutation_test_two_tailed\", \"n_permutations\": 120, \"bug_fixed\": \"scipy.stats.spearmanr asymptotic p replaced with exact permutation\", \"bootstrap_ci\": {\"benchmark\": \"LAMBADA\", \"method\": \"architecture_resampling_percentile\", \"ci_lower\": -1, \"ci_upper\": -0.7, \"crosses_zero\": false, \"n_bootstrap\": 10000, \"n_valid\": 8875, \"seed\": 42, \"p_rho_negative\": 1, \"p_rho_positive\": 0, \"bca_note\": \"BCa degenerate at rho=-1.0 boundary; percentile CI used\"}, \"gdn_excluded\": {\"LAMBADA\": {\"rho\": -0.7, \"exact_p\": 0.2333, \"direction\": \"WEAKER\"}, \"HellaSwag\": {\"rho\": 0.5, \"exact_p\": 0.45, \"direction\": \"STRONGER\"}, \"WinoGrande\": {\"rho\": 0.3, \"exact_p\": 0.6833, \"direction\": \"STRONGER\"}, \"ARC-Easy\": {\"rho\": -0.9, \"exact_p\": 0.0833, \"direction\": \"STRONGER\"}, \"ARC-Challenge\": {\"rho\": -0.2, \"exact_p\": 0.7833, \"direction\": \"WEAKER\"}, \"MMLU\": {\"rho\": 0.6, \"exact_p\": 0.35, \"direction\": \"WEAKER\"}, \"note\": \"ARC-Easy rho improves from -0.7 to -0.9 (p=0.0833) without GDN confound — suggestive second anchor\"}}, \"completed_at\": \"2026-05-19T14:18:07.535Z\"}, \"exp-003-p2v2\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-19T14:13:12.772Z\", \"updated_at\": \"2026-05-19T14:20:24.378Z\", \"hypothesis\": \"Helped samples have higher pure-model perplexity (model uncertain → attention helped) while hurt samples have lower perplexity (model confident → attention interfered), with architecture-specific patterns across GDN/RetNet/HGRN2. Retry with HGRN2 monkey-patch fix for _tied_weights_keys AttributeError.\", \"parent\": \"exp-003-p2\", \"conclusion\": \"killed\"}, \"exp-003-p2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T13:52:59.192Z\", \"updated_at\": \"2026-05-19T14:06:41.114Z\", \"hypothesis\": \"Helped samples have higher pure-model perplexity (model was uncertain → attention helped), while hurt samples have lower pure-model perplexity (model was confident → attention interfered). This pattern is architecture-specific.\", \"parent\": \"exp-003\", \"spec\": {\"command\": \"python3 /root/entrainment_gated_ft/analysis/sample_perplexity_analysis.py\", \"server\": \"westb-48145\", \"data_path\": \"/root/entrainment_gated_ft/lm_eval_clean\", \"data_count\": 5153, \"model_name\": \"GDN-pure, RetNet-pure, HGRN2-pure (1.3B)\", \"seed\": \"N/A\", \"checkpoint_source\": \"/root/autodl-tmp/models_1.3b/{GDN,RetNet,HGRN2}-pure\", \"eval_data\": \"LAMBADA OpenAI (5153 samples)\"}, \"conclusion\": \"negative\", \"log_path\": \"/root/entrainment_gated_ft/analysis/sample_perplexity_summary.json\", \"checkpoint_path\": \"/root/entrainment_gated_ft/analysis/sample_perplexity_results.csv\", \"completed_at\": \"2026-05-19T14:06:38.461Z\", \"metrics\": {\"GDN\": {\"U\": 148410, \"p\": 0.209189, \"r_rb\": -0.0447, \"helped_mean\": 3.3695, \"hurt_mean\": 3.3382}, \"RetNet\": {\"U\": 107210, \"p\": 0.659319, \"r_rb\": -0.0168, \"helped_mean\": 3.4432, \"hurt_mean\": 3.4207}, \"HGRN2\": {\"U\": 112999, \"p\": 0.247856, \"r_rb\": -0.0441, \"helped_mean\": 3.3775, \"hurt_mean\": 3.3538}, \"cross_arch_helped_KW_p\": 0.020136, \"cross_arch_hurt_KW_p\": 0.000498}}, \"exp-003\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T13:38:18.995Z\", \"updated_at\": \"2026-05-19T13:38:51.683Z\", \"hypothesis\": \"Architecture-specific helped/hurt samples on LAMBADA differ in surface features (token frequency, context length, lexical complexity), AND these feature profiles differ across GDN/HGRN2/RetNet — indicating architecture-specific mechanisms rather than generic attention benefit\", \"spec\": {\"command\": \"python analysis/sample_characterization.py — surface feature analysis of helped/hurt samples\", \"server\": \"westb-48145\", \"data_path\": \"/root/entrainment_gated_ft/lm_eval_clean/ (per-example logprob data)\", \"data_count\": 5153, \"model_name\": \"GDN/HGRN2/RetNet 1.3B h3-1 vs pure\", \"seed\": 0}, \"checkpoint_path\": \"/root/entrainment_gated_ft/analysis/sample_characterization_results.csv\", \"log_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/logs/workers/worker_analysis_exp_003_sample_characterization_20260519T131141.log\", \"conclusion\": \"negative\", \"metrics\": {\"GDN\": {\"helped\": 462, \"hurt\": 615, \"net\": -153, \"surface_features_significant\": false}, \"HGRN2\": {\"helped\": 548, \"hurt\": 395, \"net\": 153, \"surface_features_significant\": false}, \"RetNet\": {\"helped\": 426, \"hurt\": 495, \"net\": -69, \"context_length_p\": 0.012, \"context_length_r\": -0.096, \"unique_tokens_p\": 0.009, \"unique_tokens_r\": -0.099}, \"cross_arch_difference\": \"not_significant\", \"pass_fail\": \"FAIL — RetNet context_unique_tokens p=0.009 passes criterion 1 for one arch only; criterion 2 (cross-arch difference) fails\", \"summary\": \"Surface features do not explain helped/hurt identity. Rules out trivial explanations (frequency, length, diversity). RetNet shows weak context-length signal (p=0.012, r=-0.096).\"}, \"completed_at\": \"2026-05-19T13:38:51.683Z\"}, \"exp-009\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T13:32:43.818Z\", \"updated_at\": \"2026-05-19T13:33:45.506Z\", \"hypothesis\": \"Our equalizer effect analysis provides fully novel contributions relative to Wang et al. (arXiv 2507.06457) across 4 dimensions: convergence quantification (Spearman ρ + permutation test vs qualitative observation), scale dependency (quantitative 1.3B vs 340M contrast vs binary statement), per-example mechanism (Jaccard + net effect analysis vs absent), and task-specificity (convergence-strength by task type vs ratio-sensitivity)\", \"spec\": {\"command\": \"literature analysis: extract Wang et al. (2507.06457) exact claims, compare 4 differentiation dimensions\", \"server\": \"local + westb-48145\", \"data_path\": \"Wang et al. arXiv 2507.06457 + task_specificity_results.csv\", \"data_count\": 1, \"model_name\": \"N/A (literature analysis)\", \"seed\": 0}, \"checkpoint_path\": \"/root/entrainment_gated_ft/analysis/wang_et_al_differentiation.md\", \"log_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/logs/workers/worker_research_exp_009_wang_differentiation_20260519T131120.log\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-19T13:33:45.506Z\"}, \"eval_340m_retnet_hgrn2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T04:03:58.762Z\", \"updated_at\": \"2026-05-19T04:32:37.289Z\", \"hypothesis\": \"340M RetNet and HGRN2 models will show the same architecture-dependent attention effect observed at 1.3B scale: HGRN2 benefits from attention while RetNet shows minimal benefit, with task-dependent equalizer effect on LAMBADA\", \"spec\": {\"command\": \"bash /root/entrainment_gated_ft/run_all_340m_eval.sh\", \"server\": \"westb-48145\", \"data_path\": \"/root/autodl-tmp/models/\", \"data_count\": 10, \"model_name\": \"340M RetNet×5 + HGRN2×5\", \"seed\": 0}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/entrainment_gated_ft/lm_eval_clean/340m/\", \"log_path\": \"/root/entrainment_gated_ft/lm_eval_clean/340m/run_all.log\", \"completed_at\": \"2026-05-19T04:32:37.289Z\"}, \"hgrn2_eval_h3_1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T16:47:57.853Z\", \"updated_at\": \"2026-05-18T16:53:12.858Z\", \"spec\": {\"command\": \"HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1 python run_lmeval_clean.py --model_path 1.3B-100B-HGRN2-hybrid-3-1 --tasks 6tasks --batch_size 8\", \"server\": \"westb-48145\", \"data_path\": \"/root/autodl-tmp/models_1.3b/1.3B-100B-HGRN2-hybrid-3-1\", \"data_count\": 1, \"model_name\": \"HGRN2-1.3B-hybrid-3-1\", \"seed\": 0}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/entrainment_gated_ft/lm_eval_clean/1.3B-100B-HGRN2-hybrid-3-1.json\", \"log_path\": \"/tmp/hgrn2_eval_h3_1.log\", \"hypothesis\": \"HGRN2 hybrid-3-1 (highest attention ratio) will show less degradation on composition-heavy benchmarks compared to pure linear models, following the attention-ratio degradation pattern observed in GDN and RetNet families\", \"completed_at\": \"2026-05-18T16:53:12.858Z\"}, \"hgrn2_eval_1_3b_all\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T15:57:15.535Z\", \"updated_at\": \"2026-05-18T16:00:12.920Z\", \"spec\": {\"command\": \"python run_lmeval_clean.py --model_path {MODEL} --tasks lambada_openai,hellaswag,winogrande,arc_easy,arc_challenge,mmlu --output_dir lm_eval_clean/ --batch_size 8 (x3 models: hybrid-12-1, hybrid-24-1, hybrid-3-1)\", \"server\": \"westb-48145\", \"data_path\": \"/root/autodl-tmp/models_1.3b/\", \"data_count\": 3, \"model_name\": \"HGRN2-1.3B (3 hybrid variants)\", \"seed\": 0}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-18T16:00:12.920Z\"}}, \"count\": 40, \"total\": 40, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.0959}}"
    }
  },
  "sourceToolAssistantUUID": "e0343f6d-4d80-4f54-a1ee-04e1824eb267",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/sessions/agent_aa1a2296",
  "sessionId": "ccd4bb6d-9c70-4ece-9e7e-8b842791a0aa",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-22T16:41:51.711Z_

<details><summary>↩ Tool result · `toolu_01R9sMSKpamrZpeEZ6ePB6a3`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"reconciled\": 0, \"results\": []}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1592f242-eee1-44aa-b494-50dfa7e5077d",
  "isSidechain": false,
  "promptId": "53afff33-bebc-42c8-b6ca-8baf6ae2df0c",
  "type": "user",
  "uuid": "621b0ea2-dc85-47d4-bf5c-3118b9e61d24",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"reconciled\\\": 0, \\\"results\\\": []}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"reconciled\": 0, \"results\": []}, \"error\": null, \"metadata\": {}}"
    }
  },
  "sourceToolAssistantUUID": "1592f242-eee1-44aa-b494-50dfa7e5077d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/sessions/agent_aa1a2296",
  "sessionId": "ccd4bb6d-9c70-4ece-9e7e-8b842791a0aa",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-22T16:41:51.765Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01KxbRXLGj3ox26s13LPFWSK`</summary>

```json
{
  "project": "entrainment_gated_ft",
  "file": "report.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "621b0ea2-dc85-47d4-bf5c-3118b9e61d24",
  "isSidechain": false,
  "requestId": "req_011CbHwVyAmSPWi5G7kuCf5p",
  "type": "assistant",
  "uuid": "92a183c0-8396-48b4-b539-dcee131df866",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/sessions/agent_aa1a2296",
  "sessionId": "ccd4bb6d-9c70-4ece-9e7e-8b842791a0aa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ji6o9tmuz6jFh7TMfJvHve",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 4132,
      "cache_read_input_tokens": 37172,
      "output_tokens": 363,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4132,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 363,
          "cache_read_input_tokens": 37172,
          "cache_creation_input_tokens": 4132,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4132
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

_source line 18 · 2026-05-22T16:41:51.781Z_

<details><summary>↩ Tool result · `toolu_01KxbRXLGj3ox26s13LPFWSK`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/report.md\", \"content\": \"&lt;!-- AUTO-FACTS-BEGIN (generated 2026-05-22T16:41:32Z; do not edit — regenerated by auto_build_report_facts) -->\\n## 📊 当前状态（auto-derived from registry）\\n\\n**总计**: 40 个实验 — DONE 20, PENDING 1, PREPARING 19\\n**DONE 分布**: failed 1, killed 1, negative 4, success 14\\n\\n### GPU 占用\\n- **分配**: 1 张 — westb-48145:cuda:0\\n- **空闲（分配了没跑）**: westb-48145:cuda:0\\n\\n### 💾 磁盘余量\\n- **westb-48145**:\\n  - `/autodl-pub`: 7.6T/14T 可用（已用 46%）\\n  - `/autodl-pub/data`: 18T/20T 可用（已用 9%）\\n  - `/usr/bin/nvidia-smi`: 396G/439G 可用（已用 5%）\\n\\n### 🏃 RUNNING\\n_（无）_\\n\\n### 📌 最近完成 (top 5)\\n- `e4-pythia-seed-calibration` [success] — 2026-05-22T11:44:42 — process dead 5× with no sentinel/W&B — auto-resolved as failed\\n- `exp-340m-multi-bench` [success] — 2026-05-22T00:34:02\\n- `w3-winogrande-piqa-eval` [success] — 2026-05-21T10:27:33\\n- `exp-boolq-hellaswag-eval` [success] — 2026-05-21T08:53:38\\n- `exp-015` [success] — 2026-05-20T10:06:09\\n\\n&lt;!-- AUTO-FACTS-END -->\\n\\n---\\n\\n# Handover — 2026-05-22\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n（无）\\n\\n## 待处理\\n- exp-005-eval: Cross-architecture per-example Jaccard (helped/hurt) remains ≤0.10 when expanding from 3 architectures (GDN/RetNet/HGRN2) to 6 (adding GLA/DeltaNet/HGRN), with 15 pairwise comparisons and 720 permutations providing dramatically stronger statistical power.（等待人工审批）\\n- exp-005: Cross-architecture Jaccard overlap of helped/hurt sets will remain significantly above chance when expanded from 3 to 6 linear attention architectures, indicating that attention-mediated sample sensitivity is architecture-independent.（准备中）\\n- exp-003-p2v2: Helped samples have higher pure-model perplexity (model uncertain → attention helped) while hurt samples have lower perplexity (model confident → attention interfered), with architecture-specific patterns across GDN/RetNet/HGRN2. Retry with HGRN2 monkey-patch fix for _tied_weights_keys AttributeError.（准备中）\\n\\n## 近期结论\\n- **e4-pythia-seed-calibration** (success): Pythia 70M 9-seed variants 的 within-seed per-example Jaccard (same architecture, different random seed) 显著高于 cross-architecture Jaccard (~0.10), 证明 within-arch overlap >> cross-arch overlap, 即 cross-arch 信号不能被 seed noise 解释。 ← 基于 exp-001\\n  [e4_pythia_seed_calibration](/api/workspace-files/projects/entrainment_gated_ft/artifacts/e4-pythia-seed-calibration/data/e4_pythia_seed_calibration.json)\\n- **exp-340m-multi-bench** (success): 340M models exhibit α spectrum (per-example ambiguity) consistent with 1.3B across HellaSwag/PIQA/ARC-Easy — establishing scale-invariance of the multiplicity phenomenon beyond the single-benchmark (LAMBADA) evidence in §4.3. If α_340M ≈ α_1.3B per benchmark, cross-scale stability is confirmed; if systematically different, the scale-dependency claim needs qualification. ← 基于 exp-007\\n  [340m_multi_bench_analysis](/api/workspace-files/projects/entrainment_gated_ft/artifacts/exp-340m-multi-bench/data/340m_multi_bench_analysis.json)\\n- **w3-winogrande-piqa-eval** (success): WinoGrande + PIQA per-example multiplicity analysis to decouple format (2-choice vs 4-way MC) from task-type as driver of ambiguity α spectrum, addressing Round 5 W3 format confound concern\\n\\n## 趋势\\n成功 14 / 负向 4 / 失败 1 / 共 20\\n\\n## 下一步\\n（无活跃 idea，请通过 ideas.md 添加）\\n\\n## 资源状态\\nwestb-48145: 无 GPU 信息\\n\\n## 告警\\n- hgrn2_eval_1_3b_all: 已被终止 — unknown\\n- exp-004: 训练失败 — unknown\\n\", \"total_chars\": 3280, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "92a183c0-8396-48b4-b539-dcee131df866",
  "isSidechain": false,
  "promptId": "53afff33-bebc-42c8-b6ca-8baf6ae2df0c",
  "type": "user",
  "uuid": "2cc6fc62-c262-49b6-a70f-39e4f0d38f67",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/report.md\\\", \\\"content\\\": \\\"&lt;!-- AUTO-FACTS-BEGIN (generated 2026-05-22T16:41:32Z; do not edit — regenerated by auto_build_report_facts) -->\\\\n## 📊 当前状态（auto-derived from registry）\\\\n\\\\n**总计**: 40 个实验 — DONE 20, PENDING 1, PREPARING 19\\\\n**DONE 分布**: failed 1, killed 1, negative 4, success 14\\\\n\\\\n### GPU 占用\\\\n- **分配**: 1 张 — westb-48145:cuda:0\\\\n- **空闲（分配了没跑）**: westb-48145:cuda:0\\\\n\\\\n### 💾 磁盘余量\\\\n- **westb-48145**:\\\\n  - `/autodl-pub`: 7.6T/14T 可用（已用 46%）\\\\n  - `/autodl-pub/data`: 18T/20T 可用（已用 9%）\\\\n  - `/usr/bin/nvidia-smi`: 396G/439G 可用（已用 5%）\\\\n\\\\n### 🏃 RUNNING\\\\n_（无）_\\\\n\\\\n### 📌 最近完成 (top 5)\\\\n- `e4-pythia-seed-calibration` [success] — 2026-05-22T11:44:42 — process dead 5× with no sentinel/W&B — auto-resolved as failed\\\\n- `exp-340m-multi-bench` [success] — 2026-05-22T00:34:02\\\\n- `w3-winogrande-piqa-eval` [success] — 2026-05-21T10:27:33\\\\n- `exp-boolq-hellaswag-eval` [success] — 2026-05-21T08:53:38\\\\n- `exp-015` [success] — 2026-05-20T10:06:09\\\\n\\\\n&lt;!-- AUTO-FACTS-END -->\\\\n\\\\n---\\\\n\\\\n# Handover — 2026-05-22\\\\n\\\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\\\n\\\\n## 运行中\\\\n（无）\\\\n\\\\n## 待处理\\\\n- exp-005-eval: Cross-architecture per-example Jaccard (helped/hurt) remains ≤0.10 when expanding from 3 architectures (GDN/RetNet/HGRN2) to 6 (adding GLA/DeltaNet/HGRN), with 15 pairwise comparisons and 720 permutations providing dramatically stronger statistical power.（等待人工审批）\\\\n- exp-005: Cross-architecture Jaccard overlap of helped/hurt sets will remain significantly above chance when expanded from 3 to 6 linear attention architectures, indicating that attention-mediated sample sensitivity is architecture-independent.（准备中）\\\\n- exp-003-p2v2: Helped samples have higher pure-model perplexity (model uncertain → attention helped) while hurt samples have lower perplexity (model confident → attention interfered), with architecture-specific patterns across GDN/RetNet/HGRN2. Retry with HGRN2 monkey-patch fix for _tied_weights_keys AttributeError.（准备中）\\\\n\\\\n## 近期结论\\\\n- **e4-pythia-seed-calibration** (success): Pythia 70M 9-seed variants 的 within-seed per-example Jaccard (same architecture, different random seed) 显著高于 cross-architecture Jaccard (~0.10), 证明 within-arch overlap >> cross-arch overlap, 即 cross-arch 信号不能被 seed noise 解释。 ← 基于 exp-001\\\\n  [e4_pythia_seed_calibration](/api/workspace-files/projects/entrainment_gated_ft/artifacts/e4-pythia-seed-calibration/data/e4_pythia_seed_calibration.json)\\\\n- **exp-340m-multi-bench** (success): 340M models exhibit α spectrum (per-example ambiguity) consistent with 1.3B across HellaSwag/PIQA/ARC-Easy — establishing scale-invariance of the multiplicity phenomenon beyond the single-benchmark (LAMBADA) evidence in §4.3. If α_340M ≈ α_1.3B per benchmark, cross-scale stability is confirmed; if systematically different, the scale-dependency claim needs qualification. ← 基于 exp-007\\\\n  [340m_multi_bench_analysis](/api/workspace-files/projects/entrainment_gated_ft/artifacts/exp-340m-multi-bench/data/340m_multi_bench_analysis.json)\\\\n- **w3-winogrande-piqa-eval** (success): WinoGrande + PIQA per-example multiplicity analysis to decouple format (2-choice vs 4-way MC) from task-type as driver of ambiguity α spectrum, addressing Round 5 W3 format confound concern\\\\n\\\\n## 趋势\\\\n成功 14 / 负向 4 / 失败 1 / 共 20\\\\n\\\\n## 下一步\\\\n（无活跃 idea，请通过 ideas.md 添加）\\\\n\\\\n## 资源状态\\\\nwestb-48145: 无 GPU 信息\\\\n\\\\n## 告警\\\\n- hgrn2_eval_1_3b_all: 已被终止 — unknown\\\\n- exp-004: 训练失败 — unknown\\\\n\\\", \\\"total_chars\\\": 3280, \\\"truncated\\\": false}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/report.md\", \"content\": \"&lt;!-- AUTO-FACTS-BEGIN (generated 2026-05-22T16:41:32Z; do not edit — regenerated by auto_build_report_facts) -->\\n## 📊 当前状态（auto-derived from registry）\\n\\n**总计**: 40 个实验 — DONE 20, PENDING 1, PREPARING 19\\n**DONE 分布**: failed 1, killed 1, negative 4, success 14\\n\\n### GPU 占用\\n- **分配**: 1 张 — westb-48145:cuda:0\\n- **空闲（分配了没跑）**: westb-48145:cuda:0\\n\\n### 💾 磁盘余量\\n- **westb-48145**:\\n  - `/autodl-pub`: 7.6T/14T 可用（已用 46%）\\n  - `/autodl-pub/data`: 18T/20T 可用（已用 9%）\\n  - `/usr/bin/nvidia-smi`: 396G/439G 可用（已用 5%）\\n\\n### 🏃 RUNNING\\n_（无）_\\n\\n### 📌 最近完成 (top 5)\\n- `e4-pythia-seed-calibration` [success] — 2026-05-22T11:44:42 — process dead 5× with no sentinel/W&B — auto-resolved as failed\\n- `exp-340m-multi-bench` [success] — 2026-05-22T00:34:02\\n- `w3-winogrande-piqa-eval` [success] — 2026-05-21T10:27:33\\n- `exp-boolq-hellaswag-eval` [success] — 2026-05-21T08:53:38\\n- `exp-015` [success] — 2026-05-20T10:06:09\\n\\n&lt;!-- AUTO-FACTS-END -->\\n\\n---\\n\\n# Handover — 2026-05-22\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n（无）\\n\\n## 待处理\\n- exp-005-eval: Cross-architecture per-example Jaccard (helped/hurt) remains ≤0.10 when expanding from 3 architectures (GDN/RetNet/HGRN2) to 6 (adding GLA/DeltaNet/HGRN), with 15 pairwise comparisons and 720 permutations providing dramatically stronger statistical power.（等待人工审批）\\n- exp-005: Cross-architecture Jaccard overlap of helped/hurt sets will remain significantly above chance when expanded from 3 to 6 linear attention architectures, indicating that attention-mediated sample sensitivity is architecture-independent.（准备中）\\n- exp-003-p2v2: Helped samples have higher pure-model perplexity (model uncertain → attention helped) while hurt samples have lower perplexity (model confident → attention interfered), with architecture-specific patterns across GDN/RetNet/HGRN2. Retry with HGRN2 monkey-patch fix for _tied_weights_keys AttributeError.（准备中）\\n\\n## 近期结论\\n- **e4-pythia-seed-calibration** (success): Pythia 70M 9-seed variants 的 within-seed per-example Jaccard (same architecture, different random seed) 显著高于 cross-architecture Jaccard (~0.10), 证明 within-arch overlap >> cross-arch overlap, 即 cross-arch 信号不能被 seed noise 解释。 ← 基于 exp-001\\n  [e4_pythia_seed_calibration](/api/workspace-files/projects/entrainment_gated_ft/artifacts/e4-pythia-seed-calibration/data/e4_pythia_seed_calibration.json)\\n- **exp-340m-multi-bench** (success): 340M models exhibit α spectrum (per-example ambiguity) consistent with 1.3B across HellaSwag/PIQA/ARC-Easy — establishing scale-invariance of the multiplicity phenomenon beyond the single-benchmark (LAMBADA) evidence in §4.3. If α_340M ≈ α_1.3B per benchmark, cross-scale stability is confirmed; if systematically different, the scale-dependency claim needs qualification. ← 基于 exp-007\\n  [340m_multi_bench_analysis](/api/workspace-files/projects/entrainment_gated_ft/artifacts/exp-340m-multi-bench/data/340m_multi_bench_analysis.json)\\n- **w3-winogrande-piqa-eval** (success): WinoGrande + PIQA per-example multiplicity analysis to decouple format (2-choice vs 4-way MC) from task-type as driver of ambiguity α spectrum, addressing Round 5 W3 format confound concern\\n\\n## 趋势\\n成功 14 / 负向 4 / 失败 1 / 共 20\\n\\n## 下一步\\n（无活跃 idea，请通过 ideas.md 添加）\\n\\n## 资源状态\\nwestb-48145: 无 GPU 信息\\n\\n## 告警\\n- hgrn2_eval_1_3b_all: 已被终止 — unknown\\n- exp-004: 训练失败 — unknown\\n\", \"total_chars\": 3280, \"truncated\": false}, \"error\": null, \"metadata\": {}}"
    }
  },
  "sourceToolAssistantUUID": "92a183c0-8396-48b4-b539-dcee131df866",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/sessions/agent_aa1a2296",
  "sessionId": "ccd4bb6d-9c70-4ece-9e7e-8b842791a0aa",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-22T16:41:52.265Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_roadmap · `toolu_01HzfL4a9UCfZcmrwghChHaw`</summary>

```json
{
  "project": "entrainment_gated_ft"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2cc6fc62-c262-49b6-a70f-39e4f0d38f67",
  "isSidechain": false,
  "requestId": "req_011CbHwVyAmSPWi5G7kuCf5p",
  "type": "assistant",
  "uuid": "f342ef05-f34b-4fc3-90b9-860c3f06fc0e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/sessions/agent_aa1a2296",
  "sessionId": "ccd4bb6d-9c70-4ece-9e7e-8b842791a0aa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ji6o9tmuz6jFh7TMfJvHve",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 4132,
      "cache_read_input_tokens": 37172,
      "output_tokens": 363,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4132,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 363,
          "cache_read_input_tokens": 37172,
          "cache_creation_input_tokens": 4132,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4132
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

_source line 20 · 2026-05-22T16:41:52.274Z_

<details><summary>↩ Tool result · `toolu_01HzfL4a9UCfZcmrwghChHaw`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/ROADMAP.md\", \"content\": \"# entrainment_gated_ft — Research Dashboard\\n\\n> 最后更新: 2026-05-22 10:17 UTC | 更新原因: E1/E2/E3 完成 + E4 Pythia seed 实验派发 + Paper Agent R13 修复中\\n\\n## 核心方向\\nHybrid linear recurrent architectures (GDN/RetNet/HGRN2) 中 attention 对 cross-architecture behavioral diversity 的 per-example 分析。Predictive multiplicity 框架（Marx 2020）+ confidence-based architecture selection。详见 paper_framing.md。\\n\\n## 当前阶段\\n**目标：4.0 Conference。实验补充 + 写作修复并行推进。**\\n\\n### ⚠️ DEADLINE: 2026-05-25 (ARR May cycle) — 剩余 ~72h\\n\\n### 审稿历史\\n- Round 5-9: 连续 3.0 Findings\\n- Round 10-12: 逐步修复，R12 Overall 3.0 (R1=3.5, R2=3.0)\\n- Round 13: Fresh review 3.0。三个结构性问题：convergence 不显著、seed confound、novelty 有限\\n- **Post-R13**: 补 4 个实验 + 10+ 项 text fix\\n\\n### 分数瓶颈 → 对策\\n| 问题 | 对策 | 状态 |\\n|------|------|------|\\n| Seed confound (R5-W1, 13轮 Critical) | **E4 Pythia 410M 9-seed calibration** | Agent 执行中 |\\n| Novelty/Actionability (R2 Excitement 2/5) | E1 routing +5.33pp LAMBADA | ✅ done, Paper Agent 整合中 |\\n| Binary decomposition concern | E2 continuous Jaccard robust | ✅ done, Paper Agent 整合中 |\\n| Calibration confound | E3 ECE 17% vs threshold 47% | ✅ done, Paper Agent 整合中 |\\n| Convergence 叙事过重 | Paper Agent 结构重构完成 | ✅ done |\\n| Ecological Fallacy 未讨论 | Robinson (1950) + 讨论 | Paper Agent 执行中 |\\n\\n## 近期任务\\n- [ ] **E4** Pythia 410M multi-seed calibration（Agent 执行中，预计 2-4h）\\n- [ ] Paper Agent R13 text fixes + E1/E2/E3 integration（执行中，预计 2-3h）\\n- [ ] E4 结果整合到论文\\n- [ ] 编译 + Round 14 review\\n- [ ] Final polish + 提交 ARR\\n\\n## 实验成果总结\\n| ID | 结果 | 价值 |\\n|----|------|------|\\n| E1 Routing | LAMBADA +5.33pp, 36% oracle gap | 主文 §4.1 supporting |\\n| E2 Continuous J | J monotonic decrease τ=0→0.30 | Appendix + §4.1 ref |\\n| E3 Calibration | ECE 17% << threshold 47% | Appendix + §4.1 ref |\\n| E4 Pythia Seed | 执行中 | 预期：主文 §4.2 或 Appendix |\\n\\n## GPU 预算\\nwestb-48145: 1× GPU (cuda:0), E4 Pythia eval 使用中。\\n\\n## 关键决策日志\\n\\n| ID | 日期 | 摘要 | 关联实验 |\\n|----|------|------|----------|\\n| D036 | 2026-05-22 | 恢复 exp-005：Zoo 确认含 6 架构，之前取消理由有误 | exp-005 |\\n| D035 | 2026-05-22 | 取消 exp-005（6 架构扩展不可行），转向替代实验方案 | exp-005 |\\n| D034 | 2026-05-22 | E4 Pythia seed calibration 结果接受：70M 替代 410M，放 Appe | e4-pythia-seed-calibration |\\n| D033 | 2026-05-22 | D033: Pythia framing 策略 + 额外架构 stretch goal 标记 | e4-pythia-seed-calibration |\\n| D032 | 2026-05-22 | D032: 批准 Pythia 410M multi-seed calibration 实验——用  | — |\\n| D031 | 2026-05-22 | D031: E1 routing 结果 framing——作为 §4.1 supporting an | — |\\n| D030 | 2026-05-22 | D030: 目标从 3.0 Findings 升级到 4.0 Conference——补 3 个实验 | — |\\n| D029 | 2026-05-22 | Round 10 Fresh Review Action Matrix 定稿：接受 Reviewer | — |\\n| D028 | 2026-05-22 | Round 10 直接修复：Director 跳过 Paper Agent 直接编辑论文，修复 9  | — |\\n| D027 | 2026-05-22 | Round 8 Action Matrix: 合并 C2+C3 为 secondary observ | — |\\n\\n\", \"lines\": 62}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f342ef05-f34b-4fc3-90b9-860c3f06fc0e",
  "isSidechain": false,
  "promptId": "53afff33-bebc-42c8-b6ca-8baf6ae2df0c",
  "type": "user",
  "uuid": "f9a10ca5-d69b-4d9f-9dc7-4dcc0e490a3a",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/ROADMAP.md\\\", \\\"content\\\": \\\"# entrainment_gated_ft — Research Dashboard\\\\n\\\\n> 最后更新: 2026-05-22 10:17 UTC | 更新原因: E1/E2/E3 完成 + E4 Pythia seed 实验派发 + Paper Agent R13 修复中\\\\n\\\\n## 核心方向\\\\nHybrid linear recurrent architectures (GDN/RetNet/HGRN2) 中 attention 对 cross-architecture behavioral diversity 的 per-example 分析。Predictive multiplicity 框架（Marx 2020）+ confidence-based architecture selection。详见 paper_framing.md。\\\\n\\\\n## 当前阶段\\\\n**目标：4.0 Conference。实验补充 + 写作修复并行推进。**\\\\n\\\\n### ⚠️ DEADLINE: 2026-05-25 (ARR May cycle) — 剩余 ~72h\\\\n\\\\n### 审稿历史\\\\n- Round 5-9: 连续 3.0 Findings\\\\n- Round 10-12: 逐步修复，R12 Overall 3.0 (R1=3.5, R2=3.0)\\\\n- Round 13: Fresh review 3.0。三个结构性问题：convergence 不显著、seed confound、novelty 有限\\\\n- **Post-R13**: 补 4 个实验 + 10+ 项 text fix\\\\n\\\\n### 分数瓶颈 → 对策\\\\n| 问题 | 对策 | 状态 |\\\\n|------|------|------|\\\\n| Seed confound (R5-W1, 13轮 Critical) | **E4 Pythia 410M 9-seed calibration** | Agent 执行中 |\\\\n| Novelty/Actionability (R2 Excitement 2/5) | E1 routing +5.33pp LAMBADA | ✅ done, Paper Agent 整合中 |\\\\n| Binary decomposition concern | E2 continuous Jaccard robust | ✅ done, Paper Agent 整合中 |\\\\n| Calibration confound | E3 ECE 17% vs threshold 47% | ✅ done, Paper Agent 整合中 |\\\\n| Convergence 叙事过重 | Paper Agent 结构重构完成 | ✅ done |\\\\n| Ecological Fallacy 未讨论 | Robinson (1950) + 讨论 | Paper Agent 执行中 |\\\\n\\\\n## 近期任务\\\\n- [ ] **E4** Pythia 410M multi-seed calibration（Agent 执行中，预计 2-4h）\\\\n- [ ] Paper Agent R13 text fixes + E1/E2/E3 integration（执行中，预计 2-3h）\\\\n- [ ] E4 结果整合到论文\\\\n- [ ] 编译 + Round 14 review\\\\n- [ ] Final polish + 提交 ARR\\\\n\\\\n## 实验成果总结\\\\n| ID | 结果 | 价值 |\\\\n|----|------|------|\\\\n| E1 Routing | LAMBADA +5.33pp, 36% oracle gap | 主文 §4.1 supporting |\\\\n| E2 Continuous J | J monotonic decrease τ=0→0.30 | Appendix + §4.1 ref |\\\\n| E3 Calibration | ECE 17% << threshold 47% | Appendix + §4.1 ref |\\\\n| E4 Pythia Seed | 执行中 | 预期：主文 §4.2 或 Appendix |\\\\n\\\\n## GPU 预算\\\\nwestb-48145: 1× GPU (cuda:0), E4 Pythia eval 使用中。\\\\n\\\\n## 关键决策日志\\\\n\\\\n| ID | 日期 | 摘要 | 关联实验 |\\\\n|----|------|------|----------|\\\\n| D036 | 2026-05-22 | 恢复 exp-005：Zoo 确认含 6 架构，之前取消理由有误 | exp-005 |\\\\n| D035 | 2026-05-22 | 取消 exp-005（6 架构扩展不可行），转向替代实验方案 | exp-005 |\\\\n| D034 | 2026-05-22 | E4 Pythia seed calibration 结果接受：70M 替代 410M，放 Appe | e4-pythia-seed-calibration |\\\\n| D033 | 2026-05-22 | D033: Pythia framing 策略 + 额外架构 stretch goal 标记 | e4-pythia-seed-calibration |\\\\n| D032 | 2026-05-22 | D032: 批准 Pythia 410M multi-seed calibration 实验——用  | — |\\\\n| D031 | 2026-05-22 | D031: E1 routing 结果 framing——作为 §4.1 supporting an | — |\\\\n| D030 | 2026-05-22 | D030: 目标从 3.0 Findings 升级到 4.0 Conference——补 3 个实验 | — |\\\\n| D029 | 2026-05-22 | Round 10 Fresh Review Action Matrix 定稿：接受 Reviewer | — |\\\\n| D028 | 2026-05-22 | Round 10 直接修复：Director 跳过 Paper Agent 直接编辑论文，修复 9  | — |\\\\n| D027 | 2026-05-22 | Round 8 Action Matrix: 合并 C2+C3 为 secondary observ | — |\\\\n\\\\n\\\", \\\"lines\\\": 62}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/ROADMAP.md\", \"content\": \"# entrainment_gated_ft — Research Dashboard\\n\\n> 最后更新: 2026-05-22 10:17 UTC | 更新原因: E1/E2/E3 完成 + E4 Pythia seed 实验派发 + Paper Agent R13 修复中\\n\\n## 核心方向\\nHybrid linear recurrent architectures (GDN/RetNet/HGRN2) 中 attention 对 cross-architecture behavioral diversity 的 per-example 分析。Predictive multiplicity 框架（Marx 2020）+ confidence-based architecture selection。详见 paper_framing.md。\\n\\n## 当前阶段\\n**目标：4.0 Conference。实验补充 + 写作修复并行推进。**\\n\\n### ⚠️ DEADLINE: 2026-05-25 (ARR May cycle) — 剩余 ~72h\\n\\n### 审稿历史\\n- Round 5-9: 连续 3.0 Findings\\n- Round 10-12: 逐步修复，R12 Overall 3.0 (R1=3.5, R2=3.0)\\n- Round 13: Fresh review 3.0。三个结构性问题：convergence 不显著、seed confound、novelty 有限\\n- **Post-R13**: 补 4 个实验 + 10+ 项 text fix\\n\\n### 分数瓶颈 → 对策\\n| 问题 | 对策 | 状态 |\\n|------|------|------|\\n| Seed confound (R5-W1, 13轮 Critical) | **E4 Pythia 410M 9-seed calibration** | Agent 执行中 |\\n| Novelty/Actionability (R2 Excitement 2/5) | E1 routing +5.33pp LAMBADA | ✅ done, Paper Agent 整合中 |\\n| Binary decomposition concern | E2 continuous Jaccard robust | ✅ done, Paper Agent 整合中 |\\n| Calibration confound | E3 ECE 17% vs threshold 47% | ✅ done, Paper Agent 整合中 |\\n| Convergence 叙事过重 | Paper Agent 结构重构完成 | ✅ done |\\n| Ecological Fallacy 未讨论 | Robinson (1950) + 讨论 | Paper Agent 执行中 |\\n\\n## 近期任务\\n- [ ] **E4** Pythia 410M multi-seed calibration（Agent 执行中，预计 2-4h）\\n- [ ] Paper Agent R13 text fixes + E1/E2/E3 integration（执行中，预计 2-3h）\\n- [ ] E4 结果整合到论文\\n- [ ] 编译 + Round 14 review\\n- [ ] Final polish + 提交 ARR\\n\\n## 实验成果总结\\n| ID | 结果 | 价值 |\\n|----|------|------|\\n| E1 Routing | LAMBADA +5.33pp, 36% oracle gap | 主文 §4.1 supporting |\\n| E2 Continuous J | J monotonic decrease τ=0→0.30 | Appendix + §4.1 ref |\\n| E3 Calibration | ECE 17% << threshold 47% | Appendix + §4.1 ref |\\n| E4 Pythia Seed | 执行中 | 预期：主文 §4.2 或 Appendix |\\n\\n## GPU 预算\\nwestb-48145: 1× GPU (cuda:0), E4 Pythia eval 使用中。\\n\\n## 关键决策日志\\n\\n| ID | 日期 | 摘要 | 关联实验 |\\n|----|------|------|----------|\\n| D036 | 2026-05-22 | 恢复 exp-005：Zoo 确认含 6 架构，之前取消理由有误 | exp-005 |\\n| D035 | 2026-05-22 | 取消 exp-005（6 架构扩展不可行），转向替代实验方案 | exp-005 |\\n| D034 | 2026-05-22 | E4 Pythia seed calibration 结果接受：70M 替代 410M，放 Appe | e4-pythia-seed-calibration |\\n| D033 | 2026-05-22 | D033: Pythia framing 策略 + 额外架构 stretch goal 标记 | e4-pythia-seed-calibration |\\n| D032 | 2026-05-22 | D032: 批准 Pythia 410M multi-seed calibration 实验——用  | — |\\n| D031 | 2026-05-22 | D031: E1 routing 结果 framing——作为 §4.1 supporting an | — |\\n| D030 | 2026-05-22 | D030: 目标从 3.0 Findings 升级到 4.0 Conference——补 3 个实验 | — |\\n| D029 | 2026-05-22 | Round 10 Fresh Review Action Matrix 定稿：接受 Reviewer | — |\\n| D028 | 2026-05-22 | Round 10 直接修复：Director 跳过 Paper Agent 直接编辑论文，修复 9  | — |\\n| D027 | 2026-05-22 | Round 8 Action Matrix: 合并 C2+C3 为 secondary observ | — |\\n\\n\", \"lines\": 62}, \"error\": null, \"metadata\": {}}"
    }
  },
  "sourceToolAssistantUUID": "f342ef05-f34b-4fc3-90b9-860c3f06fc0e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/sessions/agent_aa1a2296",
  "sessionId": "ccd4bb6d-9c70-4ece-9e7e-8b842791a0aa",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-22T16:41:52.534Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__list_workers · `toolu_01Qvfg8qFTrTfZD3mGEx6x3W`</summary>

```json
{
  "project": "entrainment_gated_ft",
  "status": "running"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f9a10ca5-d69b-4d9f-9dc7-4dcc0e490a3a",
  "isSidechain": false,
  "requestId": "req_011CbHwVyAmSPWi5G7kuCf5p",
  "type": "assistant",
  "uuid": "31feae8c-5b54-4ca1-ae6e-19d2ac9b39a7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/sessions/agent_aa1a2296",
  "sessionId": "ccd4bb6d-9c70-4ece-9e7e-8b842791a0aa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ji6o9tmuz6jFh7TMfJvHve",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 4132,
      "cache_read_input_tokens": 37172,
      "output_tokens": 363,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4132,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 363,
          "cache_read_input_tokens": 37172,
          "cache_creation_input_tokens": 4132,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4132
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

_source line 22 · 2026-05-22T16:41:52.631Z_

<details><summary>↩ Tool result · `toolu_01Qvfg8qFTrTfZD3mGEx6x3W`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"workers\": [{\"worker_id\": \"worker_fix_exp-005-download-fix_20260522T151052\", \"task_type\": \"fix:exp-005-download-fix\", \"project\": \"entrainment_gated_ft\", \"status\": \"running\", \"started_at\": \"2026-05-22T15:10:52.291078+00:00\", \"ended_at\": null}, {\"worker_id\": \"worker_exp_exp-005-pure-baselines_20260522T155641\", \"task_type\": \"exp:exp-005-pure-baselines\", \"project\": \"entrainment_gated_ft\", \"status\": \"running\", \"started_at\": \"2026-05-22T15:56:41.476588+00:00\", \"ended_at\": null}], \"count\": 2}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "31feae8c-5b54-4ca1-ae6e-19d2ac9b39a7",
  "isSidechain": false,
  "promptId": "53afff33-bebc-42c8-b6ca-8baf6ae2df0c",
  "type": "user",
  "uuid": "cc26528a-1ee0-4ab0-a013-7027af4b0c4c",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"workers\\\": [{\\\"worker_id\\\": \\\"worker_fix_exp-005-download-fix_20260522T151052\\\", \\\"task_type\\\": \\\"fix:exp-005-download-fix\\\", \\\"project\\\": \\\"entrainment_gated_ft\\\", \\\"status\\\": \\\"running\\\", \\\"started_at\\\": \\\"2026-05-22T15:10:52.291078+00:00\\\", \\\"ended_at\\\": null}, {\\\"worker_id\\\": \\\"worker_exp_exp-005-pure-baselines_20260522T155641\\\", \\\"task_type\\\": \\\"exp:exp-005-pure-baselines\\\", \\\"project\\\": \\\"entrainment_gated_ft\\\", \\\"status\\\": \\\"running\\\", \\\"started_at\\\": \\\"2026-05-22T15:56:41.476588+00:00\\\", \\\"ended_at\\\": null}], \\\"count\\\": 2}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"workers\": [{\"worker_id\": \"worker_fix_exp-005-download-fix_20260522T151052\", \"task_type\": \"fix:exp-005-download-fix\", \"project\": \"entrainment_gated_ft\", \"status\": \"running\", \"started_at\": \"2026-05-22T15:10:52.291078+00:00\", \"ended_at\": null}, {\"worker_id\": \"worker_exp_exp-005-pure-baselines_20260522T155641\", \"task_type\": \"exp:exp-005-pure-baselines\", \"project\": \"entrainment_gated_ft\", \"status\": \"running\", \"started_at\": \"2026-05-22T15:56:41.476588+00:00\", \"ended_at\": null}], \"count\": 2}, \"error\": null, \"metadata\": {}}"
    }
  },
  "sourceToolAssistantUUID": "31feae8c-5b54-4ca1-ae6e-19d2ac9b39a7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/sessions/agent_aa1a2296",
  "sessionId": "ccd4bb6d-9c70-4ece-9e7e-8b842791a0aa",
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
  "lastPrompt": "[CRON] 实验进程已正常退出，状态已转为 ANALYZING，需要你分析结果并推进到 DONE。 详情: Process exited cleanly, W&B data available  - exp_id: exp-005-gla-pure - project: entrainment_gated_ft - server: westb-48145 - log_path: ~/runs/e…",
  "leafUuid": "cc26528a-1ee0-4ab0-a013-7027af4b0c4c",
  "sessionId": "ccd4bb6d-9c70-4ece-9e7e-8b842791a0aa"
}
```

---

### Runtime record

_source line 24_

```json
{
  "type": "ai-title",
  "aiTitle": "Analyze experiment results and mark as done",
  "sessionId": "ccd4bb6d-9c70-4ece-9e7e-8b842791a0aa"
}
```

---

### Assistant

_source line 25 · 2026-05-22T16:42:09.430Z_

<details><summary>Logged reasoning block</summary>

```text
Let me analyze the situation:

1. **exp-005-gla-pure** - Status is PREPARING in registry (but cron says it's ANALYZING). The spec shows it's an eval job running `patch_fla_eval.py` on a GLA pure baseline model for lambada_openai and arc_easy tasks. Server: westb-48145, GPU: cuda:0. The process has finished.

2. **Running workers**: 
   - `worker_fix_exp-005-download-fix` - running since 15:10
   - `worker_exp_exp-005-pure-baselines` - running since 15:56

3. **ROADMAP**: Deadline is 2026-05-25 (ARR May cycle), ~72h remaining. Current focus is on expanding the architecture zoo from 3 to 6 for cross-architecture analysis. exp-005 is about this zoo expansion.

4. **Report**: Shows 40 experiments total, 20 DONE, 1 PENDING, 19 PREPARING. No GPU currently running.

Now I need to check the full registry entry for exp-005-gla-pure since it's finished and ready for analysis.

Looking at the registry, exp-005-gla-pure is evaluating the `340M-20B-GLA-pure-baseline` model using the FLA evaluation script on lambada_openai and arc_easy tasks. The reproduce step finished at 2026-05-22T16:41:30.660Z, though the status hasn't updated to ANALYZING yet. I need to spawn a worker to SSH into westb-48145, pull the logs and results, analyze the metrics, and then update the registry accordingly. This experiment is part of the zoo expansion work, so understanding its performance will help inform the cross-architecture comparison.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cc26528a-1ee0-4ab0-a013-7027af4b0c4c",
  "isSidechain": false,
  "requestId": "req_011CbHwWRghzWdSk6QuEGmAg",
  "type": "assistant",
  "uuid": "218acd17-2ffa-42a7-89bb-9a68d8bf9a83",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/sessions/agent_aa1a2296",
  "sessionId": "ccd4bb6d-9c70-4ece-9e7e-8b842791a0aa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019GXPuPPnGiJTB4TcbvFj4d",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4929,
      "cache_read_input_tokens": 41304,
      "output_tokens": 864,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4929,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 864,
          "cache_read_input_tokens": 41304,
          "cache_creation_input_tokens": 4929,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4929
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

_source line 26 · 2026-05-22T16:42:09.432Z_

需要读取完整 registry 数据和实验详情。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "218acd17-2ffa-42a7-89bb-9a68d8bf9a83",
  "isSidechain": false,
  "requestId": "req_011CbHwWRghzWdSk6QuEGmAg",
  "type": "assistant",
  "uuid": "ef02fbf7-bbcb-4f98-a4e9-151ae19b6735",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/sessions/agent_aa1a2296",
  "sessionId": "ccd4bb6d-9c70-4ece-9e7e-8b842791a0aa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019GXPuPPnGiJTB4TcbvFj4d",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4929,
      "cache_read_input_tokens": 41304,
      "output_tokens": 864,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4929,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 864,
          "cache_read_input_tokens": 41304,
          "cache_creation_input_tokens": 4929,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4929
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

_source line 27 · 2026-05-22T16:42:14.025Z_

<details open><summary>🔧 Tool call — Read · `toolu_019mP95PJ7oNZTyChLo6KzeB`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-2-projects-entrainment-gated-ft--claude-sessions-agent-aa1a2296/ccd4bb6d-9c70-4ece-9e7e-8b842791a0aa/tool-results/toolu_017SjjVew7bhkJio3KNz9LNC.txt",
  "limit": 200
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ef02fbf7-bbcb-4f98-a4e9-151ae19b6735",
  "isSidechain": false,
  "requestId": "req_011CbHwWRghzWdSk6QuEGmAg",
  "type": "assistant",
  "uuid": "e0a2fe02-939a-4ef2-b3bd-fc442aa65c19",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/sessions/agent_aa1a2296",
  "sessionId": "ccd4bb6d-9c70-4ece-9e7e-8b842791a0aa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019GXPuPPnGiJTB4TcbvFj4d",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4929,
      "cache_read_input_tokens": 41304,
      "output_tokens": 864,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4929,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 864,
          "cache_read_input_tokens": 41304,
          "cache_creation_input_tokens": 4929,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4929
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

_source line 28 · 2026-05-22T16:42:14.035Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_experiment_plan_with_status · `toolu_01G2WS4qHRoaGKG3P313Cbg2`</summary>

```json
{
  "project": "entrainment_gated_ft"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e0a2fe02-939a-4ef2-b3bd-fc442aa65c19",
  "isSidechain": false,
  "requestId": "req_011CbHwWRghzWdSk6QuEGmAg",
  "type": "assistant",
  "uuid": "896921bc-cafe-4244-9aaa-456b26890548",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/sessions/agent_aa1a2296",
  "sessionId": "ccd4bb6d-9c70-4ece-9e7e-8b842791a0aa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019GXPuPPnGiJTB4TcbvFj4d",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4929,
      "cache_read_input_tokens": 41304,
      "output_tokens": 864,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4929,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 864,
          "cache_read_input_tokens": 41304,
          "cache_creation_input_tokens": 4929,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4929
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

_source line 29 · 2026-05-22T16:42:14.333Z_

<details><summary>↩ Tool result · `toolu_019mP95PJ7oNZTyChLo6KzeB`</summary>

```text
1	{"result":"{\"success\": true, \"data\": {\"experiments\": {\"exp-005-gla-pure\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-22T16:33:56.971Z\", \"updated_at\": \"2026-05-22T16:41:30.660Z\", \"spec\": {\"command\": \"bash -c \\\"source /etc/network_turbo && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_HUB_DISABLE_XET=1 && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && python /root/entrainment_gated_ft/scripts/patch_fla_eval.py --model hf --model_args pretrained=/root/entrainment_gated_ft/models/340M-20B-GLA-pure-baseline,trust_remote_code=True --tasks lambada_openai,arc_easy --device cuda:0 --batch_size auto --log_samples --output_path /root/entrainment_gated_ft/results/exp005_zoo_expansion/GLA_pure/ && echo GLA_PURE_EVAL_DONE\\\"\", \"server\": \"westb-48145\", \"gpu\": [\"cuda:0\"], \"pid\": \"904591\", \"log_path\": \"~/runs/entrainment_gated_ft/exp-005-gla-pure.log\", \"submitted_at\": \"2026-05-22T16:39:54.061Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"reproduce\": {\"finished_at\": \"2026-05-22T16:41:30.660Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-22T16:41:32.936910+00:00\"}]}}, \"exp-005-pure-v5\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-22T16:37:28.872Z\", \"updated_at\": \"2026-05-22T16:37:28.872Z\", \"spec\": {\"command\": \"bash -c \\\"bash /root/entrainment_gated_ft/results/exp005_zoo_expansion/run_pure_v5.sh\\\"\", \"server\": \"westb-48145\", \"gpu\": [\"cuda:0\"], \"pid\": \"904122\", \"log_path\": \"~/runs/entrainment_gated_ft/exp-005-pure-v5.log\", \"submitted_at\": \"2026-05-22T16:37:28.788Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"exp-005-pure-v4\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-22T16:35:11.429Z\", \"updated_at\": \"2026-05-22T16:35:11.429Z\", \"spec\": {\"command\": \"bash -c \\\"bash /root/entrainment_gated_ft/results/exp005_zoo_expansion/run_pure_v4.sh\\\"\", \"server\": \"westb-48145\", \"gpu\": [\"cuda:0\"], \"pid\": \"903338\", \"log_path\": \"~/runs/entrainment_gated_ft/exp-005-pure-v4.log\", \"submitted_at\": \"2026-05-22T16:35:11.341Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"exp-005-pure-v3\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-22T16:32:39.150Z\", \"updated_at\": \"2026-05-22T16:32:39.150Z\", \"spec\": {\"command\": \"bash -c \\\"bash /root/entrainment_gated_ft/results/exp005_zoo_expansion/run_pure_v3.sh\\\"\", \"server\": \"westb-48145\", \"gpu\": [\"cuda:0\"], \"pid\": \"902795\", \"log_path\": \"~/runs/entrainment_gated_ft/exp-005-pure-v3.log\", \"submitted_at\": \"2026-05-22T16:32:39.070Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"exp-005-batch\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-22T16:30:41.446Z\", \"updated_at\": \"2026-05-22T16:31:53.107Z\", \"spec\": {\"command\": \"bash -c \\\"bash /root/entrainment_gated_ft/results/exp005_zoo_expansion/run_eval_download.sh\\\"\", \"server\": \"westb-48145\", \"gpu\": [\"cuda:0\"], \"pid\": \"902349\", \"log_path\": \"~/runs/entrainment_gated_ft/exp-005-batch.log\", \"submitted_at\": \"2026-05-22T16:30:41.362Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"reproduce\": {\"finished_at\": \"2026-05-22T16:31:50.753Z\"}, \"failure_reason\": \"EXIT_CODE=1 (generic error — check log tail)\", \"conclusion\": \"failed\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-22T16:31:55.361162+00:00\"}]}}, \"exp-005-hgrn-chain\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-22T16:27:47.360Z\", \"updated_at\": \"2026-05-22T16:27:47.360Z\", \"spec\": {\"command\": \"bash -c \\\"bash /root/entrainment_gated_ft/results/exp005_zoo_expansion/run_hgrn_chain.sh\\\"\", \"server\": \"westb-48145\", \"gpu\": [\"cuda:0\"], \"pid\": \"902087\", \"log_path\": \"~/runs/entrainment_gated_ft/exp-005-hgrn-chain.log\", \"submitted_at\": \"2026-05-22T16:27:47.270Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"exp-005\": {\"status\": \"PREPARING\", \"retry_count\": 1, \"created_at\": \"2026-05-20T02:26:40.718Z\", \"updated_at\": \"2026-05-22T16:18:38.064Z\", \"hypothesis\": \"Cross-architecture Jaccard overlap of helped/hurt sets will remain significantly above chance when expanded from 3 to 6 linear attention architectures, indicating that attention-mediated sample sensitivity is architecture-independent.\", \"parent\": \"exp-001\", \"completed_at\": \"2026-05-22T14:24:29.103Z\", \"extra\": {\"previous_failure\": {\"conclusion\": \"killed\", \"metrics\": {\"cancel_reason\": \"Wang et al. zoo 仅含 GDN/RetNet/HGRN2，无法扩展 n>3，已由 worker_analysis_arch-extension-check 确认\"}}, \"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-22T15:05:27.711311+00:00\"}]}, \"metrics\": {\"gla_h31_lambada_acc\": 0.3819, \"gla_h31_arc_acc\": 0.5673, \"deltanet_h31_lambada_acc\": 0.3536, \"deltanet_h31_lambada_ppl\": 30.45, \"deltanet_h31_arc_acc\": 0.601, \"fla_patch_needed\": \"scripts/patch_fla_eval.py fixes _tied_weights_keys list→dict for fla 0.5.0 + transformers 5.8.1\"}, \"reproduce\": {\"finished_at\": \"2026-05-22T15:05:23.157Z\"}, \"failure_reason\": \"EXIT_CODE=1 (generic error — check log tail)\", \"conclusion\": \"failed\", \"notes\": \"诊断中: worker_diagnose_exp-005-p1-v4_20260522T150706 正在查日志。日志仅7行，进程在下载 DeltaNet h3-1 模型时 EXIT_CODE=1 退出。\"}, \"exp-005-p1-eval-v5\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-22T16:18:29.815Z\", \"updated_at\": \"2026-05-22T16:18:29.815Z\", \"spec\": {\"command\": \"bash -c \\\"bash /root/entrainment_gated_ft/results/exp005_zoo_expansion/run_eval_p1.sh\\\"\", \"server\": \"westb-48145\", \"gpu\": [\"cuda:0\"], \"pid\": \"898757\", \"log_path\": \"~/runs/entrainment_gated_ft/exp-005-p1-eval-v5.log\", \"submitted_at\": \"2026-05-22T16:18:29.731Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"exp-005-p1-eval-v4\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-22T16:16:34.914Z\", \"updated_at\": \"2026-05-22T16:16:34.914Z\", \"spec\": {\"command\": \"bash -c \\\"bash /root/entrainment_gated_ft/results/exp005_zoo_expansion/run_eval_p1.sh\\\"\", \"server\": \"westb-48145\", \"gpu\": [\"cuda:0\"], \"pid\": \"897689\", \"log_path\": \"~/runs/entrainment_gated_ft/exp-005-p1-eval-v4.log\", \"submitted_at\": \"2026-05-22T16:16:34.836Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"exp-005-dn-eval\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-22T15:56:19.907Z\", \"updated_at\": \"2026-05-22T16:10:46.245Z\", \"spec\": {\"command\": \"bash -c \\\"source /etc/network_turbo && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_HUB_DISABLE_XET=1 && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && cd /root/entrainment_gated_ft && python scripts/patch_fla_eval.py --model hf --model_args pretrained=/root/entrainment_gated_ft/models/340M-20B-DeltaNet-hybrid-3-1,trust_remote_code=True,dtype=float16 --tasks lambada_openai,arc_easy --device cuda:0 --batch_size auto --log_samples --output_path /root/entrainment_gated_ft/results/exp005_zoo_expansion/DeltaNet_hybrid-3-1/ && echo DELTANET_EVAL_DONE\\\"\", \"server\": \"westb-48145\", \"gpu\": [\"cuda:0\"], \"pid\": \"886300\", \"log_path\": \"~/runs/entrainment_gated_ft/exp-005-dn-eval.log\", \"submitted_at\": \"2026-05-22T16:04:02.638Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"metrics\": {\"model\": \"340M-20B-DeltaNet-hybrid-3-1\", \"lambada_openai_acc\": 0.3536, \"lambada_openai_ppl\": 30.45, \"arc_easy_acc\": 0.601, \"arc_easy_acc_norm\": 0.5198, \"status\": \"DONE\"}}, \"exp-005-p1-eval-v3\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-22T16:07:46.157Z\", \"updated_at\": \"2026-05-22T16:07:46.157Z\", \"spec\": {\"command\": \"bash -c \\\"bash /root/entrainment_gated_ft/results/exp005_zoo_expansion/run_eval_p1.sh\\\"\", \"server\": \"westb-48145\", \"gpu\": [\"cuda:0\"], \"pid\": \"891633\", \"log_path\": \"~/runs/entrainment_gated_ft/exp-005-p1-eval-v3.log\", \"submitted_at\": \"2026-05-22T16:07:46.079Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"exp-005-p1-eval-v2\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-22T16:06:40.443Z\", \"updated_at\": \"2026-05-22T16:06:40.443Z\", \"spec\": {\"command\": \"bash -c \\\"bash /root/entrainment_gated_ft/results/exp005_zoo_expansion/run_eval_p1.sh\\\"\", \"server\": \"westb-48145\", \"gpu\": [\"cuda:0\"], \"pid\": \"889541\", \"log_path\": \"~/runs/entrainment_gated_ft/exp-005-p1-eval-v2.log\", \"submitted_at\": \"2026-05-22T16:06:40.369Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"exp-005-p1-eval\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-22T16:01:38.958Z\", \"updated_at\": \"2026-05-22T16:01:38.958Z\", \"spec\": {\"command\": \"bash -c \\\"bash /root/entrainment_gated_ft/results/exp005_zoo_expansion/run_eval_p1.sh\\\"\", \"server\": \"westb-48145\", \"gpu\": [\"cuda:0\"], \"pid\": \"884365\", \"log_path\": \"~/runs/entrainment_gated_ft/exp-005-p1-eval.log\", \"submitted_at\": \"2026-05-22T16:01:38.883Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"exp-005-pure-eval\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-22T15:58:12.656Z\", \"updated_at\": \"2026-05-22T16:01:21.317Z\", \"spec\": {\"command\": \"bash -c \\\"bash /root/entrainment_gated_ft/results/exp005_zoo_expansion/run_wget_eval_pure.sh\\\"\", \"server\": \"westb-48145\", \"gpu\": [\"cuda:0\"], \"pid\": \"884046\", \"log_path\": \"~/runs/entrainment_gated_ft/exp-005-pure-eval.log\", \"submitted_at\": \"2026-05-22T16:01:21.241Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"exp-005-deltanet\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-22T15:51:45.169Z\", \"updated_at\": \"2026-05-22T15:51:45.169Z\", \"spec\": {\"command\": \"bash -c \\\"bash /root/entrainment_gated_ft/results/exp005_zoo_expansion/eval_deltanet_hardcode.sh\\\"\", \"server\": \"westb-48145\", \"gpu\": [\"cuda:0\"], \"pid\": \"881335\", \"log_path\": \"~/runs/entrainment_gated_ft/exp-005-deltanet.log\", \"submitted_at\": \"2026-05-22T15:51:45.096Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"exp-005-gla\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-22T15:41:49.615Z\", \"updated_at\": \"2026-05-22T15:48:24.790Z\", \"spec\": {\"command\": \"bash -c \\\"bash /root/entrainment_gated_ft/results/exp005_zoo_expansion/eval_gla_hardcode.sh\\\"\", \"server\": \"westb-48145\", \"gpu\": [\"cuda:0\"], \"pid\": \"878457\", \"log_path\": \"~/runs/entrainment_gated_ft/exp-005-gla.log\", \"submitted_at\": \"2026-05-22T15:48:24.719Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"exp-005-gla-eval\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-22T15:38:30.968Z\", \"updated_at\": \"2026-05-22T15:44:36.037Z\", \"spec\": {\"command\": \"bash -c \\\"source /etc/network_turbo && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_HUB_DISABLE_XET=1 && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && python -c 'import fla; print(fla.__version__)' && python -m lm_eval --model hf --model_args pretrained=/root/entrainment_gated_ft/models/340M-20B-GLA-hybrid-3-1,trust_remote_code=True --tasks lambada_openai,arc_easy --device cuda:0 --batch_size auto --log_samples --output_path /root/entrainment_gated_ft/results/exp005_zoo_expansion/GLA_hybrid-3-1/ && echo GLA_EVAL_DONE\\\"\", \"server\": \"westb-48145\", \"gpu\": [\"cuda:0\"], \"pid\": \"875395\", \"log_path\": \"~/runs/entrainment_gated_ft/exp-005-gla-eval.log\", \"submitted_at\": \"2026-05-22T15:42:46.005Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"reproduce\": {\"finished_at\": \"2026-05-22T15:43:08.734Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-22T15:39:05.469998+00:00\"}, {\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-22T15:43:12.720582+00:00\"}]}, \"failure_reason\": \"Traceback → ss = CONFIG_MAPPING[config_dict[\\\"model_type\\\"]] ~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^ File \\\"/root/miniconda3/lib/python3.12/site-packages/transformers/models/auto/configuration_auto.py\\\", line 105, in __getitem__ raise KeyError(key) KeyError: 'gla'\", \"conclusion\": \"failed\", \"notes\": \"失败原因已诊断：1) 首次提交 pretrained='' 空字符串（shell 变量展开问题）；2) 重试时 KeyError: 'gla'（transformers AutoModel 不识别 GLA 模型类型，需要 fla 包注册）。模型文件本身完整（340M-20B-GLA-hybrid-3-1/model.safetensors 存在）。worker_fix_exp-005-gla-eval-hardcode 正在创建 wrapper 脚本修复。\"}, \"exp-005-p1-v4\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-22T14:49:36.217Z\", \"updated_at\": \"2026-05-22T14:49:36.217Z\", \"spec\": {\"command\": \"bash -c \\\"bash /root/entrainment_gated_ft/results/exp005_zoo_expansion/run_p1_v4.sh\\\"\", \"server\": \"westb-48145\", \"gpu\": [\"cuda:0\"], \"pid\": \"870648\", \"log_path\": \"~/runs/entrainment_gated_ft/exp-005-p1-v4.log\", \"submitted_at\": \"2026-05-22T14:49:36.151Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"exp-005-eval\": {\"status\": \"PENDING\", \"retry_count\": 0, \"created_at\": \"2026-05-22T14:22:49.860Z\", \"updated_at\": \"2026-05-22T14:25:11.027Z\", \"spec\": {\"command\": \"bash -c '\\nset -eo pipefail\\nsource /etc/network_turbo\\nsource /root/miniconda3/etc/profile.d/conda.sh && conda activate base\\nexport HF_HOME=/root/autodl-tmp/.hf_cache\\nexport HF_HUB_DISABLE_XET=1\\nexport REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt\\nexport SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt\\n\\nMODELS_DIR=\\\"/root/entrainment_gated_ft/models\\\"\\nRESULTS_DIR=\\\"/root/entrainment_gated_ft/results/exp005_zoo_expansion\\\"\\nLOG=\\\"$RESULTS_DIR/run_all.log\\\"\\nmkdir -p \\\"$RESULTS_DIR\\\"\\n\\necho \\\"=== EXP-005 FULL RUN $(date) ===\\\" | tee \\\"$LOG\\\"\\n\\n# Phase 1: Download missing Priority 1 models (GLA already done)\\nfor arch in DeltaNet HGRN; do\\n  MODEL_NAME=\\\"340M-20B-${arch}-hybrid-3-1\\\"\\n  MODEL_DIR=\\\"$MODELS_DIR/$MODEL_NAME\\\"\\n  if [ ! -f \\\"$MODEL_DIR/model.safetensors\\\" ]; then\\n    echo \\\"Downloading $MODEL_NAME ...\\\" | tee -a \\\"$LOG\\\"\\n    rm -rf \\\"$MODEL_DIR\\\"\\n    huggingface-cli download \\\"m-a-p/$MODEL_NAME\\\" --local-dir \\\"$MODEL_DIR\\\" 2>&1 | tail -5 | tee -a \\\"$LOG\\\"\\n    echo \\\"Downloaded $MODEL_NAME $(date)\\\" | tee -a \\\"$LOG\\\"\\n  else\\n    echo \\\"Already have $MODEL_NAME\\\" | tee -a \\\"$LOG\\\"\\n  fi\\ndone\\n\\n# Phase 2: Evaluate Priority 1 (h3-1 x 3 new archs)\\nfor arch in GLA DeltaNet HGRN; do\\n  MODEL_NAME=\\\"340M-20B-${arch}-hybrid-3-1\\\"\\n  MODEL_DIR=\\\"$MODELS_DIR/$MODEL_NAME\\\"\\n  OUT_DIR=\\\"$RESULTS_DIR/${arch}_hybrid-3-1\\\"\\n  echo \\\"EVAL $MODEL_NAME START $(date)\\\" | tee -a \\\"$LOG\\\"\\n  python -m lm_eval \\\\\\n    --model hf \\\\\\n    --model_args pretrained=$MODEL_DIR,trust_remote_code=True \\\\\\n    --tasks lambada_openai,arc_easy \\\\\\n    --device cuda:0 \\\\\\n    --batch_size auto \\\\\\n    --log_samples \\\\\\n    --output_path \\\"$OUT_DIR/\\\" 2>&1 | tail -10 | tee -a \\\"$LOG\\\"\\n  echo \\\"EVAL $MODEL_NAME DONE $(date)\\\" | tee -a \\\"$LOG\\\"\\ndone\\n\\necho \\\"=== PRIORITY 1 COMPLETE $(date) ===\\\" | tee -a \\\"$LOG\\\"\\n\\n# Phase 3: Download + evaluate remaining ratios\\nfor arch in GLA DeltaNet HGRN; do\\n  for ratio in pure-baseline hybrid-24-1 hybrid-12-1 hybrid-6-1; do\\n    MODEL_NAME=\\\"340M-20B-${arch}-${ratio}\\\"\\n    MODEL_DIR=\\\"$MODELS_DIR/$MODEL_NAME\\\"\\n    OUT_DIR=\\\"$RESULTS_DIR/${arch}_${ratio}\\\"\\n\\n    if [ ! -f \\\"$MODEL_DIR/model.safetensors\\\" ]; then\\n      echo \\\"Downloading $MODEL_NAME ...\\\" | tee -a \\\"$LOG\\\"\\n      rm -rf \\\"$MODEL_DIR\\\"\\n      huggingface-cli download \\\"m-a-p/$MODEL_NAME\\\" --local-dir \\\"$MODEL_DIR\\\" 2>&1 | tail -3 | tee -a \\\"$LOG\\\"\\n      if [ ! -f \\\"$MODEL_DIR/model.safetensors\\\" ]; then\\n        ALT_NAME=\\\"340M-20B-${arch}-pure\\\"\\n        if [ \\\"$ratio\\\" = \\\"pure-baseline\\\" ]; then\\n          echo \\\"Trying alternate: $ALT_NAME ...\\\" | tee -a \\\"$LOG\\\"\\n          huggingface-cli download \\\"m-a-p/$ALT_NAME\\\" --local-dir \\\"$MODELS_DIR/$ALT_NAME\\\" 2>&1 | tail -3 | tee -a \\\"$LOG\\\"\\n          MODEL_DIR=\\\"$MODELS_DIR/$ALT_NAME\\\"\\n        fi\\n      fi\\n      echo \\\"Downloaded $(date)\\\" | tee -a \\\"$LOG\\\"\\n    fi\\n\\n    echo \\\"EVAL $MODEL_NAME START $(date)\\\" | tee -a \\\"$LOG\\\"\\n    python -m lm_eval \\\\\\n      --model hf \\\\\\n      --model_args pretrained=$MODEL_DIR,trust_remote_code=True \\\\\\n      --tasks lambada_openai,arc_easy \\\\\\n      --device cuda:0 \\\\\\n      --batch_size auto \\\\\\n      --log_samples \\\\\\n      --output_path \\\"$OUT_DIR/\\\" 2>&1 | tail -10 | tee -a \\\"$LOG\\\"\\n    echo \\\"EVAL $MODEL_NAME DONE $(date)\\\" | tee -a \\\"$LOG\\\"\\n  done\\ndone\\n\\necho \\\"=== ALL EVALUATIONS COMPLETE $(date) ===\\\" | tee -a \\\"$LOG\\\"\\n'\", \"server\": \"westb-48145\", \"gpu\": [\"cuda:0\"], \"pid\": \"unknown\", \"log_path\": \"~/runs/entrainment_gated_ft/exp-005-eval.log\", \"submitted_at\": \"2026-05-22T14:22:49.797Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"reproduce\": {\"finished_at\": \"2026-05-22T14:23:13.448Z\"}, \"failure_reason\": \"EXIT_CODE=1 (generic error — check log tail)\", \"conclusion\": \"killed\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-22T14:23:17.070767+00:00\"}]}, \"hypothesis\": \"Cross-architecture per-example Jaccard (helped/hurt) remains ≤0.10 when expanding from 3 architectures (GDN/RetNet/HGRN2) to 6 (adding GLA/DeltaNet/HGRN), with 15 pairwise comparisons and 720 permutations providing dramatically stronger statistical power.\"}, \"e4-pythia-seed-calibration\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T10:17:05.445Z\", \"updated_at\": \"2026-05-22T11:44:42.532Z\", \"hypothesis\": \"Pythia 70M 9-seed variants 的 within-seed per-example Jaccard (same architecture, different random seed) 显著高于 cross-architecture Jaccard (~0.10), 证明 within-arch overlap >> cross-arch overlap, 即 cross-arch 信号不能被 seed noise 解释。\", \"parent\": \"exp-001\", \"spec\": {\"command\": \"lm_eval --model hf --tasks lambada_openai,arc_easy --log_samples\", \"server\": \"westb-48145\", \"model_name\": \"EleutherAI/pythia-70m-seed{1-9}\", \"seed\": \"1-9\", \"data_path\": \"/root/entrainment_gated_ft/results/e4_pythia_seed/\", \"data_count\": \"5153+2376 per seed × 9 seeds\", \"checkpoint_source\": \"ModelScope CDN\", \"eval_data\": \"lambada_openai + arc_easy\", \"checkpoint_path\": \"/root/autodl-tmp/pythia_weights_70m/seed{1-9}/\", \"log_path\": \"/root/entrainment_gated_ft/results/e4_pythia_seed/eval.log\"}, \"reproduce\": {\"finished_at\": \"2026-05-22T11:10:00.780Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-22T11:10:01.238Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-22T11:10:03.664374+00:00\"}]}, \"metrics\": {\"lambada_J_helped\": 0.273, \"lambada_J_hurt\": 0.393, \"lambada_alpha\": 0.355, \"arc_J_helped\": 0.312, \"arc_alpha\": 0.491, \"cross_arch_ref_J_helped\": 0.1, \"ratio_lambada\": 2.73, \"ratio_arc\": 3.12}}, \"exp-340m-multi-bench\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T22:23:25.467Z\", \"updated_at\": \"2026-05-22T00:34:02.116Z\", \"hypothesis\": \"340M models exhibit α spectrum (per-example ambiguity) consistent with 1.3B across HellaSwag/PIQA/ARC-Easy — establishing scale-invariance of the multiplicity phenomenon beyond the single-benchmark (LAMBADA) evidence in §4.3. If α_340M ≈ α_1.3B per benchmark, cross-scale stability is confirmed; if systematically different, the scale-dependency claim needs qualification.\", \"parent\": \"exp-007\", \"spec\": {\"command\": \"bash run_340m_multi_eval.sh (run_lmeval_clean.py × 15 models × 3 tasks with --log_samples)\", \"server\": \"westb-48145\", \"gpu\": [\"cuda:0\"], \"data_path\": \"/root/entrainment_gated_ft/models/ (15 × 340M models)\", \"data_count\": \"hellaswag=10042, piqa=1838, arc_easy=2376 per model\", \"model_name\": \"GDN/RetNet/HGRN2 × 5 ratios (340M, 15 models)\", \"seed\": \"default\", \"checkpoint_source\": \"/root/entrainment_gated_ft/models/340M-20B-*\", \"eval_data\": \"HellaSwag (10042) + PIQA (1838) + ARC-Easy (2376)\", \"pid\": \"777365\", \"log_path\": \"~/runs/entrainment_gated_ft/exp-340m-multi-bench.log\", \"submitted_at\": \"2026-05-21T22:27:20Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"/root/entrainment_gated_ft/lm_eval_clean/340m_multi/\", \"wall_clock_seconds\": 7602.1, \"gpu_hours\": 2.11}, \"conclusion\": \"success\", \"metrics\": {\"hellaswag_acc_norm\": {\"340m_alpha_all\": 0.334, \"1_3b_alpha_all\": 0.302, \"delta\": 0.031, \"340m_alpha_pure\": 0.167, \"1_3b_alpha_pure\": 0.148, \"340m_J_helped\": 0.084, \"1_3b_J_helped\": 0.095, \"340m_J_hurt\": 0.083, \"1_3b_J_hurt\": 0.085, \"340m_convergence_rho\": 0.4, \"340m_convergence_p\": 0.517}, \"piqa\": {\"340m_alpha_all\": 0.366, \"1_3b_alpha_all\": 0.278, \"delta\": 0.089, \"340m_alpha_pure\": 0.181, \"1_3b_alpha_pure\": 0.143, \"340m_J_helped\": 0.09, \"1_3b_J_helped\": 0.091, \"340m_J_hurt\": 0.085, \"1_3b_J_hurt\": 0.094, \"340m_convergence_rho\": 0.3, \"340m_convergence_p\": 0.683}, \"arc_easy\": {\"340m_alpha_all\": 0.564, \"1_3b_alpha_all\": 0.434, \"delta\": 0.13, \"340m_alpha_pure\": 0.289, \"1_3b_alpha_pure\": 0.205, \"340m_J_helped\": 0.098, \"1_3b_J_helped\": 0.092, \"340m_J_hurt\": 0.103, \"1_3b_J_hurt\": 0.099, \"340m_convergence_rho\": -0.1, \"340m_convergence_p\": 0.95}, \"summary\": {\"mean_delta_alpha_all\": 0.084, \"scenario\": \"B_mixed\", \"pattern_invariant\": true, \"magnitude_scale_dependent\": true}, \"artifacts\": [\"340m_multi_bench_analysis.json\"]}, \"completed_at\": \"2026-05-22T00:34:02.116Z\"}, \"w3-winogrande-piqa-eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T08:28:29.577Z\", \"updated_at\": \"2026-05-21T10:27:33.995Z\", \"spec\": {\"command\": \"bash run_winogrande_piqa_all.sh (run_lmeval_clean.py × 30 tasks)\", \"server\": \"westb-48145\", \"gpu\": [\"cuda:0\"], \"pid\": \"722233\", \"log_path\": \"/root/entrainment_gated_ft/lm_eval_clean/winogrande_piqa_eval.log\", \"submitted_at\": \"2026-05-21T08:28:29.524Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"lm-eval-harness winogrande + piqa\", \"data_count\": \"winogrande=1267, piqa=1838\", \"model_name\": \"GDN/RetNet/HGRN2 × 5 ratios (1.3B)\", \"seed\": \"default\", \"checkpoint_path\": \"artifacts/paper_data/winogrande_per_example.json + piqa_per_example.json\", \"wall_clock_seconds\": 7144.5, \"gpu_hours\": 1.98}, \"hypothesis\": \"WinoGrande + PIQA per-example multiplicity analysis to decouple format (2-choice vs 4-way MC) from task-type as driver of ambiguity α spectrum, addressing Round 5 W3 format confound concern\", \"conclusion\": \"success\", \"metrics\": {\"winogrande\": {\"n_samples\": 1267, \"alpha_pure\": 0.463, \"alpha_range\": [0.409, 0.463], \"convergence_rho\": -0.2, \"convergence_p\": 0.783}, \"piqa\": {\"n_samples\": 1838, \"alpha_pure\": 0.143, \"alpha_range\": [0.132, 0.143], \"convergence_rho\": -0.5, \"convergence_p\": 0.45}, \"format_confound_test\": {\"finding\": \"PIQA (2-choice, α=0.14) vs WinoGrande (2-choice, α=0.46) vs BoolQ (2-choice, α=0.51) — same format, 3.5× α variation. Format confound refuted.\", \"alpha_vs_accuracy_rho\": 0.03, \"alpha_vs_accuracy_p_exact\": 1}, \"artifacts\": [\"winogrande_per_example.json\", \"piqa_per_example.json\", \"winogrande_jaccard_analysis.json\", \"piqa_jaccard_analysis.json\"]}, \"completed_at\": \"2026-05-21T10:27:33.995Z\"}, \"exp-boolq-hellaswag-eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T11:32:21.428Z\", \"updated_at\": \"2026-05-21T08:53:38.336Z\", \"spec\": {\"command\": \"bash run_boolq_hellaswag_all.sh\", \"server\": \"westb-48145\", \"gpu\": [\"cuda:0\"], \"pid\": \"653104\", \"log_path\": \"~/runs/entrainment_gated_ft/exp-boolq-hellaswag-eval.log\", \"submitted_at\": \"2026-05-20T11:32:21.381Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/entrainment_gated_ft/lm_eval_clean/\", \"data_count\": 13312, \"model_name\": \"GDN/RetNet/HGRN2 x 5 ratios + Transformer (15 models)\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/models_1.3b/\", \"eval_data\": \"BoolQ (3270 samples) + HellaSwag (10042 samples)\", \"wall_clock_seconds\": 76877.0, \"gpu_hours\": 21.35}, \"reproduce\": {\"finished_at\": \"2026-05-20T12:47:53.740Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-20T12:47:55.697105+00:00\"}]}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/entrainment_gated_ft/lm_eval_clean/boolq/ + /root/entrainment_gated_ft/lm_eval_clean/hellaswag/\", \"log_path\": \"/root/entrainment_gated_ft/lm_eval_clean/boolq_hellaswag_eval.log\", \"metrics\": {\"benchmarks\": [\"boolq\", \"hellaswag\"], \"boolq\": {\"n_samples\": 3270, \"ambiguity_alpha_mean\": 0.487, \"jaccard_helped_mean\": 0.103, \"jaccard_hurt_mean\": 0.098, \"convergence_rho\": 0.1, \"convergence_p\": 0.95, \"note\": \"GDN h24-1 acc=0.489 (near random) is genuine model performance, not eval bug. Selective overlap: GDN-RetNet significant, but GDN-HGRN2 and RetNet-HGRN2 often not significant\"}, \"hellaswag\": {\"n_samples\": 10042, \"ambiguity_alpha_mean\": 0.098, \"jaccard_helped_mean\": 0.091, \"jaccard_hurt_mean\": 0.08, \"convergence_rho\": -0.8, \"convergence_p\": 0.133, \"note\": \"90% samples unanimous across architectures. All Jaccard p<0.001 but nES very small (0.05-0.11)\"}, \"four_benchmark_summary\": {\"spectrum\": \"HellaSwag(α=0.10) < ARC-Easy(α=0.21) < LAMBADA(α=0.30) < BoolQ(α=0.49)\", \"key_finding\": \"Multiplicity varies dramatically by task (10%-49%) while Jaccard overlap stays consistently low (~0.08-0.10). Per-example divergence is universal but magnitude is task-dependent.\"}, \"artifacts\": [\"boolq_per_example.json\", \"boolq_jaccard_analysis.json\", \"hellaswag_per_example.json\", \"hellaswag_jaccard_analysis.json\"]}, \"hypothesis\": \"BoolQ 和 HellaSwag 的 per-example log_samples 数据扩展 multiplicity 分析到更多 benchmark，验证 per-example predictive multiplicity（α 和 cross-architecture Jaccard divergence）在不同任务类型上的普遍性——建立从 LAMBADA/ARC-Easy 到 4-benchmark spectrum 的泛化\", \"parent\": \"exp-011\", \"completed_at\": \"2026-05-21T08:53:38.336Z\"}, \"exp-015\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T10:05:29.020Z\", \"updated_at\": \"2026-05-20T10:06:09.562Z\", \"hypothesis\": \"Per-example predictive multiplicity (cross-architecture Jaccard divergence of helped/hurt sets, formal ambiguity α) exists on ARC-Easy (N=2376) even without aggregate convergence, establishing that multiplicity is a general property of hybrid architectures independent of task-specific convergence\", \"parent\": \"exp-arc-easy-eval\", \"spec\": {\"command\": \"Python analysis on westb-48145 (CPU)\", \"server\": \"westb-48145\", \"data_path\": \"/root/entrainment_gated_ft/lm_eval_clean/arc_easy/\", \"data_count\": 2376, \"model_name\": \"GDN/RetNet/HGRN2 x 5 ratios (15 models)\", \"seed\": \"N/A (deterministic eval)\", \"checkpoint_source\": \"exp-arc-easy-eval\", \"eval_data\": \"ARC-Easy (2376 samples)\"}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/entrainment_gated_ft/lm_eval_clean/arc_easy/\", \"log_path\": \"/root/entrainment_gated_ft/lm_eval_clean/arc_easy/\", \"completed_at\": \"2026-05-20T10:06:01.194Z\", \"metrics\": {\"benchmark\": \"arc_easy\", \"n_samples\": 2376, \"convergence\": {\"spearman_rho\": -0.2, \"p_exact\": 0.783, \"significant\": false}, \"jaccard_range\": {\"helped\": [0.067, 0.117], \"hurt\": [0.079, 0.134]}, \"normalized_ES_range\": [0.035, 0.135], \"all_24_jaccard_above_null\": true, \"multiplicity_arc_easy\": {\"alpha_range\": [0.201, 0.226], \"delta_range\": [2.32, 3.12]}, \"multiplicity_lambada\": {\"alpha_range\": [0.294, 0.316], \"delta_range\": [0.53, 0.61]}, \"claim\": \"Claim 3: per-example predictive multiplicity is general\", \"artifacts\": [\"arc_easy_per_example.json\", \"arc_easy_jaccard_analysis.json\", \"formal_multiplicity_metrics.json\"]}}, \"exp-arc-easy-eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T06:08:47.284Z\", \"updated_at\": \"2026-05-20T09:46:49.153Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/entrainment_gated_ft && bash run_arc_easy_all.sh\\\"\", \"server\": \"westb-48145\", \"gpu\": [\"cuda:0\"], \"pid\": \"620603\", \"log_path\": \"~/runs/entrainment_gated_ft/exp-arc-easy-eval.log\", \"submitted_at\": \"2026-05-20T06:08:47.244Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 11793.6, \"gpu_hours\": 3.28}, \"hypothesis\": \"Per-example divergence (low cross-architecture Jaccard of helped/hurt sets) exists on ARC-Easy as well as LAMBADA, establishing that per-example underspecification is not task-specific even when aggregate convergence is absent\", \"parent\": \"exp-001\", \"conclusion\": \"success\", \"checkpoint_path\": \"/root/entrainment_gated_ft/lm_eval_clean/arc_easy/\", \"log_path\": \"/root/entrainment_gated_ft/lm_eval_clean/arc_easy/\", \"completed_at\": \"2026-05-20T09:25:20.825Z\", \"metrics\": {\"benchmark\": \"arc_easy\", \"n_samples\": 2376, \"models_completed\": \"15/15\", \"acc_range\": [0.6961, 0.7412], \"convergence\": {\"spearman_rho\": -0.2, \"p_exact\": 0.783, \"significant\": false, \"sigma_pure\": 0.0964, \"sigma_h3_1\": 0.099}, \"jaccard_range\": {\"helped\": [0.067, 0.117], \"hurt\": [0.079, 0.134]}, \"normalized_ES_range\": [0.035, 0.135], \"all_24_jaccard_above_null\": true, \"multiplicity\": {\"alpha_range\": [0.201, 0.226], \"delta_range\": [2.32, 3.12]}, \"lambada_multiplicity\": {\"alpha_range\": [0.294, 0.316], \"delta_range\": [0.53, 0.61]}, \"key_finding\": \"Per-example multiplicity exists on ARC-Easy (alpha~0.21, Jaccard~0.07-0.13) WITHOUT aggregate convergence (rho=-0.20,p=0.78). Combined with LAMBADA (alpha~0.30 WITH convergence), per-example multiplicity is a general property not tied to convergence.\", \"artifacts\": [\"arc_easy_per_example.json\", \"arc_easy_jaccard_analysis.json\", \"formal_multiplicity_metrics.json\"]}}, \"exp-007\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T17:08:19.724Z\", \"updated_at\": \"2026-05-19T18:53:42.640Z\", \"hypothesis\": \"340M models show non-monotonic rebound in cross-architecture convergence at high attention ratios on LAMBADA, caused by capacity-limited interaction between attention and recurrent components — the rebound mechanism differs from 1.3B's complete convergence, establishing scale as a necessary condition for full equalization\", \"parent\": \"exp-001\", \"spec\": {\"command\": \"bash run_exp007_logsamples.sh (run_lmeval_clean.py with allow_neg_eigval=True, --log_samples, --tasks lambada_openai)\", \"server\": \"westb-48145\", \"gpu\": \"cuda:0\", \"pid\": 530432, \"log_path\": \"~/runs/entrainment_gated_ft/exp-007.log\", \"submitted_at\": \"2026-05-19T17:51:40.355Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"lambada_openai (lm-eval built-in)\", \"data_count\": \"5153 per model x 27 models\", \"model_name\": \"340M x16 + 1.3B x11 (GDN/RetNet/HGRN2 hybrids + Transformer)\", \"seed\": \"default\", \"checkpoint_source\": \"m-a-p pretrained (340M: /root/autodl-tmp/models/, 1.3B: /root/autodl-tmp/models_1.3b/)\", \"eval_data\": \"lambada_openai (lm-eval built-in, 5153 samples)\", \"checkpoint_path\": \"/root/entrainment_gated_ft/lm_eval_clean/exp007/\", \"wall_clock_seconds\": 3722.3, \"gpu_hours\": 1.03}, \"reproduce\": {\"finished_at\": \"2026-05-19T18:49:39.310Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-19T18:49:41.012664+00:00\"}]}, \"metrics\": {\"340m_cross_arch_std\": {\"pure\": 0.02481, \"h24-1\": 0.011647, \"h12-1\": 0.017833, \"h6-1\": 0.011035, \"h3-1\": 0.016004}, \"340m_spearman_rho\": -0.5, \"340m_spearman_perm_p\": 0.45, \"1.3b_spearman_rho_ref\": -1, \"1.3b_spearman_perm_p_ref\": 0.0167, \"rebound_h3_1_delta\": 0.004969, \"rebound_h12_1_delta\": 0.006186, \"340m_h3_1_helped_jaccard\": 0.0944, \"340m_h3_1_hurt_jaccard\": 0.0899, \"models_completed\": 26, \"models_skipped\": 1}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-19T18:53:42.640Z\"}, \"exp-004-r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T16:58:01.256Z\", \"updated_at\": \"2026-05-19T17:17:20.215Z\", \"hypothesis\": \"Attention weight patterns in hybrid h3-1 models differ systematically between helped and hurt samples on LAMBADA, with cross-architecture attention pattern similarity lower than expected given aggregate convergence — providing mechanistic evidence for architecture-specific per-example effects (Claim 3)\", \"parent\": \"exp-004\", \"spec\": {\"command\": \"python -u analysis/extract_attention_weights.py --arch {gdn,retnet,hgrn2} --device cuda:0 (sequential per arch)\", \"server\": \"westb-48145\", \"data_path\": \"EleutherAI/lambada_openai (default, split=test, cached)\", \"data_count\": 5153, \"model_name\": \"1.3B-100B-{GatedDeltaNet,RetNet,HGRN2}-hybrid-3-1\", \"seed\": 0, \"gpu\": \"cuda:0 (RTX PRO 6000)\", \"checkpoint_source\": \"/root/autodl-tmp/models_1.3b/\", \"eval_data\": \"LAMBADA OpenAI (5153 samples)\", \"log_path\": \"/tmp/exp004.log\", \"pid\": 517172, \"output_dir\": \"/root/entrainment_gated_ft/analysis/attention_weights/\", \"progress\": \"gdn=DONE, retnet=42% running (PID 517172), hgrn2=PENDING\", \"session\": \"process detached with fd redirect to /tmp/exp004.log; tmux unavailable on server; screen available for hgrn2\", \"checkpoint_path\": \"/root/entrainment_gated_ft/analysis/attention_weights/\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-19T17:17:10.232Z\", \"metrics\": {\"helped_vs_hurt_entropy_diff\": {\"gdn\": -0.0009, \"retnet\": 0.0179, \"hgrn2\": 0.002}, \"helped_vs_hurt_last5_mass\": {\"gdn_helped\": 0.0834, \"gdn_hurt\": 0.0831, \"retnet_helped\": 0.1578, \"retnet_hurt\": 0.1591, \"hgrn2_helped\": 0.0453, \"hgrn2_hurt\": 0.0467}, \"cross_arch_similarity_mean\": {\"gdn_vs_retnet\": 0.905, \"gdn_vs_hgrn2\": 0.766, \"hgrn2_vs_retnet\": 0.698}, \"cross_arch_similarity_deep_layers\": {\"gdn_vs_retnet_L20\": 0.986, \"gdn_vs_hgrn2_L20\": 0.942, \"hgrn2_vs_retnet_L20\": 0.943}, \"cross_arch_similarity_early_layers\": {\"gdn_vs_retnet_L2\": 0.995, \"gdn_vs_hgrn2_L2\": 0.244, \"hgrn2_vs_retnet_L2\": 0.196}, \"finding\": \"Attention entropy does NOT differentiate helped vs hurt samples — differences are negligible across all 3 architectures. Cross-arch: GDN and RetNet highly similar throughout; HGRN2 diverges in early layers but converges in deep layers (>0.94 at L20). The per-example effect is not visible at the attention pattern level.\", \"n_samples\": 5153, \"runtime_minutes\": 30, \"output_files\": [\"gdn_attention_patterns.pt\", \"gdn_attention_entropy.csv\", \"retnet_attention_patterns.pt\", \"retnet_attention_entropy.csv\", \"hgrn2_attention_patterns.pt\", \"hgrn2_attention_entropy.csv\", \"attention_analysis_summary.json\", \"cross_arch_attention_similarity.csv\", \"helped_vs_hurt_entropy.csv\"]}}, \"exp-011-xstorycloze\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T16:18:38.168Z\", \"updated_at\": \"2026-05-19T17:00:01.089Z\", \"hypothesis\": \"xstorycloze_en (StoryCloze equivalent, context completion task) shows significant cross-architecture convergence with attention ratio, providing a second statistically significant anchor beyond LAMBADA after Bonferroni correction\", \"parent\": \"exp-011\", \"spec\": {\"command\": \"bash /root/entrainment_gated_ft/run_xstorycloze_batch.sh (PID 497694)\", \"server\": \"westb-48145\", \"data_path\": \"/root/autodl-tmp/models_1.3b/ (16 models)\", \"data_count\": 16, \"model_name\": \"GDN/RetNet/HGRN2 x 5 ratios + Transformer baseline (1.3B)\", \"seed\": 0, \"checkpoint_source\": \"/root/autodl-tmp/models_1.3b/ (Wang et al. pretrained)\", \"eval_data\": \"xstorycloze_en (juletxara/xstory_cloze, en split)\", \"gpu\": \"cuda:0 (RTX PRO 6000)\"}, \"conclusion\": \"negative\", \"checkpoint_path\": \"/root/entrainment_gated_ft/lm_eval_clean/xstorycloze/\", \"log_path\": \"/root/entrainment_gated_ft/nohup.out\", \"completed_at\": \"2026-05-19T16:32:04.959Z\", \"metrics\": {\"xstorycloze_en\": {\"rho\": -0.6, \"raw_p\": 0.35, \"bonferroni_adj_p_10\": 1, \"std_pure\": 0.0082, \"std_h3_1\": 0.0055, \"convergence_direction\": \"correct but weak\"}, \"ten_benchmark_bonferroni\": {\"significant_count\": \"0/10\", \"LAMBADA_adj_p\": 0.167, \"note\": \"No benchmark survives 10-benchmark Bonferroni\"}, \"method\": \"exact_permutation_test_two_tailed\", \"conclusion\": \"xstorycloze_en NOT a second anchor. Convergence is LAMBADA-specific. W1 unresolved via multi-benchmark approach.\"}}, \"exp-004\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T16:41:10.744Z\", \"updated_at\": \"2026-05-19T16:57:48.978Z\", \"hypothesis\": \"Attention layers in hybrid-3-1 models exhibit systematically different attention patterns (entropy, position distribution) between helped and hurt samples on LAMBADA, revealing how attention mediates the entrainment-gating effect across architectures.\", \"parent\": \"exp-003\", \"spec\": {\"command\": \"python extract_attention_weights.py (forward hooks on Q,K, manual softmax(QK^T/√d) with GQA expansion)\", \"server\": \"westb-48145\", \"data_path\": \"/root/entrainment_gated_ft/lm_eval_clean/lambada_openai per-example data\", \"data_count\": 5153, \"model_name\": \"GDN-h3-1, RetNet-h3-1, HGRN2-h3-1 (1.3B)\", \"seed\": 42, \"gpu\": \"cuda:0\", \"checkpoint_source\": \"Wang et al. pretrained weights\", \"eval_data\": \"lambada_openai (5153 examples)\", \"log_path\": \"/tmp/exp004.log (process died after Worker exited - nohup orphan)\", \"checkpoint_path\": \"N/A - process crashed before completion\", \"failure_reason\": \"Worker used nohup instead of submit_training_job/tmux; PID 515917 died after Worker exit. GPU idle since ~16:47 UTC.\"}, \"conclusion\": \"failed\", \"completed_at\": \"2026-05-19T16:57:48.978Z\"}, \"exp-011\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T14:12:29.428Z\", \"updated_at\": \"2026-05-19T16:37:27.600Z\", \"hypothesis\": \"Cross-architecture variance on additional retrieval-dependent benchmarks (StoryCloze, BoolQ, COPA, PIQA, SciQ) decreases monotonically with attention ratio, providing a second statistically significant anchor (exact permutation p<0.05, two-tailed) beyond LAMBADA after Bonferroni correction\", \"parent\": \"exp-001\", \"spec\": {\"command\": \"bash /root/entrainment_gated_ft/run_exp011_batch.sh (nohup PID 474289)\", \"server\": \"westb-48145\", \"data_path\": \"/root/autodl-tmp/models_1.3b/ (16 models)\", \"data_count\": 16, \"model_name\": \"GDN/RetNet/HGRN2 x 5 ratios + Transformer baseline (1.3B)\", \"seed\": 0, \"eval_data\": \"boolq, copa, piqa, sciq (4 benchmarks x 16 models)\", \"gpu\": \"cuda:0 (RTX PRO 6000)\", \"checkpoint_source\": \"/root/autodl-tmp/models_1.3b/ (Wang et al. pretrained checkpoints)\"}, \"conclusion\": \"negative\", \"checkpoint_path\": \"/root/entrainment_gated_ft/lm_eval_clean/exp011/\", \"log_path\": \"/root/entrainment_gated_ft/lm_eval_clean/exp011/run_all.log\", \"completed_at\": \"2026-05-19T16:14:41.324Z\", \"metrics\": {\"boolq\": {\"rho\": 0.2, \"raw_p\": 0.7833, \"bonferroni_adj_p_9\": 1, \"std_pure\": 0.0163, \"std_h3_1\": 0.0236, \"convergence\": false}, \"piqa\": {\"rho\": -0.5, \"raw_p\": 0.45, \"bonferroni_adj_p_9\": 1, \"std_pure\": 0.0054, \"std_h3_1\": 0.0034, \"convergence\": false}, \"sciq\": {\"rho\": 0.1, \"raw_p\": 0.95, \"bonferroni_adj_p_9\": 1, \"std_pure\": 0.0087, \"std_h3_1\": 0.0074, \"convergence\": false}, \"copa_supplementary\": {\"rho\": -0.67, \"raw_p\": 0.2667, \"std_pure\": 0.0262, \"std_h3_1\": 0.0047, \"convergence_ratio\": 5.57, \"note\": \"supplementary only (n=100), not in main Bonferroni\"}, \"LAMBADA_recomputed\": {\"rho\": -1, \"raw_p\": 0.0167, \"bonferroni_adj_p_6\": 0.1, \"bonferroni_adj_p_10\": 0.167, \"note\": \"6-Bonf=0.100 (D003 pre-registered); 10-Bonf=0.167; does not survive strict Bonferroni\"}, \"merged_10benchmark_significant_count\": \"0/10\", \"method\": \"exact_permutation_test_two_tailed\", \"D009_strategy\": \"BCa CI [-1.0,-0.7] as primary evidence; 6-Bonf adj_p=0.100 reported honestly; 10-benchmark negative -> task-specificity positive evidence (supplementary); underpowered caveat in Limitations\", \"D009_prohibited\": \"NO post-hoc 2-benchmark Bonferroni; NO post-hoc rho<0 subset correction\", \"conclusion\": \"No second anchor. Convergence LAMBADA-specific. W1 addressed via task-specificity reframing (D009).\"}}, \"exp-010\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T15:08:21.255Z\", \"updated_at\": \"2026-05-19T15:12:28.565Z\", \"hypothesis\": \"Aggregate convergence (cross-arch std decreasing with attention ratio) and per-example divergence (low Jaccard of helped/hurt sets) co-evolve as attention ratio increases on LAMBADA — demonstrating underspecification: architectures converge in aggregate performance while helping/hurting almost entirely different samples\", \"parent\": \"exp-001\", \"spec\": {\"command\": \"python3 /root/entrainment_gated_ft/analysis/exp010_bridge_analysis.py\", \"server\": \"westb-48145\", \"data_path\": \"/root/entrainment_gated_ft/lm_eval_clean/\", \"data_count\": 5153, \"model_name\": \"GDN/RetNet/HGRN2 x 5 ratios (1.3B)\", \"seed\": 0, \"checkpoint_source\": \"/root/autodl-tmp/models_1.3b/ (Wang et al. pretrained)\", \"eval_data\": \"LAMBADA OpenAI per-example logprob (5153 samples)\"}, \"checkpoint_path\": \"/root/entrainment_gated_ft/analysis/exp010_bridge_results.csv\", \"log_path\": \"/root/entrainment_gated_ft/analysis/exp010_bridge_summary.json\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-19T15:09:01.266Z\", \"metrics\": {\"aggregate_convergence\": {\"std_pure\": 0.024, \"std_h24_1\": 0.0162, \"std_h12_1\": 0.0136, \"std_h6_1\": 0.0061, \"std_h3_1\": 0.0049, \"reduction_ratio\": 0.8, \"note\": \"Cross-arch std drops 5x monotonically\"}, \"per_example_divergence\": {\"jaccard_helped_range\": [0.092, 0.1], \"jaccard_hurt_range\": [0.081, 0.099], \"net_asymmetry_range\": [0.013, 0.04], \"net_asymmetry_trend\": \"increasing with attention ratio\", \"note\": \"Jaccard saturates at ~0.095 by 4% attention (h24-1), flat thereafter\"}, \"co_evolution_spearman\": {\"std_vs_J_helped\": {\"rho\": -0.7, \"exact_p\": 0.23}, \"std_vs_J_hurt\": {\"rho\": -0.8, \"exact_p\": 0.13}, \"CAVEAT\": \"D008: rho inflated by pure=0 degeneracy (Jaccard=NaN->0). Excluding pure: rho=-0.40, p=0.75. NOT co-evolution.\"}, \"key_finding\": \"DECOUPLING (D008): minimal attention (4%) creates per-example specificity (Jaccard saturates ~0.095), gradual attention drives aggregate convergence (sigma 0.024->0.005). Two processes operate on different timescales. Net asymmetry INCREASES (0.013->0.040).\", \"narrative_constraints\": \"PROHIBITED: co-evolution, paradoxical coexistence, paradox. USE: decoupling, different timescales.\"}}, \"exp-001\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T13:32:43.793Z\", \"updated_at\": \"2026-05-19T15:00:43.856Z\", \"hypothesis\": \"Cross-architecture variance (std) on retrieval-dependent tasks decreases monotonically with attention ratio at 1.3B scale, while reasoning-dependent tasks show no convergence — establishing task-specificity as a principled feature of the equalizer effect, not a limitation\", \"spec\": {\"command\": \"python analysis: compute cross-arch std + Spearman rho for 6 benchmarks x 5 attention ratios\", \"server\": \"westb-48145\", \"data_path\": \"/root/entrainment_gated_ft/lm_eval_clean/ (summary_all_1.3b.csv + 340M results)\", \"data_count\": 26, \"model_name\": \"16x1.3B + 10x340M (GDN/RetNet/HGRN2)\", \"seed\": 0}, \"checkpoint_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/exp-001/data/task_specificity_results.csv\", \"log_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/logs/workers/worker_research_wang_differentiation_20260519T130431.log\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-19T13:33:45.162Z\", \"metrics\": {\"LAMBADA\": {\"rho\": -1, \"p\": 0.0167, \"significant\": false, \"taxonomy\": \"retrieval-dependent\", \"note\": \"exact permutation two-tailed (was 0.008 one-tailed)\"}, \"HellaSwag\": {\"rho\": 0.3, \"p\": 0.6833, \"significant\": false, \"taxonomy\": \"reasoning-dependent\"}, \"ARC-C\": {\"rho\": 0.6, \"p\": 0.35, \"significant\": false, \"taxonomy\": \"reasoning-dependent\"}, \"Winogrande\": {\"rho\": 0.1, \"p\": 0.95, \"significant\": false, \"taxonomy\": \"reasoning-dependent\"}, \"ARC-Easy\": {\"rho\": -0.7, \"p\": 0.2333, \"significant\": false, \"taxonomy\": \"mixed\"}, \"MMLU\": {\"rho\": -0.7, \"p\": 0.2333, \"significant\": false, \"taxonomy\": \"mixed\"}, \"significant_count\": \"0/6\", \"summary\": \"LAMBADA shows perfect negative correlation (rho=-1.0) but exact permutation two-tailed p=0.0167 (Bonferroni adj-p=0.100, not significant). Reasoning tasks show no convergence. Mixed tasks suggestive but underpowered (n=5).\", \"method\": \"exact_permutation_test_two_tailed\"}}, \"exp-008\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T14:12:33.026Z\", \"updated_at\": \"2026-05-19T14:28:33.593Z\", \"hypothesis\": \"Replacing scipy.stats.spearmanr asymptotic p-values with exact permutation tests (n=5, 120 permutations, two-tailed) corrects the spurious p=1.4e-24 bug; expected: LAMBADA raw p≈0.017, Bonferroni adj-p≈0.100 (not significant), confirming need for additional benchmarks\", \"parent\": \"exp-001\", \"checkpoint_path\": \"/root/entrainment_gated_ft/analysis/robustness_results.csv\", \"log_path\": \"/root/entrainment_gated_ft/analysis/robustness_summary.md\", \"conclusion\": \"success\", \"spec\": {\"command\": \"python3 /root/entrainment_gated_ft/analysis/statistical_robustness.py\", \"server\": \"westb-48145\", \"data_path\": \"/root/entrainment_gated_ft/lm_eval_clean/summary_all_1.3b.csv\", \"data_count\": 15, \"model_name\": \"GDN/HGRN2/RetNet 1.3B (5 attn ratios x 3 archs)\", \"seed\": 42, \"checkpoint_source\": \"/root/entrainment_gated_ft/lm_eval_clean/summary_all_1.3b.csv\", \"eval_data\": \"6 benchmarks x 15 model configs (summary_all_1.3b.csv)\"}, \"metrics\": {\"LAMBADA\": {\"rho\": -1, \"raw_p\": 0.0167, \"bonferroni_adj_p\": 0.1, \"bh_fdr_adj_p\": 0.1}, \"HellaSwag\": {\"rho\": 0.3, \"raw_p\": 0.6833, \"bonferroni_adj_p\": 1, \"bh_fdr_adj_p\": 0.82}, \"WinoGrande\": {\"rho\": 0.1, \"raw_p\": 0.95, \"bonferroni_adj_p\": 1, \"bh_fdr_adj_p\": 0.95}, \"ARC-Easy\": {\"rho\": -0.7, \"raw_p\": 0.2333, \"bonferroni_adj_p\": 1, \"bh_fdr_adj_p\": 0.4667}, \"ARC-Challenge\": {\"rho\": 0.6, \"raw_p\": 0.35, \"bonferroni_adj_p\": 1, \"bh_fdr_adj_p\": 0.525}, \"MMLU\": {\"rho\": -0.7, \"raw_p\": 0.2333, \"bonferroni_adj_p\": 1, \"bh_fdr_adj_p\": 0.4667}, \"method\": \"exact_permutation_test_two_tailed\", \"n_permutations\": 120, \"bug_fixed\": \"scipy.stats.spearmanr asymptotic p replaced with exact permutation\", \"bootstrap_ci\": {\"benchmark\": \"LAMBADA\", \"method\": \"architecture_resampling_percentile\", \"ci_lower\": -1, \"ci_upper\": -0.7, \"crosses_zero\": false, \"n_bootstrap\": 10000, \"n_valid\": 8875, \"seed\": 42, \"p_rho_negative\": 1, \"p_rho_positive\": 0, \"bca_note\": \"BCa degenerate at rho=-1.0 boundary; percentile CI used\"}, \"gdn_excluded\": {\"LAMBADA\": {\"rho\": -0.7, \"exact_p\": 0.2333, \"direction\": \"WEAKER\"}, \"HellaSwag\": {\"rho\": 0.5, \"exact_p\": 0.45, \"direction\": \"STRONGER\"}, \"WinoGrande\": {\"rho\": 0.3, \"exact_p\": 0.6833, \"direction\": \"STRONGER\"}, \"ARC-Easy\": {\"rho\": -0.9, \"exact_p\": 0.0833, \"direction\": \"STRONGER\"}, \"ARC-Challenge\": {\"rho\": -0.2, \"exact_p\": 0.7833, \"direction\": \"WEAKER\"}, \"MMLU\": {\"rho\": 0.6, \"exact_p\": 0.35, \"direction\": \"WEAKER\"}, \"note\": \"ARC-Easy rho improves from -0.7 to -0.9 (p=0.0833) without GDN confound — suggestive second anchor\"}}, \"completed_at\": \"2026-05-19T14:18:07.535Z\"}, \"exp-003-p2v2\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-19T14:13:12.772Z\", \"updated_at\": \"2026-05-19T14:20:24.378Z\", \"hypothesis\": \"Helped samples have higher pure-model perplexity (model uncertain → attention helped) while hurt samples have lower perplexity (model confident → attention interfered), with architecture-specific patterns across GDN/RetNet/HGRN2. Retry with HGRN2 monkey-patch fix for _tied_weights_keys AttributeError.\", \"parent\": \"exp-003-p2\", \"conclusion\": \"killed\"}, \"exp-003-p2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T13:52:59.192Z\", \"updated_at\": \"2026-05-19T14:06:41.114Z\", \"hypothesis\": \"Helped samples have higher pure-model perplexity (model was uncertain → attention helped), while hurt samples have lower pure-model perplexity (model was confident → attention interfered). This pattern is architecture-specific.\", \"parent\": \"exp-003\", \"spec\": {\"command\": \"python3 /root/entrainment_gated_ft/analysis/sample_perplexity_analysis.py\", \"server\": \"westb-48145\", \"data_path\": \"/root/entrainment_gated_ft/lm_eval_clean\", \"data_count\": 5153, \"model_name\": \"GDN-pure, RetNet-pure, HGRN2-pure (1.3B)\", \"seed\": \"N/A\", \"checkpoint_source\": \"/root/autodl-tmp/models_1.3b/{GDN,RetNet,HGRN2}-pure\", \"eval_data\": \"LAMBADA OpenAI (5153 samples)\"}, \"conclusion\": \"negative\", \"log_path\": \"/root/entrainment_gated_ft/analysis/sample_perplexity_summary.json\", \"checkpoint_path\": \"/root/entrainment_gated_ft/analysis/sample_perplexity_results.csv\", \"completed_at\": \"2026-05-19T14:06:38.461Z\", \"metrics\": {\"GDN\": {\"U\": 148410, \"p\": 0.209189, \"r_rb\": -0.0447, \"helped_mean\": 3.3695, \"hurt_mean\": 3.3382}, \"RetNet\": {\"U\": 107210, \"p\": 0.659319, \"r_rb\": -0.0168, \"helped_mean\": 3.4432, \"hurt_mean\": 3.4207}, \"HGRN2\": {\"U\": 112999, \"p\": 0.247856, \"r_rb\": -0.0441, \"helped_mean\": 3.3775, \"hurt_mean\": 3.3538}, \"cross_arch_helped_KW_p\": 0.020136, \"cross_arch_hurt_KW_p\": 0.000498}}, \"exp-003\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T13:38:18.995Z\", \"updated_at\": \"2026-05-19T13:38:51.683Z\", \"hypothesis\": \"Architecture-specific helped/hurt samples on LAMBADA differ in surface features (token frequency, context length, lexical complexity), AND these feature profiles differ across GDN/HGRN2/RetNet — indicating architecture-specific mechanisms rather than generic attention benefit\", \"spec\": {\"command\": \"python analysis/sample_characterization.py — surface feature analysis of helped/hurt samples\", \"server\": \"westb-48145\", \"data_path\": \"/root/entrainment_gated_ft/lm_eval_clean/ (per-example logprob data)\", \"data_count\": 5153, \"model_name\": \"GDN/HGRN2/RetNet 1.3B h3-1 vs pure\", \"seed\": 0}, \"checkpoint_path\": \"/root/entrainment_gated_ft/analysis/sample_characterization_results.csv\", \"log_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/logs/workers/worker_analysis_exp_003_sample_characterization_20260519T131141.log\", \"conclusion\": \"negative\", \"metrics\": {\"GDN\": {\"helped\": 462, \"hurt\": 615, \"net\": -153, \"surface_features_significant\": false}, \"HGRN2\": {\"helped\": 548, \"hurt\": 395, \"net\": 153, \"surface_features_significant\": false}, \"RetNet\": {\"helped\": 426, \"hurt\": 495, \"net\": -69, \"context_length_p\": 0.012, \"context_length_r\": -0.096, \"unique_tokens_p\": 0.009, \"unique_tokens_r\": -0.099}, \"cross_arch_difference\": \"not_significant\", \"pass_fail\": \"FAIL — RetNet context_unique_tokens p=0.009 passes criterion 1 for one arch only; criterion 2 (cross-arch difference) fails\", \"summary\": \"Surface features do not explain helped/hurt identity. Rules out trivial explanations (frequency, length, diversity). RetNet shows weak context-length signal (p=0.012, r=-0.096).\"}, \"completed_at\": \"2026-05-19T13:38:51.683Z\"}, \"exp-009\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T13:32:43.818Z\", \"updated_at\": \"2026-05-19T13:33:45.506Z\", \"hypothesis\": \"Our equalizer effect analysis provides fully novel contributions relative to Wang et al. (arXiv 2507.06457) across 4 dimensions: convergence quantification (Spearman ρ + permutation test vs qualitative observation), scale dependency (quantitative 1.3B vs 340M contrast vs binary statement), per-example mechanism (Jaccard + net effect analysis vs absent), and task-specificity (convergence-strength by task type vs ratio-sensitivity)\", \"spec\": {\"command\": \"literature analysis: extract Wang et al. (2507.06457) exact claims, compare 4 differentiation dimensions\", \"server\": \"local + westb-48145\", \"data_path\": \"Wang et al. arXiv 2507.06457 + task_specificity_results.csv\", \"data_count\": 1, \"model_name\": \"N/A (literature analysis)\", \"seed\": 0}, \"checkpoint_path\": \"/root/entrainment_gated_ft/analysis/wang_et_al_differentiation.md\", \"log_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/logs/workers/worker_research_exp_009_wang_differentiation_20260519T131120.log\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-19T13:33:45.506Z\"}, \"eval_340m_retnet_hgrn2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T04:03:58.762Z\", \"updated_at\": \"2026-05-19T04:32:37.289Z\", \"hypothesis\": \"340M RetNet and HGRN2 models will show the same architecture-dependent attention effect observed at 1.3B scale: HGRN2 benefits from attention while RetNet shows minimal benefit, with task-dependent equalizer effect on LAMBADA\", \"spec\": {\"command\": \"bash /root/entrainment_gated_ft/run_all_340m_eval.sh\", \"server\": \"westb-48145\", \"data_path\": \"/root/autodl-tmp/models/\", \"data_count\": 10, \"model_name\": \"340M RetNet×5 + HGRN2×5\", \"seed\": 0}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/entrainment_gated_ft/lm_eval_clean/340m/\", \"log_path\": \"/root/entrainment_gated_ft/lm_eval_clean/340m/run_all.log\", \"completed_at\": \"2026-05-19T04:32:37.289Z\"}, \"hgrn2_eval_h3_1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T16:47:57.853Z\", \"updated_at\": \"2026-05-18T16:53:12.858Z\", \"spec\": {\"command\": \"HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1 python run_lmeval_clean.py --model_path 1.3B-100B-HGRN2-hybrid-3-1 --tasks 6tasks --batch_size 8\", \"server\": \"westb-48145\", \"data_path\": \"/root/autodl-tmp/models_1.3b/1.3B-100B-HGRN2-hybrid-3-1\", \"data_count\": 1, \"model_name\": \"HGRN2-1.3B-hybrid-3-1\", \"seed\": 0}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/entrainment_gated_ft/lm_eval_clean/1.3B-100B-HGRN2-hybrid-3-1.json\", \"log_path\": \"/tmp/hgrn2_eval_h3_1.log\", \"hypothesis\": \"HGRN2 hybrid-3-1 (highest attention ratio) will show less degradation on composition-heavy benchmarks compared to pure linear models, following the attention-ratio degradation pattern observed in GDN and RetNet families\", \"completed_at\": \"2026-05-18T16:53:12.858Z\"}, \"hgrn2_eval_1_3b_all\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T15:57:15.535Z\", \"updated_at\": \"2026-05-18T16:00:12.920Z\", \"spec\": {\"command\": \"python run_lmeval_clean.py --model_path {MODEL} --tasks lambada_openai,hellaswag,winogrande,arc_easy,arc_challenge,mmlu --output_dir lm_eval_clean/ --batch_size 8 (x3 models: hybrid-12-1, hybrid-24-1, hybrid-3-1)\", \"server\": \"westb-48145\", \"data_path\": \"/root/autodl-tmp/models_1.3b/\", \"data_count\": 3, \"model_name\": \"HGRN2-1.3B (3 hybrid variants)\", \"seed\": 0}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-18T16:00:12.920Z\"}}, \"count\": 40, \"total\": 40, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.0959}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e0a2fe02-939a-4ef2-b3bd-fc442aa65c19",
  "isSidechain": false,
  "promptId": "53afff33-bebc-42c8-b6ca-8baf6ae2df0c",
  "type": "user",
  "uuid": "ec69d089-ac7d-4469-8ff1-e8ecb0f61fd0",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-2-projects-entrainment-gated-ft--claude-sessions-agent-aa1a2296/ccd4bb6d-9c70-4ece-9e7e-8b842791a0aa/tool-results/toolu_017SjjVew7bhkJio3KNz9LNC.txt",
      "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {\\\"exp-005-gla-pure\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-22T16:33:56.971Z\\\", \\\"updated_at\\\": \\\"2026-05-22T16:41:30.660Z\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"source /etc/network_turbo && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_HUB_DISABLE_XET=1 && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && python /root/entrainment_gated_ft/scripts/patch_fla_eval.py --model hf --model_args pretrained=/root/entrainment_gated_ft/models/340M-20B-GLA-pure-baseline,trust_remote_code=True --tasks lambada_openai,arc_easy --device cuda:0 --batch_size auto --log_samples --output_path /root/entrainment_gated_ft/results/exp005_zoo_expansion/GLA_pure/ && echo GLA_PURE_EVAL_DONE\\\\\\\"\\\", \\\"server\\\": \\\"westb-48145\\\", \\\"gpu\\\": [\\\"cuda:0\\\"], \\\"pid\\\": \\\"904591\\\", \\\"log_path\\\": \\\"~/runs/entrainment_gated_ft/exp-005-gla-pure.log\\\", \\\"submitted_at\\\": \\\"2026-05-22T16:39:54.061Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\"}, \\\"reproduce\\\": {\\\"finished_at\\\": \\\"2026-05-22T16:41:30.660Z\\\"}, \\\"extra\\\": {\\\"hook_events\\\": [{\\\"event\\\": \\\"on_complete\\\", \\\"action\\\": \\\"agent\\\", \\\"ts\\\": \\\"2026-05-22T16:41:32.936910+00:00\\\"}]}}, \\\"exp-005-pure-v5\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-22T16:37:28.872Z\\\", \\\"updated_at\\\": \\\"2026-05-22T16:37:28.872Z\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"bash /root/entrainment_gated_ft/results/exp005_zoo_expansion/run_pure_v5.sh\\\\\\\"\\\", \\\"server\\\": \\\"westb-48145\\\", \\\"gpu\\\": [\\\"cuda:0\\\"], \\\"pid\\\": \\\"904122\\\", \\\"log_path\\\": \\\"~/runs/entrainment_gated_ft/exp-005-pure-v5.log\\\", \\\"submitted_at\\\": \\\"2026-05-22T16:37:28.788Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\"}}, \\\"exp-005-pure-v4\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-22T16:35:11.429Z\\\", \\\"updated_at\\\": \\\"2026-05-22T16:35:11.429Z\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"bash /root/entrainment_gated_ft/results/exp005_zoo_expansion/run_pure_v4.sh\\\\\\\"\\\", \\\"server\\\": \\\"westb-48145\\\", \\\"gpu\\\": [\\\"cuda:0\\\"], \\\"pid\\\": \\\"903338\\\", \\\"log_path\\\": \\\"~/runs/entrainment_gated_ft/exp-005-pure-v4.log\\\", \\\"submitted_at\\\": \\\"2026-05-22T16:35:11.341Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\"}}, \\\"exp-005-pure-v3\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-22T16:32:39.150Z\\\", \\\"updated_at\\\": \\\"2026-05-22T16:32:39.150Z\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"bash /root/entrainment_gated_ft/results/exp005_zoo_expansion/run_pure_v3.sh\\\\\\\"\\\", \\\"server\\\": \\\"westb-48145\\\", \\\"gpu\\\": [\\\"cuda:0\\\"], \\\"pid\\\": \\\"902795\\\", \\\"log_path\\\": \\\"~/runs/entrainment_gated_ft/exp-005-pure-v3.log\\\", \\\"submitted_at\\\": \\\"2026-05-22T16:32:39.070Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\"}}, \\\"exp-005-batch\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-22T16:30:41.446Z\\\", \\\"updated_at\\\": \\\"2026-05-22T16:31:53.107Z\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"bash /root/entrainment_gated_ft/results/exp005_zoo_expansion/run_eval_download.sh\\\\\\\"\\\", \\\"server\\\": \\\"westb-48145\\\", \\\"gpu\\\": [\\\"cuda:0\\\"], \\\"pid\\\": \\\"902349\\\", \\\"log_path\\\": \\\"~/runs/entrainment_gated_ft/exp-005-batch.log\\\", \\\"submitted_at\\\": \\\"2026-05-22T16:30:41.362Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\"}, \\\"reproduce\\\": {\\\"finished_at\\\": \\\"2026-05-22T16:31:50.753Z\\\"}, \\\"failure_reason\\\": \\\"EXIT_CODE=1 (generic error — check log tail)\\\", \\\"conclusion\\\": \\\"failed\\\", \\\"extra\\\": {\\\"hook_events\\\": [{\\\"event\\\": \\\"on_failed\\\", \\\"action\\\": \\\"agent\\\", \\\"ts\\\": \\\"2026-05-22T16:31:55.361162+00:00\\\"}]}}, \\\"exp-005-hgrn-chain\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-22T16:27:47.360Z\\\", \\\"updated_at\\\": \\\"2026-05-22T16:27:47.360Z\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"bash /root/entrainment_gated_ft/results/exp005_zoo_expansion/run_hgrn_chain.sh\\\\\\\"\\\", \\\"server\\\": \\\"westb-48145\\\", \\\"gpu\\\": [\\\"cuda:0\\\"], \\\"pid\\\": \\\"902087\\\", \\\"log_path\\\": \\\"~/runs/entrainment_gated_ft/exp-005-hgrn-chain.log\\\", \\\"submitted_at\\\": \\\"2026-05-22T16:27:47.270Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\"}}, \\\"exp-005\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"retry_count\\\": 1, \\\"created_at\\\": \\\"2026-05-20T02:26:40.718Z\\\", \\\"updated_at\\\": \\\"2026-05-22T16:18:38.064Z\\\", \\\"hypothesis\\\": \\\"Cross-architecture Jaccard overlap of helped/hurt sets will remain significantly above chance when expanded from 3 to 6 linear attention architectures, indicating that attention-mediated sample sensitivity is architecture-independent.\\\", \\\"parent\\\": \\\"exp-001\\\", \\\"completed_at\\\": \\\"2026-05-22T14:24:29.103Z\\\", \\\"extra\\\": {\\\"previous_failure\\\": {\\\"conclusion\\\": \\\"killed\\\", \\\"metrics\\\": {\\\"cancel_reason\\\": \\\"Wang et al. zoo 仅含 GDN/RetNet/HGRN2，无法扩展 n>3，已由 worker_analysis_arch-extension-check 确认\\\"}}, \\\"hook_events\\\": [{\\\"event\\\": \\\"on_failed\\\", \\\"action\\\": \\\"agent\\\", \\\"ts\\\": \\\"2026-05-22T15:05:27.711311+00:00\\\"}]}, \\\"metrics\\\": {\\\"gla_h31_lambada_acc\\\": 0.3819, \\\"gla_h31_arc_acc\\\": 0.5673, \\\"deltanet_h31_lambada_acc\\\": 0.3536, \\\"deltanet_h31_lambada_ppl\\\": 30.45, \\\"deltanet_h31_arc_acc\\\": 0.601, \\\"fla_patch_needed\\\": \\\"scripts/patch_fla_eval.py fixes _tied_weights_keys list→dict for fla 0.5.0 + transformers 5.8.1\\\"}, \\\"reproduce\\\": {\\\"finished_at\\\": \\\"2026-05-22T15:05:23.157Z\\\"}, \\\"failure_reason\\\": \\\"EXIT_CODE=1 (generic error — check log tail)\\\", \\\"conclusion\\\": \\\"failed\\\", \\\"notes\\\": \\\"诊断中: worker_diagnose_exp-005-p1-v4_20260522T150706 正在查日志。日志仅7行，进程在下载 DeltaNet h3-1 模型时 EXIT_CODE=1 退出。\\\"}, \\\"exp-005-p1-eval-v5\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-22T16:18:29.815Z\\\", \\\"updated_at\\\": \\\"2026-05-22T16:18:29.815Z\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"bash /root/entrainment_gated_ft/results/exp005_zoo_expansion/run_eval_p1.sh\\\\\\\"\\\", \\\"server\\\": \\\"westb-48145\\\", \\\"gpu\\\": [\\\"cuda:0\\\"], \\\"pid\\\": \\\"898757\\\", \\\"log_path\\\": \\\"~/runs/entrainment_gated_ft/exp-005-p1-eval-v5.log\\\", \\\"submitted_at\\\": \\\"2026-05-22T16:18:29.731Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\"}}, \\\"exp-005-p1-eval-v4\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-22T16:16:34.914Z\\\", \\\"updated_at\\\": \\\"2026-05-22T16:16:34.914Z\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"bash /root/entrainment_gated_ft/results/exp005_zoo_expansion/run_eval_p1.sh\\\\\\\"\\\", \\\"server\\\": \\\"westb-48145\\\", \\\"gpu\\\": [\\\"cuda:0\\\"], \\\"pid\\\": \\\"897689\\\", \\\"log_path\\\": \\\"~/runs/entrainment_gated_ft/exp-005-p1-eval-v4.log\\\", \\\"submitted_at\\\": \\\"2026-05-22T16:16:34.836Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\"}}, \\\"exp-005-dn-eval\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-22T15:56:19.907Z\\\", \\\"updated_at\\\": \\\"2026-05-22T16:10:46.245Z\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"source /etc/network_turbo && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_HUB_DISABLE_XET=1 && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && cd /root/entrainment_gated_ft && python scripts/patch_fla_eval.py --model hf --model_args pretrained=/root/entrainment_gated_ft/models/340M-20B-DeltaNet-hybrid-3-1,trust_remote_code=True,dtype=float16 --tasks lambada_openai,arc_easy --device cuda:0 --batch_size auto --log_samples --output_path /root/entrainment_gated_ft/results/exp005_zoo_expansion/DeltaNet_hybrid-3-1/ && echo DELTANET_EVAL_DONE\\\\\\\"\\\", \\\"server\\\": \\\"westb-48145\\\", \\\"gpu\\\": [\\\"cuda:0\\\"], \\\"pid\\\": \\\"886300\\\", \\\"log_path\\\": \\\"~/runs/entrainment_gated_ft/exp-005-dn-eval.log\\\", \\\"submitted_at\\\": \\\"2026-05-22T16:04:02.638Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\"}, \\\"metrics\\\": {\\\"model\\\": \\\"340M-20B-DeltaNet-hybrid-3-1\\\", \\\"lambada_openai_acc\\\": 0.3536, \\\"lambada_openai_ppl\\\": 30.45, \\\"arc_easy_acc\\\": 0.601, \\\"arc_easy_acc_norm\\\": 0.5198, \\\"status\\\": \\\"DONE\\\"}}, \\\"exp-005-p1-eval-v3\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-22T16:07:46.157Z\\\", \\\"updated_at\\\": \\\"2026-05-22T16:07:46.157Z\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"bash /root/entrainment_gated_ft/results/exp005_zoo_expansion/run_eval_p1.sh\\\\\\\"\\\", \\\"server\\\": \\\"westb-48145\\\", \\\"gpu\\\": [\\\"cuda:0\\\"], \\\"pid\\\": \\\"891633\\\", \\\"log_path\\\": \\\"~/runs/entrainment_gated_ft/exp-005-p1-eval-v3.log\\\", \\\"submitted_at\\\": \\\"2026-05-22T16:07:46.079Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\"}}, \\\"exp-005-p1-eval-v2\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-22T16:06:40.443Z\\\", \\\"updated_at\\\": \\\"2026-05-22T16:06:40.443Z\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"bash /root/entrainment_gated_ft/results/exp005_zoo_expansion/run_eval_p1.sh\\\\\\\"\\\", \\\"server\\\": \\\"westb-48145\\\", \\\"gpu\\\": [\\\"cuda:0\\\"], \\\"pid\\\": \\\"889541\\\", \\\"log_path\\\": \\\"~/runs/entrainment_gated_ft/exp-005-p1-eval-v2.log\\\", \\\"submitted_at\\\": \\\"2026-05-22T16:06:40.369Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\"}}, \\\"exp-005-p1-eval\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-22T16:01:38.958Z\\\", \\\"updated_at\\\": \\\"2026-05-22T16:01:38.958Z\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"bash /root/entrainment_gated_ft/results/exp005_zoo_expansion/run_eval_p1.sh\\\\\\\"\\\", \\\"server\\\": \\\"westb-48145\\\", \\\"gpu\\\": [\\\"cuda:0\\\"], \\\"pid\\\": \\\"884365\\\", \\\"log_path\\\": \\\"~/runs/entrainment_gated_ft/exp-005-p1-eval.log\\\", \\\"submitted_at\\\": \\\"2026-05-22T16:01:38.883Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\"}}, \\\"exp-005-pure-eval\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-22T15:58:12.656Z\\\", \\\"updated_at\\\": \\\"2026-05-22T16:01:21.317Z\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"bash /root/entrainment_gated_ft/results/exp005_zoo_expansion/run_wget_eval_pure.sh\\\\\\\"\\\", \\\"server\\\": \\\"westb-48145\\\", \\\"gpu\\\": [\\\"cuda:0\\\"], \\\"pid\\\": \\\"884046\\\", \\\"log_path\\\": \\\"~/runs/entrainment_gated_ft/exp-005-pure-eval.log\\\", \\\"submitted_at\\\": \\\"2026-05-22T16:01:21.241Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\"}}, \\\"exp-005-deltanet\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-22T15:51:45.169Z\\\", \\\"updated_at\\\": \\\"2026-05-22T15:51:45.169Z\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"bash /root/entrainment_gated_ft/results/exp005_zoo_expansion/eval_deltanet_hardcode.sh\\\\\\\"\\\", \\\"server\\\": \\\"westb-48145\\\", \\\"gpu\\\": [\\\"cuda:0\\\"], \\\"pid\\\": \\\"881335\\\", \\\"log_path\\\": \\\"~/runs/entrainment_gated_ft/exp-005-deltanet.log\\\", \\\"submitted_at\\\": \\\"2026-05-22T15:51:45.096Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\"}}, \\\"exp-005-gla\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-22T15:41:49.615Z\\\", \\\"updated_at\\\": \\\"2026-05-22T15:48:24.790Z\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"bash /root/entrainment_gated_ft/results/exp005_zoo_expansion/eval_gla_hardcode.sh\\\\\\\"\\\", \\\"server\\\": \\\"westb-48145\\\", \\\"gpu\\\": [\\\"cuda:0\\\"], \\\"pid\\\": \\\"878457\\\", \\\"log_path\\\": \\\"~/runs/entrainment_gated_ft/exp-005-gla.log\\\", \\\"submitted_at\\\": \\\"2026-05-22T15:48:24.719Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\"}}, \\\"exp-005-gla-eval\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-22T15:38:30.968Z\\\", \\\"updated_at\\\": \\\"2026-05-22T15:44:36.037Z\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"source /etc/network_turbo && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_HUB_DISABLE_XET=1 && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && python -c 'import fla; print(fla.__version__)' && python -m lm_eval --model hf --model_args pretrained=/root/entrainment_gated_ft/models/340M-20B-GLA-hybrid-3-1,trust_remote_code=True --tasks lambada_openai,arc_easy --device cuda:0 --batch_size auto --log_samples --output_path /root/entrainment_gated_ft/results/exp005_zoo_expansion/GLA_hybrid-3-1/ && echo GLA_EVAL_DONE\\\\\\\"\\\", \\\"server\\\": \\\"westb-48145\\\", \\\"gpu\\\": [\\\"cuda:0\\\"], \\\"pid\\\": \\\"875395\\\", \\\"log_path\\\": \\\"~/runs/entrainment_gated_ft/exp-005-gla-eval.log\\\", \\\"submitted_at\\\": \\\"2026-05-22T15:42:46.005Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\"}, \\\"reproduce\\\": {\\\"finished_at\\\": \\\"2026-05-22T15:43:08.734Z\\\"}, \\\"extra\\\": {\\\"hook_events\\\": [{\\\"event\\\": \\\"on_complete\\\", \\\"action\\\": \\\"agent\\\", \\\"ts\\\": \\\"2026-05-22T15:39:05.469998+00:00\\\"}, {\\\"event\\\": \\\"on_failed\\\", \\\"action\\\": \\\"agent\\\", \\\"ts\\\": \\\"2026-05-22T15:43:12.720582+00:00\\\"}]}, \\\"failure_reason\\\": \\\"Traceback → ss = CONFIG_MAPPING[config_dict[\\\\\\\"model_type\\\\\\\"]] ~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^ File \\\\\\\"/root/miniconda3/lib/python3.12/site-packages/transformers/models/auto/configuration_auto.py\\\\\\\", line 105, in __getitem__ raise KeyError(key) KeyError: 'gla'\\\", \\\"conclusion\\\": \\\"failed\\\", \\\"notes\\\": \\\"失败原因已诊断：1) 首次提交 pretrained='' 空字符串（shell 变量展开问题）；2) 重试时 KeyError: 'gla'（transformers AutoModel 不识别 GLA 模型类型，需要 fla 包注册）。模型文件本身完整（340M-20B-GLA-hybrid-3-1/model.safetensors 存在）。worker_fix_exp-005-gla-eval-hardcode 正在创建 wrapper 脚本修复。\\\"}, \\\"exp-005-p1-v4\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-22T14:49:36.217Z\\\", \\\"updated_at\\\": \\\"2026-05-22T14:49:36.217Z\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"bash /root/entrainment_gated_ft/results/exp005_zoo_expansion/run_p1_v4.sh\\\\\\\"\\\", \\\"server\\\": \\\"westb-48145\\\", \\\"gpu\\\": [\\\"cuda:0\\\"], \\\"pid\\\": \\\"870648\\\", \\\"log_path\\\": \\\"~/runs/entrainment_gated_ft/exp-005-p1-v4.log\\\", \\\"submitted_at\\\": \\\"2026-05-22T14:49:36.151Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\"}}, \\\"exp-005-eval\\\": {\\\"status\\\": \\\"PENDING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-22T14:22:49.860Z\\\", \\\"updated_at\\\": \\\"2026-05-22T14:25:11.027Z\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash -c '\\\\nset -eo pipefail\\\\nsource /etc/network_turbo\\\\nsource /root/miniconda3/etc/profile.d/conda.sh && conda activate base\\\\nexport HF_HOME=/root/autodl-tmp/.hf_cache\\\\nexport HF_HUB_DISABLE_XET=1\\\\nexport REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt\\\\nexport SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt\\\\n\\\\nMODELS_DIR=\\\\\\\"/root/entrainment_gated_ft/models\\\\\\\"\\\\nRESULTS_DIR=\\\\\\\"/root/entrainment_gated_ft/results/exp005_zoo_expansion\\\\\\\"\\\\nLOG=\\\\\\\"$RESULTS_DIR/run_all.log\\\\\\\"\\\\nmkdir -p \\\\\\\"$RESULTS_DIR\\\\\\\"\\\\n\\\\necho \\\\\\\"=== EXP-005 FULL RUN $(date) ===\\\\\\\" | tee \\\\\\\"$LOG\\\\\\\"\\\\n\\\\n# Phase 1: Download missing Priority 1 models (GLA already done)\\\\nfor arch in DeltaNet HGRN; do\\\\n  MODEL_NAME=\\\\\\\"340M-20B-${arch}-hybrid-3-1\\\\\\\"\\\\n  MODEL_DIR=\\\\\\\"$MODELS_DIR/$MODEL_NAME\\\\\\\"\\\\n  if [ ! -f \\\\\\\"$MODEL_DIR/model.safetensors\\\\\\\" ]; then\\\\n    echo \\\\\\\"Downloading $MODEL_NAME ...\\\\\\\" | tee -a \\\\\\\"$LOG\\\\\\\"\\\\n    rm -rf \\\\\\\"$MODEL_DIR\\\\\\\"\\\\n    huggingface-cli download \\\\\\\"m-a-p/$MODEL_NAME\\\\\\\" --local-dir \\\\\\\"$MODEL_DIR\\\\\\\" 2>&1 | tail -5 | tee -a \\\\\\\"$LOG\\\\\\\"\\\\n    echo \\\\\\\"Downloaded $MODEL_NAME $(date)\\\\\\\" | tee -a \\\\\\\"$LOG\\\\\\\"\\\\n  else\\\\n    echo \\\\\\\"Already have $MODEL_NAME\\\\\\\" | tee -a \\\\\\\"$LOG\\\\\\\"\\\\n  fi\\\\ndone\\\\n\\\\n# Phase 2: Evaluate Priority 1 (h3-1 x 3 new archs)\\\\nfor arch in GLA DeltaNet HGRN; do\\\\n  MODEL_NAME=\\\\\\\"340M-20B-${arch}-hybrid-3-1\\\\\\\"\\\\n  MODEL_DIR=\\\\\\\"$MODELS_DIR/$MODEL_NAME\\\\\\\"\\\\n  OUT_DIR=\\\\\\\"$RESULTS_DIR/${arch}_hybrid-3-1\\\\\\\"\\\\n  echo \\\\\\\"EVAL $MODEL_NAME START $(date)\\\\\\\" | tee -a \\\\\\\"$LOG\\\\\\\"\\\\n  python -m lm_eval \\\\\\\\\\\\n    --model hf \\\\\\\\\\\\n    --model_args pretrained=$MODEL_DIR,trust_remote_code=True \\\\\\\\\\\\n    --tasks lambada_openai,arc_easy \\\\\\\\\\\\n    --device cuda:0 \\\\\\\\\\\\n    --batch_size auto \\\\\\\\\\\\n    --log_samples \\\\\\\\\\\\n    --output_path \\\\\\\"$OUT_DIR/\\\\\\\" 2>&1 | tail -10 | tee -a \\\\\\\"$LOG\\\\\\\"\\\\n  echo \\\\\\\"EVAL $MODEL_NAME DONE $(date)\\\\\\\" | tee -a \\\\\\\"$LOG\\\\\\\"\\\\ndone\\\\n\\\\necho \\\\\\\"=== PRIORITY 1 COMPLETE $(date) ===\\\\\\\" | tee -a \\\\\\\"$LOG\\\\\\\"\\\\n\\\\n# Phase 3: Download + evaluate remaining ratios\\\\nfor arch in GLA DeltaNet HGRN; do\\\\n  for ratio in pure-baseline hybrid-24-1 hybrid-12-1 hybrid-6-1; do\\\\n    MODEL_NAME=\\\\\\\"340M-20B-${arch}-${ratio}\\\\\\\"\\\\n    MODEL_DIR=\\\\\\\"$MODELS_DIR/$MODEL_NAME\\\\\\\"\\\\n    OUT_DIR=\\\\\\\"$RESULTS_DIR/${arch}_${ratio}\\\\\\\"\\\\n\\\\n    if [ ! -f \\\\\\\"$MODEL_DIR/model.safetensors\\\\\\\" ]; then\\\\n      echo \\\\\\\"Downloading $MODEL_NAME ...\\\\\\\" | tee -a \\\\\\\"$LOG\\\\\\\"\\\\n      rm -rf \\\\\\\"$MODEL_DIR\\\\\\\"\\\\n      huggingface-cli download \\\\\\\"m-a-p/$MODEL_NAME\\\\\\\" --local-dir \\\\\\\"$MODEL_DIR\\\\\\\" 2>&1 | tail -3 | tee -a \\\\\\\"$LOG\\\\\\\"\\\\n      if [ ! -f \\\\\\\"$MODEL_DIR/model.safetensors\\\\\\\" ]; then\\\\n        ALT_NAME=\\\\\\\"340M-20B-${arch}-pure\\\\\\\"\\\\n        if [ \\\\\\\"$ratio\\\\\\\" = \\\\\\\"pure-baseline\\\\\\\" ]; then\\\\n          echo \\\\\\\"Trying alternate: $ALT_NAME ...\\\\\\\" | tee -a \\\\\\\"$LOG\\\\\\\"\\\\n          huggingface-cli download \\\\\\\"m-a-p/$ALT_NAME\\\\\\\" --local-dir \\\\\\\"$MODELS_DIR/$ALT_NAME\\\\\\\" 2>&1 | tail -3 | tee -a \\\\\\\"$LOG\\\\\\\"\\\\n          MODEL_DIR=\\\\\\\"$MODELS_DIR/$ALT_NAME\\\\\\\"\\\\n        fi\\\\n      fi\\\\n      echo \\\\\\\"Downloaded $(date)\\\\\\\" | tee -a \\\\\\\"$LOG\\\\\\\"\\\\n    fi\\\\n\\\\n    echo \\\\\\\"EVAL $MODEL_NAME START $(date)\\\\\\\" | tee -a \\\\\\\"$LOG\\\\\\\"\\\\n    python -m lm_eval \\\\\\\\\\\\n      --model hf \\\\\\\\\\\\n      --model_args pretrained=$MODEL_DIR,trust_remote_code=True \\\\\\\\\\\\n      --tasks lambada_openai,arc_easy \\\\\\\\\\\\n      --device cuda:0 \\\\\\\\\\\\n      --batch_size auto \\\\\\\\\\\\n      --log_samples \\\\\\\\\\\\n      --output_path \\\\\\\"$OUT_DIR/\\\\\\\" 2>&1 | tail -10 | tee -a \\\\\\\"$LOG\\\\\\\"\\\\n    echo \\\\\\\"EVAL $MODEL_NAME DONE $(date)\\\\\\\" | tee -a \\\\\\\"$LOG\\\\\\\"\\\\n  done\\\\ndone\\\\n\\\\necho \\\\\\\"=== ALL EVALUATIONS COMPLETE $(date) ===\\\\\\\" | tee -a \\\\\\\"$LOG\\\\\\\"\\\\n'\\\", \\\"server\\\": \\\"westb-48145\\\", \\\"gpu\\\": [\\\"cuda:0\\\"], \\\"pid\\\": \\\"unknown\\\", \\\"log_path\\\": \\\"~/runs/entrainment_gated_ft/exp-005-eval.log\\\", \\\"submitted_at\\\": \\\"2026-05-22T14:22:49.797Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\"}, \\\"reproduce\\\": {\\\"finished_at\\\": \\\"2026-05-22T14:23:13.448Z\\\"}, \\\"failure_reason\\\": \\\"EXIT_CODE=1 (generic error — check log tail)\\\", \\\"conclusion\\\": \\\"killed\\\", \\\"extra\\\": {\\\"hook_events\\\": [{\\\"event\\\": \\\"on_failed\\\", \\\"action\\\": \\\"agent\\\", \\\"ts\\\": \\\"2026-05-22T14:23:17.070767+00:00\\\"}]}, \\\"hypothesis\\\": \\\"Cross-architecture per-example Jaccard (helped/hurt) remains ≤0.10 when expanding from 3 architectures (GDN/RetNet/HGRN2) to 6 (adding GLA/DeltaNet/HGRN), with 15 pairwise comparisons and 720 permutations providing dramatically stronger statistical power.\\\"}, \\\"e4-pythia-seed-calibration\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-22T10:17:05.445Z\\\", \\\"updated_at\\\": \\\"2026-05-22T11:44:42.532Z\\\", \\\"hypothesis\\\": \\\"Pythia 70M 9-seed variants 的 within-seed per-example Jaccard (same architecture, different random seed) 显著高于 cross-architecture Jaccard (~0.10), 证明 within-arch overlap >> cross-arch overlap, 即 cross-arch 信号不能被 seed noise 解释。\\\", \\\"parent\\\": \\\"exp-001\\\", \\\"spec\\\": {\\\"command\\\": \\\"lm_eval --model hf --tasks lambada_openai,arc_easy --log_samples\\\", \\\"server\\\": \\\"westb-48145\\\", \\\"model_name\\\": \\\"EleutherAI/pythia-70m-seed{1-9}\\\", \\\"seed\\\": \\\"1-9\\\", \\\"data_path\\\": \\\"/root/entrainment_gated_ft/results/e4_pythia_seed/\\\", \\\"data_count\\\": \\\"5153+2376 per seed × 9 seeds\\\", \\\"checkpoint_source\\\": \\\"ModelScope CDN\\\", \\\"eval_data\\\": \\\"lambada_openai + arc_easy\\\", \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/pythia_weights_70m/seed{1-9}/\\\", \\\"log_path\\\": \\\"/root/entrainment_gated_ft/results/e4_pythia_seed/eval.log\\\"}, \\\"reproduce\\\": {\\\"finished_at\\\": \\\"2026-05-22T11:10:00.780Z\\\"}, \\\"failure_reason\\\": \\\"process dead 5× with no sentinel/W&B — auto-resolved as failed\\\", \\\"conclusion\\\": \\\"success\\\", \\\"completed_at\\\": \\\"2026-05-22T11:10:01.238Z\\\", \\\"extra\\\": {\\\"hook_events\\\": [{\\\"event\\\": \\\"on_failed\\\", \\\"action\\\": \\\"agent\\\", \\\"ts\\\": \\\"2026-05-22T11:10:03.664374+00:00\\\"}]}, \\\"metrics\\\": {\\\"lambada_J_helped\\\": 0.273, \\\"lambada_J_hurt\\\": 0.393, \\\"lambada_alpha\\\": 0.355, \\\"arc_J_helped\\\": 0.312, \\\"arc_alpha\\\": 0.491, \\\"cross_arch_ref_J_helped\\\": 0.1, \\\"ratio_lambada\\\": 2.73, \\\"ratio_arc\\\": 3.12}}, \\\"exp-340m-multi-bench\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-21T22:23:25.467Z\\\", \\\"updated_at\\\": \\\"2026-05-22T00:34:02.116Z\\\", \\\"hypothesis\\\": \\\"340M models exhibit α spectrum (per-example ambiguity) consistent with 1.3B across HellaSwag/PIQA/ARC-Easy — establishing scale-invariance of the multiplicity phenomenon beyond the single-benchmark (LAMBADA) evidence in §4.3. If α_340M ≈ α_1.3B per benchmark, cross-scale stability is confirmed; if systematically different, the scale-dependency claim needs qualification.\\\", \\\"parent\\\": \\\"exp-007\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash run_340m_multi_eval.sh (run_lmeval_clean.py × 15 models × 3 tasks with --log_samples)\\\", \\\"server\\\": \\\"westb-48145\\\", \\\"gpu\\\": [\\\"cuda:0\\\"], \\\"data_path\\\": \\\"/root/entrainment_gated_ft/models/ (15 × 340M models)\\\", \\\"data_count\\\": \\\"hellaswag=10042, piqa=1838, arc_easy=2376 per model\\\", \\\"model_name\\\": \\\"GDN/RetNet/HGRN2 × 5 ratios (340M, 15 models)\\\", \\\"seed\\\": \\\"default\\\", \\\"checkpoint_source\\\": \\\"/root/entrainment_gated_ft/models/340M-20B-*\\\", \\\"eval_data\\\": \\\"HellaSwag (10042) + PIQA (1838) + ARC-Easy (2376)\\\", \\\"pid\\\": \\\"777365\\\", \\\"log_path\\\": \\\"~/runs/entrainment_gated_ft/exp-340m-multi-bench.log\\\", \\\"submitted_at\\\": \\\"2026-05-21T22:27:20Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"checkpoint_path\\\": \\\"/root/entrainment_gated_ft/lm_eval_clean/340m_multi/\\\", \\\"wall_clock_seconds\\\": 7602.1, \\\"gpu_hours\\\": 2.11}, \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"hellaswag_acc_norm\\\": {\\\"340m_alpha_all\\\": 0.334, \\\"1_3b_alpha_all\\\": 0.302, \\\"delta\\\": 0.031, \\\"340m_alpha_pure\\\": 0.167, \\\"1_3b_alpha_pure\\\": 0.148, \\\"340m_J_helped\\\": 0.084, \\\"1_3b_J_helped\\\": 0.095, \\\"340m_J_hurt\\\": 0.083, \\\"1_3b_J_hurt\\\": 0.085, \\\"340m_convergence_rho\\\": 0.4, \\\"340m_convergence_p\\\": 0.517}, \\\"piqa\\\": {\\\"340m_alpha_all\\\": 0.366, \\\"1_3b_alpha_all\\\": 0.278, \\\"delta\\\": 0.089, \\\"340m_alpha_pure\\\": 0.181, \\\"1_3b_alpha_pure\\\": 0.143, \\\"340m_J_helped\\\": 0.09, \\\"1_3b_J_helped\\\": 0.091, \\\"340m_J_hurt\\\": 0.085, \\\"1_3b_J_hurt\\\": 0.094, \\\"340m_convergence_rho\\\": 0.3, \\\"340m_convergence_p\\\": 0.683}, \\\"arc_easy\\\": {\\\"340m_alpha_all\\\": 0.564, \\\"1_3b_alpha_all\\\": 0.434, \\\"delta\\\": 0.13, \\\"340m_alpha_pure\\\": 0.289, \\\"1_3b_alpha_pure\\\": 0.205, \\\"340m_J_helped\\\": 0.098, \\\"1_3b_J_helped\\\": 0.092, \\\"340m_J_hurt\\\": 0.103, \\\"1_3b_J_hurt\\\": 0.099, \\\"340m_convergence_rho\\\": -0.1, \\\"340m_convergence_p\\\": 0.95}, \\\"summary\\\": {\\\"mean_delta_alpha_all\\\": 0.084, \\\"scenario\\\": \\\"B_mixed\\\", \\\"pattern_invariant\\\": true, \\\"magnitude_scale_dependent\\\": true}, \\\"artifacts\\\": [\\\"340m_multi_bench_analysis.json\\\"]}, \\\"completed_at\\\": \\\"2026-05-22T00:34:02.116Z\\\"}, \\\"w3-winogrande-piqa-eval\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-21T08:28:29.577Z\\\", \\\"updated_at\\\": \\\"2026-05-21T10:27:33.995Z\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash run_winogrande_piqa_all.sh (run_lmeval_clean.py × 30 tasks)\\\", \\\"server\\\": \\\"westb-48145\\\", \\\"gpu\\\": [\\\"cuda:0\\\"], \\\"pid\\\": \\\"722233\\\", \\\"log_path\\\": \\\"/root/entrainment_gated_ft/lm_eval_clean/winogrande_piqa_eval.log\\\", \\\"submitted_at\\\": \\\"2026-05-21T08:28:29.524Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"data_path\\\": \\\"lm-eval-harness winogrande + piqa\\\", \\\"data_count\\\": \\\"winogrande=1267, piqa=1838\\\", \\\"model_name\\\": \\\"GDN/RetNet/HGRN2 × 5 ratios (1.3B)\\\", \\\"seed\\\": \\\"default\\\", \\\"checkpoint_path\\\": \\\"artifacts/paper_data/winogrande_per_example.json + piqa_per_example.json\\\", \\\"wall_clock_seconds\\\": 7144.5, \\\"gpu_hours\\\": 1.98}, \\\"hypothesis\\\": \\\"WinoGrande + PIQA per-example multiplicity analysis to decouple format (2-choice vs 4-way MC) from task-type as driver of ambiguity α spectrum, addressing Round 5 W3 format confound concern\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"winogrande\\\": {\\\"n_samples\\\": 1267, \\\"alpha_pure\\\": 0.463, \\\"alpha_range\\\": [0.409, 0.463], \\\"convergence_rho\\\": -0.2, \\\"convergence_p\\\": 0.783}, \\\"piqa\\\": {\\\"n_samples\\\": 1838, \\\"alpha_pure\\\": 0.143, \\\"alpha_range\\\": [0.132, 0.143], \\\"convergence_rho\\\": -0.5, \\\"convergence_p\\\": 0.45}, \\\"format_confound_test\\\": {\\\"finding\\\": \\\"PIQA (2-choice, α=0.14) vs WinoGrande (2-choice, α=0.46) vs BoolQ (2-choice, α=0.51) — same format, 3.5× α variation. Format confound refuted.\\\", \\\"alpha_vs_accuracy_rho\\\": 0.03, \\\"alpha_vs_accuracy_p_exact\\\": 1}, \\\"artifacts\\\": [\\\"winogrande_per_example.json\\\", \\\"piqa_per_example.json\\\", \\\"winogrande_jaccard_analysis.json\\\", \\\"piqa_jaccard_analysis.json\\\"]}, \\\"completed_at\\\": \\\"2026-05-21T10:27:33.995Z\\\"}, \\\"exp-boolq-hellaswag-eval\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-20T11:32:21.428Z\\\", \\\"updated_at\\\": \\\"2026-05-21T08:53:38.336Z\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash run_boolq_hellaswag_all.sh\\\", \\\"server\\\": \\\"westb-48145\\\", \\\"gpu\\\": [\\\"cuda:0\\\"], \\\"pid\\\": \\\"653104\\\", \\\"log_path\\\": \\\"~/runs/entrainment_gated_ft/exp-boolq-hellaswag-eval.log\\\", \\\"submitted_at\\\": \\\"2026-05-20T11:32:21.381Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"data_path\\\": \\\"/root/entrainment_gated_ft/lm_eval_clean/\\\", \\\"data_count\\\": 13312, \\\"model_name\\\": \\\"GDN/RetNet/HGRN2 x 5 ratios + Transformer (15 models)\\\", \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/models_1.3b/\\\", \\\"eval_data\\\": \\\"BoolQ (3270 samples) + HellaSwag (10042 samples)\\\", \\\"wall_clock_seconds\\\": 76877.0, \\\"gpu_hours\\\": 21.35}, \\\"reproduce\\\": {\\\"finished_at\\\": \\\"2026-05-20T12:47:53.740Z\\\"}, \\\"extra\\\": {\\\"hook_events\\\": [{\\\"event\\\": \\\"on_complete\\\", \\\"action\\\": \\\"agent\\\", \\\"ts\\\": \\\"2026-05-20T12:47:55.697105+00:00\\\"}]}, \\\"conclusion\\\": \\\"success\\\", \\\"checkpoint_path\\\": \\\"/root/entrainment_gated_ft/lm_eval_clean/boolq/ + /root/entrainment_gated_ft/lm_eval_clean/hellaswag/\\\", \\\"log_path\\\": \\\"/root/entrainment_gated_ft/lm_eval_clean/boolq_hellaswag_eval.log\\\", \\\"metrics\\\": {\\\"benchmarks\\\": [\\\"boolq\\\", \\\"hellaswag\\\"], \\\"boolq\\\": {\\\"n_samples\\\": 3270, \\\"ambiguity_alpha_mean\\\": 0.487, \\\"jaccard_helped_mean\\\": 0.103, \\\"jaccard_hurt_mean\\\": 0.098, \\\"convergence_rho\\\": 0.1, \\\"convergence_p\\\": 0.95, \\\"note\\\": \\\"GDN h24-1 acc=0.489 (near random) is genuine model performance, not eval bug. Selective overlap: GDN-RetNet significant, but GDN-HGRN2 and RetNet-HGRN2 often not significant\\\"}, \\\"hellaswag\\\": {\\\"n_samples\\\": 10042, \\\"ambiguity_alpha_mean\\\": 0.098, \\\"jaccard_helped_mean\\\": 0.091, \\\"jaccard_hurt_mean\\\": 0.08, \\\"convergence_rho\\\": -0.8, \\\"convergence_p\\\": 0.133, \\\"note\\\": \\\"90% samples unanimous across architectures. All Jaccard p<0.001 but nES very small (0.05-0.11)\\\"}, \\\"four_benchmark_summary\\\": {\\\"spectrum\\\": \\\"HellaSwag(α=0.10) < ARC-Easy(α=0.21) < LAMBADA(α=0.30) < BoolQ(α=0.49)\\\", \\\"key_finding\\\": \\\"Multiplicity varies dramatically by task (10%-49%) while Jaccard overlap stays consistently low (~0.08-0.10). Per-example divergence is universal but magnitude is task-dependent.\\\"}, \\\"artifacts\\\": [\\\"boolq_per_example.json\\\", \\\"boolq_jaccard_analysis.json\\\", \\\"hellaswag_per_example.json\\\", \\\"hellaswag_jaccard_analysis.json\\\"]}, \\\"hypothesis\\\": \\\"BoolQ 和 HellaSwag 的 per-example log_samples 数据扩展 multiplicity 分析到更多 benchmark，验证 per-example predictive multiplicity（α 和 cross-architecture Jaccard divergence）在不同任务类型上的普遍性——建立从 LAMBADA/ARC-Easy 到 4-benchmark spectrum 的泛化\\\", \\\"parent\\\": \\\"exp-011\\\", \\\"completed_at\\\": \\\"2026-05-21T08:53:38.336Z\\\"}, \\\"exp-015\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-20T10:05:29.020Z\\\", \\\"updated_at\\\": \\\"2026-05-20T10:06:09.562Z\\\", \\\"hypothesis\\\": \\\"Per-example predictive multiplicity (cross-architecture Jaccard divergence of helped/hurt sets, formal ambiguity α) exists on ARC-Easy (N=2376) even without aggregate convergence, establishing that multiplicity is a general property of hybrid architectures independent of task-specific convergence\\\", \\\"parent\\\": \\\"exp-arc-easy-eval\\\", \\\"spec\\\": {\\\"command\\\": \\\"Python analysis on westb-48145 (CPU)\\\", \\\"server\\\": \\\"westb-48145\\\", \\\"data_path\\\": \\\"/root/entrainment_gated_ft/lm_eval_clean/arc_easy/\\\", \\\"data_count\\\": 2376, \\\"model_name\\\": \\\"GDN/RetNet/HGRN2 x 5 ratios (15 models)\\\", \\\"seed\\\": \\\"N/A (deterministic eval)\\\", \\\"checkpoint_source\\\": \\\"exp-arc-easy-eval\\\", \\\"eval_data\\\": \\\"ARC-Easy (2376 samples)\\\"}, \\\"conclusion\\\": \\\"success\\\", \\\"checkpoint_path\\\": \\\"/root/entrainment_gated_ft/lm_eval_clean/arc_easy/\\\", \\\"log_path\\\": \\\"/root/entrainment_gated_ft/lm_eval_clean/arc_easy/\\\", \\\"completed_at\\\": \\\"2026-05-20T10:06:01.194Z\\\", \\\"metrics\\\": {\\\"benchmark\\\": \\\"arc_easy\\\", \\\"n_samples\\\": 2376, \\\"convergence\\\": {\\\"spearman_rho\\\": -0.2, \\\"p_exact\\\": 0.783, \\\"significant\\\": false}, \\\"jaccard_range\\\": {\\\"helped\\\": [0.067, 0.117], \\\"hurt\\\": [0.079, 0.134]}, \\\"normalized_ES_range\\\": [0.035, 0.135], \\\"all_24_jaccard_above_null\\\": true, \\\"multiplicity_arc_easy\\\": {\\\"alpha_range\\\": [0.201, 0.226], \\\"delta_range\\\": [2.32, 3.12]}, \\\"multiplicity_lambada\\\": {\\\"alpha_range\\\": [0.294, 0.316], \\\"delta_range\\\": [0.53, 0.61]}, \\\"claim\\\": \\\"Claim 3: per-example predictive multiplicity is general\\\", \\\"artifacts\\\": [\\\"arc_easy_per_example.json\\\", \\\"arc_easy_jaccard_analysis.json\\\", \\\"formal_multiplicity_metrics.json\\\"]}}, \\\"exp-arc-easy-eval\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-20T06:08:47.284Z\\\", \\\"updated_at\\\": \\\"2026-05-20T09:46:49.153Z\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/entrainment_gated_ft && bash run_arc_easy_all.sh\\\\\\\"\\\", \\\"server\\\": \\\"westb-48145\\\", \\\"gpu\\\": [\\\"cuda:0\\\"], \\\"pid\\\": \\\"620603\\\", \\\"log_path\\\": \\\"~/runs/entrainment_gated_ft/exp-arc-easy-eval.log\\\", \\\"submitted_at\\\": \\\"2026-05-20T06:08:47.244Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"wall_clock_seconds\\\": 11793.6, \\\"gpu_hours\\\": 3.28}, \\\"hypothesis\\\": \\\"Per-example divergence (low cross-architecture Jaccard of helped/hurt sets) exists on ARC-Easy as well as LAMBADA, establishing that per-example underspecification is not task-specific even when aggregate convergence is absent\\\", \\\"parent\\\": \\\"exp-001\\\", \\\"conclusion\\\": \\\"success\\\", \\\"checkpoint_path\\\": \\\"/root/entrainment_gated_ft/lm_eval_clean/arc_easy/\\\", \\\"log_path\\\": \\\"/root/entrainment_gated_ft/lm_eval_clean/arc_easy/\\\", \\\"completed_at\\\": \\\"2026-05-20T09:25:20.825Z\\\", \\\"metrics\\\": {\\\"benchmark\\\": \\\"arc_easy\\\", \\\"n_samples\\\": 2376, \\\"models_completed\\\": \\\"15/15\\\", \\\"acc_range\\\": [0.6961, 0.7412], \\\"convergence\\\": {\\\"spearman_rho\\\": -0.2, \\\"p_exact\\\": 0.783, \\\"significant\\\": false, \\\"sigma_pure\\\": 0.0964, \\\"sigma_h3_1\\\": 0.099}, \\\"jaccard_range\\\": {\\\"helped\\\": [0.067, 0.117], \\\"hurt\\\": [0.079, 0.134]}, \\\"normalized_ES_range\\\": [0.035, 0.135], \\\"all_24_jaccard_above_null\\\": true, \\\"multiplicity\\\": {\\\"alpha_range\\\": [0.201, 0.226], \\\"delta_range\\\": [2.32, 3.12]}, \\\"lambada_multiplicity\\\": {\\\"alpha_range\\\": [0.294, 0.316], \\\"delta_range\\\": [0.53, 0.61]}, \\\"key_finding\\\": \\\"Per-example multiplicity exists on ARC-Easy (alpha~0.21, Jaccard~0.07-0.13) WITHOUT aggregate convergence (rho=-0.20,p=0.78). Combined with LAMBADA (alpha~0.30 WITH convergence), per-example multiplicity is a general property not tied to convergence.\\\", \\\"artifacts\\\": [\\\"arc_easy_per_example.json\\\", \\\"arc_easy_jaccard_analysis.json\\\", \\\"formal_multiplicity_metrics.json\\\"]}}, \\\"exp-007\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-19T17:08:19.724Z\\\", \\\"updated_at\\\": \\\"2026-05-19T18:53:42.640Z\\\", \\\"hypothesis\\\": \\\"340M models show non-monotonic rebound in cross-architecture convergence at high attention ratios on LAMBADA, caused by capacity-limited interaction between attention and recurrent components — the rebound mechanism differs from 1.3B's complete convergence, establishing scale as a necessary condition for full equalization\\\", \\\"parent\\\": \\\"exp-001\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash run_exp007_logsamples.sh (run_lmeval_clean.py with allow_neg_eigval=True, --log_samples, --tasks lambada_openai)\\\", \\\"server\\\": \\\"westb-48145\\\", \\\"gpu\\\": \\\"cuda:0\\\", \\\"pid\\\": 530432, \\\"log_path\\\": \\\"~/runs/entrainment_gated_ft/exp-007.log\\\", \\\"submitted_at\\\": \\\"2026-05-19T17:51:40.355Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"data_path\\\": \\\"lambada_openai (lm-eval built-in)\\\", \\\"data_count\\\": \\\"5153 per model x 27 models\\\", \\\"model_name\\\": \\\"340M x16 + 1.3B x11 (GDN/RetNet/HGRN2 hybrids + Transformer)\\\", \\\"seed\\\": \\\"default\\\", \\\"checkpoint_source\\\": \\\"m-a-p pretrained (340M: /root/autodl-tmp/models/, 1.3B: /root/autodl-tmp/models_1.3b/)\\\", \\\"eval_data\\\": \\\"lambada_openai (lm-eval built-in, 5153 samples)\\\", \\\"checkpoint_path\\\": \\\"/root/entrainment_gated_ft/lm_eval_clean/exp007/\\\", \\\"wall_clock_seconds\\\": 3722.3, \\\"gpu_hours\\\": 1.03}, \\\"reproduce\\\": {\\\"finished_at\\\": \\\"2026-05-19T18:49:39.310Z\\\"}, \\\"extra\\\": {\\\"hook_events\\\": [{\\\"event\\\": \\\"on_complete\\\", \\\"action\\\": \\\"agent\\\", \\\"ts\\\": \\\"2026-05-19T18:49:41.012664+00:00\\\"}]}, \\\"metrics\\\": {\\\"340m_cross_arch_std\\\": {\\\"pure\\\": 0.02481, \\\"h24-1\\\": 0.011647, \\\"h12-1\\\": 0.017833, \\\"h6-1\\\": 0.011035, \\\"h3-1\\\": 0.016004}, \\\"340m_spearman_rho\\\": -0.5, \\\"340m_spearman_perm_p\\\": 0.45, \\\"1.3b_spearman_rho_ref\\\": -1, \\\"1.3b_spearman_perm_p_ref\\\": 0.0167, \\\"rebound_h3_1_delta\\\": 0.004969, \\\"rebound_h12_1_delta\\\": 0.006186, \\\"340m_h3_1_helped_jaccard\\\": 0.0944, \\\"340m_h3_1_hurt_jaccard\\\": 0.0899, \\\"models_completed\\\": 26, \\\"models_skipped\\\": 1}, \\\"conclusion\\\": \\\"success\\\", \\\"completed_at\\\": \\\"2026-05-19T18:53:42.640Z\\\"}, \\\"exp-004-r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-19T16:58:01.256Z\\\", \\\"updated_at\\\": \\\"2026-05-19T17:17:20.215Z\\\", \\\"hypothesis\\\": \\\"Attention weight patterns in hybrid h3-1 models differ systematically between helped and hurt samples on LAMBADA, with cross-architecture attention pattern similarity lower than expected given aggregate convergence — providing mechanistic evidence for architecture-specific per-example effects (Claim 3)\\\", \\\"parent\\\": \\\"exp-004\\\", \\\"spec\\\": {\\\"command\\\": \\\"python -u analysis/extract_attention_weights.py --arch {gdn,retnet,hgrn2} --device cuda:0 (sequential per arch)\\\", \\\"server\\\": \\\"westb-48145\\\", \\\"data_path\\\": \\\"EleutherAI/lambada_openai (default, split=test, cached)\\\", \\\"data_count\\\": 5153, \\\"model_name\\\": \\\"1.3B-100B-{GatedDeltaNet,RetNet,HGRN2}-hybrid-3-1\\\", \\\"seed\\\": 0, \\\"gpu\\\": \\\"cuda:0 (RTX PRO 6000)\\\", \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/models_1.3b/\\\", \\\"eval_data\\\": \\\"LAMBADA OpenAI (5153 samples)\\\", \\\"log_path\\\": \\\"/tmp/exp004.log\\\", \\\"pid\\\": 517172, \\\"output_dir\\\": \\\"/root/entrainment_gated_ft/analysis/attention_weights/\\\", \\\"progress\\\": \\\"gdn=DONE, retnet=42% running (PID 517172), hgrn2=PENDING\\\", \\\"session\\\": \\\"process detached with fd redirect to /tmp/exp004.log; tmux unavailable on server; screen available for hgrn2\\\", \\\"checkpoint_path\\\": \\\"/root/entrainment_gated_ft/analysis/attention_weights/\\\"}, \\\"conclusion\\\": \\\"success\\\", \\\"completed_at\\\": \\\"2026-05-19T17:17:10.232Z\\\", \\\"metrics\\\": {\\\"helped_vs_hurt_entropy_diff\\\": {\\\"gdn\\\": -0.0009, \\\"retnet\\\": 0.0179, \\\"hgrn2\\\": 0.002}, \\\"helped_vs_hurt_last5_mass\\\": {\\\"gdn_helped\\\": 0.0834, \\\"gdn_hurt\\\": 0.0831, \\\"retnet_helped\\\": 0.1578, \\\"retnet_hurt\\\": 0.1591, \\\"hgrn2_helped\\\": 0.0453, \\\"hgrn2_hurt\\\": 0.0467}, \\\"cross_arch_similarity_mean\\\": {\\\"gdn_vs_retnet\\\": 0.905, \\\"gdn_vs_hgrn2\\\": 0.766, \\\"hgrn2_vs_retnet\\\": 0.698}, \\\"cross_arch_similarity_deep_layers\\\": {\\\"gdn_vs_retnet_L20\\\": 0.986, \\\"gdn_vs_hgrn2_L20\\\": 0.942, \\\"hgrn2_vs_retnet_L20\\\": 0.943}, \\\"cross_arch_similarity_early_layers\\\": {\\\"gdn_vs_retnet_L2\\\": 0.995, \\\"gdn_vs_hgrn2_L2\\\": 0.244, \\\"hgrn2_vs_retnet_L2\\\": 0.196}, \\\"finding\\\": \\\"Attention entropy does NOT differentiate helped vs hurt samples — differences are negligible across all 3 architectures. Cross-arch: GDN and RetNet highly similar throughout; HGRN2 diverges in early layers but converges in deep layers (>0.94 at L20). The per-example effect is not visible at the attention pattern level.\\\", \\\"n_samples\\\": 5153, \\\"runtime_minutes\\\": 30, \\\"output_files\\\": [\\\"gdn_attention_patterns.pt\\\", \\\"gdn_attention_entropy.csv\\\", \\\"retnet_attention_patterns.pt\\\", \\\"retnet_attention_entropy.csv\\\", \\\"hgrn2_attention_patterns.pt\\\", \\\"hgrn2_attention_entropy.csv\\\", \\\"attention_analysis_summary.json\\\", \\\"cross_arch_attention_similarity.csv\\\", \\\"helped_vs_hurt_entropy.csv\\\"]}}, \\\"exp-011-xstorycloze\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-19T16:18:38.168Z\\\", \\\"updated_at\\\": \\\"2026-05-19T17:00:01.089Z\\\", \\\"hypothesis\\\": \\\"xstorycloze_en (StoryCloze equivalent, context completion task) shows significant cross-architecture convergence with attention ratio, providing a second statistically significant anchor beyond LAMBADA after Bonferroni correction\\\", \\\"parent\\\": \\\"exp-011\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash /root/entrainment_gated_ft/run_xstorycloze_batch.sh (PID 497694)\\\", \\\"server\\\": \\\"westb-48145\\\", \\\"data_path\\\": \\\"/root/autodl-tmp/models_1.3b/ (16 models)\\\", \\\"data_count\\\": 16, \\\"model_name\\\": \\\"GDN/RetNet/HGRN2 x 5 ratios + Transformer baseline (1.3B)\\\", \\\"seed\\\": 0, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/models_1.3b/ (Wang et al. pretrained)\\\", \\\"eval_data\\\": \\\"xstorycloze_en (juletxara/xstory_cloze, en split)\\\", \\\"gpu\\\": \\\"cuda:0 (RTX PRO 6000)\\\"}, \\\"conclusion\\\": \\\"negative\\\", \\\"checkpoint_path\\\": \\\"/root/entrainment_gated_ft/lm_eval_clean/xstorycloze/\\\", \\\"log_path\\\": \\\"/root/entrainment_gated_ft/nohup.out\\\", \\\"completed_at\\\": \\\"2026-05-19T16:32:04.959Z\\\", \\\"metrics\\\": {\\\"xstorycloze_en\\\": {\\\"rho\\\": -0.6, \\\"raw_p\\\": 0.35, \\\"bonferroni_adj_p_10\\\": 1, \\\"std_pure\\\": 0.0082, \\\"std_h3_1\\\": 0.0055, \\\"convergence_direction\\\": \\\"correct but weak\\\"}, \\\"ten_benchmark_bonferroni\\\": {\\\"significant_count\\\": \\\"0/10\\\", \\\"LAMBADA_adj_p\\\": 0.167, \\\"note\\\": \\\"No benchmark survives 10-benchmark Bonferroni\\\"}, \\\"method\\\": \\\"exact_permutation_test_two_tailed\\\", \\\"conclusion\\\": \\\"xstorycloze_en NOT a second anchor. Convergence is LAMBADA-specific. W1 unresolved via multi-benchmark approach.\\\"}}, \\\"exp-004\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-19T16:41:10.744Z\\\", \\\"updated_at\\\": \\\"2026-05-19T16:57:48.978Z\\\", \\\"hypothesis\\\": \\\"Attention layers in hybrid-3-1 models exhibit systematically different attention patterns (entropy, position distribution) between helped and hurt samples on LAMBADA, revealing how attention mediates the entrainment-gating effect across architectures.\\\", \\\"parent\\\": \\\"exp-003\\\", \\\"spec\\\": {\\\"command\\\": \\\"python extract_attention_weights.py (forward hooks on Q,K, manual softmax(QK^T/√d) with GQA expansion)\\\", \\\"server\\\": \\\"westb-48145\\\", \\\"data_path\\\": \\\"/root/entrainment_gated_ft/lm_eval_clean/lambada_openai per-example data\\\", \\\"data_count\\\": 5153, \\\"model_name\\\": \\\"GDN-h3-1, RetNet-h3-1, HGRN2-h3-1 (1.3B)\\\", \\\"seed\\\": 42, \\\"gpu\\\": \\\"cuda:0\\\", \\\"checkpoint_source\\\": \\\"Wang et al. pretrained weights\\\", \\\"eval_data\\\": \\\"lambada_openai (5153 examples)\\\", \\\"log_path\\\": \\\"/tmp/exp004.log (process died after Worker exited - nohup orphan)\\\", \\\"checkpoint_path\\\": \\\"N/A - process crashed before completion\\\", \\\"failure_reason\\\": \\\"Worker used nohup instead of submit_training_job/tmux; PID 515917 died after Worker exit. GPU idle since ~16:47 UTC.\\\"}, \\\"conclusion\\\": \\\"failed\\\", \\\"completed_at\\\": \\\"2026-05-19T16:57:48.978Z\\\"}, \\\"exp-011\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-19T14:12:29.428Z\\\", \\\"updated_at\\\": \\\"2026-05-19T16:37:27.600Z\\\", \\\"hypothesis\\\": \\\"Cross-architecture variance on additional retrieval-dependent benchmarks (StoryCloze, BoolQ, COPA, PIQA, SciQ) decreases monotonically with attention ratio, providing a second statistically significant anchor (exact permutation p<0.05, two-tailed) beyond LAMBADA after Bonferroni correction\\\", \\\"parent\\\": \\\"exp-001\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash /root/entrainment_gated_ft/run_exp011_batch.sh (nohup PID 474289)\\\", \\\"server\\\": \\\"westb-48145\\\", \\\"data_path\\\": \\\"/root/autodl-tmp/models_1.3b/ (16 models)\\\", \\\"data_count\\\": 16, \\\"model_name\\\": \\\"GDN/RetNet/HGRN2 x 5 ratios + Transformer baseline (1.3B)\\\", \\\"seed\\\": 0, \\\"eval_data\\\": \\\"boolq, copa, piqa, sciq (4 benchmarks x 16 models)\\\", \\\"gpu\\\": \\\"cuda:0 (RTX PRO 6000)\\\", \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/models_1.3b/ (Wang et al. pretrained checkpoints)\\\"}, \\\"conclusion\\\": \\\"negative\\\", \\\"checkpoint_path\\\": \\\"/root/entrainment_gated_ft/lm_eval_clean/exp011/\\\", \\\"log_path\\\": \\\"/root/entrainment_gated_ft/lm_eval_clean/exp011/run_all.log\\\", \\\"completed_at\\\": \\\"2026-05-19T16:14:41.324Z\\\", \\\"metrics\\\": {\\\"boolq\\\": {\\\"rho\\\": 0.2, \\\"raw_p\\\": 0.7833, \\\"bonferroni_adj_p_9\\\": 1, \\\"std_pure\\\": 0.0163, \\\"std_h3_1\\\": 0.0236, \\\"convergence\\\": false}, \\\"piqa\\\": {\\\"rho\\\": -0.5, \\\"raw_p\\\": 0.45, \\\"bonferroni_adj_p_9\\\": 1, \\\"std_pure\\\": 0.0054, \\\"std_h3_1\\\": 0.0034, \\\"convergence\\\": false}, \\\"sciq\\\": {\\\"rho\\\": 0.1, \\\"raw_p\\\": 0.95, \\\"bonferroni_adj_p_9\\\": 1, \\\"std_pure\\\": 0.0087, \\\"std_h3_1\\\": 0.0074, \\\"convergence\\\": false}, \\\"copa_supplementary\\\": {\\\"rho\\\": -0.67, \\\"raw_p\\\": 0.2667, \\\"std_pure\\\": 0.0262, \\\"std_h3_1\\\": 0.0047, \\\"convergence_ratio\\\": 5.57, \\\"note\\\": \\\"supplementary only (n=100), not in main Bonferroni\\\"}, \\\"LAMBADA_recomputed\\\": {\\\"rho\\\": -1, \\\"raw_p\\\": 0.0167, \\\"bonferroni_adj_p_6\\\": 0.1, \\\"bonferroni_adj_p_10\\\": 0.167, \\\"note\\\": \\\"6-Bonf=0.100 (D003 pre-registered); 10-Bonf=0.167; does not survive strict Bonferroni\\\"}, \\\"merged_10benchmark_significant_count\\\": \\\"0/10\\\", \\\"method\\\": \\\"exact_permutation_test_two_tailed\\\", \\\"D009_strategy\\\": \\\"BCa CI [-1.0,-0.7] as primary evidence; 6-Bonf adj_p=0.100 reported honestly; 10-benchmark negative -> task-specificity positive evidence (supplementary); underpowered caveat in Limitations\\\", \\\"D009_prohibited\\\": \\\"NO post-hoc 2-benchmark Bonferroni; NO post-hoc rho<0 subset correction\\\", \\\"conclusion\\\": \\\"No second anchor. Convergence LAMBADA-specific. W1 addressed via task-specificity reframing (D009).\\\"}}, \\\"exp-010\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-19T15:08:21.255Z\\\", \\\"updated_at\\\": \\\"2026-05-19T15:12:28.565Z\\\", \\\"hypothesis\\\": \\\"Aggregate convergence (cross-arch std decreasing with attention ratio) and per-example divergence (low Jaccard of helped/hurt sets) co-evolve as attention ratio increases on LAMBADA — demonstrating underspecification: architectures converge in aggregate performance while helping/hurting almost entirely different samples\\\", \\\"parent\\\": \\\"exp-001\\\", \\\"spec\\\": {\\\"command\\\": \\\"python3 /root/entrainment_gated_ft/analysis/exp010_bridge_analysis.py\\\", \\\"server\\\": \\\"westb-48145\\\", \\\"data_path\\\": \\\"/root/entrainment_gated_ft/lm_eval_clean/\\\", \\\"data_count\\\": 5153, \\\"model_name\\\": \\\"GDN/RetNet/HGRN2 x 5 ratios (1.3B)\\\", \\\"seed\\\": 0, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/models_1.3b/ (Wang et al. pretrained)\\\", \\\"eval_data\\\": \\\"LAMBADA OpenAI per-example logprob (5153 samples)\\\"}, \\\"checkpoint_path\\\": \\\"/root/entrainment_gated_ft/analysis/exp010_bridge_results.csv\\\", \\\"log_path\\\": \\\"/root/entrainment_gated_ft/analysis/exp010_bridge_summary.json\\\", \\\"conclusion\\\": \\\"success\\\", \\\"completed_at\\\": \\\"2026-05-19T15:09:01.266Z\\\", \\\"metrics\\\": {\\\"aggregate_convergence\\\": {\\\"std_pure\\\": 0.024, \\\"std_h24_1\\\": 0.0162, \\\"std_h12_1\\\": 0.0136, \\\"std_h6_1\\\": 0.0061, \\\"std_h3_1\\\": 0.0049, \\\"reduction_ratio\\\": 0.8, \\\"note\\\": \\\"Cross-arch std drops 5x monotonically\\\"}, \\\"per_example_divergence\\\": {\\\"jaccard_helped_range\\\": [0.092, 0.1], \\\"jaccard_hurt_range\\\": [0.081, 0.099], \\\"net_asymmetry_range\\\": [0.013, 0.04], \\\"net_asymmetry_trend\\\": \\\"increasing with attention ratio\\\", \\\"note\\\": \\\"Jaccard saturates at ~0.095 by 4% attention (h24-1), flat thereafter\\\"}, \\\"co_evolution_spearman\\\": {\\\"std_vs_J_helped\\\": {\\\"rho\\\": -0.7, \\\"exact_p\\\": 0.23}, \\\"std_vs_J_hurt\\\": {\\\"rho\\\": -0.8, \\\"exact_p\\\": 0.13}, \\\"CAVEAT\\\": \\\"D008: rho inflated by pure=0 degeneracy (Jaccard=NaN->0). Excluding pure: rho=-0.40, p=0.75. NOT co-evolution.\\\"}, \\\"key_finding\\\": \\\"DECOUPLING (D008): minimal attention (4%) creates per-example specificity (Jaccard saturates ~0.095), gradual attention drives aggregate convergence (sigma 0.024->0.005). Two processes operate on different timescales. Net asymmetry INCREASES (0.013->0.040).\\\", \\\"narrative_constraints\\\": \\\"PROHIBITED: co-evolution, paradoxical coexistence, paradox. USE: decoupling, different timescales.\\\"}}, \\\"exp-001\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-19T13:32:43.793Z\\\", \\\"updated_at\\\": \\\"2026-05-19T15:00:43.856Z\\\", \\\"hypothesis\\\": \\\"Cross-architecture variance (std) on retrieval-dependent tasks decreases monotonically with attention ratio at 1.3B scale, while reasoning-dependent tasks show no convergence — establishing task-specificity as a principled feature of the equalizer effect, not a limitation\\\", \\\"spec\\\": {\\\"command\\\": \\\"python analysis: compute cross-arch std + Spearman rho for 6 benchmarks x 5 attention ratios\\\", \\\"server\\\": \\\"westb-48145\\\", \\\"data_path\\\": \\\"/root/entrainment_gated_ft/lm_eval_clean/ (summary_all_1.3b.csv + 340M results)\\\", \\\"data_count\\\": 26, \\\"model_name\\\": \\\"16x1.3B + 10x340M (GDN/RetNet/HGRN2)\\\", \\\"seed\\\": 0}, \\\"checkpoint_path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/exp-001/data/task_specificity_results.csv\\\", \\\"log_path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/logs/workers/worker_research_wang_differentiation_20260519T130431.log\\\", \\\"conclusion\\\": \\\"success\\\", \\\"completed_at\\\": \\\"2026-05-19T13:33:45.162Z\\\", \\\"metrics\\\": {\\\"LAMBADA\\\": {\\\"rho\\\": -1, \\\"p\\\": 0.0167, \\\"significant\\\": false, \\\"taxonomy\\\": \\\"retrieval-dependent\\\", \\\"note\\\": \\\"exact permutation two-tailed (was 0.008 one-tailed)\\\"}, \\\"HellaSwag\\\": {\\\"rho\\\": 0.3, \\\"p\\\": 0.6833, \\\"significant\\\": false, \\\"taxonomy\\\": \\\"reasoning-dependent\\\"}, \\\"ARC-C\\\": {\\\"rho\\\": 0.6, \\\"p\\\": 0.35, \\\"significant\\\": false, \\\"taxonomy\\\": \\\"reasoning-dependent\\\"}, \\\"Winogrande\\\": {\\\"rho\\\": 0.1, \\\"p\\\": 0.95, \\\"significant\\\": false, \\\"taxonomy\\\": \\\"reasoning-dependent\\\"}, \\\"ARC-Easy\\\": {\\\"rho\\\": -0.7, \\\"p\\\": 0.2333, \\\"significant\\\": false, \\\"taxonomy\\\": \\\"mixed\\\"}, \\\"MMLU\\\": {\\\"rho\\\": -0.7, \\\"p\\\": 0.2333, \\\"significant\\\": false, \\\"taxonomy\\\": \\\"mixed\\\"}, \\\"significant_count\\\": \\\"0/6\\\", \\\"summary\\\": \\\"LAMBADA shows perfect negative correlation (rho=-1.0) but exact permutation two-tailed p=0.0167 (Bonferroni adj-p=0.100, not significant). Reasoning tasks show no convergence. Mixed tasks suggestive but underpowered (n=5).\\\", \\\"method\\\": \\\"exact_permutation_test_two_tailed\\\"}}, \\\"exp-008\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-19T14:12:33.026Z\\\", \\\"updated_at\\\": \\\"2026-05-19T14:28:33.593Z\\\", \\\"hypothesis\\\": \\\"Replacing scipy.stats.spearmanr asymptotic p-values with exact permutation tests (n=5, 120 permutations, two-tailed) corrects the spurious p=1.4e-24 bug; expected: LAMBADA raw p≈0.017, Bonferroni adj-p≈0.100 (not significant), confirming need for additional benchmarks\\\", \\\"parent\\\": \\\"exp-001\\\", \\\"checkpoint_path\\\": \\\"/root/entrainment_gated_ft/analysis/robustness_results.csv\\\", \\\"log_path\\\": \\\"/root/entrainment_gated_ft/analysis/robustness_summary.md\\\", \\\"conclusion\\\": \\\"success\\\", \\\"spec\\\": {\\\"command\\\": \\\"python3 /root/entrainment_gated_ft/analysis/statistical_robustness.py\\\", \\\"server\\\": \\\"westb-48145\\\", \\\"data_path\\\": \\\"/root/entrainment_gated_ft/lm_eval_clean/summary_all_1.3b.csv\\\", \\\"data_count\\\": 15, \\\"model_name\\\": \\\"GDN/HGRN2/RetNet 1.3B (5 attn ratios x 3 archs)\\\", \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"/root/entrainment_gated_ft/lm_eval_clean/summary_all_1.3b.csv\\\", \\\"eval_data\\\": \\\"6 benchmarks x 15 model configs (summary_all_1.3b.csv)\\\"}, \\\"metrics\\\": {\\\"LAMBADA\\\": {\\\"rho\\\": -1, \\\"raw_p\\\": 0.0167, \\\"bonferroni_adj_p\\\": 0.1, \\\"bh_fdr_adj_p\\\": 0.1}, \\\"HellaSwag\\\": {\\\"rho\\\": 0.3, \\\"raw_p\\\": 0.6833, \\\"bonferroni_adj_p\\\": 1, \\\"bh_fdr_adj_p\\\": 0.82}, \\\"WinoGrande\\\": {\\\"rho\\\": 0.1, \\\"raw_p\\\": 0.95, \\\"bonferroni_adj_p\\\": 1, \\\"bh_fdr_adj_p\\\": 0.95}, \\\"ARC-Easy\\\": {\\\"rho\\\": -0.7, \\\"raw_p\\\": 0.2333, \\\"bonferroni_adj_p\\\": 1, \\\"bh_fdr_adj_p\\\": 0.4667}, \\\"ARC-Challenge\\\": {\\\"rho\\\": 0.6, \\\"raw_p\\\": 0.35, \\\"bonferroni_adj_p\\\": 1, \\\"bh_fdr_adj_p\\\": 0.525}, \\\"MMLU\\\": {\\\"rho\\\": -0.7, \\\"raw_p\\\": 0.2333, \\\"bonferroni_adj_p\\\": 1, \\\"bh_fdr_adj_p\\\": 0.4667}, \\\"method\\\": \\\"exact_permutation_test_two_tailed\\\", \\\"n_permutations\\\": 120, \\\"bug_fixed\\\": \\\"scipy.stats.spearmanr asymptotic p replaced with exact permutation\\\", \\\"bootstrap_ci\\\": {\\\"benchmark\\\": \\\"LAMBADA\\\", \\\"method\\\": \\\"architecture_resampling_percentile\\\", \\\"ci_lower\\\": -1, \\\"ci_upper\\\": -0.7, \\\"crosses_zero\\\": false, \\\"n_bootstrap\\\": 10000, \\\"n_valid\\\": 8875, \\\"seed\\\": 42, \\\"p_rho_negative\\\": 1, \\\"p_rho_positive\\\": 0, \\\"bca_note\\\": \\\"BCa degenerate at rho=-1.0 boundary; percentile CI used\\\"}, \\\"gdn_excluded\\\": {\\\"LAMBADA\\\": {\\\"rho\\\": -0.7, \\\"exact_p\\\": 0.2333, \\\"direction\\\": \\\"WEAKER\\\"}, \\\"HellaSwag\\\": {\\\"rho\\\": 0.5, \\\"exact_p\\\": 0.45, \\\"direction\\\": \\\"STRONGER\\\"}, \\\"WinoGrande\\\": {\\\"rho\\\": 0.3, \\\"exact_p\\\": 0.6833, \\\"direction\\\": \\\"STRONGER\\\"}, \\\"ARC-Easy\\\": {\\\"rho\\\": -0.9, \\\"exact_p\\\": 0.0833, \\\"direction\\\": \\\"STRONGER\\\"}, \\\"ARC-Challenge\\\": {\\\"rho\\\": -0.2, \\\"exact_p\\\": 0.7833, \\\"direction\\\": \\\"WEAKER\\\"}, \\\"MMLU\\\": {\\\"rho\\\": 0.6, \\\"exact_p\\\": 0.35, \\\"direction\\\": \\\"WEAKER\\\"}, \\\"note\\\": \\\"ARC-Easy rho improves from -0.7 to -0.9 (p=0.0833) without GDN confound — suggestive second anchor\\\"}}, \\\"completed_at\\\": \\\"2026-05-19T14:18:07.535Z\\\"}, \\\"exp-003-p2v2\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-19T14:13:12.772Z\\\", \\\"updated_at\\\": \\\"2026-05-19T14:20:24.378Z\\\", \\\"hypothesis\\\": \\\"Helped samples have higher pure-model perplexity (model uncertain → attention helped) while hurt samples have lower perplexity (model confident → attention interfered), with architecture-specific patterns across GDN/RetNet/HGRN2. Retry with HGRN2 monkey-patch fix for _tied_weights_keys AttributeError.\\\", \\\"parent\\\": \\\"exp-003-p2\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"exp-003-p2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-19T13:52:59.192Z\\\", \\\"updated_at\\\": \\\"2026-05-19T14:06:41.114Z\\\", \\\"hypothesis\\\": \\\"Helped samples have higher pure-model perplexity (model was uncertain → attention helped), while hurt samples have lower pure-model perplexity (model was confident → attention interfered). This pattern is architecture-specific.\\\", \\\"parent\\\": \\\"exp-003\\\", \\\"spec\\\": {\\\"command\\\": \\\"python3 /root/entrainment_gated_ft/analysis/sample_perplexity_analysis.py\\\", \\\"server\\\": \\\"westb-48145\\\", \\\"data_path\\\": \\\"/root/entrainment_gated_ft/lm_eval_clean\\\", \\\"data_count\\\": 5153, \\\"model_name\\\": \\\"GDN-pure, RetNet-pure, HGRN2-pure (1.3B)\\\", \\\"seed\\\": \\\"N/A\\\", \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/models_1.3b/{GDN,RetNet,HGRN2}-pure\\\", \\\"eval_data\\\": \\\"LAMBADA OpenAI (5153 samples)\\\"}, \\\"conclusion\\\": \\\"negative\\\", \\\"log_path\\\": \\\"/root/entrainment_gated_ft/analysis/sample_perplexity_summary.json\\\", \\\"checkpoint_path\\\": \\\"/root/entrainment_gated_ft/analysis/sample_perplexity_results.csv\\\", \\\"completed_at\\\": \\\"2026-05-19T14:06:38.461Z\\\", \\\"metrics\\\": {\\\"GDN\\\": {\\\"U\\\": 148410, \\\"p\\\": 0.209189, \\\"r_rb\\\": -0.0447, \\\"helped_mean\\\": 3.3695, \\\"hurt_mean\\\": 3.3382}, \\\"RetNet\\\": {\\\"U\\\": 107210, \\\"p\\\": 0.659319, \\\"r_rb\\\": -0.0168, \\\"helped_mean\\\": 3.4432, \\\"hurt_mean\\\": 3.4207}, \\\"HGRN2\\\": {\\\"U\\\": 112999, \\\"p\\\": 0.247856, \\\"r_rb\\\": -0.0441, \\\"helped_mean\\\": 3.3775, \\\"hurt_mean\\\": 3.3538}, \\\"cross_arch_helped_KW_p\\\": 0.020136, \\\"cross_arch_hurt_KW_p\\\": 0.000498}}, \\\"exp-003\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-19T13:38:18.995Z\\\", \\\"updated_at\\\": \\\"2026-05-19T13:38:51.683Z\\\", \\\"hypothesis\\\": \\\"Architecture-specific helped/hurt samples on LAMBADA differ in surface features (token frequency, context length, lexical complexity), AND these feature profiles differ across GDN/HGRN2/RetNet — indicating architecture-specific mechanisms rather than generic attention benefit\\\", \\\"spec\\\": {\\\"command\\\": \\\"python analysis/sample_characterization.py — surface feature analysis of helped/hurt samples\\\", \\\"server\\\": \\\"westb-48145\\\", \\\"data_path\\\": \\\"/root/entrainment_gated_ft/lm_eval_clean/ (per-example logprob data)\\\", \\\"data_count\\\": 5153, \\\"model_name\\\": \\\"GDN/HGRN2/RetNet 1.3B h3-1 vs pure\\\", \\\"seed\\\": 0}, \\\"checkpoint_path\\\": \\\"/root/entrainment_gated_ft/analysis/sample_characterization_results.csv\\\", \\\"log_path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/logs/workers/worker_analysis_exp_003_sample_characterization_20260519T131141.log\\\", \\\"conclusion\\\": \\\"negative\\\", \\\"metrics\\\": {\\\"GDN\\\": {\\\"helped\\\": 462, \\\"hurt\\\": 615, \\\"net\\\": -153, \\\"surface_features_significant\\\": false}, \\\"HGRN2\\\": {\\\"helped\\\": 548, \\\"hurt\\\": 395, \\\"net\\\": 153, \\\"surface_features_significant\\\": false}, \\\"RetNet\\\": {\\\"helped\\\": 426, \\\"hurt\\\": 495, \\\"net\\\": -69, \\\"context_length_p\\\": 0.012, \\\"context_length_r\\\": -0.096, \\\"unique_tokens_p\\\": 0.009, \\\"unique_tokens_r\\\": -0.099}, \\\"cross_arch_difference\\\": \\\"not_significant\\\", \\\"pass_fail\\\": \\\"FAIL — RetNet context_unique_tokens p=0.009 passes criterion 1 for one arch only; criterion 2 (cross-arch difference) fails\\\", \\\"summary\\\": \\\"Surface features do not explain helped/hurt identity. Rules out trivial explanations (frequency, length, diversity). RetNet shows weak context-length signal (p=0.012, r=-0.096).\\\"}, \\\"completed_at\\\": \\\"2026-05-19T13:38:51.683Z\\\"}, \\\"exp-009\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-19T13:32:43.818Z\\\", \\\"updated_at\\\": \\\"2026-05-19T13:33:45.506Z\\\", \\\"hypothesis\\\": \\\"Our equalizer effect analysis provides fully novel contributions relative to Wang et al. (arXiv 2507.06457) across 4 dimensions: convergence quantification (Spearman ρ + permutation test vs qualitative observation), scale dependency (quantitative 1.3B vs 340M contrast vs binary statement), per-example mechanism (Jaccard + net effect analysis vs absent), and task-specificity (convergence-strength by task type vs ratio-sensitivity)\\\", \\\"spec\\\": {\\\"command\\\": \\\"literature analysis: extract Wang et al. (2507.06457) exact claims, compare 4 differentiation dimensions\\\", \\\"server\\\": \\\"local + westb-48145\\\", \\\"data_path\\\": \\\"Wang et al. arXiv 2507.06457 + task_specificity_results.csv\\\", \\\"data_count\\\": 1, \\\"model_name\\\": \\\"N/A (literature analysis)\\\", \\\"seed\\\": 0}, \\\"checkpoint_path\\\": \\\"/root/entrainment_gated_ft/analysis/wang_et_al_differentiation.md\\\", \\\"log_path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/logs/workers/worker_research_exp_009_wang_differentiation_20260519T131120.log\\\", \\\"conclusion\\\": \\\"success\\\", \\\"completed_at\\\": \\\"2026-05-19T13:33:45.506Z\\\"}, \\\"eval_340m_retnet_hgrn2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-19T04:03:58.762Z\\\", \\\"updated_at\\\": \\\"2026-05-19T04:32:37.289Z\\\", \\\"hypothesis\\\": \\\"340M RetNet and HGRN2 models will show the same architecture-dependent attention effect observed at 1.3B scale: HGRN2 benefits from attention while RetNet shows minimal benefit, with task-dependent equalizer effect on LAMBADA\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash /root/entrainment_gated_ft/run_all_340m_eval.sh\\\", \\\"server\\\": \\\"westb-48145\\\", \\\"data_path\\\": \\\"/root/autodl-tmp/models/\\\", \\\"data_count\\\": 10, \\\"model_name\\\": \\\"340M RetNet×5 + HGRN2×5\\\", \\\"seed\\\": 0}, \\\"conclusion\\\": \\\"success\\\", \\\"checkpoint_path\\\": \\\"/root/entrainment_gated_ft/lm_eval_clean/340m/\\\", \\\"log_path\\\": \\\"/root/entrainment_gated_ft/lm_eval_clean/340m/run_all.log\\\", \\\"completed_at\\\": \\\"2026-05-19T04:32:37.289Z\\\"}, \\\"hgrn2_eval_h3_1\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-18T16:47:57.853Z\\\", \\\"updated_at\\\": \\\"2026-05-18T16:53:12.858Z\\\", \\\"spec\\\": {\\\"command\\\": \\\"HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1 python run_lmeval_clean.py --model_path 1.3B-100B-HGRN2-hybrid-3-1 --tasks 6tasks --batch_size 8\\\", \\\"server\\\": \\\"westb-48145\\\", \\\"data_path\\\": \\\"/root/autodl-tmp/models_1.3b/1.3B-100B-HGRN2-hybrid-3-1\\\", \\\"data_count\\\": 1, \\\"model_name\\\": \\\"HGRN2-1.3B-hybrid-3-1\\\", \\\"seed\\\": 0}, \\\"conclusion\\\": \\\"success\\\", \\\"checkpoint_path\\\": \\\"/root/entrainment_gated_ft/lm_eval_clean/1.3B-100B-HGRN2-hybrid-3-1.json\\\", \\\"log_path\\\": \\\"/tmp/hgrn2_eval_h3_1.log\\\", \\\"hypothesis\\\": \\\"HGRN2 hybrid-3-1 (highest attention ratio) will show less degradation on composition-heavy benchmarks compared to pure linear models, following the attention-ratio degradation pattern observed in GDN and RetNet families\\\", \\\"completed_at\\\": \\\"2026-05-18T16:53:12.858Z\\\"}, \\\"hgrn2_eval_1_3b_all\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-18T15:57:15.535Z\\\", \\\"updated_at\\\": \\\"2026-05-18T16:00:12.920Z\\\", \\\"spec\\\": {\\\"command\\\": \\\"python run_lmeval_clean.py --model_path {MODEL} --tasks lambada_openai,hellaswag,winogrande,arc_easy,arc_challenge,mmlu --output_dir lm_eval_clean/ --batch_size 8 (x3 models: hybrid-12-1, hybrid-24-1, hybrid-3-1)\\\", \\\"server\\\": \\\"westb-48145\\\", \\\"data_path\\\": \\\"/root/autodl-tmp/models_1.3b/\\\", \\\"data_count\\\": 3, \\\"model_name\\\": \\\"HGRN2-1.3B (3 hybrid variants)\\\", \\\"seed\\\": 0}, \\\"conclusion\\\": \\\"killed\\\", \\\"completed_at\\\": \\\"2026-05-18T16:00:12.920Z\\\"}}, \\\"count\\\": 40, \\\"total\\\": 40, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.0959}}\"}",
      "numLines": 1,
      "startLine": 1,
      "totalLines": 1
    }
  },
  "sourceToolAssistantUUID": "e0a2fe02-939a-4ef2-b3bd-fc442aa65c19",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/sessions/agent_aa1a2296",
  "sessionId": "ccd4bb6d-9c70-4ece-9e7e-8b842791a0aa",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 30_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[CRON] 实验进程已正常退出，状态已转为 ANALYZING，需要你分析结果并推进到 DONE。 详情: Process exited cleanly, W&B data available  - exp_id: exp-005-gla-pure - project: entrainment_gated_ft - server: westb-48145 - log_path: ~/runs/e…",
  "leafUuid": "ec69d089-ac7d-4469-8ff1-e8ecb0f61fd0",
  "sessionId": "ccd4bb6d-9c70-4ece-9e7e-8b842791a0aa"
}
```

---

### Runtime record

_source line 31_

```json
{
  "type": "ai-title",
  "aiTitle": "Analyze experiment results and mark as done",
  "sessionId": "ccd4bb6d-9c70-4ece-9e7e-8b842791a0aa"
}
```

---

### Tool result

_source line 32 · 2026-05-22T16:42:14.457Z_

<details><summary>↩ Tool result · `toolu_01G2WS4qHRoaGKG3P313Cbg2`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": [{\"id\": \"exp-001\", \"registry_id\": \"exp-001\", \"claim\": 1, \"title\": \"Task-specificity characterization of equalizer effect\", \"description\": \"Compute cross-architecture variance (std) at each attention ratio for all 6 benchmarks. Known: only LAMBADA shows significant convergence (p<0.05). Goal: build principled task taxonomy (retrieval-dependent vs reasoning-dependent) explaining WHY convergence is task-specific. LAMBADA = last-word retrieval from context; HellaSwag/ARC = multi-step reasoning. Show the dichotomy is a feature (task-type modulation), not a limitation.\\n\", \"priority\": \"P0\", \"type\": \"analysis\", \"gpu_budget_hours\": 0, \"deps\": [], \"data_source\": \"existing summary_all_1.3b.csv + 340M results + cross_scale_convergence output\", \"pass_fail\": \"Clear task-type dichotomy with principled taxonomy; convergence correlates with retrieval demand\", \"reviewer_risk\": \"Risk A — reframed per Reviewer warning: single-task convergence → task-specificity as positive finding\", \"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"LAMBADA\": {\"rho\": -1, \"p\": 0.0167, \"significant\": false, \"taxonomy\": \"retrieval-dependent\", \"note\": \"exact permutation two-tailed (was 0.008 one-tailed)\"}, \"HellaSwag\": {\"rho\": 0.3, \"p\": 0.6833, \"significant\": false, \"taxonomy\": \"reasoning-dependent\"}, \"ARC-C\": {\"rho\": 0.6, \"p\": 0.35, \"significant\": false, \"taxonomy\": \"reasoning-dependent\"}, \"Winogrande\": {\"rho\": 0.1, \"p\": 0.95, \"significant\": false, \"taxonomy\": \"reasoning-dependent\"}, \"ARC-Easy\": {\"rho\": -0.7, \"p\": 0.2333, \"significant\": false, \"taxonomy\": \"mixed\"}, \"MMLU\": {\"rho\": -0.7, \"p\": 0.2333, \"significant\": false, \"taxonomy\": \"mixed\"}, \"significant_count\": \"0/6\", \"summary\": \"LAMBADA shows perfect negative correlation (rho=-1.0) but exact permutation two-tailed p=0.0167 (Bonferroni adj-p=0.100, not significant). Reasoning tasks show no convergence. Mixed tasks suggestive but underpowered (n=5).\", \"method\": \"exact_permutation_test_two_tailed\"}}, {\"id\": \"exp-002\", \"claim\": 1, \"title\": \"Multi-benchmark per-example analysis (task-specificity validation)\", \"description\": \"Re-run lm-eval on 1.3B models with --log_samples for HellaSwag, ARC-easy, ARC-challenge. Two goals: (a) confirm task-specificity — per-example convergence absent on reasoning tasks, (b) characterize HOW attention affects per-example behavior on non-converging tasks (random noise vs systematic but architecture-specific). Strengthens Claim 1 regardless of outcome.\\n\", \"priority\": \"cancelled\", \"type\": \"experiment\", \"gpu_budget_hours\": 0, \"deps\": [\"exp-001\"], \"pass_fail\": \"Per-example data collected for ≥3 benchmarks; task-specificity of per-example mechanism confirmed or refuted\", \"reviewer_risk\": \"Risk B — outcome determines Claim 1 scope: cross-task vs retrieval-specific equalizer\", \"note\": \"CANCELLED (D010, 2026-05-19): Expected value negative after D009 task-specificity reframing. Most likely outcome (non-LAMBADA also low Jaccard) would weaken task-specificity narrative. 20h GPU reallocated to exp-007 + buffer.\", \"status\": \"planned\"}, {\"id\": \"exp-006\", \"claim\": 2, \"title\": \"7B model evaluation — CANCELLED (unavailable)\", \"description\": \"Wang et al. only have 340M + 1.3B (72 models total). Paper Limitations explicitly excludes 10B+. No 7B models exist. Budget reallocated to exp-002/004/005.\\n\", \"priority\": \"cancelled\", \"type\": \"experiment\", \"gpu_budget_hours\": 0, \"deps\": [], \"pass_fail\": \"N/A — 7B unavailable, confirmed 2026-05-19\", \"status\": \"planned\"}, {\"id\": \"exp-007\", \"claim\": 2, \"title\": \"340M rebound mechanism analysis (upgraded: compensate 7B absence)\", \"description\": \"Deep analysis of 340M non-monotonic rebound at attn=8. Per-example comparison with 1.3B at same attention ratio to identify which samples diverge. Characterize rebound samples. With 7B unavailable, this becomes the primary vehicle for Claim 2 depth — show the binary contrast (340M partial vs 1.3B complete) has mechanistic explanation, not just correlation with scale. Analyze training token count (20B vs 100B) as confound vs scale.\\n\", \"priority\": \"P0\", \"type\": \"analysis\", \"gpu_budget_hours\": 2, \"deps\": [], \"data_source\": \"existing 340M + 1.3B LAMBADA per-example logprob data (if available from MVP); else rerun 340M with --log_samples\", \"pass_fail\": \"Rebound mechanism identified with principled explanation; 340M vs 1.3B contrast characterized beyond aggregate metrics\", \"note\": \"Upgraded from P1 to P0 after 7B cancellation. May need 340M per-example rerun (2h GPU).\", \"status\": \"planned\"}, {\"id\": \"exp-003\", \"registry_id\": \"exp-003\", \"claim\": 3, \"title\": \"Helped/hurt sample characterization\", \"description\": \"For each architecture's helped/hurt samples on LAMBADA, compute: (a) target token frequency (unigram rank in training data proxy), (b) context length (token count), (c) last-sentence complexity (perplexity under baseline), (d) topic/domain distribution. Test whether architecture-specific sample subsets differ on these features.\\n\", \"priority\": \"P0\", \"type\": \"analysis\", \"gpu_budget_hours\": 1, \"deps\": [], \"data_source\": \"existing lambada per-example logprob data\", \"pass_fail\": \"≥1 feature significantly differentiates helped vs hurt samples (p<0.01), AND features differ across architectures\", \"status_note\": \"Phase 1 (surface features) DONE: all non-significant within-arch (p>0.2). Phase 2 (perplexity) DONE: within-arch perplexity also non-significant (r_rb≈-0.04, p>0.2). PASS on second criterion: cross-arch KW significant (hurt p=0.0005, helped p=0.020). Different archs help/hurt samples with systematically different baseline difficulty profiles. Both negative within-arch results are informative (rules out trivial explanations). Cross-arch finding strengthens Claim 3 (architecture-specificity is structured, not random).\\n\", \"status\": \"DONE\", \"conclusion\": \"negative\", \"metrics\": {\"GDN\": {\"helped\": 462, \"hurt\": 615, \"net\": -153, \"surface_features_significant\": false}, \"HGRN2\": {\"helped\": 548, \"hurt\": 395, \"net\": 153, \"surface_features_significant\": false}, \"RetNet\": {\"helped\": 426, \"hurt\": 495, \"net\": -69, \"context_length_p\": 0.012, \"context_length_r\": -0.096, \"unique_tokens_p\": 0.009, \"unique_tokens_r\": -0.099}, \"cross_arch_difference\": \"not_significant\", \"pass_fail\": \"FAIL — RetNet context_unique_tokens p=0.009 passes criterion 1 for one arch only; criterion 2 (cross-arch difference) fails\", \"summary\": \"Surface features do not explain helped/hurt identity. Rules out trivial explanations (frequency, length, diversity). RetNet shows weak context-length signal (p=0.012, r=-0.096).\"}}, {\"id\": \"exp-004\", \"claim\": 3, \"title\": \"Attention weight extraction and visualization\", \"description\": \"Extract attention weight patterns from hybrid models (h3-1 config) for all 3 architectures. Analyze: (a) which positions attention focuses on, (b) whether attention patterns correlate with helped/hurt sample identity, (c) cross-architecture attention pattern similarity.\\n\", \"priority\": \"P0\", \"type\": \"experiment\", \"gpu_budget_hours\": 4, \"deps\": [\"exp-003\"], \"pass_fail\": \"Attention pattern differences documented; correlation with per-example effects > 0.3\", \"note\": \"Upgraded P1→P0: mechanistic evidence is critical for Claim 3 and Reviewer Concern C\", \"status\": \"planned\"}, {\"id\": \"exp-005\", \"claim\": 1, \"title\": \"Architecture expansion check\", \"description\": \"Search Wang et al. model zoo and other sources for additional hybrid architectures (Mamba/Mamba2 hybrids, RWKV hybrids, etc.). If found, evaluate on LAMBADA to test whether convergence generalizes beyond GDN/RetNet/HGRN2.\\n\", \"priority\": \"P1\", \"type\": \"experiment\", \"gpu_budget_hours\": 6, \"deps\": [], \"pass_fail\": \"≥1 additional architecture evaluated and convergence pattern confirmed/denied\", \"status\": \"planned\"}, {\"id\": \"exp-008\", \"registry_id\": \"exp-008\", \"claim\": 1, \"title\": \"Statistical robustness framework\", \"description\": \"Implement bootstrap CIs for convergence metrics. Multi-comparison correction (Bonferroni/FDR) across benchmarks. Sensitivity analysis: does conclusion hold if GDN (with D004 confound) is excluded? Report effect sizes (Cohen's d / η²).\\n\", \"priority\": \"P0\", \"type\": \"analysis\", \"gpu_budget_hours\": 0, \"deps\": [\"exp-001\"], \"pass_fail\": \"All core claims survive with GDN excluded; bootstrap 95% CIs don't cross zero\", \"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"LAMBADA\": {\"rho\": -1, \"raw_p\": 0.0167, \"bonferroni_adj_p\": 0.1, \"bh_fdr_adj_p\": 0.1}, \"HellaSwag\": {\"rho\": 0.3, \"raw_p\": 0.6833, \"bonferroni_adj_p\": 1, \"bh_fdr_adj_p\": 0.82}, \"WinoGrande\": {\"rho\": 0.1, \"raw_p\": 0.95, \"bonferroni_adj_p\": 1, \"bh_fdr_adj_p\": 0.95}, \"ARC-Easy\": {\"rho\": -0.7, \"raw_p\": 0.2333, \"bonferroni_adj_p\": 1, \"bh_fdr_adj_p\": 0.4667}, \"ARC-Challenge\": {\"rho\": 0.6, \"raw_p\": 0.35, \"bonferroni_adj_p\": 1, \"bh_fdr_adj_p\": 0.525}, \"MMLU\": {\"rho\": -0.7, \"raw_p\": 0.2333, \"bonferroni_adj_p\": 1, \"bh_fdr_adj_p\": 0.4667}, \"method\": \"exact_permutation_test_two_tailed\", \"n_permutations\": 120, \"bug_fixed\": \"scipy.stats.spearmanr asymptotic p replaced with exact permutation\", \"bootstrap_ci\": {\"benchmark\": \"LAMBADA\", \"method\": \"architecture_resampling_percentile\", \"ci_lower\": -1, \"ci_upper\": -0.7, \"crosses_zero\": false, \"n_bootstrap\": 10000, \"n_valid\": 8875, \"seed\": 42, \"p_rho_negative\": 1, \"p_rho_positive\": 0, \"bca_note\": \"BCa degenerate at rho=-1.0 boundary; percentile CI used\"}, \"gdn_excluded\": {\"LAMBADA\": {\"rho\": -0.7, \"exact_p\": 0.2333, \"direction\": \"WEAKER\"}, \"HellaSwag\": {\"rho\": 0.5, \"exact_p\": 0.45, \"direction\": \"STRONGER\"}, \"WinoGrande\": {\"rho\": 0.3, \"exact_p\": 0.6833, \"direction\": \"STRONGER\"}, \"ARC-Easy\": {\"rho\": -0.9, \"exact_p\": 0.0833, \"direction\": \"STRONGER\"}, \"ARC-Challenge\": {\"rho\": -0.2, \"exact_p\": 0.7833, \"direction\": \"WEAKER\"}, \"MMLU\": {\"rho\": 0.6, \"exact_p\": 0.35, \"direction\": \"WEAKER\"}, \"note\": \"ARC-Easy rho improves from -0.7 to -0.9 (p=0.0833) without GDN confound — suggestive second anchor\"}}}, {\"id\": \"exp-009\", \"registry_id\": \"exp-009\", \"claim\": 1, \"title\": \"Wang et al. explicit differentiation\", \"description\": \"Formal side-by-side comparison: what Wang et al. report vs our analysis. Extract their exact convergence-related statements. Quantify the increment: (a) they don't compute cross-arch std trajectories, (b) no per-example analysis, (c) no scale-dependent convergence characterization, (d) no mechanistic analysis.\\n\", \"priority\": \"P0\", \"type\": \"analysis\", \"gpu_budget_hours\": 0, \"deps\": [], \"data_source\": \"Wang et al. arXiv 2507.06457\", \"pass_fail\": \"Clear 4-point differentiation documented\", \"status\": \"DONE\", \"conclusion\": \"success\"}, {\"id\": \"exp-010\", \"registry_id\": \"exp-010\", \"claim\": 3, \"title\": \"Convergence-divergence bridge analysis\", \"description\": \"For LAMBADA, plot aggregate convergence curve alongside per-example divergence metrics (Jaccard, net effect asymmetry) as function of attention ratio. Show that convergence and divergence co-evolve—more attention = more aggregate convergence BUT also more architecture-specific per-example effects. Core visualization for Claim 3 (underspecification in hybrid architectures).\\n\", \"priority\": \"P0\", \"type\": \"analysis\", \"gpu_budget_hours\": 0, \"deps\": [\"exp-001\", \"exp-003\"], \"pass_fail\": \"Convergence-divergence co-evolution demonstrated with significant correlation\", \"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"aggregate_convergence\": {\"std_pure\": 0.024, \"std_h24_1\": 0.0162, \"std_h12_1\": 0.0136, \"std_h6_1\": 0.0061, \"std_h3_1\": 0.0049, \"reduction_ratio\": 0.8, \"note\": \"Cross-arch std drops 5x monotonically\"}, \"per_example_divergence\": {\"jaccard_helped_range\": [0.092, 0.1], \"jaccard_hurt_range\": [0.081, 0.099], \"net_asymmetry_range\": [0.013, 0.04], \"net_asymmetry_trend\": \"increasing with attention ratio\", \"note\": \"Jaccard saturates at ~0.095 by 4% attention (h24-1), flat thereafter\"}, \"co_evolution_spearman\": {\"std_vs_J_helped\": {\"rho\": -0.7, \"exact_p\": 0.23}, \"std_vs_J_hurt\": {\"rho\": -0.8, \"exact_p\": 0.13}, \"CAVEAT\": \"D008: rho inflated by pure=0 degeneracy (Jaccard=NaN->0). Excluding pure: rho=-0.40, p=0.75. NOT co-evolution.\"}, \"key_finding\": \"DECOUPLING (D008): minimal attention (4%) creates per-example specificity (Jaccard saturates ~0.095), gradual attention drives aggregate convergence (sigma 0.024->0.005). Two processes operate on different timescales. Net asymmetry INCREASES (0.013->0.040).\", \"narrative_constraints\": \"PROHIBITED: co-evolution, paradoxical coexistence, paradox. USE: decoupling, different timescales.\"}}, {\"id\": \"exp-011\", \"registry_id\": \"exp-011\", \"claim\": 1, \"title\": \"Additional high-retrieval benchmarks (Dream W1 response)\", \"description\": \"Dream review: LAMBADA alone does not survive Bonferroni (p=0.017 > α=0.0083). Need a second significant anchor point on a high-retrieval task. Run 1.3B models on additional retrieval-heavy benchmarks available in lm-eval: (a) StoryCloze (context completion, structurally similar to LAMBADA), (b) BoolQ (passage-based yes/no, context retrieval), (c) COPA (causal reasoning from short narratives). Compute cross-arch std at each attention ratio for each benchmark. Test for convergence (Spearman + exact permutation, two-tailed). If ANY shows significant convergence → second anchor established, W1 substantially mitigated.\\n\", \"priority\": \"P0\", \"type\": \"experiment\", \"gpu_budget_hours\": 8, \"deps\": [], \"pass_fail\": \"≥1 additional benchmark shows significant convergence (p<0.05 two-tailed)\", \"note\": \"CRITICAL for Findings acceptance. Dream best case = 2.5 without this. Added post-D006.\", \"status\": \"DONE\", \"conclusion\": \"negative\", \"metrics\": {\"boolq\": {\"rho\": 0.2, \"raw_p\": 0.7833, \"bonferroni_adj_p_9\": 1, \"std_pure\": 0.0163, \"std_h3_1\": 0.0236, \"convergence\": false}, \"piqa\": {\"rho\": -0.5, \"raw_p\": 0.45, \"bonferroni_adj_p_9\": 1, \"std_pure\": 0.0054, \"std_h3_1\": 0.0034, \"convergence\": false}, \"sciq\": {\"rho\": 0.1, \"raw_p\": 0.95, \"bonferroni_adj_p_9\": 1, \"std_pure\": 0.0087, \"std_h3_1\": 0.0074, \"convergence\": false}, \"copa_supplementary\": {\"rho\": -0.67, \"raw_p\": 0.2667, \"std_pure\": 0.0262, \"std_h3_1\": 0.0047, \"convergence_ratio\": 5.57, \"note\": \"supplementary only (n=100), not in main Bonferroni\"}, \"LAMBADA_recomputed\": {\"rho\": -1, \"raw_p\": 0.0167, \"bonferroni_adj_p_6\": 0.1, \"bonferroni_adj_p_10\": 0.167, \"note\": \"6-Bonf=0.100 (D003 pre-registered); 10-Bonf=0.167; does not survive strict Bonferroni\"}, \"merged_10benchmark_significant_count\": \"0/10\", \"method\": \"exact_permutation_test_two_tailed\", \"D009_strategy\": \"BCa CI [-1.0,-0.7] as primary evidence; 6-Bonf adj_p=0.100 reported honestly; 10-benchmark negative -> task-specificity positive evidence (supplementary); underpowered caveat in Limitations\", \"D009_prohibited\": \"NO post-hoc 2-benchmark Bonferroni; NO post-hoc rho<0 subset correction\", \"conclusion\": \"No second anchor. Convergence LAMBADA-specific. W1 addressed via task-specificity reframing (D009).\"}}], \"total\": 11}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "896921bc-cafe-4244-9aaa-456b26890548",
  "isSidechain": false,
  "promptId": "53afff33-bebc-42c8-b6ca-8baf6ae2df0c",
  "type": "user",
  "uuid": "781de150-f0e9-459b-a828-8ad9f92f7e9c",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": [{\\\"id\\\": \\\"exp-001\\\", \\\"registry_id\\\": \\\"exp-001\\\", \\\"claim\\\": 1, \\\"title\\\": \\\"Task-specificity characterization of equalizer effect\\\", \\\"description\\\": \\\"Compute cross-architecture variance (std) at each attention ratio for all 6 benchmarks. Known: only LAMBADA shows significant convergence (p<0.05). Goal: build principled task taxonomy (retrieval-dependent vs reasoning-dependent) explaining WHY convergence is task-specific. LAMBADA = last-word retrieval from context; HellaSwag/ARC = multi-step reasoning. Show the dichotomy is a feature (task-type modulation), not a limitation.\\\\n\\\", \\\"priority\\\": \\\"P0\\\", \\\"type\\\": \\\"analysis\\\", \\\"gpu_budget_hours\\\": 0, \\\"deps\\\": [], \\\"data_source\\\": \\\"existing summary_all_1.3b.csv + 340M results + cross_scale_convergence output\\\", \\\"pass_fail\\\": \\\"Clear task-type dichotomy with principled taxonomy; convergence correlates with retrieval demand\\\", \\\"reviewer_risk\\\": \\\"Risk A — reframed per Reviewer warning: single-task convergence → task-specificity as positive finding\\\", \\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"LAMBADA\\\": {\\\"rho\\\": -1, \\\"p\\\": 0.0167, \\\"significant\\\": false, \\\"taxonomy\\\": \\\"retrieval-dependent\\\", \\\"note\\\": \\\"exact permutation two-tailed (was 0.008 one-tailed)\\\"}, \\\"HellaSwag\\\": {\\\"rho\\\": 0.3, \\\"p\\\": 0.6833, \\\"significant\\\": false, \\\"taxonomy\\\": \\\"reasoning-dependent\\\"}, \\\"ARC-C\\\": {\\\"rho\\\": 0.6, \\\"p\\\": 0.35, \\\"significant\\\": false, \\\"taxonomy\\\": \\\"reasoning-dependent\\\"}, \\\"Winogrande\\\": {\\\"rho\\\": 0.1, \\\"p\\\": 0.95, \\\"significant\\\": false, \\\"taxonomy\\\": \\\"reasoning-dependent\\\"}, \\\"ARC-Easy\\\": {\\\"rho\\\": -0.7, \\\"p\\\": 0.2333, \\\"significant\\\": false, \\\"taxonomy\\\": \\\"mixed\\\"}, \\\"MMLU\\\": {\\\"rho\\\": -0.7, \\\"p\\\": 0.2333, \\\"significant\\\": false, \\\"taxonomy\\\": \\\"mixed\\\"}, \\\"significant_count\\\": \\\"0/6\\\", \\\"summary\\\": \\\"LAMBADA shows perfect negative correlation (rho=-1.0) but exact permutation two-tailed p=0.0167 (Bonferroni adj-p=0.100, not significant). Reasoning tasks show no convergence. Mixed tasks suggestive but underpowered (n=5).\\\", \\\"method\\\": \\\"exact_permutation_test_two_tailed\\\"}}, {\\\"id\\\": \\\"exp-002\\\", \\\"claim\\\": 1, \\\"title\\\": \\\"Multi-benchmark per-example analysis (task-specificity validation)\\\", \\\"description\\\": \\\"Re-run lm-eval on 1.3B models with --log_samples for HellaSwag, ARC-easy, ARC-challenge. Two goals: (a) confirm task-specificity — per-example convergence absent on reasoning tasks, (b) characterize HOW attention affects per-example behavior on non-converging tasks (random noise vs systematic but architecture-specific). Strengthens Claim 1 regardless of outcome.\\\\n\\\", \\\"priority\\\": \\\"cancelled\\\", \\\"type\\\": \\\"experiment\\\", \\\"gpu_budget_hours\\\": 0, \\\"deps\\\": [\\\"exp-001\\\"], \\\"pass_fail\\\": \\\"Per-example data collected for ≥3 benchmarks; task-specificity of per-example mechanism confirmed or refuted\\\", \\\"reviewer_risk\\\": \\\"Risk B — outcome determines Claim 1 scope: cross-task vs retrieval-specific equalizer\\\", \\\"note\\\": \\\"CANCELLED (D010, 2026-05-19): Expected value negative after D009 task-specificity reframing. Most likely outcome (non-LAMBADA also low Jaccard) would weaken task-specificity narrative. 20h GPU reallocated to exp-007 + buffer.\\\", \\\"status\\\": \\\"planned\\\"}, {\\\"id\\\": \\\"exp-006\\\", \\\"claim\\\": 2, \\\"title\\\": \\\"7B model evaluation — CANCELLED (unavailable)\\\", \\\"description\\\": \\\"Wang et al. only have 340M + 1.3B (72 models total). Paper Limitations explicitly excludes 10B+. No 7B models exist. Budget reallocated to exp-002/004/005.\\\\n\\\", \\\"priority\\\": \\\"cancelled\\\", \\\"type\\\": \\\"experiment\\\", \\\"gpu_budget_hours\\\": 0, \\\"deps\\\": [], \\\"pass_fail\\\": \\\"N/A — 7B unavailable, confirmed 2026-05-19\\\", \\\"status\\\": \\\"planned\\\"}, {\\\"id\\\": \\\"exp-007\\\", \\\"claim\\\": 2, \\\"title\\\": \\\"340M rebound mechanism analysis (upgraded: compensate 7B absence)\\\", \\\"description\\\": \\\"Deep analysis of 340M non-monotonic rebound at attn=8. Per-example comparison with 1.3B at same attention ratio to identify which samples diverge. Characterize rebound samples. With 7B unavailable, this becomes the primary vehicle for Claim 2 depth — show the binary contrast (340M partial vs 1.3B complete) has mechanistic explanation, not just correlation with scale. Analyze training token count (20B vs 100B) as confound vs scale.\\\\n\\\", \\\"priority\\\": \\\"P0\\\", \\\"type\\\": \\\"analysis\\\", \\\"gpu_budget_hours\\\": 2, \\\"deps\\\": [], \\\"data_source\\\": \\\"existing 340M + 1.3B LAMBADA per-example logprob data (if available from MVP); else rerun 340M with --log_samples\\\", \\\"pass_fail\\\": \\\"Rebound mechanism identified with principled explanation; 340M vs 1.3B contrast characterized beyond aggregate metrics\\\", \\\"note\\\": \\\"Upgraded from P1 to P0 after 7B cancellation. May need 340M per-example rerun (2h GPU).\\\", \\\"status\\\": \\\"planned\\\"}, {\\\"id\\\": \\\"exp-003\\\", \\\"registry_id\\\": \\\"exp-003\\\", \\\"claim\\\": 3, \\\"title\\\": \\\"Helped/hurt sample characterization\\\", \\\"description\\\": \\\"For each architecture's helped/hurt samples on LAMBADA, compute: (a) target token frequency (unigram rank in training data proxy), (b) context length (token count), (c) last-sentence complexity (perplexity under baseline), (d) topic/domain distribution. Test whether architecture-specific sample subsets differ on these features.\\\\n\\\", \\\"priority\\\": \\\"P0\\\", \\\"type\\\": \\\"analysis\\\", \\\"gpu_budget_hours\\\": 1, \\\"deps\\\": [], \\\"data_source\\\": \\\"existing lambada per-example logprob data\\\", \\\"pass_fail\\\": \\\"≥1 feature significantly differentiates helped vs hurt samples (p<0.01), AND features differ across architectures\\\", \\\"status_note\\\": \\\"Phase 1 (surface features) DONE: all non-significant within-arch (p>0.2). Phase 2 (perplexity) DONE: within-arch perplexity also non-significant (r_rb≈-0.04, p>0.2). PASS on second criterion: cross-arch KW significant (hurt p=0.0005, helped p=0.020). Different archs help/hurt samples with systematically different baseline difficulty profiles. Both negative within-arch results are informative (rules out trivial explanations). Cross-arch finding strengthens Claim 3 (architecture-specificity is structured, not random).\\\\n\\\", \\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\", \\\"metrics\\\": {\\\"GDN\\\": {\\\"helped\\\": 462, \\\"hurt\\\": 615, \\\"net\\\": -153, \\\"surface_features_significant\\\": false}, \\\"HGRN2\\\": {\\\"helped\\\": 548, \\\"hurt\\\": 395, \\\"net\\\": 153, \\\"surface_features_significant\\\": false}, \\\"RetNet\\\": {\\\"helped\\\": 426, \\\"hurt\\\": 495, \\\"net\\\": -69, \\\"context_length_p\\\": 0.012, \\\"context_length_r\\\": -0.096, \\\"unique_tokens_p\\\": 0.009, \\\"unique_tokens_r\\\": -0.099}, \\\"cross_arch_difference\\\": \\\"not_significant\\\", \\\"pass_fail\\\": \\\"FAIL — RetNet context_unique_tokens p=0.009 passes criterion 1 for one arch only; criterion 2 (cross-arch difference) fails\\\", \\\"summary\\\": \\\"Surface features do not explain helped/hurt identity. Rules out trivial explanations (frequency, length, diversity). RetNet shows weak context-length signal (p=0.012, r=-0.096).\\\"}}, {\\\"id\\\": \\\"exp-004\\\", \\\"claim\\\": 3, \\\"title\\\": \\\"Attention weight extraction and visualization\\\", \\\"description\\\": \\\"Extract attention weight patterns from hybrid models (h3-1 config) for all 3 architectures. Analyze: (a) which positions attention focuses on, (b) whether attention patterns correlate with helped/hurt sample identity, (c) cross-architecture attention pattern similarity.\\\\n\\\", \\\"priority\\\": \\\"P0\\\", \\\"type\\\": \\\"experiment\\\", \\\"gpu_budget_hours\\\": 4, \\\"deps\\\": [\\\"exp-003\\\"], \\\"pass_fail\\\": \\\"Attention pattern differences documented; correlation with per-example effects > 0.3\\\", \\\"note\\\": \\\"Upgraded P1→P0: mechanistic evidence is critical for Claim 3 and Reviewer Concern C\\\", \\\"status\\\": \\\"planned\\\"}, {\\\"id\\\": \\\"exp-005\\\", \\\"claim\\\": 1, \\\"title\\\": \\\"Architecture expansion check\\\", \\\"description\\\": \\\"Search Wang et al. model zoo and other sources for additional hybrid architectures (Mamba/Mamba2 hybrids, RWKV hybrids, etc.). If found, evaluate on LAMBADA to test whether convergence generalizes beyond GDN/RetNet/HGRN2.\\\\n\\\", \\\"priority\\\": \\\"P1\\\", \\\"type\\\": \\\"experiment\\\", \\\"gpu_budget_hours\\\": 6, \\\"deps\\\": [], \\\"pass_fail\\\": \\\"≥1 additional architecture evaluated and convergence pattern confirmed/denied\\\", \\\"status\\\": \\\"planned\\\"}, {\\\"id\\\": \\\"exp-008\\\", \\\"registry_id\\\": \\\"exp-008\\\", \\\"claim\\\": 1, \\\"title\\\": \\\"Statistical robustness framework\\\", \\\"description\\\": \\\"Implement bootstrap CIs for convergence metrics. Multi-comparison correction (Bonferroni/FDR) across benchmarks. Sensitivity analysis: does conclusion hold if GDN (with D004 confound) is excluded? Report effect sizes (Cohen's d / η²).\\\\n\\\", \\\"priority\\\": \\\"P0\\\", \\\"type\\\": \\\"analysis\\\", \\\"gpu_budget_hours\\\": 0, \\\"deps\\\": [\\\"exp-001\\\"], \\\"pass_fail\\\": \\\"All core claims survive with GDN excluded; bootstrap 95% CIs don't cross zero\\\", \\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"LAMBADA\\\": {\\\"rho\\\": -1, \\\"raw_p\\\": 0.0167, \\\"bonferroni_adj_p\\\": 0.1, \\\"bh_fdr_adj_p\\\": 0.1}, \\\"HellaSwag\\\": {\\\"rho\\\": 0.3, \\\"raw_p\\\": 0.6833, \\\"bonferroni_adj_p\\\": 1, \\\"bh_fdr_adj_p\\\": 0.82}, \\\"WinoGrande\\\": {\\\"rho\\\": 0.1, \\\"raw_p\\\": 0.95, \\\"bonferroni_adj_p\\\": 1, \\\"bh_fdr_adj_p\\\": 0.95}, \\\"ARC-Easy\\\": {\\\"rho\\\": -0.7, \\\"raw_p\\\": 0.2333, \\\"bonferroni_adj_p\\\": 1, \\\"bh_fdr_adj_p\\\": 0.4667}, \\\"ARC-Challenge\\\": {\\\"rho\\\": 0.6, \\\"raw_p\\\": 0.35, \\\"bonferroni_adj_p\\\": 1, \\\"bh_fdr_adj_p\\\": 0.525}, \\\"MMLU\\\": {\\\"rho\\\": -0.7, \\\"raw_p\\\": 0.2333, \\\"bonferroni_adj_p\\\": 1, \\\"bh_fdr_adj_p\\\": 0.4667}, \\\"method\\\": \\\"exact_permutation_test_two_tailed\\\", \\\"n_permutations\\\": 120, \\\"bug_fixed\\\": \\\"scipy.stats.spearmanr asymptotic p replaced with exact permutation\\\", \\\"bootstrap_ci\\\": {\\\"benchmark\\\": \\\"LAMBADA\\\", \\\"method\\\": \\\"architecture_resampling_percentile\\\", \\\"ci_lower\\\": -1, \\\"ci_upper\\\": -0.7, \\\"crosses_zero\\\": false, \\\"n_bootstrap\\\": 10000, \\\"n_valid\\\": 8875, \\\"seed\\\": 42, \\\"p_rho_negative\\\": 1, \\\"p_rho_positive\\\": 0, \\\"bca_note\\\": \\\"BCa degenerate at rho=-1.0 boundary; percentile CI used\\\"}, \\\"gdn_excluded\\\": {\\\"LAMBADA\\\": {\\\"rho\\\": -0.7, \\\"exact_p\\\": 0.2333, \\\"direction\\\": \\\"WEAKER\\\"}, \\\"HellaSwag\\\": {\\\"rho\\\": 0.5, \\\"exact_p\\\": 0.45, \\\"direction\\\": \\\"STRONGER\\\"}, \\\"WinoGrande\\\": {\\\"rho\\\": 0.3, \\\"exact_p\\\": 0.6833, \\\"direction\\\": \\\"STRONGER\\\"}, \\\"ARC-Easy\\\": {\\\"rho\\\": -0.9, \\\"exact_p\\\": 0.0833, \\\"direction\\\": \\\"STRONGER\\\"}, \\\"ARC-Challenge\\\": {\\\"rho\\\": -0.2, \\\"exact_p\\\": 0.7833, \\\"direction\\\": \\\"WEAKER\\\"}, \\\"MMLU\\\": {\\\"rho\\\": 0.6, \\\"exact_p\\\": 0.35, \\\"direction\\\": \\\"WEAKER\\\"}, \\\"note\\\": \\\"ARC-Easy rho improves from -0.7 to -0.9 (p=0.0833) without GDN confound — suggestive second anchor\\\"}}}, {\\\"id\\\": \\\"exp-009\\\", \\\"registry_id\\\": \\\"exp-009\\\", \\\"claim\\\": 1, \\\"title\\\": \\\"Wang et al. explicit differentiation\\\", \\\"description\\\": \\\"Formal side-by-side comparison: what Wang et al. report vs our analysis. Extract their exact convergence-related statements. Quantify the increment: (a) they don't compute cross-arch std trajectories, (b) no per-example analysis, (c) no scale-dependent convergence characterization, (d) no mechanistic analysis.\\\\n\\\", \\\"priority\\\": \\\"P0\\\", \\\"type\\\": \\\"analysis\\\", \\\"gpu_budget_hours\\\": 0, \\\"deps\\\": [], \\\"data_source\\\": \\\"Wang et al. arXiv 2507.06457\\\", \\\"pass_fail\\\": \\\"Clear 4-point differentiation documented\\\", \\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, {\\\"id\\\": \\\"exp-010\\\", \\\"registry_id\\\": \\\"exp-010\\\", \\\"claim\\\": 3, \\\"title\\\": \\\"Convergence-divergence bridge analysis\\\", \\\"description\\\": \\\"For LAMBADA, plot aggregate convergence curve alongside per-example divergence metrics (Jaccard, net effect asymmetry) as function of attention ratio. Show that convergence and divergence co-evolve—more attention = more aggregate convergence BUT also more architecture-specific per-example effects. Core visualization for Claim 3 (underspecification in hybrid architectures).\\\\n\\\", \\\"priority\\\": \\\"P0\\\", \\\"type\\\": \\\"analysis\\\", \\\"gpu_budget_hours\\\": 0, \\\"deps\\\": [\\\"exp-001\\\", \\\"exp-003\\\"], \\\"pass_fail\\\": \\\"Convergence-divergence co-evolution demonstrated with significant correlation\\\", \\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"aggregate_convergence\\\": {\\\"std_pure\\\": 0.024, \\\"std_h24_1\\\": 0.0162, \\\"std_h12_1\\\": 0.0136, \\\"std_h6_1\\\": 0.0061, \\\"std_h3_1\\\": 0.0049, \\\"reduction_ratio\\\": 0.8, \\\"note\\\": \\\"Cross-arch std drops 5x monotonically\\\"}, \\\"per_example_divergence\\\": {\\\"jaccard_helped_range\\\": [0.092, 0.1], \\\"jaccard_hurt_range\\\": [0.081, 0.099], \\\"net_asymmetry_range\\\": [0.013, 0.04], \\\"net_asymmetry_trend\\\": \\\"increasing with attention ratio\\\", \\\"note\\\": \\\"Jaccard saturates at ~0.095 by 4% attention (h24-1), flat thereafter\\\"}, \\\"co_evolution_spearman\\\": {\\\"std_vs_J_helped\\\": {\\\"rho\\\": -0.7, \\\"exact_p\\\": 0.23}, \\\"std_vs_J_hurt\\\": {\\\"rho\\\": -0.8, \\\"exact_p\\\": 0.13}, \\\"CAVEAT\\\": \\\"D008: rho inflated by pure=0 degeneracy (Jaccard=NaN->0). Excluding pure: rho=-0.40, p=0.75. NOT co-evolution.\\\"}, \\\"key_finding\\\": \\\"DECOUPLING (D008): minimal attention (4%) creates per-example specificity (Jaccard saturates ~0.095), gradual attention drives aggregate convergence (sigma 0.024->0.005). Two processes operate on different timescales. Net asymmetry INCREASES (0.013->0.040).\\\", \\\"narrative_constraints\\\": \\\"PROHIBITED: co-evolution, paradoxical coexistence, paradox. USE: decoupling, different timescales.\\\"}}, {\\\"id\\\": \\\"exp-011\\\", \\\"registry_id\\\": \\\"exp-011\\\", \\\"claim\\\": 1, \\\"title\\\": \\\"Additional high-retrieval benchmarks (Dream W1 response)\\\", \\\"description\\\": \\\"Dream review: LAMBADA alone does not survive Bonferroni (p=0.017 > α=0.0083). Need a second significant anchor point on a high-retrieval task. Run 1.3B models on additional retrieval-heavy benchmarks available in lm-eval: (a) StoryCloze (context completion, structurally similar to LAMBADA), (b) BoolQ (passage-based yes/no, context retrieval), (c) COPA (causal reasoning from short narratives). Compute cross-arch std at each attention ratio for each benchmark. Test for convergence (Spearman + exact permutation, two-tailed). If ANY shows significant convergence → second anchor established, W1 substantially mitigated.\\\\n\\\", \\\"priority\\\": \\\"P0\\\", \\\"type\\\": \\\"experiment\\\", \\\"gpu_budget_hours\\\": 8, \\\"deps\\\": [], \\\"pass_fail\\\": \\\"≥1 additional benchmark shows significant convergence (p<0.05 two-tailed)\\\", \\\"note\\\": \\\"CRITICAL for Findings acceptance. Dream best case = 2.5 without this. Added post-D006.\\\", \\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\", \\\"metrics\\\": {\\\"boolq\\\": {\\\"rho\\\": 0.2, \\\"raw_p\\\": 0.7833, \\\"bonferroni_adj_p_9\\\": 1, \\\"std_pure\\\": 0.0163, \\\"std_h3_1\\\": 0.0236, \\\"convergence\\\": false}, \\\"piqa\\\": {\\\"rho\\\": -0.5, \\\"raw_p\\\": 0.45, \\\"bonferroni_adj_p_9\\\": 1, \\\"std_pure\\\": 0.0054, \\\"std_h3_1\\\": 0.0034, \\\"convergence\\\": false}, \\\"sciq\\\": {\\\"rho\\\": 0.1, \\\"raw_p\\\": 0.95, \\\"bonferroni_adj_p_9\\\": 1, \\\"std_pure\\\": 0.0087, \\\"std_h3_1\\\": 0.0074, \\\"convergence\\\": false}, \\\"copa_supplementary\\\": {\\\"rho\\\": -0.67, \\\"raw_p\\\": 0.2667, \\\"std_pure\\\": 0.0262, \\\"std_h3_1\\\": 0.0047, \\\"convergence_ratio\\\": 5.57, \\\"note\\\": \\\"supplementary only (n=100), not in main Bonferroni\\\"}, \\\"LAMBADA_recomputed\\\": {\\\"rho\\\": -1, \\\"raw_p\\\": 0.0167, \\\"bonferroni_adj_p_6\\\": 0.1, \\\"bonferroni_adj_p_10\\\": 0.167, \\\"note\\\": \\\"6-Bonf=0.100 (D003 pre-registered); 10-Bonf=0.167; does not survive strict Bonferroni\\\"}, \\\"merged_10benchmark_significant_count\\\": \\\"0/10\\\", \\\"method\\\": \\\"exact_permutation_test_two_tailed\\\", \\\"D009_strategy\\\": \\\"BCa CI [-1.0,-0.7] as primary evidence; 6-Bonf adj_p=0.100 reported honestly; 10-benchmark negative -> task-specificity positive evidence (supplementary); underpowered caveat in Limitations\\\", \\\"D009_prohibited\\\": \\\"NO post-hoc 2-benchmark Bonferroni; NO post-hoc rho<0 subset correction\\\", \\\"conclusion\\\": \\\"No second anchor. Convergence LAMBADA-specific. W1 addressed via task-specificity reframing (D009).\\\"}}], \\\"total\\\": 11}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": [{\"id\": \"exp-001\", \"registry_id\": \"exp-001\", \"claim\": 1, \"title\": \"Task-specificity characterization of equalizer effect\", \"description\": \"Compute cross-architecture variance (std) at each attention ratio for all 6 benchmarks. Known: only LAMBADA shows significant convergence (p<0.05). Goal: build principled task taxonomy (retrieval-dependent vs reasoning-dependent) explaining WHY convergence is task-specific. LAMBADA = last-word retrieval from context; HellaSwag/ARC = multi-step reasoning. Show the dichotomy is a feature (task-type modulation), not a limitation.\\n\", \"priority\": \"P0\", \"type\": \"analysis\", \"gpu_budget_hours\": 0, \"deps\": [], \"data_source\": \"existing summary_all_1.3b.csv + 340M results + cross_scale_convergence output\", \"pass_fail\": \"Clear task-type dichotomy with principled taxonomy; convergence correlates with retrieval demand\", \"reviewer_risk\": \"Risk A — reframed per Reviewer warning: single-task convergence → task-specificity as positive finding\", \"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"LAMBADA\": {\"rho\": -1, \"p\": 0.0167, \"significant\": false, \"taxonomy\": \"retrieval-dependent\", \"note\": \"exact permutation two-tailed (was 0.008 one-tailed)\"}, \"HellaSwag\": {\"rho\": 0.3, \"p\": 0.6833, \"significant\": false, \"taxonomy\": \"reasoning-dependent\"}, \"ARC-C\": {\"rho\": 0.6, \"p\": 0.35, \"significant\": false, \"taxonomy\": \"reasoning-dependent\"}, \"Winogrande\": {\"rho\": 0.1, \"p\": 0.95, \"significant\": false, \"taxonomy\": \"reasoning-dependent\"}, \"ARC-Easy\": {\"rho\": -0.7, \"p\": 0.2333, \"significant\": false, \"taxonomy\": \"mixed\"}, \"MMLU\": {\"rho\": -0.7, \"p\": 0.2333, \"significant\": false, \"taxonomy\": \"mixed\"}, \"significant_count\": \"0/6\", \"summary\": \"LAMBADA shows perfect negative correlation (rho=-1.0) but exact permutation two-tailed p=0.0167 (Bonferroni adj-p=0.100, not significant). Reasoning tasks show no convergence. Mixed tasks suggestive but underpowered (n=5).\", \"method\": \"exact_permutation_test_two_tailed\"}}, {\"id\": \"exp-002\", \"claim\": 1, \"title\": \"Multi-benchmark per-example analysis (task-specificity validation)\", \"description\": \"Re-run lm-eval on 1.3B models with --log_samples for HellaSwag, ARC-easy, ARC-challenge. Two goals: (a) confirm task-specificity — per-example convergence absent on reasoning tasks, (b) characterize HOW attention affects per-example behavior on non-converging tasks (random noise vs systematic but architecture-specific). Strengthens Claim 1 regardless of outcome.\\n\", \"priority\": \"cancelled\", \"type\": \"experiment\", \"gpu_budget_hours\": 0, \"deps\": [\"exp-001\"], \"pass_fail\": \"Per-example data collected for ≥3 benchmarks; task-specificity of per-example mechanism confirmed or refuted\", \"reviewer_risk\": \"Risk B — outcome determines Claim 1 scope: cross-task vs retrieval-specific equalizer\", \"note\": \"CANCELLED (D010, 2026-05-19): Expected value negative after D009 task-specificity reframing. Most likely outcome (non-LAMBADA also low Jaccard) would weaken task-specificity narrative. 20h GPU reallocated to exp-007 + buffer.\", \"status\": \"planned\"}, {\"id\": \"exp-006\", \"claim\": 2, \"title\": \"7B model evaluation — CANCELLED (unavailable)\", \"description\": \"Wang et al. only have 340M + 1.3B (72 models total). Paper Limitations explicitly excludes 10B+. No 7B models exist. Budget reallocated to exp-002/004/005.\\n\", \"priority\": \"cancelled\", \"type\": \"experiment\", \"gpu_budget_hours\": 0, \"deps\": [], \"pass_fail\": \"N/A — 7B unavailable, confirmed 2026-05-19\", \"status\": \"planned\"}, {\"id\": \"exp-007\", \"claim\": 2, \"title\": \"340M rebound mechanism analysis (upgraded: compensate 7B absence)\", \"description\": \"Deep analysis of 340M non-monotonic rebound at attn=8. Per-example comparison with 1.3B at same attention ratio to identify which samples diverge. Characterize rebound samples. With 7B unavailable, this becomes the primary vehicle for Claim 2 depth — show the binary contrast (340M partial vs 1.3B complete) has mechanistic explanation, not just correlation with scale. Analyze training token count (20B vs 100B) as confound vs scale.\\n\", \"priority\": \"P0\", \"type\": \"analysis\", \"gpu_budget_hours\": 2, \"deps\": [], \"data_source\": \"existing 340M + 1.3B LAMBADA per-example logprob data (if available from MVP); else rerun 340M with --log_samples\", \"pass_fail\": \"Rebound mechanism identified with principled explanation; 340M vs 1.3B contrast characterized beyond aggregate metrics\", \"note\": \"Upgraded from P1 to P0 after 7B cancellation. May need 340M per-example rerun (2h GPU).\", \"status\": \"planned\"}, {\"id\": \"exp-003\", \"registry_id\": \"exp-003\", \"claim\": 3, \"title\": \"Helped/hurt sample characterization\", \"description\": \"For each architecture's helped/hurt samples on LAMBADA, compute: (a) target token frequency (unigram rank in training data proxy), (b) context length (token count), (c) last-sentence complexity (perplexity under baseline), (d) topic/domain distribution. Test whether architecture-specific sample subsets differ on these features.\\n\", \"priority\": \"P0\", \"type\": \"analysis\", \"gpu_budget_hours\": 1, \"deps\": [], \"data_source\": \"existing lambada per-example logprob data\", \"pass_fail\": \"≥1 feature significantly differentiates helped vs hurt samples (p<0.01), AND features differ across architectures\", \"status_note\": \"Phase 1 (surface features) DONE: all non-significant within-arch (p>0.2). Phase 2 (perplexity) DONE: within-arch perplexity also non-significant (r_rb≈-0.04, p>0.2). PASS on second criterion: cross-arch KW significant (hurt p=0.0005, helped p=0.020). Different archs help/hurt samples with systematically different baseline difficulty profiles. Both negative within-arch results are informative (rules out trivial explanations). Cross-arch finding strengthens Claim 3 (architecture-specificity is structured, not random).\\n\", \"status\": \"DONE\", \"conclusion\": \"negative\", \"metrics\": {\"GDN\": {\"helped\": 462, \"hurt\": 615, \"net\": -153, \"surface_features_significant\": false}, \"HGRN2\": {\"helped\": 548, \"hurt\": 395, \"net\": 153, \"surface_features_significant\": false}, \"RetNet\": {\"helped\": 426, \"hurt\": 495, \"net\": -69, \"context_length_p\": 0.012, \"context_length_r\": -0.096, \"unique_tokens_p\": 0.009, \"unique_tokens_r\": -0.099}, \"cross_arch_difference\": \"not_significant\", \"pass_fail\": \"FAIL — RetNet context_unique_tokens p=0.009 passes criterion 1 for one arch only; criterion 2 (cross-arch difference) fails\", \"summary\": \"Surface features do not explain helped/hurt identity. Rules out trivial explanations (frequency, length, diversity). RetNet shows weak context-length signal (p=0.012, r=-0.096).\"}}, {\"id\": \"exp-004\", \"claim\": 3, \"title\": \"Attention weight extraction and visualization\", \"description\": \"Extract attention weight patterns from hybrid models (h3-1 config) for all 3 architectures. Analyze: (a) which positions attention focuses on, (b) whether attention patterns correlate with helped/hurt sample identity, (c) cross-architecture attention pattern similarity.\\n\", \"priority\": \"P0\", \"type\": \"experiment\", \"gpu_budget_hours\": 4, \"deps\": [\"exp-003\"], \"pass_fail\": \"Attention pattern differences documented; correlation with per-example effects > 0.3\", \"note\": \"Upgraded P1→P0: mechanistic evidence is critical for Claim 3 and Reviewer Concern C\", \"status\": \"planned\"}, {\"id\": \"exp-005\", \"claim\": 1, \"title\": \"Architecture expansion check\", \"description\": \"Search Wang et al. model zoo and other sources for additional hybrid architectures (Mamba/Mamba2 hybrids, RWKV hybrids, etc.). If found, evaluate on LAMBADA to test whether convergence generalizes beyond GDN/RetNet/HGRN2.\\n\", \"priority\": \"P1\", \"type\": \"experiment\", \"gpu_budget_hours\": 6, \"deps\": [], \"pass_fail\": \"≥1 additional architecture evaluated and convergence pattern confirmed/denied\", \"status\": \"planned\"}, {\"id\": \"exp-008\", \"registry_id\": \"exp-008\", \"claim\": 1, \"title\": \"Statistical robustness framework\", \"description\": \"Implement bootstrap CIs for convergence metrics. Multi-comparison correction (Bonferroni/FDR) across benchmarks. Sensitivity analysis: does conclusion hold if GDN (with D004 confound) is excluded? Report effect sizes (Cohen's d / η²).\\n\", \"priority\": \"P0\", \"type\": \"analysis\", \"gpu_budget_hours\": 0, \"deps\": [\"exp-001\"], \"pass_fail\": \"All core claims survive with GDN excluded; bootstrap 95% CIs don't cross zero\", \"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"LAMBADA\": {\"rho\": -1, \"raw_p\": 0.0167, \"bonferroni_adj_p\": 0.1, \"bh_fdr_adj_p\": 0.1}, \"HellaSwag\": {\"rho\": 0.3, \"raw_p\": 0.6833, \"bonferroni_adj_p\": 1, \"bh_fdr_adj_p\": 0.82}, \"WinoGrande\": {\"rho\": 0.1, \"raw_p\": 0.95, \"bonferroni_adj_p\": 1, \"bh_fdr_adj_p\": 0.95}, \"ARC-Easy\": {\"rho\": -0.7, \"raw_p\": 0.2333, \"bonferroni_adj_p\": 1, \"bh_fdr_adj_p\": 0.4667}, \"ARC-Challenge\": {\"rho\": 0.6, \"raw_p\": 0.35, \"bonferroni_adj_p\": 1, \"bh_fdr_adj_p\": 0.525}, \"MMLU\": {\"rho\": -0.7, \"raw_p\": 0.2333, \"bonferroni_adj_p\": 1, \"bh_fdr_adj_p\": 0.4667}, \"method\": \"exact_permutation_test_two_tailed\", \"n_permutations\": 120, \"bug_fixed\": \"scipy.stats.spearmanr asymptotic p replaced with exact permutation\", \"bootstrap_ci\": {\"benchmark\": \"LAMBADA\", \"method\": \"architecture_resampling_percentile\", \"ci_lower\": -1, \"ci_upper\": -0.7, \"crosses_zero\": false, \"n_bootstrap\": 10000, \"n_valid\": 8875, \"seed\": 42, \"p_rho_negative\": 1, \"p_rho_positive\": 0, \"bca_note\": \"BCa degenerate at rho=-1.0 boundary; percentile CI used\"}, \"gdn_excluded\": {\"LAMBADA\": {\"rho\": -0.7, \"exact_p\": 0.2333, \"direction\": \"WEAKER\"}, \"HellaSwag\": {\"rho\": 0.5, \"exact_p\": 0.45, \"direction\": \"STRONGER\"}, \"WinoGrande\": {\"rho\": 0.3, \"exact_p\": 0.6833, \"direction\": \"STRONGER\"}, \"ARC-Easy\": {\"rho\": -0.9, \"exact_p\": 0.0833, \"direction\": \"STRONGER\"}, \"ARC-Challenge\": {\"rho\": -0.2, \"exact_p\": 0.7833, \"direction\": \"WEAKER\"}, \"MMLU\": {\"rho\": 0.6, \"exact_p\": 0.35, \"direction\": \"WEAKER\"}, \"note\": \"ARC-Easy rho improves from -0.7 to -0.9 (p=0.0833) without GDN confound — suggestive second anchor\"}}}, {\"id\": \"exp-009\", \"registry_id\": \"exp-009\", \"claim\": 1, \"title\": \"Wang et al. explicit differentiation\", \"description\": \"Formal side-by-side comparison: what Wang et al. report vs our analysis. Extract their exact convergence-related statements. Quantify the increment: (a) they don't compute cross-arch std trajectories, (b) no per-example analysis, (c) no scale-dependent convergence characterization, (d) no mechanistic analysis.\\n\", \"priority\": \"P0\", \"type\": \"analysis\", \"gpu_budget_hours\": 0, \"deps\": [], \"data_source\": \"Wang et al. arXiv 2507.06457\", \"pass_fail\": \"Clear 4-point differentiation documented\", \"status\": \"DONE\", \"conclusion\": \"success\"}, {\"id\": \"exp-010\", \"registry_id\": \"exp-010\", \"claim\": 3, \"title\": \"Convergence-divergence bridge analysis\", \"description\": \"For LAMBADA, plot aggregate convergence curve alongside per-example divergence metrics (Jaccard, net effect asymmetry) as function of attention ratio. Show that convergence and divergence co-evolve—more attention = more aggregate convergence BUT also more architecture-specific per-example effects. Core visualization for Claim 3 (underspecification in hybrid architectures).\\n\", \"priority\": \"P0\", \"type\": \"analysis\", \"gpu_budget_hours\": 0, \"deps\": [\"exp-001\", \"exp-003\"], \"pass_fail\": \"Convergence-divergence co-evolution demonstrated with significant correlation\", \"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"aggregate_convergence\": {\"std_pure\": 0.024, \"std_h24_1\": 0.0162, \"std_h12_1\": 0.0136, \"std_h6_1\": 0.0061, \"std_h3_1\": 0.0049, \"reduction_ratio\": 0.8, \"note\": \"Cross-arch std drops 5x monotonically\"}, \"per_example_divergence\": {\"jaccard_helped_range\": [0.092, 0.1], \"jaccard_hurt_range\": [0.081, 0.099], \"net_asymmetry_range\": [0.013, 0.04], \"net_asymmetry_trend\": \"increasing with attention ratio\", \"note\": \"Jaccard saturates at ~0.095 by 4% attention (h24-1), flat thereafter\"}, \"co_evolution_spearman\": {\"std_vs_J_helped\": {\"rho\": -0.7, \"exact_p\": 0.23}, \"std_vs_J_hurt\": {\"rho\": -0.8, \"exact_p\": 0.13}, \"CAVEAT\": \"D008: rho inflated by pure=0 degeneracy (Jaccard=NaN->0). Excluding pure: rho=-0.40, p=0.75. NOT co-evolution.\"}, \"key_finding\": \"DECOUPLING (D008): minimal attention (4%) creates per-example specificity (Jaccard saturates ~0.095), gradual attention drives aggregate convergence (sigma 0.024->0.005). Two processes operate on different timescales. Net asymmetry INCREASES (0.013->0.040).\", \"narrative_constraints\": \"PROHIBITED: co-evolution, paradoxical coexistence, paradox. USE: decoupling, different timescales.\"}}, {\"id\": \"exp-011\", \"registry_id\": \"exp-011\", \"claim\": 1, \"title\": \"Additional high-retrieval benchmarks (Dream W1 response)\", \"description\": \"Dream review: LAMBADA alone does not survive Bonferroni (p=0.017 > α=0.0083). Need a second significant anchor point on a high-retrieval task. Run 1.3B models on additional retrieval-heavy benchmarks available in lm-eval: (a) StoryCloze (context completion, structurally similar to LAMBADA), (b) BoolQ (passage-based yes/no, context retrieval), (c) COPA (causal reasoning from short narratives). Compute cross-arch std at each attention ratio for each benchmark. Test for convergence (Spearman + exact permutation, two-tailed). If ANY shows significant convergence → second anchor established, W1 substantially mitigated.\\n\", \"priority\": \"P0\", \"type\": \"experiment\", \"gpu_budget_hours\": 8, \"deps\": [], \"pass_fail\": \"≥1 additional benchmark shows significant convergence (p<0.05 two-tailed)\", \"note\": \"CRITICAL for Findings acceptance. Dream best case = 2.5 without this. Added post-D006.\", \"status\": \"DONE\", \"conclusion\": \"negative\", \"metrics\": {\"boolq\": {\"rho\": 0.2, \"raw_p\": 0.7833, \"bonferroni_adj_p_9\": 1, \"std_pure\": 0.0163, \"std_h3_1\": 0.0236, \"convergence\": false}, \"piqa\": {\"rho\": -0.5, \"raw_p\": 0.45, \"bonferroni_adj_p_9\": 1, \"std_pure\": 0.0054, \"std_h3_1\": 0.0034, \"convergence\": false}, \"sciq\": {\"rho\": 0.1, \"raw_p\": 0.95, \"bonferroni_adj_p_9\": 1, \"std_pure\": 0.0087, \"std_h3_1\": 0.0074, \"convergence\": false}, \"copa_supplementary\": {\"rho\": -0.67, \"raw_p\": 0.2667, \"std_pure\": 0.0262, \"std_h3_1\": 0.0047, \"convergence_ratio\": 5.57, \"note\": \"supplementary only (n=100), not in main Bonferroni\"}, \"LAMBADA_recomputed\": {\"rho\": -1, \"raw_p\": 0.0167, \"bonferroni_adj_p_6\": 0.1, \"bonferroni_adj_p_10\": 0.167, \"note\": \"6-Bonf=0.100 (D003 pre-registered); 10-Bonf=0.167; does not survive strict Bonferroni\"}, \"merged_10benchmark_significant_count\": \"0/10\", \"method\": \"exact_permutation_test_two_tailed\", \"D009_strategy\": \"BCa CI [-1.0,-0.7] as primary evidence; 6-Bonf adj_p=0.100 reported honestly; 10-benchmark negative -> task-specificity positive evidence (supplementary); underpowered caveat in Limitations\", \"D009_prohibited\": \"NO post-hoc 2-benchmark Bonferroni; NO post-hoc rho<0 subset correction\", \"conclusion\": \"No second anchor. Convergence LAMBADA-specific. W1 addressed via task-specificity reframing (D009).\"}}], \"total\": 11}, \"error\": null, \"metadata\": {}}"
    }
  },
  "sourceToolAssistantUUID": "896921bc-cafe-4244-9aaa-456b26890548",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/sessions/agent_aa1a2296",
  "sessionId": "ccd4bb6d-9c70-4ece-9e7e-8b842791a0aa",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 33 · 2026-05-22T16:42:14.463Z_

```json
{
  "parentUuid": "781de150-f0e9-459b-a828-8ad9f92f7e9c",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "ea693992-7839-4daa-ba66-8e2be85ec9fd",
  "timestamp": "2026-05-22T16:42:14.463Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/sessions/agent_aa1a2296",
  "sessionId": "ccd4bb6d-9c70-4ece-9e7e-8b842791a0aa",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 34_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[CRON] 实验进程已正常退出，状态已转为 ANALYZING，需要你分析结果并推进到 DONE。 详情: Process exited cleanly, W&B data available  - exp_id: exp-005-gla-pure - project: entrainment_gated_ft - server: westb-48145 - log_path: ~/runs/e…",
  "leafUuid": "ea693992-7839-4daa-ba66-8e2be85ec9fd",
  "sessionId": "ccd4bb6d-9c70-4ece-9e7e-8b842791a0aa"
}
```

---

### Runtime record

_source line 35_

```json
{
  "type": "ai-title",
  "aiTitle": "Analyze experiment results and mark as done",
  "sessionId": "ccd4bb6d-9c70-4ece-9e7e-8b842791a0aa"
}
```

---

### Assistant

_source line 36 · 2026-05-22T16:42:31.581Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a clear picture. Let me analyze the situation:

**exp-005-gla-pure** details:
- Status: PREPARING (needs to be updated to ANALYZING → DONE)
- Command: `patch_fla_eval.py` evaluating `340M-20B-GLA-pure-baseline` on `lambada_openai,arc_easy`
- Server: westb-48145
- Process exited cleanly, W&B data available
- This is part of the zoo expansion (exp-005) adding GLA/DeltaNet/HGRN architectures


- The parent experiment's hypothesis is about whether Jaccard overlap of helped/hurt sets stays significantly above chance when scaling from 3 to 6 linear attention architectures

I can see DeltaNet already has metrics from exp-005-dn-eval, while exp-005-gla-eval failed due to a missing model registration, and there are still two workers processing related tasks. Now I need to figure out what actions to take next.

Looking at the next steps, I should spawn a worker to SSH into the server, retrieve the logs and results from exp-005-gla-pure, then extract the relevant metrics and update the registry. I also need to review the resource-saturation skill before reporting findings to the Director, and load TodoWrite since the system flagged it.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ea693992-7839-4daa-ba66-8e2be85ec9fd",
  "isSidechain": false,
  "requestId": "req_011CbHwY2z1b1rGyRyHsMzTd",
  "type": "assistant",
  "uuid": "e09e53a8-0795-4a50-9df1-dd5facd31824",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/sessions/agent_aa1a2296",
  "sessionId": "ccd4bb6d-9c70-4ece-9e7e-8b842791a0aa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015mnwrQNgBu4bvnaBoJ2tNZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 30574,
      "cache_read_input_tokens": 46233,
      "output_tokens": 566,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 30574,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 566,
          "cache_read_input_tokens": 46233,
          "cache_creation_input_tokens": 30574,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 30574
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

_source line 37 · 2026-05-22T16:42:31.583Z_

Session 初始化完成。现在处理 exp-005-gla-pure 回调——派 Worker 去服务器读取结果。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e09e53a8-0795-4a50-9df1-dd5facd31824",
  "isSidechain": false,
  "requestId": "req_011CbHwY2z1b1rGyRyHsMzTd",
  "type": "assistant",
  "uuid": "a32c557f-3390-42ce-a476-6b5037146606",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/sessions/agent_aa1a2296",
  "sessionId": "ccd4bb6d-9c70-4ece-9e7e-8b842791a0aa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015mnwrQNgBu4bvnaBoJ2tNZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 30574,
      "cache_read_input_tokens": 46233,
      "output_tokens": 566,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 30574,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 566,
          "cache_read_input_tokens": 46233,
          "cache_creation_input_tokens": 30574,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 30574
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

_source line 38 · 2026-05-22T16:42:31.606Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01EP9ydynysKX62sxd8b1o4U`</summary>

```json
{
  "query": "select:TodoWrite",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a32c557f-3390-42ce-a476-6b5037146606",
  "isSidechain": false,
  "requestId": "req_011CbHwY2z1b1rGyRyHsMzTd",
  "type": "assistant",
  "uuid": "77b87a09-ad9f-425a-82b5-6827ce228774",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/sessions/agent_aa1a2296",
  "sessionId": "ccd4bb6d-9c70-4ece-9e7e-8b842791a0aa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015mnwrQNgBu4bvnaBoJ2tNZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 30574,
      "cache_read_input_tokens": 46233,
      "output_tokens": 566,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 30574,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 566,
          "cache_read_input_tokens": 46233,
          "cache_creation_input_tokens": 30574,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 30574
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

_source line 39 · 2026-05-22T16:42:31.610Z_

<details><summary>↩ Tool result · `toolu_01EP9ydynysKX62sxd8b1o4U`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "TodoWrite"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "77b87a09-ad9f-425a-82b5-6827ce228774",
  "isSidechain": false,
  "promptId": "53afff33-bebc-42c8-b6ca-8baf6ae2df0c",
  "type": "user",
  "uuid": "a57bfa0c-9e48-4e6b-a6ae-6830db0bc207",
  "toolUseResult": {
    "matches": [
      "TodoWrite"
    ],
    "query": "select:TodoWrite",
    "total_deferred_tools": 82
  },
  "sourceToolAssistantUUID": "77b87a09-ad9f-425a-82b5-6827ce228774",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/sessions/agent_aa1a2296",
  "sessionId": "ccd4bb6d-9c70-4ece-9e7e-8b842791a0aa",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 40 · 2026-05-22T16:42:38.589Z_

<details open><summary>🔧 Tool call — TodoWrite · `toolu_0175mKqTzo1TSUH2CFURh9DV`</summary>

```json
{
  "todos": [
    {
      "content": "派 Worker 读取 exp-005-gla-pure 结果日志和输出",
      "status": "in_progress",
      "activeForm": "派 Worker 读取 exp-005-gla-pure 结果"
    },
    {
      "content": "根据结果更新 registry (metrics, conclusion, status→DONE)",
      "status": "pending",
      "activeForm": "更新 registry"
    },
    {
      "content": "更新 report.md",
      "status": "pending",
      "activeForm": "更新 report.md"
    },
    {
      "content": "向 Director 汇报结果",
      "status": "pending",
      "activeForm": "向 Director 汇报"
    }
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a57bfa0c-9e48-4e6b-a6ae-6830db0bc207",
  "isSidechain": false,
  "requestId": "req_011CbHwZJSUKu3onkbqHsfh7",
  "type": "assistant",
  "uuid": "25cd239a-f897-47ed-8f2f-14fc7c5f57d8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/sessions/agent_aa1a2296",
  "sessionId": "ccd4bb6d-9c70-4ece-9e7e-8b842791a0aa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017YYET8SgQUhgC1hrBP2amn",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2956,
      "cache_read_input_tokens": 76807,
      "output_tokens": 223,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2956,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 223,
          "cache_read_input_tokens": 76807,
          "cache_creation_input_tokens": 2956,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2956
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

_source line 41 · 2026-05-22T16:42:38.591Z_

<details><summary>↩ Tool result · `toolu_0175mKqTzo1TSUH2CFURh9DV`</summary>

```text
Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "25cd239a-f897-47ed-8f2f-14fc7c5f57d8",
  "isSidechain": false,
  "promptId": "53afff33-bebc-42c8-b6ca-8baf6ae2df0c",
  "type": "user",
  "uuid": "8657e2d0-ae52-4cd3-a6d1-62f56e1c8ec2",
  "toolUseResult": {
    "oldTodos": [],
    "newTodos": [
      {
        "content": "派 Worker 读取 exp-005-gla-pure 结果日志和输出",
        "status": "in_progress",
        "activeForm": "派 Worker 读取 exp-005-gla-pure 结果"
      },
      {
        "content": "根据结果更新 registry (metrics, conclusion, status→DONE)",
        "status": "pending",
        "activeForm": "更新 registry"
      },
      {
        "content": "更新 report.md",
        "status": "pending",
        "activeForm": "更新 report.md"
      },
      {
        "content": "向 Director 汇报结果",
        "status": "pending",
        "activeForm": "向 Director 汇报"
      }
    ],
    "verificationNudgeNeeded": false
  },
  "sourceToolAssistantUUID": "25cd239a-f897-47ed-8f2f-14fc7c5f57d8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/sessions/agent_aa1a2296",
  "sessionId": "ccd4bb6d-9c70-4ece-9e7e-8b842791a0aa",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 42 · 2026-05-22T16:42:58.357Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__spawn_worker · `toolu_01QUGPKvtHq7YBYF1BB9Hx4k`</summary>

````json
{
  "task_type": "analysis:exp-005-gla-pure-results",
  "project": "entrainment_gated_ft",
  "task_prompt": "## 任务：读取 exp-005-gla-pure 评估结果\n\nexp-005-gla-pure 已完成（进程正常退出）。你需要读取结果并汇总。\n\n### 服务器信息\n- 服务器: westb-48145\n- 日志: ~/runs/entrainment_gated_ft/exp-005-gla-pure.log\n- 结果目录: /root/entrainment_gated_ft/results/exp005_zoo_expansion/GLA_pure/\n- 模型: 340M-20B-GLA-pure-baseline\n- 任务: lambada_openai, arc_easy\n- 使用了 patch_fla_eval.py 脚本（修复 fla 0.5.0 + transformers 5.8.1 兼容问题）\n\n### 要做的事\n1. SSH 到 westb-48145，用 ssh_read_only 读取日志文件尾部（最后 50 行）\n2. 读取结果目录下的 JSON 结果文件（lm-eval 输出格式，通常是 results.json 或按模型名命名的子目录下的 results*.json）\n3. 提取关键指标：\n   - lambada_openai: acc, acc_stderr, perplexity (ppl), word_perplexity\n   - arc_easy: acc, acc_norm, acc_stderr\n4. 检查是否有 per-example log_samples 数据（用于后续 Jaccard 分析）\n5. 同时读取已有的 GLA hybrid-3-1 结果用于对比：\n   - 检查 /root/entrainment_gated_ft/results/exp005_zoo_expansion/GLA_hybrid-3-1/ 是否有结果\n   - 如果没有，检查 exp-005 registry 中的 gla_h31_lambada_acc=0.3819, gla_h31_arc_acc=0.5673\n\n### 输出格式\n用 save_project_file 将结果写入 memory.md 的追加段落（先 read_project_file 读现有内容，再追加），格式：\n```\n## exp-005-gla-pure 结果 (2026-05-22)\n- 模型: 340M-20B-GLA-pure-baseline\n- lambada_openai: acc=X.XXXX, ppl=X.XX\n- arc_easy: acc=X.XXXX, acc_norm=X.XXXX\n- per-example log_samples: 有/无\n- 对比 GLA hybrid-3-1: lambada_acc=0.3819, arc_acc=0.5673\n```\n\n同时用 update_registry 更新 exp-005-gla-pure：\n- field=metrics, value={完整指标字典}\n- field=conclusion, value=\"success\"（如果结果正常）或 \"failed\"（如果有错误）\n- field=status, value=\"DONE\"\n\n**注意：先读日志确认是否真正成功（看最后有没有 GLA_PURE_EVAL_DONE sentinel），再决定 conclusion。**\n",
  "tool_groups": [
    "ssh",
    "registry",
    "knowledge"
  ]
}
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8657e2d0-ae52-4cd3-a6d1-62f56e1c8ec2",
  "isSidechain": false,
  "requestId": "req_011CbHwZpLKAeLhsWRbxEWVV",
  "type": "assistant",
  "uuid": "f368f8fc-7b55-4d20-b9ea-99a9ebf815ea",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/sessions/agent_aa1a2296",
  "sessionId": "ccd4bb6d-9c70-4ece-9e7e-8b842791a0aa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012jZHNkL5ngex2pM5qwBirR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 380,
      "cache_read_input_tokens": 79763,
      "output_tokens": 984,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 380,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 984,
          "cache_read_input_tokens": 79763,
          "cache_creation_input_tokens": 380,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 380
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

_source line 43 · 2026-05-22T16:43:01.335Z_

<details><summary>↩ Tool result · `toolu_01QUGPKvtHq7YBYF1BB9Hx4k`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"worker_id\": \"worker_analysis_exp-005-gla-pure-results_20260522T164258\", \"status\": \"running\", \"log_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/logs/workers/worker_analysis_exp-005-gla-pure-results_20260522T164258.log\", \"setup_data\": {}, \"message\": \"Worker worker_analysis_exp-005-gla-pure-results_20260522T164258 started. Use get_worker_status('worker_analysis_exp-005-gla-pure-results_20260522T164258') to check progress.\"}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f368f8fc-7b55-4d20-b9ea-99a9ebf815ea",
  "isSidechain": false,
  "promptId": "53afff33-bebc-42c8-b6ca-8baf6ae2df0c",
  "type": "user",
  "uuid": "4db9291c-79a0-4151-ae48-792833e285f3",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"worker_id\\\": \\\"worker_analysis_exp-005-gla-pure-results_20260522T164258\\\", \\\"status\\\": \\\"running\\\", \\\"log_path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/logs/workers/worker_analysis_exp-005-gla-pure-results_20260522T164258.log\\\", \\\"setup_data\\\": {}, \\\"message\\\": \\\"Worker worker_analysis_exp-005-gla-pure-results_20260522T164258 started. Use get_worker_status('worker_analysis_exp-005-gla-pure-results_20260522T164258') to check progress.\\\"}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"worker_id\": \"worker_analysis_exp-005-gla-pure-results_20260522T164258\", \"status\": \"running\", \"log_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/logs/workers/worker_analysis_exp-005-gla-pure-results_20260522T164258.log\", \"setup_data\": {}, \"message\": \"Worker worker_analysis_exp-005-gla-pure-results_20260522T164258 started. Use get_worker_status('worker_analysis_exp-005-gla-pure-results_20260522T164258') to check progress.\"}, \"error\": null, \"metadata\": {}}"
    }
  },
  "sourceToolAssistantUUID": "f368f8fc-7b55-4d20-b9ea-99a9ebf815ea",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/sessions/agent_aa1a2296",
  "sessionId": "ccd4bb6d-9c70-4ece-9e7e-8b842791a0aa",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---
