# Research conversation: [系统通知 — worker_done:worker_audit_appendix_tables_20260525T201208]: Worker worker_audit_appendix_tables_20260525T201208 已 — Part 1 of 3

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue (July export snapshot)** · Conversation logs

[Transcript overview](../research-conversation-worker-done-worker-audit-appendix-tables-20260525t201208-worker-worker-audit-a.md) · [Part 2 →](part-002.md) · [Structured JSON](../../../sessions/9d/9de588854047538f7cb3.json)

## Before a recorded user message

## Before a recorded user message

2 recorded events


### Runtime record

_source line 1 · 2026-05-25T20:33:44.992Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-25T20:33:44.992Z",
  "sessionId": "5d779602-0719-4d06-8bf9-fdd84990d5d0",
  "content": "[系统通知 — worker_done:worker_audit_appendix_tables_20260525T201208]:\nWorker worker_audit_appendix_tables_20260525T201208 已完成（status=done），请审查 Agent 的处理结果。"
}
```

---


### Runtime record

_source line 2 · 2026-05-25T20:33:45.003Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-25T20:33:45.003Z",
  "sessionId": "5d779602-0719-4d06-8bf9-fdd84990d5d0"
}
```

---


## Round 1

## Round 1

93 recorded events


### User

_source line 3 · 2026-05-25T20:33:45.114Z_

[系统通知 — worker_done:worker_audit_appendix_tables_20260525T201208]:
Worker worker_audit_appendix_tables_20260525T201208 已完成（status=done），请审查 Agent 的处理结果。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "b0f005fa-c14f-47e1-bf29-f3925462c4b7",
  "type": "user",
  "uuid": "f5e04195-da89-466e-b5af-ba0ecbb264e9",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921",
  "sessionId": "5d779602-0719-4d06-8bf9-fdd84990d5d0",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---


### Runtime record

_source line 4 · 2026-05-25T20:33:45.113Z_

```json
{
  "parentUuid": "f5e04195-da89-466e-b5af-ba0ecbb264e9",
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
      "mcp__agent-ml-research__check_figures_and_layout",
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
      "mcp__agent-ml-research__check_figures_and_layout",
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
  "uuid": "51946364-dffa-4374-9fd0-9ccc50efb3a2",
  "timestamp": "2026-05-25T20:33:45.113Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921",
  "sessionId": "5d779602-0719-4d06-8bf9-fdd84990d5d0",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---


### Runtime record

_source line 5 · 2026-05-25T20:33:45.113Z_

```json
{
  "parentUuid": "51946364-dffa-4374-9fd0-9ccc50efb3a2",
  "isSidechain": false,
  "attachment": {
    "type": "agent_listing_delta",
    "addedTypes": [
      "claude",
      "Explore",
      "general-purpose",
      "Plan",
      "statusline-setup"
    ],
    "addedLines": [
      "- claude: Catch-all for any task that doesn't fit a more specific agent. FleetView's default when no agent name is typed. (Tools: *)",
      "- Explore: Fast read-only search agent for locating code. Use it to find files by pattern (eg. \"src/components/**/*.tsx\"), grep for symbols or keywords (eg. \"API endpoints\"), or answer \"where is X defined / which files reference Y.\" Do NOT use it for code review, design-doc auditing, cross-file consistency checks, or open-ended analysis — it reads excerpts rather than whole files and will miss content past its read window. When calling, specify search breadth: \"quick\" for a single targeted lookup, \"medium\" for moderate exploration, or \"very thorough\" to search across multiple locations and naming conventions. (Tools: All tools except Agent, ExitPlanMode, Edit, Write, NotebookEdit)",
      "- general-purpose: General-purpose agent for researching complex questions, searching for code, and executing multi-step tasks. When you are searching for a keyword or file and are not confident that you will find the right match in the first few tries use this agent to perform the search for you. (Tools: *)",
      "- Plan: Software architect agent for designing implementation plans. Use this when you need to plan the implementation strategy for a task. Returns step-by-step plans, identifies critical files, and considers architectural trade-offs. (Tools: All tools except Agent, ExitPlanMode, Edit, Write, NotebookEdit)",
      "- statusline-setup: Use this agent to configure the user's Claude Code status line setting. (Tools: Read, Edit)"
    ],
    "removedTypes": [],
    "isInitial": true,
    "showConcurrencyNote": true
  },
  "type": "attachment",
  "uuid": "f624d73c-6569-44a2-add2-ad9fbe220998",
  "timestamp": "2026-05-25T20:33:45.113Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921",
  "sessionId": "5d779602-0719-4d06-8bf9-fdd84990d5d0",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---


### Runtime record

_source line 6 · 2026-05-25T20:33:45.113Z_

```json
{
  "parentUuid": "f624d73c-6569-44a2-add2-ad9fbe220998",
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
  "uuid": "fcfa3569-75ab-4ca4-afde-ec1ba57c3bc2",
  "timestamp": "2026-05-25T20:33:45.113Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921",
  "sessionId": "5d779602-0719-4d06-8bf9-fdd84990d5d0",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---


### Runtime record

_source line 7 · 2026-05-25T20:33:45.113Z_

```json
{
  "parentUuid": "fcfa3569-75ab-4ca4-afde-ec1ba57c3bc2",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "e1fc4ce6-20b0-4cf0-af72-cf60bad3a994",
  "timestamp": "2026-05-25T20:33:45.113Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921",
  "sessionId": "5d779602-0719-4d06-8bf9-fdd84990d5d0",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---


### Runtime record

_source line 8_

```json
{
  "type": "ai-title",
  "aiTitle": "Review worker audit appendix tables completion",
  "sessionId": "5d779602-0719-4d06-8bf9-fdd84990d5d0"
}
```

---


### Assistant

_source line 9 · 2026-05-25T20:33:48.771Z_

<details><summary>Logged reasoning block</summary>

```text
Worker completed a task related to auditing appendix tables. I need to review the agent's work. Let me first check the registry and recent activity to understand what was done.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e1fc4ce6-20b0-4cf0-af72-cf60bad3a994",
  "isSidechain": false,
  "requestId": "req_011CbPvcixqyjaHxC5QVK6EP",
  "type": "assistant",
  "uuid": "14a8e72c-4f99-4705-88b8-5a84f85d69ef",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921",
  "sessionId": "5d779602-0719-4d06-8bf9-fdd84990d5d0",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MvjXeS22NhNziz7abemE3x",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 23337,
      "cache_read_input_tokens": 11447,
      "output_tokens": 168,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 23337,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 168,
          "cache_read_input_tokens": 11447,
          "cache_creation_input_tokens": 23337,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 23337
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

_source line 10 · 2026-05-25T20:33:49.220Z_

让我查看这个 worker 的处理结果。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "14a8e72c-4f99-4705-88b8-5a84f85d69ef",
  "isSidechain": false,
  "requestId": "req_011CbPvcixqyjaHxC5QVK6EP",
  "type": "assistant",
  "uuid": "39d2619d-4dd9-4638-89f5-11741f405b5f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921",
  "sessionId": "5d779602-0719-4d06-8bf9-fdd84990d5d0",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MvjXeS22NhNziz7abemE3x",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 23337,
      "cache_read_input_tokens": 11447,
      "output_tokens": 168,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 23337,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 168,
          "cache_read_input_tokens": 11447,
          "cache_creation_input_tokens": 23337,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 23337
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

_source line 11 · 2026-05-25T20:33:50.327Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_019sxZvnMa3tjS7t1nSFWmEt`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__read_project_file",
  "max_results": 2
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "39d2619d-4dd9-4638-89f5-11741f405b5f",
  "isSidechain": false,
  "requestId": "req_011CbPvcixqyjaHxC5QVK6EP",
  "type": "assistant",
  "uuid": "720f4e32-64de-481f-ae97-f3e67570335e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921",
  "sessionId": "5d779602-0719-4d06-8bf9-fdd84990d5d0",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MvjXeS22NhNziz7abemE3x",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 23337,
      "cache_read_input_tokens": 11447,
      "output_tokens": 168,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 23337,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 168,
          "cache_read_input_tokens": 11447,
          "cache_creation_input_tokens": 23337,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 23337
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

_source line 12 · 2026-05-25T20:33:50.334Z_

<details><summary>↩ Tool result · `toolu_019sxZvnMa3tjS7t1nSFWmEt`</summary>

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
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "720f4e32-64de-481f-ae97-f3e67570335e",
  "isSidechain": false,
  "promptId": "b0f005fa-c14f-47e1-bf29-f3925462c4b7",
  "type": "user",
  "uuid": "ef4070a3-8b63-42ca-a90f-95a3431f4496",
  "toolUseResult": {
    "matches": [
      "mcp__agent-ml-research__read_registry",
      "mcp__agent-ml-research__read_project_file"
    ],
    "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__read_project_file",
    "total_deferred_tools": 35
  },
  "sourceToolAssistantUUID": "720f4e32-64de-481f-ae97-f3e67570335e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921",
  "sessionId": "5d779602-0719-4d06-8bf9-fdd84990d5d0",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---


### Tool call

_source line 13 · 2026-05-25T20:33:53.904Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01AweRTaYJQGLHbbXcHJqs4w`</summary>

```json
{
  "project": "turn_residual_gating",
  "limit": 5,
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
  "parentUuid": "ef4070a3-8b63-42ca-a90f-95a3431f4496",
  "isSidechain": false,
  "requestId": "req_011CbPvd8SyS9K8EjaBFxCU2",
  "type": "assistant",
  "uuid": "f74530e3-8c31-4b86-94de-9a0952d5ae6f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921",
  "sessionId": "5d779602-0719-4d06-8bf9-fdd84990d5d0",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DfZbxSUi59jtZfu7hP245V",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 849,
      "cache_read_input_tokens": 34784,
      "output_tokens": 197,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 849,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 197,
          "cache_read_input_tokens": 34784,
          "cache_creation_input_tokens": 849,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 849
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

_source line 14 · 2026-05-25T20:33:54.075Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01LFKp7XAAr12b1Tj3mS1AzX`</summary>

```json
{
  "project": "turn_residual_gating",
  "file": "report.md",
  "max_chars": 12000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f74530e3-8c31-4b86-94de-9a0952d5ae6f",
  "isSidechain": false,
  "requestId": "req_011CbPvd8SyS9K8EjaBFxCU2",
  "type": "assistant",
  "uuid": "5b60a191-9115-43d2-99a4-b300a61cbcb2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921",
  "sessionId": "5d779602-0719-4d06-8bf9-fdd84990d5d0",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DfZbxSUi59jtZfu7hP245V",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 849,
      "cache_read_input_tokens": 34784,
      "output_tokens": 197,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 849,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 197,
          "cache_read_input_tokens": 34784,
          "cache_creation_input_tokens": 849,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 849
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

_source line 15 · 2026-05-25T20:33:54.118Z_

<details><summary>↩ Tool result · `toolu_01AweRTaYJQGLHbbXcHJqs4w`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {\"phase1a_multiseed_qwen\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-25T06:15:26.051Z\", \"updated_at\": \"2026-05-25T11:20:34.089Z\", \"hypothesis\": \"Multi-seed (s123, s456) training across 5 Qwen conditions (PCGrad, UG, LoRA-only, TG, SS) to establish mean±std for all claims. 8 training runs + AR eval N≥50 each. Expect TF convergence (GAR~0.50) and consistent AR rankings across seeds.\", \"spec\": {\"command\": \"python src/train_phase2_v9_pcgrad.py\", \"server\": \"westd-20861\", \"data_path\": \"data/ultrachat_8k\", \"data_count\": 8000, \"model_name\": \"Qwen2.5-7B-Instruct\", \"seed\": 123, \"checkpoint_path\": \"N/A\", \"log_path\": \"runs/d048_pcgrad_s123\"}, \"conclusion\": \"killed\", \"notes\": \"用户要求停止：30min 内无法完成。PCGrad s123 在 1800/3000 步时被终止，后续 7 个排队任务全部取消。\", \"checkpoint_path\": \"N/A\", \"log_path\": \"runs/d048_pcgrad_s123\", \"completed_at\": \"2026-05-25T11:20:34.089Z\"}, \"p1_ss_lora_only\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-25T08:58:41.419Z\", \"updated_at\": \"2026-05-25T09:42:22.185Z\", \"hypothesis\": \"SS training on LoRA-only checkpoint (no ThreadGate) with same hyperparameters (rho_max=0.3, same schedule) should achieve similar GAR improvement as SS+TG. If confirmed, this proves the SS fix is architecture-agnostic, strengthening the paper's mitigation story (the gap is caused by exposure bias in any auxiliary-loss setup, and SS fixes it regardless of gating mechanism).\", \"spec\": {\"command\": \"bash /root/turn_residual_gating/scripts/d048_ss_lo_s42.sh\", \"server\": \"westd-20861\", \"data_path\": \"/root/turn-residual-gating/data/phase2_train.jsonl\", \"data_count\": 2000, \"model_name\": \"Qwen/Qwen2.5-7B-Instruct\", \"seed\": 42, \"notes\": \"SS+LoRA-only (gate_type=none, ss_max_ratio=0.3). From-scratch training, not resume. Auto TF+AR eval after training. ~6.5h training + eval.\"}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-25T09:42:22.185Z\"}, \"phase2_switching\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-25T08:58:40.187Z\", \"updated_at\": \"2026-05-25T09:42:21.391Z\", \"hypothesis\": \"TF→AR switching at turn k (k=1..5) on ThreadGate s42 checkpoint. If GAR drops abruptly at the switch point (matching pure-AR level within 1 turn), it confirms exposure bias as instantaneous distribution shift rather than gradual KV cache drift. Staircase = exposure bias dominant; linear slope = KV drift dominant.\", \"conclusion\": \"killed\", \"completed_at\": \"2026-05-25T09:42:21.391Z\"}, \"phase2_tf_ar_switching\": {\"status\": \"QUEUED\", \"retry_count\": 0, \"created_at\": \"2026-05-25T06:15:36.221Z\", \"updated_at\": \"2026-05-25T06:45:27.338Z\", \"hypothesis\": \"TF→AR switching at turn k (k=1..5) on ThreadGate s42 checkpoint. If GAR drops abruptly at the switch point (matching pure-AR level within 1 turn), it confirms exposure bias as instantaneous distribution shift rather than gradual cumulative drift.\"}, \"phase1a_multiseed_8runs\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T06:18:08.953Z\", \"updated_at\": \"2026-05-25T06:18:08.953Z\", \"spec\": {\"command\": \"bash -c \\\"bash /root/turn_residual_gating/scripts/phase1a_multiseed_runner.sh\\\"\", \"server\": \"westd-20861\", \"gpu\": [\"cuda:0\"], \"pid\": \"5508\", \"log_path\": \"~/runs/turn_residual_gating/phase1a_multiseed_8runs.log\", \"submitted_at\": \"2026-05-25T06:18:08.495Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}}, \"count\": 5, \"total\": 60, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.2015}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f74530e3-8c31-4b86-94de-9a0952d5ae6f",
  "isSidechain": false,
  "promptId": "b0f005fa-c14f-47e1-bf29-f3925462c4b7",
  "type": "user",
  "uuid": "63d8c1cc-dd83-4352-80c9-2cfc9364e628",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {\\\"phase1a_multiseed_qwen\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-25T06:15:26.051Z\\\", \\\"updated_at\\\": \\\"2026-05-25T11:20:34.089Z\\\", \\\"hypothesis\\\": \\\"Multi-seed (s123, s456) training across 5 Qwen conditions (PCGrad, UG, LoRA-only, TG, SS) to establish mean±std for all claims. 8 training runs + AR eval N≥50 each. Expect TF convergence (GAR~0.50) and consistent AR rankings across seeds.\\\", \\\"spec\\\": {\\\"command\\\": \\\"python src/train_phase2_v9_pcgrad.py\\\", \\\"server\\\": \\\"westd-20861\\\", \\\"data_path\\\": \\\"data/ultrachat_8k\\\", \\\"data_count\\\": 8000, \\\"model_name\\\": \\\"Qwen2.5-7B-Instruct\\\", \\\"seed\\\": 123, \\\"checkpoint_path\\\": \\\"N/A\\\", \\\"log_path\\\": \\\"runs/d048_pcgrad_s123\\\"}, \\\"conclusion\\\": \\\"killed\\\", \\\"notes\\\": \\\"用户要求停止：30min 内无法完成。PCGrad s123 在 1800/3000 步时被终止，后续 7 个排队任务全部取消。\\\", \\\"checkpoint_path\\\": \\\"N/A\\\", \\\"log_path\\\": \\\"runs/d048_pcgrad_s123\\\", \\\"completed_at\\\": \\\"2026-05-25T11:20:34.089Z\\\"}, \\\"p1_ss_lora_only\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-25T08:58:41.419Z\\\", \\\"updated_at\\\": \\\"2026-05-25T09:42:22.185Z\\\", \\\"hypothesis\\\": \\\"SS training on LoRA-only checkpoint (no ThreadGate) with same hyperparameters (rho_max=0.3, same schedule) should achieve similar GAR improvement as SS+TG. If confirmed, this proves the SS fix is architecture-agnostic, strengthening the paper's mitigation story (the gap is caused by exposure bias in any auxiliary-loss setup, and SS fixes it regardless of gating mechanism).\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash /root/turn_residual_gating/scripts/d048_ss_lo_s42.sh\\\", \\\"server\\\": \\\"westd-20861\\\", \\\"data_path\\\": \\\"/root/turn-residual-gating/data/phase2_train.jsonl\\\", \\\"data_count\\\": 2000, \\\"model_name\\\": \\\"Qwen/Qwen2.5-7B-Instruct\\\", \\\"seed\\\": 42, \\\"notes\\\": \\\"SS+LoRA-only (gate_type=none, ss_max_ratio=0.3). From-scratch training, not resume. Auto TF+AR eval after training. ~6.5h training + eval.\\\"}, \\\"conclusion\\\": \\\"killed\\\", \\\"completed_at\\\": \\\"2026-05-25T09:42:22.185Z\\\"}, \\\"phase2_switching\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-25T08:58:40.187Z\\\", \\\"updated_at\\\": \\\"2026-05-25T09:42:21.391Z\\\", \\\"hypothesis\\\": \\\"TF→AR switching at turn k (k=1..5) on ThreadGate s42 checkpoint. If GAR drops abruptly at the switch point (matching pure-AR level within 1 turn), it confirms exposure bias as instantaneous distribution shift rather than gradual KV cache drift. Staircase = exposure bias dominant; linear slope = KV drift dominant.\\\", \\\"conclusion\\\": \\\"killed\\\", \\\"completed_at\\\": \\\"2026-05-25T09:42:21.391Z\\\"}, \\\"phase2_tf_ar_switching\\\": {\\\"status\\\": \\\"QUEUED\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-25T06:15:36.221Z\\\", \\\"updated_at\\\": \\\"2026-05-25T06:45:27.338Z\\\", \\\"hypothesis\\\": \\\"TF→AR switching at turn k (k=1..5) on ThreadGate s42 checkpoint. If GAR drops abruptly at the switch point (matching pure-AR level within 1 turn), it confirms exposure bias as instantaneous distribution shift rather than gradual cumulative drift.\\\"}, \\\"phase1a_multiseed_8runs\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-25T06:18:08.953Z\\\", \\\"updated_at\\\": \\\"2026-05-25T06:18:08.953Z\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"bash /root/turn_residual_gating/scripts/phase1a_multiseed_runner.sh\\\\\\\"\\\", \\\"server\\\": \\\"westd-20861\\\", \\\"gpu\\\": [\\\"cuda:0\\\"], \\\"pid\\\": \\\"5508\\\", \\\"log_path\\\": \\\"~/runs/turn_residual_gating/phase1a_multiseed_8runs.log\\\", \\\"submitted_at\\\": \\\"2026-05-25T06:18:08.495Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\"}}}, \\\"count\\\": 5, \\\"total\\\": 60, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.2015}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {\"phase1a_multiseed_qwen\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-25T06:15:26.051Z\", \"updated_at\": \"2026-05-25T11:20:34.089Z\", \"hypothesis\": \"Multi-seed (s123, s456) training across 5 Qwen conditions (PCGrad, UG, LoRA-only, TG, SS) to establish mean±std for all claims. 8 training runs + AR eval N≥50 each. Expect TF convergence (GAR~0.50) and consistent AR rankings across seeds.\", \"spec\": {\"command\": \"python src/train_phase2_v9_pcgrad.py\", \"server\": \"westd-20861\", \"data_path\": \"data/ultrachat_8k\", \"data_count\": 8000, \"model_name\": \"Qwen2.5-7B-Instruct\", \"seed\": 123, \"checkpoint_path\": \"N/A\", \"log_path\": \"runs/d048_pcgrad_s123\"}, \"conclusion\": \"killed\", \"notes\": \"用户要求停止：30min 内无法完成。PCGrad s123 在 1800/3000 步时被终止，后续 7 个排队任务全部取消。\", \"checkpoint_path\": \"N/A\", \"log_path\": \"runs/d048_pcgrad_s123\", \"completed_at\": \"2026-05-25T11:20:34.089Z\"}, \"p1_ss_lora_only\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-25T08:58:41.419Z\", \"updated_at\": \"2026-05-25T09:42:22.185Z\", \"hypothesis\": \"SS training on LoRA-only checkpoint (no ThreadGate) with same hyperparameters (rho_max=0.3, same schedule) should achieve similar GAR improvement as SS+TG. If confirmed, this proves the SS fix is architecture-agnostic, strengthening the paper's mitigation story (the gap is caused by exposure bias in any auxiliary-loss setup, and SS fixes it regardless of gating mechanism).\", \"spec\": {\"command\": \"bash /root/turn_residual_gating/scripts/d048_ss_lo_s42.sh\", \"server\": \"westd-20861\", \"data_path\": \"/root/turn-residual-gating/data/phase2_train.jsonl\", \"data_count\": 2000, \"model_name\": \"Qwen/Qwen2.5-7B-Instruct\", \"seed\": 42, \"notes\": \"SS+LoRA-only (gate_type=none, ss_max_ratio=0.3). From-scratch training, not resume. Auto TF+AR eval after training. ~6.5h training + eval.\"}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-25T09:42:22.185Z\"}, \"phase2_switching\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-25T08:58:40.187Z\", \"updated_at\": \"2026-05-25T09:42:21.391Z\", \"hypothesis\": \"TF→AR switching at turn k (k=1..5) on ThreadGate s42 checkpoint. If GAR drops abruptly at the switch point (matching pure-AR level within 1 turn), it confirms exposure bias as instantaneous distribution shift rather than gradual KV cache drift. Staircase = exposure bias dominant; linear slope = KV drift dominant.\", \"conclusion\": \"killed\", \"completed_at\": \"2026-05-25T09:42:21.391Z\"}, \"phase2_tf_ar_switching\": {\"status\": \"QUEUED\", \"retry_count\": 0, \"created_at\": \"2026-05-25T06:15:36.221Z\", \"updated_at\": \"2026-05-25T06:45:27.338Z\", \"hypothesis\": \"TF→AR switching at turn k (k=1..5) on ThreadGate s42 checkpoint. If GAR drops abruptly at the switch point (matching pure-AR level within 1 turn), it confirms exposure bias as instantaneous distribution shift rather than gradual cumulative drift.\"}, \"phase1a_multiseed_8runs\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T06:18:08.953Z\", \"updated_at\": \"2026-05-25T06:18:08.953Z\", \"spec\": {\"command\": \"bash -c \\\"bash /root/turn_residual_gating/scripts/phase1a_multiseed_runner.sh\\\"\", \"server\": \"westd-20861\", \"gpu\": [\"cuda:0\"], \"pid\": \"5508\", \"log_path\": \"~/runs/turn_residual_gating/phase1a_multiseed_8runs.log\", \"submitted_at\": \"2026-05-25T06:18:08.495Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}}, \"count\": 5, \"total\": 60, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.2015}}"
    }
  },
  "sourceToolAssistantUUID": "f74530e3-8c31-4b86-94de-9a0952d5ae6f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921",
  "sessionId": "5d779602-0719-4d06-8bf9-fdd84990d5d0",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---


### Tool result

_source line 16 · 2026-05-25T20:33:54.131Z_

<details><summary>↩ Tool result · `toolu_01LFKp7XAAr12b1Tj3mS1AzX`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/report.md\", \"content\": \"# Handover — 2026-05-25\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n（无）\\n\\n## 待处理\\n- phase2_tf_ar_switching: TF→AR switching at turn k (k=1..5) on ThreadGate s42 checkpoint. If GAR drops abruptly at the switch point (matching pure-AR level within 1 turn), it confirms exposure bias as instantaneous distribution shift rather than gradual cumulative drift.（排队等待 GPU）\\n- phase1a_multiseed_8runs（准备中）\\n- phase1b_llama_complement: Llama PCGrad + UG (s42) to complete cross-model comparison matrix. If Llama PCGrad also fails to improve AR GAR (like Qwen), it strengthens the cross-architecture causal exclusion of gradient conflict.（准备中）\\n- p0_ss_steering_eval: SS training provides AR GAR ~0.385, steering alone gives 0.717. Combining SS checkpoint with beta-steering at inference may approach TF parity (~0.50), demonstrating that SS+steering is a constructive mitigation stack for the TF-AR gap.（准备中）\\n- d048_queue_runner（准备中）\\n- d048_ss_s42_resume（准备中）\\n- llama_tg_training（准备中）\\n\\n## 近期结论\\n- **phase1a_multiseed_qwen** (killed): Multi-seed (s123, s456) training across 5 Qwen conditions (PCGrad, UG, LoRA-only, TG, SS) to establish mean±std for all claims. 8 training runs + AR eval N≥50 each. Expect TF convergence (GAR~0.50) and consistent AR rankings across seeds.\\n- **p1_ss_lora_only** (killed): SS training on LoRA-only checkpoint (no ThreadGate) with same hyperparameters (rho_max=0.3, same schedule) should achieve similar GAR improvement as SS+TG. If confirmed, this proves the SS fix is architecture-agnostic, strengthening the paper's mitigation story (the gap is caused by exposure bias in any auxiliary-loss setup, and SS fixes it regardless of gating mechanism).\\n- **phase2_switching** (killed): TF→AR switching at turn k (k=1..5) on ThreadGate s42 checkpoint. If GAR drops abruptly at the switch point (matching pure-AR level within 1 turn), it confirms exposure bias as instantaneous distribution shift rather than gradual KV cache drift. Staircase = exposure bias dominant; linear slope = KV drift dominant.\\n\\n## 趋势\\n成功 40 / 负向 5 / 失败 4 / 共 53\\n\\n## 下一步\\n（无活跃 idea，请通过 ideas.md 添加）\\n\\n## 资源状态\\nwestd-20861: 无 GPU 信息\\n\\n## 告警\\n- phase2_tg_s42_v2: 已被终止 — unknown\\n- phase2_tg_s42_v4: 训练失败 — unknown\\n- phase2_tg_s42_v8_schedsampling: 训练失败 — unknown\\n- phase2_tg_s42_v8b_ss_fixed: 训练失败 — unknown\\n- d048_split_softmax_eval: 训练失败 — unknown\\n- phase1a_multiseed_qwen: 已被终止 — unknown\\n- phase2_switching: 已被终止 — unknown\\n- p1_ss_lora_only: 已被终止 — unknown\\n\", \"total_chars\": 2436, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5b60a191-9115-43d2-99a4-b300a61cbcb2",
  "isSidechain": false,
  "promptId": "b0f005fa-c14f-47e1-bf29-f3925462c4b7",
  "type": "user",
  "uuid": "813a08c6-b6ce-4383-9b82-670599b621e9",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/report.md\\\", \\\"content\\\": \\\"# Handover — 2026-05-25\\\\n\\\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\\\n\\\\n## 运行中\\\\n（无）\\\\n\\\\n## 待处理\\\\n- phase2_tf_ar_switching: TF→AR switching at turn k (k=1..5) on ThreadGate s42 checkpoint. If GAR drops abruptly at the switch point (matching pure-AR level within 1 turn), it confirms exposure bias as instantaneous distribution shift rather than gradual cumulative drift.（排队等待 GPU）\\\\n- phase1a_multiseed_8runs（准备中）\\\\n- phase1b_llama_complement: Llama PCGrad + UG (s42) to complete cross-model comparison matrix. If Llama PCGrad also fails to improve AR GAR (like Qwen), it strengthens the cross-architecture causal exclusion of gradient conflict.（准备中）\\\\n- p0_ss_steering_eval: SS training provides AR GAR ~0.385, steering alone gives 0.717. Combining SS checkpoint with beta-steering at inference may approach TF parity (~0.50), demonstrating that SS+steering is a constructive mitigation stack for the TF-AR gap.（准备中）\\\\n- d048_queue_runner（准备中）\\\\n- d048_ss_s42_resume（准备中）\\\\n- llama_tg_training（准备中）\\\\n\\\\n## 近期结论\\\\n- **phase1a_multiseed_qwen** (killed): Multi-seed (s123, s456) training across 5 Qwen conditions (PCGrad, UG, LoRA-only, TG, SS) to establish mean±std for all claims. 8 training runs + AR eval N≥50 each. Expect TF convergence (GAR~0.50) and consistent AR rankings across seeds.\\\\n- **p1_ss_lora_only** (killed): SS training on LoRA-only checkpoint (no ThreadGate) with same hyperparameters (rho_max=0.3, same schedule) should achieve similar GAR improvement as SS+TG. If confirmed, this proves the SS fix is architecture-agnostic, strengthening the paper's mitigation story (the gap is caused by exposure bias in any auxiliary-loss setup, and SS fixes it regardless of gating mechanism).\\\\n- **phase2_switching** (killed): TF→AR switching at turn k (k=1..5) on ThreadGate s42 checkpoint. If GAR drops abruptly at the switch point (matching pure-AR level within 1 turn), it confirms exposure bias as instantaneous distribution shift rather than gradual KV cache drift. Staircase = exposure bias dominant; linear slope = KV drift dominant.\\\\n\\\\n## 趋势\\\\n成功 40 / 负向 5 / 失败 4 / 共 53\\\\n\\\\n## 下一步\\\\n（无活跃 idea，请通过 ideas.md 添加）\\\\n\\\\n## 资源状态\\\\nwestd-20861: 无 GPU 信息\\\\n\\\\n## 告警\\\\n- phase2_tg_s42_v2: 已被终止 — unknown\\\\n- phase2_tg_s42_v4: 训练失败 — unknown\\\\n- phase2_tg_s42_v8_schedsampling: 训练失败 — unknown\\\\n- phase2_tg_s42_v8b_ss_fixed: 训练失败 — unknown\\\\n- d048_split_softmax_eval: 训练失败 — unknown\\\\n- phase1a_multiseed_qwen: 已被终止 — unknown\\\\n- phase2_switching: 已被终止 — unknown\\\\n- p1_ss_lora_only: 已被终止 — unknown\\\\n\\\", \\\"total_chars\\\": 2436, \\\"truncated\\\": false}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/report.md\", \"content\": \"# Handover — 2026-05-25\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n（无）\\n\\n## 待处理\\n- phase2_tf_ar_switching: TF→AR switching at turn k (k=1..5) on ThreadGate s42 checkpoint. If GAR drops abruptly at the switch point (matching pure-AR level within 1 turn), it confirms exposure bias as instantaneous distribution shift rather than gradual cumulative drift.（排队等待 GPU）\\n- phase1a_multiseed_8runs（准备中）\\n- phase1b_llama_complement: Llama PCGrad + UG (s42) to complete cross-model comparison matrix. If Llama PCGrad also fails to improve AR GAR (like Qwen), it strengthens the cross-architecture causal exclusion of gradient conflict.（准备中）\\n- p0_ss_steering_eval: SS training provides AR GAR ~0.385, steering alone gives 0.717. Combining SS checkpoint with beta-steering at inference may approach TF parity (~0.50), demonstrating that SS+steering is a constructive mitigation stack for the TF-AR gap.（准备中）\\n- d048_queue_runner（准备中）\\n- d048_ss_s42_resume（准备中）\\n- llama_tg_training（准备中）\\n\\n## 近期结论\\n- **phase1a_multiseed_qwen** (killed): Multi-seed (s123, s456) training across 5 Qwen conditions (PCGrad, UG, LoRA-only, TG, SS) to establish mean±std for all claims. 8 training runs + AR eval N≥50 each. Expect TF convergence (GAR~0.50) and consistent AR rankings across seeds.\\n- **p1_ss_lora_only** (killed): SS training on LoRA-only checkpoint (no ThreadGate) with same hyperparameters (rho_max=0.3, same schedule) should achieve similar GAR improvement as SS+TG. If confirmed, this proves the SS fix is architecture-agnostic, strengthening the paper's mitigation story (the gap is caused by exposure bias in any auxiliary-loss setup, and SS fixes it regardless of gating mechanism).\\n- **phase2_switching** (killed): TF→AR switching at turn k (k=1..5) on ThreadGate s42 checkpoint. If GAR drops abruptly at the switch point (matching pure-AR level within 1 turn), it confirms exposure bias as instantaneous distribution shift rather than gradual KV cache drift. Staircase = exposure bias dominant; linear slope = KV drift dominant.\\n\\n## 趋势\\n成功 40 / 负向 5 / 失败 4 / 共 53\\n\\n## 下一步\\n（无活跃 idea，请通过 ideas.md 添加）\\n\\n## 资源状态\\nwestd-20861: 无 GPU 信息\\n\\n## 告警\\n- phase2_tg_s42_v2: 已被终止 — unknown\\n- phase2_tg_s42_v4: 训练失败 — unknown\\n- phase2_tg_s42_v8_schedsampling: 训练失败 — unknown\\n- phase2_tg_s42_v8b_ss_fixed: 训练失败 — unknown\\n- d048_split_softmax_eval: 训练失败 — unknown\\n- phase1a_multiseed_qwen: 已被终止 — unknown\\n- phase2_switching: 已被终止 — unknown\\n- p1_ss_lora_only: 已被终止 — unknown\\n\", \"total_chars\": 2436, \"truncated\": false}, \"error\": null, \"metadata\": {}}"
    }
  },
  "sourceToolAssistantUUID": "5b60a191-9115-43d2-99a4-b300a61cbcb2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921",
  "sessionId": "5d779602-0719-4d06-8bf9-fdd84990d5d0",
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
  "lastPrompt": "[系统通知 — worker_done:worker_audit_appendix_tables_20260525T201208]: Worker worker_audit_appendix_tables_20260525T201208 已完成（status=done），请审查 Agent 的处理结果。",
  "leafUuid": "813a08c6-b6ce-4383-9b82-670599b621e9",
  "sessionId": "5d779602-0719-4d06-8bf9-fdd84990d5d0"
}
```

---


### Runtime record

_source line 18_

```json
{
  "type": "ai-title",
  "aiTitle": "Review worker audit appendix tables completion",
  "sessionId": "5d779602-0719-4d06-8bf9-fdd84990d5d0"
}
```

---


### Assistant

_source line 19 · 2026-05-25T20:34:01.359Z_

<details><summary>Logged reasoning block</summary>

```text
The worker task was "worker_audit_appendix_tables_20260525T201208" - this seems to be about auditing appendix tables in the paper. Let me look at what was actually done. The report shows recent experiments were killed. I need to find the actual output of this worker - let me check the paper and appendix content.

Let me look at the paper's current state and the appendix tables to understand what the worker was auditing.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "813a08c6-b6ce-4383-9b82-670599b621e9",
  "isSidechain": false,
  "requestId": "req_011CbPvdPNu8Zuo7et5bZhRx",
  "type": "assistant",
  "uuid": "edcaa7a8-e6fd-4f73-9395-cd3979fdf0fc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921",
  "sessionId": "5d779602-0719-4d06-8bf9-fdd84990d5d0",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SULtjMoET9GKeSKagY6yXs",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2796,
      "cache_read_input_tokens": 35633,
      "output_tokens": 237,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2796,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 237,
          "cache_read_input_tokens": 35633,
          "cache_creation_input_tokens": 2796,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2796
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

_source line 20 · 2026-05-25T20:34:02.803Z_

Worker 任务是审计附录表格。我需要查看论文当前的附录内容来审查 worker 的工作。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "edcaa7a8-e6fd-4f73-9395-cd3979fdf0fc",
  "isSidechain": false,
  "requestId": "req_011CbPvdPNu8Zuo7et5bZhRx",
  "type": "assistant",
  "uuid": "da166812-95b0-407e-86c5-00be47d01060",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921",
  "sessionId": "5d779602-0719-4d06-8bf9-fdd84990d5d0",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SULtjMoET9GKeSKagY6yXs",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2796,
      "cache_read_input_tokens": 35633,
      "output_tokens": 237,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2796,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 237,
          "cache_read_input_tokens": 35633,
          "cache_creation_input_tokens": 2796,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2796
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

_source line 21 · 2026-05-25T20:34:03.837Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_014ZaqDtzHdPiDttWszPjBtk`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "da166812-95b0-407e-86c5-00be47d01060",
  "isSidechain": false,
  "requestId": "req_011CbPvdPNu8Zuo7et5bZhRx",
  "type": "assistant",
  "uuid": "137dbd0f-7296-43f7-95cc-5ef3e6d82378",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921",
  "sessionId": "5d779602-0719-4d06-8bf9-fdd84990d5d0",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SULtjMoET9GKeSKagY6yXs",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2796,
      "cache_read_input_tokens": 35633,
      "output_tokens": 237,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2796,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 237,
          "cache_read_input_tokens": 35633,
          "cache_creation_input_tokens": 2796,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2796
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

_source line 22 · 2026-05-25T20:34:03.840Z_

<details><summary>↩ Tool result · `toolu_014ZaqDtzHdPiDttWszPjBtk`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__ssh_read_only"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "137dbd0f-7296-43f7-95cc-5ef3e6d82378",
  "isSidechain": false,
  "promptId": "b0f005fa-c14f-47e1-bf29-f3925462c4b7",
  "type": "user",
  "uuid": "cfc5244b-2eed-4889-b465-f9030765d234",
  "toolUseResult": {
    "matches": [
      "mcp__agent-ml-research__ssh_read_only"
    ],
    "query": "select:mcp__agent-ml-research__ssh_read_only",
    "total_deferred_tools": 35
  },
  "sourceToolAssistantUUID": "137dbd0f-7296-43f7-95cc-5ef3e6d82378",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921",
  "sessionId": "5d779602-0719-4d06-8bf9-fdd84990d5d0",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---


### Tool call

_source line 23 · 2026-05-25T20:34:06.676Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_0182xjj6Lys9axaaLxwW23UV`</summary>

```json
{
  "server": "westd-20861",
  "command": "find /root/turn_residual_gating/paper -name \"*.tex\" -type f"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cfc5244b-2eed-4889-b465-f9030765d234",
  "isSidechain": false,
  "requestId": "req_011CbPve77PBTTBnyo7W7L8s",
  "type": "assistant",
  "uuid": "57e456a0-c94f-40d1-80ef-b4dfbe09d722",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921",
  "sessionId": "5d779602-0719-4d06-8bf9-fdd84990d5d0",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013oq4pFDyiMWSjUNcfxZPYR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 574,
      "cache_read_input_tokens": 38429,
      "output_tokens": 107,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 574,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 107,
          "cache_read_input_tokens": 38429,
          "cache_creation_input_tokens": 574,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 574
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

_source line 24 · 2026-05-25T20:34:07.730Z_

<details><summary>↩ Tool result · `toolu_0182xjj6Lys9axaaLxwW23UV`</summary>

```text
{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"find: '/root/turn_residual_gating/paper': No such file or directory\\n\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 1.04}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "57e456a0-c94f-40d1-80ef-b4dfbe09d722",
  "isSidechain": false,
  "promptId": "b0f005fa-c14f-47e1-bf29-f3925462c4b7",
  "type": "user",
  "uuid": "7b129f06-22d2-4b05-bead-23589ed98237",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {\\\"stdout\\\": \\\"\\\", \\\"stderr\\\": \\\"find: '/root/turn_residual_gating/paper': No such file or directory\\\\n\\\", \\\"return_code\\\": 1}, \\\"error\\\": \\\"exit code 1\\\", \\\"metadata\\\": {\\\"elapsed_seconds\\\": 1.04}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"find: '/root/turn_residual_gating/paper': No such file or directory\\n\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 1.04}}"
    }
  },
  "sourceToolAssistantUUID": "57e456a0-c94f-40d1-80ef-b4dfbe09d722",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921",
  "sessionId": "5d779602-0719-4d06-8bf9-fdd84990d5d0",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---


### Tool call

_source line 25 · 2026-05-25T20:34:10.176Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_0176ieCjfj52iwikdb17Uc39`</summary>

```json
{
  "server": "westd-20861",
  "command": "find /root/turn_residual_gating -name \"*.tex\" -type f -maxdepth 3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7b129f06-22d2-4b05-bead-23589ed98237",
  "isSidechain": false,
  "requestId": "req_011CbPvePVd9FwWMUCXABM3y",
  "type": "assistant",
  "uuid": "ca8dfd84-3cb8-45bf-9a43-a64c1eafa342",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921",
  "sessionId": "5d779602-0719-4d06-8bf9-fdd84990d5d0",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018KubsxNMx8qdAh7aw81ZXe",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 209,
      "cache_read_input_tokens": 39003,
      "output_tokens": 111,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 209,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 111,
          "cache_read_input_tokens": 39003,
          "cache_creation_input_tokens": 209,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 209
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

_source line 26 · 2026-05-25T20:34:10.626Z_

<details><summary>↩ Tool result · `toolu_0176ieCjfj52iwikdb17Uc39`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ca8dfd84-3cb8-45bf-9a43-a64c1eafa342",
  "isSidechain": false,
  "promptId": "b0f005fa-c14f-47e1-bf29-f3925462c4b7",
  "type": "user",
  "uuid": "e537cebb-1bc3-4443-9998-3d6981848468",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.44}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"
    }
  },
  "sourceToolAssistantUUID": "ca8dfd84-3cb8-45bf-9a43-a64c1eafa342",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921",
  "sessionId": "5d779602-0719-4d06-8bf9-fdd84990d5d0",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---


### Assistant

_source line 27 · 2026-05-25T20:34:13.057Z_

<details><summary>Logged reasoning block</summary>

```text
No .tex files on the remote server. The paper is probably in the local workspace. Let me check.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e537cebb-1bc3-4443-9998-3d6981848468",
  "isSidechain": false,
  "requestId": "req_011CbPvebrX8bNYoJqQ2hv8u",
  "type": "assistant",
  "uuid": "e14e5c90-dad3-47ce-b0b4-d54c3fe2c04d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921",
  "sessionId": "5d779602-0719-4d06-8bf9-fdd84990d5d0",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BfPuD3vkGy7ye55Vix5QHV",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 184,
      "cache_read_input_tokens": 39212,
      "output_tokens": 159,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 184,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 159,
          "cache_read_input_tokens": 39212,
          "cache_creation_input_tokens": 184,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 184
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

_source line 28 · 2026-05-25T20:34:13.528Z_

论文不在远程服务器上。让我在本地 workspace 查找。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e14e5c90-dad3-47ce-b0b4-d54c3fe2c04d",
  "isSidechain": false,
  "requestId": "req_011CbPvebrX8bNYoJqQ2hv8u",
  "type": "assistant",
  "uuid": "25701772-219a-4479-b7b3-86fcb6012f60",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921",
  "sessionId": "5d779602-0719-4d06-8bf9-fdd84990d5d0",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BfPuD3vkGy7ye55Vix5QHV",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 184,
      "cache_read_input_tokens": 39212,
      "output_tokens": 159,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 184,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 159,
          "cache_read_input_tokens": 39212,
          "cache_creation_input_tokens": 184,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 184
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

_source line 29 · 2026-05-25T20:34:15.228Z_

<details open><summary>🔧 Tool call — Glob · `toolu_0159xBCdMVJsGJUNLxAF7NtQ`</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "25701772-219a-4479-b7b3-86fcb6012f60",
  "isSidechain": false,
  "requestId": "req_011CbPvebrX8bNYoJqQ2hv8u",
  "type": "assistant",
  "uuid": "011d8fa9-3017-4875-8151-03f20d5bce40",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921",
  "sessionId": "5d779602-0719-4d06-8bf9-fdd84990d5d0",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BfPuD3vkGy7ye55Vix5QHV",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 184,
      "cache_read_input_tokens": 39212,
      "output_tokens": 159,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 184,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 159,
          "cache_read_input_tokens": 39212,
          "cache_creation_input_tokens": 184,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 184
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

_source line 30 · 2026-05-25T20:34:15.274Z_

<details><summary>↩ Tool result · `toolu_0159xBCdMVJsGJUNLxAF7NtQ`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T135115/best/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T135115/median/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T135115/worst/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T143220/best/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T143220/median/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T145320/best/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T145320/median/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T145320/worst/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/background.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/_project/paper/analysis.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/experiments.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/analysis.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/discussion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/limitations.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/_project/paper/table_steering_full.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/table_steering_full.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260524T081135/best/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260524T081135/median/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260524T081135/worst/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/_project/paper/tab_dataset_stats.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/_project/paper/tab_gar_robustness.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/_project/paper/tab_mmlu_detail.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/_project/paper/tab_qwen15b_results.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/_project/data/tab_statistical_tests.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/appendix_expansion/tab_gar_robustness.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/appendix_expansion/tab_statistical_tests.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/appendix_expansion/tab_perseed_ss.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/appendix_expansion/tab_perseed_tg.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/appendix_expansion/tab_perturn_qwen.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/appendix_expansion/tab_mmlu_detail.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/appendix_expansion/tab_qwen15b_results.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/appendix_expansion/tab_crossmodel_detail.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/appendix_expansion/tab_dataset_stats.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/appendix_expansion/tab_perturn_llama.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/discussion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/analysis.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/experiments.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/limitations.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/main.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/sections/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/sections/analysis.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/sections/appendix.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/sections/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/sections/discussion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/sections/experiments.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/sections/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/sections/limitations.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/sections/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/sections/related_work.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "011d8fa9-3017-4875-8151-03f20d5bce40",
  "isSidechain": false,
  "promptId": "b0f005fa-c14f-47e1-bf29-f3925462c4b7",
  "type": "user",
  "uuid": "32486205-8db0-47d8-9d6f-ae5524213cd0",
  "toolUseResult": {
    "filenames": [
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T135115/best/paper.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T135115/median/paper.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T135115/worst/paper.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T143220/best/paper.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T143220/median/paper.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T145320/best/paper.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T145320/median/paper.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260519T145320/worst/paper.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/background.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/_project/paper/analysis.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/related_work.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/experiments.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/method.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/introduction.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/analysis.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/discussion.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/conclusion.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/limitations.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/abstract.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/_project/paper/table_steering_full.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/table_steering_full.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260524T081135/best/paper.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260524T081135/median/paper.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260524T081135/worst/paper.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/_project/paper/tab_dataset_stats.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/_project/paper/tab_gar_robustness.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/_project/paper/tab_mmlu_detail.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/_project/paper/tab_qwen15b_results.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/_project/data/tab_statistical_tests.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/appendix_expansion/tab_gar_robustness.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/appendix_expansion/tab_statistical_tests.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/appendix_expansion/tab_perseed_ss.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/appendix_expansion/tab_perseed_tg.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/appendix_expansion/tab_perturn_qwen.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/appendix_expansion/tab_mmlu_detail.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/appendix_expansion/tab_qwen15b_results.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/appendix_expansion/tab_crossmodel_detail.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/appendix_expansion/tab_dataset_stats.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/appendix_expansion/tab_perturn_llama.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/discussion.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/introduction.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/abstract.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/analysis.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/method.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/related_work.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/experiments.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/limitations.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/conclusion.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/main.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/sections/abstract.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/sections/analysis.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/sections/appendix.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/sections/conclusion.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/sections/discussion.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/sections/experiments.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/sections/introduction.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/sections/limitations.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/sections/method.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/sections/related_work.tex"
    ],
    "durationMs": 39,
    "numFiles": 60,
    "truncated": false
  },
  "sourceToolAssistantUUID": "011d8fa9-3017-4875-8151-03f20d5bce40",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921",
  "sessionId": "5d779602-0719-4d06-8bf9-fdd84990d5d0",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---


### Runtime record

_source line 31 · 2026-05-25T20:34:15.375Z_

```json
{
  "parentUuid": "32486205-8db0-47d8-9d6f-ae5524213cd0",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "725ee829-c108-4567-bbc6-924008a2930b",
  "timestamp": "2026-05-25T20:34:15.375Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921",
  "sessionId": "5d779602-0719-4d06-8bf9-fdd84990d5d0",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---


### Assistant

_source line 32 · 2026-05-25T20:34:21.711Z_

<details><summary>Logged reasoning block</summary>

```text
The worker was auditing appendix tables. Let me check the appendix content and the appendix expansion tables. I need to read the appendix.tex and cross-reference the table data with the registry.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "725ee829-c108-4567-bbc6-924008a2930b",
  "isSidechain": false,
  "requestId": "req_011CbPvex7RH5bY93v4MHUSs",
  "type": "assistant",
  "uuid": "85a6e209-8600-4b77-b63a-2385aeb73bb0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921",
  "sessionId": "5d779602-0719-4d06-8bf9-fdd84990d5d0",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01946BiMqvn9RyjEosR4uPp7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2853,
      "cache_read_input_tokens": 39396,
      "output_tokens": 508,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2853,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 508,
          "cache_read_input_tokens": 39396,
          "cache_creation_input_tokens": 2853,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2853
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

_source line 33 · 2026-05-25T20:34:23.179Z_

让我读取附录和相关的附录表格，同时检查 registry 中完成的实验数据来交叉验证。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "85a6e209-8600-4b77-b63a-2385aeb73bb0",
  "isSidechain": false,
  "requestId": "req_011CbPvex7RH5bY93v4MHUSs",
  "type": "assistant",
  "uuid": "419d7070-76ff-4bb2-ae52-33a2fa4ec334",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921",
  "sessionId": "5d779602-0719-4d06-8bf9-fdd84990d5d0",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01946BiMqvn9RyjEosR4uPp7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2853,
      "cache_read_input_tokens": 39396,
      "output_tokens": 508,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2853,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 508,
          "cache_read_input_tokens": 39396,
          "cache_creation_input_tokens": 2853,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2853
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

_source line 34 · 2026-05-25T20:34:23.706Z_

<details open><summary>🔧 Tool call — Read · `toolu_01G8GeZJ5s9CyFDR2ua2yb1c`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "419d7070-76ff-4bb2-ae52-33a2fa4ec334",
  "isSidechain": false,
  "requestId": "req_011CbPvex7RH5bY93v4MHUSs",
  "type": "assistant",
  "uuid": "cd261ba4-18cb-44c8-bbf5-15ca8a55d4d8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921",
  "sessionId": "5d779602-0719-4d06-8bf9-fdd84990d5d0",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01946BiMqvn9RyjEosR4uPp7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2853,
      "cache_read_input_tokens": 39396,
      "output_tokens": 508,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2853,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 508,
          "cache_read_input_tokens": 39396,
          "cache_creation_input_tokens": 2853,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2853
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

_source line 35 · 2026-05-25T20:34:26.542Z_

<details><summary>↩ Tool result · `toolu_01MX75vx7QvF3mMcGmCyZmsR`</summary>

```text
1	% Per-seed detailed results for ThreadGate (TG) — seeds 42, 123
2	% TF eval: N=200 held-out conversations
3	% AR eval: N=5, T=10 model-generated conversations (original eval protocol)
4	\begin{table}[h]
5	\centering
6	\caption{Per-seed results for ThreadGate (TG) on Qwen2.5-7B-Instruct.
7	TF evaluation uses 200 held-out conversations.
8	AR evaluation uses 5 model-generated conversations with 10 turns each.}
9	\label{tab:perseed-tg}
10	\resizebox{\columnwidth}{!}{
11	\begin{tabular}{@{}l cc c@{}}
12	\toprule
13	\textbf{Metric} & \textbf{Seed 42} & \textbf{Seed 123} & \textbf{Mean $\pm$ Std} \\
14	\midrule
15	\multicolumn{4}{@{}l}{\textit{Teacher-Forced (TF)}} \\
16	\quad GAR-ours $\uparrow$   & 0.504 & 0.505 & 0.504 $\pm$ 0.001 \\
17	\quad GAR-Dongre $\uparrow$ & 0.015 & 0.012 & 0.014 $\pm$ 0.002 \\
18	\quad PPL $\downarrow$       & 2.784 & 2.780 & 2.782 $\pm$ 0.003 \\
19	\midrule
20	\multicolumn{4}{@{}l}{\textit{Autoregressive (AR), $\beta = 0$}} \\
21	\quad GAR-ours $\uparrow$   & 0.016 & 0.017 & 0.016 $\pm$ 0.001 \\
22	\quad GAR-Dongre $\uparrow$ & 0.019 & 0.018 & 0.019 $\pm$ 0.001 \\
23	\quad PPL $\downarrow$       & 1.360 & 1.386 & 1.373 $\pm$ 0.018 \\
24	\midrule
25	\multicolumn{4}{@{}l}{\textit{Derived}} \\
26	\quad Gap ratio (TF/AR GAR-ours) $\downarrow$ & 32.1 & 30.6 & 31.4 $\pm$ 1.1 \\
27	\bottomrule
28	\end{tabular}}
29	\end{table}
30	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "06c1e2fb-95e6-4ad5-a890-8b12b41967dd",
  "isSidechain": false,
  "promptId": "b0f005fa-c14f-47e1-bf29-f3925462c4b7",
  "type": "user",
  "uuid": "9e875b2b-7565-4aa4-aa4e-8a54c2033458",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/appendix_expansion/tab_perseed_tg.tex",
      "content": "% Per-seed detailed results for ThreadGate (TG) — seeds 42, 123\n% TF eval: N=200 held-out conversations\n% AR eval: N=5, T=10 model-generated conversations (original eval protocol)\n\\begin{table}[h]\n\\centering\n\\caption{Per-seed results for ThreadGate (TG) on Qwen2.5-7B-Instruct.\nTF evaluation uses 200 held-out conversations.\nAR evaluation uses 5 model-generated conversations with 10 turns each.}\n\\label{tab:perseed-tg}\n\\resizebox{\\columnwidth}{!}{\n\\begin{tabular}{@{}l cc c@{}}\n\\toprule\n\\textbf{Metric} & \\textbf{Seed 42} & \\textbf{Seed 123} & \\textbf{Mean $\\pm$ Std} \\\\\n\\midrule\n\\multicolumn{4}{@{}l}{\\textit{Teacher-Forced (TF)}} \\\\\n\\quad GAR-ours $\\uparrow$   & 0.504 & 0.505 & 0.504 $\\pm$ 0.001 \\\\\n\\quad GAR-Dongre $\\uparrow$ & 0.015 & 0.012 & 0.014 $\\pm$ 0.002 \\\\\n\\quad PPL $\\downarrow$       & 2.784 & 2.780 & 2.782 $\\pm$ 0.003 \\\\\n\\midrule\n\\multicolumn{4}{@{}l}{\\textit{Autoregressive (AR), $\\beta = 0$}} \\\\\n\\quad GAR-ours $\\uparrow$   & 0.016 & 0.017 & 0.016 $\\pm$ 0.001 \\\\\n\\quad GAR-Dongre $\\uparrow$ & 0.019 & 0.018 & 0.019 $\\pm$ 0.001 \\\\\n\\quad PPL $\\downarrow$       & 1.360 & 1.386 & 1.373 $\\pm$ 0.018 \\\\\n\\midrule\n\\multicolumn{4}{@{}l}{\\textit{Derived}} \\\\\n\\quad Gap ratio (TF/AR GAR-ours) $\\downarrow$ & 32.1 & 30.6 & 31.4 $\\pm$ 1.1 \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n",
      "numLines": 30,
      "startLine": 1,
      "totalLines": 30
    }
  },
  "sourceToolAssistantUUID": "06c1e2fb-95e6-4ad5-a890-8b12b41967dd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921",
  "sessionId": "5d779602-0719-4d06-8bf9-fdd84990d5d0",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---


### Tool result

_source line 36 · 2026-05-25T20:34:23.965Z_

<details><summary>↩ Tool result · reported error · `toolu_01G8GeZJ5s9CyFDR2ua2yb1c`</summary>

```text
File content (26122 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cd261ba4-18cb-44c8-bbf5-15ca8a55d4d8",
  "isSidechain": false,
  "promptId": "b0f005fa-c14f-47e1-bf29-f3925462c4b7",
  "type": "user",
  "uuid": "dcdaf6dd-098c-4b25-84e6-4d4ac0ff89fd",
  "toolUseResult": "Error: File content (26122 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.",
  "sourceToolAssistantUUID": "cd261ba4-18cb-44c8-bbf5-15ca8a55d4d8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921",
  "sessionId": "5d779602-0719-4d06-8bf9-fdd84990d5d0",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---


### Tool call

_source line 37 · 2026-05-25T20:34:24.714Z_

<details open><summary>🔧 Tool call — Read · `toolu_01AStJsomkMygryo3QVJRJmg`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/appendix_expansion/tab_gar_robustness.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dcdaf6dd-098c-4b25-84e6-4d4ac0ff89fd",
  "isSidechain": false,
  "requestId": "req_011CbPvex7RH5bY93v4MHUSs",
  "type": "assistant",
  "uuid": "cd3e8127-f57a-40aa-a759-9cba38c76268",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921",
  "sessionId": "5d779602-0719-4d06-8bf9-fdd84990d5d0",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01946BiMqvn9RyjEosR4uPp7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2853,
      "cache_read_input_tokens": 39396,
      "output_tokens": 508,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2853,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 508,
          "cache_read_input_tokens": 39396,
          "cache_creation_input_tokens": 2853,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2853
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

_source line 38 · 2026-05-25T20:34:24.719Z_

<details><summary>↩ Tool result · `toolu_01AStJsomkMygryo3QVJRJmg`</summary>

```text
1	% GAR definition robustness: 4 token selection strategies x 3 conditions
2	\begin{table*}[t]
3	\centering
4	\small
5	\caption{GAR robustness across token selection strategies. We evaluate four ways to select the token position for gradient attribution: \textbf{Last} (final token of each turn), \textbf{All} (mean over all tokens), \textbf{First} (first token), and \textbf{Goal-only} (goal token as in \citet{dongre2026attention}). Turn-1 and Mid-turn GAR are measured under autoregressive generation on 50 held-out conversations. Gap Ratio = Turn-1 / Mid-turn; lower indicates better gradient preservation across turns.}
6	\label{tab:gar_robustness}
7	\begin{tabular}{@{}ll ccc@{}}
8	\toprule
9	\textbf{Token Selection} & \textbf{Condition} & \textbf{Turn-1 GAR} & \textbf{Mid-turn GAR} & \textbf{Gap Ratio} $\downarrow$ \\
10	\midrule
11	\multirow{3}{*}{Last (ours)}
12	  & Base      & 0.0858 & 0.0152 & 5.64$\times$ \\
13	  & TG        & 0.3938 & 0.3254 & 1.21$\times$ \\
14	  & SS        & 0.5274 & 0.4582 & 1.15$\times$ \\
15	\midrule
16	\multirow{3}{*}{All tokens}
17	  & Base      & 0.1152 & 0.0152 & 7.57$\times$ \\
18	  & TG        & 0.1275 & 0.0253 & 5.04$\times$ \\
19	  & SS        & 0.5043 & 0.3658 & 1.38$\times$ \\
20	\midrule
21	\multirow{3}{*}{First token}
22	  & Base      & 0.2987 & 0.0224 & 13.32$\times$ \\
23	  & TG        & 0.3225 & 0.0392 & 8.24$\times$ \\
24	  & SS        & 0.7549 & 0.4118 & 1.83$\times$ \\
25	\midrule
26	\multirow{3}{*}{Goal-only}
27	  & Base      & 0.0110 & 0.0049 & 2.23$\times$ \\
28	  & TG        & 0.3313 & 0.3103 & 1.07$\times$ \\
29	  & SS        & 0.4528 & 0.4435 & 1.02$\times$ \\
30	\bottomrule
31	\end{tabular}
32	\end{table*}
33	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cd3e8127-f57a-40aa-a759-9cba38c76268",
  "isSidechain": false,
  "promptId": "b0f005fa-c14f-47e1-bf29-f3925462c4b7",
  "type": "user",
  "uuid": "a3a247b0-ef2f-462d-bb58-e979a0ad806c",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/appendix_expansion/tab_gar_robustness.tex",
      "content": "% GAR definition robustness: 4 token selection strategies x 3 conditions\n\\begin{table*}[t]\n\\centering\n\\small\n\\caption{GAR robustness across token selection strategies. We evaluate four ways to select the token position for gradient attribution: \\textbf{Last} (final token of each turn), \\textbf{All} (mean over all tokens), \\textbf{First} (first token), and \\textbf{Goal-only} (goal token as in \\citet{dongre2026attention}). Turn-1 and Mid-turn GAR are measured under autoregressive generation on 50 held-out conversations. Gap Ratio = Turn-1 / Mid-turn; lower indicates better gradient preservation across turns.}\n\\label{tab:gar_robustness}\n\\begin{tabular}{@{}ll ccc@{}}\n\\toprule\n\\textbf{Token Selection} & \\textbf{Condition} & \\textbf{Turn-1 GAR} & \\textbf{Mid-turn GAR} & \\textbf{Gap Ratio} $\\downarrow$ \\\\\n\\midrule\n\\multirow{3}{*}{Last (ours)}\n  & Base      & 0.0858 & 0.0152 & 5.64$\\times$ \\\\\n  & TG        & 0.3938 & 0.3254 & 1.21$\\times$ \\\\\n  & SS        & 0.5274 & 0.4582 & 1.15$\\times$ \\\\\n\\midrule\n\\multirow{3}{*}{All tokens}\n  & Base      & 0.1152 & 0.0152 & 7.57$\\times$ \\\\\n  & TG        & 0.1275 & 0.0253 & 5.04$\\times$ \\\\\n  & SS        & 0.5043 & 0.3658 & 1.38$\\times$ \\\\\n\\midrule\n\\multirow{3}{*}{First token}\n  & Base      & 0.2987 & 0.0224 & 13.32$\\times$ \\\\\n  & TG        & 0.3225 & 0.0392 & 8.24$\\times$ \\\\\n  & SS        & 0.7549 & 0.4118 & 1.83$\\times$ \\\\\n\\midrule\n\\multirow{3}{*}{Goal-only}\n  & Base      & 0.0110 & 0.0049 & 2.23$\\times$ \\\\\n  & TG        & 0.3313 & 0.3103 & 1.07$\\times$ \\\\\n  & SS        & 0.4528 & 0.4435 & 1.02$\\times$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n",
      "numLines": 33,
      "startLine": 1,
      "totalLines": 33
    }
  },
  "sourceToolAssistantUUID": "cd3e8127-f57a-40aa-a759-9cba38c76268",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921",
  "sessionId": "5d779602-0719-4d06-8bf9-fdd84990d5d0",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---


### Tool call

_source line 39 · 2026-05-25T20:34:25.223Z_

<details open><summary>🔧 Tool call — Read · `toolu_01QH6a2J885ostrexgFz2HSY`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/appendix_expansion/tab_statistical_tests.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a3a247b0-ef2f-462d-bb58-e979a0ad806c",
  "isSidechain": false,
  "requestId": "req_011CbPvex7RH5bY93v4MHUSs",
  "type": "assistant",
  "uuid": "8fbd3301-50af-4599-8c7e-67011c51c985",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921",
  "sessionId": "5d779602-0719-4d06-8bf9-fdd84990d5d0",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01946BiMqvn9RyjEosR4uPp7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2853,
      "cache_read_input_tokens": 39396,
      "output_tokens": 508,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2853,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 508,
          "cache_read_input_tokens": 39396,
          "cache_creation_input_tokens": 2853,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2853
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

_source line 40 · 2026-05-25T20:34:25.228Z_

<details><summary>↩ Tool result · `toolu_01QH6a2J885ostrexgFz2HSY`</summary>

```text
1	% Item 9: Statistical tests summary table
2	% Wilcoxon signed-rank tests for per-dialogue GAR + McNemar for instruction retention
3	\begin{table*}[t]
4	\centering
5	\caption{Summary of statistical significance tests.
6	  Wilcoxon signed-rank tests compare per-dialogue GAR across training configurations ($N\!=\!39$);
7	  McNemar's test assesses instruction-following retention under steering ($N\!=\!54$ paired instances).
8	  Bootstrap 95\% CIs from 10{,}000 resamples.
9	  Significance: $^{***}\!p<.001$, $^{**}\!p<.01$, $^{*}\!p<.05$.}
10	\label{tab:statistical_tests}
11	\small
12	\setlength{\tabcolsep}{4pt}
13	\begin{tabular}{@{}llcrrccl@{}}
14	\toprule
15	$\beta$ & Comparison & Test & Stat. & $p$ & $r$ & $\overline{\mathrm{GAR}}$\;[95\% CI] & Sig. \\
16	\midrule
17	\multirow{4}{*}{0.0}
18	 & TG vs Base    & Wilcoxon & $W\!=\!31$  & ${<}.001$ & .802 & .064\,[.041,\,.091]\;vs\;.019\,[.014,\,.024] & $^{***}$ \\
19	 & TG vs LoRA    & Wilcoxon & $W\!=\!187$ & .004      & .454 & .064\,[.041,\,.091]\;vs\;.037\,[.027,\,.050] & $^{**}$  \\
20	 & SS vs TG      & Wilcoxon & $W\!=\!1$   & ${<}.001$ & .869 & .347\,[.327,\,.366]\;vs\;.064\,[.041,\,.091] & $^{***}$ \\
21	 & PCGrad vs TG  & Wilcoxon & $W\!=\!176$ & .002      & .478 & .030\,[.023,\,.038]\;vs\;.064\,[.041,\,.091] & $^{**}$  \\
22	\midrule
23	\multirow{4}{*}{3.0}
24	 & TG vs Base    & Wilcoxon & $W\!=\!242$ & .039 & .331 & .556\,[.538,\,.575]\;vs\;.531\,[.514,\,.550] & $^{*}$  \\
25	 & TG vs LoRA    & Wilcoxon & $W\!=\!376$ & .852 & .031 & .556\,[.538,\,.575]\;vs\;.560\,[.541,\,.581] & n.s.    \\
26	 & SS vs TG      & Wilcoxon & $W\!=\!207$ & .010 & .409 & .593\,[.574,\,.613]\;vs\;.556\,[.538,\,.575] & $^{**}$ \\
27	 & PCGrad vs TG  & Wilcoxon & $W\!=\!368$ & .767 & .049 & .559\,[.543,\,.576]\;vs\;.556\,[.538,\,.575] & n.s.    \\
28	\midrule
29	\multirow{4}{*}{5.0}
30	 & TG vs Base    & Wilcoxon & $W\!=\!251$ & .084 & .281 & .727\,[.708,\,.747]\;vs\;.704\,[.679,\,.730] & n.s. \\
31	 & TG vs LoRA    & Wilcoxon & $W\!=\!277$ & .180 & .220 & .727\,[.708,\,.747]\;vs\;.708\,[.687,\,.729] & n.s. \\
32	 & SS vs TG      & Wilcoxon & $W\!=\!314$ & .421 & .133 & .717\,[.696,\,.738]\;vs\;.727\,[.708,\,.747] & n.s. \\
33	 & PCGrad vs TG  & Wilcoxon & $W\!=\!266$ & .133 & .246 & .708\,[.690,\,.727]\;vs\;.727\,[.708,\,.747] & n.s. \\
34	\midrule
35	\multicolumn{8}{@{}l}{\textit{Instruction-following retention} ($\beta\!=\!0 \to 3$, ThreadGate only)} \\[2pt]
36	 & $\beta\!=\!0$ vs $\beta\!=\!3$ & McNemar & $\chi^2\!=\!3.13$ & .077 & $.200^{\dagger}$ & Rate: .759\;vs\;.870\;($N\!=\!54$) & n.s.$^{\ddagger}$ \\
37	\bottomrule
38	\end{tabular}
39	\\[4pt]
40	{\footnotesize
41	$^{\dagger}$\,Point-biserial $r$; associated $p=.007$ (significant).
42	$^{\ddagger}$\,Marginal by McNemar ($p=.077$); significant by point-biserial correlation.
43	}
44	\end{table*}
45	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8fbd3301-50af-4599-8c7e-67011c51c985",
  "isSidechain": false,
  "promptId": "b0f005fa-c14f-47e1-bf29-f3925462c4b7",
  "type": "user",
  "uuid": "9689959b-22dd-4d4c-a95e-522b60cea2c1",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/appendix_expansion/tab_statistical_tests.tex",
      "content": "% Item 9: Statistical tests summary table\n% Wilcoxon signed-rank tests for per-dialogue GAR + McNemar for instruction retention\n\\begin{table*}[t]\n\\centering\n\\caption{Summary of statistical significance tests.\n  Wilcoxon signed-rank tests compare per-dialogue GAR across training configurations ($N\\!=\\!39$);\n  McNemar's test assesses instruction-following retention under steering ($N\\!=\\!54$ paired instances).\n  Bootstrap 95\\% CIs from 10{,}000 resamples.\n  Significance: $^{***}\\!p<.001$, $^{**}\\!p<.01$, $^{*}\\!p<.05$.}\n\\label{tab:statistical_tests}\n\\small\n\\setlength{\\tabcolsep}{4pt}\n\\begin{tabular}{@{}llcrrccl@{}}\n\\toprule\n$\\beta$ & Comparison & Test & Stat. & $p$ & $r$ & $\\overline{\\mathrm{GAR}}$\\;[95\\% CI] & Sig. \\\\\n\\midrule\n\\multirow{4}{*}{0.0}\n & TG vs Base    & Wilcoxon & $W\\!=\\!31$  & ${<}.001$ & .802 & .064\\,[.041,\\,.091]\\;vs\\;.019\\,[.014,\\,.024] & $^{***}$ \\\\\n & TG vs LoRA    & Wilcoxon & $W\\!=\\!187$ & .004      & .454 & .064\\,[.041,\\,.091]\\;vs\\;.037\\,[.027,\\,.050] & $^{**}$  \\\\\n & SS vs TG      & Wilcoxon & $W\\!=\\!1$   & ${<}.001$ & .869 & .347\\,[.327,\\,.366]\\;vs\\;.064\\,[.041,\\,.091] & $^{***}$ \\\\\n & PCGrad vs TG  & Wilcoxon & $W\\!=\\!176$ & .002      & .478 & .030\\,[.023,\\,.038]\\;vs\\;.064\\,[.041,\\,.091] & $^{**}$  \\\\\n\\midrule\n\\multirow{4}{*}{3.0}\n & TG vs Base    & Wilcoxon & $W\\!=\\!242$ & .039 & .331 & .556\\,[.538,\\,.575]\\;vs\\;.531\\,[.514,\\,.550] & $^{*}$  \\\\\n & TG vs LoRA    & Wilcoxon & $W\\!=\\!376$ & .852 & .031 & .556\\,[.538,\\,.575]\\;vs\\;.560\\,[.541,\\,.581] & n.s.    \\\\\n & SS vs TG      & Wilcoxon & $W\\!=\\!207$ & .010 & .409 & .593\\,[.574,\\,.613]\\;vs\\;.556\\,[.538,\\,.575] & $^{**}$ \\\\\n & PCGrad vs TG  & Wilcoxon & $W\\!=\\!368$ & .767 & .049 & .559\\,[.543,\\,.576]\\;vs\\;.556\\,[.538,\\,.575] & n.s.    \\\\\n\\midrule\n\\multirow{4}{*}{5.0}\n & TG vs Base    & Wilcoxon & $W\\!=\\!251$ & .084 & .281 & .727\\,[.708,\\,.747]\\;vs\\;.704\\,[.679,\\,.730] & n.s. \\\\\n & TG vs LoRA    & Wilcoxon & $W\\!=\\!277$ & .180 & .220 & .727\\,[.708,\\,.747]\\;vs\\;.708\\,[.687,\\,.729] & n.s. \\\\\n & SS vs TG      & Wilcoxon & $W\\!=\\!314$ & .421 & .133 & .717\\,[.696,\\,.738]\\;vs\\;.727\\,[.708,\\,.747] & n.s. \\\\\n & PCGrad vs TG  & Wilcoxon & $W\\!=\\!266$ & .133 & .246 & .708\\,[.690,\\,.727]\\;vs\\;.727\\,[.708,\\,.747] & n.s. \\\\\n\\midrule\n\\multicolumn{8}{@{}l}{\\textit{Instruction-following retention} ($\\beta\\!=\\!0 \\to 3$, ThreadGate only)} \\\\[2pt]\n & $\\beta\\!=\\!0$ vs $\\beta\\!=\\!3$ & McNemar & $\\chi^2\\!=\\!3.13$ & .077 & $.200^{\\dagger}$ & Rate: .759\\;vs\\;.870\\;($N\\!=\\!54$) & n.s.$^{\\ddagger}$ \\\\\n\\bottomrule\n\\end{tabular}\n\\\\[4pt]\n{\\footnotesize\n$^{\\dagger}$\\,Point-biserial $r$; associated $p=.007$ (significant).\n$^{\\ddagger}$\\,Marginal by McNemar ($p=.077$); significant by point-biserial correlation.\n}\n\\end{table*}\n",
      "numLines": 45,
      "startLine": 1,
      "totalLines": 45
    }
  },
  "sourceToolAssistantUUID": "8fbd3301-50af-4599-8c7e-67011c51c985",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921",
  "sessionId": "5d779602-0719-4d06-8bf9-fdd84990d5d0",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---


### Tool call

_source line 41 · 2026-05-25T20:34:26.223Z_

<details open><summary>🔧 Tool call — Read · `toolu_01KF6HGaXoUVa7nVtnJSMBb8`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/appendix_expansion/tab_perseed_ss.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9689959b-22dd-4d4c-a95e-522b60cea2c1",
  "isSidechain": false,
  "requestId": "req_011CbPvex7RH5bY93v4MHUSs",
  "type": "assistant",
  "uuid": "129ec2fc-9f75-4129-bc65-3bed4c4aa68f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921",
  "sessionId": "5d779602-0719-4d06-8bf9-fdd84990d5d0",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01946BiMqvn9RyjEosR4uPp7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2853,
      "cache_read_input_tokens": 39396,
      "output_tokens": 508,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2853,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 508,
          "cache_read_input_tokens": 39396,
          "cache_creation_input_tokens": 2853,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2853
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

_source line 42 · 2026-05-25T20:34:26.228Z_

<details><summary>↩ Tool result · `toolu_01KF6HGaXoUVa7nVtnJSMBb8`</summary>

```text
1	% Per-seed detailed results for Scheduled Sampling (SS) — seeds 42, 123, 456
2	% TF eval: N=200, T=3 (teacher-forced on held-out eval_200 set)
3	% AR eval: N=50 gen-mode, beta=0/3/5 (from d048_final_ar)
4	\begin{table}[h]
5	\centering
6	\caption{Per-seed results for Scheduled Sampling (SS) on Qwen2.5-7B-Instruct.
7	TF evaluation uses 200 held-out conversations; AR evaluation uses 50 model-generated conversations in free-form generation mode ($N_{\text{valid}} \approx 39$).}
8	\label{tab:perseed-ss}
9	\resizebox{\columnwidth}{!}{
10	\begin{tabular}{@{}l ccc c@{}}
11	\toprule
12	\textbf{Metric} & \textbf{Seed 42} & \textbf{Seed 123} & \textbf{Seed 456} & \textbf{Mean $\pm$ Std} \\
13	\midrule
14	\multicolumn{5}{@{}l}{\textit{Teacher-Forced (TF)}} \\
15	\quad GAR-ours $\uparrow$   & 0.502 & 0.554 & 0.496 & 0.517 $\pm$ 0.032 \\
16	\quad GAR-Dongre $\uparrow$ & 0.389 & 0.411 & 0.386 & 0.395 $\pm$ 0.014 \\
17	\quad PPL $\downarrow$       & 2.780 & 2.612 & 2.611 & 2.668 $\pm$ 0.097 \\
18	\midrule
19	\multicolumn{5}{@{}l}{\textit{Autoregressive (AR), $\beta = 0$}} \\
20	\quad GAR-ours $\uparrow$   & 0.347 & 0.423 & 0.433 & 0.401 $\pm$ 0.047 \\
21	\quad PPL $\downarrow$       & 1.442 & 1.441 & 1.439 & 1.441 $\pm$ 0.002 \\
22	\midrule
23	\multicolumn{5}{@{}l}{\textit{Autoregressive (AR), $\beta = 3$}} \\
24	\quad GAR-ours $\uparrow$   & 0.593 & 0.590 & 0.605 & 0.596 $\pm$ 0.008 \\
25	\quad PPL $\downarrow$       & 1.564 & 1.607 & 1.587 & 1.586 $\pm$ 0.022 \\
26	\midrule
27	\multicolumn{5}{@{}l}{\textit{Autoregressive (AR), $\beta = 5$}} \\
28	\quad GAR-ours $\uparrow$   & 0.717 & 0.717 & 0.716 & 0.717 $\pm$ 0.001 \\
29	\quad PPL $\downarrow$       & 1.779 & 1.785 & 1.804 & 1.789 $\pm$ 0.013 \\
30	\bottomrule
31	\end{tabular}}
32	\end{table}
33	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "129ec2fc-9f75-4129-bc65-3bed4c4aa68f",
  "isSidechain": false,
  "promptId": "b0f005fa-c14f-47e1-bf29-f3925462c4b7",
  "type": "user",
  "uuid": "bb9e7ddf-ed0d-406b-9767-3c60990aad01",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/appendix_expansion/tab_perseed_ss.tex",
      "content": "% Per-seed detailed results for Scheduled Sampling (SS) — seeds 42, 123, 456\n% TF eval: N=200, T=3 (teacher-forced on held-out eval_200 set)\n% AR eval: N=50 gen-mode, beta=0/3/5 (from d048_final_ar)\n\\begin{table}[h]\n\\centering\n\\caption{Per-seed results for Scheduled Sampling (SS) on Qwen2.5-7B-Instruct.\nTF evaluation uses 200 held-out conversations; AR evaluation uses 50 model-generated conversations in free-form generation mode ($N_{\\text{valid}} \\approx 39$).}\n\\label{tab:perseed-ss}\n\\resizebox{\\columnwidth}{!}{\n\\begin{tabular}{@{}l ccc c@{}}\n\\toprule\n\\textbf{Metric} & \\textbf{Seed 42} & \\textbf{Seed 123} & \\textbf{Seed 456} & \\textbf{Mean $\\pm$ Std} \\\\\n\\midrule\n\\multicolumn{5}{@{}l}{\\textit{Teacher-Forced (TF)}} \\\\\n\\quad GAR-ours $\\uparrow$   & 0.502 & 0.554 & 0.496 & 0.517 $\\pm$ 0.032 \\\\\n\\quad GAR-Dongre $\\uparrow$ & 0.389 & 0.411 & 0.386 & 0.395 $\\pm$ 0.014 \\\\\n\\quad PPL $\\downarrow$       & 2.780 & 2.612 & 2.611 & 2.668 $\\pm$ 0.097 \\\\\n\\midrule\n\\multicolumn{5}{@{}l}{\\textit{Autoregressive (AR), $\\beta = 0$}} \\\\\n\\quad GAR-ours $\\uparrow$   & 0.347 & 0.423 & 0.433 & 0.401 $\\pm$ 0.047 \\\\\n\\quad PPL $\\downarrow$       & 1.442 & 1.441 & 1.439 & 1.441 $\\pm$ 0.002 \\\\\n\\midrule\n\\multicolumn{5}{@{}l}{\\textit{Autoregressive (AR), $\\beta = 3$}} \\\\\n\\quad GAR-ours $\\uparrow$   & 0.593 & 0.590 & 0.605 & 0.596 $\\pm$ 0.008 \\\\\n\\quad PPL $\\downarrow$       & 1.564 & 1.607 & 1.587 & 1.586 $\\pm$ 0.022 \\\\\n\\midrule\n\\multicolumn{5}{@{}l}{\\textit{Autoregressive (AR), $\\beta = 5$}} \\\\\n\\quad GAR-ours $\\uparrow$   & 0.717 & 0.717 & 0.716 & 0.717 $\\pm$ 0.001 \\\\\n\\quad PPL $\\downarrow$       & 1.779 & 1.785 & 1.804 & 1.789 $\\pm$ 0.013 \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n",
      "numLines": 33,
      "startLine": 1,
      "totalLines": 33
    }
  },
  "sourceToolAssistantUUID": "129ec2fc-9f75-4129-bc65-3bed4c4aa68f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921",
  "sessionId": "5d779602-0719-4d06-8bf9-fdd84990d5d0",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---


### Tool call

_source line 43 · 2026-05-25T20:34:26.538Z_

<details open><summary>🔧 Tool call — Read · `toolu_01MX75vx7QvF3mMcGmCyZmsR`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/appendix_expansion/tab_perseed_tg.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bb9e7ddf-ed0d-406b-9767-3c60990aad01",
  "isSidechain": false,
  "requestId": "req_011CbPvex7RH5bY93v4MHUSs",
  "type": "assistant",
  "uuid": "06c1e2fb-95e6-4ad5-a890-8b12b41967dd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921",
  "sessionId": "5d779602-0719-4d06-8bf9-fdd84990d5d0",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01946BiMqvn9RyjEosR4uPp7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2853,
      "cache_read_input_tokens": 39396,
      "output_tokens": 508,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2853,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 508,
          "cache_read_input_tokens": 39396,
          "cache_creation_input_tokens": 2853,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2853
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
  "lastPrompt": "[系统通知 — worker_done:worker_audit_appendix_tables_20260525T201208]: Worker worker_audit_appendix_tables_20260525T201208 已完成（status=done），请审查 Agent 的处理结果。",
  "leafUuid": "9e875b2b-7565-4aa4-aa4e-8a54c2033458",
  "sessionId": "5d779602-0719-4d06-8bf9-fdd84990d5d0"
}
```

---


### Runtime record

_source line 45_

```json
{
  "type": "ai-title",
  "aiTitle": "Review worker audit appendix tables completion",
  "sessionId": "5d779602-0719-4d06-8bf9-fdd84990d5d0"
}
```

---


### Assistant

_source line 46 · 2026-05-25T20:34:31.032Z_

<details><summary>Logged reasoning block</summary>

```text
Now let me read more appendix tables and the appendix itself, plus I need to check the registry for data to cross-verify.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9e875b2b-7565-4aa4-aa4e-8a54c2033458",
  "isSidechain": false,
  "requestId": "req_011CbPvfnJ6ikQYPUdK5K88d",
  "type": "assistant",
  "uuid": "f391a47e-98ea-40f9-95fc-151149dde039",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921",
  "sessionId": "5d779602-0719-4d06-8bf9-fdd84990d5d0",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WL3xxHtp9RP3RSkZaZAkys",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4584,
      "cache_read_input_tokens": 42249,
      "output_tokens": 543,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4584,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 543,
          "cache_read_input_tokens": 42249,
          "cache_creation_input_tokens": 4584,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4584
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

_source line 47 · 2026-05-25T20:34:33.396Z_

<details open><summary>🔧 Tool call — Read · `toolu_01VQZf6XxAjijZGXBPmpmeRt`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/appendix_expansion/tab_perturn_qwen.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f391a47e-98ea-40f9-95fc-151149dde039",
  "isSidechain": false,
  "requestId": "req_011CbPvfnJ6ikQYPUdK5K88d",
  "type": "assistant",
  "uuid": "993d3eed-cdf9-4938-8e24-e022dcf039a3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921",
  "sessionId": "5d779602-0719-4d06-8bf9-fdd84990d5d0",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WL3xxHtp9RP3RSkZaZAkys",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4584,
      "cache_read_input_tokens": 42249,
      "output_tokens": 543,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4584,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 543,
          "cache_read_input_tokens": 42249,
          "cache_creation_input_tokens": 4584,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4584
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

_source line 48 · 2026-05-25T20:34:33.403Z_

<details><summary>↩ Tool result · `toolu_01VQZf6XxAjijZGXBPmpmeRt`</summary>

```text
1	% Per-turn AR GAR-ours for Qwen2.5-7B-Instruct, 6-way comparison
2	% Source: d048_final_ar, beta=0, N=50 gen-mode, n_valid~39
3	% Only turns 1--5 shown (later turns have survivor bias from variable-length generation)
4	\begin{table}[t]
5	\centering
6	\caption{Per-turn autoregressive GAR-ours ($\beta{=}0$) on Qwen2.5-7B-Instruct across six training configurations. Values represent average GAR over ${\sim}39$ valid conversations in free-form generation mode.}
7	\label{tab:perturn-qwen}
8	\resizebox{\columnwidth}{!}{
9	\begin{tabular}{@{}l ccccc@{}}
10	\toprule
11	\textbf{Configuration} & \textbf{Turn 1} & \textbf{Turn 2} & \textbf{Turn 3} & \textbf{Turn 4} & \textbf{Turn 5} \\
12	\midrule
13	Base         & .085 & .032 & .021 & .013 & .004 \\
14	ThreadGate   & .130 & .073 & .059 & .043 & .066 \\
15	PCGrad       & .090 & .038 & .028 & .029 & .027 \\
16	UG           & .113 & .056 & .033 & .020 & .016 \\
17	LoRA-only    & .107 & .059 & .030 & .049 & .040 \\
18	SS           & \textbf{.458} & \textbf{.381} & \textbf{.344} & \textbf{.370} & \textbf{.365} \\
19	\bottomrule
20	\end{tabular}}
21	\end{table}
22	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "993d3eed-cdf9-4938-8e24-e022dcf039a3",
  "isSidechain": false,
  "promptId": "b0f005fa-c14f-47e1-bf29-f3925462c4b7",
  "type": "user",
  "uuid": "2f9d2515-a142-4061-ace2-383966259576",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/appendix_expansion/tab_perturn_qwen.tex",
      "content": "% Per-turn AR GAR-ours for Qwen2.5-7B-Instruct, 6-way comparison\n% Source: d048_final_ar, beta=0, N=50 gen-mode, n_valid~39\n% Only turns 1--5 shown (later turns have survivor bias from variable-length generation)\n\\begin{table}[t]\n\\centering\n\\caption{Per-turn autoregressive GAR-ours ($\\beta{=}0$) on Qwen2.5-7B-Instruct across six training configurations. Values represent average GAR over ${\\sim}39$ valid conversations in free-form generation mode.}\n\\label{tab:perturn-qwen}\n\\resizebox{\\columnwidth}{!}{\n\\begin{tabular}{@{}l ccccc@{}}\n\\toprule\n\\textbf{Configuration} & \\textbf{Turn 1} & \\textbf{Turn 2} & \\textbf{Turn 3} & \\textbf{Turn 4} & \\textbf{Turn 5} \\\\\n\\midrule\nBase         & .085 & .032 & .021 & .013 & .004 \\\\\nThreadGate   & .130 & .073 & .059 & .043 & .066 \\\\\nPCGrad       & .090 & .038 & .028 & .029 & .027 \\\\\nUG           & .113 & .056 & .033 & .020 & .016 \\\\\nLoRA-only    & .107 & .059 & .030 & .049 & .040 \\\\\nSS           & \\textbf{.458} & \\textbf{.381} & \\textbf{.344} & \\textbf{.370} & \\textbf{.365} \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n",
      "numLines": 22,
      "startLine": 1,
      "totalLines": 22
    }
  },
  "sourceToolAssistantUUID": "993d3eed-cdf9-4938-8e24-e022dcf039a3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921",
  "sessionId": "5d779602-0719-4d06-8bf9-fdd84990d5d0",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---


### Tool result

_source line 49 · 2026-05-25T20:34:36.611Z_

<details><summary>↩ Tool result · `toolu_01E4tzuFxnUzVZN277CXaPsQ`</summary>

```text
1	% Qwen2.5-1.5B cross-scale results
2	\begin{table}[t]
3	\centering
4	\footnotesize
5	\caption{Cross-scale validation on Qwen2.5-1.5B-Instruct. Phase~1 confirms the GAR decay pattern at smaller scale (79.8\% relative drop). Phase~2 shows TG improves AR at $\beta=0$ (unamplified, $p{=}0.005$) and $\beta=5$ (strong amplification, $p{<}0.001$), confirming the mechanism transfers across model sizes.}
6	\label{tab:qwen15b_results}
7	\resizebox{\columnwidth}{!}{
8	\begin{tabular}{@{}ll cc c@{}}
9	\toprule
10	\textbf{Phase} & \textbf{Metric} & \textbf{Base} & \textbf{TG} & \textbf{$p$-value} \\
11	\midrule
12	\multicolumn{5}{@{}l}{\textit{Phase 1: GAR diagnostic}} \\
13	\quad & Turn-1 GAR & 0.0336 & --- & --- \\
14	\quad & Mid-turn GAR & 0.0068 & --- & --- \\
15	\quad & Relative drop & 79.8\% & --- & --- \\
16	\midrule
17	\multicolumn{5}{@{}l}{\textit{Phase 2: TG training ($\beta$-amplified AR)}} \\
18	\quad & AR @ $\beta{=}0$ & 0.0167 {\scriptsize$\pm$0.005} & \textbf{0.0233} {\scriptsize$\pm$0.006} & 0.005$^{**}$ \\
19	\quad & AR @ $\beta{=}3$ & 0.1202 {\scriptsize$\pm$0.032} & 0.1143 {\scriptsize$\pm$0.019} & 0.815 \\
20	\quad & AR @ $\beta{=}5$ & 0.6571 {\scriptsize$\pm$0.020} & \textbf{0.7150} {\scriptsize$\pm$0.017} & $<$0.001$^{***}$ \\
21	\bottomrule
22	\end{tabular}}
23	\vspace{1mm}
24	\begin{flushleft}
25	\scriptsize
26	$\pm$ values are 95\% CI half-widths. Significance via Wilcoxon signed-rank test ($N{=}39$ paired conversations). Effect sizes: $r{=}0.447$ ($\beta{=}0$), $r{=}0.749$ ($\beta{=}5$).
27	\end{flushleft}
28	\end{table}
29	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "139919a5-4f01-430f-9a87-c39374d23f66",
  "isSidechain": false,
  "promptId": "b0f005fa-c14f-47e1-bf29-f3925462c4b7",
  "type": "user",
  "uuid": "dc5297ae-a4ab-40da-aa18-d51dfedbeba8",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/appendix_expansion/tab_qwen15b_results.tex",
      "content": "% Qwen2.5-1.5B cross-scale results\n\\begin{table}[t]\n\\centering\n\\footnotesize\n\\caption{Cross-scale validation on Qwen2.5-1.5B-Instruct. Phase~1 confirms the GAR decay pattern at smaller scale (79.8\\% relative drop). Phase~2 shows TG improves AR at $\\beta=0$ (unamplified, $p{=}0.005$) and $\\beta=5$ (strong amplification, $p{<}0.001$), confirming the mechanism transfers across model sizes.}\n\\label{tab:qwen15b_results}\n\\resizebox{\\columnwidth}{!}{\n\\begin{tabular}{@{}ll cc c@{}}\n\\toprule\n\\textbf{Phase} & \\textbf{Metric} & \\textbf{Base} & \\textbf{TG} & \\textbf{$p$-value} \\\\\n\\midrule\n\\multicolumn{5}{@{}l}{\\textit{Phase 1: GAR diagnostic}} \\\\\n\\quad & Turn-1 GAR & 0.0336 & --- & --- \\\\\n\\quad & Mid-turn GAR & 0.0068 & --- & --- \\\\\n\\quad & Relative drop & 79.8\\% & --- & --- \\\\\n\\midrule\n\\multicolumn{5}{@{}l}{\\textit{Phase 2: TG training ($\\beta$-amplified AR)}} \\\\\n\\quad & AR @ $\\beta{=}0$ & 0.0167 {\\scriptsize$\\pm$0.005} & \\textbf{0.0233} {\\scriptsize$\\pm$0.006} & 0.005$^{**}$ \\\\\n\\quad & AR @ $\\beta{=}3$ & 0.1202 {\\scriptsize$\\pm$0.032} & 0.1143 {\\scriptsize$\\pm$0.019} & 0.815 \\\\\n\\quad & AR @ $\\beta{=}5$ & 0.6571 {\\scriptsize$\\pm$0.020} & \\textbf{0.7150} {\\scriptsize$\\pm$0.017} & $<$0.001$^{***}$ \\\\\n\\bottomrule\n\\end{tabular}}\n\\vspace{1mm}\n\\begin{flushleft}\n\\scriptsize\n$\\pm$ values are 95\\% CI half-widths. Significance via Wilcoxon signed-rank test ($N{=}39$ paired conversations). Effect sizes: $r{=}0.447$ ($\\beta{=}0$), $r{=}0.749$ ($\\beta{=}5$).\n\\end{flushleft}\n\\end{table}\n",
      "numLines": 29,
      "startLine": 1,
      "totalLines": 29
    }
  },
  "sourceToolAssistantUUID": "139919a5-4f01-430f-9a87-c39374d23f66",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921",
  "sessionId": "5d779602-0719-4d06-8bf9-fdd84990d5d0",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---


### Tool call

_source line 50 · 2026-05-25T20:34:33.912Z_

<details open><summary>🔧 Tool call — Read · `toolu_01NMujALg6mkF41yxGGCt2ya`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/appendix_expansion/tab_perturn_llama.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2f9d2515-a142-4061-ace2-383966259576",
  "isSidechain": false,
  "requestId": "req_011CbPvfnJ6ikQYPUdK5K88d",
  "type": "assistant",
  "uuid": "24e1fb72-d9f7-4d82-a102-89389dc1a0c7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921",
  "sessionId": "5d779602-0719-4d06-8bf9-fdd84990d5d0",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WL3xxHtp9RP3RSkZaZAkys",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4584,
      "cache_read_input_tokens": 42249,
      "output_tokens": 543,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4584,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 543,
          "cache_read_input_tokens": 42249,
          "cache_creation_input_tokens": 4584,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4584
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

_source line 51 · 2026-05-25T20:34:33.918Z_

<details><summary>↩ Tool result · `toolu_01NMujALg6mkF41yxGGCt2ya`</summary>

```text
1	% Per-turn AR GAR-ours for Llama-3.1-8B-Instruct
2	% Panel (a): N=20, T=4 (eval_llama_ar_n20) — reliable estimates
3	% Panel (b): Base only, N=5, T=10 (llama_phase1_gar_diag) — decay profile
4	\begin{table*}[t]
5	\centering
6	\caption{Per-turn autoregressive GAR-ours ($\beta{=}0$) on Llama-3.1-8B-Instruct.
7	(a)~Three-way comparison using $N{=}20$ conversations ($T{=}4$ turns).
8	(b)~Base model decay profile ($N{=}5$, $T{=}10$).}
9	\label{tab:perturn-llama}
10	\small
11	\begin{subtable}[t]{0.48\textwidth}
12	\centering
13	\caption{$N{=}20$, $T{=}4$}
14	\renewcommand{\arraystretch}{1.3}
15	\begin{tabular}{@{}l cccc@{}}
16	\toprule
17	\textbf{Config.} & \textbf{T1} & \textbf{T2} & \textbf{T3} & \textbf{T4} \\
18	\midrule
19	Base      & .028 & .013 & .009 & .008 \\
20	TG        & .041 & .042 & .049 & .038 \\
21	LoRA-only & .033 & .049 & .025 & .031 \\
22	\bottomrule
23	\end{tabular}
24	\end{subtable}
25	\hfill
26	\begin{subtable}[t]{0.38\textwidth}
27	\centering
28	\caption{Base decay ($N{=}5$, $T{=}10$)}
29	\begin{tabular}{@{}cc@{}}
30	\toprule
31	\textbf{Turn} & \textbf{GAR-ours} \\
32	\midrule
33	1  & .026 \\
34	2  & .018 \\
35	3  & .009 \\
36	4  & .006 \\
37	5  & .006 \\
38	6  & .004 \\
39	7  & .004 \\
40	8  & .004 \\
41	9  & .005 \\
42	10 & .003 \\
43	\bottomrule
44	\end{tabular}
45	\end{subtable}
46	\end{table*}
47	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "24e1fb72-d9f7-4d82-a102-89389dc1a0c7",
  "isSidechain": false,
  "promptId": "b0f005fa-c14f-47e1-bf29-f3925462c4b7",
  "type": "user",
  "uuid": "0b7acd49-ae9c-4a52-8841-ef26bde32b4f",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/appendix_expansion/tab_perturn_llama.tex",
      "content": "% Per-turn AR GAR-ours for Llama-3.1-8B-Instruct\n% Panel (a): N=20, T=4 (eval_llama_ar_n20) — reliable estimates\n% Panel (b): Base only, N=5, T=10 (llama_phase1_gar_diag) — decay profile\n\\begin{table*}[t]\n\\centering\n\\caption{Per-turn autoregressive GAR-ours ($\\beta{=}0$) on Llama-3.1-8B-Instruct.\n(a)~Three-way comparison using $N{=}20$ conversations ($T{=}4$ turns).\n(b)~Base model decay profile ($N{=}5$, $T{=}10$).}\n\\label{tab:perturn-llama}\n\\small\n\\begin{subtable}[t]{0.48\\textwidth}\n\\centering\n\\caption{$N{=}20$, $T{=}4$}\n\\renewcommand{\\arraystretch}{1.3}\n\\begin{tabular}{@{}l cccc@{}}\n\\toprule\n\\textbf{Config.} & \\textbf{T1} & \\textbf{T2} & \\textbf{T3} & \\textbf{T4} \\\\\n\\midrule\nBase      & .028 & .013 & .009 & .008 \\\\\nTG        & .041 & .042 & .049 & .038 \\\\\nLoRA-only & .033 & .049 & .025 & .031 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{subtable}\n\\hfill\n\\begin{subtable}[t]{0.38\\textwidth}\n\\centering\n\\caption{Base decay ($N{=}5$, $T{=}10$)}\n\\begin{tabular}{@{}cc@{}}\n\\toprule\n\\textbf{Turn} & \\textbf{GAR-ours} \\\\\n\\midrule\n1  & .026 \\\\\n2  & .018 \\\\\n3  & .009 \\\\\n4  & .006 \\\\\n5  & .006 \\\\\n6  & .004 \\\\\n7  & .004 \\\\\n8  & .004 \\\\\n9  & .005 \\\\\n10 & .003 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{subtable}\n\\end{table*}\n",
      "numLines": 47,
      "startLine": 1,
      "totalLines": 47
    }
  },
  "sourceToolAssistantUUID": "24e1fb72-d9f7-4d82-a102-89389dc1a0c7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921",
  "sessionId": "5d779602-0719-4d06-8bf9-fdd84990d5d0",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---


### Tool call

_source line 52 · 2026-05-25T20:34:34.893Z_

<details open><summary>🔧 Tool call — Read · `toolu_01CX9YZe8YCT27pdbBJLPwwC`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/appendix_expansion/tab_crossmodel_detail.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0b7acd49-ae9c-4a52-8841-ef26bde32b4f",
  "isSidechain": false,
  "requestId": "req_011CbPvfnJ6ikQYPUdK5K88d",
  "type": "assistant",
  "uuid": "f63c06d8-12eb-4226-927c-8a08e36263df",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921",
  "sessionId": "5d779602-0719-4d06-8bf9-fdd84990d5d0",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WL3xxHtp9RP3RSkZaZAkys",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4584,
      "cache_read_input_tokens": 42249,
      "output_tokens": 543,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4584,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 543,
          "cache_read_input_tokens": 42249,
          "cache_creation_input_tokens": 4584,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4584
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

_source line 53 · 2026-05-25T20:34:34.897Z_

<details><summary>↩ Tool result · `toolu_01CX9YZe8YCT27pdbBJLPwwC`</summary>

```text
1	% Cross-model detailed comparison: Qwen2.5-7B-Instruct vs Llama-3.1-8B-Instruct
2	% Conditions shared by both models: Base, ThreadGate, LoRA-only
3	% Qwen TF: N=200 held-out; Qwen AR: d048_final_ar N=50 gen beta=0
4	% Llama TF: N=50 held-out T=4; Llama AR: eval_llama_ar_n20 N=20 T=4
5	% Llama SS: p1_llama_ss_eval (epoch_1 checkpoint, N=50)
6	\begin{table*}[t]
7	\centering
8	\caption{Cross-model comparison of goal-adherence metrics on Qwen2.5-7B-Instruct and Llama-3.1-8B-Instruct.
9	Gap ratio = TF GAR / AR GAR; lower is better (less exposure bias).
10	Qwen AR uses $N{=}50$ gen-mode evaluation; Llama AR uses $N{=}20$, $T{=}4$ (SS: $N{=}50$).
11	Llama AR GAR and gaps are mean-based; median-based TG gap is 27$\times$ (\S\ref{subsec:cross-model}).}
12	\label{tab:crossmodel-detail}
13	\small
14	\begin{tabular}{@{}ll ccccc@{}}
15	\toprule
16	\textbf{Model} & \textbf{Condition} & \textbf{TF GAR}$\uparrow$ & \textbf{AR GAR}$\uparrow$ & \textbf{TF PPL}$\downarrow$ & \textbf{AR PPL}$\downarrow$ & \textbf{Gap}$\downarrow$ \\
17	\midrule
18	\multirow{4}{*}{Qwen-7B}
19	  & Base      & 0.013 & 0.019 & 4.34 & 1.447 & 0.7$\times$ \\
20	  & TG        & 0.504 & 0.064 & 2.78 & 1.432 & 7.9$\times$ \\
21	  & LoRA-only & 0.498 & 0.037 & 2.78 & 1.431 & 13.5$\times$ \\
22	  & \textbf{SS} & 0.498 & \textbf{0.401} & 2.78 & 1.441 & \textbf{1.2$\times$} \\
23	\midrule
24	\multirow{4}{*}{Llama-8B}
25	  & Base      & 0.017 & 0.009 & 3.45 & 1.293 & 1.9$\times$ \\
26	  & TG        & 0.484 & 0.043 & 2.57 & 1.437 & 11.2$\times$ \\
27	  & LoRA-only & 0.481 & 0.028 & 2.60 & 1.419 & 17.2$\times$ \\
28	  & \textbf{SS} & 0.477 & \textbf{0.166} & 2.82 & 1.370 & \textbf{2.9$\times$} \\
29	\bottomrule
30	\end{tabular}
31	\end{table*}
32	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f63c06d8-12eb-4226-927c-8a08e36263df",
  "isSidechain": false,
  "promptId": "b0f005fa-c14f-47e1-bf29-f3925462c4b7",
  "type": "user",
  "uuid": "a5fbe058-7b70-4d16-951f-ad0b58a4a9fd",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/appendix_expansion/tab_crossmodel_detail.tex",
      "content": "% Cross-model detailed comparison: Qwen2.5-7B-Instruct vs Llama-3.1-8B-Instruct\n% Conditions shared by both models: Base, ThreadGate, LoRA-only\n% Qwen TF: N=200 held-out; Qwen AR: d048_final_ar N=50 gen beta=0\n% Llama TF: N=50 held-out T=4; Llama AR: eval_llama_ar_n20 N=20 T=4\n% Llama SS: p1_llama_ss_eval (epoch_1 checkpoint, N=50)\n\\begin{table*}[t]\n\\centering\n\\caption{Cross-model comparison of goal-adherence metrics on Qwen2.5-7B-Instruct and Llama-3.1-8B-Instruct.\nGap ratio = TF GAR / AR GAR; lower is better (less exposure bias).\nQwen AR uses $N{=}50$ gen-mode evaluation; Llama AR uses $N{=}20$, $T{=}4$ (SS: $N{=}50$).\nLlama AR GAR and gaps are mean-based; median-based TG gap is 27$\\times$ (\\S\\ref{subsec:cross-model}).}\n\\label{tab:crossmodel-detail}\n\\small\n\\begin{tabular}{@{}ll ccccc@{}}\n\\toprule\n\\textbf{Model} & \\textbf{Condition} & \\textbf{TF GAR}$\\uparrow$ & \\textbf{AR GAR}$\\uparrow$ & \\textbf{TF PPL}$\\downarrow$ & \\textbf{AR PPL}$\\downarrow$ & \\textbf{Gap}$\\downarrow$ \\\\\n\\midrule\n\\multirow{4}{*}{Qwen-7B}\n  & Base      & 0.013 & 0.019 & 4.34 & 1.447 & 0.7$\\times$ \\\\\n  & TG        & 0.504 & 0.064 & 2.78 & 1.432 & 7.9$\\times$ \\\\\n  & LoRA-only & 0.498 & 0.037 & 2.78 & 1.431 & 13.5$\\times$ \\\\\n  & \\textbf{SS} & 0.498 & \\textbf{0.401} & 2.78 & 1.441 & \\textbf{1.2$\\times$} \\\\\n\\midrule\n\\multirow{4}{*}{Llama-8B}\n  & Base      & 0.017 & 0.009 & 3.45 & 1.293 & 1.9$\\times$ \\\\\n  & TG        & 0.484 & 0.043 & 2.57 & 1.437 & 11.2$\\times$ \\\\\n  & LoRA-only & 0.481 & 0.028 & 2.60 & 1.419 & 17.2$\\times$ \\\\\n  & \\textbf{SS} & 0.477 & \\textbf{0.166} & 2.82 & 1.370 & \\textbf{2.9$\\times$} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n",
      "numLines": 32,
      "startLine": 1,
      "totalLines": 32
    }
  },
  "sourceToolAssistantUUID": "f63c06d8-12eb-4226-927c-8a08e36263df",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921",
  "sessionId": "5d779602-0719-4d06-8bf9-fdd84990d5d0",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---


### Tool call

_source line 54 · 2026-05-25T20:34:35.371Z_

<details open><summary>🔧 Tool call — Read · `toolu_017RPyh3b7ARHW8EPww5sJP7`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/appendix_expansion/tab_mmlu_detail.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a5fbe058-7b70-4d16-951f-ad0b58a4a9fd",
  "isSidechain": false,
  "requestId": "req_011CbPvfnJ6ikQYPUdK5K88d",
  "type": "assistant",
  "uuid": "ab88c81f-1bfc-4d83-b9dc-8900a18ad599",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921",
  "sessionId": "5d779602-0719-4d06-8bf9-fdd84990d5d0",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WL3xxHtp9RP3RSkZaZAkys",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4584,
      "cache_read_input_tokens": 42249,
      "output_tokens": 543,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4584,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 543,
          "cache_read_input_tokens": 42249,
          "cache_creation_input_tokens": 4584,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4584
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

_source line 55 · 2026-05-25T20:34:35.375Z_

<details><summary>↩ Tool result · `toolu_017RPyh3b7ARHW8EPww5sJP7`</summary>

```text
1	% MMLU per-category quality preservation table
2	\begin{table}[t]
3	\centering
4	\footnotesize
5	\caption{MMLU accuracy (\%) by category across training conditions. All models are Qwen2.5-7B-Instruct with LoRA adapters evaluated on the full 57-subject MMLU benchmark (14{,}042 questions). $\Delta$ denotes deviation from Base.}
6	\label{tab:mmlu_detail}
7	\resizebox{\columnwidth}{!}{
8	\begin{tabular}{@{}l cccccc@{}}
9	\toprule
10	\textbf{Category} & \textbf{Base} & \textbf{TG} & \textbf{PCGrad} & \textbf{SS} & \textbf{LoRA-only} & \textbf{UG} \\
11	\midrule
12	STEM           & 70.69 & 69.20 & 69.55 & 69.97 & 70.03 & 69.65 \\
13	Social Sciences & 77.28 & 76.92 & 76.79 & 76.83 & 77.08 & 77.02 \\
14	Humanities     & 83.95 & 83.33 & 84.08 & 83.39 & 83.62 & 83.95 \\
15	Other          & 68.25 & 67.59 & 68.12 & 67.95 & 67.06 & 66.80 \\
16	\midrule
17	\textbf{Overall} & \textbf{74.23} & 73.47 & 73.86 & 73.75 & 73.57 & 73.46 \\
18	$\Delta$ & --- & $-$0.76 & $-$0.37 & $-$0.48 & $-$0.66 & $-$0.77 \\
19	\bottomrule
20	\end{tabular}}
21	\end{table}
22	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ab88c81f-1bfc-4d83-b9dc-8900a18ad599",
  "isSidechain": false,
  "promptId": "b0f005fa-c14f-47e1-bf29-f3925462c4b7",
  "type": "user",
  "uuid": "ab313cb6-7284-4710-94b3-69e9f56e6e93",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/appendix_expansion/tab_mmlu_detail.tex",
      "content": "% MMLU per-category quality preservation table\n\\begin{table}[t]\n\\centering\n\\footnotesize\n\\caption{MMLU accuracy (\\%) by category across training conditions. All models are Qwen2.5-7B-Instruct with LoRA adapters evaluated on the full 57-subject MMLU benchmark (14{,}042 questions). $\\Delta$ denotes deviation from Base.}\n\\label{tab:mmlu_detail}\n\\resizebox{\\columnwidth}{!}{\n\\begin{tabular}{@{}l cccccc@{}}\n\\toprule\n\\textbf{Category} & \\textbf{Base} & \\textbf{TG} & \\textbf{PCGrad} & \\textbf{SS} & \\textbf{LoRA-only} & \\textbf{UG} \\\\\n\\midrule\nSTEM           & 70.69 & 69.20 & 69.55 & 69.97 & 70.03 & 69.65 \\\\\nSocial Sciences & 77.28 & 76.92 & 76.79 & 76.83 & 77.08 & 77.02 \\\\\nHumanities     & 83.95 & 83.33 & 84.08 & 83.39 & 83.62 & 83.95 \\\\\nOther          & 68.25 & 67.59 & 68.12 & 67.95 & 67.06 & 66.80 \\\\\n\\midrule\n\\textbf{Overall} & \\textbf{74.23} & 73.47 & 73.86 & 73.75 & 73.57 & 73.46 \\\\\n$\\Delta$ & --- & $-$0.76 & $-$0.37 & $-$0.48 & $-$0.66 & $-$0.77 \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n",
      "numLines": 22,
      "startLine": 1,
      "totalLines": 22
    }
  },
  "sourceToolAssistantUUID": "ab88c81f-1bfc-4d83-b9dc-8900a18ad599",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921",
  "sessionId": "5d779602-0719-4d06-8bf9-fdd84990d5d0",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---


### Tool call

_source line 56 · 2026-05-25T20:34:35.851Z_

<details open><summary>🔧 Tool call — Read · `toolu_01U4qpBkTfBe3szVWP4dtWmn`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/appendix_expansion/tab_dataset_stats.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ab313cb6-7284-4710-94b3-69e9f56e6e93",
  "isSidechain": false,
  "requestId": "req_011CbPvfnJ6ikQYPUdK5K88d",
  "type": "assistant",
  "uuid": "18504a1f-a4b9-454f-963b-85f81c686b9f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921",
  "sessionId": "5d779602-0719-4d06-8bf9-fdd84990d5d0",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WL3xxHtp9RP3RSkZaZAkys",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4584,
      "cache_read_input_tokens": 42249,
      "output_tokens": 543,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4584,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 543,
          "cache_read_input_tokens": 42249,
          "cache_creation_input_tokens": 4584,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4584
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

_source line 57 · 2026-05-25T20:34:35.855Z_

<details><summary>↩ Tool result · `toolu_01U4qpBkTfBe3szVWP4dtWmn`</summary>

```text
1	% Dataset statistics table
2	\begin{table}[t]
3	\centering
4	\small
5	\caption{Dataset statistics. Training and evaluation data are sampled from UltraChat-200K \texttt{train\_sft} split~\citep{ding2023ultrachat}. All conversations contain $\geq 5$ assistant turns.}
6	\label{tab:dataset_stats}
7	\begin{tabular}{@{}lr@{}}
8	\toprule
9	\textbf{Statistic} & \textbf{Value} \\
10	\midrule
11	\multicolumn{2}{@{}l}{\textit{Source}} \\
12	\quad Total conversations & 207{,}865 \\
13	\quad After $\geq 5$ turn filter & 17{,}302 \\
14	\midrule
15	\multicolumn{2}{@{}l}{\textit{Splits}} \\
16	\quad Training & 8{,}000 \\
17	\quad Held-out AR eval & 50 \\
18	\quad IID GAR diagnostic & 50 \\
19	\quad Instruction retention & 200 \\
20	\midrule
21	\multicolumn{2}{@{}l}{\textit{Conversation structure}} \\
22	\quad Avg.\ assistant turns & 5.6 \\
23	\quad Min / Max turns & 5 / 7 \\
24	\bottomrule
25	\end{tabular}
26	\end{table}
27	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "18504a1f-a4b9-454f-963b-85f81c686b9f",
  "isSidechain": false,
  "promptId": "b0f005fa-c14f-47e1-bf29-f3925462c4b7",
  "type": "user",
  "uuid": "250c16f9-2d89-4c4c-8cf2-5d2ed980a78e",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/appendix_expansion/tab_dataset_stats.tex",
      "content": "% Dataset statistics table\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Dataset statistics. Training and evaluation data are sampled from UltraChat-200K \\texttt{train\\_sft} split~\\citep{ding2023ultrachat}. All conversations contain $\\geq 5$ assistant turns.}\n\\label{tab:dataset_stats}\n\\begin{tabular}{@{}lr@{}}\n\\toprule\n\\textbf{Statistic} & \\textbf{Value} \\\\\n\\midrule\n\\multicolumn{2}{@{}l}{\\textit{Source}} \\\\\n\\quad Total conversations & 207{,}865 \\\\\n\\quad After $\\geq 5$ turn filter & 17{,}302 \\\\\n\\midrule\n\\multicolumn{2}{@{}l}{\\textit{Splits}} \\\\\n\\quad Training & 8{,}000 \\\\\n\\quad Held-out AR eval & 50 \\\\\n\\quad IID GAR diagnostic & 50 \\\\\n\\quad Instruction retention & 200 \\\\\n\\midrule\n\\multicolumn{2}{@{}l}{\\textit{Conversation structure}} \\\\\n\\quad Avg.\\ assistant turns & 5.6 \\\\\n\\quad Min / Max turns & 5 / 7 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n",
      "numLines": 27,
      "startLine": 1,
      "totalLines": 27
    }
  },
  "sourceToolAssistantUUID": "18504a1f-a4b9-454f-963b-85f81c686b9f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921",
  "sessionId": "5d779602-0719-4d06-8bf9-fdd84990d5d0",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---


### Tool call

_source line 58 · 2026-05-25T20:34:36.607Z_

<details open><summary>🔧 Tool call — Read · `toolu_01E4tzuFxnUzVZN277CXaPsQ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/appendix_expansion/tab_qwen15b_results.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "250c16f9-2d89-4c4c-8cf2-5d2ed980a78e",
  "isSidechain": false,
  "requestId": "req_011CbPvfnJ6ikQYPUdK5K88d",
  "type": "assistant",
  "uuid": "139919a5-4f01-430f-9a87-c39374d23f66",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921",
  "sessionId": "5d779602-0719-4d06-8bf9-fdd84990d5d0",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WL3xxHtp9RP3RSkZaZAkys",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4584,
      "cache_read_input_tokens": 42249,
      "output_tokens": 543,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4584,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 543,
          "cache_read_input_tokens": 42249,
          "cache_creation_input_tokens": 4584,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4584
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

_source line 59 · 2026-05-25T20:34:36.671Z_

```json
{
  "parentUuid": "dc5297ae-a4ab-40da-aa18-d51dfedbeba8",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "b9d99153-4433-4c69-b568-d1de3e56cc07",
  "timestamp": "2026-05-25T20:34:36.671Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921",
  "sessionId": "5d779602-0719-4d06-8bf9-fdd84990d5d0",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---


### Runtime record

_source line 60_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[系统通知 — worker_done:worker_audit_appendix_tables_20260525T201208]: Worker worker_audit_appendix_tables_20260525T201208 已完成（status=done），请审查 Agent 的处理结果。",
  "leafUuid": "b9d99153-4433-4c69-b568-d1de3e56cc07",
  "sessionId": "5d779602-0719-4d06-8bf9-fdd84990d5d0"
}
```

---


### Runtime record

_source line 61_

```json
{
  "type": "ai-title",
  "aiTitle": "Review worker audit appendix tables completion",
  "sessionId": "5d779602-0719-4d06-8bf9-fdd84990d5d0"
}
```

---


### Assistant

_source line 62 · 2026-05-25T20:34:49.823Z_

<details><summary>Logged reasoning block</summary>

```text
Now let me read the appendix.tex to understand the full structure, and also cross-reference with the registry to verify the numbers in the tables.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b9d99153-4433-4c69-b568-d1de3e56cc07",
  "isSidechain": false,
  "requestId": "req_011CbPvgXBnW4DEqiLfHCB8g",
  "type": "assistant",
  "uuid": "aeb95e60-2c6d-4de9-9cb1-df3d778fe916",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921",
  "sessionId": "5d779602-0719-4d06-8bf9-fdd84990d5d0",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015qPDBZVNPxWRyoTde5zCEQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4689,
      "cache_read_input_tokens": 46833,
      "output_tokens": 309,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4689,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 309,
          "cache_read_input_tokens": 46833,
          "cache_creation_input_tokens": 4689,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4689
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

_source line 63 · 2026-05-25T20:34:50.786Z_

现在我需要读取附录正文和 registry 中的相关实验数据来交叉验证表格中的数字。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "aeb95e60-2c6d-4de9-9cb1-df3d778fe916",
  "isSidechain": false,
  "requestId": "req_011CbPvgXBnW4DEqiLfHCB8g",
  "type": "assistant",
  "uuid": "a90c9f78-9441-4a61-9d7e-78012be1d67e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921",
  "sessionId": "5d779602-0719-4d06-8bf9-fdd84990d5d0",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015qPDBZVNPxWRyoTde5zCEQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4689,
      "cache_read_input_tokens": 46833,
      "output_tokens": 309,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4689,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 309,
          "cache_read_input_tokens": 46833,
          "cache_creation_input_tokens": 4689,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4689
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

_source line 64 · 2026-05-25T20:34:52.666Z_

<details open><summary>🔧 Tool call — Read · `toolu_01VEPDAgjXKxwwDoaYJgbA7e`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex",
  "limit": 200
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a90c9f78-9441-4a61-9d7e-78012be1d67e",
  "isSidechain": false,
  "requestId": "req_011CbPvgXBnW4DEqiLfHCB8g",
  "type": "assistant",
  "uuid": "593edf02-76ca-46a3-8f5e-8d011c2655f8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921",
  "sessionId": "5d779602-0719-4d06-8bf9-fdd84990d5d0",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015qPDBZVNPxWRyoTde5zCEQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4689,
      "cache_read_input_tokens": 46833,
      "output_tokens": 309,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4689,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 309,
          "cache_read_input_tokens": 46833,
          "cache_creation_input_tokens": 4689,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4689
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

_source line 65 · 2026-05-25T20:34:52.671Z_

<details><summary>↩ Tool result · `toolu_01VEPDAgjXKxwwDoaYJgbA7e`</summary>

```text
1	\section{Training Configuration}\label{sec:appendix-hyper}
2	
3	Table~\ref{tab:hyperparams} lists the full training configuration shared across all fine-tuned variants. ThreadGate gate parameters receive a $10\times$ learning rate multiplier and are initialized with bias 1.5 ($\sigma(1.5) \approx 0.82$); the gate MLP adds ${\sim}$57K parameters per variant ($<$0.001\% of 7B). The scheduled sampling variant (v8b) linearly increases the model-generated context ratio from 0 to 0.5 over 3 epochs (29.7--37.1\% effective usage due to per-sample Bernoulli sampling). All experiments were conducted on a single NVIDIA RTX PRO 6000 Blackwell Server Edition GPU (96\,GB VRAM), requiring 6--8 hours per variant.
4	
5	\begin{table}[t]
6	\centering\small
7	\caption{Training hyperparameters for all fine-tuned variants. Entries marked $\dagger$ apply only to ThreadGate and its ablations.}
8	\label{tab:hyperparams}
9	\begin{tabular}{l@{\hspace{8pt}}l}
10	\toprule
11	\textbf{Parameter} & \textbf{Value} \\
12	\midrule
13	Base model & Qwen-2.5-7B-Instruct \\
14	LoRA rank / $\alpha$ & 16 / 32 \\
15	LoRA targets & \texttt{q\_proj}, \texttt{v\_proj} \\
16	Optimizer & AdamW ($\beta_1$\!=\!0.9, $\beta_2$\!=\!0.999) \\
17	Learning rate & $2 \times 10^{-4}$ \\
18	Gate LR mult.$^\dagger$ & $10\times$ \\
19	Batch / grad accum & 1 / 8 (eff.\ 8) \\
20	Epochs & 3 \\
21	Max seq length & 2048 \\
22	Training data & 8K UltraChat convs \\
23	Seed & 42 (+123 for TG, SS) \\
24	$\lambda_\text{GAR}$/$\lambda_\text{div}$ & 1.0 / 1.0 \\
25	GAR target $\tau$ & 0.5 \\
26	Gate init bias$^\dagger$ & 1.5 ($\sigma\!\approx\!0.82$) \\
27	Gate hidden dim$^\dagger$ & 64 \\
28	Turn embed dim$^\dagger$ & 16 \\
29	GPU & RTX PRO 6000 (96\,GB) \\
30	Training time & 6--8 h / variant \\
31	\bottomrule
32	\end{tabular}
33	\end{table}
34	
35	\section{Loss Formulation Search}\label{sec:appendix-loss}
36	
37	The final MSE + gate diversity loss (\S\ref{sec:loss}) emerged from seven iterations spanning four loss families. Table~\ref{tab:loss-iterations} summarizes the progression. The search was motivated by a consistent failure mode: naive formulations either collapse to trivial solutions (cumulative losses) or drive gates toward identity (maximize-family losses). We describe each family below.
38	
39	\paragraph{Cumulative losses (v1--v2).} These losses accumulate GAR contributions across layers, rewarding monotonically increasing attention. v1 collapsed because once the cumulative GAR exceeded the threshold, the loss gradient vanished and gates froze. v2 added an $\varepsilon$-stabilization term to the cumulative product, but numerical instability from the product of 28 per-layer terms dominated, and training followed the same trajectory.
40	
41	\paragraph{Maximize losses (v3--v5).} These losses directly maximize mean GAR ($-\text{mean}(\text{GAR})$). The unbounded objective rewards full pass-through ($g \to 1.0$), collapsing gate diversity (std $<$ 0.025). At $\lambda$=2 (v3), gates froze within 100 steps; at $\lambda$=10 (v3b), convergence to identity accelerated; at $\lambda$=1 (v5), rebalancing delayed but did not prevent the same degenerate solution.
42	
43	\paragraph{Smooth saturation (v6).} This bounded the reward using a saturating function, intended to prevent the unbounded growth of maximize losses. In practice, the loss landscape remained monotonic in $g$, and training followed the same terminal trajectory as the maximize family, only more slowly.
44	
45	\paragraph{MSE + gate diversity (v7).} The MSE formulation provides bidirectional pressure: GAR above $\tau$ incurs the same penalty as GAR below $\tau$, preventing the runaway optimization of maximize losses. The gate diversity regularizer ($\mathcal{L}_\text{div}$) enforces a minimum standard deviation across per-layer gate values, preventing all gates from collapsing to a uniform value. This combination is the only one that achieved stable convergence (GAR-ours = 0.50, PPL = 2.78).
46	
47	\begin{table*}[t]
48	\centering\footnotesize
49	\caption{Loss formulation iterations on Qwen-2.5-7B-Instruct. GAR-ours (teacher-forced) and PPL are reported only for the converged configuration (v7).}
50	\label{tab:loss-iterations}
51	\begin{tabular}{l l l p{5.8cm} c c}
52	\toprule
53	 & \textbf{Loss Family} & \textbf{Status} & \textbf{Failure Mechanism} & \textbf{GAR} & \textbf{PPL} \\
54	\midrule
55	v1  & Cumulative            & \texttimes~GAR loss $\to$ 0     & GAR loss collapses to zero once threshold is reached; gate gradients vanish at equilibrium & ---  & ---  \\
56	v2  & Cumulative + $\varepsilon$ & \texttimes~same trajectory & Numerical instability from cumulative product; $\varepsilon$-stabilization insufficient & ---  & ---  \\
57	v3  & Maximize ($\lambda$=2)  & \texttimes~gate frozen        & Unbounded reward drives gates toward identity (all-pass); no layer selectivity & ---  & ---  \\
58	v3b & Maximize ($\lambda$=10) & \texttimes~identity collapse   & Higher $\lambda$ accelerates convergence to same degenerate identity solution & ---  & ---  \\
59	v5  & Maximize ($\lambda$=1)  & \texttimes~identity collapse   & Rebalancing delays but does not prevent identity collapse & ---  & ---  \\
60	v6  & Smooth saturation       & \texttimes~identity collapse   & Monotonic reward identical to maximize in practice; boundedness slows but does not alter terminal trajectory & ---  & ---  \\
61	v7  & MSE + gate div          & \checkmark~\textbf{converged}  & \textbf{Bidirectional penalty prevents identity collapse; gate diversity regularizer enforces layer selectivity} & 0.50 & 2.78 \\
62	\bottomrule
63	\end{tabular}
64	\end{table*}
65	
66	\section{Instruction Retention Details}\label{sec:appendix-ir}
67	
68	To evaluate whether GAR improvements translate to downstream task performance, we test instruction retention across 18 system-prompt constraint types using the ThreadGate checkpoint with $\beta$\,=\,3 steering on $N$\,=\,200 held-out conversations. Each constraint type requires the model to follow a specific instruction embedded in the system prompt (e.g., ``always respond in bullet points'', ``never use the word X'', ``include a summary at the end''). This evaluation bridges the gap between our attention-level metric (GAR) and observable model behavior.
69	
70	\paragraph{Evaluation protocol.} For each conversation, we inject a constraint into the system prompt and evaluate compliance across all assistant turns. A turn is compliant if it satisfies the constraint according to rule-based checkers (for format, count, and position constraints) or GPT-4-based evaluation (for content constraints, which require semantic judgment). We use the same 18 constraint types across all conversations, yielding $N$\,=\,54 paired evaluations (18 types $\times$ 3 conversations per type) for the McNemar analysis.
71	
72	\paragraph{Per-category results.} Table~\ref{tab:ir-results} reports per-category compliance rates. Content constraints---which require attending to and recalling specific system-prompt instructions across turns---show the largest improvement (+23.8\,pp), consistent with GAR measuring attention to goal tokens. This category includes constraints like ``mention X in every response'' and ``always reference the original topic,'' which require sustained attention to the system prompt. Position constraints (e.g., ``start each response with Y'') show a modest improvement (+6.7\,pp), as they partially depend on goal-token attention. Format (e.g., ``use bullet points'') and count constraints (e.g., ``exactly 3 sentences'') show no change, consistent with these being procedural patterns that are cached in the model's generation routine rather than requiring ongoing attention to the system prompt.
73	
74	\paragraph{Correlation analysis.} The GAR-compliance correlation ($r$\,=\,0.200, $p$\,=\,0.007) is statistically significant but modest, suggesting that attention to goal tokens is one of several factors in instruction compliance. Other factors likely include the model's procedural memory for format constraints, the specificity of the constraint (vague constraints are harder regardless of attention), and the interaction between constraint type and conversation topic. McNemar's test ($p$\,=\,0.077) is marginally significant for the overall compliance improvement, reflecting the small sample size (18 constraint types). These results are exploratory and pending multi-model confirmation.
75	
76	Figure~\ref{fig:ir-bar} visualizes the per-category breakdown.
77	
78	\begin{figure}[t]
79	  \centering
80	  \includegraphics[width=\columnwidth]{fig_instruction_retention.pdf}
81	  \caption{Instruction retention by constraint category under $\beta$\,=\,3 steering. Content constraints benefit most (+23.8\,pp); format and count constraints are unaffected.}
82	  \label{fig:ir-bar}
83	\end{figure}
84	
85	\FloatBarrier
86	
87	\begin{table}[t]
88	\centering\small
89	\caption{Instruction retention by constraint category ($\beta$\,=\,3 steering on ThreadGate checkpoint). Content constraints benefit most from increased goal attention.}
90	\label{tab:ir-results}
91	\begin{tabular}{lccc}
92	\toprule
93	\textbf{Category} & $\beta$\,=\,0 & $\beta$\,=\,3 & $\Delta$ \\
94	\midrule
95	Content    & 61.9\% & 85.7\% & +23.8\,pp \\
96	Position   & 66.7\% & 73.3\% & +6.7\,pp \\
97	Count      & 100\%  & 100\%  & 0 \\
98	Format     & 100\%  & 100\%  & 0 \\
99	\midrule
100	\textbf{Overall} & 75.9\% & 87.0\% & +11.1\,pp \\
101	\bottomrule
102	\end{tabular}
103	\end{table}
104	
105	\section{Long-Conversation AR Evaluation}\label{sec:appendix-n5}
106	
107	The main results (Table~\ref{tab:five-way}) report AR GAR from $N$\,=\,50 held-out conversations with a mean of 3.6 user turns. Table~\ref{tab:n5-ar} presents complementary results on $N$\,=\,5 conversations with 10 turns each, testing whether the observed patterns generalize beyond the training distribution's conversation length.
108	
109	\paragraph{Gating advantage vanishes at length.} In these longer dialogues, the gating advantage observed in shorter conversations vanishes: all fine-tuned variants collapse to AR GAR-ours of 0.015--0.025, compared to 0.030--0.064 in the shorter evaluation. ThreadGate's advantage over LoRA-only shrinks from 1.7$\times$ (0.064 vs.\ 0.037 in the $N$\,=\,50 evaluation) to 0.64$\times$ (0.016 vs.\ 0.025), actually reversing the ordering. This reversal is not statistically robust given the small sample ($N$\,=\,5) but directionally suggests that architectural modifications provide diminishing returns as conversation length increases and exposure bias accumulates.
110	
111	\paragraph{Convergence to base.} By turn~10, all fine-tuned variants converge to within 2$\times$ of the base model's GAR, compared to 3.4$\times$ at turn~1 in the shorter evaluation. This convergence is consistent with exposure bias compounding multiplicatively over turns: each model-generated turn introduces additional distributional drift from the teacher-forced training regime, and by turn~10 the accumulated drift overwhelms any gating or LoRA signal, leaving only the base model's intrinsic attention patterns.
112	
113	\paragraph{Caveats.} The $N$\,=\,5 sample size limits statistical power, and the 10-turn conversations may differ systematically from the 3--5 turn training distribution in ways beyond length (e.g., topic complexity, user engagement patterns). We present these results as directional evidence rather than definitive conclusions.
114	
115	\begin{table}[t]
116	\centering\small
117	\caption{AR GAR-ours on $N$\,=\,5 ten-turn conversations. The gating advantage observed in Table~\ref{tab:five-way} ($N$\,=\,50, mean 3.6 turns) diminishes with conversation length.}
118	\label{tab:n5-ar}
119	\begin{tabular}{lcc}
120	\toprule
121	\textbf{Configuration} & \textbf{AR GAR-O} & \textbf{$\Delta$ vs.\ Table~\ref{tab:five-way}} \\
122	\midrule
123	Base & 0.012 & $-$0.007 \\
124	\midrule
125	ThreadGate & 0.016 & $-$0.048 \\
126	\;+\,PCGrad & 0.015 & $-$0.015 \\
127	Uniform Gate & 0.015 & $-$0.018 \\
128	LoRA-only & 0.025 & $-$0.012 \\
129	\bottomrule
130	\end{tabular}
131	\end{table}
132	
133	\section{Statistical Test Details}\label{sec:appendix-stats}
134	
135	All statistical tests reported in the main text use non-parametric methods due to the non-normal, heavy-tailed distribution of per-conversation GAR values. Table~\ref{tab:stat-tests} consolidates the full results.
136	
137	\paragraph{Wilcoxon signed-rank tests.} We use paired Wilcoxon signed-rank tests for all pairwise configuration comparisons under AR evaluation, treating each conversation as a paired observation. The TG vs.\ LoRA-only comparison ($p$\,=\,0.004, $r$\,=\,0.454) confirms that turn-conditioned gating provides a statistically significant but modest improvement. The TG vs.\ +PCGrad comparison ($p$\,=\,0.002) shows that resolving gradient conflict is actively harmful. Gate turn conditioning uses an unpaired Wilcoxon test across 28 layers.
138	
139	\paragraph{Bootstrap confidence intervals.} The 95\% CIs in Table~\ref{tab:five-way} are computed via 10,000 bootstrap resamples of per-conversation mid-turn GAR averages (turns 2--$T$), using the percentile method.
140	
141	\paragraph{Effect sizes.} We report rank-biserial correlation $r = Z / \sqrt{N}$ as the effect size for Wilcoxon tests, where $Z$ is the standardized test statistic and $N$ is the number of observations. By standard conventions: $r < 0.3$ is small, $0.3 \leq r < 0.5$ is medium, and $r \geq 0.5$ is large. The TG vs.\ LoRA-only effect ($r$\,=\,0.454) is medium, and TG vs.\ Base ($r$\,=\,0.802) is large.
142	
143	\paragraph{Multiple comparisons.} We report uncorrected $p$-values throughout, as our comparisons are hypothesis-driven (each tests a specific causal exclusion) rather than exploratory. Applying Bonferroni correction to the 4 primary AR comparisons would adjust the significance threshold to 0.0125; all reported significant results ($p \leq 0.004$) survive this correction.
144	
145	\begin{table}[t]
146	\centering\small
147	\caption{Consolidated statistical tests. All AR comparisons use $N$\,=\,50 conversations (39 with $\geq$3 turns); gate conditioning uses 28 layers.}
148	\label{tab:stat-tests}
149	\begin{tabular}{llcc}
150	\toprule
151	\textbf{Comparison} & \textbf{Test} & $p$ & $r$ \\
152	\midrule
153	\multicolumn{4}{l}{\emph{AR GAR-ours ($\beta$\,=\,0)}} \\
154	TG vs.\ Base & Wilcoxon & $<$0.001 & 0.802 \\
155	TG vs.\ LoRA-only & Wilcoxon & 0.004 & 0.454 \\
156	TG vs.\ +PCGrad & Wilcoxon & 0.002 & --- \\
157	SS vs.\ TG & Wilcoxon & $<$0.001 & 0.869 \\
158	\midrule
159	\multicolumn{4}{l}{\emph{Gate conditioning (28 layers)}} \\
160	Turn 1 vs.\ Turn 21 & Wilcoxon & $3.7\!\times\!10^{-8}$ & 0.975 \\
161	\midrule
162	\multicolumn{4}{l}{\emph{Instruction retention}} \\
163	$\beta$\,=\,0 vs.\ $\beta$\,=\,3 & McNemar & 0.077 & --- \\
164	GAR--compliance & Pearson & 0.007 & 0.200 \\
165	\bottomrule
166	\end{tabular}
167	\end{table}
168	
169	\section{Llama-3.1-8B Complete Results}\label{sec:appendix-llama}
170	
171	Table~\ref{tab:llama-full} presents the complete Llama-3.1-8B-Instruct results, complementing the summary in \S\ref{subsec:cross-model}. Three configurations were trained (Base, ThreadGate, LoRA-only) using the same training pipeline as Qwen-2.5-7B (8K UltraChat, 3 epochs, LoRA rank 16). Training required 7.0--7.3 hours per variant on the same GPU.
172	
173	\paragraph{Teacher-forced evaluation.} TF GAR-ours is 0.484 (TG) and 0.481 (LoRA-only), confirming that gating provides zero benefit under teacher forcing on Llama, consistent with the Qwen results (0.50 vs.\ 0.50).
174	
175	\paragraph{Autoregressive evaluation.} AR evaluation uses $N$\,=\,20 mid-turn conversations (turns 3--$T$, excluding the first two turns to avoid initialization effects). The AR GAR distribution is heavy-tailed: the coefficient of variation exceeds 100\% for ThreadGate (mean 0.043, std 0.100), and 5\% of turn-level measurements exhibit sporadic attention spikes (GAR $\geq$ 0.4). We therefore report both mean and median.
176	
177	\paragraph{Gate profile.} Llama's gate profile differs qualitatively from Qwen's: Qwen shows minimum attenuation at early layers (L1\,=\,0.793, L5\,=\,0.797), while Llama shows a V-shaped valley at mid-to-late layers (L25\,=\,0.719, L24\,=\,0.809). Despite this architectural difference, both models converge toward identity under NTP pressure, and the TF-AR gap is comparable (27$\times$ by median for Llama vs.\ 8--17$\times$ for Qwen).
178	
179	\begin{table}[t]
180	\centering\small
181	\caption{Llama-3.1-8B-Instruct complete results. TF: teacher-forced ($N$\,=\,50); AR: autoregressive ($N$\,=\,20 for Base/TG/LoRA-only, $N$\,=\,50 for SS). Median is more representative due to heavy-tailed AR distributions (SS uses mean only).}
182	\label{tab:llama-full}
183	\resizebox{\columnwidth}{!}{%
184	\begin{tabular}{lcccc}
185	\toprule
186	& \multicolumn{2}{c}{\textbf{TF}} & \multicolumn{2}{c}{\textbf{AR}} \\
187	\cmidrule(lr){2-3} \cmidrule(lr){4-5}
188	& GAR-O & PPL & GAR-O (mean) & GAR-O (med) \\
189	\midrule
190	Base & 0.017 & 3.45 & 0.009 & 0.009 \\
191	ThreadGate & 0.484 & 2.57 & 0.043 & 0.018 \\
192	LoRA-only & 0.481 & 2.60 & 0.028 & 0.018 \\
193	\textbf{SS} & 0.477 & 2.82 & \textbf{0.166} & --- \\
194	\bottomrule
195	\end{tabular}}
196	\end{table}
197	
198	\FloatBarrier
199	
200	\begin{figure}[t]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "593edf02-76ca-46a3-8f5e-8d011c2655f8",
  "isSidechain": false,
  "promptId": "b0f005fa-c14f-47e1-bf29-f3925462c4b7",
  "type": "user",
  "uuid": "8dc526ab-1dea-415a-a6af-3b6a1710c7f4",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex",
      "content": "\\section{Training Configuration}\\label{sec:appendix-hyper}\n\nTable~\\ref{tab:hyperparams} lists the full training configuration shared across all fine-tuned variants. ThreadGate gate parameters receive a $10\\times$ learning rate multiplier and are initialized with bias 1.5 ($\\sigma(1.5) \\approx 0.82$); the gate MLP adds ${\\sim}$57K parameters per variant ($<$0.001\\% of 7B). The scheduled sampling variant (v8b) linearly increases the model-generated context ratio from 0 to 0.5 over 3 epochs (29.7--37.1\\% effective usage due to per-sample Bernoulli sampling). All experiments were conducted on a single NVIDIA RTX PRO 6000 Blackwell Server Edition GPU (96\\,GB VRAM), requiring 6--8 hours per variant.\n\n\\begin{table}[t]\n\\centering\\small\n\\caption{Training hyperparameters for all fine-tuned variants. Entries marked $\\dagger$ apply only to ThreadGate and its ablations.}\n\\label{tab:hyperparams}\n\\begin{tabular}{l@{\\hspace{8pt}}l}\n\\toprule\n\\textbf{Parameter} & \\textbf{Value} \\\\\n\\midrule\nBase model & Qwen-2.5-7B-Instruct \\\\\nLoRA rank / $\\alpha$ & 16 / 32 \\\\\nLoRA targets & \\texttt{q\\_proj}, \\texttt{v\\_proj} \\\\\nOptimizer & AdamW ($\\beta_1$\\!=\\!0.9, $\\beta_2$\\!=\\!0.999) \\\\\nLearning rate & $2 \\times 10^{-4}$ \\\\\nGate LR mult.$^\\dagger$ & $10\\times$ \\\\\nBatch / grad accum & 1 / 8 (eff.\\ 8) \\\\\nEpochs & 3 \\\\\nMax seq length & 2048 \\\\\nTraining data & 8K UltraChat convs \\\\\nSeed & 42 (+123 for TG, SS) \\\\\n$\\lambda_\\text{GAR}$/$\\lambda_\\text{div}$ & 1.0 / 1.0 \\\\\nGAR target $\\tau$ & 0.5 \\\\\nGate init bias$^\\dagger$ & 1.5 ($\\sigma\\!\\approx\\!0.82$) \\\\\nGate hidden dim$^\\dagger$ & 64 \\\\\nTurn embed dim$^\\dagger$ & 16 \\\\\nGPU & RTX PRO 6000 (96\\,GB) \\\\\nTraining time & 6--8 h / variant \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Loss Formulation Search}\\label{sec:appendix-loss}\n\nThe final MSE + gate diversity loss (\\S\\ref{sec:loss}) emerged from seven iterations spanning four loss families. Table~\\ref{tab:loss-iterations} summarizes the progression. The search was motivated by a consistent failure mode: naive formulations either collapse to trivial solutions (cumulative losses) or drive gates toward identity (maximize-family losses). We describe each family below.\n\n\\paragraph{Cumulative losses (v1--v2).} These losses accumulate GAR contributions across layers, rewarding monotonically increasing attention. v1 collapsed because once the cumulative GAR exceeded the threshold, the loss gradient vanished and gates froze. v2 added an $\\varepsilon$-stabilization term to the cumulative product, but numerical instability from the product of 28 per-layer terms dominated, and training followed the same trajectory.\n\n\\paragraph{Maximize losses (v3--v5).} These losses directly maximize mean GAR ($-\\text{mean}(\\text{GAR})$). The unbounded objective rewards full pass-through ($g \\to 1.0$), collapsing gate diversity (std $<$ 0.025). At $\\lambda$=2 (v3), gates froze within 100 steps; at $\\lambda$=10 (v3b), convergence to identity accelerated; at $\\lambda$=1 (v5), rebalancing delayed but did not prevent the same degenerate solution.\n\n\\paragraph{Smooth saturation (v6).} This bounded the reward using a saturating function, intended to prevent the unbounded growth of maximize losses. In practice, the loss landscape remained monotonic in $g$, and training followed the same terminal trajectory as the maximize family, only more slowly.\n\n\\paragraph{MSE + gate diversity (v7).} The MSE formulation provides bidirectional pressure: GAR above $\\tau$ incurs the same penalty as GAR below $\\tau$, preventing the runaway optimization of maximize losses. The gate diversity regularizer ($\\mathcal{L}_\\text{div}$) enforces a minimum standard deviation across per-layer gate values, preventing all gates from collapsing to a uniform value. This combination is the only one that achieved stable convergence (GAR-ours = 0.50, PPL = 2.78).\n\n\\begin{table*}[t]\n\\centering\\footnotesize\n\\caption{Loss formulation iterations on Qwen-2.5-7B-Instruct. GAR-ours (teacher-forced) and PPL are reported only for the converged configuration (v7).}\n\\label{tab:loss-iterations}\n\\begin{tabular}{l l l p{5.8cm} c c}\n\\toprule\n & \\textbf{Loss Family} & \\textbf{Status} & \\textbf{Failure Mechanism} & \\textbf{GAR} & \\textbf{PPL} \\\\\n\\midrule\nv1  & Cumulative            & \\texttimes~GAR loss $\\to$ 0     & GAR loss collapses to zero once threshold is reached; gate gradients vanish at equilibrium & ---  & ---  \\\\\nv2  & Cumulative + $\\varepsilon$ & \\texttimes~same trajectory & Numerical instability from cumulative product; $\\varepsilon$-stabilization insufficient & ---  & ---  \\\\\nv3  & Maximize ($\\lambda$=2)  & \\texttimes~gate frozen        & Unbounded reward drives gates toward identity (all-pass); no layer selectivity & ---  & ---  \\\\\nv3b & Maximize ($\\lambda$=10) & \\texttimes~identity collapse   & Higher $\\lambda$ accelerates convergence to same degenerate identity solution & ---  & ---  \\\\\nv5  & Maximize ($\\lambda$=1)  & \\texttimes~identity collapse   & Rebalancing delays but does not prevent identity collapse & ---  & ---  \\\\\nv6  & Smooth saturation       & \\texttimes~identity collapse   & Monotonic reward identical to maximize in practice; boundedness slows but does not alter terminal trajectory & ---  & ---  \\\\\nv7  & MSE + gate div          & \\checkmark~\\textbf{converged}  & \\textbf{Bidirectional penalty prevents identity collapse; gate diversity regularizer enforces layer selectivity} & 0.50 & 2.78 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\n\\section{Instruction Retention Details}\\label{sec:appendix-ir}\n\nTo evaluate whether GAR improvements translate to downstream task performance, we test instruction retention across 18 system-prompt constraint types using the ThreadGate checkpoint with $\\beta$\\,=\\,3 steering on $N$\\,=\\,200 held-out conversations. Each constraint type requires the model to follow a specific instruction embedded in the system prompt (e.g., ``always respond in bullet points'', ``never use the word X'', ``include a summary at the end''). This evaluation bridges the gap between our attention-level metric (GAR) and observable model behavior.\n\n\\paragraph{Evaluation protocol.} For each conversation, we inject a constraint into the system prompt and evaluate compliance across all assistant turns. A turn is compliant if it satisfies the constraint according to rule-based checkers (for format, count, and position constraints) or GPT-4-based evaluation (for content constraints, which require semantic judgment). We use the same 18 constraint types across all conversations, yielding $N$\\,=\\,54 paired evaluations (18 types $\\times$ 3 conversations per type) for the McNemar analysis.\n\n\\paragraph{Per-category results.} Table~\\ref{tab:ir-results} reports per-category compliance rates. Content constraints---which require attending to and recalling specific system-prompt instructions across turns---show the largest improvement (+23.8\\,pp), consistent with GAR measuring attention to goal tokens. This category includes constraints like ``mention X in every response'' and ``always reference the original topic,'' which require sustained attention to the system prompt. Position constraints (e.g., ``start each response with Y'') show a modest improvement (+6.7\\,pp), as they partially depend on goal-token attention. Format (e.g., ``use bullet points'') and count constraints (e.g., ``exactly 3 sentences'') show no change, consistent with these being procedural patterns that are cached in the model's generation routine rather than requiring ongoing attention to the system prompt.\n\n\\paragraph{Correlation analysis.} The GAR-compliance correlation ($r$\\,=\\,0.200, $p$\\,=\\,0.007) is statistically significant but modest, suggesting that attention to goal tokens is one of several factors in instruction compliance. Other factors likely include the model's procedural memory for format constraints, the specificity of the constraint (vague constraints are harder regardless of attention), and the interaction between constraint type and conversation topic. McNemar's test ($p$\\,=\\,0.077) is marginally significant for the overall compliance improvement, reflecting the small sample size (18 constraint types). These results are exploratory and pending multi-model confirmation.\n\nFigure~\\ref{fig:ir-bar} visualizes the per-category breakdown.\n\n\\begin{figure}[t]\n  \\centering\n  \\includegraphics[width=\\columnwidth]{fig_instruction_retention.pdf}\n  \\caption{Instruction retention by constraint category under $\\beta$\\,=\\,3 steering. Content constraints benefit most (+23.8\\,pp); format and count constraints are unaffected.}\n  \\label{fig:ir-bar}\n\\end{figure}\n\n\\FloatBarrier\n\n\\begin{table}[t]\n\\centering\\small\n\\caption{Instruction retention by constraint category ($\\beta$\\,=\\,3 steering on ThreadGate checkpoint). Content constraints benefit most from increased goal attention.}\n\\label{tab:ir-results}\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Category} & $\\beta$\\,=\\,0 & $\\beta$\\,=\\,3 & $\\Delta$ \\\\\n\\midrule\nContent    & 61.9\\% & 85.7\\% & +23.8\\,pp \\\\\nPosition   & 66.7\\% & 73.3\\% & +6.7\\,pp \\\\\nCount      & 100\\%  & 100\\%  & 0 \\\\\nFormat     & 100\\%  & 100\\%  & 0 \\\\\n\\midrule\n\\textbf{Overall} & 75.9\\% & 87.0\\% & +11.1\\,pp \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Long-Conversation AR Evaluation}\\label{sec:appendix-n5}\n\nThe main results (Table~\\ref{tab:five-way}) report AR GAR from $N$\\,=\\,50 held-out conversations with a mean of 3.6 user turns. Table~\\ref{tab:n5-ar} presents complementary results on $N$\\,=\\,5 conversations with 10 turns each, testing whether the observed patterns generalize beyond the training distribution's conversation length.\n\n\\paragraph{Gating advantage vanishes at length.} In these longer dialogues, the gating advantage observed in shorter conversations vanishes: all fine-tuned variants collapse to AR GAR-ours of 0.015--0.025, compared to 0.030--0.064 in the shorter evaluation. ThreadGate's advantage over LoRA-only shrinks from 1.7$\\times$ (0.064 vs.\\ 0.037 in the $N$\\,=\\,50 evaluation) to 0.64$\\times$ (0.016 vs.\\ 0.025), actually reversing the ordering. This reversal is not statistically robust given the small sample ($N$\\,=\\,5) but directionally suggests that architectural modifications provide diminishing returns as conversation length increases and exposure bias accumulates.\n\n\\paragraph{Convergence to base.} By turn~10, all fine-tuned variants converge to within 2$\\times$ of the base model's GAR, compared to 3.4$\\times$ at turn~1 in the shorter evaluation. This convergence is consistent with exposure bias compounding multiplicatively over turns: each model-generated turn introduces additional distributional drift from the teacher-forced training regime, and by turn~10 the accumulated drift overwhelms any gating or LoRA signal, leaving only the base model's intrinsic attention patterns.\n\n\\paragraph{Caveats.} The $N$\\,=\\,5 sample size limits statistical power, and the 10-turn conversations may differ systematically from the 3--5 turn training distribution in ways beyond length (e.g., topic complexity, user engagement patterns). We present these results as directional evidence rather than definitive conclusions.\n\n\\begin{table}[t]\n\\centering\\small\n\\caption{AR GAR-ours on $N$\\,=\\,5 ten-turn conversations. The gating advantage observed in Table~\\ref{tab:five-way} ($N$\\,=\\,50, mean 3.6 turns) diminishes with conversation length.}\n\\label{tab:n5-ar}\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Configuration} & \\textbf{AR GAR-O} & \\textbf{$\\Delta$ vs.\\ Table~\\ref{tab:five-way}} \\\\\n\\midrule\nBase & 0.012 & $-$0.007 \\\\\n\\midrule\nThreadGate & 0.016 & $-$0.048 \\\\\n\\;+\\,PCGrad & 0.015 & $-$0.015 \\\\\nUniform Gate & 0.015 & $-$0.018 \\\\\nLoRA-only & 0.025 & $-$0.012 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Statistical Test Details}\\label{sec:appendix-stats}\n\nAll statistical tests reported in the main text use non-parametric methods due to the non-normal, heavy-tailed distribution of per-conversation GAR values. Table~\\ref{tab:stat-tests} consolidates the full results.\n\n\\paragraph{Wilcoxon signed-rank tests.} We use paired Wilcoxon signed-rank tests for all pairwise configuration comparisons under AR evaluation, treating each conversation as a paired observation. The TG vs.\\ LoRA-only comparison ($p$\\,=\\,0.004, $r$\\,=\\,0.454) confirms that turn-conditioned gating provides a statistically significant but modest improvement. The TG vs.\\ +PCGrad comparison ($p$\\,=\\,0.002) shows that resolving gradient conflict is actively harmful. Gate turn conditioning uses an unpaired Wilcoxon test across 28 layers.\n\n\\paragraph{Bootstrap confidence intervals.} The 95\\% CIs in Table~\\ref{tab:five-way} are computed via 10,000 bootstrap resamples of per-conversation mid-turn GAR averages (turns 2--$T$), using the percentile method.\n\n\\paragraph{Effect sizes.} We report rank-biserial correlation $r = Z / \\sqrt{N}$ as the effect size for Wilcoxon tests, where $Z$ is the standardized test statistic and $N$ is the number of observations. By standard conventions: $r < 0.3$ is small, $0.3 \\leq r < 0.5$ is medium, and $r \\geq 0.5$ is large. The TG vs.\\ LoRA-only effect ($r$\\,=\\,0.454) is medium, and TG vs.\\ Base ($r$\\,=\\,0.802) is large.\n\n\\paragraph{Multiple comparisons.} We report uncorrected $p$-values throughout, as our comparisons are hypothesis-driven (each tests a specific causal exclusion) rather than exploratory. Applying Bonferroni correction to the 4 primary AR comparisons would adjust the significance threshold to 0.0125; all reported significant results ($p \\leq 0.004$) survive this correction.\n\n\\begin{table}[t]\n\\centering\\small\n\\caption{Consolidated statistical tests. All AR comparisons use $N$\\,=\\,50 conversations (39 with $\\geq$3 turns); gate conditioning uses 28 layers.}\n\\label{tab:stat-tests}\n\\begin{tabular}{llcc}\n\\toprule\n\\textbf{Comparison} & \\textbf{Test} & $p$ & $r$ \\\\\n\\midrule\n\\multicolumn{4}{l}{\\emph{AR GAR-ours ($\\beta$\\,=\\,0)}} \\\\\nTG vs.\\ Base & Wilcoxon & $<$0.001 & 0.802 \\\\\nTG vs.\\ LoRA-only & Wilcoxon & 0.004 & 0.454 \\\\\nTG vs.\\ +PCGrad & Wilcoxon & 0.002 & --- \\\\\nSS vs.\\ TG & Wilcoxon & $<$0.001 & 0.869 \\\\\n\\midrule\n\\multicolumn{4}{l}{\\emph{Gate conditioning (28 layers)}} \\\\\nTurn 1 vs.\\ Turn 21 & Wilcoxon & $3.7\\!\\times\\!10^{-8}$ & 0.975 \\\\\n\\midrule\n\\multicolumn{4}{l}{\\emph{Instruction retention}} \\\\\n$\\beta$\\,=\\,0 vs.\\ $\\beta$\\,=\\,3 & McNemar & 0.077 & --- \\\\\nGAR--compliance & Pearson & 0.007 & 0.200 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Llama-3.1-8B Complete Results}\\label{sec:appendix-llama}\n\nTable~\\ref{tab:llama-full} presents the complete Llama-3.1-8B-Instruct results, complementing the summary in \\S\\ref{subsec:cross-model}. Three configurations were trained (Base, ThreadGate, LoRA-only) using the same training pipeline as Qwen-2.5-7B (8K UltraChat, 3 epochs, LoRA rank 16). Training required 7.0--7.3 hours per variant on the same GPU.\n\n\\paragraph{Teacher-forced evaluation.} TF GAR-ours is 0.484 (TG) and 0.481 (LoRA-only), confirming that gating provides zero benefit under teacher forcing on Llama, consistent with the Qwen results (0.50 vs.\\ 0.50).\n\n\\paragraph{Autoregressive evaluation.} AR evaluation uses $N$\\,=\\,20 mid-turn conversations (turns 3--$T$, excluding the first two turns to avoid initialization effects). The AR GAR distribution is heavy-tailed: the coefficient of variation exceeds 100\\% for ThreadGate (mean 0.043, std 0.100), and 5\\% of turn-level measurements exhibit sporadic attention spikes (GAR $\\geq$ 0.4). We therefore report both mean and median.\n\n\\paragraph{Gate profile.} Llama's gate profile differs qualitatively from Qwen's: Qwen shows minimum attenuation at early layers (L1\\,=\\,0.793, L5\\,=\\,0.797), while Llama shows a V-shaped valley at mid-to-late layers (L25\\,=\\,0.719, L24\\,=\\,0.809). Despite this architectural difference, both models converge toward identity under NTP pressure, and the TF-AR gap is comparable (27$\\times$ by median for Llama vs.\\ 8--17$\\times$ for Qwen).\n\n\\begin{table}[t]\n\\centering\\small\n\\caption{Llama-3.1-8B-Instruct complete results. TF: teacher-forced ($N$\\,=\\,50); AR: autoregressive ($N$\\,=\\,20 for Base/TG/LoRA-only, $N$\\,=\\,50 for SS). Median is more representative due to heavy-tailed AR distributions (SS uses mean only).}\n\\label{tab:llama-full}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lcccc}\n\\toprule\n& \\multicolumn{2}{c}{\\textbf{TF}} & \\multicolumn{2}{c}{\\textbf{AR}} \\\\\n\\cmidrule(lr){2-3} \\cmidrule(lr){4-5}\n& GAR-O & PPL & GAR-O (mean) & GAR-O (med) \\\\\n\\midrule\nBase & 0.017 & 3.45 & 0.009 & 0.009 \\\\\nThreadGate & 0.484 & 2.57 & 0.043 & 0.018 \\\\\nLoRA-only & 0.481 & 2.60 & 0.028 & 0.018 \\\\\n\\textbf{SS} & 0.477 & 2.82 & \\textbf{0.166} & --- \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\\FloatBarrier\n\n\\begin{figure}[t]",
      "numLines": 200,
      "startLine": 1,
      "totalLines": 851
    }
  },
  "sourceToolAssistantUUID": "593edf02-76ca-46a3-8f5e-8d011c2655f8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921",
  "sessionId": "5d779602-0719-4d06-8bf9-fdd84990d5d0",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---


### Tool call

_source line 66 · 2026-05-25T20:34:53.820Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_0169LiEBYTw6fGb8UU93kaNW`</summary>

```json
{
  "project": "turn_residual_gating",
  "limit": 0,
  "filters": {
    "status": "DONE"
  },
  "fields": [
    "status",
    "conclusion",
    "metrics",
    "hypothesis"
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8dc526ab-1dea-415a-a6af-3b6a1710c7f4",
  "isSidechain": false,
  "requestId": "req_011CbPvgXBnW4DEqiLfHCB8g",
  "type": "assistant",
  "uuid": "db2ac22c-6c15-44ad-9287-bd45bf303fcd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921",
  "sessionId": "5d779602-0719-4d06-8bf9-fdd84990d5d0",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015qPDBZVNPxWRyoTde5zCEQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4689,
      "cache_read_input_tokens": 46833,
      "output_tokens": 309,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4689,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 309,
          "cache_read_input_tokens": 46833,
          "cache_creation_input_tokens": 4689,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4689
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

_source line 67_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[系统通知 — worker_done:worker_audit_appendix_tables_20260525T201208]: Worker worker_audit_appendix_tables_20260525T201208 已完成（status=done），请审查 Agent 的处理结果。",
  "leafUuid": "db2ac22c-6c15-44ad-9287-bd45bf303fcd",
  "sessionId": "5d779602-0719-4d06-8bf9-fdd84990d5d0"
}
```

---


### Runtime record

_source line 68_

```json
{
  "type": "ai-title",
  "aiTitle": "Review worker audit appendix tables completion",
  "sessionId": "5d779602-0719-4d06-8bf9-fdd84990d5d0"
}
```

---


### Tool result

_source line 69 · 2026-05-25T20:34:54.004Z_

<details><summary>↩ Tool result · `toolu_0169LiEBYTw6fGb8UU93kaNW`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {\"phase1a_multiseed_qwen\": {\"status\": \"DONE\", \"hypothesis\": \"Multi-seed (s123, s456) training across 5 Qwen conditions (PCGrad, UG, LoRA-only, TG, SS) to establish mean±std for all claims. 8 training runs + AR eval N≥50 each. Expect TF convergence (GAR~0.50) and consistent AR rankings across seeds.\", \"conclusion\": \"killed\"}, \"p1_ss_lora_only\": {\"status\": \"DONE\", \"hypothesis\": \"SS training on LoRA-only checkpoint (no ThreadGate) with same hyperparameters (rho_max=0.3, same schedule) should achieve similar GAR improvement as SS+TG. If confirmed, this proves the SS fix is architecture-agnostic, strengthening the paper's mitigation story (the gap is caused by exposure bias in any auxiliary-loss setup, and SS fixes it regardless of gating mechanism).\", \"conclusion\": \"killed\"}, \"phase2_switching\": {\"status\": \"DONE\", \"hypothesis\": \"TF→AR switching at turn k (k=1..5) on ThreadGate s42 checkpoint. If GAR drops abruptly at the switch point (matching pure-AR level within 1 turn), it confirms exposure bias as instantaneous distribution shift rather than gradual KV cache drift. Staircase = exposure bias dominant; linear slope = KV drift dominant.\", \"conclusion\": \"killed\"}, \"p1_llama_ss_eval\": {\"status\": \"DONE\", \"hypothesis\": \"Llama SS (2-epoch) reduces the TF-AR GAR gap on Llama-3.1-8B, confirming SS as model-general mitigation (C4+C5). Eval: TF+AR N=50 β=0/3/5.\", \"conclusion\": \"success\", \"metrics\": {\"ss_tf_gar\": 0.477, \"ss_tf_ppl\": 2.82, \"ss_ar_b0_gar\": 0.1662, \"ss_ar_b0_ppl\": 1.37, \"ss_ar_b5_gar\": 0.7905, \"ss_ar_b5_ppl\": 1.81, \"base_ar_gar\": 0.0179, \"base_ar_ppl\": 1.22, \"tf_ar_gap\": 2.87}}, \"p1_llama_ss_training\": {\"status\": \"DONE\", \"hypothesis\": \"SS is effective on Qwen (gap 8x to 1.4x). If SS also reduces the TF-AR gap on Llama-3.1-8B, it confirms SS as a model-general mitigation, strengthening C4 (mitigation) and C5 (cross-model) claims.\", \"conclusion\": \"success\"}, \"mmlu_eval_all\": {\"status\": \"DONE\", \"hypothesis\": \"ThreadGate's per-layer gating and auxiliary GAR loss do not degrade the model's general language understanding capabilities. All fine-tuned variants (TG/UG/LO/PCGrad/SS) should maintain MMLU 5-shot accuracy within 1pp of the Base LoRA-only checkpoint, confirming that attention steering is additive rather than destructive.\", \"conclusion\": \"success\", \"metrics\": {\"base_qwen\": 0.7423, \"pcgrad_v9_s42\": 0.7386, \"ss_v8b_s42\": 0.7375, \"lo_s42\": 0.7357, \"tg_v7_s42\": 0.7347, \"ug_s42\": 0.7346}}, \"p2_llama_gradient_conflict\": {\"status\": \"DONE\", \"hypothesis\": \"PCGrad fails to improve AR GAR on Llama-3.1-8B (as on Qwen), confirming cross-model that gradient conflict is not the root cause of the TF-AR gap, strengthening C2 (causal exclusion).\", \"conclusion\": \"success\", \"metrics\": {\"cos_sim_mean\": 0.0045, \"cos_sim_std\": 0.07, \"neg_cos_sim_layers_pct\": 53.1, \"mag_ratio_median\": 25.7, \"conclusion_note\": \"cos_sim≈0 indicates near-orthogonal (NOT conflict). Script conclusion text 'widespread conflict' is misleading — actual finding: NTP and GAR gradients are nearly orthogonal on Llama, consistent with Qwen pattern.\"}}, \"p1_tf_ar_kl_divergence\": {\"status\": \"DONE\", \"hypothesis\": \"TF and AR attention distributions diverge more on GAR-relevant heads (high gate values) than non-relevant heads, providing mechanistic evidence that exposure bias selectively disrupts goal-attending computation rather than uniformly degrading attention.\", \"metrics\": {\"tg_delta_gar\": 0.0165, \"base_delta_gar\": 0.0122, \"tg_mean_kl\": 0.054, \"base_mean_kl\": 0.043, \"gate_kl_correlation\": 0.11, \"high_kl_layers\": \"L23-L27, L9\", \"gar_robustness_ours_tg_base_ratio\": 21.4, \"gar_robustness_goal_only_ratio\": 63, \"gar_robustness_ours_all_ratio\": 1.7, \"gar_robustness_ours_first_ratio\": 1.8}, \"conclusion\": \"success\"}, \"qwen15b_phase1_diag\": {\"status\": \"DONE\", \"hypothesis\": \"GAR attention decay toward system-prompt goal tokens is a general phenomenon across model scales, not specific to 7B. Qwen-2.5-1.5B-Instruct should also show progressive GAR decline across conversation turns, confirming the phenomenon is architecture-level rather than scale-dependent.\", \"conclusion\": \"success\"}, \"d048_eval_ss_s456\": {\"status\": \"DONE\", \"hypothesis\": \"SS s456 eval: TF + AR N=50 + bootstrap CI to complete 3-seed SS metrics. Together with s42 and s123, establishes mean±std for C2 reviewer requirement.\", \"conclusion\": \"success\", \"metrics\": {\"tf_gar_ours_mid\": 0.4964, \"tf_gar_dongre_mid\": 0.3862, \"ar_beta0_gar\": 0.4325, \"ar_beta0_ppl\": 1.4394, \"ar_beta3_gar\": 0.605, \"ar_beta3_ppl\": 1.5868, \"ar_beta5_gar\": 0.7157, \"ar_beta5_ppl\": 1.8045, \"n_convs_ar\": 50}}, \"d048_ss_s456\": {\"status\": \"DONE\", \"hypothesis\": \"Scheduled sampling (ratio=0.3) with ThreadGate multi-seed (s456) to establish 3-seed mean±std for C2 reviewer requirement of at least 3 seeds\", \"conclusion\": \"success\"}, \"d048_eval_ss_s123\": {\"status\": \"DONE\", \"hypothesis\": \"SS s123 eval: TF + AR N=50 + bootstrap CI to establish multi-seed SS metrics. Expect TF GAR ~0.50, AR GAR similar to s42 (0.347), confirming SS effectiveness across seeds.\", \"conclusion\": \"success\", \"metrics\": {\"tf_gar_ours\": 0.5536, \"tf_gar_dongre\": 0.4106, \"tf_ppl\": 2.6123, \"ar_beta0_gar\": 0.4231, \"ar_beta0_ppl\": 1.4408, \"ar_beta3_gar\": 0.5903, \"ar_beta3_ppl\": 1.607, \"ar_beta5_gar\": 0.7174, \"ar_beta5_ppl\": 1.7852, \"n_convs_tf\": 200, \"n_convs_ar\": 39}}, \"d048_ss_s123\": {\"status\": \"DONE\", \"hypothesis\": \"Scheduled sampling (ratio=0.3) with ThreadGate multi-seed (s123) to establish 3-seed mean±std for C2 reviewer requirement. Corrected hyperparams matching d048_ss_s456.\", \"conclusion\": \"success\"}, \"d048_split_softmax_eval\": {\"status\": \"DONE\", \"hypothesis\": \"Split-softmax (Li et al., COLM 2024) post-softmax rescaling recovers AR GAR without the PPL cost of pre-softmax additive steering, providing an alternative inference-time intervention that separates attention allocation from logit distribution.\", \"conclusion\": \"failed\"}, \"d048_final_ar_eval\": {\"status\": \"DONE\", \"hypothesis\": \"Unified AR N=50 eval across 6 conditions (Base/TG/UG/LO/PCGrad/SS) with bootstrap CI and Wilcoxon tests to establish statistically rigorous comparisons for all claims\", \"conclusion\": \"success\", \"metrics\": {\"beta0\": {\"base_gar\": 0.019, \"tg_gar\": 0.064, \"ug_gar\": 0.033, \"lo_gar\": 0.037, \"pcgrad_gar\": 0.03, \"ss_gar\": 0.347}, \"beta3\": {\"base_gar\": 0.531, \"tg_gar\": 0.556, \"ss_gar\": 0.593}, \"beta5\": {\"base_gar\": 0.704, \"tg_gar\": 0.727, \"ss_gar\": 0.717}, \"wilcoxon_beta0\": {\"tg_vs_base_p\": \"<0.001\", \"tg_vs_base_r\": 0.802, \"ss_vs_tg_p\": \"<0.001\", \"ss_vs_tg_r\": 0.869}, \"ppl\": {\"base\": 1.447, \"tg\": 1.432, \"ss\": 1.442}, \"n_convs\": 39}}, \"d048_eval_ss_s42\": {\"status\": \"DONE\", \"hypothesis\": \"D048 multi-seed SS s42 eval: TF + AR N=50 + bootstrap CI (curve[2:]) to establish mean±std for scheduled sampling. Expect TF GAR ~0.50, AR GAR gap < 2× (vs base ~31×), PPL stable.\", \"metrics\": {\"tf\": {\"base_gar_ours_mid\": 0.0128, \"base_gar_dongre_mid\": 0.0031, \"base_ppl\": 4.34, \"base_ntp\": 1.4, \"tg_gar_ours_mid\": 0.5025, \"tg_gar_dongre_mid\": 0.389, \"tg_ppl\": 2.78, \"tg_ntp\": 0.98, \"baseline_mid_gar\": 0.0122}, \"ar\": {\"gar_ours_mid\": 0.3887, \"gar_ours_ci_95\": [0.3692, 0.3934], \"ppl\": 1.35}, \"gap_ratio\": 1.29, \"n_conversations_tf\": 50, \"n_conversations_ar\": 5, \"bootstrap_turns\": \"curve[2:] (turns 3-T)\", \"note\": \"AR used hardcoded N=5, not N=50. Will be re-evaluated in final unified batch with eval_200.json N=50.\"}, \"conclusion\": \"success\"}, \"d048_ss_s42\": {\"status\": \"DONE\", \"hypothesis\": \"Scheduled sampling (ratio=0.3) with ThreadGate reduces the ~30× TF-AR GAR gap by exposing the model to its own generated text during training. Multi-seed run (s42) under D048 unified protocol to establish mean±std for statistical testing. SS is the strongest mitigation candidate (prior single-seed showed gap 31×→1.57×).\", \"conclusion\": \"success\", \"metrics\": {\"final_avg_loss\": 0.9326, \"final_ntp_loss\": 0.932, \"final_gar_loss\": 0.0007, \"gate_mean\": 0.9527, \"gate_std\": 0.0589, \"gate_min\": 0.7383, \"gate_min_layer\": \"L4\", \"gate_max\": 1, \"ss_usage\": \"4750/16000 (29.7%)\", \"ss_fallback\": 0, \"epochs_completed\": 3, \"wall_clock_s\": 23418, \"wall_clock_h\": 6.5}}, \"eval_llama_ar_n20\": {\"status\": \"DONE\", \"hypothesis\": \"N=20 AR eval stabilizes Llama 3-way (Base/TG/LoRA-only) autoregressive GAR estimates. N=5 suffered from outlier influence (3/5 conv had GAR>0.4 outlier turns); N=20 provides robust mean±std.\", \"metrics\": {\"base\": {\"gar_ours_mean\": 0.0088, \"gar_ours_std\": 0.0056, \"gar_ours_median_per_conv\": 0.0093, \"gar_ours_median_per_turn_pool\": 0.0071, \"gar_ours_spike_ratio\": \"0%\", \"gar_dongre_mean\": 0.0049, \"gar_dongre_std\": 0.0013, \"gar_dongre_median\": 0.0047, \"ngar_ours_mid\": 0.1019, \"ngar_dongre_mid\": 0.1171, \"ppl\": 1.293, \"ppl_std\": 0.07, \"ntp_loss\": 0.2552}, \"tg\": {\"gar_ours_mean\": 0.0434, \"gar_ours_std\": 0.1002, \"gar_ours_median_per_conv\": 0.0179, \"gar_ours_median_per_turn_pool\": 0.0126, \"gar_ours_spike_ratio\": \"5% (2/40 turns GAR>=0.4)\", \"gar_dongre_mean\": 0.0183, \"gar_dongre_std\": 0.0198, \"gar_dongre_median\": 0.0152, \"ngar_ours_mid\": 0.5357, \"ngar_dongre_mid\": 0.4436, \"ppl\": 1.437, \"ppl_std\": 0.077, \"ntp_loss\": 0.3612}, \"lora_only\": {\"gar_ours_mean\": 0.0284, \"gar_ours_std\": 0.0481, \"gar_ours_median_per_conv\": 0.0184, \"gar_ours_median_per_turn_pool\": 0.0133, \"gar_ours_spike_ratio\": \"0%\", \"gar_dongre_mean\": 0.0205, \"gar_dongre_std\": 0.0241, \"gar_dongre_median\": 0.016, \"ngar_ours_mid\": 0.3488, \"ngar_dongre_mid\": 0.4997, \"ppl\": 1.419, \"ppl_std\": 0.075, \"ntp_loss\": 0.3483}, \"n_conversations\": 20, \"n_turns\": 4, \"mid_turns_definition\": \"turns 3-T (0-indexed avg_gar[2:], excluding turns 1-2). All 16 eval entries use same definition.\", \"stat_pool\": \"median_per_conv: median of 20 per-conversation mid-turn averages. median_per_turn_pool: median of 40 individual turn values (20 conv x 2 mid turns).\", \"ranking_gar_ours_mean\": \"TG(0.0434) > LO(0.0284) > Base(0.0088)\", \"ranking_gar_ours_median_per_conv\": \"TG(0.0179) ≈ LO(0.0184) > Base(0.0093)\", \"ranking_gar_ours_median_per_turn_pool\": \"TG(0.0126) ≈ LO(0.0133) > Base(0.0071)\", \"ranking_gar_dongre\": \"LO(0.0205) > TG(0.0183) > Base(0.0049)\", \"note\": \"Paper §5.5 cites median_per_conv (median of per-conversation mid-turn averages across N=20). median_per_turn_pool is the alternative statistic from pooled individual turns. Both confirm TG ≈ LO (zero-increment).\"}, \"conclusion\": \"success\"}, \"eval_llama_lora_only_s42\": {\"status\": \"DONE\", \"hypothesis\": \"LoRA-only ablation (no gate) on Llama-3.1-8B: if TG's GAR improvement comes from the gate, LoRA-only should show minimal GAR recovery vs base.\", \"metrics\": {\"tf\": {\"gar_ours\": 0.4807, \"gar_dongre\": 0.0188, \"ngar_ours\": 11.8031, \"ngar_dongre\": 0.8261, \"ppl\": 2.6, \"ntp_loss\": 0.9366, \"n_conversations\": 50, \"n_turns\": 4}, \"ar\": {\"gar_ours\": 0.0617, \"gar_dongre\": 0.0226, \"ngar_ours\": 0.6065, \"ngar_dongre\": 0.2537, \"ppl\": 1.32, \"ntp_loss\": 0.2787, \"n_conversations\": 5, \"n_turns\": 10}, \"gap_ratio_gar_ours\": 7.79}, \"conclusion\": \"success\"}, \"llama_lora_only_s42\": {\"status\": \"DONE\", \"hypothesis\": \"Llama-3.1-8B LoRA-only baseline (gate=none, 无 gating 机制): 与 Llama TG s42 对比，验证 gating 对 Llama 的增量贡献。如果 LoRA-only GAR ≈ TG GAR → gating 零增量与 Qwen 结论一致（C5 跨模型）。\", \"conclusion\": \"success\", \"metrics\": {\"final_avg_loss\": 0.9288, \"final_avg_ntp\": 0.9279, \"final_avg_gar\": 0.0009, \"gate_fixed\": 1, \"gate_type\": \"none\", \"wall_clock_s\": 25317, \"wall_clock_h\": 7.03, \"epochs_completed\": 3}}, \"phase2_tg_s42_v6\": {\"status\": \"DONE\", \"hypothesis\": \"smooth_saturation loss (-target*tanh(GAR/target), target=0.5) 提供有界但持续的 GAR 梯度，避免 maximize 的恒等退化（gate→1）和 hinge_target 的梯度消失（GAR达标后梯度=0）。预期：gate_std>0.05 的层间分化 + GAR 稳态在 0.3-0.5 + NTP loss 正常收敛 + 总 loss 为正。\", \"metrics\": {\"dryrun_step0_L_NTP\": 2.0275, \"dryrun_step0_L_GAR\": -0.0161, \"dryrun_step0_total_loss\": 2.0114, \"dryrun_step4_L_NTP\": 1.6544, \"dryrun_step4_L_GAR\": -0.0147, \"dryrun_step4_total_loss\": 1.6397, \"dryrun_gate_grad\": true, \"dryrun_gate_mean_init\": 0.8097, \"dryrun_gate_std_init\": 0.0341, \"dryrun_gate_min_init\": 0.6836, \"dryrun_gate_max_init\": 0.8672, \"dryrun_gate_mean_step5\": 0.8025, \"dryrun_gate_std_step5\": 0.0842, \"dryrun_gate_min_step5\": 0.5547, \"dryrun_gate_max_step5\": 0.9805, \"gs50_gate_mean\": 0.8117, \"gs50_gate_std\": 0.0612, \"gs50_gate_min\": 0.6836, \"gs50_gate_max\": 0.9805, \"gs100_gate_mean\": 0.8737, \"gs100_gate_std\": 0.0367, \"gs100_gate_min\": 0.8164, \"gs100_gate_max\": 0.9766, \"gs100_L_NTP\": 0.8151, \"gs100_L_GAR\": -0.158, \"gs100_total_loss\": 0.6571, \"gs100_profile_bottom3\": \"L12=0.816 L4=0.824 L13=0.824\", \"gs100_profile_top3\": \"L27=0.977 L26=0.961 L23=0.914\", \"gs143_L_GAR\": -0.3876, \"gs143_gate_mean\": 0.9227}, \"conclusion\": \"negative\"}, \"phase2_tg_s42\": {\"status\": \"DONE\", \"hypothesis\": \"ThreadGate (turn-conditional gating) 在 L_NTP+L_GAR 联合训练后，相比 Uniform Gate，mid-turn GAR recovery 高出 ≥3pp，验证 Cesaro 理论预测：position-conditional 干预优于 uniform 干预\", \"conclusion\": \"negative\", \"metrics\": {\"final_ntp_loss\": 0.94, \"final_gar_loss\": 0, \"gate_mean\": 0.988, \"gar_loss_zero_pct\": 87.6, \"epochs_completed\": 1.67, \"killed_reason\": \"SIGTERM by diagnose worker (unauthorized)\"}}, \"eval_v7_tg_s123\": {\"status\": \"DONE\", \"hypothesis\": \"v7 TG s123 eval: 验证 s123 seed 的 TF-AR GAR gap 与 s42 一致（~32×），确认 multi-seed robustness\", \"conclusion\": \"success\", \"metrics\": {\"iid_tf\": {\"gar_ours_mid\": 0.5052, \"gar_dongre_mid\": 0.0119, \"ppl\": 2.7802, \"ntp\": 0.9752}, \"modelgen_ar\": {\"gar_ours_mid\": 0.0165, \"gar_dongre_mid\": 0.0177, \"ppl\": 1.3855, \"ntp\": 0.3223}, \"gap_ratio\": 30.6, \"comparison_s42\": {\"tf_gar_ours_delta\": 0.0017, \"ar_gar_ours_delta\": 0.0008, \"gap_ratio_delta\": -1.4}}}, \"eval_v8b_ss_s123\": {\"status\": \"DONE\", \"hypothesis\": \"v8b SS model trained with s123 seed should reproduce s42 GAR metrics within acceptable gap_ratio [1.2x-2.5x] and no PPL degradation, confirming seed robustness of the scheduled sampling approach\", \"conclusion\": \"success\", \"metrics\": {\"iid\": {\"gar_ours\": 0.503, \"gar_dongre\": 0.394, \"ppl\": 2.781, \"ntp_loss\": 0.976, \"n_conv\": 50, \"n_turns\": 3}, \"modelgen\": {\"gar_ours\": 0.418, \"gar_dongre\": 0.441, \"ppl\": 1.389, \"ntp_loss\": 0.325, \"n_conv\": 5, \"n_turns\": 10}, \"gap_ratio\": 1.2, \"base_iid_ppl\": 4.338, \"base_modelgen_ppl\": 1.351}}, \"v7_tg_s123\": {\"status\": \"DONE\", \"hypothesis\": \"v7 TG s42 已验证 ThreadGate 有效性，s123 验证 seed robustness。预期 gate profile 和 GAR 收敛模式与 s42 一致。\", \"conclusion\": \"success\", \"metrics\": {\"epoch_1\": {\"avg_loss\": 0.9447, \"avg_ntp_loss\": 0.9434, \"avg_gar_loss\": 0.0013, \"avg_div_loss\": 0}, \"epoch_2\": {\"avg_loss\": 0.9315, \"avg_ntp_loss\": 0.9305, \"avg_gar_loss\": 0.001, \"avg_div_loss\": 0}, \"final_gate\": {\"mean\": 0.9467, \"std\": 0.051, \"min\": 0.793, \"max\": 1}, \"final_gate_profile\": {\"L0\": 0.883, \"L1\": 0.793, \"L2\": 0.996, \"L3\": 0.988, \"L4\": 0.984, \"L5\": 0.797, \"L6\": 0.961, \"L7\": 0.918, \"L8\": 0.965, \"L9\": 0.934, \"L10\": 0.969, \"L11\": 0.918, \"L12\": 0.926, \"L13\": 0.941, \"L14\": 0.93, \"L15\": 0.965, \"L16\": 0.941, \"L17\": 0.91, \"L18\": 0.961, \"L19\": 0.965, \"L20\": 0.973, \"L21\": 0.988, \"L22\": 0.969, \"L23\": 0.98, \"L24\": 0.98, \"L25\": 0.984, \"L26\": 0.988, \"L27\": 1}, \"training_time_s\": 21425.2}}, \"v8b_ss_s123\": {\"status\": \"DONE\", \"hypothesis\": \"v8b SS s42 成功（gap 32×→1.57×），s123 验证结果的 seed robustness。预期 model-gen GAR 同样显著提升，PPL 无恶化。\", \"conclusion\": \"success\", \"metrics\": {\"final_loss\": 0.9316, \"final_ntp_loss\": 0.9307, \"final_gar_loss\": 0.0009, \"final_gate_mean\": 0.9505, \"final_gate_std\": 0.0508, \"final_gate_min\": 0.7383, \"final_gate_max\": 1, \"ss_used_ratio\": 0.371, \"training_time_s\": 38773.4, \"epoch0_loss\": 1.0092, \"epoch1_loss\": 0.9444, \"epoch2_loss\": 0.9316}}, \"llama_ar_matched_eval\": {\"status\": \"DONE\", \"hypothesis\": \"用 matched 设置 (N=50/T=4) 重跑 Llama AR eval，消除 TF/AR 设置差异。与 TF 结果对比得到可直接写入论文的 gap ratio，验证 TG 在 AR 模式下仍能提升 GAR。\", \"conclusion\": \"success\", \"metrics\": {\"ar_base_ours\": {\"mid_gar\": 0.0082, \"ngar\": 0.1, \"ppl\": 1.267}, \"ar_tg_ours\": {\"mid_gar\": 0.0388, \"ngar\": 0.493, \"ppl\": 1.413}, \"ar_base_dongre\": {\"mid_gar\": 0.0051, \"ngar\": 0.12, \"ppl\": 1.267}, \"ar_tg_dongre\": {\"mid_gar\": 0.018, \"ngar\": 0.431, \"ppl\": 1.413}, \"tf_reference\": {\"tf_tg_ours_ngar\": 11.88, \"tf_base_ours_ngar\": 0.388, \"tf_tg_ours_raw\": 0.4836, \"tf_tg_dongre_raw\": 0.018}, \"matched_gap_analysis\": {\"gar_ours_raw_gap\": \"12.5x (TF 0.484 / AR 0.039)\", \"gar_ours_ngar_gap\": \"24.1x (TF 11.88 / AR 0.493)\", \"gar_dongre_raw_gap\": \"1.002x (TF 0.018 / AR 0.018) — zero gap\", \"tg_over_base_ar_ours\": \"4.71x\", \"tg_over_base_ar_dongre\": \"3.54x\", \"conclusion\": \"GAR-ours TF-AR gap 12.5x (raw) / 24x (nGAR) is genuine exposure bias. GAR-Dongre zero gap (1.002x) confirms mechanism specificity: exposure bias selectively destroys learned goal-attention routing while leaving content-overlap-based attention unaffected.\"}}}, \"instruction_retention_test\": {\"status\": \"DONE\", \"hypothesis\": \"Turn-level residual gating (β=3) preserves instruction-following ability across multi-turn conversations better than the baseline (β=0), because gating modulates residual contributions to retain earlier context signals rather than letting them decay through successive transformer layers.\", \"conclusion\": \"success\", \"metrics\": {\"late_turn_rate_beta0\": 0.759, \"late_turn_rate_beta3\": 0.87, \"late_turn_delta\": 0.111, \"mcnemar_chi2\": 3.125, \"mcnemar_p\": 0.0771, \"gar_compliance_r\": 0.2003, \"gar_compliance_p\": 0.007, \"category_content_constraint\": {\"beta0\": 0.619, \"beta3\": 0.857, \"delta\": 0.238}, \"category_count_constraint\": {\"beta0\": 1, \"beta3\": 1, \"delta\": 0}, \"category_format_constraint\": {\"beta0\": 1, \"beta3\": 1, \"delta\": 0}, \"category_position_constraint\": {\"beta0\": 0.667, \"beta3\": 0.733, \"delta\": 0.067}}}, \"llama_eval_s42\": {\"status\": \"DONE\", \"hypothesis\": \"Llama-3.1-8B TG eval: 如果 Llama TG 模型在 TF 模式下 GAR-ours 显著高于 AR 模式（如 Qwen v7 的 20-33x gap），则确认 training-inference GAR gap 跨模型泛化（C5）。同时测量 base model 作为 control。\", \"metrics\": {\"tf_base\": {\"gar_ours\": 0.0166, \"ngar_ours\": 0.3882, \"gar_dongre\": 0.0038, \"ngar_dongre\": 0.163, \"ppl\": 3.45, \"N\": 50, \"T\": 4}, \"tf_tg\": {\"gar_ours\": 0.4836, \"ngar_ours\": 11.8818, \"gar_dongre\": 0.018, \"ngar_dongre\": 0.7922, \"ppl\": 2.57, \"N\": 50, \"T\": 4}, \"ar_base\": {\"gar_ours\": 0.0086, \"ngar_ours\": 0.0798, \"gar_dongre\": 0.0118, \"ngar_dongre\": 0.1265, \"ppl\": 1.24, \"N\": 5, \"T\": 10}, \"ar_tg\": {\"gar_ours\": 0.0304, \"ngar_ours\": 0.2632, \"gar_dongre\": 0.0217, \"ngar_dongre\": 0.2459, \"ppl\": 1.32, \"N\": 5, \"T\": 10}, \"gap_ratio_tg_ours\": 15.9, \"gap_ratio_base_ours\": 1.93, \"gap_ratio_tg_dongre\": 0.83, \"vs_qwen_v7_gap_ratio\": 32.1, \"baseline_mid_gar\": 0.0122}, \"conclusion\": \"success\"}, \"llama_tg_s42\": {\"status\": \"DONE\", \"hypothesis\": \"在 Llama-3.1-8B-Instruct 上训练 ThreadGate（与 Qwen v7 相同配置），验证 C5：gating mechanism 和 GAR training-inference gap 跨模型泛化。如果 Llama TG 也出现 IID GAR ≈ target 但 model-gen GAR 坍塌 → 确认 exposure bias 的跨模型通用性。\", \"conclusion\": \"success\", \"metrics\": {\"epochs_completed\": 3, \"total_steps\": 3000, \"wall_clock_seconds\": 26212, \"wall_clock_hours\": 7.28, \"final_avg_loss\": 0.9233, \"final_avg_ntp\": 0.9224, \"final_avg_gar\": 0.0009, \"final_avg_div\": 0, \"final_gate_mean\": 0.9099, \"final_gate_std\": 0.0701, \"final_gate_min\": 0.7188, \"final_gate_max\": 0.9922, \"gate_profile_step3000\": {\"L0\": 0.957, \"L1\": 0.973, \"L2\": 0.977, \"L3\": 0.965, \"L4\": 0.992, \"L5\": 0.969, \"L6\": 0.957, \"L7\": 0.957, \"L8\": 0.961, \"L9\": 0.949, \"L10\": 0.938, \"L11\": 0.934, \"L12\": 0.969, \"L13\": 0.953, \"L14\": 0.957, \"L15\": 0.965, \"L16\": 0.953, \"L17\": 0.961, \"L18\": 0.922, \"L19\": 0.902, \"L20\": 0.883, \"L21\": 0.863, \"L22\": 0.836, \"L23\": 0.844, \"L24\": 0.809, \"L25\": 0.719, \"L26\": 0.762, \"L27\": 0.805, \"L28\": 0.801, \"L29\": 0.855, \"L30\": 0.898, \"L31\": 0.934}, \"checkpoint_size_gate_mb\": 4.2, \"checkpoint_size_lora_mb\": 26, \"gpu\": \"NVIDIA RTX PRO 6000 Blackwell\", \"vram_gb\": 102, \"mem_used_gb\": 63.4}}, \"attention_steering_gen_n50\": {\"status\": \"DONE\", \"hypothesis\": \"N=5 gen steering 显示 β∈[2,5] phase transition (GAR 0.06→0.68)，但样本量不足以报告置信区间。N=50 conversations 应重现同一 phase transition pattern 并提供统计鲁棒的 mean±std，加固 C6 claim (attention steering as causal mechanism proof)。\", \"metrics\": {\"corrected\": true, \"aggregation\": \"per-conv mid_gar(turns 2-7), >=3 turns only\", \"beta_0.0\": {\"mid_gar\": 0.0641, \"mid_gar_std\": 0.0809, \"ppl\": 1.4324, \"ppl_std\": 0.1029, \"n_valid\": 39}, \"beta_2.0\": {\"mid_gar\": 0.128, \"mid_gar_std\": 0.1101, \"ppl\": 1.4822, \"ppl_std\": 0.1385, \"n_valid\": 39}, \"beta_3.0\": {\"mid_gar\": 0.5558, \"mid_gar_std\": 0.0601, \"ppl\": 1.5605, \"ppl_std\": 0.1719, \"n_valid\": 39}, \"beta_4.0\": {\"mid_gar\": 0.6439, \"mid_gar_std\": 0.0607, \"ppl\": 1.6674, \"ppl_std\": 0.2241, \"n_valid\": 39}, \"beta_5.0\": {\"mid_gar\": 0.7271, \"mid_gar_std\": 0.0605, \"ppl\": 1.7723, \"ppl_std\": 0.2693, \"n_valid\": 38}, \"beta_10.0\": {\"mid_gar\": 0.9612, \"mid_gar_std\": 0.0152, \"ppl\": 3.4517, \"ppl_std\": 1.7813, \"n_valid\": 39}, \"n_convs_total\": 50, \"n_convs_valid\": 39, \"mode\": \"gen\", \"phase_transition_range\": \"[2, 3]\"}, \"conclusion\": \"success\"}, \"phase2_tg_s42_v8b_resume\": {\"status\": \"DONE\", \"hypothesis\": \"从 epoch_0 checkpoint resume v8b scheduled sampling 训练。SS 线性混合 0→0.5 teacher-forced + model-generated contexts。如果 model-gen context 上的 GAR 训练能缩小 30x training-inference gap → exposure bias mitigation 有效。成功标准：inference GAR 显著高于 v7 的 0.016 (至少 +1pp)，PPL 不恶化。\", \"metrics\": {\"training\": {\"total_steps\": 3000, \"epochs_completed\": 3, \"wall_clock_hours\": 8.1, \"final_loss\": 0.933, \"final_ntp_loss\": 0.9322, \"final_gar_loss\": 0.0008, \"final_gate_mean\": 0.9586, \"final_gate_std\": 0.0582, \"ss_ratio\": 0.5}, \"eval_iid\": {\"gar_ours\": 0.4983, \"gar_dongre\": 0.3855, \"ppl\": 2.78}, \"eval_modelgen\": {\"gar_ours\": 0.3177, \"gar_dongre\": 0.3533, \"ppl\": 1.38}, \"vs_v7\": {\"iid_gar_ours_delta\": -0.005, \"modelgen_gar_ours_delta\": 0.302, \"gap_ratio_v7\": 32, \"gap_ratio_v8b\": 1.57}}, \"conclusion\": \"success\"}, \"llama_phase1_gar_diag\": {\"status\": \"DONE\", \"hypothesis\": \"Llama-3.1-8B-Instruct 在 multi-turn dialogue 中也应出现 goal attention decay（与 Qwen-2.5-7B 类似），确认 attention decay 是 transformer 架构通用现象而非模型特有。Phase 1 诊断：测量 base Llama 的 per-turn GAR profile。\", \"conclusion\": \"success\", \"metrics\": {\"per_turn_gar\": {\"turn_1\": 0.0263, \"turn_2\": 0.0183, \"turn_3\": 0.0087, \"turn_4\": 0.0055, \"turn_5\": 0.006, \"turn_6\": 0.0035, \"turn_7\": 0.0038, \"turn_8\": 0.0037, \"turn_9\": 0.005, \"turn_10\": 0.0026}, \"t1_t10_decay_pct\": 90.1, \"t1_mid38_drop_pct\": 80.2, \"n_topics\": 5, \"model\": \"Meta-Llama-3.1-8B-Instruct\", \"mode\": \"gen\", \"n_conversations\": 5, \"n_turns\": 10}}, \"eval_v8b_ss\": {\"status\": \"DONE\", \"hypothesis\": \"Scheduled Sampling (linear 0→0.5 mixing of teacher-forced and model-gen contexts) closes the 30x training-inference GAR gap by reducing exposure bias, resulting in model-gen GAR significantly above v7 baseline (0.016) while preserving IID GAR and PPL.\", \"metrics\": {\"iid_gar_ours\": 0.4983, \"iid_gar_dongre\": 0.3855, \"iid_ppl\": 2.78, \"iid_ngar_ours\": 13.5, \"iid_ngar_dongre\": 22.68, \"modelgen_gar_ours\": 0.3177, \"modelgen_gar_dongre\": 0.3533, \"modelgen_ppl\": 1.38, \"modelgen_ngar_ours\": 4.47, \"modelgen_ngar_dongre\": 5.92, \"iid_turn1_gar_ours\": 0.5398, \"modelgen_turn1_gar_ours\": 0.4333}, \"conclusion\": \"success\"}, \"attention_steering_eval200_tf\": {\"status\": \"DONE\", \"hypothesis\": \"N=200 TF 模式 attention steering 验证 β-GAR 关系的统计鲁棒性。在 teacher-forced context (无 exposure bias) 下，steering 效果应更温和（baseline GAR 已 ~0.50），但仍展示 β 调控 attention 的能力。与 N=5 gen 模式结果互补：tf 验证机制可控性，gen 验证因果闭环。\", \"metrics\": {\"beta_0.0\": {\"mid_gar\": 0.5353, \"ppl\": 2.62}, \"beta_2.0\": {\"mid_gar\": 0.6112, \"ppl\": 2.69}, \"beta_3.0\": {\"mid_gar\": 0.788, \"ppl\": 2.93}, \"beta_4.0\": {\"mid_gar\": 0.8165, \"ppl\": 3.49}, \"beta_5.0\": {\"mid_gar\": 0.8325, \"ppl\": 6.15}, \"beta_10.0\": {\"mid_gar\": 0.977, \"ppl\": 505.21}, \"n_convs\": 200, \"mode\": \"tf\"}, \"conclusion\": \"success\"}, \"trc_baseline_v7_tg\": {\"status\": \"DONE\", \"hypothesis\": \"如果 exposure bias 对 auxiliary objectives 的破坏跨特征空间通用，那么 TRC (hidden state cos_sim) 在 model-gen 下也应出现与 GAR (attention 空间) 类似的 TF/gen gap。在 v7 TG / LoRA-only / base 三个 checkpoint 上测量 TRC baseline，确认 gap 是否存在。成功标准：gen TRC 显著低于 TF TRC。\", \"conclusion\": \"success\", \"metrics\": {\"v7_tg\": {\"tf_trc\": 0.3339, \"gen_trc\": 0.3323, \"trc_gap\": 0.0016, \"tf_tbp_ppl\": 1.05, \"gen_tbp_ppl\": 1.05}, \"lora_only\": {\"tf_trc\": 0.349, \"gen_trc\": 0.4106, \"trc_gap\": -0.0617, \"tf_tbp_ppl\": 9.5, \"gen_tbp_ppl\": 12}, \"base\": {\"tf_trc\": 0.1494, \"gen_trc\": 0.1494, \"trc_gap\": 0, \"tf_tbp_ppl\": 2.05, \"gen_tbp_ppl\": 2.05}}}, \"attention_steering_v7_tg_gen\": {\"status\": \"DONE\", \"hypothesis\": \"推理时向 attention logits 注入 goal-position bias β 可恢复 autoregressive GAR。如果 GAR 从 0.015 显著提升 → 闭合因果环：exposure bias → attention 偏移 → GAR 坍塌 → 手动修正注意力 → GAR 恢复。扫描 β ∈ {0, 0.5, 1.0, 2.0, 5.0, 10.0}，成功标准：GAR > 0.1 且 PPL 不严重恶化。\", \"conclusion\": \"success\", \"metrics\": {\"beta_0.0\": {\"mid_turns_avg_gar\": 0.028, \"avg_ppl\": 1.409}, \"beta_0.5\": {\"mid_turns_avg_gar\": 0.0287, \"avg_ppl\": 1.387}, \"beta_1.0\": {\"mid_turns_avg_gar\": 0.0349, \"avg_ppl\": 1.36}, \"beta_2.0\": {\"mid_turns_avg_gar\": 0.062, \"avg_ppl\": 1.411}, \"beta_5.0\": {\"mid_turns_avg_gar\": 0.6795, \"avg_ppl\": 1.908}, \"beta_10.0\": {\"mid_turns_avg_gar\": 0.959, \"avg_ppl\": 4.22}, \"phase_transition_range\": \"[2, 5]\", \"baseline_gar\": 0.028, \"max_gar_at_acceptable_ppl\": 0.6795, \"max_gar_at_acceptable_ppl_beta\": 5}}, \"phase2_tg_s42_v8b_ss_fixed\": {\"status\": \"DONE\", \"hypothesis\": \"Fixed scheduled sampling (D026 三项 bug 修复后): 线性从 0→0.5 混合 teacher-forced + model-generated contexts 计算 GAR loss。如果 model-gen context 上的 GAR 训练能缩小 30x training-inference gap → exposure bias mitigation 有效，paper 从纯 negative 升级为 diagnosis + initial remedy。超参与 v7 一致 (lambda_gar=1.0, MSE+gate_div)，唯一变量是 SS path。成功标准：inference GAR 显著高于 v7 的 0.016 (至少 +1pp)，PPL 不恶化。\", \"conclusion\": \"failed\"}, \"phase2_tg_s42_v7\": {\"status\": \"DONE\", \"hypothesis\": \"MSE 双向 loss (mean_GAR - target)² + gate diversity 正则 F.relu(min_std - gate_std) 从结构上解决恒等退化：MSE 在 GAR > target 时反向惩罚（不再单调推高），gate_div 直接强制层间分化。预期：gate_std 稳定 >0.05 + GAR 收敛到 target=0.5 附近 + NTP 正常收敛。\", \"metrics\": {\"eval_iid_ours_mid_gar\": 0.5035, \"eval_iid_dongre_mid_gar\": 0.0152, \"eval_iid_ppl\": 2.784, \"eval_heldout_ours_mid_gar\": 0.5035, \"eval_heldout_dongre_mid_gar\": 0.0152, \"eval_heldout_ppl\": 2.78, \"eval_modelgen_ours_mid_gar\": 0.0157, \"eval_modelgen_dongre_mid_gar\": 0.0194, \"eval_modelgen_ppl\": 1.36, \"gate_mean_final\": 0.9336, \"gate_std_final\": 0.0492}, \"conclusion\": \"success\"}, \"phase2_tg_s42_v9_pcgrad\": {\"status\": \"DONE\", \"hypothesis\": \"PCGrad (Yu et al. NeurIPS 2020) 消除 NTP-GAR 梯度方向冲突后（仅对 gate 参数投影 NTP 梯度到 GAR 梯度正交平面），如果 30x training-inference GAR gap 仍在 → 因果证据证明 exposure bias（非梯度竞争）是 gap 根因。与 v7 对比：相同超参（lambda_gar=1.0, MSE+gate_div），唯一变量是梯度处理方式。成功标准：(1) 梯度 cos_sim 显著改善（从 v7 的 -0.089 提升到 ≥0），(2) 但推理 GAR 仍 ≈ v7 水平（0.016），证明梯度冲突不是 gap 的因。\", \"conclusion\": \"success\", \"metrics\": {\"eval_iid_ours_mid_gar\": 0.5002, \"eval_iid_dongre_mid_gar\": 0.0123, \"eval_iid_ppl\": 2.78, \"eval_iid_ntp\": 0.9752, \"eval_heldout_ours_mid_gar\": 0.5002, \"eval_heldout_dongre_mid_gar\": 0.0123, \"eval_heldout_ppl\": 2.78, \"eval_heldout_ntp\": 0.9752, \"eval_modelgen_ours_mid_gar\": 0.0151, \"eval_modelgen_dongre_mid_gar\": 0.0173, \"eval_modelgen_ppl\": 1.5, \"vs_v7_iid_ppl_diff\": 0.004, \"vs_v7_iid_gar_diff\": -0.0033}}, \"phase2_lora_only_s42\": {\"status\": \"DONE\", \"hypothesis\": \"LoRA-only baseline (gate 固定 1.0，无 gating 机制) 在相同 MSE+NTP loss 下 GAR 应低于 ThreadGate (v7)。如果 LoRA-only 也能训到 GAR~0.5，则 gating 机制贡献为零，paper story 不成立。关键对比：LoRA-only 的 GAR 收敛值 vs v7 的 0.48。\", \"conclusion\": \"success\", \"metrics\": {\"epochs_completed\": 3, \"global_steps\": 3000, \"training_time_seconds\": 20588.6, \"training_time_hours\": 5.7, \"gate_fixed\": 1, \"gate_type_actual\": \"none\", \"final_lora_size_mb\": 20, \"eval_modelgen_ours_mid_gar\": 0.0245, \"eval_modelgen_dongre_mid_gar\": 0.0185, \"eval_modelgen_ppl\": 1.371}}, \"phase2_ug_s42\": {\"status\": \"DONE\", \"hypothesis\": \"Uniform gating baseline: per-layer independent gates without turn conditioning (content-dependent only), to isolate whether ThreadGate's turn-conditioned gating provides benefit over content-only residual scaling. Same training setup as v7 but with gate-type=uniform.\", \"conclusion\": \"success\", \"metrics\": {\"epoch0_avg_loss\": 1.0019, \"epoch0_avg_ntp\": 0.9755, \"epoch0_avg_gar\": 0.0259, \"epoch0_avg_div\": 0.0005, \"epoch1_avg_loss\": 0.9447, \"epoch1_avg_ntp\": 0.9435, \"epoch1_avg_gar\": 0.0013, \"epoch1_avg_div\": 0, \"epoch2_avg_loss\": 0.9319, \"epoch2_avg_ntp\": 0.9309, \"epoch2_avg_gar\": 0.001, \"epoch2_avg_div\": 0, \"final_gate_mean\": 0.9598, \"final_gate_std\": 0.0518, \"final_gate_min\": 0.7773, \"final_gate_max\": 1, \"final_profile_L3\": 0.777, \"final_profile_L5\": 0.812, \"final_profile_L0\": 0.875, \"final_profile_L27\": 1, \"training_time_seconds\": 21994.5, \"training_time_hours\": 6.1, \"global_steps\": 7950, \"unexpected_per_layer_variation\": true, \"eval_modelgen_ours_mid_gar\": 0.0149, \"eval_modelgen_dongre_mid_gar\": 0.0185, \"eval_modelgen_ppl\": 1.396}}, \"phase2_tg_s42_v8_schedsampling\": {\"status\": \"DONE\", \"hypothesis\": \"Scheduled sampling 应用到 GAR loss（线性从 0→0.5 混合 teacher-forced + model-generated contexts）能缩小 v7 的 30x training-inference GAR gap。机制：在 model-generated context 上计算 GAR loss 迫使 attention pattern 适应推理时分布，直接 address teacher-forcing distribution shift。成功标准：inference GAR 显著高于 v7 的 0.016，PPL 不显著恶化（≤2.78+0.2）。\", \"conclusion\": \"failed\", \"metrics\": {\"killed_at_microstep\": 1950, \"total_microsteps\": 24000, \"completion_pct\": 8.1, \"global_step_approx\": 244, \"total_global_steps\": 3000, \"ss_steps_observed\": 1, \"tf_lgar_mean_step850_1400\": 0.0062, \"tf_lgar_std\": 0.0082, \"tf_lgar_collapse_step\": 800, \"gate_mean_final\": 0.93, \"ss_ratio_at_kill\": 0.081, \"crash_reason\": \"killed by director: SS path code bug (D026) makes experiment invalid, GPU needed for PCGrad\", \"design_flaw_ss_ramp_too_slow\": true, \"design_flaw_no_ss_tf_separate_logging\": true}}, \"analysis_attention_heatmap\": {\"status\": \"DONE\", \"hypothesis\": \"四模型（Base/TG/UG/LoRA-only）的 goal attention 衰减模式是否一致？如果 TG 的 attention decay 与 LoRA-only 无差异，则 gating 机制对 attention 分布零增量。\", \"conclusion\": \"success\", \"metrics\": {\"base_mean_goal_attn\": 0.0136, \"base_decay\": 0.875, \"tg_mean_goal_attn\": 0.0232, \"tg_decay\": 0.777, \"ug_mean_goal_attn\": 0.0216, \"ug_decay\": 0.803, \"lora_mean_goal_attn\": 0.0216, \"lora_decay\": 0.81, \"gating_incremental_benefit\": \"none\"}}, \"analysis_gradient_conflict\": {\"status\": \"DONE\", \"hypothesis\": \"NTP-GAR 梯度冲突在 v7 训练过程中是否逐层普遍存在？量化 cos_sim 和 magnitude ratio 的演化，验证 NTP 是否在训练中逐渐完全压制 GAR 信号。\", \"conclusion\": \"success\", \"metrics\": {\"epoch0_cos_sim\": -0.089, \"epoch1_cos_sim\": -0.054, \"epoch2_cos_sim\": -0.042, \"epoch0_neg_layers_pct\": 78.6, \"epoch1_neg_layers_pct\": 71.4, \"epoch2_neg_layers_pct\": 67.9, \"epoch0_mag_ratio\": 7.5, \"epoch1_mag_ratio\": 13.7, \"epoch2_mag_ratio\": 14.7}}, \"phase2_4way_eval_heldout\": {\"status\": \"DONE\", \"hypothesis\": \"四路消融的三路趋同结论（TG≈UG≈LoRA-only，gating 零增量）在 held-out eval 数据（idx≥8000，与训练集无重叠）上复现，排除数据重叠 confound。预期：相对比较保持（三路趋同），绝对 GAR 值可能变化。\", \"metrics\": {\"base_ours_mid_gar\": 0.0128, \"base_ours_recovery_pp\": 0.06, \"base_dongre_mid_gar\": 0.0031, \"base_dongre_recovery_pp\": -0.91, \"base_ppl\": 4.34, \"base_ntp\": 1.4045, \"tg_ours_mid_gar\": 0.5035, \"tg_ours_recovery_pp\": 49.13, \"tg_dongre_mid_gar\": 0.0152, \"tg_dongre_recovery_pp\": 0.3, \"tg_ppl\": 2.78, \"tg_ntp\": 0.9771, \"ug_ours_mid_gar\": 0.5053, \"ug_ours_recovery_pp\": 49.31, \"ug_dongre_mid_gar\": 0.0124, \"ug_dongre_recovery_pp\": 0.02, \"ug_ppl\": 2.78, \"ug_ntp\": 0.9752, \"lora_ours_mid_gar\": 0.4978, \"lora_ours_recovery_pp\": 48.56, \"lora_dongre_mid_gar\": 0.0132, \"lora_dongre_recovery_pp\": 0.1, \"lora_ppl\": 2.78, \"lora_ntp\": 0.9771, \"three_way_convergence_confirmed\": true, \"gar_ours_spread_pp\": 0.75, \"ppl_spread\": 0, \"data_overlap\": false}, \"conclusion\": \"success\"}, \"phase2_4way_eval\": {\"status\": \"DONE\", \"hypothesis\": \"Turn-residual gating (TRG) improves multi-turn response quality over LoRA-only and base model baselines because it selectively amplifies conversational context signals, which should manifest as higher GAR scores across 4 conditions (base, base+TRG, LoRA, LoRA+TRG).\", \"conclusion\": \"negative\", \"metrics\": {\"base_ours_mid_gar\": 0.0107, \"base_ours_recovery_pp\": -0.15, \"base_dongre_mid_gar\": 0.003, \"base_dongre_recovery_pp\": -0.92, \"base_ppl\": 4.23, \"base_ntp\": 1.4162, \"tg_ours_mid_gar\": 0.4866, \"tg_ours_recovery_pp\": 47.44, \"tg_dongre_mid_gar\": 0.0157, \"tg_dongre_recovery_pp\": 0.35, \"tg_ppl\": 2.63, \"tg_ntp\": 0.9484, \"ug_ours_mid_gar\": 0.4923, \"ug_ours_recovery_pp\": 48.01, \"ug_dongre_mid_gar\": 0.013, \"ug_dongre_recovery_pp\": 0.08, \"ug_ppl\": 2.62, \"ug_ntp\": 0.9433, \"lora_ours_mid_gar\": 0.486, \"lora_ours_recovery_pp\": 47.39, \"lora_dongre_mid_gar\": 0.0137, \"lora_dongre_recovery_pp\": 0.15, \"lora_ppl\": 2.63, \"lora_ntp\": 0.9482, \"route_b_confirmed\": true, \"gating_incremental_benefit\": \"none\"}}, \"phase2_tg_s42_v5\": {\"status\": \"DONE\", \"hypothesis\": \"重新平衡超参（λ=1.0 降 GAR 贡献至 ~50%，init_bias=1.5 使 sigmoid≈0.82 接近正常模型行为，gate_lr_multiplier=10 保持）能在 3-epoch 全量训练中产生有意义的 gate 分化（gate_std>0.05），同时 GAR 稳态在 0.1-0.5（非病态饱和），NTP loss 正常收敛，总 loss 保持正值\", \"metrics\": {\"step2000_gate_std\": 0.0225, \"step2000_gate_mean\": 0.9586, \"step2000_gate_min\": 0.9062, \"step2000_gate_max\": 0.9961, \"step2000_L_GAR\": -0.8977, \"step2000_L_NTP\": 0.7611, \"step2000_total_loss\": -0.1365, \"step2400_gate_std\": 0.0219, \"step2400_gate_mean\": 0.9651, \"step2400_gate_min\": 0.918, \"step2400_gate_max\": 0.9961, \"step2400_profile\": \"L0=0.918 L12=0.918 L13=0.926 L1=0.996 L26=0.996\", \"L_GAR_saturated_at\": -0.91, \"gate_range_compression\": \"0.918-0.996\"}, \"conclusion\": \"negative\"}, \"phase2_tg_s42_v4\": {\"status\": \"DONE\", \"hypothesis\": \"重新平衡超参（λ=1.0 降 GAR 贡献至 ~50%，init_bias=1.5 使 sigmoid≈0.82 接近正常模型行为，gate_lr_multiplier=10 保持）能在 3-epoch 全量训练中产生有意义的 gate 分化（gate_std>0.05），同时 GAR 稳态在 0.1-0.5（非病态饱和），NTP loss 正常收敛，总 loss 保持正值\", \"conclusion\": \"failed\"}, \"phase2_tg_s42_v3b\": {\"status\": \"DONE\", \"hypothesis\": \"λ=10 + gate_lr=10x + init_bias=0.0 (sigmoid=0.5) 能否驱动 gate 产生 layer 间分化 (gate_std>0.05)？如果 500 步后 gate_std<0.02 且无选择性 → GAR-driven gating 梯度路径确认失败，需要 pivot\", \"conclusion\": \"success\", \"metrics\": {\"gate_std_final\": 0.087, \"gate_mean_final\": 0.9388, \"gate_min_final\": 0.5352, \"gate_max_final\": 0.9922, \"L4_gate\": 0.535, \"L0_gate\": 0.777, \"L_NTP_final\": 0.7787, \"L_GAR_final\": -0.9606, \"elapsed_seconds\": 3565.9, \"optimizer_steps\": 500, \"gate_grad_received\": true}}, \"phase2_tg_s42_v3\": {\"status\": \"DONE\", \"hypothesis\": \"ThreadGate + maximize GAR loss (L_GAR=-mean(GAR)) 提供持续非零梯度，避免 hinge loss 的退化平衡点，gate 值应随训练下降（学习到选择性干预），同时 NTP loss 正常收敛\", \"conclusion\": \"negative\", \"metrics\": {\"gate_mean_step0\": 0.8743, \"gate_mean_step500\": 0.8761, \"gate_delta\": 0.004, \"gate_std\": 0.001, \"final_ntp_loss\": 0.94, \"final_gar_loss\": -0.019, \"gar_contribution_pct\": \"2-4%\", \"diagnosis\": \"gate frozen, GAR indirect gradient too weak\"}}, \"phase2_tg_s42_v2\": {\"status\": \"DONE\", \"hypothesis\": \"ThreadGate + 修复后的 cumulative GAR loss (ε=0.001) 在 L_NTP+L_GAR 联合训练后，mid-turn GAR recovery 应显著优于 v1 (NTP-only baseline)，验证 GAR loss 的有效性\", \"conclusion\": \"killed\"}, \"phase1_gar_diag\": {\"status\": \"DONE\", \"hypothesis\": \"Qwen2.5-7B-Instruct 在 10-turn 多轮对话中，中间 turns (3-8) 的 GAR (Goal Accessibility Ratio) 相对 turn-1 下降 ≥15%，表明模型对 system prompt 中目标 token 的注意力随对话进行显著衰减\", \"conclusion\": \"success\", \"metrics\": {\"turn1_avg_gar\": 0.0418, \"mid_turns_avg_gar\": 0.0122, \"relative_drop\": 0.708, \"num_conversations\": 5, \"num_turns\": 10, \"per_turn_avg_gar\": [0.0418, 0.0241, 0.0224, 0.013, 0.0133, 0.0086, 0.0078, 0.008, 0.0157, 0.0064]}}}, \"count\": 53, \"total\": 53, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.1655}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "db2ac22c-6c15-44ad-9287-bd45bf303fcd",
  "isSidechain": false,
  "promptId": "b0f005fa-c14f-47e1-bf29-f3925462c4b7",
  "type": "user",
  "uuid": "2bffec83-2837-47f2-94b9-7c117d54d296",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {\\\"phase1a_multiseed_qwen\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"Multi-seed (s123, s456) training across 5 Qwen conditions (PCGrad, UG, LoRA-only, TG, SS) to establish mean±std for all claims. 8 training runs + AR eval N≥50 each. Expect TF convergence (GAR~0.50) and consistent AR rankings across seeds.\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"p1_ss_lora_only\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"SS training on LoRA-only checkpoint (no ThreadGate) with same hyperparameters (rho_max=0.3, same schedule) should achieve similar GAR improvement as SS+TG. If confirmed, this proves the SS fix is architecture-agnostic, strengthening the paper's mitigation story (the gap is caused by exposure bias in any auxiliary-loss setup, and SS fixes it regardless of gating mechanism).\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"phase2_switching\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"TF→AR switching at turn k (k=1..5) on ThreadGate s42 checkpoint. If GAR drops abruptly at the switch point (matching pure-AR level within 1 turn), it confirms exposure bias as instantaneous distribution shift rather than gradual KV cache drift. Staircase = exposure bias dominant; linear slope = KV drift dominant.\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"p1_llama_ss_eval\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"Llama SS (2-epoch) reduces the TF-AR GAR gap on Llama-3.1-8B, confirming SS as model-general mitigation (C4+C5). Eval: TF+AR N=50 β=0/3/5.\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"ss_tf_gar\\\": 0.477, \\\"ss_tf_ppl\\\": 2.82, \\\"ss_ar_b0_gar\\\": 0.1662, \\\"ss_ar_b0_ppl\\\": 1.37, \\\"ss_ar_b5_gar\\\": 0.7905, \\\"ss_ar_b5_ppl\\\": 1.81, \\\"base_ar_gar\\\": 0.0179, \\\"base_ar_ppl\\\": 1.22, \\\"tf_ar_gap\\\": 2.87}}, \\\"p1_llama_ss_training\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"SS is effective on Qwen (gap 8x to 1.4x). If SS also reduces the TF-AR gap on Llama-3.1-8B, it confirms SS as a model-general mitigation, strengthening C4 (mitigation) and C5 (cross-model) claims.\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"mmlu_eval_all\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"ThreadGate's per-layer gating and auxiliary GAR loss do not degrade the model's general language understanding capabilities. All fine-tuned variants (TG/UG/LO/PCGrad/SS) should maintain MMLU 5-shot accuracy within 1pp of the Base LoRA-only checkpoint, confirming that attention steering is additive rather than destructive.\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"base_qwen\\\": 0.7423, \\\"pcgrad_v9_s42\\\": 0.7386, \\\"ss_v8b_s42\\\": 0.7375, \\\"lo_s42\\\": 0.7357, \\\"tg_v7_s42\\\": 0.7347, \\\"ug_s42\\\": 0.7346}}, \\\"p2_llama_gradient_conflict\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"PCGrad fails to improve AR GAR on Llama-3.1-8B (as on Qwen), confirming cross-model that gradient conflict is not the root cause of the TF-AR gap, strengthening C2 (causal exclusion).\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"cos_sim_mean\\\": 0.0045, \\\"cos_sim_std\\\": 0.07, \\\"neg_cos_sim_layers_pct\\\": 53.1, \\\"mag_ratio_median\\\": 25.7, \\\"conclusion_note\\\": \\\"cos_sim≈0 indicates near-orthogonal (NOT conflict). Script conclusion text 'widespread conflict' is misleading — actual finding: NTP and GAR gradients are nearly orthogonal on Llama, consistent with Qwen pattern.\\\"}}, \\\"p1_tf_ar_kl_divergence\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"TF and AR attention distributions diverge more on GAR-relevant heads (high gate values) than non-relevant heads, providing mechanistic evidence that exposure bias selectively disrupts goal-attending computation rather than uniformly degrading attention.\\\", \\\"metrics\\\": {\\\"tg_delta_gar\\\": 0.0165, \\\"base_delta_gar\\\": 0.0122, \\\"tg_mean_kl\\\": 0.054, \\\"base_mean_kl\\\": 0.043, \\\"gate_kl_correlation\\\": 0.11, \\\"high_kl_layers\\\": \\\"L23-L27, L9\\\", \\\"gar_robustness_ours_tg_base_ratio\\\": 21.4, \\\"gar_robustness_goal_only_ratio\\\": 63, \\\"gar_robustness_ours_all_ratio\\\": 1.7, \\\"gar_robustness_ours_first_ratio\\\": 1.8}, \\\"conclusion\\\": \\\"success\\\"}, \\\"qwen15b_phase1_diag\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"GAR attention decay toward system-prompt goal tokens is a general phenomenon across model scales, not specific to 7B. Qwen-2.5-1.5B-Instruct should also show progressive GAR decline across conversation turns, confirming the phenomenon is architecture-level rather than scale-dependent.\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"d048_eval_ss_s456\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"SS s456 eval: TF + AR N=50 + bootstrap CI to complete 3-seed SS metrics. Together with s42 and s123, establishes mean±std for C2 reviewer requirement.\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"tf_gar_ours_mid\\\": 0.4964, \\\"tf_gar_dongre_mid\\\": 0.3862, \\\"ar_beta0_gar\\\": 0.4325, \\\"ar_beta0_ppl\\\": 1.4394, \\\"ar_beta3_gar\\\": 0.605, \\\"ar_beta3_ppl\\\": 1.5868, \\\"ar_beta5_gar\\\": 0.7157, \\\"ar_beta5_ppl\\\": 1.8045, \\\"n_convs_ar\\\": 50}}, \\\"d048_ss_s456\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"Scheduled sampling (ratio=0.3) with ThreadGate multi-seed (s456) to establish 3-seed mean±std for C2 reviewer requirement of at least 3 seeds\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"d048_eval_ss_s123\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"SS s123 eval: TF + AR N=50 + bootstrap CI to establish multi-seed SS metrics. Expect TF GAR ~0.50, AR GAR similar to s42 (0.347), confirming SS effectiveness across seeds.\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"tf_gar_ours\\\": 0.5536, \\\"tf_gar_dongre\\\": 0.4106, \\\"tf_ppl\\\": 2.6123, \\\"ar_beta0_gar\\\": 0.4231, \\\"ar_beta0_ppl\\\": 1.4408, \\\"ar_beta3_gar\\\": 0.5903, \\\"ar_beta3_ppl\\\": 1.607, \\\"ar_beta5_gar\\\": 0.7174, \\\"ar_beta5_ppl\\\": 1.7852, \\\"n_convs_tf\\\": 200, \\\"n_convs_ar\\\": 39}}, \\\"d048_ss_s123\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"Scheduled sampling (ratio=0.3) with ThreadGate multi-seed (s123) to establish 3-seed mean±std for C2 reviewer requirement. Corrected hyperparams matching d048_ss_s456.\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"d048_split_softmax_eval\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"Split-softmax (Li et al., COLM 2024) post-softmax rescaling recovers AR GAR without the PPL cost of pre-softmax additive steering, providing an alternative inference-time intervention that separates attention allocation from logit distribution.\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"d048_final_ar_eval\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"Unified AR N=50 eval across 6 conditions (Base/TG/UG/LO/PCGrad/SS) with bootstrap CI and Wilcoxon tests to establish statistically rigorous comparisons for all claims\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"beta0\\\": {\\\"base_gar\\\": 0.019, \\\"tg_gar\\\": 0.064, \\\"ug_gar\\\": 0.033, \\\"lo_gar\\\": 0.037, \\\"pcgrad_gar\\\": 0.03, \\\"ss_gar\\\": 0.347}, \\\"beta3\\\": {\\\"base_gar\\\": 0.531, \\\"tg_gar\\\": 0.556, \\\"ss_gar\\\": 0.593}, \\\"beta5\\\": {\\\"base_gar\\\": 0.704, \\\"tg_gar\\\": 0.727, \\\"ss_gar\\\": 0.717}, \\\"wilcoxon_beta0\\\": {\\\"tg_vs_base_p\\\": \\\"<0.001\\\", \\\"tg_vs_base_r\\\": 0.802, \\\"ss_vs_tg_p\\\": \\\"<0.001\\\", \\\"ss_vs_tg_r\\\": 0.869}, \\\"ppl\\\": {\\\"base\\\": 1.447, \\\"tg\\\": 1.432, \\\"ss\\\": 1.442}, \\\"n_convs\\\": 39}}, \\\"d048_eval_ss_s42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"D048 multi-seed SS s42 eval: TF + AR N=50 + bootstrap CI (curve[2:]) to establish mean±std for scheduled sampling. Expect TF GAR ~0.50, AR GAR gap < 2× (vs base ~31×), PPL stable.\\\", \\\"metrics\\\": {\\\"tf\\\": {\\\"base_gar_ours_mid\\\": 0.0128, \\\"base_gar_dongre_mid\\\": 0.0031, \\\"base_ppl\\\": 4.34, \\\"base_ntp\\\": 1.4, \\\"tg_gar_ours_mid\\\": 0.5025, \\\"tg_gar_dongre_mid\\\": 0.389, \\\"tg_ppl\\\": 2.78, \\\"tg_ntp\\\": 0.98, \\\"baseline_mid_gar\\\": 0.0122}, \\\"ar\\\": {\\\"gar_ours_mid\\\": 0.3887, \\\"gar_ours_ci_95\\\": [0.3692, 0.3934], \\\"ppl\\\": 1.35}, \\\"gap_ratio\\\": 1.29, \\\"n_conversations_tf\\\": 50, \\\"n_conversations_ar\\\": 5, \\\"bootstrap_turns\\\": \\\"curve[2:] (turns 3-T)\\\", \\\"note\\\": \\\"AR used hardcoded N=5, not N=50. Will be re-evaluated in final unified batch with eval_200.json N=50.\\\"}, \\\"conclusion\\\": \\\"success\\\"}, \\\"d048_ss_s42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"Scheduled sampling (ratio=0.3) with ThreadGate reduces the ~30× TF-AR GAR gap by exposing the model to its own generated text during training. Multi-seed run (s42) under D048 unified protocol to establish mean±std for statistical testing. SS is the strongest mitigation candidate (prior single-seed showed gap 31×→1.57×).\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"final_avg_loss\\\": 0.9326, \\\"final_ntp_loss\\\": 0.932, \\\"final_gar_loss\\\": 0.0007, \\\"gate_mean\\\": 0.9527, \\\"gate_std\\\": 0.0589, \\\"gate_min\\\": 0.7383, \\\"gate_min_layer\\\": \\\"L4\\\", \\\"gate_max\\\": 1, \\\"ss_usage\\\": \\\"4750/16000 (29.7%)\\\", \\\"ss_fallback\\\": 0, \\\"epochs_completed\\\": 3, \\\"wall_clock_s\\\": 23418, \\\"wall_clock_h\\\": 6.5}}, \\\"eval_llama_ar_n20\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"N=20 AR eval stabilizes Llama 3-way (Base/TG/LoRA-only) autoregressive GAR estimates. N=5 suffered from outlier influence (3/5 conv had GAR>0.4 outlier turns); N=20 provides robust mean±std.\\\", \\\"metrics\\\": {\\\"base\\\": {\\\"gar_ours_mean\\\": 0.0088, \\\"gar_ours_std\\\": 0.0056, \\\"gar_ours_median_per_conv\\\": 0.0093, \\\"gar_ours_median_per_turn_pool\\\": 0.0071, \\\"gar_ours_spike_ratio\\\": \\\"0%\\\", \\\"gar_dongre_mean\\\": 0.0049, \\\"gar_dongre_std\\\": 0.0013, \\\"gar_dongre_median\\\": 0.0047, \\\"ngar_ours_mid\\\": 0.1019, \\\"ngar_dongre_mid\\\": 0.1171, \\\"ppl\\\": 1.293, \\\"ppl_std\\\": 0.07, \\\"ntp_loss\\\": 0.2552}, \\\"tg\\\": {\\\"gar_ours_mean\\\": 0.0434, \\\"gar_ours_std\\\": 0.1002, \\\"gar_ours_median_per_conv\\\": 0.0179, \\\"gar_ours_median_per_turn_pool\\\": 0.0126, \\\"gar_ours_spike_ratio\\\": \\\"5% (2/40 turns GAR>=0.4)\\\", \\\"gar_dongre_mean\\\": 0.0183, \\\"gar_dongre_std\\\": 0.0198, \\\"gar_dongre_median\\\": 0.0152, \\\"ngar_ours_mid\\\": 0.5357, \\\"ngar_dongre_mid\\\": 0.4436, \\\"ppl\\\": 1.437, \\\"ppl_std\\\": 0.077, \\\"ntp_loss\\\": 0.3612}, \\\"lora_only\\\": {\\\"gar_ours_mean\\\": 0.0284, \\\"gar_ours_std\\\": 0.0481, \\\"gar_ours_median_per_conv\\\": 0.0184, \\\"gar_ours_median_per_turn_pool\\\": 0.0133, \\\"gar_ours_spike_ratio\\\": \\\"0%\\\", \\\"gar_dongre_mean\\\": 0.0205, \\\"gar_dongre_std\\\": 0.0241, \\\"gar_dongre_median\\\": 0.016, \\\"ngar_ours_mid\\\": 0.3488, \\\"ngar_dongre_mid\\\": 0.4997, \\\"ppl\\\": 1.419, \\\"ppl_std\\\": 0.075, \\\"ntp_loss\\\": 0.3483}, \\\"n_conversations\\\": 20, \\\"n_turns\\\": 4, \\\"mid_turns_definition\\\": \\\"turns 3-T (0-indexed avg_gar[2:], excluding turns 1-2). All 16 eval entries use same definition.\\\", \\\"stat_pool\\\": \\\"median_per_conv: median of 20 per-conversation mid-turn averages. median_per_turn_pool: median of 40 individual turn values (20 conv x 2 mid turns).\\\", \\\"ranking_gar_ours_mean\\\": \\\"TG(0.0434) > LO(0.0284) > Base(0.0088)\\\", \\\"ranking_gar_ours_median_per_conv\\\": \\\"TG(0.0179) ≈ LO(0.0184) > Base(0.0093)\\\", \\\"ranking_gar_ours_median_per_turn_pool\\\": \\\"TG(0.0126) ≈ LO(0.0133) > Base(0.0071)\\\", \\\"ranking_gar_dongre\\\": \\\"LO(0.0205) > TG(0.0183) > Base(0.0049)\\\", \\\"note\\\": \\\"Paper §5.5 cites median_per_conv (median of per-conversation mid-turn averages across N=20). median_per_turn_pool is the alternative statistic from pooled individual turns. Both confirm TG ≈ LO (zero-increment).\\\"}, \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_llama_lora_only_s42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"LoRA-only ablation (no gate) on Llama-3.1-8B: if TG's GAR improvement comes from the gate, LoRA-only should show minimal GAR recovery vs base.\\\", \\\"metrics\\\": {\\\"tf\\\": {\\\"gar_ours\\\": 0.4807, \\\"gar_dongre\\\": 0.0188, \\\"ngar_ours\\\": 11.8031, \\\"ngar_dongre\\\": 0.8261, \\\"ppl\\\": 2.6, \\\"ntp_loss\\\": 0.9366, \\\"n_conversations\\\": 50, \\\"n_turns\\\": 4}, \\\"ar\\\": {\\\"gar_ours\\\": 0.0617, \\\"gar_dongre\\\": 0.0226, \\\"ngar_ours\\\": 0.6065, \\\"ngar_dongre\\\": 0.2537, \\\"ppl\\\": 1.32, \\\"ntp_loss\\\": 0.2787, \\\"n_conversations\\\": 5, \\\"n_turns\\\": 10}, \\\"gap_ratio_gar_ours\\\": 7.79}, \\\"conclusion\\\": \\\"success\\\"}, \\\"llama_lora_only_s42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"Llama-3.1-8B LoRA-only baseline (gate=none, 无 gating 机制): 与 Llama TG s42 对比，验证 gating 对 Llama 的增量贡献。如果 LoRA-only GAR ≈ TG GAR → gating 零增量与 Qwen 结论一致（C5 跨模型）。\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"final_avg_loss\\\": 0.9288, \\\"final_avg_ntp\\\": 0.9279, \\\"final_avg_gar\\\": 0.0009, \\\"gate_fixed\\\": 1, \\\"gate_type\\\": \\\"none\\\", \\\"wall_clock_s\\\": 25317, \\\"wall_clock_h\\\": 7.03, \\\"epochs_completed\\\": 3}}, \\\"phase2_tg_s42_v6\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"smooth_saturation loss (-target*tanh(GAR/target), target=0.5) 提供有界但持续的 GAR 梯度，避免 maximize 的恒等退化（gate→1）和 hinge_target 的梯度消失（GAR达标后梯度=0）。预期：gate_std>0.05 的层间分化 + GAR 稳态在 0.3-0.5 + NTP loss 正常收敛 + 总 loss 为正。\\\", \\\"metrics\\\": {\\\"dryrun_step0_L_NTP\\\": 2.0275, \\\"dryrun_step0_L_GAR\\\": -0.0161, \\\"dryrun_step0_total_loss\\\": 2.0114, \\\"dryrun_step4_L_NTP\\\": 1.6544, \\\"dryrun_step4_L_GAR\\\": -0.0147, \\\"dryrun_step4_total_loss\\\": 1.6397, \\\"dryrun_gate_grad\\\": true, \\\"dryrun_gate_mean_init\\\": 0.8097, \\\"dryrun_gate_std_init\\\": 0.0341, \\\"dryrun_gate_min_init\\\": 0.6836, \\\"dryrun_gate_max_init\\\": 0.8672, \\\"dryrun_gate_mean_step5\\\": 0.8025, \\\"dryrun_gate_std_step5\\\": 0.0842, \\\"dryrun_gate_min_step5\\\": 0.5547, \\\"dryrun_gate_max_step5\\\": 0.9805, \\\"gs50_gate_mean\\\": 0.8117, \\\"gs50_gate_std\\\": 0.0612, \\\"gs50_gate_min\\\": 0.6836, \\\"gs50_gate_max\\\": 0.9805, \\\"gs100_gate_mean\\\": 0.8737, \\\"gs100_gate_std\\\": 0.0367, \\\"gs100_gate_min\\\": 0.8164, \\\"gs100_gate_max\\\": 0.9766, \\\"gs100_L_NTP\\\": 0.8151, \\\"gs100_L_GAR\\\": -0.158, \\\"gs100_total_loss\\\": 0.6571, \\\"gs100_profile_bottom3\\\": \\\"L12=0.816 L4=0.824 L13=0.824\\\", \\\"gs100_profile_top3\\\": \\\"L27=0.977 L26=0.961 L23=0.914\\\", \\\"gs143_L_GAR\\\": -0.3876, \\\"gs143_gate_mean\\\": 0.9227}, \\\"conclusion\\\": \\\"negative\\\"}, \\\"phase2_tg_s42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"ThreadGate (turn-conditional gating) 在 L_NTP+L_GAR 联合训练后，相比 Uniform Gate，mid-turn GAR recovery 高出 ≥3pp，验证 Cesaro 理论预测：position-conditional 干预优于 uniform 干预\\\", \\\"conclusion\\\": \\\"negative\\\", \\\"metrics\\\": {\\\"final_ntp_loss\\\": 0.94, \\\"final_gar_loss\\\": 0, \\\"gate_mean\\\": 0.988, \\\"gar_loss_zero_pct\\\": 87.6, \\\"epochs_completed\\\": 1.67, \\\"killed_reason\\\": \\\"SIGTERM by diagnose worker (unauthorized)\\\"}}, \\\"eval_v7_tg_s123\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"v7 TG s123 eval: 验证 s123 seed 的 TF-AR GAR gap 与 s42 一致（~32×），确认 multi-seed robustness\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"iid_tf\\\": {\\\"gar_ours_mid\\\": 0.5052, \\\"gar_dongre_mid\\\": 0.0119, \\\"ppl\\\": 2.7802, \\\"ntp\\\": 0.9752}, \\\"modelgen_ar\\\": {\\\"gar_ours_mid\\\": 0.0165, \\\"gar_dongre_mid\\\": 0.0177, \\\"ppl\\\": 1.3855, \\\"ntp\\\": 0.3223}, \\\"gap_ratio\\\": 30.6, \\\"comparison_s42\\\": {\\\"tf_gar_ours_delta\\\": 0.0017, \\\"ar_gar_ours_delta\\\": 0.0008, \\\"gap_ratio_delta\\\": -1.4}}}, \\\"eval_v8b_ss_s123\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"v8b SS model trained with s123 seed should reproduce s42 GAR metrics within acceptable gap_ratio [1.2x-2.5x] and no PPL degradation, confirming seed robustness of the scheduled sampling approach\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"iid\\\": {\\\"gar_ours\\\": 0.503, \\\"gar_dongre\\\": 0.394, \\\"ppl\\\": 2.781, \\\"ntp_loss\\\": 0.976, \\\"n_conv\\\": 50, \\\"n_turns\\\": 3}, \\\"modelgen\\\": {\\\"gar_ours\\\": 0.418, \\\"gar_dongre\\\": 0.441, \\\"ppl\\\": 1.389, \\\"ntp_loss\\\": 0.325, \\\"n_conv\\\": 5, \\\"n_turns\\\": 10}, \\\"gap_ratio\\\": 1.2, \\\"base_iid_ppl\\\": 4.338, \\\"base_modelgen_ppl\\\": 1.351}}, \\\"v7_tg_s123\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"v7 TG s42 已验证 ThreadGate 有效性，s123 验证 seed robustness。预期 gate profile 和 GAR 收敛模式与 s42 一致。\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"epoch_1\\\": {\\\"avg_loss\\\": 0.9447, \\\"avg_ntp_loss\\\": 0.9434, \\\"avg_gar_loss\\\": 0.0013, \\\"avg_div_loss\\\": 0}, \\\"epoch_2\\\": {\\\"avg_loss\\\": 0.9315, \\\"avg_ntp_loss\\\": 0.9305, \\\"avg_gar_loss\\\": 0.001, \\\"avg_div_loss\\\": 0}, \\\"final_gate\\\": {\\\"mean\\\": 0.9467, \\\"std\\\": 0.051, \\\"min\\\": 0.793, \\\"max\\\": 1}, \\\"final_gate_profile\\\": {\\\"L0\\\": 0.883, \\\"L1\\\": 0.793, \\\"L2\\\": 0.996, \\\"L3\\\": 0.988, \\\"L4\\\": 0.984, \\\"L5\\\": 0.797, \\\"L6\\\": 0.961, \\\"L7\\\": 0.918, \\\"L8\\\": 0.965, \\\"L9\\\": 0.934, \\\"L10\\\": 0.969, \\\"L11\\\": 0.918, \\\"L12\\\": 0.926, \\\"L13\\\": 0.941, \\\"L14\\\": 0.93, \\\"L15\\\": 0.965, \\\"L16\\\": 0.941, \\\"L17\\\": 0.91, \\\"L18\\\": 0.961, \\\"L19\\\": 0.965, \\\"L20\\\": 0.973, \\\"L21\\\": 0.988, \\\"L22\\\": 0.969, \\\"L23\\\": 0.98, \\\"L24\\\": 0.98, \\\"L25\\\": 0.984, \\\"L26\\\": 0.988, \\\"L27\\\": 1}, \\\"training_time_s\\\": 21425.2}}, \\\"v8b_ss_s123\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"v8b SS s42 成功（gap 32×→1.57×），s123 验证结果的 seed robustness。预期 model-gen GAR 同样显著提升，PPL 无恶化。\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"final_loss\\\": 0.9316, \\\"final_ntp_loss\\\": 0.9307, \\\"final_gar_loss\\\": 0.0009, \\\"final_gate_mean\\\": 0.9505, \\\"final_gate_std\\\": 0.0508, \\\"final_gate_min\\\": 0.7383, \\\"final_gate_max\\\": 1, \\\"ss_used_ratio\\\": 0.371, \\\"training_time_s\\\": 38773.4, \\\"epoch0_loss\\\": 1.0092, \\\"epoch1_loss\\\": 0.9444, \\\"epoch2_loss\\\": 0.9316}}, \\\"llama_ar_matched_eval\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"用 matched 设置 (N=50/T=4) 重跑 Llama AR eval，消除 TF/AR 设置差异。与 TF 结果对比得到可直接写入论文的 gap ratio，验证 TG 在 AR 模式下仍能提升 GAR。\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"ar_base_ours\\\": {\\\"mid_gar\\\": 0.0082, \\\"ngar\\\": 0.1, \\\"ppl\\\": 1.267}, \\\"ar_tg_ours\\\": {\\\"mid_gar\\\": 0.0388, \\\"ngar\\\": 0.493, \\\"ppl\\\": 1.413}, \\\"ar_base_dongre\\\": {\\\"mid_gar\\\": 0.0051, \\\"ngar\\\": 0.12, \\\"ppl\\\": 1.267}, \\\"ar_tg_dongre\\\": {\\\"mid_gar\\\": 0.018, \\\"ngar\\\": 0.431, \\\"ppl\\\": 1.413}, \\\"tf_reference\\\": {\\\"tf_tg_ours_ngar\\\": 11.88, \\\"tf_base_ours_ngar\\\": 0.388, \\\"tf_tg_ours_raw\\\": 0.4836, \\\"tf_tg_dongre_raw\\\": 0.018}, \\\"matched_gap_analysis\\\": {\\\"gar_ours_raw_gap\\\": \\\"12.5x (TF 0.484 / AR 0.039)\\\", \\\"gar_ours_ngar_gap\\\": \\\"24.1x (TF 11.88 / AR 0.493)\\\", \\\"gar_dongre_raw_gap\\\": \\\"1.002x (TF 0.018 / AR 0.018) — zero gap\\\", \\\"tg_over_base_ar_ours\\\": \\\"4.71x\\\", \\\"tg_over_base_ar_dongre\\\": \\\"3.54x\\\", \\\"conclusion\\\": \\\"GAR-ours TF-AR gap 12.5x (raw) / 24x (nGAR) is genuine exposure bias. GAR-Dongre zero gap (1.002x) confirms mechanism specificity: exposure bias selectively destroys learned goal-attention routing while leaving content-overlap-based attention unaffected.\\\"}}}, \\\"instruction_retention_test\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"Turn-level residual gating (β=3) preserves instruction-following ability across multi-turn conversations better than the baseline (β=0), because gating modulates residual contributions to retain earlier context signals rather than letting them decay through successive transformer layers.\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"late_turn_rate_beta0\\\": 0.759, \\\"late_turn_rate_beta3\\\": 0.87, \\\"late_turn_delta\\\": 0.111, \\\"mcnemar_chi2\\\": 3.125, \\\"mcnemar_p\\\": 0.0771, \\\"gar_compliance_r\\\": 0.2003, \\\"gar_compliance_p\\\": 0.007, \\\"category_content_constraint\\\": {\\\"beta0\\\": 0.619, \\\"beta3\\\": 0.857, \\\"delta\\\": 0.238}, \\\"category_count_constraint\\\": {\\\"beta0\\\": 1, \\\"beta3\\\": 1, \\\"delta\\\": 0}, \\\"category_format_constraint\\\": {\\\"beta0\\\": 1, \\\"beta3\\\": 1, \\\"delta\\\": 0}, \\\"category_position_constraint\\\": {\\\"beta0\\\": 0.667, \\\"beta3\\\": 0.733, \\\"delta\\\": 0.067}}}, \\\"llama_eval_s42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"Llama-3.1-8B TG eval: 如果 Llama TG 模型在 TF 模式下 GAR-ours 显著高于 AR 模式（如 Qwen v7 的 20-33x gap），则确认 training-inference GAR gap 跨模型泛化（C5）。同时测量 base model 作为 control。\\\", \\\"metrics\\\": {\\\"tf_base\\\": {\\\"gar_ours\\\": 0.0166, \\\"ngar_ours\\\": 0.3882, \\\"gar_dongre\\\": 0.0038, \\\"ngar_dongre\\\": 0.163, \\\"ppl\\\": 3.45, \\\"N\\\": 50, \\\"T\\\": 4}, \\\"tf_tg\\\": {\\\"gar_ours\\\": 0.4836, \\\"ngar_ours\\\": 11.8818, \\\"gar_dongre\\\": 0.018, \\\"ngar_dongre\\\": 0.7922, \\\"ppl\\\": 2.57, \\\"N\\\": 50, \\\"T\\\": 4}, \\\"ar_base\\\": {\\\"gar_ours\\\": 0.0086, \\\"ngar_ours\\\": 0.0798, \\\"gar_dongre\\\": 0.0118, \\\"ngar_dongre\\\": 0.1265, \\\"ppl\\\": 1.24, \\\"N\\\": 5, \\\"T\\\": 10}, \\\"ar_tg\\\": {\\\"gar_ours\\\": 0.0304, \\\"ngar_ours\\\": 0.2632, \\\"gar_dongre\\\": 0.0217, \\\"ngar_dongre\\\": 0.2459, \\\"ppl\\\": 1.32, \\\"N\\\": 5, \\\"T\\\": 10}, \\\"gap_ratio_tg_ours\\\": 15.9, \\\"gap_ratio_base_ours\\\": 1.93, \\\"gap_ratio_tg_dongre\\\": 0.83, \\\"vs_qwen_v7_gap_ratio\\\": 32.1, \\\"baseline_mid_gar\\\": 0.0122}, \\\"conclusion\\\": \\\"success\\\"}, \\\"llama_tg_s42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"在 Llama-3.1-8B-Instruct 上训练 ThreadGate（与 Qwen v7 相同配置），验证 C5：gating mechanism 和 GAR training-inference gap 跨模型泛化。如果 Llama TG 也出现 IID GAR ≈ target 但 model-gen GAR 坍塌 → 确认 exposure bias 的跨模型通用性。\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"epochs_completed\\\": 3, \\\"total_steps\\\": 3000, \\\"wall_clock_seconds\\\": 26212, \\\"wall_clock_hours\\\": 7.28, \\\"final_avg_loss\\\": 0.9233, \\\"final_avg_ntp\\\": 0.9224, \\\"final_avg_gar\\\": 0.0009, \\\"final_avg_div\\\": 0, \\\"final_gate_mean\\\": 0.9099, \\\"final_gate_std\\\": 0.0701, \\\"final_gate_min\\\": 0.7188, \\\"final_gate_max\\\": 0.9922, \\\"gate_profile_step3000\\\": {\\\"L0\\\": 0.957, \\\"L1\\\": 0.973, \\\"L2\\\": 0.977, \\\"L3\\\": 0.965, \\\"L4\\\": 0.992, \\\"L5\\\": 0.969, \\\"L6\\\": 0.957, \\\"L7\\\": 0.957, \\\"L8\\\": 0.961, \\\"L9\\\": 0.949, \\\"L10\\\": 0.938, \\\"L11\\\": 0.934, \\\"L12\\\": 0.969, \\\"L13\\\": 0.953, \\\"L14\\\": 0.957, \\\"L15\\\": 0.965, \\\"L16\\\": 0.953, \\\"L17\\\": 0.961, \\\"L18\\\": 0.922, \\\"L19\\\": 0.902, \\\"L20\\\": 0.883, \\\"L21\\\": 0.863, \\\"L22\\\": 0.836, \\\"L23\\\": 0.844, \\\"L24\\\": 0.809, \\\"L25\\\": 0.719, \\\"L26\\\": 0.762, \\\"L27\\\": 0.805, \\\"L28\\\": 0.801, \\\"L29\\\": 0.855, \\\"L30\\\": 0.898, \\\"L31\\\": 0.934}, \\\"checkpoint_size_gate_mb\\\": 4.2, \\\"checkpoint_size_lora_mb\\\": 26, \\\"gpu\\\": \\\"NVIDIA RTX PRO 6000 Blackwell\\\", \\\"vram_gb\\\": 102, \\\"mem_used_gb\\\": 63.4}}, \\\"attention_steering_gen_n50\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"N=5 gen steering 显示 β∈[2,5] phase transition (GAR 0.06→0.68)，但样本量不足以报告置信区间。N=50 conversations 应重现同一 phase transition pattern 并提供统计鲁棒的 mean±std，加固 C6 claim (attention steering as causal mechanism proof)。\\\", \\\"metrics\\\": {\\\"corrected\\\": true, \\\"aggregation\\\": \\\"per-conv mid_gar(turns 2-7), >=3 turns only\\\", \\\"beta_0.0\\\": {\\\"mid_gar\\\": 0.0641, \\\"mid_gar_std\\\": 0.0809, \\\"ppl\\\": 1.4324, \\\"ppl_std\\\": 0.1029, \\\"n_valid\\\": 39}, \\\"beta_2.0\\\": {\\\"mid_gar\\\": 0.128, \\\"mid_gar_std\\\": 0.1101, \\\"ppl\\\": 1.4822, \\\"ppl_std\\\": 0.1385, \\\"n_valid\\\": 39}, \\\"beta_3.0\\\": {\\\"mid_gar\\\": 0.5558, \\\"mid_gar_std\\\": 0.0601, \\\"ppl\\\": 1.5605, \\\"ppl_std\\\": 0.1719, \\\"n_valid\\\": 39}, \\\"beta_4.0\\\": {\\\"mid_gar\\\": 0.6439, \\\"mid_gar_std\\\": 0.0607, \\\"ppl\\\": 1.6674, \\\"ppl_std\\\": 0.2241, \\\"n_valid\\\": 39}, \\\"beta_5.0\\\": {\\\"mid_gar\\\": 0.7271, \\\"mid_gar_std\\\": 0.0605, \\\"ppl\\\": 1.7723, \\\"ppl_std\\\": 0.2693, \\\"n_valid\\\": 38}, \\\"beta_10.0\\\": {\\\"mid_gar\\\": 0.9612, \\\"mid_gar_std\\\": 0.0152, \\\"ppl\\\": 3.4517, \\\"ppl_std\\\": 1.7813, \\\"n_valid\\\": 39}, \\\"n_convs_total\\\": 50, \\\"n_convs_valid\\\": 39, \\\"mode\\\": \\\"gen\\\", \\\"phase_transition_range\\\": \\\"[2, 3]\\\"}, \\\"conclusion\\\": \\\"success\\\"}, \\\"phase2_tg_s42_v8b_resume\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"从 epoch_0 checkpoint resume v8b scheduled sampling 训练。SS 线性混合 0→0.5 teacher-forced + model-generated contexts。如果 model-gen context 上的 GAR 训练能缩小 30x training-inference gap → exposure bias mitigation 有效。成功标准：inference GAR 显著高于 v7 的 0.016 (至少 +1pp)，PPL 不恶化。\\\", \\\"metrics\\\": {\\\"training\\\": {\\\"total_steps\\\": 3000, \\\"epochs_completed\\\": 3, \\\"wall_clock_hours\\\": 8.1, \\\"final_loss\\\": 0.933, \\\"final_ntp_loss\\\": 0.9322, \\\"final_gar_loss\\\": 0.0008, \\\"final_gate_mean\\\": 0.9586, \\\"final_gate_std\\\": 0.0582, \\\"ss_ratio\\\": 0.5}, \\\"eval_iid\\\": {\\\"gar_ours\\\": 0.4983, \\\"gar_dongre\\\": 0.3855, \\\"ppl\\\": 2.78}, \\\"eval_modelgen\\\": {\\\"gar_ours\\\": 0.3177, \\\"gar_dongre\\\": 0.3533, \\\"ppl\\\": 1.38}, \\\"vs_v7\\\": {\\\"iid_gar_ours_delta\\\": -0.005, \\\"modelgen_gar_ours_delta\\\": 0.302, \\\"gap_ratio_v7\\\": 32, \\\"gap_ratio_v8b\\\": 1.57}}, \\\"conclusion\\\": \\\"success\\\"}, \\\"llama_phase1_gar_diag\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"Llama-3.1-8B-Instruct 在 multi-turn dialogue 中也应出现 goal attention decay（与 Qwen-2.5-7B 类似），确认 attention decay 是 transformer 架构通用现象而非模型特有。Phase 1 诊断：测量 base Llama 的 per-turn GAR profile。\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"per_turn_gar\\\": {\\\"turn_1\\\": 0.0263, \\\"turn_2\\\": 0.0183, \\\"turn_3\\\": 0.0087, \\\"turn_4\\\": 0.0055, \\\"turn_5\\\": 0.006, \\\"turn_6\\\": 0.0035, \\\"turn_7\\\": 0.0038, \\\"turn_8\\\": 0.0037, \\\"turn_9\\\": 0.005, \\\"turn_10\\\": 0.0026}, \\\"t1_t10_decay_pct\\\": 90.1, \\\"t1_mid38_drop_pct\\\": 80.2, \\\"n_topics\\\": 5, \\\"model\\\": \\\"Meta-Llama-3.1-8B-Instruct\\\", \\\"mode\\\": \\\"gen\\\", \\\"n_conversations\\\": 5, \\\"n_turns\\\": 10}}, \\\"eval_v8b_ss\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"Scheduled Sampling (linear 0→0.5 mixing of teacher-forced and model-gen contexts) closes the 30x training-inference GAR gap by reducing exposure bias, resulting in model-gen GAR significantly above v7 baseline (0.016) while preserving IID GAR and PPL.\\\", \\\"metrics\\\": {\\\"iid_gar_ours\\\": 0.4983, \\\"iid_gar_dongre\\\": 0.3855, \\\"iid_ppl\\\": 2.78, \\\"iid_ngar_ours\\\": 13.5, \\\"iid_ngar_dongre\\\": 22.68, \\\"modelgen_gar_ours\\\": 0.3177, \\\"modelgen_gar_dongre\\\": 0.3533, \\\"modelgen_ppl\\\": 1.38, \\\"modelgen_ngar_ours\\\": 4.47, \\\"modelgen_ngar_dongre\\\": 5.92, \\\"iid_turn1_gar_ours\\\": 0.5398, \\\"modelgen_turn1_gar_ours\\\": 0.4333}, \\\"conclusion\\\": \\\"success\\\"}, \\\"attention_steering_eval200_tf\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"N=200 TF 模式 attention steering 验证 β-GAR 关系的统计鲁棒性。在 teacher-forced context (无 exposure bias) 下，steering 效果应更温和（baseline GAR 已 ~0.50），但仍展示 β 调控 attention 的能力。与 N=5 gen 模式结果互补：tf 验证机制可控性，gen 验证因果闭环。\\\", \\\"metrics\\\": {\\\"beta_0.0\\\": {\\\"mid_gar\\\": 0.5353, \\\"ppl\\\": 2.62}, \\\"beta_2.0\\\": {\\\"mid_gar\\\": 0.6112, \\\"ppl\\\": 2.69}, \\\"beta_3.0\\\": {\\\"mid_gar\\\": 0.788, \\\"ppl\\\": 2.93}, \\\"beta_4.0\\\": {\\\"mid_gar\\\": 0.8165, \\\"ppl\\\": 3.49}, \\\"beta_5.0\\\": {\\\"mid_gar\\\": 0.8325, \\\"ppl\\\": 6.15}, \\\"beta_10.0\\\": {\\\"mid_gar\\\": 0.977, \\\"ppl\\\": 505.21}, \\\"n_convs\\\": 200, \\\"mode\\\": \\\"tf\\\"}, \\\"conclusion\\\": \\\"success\\\"}, \\\"trc_baseline_v7_tg\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"如果 exposure bias 对 auxiliary objectives 的破坏跨特征空间通用，那么 TRC (hidden state cos_sim) 在 model-gen 下也应出现与 GAR (attention 空间) 类似的 TF/gen gap。在 v7 TG / LoRA-only / base 三个 checkpoint 上测量 TRC baseline，确认 gap 是否存在。成功标准：gen TRC 显著低于 TF TRC。\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"v7_tg\\\": {\\\"tf_trc\\\": 0.3339, \\\"gen_trc\\\": 0.3323, \\\"trc_gap\\\": 0.0016, \\\"tf_tbp_ppl\\\": 1.05, \\\"gen_tbp_ppl\\\": 1.05}, \\\"lora_only\\\": {\\\"tf_trc\\\": 0.349, \\\"gen_trc\\\": 0.4106, \\\"trc_gap\\\": -0.0617, \\\"tf_tbp_ppl\\\": 9.5, \\\"gen_tbp_ppl\\\": 12}, \\\"base\\\": {\\\"tf_trc\\\": 0.1494, \\\"gen_trc\\\": 0.1494, \\\"trc_gap\\\": 0, \\\"tf_tbp_ppl\\\": 2.05, \\\"gen_tbp_ppl\\\": 2.05}}}, \\\"attention_steering_v7_tg_gen\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"推理时向 attention logits 注入 goal-position bias β 可恢复 autoregressive GAR。如果 GAR 从 0.015 显著提升 → 闭合因果环：exposure bias → attention 偏移 → GAR 坍塌 → 手动修正注意力 → GAR 恢复。扫描 β ∈ {0, 0.5, 1.0, 2.0, 5.0, 10.0}，成功标准：GAR > 0.1 且 PPL 不严重恶化。\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"beta_0.0\\\": {\\\"mid_turns_avg_gar\\\": 0.028, \\\"avg_ppl\\\": 1.409}, \\\"beta_0.5\\\": {\\\"mid_turns_avg_gar\\\": 0.0287, \\\"avg_ppl\\\": 1.387}, \\\"beta_1.0\\\": {\\\"mid_turns_avg_gar\\\": 0.0349, \\\"avg_ppl\\\": 1.36}, \\\"beta_2.0\\\": {\\\"mid_turns_avg_gar\\\": 0.062, \\\"avg_ppl\\\": 1.411}, \\\"beta_5.0\\\": {\\\"mid_turns_avg_gar\\\": 0.6795, \\\"avg_ppl\\\": 1.908}, \\\"beta_10.0\\\": {\\\"mid_turns_avg_gar\\\": 0.959, \\\"avg_ppl\\\": 4.22}, \\\"phase_transition_range\\\": \\\"[2, 5]\\\", \\\"baseline_gar\\\": 0.028, \\\"max_gar_at_acceptable_ppl\\\": 0.6795, \\\"max_gar_at_acceptable_ppl_beta\\\": 5}}, \\\"phase2_tg_s42_v8b_ss_fixed\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"Fixed scheduled sampling (D026 三项 bug 修复后): 线性从 0→0.5 混合 teacher-forced + model-generated contexts 计算 GAR loss。如果 model-gen context 上的 GAR 训练能缩小 30x training-inference gap → exposure bias mitigation 有效，paper 从纯 negative 升级为 diagnosis + initial remedy。超参与 v7 一致 (lambda_gar=1.0, MSE+gate_div)，唯一变量是 SS path。成功标准：inference GAR 显著高于 v7 的 0.016 (至少 +1pp)，PPL 不恶化。\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"phase2_tg_s42_v7\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"MSE 双向 loss (mean_GAR - target)² + gate diversity 正则 F.relu(min_std - gate_std) 从结构上解决恒等退化：MSE 在 GAR > target 时反向惩罚（不再单调推高），gate_div 直接强制层间分化。预期：gate_std 稳定 >0.05 + GAR 收敛到 target=0.5 附近 + NTP 正常收敛。\\\", \\\"metrics\\\": {\\\"eval_iid_ours_mid_gar\\\": 0.5035, \\\"eval_iid_dongre_mid_gar\\\": 0.0152, \\\"eval_iid_ppl\\\": 2.784, \\\"eval_heldout_ours_mid_gar\\\": 0.5035, \\\"eval_heldout_dongre_mid_gar\\\": 0.0152, \\\"eval_heldout_ppl\\\": 2.78, \\\"eval_modelgen_ours_mid_gar\\\": 0.0157, \\\"eval_modelgen_dongre_mid_gar\\\": 0.0194, \\\"eval_modelgen_ppl\\\": 1.36, \\\"gate_mean_final\\\": 0.9336, \\\"gate_std_final\\\": 0.0492}, \\\"conclusion\\\": \\\"success\\\"}, \\\"phase2_tg_s42_v9_pcgrad\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"PCGrad (Yu et al. NeurIPS 2020) 消除 NTP-GAR 梯度方向冲突后（仅对 gate 参数投影 NTP 梯度到 GAR 梯度正交平面），如果 30x training-inference GAR gap 仍在 → 因果证据证明 exposure bias（非梯度竞争）是 gap 根因。与 v7 对比：相同超参（lambda_gar=1.0, MSE+gate_div），唯一变量是梯度处理方式。成功标准：(1) 梯度 cos_sim 显著改善（从 v7 的 -0.089 提升到 ≥0），(2) 但推理 GAR 仍 ≈ v7 水平（0.016），证明梯度冲突不是 gap 的因。\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"eval_iid_ours_mid_gar\\\": 0.5002, \\\"eval_iid_dongre_mid_gar\\\": 0.0123, \\\"eval_iid_ppl\\\": 2.78, \\\"eval_iid_ntp\\\": 0.9752, \\\"eval_heldout_ours_mid_gar\\\": 0.5002, \\\"eval_heldout_dongre_mid_gar\\\": 0.0123, \\\"eval_heldout_ppl\\\": 2.78, \\\"eval_heldout_ntp\\\": 0.9752, \\\"eval_modelgen_ours_mid_gar\\\": 0.0151, \\\"eval_modelgen_dongre_mid_gar\\\": 0.0173, \\\"eval_modelgen_ppl\\\": 1.5, \\\"vs_v7_iid_ppl_diff\\\": 0.004, \\\"vs_v7_iid_gar_diff\\\": -0.0033}}, \\\"phase2_lora_only_s42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"LoRA-only baseline (gate 固定 1.0，无 gating 机制) 在相同 MSE+NTP loss 下 GAR 应低于 ThreadGate (v7)。如果 LoRA-only 也能训到 GAR~0.5，则 gating 机制贡献为零，paper story 不成立。关键对比：LoRA-only 的 GAR 收敛值 vs v7 的 0.48。\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"epochs_completed\\\": 3, \\\"global_steps\\\": 3000, \\\"training_time_seconds\\\": 20588.6, \\\"training_time_hours\\\": 5.7, \\\"gate_fixed\\\": 1, \\\"gate_type_actual\\\": \\\"none\\\", \\\"final_lora_size_mb\\\": 20, \\\"eval_modelgen_ours_mid_gar\\\": 0.0245, \\\"eval_modelgen_dongre_mid_gar\\\": 0.0185, \\\"eval_modelgen_ppl\\\": 1.371}}, \\\"phase2_ug_s42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"Uniform gating baseline: per-layer independent gates without turn conditioning (content-dependent only), to isolate whether ThreadGate's turn-conditioned gating provides benefit over content-only residual scaling. Same training setup as v7 but with gate-type=uniform.\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"epoch0_avg_loss\\\": 1.0019, \\\"epoch0_avg_ntp\\\": 0.9755, \\\"epoch0_avg_gar\\\": 0.0259, \\\"epoch0_avg_div\\\": 0.0005, \\\"epoch1_avg_loss\\\": 0.9447, \\\"epoch1_avg_ntp\\\": 0.9435, \\\"epoch1_avg_gar\\\": 0.0013, \\\"epoch1_avg_div\\\": 0, \\\"epoch2_avg_loss\\\": 0.9319, \\\"epoch2_avg_ntp\\\": 0.9309, \\\"epoch2_avg_gar\\\": 0.001, \\\"epoch2_avg_div\\\": 0, \\\"final_gate_mean\\\": 0.9598, \\\"final_gate_std\\\": 0.0518, \\\"final_gate_min\\\": 0.7773, \\\"final_gate_max\\\": 1, \\\"final_profile_L3\\\": 0.777, \\\"final_profile_L5\\\": 0.812, \\\"final_profile_L0\\\": 0.875, \\\"final_profile_L27\\\": 1, \\\"training_time_seconds\\\": 21994.5, \\\"training_time_hours\\\": 6.1, \\\"global_steps\\\": 7950, \\\"unexpected_per_layer_variation\\\": true, \\\"eval_modelgen_ours_mid_gar\\\": 0.0149, \\\"eval_modelgen_dongre_mid_gar\\\": 0.0185, \\\"eval_modelgen_ppl\\\": 1.396}}, \\\"phase2_tg_s42_v8_schedsampling\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"Scheduled sampling 应用到 GAR loss（线性从 0→0.5 混合 teacher-forced + model-generated contexts）能缩小 v7 的 30x training-inference GAR gap。机制：在 model-generated context 上计算 GAR loss 迫使 attention pattern 适应推理时分布，直接 address teacher-forcing distribution shift。成功标准：inference GAR 显著高于 v7 的 0.016，PPL 不显著恶化（≤2.78+0.2）。\\\", \\\"conclusion\\\": \\\"failed\\\", \\\"metrics\\\": {\\\"killed_at_microstep\\\": 1950, \\\"total_microsteps\\\": 24000, \\\"completion_pct\\\": 8.1, \\\"global_step_approx\\\": 244, \\\"total_global_steps\\\": 3000, \\\"ss_steps_observed\\\": 1, \\\"tf_lgar_mean_step850_1400\\\": 0.0062, \\\"tf_lgar_std\\\": 0.0082, \\\"tf_lgar_collapse_step\\\": 800, \\\"gate_mean_final\\\": 0.93, \\\"ss_ratio_at_kill\\\": 0.081, \\\"crash_reason\\\": \\\"killed by director: SS path code bug (D026) makes experiment invalid, GPU needed for PCGrad\\\", \\\"design_flaw_ss_ramp_too_slow\\\": true, \\\"design_flaw_no_ss_tf_separate_logging\\\": true}}, \\\"analysis_attention_heatmap\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"四模型（Base/TG/UG/LoRA-only）的 goal attention 衰减模式是否一致？如果 TG 的 attention decay 与 LoRA-only 无差异，则 gating 机制对 attention 分布零增量。\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"base_mean_goal_attn\\\": 0.0136, \\\"base_decay\\\": 0.875, \\\"tg_mean_goal_attn\\\": 0.0232, \\\"tg_decay\\\": 0.777, \\\"ug_mean_goal_attn\\\": 0.0216, \\\"ug_decay\\\": 0.803, \\\"lora_mean_goal_attn\\\": 0.0216, \\\"lora_decay\\\": 0.81, \\\"gating_incremental_benefit\\\": \\\"none\\\"}}, \\\"analysis_gradient_conflict\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"NTP-GAR 梯度冲突在 v7 训练过程中是否逐层普遍存在？量化 cos_sim 和 magnitude ratio 的演化，验证 NTP 是否在训练中逐渐完全压制 GAR 信号。\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"epoch0_cos_sim\\\": -0.089, \\\"epoch1_cos_sim\\\": -0.054, \\\"epoch2_cos_sim\\\": -0.042, \\\"epoch0_neg_layers_pct\\\": 78.6, \\\"epoch1_neg_layers_pct\\\": 71.4, \\\"epoch2_neg_layers_pct\\\": 67.9, \\\"epoch0_mag_ratio\\\": 7.5, \\\"epoch1_mag_ratio\\\": 13.7, \\\"epoch2_mag_ratio\\\": 14.7}}, \\\"phase2_4way_eval_heldout\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"四路消融的三路趋同结论（TG≈UG≈LoRA-only，gating 零增量）在 held-out eval 数据（idx≥8000，与训练集无重叠）上复现，排除数据重叠 confound。预期：相对比较保持（三路趋同），绝对 GAR 值可能变化。\\\", \\\"metrics\\\": {\\\"base_ours_mid_gar\\\": 0.0128, \\\"base_ours_recovery_pp\\\": 0.06, \\\"base_dongre_mid_gar\\\": 0.0031, \\\"base_dongre_recovery_pp\\\": -0.91, \\\"base_ppl\\\": 4.34, \\\"base_ntp\\\": 1.4045, \\\"tg_ours_mid_gar\\\": 0.5035, \\\"tg_ours_recovery_pp\\\": 49.13, \\\"tg_dongre_mid_gar\\\": 0.0152, \\\"tg_dongre_recovery_pp\\\": 0.3, \\\"tg_ppl\\\": 2.78, \\\"tg_ntp\\\": 0.9771, \\\"ug_ours_mid_gar\\\": 0.5053, \\\"ug_ours_recovery_pp\\\": 49.31, \\\"ug_dongre_mid_gar\\\": 0.0124, \\\"ug_dongre_recovery_pp\\\": 0.02, \\\"ug_ppl\\\": 2.78, \\\"ug_ntp\\\": 0.9752, \\\"lora_ours_mid_gar\\\": 0.4978, \\\"lora_ours_recovery_pp\\\": 48.56, \\\"lora_dongre_mid_gar\\\": 0.0132, \\\"lora_dongre_recovery_pp\\\": 0.1, \\\"lora_ppl\\\": 2.78, \\\"lora_ntp\\\": 0.9771, \\\"three_way_convergence_confirmed\\\": true, \\\"gar_ours_spread_pp\\\": 0.75, \\\"ppl_spread\\\": 0, \\\"data_overlap\\\": false}, \\\"conclusion\\\": \\\"success\\\"}, \\\"phase2_4way_eval\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"Turn-residual gating (TRG) improves multi-turn response quality over LoRA-only and base model baselines because it selectively amplifies conversational context signals, which should manifest as higher GAR scores across 4 conditions (base, base+TRG, LoRA, LoRA+TRG).\\\", \\\"conclusion\\\": \\\"negative\\\", \\\"metrics\\\": {\\\"base_ours_mid_gar\\\": 0.0107, \\\"base_ours_recovery_pp\\\": -0.15, \\\"base_dongre_mid_gar\\\": 0.003, \\\"base_dongre_recovery_pp\\\": -0.92, \\\"base_ppl\\\": 4.23, \\\"base_ntp\\\": 1.4162, \\\"tg_ours_mid_gar\\\": 0.4866, \\\"tg_ours_recovery_pp\\\": 47.44, \\\"tg_dongre_mid_gar\\\": 0.0157, \\\"tg_dongre_recovery_pp\\\": 0.35, \\\"tg_ppl\\\": 2.63, \\\"tg_ntp\\\": 0.9484, \\\"ug_ours_mid_gar\\\": 0.4923, \\\"ug_ours_recovery_pp\\\": 48.01, \\\"ug_dongre_mid_gar\\\": 0.013, \\\"ug_dongre_recovery_pp\\\": 0.08, \\\"ug_ppl\\\": 2.62, \\\"ug_ntp\\\": 0.9433, \\\"lora_ours_mid_gar\\\": 0.486, \\\"lora_ours_recovery_pp\\\": 47.39, \\\"lora_dongre_mid_gar\\\": 0.0137, \\\"lora_dongre_recovery_pp\\\": 0.15, \\\"lora_ppl\\\": 2.63, \\\"lora_ntp\\\": 0.9482, \\\"route_b_confirmed\\\": true, \\\"gating_incremental_benefit\\\": \\\"none\\\"}}, \\\"phase2_tg_s42_v5\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"重新平衡超参（λ=1.0 降 GAR 贡献至 ~50%，init_bias=1.5 使 sigmoid≈0.82 接近正常模型行为，gate_lr_multiplier=10 保持）能在 3-epoch 全量训练中产生有意义的 gate 分化（gate_std>0.05），同时 GAR 稳态在 0.1-0.5（非病态饱和），NTP loss 正常收敛，总 loss 保持正值\\\", \\\"metrics\\\": {\\\"step2000_gate_std\\\": 0.0225, \\\"step2000_gate_mean\\\": 0.9586, \\\"step2000_gate_min\\\": 0.9062, \\\"step2000_gate_max\\\": 0.9961, \\\"step2000_L_GAR\\\": -0.8977, \\\"step2000_L_NTP\\\": 0.7611, \\\"step2000_total_loss\\\": -0.1365, \\\"step2400_gate_std\\\": 0.0219, \\\"step2400_gate_mean\\\": 0.9651, \\\"step2400_gate_min\\\": 0.918, \\\"step2400_gate_max\\\": 0.9961, \\\"step2400_profile\\\": \\\"L0=0.918 L12=0.918 L13=0.926 L1=0.996 L26=0.996\\\", \\\"L_GAR_saturated_at\\\": -0.91, \\\"gate_range_compression\\\": \\\"0.918-0.996\\\"}, \\\"conclusion\\\": \\\"negative\\\"}, \\\"phase2_tg_s42_v4\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"重新平衡超参（λ=1.0 降 GAR 贡献至 ~50%，init_bias=1.5 使 sigmoid≈0.82 接近正常模型行为，gate_lr_multiplier=10 保持）能在 3-epoch 全量训练中产生有意义的 gate 分化（gate_std>0.05），同时 GAR 稳态在 0.1-0.5（非病态饱和），NTP loss 正常收敛，总 loss 保持正值\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"phase2_tg_s42_v3b\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"λ=10 + gate_lr=10x + init_bias=0.0 (sigmoid=0.5) 能否驱动 gate 产生 layer 间分化 (gate_std>0.05)？如果 500 步后 gate_std<0.02 且无选择性 → GAR-driven gating 梯度路径确认失败，需要 pivot\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"gate_std_final\\\": 0.087, \\\"gate_mean_final\\\": 0.9388, \\\"gate_min_final\\\": 0.5352, \\\"gate_max_final\\\": 0.9922, \\\"L4_gate\\\": 0.535, \\\"L0_gate\\\": 0.777, \\\"L_NTP_final\\\": 0.7787, \\\"L_GAR_final\\\": -0.9606, \\\"elapsed_seconds\\\": 3565.9, \\\"optimizer_steps\\\": 500, \\\"gate_grad_received\\\": true}}, \\\"phase2_tg_s42_v3\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"ThreadGate + maximize GAR loss (L_GAR=-mean(GAR)) 提供持续非零梯度，避免 hinge loss 的退化平衡点，gate 值应随训练下降（学习到选择性干预），同时 NTP loss 正常收敛\\\", \\\"conclusion\\\": \\\"negative\\\", \\\"metrics\\\": {\\\"gate_mean_step0\\\": 0.8743, \\\"gate_mean_step500\\\": 0.8761, \\\"gate_delta\\\": 0.004, \\\"gate_std\\\": 0.001, \\\"final_ntp_loss\\\": 0.94, \\\"final_gar_loss\\\": -0.019, \\\"gar_contribution_pct\\\": \\\"2-4%\\\", \\\"diagnosis\\\": \\\"gate frozen, GAR indirect gradient too weak\\\"}}, \\\"phase2_tg_s42_v2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"ThreadGate + 修复后的 cumulative GAR loss (ε=0.001) 在 L_NTP+L_GAR 联合训练后，mid-turn GAR recovery 应显著优于 v1 (NTP-only baseline)，验证 GAR loss 的有效性\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"phase1_gar_diag\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"Qwen2.5-7B-Instruct 在 10-turn 多轮对话中，中间 turns (3-8) 的 GAR (Goal Accessibility Ratio) 相对 turn-1 下降 ≥15%，表明模型对 system prompt 中目标 token 的注意力随对话进行显著衰减\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"turn1_avg_gar\\\": 0.0418, \\\"mid_turns_avg_gar\\\": 0.0122, \\\"relative_drop\\\": 0.708, \\\"num_conversations\\\": 5, \\\"num_turns\\\": 10, \\\"per_turn_avg_gar\\\": [0.0418, 0.0241, 0.0224, 0.013, 0.0133, 0.0086, 0.0078, 0.008, 0.0157, 0.0064]}}}, \\\"count\\\": 53, \\\"total\\\": 53, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.1655}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {\"phase1a_multiseed_qwen\": {\"status\": \"DONE\", \"hypothesis\": \"Multi-seed (s123, s456) training across 5 Qwen conditions (PCGrad, UG, LoRA-only, TG, SS) to establish mean±std for all claims. 8 training runs + AR eval N≥50 each. Expect TF convergence (GAR~0.50) and consistent AR rankings across seeds.\", \"conclusion\": \"killed\"}, \"p1_ss_lora_only\": {\"status\": \"DONE\", \"hypothesis\": \"SS training on LoRA-only checkpoint (no ThreadGate) with same hyperparameters (rho_max=0.3, same schedule) should achieve similar GAR improvement as SS+TG. If confirmed, this proves the SS fix is architecture-agnostic, strengthening the paper's mitigation story (the gap is caused by exposure bias in any auxiliary-loss setup, and SS fixes it regardless of gating mechanism).\", \"conclusion\": \"killed\"}, \"phase2_switching\": {\"status\": \"DONE\", \"hypothesis\": \"TF→AR switching at turn k (k=1..5) on ThreadGate s42 checkpoint. If GAR drops abruptly at the switch point (matching pure-AR level within 1 turn), it confirms exposure bias as instantaneous distribution shift rather than gradual KV cache drift. Staircase = exposure bias dominant; linear slope = KV drift dominant.\", \"conclusion\": \"killed\"}, \"p1_llama_ss_eval\": {\"status\": \"DONE\", \"hypothesis\": \"Llama SS (2-epoch) reduces the TF-AR GAR gap on Llama-3.1-8B, confirming SS as model-general mitigation (C4+C5). Eval: TF+AR N=50 β=0/3/5.\", \"conclusion\": \"success\", \"metrics\": {\"ss_tf_gar\": 0.477, \"ss_tf_ppl\": 2.82, \"ss_ar_b0_gar\": 0.1662, \"ss_ar_b0_ppl\": 1.37, \"ss_ar_b5_gar\": 0.7905, \"ss_ar_b5_ppl\": 1.81, \"base_ar_gar\": 0.0179, \"base_ar_ppl\": 1.22, \"tf_ar_gap\": 2.87}}, \"p1_llama_ss_training\": {\"status\": \"DONE\", \"hypothesis\": \"SS is effective on Qwen (gap 8x to 1.4x). If SS also reduces the TF-AR gap on Llama-3.1-8B, it confirms SS as a model-general mitigation, strengthening C4 (mitigation) and C5 (cross-model) claims.\", \"conclusion\": \"success\"}, \"mmlu_eval_all\": {\"status\": \"DONE\", \"hypothesis\": \"ThreadGate's per-layer gating and auxiliary GAR loss do not degrade the model's general language understanding capabilities. All fine-tuned variants (TG/UG/LO/PCGrad/SS) should maintain MMLU 5-shot accuracy within 1pp of the Base LoRA-only checkpoint, confirming that attention steering is additive rather than destructive.\", \"conclusion\": \"success\", \"metrics\": {\"base_qwen\": 0.7423, \"pcgrad_v9_s42\": 0.7386, \"ss_v8b_s42\": 0.7375, \"lo_s42\": 0.7357, \"tg_v7_s42\": 0.7347, \"ug_s42\": 0.7346}}, \"p2_llama_gradient_conflict\": {\"status\": \"DONE\", \"hypothesis\": \"PCGrad fails to improve AR GAR on Llama-3.1-8B (as on Qwen), confirming cross-model that gradient conflict is not the root cause of the TF-AR gap, strengthening C2 (causal exclusion).\", \"conclusion\": \"success\", \"metrics\": {\"cos_sim_mean\": 0.0045, \"cos_sim_std\": 0.07, \"neg_cos_sim_layers_pct\": 53.1, \"mag_ratio_median\": 25.7, \"conclusion_note\": \"cos_sim≈0 indicates near-orthogonal (NOT conflict). Script conclusion text 'widespread conflict' is misleading — actual finding: NTP and GAR gradients are nearly orthogonal on Llama, consistent with Qwen pattern.\"}}, \"p1_tf_ar_kl_divergence\": {\"status\": \"DONE\", \"hypothesis\": \"TF and AR attention distributions diverge more on GAR-relevant heads (high gate values) than non-relevant heads, providing mechanistic evidence that exposure bias selectively disrupts goal-attending computation rather than uniformly degrading attention.\", \"metrics\": {\"tg_delta_gar\": 0.0165, \"base_delta_gar\": 0.0122, \"tg_mean_kl\": 0.054, \"base_mean_kl\": 0.043, \"gate_kl_correlation\": 0.11, \"high_kl_layers\": \"L23-L27, L9\", \"gar_robustness_ours_tg_base_ratio\": 21.4, \"gar_robustness_goal_only_ratio\": 63, \"gar_robustness_ours_all_ratio\": 1.7, \"gar_robustness_ours_first_ratio\": 1.8}, \"conclusion\": \"success\"}, \"qwen15b_phase1_diag\": {\"status\": \"DONE\", \"hypothesis\": \"GAR attention decay toward system-prompt goal tokens is a general phenomenon across model scales, not specific to 7B. Qwen-2.5-1.5B-Instruct should also show progressive GAR decline across conversation turns, confirming the phenomenon is architecture-level rather than scale-dependent.\", \"conclusion\": \"success\"}, \"d048_eval_ss_s456\": {\"status\": \"DONE\", \"hypothesis\": \"SS s456 eval: TF + AR N=50 + bootstrap CI to complete 3-seed SS metrics. Together with s42 and s123, establishes mean±std for C2 reviewer requirement.\", \"conclusion\": \"success\", \"metrics\": {\"tf_gar_ours_mid\": 0.4964, \"tf_gar_dongre_mid\": 0.3862, \"ar_beta0_gar\": 0.4325, \"ar_beta0_ppl\": 1.4394, \"ar_beta3_gar\": 0.605, \"ar_beta3_ppl\": 1.5868, \"ar_beta5_gar\": 0.7157, \"ar_beta5_ppl\": 1.8045, \"n_convs_ar\": 50}}, \"d048_ss_s456\": {\"status\": \"DONE\", \"hypothesis\": \"Scheduled sampling (ratio=0.3) with ThreadGate multi-seed (s456) to establish 3-seed mean±std for C2 reviewer requirement of at least 3 seeds\", \"conclusion\": \"success\"}, \"d048_eval_ss_s123\": {\"status\": \"DONE\", \"hypothesis\": \"SS s123 eval: TF + AR N=50 + bootstrap CI to establish multi-seed SS metrics. Expect TF GAR ~0.50, AR GAR similar to s42 (0.347), confirming SS effectiveness across seeds.\", \"conclusion\": \"success\", \"metrics\": {\"tf_gar_ours\": 0.5536, \"tf_gar_dongre\": 0.4106, \"tf_ppl\": 2.6123, \"ar_beta0_gar\": 0.4231, \"ar_beta0_ppl\": 1.4408, \"ar_beta3_gar\": 0.5903, \"ar_beta3_ppl\": 1.607, \"ar_beta5_gar\": 0.7174, \"ar_beta5_ppl\": 1.7852, \"n_convs_tf\": 200, \"n_convs_ar\": 39}}, \"d048_ss_s123\": {\"status\": \"DONE\", \"hypothesis\": \"Scheduled sampling (ratio=0.3) with ThreadGate multi-seed (s123) to establish 3-seed mean±std for C2 reviewer requirement. Corrected hyperparams matching d048_ss_s456.\", \"conclusion\": \"success\"}, \"d048_split_softmax_eval\": {\"status\": \"DONE\", \"hypothesis\": \"Split-softmax (Li et al., COLM 2024) post-softmax rescaling recovers AR GAR without the PPL cost of pre-softmax additive steering, providing an alternative inference-time intervention that separates attention allocation from logit distribution.\", \"conclusion\": \"failed\"}, \"d048_final_ar_eval\": {\"status\": \"DONE\", \"hypothesis\": \"Unified AR N=50 eval across 6 conditions (Base/TG/UG/LO/PCGrad/SS) with bootstrap CI and Wilcoxon tests to establish statistically rigorous comparisons for all claims\", \"conclusion\": \"success\", \"metrics\": {\"beta0\": {\"base_gar\": 0.019, \"tg_gar\": 0.064, \"ug_gar\": 0.033, \"lo_gar\": 0.037, \"pcgrad_gar\": 0.03, \"ss_gar\": 0.347}, \"beta3\": {\"base_gar\": 0.531, \"tg_gar\": 0.556, \"ss_gar\": 0.593}, \"beta5\": {\"base_gar\": 0.704, \"tg_gar\": 0.727, \"ss_gar\": 0.717}, \"wilcoxon_beta0\": {\"tg_vs_base_p\": \"<0.001\", \"tg_vs_base_r\": 0.802, \"ss_vs_tg_p\": \"<0.001\", \"ss_vs_tg_r\": 0.869}, \"ppl\": {\"base\": 1.447, \"tg\": 1.432, \"ss\": 1.442}, \"n_convs\": 39}}, \"d048_eval_ss_s42\": {\"status\": \"DONE\", \"hypothesis\": \"D048 multi-seed SS s42 eval: TF + AR N=50 + bootstrap CI (curve[2:]) to establish mean±std for scheduled sampling. Expect TF GAR ~0.50, AR GAR gap < 2× (vs base ~31×), PPL stable.\", \"metrics\": {\"tf\": {\"base_gar_ours_mid\": 0.0128, \"base_gar_dongre_mid\": 0.0031, \"base_ppl\": 4.34, \"base_ntp\": 1.4, \"tg_gar_ours_mid\": 0.5025, \"tg_gar_dongre_mid\": 0.389, \"tg_ppl\": 2.78, \"tg_ntp\": 0.98, \"baseline_mid_gar\": 0.0122}, \"ar\": {\"gar_ours_mid\": 0.3887, \"gar_ours_ci_95\": [0.3692, 0.3934], \"ppl\": 1.35}, \"gap_ratio\": 1.29, \"n_conversations_tf\": 50, \"n_conversations_ar\": 5, \"bootstrap_turns\": \"curve[2:] (turns 3-T)\", \"note\": \"AR used hardcoded N=5, not N=50. Will be re-evaluated in final unified batch with eval_200.json N=50.\"}, \"conclusion\": \"success\"}, \"d048_ss_s42\": {\"status\": \"DONE\", \"hypothesis\": \"Scheduled sampling (ratio=0.3) with ThreadGate reduces the ~30× TF-AR GAR gap by exposing the model to its own generated text during training. Multi-seed run (s42) under D048 unified protocol to establish mean±std for statistical testing. SS is the strongest mitigation candidate (prior single-seed showed gap 31×→1.57×).\", \"conclusion\": \"success\", \"metrics\": {\"final_avg_loss\": 0.9326, \"final_ntp_loss\": 0.932, \"final_gar_loss\": 0.0007, \"gate_mean\": 0.9527, \"gate_std\": 0.0589, \"gate_min\": 0.7383, \"gate_min_layer\": \"L4\", \"gate_max\": 1, \"ss_usage\": \"4750/16000 (29.7%)\", \"ss_fallback\": 0, \"epochs_completed\": 3, \"wall_clock_s\": 23418, \"wall_clock_h\": 6.5}}, \"eval_llama_ar_n20\": {\"status\": \"DONE\", \"hypothesis\": \"N=20 AR eval stabilizes Llama 3-way (Base/TG/LoRA-only) autoregressive GAR estimates. N=5 suffered from outlier influence (3/5 conv had GAR>0.4 outlier turns); N=20 provides robust mean±std.\", \"metrics\": {\"base\": {\"gar_ours_mean\": 0.0088, \"gar_ours_std\": 0.0056, \"gar_ours_median_per_conv\": 0.0093, \"gar_ours_median_per_turn_pool\": 0.0071, \"gar_ours_spike_ratio\": \"0%\", \"gar_dongre_mean\": 0.0049, \"gar_dongre_std\": 0.0013, \"gar_dongre_median\": 0.0047, \"ngar_ours_mid\": 0.1019, \"ngar_dongre_mid\": 0.1171, \"ppl\": 1.293, \"ppl_std\": 0.07, \"ntp_loss\": 0.2552}, \"tg\": {\"gar_ours_mean\": 0.0434, \"gar_ours_std\": 0.1002, \"gar_ours_median_per_conv\": 0.0179, \"gar_ours_median_per_turn_pool\": 0.0126, \"gar_ours_spike_ratio\": \"5% (2/40 turns GAR>=0.4)\", \"gar_dongre_mean\": 0.0183, \"gar_dongre_std\": 0.0198, \"gar_dongre_median\": 0.0152, \"ngar_ours_mid\": 0.5357, \"ngar_dongre_mid\": 0.4436, \"ppl\": 1.437, \"ppl_std\": 0.077, \"ntp_loss\": 0.3612}, \"lora_only\": {\"gar_ours_mean\": 0.0284, \"gar_ours_std\": 0.0481, \"gar_ours_median_per_conv\": 0.0184, \"gar_ours_median_per_turn_pool\": 0.0133, \"gar_ours_spike_ratio\": \"0%\", \"gar_dongre_mean\": 0.0205, \"gar_dongre_std\": 0.0241, \"gar_dongre_median\": 0.016, \"ngar_ours_mid\": 0.3488, \"ngar_dongre_mid\": 0.4997, \"ppl\": 1.419, \"ppl_std\": 0.075, \"ntp_loss\": 0.3483}, \"n_conversations\": 20, \"n_turns\": 4, \"mid_turns_definition\": \"turns 3-T (0-indexed avg_gar[2:], excluding turns 1-2). All 16 eval entries use same definition.\", \"stat_pool\": \"median_per_conv: median of 20 per-conversation mid-turn averages. median_per_turn_pool: median of 40 individual turn values (20 conv x 2 mid turns).\", \"ranking_gar_ours_mean\": \"TG(0.0434) > LO(0.0284) > Base(0.0088)\", \"ranking_gar_ours_median_per_conv\": \"TG(0.0179) ≈ LO(0.0184) > Base(0.0093)\", \"ranking_gar_ours_median_per_turn_pool\": \"TG(0.0126) ≈ LO(0.0133) > Base(0.0071)\", \"ranking_gar_dongre\": \"LO(0.0205) > TG(0.0183) > Base(0.0049)\", \"note\": \"Paper §5.5 cites median_per_conv (median of per-conversation mid-turn averages across N=20). median_per_turn_pool is the alternative statistic from pooled individual turns. Both confirm TG ≈ LO (zero-increment).\"}, \"conclusion\": \"success\"}, \"eval_llama_lora_only_s42\": {\"status\": \"DONE\", \"hypothesis\": \"LoRA-only ablation (no gate) on Llama-3.1-8B: if TG's GAR improvement comes from the gate, LoRA-only should show minimal GAR recovery vs base.\", \"metrics\": {\"tf\": {\"gar_ours\": 0.4807, \"gar_dongre\": 0.0188, \"ngar_ours\": 11.8031, \"ngar_dongre\": 0.8261, \"ppl\": 2.6, \"ntp_loss\": 0.9366, \"n_conversations\": 50, \"n_turns\": 4}, \"ar\": {\"gar_ours\": 0.0617, \"gar_dongre\": 0.0226, \"ngar_ours\": 0.6065, \"ngar_dongre\": 0.2537, \"ppl\": 1.32, \"ntp_loss\": 0.2787, \"n_conversations\": 5, \"n_turns\": 10}, \"gap_ratio_gar_ours\": 7.79}, \"conclusion\": \"success\"}, \"llama_lora_only_s42\": {\"status\": \"DONE\", \"hypothesis\": \"Llama-3.1-8B LoRA-only baseline (gate=none, 无 gating 机制): 与 Llama TG s42 对比，验证 gating 对 Llama 的增量贡献。如果 LoRA-only GAR ≈ TG GAR → gating 零增量与 Qwen 结论一致（C5 跨模型）。\", \"conclusion\": \"success\", \"metrics\": {\"final_avg_loss\": 0.9288, \"final_avg_ntp\": 0.9279, \"final_avg_gar\": 0.0009, \"gate_fixed\": 1, \"gate_type\": \"none\", \"wall_clock_s\": 25317, \"wall_clock_h\": 7.03, \"epochs_completed\": 3}}, \"phase2_tg_s42_v6\": {\"status\": \"DONE\", \"hypothesis\": \"smooth_saturation loss (-target*tanh(GAR/target), target=0.5) 提供有界但持续的 GAR 梯度，避免 maximize 的恒等退化（gate→1）和 hinge_target 的梯度消失（GAR达标后梯度=0）。预期：gate_std>0.05 的层间分化 + GAR 稳态在 0.3-0.5 + NTP loss 正常收敛 + 总 loss 为正。\", \"metrics\": {\"dryrun_step0_L_NTP\": 2.0275, \"dryrun_step0_L_GAR\": -0.0161, \"dryrun_step0_total_loss\": 2.0114, \"dryrun_step4_L_NTP\": 1.6544, \"dryrun_step4_L_GAR\": -0.0147, \"dryrun_step4_total_loss\": 1.6397, \"dryrun_gate_grad\": true, \"dryrun_gate_mean_init\": 0.8097, \"dryrun_gate_std_init\": 0.0341, \"dryrun_gate_min_init\": 0.6836, \"dryrun_gate_max_init\": 0.8672, \"dryrun_gate_mean_step5\": 0.8025, \"dryrun_gate_std_step5\": 0.0842, \"dryrun_gate_min_step5\": 0.5547, \"dryrun_gate_max_step5\": 0.9805, \"gs50_gate_mean\": 0.8117, \"gs50_gate_std\": 0.0612, \"gs50_gate_min\": 0.6836, \"gs50_gate_max\": 0.9805, \"gs100_gate_mean\": 0.8737, \"gs100_gate_std\": 0.0367, \"gs100_gate_min\": 0.8164, \"gs100_gate_max\": 0.9766, \"gs100_L_NTP\": 0.8151, \"gs100_L_GAR\": -0.158, \"gs100_total_loss\": 0.6571, \"gs100_profile_bottom3\": \"L12=0.816 L4=0.824 L13=0.824\", \"gs100_profile_top3\": \"L27=0.977 L26=0.961 L23=0.914\", \"gs143_L_GAR\": -0.3876, \"gs143_gate_mean\": 0.9227}, \"conclusion\": \"negative\"}, \"phase2_tg_s42\": {\"status\": \"DONE\", \"hypothesis\": \"ThreadGate (turn-conditional gating) 在 L_NTP+L_GAR 联合训练后，相比 Uniform Gate，mid-turn GAR recovery 高出 ≥3pp，验证 Cesaro 理论预测：position-conditional 干预优于 uniform 干预\", \"conclusion\": \"negative\", \"metrics\": {\"final_ntp_loss\": 0.94, \"final_gar_loss\": 0, \"gate_mean\": 0.988, \"gar_loss_zero_pct\": 87.6, \"epochs_completed\": 1.67, \"killed_reason\": \"SIGTERM by diagnose worker (unauthorized)\"}}, \"eval_v7_tg_s123\": {\"status\": \"DONE\", \"hypothesis\": \"v7 TG s123 eval: 验证 s123 seed 的 TF-AR GAR gap 与 s42 一致（~32×），确认 multi-seed robustness\", \"conclusion\": \"success\", \"metrics\": {\"iid_tf\": {\"gar_ours_mid\": 0.5052, \"gar_dongre_mid\": 0.0119, \"ppl\": 2.7802, \"ntp\": 0.9752}, \"modelgen_ar\": {\"gar_ours_mid\": 0.0165, \"gar_dongre_mid\": 0.0177, \"ppl\": 1.3855, \"ntp\": 0.3223}, \"gap_ratio\": 30.6, \"comparison_s42\": {\"tf_gar_ours_delta\": 0.0017, \"ar_gar_ours_delta\": 0.0008, \"gap_ratio_delta\": -1.4}}}, \"eval_v8b_ss_s123\": {\"status\": \"DONE\", \"hypothesis\": \"v8b SS model trained with s123 seed should reproduce s42 GAR metrics within acceptable gap_ratio [1.2x-2.5x] and no PPL degradation, confirming seed robustness of the scheduled sampling approach\", \"conclusion\": \"success\", \"metrics\": {\"iid\": {\"gar_ours\": 0.503, \"gar_dongre\": 0.394, \"ppl\": 2.781, \"ntp_loss\": 0.976, \"n_conv\": 50, \"n_turns\": 3}, \"modelgen\": {\"gar_ours\": 0.418, \"gar_dongre\": 0.441, \"ppl\": 1.389, \"ntp_loss\": 0.325, \"n_conv\": 5, \"n_turns\": 10}, \"gap_ratio\": 1.2, \"base_iid_ppl\": 4.338, \"base_modelgen_ppl\": 1.351}}, \"v7_tg_s123\": {\"status\": \"DONE\", \"hypothesis\": \"v7 TG s42 已验证 ThreadGate 有效性，s123 验证 seed robustness。预期 gate profile 和 GAR 收敛模式与 s42 一致。\", \"conclusion\": \"success\", \"metrics\": {\"epoch_1\": {\"avg_loss\": 0.9447, \"avg_ntp_loss\": 0.9434, \"avg_gar_loss\": 0.0013, \"avg_div_loss\": 0}, \"epoch_2\": {\"avg_loss\": 0.9315, \"avg_ntp_loss\": 0.9305, \"avg_gar_loss\": 0.001, \"avg_div_loss\": 0}, \"final_gate\": {\"mean\": 0.9467, \"std\": 0.051, \"min\": 0.793, \"max\": 1}, \"final_gate_profile\": {\"L0\": 0.883, \"L1\": 0.793, \"L2\": 0.996, \"L3\": 0.988, \"L4\": 0.984, \"L5\": 0.797, \"L6\": 0.961, \"L7\": 0.918, \"L8\": 0.965, \"L9\": 0.934, \"L10\": 0.969, \"L11\": 0.918, \"L12\": 0.926, \"L13\": 0.941, \"L14\": 0.93, \"L15\": 0.965, \"L16\": 0.941, \"L17\": 0.91, \"L18\": 0.961, \"L19\": 0.965, \"L20\": 0.973, \"L21\": 0.988, \"L22\": 0.969, \"L23\": 0.98, \"L24\": 0.98, \"L25\": 0.984, \"L26\": 0.988, \"L27\": 1}, \"training_time_s\": 21425.2}}, \"v8b_ss_s123\": {\"status\": \"DONE\", \"hypothesis\": \"v8b SS s42 成功（gap 32×→1.57×），s123 验证结果的 seed robustness。预期 model-gen GAR 同样显著提升，PPL 无恶化。\", \"conclusion\": \"success\", \"metrics\": {\"final_loss\": 0.9316, \"final_ntp_loss\": 0.9307, \"final_gar_loss\": 0.0009, \"final_gate_mean\": 0.9505, \"final_gate_std\": 0.0508, \"final_gate_min\": 0.7383, \"final_gate_max\": 1, \"ss_used_ratio\": 0.371, \"training_time_s\": 38773.4, \"epoch0_loss\": 1.0092, \"epoch1_loss\": 0.9444, \"epoch2_loss\": 0.9316}}, \"llama_ar_matched_eval\": {\"status\": \"DONE\", \"hypothesis\": \"用 matched 设置 (N=50/T=4) 重跑 Llama AR eval，消除 TF/AR 设置差异。与 TF 结果对比得到可直接写入论文的 gap ratio，验证 TG 在 AR 模式下仍能提升 GAR。\", \"conclusion\": \"success\", \"metrics\": {\"ar_base_ours\": {\"mid_gar\": 0.0082, \"ngar\": 0.1, \"ppl\": 1.267}, \"ar_tg_ours\": {\"mid_gar\": 0.0388, \"ngar\": 0.493, \"ppl\": 1.413}, \"ar_base_dongre\": {\"mid_gar\": 0.0051, \"ngar\": 0.12, \"ppl\": 1.267}, \"ar_tg_dongre\": {\"mid_gar\": 0.018, \"ngar\": 0.431, \"ppl\": 1.413}, \"tf_reference\": {\"tf_tg_ours_ngar\": 11.88, \"tf_base_ours_ngar\": 0.388, \"tf_tg_ours_raw\": 0.4836, \"tf_tg_dongre_raw\": 0.018}, \"matched_gap_analysis\": {\"gar_ours_raw_gap\": \"12.5x (TF 0.484 / AR 0.039)\", \"gar_ours_ngar_gap\": \"24.1x (TF 11.88 / AR 0.493)\", \"gar_dongre_raw_gap\": \"1.002x (TF 0.018 / AR 0.018) — zero gap\", \"tg_over_base_ar_ours\": \"4.71x\", \"tg_over_base_ar_dongre\": \"3.54x\", \"conclusion\": \"GAR-ours TF-AR gap 12.5x (raw) / 24x (nGAR) is genuine exposure bias. GAR-Dongre zero gap (1.002x) confirms mechanism specificity: exposure bias selectively destroys learned goal-attention routing while leaving content-overlap-based attention unaffected.\"}}}, \"instruction_retention_test\": {\"status\": \"DONE\", \"hypothesis\": \"Turn-level residual gating (β=3) preserves instruction-following ability across multi-turn conversations better than the baseline (β=0), because gating modulates residual contributions to retain earlier context signals rather than letting them decay through successive transformer layers.\", \"conclusion\": \"success\", \"metrics\": {\"late_turn_rate_beta0\": 0.759, \"late_turn_rate_beta3\": 0.87, \"late_turn_delta\": 0.111, \"mcnemar_chi2\": 3.125, \"mcnemar_p\": 0.0771, \"gar_compliance_r\": 0.2003, \"gar_compliance_p\": 0.007, \"category_content_constraint\": {\"beta0\": 0.619, \"beta3\": 0.857, \"delta\": 0.238}, \"category_count_constraint\": {\"beta0\": 1, \"beta3\": 1, \"delta\": 0}, \"category_format_constraint\": {\"beta0\": 1, \"beta3\": 1, \"delta\": 0}, \"category_position_constraint\": {\"beta0\": 0.667, \"beta3\": 0.733, \"delta\": 0.067}}}, \"llama_eval_s42\": {\"status\": \"DONE\", \"hypothesis\": \"Llama-3.1-8B TG eval: 如果 Llama TG 模型在 TF 模式下 GAR-ours 显著高于 AR 模式（如 Qwen v7 的 20-33x gap），则确认 training-inference GAR gap 跨模型泛化（C5）。同时测量 base model 作为 control。\", \"metrics\": {\"tf_base\": {\"gar_ours\": 0.0166, \"ngar_ours\": 0.3882, \"gar_dongre\": 0.0038, \"ngar_dongre\": 0.163, \"ppl\": 3.45, \"N\": 50, \"T\": 4}, \"tf_tg\": {\"gar_ours\": 0.4836, \"ngar_ours\": 11.8818, \"gar_dongre\": 0.018, \"ngar_dongre\": 0.7922, \"ppl\": 2.57, \"N\": 50, \"T\": 4}, \"ar_base\": {\"gar_ours\": 0.0086, \"ngar_ours\": 0.0798, \"gar_dongre\": 0.0118, \"ngar_dongre\": 0.1265, \"ppl\": 1.24, \"N\": 5, \"T\": 10}, \"ar_tg\": {\"gar_ours\": 0.0304, \"ngar_ours\": 0.2632, \"gar_dongre\": 0.0217, \"ngar_dongre\": 0.2459, \"ppl\": 1.32, \"N\": 5, \"T\": 10}, \"gap_ratio_tg_ours\": 15.9, \"gap_ratio_base_ours\": 1.93, \"gap_ratio_tg_dongre\": 0.83, \"vs_qwen_v7_gap_ratio\": 32.1, \"baseline_mid_gar\": 0.0122}, \"conclusion\": \"success\"}, \"llama_tg_s42\": {\"status\": \"DONE\", \"hypothesis\": \"在 Llama-3.1-8B-Instruct 上训练 ThreadGate（与 Qwen v7 相同配置），验证 C5：gating mechanism 和 GAR training-inference gap 跨模型泛化。如果 Llama TG 也出现 IID GAR ≈ target 但 model-gen GAR 坍塌 → 确认 exposure bias 的跨模型通用性。\", \"conclusion\": \"success\", \"metrics\": {\"epochs_completed\": 3, \"total_steps\": 3000, \"wall_clock_seconds\": 26212, \"wall_clock_hours\": 7.28, \"final_avg_loss\": 0.9233, \"final_avg_ntp\": 0.9224, \"final_avg_gar\": 0.0009, \"final_avg_div\": 0, \"final_gate_mean\": 0.9099, \"final_gate_std\": 0.0701, \"final_gate_min\": 0.7188, \"final_gate_max\": 0.9922, \"gate_profile_step3000\": {\"L0\": 0.957, \"L1\": 0.973, \"L2\": 0.977, \"L3\": 0.965, \"L4\": 0.992, \"L5\": 0.969, \"L6\": 0.957, \"L7\": 0.957, \"L8\": 0.961, \"L9\": 0.949, \"L10\": 0.938, \"L11\": 0.934, \"L12\": 0.969, \"L13\": 0.953, \"L14\": 0.957, \"L15\": 0.965, \"L16\": 0.953, \"L17\": 0.961, \"L18\": 0.922, \"L19\": 0.902, \"L20\": 0.883, \"L21\": 0.863, \"L22\": 0.836, \"L23\": 0.844, \"L24\": 0.809, \"L25\": 0.719, \"L26\": 0.762, \"L27\": 0.805, \"L28\": 0.801, \"L29\": 0.855, \"L30\": 0.898, \"L31\": 0.934}, \"checkpoint_size_gate_mb\": 4.2, \"checkpoint_size_lora_mb\": 26, \"gpu\": \"NVIDIA RTX PRO 6000 Blackwell\", \"vram_gb\": 102, \"mem_used_gb\": 63.4}}, \"attention_steering_gen_n50\": {\"status\": \"DONE\", \"hypothesis\": \"N=5 gen steering 显示 β∈[2,5] phase transition (GAR 0.06→0.68)，但样本量不足以报告置信区间。N=50 conversations 应重现同一 phase transition pattern 并提供统计鲁棒的 mean±std，加固 C6 claim (attention steering as causal mechanism proof)。\", \"metrics\": {\"corrected\": true, \"aggregation\": \"per-conv mid_gar(turns 2-7), >=3 turns only\", \"beta_0.0\": {\"mid_gar\": 0.0641, \"mid_gar_std\": 0.0809, \"ppl\": 1.4324, \"ppl_std\": 0.1029, \"n_valid\": 39}, \"beta_2.0\": {\"mid_gar\": 0.128, \"mid_gar_std\": 0.1101, \"ppl\": 1.4822, \"ppl_std\": 0.1385, \"n_valid\": 39}, \"beta_3.0\": {\"mid_gar\": 0.5558, \"mid_gar_std\": 0.0601, \"ppl\": 1.5605, \"ppl_std\": 0.1719, \"n_valid\": 39}, \"beta_4.0\": {\"mid_gar\": 0.6439, \"mid_gar_std\": 0.0607, \"ppl\": 1.6674, \"ppl_std\": 0.2241, \"n_valid\": 39}, \"beta_5.0\": {\"mid_gar\": 0.7271, \"mid_gar_std\": 0.0605, \"ppl\": 1.7723, \"ppl_std\": 0.2693, \"n_valid\": 38}, \"beta_10.0\": {\"mid_gar\": 0.9612, \"mid_gar_std\": 0.0152, \"ppl\": 3.4517, \"ppl_std\": 1.7813, \"n_valid\": 39}, \"n_convs_total\": 50, \"n_convs_valid\": 39, \"mode\": \"gen\", \"phase_transition_range\": \"[2, 3]\"}, \"conclusion\": \"success\"}, \"phase2_tg_s42_v8b_resume\": {\"status\": \"DONE\", \"hypothesis\": \"从 epoch_0 checkpoint resume v8b scheduled sampling 训练。SS 线性混合 0→0.5 teacher-forced + model-generated contexts。如果 model-gen context 上的 GAR 训练能缩小 30x training-inference gap → exposure bias mitigation 有效。成功标准：inference GAR 显著高于 v7 的 0.016 (至少 +1pp)，PPL 不恶化。\", \"metrics\": {\"training\": {\"total_steps\": 3000, \"epochs_completed\": 3, \"wall_clock_hours\": 8.1, \"final_loss\": 0.933, \"final_ntp_loss\": 0.9322, \"final_gar_loss\": 0.0008, \"final_gate_mean\": 0.9586, \"final_gate_std\": 0.0582, \"ss_ratio\": 0.5}, \"eval_iid\": {\"gar_ours\": 0.4983, \"gar_dongre\": 0.3855, \"ppl\": 2.78}, \"eval_modelgen\": {\"gar_ours\": 0.3177, \"gar_dongre\": 0.3533, \"ppl\": 1.38}, \"vs_v7\": {\"iid_gar_ours_delta\": -0.005, \"modelgen_gar_ours_delta\": 0.302, \"gap_ratio_v7\": 32, \"gap_ratio_v8b\": 1.57}}, \"conclusion\": \"success\"}, \"llama_phase1_gar_diag\": {\"status\": \"DONE\", \"hypothesis\": \"Llama-3.1-8B-Instruct 在 multi-turn dialogue 中也应出现 goal attention decay（与 Qwen-2.5-7B 类似），确认 attention decay 是 transformer 架构通用现象而非模型特有。Phase 1 诊断：测量 base Llama 的 per-turn GAR profile。\", \"conclusion\": \"success\", \"metrics\": {\"per_turn_gar\": {\"turn_1\": 0.0263, \"turn_2\": 0.0183, \"turn_3\": 0.0087, \"turn_4\": 0.0055, \"turn_5\": 0.006, \"turn_6\": 0.0035, \"turn_7\": 0.0038, \"turn_8\": 0.0037, \"turn_9\": 0.005, \"turn_10\": 0.0026}, \"t1_t10_decay_pct\": 90.1, \"t1_mid38_drop_pct\": 80.2, \"n_topics\": 5, \"model\": \"Meta-Llama-3.1-8B-Instruct\", \"mode\": \"gen\", \"n_conversations\": 5, \"n_turns\": 10}}, \"eval_v8b_ss\": {\"status\": \"DONE\", \"hypothesis\": \"Scheduled Sampling (linear 0→0.5 mixing of teacher-forced and model-gen contexts) closes the 30x training-inference GAR gap by reducing exposure bias, resulting in model-gen GAR significantly above v7 baseline (0.016) while preserving IID GAR and PPL.\", \"metrics\": {\"iid_gar_ours\": 0.4983, \"iid_gar_dongre\": 0.3855, \"iid_ppl\": 2.78, \"iid_ngar_ours\": 13.5, \"iid_ngar_dongre\": 22.68, \"modelgen_gar_ours\": 0.3177, \"modelgen_gar_dongre\": 0.3533, \"modelgen_ppl\": 1.38, \"modelgen_ngar_ours\": 4.47, \"modelgen_ngar_dongre\": 5.92, \"iid_turn1_gar_ours\": 0.5398, \"modelgen_turn1_gar_ours\": 0.4333}, \"conclusion\": \"success\"}, \"attention_steering_eval200_tf\": {\"status\": \"DONE\", \"hypothesis\": \"N=200 TF 模式 attention steering 验证 β-GAR 关系的统计鲁棒性。在 teacher-forced context (无 exposure bias) 下，steering 效果应更温和（baseline GAR 已 ~0.50），但仍展示 β 调控 attention 的能力。与 N=5 gen 模式结果互补：tf 验证机制可控性，gen 验证因果闭环。\", \"metrics\": {\"beta_0.0\": {\"mid_gar\": 0.5353, \"ppl\": 2.62}, \"beta_2.0\": {\"mid_gar\": 0.6112, \"ppl\": 2.69}, \"beta_3.0\": {\"mid_gar\": 0.788, \"ppl\": 2.93}, \"beta_4.0\": {\"mid_gar\": 0.8165, \"ppl\": 3.49}, \"beta_5.0\": {\"mid_gar\": 0.8325, \"ppl\": 6.15}, \"beta_10.0\": {\"mid_gar\": 0.977, \"ppl\": 505.21}, \"n_convs\": 200, \"mode\": \"tf\"}, \"conclusion\": \"success\"}, \"trc_baseline_v7_tg\": {\"status\": \"DONE\", \"hypothesis\": \"如果 exposure bias 对 auxiliary objectives 的破坏跨特征空间通用，那么 TRC (hidden state cos_sim) 在 model-gen 下也应出现与 GAR (attention 空间) 类似的 TF/gen gap。在 v7 TG / LoRA-only / base 三个 checkpoint 上测量 TRC baseline，确认 gap 是否存在。成功标准：gen TRC 显著低于 TF TRC。\", \"conclusion\": \"success\", \"metrics\": {\"v7_tg\": {\"tf_trc\": 0.3339, \"gen_trc\": 0.3323, \"trc_gap\": 0.0016, \"tf_tbp_ppl\": 1.05, \"gen_tbp_ppl\": 1.05}, \"lora_only\": {\"tf_trc\": 0.349, \"gen_trc\": 0.4106, \"trc_gap\": -0.0617, \"tf_tbp_ppl\": 9.5, \"gen_tbp_ppl\": 12}, \"base\": {\"tf_trc\": 0.1494, \"gen_trc\": 0.1494, \"trc_gap\": 0, \"tf_tbp_ppl\": 2.05, \"gen_tbp_ppl\": 2.05}}}, \"attention_steering_v7_tg_gen\": {\"status\": \"DONE\", \"hypothesis\": \"推理时向 attention logits 注入 goal-position bias β 可恢复 autoregressive GAR。如果 GAR 从 0.015 显著提升 → 闭合因果环：exposure bias → attention 偏移 → GAR 坍塌 → 手动修正注意力 → GAR 恢复。扫描 β ∈ {0, 0.5, 1.0, 2.0, 5.0, 10.0}，成功标准：GAR > 0.1 且 PPL 不严重恶化。\", \"conclusion\": \"success\", \"metrics\": {\"beta_0.0\": {\"mid_turns_avg_gar\": 0.028, \"avg_ppl\": 1.409}, \"beta_0.5\": {\"mid_turns_avg_gar\": 0.0287, \"avg_ppl\": 1.387}, \"beta_1.0\": {\"mid_turns_avg_gar\": 0.0349, \"avg_ppl\": 1.36}, \"beta_2.0\": {\"mid_turns_avg_gar\": 0.062, \"avg_ppl\": 1.411}, \"beta_5.0\": {\"mid_turns_avg_gar\": 0.6795, \"avg_ppl\": 1.908}, \"beta_10.0\": {\"mid_turns_avg_gar\": 0.959, \"avg_ppl\": 4.22}, \"phase_transition_range\": \"[2, 5]\", \"baseline_gar\": 0.028, \"max_gar_at_acceptable_ppl\": 0.6795, \"max_gar_at_acceptable_ppl_beta\": 5}}, \"phase2_tg_s42_v8b_ss_fixed\": {\"status\": \"DONE\", \"hypothesis\": \"Fixed scheduled sampling (D026 三项 bug 修复后): 线性从 0→0.5 混合 teacher-forced + model-generated contexts 计算 GAR loss。如果 model-gen context 上的 GAR 训练能缩小 30x training-inference gap → exposure bias mitigation 有效，paper 从纯 negative 升级为 diagnosis + initial remedy。超参与 v7 一致 (lambda_gar=1.0, MSE+gate_div)，唯一变量是 SS path。成功标准：inference GAR 显著高于 v7 的 0.016 (至少 +1pp)，PPL 不恶化。\", \"conclusion\": \"failed\"}, \"phase2_tg_s42_v7\": {\"status\": \"DONE\", \"hypothesis\": \"MSE 双向 loss (mean_GAR - target)² + gate diversity 正则 F.relu(min_std - gate_std) 从结构上解决恒等退化：MSE 在 GAR > target 时反向惩罚（不再单调推高），gate_div 直接强制层间分化。预期：gate_std 稳定 >0.05 + GAR 收敛到 target=0.5 附近 + NTP 正常收敛。\", \"metrics\": {\"eval_iid_ours_mid_gar\": 0.5035, \"eval_iid_dongre_mid_gar\": 0.0152, \"eval_iid_ppl\": 2.784, \"eval_heldout_ours_mid_gar\": 0.5035, \"eval_heldout_dongre_mid_gar\": 0.0152, \"eval_heldout_ppl\": 2.78, \"eval_modelgen_ours_mid_gar\": 0.0157, \"eval_modelgen_dongre_mid_gar\": 0.0194, \"eval_modelgen_ppl\": 1.36, \"gate_mean_final\": 0.9336, \"gate_std_final\": 0.0492}, \"conclusion\": \"success\"}, \"phase2_tg_s42_v9_pcgrad\": {\"status\": \"DONE\", \"hypothesis\": \"PCGrad (Yu et al. NeurIPS 2020) 消除 NTP-GAR 梯度方向冲突后（仅对 gate 参数投影 NTP 梯度到 GAR 梯度正交平面），如果 30x training-inference GAR gap 仍在 → 因果证据证明 exposure bias（非梯度竞争）是 gap 根因。与 v7 对比：相同超参（lambda_gar=1.0, MSE+gate_div），唯一变量是梯度处理方式。成功标准：(1) 梯度 cos_sim 显著改善（从 v7 的 -0.089 提升到 ≥0），(2) 但推理 GAR 仍 ≈ v7 水平（0.016），证明梯度冲突不是 gap 的因。\", \"conclusion\": \"success\", \"metrics\": {\"eval_iid_ours_mid_gar\": 0.5002, \"eval_iid_dongre_mid_gar\": 0.0123, \"eval_iid_ppl\": 2.78, \"eval_iid_ntp\": 0.9752, \"eval_heldout_ours_mid_gar\": 0.5002, \"eval_heldout_dongre_mid_gar\": 0.0123, \"eval_heldout_ppl\": 2.78, \"eval_heldout_ntp\": 0.9752, \"eval_modelgen_ours_mid_gar\": 0.0151, \"eval_modelgen_dongre_mid_gar\": 0.0173, \"eval_modelgen_ppl\": 1.5, \"vs_v7_iid_ppl_diff\": 0.004, \"vs_v7_iid_gar_diff\": -0.0033}}, \"phase2_lora_only_s42\": {\"status\": \"DONE\", \"hypothesis\": \"LoRA-only baseline (gate 固定 1.0，无 gating 机制) 在相同 MSE+NTP loss 下 GAR 应低于 ThreadGate (v7)。如果 LoRA-only 也能训到 GAR~0.5，则 gating 机制贡献为零，paper story 不成立。关键对比：LoRA-only 的 GAR 收敛值 vs v7 的 0.48。\", \"conclusion\": \"success\", \"metrics\": {\"epochs_completed\": 3, \"global_steps\": 3000, \"training_time_seconds\": 20588.6, \"training_time_hours\": 5.7, \"gate_fixed\": 1, \"gate_type_actual\": \"none\", \"final_lora_size_mb\": 20, \"eval_modelgen_ours_mid_gar\": 0.0245, \"eval_modelgen_dongre_mid_gar\": 0.0185, \"eval_modelgen_ppl\": 1.371}}, \"phase2_ug_s42\": {\"status\": \"DONE\", \"hypothesis\": \"Uniform gating baseline: per-layer independent gates without turn conditioning (content-dependent only), to isolate whether ThreadGate's turn-conditioned gating provides benefit over content-only residual scaling. Same training setup as v7 but with gate-type=uniform.\", \"conclusion\": \"success\", \"metrics\": {\"epoch0_avg_loss\": 1.0019, \"epoch0_avg_ntp\": 0.9755, \"epoch0_avg_gar\": 0.0259, \"epoch0_avg_div\": 0.0005, \"epoch1_avg_loss\": 0.9447, \"epoch1_avg_ntp\": 0.9435, \"epoch1_avg_gar\": 0.0013, \"epoch1_avg_div\": 0, \"epoch2_avg_loss\": 0.9319, \"epoch2_avg_ntp\": 0.9309, \"epoch2_avg_gar\": 0.001, \"epoch2_avg_div\": 0, \"final_gate_mean\": 0.9598, \"final_gate_std\": 0.0518, \"final_gate_min\": 0.7773, \"final_gate_max\": 1, \"final_profile_L3\": 0.777, \"final_profile_L5\": 0.812, \"final_profile_L0\": 0.875, \"final_profile_L27\": 1, \"training_time_seconds\": 21994.5, \"training_time_hours\": 6.1, \"global_steps\": 7950, \"unexpected_per_layer_variation\": true, \"eval_modelgen_ours_mid_gar\": 0.0149, \"eval_modelgen_dongre_mid_gar\": 0.0185, \"eval_modelgen_ppl\": 1.396}}, \"phase2_tg_s42_v8_schedsampling\": {\"status\": \"DONE\", \"hypothesis\": \"Scheduled sampling 应用到 GAR loss（线性从 0→0.5 混合 teacher-forced + model-generated contexts）能缩小 v7 的 30x training-inference GAR gap。机制：在 model-generated context 上计算 GAR loss 迫使 attention pattern 适应推理时分布，直接 address teacher-forcing distribution shift。成功标准：inference GAR 显著高于 v7 的 0.016，PPL 不显著恶化（≤2.78+0.2）。\", \"conclusion\": \"failed\", \"metrics\": {\"killed_at_microstep\": 1950, \"total_microsteps\": 24000, \"completion_pct\": 8.1, \"global_step_approx\": 244, \"total_global_steps\": 3000, \"ss_steps_observed\": 1, \"tf_lgar_mean_step850_1400\": 0.0062, \"tf_lgar_std\": 0.0082, \"tf_lgar_collapse_step\": 800, \"gate_mean_final\": 0.93, \"ss_ratio_at_kill\": 0.081, \"crash_reason\": \"killed by director: SS path code bug (D026) makes experiment invalid, GPU needed for PCGrad\", \"design_flaw_ss_ramp_too_slow\": true, \"design_flaw_no_ss_tf_separate_logging\": true}}, \"analysis_attention_heatmap\": {\"status\": \"DONE\", \"hypothesis\": \"四模型（Base/TG/UG/LoRA-only）的 goal attention 衰减模式是否一致？如果 TG 的 attention decay 与 LoRA-only 无差异，则 gating 机制对 attention 分布零增量。\", \"conclusion\": \"success\", \"metrics\": {\"base_mean_goal_attn\": 0.0136, \"base_decay\": 0.875, \"tg_mean_goal_attn\": 0.0232, \"tg_decay\": 0.777, \"ug_mean_goal_attn\": 0.0216, \"ug_decay\": 0.803, \"lora_mean_goal_attn\": 0.0216, \"lora_decay\": 0.81, \"gating_incremental_benefit\": \"none\"}}, \"analysis_gradient_conflict\": {\"status\": \"DONE\", \"hypothesis\": \"NTP-GAR 梯度冲突在 v7 训练过程中是否逐层普遍存在？量化 cos_sim 和 magnitude ratio 的演化，验证 NTP 是否在训练中逐渐完全压制 GAR 信号。\", \"conclusion\": \"success\", \"metrics\": {\"epoch0_cos_sim\": -0.089, \"epoch1_cos_sim\": -0.054, \"epoch2_cos_sim\": -0.042, \"epoch0_neg_layers_pct\": 78.6, \"epoch1_neg_layers_pct\": 71.4, \"epoch2_neg_layers_pct\": 67.9, \"epoch0_mag_ratio\": 7.5, \"epoch1_mag_ratio\": 13.7, \"epoch2_mag_ratio\": 14.7}}, \"phase2_4way_eval_heldout\": {\"status\": \"DONE\", \"hypothesis\": \"四路消融的三路趋同结论（TG≈UG≈LoRA-only，gating 零增量）在 held-out eval 数据（idx≥8000，与训练集无重叠）上复现，排除数据重叠 confound。预期：相对比较保持（三路趋同），绝对 GAR 值可能变化。\", \"metrics\": {\"base_ours_mid_gar\": 0.0128, \"base_ours_recovery_pp\": 0.06, \"base_dongre_mid_gar\": 0.0031, \"base_dongre_recovery_pp\": -0.91, \"base_ppl\": 4.34, \"base_ntp\": 1.4045, \"tg_ours_mid_gar\": 0.5035, \"tg_ours_recovery_pp\": 49.13, \"tg_dongre_mid_gar\": 0.0152, \"tg_dongre_recovery_pp\": 0.3, \"tg_ppl\": 2.78, \"tg_ntp\": 0.9771, \"ug_ours_mid_gar\": 0.5053, \"ug_ours_recovery_pp\": 49.31, \"ug_dongre_mid_gar\": 0.0124, \"ug_dongre_recovery_pp\": 0.02, \"ug_ppl\": 2.78, \"ug_ntp\": 0.9752, \"lora_ours_mid_gar\": 0.4978, \"lora_ours_recovery_pp\": 48.56, \"lora_dongre_mid_gar\": 0.0132, \"lora_dongre_recovery_pp\": 0.1, \"lora_ppl\": 2.78, \"lora_ntp\": 0.9771, \"three_way_convergence_confirmed\": true, \"gar_ours_spread_pp\": 0.75, \"ppl_spread\": 0, \"data_overlap\": false}, \"conclusion\": \"success\"}, \"phase2_4way_eval\": {\"status\": \"DONE\", \"hypothesis\": \"Turn-residual gating (TRG) improves multi-turn response quality over LoRA-only and base model baselines because it selectively amplifies conversational context signals, which should manifest as higher GAR scores across 4 conditions (base, base+TRG, LoRA, LoRA+TRG).\", \"conclusion\": \"negative\", \"metrics\": {\"base_ours_mid_gar\": 0.0107, \"base_ours_recovery_pp\": -0.15, \"base_dongre_mid_gar\": 0.003, \"base_dongre_recovery_pp\": -0.92, \"base_ppl\": 4.23, \"base_ntp\": 1.4162, \"tg_ours_mid_gar\": 0.4866, \"tg_ours_recovery_pp\": 47.44, \"tg_dongre_mid_gar\": 0.0157, \"tg_dongre_recovery_pp\": 0.35, \"tg_ppl\": 2.63, \"tg_ntp\": 0.9484, \"ug_ours_mid_gar\": 0.4923, \"ug_ours_recovery_pp\": 48.01, \"ug_dongre_mid_gar\": 0.013, \"ug_dongre_recovery_pp\": 0.08, \"ug_ppl\": 2.62, \"ug_ntp\": 0.9433, \"lora_ours_mid_gar\": 0.486, \"lora_ours_recovery_pp\": 47.39, \"lora_dongre_mid_gar\": 0.0137, \"lora_dongre_recovery_pp\": 0.15, \"lora_ppl\": 2.63, \"lora_ntp\": 0.9482, \"route_b_confirmed\": true, \"gating_incremental_benefit\": \"none\"}}, \"phase2_tg_s42_v5\": {\"status\": \"DONE\", \"hypothesis\": \"重新平衡超参（λ=1.0 降 GAR 贡献至 ~50%，init_bias=1.5 使 sigmoid≈0.82 接近正常模型行为，gate_lr_multiplier=10 保持）能在 3-epoch 全量训练中产生有意义的 gate 分化（gate_std>0.05），同时 GAR 稳态在 0.1-0.5（非病态饱和），NTP loss 正常收敛，总 loss 保持正值\", \"metrics\": {\"step2000_gate_std\": 0.0225, \"step2000_gate_mean\": 0.9586, \"step2000_gate_min\": 0.9062, \"step2000_gate_max\": 0.9961, \"step2000_L_GAR\": -0.8977, \"step2000_L_NTP\": 0.7611, \"step2000_total_loss\": -0.1365, \"step2400_gate_std\": 0.0219, \"step2400_gate_mean\": 0.9651, \"step2400_gate_min\": 0.918, \"step2400_gate_max\": 0.9961, \"step2400_profile\": \"L0=0.918 L12=0.918 L13=0.926 L1=0.996 L26=0.996\", \"L_GAR_saturated_at\": -0.91, \"gate_range_compression\": \"0.918-0.996\"}, \"conclusion\": \"negative\"}, \"phase2_tg_s42_v4\": {\"status\": \"DONE\", \"hypothesis\": \"重新平衡超参（λ=1.0 降 GAR 贡献至 ~50%，init_bias=1.5 使 sigmoid≈0.82 接近正常模型行为，gate_lr_multiplier=10 保持）能在 3-epoch 全量训练中产生有意义的 gate 分化（gate_std>0.05），同时 GAR 稳态在 0.1-0.5（非病态饱和），NTP loss 正常收敛，总 loss 保持正值\", \"conclusion\": \"failed\"}, \"phase2_tg_s42_v3b\": {\"status\": \"DONE\", \"hypothesis\": \"λ=10 + gate_lr=10x + init_bias=0.0 (sigmoid=0.5) 能否驱动 gate 产生 layer 间分化 (gate_std>0.05)？如果 500 步后 gate_std<0.02 且无选择性 → GAR-driven gating 梯度路径确认失败，需要 pivot\", \"conclusion\": \"success\", \"metrics\": {\"gate_std_final\": 0.087, \"gate_mean_final\": 0.9388, \"gate_min_final\": 0.5352, \"gate_max_final\": 0.9922, \"L4_gate\": 0.535, \"L0_gate\": 0.777, \"L_NTP_final\": 0.7787, \"L_GAR_final\": -0.9606, \"elapsed_seconds\": 3565.9, \"optimizer_steps\": 500, \"gate_grad_received\": true}}, \"phase2_tg_s42_v3\": {\"status\": \"DONE\", \"hypothesis\": \"ThreadGate + maximize GAR loss (L_GAR=-mean(GAR)) 提供持续非零梯度，避免 hinge loss 的退化平衡点，gate 值应随训练下降（学习到选择性干预），同时 NTP loss 正常收敛\", \"conclusion\": \"negative\", \"metrics\": {\"gate_mean_step0\": 0.8743, \"gate_mean_step500\": 0.8761, \"gate_delta\": 0.004, \"gate_std\": 0.001, \"final_ntp_loss\": 0.94, \"final_gar_loss\": -0.019, \"gar_contribution_pct\": \"2-4%\", \"diagnosis\": \"gate frozen, GAR indirect gradient too weak\"}}, \"phase2_tg_s42_v2\": {\"status\": \"DONE\", \"hypothesis\": \"ThreadGate + 修复后的 cumulative GAR loss (ε=0.001) 在 L_NTP+L_GAR 联合训练后，mid-turn GAR recovery 应显著优于 v1 (NTP-only baseline)，验证 GAR loss 的有效性\", \"conclusion\": \"killed\"}, \"phase1_gar_diag\": {\"status\": \"DONE\", \"hypothesis\": \"Qwen2.5-7B-Instruct 在 10-turn 多轮对话中，中间 turns (3-8) 的 GAR (Goal Accessibility Ratio) 相对 turn-1 下降 ≥15%，表明模型对 system prompt 中目标 token 的注意力随对话进行显著衰减\", \"conclusion\": \"success\", \"metrics\": {\"turn1_avg_gar\": 0.0418, \"mid_turns_avg_gar\": 0.0122, \"relative_drop\": 0.708, \"num_conversations\": 5, \"num_turns\": 10, \"per_turn_avg_gar\": [0.0418, 0.0241, 0.0224, 0.013, 0.0133, 0.0086, 0.0078, 0.008, 0.0157, 0.0064]}}}, \"count\": 53, \"total\": 53, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.1655}}"
    }
  },
  "sourceToolAssistantUUID": "db2ac22c-6c15-44ad-9287-bd45bf303fcd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921",
  "sessionId": "5d779602-0719-4d06-8bf9-fdd84990d5d0",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---


### Runtime record

_source line 70_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[系统通知 — worker_done:worker_audit_appendix_tables_20260525T201208]: Worker worker_audit_appendix_tables_20260525T201208 已完成（status=done），请审查 Agent 的处理结果。",
  "leafUuid": "2bffec83-2837-47f2-94b9-7c117d54d296",
  "sessionId": "5d779602-0719-4d06-8bf9-fdd84990d5d0"
}
```

---


### Runtime record

_source line 71_

```json
{
  "type": "ai-title",
  "aiTitle": "Review worker audit appendix tables completion",
  "sessionId": "5d779602-0719-4d06-8bf9-fdd84990d5d0"
}
```

---


### Assistant

_source line 72 · 2026-05-25T20:38:28.172Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a comprehensive view of the appendix tables and the registry data. Let me systematically cross-verify the numbers in the appendix tables against the registry data.

Let me check several key tables:

### 1. tab_perseed_ss.tex
SS per-seed results:
- Seed 42: AR β=0 GAR = 0.347, AR β=3 GAR = 0.593, AR β=5 GAR = 0.717
- Seed 123: AR β=0 GAR = 0.423, AR β=3 GAR = 0.590, AR β=5 GAR = 0.717


- Seed 456: AR β=0 GAR = 0.433, AR β=3 GAR = 0.605, AR β=5 GAR = 0.716
- Mean: AR β=0 GAR = 0.401±0.047, AR β=3 GAR = 0.596±0.008, AR β=5 GAR = 0.717±0.001

Now I'm comparing these against the registry data to verify the reported values match what's stored in the evaluation records. Seed 123 values match up perfectly when rounded. For seed 456, the registry entries also align with the table after rounding. Now I'm calculating the mean across all three seeds at β=0, which gives me 1.203.

Continuing with the means for β=3 and β=5, I get 0.596 and 0.717 respectively. For the standard deviation at β=0, I'm working through the deviations from the mean of 0.401, computing the variance across the sample, and arriving at a standard deviation of 0.047.

Now checking the standard deviations for the higher beta values—at β=3 the values cluster very tightly around 0.596 with a standard deviation of just 0.008, and at β=5 they're even more consistent around 0.717 with a standard deviation of 0.001. Moving on to the TF metrics now.

For the Seed 42 TF GAR value, I'm trying to locate where the 0.502 figure comes from—it might be in the d048_eval_ss_s42 results, but I'm seeing some confusion between the TG and TF metrics in that file, and the actual IID GAR value from the first SS run appears to be closer to 0.498.

Now moving on to Seed 123, I need to check the corresponding d048_eval_ss_s123 metrics.

For the TF PPL values, I'm verifying each seed against the registry. Seed 42 shows 2.78 which matches the expected 2.780, and Seed 123 has 2.6123 rounding to 2.612. However, Seed 456 is missing the tf_ppl metric entirely in the data.

Now looking at the AR β=0 PPL values, I'm noticing a discrepancy with Seed 42 — the table shows 1.442 but I'm finding different values depending on which evaluation run I check. The d048_final_ar_eval used N=50 while d048_eval_ss_s42 was an N=5 evaluation, which explains why the numbers don't align.

For the per-seed table, I need to pull the AR metrics from the right sources: d048_final_ar_eval for Seed 42, and d048_eval_ss_s123 and d048_eval_ss_s456 for the other seeds. Checking those values now — Seed 123 gives 1.441 and Seed 456 gives 1.439, both matching what's in the table.

Moving on to the TG per-seed results...

I'm verifying the metrics across seeds. For Seed 42, the TF GAR and PPL values match the phase2_tg_s42_v7 registry entries, and the AR β=0 GAR also checks out. For Seed 123, I'm cross-referencing with eval_v7_tg_s123 to confirm the TF GAR value.

Now I'm computing the gap ratios by dividing the TF GAR by the AR GAR for each seed. For Seed 42, using the more precise unrounded values gives 32.07, which matches the table's 32.1. For Seed 123, the ratio is 30.6. The mean across both seeds comes to 31.

4, which aligns with the table's reported 31.4 ± 1.1.

Moving on to verify the TG GAR-Dongre values: both seeds check out against the registry entries when rounded appropriately. Then I'm checking the AR β=0 GAR-Dongre values, where Seed 42 gives 0.019 and Seed 123 gives 0.018, both matching the table.

For AR PPL, Seed 42 shows 1.360 and Seed 123 shows 1.386, which both align with the registry values when rounded.

I'm noticing that TG only has 2 seeds since the multi-seed experiment was terminated, while the SS condition has 3 seeds. This asymmetry might be worth considering, though the paper does report results for these 2 seeds.

Now I'm moving into the cross-model comparison section to verify those entries.

For Qwen-7B, I'm checking the base and AR metrics: the TF GAR of 0.013 and AR GAR of 0.019 match the registry values, the TF PPL of 4.34 is confirmed, and the AR PPL of 1.447 checks out. The gap calculation of 0.68 (roughly 0.7×) is correct when dividing the base GAR by the AR GAR.

Now looking at the TG variant, the TF GAR of 0.504 is verified from the phase2 evaluation, the AR GAR of 0.064 is confirmed, and both PPL values of 2.78 and 1.432 match the expected results. The gap here is much larger at 7.9×.

For the LoRA-only configuration, the TF GAR rounds to 0.498, AR GAR is 0.037, and the gap widens to 13.5×. The SS variant shows similar TF and AR GAR values of 0.498 and 0.401 respectively, with the same PPL of 2.78 for TF, but the AR PPL is still being pulled from the data.

Now I'm noticing a discrepancy in the SS TF GAR values—the cross-model table shows 0.498, but when I calculate the mean from the per-seed results across three seeds, I get 0.517 ± 0.032, which doesn't match. Let me check if the cross-model table is using the specific s42 seed value instead of the multi-seed average.

Looking at the AR GAR values, there's another inconsistency: the cross-model table lists 0.401 for SS, but the per-seed table shows 0.347 for s42. However, 0.401 is actually the multi-seed mean from the per-seed table, so it seems the cross-model table is mixing single-seed and multi-seed values inconsistently. the table is indeed mixing metrics from different evaluation runs—using the single-seed TF GAR value alongside the multi-seed AR GAR mean. This produces the 1.2× gap shown, but consistency would shift it to either 1.4× (both single-seed) or 1.3× (both multi-seed).

Now I'm noticing there are actually two different evaluations for s42 that give slightly different TF GAR values—0.498 versus 0.502/0.503—likely from different eval protocols or dataset sizes. Let me check what the per-seed table documentation says about which one to use. The cross-model table mixes evaluation protocols—using Qwen's TF GAR from a 50-conversation eval (0.498) while pulling the AR GAR from a 3-seed average (0.401), creating a gap of 1.24×. The per-seed table shows Qwen's TF GAR as 0.502 from a 200-conversation eval, which differs from the cross-model value, highlighting how inconsistent evaluation datasets are being combined in the same table. For Llama-8B, the base TF GAR is 0.017 versus AR GAR of 0.009, yielding a 1.9× gap.

Now I'm verifying the Llama-8B numbers against the registry—the TF GAR of 0.017 matches the seed 42 eval, the AR GAR of 0.009 matches the mean from the 20-conversation AR eval, and both perplexity values check out. For the TG model, I'm seeing TF GAR at 0.484 and AR GAR at 0.043. Now I'm verifying the LoRA-only configuration shows a larger performance gap at 17.2×, with the transformer achieving 0.481 GAR while the autoregressive model drops to 0.028. Moving on to check the Supervised Scaling results, which show a much tighter gap of 2.9× with the transformer at 0.477 GAR.

I'm looking at the per-turn Qwen results from the final autoregressive run with beta=0 and 50 generation steps, though I'm noticing these individual turn-level metrics aren't directly available in the registry summary. The per-turn table only shows turns 1-5, but conversations average 5.6 turns, so the overall metric likely includes additional turns beyond what's displayed that pull the average down. The mid-turn definition also varies across experiments—some use turns 2-T, others 3-T—which could explain the discrepancy between the per-turn average I calculated and the reported overall value. Looking at the Base model numbers now to check for similar patterns. For the Llama model with N=20 and T=4, I'm checking the base GAR values against the registry definition. The mid-turn metric excludes the first two turns, so I'm looking at turns 3-4 (in 1-indexed terms, or 0-indexed turns 2-3). The table shows base values of .009 and .008 for those turns, averaging to .0085, which matches the reported mean of .0088 quite closely.

Now I'm verifying the other conditions in the same panel. The TG variant shows mid-turn values of .049 and .038 averaging to .0435, matching the registry's .0434. The LO variant gives .025 and .031 averaging to .028, which aligns with the registry's .0284.

Moving to panel (b) with base decay at N=5 and T=10, I'm spot-checking individual turns against the registry values. Turn 1 shows .026 matching the registry's .0263, turn 3 shows .009 matching .0087, and turn 10 shows .003 matching .0026—all checks passing.

Now I'm looking at the MMLU detail table and verifying the overall accuracy scores across all model variants. The base Qwen model registers at 74.23%, while the TG, PCGrad, SS, LoRA-only, and UG variants come in at 73.47%, 73.86%, 73.75%, 73.57%, and 73.46% respectively—all matching their table entries. I'm about to examine the delta values next.

Computing the performance deltas relative to the baseline shows TG dropping 0.76 percentage points, PCGrad at -0.37, SS at -0.48, LoRA-only at -0.66, and UG at -0.77. The per-category breakdowns aren't available in the registry, so I can only verify the overall scores. Moving on to the dataset statistics table, I'm confirming the training set size of 8000 samples and the held-out evaluation set of 50 samples both align with the experiment specifications.

Now I'm checking the Qwen 1.5B results against the registry. The table shows a turn-1 GAR of 0.0336 dropping to 0.0068 mid-turn, which represents a 79.8% relative decline. For phase 2 training with TG, the baseline AR at β=0 is 0.0167 ± 0.005, dropping to 0.0 with TG applied.

Looking at the robustness metrics, I'm examining the GAR robustness results from the KL divergence experiment. The registry shows a ratio of 21.4, though the actual table displays different gap ratios across the four token selection strategies being tested. Spot-checking a few more ratios to verify consistency—Goal-only TG comes out to 1.07, and First token Base is around 13.32 when I divide it out. Now I'm examining the statistical test results from the registry, confirming the Wilcoxon p-values and effect sizes all match what's documented in the table.

Now I'm verifying the GAR values across different method comparisons—TG outperforms Base at 0.064 versus 0.019, LoRA sits at 0.037, and SS shows the strongest performance at 0.347. The β=3 results show Base at 0.531 with TG and SS pushing higher, which aligns with what's stored in the registry.

For β=5, the values continue climbing with Base at 0.704, TG at 0.727, and SS at 0.717. Moving to the instruction retention section, the McNemar test yields χ²=3.13 with p=.077, and the late-turn rates show improvement from 0.759 to 0.870 across beta conditions. Now I'm checking the confidence intervals in the statistical analysis.

Looking at the bootstrap CIs for β=0 across different methods—TG shows .064 [.041, .091], Base is .019 [.014, .024], SS is .347 [.327, .366], and PCGrad is .030 [.023, .038]—these aren't directly stored in the registry but computed from bootstrap resampling, so I can't verify them without recalculating. I'm also noticing a data consistency issue in the cross-model table where Qwen's SS values mix single-seed and multi-seed results, creating an inconsistency that affects the gap ratio calculation.

Tracing through the different eval runs, I'm finding that the same s42 SS model produces slightly different TF GAR values across different evaluation runs—0.5025 in one, 0.502 in the per-seed table, and 0.4983 in eval_v8b_ss—which explains why the cross-model table shows 0.498 rather than the other values.

Looking at the experiment dates, the d048 evals appear to be the newer unified protocol while eval_v8b_ss is from an older run, so the cross-model table might actually be pulling outdated numbers instead of the latest d048 results. I'm seeing that 0.498 and 0.502 are from different eval runs on the same checkpoint, which explains the small discrepancy. But the real issue is that the cross-model table's AR GAR value of 0.401 doesn't match what I'm finding in d048_final_ar (0.347), so it must be pulling from a different evaluation run entirely. Looking at the caption again, it specifies that Qwen AR uses d048_final_ar with N=50 gen beta=0, but the SS AR value of 0.401 is actually the 3-seed mean, not the s42-specific value of 0.347 from that dataset. This is a real mismatch—it seems the SS value was updated to reflect multi-seed data while the caption and TF value weren't synchronized, which warrants flagging as a warning-level inconsistency. Now I need to check whether d048_final_ar_eval is specifically designed for s42 or if it covers multiple conditions.

The experiment evaluated 6 conditions across s42, so the 0.347 ss_gar is the s42-only result. The cross-model table's 0.401 is pulling from a different source—the 3-seed average—which creates an inconsistency since the other Qwen conditions (Base, TG, LoRA-only) all use s42 values. Additionally, TG only has 2 seeds available (42 and 123, since the phase1a_multiseed_qwen experiment was terminated), whereas SS has 3 seeds, which is another asymmetry the paper should acknowledge.

There's also a protocol mismatch: TG's per-seed AR evaluation uses the older N=5, T=10 protocol, while SS uses the newer N=50 d048 protocol. This difference in sample size affects statistical power—TG's AR GAR values (0.016, 0.017) come from just 5 conversations, while SS's values (0.347, 0.423, 0.433) come from 50.

But now I'm seeing a major inconsistency: the main d048_final_ar_eval reports tg_gar = 0.064 with N=50, yet the per-seed TG table shows seed 42 with AR GAR = 0.016. The v7 eval from phase2_tg_s42 gives 0.0157 from N=5, T=10, so the same seed 42 model is producing vastly different AR GAR values depending on which evaluation protocol was used.

The 4× difference comes down to the evaluation settings: the per-seed table uses the older N=5 T=10 protocol while the main results use N=50 generation mode, and as the appendix notes, the gating advantage diminishes in longer dialogues. This creates a real problem for readers trying to compare the per-seed TG AR GAR (0.016) against the main table's TG AR GAR (0.064)—they're fundamentally different evaluation conditions, which isn't immediately obvious.

The per-seed table does caption that it uses 5 model-generated conversations with 10 turns each, so it's technically transparent, but the gap ratios are starkly different: 31.4× from the N=5 eval versus 7.9× from the N=50 eval. I need to check which number the paper's main text actually cites when making claims about the TF-AR gap for TG.

The core issue is that the per-seed table mixes evaluation protocols—TF uses N=200 while AR uses only N=5—and this produces a gap ratio that's dramatically inflated compared to the main cross-model results. A reviewer could easily be confused about which gap ratio represents the actual finding, especially since the appendix itself acknowledges the N=5 protocol as "directional evidence" due to the small sample size.

I can't fully verify the Qwen 1.5B results against the registry since the phase 2 metrics aren't stored there. Let me scan through the rest of the appendix to see if there are other issues I should flag, and I should also check what the worker that audited these tables actually produced.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2bffec83-2837-47f2-94b9-7c117d54d296",
  "isSidechain": false,
  "requestId": "req_011CbPvhoPPLcGrV1ZyCdTeR",
  "type": "assistant",
  "uuid": "3ad162d2-e51e-40f0-8140-4ee30b389b42",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921",
  "sessionId": "5d779602-0719-4d06-8bf9-fdd84990d5d0",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Nz8YsY9jpcaw3eQYNuT6Ri",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 24430,
      "cache_read_input_tokens": 51522,
      "output_tokens": 12020,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 24430,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 12020,
          "cache_read_input_tokens": 51522,
          "cache_creation_input_tokens": 24430,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 24430
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

_source line 73 · 2026-05-25T20:38:28.175Z_

让我进一步检查附录剩余部分和 worker 的实际产出。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3ad162d2-e51e-40f0-8140-4ee30b389b42",
  "isSidechain": false,
  "requestId": "req_011CbPvhoPPLcGrV1ZyCdTeR",
  "type": "assistant",
  "uuid": "feaa7d34-e0e9-42a6-a63d-17514e77081a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921",
  "sessionId": "5d779602-0719-4d06-8bf9-fdd84990d5d0",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Nz8YsY9jpcaw3eQYNuT6Ri",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 24430,
      "cache_read_input_tokens": 51522,
      "output_tokens": 12020,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 24430,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 12020,
          "cache_read_input_tokens": 51522,
          "cache_creation_input_tokens": 24430,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 24430
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

_source line 74 · 2026-05-25T20:38:28.177Z_

<details open><summary>🔧 Tool call — Read · `toolu_016TMGUgREsCiRcXHfa3f4nK`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex",
  "offset": 200,
  "limit": 200
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "feaa7d34-e0e9-42a6-a63d-17514e77081a",
  "isSidechain": false,
  "requestId": "req_011CbPvhoPPLcGrV1ZyCdTeR",
  "type": "assistant",
  "uuid": "21ec9fc7-6186-497c-826b-32ed3e4fd0d5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921",
  "sessionId": "5d779602-0719-4d06-8bf9-fdd84990d5d0",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Nz8YsY9jpcaw3eQYNuT6Ri",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 24430,
      "cache_read_input_tokens": 51522,
      "output_tokens": 12020,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 24430,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 12020,
          "cache_read_input_tokens": 51522,
          "cache_creation_input_tokens": 24430,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 24430
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

_source line 75 · 2026-05-25T20:38:28.195Z_

<details><summary>↩ Tool result · `toolu_016TMGUgREsCiRcXHfa3f4nK`</summary>

```text
200	\begin{figure}[t]
201	  \centering
202	  \includegraphics[width=\columnwidth]{fig_crossmodel.pdf}
203	  \caption{Cross-architecture validation. (a)~The TF-AR gap persists on Llama-3.1-8B (27$\times$ by median), exceeding Qwen's 8$\times$. (b)~Gate profiles on normalized depth: Qwen dips at early layers, Llama at late layers; architecture-dependent patterns, but both converge toward identity.}
204	  \label{fig:crossmodel}
205	\end{figure}
206	
207	\paragraph{Cross-model summary.} Table~\ref{tab:crossmodel-detail} consolidates the cross-model comparison, showing TF GAR, AR GAR, PPL, and gap ratios side by side for both architectures. The consistent pattern---TF GAR $\approx$ 0.5, AR GAR $\ll$ 0.1, gap $\geq$ 7.9$\times$---across two architectures with different layer counts, attention head configurations, and pre-training corpora provides strong evidence that exposure bias is architecture-independent. Notably, Llama's larger gaps (27$\times$ by median for TG; mean-based range 11.2--17.2$\times$) compared to Qwen's (7.9--13.5$\times$) may reflect its deeper architecture (32 vs.\ 28 layers), which allows more layers for distributional drift to compound through.
208	
209	\input{../artifacts/appendix_expansion/tab_crossmodel_detail.tex}
210	
211	\paragraph{GAR-Dongre cross-model comparison.} GAR-Dongre shows negligible distribution shift on Llama (AR/TF ratio 1.002$\times$), compared to 1.28$\times$ on Qwen. This confirms the mechanism specificity finding: exposure bias selectively disrupts the concentrated last-token attention pattern (GAR-ours) while leaving the diffuse all-token attention (GAR-Dongre) unaffected across both architectures.
212	
213	\paragraph{Training details.} Llama variants used the same pipeline as Qwen: 8K UltraChat conversations, LoRA rank 16 targeting $q$/$v$ projections, 3 epochs. Training loss converged to 0.929 (LoRA-only) and 0.934 (ThreadGate); the slight difference is attributable to the additional GAR loss component. Wall-clock time was 7.0h (LoRA-only) and 7.3h (ThreadGate), approximately 17\% longer than Qwen due to Llama's larger layer count (32 vs.\ 28 layers).
214	
215	\paragraph{Phase 1 diagnostics.} Before fine-tuning, we confirmed that Llama exhibits the same goal attention decay as Qwen. Base model GAR decays from 0.026 (turn 1) to 0.003 (turn 10), a 90\% decline. This is steeper than Qwen's 70.8\% decline, suggesting that attention decay may be more severe in Llama's architecture despite its larger head count (32 vs.\ 28 KV heads).
216	
217	\paragraph{Cross-model gradient analysis.} Table~\ref{tab:gradient-crossmodel} compares NTP--GAR gradient interaction between the two architectures. Both models exhibit near-orthogonal gradients (cosine similarity $\approx$\,0), not systematic conflict: Qwen shows a slight negative mean ($-$0.042) while Llama is marginally positive (+0.005). NTP gradients dominate GAR by 14.7$\times$ on Qwen and 25.7$\times$ on Llama, indicating that the auxiliary signal is overwhelmed by magnitude rather than opposed by direction. The cross-model consistency---near-zero cosine similarity and order-of-magnitude NTP dominance on both architectures---reinforces the \emph{modus tollens} argument (\S\ref{subsec:pcgrad}): gradient direction conflict is not the primary cause of the TF-AR gap.
218	
219	\begin{table}[t]
220	\centering\small
221	\caption{Cross-model NTP--GAR gradient interaction. Gradients are near-orthogonal on both architectures; NTP magnitude dominates GAR by 15--26$\times$.}
222	\label{tab:gradient-crossmodel}
223	\begin{tabular}{lcc}
224	\toprule
225	\textbf{Metric} & \textbf{Qwen-7B} & \textbf{Llama-8B} \\
226	\midrule
227	Mean cos sim & $-$0.042 & +0.005 \\
228	Neg-layer \% & 67.9\% & 53.1\% \\
229	NTP/GAR mag ratio & 14.7$\times$ & 25.7$\times$ \\
230	\bottomrule
231	\end{tabular}
232	\end{table}
233	
234	\section{Additional Visualizations}\label{sec:appendix-viz}
235	
236	This section presents extended visualizations referenced in the main text. Each figure examines a different aspect of the gating behavior and its failure under autoregressive generation.
237	
238	\subsection{Gate Profile Heatmap}
239	
240	Figure~\ref{fig:gate-heatmap} shows the per-layer gate values across all training configurations for both Qwen-2.5-7B (28 layers) and Llama-3.1-8B (32 layers). The key observation is that early layers consistently receive the lowest gate values across all conditions, suggesting that these layers contribute more dispensable computations for the NTP objective. The pattern is remarkably consistent across ThreadGate, Uniform Gate, and PCGrad variants, indicating that gate-value allocation is driven primarily by the NTP loss landscape rather than the GAR auxiliary objective.
241	
242	\begin{figure}[H]
243	\centering
244	\includegraphics[width=\columnwidth]{fig_gate_profile_heatmap.pdf}
245	\caption{Per-layer gate values across training for Qwen-2.5-7B (28 layers $\times$ 5 conditions) and Llama-3.1-8B (32 layers $\times$ 1 condition). Early layers (L1, L4--5) consistently receive the lowest gate values across conditions.}
246	\label{fig:gate-heatmap}
247	\end{figure}
248	
249	\subsection{Cross-Model Gate Profile Comparison}
250	
251	Figure~\ref{fig:gate-crossmodel} compares gate profiles between the two architectures. Qwen-2.5-7B shows minimum gate values at early layers (L1\,=\,0.793, L5\,=\,0.797), suggesting these layers are most amenable to attenuation without disrupting NTP. Llama-3.1-8B instead shows a V-shaped valley at mid-to-late layers (L25\,=\,0.719), indicating that architecturally distinct models learn different layer-importance hierarchies. Both profiles converge toward identity at their respective final layers, consistent with NTP gradient pressure dominating gate optimization at output-adjacent layers.
252	
253	\begin{figure}[H]
254	\centering
255	\includegraphics[width=\columnwidth]{fig_gate_profile_crossmodel.pdf}
256	\caption{Side-by-side gate profiles for Qwen-2.5-7B and Llama-3.1-8B. Qwen dips at early layers (L1\,=\,0.793, L5\,=\,0.797), while Llama shows a V-shaped valley at mid-to-late layers (L25\,=\,0.719). Both models learn layer-selective gating but with architecture-dependent patterns.}
257	\label{fig:gate-crossmodel}
258	\end{figure}
259	
260	\subsection{Per-Turn AR GAR Decay}
261	
262	Figure~\ref{fig:ar-gar-perturn} visualizes the monotonic decay of GAR across conversation turns under autoregressive generation. Qwen base drops 85\% from turn 1 to turn 10; Llama base drops 90\%. The ThreadGate-trained model shows slight elevation in absolute GAR values but follows the same decay pattern, confirming that training-time GAR optimization does not alter the fundamental decay dynamic during generation. This per-turn view complements the aggregate TF-AR gap reported in Table~\ref{tab:five-way}: the gap is not a fixed offset but grows with conversation length, consistent with cumulative exposure bias.
263	
264	\begin{figure}[H]
265	\centering
266	\includegraphics[width=\columnwidth]{fig_ar_gar_perturn.pdf}
267	\caption{GAR decays monotonically across turns under autoregressive generation. Qwen base drops 85\% (turn 1$\to$10), Llama base drops 90\%. The ThreadGate-trained model (AR) shows slight elevation but the same decay pattern, confirming that training-time GAR optimization does not transfer to generation.}
268	\label{fig:ar-gar-perturn}
269	\end{figure}
270	
271	\subsection{Bootstrap Confidence Intervals}
272	
273	Figure~\ref{fig:bootstrap-ci} shows the bootstrap resampling distributions underlying the 95\% CIs reported in Table~\ref{tab:five-way}.
274	
275	\begin{figure}[H]
276	  \centering
277	  \includegraphics[width=\columnwidth]{fig_bootstrap_ci.pdf}
278	  \caption{Bootstrap CI distributions for AR GAR-ours (ThreadGate vs.\ LoRA-only, $N$\,=\,50, 10K resamples). Distributions overlap substantially, consistent with the modest effect size ($r$\,=\,0.454).}
279	  \label{fig:bootstrap-ci}
280	\end{figure}
281	
282	\subsection{Gate Value Distributions}
283	
284	Figure~\ref{fig:gate-distribution} shows the full distribution of per-layer gate values for ThreadGate, Uniform Gate, and PCGrad variants. All three converge to similar distributions (mean $\sim$0.94--0.96, concentrated between 0.9 and 1.0), confirming that the gating mechanism provides minimal modulation regardless of the specific variant. The distributions are right-skewed with a sharp cutoff at 1.0, reflecting NTP pressure pushing gates toward identity.
285	
286	\begin{figure}[H]
287	\centering
288	\includegraphics[width=\columnwidth]{fig_gate_distribution.pdf}
289	\caption{Per-layer gate value distributions for ThreadGate, Uniform Gate, and PCGrad variants. All three converge to similar distributions (mean $\sim$0.94--0.96), confirming minimal modulation from the gating mechanism.}
290	\label{fig:gate-distribution}
291	\end{figure}
292	
293	\subsection{Training Loss Curves}
294	
295	Figure~\ref{fig:training-loss} shows the NTP, GAR, and total loss trajectories during training. GAR loss collapses to near-zero within the first epoch across all variants, indicating rapid convergence of the auxiliary objective under teacher forcing. NTP loss converges normally to ${\sim}$0.93 by epoch 3. The fast GAR convergence is not itself pathological---it indicates successful optimization under the training distribution. The pathology emerges only at the transition to autoregressive generation, where the learned attention patterns fail to transfer.
296	
297	\begin{figure}[H]
298	\centering
299	\includegraphics[width=\columnwidth]{fig_training_loss_curves.pdf}
300	\caption{NTP, GAR, and total loss trajectories. GAR loss collapses to near-zero within the first epoch across all variants, while NTP loss converges normally.}
301	\label{fig:training-loss}
302	\end{figure}
303	
304	\subsection{Full Attention Steering Results}\label{sec:appendix-steering}
305	
306	\begin{table*}[t]
307	\centering\small
308	\caption{Full attention steering results across evaluation settings.
309	\textbf{Bold} indicates the operating point cited in the main text ($\beta$\,=\,5).
310	A visual gap separates the phase-transition boundary: GAR jumps sharply between $\beta$\,=\,2 and $\beta$\,=\,3 across all settings.}
311	\label{tab:steering-full}
312	\begin{tabular}{r cc cc cc}
313	\toprule
314	 & \multicolumn{2}{c}{\textbf{$N$\,=\,5, Gen}} & \multicolumn{2}{c}{\textbf{$N$\,=\,50, Gen}} & \multicolumn{2}{c}{\textbf{$N$\,=\,200, TF}} \\
315	\cmidrule(lr){2-3} \cmidrule(lr){4-5} \cmidrule(lr){6-7}
316	$\beta$ & GAR & PPL & GAR & PPL & GAR & PPL \\
317	\midrule
318	0   & .028 & 1.41 & $.064 \pm .081$ & $1.43 \pm .10$ & .535 & 2.62 \\
319	0.5 & .029 & 1.39 & ---             & ---             & ---  & ---  \\
320	1   & .035 & 1.36 & ---             & ---             & ---  & ---  \\
321	2   & .062 & 1.41 & $.128 \pm .110$ & $1.48 \pm .14$ & .611 & 2.69 \\
322	\addlinespace[3pt]
323	3   & ---  & ---  & $.556 \pm .060$ & $1.56 \pm .17$ & .788 & 2.93 \\
324	4   & ---  & ---  & $.644 \pm .061$ & $1.67 \pm .22$ & .817 & 3.49 \\
325	\textbf{5}  & \textbf{.680} & \textbf{1.91} & $\mathbf{.727 \pm .061}$ & $\mathbf{1.77 \pm .27}$ & \textbf{.833} & \textbf{6.15} \\
326	10  & .959 & 4.22 & $.961 \pm .015$ & $3.45 \pm 1.78$ & .977 & 505.2 \\
327	\bottomrule
328	\end{tabular}
329	\end{table*}
330	
331	\begin{figure}[t]
332	  \centering
333	  \includegraphics[width=\columnwidth]{fig_steering_standalone.pdf}
334	  \caption{Detailed $\beta$-steering trade-off ($N$\,=\,50). GAR-ours (top) increases monotonically with $\beta$; PPL (bottom) remains stable below $\beta$\,=\,3 (9\% cost), then rises sharply. The $\beta$\,=\,3 operating point (circled) achieves 8.7$\times$ GAR recovery while crossing the TF baseline, representing the optimal trade-off.}
335	  \label{fig:steering-standalone}
336	\end{figure}
337	
338	\section{Per-Layer Gate Profile}\label{sec:appendix-gate-profile}
339	
340	Table~\ref{tab:gate-profile} reports the final per-layer gate values for ThreadGate (seed 123) on Qwen-2.5-7B-Instruct (28 layers). Gate values are averaged across all tokens in the evaluation set. Layers 1 and 5 show the lowest gate values (0.793 and 0.797), indicating these layers are most amenable to attenuation without disrupting NTP. Layers 26--27 converge to $\geq$0.988, consistent with NTP gradient pressure dominating at output-adjacent layers. The mean across all layers is 0.947 ($\sigma$\,=\,0.051).
341	
342	\begin{table}[t]
343	\centering\small
344	\caption{Per-layer gate values for ThreadGate (seed 123) on Qwen-2.5-7B-Instruct. Min values (L1, L5) in bold.}
345	\label{tab:gate-profile}
346	\resizebox{\columnwidth}{!}{%
347	\begin{tabular}{cccccccc}
348	\toprule
349	L0 & L1 & L2 & L3 & L4 & L5 & L6 & L7 \\
350	.883 & \textbf{.793} & .996 & .988 & .984 & \textbf{.797} & .961 & .918 \\
351	\midrule
352	L8 & L9 & L10 & L11 & L12 & L13 & L14 & L15 \\
353	.965 & .934 & .969 & .918 & .926 & .941 & .930 & .965 \\
354	\midrule
355	L16 & L17 & L18 & L19 & L20 & L21 & L22 & L23 \\
356	.941 & .910 & .961 & .965 & .973 & .988 & .969 & .980 \\
357	\midrule
358	L24 & L25 & L26 & L27 & \multicolumn{4}{c}{Summary} \\
359	.980 & .984 & .988 & 1.00 & \multicolumn{4}{c}{$\bar{g}$\,=\,.947, $\sigma$\,=\,.051} \\
360	\bottomrule
361	\end{tabular}}
362	\end{table}
363	
364	The gate profile exhibits two notable patterns: (1)~a bimodal dip at L1 and L5, suggesting two distinct ``dispensable'' layer clusters in Qwen's architecture; (2)~monotonic increase from L17 to L27, indicating output-adjacent layers are progressively more critical for NTP. Seed 42 produces a similar profile (mean 0.934, min at L3--L5), confirming the pattern is not seed-dependent.
365	
366	\paragraph{Cross-model comparison.} See \S\ref{sec:appendix-viz} for the full cross-model gate profile comparison (Figure~\ref{fig:gate-crossmodel}). Llama-3.1-8B shows a qualitatively different profile---a V-shaped valley at mid-to-late layers rather than early-layer dips---suggesting architecture-dependent layer importance hierarchies.
367	
368	\section{Scheduled Sampling Implementation}\label{sec:appendix-ss}
369	
370	Our scheduled sampling implementation follows \citet{bengio2015scheduled} with modifications for multi-turn transformer training:
371	
372	\paragraph{Sampling schedule.} The model-generated context ratio $\rho$ increases linearly from 0 to 0.3 over 3 epochs. At each training step, a Bernoulli trial with probability $\rho$ determines whether the input prefix is replaced with model-generated tokens. The effective usage rate (29.7--37.1\%) is lower than the nominal schedule due to per-sample Bernoulli variance.
373	
374	\paragraph{Context generation.} When model-generated context is selected, the model autoregressively generates the assistant turns from the conversation prefix up to the current training position. The generated tokens replace the ground-truth assistant tokens in the input, while user turns remain unchanged. This preserves the multi-turn structure while introducing distributional diversity in the conditioning context.
375	
376	\paragraph{Training dynamics.} The scheduled sampling variant converges to similar final loss (NTP 0.932 vs.\ 0.930 for standard ThreadGate) but with higher variance in early epochs due to the stochastic context mixing (Figure~\ref{fig:ss-dynamics}). Gate profiles remain similar (mean 0.953 vs.\ 0.947, min at L4 vs.\ L1), indicating that scheduled sampling does not fundamentally alter gate optimization but rather improves the robustness of the learned attention patterns to distributional shift. Training time increases by 8--80\% across seeds (seed-dependent; dominated by GAR forward pass overhead): 6.5h (seed 42), 10.8h (seed 123), and 6.5h (seed 456) vs.\ 6.0h for standard ThreadGate on Qwen. Seed 456 exhibits consistent training dynamics with seeds 42 and 123.
377	
378	\begin{figure}[t]
379	  \centering
380	  \includegraphics[width=\columnwidth]{fig_ss_training_dynamics.pdf}
381	  \caption{Scheduled sampling training dynamics: sampling ratio $\rho$ ramps linearly from 0 to 0.3 (left axis); GAR loss (right axis) shows higher early-epoch variance due to stochastic context mixing.}
382	  \label{fig:ss-dynamics}
383	\end{figure}
384	
385	\section{Computational Cost Analysis}\label{sec:appendix-cost}
386	
387	\begin{table}[t]
388	\centering\small
389	\caption{Computational cost across training configurations. All experiments use a single NVIDIA RTX PRO 6000 (96\,GB VRAM).}
390	\label{tab:cost}
391	\resizebox{\columnwidth}{!}{%
392	\begin{tabular}{lcccc}
393	\toprule
394	\textbf{Config} & \textbf{Params} & \textbf{Time (h)} & \textbf{VRAM} & \textbf{Overhead} \\
395	\midrule
396	\multicolumn{5}{l}{\emph{Qwen-2.5-7B-Instruct}} \\
397	LoRA-only & 4.2M & 6.0 & 42\,GB & baseline \\
398	ThreadGate & 4.3M & 6.0 & 43\,GB & $+$57K \\
399	\;+\,PCGrad & 4.3M & 8.0 & 43\,GB & $+$33\% \\
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "21ec9fc7-6186-497c-826b-32ed3e4fd0d5",
  "isSidechain": false,
  "promptId": "b0f005fa-c14f-47e1-bf29-f3925462c4b7",
  "type": "user",
  "uuid": "6c8dcc34-6b12-4c1b-a959-ec0ec34b2780",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex",
      "content": "\\begin{figure}[t]\n  \\centering\n  \\includegraphics[width=\\columnwidth]{fig_crossmodel.pdf}\n  \\caption{Cross-architecture validation. (a)~The TF-AR gap persists on Llama-3.1-8B (27$\\times$ by median), exceeding Qwen's 8$\\times$. (b)~Gate profiles on normalized depth: Qwen dips at early layers, Llama at late layers; architecture-dependent patterns, but both converge toward identity.}\n  \\label{fig:crossmodel}\n\\end{figure}\n\n\\paragraph{Cross-model summary.} Table~\\ref{tab:crossmodel-detail} consolidates the cross-model comparison, showing TF GAR, AR GAR, PPL, and gap ratios side by side for both architectures. The consistent pattern---TF GAR $\\approx$ 0.5, AR GAR $\\ll$ 0.1, gap $\\geq$ 7.9$\\times$---across two architectures with different layer counts, attention head configurations, and pre-training corpora provides strong evidence that exposure bias is architecture-independent. Notably, Llama's larger gaps (27$\\times$ by median for TG; mean-based range 11.2--17.2$\\times$) compared to Qwen's (7.9--13.5$\\times$) may reflect its deeper architecture (32 vs.\\ 28 layers), which allows more layers for distributional drift to compound through.\n\n\\input{../artifacts/appendix_expansion/tab_crossmodel_detail.tex}\n\n\\paragraph{GAR-Dongre cross-model comparison.} GAR-Dongre shows negligible distribution shift on Llama (AR/TF ratio 1.002$\\times$), compared to 1.28$\\times$ on Qwen. This confirms the mechanism specificity finding: exposure bias selectively disrupts the concentrated last-token attention pattern (GAR-ours) while leaving the diffuse all-token attention (GAR-Dongre) unaffected across both architectures.\n\n\\paragraph{Training details.} Llama variants used the same pipeline as Qwen: 8K UltraChat conversations, LoRA rank 16 targeting $q$/$v$ projections, 3 epochs. Training loss converged to 0.929 (LoRA-only) and 0.934 (ThreadGate); the slight difference is attributable to the additional GAR loss component. Wall-clock time was 7.0h (LoRA-only) and 7.3h (ThreadGate), approximately 17\\% longer than Qwen due to Llama's larger layer count (32 vs.\\ 28 layers).\n\n\\paragraph{Phase 1 diagnostics.} Before fine-tuning, we confirmed that Llama exhibits the same goal attention decay as Qwen. Base model GAR decays from 0.026 (turn 1) to 0.003 (turn 10), a 90\\% decline. This is steeper than Qwen's 70.8\\% decline, suggesting that attention decay may be more severe in Llama's architecture despite its larger head count (32 vs.\\ 28 KV heads).\n\n\\paragraph{Cross-model gradient analysis.} Table~\\ref{tab:gradient-crossmodel} compares NTP--GAR gradient interaction between the two architectures. Both models exhibit near-orthogonal gradients (cosine similarity $\\approx$\\,0), not systematic conflict: Qwen shows a slight negative mean ($-$0.042) while Llama is marginally positive (+0.005). NTP gradients dominate GAR by 14.7$\\times$ on Qwen and 25.7$\\times$ on Llama, indicating that the auxiliary signal is overwhelmed by magnitude rather than opposed by direction. The cross-model consistency---near-zero cosine similarity and order-of-magnitude NTP dominance on both architectures---reinforces the \\emph{modus tollens} argument (\\S\\ref{subsec:pcgrad}): gradient direction conflict is not the primary cause of the TF-AR gap.\n\n\\begin{table}[t]\n\\centering\\small\n\\caption{Cross-model NTP--GAR gradient interaction. Gradients are near-orthogonal on both architectures; NTP magnitude dominates GAR by 15--26$\\times$.}\n\\label{tab:gradient-crossmodel}\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Metric} & \\textbf{Qwen-7B} & \\textbf{Llama-8B} \\\\\n\\midrule\nMean cos sim & $-$0.042 & +0.005 \\\\\nNeg-layer \\% & 67.9\\% & 53.1\\% \\\\\nNTP/GAR mag ratio & 14.7$\\times$ & 25.7$\\times$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Additional Visualizations}\\label{sec:appendix-viz}\n\nThis section presents extended visualizations referenced in the main text. Each figure examines a different aspect of the gating behavior and its failure under autoregressive generation.\n\n\\subsection{Gate Profile Heatmap}\n\nFigure~\\ref{fig:gate-heatmap} shows the per-layer gate values across all training configurations for both Qwen-2.5-7B (28 layers) and Llama-3.1-8B (32 layers). The key observation is that early layers consistently receive the lowest gate values across all conditions, suggesting that these layers contribute more dispensable computations for the NTP objective. The pattern is remarkably consistent across ThreadGate, Uniform Gate, and PCGrad variants, indicating that gate-value allocation is driven primarily by the NTP loss landscape rather than the GAR auxiliary objective.\n\n\\begin{figure}[H]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig_gate_profile_heatmap.pdf}\n\\caption{Per-layer gate values across training for Qwen-2.5-7B (28 layers $\\times$ 5 conditions) and Llama-3.1-8B (32 layers $\\times$ 1 condition). Early layers (L1, L4--5) consistently receive the lowest gate values across conditions.}\n\\label{fig:gate-heatmap}\n\\end{figure}\n\n\\subsection{Cross-Model Gate Profile Comparison}\n\nFigure~\\ref{fig:gate-crossmodel} compares gate profiles between the two architectures. Qwen-2.5-7B shows minimum gate values at early layers (L1\\,=\\,0.793, L5\\,=\\,0.797), suggesting these layers are most amenable to attenuation without disrupting NTP. Llama-3.1-8B instead shows a V-shaped valley at mid-to-late layers (L25\\,=\\,0.719), indicating that architecturally distinct models learn different layer-importance hierarchies. Both profiles converge toward identity at their respective final layers, consistent with NTP gradient pressure dominating gate optimization at output-adjacent layers.\n\n\\begin{figure}[H]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig_gate_profile_crossmodel.pdf}\n\\caption{Side-by-side gate profiles for Qwen-2.5-7B and Llama-3.1-8B. Qwen dips at early layers (L1\\,=\\,0.793, L5\\,=\\,0.797), while Llama shows a V-shaped valley at mid-to-late layers (L25\\,=\\,0.719). Both models learn layer-selective gating but with architecture-dependent patterns.}\n\\label{fig:gate-crossmodel}\n\\end{figure}\n\n\\subsection{Per-Turn AR GAR Decay}\n\nFigure~\\ref{fig:ar-gar-perturn} visualizes the monotonic decay of GAR across conversation turns under autoregressive generation. Qwen base drops 85\\% from turn 1 to turn 10; Llama base drops 90\\%. The ThreadGate-trained model shows slight elevation in absolute GAR values but follows the same decay pattern, confirming that training-time GAR optimization does not alter the fundamental decay dynamic during generation. This per-turn view complements the aggregate TF-AR gap reported in Table~\\ref{tab:five-way}: the gap is not a fixed offset but grows with conversation length, consistent with cumulative exposure bias.\n\n\\begin{figure}[H]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig_ar_gar_perturn.pdf}\n\\caption{GAR decays monotonically across turns under autoregressive generation. Qwen base drops 85\\% (turn 1$\\to$10), Llama base drops 90\\%. The ThreadGate-trained model (AR) shows slight elevation but the same decay pattern, confirming that training-time GAR optimization does not transfer to generation.}\n\\label{fig:ar-gar-perturn}\n\\end{figure}\n\n\\subsection{Bootstrap Confidence Intervals}\n\nFigure~\\ref{fig:bootstrap-ci} shows the bootstrap resampling distributions underlying the 95\\% CIs reported in Table~\\ref{tab:five-way}.\n\n\\begin{figure}[H]\n  \\centering\n  \\includegraphics[width=\\columnwidth]{fig_bootstrap_ci.pdf}\n  \\caption{Bootstrap CI distributions for AR GAR-ours (ThreadGate vs.\\ LoRA-only, $N$\\,=\\,50, 10K resamples). Distributions overlap substantially, consistent with the modest effect size ($r$\\,=\\,0.454).}\n  \\label{fig:bootstrap-ci}\n\\end{figure}\n\n\\subsection{Gate Value Distributions}\n\nFigure~\\ref{fig:gate-distribution} shows the full distribution of per-layer gate values for ThreadGate, Uniform Gate, and PCGrad variants. All three converge to similar distributions (mean $\\sim$0.94--0.96, concentrated between 0.9 and 1.0), confirming that the gating mechanism provides minimal modulation regardless of the specific variant. The distributions are right-skewed with a sharp cutoff at 1.0, reflecting NTP pressure pushing gates toward identity.\n\n\\begin{figure}[H]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig_gate_distribution.pdf}\n\\caption{Per-layer gate value distributions for ThreadGate, Uniform Gate, and PCGrad variants. All three converge to similar distributions (mean $\\sim$0.94--0.96), confirming minimal modulation from the gating mechanism.}\n\\label{fig:gate-distribution}\n\\end{figure}\n\n\\subsection{Training Loss Curves}\n\nFigure~\\ref{fig:training-loss} shows the NTP, GAR, and total loss trajectories during training. GAR loss collapses to near-zero within the first epoch across all variants, indicating rapid convergence of the auxiliary objective under teacher forcing. NTP loss converges normally to ${\\sim}$0.93 by epoch 3. The fast GAR convergence is not itself pathological---it indicates successful optimization under the training distribution. The pathology emerges only at the transition to autoregressive generation, where the learned attention patterns fail to transfer.\n\n\\begin{figure}[H]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig_training_loss_curves.pdf}\n\\caption{NTP, GAR, and total loss trajectories. GAR loss collapses to near-zero within the first epoch across all variants, while NTP loss converges normally.}\n\\label{fig:training-loss}\n\\end{figure}\n\n\\subsection{Full Attention Steering Results}\\label{sec:appendix-steering}\n\n\\begin{table*}[t]\n\\centering\\small\n\\caption{Full attention steering results across evaluation settings.\n\\textbf{Bold} indicates the operating point cited in the main text ($\\beta$\\,=\\,5).\nA visual gap separates the phase-transition boundary: GAR jumps sharply between $\\beta$\\,=\\,2 and $\\beta$\\,=\\,3 across all settings.}\n\\label{tab:steering-full}\n\\begin{tabular}{r cc cc cc}\n\\toprule\n & \\multicolumn{2}{c}{\\textbf{$N$\\,=\\,5, Gen}} & \\multicolumn{2}{c}{\\textbf{$N$\\,=\\,50, Gen}} & \\multicolumn{2}{c}{\\textbf{$N$\\,=\\,200, TF}} \\\\\n\\cmidrule(lr){2-3} \\cmidrule(lr){4-5} \\cmidrule(lr){6-7}\n$\\beta$ & GAR & PPL & GAR & PPL & GAR & PPL \\\\\n\\midrule\n0   & .028 & 1.41 & $.064 \\pm .081$ & $1.43 \\pm .10$ & .535 & 2.62 \\\\\n0.5 & .029 & 1.39 & ---             & ---             & ---  & ---  \\\\\n1   & .035 & 1.36 & ---             & ---             & ---  & ---  \\\\\n2   & .062 & 1.41 & $.128 \\pm .110$ & $1.48 \\pm .14$ & .611 & 2.69 \\\\\n\\addlinespace[3pt]\n3   & ---  & ---  & $.556 \\pm .060$ & $1.56 \\pm .17$ & .788 & 2.93 \\\\\n4   & ---  & ---  & $.644 \\pm .061$ & $1.67 \\pm .22$ & .817 & 3.49 \\\\\n\\textbf{5}  & \\textbf{.680} & \\textbf{1.91} & $\\mathbf{.727 \\pm .061}$ & $\\mathbf{1.77 \\pm .27}$ & \\textbf{.833} & \\textbf{6.15} \\\\\n10  & .959 & 4.22 & $.961 \\pm .015$ & $3.45 \\pm 1.78$ & .977 & 505.2 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\n\\begin{figure}[t]\n  \\centering\n  \\includegraphics[width=\\columnwidth]{fig_steering_standalone.pdf}\n  \\caption{Detailed $\\beta$-steering trade-off ($N$\\,=\\,50). GAR-ours (top) increases monotonically with $\\beta$; PPL (bottom) remains stable below $\\beta$\\,=\\,3 (9\\% cost), then rises sharply. The $\\beta$\\,=\\,3 operating point (circled) achieves 8.7$\\times$ GAR recovery while crossing the TF baseline, representing the optimal trade-off.}\n  \\label{fig:steering-standalone}\n\\end{figure}\n\n\\section{Per-Layer Gate Profile}\\label{sec:appendix-gate-profile}\n\nTable~\\ref{tab:gate-profile} reports the final per-layer gate values for ThreadGate (seed 123) on Qwen-2.5-7B-Instruct (28 layers). Gate values are averaged across all tokens in the evaluation set. Layers 1 and 5 show the lowest gate values (0.793 and 0.797), indicating these layers are most amenable to attenuation without disrupting NTP. Layers 26--27 converge to $\\geq$0.988, consistent with NTP gradient pressure dominating at output-adjacent layers. The mean across all layers is 0.947 ($\\sigma$\\,=\\,0.051).\n\n\\begin{table}[t]\n\\centering\\small\n\\caption{Per-layer gate values for ThreadGate (seed 123) on Qwen-2.5-7B-Instruct. Min values (L1, L5) in bold.}\n\\label{tab:gate-profile}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{cccccccc}\n\\toprule\nL0 & L1 & L2 & L3 & L4 & L5 & L6 & L7 \\\\\n.883 & \\textbf{.793} & .996 & .988 & .984 & \\textbf{.797} & .961 & .918 \\\\\n\\midrule\nL8 & L9 & L10 & L11 & L12 & L13 & L14 & L15 \\\\\n.965 & .934 & .969 & .918 & .926 & .941 & .930 & .965 \\\\\n\\midrule\nL16 & L17 & L18 & L19 & L20 & L21 & L22 & L23 \\\\\n.941 & .910 & .961 & .965 & .973 & .988 & .969 & .980 \\\\\n\\midrule\nL24 & L25 & L26 & L27 & \\multicolumn{4}{c}{Summary} \\\\\n.980 & .984 & .988 & 1.00 & \\multicolumn{4}{c}{$\\bar{g}$\\,=\\,.947, $\\sigma$\\,=\\,.051} \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\nThe gate profile exhibits two notable patterns: (1)~a bimodal dip at L1 and L5, suggesting two distinct ``dispensable'' layer clusters in Qwen's architecture; (2)~monotonic increase from L17 to L27, indicating output-adjacent layers are progressively more critical for NTP. Seed 42 produces a similar profile (mean 0.934, min at L3--L5), confirming the pattern is not seed-dependent.\n\n\\paragraph{Cross-model comparison.} See \\S\\ref{sec:appendix-viz} for the full cross-model gate profile comparison (Figure~\\ref{fig:gate-crossmodel}). Llama-3.1-8B shows a qualitatively different profile---a V-shaped valley at mid-to-late layers rather than early-layer dips---suggesting architecture-dependent layer importance hierarchies.\n\n\\section{Scheduled Sampling Implementation}\\label{sec:appendix-ss}\n\nOur scheduled sampling implementation follows \\citet{bengio2015scheduled} with modifications for multi-turn transformer training:\n\n\\paragraph{Sampling schedule.} The model-generated context ratio $\\rho$ increases linearly from 0 to 0.3 over 3 epochs. At each training step, a Bernoulli trial with probability $\\rho$ determines whether the input prefix is replaced with model-generated tokens. The effective usage rate (29.7--37.1\\%) is lower than the nominal schedule due to per-sample Bernoulli variance.\n\n\\paragraph{Context generation.} When model-generated context is selected, the model autoregressively generates the assistant turns from the conversation prefix up to the current training position. The generated tokens replace the ground-truth assistant tokens in the input, while user turns remain unchanged. This preserves the multi-turn structure while introducing distributional diversity in the conditioning context.\n\n\\paragraph{Training dynamics.} The scheduled sampling variant converges to similar final loss (NTP 0.932 vs.\\ 0.930 for standard ThreadGate) but with higher variance in early epochs due to the stochastic context mixing (Figure~\\ref{fig:ss-dynamics}). Gate profiles remain similar (mean 0.953 vs.\\ 0.947, min at L4 vs.\\ L1), indicating that scheduled sampling does not fundamentally alter gate optimization but rather improves the robustness of the learned attention patterns to distributional shift. Training time increases by 8--80\\% across seeds (seed-dependent; dominated by GAR forward pass overhead): 6.5h (seed 42), 10.8h (seed 123), and 6.5h (seed 456) vs.\\ 6.0h for standard ThreadGate on Qwen. Seed 456 exhibits consistent training dynamics with seeds 42 and 123.\n\n\\begin{figure}[t]\n  \\centering\n  \\includegraphics[width=\\columnwidth]{fig_ss_training_dynamics.pdf}\n  \\caption{Scheduled sampling training dynamics: sampling ratio $\\rho$ ramps linearly from 0 to 0.3 (left axis); GAR loss (right axis) shows higher early-epoch variance due to stochastic context mixing.}\n  \\label{fig:ss-dynamics}\n\\end{figure}\n\n\\section{Computational Cost Analysis}\\label{sec:appendix-cost}\n\n\\begin{table}[t]\n\\centering\\small\n\\caption{Computational cost across training configurations. All experiments use a single NVIDIA RTX PRO 6000 (96\\,GB VRAM).}\n\\label{tab:cost}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Config} & \\textbf{Params} & \\textbf{Time (h)} & \\textbf{VRAM} & \\textbf{Overhead} \\\\\n\\midrule\n\\multicolumn{5}{l}{\\emph{Qwen-2.5-7B-Instruct}} \\\\\nLoRA-only & 4.2M & 6.0 & 42\\,GB & baseline \\\\\nThreadGate & 4.3M & 6.0 & 43\\,GB & $+$57K \\\\\n\\;+\\,PCGrad & 4.3M & 8.0 & 43\\,GB & $+$33\\% \\\\",
      "numLines": 200,
      "startLine": 200,
      "totalLines": 851
    }
  },
  "sourceToolAssistantUUID": "21ec9fc7-6186-497c-826b-32ed3e4fd0d5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921",
  "sessionId": "5d779602-0719-4d06-8bf9-fdd84990d5d0",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---


### Tool call

_source line 76 · 2026-05-25T20:38:28.572Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01EVKskL9sGfQzkvEofcnPmV`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_11 && git log --oneline -10",
  "description": "Check recent commits"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6c8dcc34-6b12-4c1b-a959-ec0ec34b2780",
  "isSidechain": false,
  "requestId": "req_011CbPvhoPPLcGrV1ZyCdTeR",
  "type": "assistant",
  "uuid": "d4f16c4f-25d0-4bf4-969e-a7bbb1b26870",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921",
  "sessionId": "5d779602-0719-4d06-8bf9-fdd84990d5d0",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Nz8YsY9jpcaw3eQYNuT6Ri",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 24430,
      "cache_read_input_tokens": 51522,
      "output_tokens": 12020,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 24430,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 12020,
          "cache_read_input_tokens": 51522,
          "cache_creation_input_tokens": 24430,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 24430
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

_source line 77_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[系统通知 — worker_done:worker_audit_appendix_tables_20260525T201208]: Worker worker_audit_appendix_tables_20260525T201208 已完成（status=done），请审查 Agent 的处理结果。",
  "leafUuid": "d4f16c4f-25d0-4bf4-969e-a7bbb1b26870",
  "sessionId": "5d779602-0719-4d06-8bf9-fdd84990d5d0"
}
```

---


### Runtime record

_source line 78_

```json
{
  "type": "ai-title",
  "aiTitle": "Review worker audit appendix tables completion",
  "sessionId": "5d779602-0719-4d06-8bf9-fdd84990d5d0"
}
```

---


### Tool result

_source line 79 · 2026-05-25T20:38:28.797Z_

<details><summary>↩ Tool result · reported error · `toolu_01EVKskL9sGfQzkvEofcnPmV`</summary>

```text
Exit code 128
fatal: not a git repository (or any of the parent directories): .git
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d4f16c4f-25d0-4bf4-969e-a7bbb1b26870",
  "isSidechain": false,
  "promptId": "b0f005fa-c14f-47e1-bf29-f3925462c4b7",
  "type": "user",
  "uuid": "cabb26c8-4a6f-4d29-a474-40e122f6a6e4",
  "toolUseResult": "Error: Exit code 128\nfatal: not a git repository (or any of the parent directories): .git",
  "sourceToolAssistantUUID": "d4f16c4f-25d0-4bf4-969e-a7bbb1b26870",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921",
  "sessionId": "5d779602-0719-4d06-8bf9-fdd84990d5d0",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---


### Tool call

_source line 80 · 2026-05-25T20:38:33.764Z_

<details open><summary>🔧 Tool call — Read · `toolu_01CrCcnfAShjWtC3AnHpR7uJ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex",
  "offset": 390,
  "limit": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cabb26c8-4a6f-4d29-a474-40e122f6a6e4",
  "isSidechain": false,
  "requestId": "req_011CbPvydiQya2dyfYTDhTyF",
  "type": "assistant",
  "uuid": "fbb7371c-ee14-4bd7-b6d6-0e9adf0b3609",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921",
  "sessionId": "5d779602-0719-4d06-8bf9-fdd84990d5d0",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0111pyAGatAL7GziMBNNZN5U",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 17839,
      "cache_read_input_tokens": 75952,
      "output_tokens": 218,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 17839,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 218,
          "cache_read_input_tokens": 75952,
          "cache_creation_input_tokens": 17839,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 17839
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

_source line 81 · 2026-05-25T20:38:33.770Z_

<details><summary>↩ Tool result · `toolu_01CrCcnfAShjWtC3AnHpR7uJ`</summary>

```text
390	\label{tab:cost}
391	\resizebox{\columnwidth}{!}{%
392	\begin{tabular}{lcccc}
393	\toprule
394	\textbf{Config} & \textbf{Params} & \textbf{Time (h)} & \textbf{VRAM} & \textbf{Overhead} \\
395	\midrule
396	\multicolumn{5}{l}{\emph{Qwen-2.5-7B-Instruct}} \\
397	LoRA-only & 4.2M & 6.0 & 42\,GB & baseline \\
398	ThreadGate & 4.3M & 6.0 & 43\,GB & $+$57K \\
399	\;+\,PCGrad & 4.3M & 8.0 & 43\,GB & $+$33\% \\
400	Uniform Gate & 4.3M & 6.0 & 43\,GB & $+$57K \\
401	SS (s42) & 4.3M & 6.5 & 43\,GB & $+$8\% \\
402	SS (s123) & 4.3M & 10.8 & 43\,GB & $+$80\% \\
403	SS (s456) & 4.3M & 6.5 & 43\,GB & $+$8\% \\
404	\midrule
405	\multicolumn{5}{l}{\emph{Llama-3.1-8B-Instruct}} \\
406	LoRA-only & 4.2M & 7.0 & 45\,GB & baseline \\
407	ThreadGate & 4.3M & 7.3 & 46\,GB & $+$65K \\
408	\bottomrule
409	\end{tabular}}
410	\end{table}
411	
412	\paragraph{Parameter overhead.} ThreadGate adds ${\sim}$57K gate parameters for Qwen-2.5-7B (28 layers $\times$ 2K per gate MLP) and ${\sim}$65K for Llama-3.1-8B (32 layers), representing $<$0.001\% of the base model. LoRA adapters (rank 16, targeting $q$/$v$ projections) contribute 4.2M parameters across both architectures.
413	
414	\paragraph{Training time.} Standard variants (ThreadGate, Uniform Gate, LoRA-only) train in 6.0--7.3 hours. PCGrad adds ${\sim}$33\% overhead due to the per-step gradient projection computation. Scheduled sampling overhead varies: seed 42 adds only 8\% (6.5h) due to efficient batched generation, while seed 123 adds 80\% (10.8h) because of a longer generation schedule. The difference is due to the extended AR generation schedule in the seed 123 variant.
415	
416	\paragraph{Inference overhead.} Gate computation at inference time is negligible: a single 32$\to$64$\to$1 MLP forward pass per layer adds $<$0.1\% latency. $\beta$-steering requires identifying goal tokens (a one-time operation per conversation) and adding a constant bias to attention logits, with zero additional parameters.
417	
418	\section{Qualitative Steering Examples}\label{sec:appendix-examples}
419	
420	Table~\ref{tab:examples} illustrates the effect of $\beta$-steering on model behavior in a 4-turn conversation where the system prompt instructs ``Always respond in exactly three bullet points.''
421	
422	\begin{table*}[t]
423	\centering\small
424	\caption{Qualitative effect of $\beta$-steering on instruction following across conversation turns. System prompt: ``Always respond in exactly three bullet points.'' ThreadGate checkpoint, 4-turn conversation.}
425	\label{tab:examples}
426	\begin{tabular}{c p{5.5cm} p{5.5cm}}
427	\toprule
428	\textbf{Turn} & \textbf{$\beta$\,=\,0 (unsteered)} & \textbf{$\beta$\,=\,3 (steered)} \\
429	\midrule
430	1 & \checkmark~Three bullet points, on-topic & \checkmark~Three bullet points, on-topic \\
431	2 & \checkmark~Three bullet points, relevant & \checkmark~Three bullet points, relevant \\
432	3 & $\sim$~Four bullet points, partially on-topic & \checkmark~Three bullet points, on-topic \\
433	4 & \texttimes~Free-form paragraph, no bullets & \checkmark~Three bullet points, on-topic \\
434	\bottomrule
435	\end{tabular}
436	\end{table*}
437	
438	The pattern is consistent with the GAR decay analysis (\S\ref{sec:analysis}): unsteered models progressively lose attention to the system-prompt constraint, leading to format violations at later turns. Steering maintains goal-token attention, preserving instruction compliance. The per-category breakdown in Table~\ref{tab:ir-results} shows that content constraints benefit most from this effect.
439	
440	\section{Gradient Conflict Analysis}\label{sec:appendix-gradient}
441	
442	\begin{figure}[t]
443	  \centering
444	  \includegraphics[width=\columnwidth,height=0.42\textheight,keepaspectratio]{fig2_training_pcgrad.pdf}
445	  \caption{(a)~Training GAR convergence to target ($\tau$\,=\,0.5). (b)~PCGrad removes gradient conflict but $\mathcal{L}_\text{GAR}$ still collapses, confirming that gradient direction conflict is not the primary cause (\S\ref{subsec:pcgrad}).}
446	  \label{fig:training-pcgrad}
447	\end{figure}
448	
449	This section provides extended gradient interaction analysis supporting the PCGrad exclusion argument in \S\ref{subsec:pcgrad}. We measure per-layer cosine similarity between NTP and GAR gradients, gradient magnitude ratios, and the effect of PCGrad projection on these quantities.
450	
451	\paragraph{Gradient direction analysis.} Figure~\ref{fig:gradient-heatmap} visualizes the per-layer cosine similarity between NTP and GAR gradients across training epochs for both standard ThreadGate and PCGrad training. Under standard training, 79\% of layers show negative cosine similarity (gradient conflict) at epoch~0, declining to 68\% by epoch~2 as GAR loss converges to near-zero. This decline reflects diminishing GAR gradient magnitude rather than alignment improvement---as GAR loss approaches zero, the GAR gradient shrinks proportionally, making cosine similarity measurements less reliable (small gradients produce noisy direction estimates). Under PCGrad training, the conflict percentage decreases more slowly (79\%$\to$71\%), consistent with PCGrad projecting conflicting gradients onto the other's normal plane but not eliminating the underlying gradient conflict.
452	
453	\paragraph{Spatial patterns.} The early layers (L0--L5) and output-adjacent layers (L24--L27) show the strongest conflict, corresponding to the layers where gate values deviate most from identity (Figure~\ref{fig:gate-heatmap}). This spatial correlation is not causal: removing gradient conflict via PCGrad does not improve AR GAR, and gates at high-conflict layers are not systematically different from gates at low-conflict layers (Spearman $\rho$\,=\,$-$0.12, $p$\,=\,0.54 between gate value and conflict magnitude).
454	
455	\paragraph{Magnitude dominance.} NTP gradient magnitude dominates GAR by 7.5$\times$ at epoch~0 and 14.7$\times$ by epoch~2, as GAR loss converges while NTP loss remains at $\sim$0.93. This growing dominance means that even when directions oppose, the effective update direction is determined almost entirely by NTP. PCGrad addresses gradient conflict but not magnitude dominance---it projects conflicting gradients onto the other's normal plane (changing direction) but preserves relative magnitudes. The 7.5--14.7$\times$ magnitude ratio means that even after PCGrad projection, GAR contributes $<$7\% of the effective update magnitude, explaining why PCGrad is ineffective.
456	
457	\paragraph{Cross-model consistency.} Table~\ref{tab:gradient-crossmodel} confirms the pattern on Llama-3.1-8B: gradients are near-orthogonal (mean cosine $+$0.005, essentially zero) rather than systematically conflicting, with 25.7$\times$ NTP dominance. The Llama result is particularly informative because it shows that even without systematic gradient conflict (53\% negative layers, near chance), the same TF-AR gap persists. This cross-model evidence strengthens the \textit{modus tollens} argument: if gradient conflict were the cause, it should be present on both architectures; it is absent on Llama, yet the gap persists; therefore gradient direction conflict is not the primary cause.
458	
459	\begin{figure*}[t]
460	\centering
461	\includegraphics[width=0.95\textwidth]{fig_gradient_conflict_heatmap.pdf}
462	\caption{Per-layer cosine similarity between NTP and GAR gradients across training epochs. (a)~Standard training: conflict decreases from 79\% to 68\% of layers as GAR loss vanishes. (b)~PCGrad training: projection reduces conflict more slowly (79\%$\to$71\%) but does not improve AR GAR, ruling out gradient direction conflict as the primary cause (\S\ref{subsec:pcgrad}).}
463	\label{fig:gradient-heatmap}
464	\end{figure*}
465	
466	\section{Training Data Characteristics}\label{sec:appendix-data}
467	
468	All experiments use 8,000 multi-turn conversations sampled from the UltraChat \citep{ding2023ultrachat} training split. Table~\ref{tab:data-stats} summarizes the dataset characteristics. Conversations are truncated to 2,048 tokens; conversations shorter than 3 user turns are excluded to ensure sufficient multi-turn structure for GAR computation. The held-out evaluation sets use separate non-overlapping samples: $N$\,=\,50 conversations (mean 3.6 user turns) for the primary AR evaluation and $N$\,=\,5 conversations (10 turns each) for the long-conversation analysis (Appendix~\ref{sec:appendix-n5}).
469	
470	\begin{table}[t]
471	\centering\small
472	\caption{Training and evaluation data characteristics. All data from UltraChat \citep{ding2023ultrachat}.}
473	\label{tab:data-stats}
474	\begin{tabular}{lcc}
475	\toprule
476	\textbf{Property} & \textbf{Train} & \textbf{Eval (primary)} \\
477	\midrule
478	Conversations & 8,000 & 50 \\
479	Min user turns & 3 & 3 \\
480	Max sequence length & 2,048 & 2,048 \\
481	Source & UltraChat train & UltraChat train \\
482	Overlap & --- & non-overlapping \\
483	\bottomrule
484	\end{tabular}
485	\end{table}
486	
487	\section{Exposure Bias Scaling}\label{sec:appendix-eb-scaling}
488	
489	Figure~\ref{fig:eb-scaling} quantifies two scaling dimensions of the exposure bias phenomenon: cross-variant gap ratios (panel~a) and length-dependent gap compounding (panel~b).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fbb7371c-ee14-4bd7-b6d6-0e9adf0b3609",
  "isSidechain": false,
  "promptId": "b0f005fa-c14f-47e1-bf29-f3925462c4b7",
  "type": "user",
  "uuid": "4d35af4f-3598-4a8e-bff2-d645353c0108",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex",
      "content": "\\label{tab:cost}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Config} & \\textbf{Params} & \\textbf{Time (h)} & \\textbf{VRAM} & \\textbf{Overhead} \\\\\n\\midrule\n\\multicolumn{5}{l}{\\emph{Qwen-2.5-7B-Instruct}} \\\\\nLoRA-only & 4.2M & 6.0 & 42\\,GB & baseline \\\\\nThreadGate & 4.3M & 6.0 & 43\\,GB & $+$57K \\\\\n\\;+\\,PCGrad & 4.3M & 8.0 & 43\\,GB & $+$33\\% \\\\\nUniform Gate & 4.3M & 6.0 & 43\\,GB & $+$57K \\\\\nSS (s42) & 4.3M & 6.5 & 43\\,GB & $+$8\\% \\\\\nSS (s123) & 4.3M & 10.8 & 43\\,GB & $+$80\\% \\\\\nSS (s456) & 4.3M & 6.5 & 43\\,GB & $+$8\\% \\\\\n\\midrule\n\\multicolumn{5}{l}{\\emph{Llama-3.1-8B-Instruct}} \\\\\nLoRA-only & 4.2M & 7.0 & 45\\,GB & baseline \\\\\nThreadGate & 4.3M & 7.3 & 46\\,GB & $+$65K \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\\paragraph{Parameter overhead.} ThreadGate adds ${\\sim}$57K gate parameters for Qwen-2.5-7B (28 layers $\\times$ 2K per gate MLP) and ${\\sim}$65K for Llama-3.1-8B (32 layers), representing $<$0.001\\% of the base model. LoRA adapters (rank 16, targeting $q$/$v$ projections) contribute 4.2M parameters across both architectures.\n\n\\paragraph{Training time.} Standard variants (ThreadGate, Uniform Gate, LoRA-only) train in 6.0--7.3 hours. PCGrad adds ${\\sim}$33\\% overhead due to the per-step gradient projection computation. Scheduled sampling overhead varies: seed 42 adds only 8\\% (6.5h) due to efficient batched generation, while seed 123 adds 80\\% (10.8h) because of a longer generation schedule. The difference is due to the extended AR generation schedule in the seed 123 variant.\n\n\\paragraph{Inference overhead.} Gate computation at inference time is negligible: a single 32$\\to$64$\\to$1 MLP forward pass per layer adds $<$0.1\\% latency. $\\beta$-steering requires identifying goal tokens (a one-time operation per conversation) and adding a constant bias to attention logits, with zero additional parameters.\n\n\\section{Qualitative Steering Examples}\\label{sec:appendix-examples}\n\nTable~\\ref{tab:examples} illustrates the effect of $\\beta$-steering on model behavior in a 4-turn conversation where the system prompt instructs ``Always respond in exactly three bullet points.''\n\n\\begin{table*}[t]\n\\centering\\small\n\\caption{Qualitative effect of $\\beta$-steering on instruction following across conversation turns. System prompt: ``Always respond in exactly three bullet points.'' ThreadGate checkpoint, 4-turn conversation.}\n\\label{tab:examples}\n\\begin{tabular}{c p{5.5cm} p{5.5cm}}\n\\toprule\n\\textbf{Turn} & \\textbf{$\\beta$\\,=\\,0 (unsteered)} & \\textbf{$\\beta$\\,=\\,3 (steered)} \\\\\n\\midrule\n1 & \\checkmark~Three bullet points, on-topic & \\checkmark~Three bullet points, on-topic \\\\\n2 & \\checkmark~Three bullet points, relevant & \\checkmark~Three bullet points, relevant \\\\\n3 & $\\sim$~Four bullet points, partially on-topic & \\checkmark~Three bullet points, on-topic \\\\\n4 & \\texttimes~Free-form paragraph, no bullets & \\checkmark~Three bullet points, on-topic \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\nThe pattern is consistent with the GAR decay analysis (\\S\\ref{sec:analysis}): unsteered models progressively lose attention to the system-prompt constraint, leading to format violations at later turns. Steering maintains goal-token attention, preserving instruction compliance. The per-category breakdown in Table~\\ref{tab:ir-results} shows that content constraints benefit most from this effect.\n\n\\section{Gradient Conflict Analysis}\\label{sec:appendix-gradient}\n\n\\begin{figure}[t]\n  \\centering\n  \\includegraphics[width=\\columnwidth,height=0.42\\textheight,keepaspectratio]{fig2_training_pcgrad.pdf}\n  \\caption{(a)~Training GAR convergence to target ($\\tau$\\,=\\,0.5). (b)~PCGrad removes gradient conflict but $\\mathcal{L}_\\text{GAR}$ still collapses, confirming that gradient direction conflict is not the primary cause (\\S\\ref{subsec:pcgrad}).}\n  \\label{fig:training-pcgrad}\n\\end{figure}\n\nThis section provides extended gradient interaction analysis supporting the PCGrad exclusion argument in \\S\\ref{subsec:pcgrad}. We measure per-layer cosine similarity between NTP and GAR gradients, gradient magnitude ratios, and the effect of PCGrad projection on these quantities.\n\n\\paragraph{Gradient direction analysis.} Figure~\\ref{fig:gradient-heatmap} visualizes the per-layer cosine similarity between NTP and GAR gradients across training epochs for both standard ThreadGate and PCGrad training. Under standard training, 79\\% of layers show negative cosine similarity (gradient conflict) at epoch~0, declining to 68\\% by epoch~2 as GAR loss converges to near-zero. This decline reflects diminishing GAR gradient magnitude rather than alignment improvement---as GAR loss approaches zero, the GAR gradient shrinks proportionally, making cosine similarity measurements less reliable (small gradients produce noisy direction estimates). Under PCGrad training, the conflict percentage decreases more slowly (79\\%$\\to$71\\%), consistent with PCGrad projecting conflicting gradients onto the other's normal plane but not eliminating the underlying gradient conflict.\n\n\\paragraph{Spatial patterns.} The early layers (L0--L5) and output-adjacent layers (L24--L27) show the strongest conflict, corresponding to the layers where gate values deviate most from identity (Figure~\\ref{fig:gate-heatmap}). This spatial correlation is not causal: removing gradient conflict via PCGrad does not improve AR GAR, and gates at high-conflict layers are not systematically different from gates at low-conflict layers (Spearman $\\rho$\\,=\\,$-$0.12, $p$\\,=\\,0.54 between gate value and conflict magnitude).\n\n\\paragraph{Magnitude dominance.} NTP gradient magnitude dominates GAR by 7.5$\\times$ at epoch~0 and 14.7$\\times$ by epoch~2, as GAR loss converges while NTP loss remains at $\\sim$0.93. This growing dominance means that even when directions oppose, the effective update direction is determined almost entirely by NTP. PCGrad addresses gradient conflict but not magnitude dominance---it projects conflicting gradients onto the other's normal plane (changing direction) but preserves relative magnitudes. The 7.5--14.7$\\times$ magnitude ratio means that even after PCGrad projection, GAR contributes $<$7\\% of the effective update magnitude, explaining why PCGrad is ineffective.\n\n\\paragraph{Cross-model consistency.} Table~\\ref{tab:gradient-crossmodel} confirms the pattern on Llama-3.1-8B: gradients are near-orthogonal (mean cosine $+$0.005, essentially zero) rather than systematically conflicting, with 25.7$\\times$ NTP dominance. The Llama result is particularly informative because it shows that even without systematic gradient conflict (53\\% negative layers, near chance), the same TF-AR gap persists. This cross-model evidence strengthens the \\textit{modus tollens} argument: if gradient conflict were the cause, it should be present on both architectures; it is absent on Llama, yet the gap persists; therefore gradient direction conflict is not the primary cause.\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=0.95\\textwidth]{fig_gradient_conflict_heatmap.pdf}\n\\caption{Per-layer cosine similarity between NTP and GAR gradients across training epochs. (a)~Standard training: conflict decreases from 79\\% to 68\\% of layers as GAR loss vanishes. (b)~PCGrad training: projection reduces conflict more slowly (79\\%$\\to$71\\%) but does not improve AR GAR, ruling out gradient direction conflict as the primary cause (\\S\\ref{subsec:pcgrad}).}\n\\label{fig:gradient-heatmap}\n\\end{figure*}\n\n\\section{Training Data Characteristics}\\label{sec:appendix-data}\n\nAll experiments use 8,000 multi-turn conversations sampled from the UltraChat \\citep{ding2023ultrachat} training split. Table~\\ref{tab:data-stats} summarizes the dataset characteristics. Conversations are truncated to 2,048 tokens; conversations shorter than 3 user turns are excluded to ensure sufficient multi-turn structure for GAR computation. The held-out evaluation sets use separate non-overlapping samples: $N$\\,=\\,50 conversations (mean 3.6 user turns) for the primary AR evaluation and $N$\\,=\\,5 conversations (10 turns each) for the long-conversation analysis (Appendix~\\ref{sec:appendix-n5}).\n\n\\begin{table}[t]\n\\centering\\small\n\\caption{Training and evaluation data characteristics. All data from UltraChat \\citep{ding2023ultrachat}.}\n\\label{tab:data-stats}\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Property} & \\textbf{Train} & \\textbf{Eval (primary)} \\\\\n\\midrule\nConversations & 8,000 & 50 \\\\\nMin user turns & 3 & 3 \\\\\nMax sequence length & 2,048 & 2,048 \\\\\nSource & UltraChat train & UltraChat train \\\\\nOverlap & --- & non-overlapping \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Exposure Bias Scaling}\\label{sec:appendix-eb-scaling}\n\nFigure~\\ref{fig:eb-scaling} quantifies two scaling dimensions of the exposure bias phenomenon: cross-variant gap ratios (panel~a) and length-dependent gap compounding (panel~b).",
      "numLines": 100,
      "startLine": 390,
      "totalLines": 851
    }
  },
  "sourceToolAssistantUUID": "fbb7371c-ee14-4bd7-b6d6-0e9adf0b3609",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921",
  "sessionId": "5d779602-0719-4d06-8bf9-fdd84990d5d0",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---


### Tool call

_source line 82 · 2026-05-25T20:38:34.651Z_

<details open><summary>🔧 Tool call — Bash · `toolu_014YEy4jMcZGUZMCeFSkrJxz`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating && git log --oneline -10",
  "description": "Check recent commits in project repo"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4d35af4f-3598-4a8e-bff2-d645353c0108",
  "isSidechain": false,
  "requestId": "req_011CbPvydiQya2dyfYTDhTyF",
  "type": "assistant",
  "uuid": "4be71593-f6f9-46b3-ac12-932f75dcfbcb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921",
  "sessionId": "5d779602-0719-4d06-8bf9-fdd84990d5d0",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0111pyAGatAL7GziMBNNZN5U",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 17839,
      "cache_read_input_tokens": 75952,
      "output_tokens": 218,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 17839,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 218,
          "cache_read_input_tokens": 75952,
          "cache_creation_input_tokens": 17839,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 17839
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

_source line 83 · 2026-05-25T20:38:34.697Z_

<details><summary>↩ Tool result · `toolu_014YEy4jMcZGUZMCeFSkrJxz`</summary>

```text
98eff19 [paper] Fix cross-model gap comparison + add median justification
73a7969 [paper] Write Llama LoRA-only cross-model results (C5 completion)
74bb496 [paper] Add Li et al. 2024 (direct competitor) + strengthen exposure bias citations
2e58ab1 [paper] Fix 2 author errors + 3 bib warnings from citation audit
c93a515 [paper] Multi-seed v7 TG data + v8b SS training schedule observation
c4dc400 [paper] Add β=5 PPL tradeoff to Discussion steering paragraph
66c3ef4 [paper] Fix 5 paper-registry numerical inconsistencies (N=5 steering data)
e4522a3 [paper] Fix instruction retention params + update Limitations + compress Abstract
52e5da3 [paper] Llama cross-model confirmed + §6 mechanism expansion + instruction retention
760d758 [paper] Llama-3.1-8B cross-model GAR decay diagnostic (§6.5 preliminary evidence)
Shell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4be71593-f6f9-46b3-ac12-932f75dcfbcb",
  "isSidechain": false,
  "promptId": "b0f005fa-c14f-47e1-bf29-f3925462c4b7",
  "type": "user",
  "uuid": "9a22b79d-d171-4ee1-89bb-524e64b31c02",
  "toolUseResult": {
    "stdout": "98eff19 [paper] Fix cross-model gap comparison + add median justification\n73a7969 [paper] Write Llama LoRA-only cross-model results (C5 completion)\n74bb496 [paper] Add Li et al. 2024 (direct competitor) + strengthen exposure bias citations\n2e58ab1 [paper] Fix 2 author errors + 3 bib warnings from citation audit\nc93a515 [paper] Multi-seed v7 TG data + v8b SS training schedule observation\nc4dc400 [paper] Add β=5 PPL tradeoff to Discussion steering paragraph\n66c3ef4 [paper] Fix 5 paper-registry numerical inconsistencies (N=5 steering data)\ne4522a3 [paper] Fix instruction retention params + update Limitations + compress Abstract\n52e5da3 [paper] Llama cross-model confirmed + §6 mechanism expansion + instruction retention\n760d758 [paper] Llama-3.1-8B cross-model GAR decay diagnostic (§6.5 preliminary evidence)",
    "stderr": "\nShell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "4be71593-f6f9-46b3-ac12-932f75dcfbcb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921",
  "sessionId": "5d779602-0719-4d06-8bf9-fdd84990d5d0",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---


### Assistant

_source line 84 · 2026-05-25T20:39:50.527Z_

<details><summary>Logged reasoning block</summary>

```text
Now let me read the remaining appendix and verify the steering table data against the registry.

Let me check the steering table (tab_steering_full.tex) data against the registry:

From the appendix (line 306-329), the steering table shows:
- N=5 Gen β=0: GAR=.028, PPL=1.41
  Registry attention_steering_v7_tg_gen: beta_0.0.mid_turns_avg_gar = 0.028, beta_0.0.avg_ppl = 1.409 → 1.41 ✓


- N=5 Gen β=0.5: GAR=.029, PPL=1.39
  Registry: beta_0.5.mid_turns_avg_gar = 0.0287 → .029 ✓, beta_0.5.avg_ppl = 1.387 → 1.39 ✓
- N=5 Gen β=5: GAR=.680, PPL=1.91
  Registry: beta_5.0.mid_turns_avg_gar = 0.6795 → .680 ✓, beta_5.0.avg_ppl = 1.910 → 1.91 ✓

Now checking the larger sample size with N=50, where the β=0 configuration shows GAR of .064 with standard deviation .081 and perplexity of 1.43±.10, all matching the registry values. The β=3 variant gives a GAR of .556±.060, which also checks out against the stored metrics.

Continuing with the N=200 transformer-based evaluations, where β=0 yields a GAR of .535 and perplexity of 2.62, and β=5 pushes the GAR up to .833 with perplexity climbing to 6.15—all values aligning with what's in the registry.

Now I'm checking the gate profile data from the registry against the reported values, looking at the per-layer gate activations for seed 123 across all 20 layers. Checking the remaining layer scores through L27, all passing their thresholds, with the final mean coming in at 0.9.

Now I'm verifying the cost table entries—the LoRA-only and ThreadGate training times align with the registry values when accounting for rounding, and I'm working through the PCGrad metrics. Continuing to verify the Llama LoRA-only and TG training times against the registry, then cross-checking the gradient analysis metrics for both Qwen and Llama models—the cosine similarities, negative layer percentages, and magnitude ratios all line up with what's recorded.

Now I'm compiling the audit findings and spotting a data source inconsistency in the cross-model table where the Qwen SS row pulls TF GAR from one protocol but AR GAR from a different aggregation method.

The reported 1.2× gap ratio mixes these incompatible values, but using consistent sources gives either 1.4× (s42-only) or 1.3× (3-seed mean), which changes the headline claim.

I'm also noticing the per-seed TG table applies a different AR evaluation protocol than expected. than main results**
   - TG per-seed AR eval: N=5, T=10 (old protocol) → GAR = 0.016
   - Main results AR eval: N=50, gen-mode (d048 protocol) → GAR = 0.064
   - Per-seed gap ratio: 31.4× (based on N=5)
   - Main results gap ratio: 7.9× (based on N=50)
   - This 4× discrepancy in gap ratios could confuse reviewers
   - The table caption is transparent about N=5, but the dramatically different number needs discussion
   - TG only has 2 seeds (vs SS's 3), and those 2 seeds use the weaker eval protocol
   
3. **[severity: info] Per-seed SS table (tab_perseed_ss) TF values use different eval runs** — the s42 checkpoint shows a TF GAR of 0.502 from one evaluation but appears as 0.498 in the cross-model table from a separate run, a small discrepancy that should ideally be reconciled by using consistent evaluation sources.

4. **[severity: info] LoRA-only training time**: registry says 5.7h, table says 6.0h. Minor rounding discrepancy.

5. **[severity: info] Cost table SS s123 overhead calculation**: The paper says seed 123 adds 80

% overhead (10.8h), which checks out against the LoRA-only baseline of 6.0h, though the exact percentage depends on which baseline is used for comparison.

Now I'm verifying the cross-model table caption claim about N=200 for Qwen's TF eval and tracing back through the evaluation sources to confirm the protocol used. So different seeds ended up using different sample sizes for the TF eval—s42 had N=50 while s123 had N=200. It's a bit messy, but TF GAR is stable enough across different N that it shouldn't be a major problem. Let me verify the LoRA-only numbers match up: the AR GAR of 0.037 and TF GAR of 0.498 both check out against the source data. I think I have what I need to write up a comprehensive audit report now, starting with documenting the issues I've found. Now I'm putting together the report with these findings.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9a22b79d-d171-4ee1-89bb-524e64b31c02",
  "isSidechain": false,
  "requestId": "req_011CbPvz4ywmEgnjx9zWkCYs",
  "type": "assistant",
  "uuid": "745e6d01-cafa-44e2-ac7a-7da2b76314b9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921",
  "sessionId": "5d779602-0719-4d06-8bf9-fdd84990d5d0",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KLKZjB181rXGx7PvQPBMG6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3581,
      "cache_read_input_tokens": 93791,
      "output_tokens": 3880,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3581,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3880,
          "cache_read_input_tokens": 93791,
          "cache_creation_input_tokens": 3581,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3581
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

_source line 85 · 2026-05-25T20:39:50.945Z_

审查完成。我已经交叉验证了全部附录表格数据与 registry 实验记录。发现了 2 个 warning 级别问题和 2 个 info 级别问题。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "745e6d01-cafa-44e2-ac7a-7da2b76314b9",
  "isSidechain": false,
  "requestId": "req_011CbPvz4ywmEgnjx9zWkCYs",
  "type": "assistant",
  "uuid": "29292e36-f3f1-4925-be8c-d3a40b2d5608",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921",
  "sessionId": "5d779602-0719-4d06-8bf9-fdd84990d5d0",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KLKZjB181rXGx7PvQPBMG6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3581,
      "cache_read_input_tokens": 93791,
      "output_tokens": 3880,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3581,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3880,
          "cache_read_input_tokens": 93791,
          "cache_creation_input_tokens": 3581,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3581
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

_source line 86 · 2026-05-25T20:39:51.988Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01HJuPuVRWs8aqcgHUjBh8iv`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__reviewer_post_to_director",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "29292e36-f3f1-4925-be8c-d3a40b2d5608",
  "isSidechain": false,
  "requestId": "req_011CbPvz4ywmEgnjx9zWkCYs",
  "type": "assistant",
  "uuid": "e6b8e349-d146-48b9-aa90-c3e91e7f8893",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921",
  "sessionId": "5d779602-0719-4d06-8bf9-fdd84990d5d0",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KLKZjB181rXGx7PvQPBMG6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3581,
      "cache_read_input_tokens": 93791,
      "output_tokens": 3880,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3581,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3880,
          "cache_read_input_tokens": 93791,
          "cache_creation_input_tokens": 3581,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3581
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

_source line 87 · 2026-05-25T20:39:51.994Z_

<details><summary>↩ Tool result · `toolu_01HJuPuVRWs8aqcgHUjBh8iv`</summary>

````text
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
  "parentUuid": "e6b8e349-d146-48b9-aa90-c3e91e7f8893",
  "isSidechain": false,
  "promptId": "b0f005fa-c14f-47e1-bf29-f3925462c4b7",
  "type": "user",
  "uuid": "22f6c452-1ded-42f4-b81a-f449a2145b5d",
  "toolUseResult": {
    "matches": [
      "mcp__agent-ml-research__reviewer_post_to_director"
    ],
    "query": "select:mcp__agent-ml-research__reviewer_post_to_director",
    "total_deferred_tools": 35
  },
  "sourceToolAssistantUUID": "e6b8e349-d146-48b9-aa90-c3e91e7f8893",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921",
  "sessionId": "5d779602-0719-4d06-8bf9-fdd84990d5d0",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---


### Runtime record

_source line 88 · 2026-05-25T20:39:52.053Z_

```json
{
  "parentUuid": "22f6c452-1ded-42f4-b81a-f449a2145b5d",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "2876dbb0-956d-424a-960a-e58475adf3ec",
  "timestamp": "2026-05-25T20:39:52.053Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921",
  "sessionId": "5d779602-0719-4d06-8bf9-fdd84990d5d0",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---


### Runtime record

_source line 89_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[系统通知 — worker_done:worker_audit_appendix_tables_20260525T201208]: Worker worker_audit_appendix_tables_20260525T201208 已完成（status=done），请审查 Agent 的处理结果。",
  "leafUuid": "2876dbb0-956d-424a-960a-e58475adf3ec",
  "sessionId": "5d779602-0719-4d06-8bf9-fdd84990d5d0"
}
```

---


### Runtime record

_source line 90_

```json
{
  "type": "ai-title",
  "aiTitle": "Review worker audit appendix tables completion",
  "sessionId": "5d779602-0719-4d06-8bf9-fdd84990d5d0"
}
```

---


### Tool call

_source line 91 · 2026-05-25T20:40:25.928Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__reviewer_post_to_director · `toolu_019A3R2ES1rzLDEXfhn4Q2hK`</summary>

```json
{
  "text": "## 审查报告 — worker_audit_appendix_tables\n\n**结论**: WARNING\n\n我对全部附录表格（10张表 + 内联数据）逐项与 registry 实验记录交叉验证，大部分数字一致。发现以下问题：\n\n### 发现\n\n- [severity: warning] **tab_crossmodel_detail (Table crossmodel-detail) Qwen SS 行数据源混合**\n  - TF GAR = 0.498：来自 s42 单种子旧协议 eval (eval_v8b_ss, N=50)\n  - AR GAR = 0.401：来自 3 种子均值 (tab_perseed_ss 的 mean)\n  - 但表格 caption 明确写 \"Qwen AR: d048_final_ar N=50 gen beta=0\"，该实验给出 ss_gar = 0.347 (s42)\n  - Gap 1.2× 是混合计算的结果 (0.498/0.401)。如果一致用 s42：gap = 0.498/0.347 = 1.4×；一致用 3-seed mean：gap = 0.517/0.401 = 1.3×\n  - **影响**：SS 的 headline gap 数字不可靠，审稿人若按 caption 溯源会发现 0.401 不来自 d048_final_ar\n\n- [severity: warning] **tab_perseed_tg 使用与主结果不同的 AR eval 协议**\n  - TG per-seed AR eval：N=5, T=10（旧协议）→ GAR = 0.016, gap = 31.4×\n  - 主结果 (tab_five_way / tab_crossmodel_detail) AR eval：N=50 gen-mode → GAR = 0.064, gap = 7.9×\n  - 同一模型 (TG s42) 在两个协议下 AR GAR 相差 4×（0.016 vs 0.064），gap 31× vs 8×\n  - TG 只有 2 seeds（vs SS 的 3 seeds），且这 2 seeds 用的是统计功效更弱的 N=5 协议\n  - caption 虽透明标注了 N=5，但审稿人对比主表与附录会质疑哪个 gap ratio 才是 ground truth\n  - **建议**：用 d048_final_ar_eval 的 N=50 数据更新 TG per-seed 表的 AR 列，或至少在文中明确解释两个数字的差异来源\n\n- [severity: info] **SS s42 TF GAR 跨表不一致**：tab_perseed_ss 用 0.502 (d048_eval_ss_s42)，tab_crossmodel_detail 用 0.498 (eval_v8b_ss)。同一 checkpoint 不同 eval run，差异在噪声范围内，但理想情况应统一 eval 来源\n\n- [severity: info] **Cost table 训练时间轻微舍入**：LoRA-only registry 记录 5.7h，表中写 6.0h；UG registry 6.1h，表中写 6.0h。不影响结论但可精确化\n\n### 已验证一致的表格\n以下表格全部数字与 registry 一致（含算术验证）：\n- tab_statistical_tests：Wilcoxon/McNemar 统计量、p 值、效应量、GAR 均值与 CI 全部匹配\n- tab_gar_robustness：4种 token selection × 3 conditions，Gap Ratio 算术验证通过\n- tab_perturn_qwen / tab_perturn_llama：per-turn 值与 registry 中间回合均值一致\n- tab_mmlu_detail：6 条件 overall 精确匹配，Δ 算术正确\n- tab_dataset_stats：与实验 spec 一致\n- tab_qwen15b_results：Phase 1 relative drop 算术正确 (79.8%)\n- Gate profile table (s123)：28 层逐层值与 registry v7_tg_s123 精确匹配\n- Steering full table：3 eval settings × 8 β 值全部与 registry 匹配\n- Gradient cross-model table：cos_sim / neg-layer% / mag_ratio 双模型数据匹配\n- Cost table：除上述舍入外，wall clock 时间与 registry 一致",
  "project": "turn_residual_gating"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2876dbb0-956d-424a-960a-e58475adf3ec",
  "isSidechain": false,
  "requestId": "req_011CbPw5mcbN1bki653BA1t8",
  "type": "assistant",
  "uuid": "5ac5a9e0-877d-4bbe-8dfd-a648f28d1b7d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921",
  "sessionId": "5d779602-0719-4d06-8bf9-fdd84990d5d0",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FMFBvZ5ppawmn1Squ9tEZD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 4214,
      "cache_read_input_tokens": 97372,
      "output_tokens": 1309,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4214,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1309,
          "cache_read_input_tokens": 97372,
          "cache_creation_input_tokens": 4214,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4214
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

_source line 92 · 2026-05-25T20:40:29.598Z_

<details><summary>↩ Tool result · `toolu_019A3R2ES1rzLDEXfhn4Q2hK`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"director_session\": \"feishu:group:oc_640e53b6afbbd5e34eb7273cd5a707a0:director\"}, \"error\": \"\"}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5ac5a9e0-877d-4bbe-8dfd-a648f28d1b7d",
  "isSidechain": false,
  "promptId": "b0f005fa-c14f-47e1-bf29-f3925462c4b7",
  "type": "user",
  "uuid": "dfdfa786-5d36-497f-b0c1-c030a6f711a4",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"director_session\\\": \\\"feishu:group:oc_640e53b6afbbd5e34eb7273cd5a707a0:director\\\"}, \\\"error\\\": \\\"\\\"}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"director_session\": \"feishu:group:oc_640e53b6afbbd5e34eb7273cd5a707a0:director\"}, \"error\": \"\"}"
    }
  },
  "sourceToolAssistantUUID": "5ac5a9e0-877d-4bbe-8dfd-a648f28d1b7d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921",
  "sessionId": "5d779602-0719-4d06-8bf9-fdd84990d5d0",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---


### Runtime record

_source line 93_

```json
{
  "type": "ai-title",
  "aiTitle": "Review worker audit appendix tables completion",
  "sessionId": "5d779602-0719-4d06-8bf9-fdd84990d5d0"
}
```

---


### Runtime record

_source line 94 · 2026-05-25T20:41:50.068Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-25T20:41:50.068Z",
  "sessionId": "5d779602-0719-4d06-8bf9-fdd84990d5d0",
  "content": "[服务器重启后首条消息] 当前日期: 2026-05-25。服务器刚重启，项目状态可能已更新。在处理审查请求前，**先读取 registry.yaml 和 report.md** 获取最新实验状态，不要依赖对话历史中的状态信息。\n\n**审查请求：** [系统通知 — worker_done:worker_fix_audit_appendix_issues_20260525T203522]:\nWorker worker_fix_audit_appendix_issues_20260525T203522 已完成（status=done），请审查 Agent 的处理结果。"
}
```

---


### Runtime record

_source line 95 · 2026-05-25T20:41:50.068Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-25T20:41:50.068Z",
  "sessionId": "5d779602-0719-4d06-8bf9-fdd84990d5d0"
}
```

---


## Round 2

## Round 2

2 recorded events


### User

_source line 96 · 2026-05-25T20:41:50.060Z_

Continue from where you left off.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "dfdfa786-5d36-497f-b0c1-c030a6f711a4",
  "isSidechain": false,
  "promptId": "8d8464e4-1523-464c-8d63-5cd7db13bd3f",
  "type": "user",
  "isMeta": true,
  "uuid": "c6b476c2-2dd2-4867-85b3-fd0b88ab7fbd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921",
  "sessionId": "5d779602-0719-4d06-8bf9-fdd84990d5d0",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---


### Assistant

_source line 97 · 2026-05-25T20:41:50.060Z_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c6b476c2-2dd2-4867-85b3-fd0b88ab7fbd",
  "isSidechain": false,
  "type": "assistant",
  "uuid": "426b692a-eaf0-4668-a323-aa3de543ef01",
  "isApiErrorMessage": false,
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921",
  "sessionId": "5d779602-0719-4d06-8bf9-fdd84990d5d0",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "id": "ace8ab81-0617-4882-b7d1-e46bac523257",
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

## Round 3

74 recorded events


### User

_source line 98 · 2026-05-25T20:41:50.192Z_

[服务器重启后首条消息] 当前日期: 2026-05-25。服务器刚重启，项目状态可能已更新。在处理审查请求前，**先读取 registry.yaml 和 report.md** 获取最新实验状态，不要依赖对话历史中的状态信息。

**审查请求：** [系统通知 — worker_done:worker_fix_audit_appendix_issues_20260525T203522]:
Worker worker_fix_audit_appendix_issues_20260525T203522 已完成（status=done），请审查 Agent 的处理结果。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "426b692a-eaf0-4668-a323-aa3de543ef01",
  "isSidechain": false,
  "promptId": "8d8464e4-1523-464c-8d63-5cd7db13bd3f",
  "type": "user",
  "uuid": "eededf7b-768d-46d0-aaa1-50e44aeff3fb",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921",
  "sessionId": "5d779602-0719-4d06-8bf9-fdd84990d5d0",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---


### Assistant

_source line 99 · 2026-05-25T20:41:53.865Z_

<details><summary>Logged reasoning block</summary>

```text
The server restarted and I need to review the worker's fix for the appendix issues I previously identified. Let me first read the registry and report to get the latest state, then check what changes the worker made.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "eededf7b-768d-46d0-aaa1-50e44aeff3fb",
  "isSidechain": false,
  "requestId": "req_011CbPwEUpo31hMtip6JfkTx",
  "type": "assistant",
  "uuid": "bb4ed02a-86ba-449f-b31d-e95cd4641132",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921",
  "sessionId": "5d779602-0719-4d06-8bf9-fdd84990d5d0",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017HZXVXMjujcDe6BigkeJnT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 191,
      "cache_read_input_tokens": 102971,
      "output_tokens": 284,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 191,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 284,
          "cache_read_input_tokens": 102971,
          "cache_creation_input_tokens": 191,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 191
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

_source line 100 · 2026-05-25T20:41:55.376Z_

先读取最新状态，再审查 worker 的修复。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bb4ed02a-86ba-449f-b31d-e95cd4641132",
  "isSidechain": false,
  "requestId": "req_011CbPwEUpo31hMtip6JfkTx",
  "type": "assistant",
  "uuid": "675248ab-7b39-49a6-a867-f7b398309243",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921",
  "sessionId": "5d779602-0719-4d06-8bf9-fdd84990d5d0",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017HZXVXMjujcDe6BigkeJnT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 191,
      "cache_read_input_tokens": 102971,
      "output_tokens": 284,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 191,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 284,
          "cache_read_input_tokens": 102971,
          "cache_creation_input_tokens": 191,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 191
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

_source line 101 · 2026-05-25T20:41:56.434Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01BRBh43PY1rYokUd9baKUGV`</summary>

```json
{
  "project": "turn_residual_gating",
  "limit": 5,
  "fields": [
    "status",
    "conclusion",
    "updated_at"
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "675248ab-7b39-49a6-a867-f7b398309243",
  "isSidechain": false,
  "requestId": "req_011CbPwEUpo31hMtip6JfkTx",
  "type": "assistant",
  "uuid": "85f06e6b-6d55-42b9-80a6-f007d1eb4c8f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921",
  "sessionId": "5d779602-0719-4d06-8bf9-fdd84990d5d0",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017HZXVXMjujcDe6BigkeJnT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 191,
      "cache_read_input_tokens": 102971,
      "output_tokens": 284,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 191,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 284,
          "cache_read_input_tokens": 102971,
          "cache_creation_input_tokens": 191,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 191
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

_source line 102 · 2026-05-25T20:41:56.649Z_

<details><summary>↩ Tool result · `toolu_01BRBh43PY1rYokUd9baKUGV`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {\"phase1a_multiseed_qwen\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-25T11:20:34.089Z\", \"conclusion\": \"killed\"}, \"p1_ss_lora_only\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-25T09:42:22.185Z\", \"conclusion\": \"killed\"}, \"phase2_switching\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-25T09:42:21.391Z\", \"conclusion\": \"killed\"}, \"phase2_tf_ar_switching\": {\"status\": \"QUEUED\", \"updated_at\": \"2026-05-25T06:45:27.338Z\"}, \"phase1a_multiseed_8runs\": {\"status\": \"PREPARING\", \"updated_at\": \"2026-05-25T06:18:08.953Z\"}}, \"count\": 5, \"total\": 60, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.2001}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "85f06e6b-6d55-42b9-80a6-f007d1eb4c8f",
  "isSidechain": false,
  "promptId": "8d8464e4-1523-464c-8d63-5cd7db13bd3f",
  "type": "user",
  "uuid": "f1d5baee-5396-4462-9426-11fab6c16452",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {\\\"phase1a_multiseed_qwen\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-25T11:20:34.089Z\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"p1_ss_lora_only\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-25T09:42:22.185Z\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"phase2_switching\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-25T09:42:21.391Z\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"phase2_tf_ar_switching\\\": {\\\"status\\\": \\\"QUEUED\\\", \\\"updated_at\\\": \\\"2026-05-25T06:45:27.338Z\\\"}, \\\"phase1a_multiseed_8runs\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"updated_at\\\": \\\"2026-05-25T06:18:08.953Z\\\"}}, \\\"count\\\": 5, \\\"total\\\": 60, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.2001}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {\"phase1a_multiseed_qwen\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-25T11:20:34.089Z\", \"conclusion\": \"killed\"}, \"p1_ss_lora_only\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-25T09:42:22.185Z\", \"conclusion\": \"killed\"}, \"phase2_switching\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-25T09:42:21.391Z\", \"conclusion\": \"killed\"}, \"phase2_tf_ar_switching\": {\"status\": \"QUEUED\", \"updated_at\": \"2026-05-25T06:45:27.338Z\"}, \"phase1a_multiseed_8runs\": {\"status\": \"PREPARING\", \"updated_at\": \"2026-05-25T06:18:08.953Z\"}}, \"count\": 5, \"total\": 60, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.2001}}"
    }
  },
  "sourceToolAssistantUUID": "85f06e6b-6d55-42b9-80a6-f007d1eb4c8f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921",
  "sessionId": "5d779602-0719-4d06-8bf9-fdd84990d5d0",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---


### Tool call

_source line 103 · 2026-05-25T20:41:56.915Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01CxhGZGij2qmAkiZVvBq41L`</summary>

```json
{
  "project": "turn_residual_gating",
  "file": "report.md",
  "max_chars": 6000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f1d5baee-5396-4462-9426-11fab6c16452",
  "isSidechain": false,
  "requestId": "req_011CbPwEUpo31hMtip6JfkTx",
  "type": "assistant",
  "uuid": "e0af7716-dcd4-40de-b4fc-a82581a8224a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921",
  "sessionId": "5d779602-0719-4d06-8bf9-fdd84990d5d0",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017HZXVXMjujcDe6BigkeJnT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 191,
      "cache_read_input_tokens": 102971,
      "output_tokens": 284,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 191,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 284,
          "cache_read_input_tokens": 102971,
          "cache_creation_input_tokens": 191,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 191
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

_source line 104 · 2026-05-25T20:41:56.925Z_

<details><summary>↩ Tool result · `toolu_01CxhGZGij2qmAkiZVvBq41L`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/report.md\", \"content\": \"# Handover — 2026-05-25\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n（无）\\n\\n## 待处理\\n- phase2_tf_ar_switching: TF→AR switching at turn k (k=1..5) on ThreadGate s42 checkpoint. If GAR drops abruptly at the switch point (matching pure-AR level within 1 turn), it confirms exposure bias as instantaneous distribution shift rather than gradual cumulative drift.（排队等待 GPU）\\n- phase1a_multiseed_8runs（准备中）\\n- phase1b_llama_complement: Llama PCGrad + UG (s42) to complete cross-model comparison matrix. If Llama PCGrad also fails to improve AR GAR (like Qwen), it strengthens the cross-architecture causal exclusion of gradient conflict.（准备中）\\n- p0_ss_steering_eval: SS training provides AR GAR ~0.385, steering alone gives 0.717. Combining SS checkpoint with beta-steering at inference may approach TF parity (~0.50), demonstrating that SS+steering is a constructive mitigation stack for the TF-AR gap.（准备中）\\n- d048_queue_runner（准备中）\\n- d048_ss_s42_resume（准备中）\\n- llama_tg_training（准备中）\\n\\n## 近期结论\\n- **phase1a_multiseed_qwen** (killed): Multi-seed (s123, s456) training across 5 Qwen conditions (PCGrad, UG, LoRA-only, TG, SS) to establish mean±std for all claims. 8 training runs + AR eval N≥50 each. Expect TF convergence (GAR~0.50) and consistent AR rankings across seeds.\\n- **p1_ss_lora_only** (killed): SS training on LoRA-only checkpoint (no ThreadGate) with same hyperparameters (rho_max=0.3, same schedule) should achieve similar GAR improvement as SS+TG. If confirmed, this proves the SS fix is architecture-agnostic, strengthening the paper's mitigation story (the gap is caused by exposure bias in any auxiliary-loss setup, and SS fixes it regardless of gating mechanism).\\n- **phase2_switching** (killed): TF→AR switching at turn k (k=1..5) on ThreadGate s42 checkpoint. If GAR drops abruptly at the switch point (matching pure-AR level within 1 turn), it confirms exposure bias as instantaneous distribution shift rather than gradual KV cache drift. Staircase = exposure bias dominant; linear slope = KV drift dominant.\\n\\n## 趋势\\n成功 40 / 负向 5 / 失败 4 / 共 53\\n\\n## 下一步\\n（无活跃 idea，请通过 ideas.md 添加）\\n\\n## 资源状态\\nwestd-20861: 无 GPU 信息\\n\\n## 告警\\n- phase2_tg_s42_v2: 已被终止 — unknown\\n- phase2_tg_s42_v4: 训练失败 — unknown\\n- phase2_tg_s42_v8_schedsampling: 训练失败 — unknown\\n- phase2_tg_s42_v8b_ss_fixed: 训练失败 — unknown\\n- d048_split_softmax_eval: 训练失败 — unknown\\n- phase1a_multiseed_qwen: 已被终止 — unknown\\n- phase2_switching: 已被终止 — unknown\\n- p1_ss_lora_only: 已被终止 — unknown\\n\", \"total_chars\": 2436, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e0af7716-dcd4-40de-b4fc-a82581a8224a",
  "isSidechain": false,
  "promptId": "8d8464e4-1523-464c-8d63-5cd7db13bd3f",
  "type": "user",
  "uuid": "58528b50-2495-4946-8cb4-5b9b52f97616",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/report.md\\\", \\\"content\\\": \\\"# Handover — 2026-05-25\\\\n\\\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\\\n\\\\n## 运行中\\\\n（无）\\\\n\\\\n## 待处理\\\\n- phase2_tf_ar_switching: TF→AR switching at turn k (k=1..5) on ThreadGate s42 checkpoint. If GAR drops abruptly at the switch point (matching pure-AR level within 1 turn), it confirms exposure bias as instantaneous distribution shift rather than gradual cumulative drift.（排队等待 GPU）\\\\n- phase1a_multiseed_8runs（准备中）\\\\n- phase1b_llama_complement: Llama PCGrad + UG (s42) to complete cross-model comparison matrix. If Llama PCGrad also fails to improve AR GAR (like Qwen), it strengthens the cross-architecture causal exclusion of gradient conflict.（准备中）\\\\n- p0_ss_steering_eval: SS training provides AR GAR ~0.385, steering alone gives 0.717. Combining SS checkpoint with beta-steering at inference may approach TF parity (~0.50), demonstrating that SS+steering is a constructive mitigation stack for the TF-AR gap.（准备中）\\\\n- d048_queue_runner（准备中）\\\\n- d048_ss_s42_resume（准备中）\\\\n- llama_tg_training（准备中）\\\\n\\\\n## 近期结论\\\\n- **phase1a_multiseed_qwen** (killed): Multi-seed (s123, s456) training across 5 Qwen conditions (PCGrad, UG, LoRA-only, TG, SS) to establish mean±std for all claims. 8 training runs + AR eval N≥50 each. Expect TF convergence (GAR~0.50) and consistent AR rankings across seeds.\\\\n- **p1_ss_lora_only** (killed): SS training on LoRA-only checkpoint (no ThreadGate) with same hyperparameters (rho_max=0.3, same schedule) should achieve similar GAR improvement as SS+TG. If confirmed, this proves the SS fix is architecture-agnostic, strengthening the paper's mitigation story (the gap is caused by exposure bias in any auxiliary-loss setup, and SS fixes it regardless of gating mechanism).\\\\n- **phase2_switching** (killed): TF→AR switching at turn k (k=1..5) on ThreadGate s42 checkpoint. If GAR drops abruptly at the switch point (matching pure-AR level within 1 turn), it confirms exposure bias as instantaneous distribution shift rather than gradual KV cache drift. Staircase = exposure bias dominant; linear slope = KV drift dominant.\\\\n\\\\n## 趋势\\\\n成功 40 / 负向 5 / 失败 4 / 共 53\\\\n\\\\n## 下一步\\\\n（无活跃 idea，请通过 ideas.md 添加）\\\\n\\\\n## 资源状态\\\\nwestd-20861: 无 GPU 信息\\\\n\\\\n## 告警\\\\n- phase2_tg_s42_v2: 已被终止 — unknown\\\\n- phase2_tg_s42_v4: 训练失败 — unknown\\\\n- phase2_tg_s42_v8_schedsampling: 训练失败 — unknown\\\\n- phase2_tg_s42_v8b_ss_fixed: 训练失败 — unknown\\\\n- d048_split_softmax_eval: 训练失败 — unknown\\\\n- phase1a_multiseed_qwen: 已被终止 — unknown\\\\n- phase2_switching: 已被终止 — unknown\\\\n- p1_ss_lora_only: 已被终止 — unknown\\\\n\\\", \\\"total_chars\\\": 2436, \\\"truncated\\\": false}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/report.md\", \"content\": \"# Handover — 2026-05-25\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n（无）\\n\\n## 待处理\\n- phase2_tf_ar_switching: TF→AR switching at turn k (k=1..5) on ThreadGate s42 checkpoint. If GAR drops abruptly at the switch point (matching pure-AR level within 1 turn), it confirms exposure bias as instantaneous distribution shift rather than gradual cumulative drift.（排队等待 GPU）\\n- phase1a_multiseed_8runs（准备中）\\n- phase1b_llama_complement: Llama PCGrad + UG (s42) to complete cross-model comparison matrix. If Llama PCGrad also fails to improve AR GAR (like Qwen), it strengthens the cross-architecture causal exclusion of gradient conflict.（准备中）\\n- p0_ss_steering_eval: SS training provides AR GAR ~0.385, steering alone gives 0.717. Combining SS checkpoint with beta-steering at inference may approach TF parity (~0.50), demonstrating that SS+steering is a constructive mitigation stack for the TF-AR gap.（准备中）\\n- d048_queue_runner（准备中）\\n- d048_ss_s42_resume（准备中）\\n- llama_tg_training（准备中）\\n\\n## 近期结论\\n- **phase1a_multiseed_qwen** (killed): Multi-seed (s123, s456) training across 5 Qwen conditions (PCGrad, UG, LoRA-only, TG, SS) to establish mean±std for all claims. 8 training runs + AR eval N≥50 each. Expect TF convergence (GAR~0.50) and consistent AR rankings across seeds.\\n- **p1_ss_lora_only** (killed): SS training on LoRA-only checkpoint (no ThreadGate) with same hyperparameters (rho_max=0.3, same schedule) should achieve similar GAR improvement as SS+TG. If confirmed, this proves the SS fix is architecture-agnostic, strengthening the paper's mitigation story (the gap is caused by exposure bias in any auxiliary-loss setup, and SS fixes it regardless of gating mechanism).\\n- **phase2_switching** (killed): TF→AR switching at turn k (k=1..5) on ThreadGate s42 checkpoint. If GAR drops abruptly at the switch point (matching pure-AR level within 1 turn), it confirms exposure bias as instantaneous distribution shift rather than gradual KV cache drift. Staircase = exposure bias dominant; linear slope = KV drift dominant.\\n\\n## 趋势\\n成功 40 / 负向 5 / 失败 4 / 共 53\\n\\n## 下一步\\n（无活跃 idea，请通过 ideas.md 添加）\\n\\n## 资源状态\\nwestd-20861: 无 GPU 信息\\n\\n## 告警\\n- phase2_tg_s42_v2: 已被终止 — unknown\\n- phase2_tg_s42_v4: 训练失败 — unknown\\n- phase2_tg_s42_v8_schedsampling: 训练失败 — unknown\\n- phase2_tg_s42_v8b_ss_fixed: 训练失败 — unknown\\n- d048_split_softmax_eval: 训练失败 — unknown\\n- phase1a_multiseed_qwen: 已被终止 — unknown\\n- phase2_switching: 已被终止 — unknown\\n- p1_ss_lora_only: 已被终止 — unknown\\n\", \"total_chars\": 2436, \"truncated\": false}, \"error\": null, \"metadata\": {}}"
    }
  },
  "sourceToolAssistantUUID": "e0af7716-dcd4-40de-b4fc-a82581a8224a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921",
  "sessionId": "5d779602-0719-4d06-8bf9-fdd84990d5d0",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---


### Assistant

_source line 105 · 2026-05-25T20:42:06.535Z_

<details><summary>Logged reasoning block</summary>

```text
Report and registry status haven't changed much since my last review. The worker was supposed to fix the appendix issues I identified. Let me check the actual changes to the appendix tables.

My previous findings were:
1. [warning] tab_crossmodel_detail Qwen SS row mixes single-seed TF (0.498) with 3-seed mean AR (0.401), gap 1.2× is incorrect
2. [warning] tab_perseed_tg uses N=5 T=10 old eval protocol (gap=31×) vs main results N=50 (gap=8×)


3. [info] SS s42 TF GAR shows inconsistency across tables (0.498 vs 0.502)
4. [info] Cost table has rounding issues in training time values

Now I need to look at the current versions of these files to verify whether the worker addressed any of these problems.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "58528b50-2495-4946-8cb4-5b9b52f97616",
  "isSidechain": false,
  "requestId": "req_011CbPwEymLbLZVCXXNrmodd",
  "type": "assistant",
  "uuid": "e829d09a-9ce6-43b6-9f14-a39338dc1b69",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921",
  "sessionId": "5d779602-0719-4d06-8bf9-fdd84990d5d0",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VVXmgVPnyfNrvUjdvnqnkj",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1739,
      "cache_read_input_tokens": 103162,
      "output_tokens": 493,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1739,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 493,
          "cache_read_input_tokens": 103162,
          "cache_creation_input_tokens": 1739,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1739
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

_source line 106 · 2026-05-25T20:42:06.663Z_

状态无变化。现在检查 worker 对附录表格的修复。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e829d09a-9ce6-43b6-9f14-a39338dc1b69",
  "isSidechain": false,
  "requestId": "req_011CbPwEymLbLZVCXXNrmodd",
  "type": "assistant",
  "uuid": "9bd8fe3c-02fd-44f1-a02a-f5291231c77c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921",
  "sessionId": "5d779602-0719-4d06-8bf9-fdd84990d5d0",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VVXmgVPnyfNrvUjdvnqnkj",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1739,
      "cache_read_input_tokens": 103162,
      "output_tokens": 493,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1739,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 493,
          "cache_read_input_tokens": 103162,
          "cache_creation_input_tokens": 1739,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1739
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

_source line 107 · 2026-05-25T20:42:08.667Z_

<details open><summary>🔧 Tool call — Read · `toolu_013k6L3Tiqf8j4Yn3fYtSXpv`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/appendix_expansion/tab_crossmodel_detail.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9bd8fe3c-02fd-44f1-a02a-f5291231c77c",
  "isSidechain": false,
  "requestId": "req_011CbPwEymLbLZVCXXNrmodd",
  "type": "assistant",
  "uuid": "69e70f34-55eb-4263-8e5f-93a085c4e5d6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921",
  "sessionId": "5d779602-0719-4d06-8bf9-fdd84990d5d0",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VVXmgVPnyfNrvUjdvnqnkj",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1739,
      "cache_read_input_tokens": 103162,
      "output_tokens": 493,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1739,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 493,
          "cache_read_input_tokens": 103162,
          "cache_creation_input_tokens": 1739,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1739
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

_source line 108 · 2026-05-25T20:42:09.408Z_

<details><summary>↩ Tool result · `toolu_01BtTWZWQfMbuM74XHGdFmyh`</summary>

```text
1	% Per-seed detailed results for Scheduled Sampling (SS) — seeds 42, 123, 456
2	% TF eval: N=200, T=3 (teacher-forced on held-out eval_200 set)
3	% AR eval: N=50 gen-mode, beta=0/3/5 (from d048_final_ar)
4	\begin{table}[h]
5	\centering
6	\caption{Per-seed results for Scheduled Sampling (SS) on Qwen2.5-7B-Instruct.
7	TF evaluation uses 200 held-out conversations; AR evaluation uses 50 model-generated conversations in free-form generation mode ($N_{\text{valid}} \approx 39$).}
8	\label{tab:perseed-ss}
9	\resizebox{\columnwidth}{!}{
10	\begin{tabular}{@{}l ccc c@{}}
11	\toprule
12	\textbf{Metric} & \textbf{Seed 42} & \textbf{Seed 123} & \textbf{Seed 456} & \textbf{Mean $\pm$ Std} \\
13	\midrule
14	\multicolumn{5}{@{}l}{\textit{Teacher-Forced (TF)}} \\
15	\quad GAR-ours $\uparrow$   & 0.502 & 0.554 & 0.496 & 0.517 $\pm$ 0.032 \\
16	\quad GAR-Dongre $\uparrow$ & 0.389 & 0.411 & 0.386 & 0.395 $\pm$ 0.014 \\
17	\quad PPL $\downarrow$       & 2.780 & 2.612 & 2.611 & 2.668 $\pm$ 0.097 \\
18	\midrule
19	\multicolumn{5}{@{}l}{\textit{Autoregressive (AR), $\beta = 0$}} \\
20	\quad GAR-ours $\uparrow$   & 0.347 & 0.423 & 0.433 & 0.401 $\pm$ 0.047 \\
21	\quad PPL $\downarrow$       & 1.442 & 1.441 & 1.439 & 1.441 $\pm$ 0.002 \\
22	\midrule
23	\multicolumn{5}{@{}l}{\textit{Autoregressive (AR), $\beta = 3$}} \\
24	\quad GAR-ours $\uparrow$   & 0.593 & 0.590 & 0.605 & 0.596 $\pm$ 0.008 \\
25	\quad PPL $\downarrow$       & 1.564 & 1.607 & 1.587 & 1.586 $\pm$ 0.022 \\
26	\midrule
27	\multicolumn{5}{@{}l}{\textit{Autoregressive (AR), $\beta = 5$}} \\
28	\quad GAR-ours $\uparrow$   & 0.717 & 0.717 & 0.716 & 0.717 $\pm$ 0.001 \\
29	\quad PPL $\downarrow$       & 1.779 & 1.785 & 1.804 & 1.789 $\pm$ 0.013 \\
30	\bottomrule
31	\end{tabular}}
32	\end{table}
33	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "04292c72-0ede-4fa6-90c6-772572d40d7b",
  "isSidechain": false,
  "promptId": "8d8464e4-1523-464c-8d63-5cd7db13bd3f",
  "type": "user",
  "uuid": "7d056654-5262-4e21-ab01-95a2479ef139",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/appendix_expansion/tab_perseed_ss.tex",
      "content": "% Per-seed detailed results for Scheduled Sampling (SS) — seeds 42, 123, 456\n% TF eval: N=200, T=3 (teacher-forced on held-out eval_200 set)\n% AR eval: N=50 gen-mode, beta=0/3/5 (from d048_final_ar)\n\\begin{table}[h]\n\\centering\n\\caption{Per-seed results for Scheduled Sampling (SS) on Qwen2.5-7B-Instruct.\nTF evaluation uses 200 held-out conversations; AR evaluation uses 50 model-generated conversations in free-form generation mode ($N_{\\text{valid}} \\approx 39$).}\n\\label{tab:perseed-ss}\n\\resizebox{\\columnwidth}{!}{\n\\begin{tabular}{@{}l ccc c@{}}\n\\toprule\n\\textbf{Metric} & \\textbf{Seed 42} & \\textbf{Seed 123} & \\textbf{Seed 456} & \\textbf{Mean $\\pm$ Std} \\\\\n\\midrule\n\\multicolumn{5}{@{}l}{\\textit{Teacher-Forced (TF)}} \\\\\n\\quad GAR-ours $\\uparrow$   & 0.502 & 0.554 & 0.496 & 0.517 $\\pm$ 0.032 \\\\\n\\quad GAR-Dongre $\\uparrow$ & 0.389 & 0.411 & 0.386 & 0.395 $\\pm$ 0.014 \\\\\n\\quad PPL $\\downarrow$       & 2.780 & 2.612 & 2.611 & 2.668 $\\pm$ 0.097 \\\\\n\\midrule\n\\multicolumn{5}{@{}l}{\\textit{Autoregressive (AR), $\\beta = 0$}} \\\\\n\\quad GAR-ours $\\uparrow$   & 0.347 & 0.423 & 0.433 & 0.401 $\\pm$ 0.047 \\\\\n\\quad PPL $\\downarrow$       & 1.442 & 1.441 & 1.439 & 1.441 $\\pm$ 0.002 \\\\\n\\midrule\n\\multicolumn{5}{@{}l}{\\textit{Autoregressive (AR), $\\beta = 3$}} \\\\\n\\quad GAR-ours $\\uparrow$   & 0.593 & 0.590 & 0.605 & 0.596 $\\pm$ 0.008 \\\\\n\\quad PPL $\\downarrow$       & 1.564 & 1.607 & 1.587 & 1.586 $\\pm$ 0.022 \\\\\n\\midrule\n\\multicolumn{5}{@{}l}{\\textit{Autoregressive (AR), $\\beta = 5$}} \\\\\n\\quad GAR-ours $\\uparrow$   & 0.717 & 0.717 & 0.716 & 0.717 $\\pm$ 0.001 \\\\\n\\quad PPL $\\downarrow$       & 1.779 & 1.785 & 1.804 & 1.789 $\\pm$ 0.013 \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n",
      "numLines": 33,
      "startLine": 1,
      "totalLines": 33
    }
  },
  "sourceToolAssistantUUID": "04292c72-0ede-4fa6-90c6-772572d40d7b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921",
  "sessionId": "5d779602-0719-4d06-8bf9-fdd84990d5d0",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---


### Tool result

_source line 109 · 2026-05-25T20:42:08.679Z_

<details><summary>↩ Tool result · `toolu_013k6L3Tiqf8j4Yn3fYtSXpv`</summary>

```text
1	% Cross-model detailed comparison: Qwen2.5-7B-Instruct vs Llama-3.1-8B-Instruct
2	% Conditions shared by both models: Base, ThreadGate, LoRA-only
3	% Qwen TF: N=200 held-out; Qwen AR: d048_final_ar N=50 gen beta=0
4	% Llama TF: N=50 held-out T=4; Llama AR: eval_llama_ar_n20 N=20 T=4
5	% Llama SS: p1_llama_ss_eval (epoch_1 checkpoint, N=50)
6	\begin{table*}[t]
7	\centering
8	\caption{Cross-model comparison of goal-adherence metrics on Qwen2.5-7B-Instruct and Llama-3.1-8B-Instruct.
9	Gap ratio = TF GAR / AR GAR; lower is better (less exposure bias).
10	Qwen AR uses $N{=}50$ gen-mode evaluation; Llama AR uses $N{=}20$, $T{=}4$ (SS: $N{=}50$).
11	Llama AR GAR and gaps are mean-based; median-based TG gap is 27$\times$ (\S\ref{subsec:cross-model}).}
12	\label{tab:crossmodel-detail}
13	\small
14	\begin{tabular}{@{}ll ccccc@{}}
15	\toprule
16	\textbf{Model} & \textbf{Condition} & \textbf{TF GAR}$\uparrow$ & \textbf{AR GAR}$\uparrow$ & \textbf{TF PPL}$\downarrow$ & \textbf{AR PPL}$\downarrow$ & \textbf{Gap}$\downarrow$ \\
17	\midrule
18	\multirow{4}{*}{Qwen-7B}
19	  & Base      & 0.013 & 0.019 & 4.34 & 1.447 & 0.7$\times$ \\
20	  & TG        & 0.504 & 0.064 & 2.78 & 1.432 & 7.9$\times$ \\
21	  & LoRA-only & 0.498 & 0.037 & 2.78 & 1.431 & 13.5$\times$ \\
22	  & \textbf{SS} & 0.498 & \textbf{0.401} & 2.78 & 1.441 & \textbf{1.2$\times$} \\
23	\midrule
24	\multirow{4}{*}{Llama-8B}
25	  & Base      & 0.017 & 0.009 & 3.45 & 1.293 & 1.9$\times$ \\
26	  & TG        & 0.484 & 0.043 & 2.57 & 1.437 & 11.2$\times$ \\
27	  & LoRA-only & 0.481 & 0.028 & 2.60 & 1.419 & 17.2$\times$ \\
28	  & \textbf{SS} & 0.477 & \textbf{0.166} & 2.82 & 1.370 & \textbf{2.9$\times$} \\
29	\bottomrule
30	\end{tabular}
31	\end{table*}
32	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "69e70f34-55eb-4263-8e5f-93a085c4e5d6",
  "isSidechain": false,
  "promptId": "8d8464e4-1523-464c-8d63-5cd7db13bd3f",
  "type": "user",
  "uuid": "f85f63f6-0ac3-4622-bb80-f1a56a4eca38",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/appendix_expansion/tab_crossmodel_detail.tex",
      "content": "% Cross-model detailed comparison: Qwen2.5-7B-Instruct vs Llama-3.1-8B-Instruct\n% Conditions shared by both models: Base, ThreadGate, LoRA-only\n% Qwen TF: N=200 held-out; Qwen AR: d048_final_ar N=50 gen beta=0\n% Llama TF: N=50 held-out T=4; Llama AR: eval_llama_ar_n20 N=20 T=4\n% Llama SS: p1_llama_ss_eval (epoch_1 checkpoint, N=50)\n\\begin{table*}[t]\n\\centering\n\\caption{Cross-model comparison of goal-adherence metrics on Qwen2.5-7B-Instruct and Llama-3.1-8B-Instruct.\nGap ratio = TF GAR / AR GAR; lower is better (less exposure bias).\nQwen AR uses $N{=}50$ gen-mode evaluation; Llama AR uses $N{=}20$, $T{=}4$ (SS: $N{=}50$).\nLlama AR GAR and gaps are mean-based; median-based TG gap is 27$\\times$ (\\S\\ref{subsec:cross-model}).}\n\\label{tab:crossmodel-detail}\n\\small\n\\begin{tabular}{@{}ll ccccc@{}}\n\\toprule\n\\textbf{Model} & \\textbf{Condition} & \\textbf{TF GAR}$\\uparrow$ & \\textbf{AR GAR}$\\uparrow$ & \\textbf{TF PPL}$\\downarrow$ & \\textbf{AR PPL}$\\downarrow$ & \\textbf{Gap}$\\downarrow$ \\\\\n\\midrule\n\\multirow{4}{*}{Qwen-7B}\n  & Base      & 0.013 & 0.019 & 4.34 & 1.447 & 0.7$\\times$ \\\\\n  & TG        & 0.504 & 0.064 & 2.78 & 1.432 & 7.9$\\times$ \\\\\n  & LoRA-only & 0.498 & 0.037 & 2.78 & 1.431 & 13.5$\\times$ \\\\\n  & \\textbf{SS} & 0.498 & \\textbf{0.401} & 2.78 & 1.441 & \\textbf{1.2$\\times$} \\\\\n\\midrule\n\\multirow{4}{*}{Llama-8B}\n  & Base      & 0.017 & 0.009 & 3.45 & 1.293 & 1.9$\\times$ \\\\\n  & TG        & 0.484 & 0.043 & 2.57 & 1.437 & 11.2$\\times$ \\\\\n  & LoRA-only & 0.481 & 0.028 & 2.60 & 1.419 & 17.2$\\times$ \\\\\n  & \\textbf{SS} & 0.477 & \\textbf{0.166} & 2.82 & 1.370 & \\textbf{2.9$\\times$} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n",
      "numLines": 32,
      "startLine": 1,
      "totalLines": 32
    }
  },
  "sourceToolAssistantUUID": "69e70f34-55eb-4263-8e5f-93a085c4e5d6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921",
  "sessionId": "5d779602-0719-4d06-8bf9-fdd84990d5d0",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---


### Tool call

_source line 110 · 2026-05-25T20:42:09.153Z_

<details open><summary>🔧 Tool call — Read · `toolu_01NfkjkPTuwBg2sFB1ie8qjD`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/appendix_expansion/tab_perseed_tg.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f85f63f6-0ac3-4622-bb80-f1a56a4eca38",
  "isSidechain": false,
  "requestId": "req_011CbPwEymLbLZVCXXNrmodd",
  "type": "assistant",
  "uuid": "23f3799e-d985-4d1a-bbab-ed03497b770c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921",
  "sessionId": "5d779602-0719-4d06-8bf9-fdd84990d5d0",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VVXmgVPnyfNrvUjdvnqnkj",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1739,
      "cache_read_input_tokens": 103162,
      "output_tokens": 493,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1739,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 493,
          "cache_read_input_tokens": 103162,
          "cache_creation_input_tokens": 1739,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1739
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

_source line 111 · 2026-05-25T20:42:09.166Z_

<details><summary>↩ Tool result · `toolu_01NfkjkPTuwBg2sFB1ie8qjD`</summary>

```text
1	% Per-seed detailed results for ThreadGate (TG) — seeds 42, 123
2	% TF eval: N=200 held-out conversations
3	% AR eval: N=5, T=10 model-generated conversations (original eval protocol)
4	\begin{table}[h]
5	\centering
6	\caption{Per-seed results for ThreadGate (TG) on Qwen2.5-7B-Instruct.
7	TF evaluation uses 200 held-out conversations.
8	AR evaluation uses 5 model-generated conversations with 10 turns each.}
9	\label{tab:perseed-tg}
10	\resizebox{\columnwidth}{!}{
11	\begin{tabular}{@{}l cc c@{}}
12	\toprule
13	\textbf{Metric} & \textbf{Seed 42} & \textbf{Seed 123} & \textbf{Mean $\pm$ Std} \\
14	\midrule
15	\multicolumn{4}{@{}l}{\textit{Teacher-Forced (TF)}} \\
16	\quad GAR-ours $\uparrow$   & 0.504 & 0.505 & 0.504 $\pm$ 0.001 \\
17	\quad GAR-Dongre $\uparrow$ & 0.015 & 0.012 & 0.014 $\pm$ 0.002 \\
18	\quad PPL $\downarrow$       & 2.784 & 2.780 & 2.782 $\pm$ 0.003 \\
19	\midrule
20	\multicolumn{4}{@{}l}{\textit{Autoregressive (AR), $\beta = 0$}} \\
21	\quad GAR-ours $\uparrow$   & 0.016 & 0.017 & 0.016 $\pm$ 0.001 \\
22	\quad GAR-Dongre $\uparrow$ & 0.019 & 0.018 & 0.019 $\pm$ 0.001 \\
23	\quad PPL $\downarrow$       & 1.360 & 1.386 & 1.373 $\pm$ 0.018 \\
24	\midrule
25	\multicolumn{4}{@{}l}{\textit{Derived}} \\
26	\quad Gap ratio (TF/AR GAR-ours) $\downarrow$ & 32.1 & 30.6 & 31.4 $\pm$ 1.1 \\
27	\bottomrule
28	\end{tabular}}
29	\end{table}
30	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "23f3799e-d985-4d1a-bbab-ed03497b770c",
  "isSidechain": false,
  "promptId": "8d8464e4-1523-464c-8d63-5cd7db13bd3f",
  "type": "user",
  "uuid": "27656318-71cb-4cef-9829-487a4234ec70",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/appendix_expansion/tab_perseed_tg.tex",
      "content": "% Per-seed detailed results for ThreadGate (TG) — seeds 42, 123\n% TF eval: N=200 held-out conversations\n% AR eval: N=5, T=10 model-generated conversations (original eval protocol)\n\\begin{table}[h]\n\\centering\n\\caption{Per-seed results for ThreadGate (TG) on Qwen2.5-7B-Instruct.\nTF evaluation uses 200 held-out conversations.\nAR evaluation uses 5 model-generated conversations with 10 turns each.}\n\\label{tab:perseed-tg}\n\\resizebox{\\columnwidth}{!}{\n\\begin{tabular}{@{}l cc c@{}}\n\\toprule\n\\textbf{Metric} & \\textbf{Seed 42} & \\textbf{Seed 123} & \\textbf{Mean $\\pm$ Std} \\\\\n\\midrule\n\\multicolumn{4}{@{}l}{\\textit{Teacher-Forced (TF)}} \\\\\n\\quad GAR-ours $\\uparrow$   & 0.504 & 0.505 & 0.504 $\\pm$ 0.001 \\\\\n\\quad GAR-Dongre $\\uparrow$ & 0.015 & 0.012 & 0.014 $\\pm$ 0.002 \\\\\n\\quad PPL $\\downarrow$       & 2.784 & 2.780 & 2.782 $\\pm$ 0.003 \\\\\n\\midrule\n\\multicolumn{4}{@{}l}{\\textit{Autoregressive (AR), $\\beta = 0$}} \\\\\n\\quad GAR-ours $\\uparrow$   & 0.016 & 0.017 & 0.016 $\\pm$ 0.001 \\\\\n\\quad GAR-Dongre $\\uparrow$ & 0.019 & 0.018 & 0.019 $\\pm$ 0.001 \\\\\n\\quad PPL $\\downarrow$       & 1.360 & 1.386 & 1.373 $\\pm$ 0.018 \\\\\n\\midrule\n\\multicolumn{4}{@{}l}{\\textit{Derived}} \\\\\n\\quad Gap ratio (TF/AR GAR-ours) $\\downarrow$ & 32.1 & 30.6 & 31.4 $\\pm$ 1.1 \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n",
      "numLines": 30,
      "startLine": 1,
      "totalLines": 30
    }
  },
  "sourceToolAssistantUUID": "23f3799e-d985-4d1a-bbab-ed03497b770c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921",
  "sessionId": "5d779602-0719-4d06-8bf9-fdd84990d5d0",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---


### Tool call

_source line 112 · 2026-05-25T20:42:09.404Z_

<details open><summary>🔧 Tool call — Read · `toolu_01BtTWZWQfMbuM74XHGdFmyh`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/appendix_expansion/tab_perseed_ss.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "27656318-71cb-4cef-9829-487a4234ec70",
  "isSidechain": false,
  "requestId": "req_011CbPwEymLbLZVCXXNrmodd",
  "type": "assistant",
  "uuid": "04292c72-0ede-4fa6-90c6-772572d40d7b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921",
  "sessionId": "5d779602-0719-4d06-8bf9-fdd84990d5d0",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VVXmgVPnyfNrvUjdvnqnkj",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1739,
      "cache_read_input_tokens": 103162,
      "output_tokens": 493,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1739,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 493,
          "cache_read_input_tokens": 103162,
          "cache_creation_input_tokens": 1739,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1739
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

_source line 113_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[服务器重启后首条消息] 当前日期: 2026-05-25。服务器刚重启，项目状态可能已更新。在处理审查请求前，**先读取 registry.yaml 和 report.md** 获取最新实验状态，不要依赖对话历史中的状态信息。  **审查请求：** [系统通知 — worker_done:worker_fix_audit_appendix_issues_20260525T203522]: Wor…",
  "leafUuid": "7d056654-5262-4e21-ab01-95a2479ef139",
  "sessionId": "5d779602-0719-4d06-8bf9-fdd84990d5d0"
}
```

---


### Runtime record

_source line 114_

```json
{
  "type": "ai-title",
  "aiTitle": "Review worker audit appendix tables completion",
  "sessionId": "5d779602-0719-4d06-8bf9-fdd84990d5d0"
}
```

---


### Assistant

_source line 115 · 2026-05-25T20:42:26.688Z_

<details><summary>Logged reasoning block</summary>

```text
The tables are UNCHANGED from what I reviewed before. The worker was supposed to fix the issues I identified:

1. tab_crossmodel_detail: Still shows Qwen SS TF GAR = 0.498 (single-seed) and AR GAR = 0.401 (3-seed mean), gap 1.2×. **NOT FIXED.**
2. tab_perseed_tg: Still uses N=5, T=10 old eval protocol. **NOT FIXED.**
3. tab_perseed_ss: Same as before. (This was info-level)


4. Let me check if the worker made changes elsewhere - maybe in the appendix.tex itself, or added footnotes/notes, or modified the caption.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7d056654-5262-4e21-ab01-95a2479ef139",
  "isSidechain": false,
  "requestId": "req_011CbPwFu9YoLdx9d751vjXg",
  "type": "assistant",
  "uuid": "2aceed30-4949-4af0-8f30-f802145e97ab",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921",
  "sessionId": "5d779602-0719-4d06-8bf9-fdd84990d5d0",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RJfBKFz5cQfYEXQJLSQAQt",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3165,
      "cache_read_input_tokens": 104901,
      "output_tokens": 458,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3165,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 458,
          "cache_read_input_tokens": 104901,
          "cache_creation_input_tokens": 3165,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3165
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

_source line 116 · 2026-05-25T20:42:26.853Z_

三张表均未改变。让我检查 worker 是否在附录正文中添加了说明性文字。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2aceed30-4949-4af0-8f30-f802145e97ab",
  "isSidechain": false,
  "requestId": "req_011CbPwFu9YoLdx9d751vjXg",
  "type": "assistant",
  "uuid": "688abc89-48b3-40f2-8caa-f5ce05d06c0b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921",
  "sessionId": "5d779602-0719-4d06-8bf9-fdd84990d5d0",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RJfBKFz5cQfYEXQJLSQAQt",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3165,
      "cache_read_input_tokens": 104901,
      "output_tokens": 458,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3165,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 458,
          "cache_read_input_tokens": 104901,
          "cache_creation_input_tokens": 3165,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3165
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

_source line 117 · 2026-05-25T20:42:27.826Z_

<details open><summary>🔧 Tool call — Bash · `toolu_0161KCdkcuECf8L4911dCQp2`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating && git log --oneline -5",
  "description": "Check latest commits"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "688abc89-48b3-40f2-8caa-f5ce05d06c0b",
  "isSidechain": false,
  "requestId": "req_011CbPwFu9YoLdx9d751vjXg",
  "type": "assistant",
  "uuid": "959351fc-9c0a-4c07-9e96-8a16ae5e8b39",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921",
  "sessionId": "5d779602-0719-4d06-8bf9-fdd84990d5d0",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RJfBKFz5cQfYEXQJLSQAQt",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3165,
      "cache_read_input_tokens": 104901,
      "output_tokens": 458,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3165,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 458,
          "cache_read_input_tokens": 104901,
          "cache_creation_input_tokens": 3165,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3165
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

_source line 118 · 2026-05-25T20:42:27.999Z_

<details><summary>↩ Tool result · `toolu_0161KCdkcuECf8L4911dCQp2`</summary>

```text
98eff19 [paper] Fix cross-model gap comparison + add median justification
73a7969 [paper] Write Llama LoRA-only cross-model results (C5 completion)
74bb496 [paper] Add Li et al. 2024 (direct competitor) + strengthen exposure bias citations
2e58ab1 [paper] Fix 2 author errors + 3 bib warnings from citation audit
c93a515 [paper] Multi-seed v7 TG data + v8b SS training schedule observation
Shell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "959351fc-9c0a-4c07-9e96-8a16ae5e8b39",
  "isSidechain": false,
  "promptId": "8d8464e4-1523-464c-8d63-5cd7db13bd3f",
  "type": "user",
  "uuid": "d21870c0-13b7-4380-b23c-20afbddf25e9",
  "toolUseResult": {
    "stdout": "98eff19 [paper] Fix cross-model gap comparison + add median justification\n73a7969 [paper] Write Llama LoRA-only cross-model results (C5 completion)\n74bb496 [paper] Add Li et al. 2024 (direct competitor) + strengthen exposure bias citations\n2e58ab1 [paper] Fix 2 author errors + 3 bib warnings from citation audit\nc93a515 [paper] Multi-seed v7 TG data + v8b SS training schedule observation",
    "stderr": "\nShell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "959351fc-9c0a-4c07-9e96-8a16ae5e8b39",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921",
  "sessionId": "5d779602-0719-4d06-8bf9-fdd84990d5d0",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---


### Tool call

_source line 119 · 2026-05-25T20:42:28.747Z_

<details open><summary>🔧 Tool call — Bash · `toolu_014p4AtDkQx6bbti1PAzBEZG`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating && git diff HEAD~3 -- artifacts/appendix_expansion/ paper/sections/appendix.tex 2>/dev/null | head -200",
  "description": "Check recent changes to appendix files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d21870c0-13b7-4380-b23c-20afbddf25e9",
  "isSidechain": false,
  "requestId": "req_011CbPwFu9YoLdx9d751vjXg",
  "type": "assistant",
  "uuid": "f9cce00b-a83c-4342-9397-3840d0729f73",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921",
  "sessionId": "5d779602-0719-4d06-8bf9-fdd84990d5d0",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RJfBKFz5cQfYEXQJLSQAQt",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3165,
      "cache_read_input_tokens": 104901,
      "output_tokens": 458,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3165,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 458,
          "cache_read_input_tokens": 104901,
          "cache_creation_input_tokens": 3165,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3165
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

_source line 120 · 2026-05-25T20:42:28.822Z_

<details><summary>↩ Tool result · `toolu_014p4AtDkQx6bbti1PAzBEZG`</summary>

```text
diff --git a/paper/sections/appendix.tex b/paper/sections/appendix.tex
index 8f1bb3d..8f22842 100644
--- a/paper/sections/appendix.tex
+++ b/paper/sections/appendix.tex
@@ -1,26 +1,850 @@
-\section{Training Hyperparameters}\label{sec:appendix-hyper}
+\section{Training Configuration}\label{sec:appendix-hyper}
 
-All fine-tuned variants share the following configuration: Qwen-2.5-7B-Instruct base model, LoRA rank 16 ($\alpha$=32) on \texttt{q\_proj} and \texttt{v\_proj}, AdamW optimizer (lr = $2 \times 10^{-4}$, $\beta_1$=0.9, $\beta_2$=0.999), batch size 1 with gradient accumulation 8, 3 epochs over 8K UltraChat conversations, maximum sequence length 2048, seed 42. ThreadGate gates use a 10$\times$ learning rate multiplier and initial bias 1.5 ($\sigma(1.5) \approx 0.82$).
+Table~\ref{tab:hyperparams} lists the full training configuration shared across all fine-tuned variants. ThreadGate gate parameters receive a $10\times$ learning rate multiplier and are initialized with bias 1.5 ($\sigma(1.5) \approx 0.82$); the gate MLP adds ${\sim}$57K parameters per variant ($<$0.001\% of 7B). The scheduled sampling variant (v8b) linearly increases the model-generated context ratio from 0 to 0.3 over 3 epochs (29.7--37.1\% effective usage due to per-sample Bernoulli sampling). All experiments were conducted on a single NVIDIA RTX PRO 6000 Blackwell Server Edition GPU (96\,GB VRAM), requiring 6--8 hours per variant.
+
+\begin{table}[t]
+\centering\small
+\caption{Training hyperparameters for all fine-tuned variants. Entries marked $\dagger$ apply only to ThreadGate and its ablations.}
+\label{tab:hyperparams}
+\begin{tabular}{l@{\hspace{8pt}}l}
+\toprule
+\textbf{Parameter} & \textbf{Value} \\
+\midrule
+Base model & Qwen-2.5-7B-Instruct \\
+LoRA rank / $\alpha$ & 16 / 32 \\
+LoRA targets & \texttt{q\_proj}, \texttt{v\_proj} \\
+Optimizer & AdamW ($\beta_1$\!=\!0.9, $\beta_2$\!=\!0.999) \\
+Learning rate & $2 \times 10^{-4}$ \\
+Gate LR mult.$^\dagger$ & $10\times$ \\
+Batch / grad accum & 1 / 8 (eff.\ 8) \\
+Epochs & 3 \\
+Max seq length & 2048 \\
+Training data & 8K UltraChat convs \\
+Seed & 42 (+123 for TG, SS) \\
+$\lambda_\text{GAR}$/$\lambda_\text{div}$ & 1.0 / 1.0 \\
+GAR target $\tau$ & 0.5 \\
+Gate init bias$^\dagger$ & 1.5 ($\sigma\!\approx\!0.82$) \\
+Gate hidden dim$^\dagger$ & 64 \\
+Turn embed dim$^\dagger$ & 16 \\
+GPU & RTX PRO 6000 (96\,GB) \\
+Training time & 6--8 h / variant \\
+\bottomrule
+\end{tabular}
+\end{table}
 
 \section{Loss Formulation Search}\label{sec:appendix-loss}
 
-Table~\ref{tab:loss-iterations} summarizes the seven loss configurations explored before arriving at the final MSE + gate diversity formulation (\S\ref{sec:loss}). Configurations v1--v6 span three alternative loss families; none converged during training.
+The final MSE + gate diversity loss (\S\ref{sec:loss}) emerged from seven iterations spanning four loss families. Table~\ref{tab:loss-iterations} summarizes the progression. The search was motivated by a consistent failure mode: naive formulations either collapse to trivial solutions (cumulative losses) or drive gates toward identity (maximize-family losses). We describe each family below.
 
-\begin{table}[h]
-\centering\small
-\caption{Loss formulation iterations on Qwen-2.5-7B-Instruct. GAR-ours (teacher-forced) and PPL are reported only for the converged configuration.}
+\paragraph{Cumulative losses (v1--v2).} These losses accumulate GAR contributions across layers, rewarding monotonically increasing attention. v1 collapsed because once the cumulative GAR exceeded the threshold, the loss gradient vanished and gates froze. v2 added an $\varepsilon$-stabilization term to the cumulative product, but numerical instability from the product of 28 per-layer terms dominated, and training followed the same trajectory.
+
+\paragraph{Maximize losses (v3--v5).} These losses directly maximize mean GAR ($-\text{mean}(\text{GAR})$). The unbounded objective rewards full pass-through ($g \to 1.0$), collapsing gate diversity (std $<$ 0.025). At $\lambda$=2 (v3), gates froze within 100 steps; at $\lambda$=10 (v3b), convergence to identity accelerated; at $\lambda$=1 (v5), rebalancing delayed but did not prevent the same degenerate solution.
+
+\paragraph{Smooth saturation (v6).} This bounded the reward using a saturating function, intended to prevent the unbounded growth of maximize losses. In practice, the loss landscape remained monotonic in $g$, and training followed the same terminal trajectory as the maximize family, only more slowly.
+
+\paragraph{MSE + gate diversity (v7).} The MSE formulation provides bidirectional pressure: GAR above $\tau$ incurs the same penalty as GAR below $\tau$, preventing the runaway optimization of maximize losses. The gate diversity regularizer ($\mathcal{L}_\text{div}$) enforces a minimum standard deviation across per-layer gate values, preventing all gates from collapsing to a uniform value. This combination is the only one that achieved stable convergence (GAR-ours = 0.50, PPL = 2.78).
+
+\begin{table*}[t]
+\centering\footnotesize
+\caption{Loss formulation iterations on Qwen-2.5-7B-Instruct. GAR-ours (teacher-forced) and PPL are reported only for the converged configuration (v7).}
 \label{tab:loss-iterations}
-\begin{tabular}{l l l c c}
+\begin{tabular}{l l l p{5.8cm} c c}
+\toprule
+ & \textbf{Loss Family} & \textbf{Status} & \textbf{Failure Mechanism} & \textbf{GAR} & \textbf{PPL} \\
+\midrule
+v1  & Cumulative            & \texttimes~GAR loss $\to$ 0     & GAR loss collapses to zero once threshold is reached; gate gradients vanish at equilibrium & ---  & ---  \\
+v2  & Cumulative + $\varepsilon$ & \texttimes~same trajectory & Numerical instability from cumulative product; $\varepsilon$-stabilization insufficient & ---  & ---  \\
+v3  & Maximize ($\lambda$=2)  & \texttimes~gate frozen        & Unbounded reward drives gates toward identity (all-pass); no layer selectivity & ---  & ---  \\
+v3b & Maximize ($\lambda$=10) & \texttimes~identity collapse   & Higher $\lambda$ accelerates convergence to same degenerate identity solution & ---  & ---  \\
+v5  & Maximize ($\lambda$=1)  & \texttimes~identity collapse   & Rebalancing delays but does not prevent identity collapse & ---  & ---  \\
+v6  & Smooth saturation       & \texttimes~identity collapse   & Monotonic reward identical to maximize in practice; boundedness slows but does not alter terminal trajectory & ---  & ---  \\
+v7  & MSE + gate div          & \checkmark~\textbf{converged}  & \textbf{Bidirectional penalty prevents identity collapse; gate diversity regularizer enforces layer selectivity} & 0.50 & 2.78 \\
+\bottomrule
+\end{tabular}
+\end{table*}
+
+\section{Instruction Retention Details}\label{sec:appendix-ir}
+
+To evaluate whether GAR improvements translate to downstream task performance, we test instruction retention across 18 system-prompt constraint types using the ThreadGate checkpoint with $\beta$\,=\,3 steering on $N$\,=\,200 held-out conversations. Each constraint type requires the model to follow a specific instruction embedded in the system prompt (e.g., ``always respond in bullet points'', ``never use the word X'', ``include a summary at the end''). This evaluation bridges the gap between our attention-level metric (GAR) and observable model behavior.
+
+\paragraph{Evaluation protocol.} For each conversation, we inject a constraint into the system prompt and evaluate compliance across all assistant turns. A turn is compliant if it satisfies the constraint according to rule-based checkers (for format, count, and position constraints) or GPT-4-based evaluation (for content constraints, which require semantic judgment). We use the same 18 constraint types across all conversations, yielding $N$\,=\,54 paired evaluations (18 types $\times$ 3 conversations per type) for the McNemar analysis.
+
+\paragraph{Per-category results.} Table~\ref{tab:ir-results} reports per-category compliance rates. Content constraints---which require attending to and recalling specific system-prompt instructions across turns---show the largest improvement (+23.8\,pp), consistent with GAR measuring attention to goal tokens. This category includes constraints like ``mention X in every response'' and ``always reference the original topic,'' which require sustained attention to the system prompt. Position constraints (e.g., ``start each response with Y'') show a modest improvement (+6.7\,pp), as they partially depend on goal-token attention. Format (e.g., ``use bullet points'') and count constraints (e.g., ``exactly 3 sentences'') show no change, consistent with these being procedural patterns that are cached in the model's generation routine rather than requiring ongoing attention to the system prompt.
+
+\paragraph{Correlation analysis.} The GAR-compliance correlation ($r$\,=\,0.200, $p$\,=\,0.007) is statistically significant but modest, suggesting that attention to goal tokens is one of several factors in instruction compliance. Other factors likely include the model's procedural memory for format constraints, the specificity of the constraint (vague constraints are harder regardless of attention), and the interaction between constraint type and conversation topic. McNemar's test ($p$\,=\,0.077) is marginally significant for the overall compliance improvement, reflecting the small sample size (18 constraint types). These results are exploratory and pending multi-model confirmation.
+
+Figure~\ref{fig:ir-bar} visualizes the per-category breakdown.
+
+\begin{figure}[t]
+  \centering
+  \includegraphics[width=\columnwidth]{fig_instruction_retention.pdf}
+  \caption{Instruction retention by constraint category under $\beta$\,=\,3 steering. Content constraints benefit most (+23.8\,pp); format and count constraints are unaffected.}
+  \label{fig:ir-bar}
+\end{figure}
+
+\FloatBarrier
+
+\begin{table}[t]
+\centering\small
+\caption{Instruction retention by constraint category ($\beta$\,=\,3 steering on ThreadGate checkpoint). Content constraints benefit most from increased goal attention.}
+\label{tab:ir-results}
+\begin{tabular}{lccc}
+\toprule
+\textbf{Category} & $\beta$\,=\,0 & $\beta$\,=\,3 & $\Delta$ \\
+\midrule
+Content    & 61.9\% & 85.7\% & +23.8\,pp \\
+Position   & 66.7\% & 73.3\% & +6.7\,pp \\
+Count      & 100\%  & 100\%  & 0 \\
+Format     & 100\%  & 100\%  & 0 \\
+\midrule
+\textbf{Overall} & 75.9\% & 87.0\% & +11.1\,pp \\
+\bottomrule
+\end{tabular}
+\end{table}
+
+\section{Long-Conversation AR Evaluation}\label{sec:appendix-n5}
+
+The main results (Table~\ref{tab:five-way}) report AR GAR from $N$\,=\,50 held-out conversations with a mean of 3.6 user turns. Table~\ref{tab:n5-ar} presents complementary results on $N$\,=\,5 conversations with 10 turns each, testing whether the observed patterns generalize beyond the training distribution's conversation length.
+
+\paragraph{Gating advantage vanishes at length.} In these longer dialogues, the gating advantage observed in shorter conversations vanishes: all fine-tuned variants collapse to AR GAR-ours of 0.015--0.025, compared to 0.030--0.064 in the shorter evaluation. ThreadGate's advantage over LoRA-only shrinks from 1.7$\times$ (0.064 vs.\ 0.037 in the $N$\,=\,50 evaluation) to 0.64$\times$ (0.016 vs.\ 0.025), actually reversing the ordering. This reversal is not statistically robust given the small sample ($N$\,=\,5) but directionally suggests that architectural modifications provide diminishing returns as conversation length increases and exposure bias accumulates.
+
+\paragraph{Convergence to base.} By turn~10, all fine-tuned variants converge to within 2$\times$ of the base model's GAR, compared to 3.4$\times$ at turn~1 in the shorter evaluation. This convergence is consistent with exposure bias compounding multiplicatively over turns: each model-generated turn introduces additional distributional drift from the teacher-forced training regime, and by turn~10 the accumulated drift overwhelms any gating or LoRA signal, leaving only the base model's intrinsic attention patterns.
+
+\paragraph{Caveats.} The $N$\,=\,5 sample size limits statistical power, and the 10-turn conversations may differ systematically from the 3--5 turn training distribution in ways beyond length (e.g., topic complexity, user engagement patterns). We present these results as directional evidence rather than definitive conclusions.
+
+\begin{table}[t]
+\centering\small
+\caption{AR GAR-ours on $N$\,=\,5 ten-turn conversations. The gating advantage observed in Table~\ref{tab:five-way} ($N$\,=\,50, mean 3.6 turns) diminishes with conversation length.}
+\label{tab:n5-ar}
+\begin{tabular}{lcc}
 \toprule
- & \textbf{Loss Family} & \textbf{Status} & \textbf{GAR} & \textbf{PPL} \\
+\textbf{Configuration} & \textbf{AR GAR-O} & \textbf{$\Delta$ vs.\ Table~\ref{tab:five-way}} \\
 \midrule
-v1  & Cumulative            & \texttimes~GAR loss $\to$ 0     & ---  & ---  \\
-v2  & Cumulative + $\varepsilon$ & \texttimes~same trajectory & ---  & ---  \\
-v3  & Maximize ($\lambda$=2)  & \texttimes~gate frozen        & ---  & ---  \\
-v3b & Maximize ($\lambda$=10) & \texttimes~identity collapse   & ---  & ---  \\
-v5  & Maximize ($\lambda$=1)  & \texttimes~identity collapse   & ---  & ---  \\
-v6  & Smooth saturation       & \texttimes~identity collapse   & ---  & ---  \\
-v7  & MSE + gate div          & \checkmark~converged           & 0.50 & 2.78 \\
+Base & 0.012 & $-$0.007 \\
+\midrule
+ThreadGate & 0.016 & $-$0.048 \\
+\;+\,PCGrad & 0.015 & $-$0.015 \\
+Uniform Gate & 0.015 & $-$0.018 \\
+LoRA-only & 0.025 & $-$0.012 \\
+\bottomrule
+\end{tabular}
+\end{table}
+
+\section{Statistical Test Details}\label{sec:appendix-stats}
+
+All statistical tests reported in the main text use non-parametric methods due to the non-normal, heavy-tailed distribution of per-conversation GAR values. Table~\ref{tab:stat-tests} consolidates the full results.
+
+\paragraph{Wilcoxon signed-rank tests.} We use paired Wilcoxon signed-rank tests for all pairwise configuration comparisons under AR evaluation, treating each conversation as a paired observation. The TG vs.\ LoRA-only comparison ($p$\,=\,0.004, $r$\,=\,0.454) confirms that turn-conditioned gating provides a statistically significant but modest improvement. The TG vs.\ +PCGrad comparison ($p$\,=\,0.002) shows that resolving gradient conflict is actively harmful. Gate turn conditioning uses an unpaired Wilcoxon test across 28 layers.
+
+\paragraph{Bootstrap confidence intervals.} The 95\% CIs in Table~\ref{tab:five-way} are computed via 10,000 bootstrap resamples of per-conversation mid-turn GAR averages (turns 2--$T$), using the percentile method.
+
+\paragraph{Effect sizes.} We report rank-biserial correlation $r = Z / \sqrt{N}$ as the effect size for Wilcoxon tests, where $Z$ is the standardized test statistic and $N$ is the number of observations. By standard conventions: $r < 0.3$ is small, $0.3 \leq r < 0.5$ is medium, and $r \geq 0.5$ is large. The TG vs.\ LoRA-only effect ($r$\,=\,0.454) is medium, and TG vs.\ Base ($r$\,=\,0.802) is large.
+
+\paragraph{Multiple comparisons.} We report uncorrected $p$-values throughout, as our comparisons are hypothesis-driven (each tests a specific causal exclusion) rather than exploratory. Applying Bonferroni correction to the 4 primary AR comparisons would adjust the significance threshold to 0.0125; all reported significant results ($p \leq 0.004$) survive this correction.
+
+\begin{table}[t]
+\centering\small
+\caption{Consolidated statistical tests. All AR comparisons use $N$\,=\,50 conversations (39 with $\geq$3 turns); gate conditioning uses 28 layers.}
+\label{tab:stat-tests}
+\begin{tabular}{llcc}
+\toprule
+\textbf{Comparison} & \textbf{Test} & $p$ & $r$ \\
+\midrule
+\multicolumn{4}{l}{\emph{AR GAR-ours ($\beta$\,=\,0)}} \\
+TG vs.\ Base & Wilcoxon & $<$0.001 & 0.802 \\
+TG vs.\ LoRA-only & Wilcoxon & 0.004 & 0.454 \\
+TG vs.\ +PCGrad & Wilcoxon & 0.002 & --- \\
+SS vs.\ TG & Wilcoxon & $<$0.001 & 0.869 \\
+\midrule
+\multicolumn{4}{l}{\emph{Gate conditioning (28 layers)}} \\
+Turn 1 vs.\ Turn 21 & Wilcoxon & $3.7\!\times\!10^{-8}$ & 0.975 \\
+\midrule
+\multicolumn{4}{l}{\emph{Instruction retention}} \\
+$\beta$\,=\,0 vs.\ $\beta$\,=\,3 & McNemar & 0.077 & --- \\
+GAR--compliance & Pearson & 0.007 & 0.200 \\
 \bottomrule
 \end{tabular}
 \end{table}
+
+\section{Llama-3.1-8B Complete Results}\label{sec:appendix-llama}
+
+Table~\ref{tab:llama-full} presents the complete Llama-3.1-8B-Instruct results, complementing the summary in \S\ref{subsec:cross-model}. Three configurations were trained (Base, ThreadGate, LoRA-only) using the same training pipeline as Qwen-2.5-7B (8K UltraChat, 3 epochs, LoRA rank 16). Training required 7.0--7.3 hours per variant on the same GPU.
+
+\paragraph{Teacher-forced evaluation.} TF GAR-ours is 0.484 (TG) and 0.481 (LoRA-only), confirming that gating provides zero benefit under teacher forcing on Llama, consistent with the Qwen results (0.50 vs.\ 0.50).
+
+\paragraph{Autoregressive evaluation.} AR evaluation uses $N$\,=\,20 mid-turn conversations (turns 3--$T$, excluding the first two turns to avoid initialization effects). The AR GAR distribution is heavy-tailed: the coefficient of variation exceeds 100\% for ThreadGate (mean 0.043, std 0.100), and 5\% of turn-level measurements exhibit sporadic attention spikes (GAR $\geq$ 0.4). We therefore report both mean and median.
+
+\paragraph{Gate profile.} Llama's gate profile differs qualitatively from Qwen's: Qwen shows minimum attenuation at early layers (L1\,=\,0.793, L5\,=\,0.797), while Llama shows a V-shaped valley at mid-to-late layers (L25\,=\,0.719, L24\,=\,0.809). Despite this architectural difference, both models converge toward identity under NTP pressure, and the TF-AR gap is comparable (27$\times$ by median for Llama vs.\ 8--17$\times$ for Qwen).
+
+\begin{table}[t]
+\centering\small
Shell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f9cce00b-a83c-4342-9397-3840d0729f73",
  "isSidechain": false,
  "promptId": "8d8464e4-1523-464c-8d63-5cd7db13bd3f",
  "type": "user",
  "uuid": "9a2cdc76-f33e-4a09-b81b-cdbb88cc8ffd",
  "toolUseResult": {
    "stdout": "diff --git a/paper/sections/appendix.tex b/paper/sections/appendix.tex\nindex 8f1bb3d..8f22842 100644\n--- a/paper/sections/appendix.tex\n+++ b/paper/sections/appendix.tex\n@@ -1,26 +1,850 @@\n-\\section{Training Hyperparameters}\\label{sec:appendix-hyper}\n+\\section{Training Configuration}\\label{sec:appendix-hyper}\n \n-All fine-tuned variants share the following configuration: Qwen-2.5-7B-Instruct base model, LoRA rank 16 ($\\alpha$=32) on \\texttt{q\\_proj} and \\texttt{v\\_proj}, AdamW optimizer (lr = $2 \\times 10^{-4}$, $\\beta_1$=0.9, $\\beta_2$=0.999), batch size 1 with gradient accumulation 8, 3 epochs over 8K UltraChat conversations, maximum sequence length 2048, seed 42. ThreadGate gates use a 10$\\times$ learning rate multiplier and initial bias 1.5 ($\\sigma(1.5) \\approx 0.82$).\n+Table~\\ref{tab:hyperparams} lists the full training configuration shared across all fine-tuned variants. ThreadGate gate parameters receive a $10\\times$ learning rate multiplier and are initialized with bias 1.5 ($\\sigma(1.5) \\approx 0.82$); the gate MLP adds ${\\sim}$57K parameters per variant ($<$0.001\\% of 7B). The scheduled sampling variant (v8b) linearly increases the model-generated context ratio from 0 to 0.3 over 3 epochs (29.7--37.1\\% effective usage due to per-sample Bernoulli sampling). All experiments were conducted on a single NVIDIA RTX PRO 6000 Blackwell Server Edition GPU (96\\,GB VRAM), requiring 6--8 hours per variant.\n+\n+\\begin{table}[t]\n+\\centering\\small\n+\\caption{Training hyperparameters for all fine-tuned variants. Entries marked $\\dagger$ apply only to ThreadGate and its ablations.}\n+\\label{tab:hyperparams}\n+\\begin{tabular}{l@{\\hspace{8pt}}l}\n+\\toprule\n+\\textbf{Parameter} & \\textbf{Value} \\\\\n+\\midrule\n+Base model & Qwen-2.5-7B-Instruct \\\\\n+LoRA rank / $\\alpha$ & 16 / 32 \\\\\n+LoRA targets & \\texttt{q\\_proj}, \\texttt{v\\_proj} \\\\\n+Optimizer & AdamW ($\\beta_1$\\!=\\!0.9, $\\beta_2$\\!=\\!0.999) \\\\\n+Learning rate & $2 \\times 10^{-4}$ \\\\\n+Gate LR mult.$^\\dagger$ & $10\\times$ \\\\\n+Batch / grad accum & 1 / 8 (eff.\\ 8) \\\\\n+Epochs & 3 \\\\\n+Max seq length & 2048 \\\\\n+Training data & 8K UltraChat convs \\\\\n+Seed & 42 (+123 for TG, SS) \\\\\n+$\\lambda_\\text{GAR}$/$\\lambda_\\text{div}$ & 1.0 / 1.0 \\\\\n+GAR target $\\tau$ & 0.5 \\\\\n+Gate init bias$^\\dagger$ & 1.5 ($\\sigma\\!\\approx\\!0.82$) \\\\\n+Gate hidden dim$^\\dagger$ & 64 \\\\\n+Turn embed dim$^\\dagger$ & 16 \\\\\n+GPU & RTX PRO 6000 (96\\,GB) \\\\\n+Training time & 6--8 h / variant \\\\\n+\\bottomrule\n+\\end{tabular}\n+\\end{table}\n \n \\section{Loss Formulation Search}\\label{sec:appendix-loss}\n \n-Table~\\ref{tab:loss-iterations} summarizes the seven loss configurations explored before arriving at the final MSE + gate diversity formulation (\\S\\ref{sec:loss}). Configurations v1--v6 span three alternative loss families; none converged during training.\n+The final MSE + gate diversity loss (\\S\\ref{sec:loss}) emerged from seven iterations spanning four loss families. Table~\\ref{tab:loss-iterations} summarizes the progression. The search was motivated by a consistent failure mode: naive formulations either collapse to trivial solutions (cumulative losses) or drive gates toward identity (maximize-family losses). We describe each family below.\n \n-\\begin{table}[h]\n-\\centering\\small\n-\\caption{Loss formulation iterations on Qwen-2.5-7B-Instruct. GAR-ours (teacher-forced) and PPL are reported only for the converged configuration.}\n+\\paragraph{Cumulative losses (v1--v2).} These losses accumulate GAR contributions across layers, rewarding monotonically increasing attention. v1 collapsed because once the cumulative GAR exceeded the threshold, the loss gradient vanished and gates froze. v2 added an $\\varepsilon$-stabilization term to the cumulative product, but numerical instability from the product of 28 per-layer terms dominated, and training followed the same trajectory.\n+\n+\\paragraph{Maximize losses (v3--v5).} These losses directly maximize mean GAR ($-\\text{mean}(\\text{GAR})$). The unbounded objective rewards full pass-through ($g \\to 1.0$), collapsing gate diversity (std $<$ 0.025). At $\\lambda$=2 (v3), gates froze within 100 steps; at $\\lambda$=10 (v3b), convergence to identity accelerated; at $\\lambda$=1 (v5), rebalancing delayed but did not prevent the same degenerate solution.\n+\n+\\paragraph{Smooth saturation (v6).} This bounded the reward using a saturating function, intended to prevent the unbounded growth of maximize losses. In practice, the loss landscape remained monotonic in $g$, and training followed the same terminal trajectory as the maximize family, only more slowly.\n+\n+\\paragraph{MSE + gate diversity (v7).} The MSE formulation provides bidirectional pressure: GAR above $\\tau$ incurs the same penalty as GAR below $\\tau$, preventing the runaway optimization of maximize losses. The gate diversity regularizer ($\\mathcal{L}_\\text{div}$) enforces a minimum standard deviation across per-layer gate values, preventing all gates from collapsing to a uniform value. This combination is the only one that achieved stable convergence (GAR-ours = 0.50, PPL = 2.78).\n+\n+\\begin{table*}[t]\n+\\centering\\footnotesize\n+\\caption{Loss formulation iterations on Qwen-2.5-7B-Instruct. GAR-ours (teacher-forced) and PPL are reported only for the converged configuration (v7).}\n \\label{tab:loss-iterations}\n-\\begin{tabular}{l l l c c}\n+\\begin{tabular}{l l l p{5.8cm} c c}\n+\\toprule\n+ & \\textbf{Loss Family} & \\textbf{Status} & \\textbf{Failure Mechanism} & \\textbf{GAR} & \\textbf{PPL} \\\\\n+\\midrule\n+v1  & Cumulative            & \\texttimes~GAR loss $\\to$ 0     & GAR loss collapses to zero once threshold is reached; gate gradients vanish at equilibrium & ---  & ---  \\\\\n+v2  & Cumulative + $\\varepsilon$ & \\texttimes~same trajectory & Numerical instability from cumulative product; $\\varepsilon$-stabilization insufficient & ---  & ---  \\\\\n+v3  & Maximize ($\\lambda$=2)  & \\texttimes~gate frozen        & Unbounded reward drives gates toward identity (all-pass); no layer selectivity & ---  & ---  \\\\\n+v3b & Maximize ($\\lambda$=10) & \\texttimes~identity collapse   & Higher $\\lambda$ accelerates convergence to same degenerate identity solution & ---  & ---  \\\\\n+v5  & Maximize ($\\lambda$=1)  & \\texttimes~identity collapse   & Rebalancing delays but does not prevent identity collapse & ---  & ---  \\\\\n+v6  & Smooth saturation       & \\texttimes~identity collapse   & Monotonic reward identical to maximize in practice; boundedness slows but does not alter terminal trajectory & ---  & ---  \\\\\n+v7  & MSE + gate div          & \\checkmark~\\textbf{converged}  & \\textbf{Bidirectional penalty prevents identity collapse; gate diversity regularizer enforces layer selectivity} & 0.50 & 2.78 \\\\\n+\\bottomrule\n+\\end{tabular}\n+\\end{table*}\n+\n+\\section{Instruction Retention Details}\\label{sec:appendix-ir}\n+\n+To evaluate whether GAR improvements translate to downstream task performance, we test instruction retention across 18 system-prompt constraint types using the ThreadGate checkpoint with $\\beta$\\,=\\,3 steering on $N$\\,=\\,200 held-out conversations. Each constraint type requires the model to follow a specific instruction embedded in the system prompt (e.g., ``always respond in bullet points'', ``never use the word X'', ``include a summary at the end''). This evaluation bridges the gap between our attention-level metric (GAR) and observable model behavior.\n+\n+\\paragraph{Evaluation protocol.} For each conversation, we inject a constraint into the system prompt and evaluate compliance across all assistant turns. A turn is compliant if it satisfies the constraint according to rule-based checkers (for format, count, and position constraints) or GPT-4-based evaluation (for content constraints, which require semantic judgment). We use the same 18 constraint types across all conversations, yielding $N$\\,=\\,54 paired evaluations (18 types $\\times$ 3 conversations per type) for the McNemar analysis.\n+\n+\\paragraph{Per-category results.} Table~\\ref{tab:ir-results} reports per-category compliance rates. Content constraints---which require attending to and recalling specific system-prompt instructions across turns---show the largest improvement (+23.8\\,pp), consistent with GAR measuring attention to goal tokens. This category includes constraints like ``mention X in every response'' and ``always reference the original topic,'' which require sustained attention to the system prompt. Position constraints (e.g., ``start each response with Y'') show a modest improvement (+6.7\\,pp), as they partially depend on goal-token attention. Format (e.g., ``use bullet points'') and count constraints (e.g., ``exactly 3 sentences'') show no change, consistent with these being procedural patterns that are cached in the model's generation routine rather than requiring ongoing attention to the system prompt.\n+\n+\\paragraph{Correlation analysis.} The GAR-compliance correlation ($r$\\,=\\,0.200, $p$\\,=\\,0.007) is statistically significant but modest, suggesting that attention to goal tokens is one of several factors in instruction compliance. Other factors likely include the model's procedural memory for format constraints, the specificity of the constraint (vague constraints are harder regardless of attention), and the interaction between constraint type and conversation topic. McNemar's test ($p$\\,=\\,0.077) is marginally significant for the overall compliance improvement, reflecting the small sample size (18 constraint types). These results are exploratory and pending multi-model confirmation.\n+\n+Figure~\\ref{fig:ir-bar} visualizes the per-category breakdown.\n+\n+\\begin{figure}[t]\n+  \\centering\n+  \\includegraphics[width=\\columnwidth]{fig_instruction_retention.pdf}\n+  \\caption{Instruction retention by constraint category under $\\beta$\\,=\\,3 steering. Content constraints benefit most (+23.8\\,pp); format and count constraints are unaffected.}\n+  \\label{fig:ir-bar}\n+\\end{figure}\n+\n+\\FloatBarrier\n+\n+\\begin{table}[t]\n+\\centering\\small\n+\\caption{Instruction retention by constraint category ($\\beta$\\,=\\,3 steering on ThreadGate checkpoint). Content constraints benefit most from increased goal attention.}\n+\\label{tab:ir-results}\n+\\begin{tabular}{lccc}\n+\\toprule\n+\\textbf{Category} & $\\beta$\\,=\\,0 & $\\beta$\\,=\\,3 & $\\Delta$ \\\\\n+\\midrule\n+Content    & 61.9\\% & 85.7\\% & +23.8\\,pp \\\\\n+Position   & 66.7\\% & 73.3\\% & +6.7\\,pp \\\\\n+Count      & 100\\%  & 100\\%  & 0 \\\\\n+Format     & 100\\%  & 100\\%  & 0 \\\\\n+\\midrule\n+\\textbf{Overall} & 75.9\\% & 87.0\\% & +11.1\\,pp \\\\\n+\\bottomrule\n+\\end{tabular}\n+\\end{table}\n+\n+\\section{Long-Conversation AR Evaluation}\\label{sec:appendix-n5}\n+\n+The main results (Table~\\ref{tab:five-way}) report AR GAR from $N$\\,=\\,50 held-out conversations with a mean of 3.6 user turns. Table~\\ref{tab:n5-ar} presents complementary results on $N$\\,=\\,5 conversations with 10 turns each, testing whether the observed patterns generalize beyond the training distribution's conversation length.\n+\n+\\paragraph{Gating advantage vanishes at length.} In these longer dialogues, the gating advantage observed in shorter conversations vanishes: all fine-tuned variants collapse to AR GAR-ours of 0.015--0.025, compared to 0.030--0.064 in the shorter evaluation. ThreadGate's advantage over LoRA-only shrinks from 1.7$\\times$ (0.064 vs.\\ 0.037 in the $N$\\,=\\,50 evaluation) to 0.64$\\times$ (0.016 vs.\\ 0.025), actually reversing the ordering. This reversal is not statistically robust given the small sample ($N$\\,=\\,5) but directionally suggests that architectural modifications provide diminishing returns as conversation length increases and exposure bias accumulates.\n+\n+\\paragraph{Convergence to base.} By turn~10, all fine-tuned variants converge to within 2$\\times$ of the base model's GAR, compared to 3.4$\\times$ at turn~1 in the shorter evaluation. This convergence is consistent with exposure bias compounding multiplicatively over turns: each model-generated turn introduces additional distributional drift from the teacher-forced training regime, and by turn~10 the accumulated drift overwhelms any gating or LoRA signal, leaving only the base model's intrinsic attention patterns.\n+\n+\\paragraph{Caveats.} The $N$\\,=\\,5 sample size limits statistical power, and the 10-turn conversations may differ systematically from the 3--5 turn training distribution in ways beyond length (e.g., topic complexity, user engagement patterns). We present these results as directional evidence rather than definitive conclusions.\n+\n+\\begin{table}[t]\n+\\centering\\small\n+\\caption{AR GAR-ours on $N$\\,=\\,5 ten-turn conversations. The gating advantage observed in Table~\\ref{tab:five-way} ($N$\\,=\\,50, mean 3.6 turns) diminishes with conversation length.}\n+\\label{tab:n5-ar}\n+\\begin{tabular}{lcc}\n \\toprule\n- & \\textbf{Loss Family} & \\textbf{Status} & \\textbf{GAR} & \\textbf{PPL} \\\\\n+\\textbf{Configuration} & \\textbf{AR GAR-O} & \\textbf{$\\Delta$ vs.\\ Table~\\ref{tab:five-way}} \\\\\n \\midrule\n-v1  & Cumulative            & \\texttimes~GAR loss $\\to$ 0     & ---  & ---  \\\\\n-v2  & Cumulative + $\\varepsilon$ & \\texttimes~same trajectory & ---  & ---  \\\\\n-v3  & Maximize ($\\lambda$=2)  & \\texttimes~gate frozen        & ---  & ---  \\\\\n-v3b & Maximize ($\\lambda$=10) & \\texttimes~identity collapse   & ---  & ---  \\\\\n-v5  & Maximize ($\\lambda$=1)  & \\texttimes~identity collapse   & ---  & ---  \\\\\n-v6  & Smooth saturation       & \\texttimes~identity collapse   & ---  & ---  \\\\\n-v7  & MSE + gate div          & \\checkmark~converged           & 0.50 & 2.78 \\\\\n+Base & 0.012 & $-$0.007 \\\\\n+\\midrule\n+ThreadGate & 0.016 & $-$0.048 \\\\\n+\\;+\\,PCGrad & 0.015 & $-$0.015 \\\\\n+Uniform Gate & 0.015 & $-$0.018 \\\\\n+LoRA-only & 0.025 & $-$0.012 \\\\\n+\\bottomrule\n+\\end{tabular}\n+\\end{table}\n+\n+\\section{Statistical Test Details}\\label{sec:appendix-stats}\n+\n+All statistical tests reported in the main text use non-parametric methods due to the non-normal, heavy-tailed distribution of per-conversation GAR values. Table~\\ref{tab:stat-tests} consolidates the full results.\n+\n+\\paragraph{Wilcoxon signed-rank tests.} We use paired Wilcoxon signed-rank tests for all pairwise configuration comparisons under AR evaluation, treating each conversation as a paired observation. The TG vs.\\ LoRA-only comparison ($p$\\,=\\,0.004, $r$\\,=\\,0.454) confirms that turn-conditioned gating provides a statistically significant but modest improvement. The TG vs.\\ +PCGrad comparison ($p$\\,=\\,0.002) shows that resolving gradient conflict is actively harmful. Gate turn conditioning uses an unpaired Wilcoxon test across 28 layers.\n+\n+\\paragraph{Bootstrap confidence intervals.} The 95\\% CIs in Table~\\ref{tab:five-way} are computed via 10,000 bootstrap resamples of per-conversation mid-turn GAR averages (turns 2--$T$), using the percentile method.\n+\n+\\paragraph{Effect sizes.} We report rank-biserial correlation $r = Z / \\sqrt{N}$ as the effect size for Wilcoxon tests, where $Z$ is the standardized test statistic and $N$ is the number of observations. By standard conventions: $r < 0.3$ is small, $0.3 \\leq r < 0.5$ is medium, and $r \\geq 0.5$ is large. The TG vs.\\ LoRA-only effect ($r$\\,=\\,0.454) is medium, and TG vs.\\ Base ($r$\\,=\\,0.802) is large.\n+\n+\\paragraph{Multiple comparisons.} We report uncorrected $p$-values throughout, as our comparisons are hypothesis-driven (each tests a specific causal exclusion) rather than exploratory. Applying Bonferroni correction to the 4 primary AR comparisons would adjust the significance threshold to 0.0125; all reported significant results ($p \\leq 0.004$) survive this correction.\n+\n+\\begin{table}[t]\n+\\centering\\small\n+\\caption{Consolidated statistical tests. All AR comparisons use $N$\\,=\\,50 conversations (39 with $\\geq$3 turns); gate conditioning uses 28 layers.}\n+\\label{tab:stat-tests}\n+\\begin{tabular}{llcc}\n+\\toprule\n+\\textbf{Comparison} & \\textbf{Test} & $p$ & $r$ \\\\\n+\\midrule\n+\\multicolumn{4}{l}{\\emph{AR GAR-ours ($\\beta$\\,=\\,0)}} \\\\\n+TG vs.\\ Base & Wilcoxon & $<$0.001 & 0.802 \\\\\n+TG vs.\\ LoRA-only & Wilcoxon & 0.004 & 0.454 \\\\\n+TG vs.\\ +PCGrad & Wilcoxon & 0.002 & --- \\\\\n+SS vs.\\ TG & Wilcoxon & $<$0.001 & 0.869 \\\\\n+\\midrule\n+\\multicolumn{4}{l}{\\emph{Gate conditioning (28 layers)}} \\\\\n+Turn 1 vs.\\ Turn 21 & Wilcoxon & $3.7\\!\\times\\!10^{-8}$ & 0.975 \\\\\n+\\midrule\n+\\multicolumn{4}{l}{\\emph{Instruction retention}} \\\\\n+$\\beta$\\,=\\,0 vs.\\ $\\beta$\\,=\\,3 & McNemar & 0.077 & --- \\\\\n+GAR--compliance & Pearson & 0.007 & 0.200 \\\\\n \\bottomrule\n \\end{tabular}\n \\end{table}\n+\n+\\section{Llama-3.1-8B Complete Results}\\label{sec:appendix-llama}\n+\n+Table~\\ref{tab:llama-full} presents the complete Llama-3.1-8B-Instruct results, complementing the summary in \\S\\ref{subsec:cross-model}. Three configurations were trained (Base, ThreadGate, LoRA-only) using the same training pipeline as Qwen-2.5-7B (8K UltraChat, 3 epochs, LoRA rank 16). Training required 7.0--7.3 hours per variant on the same GPU.\n+\n+\\paragraph{Teacher-forced evaluation.} TF GAR-ours is 0.484 (TG) and 0.481 (LoRA-only), confirming that gating provides zero benefit under teacher forcing on Llama, consistent with the Qwen results (0.50 vs.\\ 0.50).\n+\n+\\paragraph{Autoregressive evaluation.} AR evaluation uses $N$\\,=\\,20 mid-turn conversations (turns 3--$T$, excluding the first two turns to avoid initialization effects). The AR GAR distribution is heavy-tailed: the coefficient of variation exceeds 100\\% for ThreadGate (mean 0.043, std 0.100), and 5\\% of turn-level measurements exhibit sporadic attention spikes (GAR $\\geq$ 0.4). We therefore report both mean and median.\n+\n+\\paragraph{Gate profile.} Llama's gate profile differs qualitatively from Qwen's: Qwen shows minimum attenuation at early layers (L1\\,=\\,0.793, L5\\,=\\,0.797), while Llama shows a V-shaped valley at mid-to-late layers (L25\\,=\\,0.719, L24\\,=\\,0.809). Despite this architectural difference, both models converge toward identity under NTP pressure, and the TF-AR gap is comparable (27$\\times$ by median for Llama vs.\\ 8--17$\\times$ for Qwen).\n+\n+\\begin{table}[t]\n+\\centering\\small",
    "stderr": "\nShell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "f9cce00b-a83c-4342-9397-3840d0729f73",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921",
  "sessionId": "5d779602-0719-4d06-8bf9-fdd84990d5d0",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---


### Runtime record

_source line 121 · 2026-05-25T20:42:28.827Z_

```json
{
  "parentUuid": "9a2cdc76-f33e-4a09-b81b-cdbb88cc8ffd",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "59e345d4-529b-4e89-9253-8485c164c6e2",
  "timestamp": "2026-05-25T20:42:28.827Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921",
  "sessionId": "5d779602-0719-4d06-8bf9-fdd84990d5d0",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---


### Runtime record

_source line 122_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[服务器重启后首条消息] 当前日期: 2026-05-25。服务器刚重启，项目状态可能已更新。在处理审查请求前，**先读取 registry.yaml 和 report.md** 获取最新实验状态，不要依赖对话历史中的状态信息。  **审查请求：** [系统通知 — worker_done:worker_fix_audit_appendix_issues_20260525T203522]: Wor…",
  "leafUuid": "59e345d4-529b-4e89-9253-8485c164c6e2",
  "sessionId": "5d779602-0719-4d06-8bf9-fdd84990d5d0"
}
```

---


### Runtime record

_source line 123_

```json
{
  "type": "ai-title",
  "aiTitle": "Review worker audit appendix tables completion",
  "sessionId": "5d779602-0719-4d06-8bf9-fdd84990d5d0"
}
```

---


### Assistant

_source line 124 · 2026-05-25T20:42:48.222Z_

<details><summary>Logged reasoning block</summary>

```text
The git diff shows a massive expansion of the appendix from a skeletal version to the full version. But this doesn't seem to be a diff specifically from the "fix_audit_appendix_issues" worker - it's the diff between the last 3 commits and the current state, which shows the whole appendix rewrite.

Let me check more specifically what happened. The worker was supposed to fix the two warning-level issues I identified:
1. tab_crossmodel_detail: Qwen SS row mixing single-seed TF with multi-seed AR
2. tab_perseed_tg: Using N=5 old eval protocol


Both tables are unchanged, so the worker didn't actually fix these issues. But the worker completed with status=done, so I need to check if it made changes elsewhere or if there were commits after the one I'm looking at.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "59e345d4-529b-4e89-9253-8485c164c6e2",
  "isSidechain": false,
  "requestId": "req_011CbPwHL52XdWxgWkGgjXgg",
  "type": "assistant",
  "uuid": "b54035ac-89eb-4f71-8dfd-9dfb184d39af",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921",
  "sessionId": "5d779602-0719-4d06-8bf9-fdd84990d5d0",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012absUYQ1bkpMwhytjt57qH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6836,
      "cache_read_input_tokens": 108066,
      "output_tokens": 473,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6836,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 473,
          "cache_read_input_tokens": 108066,
          "cache_creation_input_tokens": 6836,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6836
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

_source line 125 · 2026-05-25T20:42:48.289Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01NFaJrUu5rd3d6ZnvEtHBkS`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating && git log --oneline --all -10",
  "description": "Check all branches for recent commits"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b54035ac-89eb-4f71-8dfd-9dfb184d39af",
  "isSidechain": false,
  "requestId": "req_011CbPwHL52XdWxgWkGgjXgg",
  "type": "assistant",
  "uuid": "cea95b98-7632-4d19-8906-3ced1bea9c34",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921",
  "sessionId": "5d779602-0719-4d06-8bf9-fdd84990d5d0",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012absUYQ1bkpMwhytjt57qH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6836,
      "cache_read_input_tokens": 108066,
      "output_tokens": 473,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6836,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 473,
          "cache_read_input_tokens": 108066,
          "cache_creation_input_tokens": 6836,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6836
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

_source line 126 · 2026-05-25T20:42:48.337Z_

<details><summary>↩ Tool result · `toolu_01NFaJrUu5rd3d6ZnvEtHBkS`</summary>

```text
98eff19 [paper] Fix cross-model gap comparison + add median justification
73a7969 [paper] Write Llama LoRA-only cross-model results (C5 completion)
74bb496 [paper] Add Li et al. 2024 (direct competitor) + strengthen exposure bias citations
2e58ab1 [paper] Fix 2 author errors + 3 bib warnings from citation audit
c93a515 [paper] Multi-seed v7 TG data + v8b SS training schedule observation
c4dc400 [paper] Add β=5 PPL tradeoff to Discussion steering paragraph
66c3ef4 [paper] Fix 5 paper-registry numerical inconsistencies (N=5 steering data)
e4522a3 [paper] Fix instruction retention params + update Limitations + compress Abstract
52e5da3 [paper] Llama cross-model confirmed + §6 mechanism expansion + instruction retention
760d758 [paper] Llama-3.1-8B cross-model GAR decay diagnostic (§6.5 preliminary evidence)
Shell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cea95b98-7632-4d19-8906-3ced1bea9c34",
  "isSidechain": false,
  "promptId": "8d8464e4-1523-464c-8d63-5cd7db13bd3f",
  "type": "user",
  "uuid": "ebcd40b4-eaa6-429e-a4b7-94054e8bb654",
  "toolUseResult": {
    "stdout": "98eff19 [paper] Fix cross-model gap comparison + add median justification\n73a7969 [paper] Write Llama LoRA-only cross-model results (C5 completion)\n74bb496 [paper] Add Li et al. 2024 (direct competitor) + strengthen exposure bias citations\n2e58ab1 [paper] Fix 2 author errors + 3 bib warnings from citation audit\nc93a515 [paper] Multi-seed v7 TG data + v8b SS training schedule observation\nc4dc400 [paper] Add β=5 PPL tradeoff to Discussion steering paragraph\n66c3ef4 [paper] Fix 5 paper-registry numerical inconsistencies (N=5 steering data)\ne4522a3 [paper] Fix instruction retention params + update Limitations + compress Abstract\n52e5da3 [paper] Llama cross-model confirmed + §6 mechanism expansion + instruction retention\n760d758 [paper] Llama-3.1-8B cross-model GAR decay diagnostic (§6.5 preliminary evidence)",
    "stderr": "\nShell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "cea95b98-7632-4d19-8906-3ced1bea9c34",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921",
  "sessionId": "5d779602-0719-4d06-8bf9-fdd84990d5d0",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---


### Tool result

_source line 127 · 2026-05-25T20:42:49.264Z_

<details><summary>↩ Tool result · `toolu_01GiW5XtgnSFr4LiEem2ZSVE`</summary>

```text
diff --git a/paper/sections/appendix.tex b/paper/sections/appendix.tex
index 8f1bb3d..8f22842 100644
--- a/paper/sections/appendix.tex
+++ b/paper/sections/appendix.tex
@@ -1,26 +1,850 @@
-\section{Training Hyperparameters}\label{sec:appendix-hyper}
+\section{Training Configuration}\label{sec:appendix-hyper}
 
-All fine-tuned variants share the following configuration: Qwen-2.5-7B-Instruct base model, LoRA rank 16 ($\alpha$=32) on \texttt{q\_proj} and \texttt{v\_proj}, AdamW optimizer (lr = $2 \times 10^{-4}$, $\beta_1$=0.9, $\beta_2$=0.999), batch size 1 with gradient accumulation 8, 3 epochs over 8K UltraChat conversations, maximum sequence length 2048, seed 42. ThreadGate gates use a 10$\times$ learning rate multiplier and initial bias 1.5 ($\sigma(1.5) \approx 0.82$).
+Table~\ref{tab:hyperparams} lists the full training configuration shared across all fine-tuned variants. ThreadGate gate parameters receive a $10\times$ learning rate multiplier and are initialized with bias 1.5 ($\sigma(1.5) \approx 0.82$); the gate MLP adds ${\sim}$57K parameters per variant ($<$0.001\% of 7B). The scheduled sampling variant (v8b) linearly increases the model-generated context ratio from 0 to 0.3 over 3 epochs (29.7--37.1\% effective usage due to per-sample Bernoulli sampling). All experiments were conducted on a single NVIDIA RTX PRO 6000 Blackwell Server Edition GPU (96\,GB VRAM), requiring 6--8 hours per variant.
+
+\begin{table}[t]
+\centering\small
+\caption{Training hyperparameters for all fine-tuned variants. Entries marked $\dagger$ apply only to ThreadGate and its ablations.}
+\label{tab:hyperparams}
+\begin{tabular}{l@{\hspace{8pt}}l}
+\toprule
+\textbf{Parameter} & \textbf{Value} \\
+\midrule
+Base model & Qwen-2.5-7B-Instruct \\
+LoRA rank / $\alpha$ & 16 / 32 \\
+LoRA targets & \texttt{q\_proj}, \texttt{v\_proj} \\
+Optimizer & AdamW ($\beta_1$\!=\!0.9, $\beta_2$\!=\!0.999) \\
+Learning rate & $2 \times 10^{-4}$ \\
+Gate LR mult.$^\dagger$ & $10\times$ \\
+Batch / grad accum & 1 / 8 (eff.\ 8) \\
+Epochs & 3 \\
+Max seq length & 2048 \\
+Training data & 8K UltraChat convs \\
+Seed & 42 (+123 for TG, SS) \\
+$\lambda_\text{GAR}$/$\lambda_\text{div}$ & 1.0 / 1.0 \\
+GAR target $\tau$ & 0.5 \\
+Gate init bias$^\dagger$ & 1.5 ($\sigma\!\approx\!0.82$) \\
+Gate hidden dim$^\dagger$ & 64 \\
+Turn embed dim$^\dagger$ & 16 \\
+GPU & RTX PRO 6000 (96\,GB) \\
+Training time & 6--8 h / variant \\
+\bottomrule
+\end{tabular}
+\end{table}
 
 \section{Loss Formulation Search}\label{sec:appendix-loss}
 
-Table~\ref{tab:loss-iterations} summarizes the seven loss configurations explored before arriving at the final MSE + gate diversity formulation (\S\ref{sec:loss}). Configurations v1--v6 span three alternative loss families; none converged during training.
+The final MSE + gate diversity loss (\S\ref{sec:loss}) emerged from seven iterations spanning four loss families. Table~\ref{tab:loss-iterations} summarizes the progression. The search was motivated by a consistent failure mode: naive formulations either collapse to trivial solutions (cumulative losses) or drive gates toward identity (maximize-family losses). We describe each family below.
 
-\begin{table}[h]
-\centering\small
-\caption{Loss formulation iterations on Qwen-2.5-7B-Instruct. GAR-ours (teacher-forced) and PPL are reported only for the converged configuration.}
+\paragraph{Cumulative losses (v1--v2).} These losses accumulate GAR contributions across layers, rewarding monotonically increasing attention. v1 collapsed because once the cumulative GAR exceeded the threshold, the loss gradient vanished and gates froze. v2 added an $\varepsilon$-stabilization term to the cumulative product, but numerical instability from the product of 28 per-layer terms dominated, and training followed the same trajectory.
+
+\paragraph{Maximize losses (v3--v5).} These losses directly maximize mean GAR ($-\text{mean}(\text{GAR})$). The unbounded objective rewards full pass-through ($g \to 1.0$), collapsing gate diversity (std $<$ 0.025). At $\lambda$=2 (v3), gates froze within 100 steps; at $\lambda$=10 (v3b), convergence to identity accelerated; at $\lambda$=1 (v5), rebalancing delayed but did not prevent the same degenerate solution.
+
+\paragraph{Smooth saturation (v6).} This bounded the reward using a saturating function, intended to prevent the unbounded growth of maximize losses. In practice, the loss landscape remained monotonic in $g$, and training followed the same terminal trajectory as the maximize family, only more slowly.
+
+\paragraph{MSE + gate diversity (v7).} The MSE formulation provides bidirectional pressure: GAR above $\tau$ incurs the same penalty as GAR below $\tau$, preventing the runaway optimization of maximize losses. The gate diversity regularizer ($\mathcal{L}_\text{div}$) enforces a minimum standard deviation across per-layer gate values, preventing all gates from collapsing to a uniform value. This combination is the only one that achieved stable convergence (GAR-ours = 0.50, PPL = 2.78).
+
+\begin{table*}[t]
+\centering\footnotesize
+\caption{Loss formulation iterations on Qwen-2.5-7B-Instruct. GAR-ours (teacher-forced) and PPL are reported only for the converged configuration (v7).}
 \label{tab:loss-iterations}
-\begin{tabular}{l l l c c}
+\begin{tabular}{l l l p{5.8cm} c c}
+\toprule
+ & \textbf{Loss Family} & \textbf{Status} & \textbf{Failure Mechanism} & \textbf{GAR} & \textbf{PPL} \\
+\midrule
+v1  & Cumulative            & \texttimes~GAR loss $\to$ 0     & GAR loss collapses to zero once threshold is reached; gate gradients vanish at equilibrium & ---  & ---  \\
+v2  & Cumulative + $\varepsilon$ & \texttimes~same trajectory & Numerical instability from cumulative product; $\varepsilon$-stabilization insufficient & ---  & ---  \\
+v3  & Maximize ($\lambda$=2)  & \texttimes~gate frozen        & Unbounded reward drives gates toward identity (all-pass); no layer selectivity & ---  & ---  \\
+v3b & Maximize ($\lambda$=10) & \texttimes~identity collapse   & Higher $\lambda$ accelerates convergence to same degenerate identity solution & ---  & ---  \\
+v5  & Maximize ($\lambda$=1)  & \texttimes~identity collapse   & Rebalancing delays but does not prevent identity collapse & ---  & ---  \\
+v6  & Smooth saturation       & \texttimes~identity collapse   & Monotonic reward identical to maximize in practice; boundedness slows but does not alter terminal trajectory & ---  & ---  \\
+v7  & MSE + gate div          & \checkmark~\textbf{converged}  & \textbf{Bidirectional penalty prevents identity collapse; gate diversity regularizer enforces layer selectivity} & 0.50 & 2.78 \\
+\bottomrule
+\end{tabular}
+\end{table*}
+
+\section{Instruction Retention Details}\label{sec:appendix-ir}
+
+To evaluate whether GAR improvements translate to downstream task performance, we test instruction retention across 18 system-prompt constraint types using the ThreadGate checkpoint with $\beta$\,=\,3 steering on $N$\,=\,200 held-out conversations. Each constraint type requires the model to follow a specific instruction embedded in the system prompt (e.g., ``always respond in bullet points'', ``never use the word X'', ``include a summary at the end''). This evaluation bridges the gap between our attention-level metric (GAR) and observable model behavior.
+
+\paragraph{Evaluation protocol.} For each conversation, we inject a constraint into the system prompt and evaluate compliance across all assistant turns. A turn is compliant if it satisfies the constraint according to rule-based checkers (for format, count, and position constraints) or GPT-4-based evaluation (for content constraints, which require semantic judgment). We use the same 18 constraint types across all conversations, yielding $N$\,=\,54 paired evaluations (18 types $\times$ 3 conversations per type) for the McNemar analysis.
+
+\paragraph{Per-category results.} Table~\ref{tab:ir-results} reports per-category compliance rates. Content constraints---which require attending to and recalling specific system-prompt instructions across turns---show the largest improvement (+23.8\,pp), consistent with GAR measuring attention to goal tokens. This category includes constraints like ``mention X in every response'' and ``always reference the original topic,'' which require sustained attention to the system prompt. Position constraints (e.g., ``start each response with Y'') show a modest improvement (+6.7\,pp), as they partially depend on goal-token attention. Format (e.g., ``use bullet points'') and count constraints (e.g., ``exactly 3 sentences'') show no change, consistent with these being procedural patterns that are cached in the model's generation routine rather than requiring ongoing attention to the system prompt.
+
+\paragraph{Correlation analysis.} The GAR-compliance correlation ($r$\,=\,0.200, $p$\,=\,0.007) is statistically significant but modest, suggesting that attention to goal tokens is one of several factors in instruction compliance. Other factors likely include the model's procedural memory for format constraints, the specificity of the constraint (vague constraints are harder regardless of attention), and the interaction between constraint type and conversation topic. McNemar's test ($p$\,=\,0.077) is marginally significant for the overall compliance improvement, reflecting the small sample size (18 constraint types). These results are exploratory and pending multi-model confirmation.
+
+Figure~\ref{fig:ir-bar} visualizes the per-category breakdown.
+
+\begin{figure}[t]
+  \centering
+  \includegraphics[width=\columnwidth]{fig_instruction_retention.pdf}
+  \caption{Instruction retention by constraint category under $\beta$\,=\,3 steering. Content constraints benefit most (+23.8\,pp); format and count constraints are unaffected.}
+  \label{fig:ir-bar}
+\end{figure}
+
+\FloatBarrier
+
+\begin{table}[t]
+\centering\small
Shell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "796fc862-185e-49f2-aa0e-027cc817fe45",
  "isSidechain": false,
  "promptId": "8d8464e4-1523-464c-8d63-5cd7db13bd3f",
  "type": "user",
  "uuid": "9099c556-69d0-4611-a9a9-1e7c9bf82619",
  "toolUseResult": {
    "stdout": "diff --git a/paper/sections/appendix.tex b/paper/sections/appendix.tex\nindex 8f1bb3d..8f22842 100644\n--- a/paper/sections/appendix.tex\n+++ b/paper/sections/appendix.tex\n@@ -1,26 +1,850 @@\n-\\section{Training Hyperparameters}\\label{sec:appendix-hyper}\n+\\section{Training Configuration}\\label{sec:appendix-hyper}\n \n-All fine-tuned variants share the following configuration: Qwen-2.5-7B-Instruct base model, LoRA rank 16 ($\\alpha$=32) on \\texttt{q\\_proj} and \\texttt{v\\_proj}, AdamW optimizer (lr = $2 \\times 10^{-4}$, $\\beta_1$=0.9, $\\beta_2$=0.999), batch size 1 with gradient accumulation 8, 3 epochs over 8K UltraChat conversations, maximum sequence length 2048, seed 42. ThreadGate gates use a 10$\\times$ learning rate multiplier and initial bias 1.5 ($\\sigma(1.5) \\approx 0.82$).\n+Table~\\ref{tab:hyperparams} lists the full training configuration shared across all fine-tuned variants. ThreadGate gate parameters receive a $10\\times$ learning rate multiplier and are initialized with bias 1.5 ($\\sigma(1.5) \\approx 0.82$); the gate MLP adds ${\\sim}$57K parameters per variant ($<$0.001\\% of 7B). The scheduled sampling variant (v8b) linearly increases the model-generated context ratio from 0 to 0.3 over 3 epochs (29.7--37.1\\% effective usage due to per-sample Bernoulli sampling). All experiments were conducted on a single NVIDIA RTX PRO 6000 Blackwell Server Edition GPU (96\\,GB VRAM), requiring 6--8 hours per variant.\n+\n+\\begin{table}[t]\n+\\centering\\small\n+\\caption{Training hyperparameters for all fine-tuned variants. Entries marked $\\dagger$ apply only to ThreadGate and its ablations.}\n+\\label{tab:hyperparams}\n+\\begin{tabular}{l@{\\hspace{8pt}}l}\n+\\toprule\n+\\textbf{Parameter} & \\textbf{Value} \\\\\n+\\midrule\n+Base model & Qwen-2.5-7B-Instruct \\\\\n+LoRA rank / $\\alpha$ & 16 / 32 \\\\\n+LoRA targets & \\texttt{q\\_proj}, \\texttt{v\\_proj} \\\\\n+Optimizer & AdamW ($\\beta_1$\\!=\\!0.9, $\\beta_2$\\!=\\!0.999) \\\\\n+Learning rate & $2 \\times 10^{-4}$ \\\\\n+Gate LR mult.$^\\dagger$ & $10\\times$ \\\\\n+Batch / grad accum & 1 / 8 (eff.\\ 8) \\\\\n+Epochs & 3 \\\\\n+Max seq length & 2048 \\\\\n+Training data & 8K UltraChat convs \\\\\n+Seed & 42 (+123 for TG, SS) \\\\\n+$\\lambda_\\text{GAR}$/$\\lambda_\\text{div}$ & 1.0 / 1.0 \\\\\n+GAR target $\\tau$ & 0.5 \\\\\n+Gate init bias$^\\dagger$ & 1.5 ($\\sigma\\!\\approx\\!0.82$) \\\\\n+Gate hidden dim$^\\dagger$ & 64 \\\\\n+Turn embed dim$^\\dagger$ & 16 \\\\\n+GPU & RTX PRO 6000 (96\\,GB) \\\\\n+Training time & 6--8 h / variant \\\\\n+\\bottomrule\n+\\end{tabular}\n+\\end{table}\n \n \\section{Loss Formulation Search}\\label{sec:appendix-loss}\n \n-Table~\\ref{tab:loss-iterations} summarizes the seven loss configurations explored before arriving at the final MSE + gate diversity formulation (\\S\\ref{sec:loss}). Configurations v1--v6 span three alternative loss families; none converged during training.\n+The final MSE + gate diversity loss (\\S\\ref{sec:loss}) emerged from seven iterations spanning four loss families. Table~\\ref{tab:loss-iterations} summarizes the progression. The search was motivated by a consistent failure mode: naive formulations either collapse to trivial solutions (cumulative losses) or drive gates toward identity (maximize-family losses). We describe each family below.\n \n-\\begin{table}[h]\n-\\centering\\small\n-\\caption{Loss formulation iterations on Qwen-2.5-7B-Instruct. GAR-ours (teacher-forced) and PPL are reported only for the converged configuration.}\n+\\paragraph{Cumulative losses (v1--v2).} These losses accumulate GAR contributions across layers, rewarding monotonically increasing attention. v1 collapsed because once the cumulative GAR exceeded the threshold, the loss gradient vanished and gates froze. v2 added an $\\varepsilon$-stabilization term to the cumulative product, but numerical instability from the product of 28 per-layer terms dominated, and training followed the same trajectory.\n+\n+\\paragraph{Maximize losses (v3--v5).} These losses directly maximize mean GAR ($-\\text{mean}(\\text{GAR})$). The unbounded objective rewards full pass-through ($g \\to 1.0$), collapsing gate diversity (std $<$ 0.025). At $\\lambda$=2 (v3), gates froze within 100 steps; at $\\lambda$=10 (v3b), convergence to identity accelerated; at $\\lambda$=1 (v5), rebalancing delayed but did not prevent the same degenerate solution.\n+\n+\\paragraph{Smooth saturation (v6).} This bounded the reward using a saturating function, intended to prevent the unbounded growth of maximize losses. In practice, the loss landscape remained monotonic in $g$, and training followed the same terminal trajectory as the maximize family, only more slowly.\n+\n+\\paragraph{MSE + gate diversity (v7).} The MSE formulation provides bidirectional pressure: GAR above $\\tau$ incurs the same penalty as GAR below $\\tau$, preventing the runaway optimization of maximize losses. The gate diversity regularizer ($\\mathcal{L}_\\text{div}$) enforces a minimum standard deviation across per-layer gate values, preventing all gates from collapsing to a uniform value. This combination is the only one that achieved stable convergence (GAR-ours = 0.50, PPL = 2.78).\n+\n+\\begin{table*}[t]\n+\\centering\\footnotesize\n+\\caption{Loss formulation iterations on Qwen-2.5-7B-Instruct. GAR-ours (teacher-forced) and PPL are reported only for the converged configuration (v7).}\n \\label{tab:loss-iterations}\n-\\begin{tabular}{l l l c c}\n+\\begin{tabular}{l l l p{5.8cm} c c}\n+\\toprule\n+ & \\textbf{Loss Family} & \\textbf{Status} & \\textbf{Failure Mechanism} & \\textbf{GAR} & \\textbf{PPL} \\\\\n+\\midrule\n+v1  & Cumulative            & \\texttimes~GAR loss $\\to$ 0     & GAR loss collapses to zero once threshold is reached; gate gradients vanish at equilibrium & ---  & ---  \\\\\n+v2  & Cumulative + $\\varepsilon$ & \\texttimes~same trajectory & Numerical instability from cumulative product; $\\varepsilon$-stabilization insufficient & ---  & ---  \\\\\n+v3  & Maximize ($\\lambda$=2)  & \\texttimes~gate frozen        & Unbounded reward drives gates toward identity (all-pass); no layer selectivity & ---  & ---  \\\\\n+v3b & Maximize ($\\lambda$=10) & \\texttimes~identity collapse   & Higher $\\lambda$ accelerates convergence to same degenerate identity solution & ---  & ---  \\\\\n+v5  & Maximize ($\\lambda$=1)  & \\texttimes~identity collapse   & Rebalancing delays but does not prevent identity collapse & ---  & ---  \\\\\n+v6  & Smooth saturation       & \\texttimes~identity collapse   & Monotonic reward identical to maximize in practice; boundedness slows but does not alter terminal trajectory & ---  & ---  \\\\\n+v7  & MSE + gate div          & \\checkmark~\\textbf{converged}  & \\textbf{Bidirectional penalty prevents identity collapse; gate diversity regularizer enforces layer selectivity} & 0.50 & 2.78 \\\\\n+\\bottomrule\n+\\end{tabular}\n+\\end{table*}\n+\n+\\section{Instruction Retention Details}\\label{sec:appendix-ir}\n+\n+To evaluate whether GAR improvements translate to downstream task performance, we test instruction retention across 18 system-prompt constraint types using the ThreadGate checkpoint with $\\beta$\\,=\\,3 steering on $N$\\,=\\,200 held-out conversations. Each constraint type requires the model to follow a specific instruction embedded in the system prompt (e.g., ``always respond in bullet points'', ``never use the word X'', ``include a summary at the end''). This evaluation bridges the gap between our attention-level metric (GAR) and observable model behavior.\n+\n+\\paragraph{Evaluation protocol.} For each conversation, we inject a constraint into the system prompt and evaluate compliance across all assistant turns. A turn is compliant if it satisfies the constraint according to rule-based checkers (for format, count, and position constraints) or GPT-4-based evaluation (for content constraints, which require semantic judgment). We use the same 18 constraint types across all conversations, yielding $N$\\,=\\,54 paired evaluations (18 types $\\times$ 3 conversations per type) for the McNemar analysis.\n+\n+\\paragraph{Per-category results.} Table~\\ref{tab:ir-results} reports per-category compliance rates. Content constraints---which require attending to and recalling specific system-prompt instructions across turns---show the largest improvement (+23.8\\,pp), consistent with GAR measuring attention to goal tokens. This category includes constraints like ``mention X in every response'' and ``always reference the original topic,'' which require sustained attention to the system prompt. Position constraints (e.g., ``start each response with Y'') show a modest improvement (+6.7\\,pp), as they partially depend on goal-token attention. Format (e.g., ``use bullet points'') and count constraints (e.g., ``exactly 3 sentences'') show no change, consistent with these being procedural patterns that are cached in the model's generation routine rather than requiring ongoing attention to the system prompt.\n+\n+\\paragraph{Correlation analysis.} The GAR-compliance correlation ($r$\\,=\\,0.200, $p$\\,=\\,0.007) is statistically significant but modest, suggesting that attention to goal tokens is one of several factors in instruction compliance. Other factors likely include the model's procedural memory for format constraints, the specificity of the constraint (vague constraints are harder regardless of attention), and the interaction between constraint type and conversation topic. McNemar's test ($p$\\,=\\,0.077) is marginally significant for the overall compliance improvement, reflecting the small sample size (18 constraint types). These results are exploratory and pending multi-model confirmation.\n+\n+Figure~\\ref{fig:ir-bar} visualizes the per-category breakdown.\n+\n+\\begin{figure}[t]\n+  \\centering\n+  \\includegraphics[width=\\columnwidth]{fig_instruction_retention.pdf}\n+  \\caption{Instruction retention by constraint category under $\\beta$\\,=\\,3 steering. Content constraints benefit most (+23.8\\,pp); format and count constraints are unaffected.}\n+  \\label{fig:ir-bar}\n+\\end{figure}\n+\n+\\FloatBarrier\n+\n+\\begin{table}[t]\n+\\centering\\small",
    "stderr": "\nShell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "796fc862-185e-49f2-aa0e-027cc817fe45",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921",
  "sessionId": "5d779602-0719-4d06-8bf9-fdd84990d5d0",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---


### Tool call

_source line 128 · 2026-05-25T20:42:49.212Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01GiW5XtgnSFr4LiEem2ZSVE`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating && git diff HEAD -- artifacts/appendix_expansion/ paper/sections/appendix.tex 2>/dev/null | head -100",
  "description": "Check uncommitted changes to appendix files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ebcd40b4-eaa6-429e-a4b7-94054e8bb654",
  "isSidechain": false,
  "requestId": "req_011CbPwHL52XdWxgWkGgjXgg",
  "type": "assistant",
  "uuid": "796fc862-185e-49f2-aa0e-027cc817fe45",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921",
  "sessionId": "5d779602-0719-4d06-8bf9-fdd84990d5d0",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012absUYQ1bkpMwhytjt57qH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6836,
      "cache_read_input_tokens": 108066,
      "output_tokens": 473,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6836,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 473,
          "cache_read_input_tokens": 108066,
          "cache_creation_input_tokens": 6836,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6836
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

_source line 129 · 2026-05-25T20:43:05.748Z_

<details><summary>Logged reasoning block</summary>

```text
The diff shows the appendix.tex was massively expanded from a skeleton to the full version, but the changes to `artifacts/appendix_expansion/` tables are NOT shown in this diff. This suggests the appendix_expansion tables haven't been modified.

Let me specifically check if there are any uncommitted changes to the specific tables I flagged.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9099c556-69d0-4611-a9a9-1e7c9bf82619",
  "isSidechain": false,
  "requestId": "req_011CbPwJqZavWHgciqWPUecE",
  "type": "assistant",
  "uuid": "2ebf16ce-3f06-4aeb-8eff-e3436fe6c3d9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921",
  "sessionId": "5d779602-0719-4d06-8bf9-fdd84990d5d0",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015ciJXrqghSJNRNeq1cyrwn",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3953,
      "cache_read_input_tokens": 114902,
      "output_tokens": 362,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3953,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 362,
          "cache_read_input_tokens": 114902,
          "cache_creation_input_tokens": 3953,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3953
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

_source line 130 · 2026-05-25T20:43:05.984Z_

<details open><summary>🔧 Tool call — Bash · `toolu_015AtppH88vLgfEoi6wmf72h`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating && git diff HEAD -- artifacts/appendix_expansion/tab_crossmodel_detail.tex artifacts/appendix_expansion/tab_perseed_tg.tex artifacts/appendix_expansion/tab_perseed_ss.tex 2>/dev/null",
  "description": "Check uncommitted changes to flagged tables"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2ebf16ce-3f06-4aeb-8eff-e3436fe6c3d9",
  "isSidechain": false,
  "requestId": "req_011CbPwJqZavWHgciqWPUecE",
  "type": "assistant",
  "uuid": "b4199e33-d772-4ccf-bf5e-640aae23a10e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921",
  "sessionId": "5d779602-0719-4d06-8bf9-fdd84990d5d0",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015ciJXrqghSJNRNeq1cyrwn",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3953,
      "cache_read_input_tokens": 114902,
      "output_tokens": 362,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3953,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 362,
          "cache_read_input_tokens": 114902,
          "cache_creation_input_tokens": 3953,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3953
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

_source line 131 · 2026-05-25T20:43:06.030Z_

<details><summary>↩ Tool result · `toolu_015AtppH88vLgfEoi6wmf72h`</summary>

```text
Shell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b4199e33-d772-4ccf-bf5e-640aae23a10e",
  "isSidechain": false,
  "promptId": "8d8464e4-1523-464c-8d63-5cd7db13bd3f",
  "type": "user",
  "uuid": "5e484275-2994-46af-845d-bc4b482b5b39",
  "toolUseResult": {
    "stdout": "",
    "stderr": "\nShell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "b4199e33-d772-4ccf-bf5e-640aae23a10e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921",
  "sessionId": "5d779602-0719-4d06-8bf9-fdd84990d5d0",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---


### Tool result

_source line 132 · 2026-05-25T20:43:07.290Z_

<details><summary>↩ Tool result · `toolu_01NFupDHK559Vbz9zAmSathU`</summary>

```text
On branch master
Changes not staged for commit:
  (use "git add &lt;file>..." to update what will be committed)
  (use "git restore &lt;file>..." to discard changes in working directory)
	modified:   paper/sections/appendix.tex

Untracked files:
  (use "git add &lt;file>..." to include in what will be committed)
	artifacts/appendix_expansion/

no changes added to commit (use "git add" and/or "git commit -a")
Shell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "44d443a4-5ab9-48e8-b6f6-af415177e3f4",
  "isSidechain": false,
  "promptId": "8d8464e4-1523-464c-8d63-5cd7db13bd3f",
  "type": "user",
  "uuid": "3c4c89f8-f95e-47c1-9d68-2d99387dc78f",
  "toolUseResult": {
    "stdout": "On branch master\nChanges not staged for commit:\n  (use \"git add &lt;file>...\" to update what will be committed)\n  (use \"git restore &lt;file>...\" to discard changes in working directory)\n\tmodified:   paper/sections/appendix.tex\n\nUntracked files:\n  (use \"git add &lt;file>...\" to include in what will be committed)\n\tartifacts/appendix_expansion/\n\nno changes added to commit (use \"git add\" and/or \"git commit -a\")",
    "stderr": "\nShell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "44d443a4-5ab9-48e8-b6f6-af415177e3f4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921",
  "sessionId": "5d779602-0719-4d06-8bf9-fdd84990d5d0",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---


### Tool call

_source line 133 · 2026-05-25T20:43:07.228Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01NFupDHK559Vbz9zAmSathU`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating && git status -- artifacts/appendix_expansion/ paper/sections/appendix.tex 2>/dev/null",
  "description": "Check file status for appendix"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5e484275-2994-46af-845d-bc4b482b5b39",
  "isSidechain": false,
  "requestId": "req_011CbPwJqZavWHgciqWPUecE",
  "type": "assistant",
  "uuid": "44d443a4-5ab9-48e8-b6f6-af415177e3f4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921",
  "sessionId": "5d779602-0719-4d06-8bf9-fdd84990d5d0",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015ciJXrqghSJNRNeq1cyrwn",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3953,
      "cache_read_input_tokens": 114902,
      "output_tokens": 362,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3953,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 362,
          "cache_read_input_tokens": 114902,
          "cache_creation_input_tokens": 3953,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3953
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

_source line 134_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[服务器重启后首条消息] 当前日期: 2026-05-25。服务器刚重启，项目状态可能已更新。在处理审查请求前，**先读取 registry.yaml 和 report.md** 获取最新实验状态，不要依赖对话历史中的状态信息。  **审查请求：** [系统通知 — worker_done:worker_fix_audit_appendix_issues_20260525T203522]: Wor…",
  "leafUuid": "3c4c89f8-f95e-47c1-9d68-2d99387dc78f",
  "sessionId": "5d779602-0719-4d06-8bf9-fdd84990d5d0"
}
```

---


### Runtime record

_source line 135_

```json
{
  "type": "ai-title",
  "aiTitle": "Review worker audit appendix tables completion",
  "sessionId": "5d779602-0719-4d06-8bf9-fdd84990d5d0"
}
```

---


### Assistant

_source line 136 · 2026-05-25T20:43:18.498Z_

<details><summary>Logged reasoning block</summary>

```text
So `artifacts/appendix_expansion/` is listed as "Untracked files" - meaning the entire directory is new and hasn't been committed yet. The `paper/sections/appendix.tex` has uncommitted modifications. But neither of the specific tables I flagged (tab_crossmodel_detail.tex, tab_perseed_tg.tex) have been changed since they were first created.

The worker "worker_fix_audit_appendix_issues" was supposed to fix the issues I flagged. Let me check the appendix.tex diff more carefully to see if the worker added any explanatory text or footnotes addressing my concerns in the body text (rather than changing the table .tex files themselves).


The appendix.tex expanded from a skeleton to a full 850-line document, likely from the first worker I reviewed. The second worker was supposed to address my specific concerns, but the tables themselves remain unchanged. I need to look at the current appendix.tex sections covering the cross-model and per-seed TG tables to see if any explanatory notes were added to address my concerns.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3c4c89f8-f95e-47c1-9d68-2d99387dc78f",
  "isSidechain": false,
  "requestId": "req_011CbPwLAUecB4ToTj5Mwkos",
  "type": "assistant",
  "uuid": "28b8dffd-60f2-4298-b13d-0fe4c7e487a2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921",
  "sessionId": "5d779602-0719-4d06-8bf9-fdd84990d5d0",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PrE4uYjjmcoYri3gbJ8YJ3",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 632,
      "cache_read_input_tokens": 118855,
      "output_tokens": 561,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 632,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 561,
          "cache_read_input_tokens": 118855,
          "cache_creation_input_tokens": 632,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 632
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

_source line 137 · 2026-05-25T20:43:18.500Z_

附录表格文件未被修改。让我检查附录正文中是否添加了解释性文字来回应我的审查意见。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "28b8dffd-60f2-4298-b13d-0fe4c7e487a2",
  "isSidechain": false,
  "requestId": "req_011CbPwLAUecB4ToTj5Mwkos",
  "type": "assistant",
  "uuid": "e082d49e-ed50-4042-a63e-2c2f501a7e72",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921",
  "sessionId": "5d779602-0719-4d06-8bf9-fdd84990d5d0",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PrE4uYjjmcoYri3gbJ8YJ3",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 632,
      "cache_read_input_tokens": 118855,
      "output_tokens": 561,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 632,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 561,
          "cache_read_input_tokens": 118855,
          "cache_creation_input_tokens": 632,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 632
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

_source line 138 · 2026-05-25T20:43:20.836Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01Nv2v3vRNQFXSaw7Yata4gh`</summary>

```json
{
  "pattern": "three.seed|multi.seed|3-seed|N=5.*N=50|eval protocol|gap.*31|gap.*7\\.9",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex",
  "output_mode": "content",
  "-i": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e082d49e-ed50-4042-a63e-2c2f501a7e72",
  "isSidechain": false,
  "requestId": "req_011CbPwLAUecB4ToTj5Mwkos",
  "type": "assistant",
  "uuid": "0e8c5147-1845-44a0-9354-0d46cf94783b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921",
  "sessionId": "5d779602-0719-4d06-8bf9-fdd84990d5d0",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PrE4uYjjmcoYri3gbJ8YJ3",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 632,
      "cache_read_input_tokens": 118855,
      "output_tokens": 561,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 632,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 561,
          "cache_read_input_tokens": 118855,
          "cache_creation_input_tokens": 632,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 632
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

_source line 139 · 2026-05-25T20:43:20.865Z_

<details><summary>↩ Tool result · `toolu_01Nv2v3vRNQFXSaw7Yata4gh`</summary>

```text
207:[Omitted long matching line]
491:[Omitted long matching line]
493:[Omitted long matching line]
500:\caption{Exposure bias scaling analysis. (a)~TF/AR gap ratio across training variants; scheduled sampling (SS, ${\sim}$1.2$\times$) is the only variant near parity. Llama gaps ($\sim$27$\times$) exceed all Qwen variants. (b)~Gap compounds with conversation length: ThreadGate's gap widens from 8$\times$ (3.6 turns) to 31$\times$ (10 turns).}
631:Tables~\ref{tab:perseed-ss} and~\ref{tab:perseed-tg} report full per-seed breakdowns for the two multi-seed configurations, providing evidence that our main findings are robust to random initialization.
635:\paragraph{ThreadGate (2 seeds).} Two seeds produce nearly identical TF metrics ($0.504\pm0.001$) and similar AR GAR (0.064 vs.\ 0.055), with gap ratios of 7.9$\times$ and 9.1$\times$ respectively. The 15\% relative difference in AR GAR is small compared to the order-of-magnitude TF-AR gap, confirming that the exposure bias phenomenon is not seed-dependent.
637:[Omitted long matching line]
810:[Omitted long matching line]
830:Baseline TG gap & 7.9$\times$ & 27$\times$ (median) \\
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0e8c5147-1845-44a0-9354-0d46cf94783b",
  "isSidechain": false,
  "promptId": "8d8464e4-1523-464c-8d63-5cd7db13bd3f",
  "type": "user",
  "uuid": "34dfc619-e0a1-4eaf-b7d9-5ac586333ff0",
  "toolUseResult": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "207:[Omitted long matching line]\n491:[Omitted long matching line]\n493:[Omitted long matching line]\n500:\\caption{Exposure bias scaling analysis. (a)~TF/AR gap ratio across training variants; scheduled sampling (SS, ${\\sim}$1.2$\\times$) is the only variant near parity. Llama gaps ($\\sim$27$\\times$) exceed all Qwen variants. (b)~Gap compounds with conversation length: ThreadGate's gap widens from 8$\\times$ (3.6 turns) to 31$\\times$ (10 turns).}\n631:Tables~\\ref{tab:perseed-ss} and~\\ref{tab:perseed-tg} report full per-seed breakdowns for the two multi-seed configurations, providing evidence that our main findings are robust to random initialization.\n635:\\paragraph{ThreadGate (2 seeds).} Two seeds produce nearly identical TF metrics ($0.504\\pm0.001$) and similar AR GAR (0.064 vs.\\ 0.055), with gap ratios of 7.9$\\times$ and 9.1$\\times$ respectively. The 15\\% relative difference in AR GAR is small compared to the order-of-magnitude TF-AR gap, confirming that the exposure bias phenomenon is not seed-dependent.\n637:[Omitted long matching line]\n810:[Omitted long matching line]\n830:Baseline TG gap & 7.9$\\times$ & 27$\\times$ (median) \\\\",
    "numLines": 9
  },
  "sourceToolAssistantUUID": "0e8c5147-1845-44a0-9354-0d46cf94783b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921",
  "sessionId": "5d779602-0719-4d06-8bf9-fdd84990d5d0",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---


### Assistant

_source line 140 · 2026-05-25T20:43:27.785Z_

<details><summary>Logged reasoning block</summary>

```text
Interesting! Let me read the multi-seed section around line 631-640 in the appendix to see if the worker addressed the issues.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "34dfc619-e0a1-4eaf-b7d9-5ac586333ff0",
  "isSidechain": false,
  "requestId": "req_011CbPwMAZ989ZFDPfdCseFh",
  "type": "assistant",
  "uuid": "2c44f1b2-bf2a-4c32-8f12-5ed2aa94c9ba",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921",
  "sessionId": "5d779602-0719-4d06-8bf9-fdd84990d5d0",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LP9FnvrwYnysUWx4GhwsrF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 937,
      "cache_read_input_tokens": 119487,
      "output_tokens": 277,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 937,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 277,
          "cache_read_input_tokens": 119487,
          "cache_creation_input_tokens": 937,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 937
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

_source line 141 · 2026-05-25T20:43:28.852Z_

<details open><summary>🔧 Tool call — Read · `toolu_01XzQEpiedhdSzs3MewXep92`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex",
  "offset": 625,
  "limit": 50
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2c44f1b2-bf2a-4c32-8f12-5ed2aa94c9ba",
  "isSidechain": false,
  "requestId": "req_011CbPwMAZ989ZFDPfdCseFh",
  "type": "assistant",
  "uuid": "1f66f91c-135b-415e-b6d1-3ec2a3939bae",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921",
  "sessionId": "5d779602-0719-4d06-8bf9-fdd84990d5d0",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LP9FnvrwYnysUWx4GhwsrF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 937,
      "cache_read_input_tokens": 119487,
      "output_tokens": 277,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 937,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 277,
          "cache_read_input_tokens": 119487,
          "cache_creation_input_tokens": 937,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 937
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

_source line 142 · 2026-05-25T20:43:28.859Z_

<details><summary>↩ Tool result · `toolu_01XzQEpiedhdSzs3MewXep92`</summary>

```text
625	\end{table}
626	
627	The steering pattern mirrors the 7B results: $\beta$\,=\,5 recovers GAR to 0.657--0.715 ($p < 0.001$), confirming that attention misallocation is the proximal cause of GAR collapse across scales. At $\beta$\,=\,0, TG shows a small but significant GAR advantage ($p$\,=\,0.005); at $\beta$\,=\,3, the TG--Base difference is not statistically significant ($p$\,=\,0.815), unlike the 7B pattern where TG consistently outperforms Base. This scale-specific difference may reflect the 1.5B model's limited capacity to maintain learned routing at intermediate steering strengths. ThreadGate does provide a stability advantage---zero catastrophic PPL outliers vs.\ one in Base---suggesting that residual gating regularizes attention distributions even when aggregate GAR is comparable.
628	
629	\section{Per-Seed Detailed Results}\label{sec:appendix-perseed}
630	
631	Tables~\ref{tab:perseed-ss} and~\ref{tab:perseed-tg} report full per-seed breakdowns for the two multi-seed configurations, providing evidence that our main findings are robust to random initialization.
632	
633	\paragraph{Scheduled sampling (3 seeds).} TF GAR-ours averages $0.517\pm0.032$ across seeds under the held-out protocol (Table~\ref{tab:perseed-ss}); under IID evaluation, TF is more stable ($0.499\pm0.003$), with the held-out variance driven by seed~123's higher value on the larger $N$\,=\,200 sample. AR GAR shows meaningful variance (std\,=\,0.047): seed 42 produces the lowest AR GAR (0.347, gap 1.4$\times$), seed 123 is intermediate (0.423, gap 1.3$\times$), and seed 456 is highest (0.433, gap 1.2$\times$). This variance is expected: AR evaluation involves free-form generation where small differences in learned attention patterns can compound across turns. The variance is asymmetric---all seeds remain well above the non-SS baseline (0.064)---so the qualitative conclusion (SS provides order-of-magnitude improvement) holds across seeds. At $\beta$\,=\,5, the cross-seed variance nearly vanishes ($0.717\pm0.001$), confirming that strong steering converges to a seed-independent attention equilibrium that overwhelms initialization differences.
634	
635	\paragraph{ThreadGate (2 seeds).} Two seeds produce nearly identical TF metrics ($0.504\pm0.001$) and similar AR GAR (0.064 vs.\ 0.055), with gap ratios of 7.9$\times$ and 9.1$\times$ respectively. The 15\% relative difference in AR GAR is small compared to the order-of-magnitude TF-AR gap, confirming that the exposure bias phenomenon is not seed-dependent.
636	
637	\paragraph{Training dynamics.} Seed variance in training time is non-trivial for scheduled sampling: seed 123 requires 10.8 hours (80\% overhead) vs.\ 6.5 hours for seeds 42 and 456 (8\% overhead). This variance is driven by the stochastic Bernoulli sampling of model-generated contexts: seed 123 happens to trigger longer autoregressive generation episodes early in training, where the model produces longer outputs before hitting the max-length cutoff. Despite this training-time variance, all three seeds converge to similar final metrics, suggesting the optimization landscape is robust.
638	
639	\input{../artifacts/appendix_expansion/tab_perseed_ss.tex}
640	
641	\input{../artifacts/appendix_expansion/tab_perseed_tg.tex}
642	
643	\section{Per-Turn GAR Decay Analysis}\label{sec:appendix-perturn-detail}
644	
645	Tables~\ref{tab:perturn-qwen} and~\ref{tab:perturn-llama} present per-turn AR GAR values for all configurations on both architectures, complementing the aggregate mid-turn GAR reported in the main text (Table~\ref{tab:five-way}).
646	
647	\paragraph{Qwen per-turn dynamics.} On Qwen (Table~\ref{tab:perturn-qwen}), all non-SS variants show rapid monotonic decay: turn-1 GAR ranges from 0.085 (Base) to 0.130 (ThreadGate), but by turn~5 all collapse below 0.07. The decay rate is approximately exponential for the first 3 turns, then plateaus near a floor value that varies by configuration (Base: 0.004, ThreadGate: 0.043--0.066, LoRA-only: 0.040). ThreadGate and LoRA-only show occasional turn-level fluctuations (e.g., TG turn~5 = 0.066 $>$ turn~4 = 0.043), which reflect stochastic variation in individual conversations rather than systematic recovery. Scheduled sampling retains substantially higher GAR throughout (turn-5 GAR\,=\,0.365 vs.\ 0.066 for ThreadGate), with a much flatter decay profile (15\% decline from turn~1 to turn~5 vs.\ 49\% for ThreadGate). This flatter profile is the signature of distributional robustification: SS-trained models encounter model-generated context during training, so the attention patterns are calibrated for the distribution they actually face during inference.
648	
649	\paragraph{Llama per-turn dynamics.} On Llama (Table~\ref{tab:perturn-llama}), the decay is steeper: Base GAR drops from 0.028 to 0.008 over 4 turns (71\% decline in the $N$\,=\,20 evaluation), and from 0.026 to 0.003 over 10 turns (88\% decline in the $N$\,=\,5 long-conversation evaluation). ThreadGate on Llama shows a distinctive pattern: turn-level GAR is roughly constant (0.038--0.049) rather than monotonically declining, suggesting that the gating mechanism maintains a stable floor on Llama that it fails to maintain on Qwen. However, this floor (0.04) is still an order of magnitude below the TF target (0.484), confirming that the fundamental TF-AR gap persists.
650	
651	\paragraph{Cross-architecture comparison.} The per-turn decay profiles reveal an architectural difference: Qwen shows a sharper initial decline (turn~1 to turn~2: $-$62\% for Base) followed by a plateau, while Llama shows a more gradual and sustained decline throughout. This difference may reflect the two architectures' different attention head configurations and layer counts, but the qualitative pattern---monotonic or near-monotonic decline toward a near-zero floor---is universal.
652	
653	Figures~\ref{fig:perturn-qwen-detail} and~\ref{fig:perturn-llama-detail} visualize these trajectories.
654	
655	\input{../artifacts/appendix_expansion/tab_perturn_qwen.tex}
656	
657	\begin{figure}[t]
658	  \centering
659	  \includegraphics[width=\columnwidth]{fig_perturn_qwen_detail.pdf}
660	  \caption{Per-turn AR GAR-ours across six Qwen-2.5-7B configurations. Scheduled sampling (green) retains far higher GAR than all other variants, which cluster below 0.13 and decay rapidly.}
661	  \label{fig:perturn-qwen-detail}
662	\end{figure}
663	
664	\input{../artifacts/appendix_expansion/tab_perturn_llama.tex}
665	
666	\begin{figure}[t]
667	  \centering
668	  \includegraphics[width=\columnwidth]{fig_perturn_llama_detail.pdf}
669	  \caption{Per-turn AR GAR decay on Llama-3.1-8B. (a)~Three-way comparison (Base, TG, LoRA-only; $N$\,=\,20, 4 turns). (b)~Extended Base decay profile ($N$\,=\,5, 10 turns), showing 90\% decline.}
670	  \label{fig:perturn-llama-detail}
671	\end{figure}
672	
673	\section{Extended Dataset Statistics}\label{sec:appendix-dataset-ext}
674	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1f66f91c-135b-415e-b6d1-3ec2a3939bae",
  "isSidechain": false,
  "promptId": "8d8464e4-1523-464c-8d63-5cd7db13bd3f",
  "type": "user",
  "uuid": "21100320-f4d4-4c0d-801b-21d5260775de",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex",
      "content": "\\end{table}\n\nThe steering pattern mirrors the 7B results: $\\beta$\\,=\\,5 recovers GAR to 0.657--0.715 ($p < 0.001$), confirming that attention misallocation is the proximal cause of GAR collapse across scales. At $\\beta$\\,=\\,0, TG shows a small but significant GAR advantage ($p$\\,=\\,0.005); at $\\beta$\\,=\\,3, the TG--Base difference is not statistically significant ($p$\\,=\\,0.815), unlike the 7B pattern where TG consistently outperforms Base. This scale-specific difference may reflect the 1.5B model's limited capacity to maintain learned routing at intermediate steering strengths. ThreadGate does provide a stability advantage---zero catastrophic PPL outliers vs.\\ one in Base---suggesting that residual gating regularizes attention distributions even when aggregate GAR is comparable.\n\n\\section{Per-Seed Detailed Results}\\label{sec:appendix-perseed}\n\nTables~\\ref{tab:perseed-ss} and~\\ref{tab:perseed-tg} report full per-seed breakdowns for the two multi-seed configurations, providing evidence that our main findings are robust to random initialization.\n\n\\paragraph{Scheduled sampling (3 seeds).} TF GAR-ours averages $0.517\\pm0.032$ across seeds under the held-out protocol (Table~\\ref{tab:perseed-ss}); under IID evaluation, TF is more stable ($0.499\\pm0.003$), with the held-out variance driven by seed~123's higher value on the larger $N$\\,=\\,200 sample. AR GAR shows meaningful variance (std\\,=\\,0.047): seed 42 produces the lowest AR GAR (0.347, gap 1.4$\\times$), seed 123 is intermediate (0.423, gap 1.3$\\times$), and seed 456 is highest (0.433, gap 1.2$\\times$). This variance is expected: AR evaluation involves free-form generation where small differences in learned attention patterns can compound across turns. The variance is asymmetric---all seeds remain well above the non-SS baseline (0.064)---so the qualitative conclusion (SS provides order-of-magnitude improvement) holds across seeds. At $\\beta$\\,=\\,5, the cross-seed variance nearly vanishes ($0.717\\pm0.001$), confirming that strong steering converges to a seed-independent attention equilibrium that overwhelms initialization differences.\n\n\\paragraph{ThreadGate (2 seeds).} Two seeds produce nearly identical TF metrics ($0.504\\pm0.001$) and similar AR GAR (0.064 vs.\\ 0.055), with gap ratios of 7.9$\\times$ and 9.1$\\times$ respectively. The 15\\% relative difference in AR GAR is small compared to the order-of-magnitude TF-AR gap, confirming that the exposure bias phenomenon is not seed-dependent.\n\n\\paragraph{Training dynamics.} Seed variance in training time is non-trivial for scheduled sampling: seed 123 requires 10.8 hours (80\\% overhead) vs.\\ 6.5 hours for seeds 42 and 456 (8\\% overhead). This variance is driven by the stochastic Bernoulli sampling of model-generated contexts: seed 123 happens to trigger longer autoregressive generation episodes early in training, where the model produces longer outputs before hitting the max-length cutoff. Despite this training-time variance, all three seeds converge to similar final metrics, suggesting the optimization landscape is robust.\n\n\\input{../artifacts/appendix_expansion/tab_perseed_ss.tex}\n\n\\input{../artifacts/appendix_expansion/tab_perseed_tg.tex}\n\n\\section{Per-Turn GAR Decay Analysis}\\label{sec:appendix-perturn-detail}\n\nTables~\\ref{tab:perturn-qwen} and~\\ref{tab:perturn-llama} present per-turn AR GAR values for all configurations on both architectures, complementing the aggregate mid-turn GAR reported in the main text (Table~\\ref{tab:five-way}).\n\n\\paragraph{Qwen per-turn dynamics.} On Qwen (Table~\\ref{tab:perturn-qwen}), all non-SS variants show rapid monotonic decay: turn-1 GAR ranges from 0.085 (Base) to 0.130 (ThreadGate), but by turn~5 all collapse below 0.07. The decay rate is approximately exponential for the first 3 turns, then plateaus near a floor value that varies by configuration (Base: 0.004, ThreadGate: 0.043--0.066, LoRA-only: 0.040). ThreadGate and LoRA-only show occasional turn-level fluctuations (e.g., TG turn~5 = 0.066 $>$ turn~4 = 0.043), which reflect stochastic variation in individual conversations rather than systematic recovery. Scheduled sampling retains substantially higher GAR throughout (turn-5 GAR\\,=\\,0.365 vs.\\ 0.066 for ThreadGate), with a much flatter decay profile (15\\% decline from turn~1 to turn~5 vs.\\ 49\\% for ThreadGate). This flatter profile is the signature of distributional robustification: SS-trained models encounter model-generated context during training, so the attention patterns are calibrated for the distribution they actually face during inference.\n\n\\paragraph{Llama per-turn dynamics.} On Llama (Table~\\ref{tab:perturn-llama}), the decay is steeper: Base GAR drops from 0.028 to 0.008 over 4 turns (71\\% decline in the $N$\\,=\\,20 evaluation), and from 0.026 to 0.003 over 10 turns (88\\% decline in the $N$\\,=\\,5 long-conversation evaluation). ThreadGate on Llama shows a distinctive pattern: turn-level GAR is roughly constant (0.038--0.049) rather than monotonically declining, suggesting that the gating mechanism maintains a stable floor on Llama that it fails to maintain on Qwen. However, this floor (0.04) is still an order of magnitude below the TF target (0.484), confirming that the fundamental TF-AR gap persists.\n\n\\paragraph{Cross-architecture comparison.} The per-turn decay profiles reveal an architectural difference: Qwen shows a sharper initial decline (turn~1 to turn~2: $-$62\\% for Base) followed by a plateau, while Llama shows a more gradual and sustained decline throughout. This difference may reflect the two architectures' different attention head configurations and layer counts, but the qualitative pattern---monotonic or near-monotonic decline toward a near-zero floor---is universal.\n\nFigures~\\ref{fig:perturn-qwen-detail} and~\\ref{fig:perturn-llama-detail} visualize these trajectories.\n\n\\input{../artifacts/appendix_expansion/tab_perturn_qwen.tex}\n\n\\begin{figure}[t]\n  \\centering\n  \\includegraphics[width=\\columnwidth]{fig_perturn_qwen_detail.pdf}\n  \\caption{Per-turn AR GAR-ours across six Qwen-2.5-7B configurations. Scheduled sampling (green) retains far higher GAR than all other variants, which cluster below 0.13 and decay rapidly.}\n  \\label{fig:perturn-qwen-detail}\n\\end{figure}\n\n\\input{../artifacts/appendix_expansion/tab_perturn_llama.tex}\n\n\\begin{figure}[t]\n  \\centering\n  \\includegraphics[width=\\columnwidth]{fig_perturn_llama_detail.pdf}\n  \\caption{Per-turn AR GAR decay on Llama-3.1-8B. (a)~Three-way comparison (Base, TG, LoRA-only; $N$\\,=\\,20, 4 turns). (b)~Extended Base decay profile ($N$\\,=\\,5, 10 turns), showing 90\\% decline.}\n  \\label{fig:perturn-llama-detail}\n\\end{figure}\n\n\\section{Extended Dataset Statistics}\\label{sec:appendix-dataset-ext}\n",
      "numLines": 50,
      "startLine": 625,
      "totalLines": 851
    }
  },
  "sourceToolAssistantUUID": "1f66f91c-135b-415e-b6d1-3ec2a3939bae",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921",
  "sessionId": "5d779602-0719-4d06-8bf9-fdd84990d5d0",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---


### Tool result

_source line 143 · 2026-05-25T20:43:29.334Z_

<details><summary>↩ Tool result · `toolu_011eZVDHwWmJgqLe5VhDPdv7`</summary>

```text
485	\end{table}
486	
487	\section{Exposure Bias Scaling}\label{sec:appendix-eb-scaling}
488	
489	Figure~\ref{fig:eb-scaling} quantifies two scaling dimensions of the exposure bias phenomenon: cross-variant gap ratios (panel~a) and length-dependent gap compounding (panel~b).
490	
491	\paragraph{Cross-variant gaps.} On Qwen, ThreadGate achieves the smallest gap among standard variants (7.9$\times$) while PCGrad shows the largest (16.7$\times$, consistent with its counterproductive effect on AR GAR). Scheduled sampling reduces the gap to ${\sim}$1.2$\times$, the only variant approaching parity. The ordering of gap ratios (SS $\ll$ TG $<$ LoRA $<$ UG $<$ PCGrad) differs from the ordering of TF GAR (all $\approx$ 0.50), confirming that training-time optimization success does not predict inference-time robustness. On Llama, both ThreadGate and LoRA-only show $\sim$27$\times$ gaps (by median), larger than any Qwen variant. The consistently larger Llama gaps may reflect its deeper architecture (32 vs.\ 28 layers), which provides more layers for distributional drift to compound through.
492	
493	\paragraph{Length-dependent compounding.} Panel~(b) shows that the gap compounds with conversation length: at 3.6 mean turns ($N$\,=\,50), ThreadGate's gap is 8$\times$; at 10 turns ($N$\,=\,5), it widens to 31$\times$. The relationship is approximately linear in the number of turns on a log scale, suggesting that the per-turn drift contribution is roughly multiplicative. Extrapolating this trend suggests that at 20 turns the gap would exceed 100$\times$, making any training-time attention signal essentially undetectable. This length dependence is consistent with cumulative distributional drift---each model-generated turn introduces additional divergence from the teacher-forced training distribution, and by turn~10 the accumulated drift overwhelms any gating signal.
494	
495	\paragraph{Implications for deployment.} These scaling results have practical implications: (1)~for applications requiring sustained attention over many turns (e.g., long-form tutoring, multi-step reasoning), architectural modifications alone are insufficient---distributional robustification or inference-time intervention is necessary; (2)~the near-parity of scheduled sampling (${\sim}$1.2$\times$ gap) suggests that bridging the training-inference distribution gap is both necessary and sufficient for maintaining attention; (3)~the $\beta$-steering approach provides a complementary inference-time solution, but its effectiveness also depends on conversation length (Appendix~\ref{sec:appendix-steering-viz}).
496	
497	\begin{figure}[t]
498	\centering
499	\includegraphics[width=\columnwidth]{fig_eb_scaling.pdf}
500	\caption{Exposure bias scaling analysis. (a)~TF/AR gap ratio across training variants; scheduled sampling (SS, ${\sim}$1.2$\times$) is the only variant near parity. Llama gaps ($\sim$27$\times$) exceed all Qwen variants. (b)~Gap compounds with conversation length: ThreadGate's gap widens from 8$\times$ (3.6 turns) to 31$\times$ (10 turns).}
501	\label{fig:eb-scaling}
502	\end{figure}
503	
504	\section{Per-Turn AR GAR Dynamics}\label{sec:appendix-ar-gar-dynamics}
505	
506	To characterize how goal attention evolves across conversation turns under autoregressive generation, we compute per-turn AR GAR for all six Qwen-2.5-7B training configurations (Base, LoRA-only, Uniform Gate, PCGrad, Scheduled Sampling, ThreadGate) on the held-out evaluation set. Figure~\ref{fig:kl_ar_gar_curves} plots per-turn AR GAR trajectories across turns 1--5, and Figure~\ref{fig:kl_ar_gar_bar} compares mid-turn AR GAR levels across configurations.
507	
508	All six configurations exhibit monotonic GAR decay as turn index increases, consistent with cumulative exposure bias eroding attention to goal tokens. The decay rate varies substantially: Scheduled Sampling retains by far the highest mid-turn GAR (0.423), followed distantly by ThreadGate (0.064), LoRA-only (0.037), Uniform Gate (0.033), PCGrad (0.030), and Base (0.019). Base decays most rapidly, losing the majority of its initial GAR within the first few turns. The large SS--TG gap mirrors Table~\ref{tab:five-way} and confirms that distributional robustification---not gating architecture alone---is the primary driver of AR GAR retention.\footnote{SS configuration uses seed 123 data; all other configurations use seed 42. Cross-seed trends are consistent (\S\ref{subsec:ss}).}
509	
510	\begin{figure}[t]
511	\centering
512	\includegraphics[width=\columnwidth]{fig_kl_ar_gar_curves.pdf}
513	\caption{Per-turn AR GAR trajectories for six Qwen-2.5-7B configurations (turns 1--5). All models show monotonic decay; Scheduled Sampling retains far higher GAR throughout (0.53$\to$0.39), while the remaining five variants cluster below 0.13 and decay rapidly.}
514	\label{fig:kl_ar_gar_curves}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5c738ee6-8838-48df-927b-7c8a4d2404ea",
  "isSidechain": false,
  "promptId": "8d8464e4-1523-464c-8d63-5cd7db13bd3f",
  "type": "user",
  "uuid": "85929b39-53a1-4046-b503-6d35c65ee574",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex",
      "content": "\\end{table}\n\n\\section{Exposure Bias Scaling}\\label{sec:appendix-eb-scaling}\n\nFigure~\\ref{fig:eb-scaling} quantifies two scaling dimensions of the exposure bias phenomenon: cross-variant gap ratios (panel~a) and length-dependent gap compounding (panel~b).\n\n\\paragraph{Cross-variant gaps.} On Qwen, ThreadGate achieves the smallest gap among standard variants (7.9$\\times$) while PCGrad shows the largest (16.7$\\times$, consistent with its counterproductive effect on AR GAR). Scheduled sampling reduces the gap to ${\\sim}$1.2$\\times$, the only variant approaching parity. The ordering of gap ratios (SS $\\ll$ TG $<$ LoRA $<$ UG $<$ PCGrad) differs from the ordering of TF GAR (all $\\approx$ 0.50), confirming that training-time optimization success does not predict inference-time robustness. On Llama, both ThreadGate and LoRA-only show $\\sim$27$\\times$ gaps (by median), larger than any Qwen variant. The consistently larger Llama gaps may reflect its deeper architecture (32 vs.\\ 28 layers), which provides more layers for distributional drift to compound through.\n\n\\paragraph{Length-dependent compounding.} Panel~(b) shows that the gap compounds with conversation length: at 3.6 mean turns ($N$\\,=\\,50), ThreadGate's gap is 8$\\times$; at 10 turns ($N$\\,=\\,5), it widens to 31$\\times$. The relationship is approximately linear in the number of turns on a log scale, suggesting that the per-turn drift contribution is roughly multiplicative. Extrapolating this trend suggests that at 20 turns the gap would exceed 100$\\times$, making any training-time attention signal essentially undetectable. This length dependence is consistent with cumulative distributional drift---each model-generated turn introduces additional divergence from the teacher-forced training distribution, and by turn~10 the accumulated drift overwhelms any gating signal.\n\n\\paragraph{Implications for deployment.} These scaling results have practical implications: (1)~for applications requiring sustained attention over many turns (e.g., long-form tutoring, multi-step reasoning), architectural modifications alone are insufficient---distributional robustification or inference-time intervention is necessary; (2)~the near-parity of scheduled sampling (${\\sim}$1.2$\\times$ gap) suggests that bridging the training-inference distribution gap is both necessary and sufficient for maintaining attention; (3)~the $\\beta$-steering approach provides a complementary inference-time solution, but its effectiveness also depends on conversation length (Appendix~\\ref{sec:appendix-steering-viz}).\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig_eb_scaling.pdf}\n\\caption{Exposure bias scaling analysis. (a)~TF/AR gap ratio across training variants; scheduled sampling (SS, ${\\sim}$1.2$\\times$) is the only variant near parity. Llama gaps ($\\sim$27$\\times$) exceed all Qwen variants. (b)~Gap compounds with conversation length: ThreadGate's gap widens from 8$\\times$ (3.6 turns) to 31$\\times$ (10 turns).}\n\\label{fig:eb-scaling}\n\\end{figure}\n\n\\section{Per-Turn AR GAR Dynamics}\\label{sec:appendix-ar-gar-dynamics}\n\nTo characterize how goal attention evolves across conversation turns under autoregressive generation, we compute per-turn AR GAR for all six Qwen-2.5-7B training configurations (Base, LoRA-only, Uniform Gate, PCGrad, Scheduled Sampling, ThreadGate) on the held-out evaluation set. Figure~\\ref{fig:kl_ar_gar_curves} plots per-turn AR GAR trajectories across turns 1--5, and Figure~\\ref{fig:kl_ar_gar_bar} compares mid-turn AR GAR levels across configurations.\n\nAll six configurations exhibit monotonic GAR decay as turn index increases, consistent with cumulative exposure bias eroding attention to goal tokens. The decay rate varies substantially: Scheduled Sampling retains by far the highest mid-turn GAR (0.423), followed distantly by ThreadGate (0.064), LoRA-only (0.037), Uniform Gate (0.033), PCGrad (0.030), and Base (0.019). Base decays most rapidly, losing the majority of its initial GAR within the first few turns. The large SS--TG gap mirrors Table~\\ref{tab:five-way} and confirms that distributional robustification---not gating architecture alone---is the primary driver of AR GAR retention.\\footnote{SS configuration uses seed 123 data; all other configurations use seed 42. Cross-seed trends are consistent (\\S\\ref{subsec:ss}).}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig_kl_ar_gar_curves.pdf}\n\\caption{Per-turn AR GAR trajectories for six Qwen-2.5-7B configurations (turns 1--5). All models show monotonic decay; Scheduled Sampling retains far higher GAR throughout (0.53$\\to$0.39), while the remaining five variants cluster below 0.13 and decay rapidly.}\n\\label{fig:kl_ar_gar_curves}",
      "numLines": 30,
      "startLine": 485,
      "totalLines": 851
    }
  },
  "sourceToolAssistantUUID": "5c738ee6-8838-48df-927b-7c8a4d2404ea",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921",
  "sessionId": "5d779602-0719-4d06-8bf9-fdd84990d5d0",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---


### Tool call

_source line 144 · 2026-05-25T20:43:29.321Z_

<details open><summary>🔧 Tool call — Read · `toolu_011eZVDHwWmJgqLe5VhDPdv7`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex",
  "offset": 485,
  "limit": 30
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "21100320-f4d4-4c0d-801b-21d5260775de",
  "isSidechain": false,
  "requestId": "req_011CbPwMAZ989ZFDPfdCseFh",
  "type": "assistant",
  "uuid": "5c738ee6-8838-48df-927b-7c8a4d2404ea",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921",
  "sessionId": "5d779602-0719-4d06-8bf9-fdd84990d5d0",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LP9FnvrwYnysUWx4GhwsrF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 937,
      "cache_read_input_tokens": 119487,
      "output_tokens": 277,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 937,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 277,
          "cache_read_input_tokens": 119487,
          "cache_creation_input_tokens": 937,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 937
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

_source line 145_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[服务器重启后首条消息] 当前日期: 2026-05-25。服务器刚重启，项目状态可能已更新。在处理审查请求前，**先读取 registry.yaml 和 report.md** 获取最新实验状态，不要依赖对话历史中的状态信息。  **审查请求：** [系统通知 — worker_done:worker_fix_audit_appendix_issues_20260525T203522]: Wor…",
  "leafUuid": "85929b39-53a1-4046-b503-6d35c65ee574",
  "sessionId": "5d779602-0719-4d06-8bf9-fdd84990d5d0"
}
```

---


### Runtime record

_source line 146_

```json
{
  "type": "ai-title",
  "aiTitle": "Review worker audit appendix tables completion",
  "sessionId": "5d779602-0719-4d06-8bf9-fdd84990d5d0"
}
```

---


### Assistant

_source line 147 · 2026-05-25T20:44:23.052Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a clear picture. Let me assess whether the worker addressed my two warning-level issues:

**Issue 1: tab_crossmodel_detail Qwen SS row mixes single-seed TF with multi-seed AR**

Looking at the current appendix text:
- Line 635: "ThreadGate (2 seeds). Two seeds produce nearly identical TF metrics ($0.504\pm0.001$) and similar AR GAR (0.064 vs. 0.055), with gap ratios of 7.9× and 9.1× respectively."

Wait, this says AR GAR = 0.064 and 0.055 for the two TG seeds. 

But the per-seed TG table shows AR GAR = 0.016 and 0.017 — completely different values! The body text is pulling from the N=50 evaluation (0.064, 7.9× gap) while the per-seed table still uses N=5 numbers (0.016, 31.4× gap). This creates a new inconsistency between the two sections.

Now I'm trying to track down where 0.055 comes from for the s123 seed. The d048_final_ar_eval only has s42 data showing 0.064, and the older eval_v7_tg_s123 shows 0.0165 for N=5, not 0.055. The eval_llama_ar_n20 is for Llama, not Qwen, so there's no N=50 evaluation for TG s123 in the registry I can find. This 0.055 value seems either fabricated or from an evaluation I haven't located, which is troubling.

Let me verify the math: 0.504/0.064 gives 7.875, which matches the 7.9× gap ratio cited for s42. For s123 to get the 9.1× ratio mentioned, I'd need 0.505/0.055 = 9.18, so the paper definitely needs that 0.055 value. But the d048_final_ar_eval description says it's a unified N=50 eval across six conditions for s42 only—there's no corresponding s123 evaluation in that dataset.

I'm wondering if the 0.055 number was estimated or computed some other way, or if it's just made up by whoever wrote this. That would be a major problem. I should check what the worker_fix_audit_appendix_issues actually changed in the appendix, but the diff is so large (skeleton to full appendix) that it's hard to isolate what came from the fix worker versus the audit worker. Let me narrow down the specific issues: the cross-model table SS mixing appears unchanged in the table itself, but the body text around line 491 might have been modified.

The per-seed section now has detailed variance explanations with gap ratios for each seed, which acknowledges the variance but doesn't resolve the fundamental inconsistency where TF uses s42 while AR uses a 3-seed mean. For the per-seed TG table, it's still using the N=5/T=10 protocol with a 31× gap, and the body text at line 635 is mixing N=50 numbers for s42 with what appears to be a different protocol number for the 0.055 value.

The real problem is that the text claims gap ratios of 7.9× and 9.1× while the table shows 31.4×, and the 0.055 value for s123 doesn't match any documented result. The "Exposure Bias Scaling" section does acknowledge that both the 8× and 31× gaps are valid at different conversation lengths, which is a reasonable framing, but the per-seed TG table is being presented as a robustness measure when it's actually showing something different. I'm noticing the 0.055 value doesn't match anything in the registry either—it could be an interpolated estimate rather than an actual evaluation result. But I just realized the registry has grown from 53 to 60 experiments, so there might be new TG-related entries I haven't checked yet.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "85929b39-53a1-4046-b503-6d35c65ee574",
  "isSidechain": false,
  "requestId": "req_011CbPwMo3rZiyGRWAFM7gDN",
  "type": "assistant",
  "uuid": "2a1ad71f-0d96-4b7b-92a8-d4a525cb95e1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921",
  "sessionId": "5d779602-0719-4d06-8bf9-fdd84990d5d0",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TuaKbqh4RJNtUDwYqQTXVy",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3853,
      "cache_read_input_tokens": 120424,
      "output_tokens": 1964,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3853,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1964,
          "cache_read_input_tokens": 120424,
          "cache_creation_input_tokens": 3853,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3853
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

_source line 148 · 2026-05-25T20:44:23.959Z_

发现关键问题：正文声称 TG s123 AR GAR = 0.055（gap 9.1×），但这个数字不在我之前读取的 registry 中。registry 总数从 53 增到 60，让我检查新增实验。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2a1ad71f-0d96-4b7b-92a8-d4a525cb95e1",
  "isSidechain": false,
  "requestId": "req_011CbPwMo3rZiyGRWAFM7gDN",
  "type": "assistant",
  "uuid": "0c2cc870-99fc-49aa-957e-a667f7df3c20",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921",
  "sessionId": "5d779602-0719-4d06-8bf9-fdd84990d5d0",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TuaKbqh4RJNtUDwYqQTXVy",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3853,
      "cache_read_input_tokens": 120424,
      "output_tokens": 1964,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3853,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1964,
          "cache_read_input_tokens": 120424,
          "cache_creation_input_tokens": 3853,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3853
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

_source line 149 · 2026-05-25T20:44:24.904Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01LzcpPKZxYkjc5tDGcyojCK`</summary>

```json
{
  "project": "turn_residual_gating",
  "limit": 10,
  "fields": [
    "status",
    "conclusion",
    "metrics",
    "hypothesis",
    "created_at"
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0c2cc870-99fc-49aa-957e-a667f7df3c20",
  "isSidechain": false,
  "requestId": "req_011CbPwMo3rZiyGRWAFM7gDN",
  "type": "assistant",
  "uuid": "ec08cdd2-0b56-4a26-82eb-377ddfe6e0dc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921",
  "sessionId": "5d779602-0719-4d06-8bf9-fdd84990d5d0",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TuaKbqh4RJNtUDwYqQTXVy",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3853,
      "cache_read_input_tokens": 120424,
      "output_tokens": 1964,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3853,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1964,
          "cache_read_input_tokens": 120424,
          "cache_creation_input_tokens": 3853,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3853
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

_source line 150 · 2026-05-25T20:44:25.083Z_

<details><summary>↩ Tool result · `toolu_01LzcpPKZxYkjc5tDGcyojCK`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {\"phase1a_multiseed_qwen\": {\"status\": \"DONE\", \"created_at\": \"2026-05-25T06:15:26.051Z\", \"hypothesis\": \"Multi-seed (s123, s456) training across 5 Qwen conditions (PCGrad, UG, LoRA-only, TG, SS) to establish mean±std for all claims. 8 training runs + AR eval N≥50 each. Expect TF convergence (GAR~0.50) and consistent AR rankings across seeds.\", \"conclusion\": \"killed\"}, \"p1_ss_lora_only\": {\"status\": \"DONE\", \"created_at\": \"2026-05-25T08:58:41.419Z\", \"hypothesis\": \"SS training on LoRA-only checkpoint (no ThreadGate) with same hyperparameters (rho_max=0.3, same schedule) should achieve similar GAR improvement as SS+TG. If confirmed, this proves the SS fix is architecture-agnostic, strengthening the paper's mitigation story (the gap is caused by exposure bias in any auxiliary-loss setup, and SS fixes it regardless of gating mechanism).\", \"conclusion\": \"killed\"}, \"phase2_switching\": {\"status\": \"DONE\", \"created_at\": \"2026-05-25T08:58:40.187Z\", \"hypothesis\": \"TF→AR switching at turn k (k=1..5) on ThreadGate s42 checkpoint. If GAR drops abruptly at the switch point (matching pure-AR level within 1 turn), it confirms exposure bias as instantaneous distribution shift rather than gradual KV cache drift. Staircase = exposure bias dominant; linear slope = KV drift dominant.\", \"conclusion\": \"killed\"}, \"phase2_tf_ar_switching\": {\"status\": \"QUEUED\", \"created_at\": \"2026-05-25T06:15:36.221Z\", \"hypothesis\": \"TF→AR switching at turn k (k=1..5) on ThreadGate s42 checkpoint. If GAR drops abruptly at the switch point (matching pure-AR level within 1 turn), it confirms exposure bias as instantaneous distribution shift rather than gradual cumulative drift.\"}, \"phase1a_multiseed_8runs\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-25T06:18:08.953Z\"}, \"phase1b_llama_complement\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-25T06:15:34.729Z\", \"hypothesis\": \"Llama PCGrad + UG (s42) to complete cross-model comparison matrix. If Llama PCGrad also fails to improve AR GAR (like Qwen), it strengthens the cross-architecture causal exclusion of gradient conflict.\"}, \"p1_llama_ss_eval\": {\"status\": \"DONE\", \"created_at\": \"2026-05-24T15:53:29.650Z\", \"hypothesis\": \"Llama SS (2-epoch) reduces the TF-AR GAR gap on Llama-3.1-8B, confirming SS as model-general mitigation (C4+C5). Eval: TF+AR N=50 β=0/3/5.\", \"conclusion\": \"success\", \"metrics\": {\"ss_tf_gar\": 0.477, \"ss_tf_ppl\": 2.82, \"ss_ar_b0_gar\": 0.1662, \"ss_ar_b0_ppl\": 1.37, \"ss_ar_b5_gar\": 0.7905, \"ss_ar_b5_ppl\": 1.81, \"base_ar_gar\": 0.0179, \"base_ar_ppl\": 1.22, \"tf_ar_gap\": 2.87}}, \"p1_llama_ss_training\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T19:37:48.689Z\", \"hypothesis\": \"SS is effective on Qwen (gap 8x to 1.4x). If SS also reduces the TF-AR gap on Llama-3.1-8B, it confirms SS as a model-general mitigation, strengthening C4 (mitigation) and C5 (cross-model) claims.\", \"conclusion\": \"success\"}, \"mmlu_eval_all\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T06:45:04.153Z\", \"hypothesis\": \"ThreadGate's per-layer gating and auxiliary GAR loss do not degrade the model's general language understanding capabilities. All fine-tuned variants (TG/UG/LO/PCGrad/SS) should maintain MMLU 5-shot accuracy within 1pp of the Base LoRA-only checkpoint, confirming that attention steering is additive rather than destructive.\", \"conclusion\": \"success\", \"metrics\": {\"base_qwen\": 0.7423, \"pcgrad_v9_s42\": 0.7386, \"ss_v8b_s42\": 0.7375, \"lo_s42\": 0.7357, \"tg_v7_s42\": 0.7347, \"ug_s42\": 0.7346}}, \"p2_llama_gradient_conflict\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T19:37:50.492Z\", \"hypothesis\": \"PCGrad fails to improve AR GAR on Llama-3.1-8B (as on Qwen), confirming cross-model that gradient conflict is not the root cause of the TF-AR gap, strengthening C2 (causal exclusion).\", \"conclusion\": \"success\", \"metrics\": {\"cos_sim_mean\": 0.0045, \"cos_sim_std\": 0.07, \"neg_cos_sim_layers_pct\": 53.1, \"mag_ratio_median\": 25.7, \"conclusion_note\": \"cos_sim≈0 indicates near-orthogonal (NOT conflict). Script conclusion text 'widespread conflict' is misleading — actual finding: NTP and GAR gradients are nearly orthogonal on Llama, consistent with Qwen pattern.\"}}}, \"count\": 10, \"total\": 60, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.1632}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ec08cdd2-0b56-4a26-82eb-377ddfe6e0dc",
  "isSidechain": false,
  "promptId": "8d8464e4-1523-464c-8d63-5cd7db13bd3f",
  "type": "user",
  "uuid": "b3a6de15-ebfb-4c54-84d0-3854c904105d",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {\\\"phase1a_multiseed_qwen\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-25T06:15:26.051Z\\\", \\\"hypothesis\\\": \\\"Multi-seed (s123, s456) training across 5 Qwen conditions (PCGrad, UG, LoRA-only, TG, SS) to establish mean±std for all claims. 8 training runs + AR eval N≥50 each. Expect TF convergence (GAR~0.50) and consistent AR rankings across seeds.\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"p1_ss_lora_only\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-25T08:58:41.419Z\\\", \\\"hypothesis\\\": \\\"SS training on LoRA-only checkpoint (no ThreadGate) with same hyperparameters (rho_max=0.3, same schedule) should achieve similar GAR improvement as SS+TG. If confirmed, this proves the SS fix is architecture-agnostic, strengthening the paper's mitigation story (the gap is caused by exposure bias in any auxiliary-loss setup, and SS fixes it regardless of gating mechanism).\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"phase2_switching\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-25T08:58:40.187Z\\\", \\\"hypothesis\\\": \\\"TF→AR switching at turn k (k=1..5) on ThreadGate s42 checkpoint. If GAR drops abruptly at the switch point (matching pure-AR level within 1 turn), it confirms exposure bias as instantaneous distribution shift rather than gradual KV cache drift. Staircase = exposure bias dominant; linear slope = KV drift dominant.\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"phase2_tf_ar_switching\\\": {\\\"status\\\": \\\"QUEUED\\\", \\\"created_at\\\": \\\"2026-05-25T06:15:36.221Z\\\", \\\"hypothesis\\\": \\\"TF→AR switching at turn k (k=1..5) on ThreadGate s42 checkpoint. If GAR drops abruptly at the switch point (matching pure-AR level within 1 turn), it confirms exposure bias as instantaneous distribution shift rather than gradual cumulative drift.\\\"}, \\\"phase1a_multiseed_8runs\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"created_at\\\": \\\"2026-05-25T06:18:08.953Z\\\"}, \\\"phase1b_llama_complement\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"created_at\\\": \\\"2026-05-25T06:15:34.729Z\\\", \\\"hypothesis\\\": \\\"Llama PCGrad + UG (s42) to complete cross-model comparison matrix. If Llama PCGrad also fails to improve AR GAR (like Qwen), it strengthens the cross-architecture causal exclusion of gradient conflict.\\\"}, \\\"p1_llama_ss_eval\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-24T15:53:29.650Z\\\", \\\"hypothesis\\\": \\\"Llama SS (2-epoch) reduces the TF-AR GAR gap on Llama-3.1-8B, confirming SS as model-general mitigation (C4+C5). Eval: TF+AR N=50 β=0/3/5.\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"ss_tf_gar\\\": 0.477, \\\"ss_tf_ppl\\\": 2.82, \\\"ss_ar_b0_gar\\\": 0.1662, \\\"ss_ar_b0_ppl\\\": 1.37, \\\"ss_ar_b5_gar\\\": 0.7905, \\\"ss_ar_b5_ppl\\\": 1.81, \\\"base_ar_gar\\\": 0.0179, \\\"base_ar_ppl\\\": 1.22, \\\"tf_ar_gap\\\": 2.87}}, \\\"p1_llama_ss_training\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-23T19:37:48.689Z\\\", \\\"hypothesis\\\": \\\"SS is effective on Qwen (gap 8x to 1.4x). If SS also reduces the TF-AR gap on Llama-3.1-8B, it confirms SS as a model-general mitigation, strengthening C4 (mitigation) and C5 (cross-model) claims.\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"mmlu_eval_all\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-23T06:45:04.153Z\\\", \\\"hypothesis\\\": \\\"ThreadGate's per-layer gating and auxiliary GAR loss do not degrade the model's general language understanding capabilities. All fine-tuned variants (TG/UG/LO/PCGrad/SS) should maintain MMLU 5-shot accuracy within 1pp of the Base LoRA-only checkpoint, confirming that attention steering is additive rather than destructive.\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"base_qwen\\\": 0.7423, \\\"pcgrad_v9_s42\\\": 0.7386, \\\"ss_v8b_s42\\\": 0.7375, \\\"lo_s42\\\": 0.7357, \\\"tg_v7_s42\\\": 0.7347, \\\"ug_s42\\\": 0.7346}}, \\\"p2_llama_gradient_conflict\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-23T19:37:50.492Z\\\", \\\"hypothesis\\\": \\\"PCGrad fails to improve AR GAR on Llama-3.1-8B (as on Qwen), confirming cross-model that gradient conflict is not the root cause of the TF-AR gap, strengthening C2 (causal exclusion).\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"cos_sim_mean\\\": 0.0045, \\\"cos_sim_std\\\": 0.07, \\\"neg_cos_sim_layers_pct\\\": 53.1, \\\"mag_ratio_median\\\": 25.7, \\\"conclusion_note\\\": \\\"cos_sim≈0 indicates near-orthogonal (NOT conflict). Script conclusion text 'widespread conflict' is misleading — actual finding: NTP and GAR gradients are nearly orthogonal on Llama, consistent with Qwen pattern.\\\"}}}, \\\"count\\\": 10, \\\"total\\\": 60, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.1632}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {\"phase1a_multiseed_qwen\": {\"status\": \"DONE\", \"created_at\": \"2026-05-25T06:15:26.051Z\", \"hypothesis\": \"Multi-seed (s123, s456) training across 5 Qwen conditions (PCGrad, UG, LoRA-only, TG, SS) to establish mean±std for all claims. 8 training runs + AR eval N≥50 each. Expect TF convergence (GAR~0.50) and consistent AR rankings across seeds.\", \"conclusion\": \"killed\"}, \"p1_ss_lora_only\": {\"status\": \"DONE\", \"created_at\": \"2026-05-25T08:58:41.419Z\", \"hypothesis\": \"SS training on LoRA-only checkpoint (no ThreadGate) with same hyperparameters (rho_max=0.3, same schedule) should achieve similar GAR improvement as SS+TG. If confirmed, this proves the SS fix is architecture-agnostic, strengthening the paper's mitigation story (the gap is caused by exposure bias in any auxiliary-loss setup, and SS fixes it regardless of gating mechanism).\", \"conclusion\": \"killed\"}, \"phase2_switching\": {\"status\": \"DONE\", \"created_at\": \"2026-05-25T08:58:40.187Z\", \"hypothesis\": \"TF→AR switching at turn k (k=1..5) on ThreadGate s42 checkpoint. If GAR drops abruptly at the switch point (matching pure-AR level within 1 turn), it confirms exposure bias as instantaneous distribution shift rather than gradual KV cache drift. Staircase = exposure bias dominant; linear slope = KV drift dominant.\", \"conclusion\": \"killed\"}, \"phase2_tf_ar_switching\": {\"status\": \"QUEUED\", \"created_at\": \"2026-05-25T06:15:36.221Z\", \"hypothesis\": \"TF→AR switching at turn k (k=1..5) on ThreadGate s42 checkpoint. If GAR drops abruptly at the switch point (matching pure-AR level within 1 turn), it confirms exposure bias as instantaneous distribution shift rather than gradual cumulative drift.\"}, \"phase1a_multiseed_8runs\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-25T06:18:08.953Z\"}, \"phase1b_llama_complement\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-25T06:15:34.729Z\", \"hypothesis\": \"Llama PCGrad + UG (s42) to complete cross-model comparison matrix. If Llama PCGrad also fails to improve AR GAR (like Qwen), it strengthens the cross-architecture causal exclusion of gradient conflict.\"}, \"p1_llama_ss_eval\": {\"status\": \"DONE\", \"created_at\": \"2026-05-24T15:53:29.650Z\", \"hypothesis\": \"Llama SS (2-epoch) reduces the TF-AR GAR gap on Llama-3.1-8B, confirming SS as model-general mitigation (C4+C5). Eval: TF+AR N=50 β=0/3/5.\", \"conclusion\": \"success\", \"metrics\": {\"ss_tf_gar\": 0.477, \"ss_tf_ppl\": 2.82, \"ss_ar_b0_gar\": 0.1662, \"ss_ar_b0_ppl\": 1.37, \"ss_ar_b5_gar\": 0.7905, \"ss_ar_b5_ppl\": 1.81, \"base_ar_gar\": 0.0179, \"base_ar_ppl\": 1.22, \"tf_ar_gap\": 2.87}}, \"p1_llama_ss_training\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T19:37:48.689Z\", \"hypothesis\": \"SS is effective on Qwen (gap 8x to 1.4x). If SS also reduces the TF-AR gap on Llama-3.1-8B, it confirms SS as a model-general mitigation, strengthening C4 (mitigation) and C5 (cross-model) claims.\", \"conclusion\": \"success\"}, \"mmlu_eval_all\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T06:45:04.153Z\", \"hypothesis\": \"ThreadGate's per-layer gating and auxiliary GAR loss do not degrade the model's general language understanding capabilities. All fine-tuned variants (TG/UG/LO/PCGrad/SS) should maintain MMLU 5-shot accuracy within 1pp of the Base LoRA-only checkpoint, confirming that attention steering is additive rather than destructive.\", \"conclusion\": \"success\", \"metrics\": {\"base_qwen\": 0.7423, \"pcgrad_v9_s42\": 0.7386, \"ss_v8b_s42\": 0.7375, \"lo_s42\": 0.7357, \"tg_v7_s42\": 0.7347, \"ug_s42\": 0.7346}}, \"p2_llama_gradient_conflict\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T19:37:50.492Z\", \"hypothesis\": \"PCGrad fails to improve AR GAR on Llama-3.1-8B (as on Qwen), confirming cross-model that gradient conflict is not the root cause of the TF-AR gap, strengthening C2 (causal exclusion).\", \"conclusion\": \"success\", \"metrics\": {\"cos_sim_mean\": 0.0045, \"cos_sim_std\": 0.07, \"neg_cos_sim_layers_pct\": 53.1, \"mag_ratio_median\": 25.7, \"conclusion_note\": \"cos_sim≈0 indicates near-orthogonal (NOT conflict). Script conclusion text 'widespread conflict' is misleading — actual finding: NTP and GAR gradients are nearly orthogonal on Llama, consistent with Qwen pattern.\"}}}, \"count\": 10, \"total\": 60, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.1632}}"
    }
  },
  "sourceToolAssistantUUID": "ec08cdd2-0b56-4a26-82eb-377ddfe6e0dc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921",
  "sessionId": "5d779602-0719-4d06-8bf9-fdd84990d5d0",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---


### Runtime record

_source line 151 · 2026-05-25T20:44:25.088Z_

```json
{
  "parentUuid": "b3a6de15-ebfb-4c54-84d0-3854c904105d",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "214c042c-4d9f-473c-ae38-cf62bbaa4d56",
  "timestamp": "2026-05-25T20:44:25.088Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921",
  "sessionId": "5d779602-0719-4d06-8bf9-fdd84990d5d0",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---


### Assistant

_source line 152 · 2026-05-25T20:44:31.356Z_

<details><summary>Logged reasoning block</summary>

```text
I see the registry now has 60 experiments total, up from 53 before. Let me search specifically for any new TG s123 eval experiment with N=50.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "214c042c-4d9f-473c-ae38-cf62bbaa4d56",
  "isSidechain": false,
  "requestId": "req_011CbPwRtxfwwBdqBEdVrgzZ",
  "type": "assistant",
  "uuid": "611127f9-f4d0-4db9-9041-4e5a33d175de",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921",
  "sessionId": "5d779602-0719-4d06-8bf9-fdd84990d5d0",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KDt5N7koGTkyUJvoMBQ1mg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3741,
      "cache_read_input_tokens": 124277,
      "output_tokens": 352,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3741,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 352,
          "cache_read_input_tokens": 124277,
          "cache_creation_input_tokens": 3741,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3741
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

_source line 153 · 2026-05-25T20:44:34.699Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01TQjKqRq5KEenrSPKxUZQFf`</summary>

```json
{
  "pattern": "tg.*s123.*n50|d048.*tg.*s123|eval.*tg.*s123.*50",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "glob": "registry.yaml",
  "output_mode": "content",
  "-i": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "611127f9-f4d0-4db9-9041-4e5a33d175de",
  "isSidechain": false,
  "requestId": "req_011CbPwRtxfwwBdqBEdVrgzZ",
  "type": "assistant",
  "uuid": "8c9a9e17-4646-4e0a-b88e-54d4e26a7f30",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921",
  "sessionId": "5d779602-0719-4d06-8bf9-fdd84990d5d0",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KDt5N7koGTkyUJvoMBQ1mg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3741,
      "cache_read_input_tokens": 124277,
      "output_tokens": 352,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3741,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 352,
          "cache_read_input_tokens": 124277,
          "cache_creation_input_tokens": 3741,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3741
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

_source line 154 · 2026-05-25T20:44:34.739Z_

<details><summary>↩ Tool result · `toolu_01TQjKqRq5KEenrSPKxUZQFf`</summary>

```text
No matches found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8c9a9e17-4646-4e0a-b88e-54d4e26a7f30",
  "isSidechain": false,
  "promptId": "8d8464e4-1523-464c-8d63-5cd7db13bd3f",
  "type": "user",
  "uuid": "6c3f033f-6a4d-4359-8aa4-5604bf674696",
  "toolUseResult": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "",
    "numLines": 0
  },
  "sourceToolAssistantUUID": "8c9a9e17-4646-4e0a-b88e-54d4e26a7f30",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921",
  "sessionId": "5d779602-0719-4d06-8bf9-fdd84990d5d0",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---


### Tool result

_source line 155 · 2026-05-25T20:44:35.584Z_

<details><summary>↩ Tool result · `toolu_01MiXzVwAmTB6jKoq4g1cSae`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/registry.yaml:820:      从 -0.061→+0.055→-0.035 (围绕 0 振荡), NTP mag_ratio 2.8→28.8 持续增长。L_GAR 有 0-350
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6429312d-8a05-4791-82d4-93be50dda8ba",
  "isSidechain": false,
  "promptId": "8d8464e4-1523-464c-8d63-5cd7db13bd3f",
  "type": "user",
  "uuid": "4e33b6df-91de-4cbf-80e9-c4087f218b4d",
  "toolUseResult": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/registry.yaml:820:      从 -0.061→+0.055→-0.035 (围绕 0 振荡), NTP mag_ratio 2.8→28.8 持续增长。L_GAR 有 0-350",
    "numLines": 1
  },
  "sourceToolAssistantUUID": "6429312d-8a05-4791-82d4-93be50dda8ba",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921",
  "sessionId": "5d779602-0719-4d06-8bf9-fdd84990d5d0",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---


### Tool call

_source line 156 · 2026-05-25T20:44:35.563Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01MiXzVwAmTB6jKoq4g1cSae`</summary>

```json
{
  "pattern": "0\\.055",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "glob": "registry.yaml",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6c3f033f-6a4d-4359-8aa4-5604bf674696",
  "isSidechain": false,
  "requestId": "req_011CbPwRtxfwwBdqBEdVrgzZ",
  "type": "assistant",
  "uuid": "6429312d-8a05-4791-82d4-93be50dda8ba",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921",
  "sessionId": "5d779602-0719-4d06-8bf9-fdd84990d5d0",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KDt5N7koGTkyUJvoMBQ1mg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3741,
      "cache_read_input_tokens": 124277,
      "output_tokens": 352,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3741,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 352,
          "cache_read_input_tokens": 124277,
          "cache_creation_input_tokens": 3741,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3741
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

_source line 157_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[服务器重启后首条消息] 当前日期: 2026-05-25。服务器刚重启，项目状态可能已更新。在处理审查请求前，**先读取 registry.yaml 和 report.md** 获取最新实验状态，不要依赖对话历史中的状态信息。  **审查请求：** [系统通知 — worker_done:worker_fix_audit_appendix_issues_20260525T203522]: Wor…",
  "leafUuid": "4e33b6df-91de-4cbf-80e9-c4087f218b4d",
  "sessionId": "5d779602-0719-4d06-8bf9-fdd84990d5d0"
}
```

---


### Runtime record

_source line 158_

```json
{
  "type": "ai-title",
  "aiTitle": "Review worker audit appendix tables completion",
  "sessionId": "5d779602-0719-4d06-8bf9-fdd84990d5d0"
}
```

---


### Assistant

_source line 159 · 2026-05-25T20:45:01.634Z_

<details><summary>Logged reasoning block</summary>

```text
The 0.055 in the registry is from a different context (gradient analysis, not AR GAR). There is NO registry entry for a TG s123 N=50 AR eval, and 0.055 doesn't appear as an AR GAR value anywhere in the registry.

Let me also search the eval_v7_tg_s123 entry more carefully. Earlier I read: eval_v7_tg_s123 has modelgen_ar.gar_ours_mid = 0.0165, which is from N=5 eval.

So the number 0.055 in the appendix body text (line 635) is NOT supported by any registry entry. 

The closest registry values for TG s123 AR GAR are 0.0165 from the N=5 eval, with no N=50 eval existing for s123. This suggests the worker either fabricated the number, used an unreliable estimate, or pulled it from an unregistered eval—which is a significant issue. Let me check if 0.055 might come from the d048_final_ar_eval, which was a unified N=50 AR eval across six conditions using the s42 check.

But looking closer, the worker could've computed 0.055 by dividing TG s123 TF GAR (0.505) by the gap ratio (9.1×), giving 0.505/9.1 = 0.055—though that's circular reasoning since it assumes the gap rather than measuring AR GAR directly. The eval_v8b_ss_s123 and eval_v7_tg_s123 both used N=5 T=10 protocols, and d048_final_ar only evaluated s42 checkpoints anyway, so there's no legitimate N=50 source for s123 data.

The core problem is that 0.055 for TG s123 AR GAR has no registry entry to back it up, yet the body text now claims these N=50-based values while the per-seed TG table still shows the original N=5 results (0.016/0.017), creating a direct contradiction. Looking at what the worker actually fixed: the cross-model SS table mixing remains unfixed, the per-seed TG table still uses N=5 data, and the new body text introduces unsupported AR GAR claims that conflict with what's in the tables.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4e33b6df-91de-4cbf-80e9-c4087f218b4d",
  "isSidechain": false,
  "requestId": "req_011CbPwSg3p26xh8T4eucQyf",
  "type": "assistant",
  "uuid": "5af1a23f-80a5-40f9-a949-3d55f759b484",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921",
  "sessionId": "5d779602-0719-4d06-8bf9-fdd84990d5d0",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011uLp555ecmjx17UFwHeG5J",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 509,
      "cache_read_input_tokens": 128018,
      "output_tokens": 1017,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 509,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1017,
          "cache_read_input_tokens": 128018,
          "cache_creation_input_tokens": 509,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 509
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

_source line 160 · 2026-05-25T20:45:02.518Z_

TG s123 AR GAR = 0.055 在 registry 中不存在。这是一个严重问题。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5af1a23f-80a5-40f9-a949-3d55f759b484",
  "isSidechain": false,
  "requestId": "req_011CbPwSg3p26xh8T4eucQyf",
  "type": "assistant",
  "uuid": "b76b1e56-9d03-4b56-96bb-eee023c66a76",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921",
  "sessionId": "5d779602-0719-4d06-8bf9-fdd84990d5d0",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011uLp555ecmjx17UFwHeG5J",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 509,
      "cache_read_input_tokens": 128018,
      "output_tokens": 1017,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 509,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1017,
          "cache_read_input_tokens": 128018,
          "cache_creation_input_tokens": 509,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 509
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

_source line 161 · 2026-05-25T20:45:03.494Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_018SY8B4PXhJ4SbkJDQHSXNR`</summary>

```json
{
  "project": "turn_residual_gating",
  "limit": 0,
  "filters": {
    "status": "DONE"
  },
  "fields": [
    "status",
    "hypothesis",
    "metrics",
    "conclusion"
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b76b1e56-9d03-4b56-96bb-eee023c66a76",
  "isSidechain": false,
  "requestId": "req_011CbPwSg3p26xh8T4eucQyf",
  "type": "assistant",
  "uuid": "258a34c5-fde4-475f-b756-8ca103ab93ef",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921",
  "sessionId": "5d779602-0719-4d06-8bf9-fdd84990d5d0",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011uLp555ecmjx17UFwHeG5J",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 509,
      "cache_read_input_tokens": 128018,
      "output_tokens": 1017,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 509,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1017,
          "cache_read_input_tokens": 128018,
          "cache_creation_input_tokens": 509,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 509
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

_source line 162 · 2026-05-25T20:45:03.691Z_

<details><summary>↩ Tool result · `toolu_018SY8B4PXhJ4SbkJDQHSXNR`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {\"phase1a_multiseed_qwen\": {\"status\": \"DONE\", \"hypothesis\": \"Multi-seed (s123, s456) training across 5 Qwen conditions (PCGrad, UG, LoRA-only, TG, SS) to establish mean±std for all claims. 8 training runs + AR eval N≥50 each. Expect TF convergence (GAR~0.50) and consistent AR rankings across seeds.\", \"conclusion\": \"killed\"}, \"p1_ss_lora_only\": {\"status\": \"DONE\", \"hypothesis\": \"SS training on LoRA-only checkpoint (no ThreadGate) with same hyperparameters (rho_max=0.3, same schedule) should achieve similar GAR improvement as SS+TG. If confirmed, this proves the SS fix is architecture-agnostic, strengthening the paper's mitigation story (the gap is caused by exposure bias in any auxiliary-loss setup, and SS fixes it regardless of gating mechanism).\", \"conclusion\": \"killed\"}, \"phase2_switching\": {\"status\": \"DONE\", \"hypothesis\": \"TF→AR switching at turn k (k=1..5) on ThreadGate s42 checkpoint. If GAR drops abruptly at the switch point (matching pure-AR level within 1 turn), it confirms exposure bias as instantaneous distribution shift rather than gradual KV cache drift. Staircase = exposure bias dominant; linear slope = KV drift dominant.\", \"conclusion\": \"killed\"}, \"p1_llama_ss_eval\": {\"status\": \"DONE\", \"hypothesis\": \"Llama SS (2-epoch) reduces the TF-AR GAR gap on Llama-3.1-8B, confirming SS as model-general mitigation (C4+C5). Eval: TF+AR N=50 β=0/3/5.\", \"conclusion\": \"success\", \"metrics\": {\"ss_tf_gar\": 0.477, \"ss_tf_ppl\": 2.82, \"ss_ar_b0_gar\": 0.1662, \"ss_ar_b0_ppl\": 1.37, \"ss_ar_b5_gar\": 0.7905, \"ss_ar_b5_ppl\": 1.81, \"base_ar_gar\": 0.0179, \"base_ar_ppl\": 1.22, \"tf_ar_gap\": 2.87}}, \"p1_llama_ss_training\": {\"status\": \"DONE\", \"hypothesis\": \"SS is effective on Qwen (gap 8x to 1.4x). If SS also reduces the TF-AR gap on Llama-3.1-8B, it confirms SS as a model-general mitigation, strengthening C4 (mitigation) and C5 (cross-model) claims.\", \"conclusion\": \"success\"}, \"mmlu_eval_all\": {\"status\": \"DONE\", \"hypothesis\": \"ThreadGate's per-layer gating and auxiliary GAR loss do not degrade the model's general language understanding capabilities. All fine-tuned variants (TG/UG/LO/PCGrad/SS) should maintain MMLU 5-shot accuracy within 1pp of the Base LoRA-only checkpoint, confirming that attention steering is additive rather than destructive.\", \"conclusion\": \"success\", \"metrics\": {\"base_qwen\": 0.7423, \"pcgrad_v9_s42\": 0.7386, \"ss_v8b_s42\": 0.7375, \"lo_s42\": 0.7357, \"tg_v7_s42\": 0.7347, \"ug_s42\": 0.7346}}, \"p2_llama_gradient_conflict\": {\"status\": \"DONE\", \"hypothesis\": \"PCGrad fails to improve AR GAR on Llama-3.1-8B (as on Qwen), confirming cross-model that gradient conflict is not the root cause of the TF-AR gap, strengthening C2 (causal exclusion).\", \"conclusion\": \"success\", \"metrics\": {\"cos_sim_mean\": 0.0045, \"cos_sim_std\": 0.07, \"neg_cos_sim_layers_pct\": 53.1, \"mag_ratio_median\": 25.7, \"conclusion_note\": \"cos_sim≈0 indicates near-orthogonal (NOT conflict). Script conclusion text 'widespread conflict' is misleading — actual finding: NTP and GAR gradients are nearly orthogonal on Llama, consistent with Qwen pattern.\"}}, \"p1_tf_ar_kl_divergence\": {\"status\": \"DONE\", \"hypothesis\": \"TF and AR attention distributions diverge more on GAR-relevant heads (high gate values) than non-relevant heads, providing mechanistic evidence that exposure bias selectively disrupts goal-attending computation rather than uniformly degrading attention.\", \"metrics\": {\"tg_delta_gar\": 0.0165, \"base_delta_gar\": 0.0122, \"tg_mean_kl\": 0.054, \"base_mean_kl\": 0.043, \"gate_kl_correlation\": 0.11, \"high_kl_layers\": \"L23-L27, L9\", \"gar_robustness_ours_tg_base_ratio\": 21.4, \"gar_robustness_goal_only_ratio\": 63, \"gar_robustness_ours_all_ratio\": 1.7, \"gar_robustness_ours_first_ratio\": 1.8}, \"conclusion\": \"success\"}, \"qwen15b_phase1_diag\": {\"status\": \"DONE\", \"hypothesis\": \"GAR attention decay toward system-prompt goal tokens is a general phenomenon across model scales, not specific to 7B. Qwen-2.5-1.5B-Instruct should also show progressive GAR decline across conversation turns, confirming the phenomenon is architecture-level rather than scale-dependent.\", \"conclusion\": \"success\"}, \"d048_eval_ss_s456\": {\"status\": \"DONE\", \"hypothesis\": \"SS s456 eval: TF + AR N=50 + bootstrap CI to complete 3-seed SS metrics. Together with s42 and s123, establishes mean±std for C2 reviewer requirement.\", \"conclusion\": \"success\", \"metrics\": {\"tf_gar_ours_mid\": 0.4964, \"tf_gar_dongre_mid\": 0.3862, \"ar_beta0_gar\": 0.4325, \"ar_beta0_ppl\": 1.4394, \"ar_beta3_gar\": 0.605, \"ar_beta3_ppl\": 1.5868, \"ar_beta5_gar\": 0.7157, \"ar_beta5_ppl\": 1.8045, \"n_convs_ar\": 50}}, \"d048_ss_s456\": {\"status\": \"DONE\", \"hypothesis\": \"Scheduled sampling (ratio=0.3) with ThreadGate multi-seed (s456) to establish 3-seed mean±std for C2 reviewer requirement of at least 3 seeds\", \"conclusion\": \"success\"}, \"d048_eval_ss_s123\": {\"status\": \"DONE\", \"hypothesis\": \"SS s123 eval: TF + AR N=50 + bootstrap CI to establish multi-seed SS metrics. Expect TF GAR ~0.50, AR GAR similar to s42 (0.347), confirming SS effectiveness across seeds.\", \"conclusion\": \"success\", \"metrics\": {\"tf_gar_ours\": 0.5536, \"tf_gar_dongre\": 0.4106, \"tf_ppl\": 2.6123, \"ar_beta0_gar\": 0.4231, \"ar_beta0_ppl\": 1.4408, \"ar_beta3_gar\": 0.5903, \"ar_beta3_ppl\": 1.607, \"ar_beta5_gar\": 0.7174, \"ar_beta5_ppl\": 1.7852, \"n_convs_tf\": 200, \"n_convs_ar\": 39}}, \"d048_ss_s123\": {\"status\": \"DONE\", \"hypothesis\": \"Scheduled sampling (ratio=0.3) with ThreadGate multi-seed (s123) to establish 3-seed mean±std for C2 reviewer requirement. Corrected hyperparams matching d048_ss_s456.\", \"conclusion\": \"success\"}, \"d048_split_softmax_eval\": {\"status\": \"DONE\", \"hypothesis\": \"Split-softmax (Li et al., COLM 2024) post-softmax rescaling recovers AR GAR without the PPL cost of pre-softmax additive steering, providing an alternative inference-time intervention that separates attention allocation from logit distribution.\", \"conclusion\": \"failed\"}, \"d048_final_ar_eval\": {\"status\": \"DONE\", \"hypothesis\": \"Unified AR N=50 eval across 6 conditions (Base/TG/UG/LO/PCGrad/SS) with bootstrap CI and Wilcoxon tests to establish statistically rigorous comparisons for all claims\", \"conclusion\": \"success\", \"metrics\": {\"beta0\": {\"base_gar\": 0.019, \"tg_gar\": 0.064, \"ug_gar\": 0.033, \"lo_gar\": 0.037, \"pcgrad_gar\": 0.03, \"ss_gar\": 0.347}, \"beta3\": {\"base_gar\": 0.531, \"tg_gar\": 0.556, \"ss_gar\": 0.593}, \"beta5\": {\"base_gar\": 0.704, \"tg_gar\": 0.727, \"ss_gar\": 0.717}, \"wilcoxon_beta0\": {\"tg_vs_base_p\": \"<0.001\", \"tg_vs_base_r\": 0.802, \"ss_vs_tg_p\": \"<0.001\", \"ss_vs_tg_r\": 0.869}, \"ppl\": {\"base\": 1.447, \"tg\": 1.432, \"ss\": 1.442}, \"n_convs\": 39}}, \"d048_eval_ss_s42\": {\"status\": \"DONE\", \"hypothesis\": \"D048 multi-seed SS s42 eval: TF + AR N=50 + bootstrap CI (curve[2:]) to establish mean±std for scheduled sampling. Expect TF GAR ~0.50, AR GAR gap < 2× (vs base ~31×), PPL stable.\", \"metrics\": {\"tf\": {\"base_gar_ours_mid\": 0.0128, \"base_gar_dongre_mid\": 0.0031, \"base_ppl\": 4.34, \"base_ntp\": 1.4, \"tg_gar_ours_mid\": 0.5025, \"tg_gar_dongre_mid\": 0.389, \"tg_ppl\": 2.78, \"tg_ntp\": 0.98, \"baseline_mid_gar\": 0.0122}, \"ar\": {\"gar_ours_mid\": 0.3887, \"gar_ours_ci_95\": [0.3692, 0.3934], \"ppl\": 1.35}, \"gap_ratio\": 1.29, \"n_conversations_tf\": 50, \"n_conversations_ar\": 5, \"bootstrap_turns\": \"curve[2:] (turns 3-T)\", \"note\": \"AR used hardcoded N=5, not N=50. Will be re-evaluated in final unified batch with eval_200.json N=50.\"}, \"conclusion\": \"success\"}, \"d048_ss_s42\": {\"status\": \"DONE\", \"hypothesis\": \"Scheduled sampling (ratio=0.3) with ThreadGate reduces the ~30× TF-AR GAR gap by exposing the model to its own generated text during training. Multi-seed run (s42) under D048 unified protocol to establish mean±std for statistical testing. SS is the strongest mitigation candidate (prior single-seed showed gap 31×→1.57×).\", \"conclusion\": \"success\", \"metrics\": {\"final_avg_loss\": 0.9326, \"final_ntp_loss\": 0.932, \"final_gar_loss\": 0.0007, \"gate_mean\": 0.9527, \"gate_std\": 0.0589, \"gate_min\": 0.7383, \"gate_min_layer\": \"L4\", \"gate_max\": 1, \"ss_usage\": \"4750/16000 (29.7%)\", \"ss_fallback\": 0, \"epochs_completed\": 3, \"wall_clock_s\": 23418, \"wall_clock_h\": 6.5}}, \"eval_llama_ar_n20\": {\"status\": \"DONE\", \"hypothesis\": \"N=20 AR eval stabilizes Llama 3-way (Base/TG/LoRA-only) autoregressive GAR estimates. N=5 suffered from outlier influence (3/5 conv had GAR>0.4 outlier turns); N=20 provides robust mean±std.\", \"metrics\": {\"base\": {\"gar_ours_mean\": 0.0088, \"gar_ours_std\": 0.0056, \"gar_ours_median_per_conv\": 0.0093, \"gar_ours_median_per_turn_pool\": 0.0071, \"gar_ours_spike_ratio\": \"0%\", \"gar_dongre_mean\": 0.0049, \"gar_dongre_std\": 0.0013, \"gar_dongre_median\": 0.0047, \"ngar_ours_mid\": 0.1019, \"ngar_dongre_mid\": 0.1171, \"ppl\": 1.293, \"ppl_std\": 0.07, \"ntp_loss\": 0.2552}, \"tg\": {\"gar_ours_mean\": 0.0434, \"gar_ours_std\": 0.1002, \"gar_ours_median_per_conv\": 0.0179, \"gar_ours_median_per_turn_pool\": 0.0126, \"gar_ours_spike_ratio\": \"5% (2/40 turns GAR>=0.4)\", \"gar_dongre_mean\": 0.0183, \"gar_dongre_std\": 0.0198, \"gar_dongre_median\": 0.0152, \"ngar_ours_mid\": 0.5357, \"ngar_dongre_mid\": 0.4436, \"ppl\": 1.437, \"ppl_std\": 0.077, \"ntp_loss\": 0.3612}, \"lora_only\": {\"gar_ours_mean\": 0.0284, \"gar_ours_std\": 0.0481, \"gar_ours_median_per_conv\": 0.0184, \"gar_ours_median_per_turn_pool\": 0.0133, \"gar_ours_spike_ratio\": \"0%\", \"gar_dongre_mean\": 0.0205, \"gar_dongre_std\": 0.0241, \"gar_dongre_median\": 0.016, \"ngar_ours_mid\": 0.3488, \"ngar_dongre_mid\": 0.4997, \"ppl\": 1.419, \"ppl_std\": 0.075, \"ntp_loss\": 0.3483}, \"n_conversations\": 20, \"n_turns\": 4, \"mid_turns_definition\": \"turns 3-T (0-indexed avg_gar[2:], excluding turns 1-2). All 16 eval entries use same definition.\", \"stat_pool\": \"median_per_conv: median of 20 per-conversation mid-turn averages. median_per_turn_pool: median of 40 individual turn values (20 conv x 2 mid turns).\", \"ranking_gar_ours_mean\": \"TG(0.0434) > LO(0.0284) > Base(0.0088)\", \"ranking_gar_ours_median_per_conv\": \"TG(0.0179) ≈ LO(0.0184) > Base(0.0093)\", \"ranking_gar_ours_median_per_turn_pool\": \"TG(0.0126) ≈ LO(0.0133) > Base(0.0071)\", \"ranking_gar_dongre\": \"LO(0.0205) > TG(0.0183) > Base(0.0049)\", \"note\": \"Paper §5.5 cites median_per_conv (median of per-conversation mid-turn averages across N=20). median_per_turn_pool is the alternative statistic from pooled individual turns. Both confirm TG ≈ LO (zero-increment).\"}, \"conclusion\": \"success\"}, \"eval_llama_lora_only_s42\": {\"status\": \"DONE\", \"hypothesis\": \"LoRA-only ablation (no gate) on Llama-3.1-8B: if TG's GAR improvement comes from the gate, LoRA-only should show minimal GAR recovery vs base.\", \"metrics\": {\"tf\": {\"gar_ours\": 0.4807, \"gar_dongre\": 0.0188, \"ngar_ours\": 11.8031, \"ngar_dongre\": 0.8261, \"ppl\": 2.6, \"ntp_loss\": 0.9366, \"n_conversations\": 50, \"n_turns\": 4}, \"ar\": {\"gar_ours\": 0.0617, \"gar_dongre\": 0.0226, \"ngar_ours\": 0.6065, \"ngar_dongre\": 0.2537, \"ppl\": 1.32, \"ntp_loss\": 0.2787, \"n_conversations\": 5, \"n_turns\": 10}, \"gap_ratio_gar_ours\": 7.79}, \"conclusion\": \"success\"}, \"llama_lora_only_s42\": {\"status\": \"DONE\", \"hypothesis\": \"Llama-3.1-8B LoRA-only baseline (gate=none, 无 gating 机制): 与 Llama TG s42 对比，验证 gating 对 Llama 的增量贡献。如果 LoRA-only GAR ≈ TG GAR → gating 零增量与 Qwen 结论一致（C5 跨模型）。\", \"conclusion\": \"success\", \"metrics\": {\"final_avg_loss\": 0.9288, \"final_avg_ntp\": 0.9279, \"final_avg_gar\": 0.0009, \"gate_fixed\": 1, \"gate_type\": \"none\", \"wall_clock_s\": 25317, \"wall_clock_h\": 7.03, \"epochs_completed\": 3}}, \"phase2_tg_s42_v6\": {\"status\": \"DONE\", \"hypothesis\": \"smooth_saturation loss (-target*tanh(GAR/target), target=0.5) 提供有界但持续的 GAR 梯度，避免 maximize 的恒等退化（gate→1）和 hinge_target 的梯度消失（GAR达标后梯度=0）。预期：gate_std>0.05 的层间分化 + GAR 稳态在 0.3-0.5 + NTP loss 正常收敛 + 总 loss 为正。\", \"metrics\": {\"dryrun_step0_L_NTP\": 2.0275, \"dryrun_step0_L_GAR\": -0.0161, \"dryrun_step0_total_loss\": 2.0114, \"dryrun_step4_L_NTP\": 1.6544, \"dryrun_step4_L_GAR\": -0.0147, \"dryrun_step4_total_loss\": 1.6397, \"dryrun_gate_grad\": true, \"dryrun_gate_mean_init\": 0.8097, \"dryrun_gate_std_init\": 0.0341, \"dryrun_gate_min_init\": 0.6836, \"dryrun_gate_max_init\": 0.8672, \"dryrun_gate_mean_step5\": 0.8025, \"dryrun_gate_std_step5\": 0.0842, \"dryrun_gate_min_step5\": 0.5547, \"dryrun_gate_max_step5\": 0.9805, \"gs50_gate_mean\": 0.8117, \"gs50_gate_std\": 0.0612, \"gs50_gate_min\": 0.6836, \"gs50_gate_max\": 0.9805, \"gs100_gate_mean\": 0.8737, \"gs100_gate_std\": 0.0367, \"gs100_gate_min\": 0.8164, \"gs100_gate_max\": 0.9766, \"gs100_L_NTP\": 0.8151, \"gs100_L_GAR\": -0.158, \"gs100_total_loss\": 0.6571, \"gs100_profile_bottom3\": \"L12=0.816 L4=0.824 L13=0.824\", \"gs100_profile_top3\": \"L27=0.977 L26=0.961 L23=0.914\", \"gs143_L_GAR\": -0.3876, \"gs143_gate_mean\": 0.9227}, \"conclusion\": \"negative\"}, \"phase2_tg_s42\": {\"status\": \"DONE\", \"hypothesis\": \"ThreadGate (turn-conditional gating) 在 L_NTP+L_GAR 联合训练后，相比 Uniform Gate，mid-turn GAR recovery 高出 ≥3pp，验证 Cesaro 理论预测：position-conditional 干预优于 uniform 干预\", \"conclusion\": \"negative\", \"metrics\": {\"final_ntp_loss\": 0.94, \"final_gar_loss\": 0, \"gate_mean\": 0.988, \"gar_loss_zero_pct\": 87.6, \"epochs_completed\": 1.67, \"killed_reason\": \"SIGTERM by diagnose worker (unauthorized)\"}}, \"eval_v7_tg_s123\": {\"status\": \"DONE\", \"hypothesis\": \"v7 TG s123 eval: 验证 s123 seed 的 TF-AR GAR gap 与 s42 一致（~32×），确认 multi-seed robustness\", \"conclusion\": \"success\", \"metrics\": {\"iid_tf\": {\"gar_ours_mid\": 0.5052, \"gar_dongre_mid\": 0.0119, \"ppl\": 2.7802, \"ntp\": 0.9752}, \"modelgen_ar\": {\"gar_ours_mid\": 0.0165, \"gar_dongre_mid\": 0.0177, \"ppl\": 1.3855, \"ntp\": 0.3223}, \"gap_ratio\": 30.6, \"comparison_s42\": {\"tf_gar_ours_delta\": 0.0017, \"ar_gar_ours_delta\": 0.0008, \"gap_ratio_delta\": -1.4}}}, \"eval_v8b_ss_s123\": {\"status\": \"DONE\", \"hypothesis\": \"v8b SS model trained with s123 seed should reproduce s42 GAR metrics within acceptable gap_ratio [1.2x-2.5x] and no PPL degradation, confirming seed robustness of the scheduled sampling approach\", \"conclusion\": \"success\", \"metrics\": {\"iid\": {\"gar_ours\": 0.503, \"gar_dongre\": 0.394, \"ppl\": 2.781, \"ntp_loss\": 0.976, \"n_conv\": 50, \"n_turns\": 3}, \"modelgen\": {\"gar_ours\": 0.418, \"gar_dongre\": 0.441, \"ppl\": 1.389, \"ntp_loss\": 0.325, \"n_conv\": 5, \"n_turns\": 10}, \"gap_ratio\": 1.2, \"base_iid_ppl\": 4.338, \"base_modelgen_ppl\": 1.351}}, \"v7_tg_s123\": {\"status\": \"DONE\", \"hypothesis\": \"v7 TG s42 已验证 ThreadGate 有效性，s123 验证 seed robustness。预期 gate profile 和 GAR 收敛模式与 s42 一致。\", \"conclusion\": \"success\", \"metrics\": {\"epoch_1\": {\"avg_loss\": 0.9447, \"avg_ntp_loss\": 0.9434, \"avg_gar_loss\": 0.0013, \"avg_div_loss\": 0}, \"epoch_2\": {\"avg_loss\": 0.9315, \"avg_ntp_loss\": 0.9305, \"avg_gar_loss\": 0.001, \"avg_div_loss\": 0}, \"final_gate\": {\"mean\": 0.9467, \"std\": 0.051, \"min\": 0.793, \"max\": 1}, \"final_gate_profile\": {\"L0\": 0.883, \"L1\": 0.793, \"L2\": 0.996, \"L3\": 0.988, \"L4\": 0.984, \"L5\": 0.797, \"L6\": 0.961, \"L7\": 0.918, \"L8\": 0.965, \"L9\": 0.934, \"L10\": 0.969, \"L11\": 0.918, \"L12\": 0.926, \"L13\": 0.941, \"L14\": 0.93, \"L15\": 0.965, \"L16\": 0.941, \"L17\": 0.91, \"L18\": 0.961, \"L19\": 0.965, \"L20\": 0.973, \"L21\": 0.988, \"L22\": 0.969, \"L23\": 0.98, \"L24\": 0.98, \"L25\": 0.984, \"L26\": 0.988, \"L27\": 1}, \"training_time_s\": 21425.2}}, \"v8b_ss_s123\": {\"status\": \"DONE\", \"hypothesis\": \"v8b SS s42 成功（gap 32×→1.57×），s123 验证结果的 seed robustness。预期 model-gen GAR 同样显著提升，PPL 无恶化。\", \"conclusion\": \"success\", \"metrics\": {\"final_loss\": 0.9316, \"final_ntp_loss\": 0.9307, \"final_gar_loss\": 0.0009, \"final_gate_mean\": 0.9505, \"final_gate_std\": 0.0508, \"final_gate_min\": 0.7383, \"final_gate_max\": 1, \"ss_used_ratio\": 0.371, \"training_time_s\": 38773.4, \"epoch0_loss\": 1.0092, \"epoch1_loss\": 0.9444, \"epoch2_loss\": 0.9316}}, \"llama_ar_matched_eval\": {\"status\": \"DONE\", \"hypothesis\": \"用 matched 设置 (N=50/T=4) 重跑 Llama AR eval，消除 TF/AR 设置差异。与 TF 结果对比得到可直接写入论文的 gap ratio，验证 TG 在 AR 模式下仍能提升 GAR。\", \"conclusion\": \"success\", \"metrics\": {\"ar_base_ours\": {\"mid_gar\": 0.0082, \"ngar\": 0.1, \"ppl\": 1.267}, \"ar_tg_ours\": {\"mid_gar\": 0.0388, \"ngar\": 0.493, \"ppl\": 1.413}, \"ar_base_dongre\": {\"mid_gar\": 0.0051, \"ngar\": 0.12, \"ppl\": 1.267}, \"ar_tg_dongre\": {\"mid_gar\": 0.018, \"ngar\": 0.431, \"ppl\": 1.413}, \"tf_reference\": {\"tf_tg_ours_ngar\": 11.88, \"tf_base_ours_ngar\": 0.388, \"tf_tg_ours_raw\": 0.4836, \"tf_tg_dongre_raw\": 0.018}, \"matched_gap_analysis\": {\"gar_ours_raw_gap\": \"12.5x (TF 0.484 / AR 0.039)\", \"gar_ours_ngar_gap\": \"24.1x (TF 11.88 / AR 0.493)\", \"gar_dongre_raw_gap\": \"1.002x (TF 0.018 / AR 0.018) — zero gap\", \"tg_over_base_ar_ours\": \"4.71x\", \"tg_over_base_ar_dongre\": \"3.54x\", \"conclusion\": \"GAR-ours TF-AR gap 12.5x (raw) / 24x (nGAR) is genuine exposure bias. GAR-Dongre zero gap (1.002x) confirms mechanism specificity: exposure bias selectively destroys learned goal-attention routing while leaving content-overlap-based attention unaffected.\"}}}, \"instruction_retention_test\": {\"status\": \"DONE\", \"hypothesis\": \"Turn-level residual gating (β=3) preserves instruction-following ability across multi-turn conversations better than the baseline (β=0), because gating modulates residual contributions to retain earlier context signals rather than letting them decay through successive transformer layers.\", \"conclusion\": \"success\", \"metrics\": {\"late_turn_rate_beta0\": 0.759, \"late_turn_rate_beta3\": 0.87, \"late_turn_delta\": 0.111, \"mcnemar_chi2\": 3.125, \"mcnemar_p\": 0.0771, \"gar_compliance_r\": 0.2003, \"gar_compliance_p\": 0.007, \"category_content_constraint\": {\"beta0\": 0.619, \"beta3\": 0.857, \"delta\": 0.238}, \"category_count_constraint\": {\"beta0\": 1, \"beta3\": 1, \"delta\": 0}, \"category_format_constraint\": {\"beta0\": 1, \"beta3\": 1, \"delta\": 0}, \"category_position_constraint\": {\"beta0\": 0.667, \"beta3\": 0.733, \"delta\": 0.067}}}, \"llama_eval_s42\": {\"status\": \"DONE\", \"hypothesis\": \"Llama-3.1-8B TG eval: 如果 Llama TG 模型在 TF 模式下 GAR-ours 显著高于 AR 模式（如 Qwen v7 的 20-33x gap），则确认 training-inference GAR gap 跨模型泛化（C5）。同时测量 base model 作为 control。\", \"metrics\": {\"tf_base\": {\"gar_ours\": 0.0166, \"ngar_ours\": 0.3882, \"gar_dongre\": 0.0038, \"ngar_dongre\": 0.163, \"ppl\": 3.45, \"N\": 50, \"T\": 4}, \"tf_tg\": {\"gar_ours\": 0.4836, \"ngar_ours\": 11.8818, \"gar_dongre\": 0.018, \"ngar_dongre\": 0.7922, \"ppl\": 2.57, \"N\": 50, \"T\": 4}, \"ar_base\": {\"gar_ours\": 0.0086, \"ngar_ours\": 0.0798, \"gar_dongre\": 0.0118, \"ngar_dongre\": 0.1265, \"ppl\": 1.24, \"N\": 5, \"T\": 10}, \"ar_tg\": {\"gar_ours\": 0.0304, \"ngar_ours\": 0.2632, \"gar_dongre\": 0.0217, \"ngar_dongre\": 0.2459, \"ppl\": 1.32, \"N\": 5, \"T\": 10}, \"gap_ratio_tg_ours\": 15.9, \"gap_ratio_base_ours\": 1.93, \"gap_ratio_tg_dongre\": 0.83, \"vs_qwen_v7_gap_ratio\": 32.1, \"baseline_mid_gar\": 0.0122}, \"conclusion\": \"success\"}, \"llama_tg_s42\": {\"status\": \"DONE\", \"hypothesis\": \"在 Llama-3.1-8B-Instruct 上训练 ThreadGate（与 Qwen v7 相同配置），验证 C5：gating mechanism 和 GAR training-inference gap 跨模型泛化。如果 Llama TG 也出现 IID GAR ≈ target 但 model-gen GAR 坍塌 → 确认 exposure bias 的跨模型通用性。\", \"conclusion\": \"success\", \"metrics\": {\"epochs_completed\": 3, \"total_steps\": 3000, \"wall_clock_seconds\": 26212, \"wall_clock_hours\": 7.28, \"final_avg_loss\": 0.9233, \"final_avg_ntp\": 0.9224, \"final_avg_gar\": 0.0009, \"final_avg_div\": 0, \"final_gate_mean\": 0.9099, \"final_gate_std\": 0.0701, \"final_gate_min\": 0.7188, \"final_gate_max\": 0.9922, \"gate_profile_step3000\": {\"L0\": 0.957, \"L1\": 0.973, \"L2\": 0.977, \"L3\": 0.965, \"L4\": 0.992, \"L5\": 0.969, \"L6\": 0.957, \"L7\": 0.957, \"L8\": 0.961, \"L9\": 0.949, \"L10\": 0.938, \"L11\": 0.934, \"L12\": 0.969, \"L13\": 0.953, \"L14\": 0.957, \"L15\": 0.965, \"L16\": 0.953, \"L17\": 0.961, \"L18\": 0.922, \"L19\": 0.902, \"L20\": 0.883, \"L21\": 0.863, \"L22\": 0.836, \"L23\": 0.844, \"L24\": 0.809, \"L25\": 0.719, \"L26\": 0.762, \"L27\": 0.805, \"L28\": 0.801, \"L29\": 0.855, \"L30\": 0.898, \"L31\": 0.934}, \"checkpoint_size_gate_mb\": 4.2, \"checkpoint_size_lora_mb\": 26, \"gpu\": \"NVIDIA RTX PRO 6000 Blackwell\", \"vram_gb\": 102, \"mem_used_gb\": 63.4}}, \"attention_steering_gen_n50\": {\"status\": \"DONE\", \"hypothesis\": \"N=5 gen steering 显示 β∈[2,5] phase transition (GAR 0.06→0.68)，但样本量不足以报告置信区间。N=50 conversations 应重现同一 phase transition pattern 并提供统计鲁棒的 mean±std，加固 C6 claim (attention steering as causal mechanism proof)。\", \"metrics\": {\"corrected\": true, \"aggregation\": \"per-conv mid_gar(turns 2-7), >=3 turns only\", \"beta_0.0\": {\"mid_gar\": 0.0641, \"mid_gar_std\": 0.0809, \"ppl\": 1.4324, \"ppl_std\": 0.1029, \"n_valid\": 39}, \"beta_2.0\": {\"mid_gar\": 0.128, \"mid_gar_std\": 0.1101, \"ppl\": 1.4822, \"ppl_std\": 0.1385, \"n_valid\": 39}, \"beta_3.0\": {\"mid_gar\": 0.5558, \"mid_gar_std\": 0.0601, \"ppl\": 1.5605, \"ppl_std\": 0.1719, \"n_valid\": 39}, \"beta_4.0\": {\"mid_gar\": 0.6439, \"mid_gar_std\": 0.0607, \"ppl\": 1.6674, \"ppl_std\": 0.2241, \"n_valid\": 39}, \"beta_5.0\": {\"mid_gar\": 0.7271, \"mid_gar_std\": 0.0605, \"ppl\": 1.7723, \"ppl_std\": 0.2693, \"n_valid\": 38}, \"beta_10.0\": {\"mid_gar\": 0.9612, \"mid_gar_std\": 0.0152, \"ppl\": 3.4517, \"ppl_std\": 1.7813, \"n_valid\": 39}, \"n_convs_total\": 50, \"n_convs_valid\": 39, \"mode\": \"gen\", \"phase_transition_range\": \"[2, 3]\"}, \"conclusion\": \"success\"}, \"phase2_tg_s42_v8b_resume\": {\"status\": \"DONE\", \"hypothesis\": \"从 epoch_0 checkpoint resume v8b scheduled sampling 训练。SS 线性混合 0→0.5 teacher-forced + model-generated contexts。如果 model-gen context 上的 GAR 训练能缩小 30x training-inference gap → exposure bias mitigation 有效。成功标准：inference GAR 显著高于 v7 的 0.016 (至少 +1pp)，PPL 不恶化。\", \"metrics\": {\"training\": {\"total_steps\": 3000, \"epochs_completed\": 3, \"wall_clock_hours\": 8.1, \"final_loss\": 0.933, \"final_ntp_loss\": 0.9322, \"final_gar_loss\": 0.0008, \"final_gate_mean\": 0.9586, \"final_gate_std\": 0.0582, \"ss_ratio\": 0.5}, \"eval_iid\": {\"gar_ours\": 0.4983, \"gar_dongre\": 0.3855, \"ppl\": 2.78}, \"eval_modelgen\": {\"gar_ours\": 0.3177, \"gar_dongre\": 0.3533, \"ppl\": 1.38}, \"vs_v7\": {\"iid_gar_ours_delta\": -0.005, \"modelgen_gar_ours_delta\": 0.302, \"gap_ratio_v7\": 32, \"gap_ratio_v8b\": 1.57}}, \"conclusion\": \"success\"}, \"llama_phase1_gar_diag\": {\"status\": \"DONE\", \"hypothesis\": \"Llama-3.1-8B-Instruct 在 multi-turn dialogue 中也应出现 goal attention decay（与 Qwen-2.5-7B 类似），确认 attention decay 是 transformer 架构通用现象而非模型特有。Phase 1 诊断：测量 base Llama 的 per-turn GAR profile。\", \"conclusion\": \"success\", \"metrics\": {\"per_turn_gar\": {\"turn_1\": 0.0263, \"turn_2\": 0.0183, \"turn_3\": 0.0087, \"turn_4\": 0.0055, \"turn_5\": 0.006, \"turn_6\": 0.0035, \"turn_7\": 0.0038, \"turn_8\": 0.0037, \"turn_9\": 0.005, \"turn_10\": 0.0026}, \"t1_t10_decay_pct\": 90.1, \"t1_mid38_drop_pct\": 80.2, \"n_topics\": 5, \"model\": \"Meta-Llama-3.1-8B-Instruct\", \"mode\": \"gen\", \"n_conversations\": 5, \"n_turns\": 10}}, \"eval_v8b_ss\": {\"status\": \"DONE\", \"hypothesis\": \"Scheduled Sampling (linear 0→0.5 mixing of teacher-forced and model-gen contexts) closes the 30x training-inference GAR gap by reducing exposure bias, resulting in model-gen GAR significantly above v7 baseline (0.016) while preserving IID GAR and PPL.\", \"metrics\": {\"iid_gar_ours\": 0.4983, \"iid_gar_dongre\": 0.3855, \"iid_ppl\": 2.78, \"iid_ngar_ours\": 13.5, \"iid_ngar_dongre\": 22.68, \"modelgen_gar_ours\": 0.3177, \"modelgen_gar_dongre\": 0.3533, \"modelgen_ppl\": 1.38, \"modelgen_ngar_ours\": 4.47, \"modelgen_ngar_dongre\": 5.92, \"iid_turn1_gar_ours\": 0.5398, \"modelgen_turn1_gar_ours\": 0.4333}, \"conclusion\": \"success\"}, \"attention_steering_eval200_tf\": {\"status\": \"DONE\", \"hypothesis\": \"N=200 TF 模式 attention steering 验证 β-GAR 关系的统计鲁棒性。在 teacher-forced context (无 exposure bias) 下，steering 效果应更温和（baseline GAR 已 ~0.50），但仍展示 β 调控 attention 的能力。与 N=5 gen 模式结果互补：tf 验证机制可控性，gen 验证因果闭环。\", \"metrics\": {\"beta_0.0\": {\"mid_gar\": 0.5353, \"ppl\": 2.62}, \"beta_2.0\": {\"mid_gar\": 0.6112, \"ppl\": 2.69}, \"beta_3.0\": {\"mid_gar\": 0.788, \"ppl\": 2.93}, \"beta_4.0\": {\"mid_gar\": 0.8165, \"ppl\": 3.49}, \"beta_5.0\": {\"mid_gar\": 0.8325, \"ppl\": 6.15}, \"beta_10.0\": {\"mid_gar\": 0.977, \"ppl\": 505.21}, \"n_convs\": 200, \"mode\": \"tf\"}, \"conclusion\": \"success\"}, \"trc_baseline_v7_tg\": {\"status\": \"DONE\", \"hypothesis\": \"如果 exposure bias 对 auxiliary objectives 的破坏跨特征空间通用，那么 TRC (hidden state cos_sim) 在 model-gen 下也应出现与 GAR (attention 空间) 类似的 TF/gen gap。在 v7 TG / LoRA-only / base 三个 checkpoint 上测量 TRC baseline，确认 gap 是否存在。成功标准：gen TRC 显著低于 TF TRC。\", \"conclusion\": \"success\", \"metrics\": {\"v7_tg\": {\"tf_trc\": 0.3339, \"gen_trc\": 0.3323, \"trc_gap\": 0.0016, \"tf_tbp_ppl\": 1.05, \"gen_tbp_ppl\": 1.05}, \"lora_only\": {\"tf_trc\": 0.349, \"gen_trc\": 0.4106, \"trc_gap\": -0.0617, \"tf_tbp_ppl\": 9.5, \"gen_tbp_ppl\": 12}, \"base\": {\"tf_trc\": 0.1494, \"gen_trc\": 0.1494, \"trc_gap\": 0, \"tf_tbp_ppl\": 2.05, \"gen_tbp_ppl\": 2.05}}}, \"attention_steering_v7_tg_gen\": {\"status\": \"DONE\", \"hypothesis\": \"推理时向 attention logits 注入 goal-position bias β 可恢复 autoregressive GAR。如果 GAR 从 0.015 显著提升 → 闭合因果环：exposure bias → attention 偏移 → GAR 坍塌 → 手动修正注意力 → GAR 恢复。扫描 β ∈ {0, 0.5, 1.0, 2.0, 5.0, 10.0}，成功标准：GAR > 0.1 且 PPL 不严重恶化。\", \"conclusion\": \"success\", \"metrics\": {\"beta_0.0\": {\"mid_turns_avg_gar\": 0.028, \"avg_ppl\": 1.409}, \"beta_0.5\": {\"mid_turns_avg_gar\": 0.0287, \"avg_ppl\": 1.387}, \"beta_1.0\": {\"mid_turns_avg_gar\": 0.0349, \"avg_ppl\": 1.36}, \"beta_2.0\": {\"mid_turns_avg_gar\": 0.062, \"avg_ppl\": 1.411}, \"beta_5.0\": {\"mid_turns_avg_gar\": 0.6795, \"avg_ppl\": 1.908}, \"beta_10.0\": {\"mid_turns_avg_gar\": 0.959, \"avg_ppl\": 4.22}, \"phase_transition_range\": \"[2, 5]\", \"baseline_gar\": 0.028, \"max_gar_at_acceptable_ppl\": 0.6795, \"max_gar_at_acceptable_ppl_beta\": 5}}, \"phase2_tg_s42_v8b_ss_fixed\": {\"status\": \"DONE\", \"hypothesis\": \"Fixed scheduled sampling (D026 三项 bug 修复后): 线性从 0→0.5 混合 teacher-forced + model-generated contexts 计算 GAR loss。如果 model-gen context 上的 GAR 训练能缩小 30x training-inference gap → exposure bias mitigation 有效，paper 从纯 negative 升级为 diagnosis + initial remedy。超参与 v7 一致 (lambda_gar=1.0, MSE+gate_div)，唯一变量是 SS path。成功标准：inference GAR 显著高于 v7 的 0.016 (至少 +1pp)，PPL 不恶化。\", \"conclusion\": \"failed\"}, \"phase2_tg_s42_v7\": {\"status\": \"DONE\", \"hypothesis\": \"MSE 双向 loss (mean_GAR - target)² + gate diversity 正则 F.relu(min_std - gate_std) 从结构上解决恒等退化：MSE 在 GAR > target 时反向惩罚（不再单调推高），gate_div 直接强制层间分化。预期：gate_std 稳定 >0.05 + GAR 收敛到 target=0.5 附近 + NTP 正常收敛。\", \"metrics\": {\"eval_iid_ours_mid_gar\": 0.5035, \"eval_iid_dongre_mid_gar\": 0.0152, \"eval_iid_ppl\": 2.784, \"eval_heldout_ours_mid_gar\": 0.5035, \"eval_heldout_dongre_mid_gar\": 0.0152, \"eval_heldout_ppl\": 2.78, \"eval_modelgen_ours_mid_gar\": 0.0157, \"eval_modelgen_dongre_mid_gar\": 0.0194, \"eval_modelgen_ppl\": 1.36, \"gate_mean_final\": 0.9336, \"gate_std_final\": 0.0492}, \"conclusion\": \"success\"}, \"phase2_tg_s42_v9_pcgrad\": {\"status\": \"DONE\", \"hypothesis\": \"PCGrad (Yu et al. NeurIPS 2020) 消除 NTP-GAR 梯度方向冲突后（仅对 gate 参数投影 NTP 梯度到 GAR 梯度正交平面），如果 30x training-inference GAR gap 仍在 → 因果证据证明 exposure bias（非梯度竞争）是 gap 根因。与 v7 对比：相同超参（lambda_gar=1.0, MSE+gate_div），唯一变量是梯度处理方式。成功标准：(1) 梯度 cos_sim 显著改善（从 v7 的 -0.089 提升到 ≥0），(2) 但推理 GAR 仍 ≈ v7 水平（0.016），证明梯度冲突不是 gap 的因。\", \"conclusion\": \"success\", \"metrics\": {\"eval_iid_ours_mid_gar\": 0.5002, \"eval_iid_dongre_mid_gar\": 0.0123, \"eval_iid_ppl\": 2.78, \"eval_iid_ntp\": 0.9752, \"eval_heldout_ours_mid_gar\": 0.5002, \"eval_heldout_dongre_mid_gar\": 0.0123, \"eval_heldout_ppl\": 2.78, \"eval_heldout_ntp\": 0.9752, \"eval_modelgen_ours_mid_gar\": 0.0151, \"eval_modelgen_dongre_mid_gar\": 0.0173, \"eval_modelgen_ppl\": 1.5, \"vs_v7_iid_ppl_diff\": 0.004, \"vs_v7_iid_gar_diff\": -0.0033}}, \"phase2_lora_only_s42\": {\"status\": \"DONE\", \"hypothesis\": \"LoRA-only baseline (gate 固定 1.0，无 gating 机制) 在相同 MSE+NTP loss 下 GAR 应低于 ThreadGate (v7)。如果 LoRA-only 也能训到 GAR~0.5，则 gating 机制贡献为零，paper story 不成立。关键对比：LoRA-only 的 GAR 收敛值 vs v7 的 0.48。\", \"conclusion\": \"success\", \"metrics\": {\"epochs_completed\": 3, \"global_steps\": 3000, \"training_time_seconds\": 20588.6, \"training_time_hours\": 5.7, \"gate_fixed\": 1, \"gate_type_actual\": \"none\", \"final_lora_size_mb\": 20, \"eval_modelgen_ours_mid_gar\": 0.0245, \"eval_modelgen_dongre_mid_gar\": 0.0185, \"eval_modelgen_ppl\": 1.371}}, \"phase2_ug_s42\": {\"status\": \"DONE\", \"hypothesis\": \"Uniform gating baseline: per-layer independent gates without turn conditioning (content-dependent only), to isolate whether ThreadGate's turn-conditioned gating provides benefit over content-only residual scaling. Same training setup as v7 but with gate-type=uniform.\", \"conclusion\": \"success\", \"metrics\": {\"epoch0_avg_loss\": 1.0019, \"epoch0_avg_ntp\": 0.9755, \"epoch0_avg_gar\": 0.0259, \"epoch0_avg_div\": 0.0005, \"epoch1_avg_loss\": 0.9447, \"epoch1_avg_ntp\": 0.9435, \"epoch1_avg_gar\": 0.0013, \"epoch1_avg_div\": 0, \"epoch2_avg_loss\": 0.9319, \"epoch2_avg_ntp\": 0.9309, \"epoch2_avg_gar\": 0.001, \"epoch2_avg_div\": 0, \"final_gate_mean\": 0.9598, \"final_gate_std\": 0.0518, \"final_gate_min\": 0.7773, \"final_gate_max\": 1, \"final_profile_L3\": 0.777, \"final_profile_L5\": 0.812, \"final_profile_L0\": 0.875, \"final_profile_L27\": 1, \"training_time_seconds\": 21994.5, \"training_time_hours\": 6.1, \"global_steps\": 7950, \"unexpected_per_layer_variation\": true, \"eval_modelgen_ours_mid_gar\": 0.0149, \"eval_modelgen_dongre_mid_gar\": 0.0185, \"eval_modelgen_ppl\": 1.396}}, \"phase2_tg_s42_v8_schedsampling\": {\"status\": \"DONE\", \"hypothesis\": \"Scheduled sampling 应用到 GAR loss（线性从 0→0.5 混合 teacher-forced + model-generated contexts）能缩小 v7 的 30x training-inference GAR gap。机制：在 model-generated context 上计算 GAR loss 迫使 attention pattern 适应推理时分布，直接 address teacher-forcing distribution shift。成功标准：inference GAR 显著高于 v7 的 0.016，PPL 不显著恶化（≤2.78+0.2）。\", \"conclusion\": \"failed\", \"metrics\": {\"killed_at_microstep\": 1950, \"total_microsteps\": 24000, \"completion_pct\": 8.1, \"global_step_approx\": 244, \"total_global_steps\": 3000, \"ss_steps_observed\": 1, \"tf_lgar_mean_step850_1400\": 0.0062, \"tf_lgar_std\": 0.0082, \"tf_lgar_collapse_step\": 800, \"gate_mean_final\": 0.93, \"ss_ratio_at_kill\": 0.081, \"crash_reason\": \"killed by director: SS path code bug (D026) makes experiment invalid, GPU needed for PCGrad\", \"design_flaw_ss_ramp_too_slow\": true, \"design_flaw_no_ss_tf_separate_logging\": true}}, \"analysis_attention_heatmap\": {\"status\": \"DONE\", \"hypothesis\": \"四模型（Base/TG/UG/LoRA-only）的 goal attention 衰减模式是否一致？如果 TG 的 attention decay 与 LoRA-only 无差异，则 gating 机制对 attention 分布零增量。\", \"conclusion\": \"success\", \"metrics\": {\"base_mean_goal_attn\": 0.0136, \"base_decay\": 0.875, \"tg_mean_goal_attn\": 0.0232, \"tg_decay\": 0.777, \"ug_mean_goal_attn\": 0.0216, \"ug_decay\": 0.803, \"lora_mean_goal_attn\": 0.0216, \"lora_decay\": 0.81, \"gating_incremental_benefit\": \"none\"}}, \"analysis_gradient_conflict\": {\"status\": \"DONE\", \"hypothesis\": \"NTP-GAR 梯度冲突在 v7 训练过程中是否逐层普遍存在？量化 cos_sim 和 magnitude ratio 的演化，验证 NTP 是否在训练中逐渐完全压制 GAR 信号。\", \"conclusion\": \"success\", \"metrics\": {\"epoch0_cos_sim\": -0.089, \"epoch1_cos_sim\": -0.054, \"epoch2_cos_sim\": -0.042, \"epoch0_neg_layers_pct\": 78.6, \"epoch1_neg_layers_pct\": 71.4, \"epoch2_neg_layers_pct\": 67.9, \"epoch0_mag_ratio\": 7.5, \"epoch1_mag_ratio\": 13.7, \"epoch2_mag_ratio\": 14.7}}, \"phase2_4way_eval_heldout\": {\"status\": \"DONE\", \"hypothesis\": \"四路消融的三路趋同结论（TG≈UG≈LoRA-only，gating 零增量）在 held-out eval 数据（idx≥8000，与训练集无重叠）上复现，排除数据重叠 confound。预期：相对比较保持（三路趋同），绝对 GAR 值可能变化。\", \"metrics\": {\"base_ours_mid_gar\": 0.0128, \"base_ours_recovery_pp\": 0.06, \"base_dongre_mid_gar\": 0.0031, \"base_dongre_recovery_pp\": -0.91, \"base_ppl\": 4.34, \"base_ntp\": 1.4045, \"tg_ours_mid_gar\": 0.5035, \"tg_ours_recovery_pp\": 49.13, \"tg_dongre_mid_gar\": 0.0152, \"tg_dongre_recovery_pp\": 0.3, \"tg_ppl\": 2.78, \"tg_ntp\": 0.9771, \"ug_ours_mid_gar\": 0.5053, \"ug_ours_recovery_pp\": 49.31, \"ug_dongre_mid_gar\": 0.0124, \"ug_dongre_recovery_pp\": 0.02, \"ug_ppl\": 2.78, \"ug_ntp\": 0.9752, \"lora_ours_mid_gar\": 0.4978, \"lora_ours_recovery_pp\": 48.56, \"lora_dongre_mid_gar\": 0.0132, \"lora_dongre_recovery_pp\": 0.1, \"lora_ppl\": 2.78, \"lora_ntp\": 0.9771, \"three_way_convergence_confirmed\": true, \"gar_ours_spread_pp\": 0.75, \"ppl_spread\": 0, \"data_overlap\": false}, \"conclusion\": \"success\"}, \"phase2_4way_eval\": {\"status\": \"DONE\", \"hypothesis\": \"Turn-residual gating (TRG) improves multi-turn response quality over LoRA-only and base model baselines because it selectively amplifies conversational context signals, which should manifest as higher GAR scores across 4 conditions (base, base+TRG, LoRA, LoRA+TRG).\", \"conclusion\": \"negative\", \"metrics\": {\"base_ours_mid_gar\": 0.0107, \"base_ours_recovery_pp\": -0.15, \"base_dongre_mid_gar\": 0.003, \"base_dongre_recovery_pp\": -0.92, \"base_ppl\": 4.23, \"base_ntp\": 1.4162, \"tg_ours_mid_gar\": 0.4866, \"tg_ours_recovery_pp\": 47.44, \"tg_dongre_mid_gar\": 0.0157, \"tg_dongre_recovery_pp\": 0.35, \"tg_ppl\": 2.63, \"tg_ntp\": 0.9484, \"ug_ours_mid_gar\": 0.4923, \"ug_ours_recovery_pp\": 48.01, \"ug_dongre_mid_gar\": 0.013, \"ug_dongre_recovery_pp\": 0.08, \"ug_ppl\": 2.62, \"ug_ntp\": 0.9433, \"lora_ours_mid_gar\": 0.486, \"lora_ours_recovery_pp\": 47.39, \"lora_dongre_mid_gar\": 0.0137, \"lora_dongre_recovery_pp\": 0.15, \"lora_ppl\": 2.63, \"lora_ntp\": 0.9482, \"route_b_confirmed\": true, \"gating_incremental_benefit\": \"none\"}}, \"phase2_tg_s42_v5\": {\"status\": \"DONE\", \"hypothesis\": \"重新平衡超参（λ=1.0 降 GAR 贡献至 ~50%，init_bias=1.5 使 sigmoid≈0.82 接近正常模型行为，gate_lr_multiplier=10 保持）能在 3-epoch 全量训练中产生有意义的 gate 分化（gate_std>0.05），同时 GAR 稳态在 0.1-0.5（非病态饱和），NTP loss 正常收敛，总 loss 保持正值\", \"metrics\": {\"step2000_gate_std\": 0.0225, \"step2000_gate_mean\": 0.9586, \"step2000_gate_min\": 0.9062, \"step2000_gate_max\": 0.9961, \"step2000_L_GAR\": -0.8977, \"step2000_L_NTP\": 0.7611, \"step2000_total_loss\": -0.1365, \"step2400_gate_std\": 0.0219, \"step2400_gate_mean\": 0.9651, \"step2400_gate_min\": 0.918, \"step2400_gate_max\": 0.9961, \"step2400_profile\": \"L0=0.918 L12=0.918 L13=0.926 L1=0.996 L26=0.996\", \"L_GAR_saturated_at\": -0.91, \"gate_range_compression\": \"0.918-0.996\"}, \"conclusion\": \"negative\"}, \"phase2_tg_s42_v4\": {\"status\": \"DONE\", \"hypothesis\": \"重新平衡超参（λ=1.0 降 GAR 贡献至 ~50%，init_bias=1.5 使 sigmoid≈0.82 接近正常模型行为，gate_lr_multiplier=10 保持）能在 3-epoch 全量训练中产生有意义的 gate 分化（gate_std>0.05），同时 GAR 稳态在 0.1-0.5（非病态饱和），NTP loss 正常收敛，总 loss 保持正值\", \"conclusion\": \"failed\"}, \"phase2_tg_s42_v3b\": {\"status\": \"DONE\", \"hypothesis\": \"λ=10 + gate_lr=10x + init_bias=0.0 (sigmoid=0.5) 能否驱动 gate 产生 layer 间分化 (gate_std>0.05)？如果 500 步后 gate_std<0.02 且无选择性 → GAR-driven gating 梯度路径确认失败，需要 pivot\", \"conclusion\": \"success\", \"metrics\": {\"gate_std_final\": 0.087, \"gate_mean_final\": 0.9388, \"gate_min_final\": 0.5352, \"gate_max_final\": 0.9922, \"L4_gate\": 0.535, \"L0_gate\": 0.777, \"L_NTP_final\": 0.7787, \"L_GAR_final\": -0.9606, \"elapsed_seconds\": 3565.9, \"optimizer_steps\": 500, \"gate_grad_received\": true}}, \"phase2_tg_s42_v3\": {\"status\": \"DONE\", \"hypothesis\": \"ThreadGate + maximize GAR loss (L_GAR=-mean(GAR)) 提供持续非零梯度，避免 hinge loss 的退化平衡点，gate 值应随训练下降（学习到选择性干预），同时 NTP loss 正常收敛\", \"conclusion\": \"negative\", \"metrics\": {\"gate_mean_step0\": 0.8743, \"gate_mean_step500\": 0.8761, \"gate_delta\": 0.004, \"gate_std\": 0.001, \"final_ntp_loss\": 0.94, \"final_gar_loss\": -0.019, \"gar_contribution_pct\": \"2-4%\", \"diagnosis\": \"gate frozen, GAR indirect gradient too weak\"}}, \"phase2_tg_s42_v2\": {\"status\": \"DONE\", \"hypothesis\": \"ThreadGate + 修复后的 cumulative GAR loss (ε=0.001) 在 L_NTP+L_GAR 联合训练后，mid-turn GAR recovery 应显著优于 v1 (NTP-only baseline)，验证 GAR loss 的有效性\", \"conclusion\": \"killed\"}, \"phase1_gar_diag\": {\"status\": \"DONE\", \"hypothesis\": \"Qwen2.5-7B-Instruct 在 10-turn 多轮对话中，中间 turns (3-8) 的 GAR (Goal Accessibility Ratio) 相对 turn-1 下降 ≥15%，表明模型对 system prompt 中目标 token 的注意力随对话进行显著衰减\", \"conclusion\": \"success\", \"metrics\": {\"turn1_avg_gar\": 0.0418, \"mid_turns_avg_gar\": 0.0122, \"relative_drop\": 0.708, \"num_conversations\": 5, \"num_turns\": 10, \"per_turn_avg_gar\": [0.0418, 0.0241, 0.0224, 0.013, 0.0133, 0.0086, 0.0078, 0.008, 0.0157, 0.0064]}}}, \"count\": 53, \"total\": 53, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.1764}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "258a34c5-fde4-475f-b756-8ca103ab93ef",
  "isSidechain": false,
  "promptId": "8d8464e4-1523-464c-8d63-5cd7db13bd3f",
  "type": "user",
  "uuid": "0e066bda-3f45-4584-9db9-1703d689ce83",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {\\\"phase1a_multiseed_qwen\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"Multi-seed (s123, s456) training across 5 Qwen conditions (PCGrad, UG, LoRA-only, TG, SS) to establish mean±std for all claims. 8 training runs + AR eval N≥50 each. Expect TF convergence (GAR~0.50) and consistent AR rankings across seeds.\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"p1_ss_lora_only\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"SS training on LoRA-only checkpoint (no ThreadGate) with same hyperparameters (rho_max=0.3, same schedule) should achieve similar GAR improvement as SS+TG. If confirmed, this proves the SS fix is architecture-agnostic, strengthening the paper's mitigation story (the gap is caused by exposure bias in any auxiliary-loss setup, and SS fixes it regardless of gating mechanism).\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"phase2_switching\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"TF→AR switching at turn k (k=1..5) on ThreadGate s42 checkpoint. If GAR drops abruptly at the switch point (matching pure-AR level within 1 turn), it confirms exposure bias as instantaneous distribution shift rather than gradual KV cache drift. Staircase = exposure bias dominant; linear slope = KV drift dominant.\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"p1_llama_ss_eval\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"Llama SS (2-epoch) reduces the TF-AR GAR gap on Llama-3.1-8B, confirming SS as model-general mitigation (C4+C5). Eval: TF+AR N=50 β=0/3/5.\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"ss_tf_gar\\\": 0.477, \\\"ss_tf_ppl\\\": 2.82, \\\"ss_ar_b0_gar\\\": 0.1662, \\\"ss_ar_b0_ppl\\\": 1.37, \\\"ss_ar_b5_gar\\\": 0.7905, \\\"ss_ar_b5_ppl\\\": 1.81, \\\"base_ar_gar\\\": 0.0179, \\\"base_ar_ppl\\\": 1.22, \\\"tf_ar_gap\\\": 2.87}}, \\\"p1_llama_ss_training\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"SS is effective on Qwen (gap 8x to 1.4x). If SS also reduces the TF-AR gap on Llama-3.1-8B, it confirms SS as a model-general mitigation, strengthening C4 (mitigation) and C5 (cross-model) claims.\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"mmlu_eval_all\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"ThreadGate's per-layer gating and auxiliary GAR loss do not degrade the model's general language understanding capabilities. All fine-tuned variants (TG/UG/LO/PCGrad/SS) should maintain MMLU 5-shot accuracy within 1pp of the Base LoRA-only checkpoint, confirming that attention steering is additive rather than destructive.\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"base_qwen\\\": 0.7423, \\\"pcgrad_v9_s42\\\": 0.7386, \\\"ss_v8b_s42\\\": 0.7375, \\\"lo_s42\\\": 0.7357, \\\"tg_v7_s42\\\": 0.7347, \\\"ug_s42\\\": 0.7346}}, \\\"p2_llama_gradient_conflict\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"PCGrad fails to improve AR GAR on Llama-3.1-8B (as on Qwen), confirming cross-model that gradient conflict is not the root cause of the TF-AR gap, strengthening C2 (causal exclusion).\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"cos_sim_mean\\\": 0.0045, \\\"cos_sim_std\\\": 0.07, \\\"neg_cos_sim_layers_pct\\\": 53.1, \\\"mag_ratio_median\\\": 25.7, \\\"conclusion_note\\\": \\\"cos_sim≈0 indicates near-orthogonal (NOT conflict). Script conclusion text 'widespread conflict' is misleading — actual finding: NTP and GAR gradients are nearly orthogonal on Llama, consistent with Qwen pattern.\\\"}}, \\\"p1_tf_ar_kl_divergence\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"TF and AR attention distributions diverge more on GAR-relevant heads (high gate values) than non-relevant heads, providing mechanistic evidence that exposure bias selectively disrupts goal-attending computation rather than uniformly degrading attention.\\\", \\\"metrics\\\": {\\\"tg_delta_gar\\\": 0.0165, \\\"base_delta_gar\\\": 0.0122, \\\"tg_mean_kl\\\": 0.054, \\\"base_mean_kl\\\": 0.043, \\\"gate_kl_correlation\\\": 0.11, \\\"high_kl_layers\\\": \\\"L23-L27, L9\\\", \\\"gar_robustness_ours_tg_base_ratio\\\": 21.4, \\\"gar_robustness_goal_only_ratio\\\": 63, \\\"gar_robustness_ours_all_ratio\\\": 1.7, \\\"gar_robustness_ours_first_ratio\\\": 1.8}, \\\"conclusion\\\": \\\"success\\\"}, \\\"qwen15b_phase1_diag\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"GAR attention decay toward system-prompt goal tokens is a general phenomenon across model scales, not specific to 7B. Qwen-2.5-1.5B-Instruct should also show progressive GAR decline across conversation turns, confirming the phenomenon is architecture-level rather than scale-dependent.\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"d048_eval_ss_s456\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"SS s456 eval: TF + AR N=50 + bootstrap CI to complete 3-seed SS metrics. Together with s42 and s123, establishes mean±std for C2 reviewer requirement.\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"tf_gar_ours_mid\\\": 0.4964, \\\"tf_gar_dongre_mid\\\": 0.3862, \\\"ar_beta0_gar\\\": 0.4325, \\\"ar_beta0_ppl\\\": 1.4394, \\\"ar_beta3_gar\\\": 0.605, \\\"ar_beta3_ppl\\\": 1.5868, \\\"ar_beta5_gar\\\": 0.7157, \\\"ar_beta5_ppl\\\": 1.8045, \\\"n_convs_ar\\\": 50}}, \\\"d048_ss_s456\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"Scheduled sampling (ratio=0.3) with ThreadGate multi-seed (s456) to establish 3-seed mean±std for C2 reviewer requirement of at least 3 seeds\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"d048_eval_ss_s123\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"SS s123 eval: TF + AR N=50 + bootstrap CI to establish multi-seed SS metrics. Expect TF GAR ~0.50, AR GAR similar to s42 (0.347), confirming SS effectiveness across seeds.\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"tf_gar_ours\\\": 0.5536, \\\"tf_gar_dongre\\\": 0.4106, \\\"tf_ppl\\\": 2.6123, \\\"ar_beta0_gar\\\": 0.4231, \\\"ar_beta0_ppl\\\": 1.4408, \\\"ar_beta3_gar\\\": 0.5903, \\\"ar_beta3_ppl\\\": 1.607, \\\"ar_beta5_gar\\\": 0.7174, \\\"ar_beta5_ppl\\\": 1.7852, \\\"n_convs_tf\\\": 200, \\\"n_convs_ar\\\": 39}}, \\\"d048_ss_s123\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"Scheduled sampling (ratio=0.3) with ThreadGate multi-seed (s123) to establish 3-seed mean±std for C2 reviewer requirement. Corrected hyperparams matching d048_ss_s456.\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"d048_split_softmax_eval\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"Split-softmax (Li et al., COLM 2024) post-softmax rescaling recovers AR GAR without the PPL cost of pre-softmax additive steering, providing an alternative inference-time intervention that separates attention allocation from logit distribution.\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"d048_final_ar_eval\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"Unified AR N=50 eval across 6 conditions (Base/TG/UG/LO/PCGrad/SS) with bootstrap CI and Wilcoxon tests to establish statistically rigorous comparisons for all claims\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"beta0\\\": {\\\"base_gar\\\": 0.019, \\\"tg_gar\\\": 0.064, \\\"ug_gar\\\": 0.033, \\\"lo_gar\\\": 0.037, \\\"pcgrad_gar\\\": 0.03, \\\"ss_gar\\\": 0.347}, \\\"beta3\\\": {\\\"base_gar\\\": 0.531, \\\"tg_gar\\\": 0.556, \\\"ss_gar\\\": 0.593}, \\\"beta5\\\": {\\\"base_gar\\\": 0.704, \\\"tg_gar\\\": 0.727, \\\"ss_gar\\\": 0.717}, \\\"wilcoxon_beta0\\\": {\\\"tg_vs_base_p\\\": \\\"<0.001\\\", \\\"tg_vs_base_r\\\": 0.802, \\\"ss_vs_tg_p\\\": \\\"<0.001\\\", \\\"ss_vs_tg_r\\\": 0.869}, \\\"ppl\\\": {\\\"base\\\": 1.447, \\\"tg\\\": 1.432, \\\"ss\\\": 1.442}, \\\"n_convs\\\": 39}}, \\\"d048_eval_ss_s42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"D048 multi-seed SS s42 eval: TF + AR N=50 + bootstrap CI (curve[2:]) to establish mean±std for scheduled sampling. Expect TF GAR ~0.50, AR GAR gap < 2× (vs base ~31×), PPL stable.\\\", \\\"metrics\\\": {\\\"tf\\\": {\\\"base_gar_ours_mid\\\": 0.0128, \\\"base_gar_dongre_mid\\\": 0.0031, \\\"base_ppl\\\": 4.34, \\\"base_ntp\\\": 1.4, \\\"tg_gar_ours_mid\\\": 0.5025, \\\"tg_gar_dongre_mid\\\": 0.389, \\\"tg_ppl\\\": 2.78, \\\"tg_ntp\\\": 0.98, \\\"baseline_mid_gar\\\": 0.0122}, \\\"ar\\\": {\\\"gar_ours_mid\\\": 0.3887, \\\"gar_ours_ci_95\\\": [0.3692, 0.3934], \\\"ppl\\\": 1.35}, \\\"gap_ratio\\\": 1.29, \\\"n_conversations_tf\\\": 50, \\\"n_conversations_ar\\\": 5, \\\"bootstrap_turns\\\": \\\"curve[2:] (turns 3-T)\\\", \\\"note\\\": \\\"AR used hardcoded N=5, not N=50. Will be re-evaluated in final unified batch with eval_200.json N=50.\\\"}, \\\"conclusion\\\": \\\"success\\\"}, \\\"d048_ss_s42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"Scheduled sampling (ratio=0.3) with ThreadGate reduces the ~30× TF-AR GAR gap by exposing the model to its own generated text during training. Multi-seed run (s42) under D048 unified protocol to establish mean±std for statistical testing. SS is the strongest mitigation candidate (prior single-seed showed gap 31×→1.57×).\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"final_avg_loss\\\": 0.9326, \\\"final_ntp_loss\\\": 0.932, \\\"final_gar_loss\\\": 0.0007, \\\"gate_mean\\\": 0.9527, \\\"gate_std\\\": 0.0589, \\\"gate_min\\\": 0.7383, \\\"gate_min_layer\\\": \\\"L4\\\", \\\"gate_max\\\": 1, \\\"ss_usage\\\": \\\"4750/16000 (29.7%)\\\", \\\"ss_fallback\\\": 0, \\\"epochs_completed\\\": 3, \\\"wall_clock_s\\\": 23418, \\\"wall_clock_h\\\": 6.5}}, \\\"eval_llama_ar_n20\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"N=20 AR eval stabilizes Llama 3-way (Base/TG/LoRA-only) autoregressive GAR estimates. N=5 suffered from outlier influence (3/5 conv had GAR>0.4 outlier turns); N=20 provides robust mean±std.\\\", \\\"metrics\\\": {\\\"base\\\": {\\\"gar_ours_mean\\\": 0.0088, \\\"gar_ours_std\\\": 0.0056, \\\"gar_ours_median_per_conv\\\": 0.0093, \\\"gar_ours_median_per_turn_pool\\\": 0.0071, \\\"gar_ours_spike_ratio\\\": \\\"0%\\\", \\\"gar_dongre_mean\\\": 0.0049, \\\"gar_dongre_std\\\": 0.0013, \\\"gar_dongre_median\\\": 0.0047, \\\"ngar_ours_mid\\\": 0.1019, \\\"ngar_dongre_mid\\\": 0.1171, \\\"ppl\\\": 1.293, \\\"ppl_std\\\": 0.07, \\\"ntp_loss\\\": 0.2552}, \\\"tg\\\": {\\\"gar_ours_mean\\\": 0.0434, \\\"gar_ours_std\\\": 0.1002, \\\"gar_ours_median_per_conv\\\": 0.0179, \\\"gar_ours_median_per_turn_pool\\\": 0.0126, \\\"gar_ours_spike_ratio\\\": \\\"5% (2/40 turns GAR>=0.4)\\\", \\\"gar_dongre_mean\\\": 0.0183, \\\"gar_dongre_std\\\": 0.0198, \\\"gar_dongre_median\\\": 0.0152, \\\"ngar_ours_mid\\\": 0.5357, \\\"ngar_dongre_mid\\\": 0.4436, \\\"ppl\\\": 1.437, \\\"ppl_std\\\": 0.077, \\\"ntp_loss\\\": 0.3612}, \\\"lora_only\\\": {\\\"gar_ours_mean\\\": 0.0284, \\\"gar_ours_std\\\": 0.0481, \\\"gar_ours_median_per_conv\\\": 0.0184, \\\"gar_ours_median_per_turn_pool\\\": 0.0133, \\\"gar_ours_spike_ratio\\\": \\\"0%\\\", \\\"gar_dongre_mean\\\": 0.0205, \\\"gar_dongre_std\\\": 0.0241, \\\"gar_dongre_median\\\": 0.016, \\\"ngar_ours_mid\\\": 0.3488, \\\"ngar_dongre_mid\\\": 0.4997, \\\"ppl\\\": 1.419, \\\"ppl_std\\\": 0.075, \\\"ntp_loss\\\": 0.3483}, \\\"n_conversations\\\": 20, \\\"n_turns\\\": 4, \\\"mid_turns_definition\\\": \\\"turns 3-T (0-indexed avg_gar[2:], excluding turns 1-2). All 16 eval entries use same definition.\\\", \\\"stat_pool\\\": \\\"median_per_conv: median of 20 per-conversation mid-turn averages. median_per_turn_pool: median of 40 individual turn values (20 conv x 2 mid turns).\\\", \\\"ranking_gar_ours_mean\\\": \\\"TG(0.0434) > LO(0.0284) > Base(0.0088)\\\", \\\"ranking_gar_ours_median_per_conv\\\": \\\"TG(0.0179) ≈ LO(0.0184) > Base(0.0093)\\\", \\\"ranking_gar_ours_median_per_turn_pool\\\": \\\"TG(0.0126) ≈ LO(0.0133) > Base(0.0071)\\\", \\\"ranking_gar_dongre\\\": \\\"LO(0.0205) > TG(0.0183) > Base(0.0049)\\\", \\\"note\\\": \\\"Paper §5.5 cites median_per_conv (median of per-conversation mid-turn averages across N=20). median_per_turn_pool is the alternative statistic from pooled individual turns. Both confirm TG ≈ LO (zero-increment).\\\"}, \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_llama_lora_only_s42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"LoRA-only ablation (no gate) on Llama-3.1-8B: if TG's GAR improvement comes from the gate, LoRA-only should show minimal GAR recovery vs base.\\\", \\\"metrics\\\": {\\\"tf\\\": {\\\"gar_ours\\\": 0.4807, \\\"gar_dongre\\\": 0.0188, \\\"ngar_ours\\\": 11.8031, \\\"ngar_dongre\\\": 0.8261, \\\"ppl\\\": 2.6, \\\"ntp_loss\\\": 0.9366, \\\"n_conversations\\\": 50, \\\"n_turns\\\": 4}, \\\"ar\\\": {\\\"gar_ours\\\": 0.0617, \\\"gar_dongre\\\": 0.0226, \\\"ngar_ours\\\": 0.6065, \\\"ngar_dongre\\\": 0.2537, \\\"ppl\\\": 1.32, \\\"ntp_loss\\\": 0.2787, \\\"n_conversations\\\": 5, \\\"n_turns\\\": 10}, \\\"gap_ratio_gar_ours\\\": 7.79}, \\\"conclusion\\\": \\\"success\\\"}, \\\"llama_lora_only_s42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"Llama-3.1-8B LoRA-only baseline (gate=none, 无 gating 机制): 与 Llama TG s42 对比，验证 gating 对 Llama 的增量贡献。如果 LoRA-only GAR ≈ TG GAR → gating 零增量与 Qwen 结论一致（C5 跨模型）。\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"final_avg_loss\\\": 0.9288, \\\"final_avg_ntp\\\": 0.9279, \\\"final_avg_gar\\\": 0.0009, \\\"gate_fixed\\\": 1, \\\"gate_type\\\": \\\"none\\\", \\\"wall_clock_s\\\": 25317, \\\"wall_clock_h\\\": 7.03, \\\"epochs_completed\\\": 3}}, \\\"phase2_tg_s42_v6\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"smooth_saturation loss (-target*tanh(GAR/target), target=0.5) 提供有界但持续的 GAR 梯度，避免 maximize 的恒等退化（gate→1）和 hinge_target 的梯度消失（GAR达标后梯度=0）。预期：gate_std>0.05 的层间分化 + GAR 稳态在 0.3-0.5 + NTP loss 正常收敛 + 总 loss 为正。\\\", \\\"metrics\\\": {\\\"dryrun_step0_L_NTP\\\": 2.0275, \\\"dryrun_step0_L_GAR\\\": -0.0161, \\\"dryrun_step0_total_loss\\\": 2.0114, \\\"dryrun_step4_L_NTP\\\": 1.6544, \\\"dryrun_step4_L_GAR\\\": -0.0147, \\\"dryrun_step4_total_loss\\\": 1.6397, \\\"dryrun_gate_grad\\\": true, \\\"dryrun_gate_mean_init\\\": 0.8097, \\\"dryrun_gate_std_init\\\": 0.0341, \\\"dryrun_gate_min_init\\\": 0.6836, \\\"dryrun_gate_max_init\\\": 0.8672, \\\"dryrun_gate_mean_step5\\\": 0.8025, \\\"dryrun_gate_std_step5\\\": 0.0842, \\\"dryrun_gate_min_step5\\\": 0.5547, \\\"dryrun_gate_max_step5\\\": 0.9805, \\\"gs50_gate_mean\\\": 0.8117, \\\"gs50_gate_std\\\": 0.0612, \\\"gs50_gate_min\\\": 0.6836, \\\"gs50_gate_max\\\": 0.9805, \\\"gs100_gate_mean\\\": 0.8737, \\\"gs100_gate_std\\\": 0.0367, \\\"gs100_gate_min\\\": 0.8164, \\\"gs100_gate_max\\\": 0.9766, \\\"gs100_L_NTP\\\": 0.8151, \\\"gs100_L_GAR\\\": -0.158, \\\"gs100_total_loss\\\": 0.6571, \\\"gs100_profile_bottom3\\\": \\\"L12=0.816 L4=0.824 L13=0.824\\\", \\\"gs100_profile_top3\\\": \\\"L27=0.977 L26=0.961 L23=0.914\\\", \\\"gs143_L_GAR\\\": -0.3876, \\\"gs143_gate_mean\\\": 0.9227}, \\\"conclusion\\\": \\\"negative\\\"}, \\\"phase2_tg_s42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"ThreadGate (turn-conditional gating) 在 L_NTP+L_GAR 联合训练后，相比 Uniform Gate，mid-turn GAR recovery 高出 ≥3pp，验证 Cesaro 理论预测：position-conditional 干预优于 uniform 干预\\\", \\\"conclusion\\\": \\\"negative\\\", \\\"metrics\\\": {\\\"final_ntp_loss\\\": 0.94, \\\"final_gar_loss\\\": 0, \\\"gate_mean\\\": 0.988, \\\"gar_loss_zero_pct\\\": 87.6, \\\"epochs_completed\\\": 1.67, \\\"killed_reason\\\": \\\"SIGTERM by diagnose worker (unauthorized)\\\"}}, \\\"eval_v7_tg_s123\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"v7 TG s123 eval: 验证 s123 seed 的 TF-AR GAR gap 与 s42 一致（~32×），确认 multi-seed robustness\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"iid_tf\\\": {\\\"gar_ours_mid\\\": 0.5052, \\\"gar_dongre_mid\\\": 0.0119, \\\"ppl\\\": 2.7802, \\\"ntp\\\": 0.9752}, \\\"modelgen_ar\\\": {\\\"gar_ours_mid\\\": 0.0165, \\\"gar_dongre_mid\\\": 0.0177, \\\"ppl\\\": 1.3855, \\\"ntp\\\": 0.3223}, \\\"gap_ratio\\\": 30.6, \\\"comparison_s42\\\": {\\\"tf_gar_ours_delta\\\": 0.0017, \\\"ar_gar_ours_delta\\\": 0.0008, \\\"gap_ratio_delta\\\": -1.4}}}, \\\"eval_v8b_ss_s123\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"v8b SS model trained with s123 seed should reproduce s42 GAR metrics within acceptable gap_ratio [1.2x-2.5x] and no PPL degradation, confirming seed robustness of the scheduled sampling approach\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"iid\\\": {\\\"gar_ours\\\": 0.503, \\\"gar_dongre\\\": 0.394, \\\"ppl\\\": 2.781, \\\"ntp_loss\\\": 0.976, \\\"n_conv\\\": 50, \\\"n_turns\\\": 3}, \\\"modelgen\\\": {\\\"gar_ours\\\": 0.418, \\\"gar_dongre\\\": 0.441, \\\"ppl\\\": 1.389, \\\"ntp_loss\\\": 0.325, \\\"n_conv\\\": 5, \\\"n_turns\\\": 10}, \\\"gap_ratio\\\": 1.2, \\\"base_iid_ppl\\\": 4.338, \\\"base_modelgen_ppl\\\": 1.351}}, \\\"v7_tg_s123\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"v7 TG s42 已验证 ThreadGate 有效性，s123 验证 seed robustness。预期 gate profile 和 GAR 收敛模式与 s42 一致。\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"epoch_1\\\": {\\\"avg_loss\\\": 0.9447, \\\"avg_ntp_loss\\\": 0.9434, \\\"avg_gar_loss\\\": 0.0013, \\\"avg_div_loss\\\": 0}, \\\"epoch_2\\\": {\\\"avg_loss\\\": 0.9315, \\\"avg_ntp_loss\\\": 0.9305, \\\"avg_gar_loss\\\": 0.001, \\\"avg_div_loss\\\": 0}, \\\"final_gate\\\": {\\\"mean\\\": 0.9467, \\\"std\\\": 0.051, \\\"min\\\": 0.793, \\\"max\\\": 1}, \\\"final_gate_profile\\\": {\\\"L0\\\": 0.883, \\\"L1\\\": 0.793, \\\"L2\\\": 0.996, \\\"L3\\\": 0.988, \\\"L4\\\": 0.984, \\\"L5\\\": 0.797, \\\"L6\\\": 0.961, \\\"L7\\\": 0.918, \\\"L8\\\": 0.965, \\\"L9\\\": 0.934, \\\"L10\\\": 0.969, \\\"L11\\\": 0.918, \\\"L12\\\": 0.926, \\\"L13\\\": 0.941, \\\"L14\\\": 0.93, \\\"L15\\\": 0.965, \\\"L16\\\": 0.941, \\\"L17\\\": 0.91, \\\"L18\\\": 0.961, \\\"L19\\\": 0.965, \\\"L20\\\": 0.973, \\\"L21\\\": 0.988, \\\"L22\\\": 0.969, \\\"L23\\\": 0.98, \\\"L24\\\": 0.98, \\\"L25\\\": 0.984, \\\"L26\\\": 0.988, \\\"L27\\\": 1}, \\\"training_time_s\\\": 21425.2}}, \\\"v8b_ss_s123\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"v8b SS s42 成功（gap 32×→1.57×），s123 验证结果的 seed robustness。预期 model-gen GAR 同样显著提升，PPL 无恶化。\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"final_loss\\\": 0.9316, \\\"final_ntp_loss\\\": 0.9307, \\\"final_gar_loss\\\": 0.0009, \\\"final_gate_mean\\\": 0.9505, \\\"final_gate_std\\\": 0.0508, \\\"final_gate_min\\\": 0.7383, \\\"final_gate_max\\\": 1, \\\"ss_used_ratio\\\": 0.371, \\\"training_time_s\\\": 38773.4, \\\"epoch0_loss\\\": 1.0092, \\\"epoch1_loss\\\": 0.9444, \\\"epoch2_loss\\\": 0.9316}}, \\\"llama_ar_matched_eval\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"用 matched 设置 (N=50/T=4) 重跑 Llama AR eval，消除 TF/AR 设置差异。与 TF 结果对比得到可直接写入论文的 gap ratio，验证 TG 在 AR 模式下仍能提升 GAR。\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"ar_base_ours\\\": {\\\"mid_gar\\\": 0.0082, \\\"ngar\\\": 0.1, \\\"ppl\\\": 1.267}, \\\"ar_tg_ours\\\": {\\\"mid_gar\\\": 0.0388, \\\"ngar\\\": 0.493, \\\"ppl\\\": 1.413}, \\\"ar_base_dongre\\\": {\\\"mid_gar\\\": 0.0051, \\\"ngar\\\": 0.12, \\\"ppl\\\": 1.267}, \\\"ar_tg_dongre\\\": {\\\"mid_gar\\\": 0.018, \\\"ngar\\\": 0.431, \\\"ppl\\\": 1.413}, \\\"tf_reference\\\": {\\\"tf_tg_ours_ngar\\\": 11.88, \\\"tf_base_ours_ngar\\\": 0.388, \\\"tf_tg_ours_raw\\\": 0.4836, \\\"tf_tg_dongre_raw\\\": 0.018}, \\\"matched_gap_analysis\\\": {\\\"gar_ours_raw_gap\\\": \\\"12.5x (TF 0.484 / AR 0.039)\\\", \\\"gar_ours_ngar_gap\\\": \\\"24.1x (TF 11.88 / AR 0.493)\\\", \\\"gar_dongre_raw_gap\\\": \\\"1.002x (TF 0.018 / AR 0.018) — zero gap\\\", \\\"tg_over_base_ar_ours\\\": \\\"4.71x\\\", \\\"tg_over_base_ar_dongre\\\": \\\"3.54x\\\", \\\"conclusion\\\": \\\"GAR-ours TF-AR gap 12.5x (raw) / 24x (nGAR) is genuine exposure bias. GAR-Dongre zero gap (1.002x) confirms mechanism specificity: exposure bias selectively destroys learned goal-attention routing while leaving content-overlap-based attention unaffected.\\\"}}}, \\\"instruction_retention_test\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"Turn-level residual gating (β=3) preserves instruction-following ability across multi-turn conversations better than the baseline (β=0), because gating modulates residual contributions to retain earlier context signals rather than letting them decay through successive transformer layers.\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"late_turn_rate_beta0\\\": 0.759, \\\"late_turn_rate_beta3\\\": 0.87, \\\"late_turn_delta\\\": 0.111, \\\"mcnemar_chi2\\\": 3.125, \\\"mcnemar_p\\\": 0.0771, \\\"gar_compliance_r\\\": 0.2003, \\\"gar_compliance_p\\\": 0.007, \\\"category_content_constraint\\\": {\\\"beta0\\\": 0.619, \\\"beta3\\\": 0.857, \\\"delta\\\": 0.238}, \\\"category_count_constraint\\\": {\\\"beta0\\\": 1, \\\"beta3\\\": 1, \\\"delta\\\": 0}, \\\"category_format_constraint\\\": {\\\"beta0\\\": 1, \\\"beta3\\\": 1, \\\"delta\\\": 0}, \\\"category_position_constraint\\\": {\\\"beta0\\\": 0.667, \\\"beta3\\\": 0.733, \\\"delta\\\": 0.067}}}, \\\"llama_eval_s42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"Llama-3.1-8B TG eval: 如果 Llama TG 模型在 TF 模式下 GAR-ours 显著高于 AR 模式（如 Qwen v7 的 20-33x gap），则确认 training-inference GAR gap 跨模型泛化（C5）。同时测量 base model 作为 control。\\\", \\\"metrics\\\": {\\\"tf_base\\\": {\\\"gar_ours\\\": 0.0166, \\\"ngar_ours\\\": 0.3882, \\\"gar_dongre\\\": 0.0038, \\\"ngar_dongre\\\": 0.163, \\\"ppl\\\": 3.45, \\\"N\\\": 50, \\\"T\\\": 4}, \\\"tf_tg\\\": {\\\"gar_ours\\\": 0.4836, \\\"ngar_ours\\\": 11.8818, \\\"gar_dongre\\\": 0.018, \\\"ngar_dongre\\\": 0.7922, \\\"ppl\\\": 2.57, \\\"N\\\": 50, \\\"T\\\": 4}, \\\"ar_base\\\": {\\\"gar_ours\\\": 0.0086, \\\"ngar_ours\\\": 0.0798, \\\"gar_dongre\\\": 0.0118, \\\"ngar_dongre\\\": 0.1265, \\\"ppl\\\": 1.24, \\\"N\\\": 5, \\\"T\\\": 10}, \\\"ar_tg\\\": {\\\"gar_ours\\\": 0.0304, \\\"ngar_ours\\\": 0.2632, \\\"gar_dongre\\\": 0.0217, \\\"ngar_dongre\\\": 0.2459, \\\"ppl\\\": 1.32, \\\"N\\\": 5, \\\"T\\\": 10}, \\\"gap_ratio_tg_ours\\\": 15.9, \\\"gap_ratio_base_ours\\\": 1.93, \\\"gap_ratio_tg_dongre\\\": 0.83, \\\"vs_qwen_v7_gap_ratio\\\": 32.1, \\\"baseline_mid_gar\\\": 0.0122}, \\\"conclusion\\\": \\\"success\\\"}, \\\"llama_tg_s42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"在 Llama-3.1-8B-Instruct 上训练 ThreadGate（与 Qwen v7 相同配置），验证 C5：gating mechanism 和 GAR training-inference gap 跨模型泛化。如果 Llama TG 也出现 IID GAR ≈ target 但 model-gen GAR 坍塌 → 确认 exposure bias 的跨模型通用性。\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"epochs_completed\\\": 3, \\\"total_steps\\\": 3000, \\\"wall_clock_seconds\\\": 26212, \\\"wall_clock_hours\\\": 7.28, \\\"final_avg_loss\\\": 0.9233, \\\"final_avg_ntp\\\": 0.9224, \\\"final_avg_gar\\\": 0.0009, \\\"final_avg_div\\\": 0, \\\"final_gate_mean\\\": 0.9099, \\\"final_gate_std\\\": 0.0701, \\\"final_gate_min\\\": 0.7188, \\\"final_gate_max\\\": 0.9922, \\\"gate_profile_step3000\\\": {\\\"L0\\\": 0.957, \\\"L1\\\": 0.973, \\\"L2\\\": 0.977, \\\"L3\\\": 0.965, \\\"L4\\\": 0.992, \\\"L5\\\": 0.969, \\\"L6\\\": 0.957, \\\"L7\\\": 0.957, \\\"L8\\\": 0.961, \\\"L9\\\": 0.949, \\\"L10\\\": 0.938, \\\"L11\\\": 0.934, \\\"L12\\\": 0.969, \\\"L13\\\": 0.953, \\\"L14\\\": 0.957, \\\"L15\\\": 0.965, \\\"L16\\\": 0.953, \\\"L17\\\": 0.961, \\\"L18\\\": 0.922, \\\"L19\\\": 0.902, \\\"L20\\\": 0.883, \\\"L21\\\": 0.863, \\\"L22\\\": 0.836, \\\"L23\\\": 0.844, \\\"L24\\\": 0.809, \\\"L25\\\": 0.719, \\\"L26\\\": 0.762, \\\"L27\\\": 0.805, \\\"L28\\\": 0.801, \\\"L29\\\": 0.855, \\\"L30\\\": 0.898, \\\"L31\\\": 0.934}, \\\"checkpoint_size_gate_mb\\\": 4.2, \\\"checkpoint_size_lora_mb\\\": 26, \\\"gpu\\\": \\\"NVIDIA RTX PRO 6000 Blackwell\\\", \\\"vram_gb\\\": 102, \\\"mem_used_gb\\\": 63.4}}, \\\"attention_steering_gen_n50\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"N=5 gen steering 显示 β∈[2,5] phase transition (GAR 0.06→0.68)，但样本量不足以报告置信区间。N=50 conversations 应重现同一 phase transition pattern 并提供统计鲁棒的 mean±std，加固 C6 claim (attention steering as causal mechanism proof)。\\\", \\\"metrics\\\": {\\\"corrected\\\": true, \\\"aggregation\\\": \\\"per-conv mid_gar(turns 2-7), >=3 turns only\\\", \\\"beta_0.0\\\": {\\\"mid_gar\\\": 0.0641, \\\"mid_gar_std\\\": 0.0809, \\\"ppl\\\": 1.4324, \\\"ppl_std\\\": 0.1029, \\\"n_valid\\\": 39}, \\\"beta_2.0\\\": {\\\"mid_gar\\\": 0.128, \\\"mid_gar_std\\\": 0.1101, \\\"ppl\\\": 1.4822, \\\"ppl_std\\\": 0.1385, \\\"n_valid\\\": 39}, \\\"beta_3.0\\\": {\\\"mid_gar\\\": 0.5558, \\\"mid_gar_std\\\": 0.0601, \\\"ppl\\\": 1.5605, \\\"ppl_std\\\": 0.1719, \\\"n_valid\\\": 39}, \\\"beta_4.0\\\": {\\\"mid_gar\\\": 0.6439, \\\"mid_gar_std\\\": 0.0607, \\\"ppl\\\": 1.6674, \\\"ppl_std\\\": 0.2241, \\\"n_valid\\\": 39}, \\\"beta_5.0\\\": {\\\"mid_gar\\\": 0.7271, \\\"mid_gar_std\\\": 0.0605, \\\"ppl\\\": 1.7723, \\\"ppl_std\\\": 0.2693, \\\"n_valid\\\": 38}, \\\"beta_10.0\\\": {\\\"mid_gar\\\": 0.9612, \\\"mid_gar_std\\\": 0.0152, \\\"ppl\\\": 3.4517, \\\"ppl_std\\\": 1.7813, \\\"n_valid\\\": 39}, \\\"n_convs_total\\\": 50, \\\"n_convs_valid\\\": 39, \\\"mode\\\": \\\"gen\\\", \\\"phase_transition_range\\\": \\\"[2, 3]\\\"}, \\\"conclusion\\\": \\\"success\\\"}, \\\"phase2_tg_s42_v8b_resume\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"从 epoch_0 checkpoint resume v8b scheduled sampling 训练。SS 线性混合 0→0.5 teacher-forced + model-generated contexts。如果 model-gen context 上的 GAR 训练能缩小 30x training-inference gap → exposure bias mitigation 有效。成功标准：inference GAR 显著高于 v7 的 0.016 (至少 +1pp)，PPL 不恶化。\\\", \\\"metrics\\\": {\\\"training\\\": {\\\"total_steps\\\": 3000, \\\"epochs_completed\\\": 3, \\\"wall_clock_hours\\\": 8.1, \\\"final_loss\\\": 0.933, \\\"final_ntp_loss\\\": 0.9322, \\\"final_gar_loss\\\": 0.0008, \\\"final_gate_mean\\\": 0.9586, \\\"final_gate_std\\\": 0.0582, \\\"ss_ratio\\\": 0.5}, \\\"eval_iid\\\": {\\\"gar_ours\\\": 0.4983, \\\"gar_dongre\\\": 0.3855, \\\"ppl\\\": 2.78}, \\\"eval_modelgen\\\": {\\\"gar_ours\\\": 0.3177, \\\"gar_dongre\\\": 0.3533, \\\"ppl\\\": 1.38}, \\\"vs_v7\\\": {\\\"iid_gar_ours_delta\\\": -0.005, \\\"modelgen_gar_ours_delta\\\": 0.302, \\\"gap_ratio_v7\\\": 32, \\\"gap_ratio_v8b\\\": 1.57}}, \\\"conclusion\\\": \\\"success\\\"}, \\\"llama_phase1_gar_diag\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"Llama-3.1-8B-Instruct 在 multi-turn dialogue 中也应出现 goal attention decay（与 Qwen-2.5-7B 类似），确认 attention decay 是 transformer 架构通用现象而非模型特有。Phase 1 诊断：测量 base Llama 的 per-turn GAR profile。\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"per_turn_gar\\\": {\\\"turn_1\\\": 0.0263, \\\"turn_2\\\": 0.0183, \\\"turn_3\\\": 0.0087, \\\"turn_4\\\": 0.0055, \\\"turn_5\\\": 0.006, \\\"turn_6\\\": 0.0035, \\\"turn_7\\\": 0.0038, \\\"turn_8\\\": 0.0037, \\\"turn_9\\\": 0.005, \\\"turn_10\\\": 0.0026}, \\\"t1_t10_decay_pct\\\": 90.1, \\\"t1_mid38_drop_pct\\\": 80.2, \\\"n_topics\\\": 5, \\\"model\\\": \\\"Meta-Llama-3.1-8B-Instruct\\\", \\\"mode\\\": \\\"gen\\\", \\\"n_conversations\\\": 5, \\\"n_turns\\\": 10}}, \\\"eval_v8b_ss\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"Scheduled Sampling (linear 0→0.5 mixing of teacher-forced and model-gen contexts) closes the 30x training-inference GAR gap by reducing exposure bias, resulting in model-gen GAR significantly above v7 baseline (0.016) while preserving IID GAR and PPL.\\\", \\\"metrics\\\": {\\\"iid_gar_ours\\\": 0.4983, \\\"iid_gar_dongre\\\": 0.3855, \\\"iid_ppl\\\": 2.78, \\\"iid_ngar_ours\\\": 13.5, \\\"iid_ngar_dongre\\\": 22.68, \\\"modelgen_gar_ours\\\": 0.3177, \\\"modelgen_gar_dongre\\\": 0.3533, \\\"modelgen_ppl\\\": 1.38, \\\"modelgen_ngar_ours\\\": 4.47, \\\"modelgen_ngar_dongre\\\": 5.92, \\\"iid_turn1_gar_ours\\\": 0.5398, \\\"modelgen_turn1_gar_ours\\\": 0.4333}, \\\"conclusion\\\": \\\"success\\\"}, \\\"attention_steering_eval200_tf\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"N=200 TF 模式 attention steering 验证 β-GAR 关系的统计鲁棒性。在 teacher-forced context (无 exposure bias) 下，steering 效果应更温和（baseline GAR 已 ~0.50），但仍展示 β 调控 attention 的能力。与 N=5 gen 模式结果互补：tf 验证机制可控性，gen 验证因果闭环。\\\", \\\"metrics\\\": {\\\"beta_0.0\\\": {\\\"mid_gar\\\": 0.5353, \\\"ppl\\\": 2.62}, \\\"beta_2.0\\\": {\\\"mid_gar\\\": 0.6112, \\\"ppl\\\": 2.69}, \\\"beta_3.0\\\": {\\\"mid_gar\\\": 0.788, \\\"ppl\\\": 2.93}, \\\"beta_4.0\\\": {\\\"mid_gar\\\": 0.8165, \\\"ppl\\\": 3.49}, \\\"beta_5.0\\\": {\\\"mid_gar\\\": 0.8325, \\\"ppl\\\": 6.15}, \\\"beta_10.0\\\": {\\\"mid_gar\\\": 0.977, \\\"ppl\\\": 505.21}, \\\"n_convs\\\": 200, \\\"mode\\\": \\\"tf\\\"}, \\\"conclusion\\\": \\\"success\\\"}, \\\"trc_baseline_v7_tg\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"如果 exposure bias 对 auxiliary objectives 的破坏跨特征空间通用，那么 TRC (hidden state cos_sim) 在 model-gen 下也应出现与 GAR (attention 空间) 类似的 TF/gen gap。在 v7 TG / LoRA-only / base 三个 checkpoint 上测量 TRC baseline，确认 gap 是否存在。成功标准：gen TRC 显著低于 TF TRC。\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"v7_tg\\\": {\\\"tf_trc\\\": 0.3339, \\\"gen_trc\\\": 0.3323, \\\"trc_gap\\\": 0.0016, \\\"tf_tbp_ppl\\\": 1.05, \\\"gen_tbp_ppl\\\": 1.05}, \\\"lora_only\\\": {\\\"tf_trc\\\": 0.349, \\\"gen_trc\\\": 0.4106, \\\"trc_gap\\\": -0.0617, \\\"tf_tbp_ppl\\\": 9.5, \\\"gen_tbp_ppl\\\": 12}, \\\"base\\\": {\\\"tf_trc\\\": 0.1494, \\\"gen_trc\\\": 0.1494, \\\"trc_gap\\\": 0, \\\"tf_tbp_ppl\\\": 2.05, \\\"gen_tbp_ppl\\\": 2.05}}}, \\\"attention_steering_v7_tg_gen\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"推理时向 attention logits 注入 goal-position bias β 可恢复 autoregressive GAR。如果 GAR 从 0.015 显著提升 → 闭合因果环：exposure bias → attention 偏移 → GAR 坍塌 → 手动修正注意力 → GAR 恢复。扫描 β ∈ {0, 0.5, 1.0, 2.0, 5.0, 10.0}，成功标准：GAR > 0.1 且 PPL 不严重恶化。\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"beta_0.0\\\": {\\\"mid_turns_avg_gar\\\": 0.028, \\\"avg_ppl\\\": 1.409}, \\\"beta_0.5\\\": {\\\"mid_turns_avg_gar\\\": 0.0287, \\\"avg_ppl\\\": 1.387}, \\\"beta_1.0\\\": {\\\"mid_turns_avg_gar\\\": 0.0349, \\\"avg_ppl\\\": 1.36}, \\\"beta_2.0\\\": {\\\"mid_turns_avg_gar\\\": 0.062, \\\"avg_ppl\\\": 1.411}, \\\"beta_5.0\\\": {\\\"mid_turns_avg_gar\\\": 0.6795, \\\"avg_ppl\\\": 1.908}, \\\"beta_10.0\\\": {\\\"mid_turns_avg_gar\\\": 0.959, \\\"avg_ppl\\\": 4.22}, \\\"phase_transition_range\\\": \\\"[2, 5]\\\", \\\"baseline_gar\\\": 0.028, \\\"max_gar_at_acceptable_ppl\\\": 0.6795, \\\"max_gar_at_acceptable_ppl_beta\\\": 5}}, \\\"phase2_tg_s42_v8b_ss_fixed\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"Fixed scheduled sampling (D026 三项 bug 修复后): 线性从 0→0.5 混合 teacher-forced + model-generated contexts 计算 GAR loss。如果 model-gen context 上的 GAR 训练能缩小 30x training-inference gap → exposure bias mitigation 有效，paper 从纯 negative 升级为 diagnosis + initial remedy。超参与 v7 一致 (lambda_gar=1.0, MSE+gate_div)，唯一变量是 SS path。成功标准：inference GAR 显著高于 v7 的 0.016 (至少 +1pp)，PPL 不恶化。\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"phase2_tg_s42_v7\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"MSE 双向 loss (mean_GAR - target)² + gate diversity 正则 F.relu(min_std - gate_std) 从结构上解决恒等退化：MSE 在 GAR > target 时反向惩罚（不再单调推高），gate_div 直接强制层间分化。预期：gate_std 稳定 >0.05 + GAR 收敛到 target=0.5 附近 + NTP 正常收敛。\\\", \\\"metrics\\\": {\\\"eval_iid_ours_mid_gar\\\": 0.5035, \\\"eval_iid_dongre_mid_gar\\\": 0.0152, \\\"eval_iid_ppl\\\": 2.784, \\\"eval_heldout_ours_mid_gar\\\": 0.5035, \\\"eval_heldout_dongre_mid_gar\\\": 0.0152, \\\"eval_heldout_ppl\\\": 2.78, \\\"eval_modelgen_ours_mid_gar\\\": 0.0157, \\\"eval_modelgen_dongre_mid_gar\\\": 0.0194, \\\"eval_modelgen_ppl\\\": 1.36, \\\"gate_mean_final\\\": 0.9336, \\\"gate_std_final\\\": 0.0492}, \\\"conclusion\\\": \\\"success\\\"}, \\\"phase2_tg_s42_v9_pcgrad\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"PCGrad (Yu et al. NeurIPS 2020) 消除 NTP-GAR 梯度方向冲突后（仅对 gate 参数投影 NTP 梯度到 GAR 梯度正交平面），如果 30x training-inference GAR gap 仍在 → 因果证据证明 exposure bias（非梯度竞争）是 gap 根因。与 v7 对比：相同超参（lambda_gar=1.0, MSE+gate_div），唯一变量是梯度处理方式。成功标准：(1) 梯度 cos_sim 显著改善（从 v7 的 -0.089 提升到 ≥0），(2) 但推理 GAR 仍 ≈ v7 水平（0.016），证明梯度冲突不是 gap 的因。\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"eval_iid_ours_mid_gar\\\": 0.5002, \\\"eval_iid_dongre_mid_gar\\\": 0.0123, \\\"eval_iid_ppl\\\": 2.78, \\\"eval_iid_ntp\\\": 0.9752, \\\"eval_heldout_ours_mid_gar\\\": 0.5002, \\\"eval_heldout_dongre_mid_gar\\\": 0.0123, \\\"eval_heldout_ppl\\\": 2.78, \\\"eval_heldout_ntp\\\": 0.9752, \\\"eval_modelgen_ours_mid_gar\\\": 0.0151, \\\"eval_modelgen_dongre_mid_gar\\\": 0.0173, \\\"eval_modelgen_ppl\\\": 1.5, \\\"vs_v7_iid_ppl_diff\\\": 0.004, \\\"vs_v7_iid_gar_diff\\\": -0.0033}}, \\\"phase2_lora_only_s42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"LoRA-only baseline (gate 固定 1.0，无 gating 机制) 在相同 MSE+NTP loss 下 GAR 应低于 ThreadGate (v7)。如果 LoRA-only 也能训到 GAR~0.5，则 gating 机制贡献为零，paper story 不成立。关键对比：LoRA-only 的 GAR 收敛值 vs v7 的 0.48。\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"epochs_completed\\\": 3, \\\"global_steps\\\": 3000, \\\"training_time_seconds\\\": 20588.6, \\\"training_time_hours\\\": 5.7, \\\"gate_fixed\\\": 1, \\\"gate_type_actual\\\": \\\"none\\\", \\\"final_lora_size_mb\\\": 20, \\\"eval_modelgen_ours_mid_gar\\\": 0.0245, \\\"eval_modelgen_dongre_mid_gar\\\": 0.0185, \\\"eval_modelgen_ppl\\\": 1.371}}, \\\"phase2_ug_s42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"Uniform gating baseline: per-layer independent gates without turn conditioning (content-dependent only), to isolate whether ThreadGate's turn-conditioned gating provides benefit over content-only residual scaling. Same training setup as v7 but with gate-type=uniform.\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"epoch0_avg_loss\\\": 1.0019, \\\"epoch0_avg_ntp\\\": 0.9755, \\\"epoch0_avg_gar\\\": 0.0259, \\\"epoch0_avg_div\\\": 0.0005, \\\"epoch1_avg_loss\\\": 0.9447, \\\"epoch1_avg_ntp\\\": 0.9435, \\\"epoch1_avg_gar\\\": 0.0013, \\\"epoch1_avg_div\\\": 0, \\\"epoch2_avg_loss\\\": 0.9319, \\\"epoch2_avg_ntp\\\": 0.9309, \\\"epoch2_avg_gar\\\": 0.001, \\\"epoch2_avg_div\\\": 0, \\\"final_gate_mean\\\": 0.9598, \\\"final_gate_std\\\": 0.0518, \\\"final_gate_min\\\": 0.7773, \\\"final_gate_max\\\": 1, \\\"final_profile_L3\\\": 0.777, \\\"final_profile_L5\\\": 0.812, \\\"final_profile_L0\\\": 0.875, \\\"final_profile_L27\\\": 1, \\\"training_time_seconds\\\": 21994.5, \\\"training_time_hours\\\": 6.1, \\\"global_steps\\\": 7950, \\\"unexpected_per_layer_variation\\\": true, \\\"eval_modelgen_ours_mid_gar\\\": 0.0149, \\\"eval_modelgen_dongre_mid_gar\\\": 0.0185, \\\"eval_modelgen_ppl\\\": 1.396}}, \\\"phase2_tg_s42_v8_schedsampling\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"Scheduled sampling 应用到 GAR loss（线性从 0→0.5 混合 teacher-forced + model-generated contexts）能缩小 v7 的 30x training-inference GAR gap。机制：在 model-generated context 上计算 GAR loss 迫使 attention pattern 适应推理时分布，直接 address teacher-forcing distribution shift。成功标准：inference GAR 显著高于 v7 的 0.016，PPL 不显著恶化（≤2.78+0.2）。\\\", \\\"conclusion\\\": \\\"failed\\\", \\\"metrics\\\": {\\\"killed_at_microstep\\\": 1950, \\\"total_microsteps\\\": 24000, \\\"completion_pct\\\": 8.1, \\\"global_step_approx\\\": 244, \\\"total_global_steps\\\": 3000, \\\"ss_steps_observed\\\": 1, \\\"tf_lgar_mean_step850_1400\\\": 0.0062, \\\"tf_lgar_std\\\": 0.0082, \\\"tf_lgar_collapse_step\\\": 800, \\\"gate_mean_final\\\": 0.93, \\\"ss_ratio_at_kill\\\": 0.081, \\\"crash_reason\\\": \\\"killed by director: SS path code bug (D026) makes experiment invalid, GPU needed for PCGrad\\\", \\\"design_flaw_ss_ramp_too_slow\\\": true, \\\"design_flaw_no_ss_tf_separate_logging\\\": true}}, \\\"analysis_attention_heatmap\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"四模型（Base/TG/UG/LoRA-only）的 goal attention 衰减模式是否一致？如果 TG 的 attention decay 与 LoRA-only 无差异，则 gating 机制对 attention 分布零增量。\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"base_mean_goal_attn\\\": 0.0136, \\\"base_decay\\\": 0.875, \\\"tg_mean_goal_attn\\\": 0.0232, \\\"tg_decay\\\": 0.777, \\\"ug_mean_goal_attn\\\": 0.0216, \\\"ug_decay\\\": 0.803, \\\"lora_mean_goal_attn\\\": 0.0216, \\\"lora_decay\\\": 0.81, \\\"gating_incremental_benefit\\\": \\\"none\\\"}}, \\\"analysis_gradient_conflict\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"NTP-GAR 梯度冲突在 v7 训练过程中是否逐层普遍存在？量化 cos_sim 和 magnitude ratio 的演化，验证 NTP 是否在训练中逐渐完全压制 GAR 信号。\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"epoch0_cos_sim\\\": -0.089, \\\"epoch1_cos_sim\\\": -0.054, \\\"epoch2_cos_sim\\\": -0.042, \\\"epoch0_neg_layers_pct\\\": 78.6, \\\"epoch1_neg_layers_pct\\\": 71.4, \\\"epoch2_neg_layers_pct\\\": 67.9, \\\"epoch0_mag_ratio\\\": 7.5, \\\"epoch1_mag_ratio\\\": 13.7, \\\"epoch2_mag_ratio\\\": 14.7}}, \\\"phase2_4way_eval_heldout\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"四路消融的三路趋同结论（TG≈UG≈LoRA-only，gating 零增量）在 held-out eval 数据（idx≥8000，与训练集无重叠）上复现，排除数据重叠 confound。预期：相对比较保持（三路趋同），绝对 GAR 值可能变化。\\\", \\\"metrics\\\": {\\\"base_ours_mid_gar\\\": 0.0128, \\\"base_ours_recovery_pp\\\": 0.06, \\\"base_dongre_mid_gar\\\": 0.0031, \\\"base_dongre_recovery_pp\\\": -0.91, \\\"base_ppl\\\": 4.34, \\\"base_ntp\\\": 1.4045, \\\"tg_ours_mid_gar\\\": 0.5035, \\\"tg_ours_recovery_pp\\\": 49.13, \\\"tg_dongre_mid_gar\\\": 0.0152, \\\"tg_dongre_recovery_pp\\\": 0.3, \\\"tg_ppl\\\": 2.78, \\\"tg_ntp\\\": 0.9771, \\\"ug_ours_mid_gar\\\": 0.5053, \\\"ug_ours_recovery_pp\\\": 49.31, \\\"ug_dongre_mid_gar\\\": 0.0124, \\\"ug_dongre_recovery_pp\\\": 0.02, \\\"ug_ppl\\\": 2.78, \\\"ug_ntp\\\": 0.9752, \\\"lora_ours_mid_gar\\\": 0.4978, \\\"lora_ours_recovery_pp\\\": 48.56, \\\"lora_dongre_mid_gar\\\": 0.0132, \\\"lora_dongre_recovery_pp\\\": 0.1, \\\"lora_ppl\\\": 2.78, \\\"lora_ntp\\\": 0.9771, \\\"three_way_convergence_confirmed\\\": true, \\\"gar_ours_spread_pp\\\": 0.75, \\\"ppl_spread\\\": 0, \\\"data_overlap\\\": false}, \\\"conclusion\\\": \\\"success\\\"}, \\\"phase2_4way_eval\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"Turn-residual gating (TRG) improves multi-turn response quality over LoRA-only and base model baselines because it selectively amplifies conversational context signals, which should manifest as higher GAR scores across 4 conditions (base, base+TRG, LoRA, LoRA+TRG).\\\", \\\"conclusion\\\": \\\"negative\\\", \\\"metrics\\\": {\\\"base_ours_mid_gar\\\": 0.0107, \\\"base_ours_recovery_pp\\\": -0.15, \\\"base_dongre_mid_gar\\\": 0.003, \\\"base_dongre_recovery_pp\\\": -0.92, \\\"base_ppl\\\": 4.23, \\\"base_ntp\\\": 1.4162, \\\"tg_ours_mid_gar\\\": 0.4866, \\\"tg_ours_recovery_pp\\\": 47.44, \\\"tg_dongre_mid_gar\\\": 0.0157, \\\"tg_dongre_recovery_pp\\\": 0.35, \\\"tg_ppl\\\": 2.63, \\\"tg_ntp\\\": 0.9484, \\\"ug_ours_mid_gar\\\": 0.4923, \\\"ug_ours_recovery_pp\\\": 48.01, \\\"ug_dongre_mid_gar\\\": 0.013, \\\"ug_dongre_recovery_pp\\\": 0.08, \\\"ug_ppl\\\": 2.62, \\\"ug_ntp\\\": 0.9433, \\\"lora_ours_mid_gar\\\": 0.486, \\\"lora_ours_recovery_pp\\\": 47.39, \\\"lora_dongre_mid_gar\\\": 0.0137, \\\"lora_dongre_recovery_pp\\\": 0.15, \\\"lora_ppl\\\": 2.63, \\\"lora_ntp\\\": 0.9482, \\\"route_b_confirmed\\\": true, \\\"gating_incremental_benefit\\\": \\\"none\\\"}}, \\\"phase2_tg_s42_v5\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"重新平衡超参（λ=1.0 降 GAR 贡献至 ~50%，init_bias=1.5 使 sigmoid≈0.82 接近正常模型行为，gate_lr_multiplier=10 保持）能在 3-epoch 全量训练中产生有意义的 gate 分化（gate_std>0.05），同时 GAR 稳态在 0.1-0.5（非病态饱和），NTP loss 正常收敛，总 loss 保持正值\\\", \\\"metrics\\\": {\\\"step2000_gate_std\\\": 0.0225, \\\"step2000_gate_mean\\\": 0.9586, \\\"step2000_gate_min\\\": 0.9062, \\\"step2000_gate_max\\\": 0.9961, \\\"step2000_L_GAR\\\": -0.8977, \\\"step2000_L_NTP\\\": 0.7611, \\\"step2000_total_loss\\\": -0.1365, \\\"step2400_gate_std\\\": 0.0219, \\\"step2400_gate_mean\\\": 0.9651, \\\"step2400_gate_min\\\": 0.918, \\\"step2400_gate_max\\\": 0.9961, \\\"step2400_profile\\\": \\\"L0=0.918 L12=0.918 L13=0.926 L1=0.996 L26=0.996\\\", \\\"L_GAR_saturated_at\\\": -0.91, \\\"gate_range_compression\\\": \\\"0.918-0.996\\\"}, \\\"conclusion\\\": \\\"negative\\\"}, \\\"phase2_tg_s42_v4\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"重新平衡超参（λ=1.0 降 GAR 贡献至 ~50%，init_bias=1.5 使 sigmoid≈0.82 接近正常模型行为，gate_lr_multiplier=10 保持）能在 3-epoch 全量训练中产生有意义的 gate 分化（gate_std>0.05），同时 GAR 稳态在 0.1-0.5（非病态饱和），NTP loss 正常收敛，总 loss 保持正值\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"phase2_tg_s42_v3b\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"λ=10 + gate_lr=10x + init_bias=0.0 (sigmoid=0.5) 能否驱动 gate 产生 layer 间分化 (gate_std>0.05)？如果 500 步后 gate_std<0.02 且无选择性 → GAR-driven gating 梯度路径确认失败，需要 pivot\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"gate_std_final\\\": 0.087, \\\"gate_mean_final\\\": 0.9388, \\\"gate_min_final\\\": 0.5352, \\\"gate_max_final\\\": 0.9922, \\\"L4_gate\\\": 0.535, \\\"L0_gate\\\": 0.777, \\\"L_NTP_final\\\": 0.7787, \\\"L_GAR_final\\\": -0.9606, \\\"elapsed_seconds\\\": 3565.9, \\\"optimizer_steps\\\": 500, \\\"gate_grad_received\\\": true}}, \\\"phase2_tg_s42_v3\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"ThreadGate + maximize GAR loss (L_GAR=-mean(GAR)) 提供持续非零梯度，避免 hinge loss 的退化平衡点，gate 值应随训练下降（学习到选择性干预），同时 NTP loss 正常收敛\\\", \\\"conclusion\\\": \\\"negative\\\", \\\"metrics\\\": {\\\"gate_mean_step0\\\": 0.8743, \\\"gate_mean_step500\\\": 0.8761, \\\"gate_delta\\\": 0.004, \\\"gate_std\\\": 0.001, \\\"final_ntp_loss\\\": 0.94, \\\"final_gar_loss\\\": -0.019, \\\"gar_contribution_pct\\\": \\\"2-4%\\\", \\\"diagnosis\\\": \\\"gate frozen, GAR indirect gradient too weak\\\"}}, \\\"phase2_tg_s42_v2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"ThreadGate + 修复后的 cumulative GAR loss (ε=0.001) 在 L_NTP+L_GAR 联合训练后，mid-turn GAR recovery 应显著优于 v1 (NTP-only baseline)，验证 GAR loss 的有效性\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"phase1_gar_diag\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"Qwen2.5-7B-Instruct 在 10-turn 多轮对话中，中间 turns (3-8) 的 GAR (Goal Accessibility Ratio) 相对 turn-1 下降 ≥15%，表明模型对 system prompt 中目标 token 的注意力随对话进行显著衰减\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"turn1_avg_gar\\\": 0.0418, \\\"mid_turns_avg_gar\\\": 0.0122, \\\"relative_drop\\\": 0.708, \\\"num_conversations\\\": 5, \\\"num_turns\\\": 10, \\\"per_turn_avg_gar\\\": [0.0418, 0.0241, 0.0224, 0.013, 0.0133, 0.0086, 0.0078, 0.008, 0.0157, 0.0064]}}}, \\\"count\\\": 53, \\\"total\\\": 53, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.1764}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {\"phase1a_multiseed_qwen\": {\"status\": \"DONE\", \"hypothesis\": \"Multi-seed (s123, s456) training across 5 Qwen conditions (PCGrad, UG, LoRA-only, TG, SS) to establish mean±std for all claims. 8 training runs + AR eval N≥50 each. Expect TF convergence (GAR~0.50) and consistent AR rankings across seeds.\", \"conclusion\": \"killed\"}, \"p1_ss_lora_only\": {\"status\": \"DONE\", \"hypothesis\": \"SS training on LoRA-only checkpoint (no ThreadGate) with same hyperparameters (rho_max=0.3, same schedule) should achieve similar GAR improvement as SS+TG. If confirmed, this proves the SS fix is architecture-agnostic, strengthening the paper's mitigation story (the gap is caused by exposure bias in any auxiliary-loss setup, and SS fixes it regardless of gating mechanism).\", \"conclusion\": \"killed\"}, \"phase2_switching\": {\"status\": \"DONE\", \"hypothesis\": \"TF→AR switching at turn k (k=1..5) on ThreadGate s42 checkpoint. If GAR drops abruptly at the switch point (matching pure-AR level within 1 turn), it confirms exposure bias as instantaneous distribution shift rather than gradual KV cache drift. Staircase = exposure bias dominant; linear slope = KV drift dominant.\", \"conclusion\": \"killed\"}, \"p1_llama_ss_eval\": {\"status\": \"DONE\", \"hypothesis\": \"Llama SS (2-epoch) reduces the TF-AR GAR gap on Llama-3.1-8B, confirming SS as model-general mitigation (C4+C5). Eval: TF+AR N=50 β=0/3/5.\", \"conclusion\": \"success\", \"metrics\": {\"ss_tf_gar\": 0.477, \"ss_tf_ppl\": 2.82, \"ss_ar_b0_gar\": 0.1662, \"ss_ar_b0_ppl\": 1.37, \"ss_ar_b5_gar\": 0.7905, \"ss_ar_b5_ppl\": 1.81, \"base_ar_gar\": 0.0179, \"base_ar_ppl\": 1.22, \"tf_ar_gap\": 2.87}}, \"p1_llama_ss_training\": {\"status\": \"DONE\", \"hypothesis\": \"SS is effective on Qwen (gap 8x to 1.4x). If SS also reduces the TF-AR gap on Llama-3.1-8B, it confirms SS as a model-general mitigation, strengthening C4 (mitigation) and C5 (cross-model) claims.\", \"conclusion\": \"success\"}, \"mmlu_eval_all\": {\"status\": \"DONE\", \"hypothesis\": \"ThreadGate's per-layer gating and auxiliary GAR loss do not degrade the model's general language understanding capabilities. All fine-tuned variants (TG/UG/LO/PCGrad/SS) should maintain MMLU 5-shot accuracy within 1pp of the Base LoRA-only checkpoint, confirming that attention steering is additive rather than destructive.\", \"conclusion\": \"success\", \"metrics\": {\"base_qwen\": 0.7423, \"pcgrad_v9_s42\": 0.7386, \"ss_v8b_s42\": 0.7375, \"lo_s42\": 0.7357, \"tg_v7_s42\": 0.7347, \"ug_s42\": 0.7346}}, \"p2_llama_gradient_conflict\": {\"status\": \"DONE\", \"hypothesis\": \"PCGrad fails to improve AR GAR on Llama-3.1-8B (as on Qwen), confirming cross-model that gradient conflict is not the root cause of the TF-AR gap, strengthening C2 (causal exclusion).\", \"conclusion\": \"success\", \"metrics\": {\"cos_sim_mean\": 0.0045, \"cos_sim_std\": 0.07, \"neg_cos_sim_layers_pct\": 53.1, \"mag_ratio_median\": 25.7, \"conclusion_note\": \"cos_sim≈0 indicates near-orthogonal (NOT conflict). Script conclusion text 'widespread conflict' is misleading — actual finding: NTP and GAR gradients are nearly orthogonal on Llama, consistent with Qwen pattern.\"}}, \"p1_tf_ar_kl_divergence\": {\"status\": \"DONE\", \"hypothesis\": \"TF and AR attention distributions diverge more on GAR-relevant heads (high gate values) than non-relevant heads, providing mechanistic evidence that exposure bias selectively disrupts goal-attending computation rather than uniformly degrading attention.\", \"metrics\": {\"tg_delta_gar\": 0.0165, \"base_delta_gar\": 0.0122, \"tg_mean_kl\": 0.054, \"base_mean_kl\": 0.043, \"gate_kl_correlation\": 0.11, \"high_kl_layers\": \"L23-L27, L9\", \"gar_robustness_ours_tg_base_ratio\": 21.4, \"gar_robustness_goal_only_ratio\": 63, \"gar_robustness_ours_all_ratio\": 1.7, \"gar_robustness_ours_first_ratio\": 1.8}, \"conclusion\": \"success\"}, \"qwen15b_phase1_diag\": {\"status\": \"DONE\", \"hypothesis\": \"GAR attention decay toward system-prompt goal tokens is a general phenomenon across model scales, not specific to 7B. Qwen-2.5-1.5B-Instruct should also show progressive GAR decline across conversation turns, confirming the phenomenon is architecture-level rather than scale-dependent.\", \"conclusion\": \"success\"}, \"d048_eval_ss_s456\": {\"status\": \"DONE\", \"hypothesis\": \"SS s456 eval: TF + AR N=50 + bootstrap CI to complete 3-seed SS metrics. Together with s42 and s123, establishes mean±std for C2 reviewer requirement.\", \"conclusion\": \"success\", \"metrics\": {\"tf_gar_ours_mid\": 0.4964, \"tf_gar_dongre_mid\": 0.3862, \"ar_beta0_gar\": 0.4325, \"ar_beta0_ppl\": 1.4394, \"ar_beta3_gar\": 0.605, \"ar_beta3_ppl\": 1.5868, \"ar_beta5_gar\": 0.7157, \"ar_beta5_ppl\": 1.8045, \"n_convs_ar\": 50}}, \"d048_ss_s456\": {\"status\": \"DONE\", \"hypothesis\": \"Scheduled sampling (ratio=0.3) with ThreadGate multi-seed (s456) to establish 3-seed mean±std for C2 reviewer requirement of at least 3 seeds\", \"conclusion\": \"success\"}, \"d048_eval_ss_s123\": {\"status\": \"DONE\", \"hypothesis\": \"SS s123 eval: TF + AR N=50 + bootstrap CI to establish multi-seed SS metrics. Expect TF GAR ~0.50, AR GAR similar to s42 (0.347), confirming SS effectiveness across seeds.\", \"conclusion\": \"success\", \"metrics\": {\"tf_gar_ours\": 0.5536, \"tf_gar_dongre\": 0.4106, \"tf_ppl\": 2.6123, \"ar_beta0_gar\": 0.4231, \"ar_beta0_ppl\": 1.4408, \"ar_beta3_gar\": 0.5903, \"ar_beta3_ppl\": 1.607, \"ar_beta5_gar\": 0.7174, \"ar_beta5_ppl\": 1.7852, \"n_convs_tf\": 200, \"n_convs_ar\": 39}}, \"d048_ss_s123\": {\"status\": \"DONE\", \"hypothesis\": \"Scheduled sampling (ratio=0.3) with ThreadGate multi-seed (s123) to establish 3-seed mean±std for C2 reviewer requirement. Corrected hyperparams matching d048_ss_s456.\", \"conclusion\": \"success\"}, \"d048_split_softmax_eval\": {\"status\": \"DONE\", \"hypothesis\": \"Split-softmax (Li et al., COLM 2024) post-softmax rescaling recovers AR GAR without the PPL cost of pre-softmax additive steering, providing an alternative inference-time intervention that separates attention allocation from logit distribution.\", \"conclusion\": \"failed\"}, \"d048_final_ar_eval\": {\"status\": \"DONE\", \"hypothesis\": \"Unified AR N=50 eval across 6 conditions (Base/TG/UG/LO/PCGrad/SS) with bootstrap CI and Wilcoxon tests to establish statistically rigorous comparisons for all claims\", \"conclusion\": \"success\", \"metrics\": {\"beta0\": {\"base_gar\": 0.019, \"tg_gar\": 0.064, \"ug_gar\": 0.033, \"lo_gar\": 0.037, \"pcgrad_gar\": 0.03, \"ss_gar\": 0.347}, \"beta3\": {\"base_gar\": 0.531, \"tg_gar\": 0.556, \"ss_gar\": 0.593}, \"beta5\": {\"base_gar\": 0.704, \"tg_gar\": 0.727, \"ss_gar\": 0.717}, \"wilcoxon_beta0\": {\"tg_vs_base_p\": \"<0.001\", \"tg_vs_base_r\": 0.802, \"ss_vs_tg_p\": \"<0.001\", \"ss_vs_tg_r\": 0.869}, \"ppl\": {\"base\": 1.447, \"tg\": 1.432, \"ss\": 1.442}, \"n_convs\": 39}}, \"d048_eval_ss_s42\": {\"status\": \"DONE\", \"hypothesis\": \"D048 multi-seed SS s42 eval: TF + AR N=50 + bootstrap CI (curve[2:]) to establish mean±std for scheduled sampling. Expect TF GAR ~0.50, AR GAR gap < 2× (vs base ~31×), PPL stable.\", \"metrics\": {\"tf\": {\"base_gar_ours_mid\": 0.0128, \"base_gar_dongre_mid\": 0.0031, \"base_ppl\": 4.34, \"base_ntp\": 1.4, \"tg_gar_ours_mid\": 0.5025, \"tg_gar_dongre_mid\": 0.389, \"tg_ppl\": 2.78, \"tg_ntp\": 0.98, \"baseline_mid_gar\": 0.0122}, \"ar\": {\"gar_ours_mid\": 0.3887, \"gar_ours_ci_95\": [0.3692, 0.3934], \"ppl\": 1.35}, \"gap_ratio\": 1.29, \"n_conversations_tf\": 50, \"n_conversations_ar\": 5, \"bootstrap_turns\": \"curve[2:] (turns 3-T)\", \"note\": \"AR used hardcoded N=5, not N=50. Will be re-evaluated in final unified batch with eval_200.json N=50.\"}, \"conclusion\": \"success\"}, \"d048_ss_s42\": {\"status\": \"DONE\", \"hypothesis\": \"Scheduled sampling (ratio=0.3) with ThreadGate reduces the ~30× TF-AR GAR gap by exposing the model to its own generated text during training. Multi-seed run (s42) under D048 unified protocol to establish mean±std for statistical testing. SS is the strongest mitigation candidate (prior single-seed showed gap 31×→1.57×).\", \"conclusion\": \"success\", \"metrics\": {\"final_avg_loss\": 0.9326, \"final_ntp_loss\": 0.932, \"final_gar_loss\": 0.0007, \"gate_mean\": 0.9527, \"gate_std\": 0.0589, \"gate_min\": 0.7383, \"gate_min_layer\": \"L4\", \"gate_max\": 1, \"ss_usage\": \"4750/16000 (29.7%)\", \"ss_fallback\": 0, \"epochs_completed\": 3, \"wall_clock_s\": 23418, \"wall_clock_h\": 6.5}}, \"eval_llama_ar_n20\": {\"status\": \"DONE\", \"hypothesis\": \"N=20 AR eval stabilizes Llama 3-way (Base/TG/LoRA-only) autoregressive GAR estimates. N=5 suffered from outlier influence (3/5 conv had GAR>0.4 outlier turns); N=20 provides robust mean±std.\", \"metrics\": {\"base\": {\"gar_ours_mean\": 0.0088, \"gar_ours_std\": 0.0056, \"gar_ours_median_per_conv\": 0.0093, \"gar_ours_median_per_turn_pool\": 0.0071, \"gar_ours_spike_ratio\": \"0%\", \"gar_dongre_mean\": 0.0049, \"gar_dongre_std\": 0.0013, \"gar_dongre_median\": 0.0047, \"ngar_ours_mid\": 0.1019, \"ngar_dongre_mid\": 0.1171, \"ppl\": 1.293, \"ppl_std\": 0.07, \"ntp_loss\": 0.2552}, \"tg\": {\"gar_ours_mean\": 0.0434, \"gar_ours_std\": 0.1002, \"gar_ours_median_per_conv\": 0.0179, \"gar_ours_median_per_turn_pool\": 0.0126, \"gar_ours_spike_ratio\": \"5% (2/40 turns GAR>=0.4)\", \"gar_dongre_mean\": 0.0183, \"gar_dongre_std\": 0.0198, \"gar_dongre_median\": 0.0152, \"ngar_ours_mid\": 0.5357, \"ngar_dongre_mid\": 0.4436, \"ppl\": 1.437, \"ppl_std\": 0.077, \"ntp_loss\": 0.3612}, \"lora_only\": {\"gar_ours_mean\": 0.0284, \"gar_ours_std\": 0.0481, \"gar_ours_median_per_conv\": 0.0184, \"gar_ours_median_per_turn_pool\": 0.0133, \"gar_ours_spike_ratio\": \"0%\", \"gar_dongre_mean\": 0.0205, \"gar_dongre_std\": 0.0241, \"gar_dongre_median\": 0.016, \"ngar_ours_mid\": 0.3488, \"ngar_dongre_mid\": 0.4997, \"ppl\": 1.419, \"ppl_std\": 0.075, \"ntp_loss\": 0.3483}, \"n_conversations\": 20, \"n_turns\": 4, \"mid_turns_definition\": \"turns 3-T (0-indexed avg_gar[2:], excluding turns 1-2). All 16 eval entries use same definition.\", \"stat_pool\": \"median_per_conv: median of 20 per-conversation mid-turn averages. median_per_turn_pool: median of 40 individual turn values (20 conv x 2 mid turns).\", \"ranking_gar_ours_mean\": \"TG(0.0434) > LO(0.0284) > Base(0.0088)\", \"ranking_gar_ours_median_per_conv\": \"TG(0.0179) ≈ LO(0.0184) > Base(0.0093)\", \"ranking_gar_ours_median_per_turn_pool\": \"TG(0.0126) ≈ LO(0.0133) > Base(0.0071)\", \"ranking_gar_dongre\": \"LO(0.0205) > TG(0.0183) > Base(0.0049)\", \"note\": \"Paper §5.5 cites median_per_conv (median of per-conversation mid-turn averages across N=20). median_per_turn_pool is the alternative statistic from pooled individual turns. Both confirm TG ≈ LO (zero-increment).\"}, \"conclusion\": \"success\"}, \"eval_llama_lora_only_s42\": {\"status\": \"DONE\", \"hypothesis\": \"LoRA-only ablation (no gate) on Llama-3.1-8B: if TG's GAR improvement comes from the gate, LoRA-only should show minimal GAR recovery vs base.\", \"metrics\": {\"tf\": {\"gar_ours\": 0.4807, \"gar_dongre\": 0.0188, \"ngar_ours\": 11.8031, \"ngar_dongre\": 0.8261, \"ppl\": 2.6, \"ntp_loss\": 0.9366, \"n_conversations\": 50, \"n_turns\": 4}, \"ar\": {\"gar_ours\": 0.0617, \"gar_dongre\": 0.0226, \"ngar_ours\": 0.6065, \"ngar_dongre\": 0.2537, \"ppl\": 1.32, \"ntp_loss\": 0.2787, \"n_conversations\": 5, \"n_turns\": 10}, \"gap_ratio_gar_ours\": 7.79}, \"conclusion\": \"success\"}, \"llama_lora_only_s42\": {\"status\": \"DONE\", \"hypothesis\": \"Llama-3.1-8B LoRA-only baseline (gate=none, 无 gating 机制): 与 Llama TG s42 对比，验证 gating 对 Llama 的增量贡献。如果 LoRA-only GAR ≈ TG GAR → gating 零增量与 Qwen 结论一致（C5 跨模型）。\", \"conclusion\": \"success\", \"metrics\": {\"final_avg_loss\": 0.9288, \"final_avg_ntp\": 0.9279, \"final_avg_gar\": 0.0009, \"gate_fixed\": 1, \"gate_type\": \"none\", \"wall_clock_s\": 25317, \"wall_clock_h\": 7.03, \"epochs_completed\": 3}}, \"phase2_tg_s42_v6\": {\"status\": \"DONE\", \"hypothesis\": \"smooth_saturation loss (-target*tanh(GAR/target), target=0.5) 提供有界但持续的 GAR 梯度，避免 maximize 的恒等退化（gate→1）和 hinge_target 的梯度消失（GAR达标后梯度=0）。预期：gate_std>0.05 的层间分化 + GAR 稳态在 0.3-0.5 + NTP loss 正常收敛 + 总 loss 为正。\", \"metrics\": {\"dryrun_step0_L_NTP\": 2.0275, \"dryrun_step0_L_GAR\": -0.0161, \"dryrun_step0_total_loss\": 2.0114, \"dryrun_step4_L_NTP\": 1.6544, \"dryrun_step4_L_GAR\": -0.0147, \"dryrun_step4_total_loss\": 1.6397, \"dryrun_gate_grad\": true, \"dryrun_gate_mean_init\": 0.8097, \"dryrun_gate_std_init\": 0.0341, \"dryrun_gate_min_init\": 0.6836, \"dryrun_gate_max_init\": 0.8672, \"dryrun_gate_mean_step5\": 0.8025, \"dryrun_gate_std_step5\": 0.0842, \"dryrun_gate_min_step5\": 0.5547, \"dryrun_gate_max_step5\": 0.9805, \"gs50_gate_mean\": 0.8117, \"gs50_gate_std\": 0.0612, \"gs50_gate_min\": 0.6836, \"gs50_gate_max\": 0.9805, \"gs100_gate_mean\": 0.8737, \"gs100_gate_std\": 0.0367, \"gs100_gate_min\": 0.8164, \"gs100_gate_max\": 0.9766, \"gs100_L_NTP\": 0.8151, \"gs100_L_GAR\": -0.158, \"gs100_total_loss\": 0.6571, \"gs100_profile_bottom3\": \"L12=0.816 L4=0.824 L13=0.824\", \"gs100_profile_top3\": \"L27=0.977 L26=0.961 L23=0.914\", \"gs143_L_GAR\": -0.3876, \"gs143_gate_mean\": 0.9227}, \"conclusion\": \"negative\"}, \"phase2_tg_s42\": {\"status\": \"DONE\", \"hypothesis\": \"ThreadGate (turn-conditional gating) 在 L_NTP+L_GAR 联合训练后，相比 Uniform Gate，mid-turn GAR recovery 高出 ≥3pp，验证 Cesaro 理论预测：position-conditional 干预优于 uniform 干预\", \"conclusion\": \"negative\", \"metrics\": {\"final_ntp_loss\": 0.94, \"final_gar_loss\": 0, \"gate_mean\": 0.988, \"gar_loss_zero_pct\": 87.6, \"epochs_completed\": 1.67, \"killed_reason\": \"SIGTERM by diagnose worker (unauthorized)\"}}, \"eval_v7_tg_s123\": {\"status\": \"DONE\", \"hypothesis\": \"v7 TG s123 eval: 验证 s123 seed 的 TF-AR GAR gap 与 s42 一致（~32×），确认 multi-seed robustness\", \"conclusion\": \"success\", \"metrics\": {\"iid_tf\": {\"gar_ours_mid\": 0.5052, \"gar_dongre_mid\": 0.0119, \"ppl\": 2.7802, \"ntp\": 0.9752}, \"modelgen_ar\": {\"gar_ours_mid\": 0.0165, \"gar_dongre_mid\": 0.0177, \"ppl\": 1.3855, \"ntp\": 0.3223}, \"gap_ratio\": 30.6, \"comparison_s42\": {\"tf_gar_ours_delta\": 0.0017, \"ar_gar_ours_delta\": 0.0008, \"gap_ratio_delta\": -1.4}}}, \"eval_v8b_ss_s123\": {\"status\": \"DONE\", \"hypothesis\": \"v8b SS model trained with s123 seed should reproduce s42 GAR metrics within acceptable gap_ratio [1.2x-2.5x] and no PPL degradation, confirming seed robustness of the scheduled sampling approach\", \"conclusion\": \"success\", \"metrics\": {\"iid\": {\"gar_ours\": 0.503, \"gar_dongre\": 0.394, \"ppl\": 2.781, \"ntp_loss\": 0.976, \"n_conv\": 50, \"n_turns\": 3}, \"modelgen\": {\"gar_ours\": 0.418, \"gar_dongre\": 0.441, \"ppl\": 1.389, \"ntp_loss\": 0.325, \"n_conv\": 5, \"n_turns\": 10}, \"gap_ratio\": 1.2, \"base_iid_ppl\": 4.338, \"base_modelgen_ppl\": 1.351}}, \"v7_tg_s123\": {\"status\": \"DONE\", \"hypothesis\": \"v7 TG s42 已验证 ThreadGate 有效性，s123 验证 seed robustness。预期 gate profile 和 GAR 收敛模式与 s42 一致。\", \"conclusion\": \"success\", \"metrics\": {\"epoch_1\": {\"avg_loss\": 0.9447, \"avg_ntp_loss\": 0.9434, \"avg_gar_loss\": 0.0013, \"avg_div_loss\": 0}, \"epoch_2\": {\"avg_loss\": 0.9315, \"avg_ntp_loss\": 0.9305, \"avg_gar_loss\": 0.001, \"avg_div_loss\": 0}, \"final_gate\": {\"mean\": 0.9467, \"std\": 0.051, \"min\": 0.793, \"max\": 1}, \"final_gate_profile\": {\"L0\": 0.883, \"L1\": 0.793, \"L2\": 0.996, \"L3\": 0.988, \"L4\": 0.984, \"L5\": 0.797, \"L6\": 0.961, \"L7\": 0.918, \"L8\": 0.965, \"L9\": 0.934, \"L10\": 0.969, \"L11\": 0.918, \"L12\": 0.926, \"L13\": 0.941, \"L14\": 0.93, \"L15\": 0.965, \"L16\": 0.941, \"L17\": 0.91, \"L18\": 0.961, \"L19\": 0.965, \"L20\": 0.973, \"L21\": 0.988, \"L22\": 0.969, \"L23\": 0.98, \"L24\": 0.98, \"L25\": 0.984, \"L26\": 0.988, \"L27\": 1}, \"training_time_s\": 21425.2}}, \"v8b_ss_s123\": {\"status\": \"DONE\", \"hypothesis\": \"v8b SS s42 成功（gap 32×→1.57×），s123 验证结果的 seed robustness。预期 model-gen GAR 同样显著提升，PPL 无恶化。\", \"conclusion\": \"success\", \"metrics\": {\"final_loss\": 0.9316, \"final_ntp_loss\": 0.9307, \"final_gar_loss\": 0.0009, \"final_gate_mean\": 0.9505, \"final_gate_std\": 0.0508, \"final_gate_min\": 0.7383, \"final_gate_max\": 1, \"ss_used_ratio\": 0.371, \"training_time_s\": 38773.4, \"epoch0_loss\": 1.0092, \"epoch1_loss\": 0.9444, \"epoch2_loss\": 0.9316}}, \"llama_ar_matched_eval\": {\"status\": \"DONE\", \"hypothesis\": \"用 matched 设置 (N=50/T=4) 重跑 Llama AR eval，消除 TF/AR 设置差异。与 TF 结果对比得到可直接写入论文的 gap ratio，验证 TG 在 AR 模式下仍能提升 GAR。\", \"conclusion\": \"success\", \"metrics\": {\"ar_base_ours\": {\"mid_gar\": 0.0082, \"ngar\": 0.1, \"ppl\": 1.267}, \"ar_tg_ours\": {\"mid_gar\": 0.0388, \"ngar\": 0.493, \"ppl\": 1.413}, \"ar_base_dongre\": {\"mid_gar\": 0.0051, \"ngar\": 0.12, \"ppl\": 1.267}, \"ar_tg_dongre\": {\"mid_gar\": 0.018, \"ngar\": 0.431, \"ppl\": 1.413}, \"tf_reference\": {\"tf_tg_ours_ngar\": 11.88, \"tf_base_ours_ngar\": 0.388, \"tf_tg_ours_raw\": 0.4836, \"tf_tg_dongre_raw\": 0.018}, \"matched_gap_analysis\": {\"gar_ours_raw_gap\": \"12.5x (TF 0.484 / AR 0.039)\", \"gar_ours_ngar_gap\": \"24.1x (TF 11.88 / AR 0.493)\", \"gar_dongre_raw_gap\": \"1.002x (TF 0.018 / AR 0.018) — zero gap\", \"tg_over_base_ar_ours\": \"4.71x\", \"tg_over_base_ar_dongre\": \"3.54x\", \"conclusion\": \"GAR-ours TF-AR gap 12.5x (raw) / 24x (nGAR) is genuine exposure bias. GAR-Dongre zero gap (1.002x) confirms mechanism specificity: exposure bias selectively destroys learned goal-attention routing while leaving content-overlap-based attention unaffected.\"}}}, \"instruction_retention_test\": {\"status\": \"DONE\", \"hypothesis\": \"Turn-level residual gating (β=3) preserves instruction-following ability across multi-turn conversations better than the baseline (β=0), because gating modulates residual contributions to retain earlier context signals rather than letting them decay through successive transformer layers.\", \"conclusion\": \"success\", \"metrics\": {\"late_turn_rate_beta0\": 0.759, \"late_turn_rate_beta3\": 0.87, \"late_turn_delta\": 0.111, \"mcnemar_chi2\": 3.125, \"mcnemar_p\": 0.0771, \"gar_compliance_r\": 0.2003, \"gar_compliance_p\": 0.007, \"category_content_constraint\": {\"beta0\": 0.619, \"beta3\": 0.857, \"delta\": 0.238}, \"category_count_constraint\": {\"beta0\": 1, \"beta3\": 1, \"delta\": 0}, \"category_format_constraint\": {\"beta0\": 1, \"beta3\": 1, \"delta\": 0}, \"category_position_constraint\": {\"beta0\": 0.667, \"beta3\": 0.733, \"delta\": 0.067}}}, \"llama_eval_s42\": {\"status\": \"DONE\", \"hypothesis\": \"Llama-3.1-8B TG eval: 如果 Llama TG 模型在 TF 模式下 GAR-ours 显著高于 AR 模式（如 Qwen v7 的 20-33x gap），则确认 training-inference GAR gap 跨模型泛化（C5）。同时测量 base model 作为 control。\", \"metrics\": {\"tf_base\": {\"gar_ours\": 0.0166, \"ngar_ours\": 0.3882, \"gar_dongre\": 0.0038, \"ngar_dongre\": 0.163, \"ppl\": 3.45, \"N\": 50, \"T\": 4}, \"tf_tg\": {\"gar_ours\": 0.4836, \"ngar_ours\": 11.8818, \"gar_dongre\": 0.018, \"ngar_dongre\": 0.7922, \"ppl\": 2.57, \"N\": 50, \"T\": 4}, \"ar_base\": {\"gar_ours\": 0.0086, \"ngar_ours\": 0.0798, \"gar_dongre\": 0.0118, \"ngar_dongre\": 0.1265, \"ppl\": 1.24, \"N\": 5, \"T\": 10}, \"ar_tg\": {\"gar_ours\": 0.0304, \"ngar_ours\": 0.2632, \"gar_dongre\": 0.0217, \"ngar_dongre\": 0.2459, \"ppl\": 1.32, \"N\": 5, \"T\": 10}, \"gap_ratio_tg_ours\": 15.9, \"gap_ratio_base_ours\": 1.93, \"gap_ratio_tg_dongre\": 0.83, \"vs_qwen_v7_gap_ratio\": 32.1, \"baseline_mid_gar\": 0.0122}, \"conclusion\": \"success\"}, \"llama_tg_s42\": {\"status\": \"DONE\", \"hypothesis\": \"在 Llama-3.1-8B-Instruct 上训练 ThreadGate（与 Qwen v7 相同配置），验证 C5：gating mechanism 和 GAR training-inference gap 跨模型泛化。如果 Llama TG 也出现 IID GAR ≈ target 但 model-gen GAR 坍塌 → 确认 exposure bias 的跨模型通用性。\", \"conclusion\": \"success\", \"metrics\": {\"epochs_completed\": 3, \"total_steps\": 3000, \"wall_clock_seconds\": 26212, \"wall_clock_hours\": 7.28, \"final_avg_loss\": 0.9233, \"final_avg_ntp\": 0.9224, \"final_avg_gar\": 0.0009, \"final_avg_div\": 0, \"final_gate_mean\": 0.9099, \"final_gate_std\": 0.0701, \"final_gate_min\": 0.7188, \"final_gate_max\": 0.9922, \"gate_profile_step3000\": {\"L0\": 0.957, \"L1\": 0.973, \"L2\": 0.977, \"L3\": 0.965, \"L4\": 0.992, \"L5\": 0.969, \"L6\": 0.957, \"L7\": 0.957, \"L8\": 0.961, \"L9\": 0.949, \"L10\": 0.938, \"L11\": 0.934, \"L12\": 0.969, \"L13\": 0.953, \"L14\": 0.957, \"L15\": 0.965, \"L16\": 0.953, \"L17\": 0.961, \"L18\": 0.922, \"L19\": 0.902, \"L20\": 0.883, \"L21\": 0.863, \"L22\": 0.836, \"L23\": 0.844, \"L24\": 0.809, \"L25\": 0.719, \"L26\": 0.762, \"L27\": 0.805, \"L28\": 0.801, \"L29\": 0.855, \"L30\": 0.898, \"L31\": 0.934}, \"checkpoint_size_gate_mb\": 4.2, \"checkpoint_size_lora_mb\": 26, \"gpu\": \"NVIDIA RTX PRO 6000 Blackwell\", \"vram_gb\": 102, \"mem_used_gb\": 63.4}}, \"attention_steering_gen_n50\": {\"status\": \"DONE\", \"hypothesis\": \"N=5 gen steering 显示 β∈[2,5] phase transition (GAR 0.06→0.68)，但样本量不足以报告置信区间。N=50 conversations 应重现同一 phase transition pattern 并提供统计鲁棒的 mean±std，加固 C6 claim (attention steering as causal mechanism proof)。\", \"metrics\": {\"corrected\": true, \"aggregation\": \"per-conv mid_gar(turns 2-7), >=3 turns only\", \"beta_0.0\": {\"mid_gar\": 0.0641, \"mid_gar_std\": 0.0809, \"ppl\": 1.4324, \"ppl_std\": 0.1029, \"n_valid\": 39}, \"beta_2.0\": {\"mid_gar\": 0.128, \"mid_gar_std\": 0.1101, \"ppl\": 1.4822, \"ppl_std\": 0.1385, \"n_valid\": 39}, \"beta_3.0\": {\"mid_gar\": 0.5558, \"mid_gar_std\": 0.0601, \"ppl\": 1.5605, \"ppl_std\": 0.1719, \"n_valid\": 39}, \"beta_4.0\": {\"mid_gar\": 0.6439, \"mid_gar_std\": 0.0607, \"ppl\": 1.6674, \"ppl_std\": 0.2241, \"n_valid\": 39}, \"beta_5.0\": {\"mid_gar\": 0.7271, \"mid_gar_std\": 0.0605, \"ppl\": 1.7723, \"ppl_std\": 0.2693, \"n_valid\": 38}, \"beta_10.0\": {\"mid_gar\": 0.9612, \"mid_gar_std\": 0.0152, \"ppl\": 3.4517, \"ppl_std\": 1.7813, \"n_valid\": 39}, \"n_convs_total\": 50, \"n_convs_valid\": 39, \"mode\": \"gen\", \"phase_transition_range\": \"[2, 3]\"}, \"conclusion\": \"success\"}, \"phase2_tg_s42_v8b_resume\": {\"status\": \"DONE\", \"hypothesis\": \"从 epoch_0 checkpoint resume v8b scheduled sampling 训练。SS 线性混合 0→0.5 teacher-forced + model-generated contexts。如果 model-gen context 上的 GAR 训练能缩小 30x training-inference gap → exposure bias mitigation 有效。成功标准：inference GAR 显著高于 v7 的 0.016 (至少 +1pp)，PPL 不恶化。\", \"metrics\": {\"training\": {\"total_steps\": 3000, \"epochs_completed\": 3, \"wall_clock_hours\": 8.1, \"final_loss\": 0.933, \"final_ntp_loss\": 0.9322, \"final_gar_loss\": 0.0008, \"final_gate_mean\": 0.9586, \"final_gate_std\": 0.0582, \"ss_ratio\": 0.5}, \"eval_iid\": {\"gar_ours\": 0.4983, \"gar_dongre\": 0.3855, \"ppl\": 2.78}, \"eval_modelgen\": {\"gar_ours\": 0.3177, \"gar_dongre\": 0.3533, \"ppl\": 1.38}, \"vs_v7\": {\"iid_gar_ours_delta\": -0.005, \"modelgen_gar_ours_delta\": 0.302, \"gap_ratio_v7\": 32, \"gap_ratio_v8b\": 1.57}}, \"conclusion\": \"success\"}, \"llama_phase1_gar_diag\": {\"status\": \"DONE\", \"hypothesis\": \"Llama-3.1-8B-Instruct 在 multi-turn dialogue 中也应出现 goal attention decay（与 Qwen-2.5-7B 类似），确认 attention decay 是 transformer 架构通用现象而非模型特有。Phase 1 诊断：测量 base Llama 的 per-turn GAR profile。\", \"conclusion\": \"success\", \"metrics\": {\"per_turn_gar\": {\"turn_1\": 0.0263, \"turn_2\": 0.0183, \"turn_3\": 0.0087, \"turn_4\": 0.0055, \"turn_5\": 0.006, \"turn_6\": 0.0035, \"turn_7\": 0.0038, \"turn_8\": 0.0037, \"turn_9\": 0.005, \"turn_10\": 0.0026}, \"t1_t10_decay_pct\": 90.1, \"t1_mid38_drop_pct\": 80.2, \"n_topics\": 5, \"model\": \"Meta-Llama-3.1-8B-Instruct\", \"mode\": \"gen\", \"n_conversations\": 5, \"n_turns\": 10}}, \"eval_v8b_ss\": {\"status\": \"DONE\", \"hypothesis\": \"Scheduled Sampling (linear 0→0.5 mixing of teacher-forced and model-gen contexts) closes the 30x training-inference GAR gap by reducing exposure bias, resulting in model-gen GAR significantly above v7 baseline (0.016) while preserving IID GAR and PPL.\", \"metrics\": {\"iid_gar_ours\": 0.4983, \"iid_gar_dongre\": 0.3855, \"iid_ppl\": 2.78, \"iid_ngar_ours\": 13.5, \"iid_ngar_dongre\": 22.68, \"modelgen_gar_ours\": 0.3177, \"modelgen_gar_dongre\": 0.3533, \"modelgen_ppl\": 1.38, \"modelgen_ngar_ours\": 4.47, \"modelgen_ngar_dongre\": 5.92, \"iid_turn1_gar_ours\": 0.5398, \"modelgen_turn1_gar_ours\": 0.4333}, \"conclusion\": \"success\"}, \"attention_steering_eval200_tf\": {\"status\": \"DONE\", \"hypothesis\": \"N=200 TF 模式 attention steering 验证 β-GAR 关系的统计鲁棒性。在 teacher-forced context (无 exposure bias) 下，steering 效果应更温和（baseline GAR 已 ~0.50），但仍展示 β 调控 attention 的能力。与 N=5 gen 模式结果互补：tf 验证机制可控性，gen 验证因果闭环。\", \"metrics\": {\"beta_0.0\": {\"mid_gar\": 0.5353, \"ppl\": 2.62}, \"beta_2.0\": {\"mid_gar\": 0.6112, \"ppl\": 2.69}, \"beta_3.0\": {\"mid_gar\": 0.788, \"ppl\": 2.93}, \"beta_4.0\": {\"mid_gar\": 0.8165, \"ppl\": 3.49}, \"beta_5.0\": {\"mid_gar\": 0.8325, \"ppl\": 6.15}, \"beta_10.0\": {\"mid_gar\": 0.977, \"ppl\": 505.21}, \"n_convs\": 200, \"mode\": \"tf\"}, \"conclusion\": \"success\"}, \"trc_baseline_v7_tg\": {\"status\": \"DONE\", \"hypothesis\": \"如果 exposure bias 对 auxiliary objectives 的破坏跨特征空间通用，那么 TRC (hidden state cos_sim) 在 model-gen 下也应出现与 GAR (attention 空间) 类似的 TF/gen gap。在 v7 TG / LoRA-only / base 三个 checkpoint 上测量 TRC baseline，确认 gap 是否存在。成功标准：gen TRC 显著低于 TF TRC。\", \"conclusion\": \"success\", \"metrics\": {\"v7_tg\": {\"tf_trc\": 0.3339, \"gen_trc\": 0.3323, \"trc_gap\": 0.0016, \"tf_tbp_ppl\": 1.05, \"gen_tbp_ppl\": 1.05}, \"lora_only\": {\"tf_trc\": 0.349, \"gen_trc\": 0.4106, \"trc_gap\": -0.0617, \"tf_tbp_ppl\": 9.5, \"gen_tbp_ppl\": 12}, \"base\": {\"tf_trc\": 0.1494, \"gen_trc\": 0.1494, \"trc_gap\": 0, \"tf_tbp_ppl\": 2.05, \"gen_tbp_ppl\": 2.05}}}, \"attention_steering_v7_tg_gen\": {\"status\": \"DONE\", \"hypothesis\": \"推理时向 attention logits 注入 goal-position bias β 可恢复 autoregressive GAR。如果 GAR 从 0.015 显著提升 → 闭合因果环：exposure bias → attention 偏移 → GAR 坍塌 → 手动修正注意力 → GAR 恢复。扫描 β ∈ {0, 0.5, 1.0, 2.0, 5.0, 10.0}，成功标准：GAR > 0.1 且 PPL 不严重恶化。\", \"conclusion\": \"success\", \"metrics\": {\"beta_0.0\": {\"mid_turns_avg_gar\": 0.028, \"avg_ppl\": 1.409}, \"beta_0.5\": {\"mid_turns_avg_gar\": 0.0287, \"avg_ppl\": 1.387}, \"beta_1.0\": {\"mid_turns_avg_gar\": 0.0349, \"avg_ppl\": 1.36}, \"beta_2.0\": {\"mid_turns_avg_gar\": 0.062, \"avg_ppl\": 1.411}, \"beta_5.0\": {\"mid_turns_avg_gar\": 0.6795, \"avg_ppl\": 1.908}, \"beta_10.0\": {\"mid_turns_avg_gar\": 0.959, \"avg_ppl\": 4.22}, \"phase_transition_range\": \"[2, 5]\", \"baseline_gar\": 0.028, \"max_gar_at_acceptable_ppl\": 0.6795, \"max_gar_at_acceptable_ppl_beta\": 5}}, \"phase2_tg_s42_v8b_ss_fixed\": {\"status\": \"DONE\", \"hypothesis\": \"Fixed scheduled sampling (D026 三项 bug 修复后): 线性从 0→0.5 混合 teacher-forced + model-generated contexts 计算 GAR loss。如果 model-gen context 上的 GAR 训练能缩小 30x training-inference gap → exposure bias mitigation 有效，paper 从纯 negative 升级为 diagnosis + initial remedy。超参与 v7 一致 (lambda_gar=1.0, MSE+gate_div)，唯一变量是 SS path。成功标准：inference GAR 显著高于 v7 的 0.016 (至少 +1pp)，PPL 不恶化。\", \"conclusion\": \"failed\"}, \"phase2_tg_s42_v7\": {\"status\": \"DONE\", \"hypothesis\": \"MSE 双向 loss (mean_GAR - target)² + gate diversity 正则 F.relu(min_std - gate_std) 从结构上解决恒等退化：MSE 在 GAR > target 时反向惩罚（不再单调推高），gate_div 直接强制层间分化。预期：gate_std 稳定 >0.05 + GAR 收敛到 target=0.5 附近 + NTP 正常收敛。\", \"metrics\": {\"eval_iid_ours_mid_gar\": 0.5035, \"eval_iid_dongre_mid_gar\": 0.0152, \"eval_iid_ppl\": 2.784, \"eval_heldout_ours_mid_gar\": 0.5035, \"eval_heldout_dongre_mid_gar\": 0.0152, \"eval_heldout_ppl\": 2.78, \"eval_modelgen_ours_mid_gar\": 0.0157, \"eval_modelgen_dongre_mid_gar\": 0.0194, \"eval_modelgen_ppl\": 1.36, \"gate_mean_final\": 0.9336, \"gate_std_final\": 0.0492}, \"conclusion\": \"success\"}, \"phase2_tg_s42_v9_pcgrad\": {\"status\": \"DONE\", \"hypothesis\": \"PCGrad (Yu et al. NeurIPS 2020) 消除 NTP-GAR 梯度方向冲突后（仅对 gate 参数投影 NTP 梯度到 GAR 梯度正交平面），如果 30x training-inference GAR gap 仍在 → 因果证据证明 exposure bias（非梯度竞争）是 gap 根因。与 v7 对比：相同超参（lambda_gar=1.0, MSE+gate_div），唯一变量是梯度处理方式。成功标准：(1) 梯度 cos_sim 显著改善（从 v7 的 -0.089 提升到 ≥0），(2) 但推理 GAR 仍 ≈ v7 水平（0.016），证明梯度冲突不是 gap 的因。\", \"conclusion\": \"success\", \"metrics\": {\"eval_iid_ours_mid_gar\": 0.5002, \"eval_iid_dongre_mid_gar\": 0.0123, \"eval_iid_ppl\": 2.78, \"eval_iid_ntp\": 0.9752, \"eval_heldout_ours_mid_gar\": 0.5002, \"eval_heldout_dongre_mid_gar\": 0.0123, \"eval_heldout_ppl\": 2.78, \"eval_heldout_ntp\": 0.9752, \"eval_modelgen_ours_mid_gar\": 0.0151, \"eval_modelgen_dongre_mid_gar\": 0.0173, \"eval_modelgen_ppl\": 1.5, \"vs_v7_iid_ppl_diff\": 0.004, \"vs_v7_iid_gar_diff\": -0.0033}}, \"phase2_lora_only_s42\": {\"status\": \"DONE\", \"hypothesis\": \"LoRA-only baseline (gate 固定 1.0，无 gating 机制) 在相同 MSE+NTP loss 下 GAR 应低于 ThreadGate (v7)。如果 LoRA-only 也能训到 GAR~0.5，则 gating 机制贡献为零，paper story 不成立。关键对比：LoRA-only 的 GAR 收敛值 vs v7 的 0.48。\", \"conclusion\": \"success\", \"metrics\": {\"epochs_completed\": 3, \"global_steps\": 3000, \"training_time_seconds\": 20588.6, \"training_time_hours\": 5.7, \"gate_fixed\": 1, \"gate_type_actual\": \"none\", \"final_lora_size_mb\": 20, \"eval_modelgen_ours_mid_gar\": 0.0245, \"eval_modelgen_dongre_mid_gar\": 0.0185, \"eval_modelgen_ppl\": 1.371}}, \"phase2_ug_s42\": {\"status\": \"DONE\", \"hypothesis\": \"Uniform gating baseline: per-layer independent gates without turn conditioning (content-dependent only), to isolate whether ThreadGate's turn-conditioned gating provides benefit over content-only residual scaling. Same training setup as v7 but with gate-type=uniform.\", \"conclusion\": \"success\", \"metrics\": {\"epoch0_avg_loss\": 1.0019, \"epoch0_avg_ntp\": 0.9755, \"epoch0_avg_gar\": 0.0259, \"epoch0_avg_div\": 0.0005, \"epoch1_avg_loss\": 0.9447, \"epoch1_avg_ntp\": 0.9435, \"epoch1_avg_gar\": 0.0013, \"epoch1_avg_div\": 0, \"epoch2_avg_loss\": 0.9319, \"epoch2_avg_ntp\": 0.9309, \"epoch2_avg_gar\": 0.001, \"epoch2_avg_div\": 0, \"final_gate_mean\": 0.9598, \"final_gate_std\": 0.0518, \"final_gate_min\": 0.7773, \"final_gate_max\": 1, \"final_profile_L3\": 0.777, \"final_profile_L5\": 0.812, \"final_profile_L0\": 0.875, \"final_profile_L27\": 1, \"training_time_seconds\": 21994.5, \"training_time_hours\": 6.1, \"global_steps\": 7950, \"unexpected_per_layer_variation\": true, \"eval_modelgen_ours_mid_gar\": 0.0149, \"eval_modelgen_dongre_mid_gar\": 0.0185, \"eval_modelgen_ppl\": 1.396}}, \"phase2_tg_s42_v8_schedsampling\": {\"status\": \"DONE\", \"hypothesis\": \"Scheduled sampling 应用到 GAR loss（线性从 0→0.5 混合 teacher-forced + model-generated contexts）能缩小 v7 的 30x training-inference GAR gap。机制：在 model-generated context 上计算 GAR loss 迫使 attention pattern 适应推理时分布，直接 address teacher-forcing distribution shift。成功标准：inference GAR 显著高于 v7 的 0.016，PPL 不显著恶化（≤2.78+0.2）。\", \"conclusion\": \"failed\", \"metrics\": {\"killed_at_microstep\": 1950, \"total_microsteps\": 24000, \"completion_pct\": 8.1, \"global_step_approx\": 244, \"total_global_steps\": 3000, \"ss_steps_observed\": 1, \"tf_lgar_mean_step850_1400\": 0.0062, \"tf_lgar_std\": 0.0082, \"tf_lgar_collapse_step\": 800, \"gate_mean_final\": 0.93, \"ss_ratio_at_kill\": 0.081, \"crash_reason\": \"killed by director: SS path code bug (D026) makes experiment invalid, GPU needed for PCGrad\", \"design_flaw_ss_ramp_too_slow\": true, \"design_flaw_no_ss_tf_separate_logging\": true}}, \"analysis_attention_heatmap\": {\"status\": \"DONE\", \"hypothesis\": \"四模型（Base/TG/UG/LoRA-only）的 goal attention 衰减模式是否一致？如果 TG 的 attention decay 与 LoRA-only 无差异，则 gating 机制对 attention 分布零增量。\", \"conclusion\": \"success\", \"metrics\": {\"base_mean_goal_attn\": 0.0136, \"base_decay\": 0.875, \"tg_mean_goal_attn\": 0.0232, \"tg_decay\": 0.777, \"ug_mean_goal_attn\": 0.0216, \"ug_decay\": 0.803, \"lora_mean_goal_attn\": 0.0216, \"lora_decay\": 0.81, \"gating_incremental_benefit\": \"none\"}}, \"analysis_gradient_conflict\": {\"status\": \"DONE\", \"hypothesis\": \"NTP-GAR 梯度冲突在 v7 训练过程中是否逐层普遍存在？量化 cos_sim 和 magnitude ratio 的演化，验证 NTP 是否在训练中逐渐完全压制 GAR 信号。\", \"conclusion\": \"success\", \"metrics\": {\"epoch0_cos_sim\": -0.089, \"epoch1_cos_sim\": -0.054, \"epoch2_cos_sim\": -0.042, \"epoch0_neg_layers_pct\": 78.6, \"epoch1_neg_layers_pct\": 71.4, \"epoch2_neg_layers_pct\": 67.9, \"epoch0_mag_ratio\": 7.5, \"epoch1_mag_ratio\": 13.7, \"epoch2_mag_ratio\": 14.7}}, \"phase2_4way_eval_heldout\": {\"status\": \"DONE\", \"hypothesis\": \"四路消融的三路趋同结论（TG≈UG≈LoRA-only，gating 零增量）在 held-out eval 数据（idx≥8000，与训练集无重叠）上复现，排除数据重叠 confound。预期：相对比较保持（三路趋同），绝对 GAR 值可能变化。\", \"metrics\": {\"base_ours_mid_gar\": 0.0128, \"base_ours_recovery_pp\": 0.06, \"base_dongre_mid_gar\": 0.0031, \"base_dongre_recovery_pp\": -0.91, \"base_ppl\": 4.34, \"base_ntp\": 1.4045, \"tg_ours_mid_gar\": 0.5035, \"tg_ours_recovery_pp\": 49.13, \"tg_dongre_mid_gar\": 0.0152, \"tg_dongre_recovery_pp\": 0.3, \"tg_ppl\": 2.78, \"tg_ntp\": 0.9771, \"ug_ours_mid_gar\": 0.5053, \"ug_ours_recovery_pp\": 49.31, \"ug_dongre_mid_gar\": 0.0124, \"ug_dongre_recovery_pp\": 0.02, \"ug_ppl\": 2.78, \"ug_ntp\": 0.9752, \"lora_ours_mid_gar\": 0.4978, \"lora_ours_recovery_pp\": 48.56, \"lora_dongre_mid_gar\": 0.0132, \"lora_dongre_recovery_pp\": 0.1, \"lora_ppl\": 2.78, \"lora_ntp\": 0.9771, \"three_way_convergence_confirmed\": true, \"gar_ours_spread_pp\": 0.75, \"ppl_spread\": 0, \"data_overlap\": false}, \"conclusion\": \"success\"}, \"phase2_4way_eval\": {\"status\": \"DONE\", \"hypothesis\": \"Turn-residual gating (TRG) improves multi-turn response quality over LoRA-only and base model baselines because it selectively amplifies conversational context signals, which should manifest as higher GAR scores across 4 conditions (base, base+TRG, LoRA, LoRA+TRG).\", \"conclusion\": \"negative\", \"metrics\": {\"base_ours_mid_gar\": 0.0107, \"base_ours_recovery_pp\": -0.15, \"base_dongre_mid_gar\": 0.003, \"base_dongre_recovery_pp\": -0.92, \"base_ppl\": 4.23, \"base_ntp\": 1.4162, \"tg_ours_mid_gar\": 0.4866, \"tg_ours_recovery_pp\": 47.44, \"tg_dongre_mid_gar\": 0.0157, \"tg_dongre_recovery_pp\": 0.35, \"tg_ppl\": 2.63, \"tg_ntp\": 0.9484, \"ug_ours_mid_gar\": 0.4923, \"ug_ours_recovery_pp\": 48.01, \"ug_dongre_mid_gar\": 0.013, \"ug_dongre_recovery_pp\": 0.08, \"ug_ppl\": 2.62, \"ug_ntp\": 0.9433, \"lora_ours_mid_gar\": 0.486, \"lora_ours_recovery_pp\": 47.39, \"lora_dongre_mid_gar\": 0.0137, \"lora_dongre_recovery_pp\": 0.15, \"lora_ppl\": 2.63, \"lora_ntp\": 0.9482, \"route_b_confirmed\": true, \"gating_incremental_benefit\": \"none\"}}, \"phase2_tg_s42_v5\": {\"status\": \"DONE\", \"hypothesis\": \"重新平衡超参（λ=1.0 降 GAR 贡献至 ~50%，init_bias=1.5 使 sigmoid≈0.82 接近正常模型行为，gate_lr_multiplier=10 保持）能在 3-epoch 全量训练中产生有意义的 gate 分化（gate_std>0.05），同时 GAR 稳态在 0.1-0.5（非病态饱和），NTP loss 正常收敛，总 loss 保持正值\", \"metrics\": {\"step2000_gate_std\": 0.0225, \"step2000_gate_mean\": 0.9586, \"step2000_gate_min\": 0.9062, \"step2000_gate_max\": 0.9961, \"step2000_L_GAR\": -0.8977, \"step2000_L_NTP\": 0.7611, \"step2000_total_loss\": -0.1365, \"step2400_gate_std\": 0.0219, \"step2400_gate_mean\": 0.9651, \"step2400_gate_min\": 0.918, \"step2400_gate_max\": 0.9961, \"step2400_profile\": \"L0=0.918 L12=0.918 L13=0.926 L1=0.996 L26=0.996\", \"L_GAR_saturated_at\": -0.91, \"gate_range_compression\": \"0.918-0.996\"}, \"conclusion\": \"negative\"}, \"phase2_tg_s42_v4\": {\"status\": \"DONE\", \"hypothesis\": \"重新平衡超参（λ=1.0 降 GAR 贡献至 ~50%，init_bias=1.5 使 sigmoid≈0.82 接近正常模型行为，gate_lr_multiplier=10 保持）能在 3-epoch 全量训练中产生有意义的 gate 分化（gate_std>0.05），同时 GAR 稳态在 0.1-0.5（非病态饱和），NTP loss 正常收敛，总 loss 保持正值\", \"conclusion\": \"failed\"}, \"phase2_tg_s42_v3b\": {\"status\": \"DONE\", \"hypothesis\": \"λ=10 + gate_lr=10x + init_bias=0.0 (sigmoid=0.5) 能否驱动 gate 产生 layer 间分化 (gate_std>0.05)？如果 500 步后 gate_std<0.02 且无选择性 → GAR-driven gating 梯度路径确认失败，需要 pivot\", \"conclusion\": \"success\", \"metrics\": {\"gate_std_final\": 0.087, \"gate_mean_final\": 0.9388, \"gate_min_final\": 0.5352, \"gate_max_final\": 0.9922, \"L4_gate\": 0.535, \"L0_gate\": 0.777, \"L_NTP_final\": 0.7787, \"L_GAR_final\": -0.9606, \"elapsed_seconds\": 3565.9, \"optimizer_steps\": 500, \"gate_grad_received\": true}}, \"phase2_tg_s42_v3\": {\"status\": \"DONE\", \"hypothesis\": \"ThreadGate + maximize GAR loss (L_GAR=-mean(GAR)) 提供持续非零梯度，避免 hinge loss 的退化平衡点，gate 值应随训练下降（学习到选择性干预），同时 NTP loss 正常收敛\", \"conclusion\": \"negative\", \"metrics\": {\"gate_mean_step0\": 0.8743, \"gate_mean_step500\": 0.8761, \"gate_delta\": 0.004, \"gate_std\": 0.001, \"final_ntp_loss\": 0.94, \"final_gar_loss\": -0.019, \"gar_contribution_pct\": \"2-4%\", \"diagnosis\": \"gate frozen, GAR indirect gradient too weak\"}}, \"phase2_tg_s42_v2\": {\"status\": \"DONE\", \"hypothesis\": \"ThreadGate + 修复后的 cumulative GAR loss (ε=0.001) 在 L_NTP+L_GAR 联合训练后，mid-turn GAR recovery 应显著优于 v1 (NTP-only baseline)，验证 GAR loss 的有效性\", \"conclusion\": \"killed\"}, \"phase1_gar_diag\": {\"status\": \"DONE\", \"hypothesis\": \"Qwen2.5-7B-Instruct 在 10-turn 多轮对话中，中间 turns (3-8) 的 GAR (Goal Accessibility Ratio) 相对 turn-1 下降 ≥15%，表明模型对 system prompt 中目标 token 的注意力随对话进行显著衰减\", \"conclusion\": \"success\", \"metrics\": {\"turn1_avg_gar\": 0.0418, \"mid_turns_avg_gar\": 0.0122, \"relative_drop\": 0.708, \"num_conversations\": 5, \"num_turns\": 10, \"per_turn_avg_gar\": [0.0418, 0.0241, 0.0224, 0.013, 0.0133, 0.0086, 0.0078, 0.008, 0.0157, 0.0064]}}}, \"count\": 53, \"total\": 53, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.1764}}"
    }
  },
  "sourceToolAssistantUUID": "258a34c5-fde4-475f-b756-8ca103ab93ef",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921",
  "sessionId": "5d779602-0719-4d06-8bf9-fdd84990d5d0",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---


### Runtime record

_source line 163_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[服务器重启后首条消息] 当前日期: 2026-05-25。服务器刚重启，项目状态可能已更新。在处理审查请求前，**先读取 registry.yaml 和 report.md** 获取最新实验状态，不要依赖对话历史中的状态信息。  **审查请求：** [系统通知 — worker_done:worker_fix_audit_appendix_issues_20260525T203522]: Wor…",
  "leafUuid": "0e066bda-3f45-4584-9db9-1703d689ce83",
  "sessionId": "5d779602-0719-4d06-8bf9-fdd84990d5d0"
}
```

---


### Runtime record

_source line 164_

```json
{
  "type": "ai-title",
  "aiTitle": "Review worker audit appendix tables completion",
  "sessionId": "5d779602-0719-4d06-8bf9-fdd84990d5d0"
}
```

---


### Assistant

_source line 165 · 2026-05-25T20:45:23.664Z_

<details><summary>Logged reasoning block</summary>

```text
Wait, now the registry shows total=53, which is the same as before. Earlier it showed total=60. Let me re-check - the filter was status=DONE and it returned 53 experiments total. Without the filter, the earlier call returned total=60 but I only got 5 results. So there are 60 total experiments (53 DONE + others in various states like QUEUED/PREPARING/killed).

Anyway, I've confirmed: there is NO experiment in the registry that provides TG s123 AR GAR at N=50. The only TG s123 AR eval is eval_v7_tg_s123 with modelgen_ar.gar_ours_mid = 0.0165 (N=5, T=10).


The appendix text cites 0.064 for seed 42 (which matches d048_final_ar_eval at N=50) but 0.055 for seed 123 has no corresponding registry entry. Looking at the worker's fix, the cross-model table mixing issue remains unresolved—the table itself wasn't corrected, only the body text was expanded with per-seed details.

The per-seed TG table is also still broken at N=5, and now there's a worse problem: the new body text introduces 0.055 as fact without any experimental source, directly contradicting the table values of 0.016-0.017. While the contextual writing around seed variance is solid, this unsourced number is a critical violation—it's exactly the kind of unsupported data point the L1 rules are meant to catch. I need to flag this as a major issue in my review.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0e066bda-3f45-4584-9db9-1703d689ce83",
  "isSidechain": false,
  "requestId": "req_011CbPwUkEt6sZbw7GhuW82z",
  "type": "assistant",
  "uuid": "53f008e0-ddb7-4d99-9fe8-48b6414ba724",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921",
  "sessionId": "5d779602-0719-4d06-8bf9-fdd84990d5d0",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Fs32JFN4NfTcqtvu9TpACZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 19164,
      "cache_read_input_tokens": 128527,
      "output_tokens": 1632,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 19164,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1632,
          "cache_read_input_tokens": 128527,
          "cache_creation_input_tokens": 19164,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 19164
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

_source line 166 · 2026-05-25T20:45:24.920Z_

确认完毕。registry 中不存在 TG s123 N=50 AR eval，0.055 无实验支撑。我的两个原始 warning 均未修复，且引入了一个新的 critical 级问题。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "53f008e0-ddb7-4d99-9fe8-48b6414ba724",
  "isSidechain": false,
  "requestId": "req_011CbPwUkEt6sZbw7GhuW82z",
  "type": "assistant",
  "uuid": "f528f46d-3985-4f8c-994f-1343c75ea9c7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921",
  "sessionId": "5d779602-0719-4d06-8bf9-fdd84990d5d0",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Fs32JFN4NfTcqtvu9TpACZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 19164,
      "cache_read_input_tokens": 128527,
      "output_tokens": 1632,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 19164,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1632,
          "cache_read_input_tokens": 128527,
          "cache_creation_input_tokens": 19164,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 19164
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

_source line 167 · 2026-05-25T20:45:49.104Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__reviewer_post_to_director · `toolu_012tAqugDyYc24dFLpJkPvWr`</summary>

```json
{
  "text": "## 审查报告 — worker_fix_audit_appendix_issues\n\n**结论**: CRITICAL\n\nworker 声称修复了我此前标记的附录表格问题（status=done），但实际上：\n\n### 发现\n\n- [severity: critical] **正文引入无 registry 支撑的数据点（TG s123 AR GAR = 0.055）**\n  - appendix.tex §Per-Seed Detailed Results（第635行）写道：\"Two seeds produce…similar AR GAR (0.064 vs. 0.055), with gap ratios of 7.9× and 9.1× respectively\"\n  - 0.064 (s42) 来自 d048_final_ar_eval（N=50 gen-mode）✓\n  - **0.055 (s123) 在整个 registry 中不存在**。唯一的 TG s123 AR eval 是 eval_v7_tg_s123，其 modelgen_ar.gar_ours_mid = 0.0165（N=5, T=10 协议），不是 0.055\n  - 0.055 看起来像是反算出来的：0.505 / 9.1 ≈ 0.0555，即 worker 可能先设定了 gap ratio 9.1×，再除法得到 AR GAR，而非从实际实验测量\n  - 这违反论文溯源原则——paper 中的每个定量 claim 必须有 registry 实验数据支撑\n  - **修复方案**：(a) 跑 TG s123 的 N=50 AR eval 获得真实数据，或 (b) 删除 0.055 和 9.1× 这两个数字，只报告有实验支撑的 s42 数据\n\n- [severity: warning] **原始问题 1 未修复：tab_crossmodel_detail Qwen SS 行仍混合单种子 TF (0.498) 与 3-seed mean AR (0.401)**\n  - 表格文件完全未改动\n  - caption 仍声称 \"Qwen AR: d048_final_ar N=50 gen beta=0\"，但 d048_final_ar 给出 ss_gar = 0.347（s42），不是 0.401（3-seed mean）\n  - Gap 1.2× 仍基于混合计算\n\n- [severity: warning] **原始问题 2 未修复：tab_perseed_tg 仍用 N=5/T=10 旧协议**\n  - 表格文件完全未改动，AR GAR = 0.016/0.017，gap = 31.4×\n  - 正文（第635行）却说 AR GAR = 0.064/0.055，gap = 7.9×/9.1×\n  - 同一个章节里，正文与其引用的表格给出截然不同的数字（0.064 vs 0.016，gap 7.9× vs 31×），审稿人必然质疑\n\n### 建议\n1. 立即删除或标注 0.055 为\"待补实验验证\"，不可将无源数据留在论文中\n2. tab_perseed_tg 的 AR 列要么更新为 N=50 数据（需跑 eval），要么正文引用时与表格数字保持一致（使用 N=5 数据并注明）\n3. tab_crossmodel_detail 的 SS 行统一数据源：全用 s42 或全用 3-seed mean",
  "project": "turn_residual_gating"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f528f46d-3985-4f8c-994f-1343c75ea9c7",
  "isSidechain": false,
  "requestId": "req_011CbPwUkEt6sZbw7GhuW82z",
  "type": "assistant",
  "uuid": "b1f89e68-80fc-4cdc-afbd-67f153f1e65d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921",
  "sessionId": "5d779602-0719-4d06-8bf9-fdd84990d5d0",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Fs32JFN4NfTcqtvu9TpACZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 19164,
      "cache_read_input_tokens": 128527,
      "output_tokens": 1632,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 19164,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1632,
          "cache_read_input_tokens": 128527,
          "cache_creation_input_tokens": 19164,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 19164
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

_source line 168 · 2026-05-25T20:45:52.893Z_

<details><summary>↩ Tool result · `toolu_012tAqugDyYc24dFLpJkPvWr`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"director_session\": \"feishu:group:oc_640e53b6afbbd5e34eb7273cd5a707a0:director\"}, \"error\": \"\"}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b1f89e68-80fc-4cdc-afbd-67f153f1e65d",
  "isSidechain": false,
  "promptId": "8d8464e4-1523-464c-8d63-5cd7db13bd3f",
  "type": "user",
  "uuid": "c18799c2-8dad-4b24-bb24-b55362156c42",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"director_session\\\": \\\"feishu:group:oc_640e53b6afbbd5e34eb7273cd5a707a0:director\\\"}, \\\"error\\\": \\\"\\\"}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"director_session\": \"feishu:group:oc_640e53b6afbbd5e34eb7273cd5a707a0:director\"}, \"error\": \"\"}"
    }
  },
  "sourceToolAssistantUUID": "b1f89e68-80fc-4cdc-afbd-67f153f1e65d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921",
  "sessionId": "5d779602-0719-4d06-8bf9-fdd84990d5d0",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---


### Runtime record

_source line 169_

```json
{
  "type": "ai-title",
  "aiTitle": "Review worker audit appendix tables completion",
  "sessionId": "5d779602-0719-4d06-8bf9-fdd84990d5d0"
}
```

---


### Runtime record

_source line 170 · 2026-05-25T20:53:43.309Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-25T20:53:43.309Z",
  "sessionId": "5d779602-0719-4d06-8bf9-fdd84990d5d0",
  "content": "[系统通知 — worker_done:worker_fix_reviewer_w1_w2_issues_20260525T204337]:\nWorker worker_fix_reviewer_w1_w2_issues_20260525T204337 已完成（status=done），请审查 Agent 的处理结果。"
}
```

---


### Runtime record

_source line 171 · 2026-05-25T20:53:43.310Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-25T20:53:43.310Z",
  "sessionId": "5d779602-0719-4d06-8bf9-fdd84990d5d0"
}
```

---


## Round 4

## Round 4

2 recorded events


### User

_source line 172 · 2026-05-25T20:53:43.301Z_

Continue from where you left off.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c18799c2-8dad-4b24-bb24-b55362156c42",
  "isSidechain": false,
  "promptId": "5794a2d4-fabe-4aa4-b195-ac928e4f6662",
  "type": "user",
  "isMeta": true,
  "uuid": "66618250-a16c-477f-baf0-ead70a7cd96c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921",
  "sessionId": "5d779602-0719-4d06-8bf9-fdd84990d5d0",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---


### Assistant

_source line 173 · 2026-05-25T20:53:43.301Z_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "66618250-a16c-477f-baf0-ead70a7cd96c",
  "isSidechain": false,
  "type": "assistant",
  "uuid": "935c71e7-eda4-4603-8cd4-645645f1cc00",
  "isApiErrorMessage": false,
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921",
  "sessionId": "5d779602-0719-4d06-8bf9-fdd84990d5d0",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "id": "f3d2b6df-7a0d-435a-94ea-74e535534c5f",
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


## Round 5

## Round 5

23 recorded events


### User

_source line 174 · 2026-05-25T20:53:43.433Z_

[系统通知 — worker_done:worker_fix_reviewer_w1_w2_issues_20260525T204337]:
Worker worker_fix_reviewer_w1_w2_issues_20260525T204337 已完成（status=done），请审查 Agent 的处理结果。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "935c71e7-eda4-4603-8cd4-645645f1cc00",
  "isSidechain": false,
  "promptId": "5794a2d4-fabe-4aa4-b195-ac928e4f6662",
  "type": "user",
  "uuid": "be7a09ec-cf07-4954-a56c-7b8f14bfb5ed",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/reviewer_e7517921",
  "sessionId": "5d779602-0719-4d06-8bf9-fdd84990d5d0",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---
