# Research conversation: [CRON] 实验进程异常退出（失败），需要你诊断原因。 详情: Process exited without valid W&B metrics - exp_id: kl50_global_s123_downstream_v2 - pro

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 46
- **Recorded user turns:** 1
- **Tool calls:** 13
- **Original source:** `logs/chats/exported-trajectories/account-3/062027a5-1c13-4530-a568-995829f28b19.jsonl`
- **Structured JSON:** [`4e8755f98076fe36b74e.json`](../../sessions/4e/4e8755f98076fe36b74e.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-22T18:49:12.668Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-22T18:49:12.668Z",
  "sessionId": "062027a5-1c13-4530-a568-995829f28b19",
  "content": "[CRON] 实验进程异常退出（失败），需要你诊断原因。\n详情: Process exited without valid W&B metrics\n\n- exp_id: kl50_global_s123_downstream_v2\n- project: distill_sparse_swiglu\n- server: westd-34887\n- log_path: ~/runs/distill_sparse_swiglu/kl50_global_s123_downstream_v2.log"
}
```

---

### Runtime record

_source line 2 · 2026-05-22T18:49:12.671Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-22T18:49:12.671Z",
  "sessionId": "062027a5-1c13-4530-a568-995829f28b19"
}
```

---

## Round 1

44 recorded events

### User

_source line 3 · 2026-05-22T18:49:12.708Z_

[CRON] 实验进程异常退出（失败），需要你诊断原因。
详情: Process exited without valid W&B metrics

- exp_id: kl50_global_s123_downstream_v2
- project: distill_sparse_swiglu
- server: westd-34887
- log_path: ~/runs/distill_sparse_swiglu/kl50_global_s123_downstream_v2.log

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "e0126d52-e1d3-4c8c-a4f2-76af8e88bda0",
  "type": "user",
  "uuid": "125051f7-265d-43aa-a5de-c3904b0c0d8e",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/agent_66b8aa9d",
  "sessionId": "062027a5-1c13-4530-a568-995829f28b19",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-22T18:49:12.707Z_

```json
{
  "parentUuid": "125051f7-265d-43aa-a5de-c3904b0c0d8e",
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
  "uuid": "22460585-db8e-4fd3-8b5f-e9a9bb8196fa",
  "timestamp": "2026-05-22T18:49:12.707Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/agent_66b8aa9d",
  "sessionId": "062027a5-1c13-4530-a568-995829f28b19",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---

### Runtime record

_source line 5 · 2026-05-22T18:49:12.708Z_

```json
{
  "parentUuid": "22460585-db8e-4fd3-8b5f-e9a9bb8196fa",
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
  "uuid": "ecdba9d4-e116-4719-a28b-5ead711f1526",
  "timestamp": "2026-05-22T18:49:12.708Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/agent_66b8aa9d",
  "sessionId": "062027a5-1c13-4530-a568-995829f28b19",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---

### Runtime record

_source line 6 · 2026-05-22T18:49:12.708Z_

```json
{
  "parentUuid": "ecdba9d4-e116-4719-a28b-5ead711f1526",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "80385103-0805-4cba-b25d-75169f425050",
  "timestamp": "2026-05-22T18:49:12.708Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/agent_66b8aa9d",
  "sessionId": "062027a5-1c13-4530-a568-995829f28b19",
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
  "aiTitle": "Diagnose W&B metrics missing error in experiment",
  "sessionId": "062027a5-1c13-4530-a568-995829f28b19"
}
```

---

### Assistant

_source line 8 · 2026-05-22T18:49:17.343Z_

<details><summary>Logged reasoning block</summary>

```text
收到 CRON 回调：实验 `kl50_global_s123_downstream_v2` 在 `westd-34887` 上进程异常退出。需要按 session-start 流程初始化，然后按 on-experiment-failed skill 处理。

先执行 session-start 初始化，然后读 on-experiment-failed skill。
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "80385103-0805-4cba-b25d-75169f425050",
  "isSidechain": false,
  "requestId": "req_011CbJ7DcFte2j85BDbkZT1F",
  "type": "assistant",
  "uuid": "5f576471-13f2-4cea-8c0b-cc10feff0ffa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/agent_66b8aa9d",
  "sessionId": "062027a5-1c13-4530-a568-995829f28b19",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0176Gufxd2yZxWp2DLuuRv1y",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 0,
      "cache_read_input_tokens": 38236,
      "output_tokens": 314,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 314,
          "cache_read_input_tokens": 38236,
          "cache_creation_input_tokens": 0,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
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

### Assistant

_source line 9 · 2026-05-22T18:49:18.041Z_

收到实验失败回调，开始 session-start 初始化并诊断。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5f576471-13f2-4cea-8c0b-cc10feff0ffa",
  "isSidechain": false,
  "requestId": "req_011CbJ7DcFte2j85BDbkZT1F",
  "type": "assistant",
  "uuid": "b4e6bdc6-161a-4654-9085-35081c42ed50",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/agent_66b8aa9d",
  "sessionId": "062027a5-1c13-4530-a568-995829f28b19",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0176Gufxd2yZxWp2DLuuRv1y",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 0,
      "cache_read_input_tokens": 38236,
      "output_tokens": 314,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 314,
          "cache_read_input_tokens": 38236,
          "cache_creation_input_tokens": 0,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
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

### Tool call

_source line 10 · 2026-05-22T18:49:20.537Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01USmrdiQKxEuuqqp423HnCk`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__reconcile_crons,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__read_roadmap,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__spawn_worker,mcp__agent-ml-research__main_agent_post_to_director",
  "max_results": 7
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b4e6bdc6-161a-4654-9085-35081c42ed50",
  "isSidechain": false,
  "requestId": "req_011CbJ7DcFte2j85BDbkZT1F",
  "type": "assistant",
  "uuid": "0fbfce69-708c-4898-877a-93b25e00bb1a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/agent_66b8aa9d",
  "sessionId": "062027a5-1c13-4530-a568-995829f28b19",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0176Gufxd2yZxWp2DLuuRv1y",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 0,
      "cache_read_input_tokens": 38236,
      "output_tokens": 314,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 314,
          "cache_read_input_tokens": 38236,
          "cache_creation_input_tokens": 0,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
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

_source line 11 · 2026-05-22T18:49:20.545Z_

<details><summary>↩ Tool result · `toolu_01USmrdiQKxEuuqqp423HnCk`</summary>

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
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0fbfce69-708c-4898-877a-93b25e00bb1a",
  "isSidechain": false,
  "promptId": "e0126d52-e1d3-4c8c-a4f2-76af8e88bda0",
  "type": "user",
  "uuid": "7694ad07-304e-416d-b41e-763649befe9e",
  "toolUseResult": {
    "matches": [
      "mcp__agent-ml-research__read_registry",
      "mcp__agent-ml-research__reconcile_crons",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__read_roadmap",
      "mcp__agent-ml-research__update_registry",
      "mcp__agent-ml-research__spawn_worker",
      "mcp__agent-ml-research__main_agent_post_to_director"
    ],
    "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__reconcile_crons,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__read_roadmap,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__spawn_worker,mcp__agent-ml-research__main_agent_post_to_director",
    "total_deferred_tools": 82
  },
  "sourceToolAssistantUUID": "0fbfce69-708c-4898-877a-93b25e00bb1a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/agent_66b8aa9d",
  "sessionId": "062027a5-1c13-4530-a568-995829f28b19",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-22T18:49:24.555Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_013eTvVvmLSws6btKz5pBFFx`</summary>

```json
{
  "project": "distill_sparse_swiglu",
  "limit": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7694ad07-304e-416d-b41e-763649befe9e",
  "isSidechain": false,
  "requestId": "req_011CbJ7EBkXAUhU5CntZQSuL",
  "type": "assistant",
  "uuid": "9c19b765-389a-4a28-b04d-9faf045e0ad1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/agent_66b8aa9d",
  "sessionId": "062027a5-1c13-4530-a568-995829f28b19",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GwNE1VVHQx5fbwMJqgpqYZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 3101,
      "cache_read_input_tokens": 38236,
      "output_tokens": 243,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3101,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 243,
          "cache_read_input_tokens": 38236,
          "cache_creation_input_tokens": 3101,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3101
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

_source line 13 · 2026-05-22T18:49:25.049Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__reconcile_crons · `toolu_01Bx1GLUtX68z5x5RaV9HmeY`</summary>

```json
{}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9c19b765-389a-4a28-b04d-9faf045e0ad1",
  "isSidechain": false,
  "requestId": "req_011CbJ7EBkXAUhU5CntZQSuL",
  "type": "assistant",
  "uuid": "3863c078-9182-4bde-aca1-9efbf20a6b85",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/agent_66b8aa9d",
  "sessionId": "062027a5-1c13-4530-a568-995829f28b19",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GwNE1VVHQx5fbwMJqgpqYZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 3101,
      "cache_read_input_tokens": 38236,
      "output_tokens": 243,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3101,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 243,
          "cache_read_input_tokens": 38236,
          "cache_creation_input_tokens": 3101,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3101
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

_source line 14 · 2026-05-22T18:49:25.500Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01XRSjA9KrTL8dEP11jsys48`</summary>

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
  "parentUuid": "3863c078-9182-4bde-aca1-9efbf20a6b85",
  "isSidechain": false,
  "requestId": "req_011CbJ7EBkXAUhU5CntZQSuL",
  "type": "assistant",
  "uuid": "bd12f263-bb99-4545-b1fb-dd6abf57feff",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/agent_66b8aa9d",
  "sessionId": "062027a5-1c13-4530-a568-995829f28b19",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GwNE1VVHQx5fbwMJqgpqYZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 3101,
      "cache_read_input_tokens": 38236,
      "output_tokens": 243,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3101,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 243,
          "cache_read_input_tokens": 38236,
          "cache_creation_input_tokens": 3101,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3101
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

_source line 15 · 2026-05-22T18:49:25.727Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_roadmap · `toolu_01CqjYCFa4mQqRK4Bfnfz86c`</summary>

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
  "parentUuid": "bd12f263-bb99-4545-b1fb-dd6abf57feff",
  "isSidechain": false,
  "requestId": "req_011CbJ7EBkXAUhU5CntZQSuL",
  "type": "assistant",
  "uuid": "bf8804e3-2543-4006-b66c-b6a3e9970be6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/agent_66b8aa9d",
  "sessionId": "062027a5-1c13-4530-a568-995829f28b19",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GwNE1VVHQx5fbwMJqgpqYZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 3101,
      "cache_read_input_tokens": 38236,
      "output_tokens": 243,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3101,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 243,
          "cache_read_input_tokens": 38236,
          "cache_creation_input_tokens": 3101,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3101
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

_source line 16 · 2026-05-22T18:49:25.833Z_

<details><summary>↩ Tool result · `toolu_013eTvVvmLSws6btKz5pBFFx`</summary>

```text
Error: result (217,678 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-14-projects-distill-sparse-swiglu--claude-sessions-agent-66b8aa9d/062027a5-1c13-4530-a568-995829f28b19/tool-results/mcp-agent-ml-research-read_registry-1779475765817.txt.
Format: JSON with schema: {result: string}
- For targeted queries (find a value, filter by field): use jq on the file directly.
- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-14-projects-distill-sparse-swiglu--claude-sessions-agent-66b8aa9d/062027a5-1c13-4530-a568-995829f28b19/tool-results/mcp-agent-ml-research-read_registry-1779475765817.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.
- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-14-projects-distill-sparse-swiglu--claude-sessions-agent-66b8aa9d/062027a5-1c13-4530-a568-995829f28b19/tool-results/mcp-agent-ml-research-read_registry-1779475765817.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim." A vague "summarize this" may lose detail.

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9c19b765-389a-4a28-b04d-9faf045e0ad1",
  "isSidechain": false,
  "promptId": "e0126d52-e1d3-4c8c-a4f2-76af8e88bda0",
  "type": "user",
  "uuid": "8346e332-537a-4f0a-8aae-5c3be68ffcb9",
  "toolUseResult": "Error: result (217,678 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-14-projects-distill-sparse-swiglu--claude-sessions-agent-66b8aa9d/062027a5-1c13-4530-a568-995829f28b19/tool-results/mcp-agent-ml-research-read_registry-1779475765817.txt.\nFormat: JSON with schema: {result: string}\n- For targeted queries (find a value, filter by field): use jq on the file directly.\n- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-14-projects-distill-sparse-swiglu--claude-sessions-agent-66b8aa9d/062027a5-1c13-4530-a568-995829f28b19/tool-results/mcp-agent-ml-research-read_registry-1779475765817.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.\n- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. \"/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-14-projects-distill-sparse-swiglu--claude-sessions-agent-66b8aa9d/062027a5-1c13-4530-a568-995829f28b19/tool-results/mcp-agent-ml-research-read_registry-1779475765817.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim.\" A vague \"summarize this\" may lose detail.\n",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {\"perlayer_kl_k4_50_s42_ppl_v2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-22T18:43:17.308Z\", \"updated_at\": \"2026-05-22T18:45:40.524Z\", \"hypothesis\": \"K=4 per-layer KL at 50% sparsity PPL eval (retry of perlayer_kl_k4_50_s42_ppl which failed due to ambiguous --sparsity arg). K=1 50% PPL=34.85, E2E KL 50% PPL=11.84. If K=4 PPL is close to E2E → mismatch dominates at 50% (same as 30%). If K=4 PPL remains high → genuine coupling increases with sparsity.\", \"parent\": \"perlayer_kl_k4_50_s42\", \"metrics\": {\"wikitext2_ppl\": 44.2321, \"sparsity_actual\": 0.495, \"seq_len\": 2048, \"num_sequences\": 141}, \"conclusion\": \"negative\"}, \"perlayer_kl_k4_50_s42_ppl\": {\"status\": \"DONE\", \"created_at\": \"2026-05-22T18:39:35.700Z\", \"updated_at\": \"2026-05-22T18:42:25.237Z\", \"hypothesis\": \"K=4 per-layer KL at 50% sparsity PPL eval. K=1 50% PPL=34.85, E2E KL 50% PPL=11.84. If K=4 PPL is close to E2E → mismatch dominates at 50% (same as 30%). If K=4 PPL remains high → genuine coupling increases with sparsity.\", \"parent\": \"perlayer_kl_k4_50_s42\", \"conclusion\": \"failed\"}, \"perlayer_kl_k4_50_s42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-22T17:42:05.816Z\", \"updated_at\": \"2026-05-22T18:39:54.573Z\", \"hypothesis\": \"K=4 per-layer KL at 50% sparsity: tests mismatch explanation rate at high sparsity. K=1 50% PPL=34.85, E2E KL 50% PPL=11.84. If K=4 closes large gap → mismatch dominates even more at high sparsity.\", \"parent\": \"perlayer_kl_50_s42\", \"conclusion\": \"success\"}, \"kl50_global_s123_downstream_v2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-22T17:42:51.552Z\", \"updated_at\": \"2026-05-22T18:39:51.918Z\", \"hypothesis\": \"Re-eval KL 50% global s123 downstream (ARC-c, WG, MMLU, GSM8K) to complete 3-seed data for Table 2. Previous attempt (kl50_global_s123_reeval) failed with EXIT_CODE=1.\", \"parent\": \"kl50_global_s123_reeval\", \"conclusion\": \"success\", \"metrics\": {\"arc_challenge_acc_norm\": 0.3916, \"winogrande_acc\": 0.6401, \"mmlu_acc\": 0.2908, \"gsm8k_exact_match\": 0.0341}}, \"perlayer_kl_k4_s456\": {\"status\": \"DONE\", \"created_at\": \"2026-05-22T13:36:14.417Z\", \"updated_at\": \"2026-05-22T16:16:58.996Z\", \"hypothesis\": \"K=4 per-layer KL (seed 456): replicates s42 pilot to confirm PPL mismatch explanation rate ~67% and downstream task-dependency pattern across seeds.\", \"parent\": \"perlayer_kl_k4_s42\", \"metrics\": {\"wikitext2_ppl\": 8.8828, \"arc_challenge_acc_norm\": 0.3857, \"winogrande_acc\": 0.6701, \"mmlu_acc\": 0.4351, \"gsm8k_exact_match\": 0.0788, \"hellaswag_acc_norm\": 0.6821, \"piqa_acc_norm\": 0.7503, \"boolq_acc\": 0.7092}, \"conclusion\": \"success\"}, \"perlayer_kl_k4_s123\": {\"status\": \"DONE\", \"created_at\": \"2026-05-22T13:36:32.577Z\", \"updated_at\": \"2026-05-22T16:12:32.871Z\", \"hypothesis\": \"K=4 per-layer KL (seed 123): replicates s42 pilot to confirm PPL mismatch explanation rate ~67% and downstream task-dependency pattern across seeds.\", \"parent\": \"perlayer_kl_k4_s42\", \"metrics\": {\"wikitext2_ppl\": 8.8897, \"arc_challenge_acc_norm\": 0.4053, \"winogrande_acc\": 0.6701, \"mmlu_acc\": 0.4118, \"gsm8k_exact_match\": 0.0781, \"hellaswag_acc_norm\": 0.6668, \"piqa_acc_norm\": 0.7448, \"boolq_acc\": 0.5914}, \"conclusion\": \"success\"}, \"mse30_s123_downstream\": {\"status\": \"DONE\", \"created_at\": \"2026-05-22T10:42:48.731Z\", \"updated_at\": \"2026-05-22T15:13:32.566Z\", \"metrics\": {\"arc_challenge_acc\": 0.3285, \"arc_challenge_acc_norm\": 0.3737, \"winogrande_acc\": 0.5699, \"mmlu_acc\": 0.2781, \"gsm8k_exact_match\": 0.0174, \"hellaswag_acc\": 0.4009, \"hellaswag_acc_norm\": 0.5358, \"piqa_acc\": 0.7106, \"piqa_acc_norm\": 0.7067, \"boolq_acc\": 0.6324}, \"conclusion\": \"success\", \"hypothesis\": \"MSE-trained predictor at 30% sparsity (seed 123) preserves downstream task performance comparable to dense baseline because MSE distillation captures sufficient activation magnitude information to maintain task-relevant features in the sparse SwiGLU network.\"}, \"constraint_remove_valley_kl30_s42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-22T13:49:57.933Z\", \"updated_at\": \"2026-05-22T14:47:00.000Z\", \"metrics\": {\"wikitext2_ppl\": 8.7592, \"arc_challenge_acc_norm\": 0.3933, \"mmlu_acc\": 0.4397, \"gsm8k_exact_match\": 0.0895, \"actual_sparsity\": 0.2955}, \"conclusion\": \"negative\"}, \"constraint_protect_late_kl30_s42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-22T13:50:02.509Z\", \"updated_at\": \"2026-05-22T14:28:00.000Z\", \"metrics\": {\"wikitext2_ppl\": 9.2638, \"arc_challenge_acc_norm\": 0.4241, \"mmlu_acc\": 0.4066, \"gsm8k_exact_match\": 0.0652}, \"conclusion\": \"negative\"}, \"qwen14b_kl30_s42_gsm8k_uniform\": {\"status\": \"DONE\", \"created_at\": \"2026-05-22T06:44:51.587Z\", \"updated_at\": \"2026-05-22T13:08:00.000Z\", \"hypothesis\": \"Qwen-14B KL 30% s42 GSM8K eval with uniform allocation. Fills missing GSM8K cell in Qwen-14B comparison table.\", \"parent\": \"qwen14b_kl30_s42_eval_uniform_v3\", \"metrics\": {\"gsm8k_exact_match\": 0.3548}, \"conclusion\": \"success\"}, \"perlayer_kl_k4_s42_downstream\": {\"status\": \"DONE\", \"created_at\": \"2026-05-22T11:34:33.471Z\", \"updated_at\": \"2026-05-22T12:48:13.289Z\", \"hypothesis\": \"Per-layer KL K=4 downstream eval at 30% uniform sparsity, 7 tasks (ARC-c, WG, MMLU, GSM8K, HS, PIQA, BoolQ). Tests whether K=4 active layers per step closes the downstream gap K=1→E2E (ARC-c +3.8pp, WG +3.0pp, MMLU +2.1pp, GSM8K +1.7pp, BoolQ +9.2pp). If K=4 ≈ E2E, gradient coupling is the mechanism and K=4 ≈ E2E approximation. If K=4 ≈ K=1, per-layer locality is the bottleneck regardless of K. Determines C1 narrative direction.\", \"parent\": \"perlayer_kl_k4_s42\", \"metrics\": {\"arc_challenge_acc_norm\": 0.4096, \"winogrande_acc\": 0.6669, \"mmlu_acc\": 0.4353, \"gsm8k_exact_match\": 0.0516, \"hellaswag_acc_norm\": 0.6849, \"piqa_acc_norm\": 0.7399, \"boolq_acc\": 0.7318}, \"conclusion\": \"success\"}, \"perlayer_kl_k4_s42_ppl\": {\"status\": \"DONE\", \"created_at\": \"2026-05-22T11:33:49.662Z\", \"updated_at\": \"2026-05-22T11:36:26.380Z\", \"hypothesis\": \"K=4 per-layer KL training reduces train-inference mismatch compared to K=1, yielding PPL closer to E2E KL (8.81) than K=1 baseline (9.05) at 30% uniform sparsity\", \"parent\": \"perlayer_kl_k4_s42\", \"metrics\": {\"wikitext2_ppl\": 8.8932, \"sparsity_mean\": 0.296, \"ppl_k1_baseline\": 9.05, \"ppl_e2e_kl_baseline\": 8.81, \"delta_vs_k1\": -0.16, \"delta_vs_e2e_kl\": 0.08}, \"conclusion\": \"negative\"}, \"perlayer_kl_k4_s42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-22T11:31:06.522Z\", \"updated_at\": \"2026-05-22T11:31:45.093Z\", \"conclusion\": \"success\", \"hypothesis\": \"Per-layer KL distillation with K=4 active layers per step and adaptive lambda scheduling can train the sparsity predictor to achieve avg KL < 0.05 while maintaining ~28% sparsity across all 32 layers.\"}, \"mse30_s456_downstream\": {\"status\": \"DONE\", \"created_at\": \"2026-05-22T09:46:58.268Z\", \"updated_at\": \"2026-05-22T10:58:00.517Z\", \"hypothesis\": \"MSE 30% s456 full downstream eval (ARC-c+WG+MMLU+GSM8K+HS+PIQA+BoolQ) to complete 3-seed mean±std for 2D decomposition table (objective × allocation). Reviewer required multi-seed for MSE row; s42 already has full downstream, s123 running in parallel. Together the three seeds give mean±std for MSE 30% uniform downstream so the table can replace s42-only numbers without re-write of the framing.\", \"parent\": \"mse30_s456\", \"metrics\": {\"arc_challenge_acc_norm\": 0.3882, \"winogrande_acc\": 0.6196, \"mmlu_acc\": 0.3264, \"gsm8k_exact_match\": 0.0311, \"hellaswag_acc_norm\": 0.6129, \"piqa_acc_norm\": 0.7383, \"boolq_acc\": 0.7034}, \"conclusion\": \"success\"}, \"mse30_s42_boolq\": {\"status\": \"DONE\", \"created_at\": \"2026-05-22T09:16:56.987Z\", \"updated_at\": \"2026-05-22T09:18:50.839Z\", \"parent\": \"mse30_s42_train\", \"hypothesis\": \"MSE 30% sparsity (s42) BoolQ downstream eval: sparse model retains majority of dense BoolQ accuracy, completing the 7-task downstream evaluation suite for the 2D decomposition table.\", \"metrics\": {\"boolq_acc\": 0.5997, \"boolq_acc_stderr\": 0.008569, \"boolq_sample_len\": 3270}, \"conclusion\": \"success\"}, \"perlayer_kl_50_s42_downstream\": {\"status\": \"DONE\", \"created_at\": \"2026-05-22T06:53:21.544Z\", \"updated_at\": \"2026-05-22T08:14:27.075Z\", \"hypothesis\": \"Per-layer KL distillation at 50% sparsity will produce competitive downstream task performance despite high PPL (34.85), because per-layer optimization may preserve task-relevant features even when global perplexity degrades.\", \"conclusion\": \"negative\", \"metrics\": {\"arc_challenge_acc_norm\": 0.2705, \"winogrande_acc\": 0.5154, \"mmlu_acc\": 0.2658, \"gsm8k_exact_match\": 0.0174, \"hellaswag_acc_norm\": 0.3818, \"piqa_acc_norm\": 0.6279}}, \"perlayer_kl_50_s42_boolq\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-22T07:10:15.073Z\", \"updated_at\": \"2026-05-22T07:10:15.074Z\"}, \"perlayer_kl_50_s42_ppl\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-22T06:53:14.546Z\", \"updated_at\": \"2026-05-22T07:09:22.594Z\"}, \"perlayer_kl_50_s42\": {\"status\": \"ANALYZING\", \"created_at\": \"2026-05-22T01:47:41.520Z\", \"updated_at\": \"2026-05-22T06:56:21.449Z\", \"hypothesis\": \"Per-layer KL 50% uniform training (seed 42). Tests whether 2D decomposition (signal type × coupling scope) holds at higher sparsity. PPL should fall between E2E KL 50% (11.84) and MSE (18.52). If gap to E2E KL is small (&lt;5%), signal type dominates PPL even at 50%, strengthening the 2D claim.\", \"metrics\": {\"avg_kl\": 0.0282, \"sparsity_mean\": 0.496, \"wikitext2_ppl\": 34.85, \"training_steps\": 10000, \"training_duration_s\": 18216}, \"conclusion\": \"negative\"}, \"revkl_30_s42_boolq_uniform\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-22T02:55:00.102Z\", \"updated_at\": \"2026-05-22T03:21:33.292Z\", \"conclusion\": \"failed\"}, \"cross_seed_jaccard_r18w7\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T23:54:11.633Z\", \"updated_at\": \"2026-05-22T00:47:17.998Z\", \"hypothesis\": \"Cross-seed mask Jaccard distance for KL-trained predictors should be significantly lower than KL-vs-magnitude divergence (46-68%), proving that the divergence is caused by loss function design rather than seed noise. If cross-seed Jaccard is comparable to 46-68%, then the KL-vs-magnitude divergence claim lacks discriminative power (R18-W7).\", \"metrics\": {\"cross_seed_jaccard_mean\": 0.3633, \"cross_seed_s42_s123\": 0.364, \"cross_seed_s42_s456\": 0.3617, \"cross_seed_s123_s456\": 0.3642, \"kl_vs_mag_jaccard_mean\": 0.4276, \"kl_vs_mag_s42\": 0.4276, \"kl_vs_mag_s123\": 0.4274, \"kl_vs_mag_s456\": 0.4278, \"ratio\": 1.2, \"early_cross_seed\": 0.361, \"early_kl_vs_mag\": 0.4378, \"middle_cross_seed\": 0.3521, \"middle_kl_vs_mag\": 0.4153, \"late_cross_seed\": 0.377, \"late_kl_vs_mag\": 0.4294}, \"conclusion\": \"negative\"}, \"perlayer_kl_s123_boolq\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T23:38:25.403Z\", \"updated_at\": \"2026-05-21T23:47:10.956Z\", \"hypothesis\": \"Per-layer KL s123 BoolQ eval at 30% uniform allocation. Completes 3-seed BoolQ set for per-layer KL (s42=71.77%, s456=51.25% already done). Required for Table 4 comparison vs E2E KL.\", \"parent\": \"perlayer_kl_30_s123_v4\", \"metrics\": {\"boolq_acc\": 0.7046}, \"conclusion\": \"success\"}, \"kl30_uniform_boolq_s456\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T23:38:29.122Z\", \"updated_at\": \"2026-05-21T23:47:08.540Z\", \"hypothesis\": \"E2E KL 30% uniform allocation BoolQ eval (seed 456). Part of 3-seed BoolQ set with uniform allocation to match Table 4 consistency.\", \"parent\": \"kl_sparsity30_s456\", \"metrics\": {\"boolq_acc\": 0.7554}, \"conclusion\": \"success\"}, \"kl30_uniform_boolq_s123\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T23:34:09.491Z\", \"updated_at\": \"2026-05-21T23:47:06.142Z\", \"hypothesis\": \"E2E KL 30% uniform allocation BoolQ eval (seed 123). Part of 3-seed BoolQ set with uniform allocation to match Table 4 consistency.\", \"parent\": \"kl_sparsity30_s123\", \"metrics\": {\"boolq_acc\": 0.7006}, \"conclusion\": \"success\"}, \"kl30_uniform_boolq_s42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T23:34:06.499Z\", \"updated_at\": \"2026-05-21T23:47:03.778Z\", \"hypothesis\": \"E2E KL 30% uniform allocation BoolQ eval (seed 42). Eliminates allocation mismatch caveat — previous BoolQ=76.85% was from global allocation. Re-evaluates with uniform to match Table 4 consistency (D091).\", \"parent\": \"kl_sparsity30_s42_v3\", \"metrics\": {\"boolq_acc\": 0.756}, \"conclusion\": \"success\"}, \"perlayer_kl_s123_downstream_v2\": {\"status\": \"PENDING\", \"created_at\": \"2026-05-21T21:29:09.961Z\", \"updated_at\": \"2026-05-21T22:47:13.663Z\", \"hypothesis\": \"Per-layer KL s123 downstream 6-task eval (ARC-c, WG, MMLU, GSM8K, HS, PIQA) — excluding BoolQ due to missing super_glue cache on westd-34887. Retry of perlayer_kl_s123_downstream.\", \"parent\": \"perlayer_kl_30_s123_v4\"}, \"perlayer_kl_s123_convergence\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T19:16:48.424Z\", \"updated_at\": \"2026-05-21T21:32:21.549Z\", \"hypothesis\": \"Per-layer KL s123 convergence curve: PPL at step 2000/4000/6000/8000 to determine how many training steps are needed. Useful for appendix (training efficiency analysis).\", \"parent\": \"perlayer_kl_30_s123_v4\", \"conclusion\": \"success\", \"metrics\": {\"step_2000_ppl\": 9.9795, \"step_4000_ppl\": 9.4108, \"step_6000_ppl\": 9.1051, \"step_8000_ppl\": 9.1567, \"step_10000_ppl\": 9.0598}}, \"perlayer_kl_s42_convergence\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T19:16:47.084Z\", \"updated_at\": \"2026-05-21T21:32:19.257Z\", \"hypothesis\": \"Per-layer KL s42 convergence curve: PPL at step 2000/4000/6000/8000 to determine how many training steps are needed. Useful for appendix (training efficiency analysis).\", \"parent\": \"perlayer_kl_30_s42_v6\", \"conclusion\": \"success\", \"metrics\": {\"step_2000_ppl\": 9.8515, \"step_4000_ppl\": 9.251, \"step_6000_ppl\": 9.1071, \"step_8000_ppl\": 9.0558, \"step_10000_ppl\": 9.0568}}, \"perlayer_kl_s456_boolq_v2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T15:18:35.730Z\", \"updated_at\": \"2026-05-21T21:28:38.115Z\", \"hypothesis\": \"Per-layer KL s456 BoolQ eval to align with RevKL 7-task format for Table 4 comparison. v2: run on westd-41718 where checkpoint is local (v1 SCP hung).\", \"parent\": \"perlayer_kl_30_s456_ppl\", \"conclusion\": \"success\", \"metrics\": {\"boolq_acc\": 0.5125}}, \"perlayer_kl_s123_downstream\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T19:09:40.716Z\", \"updated_at\": \"2026-05-21T21:27:53.906Z\", \"hypothesis\": \"Per-layer KL s123 downstream 7-task eval (ARC-c, WG, MMLU, GSM8K, HS, PIQA, BoolQ). s456 BoolQ=51.25% was significantly below RevKL s42 BoolQ=65.29%; need 3-seed data to confirm per-layer degradation pattern on downstream tasks.\", \"parent\": \"perlayer_kl_30_s123_v4\", \"conclusion\": \"failed\"}, \"perlayer_kl_s42_downstream\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T19:09:37.830Z\", \"updated_at\": \"2026-05-21T21:24:36.161Z\", \"hypothesis\": \"Per-layer KL s42 downstream 7-task eval (ARC-c, WG, MMLU, GSM8K, HS, PIQA, BoolQ). s456 BoolQ=51.25% was significantly below RevKL s42 BoolQ=65.29%; need 3-seed data to confirm per-layer degradation pattern on downstream tasks.\", \"parent\": \"perlayer_kl_30_s42_v6\", \"conclusion\": \"success\", \"metrics\": {\"arc_challenge_acc\": 0.3601, \"arc_challenge_acc_norm\": 0.3916, \"winogrande_acc\": 0.6527, \"mmlu_acc\": 0.3786, \"gsm8k_exact_match\": 0.0531, \"hellaswag_acc\": 0.4853, \"hellaswag_acc_norm\": 0.6763, \"piqa_acc\": 0.7361, \"piqa_acc_norm\": 0.7546, \"boolq_acc\": 0.7177}}, \"perlayer_kl_30_s42_v6\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T13:04:18.712Z\", \"updated_at\": \"2026-05-21T19:15:11.662Z\", \"hypothesis\": \"Per-layer KL training (each step masks only 1 random layer independently) will produce significantly worse PPL than end-to-end KL (8.81) when all 32 masks are applied simultaneously at inference, quantifying the value of cross-layer coupling in joint optimization. Restart with intermediate checkpointing to prevent progress loss from timeout kills.\", \"conclusion\": \"success\", \"metrics\": {\"steps\": 10000}}, \"perlayer_kl_30_s123_v4\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T13:04:21.493Z\", \"updated_at\": \"2026-05-21T19:15:09.357Z\", \"hypothesis\": \"Per-layer KL training (each step masks only 1 random layer independently) will produce significantly worse PPL than end-to-end KL (8.81) when all 32 masks are applied simultaneously at inference, quantifying the value of cross-layer coupling in joint optimization. Restart with intermediate checkpointing to prevent progress loss from timeout kills.\", \"conclusion\": \"success\", \"metrics\": {\"final_avg_kl\": 0.0114, \"final_tau\": 0.1, \"steps\": 10000}}, \"perlayer_kl_s123_ppl\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T19:09:39.333Z\", \"updated_at\": \"2026-05-21T19:13:48.108Z\", \"hypothesis\": \"Per-layer KL s123 PPL eval (wikitext2, seq_len 2048, uniform allocation, 30% sparsity). Expected PPL ~9.0 range based on s456=9.03. 3-seed mean needed for Table 4 coupling hierarchy comparison.\", \"parent\": \"perlayer_kl_30_s123_v4\", \"conclusion\": \"success\", \"metrics\": {\"wikitext2_ppl\": 9.0598}}, \"perlayer_kl_s42_ppl\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T19:09:35.080Z\", \"updated_at\": \"2026-05-21T19:13:45.686Z\", \"hypothesis\": \"Per-layer KL s42 PPL eval (wikitext2, seq_len 2048, uniform allocation, 30% sparsity). Expected PPL ~9.0 range based on s456=9.03. 3-seed mean needed for Table 4 coupling hierarchy comparison.\", \"parent\": \"perlayer_kl_30_s42_v6\", \"conclusion\": \"success\", \"metrics\": {\"wikitext2_ppl\": 9.0568}}, \"perlayer_kl_s456_boolq\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T14:43:45.621Z\", \"updated_at\": \"2026-05-21T17:25:02.422Z\", \"parent\": \"perlayer_kl_30_s456_ppl\", \"hypothesis\": \"Per-layer KL s456 BoolQ eval to align with RevKL 7-task format for Table 4 comparison. Checkpoint SCP from westd-41718.\", \"conclusion\": \"failed\"}, \"diag_eval_env_34887\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-21T15:26:22.732Z\", \"updated_at\": \"2026-05-21T15:26:22.732Z\"}, \"perlayer_kl_s456_ppl_repro\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-21T14:42:26.659Z\", \"updated_at\": \"2026-05-21T15:19:07.090Z\", \"hypothesis\": \"Reproducibility check: per-layer KL s456 PPL should match original 9.0282. Running with same checkpoint on different eval session to verify stability.\", \"parent\": \"perlayer_kl_30_s456_ppl\", \"conclusion\": \"success\", \"metrics\": {\"wikitext2_ppl\": 9.0282}}, \"diag_status_34887\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-21T15:17:19.912Z\", \"updated_at\": \"2026-05-21T15:17:19.912Z\"}, \"diag_status_41718\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-21T15:17:15.288Z\", \"updated_at\": \"2026-05-21T15:17:15.289Z\"}, \"revkl_30_s42_boolq\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T14:06:27.905Z\", \"updated_at\": \"2026-05-21T14:42:19.163Z\", \"hypothesis\": \"RevKL 30% s42 BoolQ eval to align with s123/s456 7-task format. Original reverse_kl_30_s42_uniform_eval only ran 6 tasks (missing BoolQ).\", \"parent\": \"reverse_kl_30_s42_uniform_eval\", \"metrics\": {\"boolq_acc\": 0.6529}, \"conclusion\": \"success\"}, \"read_boolq_results\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-21T14:41:36.074Z\", \"updated_at\": \"2026-05-21T14:41:36.074Z\"}, \"diag_ckpt_34887\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-21T14:40:48.364Z\", \"updated_at\": \"2026-05-21T14:40:48.364Z\"}, \"diag_ckpt_41718\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-21T14:40:44.587Z\", \"updated_at\": \"2026-05-21T14:40:44.587Z\"}, \"kill_old_34887\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-21T14:05:02.951Z\", \"updated_at\": \"2026-05-21T14:05:02.951Z\"}, \"kill_old_41718\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-21T14:04:59.665Z\", \"updated_at\": \"2026-05-21T14:04:59.665Z\"}, \"diag_34887_processes\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-21T14:03:38.179Z\", \"updated_at\": \"2026-05-21T14:03:38.180Z\"}, \"diag_41718_processes\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-21T14:03:34.154Z\", \"updated_at\": \"2026-05-21T14:03:34.154Z\"}, \"revkl_30_s456_downstream_v2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T04:53:55.143Z\", \"updated_at\": \"2026-05-21T14:02:24.499Z\", \"hypothesis\": \"RevKL 30% s456 downstream 7-task eval\", \"parent\": \"revkl_30_s456\", \"metrics\": {\"arc_challenge_acc_norm\": 0.4258, \"winogrande_acc\": 0.6788, \"mmlu_acc\": 0.42, \"gsm8k_exact_match\": 0.0614, \"hellaswag_acc_norm\": 0.704, \"piqa_acc_norm\": 0.7508, \"boolq_acc\": 0.5966}, \"conclusion\": \"success\"}, \"revkl_30_s123_downstream\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T02:59:47.275Z\", \"updated_at\": \"2026-05-21T14:02:15.372Z\", \"hypothesis\": \"RevKL 30% s123 downstream 7-task eval (arc_challenge, winogrande, mmlu, gsm8k, hellaswag, piqa, boolq) to supplement Table 4 with downstream metrics for coupling hierarchy comparison.\", \"parent\": \"revkl_30_s123\", \"metrics\": {\"arc_challenge_acc_norm\": 0.4556, \"winogrande_acc\": 0.689, \"mmlu_acc\": 0.38, \"gsm8k_exact_match\": 0.072, \"hellaswag_acc_norm\": 0.7092, \"piqa_acc_norm\": 0.7524, \"boolq_acc\": 0.7199}, \"conclusion\": \"success\"}, \"perlayer_kl_30_s456_downstream\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T09:23:09.217Z\", \"updated_at\": \"2026-05-21T13:18:10.566Z\", \"hypothesis\": \"Per-layer KL s456 downstream 6-task eval (ARC-c, WG, MMLU, GSM8K, HS, PIQA) at 30% uniform allocation. PPL gap is only +0.22 (9.03 vs 8.81); test if downstream task gap is also small, which would determine whether per-layer KL is a viable lightweight alternative or coupling is essential for downstream quality.\", \"parent\": \"perlayer_kl_30_s456_ppl\", \"metrics\": {\"arc_challenge_acc_norm\": 0.3848, \"winogrande_acc\": 0.663, \"mmlu_acc\": 0.3904, \"gsm8k_exact_match\": 0.0644, \"hellaswag_acc_norm\": 0.6616, \"piqa_acc_norm\": 0.7356}, \"conclusion\": \"success\"}, \"perlayer_kl_30_s456_ppl\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T07:36:38.887Z\", \"updated_at\": \"2026-05-21T09:21:04.571Z\", \"hypothesis\": \"Per-layer KL (each step trains only 1 random layer independently) PPL eval at 30% uniform allocation. If PPL >> end-to-end KL (8.81), proves cross-layer coupling is essential for optimal mask discovery.\", \"metrics\": {\"wikitext2_ppl\": 9.0282, \"model_level_sparsity\": 0.297}, \"conclusion\": \"success\"}, \"bce_iso_v3_s42_30pct_uniform_eval\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"created_at\": \"2026-05-21T00:07:15.639Z\", \"updated_at\": \"2026-05-21T08:08:00.000Z\", \"hypothesis\": \"BCE isocompute v3 seed 42 evaluated at 30% sparsity with uniform allocation, completing 3-seed set (s42/s123/s456) for Table 2 BCE 30% global† row multi-seed upgrade\", \"parent\": \"bce_isocompute_v3_s42\", \"metrics\": {\"ppl\": 14.947, \"arc_challenge\": 0.3294, \"winogrande\": 0.6062, \"mmlu\": 0.4291, \"gsm8k\": 0.0379, \"hellaswag\": 0.6165, \"piqa\": 0.7356}}, \"mse30_s123\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"created_at\": \"2026-05-21T01:20:27.976Z\", \"updated_at\": \"2026-05-21T08:00:00.000Z\", \"hypothesis\": \"MSE per-layer 30% seed 123 training + PPL-only eval (uniform allocation) for Table 4 coupling hierarchy multi-seed. MSE sits between RevKL and BCE in hierarchy (s42=20.43). Completing 3-seed validates this position.\", \"parent\": \"mse30_s42_train\", \"metrics\": {\"ppl\": 17.7313, \"sparsity\": 0.273, \"allocation\": \"uniform\"}}, \"mse30_s456\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"created_at\": \"2026-05-21T01:20:30.484Z\", \"updated_at\": \"2026-05-21T08:00:00.000Z\", \"hypothesis\": \"MSE per-layer 30% seed 456 training + PPL-only eval (uniform allocation) for Table 4 coupling hierarchy multi-seed. MSE sits between RevKL and BCE in hierarchy (s42=20.43). Completing 3-seed validates this position.\", \"parent\": \"mse30_s42_train\", \"metrics\": {\"ppl\": 17.3888, \"sparsity\": 0.28, \"allocation\": \"uniform\"}}, \"reverse_kl_30_s42_uniform_eval\": {\"status\": \"DONE\", \"created_at\": \"2026-05-21T07:42:41.949Z\", \"updated_at\": \"2026-05-21T07:43:19.290Z\", \"conclusion\": \"success\", \"metrics\": {\"arc_challenge_acc_norm\": 0.4283, \"winogrande_acc\": 0.7009, \"mmlu_acc\": 0.3749, \"gsm8k_exact_match\": 0.0697, \"hellaswag_acc_norm\": 0.6969, \"piqa_acc_norm\": 0.7459}, \"hypothesis\": \"Reverse KL 30% eval re-run with explicit --allocation uniform to fix Table 4 allocation consistency (D091). Original reverse_kl_30_s42 eval may have used default global_topk allocation; this re-run enforces uniform per-layer top-k matching the rest of the 30% section in Table 4.\"}, \"bce_iso_v3_s123_30pct_uniform_eval\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"created_at\": \"2026-05-20T22:48:20.128Z\", \"updated_at\": \"2026-05-21T06:50:00.000Z\", \"hypothesis\": \"BCE isocompute v3 seed 123 evaluated at 30% sparsity with uniform allocation for Table 2 multi-seed upgrade of BCE 30% global row\", \"metrics\": {\"ppl\": 15.2051, \"arc_challenge\": 0.3396, \"winogrande\": 0.6046, \"mmlu\": 0.4363, \"gsm8k\": 0.0455, \"hellaswag\": 0.614, \"piqa\": 0.7356}}, \"bce_iso_v3_s456_30pct_uniform_eval\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"created_at\": \"2026-05-20T22:48:22.518Z\", \"updated_at\": \"2026-05-21T06:50:00.000Z\", \"hypothesis\": \"BCE isocompute v3 seed 456 evaluated at 30% sparsity with uniform allocation for Table 2 multi-seed upgrade of BCE 30% global row\", \"metrics\": {\"ppl\": 15.1102, \"arc_challenge\": 0.3345, \"winogrande\": 0.6219, \"mmlu\": 0.4261, \"gsm8k\": 0.0356, \"hellaswag\": 0.6158, \"piqa\": 0.7323}}, \"teal_30pct_uniform_multiseed_eval\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"created_at\": \"2026-05-20T22:48:24.574Z\", \"updated_at\": \"2026-05-21T06:50:00.000Z\", \"hypothesis\": \"TEAL 30% uniform baseline multi-seed eval to verify TEAL results are deterministic (no predictor training, mask derived from model activations)\", \"metrics\": {\"ppl\": 10.8173, \"arc_challenge\": 0.3771, \"winogrande\": 0.6504, \"mmlu\": 0.4586, \"gsm8k\": 0.0879, \"hellaswag\": 0.6331, \"piqa\": 0.7198}}, \"perlayer_kl_30_s42_v5\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-21T04:59:08.935Z\", \"updated_at\": \"2026-05-21T04:59:17.600Z\", \"parent\": \"kl_30_s42\"}, \"revkl_30_s456_downstream\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-21T04:34:29.023Z\", \"updated_at\": \"2026-05-21T04:34:36.847Z\", \"hypothesis\": \"RevKL 30% s456 downstream 7-task eval (arc_challenge, winogrande, mmlu, gsm8k, hellaswag, piqa, boolq) to supplement Table 4 with downstream metrics for coupling hierarchy comparison.\", \"parent\": \"revkl_30_s456\"}, \"perlayer_kl_30_s42_v4\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-21T02:40:10.777Z\", \"updated_at\": \"2026-05-21T02:40:47.311Z\", \"hypothesis\": \"Per-layer KL training (each step masks only 1 random layer independently) will produce significantly worse PPL than end-to-end KL (8.81) when all 32 masks are applied simultaneously at inference. This gap quantifies the value of cross-layer coupling in joint optimization.\", \"parent\": \"kl_30_s42\"}, \"perlayer_kl_30_s456_v3\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-21T02:38:56.269Z\", \"updated_at\": \"2026-05-21T02:39:21.155Z\", \"hypothesis\": \"Per-layer KL training seed 456 for multi-seed validation. Expect PPL significantly worse than end-to-end KL (8.81), demonstrating coupling value.\", \"parent\": \"perlayer_kl_30_s42_v3\"}, \"perlayer_kl_30_s123_v3\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-21T02:38:53.244Z\", \"updated_at\": \"2026-05-21T02:39:18.221Z\", \"hypothesis\": \"Per-layer KL training seed 123 for multi-seed validation. Expect PPL significantly worse than end-to-end KL (8.81), demonstrating coupling value.\", \"parent\": \"perlayer_kl_30_s42_v3\"}, \"perlayer_kl_30_s42_v3\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-21T02:38:50.368Z\", \"updated_at\": \"2026-05-21T02:39:15.111Z\", \"hypothesis\": \"Per-layer KL training (each step masks only 1 random layer independently) will produce significantly worse PPL than end-to-end KL (8.81) when all 32 masks are applied simultaneously at inference. This gap quantifies the value of cross-layer coupling in joint optimization.\", \"parent\": \"kl_30_s42\"}, \"perlayer_kl_30_s456_v2\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-21T02:37:44.863Z\", \"updated_at\": \"2026-05-21T02:38:04.666Z\", \"hypothesis\": \"Per-layer KL training seed 456 for multi-seed validation. Expect similar PPL to s42 — both should be significantly worse than end-to-end KL (8.81), demonstrating coupling value.\", \"parent\": \"perlayer_kl_30_s42_v2\"}, \"perlayer_kl_30_s123_v2\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-21T02:37:41.877Z\", \"updated_at\": \"2026-05-21T02:38:03.190Z\", \"hypothesis\": \"Per-layer KL training seed 123 for multi-seed validation. Expect similar PPL to s42 — both should be significantly worse than end-to-end KL (8.81), demonstrating coupling value.\", \"parent\": \"perlayer_kl_30_s42_v2\"}, \"perlayer_kl_30_s42_v2\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-21T02:37:38.436Z\", \"updated_at\": \"2026-05-21T02:38:01.667Z\", \"hypothesis\": \"Per-layer KL training (each step masks only 1 random layer independently) will produce significantly worse PPL than end-to-end KL (8.81) when all 32 masks are applied simultaneously at inference. This gap quantifies the value of cross-layer coupling in joint optimization. [v2 restart after tmux session death]\", \"parent\": \"kl_30_s42\"}, \"perlayer_kl_30_s456\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-21T02:26:19.951Z\", \"updated_at\": \"2026-05-21T02:31:39.535Z\", \"hypothesis\": \"Per-layer KL training seed 456 for multi-seed validation. Expect similar PPL to s42 — both should be significantly worse than end-to-end KL (8.81), demonstrating coupling value.\", \"parent\": \"perlayer_kl_30_s42\"}, \"perlayer_kl_30_s123\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-21T02:26:18.396Z\", \"updated_at\": \"2026-05-21T02:27:10.709Z\", \"hypothesis\": \"Per-layer KL training seed 123 for multi-seed validation. Expect similar PPL to s42 — both should be significantly worse than end-to-end KL (8.81), demonstrating coupling value.\", \"parent\": \"perlayer_kl_30_s42\"}, \"perlayer_kl_30_s42\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-21T02:06:23.443Z\", \"updated_at\": \"2026-05-21T02:23:54.062Z\", \"hypothesis\": \"Per-layer KL training (each step masks only 1 random layer independently) will produce significantly worse PPL than end-to-end KL (8.81) when all 32 masks are applied simultaneously at inference. This gap quantifies the value of cross-layer coupling in joint optimization.\", \"parent\": \"kl_30_s42\"}, \"revkl_30_s456\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"created_at\": \"2026-05-21T00:14:02.472Z\", \"updated_at\": \"2026-05-21T02:01:00.000Z\", \"metrics\": {\"ppl\": 9.1841}, \"hypothesis\": \"Reverse KL 30% seed 456 training + PPL-only eval (uniform allocation) for Table 4 coupling hierarchy multi-seed upgrade. Expect PPL close to s42=9.31. Will run when a GPU frees up from the current 3 parallel jobs.\", \"parent\": \"reverse_kl_30_s42\"}, \"jsd_30_s123\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"created_at\": \"2026-05-21T00:13:18.525Z\", \"updated_at\": \"2026-05-21T01:25:00.000Z\", \"hypothesis\": \"JSD 30% seed 123 training + PPL-only eval (uniform allocation) for Table 4 coupling hierarchy multi-seed upgrade. Expect PPL close to s42=8.88.\", \"parent\": \"jsd_30_s42\", \"metrics\": {\"ppl\": 8.9144, \"sparsity\": 0.296, \"allocation\": \"uniform\"}}, \"jsd_30_s456\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"created_at\": \"2026-05-21T00:13:19.878Z\", \"updated_at\": \"2026-05-21T01:25:00.000Z\", \"hypothesis\": \"JSD 30% seed 456 training + PPL-only eval (uniform allocation) for Table 4 coupling hierarchy multi-seed upgrade. Expect PPL close to s42=8.88.\", \"parent\": \"jsd_30_s42\", \"metrics\": {\"ppl\": 8.9099, \"sparsity\": 0.296, \"allocation\": \"uniform\"}}, \"revkl_30_s123\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"created_at\": \"2026-05-21T00:13:21.127Z\", \"updated_at\": \"2026-05-21T01:25:00.000Z\", \"hypothesis\": \"Reverse KL 30% seed 123 training + PPL-only eval (uniform allocation) for Table 4 coupling hierarchy multi-seed upgrade. Expect PPL close to s42=9.31.\", \"parent\": \"reverse_kl_30_s42\", \"metrics\": {\"ppl\": 9.2859, \"sparsity\": 0.296, \"allocation\": \"uniform\"}}, \"bce_30_s42_uniform_eval\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"created_at\": \"2026-05-20T21:47:31.107Z\", \"updated_at\": \"2026-05-20T23:55:00.000Z\", \"hypothesis\": \"BCE 30% eval with explicit --allocation uniform to fill Table 4 30% BCE (no compensation) row, currently marked as dash\", \"parent\": \"bce_30pct_s42\", \"metrics\": {\"ppl\": 15.7069, \"arc_challenge\": 0.3319, \"winogrande\": 0.618, \"mmlu\": 0.4237, \"gsm8k\": 0.0394, \"hellaswag\": 0.6156, \"piqa\": 0.741}}, \"debug_check_bce_iso_ckpts\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-20T22:48:10.070Z\", \"updated_at\": \"2026-05-20T22:48:10.070Z\"}, \"debug_list_ckpts_34887\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-20T22:45:30.586Z\", \"updated_at\": \"2026-05-20T22:45:30.586Z\"}, \"debug_list_ckpts_41718\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-20T22:45:27.387Z\", \"updated_at\": \"2026-05-20T22:45:27.387Z\"}, \"debug_grep_bce_ppl\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-20T22:03:00.803Z\", \"updated_at\": \"2026-05-20T22:03:00.803Z\"}, \"debug_find_bce_ckpt_34887\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-20T22:00:39.077Z\", \"updated_at\": \"2026-05-20T22:00:39.077Z\"}, \"debug_read_revkl_results\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-20T21:45:30.439Z\", \"updated_at\": \"2026-05-20T21:45:30.439Z\"}, \"debug_find_revkl_logs\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-20T21:45:03.989Z\", \"updated_at\": \"2026-05-20T21:45:03.990Z\"}, \"revkl_30_s42_uniform_eval\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"created_at\": \"2026-05-20T19:51:26.599Z\", \"updated_at\": \"2026-05-20T21:15:00.000Z\", \"metrics\": {\"ppl\": 9.3081, \"arc_challenge\": 0.4283, \"winogrande\": 0.7009, \"mmlu\": 0.3749, \"gsm8k\": 0.0697, \"hellaswag\": 0.6969, \"piqa\": 0.7459}}, \"jsd_30_s42_uniform_eval\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"created_at\": \"2026-05-20T19:43:24.180Z\", \"updated_at\": \"2026-05-20T21:10:00.000Z\", \"hypothesis\": \"JSD 30% eval re-run with explicit --allocation uniform to fix Table 4 allocation consistency (D091)\", \"parent\": \"jsd_30_s42\", \"metrics\": {\"ppl\": 8.8848, \"arc_challenge\": 0.4437, \"winogrande\": 0.6977, \"mmlu\": 0.3857, \"gsm8k\": 0.0857, \"hellaswag\": 0.7063, \"piqa\": 0.7519}}, \"mse50_s123_eval_retry\": {\"status\": \"DONE\", \"conclusion\": \"killed\", \"created_at\": \"2026-05-20T20:55:02.443Z\", \"updated_at\": \"2026-05-20T20:55:02.443Z\"}, \"mse50_s123\": {\"status\": \"DONE\", \"conclusion\": \"negative\", \"metrics\": {\"final_loss\": 185.0, \"final_sparsity\": 0.051, \"note\": \"Native sparsity collapsed to 5.1% (target 50%). Eval PPL=15789 under forced 50% mask.\"}, \"created_at\": \"2026-05-20T18:56:40.578Z\", \"updated_at\": \"2026-05-20T18:57:12.696Z\", \"hypothesis\": \"MSE 50% seed 123 provides second seed for MSE baseline, confirming PPL>>KL is systematic not seed-dependent\", \"parent\": \"mse50_s42_eval_7task\"}, \"kl50_global_s456_eval\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T17:34:19.564Z\", \"updated_at\": \"2026-05-20T18:49:58.709Z\", \"hypothesis\": \"KL 50% global_topk allocation with seed 456 provides multi-seed evidence for global allocation advantage over uniform\", \"parent\": \"mvp_kl_norm_v2_s456\", \"conclusion\": \"success\", \"metrics\": {\"wikitext2_ppl\": 12.01, \"arc_challenge_acc_norm\": 0.369, \"winogrande_acc\": 0.64, \"mmlu_acc\": 0.28, \"gsm8k_exact_match\": 0.035, \"hellaswag_acc_norm\": 0.595, \"piqa_acc_norm\": 0.68}}, \"ste_30_s42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T16:31:52.815Z\", \"updated_at\": \"2026-05-20T18:36:14.452Z\", \"hypothesis\": \"STE relaxation at 30% sparsity underperforms Gumbel-Softmax, extending relaxation ablation to lower sparsity\", \"metrics\": {\"wikitext2_ppl\": 8.4138, \"arc_challenge_acc_norm\": 0.4846, \"winogrande_acc\": 0.7277, \"mmlu_acc\": 0.4395, \"gsm8k_exact_match\": 0.1676, \"hellaswag_acc_norm\": 0.7511, \"piqa_acc_norm\": 0.7726, \"model_level_sparsity\": 0.3}, \"conclusion\": \"success\"}, \"reverse_kl_30_s42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T15:52:08.516Z\", \"updated_at\": \"2026-05-20T18:05:21.883Z\", \"hypothesis\": \"Reverse KL at 30% sparsity underperforms forward KL, extending Table 4 ablation to lower sparsity regime\", \"metrics\": {\"wikitext2_ppl\": 9.31, \"arc_challenge_acc_norm\": 0.4317, \"winogrande_acc\": 0.6938, \"mmlu_acc\": 0.3744, \"gsm8k_exact_match\": 0.0697, \"hellaswag_acc_norm\": 0.6972, \"piqa_acc_norm\": 0.7459}, \"conclusion\": \"success\"}, \"jsd_30_s42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T15:51:54.005Z\", \"updated_at\": \"2026-05-20T18:05:20.630Z\", \"hypothesis\": \"JSD at 30% sparsity underperforms forward KL, extending Table 4 ablation to lower sparsity regime\", \"metrics\": {\"wikitext2_ppl\": 8.884, \"arc_challenge_acc_norm\": 0.4445, \"winogrande_acc\": 0.7072, \"mmlu_acc\": 0.3825, \"gsm8k_exact_match\": 0.0925, \"hellaswag_acc_norm\": 0.7073, \"piqa_acc_norm\": 0.7508, \"model_level_sparsity\": 0.285}, \"conclusion\": \"success\"}, \"mistral_kl30_s456\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T12:49:11.540Z\", \"updated_at\": \"2026-05-20T15:31:04.444Z\", \"hypothesis\": \"Mistral KL30 seed 456 replicates seed 42/123 results, providing 3-seed cross-arch evidence for KL advantage\", \"parent\": \"mistral_kl30_s123\", \"metrics\": {\"training_final_loss\": 0.105, \"training_final_sparsity\": 0.281, \"wikitext2_ppl\": 6.8752, \"arc_challenge_acc_norm\": 0.4684, \"winogrande_acc\": 0.7143, \"mmlu_acc\": 0.4161, \"gsm8k_exact_match\": 0.0697, \"hellaswag_acc_norm\": 0.705, \"piqa_acc_norm\": 0.7448}, \"conclusion\": \"success\"}, \"mistral_kl30_s123\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T12:17:54.631Z\", \"updated_at\": \"2026-05-20T15:08:10.846Z\", \"hypothesis\": \"Mistral-7B KL predictor at 30% sparsity with seed 123 reproduces s42 quality (PPL ~8.38), providing 2nd seed for cross-architecture robustness evidence\", \"metrics\": {\"training_final_loss\": 0.0996, \"training_final_sparsity\": 0.281, \"wikitext2_ppl\": 7.1491, \"arc_challenge_acc_norm\": 0.378, \"winogrande_acc\": 0.7017, \"mmlu_acc\": 0.4423, \"gsm8k_exact_match\": 0.0773, \"hellaswag_acc_norm\": 0.6961, \"piqa_acc_norm\": 0.7459}, \"conclusion\": \"success\"}, \"c4_ood_downstream_kl30\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T11:30:03.220Z\", \"updated_at\": \"2026-05-20T14:13:42.638Z\", \"hypothesis\": \"KL predictor trained on WikiText-103 maintains downstream task quality when mask predictions are generated from C4 OOD text, demonstrating domain-agnostic mask transfer\", \"metrics\": {\"arc_challenge_acc_norm\": 0.4036, \"winogrande_acc\": 0.693, \"mmlu_acc\": 0.4137, \"gsm8k_exact_match\": 0.0629, \"hellaswag_acc_norm\": 0.7074, \"piqa_acc_norm\": 0.7399, \"model_level_sparsity\": 0.295}, \"conclusion\": \"success\"}, \"c4_ood_kl30_s123\": {\"status\": \"DEPLOYED\", \"created_at\": \"2026-05-18T05:04:06.474Z\", \"updated_at\": \"2026-05-20T14:13:41.394Z\", \"hypothesis\": \"C4 OOD downstream seed 123 provides multi-seed robustness evidence for KL predictor under domain shift (Appendix D, D084)\", \"parent\": \"c4_ood_downstream_kl30\", \"conclusion\": \"killed\"}, \"bce_ste_s42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T11:30:01.125Z\", \"updated_at\": \"2026-05-20T13:25:33.780Z\", \"hypothesis\": \"BCE+STE combination fills the missing cell in the 2x2 loss×relaxation ablation matrix; if BCE+STE underperforms KL+Gumbel similarly to BCE+Gumbel, the loss function (not relaxation) is the dominant factor\", \"metrics\": {\"training_final_loss\": 0.641, \"training_final_bce\": 0.6398, \"training_final_sparsity\": 0.512, \"wikitext2_ppl\": 60.54, \"arc_challenge_acc_norm\": 0.2321, \"winogrande_acc\": 0.5185, \"mmlu_acc\": 0.2898, \"gsm8k_exact_match\": 0.0182, \"hellaswag_acc_norm\": 0.3446, \"piqa_acc_norm\": 0.6273, \"model_level_sparsity\": 0.495}, \"conclusion\": \"negative\"}, \"kl_sparsity40_s42_global_eval_v2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T09:27:11.182Z\", \"updated_at\": \"2026-05-20T12:39:20.119Z\", \"hypothesis\": \"40% KL predictor with global_topk allocation at sparsity_target=0.4 should achieve model-level sparsity ~0.38-0.42 and PPL comparable to the old 10.12; v1 eval omitted --sparsity_target causing 50% actual sparsity\", \"parent\": \"kl_sparsity40_s42_retrain_uniform\", \"conclusion\": \"success\", \"metrics\": {\"wikitext2_ppl\": 10.14, \"arc_challenge_acc_norm\": 0.3951, \"winogrande_acc\": 0.6748, \"mmlu_acc\": 0.3947, \"gsm8k_exact_match\": 0.066, \"hellaswag_acc_norm\": 0.6779, \"piqa_acc_norm\": 0.7269}}, \"kl_sparsity40_s42_uniform_hspiqa\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-20T09:28:45.384Z\", \"updated_at\": \"2026-05-20T10:53:46.011Z\", \"parent\": \"kl_sparsity40_s42_retrain_uniform\", \"conclusion\": \"success\", \"metrics\": {\"hellaswag_acc_norm\": 0.6497, \"piqa_acc_norm\": 0.7236, \"model_level_sparsity\": 0.397}}, \"kl_sparsity40_s42_global_eval\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-20T07:03:30.397Z\", \"updated_at\": \"2026-05-20T09:28:06.643Z\", \"hypothesis\": \"New 40% KL checkpoint (retrained with seed 42) produces consistent global-allocation PPL with the uniform eval, ensuring tab:phase_full 40% row uses same predictor for both allocation modes\", \"parent\": \"kl_sparsity40_s42_retrain_uniform\", \"conclusion\": \"failed\"}, \"kl_sparsity40_s42_retrain_uniform\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"created_at\": \"2026-05-20T05:30:07.319Z\", \"updated_at\": \"2026-05-20T06:50:00.000Z\", \"metrics\": {\"wikitext2_ppl\": 10.76, \"arc_challenge_acc_norm\": 0.3959, \"winogrande_acc\": 0.6306, \"mmlu_acc\": 0.355, \"gsm8k_acc\": 0.0356, \"training_final_loss\": 0.2598, \"training_final_sparsity\": 0.387}, \"hypothesis\": \"Retrain KL predictor at 40% sparsity + uniform allocation eval. Fills the missing 40% uniform data point in the regime curve (Table 4 / tab:phase_full appendix). Previous checkpoint deleted; global 40% exists (PPL=10.12) but uniform column is empty.\"}, \"mse30_s42_eval_7task\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"created_at\": \"2026-05-20T03:27:04.190Z\", \"updated_at\": \"2026-05-20T05:25:00.000Z\", \"metrics\": {\"wikitext2_ppl\": 20.43, \"arc_challenge_acc_norm\": 0.3123, \"winogrande_acc\": 0.6038, \"mmlu_acc\": 0.3179, \"gsm8k_exact_match\": 0.0197, \"hellaswag_acc_norm\": 0.5248, \"piqa_acc_norm\": 0.6937}, \"parent\": \"mse30_s42_train\", \"hypothesis\": \"MSE baseline 30% s42 full eval (PPL+ARC+WG+MMLU+GSM8K+HS+PIQA). Reviewer-requested intermediate baseline. If MSE significantly underperforms KL on downstream tasks while PPL is closer, validates distributional knowledge transfer > per-layer output matching.\"}, \"mse50_s42_eval_7task\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"created_at\": \"2026-05-20T03:52:14.884Z\", \"updated_at\": \"2026-05-20T05:25:00.000Z\", \"parent\": \"mse50_s42_train\", \"metrics\": {\"wikitext2_ppl\": 229.26, \"arc_challenge_acc_norm\": 0.25, \"winogrande_acc\": 0.5059, \"mmlu_acc\": 0.2379, \"gsm8k_exact_match\": 0.0159, \"hellaswag_acc_norm\": 0.2722, \"piqa_acc_norm\": 0.5577}, \"hypothesis\": \"MSE baseline 50% s42 full eval (PPL+ARC+WG+MMLU+GSM8K+HS+PIQA). Extends MSE comparison to 50% sparsity for Table 4. If MSE degrades proportionally more than KL at 50% vs 30%, demonstrates distributional advantage scales with sparsity.\"}, \"snr_full_curve_1000steps\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"created_at\": \"2026-05-20T03:59:14.041Z\", \"updated_at\": \"2026-05-20T05:25:00.000Z\", \"metrics\": {\"kl_snr_step0\": 1.3e-05, \"kl_snr_step300\": 0.0003465, \"kl_snr_step1000\": 0.0008777, \"bce_snr_step0\": 6.99e-05, \"bce_snr_step300\": 0.0017422, \"bce_snr_step1000\": 0.0020263, \"kl_bce_ratio_step1000\": 0.4332}, \"hypothesis\": \"Full 0-1000 step SNR trajectory for KL and BCE. Extends existing 0-300 data to complete training curve. N3 reviewer requires full trajectory. Key question: does KL maintain SNR advantage over BCE throughout training (step 300-1000), or does BCE catch up?\"}, \"qwen14b_teal30_global_hspiqa\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"created_at\": \"2026-05-20T02:32:52.201Z\", \"updated_at\": \"2026-05-20T03:50:00.000Z\", \"metrics\": {\"hellaswag_acc_norm\": 0.7051, \"piqa_acc_norm\": 0.747}, \"hypothesis\": \"14B TEAL 30% global (vanilla) HellaSwag+PIQA eval. 填 Table 5 TEAL global 行的 HS/PIQA 两个 \\\"---\\\" 格。\", \"parent\": \"qwen14b_teal30_eval\"}, \"qwen14b_bce30_global_hspiqa\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"created_at\": \"2026-05-20T02:32:54.713Z\", \"updated_at\": \"2026-05-20T03:50:00.000Z\", \"metrics\": {\"hellaswag_acc_norm\": 0.5343, \"piqa_acc_norm\": 0.6828}, \"hypothesis\": \"14B BCE 30% global HellaSwag+PIQA eval. 填 Table 5 BCE global 行的 HS/PIQA 两个 \\\"---\\\" 格。\", \"parent\": \"qwen14b_bce30_s42_eval\"}, \"mse50_s42_train\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"created_at\": \"2026-05-20T03:27:06.541Z\", \"updated_at\": \"2026-05-20T03:50:00.000Z\", \"metrics\": {\"final_loss\": 0.0083, \"final_sparsity\": 0.539, \"steps\": 1000}, \"hypothesis\": \"MSE baseline 50% sparsity training (s42). Extends MSE baseline to higher sparsity for Table 4 comparison. If MSE degrades more than KL at 50%, demonstrates KL's distributional advantage scales with sparsity.\"}, \"mse30_s42_train\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"created_at\": \"2026-05-20T02:39:15.431Z\", \"updated_at\": \"2026-05-20T03:26:00.000Z\", \"metrics\": {\"final_mse_loss\": 0.005735, \"final_constraint_loss\": 0.007294, \"final_total_loss\": 0.013, \"final_sparsity\": 0.277, \"final_tau\": 0.1, \"final_lambda\": 1000, \"steps\": 1000}, \"hypothesis\": \"Per-layer MSE loss baseline: ||down_proj(dense_act * mask) - down_proj(dense_act)||² trains predictor to minimize output reconstruction error per layer. Reviewer-requested \\\"Intermediate\\\" baseline comparing against KL (distribution-level) and BCE (binary classification) approaches. If MSE significantly underperforms KL, validates that distributional knowledge transfer > per-layer output matching for sparsity prediction.\"}, \"c4_ood_kl30_uniform_s42\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"created_at\": \"2026-05-20T03:12:45.778Z\", \"updated_at\": \"2026-05-20T03:26:00.000Z\", \"parent\": \"c4_ood_kl30_uniform_s123\", \"metrics\": {\"c4_ppl\": 18.2211, \"allocation\": \"uniform\", \"sparsity\": 0.296, \"seed\": 42}, \"hypothesis\": \"KL 30% uniform allocation C4 OOD PPL for s42. First seed completing 3-seed uniform C4 OOD data (s123=16.37, s456=16.36 done). W7 OOD statistical coverage requires all three seeds with uniform allocation.\"}, \"c4_ood_kl30_uniform_s456\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"created_at\": \"2026-05-20T03:08:49.787Z\", \"updated_at\": \"2026-05-20T03:11:30.000Z\", \"parent\": \"c4_ood_kl30_uniform_s123\", \"metrics\": {\"c4_ppl\": 16.3551, \"allocation\": \"uniform\", \"sparsity\": 0.3, \"seed\": 456}, \"hypothesis\": \"KL 30% uniform allocation C4 OOD PPL for s456. Third seed completing 3-seed uniform C4 OOD data (s42 pending, s123 running, s456 this). W7 OOD statistical coverage requires all three seeds with uniform allocation.\"}, \"c4_ood_kl30_uniform_s123\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"created_at\": \"2026-05-20T03:07:15.550Z\", \"updated_at\": \"2026-05-20T03:11:00.000Z\", \"parent\": \"c4_ood_kl30_s123_v2\", \"metrics\": {\"c4_ppl\": 16.3686, \"allocation\": \"uniform\", \"sparsity\": 0.3, \"seed\": 123}, \"hypothesis\": \"KL 30% uniform allocation C4 OOD PPL for s123. Supplements existing global-allocation C4 OOD data (s42/s123/s456 all global). Uniform allocation is the paper's primary protocol; W7 OOD claim needs 3-seed uniform data for consistency.\"}, \"qwen14b_kl30_global_hspiqa\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"created_at\": \"2026-05-20T01:39:41.918Z\", \"updated_at\": \"2026-05-20T03:00:00.000Z\", \"metrics\": {\"hellaswag_acc_norm\": 0.7501, \"piqa_acc_norm\": 0.7737}, \"hypothesis\": \"14B KL 30% global HellaSwag+PIQA eval. 填 Table 5 Global KL 行的 HS/PIQA 两个 \\\"---\\\" 格。\", \"parent\": \"qwen14b_kl30_s42_eval\"}, \"qwen14b_teal30_uniform_hspiqa\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T13:19:22.790Z\", \"updated_at\": \"2026-05-20T02:10:00.000Z\", \"hypothesis\": \"14B TEAL 30% uniform HellaSwag+PIQA eval. 填 Table 5 Uniform TEAL 行的 HS/PIQA 两个 \\\"---\\\" 格。重跑（前次被 killed）。\", \"parent\": \"qwen14b_teal30_uniform_eval_4task\", \"conclusion\": \"success\", \"metrics\": {\"hellaswag_acc_norm\": 0.6772, \"piqa_acc_norm\": 0.747}}, \"qwen14b_kl30_uniform_hspiqa\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T00:54:43.072Z\", \"updated_at\": \"2026-05-20T02:10:00.000Z\", \"conclusion\": \"success\", \"metrics\": {\"hellaswag_acc_norm\": 0.7266, \"piqa_acc_norm\": 0.7514}, \"hypothesis\": \"14B KL 30% uniform HellaSwag+PIQA eval. 填 Table 5 Uniform KL 行的 HS/PIQA 两个 \\\"---\\\" 格。\", \"parent\": \"qwen14b_kl30_uniform_eval_4task\"}, \"qwen14b_teal30_uniform_gsm8k\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T19:33:08.754Z\", \"updated_at\": \"2026-05-20T02:08:46.221Z\", \"hypothesis\": \"TEAL@30% uniform allocation GSM8K eval for Qwen-14B. Nominal-matched comparison for appendix table. Supplements existing TEAL@30% uniform 4-task + HS+PIQA data.\", \"parent\": \"qwen14b_teal30_uniform_eval_4task\", \"metrics\": {\"gsm8k_exact_match\": 0.5208, \"gsm8k_exact_match_strict\": 0.5208, \"gsm8k_exact_match_flexible\": 0.5208, \"gsm8k_exact_match_stderr\": 0.01376, \"actual_sparsity\": 0.293, \"sample_len\": 1319}, \"conclusion\": \"success\"}, \"bench_teal50_uniform_gsm8k\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T00:47:27.225Z\", \"updated_at\": \"2026-05-20T01:38:00.000Z\", \"conclusion\": \"success\", \"metrics\": {\"gsm8k_exact_match_flexible\": 0.0174}, \"hypothesis\": \"8B TEAL 50% uniform GSM8K eval. 补齐 Table 2 50% row GSM8K 数据，与 30% section 保持 uniform allocation 一致性。\", \"parent\": \"bench_teal50_uniform_6task\"}, \"bench_teal50_uniform_6task\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T23:59:08.076Z\", \"updated_at\": \"2026-05-20T00:52:00.000Z\", \"hypothesis\": \"8B TEAL 50% uniform 6-task eval. 修复 Table 2 50% section TEAL 从 global 改为 uniform，与 30% section 保持一致。\", \"conclusion\": \"success\", \"metrics\": {\"wikitext2_ppl\": 23.9, \"arc_challenge_acc_norm\": 0.2747, \"winogrande_acc\": 0.5438, \"mmlu_acc\": 0.2926, \"hellaswag_acc_norm\": 0.3935, \"piqa_acc_norm\": 0.6366}}, \"kl30_uniform_hspiqa_s456\": {\"status\": \"DONE\", \"created_at\": \"2026-05-20T00:06:11.383Z\", \"updated_at\": \"2026-05-20T00:45:00.000Z\", \"hypothesis\": \"8B KL 30% uniform s456 HellaSwag+PIQA eval. 补齐 3-seed HS/PIQA。\", \"parent\": \"kl30_uniform_hellaswag_piqa\", \"conclusion\": \"success\", \"metrics\": {\"hellaswag_acc_norm\": 0.7168, \"piqa_acc_norm\": 0.7524}}, \"kl30_uniform_hspiqa_s123\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T23:59:10.797Z\", \"updated_at\": \"2026-05-20T00:40:00.000Z\", \"hypothesis\": \"8B KL 30% uniform s123 HellaSwag+PIQA eval. 补齐 3-seed HS/PIQA。\", \"parent\": \"kl30_uniform_hellaswag_piqa\", \"conclusion\": \"success\", \"metrics\": {\"hellaswag_acc_norm\": 0.7067, \"piqa_acc_norm\": 0.7481}}, \"qwen14b_kl30_s456_gsm8k\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T18:22:31.492Z\", \"updated_at\": \"2026-05-20T00:02:43.659Z\", \"hypothesis\": \"KL s456 GSM8K supplement for Qwen-14B. Completes 3-seed GSM8K comparison. Required for complete 14B paper table.\", \"parent\": \"qwen14b_kl30_s456_eval_v3\", \"metrics\": {\"gsm8k_exact_match\": 0.2608, \"gsm8k_exact_match_stderr\": 0.01209, \"gsm8k_exact_match_strict\": 0.2547, \"gsm8k_exact_match_strict_stderr\": 0.012, \"actual_sparsity\": 0.297}, \"conclusion\": \"success\"}, \"c1_eval_30pct_s456\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T02:24:04.213Z\", \"updated_at\": \"2026-05-19T23:56:00.000Z\", \"hypothesis\": \"C1 ablation s456 complete eval at 30% sparsity uniform. 补齐 ARC 和 GSM8K，strengthens C1 multi-seed evidence at recommended operating point.\", \"parent\": \"c1_ablation_30pct_s456\", \"conclusion\": \"success\", \"metrics\": {\"wikitext2_ppl\": 8.9773, \"arc_challenge_acc_norm\": 0.4718, \"winogrande_acc\": 0.6882, \"mmlu_acc\": 0.3656, \"gsm8k_exact_match\": 0.0842}}, \"bench_teal30_uniform_6task\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T22:37:10.303Z\", \"updated_at\": \"2026-05-19T23:37:00.000Z\", \"hypothesis\": \"8B TEAL 30% uniform allocation 6-task eval (PPL, ARC, WG, MMLU, HS, PIQA). 补齐 Table 2 uniform 对照。\", \"parent\": \"bench_teal30\", \"conclusion\": \"success\", \"metrics\": {\"wikitext2_ppl\": 10.8173, \"arc_challenge_acc_norm\": 0.3933, \"winogrande_acc\": 0.6504, \"mmlu_acc\": 0.4586, \"hellaswag_acc_norm\": 0.6331, \"piqa_acc_norm\": 0.728, \"actual_sparsity\": 0.3}}, \"qwen14b_kl30_s42_gsm8k_v2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T17:52:58.669Z\", \"updated_at\": \"2026-05-19T22:53:23.576Z\", \"conclusion\": \"success\", \"metrics\": {\"gsm8k_exact_match\": 0.3571, \"gsm8k_exact_match_strict\": 0.3541, \"gsm8k_exact_match_stderr\": 0.0132, \"actual_sparsity\": 0.296, \"sample_len\": 1319}, \"hypothesis\": \"KL s42 GSM8K supplement for Qwen-14B (retry). Enables KL vs TEAL comparison on reasoning task. v1 killed due to GPU contention on 41718:1.\", \"parent\": \"qwen14b_kl30_s42_eval_uniform_v3\"}, \"bench_teal30_uniform_gsm8k\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T21:59:56.432Z\", \"updated_at\": \"2026-05-19T22:34:00.000Z\", \"hypothesis\": \"8B TEAL 30% uniform allocation GSM8K eval. 补齐 uniform 分配下的 TEAL baseline，与 KL 30% uniform (bench_kl30_uniform) 和 Dense (bench_dense) 做 GSM8K 三方对比。bench_teal30 用的是 global allocation，本实验用 uniform 保持分配策略一致。\", \"parent\": \"bench_teal30\", \"conclusion\": \"success\", \"metrics\": {\"gsm8k_exact_match\": 0.0879, \"actual_sparsity\": 0.3}}, \"bench_kl30_uniform_gsm8k_d075\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-19T21:02:45.729Z\", \"updated_at\": \"2026-05-19T21:02:45.729Z\"}, \"qwen14b_kl30_s123_gsm8k\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T18:22:30.203Z\", \"updated_at\": \"2026-05-19T20:56:54.196Z\", \"hypothesis\": \"KL s123 GSM8K supplement for Qwen-14B. Completes 3-seed GSM8K comparison (s42 running, s456 queued). Required for complete 14B paper table.\", \"parent\": \"qwen14b_kl30_s123_eval_v5\", \"conclusion\": \"success\", \"metrics\": {\"gsm8k_exact_match\": 0.3442, \"gsm8k_exact_match_strict\": 0.3434, \"actual_sparsity\": 0.297}}, \"qwen14b_kl30_s456_eval_v3\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T15:37:22.929Z\", \"updated_at\": \"2026-05-19T20:40:09.524Z\", \"hypothesis\": \"Qwen-14B KL s456 eval with D075 sigmoid fix + uniform allocation on westd-41718. Standard 6-task list. Re-run of v2 to verify on different server. Completing 3-seed comparison table.\", \"parent\": \"qwen14b_kl30_s456\", \"conclusion\": \"success\", \"metrics\": {\"wikitext2_ppl\": 7.8992, \"arc_challenge_acc_norm\": 0.5145, \"winogrande_acc\": 0.7316, \"hellaswag_acc_norm\": 0.7249, \"piqa_acc_norm\": 0.7677, \"mmlu_acc\": 0.6351, \"actual_sparsity\": 0.297}}, \"qwen14b_kl30_s123_eval_v5\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T15:12:25.174Z\", \"updated_at\": \"2026-05-19T20:40:08.018Z\", \"hypothesis\": \"Qwen-14B KL 30% s123 eval rerun with D075 sigmoid fix (teal_global_masks: sigmoid(logits) replaces degenerate mag*hard_mask) + uniform allocation on westd-41718 cuda:1. Completing multi-seed comparison table. v4 was pre-D075 on westd-34887.\", \"parent\": \"qwen14b_kl30_s123_eval_v4\", \"conclusion\": \"success\", \"metrics\": {\"wikitext2_ppl\": 7.9367, \"arc_challenge_acc_norm\": 0.541, \"winogrande_acc\": 0.7403, \"hellaswag_acc_norm\": 0.7287, \"piqa_acc_norm\": 0.765, \"mmlu_acc\": 0.6234, \"actual_sparsity\": 0.296}}, \"qwen14b_kl30_s42_eval_uniform_v3\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T14:22:33.970Z\", \"updated_at\": \"2026-05-19T20:40:06.557Z\", \"hypothesis\": \"Re-run of s42 eval after D075 evaluate.py teal_global_masks() fix. sigmoid(logits) replaces degenerate mag*hard_mask scoring for correct per-layer top-k neuron selection.\", \"parent\": \"qwen14b_kl30_s42_eval_uniform_v2\", \"conclusion\": \"success\", \"metrics\": {\"wikitext2_ppl\": 7.8715, \"arc_challenge_acc\": 0.5051, \"arc_challenge_acc_norm\": 0.5495, \"winogrande_acc\": 0.7127, \"mmlu_acc\": 0.648, \"hellaswag_acc_norm\": 0.7268, \"piqa_acc_norm\": 0.7476, \"actual_sparsity\": 0.296}}, \"qwen14b_dense_4task_v2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T17:48:38.383Z\", \"updated_at\": \"2026-05-19T20:36:53.074Z\", \"hypothesis\": \"Qwen-14B dense baseline remaining 4 tasks (wikitext2, arc_challenge, winogrande, mmlu). Retry of qwen14b_dense_4task which OOMed due to GSM8K orphan process. Orphan now killed.\", \"parent\": \"qwen14b_dense_baseline\", \"metrics\": {\"wikitext2_ppl\": 5.1854, \"arc_challenge_acc_norm\": 0.6758, \"winogrande_acc\": 0.8106, \"mmlu_acc\": 0.7977}, \"conclusion\": \"success\"}, \"qwen14b_teal275_uniform_eval_v3\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T14:39:28.152Z\", \"updated_at\": \"2026-05-19T20:28:54.153Z\", \"hypothesis\": \"TEAL@27.5% uniform baseline for sparsity-matched KL comparison on Qwen-14B. Fix: relaxed _uniform_topk_masks assert from 0.02 to 0.05 tolerance. Current tasks: wikitext2,arc,wg,mmlu,gsm8k. Missing hellaswag+piqa will supplement.\", \"parent\": \"qwen14b_teal275_uniform_eval_v2\", \"metrics\": {\"wikitext2_ppl\": 7.7087, \"arc_challenge_acc_norm\": 0.57, \"winogrande_acc\": 0.7167, \"mmlu_acc\": 0.6738, \"gsm8k_exact_match\": 0.5709}, \"conclusion\": \"success\"}, \"qwen14b_teal275_hspiqa\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T17:48:36.615Z\", \"updated_at\": \"2026-05-19T18:53:18.929Z\", \"hypothesis\": \"TEAL@27.5% uniform HellaSwag+PIQA supplement for Qwen-14B. Completes 6-task TEAL baseline alongside qwen14b_teal275_uniform_eval_v3 (wikitext2/arc/wg/mmlu/gsm8k).\", \"parent\": \"qwen14b_teal275_uniform_eval_v3\", \"conclusion\": \"success\", \"metrics\": {\"hellaswag_acc\": 0.5092, \"hellaswag_acc_norm\": 0.6993, \"piqa_acc\": 0.753, \"piqa_acc_norm\": 0.7476, \"model_sparsity\": 0.268, \"runtime_seconds\": 3551.3}}, \"qwen14b_dense_hspiqa\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T17:15:01.916Z\", \"updated_at\": \"2026-05-19T18:14:50.005Z\", \"hypothesis\": \"Qwen-14B dense baseline hellaswag+piqa supplement. Completing 6-task suite for 14B comparison table.\", \"parent\": \"qwen14b_dense_baseline\", \"conclusion\": \"success\", \"metrics\": {\"hellaswag_acc\": 0.6444, \"hellaswag_acc_norm\": 0.8421, \"piqa_acc\": 0.809, \"piqa_acc_norm\": 0.8194}}, \"qwen14b_kl30_s42_gsm8k\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T17:34:34.287Z\", \"updated_at\": \"2026-05-19T17:50:51.366Z\", \"hypothesis\": \"KL s42 GSM8K supplement for Qwen-14B. Enables KL vs TEAL comparison on reasoning task (Round 12 Q6).\", \"parent\": \"qwen14b_kl30_s42_eval_uniform_v3\", \"conclusion\": \"killed\"}, \"qwen14b_dense_4task\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T17:42:50.508Z\", \"updated_at\": \"2026-05-19T17:50:33.183Z\", \"hypothesis\": \"Qwen-14B dense baseline remaining 4 tasks (wikitext2, arc_challenge, winogrande, mmlu). Parallel with qwen14b_dense_hspiqa (HS+PIQA) on cuda:0 to complete full 6-task dense baseline for 14B comparison table.\", \"parent\": \"qwen14b_dense_baseline\", \"conclusion\": \"failed\", \"notes\": \"失败原因: CUDA OOM at MMLU loglikelihood stage. Process 163225 (orphaned child of killed gsm8k experiment PID 163224) held 61.77 GiB on cuda:1, leaving only 1.77 GiB free. lm_head forward pass needed 2.90 GiB allocation. | 已有成果: arc_challenge eval completed (~33%), wikitext2 completed. | 后续: v2 已自动重新提交 (PID 164330, westd-41718:cuda:1), orphan 已清理。\"}, \"flashinfer_benchmark_llama8b_v2\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-19T17:08:38.448Z\", \"updated_at\": \"2026-05-19T17:08:40.329Z\", \"hypothesis\": \"Wall-clock inference speedup: gather-matmul sparse FFN (30%/50% sparsity) vs dense on LLaMA-3.1-8B. Full-sparse path: all 3 projections (gate/up/down) use gathered weights. Addresses reviewer W3.\"}, \"flashinfer_benchmark_llama8b\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T17:05:25.529Z\", \"updated_at\": \"2026-05-19T17:08:31.111Z\", \"hypothesis\": \"Wall-clock inference speedup: gather-matmul sparse FFN (30%/50% sparsity) vs dense on LLaMA-3.1-8B. Full-sparse path: all 3 projections (gate/up/down) use gathered weights. Addresses reviewer W3.\", \"conclusion\": \"failed\"}, \"qwen14b_teal275_uniform_hspiqa\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T15:58:55.851Z\", \"updated_at\": \"2026-05-19T17:03:12.867Z\", \"conclusion\": \"success\", \"metrics\": {\"hellaswag_acc\": 0.5092, \"hellaswag_acc_norm\": 0.6993, \"piqa_acc\": 0.753, \"piqa_acc_norm\": 0.7476}, \"hypothesis\": \"TEAL@27.5% uniform sparsity on Qwen2.5-14B preserves hellaswag and piqa accuracy within acceptable degradation bounds, completing the 6-task evaluation suite for the 14B model comparison table.\"}, \"qwen14b_kl30_s456_eval_v2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T11:20:38.257Z\", \"updated_at\": \"2026-05-19T15:36:39.762Z\", \"hypothesis\": \"Qwen-14B KL s456 eval with D075 sigmoid fix + uniform allocation. Standard 6-task list. Completing 3-seed comparison table.\", \"parent\": \"qwen14b_kl30_s456\", \"metrics\": {\"wikitext2_ppl\": 7.6933, \"arc_challenge_acc\": 0.5051, \"arc_challenge_acc_norm\": 0.5324, \"winogrande_acc\": 0.723, \"mmlu_acc\": 0.6411, \"hellaswag_acc\": 0.5197, \"hellaswag_acc_norm\": 0.7113, \"piqa_acc\": 0.7421, \"piqa_acc_norm\": 0.7552, \"model_sparsity\": 0.275}, \"conclusion\": \"success\"}, \"qwen14b_teal30_uniform_hspiqa_v2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T14:25:23.976Z\", \"updated_at\": \"2026-05-19T15:31:08.241Z\", \"hypothesis\": \"TEAL 30% uniform on Qwen-14B HellaSwag+PIQA. Re-submit after erroneous kill (TEAL vanilla not affected by D075 bug).\", \"parent\": \"qwen14b_teal30_uniform_eval_4task\", \"conclusion\": \"success\", \"metrics\": {\"hellaswag_acc\": 0.4936, \"hellaswag_acc_norm\": 0.6756, \"piqa_acc\": 0.7443, \"piqa_acc_norm\": 0.7427}}, \"qwen14b_teal275_uniform_eval_v2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T14:25:22.236Z\", \"updated_at\": \"2026-05-19T14:33:35.288Z\", \"hypothesis\": \"TEAL@27.5% uniform baseline for sparsity-matched KL comparison. Re-submit after erroneous kill (TEAL vanilla not affected by D075 bug). Expect same results as original submission would have produced.\", \"parent\": \"qwen14b_teal30_uniform_eval_4task\", \"conclusion\": \"failed\"}, \"qwen14b_teal275_uniform_eval\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T13:47:12.391Z\", \"updated_at\": \"2026-05-19T14:16:24.757Z\", \"hypothesis\": \"TEAL@27.5% uniform baseline provides a fair sparsity-matched comparison for KL predictor (actual 27.5% due to Layer 1-4 zero sparsity). Expect similar or slightly different PPL/downstream vs TEAL@30% since 2.5pp less pruning.\", \"parent\": \"qwen14b_teal30_uniform_eval_4task\", \"conclusion\": \"killed\"}, \"qwen14b_kl30_s42_eval_uniform_v2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T13:23:44.297Z\", \"updated_at\": \"2026-05-19T14:16:22.737Z\", \"hypothesis\": \"Qwen-14B KL 30% s42 eval under TEAL uniform allocation will produce comparable downstream metrics to s123/s456 (also uniform), enabling valid 3-seed comparison. Retry of v1 which failed due to missing HF offline env vars (network unreachable). v2 adds HF_DATASETS_OFFLINE=1, TRANSFORMERS_OFFLINE=1, HF_HUB_OFFLINE=1.\", \"parent\": \"qwen14b_kl30_s42_eval_uniform\", \"conclusion\": \"killed\"}, \"qwen14b_kl30_s42_eval_uniform\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T13:13:51.678Z\", \"updated_at\": \"2026-05-19T13:44:20.478Z\", \"hypothesis\": \"Qwen-14B KL 30% s42 eval under TEAL uniform allocation will produce comparable downstream metrics to s123/s456 (also uniform), enabling valid 3-seed comparison. Prior s42 eval used global_topk (the default), making it inconsistent with s123/s456 which used uniform.\", \"parent\": \"qwen14b_kl30_s42\", \"conclusion\": \"failed\", \"notes\": \"失败原因: lm-eval 加载数据集时尝试访问 HF Hub，但服务器网络不通。Traceback: RuntimeError: Cannot send a request, as the client has been closed. 根因: 提交命令缺少 HF_DATASETS_OFFLINE=1 / TRANSFORMERS_OFFLINE=1 / HF_HUB_OFFLINE=1 环境变量。已知模式（memory.md）。v2 已准备，加了离线环境变量。\"}, \"qwen14b_kl30_s123\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T08:21:05.971Z\", \"updated_at\": \"2026-05-19T13:43:53.414Z\", \"hypothesis\": \"KL-normalized Lagrangian distillation at 30% sparsity target on Qwen2.5-14B (seed 123) will produce a predictor that achieves comparable downstream quality to dense baseline while pruning ~30% of SwiGLU intermediate activations.\", \"parent\": \"qwen14b_kl30_s42\", \"metrics\": {\"final_loss_kl_norm\": 0.326, \"final_kl_raw\": 0.326, \"final_sparsity\": 0.277, \"final_constraint\": 0.037, \"final_lambda\": 5000, \"final_tau\": 0.1, \"steps\": 1000, \"trainable_params\": \"117M (0.793%)\"}, \"conclusion\": \"success\"}, \"qwen14b_kl30_s123_eval_v4\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T11:25:23.513Z\", \"updated_at\": \"2026-05-19T13:05:52.694Z\", \"hypothesis\": \"Qwen-14B KL 30% s123 benchmark eval (WikiText-2 PPL + 5 downstream: ARC/WG/HS/PIQA/MMLU) with TEAL uniform allocation. Retry after v2/v3 OOM (caused by orphan PID 93142, now killed). Multi-seed replication to confirm MMLU reversal is systematic.\", \"parent\": \"qwen14b_kl30_s123\", \"metrics\": {\"wikitext2_ppl\": 7.6607, \"arc_challenge_acc\": 0.5222, \"arc_challenge_acc_norm\": 0.5606, \"winogrande_acc\": 0.7293, \"hellaswag_acc\": 0.5179, \"hellaswag_acc_norm\": 0.7132, \"piqa_acc\": 0.7388, \"piqa_acc_norm\": 0.7535, \"mmlu_acc\": 0.6449}, \"conclusion\": \"success\"}, \"qwen14b_kl30_s456\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T08:21:07.866Z\", \"updated_at\": \"2026-05-19T12:52:55.464Z\", \"hypothesis\": \"Qwen-14B KL 30% with seed 456 should replicate s42's MMLU reversal pattern (KL < TEAL on MMLU), confirming it is a systematic property of the loss function on this model family rather than seed-specific noise. Multi-seed replication strengthens W2 response about MMLU reversal being architecture-dependent.\", \"parent\": \"qwen14b_kl30_s42\", \"metrics\": {\"final_loss\": 0.3086, \"final_kl_norm\": 0.2715, \"final_sparsity\": 0.277, \"final_constraint\": 0.0366, \"final_lambda\": 5000, \"final_tau\": 0.1, \"training_steps\": 1000}, \"conclusion\": \"success\"}, \"qwen14b_kl30_s456_eval\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T08:41:23.198Z\", \"updated_at\": \"2026-05-19T11:28:16.323Z\", \"hypothesis\": \"Qwen-14B KL 30% s456 benchmark eval (WikiText-2 PPL + 6 downstream tasks) with TEAL uniform allocation at 30% sparsity. Multi-seed replication of qwen14b_kl30_s42 eval to confirm KL vs TEAL performance gap is systematic on Qwen-14B, not seed-specific noise.\", \"parent\": \"qwen14b_kl30_s456\", \"conclusion\": \"killed\"}, \"qwen14b_kl30_s123_eval\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T08:41:03.644Z\", \"updated_at\": \"2026-05-19T11:28:15.243Z\", \"hypothesis\": \"The qwen14b_kl30_s123 predictor at 30% TEAL uniform sparsity will maintain downstream benchmark performance (ARC, WinoGrande, HellaSwag, PIQA, MMLU, GSM8K) within acceptable degradation from the dense baseline.\", \"parent\": \"qwen14b_kl30_s123\", \"conclusion\": \"killed\"}, \"qwen14b_kl30_s123_eval_v3\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T11:24:01.513Z\", \"updated_at\": \"2026-05-19T11:25:18.056Z\", \"hypothesis\": \"Qwen-14B KL 30% s123 benchmark eval (WikiText-2 PPL + 5 downstream: ARC/WG/HS/PIQA/MMLU) with TEAL uniform allocation. Retry after v2 OOM. Multi-seed replication to confirm MMLU reversal is systematic.\", \"parent\": \"qwen14b_kl30_s123\", \"conclusion\": \"failed\"}, \"qwen14b_kl30_s123_eval_v2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T11:20:36.444Z\", \"updated_at\": \"2026-05-19T11:23:55.893Z\", \"hypothesis\": \"Qwen-14B KL 30% s123 benchmark eval (WikiText-2 PPL + 5 downstream: ARC/WG/HS/PIQA/MMLU) with TEAL uniform allocation. Multi-seed replication to confirm MMLU reversal is systematic. GSM8K excluded due to generate_until cost on 14B.\", \"parent\": \"qwen14b_kl30_s123\", \"conclusion\": \"failed\"}, \"teal_28.5pct_sanity\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T06:52:16.546Z\", \"updated_at\": \"2026-05-19T07:47:00.307Z\", \"hypothesis\": \"TEAL vanilla at 28.5% sparsity (matching KL predictor's actual achieved sparsity) produces similar PPL to TEAL at 30%, confirming the 1.5pp sparsity gap does not meaningfully affect the KL vs TEAL comparison. If PPL difference is < 0.1, the comparison is fair.\", \"metrics\": {\"wikitext2_ppl\": 10.3}, \"conclusion\": \"success\"}, \"mistral_dense_hellaswag_piqa\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T06:19:17.368Z\", \"updated_at\": \"2026-05-19T07:43:18.197Z\", \"hypothesis\": \"Mistral-7B-v0.3 Dense baseline on HellaSwag (10-shot) and PIQA (0-shot). Required to complete Dense row in tab:mistral_downstream. Parent: lm_eval_mistral_dense.\", \"parent\": \"lm_eval_mistral_dense\", \"metrics\": {\"hellaswag_acc_norm\": 0.832, \"piqa_acc_norm\": 0.8188}, \"conclusion\": \"success\"}, \"bce_gumbel_no_penalty_s42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T06:54:15.611Z\", \"updated_at\": \"2026-05-19T07:19:51.533Z\", \"hypothesis\": \"BCE+Gumbel without adaptive penalty controller isolates the effect of Gumbel relaxation from Lagrangian sparsity control. If PPL degrades significantly vs bce_gumbel_lagrangian_isolation (38.02), penalty controller is necessary; if similar, Gumbel alone suffices.\", \"parent\": \"bce_gumbel_lagrangian_isolation\", \"metrics\": {\"training_bce_loss\": 0.6307, \"training_sparsity\": 0.383, \"wikitext2_ppl\": 32.22, \"training_time_seconds\": 977.6}, \"conclusion\": \"success\"}, \"qwen14b_mask_divergence_analysis\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T06:55:58.629Z\", \"updated_at\": \"2026-05-19T07:02:59.470Z\", \"hypothesis\": \"Per-layer Jaccard divergence between KL-predicted and magnitude-based masks on Qwen-14B reveals whether cross-scale models exhibit similar layer-wise importance disagreement patterns as LLaMA-8B. Higher divergence at specific layers indicates the predictor discovers non-trivial importance patterns beyond magnitude.\", \"metrics\": {\"qwen14b_mean_jaccard\": 0.4016, \"qwen14b_std_jaccard\": 0.0756, \"qwen14b_max_jaccard\": 0.446, \"qwen14b_max_layer\": 11, \"qwen14b_min_jaccard\": 0.0627, \"qwen14b_min_layer\": 4, \"llama8b_mean_jaccard\": 0.3939, \"llama8b_std_jaccard\": 0.0314, \"llama8b_max_jaccard\": 0.4818, \"llama8b_max_layer\": 0, \"llama8b_min_jaccard\": 0.3528, \"llama8b_min_layer\": 14}, \"conclusion\": \"success\"}, \"mistral_kl30_hellaswag_piqa\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T05:11:30.999Z\", \"updated_at\": \"2026-05-19T05:51:17.403Z\", \"hypothesis\": \"KL 30% predictor on Mistral-7B evaluated on HellaSwag (10-shot) and PIQA (0-shot) with TEAL uniform allocation. Completes the 7-task Mistral comparison table (KL vs TEAL). TEAL 30% baseline: HS=60.1%, PIQA=72.1%. Required for W2 cross-architecture claim.\", \"parent\": \"mistral_kl30_downstream\", \"conclusion\": \"success\", \"metrics\": {\"hellaswag_acc_norm\": 0.6892, \"piqa_acc_norm\": 0.7519}}, \"eval_c1_retrain_30pct_s456\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T03:38:44.698Z\", \"updated_at\": \"2026-05-19T05:20:06.906Z\", \"metrics\": {\"wikitext2_ppl\": 8.82, \"arc_challenge_acc_norm\": 0.4471, \"winogrande_acc\": 0.6993, \"mmlu_acc\": 0.4104, \"gsm8k_exact_match\": 0.066}, \"hypothesis\": \"C1 retrain eval s456: BCE predictor trained on kl_30pct_s456 oracle (matching main table) evaluated at 30% TEAL uniform. Eliminates oracle inconsistency between C1 ablation table and main results table.\", \"conclusion\": \"success\"}, \"eval_c1_retrain_30pct_s123\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T03:38:41.759Z\", \"updated_at\": \"2026-05-19T05:20:05.795Z\", \"metrics\": {\"wikitext2_ppl\": 8.84, \"arc_challenge_acc_norm\": 0.4471, \"winogrande_acc\": 0.6977, \"mmlu_acc\": 0.3992, \"gsm8k_exact_match\": 0.0682}, \"hypothesis\": \"C1 retrain eval s123: BCE predictor trained on kl_30pct_s123 oracle (matching main table) evaluated at 30% TEAL uniform. Eliminates oracle inconsistency between C1 ablation table and main results table.\", \"conclusion\": \"success\"}, \"c1_retrain_30pct_s456\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T03:22:36.158Z\", \"updated_at\": \"2026-05-19T05:06:43.280Z\", \"metrics\": {\"training_agreement\": 0.977, \"training_sparsity\": 0.312, \"wikitext2_ppl\": 7.38, \"actual_sparsity\": 0.346}, \"hypothesis\": \"C1 retrain training s456: Train BCE predictor using kl_30pct_s456 oracle masks (consistent with main table), replacing kl_sparsity30_s456. Eliminates reviewer attack surface on oracle inconsistency.\", \"conclusion\": \"success\"}, \"c1_retrain_30pct_s123\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T03:22:33.404Z\", \"updated_at\": \"2026-05-19T05:06:41.273Z\", \"metrics\": {\"training_agreement\": 0.977, \"training_sparsity\": 0.31, \"wikitext2_ppl\": 7.54, \"actual_sparsity\": 0.332}, \"hypothesis\": \"C1 retrain training s123: Train BCE predictor using kl_30pct_s123 oracle masks (consistent with main table), replacing kl_sparsity30_s123. Eliminates reviewer attack surface on oracle inconsistency.\", \"conclusion\": \"success\"}, \"mistral_teal50_downstream\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T03:15:46.635Z\", \"updated_at\": \"2026-05-19T05:06:39.140Z\", \"hypothesis\": \"Training-free TEAL 50% uniform allocation baseline on Mistral-7B for downstream tasks (PPL + ARC + WG + MMLU + GSM8K + HellaSwag + PIQA). Completes cross-architecture sparsity regime comparison alongside KL 50% results. Required for W2 cross-architecture claim.\", \"metrics\": {\"wikitext2_ppl\": 18.3061, \"arc_challenge_acc_norm\": 0.2457, \"winogrande_acc\": 0.5091, \"mmlu_acc\": 0.2635, \"gsm8k_exact_match\": 0.0341, \"hellaswag_acc_norm\": 0.3603, \"piqa_acc_norm\": 0.6045}, \"conclusion\": \"success\"}, \"mistral_teal30_downstream\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T03:15:45.662Z\", \"updated_at\": \"2026-05-19T05:06:37.120Z\", \"hypothesis\": \"Training-free TEAL 30% uniform allocation baseline on Mistral-7B for downstream tasks (PPL + ARC + WG + MMLU + GSM8K + HellaSwag + PIQA). Without this TEAL baseline, Mistral cross-architecture comparison cannot isolate KL predictor improvement from TEAL inherent capability. Required for W2 cross-architecture claim.\", \"metrics\": {\"wikitext2_ppl\": 8.3807, \"arc_challenge_acc_norm\": 0.4113, \"winogrande_acc\": 0.6354, \"mmlu_acc\": 0.4348, \"gsm8k_exact_match\": 0.1592, \"hellaswag_acc_norm\": 0.6011, \"piqa_acc_norm\": 0.7214}, \"conclusion\": \"success\"}, \"c1_ablation_30pct_s456\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T02:07:23.205Z\", \"updated_at\": \"2026-05-19T03:15:21.487Z\", \"hypothesis\": \"C1 causal ablation at 30% sparsity seed 456: BCE predictor trained on KL-derived oracle masks should reproduce KL quality (max Δ ≤ 2pp downstream), confirming target quality drives KL advantage across seeds. Multi-seed validation strengthens C1 claim.\", \"metrics\": {\"wikitext2_ppl\": 8.84, \"mmlu_acc\": 0.367, \"winogrande_acc\": 0.6938}, \"conclusion\": \"success\"}, \"c1_ablation_30pct_s123\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T02:07:21.635Z\", \"updated_at\": \"2026-05-19T03:15:19.324Z\", \"hypothesis\": \"C1 causal ablation at 30% sparsity seed 123: BCE predictor trained on KL-derived oracle masks should reproduce KL quality (max Δ ≤ 2pp downstream), confirming target quality drives KL advantage across seeds. Multi-seed validation strengthens C1 claim.\", \"metrics\": {\"wikitext2_ppl\": 8.83, \"mmlu_acc\": 0.3833, \"winogrande_acc\": 0.7119}, \"conclusion\": \"success\"}, \"mistral_kl30_downstream\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T02:07:32.697Z\", \"updated_at\": \"2026-05-19T03:14:27.156Z\", \"hypothesis\": \"KL 30% predictor on Mistral-7B evaluated on downstream tasks (ARC, WG, MMLU, GSM8K) with TEAL uniform allocation. Dense Mistral baseline: ARC=60.2%, WG=78.7%, MMLU=62.4%, GSM8K=36.5%. Supports W2 cross-architecture downstream claim.\", \"metrics\": {\"arc_challenge_acc_norm\": 0.5017, \"winogrande_acc\": 0.6914, \"mmlu_acc\": 0.4404, \"gsm8k_exact_match\": 0.1114}, \"conclusion\": \"success\"}, \"bce_50pct_teal_global_unified\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T02:07:25.925Z\", \"updated_at\": \"2026-05-19T03:14:25.300Z\", \"hypothesis\": \"BCE iso-compute predictor evaluated at 50% TEAL global_topk on unified protocol (PPL + 4 downstream tasks). Provides fair BCE comparison at 50% using same eval protocol as KL experiments. Supports N3 fair BCE comparison claim.\", \"metrics\": {\"wikitext2_ppl\": 27.97, \"arc_challenge_acc_norm\": 0.2765, \"winogrande_acc\": 0.5162, \"mmlu_acc\": 0.2614, \"gsm8k_exact_match\": 0.019}, \"conclusion\": \"success\"}, \"bce_isocompute_hellaswag_piqa_v2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T01:08:16.119Z\", \"updated_at\": \"2026-05-19T02:32:57.874Z\", \"hypothesis\": \"BCE iso-compute predictor evaluated on HellaSwag (10-shot) and PIQA (0-shot) with TEAL uniform 30% completes the BCE row in the 6-task downstream table. Expected to show larger degradation than KL 30% (hellaswag=70.85%, piqa=74.81%). V2: submit on 34887 where checkpoint exists (M026 lesson).\", \"metrics\": {\"hellaswag_acc_norm\": 0.6281, \"piqa_acc_norm\": 0.7421}, \"conclusion\": \"success\"}, \"c1_ablation_30pct_eval_34887\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T01:27:54.967Z\", \"updated_at\": \"2026-05-19T01:38:57.451Z\", \"hypothesis\": \"C1@30% eval on 34887 where checkpoint exists. TEAL uniform 30%, PPL+ARC+WinoGrande+MMLU+GSM8K. Compare vs KL 30% uniform (PPL=8.82, ARC=50.3%, Wino=72.1%, MMLU=44.8%, GSM8K=14.3%).\", \"parent\": \"c1_ablation_30pct_s42_v2\", \"conclusion\": \"killed\"}, \"kl30_uniform_hellaswag_piqa\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T23:12:05.345Z\", \"updated_at\": \"2026-05-19T01:37:12.599Z\", \"hypothesis\": \"KL 30% uniform predictor should maintain near-dense performance on HellaSwag (10-shot) and PIQA (0-shot) at the recommended 30% operating point, consistent with graceful degradation observed on ARC/Winogrande/MMLU/GSM8K. Broadens downstream coverage from 4 to 6 tasks.\", \"conclusion\": \"success\", \"metrics\": {\"hellaswag_acc_norm\": 0.7085, \"piqa_acc_norm\": 0.7481, \"note\": \"from v2 retry\"}}, \"kl50_global_hellaswag_piqa\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T23:12:07.411Z\", \"updated_at\": \"2026-05-19T01:37:11.562Z\", \"hypothesis\": \"KL 50% global predictor HellaSwag/PIQA establishes upper-bound degradation at high sparsity. Expected to show larger drops than 30% but still meaningful retention, completing the 6-task regime curve at 50% sparsity.\", \"conclusion\": \"success\", \"metrics\": {\"hellaswag_acc_norm\": 0.5895, \"piqa_acc_norm\": 0.6948, \"note\": \"from v2 retry\"}}, \"kl50_uniform_hellaswag_piqa\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T00:30:56.542Z\", \"updated_at\": \"2026-05-19T01:36:35.995Z\", \"hypothesis\": \"KL 50% uniform predictor HellaSwag/PIQA completes the P1 table: uniform allocation at high sparsity. Expected to show moderate degradation from dense, less severe than global_topk (which had hellaswag=58.95%, piqa=69.48%).\", \"metrics\": {\"hellaswag_acc_norm\": 0.5666, \"piqa_acc_norm\": 0.691}, \"conclusion\": \"success\"}, \"c1_ablation_30pct_s42_eval_v2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T00:32:20.594Z\", \"updated_at\": \"2026-05-19T01:34:04.236Z\", \"hypothesis\": \"C1@30% eval on 34887 (checkpoint confirmed there). PPL already measured: 9.4463. Running full downstream (ARC, WinoGrande, MMLU, GSM8K) with TEAL uniform 30%.\", \"parent\": \"c1_ablation_30pct_s42_v2\", \"metrics\": {\"wikitext2_ppl\": 9.4463, \"arc_challenge_acc_norm\": 0.4027, \"winogrande_acc\": 0.674, \"mmlu_acc\": 0.4229, \"gsm8k_exact_match\": 0.0758}, \"conclusion\": \"success\"}, \"c1_ablation_30pct_s42_v2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T00:23:44.772Z\", \"updated_at\": \"2026-05-19T01:32:24.856Z\", \"hypothesis\": \"C1 causal ablation at 30% sparsity: BCE predictor trained on KL-derived oracle masks should achieve similar PPL and downstream metrics as KL predictor, demonstrating target quality (not gradient coupling) drives KL advantage. V2: fixed script path (train_bce_kl_targets.py exists on 41718 not 34887).\", \"parent\": \"c1_ablation_30pct_s42\", \"metrics\": {\"agreement\": 0.975}, \"conclusion\": \"success\"}, \"dense_baseline_hellaswag_piqa\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T00:04:50.389Z\", \"updated_at\": \"2026-05-19T01:32:20.749Z\", \"hypothesis\": \"Dense LLaMA-3.1-8B baseline on HellaSwag and PIQA establishes reference performance for the 6-task downstream evaluation suite. Required to compute degradation percentages for sparse predictors on these two new tasks.\", \"metrics\": {\"hellaswag_acc_norm\": 0.8235, \"piqa_acc_norm\": 0.809}, \"conclusion\": \"success\"}, \"bce_isocompute_hellaswag_piqa\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T00:34:52.111Z\", \"updated_at\": \"2026-05-19T01:08:09.261Z\", \"hypothesis\": \"BCE iso-compute predictor evaluated on HellaSwag+PIQA with TEAL uniform 30% completes the BCE row in the 6-task downstream table. Expected to show larger degradation than KL 30% (which had hellaswag=70.85%, piqa=74.81%).\", \"conclusion\": \"failed\"}, \"c1_ablation_30pct_s42_eval\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T00:27:36.305Z\", \"updated_at\": \"2026-05-19T00:32:18.584Z\", \"hypothesis\": \"C1@30% eval: BCE predictor trained on KL oracle masks at 30% sparsity should achieve PPL and downstream metrics close to KL 30% uniform (PPL=8.82, ARC=50.3%, Wino=72.1%, MMLU=44.8%, GSM8K=14.3%), confirming target quality drives KL advantage at the recommended operating point.\", \"parent\": \"c1_ablation_30pct_s42_v2\", \"conclusion\": \"failed\"}, \"kl50_global_hellaswag_piqa_v2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T23:27:29.696Z\", \"updated_at\": \"2026-05-19T00:29:56.105Z\", \"hypothesis\": \"KL 50% global predictor HellaSwag/PIQA establishes upper-bound degradation at high sparsity. Expected to show larger drops than 30% but still meaningful retention, completing the 6-task regime curve at 50% sparsity. V2: retry after fixing HF dataset cache.\", \"parent\": \"kl50_global_hellaswag_piqa\", \"metrics\": {\"hellaswag_acc_norm\": 0.5895, \"piqa_acc_norm\": 0.6948}, \"conclusion\": \"success\"}, \"kl30_uniform_hellaswag_piqa_v2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T23:27:28.149Z\", \"updated_at\": \"2026-05-19T00:29:54.134Z\", \"hypothesis\": \"KL 30% uniform predictor should maintain near-dense performance on HellaSwag (10-shot) and PIQA (0-shot) at the recommended 30% operating point, consistent with graceful degradation observed on ARC/Winogrande/MMLU/GSM8K. Broadens downstream coverage from 4 to 6 tasks. V2: retry after fixing HF dataset cache (hellaswag+piqa now pre-downloaded).\", \"parent\": \"kl30_uniform_hellaswag_piqa\", \"metrics\": {\"hellaswag_acc_norm\": 0.7085, \"piqa_acc_norm\": 0.7481}, \"conclusion\": \"success\"}, \"kl30_s42_global_mmlu_recheck\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T23:25:44.731Z\", \"updated_at\": \"2026-05-19T00:03:53.079Z\", \"hypothesis\": \"s42 global 30% MMLU=25.3% is an anomalous outlier (vs s123=38.1%, s456=43.8%) likely due to eval instability rather than predictor quality, since PPL is consistent across seeds (8.93-8.98). Rerunning with identical protocol should either reproduce the low score (confirming seed-specific MMLU sensitivity) or show a normal score (confirming eval noise).\", \"parent\": \"kl30_s42_global_v3\", \"metrics\": {\"mmlu_acc\": 0.2527, \"mmlu_stderr\": 0.00364}, \"conclusion\": \"success\"}, \"c1_ablation_30pct_s42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T23:25:43.181Z\", \"updated_at\": \"2026-05-19T00:03:46.334Z\", \"hypothesis\": \"C1 causal ablation at 30% sparsity (recommended operating point): BCE predictor trained on KL-derived oracle masks should achieve similar PPL and downstream metrics as the KL predictor at 30%, demonstrating that KL's advantage comes from mask quality (target effect) rather than gradient coupling. At 30% where downstream metrics are well-preserved, C1 should show smaller gaps than at 50% where degradation was severe.\", \"parent\": \"c1_ablation_s42\", \"conclusion\": \"failed\"}, \"kl30_s456_global_v3\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T22:12:57.454Z\", \"updated_at\": \"2026-05-18T23:11:50.581Z\", \"hypothesis\": \"KL 30% predictor (seed 456) global_topk eval on westd-34887 with unified protocol. Resolves MMLU contradiction (27.1% on 41718 vs 43.8% on 34887 in prior runs). Expect PPL ~8.93 consistent with s42 (8.98) and s123.\", \"parent\": \"bench_kl30_global\", \"conclusion\": \"success\", \"metrics\": {\"wikitext2_ppl\": 8.9332, \"arc_challenge_acc_norm\": 0.4633, \"winogrande_acc\": 0.7111, \"mmlu_acc\": 0.4382, \"gsm8k_exact_match\": 0.0758, \"actual_sparsity\": 0.3, \"allocation\": \"global_topk\"}}, \"kl30_s123_global_v3\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T22:12:55.969Z\", \"updated_at\": \"2026-05-18T23:11:49.677Z\", \"hypothesis\": \"KL 30% predictor (seed 123) global_topk eval on westd-34887 with unified protocol. Resolves cross-server MMLU inconsistency (41718 vs 34887 checkpoint/eval differences). Expect PPL ~8.93 consistent with s42 (8.98) and s456.\", \"parent\": \"bench_kl30_global\", \"conclusion\": \"success\", \"metrics\": {\"wikitext2_ppl\": 8.9748, \"arc_challenge_acc_norm\": 0.4531, \"winogrande_acc\": 0.693, \"mmlu_acc\": 0.3807, \"gsm8k_exact_match\": 0.0758, \"actual_sparsity\": 0.3, \"allocation\": \"global_topk\"}}, \"kl30_s456_uniform_v3\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T13:53:04.002Z\", \"updated_at\": \"2026-05-18T21:36:19.800Z\", \"hypothesis\": \"KL 30% predictor (seed 456) with uniform allocation produces consistent PPL and downstream metrics with s42 baseline (PPL=8.82), enabling mean±std reporting at the recommended 30% operating point. V3 runs on westd-34887 for server-consistent comparison.\", \"conclusion\": \"success\", \"notes\": \"Resubmitted per Director instruction (v2 had no metrics in registry). Running on westd-34887:1 for server-consistent comparison with bench_kl30_uniform (s42).\", \"parent\": \"bench_kl30_uniform\", \"metrics\": {\"wikitext2_ppl\": 8.7947, \"arc_challenge_acc_norm\": 0.4505, \"winogrande_acc\": 0.6875, \"mmlu_acc\": 0.4198, \"gsm8k_exact_match\": 0.0758, \"actual_sparsity\": 0.3, \"allocation\": \"uniform\", \"eval_wall_time_sec\": 2325.3}}, \"kl30_s123_uniform_v3\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T13:53:02.649Z\", \"updated_at\": \"2026-05-18T21:36:18.318Z\", \"hypothesis\": \"KL 30% predictor (seed 123) with uniform allocation produces consistent PPL and downstream metrics with s42 baseline (PPL=8.82), enabling mean±std reporting at the recommended 30% operating point. V3 runs on westd-34887 for server-consistent comparison.\", \"conclusion\": \"success\", \"notes\": \"Resubmitted per Director instruction (v2 had no metrics in registry). Running on westd-34887:0 for server-consistent comparison with bench_kl30_uniform (s42).\", \"parent\": \"bench_kl30_uniform\", \"metrics\": {\"wikitext2_ppl\": 8.8308, \"arc_challenge_acc_norm\": 0.4531, \"winogrande_acc\": 0.6938, \"mmlu_acc\": 0.3944, \"gsm8k_exact_match\": 0.0751, \"actual_sparsity\": 0.3, \"allocation\": \"uniform\", \"eval_wall_time_sec\": 2157.6}}, \"wallclock_speedup_30_50\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T15:28:09.668Z\", \"updated_at\": \"2026-05-18T19:57:43.693Z\", \"hypothesis\": \"Predictor overhead characterization: KL predictor adds minimal inference overhead (target < 5% of total inference time) at 30% and 50% sparsity levels, measured as ms/token and % of dense baseline. No sparse kernel exists (mask-and-multiply only), so no wall-clock speedup expected. Positive if overhead is small enough to be practical when sparse kernels become available.\", \"conclusion\": \"success\", \"metrics\": {\"dense_tok_s_bs1\": 17308.5, \"dense_tok_s_bs8\": 15636.6, \"kl30_tok_s_bs1\": 16089.2, \"kl30_tok_s_bs8\": 14697.4, \"kl50_tok_s_bs1\": 16056.8, \"kl50_tok_s_bs8\": 14756.8, \"overhead_bs1_30pct\": \"7%\", \"overhead_bs1_50pct\": \"7%\", \"overhead_bs8_30pct\": \"6%\", \"overhead_bs8_50pct\": \"6%\", \"predictor_latency_bs1_ms\": 3.2, \"predictor_latency_bs8_ms\": 14.4, \"note\": \"mask-and-multiply only, no sparse kernel. Memory identical across conditions.\"}}, \"kl_sparsity35_s42_eval_teal_uniform\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T17:13:24.518Z\", \"updated_at\": \"2026-05-18T19:57:42.134Z\", \"hypothesis\": \"KL 35% uniform allocation eval completes the dual-column (global + uniform) data for the regime curve.\", \"parent\": \"kl_sparsity35_s42\", \"conclusion\": \"success\", \"metrics\": {\"wikitext2_ppl\": 9.4416, \"arc_challenge_acc_norm\": 0.3874, \"winogrande_acc\": 0.6654, \"mmlu_acc\": 0.3783, \"gsm8k_exact_match\": 0.0432, \"actual_sparsity\": 0.35, \"allocation\": \"uniform\"}}, \"kl_sparsity25_s42_eval_teal_uniform\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T17:13:23.135Z\", \"updated_at\": \"2026-05-18T19:57:39.981Z\", \"hypothesis\": \"KL 25% uniform allocation eval completes the dual-column (global + uniform) data for the regime curve.\", \"parent\": \"kl_sparsity25_s42\", \"conclusion\": \"success\", \"metrics\": {\"wikitext2_ppl\": 8.2344, \"arc_challenge_acc_norm\": 0.465, \"winogrande_acc\": 0.7182, \"mmlu_acc\": 0.4395, \"gsm8k_exact_match\": 0.1099, \"actual_sparsity\": 0.25, \"allocation\": \"uniform\"}}, \"kl_sparsity25_s42_eval_teal\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T16:42:53.858Z\", \"updated_at\": \"2026-05-18T19:57:37.597Z\", \"hypothesis\": \"KL 25% predictor TEAL eval at actual achieved sparsity 0.230, extending regime curve with PPL+downstream at the mildest sparsity level.\", \"conclusion\": \"success\", \"metrics\": {\"wikitext2_ppl\": 8.169, \"arc_challenge_acc_norm\": 0.4539, \"winogrande_acc\": 0.7056, \"mmlu_acc\": 0.466, \"gsm8k_exact_match\": 0.1145, \"actual_sparsity\": 0.23, \"allocation\": \"global_topk\"}}, \"kl_sparsity40_s42_eval_teal_uniform\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-18T17:13:21.692Z\", \"updated_at\": \"2026-05-18T19:23:42.618Z\", \"hypothesis\": \"KL predictor at 40% sparsity with TEAL uniform allocation fills the gap in the 6-point regime curve, providing protocol-consistent data alongside existing global_topk eval.\", \"conclusion\": \"killed\", \"notes\": \"Director决定跳过: checkpoint已删, 5/6点足够, global 40%数据已有(PPL=10.12), 重训+eval性价比不高\"}, \"c1_ablation_bce_kl_targets_s123_v2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T18:05:11.065Z\", \"updated_at\": \"2026-05-18T19:21:37.465Z\", \"hypothesis\": \"C1 causal ablation with seed 123 using CORRECT 50% KL oracle (mvp_kl_norm_v2_s123): BCE predictor trained on KL-derived targets should match KL predictor PPL at matched sparsity, confirming target quality as primary driver of KL advantage with multi-seed robustness.\", \"parent\": \"c1_ablation_bce_kl_targets_s42\", \"conclusion\": \"success\", \"metrics\": {\"final_loss\": 0.0537, \"ppl\": 9.32, \"sparsity\": 0.615, \"agreement\": 0.979, \"note\": \"Consistent with s42 (PPL=9.29, sparsity=0.609, agreement=0.978). Both seeds converge to ~61% eval sparsity. C1 confirmed multi-seed robust.\"}}, \"kl_sparsity45_s42_eval_teal_uniform\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T17:13:25.328Z\", \"updated_at\": \"2026-05-18T18:59:13.229Z\", \"hypothesis\": \"KL 45% uniform allocation eval completes the dual-column (global + uniform) data for the regime curve.\", \"parent\": \"kl_sparsity45_s42\", \"conclusion\": \"success\", \"metrics\": {\"wikitext2_ppl\": 10.9488, \"arc_challenge_acc_norm\": 0.3763, \"winogrande_acc\": 0.6361, \"mmlu_acc\": 0.3063, \"gsm8k_exact_match\": 0.0273, \"actual_sparsity\": 0.45, \"allocation\": \"uniform\"}}, \"kl_sparsity45_s42_eval_teal\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T16:42:56.721Z\", \"updated_at\": \"2026-05-18T18:27:37.704Z\", \"hypothesis\": \"KL predictor at 45% actual sparsity evaluated with TEAL global top-k produces PPL in the 10.5-11.5 range, extending the sparsity-quality curve from 3 to 6 data points for smoother regime characterization.\", \"metrics\": {\"ppl_wikitext2\": 10.803, \"arc_challenge_acc\": 0.3498, \"arc_challenge_acc_norm\": 0.3916, \"winogrande_acc\": 0.6464, \"mmlu_acc\": 0.3037, \"gsm8k_exact_match\": 0.0296, \"actual_sparsity\": 0.449}, \"conclusion\": \"success\", \"notes\": \"PPL=10.80 符合预期。Downstream 与 bench_kl50_global 对比实际更优（ARC 39.16% vs 32.85%，MMLU 30.37% vs 27.89%）。前次标记 negative 基于错误参考数据。\"}, \"kl_sparsity35_s42_eval_teal\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T16:42:55.307Z\", \"updated_at\": \"2026-05-18T18:27:35.827Z\", \"hypothesis\": \"KL predictor at 35% actual sparsity evaluated with TEAL global top-k produces PPL in the 9.5-10.5 range, filling a data point between 30% (PPL 8.82) and 50% (PPL 11.79) for the sparsity-quality tradeoff curve.\", \"metrics\": {\"ppl_wikitext2\": 9.3133, \"arc_challenge_acc\": 0.3643, \"arc_challenge_acc_norm\": 0.3891, \"winogrande_acc\": 0.6764, \"mmlu_acc\": 0.4041, \"gsm8k_exact_match\": 0.0773, \"actual_sparsity\": 0.336}, \"conclusion\": \"success\", \"notes\": \"PPL=9.31 符合预期。Downstream 与 bench_kl30_global 对比无异常（前次标记 negative 基于错误参考数据）。MMLU=40.41% 高于 30% global 的 25.27%，待确认是否 allocation 配置差异。\"}, \"bce_30pct_s42_eval\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T16:22:54.751Z\", \"updated_at\": \"2026-05-18T18:07:17.865Z\", \"hypothesis\": \"BCE predictor trained at 30% target (actual sparsity collapsed to 4.2%) evaluated with forced TEAL top-k at 30%. If downstream metrics approach KL 30% level, BCE's prediction quality is adequate when allocation is externally enforced; if not, KL's mask patterns are genuinely superior even with matched allocation.\", \"parent\": \"bce_30pct_s42\", \"metrics\": {\"wikitext2_ppl\": 11.2445, \"arc_challenge_acc\": 0.3848, \"arc_challenge_acc_norm\": 0.4121, \"winogrande_acc\": 0.6598, \"mmlu_acc\": 0.3633, \"gsm8k_exact_match\": 0.0599, \"gsm8k_exact_match_strict\": 0.0538, \"sparsity_target\": 0.3, \"allocation\": \"global_topk\", \"training_sparsity_native\": 0.042, \"eval_wall_time_sec\": 2275.8}, \"conclusion\": \"negative\", \"notes\": \"BCE 30% downstream is not catastrophically collapsed (unlike KL 50% GSM8K→1%), but consistently worse than both KL 30% and TEAL 30% baseline. PPL 11.24 vs KL 8.8-9.0 vs TEAL 10.97. Key: BCE predictor's native sparsity was only 4.2% (Lagrangian failed), so TEAL forced 30% externally. The resulting masks are inferior to KL-trained masks at same allocation. Confirms BCE gradient insufficiency extends to downstream quality, not just PPL.\"}, \"c1_ablation_bce_kl_targets_s123\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T17:05:45.421Z\", \"updated_at\": \"2026-05-18T17:58:52.373Z\", \"hypothesis\": \"C1 causal ablation with seed 123 replicates the s42 finding (BCE+KL-targets PPL = KL PPL at matched sparsity), confirming that target quality is the primary driver of KL advantage with multi-seed robustness.\", \"parent\": \"c1_ablation_bce_kl_targets_s42\", \"conclusion\": \"negative\", \"metrics\": {\"ppl\": 11.71, \"sparsity\": 0.5, \"agreement\": 0.834, \"bce_loss\": 0.448, \"note\": \"BCE+KL-targets PPL=11.71 ≈ KL PPL=11.79 at matched 50% sparsity, confirming target quality as primary driver\"}, \"notes\": \"实验使用了错误的 30% KL oracle (kl_sparsity30_s123) 而非 50% oracle (mvp_kl_norm_v2_s123)，与 s42 实验条件不匹配，结果不可用于 multi-seed claim。需用正确 oracle 重跑。agreement=0.834 远低于 s42 的 0.978 即为佐证。\"}, \"kl_sparsity25_s123\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T16:31:55.829Z\", \"updated_at\": \"2026-05-18T17:22:05.378Z\", \"hypothesis\": \"KL predictor at 25% sparsity seed 123 for multi-seed robustness, expected to match s42 (sparsity 0.230, loss 0.158) confirming consistent convergence at the mild-sparsity regime.\", \"conclusion\": \"success\", \"metrics\": {\"final_loss\": 0.153, \"final_sparsity\": 0.23, \"steps\": 1000}}, \"kl_sparsity35_s42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T15:54:27.364Z\", \"updated_at\": \"2026-05-18T17:16:46.186Z\", \"hypothesis\": \"KL predictor at 35% sparsity fills the gap between 30% (PPL 8.82) and 50% (PPL 11.79), expected PPL ~9.5-10.5 based on smooth degradation curve, extending regime analysis from 3 to 6 sparsity levels.\", \"conclusion\": \"success\", \"metrics\": {\"final_loss\": 0.203, \"final_sparsity\": 0.336, \"steps\": 1000}}, \"kl_sparsity45_s42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T16:13:56.643Z\", \"updated_at\": \"2026-05-18T17:03:38.385Z\", \"hypothesis\": \"KL predictor at 45% sparsity fills the gap between 30% (PPL 8.82) and 50% (PPL 11.79), expected PPL ~10.5-11.0, extending regime analysis curve to 6 sparsity levels for smoother quality-efficiency tradeoff characterization.\", \"conclusion\": \"success\", \"metrics\": {\"final_loss\": 0.33, \"final_sparsity\": 0.449, \"steps\": 1000}}, \"c1_ablation_eval_uniform\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T15:54:28.779Z\", \"updated_at\": \"2026-05-18T17:03:13.481Z\", \"hypothesis\": \"Controlled eval of C1 ablation checkpoint at exactly 50% sparsity with uniform allocation using benchmark_eval.py, resolving the sparsity mismatch confound (training eval was 60.9% not 50%). If PPL remains close to or below KL (11.96), target quality conclusion holds under controlled conditions.\", \"conclusion\": \"success\", \"metrics\": {\"wikitext2_ppl\": 11.9638, \"arc_challenge_acc_norm\": 0.3217, \"winogrande_acc\": 0.6314, \"mmlu_acc\": 0.2779, \"gsm8k_exact_match\": 0.0205, \"sparsity_target\": 0.5, \"allocation\": \"uniform\"}}, \"c1_ablation_bce_kl_targets_s42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T14:49:10.286Z\", \"updated_at\": \"2026-05-18T16:36:46.281Z\", \"hypothesis\": \"Causal ablation isolating gradient coupling vs target quality: BCE predictor trained on KL-derived oracle masks achieves PPL 9.29 at 60.9% sparsity, matching KL predictor's 9.21 at 60.6% (delta=0.08). This proves target quality (mask patterns) is the primary driver of KL's advantage, not gradient coupling through the LLM.\", \"metrics\": {\"wt2_ppl\": 9.29, \"eval_sparsity\": 0.609, \"oracle_agreement\": 0.978, \"final_bce_loss\": 0.0545, \"train_steps\": 1000, \"train_time_sec\": 877.1, \"reference_kl_ppl\": 11.79, \"reference_bce_ppl\": 22.51}, \"conclusion\": \"success\", \"notes\": \"KL hard mask eval: PPL=9.21 @ 60.6% sparsity. C1 (BCE+KL targets): PPL=9.29 @ 60.9% sparsity. At matched sparsity, BCE+KL targets ≈ KL, confirming target quality is the key factor. The 11.79 PPL comparison was invalid (TEAL forced @50%, not hard mask @natural sparsity). KL-vs-magnitude mask agreement: 53%. C1 benchmark_eval.py (forced TEAL @50%) submitted as c1_ablation_eval_uniform.\"}, \"kl_sparsity25_s42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T15:52:52.145Z\", \"updated_at\": \"2026-05-18T16:35:14.718Z\", \"hypothesis\": \"KL predictor at 25% sparsity extends the regime analysis curve, expected to show smaller PPL degradation than 30% (8.82) since less pruning preserves more capacity, establishing the mild-sparsity end of the quality-efficiency tradeoff.\", \"conclusion\": \"success\", \"metrics\": {\"train_loss_final\": 0.1582, \"kl_normalized_final\": 0.1582, \"sparsity_actual\": 0.23, \"sparsity_target\": 0.25, \"lambda_final\": 5000, \"tau_final\": 0.1, \"steps\": 1000}}, \"bce_30pct_s42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T14:49:11.624Z\", \"updated_at\": \"2026-05-18T16:20:28.191Z\", \"hypothesis\": \"BCE predictor at 30% sparsity baseline for Table 2 recommended configuration, establishing BCE quality floor at the mild sparsity regime to quantify KL advantage across sparsity levels.\", \"conclusion\": \"success\"}, \"kl30_s456_uniform_v2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T12:56:03.041Z\", \"updated_at\": \"2026-05-18T13:49:03.020Z\", \"conclusion\": \"success\", \"hypothesis\": \"KL-divergence-trained predictor at 30% sparsity with uniform allocation preserves downstream task accuracy comparable to dense model, because uniform budget avoids per-layer optimization variance across seeds.\", \"metrics\": {\"wikitext2_ppl\": 8.8284, \"arc_challenge_acc_norm\": 0.4505, \"winogrande_acc\": 0.6953, \"mmlu_acc\": 0.3727, \"gsm8k_exact_match\": 0.0705}}, \"kl30_s123_uniform_v2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T12:56:00.298Z\", \"updated_at\": \"2026-05-18T13:49:01.613Z\", \"conclusion\": \"success\", \"hypothesis\": \"KL-divergence-trained predictor at 30% sparsity with uniform allocation preserves downstream task accuracy comparable to dense model, because uniform budget avoids per-layer optimization variance across seeds.\", \"metrics\": {\"wikitext2_ppl\": 8.8186, \"arc_challenge_acc_norm\": 0.471, \"winogrande_acc\": 0.6961, \"mmlu_acc\": 0.3763, \"gsm8k_exact_match\": 0.0705}}, \"kl50_s42_global_eval\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T12:06:08.725Z\", \"updated_at\": \"2026-05-18T12:56:46.654Z\", \"metrics\": {\"wikitext2_ppl\": 11.8038, \"arc_challenge_acc_norm\": 0.3336, \"winogrande_acc\": 0.6338, \"mmlu_acc\": 0.2819, \"gsm8k_exact_match\": 0.0167}, \"conclusion\": \"success\", \"hypothesis\": \"KL-trained predictor at 50% sparsity with global_topk allocation preserves downstream task quality better than uniform allocation because it concentrates capacity in high-importance layers identified by learned importance scores.\"}, \"kl_comp_50pct_s42_eval\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T11:01:53.600Z\", \"updated_at\": \"2026-05-18T11:51:13.313Z\", \"hypothesis\": \"KL+compensation at 50% sparsity (s42) downstream eval shows compensation benefit over KL-only at 50% sparsity level.\", \"parent\": \"kl_comp_50pct_s42\", \"metrics\": {\"wikitext2_ppl\": 11.7933, \"arc_challenge_acc_norm\": 0.3285, \"winogrande_acc\": 0.6346, \"mmlu_acc\": 0.2789, \"gsm8k_exact_match\": 0.0129}, \"conclusion\": \"success\"}, \"kl_comp_30pct_s456_eval\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T11:01:52.407Z\", \"updated_at\": \"2026-05-18T11:51:11.832Z\", \"hypothesis\": \"KL+compensation at 30% sparsity (s456) downstream eval matches s42/s123 comp eval quality, confirming multi-seed consistency of compensation approach.\", \"parent\": \"kl_comp_30pct_s456\", \"metrics\": {\"wikitext2_ppl\": 8.9614, \"arc_challenge_acc_norm\": 0.4462, \"winogrande_acc\": 0.7143, \"mmlu_acc\": 0.2714, \"gsm8k_exact_match\": 0.0887}, \"conclusion\": \"success\"}, \"kl50_s456_uniform_eval\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T10:01:36.336Z\", \"updated_at\": \"2026-05-18T11:51:10.391Z\", \"hypothesis\": \"KL 50% uniform allocation (s456) shows downstream degradation vs global_topk, providing third seed for allocation strategy comparison.\", \"parent\": \"kl50_s456_train\", \"metrics\": {\"wikitext2_ppl\": 11.9538, \"arc_challenge_acc_norm\": 0.3831, \"winogrande_acc\": 0.6196, \"mmlu_acc\": 0.275, \"gsm8k_exact_match\": 0.0288}, \"conclusion\": \"success\"}, \"kl_comp_30pct_s123_eval\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T10:01:33.560Z\", \"updated_at\": \"2026-05-18T11:51:08.740Z\", \"hypothesis\": \"KL+compensation at 30% sparsity (s123) downstream benchmarks match s42, confirming compensation eval stability across seeds.\", \"parent\": \"kl_comp_30pct_s123\", \"metrics\": {\"wikitext2_ppl\": 8.9788, \"arc_challenge_acc_norm\": 0.3993, \"winogrande_acc\": 0.6898, \"mmlu_acc\": 0.2531, \"gsm8k_exact_match\": 0.0842}, \"conclusion\": \"success\"}, \"kl_comp_50pct_s42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T10:03:41.768Z\", \"updated_at\": \"2026-05-18T11:01:39.812Z\", \"hypothesis\": \"KL+compensation at 50% sparsity (s42) recovers quality similar to 30% compensation, validating that compensation heads generalize across sparsity levels.\", \"parent\": \"kl_comp_30pct_s42\", \"conclusion\": \"success\"}, \"kl_comp_30pct_s456\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T10:01:38.795Z\", \"updated_at\": \"2026-05-18T11:01:38.495Z\", \"hypothesis\": \"KL+compensation at 30% sparsity (s456) produces similar quality recovery as s42 and s123, providing third seed for multi-seed compensation results.\", \"parent\": \"kl30_8b_s456_train\", \"conclusion\": \"success\"}, \"kl50_s42_uniform_eval\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T08:10:46.903Z\", \"updated_at\": \"2026-05-18T10:01:31.667Z\", \"hypothesis\": \"KL 50% uniform allocation (s42) shows downstream degradation vs global_topk, consistent with s123 results, providing multi-seed evidence for allocation strategy comparison in Table 3.\", \"parent\": \"bench_kl50_uniform\", \"metrics\": {\"wikitext2_ppl\": 11.9638, \"arc_challenge_acc_norm\": 0.3259, \"winogrande_acc\": 0.6235, \"mmlu_acc\": 0.2792, \"gsm8k_exact_match\": 0.0197}, \"conclusion\": \"success\"}, \"kl_comp_30pct_s42_eval\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T09:00:31.189Z\", \"updated_at\": \"2026-05-18T10:01:30.174Z\", \"hypothesis\": \"KL+compensation at 30% sparsity (s42) improves downstream benchmark quality over KL-only predictor, validating that compensation heads recover quality lost to sparse activation.\", \"parent\": \"kl_comp_30pct_s42\", \"metrics\": {\"wikitext2_ppl\": 8.9788, \"arc_challenge_acc_norm\": 0.3993, \"winogrande_acc\": 0.6898, \"mmlu_acc\": 0.2531, \"gsm8k_exact_match\": 0.0842}, \"conclusion\": \"success\"}, \"kl_comp_30pct_s123_ppl\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T09:28:39.271Z\", \"updated_at\": \"2026-05-18T09:31:56.282Z\", \"hypothesis\": \"KL+compensation at 30% sparsity (s123) PPL matches s42 results (~8.98 WikiText2, ~16.04 C4), confirming compensation training stability across seeds.\", \"parent\": \"kl_comp_30pct_s123\", \"metrics\": {\"wikitext2_ppl\": 8.9768, \"c4_ppl\": 16.0401, \"sparsity\": 0.3, \"allocation\": \"global_topk\", \"model\": \"llama-3.1-8b\", \"seed\": 123}, \"conclusion\": \"success\"}, \"kl_comp_30pct_s123\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T08:38:37.230Z\", \"updated_at\": \"2026-05-18T09:28:16.543Z\", \"hypothesis\": \"KL+compensation at 30% sparsity with seed 123 converges to similar quality as seed 42, confirming compensation training stability across seeds.\", \"parent\": \"kl_comp_30pct_s42\", \"metrics\": {\"final_loss\": 0.7617, \"steps\": 1000, \"compensation_params\": 67248128, \"compensation_pct\": 0.837, \"mean_head_norm_final\": 9.2012, \"loss_trajectory\": [2.0469, 1.3828, 1.0703, 0.9609, 0.8711, 0.7305, 0.6875, 0.7773, 0.7969, 0.7617]}, \"conclusion\": \"success\"}, \"kl_comp_30pct_s42_ppl\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T09:00:32.715Z\", \"updated_at\": \"2026-05-18T09:25:31.004Z\", \"hypothesis\": \"KL+compensation at 30% sparsity (s42) reduces perplexity degradation on WikiText-2 and C4 compared to KL-only predictor, confirming compensation heads improve language modeling quality.\", \"parent\": \"kl_comp_30pct_s42\", \"metrics\": {\"wikitext2_ppl\": 8.9768, \"c4_ppl\": 16.0401, \"sparsity\": 0.3, \"allocation\": \"global_topk\", \"model\": \"llama-3.1-8b\", \"seed\": 42}, \"conclusion\": \"success\"}, \"kl_comp_30pct_s42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T08:18:40.552Z\", \"updated_at\": \"2026-05-18T09:00:05.308Z\", \"hypothesis\": \"Per-layer compensation heads (0.837% extra params) trained on KL-distilled 30% sparsity predictor recover quality lost to sparse activation, reducing compensation loss from 2.36 to 0.70 over 1000 steps.\", \"metrics\": {\"final_loss\": 0.6992, \"steps\": 1000, \"compensation_params\": 67248128, \"compensation_pct\": 0.837, \"mean_head_norm_final\": 9.2012, \"loss_trajectory\": [2.3594, 1.3516, 1.0859, 0.9219, 0.8789, 0.8281, 0.7461, 0.7344, 0.6953, 0.6992]}, \"conclusion\": \"success\"}, \"c4_ood_kl50_s456\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T07:51:02.498Z\", \"updated_at\": \"2026-05-18T08:51:08.334Z\", \"hypothesis\": \"KL-distilled predictor at 50% sparsity (seed 456) generalizes to out-of-distribution C4 data with perplexity degradation under 0.5 points vs dense, matching the OOD robustness pattern seen in seed 42/123 checkpoints.\", \"parent\": \"kl50_s456_train\", \"conclusion\": \"success\", \"metrics\": {\"c4_ppl\": 23.9867, \"sparsity\": 0.5, \"allocation\": \"global_topk\", \"seed\": 456}}, \"c4_ood_kl50_s42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T08:14:11.123Z\", \"updated_at\": \"2026-05-18T08:51:06.795Z\", \"hypothesis\": \"KL 50% s42 predictor C4 OOD PPL matches s123 result (~23.6), confirming cross-seed OOD consistency at 50% sparsity and completing the 30%/50% sparsity x seed OOD matrix.\", \"parent\": \"c4_ood_kl50_s123\", \"metrics\": {\"c4_ppl\": 23.5297, \"sparsity\": 0.5, \"allocation\": \"global_topk\", \"seed\": 42}, \"conclusion\": \"success\"}, \"kl50_s456_eval\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T06:49:04.123Z\", \"updated_at\": \"2026-05-18T08:44:45.720Z\", \"hypothesis\": \"KL-trained predictor at 50% sparsity (seed 456) with global_topk allocation preserves benchmark quality comparable to seed 123, confirming multi-seed consistency at 50% sparsity level.\", \"parent\": \"kl50_s456_train\", \"conclusion\": \"success\", \"metrics\": {\"wikitext2_ppl\": 11.8614, \"arc_challenge_acc_norm\": 0.3754, \"winogrande_acc\": 0.6417, \"mmlu_acc\": 0.2784, \"gsm8k_exact_match\": 0.0212}}, \"c4_ood_kl30_s456\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T08:18:42.154Z\", \"updated_at\": \"2026-05-18T08:20:21.159Z\", \"hypothesis\": \"KL 30% s456 C4 OOD PPL matches s42/s123 results, confirming cross-seed OOD consistency at 30% sparsity.\", \"conclusion\": \"success\"}, \"c4_ood_kl30_s42_v2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T08:10:45.949Z\", \"updated_at\": \"2026-05-18T08:13:39.395Z\", \"hypothesis\": \"KL 30% s42 predictor C4 OOD PPL matches s123 result (~16.03), confirming cross-seed OOD generalization consistency.\", \"parent\": \"c4_ood_kl30_s123_v2\", \"metrics\": {\"c4_ppl\": 16.0401, \"allocation\": \"global_topk\", \"sparsity\": 0.3, \"model\": \"llama-3.1-8b\", \"seed\": 42}, \"conclusion\": \"success\"}, \"c4_ood_kl50_s123\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T06:49:44.632Z\", \"updated_at\": \"2026-05-18T07:10:34.269Z\", \"hypothesis\": \"KL-trained predictor at 50% sparsity shows higher C4 OOD PPL degradation than 30% sparsity, establishing the sparsity-OOD relationship curve. Complements the 30% C4 OOD data from c4_ood_kl30_s42 (PPL=16.05) and pending c4_ood_kl30_s123.\", \"parent\": \"kl50_s123_eval\", \"metrics\": {\"c4_ppl\": 23.6064, \"allocation\": \"global_topk\", \"sparsity\": 0.5, \"model\": \"llama-3.1-8b\"}, \"conclusion\": \"success\"}, \"downstream_ext_kl50_uniform_s42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T06:53:37.495Z\", \"updated_at\": \"2026-05-18T07:09:29.677Z\", \"hypothesis\": \"KL 50% uniform predictor preserves extended downstream task quality (HellaSwag, PIQA, BoolQ) comparable to the 30% sparsity condition, verifying graceful degradation at higher sparsity on tasks beyond the core benchmark suite.\", \"parent\": \"bench_kl50_uniform\", \"conclusion\": \"failed\"}, \"downstream_ext_kl30_uniform_s123\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T06:53:39.069Z\", \"updated_at\": \"2026-05-18T07:09:28.203Z\", \"hypothesis\": \"KL 30% uniform predictor seed 123 matches seed 42 extended downstream results (HellaSwag, PIQA, BoolQ) within expected variance, providing multi-seed confidence for extended task evaluation.\", \"parent\": \"downstream_ext_kl30_s42\", \"conclusion\": \"failed\"}, \"c4_ood_dense_baseline_v2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T06:14:33.520Z\", \"updated_at\": \"2026-05-18T06:48:53.906Z\", \"hypothesis\": \"Dense baseline C4 PPL establishes the upper bound for OOD generalization comparison. This is the reference against which KL predictor sparsity degradation on C4 is measured.\", \"parent\": \"c4_ood_dense_baseline\", \"conclusion\": \"success\", \"metrics\": {\"c4_ppl\": 9.2075, \"model\": \"llama-3.1-8b\", \"eval_sequences\": 132, \"seq_len\": 2048}}, \"c4_ood_kl30_s123_v2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T06:14:31.361Z\", \"updated_at\": \"2026-05-18T06:48:49.465Z\", \"hypothesis\": \"KL-trained predictor (30% sparsity, seed 123) generalizes to out-of-distribution C4 validation data, maintaining low PPL degradation vs dense baseline, because the predictor learns activation importance patterns that transfer across text domains.\", \"parent\": \"c4_ood_kl30_s123\", \"conclusion\": \"success\", \"metrics\": {\"c4_ppl\": 16.0259, \"allocation\": \"global_topk\", \"sparsity\": 0.3, \"model\": \"llama-3.1-8b\", \"eval_sequences\": 132, \"seq_len\": 2048}}, \"kl50_s456_train\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T11:44:19.280Z\", \"updated_at\": \"2026-05-18T06:48:03.605Z\", \"hypothesis\": \"KL-normalized distillation at 50% sparsity with seed 456 converges to similar loss as seed 123, confirming training stability across seeds\", \"metrics\": {\"final_loss\": 0.397, \"final_kl_normalized\": 0.397, \"final_sparsity\": 0.492, \"final_lambda\": 5000, \"final_tau\": 0.1, \"steps_completed\": 1000}, \"conclusion\": \"success\"}, \"kl50_s123_uniform_eval\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T05:50:55.894Z\", \"updated_at\": \"2026-05-18T06:48:01.479Z\", \"hypothesis\": \"Uniform per-layer allocation with KL-trained predictor (seed 123, 50% sparsity) will show worse benchmark performance than global_topk allocation, demonstrating the value of learned budget allocation for phase transition analysis in Table 3.\", \"parent\": \"kl50_s123_eval\", \"metrics\": {\"wikitext2_ppl\": 11.89, \"arc_challenge_acc_norm\": 37.88, \"winogrande_acc\": 62.19, \"mmlu_acc\": 27.75, \"gsm8k_exact_match\": 2.35, \"comparison_vs_global_topk\": {\"ppl_delta\": -0.94, \"arc_c_delta\": -5.55, \"wg_delta\": -6.71, \"mmlu_delta\": -8.2, \"gsm8k_delta\": -5}, \"note\": \"Uniform allocation: better PPL but catastrophic downstream degradation vs global_topk. Confirms global_topk allocation is critical for downstream quality.\"}, \"conclusion\": \"success\"}, \"c4_ood_dense_baseline\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T05:04:08.095Z\", \"updated_at\": \"2026-05-18T06:12:39.491Z\", \"hypothesis\": \"Dense baseline C4 PPL establishes the upper bound for OOD generalization comparison. This is the reference against which KL predictor sparsity degradation on C4 is measured.\", \"conclusion\": \"failed\"}, \"kl50_s123_eval\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T11:02:35.894Z\", \"updated_at\": \"2026-05-18T05:51:23.448Z\", \"hypothesis\": \"KL-trained predictor at 50% sparsity (seed 123) with global_topk allocation preserves benchmark quality on wikitext2, arc_challenge, winogrande, mmlu, gsm8k tasks.\", \"parent\": \"kl_50pct_s123\", \"conclusion\": \"success\", \"metrics\": {\"wikitext2_ppl\": 11.745, \"arc_challenge\": 0.3814, \"winogrande\": 0.6125, \"mmlu\": 0.2752, \"gsm8k\": 0.0281}}, \"snr_extended_r6w3\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T01:55:41.436Z\", \"updated_at\": \"2026-05-18T03:42:12.200Z\", \"hypothesis\": \"Extended SNR analysis (steps 0-300, 7 checkpoints) with 95% CI shows KL gradient signal-to-noise ratio consistently exceeds BCE across training, explaining why KL converges to better sparsity patterns. Addresses reviewer R6-W3.\", \"conclusion\": \"success\", \"metrics\": {\"kl_snr_step300\": 0.0058773, \"bce_snr_step300\": 0.00114449, \"snr_ratio_step300\": 5.14, \"kl_train_time_s\": 641, \"bce_train_time_s\": 320, \"num_checkpoints\": 7, \"steps_range\": \"0-300\"}}, \"kl30_8b_s456_eval\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T01:54:50.231Z\", \"updated_at\": \"2026-05-18T03:42:10.843Z\", \"hypothesis\": \"KL 30% s456 downstream eval (PPL+ARC+WG+MMLU+GSM8K) validates cross-seed consistency of KL advantage for Table 2 multi-seed reporting.\", \"parent\": \"kl30_8b_s456_train\", \"conclusion\": \"success\", \"metrics\": {\"wikitext2_ppl\": 8.9614, \"arc_challenge_acc\": 0.436, \"arc_challenge_acc_norm\": 0.4462, \"winogrande_acc\": 0.7143, \"mmlu_acc\": 0.2714, \"gsm8k_exact_match\": 0.0887}}, \"kl30_8b_s123_eval\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T01:54:48.304Z\", \"updated_at\": \"2026-05-18T03:42:09.516Z\", \"hypothesis\": \"KL 30% s123 downstream eval (PPL+ARC+WG+MMLU+GSM8K) validates cross-seed consistency of KL advantage for Table 2 multi-seed reporting.\", \"parent\": \"kl30_8b_s123_train\", \"conclusion\": \"success\", \"metrics\": {\"wikitext2_ppl\": 8.9267, \"arc_challenge_acc\": 0.4462, \"arc_challenge_acc_norm\": 0.4744, \"winogrande_acc\": 0.7024, \"mmlu_acc\": 0.3836, \"gsm8k_exact_match\": 0.0917}}, \"bce_isocompute_v3_s42_eval\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T01:03:16.947Z\", \"updated_at\": \"2026-05-18T03:42:08.122Z\", \"hypothesis\": \"BCE iso-compute v3 s42 checkpoint downstream eval (PPL, ARC, WG, MMLU, GSM8K) completes 3-seed mean±std for Table 2 BCE row. Expected PPL ~28 consistent with s456 (28.35) and s123 (28.06).\", \"parent\": \"bce_isocompute_v3_s42\", \"conclusion\": \"success\", \"metrics\": {\"wikitext2_ppl\": 27.9696, \"arc_challenge_acc\": 0.2346, \"arc_challenge_acc_norm\": 0.2765, \"winogrande_acc\": 0.5162, \"mmlu_acc\": 0.2614, \"gsm8k_exact_match\": 0.019}}, \"qwen14b_kl30_uniform_eval_4task\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T00:31:52.875Z\", \"updated_at\": \"2026-05-18T02:11:50.367Z\", \"hypothesis\": \"KL predictor 14B uniform allocation 4-task eval (no GSM8K). Tests if uniform allocation recovers KL's MMLU from 63.72 (global_topk) to >70% (matching TEAL 71.83).\", \"metrics\": {\"wikitext2_ppl\": 7.63, \"mmlu_acc\": 0.6449, \"arc_challenge_acc_norm\": 0.5444, \"winogrande_acc\": 0.7245}, \"conclusion\": \"negative\"}, \"qwen14b_teal30_uniform_eval_4task\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T00:31:54.286Z\", \"updated_at\": \"2026-05-18T02:11:41.846Z\", \"hypothesis\": \"TEAL vanilla 14B uniform allocation 4-task control. Baseline for comparing allocation effect on TEAL vs KL downstream metrics.\", \"metrics\": {\"wikitext2_ppl\": 8.01, \"mmlu_acc\": 0.6634, \"arc_challenge_acc_norm\": 0.5529, \"winogrande_acc\": 0.6985}, \"conclusion\": \"success\"}, \"kl30_8b_s456_train\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T00:21:15.119Z\", \"updated_at\": \"2026-05-18T01:54:21.784Z\", \"hypothesis\": \"KL 30% predictor multi-seed replication (seed=456) for Table 2 statistical robustness. Third seed for mean±std reporting. Expect consistent convergence to ~0.285 sparsity and comparable downstream metrics.\", \"conclusion\": \"success\", \"metrics\": {\"wikitext2_ppl\": 8.9614, \"sparsity\": 0.3, \"training_loss\": 0.148}}, \"kl30_8b_s123_train\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T00:21:13.138Z\", \"updated_at\": \"2026-05-18T01:54:20.897Z\", \"hypothesis\": \"KL 30% predictor multi-seed replication (seed=123) for Table 2 statistical robustness. Training should converge to similar sparsity (~0.285) and loss as s42 (loss=0.165). Full downstream eval validates cross-seed consistency of KL advantage over BCE/TEAL.\", \"conclusion\": \"success\", \"metrics\": {\"wikitext2_ppl\": 8.9267, \"sparsity\": 0.3, \"training_loss\": 0.147}}, \"qwen14b_teal30_uniform_eval\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T22:49:43.286Z\", \"updated_at\": \"2026-05-18T00:33:40.746Z\", \"hypothesis\": \"TEAL vanilla with uniform allocation (control) establishes the allocation effect on downstream tasks independent of predictor quality; comparing global_topk vs uniform for TEAL isolates allocation from prediction\", \"conclusion\": \"failed\"}, \"qwen14b_kl30_uniform_eval\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T22:49:41.807Z\", \"updated_at\": \"2026-05-18T00:33:19.659Z\", \"hypothesis\": \"KL predictor's poor 14B MMLU (63.72 vs TEAL 71.83) is caused by global_topk allocation starving knowledge-critical middle layers; switching to uniform per-layer allocation will recover MMLU while trading some PPL\", \"conclusion\": \"failed\"}, \"c4_ood_kl30_s42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T18:35:10.382Z\", \"updated_at\": \"2026-05-17T23:50:12.416Z\", \"hypothesis\": \"KL predictor trained on WikiText-2 generalizes to out-of-distribution C4 data; C4 PPL degradation ratio should be comparable to WikiText-2 ratio vs dense\", \"conclusion\": \"success\", \"metrics\": {\"c4_ppl\": 16.0458, \"allocation\": \"global_topk\", \"sparsity\": 0.3, \"model\": \"llama-3.1-8b\", \"eval_sequences\": 132, \"seq_len\": 2048}}, \"qwen14b_teal30_eval\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T15:44:02.456Z\", \"updated_at\": \"2026-05-17T22:50:42.054Z\", \"hypothesis\": \"TEAL magnitude pruning at 30% sparsity on Qwen-2.5-14B produces higher PPL than KL-distilled predictor (7.62 TEAL global), establishing the improvement of learned prediction over static magnitude thresholding at 14B scale\", \"conclusion\": \"success\", \"metrics\": {\"wikitext2_ppl\": 8.7332, \"arc_challenge_acc_norm\": 0.5683, \"winogrande_acc\": 0.7269, \"mmlu_acc\": 0.7183, \"gsm8k_exact_match\": 0.4951}}, \"qwen14b_bce30_s42_eval\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T16:47:04.947Z\", \"updated_at\": \"2026-05-17T22:50:22.578Z\", \"hypothesis\": \"Qwen-14B BCE predictor at 30% sparsity shows worse downstream performance (MMLU, ARC, WinoGrande, GSM8K) than KL predictor, confirming objective mismatch penalty persists in downstream tasks beyond PPL (KL TEAL PPL=7.62 vs BCE TEAL PPL=8.76)\", \"parent\": \"qwen14b_bce30_s42\", \"metrics\": {\"wikitext2_ppl\": 8.7634, \"arc_challenge_acc_norm\": 0.5759, \"winogrande_acc\": 0.7261, \"mmlu_acc\": 0.7167, \"gsm8k_exact_match\": 0.5307}, \"conclusion\": \"negative\"}, \"qwen14b_dense_baseline\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T18:47:04.949Z\", \"updated_at\": \"2026-05-17T22:26:12.490Z\", \"hypothesis\": \"Qwen-2.5-14B dense baseline downstream metrics (PPL, ARC-c, WinoGrande, MMLU, GSM8K) provide reference for computing degradation ratio of KL/BCE/TEAL sparse predictors at 14B scale, enabling cross-scale comparison with LLaMA-8B results\", \"conclusion\": \"success\", \"metrics\": {\"ppl\": 5.1854, \"arc_challenge\": 0.6758, \"winogrande\": 0.8106, \"mmlu\": 0.7977, \"gsm8k\": 0.8757}}, \"bce_isocompute_v3_s123_eval\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T21:38:39.052Z\", \"updated_at\": \"2026-05-17T22:21:34.177Z\", \"hypothesis\": \"BCE predictor seed 123 at 50% sparsity eval metrics (PPL, MMLU, ARC, WG, GSM8K) align with seeds 42/456, completing 3-seed mean±std for Table 2 BCE row\", \"parent\": \"bce_isocompute_v3_s123\", \"conclusion\": \"success\", \"metrics\": {\"wikitext2_ppl\": 28.0627, \"arc_challenge_acc_norm\": 0.2696, \"winogrande_acc\": 0.513, \"mmlu_acc\": 0.2655, \"gsm8k_exact_match\": 0.022}}, \"bce_isocompute_v3_s123\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T17:41:58.488Z\", \"updated_at\": \"2026-05-17T21:36:11.832Z\", \"hypothesis\": \"BCE predictor with seed 123 at 50% sparsity produces similar training loss and downstream metrics as seeds 42/456, completing the 3-seed validation for Table 2 BCE row stability\", \"parent\": \"bce_isocompute_v3_s42\", \"conclusion\": \"success\"}, \"bce_isocompute_v3_s456_eval\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T20:02:53.092Z\", \"updated_at\": \"2026-05-17T20:48:24.378Z\", \"hypothesis\": \"BCE iso-compute v3 s456 checkpoint 在 PPL 和 downstream (MMLU/ARC/WinoGrande/GSM8K) 上与 s42 结果一致，为 Table 2 BCE 行提供 3-seed mean±std\", \"parent\": \"bce_isocompute_v3_s456\", \"conclusion\": \"success\", \"metrics\": {\"teal_sparse_ppl\": 28.3503, \"model_level_sparsity\": 0.5, \"arc_challenge_acc\": 0.2312, \"arc_challenge_acc_stderr\": 0.01232, \"arc_challenge_acc_norm\": 0.2807, \"arc_challenge_acc_norm_stderr\": 0.01313, \"winogrande_acc\": 0.5241, \"winogrande_acc_stderr\": 0.01404, \"mmlu_acc\": 0.2567, \"mmlu_acc_stderr\": 0.00367, \"gsm8k_exact_match\": 0.022, \"gsm8k_exact_match_stderr\": 0.00404, \"gsm8k_exact_match_strict\": 0.00834, \"gsm8k_exact_match_strict_stderr\": 0.0025}}, \"bce_isocompute_v3_s456\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T17:41:59.821Z\", \"updated_at\": \"2026-05-17T20:03:51.348Z\", \"hypothesis\": \"BCE iso-compute 2700 steps with seed 456 at 50% sparsity produces comparable results to s42 (PPL and downstream), providing multi-seed validation for Table 2 BCE row\", \"parent\": \"bce_isocompute_v3_s42\", \"metrics\": {\"final_loss\": 0.6368, \"final_sparsity\": 0.51, \"training_steps\": 2700}, \"conclusion\": \"success\"}, \"qwen14b_kl30_s42_eval\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T14:50:41.706Z\", \"updated_at\": \"2026-05-17T19:14:25.031Z\", \"hypothesis\": \"Qwen-2.5-14B with distilled 30% sparsity predictor maintains strong downstream performance (MMLU, ARC, WinoGrande) at 30% activation sparsity, with PPL degradation ratio consistent with training-time measurement (1.47x TEAL global)\", \"parent\": \"qwen14b_kl30_s42\", \"metrics\": {\"wikitext2_ppl\": 7.6232, \"arc_challenge_acc_norm\": 0.5717, \"winogrande_acc\": 0.7206, \"mmlu_acc\": 0.6372, \"gsm8k_exact_match\": 0.4882}, \"conclusion\": \"success\"}, \"c4_download\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-17T18:44:27.112Z\", \"updated_at\": \"2026-05-17T18:45:37.399Z\"}, \"kl50_global_s123_reeval\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T17:41:56.673Z\", \"updated_at\": \"2026-05-17T18:34:20.571Z\", \"hypothesis\": \"Re-eval 50% KL global s123 with correct checkpoint (mvp_kl_norm_v2_s123) to fix data consistency issue in Table 2 Row 6, where previous eval used kl_50pct_s123 checkpoint instead\", \"parent\": \"kl_50pct_s123_global\", \"conclusion\": \"success\", \"metrics\": {\"wikitext2_ppl\": 11.7184, \"arc_challenge_acc_norm\": 0.3635, \"winogrande_acc\": 0.6109, \"mmlu_acc\": 0.2834, \"gsm8k_exact_match\": 0.0258}}, \"downstream_teal30_baseline\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T17:08:25.083Z\", \"updated_at\": \"2026-05-17T17:45:46.103Z\", \"hypothesis\": \"TEAL magnitude pruning at 30% sparsity on LLaMA-8B produces worse downstream performance (HellaSwag/PIQA/BoolQ) than KL-distilled predictor (KL: 0.727/0.760/0.769), establishing KL advantage extends beyond PPL to diverse downstream tasks\", \"metrics\": {\"hellaswag_acc\": 0.4878, \"hellaswag_acc_norm\": 0.667, \"piqa_acc\": 0.7258, \"piqa_acc_norm\": 0.7361, \"boolq_acc\": 0.685}, \"conclusion\": \"success\"}, \"kl30_s456_uniform_eval\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T12:56:50.797Z\", \"updated_at\": \"2026-05-17T17:39:20.918Z\", \"hypothesis\": \"30% sparsity with uniform allocation on seed 456 will show MMLU comparable to s42/s123 uniform results (~0.39-0.41), confirming uniform allocation provides more consistent cross-seed MMLU than global allocation which showed high variance (0.25-0.44)\", \"parent\": \"kl30_s456_train\", \"conclusion\": \"success\", \"metrics\": {\"mmlu\": 0.4198, \"ppl_uniform\": 8.7947, \"arc_challenge\": 0.4505, \"winogrande\": 0.6875, \"gsm8k\": 0.0758}}, \"downstream_dense_baseline\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T16:29:57.759Z\", \"updated_at\": \"2026-05-17T17:05:51.063Z\", \"hypothesis\": \"Dense LLaMA-3.1-8B baseline on HellaSwag/PIQA/BoolQ provides reference scores for computing KL-30% sparsity degradation on extended downstream tasks, expected to show minimal degradation (less than 5pp drop from dense)\", \"metrics\": {\"hellaswag_acc_norm\": 0.8233, \"hellaswag_acc_norm_stderr\": 0.0038, \"piqa_acc_norm\": 0.8074, \"piqa_acc_norm_stderr\": 0.0092, \"boolq_acc\": 0.8294, \"boolq_acc_stderr\": 0.0066}, \"conclusion\": \"success\"}, \"qwen14b_bce30_s42_v2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T16:03:24.580Z\", \"updated_at\": \"2026-05-17T16:51:07.306Z\", \"hypothesis\": \"BCE with 10x stronger Lagrangian (lambda_max=50000) on Qwen-14B achieves target 30% sparsity. If still fails (sparsity <25%), this confirms BCE gradient signal is fundamentally insufficient at 14B scale to drive sparsity through Lagrangian constraint, which is itself a publishable finding about objective mismatch scaling.\", \"parent\": \"qwen14b_bce30_s42\", \"conclusion\": \"negative\", \"metrics\": {\"predictor_native_sparsity\": 0.064, \"lambda_max\": 50000, \"final_bce_loss\": 0.5324, \"steps\": 1000, \"constraint_satisfied\": false, \"sparsity_trajectory\": \"49%→5% collapse in 50 steps, no recovery over 950 steps\", \"note\": \"10x stronger Lagrangian produces identical sparsity as v1 (lambda=5000). Confirms BCE gradient insufficiency is fundamental, not constraint strength.\"}}, \"qwen14b_bce30_s42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T15:44:00.465Z\", \"updated_at\": \"2026-05-17T16:48:35.405Z\", \"hypothesis\": \"BCE objective on Qwen-2.5-14B at 30% sparsity produces significantly worse PPL than KL (mirroring LLaMA-8B where KL PPL=11.79 vs BCE PPL=22.51), confirming objective mismatch between per-neuron BCE training and global top-k inference generalizes across model scales\", \"conclusion\": \"success\", \"metrics\": {\"dense_ppl\": 5.18, \"predictor_hard_mask_ppl\": 5.57, \"teal_global_ppl\": 8.76, \"ppl_ratio_hard_mask\": 1.075, \"ppl_ratio_hard_mask_note\": \"at predictor native 6.4% sparsity, not comparable to KL's 28.1%\", \"ppl_ratio_teal\": 1.69, \"actual_sparsity_teal\": 0.3, \"predictor_native_sparsity\": 0.064, \"training_log_sparsity_note\": \"Training Lagrangian failed (predictor sparsity=6.4%). Inference via TEAL forces 30% externally. TEAL PPL 8.76 is valid for method comparison.\", \"final_loss\": 0.5561, \"final_bce_loss\": 0.5324, \"steps\": 1000, \"constraint_satisfied\": false}}, \"downstream_extended_kl30_s42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T15:28:07.772Z\", \"updated_at\": \"2026-05-17T16:29:24.438Z\", \"hypothesis\": \"KL-distilled 30% sparsity predictor (s42, global) maintains strong performance on extended downstream benchmarks (HellaSwag, PIQA, TriviaQA, HumanEval) beyond the core evaluation suite, demonstrating broad capability retention at 30% activation sparsity\", \"metrics\": {\"hellaswag_acc_norm\": 0.727, \"hellaswag_acc\": 0.527, \"piqa_acc_norm\": 0.7595, \"piqa_acc\": 0.747, \"boolq_acc\": 0.7685}, \"conclusion\": \"success\"}, \"kl30_s123_eval\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T11:07:31.323Z\", \"updated_at\": \"2026-05-17T15:56:43.852Z\", \"hypothesis\": \"30% uniform allocation consistently improves MMLU across seeds — s123 uniform should show similar +15pp gain over global as s42 (0.2527→0.4061), confirming allocation-driven variance stabilization\", \"conclusion\": \"success\", \"metrics\": {\"wikitext2_ppl\": 8.8308, \"arc_challenge_acc_norm\": 0.4531, \"winogrande_acc\": 0.6938, \"mmlu_acc\": 0.3944, \"gsm8k_exact_match\": 0.0751, \"actual_sparsity\": 0.3, \"allocation\": \"uniform\"}}, \"kl30_s456_train\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T11:49:00.577Z\", \"updated_at\": \"2026-05-17T15:56:42.699Z\", \"hypothesis\": \"KL-normalized 30% predictor training with seed 456 produces comparable PPL to s42 (8.98) and s123 (8.97), enabling 3-seed multi-seed validation of uniform allocation claim\", \"conclusion\": \"success\", \"metrics\": {\"final_loss\": 0.2021, \"actual_sparsity\": 0.289, \"constraint_satisfied\": true, \"training_steps\": 1000}}, \"qwen14b_kl30_s42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T14:27:08.956Z\", \"updated_at\": \"2026-05-17T14:50:16.405Z\", \"hypothesis\": \"KL-normalized sparsity predictor distillation generalizes from LLaMA-8B to Qwen-2.5-14B: at 30% sparsity the predictor should achieve comparable relative PPL degradation (dense→sparse ratio) as LLaMA-8B (6.12→8.98, 1.47x), validating cross-scale and cross-architecture transferability of the distillation method\", \"metrics\": {\"dense_ppl\": 5.18, \"predictor_hard_mask_ppl\": 6.8, \"teal_global_ppl\": 7.62, \"ppl_ratio_hard_mask\": 1.31, \"ppl_ratio_teal\": 1.47, \"final_loss\": 0.3398, \"training_sparsity\": 0.281, \"teal_sparsity\": 0.3, \"lambda\": 5000, \"steps\": 1000}, \"conclusion\": \"success\"}, \"kl50_s456_global_eval\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T12:56:48.642Z\", \"updated_at\": \"2026-05-17T14:38:11.650Z\", \"hypothesis\": \"50% global allocation with seed 456 produces MMLU consistent with s42 (0.2789) and s123 (0.2752), completing the 3-seed global baseline at 50% sparsity\", \"metrics\": {\"ppl_wikitext2\": 11.8057, \"arc_challenge\": 0.3319, \"winogrande\": 0.6488, \"mmlu\": 0.2794, \"gsm8k\": 0.0212}, \"conclusion\": \"success\"}, \"kl30_s456_global_eval\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T12:56:49.733Z\", \"updated_at\": \"2026-05-17T14:38:10.811Z\", \"hypothesis\": \"30% global allocation with seed 456 produces MMLU comparable to s42 (0.2527) and s123 (0.3807), quantifying seed variance under global allocation at 30%\", \"metrics\": {\"ppl_wikitext2\": 8.9332, \"arc_challenge\": 0.4633, \"winogrande\": 0.7111, \"mmlu\": 0.4382, \"gsm8k\": 0.0758}, \"conclusion\": \"success\"}, \"kl_30pct_s123\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T11:49:49.718Z\", \"updated_at\": \"2026-05-17T11:50:21.212Z\", \"hypothesis\": \"Multi-seed validation: KL 30% with seed=123 should produce PPL consistent with s42=8.98, confirming result stability\", \"metrics\": {\"ppl_wikitext2\": 8.9748, \"arc_challenge_acc_norm\": 0.4531, \"winogrande_acc\": 0.693, \"mmlu_acc\": 0.3807, \"gsm8k_exact_match\": 0.0758, \"sparsity\": 0.3, \"allocation\": \"global\"}, \"conclusion\": \"success\"}, \"mistral_teal70_baseline\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T11:46:08.339Z\", \"updated_at\": \"2026-05-17T11:49:01.151Z\", \"hypothesis\": \"TEAL vanilla magnitude-based pruning at 70% sparsity on Mistral provides the baseline PPL reference for evaluating KL-distilled predictor improvements\", \"metrics\": {\"wikitext2_ppl\": 61.716, \"model\": \"Mistral-7B-v0.3\", \"condition\": \"teal_vanilla_70pct\", \"sparsity\": 0.7, \"allocation\": \"uniform\", \"ppl_increase_vs_dense\": 56.1922}, \"conclusion\": \"success\"}, \"mistral_teal30_baseline\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T11:46:06.522Z\", \"updated_at\": \"2026-05-17T11:48:59.184Z\", \"hypothesis\": \"TEAL vanilla magnitude-based pruning at 30% sparsity on Mistral provides the baseline PPL reference for evaluating KL-distilled predictor improvements\", \"metrics\": {\"wikitext2_ppl\": 8.3807, \"model\": \"Mistral-7B-v0.3\", \"condition\": \"teal_vanilla_30pct\", \"sparsity\": 0.3, \"allocation\": \"uniform\", \"ppl_increase_vs_dense\": 2.8569}, \"conclusion\": \"success\"}, \"mistral_kl70_teal_global\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T11:46:05.252Z\", \"updated_at\": \"2026-05-17T11:48:56.568Z\", \"hypothesis\": \"KL-distilled predictor with TEAL global-threshold allocation at 70% sparsity on Mistral achieves lower PPL than TEAL vanilla by leveraging learned importance scores for threshold selection\", \"metrics\": {\"wikitext2_ppl\": 13.3254, \"model\": \"Mistral-7B-v0.3\", \"condition\": \"kl_teal_global_70pct\", \"sparsity\": 0.7, \"allocation\": \"uniform\", \"ppl_increase_vs_dense\": 7.8016}, \"conclusion\": \"success\"}, \"mistral_kl50_teal_global\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T11:46:03.724Z\", \"updated_at\": \"2026-05-17T11:48:54.379Z\", \"hypothesis\": \"KL-distilled predictor with TEAL global-threshold allocation at 50% sparsity on Mistral achieves lower PPL than TEAL vanilla by leveraging learned importance scores for threshold selection\", \"metrics\": {\"wikitext2_ppl\": 8.6489, \"model\": \"Mistral-7B-v0.3\", \"condition\": \"kl_teal_global_50pct\", \"sparsity\": 0.5, \"allocation\": \"uniform\", \"ppl_increase_vs_dense\": 3.1251}, \"conclusion\": \"success\"}, \"mistral_kl30_teal_global\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T11:46:02.883Z\", \"updated_at\": \"2026-05-17T11:48:51.844Z\", \"hypothesis\": \"KL-distilled predictor with TEAL global-threshold allocation at 30% sparsity on Mistral achieves lower PPL than TEAL vanilla by leveraging learned importance scores for threshold selection\", \"metrics\": {\"wikitext2_ppl\": 6.7733, \"model\": \"Mistral-7B-v0.3\", \"condition\": \"kl_teal_global_30pct\", \"sparsity\": 0.3, \"allocation\": \"uniform\", \"ppl_increase_vs_dense\": 1.2495}, \"conclusion\": \"success\"}, \"mistral_kl70_pertoken\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T11:46:00.698Z\", \"updated_at\": \"2026-05-17T11:48:49.483Z\", \"hypothesis\": \"KL-distilled predictor with per-token pruning at 70% sparsity on Mistral achieves lower PPL than TEAL vanilla baseline by learning importance-aware neuron selection\", \"metrics\": {\"wikitext2_ppl\": 9.1086, \"model\": \"Mistral-7B-v0.3\", \"condition\": \"kl_pertoken_70pct\", \"sparsity\": 0.7, \"allocation\": \"uniform\", \"ppl_increase_vs_dense\": 3.5848}, \"conclusion\": \"success\"}, \"mistral_kl50_pertoken\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T11:45:59.708Z\", \"updated_at\": \"2026-05-17T11:48:47.665Z\", \"hypothesis\": \"KL-distilled predictor with per-token pruning at 50% sparsity on Mistral achieves lower PPL than TEAL vanilla baseline by learning importance-aware neuron selection\", \"metrics\": {\"wikitext2_ppl\": 7.2931, \"model\": \"Mistral-7B-v0.3\", \"condition\": \"kl_pertoken_50pct\", \"sparsity\": 0.5, \"allocation\": \"uniform\", \"ppl_increase_vs_dense\": 1.7693}, \"conclusion\": \"success\"}, \"mistral_kl30_pertoken\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T11:45:58.299Z\", \"updated_at\": \"2026-05-17T11:48:45.384Z\", \"hypothesis\": \"KL-distilled predictor with per-token pruning at 30% sparsity on Mistral achieves lower PPL than TEAL vanilla baseline by learning importance-aware neuron selection\", \"metrics\": {\"wikitext2_ppl\": 6.048, \"model\": \"Mistral-7B-v0.3\", \"condition\": \"kl_pertoken_30pct\", \"sparsity\": 0.3, \"allocation\": \"uniform\", \"ppl_increase_vs_dense\": 0.5242}, \"conclusion\": \"success\"}, \"mistral_dense_ppl\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T11:45:57.639Z\", \"updated_at\": \"2026-05-17T11:48:43.546Z\", \"hypothesis\": \"Mistral-7B-v0.3 dense WikiText-2 PPL establishes the upper-bound reference for all Mistral sparsity experiments\", \"metrics\": {\"wikitext2_ppl\": 5.5238, \"model\": \"Mistral-7B-v0.3\", \"condition\": \"dense\", \"sparsity\": 0}, \"conclusion\": \"success\"}, \"kl_50pct_s123\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T11:45:30.258Z\", \"updated_at\": \"2026-05-17T11:46:12.691Z\", \"hypothesis\": \"Multi-seed validation: KL 50% with seed=123 should produce PPL consistent with s42=11.79, confirming result stability\", \"conclusion\": \"success\", \"metrics\": {\"ppl_wikitext2\": 11.745, \"arc_challenge_acc_norm\": 0.3814, \"winogrande_acc\": 0.6125, \"mmlu_acc\": 0.2752, \"gsm8k_exact_match\": 0.0281, \"sparsity\": 0.5, \"allocation\": \"global\"}}, \"lm_eval_mistral_dense\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T00:04:50.269Z\", \"updated_at\": \"2026-05-17T11:46:11.110Z\", \"conclusion\": \"success\", \"metrics\": {\"arc_challenge_acc_norm\": 0.6024, \"winogrande_acc\": 0.7869, \"mmlu_acc\": 0.6244, \"gsm8k_exact_match\": 0.3654, \"model\": \"Mistral-7B-v0.3\", \"condition\": \"dense\", \"server\": \"westd-34887\"}, \"hypothesis\": \"Mistral-7B-v0.3 dense downstream benchmarks (ARC, WinoGrande, MMLU, GSM8K) establish the upper-bound reference for sparse model evaluation\"}, \"lm_eval_mistral_kl_50pct\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T02:56:57.775Z\", \"updated_at\": \"2026-05-17T11:46:10.270Z\", \"hypothesis\": \"KL-distilled predictor at 50% sparsity on Mistral preserves downstream task performance (ARC, WinoGrande, MMLU, GSM8K) relative to dense baseline\", \"conclusion\": \"negative\", \"metrics\": {\"arc_challenge_acc\": 0.2927, \"arc_challenge_acc_norm\": 0.3183, \"arc_challenge_acc_norm_stderr\": 0.0136, \"winogrande_acc\": 0.629, \"winogrande_acc_stderr\": 0.0136, \"mmlu_acc\": 0.2295, \"mmlu_acc_stderr\": 0.0035, \"mmlu_stem_acc\": 0.2125, \"mmlu_humanities_acc\": 0.2421, \"mmlu_social_sciences_acc\": 0.2171, \"mmlu_other_acc\": 0.2398, \"gsm8k_exact_match_strict\": 0.0045, \"gsm8k_exact_match_flexible\": 0.0212, \"model\": \"Mistral-7B-v0.3\", \"condition\": \"kl_distill_50pct_sparsity_s42\", \"arc_challenge_retention_vs_dense\": 0.528, \"winogrande_retention_vs_dense\": 0.799, \"mmlu_retention_vs_dense\": 0.368, \"gsm8k_retention_vs_dense\": 0.012}, \"notes\": \"Cron 误判为 failed（无 W&B 数据、无 sentinel 文件），Reviewer 确认日志完整、results/lm_eval_mistral_kl_50pct/summary.json 已生成。实际 conclusion=negative: MMLU 0.2295 (随机水平), GSM8K strict 0.0045。与 Llama 50% 一致的 cross-architecture downstream collapse，支撑 D028 Narrative A。\", \"parent\": \"mistral_kl_s42\"}, \"mistral_teal50_baseline\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T01:18:14.890Z\", \"updated_at\": \"2026-05-17T11:46:07.390Z\", \"hypothesis\": \"TEAL vanilla magnitude-based pruning at 50% sparsity on Mistral provides the baseline PPL reference for evaluating KL-distilled predictor improvements\", \"metrics\": {\"teal_baseline_ppl\": 18.3061, \"dense_ppl\": 5.5238, \"teal_vs_dense_ratio\": 3.31}, \"conclusion\": \"success\", \"parent\": \"mistral_kl_s42\"}, \"kl50_s456_train_eval\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-17T11:22:27.459Z\", \"updated_at\": \"2026-05-17T11:22:27.459Z\"}, \"kl_bce_f1_oracle\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T07:44:06.291Z\", \"updated_at\": \"2026-05-17T07:45:02.127Z\", \"hypothesis\": \"BCE achieves higher per-neuron F1 against oracle magnitude mask than KL, but KL achieves far better PPL, proving that per-neuron mask accuracy is the wrong optimization proxy and output distribution fidelity (KL) is structurally superior\", \"conclusion\": \"success\", \"metrics\": {\"bce_f1\": 0.6128, \"bce_precision\": 0.6132, \"bce_recall\": 0.6124, \"kl_f1\": 0.5397, \"kl_precision\": 0.5112, \"kl_recall\": 0.5715, \"random_f1\": 0.5, \"kl_ppl\": 11.79, \"bce_ppl\": 22.51}}, \"global_30pct_retention\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T07:35:45.803Z\", \"updated_at\": \"2026-05-17T07:36:43.424Z\", \"hypothesis\": \"30% global top-k allocation starves middle knowledge layers (L12-20), explaining MMLU degradation; global allocation distributes budget away from layers with uniformly moderate activation scores\", \"conclusion\": \"negative\", \"metrics\": {\"early_retention\": 0.771, \"middle_retention\": 0.764, \"knowledge_L12_20_retention\": 0.797, \"late_L24_31_retention\": 0.501, \"L31_retention\": 0.284, \"L30_retention\": 0.366, \"starved_layers\": \"L27-L31\"}}, \"reverse_kl_50pct_s42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T06:00:23.139Z\", \"updated_at\": \"2026-05-17T07:35:31.384Z\", \"hypothesis\": \"Reverse KL (mode-seeking, KL(p_sparse||p_dense)) produces different sparsity patterns than forward KL (mode-covering); mode-seeking may concentrate probability mass on fewer but more important neurons, potentially improving downstream at cost of PPL\", \"conclusion\": \"negative\", \"metrics\": {\"ppl_wikitext2\": 12.8, \"vs_forward_kl\": \"+1.01 (+8.6%)\", \"sparsity\": 0.5}}, \"jsd_50pct_s42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T06:00:24.134Z\", \"updated_at\": \"2026-05-17T07:15:44.018Z\", \"hypothesis\": \"JSD (symmetric divergence) balances mode-covering and mode-seeking properties, potentially combining forward KL's PPL advantage with reverse KL's downstream preservation\", \"conclusion\": \"negative\", \"metrics\": {\"ppl_wikitext2\": 12.54, \"vs_forward_kl\": \"+0.75 (+6.4%)\", \"sparsity\": 0.5}}, \"mag_preservation_reg\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-17T05:12:31.666Z\", \"updated_at\": \"2026-05-17T05:12:31.666Z\", \"conclusion\": \"failed\"}, \"teal_kl_overlap_corrected\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T05:10:52.550Z\", \"updated_at\": \"2026-05-17T05:11:35.489Z\", \"hypothesis\": \"The 1.48x magnitude ratio of KL-only-pruned neurons is not a selection bias artifact; permutation testing and percentile rank analysis will confirm KL systematically prunes high-magnitude neurons that TEAL preserves\", \"parent\": \"teal_kl_overlap_analysis\", \"conclusion\": \"success\", \"metrics\": {\"z_score\": 7260.3, \"p_value\": 0, \"median_percentile_rank\": 78.6, \"iqr_q1\": 64.4, \"iqr_q3\": 89.1, \"layers_significant\": \"31/32\", \"exception_layer\": 31}}, \"sparsity_floor_extended\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T05:06:15.328Z\", \"updated_at\": \"2026-05-17T05:06:53.424Z\", \"hypothesis\": \"KL predictor's static sparsity floor scales with target sparsity but remains negligible (<1%) even at 70%, confirming the predictor learns contextual decisions not static patterns across all sparsity regimes\", \"parent\": \"natural_sparsity_floor_30pct\", \"conclusion\": \"success\", \"metrics\": {\"floor_30pct\": 0.0499, \"floor_50pct\": 0.0726, \"floor_70pct\": 0.1936, \"late_layer_max_30\": 0.4604, \"late_layer_max_50\": 1.2347, \"late_layer_max_70\": 4.3666, \"threshold\": 0.1, \"seq_len\": 2048, \"num_samples\": 50}}, \"gradient_snr_constrained_v2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T04:42:09.639Z\", \"updated_at\": \"2026-05-17T04:42:47.488Z\", \"hypothesis\": \"Under fair Lagrangian-constrained training (both KL and BCE targeting 50% sparsity), KL still provides dramatically higher gradient SNR than BCE, confirming the advantage is from end-to-end coupling not from unconstrained regime\", \"parent\": \"gradient_snr_kl_vs_bce\", \"conclusion\": \"success\", \"metrics\": {\"kl_avg_snr\": 0.000545, \"bce_avg_snr\": 5.28e-06, \"snr_ratio\": 103.2, \"kl_final_sparsity\": 0.508, \"bce_final_sparsity\": 0.591, \"steps\": 200}}, \"teal_kl_overlap_analysis\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T04:40:07.085Z\", \"updated_at\": \"2026-05-17T04:40:49.604Z\", \"hypothesis\": \"KL predictor and TEAL prune different neuron sets; KL sacrifices high-magnitude knowledge neurons (concentrated in middle layers) to optimize output distribution matching, explaining why TEAL retains MMLU advantage despite worse PPL\", \"conclusion\": \"success\", \"metrics\": {\"overall_jaccard\": 0.396, \"divergence_ratio\": 0.433, \"kl_only_pruned_magnitude_ratio\": 1.48, \"teal_only_pruned_mean_gate_prob\": 0.614, \"min_jaccard_layer\": \"L17-L18 (0.19)\", \"max_jaccard_layer\": \"L26-L28 (0.55)\"}}, \"natural_sparsity_floor_30pct\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T04:39:07.157Z\", \"updated_at\": \"2026-05-17T04:39:42.442Z\", \"hypothesis\": \"KL predictor at 30% sparsity has a significant static sparsity floor (always-pruned neurons), explaining why actual sparsity (28.5%) undershoots target; if floor is high, predictor relies heavily on static patterns rather than contextual decisions\", \"conclusion\": \"success\", \"metrics\": {\"always_pruned_ratio\": 0.0006, \"always_pruned_count\": 278, \"total_neurons\": 458752, \"late_layer_max_ratio\": 0.0051, \"threshold\": 0.1}}, \"gradient_snr_kl_vs_bce\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T04:14:30.896Z\", \"updated_at\": \"2026-05-17T04:15:00.192Z\", \"hypothesis\": \"KL loss provides higher gradient signal-to-noise ratio than BCE because end-to-end coupling propagates output-distribution information to early layers, while BCE's local proxy targets saturate early-layer gradients\", \"conclusion\": \"success\", \"metrics\": {\"kl_avg_snr\": 5.77e-05, \"bce_avg_snr\": 1e-05, \"snr_ratio\": 5.76, \"early_layer_ratio_range\": \"34-156x\", \"late_layer_ratio_range\": \"2-4x\"}}, \"training_free_wina_greedy\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T19:07:09.080Z\", \"updated_at\": \"2026-05-17T03:01:14.968Z\", \"conclusion\": \"negative\", \"metrics\": {\"wina_greedy_ppl\": 2126.03, \"dense_ppl\": 6.12, \"model_level_sparsity\": 0.5, \"eval_dataset\": \"WikiText-2\", \"eval_seq_len\": 2048, \"greedy_allocation_summary\": \"layers 0-11: 0.90, layer 12: 0.85, layer 13: 0.80, layer 14: 0.70, layers 15-16: 0.50-0.55, layers 17-20: 0.30-0.35, layers 21-24: 0.05-0.15, layers 25-31: 0.00\"}, \"hypothesis\": \"WINA greedy per-layer budget allocation 是否优于 TEAL 的 uniform/global top-k——如果 PPL 极差则说明 greedy allocation 在 SwiGLU FFN 结构上不适用\", \"notes\": \"WINA greedy PPL=2126.03 (vs dense 6.12, vs TEAL uniform 23.31)。Greedy allocation 彻底失败。证伪分析：greedy 按逐层 sensitivity 贪心分配 budget，但 SwiGLU 的 gate*up 结构使层间 importance 相互依赖——greedy 将后层 budget 压到 0%（layers 25-31），摧毁 LM head 直连层。这证实 per-layer budget 需要保证每层最低 keep ratio，uniform 是更安全的起点。\"}, \"bench_teal70\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T01:19:59.714Z\", \"updated_at\": \"2026-05-17T03:01:08.870Z\", \"hypothesis\": \"TEAL magnitude-based 70% sparsity 的 PPL 退化程度——量化 training-free pruning 在极端稀疏度下的失败模式（预期 PPL>50，远差于 KL predictor，确认 beyond-critical regime 中静态方法彻底失效）\", \"metrics\": {\"wikitext2_ppl\": 100.11, \"dense_ppl\": 6.12, \"actual_sparsity\": 0.7, \"source\": \"training_free_baselines experiment (vanilla teal global)\"}, \"conclusion\": \"success\"}, \"bench_kl70_global\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T01:19:58.812Z\", \"updated_at\": \"2026-05-17T03:01:06.065Z\", \"hypothesis\": \"KL predictor 在 70% 极端稀疏度 (beyond-critical regime) + global top-k 下的 PPL——与 TEAL 70% (100.11) 对比量化 KL 优势在高稀疏度下是否放大（预期 advantage ratio >5×）\", \"metrics\": {\"wikitext2_ppl\": 17.91, \"dense_ppl\": 6.12, \"actual_sparsity\": 0.7, \"source\": \"kl_sparsity70_s42_v2 (teal_global_masks protocol)\", \"vanilla_teal_ppl\": 100.11}, \"conclusion\": \"success\"}, \"bench_kl50_global\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T07:04:18.606Z\", \"updated_at\": \"2026-05-17T03:01:03.243Z\", \"hypothesis\": \"KL 50% + global top-k 在统一 few-shot 协议下的 downstream 崩溃程度——量化 global allocation 导致的知识层 over-pruning 严重性（MMLU 预期<30%，接近随机，确认 global top-k 在 50% 下不可用于知识任务）\", \"conclusion\": \"success\", \"metrics\": {\"wikitext2_ppl\": 11.7933, \"arc_challenge_acc_norm\": 0.3285, \"winogrande_acc\": 0.6346, \"mmlu_acc\": 0.2789, \"gsm8k_exact_match\": 0.0129, \"actual_sparsity\": 0.5}}, \"bench_kl30_uniform\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T07:04:04.454Z\", \"updated_at\": \"2026-05-17T03:00:59.902Z\", \"hypothesis\": \"KL 30% + uniform per-layer allocation 在统一 few-shot 协议下同时保持低 PPL 和较好 downstream——验证此为论文推荐的实用配置（PPL/downstream/latency 最佳平衡点，MMLU 预期>35%）\", \"metrics\": {\"wikitext2_ppl\": 8.8157, \"arc_challenge_acc_norm\": 0.4078, \"winogrande_acc\": 0.6859, \"mmlu_acc\": 0.4061, \"gsm8k_exact_match\": 0.0735, \"actual_sparsity\": 0.3}, \"conclusion\": \"success\"}, \"eval_kl30_teal_30pct\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T05:15:54.042Z\", \"updated_at\": \"2026-05-17T03:00:57.138Z\", \"hypothesis\": \"KL 30% predictor 在 sparsity_target=0.3 条件下的真实 TEAL PPL——验证之前 13.63 是否由 evaluate.py 默认 target=0.5 导致虚高（正确值预期接近 9.0 而非 13.6）\", \"conclusion\": \"success\", \"metrics\": {\"dense_ppl\": 6.12, \"predictor_hard_mask_ppl\": 7.3, \"teal_sparse_ppl\": 8.98, \"sparsity_target\": 0.3, \"actual_sparsity\": 0.3}}, \"bench_dense\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T05:10:27.292Z\", \"updated_at\": \"2026-05-17T03:00:54.085Z\", \"hypothesis\": \"Dense LLaMA-3.1-8B 在 benchmark_eval.py 统一 few-shot 协议 (ARC-c 25-shot, WG 5-shot, MMLU 5-shot, GSM8K 8-shot) 的基准分——所有 sparse 方法对比的上界，任何 sparse 配置超过此值即为评估 bug\", \"metrics\": {\"wikitext2_ppl\": 6.1173, \"arc_challenge_acc\": 0.5478, \"arc_challenge_acc_norm\": 0.5828, \"winogrande_acc\": 0.7806, \"mmlu_acc\": 0.6527, \"gsm8k_exact_match\": 0.4875}, \"conclusion\": \"success\"}, \"kl_sparsity30_s42_v2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T20:30:30.528Z\", \"updated_at\": \"2026-05-17T03:00:50.360Z\", \"hypothesis\": \"KL distillation 在 30% 温和稀疏度下能用 lambda_max=1000 稳定收敛到目标——如果 sparsity 不达标则说明 Lagrangian cap 需要按目标稀疏度级别调整（低 sparsity 需要更高 cap 来平衡小 constraint 信号）\", \"conclusion\": \"negative\", \"metrics\": {\"final_loss\": 0.1465, \"kl_normalized\": 0.1465, \"kl_raw\": 0.1465, \"model_level_sparsity\": 0.281, \"sparsity_target\": 0.3, \"lambda_sparse_final\": 1000, \"lambda_max_cap\": 1000, \"tau_final\": 0.1, \"constraint_loss_final\": 0, \"training_steps\": 1000, \"wall_clock_seconds\": 2662.6, \"gpu_hours\": 0.74, \"note\": \"No PPL evaluation in training script. Sparsity stuck at 0.281 (same as v1). Lambda hit cap=1000 by step 220 and could not push sparsity further. W&B run was offline (not synced).\"}}, \"bce_gumbel_lagrangian_isolation\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T20:58:31.768Z\", \"updated_at\": \"2026-05-17T03:00:37.906Z\", \"metrics\": {\"lr_1e4_ppl\": 42.99, \"lr_1e3_ppl\": 48.4, \"lr_3e3_ppl\": 38.02, \"lr_1e4_bce_loss\": 0.7158, \"lr_1e3_bce_loss\": 0.6781, \"lr_3e3_bce_loss\": 0.6632, \"lr_1e4_sparsity\": 0.514, \"lr_1e3_sparsity\": 0.506, \"lr_3e3_sparsity\": 0.504, \"best_ppl\": 38.02, \"best_lr\": \"3e-3\", \"kl_baseline_ppl\": 11.79, \"gap_vs_kl\": 26.23}, \"conclusion\": \"success\", \"hypothesis\": \"消融分离 Gumbel-sigmoid 和 Lagrangian 对 KL 训练成功的各自贡献——确认两者都是必要组件（去掉任一导致 sparsity collapse 或 PPL 显著退化）还是其中之一可省\"}, \"eval_c4_ood_kl50\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T19:12:11.039Z\", \"updated_at\": \"2026-05-17T03:00:36.669Z\", \"metrics\": {\"dense_ppl\": 9.2075, \"kl_50_global_ppl\": 18.401, \"teal_50_ppl\": 38.7503, \"kl_vs_dense_ratio\": 2, \"teal_vs_dense_ratio\": 4.21}, \"conclusion\": \"success\", \"hypothesis\": \"KL predictor (WikiText-103 训练) 在 C4 OOD 数据上仍保持有效性（PPL 退化<15% vs in-distribution）——验证 predictor 学到的 neuron 重要性 pattern 是通用的而非 overfit 训练分布\"}, \"longbench_kl30_uniform_v6\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T16:56:19.111Z\", \"updated_at\": \"2026-05-17T03:00:35.333Z\", \"metrics\": {\"longbench_narrativeqa\": 4.12, \"longbench_qasper\": 6.23, \"longbench_gov_report\": 16.97, \"longbench_multi_news\": 18.01, \"runtime_seconds\": 6156.6}, \"conclusion\": \"negative\", \"notes\": \"LongBench KL 30% uniform: 3/4 任务显著低于 dense baseline（narrativeqa -44%, qasper -54%, gov_report -44%）。multi_news 异常高于 dense 但 dense baseline 本身极低(2.5)，可能是评估噪声。结论：uniform allocation 在长上下文任务上不如 dense，不纳入论文主体。\", \"parent\": \"longbench_dense_v6\", \"hypothesis\": \"KL 30% uniform 在 LongBench 长上下文任务能保持接近 dense 水平（差异<20%）——如果显著退化则说明 uniform per-layer budget 对长上下文中注意力依赖层的 neuron 保留不足\"}, \"longbench_dense_v6\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T15:37:54.958Z\", \"updated_at\": \"2026-05-17T03:00:33.325Z\", \"conclusion\": \"success\", \"metrics\": {\"longbench_narrativeqa\": 7.3, \"longbench_qasper\": 13.4, \"longbench_gov_report\": 30.5, \"longbench_multi_news\": 2.5}, \"hypothesis\": \"Dense LLaMA 在 LongBench 长上下文任务 (NarrativeQA, Qasper, GovReport, MultiNews) 的基准分——作为 KL sparse 条件在长上下文场景的参照上界\"}, \"bench_kl50_uniform_s456\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T14:27:20.124Z\", \"updated_at\": \"2026-05-17T03:00:32.121Z\", \"metrics\": {\"wikitext2_ppl\": 11.9604, \"arc_challenge_acc_norm\": 0.3345, \"winogrande_acc\": 0.6275, \"mmlu_acc\": 0.2874, \"gsm8k_exact_match\": 0.0212, \"actual_sparsity\": 0.5}, \"conclusion\": \"success\", \"hypothesis\": \"KL 50% uniform multi-seed (s456) 统一协议评测——验证 PPL 结果跨种子稳定性（与 s42 差异<0.5 PPL 即确认 CV<1%）\"}, \"bench_kl50_uniform_s123\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T14:27:17.469Z\", \"updated_at\": \"2026-05-17T03:00:31.166Z\", \"metrics\": {\"wikitext2_ppl\": 11.83, \"arc_challenge_acc_norm\": 0.3515, \"winogrande_acc\": 0.6298, \"mmlu_acc\": 0.2751, \"gsm8k_exact_match\": 0.0235, \"actual_sparsity\": 0.5}, \"conclusion\": \"success\", \"hypothesis\": \"KL 50% uniform multi-seed (s123) 统一协议评测——验证 PPL 结果跨种子稳定性（与 s42 差异<0.5 PPL 即确认 CV<1%）\"}, \"latency_benchmark\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T14:06:00.262Z\", \"updated_at\": \"2026-05-17T03:00:24.496Z\", \"conclusion\": \"success\", \"metrics\": {\"gpu_model\": \"NVIDIA RTX PRO 6000 Blackwell Server Edition\", \"dtype\": \"float16\", \"attn\": \"flash_attention_2\", \"batch\": 1, \"seq_len\": 2048, \"warmup\": 10, \"iters\": 100, \"dense_ms\": 119.11, \"dense_std\": 0.57, \"dense_tokens_per_s\": 17194.5, \"kl_30pct_ms\": 126.64, \"kl_30pct_std\": 0.7, \"kl_30pct_tokens_per_s\": 16171.8, \"kl_30pct_speedup\": 0.941, \"kl_50pct_ms\": 126.78, \"kl_50pct_std\": 0.31, \"kl_50pct_tokens_per_s\": 16154.2, \"kl_50pct_speedup\": 0.939, \"comp_30pct_ms\": 129.94, \"comp_30pct_std\": 0.75, \"comp_30pct_tokens_per_s\": 15761.4, \"comp_30pct_speedup\": 0.917, \"comp_50pct_ms\": 129.71, \"comp_50pct_std\": 0.53, \"comp_50pct_tokens_per_s\": 15788.8, \"comp_50pct_speedup\": 0.918, \"predictor_overhead_ms\": 3.17, \"predictor_overhead_pct\": 2.7, \"per_layer_predictor_ms\": 0.099, \"dense_ffn_per_layer_ms\": 2.427, \"sparse_ffn_pred_per_layer_ms\": 2.686, \"compensation_overhead_ms\": 3.3}, \"hypothesis\": \"KL predictor 的推理 latency overhead <10%（相对 dense baseline）——验证 predictor forward pass 不构成实用性瓶颈，支撑 practical deployment claim\"}, \"bench_kl40_global\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T12:20:14.275Z\", \"updated_at\": \"2026-05-17T03:00:21.964Z\", \"conclusion\": \"success\", \"metrics\": {\"wikitext2_ppl\": 10.117, \"arc_challenge_acc_norm\": 0.4096, \"winogrande_acc\": 0.6535, \"mmlu_acc\": 0.3806, \"gsm8k_exact_match\": 0.05, \"actual_sparsity\": 0.4}, \"hypothesis\": \"KL 40% + global top-k 统一协议评测——定位 budget-neutral 到 budget-deficit 转折点的精确退化程度，与 30%/50% 构成连续 sparsity 曲线\"}, \"bench_kl50_uniform\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T09:40:34.336Z\", \"updated_at\": \"2026-05-17T03:00:20.321Z\", \"conclusion\": \"success\", \"metrics\": {\"wikitext2_ppl\": 11.963, \"arc_challenge_acc_norm\": 0.3276, \"winogrande_acc\": 0.629, \"mmlu_acc\": 0.2777, \"gsm8k_exact_match\": 0.0212, \"actual_sparsity\": 0.5}, \"hypothesis\": \"KL 50% + uniform per-layer allocation 在统一协议下的 PPL 和 downstream——验证 uniform allocation 在 50% 下是否比 global top-k 保留更好的知识能力（MMLU 差异是否显著）\"}, \"bench_teal50\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T09:40:31.432Z\", \"updated_at\": \"2026-05-17T03:00:16.203Z\", \"conclusion\": \"success\", \"metrics\": {\"wikitext2_ppl\": 23.31, \"arc_challenge_acc_norm\": 0.2841, \"winogrande_acc\": 0.5304, \"mmlu_acc\": 0.2832, \"gsm8k_exact_match\": 0.0197, \"actual_sparsity\": 0.5}, \"hypothesis\": \"TEAL 50% training-free baseline 统一协议评测——量化 KL predictor 在中等 sparsity 下相对 TEAL 的 PPL 优势幅度（预期 KL/TEAL ratio >1.5×）\"}, \"bench_teal30\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T09:40:29.575Z\", \"updated_at\": \"2026-05-17T03:00:14.912Z\", \"conclusion\": \"success\", \"metrics\": {\"wikitext2_ppl\": 10.97, \"arc_challenge_acc_norm\": 0.4232, \"winogrande_acc\": 0.6606, \"mmlu_acc\": 0.3861, \"gsm8k_exact_match\": 0.0788, \"actual_sparsity\": 0.3}, \"hypothesis\": \"TEAL 30% training-free baseline 统一协议评测——量化 KL predictor 在低 sparsity 下相对 TEAL 的 PPL 优势幅度（预期 KL/TEAL ratio >1.2×）\"}, \"bench_kl30_global\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T09:36:59.346Z\", \"updated_at\": \"2026-05-17T03:00:13.448Z\", \"conclusion\": \"success\", \"metrics\": {\"wikitext2_ppl\": 8.9768, \"arc_challenge_acc_norm\": 0.3968, \"winogrande_acc\": 0.7017, \"mmlu_acc\": 0.2527, \"gsm8k_exact_match\": 0.0879, \"actual_sparsity\": 0.3}, \"hypothesis\": \"KL 30% predictor + global top-k allocation 的统一协议评测——与 uniform allocation 对比确认 global top-k 在低 sparsity 下是否仍导致知识层 over-pruning（MMLU 差异>5pp 即确认）\"}, \"lm_eval_dense\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T22:39:59.634Z\", \"updated_at\": \"2026-05-17T02:59:46.203Z\", \"metrics\": {\"arc_challenge_acc_norm\": 0.5819, \"winogrande_acc\": 0.7814, \"mmlu_acc\": 0.6532, \"gsm8k_exact_match\": 0.5004, \"eval_tasks\": [\"arc_challenge\", \"winogrande\", \"mmlu\", \"gsm8k\"], \"model\": \"llama-3.1-8b\", \"condition\": \"dense\", \"server\": \"westd-34887\"}, \"conclusion\": \"success\", \"hypothesis\": \"Dense LLaMA-3.1-8B 在 lm-eval-harness 标准 downstream benchmark (ARC-c, WG, MMLU, GSM8K) 的基准分——所有 sparse 条件对比的参照上界\"}, \"lm_eval_kl_s42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T22:34:42.788Z\", \"updated_at\": \"2026-05-17T02:59:43.893Z\", \"notes\": \"## lm-eval Results (2026-05-16)\\n\\n| Task | Dense | KL Sparse 50% | Drop |\\n|------|-------|---------------|------|\\n| arc_challenge | 0.5819 | 0.3771 | -35.2% |\\n| winogrande | 0.7814 | 0.6156 | -21.2% |\\n| mmlu | 0.6532 | 0.2591 | -60.3% |\\n| gsm8k | 0.5004 | 0.0121 | -97.6% |\\n\\nEXIT_CODE=129 (SIGHUP). 结果保存在 plan_007/ 目录。\\n\\n### acc_norm 确认 (worker 验证)\\n所有指标已正确使用 acc_norm（可用时），无需修正。MMLU 无 acc_norm。\\n\\n### Mask 逻辑审查 (worker 验证) — 无 bug\\n- Mask shape/type/位置/predictor checkpoint 全部正确\\n- HFLM 透传验证：logit diff = 0.000000（patch 完整保留到 lm-eval）\\n- Per-token sparsity 动态工作：content words 保留更多 neurons\\n- 平均 sparsity 0.5031 ≈ 目标 0.50\\n\\n### 根因确认：PPL-Downstream Disconnect 是真实现象\\n\\\"Paris\\\" 从 dense top-2 (16.0) 降到 sparse top-5 (14.81)。logit 微小偏移足以翻转 4-choice 答案。\\n- PPL 是平均指标 → 多数 token 合理即可\\n- MMLU/GSM8K 要求精确知识检索 → 单个 token logit 偏移即致命\\n- Predictor 在 C4/WikiText 上训练，优化 PPL 而非 downstream accuracy\\n\\n### \\\"A\\\" Token Bias (debug worker 诊断)\\nSparse model MMLU letter-choice 下系统性偏好 \\\"A\\\"。是深层表征损伤的症状。\\n\\n### 服务器进程状态 (00:35 UTC)\\n- cuda:0: PID 181121 (Mistral dense gsm8k) — debug 进程已被 kill\\n- cuda:1: PID 174850 (Mistral KL gsm8k), PID 179918 (KL sparse rerun)\", \"metrics\": {\"arc_challenge_acc_norm\": 0.3771, \"winogrande_acc\": 0.6156, \"mmlu_acc\": 0.2591, \"gsm8k_exact_match\": 0.0121, \"eval_tasks\": [\"arc_challenge\", \"winogrande\", \"mmlu\", \"gsm8k\"], \"model\": \"llama-3.1-8b\", \"condition\": \"kl_sparse_50pct\", \"server\": \"westd-34887\", \"exit_code\": 129, \"wall_time_sec\": 3010, \"flag\": \"SUSPECT — gsm8k 0.50→0.01 catastrophic drop; PID 179918 rerunning with lm_eval_sparse.py\"}, \"conclusion\": \"negative\", \"hypothesis\": \"KL predictor 的 PPL 优势 (9.21 vs dense 6.12) 能转化为 downstream task (ARC-c, WG, MMLU, GSM8K) 的保持——如果 downstream 崩溃而 PPL 良好则揭示 PPL-downstream disconnect 现象\"}, \"kl_sparsity70_s42_v2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T20:34:18.823Z\", \"updated_at\": \"2026-05-17T02:59:42.831Z\", \"metrics\": {\"true_dense_ppl\": 6.12, \"predictor_hard_mask_ppl\": 13.84, \"predictor_teal_sparse_ppl\": 17.91, \"vanilla_teal_sparse_ppl\": 100.11, \"teal_sparse_ppl\": 17.91, \"teal_sparse_ppl_static_baseline\": 17.91, \"model_level_sparsity\": 0.7, \"teal_sparse_note\": \"17.91 = predictor-based TEAL (teal_global_masks: predictor-gated magnitude scoring + global topk @70%). vanilla TEAL @70% = 100.11. 代码来源: quick_sp70.py L10 imports teal_global_masks, L60 调用. plan_007_all_ppl_fixed.json 的 mode=static_mask_70pct metadata 有误导性.\", \"eval_dataset\": \"wikitext-2\", \"eval_seq_len\": 2048, \"calibration_samples\": 32, \"per_layer_sparsity_range\": [0.508, 0.876]}, \"conclusion\": \"success\", \"notes\": \"## Training Analysis (2026-05-16)\\n\\n### Training Summary\\n- 1000/1000 steps completed, EXIT_CODE=0\\n- Sparsity converged to ~0.688 (target 0.70, within 0.65-0.75 success range)\\n- Lambda hit cap 1000 by step 10, tau annealed 0.999 → 0.100\\n- KL loss: 1.18 → 0.61\\n\\n### PPL Evaluation Results\\n- true_dense_ppl: 6.12\\n- predictor_hard_mask_ppl: **13.84** (per-token adaptive mask)\\n- teal_sparse_ppl: **17.91** (static global topk, FIXED via D017)\\n- model_level_sparsity: 0.699\\n\\n### D017 Bug Fix (2026-05-15)\\nOriginal teal_sparse_ppl=136,069 was caused by using raw sigmoid scores for global topk mask selection. Sigmoid probabilities lack magnitude information and are poor proxies for static neuron importance. Fix: score neurons by mean(|intermediate| * predictor_hard_mask) — activation magnitude weighted by predictor decisions. Also added per-layer mean normalization (from _global_topk_masks). Result: 136K → 17.91.\", \"hypothesis\": \"KL distillation 在 70% 极端稀疏度 (beyond-critical regime) 下仍能收敛且保持相对于 TEAL 的 PPL 优势——验证方法在高稀疏度下 advantage ratio 是否放大\"}, \"training_free_baselines\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T18:31:40.470Z\", \"updated_at\": \"2026-05-17T02:59:35.177Z\", \"conclusion\": \"success\", \"metrics\": {\"dense_ppl\": 6.12, \"vanilla_teal_global_ppl_30pct\": 10.97, \"vanilla_teal_global_ppl_50pct\": 23.31, \"vanilla_teal_global_ppl_70pct\": 100.11, \"wina_global_ppl_30pct\": 11.45, \"wina_global_ppl_50pct\": 27.93, \"wina_global_ppl_70pct\": 137.24, \"uniform_50pct_ppl\": 23.9, \"teal_greedy_ppl\": 33.47, \"vanilla_teal_global_ppl\": 23.31, \"wina_global_ppl\": 27.93, \"rsparse_global_ppl\": 151.2}, \"notes\": \"2026-05-16 全部用 D017 bugfix (per-layer mean normalization) 后代码统一重跑确认。三个 sparsity level 全部物理一致：30% < 50% < 70%。TEAL: 10.97 < 23.31 < 100.11, WINA: 11.45 < 27.93 < 137.24。旧 70% TEAL=17.91 是 predictor-based TEAL (非 vanilla TEAL)，不可直接比较。代码确认 _global_topk_masks 包含 per-layer mean normalization (s_f / mu)。环境: HF_DATASETS_OFFLINE=1, CUDA_VISIBLE_DEVICES=1, setup_env.sh sourced。\", \"hypothesis\": \"TEAL magnitude-based training-free pruning 在多个 sparsity level (30/50/70%) 的 PPL 表现——建立 KL predictor 的标准参照基线，量化\\\"需要训练\\\"带来的增量\"}, \"bce_comp_staged_s42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T17:27:26.983Z\", \"updated_at\": \"2026-05-17T02:59:32.249Z\", \"conclusion\": \"negative\", \"metrics\": {\"true_dense_ppl\": 6.12, \"predictor_hard_mask_ppl\": 25.44, \"predictor_hard_mask_ppl_no_comp\": 27.96, \"teal_sparse_ppl\": 44.54, \"model_level_sparsity\": 0.558, \"ppl_increase_vs_true_dense_pct\": 315.7, \"comp_loss_final\": 0.0033, \"bce_loss_final\": 0.6379, \"eval_seq_len\": 2048, \"calibration_samples\": 32}, \"notes\": \"BCE+Compensation staged training (200步BCE warmup + 800步joint). 训练正常完成1000步。Compensation带来约9%的per-token PPL改善(27.96→25.44)，但仍远差于KL-only(9.21)，差距2.8倍。TEAL路径不经过comp network，PPL=44.54与BCE-only一致。训练曲线：comp_loss从Phase2开始的0.0053稳定下降至0.0033，说明comp网络在学习但改善空间有限。⚠️ Sparsity mismatch: BCE+comp model_level_sparsity=0.558 vs KL model_level_sparsity=0.498。论文对比时必须标注此差异——BCE+comp 稀疏度更高意味着其 PPL 劣势可能被低估。结论：compensation不能弥补BCE损失函数的根本缺陷——不区分neuron重要性。强化Claim 1：KL distillation通过端到端输出对齐隐式学到neuron重要性排序，是更优方案。\", \"hypothesis\": \"BCE predictor + 后置 error compensation 能缩小与 KL-only 的 PPL 差距——如果差距仍>2× 则说明 BCE 损失函数本身（非 compensation 不足）是根本限制\"}, \"spon_training\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T17:27:18.117Z\", \"updated_at\": \"2026-05-17T02:59:29.428Z\", \"notes\": \"## 训练概要\\n1000 steps 正常完成，loss 波动在 0.38-0.47 区间，未有效收敛。Bias norm 从 0→0.041 后在 step 700 饱和。LR cosine+warmup 正常 (1e-5→0)。仅 458K/8B 可训练参数 (0.0057%)。\\n\\n## WikiText-2 评估 (seq_len=2048, 141 sequences)\\n- True Dense PPL: 6.12\\n- Per-token sparse PPL (predictor hard mask, no SPON): 9.22 (+50.6%)\\n- Per-token sparse + SPON PPL: 9.10 (+48.7%)\\n- SPON recovery: 仅 3.8% of sparse-vs-dense gap (0.12 PPL improvement)\\n- TEAL global mask sparse PPL (from KL-only eval): 12.08\\n\\n## 结论: **Negative**\\nSPON bias 补偿效果极其微弱，仅恢复 3.8% 的稀疏化误差。可能原因：\\n1. Bias norm 极小 (mean=0.041) 且提前饱和，说明学习容量不足或信号太弱\\n2. 训练 seq_len=128 vs eval seq_len=2048 的 mismatch 可能削弱效果\\n3. Per-token predictor hard mask 本身已经较好 (sparse PPL 9.22 vs TEAL global 12.08)，残余误差可能不是简单的 additive bias 能补偿的\\n\\n## Claim 2 影响\\nSPON + KL predictor 的加性组合改善微不足道。如果要验证 Claim 2，可能需要：(a) 更高表达力的补偿机制替代 static bias，或 (b) 更长 seq_len 训练，或 (c) 在 TEAL global mask 场景下测试 SPON（误差更大，补偿空间更大）。\", \"conclusion\": \"negative\", \"metrics\": {\"true_dense_ppl\": 6.1193, \"predictor_hard_mask_ppl\": 9.2165, \"spon_sparse_ppl\": 9.0977, \"spon_recovery_pct\": 3.8, \"ppl_improvement_from_spon\": 0.1188, \"ppl_increase_vs_true_dense_pct\": 48.7, \"ppl_increase_no_spon_vs_true_dense_pct\": 50.6, \"mean_bias_norm\": 0.040596, \"max_bias_norm\": 0.054199, \"teal_sparse_ppl\": 12.08, \"teal_with_spon_ppl\": 11.93, \"spon_dense_ppl_degradation\": 6.19, \"model_level_sparsity\": 0.5, \"eval_seq_len\": 2048, \"eval_samples\": 141, \"trainable_params\": 458752, \"trainable_pct\": 0.0057}, \"hypothesis\": \"SPON static bias correction 能显著恢复（>10%）稀疏化引入的 output 误差——如果恢复率<10% 则说明 static additive bias 无法补偿 contextual sparsity 的 token 级动态误差\"}, \"kl_only_s1\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T17:19:37.074Z\", \"updated_at\": \"2026-05-17T02:59:26.550Z\", \"conclusion\": \"success\", \"metrics\": {\"true_dense_ppl\": 6.12, \"predictor_hard_mask_ppl\": 9.15, \"teal_sparse_ppl\": 11.99, \"model_level_sparsity\": 0.498, \"ppl_increase_vs_true_dense_pct\": 96}, \"notes\": \"训练 1000 步正常完成，最终 loss=0.332, sparsity=0.484, lambda=1000。WikiText-2 评估：true_dense=6.12, hard_mask=9.15, teal_sparse=11.99, sparsity=0.498, PPL increase=31.0%。\\\\n\\\\n## 5-seed 汇总表 (KL normalized v3)\\\\n| Metric | s0 | s1 | s42 | s123 | s456 | Mean ± Std |\\\\n|--------|----|----|-----|------|------|------------|\\\\n| Dense PPL | 9.19 | 9.15 | 9.21 | 9.25 | 9.14 | 9.19 ± 0.04 |\\\\n| Sparse PPL | 12.03 | 11.99 | 12.08 | 11.91 | 13.58 | 12.32 ± 0.71 |\\\\n| PPL increase | 30.9% | 31.0% | 31.2% | 28.8% | 48.6% | 34.1% ± 8.2% |\\\\n\\\\n5-seed headline: sparse PPL 12.32 ± 0.71 (排除 s456 异常值后 4-seed mean=12.00 ± 0.07)。s1 是 5-seed 中最优（sparse PPL 11.99, dense PPL 9.15），确认 KL normalized v3 seed 鲁棒性良好。\", \"hypothesis\": \"Pure KL distillation 训练动态 multi-seed (seed=1) 验证：无约束 KL 的自然 sparsity emergence pattern 是否跨种子稳定\"}, \"kl_only_s0\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T17:19:35.138Z\", \"updated_at\": \"2026-05-17T02:59:24.175Z\", \"conclusion\": \"success\", \"metrics\": {\"true_dense_ppl\": 6.12, \"predictor_hard_mask_ppl\": 9.19, \"teal_sparse_ppl\": 12.03, \"model_level_sparsity\": 0.499, \"ppl_increase_vs_true_dense_pct\": 96.57, \"eval_seq_len\": 2048, \"calibration_samples\": 32}, \"notes\": \"训练 1000 步正常完成，最终 loss=0.305, sparsity=0.488, lambda=1000。\\\\n\\\\n## WikiText-2 评估 (seq_len=2048 重跑)\\\\n**2026-05-15 重跑原因**: 原 eval 使用 --seq_len 1024，与其他 seed (s1/s42/s123/s456) 的 2048 不一致，结果不可比。已用 seq_len=2048 重跑，结果与原始一致。\\\\n- true_dense_ppl: 6.12\\\\n- predictor_hard_mask_ppl (Dense PPL): 9.19\\\\n- teal_sparse_ppl (Sparse PPL): 12.03\\\\n- model_level_sparsity: 0.499\\\\n- ppl_increase_vs_true_dense_pct: 96.57%\\\\n\\\\n## 5-seed 汇总表 (KL normalized v3)\\\\n| Metric | s0 | s1 | s42 | s123 | s456 | Mean ± Std |\\\\n|--------|----|----|-----|------|------|------------|\\\\n| Dense PPL | 9.19 | 9.15 | 9.21 | 9.25 | 9.14 | 9.19 ± 0.04 |\\\\n| Sparse PPL | 12.03 | 11.99 | 12.08 | 11.91 | 13.58 | 12.32 ± 0.71 |\\\\n| PPL increase | 30.9% | 31.0% | 31.2% | 28.8% | 48.6% | 34.1% ± 8.2% |\\\\n\\\\n5-seed headline: sparse PPL 12.32 ± 0.71 (排除 s456 异常值后 4-seed mean=12.00 ± 0.07)。s0 结果与 s42/s123 高度一致，确认 KL normalized v3 seed 鲁棒性良好。s456 仍为唯一异常值。\", \"hypothesis\": \"Pure KL distillation（无 sparsity constraint）的训练动态：验证 KL loss 是否自然产生 sparse gate pattern，还是需要显式 sparsity 约束引导\"}, \"mvp_kl_norm_v2_s456\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T15:19:33.798Z\", \"updated_at\": \"2026-05-17T02:59:22.263Z\", \"metrics\": {\"true_dense_ppl\": 6.1173, \"predictor_hard_mask_ppl\": 9.14, \"teal_sparse_ppl\": 13.58, \"model_level_sparsity\": 0.498, \"ppl_increase_vs_true_dense_pct\": 121.9, \"eval_md5\": \"f4086818bb55dc354ea4c6fe8ed8899a\", \"calibration_samples\": 32, \"vanilla_teal_sparse_ppl_INVALID\": 66036.4062}, \"notes\": \"## 训练指标 (1000 steps)\\n- 最终 kl_raw: ~0.29-0.32, sparsity: 0.480-0.488, lambda: 1000 (饱和), tau: 0.1\\n- 训练正常完成，无报错\\n\\n## WikiText-2 评估\\n- True Dense PPL: 6.12\\n- Dense/Hard-mask PPL: 9.14\\n- TEAL Sparse PPL: 13.58\\n- PPL increase: 48.6%\\n- Model sparsity: 0.498\\n\\n## s456 Outlier 根因分析 (2026-05-15)\\n训练端完全正常（loss/sparsity/lambda 与其他 seed 一致）。问题在 TEAL 推理时的全局 topk 分配：\\n- s456 predictor 对 Layer 31 的 sigmoid 均分 = 0.5161（其他 4 seed 均值 = 0.5287，差 -0.0126）\\n- TEAL 将 Layer 31 keep ratio 压到 49.9%（其他 seed 52.1%），Layer 31 直连 LM head，微小剪枝差异被放大\\n- Layer 12 也偏低（-431 neurons），预算被挤向 Layer 7（+771 neurons）\\n- Hard-mask PPL 不受影响因为 per-token mask 不经过全局 topk\\n结论：不需要重跑。是 TEAL 全局分配的放大效应，非 predictor 质量问题。\\n论文报告建议：报 4-seed mean=12.00±0.07 + 注明 s456 为 TEAL 分配 outlier。\", \"conclusion\": \"success\", \"parent\": \"mvp_kl_norm_v2_s42\", \"hypothesis\": \"KL normalized predictor multi-seed 验证 (seed=456)：方法有效性不依赖种子选择，sparse PPL 应与 s42 (12.08) 一致（CV<5%）\"}, \"mvp_kl_norm_v2_s123\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T15:19:03.245Z\", \"updated_at\": \"2026-05-17T02:59:20.835Z\", \"metrics\": {\"true_dense_ppl\": 6.1173, \"predictor_hard_mask_ppl\": 9.2474, \"teal_sparse_ppl\": 11.9128, \"model_level_sparsity\": 0.4979, \"ppl_increase_vs_true_dense_pct\": 94.7, \"eval_md5\": \"f4086818bb55dc354ea4c6fe8ed8899a\", \"calibration_samples\": 32, \"vanilla_teal_sparse_ppl_INVALID\": 66036.4062}, \"conclusion\": \"success\", \"notes\": \"KL normalized v3 (÷seq_len only), seed=123, 1000步训练。\\n\\n## WikiText-2 评估\\n| 指标 | KL s123 | BCE s123 |\\n|------|---------|----------|\\n| Dense PPL | 9.25 | 28.38 |\\n| Sparse PPL | 11.91 | 44.59 |\\n| PPL increase | 28.8% | 57.1% |\\n| Sparsity | 0.498 | 0.496 |\\n\\n## 结论: SUCCESS\\nKL normalized loss 在所有指标上显著优于 BCE。与 KL s42 高度一致（sparse PPL 11.91 vs 12.08），seed 稳定性良好。\", \"parent\": \"mvp_kl_norm_v2_s42\", \"hypothesis\": \"KL normalized predictor multi-seed 验证 (seed=123)：方法有效性不依赖种子选择，sparse PPL 应与 s42 (12.08) 一致（CV<5%）\"}, \"mvp_kl_norm_v2_s42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T15:19:01.567Z\", \"updated_at\": \"2026-05-17T02:59:19.006Z\", \"metrics\": {\"true_dense_ppl\": 6.1173, \"predictor_hard_mask_ppl\": 9.2142, \"teal_sparse_ppl\": 12.0776, \"model_level_sparsity\": 0.4979, \"ppl_increase_vs_true_dense_pct\": 97.4, \"eval_md5\": \"f4086818bb55dc354ea4c6fe8ed8899a\", \"calibration_samples\": 32, \"vanilla_teal_sparse_ppl_INVALID\": 66036.4062}, \"notes\": \"KL normalized v2 (÷seq_len only, 修复 ÷vocab_size bug) + Lagrangian, 1000步训练。\\n\\n## 训练指标\\n- KL loss: 1.18→0.49(step100)→0.26(step500)→0.30(step1000)\\n- Sparsity: 0.406→0.492→0.484→0.488, 稳定接近 target=0.5\\n- Lambda 收敛到 cap=1000, constraint=0 (满足约束)\\n\\n## WikiText-2 评估 (同一 evaluate.py 做公平对比)\\n|  | KL norm v2 (s42) | BCE (s42 rerun) |\\n|--|------------------|-----------------|\\n| Dense(hard mask) PPL | 9.21 | 27.96 |\\n| Sparse(TEAL) PPL | 12.08 | 44.54 |\\n| PPL increase | 31.2% | 59.3% |\\n| Model sparsity | 0.498 | 0.496 |\\n\\n## 重要发现\\nevaluate.py 的 \\\"Dense baseline\\\" 实际是通过 predictor hard mask 的评估（PredictorWrapper._patch_mlps() monkey-patch 所有 MLP，forward_dense() 执行后 sparse_mode 重置为 True）。因此 \\\"dense\\\" PPL 反映的是 predictor per-token hard mask 质量，而非真 dense 模型性能。\\n\\nKL predictor hard mask PPL (9.21) 接近真 dense (~8-9), 说明其学会了精准识别不重要 neuron。BCE hard mask PPL (27.96) 远差于真 dense，说明 BCE predictor 误杀重要 neuron。\\n\\n## Per-layer sparsity 分布差异\\n- KL: 非均匀 (0.215-0.806), 中间层低稀疏(保护), 后层高稀疏\\n- BCE: 较均匀 (0.430-0.664), 后层略高\\n\\n## 结论: SUCCESS\\nKL normalized loss 在所有指标上显著优于 BCE: TEAL sparse PPL 12.08 vs 44.54, PPL increase 31.2% vs 59.3%。\", \"conclusion\": \"success\", \"parent\": \"kl_lagrangian_quicktest\", \"hypothesis\": \"Per-token KL normalized loss (÷seq_len, 修复 ÷vocab_size bug) + 高 lambda_max Lagrangian 能同时解决量级不匹配和稀疏性坍塌，稳定收敛到 50% sparsity 且 PPL 显著优于 BCE\"}, \"kl_lagrangian_quicktest\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T13:17:49.894Z\", \"updated_at\": \"2026-05-17T02:59:15.944Z\", \"conclusion\": \"negative\", \"metrics\": {\"final_kl_loss\": 418, \"final_constraint_loss\": 1.211, \"final_sparsity\": 0.141, \"final_lambda\": 5.06, \"steps\": 200, \"sparsity_trajectory\": [0.406, 0.387, 0.289, 0.168, 0.141]}, \"notes\": \"NEGATIVE: Lagrangian 仍无法阻止稀疏性坍塌。Sparsity 0.406→0.141。根因: KL loss (~418) vs constraint (~1.2)，3 个数量级差距。lambda ×1.5 增长太慢 + cap=100 不够。即使 lambda=100, constraint=36 仍远小于 KL=418。梯度信号不足: clamp 约束项的梯度被 vocab 维度 KL 梯度淹没。\", \"parent\": \"mvp_kl_s42\", \"hypothesis\": \"Lagrangian multiplier 自适应约束（lambda ×1.5 增长, cap=100）能解决 mvp_kl_s42 中固定 reg_weight 导致的稀疏性坍塌——如果仍坍塌则说明 KL/constraint 量级差需要更激进的 lambda 策略\"}, \"mvp_bce_s456\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T11:51:08.412Z\", \"updated_at\": \"2026-05-17T02:59:12.511Z\", \"notes\": \"训练完成 1000/1000 步，checkpoint 已保存。EXIT_CODE=129 (SIGHUP) 发生在 checkpoint save 之后、evaluation 之前。训练指标与 s42/s123 高度一致 (bce_loss=0.6388, sparsity=0.551)。待评估 WikiText-2 PPL。\", \"conclusion\": \"success\", \"metrics\": {\"true_dense_ppl\": 6.1173, \"predictor_hard_mask_ppl\": 28.1437, \"teal_sparse_ppl\": 43.033, \"model_level_sparsity\": 0.4957, \"ppl_increase_vs_true_dense_pct\": 603.3, \"eval_md5\": \"f4086818bb55dc354ea4c6fe8ed8899a\", \"calibration_samples\": 32, \"vanilla_teal_sparse_ppl_INVALID\": 66036.4062}, \"hypothesis\": \"BCE predictor multi-seed 验证 (seed=456)：BCE 方法有效性不依赖种子选择，PPL 应与 s42 一致（CV<5%）\"}, \"mvp_bce_s123\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T11:51:07.010Z\", \"updated_at\": \"2026-05-17T02:59:11.198Z\", \"metrics\": {\"true_dense_ppl\": 6.1173, \"predictor_hard_mask_ppl\": 28.3817, \"teal_sparse_ppl\": 44.5864, \"model_level_sparsity\": 0.4957, \"ppl_increase_vs_true_dense_pct\": 629, \"eval_md5\": \"f4086818bb55dc354ea4c6fe8ed8899a\", \"calibration_samples\": 32, \"vanilla_teal_sparse_ppl_INVALID\": 66036.4062}, \"notes\": \"BCE loss, seed=123, 1000 steps. 训练正常完成，无报错。\\n\\n与 mvp_bce_s42 对比:\\n| 指标 | s42 | s123 | 差异 |\\n|------|-----|------|------|\\n| final_total_loss | 0.643 | 0.6433 | +0.0003 |\\n| final_bce_loss | 0.6379 | 0.6382 | +0.0003 |\\n| final_reg_loss | 0.0051 | 0.0051 | 相同 |\\n| final_sparsity | 0.551 | 0.551 | 相同 |\\n| model_level_sparsity | 0.498 | 0.498 | 相同 |\\n| wikitext2_ppl_dense | 27.96 | 28.38 | +0.42 |\\n| wikitext2_ppl_sparse | 44.21 | 44.83 | +0.62 |\\n| ppl_increase_pct | 58.1% | 57.9% | -0.2pp |\\n| training_time_min | 25.5 | 15.4 | -10.1min (可能因GPU型号差异) |\\n\\n结论: 两个 seed 的结果高度一致。loss、sparsity、PPL 增幅几乎相同，seed 稳定性良好。dense PPL 略有差异（28.38 vs 27.96）属正常 WikiText-2 评估波动。逐层稀疏性分布呈前低后高模式（浅层 ~0.44-0.47，深层 ~0.59-0.65），与 TEAL 论文观察一致。\", \"conclusion\": \"success\", \"hypothesis\": \"BCE predictor multi-seed 验证 (seed=123)：BCE 方法有效性不依赖种子选择，PPL 应与 s42 一致（CV<5%）\"}, \"mvp_bce_s42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T11:51:05.131Z\", \"updated_at\": \"2026-05-17T02:59:08.627Z\", \"notes\": \"训练+评估完成。训练: 1000 steps, 25.5 min, BCE loss 0.6711→0.6430。评估: WikiText-2 PPL dense=27.96 → sparse=44.21 (+58.1%)。C4 评估跳过（离线模式无法 streaming 加载）。TEAL 逐层分布: 浅层~44-50%, 深层51-66%。注意: dense baseline 27.96 高于文献~6 因使用 packed chunks 非 sliding window，但 dense/sparse 对比公平。evaluate.py 有 off-by-one bug 已修复（原始 shift 重复导致错位）。58% PPL 增幅对 MVP 1000 steps 可接受，文献中充分训练可降至 1-5%。\", \"conclusion\": \"success\", \"metrics\": {\"true_dense_ppl\": 6.1173, \"predictor_hard_mask_ppl\": 27.9603, \"teal_sparse_ppl\": 44.537, \"model_level_sparsity\": 0.4957, \"ppl_increase_vs_true_dense_pct\": 628, \"eval_md5\": \"f4086818bb55dc354ea4c6fe8ed8899a\", \"calibration_samples\": 32, \"vanilla_teal_sparse_ppl_INVALID\": 66036.4062}, \"hypothesis\": \"BCE loss 训练 sparse gate predictor (seed=42) 在 50% sparsity 下能产生有效预测——作为 KL distillation 的对照基线，BCE 直接拟合 binary mask 而非蒸馏 dense output distribution\"}, \"mvp_kl_s42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T11:50:59.003Z\", \"updated_at\": \"2026-05-17T02:59:05.828Z\", \"notes\": \"NEGATIVE: 稀疏性坍塌。Sparsity 0.328→0.000 (step 500+ 全 0)。根因: KL loss (收敛 3.3) 远大于 reg (0.05)，66 倍差距，fixed reg_weight=0.1 完全压不住。KL 最优解是 sparse=dense (0% sparsity)。修复: Lagrangian multiplier 自适应约束（Director 批准）。\", \"conclusion\": \"negative\", \"metrics\": {\"final_total_loss\": 3.3438, \"final_kl_loss\": 3.2969, \"final_reg_loss\": 0.05, \"final_sparsity\": 0, \"steps\": 1000, \"tau_final\": 0.1, \"wikitext2_ppl_dense\": 6.12, \"wikitext2_ppl_sparse\": 455.93, \"wikitext2_ppl_increase_pct\": 7349, \"model_level_sparsity\": 0.372, \"checkpoint_path\": \"/root/distill_sparse_swiglu/checkpoints/mvp_kl_s42/predictor_kl.pt\"}, \"hypothesis\": \"Raw KL divergence loss 直接蒸馏 dense→sparse gate，结合固定 sparsity regularization (reg_weight=0.1)，能稳定收敛到目标 50% 稀疏度——如果 sparsity collapse 则说明 KL loss 量级远大于 reg 需要自适应平衡\"}, \"mistral_kl70_s42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T00:16:13.454Z\", \"updated_at\": \"2026-05-17T02:58:56.173Z\", \"hypothesis\": \"KL distillation predictor generalizes across architectures: Mistral-7B at 70% sparsity should show similar KL advantage over TEAL as LLaMA, validating cross-architecture claim\", \"metrics\": {\"kl_per_token_ppl\": 9.1086, \"kl_teal_global_ppl\": 13.3254, \"teal_baseline_ppl\": 61.716, \"dense_ppl\": 5.5238, \"kl_advantage_ratio\": 6.77, \"final_loss\": 0.3945, \"actual_sparsity\": 0.682}, \"conclusion\": \"success\", \"parent\": \"mistral_kl_s42\"}, \"mistral_kl30_s42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T00:16:12.670Z\", \"updated_at\": \"2026-05-17T02:58:55.221Z\", \"hypothesis\": \"KL distillation predictor generalizes across architectures: Mistral-7B at 30% sparsity should show similar KL advantage over TEAL as LLaMA, validating cross-architecture claim\", \"metrics\": {\"kl_per_token_ppl\": 6.048, \"kl_teal_global_ppl\": 6.7733, \"teal_baseline_ppl\": 8.3807, \"dense_ppl\": 5.5238, \"kl_advantage_ratio\": 1.386, \"ppl_vs_dense_pct\": 9.5}, \"conclusion\": \"success\", \"parent\": \"mistral_kl_s42\"}, \"plan_005_subsumption_s42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T20:20:21.300Z\", \"updated_at\": \"2026-05-17T02:58:53.349Z\", \"hypothesis\": \"验证 SPON bias correction 与 KL predictor mask 效应的关系：正交性、量级比、跨层非线性交互。结果支持 D010 \\\"marginal complement\\\" framing — SPON corrections are orthogonal and negligibly small (magnitude ratio 16%, cos_sim 0.20).\", \"metrics\": {\"linearity_ratio\": 0.2644, \"linearity_ratio_std\": 0.0073, \"magnitude_ratio\": 0.1578, \"magnitude_ratio_std\": 0.0088, \"cosine_similarity\": 0.1962, \"cosine_similarity_std\": 0.0268, \"predictor_effect_norm\": 482.65, \"spon_correction_norm\": 76.2, \"interaction_norm\": 147.74, \"num_samples\": 50, \"seq_len\": 2048, \"conclusion_type\": \"weak_subsumption\"}, \"conclusion\": \"success\", \"notes\": \"## Subsumption Test Results (50 samples, seq_len=2048)\\n\\n### 核心指标\\n- Linearity ratio: 0.264 ± 0.007 (cross-layer cascade non-linearity)\\n- Magnitude ratio: 0.158 ± 0.009 (SPON correction / predictor effect)\\n- Cosine similarity: 0.196 ± 0.027 (near-orthogonal)\\n\\n### Effect magnitudes\\n- ‖D(predictor)‖ = 482.65 (KL predictor logit shift)\\n- ‖D(SPON)‖ = 76.20 (SPON bias correction logit shift)\\n- ‖interaction‖ = 147.74 (cross-layer cascade non-linearity)\\n\\n### 结论：Informative — SPON corrections are orthogonal and negligibly small\\n\\n1. **SPON 与 mask 效应正交**：cos_sim ≈ 0.20，两种修正作用在不同维度\\n2. **SPON 量级微小**：仅为 predictor 效应的 16%（76 vs 483）\\n3. **逐层精确可加**：交互项（148）来源于跨层级联非线性（down_proj 是线性的，层内 mask+bias 严格可加），非层内交互\\n4. **支持 D010 \\\"marginal complement\\\" framing**：SPON 提供的是正交但微弱的补充，不构成有意义的 compositional gain\\n\\n⚠️ 不使用 \\\"subsumption\\\" 措辞——数据显示正交性而非包含关系。正确表述：SPON corrections are orthogonal to and much smaller than predictor mask effects; the non-zero interaction term arises from cross-layer cascading, not intra-layer coupling.\\n\\n### 产出文件\\nresults/subsumption_test/subsumption_results.json (15KB)\", \"parent\": \"spon_training\"}, \"eval_bce_v3_s42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T05:53:24.152Z\", \"updated_at\": \"2026-05-17T02:58:52.396Z\", \"hypothesis\": \"D031 eval: BCE iso-compute v3 评测——对比 KL predictor 在相同 sparsity (50%) 下的 PPL/TEAL，证明 KL 优势来自 loss 函数本身而非计算量差异 (Reviewer Concern #2 defense)\", \"metrics\": {\"dense_ppl\": 6.12, \"predictor_hard_mask_ppl\": 22.51, \"teal_sparse_ppl\": 27.97, \"model_level_sparsity\": 0.5, \"arc_challenge_acc\": 0.2048, \"arc_challenge_acc_norm\": 0.2398, \"arc_challenge_acc_norm_stderr\": 0.0125, \"winogrande_acc\": 0.5059, \"winogrande_acc_stderr\": 0.0141, \"mmlu_acc\": 0.3002, \"mmlu_acc_stderr\": 0.0038, \"gsm8k_exact_match\": 0.0485, \"gsm8k_exact_match_strict\": 0.0425, \"gsm8k_exact_match_stderr\": 0.0059}, \"conclusion\": \"success\", \"parent\": \"bce_isocompute_v3_s42\"}, \"lm_eval_teal_30pct\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T02:19:18.755Z\", \"updated_at\": \"2026-05-17T02:58:50.565Z\", \"hypothesis\": \"TEAL 30% training-free downstream eval — 与 KL 30% 对比，看 training-free baseline 在低 sparsity 下的 downstream 表现。配合 50% 数据点构建完整 sparsity-task tradeoff 曲线。\", \"metrics\": {\"arc_challenge\": {\"acc\": 0.3933, \"acc_norm\": 0.4155, \"acc_stderr\": 0.0143, \"acc_norm_stderr\": 0.0144}, \"winogrande\": {\"acc\": 0.6559, \"acc_stderr\": 0.0134}, \"mmlu\": {\"acc\": 0.3598, \"acc_stderr\": 0.004}, \"mmlu_stem\": {\"acc\": 0.313}, \"mmlu_humanities\": {\"acc\": 0.3305}, \"mmlu_social_sciences\": {\"acc\": 0.4108}, \"mmlu_other\": {\"acc\": 0.401}, \"gsm8k\": {\"exact_match_strict\": 0.0849, \"exact_match_flexible\": 0.0925, \"strict_stderr\": 0.0077, \"flexible_stderr\": 0.008}, \"actual_sparsity\": 0.3}, \"conclusion\": \"negative\", \"notes\": \"TEAL 30% vs KL 30% vs Dense (0-shot): ARC-c acc_norm: TEAL=0.4155 > KL=0.3737 (+4.2pp), Dense=0.5819. WinoGrande: TEAL=0.6559 < KL=0.6756 (-2.0pp), Dense=0.7814. MMLU: TEAL=0.3598 > KL=0.2874 (+7.2pp), Dense=0.6532. GSM8K strict: TEAL=0.0849 ≈ KL=0.0743 (+1.1pp), Dense=0.5004. TEAL 在知识密集型任务(ARC-c, MMLU)上显著优于 KL distill，但在推理任务(GSM8K)上两者都崩溃严重。整体仍远低于 Dense baseline，30% sparsity 对 downstream 损害巨大。\", \"parent\": \"lm_eval_teal_50pct\"}, \"lm_eval_kl_30pct_s42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T00:35:56.358Z\", \"updated_at\": \"2026-05-17T02:58:49.558Z\", \"hypothesis\": \"30% sparsity downstream eval (ARC-c, WinoGrande, MMLU, GSM8K) - 与 50% 对比看退化是否有梯度。决定论文是否能 claim \\\"30% 为推荐配置\\\"。\", \"notes\": \"第一次提交 (PID 186674) 因 HF httpx \\\"Cannot send a request, client closed\\\" 失败，无输出。需设 HF_HUB_OFFLINE=1 重跑。\", \"metrics\": {\"arc_challenge_acc\": 0.3575, \"arc_challenge_acc_norm\": 0.3737, \"winogrande_acc\": 0.6756, \"mmlu_acc\": 0.2874, \"gsm8k_exact_match_strict\": 0.0743, \"gsm8k_exact_match_flexible\": 0.0781, \"actual_sparsity\": 0.3, \"model\": \"llama-3.1-8b\", \"condition\": \"kl_distill_30pct_sparsity_s42\", \"mmlu_stem_acc\": 0.2499, \"mmlu_social_sciences_acc\": 0.2896, \"mmlu_humanities_acc\": 0.2786, \"mmlu_other_acc\": 0.3363}, \"conclusion\": \"negative\", \"parent\": \"lm_eval_kl_s42\"}, \"gsm8k_gen_compare\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T00:35:56.904Z\", \"updated_at\": \"2026-05-17T02:58:48.632Z\", \"hypothesis\": \"GSM8K 生成质量对比：dense vs KL sparse 50% greedy 生成 5-10 样本。判断退化是\\\"推理丧失（重复/无意义文本）\\\"还是\\\"仅数字算错\\\"。\", \"conclusion\": \"negative\", \"notes\": \"## GSM8K 生成质量对比：Dense vs KL Sparse 50% (10 samples)\\n\\n### 结论：推理能力根本性丧失（模式 A），非仅数字算错\\n\\n| 维度 | Dense | Sparse 50% |\\n|------|-------|------------|\\n| 推理连贯性 | 多步推理，逻辑清晰 | 1-3 句后进入无限重复循环 |\\n| 正确答案 | 多数正确 | 0/10 |\\n| 重复退化 | 无 | 10/10 全部出现 |\\n| 拼写质量 | 正常 | 退化（crabs→crbs, skein→skeen）|\\n\\n### 退化模式\\nSparse 模型能生成与问题相关的开头（如 \\\"First, we need to know...\\\"），但随即进入同一句话的无限重复（15+ 次）。Sample 7 中正确算出 9×2=18，但无法继续推理。\\n\\n### 对论文的意义\\n50% sparsity 摧毁了深层推理能力。PPL-downstream disconnect 的机制：PPL 衡量 next-token 平均质量，repetition loop 的每个重复 token 仍有较高概率（模型\\\"自信地\\\"重复），但推理链断裂。\", \"parent\": \"lm_eval_kl_s42\"}, \"d030_kl40_uniform\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T05:18:45.733Z\", \"updated_at\": \"2026-05-17T02:58:48.163Z\", \"hypothesis\": \"D033: KL 40% sparsity with UNIFORM per-layer allocation — 定位 allocation 修复的精确 threshold。30% uniform MMLU=40.61%（修复有效），50% uniform MMLU=27.77%（修复失效）。40% 是 threshold 精确定位的关键数据点。\", \"notes\": \"Director 确认方案 B：训练专用 40% predictor（非复用 30%/50% predictor eval）。流程：train.py --sparsity_target 0.4 (1000步, ~45min) → evaluate.py --sparsity_target 0.4 + lm_eval downstream with uniform allocation。排在 BCE v3 完成后用同一张卡（cuda:1）。与 30%/50% 保持一致，每个 sparsity level 用专用 predictor。\", \"metrics\": {\"wikitext2_ppl\": 8.3627, \"arc_challenge_acc_norm\": 0.4181, \"winogrande_acc\": 0.6717, \"mmlu_acc\": 0.3068, \"gsm8k_exact_match\": 0.0394, \"actual_sparsity\": 0.398}, \"conclusion\": \"success\", \"parent\": \"d030_kl30_uniform\"}, \"d030_kl50_uniform\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T04:30:55.969Z\", \"updated_at\": \"2026-05-17T02:58:47.243Z\", \"hypothesis\": \"D030: KL 50% sparsity with UNIFORM per-layer allocation — 30% uniform 显示 MMLU +12pp 但 GSM8K 无恢复。50% 测试更高 sparsity 下 uniform 是否仍能部分修复知识类任务。\", \"conclusion\": \"success\", \"metrics\": {\"wikitext2_ppl\": 11.96, \"arc_challenge_acc_norm\": 0.3276, \"winogrande_acc\": 0.629, \"mmlu_acc\": 0.2777, \"gsm8k_exact_match\": 0.0212, \"actual_sparsity\": 0.5, \"allocation\": \"uniform\", \"per_layer_sparsity\": \"uniform 0.500 across all 32 layers\", \"mmlu_change_vs_global\": \"+1.86pp (0.2591 → 0.2777, not significant)\", \"gsm8k_change_vs_global\": \"+0.91pp (0.0121 → 0.0212, not significant)\", \"conclusion_note\": \"50% uniform 未能修复 MMLU/GSM8K collapse. Uniform allocation 的修复效应在 50% sparsity 下消失。\"}, \"notes\": \"## D030 50% Uniform 结果\\n\\n50% uniform per-layer allocation 未能修复 downstream collapse。MMLU 0.2777（接近随机 0.25），GSM8K 0.0212，与 global top-k 的 0.2591/0.0121 几乎无差异。\\n\\n### 与 30% Uniform 对比\\n30% uniform 将 MMLU 从 0.2874 拉到 0.4061（+12pp），但 50% uniform 对 MMLU 仅 +1.86pp。说明 uniform allocation 的修复效应在 50% 下完全消失。\\n\\n### 结论\\n50% 是 downstream capability 的断崖点。无论 per-layer allocation 策略如何，50% sparsity 对 SwiGLU FFN 的知识检索和推理能力有根本性破坏。支撑 Narrative A（50% collapse is universal）。\\n\\n### 对论文的意义\\n- Claim 3 需要调整：30% 可以作为\\\"推荐配置\\\"叙述（PPL 8.82, MMLU 0.4061），但 50% 只能用于 PPL 场景\\n- 论文应报告 30% uniform 为 downstream-safe operating point\", \"parent\": \"d030_kl30_uniform\"}, \"bce_isocompute_v3_s42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T03:56:03.520Z\", \"updated_at\": \"2026-05-17T02:58:46.255Z\", \"hypothesis\": \"D031: BCE iso-compute 重跑（v1/v2 两次被 tmux 杀死）。2700 步匹配 KL 1000 步总 FLOPs (ratio≈2.71x)，50% sparsity。Reviewer Concern #2 defense: 验证 KL 优势来自 loss 函数本身而非计算量差异。\", \"conclusion\": \"success\", \"metrics\": {\"steps\": 2700, \"loss\": 0.6382, \"bce_loss\": 0.6371, \"reg_loss\": 0.001, \"sparsity\": 0.51, \"training_time_seconds\": 2828, \"note\": \"BCE saturation confirmed: step 500→2700 only 0.006 improvement\"}, \"parent\": \"bce_isocompute_v2_s42\"}, \"spon_2048_s42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T18:40:29.059Z\", \"updated_at\": \"2026-05-17T02:58:45.331Z\", \"conclusion\": \"negative\", \"metrics\": {\"true_dense_ppl\": 6.1173, \"predictor_hard_mask_ppl\": 9.2165, \"spon_sparse_ppl\": 8.991, \"spon_recovery_pct\": 7.3, \"ppl_improvement_from_spon\": 0.2255, \"mean_bias_norm\": 0.05312, \"max_bias_norm\": 0.065918, \"model_level_sparsity\": 0.498, \"eval_seq_len\": 2048, \"training_seq_len\": 2048, \"eval_samples\": 141, \"trainable_params\": 458752, \"trainable_pct\": 0.0057, \"training_steps\": 1000, \"final_loss\": 0.377, \"dense_with_spon_ppl\": 6.1823, \"dense_ppl_degradation\": 0.0651, \"teal_sparse_no_spon_ppl\": 12.0776, \"teal_sparse_with_spon_ppl\": 11.7907, \"spon_recovery_teal_pct\": 4.8, \"teal_sparsity\": 0.4979}, \"notes\": \"## SPON seq_len=2048 重训，消除 train/eval length mismatch confound\\n\\n### 训练概要\\n1000 steps 正常完成。Loss 从 0.41 下降到 0.38 区间后波动。Bias norm 从 0→0.053 在 step 700 饱和（vs seq_len=128 版的 0.041）。Seq_len=2048 训练使得 bias 学到更多信息（norm 更高 30%），但改善仍有限。\\n\\n### WikiText-2 评估 (seq_len=2048, 141 sequences)\\n- True Dense PPL: 6.12\\n- Predictor Hard Mask PPL (no SPON): 9.22 (+50.6%)\\n- SPON Sparse PPL: 8.99 (+46.9%)\\n- **SPON recovery: 7.3%** (0.23 PPL improvement)\\n\\n### 与 spon_training (seq_len=128) 对比\\n| 指标 | seq_len=128 | seq_len=2048 | 变化 |\\n|------|-------------|--------------|------|\\n| SPON recovery | 3.8% | 7.3% | +3.5pp |\\n| PPL improvement | 0.12 | 0.23 | +0.11 |\\n| mean_bias_norm | 0.041 | 0.053 | +30% |\\n| spon_sparse_ppl | 9.10 | 8.99 | -0.11 |\\n\\n### 结论: **Negative** (recovery 7.3% < 10% 阈值)\\n消除 seq_len mismatch 后 SPON recovery 从 3.8% 提升到 7.3%，说明 mismatch 确实是部分原因，但即使在匹配条件下 static bias 仍只能恢复不到 10% 的稀疏化误差。确认 D009 \\\"KL subsumes SPON\\\" reframe：KL predictor 的 per-token mask 已经很好地适应了重要 neuron，残余误差不是简单的 additive bias 能补偿的。\", \"parent\": \"spon_training\"}, \"kl_sparsity30_s42_v3\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T21:09:36.571Z\", \"updated_at\": \"2026-05-17T02:58:44.374Z\", \"hypothesis\": \"KL distillation @ 30% sparsity, lambda_max=5000 (v2 lambda_max=1000 导致 sparsity 仅收敛到 0.281). Plan_008 sparsity sweep 30% 数据点重跑。\", \"metrics\": {\"loss\": 0.165, \"kl_normalized\": 0.165, \"kl_raw\": 0.165, \"sparsity\": 0.285, \"lambda_sparse\": 5000, \"tau\": 0.1, \"constraint_loss\": 0, \"steps\": 1000, \"true_dense_ppl\": 6.12, \"predictor_hard_mask_ppl\": 7.3, \"teal_sparse_ppl\": 8.98, \"teal_sparse_ppl_note\": \"已通过 eval_kl30_teal_30pct 独立验证 (sparsity_target=0.3, D034)\", \"model_level_sparsity\": 0.3, \"eval_dataset\": \"wikitext-2\", \"eval_seq_len\": 2048}, \"conclusion\": \"success\", \"notes\": \"D016 决策：sparsity=0.285（target=0.30），lambda_max=5000 仍无法推到 target。Director 接受为实际数据点——predictor 在 ~28.5% 有自然下限，不再重跑。论文报 achieved sparsity 28.5%（不写 target 30%）。\\n\\n## PPL 评估（已修正，D034）\\n- predictor_hard_mask_ppl=7.30: per-token adaptive mask 评估值\\n- teal_sparse_ppl=8.98: 已通过 eval_kl30_teal_30pct 独立验证（sparsity_target=0.3）\\n- D032 曾误判原值 8.98 为\\\"Mistral 数据误拷\\\"，实际原值正确。13.63 是 evaluate.py 默认 sparsity_target=0.5 的结果（非 30% PPL）\\n\\nPer-layer sparsity: 早期层 0.13-0.23, 中间层 0.30-0.34, 后层 0.50-0.70。\", \"parent\": \"kl_sparsity30_s42_v2\"}, \"steps_curve_v2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T23:53:44.668Z\", \"updated_at\": \"2026-05-16T23:57:45.934Z\", \"metrics\": {\"step200_ppl\": 15.158, \"step400_ppl\": 12.538, \"step600_ppl\": 12.046, \"step800_ppl\": 11.907, \"step1000_ppl\": 11.906, \"convergence_step\": 800, \"ppl_800_vs_1000_delta\": 0.001}, \"conclusion\": \"success\", \"hypothesis\": \"KL predictor training converges within 600-800 steps; 1000 steps is sufficient and near-saturated performance\"}, \"tau_schedule_ablation\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T23:53:42.391Z\", \"updated_at\": \"2026-05-16T23:57:45.222Z\", \"metrics\": {\"tau_linear_baseline_ppl\": 11.963, \"tau_fixed05_ppl\": 11.861, \"tau_fixed01_ppl\": 12.072, \"tau_fixed05_loss\": 0.248, \"tau_fixed01_loss\": 0.43, \"best_tau\": \"fixed_0.5\", \"ppl_range\": 0.211}, \"conclusion\": \"success\", \"hypothesis\": \"Temperature schedule has minor impact on final PPL - method is robust to tau choice within reasonable range (fixed 0.5 vs fixed 0.1 vs linear annealing)\"}, \"steps_curve_s42_v3\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"created_at\": \"2026-05-16T22:15:19.436Z\", \"updated_at\": \"2026-05-16T22:15:19.436Z\"}, \"steps_curve_s42_v2\": {\"status\": \"DONE\", \"conclusion\": \"killed\", \"created_at\": \"2026-05-16T22:14:37.684Z\", \"updated_at\": \"2026-05-16T22:14:37.684Z\"}, \"steps_curve_s42\": {\"status\": \"DONE\", \"conclusion\": \"killed\", \"created_at\": \"2026-05-16T22:13:36.875Z\", \"updated_at\": \"2026-05-16T22:13:36.875Z\"}, \"db_sensitivity_sweep\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T20:02:33.553Z\", \"updated_at\": \"2026-05-16T22:04:02.778Z\", \"metrics\": {\"db64_per_token_ppl\": 10.158, \"db64_teal_global_ppl\": 12.076, \"db64_sparsity\": 0.5, \"db64_loss\": 0.361, \"db128_teal_global_ppl\": 11.963, \"db128_per_token_ppl\": 9.218, \"db256_per_token_ppl\": 8.586, \"db256_teal_global_ppl\": 12.105, \"db256_sparsity\": 0.5, \"db256_loss\": 0.27, \"db512_per_token_ppl\": 7.933, \"db512_teal_global_ppl\": 12.315, \"db512_sparsity\": 0.5, \"db512_loss\": 0.224, \"best_teal_global_db\": 128, \"best_teal_global_ppl\": 11.963}, \"conclusion\": \"success\", \"hypothesis\": \"Predictor bottleneck dimension d_b has low sensitivity to teal_global PPL across 4x range (64-512), justifying d_b=128 as default without hyperparameter tuning\"}, \"longbench_kl30_uniform_v2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T13:22:55.841Z\", \"updated_at\": \"2026-05-16T17:00:25.982Z\", \"conclusion\": \"failed\", \"notes\": \"OOM: 两个进程争抢同一 GPU + 无 flash-attn 导致内存溢出\"}, \"longbench_dense_v2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T13:22:57.327Z\", \"updated_at\": \"2026-05-16T17:00:25.298Z\", \"conclusion\": \"failed\", \"notes\": \"OOM: 两个进程争抢同一 GPU + 无 flash-attn 导致内存溢出\"}, \"longbench_kl30_uniform_v3\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T13:32:56.949Z\", \"updated_at\": \"2026-05-16T17:00:24.335Z\", \"conclusion\": \"failed\", \"notes\": \"OOM: 单卡无法处理 32k token LongBench 文档，需要 2 卡 tensor parallel\"}, \"longbench_dense_v3\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T13:32:58.232Z\", \"updated_at\": \"2026-05-16T17:00:23.387Z\", \"conclusion\": \"failed\", \"notes\": \"OOM: 单卡无法处理 32k token LongBench 文档，需要 2 卡 tensor parallel\"}, \"longbench_dense_v5\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-16T13:45:44.157Z\", \"updated_at\": \"2026-05-16T14:45:11.139Z\", \"conclusion\": \"killed\", \"notes\": \"LongBench 正式放弃（Director 决策）。5 次 OOM 失败，物理内存不可解。论文不纳入 LongBench。\"}, \"longbench_dense_v4\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T13:40:39.061Z\", \"updated_at\": \"2026-05-16T13:44:29.665Z\", \"conclusion\": \"failed\", \"notes\": \"OOM: CUDA 内存碎片化（reserved 17.98GB > requested 13.98GB），非绝对容量不足。需加 PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True\"}, \"longbench_dense\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T12:57:41.121Z\", \"updated_at\": \"2026-05-16T13:21:12.937Z\", \"conclusion\": \"failed\", \"notes\": \"HF_HUB_OFFLINE=1 + 数据未缓存导致下载失败\"}, \"longbench_kl30_uniform\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T12:57:39.563Z\", \"updated_at\": \"2026-05-16T13:21:12.363Z\", \"conclusion\": \"failed\", \"notes\": \"HF_HUB_OFFLINE=1 + 数据未缓存导致下载失败\"}, \"bench_mistral_kl50_s42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T04:22:12.157Z\", \"updated_at\": \"2026-05-16T05:23:45.617Z\", \"hypothesis\": \"D029: Mistral KL 50% sparsity — benchmark_eval.py 统一 few-shot 评测 (ARC-c=25, WG=5, MMLU=5, GSM8K=8)。与 lm_eval_mistral_kl_50pct (0-shot) 对比，确保评测一致性。\", \"conclusion\": \"killed\", \"notes\": \"D034 修正：PID 207962 实际仍在 cuda:0 运行。之前 registry 误标为 killed（Director 优先级调整时标记，但进程未被实际终止）。等完成后更新实际结果。\"}, \"lm_eval_teal_50pct\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T00:35:57.527Z\", \"updated_at\": \"2026-05-16T04:52:09.866Z\", \"hypothesis\": \"TEAL 50% training-free sparse downstream eval - 判断 downstream 崩溃是否为所有 50% sparsity 方法的固有限制，而非 KL predictor 特有问题。\", \"notes\": \"TEAL 50% downstream 结果确认 collapse 是 universal：\\n\\n| Task | TEAL 50% | KL 50% | Dense | TEAL drop | KL drop |\\n|------|----------|--------|-------|-----------|---------|\\n| arc_challenge (acc_norm) | 0.2910 | 0.3771 | 0.5819 | -50.0% | -35.2% |\\n| winogrande (acc) | 0.5556 | 0.6156 | 0.7814 | -28.9% | -21.2% |\\n| mmlu (acc) | 0.2856 | 0.2591 | 0.6532 | -56.3% | -60.3% |\\n| gsm8k (flexible-extract) | 0.0190 | 0.0121 | 0.5004 | -96.2% | -97.6% |\\n\\n关键发现：\\n1. TEAL 和 KL 在 MMLU/GSM8K 上均出现灾难性崩溃（接近随机水平），证明 50% sparsity downstream collapse 不是 KL predictor 特有问题\\n2. TEAL 在 ARC/WinoGrande 上甚至比 KL 更差（TEAL drop -50%/-29% vs KL drop -35%/-21%），说明 training-free 方法在简单 task 上也不如 learned predictor\\n3. MMLU/GSM8K 两者均近随机（MMLU ~0.25-0.29 = 4-choice random level），collapse 程度相当\\n4. 结论：50% unstructured sparsity 对 SwiGLU FFN 的 downstream capability 有根本性破坏，与 sparsity 选择方法无关\", \"metrics\": {\"method\": \"vanilla_teal\", \"sparsity\": 0.5, \"actual_sparsity\": 0.5, \"arc_challenge_acc_norm\": 0.291, \"winogrande_acc\": 0.5556, \"mmlu_acc\": 0.2856, \"gsm8k_exact_match_flexible\": 0.019, \"gsm8k_exact_match_strict\": 0.0114, \"arc_challenge_drop_vs_dense\": -0.5, \"winogrande_drop_vs_dense\": -0.289, \"mmlu_drop_vs_dense\": -0.563, \"gsm8k_drop_vs_dense\": -0.962, \"model\": \"Llama-3.1-8B\", \"condition\": \"TEAL 50% training-free sparsity\"}, \"conclusion\": \"success\"}, \"d030_kl30_uniform\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T03:53:01.230Z\", \"updated_at\": \"2026-05-16T04:34:08.796Z\", \"hypothesis\": \"D030: KL 30% sparsity with UNIFORM per-layer allocation — 验证 global top-k 的 per-layer 不均匀是否是 downstream 崩溃的根因。对比 global top-k 的 MMLU 28.74%/GSM8K 7.43%。\", \"metrics\": {\"wikitext2_ppl\": 8.8157, \"arc_challenge_acc_norm\": 0.4078, \"winogrande_acc\": 0.6859, \"mmlu_acc\": 0.4061, \"gsm8k_exact_match\": 0.0735, \"actual_sparsity\": 0.3, \"allocation\": \"uniform\", \"per_layer_sparsity\": \"uniform 0.301 across all 32 layers\", \"mmlu_improvement_vs_global\": \"+11.87pp (0.2874 → 0.4061)\", \"gsm8k_change_vs_global\": \"no change (0.0743 → 0.0735, within noise)\"}, \"conclusion\": \"success\"}, \"mistral_kl_s42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T22:12:33.050Z\", \"updated_at\": \"2026-05-16T04:27:36.290Z\", \"hypothesis\": \"Mistral-7B-v0.3 跨架构验证：KL normalized loss @ 50% sparsity。验证 KL distillation 方法在非 Llama 架构上也有效。Plan_009 第一个实验。\", \"metrics\": {\"train_final_loss\": 0.2188, \"train_final_kl_raw\": 0.2188, \"train_final_kl_norm\": 0.2188, \"train_final_constraint\": 0, \"train_final_sparsity\": 0.48, \"train_final_lambda\": 1000, \"train_final_tau\": 0.1, \"train_steps_completed\": 1000, \"true_dense_ppl\": 5.52, \"predictor_hard_mask_ppl\": 7.3, \"teal_sparse_ppl\": 8.98, \"model_level_sparsity\": 0.5, \"eval_dataset\": \"wikitext-2\", \"eval_seq_len\": 2048, \"calibration_samples\": 32, \"eval_samples\": 159}, \"notes\": \"teal_sparse_ppl=8.98 已通过原始日志验证 (eval_mistral_kl_s42.log)，模型=mistral-7b, predictor=predictor_kl_normalized.pt, sparsity=0.5，三项指标均与日志一致 [2026-05-16 D032交叉验证]\", \"conclusion\": \"success\"}, \"kl_lagrangian_v2\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-15T13:34:10.257Z\", \"updated_at\": \"2026-05-16T03:08:33.111Z\", \"notes\": \"取消: Director 改为方案 C（KL 归一化 + Lagrangian），v2 仅调参数不够。新实验 kl_normalized_quicktest 替代。\", \"conclusion\": \"killed\"}, \"kl_norm_v3_quicktest\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-15T15:16:56.462Z\", \"updated_at\": \"2026-05-16T03:08:32.570Z\", \"conclusion\": \"killed\", \"metrics\": {\"step1_kl_raw\": 1.1797, \"step1_kl_norm\": 1.1797, \"step1_sparsity\": 0.406, \"step1_lambda\": 2, \"step50_kl_raw\": 0.7344, \"step50_kl_norm\": 0.7344, \"step50_sparsity\": 0.514, \"step50_lambda\": 1.95, \"step100_kl_raw\": 0.625, \"step100_kl_norm\": 0.625, \"step100_sparsity\": 0.496, \"step100_lambda\": 1000, \"step150_kl_raw\": 0.5703, \"step150_kl_norm\": 0.5703, \"step150_sparsity\": 0.48, \"step150_lambda\": 1000, \"step200_kl_raw\": 0.6836, \"step200_kl_norm\": 0.6836, \"step200_sparsity\": 0.477, \"step200_lambda\": 1000, \"step200_constraint\": 0.01178, \"kl_trend\": \"decreasing (1.18→0.57 min, uptick to 0.68 at end)\", \"sparsity_range\": \"0.477-0.514 after step 50\", \"checkpoint_path\": \"/root/distill_sparse_swiglu/checkpoints/kl_norm_v3_quicktest/predictor_kl_normalized.pt\"}, \"notes\": \"PASS: Bug 修复后 kl_norm = kl_raw (仅保留 losses.py 的 ÷seq_len)。KL 从 1.18 下降到 0.57(step150)，sparsity 收敛到 0.477-0.514。Lambda 到 1000 cap 是因为 sparsity 在 margin 边界(0.477-0.484 < target-0.02=0.48)。注意: step 200 KL 略回升到 0.68(lr 接近 0 + tau=0.1 硬化)。\"}, \"mvp_kl_norm_s456\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-15T14:30:12.769Z\", \"updated_at\": \"2026-05-16T03:08:31.529Z\", \"conclusion\": \"killed\"}, \"spon_kl_s42\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-15T17:27:18.621Z\", \"updated_at\": \"2026-05-16T03:08:30.602Z\", \"conclusion\": \"killed\"}, \"diag_30pct_downstream\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-16T00:34:04.456Z\", \"updated_at\": \"2026-05-16T03:08:29.808Z\", \"conclusion\": \"killed\"}, \"diag_gsm8k_gencomp\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-16T00:34:07.736Z\", \"updated_at\": \"2026-05-16T03:08:29.420Z\", \"notes\": \"10 GSM8K samples compared (dense vs KL sparse 50% TEAL). Sparse model suffers FUNDAMENTAL reasoning collapse: (1) 10/10 samples degenerate into repetitive loops within 1-3 sentences; (2) no sample produces correct final answer or completes multi-step reasoning; (3) sparse model can generate topically relevant opening text but immediately enters infinite repetition (e.g. \\\"We can then use the formula...\\\" repeated 15+ times); (4) occasional partial correctness in first sentence (Sample 7: correctly computes 9*2=18 but never adds +3); (5) spelling degradation observed (crabs→crbs, skein→skeen). Dense model generates coherent step-by-step reasoning and often reaches correct answers. Conclusion: GSM8K score of 0.0121 is NOT caused by answer extraction/format mismatch — it reflects genuine loss of reasoning and generation ability under 50% TEAL sparsity with KL-trained predictor.\", \"conclusion\": \"killed\"}, \"diag_teal_downstream\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-16T00:34:11.737Z\", \"updated_at\": \"2026-05-16T03:08:28.224Z\", \"conclusion\": \"killed\"}, \"bce_isocompute_s42_v2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T19:47:02.076Z\", \"updated_at\": \"2026-05-16T02:24:56.731Z\", \"hypothesis\": \"BCE 在等量 FLOPs (2700 步 vs KL 1000 步, ratio=2.71x) 下是否能缩小与 KL 的 PPL 差距？如果不能，说明 KL 的优势来自 loss 函数本身而非计算量（Reviewer Concern #2 defense）。[Retry of bce_isocompute_s42 which crashed at step 500]\", \"notes\": \"PID 123984 已死亡（v2 重试也失败）。tmux session 再次被外部终止，与 v1 相同模式。BCE iso-compute 实验需要在清空 GPU 后单独重跑。\", \"conclusion\": \"killed\"}, \"eval_spon_supp_retry\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T19:44:22.659Z\", \"updated_at\": \"2026-05-16T02:24:55.659Z\", \"conclusion\": \"failed\", \"notes\": \"PID 123231 已死亡。SPON 补充 eval，tmux session 消失，被后续实验覆盖。\"}, \"lm_eval_dense_test\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T22:30:54.405Z\", \"updated_at\": \"2026-05-16T02:24:54.247Z\", \"conclusion\": \"failed\", \"notes\": \"PID 153249 已死亡。早期探索性 eval，tmux session 消失，被后续实验覆盖。\"}, \"lm_eval_mistral_downstream\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T23:34:22.527Z\", \"updated_at\": \"2026-05-16T02:24:53.274Z\", \"conclusion\": \"failed\", \"notes\": \"PID 174840 已死亡（进程不存在）。被后续实验 lm_eval_teal_50pct 占用 cuda:1 时挤掉，tmux session 消失。\"}, \"mvp_kl_s123\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T11:51:00.876Z\", \"updated_at\": \"2026-05-16T02:23:07.388Z\", \"notes\": \"Killed: 使用旧 KL 配置（无归一化），已被 mvp_kl_norm_s123 替代。参见 kl_normalized_quicktest 验证 seq_len-only 归一化有效。\", \"conclusion\": \"killed\"}, \"mvp_kl_s456\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T11:51:02.768Z\", \"updated_at\": \"2026-05-16T02:23:06.464Z\", \"conclusion\": \"killed\", \"notes\": \"Killed: 使用旧 KL 配置（无归一化），已被 mvp_kl_norm_s456 替代。参见 kl_normalized_quicktest 验证 seq_len-only 归一化有效。\"}, \"bce_isocompute_v2_s42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T20:01:43.104Z\", \"updated_at\": \"2026-05-15T21:11:42.245Z\", \"hypothesis\": \"BCE 在 iso-compute (1000 steps) + iso-sparsity (STE reg_weight=2.0 使 sparsity 收敛到 ~0.50) 下是否能缩小与 KL 的 PPL 差距？消除 compute 和 sparsity 两个 confound。\", \"notes\": \"## Eval Results (2026-05-16)\\n- true_dense_ppl: 6.12\\n- predictor_hard_mask_ppl: 26.76\\n- teal_sparse_ppl: 54.84\\n- sparsity_target: 0.50 (converged correctly, STE fix worked)\\n\\n## Training Summary\\n- 1000 steps, 1048s (1.05s/step), EXIT_CODE=0\\n- BCE loss: 0.6714 → 0.6586 (only 5% better than random 0.693)\\n- Reg loss: 0.0171 → 0.0051 (sparsity converged to 0.50)\\n- reg_weight=2.0, Gumbel-sigmoid STE\\n\\n## Comparison with KL Baseline\\n- KL normalized (50% sparsity, 4-seed mean): teal_sparse_ppl = 12.00 ± 0.07\\n- BCE v2: teal_sparse_ppl = 54.84 — 4.6x worse than KL\\n\\n## Conclusion\\nBCE + STE dramatically underperforms KL at 50% sparsity under iso-compute (1000 steps). BCE treats each neuron as an independent binary classification, losing inter-neuron coordination and output distribution signal. The predictor barely learned meaningful patterns (BCE only 5% better than random). KL's direct output-distribution matching provides much stronger learning signal. BCE is not a viable alternative loss for sparsity predictor training.\", \"conclusion\": \"success\", \"metrics\": {\"final_loss\": 0.6637, \"final_bce_loss\": 0.6586, \"final_reg_loss\": 0.0051, \"final_sparsity\": 0.502, \"training_steps\": 1000, \"training_time_sec\": 1047.8, \"reg_weight\": 2, \"true_dense_ppl\": 6.12, \"predictor_hard_mask_ppl\": 26.76, \"teal_sparse_ppl\": 54.84, \"eval_seq_len\": 2048, \"eval_dataset\": \"wikitext-2\"}}, \"kl_sparsity70_s42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T20:24:08.219Z\", \"updated_at\": \"2026-05-15T20:35:03.728Z\", \"conclusion\": \"killed\", \"notes\": \"cuda:1 系统性问题：进程启动后快速死亡，零日志/零checkpoint/零stderr。连续三个进程在 cuda:1 上死亡(plan_005完成后)。需硬件诊断后才能重跑。conclusion=killed(系统kill，非OOM)。\"}, \"kl_sparsity30_s42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T20:24:03.207Z\", \"updated_at\": \"2026-05-15T20:35:02.572Z\", \"conclusion\": \"killed\", \"notes\": \"cuda:1 系统性问题：进程启动后快速死亡，零日志/零checkpoint/零stderr。与 kl_sparsity70_s42 同一模式——cuda:1 连续三个进程(plan_005后)均快速死亡。需硬件诊断后才能重跑。conclusion=killed(系统kill，非OOM)。v2版本(PID 132397)也同样死亡。\"}, \"ste_baseline_s42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T18:35:42.177Z\", \"updated_at\": \"2026-05-15T20:03:55.571Z\", \"notes\": \"STE baseline 代码实现完成 (Worker worker_code_ste_baseline_20260515T183635)。修改：src/predictor.py 新增 STEMask 类（hard threshold + STE gradient），src/train.py 新增 --relaxation ste/gumbel 参数。\\n\\n## WikiText-2 评估 (seq_len=2048, 141 sequences, calibration=32)\\n- True Dense PPL: 6.12\\n- Predictor Hard Mask PPL: 8.18 (per-token sparsity=0.470, 低于 target 0.5)\\n- TEAL Sparse PPL: **15.77** (global 50% sparsity)\\n\\n## vs Gumbel-sigmoid 对比 (TEAL Sparse PPL, 公平 50% 全局稀疏度)\\n| 指标 | STE | Gumbel 4-seed mean | 差异 |\\n|------|-----|---------------------|------|\\n| TEAL Sparse PPL | 15.77 | 12.00 ± 0.07 | +31.4% |\\n| Hard Mask PPL | 8.18 | 9.19 ± 0.04 | -11.0%* |\\n| Per-token sparsity | 0.470 | 0.498 | -2.8pp |\\n\\n*Hard mask PPL 不可直接比较：STE per-token sparsity 仅 0.470（低于 Gumbel 0.498），较低稀疏度自然带来较低 PPL。\\n\\n## Lambda 震荡统计\\nSTE hard threshold 导致 Lagrangian multiplier 剧烈震荡：\\n- Steps 70-130 (关键不稳定区间): mean=66.40, std=94.87, range=[0.01, 1000]\\n- 前 500 步 (51 pts): mean=688.07, std=440.57, min=0.01, max=1000\\n- 后 500 步 (51 pts): mean=965.69, std=141.59, min=250, max=1000\\n- 全程: mean=826.88, std=354.23\\n\\nLambda 在前 100 步内从 0.01 飙升到 1000 再回落到 3.91，反复震荡。对比 Gumbel 训练中 lambda 平稳收敛到 cap，STE 的 constraint 满足极不稳定。\\n\\n## 根因分析\\nSTE hard threshold (>0.5=keep, ≤0.5=prune) 导致：\\n1. 离散 sparsity 值（sigmoid 微小变化可翻转大量 neuron）→ constraint 满足不稳定\\n2. Lambda 被迫在 0.01-1000 间震荡以追踪快速变化的 constraint violation\\n3. 最终收敛到 lambda=1000 (cap) 但 per-token sparsity 仅 0.470（未达 target 0.5）\\n4. 逐层稀疏度极端两极化（Layer 0-17: 5-56%, Layer 18-31: 56-90%），导致 TEAL 全局分配效果差\\n\\n## Conclusion: SUCCESS (验证 Gumbel 必要性)\\nTEAL sparse PPL 15.77 显著差于 Gumbel 12.00 (+31.4%)，确认 Gumbel soft mask 的平滑梯度对 KL distillation 训练至关重要。可直接用于 Reviewer Concern #3 defense。\", \"hypothesis\": \"STE relaxation (hard threshold + straight-through gradient) 是否能匹配 Gumbel-sigmoid 的 KL distillation 效果？如果差距大，说明 Gumbel soft mask 对 KL 训练至关重要（Reviewer Concern #3 defense）。\", \"metrics\": {\"true_dense_ppl\": 6.12, \"predictor_hard_mask_ppl\": 8.18, \"teal_sparse_ppl\": 15.77, \"model_level_sparsity\": 0.47, \"ppl_increase_vs_true_dense_pct\": 157.7, \"eval_seq_len\": 2048, \"calibration_samples\": 32, \"eval_dataset\": \"wikitext-2\", \"per_token_sparsity\": 0.47, \"lambda_stats\": {\"steps_70_130_mean\": 66.4, \"steps_70_130_std\": 94.87, \"first_500_mean\": 688.07, \"first_500_std\": 440.57, \"last_500_mean\": 965.69, \"last_500_std\": 141.59, \"overall_mean\": 826.88, \"overall_std\": 354.23}}, \"conclusion\": \"success\"}, \"spon_supp_eval_retry\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T19:58:35.272Z\", \"updated_at\": \"2026-05-15T20:01:49.058Z\", \"conclusion\": \"failed\"}, \"bce_isocompute_s42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T19:29:17.153Z\", \"updated_at\": \"2026-05-15T19:40:29.742Z\", \"hypothesis\": \"BCE 在等量 FLOPs (2700 步 vs KL 1000 步, ratio=2.71x) 下是否能缩小与 KL 的 PPL 差距？如果不能，说明 KL 的优势来自 loss 函数本身而非计算量（Reviewer Concern #2 defense）。\", \"notes\": \"Iso-compute BCE: 2700 步匹配 KL 1000 步的总 FLOPs (ratio=2.71x, 实测 profile_flops.py: KL 0.549s/step vs BCE 0.202s/step @BS=1,SL=512)。\\\\nReviewer Concern #2 defense: 验证 KL 优势来自 loss 函数本身而非计算量差异。\\\\n\\\\n## FLOPs 计算依据\\\\n- KL 每步: dense fwd (no grad) + sparse fwd (grad) + backward w/ gradient checkpointing = 0.549s\\\\n- BCE 每步: dense fwd (no grad) + predictor fwd/bwd (~0.9% model FLOPs) = 0.202s\\\\n- Ratio: 2.71x → 1000 KL steps ≈ 2700 BCE steps\\\\n\\\\n## 失败记录 [2026-05-15]\\\\n进程在 Step 500/2700 后静默退出（PID 120879）。日志仅 17 行，最后记录 Step 500: loss=0.6461, bce=0.6406, reg=0.0055, sparsity=0.555。无 error traceback，无 checkpoint 产出。wandb offline 数据截至 03:38（启动后仅 9 分钟）。疑似 OOM 或被外部 kill。\", \"conclusion\": \"failed\"}, \"ste_kl_s42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T18:48:15.860Z\", \"updated_at\": \"2026-05-15T18:56:12.716Z\", \"conclusion\": \"killed\", \"notes\": \"Director 确认 cuda:1 空转超过 30 分钟，ste_kl_s42 进程 PID 112197 已死。释放 cuda:1 给 ste_baseline_s42 重跑。\"}, \"spon_training_seq2048\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T18:35:39.812Z\", \"updated_at\": \"2026-05-15T18:54:31.996Z\", \"conclusion\": \"killed\"}, \"mvp_kl_norm_s123\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T14:30:10.779Z\", \"updated_at\": \"2026-05-15T14:56:37.217Z\", \"conclusion\": \"failed\"}, \"mvp_kl_norm_s42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T14:23:52.490Z\", \"updated_at\": \"2026-05-15T14:56:36.798Z\", \"notes\": \"Director 指令的 mvp_kl_s42（新配方）。Normalized KL (÷seq_len) + Lagrangian, 1000 steps, seed=42。已于 session 恢复时提交 (PID=67789)。训练完后需跑 WikiText-2 + C4 eval。\", \"conclusion\": \"failed\"}, \"kl_normalized_quicktest\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T13:36:21.345Z\", \"updated_at\": \"2026-05-15T14:36:32.465Z\", \"conclusion\": \"failed\", \"metrics\": {\"step1_kl\": 1.18, \"step200_kl\": 0.641, \"step200_sparsity\": 0.504, \"final_lambda\": 8, \"sparsity_converged_step\": 80, \"sparsity_trajectory\": [0.406, 0.398, 0.398, 0.457, 0.52, 0.506, 0.504, 0.504], \"lambda_trajectory\": [1, 2, 4, 8, 8, 8, 8, 8]}, \"notes\": \"FAILED: 代码 bug — train.py:228 有 kl_norm = kl_raw / vocab_size (÷128256), 同时 KLDistillLoss 已做 kl / seq_len。总归一化 = ÷(seq_len × vocab_size), kl_norm≈0.00007。梯度信号~10^-5, predictor 只学了维持 50% 总量。kl_raw 实际从 1.18 上升到 9.94（非下降）。之前的 SUCCESS 结论是错误的。\"}}, \"count\": 378, \"total\": 378, \"baseline\": \"bench_dense\"}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.8762}}"
    }
  },
  "sourceToolAssistantUUID": "9c19b765-389a-4a28-b04d-9faf045e0ad1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/agent_66b8aa9d",
  "sessionId": "062027a5-1c13-4530-a568-995829f28b19",
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
  "lastPrompt": "[CRON] 实验进程异常退出（失败），需要你诊断原因。 详情: Process exited without valid W&B metrics  - exp_id: kl50_global_s123_downstream_v2 - project: distill_sparse_swiglu - server: westd-34887 - log_path: ~/runs/distill_sp…",
  "leafUuid": "f5ab47e2-fb5c-4046-bd3e-6812defdff50",
  "sessionId": "062027a5-1c13-4530-a568-995829f28b19"
}
```

---

### Runtime record

_source line 18_

```json
{
  "type": "ai-title",
  "aiTitle": "Diagnose W&B metrics missing error in experiment",
  "sessionId": "062027a5-1c13-4530-a568-995829f28b19"
}
```

---

### Tool result

_source line 19 · 2026-05-22T18:49:25.897Z_

<details><summary>↩ Tool result · `toolu_01Bx1GLUtX68z5x5RaV9HmeY`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"reconciled\": 0, \"results\": []}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3863c078-9182-4bde-aca1-9efbf20a6b85",
  "isSidechain": false,
  "promptId": "e0126d52-e1d3-4c8c-a4f2-76af8e88bda0",
  "type": "user",
  "uuid": "fa229629-7d5f-44f0-a04a-020e4caa739f",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"reconciled\\\": 0, \\\"results\\\": []}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"reconciled\": 0, \"results\": []}, \"error\": null, \"metadata\": {}}"
    }
  },
  "sourceToolAssistantUUID": "3863c078-9182-4bde-aca1-9efbf20a6b85",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/agent_66b8aa9d",
  "sessionId": "062027a5-1c13-4530-a568-995829f28b19",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-22T18:49:25.910Z_

<details><summary>↩ Tool result · `toolu_01XRSjA9KrTL8dEP11jsys48`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/report.md\", \"content\": \"# Handover — 2026-05-22\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\\n|--------|------|------|---------|-----|\\n| perlayer_kl_50_s42 | Per-layer KL 50% uniform training (seed 42). Tests whether 2D decomposition (signal type × coupling scope) holds at higher sparsity. PPL should fall between E2E KL 50% (11.84) and MSE (18.52). If gap to E2E KL is small (&lt;5%), signal type dominates PPL even at 50%, strengthening the 2D claim. | — | — | — |\\n\\n## 待处理\\n- perlayer_kl_s123_downstream_v2: Per-layer KL s123 downstream 6-task eval (ARC-c, WG, MMLU, GSM8K, HS, PIQA) — excluding BoolQ due to missing super_glue cache on westd-34887. Retry of perlayer_kl_s123_downstream.（等待人工审批）\\n- perlayer_kl_50_s42_boolq（准备中）\\n- perlayer_kl_50_s42_ppl（准备中）\\n- revkl_30_s42_boolq_uniform（准备中）\\n- diag_eval_env_34887（准备中）\\n- perlayer_kl_s456_ppl_repro: Reproducibility check: per-layer KL s456 PPL should match original 9.0282. Running with same checkpoint on different eval session to verify stability.（准备中）\\n- diag_status_34887（准备中）\\n- diag_status_41718（准备中）\\n- read_boolq_results（准备中）\\n- diag_ckpt_34887（准备中）\\n- …另有 40 项\\n\\n## 近期结论\\n- **perlayer_kl_k4_50_s42_ppl_v2** (negative): K=4 per-layer KL at 50% sparsity PPL eval (retry of perlayer_kl_k4_50_s42_ppl which failed due to ambiguous --sparsity arg). K=1 50% PPL=34.85, E2E KL 50% PPL=11.84. If K=4 PPL is close to E2E → mismatch dominates at 50% (same as 30%). If K=4 PPL remains high → genuine coupling increases with sparsity. ← 基于 perlayer_kl_k4_50_s42\\n- **perlayer_kl_k4_50_s42_ppl** (failed): K=4 per-layer KL at 50% sparsity PPL eval. K=1 50% PPL=34.85, E2E KL 50% PPL=11.84. If K=4 PPL is close to E2E → mismatch dominates at 50% (same as 30%). If K=4 PPL remains high → genuine coupling increases with sparsity. ← 基于 perlayer_kl_k4_50_s42\\n- **perlayer_kl_k4_50_s42** (success): K=4 per-layer KL at 50% sparsity: tests mismatch explanation rate at high sparsity. K=1 50% PPL=34.85, E2E KL 50% PPL=11.84. If K=4 closes large gap → mismatch dominates even more at high sparsity. ← 基于 perlayer_kl_50_s42\\n\\n## 趋势\\n成功 248 / 负向 29 / 失败 32 / 共 326\\narc_challenge_acc_norm: 0.3916 ↓（近 3 次 success）\\ngsm8k_exact_match: 0.0341 ↓（近 3 次 success）\\n\\n## 下一步\\n（无活跃 idea，请通过 ideas.md 添加）\\n\\n## 资源状态\\nwestd-34887: 无 GPU 信息\\nwestd-41718: 无 GPU 信息\\n\\n## 告警\\n- mvp_kl_s123: 已被终止 — unknown\\n- mvp_kl_s456: 已被终止 — unknown\\n- kl_normalized_quicktest: 训练失败 — unknown\\n- mvp_kl_norm_s42: 训练失败 — unknown\\n- mvp_kl_norm_s123: 训练失败 — unknown\\n- spon_training_seq2048: 已被终止 — unknown\\n- ste_kl_s42: 已被终止 — unknown\\n- bce_isocompute_s42: 训练失败 — unknown\\n- eval_spon_supp_retry: 训练失败 — unknown\\n- bce_isocompute_s42_v2: 已被终止 — unknown\\n- spon_supp_eval_retry: 训练失败 — unknown\\n- kl_sparsity30_s42: 已被终止 — unknown\\n- kl_sparsity70_s42: 已被终止 — unknown\\n- lm_eval_dense_test: 训练失败 — unknown\\n- lm_eval_mistral_downstream: 训练失败 — unknown\\n- bench_mistral_kl50_s42: 已被终止 — unknown\\n- longbench_kl30_uniform: 训练失败 — unknown\\n- longbench_dense: 训练失败 — unknown\\n- longbench_kl30_uniform_v2: 训练失败 — unknown\\n- longbench_dense_v2: 训练失败 — unknown\\n- longbench_kl30_uniform_v3: 训练失败 — unknown\\n- longbench_dense_v3: 训练失败 — unknown\\n- longbench_dense_v4: 训练失败 — unknown\\n- steps_curve_s42: 已被终止 — unknown\\n- steps_curve_s42_v2: 已被终止 — unknown\\n- qwen14b_kl30_uniform_eval: 训练失败 — unknown\\n- qwen14b_teal30_uniform_eval: 训练失败 — unknown\\n- c4_ood_dense_baseline: 训练失败 — unknown\\n- downstream_ext_kl50_uniform_s42: 训练失败 — unknown\\n- downstream_ext_kl30_uniform_s123: 训练失败 — unknown\\n- c1_ablation_30pct_s42: 训练失败 — unknown\\n- c1_ablation_30pct_s42_eval: 训练失败 — unknown\\n- bce_isocompute_hellaswag_piqa: 训练失败 — unknown\\n- c1_ablation_30pct_eval_34887: 已被终止 — unknown\\n- qwen14b_kl30_s123_eval: 已被终止 — unknown\\n- qwen14b_kl30_s456_eval: 已被终止 — unknown\\n- qwen14b_kl30_s123_eval_v2: 训练失败 — unknown\\n- qwen14b_kl30_s123_eval_v3: 训练失败 — unknown\\n- qwen14b_kl30_s42_eval_uniform: 训练失败 — unknown\\n- qwen14b_kl30_s42_eval_uniform_v2: 已被终止 — unknown\\n- qwen14b_teal275_uniform_eval: 已被终止 — unknown\\n- qwen14b_teal275_uniform_eval_v2: 训练失败 — unknown\\n- flashinfer_benchmark_llama8b: 训练失败 — unknown\\n- qwen14b_kl30_s42_gsm8k: 已被终止 — unknown\\n- qwen14b_dense_4task: 训练失败 — unknown\\n- mse50_s123_eval_retry: 已被终止 — Director ordered kill - PPL=15789 (random level), MSE sparsity collapsed to 5.1% during training, forced 50% mask produces garbage. Not re-running.\\n- perlayer_kl_s456_boolq: 训练失败 — unknown\\n- perlayer_kl_s123_downstream: 训练失败 — unknown\\n- perlayer_kl_k4_50_s42_ppl: 训练失败 — unknown\\n\", \"total_chars\": 4437, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bd12f263-bb99-4545-b1fb-dd6abf57feff",
  "isSidechain": false,
  "promptId": "e0126d52-e1d3-4c8c-a4f2-76af8e88bda0",
  "type": "user",
  "uuid": "f5ab47e2-fb5c-4046-bd3e-6812defdff50",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/report.md\\\", \\\"content\\\": \\\"# Handover — 2026-05-22\\\\n\\\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\\\n\\\\n## 运行中\\\\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\\\\n|--------|------|------|---------|-----|\\\\n| perlayer_kl_50_s42 | Per-layer KL 50% uniform training (seed 42). Tests whether 2D decomposition (signal type × coupling scope) holds at higher sparsity. PPL should fall between E2E KL 50% (11.84) and MSE (18.52). If gap to E2E KL is small (&lt;5%), signal type dominates PPL even at 50%, strengthening the 2D claim. | — | — | — |\\\\n\\\\n## 待处理\\\\n- perlayer_kl_s123_downstream_v2: Per-layer KL s123 downstream 6-task eval (ARC-c, WG, MMLU, GSM8K, HS, PIQA) — excluding BoolQ due to missing super_glue cache on westd-34887. Retry of perlayer_kl_s123_downstream.（等待人工审批）\\\\n- perlayer_kl_50_s42_boolq（准备中）\\\\n- perlayer_kl_50_s42_ppl（准备中）\\\\n- revkl_30_s42_boolq_uniform（准备中）\\\\n- diag_eval_env_34887（准备中）\\\\n- perlayer_kl_s456_ppl_repro: Reproducibility check: per-layer KL s456 PPL should match original 9.0282. Running with same checkpoint on different eval session to verify stability.（准备中）\\\\n- diag_status_34887（准备中）\\\\n- diag_status_41718（准备中）\\\\n- read_boolq_results（准备中）\\\\n- diag_ckpt_34887（准备中）\\\\n- …另有 40 项\\\\n\\\\n## 近期结论\\\\n- **perlayer_kl_k4_50_s42_ppl_v2** (negative): K=4 per-layer KL at 50% sparsity PPL eval (retry of perlayer_kl_k4_50_s42_ppl which failed due to ambiguous --sparsity arg). K=1 50% PPL=34.85, E2E KL 50% PPL=11.84. If K=4 PPL is close to E2E → mismatch dominates at 50% (same as 30%). If K=4 PPL remains high → genuine coupling increases with sparsity. ← 基于 perlayer_kl_k4_50_s42\\\\n- **perlayer_kl_k4_50_s42_ppl** (failed): K=4 per-layer KL at 50% sparsity PPL eval. K=1 50% PPL=34.85, E2E KL 50% PPL=11.84. If K=4 PPL is close to E2E → mismatch dominates at 50% (same as 30%). If K=4 PPL remains high → genuine coupling increases with sparsity. ← 基于 perlayer_kl_k4_50_s42\\\\n- **perlayer_kl_k4_50_s42** (success): K=4 per-layer KL at 50% sparsity: tests mismatch explanation rate at high sparsity. K=1 50% PPL=34.85, E2E KL 50% PPL=11.84. If K=4 closes large gap → mismatch dominates even more at high sparsity. ← 基于 perlayer_kl_50_s42\\\\n\\\\n## 趋势\\\\n成功 248 / 负向 29 / 失败 32 / 共 326\\\\narc_challenge_acc_norm: 0.3916 ↓（近 3 次 success）\\\\ngsm8k_exact_match: 0.0341 ↓（近 3 次 success）\\\\n\\\\n## 下一步\\\\n（无活跃 idea，请通过 ideas.md 添加）\\\\n\\\\n## 资源状态\\\\nwestd-34887: 无 GPU 信息\\\\nwestd-41718: 无 GPU 信息\\\\n\\\\n## 告警\\\\n- mvp_kl_s123: 已被终止 — unknown\\\\n- mvp_kl_s456: 已被终止 — unknown\\\\n- kl_normalized_quicktest: 训练失败 — unknown\\\\n- mvp_kl_norm_s42: 训练失败 — unknown\\\\n- mvp_kl_norm_s123: 训练失败 — unknown\\\\n- spon_training_seq2048: 已被终止 — unknown\\\\n- ste_kl_s42: 已被终止 — unknown\\\\n- bce_isocompute_s42: 训练失败 — unknown\\\\n- eval_spon_supp_retry: 训练失败 — unknown\\\\n- bce_isocompute_s42_v2: 已被终止 — unknown\\\\n- spon_supp_eval_retry: 训练失败 — unknown\\\\n- kl_sparsity30_s42: 已被终止 — unknown\\\\n- kl_sparsity70_s42: 已被终止 — unknown\\\\n- lm_eval_dense_test: 训练失败 — unknown\\\\n- lm_eval_mistral_downstream: 训练失败 — unknown\\\\n- bench_mistral_kl50_s42: 已被终止 — unknown\\\\n- longbench_kl30_uniform: 训练失败 — unknown\\\\n- longbench_dense: 训练失败 — unknown\\\\n- longbench_kl30_uniform_v2: 训练失败 — unknown\\\\n- longbench_dense_v2: 训练失败 — unknown\\\\n- longbench_kl30_uniform_v3: 训练失败 — unknown\\\\n- longbench_dense_v3: 训练失败 — unknown\\\\n- longbench_dense_v4: 训练失败 — unknown\\\\n- steps_curve_s42: 已被终止 — unknown\\\\n- steps_curve_s42_v2: 已被终止 — unknown\\\\n- qwen14b_kl30_uniform_eval: 训练失败 — unknown\\\\n- qwen14b_teal30_uniform_eval: 训练失败 — unknown\\\\n- c4_ood_dense_baseline: 训练失败 — unknown\\\\n- downstream_ext_kl50_uniform_s42: 训练失败 — unknown\\\\n- downstream_ext_kl30_uniform_s123: 训练失败 — unknown\\\\n- c1_ablation_30pct_s42: 训练失败 — unknown\\\\n- c1_ablation_30pct_s42_eval: 训练失败 — unknown\\\\n- bce_isocompute_hellaswag_piqa: 训练失败 — unknown\\\\n- c1_ablation_30pct_eval_34887: 已被终止 — unknown\\\\n- qwen14b_kl30_s123_eval: 已被终止 — unknown\\\\n- qwen14b_kl30_s456_eval: 已被终止 — unknown\\\\n- qwen14b_kl30_s123_eval_v2: 训练失败 — unknown\\\\n- qwen14b_kl30_s123_eval_v3: 训练失败 — unknown\\\\n- qwen14b_kl30_s42_eval_uniform: 训练失败 — unknown\\\\n- qwen14b_kl30_s42_eval_uniform_v2: 已被终止 — unknown\\\\n- qwen14b_teal275_uniform_eval: 已被终止 — unknown\\\\n- qwen14b_teal275_uniform_eval_v2: 训练失败 — unknown\\\\n- flashinfer_benchmark_llama8b: 训练失败 — unknown\\\\n- qwen14b_kl30_s42_gsm8k: 已被终止 — unknown\\\\n- qwen14b_dense_4task: 训练失败 — unknown\\\\n- mse50_s123_eval_retry: 已被终止 — Director ordered kill - PPL=15789 (random level), MSE sparsity collapsed to 5.1% during training, forced 50% mask produces garbage. Not re-running.\\\\n- perlayer_kl_s456_boolq: 训练失败 — unknown\\\\n- perlayer_kl_s123_downstream: 训练失败 — unknown\\\\n- perlayer_kl_k4_50_s42_ppl: 训练失败 — unknown\\\\n\\\", \\\"total_chars\\\": 4437, \\\"truncated\\\": false}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/report.md\", \"content\": \"# Handover — 2026-05-22\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\\n|--------|------|------|---------|-----|\\n| perlayer_kl_50_s42 | Per-layer KL 50% uniform training (seed 42). Tests whether 2D decomposition (signal type × coupling scope) holds at higher sparsity. PPL should fall between E2E KL 50% (11.84) and MSE (18.52). If gap to E2E KL is small (&lt;5%), signal type dominates PPL even at 50%, strengthening the 2D claim. | — | — | — |\\n\\n## 待处理\\n- perlayer_kl_s123_downstream_v2: Per-layer KL s123 downstream 6-task eval (ARC-c, WG, MMLU, GSM8K, HS, PIQA) — excluding BoolQ due to missing super_glue cache on westd-34887. Retry of perlayer_kl_s123_downstream.（等待人工审批）\\n- perlayer_kl_50_s42_boolq（准备中）\\n- perlayer_kl_50_s42_ppl（准备中）\\n- revkl_30_s42_boolq_uniform（准备中）\\n- diag_eval_env_34887（准备中）\\n- perlayer_kl_s456_ppl_repro: Reproducibility check: per-layer KL s456 PPL should match original 9.0282. Running with same checkpoint on different eval session to verify stability.（准备中）\\n- diag_status_34887（准备中）\\n- diag_status_41718（准备中）\\n- read_boolq_results（准备中）\\n- diag_ckpt_34887（准备中）\\n- …另有 40 项\\n\\n## 近期结论\\n- **perlayer_kl_k4_50_s42_ppl_v2** (negative): K=4 per-layer KL at 50% sparsity PPL eval (retry of perlayer_kl_k4_50_s42_ppl which failed due to ambiguous --sparsity arg). K=1 50% PPL=34.85, E2E KL 50% PPL=11.84. If K=4 PPL is close to E2E → mismatch dominates at 50% (same as 30%). If K=4 PPL remains high → genuine coupling increases with sparsity. ← 基于 perlayer_kl_k4_50_s42\\n- **perlayer_kl_k4_50_s42_ppl** (failed): K=4 per-layer KL at 50% sparsity PPL eval. K=1 50% PPL=34.85, E2E KL 50% PPL=11.84. If K=4 PPL is close to E2E → mismatch dominates at 50% (same as 30%). If K=4 PPL remains high → genuine coupling increases with sparsity. ← 基于 perlayer_kl_k4_50_s42\\n- **perlayer_kl_k4_50_s42** (success): K=4 per-layer KL at 50% sparsity: tests mismatch explanation rate at high sparsity. K=1 50% PPL=34.85, E2E KL 50% PPL=11.84. If K=4 closes large gap → mismatch dominates even more at high sparsity. ← 基于 perlayer_kl_50_s42\\n\\n## 趋势\\n成功 248 / 负向 29 / 失败 32 / 共 326\\narc_challenge_acc_norm: 0.3916 ↓（近 3 次 success）\\ngsm8k_exact_match: 0.0341 ↓（近 3 次 success）\\n\\n## 下一步\\n（无活跃 idea，请通过 ideas.md 添加）\\n\\n## 资源状态\\nwestd-34887: 无 GPU 信息\\nwestd-41718: 无 GPU 信息\\n\\n## 告警\\n- mvp_kl_s123: 已被终止 — unknown\\n- mvp_kl_s456: 已被终止 — unknown\\n- kl_normalized_quicktest: 训练失败 — unknown\\n- mvp_kl_norm_s42: 训练失败 — unknown\\n- mvp_kl_norm_s123: 训练失败 — unknown\\n- spon_training_seq2048: 已被终止 — unknown\\n- ste_kl_s42: 已被终止 — unknown\\n- bce_isocompute_s42: 训练失败 — unknown\\n- eval_spon_supp_retry: 训练失败 — unknown\\n- bce_isocompute_s42_v2: 已被终止 — unknown\\n- spon_supp_eval_retry: 训练失败 — unknown\\n- kl_sparsity30_s42: 已被终止 — unknown\\n- kl_sparsity70_s42: 已被终止 — unknown\\n- lm_eval_dense_test: 训练失败 — unknown\\n- lm_eval_mistral_downstream: 训练失败 — unknown\\n- bench_mistral_kl50_s42: 已被终止 — unknown\\n- longbench_kl30_uniform: 训练失败 — unknown\\n- longbench_dense: 训练失败 — unknown\\n- longbench_kl30_uniform_v2: 训练失败 — unknown\\n- longbench_dense_v2: 训练失败 — unknown\\n- longbench_kl30_uniform_v3: 训练失败 — unknown\\n- longbench_dense_v3: 训练失败 — unknown\\n- longbench_dense_v4: 训练失败 — unknown\\n- steps_curve_s42: 已被终止 — unknown\\n- steps_curve_s42_v2: 已被终止 — unknown\\n- qwen14b_kl30_uniform_eval: 训练失败 — unknown\\n- qwen14b_teal30_uniform_eval: 训练失败 — unknown\\n- c4_ood_dense_baseline: 训练失败 — unknown\\n- downstream_ext_kl50_uniform_s42: 训练失败 — unknown\\n- downstream_ext_kl30_uniform_s123: 训练失败 — unknown\\n- c1_ablation_30pct_s42: 训练失败 — unknown\\n- c1_ablation_30pct_s42_eval: 训练失败 — unknown\\n- bce_isocompute_hellaswag_piqa: 训练失败 — unknown\\n- c1_ablation_30pct_eval_34887: 已被终止 — unknown\\n- qwen14b_kl30_s123_eval: 已被终止 — unknown\\n- qwen14b_kl30_s456_eval: 已被终止 — unknown\\n- qwen14b_kl30_s123_eval_v2: 训练失败 — unknown\\n- qwen14b_kl30_s123_eval_v3: 训练失败 — unknown\\n- qwen14b_kl30_s42_eval_uniform: 训练失败 — unknown\\n- qwen14b_kl30_s42_eval_uniform_v2: 已被终止 — unknown\\n- qwen14b_teal275_uniform_eval: 已被终止 — unknown\\n- qwen14b_teal275_uniform_eval_v2: 训练失败 — unknown\\n- flashinfer_benchmark_llama8b: 训练失败 — unknown\\n- qwen14b_kl30_s42_gsm8k: 已被终止 — unknown\\n- qwen14b_dense_4task: 训练失败 — unknown\\n- mse50_s123_eval_retry: 已被终止 — Director ordered kill - PPL=15789 (random level), MSE sparsity collapsed to 5.1% during training, forced 50% mask produces garbage. Not re-running.\\n- perlayer_kl_s456_boolq: 训练失败 — unknown\\n- perlayer_kl_s123_downstream: 训练失败 — unknown\\n- perlayer_kl_k4_50_s42_ppl: 训练失败 — unknown\\n\", \"total_chars\": 4437, \"truncated\": false}, \"error\": null, \"metadata\": {}}"
    }
  },
  "sourceToolAssistantUUID": "bd12f263-bb99-4545-b1fb-dd6abf57feff",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/agent_66b8aa9d",
  "sessionId": "062027a5-1c13-4530-a568-995829f28b19",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-22T18:49:25.949Z_

<details><summary>↩ Tool result · `toolu_01CqjYCFa4mQqRK4Bfnfz86c`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/ROADMAP.md\", \"content\": \"# distill_sparse_swiglu — Research Dashboard\\n\\n> 最后更新: 2026-05-22 13:01 UTC | 更新原因: K=4 downstream 完成 + R21 提交 + 全 action items 完成\\n\\n## 核心方向\\nKL distillation for SwiGLU sparsity prediction：output-distribution alignment 是 PPL 的主导设计维度。K=4 mismatch control 揭示 downstream coupling 是 task-dependent 的——knowledge 任务的 gap 主要来自 mismatch，commonsense 有真实 coupling (~60%)，math 需要全层优化。详见 paper_framing.md。\\n\\n## 当前进展\\n- **阶段**: Review → Round 21 提交中（continue mode，待用户批准）\\n- **Round 20 评分**: 3.0 Findings（fresh review）\\n- **R20 全部 action items 完成**：\\n  - ✅ 术语重构：coupling alignment → output-distribution alignment\\n  - ✅ K=4 mismatch control pilot（PPL 66.7% mismatch + task-dependent downstream）\\n  - ✅ Per-layer sparsity protection valley (L14-L18) 机制分析\\n  - ✅ MSE 3-seed downstream 2D decomposition\\n  - ✅ confirms→suggests 全文 8 处\\n  - ✅ BoolQ seed-matched footnote（Reviewer 修正：73% 非 95%）\\n  - ✅ Limitations 扩充（batched inference, WikiText 同分布）\\n  - ✅ efficiency language 残留清除\\n\\n## 近期任务\\n- [x] K=4 pilot 训练 + downstream eval\\n- [x] Paper Agent K=4 patch（§4.5 重写 + abstract/conclusion/intro）\\n- [x] BoolQ appendix table 修正（seed-matched footnote）\\n- [x] confirms→suggests 4 处残留修正\\n- [x] Appendix L489 修正（已确认正确）\\n- [x] 编译检查（0 critical warnings，主文 ≤ 8 页）\\n- [x] R21 审稿提交（continue mode）\\n- [ ] 等待 R21 审稿结果\\n- [ ] 根据 R21 结果决定是否需要进一步实验\\n\\n## GPU 预算\\n- 分配: westd-41718 cuda:0,1 + westd-34887 cuda:0,1（4× RTX PRO 6000 Blackwell 96GB）\\n- 当前: 全部空闲（K=4 eval 已完成，无 pending 实验）\\n- DDL: 2026-05-25（EMNLP 2026 ARR May cycle，剩余 ~2.5 天）\\n\\n## 关键数据汇总\\n\\n### K=4 Mismatch Control（核心新发现）\\n| Task | K=4 | K=1 | E2E KL | Mismatch解释% | 解读 |\\n|------|-----|-----|--------|---------------|------|\\n| PPL | 8.89 | 9.05 | 8.81 | 66.7% | mismatch 主导 |\\n| ARC-c | 41.0 | 39.9 | 43.7 | 28.9% | 真实 coupling ~71% |\\n| WG | 66.7 | 65.9 | 68.9 | 26.7% | 真实 coupling ~73% |\\n| MMLU | 43.5 | 38.6 | 40.7 | >100% | 异常（training-eval alignment?）|\\n| GSM8K | 5.2 | 5.8 | 7.5 | -35% | 需要全层 gradient flow |\\n| BoolQ | 73.2 | 71.8(s42) | 73.7 | 73.1%(s42) | mismatch 主导 |\\n\\n### 主表数据（30% uniform）\\n| Method | PPL | ARC-c | WG | MMLU | GSM8K | BoolQ |\\n|--------|-----|-------|------|------|-------|-------|\\n| E2E KL | 8.81±0.02 | 43.7±2.5 | 68.9±0.4 | 40.7±1.3 | 7.5±0.1 | 73.7±3.2 |\\n| Per-layer KL | 9.05±0.02 | 39.9±1.9 | 65.9±0.6 | 38.6±0.7 | 5.8±0.6 | 64.5±11.5 |\\n| MSE | 18.52±1.68 | 35.8±4.1 | 59.8±2.6 | 30.7±2.6 | 2.3±0.7 | 64.5±5.3 |\\n\\n## 关键决策日志\\n\\n| ID | 日期 | 摘要 | 关联实验 |\\n|----|------|------|----------|\\n| D103 | 2026-05-22 | K=4 3-seed downstream 完成：ARC-c 97% genuine couplin | perlayer_kl_k4_s123, perlayer_kl_k4_s456, constraint_remove_valley_kl30_s42 |\\n| D102 | 2026-05-22 | Constraint 双向实验揭示 allocation trade-off：protection  | constraint_protect_late_kl30_s42, constraint_remove_valley_kl30_s42 |\\n| D101 | 2026-05-22 | R21 Action Matrix: K=4 multi-seed + per-layer cons | perlayer_kl_k4_30 |\\n| D100 | 2026-05-22 | Qwen-14B GSM8K 数据完整性修复：补跑 s123 uniform GSM8K + 核查  | qwen14b_kl30_s42_gsm8k_uniform |\\n| D099 | 2026-05-22 | K=4 pilot 揭示 task-dependent mismatch：PPL/BoolQ 主要是 | gradual_k4_pilot, perlayer_kl_30_3seed, kl30_3seed |\\n| D098 | 2026-05-22 | R20 Action Matrix: 术语重构(coupling→output-dist align | gradual_k4_pilot, mse30_s123_downstream, mse30_s456_downstream |\\n| D097 | 2026-05-22 | R19 Action Matrix 修订：补 MSE 30% downstream eval（用户强 | mse_30_downstream |\\n| D096 | 2026-05-22 | Round 19 审稿 3.0 Findings 应对：18 条 paper patch，无需补实验 | perlayer_kl_50_s42, cross_seed_jaccard_r18w7 |\\n| D095 | 2026-05-22 | Per-layer KL 50% PPL=34.85 纳入论文：2D decomposition 升 | perlayer_kl_50_s42 |\\n| D094 | 2026-05-22 | 审稿等待期启动 per-layer KL 50% s42 训练，填充 Table 4 空行 | — |\\n\\n\", \"lines\": 71}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bf8804e3-2543-4006-b66c-b6a3e9970be6",
  "isSidechain": false,
  "promptId": "e0126d52-e1d3-4c8c-a4f2-76af8e88bda0",
  "type": "user",
  "uuid": "2a571e19-b4e3-445f-bb12-ab3495569603",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/ROADMAP.md\\\", \\\"content\\\": \\\"# distill_sparse_swiglu — Research Dashboard\\\\n\\\\n> 最后更新: 2026-05-22 13:01 UTC | 更新原因: K=4 downstream 完成 + R21 提交 + 全 action items 完成\\\\n\\\\n## 核心方向\\\\nKL distillation for SwiGLU sparsity prediction：output-distribution alignment 是 PPL 的主导设计维度。K=4 mismatch control 揭示 downstream coupling 是 task-dependent 的——knowledge 任务的 gap 主要来自 mismatch，commonsense 有真实 coupling (~60%)，math 需要全层优化。详见 paper_framing.md。\\\\n\\\\n## 当前进展\\\\n- **阶段**: Review → Round 21 提交中（continue mode，待用户批准）\\\\n- **Round 20 评分**: 3.0 Findings（fresh review）\\\\n- **R20 全部 action items 完成**：\\\\n  - ✅ 术语重构：coupling alignment → output-distribution alignment\\\\n  - ✅ K=4 mismatch control pilot（PPL 66.7% mismatch + task-dependent downstream）\\\\n  - ✅ Per-layer sparsity protection valley (L14-L18) 机制分析\\\\n  - ✅ MSE 3-seed downstream 2D decomposition\\\\n  - ✅ confirms→suggests 全文 8 处\\\\n  - ✅ BoolQ seed-matched footnote（Reviewer 修正：73% 非 95%）\\\\n  - ✅ Limitations 扩充（batched inference, WikiText 同分布）\\\\n  - ✅ efficiency language 残留清除\\\\n\\\\n## 近期任务\\\\n- [x] K=4 pilot 训练 + downstream eval\\\\n- [x] Paper Agent K=4 patch（§4.5 重写 + abstract/conclusion/intro）\\\\n- [x] BoolQ appendix table 修正（seed-matched footnote）\\\\n- [x] confirms→suggests 4 处残留修正\\\\n- [x] Appendix L489 修正（已确认正确）\\\\n- [x] 编译检查（0 critical warnings，主文 ≤ 8 页）\\\\n- [x] R21 审稿提交（continue mode）\\\\n- [ ] 等待 R21 审稿结果\\\\n- [ ] 根据 R21 结果决定是否需要进一步实验\\\\n\\\\n## GPU 预算\\\\n- 分配: westd-41718 cuda:0,1 + westd-34887 cuda:0,1（4× RTX PRO 6000 Blackwell 96GB）\\\\n- 当前: 全部空闲（K=4 eval 已完成，无 pending 实验）\\\\n- DDL: 2026-05-25（EMNLP 2026 ARR May cycle，剩余 ~2.5 天）\\\\n\\\\n## 关键数据汇总\\\\n\\\\n### K=4 Mismatch Control（核心新发现）\\\\n| Task | K=4 | K=1 | E2E KL | Mismatch解释% | 解读 |\\\\n|------|-----|-----|--------|---------------|------|\\\\n| PPL | 8.89 | 9.05 | 8.81 | 66.7% | mismatch 主导 |\\\\n| ARC-c | 41.0 | 39.9 | 43.7 | 28.9% | 真实 coupling ~71% |\\\\n| WG | 66.7 | 65.9 | 68.9 | 26.7% | 真实 coupling ~73% |\\\\n| MMLU | 43.5 | 38.6 | 40.7 | >100% | 异常（training-eval alignment?）|\\\\n| GSM8K | 5.2 | 5.8 | 7.5 | -35% | 需要全层 gradient flow |\\\\n| BoolQ | 73.2 | 71.8(s42) | 73.7 | 73.1%(s42) | mismatch 主导 |\\\\n\\\\n### 主表数据（30% uniform）\\\\n| Method | PPL | ARC-c | WG | MMLU | GSM8K | BoolQ |\\\\n|--------|-----|-------|------|------|-------|-------|\\\\n| E2E KL | 8.81±0.02 | 43.7±2.5 | 68.9±0.4 | 40.7±1.3 | 7.5±0.1 | 73.7±3.2 |\\\\n| Per-layer KL | 9.05±0.02 | 39.9±1.9 | 65.9±0.6 | 38.6±0.7 | 5.8±0.6 | 64.5±11.5 |\\\\n| MSE | 18.52±1.68 | 35.8±4.1 | 59.8±2.6 | 30.7±2.6 | 2.3±0.7 | 64.5±5.3 |\\\\n\\\\n## 关键决策日志\\\\n\\\\n| ID | 日期 | 摘要 | 关联实验 |\\\\n|----|------|------|----------|\\\\n| D103 | 2026-05-22 | K=4 3-seed downstream 完成：ARC-c 97% genuine couplin | perlayer_kl_k4_s123, perlayer_kl_k4_s456, constraint_remove_valley_kl30_s42 |\\\\n| D102 | 2026-05-22 | Constraint 双向实验揭示 allocation trade-off：protection  | constraint_protect_late_kl30_s42, constraint_remove_valley_kl30_s42 |\\\\n| D101 | 2026-05-22 | R21 Action Matrix: K=4 multi-seed + per-layer cons | perlayer_kl_k4_30 |\\\\n| D100 | 2026-05-22 | Qwen-14B GSM8K 数据完整性修复：补跑 s123 uniform GSM8K + 核查  | qwen14b_kl30_s42_gsm8k_uniform |\\\\n| D099 | 2026-05-22 | K=4 pilot 揭示 task-dependent mismatch：PPL/BoolQ 主要是 | gradual_k4_pilot, perlayer_kl_30_3seed, kl30_3seed |\\\\n| D098 | 2026-05-22 | R20 Action Matrix: 术语重构(coupling→output-dist align | gradual_k4_pilot, mse30_s123_downstream, mse30_s456_downstream |\\\\n| D097 | 2026-05-22 | R19 Action Matrix 修订：补 MSE 30% downstream eval（用户强 | mse_30_downstream |\\\\n| D096 | 2026-05-22 | Round 19 审稿 3.0 Findings 应对：18 条 paper patch，无需补实验 | perlayer_kl_50_s42, cross_seed_jaccard_r18w7 |\\\\n| D095 | 2026-05-22 | Per-layer KL 50% PPL=34.85 纳入论文：2D decomposition 升 | perlayer_kl_50_s42 |\\\\n| D094 | 2026-05-22 | 审稿等待期启动 per-layer KL 50% s42 训练，填充 Table 4 空行 | — |\\\\n\\\\n\\\", \\\"lines\\\": 71}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/ROADMAP.md\", \"content\": \"# distill_sparse_swiglu — Research Dashboard\\n\\n> 最后更新: 2026-05-22 13:01 UTC | 更新原因: K=4 downstream 完成 + R21 提交 + 全 action items 完成\\n\\n## 核心方向\\nKL distillation for SwiGLU sparsity prediction：output-distribution alignment 是 PPL 的主导设计维度。K=4 mismatch control 揭示 downstream coupling 是 task-dependent 的——knowledge 任务的 gap 主要来自 mismatch，commonsense 有真实 coupling (~60%)，math 需要全层优化。详见 paper_framing.md。\\n\\n## 当前进展\\n- **阶段**: Review → Round 21 提交中（continue mode，待用户批准）\\n- **Round 20 评分**: 3.0 Findings（fresh review）\\n- **R20 全部 action items 完成**：\\n  - ✅ 术语重构：coupling alignment → output-distribution alignment\\n  - ✅ K=4 mismatch control pilot（PPL 66.7% mismatch + task-dependent downstream）\\n  - ✅ Per-layer sparsity protection valley (L14-L18) 机制分析\\n  - ✅ MSE 3-seed downstream 2D decomposition\\n  - ✅ confirms→suggests 全文 8 处\\n  - ✅ BoolQ seed-matched footnote（Reviewer 修正：73% 非 95%）\\n  - ✅ Limitations 扩充（batched inference, WikiText 同分布）\\n  - ✅ efficiency language 残留清除\\n\\n## 近期任务\\n- [x] K=4 pilot 训练 + downstream eval\\n- [x] Paper Agent K=4 patch（§4.5 重写 + abstract/conclusion/intro）\\n- [x] BoolQ appendix table 修正（seed-matched footnote）\\n- [x] confirms→suggests 4 处残留修正\\n- [x] Appendix L489 修正（已确认正确）\\n- [x] 编译检查（0 critical warnings，主文 ≤ 8 页）\\n- [x] R21 审稿提交（continue mode）\\n- [ ] 等待 R21 审稿结果\\n- [ ] 根据 R21 结果决定是否需要进一步实验\\n\\n## GPU 预算\\n- 分配: westd-41718 cuda:0,1 + westd-34887 cuda:0,1（4× RTX PRO 6000 Blackwell 96GB）\\n- 当前: 全部空闲（K=4 eval 已完成，无 pending 实验）\\n- DDL: 2026-05-25（EMNLP 2026 ARR May cycle，剩余 ~2.5 天）\\n\\n## 关键数据汇总\\n\\n### K=4 Mismatch Control（核心新发现）\\n| Task | K=4 | K=1 | E2E KL | Mismatch解释% | 解读 |\\n|------|-----|-----|--------|---------------|------|\\n| PPL | 8.89 | 9.05 | 8.81 | 66.7% | mismatch 主导 |\\n| ARC-c | 41.0 | 39.9 | 43.7 | 28.9% | 真实 coupling ~71% |\\n| WG | 66.7 | 65.9 | 68.9 | 26.7% | 真实 coupling ~73% |\\n| MMLU | 43.5 | 38.6 | 40.7 | >100% | 异常（training-eval alignment?）|\\n| GSM8K | 5.2 | 5.8 | 7.5 | -35% | 需要全层 gradient flow |\\n| BoolQ | 73.2 | 71.8(s42) | 73.7 | 73.1%(s42) | mismatch 主导 |\\n\\n### 主表数据（30% uniform）\\n| Method | PPL | ARC-c | WG | MMLU | GSM8K | BoolQ |\\n|--------|-----|-------|------|------|-------|-------|\\n| E2E KL | 8.81±0.02 | 43.7±2.5 | 68.9±0.4 | 40.7±1.3 | 7.5±0.1 | 73.7±3.2 |\\n| Per-layer KL | 9.05±0.02 | 39.9±1.9 | 65.9±0.6 | 38.6±0.7 | 5.8±0.6 | 64.5±11.5 |\\n| MSE | 18.52±1.68 | 35.8±4.1 | 59.8±2.6 | 30.7±2.6 | 2.3±0.7 | 64.5±5.3 |\\n\\n## 关键决策日志\\n\\n| ID | 日期 | 摘要 | 关联实验 |\\n|----|------|------|----------|\\n| D103 | 2026-05-22 | K=4 3-seed downstream 完成：ARC-c 97% genuine couplin | perlayer_kl_k4_s123, perlayer_kl_k4_s456, constraint_remove_valley_kl30_s42 |\\n| D102 | 2026-05-22 | Constraint 双向实验揭示 allocation trade-off：protection  | constraint_protect_late_kl30_s42, constraint_remove_valley_kl30_s42 |\\n| D101 | 2026-05-22 | R21 Action Matrix: K=4 multi-seed + per-layer cons | perlayer_kl_k4_30 |\\n| D100 | 2026-05-22 | Qwen-14B GSM8K 数据完整性修复：补跑 s123 uniform GSM8K + 核查  | qwen14b_kl30_s42_gsm8k_uniform |\\n| D099 | 2026-05-22 | K=4 pilot 揭示 task-dependent mismatch：PPL/BoolQ 主要是 | gradual_k4_pilot, perlayer_kl_30_3seed, kl30_3seed |\\n| D098 | 2026-05-22 | R20 Action Matrix: 术语重构(coupling→output-dist align | gradual_k4_pilot, mse30_s123_downstream, mse30_s456_downstream |\\n| D097 | 2026-05-22 | R19 Action Matrix 修订：补 MSE 30% downstream eval（用户强 | mse_30_downstream |\\n| D096 | 2026-05-22 | Round 19 审稿 3.0 Findings 应对：18 条 paper patch，无需补实验 | perlayer_kl_50_s42, cross_seed_jaccard_r18w7 |\\n| D095 | 2026-05-22 | Per-layer KL 50% PPL=34.85 纳入论文：2D decomposition 升 | perlayer_kl_50_s42 |\\n| D094 | 2026-05-22 | 审稿等待期启动 per-layer KL 50% s42 训练，填充 Table 4 空行 | — |\\n\\n\", \"lines\": 71}, \"error\": null, \"metadata\": {}}"
    }
  },
  "sourceToolAssistantUUID": "bf8804e3-2543-4006-b66c-b6a3e9970be6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/agent_66b8aa9d",
  "sessionId": "062027a5-1c13-4530-a568-995829f28b19",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 22_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[CRON] 实验进程异常退出（失败），需要你诊断原因。 详情: Process exited without valid W&B metrics  - exp_id: kl50_global_s123_downstream_v2 - project: distill_sparse_swiglu - server: westd-34887 - log_path: ~/runs/distill_sp…",
  "leafUuid": "2a571e19-b4e3-445f-bb12-ab3495569603",
  "sessionId": "062027a5-1c13-4530-a568-995829f28b19"
}
```

---

### Runtime record

_source line 23_

```json
{
  "type": "ai-title",
  "aiTitle": "Diagnose W&B metrics missing error in experiment",
  "sessionId": "062027a5-1c13-4530-a568-995829f28b19"
}
```

---

### Assistant

_source line 24 · 2026-05-22T18:49:30.115Z_

<details><summary>Logged reasoning block</summary>

```text
Now let me get the specific experiment details for `kl50_global_s123_downstream_v2` and read the on-experiment-failed skill.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2a571e19-b4e3-445f-bb12-ab3495569603",
  "isSidechain": false,
  "requestId": "req_011CbJ7EavJXhFybiZ3FjFEX",
  "type": "assistant",
  "uuid": "ad6af24f-60b4-46ad-8b5a-9761c682c2db",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/agent_66b8aa9d",
  "sessionId": "062027a5-1c13-4530-a568-995829f28b19",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012XM6t2552oxdWqg5MLs3uJ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5529,
      "cache_read_input_tokens": 41337,
      "output_tokens": 421,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5529,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 421,
          "cache_read_input_tokens": 41337,
          "cache_creation_input_tokens": 5529,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5529
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

_source line 25 · 2026-05-22T18:49:30.495Z_

查看失败实验详情和 on-experiment-failed skill。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ad6af24f-60b4-46ad-8b5a-9761c682c2db",
  "isSidechain": false,
  "requestId": "req_011CbJ7EavJXhFybiZ3FjFEX",
  "type": "assistant",
  "uuid": "5d281fb9-66a7-4851-ad52-4cab03515694",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/agent_66b8aa9d",
  "sessionId": "062027a5-1c13-4530-a568-995829f28b19",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012XM6t2552oxdWqg5MLs3uJ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5529,
      "cache_read_input_tokens": 41337,
      "output_tokens": 421,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5529,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 421,
          "cache_read_input_tokens": 41337,
          "cache_creation_input_tokens": 5529,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5529
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

_source line 26 · 2026-05-22T18:49:42.117Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01RZNvdexfLdZjzrLa6joWfS`</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-14-projects-distill-sparse-swiglu--claude-sessions-agent-66b8aa9d/062027a5-1c13-4530-a568-995829f28b19/tool-results/mcp-agent-ml-research-read_registry-1779475765817.txt | python3 -c \"\nimport json, sys\ndata = json.load(sys.stdin)\nregistry = json.loads(data['result'])\n# Find the specific experiment\nfor exp in registry.get('data', []):\n    if exp.get('exp_id') == 'kl50_global_s123_downstream_v2':\n        print(json.dumps(exp, indent=2))\n        break\n\"",
  "description": "Extract failed experiment details from registry"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5d281fb9-66a7-4851-ad52-4cab03515694",
  "isSidechain": false,
  "requestId": "req_011CbJ7EavJXhFybiZ3FjFEX",
  "type": "assistant",
  "uuid": "2d716f4a-a005-41f4-a005-619a85261ea0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/agent_66b8aa9d",
  "sessionId": "062027a5-1c13-4530-a568-995829f28b19",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012XM6t2552oxdWqg5MLs3uJ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5529,
      "cache_read_input_tokens": 41337,
      "output_tokens": 421,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5529,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 421,
          "cache_read_input_tokens": 41337,
          "cache_creation_input_tokens": 5529,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5529
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

_source line 27 · 2026-05-22T18:49:42.211Z_

<details open><summary>🔧 Tool call — Read · `toolu_01UFspXPzzKxLkWMgnwry2uo`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/skills/on-experiment-failed.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2d716f4a-a005-41f4-a005-619a85261ea0",
  "isSidechain": false,
  "requestId": "req_011CbJ7EavJXhFybiZ3FjFEX",
  "type": "assistant",
  "uuid": "8ded55af-fb0e-43d9-a07c-c2b77b719f8c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/agent_66b8aa9d",
  "sessionId": "062027a5-1c13-4530-a568-995829f28b19",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012XM6t2552oxdWqg5MLs3uJ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5529,
      "cache_read_input_tokens": 41337,
      "output_tokens": 421,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5529,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 421,
          "cache_read_input_tokens": 41337,
          "cache_creation_input_tokens": 5529,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5529
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

_source line 28 · 2026-05-22T18:49:42.499Z_

<details><summary>↩ Tool result · reported error · `toolu_01RZNvdexfLdZjzrLa6joWfS`</summary>

```text
Exit code 1
Traceback (most recent call last):
  File "&lt;string>", line 7, in &lt;module>
    if exp.get('exp_id') == 'kl50_global_s123_downstream_v2':
       ^^^^^^^
AttributeError: 'str' object has no attribute 'get'
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2d716f4a-a005-41f4-a005-619a85261ea0",
  "isSidechain": false,
  "promptId": "e0126d52-e1d3-4c8c-a4f2-76af8e88bda0",
  "type": "user",
  "uuid": "c935aa50-3417-4172-989f-a362bd51fff3",
  "toolUseResult": "Error: Exit code 1\nTraceback (most recent call last):\n  File \"&lt;string>\", line 7, in &lt;module>\n    if exp.get('exp_id') == 'kl50_global_s123_downstream_v2':\n       ^^^^^^^\nAttributeError: 'str' object has no attribute 'get'",
  "sourceToolAssistantUUID": "2d716f4a-a005-41f4-a005-619a85261ea0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/agent_66b8aa9d",
  "sessionId": "062027a5-1c13-4530-a568-995829f28b19",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-22T18:49:42.500Z_

<details><summary>↩ Tool result · reported error · `toolu_01UFspXPzzKxLkWMgnwry2uo`</summary>

```text
&lt;tool_use_error>Cancelled: parallel tool call Bash(cat /home/ubuntu/.claude-account-3/proje…) errored&lt;/tool_use_error>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8ded55af-fb0e-43d9-a07c-c2b77b719f8c",
  "isSidechain": false,
  "promptId": "e0126d52-e1d3-4c8c-a4f2-76af8e88bda0",
  "type": "user",
  "uuid": "ec49d43b-774f-4de6-b168-0439626c3abd",
  "toolUseResult": "Cancelled: parallel tool call Bash(cat /home/ubuntu/.claude-account-3/proje…) errored",
  "sourceToolAssistantUUID": "8ded55af-fb0e-43d9-a07c-c2b77b719f8c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/agent_66b8aa9d",
  "sessionId": "062027a5-1c13-4530-a568-995829f28b19",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-22T18:49:52.743Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01PktStXPULVfxTwChQbXkqH`</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-14-projects-distill-sparse-swiglu--claude-sessions-agent-66b8aa9d/062027a5-1c13-4530-a568-995829f28b19/tool-results/mcp-agent-ml-research-read_registry-1779475765817.txt | python3 -c \"\nimport json, sys\ndata = json.load(sys.stdin)\nresult = json.loads(data['result'])\nprint(type(result['data']))\nif isinstance(result['data'], list):\n    print(type(result['data'][0]))\n    print(result['data'][0][:200] if isinstance(result['data'][0], str) else json.dumps(result['data'][0])[:200])\nelif isinstance(result['data'], dict):\n    print(list(result['data'].keys())[:5])\n\" 2>&1 | head -20",
  "description": "Probe registry data structure"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ec49d43b-774f-4de6-b168-0439626c3abd",
  "isSidechain": false,
  "requestId": "req_011CbJ7FpG1T4H4eYdFQG9j7",
  "type": "assistant",
  "uuid": "f1273fd7-5184-45b6-8351-af4defb9f1c1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/agent_66b8aa9d",
  "sessionId": "062027a5-1c13-4530-a568-995829f28b19",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017fb3GnNoJTvAXM39QUi95q",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 598,
      "cache_read_input_tokens": 46866,
      "output_tokens": 314,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 598,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 314,
          "cache_read_input_tokens": 46866,
          "cache_creation_input_tokens": 598,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 598
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

_source line 31 · 2026-05-22T18:49:52.852Z_

<details><summary>↩ Tool result · `toolu_01PktStXPULVfxTwChQbXkqH`</summary>

```text
&lt;class 'dict'>
['experiments', 'count', 'total', 'baseline']
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f1273fd7-5184-45b6-8351-af4defb9f1c1",
  "isSidechain": false,
  "promptId": "e0126d52-e1d3-4c8c-a4f2-76af8e88bda0",
  "type": "user",
  "uuid": "a899e0ce-a317-437e-a7d7-269159eb1ff1",
  "toolUseResult": {
    "stdout": "&lt;class 'dict'>\n['experiments', 'count', 'total', 'baseline']",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "f1273fd7-5184-45b6-8351-af4defb9f1c1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/agent_66b8aa9d",
  "sessionId": "062027a5-1c13-4530-a568-995829f28b19",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 32 · 2026-05-22T18:49:52.855Z_

```json
{
  "parentUuid": "a899e0ce-a317-437e-a7d7-269159eb1ff1",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "3be5c216-abe7-473f-80f0-26ef771792de",
  "timestamp": "2026-05-22T18:49:52.855Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/agent_66b8aa9d",
  "sessionId": "062027a5-1c13-4530-a568-995829f28b19",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---

### Tool call

_source line 33 · 2026-05-22T18:49:59.187Z_

<details open><summary>🔧 Tool call — Bash · `toolu_017zAkUSC9vuj6DcZWM7QPrw`</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-14-projects-distill-sparse-swiglu--claude-sessions-agent-66b8aa9d/062027a5-1c13-4530-a568-995829f28b19/tool-results/mcp-agent-ml-research-read_registry-1779475765817.txt | python3 -c \"\nimport json, sys\ndata = json.load(sys.stdin)\nresult = json.loads(data['result'])\nexps = result['data']['experiments']\nfor exp in exps:\n    if exp.get('exp_id') == 'kl50_global_s123_downstream_v2':\n        print(json.dumps(exp, indent=2))\n        break\nelse:\n    # try string match\n    for exp in exps:\n        eid = exp if isinstance(exp, str) else exp.get('exp_id','')\n        if 'kl50_global_s123_downstream_v2' in str(eid):\n            print(json.dumps(exp, indent=2) if isinstance(exp, dict) else exp)\n            break\n    else:\n        print('NOT FOUND')\n        print('Sample:', json.dumps(exps[0], indent=2)[:300] if isinstance(exps[0], dict) else str(exps[0])[:300])\n\"",
  "description": "Find kl50_global_s123_downstream_v2 in registry"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3be5c216-abe7-473f-80f0-26ef771792de",
  "isSidechain": false,
  "requestId": "req_011CbJ7GZuLMsp6Libqt9maP",
  "type": "assistant",
  "uuid": "a17f603c-5e31-4db1-9006-65f58525988b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/agent_66b8aa9d",
  "sessionId": "062027a5-1c13-4530-a568-995829f28b19",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011F2yozPVcXY7aPXgWbSsMG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 450,
      "cache_read_input_tokens": 47464,
      "output_tokens": 511,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 450,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 511,
          "cache_read_input_tokens": 47464,
          "cache_creation_input_tokens": 450,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 450
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

_source line 34 · 2026-05-22T18:49:59.382Z_

<details><summary>↩ Tool result · reported error · `toolu_017zAkUSC9vuj6DcZWM7QPrw`</summary>

```text
Exit code 1
Traceback (most recent call last):
  File "&lt;string>", line 7, in &lt;module>
    if exp.get('exp_id') == 'kl50_global_s123_downstream_v2':
       ^^^^^^^
AttributeError: 'str' object has no attribute 'get'
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a17f603c-5e31-4db1-9006-65f58525988b",
  "isSidechain": false,
  "promptId": "e0126d52-e1d3-4c8c-a4f2-76af8e88bda0",
  "type": "user",
  "uuid": "8de5bf6e-7abf-42ad-80b5-56d5368a3b9e",
  "toolUseResult": "Error: Exit code 1\nTraceback (most recent call last):\n  File \"&lt;string>\", line 7, in &lt;module>\n    if exp.get('exp_id') == 'kl50_global_s123_downstream_v2':\n       ^^^^^^^\nAttributeError: 'str' object has no attribute 'get'",
  "sourceToolAssistantUUID": "a17f603c-5e31-4db1-9006-65f58525988b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/agent_66b8aa9d",
  "sessionId": "062027a5-1c13-4530-a568-995829f28b19",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-22T18:49:59.453Z_

<details open><summary>🔧 Tool call — Read · `toolu_01B1oaCXywVRypiMqQXUdQxm`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/skills/on-experiment-failed.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8de5bf6e-7abf-42ad-80b5-56d5368a3b9e",
  "isSidechain": false,
  "requestId": "req_011CbJ7GZuLMsp6Libqt9maP",
  "type": "assistant",
  "uuid": "ad8bf419-e562-4800-8113-13892bae8b03",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/agent_66b8aa9d",
  "sessionId": "062027a5-1c13-4530-a568-995829f28b19",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011F2yozPVcXY7aPXgWbSsMG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 450,
      "cache_read_input_tokens": 47464,
      "output_tokens": 511,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 450,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 511,
          "cache_read_input_tokens": 47464,
          "cache_creation_input_tokens": 450,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 450
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

_source line 36 · 2026-05-22T18:49:59.453Z_

<details><summary>↩ Tool result · reported error · `toolu_01B1oaCXywVRypiMqQXUdQxm`</summary>

```text
&lt;tool_use_error>Cancelled: parallel tool call Bash(cat /home/ubuntu/.claude-account-3/proje…) errored&lt;/tool_use_error>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ad8bf419-e562-4800-8113-13892bae8b03",
  "isSidechain": false,
  "promptId": "e0126d52-e1d3-4c8c-a4f2-76af8e88bda0",
  "type": "user",
  "uuid": "c036c80e-2e34-43d5-8db2-797699afd43d",
  "toolUseResult": "Cancelled: parallel tool call Bash(cat /home/ubuntu/.claude-account-3/proje…) errored",
  "sourceToolAssistantUUID": "ad8bf419-e562-4800-8113-13892bae8b03",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/agent_66b8aa9d",
  "sessionId": "062027a5-1c13-4530-a568-995829f28b19",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-22T18:50:04.270Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01VoYwZq9ExorPPpwSURiBED`</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-14-projects-distill-sparse-swiglu--claude-sessions-agent-66b8aa9d/062027a5-1c13-4530-a568-995829f28b19/tool-results/mcp-agent-ml-research-read_registry-1779475765817.txt | python3 -c \"\nimport json, sys\ndata = json.load(sys.stdin)\nresult = json.loads(data['result'])\nexps = result['data']['experiments']\nprint('type of exps[0]:', type(exps[0]))\nprint('first 300 chars:', str(exps[0])[:300])\n\"",
  "description": "Check experiment data type"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c036c80e-2e34-43d5-8db2-797699afd43d",
  "isSidechain": false,
  "requestId": "req_011CbJ7H5PsRZjZKhQCwanXR",
  "type": "assistant",
  "uuid": "5612c66e-97bc-4031-9f0e-7838cf603af0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/agent_66b8aa9d",
  "sessionId": "062027a5-1c13-4530-a568-995829f28b19",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016o3VsngRptR1L3fWhX9DmC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 688,
      "cache_read_input_tokens": 47914,
      "output_tokens": 257,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 688,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 257,
          "cache_read_input_tokens": 47914,
          "cache_creation_input_tokens": 688,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 688
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

_source line 38 · 2026-05-22T18:50:04.482Z_

<details><summary>↩ Tool result · reported error · `toolu_01VoYwZq9ExorPPpwSURiBED`</summary>

```text
Exit code 1
Traceback (most recent call last):
  File "&lt;string>", line 6, in &lt;module>
    print('type of exps[0]:', type(exps[0]))
                                   ~~~~^^^
KeyError: 0
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5612c66e-97bc-4031-9f0e-7838cf603af0",
  "isSidechain": false,
  "promptId": "e0126d52-e1d3-4c8c-a4f2-76af8e88bda0",
  "type": "user",
  "uuid": "61412ede-a8dc-42ed-962b-fb7c284a2a2c",
  "toolUseResult": "Error: Exit code 1\nTraceback (most recent call last):\n  File \"&lt;string>\", line 6, in &lt;module>\n    print('type of exps[0]:', type(exps[0]))\n                                   ~~~~^^^\nKeyError: 0",
  "sourceToolAssistantUUID": "5612c66e-97bc-4031-9f0e-7838cf603af0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/agent_66b8aa9d",
  "sessionId": "062027a5-1c13-4530-a568-995829f28b19",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-22T18:50:09.700Z_

<details open><summary>🔧 Tool call — Bash · `toolu_012DLWZQsaxFS1iqBtSqWwqw`</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-14-projects-distill-sparse-swiglu--claude-sessions-agent-66b8aa9d/062027a5-1c13-4530-a568-995829f28b19/tool-results/mcp-agent-ml-research-read_registry-1779475765817.txt | python3 -c \"\nimport json, sys\ndata = json.load(sys.stdin)\nresult = json.loads(data['result'])\nexps = result['data']['experiments']\nprint('type:', type(exps))\nif isinstance(exps, dict):\n    if 'kl50_global_s123_downstream_v2' in exps:\n        print(json.dumps(exps['kl50_global_s123_downstream_v2'], indent=2))\n    else:\n        # search\n        matches = [k for k in exps.keys() if 'kl50_global' in k]\n        print('matches:', matches)\n\"",
  "description": "Find experiment in dict-keyed registry"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "61412ede-a8dc-42ed-962b-fb7c284a2a2c",
  "isSidechain": false,
  "requestId": "req_011CbJ7HRaZT923k6kK4vKWY",
  "type": "assistant",
  "uuid": "1f00beb8-875b-4624-8853-d89709cb0fa7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/agent_66b8aa9d",
  "sessionId": "062027a5-1c13-4530-a568-995829f28b19",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01T93WESBtLNmvA8smqe5koK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 338,
      "cache_read_input_tokens": 48602,
      "output_tokens": 337,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 338,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 337,
          "cache_read_input_tokens": 48602,
          "cache_creation_input_tokens": 338,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 338
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

_source line 40 · 2026-05-22T18:50:09.781Z_

<details><summary>↩ Tool result · `toolu_012DLWZQsaxFS1iqBtSqWwqw`</summary>

```text
type: &lt;class 'dict'>
{
  "status": "DONE",
  "created_at": "2026-05-22T17:42:51.552Z",
  "updated_at": "2026-05-22T18:39:51.918Z",
  "hypothesis": "Re-eval KL 50% global s123 downstream (ARC-c, WG, MMLU, GSM8K) to complete 3-seed data for Table 2. Previous attempt (kl50_global_s123_reeval) failed with EXIT_CODE=1.",
  "parent": "kl50_global_s123_reeval",
  "conclusion": "success",
  "metrics": {
    "arc_challenge_acc_norm": 0.3916,
    "winogrande_acc": 0.6401,
    "mmlu_acc": 0.2908,
    "gsm8k_exact_match": 0.0341
  }
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1f00beb8-875b-4624-8853-d89709cb0fa7",
  "isSidechain": false,
  "promptId": "e0126d52-e1d3-4c8c-a4f2-76af8e88bda0",
  "type": "user",
  "uuid": "f72f7f26-b9c7-4257-b487-f49dca60ce8c",
  "toolUseResult": {
    "stdout": "type: &lt;class 'dict'>\n{\n  \"status\": \"DONE\",\n  \"created_at\": \"2026-05-22T17:42:51.552Z\",\n  \"updated_at\": \"2026-05-22T18:39:51.918Z\",\n  \"hypothesis\": \"Re-eval KL 50% global s123 downstream (ARC-c, WG, MMLU, GSM8K) to complete 3-seed data for Table 2. Previous attempt (kl50_global_s123_reeval) failed with EXIT_CODE=1.\",\n  \"parent\": \"kl50_global_s123_reeval\",\n  \"conclusion\": \"success\",\n  \"metrics\": {\n    \"arc_challenge_acc_norm\": 0.3916,\n    \"winogrande_acc\": 0.6401,\n    \"mmlu_acc\": 0.2908,\n    \"gsm8k_exact_match\": 0.0341\n  }\n}",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "1f00beb8-875b-4624-8853-d89709cb0fa7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/agent_66b8aa9d",
  "sessionId": "062027a5-1c13-4530-a568-995829f28b19",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 41 · 2026-05-22T18:50:30.023Z_

<details><summary>Logged reasoning block</summary>

```text
Wait, the experiment is DONE with conclusion=success! But the CRON said it failed ("Process exited without valid W&B metrics"). Let me check more carefully - maybe the registry was already updated. Let me also look at what's currently happening with this experiment. The CRON message says it failed, but the registry shows success with metrics. This might be a case where the cron detected the process exit but the experiment had already been marked as success by a worker.

Actually, let me re-read the CRON message: "实验进程异常退出（失败），需要你诊断原因。详情: Process exited without valid W&B metrics". 

The registry shows conclusion=success with valid metrics though, which suggests the experiment was already successfully processed by a worker before this cron callback fired. Since reconcile_crons reported zero reconciliations and the updated_at timestamp predates this callback, this looks like a stale cron notification - the experiment had already completed successfully.

Now I'm realizing the cron message about "Process exited without valid W&B metrics" is likely the standard monitoring behavior for eval experiments that don't log to W&B, so the process exiting is expected after completion.

Since the registry already shows the experiment as DONE with success and extracted metrics, this is a false alarm from the cron. I should verify there are no other RUNNING experiments that need attention.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f72f7f26-b9c7-4257-b487-f49dca60ce8c",
  "isSidechain": false,
  "requestId": "req_011CbJ7HpQzHG5hFub8HMcKv",
  "type": "assistant",
  "uuid": "4296d708-6215-4934-a30e-be1e7f903639",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/agent_66b8aa9d",
  "sessionId": "062027a5-1c13-4530-a568-995829f28b19",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01X8v9bmieAnnUUZtHDfvUDt",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 588,
      "cache_read_input_tokens": 48940,
      "output_tokens": 940,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 588,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 940,
          "cache_read_input_tokens": 48940,
          "cache_creation_input_tokens": 588,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 588
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

_source line 42 · 2026-05-22T18:50:33.425Z_

实验 `kl50_global_s123_downstream_v2` registry 已标记为 **DONE/success**（metrics: ARC-c=0.3916, WG=0.6401, MMLU=0.2908, GSM8K=0.0341），updated_at 为 18:39 UTC。

这是一个**误报**：该实验是 lm-eval-harness 下游评估，不走 W&B 日志。进程正常退出后 cron 检测不到 W&B metrics 就触发了失败回调，但 Worker 已经从 log 提取了 metrics 并更新了 registry。

确认无需操作。检查是否还有其他需要处理的事项。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4296d708-6215-4934-a30e-be1e7f903639",
  "isSidechain": false,
  "requestId": "req_011CbJ7HpQzHG5hFub8HMcKv",
  "type": "assistant",
  "uuid": "cb949e39-35aa-4f81-b72d-07458bd0b532",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/agent_66b8aa9d",
  "sessionId": "062027a5-1c13-4530-a568-995829f28b19",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01X8v9bmieAnnUUZtHDfvUDt",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 588,
      "cache_read_input_tokens": 48940,
      "output_tokens": 940,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 588,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 940,
          "cache_read_input_tokens": 48940,
          "cache_creation_input_tokens": 588,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 588
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

_source line 43 · 2026-05-22T18:50:33.886Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01AbMsVptEKgSdmthNf6pep7`</summary>

```json
{
  "project": "distill_sparse_swiglu",
  "filters": {
    "status": "RUNNING"
  }
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cb949e39-35aa-4f81-b72d-07458bd0b532",
  "isSidechain": false,
  "requestId": "req_011CbJ7HpQzHG5hFub8HMcKv",
  "type": "assistant",
  "uuid": "70b79136-5605-4b35-af4b-3d679123c56a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/agent_66b8aa9d",
  "sessionId": "062027a5-1c13-4530-a568-995829f28b19",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01X8v9bmieAnnUUZtHDfvUDt",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 588,
      "cache_read_input_tokens": 48940,
      "output_tokens": 940,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 588,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 940,
          "cache_read_input_tokens": 48940,
          "cache_creation_input_tokens": 588,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 588
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
  "lastPrompt": "[CRON] 实验进程异常退出（失败），需要你诊断原因。 详情: Process exited without valid W&B metrics  - exp_id: kl50_global_s123_downstream_v2 - project: distill_sparse_swiglu - server: westd-34887 - log_path: ~/runs/distill_sp…",
  "leafUuid": "70b79136-5605-4b35-af4b-3d679123c56a",
  "sessionId": "062027a5-1c13-4530-a568-995829f28b19"
}
```

---

### Runtime record

_source line 45_

```json
{
  "type": "ai-title",
  "aiTitle": "Diagnose W&B metrics missing error in experiment",
  "sessionId": "062027a5-1c13-4530-a568-995829f28b19"
}
```

---

### Tool result

_source line 46 · 2026-05-22T18:50:34.783Z_

<details><summary>↩ Tool result · `toolu_01AbMsVptEKgSdmthNf6pep7`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": \"bench_dense\"}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.8801}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "70b79136-5605-4b35-af4b-3d679123c56a",
  "isSidechain": false,
  "promptId": "e0126d52-e1d3-4c8c-a4f2-76af8e88bda0",
  "type": "user",
  "uuid": "0c692a97-8b78-4c84-8952-25faea22fcc0",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {}, \\\"count\\\": 0, \\\"total\\\": 0, \\\"baseline\\\": \\\"bench_dense\\\"}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.8801}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": \"bench_dense\"}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.8801}}"
    }
  },
  "sourceToolAssistantUUID": "70b79136-5605-4b35-af4b-3d679123c56a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/agent_66b8aa9d",
  "sessionId": "062027a5-1c13-4530-a568-995829f28b19",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---
