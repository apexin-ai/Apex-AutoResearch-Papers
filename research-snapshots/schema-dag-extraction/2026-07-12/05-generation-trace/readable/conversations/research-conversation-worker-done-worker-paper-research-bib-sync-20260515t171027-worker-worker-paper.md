# Research conversation: [系统通知 — worker_done:worker_paper_research_bib_sync_20260515T171027]: Worker worker_paper_research_bib_sync_20260515T1710

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction? (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 48
- **Recorded user turns:** 1
- **Tool calls:** 11
- **Original source:** `logs/chats/exported-trajectories/account-1/f59020b4-1c0e-4081-9cb3-293eac3560ff.jsonl`
- **Structured JSON:** [`ae918f3d22ec87d22461.json`](../../sessions/ae/ae918f3d22ec87d22461.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-15T17:15:16.768Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-15T17:15:16.768Z",
  "sessionId": "f59020b4-1c0e-4081-9cb3-293eac3560ff",
  "content": "[系统通知 — worker_done:worker_paper_research_bib_sync_20260515T171027]:\nWorker worker_paper_research_bib_sync_20260515T171027 已完成（status=done），请审查 Agent 的处理结果。"
}
```

---

### Runtime record

_source line 2 · 2026-05-15T17:15:16.773Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-15T17:15:16.773Z",
  "sessionId": "f59020b4-1c0e-4081-9cb3-293eac3560ff"
}
```

---

## Round 1

46 recorded events

### User

_source line 3 · 2026-05-15T17:15:16.852Z_

[系统通知 — worker_done:worker_paper_research_bib_sync_20260515T171027]:
Worker worker_paper_research_bib_sync_20260515T171027 已完成（status=done），请审查 Agent 的处理结果。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "b593ab42-40aa-4651-8f99-a82b6d6b969a",
  "type": "user",
  "uuid": "81d268fa-fb7a-4bca-8382-8948b16485cb",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/reviewer_efaaa6bc",
  "sessionId": "f59020b4-1c0e-4081-9cb3-293eac3560ff",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-15T17:15:16.851Z_

```json
{
  "parentUuid": "81d268fa-fb7a-4bca-8382-8948b16485cb",
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
      "mcp__agent-ml-research__cleanup_pdf_images",
      "mcp__agent-ml-research__compute_coverage_matrix",
      "mcp__agent-ml-research__fetch_wandb_metrics",
      "mcp__agent-ml-research__get_gpu_health",
      "mcp__agent-ml-research__get_project_resource_usage",
      "mcp__agent-ml-research__list_constraints",
      "mcp__agent-ml-research__pdf_to_images",
      "mcp__agent-ml-research__read_experiment_plan_with_status",
      "mcp__agent-ml-research__read_matrix",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__read_registry",
      "mcp__agent-ml-research__read_roadmap",
      "mcp__agent-ml-research__reviewer_post_to_director",
      "mcp__agent-ml-research__ssh_read_only",
      "mcp__agent-ml-research__tail_training_logs"
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
      "mcp__agent-ml-research__cleanup_pdf_images",
      "mcp__agent-ml-research__compute_coverage_matrix",
      "mcp__agent-ml-research__fetch_wandb_metrics",
      "mcp__agent-ml-research__get_gpu_health",
      "mcp__agent-ml-research__get_project_resource_usage",
      "mcp__agent-ml-research__list_constraints",
      "mcp__agent-ml-research__pdf_to_images",
      "mcp__agent-ml-research__read_experiment_plan_with_status",
      "mcp__agent-ml-research__read_matrix",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__read_registry",
      "mcp__agent-ml-research__read_roadmap",
      "mcp__agent-ml-research__reviewer_post_to_director",
      "mcp__agent-ml-research__ssh_read_only",
      "mcp__agent-ml-research__tail_training_logs"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "22930a30-85ec-4274-8026-0a6c0fc787de",
  "timestamp": "2026-05-15T17:15:16.851Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/reviewer_efaaa6bc",
  "sessionId": "f59020b4-1c0e-4081-9cb3-293eac3560ff",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-15T17:15:16.851Z_

```json
{
  "parentUuid": "22930a30-85ec-4274-8026-0a6c0fc787de",
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
  "uuid": "1692f99a-6dd7-4977-a486-ec249e35520f",
  "timestamp": "2026-05-15T17:15:16.851Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/reviewer_efaaa6bc",
  "sessionId": "f59020b4-1c0e-4081-9cb3-293eac3560ff",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6 · 2026-05-15T17:15:16.851Z_

```json
{
  "parentUuid": "1692f99a-6dd7-4977-a486-ec249e35520f",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "3a2f2414-21fb-4f80-b0a3-49da842c3833",
  "timestamp": "2026-05-15T17:15:16.851Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/reviewer_efaaa6bc",
  "sessionId": "f59020b4-1c0e-4081-9cb3-293eac3560ff",
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
  "aiTitle": "Review paper research bibliography sync results",
  "sessionId": "f59020b4-1c0e-4081-9cb3-293eac3560ff"
}
```

---

### Assistant

_source line 8 · 2026-05-15T17:15:23.443Z_

<details><summary>Logged reasoning block</summary>

```text
Worker完成了一个关于paper research bib sync的任务。我需要审查这个worker的处理结果。让我先查看registry和相关文件来了解情况。
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3a2f2414-21fb-4f80-b0a3-49da842c3833",
  "isSidechain": false,
  "requestId": "req_011Cb4jPm2QCj8auZ12PZ5bj",
  "type": "assistant",
  "uuid": "2e690284-dd84-40ac-b2a5-ac04d057b364",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/reviewer_efaaa6bc",
  "sessionId": "f59020b4-1c0e-4081-9cb3-293eac3560ff",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CfeP9nA1swhNBqVvaVhah2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 18849,
      "cache_read_input_tokens": 11841,
      "output_tokens": 213,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 18849,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 213,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 18849,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 18849
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

_source line 9 · 2026-05-15T17:15:23.903Z_

开始审查 worker_paper_research_bib_sync 的处理结果。先读取 registry 和相关文件。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2e690284-dd84-40ac-b2a5-ac04d057b364",
  "isSidechain": false,
  "requestId": "req_011Cb4jPm2QCj8auZ12PZ5bj",
  "type": "assistant",
  "uuid": "fbfdd3c7-4f3e-4e03-ab18-e7c7eab09029",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/reviewer_efaaa6bc",
  "sessionId": "f59020b4-1c0e-4081-9cb3-293eac3560ff",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CfeP9nA1swhNBqVvaVhah2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 18849,
      "cache_read_input_tokens": 11841,
      "output_tokens": 213,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 18849,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 213,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 18849,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 18849
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

_source line 10 · 2026-05-15T17:15:24.869Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01Ao75CQF5YmJP7m6AETQqCH`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__read_roadmap",
  "max_results": 3
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fbfdd3c7-4f3e-4e03-ab18-e7c7eab09029",
  "isSidechain": false,
  "requestId": "req_011Cb4jPm2QCj8auZ12PZ5bj",
  "type": "assistant",
  "uuid": "e0046788-f436-43f6-95bc-b95c274303a9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/reviewer_efaaa6bc",
  "sessionId": "f59020b4-1c0e-4081-9cb3-293eac3560ff",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CfeP9nA1swhNBqVvaVhah2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 18849,
      "cache_read_input_tokens": 11841,
      "output_tokens": 213,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 18849,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 213,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 18849,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 18849
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

_source line 11 · 2026-05-15T17:15:24.875Z_

<details><summary>↩ Tool result · `toolu_01Ao75CQF5YmJP7m6AETQqCH`</summary>

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
  "parentUuid": "e0046788-f436-43f6-95bc-b95c274303a9",
  "isSidechain": false,
  "promptId": "b593ab42-40aa-4651-8f99-a82b6d6b969a",
  "type": "user",
  "uuid": "ef1d70f0-ac62-4853-9420-8f33d31fae93",
  "toolUseResult": {
    "matches": [
      "mcp__agent-ml-research__read_registry",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__read_roadmap"
    ],
    "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__read_roadmap",
    "total_deferred_tools": 34
  },
  "sourceToolAssistantUUID": "e0046788-f436-43f6-95bc-b95c274303a9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/reviewer_efaaa6bc",
  "sessionId": "f59020b4-1c0e-4081-9cb3-293eac3560ff",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-15T17:15:27.827Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01BfHWX8hR1dEmNwBTmP6qDD`</summary>

```json
{
  "project": "schema-dag-extraction",
  "limit": 10,
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
  "parentUuid": "ef1d70f0-ac62-4853-9420-8f33d31fae93",
  "isSidechain": false,
  "requestId": "req_011Cb4jQMLA5Q7jjcXuhvTJ8",
  "type": "assistant",
  "uuid": "f51bc04c-e450-4422-bc6a-6d133f4765a4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/reviewer_efaaa6bc",
  "sessionId": "f59020b4-1c0e-4081-9cb3-293eac3560ff",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GPPHHwJoc7aeRBjYvkbjUa",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 995,
      "cache_read_input_tokens": 30690,
      "output_tokens": 173,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 995,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 173,
          "cache_read_input_tokens": 30690,
          "cache_creation_input_tokens": 995,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 995
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

_source line 13 · 2026-05-15T17:15:27.949Z_

<details><summary>↩ Tool result · `toolu_01BfHWX8hR1dEmNwBTmP6qDD`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {\"exp012_llama_8b_r2\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-15T17:05:44.959Z\", \"updated_at\": \"2026-05-15T17:13:40.989Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/schema-dag-extraction && export FLASHINFER_DISABLE_VERSION_CHECK=1 && export HF_HOME=/root/autodl-tmp/.hf_cache && bash scripts/run_exp012_llama8b.sh\\\"\", \"server\": \"cqa1-38874\", \"gpu\": [\"cuda:0\"], \"pid\": \"302875\", \"log_path\": \"~/runs/schema-dag-extraction/exp012_llama_8b_r2.log\", \"submitted_at\": \"2026-05-15T17:09:16.451Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"notes\": \"SIGKILL EXIT_CODE=137 — 系统级 OOM kill，与 r3 相同症状。vLLM 初始化前被杀，GPU VRAM 0MiB。\", \"conclusion\": \"failed\"}, \"exp012_llama_8b_r3\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-15T17:09:36.668Z\", \"updated_at\": \"2026-05-15T17:13:40.158Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export FLASHINFER_DISABLE_VERSION_CHECK=1 && cd /root/schema-dag-extraction && bash scripts/run_exp012_llama8b.sh\\\"\", \"server\": \"cqa1-38874\", \"gpu\": [\"cuda:0\"], \"pid\": \"303055\", \"log_path\": \"~/runs/schema-dag-extraction/exp012_llama_8b_r3.log\", \"submitted_at\": \"2026-05-15T17:09:36.582Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"conclusion\": \"failed\", \"notes\": \"SIGKILL EXIT_CODE=137 — 系统级 OOM kill，vLLM 初始化前被杀，GPU VRAM 始终 0MiB。连续两次（r2+r3）相同症状。非 GPU OOM，是 host RAM 不足。\"}, \"exp_fewrel_40rel_r3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T16:57:11.672Z\", \"updated_at\": \"2026-05-15T17:11:07.041Z\", \"spec\": {\"command\": \"python3 src/run_fewrel_40rel.py --stage extract --mode exp1 + exp2\", \"server\": \"cqa1-38874\", \"gpu\": [\"cuda:0\"], \"pid\": \"300803\", \"log_path\": \"~/runs/schema-dag-extraction/exp_fewrel_40rel_r3.log\", \"submitted_at\": \"2026-05-15T16:57:11.592Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"FewRel 40-rel subset (preprocess_exp1.json)\", \"data_count\": 960, \"model_name\": \"Qwen3-32B-FP8\", \"seed\": 42, \"checkpoint_source\": \"Qwen/Qwen3-32B-FP8 at /root/autodl-tmp/.hf_cache/qwen3-32b-fp8/\", \"eval_data\": \"FewRel val set, 40-rel, 960 samples, 105 batches, count curve + BCS controlled\", \"wall_clock_seconds\": 731.6, \"gpu_hours\": 0.2}, \"hypothesis\": \"FewRel 40-rel 中间点 scaling curve: 验证 count↑→accuracy↓ 在 40-rel 规模下的 degradation 幅度，补全 16-rel 到 80-rel 之间的 scaling 趋势\", \"parent\": \"exp_fewrel_40rel_r2\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-15T17:09:23.232Z\", \"notes\": \"EXIT_CODE=0 但只做了 exp2 预处理，无任何 predictions 产出。vLLM 参数与成功的 run_fewrel_formal.py 一致，r2 OOM 系其他 GPU 进程占显存所致。已修复 gpu_memory_utilization 0.95→0.85，脚本就绪待 exp012 完成后重跑。\"}, \"exp_fewrel_40rel_r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T16:48:22.142Z\", \"updated_at\": \"2026-05-15T16:56:52.602Z\", \"hypothesis\": \"FewRel 40-rel 中间点 scaling curve: 验证 count↑→accuracy↓ 在 40-rel 规模下的 degradation 幅度，补全 16-rel 到 80-rel 之间的 scaling 趋势\", \"parent\": \"exp_fewrel_40rel\", \"spec\": {\"command\": \"bash scripts/run_fewrel_40rel.sh || python run_fewrel_40rel.py\", \"server\": \"cqa1-38874\", \"gpu\": [\"cuda:0\"], \"pid\": \"299625\", \"log_path\": \"~/runs/schema-dag-extraction/exp_fewrel_40rel_r2.log\", \"submitted_at\": \"2026-05-15T16:50:29.191Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"FewRel 40-rel subset\", \"data_count\": 800, \"model_name\": \"Qwen3-32B-FP8\", \"seed\": 42, \"checkpoint_source\": \"Qwen/Qwen3-32B-FP8 (pre-downloaded on server)\", \"eval_data\": \"FewRel val set, 40-rel subset, count curve + BCS controlled\", \"wall_clock_seconds\": 377.8, \"gpu_hours\": 0.1}, \"conclusion\": \"failed\", \"completed_at\": \"2026-05-15T16:56:46.973Z\", \"notes\": \"vLLM EngineCore OOM during Qwen3-32B-FP8 initialization. SIGKILL at shard 1/7 (14%). Missing FLASHINFER_DISABLE_VERSION_CHECK=1. Creating r3 with correct env vars.\"}, \"exp012_llama_fewnerd_r4\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T16:24:15.927Z\", \"updated_at\": \"2026-05-15T16:49:17.831Z\", \"spec\": {\"command\": \"bash scripts/run_exp012_llama8b.sh\", \"server\": \"cqa1-38874\", \"gpu\": [\"cuda:0\"], \"pid\": \"294443\", \"log_path\": \"~/runs/schema-dag-extraction/exp012_llama_fewnerd_r4.log\", \"submitted_at\": \"2026-05-15T16:24:15.825Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"LLaMA-3.1-8B-Instruct\", \"quantization\": \"none (BF16)\", \"fix_applied\": \"switched from 70B FP8 to 8B BF16 to avoid FlashInfer FP8 kernel JIT failure on Blackwell SM120\", \"data_path\": \"/root/schema-dag-extraction/data/parquet/test.parquet\", \"data_count\": 1000, \"seed\": 42, \"hypothesis\": \"Multi-model validation: LLaMA-3.1-8B-Instruct (BF16) replicates confusability effect on Few-NERD\", \"dataset\": \"Few-NERD\", \"plan_id\": \"exp-012\", \"checkpoint_source\": \"meta-llama/Llama-3.1-8B-Instruct (ModelScope download)\", \"eval_data\": \"Few-NERD test.parquet 1000 samples\", \"wall_clock_seconds\": 1231.4, \"gpu_hours\": 0.34}, \"hypothesis\": \"LLaMA model replicates confusability-driven type confusion pattern observed with Qwen, validating model-independence of the phenomenon\", \"parent\": \"exp012_llama_fewnerd_r3\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-15T16:44:47.235Z\", \"notes\": \"LLaMA-3.1-8B zero predictions on all 94 batches, gen_tokens=2, model outputs empty JSON array. Structured JSON output constraint 下模型无法执行 NER。PID 297093 (rogue vLLM exp2 进程) 已派 Worker kill。\"}, \"exp012_llama_8b_fewnerd\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T16:26:10.725Z\", \"updated_at\": \"2026-05-15T16:41:15.276Z\", \"spec\": {\"hypothesis\": \"Multi-model validation: LLaMA-3.1-8B-Instruct (BF16) replicates confusability effect on Few-NERD — count curve + BCS-controlled, proving effect holds across model families and sizes\", \"dataset\": \"Few-NERD\", \"model\": \"LLaMA-3.1-8B-Instruct\", \"data_path\": \"/root/schema-dag-extraction/data/parquet/test.parquet\", \"data_count\": 1000, \"model_name\": \"LLaMA-3.1-8B-Instruct\", \"seed\": 42, \"plan_id\": \"exp-012\", \"parent\": \"exp012_llama_fewnerd_r3\", \"server\": \"cqa1-38874\", \"command\": \"bash scripts/run_exp012_llama_8b.sh\", \"pid\": 295200, \"log_path\": \"/root/schema-dag-extraction/logs/exp012_llama_8b.log\", \"checkpoint_path\": \"artifacts/exp012_llama_8b/\"}, \"conclusion\": \"failed\", \"notes\": \"Dead entry: PID 295200 was OOM-killed when exp012_llama_fewnerd_r4 (PID 294443) took cuda:0. Superseded by r4.\", \"completed_at\": \"2026-05-15T16:41:15.276Z\"}, \"exp012_llama_8b\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-15T16:06:32.024Z\", \"updated_at\": \"2026-05-15T16:41:03.756Z\", \"spec\": {\"hypothesis\": \"Multi-model validation: LLaMA-3.1-8B replicates confusability effect on Few-NERD (count curve + BCS-controlled)\", \"dataset\": \"Few-NERD\", \"data_path\": \"/root/schema-dag-extraction/data/parquet/test.parquet\", \"data_count\": 1000, \"plan_id\": \"exp-012\", \"parent\": \"exp012_llama_fewnerd_r3\", \"model_name\": \"llama-3.1-8b-instruct\", \"server\": \"cqa1-38874\"}, \"notes\": \"GPU OOM: conflicted with r4 (PID 294443) on cuda:0. PID 295200 killed. Duplicate entry, superseded by exp012_llama_fewnerd_r4.\", \"conclusion\": \"killed\"}, \"exp_fewrel_40rel\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T16:07:32.483Z\", \"updated_at\": \"2026-05-15T16:30:30.024Z\", \"spec\": {\"hypothesis\": \"FewRel 40-rel intermediate point: confirms monotonic scaling between 16-rel and 80-rel for count curve degradation and BCS effect\", \"dataset\": \"FewRel (80 relations pool, max count 40)\", \"model\": \"Qwen3-32B-FP8\", \"data_path\": \"/root/schema-dag-extraction/data/fewrel_parquet/\", \"data_count\": \"full FewRel 80 rel pool, batches capped at 40\", \"model_name\": \"Qwen3-32B-FP8\", \"seed\": 42, \"plan_id\": \"exp-012\", \"parent\": \"exp_fewrel_formal_80rel\", \"command\": \"bash scripts/run_fewrel_40rel.sh\", \"server\": \"cqa1-38874\", \"checkpoint_source\": \"Qwen3-32B-FP8 (same as parent)\", \"eval_data\": \"FewRel 80-rel pool, 1000 balanced samples\"}, \"conclusion\": \"failed\", \"notes\": \"Process killed, results not saved (no per-batch incremental saving). Need to rerun with incremental save after exp012_llama_fewnerd_r4 completes.\", \"completed_at\": \"2026-05-15T16:30:30.024Z\"}, \"exp012_llama_awq\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-15T16:08:55.256Z\", \"updated_at\": \"2026-05-15T16:27:38.824Z\", \"spec\": {\"hypothesis\": \"Multi-model validation: LLaMA-3.1-70B-AWQ replicates confusability effect on Few-NERD (count curve + BCS-controlled)\", \"dataset\": \"Few-NERD\", \"data_path\": \"/root/schema-dag-extraction/data/parquet/test.parquet\", \"data_count\": 1000, \"plan_id\": \"exp-012\", \"parent\": \"exp012_llama_fewnerd_r3\", \"model_name\": \"llama-3.1-70b-instruct-awq-int4\", \"server\": \"cqa1-38874\"}, \"notes\": \"Abandoned: AWQ download failed due to disk space (2.6GB remaining, needed 9.2GB). Superseded by exp012_llama_fewnerd_r4 (8B BF16).\", \"conclusion\": \"killed\"}, \"exp012_llama_fewnerd_r3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T15:53:18.937Z\", \"updated_at\": \"2026-05-15T16:25:46.495Z\", \"spec\": {\"command\": \"bash scripts/run_exp012_llama.sh\", \"server\": \"cqa1-38874\", \"data_path\": \"/root/schema-dag-extraction/data/parquet/test.parquet\", \"data_count\": 1000, \"model_name\": \"LLaMA-3.3-70B-Instruct-FP8\", \"seed\": 42, \"hypothesis\": \"Multi-model validation: LLaMA-70B replicates count-degradation and BCS-confusion patterns found with Qwen3-32B on Few-NERD\", \"dataset\": \"Few-NERD\", \"model_path\": \"/root/autodl-tmp/.hf_cache/llama-3.3-70b-instruct-fp8/\", \"plan_id\": \"exp-012\", \"claim\": \"1+2\", \"gpu\": [\"cuda:0\"], \"log_path\": \"/tmp/exp012_r3.log\"}, \"notes\": \"vLLM engine core initialization failed — flashinfer JIT requires CUDA 12.9 but server has nvcc 12.8, SM120 Blackwell FP8 incompatible. Same root cause as r1/r2. Three consecutive failures, FP8 path abandoned.\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-15T16:25:46.495Z\"}}, \"count\": 10, \"total\": 27, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.1073}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f51bc04c-e450-4422-bc6a-6d133f4765a4",
  "isSidechain": false,
  "promptId": "b593ab42-40aa-4651-8f99-a82b6d6b969a",
  "type": "user",
  "uuid": "c60307c2-1593-4790-b665-d58078c00164",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {\\\"exp012_llama_8b_r2\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-15T17:05:44.959Z\\\", \\\"updated_at\\\": \\\"2026-05-15T17:13:40.989Z\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/schema-dag-extraction && export FLASHINFER_DISABLE_VERSION_CHECK=1 && export HF_HOME=/root/autodl-tmp/.hf_cache && bash scripts/run_exp012_llama8b.sh\\\\\\\"\\\", \\\"server\\\": \\\"cqa1-38874\\\", \\\"gpu\\\": [\\\"cuda:0\\\"], \\\"pid\\\": \\\"302875\\\", \\\"log_path\\\": \\\"~/runs/schema-dag-extraction/exp012_llama_8b_r2.log\\\", \\\"submitted_at\\\": \\\"2026-05-15T17:09:16.451Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\"}, \\\"notes\\\": \\\"SIGKILL EXIT_CODE=137 — 系统级 OOM kill，与 r3 相同症状。vLLM 初始化前被杀，GPU VRAM 0MiB。\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"exp012_llama_8b_r3\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-15T17:09:36.668Z\\\", \\\"updated_at\\\": \\\"2026-05-15T17:13:40.158Z\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export FLASHINFER_DISABLE_VERSION_CHECK=1 && cd /root/schema-dag-extraction && bash scripts/run_exp012_llama8b.sh\\\\\\\"\\\", \\\"server\\\": \\\"cqa1-38874\\\", \\\"gpu\\\": [\\\"cuda:0\\\"], \\\"pid\\\": \\\"303055\\\", \\\"log_path\\\": \\\"~/runs/schema-dag-extraction/exp012_llama_8b_r3.log\\\", \\\"submitted_at\\\": \\\"2026-05-15T17:09:36.582Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\"}, \\\"conclusion\\\": \\\"failed\\\", \\\"notes\\\": \\\"SIGKILL EXIT_CODE=137 — 系统级 OOM kill，vLLM 初始化前被杀，GPU VRAM 始终 0MiB。连续两次（r2+r3）相同症状。非 GPU OOM，是 host RAM 不足。\\\"}, \\\"exp_fewrel_40rel_r3\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-15T16:57:11.672Z\\\", \\\"updated_at\\\": \\\"2026-05-15T17:11:07.041Z\\\", \\\"spec\\\": {\\\"command\\\": \\\"python3 src/run_fewrel_40rel.py --stage extract --mode exp1 + exp2\\\", \\\"server\\\": \\\"cqa1-38874\\\", \\\"gpu\\\": [\\\"cuda:0\\\"], \\\"pid\\\": \\\"300803\\\", \\\"log_path\\\": \\\"~/runs/schema-dag-extraction/exp_fewrel_40rel_r3.log\\\", \\\"submitted_at\\\": \\\"2026-05-15T16:57:11.592Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"data_path\\\": \\\"FewRel 40-rel subset (preprocess_exp1.json)\\\", \\\"data_count\\\": 960, \\\"model_name\\\": \\\"Qwen3-32B-FP8\\\", \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"Qwen/Qwen3-32B-FP8 at /root/autodl-tmp/.hf_cache/qwen3-32b-fp8/\\\", \\\"eval_data\\\": \\\"FewRel val set, 40-rel, 960 samples, 105 batches, count curve + BCS controlled\\\", \\\"wall_clock_seconds\\\": 731.6, \\\"gpu_hours\\\": 0.2}, \\\"hypothesis\\\": \\\"FewRel 40-rel 中间点 scaling curve: 验证 count↑→accuracy↓ 在 40-rel 规模下的 degradation 幅度，补全 16-rel 到 80-rel 之间的 scaling 趋势\\\", \\\"parent\\\": \\\"exp_fewrel_40rel_r2\\\", \\\"conclusion\\\": \\\"failed\\\", \\\"completed_at\\\": \\\"2026-05-15T17:09:23.232Z\\\", \\\"notes\\\": \\\"EXIT_CODE=0 但只做了 exp2 预处理，无任何 predictions 产出。vLLM 参数与成功的 run_fewrel_formal.py 一致，r2 OOM 系其他 GPU 进程占显存所致。已修复 gpu_memory_utilization 0.95→0.85，脚本就绪待 exp012 完成后重跑。\\\"}, \\\"exp_fewrel_40rel_r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-15T16:48:22.142Z\\\", \\\"updated_at\\\": \\\"2026-05-15T16:56:52.602Z\\\", \\\"hypothesis\\\": \\\"FewRel 40-rel 中间点 scaling curve: 验证 count↑→accuracy↓ 在 40-rel 规模下的 degradation 幅度，补全 16-rel 到 80-rel 之间的 scaling 趋势\\\", \\\"parent\\\": \\\"exp_fewrel_40rel\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash scripts/run_fewrel_40rel.sh || python run_fewrel_40rel.py\\\", \\\"server\\\": \\\"cqa1-38874\\\", \\\"gpu\\\": [\\\"cuda:0\\\"], \\\"pid\\\": \\\"299625\\\", \\\"log_path\\\": \\\"~/runs/schema-dag-extraction/exp_fewrel_40rel_r2.log\\\", \\\"submitted_at\\\": \\\"2026-05-15T16:50:29.191Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"data_path\\\": \\\"FewRel 40-rel subset\\\", \\\"data_count\\\": 800, \\\"model_name\\\": \\\"Qwen3-32B-FP8\\\", \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"Qwen/Qwen3-32B-FP8 (pre-downloaded on server)\\\", \\\"eval_data\\\": \\\"FewRel val set, 40-rel subset, count curve + BCS controlled\\\", \\\"wall_clock_seconds\\\": 377.8, \\\"gpu_hours\\\": 0.1}, \\\"conclusion\\\": \\\"failed\\\", \\\"completed_at\\\": \\\"2026-05-15T16:56:46.973Z\\\", \\\"notes\\\": \\\"vLLM EngineCore OOM during Qwen3-32B-FP8 initialization. SIGKILL at shard 1/7 (14%). Missing FLASHINFER_DISABLE_VERSION_CHECK=1. Creating r3 with correct env vars.\\\"}, \\\"exp012_llama_fewnerd_r4\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-15T16:24:15.927Z\\\", \\\"updated_at\\\": \\\"2026-05-15T16:49:17.831Z\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash scripts/run_exp012_llama8b.sh\\\", \\\"server\\\": \\\"cqa1-38874\\\", \\\"gpu\\\": [\\\"cuda:0\\\"], \\\"pid\\\": \\\"294443\\\", \\\"log_path\\\": \\\"~/runs/schema-dag-extraction/exp012_llama_fewnerd_r4.log\\\", \\\"submitted_at\\\": \\\"2026-05-15T16:24:15.825Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"model_name\\\": \\\"LLaMA-3.1-8B-Instruct\\\", \\\"quantization\\\": \\\"none (BF16)\\\", \\\"fix_applied\\\": \\\"switched from 70B FP8 to 8B BF16 to avoid FlashInfer FP8 kernel JIT failure on Blackwell SM120\\\", \\\"data_path\\\": \\\"/root/schema-dag-extraction/data/parquet/test.parquet\\\", \\\"data_count\\\": 1000, \\\"seed\\\": 42, \\\"hypothesis\\\": \\\"Multi-model validation: LLaMA-3.1-8B-Instruct (BF16) replicates confusability effect on Few-NERD\\\", \\\"dataset\\\": \\\"Few-NERD\\\", \\\"plan_id\\\": \\\"exp-012\\\", \\\"checkpoint_source\\\": \\\"meta-llama/Llama-3.1-8B-Instruct (ModelScope download)\\\", \\\"eval_data\\\": \\\"Few-NERD test.parquet 1000 samples\\\", \\\"wall_clock_seconds\\\": 1231.4, \\\"gpu_hours\\\": 0.34}, \\\"hypothesis\\\": \\\"LLaMA model replicates confusability-driven type confusion pattern observed with Qwen, validating model-independence of the phenomenon\\\", \\\"parent\\\": \\\"exp012_llama_fewnerd_r3\\\", \\\"conclusion\\\": \\\"failed\\\", \\\"completed_at\\\": \\\"2026-05-15T16:44:47.235Z\\\", \\\"notes\\\": \\\"LLaMA-3.1-8B zero predictions on all 94 batches, gen_tokens=2, model outputs empty JSON array. Structured JSON output constraint 下模型无法执行 NER。PID 297093 (rogue vLLM exp2 进程) 已派 Worker kill。\\\"}, \\\"exp012_llama_8b_fewnerd\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-15T16:26:10.725Z\\\", \\\"updated_at\\\": \\\"2026-05-15T16:41:15.276Z\\\", \\\"spec\\\": {\\\"hypothesis\\\": \\\"Multi-model validation: LLaMA-3.1-8B-Instruct (BF16) replicates confusability effect on Few-NERD — count curve + BCS-controlled, proving effect holds across model families and sizes\\\", \\\"dataset\\\": \\\"Few-NERD\\\", \\\"model\\\": \\\"LLaMA-3.1-8B-Instruct\\\", \\\"data_path\\\": \\\"/root/schema-dag-extraction/data/parquet/test.parquet\\\", \\\"data_count\\\": 1000, \\\"model_name\\\": \\\"LLaMA-3.1-8B-Instruct\\\", \\\"seed\\\": 42, \\\"plan_id\\\": \\\"exp-012\\\", \\\"parent\\\": \\\"exp012_llama_fewnerd_r3\\\", \\\"server\\\": \\\"cqa1-38874\\\", \\\"command\\\": \\\"bash scripts/run_exp012_llama_8b.sh\\\", \\\"pid\\\": 295200, \\\"log_path\\\": \\\"/root/schema-dag-extraction/logs/exp012_llama_8b.log\\\", \\\"checkpoint_path\\\": \\\"artifacts/exp012_llama_8b/\\\"}, \\\"conclusion\\\": \\\"failed\\\", \\\"notes\\\": \\\"Dead entry: PID 295200 was OOM-killed when exp012_llama_fewnerd_r4 (PID 294443) took cuda:0. Superseded by r4.\\\", \\\"completed_at\\\": \\\"2026-05-15T16:41:15.276Z\\\"}, \\\"exp012_llama_8b\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-15T16:06:32.024Z\\\", \\\"updated_at\\\": \\\"2026-05-15T16:41:03.756Z\\\", \\\"spec\\\": {\\\"hypothesis\\\": \\\"Multi-model validation: LLaMA-3.1-8B replicates confusability effect on Few-NERD (count curve + BCS-controlled)\\\", \\\"dataset\\\": \\\"Few-NERD\\\", \\\"data_path\\\": \\\"/root/schema-dag-extraction/data/parquet/test.parquet\\\", \\\"data_count\\\": 1000, \\\"plan_id\\\": \\\"exp-012\\\", \\\"parent\\\": \\\"exp012_llama_fewnerd_r3\\\", \\\"model_name\\\": \\\"llama-3.1-8b-instruct\\\", \\\"server\\\": \\\"cqa1-38874\\\"}, \\\"notes\\\": \\\"GPU OOM: conflicted with r4 (PID 294443) on cuda:0. PID 295200 killed. Duplicate entry, superseded by exp012_llama_fewnerd_r4.\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"exp_fewrel_40rel\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-15T16:07:32.483Z\\\", \\\"updated_at\\\": \\\"2026-05-15T16:30:30.024Z\\\", \\\"spec\\\": {\\\"hypothesis\\\": \\\"FewRel 40-rel intermediate point: confirms monotonic scaling between 16-rel and 80-rel for count curve degradation and BCS effect\\\", \\\"dataset\\\": \\\"FewRel (80 relations pool, max count 40)\\\", \\\"model\\\": \\\"Qwen3-32B-FP8\\\", \\\"data_path\\\": \\\"/root/schema-dag-extraction/data/fewrel_parquet/\\\", \\\"data_count\\\": \\\"full FewRel 80 rel pool, batches capped at 40\\\", \\\"model_name\\\": \\\"Qwen3-32B-FP8\\\", \\\"seed\\\": 42, \\\"plan_id\\\": \\\"exp-012\\\", \\\"parent\\\": \\\"exp_fewrel_formal_80rel\\\", \\\"command\\\": \\\"bash scripts/run_fewrel_40rel.sh\\\", \\\"server\\\": \\\"cqa1-38874\\\", \\\"checkpoint_source\\\": \\\"Qwen3-32B-FP8 (same as parent)\\\", \\\"eval_data\\\": \\\"FewRel 80-rel pool, 1000 balanced samples\\\"}, \\\"conclusion\\\": \\\"failed\\\", \\\"notes\\\": \\\"Process killed, results not saved (no per-batch incremental saving). Need to rerun with incremental save after exp012_llama_fewnerd_r4 completes.\\\", \\\"completed_at\\\": \\\"2026-05-15T16:30:30.024Z\\\"}, \\\"exp012_llama_awq\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-15T16:08:55.256Z\\\", \\\"updated_at\\\": \\\"2026-05-15T16:27:38.824Z\\\", \\\"spec\\\": {\\\"hypothesis\\\": \\\"Multi-model validation: LLaMA-3.1-70B-AWQ replicates confusability effect on Few-NERD (count curve + BCS-controlled)\\\", \\\"dataset\\\": \\\"Few-NERD\\\", \\\"data_path\\\": \\\"/root/schema-dag-extraction/data/parquet/test.parquet\\\", \\\"data_count\\\": 1000, \\\"plan_id\\\": \\\"exp-012\\\", \\\"parent\\\": \\\"exp012_llama_fewnerd_r3\\\", \\\"model_name\\\": \\\"llama-3.1-70b-instruct-awq-int4\\\", \\\"server\\\": \\\"cqa1-38874\\\"}, \\\"notes\\\": \\\"Abandoned: AWQ download failed due to disk space (2.6GB remaining, needed 9.2GB). Superseded by exp012_llama_fewnerd_r4 (8B BF16).\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"exp012_llama_fewnerd_r3\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-15T15:53:18.937Z\\\", \\\"updated_at\\\": \\\"2026-05-15T16:25:46.495Z\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash scripts/run_exp012_llama.sh\\\", \\\"server\\\": \\\"cqa1-38874\\\", \\\"data_path\\\": \\\"/root/schema-dag-extraction/data/parquet/test.parquet\\\", \\\"data_count\\\": 1000, \\\"model_name\\\": \\\"LLaMA-3.3-70B-Instruct-FP8\\\", \\\"seed\\\": 42, \\\"hypothesis\\\": \\\"Multi-model validation: LLaMA-70B replicates count-degradation and BCS-confusion patterns found with Qwen3-32B on Few-NERD\\\", \\\"dataset\\\": \\\"Few-NERD\\\", \\\"model_path\\\": \\\"/root/autodl-tmp/.hf_cache/llama-3.3-70b-instruct-fp8/\\\", \\\"plan_id\\\": \\\"exp-012\\\", \\\"claim\\\": \\\"1+2\\\", \\\"gpu\\\": [\\\"cuda:0\\\"], \\\"log_path\\\": \\\"/tmp/exp012_r3.log\\\"}, \\\"notes\\\": \\\"vLLM engine core initialization failed — flashinfer JIT requires CUDA 12.9 but server has nvcc 12.8, SM120 Blackwell FP8 incompatible. Same root cause as r1/r2. Three consecutive failures, FP8 path abandoned.\\\", \\\"conclusion\\\": \\\"failed\\\", \\\"completed_at\\\": \\\"2026-05-15T16:25:46.495Z\\\"}}, \\\"count\\\": 10, \\\"total\\\": 27, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.1073}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {\"exp012_llama_8b_r2\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-15T17:05:44.959Z\", \"updated_at\": \"2026-05-15T17:13:40.989Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/schema-dag-extraction && export FLASHINFER_DISABLE_VERSION_CHECK=1 && export HF_HOME=/root/autodl-tmp/.hf_cache && bash scripts/run_exp012_llama8b.sh\\\"\", \"server\": \"cqa1-38874\", \"gpu\": [\"cuda:0\"], \"pid\": \"302875\", \"log_path\": \"~/runs/schema-dag-extraction/exp012_llama_8b_r2.log\", \"submitted_at\": \"2026-05-15T17:09:16.451Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"notes\": \"SIGKILL EXIT_CODE=137 — 系统级 OOM kill，与 r3 相同症状。vLLM 初始化前被杀，GPU VRAM 0MiB。\", \"conclusion\": \"failed\"}, \"exp012_llama_8b_r3\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-15T17:09:36.668Z\", \"updated_at\": \"2026-05-15T17:13:40.158Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export FLASHINFER_DISABLE_VERSION_CHECK=1 && cd /root/schema-dag-extraction && bash scripts/run_exp012_llama8b.sh\\\"\", \"server\": \"cqa1-38874\", \"gpu\": [\"cuda:0\"], \"pid\": \"303055\", \"log_path\": \"~/runs/schema-dag-extraction/exp012_llama_8b_r3.log\", \"submitted_at\": \"2026-05-15T17:09:36.582Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"conclusion\": \"failed\", \"notes\": \"SIGKILL EXIT_CODE=137 — 系统级 OOM kill，vLLM 初始化前被杀，GPU VRAM 始终 0MiB。连续两次（r2+r3）相同症状。非 GPU OOM，是 host RAM 不足。\"}, \"exp_fewrel_40rel_r3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T16:57:11.672Z\", \"updated_at\": \"2026-05-15T17:11:07.041Z\", \"spec\": {\"command\": \"python3 src/run_fewrel_40rel.py --stage extract --mode exp1 + exp2\", \"server\": \"cqa1-38874\", \"gpu\": [\"cuda:0\"], \"pid\": \"300803\", \"log_path\": \"~/runs/schema-dag-extraction/exp_fewrel_40rel_r3.log\", \"submitted_at\": \"2026-05-15T16:57:11.592Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"FewRel 40-rel subset (preprocess_exp1.json)\", \"data_count\": 960, \"model_name\": \"Qwen3-32B-FP8\", \"seed\": 42, \"checkpoint_source\": \"Qwen/Qwen3-32B-FP8 at /root/autodl-tmp/.hf_cache/qwen3-32b-fp8/\", \"eval_data\": \"FewRel val set, 40-rel, 960 samples, 105 batches, count curve + BCS controlled\", \"wall_clock_seconds\": 731.6, \"gpu_hours\": 0.2}, \"hypothesis\": \"FewRel 40-rel 中间点 scaling curve: 验证 count↑→accuracy↓ 在 40-rel 规模下的 degradation 幅度，补全 16-rel 到 80-rel 之间的 scaling 趋势\", \"parent\": \"exp_fewrel_40rel_r2\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-15T17:09:23.232Z\", \"notes\": \"EXIT_CODE=0 但只做了 exp2 预处理，无任何 predictions 产出。vLLM 参数与成功的 run_fewrel_formal.py 一致，r2 OOM 系其他 GPU 进程占显存所致。已修复 gpu_memory_utilization 0.95→0.85，脚本就绪待 exp012 完成后重跑。\"}, \"exp_fewrel_40rel_r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T16:48:22.142Z\", \"updated_at\": \"2026-05-15T16:56:52.602Z\", \"hypothesis\": \"FewRel 40-rel 中间点 scaling curve: 验证 count↑→accuracy↓ 在 40-rel 规模下的 degradation 幅度，补全 16-rel 到 80-rel 之间的 scaling 趋势\", \"parent\": \"exp_fewrel_40rel\", \"spec\": {\"command\": \"bash scripts/run_fewrel_40rel.sh || python run_fewrel_40rel.py\", \"server\": \"cqa1-38874\", \"gpu\": [\"cuda:0\"], \"pid\": \"299625\", \"log_path\": \"~/runs/schema-dag-extraction/exp_fewrel_40rel_r2.log\", \"submitted_at\": \"2026-05-15T16:50:29.191Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"FewRel 40-rel subset\", \"data_count\": 800, \"model_name\": \"Qwen3-32B-FP8\", \"seed\": 42, \"checkpoint_source\": \"Qwen/Qwen3-32B-FP8 (pre-downloaded on server)\", \"eval_data\": \"FewRel val set, 40-rel subset, count curve + BCS controlled\", \"wall_clock_seconds\": 377.8, \"gpu_hours\": 0.1}, \"conclusion\": \"failed\", \"completed_at\": \"2026-05-15T16:56:46.973Z\", \"notes\": \"vLLM EngineCore OOM during Qwen3-32B-FP8 initialization. SIGKILL at shard 1/7 (14%). Missing FLASHINFER_DISABLE_VERSION_CHECK=1. Creating r3 with correct env vars.\"}, \"exp012_llama_fewnerd_r4\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T16:24:15.927Z\", \"updated_at\": \"2026-05-15T16:49:17.831Z\", \"spec\": {\"command\": \"bash scripts/run_exp012_llama8b.sh\", \"server\": \"cqa1-38874\", \"gpu\": [\"cuda:0\"], \"pid\": \"294443\", \"log_path\": \"~/runs/schema-dag-extraction/exp012_llama_fewnerd_r4.log\", \"submitted_at\": \"2026-05-15T16:24:15.825Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"LLaMA-3.1-8B-Instruct\", \"quantization\": \"none (BF16)\", \"fix_applied\": \"switched from 70B FP8 to 8B BF16 to avoid FlashInfer FP8 kernel JIT failure on Blackwell SM120\", \"data_path\": \"/root/schema-dag-extraction/data/parquet/test.parquet\", \"data_count\": 1000, \"seed\": 42, \"hypothesis\": \"Multi-model validation: LLaMA-3.1-8B-Instruct (BF16) replicates confusability effect on Few-NERD\", \"dataset\": \"Few-NERD\", \"plan_id\": \"exp-012\", \"checkpoint_source\": \"meta-llama/Llama-3.1-8B-Instruct (ModelScope download)\", \"eval_data\": \"Few-NERD test.parquet 1000 samples\", \"wall_clock_seconds\": 1231.4, \"gpu_hours\": 0.34}, \"hypothesis\": \"LLaMA model replicates confusability-driven type confusion pattern observed with Qwen, validating model-independence of the phenomenon\", \"parent\": \"exp012_llama_fewnerd_r3\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-15T16:44:47.235Z\", \"notes\": \"LLaMA-3.1-8B zero predictions on all 94 batches, gen_tokens=2, model outputs empty JSON array. Structured JSON output constraint 下模型无法执行 NER。PID 297093 (rogue vLLM exp2 进程) 已派 Worker kill。\"}, \"exp012_llama_8b_fewnerd\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T16:26:10.725Z\", \"updated_at\": \"2026-05-15T16:41:15.276Z\", \"spec\": {\"hypothesis\": \"Multi-model validation: LLaMA-3.1-8B-Instruct (BF16) replicates confusability effect on Few-NERD — count curve + BCS-controlled, proving effect holds across model families and sizes\", \"dataset\": \"Few-NERD\", \"model\": \"LLaMA-3.1-8B-Instruct\", \"data_path\": \"/root/schema-dag-extraction/data/parquet/test.parquet\", \"data_count\": 1000, \"model_name\": \"LLaMA-3.1-8B-Instruct\", \"seed\": 42, \"plan_id\": \"exp-012\", \"parent\": \"exp012_llama_fewnerd_r3\", \"server\": \"cqa1-38874\", \"command\": \"bash scripts/run_exp012_llama_8b.sh\", \"pid\": 295200, \"log_path\": \"/root/schema-dag-extraction/logs/exp012_llama_8b.log\", \"checkpoint_path\": \"artifacts/exp012_llama_8b/\"}, \"conclusion\": \"failed\", \"notes\": \"Dead entry: PID 295200 was OOM-killed when exp012_llama_fewnerd_r4 (PID 294443) took cuda:0. Superseded by r4.\", \"completed_at\": \"2026-05-15T16:41:15.276Z\"}, \"exp012_llama_8b\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-15T16:06:32.024Z\", \"updated_at\": \"2026-05-15T16:41:03.756Z\", \"spec\": {\"hypothesis\": \"Multi-model validation: LLaMA-3.1-8B replicates confusability effect on Few-NERD (count curve + BCS-controlled)\", \"dataset\": \"Few-NERD\", \"data_path\": \"/root/schema-dag-extraction/data/parquet/test.parquet\", \"data_count\": 1000, \"plan_id\": \"exp-012\", \"parent\": \"exp012_llama_fewnerd_r3\", \"model_name\": \"llama-3.1-8b-instruct\", \"server\": \"cqa1-38874\"}, \"notes\": \"GPU OOM: conflicted with r4 (PID 294443) on cuda:0. PID 295200 killed. Duplicate entry, superseded by exp012_llama_fewnerd_r4.\", \"conclusion\": \"killed\"}, \"exp_fewrel_40rel\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T16:07:32.483Z\", \"updated_at\": \"2026-05-15T16:30:30.024Z\", \"spec\": {\"hypothesis\": \"FewRel 40-rel intermediate point: confirms monotonic scaling between 16-rel and 80-rel for count curve degradation and BCS effect\", \"dataset\": \"FewRel (80 relations pool, max count 40)\", \"model\": \"Qwen3-32B-FP8\", \"data_path\": \"/root/schema-dag-extraction/data/fewrel_parquet/\", \"data_count\": \"full FewRel 80 rel pool, batches capped at 40\", \"model_name\": \"Qwen3-32B-FP8\", \"seed\": 42, \"plan_id\": \"exp-012\", \"parent\": \"exp_fewrel_formal_80rel\", \"command\": \"bash scripts/run_fewrel_40rel.sh\", \"server\": \"cqa1-38874\", \"checkpoint_source\": \"Qwen3-32B-FP8 (same as parent)\", \"eval_data\": \"FewRel 80-rel pool, 1000 balanced samples\"}, \"conclusion\": \"failed\", \"notes\": \"Process killed, results not saved (no per-batch incremental saving). Need to rerun with incremental save after exp012_llama_fewnerd_r4 completes.\", \"completed_at\": \"2026-05-15T16:30:30.024Z\"}, \"exp012_llama_awq\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-15T16:08:55.256Z\", \"updated_at\": \"2026-05-15T16:27:38.824Z\", \"spec\": {\"hypothesis\": \"Multi-model validation: LLaMA-3.1-70B-AWQ replicates confusability effect on Few-NERD (count curve + BCS-controlled)\", \"dataset\": \"Few-NERD\", \"data_path\": \"/root/schema-dag-extraction/data/parquet/test.parquet\", \"data_count\": 1000, \"plan_id\": \"exp-012\", \"parent\": \"exp012_llama_fewnerd_r3\", \"model_name\": \"llama-3.1-70b-instruct-awq-int4\", \"server\": \"cqa1-38874\"}, \"notes\": \"Abandoned: AWQ download failed due to disk space (2.6GB remaining, needed 9.2GB). Superseded by exp012_llama_fewnerd_r4 (8B BF16).\", \"conclusion\": \"killed\"}, \"exp012_llama_fewnerd_r3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T15:53:18.937Z\", \"updated_at\": \"2026-05-15T16:25:46.495Z\", \"spec\": {\"command\": \"bash scripts/run_exp012_llama.sh\", \"server\": \"cqa1-38874\", \"data_path\": \"/root/schema-dag-extraction/data/parquet/test.parquet\", \"data_count\": 1000, \"model_name\": \"LLaMA-3.3-70B-Instruct-FP8\", \"seed\": 42, \"hypothesis\": \"Multi-model validation: LLaMA-70B replicates count-degradation and BCS-confusion patterns found with Qwen3-32B on Few-NERD\", \"dataset\": \"Few-NERD\", \"model_path\": \"/root/autodl-tmp/.hf_cache/llama-3.3-70b-instruct-fp8/\", \"plan_id\": \"exp-012\", \"claim\": \"1+2\", \"gpu\": [\"cuda:0\"], \"log_path\": \"/tmp/exp012_r3.log\"}, \"notes\": \"vLLM engine core initialization failed — flashinfer JIT requires CUDA 12.9 but server has nvcc 12.8, SM120 Blackwell FP8 incompatible. Same root cause as r1/r2. Three consecutive failures, FP8 path abandoned.\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-15T16:25:46.495Z\"}}, \"count\": 10, \"total\": 27, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.1073}}"
    }
  },
  "sourceToolAssistantUUID": "f51bc04c-e450-4422-bc6a-6d133f4765a4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/reviewer_efaaa6bc",
  "sessionId": "f59020b4-1c0e-4081-9cb3-293eac3560ff",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-15T17:15:28.327Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01LBCaKWVK8XhJoqYnB1hetN`</summary>

```json
{
  "project": "schema-dag-extraction",
  "file": "report.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c60307c2-1593-4790-b665-d58078c00164",
  "isSidechain": false,
  "requestId": "req_011Cb4jQMLA5Q7jjcXuhvTJ8",
  "type": "assistant",
  "uuid": "71a98d2f-1975-4de2-9c5a-23506bc0879a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/reviewer_efaaa6bc",
  "sessionId": "f59020b4-1c0e-4081-9cb3-293eac3560ff",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GPPHHwJoc7aeRBjYvkbjUa",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 995,
      "cache_read_input_tokens": 30690,
      "output_tokens": 173,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 995,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 173,
          "cache_read_input_tokens": 30690,
          "cache_creation_input_tokens": 995,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 995
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

_source line 15 · 2026-05-15T17:15:28.341Z_

<details><summary>↩ Tool result · `toolu_01LBCaKWVK8XhJoqYnB1hetN`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/report.md\", \"content\": \"# Handover — 2026-05-15\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n（无）\\n\\n## 待处理\\n- exp012_llama_8b_r2（准备中）\\n- exp012_llama_8b（准备中）\\n- exp012_llama_awq（准备中）\\n\\n## 近期结论\\n- **exp_fewrel_40rel_r3** (failed): FewRel 40-rel 中间点 scaling curve: 验证 count↑→accuracy↓ 在 40-rel 规模下的 degradation 幅度，补全 16-rel 到 80-rel 之间的 scaling 趋势 ← 基于 exp_fewrel_40rel_r2\\n- **exp_fewrel_40rel_r2** (failed): FewRel 40-rel 中间点 scaling curve: 验证 count↑→accuracy↓ 在 40-rel 规模下的 degradation 幅度，补全 16-rel 到 80-rel 之间的 scaling 趋势 ← 基于 exp_fewrel_40rel\\n- **exp012_llama_fewnerd_r4** (failed): LLaMA model replicates confusability-driven type confusion pattern observed with Qwen, validating model-independence of the phenomenon ← 基于 exp012_llama_fewnerd_r3\\n\\n## 趋势\\n成功 11 / 负向 3 / 失败 9 / 共 23\\n\\n## 下一步\\n（无活跃 idea，请通过 ideas.md 添加）\\n\\n## 资源状态\\ncqa1-38874: 无 GPU 信息\\n\\n## 告警\\n- exp008_sdgd_zero_fewnerd: 训练失败 — unknown\\n- exp012_llama_fewnerd: 训练失败 — unknown\\n- exp012_llama_fewnerd_r2: 训练失败 — unknown\\n- exp012_llama_fewnerd_r3: 训练失败 — unknown\\n- exp_fewrel_40rel: 训练失败 — unknown\\n- exp012_llama_fewnerd_r4: 训练失败 — unknown\\n- exp012_llama_8b_fewnerd: 训练失败 — unknown\\n- exp_fewrel_40rel_r2: 训练失败 — unknown\\n- exp_fewrel_40rel_r3: 训练失败 — unknown\\n\", \"total_chars\": 1184, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "71a98d2f-1975-4de2-9c5a-23506bc0879a",
  "isSidechain": false,
  "promptId": "b593ab42-40aa-4651-8f99-a82b6d6b969a",
  "type": "user",
  "uuid": "727b4ea8-57d2-459d-b245-7e29320840f0",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/report.md\\\", \\\"content\\\": \\\"# Handover — 2026-05-15\\\\n\\\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\\\n\\\\n## 运行中\\\\n（无）\\\\n\\\\n## 待处理\\\\n- exp012_llama_8b_r2（准备中）\\\\n- exp012_llama_8b（准备中）\\\\n- exp012_llama_awq（准备中）\\\\n\\\\n## 近期结论\\\\n- **exp_fewrel_40rel_r3** (failed): FewRel 40-rel 中间点 scaling curve: 验证 count↑→accuracy↓ 在 40-rel 规模下的 degradation 幅度，补全 16-rel 到 80-rel 之间的 scaling 趋势 ← 基于 exp_fewrel_40rel_r2\\\\n- **exp_fewrel_40rel_r2** (failed): FewRel 40-rel 中间点 scaling curve: 验证 count↑→accuracy↓ 在 40-rel 规模下的 degradation 幅度，补全 16-rel 到 80-rel 之间的 scaling 趋势 ← 基于 exp_fewrel_40rel\\\\n- **exp012_llama_fewnerd_r4** (failed): LLaMA model replicates confusability-driven type confusion pattern observed with Qwen, validating model-independence of the phenomenon ← 基于 exp012_llama_fewnerd_r3\\\\n\\\\n## 趋势\\\\n成功 11 / 负向 3 / 失败 9 / 共 23\\\\n\\\\n## 下一步\\\\n（无活跃 idea，请通过 ideas.md 添加）\\\\n\\\\n## 资源状态\\\\ncqa1-38874: 无 GPU 信息\\\\n\\\\n## 告警\\\\n- exp008_sdgd_zero_fewnerd: 训练失败 — unknown\\\\n- exp012_llama_fewnerd: 训练失败 — unknown\\\\n- exp012_llama_fewnerd_r2: 训练失败 — unknown\\\\n- exp012_llama_fewnerd_r3: 训练失败 — unknown\\\\n- exp_fewrel_40rel: 训练失败 — unknown\\\\n- exp012_llama_fewnerd_r4: 训练失败 — unknown\\\\n- exp012_llama_8b_fewnerd: 训练失败 — unknown\\\\n- exp_fewrel_40rel_r2: 训练失败 — unknown\\\\n- exp_fewrel_40rel_r3: 训练失败 — unknown\\\\n\\\", \\\"total_chars\\\": 1184, \\\"truncated\\\": false}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/report.md\", \"content\": \"# Handover — 2026-05-15\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n（无）\\n\\n## 待处理\\n- exp012_llama_8b_r2（准备中）\\n- exp012_llama_8b（准备中）\\n- exp012_llama_awq（准备中）\\n\\n## 近期结论\\n- **exp_fewrel_40rel_r3** (failed): FewRel 40-rel 中间点 scaling curve: 验证 count↑→accuracy↓ 在 40-rel 规模下的 degradation 幅度，补全 16-rel 到 80-rel 之间的 scaling 趋势 ← 基于 exp_fewrel_40rel_r2\\n- **exp_fewrel_40rel_r2** (failed): FewRel 40-rel 中间点 scaling curve: 验证 count↑→accuracy↓ 在 40-rel 规模下的 degradation 幅度，补全 16-rel 到 80-rel 之间的 scaling 趋势 ← 基于 exp_fewrel_40rel\\n- **exp012_llama_fewnerd_r4** (failed): LLaMA model replicates confusability-driven type confusion pattern observed with Qwen, validating model-independence of the phenomenon ← 基于 exp012_llama_fewnerd_r3\\n\\n## 趋势\\n成功 11 / 负向 3 / 失败 9 / 共 23\\n\\n## 下一步\\n（无活跃 idea，请通过 ideas.md 添加）\\n\\n## 资源状态\\ncqa1-38874: 无 GPU 信息\\n\\n## 告警\\n- exp008_sdgd_zero_fewnerd: 训练失败 — unknown\\n- exp012_llama_fewnerd: 训练失败 — unknown\\n- exp012_llama_fewnerd_r2: 训练失败 — unknown\\n- exp012_llama_fewnerd_r3: 训练失败 — unknown\\n- exp_fewrel_40rel: 训练失败 — unknown\\n- exp012_llama_fewnerd_r4: 训练失败 — unknown\\n- exp012_llama_8b_fewnerd: 训练失败 — unknown\\n- exp_fewrel_40rel_r2: 训练失败 — unknown\\n- exp_fewrel_40rel_r3: 训练失败 — unknown\\n\", \"total_chars\": 1184, \"truncated\": false}, \"error\": null, \"metadata\": {}}"
    }
  },
  "sourceToolAssistantUUID": "71a98d2f-1975-4de2-9c5a-23506bc0879a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/reviewer_efaaa6bc",
  "sessionId": "f59020b4-1c0e-4081-9cb3-293eac3560ff",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 16_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[系统通知 — worker_done:worker_paper_research_bib_sync_20260515T171027]: Worker worker_paper_research_bib_sync_20260515T171027 已完成（status=done），请审查 Agent 的处理结果。",
  "leafUuid": "727b4ea8-57d2-459d-b245-7e29320840f0",
  "sessionId": "f59020b4-1c0e-4081-9cb3-293eac3560ff"
}
```

---

### Runtime record

_source line 17_

```json
{
  "type": "ai-title",
  "aiTitle": "Review paper research bibliography sync results",
  "sessionId": "f59020b4-1c0e-4081-9cb3-293eac3560ff"
}
```

---

### Assistant

_source line 18 · 2026-05-15T17:15:43.182Z_

<details><summary>Logged reasoning block</summary>

```text
The worker task was "paper_research_bib_sync" - this seems to be about syncing bibliography/references for the paper. Let me check what this worker actually did. I should look at the recent changes to understand what bib sync means. Let me check the literature_map.yaml or any bib-related files, and also look at the older registry entries to get context on what successful experiments exist.

Actually, the worker name is "worker_paper_research_bib_sync_20260515T171027" - this is about paper research bibliography synchronization. Let me look at what files were changed and what the worker's actual output was.


Now I need to examine the literature_map.yaml and any bibliography files to see what the bib sync worker actually modified.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "727b4ea8-57d2-459d-b245-7e29320840f0",
  "isSidechain": false,
  "requestId": "req_011Cb4jQc1wxpappYiS3eeJs",
  "type": "assistant",
  "uuid": "eca47792-36d5-44a6-b350-fe7f5a128591",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/reviewer_efaaa6bc",
  "sessionId": "f59020b4-1c0e-4081-9cb3-293eac3560ff",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01G1gt8poiUhy32oNnwZUFyY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5722,
      "cache_read_input_tokens": 31685,
      "output_tokens": 534,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5722,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 534,
          "cache_read_input_tokens": 31685,
          "cache_creation_input_tokens": 5722,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5722
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

_source line 19 · 2026-05-15T17:15:43.358Z_

Worker 名称是 bib_sync，需要看论文引用相关文件。继续读取相关资料。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "eca47792-36d5-44a6-b350-fe7f5a128591",
  "isSidechain": false,
  "requestId": "req_011Cb4jQc1wxpappYiS3eeJs",
  "type": "assistant",
  "uuid": "b47c136a-a43c-4885-b1f7-86acc0cb161f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/reviewer_efaaa6bc",
  "sessionId": "f59020b4-1c0e-4081-9cb3-293eac3560ff",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01G1gt8poiUhy32oNnwZUFyY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5722,
      "cache_read_input_tokens": 31685,
      "output_tokens": 534,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5722,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 534,
          "cache_read_input_tokens": 31685,
          "cache_creation_input_tokens": 5722,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5722
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

_source line 20 · 2026-05-15T17:15:44.360Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01353412yXKpuXmgNvi61qbf`</summary>

```json
{
  "project": "schema-dag-extraction",
  "file": "literature_map.yaml",
  "max_chars": 12000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b47c136a-a43c-4885-b1f7-86acc0cb161f",
  "isSidechain": false,
  "requestId": "req_011Cb4jQc1wxpappYiS3eeJs",
  "type": "assistant",
  "uuid": "e630bb63-2ba0-4c4e-b189-59989e9ab1b9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/reviewer_efaaa6bc",
  "sessionId": "f59020b4-1c0e-4081-9cb3-293eac3560ff",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01G1gt8poiUhy32oNnwZUFyY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5722,
      "cache_read_input_tokens": 31685,
      "output_tokens": 534,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5722,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 534,
          "cache_read_input_tokens": 31685,
          "cache_creation_input_tokens": 5722,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5722
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

_source line 21 · 2026-05-15T17:15:45.624Z_

<details><summary>↩ Tool result · `toolu_0196Awu2ZeMQdpLMyBSpqKtA`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/references.bib
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7f981343-3bab-4553-910c-a650c1059c07",
  "isSidechain": false,
  "promptId": "b593ab42-40aa-4651-8f99-a82b6d6b969a",
  "type": "user",
  "uuid": "cc2040fd-e133-463e-b54e-531793d13528",
  "toolUseResult": {
    "filenames": [
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/references.bib"
    ],
    "durationMs": 20,
    "numFiles": 1,
    "truncated": false
  },
  "sourceToolAssistantUUID": "7f981343-3bab-4553-910c-a650c1059c07",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/reviewer_efaaa6bc",
  "sessionId": "f59020b4-1c0e-4081-9cb3-293eac3560ff",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-15T17:15:44.384Z_

<details><summary>↩ Tool result · `toolu_01353412yXKpuXmgNvi61qbf`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/literature_map.yaml\", \"content\": \"# Literature Map for schema-dag-extraction\\n# Updated: 2026-05-15\\n# Paper: Multi-channel Degradation Model + SDGD Framework for Training-free LLM IE\\n\\n# =============================================================================\\n# DIRECT COMPETITORS — schema decomposition for LLM-based IE\\n# =============================================================================\\n\\n- id: llm-pee-2025\\n  title: \\\"Towards Event Extraction with Massive Types: LLM-based Collaborative Annotation and Partitioning Extraction\\\"\\n  year: 2025\\n  venue: arXiv\\n  url: https://arxiv.org/abs/2503.02628\\n  role: direct-competitor\\n  relevance_note: >\\n    Similarity-based type recall + type-partitioning prompting for massive event types.\\n    Divides candidate types into partitions to reduce prompt length.\\n    +5.4% event detection, +6.1% argument extraction, +12.9% F1 over mainstream LLMs zero-shot.\\n    KEY DIFF: partitions by similarity-based recall, NOT confusability-aware.\\n    Our DAG decomposition is confusability-driven, not just similarity-driven.\\n\\n- id: parse-2025\\n  title: \\\"PARSE: LLM Driven Schema Optimization for Reliable Entity Extraction\\\"\\n  authors: [Anubhav Shrimal, Aryan Jain, Soumyajit Chowdhury, Promod Yenigalla]\\n  year: 2025\\n  venue: EMNLP 2025 Industry\\n  url: https://arxiv.org/abs/2510.08623\\n  role: direct-competitor\\n  relevance_note: >\\n    ARCHITECT autonomously rewrites JSON schemas for LLM consumption.\\n    SCOPE uses reflection-based extraction with guardrails. +64.7% on SWDE.\\n    Treats schema optimization as black-box LLM rewriting, not principled decomposition.\\n    Does NOT model type confusability explicitly.\\n\\n- id: dee-2024\\n  title: \\\"Decompose, Enrich, and Extract! Schema-aware Event Extraction using LLMs\\\"\\n  year: 2024\\n  venue: arXiv\\n  url: https://arxiv.org/abs/2406.01045\\n  role: direct-competitor\\n  relevance_note: >\\n    Decomposes event extraction into detection + argument extraction.\\n    Dynamic schema-aware RAG for augmented prompts.\\n    KEY DIFF: task-level decomposition (detection vs argument), not schema-level type decomposition.\\n\\n- id: crossagentie-2025\\n  title: \\\"CROSSAGENTIE: Cross-Type and Cross-Task Multi-Agent LLM Collaboration for Zero-Shot IE\\\"\\n  authors: [Meng Lu, Yuzhang Xie, Zhenyu Bi, Shuxiang Cao, Xuan Wang]\\n  year: 2025\\n  venue: ACL 2025 Findings\\n  url: https://aclanthology.org/2025.findings-acl.718/\\n  role: direct-competitor\\n  relevance_note: >\\n    Multi-agent: intra-group cross-type debate (resolves entity-label conflicts)\\n    + inter-group cross-task debate (NER↔RE mutual refinement).\\n    ⚠️ MODERATE NOVELTY CONCERN: cross-type debate explicitly addresses type confusion.\\n    KEY DIFF: reactive debate to resolve confusion post-hoc vs our proactive decomposition to prevent it.\\n    Must clearly differentiate in paper.\\n\\n- id: dlisc-2025\\n  title: \\\"Effective and Efficient Schema-aware Information Extraction Using On-Device LLMs\\\"\\n  year: 2025\\n  venue: arXiv (May 2025)\\n  url: https://arxiv.org/abs/2505.14992\\n  role: direct-competitor\\n  relevance_note: >\\n    Dual-LoRA with Incremental Schema Caching.\\n    Identification LoRA retrieves relevant schemas, Extraction LoRA performs IE.\\n    Focus on efficiency for on-device LLMs, not confusability analysis.\\n\\n- id: spt-2025\\n  title: \\\"Schema as Parameterized Tools for Universal Information Extraction\\\"\\n  year: 2025\\n  venue: arXiv (June 2025)\\n  url: https://arxiv.org/abs/2506.01276\\n  role: direct-competitor\\n  relevance_note: >\\n    Treats schemas as parameterized tools for LLM tool-calling.\\n    Schema retrieval + generation + infilling. Novel schema-LLM interface.\\n    Does not address type confusability.\\n\\n- id: zeroner-2025\\n  title: \\\"ZeroNER: Fueling Zero-Shot NER via Entity Type Descriptions\\\"\\n  year: 2025\\n  venue: ACL 2025 Findings\\n  url: https://aclanthology.org/2025.findings-acl.805/\\n  role: direct-competitor\\n  relevance_note: >\\n    Description-driven: LLM supervision → BERT student for unseen types.\\n    +16% F1 over LLMs on hard zero-shot. Leverages type descriptions.\\n    Related to how schema semantics affect extraction quality.\\n\\n- id: cmas-ner-2025\\n  title: \\\"A Cooperative Multi-Agent Framework for Zero-Shot Named Entity Recognition\\\"\\n  year: 2025\\n  venue: TheWebConf 2025\\n  url: https://dl.acm.org/doi/10.1145/3696410.3714923\\n  role: direct-competitor\\n  relevance_note: >\\n    Multi-agent collective intelligence for zero-shot NER.\\n    Addresses context correlation and indiscriminate demonstration problems.\\n    Outperforms on 6 benchmarks including domain-specific and general-domain.\\n\\n# =============================================================================\\n# METHOD COMPONENTS — techniques we build upon or relate to\\n# =============================================================================\\n\\n- id: uniner-2024\\n  title: \\\"UniversalNER: Targeted Distillation from Large Language Models for Open NER\\\"\\n  authors: [Wenxuan Zhou et al.]\\n  year: 2024\\n  venue: ICLR 2024\\n  url: https://arxiv.org/abs/2308.03279\\n  role: method-component\\n  relevance_note: >\\n    Instruction-tuning on ChatGPT-generated NER data. 43 datasets, 9 domains, 13K+ types.\\n    UniNER-7B outperforms ChatGPT by 7 F1 points.\\n    Important baseline for universal NER and schema-at-scale challenges.\\n\\n- id: gollie-2024\\n  title: \\\"GoLLIE: Annotation Guidelines Following Large Language Model for Information Extraction\\\"\\n  authors: [Oscar Sainz et al.]\\n  year: 2024\\n  venue: ICLR 2024\\n  url: https://hitz-zentroa.github.io/GoLLIE/\\n  role: method-component\\n  relevance_note: >\\n    Code-style schema definitions + annotation guideline following.\\n    Strong zero-shot on unseen IE tasks. Code-Llama based.\\n    Baseline for guideline-driven schema representation.\\n\\n- id: gliner-2024\\n  title: \\\"GLiNER: Generalist Model for Named Entity Recognition using Bidirectional Transformer\\\"\\n  authors: [Urchade Zaratiana et al.]\\n  year: 2024\\n  venue: NAACL 2024\\n  url: https://arxiv.org/abs/2311.08526\\n  role: method-component\\n  relevance_note: >\\n    Compact bidirectional encoder for zero-shot NER with parallel extraction.\\n    Outperforms InstructUIE and larger models. Non-LLM competitive baseline.\\n\\n- id: gliner2-2025\\n  title: \\\"GLiNER2: Efficient Multi-Task IE System with Schema-Driven Interface\\\"\\n  authors: [Urchade Zaratiana et al.]\\n  year: 2025\\n  venue: EMNLP 2025 Demo\\n  url: https://arxiv.org/abs/2507.18546\\n  role: method-component\\n  relevance_note: >\\n    Extends GLiNER to multi-task IE (NER+RE+classification). 205M params, CPU-efficient.\\n    Schema-driven interface. Shows schema approach scales to multi-task.\\n\\n- id: kggen-2025\\n  title: \\\"KGGen: Extracting Knowledge Graphs from Plain Text with Language Models\\\"\\n  authors: [Mo et al.]\\n  year: 2025\\n  venue: NeurIPS 2025\\n  url: https://arxiv.org/abs/2502.09956\\n  role: method-component\\n  relevance_note: >\\n    Two-stage decomposition: entities first, then relations.\\n    Entity clustering/deduplication to reduce graph sparsity.\\n    Schema decomposition approach for KG construction.\\n\\n- id: code4uie-2024\\n  title: \\\"Retrieval-Augmented Code Generation for Universal Information Extraction\\\"\\n  authors: [Yucan Guo et al.]\\n  year: 2024\\n  venue: NeurIPS 2024 Workshop\\n  url: https://arxiv.org/abs/2311.02962\\n  role: method-component\\n  relevance_note: >\\n    Python class-based schema definitions + RAG for code generation.\\n    Unified code-style schema for all IE tasks.\\n\\n- id: iepile-2024\\n  title: \\\"IEPile: Unearthing Large-Scale Schema-Based Information Extraction Corpus\\\"\\n  authors: [Guanzheng Chen et al., ZJU NLP]\\n  year: 2024\\n  venue: ACL 2024\\n  url: https://arxiv.org/abs/2402.14710\\n  role: method-component\\n  relevance_note: >\\n    0.32B token bilingual IE corpus. Hard negative schema construction =\\n    semantically proximate schemas to train type discrimination.\\n    ⚠️ RELATED: hard negatives ≈ confusable schemas, but for TRAINING, not inference-time.\\n    Our contribution is inference-time confusability-aware decomposition (training-free).\\n\\n- id: lost-in-middle-2024\\n  title: \\\"Lost in the Middle: How Language Models Use Long Contexts\\\"\\n  authors: [Nelson F. Liu et al.]\\n  year: 2024\\n  venue: TACL 2024\\n  url: https://arxiv.org/abs/2307.03172\\n  role: method-component\\n  relevance_note: >\\n    LLMs degrade when relevant info is in middle of long contexts (U-shaped attention).\\n    Motivates schema decomposition to reduce prompt length.\\n    No IE-specific follow-up found — opportunity for us to be first to connect this to IE.\\n\\n# =============================================================================\\n# ZERO-SHOT NER / RE BASELINES\\n# =============================================================================\\n\\n- id: self-improve-ner-2024\\n  title: \\\"Self-Improving for Zero-Shot Named Entity Recognition with Large Language Models\\\"\\n  year: 2024\\n  venue: NAACL 2024\\n  url: https://arxiv.org/abs/2311.08921\\n  role: background\\n  relevance_note: >\\n    Self-improving framework using LLM self-generated examples for zero-shot NER.\\n\\n- id: self-prompting-re-2024\\n  title: \\\"Unleashing the Power of LLMs in Zero-shot Relation Extraction via Self-Prompting\\\"\\n  year: 2024\\n  venue: EMNLP 2024 Findings\\n  url: https://arxiv.org/abs/2410.01154\\n  role: background\\n  relevance_note: >\\n    Three-stage self-prompting for zero-shot RE. Generates synthetic ICL samples.\\n    Training-free RE baseline.\\n\\n- id: reasoning-ner-2025\\n  title: \\\"A Reasoning Paradigm for Named Entity Recognition\\\"\\n  year: 2025\\n  venue: arXiv (Nov 2025)\\n  url: https://arxiv.org/abs/2511.11978\\n  role: background\\n  relevance_note: >\\n    CoT-based reasoning for NER. Outperforms GPT-4 by 12.3 F1 in zero-shot.\\n    Shifts NER from pattern matching to explicit reasoning. Strong zero-shot baseline.\\n\\n- id: nuner-2024\\n  title: \\\"NuNER: Entity Recognition Encoder Pre-training via LLM-Annotated Data\\\"\\n  authors: [Sergei Bogdanov et al., NuMind]\\n  year: 2024\\n  venue: EMNLP 2024\\n  url: https://arxiv.org/abs/2402.15343\\n  role: background\\n  relevance_note: >\\n    Contrastive pre-training on LLM-annotated data. Strong few-shot NER foundation model.\\n\\n# =============================================================================\\n# EVALUATION / BENCHMARKING\\n# =============================================================================\\n\\n- id: familiarity-2025\\n  title: \\\"Familiarity: Better Evaluation of Zero-Shot NER by Quantifying Label Shifts in Synthetic Training Data\\\"\\n  year: 2025\\n  venue: NAACL 2025\\n  url: https://arxiv.org/abs/2412.10121\\n  role: evaluation\\n  relevance_note: >\\n    \\\"Familiarity\\\" metric for label shift in synthetic NER data.\\n    Zero-shot NER scores overestimated due to train-eval label overlap.\\n    Quantifies semantic similarity between entity types — related to type confusability.\\n    KEY DIFF: measures evaluation bias, not extraction-time confusability.\\n\\n- id: guidex-2025\\n  title: \\\"GuideX: Guided Synthetic Data Generation for Zero-Shot Information Extraction\\\"\\n  authors: [Neil Deshpande et al.]\\n  year: 2025\\n  venue: ACL 2025 Findings\\n  url: https://arxiv.org/abs/2506.00649\\n  role: evaluation\\n  relevance_note: >\\n    Auto-generates domain-specific schemas + guidelines + synthetic labels.\\n    SOTA on 7 zero-shot NER benchmarks (+7 F1). Strong baseline.\\n\\n# =============================================================================\\n# SURVEYS\\n# =============================================================================\\n\\n- id: llm4ie-survey-2024\\n  title: \\\"Large Language Models for Generative Information Extraction: A Survey\\\"\\n  authors: [Derong Xu et al.]\\n  year: 2024\\n  venue: Frontiers of Computer Science\\n  url: https://arxiv.org/abs/2312.17617\\n  role: background\\n  relevance_note: >\\n    Comprehensive survey of LLM-based IE covering prompting, fine-tuning, benchmarks.\\n\\n- id: knowcoder-2024\\n  title: \\\"KnowCoder: Coding Structured Knowledge into LLMs for Universal IE\\\"\\n  year: 2024\\n  venue: ACL 2024\\n  url: https://arxiv.org/abs/2403.07969\\n  role: background\\n  relevance_note: >\\n    Encodes schema knowledge via code structures into LLM.\\n    Related to code-based schema representation.\\n\\n- id: slot-2025\\n  title: \\\"SLOT: Structuring the Output of Large\\n\\n... [截断: 省略 6972 字符，传 max_chars=0 获取完整内容]\", \"total_chars\": 18972, \"truncated\": true}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e630bb63-2ba0-4c4e-b189-59989e9ab1b9",
  "isSidechain": false,
  "promptId": "b593ab42-40aa-4651-8f99-a82b6d6b969a",
  "type": "user",
  "uuid": "d03f1be1-c1c5-4bf3-94c3-9ecf767a0b66",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/literature_map.yaml\\\", \\\"content\\\": \\\"# Literature Map for schema-dag-extraction\\\\n# Updated: 2026-05-15\\\\n# Paper: Multi-channel Degradation Model + SDGD Framework for Training-free LLM IE\\\\n\\\\n# =============================================================================\\\\n# DIRECT COMPETITORS — schema decomposition for LLM-based IE\\\\n# =============================================================================\\\\n\\\\n- id: llm-pee-2025\\\\n  title: \\\\\\\"Towards Event Extraction with Massive Types: LLM-based Collaborative Annotation and Partitioning Extraction\\\\\\\"\\\\n  year: 2025\\\\n  venue: arXiv\\\\n  url: https://arxiv.org/abs/2503.02628\\\\n  role: direct-competitor\\\\n  relevance_note: >\\\\n    Similarity-based type recall + type-partitioning prompting for massive event types.\\\\n    Divides candidate types into partitions to reduce prompt length.\\\\n    +5.4% event detection, +6.1% argument extraction, +12.9% F1 over mainstream LLMs zero-shot.\\\\n    KEY DIFF: partitions by similarity-based recall, NOT confusability-aware.\\\\n    Our DAG decomposition is confusability-driven, not just similarity-driven.\\\\n\\\\n- id: parse-2025\\\\n  title: \\\\\\\"PARSE: LLM Driven Schema Optimization for Reliable Entity Extraction\\\\\\\"\\\\n  authors: [Anubhav Shrimal, Aryan Jain, Soumyajit Chowdhury, Promod Yenigalla]\\\\n  year: 2025\\\\n  venue: EMNLP 2025 Industry\\\\n  url: https://arxiv.org/abs/2510.08623\\\\n  role: direct-competitor\\\\n  relevance_note: >\\\\n    ARCHITECT autonomously rewrites JSON schemas for LLM consumption.\\\\n    SCOPE uses reflection-based extraction with guardrails. +64.7% on SWDE.\\\\n    Treats schema optimization as black-box LLM rewriting, not principled decomposition.\\\\n    Does NOT model type confusability explicitly.\\\\n\\\\n- id: dee-2024\\\\n  title: \\\\\\\"Decompose, Enrich, and Extract! Schema-aware Event Extraction using LLMs\\\\\\\"\\\\n  year: 2024\\\\n  venue: arXiv\\\\n  url: https://arxiv.org/abs/2406.01045\\\\n  role: direct-competitor\\\\n  relevance_note: >\\\\n    Decomposes event extraction into detection + argument extraction.\\\\n    Dynamic schema-aware RAG for augmented prompts.\\\\n    KEY DIFF: task-level decomposition (detection vs argument), not schema-level type decomposition.\\\\n\\\\n- id: crossagentie-2025\\\\n  title: \\\\\\\"CROSSAGENTIE: Cross-Type and Cross-Task Multi-Agent LLM Collaboration for Zero-Shot IE\\\\\\\"\\\\n  authors: [Meng Lu, Yuzhang Xie, Zhenyu Bi, Shuxiang Cao, Xuan Wang]\\\\n  year: 2025\\\\n  venue: ACL 2025 Findings\\\\n  url: https://aclanthology.org/2025.findings-acl.718/\\\\n  role: direct-competitor\\\\n  relevance_note: >\\\\n    Multi-agent: intra-group cross-type debate (resolves entity-label conflicts)\\\\n    + inter-group cross-task debate (NER↔RE mutual refinement).\\\\n    ⚠️ MODERATE NOVELTY CONCERN: cross-type debate explicitly addresses type confusion.\\\\n    KEY DIFF: reactive debate to resolve confusion post-hoc vs our proactive decomposition to prevent it.\\\\n    Must clearly differentiate in paper.\\\\n\\\\n- id: dlisc-2025\\\\n  title: \\\\\\\"Effective and Efficient Schema-aware Information Extraction Using On-Device LLMs\\\\\\\"\\\\n  year: 2025\\\\n  venue: arXiv (May 2025)\\\\n  url: https://arxiv.org/abs/2505.14992\\\\n  role: direct-competitor\\\\n  relevance_note: >\\\\n    Dual-LoRA with Incremental Schema Caching.\\\\n    Identification LoRA retrieves relevant schemas, Extraction LoRA performs IE.\\\\n    Focus on efficiency for on-device LLMs, not confusability analysis.\\\\n\\\\n- id: spt-2025\\\\n  title: \\\\\\\"Schema as Parameterized Tools for Universal Information Extraction\\\\\\\"\\\\n  year: 2025\\\\n  venue: arXiv (June 2025)\\\\n  url: https://arxiv.org/abs/2506.01276\\\\n  role: direct-competitor\\\\n  relevance_note: >\\\\n    Treats schemas as parameterized tools for LLM tool-calling.\\\\n    Schema retrieval + generation + infilling. Novel schema-LLM interface.\\\\n    Does not address type confusability.\\\\n\\\\n- id: zeroner-2025\\\\n  title: \\\\\\\"ZeroNER: Fueling Zero-Shot NER via Entity Type Descriptions\\\\\\\"\\\\n  year: 2025\\\\n  venue: ACL 2025 Findings\\\\n  url: https://aclanthology.org/2025.findings-acl.805/\\\\n  role: direct-competitor\\\\n  relevance_note: >\\\\n    Description-driven: LLM supervision → BERT student for unseen types.\\\\n    +16% F1 over LLMs on hard zero-shot. Leverages type descriptions.\\\\n    Related to how schema semantics affect extraction quality.\\\\n\\\\n- id: cmas-ner-2025\\\\n  title: \\\\\\\"A Cooperative Multi-Agent Framework for Zero-Shot Named Entity Recognition\\\\\\\"\\\\n  year: 2025\\\\n  venue: TheWebConf 2025\\\\n  url: https://dl.acm.org/doi/10.1145/3696410.3714923\\\\n  role: direct-competitor\\\\n  relevance_note: >\\\\n    Multi-agent collective intelligence for zero-shot NER.\\\\n    Addresses context correlation and indiscriminate demonstration problems.\\\\n    Outperforms on 6 benchmarks including domain-specific and general-domain.\\\\n\\\\n# =============================================================================\\\\n# METHOD COMPONENTS — techniques we build upon or relate to\\\\n# =============================================================================\\\\n\\\\n- id: uniner-2024\\\\n  title: \\\\\\\"UniversalNER: Targeted Distillation from Large Language Models for Open NER\\\\\\\"\\\\n  authors: [Wenxuan Zhou et al.]\\\\n  year: 2024\\\\n  venue: ICLR 2024\\\\n  url: https://arxiv.org/abs/2308.03279\\\\n  role: method-component\\\\n  relevance_note: >\\\\n    Instruction-tuning on ChatGPT-generated NER data. 43 datasets, 9 domains, 13K+ types.\\\\n    UniNER-7B outperforms ChatGPT by 7 F1 points.\\\\n    Important baseline for universal NER and schema-at-scale challenges.\\\\n\\\\n- id: gollie-2024\\\\n  title: \\\\\\\"GoLLIE: Annotation Guidelines Following Large Language Model for Information Extraction\\\\\\\"\\\\n  authors: [Oscar Sainz et al.]\\\\n  year: 2024\\\\n  venue: ICLR 2024\\\\n  url: https://hitz-zentroa.github.io/GoLLIE/\\\\n  role: method-component\\\\n  relevance_note: >\\\\n    Code-style schema definitions + annotation guideline following.\\\\n    Strong zero-shot on unseen IE tasks. Code-Llama based.\\\\n    Baseline for guideline-driven schema representation.\\\\n\\\\n- id: gliner-2024\\\\n  title: \\\\\\\"GLiNER: Generalist Model for Named Entity Recognition using Bidirectional Transformer\\\\\\\"\\\\n  authors: [Urchade Zaratiana et al.]\\\\n  year: 2024\\\\n  venue: NAACL 2024\\\\n  url: https://arxiv.org/abs/2311.08526\\\\n  role: method-component\\\\n  relevance_note: >\\\\n    Compact bidirectional encoder for zero-shot NER with parallel extraction.\\\\n    Outperforms InstructUIE and larger models. Non-LLM competitive baseline.\\\\n\\\\n- id: gliner2-2025\\\\n  title: \\\\\\\"GLiNER2: Efficient Multi-Task IE System with Schema-Driven Interface\\\\\\\"\\\\n  authors: [Urchade Zaratiana et al.]\\\\n  year: 2025\\\\n  venue: EMNLP 2025 Demo\\\\n  url: https://arxiv.org/abs/2507.18546\\\\n  role: method-component\\\\n  relevance_note: >\\\\n    Extends GLiNER to multi-task IE (NER+RE+classification). 205M params, CPU-efficient.\\\\n    Schema-driven interface. Shows schema approach scales to multi-task.\\\\n\\\\n- id: kggen-2025\\\\n  title: \\\\\\\"KGGen: Extracting Knowledge Graphs from Plain Text with Language Models\\\\\\\"\\\\n  authors: [Mo et al.]\\\\n  year: 2025\\\\n  venue: NeurIPS 2025\\\\n  url: https://arxiv.org/abs/2502.09956\\\\n  role: method-component\\\\n  relevance_note: >\\\\n    Two-stage decomposition: entities first, then relations.\\\\n    Entity clustering/deduplication to reduce graph sparsity.\\\\n    Schema decomposition approach for KG construction.\\\\n\\\\n- id: code4uie-2024\\\\n  title: \\\\\\\"Retrieval-Augmented Code Generation for Universal Information Extraction\\\\\\\"\\\\n  authors: [Yucan Guo et al.]\\\\n  year: 2024\\\\n  venue: NeurIPS 2024 Workshop\\\\n  url: https://arxiv.org/abs/2311.02962\\\\n  role: method-component\\\\n  relevance_note: >\\\\n    Python class-based schema definitions + RAG for code generation.\\\\n    Unified code-style schema for all IE tasks.\\\\n\\\\n- id: iepile-2024\\\\n  title: \\\\\\\"IEPile: Unearthing Large-Scale Schema-Based Information Extraction Corpus\\\\\\\"\\\\n  authors: [Guanzheng Chen et al., ZJU NLP]\\\\n  year: 2024\\\\n  venue: ACL 2024\\\\n  url: https://arxiv.org/abs/2402.14710\\\\n  role: method-component\\\\n  relevance_note: >\\\\n    0.32B token bilingual IE corpus. Hard negative schema construction =\\\\n    semantically proximate schemas to train type discrimination.\\\\n    ⚠️ RELATED: hard negatives ≈ confusable schemas, but for TRAINING, not inference-time.\\\\n    Our contribution is inference-time confusability-aware decomposition (training-free).\\\\n\\\\n- id: lost-in-middle-2024\\\\n  title: \\\\\\\"Lost in the Middle: How Language Models Use Long Contexts\\\\\\\"\\\\n  authors: [Nelson F. Liu et al.]\\\\n  year: 2024\\\\n  venue: TACL 2024\\\\n  url: https://arxiv.org/abs/2307.03172\\\\n  role: method-component\\\\n  relevance_note: >\\\\n    LLMs degrade when relevant info is in middle of long contexts (U-shaped attention).\\\\n    Motivates schema decomposition to reduce prompt length.\\\\n    No IE-specific follow-up found — opportunity for us to be first to connect this to IE.\\\\n\\\\n# =============================================================================\\\\n# ZERO-SHOT NER / RE BASELINES\\\\n# =============================================================================\\\\n\\\\n- id: self-improve-ner-2024\\\\n  title: \\\\\\\"Self-Improving for Zero-Shot Named Entity Recognition with Large Language Models\\\\\\\"\\\\n  year: 2024\\\\n  venue: NAACL 2024\\\\n  url: https://arxiv.org/abs/2311.08921\\\\n  role: background\\\\n  relevance_note: >\\\\n    Self-improving framework using LLM self-generated examples for zero-shot NER.\\\\n\\\\n- id: self-prompting-re-2024\\\\n  title: \\\\\\\"Unleashing the Power of LLMs in Zero-shot Relation Extraction via Self-Prompting\\\\\\\"\\\\n  year: 2024\\\\n  venue: EMNLP 2024 Findings\\\\n  url: https://arxiv.org/abs/2410.01154\\\\n  role: background\\\\n  relevance_note: >\\\\n    Three-stage self-prompting for zero-shot RE. Generates synthetic ICL samples.\\\\n    Training-free RE baseline.\\\\n\\\\n- id: reasoning-ner-2025\\\\n  title: \\\\\\\"A Reasoning Paradigm for Named Entity Recognition\\\\\\\"\\\\n  year: 2025\\\\n  venue: arXiv (Nov 2025)\\\\n  url: https://arxiv.org/abs/2511.11978\\\\n  role: background\\\\n  relevance_note: >\\\\n    CoT-based reasoning for NER. Outperforms GPT-4 by 12.3 F1 in zero-shot.\\\\n    Shifts NER from pattern matching to explicit reasoning. Strong zero-shot baseline.\\\\n\\\\n- id: nuner-2024\\\\n  title: \\\\\\\"NuNER: Entity Recognition Encoder Pre-training via LLM-Annotated Data\\\\\\\"\\\\n  authors: [Sergei Bogdanov et al., NuMind]\\\\n  year: 2024\\\\n  venue: EMNLP 2024\\\\n  url: https://arxiv.org/abs/2402.15343\\\\n  role: background\\\\n  relevance_note: >\\\\n    Contrastive pre-training on LLM-annotated data. Strong few-shot NER foundation model.\\\\n\\\\n# =============================================================================\\\\n# EVALUATION / BENCHMARKING\\\\n# =============================================================================\\\\n\\\\n- id: familiarity-2025\\\\n  title: \\\\\\\"Familiarity: Better Evaluation of Zero-Shot NER by Quantifying Label Shifts in Synthetic Training Data\\\\\\\"\\\\n  year: 2025\\\\n  venue: NAACL 2025\\\\n  url: https://arxiv.org/abs/2412.10121\\\\n  role: evaluation\\\\n  relevance_note: >\\\\n    \\\\\\\"Familiarity\\\\\\\" metric for label shift in synthetic NER data.\\\\n    Zero-shot NER scores overestimated due to train-eval label overlap.\\\\n    Quantifies semantic similarity between entity types — related to type confusability.\\\\n    KEY DIFF: measures evaluation bias, not extraction-time confusability.\\\\n\\\\n- id: guidex-2025\\\\n  title: \\\\\\\"GuideX: Guided Synthetic Data Generation for Zero-Shot Information Extraction\\\\\\\"\\\\n  authors: [Neil Deshpande et al.]\\\\n  year: 2025\\\\n  venue: ACL 2025 Findings\\\\n  url: https://arxiv.org/abs/2506.00649\\\\n  role: evaluation\\\\n  relevance_note: >\\\\n    Auto-generates domain-specific schemas + guidelines + synthetic labels.\\\\n    SOTA on 7 zero-shot NER benchmarks (+7 F1). Strong baseline.\\\\n\\\\n# =============================================================================\\\\n# SURVEYS\\\\n# =============================================================================\\\\n\\\\n- id: llm4ie-survey-2024\\\\n  title: \\\\\\\"Large Language Models for Generative Information Extraction: A Survey\\\\\\\"\\\\n  authors: [Derong Xu et al.]\\\\n  year: 2024\\\\n  venue: Frontiers of Computer Science\\\\n  url: https://arxiv.org/abs/2312.17617\\\\n  role: background\\\\n  relevance_note: >\\\\n    Comprehensive survey of LLM-based IE covering prompting, fine-tuning, benchmarks.\\\\n\\\\n- id: knowcoder-2024\\\\n  title: \\\\\\\"KnowCoder: Coding Structured Knowledge into LLMs for Universal IE\\\\\\\"\\\\n  year: 2024\\\\n  venue: ACL 2024\\\\n  url: https://arxiv.org/abs/2403.07969\\\\n  role: background\\\\n  relevance_note: >\\\\n    Encodes schema knowledge via code structures into LLM.\\\\n    Related to code-based schema representation.\\\\n\\\\n- id: slot-2025\\\\n  title: \\\\\\\"SLOT: Structuring the Output of Large\\\\n\\\\n... [截断: 省略 6972 字符，传 max_chars=0 获取完整内容]\\\", \\\"total_chars\\\": 18972, \\\"truncated\\\": true}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/literature_map.yaml\", \"content\": \"# Literature Map for schema-dag-extraction\\n# Updated: 2026-05-15\\n# Paper: Multi-channel Degradation Model + SDGD Framework for Training-free LLM IE\\n\\n# =============================================================================\\n# DIRECT COMPETITORS — schema decomposition for LLM-based IE\\n# =============================================================================\\n\\n- id: llm-pee-2025\\n  title: \\\"Towards Event Extraction with Massive Types: LLM-based Collaborative Annotation and Partitioning Extraction\\\"\\n  year: 2025\\n  venue: arXiv\\n  url: https://arxiv.org/abs/2503.02628\\n  role: direct-competitor\\n  relevance_note: >\\n    Similarity-based type recall + type-partitioning prompting for massive event types.\\n    Divides candidate types into partitions to reduce prompt length.\\n    +5.4% event detection, +6.1% argument extraction, +12.9% F1 over mainstream LLMs zero-shot.\\n    KEY DIFF: partitions by similarity-based recall, NOT confusability-aware.\\n    Our DAG decomposition is confusability-driven, not just similarity-driven.\\n\\n- id: parse-2025\\n  title: \\\"PARSE: LLM Driven Schema Optimization for Reliable Entity Extraction\\\"\\n  authors: [Anubhav Shrimal, Aryan Jain, Soumyajit Chowdhury, Promod Yenigalla]\\n  year: 2025\\n  venue: EMNLP 2025 Industry\\n  url: https://arxiv.org/abs/2510.08623\\n  role: direct-competitor\\n  relevance_note: >\\n    ARCHITECT autonomously rewrites JSON schemas for LLM consumption.\\n    SCOPE uses reflection-based extraction with guardrails. +64.7% on SWDE.\\n    Treats schema optimization as black-box LLM rewriting, not principled decomposition.\\n    Does NOT model type confusability explicitly.\\n\\n- id: dee-2024\\n  title: \\\"Decompose, Enrich, and Extract! Schema-aware Event Extraction using LLMs\\\"\\n  year: 2024\\n  venue: arXiv\\n  url: https://arxiv.org/abs/2406.01045\\n  role: direct-competitor\\n  relevance_note: >\\n    Decomposes event extraction into detection + argument extraction.\\n    Dynamic schema-aware RAG for augmented prompts.\\n    KEY DIFF: task-level decomposition (detection vs argument), not schema-level type decomposition.\\n\\n- id: crossagentie-2025\\n  title: \\\"CROSSAGENTIE: Cross-Type and Cross-Task Multi-Agent LLM Collaboration for Zero-Shot IE\\\"\\n  authors: [Meng Lu, Yuzhang Xie, Zhenyu Bi, Shuxiang Cao, Xuan Wang]\\n  year: 2025\\n  venue: ACL 2025 Findings\\n  url: https://aclanthology.org/2025.findings-acl.718/\\n  role: direct-competitor\\n  relevance_note: >\\n    Multi-agent: intra-group cross-type debate (resolves entity-label conflicts)\\n    + inter-group cross-task debate (NER↔RE mutual refinement).\\n    ⚠️ MODERATE NOVELTY CONCERN: cross-type debate explicitly addresses type confusion.\\n    KEY DIFF: reactive debate to resolve confusion post-hoc vs our proactive decomposition to prevent it.\\n    Must clearly differentiate in paper.\\n\\n- id: dlisc-2025\\n  title: \\\"Effective and Efficient Schema-aware Information Extraction Using On-Device LLMs\\\"\\n  year: 2025\\n  venue: arXiv (May 2025)\\n  url: https://arxiv.org/abs/2505.14992\\n  role: direct-competitor\\n  relevance_note: >\\n    Dual-LoRA with Incremental Schema Caching.\\n    Identification LoRA retrieves relevant schemas, Extraction LoRA performs IE.\\n    Focus on efficiency for on-device LLMs, not confusability analysis.\\n\\n- id: spt-2025\\n  title: \\\"Schema as Parameterized Tools for Universal Information Extraction\\\"\\n  year: 2025\\n  venue: arXiv (June 2025)\\n  url: https://arxiv.org/abs/2506.01276\\n  role: direct-competitor\\n  relevance_note: >\\n    Treats schemas as parameterized tools for LLM tool-calling.\\n    Schema retrieval + generation + infilling. Novel schema-LLM interface.\\n    Does not address type confusability.\\n\\n- id: zeroner-2025\\n  title: \\\"ZeroNER: Fueling Zero-Shot NER via Entity Type Descriptions\\\"\\n  year: 2025\\n  venue: ACL 2025 Findings\\n  url: https://aclanthology.org/2025.findings-acl.805/\\n  role: direct-competitor\\n  relevance_note: >\\n    Description-driven: LLM supervision → BERT student for unseen types.\\n    +16% F1 over LLMs on hard zero-shot. Leverages type descriptions.\\n    Related to how schema semantics affect extraction quality.\\n\\n- id: cmas-ner-2025\\n  title: \\\"A Cooperative Multi-Agent Framework for Zero-Shot Named Entity Recognition\\\"\\n  year: 2025\\n  venue: TheWebConf 2025\\n  url: https://dl.acm.org/doi/10.1145/3696410.3714923\\n  role: direct-competitor\\n  relevance_note: >\\n    Multi-agent collective intelligence for zero-shot NER.\\n    Addresses context correlation and indiscriminate demonstration problems.\\n    Outperforms on 6 benchmarks including domain-specific and general-domain.\\n\\n# =============================================================================\\n# METHOD COMPONENTS — techniques we build upon or relate to\\n# =============================================================================\\n\\n- id: uniner-2024\\n  title: \\\"UniversalNER: Targeted Distillation from Large Language Models for Open NER\\\"\\n  authors: [Wenxuan Zhou et al.]\\n  year: 2024\\n  venue: ICLR 2024\\n  url: https://arxiv.org/abs/2308.03279\\n  role: method-component\\n  relevance_note: >\\n    Instruction-tuning on ChatGPT-generated NER data. 43 datasets, 9 domains, 13K+ types.\\n    UniNER-7B outperforms ChatGPT by 7 F1 points.\\n    Important baseline for universal NER and schema-at-scale challenges.\\n\\n- id: gollie-2024\\n  title: \\\"GoLLIE: Annotation Guidelines Following Large Language Model for Information Extraction\\\"\\n  authors: [Oscar Sainz et al.]\\n  year: 2024\\n  venue: ICLR 2024\\n  url: https://hitz-zentroa.github.io/GoLLIE/\\n  role: method-component\\n  relevance_note: >\\n    Code-style schema definitions + annotation guideline following.\\n    Strong zero-shot on unseen IE tasks. Code-Llama based.\\n    Baseline for guideline-driven schema representation.\\n\\n- id: gliner-2024\\n  title: \\\"GLiNER: Generalist Model for Named Entity Recognition using Bidirectional Transformer\\\"\\n  authors: [Urchade Zaratiana et al.]\\n  year: 2024\\n  venue: NAACL 2024\\n  url: https://arxiv.org/abs/2311.08526\\n  role: method-component\\n  relevance_note: >\\n    Compact bidirectional encoder for zero-shot NER with parallel extraction.\\n    Outperforms InstructUIE and larger models. Non-LLM competitive baseline.\\n\\n- id: gliner2-2025\\n  title: \\\"GLiNER2: Efficient Multi-Task IE System with Schema-Driven Interface\\\"\\n  authors: [Urchade Zaratiana et al.]\\n  year: 2025\\n  venue: EMNLP 2025 Demo\\n  url: https://arxiv.org/abs/2507.18546\\n  role: method-component\\n  relevance_note: >\\n    Extends GLiNER to multi-task IE (NER+RE+classification). 205M params, CPU-efficient.\\n    Schema-driven interface. Shows schema approach scales to multi-task.\\n\\n- id: kggen-2025\\n  title: \\\"KGGen: Extracting Knowledge Graphs from Plain Text with Language Models\\\"\\n  authors: [Mo et al.]\\n  year: 2025\\n  venue: NeurIPS 2025\\n  url: https://arxiv.org/abs/2502.09956\\n  role: method-component\\n  relevance_note: >\\n    Two-stage decomposition: entities first, then relations.\\n    Entity clustering/deduplication to reduce graph sparsity.\\n    Schema decomposition approach for KG construction.\\n\\n- id: code4uie-2024\\n  title: \\\"Retrieval-Augmented Code Generation for Universal Information Extraction\\\"\\n  authors: [Yucan Guo et al.]\\n  year: 2024\\n  venue: NeurIPS 2024 Workshop\\n  url: https://arxiv.org/abs/2311.02962\\n  role: method-component\\n  relevance_note: >\\n    Python class-based schema definitions + RAG for code generation.\\n    Unified code-style schema for all IE tasks.\\n\\n- id: iepile-2024\\n  title: \\\"IEPile: Unearthing Large-Scale Schema-Based Information Extraction Corpus\\\"\\n  authors: [Guanzheng Chen et al., ZJU NLP]\\n  year: 2024\\n  venue: ACL 2024\\n  url: https://arxiv.org/abs/2402.14710\\n  role: method-component\\n  relevance_note: >\\n    0.32B token bilingual IE corpus. Hard negative schema construction =\\n    semantically proximate schemas to train type discrimination.\\n    ⚠️ RELATED: hard negatives ≈ confusable schemas, but for TRAINING, not inference-time.\\n    Our contribution is inference-time confusability-aware decomposition (training-free).\\n\\n- id: lost-in-middle-2024\\n  title: \\\"Lost in the Middle: How Language Models Use Long Contexts\\\"\\n  authors: [Nelson F. Liu et al.]\\n  year: 2024\\n  venue: TACL 2024\\n  url: https://arxiv.org/abs/2307.03172\\n  role: method-component\\n  relevance_note: >\\n    LLMs degrade when relevant info is in middle of long contexts (U-shaped attention).\\n    Motivates schema decomposition to reduce prompt length.\\n    No IE-specific follow-up found — opportunity for us to be first to connect this to IE.\\n\\n# =============================================================================\\n# ZERO-SHOT NER / RE BASELINES\\n# =============================================================================\\n\\n- id: self-improve-ner-2024\\n  title: \\\"Self-Improving for Zero-Shot Named Entity Recognition with Large Language Models\\\"\\n  year: 2024\\n  venue: NAACL 2024\\n  url: https://arxiv.org/abs/2311.08921\\n  role: background\\n  relevance_note: >\\n    Self-improving framework using LLM self-generated examples for zero-shot NER.\\n\\n- id: self-prompting-re-2024\\n  title: \\\"Unleashing the Power of LLMs in Zero-shot Relation Extraction via Self-Prompting\\\"\\n  year: 2024\\n  venue: EMNLP 2024 Findings\\n  url: https://arxiv.org/abs/2410.01154\\n  role: background\\n  relevance_note: >\\n    Three-stage self-prompting for zero-shot RE. Generates synthetic ICL samples.\\n    Training-free RE baseline.\\n\\n- id: reasoning-ner-2025\\n  title: \\\"A Reasoning Paradigm for Named Entity Recognition\\\"\\n  year: 2025\\n  venue: arXiv (Nov 2025)\\n  url: https://arxiv.org/abs/2511.11978\\n  role: background\\n  relevance_note: >\\n    CoT-based reasoning for NER. Outperforms GPT-4 by 12.3 F1 in zero-shot.\\n    Shifts NER from pattern matching to explicit reasoning. Strong zero-shot baseline.\\n\\n- id: nuner-2024\\n  title: \\\"NuNER: Entity Recognition Encoder Pre-training via LLM-Annotated Data\\\"\\n  authors: [Sergei Bogdanov et al., NuMind]\\n  year: 2024\\n  venue: EMNLP 2024\\n  url: https://arxiv.org/abs/2402.15343\\n  role: background\\n  relevance_note: >\\n    Contrastive pre-training on LLM-annotated data. Strong few-shot NER foundation model.\\n\\n# =============================================================================\\n# EVALUATION / BENCHMARKING\\n# =============================================================================\\n\\n- id: familiarity-2025\\n  title: \\\"Familiarity: Better Evaluation of Zero-Shot NER by Quantifying Label Shifts in Synthetic Training Data\\\"\\n  year: 2025\\n  venue: NAACL 2025\\n  url: https://arxiv.org/abs/2412.10121\\n  role: evaluation\\n  relevance_note: >\\n    \\\"Familiarity\\\" metric for label shift in synthetic NER data.\\n    Zero-shot NER scores overestimated due to train-eval label overlap.\\n    Quantifies semantic similarity between entity types — related to type confusability.\\n    KEY DIFF: measures evaluation bias, not extraction-time confusability.\\n\\n- id: guidex-2025\\n  title: \\\"GuideX: Guided Synthetic Data Generation for Zero-Shot Information Extraction\\\"\\n  authors: [Neil Deshpande et al.]\\n  year: 2025\\n  venue: ACL 2025 Findings\\n  url: https://arxiv.org/abs/2506.00649\\n  role: evaluation\\n  relevance_note: >\\n    Auto-generates domain-specific schemas + guidelines + synthetic labels.\\n    SOTA on 7 zero-shot NER benchmarks (+7 F1). Strong baseline.\\n\\n# =============================================================================\\n# SURVEYS\\n# =============================================================================\\n\\n- id: llm4ie-survey-2024\\n  title: \\\"Large Language Models for Generative Information Extraction: A Survey\\\"\\n  authors: [Derong Xu et al.]\\n  year: 2024\\n  venue: Frontiers of Computer Science\\n  url: https://arxiv.org/abs/2312.17617\\n  role: background\\n  relevance_note: >\\n    Comprehensive survey of LLM-based IE covering prompting, fine-tuning, benchmarks.\\n\\n- id: knowcoder-2024\\n  title: \\\"KnowCoder: Coding Structured Knowledge into LLMs for Universal IE\\\"\\n  year: 2024\\n  venue: ACL 2024\\n  url: https://arxiv.org/abs/2403.07969\\n  role: background\\n  relevance_note: >\\n    Encodes schema knowledge via code structures into LLM.\\n    Related to code-based schema representation.\\n\\n- id: slot-2025\\n  title: \\\"SLOT: Structuring the Output of Large\\n\\n... [截断: 省略 6972 字符，传 max_chars=0 获取完整内容]\", \"total_chars\": 18972, \"truncated\": true}, \"error\": null, \"metadata\": {}}"
    }
  },
  "sourceToolAssistantUUID": "e630bb63-2ba0-4c4e-b189-59989e9ab1b9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/reviewer_efaaa6bc",
  "sessionId": "f59020b4-1c0e-4081-9cb3-293eac3560ff",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-15T17:15:45.374Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01JxkVgisQyUNCEr4q8Mc6Ey`</summary>

```json
{
  "project": "schema-dag-extraction",
  "file": "paper_framing.md",
  "max_chars": 12000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d03f1be1-c1c5-4bf3-94c3-9ecf767a0b66",
  "isSidechain": false,
  "requestId": "req_011Cb4jQc1wxpappYiS3eeJs",
  "type": "assistant",
  "uuid": "f794a1d7-e1db-4362-b421-b12ed1551611",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/reviewer_efaaa6bc",
  "sessionId": "f59020b4-1c0e-4081-9cb3-293eac3560ff",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01G1gt8poiUhy32oNnwZUFyY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5722,
      "cache_read_input_tokens": 31685,
      "output_tokens": 534,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5722,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 534,
          "cache_read_input_tokens": 31685,
          "cache_creation_input_tokens": 5722,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5722
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

_source line 24 · 2026-05-15T17:15:45.384Z_

<details><summary>↩ Tool result · `toolu_01JxkVgisQyUNCEr4q8Mc6Ey`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/paper_framing.md\", \"content\": \"# Paper Framing — schema-dag-extraction\\n\\n## Target Venue\\n- Primary: EMNLP 2026 Main (ARR May 25 cycle)\\n- Commitment deadline: August 2, 2026\\n- Fallback: EMNLP 2026 Findings (same ARR cycle, commitment August 26)\\n- Deadline: ARR May 25, 2026 (10 days from today)\\n\\n## Core Claims (2 claims) — Revised per D019\\n\\n1. **Confusability Independence**: Type confusability independently predicts extraction quality degradation in training-free LLM IE, beyond what type count alone explains. The signal is strongest and most robust at the **type-pair level** (pairwise SCS → confusion), validated across NER (Few-NERD), RE (FewRel), and ED (MAVEN with MiniLM). Per-type aggregation (mean BCS) introduces a centrality confound in semantically homogeneous schemas. The effect amplifies with schema complexity (3.4× between 16-type and 80-type schemas). Evidence required: (a) significant pairwise SCS-confusion correlation on >=2 datasets, (b) BCS-controlled accuracy gap on FewRel, (c) >=2 models.\\n\\n2. **Multi-Channel Degradation**: Count and confusability degrade extraction through orthogonal channels -- count causes entity omission (recall decline), while confusability causes type confusion errors (correct spans labeled with wrong types). Cross-task validated: NER IntraSub ρ=1.0, RE IntraSub ρ=0.954. Evidence required: error taxonomy showing differential error types per channel, monotonic trends in separate metrics.\\n\\n~~3. **SDGD Effectiveness**~~ — **DROPPED (D019)**: SDGD-zero v1 F1=0.251, v2 F1=0.241, both far below single-pass baseline 0.445. Merge amplification is an intrinsic challenge of schema decomposition that merge strategies (union+dedup, confidence-gated) cannot resolve. **Discussed as negative result + future work direction** — \\\"why naive decomposition fails\\\" is itself a contribution.\\n\\n## Story Spine — Revised per D012\\n\\n- **Problem**: Training-free LLM IE degrades severely on complex schemas (20-60 F1 gap vs supervised). All existing decomposition approaches operate on unvalidated assumptions about WHAT makes schemas complex for LLMs.\\n\\n- **Existing approaches & their gaps**: UniNER splits per-type (gains 3.3 F1 but loses cross-type context, no criterion for when to split). LLM-PEE uses similarity as implicit confusability proxy (never validated empirically). No prior work isolates confusability from count, or characterizes when aggregated confusability measures lose signal.\\n\\n- **Our framing**: We conduct the first controlled empirical study isolating type confusability from type count in training-free LLM IE across three tasks (NER, RE, ED). We discover: (1) a multi-channel degradation model (count→recall, confusability→type confusion), (2) pairwise type confusability is a robust cross-task signal that amplifies with schema complexity, (3) per-type aggregation of confusability is confounded by type centrality in homogeneous schemas. We further show that naive confusability-aware decomposition (SDGD) fails due to merge amplification — a structural challenge that points to calibration-based approaches as future work.\\n\\n- **Three-task validation**:\\n  - NER (Few-NERD, 66 types, cross-domain): Pairwise r=0.112 [0.076, 0.156] (n=1953), per-type ρ=-0.293 [-0.492, -0.054] (p=0.02), 10-28x confusion ratio\\n  - RE (FewRel, 80 relations, cross-domain): BCS-controlled Δ=-31.2pp (80-rel formal); count curve acc 85.7%→50.4%; BCS effect scales 3.4x vs 16-rel\\n  - ED (MAVEN, 168 event types, same-domain): Pairwise MiniLM r=0.120 (p≈0); per-type positive (centrality confound case study)\\n\\n- **Headline result template**: \\\"Pairwise type confusability independently predicts extraction degradation across NER, RE, and ED tasks (r=0.11-0.13, all CIs exclude zero), with 10-28x more type confusion errors in high-confusability batches. The effect amplifies with schema complexity: 3.4× stronger BCS effect on 80-type vs 16-type schemas (Δ=-31.2pp vs -9.1pp). On semantically homogeneous schemas, per-type aggregation obscures the signal through centrality confounding, but pairwise confusability remains valid.\\\"\\n\\n## Core Insight — Multi-Channel Degradation + Pairwise Robustness\\n\\nSchema-induced degradation in LLM IE is not a single phenomenon but a multi-channel process:\\n- **Channel 1 (Count -> Recall)**: More types in the prompt → attention dilution → entities missed. Monotonic, near-linear. Addressable by reducing batch size.\\n- **Channel 2 (Confusability -> Type Confusion)**: Semantically similar co-present types → interference during type assignment → correct entities labeled with wrong types. Addressable by separating confusable types into different batches.\\n\\nThese channels are orthogonal and independently addressable.\\n\\n**Pairwise vs Aggregated Confusability**:\\n- **Pairwise confusability** (SCS between type pairs) is robust across all tasks and schema types. Validated on Few-NERD (Qwen3, r=0.112 [0.076, 0.156]) and MAVEN (MiniLM, r=0.129 [0.104, 0.156]). SCS validated as effective confusion proxy: Qwen3 ρ=0.168 (p=7e-14), MiniLM ρ=0.306 nonzero-only (p=5e-6).\\n- **Per-type aggregation** (mean BCS = average pairwise similarity to all other types) introduces a centrality confound: in semantically homogeneous schemas (MAVEN), types with many semantic neighbors are central, well-represented types that LLMs extract well → positive correlation (high mean BCS → high F1), masking the pairwise confusability signal.\\n- **SDGD operates at pairwise level**, directly using the validated signal to construct the confusability graph for decomposition. It avoids the aggregation confound entirely.\\n\\n## Evidence Hierarchy (D012)\\n\\n### Tier 1: PRIMARY — Pairwise SCS → Confusion\\n\\nThe cleanest evidence. Directly measures: are semantically similar type pairs more often confused?\\n\\n**Few-NERD (NER)** — Qwen3 embeddings:\\n- Pearson r=0.112 [0.076, 0.156] (n=1953 type pairs) — corrected via bootstrap recomputation\\n- Nonzero-only Spearman ρ=0.272 (p=5e-5)\\n- Top confused pairs are all high-BCS semantic neighbors (person-other ↔ person-politician, BCS=0.934)\\n- Immune to type frequency confound (operates at type-pair level)\\n\\n**MAVEN (ED)** — MiniLM embeddings:\\n- Pearson r=+0.129 [0.104, 0.156] (n=11026 type pairs) — corrected via bootstrap\\n- Nonzero-only Spearman ρ=+0.191 (p<0.001)\\n- Cross-task replication on same-domain schema\\n- Note: Qwen3 pairwise not significant on MAVEN (r=-0.007, p=0.41) — embedding choice matters for pairwise signal in homogeneous schemas\\n\\n### Tier 2: STRONG SECONDARY — FewRel Cross-Task Replication\\n\\nLarge effect size, cross-task (RE), scaling with schema complexity:\\n\\n**Formal 80-rel study** (exp_fewrel_formal_80rel):\\n- Count curve: acc 85.7% (count=1) → 50.4% (count=80), BCS 0→0.97\\n- BCS-controlled: count_8 low-BCS 82.3% vs high-BCS 51.0% (Δ=-31.2pp)\\n- BCS-controlled: count_16 low-BCS 82.8% vs high-BCS 51.6% (Δ=-31.2pp)\\n- **Scaling**: vs 16-rel, degradation 2.8x (35.3pp vs 12.6pp), BCS effect 3.4x (-31.2pp vs -9.1pp)\\n\\n**16-rel sanity check** (exp_fewrel_formal):\\n- count_8: low-BCS 88.9% vs high-BCS 79.8% (Δ=-9.1pp)\\n\\n**Pilot extreme batches** (fewrel_pilot, MiniLM):\\n- count_4: Δ=-20.9pp, count_8: Δ=-50.0pp, count_16: Δ=-48.6pp\\n\\nKey insight: confusability effect amplifies with schema size — direct evidence for multi-channel degradation scaling\\n\\n### Tier 3: SUPPORTING — Few-NERD Per-type Analysis\\n\\nBridges pairwise and batch-level, demonstrates per-type signal in cross-domain schema:\\n- Spearman ρ=-0.293 (p=0.020, n=63 types, freq≥5) — Qwen3 embeddings\\n- Partial r=-0.200 (p=0.116) controlling for log-frequency\\n- Quartile comparison: high-BCS types F1=0.228 vs low-BCS F1=0.310 (Δ=-8.2pp)\\n- BCS-frequency uncorrelated at type level (r=0.042, p=0.74)\\n- MiniLM per-type: ρ≈0 (p=0.97) — extraction model alignment required for per-type signal\\n\\n### Tier 4: DISCUSSION — MAVEN Per-type Centrality Confound\\n\\nMethodological case study on when aggregated confusability measures fail:\\n- Qwen3 per-type: ρ=+0.189 (p=0.021) — OPPOSITE direction\\n- MiniLM per-type: ρ=+0.208 (p=0.011) — ALSO positive, ruling out embedding compression as sole explanation\\n- Both embeddings agree: positive direction on MAVEN is an intrinsic property of the type structure\\n- Explanation: in homogeneous schemas, mean BCS conflates confusability with type centrality (types with many semantic neighbors → common/central types → higher F1)\\n- This is stronger than \\\"domain boundary\\\" — it identifies the specific mechanism (aggregation confound) rather than just the boundary condition\\n\\n### Tier 5: MECHANISTIC — Error Taxonomy (Cross-Task)\\n\\nIntraSub rate monotonically increases with BCS on both NER and RE:\\n\\n**Few-NERD (NER, exp-007)**: IntraSub 0%→1.6%→10.6%→49.4%, ρ=1.0\\n**FewRel 80-rel (RE)**: IntraSub 0%→4.2%→13.0%→20.3%→32.3%, ρ=0.954 (p=0.0, n=154 batches)\\n- extra_sub=0 on both tasks — type confusion is purely intra-batch phenomenon\\n- Same mechanism, different absolute magnitudes — consistent with cross-task expectations\\n\\nAdditional from extreme batch design:\\n- Extreme batches: high-BCS 10-28x more type confusion errors vs low-BCS\\n- Random batches: 1.7-2.4x ratio (still significant, smaller effect)\\n\\n## Embedding Ablation (D010)\\n\\n2×3 matrix: {Qwen3, MiniLM} × {Few-NERD, FewRel, MAVEN}\\n\\n### Per-type (Layer 2)\\n| | Few-NERD | FewRel | MAVEN |\\n|---|---|---|---|\\n| Qwen3 | ρ=-0.293 ✓ | pending | ρ=+0.189 ✗ |\\n| MiniLM | ρ≈0 ✗ | Δ=21-50pp ✓ | ρ=+0.208 ✗ |\\n\\n### Pairwise (Layer 1)\\n| | Few-NERD | MAVEN |\\n|---|---|---|\\n| Qwen3 | r=0.112 [0.076,0.156] ✓ | r=-0.007 ✗ |\\n| MiniLM | — | r=+0.129 [0.104,0.156] ✓ |\\n\\n### SCS→Empirical Confusion Validation (exp-015 fast)\\n| | Qwen3 | MiniLM |\\n|---|---|---|\\n| All pairs ρ | 0.168 (p=7e-14) ✓ | 0.144 (p=2e-10) ✓ |\\n| Nonzero-only ρ | 0.272 (p=5e-5) | 0.306 (p=5e-6) ✓ |\\n\\n**Interpretation**: No single embedding dominates. Extraction-model embeddings (Qwen3) capture per-type confusability in cross-domain schemas. Generic embeddings (MiniLM) capture pairwise confusability in same-domain schemas. SDGD should use task-appropriate embeddings; SDGD-cal (empirical confusion) bypasses embedding choice entirely.\\n\\n## Venue Fit Risks\\n\\n- **\\\"Just an empirical study\\\"**: Mitigated by SDGD as direct operationalization. Controlled experimental design parallels \\\"Lost in the Middle\\\" (TACL 2024).\\n- **Training-free IE relevance**: Cite deployment scenarios — clinical, regulatory, multilingual.\\n- **Multi-model generalizability**: Qwen3-32B primary + LLaMA-3.3-70B (exp-012).\\n- **MAVEN doesn't support hypothesis?**: Pairwise MiniLM does support it. Per-type centrality confound is methodological contribution, not failure.\\n- **Embedding sensitivity**: 2×3 ablation matrix is itself a contribution — characterizes when which proxy works.\\n\\n## Anticipated Reviewer Concerns\\n\\n| Concern | Response Strategy | Experiment |\\n|---------|------------------|------------|\\n| Only one model | LLaMA-3.3-70B replication | exp-012 |\\n| Cross-task replication | Pairwise: Few-NERD ✓ + MAVEN MiniLM ✓. Batch: FewRel ✓. Three tasks. | exp-002, exp-004, fewrel |\\n| No practical method | SDGD framework (-zero, -cal) | exp-008 to exp-011 |\\n| Confusability measure validity | Embedding ablation (D010) + pairwise vs per-type analysis | D010, exp-015 |\\n| Effect size small | Pairwise r=0.12-0.16 + FewRel Δ=21-50pp + confusion ratio 10-28x | multiple |\\n| MAVEN per-type opposite | Centrality confound analysis; pairwise still works | MAVEN MiniLM |\\n| Embedding choice matters? | 2×3 ablation table; SDGD-cal bypasses embedding entirely | D010 |\\n| Why not per-type splitting? | SDGD vs per-type vs random ablation | exp-013, exp-014 |\\n| Latency overhead | Report API calls and wall-clock time | exp-008 |\\n\", \"total_chars\": 11568, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f794a1d7-e1db-4362-b421-b12ed1551611",
  "isSidechain": false,
  "promptId": "b593ab42-40aa-4651-8f99-a82b6d6b969a",
  "type": "user",
  "uuid": "2fe3fa4b-a578-41ab-a460-eaba2a6168d0",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/paper_framing.md\\\", \\\"content\\\": \\\"# Paper Framing — schema-dag-extraction\\\\n\\\\n## Target Venue\\\\n- Primary: EMNLP 2026 Main (ARR May 25 cycle)\\\\n- Commitment deadline: August 2, 2026\\\\n- Fallback: EMNLP 2026 Findings (same ARR cycle, commitment August 26)\\\\n- Deadline: ARR May 25, 2026 (10 days from today)\\\\n\\\\n## Core Claims (2 claims) — Revised per D019\\\\n\\\\n1. **Confusability Independence**: Type confusability independently predicts extraction quality degradation in training-free LLM IE, beyond what type count alone explains. The signal is strongest and most robust at the **type-pair level** (pairwise SCS → confusion), validated across NER (Few-NERD), RE (FewRel), and ED (MAVEN with MiniLM). Per-type aggregation (mean BCS) introduces a centrality confound in semantically homogeneous schemas. The effect amplifies with schema complexity (3.4× between 16-type and 80-type schemas). Evidence required: (a) significant pairwise SCS-confusion correlation on >=2 datasets, (b) BCS-controlled accuracy gap on FewRel, (c) >=2 models.\\\\n\\\\n2. **Multi-Channel Degradation**: Count and confusability degrade extraction through orthogonal channels -- count causes entity omission (recall decline), while confusability causes type confusion errors (correct spans labeled with wrong types). Cross-task validated: NER IntraSub ρ=1.0, RE IntraSub ρ=0.954. Evidence required: error taxonomy showing differential error types per channel, monotonic trends in separate metrics.\\\\n\\\\n~~3. **SDGD Effectiveness**~~ — **DROPPED (D019)**: SDGD-zero v1 F1=0.251, v2 F1=0.241, both far below single-pass baseline 0.445. Merge amplification is an intrinsic challenge of schema decomposition that merge strategies (union+dedup, confidence-gated) cannot resolve. **Discussed as negative result + future work direction** — \\\\\\\"why naive decomposition fails\\\\\\\" is itself a contribution.\\\\n\\\\n## Story Spine — Revised per D012\\\\n\\\\n- **Problem**: Training-free LLM IE degrades severely on complex schemas (20-60 F1 gap vs supervised). All existing decomposition approaches operate on unvalidated assumptions about WHAT makes schemas complex for LLMs.\\\\n\\\\n- **Existing approaches & their gaps**: UniNER splits per-type (gains 3.3 F1 but loses cross-type context, no criterion for when to split). LLM-PEE uses similarity as implicit confusability proxy (never validated empirically). No prior work isolates confusability from count, or characterizes when aggregated confusability measures lose signal.\\\\n\\\\n- **Our framing**: We conduct the first controlled empirical study isolating type confusability from type count in training-free LLM IE across three tasks (NER, RE, ED). We discover: (1) a multi-channel degradation model (count→recall, confusability→type confusion), (2) pairwise type confusability is a robust cross-task signal that amplifies with schema complexity, (3) per-type aggregation of confusability is confounded by type centrality in homogeneous schemas. We further show that naive confusability-aware decomposition (SDGD) fails due to merge amplification — a structural challenge that points to calibration-based approaches as future work.\\\\n\\\\n- **Three-task validation**:\\\\n  - NER (Few-NERD, 66 types, cross-domain): Pairwise r=0.112 [0.076, 0.156] (n=1953), per-type ρ=-0.293 [-0.492, -0.054] (p=0.02), 10-28x confusion ratio\\\\n  - RE (FewRel, 80 relations, cross-domain): BCS-controlled Δ=-31.2pp (80-rel formal); count curve acc 85.7%→50.4%; BCS effect scales 3.4x vs 16-rel\\\\n  - ED (MAVEN, 168 event types, same-domain): Pairwise MiniLM r=0.120 (p≈0); per-type positive (centrality confound case study)\\\\n\\\\n- **Headline result template**: \\\\\\\"Pairwise type confusability independently predicts extraction degradation across NER, RE, and ED tasks (r=0.11-0.13, all CIs exclude zero), with 10-28x more type confusion errors in high-confusability batches. The effect amplifies with schema complexity: 3.4× stronger BCS effect on 80-type vs 16-type schemas (Δ=-31.2pp vs -9.1pp). On semantically homogeneous schemas, per-type aggregation obscures the signal through centrality confounding, but pairwise confusability remains valid.\\\\\\\"\\\\n\\\\n## Core Insight — Multi-Channel Degradation + Pairwise Robustness\\\\n\\\\nSchema-induced degradation in LLM IE is not a single phenomenon but a multi-channel process:\\\\n- **Channel 1 (Count -> Recall)**: More types in the prompt → attention dilution → entities missed. Monotonic, near-linear. Addressable by reducing batch size.\\\\n- **Channel 2 (Confusability -> Type Confusion)**: Semantically similar co-present types → interference during type assignment → correct entities labeled with wrong types. Addressable by separating confusable types into different batches.\\\\n\\\\nThese channels are orthogonal and independently addressable.\\\\n\\\\n**Pairwise vs Aggregated Confusability**:\\\\n- **Pairwise confusability** (SCS between type pairs) is robust across all tasks and schema types. Validated on Few-NERD (Qwen3, r=0.112 [0.076, 0.156]) and MAVEN (MiniLM, r=0.129 [0.104, 0.156]). SCS validated as effective confusion proxy: Qwen3 ρ=0.168 (p=7e-14), MiniLM ρ=0.306 nonzero-only (p=5e-6).\\\\n- **Per-type aggregation** (mean BCS = average pairwise similarity to all other types) introduces a centrality confound: in semantically homogeneous schemas (MAVEN), types with many semantic neighbors are central, well-represented types that LLMs extract well → positive correlation (high mean BCS → high F1), masking the pairwise confusability signal.\\\\n- **SDGD operates at pairwise level**, directly using the validated signal to construct the confusability graph for decomposition. It avoids the aggregation confound entirely.\\\\n\\\\n## Evidence Hierarchy (D012)\\\\n\\\\n### Tier 1: PRIMARY — Pairwise SCS → Confusion\\\\n\\\\nThe cleanest evidence. Directly measures: are semantically similar type pairs more often confused?\\\\n\\\\n**Few-NERD (NER)** — Qwen3 embeddings:\\\\n- Pearson r=0.112 [0.076, 0.156] (n=1953 type pairs) — corrected via bootstrap recomputation\\\\n- Nonzero-only Spearman ρ=0.272 (p=5e-5)\\\\n- Top confused pairs are all high-BCS semantic neighbors (person-other ↔ person-politician, BCS=0.934)\\\\n- Immune to type frequency confound (operates at type-pair level)\\\\n\\\\n**MAVEN (ED)** — MiniLM embeddings:\\\\n- Pearson r=+0.129 [0.104, 0.156] (n=11026 type pairs) — corrected via bootstrap\\\\n- Nonzero-only Spearman ρ=+0.191 (p<0.001)\\\\n- Cross-task replication on same-domain schema\\\\n- Note: Qwen3 pairwise not significant on MAVEN (r=-0.007, p=0.41) — embedding choice matters for pairwise signal in homogeneous schemas\\\\n\\\\n### Tier 2: STRONG SECONDARY — FewRel Cross-Task Replication\\\\n\\\\nLarge effect size, cross-task (RE), scaling with schema complexity:\\\\n\\\\n**Formal 80-rel study** (exp_fewrel_formal_80rel):\\\\n- Count curve: acc 85.7% (count=1) → 50.4% (count=80), BCS 0→0.97\\\\n- BCS-controlled: count_8 low-BCS 82.3% vs high-BCS 51.0% (Δ=-31.2pp)\\\\n- BCS-controlled: count_16 low-BCS 82.8% vs high-BCS 51.6% (Δ=-31.2pp)\\\\n- **Scaling**: vs 16-rel, degradation 2.8x (35.3pp vs 12.6pp), BCS effect 3.4x (-31.2pp vs -9.1pp)\\\\n\\\\n**16-rel sanity check** (exp_fewrel_formal):\\\\n- count_8: low-BCS 88.9% vs high-BCS 79.8% (Δ=-9.1pp)\\\\n\\\\n**Pilot extreme batches** (fewrel_pilot, MiniLM):\\\\n- count_4: Δ=-20.9pp, count_8: Δ=-50.0pp, count_16: Δ=-48.6pp\\\\n\\\\nKey insight: confusability effect amplifies with schema size — direct evidence for multi-channel degradation scaling\\\\n\\\\n### Tier 3: SUPPORTING — Few-NERD Per-type Analysis\\\\n\\\\nBridges pairwise and batch-level, demonstrates per-type signal in cross-domain schema:\\\\n- Spearman ρ=-0.293 (p=0.020, n=63 types, freq≥5) — Qwen3 embeddings\\\\n- Partial r=-0.200 (p=0.116) controlling for log-frequency\\\\n- Quartile comparison: high-BCS types F1=0.228 vs low-BCS F1=0.310 (Δ=-8.2pp)\\\\n- BCS-frequency uncorrelated at type level (r=0.042, p=0.74)\\\\n- MiniLM per-type: ρ≈0 (p=0.97) — extraction model alignment required for per-type signal\\\\n\\\\n### Tier 4: DISCUSSION — MAVEN Per-type Centrality Confound\\\\n\\\\nMethodological case study on when aggregated confusability measures fail:\\\\n- Qwen3 per-type: ρ=+0.189 (p=0.021) — OPPOSITE direction\\\\n- MiniLM per-type: ρ=+0.208 (p=0.011) — ALSO positive, ruling out embedding compression as sole explanation\\\\n- Both embeddings agree: positive direction on MAVEN is an intrinsic property of the type structure\\\\n- Explanation: in homogeneous schemas, mean BCS conflates confusability with type centrality (types with many semantic neighbors → common/central types → higher F1)\\\\n- This is stronger than \\\\\\\"domain boundary\\\\\\\" — it identifies the specific mechanism (aggregation confound) rather than just the boundary condition\\\\n\\\\n### Tier 5: MECHANISTIC — Error Taxonomy (Cross-Task)\\\\n\\\\nIntraSub rate monotonically increases with BCS on both NER and RE:\\\\n\\\\n**Few-NERD (NER, exp-007)**: IntraSub 0%→1.6%→10.6%→49.4%, ρ=1.0\\\\n**FewRel 80-rel (RE)**: IntraSub 0%→4.2%→13.0%→20.3%→32.3%, ρ=0.954 (p=0.0, n=154 batches)\\\\n- extra_sub=0 on both tasks — type confusion is purely intra-batch phenomenon\\\\n- Same mechanism, different absolute magnitudes — consistent with cross-task expectations\\\\n\\\\nAdditional from extreme batch design:\\\\n- Extreme batches: high-BCS 10-28x more type confusion errors vs low-BCS\\\\n- Random batches: 1.7-2.4x ratio (still significant, smaller effect)\\\\n\\\\n## Embedding Ablation (D010)\\\\n\\\\n2×3 matrix: {Qwen3, MiniLM} × {Few-NERD, FewRel, MAVEN}\\\\n\\\\n### Per-type (Layer 2)\\\\n| | Few-NERD | FewRel | MAVEN |\\\\n|---|---|---|---|\\\\n| Qwen3 | ρ=-0.293 ✓ | pending | ρ=+0.189 ✗ |\\\\n| MiniLM | ρ≈0 ✗ | Δ=21-50pp ✓ | ρ=+0.208 ✗ |\\\\n\\\\n### Pairwise (Layer 1)\\\\n| | Few-NERD | MAVEN |\\\\n|---|---|---|\\\\n| Qwen3 | r=0.112 [0.076,0.156] ✓ | r=-0.007 ✗ |\\\\n| MiniLM | — | r=+0.129 [0.104,0.156] ✓ |\\\\n\\\\n### SCS→Empirical Confusion Validation (exp-015 fast)\\\\n| | Qwen3 | MiniLM |\\\\n|---|---|---|\\\\n| All pairs ρ | 0.168 (p=7e-14) ✓ | 0.144 (p=2e-10) ✓ |\\\\n| Nonzero-only ρ | 0.272 (p=5e-5) | 0.306 (p=5e-6) ✓ |\\\\n\\\\n**Interpretation**: No single embedding dominates. Extraction-model embeddings (Qwen3) capture per-type confusability in cross-domain schemas. Generic embeddings (MiniLM) capture pairwise confusability in same-domain schemas. SDGD should use task-appropriate embeddings; SDGD-cal (empirical confusion) bypasses embedding choice entirely.\\\\n\\\\n## Venue Fit Risks\\\\n\\\\n- **\\\\\\\"Just an empirical study\\\\\\\"**: Mitigated by SDGD as direct operationalization. Controlled experimental design parallels \\\\\\\"Lost in the Middle\\\\\\\" (TACL 2024).\\\\n- **Training-free IE relevance**: Cite deployment scenarios — clinical, regulatory, multilingual.\\\\n- **Multi-model generalizability**: Qwen3-32B primary + LLaMA-3.3-70B (exp-012).\\\\n- **MAVEN doesn't support hypothesis?**: Pairwise MiniLM does support it. Per-type centrality confound is methodological contribution, not failure.\\\\n- **Embedding sensitivity**: 2×3 ablation matrix is itself a contribution — characterizes when which proxy works.\\\\n\\\\n## Anticipated Reviewer Concerns\\\\n\\\\n| Concern | Response Strategy | Experiment |\\\\n|---------|------------------|------------|\\\\n| Only one model | LLaMA-3.3-70B replication | exp-012 |\\\\n| Cross-task replication | Pairwise: Few-NERD ✓ + MAVEN MiniLM ✓. Batch: FewRel ✓. Three tasks. | exp-002, exp-004, fewrel |\\\\n| No practical method | SDGD framework (-zero, -cal) | exp-008 to exp-011 |\\\\n| Confusability measure validity | Embedding ablation (D010) + pairwise vs per-type analysis | D010, exp-015 |\\\\n| Effect size small | Pairwise r=0.12-0.16 + FewRel Δ=21-50pp + confusion ratio 10-28x | multiple |\\\\n| MAVEN per-type opposite | Centrality confound analysis; pairwise still works | MAVEN MiniLM |\\\\n| Embedding choice matters? | 2×3 ablation table; SDGD-cal bypasses embedding entirely | D010 |\\\\n| Why not per-type splitting? | SDGD vs per-type vs random ablation | exp-013, exp-014 |\\\\n| Latency overhead | Report API calls and wall-clock time | exp-008 |\\\\n\\\", \\\"total_chars\\\": 11568, \\\"truncated\\\": false}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/paper_framing.md\", \"content\": \"# Paper Framing — schema-dag-extraction\\n\\n## Target Venue\\n- Primary: EMNLP 2026 Main (ARR May 25 cycle)\\n- Commitment deadline: August 2, 2026\\n- Fallback: EMNLP 2026 Findings (same ARR cycle, commitment August 26)\\n- Deadline: ARR May 25, 2026 (10 days from today)\\n\\n## Core Claims (2 claims) — Revised per D019\\n\\n1. **Confusability Independence**: Type confusability independently predicts extraction quality degradation in training-free LLM IE, beyond what type count alone explains. The signal is strongest and most robust at the **type-pair level** (pairwise SCS → confusion), validated across NER (Few-NERD), RE (FewRel), and ED (MAVEN with MiniLM). Per-type aggregation (mean BCS) introduces a centrality confound in semantically homogeneous schemas. The effect amplifies with schema complexity (3.4× between 16-type and 80-type schemas). Evidence required: (a) significant pairwise SCS-confusion correlation on >=2 datasets, (b) BCS-controlled accuracy gap on FewRel, (c) >=2 models.\\n\\n2. **Multi-Channel Degradation**: Count and confusability degrade extraction through orthogonal channels -- count causes entity omission (recall decline), while confusability causes type confusion errors (correct spans labeled with wrong types). Cross-task validated: NER IntraSub ρ=1.0, RE IntraSub ρ=0.954. Evidence required: error taxonomy showing differential error types per channel, monotonic trends in separate metrics.\\n\\n~~3. **SDGD Effectiveness**~~ — **DROPPED (D019)**: SDGD-zero v1 F1=0.251, v2 F1=0.241, both far below single-pass baseline 0.445. Merge amplification is an intrinsic challenge of schema decomposition that merge strategies (union+dedup, confidence-gated) cannot resolve. **Discussed as negative result + future work direction** — \\\"why naive decomposition fails\\\" is itself a contribution.\\n\\n## Story Spine — Revised per D012\\n\\n- **Problem**: Training-free LLM IE degrades severely on complex schemas (20-60 F1 gap vs supervised). All existing decomposition approaches operate on unvalidated assumptions about WHAT makes schemas complex for LLMs.\\n\\n- **Existing approaches & their gaps**: UniNER splits per-type (gains 3.3 F1 but loses cross-type context, no criterion for when to split). LLM-PEE uses similarity as implicit confusability proxy (never validated empirically). No prior work isolates confusability from count, or characterizes when aggregated confusability measures lose signal.\\n\\n- **Our framing**: We conduct the first controlled empirical study isolating type confusability from type count in training-free LLM IE across three tasks (NER, RE, ED). We discover: (1) a multi-channel degradation model (count→recall, confusability→type confusion), (2) pairwise type confusability is a robust cross-task signal that amplifies with schema complexity, (3) per-type aggregation of confusability is confounded by type centrality in homogeneous schemas. We further show that naive confusability-aware decomposition (SDGD) fails due to merge amplification — a structural challenge that points to calibration-based approaches as future work.\\n\\n- **Three-task validation**:\\n  - NER (Few-NERD, 66 types, cross-domain): Pairwise r=0.112 [0.076, 0.156] (n=1953), per-type ρ=-0.293 [-0.492, -0.054] (p=0.02), 10-28x confusion ratio\\n  - RE (FewRel, 80 relations, cross-domain): BCS-controlled Δ=-31.2pp (80-rel formal); count curve acc 85.7%→50.4%; BCS effect scales 3.4x vs 16-rel\\n  - ED (MAVEN, 168 event types, same-domain): Pairwise MiniLM r=0.120 (p≈0); per-type positive (centrality confound case study)\\n\\n- **Headline result template**: \\\"Pairwise type confusability independently predicts extraction degradation across NER, RE, and ED tasks (r=0.11-0.13, all CIs exclude zero), with 10-28x more type confusion errors in high-confusability batches. The effect amplifies with schema complexity: 3.4× stronger BCS effect on 80-type vs 16-type schemas (Δ=-31.2pp vs -9.1pp). On semantically homogeneous schemas, per-type aggregation obscures the signal through centrality confounding, but pairwise confusability remains valid.\\\"\\n\\n## Core Insight — Multi-Channel Degradation + Pairwise Robustness\\n\\nSchema-induced degradation in LLM IE is not a single phenomenon but a multi-channel process:\\n- **Channel 1 (Count -> Recall)**: More types in the prompt → attention dilution → entities missed. Monotonic, near-linear. Addressable by reducing batch size.\\n- **Channel 2 (Confusability -> Type Confusion)**: Semantically similar co-present types → interference during type assignment → correct entities labeled with wrong types. Addressable by separating confusable types into different batches.\\n\\nThese channels are orthogonal and independently addressable.\\n\\n**Pairwise vs Aggregated Confusability**:\\n- **Pairwise confusability** (SCS between type pairs) is robust across all tasks and schema types. Validated on Few-NERD (Qwen3, r=0.112 [0.076, 0.156]) and MAVEN (MiniLM, r=0.129 [0.104, 0.156]). SCS validated as effective confusion proxy: Qwen3 ρ=0.168 (p=7e-14), MiniLM ρ=0.306 nonzero-only (p=5e-6).\\n- **Per-type aggregation** (mean BCS = average pairwise similarity to all other types) introduces a centrality confound: in semantically homogeneous schemas (MAVEN), types with many semantic neighbors are central, well-represented types that LLMs extract well → positive correlation (high mean BCS → high F1), masking the pairwise confusability signal.\\n- **SDGD operates at pairwise level**, directly using the validated signal to construct the confusability graph for decomposition. It avoids the aggregation confound entirely.\\n\\n## Evidence Hierarchy (D012)\\n\\n### Tier 1: PRIMARY — Pairwise SCS → Confusion\\n\\nThe cleanest evidence. Directly measures: are semantically similar type pairs more often confused?\\n\\n**Few-NERD (NER)** — Qwen3 embeddings:\\n- Pearson r=0.112 [0.076, 0.156] (n=1953 type pairs) — corrected via bootstrap recomputation\\n- Nonzero-only Spearman ρ=0.272 (p=5e-5)\\n- Top confused pairs are all high-BCS semantic neighbors (person-other ↔ person-politician, BCS=0.934)\\n- Immune to type frequency confound (operates at type-pair level)\\n\\n**MAVEN (ED)** — MiniLM embeddings:\\n- Pearson r=+0.129 [0.104, 0.156] (n=11026 type pairs) — corrected via bootstrap\\n- Nonzero-only Spearman ρ=+0.191 (p<0.001)\\n- Cross-task replication on same-domain schema\\n- Note: Qwen3 pairwise not significant on MAVEN (r=-0.007, p=0.41) — embedding choice matters for pairwise signal in homogeneous schemas\\n\\n### Tier 2: STRONG SECONDARY — FewRel Cross-Task Replication\\n\\nLarge effect size, cross-task (RE), scaling with schema complexity:\\n\\n**Formal 80-rel study** (exp_fewrel_formal_80rel):\\n- Count curve: acc 85.7% (count=1) → 50.4% (count=80), BCS 0→0.97\\n- BCS-controlled: count_8 low-BCS 82.3% vs high-BCS 51.0% (Δ=-31.2pp)\\n- BCS-controlled: count_16 low-BCS 82.8% vs high-BCS 51.6% (Δ=-31.2pp)\\n- **Scaling**: vs 16-rel, degradation 2.8x (35.3pp vs 12.6pp), BCS effect 3.4x (-31.2pp vs -9.1pp)\\n\\n**16-rel sanity check** (exp_fewrel_formal):\\n- count_8: low-BCS 88.9% vs high-BCS 79.8% (Δ=-9.1pp)\\n\\n**Pilot extreme batches** (fewrel_pilot, MiniLM):\\n- count_4: Δ=-20.9pp, count_8: Δ=-50.0pp, count_16: Δ=-48.6pp\\n\\nKey insight: confusability effect amplifies with schema size — direct evidence for multi-channel degradation scaling\\n\\n### Tier 3: SUPPORTING — Few-NERD Per-type Analysis\\n\\nBridges pairwise and batch-level, demonstrates per-type signal in cross-domain schema:\\n- Spearman ρ=-0.293 (p=0.020, n=63 types, freq≥5) — Qwen3 embeddings\\n- Partial r=-0.200 (p=0.116) controlling for log-frequency\\n- Quartile comparison: high-BCS types F1=0.228 vs low-BCS F1=0.310 (Δ=-8.2pp)\\n- BCS-frequency uncorrelated at type level (r=0.042, p=0.74)\\n- MiniLM per-type: ρ≈0 (p=0.97) — extraction model alignment required for per-type signal\\n\\n### Tier 4: DISCUSSION — MAVEN Per-type Centrality Confound\\n\\nMethodological case study on when aggregated confusability measures fail:\\n- Qwen3 per-type: ρ=+0.189 (p=0.021) — OPPOSITE direction\\n- MiniLM per-type: ρ=+0.208 (p=0.011) — ALSO positive, ruling out embedding compression as sole explanation\\n- Both embeddings agree: positive direction on MAVEN is an intrinsic property of the type structure\\n- Explanation: in homogeneous schemas, mean BCS conflates confusability with type centrality (types with many semantic neighbors → common/central types → higher F1)\\n- This is stronger than \\\"domain boundary\\\" — it identifies the specific mechanism (aggregation confound) rather than just the boundary condition\\n\\n### Tier 5: MECHANISTIC — Error Taxonomy (Cross-Task)\\n\\nIntraSub rate monotonically increases with BCS on both NER and RE:\\n\\n**Few-NERD (NER, exp-007)**: IntraSub 0%→1.6%→10.6%→49.4%, ρ=1.0\\n**FewRel 80-rel (RE)**: IntraSub 0%→4.2%→13.0%→20.3%→32.3%, ρ=0.954 (p=0.0, n=154 batches)\\n- extra_sub=0 on both tasks — type confusion is purely intra-batch phenomenon\\n- Same mechanism, different absolute magnitudes — consistent with cross-task expectations\\n\\nAdditional from extreme batch design:\\n- Extreme batches: high-BCS 10-28x more type confusion errors vs low-BCS\\n- Random batches: 1.7-2.4x ratio (still significant, smaller effect)\\n\\n## Embedding Ablation (D010)\\n\\n2×3 matrix: {Qwen3, MiniLM} × {Few-NERD, FewRel, MAVEN}\\n\\n### Per-type (Layer 2)\\n| | Few-NERD | FewRel | MAVEN |\\n|---|---|---|---|\\n| Qwen3 | ρ=-0.293 ✓ | pending | ρ=+0.189 ✗ |\\n| MiniLM | ρ≈0 ✗ | Δ=21-50pp ✓ | ρ=+0.208 ✗ |\\n\\n### Pairwise (Layer 1)\\n| | Few-NERD | MAVEN |\\n|---|---|---|\\n| Qwen3 | r=0.112 [0.076,0.156] ✓ | r=-0.007 ✗ |\\n| MiniLM | — | r=+0.129 [0.104,0.156] ✓ |\\n\\n### SCS→Empirical Confusion Validation (exp-015 fast)\\n| | Qwen3 | MiniLM |\\n|---|---|---|\\n| All pairs ρ | 0.168 (p=7e-14) ✓ | 0.144 (p=2e-10) ✓ |\\n| Nonzero-only ρ | 0.272 (p=5e-5) | 0.306 (p=5e-6) ✓ |\\n\\n**Interpretation**: No single embedding dominates. Extraction-model embeddings (Qwen3) capture per-type confusability in cross-domain schemas. Generic embeddings (MiniLM) capture pairwise confusability in same-domain schemas. SDGD should use task-appropriate embeddings; SDGD-cal (empirical confusion) bypasses embedding choice entirely.\\n\\n## Venue Fit Risks\\n\\n- **\\\"Just an empirical study\\\"**: Mitigated by SDGD as direct operationalization. Controlled experimental design parallels \\\"Lost in the Middle\\\" (TACL 2024).\\n- **Training-free IE relevance**: Cite deployment scenarios — clinical, regulatory, multilingual.\\n- **Multi-model generalizability**: Qwen3-32B primary + LLaMA-3.3-70B (exp-012).\\n- **MAVEN doesn't support hypothesis?**: Pairwise MiniLM does support it. Per-type centrality confound is methodological contribution, not failure.\\n- **Embedding sensitivity**: 2×3 ablation matrix is itself a contribution — characterizes when which proxy works.\\n\\n## Anticipated Reviewer Concerns\\n\\n| Concern | Response Strategy | Experiment |\\n|---------|------------------|------------|\\n| Only one model | LLaMA-3.3-70B replication | exp-012 |\\n| Cross-task replication | Pairwise: Few-NERD ✓ + MAVEN MiniLM ✓. Batch: FewRel ✓. Three tasks. | exp-002, exp-004, fewrel |\\n| No practical method | SDGD framework (-zero, -cal) | exp-008 to exp-011 |\\n| Confusability measure validity | Embedding ablation (D010) + pairwise vs per-type analysis | D010, exp-015 |\\n| Effect size small | Pairwise r=0.12-0.16 + FewRel Δ=21-50pp + confusion ratio 10-28x | multiple |\\n| MAVEN per-type opposite | Centrality confound analysis; pairwise still works | MAVEN MiniLM |\\n| Embedding choice matters? | 2×3 ablation table; SDGD-cal bypasses embedding entirely | D010 |\\n| Why not per-type splitting? | SDGD vs per-type vs random ablation | exp-013, exp-014 |\\n| Latency overhead | Report API calls and wall-clock time | exp-008 |\\n\", \"total_chars\": 11568, \"truncated\": false}, \"error\": null, \"metadata\": {}}"
    }
  },
  "sourceToolAssistantUUID": "f794a1d7-e1db-4362-b421-b12ed1551611",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/reviewer_efaaa6bc",
  "sessionId": "f59020b4-1c0e-4081-9cb3-293eac3560ff",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-15T17:15:45.597Z_

<details open><summary>🔧 Tool call — Glob · `toolu_0196Awu2ZeMQdpLMyBSpqKtA`</summary>

```json
{
  "pattern": "**/*.bib",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2fe3fa4b-a578-41ab-a460-eaba2a6168d0",
  "isSidechain": false,
  "requestId": "req_011Cb4jQc1wxpappYiS3eeJs",
  "type": "assistant",
  "uuid": "7f981343-3bab-4553-910c-a650c1059c07",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/reviewer_efaaa6bc",
  "sessionId": "f59020b4-1c0e-4081-9cb3-293eac3560ff",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01G1gt8poiUhy32oNnwZUFyY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5722,
      "cache_read_input_tokens": 31685,
      "output_tokens": 534,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5722,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 534,
          "cache_read_input_tokens": 31685,
          "cache_creation_input_tokens": 5722,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5722
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

_source line 26_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[系统通知 — worker_done:worker_paper_research_bib_sync_20260515T171027]: Worker worker_paper_research_bib_sync_20260515T171027 已完成（status=done），请审查 Agent 的处理结果。",
  "leafUuid": "cc2040fd-e133-463e-b54e-531793d13528",
  "sessionId": "f59020b4-1c0e-4081-9cb3-293eac3560ff"
}
```

---

### Runtime record

_source line 27_

```json
{
  "type": "ai-title",
  "aiTitle": "Review paper research bibliography sync results",
  "sessionId": "f59020b4-1c0e-4081-9cb3-293eac3560ff"
}
```

---

### Assistant

_source line 28 · 2026-05-15T17:15:50.978Z_

<details><summary>Logged reasoning block</summary>

```text
Now I need to understand what the worker "worker_paper_research_bib_sync_20260515T171027" did. The task name suggests it synchronized bibliography entries with the literature map. Let me check the bib file and also look at the remote server to see if there were changes.

Let me read the references.bib file and also check the remote server for any changes the worker made.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cc2040fd-e133-463e-b54e-531793d13528",
  "isSidechain": false,
  "requestId": "req_011Cb4jRswBr3ZdpVCAPvuDp",
  "type": "assistant",
  "uuid": "5b7b096d-aac6-47bf-b6c9-21dc067a1311",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/reviewer_efaaa6bc",
  "sessionId": "f59020b4-1c0e-4081-9cb3-293eac3560ff",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014GFCwsATKYoApBfMEJQFFb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9136,
      "cache_read_input_tokens": 37407,
      "output_tokens": 313,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 9136,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 313,
          "cache_read_input_tokens": 37407,
          "cache_creation_input_tokens": 9136,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 9136
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

_source line 29 · 2026-05-15T17:15:51.974Z_

找到 bib 文件。读取 bib 文件内容和远程服务器对应文件来交叉验证。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5b7b096d-aac6-47bf-b6c9-21dc067a1311",
  "isSidechain": false,
  "requestId": "req_011Cb4jRswBr3ZdpVCAPvuDp",
  "type": "assistant",
  "uuid": "a3b82634-e608-4265-8edd-c4392fe8868f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/reviewer_efaaa6bc",
  "sessionId": "f59020b4-1c0e-4081-9cb3-293eac3560ff",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014GFCwsATKYoApBfMEJQFFb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9136,
      "cache_read_input_tokens": 37407,
      "output_tokens": 313,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 9136,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 313,
          "cache_read_input_tokens": 37407,
          "cache_creation_input_tokens": 9136,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 9136
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

_source line 30 · 2026-05-15T17:15:52.406Z_

<details open><summary>🔧 Tool call — Read · `toolu_01N2ByfskadFR5qb7Bigz2sp`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a3b82634-e608-4265-8edd-c4392fe8868f",
  "isSidechain": false,
  "requestId": "req_011Cb4jRswBr3ZdpVCAPvuDp",
  "type": "assistant",
  "uuid": "f2a88bd9-beb2-4f94-b9b0-4cc0171b2395",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/reviewer_efaaa6bc",
  "sessionId": "f59020b4-1c0e-4081-9cb3-293eac3560ff",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014GFCwsATKYoApBfMEJQFFb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9136,
      "cache_read_input_tokens": 37407,
      "output_tokens": 313,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 9136,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 313,
          "cache_read_input_tokens": 37407,
          "cache_creation_input_tokens": 9136,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 9136
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

_source line 31 · 2026-05-15T17:15:53.584Z_

<details><summary>↩ Tool result · `toolu_01M5CrpHKe7vSyqfHTthRAsq`</summary>

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
  "tool_name": "mcp__agent-ml-research__reviewer_post_to_director"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "931cee76-bf43-4105-af6f-24e36dd78319",
  "isSidechain": false,
  "promptId": "b593ab42-40aa-4651-8f99-a82b6d6b969a",
  "type": "user",
  "uuid": "13bf7f85-71e8-42bd-b95d-668d7404fa5a",
  "toolUseResult": {
    "matches": [
      "mcp__agent-ml-research__ssh_read_only",
      "mcp__agent-ml-research__reviewer_post_to_director"
    ],
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__reviewer_post_to_director",
    "total_deferred_tools": 34
  },
  "sourceToolAssistantUUID": "931cee76-bf43-4105-af6f-24e36dd78319",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/reviewer_efaaa6bc",
  "sessionId": "f59020b4-1c0e-4081-9cb3-293eac3560ff",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-15T17:15:52.419Z_

<details><summary>↩ Tool result · `toolu_01N2ByfskadFR5qb7Bigz2sp`</summary>

```text
1	% References for Schema-DAG-Extraction
2	% Generated: 2026-05-15
3	% Sources: literature_map.yaml + references_survey.md
4	
5	% =============================================================================
6	% DIRECT COMPETITORS
7	% =============================================================================
8	
9	@inproceedings{llm-pee-2025,
10	    title     = {Towards Event Extraction with Massive Types: {LLM}-based Collaborative Annotation and Partitioning Extraction},
11	    author    = {Liu, Wenxuan and Li, Zixuan and Bai, Long and Zuo, Yuxin and Xu, Daozhu and Jin, Xiaolong and Guo, Jiafeng and Cheng, Xueqi},
12	    booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing},
13	    year      = {2025},
14	    url       = {https://aclanthology.org/2025.emnlp-main.1743/},
15	}
16	
17	@article{parse-2025,
18	    title   = {{PARSE}: {LLM} Driven Schema Optimization for Reliable Entity Extraction},
19	    author  = {Shrimal, Anubhav and Jain, Aryan and Chowdhury, Soumyajit and Yenigalla, Promod},
20	    journal = {arXiv preprint arXiv:2510.08623},
21	    year    = {2025},
22	    url     = {https://arxiv.org/abs/2510.08623},
23	}
24	
25	@inproceedings{dee-2024,
26	    title     = {Decompose, Enrich, and Extract! Schema-aware Event Extraction using {LLM}s},
27	    author    = {Shiri, Fatemeh and Nguyen, Van and Moghimifar, Farhad and Yoo, John and Haffari, Gholamreza and Li, Yuan-Fang},
28	    booktitle = {Proceedings of the IEEE International Conference on Tools with Artificial Intelligence},
29	    year      = {2024},
30	    url       = {https://arxiv.org/abs/2406.01045},
31	}
32	
33	@inproceedings{crossagentie-2025,
34	    title     = {{CROSSAGENTIE}: Cross-Type and Cross-Task Multi-Agent {LLM} Collaboration for Zero-Shot Information Extraction},
35	    author    = {Lu, Meng and Xie, Yuzhang and Bi, Zhenyu and Cao, Shuxiang and Wang, Xuan},
36	    booktitle = {Findings of the Association for Computational Linguistics: ACL 2025},
37	    year      = {2025},
38	    url       = {https://aclanthology.org/2025.findings-acl.718/},
39	}
40	
41	@article{dlisc-2025,
42	    title   = {Effective and Efficient Schema-aware Information Extraction Using On-Device {LLM}s},
43	    author  = {Wen, Zhihao and Liang, Sheng and Wu, Yaxiong and Zhang, Yongyue and Liu, Yong},
44	    journal = {arXiv preprint arXiv:2505.14992},
45	    year    = {2025},
46	    url     = {https://arxiv.org/abs/2505.14992},
47	}
48	
49	@article{spt-2025,
50	    title   = {Schema as Parameterized Tools for Universal Information Extraction},
51	    author  = {Liang, Sheng and Zhang, Yongyue and Wu, Yaxiong and Tang, Ruiming and Liu, Yong},
52	    journal = {arXiv preprint arXiv:2506.01276},
53	    year    = {2025},
54	    url     = {https://arxiv.org/abs/2506.01276},
55	}
56	
57	@inproceedings{zeroner-2025,
58	    title     = {{ZeroNER}: Fueling Zero-Shot {NER} via Entity Type Descriptions},
59	    author    = {Cocchieri, Alessio and Mart{\'\i}nez Galindo, Marcos and Frisoni, Giacomo and Moro, Gianluca and Sartori, Claudio and Tagliavini, Giuseppe},
60	    booktitle = {Findings of the Association for Computational Linguistics: ACL 2025},
61	    year      = {2025},
62	    url       = {https://aclanthology.org/2025.findings-acl.805/},
63	}
64	
65	@inproceedings{cmas-ner-2025,
66	    title     = {A Cooperative Multi-Agent Framework for Zero-Shot Named Entity Recognition},
67	    author    = {Wang, Zihan and Zhao, Ziqi and Lyu, Yougang and Chen, Zhumin and de Rijke, Maarten and Ren, Zhaochun},
68	    booktitle = {Proceedings of the ACM Web Conference 2025},
69	    year      = {2025},
70	    url       = {https://dl.acm.org/doi/10.1145/3696410.3714923},
71	    doi       = {10.1145/3696410.3714923},
72	}
73	
74	% =============================================================================
75	% METHOD COMPONENTS
76	% =============================================================================
77	
78	@inproceedings{uniner-2024,
79	    title     = {{UniversalNER}: Targeted Distillation from Large Language Models for Open Named Entity Recognition},
80	    author    = {Zhou, Wenxuan and Zhang, Sheng and Gu, Yu and Chen, Muhao and Poon, Hoifung},
81	    booktitle = {International Conference on Learning Representations},
82	    year      = {2024},
83	    url       = {https://arxiv.org/abs/2308.03279},
84	}
85	
86	@inproceedings{gollie-2024,
87	    title     = {{GoLLIE}: Annotation Guidelines improve Zero-Shot Information-Extraction},
88	    author    = {Sainz, Oscar and Garc{\'\i}a-Ferrero, Iker and Agerri, Rodrigo and Lopez de Lacalle, Oier and Rigau, German and Agirre, Eneko},
89	    booktitle = {International Conference on Learning Representations},
90	    year      = {2024},
91	    url       = {https://arxiv.org/abs/2310.03668},
92	}
93	
94	@inproceedings{gliner-2024,
95	    title     = {{GLiNER}: Generalist Model for Named Entity Recognition using Bidirectional Transformer},
96	    author    = {Zaratiana, Urchade and Tomeh, Nadi and Holat, Pierre and Charnois, Thierry},
97	    booktitle = {Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics},
98	    year      = {2024},
99	    url       = {https://arxiv.org/abs/2311.08526},
100	}
101	
102	@inproceedings{gliner2-2025,
103	    title     = {{GLiNER2}: Efficient Multi-Task {IE} System with Schema-Driven Interface},
104	    author    = {Zaratiana, Urchade and Pasternak, Gil and Boyd, Oliver and Hurn-Maloney, George and Lewis, Ash},
105	    booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing: System Demonstrations},
106	    year      = {2025},
107	    url       = {https://arxiv.org/abs/2507.18546},
108	}
109	
110	@inproceedings{kggen-2025,
111	    title     = {{KGGen}: Extracting Knowledge Graphs from Plain Text with Language Models},
112	    author    = {Mo, Belinda and Yu, Kyssen and Kazdan, Joshua and Cabezas, Joan and Mpala, Proud and Yu, Lisa and Cundy, Chris and Kanatsoulis, Charilaos and Koyejo, Sanmi},
113	    booktitle = {Advances in Neural Information Processing Systems},
114	    year      = {2025},
115	    url       = {https://arxiv.org/abs/2502.09956},
116	}
117	
118	@inproceedings{code4uie-2024,
119	    title     = {Retrieval-Augmented Code Generation for Universal Information Extraction},
120	    author    = {Guo, Yucan and Li, Zixuan and Jin, Xiaolong and Liu, Yantao and Zeng, Yutao and Liu, Wenxuan and Li, Xiang and Yang, Pan and Bai, Long and Guo, Jiafeng and Cheng, Xueqi},
121	    booktitle = {NeurIPS 2024 Workshop},
122	    year      = {2024},
123	    url       = {https://arxiv.org/abs/2311.02962},
124	}
125	
126	@inproceedings{iepile-2024,
127	    title     = {{IEPile}: Unearthing Large-Scale Schema-Based Information Extraction Corpus},
128	    author    = {Gui, Honghao and Yuan, Lin and Ye, Hongbin and Zhang, Ningyu and Sun, Mengshu and Liang, Lei and Chen, Huajun},
129	    booktitle = {Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics},
130	    year      = {2024},
131	    url       = {https://arxiv.org/abs/2402.14710},
132	}
133	
134	@article{lost-in-middle-2024,
135	    title   = {Lost in the Middle: How Language Models Use Long Contexts},
136	    author  = {Liu, Nelson F. and Lin, Kevin and Hewitt, John and Paranjape, Ashwin and Bevilacqua, Michele and Petroni, Fabio and Liang, Percy},
137	    journal = {Transactions of the Association for Computational Linguistics},
138	    volume  = {12},
139	    pages   = {157--173},
140	    year    = {2024},
141	    url     = {https://arxiv.org/abs/2307.03172},
142	    doi     = {10.1162/tacl_a_00638},
143	}
144	
145	% =============================================================================
146	% ZERO-SHOT NER / RE BASELINES
147	% =============================================================================
148	
149	@inproceedings{self-improve-ner-2024,
150	    title     = {Self-Improving for Zero-Shot Named Entity Recognition with Large Language Models},
151	    author    = {Xie, Tingyu and Li, Qi and Zhang, Yan and Liu, Zuozhu and Wang, Hongwei},
152	    booktitle = {Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics},
153	    year      = {2024},
154	    url       = {https://arxiv.org/abs/2311.08921},
155	}
156	
157	@inproceedings{self-prompting-re-2024,
158	    title     = {Unleashing the Power of {LLM}s in Zero-shot Relation Extraction via Self-Prompting},
159	    author    = {Liu, Siyi and Li, Yang and Li, Jiang and Yang, Shan and Lan, Yunshi},
160	    booktitle = {Findings of the Association for Computational Linguistics: EMNLP 2024},
161	    year      = {2024},
162	    url       = {https://arxiv.org/abs/2410.01154},
163	}
164	
165	@article{reasoning-ner-2025,
166	    title   = {A Reasoning Paradigm for Named Entity Recognition},
167	    author  = {Huang, Hui and Chen, Yanping and Huang, Ruizhang and Lin, Chuan and Qin, Yongbin},
168	    journal = {arXiv preprint arXiv:2511.11978},
169	    year    = {2025},
170	    url     = {https://arxiv.org/abs/2511.11978},
171	}
172	
173	@inproceedings{nuner-2024,
174	    title     = {{NuNER}: Entity Recognition Encoder Pre-training via {LLM}-Annotated Data},
175	    author    = {Bogdanov, Sergei and Constantin, Alexandre and Bernard, Timoth{\'e}e and Crabb{\'e}, Benoit and Bernard, Etienne},
176	    booktitle = {Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing},
177	    year      = {2024},
178	    url       = {https://arxiv.org/abs/2402.15343},
179	}
180	
181	% =============================================================================
182	% EVALUATION / BENCHMARKING
183	% =============================================================================
184	
185	@inproceedings{familiarity-2025,
186	    title     = {Familiarity: Better Evaluation of Zero-Shot Named Entity Recognition by Quantifying Label Shifts in Synthetic Training Data},
187	    author    = {Golde, Jonas and Haller, Patrick and Ploner, Max and Barth, Fabio and Jedema, Nicolaas and Akbik, Alan},
188	    booktitle = {Proceedings of the 2025 Conference of the North American Chapter of the Association for Computational Linguistics},
189	    year      = {2025},
190	    url       = {https://arxiv.org/abs/2412.10121},
191	}
192	
193	@inproceedings{guidex-2025,
194	    title     = {{GuideX}: Guided Synthetic Data Generation for Zero-Shot Information Extraction},
195	    author    = {De La Fuente, Neil and Sainz, Oscar and Garc{\'\i}a-Ferrero, Iker and Agirre, Eneko},
196	    booktitle = {Findings of the Association for Computational Linguistics: ACL 2025},
197	    year      = {2025},
198	    url       = {https://arxiv.org/abs/2506.00649},
199	}
200	
201	% =============================================================================
202	% SURVEYS / BACKGROUND
203	% =============================================================================
204	
205	@article{llm4ie-survey-2024,
206	    title   = {Large Language Models for Generative Information Extraction: A Survey},
207	    author  = {Xu, Derong and Chen, Wei and Peng, Wenjun and Zhang, Chao and Xu, Tong and Zhao, Xiangyu and Wu, Xian and Zheng, Yefeng and Wang, Yang and Chen, Enhong},
208	    journal = {Frontiers of Computer Science},
209	    volume  = {18},
210	    number  = {6},
211	    year    = {2024},
212	    url     = {https://arxiv.org/abs/2312.17617},
213	    doi     = {10.1007/s11704-024-40555-y},
214	}
215	
216	@inproceedings{knowcoder-2024,
217	    title     = {{KnowCoder}: Coding Structured Knowledge into {LLM}s for Universal Information Extraction},
218	    author    = {Li, Zixuan and Zeng, Yutao and Zuo, Yuxin and Ren, Weicheng and Liu, Wenxuan and Su, Miao and Guo, Yucan and Liu, Yantao and Li, Xiang and Hu, Zhilei and Bai, Long and Li, Wei and Liu, Yidan and Yang, Pan and Jin, Xiaolong and Guo, Jiafeng and Cheng, Xueqi},
219	    booktitle = {Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics},
220	    year      = {2024},
221	    url       = {https://arxiv.org/abs/2403.07969},
222	}
223	
224	@inproceedings{slot-2025,
225	    title     = {{SLOT}: Structuring the Output of Large Language Models},
226	    author    = {Shen, Zhengyuan and Wang, Darren Yow-Bang and Mishra, Soumya Smruti and Xu, Zhichao and Teng, Yifei and Ding, Haibo},
227	    booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing: Industry Track},
228	    year      = {2025},
229	    url       = {https://aclanthology.org/2025.emnlp-industry.32/},
230	}
231	
232	% =============================================================================
233	% EMBEDDING ANISOTROPY / REPRESENTATION DEGENERATION
234	% =============================================================================
235	
236	@inproceedings{gao-repr-degen-2019,
237	    title     = {Representation Degeneration Problem in Training Natural Language Generation Models},
238	    author    = {Gao, Jun and He, Di and Tan, Xu and Qin, Tao and Wang, Liwei and Liu, Tie-Yan},
239	    booktitle = {International Conference on Learning Representations},
240	    year      = {2019},
241	    url       = {https://arxiv.org/abs/1907.12009},
242	}
243	
244	@inproceedings{ethayarajh-contextual-2019,
245	    title     = {How Contextual are Contextualized Word Representations? {C}omparing the Geometry of {BERT}, {ELMo}, and {GPT-2} Embeddings},
246	    author    = {Ethayarajh, Kawin},
247	    booktitle = {Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing and the 9th International Joint Conference on Natural Language Processing},
248	    year      = {2019},
249	    url       = {https://aclanthology.org/D19-1006/},
250	}
251	
252	@inproceedings{cai-isotropy-clusters-2021,
253	    title     = {Isotropy in the Contextual Embedding Space: Clusters and Manifolds},
254	    author    = {Cai, Xingyu and Huang, Jiaji and Bian, Yuchen and Church, Kenneth},
255	    booktitle = {International Conference on Learning Representations},
256	    year      = {2021},
257	    url       = {https://openreview.net/forum?id=xYGNO86OWDH},
258	}
259	
260	@inproceedings{godey-anisotropy-inherent-2024,
261	    title     = {Anisotropy Is Inherent to Self-Attention in Transformers},
262	    author    = {Godey, Nathan and de la Clergerie, {\'E}ric and Sagot, Beno{\^\i}t},
263	    booktitle = {Proceedings of the 18th Conference of the European Chapter of the Association for Computational Linguistics},
264	    year      = {2024},
265	    url       = {https://aclanthology.org/2024.eacl-long.3/},
266	}
267	
268	@inproceedings{rajaee-cluster-isotropy-2021,
269	    title     = {A Cluster-based Approach for Improving Isotropy in Contextual Embedding Space},
270	    author    = {Rajaee, Sara and Pilehvar, Mohammad Taher},
271	    booktitle = {Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics},
272	    year      = {2021},
273	    url       = {https://aclanthology.org/2021.acl-short.73/},
274	}
275	
276	% =============================================================================
277	% ADDITIONAL REFERENCES (from references_survey.md only)
278	% =============================================================================
279	
280	@article{instructuie-2023,
281	    title   = {{InstructUIE}: Multi-task Instruction Tuning for Unified Information Extraction},
282	    author  = {Wang, Xiao and Zhou, Weikang and Zu, Can and Xia, Han and Chen, Tianze and Zhang, Yuansen and Zheng, Rui and Ye, Junjie and Zhang, Qi and Gui, Tao and Kang, Jihua and Yang, Jingsheng and Li, Siyuan and Du, Chunsai},
283	    journal = {arXiv preprint arXiv:2304.08085},
284	    year    = {2023},
285	    url     = {https://arxiv.org/abs/2304.08085},
286	}
287	
288	@inproceedings{codeie-2023,
289	    title     = {{CodeIE}: Large Code Generation Models are Better Few-Shot Information Extractors},
290	    author    = {Li, Peng and Sun, Tianxiang and Tang, Qiong and Yan, Hang and Wu, Yuanbin and Huang, Xuanjing and Qiu, Xipeng},
291	    booktitle = {Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics},
292	    year      = {2023},
293	    url       = {https://aclanthology.org/2023.acl-long.855/},
294	}
295	
296	@inproceedings{adelie-2024,
297	    title     = {{ADELIE}: Aligning Large Language Models on Information Extraction},
298	    author    = {Qi, Yunjia and Peng, Hao and Wang, Xiaozhi and Xu, Bin and Hou, Lei and Li, Juanzi},
299	    booktitle = {Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing},
300	    year      = {2024},
301	    url       = {https://aclanthology.org/2024.emnlp-main.419/},
302	}
303	
304	@inproceedings{oneke-2025,
305	    title     = {{OneKE}: A Dockerized Schema-Guided {LLM} Agent-based Knowledge Extraction System},
306	    author    = {Luo, Yujie and Yan, Lingyong and Liu, Zhenghao and Ji, Yixin and Wang, Weiqi and Yu, Shi and Yan, Yukun and Wang, Shuo and Zhang, Yue and Cao, Shulin and Ren, Weicheng and Gui, Honghao and Bi, Zhen and Huang, Yongfei and Yao, Yuan and Zhang, Ningyu and Chen, Huajun},
307	    booktitle = {Companion Proceedings of the ACM Web Conference 2025},
308	    year      = {2025},
309	    url       = {https://arxiv.org/abs/2412.20005},
310	    doi       = {10.1145/3701716.3715189},
311	}
312	
313	@inproceedings{genre-2021,
314	    title     = {Autoregressive Entity Retrieval},
315	    author    = {De Cao, Nicola and Izacard, Gautier and Riedel, Sebastian and Petroni, Fabio},
316	    booktitle = {International Conference on Learning Representations},
317	    year      = {2021},
318	    url       = {https://arxiv.org/abs/2010.00904},
319	}
320	
321	@inproceedings{inerd-2024,
322	    title     = {Informed Named Entity Recognition Decoding for Generative Language Models},
323	    author    = {Deu{\ss}er, Tobias and Hillebrand, Lars Patrick and Bauckhage, Christian and Sifa, Rafet},
324	    booktitle = {Proceedings of the IEEE International Conference on Big Data},
325	    year      = {2024},
326	    url       = {https://arxiv.org/abs/2308.07791},
327	}
328	
329	@inproceedings{noisebench-2024,
330	    title     = {{NoiseBench}: Benchmarking the Impact of Real Label Noise on Named Entity Recognition},
331	    author    = {Merdjanovska, Elena and Aynetdinov, Ansar and Akbik, Alan},
332	    booktitle = {Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing},
333	    year      = {2024},
334	    url       = {https://aclanthology.org/2024.emnlp-main.1011/},
335	}
336	
337	@inproceedings{lrn-2021,
338	    title     = {Fine-grained Entity Typing via Label Reasoning},
339	    author    = {Liu, Qing and Lin, Hongyu and Xiao, Xinyan and Han, Xianpei and Sun, Le and Wu, Hua},
340	    booktitle = {Proceedings of the 2021 Conference on Empirical Methods in Natural Language Processing},
341	    year      = {2021},
342	    url       = {https://aclanthology.org/2021.emnlp-main.378/},
343	}
344	
345	@inproceedings{genres-2024,
346	    title     = {{GenRES}: Rethinking Evaluation for Generative Relation Extraction in the Era of Large Language Models},
347	    author    = {Jiang, Pengcheng and Lin, Jiacheng and Wang, Zifeng and Sun, Jimeng and Han, Jiawei},
348	    booktitle = {Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics},
349	    year      = {2024},
350	    url       = {https://aclanthology.org/2024.naacl-long.155/},
351	}
352	
353	@inproceedings{multiconner2-2023,
354	    title     = {{SemEval}-2023 Task 2: Fine-grained Multilingual Named Entity Recognition ({MultiCoNER} 2)},
355	    author    = {Fetahu, Besnik and Kar, Sudipta and Chen, Zhiyu and Rokhlenko, Oleg and Malmasi, Shervin},
356	    booktitle = {Proceedings of the 17th International Workshop on Semantic Evaluation},
357	    year      = {2023},
358	    url       = {https://aclanthology.org/2023.semeval-1.310/},
359	}
360	
361	@inproceedings{llm-calibration-survey-2024,
362	    title     = {A Survey of Confidence Estimation and Calibration in Large Language Models},
363	    author    = {Geng, Jiahui and Cai, Fengyu and Wang, Yuxia and Koeppl, Heinz and Nakov, Preslav and Gurevych, Iryna},
364	    booktitle = {Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics},
365	    year      = {2024},
366	    url       = {https://aclanthology.org/2024.naacl-long.366/},
367	}
368	
369	@inproceedings{far-calibration-2024,
370	    title     = {Fact-and-Reflection ({FaR}) Improves Confidence Calibration of Large Language Models},
371	    author    = {Zhao, Xinran and Zhang, Hongming and Pan, Xiaoman and Yao, Wenlin and Yu, Dong and Wu, Tongshuang and Chen, Jianshu},
372	    booktitle = {Findings of the Association for Computational Linguistics: ACL 2024},
373	    year      = {2024},
374	    url       = {https://aclanthology.org/2024.findings-acl.515/},
375	}
376	
377	@inproceedings{linkner-2024,
378	    title     = {{LinkNER}: Linking Local Named Entity Recognition Models to Large Language Models using Uncertainty},
379	    author    = {Zhang, Zhen and Zhao, Yuhua and Gao, Hang and Hu, Mengting},
380	    booktitle = {Proceedings of the ACM Web Conference 2024},
381	    year      = {2024},
382	    url       = {https://dl.acm.org/doi/10.1145/3589334.3645414},
383	    doi       = {10.1145/3589334.3645414},
384	}
385	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f2a88bd9-beb2-4f94-b9b0-4cc0171b2395",
  "isSidechain": false,
  "promptId": "b593ab42-40aa-4651-8f99-a82b6d6b969a",
  "type": "user",
  "uuid": "4a00cfe2-7b05-4d19-add5-d147df2c7db3",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/references.bib",
      "content": "% References for Schema-DAG-Extraction\n% Generated: 2026-05-15\n% Sources: literature_map.yaml + references_survey.md\n\n% =============================================================================\n% DIRECT COMPETITORS\n% =============================================================================\n\n@inproceedings{llm-pee-2025,\n    title     = {Towards Event Extraction with Massive Types: {LLM}-based Collaborative Annotation and Partitioning Extraction},\n    author    = {Liu, Wenxuan and Li, Zixuan and Bai, Long and Zuo, Yuxin and Xu, Daozhu and Jin, Xiaolong and Guo, Jiafeng and Cheng, Xueqi},\n    booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing},\n    year      = {2025},\n    url       = {https://aclanthology.org/2025.emnlp-main.1743/},\n}\n\n@article{parse-2025,\n    title   = {{PARSE}: {LLM} Driven Schema Optimization for Reliable Entity Extraction},\n    author  = {Shrimal, Anubhav and Jain, Aryan and Chowdhury, Soumyajit and Yenigalla, Promod},\n    journal = {arXiv preprint arXiv:2510.08623},\n    year    = {2025},\n    url     = {https://arxiv.org/abs/2510.08623},\n}\n\n@inproceedings{dee-2024,\n    title     = {Decompose, Enrich, and Extract! Schema-aware Event Extraction using {LLM}s},\n    author    = {Shiri, Fatemeh and Nguyen, Van and Moghimifar, Farhad and Yoo, John and Haffari, Gholamreza and Li, Yuan-Fang},\n    booktitle = {Proceedings of the IEEE International Conference on Tools with Artificial Intelligence},\n    year      = {2024},\n    url       = {https://arxiv.org/abs/2406.01045},\n}\n\n@inproceedings{crossagentie-2025,\n    title     = {{CROSSAGENTIE}: Cross-Type and Cross-Task Multi-Agent {LLM} Collaboration for Zero-Shot Information Extraction},\n    author    = {Lu, Meng and Xie, Yuzhang and Bi, Zhenyu and Cao, Shuxiang and Wang, Xuan},\n    booktitle = {Findings of the Association for Computational Linguistics: ACL 2025},\n    year      = {2025},\n    url       = {https://aclanthology.org/2025.findings-acl.718/},\n}\n\n@article{dlisc-2025,\n    title   = {Effective and Efficient Schema-aware Information Extraction Using On-Device {LLM}s},\n    author  = {Wen, Zhihao and Liang, Sheng and Wu, Yaxiong and Zhang, Yongyue and Liu, Yong},\n    journal = {arXiv preprint arXiv:2505.14992},\n    year    = {2025},\n    url     = {https://arxiv.org/abs/2505.14992},\n}\n\n@article{spt-2025,\n    title   = {Schema as Parameterized Tools for Universal Information Extraction},\n    author  = {Liang, Sheng and Zhang, Yongyue and Wu, Yaxiong and Tang, Ruiming and Liu, Yong},\n    journal = {arXiv preprint arXiv:2506.01276},\n    year    = {2025},\n    url     = {https://arxiv.org/abs/2506.01276},\n}\n\n@inproceedings{zeroner-2025,\n    title     = {{ZeroNER}: Fueling Zero-Shot {NER} via Entity Type Descriptions},\n    author    = {Cocchieri, Alessio and Mart{\\'\\i}nez Galindo, Marcos and Frisoni, Giacomo and Moro, Gianluca and Sartori, Claudio and Tagliavini, Giuseppe},\n    booktitle = {Findings of the Association for Computational Linguistics: ACL 2025},\n    year      = {2025},\n    url       = {https://aclanthology.org/2025.findings-acl.805/},\n}\n\n@inproceedings{cmas-ner-2025,\n    title     = {A Cooperative Multi-Agent Framework for Zero-Shot Named Entity Recognition},\n    author    = {Wang, Zihan and Zhao, Ziqi and Lyu, Yougang and Chen, Zhumin and de Rijke, Maarten and Ren, Zhaochun},\n    booktitle = {Proceedings of the ACM Web Conference 2025},\n    year      = {2025},\n    url       = {https://dl.acm.org/doi/10.1145/3696410.3714923},\n    doi       = {10.1145/3696410.3714923},\n}\n\n% =============================================================================\n% METHOD COMPONENTS\n% =============================================================================\n\n@inproceedings{uniner-2024,\n    title     = {{UniversalNER}: Targeted Distillation from Large Language Models for Open Named Entity Recognition},\n    author    = {Zhou, Wenxuan and Zhang, Sheng and Gu, Yu and Chen, Muhao and Poon, Hoifung},\n    booktitle = {International Conference on Learning Representations},\n    year      = {2024},\n    url       = {https://arxiv.org/abs/2308.03279},\n}\n\n@inproceedings{gollie-2024,\n    title     = {{GoLLIE}: Annotation Guidelines improve Zero-Shot Information-Extraction},\n    author    = {Sainz, Oscar and Garc{\\'\\i}a-Ferrero, Iker and Agerri, Rodrigo and Lopez de Lacalle, Oier and Rigau, German and Agirre, Eneko},\n    booktitle = {International Conference on Learning Representations},\n    year      = {2024},\n    url       = {https://arxiv.org/abs/2310.03668},\n}\n\n@inproceedings{gliner-2024,\n    title     = {{GLiNER}: Generalist Model for Named Entity Recognition using Bidirectional Transformer},\n    author    = {Zaratiana, Urchade and Tomeh, Nadi and Holat, Pierre and Charnois, Thierry},\n    booktitle = {Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics},\n    year      = {2024},\n    url       = {https://arxiv.org/abs/2311.08526},\n}\n\n@inproceedings{gliner2-2025,\n    title     = {{GLiNER2}: Efficient Multi-Task {IE} System with Schema-Driven Interface},\n    author    = {Zaratiana, Urchade and Pasternak, Gil and Boyd, Oliver and Hurn-Maloney, George and Lewis, Ash},\n    booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing: System Demonstrations},\n    year      = {2025},\n    url       = {https://arxiv.org/abs/2507.18546},\n}\n\n@inproceedings{kggen-2025,\n    title     = {{KGGen}: Extracting Knowledge Graphs from Plain Text with Language Models},\n    author    = {Mo, Belinda and Yu, Kyssen and Kazdan, Joshua and Cabezas, Joan and Mpala, Proud and Yu, Lisa and Cundy, Chris and Kanatsoulis, Charilaos and Koyejo, Sanmi},\n    booktitle = {Advances in Neural Information Processing Systems},\n    year      = {2025},\n    url       = {https://arxiv.org/abs/2502.09956},\n}\n\n@inproceedings{code4uie-2024,\n    title     = {Retrieval-Augmented Code Generation for Universal Information Extraction},\n    author    = {Guo, Yucan and Li, Zixuan and Jin, Xiaolong and Liu, Yantao and Zeng, Yutao and Liu, Wenxuan and Li, Xiang and Yang, Pan and Bai, Long and Guo, Jiafeng and Cheng, Xueqi},\n    booktitle = {NeurIPS 2024 Workshop},\n    year      = {2024},\n    url       = {https://arxiv.org/abs/2311.02962},\n}\n\n@inproceedings{iepile-2024,\n    title     = {{IEPile}: Unearthing Large-Scale Schema-Based Information Extraction Corpus},\n    author    = {Gui, Honghao and Yuan, Lin and Ye, Hongbin and Zhang, Ningyu and Sun, Mengshu and Liang, Lei and Chen, Huajun},\n    booktitle = {Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics},\n    year      = {2024},\n    url       = {https://arxiv.org/abs/2402.14710},\n}\n\n@article{lost-in-middle-2024,\n    title   = {Lost in the Middle: How Language Models Use Long Contexts},\n    author  = {Liu, Nelson F. and Lin, Kevin and Hewitt, John and Paranjape, Ashwin and Bevilacqua, Michele and Petroni, Fabio and Liang, Percy},\n    journal = {Transactions of the Association for Computational Linguistics},\n    volume  = {12},\n    pages   = {157--173},\n    year    = {2024},\n    url     = {https://arxiv.org/abs/2307.03172},\n    doi     = {10.1162/tacl_a_00638},\n}\n\n% =============================================================================\n% ZERO-SHOT NER / RE BASELINES\n% =============================================================================\n\n@inproceedings{self-improve-ner-2024,\n    title     = {Self-Improving for Zero-Shot Named Entity Recognition with Large Language Models},\n    author    = {Xie, Tingyu and Li, Qi and Zhang, Yan and Liu, Zuozhu and Wang, Hongwei},\n    booktitle = {Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics},\n    year      = {2024},\n    url       = {https://arxiv.org/abs/2311.08921},\n}\n\n@inproceedings{self-prompting-re-2024,\n    title     = {Unleashing the Power of {LLM}s in Zero-shot Relation Extraction via Self-Prompting},\n    author    = {Liu, Siyi and Li, Yang and Li, Jiang and Yang, Shan and Lan, Yunshi},\n    booktitle = {Findings of the Association for Computational Linguistics: EMNLP 2024},\n    year      = {2024},\n    url       = {https://arxiv.org/abs/2410.01154},\n}\n\n@article{reasoning-ner-2025,\n    title   = {A Reasoning Paradigm for Named Entity Recognition},\n    author  = {Huang, Hui and Chen, Yanping and Huang, Ruizhang and Lin, Chuan and Qin, Yongbin},\n    journal = {arXiv preprint arXiv:2511.11978},\n    year    = {2025},\n    url     = {https://arxiv.org/abs/2511.11978},\n}\n\n@inproceedings{nuner-2024,\n    title     = {{NuNER}: Entity Recognition Encoder Pre-training via {LLM}-Annotated Data},\n    author    = {Bogdanov, Sergei and Constantin, Alexandre and Bernard, Timoth{\\'e}e and Crabb{\\'e}, Benoit and Bernard, Etienne},\n    booktitle = {Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing},\n    year      = {2024},\n    url       = {https://arxiv.org/abs/2402.15343},\n}\n\n% =============================================================================\n% EVALUATION / BENCHMARKING\n% =============================================================================\n\n@inproceedings{familiarity-2025,\n    title     = {Familiarity: Better Evaluation of Zero-Shot Named Entity Recognition by Quantifying Label Shifts in Synthetic Training Data},\n    author    = {Golde, Jonas and Haller, Patrick and Ploner, Max and Barth, Fabio and Jedema, Nicolaas and Akbik, Alan},\n    booktitle = {Proceedings of the 2025 Conference of the North American Chapter of the Association for Computational Linguistics},\n    year      = {2025},\n    url       = {https://arxiv.org/abs/2412.10121},\n}\n\n@inproceedings{guidex-2025,\n    title     = {{GuideX}: Guided Synthetic Data Generation for Zero-Shot Information Extraction},\n    author    = {De La Fuente, Neil and Sainz, Oscar and Garc{\\'\\i}a-Ferrero, Iker and Agirre, Eneko},\n    booktitle = {Findings of the Association for Computational Linguistics: ACL 2025},\n    year      = {2025},\n    url       = {https://arxiv.org/abs/2506.00649},\n}\n\n% =============================================================================\n% SURVEYS / BACKGROUND\n% =============================================================================\n\n@article{llm4ie-survey-2024,\n    title   = {Large Language Models for Generative Information Extraction: A Survey},\n    author  = {Xu, Derong and Chen, Wei and Peng, Wenjun and Zhang, Chao and Xu, Tong and Zhao, Xiangyu and Wu, Xian and Zheng, Yefeng and Wang, Yang and Chen, Enhong},\n    journal = {Frontiers of Computer Science},\n    volume  = {18},\n    number  = {6},\n    year    = {2024},\n    url     = {https://arxiv.org/abs/2312.17617},\n    doi     = {10.1007/s11704-024-40555-y},\n}\n\n@inproceedings{knowcoder-2024,\n    title     = {{KnowCoder}: Coding Structured Knowledge into {LLM}s for Universal Information Extraction},\n    author    = {Li, Zixuan and Zeng, Yutao and Zuo, Yuxin and Ren, Weicheng and Liu, Wenxuan and Su, Miao and Guo, Yucan and Liu, Yantao and Li, Xiang and Hu, Zhilei and Bai, Long and Li, Wei and Liu, Yidan and Yang, Pan and Jin, Xiaolong and Guo, Jiafeng and Cheng, Xueqi},\n    booktitle = {Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics},\n    year      = {2024},\n    url       = {https://arxiv.org/abs/2403.07969},\n}\n\n@inproceedings{slot-2025,\n    title     = {{SLOT}: Structuring the Output of Large Language Models},\n    author    = {Shen, Zhengyuan and Wang, Darren Yow-Bang and Mishra, Soumya Smruti and Xu, Zhichao and Teng, Yifei and Ding, Haibo},\n    booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing: Industry Track},\n    year      = {2025},\n    url       = {https://aclanthology.org/2025.emnlp-industry.32/},\n}\n\n% =============================================================================\n% EMBEDDING ANISOTROPY / REPRESENTATION DEGENERATION\n% =============================================================================\n\n@inproceedings{gao-repr-degen-2019,\n    title     = {Representation Degeneration Problem in Training Natural Language Generation Models},\n    author    = {Gao, Jun and He, Di and Tan, Xu and Qin, Tao and Wang, Liwei and Liu, Tie-Yan},\n    booktitle = {International Conference on Learning Representations},\n    year      = {2019},\n    url       = {https://arxiv.org/abs/1907.12009},\n}\n\n@inproceedings{ethayarajh-contextual-2019,\n    title     = {How Contextual are Contextualized Word Representations? {C}omparing the Geometry of {BERT}, {ELMo}, and {GPT-2} Embeddings},\n    author    = {Ethayarajh, Kawin},\n    booktitle = {Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing and the 9th International Joint Conference on Natural Language Processing},\n    year      = {2019},\n    url       = {https://aclanthology.org/D19-1006/},\n}\n\n@inproceedings{cai-isotropy-clusters-2021,\n    title     = {Isotropy in the Contextual Embedding Space: Clusters and Manifolds},\n    author    = {Cai, Xingyu and Huang, Jiaji and Bian, Yuchen and Church, Kenneth},\n    booktitle = {International Conference on Learning Representations},\n    year      = {2021},\n    url       = {https://openreview.net/forum?id=xYGNO86OWDH},\n}\n\n@inproceedings{godey-anisotropy-inherent-2024,\n    title     = {Anisotropy Is Inherent to Self-Attention in Transformers},\n    author    = {Godey, Nathan and de la Clergerie, {\\'E}ric and Sagot, Beno{\\^\\i}t},\n    booktitle = {Proceedings of the 18th Conference of the European Chapter of the Association for Computational Linguistics},\n    year      = {2024},\n    url       = {https://aclanthology.org/2024.eacl-long.3/},\n}\n\n@inproceedings{rajaee-cluster-isotropy-2021,\n    title     = {A Cluster-based Approach for Improving Isotropy in Contextual Embedding Space},\n    author    = {Rajaee, Sara and Pilehvar, Mohammad Taher},\n    booktitle = {Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics},\n    year      = {2021},\n    url       = {https://aclanthology.org/2021.acl-short.73/},\n}\n\n% =============================================================================\n% ADDITIONAL REFERENCES (from references_survey.md only)\n% =============================================================================\n\n@article{instructuie-2023,\n    title   = {{InstructUIE}: Multi-task Instruction Tuning for Unified Information Extraction},\n    author  = {Wang, Xiao and Zhou, Weikang and Zu, Can and Xia, Han and Chen, Tianze and Zhang, Yuansen and Zheng, Rui and Ye, Junjie and Zhang, Qi and Gui, Tao and Kang, Jihua and Yang, Jingsheng and Li, Siyuan and Du, Chunsai},\n    journal = {arXiv preprint arXiv:2304.08085},\n    year    = {2023},\n    url     = {https://arxiv.org/abs/2304.08085},\n}\n\n@inproceedings{codeie-2023,\n    title     = {{CodeIE}: Large Code Generation Models are Better Few-Shot Information Extractors},\n    author    = {Li, Peng and Sun, Tianxiang and Tang, Qiong and Yan, Hang and Wu, Yuanbin and Huang, Xuanjing and Qiu, Xipeng},\n    booktitle = {Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics},\n    year      = {2023},\n    url       = {https://aclanthology.org/2023.acl-long.855/},\n}\n\n@inproceedings{adelie-2024,\n    title     = {{ADELIE}: Aligning Large Language Models on Information Extraction},\n    author    = {Qi, Yunjia and Peng, Hao and Wang, Xiaozhi and Xu, Bin and Hou, Lei and Li, Juanzi},\n    booktitle = {Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing},\n    year      = {2024},\n    url       = {https://aclanthology.org/2024.emnlp-main.419/},\n}\n\n@inproceedings{oneke-2025,\n    title     = {{OneKE}: A Dockerized Schema-Guided {LLM} Agent-based Knowledge Extraction System},\n    author    = {Luo, Yujie and Yan, Lingyong and Liu, Zhenghao and Ji, Yixin and Wang, Weiqi and Yu, Shi and Yan, Yukun and Wang, Shuo and Zhang, Yue and Cao, Shulin and Ren, Weicheng and Gui, Honghao and Bi, Zhen and Huang, Yongfei and Yao, Yuan and Zhang, Ningyu and Chen, Huajun},\n    booktitle = {Companion Proceedings of the ACM Web Conference 2025},\n    year      = {2025},\n    url       = {https://arxiv.org/abs/2412.20005},\n    doi       = {10.1145/3701716.3715189},\n}\n\n@inproceedings{genre-2021,\n    title     = {Autoregressive Entity Retrieval},\n    author    = {De Cao, Nicola and Izacard, Gautier and Riedel, Sebastian and Petroni, Fabio},\n    booktitle = {International Conference on Learning Representations},\n    year      = {2021},\n    url       = {https://arxiv.org/abs/2010.00904},\n}\n\n@inproceedings{inerd-2024,\n    title     = {Informed Named Entity Recognition Decoding for Generative Language Models},\n    author    = {Deu{\\ss}er, Tobias and Hillebrand, Lars Patrick and Bauckhage, Christian and Sifa, Rafet},\n    booktitle = {Proceedings of the IEEE International Conference on Big Data},\n    year      = {2024},\n    url       = {https://arxiv.org/abs/2308.07791},\n}\n\n@inproceedings{noisebench-2024,\n    title     = {{NoiseBench}: Benchmarking the Impact of Real Label Noise on Named Entity Recognition},\n    author    = {Merdjanovska, Elena and Aynetdinov, Ansar and Akbik, Alan},\n    booktitle = {Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing},\n    year      = {2024},\n    url       = {https://aclanthology.org/2024.emnlp-main.1011/},\n}\n\n@inproceedings{lrn-2021,\n    title     = {Fine-grained Entity Typing via Label Reasoning},\n    author    = {Liu, Qing and Lin, Hongyu and Xiao, Xinyan and Han, Xianpei and Sun, Le and Wu, Hua},\n    booktitle = {Proceedings of the 2021 Conference on Empirical Methods in Natural Language Processing},\n    year      = {2021},\n    url       = {https://aclanthology.org/2021.emnlp-main.378/},\n}\n\n@inproceedings{genres-2024,\n    title     = {{GenRES}: Rethinking Evaluation for Generative Relation Extraction in the Era of Large Language Models},\n    author    = {Jiang, Pengcheng and Lin, Jiacheng and Wang, Zifeng and Sun, Jimeng and Han, Jiawei},\n    booktitle = {Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics},\n    year      = {2024},\n    url       = {https://aclanthology.org/2024.naacl-long.155/},\n}\n\n@inproceedings{multiconner2-2023,\n    title     = {{SemEval}-2023 Task 2: Fine-grained Multilingual Named Entity Recognition ({MultiCoNER} 2)},\n    author    = {Fetahu, Besnik and Kar, Sudipta and Chen, Zhiyu and Rokhlenko, Oleg and Malmasi, Shervin},\n    booktitle = {Proceedings of the 17th International Workshop on Semantic Evaluation},\n    year      = {2023},\n    url       = {https://aclanthology.org/2023.semeval-1.310/},\n}\n\n@inproceedings{llm-calibration-survey-2024,\n    title     = {A Survey of Confidence Estimation and Calibration in Large Language Models},\n    author    = {Geng, Jiahui and Cai, Fengyu and Wang, Yuxia and Koeppl, Heinz and Nakov, Preslav and Gurevych, Iryna},\n    booktitle = {Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics},\n    year      = {2024},\n    url       = {https://aclanthology.org/2024.naacl-long.366/},\n}\n\n@inproceedings{far-calibration-2024,\n    title     = {Fact-and-Reflection ({FaR}) Improves Confidence Calibration of Large Language Models},\n    author    = {Zhao, Xinran and Zhang, Hongming and Pan, Xiaoman and Yao, Wenlin and Yu, Dong and Wu, Tongshuang and Chen, Jianshu},\n    booktitle = {Findings of the Association for Computational Linguistics: ACL 2024},\n    year      = {2024},\n    url       = {https://aclanthology.org/2024.findings-acl.515/},\n}\n\n@inproceedings{linkner-2024,\n    title     = {{LinkNER}: Linking Local Named Entity Recognition Models to Large Language Models using Uncertainty},\n    author    = {Zhang, Zhen and Zhao, Yuhua and Gao, Hang and Hu, Mengting},\n    booktitle = {Proceedings of the ACM Web Conference 2024},\n    year      = {2024},\n    url       = {https://dl.acm.org/doi/10.1145/3589334.3645414},\n    doi       = {10.1145/3589334.3645414},\n}\n",
      "numLines": 385,
      "startLine": 1,
      "totalLines": 385
    }
  },
  "sourceToolAssistantUUID": "f2a88bd9-beb2-4f94-b9b0-4cc0171b2395",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/reviewer_efaaa6bc",
  "sessionId": "f59020b4-1c0e-4081-9cb3-293eac3560ff",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-15T17:15:53.580Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01M5CrpHKe7vSyqfHTthRAsq`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__reviewer_post_to_director",
  "max_results": 2
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4a00cfe2-7b05-4d19-add5-d147df2c7db3",
  "isSidechain": false,
  "requestId": "req_011Cb4jRswBr3ZdpVCAPvuDp",
  "type": "assistant",
  "uuid": "931cee76-bf43-4105-af6f-24e36dd78319",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/reviewer_efaaa6bc",
  "sessionId": "f59020b4-1c0e-4081-9cb3-293eac3560ff",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014GFCwsATKYoApBfMEJQFFb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9136,
      "cache_read_input_tokens": 37407,
      "output_tokens": 313,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 9136,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 313,
          "cache_read_input_tokens": 37407,
          "cache_creation_input_tokens": 9136,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 9136
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

_source line 34 · 2026-05-15T17:15:53.878Z_

```json
{
  "parentUuid": "13bf7f85-71e8-42bd-b95d-668d7404fa5a",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "68377c4b-1d50-42c9-ae5e-649c58b7e877",
  "timestamp": "2026-05-15T17:15:53.878Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/reviewer_efaaa6bc",
  "sessionId": "f59020b4-1c0e-4081-9cb3-293eac3560ff",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 35_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[系统通知 — worker_done:worker_paper_research_bib_sync_20260515T171027]: Worker worker_paper_research_bib_sync_20260515T171027 已完成（status=done），请审查 Agent 的处理结果。",
  "leafUuid": "68377c4b-1d50-42c9-ae5e-649c58b7e877",
  "sessionId": "f59020b4-1c0e-4081-9cb3-293eac3560ff"
}
```

---

### Runtime record

_source line 36_

```json
{
  "type": "ai-title",
  "aiTitle": "Review paper research bibliography sync results",
  "sessionId": "f59020b4-1c0e-4081-9cb3-293eac3560ff"
}
```

---

### Assistant

_source line 37 · 2026-05-15T17:16:25.713Z_

<details><summary>Logged reasoning block</summary>

```text
Let me analyze what the worker "worker_paper_research_bib_sync_20260515T171027" did. The task name suggests it was about synchronizing bibliography entries with the literature map/research. Let me check:

1. The `references.bib` file exists and has 385 lines with entries organized by category
2. The `literature_map.yaml` has entries for the same papers

Let me cross-check:
- literature_map.yaml has entries organized into: DIRECT COMPETITORS, METHOD COMPONENTS, ZERO-SHOT NER/RE BASELINES, EVALUATION/BENCHMARKING, SURVEYS


- references.bib has the same structure plus additional sections: EMBEDDING ANISOTROPY, ADDITIONAL REFERENCES

Now I need to verify that every entry in literature_map.yaml has a corresponding bib entry, check that the bib entries are properly formatted with correct venue types and complete fields, and look for any issues with citation keys or URLs. Let me also check the remote server to see what changes the worker actually made and whether there's a paper directory there.

The worker was focused on syncing bib entries, so I should check if there are entries in the literature_map that aren't in the bib file or vice versa. Looking at the full literature_map, I can see entries organized by category: DIRECT COMPETITORS includes llm-pee-2025, parse-2025, dee-2024, and several others; METHOD COMPONENTS has uniner-2024, gollie-2024, gliner-2024, and related papers; ZERO-SHOT BASELINES covers self-improve-ner-2024, self-prompting-re-2024, and reasoning approaches; EVALUATION includes familiarity-2025 and guidex-2025; and SURVEYS has llm4ie-survey.

Now checking the references.bib file, I can see it contains all those entries plus additional ones not in the literature_map like the embedding anisotropy papers (gao-repr-degen-2019, ethayarajh-contextual-2019, and others), along with instructuie-2023, codeie-2023, adelie-2024, and various other papers on calibration, NER variants, and related topics. So the bib file is more comprehensive than what's currently cataloged in the literature_map.

I'm noticing some inconsistencies that need investigation. For instance, llm-pee-2025 shows as "arXiv" in the literature_map but the bib entry lists it as "EMNLP 2025" with a different URL pointing to aclanthology instead of arxiv—this looks like a legitimate upgrade from preprint to published version. But parse-2025 has the opposite problem: the literature_map says "EMNLP 2025 Industry" while the bib entry claims it's an arXiv preprint, which is a real discrepancy I need to resolve.

I should also verify some of the other entries like dee-2024 and reasoning-ner-2025 to see if their venue information is consistent, and I'm concerned about entries that appear in the bib but not in the literature_map—I need to check whether those are properly verified sources. The literature_map was truncated, so I should pull the full version to make sure I'm not missing anything.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "68377c4b-1d50-42c9-ae5e-649c58b7e877",
  "isSidechain": false,
  "requestId": "req_011Cb4jSczYHdFnwNmZkngqK",
  "type": "assistant",
  "uuid": "2914cc86-c1ba-440e-b749-33fcc53dacdb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/reviewer_efaaa6bc",
  "sessionId": "f59020b4-1c0e-4081-9cb3-293eac3560ff",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HCW11dZXE2VF7r3o7gjr2X",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 8597,
      "cache_read_input_tokens": 46543,
      "output_tokens": 1500,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 8597,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1500,
          "cache_read_input_tokens": 46543,
          "cache_creation_input_tokens": 8597,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 8597
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

_source line 38 · 2026-05-15T17:16:26.653Z_

需要完整的 literature_map 来做交叉校验。同时检查远程服务器上的论文目录状态。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2914cc86-c1ba-440e-b749-33fcc53dacdb",
  "isSidechain": false,
  "requestId": "req_011Cb4jSczYHdFnwNmZkngqK",
  "type": "assistant",
  "uuid": "3c170f1c-29d5-43d3-ae3c-63f03d0d94ff",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/reviewer_efaaa6bc",
  "sessionId": "f59020b4-1c0e-4081-9cb3-293eac3560ff",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HCW11dZXE2VF7r3o7gjr2X",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 8597,
      "cache_read_input_tokens": 46543,
      "output_tokens": 1500,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 8597,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1500,
          "cache_read_input_tokens": 46543,
          "cache_creation_input_tokens": 8597,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 8597
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

_source line 39 · 2026-05-15T17:16:27.665Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01U3Pef8j9FaSKMiriSyQwxb`</summary>

```json
{
  "project": "schema-dag-extraction",
  "file": "literature_map.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3c170f1c-29d5-43d3-ae3c-63f03d0d94ff",
  "isSidechain": false,
  "requestId": "req_011Cb4jSczYHdFnwNmZkngqK",
  "type": "assistant",
  "uuid": "0faafce6-d72c-4006-8b19-190c8ae024bd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/reviewer_efaaa6bc",
  "sessionId": "f59020b4-1c0e-4081-9cb3-293eac3560ff",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HCW11dZXE2VF7r3o7gjr2X",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 8597,
      "cache_read_input_tokens": 46543,
      "output_tokens": 1500,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 8597,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1500,
          "cache_read_input_tokens": 46543,
          "cache_creation_input_tokens": 8597,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 8597
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

_source line 40 · 2026-05-15T17:16:27.690Z_

<details><summary>↩ Tool result · `toolu_01U3Pef8j9FaSKMiriSyQwxb`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/literature_map.yaml\", \"content\": \"# Literature Map for schema-dag-extraction\\n# Updated: 2026-05-15\\n# Paper: Multi-channel Degradation Model + SDGD Framework for Training-free LLM IE\\n\\n# =============================================================================\\n# DIRECT COMPETITORS — schema decomposition for LLM-based IE\\n# =============================================================================\\n\\n- id: llm-pee-2025\\n  title: \\\"Towards Event Extraction with Massive Types: LLM-based Collaborative Annotation and Partitioning Extraction\\\"\\n  year: 2025\\n  venue: arXiv\\n  url: https://arxiv.org/abs/2503.02628\\n  role: direct-competitor\\n  relevance_note: >\\n    Similarity-based type recall + type-partitioning prompting for massive event types.\\n    Divides candidate types into partitions to reduce prompt length.\\n    +5.4% event detection, +6.1% argument extraction, +12.9% F1 over mainstream LLMs zero-shot.\\n    KEY DIFF: partitions by similarity-based recall, NOT confusability-aware.\\n    Our DAG decomposition is confusability-driven, not just similarity-driven.\\n\\n- id: parse-2025\\n  title: \\\"PARSE: LLM Driven Schema Optimization for Reliable Entity Extraction\\\"\\n  authors: [Anubhav Shrimal, Aryan Jain, Soumyajit Chowdhury, Promod Yenigalla]\\n  year: 2025\\n  venue: EMNLP 2025 Industry\\n  url: https://arxiv.org/abs/2510.08623\\n  role: direct-competitor\\n  relevance_note: >\\n    ARCHITECT autonomously rewrites JSON schemas for LLM consumption.\\n    SCOPE uses reflection-based extraction with guardrails. +64.7% on SWDE.\\n    Treats schema optimization as black-box LLM rewriting, not principled decomposition.\\n    Does NOT model type confusability explicitly.\\n\\n- id: dee-2024\\n  title: \\\"Decompose, Enrich, and Extract! Schema-aware Event Extraction using LLMs\\\"\\n  year: 2024\\n  venue: arXiv\\n  url: https://arxiv.org/abs/2406.01045\\n  role: direct-competitor\\n  relevance_note: >\\n    Decomposes event extraction into detection + argument extraction.\\n    Dynamic schema-aware RAG for augmented prompts.\\n    KEY DIFF: task-level decomposition (detection vs argument), not schema-level type decomposition.\\n\\n- id: crossagentie-2025\\n  title: \\\"CROSSAGENTIE: Cross-Type and Cross-Task Multi-Agent LLM Collaboration for Zero-Shot IE\\\"\\n  authors: [Meng Lu, Yuzhang Xie, Zhenyu Bi, Shuxiang Cao, Xuan Wang]\\n  year: 2025\\n  venue: ACL 2025 Findings\\n  url: https://aclanthology.org/2025.findings-acl.718/\\n  role: direct-competitor\\n  relevance_note: >\\n    Multi-agent: intra-group cross-type debate (resolves entity-label conflicts)\\n    + inter-group cross-task debate (NER↔RE mutual refinement).\\n    ⚠️ MODERATE NOVELTY CONCERN: cross-type debate explicitly addresses type confusion.\\n    KEY DIFF: reactive debate to resolve confusion post-hoc vs our proactive decomposition to prevent it.\\n    Must clearly differentiate in paper.\\n\\n- id: dlisc-2025\\n  title: \\\"Effective and Efficient Schema-aware Information Extraction Using On-Device LLMs\\\"\\n  year: 2025\\n  venue: arXiv (May 2025)\\n  url: https://arxiv.org/abs/2505.14992\\n  role: direct-competitor\\n  relevance_note: >\\n    Dual-LoRA with Incremental Schema Caching.\\n    Identification LoRA retrieves relevant schemas, Extraction LoRA performs IE.\\n    Focus on efficiency for on-device LLMs, not confusability analysis.\\n\\n- id: spt-2025\\n  title: \\\"Schema as Parameterized Tools for Universal Information Extraction\\\"\\n  year: 2025\\n  venue: arXiv (June 2025)\\n  url: https://arxiv.org/abs/2506.01276\\n  role: direct-competitor\\n  relevance_note: >\\n    Treats schemas as parameterized tools for LLM tool-calling.\\n    Schema retrieval + generation + infilling. Novel schema-LLM interface.\\n    Does not address type confusability.\\n\\n- id: zeroner-2025\\n  title: \\\"ZeroNER: Fueling Zero-Shot NER via Entity Type Descriptions\\\"\\n  year: 2025\\n  venue: ACL 2025 Findings\\n  url: https://aclanthology.org/2025.findings-acl.805/\\n  role: direct-competitor\\n  relevance_note: >\\n    Description-driven: LLM supervision → BERT student for unseen types.\\n    +16% F1 over LLMs on hard zero-shot. Leverages type descriptions.\\n    Related to how schema semantics affect extraction quality.\\n\\n- id: cmas-ner-2025\\n  title: \\\"A Cooperative Multi-Agent Framework for Zero-Shot Named Entity Recognition\\\"\\n  year: 2025\\n  venue: TheWebConf 2025\\n  url: https://dl.acm.org/doi/10.1145/3696410.3714923\\n  role: direct-competitor\\n  relevance_note: >\\n    Multi-agent collective intelligence for zero-shot NER.\\n    Addresses context correlation and indiscriminate demonstration problems.\\n    Outperforms on 6 benchmarks including domain-specific and general-domain.\\n\\n# =============================================================================\\n# METHOD COMPONENTS — techniques we build upon or relate to\\n# =============================================================================\\n\\n- id: uniner-2024\\n  title: \\\"UniversalNER: Targeted Distillation from Large Language Models for Open NER\\\"\\n  authors: [Wenxuan Zhou et al.]\\n  year: 2024\\n  venue: ICLR 2024\\n  url: https://arxiv.org/abs/2308.03279\\n  role: method-component\\n  relevance_note: >\\n    Instruction-tuning on ChatGPT-generated NER data. 43 datasets, 9 domains, 13K+ types.\\n    UniNER-7B outperforms ChatGPT by 7 F1 points.\\n    Important baseline for universal NER and schema-at-scale challenges.\\n\\n- id: gollie-2024\\n  title: \\\"GoLLIE: Annotation Guidelines Following Large Language Model for Information Extraction\\\"\\n  authors: [Oscar Sainz et al.]\\n  year: 2024\\n  venue: ICLR 2024\\n  url: https://hitz-zentroa.github.io/GoLLIE/\\n  role: method-component\\n  relevance_note: >\\n    Code-style schema definitions + annotation guideline following.\\n    Strong zero-shot on unseen IE tasks. Code-Llama based.\\n    Baseline for guideline-driven schema representation.\\n\\n- id: gliner-2024\\n  title: \\\"GLiNER: Generalist Model for Named Entity Recognition using Bidirectional Transformer\\\"\\n  authors: [Urchade Zaratiana et al.]\\n  year: 2024\\n  venue: NAACL 2024\\n  url: https://arxiv.org/abs/2311.08526\\n  role: method-component\\n  relevance_note: >\\n    Compact bidirectional encoder for zero-shot NER with parallel extraction.\\n    Outperforms InstructUIE and larger models. Non-LLM competitive baseline.\\n\\n- id: gliner2-2025\\n  title: \\\"GLiNER2: Efficient Multi-Task IE System with Schema-Driven Interface\\\"\\n  authors: [Urchade Zaratiana et al.]\\n  year: 2025\\n  venue: EMNLP 2025 Demo\\n  url: https://arxiv.org/abs/2507.18546\\n  role: method-component\\n  relevance_note: >\\n    Extends GLiNER to multi-task IE (NER+RE+classification). 205M params, CPU-efficient.\\n    Schema-driven interface. Shows schema approach scales to multi-task.\\n\\n- id: kggen-2025\\n  title: \\\"KGGen: Extracting Knowledge Graphs from Plain Text with Language Models\\\"\\n  authors: [Mo et al.]\\n  year: 2025\\n  venue: NeurIPS 2025\\n  url: https://arxiv.org/abs/2502.09956\\n  role: method-component\\n  relevance_note: >\\n    Two-stage decomposition: entities first, then relations.\\n    Entity clustering/deduplication to reduce graph sparsity.\\n    Schema decomposition approach for KG construction.\\n\\n- id: code4uie-2024\\n  title: \\\"Retrieval-Augmented Code Generation for Universal Information Extraction\\\"\\n  authors: [Yucan Guo et al.]\\n  year: 2024\\n  venue: NeurIPS 2024 Workshop\\n  url: https://arxiv.org/abs/2311.02962\\n  role: method-component\\n  relevance_note: >\\n    Python class-based schema definitions + RAG for code generation.\\n    Unified code-style schema for all IE tasks.\\n\\n- id: iepile-2024\\n  title: \\\"IEPile: Unearthing Large-Scale Schema-Based Information Extraction Corpus\\\"\\n  authors: [Guanzheng Chen et al., ZJU NLP]\\n  year: 2024\\n  venue: ACL 2024\\n  url: https://arxiv.org/abs/2402.14710\\n  role: method-component\\n  relevance_note: >\\n    0.32B token bilingual IE corpus. Hard negative schema construction =\\n    semantically proximate schemas to train type discrimination.\\n    ⚠️ RELATED: hard negatives ≈ confusable schemas, but for TRAINING, not inference-time.\\n    Our contribution is inference-time confusability-aware decomposition (training-free).\\n\\n- id: lost-in-middle-2024\\n  title: \\\"Lost in the Middle: How Language Models Use Long Contexts\\\"\\n  authors: [Nelson F. Liu et al.]\\n  year: 2024\\n  venue: TACL 2024\\n  url: https://arxiv.org/abs/2307.03172\\n  role: method-component\\n  relevance_note: >\\n    LLMs degrade when relevant info is in middle of long contexts (U-shaped attention).\\n    Motivates schema decomposition to reduce prompt length.\\n    No IE-specific follow-up found — opportunity for us to be first to connect this to IE.\\n\\n# =============================================================================\\n# ZERO-SHOT NER / RE BASELINES\\n# =============================================================================\\n\\n- id: self-improve-ner-2024\\n  title: \\\"Self-Improving for Zero-Shot Named Entity Recognition with Large Language Models\\\"\\n  year: 2024\\n  venue: NAACL 2024\\n  url: https://arxiv.org/abs/2311.08921\\n  role: background\\n  relevance_note: >\\n    Self-improving framework using LLM self-generated examples for zero-shot NER.\\n\\n- id: self-prompting-re-2024\\n  title: \\\"Unleashing the Power of LLMs in Zero-shot Relation Extraction via Self-Prompting\\\"\\n  year: 2024\\n  venue: EMNLP 2024 Findings\\n  url: https://arxiv.org/abs/2410.01154\\n  role: background\\n  relevance_note: >\\n    Three-stage self-prompting for zero-shot RE. Generates synthetic ICL samples.\\n    Training-free RE baseline.\\n\\n- id: reasoning-ner-2025\\n  title: \\\"A Reasoning Paradigm for Named Entity Recognition\\\"\\n  year: 2025\\n  venue: arXiv (Nov 2025)\\n  url: https://arxiv.org/abs/2511.11978\\n  role: background\\n  relevance_note: >\\n    CoT-based reasoning for NER. Outperforms GPT-4 by 12.3 F1 in zero-shot.\\n    Shifts NER from pattern matching to explicit reasoning. Strong zero-shot baseline.\\n\\n- id: nuner-2024\\n  title: \\\"NuNER: Entity Recognition Encoder Pre-training via LLM-Annotated Data\\\"\\n  authors: [Sergei Bogdanov et al., NuMind]\\n  year: 2024\\n  venue: EMNLP 2024\\n  url: https://arxiv.org/abs/2402.15343\\n  role: background\\n  relevance_note: >\\n    Contrastive pre-training on LLM-annotated data. Strong few-shot NER foundation model.\\n\\n# =============================================================================\\n# EVALUATION / BENCHMARKING\\n# =============================================================================\\n\\n- id: familiarity-2025\\n  title: \\\"Familiarity: Better Evaluation of Zero-Shot NER by Quantifying Label Shifts in Synthetic Training Data\\\"\\n  year: 2025\\n  venue: NAACL 2025\\n  url: https://arxiv.org/abs/2412.10121\\n  role: evaluation\\n  relevance_note: >\\n    \\\"Familiarity\\\" metric for label shift in synthetic NER data.\\n    Zero-shot NER scores overestimated due to train-eval label overlap.\\n    Quantifies semantic similarity between entity types — related to type confusability.\\n    KEY DIFF: measures evaluation bias, not extraction-time confusability.\\n\\n- id: guidex-2025\\n  title: \\\"GuideX: Guided Synthetic Data Generation for Zero-Shot Information Extraction\\\"\\n  authors: [Neil Deshpande et al.]\\n  year: 2025\\n  venue: ACL 2025 Findings\\n  url: https://arxiv.org/abs/2506.00649\\n  role: evaluation\\n  relevance_note: >\\n    Auto-generates domain-specific schemas + guidelines + synthetic labels.\\n    SOTA on 7 zero-shot NER benchmarks (+7 F1). Strong baseline.\\n\\n# =============================================================================\\n# SURVEYS\\n# =============================================================================\\n\\n- id: llm4ie-survey-2024\\n  title: \\\"Large Language Models for Generative Information Extraction: A Survey\\\"\\n  authors: [Derong Xu et al.]\\n  year: 2024\\n  venue: Frontiers of Computer Science\\n  url: https://arxiv.org/abs/2312.17617\\n  role: background\\n  relevance_note: >\\n    Comprehensive survey of LLM-based IE covering prompting, fine-tuning, benchmarks.\\n\\n- id: knowcoder-2024\\n  title: \\\"KnowCoder: Coding Structured Knowledge into LLMs for Universal IE\\\"\\n  year: 2024\\n  venue: ACL 2024\\n  url: https://arxiv.org/abs/2403.07969\\n  role: background\\n  relevance_note: >\\n    Encodes schema knowledge via code structures into LLM.\\n    Related to code-based schema representation.\\n\\n- id: slot-2025\\n  title: \\\"SLOT: Structuring the Output of Large Language Models\\\"\\n  year: 2025\\n  venue: EMNLP 2025 Industry\\n  url: https://aclanthology.org/2025.emnlp-industry.32.pdf\\n  role: background\\n  relevance_note: >\\n    Decouples output formatting from NL task. Model-agnostic structured output.\\n\\n# =============================================================================\\n# EMBEDDING ANISOTROPY / REPRESENTATION DEGENERATION\\n# — supports \\\"domain boundary\\\" finding: BCS proxy fails for same-domain schemas\\n# =============================================================================\\n\\n- id: gao-repr-degen-2019\\n  title: \\\"Representation Degeneration Problem in Training Natural Language Generation Models\\\"\\n  authors: [Jun Gao, Di He, Hang Li, Xin Jiang]\\n  year: 2019\\n  venue: ICLR 2019\\n  url: https://arxiv.org/abs/1907.12009\\n  role: theoretical-foundation\\n  relevance_note: >\\n    FOUNDATIONAL. Shows that likelihood maximization + weight tying causes word embeddings\\n    to degenerate into a narrow cone with uniformly high cosine similarity.\\n    Proposed cosine regularization (MLE-CosReg) to widen the cone aperture.\\n    LINK TO OUR WORK: This is the root mechanism behind BCS compression.\\n    When Qwen3-32B encodes 168 same-domain FrameNet types, the degeneration effect\\n    concentrates them into the same narrow cone (cosine ≥ 0.90), destroying BCS discriminability.\\n    Cite as the theoretical explanation for why embedding-based confusability proxies\\n    have a principled failure mode on semantically homogeneous schemas.\\n\\n- id: ethayarajh-contextual-2019\\n  title: \\\"How Contextual are Contextualized Word Representations? Comparing the Geometry of BERT, ELMo, and GPT-2 Embeddings\\\"\\n  authors: [Kawin Ethayarajh]\\n  year: 2019\\n  venue: EMNLP 2019\\n  url: https://aclanthology.org/D19-1006/\\n  role: theoretical-foundation\\n  relevance_note: >\\n    Shows contextualized representations are anisotropic in ALL layers of BERT/ELMo/GPT-2.\\n    Upper layers are more context-specific but still not isotropic.\\n    Introduces quantitative measures of anisotropy (avg cosine sim of random word pairs).\\n    LINK TO OUR WORK: Establishes that anisotropy is pervasive across architectures —\\n    our MAVEN embedding compression is not a Qwen-specific artifact but a general property.\\n    Supports the argument that ANY embedding-based confusability proxy inherits this limitation.\\n\\n- id: cai-isotropy-clusters-2021\\n  title: \\\"Isotropy in the Contextual Embedding Space: Clusters and Manifolds\\\"\\n  authors: [Xingyu Cai, Jiaji Huang, Yuchen Bian, Kenneth Church]\\n  year: 2021\\n  venue: ICLR 2021\\n  url: https://openreview.net/forum?id=xYGNO86OWDH\\n  role: theoretical-foundation\\n  relevance_note: >\\n    ⭐ MOST DIRECTLY RELEVANT. Key insight: global anisotropy is caused by isolated clusters;\\n    WITHIN each cluster, embeddings are locally more isotropic.\\n    Resolution: the high average cosine similarity reported in prior work is an artifact of\\n    mixing embeddings from different clusters — within-cluster geometry is better behaved.\\n    LINK TO OUR WORK: This is the exact mechanism for our \\\"domain boundary\\\" finding.\\n    Cross-domain schemas (ACE vs FewNERD) span DIFFERENT clusters → BCS captures real\\n    inter-cluster distances → proxy works. Same-domain schemas (MAVEN FrameNet types)\\n    fall within ONE cluster → within-cluster variance is low → cosine sim saturates ≥ 0.90\\n    → BCS loses discriminability. Our empirical finding is a direct instantiation of their\\n    theoretical framework applied to type-level (not token-level) embeddings.\\n\\n- id: godey-anisotropy-inherent-2024\\n  title: \\\"Anisotropy Is Inherent to Self-Attention in Transformers\\\"\\n  authors: [Nathan Godey, Éric de la Clergerie, Benoît Sagot]\\n  year: 2024\\n  venue: EACL 2024\\n  url: https://aclanthology.org/2024.eacl-long.3/\\n  role: theoretical-foundation\\n  relevance_note: >\\n    Proves anisotropy is inherent to the self-attention mechanism itself, not just a\\n    consequence of cross-entropy training on long-tailed token distributions.\\n    Observed across modalities (NLP, vision), ruling out data-distribution explanations.\\n    LINK TO OUR WORK: Strengthens the argument that BCS compression is a fundamental\\n    architectural limitation, not fixable by better prompting or model choice.\\n    Supports our position that structural decomposition (SDGD) is necessary precisely\\n    because the embedding space has inherent geometric constraints.\\n\\n- id: rajaee-cluster-isotropy-2021\\n  title: \\\"A Cluster-based Approach for Improving Isotropy in Contextual Embedding Space\\\"\\n  authors: [Sara Rajaee, Mohammad Taher Pilehvar]\\n  year: 2021\\n  venue: ACL 2021\\n  url: https://aclanthology.org/2021.acl-short.73/\\n  role: theoretical-foundation\\n  relevance_note: >\\n    Shows local (within-cluster) assessment of isotropy is more accurate than global assessment.\\n    Cluster-specific dominant directions encode structural (not semantic) information;\\n    removing them improves semantic task performance.\\n    LINK TO OUR WORK: Supports that within a semantic domain (one cluster), the dominant\\n    directions capture domain-level features rather than fine-grained type distinctions.\\n    This explains why MAVEN type embeddings are compressed: the shared \\\"event-ness\\\"\\n    dominates over type-specific semantics in the local embedding geometry.\\n\\n# =============================================================================\\n# NOVELTY THREAT ASSESSMENT (2026-05-15)\\n# =============================================================================\\n#\\n# 1. \\\"Type count vs type confusability\\\" disentangling:\\n#    ✅ NOVELTY SAFE — No prior work explicitly disentangles these two factors.\\n#    - IEPILE hard negatives: closest, but for training, not inference-time decomposition.\\n#    - Familiarity metric: measures label similarity for evaluation bias, not extraction.\\n#    - CROSSAGENTIE: resolves type confusion via debate, doesn't model as degradation channel.\\n#    Our multi-channel degradation model (count + confusability + context) is novel.\\n#\\n# 2. Schema decomposition baselines to compare:\\n#    - LLM-PEE (similarity partitioning) — MUST compare\\n#    - PARSE (LLM-driven schema rewriting) — MUST compare\\n#    - DEE (task-level decomposition) — discuss in related work\\n#    - SPT (schema as tools) — discuss in related work\\n#    - DLISC (Dual-LoRA schema caching) — discuss in related work\\n#\\n# 3. \\\"Lost in the Middle\\\" for IE:\\n#    ✅ OPPORTUNITY — No follow-up work applying it to IE task found.\\n#    We can be first to connect positional bias to schema prompt design.\\n#\\n# 4. Multi-agent approaches (CROSSAGENTIE, CMAS):\\n#    Growing area. Position clearly: we reduce confusion proactively via decomposition,\\n#    they resolve it reactively via debate. Complementary, not conflicting.\\n#\\n# 5. Overall novelty position:\\n#    STRONG — no prior work proposes (a) a formal multi-channel degradation model for\\n#    schema complexity in LLM IE, or (b) a DAG-based schema decomposition optimized\\n#    for type confusability. Main risk is CROSSAGENTIE's cross-type debate framing.\\n\", \"total_chars\": 18972, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0faafce6-d72c-4006-8b19-190c8ae024bd",
  "isSidechain": false,
  "promptId": "b593ab42-40aa-4651-8f99-a82b6d6b969a",
  "type": "user",
  "uuid": "62e27dc6-9294-443c-86f9-3e87f83f551b",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/literature_map.yaml\\\", \\\"content\\\": \\\"# Literature Map for schema-dag-extraction\\\\n# Updated: 2026-05-15\\\\n# Paper: Multi-channel Degradation Model + SDGD Framework for Training-free LLM IE\\\\n\\\\n# =============================================================================\\\\n# DIRECT COMPETITORS — schema decomposition for LLM-based IE\\\\n# =============================================================================\\\\n\\\\n- id: llm-pee-2025\\\\n  title: \\\\\\\"Towards Event Extraction with Massive Types: LLM-based Collaborative Annotation and Partitioning Extraction\\\\\\\"\\\\n  year: 2025\\\\n  venue: arXiv\\\\n  url: https://arxiv.org/abs/2503.02628\\\\n  role: direct-competitor\\\\n  relevance_note: >\\\\n    Similarity-based type recall + type-partitioning prompting for massive event types.\\\\n    Divides candidate types into partitions to reduce prompt length.\\\\n    +5.4% event detection, +6.1% argument extraction, +12.9% F1 over mainstream LLMs zero-shot.\\\\n    KEY DIFF: partitions by similarity-based recall, NOT confusability-aware.\\\\n    Our DAG decomposition is confusability-driven, not just similarity-driven.\\\\n\\\\n- id: parse-2025\\\\n  title: \\\\\\\"PARSE: LLM Driven Schema Optimization for Reliable Entity Extraction\\\\\\\"\\\\n  authors: [Anubhav Shrimal, Aryan Jain, Soumyajit Chowdhury, Promod Yenigalla]\\\\n  year: 2025\\\\n  venue: EMNLP 2025 Industry\\\\n  url: https://arxiv.org/abs/2510.08623\\\\n  role: direct-competitor\\\\n  relevance_note: >\\\\n    ARCHITECT autonomously rewrites JSON schemas for LLM consumption.\\\\n    SCOPE uses reflection-based extraction with guardrails. +64.7% on SWDE.\\\\n    Treats schema optimization as black-box LLM rewriting, not principled decomposition.\\\\n    Does NOT model type confusability explicitly.\\\\n\\\\n- id: dee-2024\\\\n  title: \\\\\\\"Decompose, Enrich, and Extract! Schema-aware Event Extraction using LLMs\\\\\\\"\\\\n  year: 2024\\\\n  venue: arXiv\\\\n  url: https://arxiv.org/abs/2406.01045\\\\n  role: direct-competitor\\\\n  relevance_note: >\\\\n    Decomposes event extraction into detection + argument extraction.\\\\n    Dynamic schema-aware RAG for augmented prompts.\\\\n    KEY DIFF: task-level decomposition (detection vs argument), not schema-level type decomposition.\\\\n\\\\n- id: crossagentie-2025\\\\n  title: \\\\\\\"CROSSAGENTIE: Cross-Type and Cross-Task Multi-Agent LLM Collaboration for Zero-Shot IE\\\\\\\"\\\\n  authors: [Meng Lu, Yuzhang Xie, Zhenyu Bi, Shuxiang Cao, Xuan Wang]\\\\n  year: 2025\\\\n  venue: ACL 2025 Findings\\\\n  url: https://aclanthology.org/2025.findings-acl.718/\\\\n  role: direct-competitor\\\\n  relevance_note: >\\\\n    Multi-agent: intra-group cross-type debate (resolves entity-label conflicts)\\\\n    + inter-group cross-task debate (NER↔RE mutual refinement).\\\\n    ⚠️ MODERATE NOVELTY CONCERN: cross-type debate explicitly addresses type confusion.\\\\n    KEY DIFF: reactive debate to resolve confusion post-hoc vs our proactive decomposition to prevent it.\\\\n    Must clearly differentiate in paper.\\\\n\\\\n- id: dlisc-2025\\\\n  title: \\\\\\\"Effective and Efficient Schema-aware Information Extraction Using On-Device LLMs\\\\\\\"\\\\n  year: 2025\\\\n  venue: arXiv (May 2025)\\\\n  url: https://arxiv.org/abs/2505.14992\\\\n  role: direct-competitor\\\\n  relevance_note: >\\\\n    Dual-LoRA with Incremental Schema Caching.\\\\n    Identification LoRA retrieves relevant schemas, Extraction LoRA performs IE.\\\\n    Focus on efficiency for on-device LLMs, not confusability analysis.\\\\n\\\\n- id: spt-2025\\\\n  title: \\\\\\\"Schema as Parameterized Tools for Universal Information Extraction\\\\\\\"\\\\n  year: 2025\\\\n  venue: arXiv (June 2025)\\\\n  url: https://arxiv.org/abs/2506.01276\\\\n  role: direct-competitor\\\\n  relevance_note: >\\\\n    Treats schemas as parameterized tools for LLM tool-calling.\\\\n    Schema retrieval + generation + infilling. Novel schema-LLM interface.\\\\n    Does not address type confusability.\\\\n\\\\n- id: zeroner-2025\\\\n  title: \\\\\\\"ZeroNER: Fueling Zero-Shot NER via Entity Type Descriptions\\\\\\\"\\\\n  year: 2025\\\\n  venue: ACL 2025 Findings\\\\n  url: https://aclanthology.org/2025.findings-acl.805/\\\\n  role: direct-competitor\\\\n  relevance_note: >\\\\n    Description-driven: LLM supervision → BERT student for unseen types.\\\\n    +16% F1 over LLMs on hard zero-shot. Leverages type descriptions.\\\\n    Related to how schema semantics affect extraction quality.\\\\n\\\\n- id: cmas-ner-2025\\\\n  title: \\\\\\\"A Cooperative Multi-Agent Framework for Zero-Shot Named Entity Recognition\\\\\\\"\\\\n  year: 2025\\\\n  venue: TheWebConf 2025\\\\n  url: https://dl.acm.org/doi/10.1145/3696410.3714923\\\\n  role: direct-competitor\\\\n  relevance_note: >\\\\n    Multi-agent collective intelligence for zero-shot NER.\\\\n    Addresses context correlation and indiscriminate demonstration problems.\\\\n    Outperforms on 6 benchmarks including domain-specific and general-domain.\\\\n\\\\n# =============================================================================\\\\n# METHOD COMPONENTS — techniques we build upon or relate to\\\\n# =============================================================================\\\\n\\\\n- id: uniner-2024\\\\n  title: \\\\\\\"UniversalNER: Targeted Distillation from Large Language Models for Open NER\\\\\\\"\\\\n  authors: [Wenxuan Zhou et al.]\\\\n  year: 2024\\\\n  venue: ICLR 2024\\\\n  url: https://arxiv.org/abs/2308.03279\\\\n  role: method-component\\\\n  relevance_note: >\\\\n    Instruction-tuning on ChatGPT-generated NER data. 43 datasets, 9 domains, 13K+ types.\\\\n    UniNER-7B outperforms ChatGPT by 7 F1 points.\\\\n    Important baseline for universal NER and schema-at-scale challenges.\\\\n\\\\n- id: gollie-2024\\\\n  title: \\\\\\\"GoLLIE: Annotation Guidelines Following Large Language Model for Information Extraction\\\\\\\"\\\\n  authors: [Oscar Sainz et al.]\\\\n  year: 2024\\\\n  venue: ICLR 2024\\\\n  url: https://hitz-zentroa.github.io/GoLLIE/\\\\n  role: method-component\\\\n  relevance_note: >\\\\n    Code-style schema definitions + annotation guideline following.\\\\n    Strong zero-shot on unseen IE tasks. Code-Llama based.\\\\n    Baseline for guideline-driven schema representation.\\\\n\\\\n- id: gliner-2024\\\\n  title: \\\\\\\"GLiNER: Generalist Model for Named Entity Recognition using Bidirectional Transformer\\\\\\\"\\\\n  authors: [Urchade Zaratiana et al.]\\\\n  year: 2024\\\\n  venue: NAACL 2024\\\\n  url: https://arxiv.org/abs/2311.08526\\\\n  role: method-component\\\\n  relevance_note: >\\\\n    Compact bidirectional encoder for zero-shot NER with parallel extraction.\\\\n    Outperforms InstructUIE and larger models. Non-LLM competitive baseline.\\\\n\\\\n- id: gliner2-2025\\\\n  title: \\\\\\\"GLiNER2: Efficient Multi-Task IE System with Schema-Driven Interface\\\\\\\"\\\\n  authors: [Urchade Zaratiana et al.]\\\\n  year: 2025\\\\n  venue: EMNLP 2025 Demo\\\\n  url: https://arxiv.org/abs/2507.18546\\\\n  role: method-component\\\\n  relevance_note: >\\\\n    Extends GLiNER to multi-task IE (NER+RE+classification). 205M params, CPU-efficient.\\\\n    Schema-driven interface. Shows schema approach scales to multi-task.\\\\n\\\\n- id: kggen-2025\\\\n  title: \\\\\\\"KGGen: Extracting Knowledge Graphs from Plain Text with Language Models\\\\\\\"\\\\n  authors: [Mo et al.]\\\\n  year: 2025\\\\n  venue: NeurIPS 2025\\\\n  url: https://arxiv.org/abs/2502.09956\\\\n  role: method-component\\\\n  relevance_note: >\\\\n    Two-stage decomposition: entities first, then relations.\\\\n    Entity clustering/deduplication to reduce graph sparsity.\\\\n    Schema decomposition approach for KG construction.\\\\n\\\\n- id: code4uie-2024\\\\n  title: \\\\\\\"Retrieval-Augmented Code Generation for Universal Information Extraction\\\\\\\"\\\\n  authors: [Yucan Guo et al.]\\\\n  year: 2024\\\\n  venue: NeurIPS 2024 Workshop\\\\n  url: https://arxiv.org/abs/2311.02962\\\\n  role: method-component\\\\n  relevance_note: >\\\\n    Python class-based schema definitions + RAG for code generation.\\\\n    Unified code-style schema for all IE tasks.\\\\n\\\\n- id: iepile-2024\\\\n  title: \\\\\\\"IEPile: Unearthing Large-Scale Schema-Based Information Extraction Corpus\\\\\\\"\\\\n  authors: [Guanzheng Chen et al., ZJU NLP]\\\\n  year: 2024\\\\n  venue: ACL 2024\\\\n  url: https://arxiv.org/abs/2402.14710\\\\n  role: method-component\\\\n  relevance_note: >\\\\n    0.32B token bilingual IE corpus. Hard negative schema construction =\\\\n    semantically proximate schemas to train type discrimination.\\\\n    ⚠️ RELATED: hard negatives ≈ confusable schemas, but for TRAINING, not inference-time.\\\\n    Our contribution is inference-time confusability-aware decomposition (training-free).\\\\n\\\\n- id: lost-in-middle-2024\\\\n  title: \\\\\\\"Lost in the Middle: How Language Models Use Long Contexts\\\\\\\"\\\\n  authors: [Nelson F. Liu et al.]\\\\n  year: 2024\\\\n  venue: TACL 2024\\\\n  url: https://arxiv.org/abs/2307.03172\\\\n  role: method-component\\\\n  relevance_note: >\\\\n    LLMs degrade when relevant info is in middle of long contexts (U-shaped attention).\\\\n    Motivates schema decomposition to reduce prompt length.\\\\n    No IE-specific follow-up found — opportunity for us to be first to connect this to IE.\\\\n\\\\n# =============================================================================\\\\n# ZERO-SHOT NER / RE BASELINES\\\\n# =============================================================================\\\\n\\\\n- id: self-improve-ner-2024\\\\n  title: \\\\\\\"Self-Improving for Zero-Shot Named Entity Recognition with Large Language Models\\\\\\\"\\\\n  year: 2024\\\\n  venue: NAACL 2024\\\\n  url: https://arxiv.org/abs/2311.08921\\\\n  role: background\\\\n  relevance_note: >\\\\n    Self-improving framework using LLM self-generated examples for zero-shot NER.\\\\n\\\\n- id: self-prompting-re-2024\\\\n  title: \\\\\\\"Unleashing the Power of LLMs in Zero-shot Relation Extraction via Self-Prompting\\\\\\\"\\\\n  year: 2024\\\\n  venue: EMNLP 2024 Findings\\\\n  url: https://arxiv.org/abs/2410.01154\\\\n  role: background\\\\n  relevance_note: >\\\\n    Three-stage self-prompting for zero-shot RE. Generates synthetic ICL samples.\\\\n    Training-free RE baseline.\\\\n\\\\n- id: reasoning-ner-2025\\\\n  title: \\\\\\\"A Reasoning Paradigm for Named Entity Recognition\\\\\\\"\\\\n  year: 2025\\\\n  venue: arXiv (Nov 2025)\\\\n  url: https://arxiv.org/abs/2511.11978\\\\n  role: background\\\\n  relevance_note: >\\\\n    CoT-based reasoning for NER. Outperforms GPT-4 by 12.3 F1 in zero-shot.\\\\n    Shifts NER from pattern matching to explicit reasoning. Strong zero-shot baseline.\\\\n\\\\n- id: nuner-2024\\\\n  title: \\\\\\\"NuNER: Entity Recognition Encoder Pre-training via LLM-Annotated Data\\\\\\\"\\\\n  authors: [Sergei Bogdanov et al., NuMind]\\\\n  year: 2024\\\\n  venue: EMNLP 2024\\\\n  url: https://arxiv.org/abs/2402.15343\\\\n  role: background\\\\n  relevance_note: >\\\\n    Contrastive pre-training on LLM-annotated data. Strong few-shot NER foundation model.\\\\n\\\\n# =============================================================================\\\\n# EVALUATION / BENCHMARKING\\\\n# =============================================================================\\\\n\\\\n- id: familiarity-2025\\\\n  title: \\\\\\\"Familiarity: Better Evaluation of Zero-Shot NER by Quantifying Label Shifts in Synthetic Training Data\\\\\\\"\\\\n  year: 2025\\\\n  venue: NAACL 2025\\\\n  url: https://arxiv.org/abs/2412.10121\\\\n  role: evaluation\\\\n  relevance_note: >\\\\n    \\\\\\\"Familiarity\\\\\\\" metric for label shift in synthetic NER data.\\\\n    Zero-shot NER scores overestimated due to train-eval label overlap.\\\\n    Quantifies semantic similarity between entity types — related to type confusability.\\\\n    KEY DIFF: measures evaluation bias, not extraction-time confusability.\\\\n\\\\n- id: guidex-2025\\\\n  title: \\\\\\\"GuideX: Guided Synthetic Data Generation for Zero-Shot Information Extraction\\\\\\\"\\\\n  authors: [Neil Deshpande et al.]\\\\n  year: 2025\\\\n  venue: ACL 2025 Findings\\\\n  url: https://arxiv.org/abs/2506.00649\\\\n  role: evaluation\\\\n  relevance_note: >\\\\n    Auto-generates domain-specific schemas + guidelines + synthetic labels.\\\\n    SOTA on 7 zero-shot NER benchmarks (+7 F1). Strong baseline.\\\\n\\\\n# =============================================================================\\\\n# SURVEYS\\\\n# =============================================================================\\\\n\\\\n- id: llm4ie-survey-2024\\\\n  title: \\\\\\\"Large Language Models for Generative Information Extraction: A Survey\\\\\\\"\\\\n  authors: [Derong Xu et al.]\\\\n  year: 2024\\\\n  venue: Frontiers of Computer Science\\\\n  url: https://arxiv.org/abs/2312.17617\\\\n  role: background\\\\n  relevance_note: >\\\\n    Comprehensive survey of LLM-based IE covering prompting, fine-tuning, benchmarks.\\\\n\\\\n- id: knowcoder-2024\\\\n  title: \\\\\\\"KnowCoder: Coding Structured Knowledge into LLMs for Universal IE\\\\\\\"\\\\n  year: 2024\\\\n  venue: ACL 2024\\\\n  url: https://arxiv.org/abs/2403.07969\\\\n  role: background\\\\n  relevance_note: >\\\\n    Encodes schema knowledge via code structures into LLM.\\\\n    Related to code-based schema representation.\\\\n\\\\n- id: slot-2025\\\\n  title: \\\\\\\"SLOT: Structuring the Output of Large Language Models\\\\\\\"\\\\n  year: 2025\\\\n  venue: EMNLP 2025 Industry\\\\n  url: https://aclanthology.org/2025.emnlp-industry.32.pdf\\\\n  role: background\\\\n  relevance_note: >\\\\n    Decouples output formatting from NL task. Model-agnostic structured output.\\\\n\\\\n# =============================================================================\\\\n# EMBEDDING ANISOTROPY / REPRESENTATION DEGENERATION\\\\n# — supports \\\\\\\"domain boundary\\\\\\\" finding: BCS proxy fails for same-domain schemas\\\\n# =============================================================================\\\\n\\\\n- id: gao-repr-degen-2019\\\\n  title: \\\\\\\"Representation Degeneration Problem in Training Natural Language Generation Models\\\\\\\"\\\\n  authors: [Jun Gao, Di He, Hang Li, Xin Jiang]\\\\n  year: 2019\\\\n  venue: ICLR 2019\\\\n  url: https://arxiv.org/abs/1907.12009\\\\n  role: theoretical-foundation\\\\n  relevance_note: >\\\\n    FOUNDATIONAL. Shows that likelihood maximization + weight tying causes word embeddings\\\\n    to degenerate into a narrow cone with uniformly high cosine similarity.\\\\n    Proposed cosine regularization (MLE-CosReg) to widen the cone aperture.\\\\n    LINK TO OUR WORK: This is the root mechanism behind BCS compression.\\\\n    When Qwen3-32B encodes 168 same-domain FrameNet types, the degeneration effect\\\\n    concentrates them into the same narrow cone (cosine ≥ 0.90), destroying BCS discriminability.\\\\n    Cite as the theoretical explanation for why embedding-based confusability proxies\\\\n    have a principled failure mode on semantically homogeneous schemas.\\\\n\\\\n- id: ethayarajh-contextual-2019\\\\n  title: \\\\\\\"How Contextual are Contextualized Word Representations? Comparing the Geometry of BERT, ELMo, and GPT-2 Embeddings\\\\\\\"\\\\n  authors: [Kawin Ethayarajh]\\\\n  year: 2019\\\\n  venue: EMNLP 2019\\\\n  url: https://aclanthology.org/D19-1006/\\\\n  role: theoretical-foundation\\\\n  relevance_note: >\\\\n    Shows contextualized representations are anisotropic in ALL layers of BERT/ELMo/GPT-2.\\\\n    Upper layers are more context-specific but still not isotropic.\\\\n    Introduces quantitative measures of anisotropy (avg cosine sim of random word pairs).\\\\n    LINK TO OUR WORK: Establishes that anisotropy is pervasive across architectures —\\\\n    our MAVEN embedding compression is not a Qwen-specific artifact but a general property.\\\\n    Supports the argument that ANY embedding-based confusability proxy inherits this limitation.\\\\n\\\\n- id: cai-isotropy-clusters-2021\\\\n  title: \\\\\\\"Isotropy in the Contextual Embedding Space: Clusters and Manifolds\\\\\\\"\\\\n  authors: [Xingyu Cai, Jiaji Huang, Yuchen Bian, Kenneth Church]\\\\n  year: 2021\\\\n  venue: ICLR 2021\\\\n  url: https://openreview.net/forum?id=xYGNO86OWDH\\\\n  role: theoretical-foundation\\\\n  relevance_note: >\\\\n    ⭐ MOST DIRECTLY RELEVANT. Key insight: global anisotropy is caused by isolated clusters;\\\\n    WITHIN each cluster, embeddings are locally more isotropic.\\\\n    Resolution: the high average cosine similarity reported in prior work is an artifact of\\\\n    mixing embeddings from different clusters — within-cluster geometry is better behaved.\\\\n    LINK TO OUR WORK: This is the exact mechanism for our \\\\\\\"domain boundary\\\\\\\" finding.\\\\n    Cross-domain schemas (ACE vs FewNERD) span DIFFERENT clusters → BCS captures real\\\\n    inter-cluster distances → proxy works. Same-domain schemas (MAVEN FrameNet types)\\\\n    fall within ONE cluster → within-cluster variance is low → cosine sim saturates ≥ 0.90\\\\n    → BCS loses discriminability. Our empirical finding is a direct instantiation of their\\\\n    theoretical framework applied to type-level (not token-level) embeddings.\\\\n\\\\n- id: godey-anisotropy-inherent-2024\\\\n  title: \\\\\\\"Anisotropy Is Inherent to Self-Attention in Transformers\\\\\\\"\\\\n  authors: [Nathan Godey, Éric de la Clergerie, Benoît Sagot]\\\\n  year: 2024\\\\n  venue: EACL 2024\\\\n  url: https://aclanthology.org/2024.eacl-long.3/\\\\n  role: theoretical-foundation\\\\n  relevance_note: >\\\\n    Proves anisotropy is inherent to the self-attention mechanism itself, not just a\\\\n    consequence of cross-entropy training on long-tailed token distributions.\\\\n    Observed across modalities (NLP, vision), ruling out data-distribution explanations.\\\\n    LINK TO OUR WORK: Strengthens the argument that BCS compression is a fundamental\\\\n    architectural limitation, not fixable by better prompting or model choice.\\\\n    Supports our position that structural decomposition (SDGD) is necessary precisely\\\\n    because the embedding space has inherent geometric constraints.\\\\n\\\\n- id: rajaee-cluster-isotropy-2021\\\\n  title: \\\\\\\"A Cluster-based Approach for Improving Isotropy in Contextual Embedding Space\\\\\\\"\\\\n  authors: [Sara Rajaee, Mohammad Taher Pilehvar]\\\\n  year: 2021\\\\n  venue: ACL 2021\\\\n  url: https://aclanthology.org/2021.acl-short.73/\\\\n  role: theoretical-foundation\\\\n  relevance_note: >\\\\n    Shows local (within-cluster) assessment of isotropy is more accurate than global assessment.\\\\n    Cluster-specific dominant directions encode structural (not semantic) information;\\\\n    removing them improves semantic task performance.\\\\n    LINK TO OUR WORK: Supports that within a semantic domain (one cluster), the dominant\\\\n    directions capture domain-level features rather than fine-grained type distinctions.\\\\n    This explains why MAVEN type embeddings are compressed: the shared \\\\\\\"event-ness\\\\\\\"\\\\n    dominates over type-specific semantics in the local embedding geometry.\\\\n\\\\n# =============================================================================\\\\n# NOVELTY THREAT ASSESSMENT (2026-05-15)\\\\n# =============================================================================\\\\n#\\\\n# 1. \\\\\\\"Type count vs type confusability\\\\\\\" disentangling:\\\\n#    ✅ NOVELTY SAFE — No prior work explicitly disentangles these two factors.\\\\n#    - IEPILE hard negatives: closest, but for training, not inference-time decomposition.\\\\n#    - Familiarity metric: measures label similarity for evaluation bias, not extraction.\\\\n#    - CROSSAGENTIE: resolves type confusion via debate, doesn't model as degradation channel.\\\\n#    Our multi-channel degradation model (count + confusability + context) is novel.\\\\n#\\\\n# 2. Schema decomposition baselines to compare:\\\\n#    - LLM-PEE (similarity partitioning) — MUST compare\\\\n#    - PARSE (LLM-driven schema rewriting) — MUST compare\\\\n#    - DEE (task-level decomposition) — discuss in related work\\\\n#    - SPT (schema as tools) — discuss in related work\\\\n#    - DLISC (Dual-LoRA schema caching) — discuss in related work\\\\n#\\\\n# 3. \\\\\\\"Lost in the Middle\\\\\\\" for IE:\\\\n#    ✅ OPPORTUNITY — No follow-up work applying it to IE task found.\\\\n#    We can be first to connect positional bias to schema prompt design.\\\\n#\\\\n# 4. Multi-agent approaches (CROSSAGENTIE, CMAS):\\\\n#    Growing area. Position clearly: we reduce confusion proactively via decomposition,\\\\n#    they resolve it reactively via debate. Complementary, not conflicting.\\\\n#\\\\n# 5. Overall novelty position:\\\\n#    STRONG — no prior work proposes (a) a formal multi-channel degradation model for\\\\n#    schema complexity in LLM IE, or (b) a DAG-based schema decomposition optimized\\\\n#    for type confusability. Main risk is CROSSAGENTIE's cross-type debate framing.\\\\n\\\", \\\"total_chars\\\": 18972, \\\"truncated\\\": false}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/literature_map.yaml\", \"content\": \"# Literature Map for schema-dag-extraction\\n# Updated: 2026-05-15\\n# Paper: Multi-channel Degradation Model + SDGD Framework for Training-free LLM IE\\n\\n# =============================================================================\\n# DIRECT COMPETITORS — schema decomposition for LLM-based IE\\n# =============================================================================\\n\\n- id: llm-pee-2025\\n  title: \\\"Towards Event Extraction with Massive Types: LLM-based Collaborative Annotation and Partitioning Extraction\\\"\\n  year: 2025\\n  venue: arXiv\\n  url: https://arxiv.org/abs/2503.02628\\n  role: direct-competitor\\n  relevance_note: >\\n    Similarity-based type recall + type-partitioning prompting for massive event types.\\n    Divides candidate types into partitions to reduce prompt length.\\n    +5.4% event detection, +6.1% argument extraction, +12.9% F1 over mainstream LLMs zero-shot.\\n    KEY DIFF: partitions by similarity-based recall, NOT confusability-aware.\\n    Our DAG decomposition is confusability-driven, not just similarity-driven.\\n\\n- id: parse-2025\\n  title: \\\"PARSE: LLM Driven Schema Optimization for Reliable Entity Extraction\\\"\\n  authors: [Anubhav Shrimal, Aryan Jain, Soumyajit Chowdhury, Promod Yenigalla]\\n  year: 2025\\n  venue: EMNLP 2025 Industry\\n  url: https://arxiv.org/abs/2510.08623\\n  role: direct-competitor\\n  relevance_note: >\\n    ARCHITECT autonomously rewrites JSON schemas for LLM consumption.\\n    SCOPE uses reflection-based extraction with guardrails. +64.7% on SWDE.\\n    Treats schema optimization as black-box LLM rewriting, not principled decomposition.\\n    Does NOT model type confusability explicitly.\\n\\n- id: dee-2024\\n  title: \\\"Decompose, Enrich, and Extract! Schema-aware Event Extraction using LLMs\\\"\\n  year: 2024\\n  venue: arXiv\\n  url: https://arxiv.org/abs/2406.01045\\n  role: direct-competitor\\n  relevance_note: >\\n    Decomposes event extraction into detection + argument extraction.\\n    Dynamic schema-aware RAG for augmented prompts.\\n    KEY DIFF: task-level decomposition (detection vs argument), not schema-level type decomposition.\\n\\n- id: crossagentie-2025\\n  title: \\\"CROSSAGENTIE: Cross-Type and Cross-Task Multi-Agent LLM Collaboration for Zero-Shot IE\\\"\\n  authors: [Meng Lu, Yuzhang Xie, Zhenyu Bi, Shuxiang Cao, Xuan Wang]\\n  year: 2025\\n  venue: ACL 2025 Findings\\n  url: https://aclanthology.org/2025.findings-acl.718/\\n  role: direct-competitor\\n  relevance_note: >\\n    Multi-agent: intra-group cross-type debate (resolves entity-label conflicts)\\n    + inter-group cross-task debate (NER↔RE mutual refinement).\\n    ⚠️ MODERATE NOVELTY CONCERN: cross-type debate explicitly addresses type confusion.\\n    KEY DIFF: reactive debate to resolve confusion post-hoc vs our proactive decomposition to prevent it.\\n    Must clearly differentiate in paper.\\n\\n- id: dlisc-2025\\n  title: \\\"Effective and Efficient Schema-aware Information Extraction Using On-Device LLMs\\\"\\n  year: 2025\\n  venue: arXiv (May 2025)\\n  url: https://arxiv.org/abs/2505.14992\\n  role: direct-competitor\\n  relevance_note: >\\n    Dual-LoRA with Incremental Schema Caching.\\n    Identification LoRA retrieves relevant schemas, Extraction LoRA performs IE.\\n    Focus on efficiency for on-device LLMs, not confusability analysis.\\n\\n- id: spt-2025\\n  title: \\\"Schema as Parameterized Tools for Universal Information Extraction\\\"\\n  year: 2025\\n  venue: arXiv (June 2025)\\n  url: https://arxiv.org/abs/2506.01276\\n  role: direct-competitor\\n  relevance_note: >\\n    Treats schemas as parameterized tools for LLM tool-calling.\\n    Schema retrieval + generation + infilling. Novel schema-LLM interface.\\n    Does not address type confusability.\\n\\n- id: zeroner-2025\\n  title: \\\"ZeroNER: Fueling Zero-Shot NER via Entity Type Descriptions\\\"\\n  year: 2025\\n  venue: ACL 2025 Findings\\n  url: https://aclanthology.org/2025.findings-acl.805/\\n  role: direct-competitor\\n  relevance_note: >\\n    Description-driven: LLM supervision → BERT student for unseen types.\\n    +16% F1 over LLMs on hard zero-shot. Leverages type descriptions.\\n    Related to how schema semantics affect extraction quality.\\n\\n- id: cmas-ner-2025\\n  title: \\\"A Cooperative Multi-Agent Framework for Zero-Shot Named Entity Recognition\\\"\\n  year: 2025\\n  venue: TheWebConf 2025\\n  url: https://dl.acm.org/doi/10.1145/3696410.3714923\\n  role: direct-competitor\\n  relevance_note: >\\n    Multi-agent collective intelligence for zero-shot NER.\\n    Addresses context correlation and indiscriminate demonstration problems.\\n    Outperforms on 6 benchmarks including domain-specific and general-domain.\\n\\n# =============================================================================\\n# METHOD COMPONENTS — techniques we build upon or relate to\\n# =============================================================================\\n\\n- id: uniner-2024\\n  title: \\\"UniversalNER: Targeted Distillation from Large Language Models for Open NER\\\"\\n  authors: [Wenxuan Zhou et al.]\\n  year: 2024\\n  venue: ICLR 2024\\n  url: https://arxiv.org/abs/2308.03279\\n  role: method-component\\n  relevance_note: >\\n    Instruction-tuning on ChatGPT-generated NER data. 43 datasets, 9 domains, 13K+ types.\\n    UniNER-7B outperforms ChatGPT by 7 F1 points.\\n    Important baseline for universal NER and schema-at-scale challenges.\\n\\n- id: gollie-2024\\n  title: \\\"GoLLIE: Annotation Guidelines Following Large Language Model for Information Extraction\\\"\\n  authors: [Oscar Sainz et al.]\\n  year: 2024\\n  venue: ICLR 2024\\n  url: https://hitz-zentroa.github.io/GoLLIE/\\n  role: method-component\\n  relevance_note: >\\n    Code-style schema definitions + annotation guideline following.\\n    Strong zero-shot on unseen IE tasks. Code-Llama based.\\n    Baseline for guideline-driven schema representation.\\n\\n- id: gliner-2024\\n  title: \\\"GLiNER: Generalist Model for Named Entity Recognition using Bidirectional Transformer\\\"\\n  authors: [Urchade Zaratiana et al.]\\n  year: 2024\\n  venue: NAACL 2024\\n  url: https://arxiv.org/abs/2311.08526\\n  role: method-component\\n  relevance_note: >\\n    Compact bidirectional encoder for zero-shot NER with parallel extraction.\\n    Outperforms InstructUIE and larger models. Non-LLM competitive baseline.\\n\\n- id: gliner2-2025\\n  title: \\\"GLiNER2: Efficient Multi-Task IE System with Schema-Driven Interface\\\"\\n  authors: [Urchade Zaratiana et al.]\\n  year: 2025\\n  venue: EMNLP 2025 Demo\\n  url: https://arxiv.org/abs/2507.18546\\n  role: method-component\\n  relevance_note: >\\n    Extends GLiNER to multi-task IE (NER+RE+classification). 205M params, CPU-efficient.\\n    Schema-driven interface. Shows schema approach scales to multi-task.\\n\\n- id: kggen-2025\\n  title: \\\"KGGen: Extracting Knowledge Graphs from Plain Text with Language Models\\\"\\n  authors: [Mo et al.]\\n  year: 2025\\n  venue: NeurIPS 2025\\n  url: https://arxiv.org/abs/2502.09956\\n  role: method-component\\n  relevance_note: >\\n    Two-stage decomposition: entities first, then relations.\\n    Entity clustering/deduplication to reduce graph sparsity.\\n    Schema decomposition approach for KG construction.\\n\\n- id: code4uie-2024\\n  title: \\\"Retrieval-Augmented Code Generation for Universal Information Extraction\\\"\\n  authors: [Yucan Guo et al.]\\n  year: 2024\\n  venue: NeurIPS 2024 Workshop\\n  url: https://arxiv.org/abs/2311.02962\\n  role: method-component\\n  relevance_note: >\\n    Python class-based schema definitions + RAG for code generation.\\n    Unified code-style schema for all IE tasks.\\n\\n- id: iepile-2024\\n  title: \\\"IEPile: Unearthing Large-Scale Schema-Based Information Extraction Corpus\\\"\\n  authors: [Guanzheng Chen et al., ZJU NLP]\\n  year: 2024\\n  venue: ACL 2024\\n  url: https://arxiv.org/abs/2402.14710\\n  role: method-component\\n  relevance_note: >\\n    0.32B token bilingual IE corpus. Hard negative schema construction =\\n    semantically proximate schemas to train type discrimination.\\n    ⚠️ RELATED: hard negatives ≈ confusable schemas, but for TRAINING, not inference-time.\\n    Our contribution is inference-time confusability-aware decomposition (training-free).\\n\\n- id: lost-in-middle-2024\\n  title: \\\"Lost in the Middle: How Language Models Use Long Contexts\\\"\\n  authors: [Nelson F. Liu et al.]\\n  year: 2024\\n  venue: TACL 2024\\n  url: https://arxiv.org/abs/2307.03172\\n  role: method-component\\n  relevance_note: >\\n    LLMs degrade when relevant info is in middle of long contexts (U-shaped attention).\\n    Motivates schema decomposition to reduce prompt length.\\n    No IE-specific follow-up found — opportunity for us to be first to connect this to IE.\\n\\n# =============================================================================\\n# ZERO-SHOT NER / RE BASELINES\\n# =============================================================================\\n\\n- id: self-improve-ner-2024\\n  title: \\\"Self-Improving for Zero-Shot Named Entity Recognition with Large Language Models\\\"\\n  year: 2024\\n  venue: NAACL 2024\\n  url: https://arxiv.org/abs/2311.08921\\n  role: background\\n  relevance_note: >\\n    Self-improving framework using LLM self-generated examples for zero-shot NER.\\n\\n- id: self-prompting-re-2024\\n  title: \\\"Unleashing the Power of LLMs in Zero-shot Relation Extraction via Self-Prompting\\\"\\n  year: 2024\\n  venue: EMNLP 2024 Findings\\n  url: https://arxiv.org/abs/2410.01154\\n  role: background\\n  relevance_note: >\\n    Three-stage self-prompting for zero-shot RE. Generates synthetic ICL samples.\\n    Training-free RE baseline.\\n\\n- id: reasoning-ner-2025\\n  title: \\\"A Reasoning Paradigm for Named Entity Recognition\\\"\\n  year: 2025\\n  venue: arXiv (Nov 2025)\\n  url: https://arxiv.org/abs/2511.11978\\n  role: background\\n  relevance_note: >\\n    CoT-based reasoning for NER. Outperforms GPT-4 by 12.3 F1 in zero-shot.\\n    Shifts NER from pattern matching to explicit reasoning. Strong zero-shot baseline.\\n\\n- id: nuner-2024\\n  title: \\\"NuNER: Entity Recognition Encoder Pre-training via LLM-Annotated Data\\\"\\n  authors: [Sergei Bogdanov et al., NuMind]\\n  year: 2024\\n  venue: EMNLP 2024\\n  url: https://arxiv.org/abs/2402.15343\\n  role: background\\n  relevance_note: >\\n    Contrastive pre-training on LLM-annotated data. Strong few-shot NER foundation model.\\n\\n# =============================================================================\\n# EVALUATION / BENCHMARKING\\n# =============================================================================\\n\\n- id: familiarity-2025\\n  title: \\\"Familiarity: Better Evaluation of Zero-Shot NER by Quantifying Label Shifts in Synthetic Training Data\\\"\\n  year: 2025\\n  venue: NAACL 2025\\n  url: https://arxiv.org/abs/2412.10121\\n  role: evaluation\\n  relevance_note: >\\n    \\\"Familiarity\\\" metric for label shift in synthetic NER data.\\n    Zero-shot NER scores overestimated due to train-eval label overlap.\\n    Quantifies semantic similarity between entity types — related to type confusability.\\n    KEY DIFF: measures evaluation bias, not extraction-time confusability.\\n\\n- id: guidex-2025\\n  title: \\\"GuideX: Guided Synthetic Data Generation for Zero-Shot Information Extraction\\\"\\n  authors: [Neil Deshpande et al.]\\n  year: 2025\\n  venue: ACL 2025 Findings\\n  url: https://arxiv.org/abs/2506.00649\\n  role: evaluation\\n  relevance_note: >\\n    Auto-generates domain-specific schemas + guidelines + synthetic labels.\\n    SOTA on 7 zero-shot NER benchmarks (+7 F1). Strong baseline.\\n\\n# =============================================================================\\n# SURVEYS\\n# =============================================================================\\n\\n- id: llm4ie-survey-2024\\n  title: \\\"Large Language Models for Generative Information Extraction: A Survey\\\"\\n  authors: [Derong Xu et al.]\\n  year: 2024\\n  venue: Frontiers of Computer Science\\n  url: https://arxiv.org/abs/2312.17617\\n  role: background\\n  relevance_note: >\\n    Comprehensive survey of LLM-based IE covering prompting, fine-tuning, benchmarks.\\n\\n- id: knowcoder-2024\\n  title: \\\"KnowCoder: Coding Structured Knowledge into LLMs for Universal IE\\\"\\n  year: 2024\\n  venue: ACL 2024\\n  url: https://arxiv.org/abs/2403.07969\\n  role: background\\n  relevance_note: >\\n    Encodes schema knowledge via code structures into LLM.\\n    Related to code-based schema representation.\\n\\n- id: slot-2025\\n  title: \\\"SLOT: Structuring the Output of Large Language Models\\\"\\n  year: 2025\\n  venue: EMNLP 2025 Industry\\n  url: https://aclanthology.org/2025.emnlp-industry.32.pdf\\n  role: background\\n  relevance_note: >\\n    Decouples output formatting from NL task. Model-agnostic structured output.\\n\\n# =============================================================================\\n# EMBEDDING ANISOTROPY / REPRESENTATION DEGENERATION\\n# — supports \\\"domain boundary\\\" finding: BCS proxy fails for same-domain schemas\\n# =============================================================================\\n\\n- id: gao-repr-degen-2019\\n  title: \\\"Representation Degeneration Problem in Training Natural Language Generation Models\\\"\\n  authors: [Jun Gao, Di He, Hang Li, Xin Jiang]\\n  year: 2019\\n  venue: ICLR 2019\\n  url: https://arxiv.org/abs/1907.12009\\n  role: theoretical-foundation\\n  relevance_note: >\\n    FOUNDATIONAL. Shows that likelihood maximization + weight tying causes word embeddings\\n    to degenerate into a narrow cone with uniformly high cosine similarity.\\n    Proposed cosine regularization (MLE-CosReg) to widen the cone aperture.\\n    LINK TO OUR WORK: This is the root mechanism behind BCS compression.\\n    When Qwen3-32B encodes 168 same-domain FrameNet types, the degeneration effect\\n    concentrates them into the same narrow cone (cosine ≥ 0.90), destroying BCS discriminability.\\n    Cite as the theoretical explanation for why embedding-based confusability proxies\\n    have a principled failure mode on semantically homogeneous schemas.\\n\\n- id: ethayarajh-contextual-2019\\n  title: \\\"How Contextual are Contextualized Word Representations? Comparing the Geometry of BERT, ELMo, and GPT-2 Embeddings\\\"\\n  authors: [Kawin Ethayarajh]\\n  year: 2019\\n  venue: EMNLP 2019\\n  url: https://aclanthology.org/D19-1006/\\n  role: theoretical-foundation\\n  relevance_note: >\\n    Shows contextualized representations are anisotropic in ALL layers of BERT/ELMo/GPT-2.\\n    Upper layers are more context-specific but still not isotropic.\\n    Introduces quantitative measures of anisotropy (avg cosine sim of random word pairs).\\n    LINK TO OUR WORK: Establishes that anisotropy is pervasive across architectures —\\n    our MAVEN embedding compression is not a Qwen-specific artifact but a general property.\\n    Supports the argument that ANY embedding-based confusability proxy inherits this limitation.\\n\\n- id: cai-isotropy-clusters-2021\\n  title: \\\"Isotropy in the Contextual Embedding Space: Clusters and Manifolds\\\"\\n  authors: [Xingyu Cai, Jiaji Huang, Yuchen Bian, Kenneth Church]\\n  year: 2021\\n  venue: ICLR 2021\\n  url: https://openreview.net/forum?id=xYGNO86OWDH\\n  role: theoretical-foundation\\n  relevance_note: >\\n    ⭐ MOST DIRECTLY RELEVANT. Key insight: global anisotropy is caused by isolated clusters;\\n    WITHIN each cluster, embeddings are locally more isotropic.\\n    Resolution: the high average cosine similarity reported in prior work is an artifact of\\n    mixing embeddings from different clusters — within-cluster geometry is better behaved.\\n    LINK TO OUR WORK: This is the exact mechanism for our \\\"domain boundary\\\" finding.\\n    Cross-domain schemas (ACE vs FewNERD) span DIFFERENT clusters → BCS captures real\\n    inter-cluster distances → proxy works. Same-domain schemas (MAVEN FrameNet types)\\n    fall within ONE cluster → within-cluster variance is low → cosine sim saturates ≥ 0.90\\n    → BCS loses discriminability. Our empirical finding is a direct instantiation of their\\n    theoretical framework applied to type-level (not token-level) embeddings.\\n\\n- id: godey-anisotropy-inherent-2024\\n  title: \\\"Anisotropy Is Inherent to Self-Attention in Transformers\\\"\\n  authors: [Nathan Godey, Éric de la Clergerie, Benoît Sagot]\\n  year: 2024\\n  venue: EACL 2024\\n  url: https://aclanthology.org/2024.eacl-long.3/\\n  role: theoretical-foundation\\n  relevance_note: >\\n    Proves anisotropy is inherent to the self-attention mechanism itself, not just a\\n    consequence of cross-entropy training on long-tailed token distributions.\\n    Observed across modalities (NLP, vision), ruling out data-distribution explanations.\\n    LINK TO OUR WORK: Strengthens the argument that BCS compression is a fundamental\\n    architectural limitation, not fixable by better prompting or model choice.\\n    Supports our position that structural decomposition (SDGD) is necessary precisely\\n    because the embedding space has inherent geometric constraints.\\n\\n- id: rajaee-cluster-isotropy-2021\\n  title: \\\"A Cluster-based Approach for Improving Isotropy in Contextual Embedding Space\\\"\\n  authors: [Sara Rajaee, Mohammad Taher Pilehvar]\\n  year: 2021\\n  venue: ACL 2021\\n  url: https://aclanthology.org/2021.acl-short.73/\\n  role: theoretical-foundation\\n  relevance_note: >\\n    Shows local (within-cluster) assessment of isotropy is more accurate than global assessment.\\n    Cluster-specific dominant directions encode structural (not semantic) information;\\n    removing them improves semantic task performance.\\n    LINK TO OUR WORK: Supports that within a semantic domain (one cluster), the dominant\\n    directions capture domain-level features rather than fine-grained type distinctions.\\n    This explains why MAVEN type embeddings are compressed: the shared \\\"event-ness\\\"\\n    dominates over type-specific semantics in the local embedding geometry.\\n\\n# =============================================================================\\n# NOVELTY THREAT ASSESSMENT (2026-05-15)\\n# =============================================================================\\n#\\n# 1. \\\"Type count vs type confusability\\\" disentangling:\\n#    ✅ NOVELTY SAFE — No prior work explicitly disentangles these two factors.\\n#    - IEPILE hard negatives: closest, but for training, not inference-time decomposition.\\n#    - Familiarity metric: measures label similarity for evaluation bias, not extraction.\\n#    - CROSSAGENTIE: resolves type confusion via debate, doesn't model as degradation channel.\\n#    Our multi-channel degradation model (count + confusability + context) is novel.\\n#\\n# 2. Schema decomposition baselines to compare:\\n#    - LLM-PEE (similarity partitioning) — MUST compare\\n#    - PARSE (LLM-driven schema rewriting) — MUST compare\\n#    - DEE (task-level decomposition) — discuss in related work\\n#    - SPT (schema as tools) — discuss in related work\\n#    - DLISC (Dual-LoRA schema caching) — discuss in related work\\n#\\n# 3. \\\"Lost in the Middle\\\" for IE:\\n#    ✅ OPPORTUNITY — No follow-up work applying it to IE task found.\\n#    We can be first to connect positional bias to schema prompt design.\\n#\\n# 4. Multi-agent approaches (CROSSAGENTIE, CMAS):\\n#    Growing area. Position clearly: we reduce confusion proactively via decomposition,\\n#    they resolve it reactively via debate. Complementary, not conflicting.\\n#\\n# 5. Overall novelty position:\\n#    STRONG — no prior work proposes (a) a formal multi-channel degradation model for\\n#    schema complexity in LLM IE, or (b) a DAG-based schema decomposition optimized\\n#    for type confusability. Main risk is CROSSAGENTIE's cross-type debate framing.\\n\", \"total_chars\": 18972, \"truncated\": false}, \"error\": null, \"metadata\": {}}"
    }
  },
  "sourceToolAssistantUUID": "0faafce6-d72c-4006-8b19-190c8ae024bd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/reviewer_efaaa6bc",
  "sessionId": "f59020b4-1c0e-4081-9cb3-293eac3560ff",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-15T17:16:28.271Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01Si5iU6tg2pJdsg6sjX5gpo`</summary>

```json
{
  "server": "cqa1-38874",
  "command": "ls -la /root/schema-dag-extraction/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "62e27dc6-9294-443c-86f9-3e87f83f551b",
  "isSidechain": false,
  "requestId": "req_011Cb4jSczYHdFnwNmZkngqK",
  "type": "assistant",
  "uuid": "1c225a3a-c912-4770-9d4e-da4c34eee5c9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/reviewer_efaaa6bc",
  "sessionId": "f59020b4-1c0e-4081-9cb3-293eac3560ff",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HCW11dZXE2VF7r3o7gjr2X",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 8597,
      "cache_read_input_tokens": 46543,
      "output_tokens": 1500,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 8597,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1500,
          "cache_read_input_tokens": 46543,
          "cache_creation_input_tokens": 8597,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 8597
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

_source line 42_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[系统通知 — worker_done:worker_paper_research_bib_sync_20260515T171027]: Worker worker_paper_research_bib_sync_20260515T171027 已完成（status=done），请审查 Agent 的处理结果。",
  "leafUuid": "1c225a3a-c912-4770-9d4e-da4c34eee5c9",
  "sessionId": "f59020b4-1c0e-4081-9cb3-293eac3560ff"
}
```

---

### Runtime record

_source line 43_

```json
{
  "type": "ai-title",
  "aiTitle": "Review paper research bibliography sync results",
  "sessionId": "f59020b4-1c0e-4081-9cb3-293eac3560ff"
}
```

---

### Tool result

_source line 44 · 2026-05-15T17:16:29.500Z_

<details><summary>↩ Tool result · `toolu_01Si5iU6tg2pJdsg6sjX5gpo`</summary>

```text
{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"ls: cannot access '/root/schema-dag-extraction/docs/paper/references.bib': No such file or directory\\n\", \"return_code\": 2}, \"error\": \"exit code 2\", \"metadata\": {\"elapsed_seconds\": 1.22}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1c225a3a-c912-4770-9d4e-da4c34eee5c9",
  "isSidechain": false,
  "promptId": "b593ab42-40aa-4651-8f99-a82b6d6b969a",
  "type": "user",
  "uuid": "d25702ef-edf1-45e4-99eb-9738e21a9991",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {\\\"stdout\\\": \\\"\\\", \\\"stderr\\\": \\\"ls: cannot access '/root/schema-dag-extraction/docs/paper/references.bib': No such file or directory\\\\n\\\", \\\"return_code\\\": 2}, \\\"error\\\": \\\"exit code 2\\\", \\\"metadata\\\": {\\\"elapsed_seconds\\\": 1.22}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"ls: cannot access '/root/schema-dag-extraction/docs/paper/references.bib': No such file or directory\\n\", \"return_code\": 2}, \"error\": \"exit code 2\", \"metadata\": {\"elapsed_seconds\": 1.22}}"
    }
  },
  "sourceToolAssistantUUID": "1c225a3a-c912-4770-9d4e-da4c34eee5c9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/reviewer_efaaa6bc",
  "sessionId": "f59020b4-1c0e-4081-9cb3-293eac3560ff",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 45 · 2026-05-15T17:17:20.923Z_

<details><summary>Logged reasoning block</summary>

```text
Remote server doesn't have the bib file - it's only in the local workspace. That's expected since paper files live locally.

Now let me do the detailed audit. I need to cross-check:

1. literature_map.yaml entries vs references.bib entries
2. Venue consistency
3. Author completeness
4. URL validity patterns
5. Any entries in bib not in literature_map (and vice versa)

Let me enumerate:

**literature_map.yaml entries** (by id):
- DIRECT COMPETITORS: llm-pee-2025, parse-2025, dee-2024, crossagentie-2025, dlisc-2025, spt-2025, zeroner-2025, cmas-ner-2025


- METHOD COMPONENTS: uniner-2024, gollie-2024, gliner-2024, gliner2-2025, kggen-2025, code4uie-2024, iepile-2024, lost-in-middle-2024
- ZERO-SHOT BASELINES: self-improve-ner-2024, self-prompting-re-2024, reasoning-ner-2025, nuner-2024
- EVALUATION: familiarity-2025, guidex-2025
- SURVEYS: llm4ie-survey-2024, knowcoder-2024, slot-2025
- EMBEDDING ANISOTROPY: gao-repr-degen-2019, ethayarajh

, contextual-2019, cai-isotropy-clusters-2021, godey-anisotropy-inherent-2024, rajaee-cluster-isotropy-2021

I'm tallying up the literature map entries across all categories and now compiling the references.bib file with direct competitors like llm-pee-2025, parse-2025, dee-2024, and others alongside the method components and baselines I've already organized. I'm tallying up the bibliography entries across all sections—that comes to 43 total, with 13 of those in the additional references pulled from a separate survey document. Now I'm checking for inconsistencies between the literature map and the bibliography itself. I notice llm-pee-2025 has conflicting venue information: the literature map lists it as an arXiv preprint, but the bibliography shows it as a published EMNLP 2025 paper with a different URL.

For parse-2025, there's another mismatch—the literature map claims it's EMNLP 2025 Industry, yet the bibliography treats it as an arXiv article rather than a conference proceeding, which suggests one of these sources is outdated. Moving on to dee-2024...

The literature map lists it as arXiv, but the bibliography references it as published in the IEEE ICTAI proceedings—another case where the bibliography got updated but the literature map didn't catch up. With gollie-2024, there's a minor divergence where the bibliography points to arXiv while the literature map uses the project page instead, which is less standard for citations. I'm also noticing the iepile-2024 entry is cut off, but I can see it's starting to list author information.

Looking at the iepile-2024 entry more carefully, the literature map claims the first author is Guanzheng Chen, but checking the actual arXiv page for 2402.14710 shows the first author is Honghao Gui, with Huajun Chen as the last author. So the bibliography has the correct author order, but the literature map has this backwards—it's a factual error in the literature map that needs fixing.

Moving on to the next entry, the literature map lists Neil Deshpande as the first author, but the bibliography shows the first author is actually De La Fuente. This is another author name mismatch in the literature map that contradicts what's in the bibliography.

I'm also noticing some potential issues with how certain entries are formatted in the bibliography. The parse-2025 entry uses @article, but if it's actually accepted at EMNLP 2025 Industry as the literature map indicates, it should probably be @inproceedings with a booktitle instead. And for dee-2024, I need to verify whether "IEEE International Conference on Tools with Artificial Intelligence" is the correct venue name.

Looking at the author lists, dlisc-2025 has authors in the bibliography but none listed in the literature map, while spt-2025 shares some overlapping authors with dlisc-2025, which makes sense if they're from the same research group. But I'm also seeing that there are 13 additional references in the bibliography that don't appear in the literature map at all, which is a significant gap.

Now checking the citation integrity — reasoning-ner-2025 uses an arXiv ID from November 2025, which is valid since we're in May 2026, though it might need updating if it's been formally published by now. For gliner2-2025, the arXiv ID is from July 2025 but the bibliography claims it was published at EMNLP 2025, so I need to verify whether that conference actually happened and if the citation format is correct.

Looking at the summary of findings, there are several venue inconsistencies I've identified: llm-pee-2025 shows arXiv in the literature map but EMNLP 2025 main conference in the bibliography, dee-2024 has the same issue with arXiv versus IEEE ICTAI, and parse-2025 has conflicting information about whether it's an EMNLP 2025 Industry paper or an arXiv article. I also noticed an author name discrepancy in iepile-2024 where the literature map lists "Guanzheng Chen" but the correct first author should be "Honghao Gui."
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d25702ef-edf1-45e4-99eb-9738e21a9991",
  "isSidechain": false,
  "requestId": "req_011Cb4jV7U7WM8hZ2JjbD1GV",
  "type": "assistant",
  "uuid": "16da738c-c87c-4bbf-b727-834b4f61a509",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/reviewer_efaaa6bc",
  "sessionId": "f59020b4-1c0e-4081-9cb3-293eac3560ff",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015fuHWmPjDQBMZpw5PTcbd8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8044,
      "cache_read_input_tokens": 55140,
      "output_tokens": 3782,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 8044,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3782,
          "cache_read_input_tokens": 55140,
          "cache_creation_input_tokens": 8044,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 8044
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

_source line 46 · 2026-05-15T17:17:21.766Z_

完成交叉比对。发现多处 literature_map ↔ bib 不一致。汇报给 Director。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "16da738c-c87c-4bbf-b727-834b4f61a509",
  "isSidechain": false,
  "requestId": "req_011Cb4jV7U7WM8hZ2JjbD1GV",
  "type": "assistant",
  "uuid": "73a8f945-baf0-4c3f-9363-3044267dd26d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/reviewer_efaaa6bc",
  "sessionId": "f59020b4-1c0e-4081-9cb3-293eac3560ff",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015fuHWmPjDQBMZpw5PTcbd8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8044,
      "cache_read_input_tokens": 55140,
      "output_tokens": 3782,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 8044,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3782,
          "cache_read_input_tokens": 55140,
          "cache_creation_input_tokens": 8044,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 8044
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

_source line 47 · 2026-05-15T17:17:40.942Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__reviewer_post_to_director · `toolu_015EBTxaBNmkBxWdupfdt5td`</summary>

```json
{
  "text": "## 审查报告 — worker_paper_research_bib_sync_20260515T171027\n\n**结论**: WARNING\n\nWorker 完成了 references.bib 与 literature_map.yaml 的同步，bib 文件共 43 条目（literature_map 30 条 + references_survey.md 13 条），结构完整。但交叉校验发现以下问题：\n\n### 发现\n\n- [severity: warning] **venue 不一致 — llm-pee-2025**: bib 已升级为 EMNLP 2025 main（`booktitle = Proceedings of the 2025 Conference on EMNLP`, url 改为 aclanthology），但 literature_map.yaml 仍标注 `venue: arXiv`、url 仍为 arxiv。literature_map 是 novelty 评估和 related work 写作的源文件，venue 滞后可能导致对竞品重要性的低估。\n\n- [severity: warning] **venue 不一致 — dee-2024**: bib 已升级为 IEEE ICTAI（`booktitle = IEEE International Conference on Tools with AI`），但 literature_map 仍标注 `venue: arXiv`。同上。\n\n- [severity: warning] **venue 矛盾 — parse-2025**: literature_map 标注 `venue: EMNLP 2025 Industry`，但 bib 使用 `@article{...journal = arXiv preprint}`。两边对不上：如果已被 EMNLP Industry 接收，bib 应改为 `@inproceedings`；如果仍是 arXiv，literature_map 的 venue 标注有误。需核实哪边正确。\n\n- [severity: warning] **作者名错误 — iepile-2024**: literature_map 标注首作者为 \"Guanzheng Chen et al., ZJU NLP\"，但 bib 和 arxiv 页面首作者为 Honghao Gui（末位作者是 Huajun Chen，非 Guanzheng）。Literature_map 的作者信息不可信。\n\n- [severity: warning] **作者名错误 — guidex-2025**: literature_map 标注 \"Neil Deshpande et al.\"，bib 首作者为 \"De La Fuente, Neil\"。姓氏完全不同。\n\n- [severity: info] **bib 额外条目来源明确**: 13 条\"ADDITIONAL REFERENCES\"来自 references_survey.md，未在 literature_map 中注册，bib header 已标注来源。不影响论文引用追溯。\n\n- [severity: info] **gollie-2024 URL 差异**: literature_map 指向项目主页(hitz-zentroa.github.io)，bib 指向 arxiv(2310.03668)。两者都有效，非错误。\n\n### 建议\n\n1. **literature_map 需同步更新 venue**：llm-pee-2025 → EMNLP 2025 Main，dee-2024 → IEEE ICTAI 2024。这两篇已从 preprint 升级为正式发表，需要在 Related Work 中准确标注 venue。\n2. **核实 parse-2025 真实 venue**：查 EMNLP 2025 Industry accepted papers list 或 aclanthology，确认后统一 bib 和 literature_map。\n3. **修正两个首作者名**：iepile-2024 (Gui, Honghao)、guidex-2025 (De La Fuente, Neil)。\n4. 如距 ARR May 25 只剩 10 天，建议优先修正 bib 中的 venue 格式（parse-2025 的 @article vs @inproceedings），因为这直接影响提交稿的引用格式。",
  "project": "schema-dag-extraction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "73a8f945-baf0-4c3f-9363-3044267dd26d",
  "isSidechain": false,
  "requestId": "req_011Cb4jV7U7WM8hZ2JjbD1GV",
  "type": "assistant",
  "uuid": "391b1cb6-482e-4f9b-9155-82ee1ad247bf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/reviewer_efaaa6bc",
  "sessionId": "f59020b4-1c0e-4081-9cb3-293eac3560ff",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015fuHWmPjDQBMZpw5PTcbd8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8044,
      "cache_read_input_tokens": 55140,
      "output_tokens": 3782,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 8044,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3782,
          "cache_read_input_tokens": 55140,
          "cache_creation_input_tokens": 8044,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 8044
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

_source line 48 · 2026-05-15T17:17:44.855Z_

<details><summary>↩ Tool result · `toolu_015EBTxaBNmkBxWdupfdt5td`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"director_session\": \"feishu:group:oc_51326259fe46fbae9da26b81cf03f1f8:director\"}, \"error\": \"\"}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "391b1cb6-482e-4f9b-9155-82ee1ad247bf",
  "isSidechain": false,
  "promptId": "b593ab42-40aa-4651-8f99-a82b6d6b969a",
  "type": "user",
  "uuid": "c6d204bd-b746-44cc-b8ad-f89240b7da17",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"director_session\\\": \\\"feishu:group:oc_51326259fe46fbae9da26b81cf03f1f8:director\\\"}, \\\"error\\\": \\\"\\\"}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"director_session\": \"feishu:group:oc_51326259fe46fbae9da26b81cf03f1f8:director\"}, \"error\": \"\"}"
    }
  },
  "sourceToolAssistantUUID": "391b1cb6-482e-4f9b-9155-82ee1ad247bf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/reviewer_efaaa6bc",
  "sessionId": "f59020b4-1c0e-4081-9cb3-293eac3560ff",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---
