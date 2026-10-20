# Research conversation: [System 触发审查]: 收到你的 critical 审查报告，6 个数据一致性问题全部确认。已派 Agent 紧急调查修复。 请你重点关注 P0-1 SciERC AUROC 问题：如果 EM AUROC 确实是 0.749 而非 0

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 59
- **Recorded user turns:** 1
- **Tool calls:** 13
- **Original source:** `logs/chats/exported-trajectories/account-3/a6ae7e35-390a-442a-93d4-9958c82c9e3b.jsonl`
- **Structured JSON:** [`2008d4d04c40813a2e7c.json`](../../sessions/20/2008d4d04c40813a2e7c.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-19T13:51:09.412Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-19T13:51:09.412Z",
  "sessionId": "a6ae7e35-390a-442a-93d4-9958c82c9e3b",
  "content": "[System 触发审查]:\n收到你的 critical 审查报告，6 个数据一致性问题全部确认。已派 Agent 紧急调查修复。\n\n请你重点关注 P0-1 SciERC AUROC 问题：如果 EM AUROC 确实是 0.749 而非 0.614，论文中以下叙述可能需要修改：\n1. Table 1 信号排序结论（EM 可能超过 VC 成为 SciERC 最高 AUROC）\n2. 正文中关于\"structural signals > LP\"的叙述是否需要修正\n3. Abstract/Conclusion 中关于信号质量的 claim\n\nAgent 修复后请你独立验证修复结果是否正确、是否有遗漏。特别关注 P1-6 CoNLL degen N=16 混用问题——如果证实，这是系统性的数据管理问题，需要全面排查是否还有其他 N=8/N=16 混用。"
}
```

---

### Runtime record

_source line 2 · 2026-05-19T13:51:09.417Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-19T13:51:09.417Z",
  "sessionId": "a6ae7e35-390a-442a-93d4-9958c82c9e3b"
}
```

---

## Round 1

57 recorded events

### User

_source line 3 · 2026-05-19T13:51:09.462Z_

[System 触发审查]:
收到你的 critical 审查报告，6 个数据一致性问题全部确认。已派 Agent 紧急调查修复。

请你重点关注 P0-1 SciERC AUROC 问题：如果 EM AUROC 确实是 0.749 而非 0.614，论文中以下叙述可能需要修改：
1. Table 1 信号排序结论（EM 可能超过 VC 成为 SciERC 最高 AUROC）
2. 正文中关于"structural signals > LP"的叙述是否需要修正
3. Abstract/Conclusion 中关于信号质量的 claim

Agent 修复后请你独立验证修复结果是否正确、是否有遗漏。特别关注 P1-6 CoNLL degen N=16 混用问题——如果证实，这是系统性的数据管理问题，需要全面排查是否还有其他 N=8/N=16 混用。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "2279f609-b135-4e34-8568-a1f529688be0",
  "type": "user",
  "uuid": "b05c5b0c-7ccd-4c5d-9bb6-15d9533bd9ac",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "a6ae7e35-390a-442a-93d4-9958c82c9e3b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-19T13:51:09.461Z_

```json
{
  "parentUuid": "b05c5b0c-7ccd-4c5d-9bb6-15d9533bd9ac",
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
  "uuid": "0a610962-d394-4731-9359-88b665a3df82",
  "timestamp": "2026-05-19T13:51:09.461Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "a6ae7e35-390a-442a-93d4-9958c82c9e3b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-19T13:51:09.461Z_

```json
{
  "parentUuid": "0a610962-d394-4731-9359-88b665a3df82",
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
  "uuid": "c338c58e-2c5d-4fcd-a49a-91295ff8da2b",
  "timestamp": "2026-05-19T13:51:09.461Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "a6ae7e35-390a-442a-93d4-9958c82c9e3b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6 · 2026-05-19T13:51:09.461Z_

```json
{
  "parentUuid": "c338c58e-2c5d-4fcd-a49a-91295ff8da2b",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "fac4ecd0-d22d-4fb9-9ab8-cfb74f40cb70",
  "timestamp": "2026-05-19T13:51:09.461Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "a6ae7e35-390a-442a-93d4-9958c82c9e3b",
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
  "aiTitle": "Verify SciERC AUROC data consistency issues",
  "sessionId": "a6ae7e35-390a-442a-93d4-9958c82c9e3b"
}
```

---

### Assistant

_source line 8 · 2026-05-19T13:51:16.159Z_

<details><summary>Logged reasoning block</summary>

```text
Director 要求我：
1. 重点关注 P0-1 SciERC AUROC 问题，分析如果 EM AUROC 是 0.749 而非 0.614 对论文叙述的影响
2. 等 Agent 修复后独立验证修复结果
3. 特别关注 P1-6 CoNLL degen N=16 混用问题

我需要先读取当前的 registry、report、论文相关文件来了解具体情况。

现在让我获取必要的工具 schema，然后开始读取这些文件。
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fac4ecd0-d22d-4fb9-9ab8-cfb74f40cb70",
  "isSidechain": false,
  "requestId": "req_011CbC34cNM8ta9ogDuuJVP1",
  "type": "assistant",
  "uuid": "c291c42b-6ece-43ad-bfaf-451a068440c1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "a6ae7e35-390a-442a-93d4-9958c82c9e3b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013Sfjy6NzsMKiQA6S91gBUF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 20876,
      "cache_read_input_tokens": 11841,
      "output_tokens": 358,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 20876,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 358,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 20876,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 20876
          },
          "type": "message"
        }
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

_source line 9 · 2026-05-19T13:51:16.160Z_

先读取 registry 和 report 了解当前数据状态。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c291c42b-6ece-43ad-bfaf-451a068440c1",
  "isSidechain": false,
  "requestId": "req_011CbC34cNM8ta9ogDuuJVP1",
  "type": "assistant",
  "uuid": "3c38678b-6797-481e-8852-813b30e50963",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "a6ae7e35-390a-442a-93d4-9958c82c9e3b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013Sfjy6NzsMKiQA6S91gBUF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 20876,
      "cache_read_input_tokens": 11841,
      "output_tokens": 358,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 20876,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 358,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 20876,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 20876
          },
          "type": "message"
        }
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

_source line 10 · 2026-05-19T13:51:17.676Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_013u5u4E7oKmP1PhTZzomXHK`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__read_roadmap,mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__reviewer_post_to_director,mcp__agent-ml-research__compute_coverage_matrix",
  "max_results": 6
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3c38678b-6797-481e-8852-813b30e50963",
  "isSidechain": false,
  "requestId": "req_011CbC34cNM8ta9ogDuuJVP1",
  "type": "assistant",
  "uuid": "4850316c-ba5c-4916-b1a8-5740f7580cbc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "a6ae7e35-390a-442a-93d4-9958c82c9e3b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013Sfjy6NzsMKiQA6S91gBUF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 20876,
      "cache_read_input_tokens": 11841,
      "output_tokens": 358,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 20876,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 358,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 20876,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 20876
          },
          "type": "message"
        }
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

_source line 11 · 2026-05-19T13:51:17.682Z_

<details><summary>↩ Tool result · `toolu_013u5u4E7oKmP1PhTZzomXHK`</summary>

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

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__compute_coverage_matrix"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4850316c-ba5c-4916-b1a8-5740f7580cbc",
  "isSidechain": false,
  "promptId": "2279f609-b135-4e34-8568-a1f529688be0",
  "type": "user",
  "uuid": "2e2d0474-25c1-4b17-b4d1-31559f2563c5",
  "toolUseResult": {
    "matches": [
      "mcp__agent-ml-research__read_registry",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__read_roadmap",
      "mcp__agent-ml-research__ssh_read_only",
      "mcp__agent-ml-research__reviewer_post_to_director",
      "mcp__agent-ml-research__compute_coverage_matrix"
    ],
    "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__read_roadmap,mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__reviewer_post_to_director,mcp__agent-ml-research__compute_coverage_matrix",
    "total_deferred_tools": 35
  },
  "sourceToolAssistantUUID": "4850316c-ba5c-4916-b1a8-5740f7580cbc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "a6ae7e35-390a-442a-93d4-9958c82c9e3b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-19T13:51:21.366Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01Yaotfiuju3DcxCYr8jtY5T`</summary>

```json
{
  "project": "struct_self_consist_ie",
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
  "parentUuid": "2e2d0474-25c1-4b17-b4d1-31559f2563c5",
  "isSidechain": false,
  "requestId": "req_011CbC35Di7PLWSZqHt8cqjY",
  "type": "assistant",
  "uuid": "5a4763d9-0be9-4c23-9fed-845e289fa17e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "a6ae7e35-390a-442a-93d4-9958c82c9e3b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BpmiiM6AKBV4ZgNwdyDduC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1855,
      "cache_read_input_tokens": 32717,
      "output_tokens": 196,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1855,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 196,
          "cache_read_input_tokens": 32717,
          "cache_creation_input_tokens": 1855,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1855
          },
          "type": "message"
        }
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

_source line 13 · 2026-05-19T13:51:21.827Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_013MPHfzCBgYUuHgHyYDSHS6`</summary>

```json
{
  "project": "struct_self_consist_ie",
  "file": "report.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5a4763d9-0be9-4c23-9fed-845e289fa17e",
  "isSidechain": false,
  "requestId": "req_011CbC35Di7PLWSZqHt8cqjY",
  "type": "assistant",
  "uuid": "d3421077-f97e-472d-9701-2f62c08fb1b7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "a6ae7e35-390a-442a-93d4-9958c82c9e3b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BpmiiM6AKBV4ZgNwdyDduC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1855,
      "cache_read_input_tokens": 32717,
      "output_tokens": 196,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1855,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 196,
          "cache_read_input_tokens": 32717,
          "cache_creation_input_tokens": 1855,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1855
          },
          "type": "message"
        }
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

_source line 14 · 2026-05-19T13:51:23.092Z_

<details><summary>↩ Tool result · `toolu_01Yaotfiuju3DcxCYr8jtY5T`</summary>

```text
Error: result (265,254 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-reviewer-0064dd56/a6ae7e35-390a-442a-93d4-9958c82c9e3b/tool-results/mcp-agent-ml-research-read_registry-1779198683077.txt.
Format: JSON with schema: {result: string}
- For targeted queries (find a value, filter by field): use jq on the file directly.
- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-reviewer-0064dd56/a6ae7e35-390a-442a-93d4-9958c82c9e3b/tool-results/mcp-agent-ml-research-read_registry-1779198683077.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.
- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-reviewer-0064dd56/a6ae7e35-390a-442a-93d4-9958c82c9e3b/tool-results/mcp-agent-ml-research-read_registry-1779198683077.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim." A vague "summarize this" may lose detail.

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5a4763d9-0be9-4c23-9fed-845e289fa17e",
  "isSidechain": false,
  "promptId": "2279f609-b135-4e34-8568-a1f529688be0",
  "type": "user",
  "uuid": "cfb13aa4-e735-4b0f-acc9-e4c9a8571af5",
  "toolUseResult": "Error: result (265,254 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-reviewer-0064dd56/a6ae7e35-390a-442a-93d4-9958c82c9e3b/tool-results/mcp-agent-ml-research-read_registry-1779198683077.txt.\nFormat: JSON with schema: {result: string}\n- For targeted queries (find a value, filter by field): use jq on the file directly.\n- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-reviewer-0064dd56/a6ae7e35-390a-442a-93d4-9958c82c9e3b/tool-results/mcp-agent-ml-research-read_registry-1779198683077.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.\n- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. \"/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-reviewer-0064dd56/a6ae7e35-390a-442a-93d4-9958c82c9e3b/tool-results/mcp-agent-ml-research-read_registry-1779198683077.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim.\" A vague \"summarize this\" may lose detail.\n",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {\"exp_qwen25_72b_zeroshot\": {\"status\": \"RUNNING\", \"retry_count\": 1, \"created_at\": \"2026-05-19T06:19:28.597Z\", \"updated_at\": \"2026-05-19T12:48:36.347Z\", \"hypothesis\": \"A larger zero-shot model (72B) will show higher greedy F1 and wider oracle-greedy gap than fine-tuned smaller models, because increased capacity enables more diverse valid extractions per stochastic sample, making self-consistency signals (SJ, FK, VC, EM) more informative for quality estimation.\", \"server\": \"autodl-5090-b\", \"gpu\": \"cuda:0,cuda:1,cuda:2,cuda:3\", \"account\": \"root\", \"reproduce\": {\"server\": \"autodl-5090-b\", \"gpu\": \"cuda:0,cuda:1,cuda:2,cuda:3\", \"started_at\": \"2026-05-19T06:47:42.658Z\"}, \"notes\": \"2026-05-19 12:47 UTC: RECOVERED from false-positive startup recovery failure. 289848/301184 prompts (96.2%). SciERC ✅ (551) CoNLL ✅ (3453) FewNERD ~96%. ETA ~10-15min. PID 59040, 4×5090 100% util. Cron registered.\", \"failure_reason\": \"startup recovery: RUNNING with no cron and no server/pid info\", \"completed_at\": \"2026-05-19T12:44:26.198Z\", \"extra\": {\"previous_failure\": {\"conclusion\": \"failed\", \"notes\": \"2026-05-19 11:36 UTC: 69.8% complete (210352/301184 prompts). SciERC ✅ CoNLL ✅ FewNERD ~66%. ETA ~1h15m. vLLM PID 59040, 4×5090 100% util.\"}}, \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0,1,2,3 python code/zeroshot_inference_72b.py --datasets scierc conll2003 fewnerd --output-dir output/72b_zeroshot --seed 42\", \"server\": \"autodl-5090-b\", \"data_path\": \"data/{scierc,conll2003,fewnerd}\", \"data_count\": 41630, \"model_name\": \"Qwen2.5-72B-Instruct-AWQ\", \"seed\": 42, \"gpu_ids\": [\"cuda:0\", \"cuda:1\", \"cuda:2\", \"cuda:3\"], \"pid\": 59040}}, \"exp_qwen25_14b_fewnerd\": {\"status\": \"RUNNING\", \"retry_count\": 1, \"created_at\": \"2026-05-19T06:19:31.620Z\", \"updated_at\": \"2026-05-19T12:48:33.954Z\", \"hypothesis\": \"The correlation-selection gap pattern is consistent at 14B scale, filling the gap between 8B and 32B. Qwen2.5-14B QLoRA fine-tuned on FewNERD should show intermediate degeneracy rates and similar signal ranking patterns, providing a smooth scaling curve for the diagnostic findings.\", \"server\": \"autodl-5090-c\", \"gpu\": \"cuda:0,cuda:1\", \"account\": \"root\", \"reproduce\": {\"server\": \"autodl-5090-c\", \"gpu\": \"cuda:0,cuda:1\", \"started_at\": \"2026-05-19T06:47:43.938Z\"}, \"notes\": \"2026-05-19 12:47 UTC: RECOVERED from false-positive startup recovery failure. Step 6483/41180 (15.7%), loss 0.0608, ~2.2s/it, ETA ~21h. checkpoint-6000 saved. screen train_14b_s42 PID 56766, GPU 0,1 95-96% util. Cron registered on PID 56773.\", \"failure_reason\": \"startup recovery: RUNNING with no cron and no server/pid info\", \"completed_at\": \"2026-05-19T12:44:29.453Z\", \"extra\": {\"previous_failure\": {\"conclusion\": \"failed\", \"notes\": \"2026-05-19 11:36 UTC: step 4934/41180 (12.0%), loss 0.067, ~2.15s/it, ETA ~22h. checkpoint-4000 saved. screen train_14b_s42, 2×5090 76-77% util.\"}}, \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0,1 FORCE_TORCHRUN=1 NNODES=1 NPROC_PER_NODE=2 llamafactory-cli train train_config_qwen25_14b_fewnerd_s42.yaml\", \"server\": \"autodl-5090-c\", \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/data/fewnerd/llmfactory_train.json\", \"data_count\": 131767, \"model_name\": \"Qwen2.5-14B-Instruct\", \"seed\": 42, \"gpu_ids\": [\"cuda:0\", \"cuda:1\"], \"screen_session\": \"train_14b_s42\", \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/logs/train_qwen25_14b_fewnerd_s42.log\"}}, \"exp_qwen25_32b_fewnerd\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-19T06:19:25.428Z\", \"updated_at\": \"2026-05-19T12:24:14.706Z\", \"hypothesis\": \"Scaling from Qwen3-8B to Qwen2.5-32B-Instruct with QLoRA fine-tuning on FewNERD will improve structured self-consistency IE performance due to stronger base model capabilities in instruction following and entity recognition.\", \"server\": \"autodl-5090\", \"gpu\": \"cuda:0,cuda:1,cuda:2,cuda:3\", \"account\": \"root\", \"reproduce\": {\"server\": \"autodl-5090\", \"gpu\": \"cuda:0,cuda:1,cuda:2,cuda:3\", \"started_at\": \"2026-05-19T06:47:41.246Z\"}, \"notes\": \"2026-05-19 11:36 UTC: step 2177/41180 (5.3%), loss 0.0663, ~2.44s/it, ETA ~26h. checkpoint-2000 saved. PID 804438, 4×5090 87-100% util.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0,1,2,3 FORCE_TORCHRUN=1 NNODES=1 NPROC_PER_NODE=4 llamafactory-cli train /root/autodl-tmp/struct_self_consist_ie/train_config_qwen25_32b_fewnerd_s42.yaml\", \"server\": \"autodl-5090\", \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/data/fewnerd/llmfactory_train.json\", \"data_count\": 131767, \"model_name\": \"Qwen2.5-32B-Instruct\", \"seed\": 42, \"method\": \"QLoRA-4bit-nf4 (rank=32, alpha=64, target=all)\", \"output_dir\": \"/root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen25-32b-fewnerd-qlora-s42\", \"config_path\": \"/root/autodl-tmp/struct_self_consist_ie/train_config_qwen25_32b_fewnerd_s42.yaml\", \"epochs\": 5, \"effective_batch_size\": 16, \"lr\": \"2e-4\", \"gpu_ids\": [\"cuda:0\", \"cuda:1\", \"cuda:2\", \"cuda:3\"], \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/logs/train_qwen25_32b_fewnerd_s42.log\", \"pid\": 804438}}, \"exp_qwen25_7b_fewnerd\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-19T06:41:43.121Z\", \"updated_at\": \"2026-05-19T12:23:28.347Z\", \"hypothesis\": \"Qwen2.5-7B QLoRA fine-tuned on FewNERD will produce structurally diverse samples enabling self-consistency-based entity extraction with meaningful LP-weighted consensus signals, comparable to the 14B model but with lower compute cost.\", \"spec\": {\"server\": \"autodl-5090-c\", \"gpu_ids\": [\"cuda:2\", \"cuda:3\"], \"command\": \"nohup bash run_fewnerd_qwen25_7b_pipeline.sh > logs/pipeline_qwen25_7b_fewnerd.log 2>&1 &\", \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/data/fewnerd/llmfactory_train.json\", \"data_count\": 131767, \"model_name\": \"Qwen2.5-7B-Instruct\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen25-7b-fewnerd-qlora-s42\", \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/logs/pipeline_qwen25_7b_fewnerd.log\", \"training_config\": \"train_config_qwen25_7b_fewnerd_s42.yaml\", \"export_config\": \"export_config_qwen25_7b_fewnerd.yaml\", \"pipeline_script\": \"run_fewnerd_qwen25_7b_pipeline.sh\", \"method\": \"QLoRA 4-bit nf4, rank=32, alpha=64, 5 epochs, lr=2e-4, effective_batch=32\", \"pipeline_phases\": \"train -> export/merge -> 3-seed N=8 inference (42/123/456) -> signal analysis -> entity construction\"}, \"notes\": \"2026-05-19 11:36 UTC: step 138/20590 (0.7%), ~2.34s/it, ETA ~13.3h. Pipeline PID 71837, llamafactory PID 71844. cuda:2,3 98-100% util. Cron registered on pipeline PID.\", \"server\": \"autodl-5090-c\", \"gpu\": \"cuda:2,cuda:3\"}, \"exp_wnut17_qwen25_7b\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T06:19:33.960Z\", \"updated_at\": \"2026-05-19T11:49:07.313Z\", \"hypothesis\": \"The correlation-selection gap extends to noisy social media NER (WNUT-17). Unlike formal-domain datasets (SciERC/CoNLL/FewNERD), WNUT-17 has higher surface-level noise which may affect structural signal reliability differently. This tests domain generalization of the diagnostic framework.\", \"server\": \"autodl-5090-c\", \"gpu\": \"cuda:2,cuda:3\", \"account\": \"root\", \"reproduce\": {\"server\": \"autodl-5090-c\", \"gpu\": \"cuda:2,cuda:3\", \"started_at\": \"2026-05-19T06:47:45.220Z\"}, \"spec\": {\"server\": \"autodl-5090-c\", \"gpu_ids\": [\"cuda:2\", \"cuda:3\"], \"command\": \"bash wait_and_train.sh (screen: exp_wnut17_7b)\", \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/data/wnut17/llmfactory_train.json\", \"data_count\": 3404, \"model_name\": \"Qwen2.5-7B-Instruct\", \"seed\": 42, \"training_config\": \"train_config_qwen25_7b_wnut17_s42.yaml\", \"method\": \"QLoRA 4-bit (bnb nf4), rank=32, alpha=64, all targets\", \"gpus\": \"cuda:2,3 (2x5090)\", \"epochs\": 5, \"effective_batch_size\": 32, \"pipeline\": \"train → export → 3-seed inference (N=8, T=1.0) → signal analysis → entity construction\", \"checkpoint_source\": \"self-trained on WNUT-17\", \"eval_data\": \"WNUT-17 test set\", \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen25-7b-wnut17-qlora-s42\", \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/logs/exp_wnut17_7b_pipeline.log\"}, \"conclusion\": \"negative\", \"metrics\": {\"seed42\": {\"greedy_f1\": 0.4524, \"construction_f1\": 0.4439, \"construction_delta_pp\": -0.84, \"construction_p\": 0.95}, \"seed123\": {\"greedy_f1\": 0.4518, \"construction_f1\": 0.4579, \"construction_delta_pp\": 0.61, \"construction_p\": 0.08}, \"seed456\": {\"greedy_f1\": 0.4526, \"construction_f1\": 0.4583, \"construction_delta_pp\": 0.57, \"construction_p\": 0.12}, \"oracle_headroom_pp\": \"6.3-9.2\"}, \"completed_at\": \"2026-05-19T11:22:56.623Z\"}, \"exp_llama_fewnerd_inference\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T02:18:49.938Z\", \"updated_at\": \"2026-05-19T03:15:04.486Z\", \"hypothesis\": \"LLaMA-3.1-8B fine-tuned on FewNERD shows the same structured self-consistency phenomena (degeneracy, LP-F1 alignment, signal ranking) as Qwen models, providing cross-model generalization evidence. 3-seed inference (42/123/456) for statistical robustness.\", \"parent\": \"exp_llama_fewnerd_lora\", \"spec\": {\"command\": \"bash code/run_llama_fewnerd_inference.sh\", \"server\": \"autodl-5090\", \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/data/fewnerd/\", \"data_count\": 37648, \"model_name\": \"LLaMA-3.1-8B-FewNERD-LoRA-merged\", \"seed\": \"42,123,456\", \"checkpoint_source\": \"exp_llama_fewnerd_lora\", \"eval_data\": \"FewNERD test set\", \"checkpoint_path\": \"checkpoints/llama3.1-8b-fewnerd-merged/\", \"log_path\": \"logs/llama_fewnerd_inference.log\"}, \"conclusion\": \"success\", \"metrics\": {\"3seed_mean\": {\"greedy_f1\": 0.7842, \"oracle_f1\": 0.8843, \"headroom_pp\": 10.01, \"degeneracy_pct\": 23.36, \"lp_delta_pp\": 0.36, \"dgs_delta_pp\": -0.35}, \"seed_42\": {\"greedy_f1\": 0.7841, \"oracle_f1\": 0.8854, \"degen\": 27.32}, \"seed_123\": {\"greedy_f1\": 0.784, \"oracle_f1\": 0.8839, \"degen\": 24.63}, \"seed_456\": {\"greedy_f1\": 0.7844, \"oracle_f1\": 0.8835, \"degen\": 18.13}, \"signal_ranking\": \"LP (+0.36pp) > SJ (-0.52) > FK (-0.53) > EM (-1.02) > VC (-2.39)\", \"lp_only_positive\": true, \"n_instances_gold_filtered\": 32565}, \"completed_at\": \"2026-05-19T03:15:04.486Z\"}, \"exp_entity_construction\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T02:00:12.074Z\", \"updated_at\": \"2026-05-19T02:40:17.571Z\", \"hypothesis\": \"Entity-level majority vote construction is the correct self-consistency analogy for structured IE: instead of selecting the best instance-level output, assemble a better output from entity-level consensus across N samples. Construction should outperform both greedy and best-of-N selection.\", \"conclusion\": \"success\", \"spec\": {\"command\": \"python code/entity_construction_fair.py\", \"server\": \"autodl-5090\", \"data_path\": \"output/*/samples_*.json\", \"data_count\": 3, \"model_name\": \"analysis_cpu\", \"seed\": 42, \"checkpoint_path\": \"output/entity_construction_fair/\", \"log_path\": \"output/entity_construction_fair/\"}, \"completed_at\": \"2026-05-19T02:15:19.616Z\", \"metrics\": {\"n16_fair_cv\": {\"scierc_ner\": {\"cv_uniform_delta\": \"+1.35pp\", \"p_value\": 0.018, \"significant\": true}, \"conll_ner\": {\"cv_uniform_delta\": \"+0.10pp\", \"p_value\": 0.303, \"significant\": false}, \"fewnerd_ner\": {\"cv_uniform_delta\": \"+1.32pp\", \"p_value\": 0, \"significant\": true}, \"scierc_re\": {\"cv_uniform_delta\": \"+1.69pp\", \"p_value\": 0.049, \"significant\": true}}, \"n8_fair_cv\": {\"scierc_ner\": {\"uniform_confirm\": \"+1.54pp (p=0.023, sig)\", \"lp_weighted_confirm\": \"+1.67pp (p=0.004, sig)\", \"cv_uniform\": \"+1.12pp (p=0.057, borderline)\"}, \"conll_ner\": {\"cv_uniform\": \"-0.39pp (p=0.963, not sig)\"}, \"fewnerd_ner\": {\"lp_weighted_cv\": \"+0.88pp (p=0.000, sig)\", \"uniform_cv\": \"+0.32pp (p=0.003, sig)\"}}, \"adaptive_combination\": \"INVALIDATED - gold label leakage confirmed\", \"note\": \"5-fold CV, bootstrap B=10000, paired one-sided\"}}, \"exp_lp_alignment_gating\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T02:00:16.520Z\", \"updated_at\": \"2026-05-19T02:15:48.197Z\", \"hypothesis\": \"Within-instance LP-F1 alignment score (adjusted by valid_ratio for degeneracy) can automatically gate whether LP selection should be applied to a dataset. A small probe sample (50-100 instances) suffices for a stable gating decision.\", \"conclusion\": \"success\", \"spec\": {\"command\": \"python code/lp_alignment_gated_selection.py\", \"server\": \"autodl-5090\", \"data_path\": \"output/*/samples_*.json\", \"data_count\": 3, \"model_name\": \"analysis_cpu\", \"seed\": 42, \"checkpoint_path\": \"output/prescriptive_analysis/\", \"log_path\": \"output/prescriptive_analysis/\"}, \"completed_at\": \"2026-05-19T02:15:23.716Z\", \"metrics\": {\"adjusted_score\": \"mean_rho * valid_ratio\", \"threshold\": 0.3, \"accuracy\": \"3/3 datasets correct\", \"robust_range\": \"0.2-0.4\"}}, \"exp_selective_prediction\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T02:00:13.989Z\", \"updated_at\": \"2026-05-19T02:15:46.588Z\", \"hypothesis\": \"QE signals (especially voting_confidence) can drive practical selective prediction: filtering out low-confidence instances yields significant F1 improvement on retained instances, enabling human-AI collaboration for structured IE.\", \"conclusion\": \"success\", \"spec\": {\"command\": \"python code/selective_prediction.py\", \"server\": \"autodl-5090\", \"data_path\": \"output/*/samples_*.json\", \"data_count\": 3, \"model_name\": \"analysis_cpu\", \"seed\": 42, \"checkpoint_path\": \"output/prescriptive_analysis/\", \"log_path\": \"output/prescriptive_analysis/\"}, \"completed_at\": \"2026-05-19T02:15:21.704Z\", \"metrics\": {\"vc_best_signal\": true, \"f1_at_80pct_coverage\": {\"scierc\": \"+5.0pp\", \"conll\": \"+8.4pp\", \"fewnerd\": \"+6.2pp\"}, \"precision_coverage_curves\": \"output/prescriptive_analysis/fig_selective_prediction.pdf\"}}, \"exp_llama_fewnerd_lora\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T13:20:55.859Z\", \"updated_at\": \"2026-05-19T01:08:20.832Z\", \"hypothesis\": \"LLaMA-based model with LoRA fine-tuning on Few-NERD can provide a second model family (beyond Qwen) for cross-model generalization evidence of structured self-consistency phenomena in NER\", \"spec\": {\"command\": \"llamafactory-cli train train_config_llama_fewnerd.yaml\", \"server\": \"autodl-5090\", \"gpu\": \"cuda:1\", \"pid\": 137865, \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/data/fewnerd\", \"data_count\": -1, \"model_name\": \"LLaMA-Few-NERD-LoRA\", \"seed\": 42, \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/logs/llama_fewnerd_train.log\", \"run_script\": \"run_llama_fewnerd_train_single_gpu.sh\", \"tmux_session\": \"llama_fewnerd\", \"note\": \"Retroactively registered - data_count unknown, seed assumed 42\"}, \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/checkpoints/llama3.1-8b-fewnerd-lora\", \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/logs/llama_fewnerd_train.log\", \"conclusion\": \"success\", \"metrics\": {\"epoch\": 3, \"train_loss\": 0.0516, \"eval_loss\": 0.0323, \"train_runtime_hours\": 15.35, \"total_steps\": 24708, \"final_checkpoint\": \"checkpoint-24708\", \"adapter_size_mb\": 320}, \"completed_at\": \"2026-05-19T01:08:20.832Z\"}, \"hidden_state_probe_conll_full\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T12:57:45.711Z\", \"updated_at\": \"2026-05-19T00:30:18.272Z\", \"conclusion\": \"killed\", \"notes\": \"Not in D154 Dual Contribution framing\", \"completed_at\": \"2026-05-19T00:30:18.272Z\"}, \"hidden_state_probe_conll_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T12:35:05.317Z\", \"updated_at\": \"2026-05-19T00:30:16.471Z\", \"conclusion\": \"killed\", \"notes\": \"Not in D154 Dual Contribution framing\", \"completed_at\": \"2026-05-19T00:30:16.471Z\"}, \"exp_031_fewnerd_t12\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T20:04:12.040Z\", \"updated_at\": \"2026-05-19T00:30:14.652Z\", \"hypothesis\": \"FewNERD T=1.2 temperature ablation: test if higher temperature reduces degeneracy on FewNERD as observed on SciERC\", \"conclusion\": \"killed\", \"failure_reason\": \"数据不可用于论文：测试集(37648 vs T=1.0的5000)、N(8 vs 16)、分析管道(MVP pilot vs 5-signal)三重不一致。Director决定不重跑(DDL约束+非核心claim)。\", \"notes\": \"T=1.2 ablation not in paper scope, SciERC T=1.2 sufficient\", \"completed_at\": \"2026-05-19T00:30:14.652Z\"}, \"exp_030_conll_t12\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T20:24:47.839Z\", \"updated_at\": \"2026-05-19T00:30:12.698Z\", \"hypothesis\": \"CoNLL T=1.2 temperature ablation: test if higher temperature reduces degeneracy on CoNLL as observed on SciERC\", \"conclusion\": \"killed\", \"failure_reason\": \"数据不可用于论文：N不一致(N=8 vs T=1.0基准的N=16)。Director决定不重跑——SciERC T消融(T=0.5/0.8/1.0/1.2, 551inst, N=8)已够用，论文温度消融用SciERC单数据集。\", \"notes\": \"T=1.2 ablation not in paper scope, SciERC T=1.2 sufficient\", \"completed_at\": \"2026-05-19T00:30:12.699Z\"}, \"mbr_pilot\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T17:56:06.462Z\", \"updated_at\": \"2026-05-19T00:29:39.285Z\", \"conclusion\": \"killed\", \"notes\": \"MBR tested negative as one of 6 methods, stale entry\", \"completed_at\": \"2026-05-19T00:29:39.285Z\"}, \"dgs_pilot\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T17:56:04.572Z\", \"updated_at\": \"2026-05-19T00:29:37.275Z\", \"hypothesis\": \"Degeneracy-Gated Selection (DGS) validates Two-Condition Theory: using degeneracy rate as gating mechanism to switch between greedy (degenerate) and LP selection (non-degenerate), the improvement direction should follow a monotonic gradient — low degeneracy yields positive delta, high degeneracy yields negative delta.\", \"conclusion\": \"killed\", \"notes\": \"D154: DGS demoted to explored heuristic, cross-model direction contradiction (D152)\", \"completed_at\": \"2026-05-19T00:29:37.275Z\"}, \"exp_fewnerd_s789_n8\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T23:17:34.011Z\", \"updated_at\": \"2026-05-18T23:18:28.125Z\", \"hypothesis\": \"FewNERD seed789 (4th seed) for statistical CI strengthening: 4-seed protocol provides tighter confidence intervals on LP selection gain and DGS effectiveness in low-degeneracy regime.\", \"parent\": \"exp_029a\", \"spec\": {\"command\": \"python code/analyze_fewnerd_s789.py\", \"server\": \"autodl-5090\", \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/fewnerd_seed789_merged/samples.jsonl\", \"data_count\": 37648, \"model_name\": \"Qwen3-8B (ft_002_v2)\", \"seed\": 789, \"checkpoint_source\": \"exp_021 shards\", \"eval_data\": \"FewNERD test (37648 instances, 32565 gold-filtered)\", \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/fewnerd_seed789_merged/\", \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/fewnerd_seed789_merged/run.log\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T23:18:17.902Z\", \"metrics\": {\"greedy_f1\": 0.7478, \"oracle_f1\": 0.8714, \"headroom_pp\": 12.37, \"degen_rate\": 0.1177, \"degen_rate_source\": \"unified_metrics_constant_f1_gold_filtered\", \"instance_count\": 37648, \"n_valid\": 32565, \"lp_sel_f1\": 0.7614, \"lp_delta_pp\": 1.36, \"lp_rho_global\": 0.1788, \"lp_rho_cond\": 0.176, \"dgs_f1\": 0.7621, \"dgs_delta_pp\": 1.43, \"dgs_vs_lp_pp\": 0.07, \"best_signal\": \"LP\", \"four_seed_mean_greedy\": 0.7481, \"four_seed_mean_lp_delta_pp\": 1.38, \"four_seed_lp_delta_ci95\": [1.32, 1.44]}}, \"exp_026_t12_seed456\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T22:05:43.694Z\", \"updated_at\": \"2026-05-18T22:07:24.547Z\", \"hypothesis\": \"Temperature ablation (T=1.2, seed=456) of Qwen3-8B SciERC N=8 SCS inference to study temperature sensitivity of structural consistency signals.\", \"spec\": {\"command\": \"python scs_inference.py --dataset scierc --seed 456 --n_samples 8 --temperature 1.2\", \"server\": \"autodl-5090\", \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/data/scierc\", \"data_count\": 551, \"model_name\": \"Qwen3-8B\", \"seed\": 456, \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_026_t12_seed456\", \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_026_t12_seed456.log\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T22:07:05.941Z\", \"metrics\": {\"ner_greedy_f1\": 0.6637, \"ner_oracle_f1\": 0.7821, \"rho_sj_ner\": 0.3995, \"sample_f1_pct_zero\": 14.08, \"instance_count\": 551, \"n_valid\": 529}}, \"exp_026_t12_seed123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T22:05:42.754Z\", \"updated_at\": \"2026-05-18T22:07:23.135Z\", \"hypothesis\": \"Temperature ablation (T=1.2, seed=123) of Qwen3-8B SciERC N=8 SCS inference to study temperature sensitivity of structural consistency signals.\", \"spec\": {\"command\": \"python scs_inference.py --dataset scierc --seed 123 --n_samples 8 --temperature 1.2\", \"server\": \"autodl-5090\", \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/data/scierc\", \"data_count\": 551, \"model_name\": \"Qwen3-8B\", \"seed\": 123, \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_026_t12_seed123\", \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_026_t12_seed123.log\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T22:07:04.119Z\", \"metrics\": {\"ner_greedy_f1\": 0.6595, \"ner_oracle_f1\": 0.7895, \"rho_sj_ner\": 0.359, \"sample_f1_pct_zero\": 13.99, \"instance_count\": 551, \"n_valid\": 529}}, \"exp_026_t10_seed456\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T22:05:41.840Z\", \"updated_at\": \"2026-05-18T22:07:21.767Z\", \"hypothesis\": \"Temperature ablation (T=1.0, seed=456) of Qwen3-8B SciERC N=8 SCS inference to study temperature sensitivity of structural consistency signals.\", \"spec\": {\"command\": \"python scs_inference.py --dataset scierc --seed 456 --n_samples 8 --temperature 1.0\", \"server\": \"autodl-5090\", \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/data/scierc\", \"data_count\": 551, \"model_name\": \"Qwen3-8B\", \"seed\": 456, \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_026_t10_seed456\", \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_026_t10_seed456.log\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T22:07:02.272Z\", \"metrics\": {\"ner_greedy_f1\": 0.6621, \"ner_oracle_f1\": 0.7754, \"rho_sj_ner\": 0.3921, \"sample_f1_pct_zero\": 12.97, \"instance_count\": 551, \"n_valid\": 529}}, \"exp_026_t10_seed123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T22:05:40.599Z\", \"updated_at\": \"2026-05-18T22:07:20.459Z\", \"hypothesis\": \"Temperature ablation (T=1.0, seed=123) of Qwen3-8B SciERC N=8 SCS inference to study temperature sensitivity of structural consistency signals.\", \"spec\": {\"command\": \"python scs_inference.py --dataset scierc --seed 123 --n_samples 8 --temperature 1.0\", \"server\": \"autodl-5090\", \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/data/scierc\", \"data_count\": 551, \"model_name\": \"Qwen3-8B\", \"seed\": 123, \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_026_t10_seed123\", \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_026_t10_seed123.log\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T22:07:00.430Z\", \"metrics\": {\"ner_greedy_f1\": 0.6633, \"ner_oracle_f1\": 0.7777, \"rho_sj_ner\": 0.3809, \"sample_f1_pct_zero\": 12.59, \"instance_count\": 551, \"n_valid\": 529}}, \"exp_026_t10_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T22:05:39.473Z\", \"updated_at\": \"2026-05-18T22:07:19.035Z\", \"hypothesis\": \"Temperature ablation (T=1.0, seed=42) of Qwen3-8B SciERC N=8 SCS inference to study temperature sensitivity of structural consistency signals.\", \"spec\": {\"command\": \"python scs_inference.py --dataset scierc --seed 42 --n_samples 8 --temperature 1.0\", \"server\": \"autodl-5090\", \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/data/scierc\", \"data_count\": 551, \"model_name\": \"Qwen3-8B\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_026_t10_seed42\", \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_026_t10_seed42.log\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T22:06:58.573Z\", \"metrics\": {\"ner_greedy_f1\": 0.6617, \"ner_oracle_f1\": 0.7798, \"rho_sj_ner\": 0.3598, \"sample_f1_pct_zero\": 12.9, \"instance_count\": 551, \"n_valid\": 529}}, \"exp_026_t08_seed456\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T22:05:38.605Z\", \"updated_at\": \"2026-05-18T22:07:17.604Z\", \"hypothesis\": \"Temperature ablation (T=0.8, seed=456) of Qwen3-8B SciERC N=8 SCS inference to study temperature sensitivity of structural consistency signals.\", \"spec\": {\"command\": \"python scs_inference.py --dataset scierc --seed 456 --n_samples 8 --temperature 0.8\", \"server\": \"autodl-5090\", \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/data/scierc\", \"data_count\": 551, \"model_name\": \"Qwen3-8B\", \"seed\": 456, \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_026_t08_seed456\", \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_026_t08_seed456.log\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T22:06:56.681Z\", \"metrics\": {\"ner_greedy_f1\": 0.6641, \"ner_oracle_f1\": 0.7694, \"rho_sj_ner\": 0.3771, \"sample_f1_pct_zero\": 11.79, \"instance_count\": 551, \"n_valid\": 529}}, \"exp_026_t08_seed123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T22:05:37.454Z\", \"updated_at\": \"2026-05-18T22:07:16.089Z\", \"hypothesis\": \"Temperature ablation (T=0.8, seed=123) of Qwen3-8B SciERC N=8 SCS inference to study temperature sensitivity of structural consistency signals.\", \"spec\": {\"command\": \"python scs_inference.py --dataset scierc --seed 123 --n_samples 8 --temperature 0.8\", \"server\": \"autodl-5090\", \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/data/scierc\", \"data_count\": 551, \"model_name\": \"Qwen3-8B\", \"seed\": 123, \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_026_t08_seed123\", \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_026_t08_seed123.log\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T22:06:54.734Z\", \"metrics\": {\"ner_greedy_f1\": 0.6607, \"ner_oracle_f1\": 0.7714, \"rho_sj_ner\": 0.3893, \"sample_f1_pct_zero\": 11.22, \"instance_count\": 551, \"n_valid\": 529}}, \"exp_026_t05_seed456\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T22:05:36.536Z\", \"updated_at\": \"2026-05-18T22:07:14.675Z\", \"hypothesis\": \"Temperature ablation (T=0.5, seed=456) of Qwen3-8B SciERC N=8 SCS inference to study temperature sensitivity of structural consistency signals.\", \"spec\": {\"command\": \"python scs_inference.py --dataset scierc --seed 456 --n_samples 8 --temperature 0.5\", \"server\": \"autodl-5090\", \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/data/scierc\", \"data_count\": 551, \"model_name\": \"Qwen3-8B\", \"seed\": 456, \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_026_t05_seed456\", \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_026_t05_seed456.log\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T22:06:52.749Z\", \"metrics\": {\"ner_greedy_f1\": 0.6639, \"ner_oracle_f1\": 0.7437, \"rho_sj_ner\": 0.3279, \"sample_f1_pct_zero\": 10.28, \"instance_count\": 551, \"n_valid\": 529}}, \"exp_026_t05_seed123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T22:05:35.201Z\", \"updated_at\": \"2026-05-18T22:07:13.198Z\", \"hypothesis\": \"Temperature ablation (T=0.5, seed=123) of Qwen3-8B SciERC N=8 SCS inference to study temperature sensitivity of structural consistency signals.\", \"spec\": {\"command\": \"python scs_inference.py --dataset scierc --seed 123 --n_samples 8 --temperature 0.5\", \"server\": \"autodl-5090\", \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/data/scierc\", \"data_count\": 551, \"model_name\": \"Qwen3-8B\", \"seed\": 123, \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_026_t05_seed123\", \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_026_t05_seed123.log\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T22:06:50.703Z\", \"metrics\": {\"ner_greedy_f1\": 0.6611, \"ner_oracle_f1\": 0.7444, \"rho_sj_ner\": 0.3133, \"sample_f1_pct_zero\": 10.09, \"instance_count\": 551, \"n_valid\": 529}}, \"exp_029b\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-17T23:32:18.543Z\", \"updated_at\": \"2026-05-18T22:05:45.856Z\", \"hypothesis\": \"Training convergence modulates degeneracy across datasets. SciERC 10-epoch training should produce higher degeneracy than 5-epoch baseline (17.8%), confirming monotonic epoch-degeneracy relationship across datasets.\", \"parent\": \"ft_002_v2\", \"failure_reason\": \"OOM on cuda:1 due to residual vLLM process (PID 416808) occupying 30.2GB VRAM\", \"reproduce\": {\"finished_at\": \"2026-05-18T02:05:15.948Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-18T00:55:29.806594+00:00\"}, {\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-18T01:58:43.646574+00:00\"}, {\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-18T02:05:20.480884+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\"}}, \"completed_at\": \"2026-05-18T00:56:47.625Z\", \"spec\": {\"pid\": \"441471\", \"server\": \"autodl-5090\", \"gpu\": \"cuda:1\", \"command\": \"FORCE_TORCHRUN=0 CUDA_VISIBLE_DEVICES=1 llamafactory-cli train train_config_scierc_10ep.yaml\", \"data_path\": \"scierc_uie_train\", \"data_count\": 1861, \"model_name\": \"Qwen3-8B\", \"seed\": 42, \"checkpoint_source\": \"Qwen/Qwen3-8B\", \"eval_data\": \"scierc_uie_test\", \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen3-8b-scierc-10epoch-lora/\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_029b.log\"}, \"metrics\": {\"degen_rate\": 0.478, \"degen_rate_source\": \"unified_metrics_constant_f1_gold_filtered\"}, \"conclusion\": \"success\"}, \"exp_029a\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T23:32:17.191Z\", \"updated_at\": \"2026-05-18T22:05:44.959Z\", \"hypothesis\": \"Training convergence modulates degeneracy across datasets. SciERC 3-epoch training should produce lower degeneracy than 5-epoch baseline (17.8%), confirming epoch confound is not Few-NERD-specific.\", \"parent\": \"ft_002_v2\", \"spec\": {\"command\": \"FORCE_TORCHRUN=0 CUDA_VISIBLE_DEVICES=0 bash -c \\\"source /root/miniconda3/bin/activate && cd /root/autodl-tmp/struct_self_consist_ie && llamafactory-cli train train_config_scierc_3ep.yaml\\\"\", \"server\": \"autodl-5090\", \"gpu\": \"cuda:0\", \"pid\": 436761, \"data_path\": \"data/scierc_uie_train\", \"data_count\": 1861, \"model_name\": \"Qwen3-8B LoRA rank=32\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen3-8b-scierc-3epoch-lora\", \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/logs/exp_029a_inference.log\", \"checkpoint_source\": \"Qwen/Qwen3-8B\", \"eval_data\": \"data/scierc_uie_dev\"}, \"reproduce\": {\"finished_at\": \"2026-05-18T00:55:16.392Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-18T00:55:20.617085+00:00\"}]}, \"failure_reason\": \"\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T01:00:18.242Z\", \"metrics\": {\"degen_rate\": 0.064, \"degen_rate_source\": \"unified_metrics_constant_f1_gold_filtered\"}}, \"exp_021_fewnerd_n8_seed456\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T22:03:17.992Z\", \"updated_at\": \"2026-05-18T22:04:50.774Z\", \"hypothesis\": \"Multi-seed replication (seed=456) of Qwen3-8B FewNERD N=8 SCS inference to validate structural consistency signal on fine-grained NER dataset.\", \"spec\": {\"command\": \"python scs_inference.py --dataset fewnerd --seed 456 --n_samples 8 --temperature 1.0\", \"server\": \"autodl-5090\", \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/data/fewnerd\", \"data_count\": 37648, \"model_name\": \"Qwen3-8B\", \"seed\": 456, \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_021_fewnerd_n8_seed456\", \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_021_fewnerd_n8_seed456_run.log\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T22:04:35.573Z\", \"metrics\": {\"degen_rate\": 0.1212, \"degen_rate_source\": \"unified_metrics_constant_f1_gold_filtered\", \"instance_count\": 37648, \"n_valid\": 32565, \"n_gold_empty\": 5083, \"ner_greedy_f1\": 0.7888, \"ner_oracle_f1\": 0.881, \"rho_fk_ner\": 0.1632, \"rho_sj_ner\": 0.313, \"sample_f1_pct_zero\": 19.32}}, \"exp_021_fewnerd_n8_seed123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T22:03:16.735Z\", \"updated_at\": \"2026-05-18T22:04:49.470Z\", \"hypothesis\": \"Multi-seed replication (seed=123) of Qwen3-8B FewNERD N=8 SCS inference to validate structural consistency signal on fine-grained NER dataset.\", \"spec\": {\"command\": \"python scs_inference.py --dataset fewnerd --seed 123 --n_samples 8 --temperature 1.0\", \"server\": \"autodl-5090\", \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/data/fewnerd\", \"data_count\": 37648, \"model_name\": \"Qwen3-8B\", \"seed\": 123, \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_021_fewnerd_n8_seed123\", \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_021_fewnerd_n8_seed123_run.log\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T22:04:33.731Z\", \"metrics\": {\"degen_rate\": 0.1312, \"degen_rate_source\": \"unified_metrics_constant_f1_gold_filtered\", \"instance_count\": 37648, \"n_valid\": 32565, \"n_gold_empty\": 5083, \"ner_greedy_f1\": 0.7885, \"ner_oracle_f1\": 0.8892, \"rho_fk_ner\": 0.1602, \"rho_sj_ner\": 0.3083, \"sample_f1_pct_zero\": 20.39}}, \"exp_002_conll_n16_seed456\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T22:03:15.720Z\", \"updated_at\": \"2026-05-18T22:04:46.954Z\", \"hypothesis\": \"Multi-seed replication (seed=456) of Qwen3-8B CoNLL-2003 N=16 SCS inference to validate structural consistency signal stability across random seeds.\", \"spec\": {\"command\": \"python scs_inference.py --dataset conll2003 --seed 456 --n_samples 16 --temperature 1.0\", \"server\": \"autodl-5090\", \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/data/conll2003\", \"data_count\": 3453, \"model_name\": \"Qwen3-8B\", \"seed\": 456, \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_002_conll_n16_seed456\", \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_002_conll_n16_seed456.log\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T22:04:31.934Z\", \"metrics\": {\"degen_rate\": 0.5544, \"degen_rate_source\": \"unified_metrics_constant_f1_gold_filtered\", \"instance_count\": 3453, \"n_valid\": 2756, \"n_gold_empty\": 697, \"ner_greedy_f1\": 0.9074, \"ner_oracle_f1\": 0.9549, \"rho_fk_ner\": 0.4718, \"rho_sj_ner\": 0.4819, \"sample_f1_pct_zero\": 7.02}}, \"exp_002_conll_n16_seed123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T22:03:14.343Z\", \"updated_at\": \"2026-05-18T22:04:45.039Z\", \"hypothesis\": \"Multi-seed replication (seed=123) of Qwen3-8B CoNLL-2003 N=16 SCS inference to validate structural consistency signal stability across random seeds.\", \"spec\": {\"command\": \"python scs_inference.py --dataset conll2003 --seed 123 --n_samples 16 --temperature 1.0\", \"server\": \"autodl-5090\", \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/data/conll2003\", \"data_count\": 3453, \"model_name\": \"Qwen3-8B\", \"seed\": 123, \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_002_conll_n16_seed123\", \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_002_conll_n16_seed123.log\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T22:04:29.992Z\", \"metrics\": {\"degen_rate\": 0.471, \"degen_rate_source\": \"unified_metrics_constant_f1_gold_filtered\", \"instance_count\": 3453, \"n_valid\": 2756, \"n_gold_empty\": 697, \"ner_greedy_f1\": 0.9068, \"ner_oracle_f1\": 0.9633, \"rho_fk_ner\": 0.4524, \"rho_sj_ner\": 0.4621, \"sample_f1_pct_zero\": 7.54}}, \"exp_017_llama_conll_n16_s456_r1024\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T22:17:04.572Z\", \"updated_at\": \"2026-05-18T20:50:15.047Z\", \"spec\": {\"hypothesis\": \"D054 rerun: max_tokens=1024. Verify truncation impact on LLaMA CoNLL N=16 seed456.\", \"parent\": \"exp_017_llama_conll_n16_s456\", \"model_name\": \"llama3.1-8b-conll2003-merged\", \"dataset\": \"CoNLL-2003\", \"seed\": 456, \"server\": \"autodl-5090\", \"command\": \"python code/run_mvp_pilot.py --model_path checkpoints/llama3.1-8b-conll2003-merged --data_dir data/conll2003 --dataset conll2003 --subtask ner --n_samples 16 --temperature 1.0 --seed 456 --num_test 9999 --max_tokens 1024 --collect_logprobs --output_dir output/exp_017_llama_conll_n16_s456_r1024\", \"gpu\": \"cuda:2\", \"pid\": \"175870\", \"data_path\": \"data/conll2003\", \"data_count\": 3453, \"tmux_session\": \"exp_017_llama_conll_n16_s456_r1024\"}, \"conclusion\": \"success\", \"metrics\": {\"degen_rate\": 0.8672, \"degen_rate_source\": \"unified_metrics_constant_f1_gold_filtered\", \"instance_count\": 3453, \"n_valid\": 2756, \"n_gold_empty\": 697, \"parse_rate\": 1, \"ner_greedy_f1\": 0.9265, \"ner_oracle_f1\": 0.9499, \"rho_fk_ner\": 0.469, \"rho_sj_ner\": 0.4734, \"rho_vc_ner\": 0.4722, \"rho_em_ner\": 0.4752, \"rho_lp_ner\": 0.3099, \"auroc_fk_ner\": 0.7408, \"auroc_sj_ner\": 0.7428, \"auroc_vc_ner\": 0.7495, \"auroc_em_ner\": 0.7444, \"auroc_lp_ner\": 0.7628, \"auroc_note\": \"median F1=1.0, AUROC uses >=median threshold\", \"rho_note\": \"CORRECTED 2026-05-15: old values (rho_fk=0.8085,rho_sj=0.1895) were inflated/deflated by 697 gold-empty instances. Now uses gold-filtered pipeline (n=2756).\"}, \"checkpoint_path\": \"N/A (inference-only)\", \"log_path\": \"output/exp_017_llama_conll_n16_s456_r1024_run.log\", \"completed_at\": \"2026-05-15T11:45:25.899Z\", \"hypothesis\": \"LLaMA CoNLL N=16 seed=456 (max_tokens=1024 rerun): cross-model multi-seed validation. Confirms structural>surface ordering is stable across seeds for LLaMA on CoNLL after gold-filtering correction.\"}, \"exp_017_llama_conll_n16_r1024\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T22:17:01.036Z\", \"updated_at\": \"2026-05-18T20:50:11.906Z\", \"spec\": {\"hypothesis\": \"D054 rerun: max_tokens=1024. Verify truncation impact on LLaMA CoNLL N=16 seed42.\", \"parent\": \"exp_017_llama_conll_n16\", \"model_name\": \"llama3.1-8b-conll2003-merged\", \"dataset\": \"CoNLL-2003\", \"seed\": 42, \"server\": \"autodl-5090\", \"command\": \"python code/run_mvp_pilot.py --model_path checkpoints/llama3.1-8b-conll2003-merged --data_dir data/conll2003 --dataset conll2003 --subtask ner --n_samples 16 --temperature 1.0 --seed 42 --num_test 9999 --max_tokens 1024 --collect_logprobs --output_dir output/exp_017_llama_conll_n16_r1024\", \"gpu\": \"cuda:1\", \"pid\": \"175734\", \"data_path\": \"data/conll2003\", \"data_count\": 3453, \"tmux_session\": \"exp_017_llama_conll_n16_r1024\"}, \"conclusion\": \"success\", \"metrics\": {\"degen_rate\": 0.8647, \"degen_rate_source\": \"unified_metrics_constant_f1_gold_filtered\", \"instance_count\": 3453, \"n_valid\": 2756, \"n_gold_empty\": 697, \"parse_rate\": 1, \"ner_greedy_f1\": 0.9265, \"ner_oracle_f1\": 0.9499, \"rho_fk_ner\": 0.4752, \"rho_sj_ner\": 0.4836, \"rho_vc_ner\": 0.4746, \"rho_em_ner\": 0.4818, \"rho_lp_ner\": 0.3136, \"auroc_fk_ner\": 0.7467, \"auroc_sj_ner\": 0.7496, \"auroc_vc_ner\": 0.7529, \"auroc_em_ner\": 0.7508, \"auroc_lp_ner\": 0.7661, \"auroc_note\": \"median F1=1.0, AUROC uses >=median threshold\", \"rho_note\": \"CORRECTED 2026-05-15: old values (rho_fk=0.8095,rho_sj=0.1815) were inflated/deflated by 697 gold-empty instances. Now uses gold-filtered pipeline (n=2756).\"}, \"checkpoint_path\": \"N/A (inference-only)\", \"log_path\": \"output/exp_017_llama_conll_n16_r1024_run.log\", \"completed_at\": \"2026-05-15T11:45:23.213Z\", \"hypothesis\": \"LLaMA CoNLL N=16 seed=42 (max_tokens=1024 rerun): cross-model baseline on CoNLL. Establishes LLaMA signal rankings after gold-filtering correction (fixes inflated FK ρ from gold-empty instances).\"}, \"exp_018_llama_scierc_seed456_r1024\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T06:12:43.492Z\", \"updated_at\": \"2026-05-18T20:50:04.988Z\", \"spec\": {\"hypothesis\": \"D066 fresh rerun: LLaMA SciERC seed=456 with explicit max_tokens=1024. Replaces exp_007 re-analysis for clean 3-seed comparison.\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && PYTHONPATH=code python code/run_mvp_pilot.py --model_path checkpoints/llama3.1-8b-scierc-merged --data_dir data/scierc/processed_data --dataset scierc --subtask joint --n_samples 8 --temperature 1.0 --seed 456 --max_tokens 1024 --num_test 9999 --collect_logprobs --output_dir output/exp_018_llama_scierc_seed456_r1024\\\"\", \"server\": \"autodl-5090\", \"seed\": 456, \"model_name\": \"LLaMA-3.1-8B-SciERC-merged\", \"model_path\": \"checkpoints/llama3.1-8b-scierc-merged\", \"dataset\": \"SciERC\", \"subtask\": \"joint\", \"data_path\": \"data/scierc/processed_data\", \"data_count\": 551, \"N\": 8, \"T\": 1, \"max_tokens\": 1024, \"is_new_inference\": true, \"checkpoint_path\": \"output/exp_018_llama_scierc_seed456_r1024/\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_018_llama_scierc_seed456_r1024.log\"}, \"server\": \"autodl-5090\", \"gpu\": \"cuda:1\", \"pid\": \"157584\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_018_llama_scierc_seed456_r1024.log\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && PYTHONPATH=code python code/run_mvp_pilot.py --model_path checkpoints/llama3.1-8b-scierc-merged --data_dir data/scierc/processed_data --dataset scierc --subtask joint --n_samples 8 --temperature 1.0 --seed 456 --max_tokens 1024 --num_test 9999 --collect_logprobs --output_dir output/exp_018_llama_scierc_seed456_r1024\\\"\", \"finished_at\": \"2026-05-15T06:18:22.307Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T06:18:24.880896+00:00\"}]}, \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_018_llama_scierc_seed456_r1024\", \"metrics\": {\"degen_rate\": 0.2741, \"degen_rate_source\": \"unified_metrics_constant_f1_gold_filtered\", \"ner_greedy_f1\": 0.6597, \"ner_oracle_f1\": 0.7683, \"ner_oracle_headroom\": 0.1086, \"ner_cond_rho_fk\": 0.1472, \"ner_cond_rho_sj\": 0.2718, \"ner_cond_rho_logprob\": 0.083, \"ner_logprob_auroc_cond\": 0.5485, \"re_greedy_f1\": 0.4338, \"re_oracle_f1\": 0.5834, \"re_oracle_headroom\": 0.1496, \"re_cond_rho_fk\": 0.2107, \"re_cond_rho_sj\": 0.3898, \"re_cond_rho_logprob\": 0.1252, \"re_logprob_auroc_cond\": 0.6119, \"ner_structural_beats_logprob\": true, \"re_structural_beats_logprob\": true}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T06:21:45.350Z\", \"hypothesis\": \"LLaMA SciERC seed=456 (max_tokens=1024): multi-seed cross-model validation. Complements seed42 for LLaMA 3-seed protocol on SciERC NER+RE signal rankings.\"}, \"exp_018_llama_scierc_seed42_r1024\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T06:09:57.155Z\", \"updated_at\": \"2026-05-18T20:50:00.335Z\", \"spec\": {\"hypothesis\": \"D066 fresh rerun: LLaMA SciERC seed=42 with explicit max_tokens=1024. Replaces exp_007_llama_inference for clean 3-seed comparison.\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && PYTHONPATH=code python code/run_mvp_pilot.py --model_path checkpoints/llama3.1-8b-scierc-merged --data_dir data/scierc/processed_data --dataset scierc --subtask joint --n_samples 8 --temperature 1.0 --seed 42 --max_tokens 1024 --num_test 9999 --collect_logprobs --output_dir output/exp_018_llama_scierc_seed42_r1024\\\"\", \"server\": \"autodl-5090\", \"seed\": 42, \"model_name\": \"LLaMA-3.1-8B-SciERC-merged\", \"model_path\": \"checkpoints/llama3.1-8b-scierc-merged\", \"dataset\": \"SciERC\", \"subtask\": \"joint\", \"data_path\": \"data/scierc/processed_data\", \"data_count\": 551, \"N\": 8, \"T\": 1, \"max_tokens\": 1024, \"is_new_inference\": true, \"checkpoint_path\": \"output/exp_018_llama_scierc_seed42_r1024/\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_018_llama_scierc_seed42_r1024.log\"}, \"server\": \"autodl-5090\", \"gpu\": \"cuda:0\", \"pid\": \"156809\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_018_llama_scierc_seed42_r1024.log\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && PYTHONPATH=code python code/run_mvp_pilot.py --model_path checkpoints/llama3.1-8b-scierc-merged --data_dir data/scierc/processed_data --dataset scierc --subtask joint --n_samples 8 --temperature 1.0 --seed 42 --max_tokens 1024 --num_test 9999 --collect_logprobs --output_dir output/exp_018_llama_scierc_seed42_r1024\\\"\", \"finished_at\": \"2026-05-15T06:15:47.963Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T06:15:50.613872+00:00\"}]}, \"metrics\": {\"degen_rate\": 0.2495, \"degen_rate_source\": \"unified_metrics_constant_f1_gold_filtered\", \"ner\": {\"full\": {\"SJ\": {\"rho\": 0.3096, \"tau\": 0.2288, \"auroc\": 0.6683}, \"FK\": {\"rho\": 0.2352, \"tau\": 0.1759, \"auroc\": 0.6069}, \"logprob\": {\"rho\": 0.1503, \"tau\": 0.1087, \"auroc\": 0.5318}, \"EM\": {\"rho\": 0.2587, \"tau\": 0.1966, \"auroc\": 0.7174}, \"voting_conf\": {\"rho\": 0.4053, \"tau\": 0.3042, \"auroc\": 0.6967}}, \"conditional\": {\"SJ\": {\"rho\": 0.2718, \"tau\": null, \"auroc\": 0.6565}, \"FK\": {\"rho\": 0.1472, \"tau\": null, \"auroc\": 0.5866}, \"logprob\": {\"rho\": 0.081, \"tau\": null, \"auroc\": 0.5129}, \"EM\": {\"rho\": 0.3165, \"tau\": null, \"auroc\": 0.7244}, \"voting_conf\": {\"rho\": 0.3078, \"tau\": null, \"auroc\": 0.6714}}, \"greedy_f1\": 0.6607, \"oracle_f1\": 0.7781, \"n_full\": 529, \"n_cond\": 478}, \"re\": {\"full\": {\"SJ\": {\"rho\": 0.2748, \"tau\": 0.2102, \"auroc\": 0.7244}, \"FK\": {\"rho\": 0.3027, \"tau\": 0.2337, \"auroc\": 0.691}, \"logprob\": {\"rho\": 0.3163, \"tau\": 0.233, \"auroc\": 0.6313}, \"EM\": {\"rho\": 0.1681, \"tau\": 0.1275, \"auroc\": 0.7697}, \"voting_conf\": {\"rho\": 0.384, \"tau\": 0.2965, \"auroc\": 0.7337}}, \"conditional\": {\"SJ\": {\"rho\": 0.3461, \"tau\": null, \"auroc\": 0.7233}, \"FK\": {\"rho\": 0.1969, \"tau\": null, \"auroc\": 0.6684}, \"logprob\": {\"rho\": 0.0888, \"tau\": null, \"auroc\": 0.5556}, \"EM\": {\"rho\": 0.4969, \"tau\": null, \"auroc\": 0.819}, \"voting_conf\": {\"rho\": 0.3433, \"tau\": null, \"auroc\": 0.7003}}, \"greedy_f1\": 0.4319, \"oracle_f1\": 0.5775, \"n_full\": 397, \"n_cond\": 251}}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T06:21:47.660Z\", \"hypothesis\": \"LLaMA SciERC seed=42 (max_tokens=1024): cross-model validation on SciERC. Establishes LLaMA NER signal rankings on same dataset as Qwen for direct model-family comparison.\"}, \"exp_002_conll_n16\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T18:12:16.041Z\", \"updated_at\": \"2026-05-18T20:49:50.398Z\", \"spec\": {\"hypothesis\": \"Qwen CoNLL-2003 N=16: cross-dataset N-scaling comparison with SciERC N=16\", \"plan_id\": \"exp-002\", \"parent\": \"exp_002_ner_conll2003\", \"command\": \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && CUDA_VISIBLE_DEVICES=0 PYTHONPATH=code python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-conll2003-merged --data_dir data/conll2003 --dataset conll2003 --subtask ner --n_samples 16 --temperature 1.0 --seed 42 --num_test 9999 --collect_logprobs --output_dir output/exp_002_conll_n16\", \"server\": \"autodl-5090\", \"data_path\": \"data/conll2003\", \"data_count\": 3453, \"model_name\": \"qwen3-8b-conll2003-merged\", \"seed\": 42}, \"conclusion\": \"success\", \"metrics\": {\"degen_rate\": 0.4844, \"degen_rate_source\": \"unified_metrics_constant_f1_gold_filtered\", \"N\": 16, \"dataset\": \"conll2003\", \"subtask\": \"ner\", \"n_instances\": 3453, \"n_valid\": 2756, \"n_conditional\": 2614, \"greedy_f1\": 0.907, \"full\": {\"SJ_rho\": 0.4496, \"FK_rho\": 0.3928, \"logprob_rho\": 0.3146, \"EM_rho\": 0.4627, \"voting_conf_rho\": 0.4286, \"SJ_AUROC\": 0.8264, \"FK_AUROC\": 0.7821, \"logprob_AUROC\": 0.7531, \"EM_AUROC\": 0.8409, \"voting_conf_AUROC\": 0.8071, \"SJ_ECE\": 0.0747, \"FK_ECE\": 0.1786, \"logprob_ECE\": 0.2031, \"EM_ECE\": 0.0786, \"voting_conf_ECE\": 0.529}, \"conditional\": {\"SJ_rho\": 0.4208, \"FK_rho\": 0.3494, \"logprob_rho\": 0.3756, \"EM_rho\": 0.4658, \"voting_conf_rho\": 0.3654, \"SJ_AUROC\": 0.8405, \"FK_AUROC\": 0.7819, \"logprob_AUROC\": 0.8259, \"EM_AUROC\": 0.8781, \"voting_conf_AUROC\": 0.7951, \"SJ_ECE\": 0.0982, \"FK_ECE\": 0.1899, \"logprob_ECE\": 0.2504, \"EM_ECE\": 0.0997, \"voting_conf_ECE\": 0.6096}, \"n8_vs_n16_delta_rho_full\": {\"SJ\": 0.0139, \"FK\": -0.007, \"logprob\": -0.0011, \"EM\": 0.012, \"voting_conf\": 0.0049}}, \"checkpoint_path\": \"output/exp_002_conll_n16/samples.jsonl\", \"log_path\": \"output/exp_002_conll_n16.log\", \"completed_at\": \"2026-05-14T18:58:40.473Z\", \"hypothesis\": \"CoNLL N=16 NER: cross-dataset validation on high-performance NER dataset. Tests if structural signals retain advantage when base model performance is already high (greedy F1 > 0.9).\"}, \"exp_012_rerun_1024\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T22:11:33.777Z\", \"updated_at\": \"2026-05-18T20:49:42.395Z\", \"spec\": {\"hypothesis\": \"Verify if max_tokens=512 truncation inflated Table 1 N=8 SciERC signal values. Rerun with max_tokens=1024 for clean comparison.\", \"model_name\": \"qwen3-8b-scierc-merged-v2\", \"dataset\": \"SciERC\", \"parent\": \"exp_012_logprob_baseline\", \"data_count\": 551, \"seed\": 42, \"server\": \"autodl-5090\", \"command\": \"CUDA_VISIBLE_DEVICES=0 python3 code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc/processed_data --dataset scierc --subtask joint --n_samples 8 --temperature 1.0 --max_tokens 1024 --seed 42 --num_test 9999 --collect_logprobs --output_dir output/exp_012_rerun_1024\", \"checkpoint_path\": \"output/exp_012_rerun_1024/\", \"log_path\": \"output/exp_012_rerun_1024/run.log\", \"data_path\": \"data/scierc/processed_data\"}, \"conclusion\": \"success\", \"metrics\": {\"degen_rate\": 0.1777, \"degen_rate_source\": \"unified_metrics_constant_f1_gold_filtered\", \"ner_full\": {\"n\": 529, \"SJ\": {\"rho\": 0.3599, \"tau\": 0.2646, \"AUROC\": 0.6917, \"ECE\": 0.4531, \"rho_ci95\": [0.2732, 0.4389], \"AUROC_ci95\": [0.6304, 0.7406]}, \"FK\": {\"rho\": 0.2665, \"tau\": 0.1974, \"AUROC\": 0.629, \"ECE\": 0.4512, \"rho_ci95\": [0.1743, 0.3486], \"AUROC_ci95\": [0.5612, 0.6882]}, \"logprob\": {\"rho\": 0.2052, \"tau\": 0.1478, \"AUROC\": 0.5783, \"ECE\": 0.7064, \"rho_ci95\": [0.1171, 0.2904], \"AUROC_ci95\": [0.5179, 0.6387]}, \"EM\": {\"rho\": 0.2945, \"tau\": 0.2208, \"AUROC\": 0.7493, \"ECE\": 0.3526, \"rho_ci95\": [0.2094, 0.37], \"AUROC_ci95\": [0.7002, 0.7928]}, \"voting_conf\": {\"rho\": 0.3792, \"tau\": 0.2805, \"AUROC\": 0.6841, \"ECE\": 0.3807, \"rho_ci95\": [0.2972, 0.4486], \"AUROC_ci95\": [0.6249, 0.7366]}}, \"ner_cond\": {\"n\": 477, \"SJ\": {\"rho\": 0.3113, \"tau\": 0.2257, \"AUROC\": 0.6772, \"ECE\": 0.4416, \"rho_ci95\": [0.2353, 0.3959], \"AUROC_ci95\": [0.621, 0.7337]}, \"FK\": {\"rho\": 0.1761, \"tau\": 0.1284, \"AUROC\": 0.6078, \"ECE\": 0.4389, \"rho_ci95\": [0.0839, 0.2665], \"AUROC_ci95\": [0.5442, 0.6709]}, \"logprob\": {\"rho\": 0.1538, \"tau\": 0.1111, \"AUROC\": 0.5633, \"ECE\": 0.6803, \"rho_ci95\": [0.0637, 0.2424], \"AUROC_ci95\": [0.5032, 0.6232]}, \"EM\": {\"rho\": 0.3596, \"tau\": 0.2735, \"AUROC\": 0.7556, \"ECE\": 0.3257, \"rho_ci95\": [0.2819, 0.4408], \"AUROC_ci95\": [0.7011, 0.8107]}, \"voting_conf\": {\"rho\": 0.3, \"tau\": 0.2189, \"AUROC\": 0.6618, \"ECE\": 0.3746, \"rho_ci95\": [0.2168, 0.3836], \"AUROC_ci95\": [0.6004, 0.7201]}}, \"re_full\": {\"n\": 397, \"SJ\": {\"rho\": 0.2503, \"tau\": 0.1878, \"AUROC\": 0.6702, \"ECE\": 0.3865}, \"FK\": {\"rho\": 0.2752, \"tau\": 0.2117, \"AUROC\": 0.6089, \"ECE\": 0.4405}, \"logprob\": {\"rho\": 0.2662, \"tau\": 0.1951, \"AUROC\": 0.6005, \"ECE\": 0.7694}, \"EM\": {\"rho\": 0.1344, \"tau\": 0.1081, \"AUROC\": 0.7059, \"ECE\": 0.3548}, \"voting_conf\": {\"rho\": 0.3498, \"tau\": 0.2663, \"AUROC\": 0.6935, \"ECE\": 0.2724}}, \"re_cond\": {\"n\": 238, \"SJ\": {\"rho\": 0.2457, \"tau\": 0.1811, \"AUROC\": 0.6463, \"ECE\": 0.2941}, \"FK\": {\"rho\": 0.1139, \"tau\": 0.0876, \"AUROC\": 0.551, \"ECE\": 0.3424}, \"logprob\": {\"rho\": 0.0112, \"tau\": 0.0051, \"AUROC\": 0.5186, \"ECE\": 0.6464}, \"EM\": {\"rho\": 0.4165, \"tau\": 0.3256, \"AUROC\": 0.7515, \"ECE\": 0.2232}, \"voting_conf\": {\"rho\": 0.2409, \"tau\": 0.178, \"AUROC\": 0.642, \"ECE\": 0.207}}, \"delta_vs_512_ner_full_rho\": {\"SJ\": 0.0034, \"FK\": 0.0014, \"EM\": 0.0379, \"voting_conf\": -0.1226, \"logprob\": 0.0656}, \"provenance_note\": \"exp_015_v2 scierc_n8_logprob used exp_012_logprob (max_tokens=512 truncated data). voting_conf was inflated 0.502→0.379, logprob was suppressed 0.140→0.205.\"}, \"completed_at\": \"2026-05-14T23:10:33.075Z\", \"hypothesis\": \"Canonical SciERC baseline with max_tokens=1024: Qwen3-8B ft_002_v2, N=8, T=1.0, seed=42, joint NER+RE. Establishes ground-truth ρ rankings and selection F1 for all 5 signals under correct generation length.\"}, \"exp_llama_scierc_seed456\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T19:15:27.504Z\", \"updated_at\": \"2026-05-18T20:49:10.758Z\", \"hypothesis\": \"LLaMA-3.1-8B on SciERC with seed=456 will show consistent 5-signal ranking patterns (SJ/FK > logprob) and DGS selection gains comparable to seed=42 and seed=123, confirming cross-seed stability.\", \"spec\": {\"command\": \"python3 code/analyze_llama_scierc_seed456_5signal.py\", \"server\": \"autodl-5090\", \"data_path\": \"output/exp_018_llama_scierc_seed456/samples.jsonl\", \"data_count\": 551, \"model_name\": \"LLaMA-3.1-8B-Instruct\", \"seed\": 456, \"checkpoint_source\": \"same as seed123\", \"eval_data\": \"SciERC test (551 instances)\", \"checkpoint_path\": \"output/exp_018_llama_scierc_seed456/5signal_dgs_report.json\", \"log_path\": \"output/exp_018_llama_scierc_seed456/run.log\"}, \"metrics\": {\"greedy_f1\": 0.6457, \"oracle_f1\": 0.7574, \"headroom\": 0.1117, \"dgs_f1\": 0.6454, \"degen_rate\": 0.2741, \"degen_rate_source\": \"unified_metrics_constant_f1_gold_filtered\", \"rho_SJ_full\": 0.3663, \"rho_FK_full\": 0.3115, \"rho_logprob_full\": 0.1911, \"rho_EM_full\": 0.3088, \"rho_vc_full\": 0.4135, \"auroc_SJ_full\": 0.7061, \"auroc_EM_full\": 0.7538, \"n_valid\": 529, \"n_conditional\": 478}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T19:16:00.973Z\"}, \"exp_007_llama_scierc_seed123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T19:10:26.278Z\", \"updated_at\": \"2026-05-18T20:49:08.934Z\", \"name\": \"LLaMA-3.1-8B SciERC NER inference seed=123\", \"hypothesis\": \"Structural consistency signals (SJ, FK) correlate with entity F1 for LLaMA-8B on SciERC at seed=123, and DGS selection improves over greedy baseline\", \"spec\": {\"command\": \"python3 code/run_mvp_pilot.py --model_path checkpoints/llama3.1-8b-scierc-merged --data_dir data/scierc/processed_data --dataset scierc --subtask joint --n_samples 8 --temperature 1.0 --seed 123 --num_test 9999 --collect_logprobs --output_dir output/exp_018_llama_scierc_seed123\", \"server\": \"autodl-5090\", \"data_path\": \"data/scierc/processed_data\", \"data_count\": 551, \"model_name\": \"LLaMA-3.1-8B-Instruct (SciERC LoRA fine-tuned)\", \"seed\": 123, \"checkpoint_source\": \"checkpoints/llama3.1-8b-scierc-merged\", \"checkpoint_path\": \"checkpoints/llama3.1-8b-scierc-lora\", \"log_path\": \"output/exp_018_llama_scierc_seed123/report.json\"}, \"conclusion\": \"negative\", \"completed_at\": \"2026-05-18T19:11:30.781Z\", \"metrics\": {\"greedy_f1\": 0.6454, \"oracle_f1\": 0.7657, \"headroom\": 0.1204, \"degen_rate\": 0.2665, \"degen_rate_source\": \"unified_metrics_constant_f1_gold_filtered\", \"dgs_delta_pp\": -0.38, \"rho_SJ_full\": 0.3552, \"rho_voting_conf_full\": 0.4193, \"auroc_SJ_full\": 0.7092, \"auroc_EM_full\": 0.7468}}, \"exp_qwen3_4b_conll_scs_inference\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T19:08:28.512Z\", \"updated_at\": \"2026-05-18T20:49:06.922Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && PYTHONPATH=code python code/run_mvp_pilot.py --model_path checkpoints/qwen3-4b-conll2003-merged --data_dir data/conll2003 --dataset conll2003 --subtask ner --n_samples 8 --temperature 1.0 --seed 42 --num_test 9999 --max_tokens 1024 --collect_logprobs --output_dir output/exp_qwen3_4b_conll_scs_inference\\\"\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:0\"], \"pid\": \"222184\", \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_qwen3_4b_conll_scs_inference/report.json\", \"submitted_at\": \"2026-05-15T19:10:19.757Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen3-4b-conll2003-merged\", \"wall_clock_seconds\": 523.8, \"gpu_hours\": 0.15}, \"metrics\": {\"greedy_f1\": 0.9251, \"oracle_f1\": 0.9408, \"oracle_headroom_pp\": 1.57, \"SJ_rho_full\": 0.4045, \"SJ_rho_cond\": 0.4306, \"FK_rho_full\": 0.3961, \"FK_rho_cond\": 0.42, \"LP_rho_full\": 0.3186, \"LP_rho_cond\": 0.3378, \"LP_auroc_full\": 0.7689, \"LP_auroc_cond\": 0.8153, \"fleiss_kappa_mean\": 0.9349, \"soft_jaccard_mean\": 0.9754, \"structural_beats_surface\": true, \"rho_advantage_pp\": 0.84, \"n_instances\": 3453, \"n_gold_empty_filtered\": 697, \"n_greedy_f1_zero_filtered\": 112, \"verdict\": \"MARGINAL\", \"degen_rate\": 0.9057, \"degen_rate_source\": \"unified_metrics_constant_f1_gold_filtered\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T19:19:03.585Z\", \"notes\": \"4B CoNLL SCS inference completed. SJ>FK>LP ordering preserved at 4B scale (rho 0.405>0.396>0.319). Greedy F1=0.925 outperforms 8B (0.907), but SJ rho is lower (0.405 vs 0.450 at 8B N=16). Structural beats surface confirmed (+0.84pp). Verdict MARGINAL due to small oracle headroom (1.57pp) — the model is already very good at CoNLL, leaving little room for selection improvement.\", \"hypothesis\": \"CoNLL 4B SCS inference (checkpoint-3800): cross-scale evidence for correlation-selection gap. Tests if structural>surface ranking and LP compression hold at smaller model scale on high-degeneracy dataset.\"}, \"exp_qwen3_4b_conll_scs_inference_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T19:41:33.501Z\", \"updated_at\": \"2026-05-18T20:49:03.705Z\", \"hypothesis\": \"CoNLL 4B SCS inference with best checkpoint-4200 (from resume training). Scale ablation: cross-scale evidence for correlation-selection gap. Compare vs v1 (ckpt-3800 baseline: greedy_f1=0.9251, SJ_rho=0.4045).\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python code/run_mvp_pilot.py --model_path checkpoints/qwen3-4b-conll2003-merged-ckpt4200 --data_dir data/conll2003 --dataset conll2003 --subtask ner --n_samples 8 --temperature 1.0 --seed 42 --num_test 9999 --max_tokens 1024 --collect_logprobs --output_dir output/exp_qwen3_4b_conll_scs_inference_v2\", \"server\": \"autodl-5090\", \"data_path\": \"data/conll2003\", \"data_count\": 3453, \"model_name\": \"Qwen3-4B (LoRA checkpoint-4200 merged)\", \"seed\": 42, \"checkpoint_source\": \"checkpoints/qwen3-4b-conll2003-lora/checkpoint-4200\", \"gpu\": [\"cuda:1\"], \"checkpoint_path\": \"checkpoints/qwen3-4b-conll2003-merged-ckpt4200\", \"log_path\": \"/tmp/infer_4b_conll_v2.log\", \"account\": \"root\", \"backend\": \"tmux\", \"tmux_session\": \"exp_4b_conll_scs_v2\"}, \"metrics\": {\"greedy_f1\": 0.9234, \"oracle_f1\": 0.9404, \"oracle_headroom_pp\": 1.7, \"SJ_rho_full\": 0.4217, \"SJ_rho_cond\": 0.459, \"FK_rho_full\": 0.4181, \"FK_rho_cond\": 0.4538, \"LP_rho_full\": 0.3313, \"LP_rho_cond\": 0.3487, \"LP_auroc_full\": 0.7761, \"LP_auroc_cond\": 0.8209, \"n_instances\": 3453, \"verdict\": \"MARGINAL\", \"degen_rate\": 0.9057, \"degen_rate_source\": \"unified_metrics_constant_f1_gold_filtered\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T19:54:14.575Z\", \"notes\": \"Gold-filter audit (2026-05-16): CONSISTENT. _full metrics (SJ_rho=0.4217, FK_rho=0.4181) are computed on gold-filtered set (n=2756), same as 8B Table 1 values. _full does NOT mean all 3453 instances — it means gold-nonempty instances. _cond further excludes greedy-F1=0 (n=2641). Confirmed via run_mvp_pilot.py source code and report.json n values.\"}, \"exp_qwen3_4b_scierc_scs_inference\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T19:45:33.384Z\", \"updated_at\": \"2026-05-18T20:49:01.260Z\", \"hypothesis\": \"SciERC 4B SCS inference after v4 finetune merge. Complete 2x2 scale matrix (4B SciERC cell). Cross-scale + cross-task evidence for correlation-selection gap.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 PYTHONPATH=code python code/run_mvp_pilot.py --model_path checkpoints/qwen3-4b-scierc-merged --data_dir data/scierc/processed_data --dataset scierc --subtask joint --n_samples 8 --temperature 1.0 --seed 42 --num_test 9999 --max_tokens 1024 --collect_logprobs --output_dir output/exp_qwen3_4b_scierc_scs_inference\", \"server\": \"autodl-5090\", \"data_path\": \"data/scierc/processed_data\", \"data_count\": 551, \"model_name\": \"qwen3-4b-scierc-merged (checkpoint-400)\", \"seed\": 42, \"checkpoint_source\": \"checkpoints/qwen3-4b-scierc-merged\", \"eval_data\": \"scierc test set\"}, \"metrics\": {\"ner_greedy_f1\": 0.6612, \"ner_oracle_f1\": 0.7839, \"ner_headroom_pp\": 12.28, \"ner_SJ_rho\": 0.4221, \"ner_FK_rho\": 0.3258, \"ner_LP_rho\": 0.28, \"re_greedy_f1\": 0.4136, \"re_oracle_f1\": 0.5846, \"re_headroom_pp\": 17.1, \"re_SJ_rho\": 0.2673, \"re_FK_rho\": 0.3593, \"re_LP_rho\": 0.3512, \"re_sample_f1_pct_zero\": 0.476, \"re_LP_rho_cond\": 0.1135, \"re_LP_rho_cond_p\": 0.074, \"degen_rate\": 0.104, \"degen_rate_source\": \"unified_metrics_constant_f1_gold_filtered\"}, \"checkpoint_path\": \"checkpoints/qwen3-4b-scierc-merged/\", \"log_path\": \"/tmp/exp_qwen3_4b_scierc_scs_inference.log\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T20:00:03.730Z\"}, \"exp_027_fewnerd_n16\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T05:28:57.036Z\", \"updated_at\": \"2026-05-18T20:48:58.455Z\", \"spec\": {\"hypothesis\": \"LP selection scales with N in low-degeneracy regime: N=16 should yield LP Δ > +2pp (vs N=8 +1.36pp) on Few-NERD (10% degen), because more samples increase oracle headroom while LP ranking remains effective.\", \"parent\": \"exp_021_fewnerd_full\", \"model_name\": \"qwen3-8b-fewnerd-exp021-merged\", \"data_path\": \"data/fewnerd_n16_subset/test.json\", \"data_count\": 5000, \"seed\": 42, \"server\": \"autodl-5090\", \"gpu\": \"cuda:0,cuda:1,cuda:2,cuda:3\", \"command\": \"python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-fewnerd-exp021-merged --data_dir data/fewnerd_n16_subset --dataset fewnerd --subtask ner --n_samples 16 --temperature 1.0 --seed 42 --collect_logprobs --start_index {0,1250,2500,3750} --end_index {1250,2500,3750,5000} --output_dir output/exp_027_fewnerd_n16/shard_{0-3}\", \"checkpoint_path\": \"output/exp_027_fewnerd_n16/sampled_results.jsonl\", \"log_path\": \"output/exp_027_fewnerd_n16/\"}, \"conclusion\": \"success\", \"metrics\": {\"LP_delta_pp\": 1.88, \"LP_delta_95CI\": [1.41, 2.37], \"degen_rate\": 0.0706, \"degen_rate_source\": \"unified_metrics_constant_f1_gold_filtered\", \"greedy_f1\": 0.7478, \"lp_sel_f1\": 0.7666, \"oracle_f1\": 0.902, \"headroom_pp\": 15.42, \"all_8_types_positive\": true, \"n_instances\": 5000, \"N_samples\": 16, \"bootstrap_p\": \"<0.001\"}, \"hypothesis\": \"LP selection scales with N in low-degeneracy regime: N=16 should yield LP Δ > +2pp (vs N=8 +1.36pp) on Few-NERD (10% degen), because more samples increase oracle headroom while LP ranking remains effective.\", \"completed_at\": \"2026-05-17T05:46:48.460Z\"}, \"exp_026_t12\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T13:18:18.780Z\", \"updated_at\": \"2026-05-18T20:48:24.965Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc/processed_data --dataset scierc --n_samples 8 --temperature 1.2 --seed 42 --max_tokens 1024 --collect_logprobs --output_dir output/exp_026_t12\", \"server\": \"autodl-5090\", \"data_path\": \"data/scierc/processed_data\", \"data_count\": 551, \"model_name\": \"qwen3-8b-scierc-merged-v2\", \"seed\": 42, \"log_path\": \"output/exp_026_t12.log\", \"checkpoint_path\": \"checkpoints/qwen3-8b-scierc-merged-v2\"}, \"conclusion\": \"success\", \"metrics\": {\"temperature\": 1.2, \"task\": \"T-ablation\", \"degen_rate\": 0.1493, \"degen_rate_source\": \"unified_metrics_constant_f1_gold_filtered\"}, \"completed_at\": \"2026-05-16T14:26:37.648Z\", \"hypothesis\": \"Temperature T=1.2 ablation on SciERC: test if higher temperature increases sample diversity (lower degeneracy) and LP discriminative range, potentially improving LP selection while maintaining structural signal effectiveness.\", \"parent\": \"exp_012_rerun_1024\"}, \"exp_026_t08\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T12:57:46.027Z\", \"updated_at\": \"2026-05-18T20:48:24.112Z\", \"spec\": {\"checkpoint_path\": \"checkpoints/qwen3-8b-scierc-merged-v2\", \"log_path\": \"output/exp_026_t08/run.log\"}, \"conclusion\": \"success\", \"metrics\": {\"temperature\": 0.8, \"task\": \"T-ablation\", \"degen_rate\": 0.2382, \"degen_rate_source\": \"unified_metrics_constant_f1_gold_filtered\"}, \"completed_at\": \"2026-05-16T14:26:36.243Z\", \"hypothesis\": \"Temperature T=0.8 ablation on SciERC: test if lower temperature increases LP compression (narrower range) while structural signals remain robust, supporting the claim that LP compression is intrinsic rather than temperature-driven.\", \"parent\": \"exp_012_rerun_1024\"}, \"exp_026_t05\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T12:19:35.753Z\", \"updated_at\": \"2026-05-18T20:48:23.339Z\", \"spec\": {\"checkpoint_path\": \"checkpoints/qwen3-8b-scierc-merged-v2\", \"log_path\": \"output/exp_026_t05/run.log\"}, \"conclusion\": \"success\", \"metrics\": {\"temperature\": 0.5, \"task\": \"T-ablation\", \"degen_rate\": 0.414, \"degen_rate_source\": \"unified_metrics_constant_f1_gold_filtered\"}, \"completed_at\": \"2026-05-16T14:26:34.808Z\", \"hypothesis\": \"Temperature T=0.5 ablation on SciERC: extreme low temperature expected to maximally compress LP scores and increase degeneracy, providing upper-bound evidence for LP compression as model-intrinsic phenomenon.\", \"parent\": \"exp_012_rerun_1024\"}, \"exp_026_T12\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T09:38:31.060Z\", \"updated_at\": \"2026-05-18T20:48:22.668Z\", \"hypothesis\": \"T=1.2 will decrease degeneracy rate and expand LP range vs T=1.0, but may degrade generation quality (lower greedy F1). Tests whether reducing degeneracy via higher T recovers selection headroom or if quality degradation offsets the benefit.\", \"server\": \"autodl-5090\", \"gpu\": \"cuda:3\", \"account\": \"root\", \"reproduce\": {\"server\": \"autodl-5090\", \"gpu\": \"cuda:3\", \"started_at\": \"2026-05-17T09:39:51.733Z\", \"command\": \"bash -c \\\"source /root/miniconda3/bin/activate && cd /root/autodl-tmp/struct_self_consist_ie && python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc/processed_data --dataset scierc --subtask joint --n_samples 8 --temperature 1.2 --seed 42 --output_dir output/exp_026_T12/ --num_test 9999 --collect_logprobs 2>&1 | tee output/exp_026_T12_run.log\\\"\", \"finished_at\": \"2026-05-17T09:48:04.019Z\", \"training_hours\": 0.14}, \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/bin/activate && cd /root/autodl-tmp/struct_self_consist_ie && python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc/processed_data --dataset scierc --subtask joint --n_samples 8 --temperature 1.2 --seed 42 --output_dir output/exp_026_T12/ --num_test 9999 --collect_logprobs 2>&1 | tee output/exp_026_T12_run.log\\\"\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:3\"], \"pid\": \"381369\", \"log_path\": \"output/exp_026_T12_run.log\", \"submitted_at\": \"2026-05-17T09:41:39.393Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"output/exp_026_T12/\", \"wall_clock_seconds\": 1114.4, \"gpu_hours\": 0.31}, \"pid\": \"381369\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_026_T12.log\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-17T09:48:08.312470+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"degen_rate\": 0.1493, \"degen_rate_source\": \"unified_metrics_constant_f1_gold_filtered\", \"lp_range_mean\": 0.075, \"lp_range_std\": 0.059, \"within_instance_rho_mean\": 0.2245, \"within_instance_rho_median\": 0.3152, \"within_instance_rho_valid_pct\": 0.875, \"greedy_f1\": 0.62, \"oracle_f1\": 0.758, \"lp_sel_f1\": 0.621, \"sj_sel_f1\": 0.597, \"em_sel_f1\": 0.596, \"vc_sel_f1\": 0.582, \"sj_rho\": 0.384, \"fk_rho\": 0.386, \"lp_rho\": 0.182, \"vc_rho\": 0.342, \"sj_auroc\": 0.683, \"lp_auroc\": 0.566}, \"completed_at\": \"2026-05-17T10:00:13.771Z\"}, \"exp_026_T08\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T09:38:29.602Z\", \"updated_at\": \"2026-05-18T20:48:21.975Z\", \"hypothesis\": \"T=0.8 will show intermediate degeneracy between T=0.5 and T=1.0, establishing a monotonic degeneracy-temperature relationship. If LP selection improves at T=0.8 vs T=1.0, it identifies the optimal operating point for the selection mechanism.\", \"server\": \"autodl-5090\", \"gpu\": \"cuda:2\", \"account\": \"root\", \"reproduce\": {\"server\": \"autodl-5090\", \"gpu\": \"cuda:2\", \"started_at\": \"2026-05-17T09:39:50.780Z\", \"command\": \"bash -c \\\"source /root/miniconda3/bin/activate && cd /root/autodl-tmp/struct_self_consist_ie && python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc/processed_data --dataset scierc --subtask joint --n_samples 8 --temperature 0.8 --seed 42 --output_dir output/exp_026_T08/ --num_test 9999 --collect_logprobs 2>&1 | tee output/exp_026_T08_run.log\\\"\", \"finished_at\": \"2026-05-17T09:47:56.543Z\", \"training_hours\": 0.13}, \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/bin/activate && cd /root/autodl-tmp/struct_self_consist_ie && python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc/processed_data --dataset scierc --subtask joint --n_samples 8 --temperature 0.8 --seed 42 --output_dir output/exp_026_T08/ --num_test 9999 --collect_logprobs 2>&1 | tee output/exp_026_T08_run.log\\\"\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:2\"], \"pid\": \"380680\", \"log_path\": \"output/exp_026_T08_run.log\", \"submitted_at\": \"2026-05-17T09:41:20.812Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"output/exp_026_T08/\", \"wall_clock_seconds\": 1131.4, \"gpu_hours\": 0.31}, \"pid\": \"380680\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_026_T08.log\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-17T09:48:02.635244+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"degen_rate\": 0.2382, \"degen_rate_source\": \"unified_metrics_constant_f1_gold_filtered\", \"lp_range_mean\": 0.043, \"lp_range_std\": 0.042, \"within_instance_rho_mean\": 0.1701, \"within_instance_rho_median\": 0.2635, \"within_instance_rho_valid_pct\": 0.728, \"greedy_f1\": 0.616, \"oracle_f1\": 0.737, \"lp_sel_f1\": 0.627, \"sj_sel_f1\": 0.619, \"em_sel_f1\": 0.611, \"vc_sel_f1\": 0.603, \"sj_rho\": 0.378, \"fk_rho\": 0.34, \"lp_rho\": 0.212, \"vc_rho\": 0.352, \"sj_auroc\": 0.662, \"lp_auroc\": 0.571}, \"completed_at\": \"2026-05-17T10:00:12.248Z\"}, \"exp_026_T05\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T09:38:28.066Z\", \"updated_at\": \"2026-05-18T20:48:16.286Z\", \"hypothesis\": \"T=0.5 will increase degeneracy rate (more deterministic outputs) and compress LP range on SciERC, reducing selection headroom. Maps the low-temperature end of the degeneracy-temperature frontier, validating that degeneracy is regime-dependent on sampling temperature.\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/bin/activate && cd /root/autodl-tmp/struct_self_consist_ie && python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc/processed_data --dataset scierc --subtask joint --n_samples 8 --temperature 0.5 --seed 42 --output_dir output/exp_026_T05/ --num_test 9999 --collect_logprobs 2>&1 | tee output/exp_026_T05_run.log\\\"\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:1\"], \"pid\": \"380188\", \"log_path\": \"output/exp_026_T05_run.log\", \"submitted_at\": \"2026-05-17T09:40:51.787Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"output/exp_026_T05/\", \"wall_clock_seconds\": 1158.3, \"gpu_hours\": 0.32}, \"server\": \"autodl-5090\", \"gpu\": \"cuda:1\", \"pid\": \"380188\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_026_T05.log\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/bin/activate && cd /root/autodl-tmp/struct_self_consist_ie && python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc/processed_data --dataset scierc --subtask joint --n_samples 8 --temperature 0.5 --seed 42 --output_dir output/exp_026_T05/ --num_test 9999 --collect_logprobs 2>&1 | tee output/exp_026_T05_run.log\\\"\", \"finished_at\": \"2026-05-17T09:47:31.332Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-17T09:47:35.127151+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"degen_rate\": 0.414, \"degen_rate_source\": \"unified_metrics_constant_f1_gold_filtered\", \"lp_range_mean\": 0.022, \"lp_range_std\": 0.021, \"within_instance_rho_mean\": 0.1306, \"within_instance_rho_median\": 0.2182, \"within_instance_rho_valid_pct\": 0.597, \"greedy_f1\": 0.617, \"oracle_f1\": 0.71, \"lp_sel_f1\": 0.622, \"sj_sel_f1\": 0.622, \"em_sel_f1\": 0.619, \"vc_sel_f1\": 0.61, \"sj_rho\": 0.333, \"fk_rho\": 0.341, \"lp_rho\": 0.208, \"vc_rho\": 0.353, \"sj_auroc\": 0.644, \"lp_auroc\": 0.577}, \"completed_at\": \"2026-05-17T10:00:10.083Z\"}, \"exp_017_llama_conll_n16_s123_r1024\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T22:17:02.953Z\", \"updated_at\": \"2026-05-18T20:47:52.122Z\", \"spec\": {\"hypothesis\": \"D054 rerun: max_tokens=1024. Verify truncation impact on LLaMA CoNLL N=16 seed123.\", \"parent\": \"exp_017_llama_conll_n16_s123\", \"model_name\": \"llama3.1-8b-conll2003-merged\", \"dataset\": \"CoNLL-2003\", \"seed\": 123, \"server\": \"autodl-5090\", \"command\": \"python code/run_mvp_pilot.py --model_path checkpoints/llama3.1-8b-conll2003-merged --data_dir data/conll2003 --dataset conll2003 --subtask ner --n_samples 16 --temperature 1.0 --seed 123 --num_test 9999 --max_tokens 1024 --collect_logprobs --output_dir output/exp_017_llama_conll_n16_s123_r1024\", \"data_path\": \"data/conll2003\", \"data_count\": 3453}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T01:20:51.219Z\", \"notes\": \"Output exists on autodl-5090. Registry status corrected from killed to success.\", \"hypothesis\": \"LLaMA CoNLL N=16 seed=123 (max_tokens=1024 rerun): cross-model multi-seed validation. Confirms structural>surface ordering is stable across seeds for LLaMA on CoNLL after gold-filtering correction.\", \"metrics\": {\"degen_rate\": 0.8636, \"degen_rate_source\": \"unified_metrics_constant_f1_gold_filtered\"}}, \"exp_018_llama_scierc_seed123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T06:07:14.370Z\", \"updated_at\": \"2026-05-18T20:47:51.435Z\", \"spec\": {\"hypothesis\": \"Multi-seed robustness: LLaMA SciERC N=8 seed=123, max_tokens=1024. Verify signal stability across seeds.\", \"command\": \"python code/run_mvp_pilot.py --model_path checkpoints/llama3.1-8b-scierc-merged --data_dir data/scierc/processed_data --dataset scierc --subtask joint --seed 123 --n_samples 8 --temperature 1.0 --max_tokens 1024 --output_dir output/exp_018_llama_scierc_seed123\", \"server\": \"autodl-5090\", \"seed\": 123, \"model_name\": \"LLaMA-3.1-8B-SciERC-merged\", \"data_path\": \"data/scierc/processed_data\", \"data_count\": 551, \"checkpoint_path\": \"output/exp_018_llama_scierc_seed123/\", \"log_path\": \"output/exp_018_llama_scierc_seed123.log\", \"samples_md5\": \"072eeca68236d46b4c5c84b945209abc\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T06:08:04.855Z\", \"hypothesis\": \"LLaMA SciERC seed=123: multi-seed cross-model validation. Complements seed42 for LLaMA 3-seed protocol on SciERC NER+RE signal rankings.\", \"metrics\": {\"degen_rate\": 0.2665, \"degen_rate_source\": \"unified_metrics_constant_f1_gold_filtered\"}}, \"exp_018_qwen_scierc_seed456\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T06:07:13.570Z\", \"updated_at\": \"2026-05-18T20:47:50.032Z\", \"spec\": {\"hypothesis\": \"Multi-seed robustness: Qwen SciERC N=8 seed=456, max_tokens=1024. Verify signal stability across seeds.\", \"command\": \"python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc/processed_data --dataset scierc --subtask joint --seed 456 --n_samples 8 --temperature 1.0 --max_tokens 1024 --output_dir output/exp_018_qwen_scierc_seed456\", \"server\": \"autodl-5090\", \"seed\": 456, \"model_name\": \"Qwen3-8B-SciERC-merged-v2\", \"data_path\": \"data/scierc/processed_data\", \"data_count\": 551, \"checkpoint_path\": \"output/exp_018_qwen_scierc_seed456/\", \"log_path\": \"output/exp_018_qwen_scierc_seed456/run.log\", \"samples_md5\": \"46d0de47ad7693c07e7df3a77c90c3be\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T06:08:03.898Z\", \"hypothesis\": \"Qwen SciERC seed=456: multi-seed Qwen validation. Part of 3-seed protocol (seed42=exp_012_rerun_1024, seed123, seed456) for statistical significance of signal rankings.\", \"metrics\": {\"degen_rate\": 0.2042, \"degen_rate_source\": \"unified_metrics_constant_f1_gold_filtered\"}}, \"exp_018_qwen_scierc_seed123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T06:07:12.747Z\", \"updated_at\": \"2026-05-18T20:47:49.306Z\", \"spec\": {\"hypothesis\": \"Multi-seed robustness: Qwen SciERC N=8 seed=123, max_tokens=1024. Verify signal stability across seeds.\", \"command\": \"python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc/processed_data --dataset scierc --subtask joint --seed 123 --n_samples 8 --temperature 1.0 --max_tokens 1024 --output_dir output/exp_018_qwen_scierc_seed123\", \"server\": \"autodl-5090\", \"seed\": 123, \"model_name\": \"Qwen3-8B-SciERC-merged-v2\", \"data_path\": \"data/scierc/processed_data\", \"data_count\": 551, \"checkpoint_path\": \"output/exp_018_qwen_scierc_seed123/\", \"log_path\": \"output/exp_018_qwen_scierc_seed123.log\", \"samples_md5\": \"866a59581dea56f4633149f0b18a31ae\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T06:08:02.954Z\", \"hypothesis\": \"Qwen SciERC seed=123: multi-seed Qwen validation. Part of 3-seed protocol (seed42=exp_012_rerun_1024, seed123, seed456) for statistical significance of signal rankings.\", \"metrics\": {\"degen_rate\": 0.172, \"degen_rate_source\": \"unified_metrics_constant_f1_gold_filtered\"}}, \"exp_epoch_dgs_analysis\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T19:59:57.921Z\", \"updated_at\": \"2026-05-18T20:01:46.134Z\", \"hypothesis\": \"DGS benefit is strictly monotonic with degeneracy rate: higher degeneracy → greater DGS improvement, validating that degeneracy rate is the key gating signal\", \"spec\": {\"command\": \"python3 code/epoch_dgs_analysis.py\", \"server\": \"autodl-5090\", \"data_path\": \"/root/struct_self_consist_ie/data/\", \"data_count\": \"all datasets\", \"model_name\": \"Qwen3-8B\", \"seed\": 42}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/struct_self_consist_ie/output/epoch_dgs_analysis_results.json\", \"log_path\": \"/root/struct_self_consist_ie/output/epoch_dgs_analysis_results.json\", \"completed_at\": \"2026-05-18T20:01:46.134Z\"}, \"exp_diagnostic_calibration\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T19:59:56.064Z\", \"updated_at\": \"2026-05-18T20:01:44.364Z\", \"hypothesis\": \"A 3-indicator regression model (degeneracy rate, LP-F1 correlation, LP range) can quantitatively predict the optimal LP selection delta for unseen instances\", \"spec\": {\"command\": \"python3 code/diagnostic_calibration.py\", \"server\": \"autodl-5090\", \"data_path\": \"/root/struct_self_consist_ie/data/\", \"data_count\": \"all datasets\", \"model_name\": \"Qwen3-8B\", \"seed\": 42}, \"conclusion\": \"negative\", \"checkpoint_path\": \"/root/struct_self_consist_ie/output/diagnostic_calibration_results.json\", \"log_path\": \"/root/struct_self_consist_ie/output/diagnostic_calibration_results.json\", \"completed_at\": \"2026-05-18T20:01:44.364Z\"}, \"exp_adaptive_temperature\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T19:59:52.771Z\", \"updated_at\": \"2026-05-18T20:01:42.646Z\", \"hypothesis\": \"Adjusting sampling temperature based on instance-level confidence indicators can improve output diversity-quality tradeoff\", \"spec\": {\"command\": \"python3 code/adaptive_temperature.py\", \"server\": \"autodl-5090\", \"data_path\": \"/root/struct_self_consist_ie/data/\", \"data_count\": \"all datasets\", \"model_name\": \"Qwen3-8B\", \"seed\": 42}, \"conclusion\": \"negative\", \"checkpoint_path\": \"/root/struct_self_consist_ie/output/adaptive_temperature_results.json\", \"log_path\": \"/root/struct_self_consist_ie/output/adaptive_temperature_results.json\", \"completed_at\": \"2026-05-18T20:01:42.646Z\"}, \"exp_entity_consensus\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T19:59:50.628Z\", \"updated_at\": \"2026-05-18T20:01:40.869Z\", \"hypothesis\": \"Constructing new output from N samples using entity frequency thresholds and LP-weighted decisions can capture complementary information that single-sample selection misses\", \"spec\": {\"command\": \"python3 code/entity_consensus.py\", \"server\": \"autodl-5090\", \"data_path\": \"/root/struct_self_consist_ie/data/\", \"data_count\": \"all datasets\", \"model_name\": \"Qwen3-8B\", \"seed\": 42}, \"conclusion\": \"negative\", \"checkpoint_path\": \"/root/struct_self_consist_ie/output/entity_consensus_results.json\", \"log_path\": \"/root/struct_self_consist_ie/output/entity_consensus_results.json\", \"completed_at\": \"2026-05-18T20:01:40.869Z\"}, \"exp_ccs_selection\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T19:59:48.671Z\", \"updated_at\": \"2026-05-18T20:01:39.128Z\", \"hypothesis\": \"Three-stage cascaded selection (degen→greedy, low-LP-range→entity MV, high-LP-range→LP) can outperform single-strategy selection by adapting to local confidence patterns\", \"spec\": {\"command\": \"python3 code/ccs_selection.py\", \"server\": \"autodl-5090\", \"data_path\": \"/root/struct_self_consist_ie/data/\", \"data_count\": \"all datasets\", \"model_name\": \"Qwen3-8B\", \"seed\": 42}, \"conclusion\": \"negative\", \"checkpoint_path\": \"/root/struct_self_consist_ie/output/ccs_selection_results.json\", \"log_path\": \"/root/struct_self_consist_ie/output/ccs_selection_results.json\", \"completed_at\": \"2026-05-18T20:01:39.128Z\"}, \"exp_017_llama_conll\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-14T14:39:32.014Z\", \"updated_at\": \"2026-05-18T19:11:03.240Z\", \"completed_at\": \"2026-05-14T17:12:15.687Z\", \"extra\": {\"previous_failure\": {\"conclusion\": \"success\"}}, \"hypothesis\": \"On CoNLL (high degeneracy regime), LLaMA should show the same pattern as Qwen3: LP selection fails due to narrow headroom, but structural signals retain diagnostic value (QE rho). Cross-model validation of the degeneracy-driven signal effectiveness framework.\", \"parent\": \"exp_007_llama_inference\", \"server\": \"autodl-5090\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"reproduce\": {\"server\": \"autodl-5090\", \"gpu\": \"cuda:1\", \"started_at\": \"2026-05-17T11:30:53.467Z\"}, \"metrics\": {\"degeneracy_cf1_gold_filtered\": 0.894, \"n_constant_f1\": 2465, \"n_gold_filtered\": 2756, \"n_total\": 3453, \"greedy_f1\": 0.9239, \"oracle_f1\": 0.9451, \"random_f1\": 0.9207, \"headroom_pp\": 2.11, \"dgs_f1\": 0.9254, \"dgs_delta_pp\": 0.14, \"dgs_nondegen_lp_delta_pp\": 1.37, \"selection_f1\": {\"SJ\": {\"f1\": 0.9237, \"delta_pp\": -0.04}, \"FK\": {\"f1\": 0.924, \"delta_pp\": -0.02}, \"VC\": {\"f1\": 0.925, \"delta_pp\": 0.08}, \"EM\": {\"f1\": 0.9244, \"delta_pp\": 0.02}, \"LP\": {\"f1\": 0.9244, \"delta_pp\": 0.02}}, \"qe_rho_full_3seed\": {\"SJ\": {\"mean\": 0.4631, \"sd\": 0.0074}, \"FK\": {\"mean\": 0.4546, \"sd\": 0.0061}, \"EM\": {\"mean\": 0.4603, \"sd\": 0.0078}, \"VC\": {\"mean\": 0.4579, \"sd\": 0.003}, \"LP\": {\"mean\": 0.3099, \"sd\": 0.0055}}, \"qe_auroc_full_3seed\": {\"SJ\": {\"mean\": 0.736, \"sd\": 0.0064}, \"FK\": {\"mean\": 0.732, \"sd\": 0.0063}, \"EM\": {\"mean\": 0.7355, \"sd\": 0.0069}, \"VC\": {\"mean\": 0.7394, \"sd\": 0.0041}, \"LP\": {\"mean\": 0.7629, \"sd\": 0.0044}}, \"lp_range\": {\"mean\": 0.0198, \"std\": 0.0315, \"median\": 0.0002}}, \"conclusion\": \"success\", \"spec\": {\"command\": \"python code/exp017_full_signal_analysis.py\", \"server\": \"autodl-5090\", \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_017_llama_conll_infer/samples.jsonl\", \"data_count\": 3453, \"model_name\": \"llama3.1-8b-conll2003-merged\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_017_llama_conll_infer/\", \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_017_llama_conll_infer/full_signal_analysis.json\"}}, \"exp_017_llama_conll_finetune\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T16:47:36.156Z\", \"updated_at\": \"2026-05-18T18:43:42.649Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/bin/activate && cd /root/autodl-tmp/struct_self_consist_ie && CUDA_VISIBLE_DEVICES=0 llamafactory-cli train train_config_llama_conll2003_3ep.yaml\\\"\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:0\"], \"pid\": \"674921\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_017_llama_conll_finetune.log\", \"submitted_at\": \"2026-05-18T16:47:35.786Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/data/conll2003/llmfactory_train.json\", \"data_count\": 14037, \"model_name\": \"Meta-Llama-3.1-8B-Instruct\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/checkpoints/llama3.1-8b-conll2003-lora-3ep\", \"checkpoint_source\": \"Meta-Llama-3.1-8B-Instruct (base model, LoRA from scratch)\", \"eval_data\": \"conll2003_uie_dev\", \"wall_clock_seconds\": 6176.5, \"gpu_hours\": 1.72}, \"hypothesis\": \"Structural self-consistency QE signals (SJ, FK, VC, EM) show model-agnostic diagnostic power: their Spearman rho with per-instance F1 should be comparable on LLaMA 3.1-8B as on Qwen 2.5-7B for CoNLL-2003 NER, even though degeneracy rates and absolute F1 may differ.\", \"parent\": \"exp_llama_fewnerd_lora\", \"conclusion\": \"success\", \"metrics\": {\"degeneracy_rate\": 0.853, \"greedy_f1\": 0.928, \"oracle_f1\": 0.951, \"headroom\": 0.023, \"selection_f1\": 0.934, \"full_rho_SJ\": 0.45, \"full_rho_FK\": 0.443, \"full_rho_VC\": 0.437, \"full_rho_EM\": 0.448, \"full_rho_LP\": 0.273, \"full_AUROC_SJ\": 0.752, \"full_AUROC_EM\": 0.753, \"full_AUROC_LP\": 0.739, \"cond_rho_SJ\": 0.454, \"cond_rho_EM\": 0.458, \"cond_rho_LP\": 0.311, \"cond_AUROC_EM\": 0.783, \"cond_AUROC_LP\": 0.804}, \"completed_at\": \"2026-05-18T18:30:32.331Z\"}, \"exp_028_entity_token_lp\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T18:22:18.594Z\", \"updated_at\": \"2026-05-18T18:23:06.601Z\", \"hypothesis\": \"Full-sequence mean LP underperforms as a quality signal because format/schema tokens dilute the entity-relevant logprob signal; isolating entity-only tokens should yield higher QE correlation and selection F1.\", \"conclusion\": \"negative\", \"spec\": {\"command\": \"python code/exp028_entity_token_lp_analysis.py\", \"server\": \"autodl-5090\", \"data_path\": \"output/exp_entity_token_lp/scierc/samples.jsonl\", \"data_count\": 529, \"model_name\": \"qwen3-8b-scierc-merged-v2\", \"seed\": 42, \"checkpoint_path\": \"checkpoints/qwen3-8b-scierc-merged-v2\", \"log_path\": \"output/exp_028_entity_token_lp/analysis_results.json\"}, \"completed_at\": \"2026-05-18T18:22:59.312Z\", \"metrics\": {\"greedy_f1\": 0.643, \"oracle_f1\": 0.7845, \"full_lp_global_rho\": 0.2971, \"entity_text_type_lp_global_rho\": 0.4401, \"full_lp_selection_f1\": 0.6465, \"entity_text_type_lp_selection_f1\": 0.6357, \"dilution_ratio\": 0.32, \"full_lp_within_range_median\": 0.0402, \"entity_text_type_within_range_median\": 0.1346, \"schema_only_within_range_median\": 0.0089}}, \"exp_026_t12_scierc\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T15:28:36.812Z\", \"updated_at\": \"2026-05-18T15:30:33.407Z\", \"hypothesis\": \"Higher temperature (T=1.2) reduces degeneracy rate and increases LP range on SciERC NER, but may degrade absolute generation quality\", \"spec\": {\"command\": \"python code/analyze_exp026_temp_5signal.py --data_path output/exp_026_t12/samples.jsonl --output_dir output/exp_026_t12/\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:3\"], \"pid\": \"665522\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_026_t12_scierc.log\", \"submitted_at\": \"2026-05-18T15:28:56.997Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"output/exp_026_t12/samples.jsonl\", \"data_count\": 551, \"model_name\": \"qwen3-8b-scierc-merged-v2\", \"seed\": 42, \"checkpoint_path\": \"checkpoints/qwen3-8b-scierc-merged-v2\", \"checkpoint_source\": \"ft_002_v2\", \"eval_data\": \"scierc_test_551\", \"wall_clock_seconds\": 96.4, \"gpu_hours\": 0.03}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T15:30:33.407Z\"}, \"exp_026_t08_scierc\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T15:28:36.084Z\", \"updated_at\": \"2026-05-18T15:30:31.219Z\", \"hypothesis\": \"Moderate temperature (T=0.8) provides intermediate degeneracy/LP-range tradeoff on SciERC NER, testing sensitivity of structural signals to temperature\", \"spec\": {\"command\": \"python code/analyze_exp026_temp_5signal.py --data_path output/exp_026_t08/samples.jsonl --output_dir output/exp_026_t08/\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:2\"], \"pid\": \"665386\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_026_t08_scierc.log\", \"submitted_at\": \"2026-05-18T15:28:55.394Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"output/exp_026_t08/samples.jsonl\", \"data_count\": 551, \"model_name\": \"qwen3-8b-scierc-merged-v2\", \"seed\": 42, \"checkpoint_path\": \"checkpoints/qwen3-8b-scierc-merged-v2\", \"checkpoint_source\": \"ft_002_v2\", \"eval_data\": \"scierc_test_551\", \"wall_clock_seconds\": 95.8, \"gpu_hours\": 0.03}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T15:30:31.219Z\"}, \"exp_026_t05_scierc\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T15:28:34.135Z\", \"updated_at\": \"2026-05-18T15:30:28.965Z\", \"hypothesis\": \"Lower temperature (T=0.5) increases degeneracy rate and reduces LP range on SciERC NER, as reduced sampling diversity causes more identical outputs\", \"spec\": {\"command\": \"python code/analyze_exp026_temp_5signal.py --data_path output/exp_026_t05/samples.jsonl --output_dir output/exp_026_t05/\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:0\"], \"pid\": \"665248\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_026_t05_scierc.log\", \"submitted_at\": \"2026-05-18T15:28:53.787Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"output/exp_026_t05/samples.jsonl\", \"data_count\": 551, \"model_name\": \"qwen3-8b-scierc-merged-v2\", \"seed\": 42, \"checkpoint_path\": \"checkpoints/qwen3-8b-scierc-merged-v2\", \"checkpoint_source\": \"ft_002_v2\", \"eval_data\": \"scierc_test_551\", \"wall_clock_seconds\": 95.2, \"gpu_hours\": 0.03}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T15:30:28.965Z\"}, \"exp_027_mlp_verifier\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T06:39:22.524Z\", \"updated_at\": \"2026-05-18T06:41:51.069Z\", \"metrics\": {\"lr_auroc\": 0.6522, \"mlp_auroc\": 0.6381, \"rf_auroc\": 0.5868, \"mlp_15feat_auroc\": 0.6341, \"lr_sel_f1\": 0.6406, \"mlp_sel_f1\": 0.6278, \"greedy_f1\": 0.6441, \"oracle_f1\": 0.8231, \"best_single_signal_auroc\": 0.6476, \"feature_bottleneck_confirmed\": true}, \"hypothesis\": \"MLP/RF等非线性模型能否通过组合5个QE信号(LP,SJ,FK,EM,VC)超越LR，或通过cross-signal interactions提取额外信息，从而缩小selection gap\", \"spec\": {\"command\": \"python train_mlp_verifier.py --n_samples 16 --cv_folds 5 --seeds 42,123,456\", \"server\": \"a100\", \"data_path\": \"output/exp_001_n16_seed*/samples.jsonl\", \"data_count\": 529, \"model_name\": \"sklearn LR/MLP/RF\", \"seed\": \"42,123,456\", \"checkpoint_path\": \"N/A\", \"log_path\": \"output/exp_027_mlp_verifier/\"}, \"conclusion\": \"negative\", \"completed_at\": \"2026-05-18T06:41:51.069Z\"}, \"exp_028_fewnerd_5epoch\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T07:53:12.913Z\", \"updated_at\": \"2026-05-17T20:29:42.274Z\", \"spec\": {\"hypothesis\": \"Few-NERD low degeneracy (10%) partially due to under-convergence at 3 epochs. 5 epochs should increase degeneracy as model becomes more confident, potentially reducing LP selection gain.\", \"parent\": \"exp_021_fewnerd_full\", \"command\": \"bash -c \\\"source /root/miniconda3/bin/activate && cd /root/autodl-tmp/struct_self_consist_ie && CUDA_VISIBLE_DEVICES=0,1,2,3 llamafactory-cli train train_config_fewnerd_5epoch_4gpu.yaml 2>&1 | tee logs/exp_028_4gpu_train.log\\\"\", \"server\": \"autodl-5090\", \"gpu\": \"cuda:0,1,2,3\", \"data_path\": \"data/fewnerd_uie_train\", \"data_count\": 131767, \"model_name\": \"Qwen3-8B LoRA rank=32\", \"seed\": 42, \"log_path\": \"logs/exp_028_4gpu_train.log\", \"checkpoint_path\": \"checkpoints/qwen3-8b-fewnerd-5epoch-lora\"}, \"conclusion\": \"negative\", \"metrics\": {\"degeneracy_cf1_gold\": 0.3133, \"greedy_f1\": 0.7773, \"lp_sel_delta_pp\": 0.624, \"lp_sel_f1\": 0.7835, \"oracle_f1\": 0.8723, \"within_instance_rho_mean\": 0.4066, \"within_instance_rho_median\": 0.6151}, \"hypothesis\": \"Few-NERD low degeneracy (10%) partially due to under-convergence at 3 epochs. 5 epochs should increase degeneracy as model becomes more confident, potentially reducing LP selection gain.\", \"completed_at\": \"2026-05-17T20:29:42.274Z\"}, \"exp_028\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-17T07:35:39.447Z\", \"updated_at\": \"2026-05-17T20:26:59.399Z\", \"hypothesis\": \"Few-NERD low degeneracy (10%) in exp-021 is NOT due to under-convergence at 3 epochs; training for 5 epochs will show similar degeneracy levels, confirming the structural property of this dataset rather than an artifact of insufficient training.\", \"failure_reason\": \"startup recovery: RUNNING with no cron and no server/pid info\", \"completed_at\": \"2026-05-17T12:09:43.334Z\", \"extra\": {\"previous_failure\": {\"conclusion\": \"failed\"}, \"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-17T20:06:01.040147+00:00\"}]}, \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/bin/activate && cd /root/autodl-tmp/struct_self_consist_ie && CUDA_VISIBLE_DEVICES=0,1,2,3 llamafactory-cli train train_config_fewnerd_5epoch_4gpu.yaml 2>&1 | tee logs/exp_028_4gpu_train.log\\\"\", \"server\": \"autodl-5090\", \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/data/fewnerd_uie_train\", \"data_count\": 131767, \"model_name\": \"Qwen3-8B LoRA rank=32\", \"seed\": 42, \"checkpoint_path\": \"checkpoints/qwen3-8b-fewnerd-5epoch-lora\", \"log_path\": \"logs/exp_028_4gpu_train.log\"}, \"reproduce\": {\"finished_at\": \"2026-05-17T20:05:57.260Z\"}, \"conclusion\": \"negative\", \"metrics\": {\"degeneracy_cf1_gold\": 0.313, \"greedy_f1\": 0.7773, \"lp_sel_f1\": 0.7835, \"lp_sel_delta_pp\": 0.62, \"oracle_f1\": 0.8723, \"within_instance_rho\": 0.4066, \"train_loss\": 0.0189, \"eval_loss\": 0.0311}}, \"exp_024_claim_audit\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T10:54:36.291Z\", \"updated_at\": \"2026-05-17T10:55:08.244Z\", \"hypothesis\": \"Systematic cross-chapter numerical consistency audit: verify all quantitative claims in paper against source experiment data, catch stale values and cross-reference errors before submission.\", \"conclusion\": \"success\", \"metrics\": {\"consistent\": 97, \"errors\": 1, \"warnings\": 5, \"old_residuals_found\": 0}, \"spec\": {\"checkpoint_path\": \"artifacts/exp_024_claim_audit/audit_report.md\", \"log_path\": \"N/A\", \"command\": \"CPU-only paper audit\", \"server\": \"local\", \"data_path\": \"docs/paper/\", \"data_count\": 0, \"model_name\": \"N/A\", \"seed\": 0}, \"completed_at\": \"2026-05-17T10:55:08.244Z\"}, \"exp_016_rerun_1024_bootstrap\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T23:44:21.577Z\", \"updated_at\": \"2026-05-17T03:33:39.786Z\", \"hypothesis\": \"3-seed bootstrap significance test for NER logprob vs greedy selection gap (+0.6pp). Tests whether the observed advantage is statistically significant.\", \"spec\": {\"command\": \"python code/bootstrap_significance.py\", \"server\": \"local\", \"data_path\": \"output/exp_016_rerun_1024/\", \"data_count\": 529, \"model_name\": \"N/A (statistical analysis)\", \"seed\": \"3-seed bootstrap (1000 iterations)\", \"checkpoint_path\": \"N/A\", \"log_path\": \"output/exp_016_rerun_1024_bootstrap/\"}, \"conclusion\": \"negative\", \"metrics\": {\"bootstrap_ci_95\": [-0.03, 0.042], \"permutation_p\": 0.39, \"cohen_d\": 0.038, \"sign_test_win_rate\": 0.466, \"ner_logprob_vs_greedy_delta\": 0.006, \"conclusion_summary\": \"NER selection: no signal significantly outperforms greedy; RE: same conclusion\"}, \"completed_at\": \"2026-05-14T23:44:48.818Z\", \"parent\": \"exp_016_rerun_1024\"}, \"exp_verbalized_confidence\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T02:45:20.552Z\", \"updated_at\": \"2026-05-17T03:33:39.197Z\", \"hypothesis\": \"Verbalized confidence baseline: let model self-rate extraction confidence. If also compressed → strengthens \\\"score compression is general\\\" claim. If effective → important positive finding requiring narrative adjustment.\", \"conclusion\": \"negative\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 python code/run_verbalized_confidence.py\", \"server\": \"autodl-5090\", \"data_path\": \"output/exp_012_rerun_1024/samples.jsonl + output/exp002_conll2003/samples.jsonl\", \"data_count\": 3285, \"model_name\": \"qwen3-8b-scierc-merged-v2 + qwen3-8b-conll2003-merged\", \"seed\": 42, \"checkpoint_path\": \"output/review_round9_experiments/verbalized_confidence/\", \"log_path\": \"output/review_round9_experiments/verbalized_confidence_run.log\"}, \"completed_at\": \"2026-05-16T03:09:39.916Z\", \"metrics\": {\"scierc\": {\"VerbConf_rho\": 0.2965, \"VerbConf_auroc\": 0.6811, \"VerbConf_sel_f1\": 0.6195, \"VerbConf_delta\": -0.0245, \"best_existing_rho\": 0.3792, \"VerbConf_mean\": 8.58, \"VerbConf_std\": 1.15, \"parse_fail_rate\": 0.0026}, \"conll\": {\"VerbConf_rho\": 0.3366, \"VerbConf_auroc\": 0.7469, \"VerbConf_sel_f1\": 0.8886, \"VerbConf_delta\": -0.0193, \"best_existing_rho\": 0.4507, \"VerbConf_mean\": 9.24, \"VerbConf_std\": 1.32, \"parse_fail_rate\": 0}}, \"parent\": \"exp_012_rerun_1024\"}, \"exp_entity_token_lp\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T05:39:44.631Z\", \"updated_at\": \"2026-05-17T03:33:38.371Z\", \"hypothesis\": \"Entity-token LP: test Discussion hypothesis (d) format-token dilution. Re-inference with per-token logprobs, then compute entity-only LP variance and selection F1. If entity-token LP compression is reduced → pilot remedy for LP selection. Also includes LP z-score normalization as zero-cost baseline. Addresses SF2+SF3 from Round 12.\", \"server\": \"autodl-5090\", \"gpu\": \"cuda:0,cuda:1\", \"account\": \"root\", \"reproduce\": {\"server\": \"autodl-5090\", \"gpu\": \"cuda:0,cuda:1\", \"started_at\": \"2026-05-16T05:41:33.768Z\"}, \"conclusion\": \"negative\", \"metrics\": {\"scierc_ner\": {\"greedy_f1\": 0.643, \"full_lp_sel_f1\": 0.6465, \"entity_lp_sel_f1\": 0.6262, \"oracle_f1\": 0.7845, \"entity_lp_delta_vs_full_lp\": -0.0203}, \"conll_ner\": {\"greedy_f1\": 0.9065, \"full_lp_sel_f1\": 0.8989, \"entity_lp_sel_f1\": 0.8659, \"oracle_f1\": 0.948, \"entity_lp_delta_vs_full_lp\": -0.033}, \"finding\": \"entity-token LP strictly worse than full-sequence LP; CoNLL entity tokens saturated (79.4% tied), SciERC entity tokens too sparse (5.3% of total)\"}, \"spec\": {\"command\": \"python analyze_entity_token_lp.py\", \"server\": \"autodl-5090\", \"data_path\": \"output/exp_012_rerun_1024/ + output/exp_002_conll_rerun_1024/\", \"data_count\": \"529 (SciERC NER) + 2756 (CoNLL NER)\", \"model_name\": \"Qwen3-8B (finetuned)\", \"seed\": 42, \"checkpoint_path\": \"artifacts/exp_entity_token_lp/results.json\", \"log_path\": \"artifacts/exp_entity_token_lp/report.md\"}, \"completed_at\": \"2026-05-16T06:28:46.845Z\", \"parent\": \"exp_012_rerun_1024\"}, \"exp_freeform_ablation\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T09:42:22.868Z\", \"updated_at\": \"2026-05-17T03:33:37.623Z\", \"spec\": {\"command\": \"python run_freeform_inference.py --seed 42 --num_samples 8 --temperature 1.0 --max_tokens 1024 --output_dir results/exp_freeform_ablation\", \"server\": \"autodl-5090\", \"gpu\": \"cuda:0\", \"pid\": \"169042\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_freeform_ablation.log\", \"submitted_at\": \"2026-05-15T09:42:30.236Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"hypothesis\": \"Free-form decoding recovers logprob variance and selection ability lost under constrained decoding\", \"plan_id\": \"exp-018\", \"data_path\": \"data/scierc/processed_data\", \"data_count\": 551, \"model_name\": \"qwen3-8b-scierc-merged-v2\", \"seed\": 42, \"tmux_session\": \"exp_freeform_ablation\", \"wall_clock_seconds\": 1059.0, \"gpu_hours\": 0.29}, \"conclusion\": \"negative\", \"metrics\": {\"lp_std_ratio_free_vs_constrained\": 0.97, \"lp_range_ratio\": 0.96, \"tied_fraction_constrained\": 0.597, \"tied_fraction_freeform\": 0.577, \"ner_selection_gap_constrained\": 0.0059, \"ner_selection_gap_freeform\": 0.0018, \"re_selection_gap_constrained\": -0.0068, \"re_selection_gap_freeform\": 0.0169, \"parse_rate\": 0.9995, \"ner_vc_rho_constrained\": 0.3792, \"ner_vc_rho_freeform\": 0.4089}, \"checkpoint_path\": \"N/A (inference-only experiment)\", \"completed_at\": \"2026-05-15T10:00:09.238Z\", \"hypothesis\": \"Free-form vs constrained decoding ablation on SciERC: test if removing JSON schema constraint changes LP variance distribution. If LP remains compressed under free-form, confirms compression is model-intrinsic not format-artifact.\", \"parent\": \"exp_012_rerun_1024\"}, \"exp_008_re_n16\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T12:03:06.876Z\", \"updated_at\": \"2026-05-17T02:58:19.490Z\", \"spec\": {\"hypothesis\": \"RE N=16 confirms negative finding with higher statistical power. If rho still <0.30, task-complexity boundary is robust.\", \"plan_id\": \"exp-008\", \"model_name\": \"qwen3-8b-scierc-merged-v2\", \"dataset\": \"SciERC\", \"gpu\": \"cuda:2\", \"server\": \"gpu-5090-4x-2\", \"gpu_budget_hours\": 12, \"description\": \"RE N=16 on SciERC to confirm negative finding. Inference with log-prob capture.\", \"priority\": \"P1\", \"command\": \"python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc/processed_data --dataset scierc --subtask joint --n_samples 16 --temperature 1.0 --seed 42 --collect_logprobs\", \"data_path\": \"data/scierc/processed_data\", \"data_count\": 551, \"seed\": 42, \"num_instances\": 200, \"partial\": true, \"note\": \"Only 200/551 instances due to --num_test default bug. Needs full rerun.\"}, \"metrics\": {\"ner\": {\"greedy_f1\": 0.6635, \"oracle_f1\": 0.8208, \"headroom\": 0.1572, \"rho_sj_full\": 0.377, \"rho_fk_full\": 0.2508, \"rho_logprob_full\": 0.3153, \"rho_sj_cond\": 0.3598, \"rho_fk_cond\": 0.2251, \"rho_logprob_cond\": 0.2927, \"sj_beats_fk\": true, \"rho_advantage\": 0.1262}, \"re\": {\"greedy_f1\": 0.4339, \"oracle_f1\": 0.6658, \"headroom\": 0.2319, \"rho_sj_full\": 0.2966, \"rho_fk_full\": 0.2871, \"rho_logprob_full\": 0.2986, \"rho_sj_cond\": 0.3975, \"rho_fk_cond\": 0.3774, \"rho_logprob_cond\": 0.2745, \"sj_beats_fk\": true, \"rho_advantage\": 0.0095}, \"verdict\": \"FAIL\"}, \"conclusion\": \"success\", \"checkpoint_path\": \"N/A\", \"log_path\": \"output/exp008_re_n16/\", \"completed_at\": \"2026-05-14T12:28:39.268Z\", \"hypothesis\": \"RE N=16 initial evaluation: first relation extraction test with structural signals. Establishes baseline RE signal effectiveness before pipeline corrections.\"}, \"exp_001_ner_n16_seed123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T12:46:06.430Z\", \"updated_at\": \"2026-05-17T02:58:18.225Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && CUDA_VISIBLE_DEVICES=3 python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc/processed_data --dataset scierc --subtask joint --n_samples 16 --temperature 1.0 --seed 123 --output_dir output/exp001_n16_seed123 --num_test 9999 --collect_logprobs 2>&1 | tee output/exp001_n16_seed123_run.log\\\"\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:3\"], \"pid\": \"63407\", \"log_path\": \"output/exp001_n16_seed123_run.log\", \"submitted_at\": \"2026-05-14T12:46:06.234Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_count\": 551, \"data_path\": \"data/scierc/processed_data\", \"model_name\": \"qwen3-8b-scierc-merged-v2\", \"seed\": 123, \"checkpoint_path\": \"output/exp001_n16_seed123/\", \"wall_clock_seconds\": 2748.0, \"gpu_hours\": 0.76}, \"conclusion\": \"success\", \"metrics\": {\"ner\": {\"greedy_f1\": 0.663, \"oracle_f1\": 0.809, \"headroom\": 0.146, \"rho_sj\": 0.423, \"rho_fk\": 0.29, \"rho_logprob\": 0.239, \"rho_sj_cond\": 0.423, \"rho_fk_cond\": 0.26}, \"re\": {\"greedy_f1\": 0.419, \"oracle_f1\": 0.625, \"headroom\": 0.206, \"rho_sj\": 0.267, \"rho_fk\": 0.315, \"rho_sj_cond\": 0.364, \"rho_fk_cond\": 0.331}, \"verdict\": \"FAIL\", \"verdict_note\": \"RE rho_sj=0.267 < 0.40; RE >30% samples F1=0\", \"n_instances\": 551, \"seed\": 123, \"N\": 16, \"T\": 1}, \"completed_at\": \"2026-05-14T13:31:54.232Z\", \"hypothesis\": \"SciERC NER N=16 seed=123: multi-seed validation at N=16. Tests seed stability for signal rankings with more samples.\"}, \"exp_007_ner_multi_model\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T11:42:20.748Z\", \"updated_at\": \"2026-05-17T02:58:16.747Z\", \"spec\": {\"command\": \"bash -c 'source env.sh && cd /root/autodl-tmp/struct_self_consist_ie && llamafactory-cli train train_config_llama.yaml'\", \"server\": \"gpu-5090-4x-2\", \"gpu\": [\"cuda:0\"], \"pid\": \"60970\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_007_ner_multi_model.log\", \"submitted_at\": \"2026-05-14T12:43:09.108Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/data\", \"data_count\": 1861, \"model_name\": \"LLaMA-3.1-8B-Instruct\", \"seed\": 42, \"log_file\": \"~/runs/struct_self_consist_ie/exp_007_ner_multi_model.log\", \"wall_clock_seconds\": 165.8, \"gpu_hours\": 0.05}, \"server\": \"autodl-5090\", \"gpu\": \"cuda:3\", \"account\": \"root\", \"reproduce\": {\"server\": \"autodl-5090\", \"gpu\": \"cuda:3\", \"started_at\": \"2026-05-14T11:43:50.977Z\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T12:45:54.952Z\", \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/checkpoints/llama3.1-8b-scierc-lora\", \"metrics\": {\"epoch\": 5, \"train_loss\": 0.0767, \"eval_loss\": 0.1049, \"train_runtime_sec\": 1494.5, \"train_samples_per_second\": 6.226, \"checkpoints\": [\"checkpoint-400\", \"checkpoint-500\", \"checkpoint-585\"], \"base_model\": \"Meta-Llama-3.1-8B-Instruct\", \"lora_r\": 32, \"lora_alpha\": 64, \"note\": \"EXIT_CODE=129 (SIGHUP) but training completed all 5 epochs before signal. Checkpoint fully intact.\"}, \"log_path\": \"~/runs/struct_self_consist_ie/exp_007_ner_multi_model.log\", \"hypothesis\": \"Multi-model NER comparison: evaluates signal effectiveness across Qwen and LLaMA on SciERC NER. Establishes cross-model generalization of structural>surface ranking.\"}, \"exp_003_ner_wnut17\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T11:42:17.544Z\", \"updated_at\": \"2026-05-17T02:58:14.928Z\", \"spec\": {\"merged_model_path\": \"/root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen3-8b-wnut17-merged\", \"pilot_command\": \"CUDA_VISIBLE_DEVICES=1 python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-wnut17-merged --data_dir data/wnut17 --dataset wnut17 --subtask ner --n_samples 16 --temperature 1.0 --seed 42 --output_dir output/exp003_wnut17_pilot --num_test 9999 --collect_logprobs\", \"pilot_pid\": 71498, \"pilot_server\": \"autodl-5090\", \"pilot_started_at\": \"2026-05-14T21:36:00Z\", \"test_samples\": 1287}, \"server\": \"autodl-5090\", \"gpu\": \"cuda:2\", \"account\": \"root\", \"reproduce\": {\"server\": \"autodl-5090\", \"gpu\": \"cuda:2\", \"started_at\": \"2026-05-14T11:43:50.537Z\", \"finished_at\": \"2026-05-14T12:53:13.262Z\", \"training_hours\": 1.16}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T12:53:14.768981+00:00\"}]}, \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen3-8b-wnut17-merged\", \"metrics\": {\"ner\": {\"greedy_f1\": 0.525, \"oracle_f1\": 0.664, \"headroom\": 0.139, \"rho_sj_full\": 0.082, \"rho_fk_full\": 0.124, \"rho_logprob_full\": -0.414, \"rho_sj_cond\": 0.275, \"rho_fk_cond\": 0.164, \"rho_logprob_cond\": 0.352, \"sj_beats_logprob_cond\": false}, \"n_instances\": 1287, \"n_gold_empty\": 598, \"sample_f1_mean\": 0.401, \"sample_f1_pct_zero\": 53.7, \"N\": 16, \"T\": 1, \"seed\": 42, \"verdict\": \"FAIL\", \"verdict_note\": \">30% samples F1=0; structural rho weak; logprob baseline stronger\"}, \"conclusion\": \"negative\", \"log_path\": \"output/exp003_wnut17_pilot/\", \"completed_at\": \"2026-05-14T13:40:20.979Z\", \"hypothesis\": \"WNUT-17 NER fine-tune + inference: initial attempt on social media domain. Tests if structural signals work when model capability is low on noisy text with novel entity types.\"}, \"exp_001_seed456_t10_full\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T13:27:41.067Z\", \"updated_at\": \"2026-05-17T02:58:12.996Z\", \"spec\": {\"command\": \"python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --dataset scierc --subtask joint --n_samples 16 --temperature 1.0 --seed 456 --num_test 9999 --collect_logprobs\", \"server\": \"autodl-5090\", \"data_path\": \"data/scierc/processed_data\", \"data_count\": 551, \"model_name\": \"qwen3-8b-scierc-merged-v2\", \"seed\": 456}, \"reproduce\": {\"finished_at\": \"2026-05-14T13:44:05.416Z\"}, \"failure_reason\": \"\", \"conclusion\": \"negative\", \"completed_at\": \"2026-05-14T13:44:05.021Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-14T13:44:10.317185+00:00\"}]}, \"metrics\": {\"ner\": {\"rho_sj\": 0.414, \"rho_fk\": 0.298}, \"re\": {\"rho_sj\": 0.268, \"rho_fk\": 0.26}, \"n_instances\": 551, \"N\": 16, \"T\": 1, \"seed\": 456, \"source\": \"reviewer_verified_report_json\"}, \"hypothesis\": \"SciERC NER seed=456 T=1.0 full: early multi-seed NER test before pipeline corrections. Preliminary evidence for seed stability.\"}, \"exp_001_seed123_t10_full\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T13:27:42.503Z\", \"updated_at\": \"2026-05-17T02:58:11.623Z\", \"spec\": {\"command\": \"python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --dataset scierc --subtask joint --n_samples 16 --temperature 1.0 --seed 123 --num_test 9999 --collect_logprobs\", \"server\": \"autodl-5090\", \"data_path\": \"data/scierc/processed_data\", \"data_count\": 551, \"model_name\": \"qwen3-8b-scierc-merged-v2\", \"seed\": 123}, \"reproduce\": {\"finished_at\": \"2026-05-14T13:44:13.823Z\"}, \"failure_reason\": \"\", \"conclusion\": \"negative\", \"completed_at\": \"2026-05-14T13:44:13.213Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-14T13:44:16.532801+00:00\"}]}, \"metrics\": {\"ner\": {\"rho_sj\": 0.417, \"rho_fk\": 0.283}, \"re\": {\"rho_sj\": 0.265, \"rho_fk\": 0.315}, \"n_instances\": 551, \"N\": 16, \"T\": 1, \"seed\": 123, \"source\": \"reviewer_verified_report_json\"}, \"hypothesis\": \"SciERC NER seed=123 T=1.0 full: early multi-seed NER test before pipeline corrections. Preliminary evidence for seed stability.\"}, \"exp_008_re_n16_t10_full\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T13:27:42.867Z\", \"updated_at\": \"2026-05-17T02:58:10.171Z\", \"spec\": {\"command\": \"python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --dataset scierc --subtask joint --n_samples 16 --temperature 1.0 --seed 42 --num_test 9999 --collect_logprobs\", \"server\": \"autodl-5090\", \"data_path\": \"data/scierc/processed_data\", \"data_count\": 551, \"model_name\": \"qwen3-8b-scierc-merged-v2\", \"seed\": 42}, \"reproduce\": {\"finished_at\": \"2026-05-14T13:44:18.988Z\"}, \"failure_reason\": \"\", \"conclusion\": \"negative\", \"completed_at\": \"2026-05-14T13:44:19.577Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-14T13:44:21.528032+00:00\"}]}, \"metrics\": {\"ner\": {\"rho_sj\": 0.444}, \"re\": {\"rho_sj\": 0.248}, \"n_instances\": 551, \"N\": 16, \"T\": 1, \"seed\": 42, \"mode\": \"RE-only\", \"source\": \"director_corrected\"}, \"hypothesis\": \"RE N=16 T=1.0 full dataset: early RE evaluation attempt. Tests structural signals on relation extraction before pipeline corrections.\"}, \"exp_007_llama_inference\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T13:54:48.055Z\", \"updated_at\": \"2026-05-17T02:58:03.014Z\", \"spec\": {\"command\": \"python run_mvp_pilot.py --model_path checkpoints/llama3.1-8b-scierc-merged --data_dir data/scierc/processed_data --dataset scierc --subtask joint --n_samples 8 --temperature 1.0 --seed 42 --num_test 9999 --collect_logprobs --output_dir output/exp007_llama_inference/\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:0\"], \"pid\": \"75172\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_007_llama_inference.log\", \"submitted_at\": \"2026-05-14T13:54:47.962Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/scierc/processed_data\", \"data_count\": 551, \"model_name\": \"Meta-Llama-3.1-8B-Instruct (LoRA fine-tuned on SciERC)\", \"seed\": 42, \"checkpoint_source\": \"checkpoints/llama3.1-8b-scierc-merged\", \"description\": \"LLaMA-3.1-8B SciERC joint inference (NER+RE) with 8 samples, T=1.0, logprobs collected.\", \"wall_clock_seconds\": 1038.5, \"gpu_hours\": 0.29}, \"log_path\": \"output/exp007_llama_inference/\", \"checkpoint_path\": \"N/A\", \"metrics\": {\"ner\": {\"greedy_f1\": 0.66, \"oracle_f1\": 0.781, \"headroom\": 0.121, \"rho_fk\": 0.327, \"rho_sj\": 0.363, \"rho_fk_cond\": 0.226, \"rho_sj_cond\": 0.311, \"rho_logprob\": 0.183, \"rho_logprob_cond\": 0.109, \"structural_beats_surface\": true, \"sample_f1_pct_zero\": 11.6}, \"re\": {\"greedy_f1\": 0.434, \"oracle_f1\": 0.568, \"headroom\": 0.135, \"rho_fk\": 0.305, \"rho_sj\": 0.299, \"rho_fk_cond\": 0.259, \"rho_sj_cond\": 0.405, \"rho_logprob\": 0.288, \"rho_logprob_cond\": 0.092, \"structural_beats_surface\": false, \"sample_f1_pct_zero\": 41.2}, \"n_instances\": 551, \"N\": 8, \"T\": 1, \"seed\": 42, \"model\": \"LLaMA-3.1-8B-Instruct\", \"verdict\": \"FAIL\", \"verdict_note\": \"RE rho_sj_full=0.299 < 0.40; >30% RE samples F1=0\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T14:12:06.442Z\", \"hypothesis\": \"LLaMA SciERC N=8 baseline: first cross-model test. Verifies structural signal effectiveness generalizes from Qwen to LLaMA model family on SciERC NER.\"}, \"exp_003_wnut17_eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T13:47:34.654Z\", \"updated_at\": \"2026-05-17T02:58:01.627Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-wnut17-merged --data_dir data/wnut17 --dataset wnut17 --subtask ner --n_samples 16 --temperature 1.0 --seed 42 --output_dir output/exp003_wnut17_eval --num_test 9999 --collect_logprobs\", \"server\": \"autodl-5090\", \"data_path\": \"data/wnut17\", \"data_count\": 1287, \"model_name\": \"qwen3-8b-wnut17-merged\", \"seed\": 42}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T14:08:17.429Z\", \"metrics\": {\"greedy_f1\": 0.523, \"oracle_f1\": 0.664, \"headroom\": 0.141, \"rho_fk\": 0.125, \"rho_sj\": 0.089, \"rho_fk_cond\": 0.169, \"rho_sj_cond\": 0.288, \"rho_logprob_full\": -0.409, \"rho_logprob_cond\": 0.35, \"structural_beats_surface\": false, \"sample_f1_pct_zero\": 53.7, \"n_instances\": 1287, \"N\": 16, \"T\": 1, \"seed\": 42, \"model\": \"Qwen3-8B\", \"n_gold_empty_filtered\": 598, \"verdict\": \"FAIL\", \"verdict_note\": \"structural_beats_surface=false; >50% samples F1=0\"}, \"hypothesis\": \"WNUT-17 NER evaluation: initial test on noisy social media domain. Tests boundary conditions for structural signal effectiveness on out-of-domain text.\"}, \"exp_010_selection_curves\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T15:01:53.585Z\", \"updated_at\": \"2026-05-17T02:58:00.378Z\", \"spec\": {\"command\": \"python3 code/exp010_selection_curves.py\", \"server\": \"autodl-5090\", \"data_path\": \"output/exp_001_seed42_v2, output/exp_008_re_n16_v2, output/exp002_conll2003\", \"data_count\": \"551+397+3453 instances\", \"model_name\": \"qwen3-8b-scierc-merged-v2\", \"seed\": 42, \"description\": \"Best-of-N selection curves: F1 vs N for 7 signals across 3 datasets\"}, \"conclusion\": \"success\", \"checkpoint_path\": \"N/A (analysis only)\", \"log_path\": \"/tmp/exp010.log\", \"completed_at\": \"2026-05-14T15:02:22.638Z\", \"metrics\": {\"scierc_ner\": {\"n_instances\": 551, \"greedy_f1\": 0.618, \"N16\": {\"oracle\": 0.787, \"SJ\": 0.62, \"FK\": 0.621, \"logprob\": 0.621, \"voting_conf\": 0.585, \"EM\": 0.606, \"random\": 0.595}, \"N8\": {\"oracle\": 0.752, \"SJ\": 0.614, \"FK\": 0.614, \"logprob\": 0.619, \"voting_conf\": 0.591, \"EM\": 0.603, \"random\": 0.589}, \"N4\": {\"oracle\": 0.714, \"SJ\": 0.607, \"FK\": 0.608, \"logprob\": 0.616, \"voting_conf\": 0.594, \"EM\": 0.6, \"random\": 0.587}}, \"scierc_re\": {\"n_instances\": 397, \"greedy_f1\": 0.403, \"N16\": {\"oracle\": 0.631, \"SJ\": 0.397, \"FK\": 0.396, \"logprob\": 0.41, \"voting_conf\": 0.408, \"EM\": 0.381, \"random\": 0.364}, \"N8\": {\"oracle\": 0.583, \"SJ\": 0.393, \"FK\": 0.394, \"logprob\": 0.413, \"voting_conf\": 0.398, \"EM\": 0.381, \"random\": 0.363}}, \"conll_ner\": {\"n_instances\": 3453, \"greedy_f1\": 0.725, \"N8\": {\"oracle\": 0.757, \"SJ\": 0.718, \"FK\": 0.717, \"logprob\": 0.716, \"voting_conf\": 0.714, \"EM\": 0.716, \"random\": 0.69}, \"N4\": {\"oracle\": 0.746, \"SJ\": 0.714, \"FK\": 0.714, \"logprob\": 0.715, \"voting_conf\": 0.714, \"EM\": 0.712, \"random\": 0.692}}}, \"hypothesis\": \"Selection curve analysis: plots selection F1 vs confidence threshold for each signal. Visualizes where correlation-selection gap emerges and at what confidence level signals become useful for filtering.\"}, \"exp_007_llama_seed456\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T15:08:50.628Z\", \"updated_at\": \"2026-05-17T02:57:59.595Z\", \"spec\": {\"description\": \"LLaMA 3.1-8B SciERC joint extraction, seed=456, cross-model robustness test\", \"hypothesis\": \"Structural consistency generalizes across model architectures (LLaMA vs Qwen)\", \"command\": \"CUDA_VISIBLE_DEVICES=2 PYTHONPATH=code python code/run_mvp_pilot.py --model_path checkpoints/llama3.1-8b-scierc-merged --data_dir data/scierc/processed_data --dataset scierc --subtask joint --n_samples 8 --temperature 1.0 --seed 456 --num_test 9999 --collect_logprobs --output_dir output/exp_007_llama_seed456\", \"server\": \"bjb1-21071\", \"data_path\": \"data/scierc/processed_data\", \"data_count\": 551, \"model_name\": \"llama3.1-8b-scierc-merged\", \"seed\": 456, \"gpu\": [\"cuda:2\"], \"backend\": \"tmux\", \"tmux_session\": \"exp007_s456\", \"account\": \"root\", \"log_path\": \"output/exp_007_llama_seed456/run.log\"}, \"conclusion\": \"negative\", \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_007_llama_seed456/run.log\", \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_007_llama_seed456/\", \"completed_at\": \"2026-05-14T15:19:20.693Z\", \"metrics\": {\"verdict\": \"FAIL\", \"ner\": {\"greedy_f1\": 0.6597, \"oracle_f1\": 0.7575, \"oracle_headroom\": 0.0978, \"fleiss_kappa\": 0.4543, \"soft_jaccard\": 0.7491, \"rho_kappa_f1\": 0.3115, \"rho_sj_f1\": 0.3663, \"structural_gt_surface\": true}, \"re\": {\"greedy_f1\": 0.4334, \"oracle_f1\": 0.5789, \"oracle_headroom\": 0.1455, \"fleiss_kappa\": 0.3791, \"soft_jaccard\": 0.6782, \"rho_kappa_f1\": 0.3013, \"rho_sj_f1\": 0.287, \"structural_gt_surface\": false}, \"logprob_ner\": {\"rho\": 0.1911, \"auroc\": 0.5989}, \"logprob_re\": {\"rho\": 0.3246, \"auroc\": 0.6678}, \"fail_reason\": \"RE rho_sj=0.2870 < 0.40 threshold; >30% samples F1=0\"}, \"hypothesis\": \"LLaMA SciERC seed=456: early cross-model multi-seed test. Verifies LLaMA NER signal pattern is reproducible across sampling seeds.\"}, \"exp_007_llama_seed123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T15:08:50.157Z\", \"updated_at\": \"2026-05-17T02:57:58.879Z\", \"spec\": {\"description\": \"LLaMA 3.1-8B SciERC joint extraction, seed=123, cross-model robustness test\", \"hypothesis\": \"Structural consistency generalizes across model architectures (LLaMA vs Qwen)\", \"command\": \"CUDA_VISIBLE_DEVICES=1 PYTHONPATH=code python code/run_mvp_pilot.py --model_path checkpoints/llama3.1-8b-scierc-merged --data_dir data/scierc/processed_data --dataset scierc --subtask joint --n_samples 8 --temperature 1.0 --seed 123 --num_test 9999 --collect_logprobs --output_dir output/exp_007_llama_seed123\", \"server\": \"bjb1-21071\", \"data_path\": \"data/scierc/processed_data\", \"data_count\": 551, \"model_name\": \"llama3.1-8b-scierc-merged\", \"seed\": 123, \"gpu\": [\"cuda:1\"], \"backend\": \"tmux\", \"tmux_session\": \"exp007_s123\", \"account\": \"root\", \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_007_llama_seed123/run.log\", \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_007_llama_seed123/\"}, \"conclusion\": \"negative\", \"completed_at\": \"2026-05-14T15:19:43.424Z\", \"metrics\": {\"verdict\": \"FAIL\", \"ner\": {\"greedy_f1\": 0.6605, \"oracle_f1\": 0.7703, \"headroom\": 0.1098, \"fleiss_kappa\": 0.4553, \"soft_jaccard\": 0.7525, \"rho_kappa_f1\": 0.2143, \"rho_sj_f1\": 0.3371, \"structural_gt_surface\": true}, \"re\": {\"greedy_f1\": 0.433, \"oracle_f1\": 0.5719, \"headroom\": 0.1389, \"fleiss_kappa\": 0.3851, \"soft_jaccard\": 0.6911, \"rho_kappa_f1\": 0.2844, \"rho_sj_f1\": 0.268, \"structural_gt_surface\": false}, \"fail_reasons\": [\"RE rho_sj=0.2680 < 0.40 threshold\", \">30% samples F1=0 (RE: 41.0%)\", \"RE structural not > surface (delta=-0.0165)\"]}, \"hypothesis\": \"LLaMA SciERC seed=123: early cross-model multi-seed test. Verifies LLaMA NER signal pattern is reproducible across sampling seeds.\"}, \"exp_008_re_seed123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T15:08:51.386Z\", \"updated_at\": \"2026-05-17T02:57:58.166Z\", \"spec\": {\"description\": \"RE N=16 on SciERC, seed=123, seed robustness test for relation extraction\", \"hypothesis\": \"Structural consistency correlates with per-instance RE F1, robust across seeds\", \"command\": \"CUDA_VISIBLE_DEVICES=3 PYTHONPATH=code python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc/processed_data --dataset scierc --subtask re --n_samples 16 --temperature 1.0 --seed 123 --num_test 9999 --collect_logprobs --output_dir output/exp_008_re_seed123\", \"server\": \"bjb1-21071\", \"data_path\": \"data/scierc/processed_data\", \"data_count\": 551, \"model_name\": \"qwen3-8b-scierc-merged-v2\", \"seed\": 123, \"gpu\": [\"cuda:3\"], \"backend\": \"tmux\", \"tmux_session\": \"exp008_rs123\", \"account\": \"root\", \"log_path\": \"output/exp_008_re_seed123/run.log\"}, \"log_path\": \"output/exp_008_re_seed123/run.log\", \"conclusion\": \"negative\", \"metrics\": {\"greedy_f1\": 0.4229, \"oracle_f1\": 0.6244, \"oracle_headroom\": 0.2015, \"fleiss_kappa_mean\": 0.3455, \"soft_jaccard_mean\": 0.6126, \"sample_f1_mean\": 0.3594, \"sample_f1_std\": 0.3793, \"sample_f1_zero_pct\": 44.1, \"structural_gt_surface\": false, \"rho_kappa_f1_full\": 0.3174, \"rho_sj_f1_full\": 0.2835, \"rho_kappa_f1_cond\": 0.0766, \"rho_sj_f1_cond\": 0.2877, \"logprob_auroc_full\": 0.6499, \"logprob_auroc_cond\": 0.5265, \"verdict\": \"FAIL\"}, \"checkpoint_path\": \"N/A\", \"completed_at\": \"2026-05-14T15:21:39.591Z\", \"hypothesis\": \"RE seed=123 multi-seed: tests reproducibility of RE signal rankings. Hypothesis: RE signals weaker than NER due to higher zero-F1 rate, but ranking should be seed-stable.\"}, \"exp_001_seed42_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T14:34:02.350Z\", \"updated_at\": \"2026-05-17T02:57:57.324Z\", \"spec\": {\"description\": \"NER N=16 on SciERC, seed=42, ft_002_v2, with logprobs\", \"hypothesis\": \"Structural consistency (Fleiss kappa, Soft Jaccard) correlates with per-instance NER F1 on SciERC\", \"server\": \"autodl-5090\", \"data_path\": \"data/scierc/processed_data\", \"data_count\": 551, \"model_name\": \"ft_002_v2\", \"seed\": 42, \"command\": \"CUDA_VISIBLE_DEVICES=1 PYTHONPATH=code python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc/processed_data --dataset scierc --subtask ner --n_samples 16 --temperature 1.0 --seed 42 --num_test 9999 --collect_logprobs --output_dir output/exp_001_seed42_v2\", \"gpu\": [\"cuda:1\"], \"pid\": \"78728\", \"backend\": \"tmux\", \"account\": \"root\", \"log_path\": \"output/exp_001_seed42_v2/run.log\"}, \"conclusion\": \"success\", \"metrics\": {\"sj_rho_full\": 0.428, \"sj_rho_cond\": 0.369, \"structural_minus_surface\": 0.147, \"conclusion_note\": \"NER seed42 robustness confirmed, structural>surface +0.147\"}, \"checkpoint_path\": \"N/A (inference)\", \"completed_at\": \"2026-05-14T15:23:34.091Z\", \"log_path\": \"output/exp_001_seed42_v2/\", \"hypothesis\": \"SciERC NER seed=42 v2: primary seed baseline under corrected pipeline. Establishes canonical signal rankings (SJ>FK>LP) for NER with gold-filtering.\"}, \"exp_001_seed123_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T14:34:04.210Z\", \"updated_at\": \"2026-05-17T02:57:42.106Z\", \"spec\": {\"description\": \"NER N=16 on SciERC, seed=123, ft_002_v2, with logprobs\", \"hypothesis\": \"Structural consistency (Fleiss kappa, Soft Jaccard) correlates with per-instance NER F1 on SciERC (seed robustness check)\", \"server\": \"autodl-5090\", \"data_path\": \"data/scierc/processed_data\", \"data_count\": 551, \"model_name\": \"ft_002_v2\", \"seed\": 123, \"command\": \"CUDA_VISIBLE_DEVICES=2 PYTHONPATH=code python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc/processed_data --dataset scierc --subtask ner --n_samples 16 --temperature 1.0 --seed 123 --num_test 9999 --collect_logprobs --output_dir output/exp_001_seed123_v2\", \"gpu\": [\"cuda:2\"], \"pid\": \"78733\", \"backend\": \"tmux\", \"account\": \"root\", \"log_path\": \"output/exp_001_seed123_v2/run.log\"}, \"conclusion\": \"success\", \"metrics\": {\"sj_rho_full\": 0.424, \"sj_rho_cond\": 0.376, \"structural_minus_surface\": 0.149, \"conclusion_note\": \"NER seed123 robustness confirmed, structural>surface +0.149\"}, \"checkpoint_path\": \"N/A (inference)\", \"completed_at\": \"2026-05-14T15:23:35.076Z\", \"log_path\": \"output/exp_001_seed123_v2/\", \"hypothesis\": \"SciERC NER seed=123 v2: second seed for multi-seed validation. Establishes reproducibility of structural>surface signal ranking across random seeds.\"}, \"exp_008_re_n16_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T14:34:06.296Z\", \"updated_at\": \"2026-05-17T02:57:41.178Z\", \"spec\": {\"description\": \"RE N=16 on SciERC full set confirmation, ft_002_v2, with logprobs\", \"hypothesis\": \"Structural consistency correlates with per-instance RE F1 on SciERC full dataset\", \"server\": \"autodl-5090\", \"data_path\": \"data/scierc/processed_data\", \"data_count\": 551, \"model_name\": \"ft_002_v2\", \"seed\": 42, \"command\": \"CUDA_VISIBLE_DEVICES=3 PYTHONPATH=code python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc/processed_data --dataset scierc --subtask re --n_samples 16 --temperature 1.0 --seed 42 --num_test 9999 --collect_logprobs --output_dir output/exp_008_re_n16_v2\", \"gpu\": [\"cuda:3\"], \"pid\": \"78737\", \"backend\": \"tmux\", \"account\": \"root\", \"log_path\": \"output/exp_008_re_n16_v2/run.log\"}, \"conclusion\": \"negative\", \"metrics\": {\"sj_rho_full\": 0.281, \"sj_rho_cond\": 0.308, \"f1_zero_pct\": 44.3, \"conclusion_note\": \"RE N=16 v2 negative: SJ weak, 44.3% F1=0\"}, \"checkpoint_path\": \"N/A (inference)\", \"completed_at\": \"2026-05-14T15:23:35.598Z\", \"log_path\": \"output/exp_008_re_n16_v2/\", \"hypothesis\": \"RE N=16 evaluation v2: tests structural signal effectiveness on relation extraction at higher sample count. Hypothesis: SJ/FK benefit from more samples on RE task where zero-F1 rate is high.\"}, \"exp_005_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T15:28:14.924Z\", \"updated_at\": \"2026-05-17T02:57:38.756Z\", \"spec\": {\"description\": \"Temperature sensitivity analysis: T=0.7 vs T=1.0 across 5 signals (SJ, FK, logprob, EM, voting_conf)\", \"command\": \"python code/analyze_exp005_v2_temperature.py\", \"server\": \"autodl-5090\", \"data_path\": \"output/mvp_pilot_004 + output/mvp_pilot_005 + output/exp_012_logprob\", \"data_count\": 551, \"model_name\": \"Qwen3-8B-SciERC-LoRA\", \"seed\": 42, \"checkpoint_path\": \"N/A\", \"log_path\": \"output/exp_005_v2_temperature/temperature_sensitivity_report.json\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T15:28:35.949Z\", \"hypothesis\": \"Selection F1 analysis v2: compute actual selection F1 (pick best sample by each signal) vs greedy and oracle. First evidence of correlation-selection gap under corrected pipeline.\"}, \"exp_006_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T15:30:02.348Z\", \"updated_at\": \"2026-05-17T02:57:36.914Z\", \"spec\": {\"command\": \"python3 code/exp_006_v2_selection.py\", \"server\": \"autodl-5090\", \"data_path\": \"output/exp_{001_seed42,001_seed123,002_conll,008_re}_v2/\", \"data_count\": 4952, \"model_name\": \"Qwen3-8B-SciERC-merged-v2\", \"seed\": 42}, \"conclusion\": \"negative\", \"checkpoint_path\": \"output/exp_006_v2/exp_006_v2_results.json\", \"log_path\": \"output/exp_006_v2_run.log\", \"completed_at\": \"2026-05-14T15:30:32.474Z\", \"metrics\": {\"NER_SciERC_s42\": {\"greedy\": 0.618, \"oracle\": 0.787, \"SJ\": 0.62, \"logprob\": 0.621, \"FK\": 0.621, \"EM\": 0.606, \"voting_conf\": 0.585, \"random\": 0.586}, \"NER_SciERC_s123\": {\"greedy\": 0.618, \"oracle\": 0.785, \"SJ\": 0.617, \"logprob\": 0.618, \"FK\": 0.621, \"EM\": 0.613, \"voting_conf\": 0.584, \"random\": 0.583}, \"NER_CoNLL\": {\"greedy\": 0.725, \"oracle\": 0.757, \"SJ\": 0.718, \"logprob\": 0.716, \"FK\": 0.717, \"EM\": 0.716, \"voting_conf\": 0.714, \"random\": 0.692}, \"RE_SciERC\": {\"greedy\": 0.403, \"oracle\": 0.631, \"SJ\": 0.397, \"logprob\": 0.41, \"FK\": 0.396, \"EM\": 0.381, \"voting_conf\": 0.408, \"random\": 0.364}}, \"hypothesis\": \"Temperature sensitivity v2: tests signal effectiveness at T=0.5,0.7,1.0,1.2. Hypothesis: structural signals are temperature-robust while LP degrades at extreme temperatures.\"}, \"exp_004_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T15:31:40.554Z\", \"updated_at\": \"2026-05-17T02:57:35.012Z\", \"conclusion\": \"success\", \"spec\": {\"command\": \"python code/analyze_exp004_v2_re_diagnostic.py\", \"server\": \"autodl-5090\", \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_012_logprob/samples_with_logprobs.jsonl\", \"data_count\": 551, \"model_name\": \"Qwen3-8B-SciERC-merged-v2\", \"seed\": 42, \"checkpoint_path\": \"N/A\", \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp004v2_re_diagnostic/\"}, \"completed_at\": \"2026-05-14T15:32:04.966Z\", \"hypothesis\": \"N-ablation v2 (N=4,8,16,32): tests how sample count affects signal ρ and selection F1. Validates N-scaling curve for structural vs surface signals under corrected pipeline.\"}, \"exp_009_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T15:36:47.946Z\", \"updated_at\": \"2026-05-17T02:57:32.655Z\", \"spec\": {\"command\": \"python3 code/exp_009_v2_stratification.py\", \"server\": \"autodl-5090\", \"data_path\": \"output/exp_001_seed42_v2 + exp_001_seed123_v2 + exp_008_re_n16_v2\", \"data_count\": 551, \"model_name\": \"analysis\", \"seed\": 42}, \"checkpoint_path\": \"output/exp_009_v2/results.json\", \"log_path\": \"output/exp_009_v2_run.log\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T15:37:18.311Z\", \"metrics\": {\"ner_seed42_global\": {\"sj_rho\": 0.431, \"fk_rho\": 0.325, \"logprob_rho\": 0.203, \"voting_conf_rho\": 0.475, \"em_rho\": 0.292}, \"ner_seed123_global\": {\"sj_rho\": 0.422, \"fk_rho\": 0.315, \"logprob_rho\": 0.226, \"voting_conf_rho\": 0.438, \"em_rho\": 0.299}, \"re_seed42_global\": {\"sj_rho\": 0.063, \"fk_rho\": 0.226, \"logprob_rho\": 0.4, \"voting_conf_rho\": 0.22, \"em_rho\": -0.132}, \"ner_seed_stability_max_delta\": 0.037, \"independent_proxies\": [\"sent_len\", \"ent_count\", \"type_diversity\"], \"inverted_u_ner\": \"not confirmed (ρ stable across independent proxies)\", \"inverted_u_re\": \"monotonic increase with complexity, not inverted-U\"}, \"hypothesis\": \"Capability stratification v2: corrected stratification with gold-filtering and extended to NER conditional analysis. Tests which instance subpopulations drive overall signal effectiveness.\"}, \"exp_016_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T15:39:07.501Z\", \"updated_at\": \"2026-05-17T02:57:30.726Z\", \"spec\": {\"command\": \"python code/exp_016_v2_ensemble.py\", \"server\": \"autodl-5090\", \"data_path\": \"output/exp_001_seed42_v2 + exp_001_seed123_v2 + exp_008_re_n16_v2\", \"data_count\": 551, \"model_name\": \"analysis_only\", \"seed\": 42, \"checkpoint_path\": \"output/exp_016_v2/\", \"log_path\": \"/tmp/exp016v2.log\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T15:39:34.478Z\", \"metrics\": {\"ner_conditional\": {\"n\": 529, \"best_single_signal_rho\": {\"soft_jaccard\": 0.4412}, \"best_combo_rho\": {\"sj+vc_a0.55\": 0.4552}, \"ensemble_auroc\": 0.7141, \"best_single_auroc\": {\"soft_jaccard\": 0.7166}, \"selection_f1\": {\"greedy\": 0.6442, \"logprob_best\": 0.6505, \"ensemble_best\": 0.6475, \"sj_best\": 0.6471, \"oracle\": 0.8442}}, \"re_conditional\": {\"n\": 397, \"best_single_signal_rho\": {\"voting_confidence\": 0.3849}, \"best_combo_rho\": {\"logprob+vc_a0.25\": 0.3936}, \"ensemble_auroc\": 0.6916, \"best_single_auroc\": {\"voting_confidence\": 0.7023}, \"selection_f1\": {\"greedy\": 0.403, \"logprob_best\": 0.4097, \"ensemble_best\": 0.4227, \"oracle\": 0.6306}}, \"re_full\": {\"ensemble_auroc\": 0.8608, \"best_single_auroc\": {\"voting_confidence\": 0.8248}}}, \"hypothesis\": \"Bootstrap significance v2: corrected bootstrap test for NER selection F1 gap with proper gold-filtering and multiple signals. Establishes which selection improvements are statistically significant.\"}, \"exp_001_seed456_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T15:38:55.569Z\", \"updated_at\": \"2026-05-17T02:57:23.336Z\", \"spec\": {\"hypothesis\": \"NER/RE N=16 seed=456 robustness test, third seed for 3-seed stability\", \"plan_id\": \"exp-001\", \"command\": \"CUDA_VISIBLE_DEVICES=2 PYTHONPATH=code python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc/processed_data --dataset scierc --subtask joint --n_samples 16 --temperature 1.0 --seed 456 --num_test 9999 --collect_logprobs --output_dir output/exp_001_seed456_v2\", \"server\": \"autodl-5090\", \"data_path\": \"data/scierc/processed_data\", \"data_count\": 551, \"model_name\": \"qwen3-8b-scierc-merged-v2\", \"seed\": 456, \"metrics\": {\"full_rho_kappa_f1\": 0.3383, \"full_rho_sj_f1\": 0.2988, \"cond_rho_kappa_f1\": 0.233, \"cond_rho_sj_f1\": 0.3245, \"logprob_full_rho\": 0.3405, \"logprob_full_auroc\": 0.6694, \"logprob_cond_rho\": 0.0501, \"structural_gt_surface\": false}, \"note\": \"CRITICAL: Ran with --subtask joint instead of --subtask ner. seed42/seed123 v2 used --subtask ner. Results valid for joint-mode analysis but NOT comparable for NER 3-seed protocol. Need NER-only rerun.\", \"log_path\": \"output/exp_001_seed456_v2/run.log\", \"checkpoint_path\": \"output/exp_001_seed456_v2/\"}, \"conclusion\": \"negative\", \"completed_at\": \"2026-05-14T17:12:14.682Z\", \"hypothesis\": \"SciERC joint NER+RE seed=456 v2: early pipeline version. Tests multi-seed stability of signal rankings on joint extraction task.\"}, \"exp_017_llama_conll_infer\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T17:33:23.653Z\", \"updated_at\": \"2026-05-17T02:57:21.948Z\", \"spec\": {\"hypothesis\": \"LLaMA-3.1-8B CoNLL-2003 inference: cross-model cross-dataset validation of structural consistency signals\", \"plan_id\": \"exp-017\", \"parent\": \"exp_017_llama_conll\", \"command\": \"python code/run_llama_conll_infer.py\", \"server\": \"autodl-5090\", \"data_path\": \"conll2003 test\", \"data_count\": 3453, \"model_name\": \"LLaMA-3.1-8B-Instruct\", \"seed\": 42, \"n_samples\": 8, \"temperature\": 1, \"description\": \"LLaMA CoNLL-2003 NER inference N=8 (cross-model + cross-dataset validation)\"}, \"metrics\": {\"greedy_f1\": 0.9266, \"oracle_f1\": 0.9443, \"oracle_headroom\": 0.0177, \"n_instances\": 3453, \"n_valid\": 2756, \"n_conditional\": 2642, \"N\": 8, \"full\": {\"SJ_rho\": 0.4314, \"FK_rho\": 0.4277, \"logprob_rho\": 0.3072, \"EM_rho\": 0.4306, \"voting_conf_rho\": 0.4256, \"SJ_AUROC\": 0.7039, \"FK_AUROC\": 0.7026, \"logprob_AUROC\": 0.761, \"EM_AUROC\": 0.7046, \"voting_conf_AUROC\": 0.7088, \"SJ_ECE\": 0.1137, \"FK_ECE\": 0.1053, \"logprob_ECE\": 0.129, \"EM_ECE\": 0.1094, \"voting_conf_ECE\": 0.0949}, \"conditional\": {\"SJ_rho\": 0.4356, \"FK_rho\": 0.431, \"logprob_rho\": 0.3282, \"EM_rho\": 0.4403, \"voting_conf_rho\": 0.3743, \"SJ_AUROC\": 0.7225, \"FK_AUROC\": 0.7208, \"logprob_AUROC\": 0.8102, \"EM_AUROC\": 0.7257, \"voting_conf_AUROC\": 0.6989, \"SJ_ECE\": 0.0829, \"FK_ECE\": 0.0796, \"logprob_ECE\": 0.0922, \"EM_ECE\": 0.0754, \"voting_conf_ECE\": 0.0784}}, \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_017_llama_conll_infer/samples.jsonl\", \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_017_llama_conll_infer/\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T17:55:33.476Z\", \"notes\": \"LLaMA CoNLL-2003 NER N=8 (not N=16, cost constraint: 3453 test instances). SJ ρ=0.431 > logprob ρ=0.307 (Δ=+0.124). ρ-AUROC dissociation: logprob AUROC=0.761 > SJ AUROC=0.704. All 4 structural signals ρ>0.42 vs logprob 0.31. Directly comparable to exp_002 (Qwen CoNLL N=8) and exp_007 (LLaMA SciERC N=8).\", \"hypothesis\": \"LLaMA CoNLL N=8 baseline inference: initial cross-model test on CoNLL before scaling to N=16. Establishes LLaMA can do CoNLL NER effectively.\"}, \"exp_003_wnut17_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T15:32:56.415Z\", \"updated_at\": \"2026-05-17T02:57:20.068Z\", \"spec\": {\"description\": \"WNUT-17 retrain: downsample gold-empty instances to ≤25%, fine-tune Qwen3-8B, inference N=16 T=1.0 with log-probs\", \"hypothesis\": \"After removing excess empty instances, structural consistency signals (SJ) will show stronger correlation on social media NER\", \"plan_id\": \"exp-003\", \"claim\": 1, \"model_name\": \"Qwen3-8B\", \"dataset\": \"WNUT-17 (downsampled)\", \"priority\": \"P0\", \"parent\": \"exp_003_ner_wnut17\", \"command\": \"CUDA_VISIBLE_DEVICES=1 llamafactory-cli train train_config_wnut17.yaml\", \"server\": \"autodl-5090\", \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/data/wnut17/llmfactory_train_downsampled.json\", \"data_count\": 1637, \"seed\": 42, \"pid\": 92215, \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/logs/train_wnut17.log\", \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen3-8b-wnut17-lora\", \"downsampling\": \"empty instances 63.8% -> 25.0%, total 3394 -> 1637\", \"metrics\": {\"train_loss\": 0.105, \"eval_loss\": 0.0836, \"epochs\": 5, \"train_time_min\": 16.37, \"train_samples_per_sec\": 8.33}, \"note\": \"D045: Training succeeded (train_loss=0.105) but inference FAIL: 54% F1=0, SJ rho=0.062 (p=0.106). WNUT-17 abandoned — model capability insufficient on social media NER. Paper reports as Claim 3 (capability boundary) evidence.\"}, \"conclusion\": \"negative\", \"completed_at\": \"2026-05-14T18:11:36.559Z\", \"hypothesis\": \"WNUT-17 NER evaluation v2: tests signal effectiveness on noisy social media text. Hypothesis: structural signals remain effective on noisy, informal text with high entity variation.\"}, \"exp_001_seed456_v2_ner\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T17:13:00.414Z\", \"updated_at\": \"2026-05-17T02:57:18.227Z\", \"spec\": {\"hypothesis\": \"NER N=16 seed=456 robustness test (NER-only rerun, fixing subtask mismatch from exp_001_seed456_v2)\", \"plan_id\": \"exp-001\", \"parent\": \"exp_001_seed456_v2\", \"command\": \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && CUDA_VISIBLE_DEVICES=2 PYTHONPATH=code python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc/processed_data --dataset scierc --subtask ner --n_samples 16 --temperature 1.0 --seed 456 --num_test 9999 --collect_logprobs --output_dir output/exp_001_seed456_v2_ner\", \"server\": \"autodl-5090\", \"data_path\": \"data/scierc/processed_data\", \"data_count\": 551, \"model_name\": \"qwen3-8b-scierc-merged-v2\", \"seed\": 456, \"checkpoint_source\": \"checkpoints/qwen3-8b-scierc-merged-v2\", \"eval_data\": \"data/scierc/processed_data\", \"metrics\": {\"sj_rho\": 0.384, \"structural_gt_surface\": true, \"structural_surface_delta\": 0.16}, \"log_path\": \"output/exp_001_seed456_v2_ner.log\", \"checkpoint_path\": \"output/exp_001_seed456_v2_ner/\"}, \"log_path\": \"output/exp_001_seed456_v2_ner.log\", \"pid\": 96161, \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T17:52:01.372Z\", \"metrics\": {\"full\": {\"SJ\": {\"rho\": 0.384, \"auroc\": 0.711}, \"FK\": {\"rho\": 0.223, \"auroc\": 0.577}, \"logprob\": {\"rho\": 0.232, \"auroc\": 0.594}, \"EM\": {\"rho\": 0.316, \"auroc\": 0.768}, \"voting_conf\": {\"rho\": 0.411, \"auroc\": 0.712}}, \"conditional\": {\"SJ\": {\"rho\": 0.349, \"auroc\": 0.699}, \"FK\": {\"rho\": 0.157, \"auroc\": 0.561}, \"logprob\": {\"rho\": 0.171, \"auroc\": 0.576}, \"EM\": {\"rho\": 0.406, \"auroc\": 0.78}, \"voting_conf\": {\"rho\": 0.346, \"auroc\": 0.694}}, \"3seed_mean_SJ_rho_full\": 0.412, \"3seed_sd_SJ_rho_full\": 0.025, \"structural_beats_surface\": true, \"verdict\": \"MARGINAL\"}, \"hypothesis\": \"SciERC NER seed=456 v2: corrected pipeline rerun with gold-filtering. Part of multi-seed validation protocol for NER signal ranking stability.\"}, \"exp_009_v2_re_rerun\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T18:56:31.535Z\", \"updated_at\": \"2026-05-17T02:57:16.383Z\", \"spec\": {\"command\": \"python code/exp_009_v2_re_rerun.py\", \"server\": \"autodl-5090\", \"data_path\": \"output/exp_008_re_n16_v2/samples.jsonl\", \"data_count\": 397, \"model_name\": \"cpu_analysis\", \"seed\": 42, \"checkpoint_source\": \"exp_008_re_n16_v2\", \"checkpoint_path\": \"output/exp_009_v2_re_rerun/results.json\", \"log_path\": \"/tmp/re_rerun.log\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T18:56:58.168Z\", \"hypothesis\": \"Capability stratification v2 (RE rerun): corrected stratification analysis for RE with proper gold-filtering. Fixes early pipeline bug affecting RE quartile ρ values.\"}, \"exp_007_llama_n16\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T18:31:44.366Z\", \"updated_at\": \"2026-05-17T02:57:12.521Z\", \"spec\": {\"hypothesis\": \"LLaMA SciERC N=16: cross-model N-scaling validation. If SJ rho increases from N=8 (0.363) to N=16, N-scaling is model-agnostic.\", \"plan_id\": \"exp-007\", \"parent\": \"exp_007_llama_inference\", \"command\": \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && CUDA_VISIBLE_DEVICES=1 PYTHONPATH=code python code/run_mvp_pilot.py --model_path checkpoints/llama3.1-8b-scierc-merged --data_dir data/scierc/processed_data --dataset scierc --subtask ner --n_samples 16 --temperature 1.0 --seed 42 --num_test 9999 --collect_logprobs --output_dir output/exp_007_llama_n16\", \"server\": \"autodl-5090\", \"data_path\": \"data/scierc/processed_data\", \"data_count\": 551, \"model_name\": \"llama3.1-8b-scierc-merged\", \"seed\": 42, \"checkpoint_source\": \"checkpoints/llama3.1-8b-scierc-merged\", \"eval_data\": \"data/scierc/processed_data\"}, \"conclusion\": \"success\", \"checkpoint_path\": \"output/exp_007_llama_n16/samples.jsonl\", \"log_path\": \"output/exp_007_llama_n16.log\", \"completed_at\": \"2026-05-14T19:03:39.163Z\", \"metrics\": {\"N\": 16, \"dataset\": \"scierc\", \"subtask\": \"ner\", \"n_instances\": 551, \"n_valid\": 529, \"n_conditional\": 478, \"greedy_f1\": 0.645, \"full\": {\"SJ_rho\": 0.3791, \"FK_rho\": 0.3081, \"logprob_rho\": 0.2041, \"EM_rho\": 0.3159, \"voting_conf_rho\": 0.4515, \"SJ_AUROC\": 0.717, \"FK_AUROC\": 0.6581, \"logprob_AUROC\": 0.5656, \"EM_AUROC\": 0.7686, \"voting_conf_AUROC\": 0.7266, \"SJ_ECE\": 0.1019, \"FK_ECE\": 0.1556, \"logprob_ECE\": 0.084, \"EM_ECE\": 0.1761, \"voting_conf_ECE\": 0.1365}, \"conditional\": {\"SJ_rho\": 0.3222, \"FK_rho\": 0.2182, \"logprob_rho\": 0.1286, \"EM_rho\": 0.3563, \"voting_conf_rho\": 0.3356, \"SJ_AUROC\": 0.7014, \"FK_AUROC\": 0.6392, \"logprob_AUROC\": 0.545, \"EM_AUROC\": 0.7708, \"voting_conf_AUROC\": 0.6988, \"SJ_ECE\": 0.1466, \"FK_ECE\": 0.1853, \"logprob_ECE\": 0.1141, \"EM_ECE\": 0.1887, \"voting_conf_ECE\": 0.2634}, \"n8_vs_n16_delta_rho_full\": {\"SJ\": 0.0161, \"FK\": -0.0185, \"logprob\": 0.0214, \"EM\": 0.0007, \"voting_conf\": 0.0184}}, \"hypothesis\": \"LLaMA SciERC N=16: cross-model NER signal evaluation at higher sample count. Tests if LLaMA shows same N-scaling benefit for structural signals as Qwen.\"}, \"exp_017_llama_conll_n16\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T19:19:35.318Z\", \"updated_at\": \"2026-05-17T02:56:57.283Z\", \"spec\": {\"hypothesis\": \"LLaMA CoNLL N=16: complete the 2x2 matrix (model x dataset x N). If SJ N-scaling holds for LLaMA on CoNLL, the finding is fully cross-model cross-dataset.\", \"plan_id\": \"exp-017\", \"parent\": \"exp_017_llama_conll_infer\", \"model_name\": \"llama3.1-8b-conll2003-merged\", \"dataset\": \"CoNLL-2003\", \"data_count\": 3453, \"seed\": 42, \"server\": \"autodl-5090\", \"command\": \"CUDA_VISIBLE_DEVICES=0 PYTHONPATH=code python code/run_mvp_pilot.py --model_path checkpoints/llama3.1-8b-conll2003-merged --data_dir data/conll2003 --dataset conll2003 --subtask ner --n_samples 16 --temperature 1.0 --seed 42 --num_test 9999 --collect_logprobs --output_dir output/exp_017_llama_conll_n16\", \"data_path\": \"data/conll2003\", \"pid\": 106997, \"n_samples\": 16, \"temperature\": 1, \"checkpoint_source\": \"checkpoints/llama3.1-8b-conll2003-merged\", \"eval_data\": \"conll2003 test set\", \"checkpoint_path\": \"output/exp_017_llama_conll_n16/samples.jsonl\", \"log_path\": \"output/exp_017_llama_conll_n16/all_signals_report.json\"}, \"metrics\": {\"greedy_f1\": 0.9243, \"oracle_f1\": 0.9487, \"oracle_headroom\": 0.0244, \"n_instances\": 3453, \"n_valid\": 2756, \"n_conditional\": 2642, \"structural_beats_surface\": true, \"full\": {\"SJ_rho\": 0.4642, \"SJ_AUROC\": 0.7391, \"SJ_ECE\": 0.1131, \"FK_rho\": 0.4566, \"FK_AUROC\": 0.736, \"FK_ECE\": 0.1071, \"logprob_rho\": 0.3058, \"logprob_AUROC\": 0.7594, \"logprob_ECE\": 0.1288, \"EM_rho\": 0.4613, \"EM_AUROC\": 0.7391, \"EM_ECE\": 0.1084, \"voting_conf_rho\": 0.4554, \"voting_conf_AUROC\": 0.7406, \"voting_conf_ECE\": 0.0844}, \"conditional\": {\"SJ_rho\": 0.4597, \"SJ_AUROC\": 0.7565, \"SJ_ECE\": 0.0846, \"FK_rho\": 0.4515, \"FK_AUROC\": 0.753, \"FK_ECE\": 0.0813, \"logprob_rho\": 0.3193, \"logprob_AUROC\": 0.8023, \"logprob_ECE\": 0.0921, \"EM_rho\": 0.4618, \"EM_AUROC\": 0.7589, \"EM_ECE\": 0.0757, \"voting_conf_rho\": 0.3978, \"voting_conf_AUROC\": 0.7287, \"voting_conf_ECE\": 0.0742}, \"best_of_n\": {\"greedy\": 0.9243, \"random_avg\": 0.9213, \"sj_best\": 0.9259, \"logprob_best\": 0.925, \"voting_conf_best\": 0.9268, \"oracle\": 0.9487}, \"n8_vs_n16_delta\": {\"full_SJ_rho_delta\": 0.0328, \"full_FK_rho_delta\": 0.0289, \"full_logprob_rho_delta\": -0.0014, \"full_EM_rho_delta\": 0.0307, \"full_voting_conf_rho_delta\": 0.0298, \"cond_SJ_rho_delta\": 0.0241, \"cond_FK_rho_delta\": 0.0205, \"cond_logprob_rho_delta\": -0.0089, \"cond_EM_rho_delta\": 0.0215, \"cond_voting_conf_rho_delta\": 0.0235}}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T19:45:16.265Z\", \"hypothesis\": \"LLaMA CoNLL N=16 seed=42 (original): cross-model validation on CoNLL. First evidence that structural>surface ranking generalizes from Qwen to LLaMA model family.\"}, \"exp_015_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T15:34:23.336Z\", \"updated_at\": \"2026-05-17T02:56:55.830Z\", \"spec\": {\"command\": \"python code/analyze_exp015_v2_metrics.py\", \"server\": \"autodl-5090\", \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/ (10 datasets)\", \"data_count\": 9148, \"model_name\": \"Qwen3-8B + LLaMA (multi-model)\", \"seed\": \"42,123,456 (multi-seed)\", \"checkpoint_path\": \"N/A (analysis only)\", \"log_path\": \"/tmp/exp015_v2.log\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T15:34:56.741Z\", \"metrics\": {\"scierc_ner_avg\": {\"sj_auroc\": 0.7394, \"fk_auroc\": 0.6172, \"em_auroc\": 0.7873, \"voting_auroc\": 0.7367, \"logprob_auroc\": 0.5918}, \"scierc_re_avg\": {\"sj_auroc\": 0.6746, \"fk_auroc\": 0.5939, \"em_auroc\": 0.715, \"voting_auroc\": 0.7234, \"logprob_auroc\": 0.5849}}, \"hypothesis\": \"Metrics expansion v2: corrected evaluation with proper conditional filtering. Updates exp_015 with gold-filtered pipeline to fix RE conditional ρ values that used wrong filter criterion.\"}, \"exp_001_n16_seed456\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-14T12:10:30.350Z\", \"updated_at\": \"2026-05-17T02:56:53.526Z\", \"completed_at\": \"2026-05-14T12:28:38.721Z\", \"extra\": {\"previous_failure\": {\"conclusion\": \"success\", \"metrics\": {\"ner\": {\"greedy_f1\": 0.6577, \"oracle_f1\": 0.8129, \"headroom\": 0.1553, \"rho_sj_full\": 0.3297, \"rho_fk_full\": 0.2578, \"rho_logprob_full\": 0.2866, \"rho_sj_cond\": 0.3394, \"rho_fk_cond\": 0.2721, \"rho_logprob_cond\": 0.2567, \"sj_beats_fk\": true, \"rho_advantage\": 0.0719}, \"re\": {\"greedy_f1\": 0.4312, \"oracle_f1\": 0.6737, \"headroom\": 0.2425, \"rho_sj_full\": 0.285, \"rho_fk_full\": 0.2372, \"rho_logprob_full\": 0.2626, \"rho_sj_cond\": 0.3525, \"rho_fk_cond\": 0.2614, \"rho_logprob_cond\": 0.1927, \"sj_beats_fk\": true, \"rho_advantage\": 0.0478}, \"verdict\": \"FAIL\"}}}, \"spec\": {\"hypothesis\": \"N=16 seed456 multi-seed robustness verification for SciERC NER+RE\", \"plan_id\": \"exp-001\", \"model_name\": \"qwen3-8b-scierc-merged-v2\", \"data_path\": \"data/scierc/processed_data\", \"data_count\": 551, \"seed\": 456, \"command\": \"python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc/processed_data --dataset scierc --subtask joint --n_samples 16 --temperature 1.0 --seed 456 --output_dir output/exp001_n16_seed456 --collect_logprobs\", \"server\": \"autodl-5090\", \"gpu\": \"cuda:0\", \"pid\": \"174595\", \"log_path\": \"output/exp001_n16_seed456_run.log\", \"tmux_session\": \"exp_001_n16_seed456\"}, \"conclusion\": \"success\", \"checkpoint_path\": \"N/A (inference-only)\", \"metrics\": {\"instance_count\": 551, \"n_valid\": 529, \"n_gold_empty\": 22, \"parse_rate\": 1, \"ner_greedy_f1\": 0.6617, \"ner_oracle_f1\": 0.8075, \"re_greedy_f1\": 0.4215, \"re_oracle_f1\": 0.4748, \"rho_sj_ner\": 0.4098, \"rho_fk_ner\": 0.2723, \"rho_vc_ner\": 0.4449, \"rho_em_ner\": 0.3363, \"rho_lp_ner\": 0.2415, \"rho_sj_re\": 0.2835, \"rho_fk_re\": 0.2929, \"auroc_sj_ner\": 0.6823, \"auroc_fk_ner\": 0.6179, \"auroc_vc_ner\": 0.6981, \"auroc_em_ner\": 0.649, \"auroc_lp_ner\": 0.5885, \"rho_note\": \"CORRECTED 2026-05-15: old values (rho_fk=0.3448,rho_sj=0.4134) included 22 gold-empty instances. Now uses gold-filtered pipeline (n=529).\"}, \"log_path\": \"output/exp001_n16_seed456_run.log\", \"hypothesis\": \"SciERC N=16 seed=456: early multi-seed validation of structural signal rankings at N=16 sample count. Establishes seed stability for SJ/FK/VC/EM ordering.\"}, \"exp_011_ood_scierc_to_conll\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T11:36:07.210Z\", \"updated_at\": \"2026-05-17T02:56:29.417Z\", \"spec\": {\"hypothesis\": \"SCS structural signals remain effective under domain shift (SciERC model on CoNLL data)\", \"plan_id\": \"exp-011\", \"model_name\": \"qwen3-8b-scierc-merged-v2\", \"data_path\": \"data/conll2003\", \"seed\": 42, \"pid\": 179761, \"server\": \"autodl-5090\", \"gpu\": \"cuda:3\", \"command\": \"python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --dataset conll2003 --data_dir data/conll2003 --subtask ner --n_samples 8 --temperature 1.0 --max_tokens 1024 --seed 42 --collect_logprobs --output_dir output/exp_011_ood_scierc_to_conll\", \"data_count\": 3500}, \"conclusion\": \"success\", \"checkpoint_path\": \"output/exp_011_ood_scierc_to_conll/samples.jsonl\", \"log_path\": \"output/exp_011_ood_scierc_to_conll/report.json\", \"completed_at\": \"2026-05-15T11:47:47.953Z\", \"metrics\": {\"greedy_ner_f1\": 0.522, \"rho_vc\": 0.469, \"rho_sj\": 0.378, \"rho_em\": 0.3, \"rho_fk\": 0.285, \"rho_lp\": 0.246}, \"hypothesis\": \"Out-of-domain transfer: SciERC-trained model on CoNLL data. Tests if confidence signals work under partial schema overlap (SciERC has Organization/Person which overlap with CoNLL ORG/PER). Complement to exp_011_ood_conll_to_scierc.\"}, \"exp_qwen3_4b_scierc_finetune_v4\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T19:26:25.512Z\", \"updated_at\": \"2026-05-17T02:56:24.418Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && llamafactory-cli train train_config_scierc_4b.yaml\\\"\", \"server\": \"autodl-5090\", \"gpu\": \"cuda:0\", \"pid\": \"227123\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_qwen3_4b_scierc_finetune_v4.log\", \"submitted_at\": \"2026-05-15T19:26:31.444Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/scierc/processed_data\", \"data_count\": 551, \"model_name\": \"Qwen3-4B\", \"seed\": 42, \"wall_clock_seconds\": 1668.8, \"gpu_hours\": 0.46}, \"conclusion\": \"success\", \"metrics\": {\"total_steps\": 585, \"completed_steps\": 585, \"best_checkpoint\": \"checkpoint-400\", \"best_eval_loss\": 0.0898, \"epochs\": 5}, \"checkpoint_path\": \"checkpoints/qwen3-4b-scierc-merged/\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_qwen3_4b_scierc_finetune_v4.log\", \"completed_at\": \"2026-05-15T19:54:20.255Z\", \"hypothesis\": \"Qwen3-4B SciERC LoRA fine-tune v4: training the smaller 4B model to complete the 2x2 scale matrix (4B×SciERC cell). Validates that fine-tuning convergence patterns hold across model scales.\"}, \"exp_011_ood_conll_to_scierc\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T11:36:08.325Z\", \"updated_at\": \"2026-05-17T02:56:14.242Z\", \"spec\": {\"hypothesis\": \"SCS structural signals remain effective under domain shift (CoNLL model on SciERC data, joint NER+RE)\", \"plan_id\": \"exp-011\", \"model_name\": \"qwen3-8b-conll2003-merged\", \"data_path\": \"data/scierc/processed_data\", \"seed\": 42, \"server\": \"autodl-5090\", \"gpu\": \"cuda:3\", \"pid\": 181723, \"command\": \"python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-conll2003-merged --dataset scierc --data_dir data/scierc/processed_data --subtask joint --n_samples 8 --temperature 1.0 --max_tokens 1024 --seed 42 --collect_logprobs --output_dir output/exp_011_ood_conll_to_scierc\", \"data_count\": 551}, \"conclusion\": \"negative\", \"checkpoint_path\": \"output/exp_011_ood_conll_to_scierc/samples.jsonl\", \"log_path\": \"output/exp_011_ood_conll_to_scierc/report.json\", \"completed_at\": \"2026-05-15T11:50:21.969Z\", \"metrics\": {\"greedy_ner_f1\": 0.009, \"greedy_re_f1\": 0.001, \"avg_structural_rho\": -0.05, \"verdict\": \"FAIL\", \"reason\": \"schema_incompatibility\", \"direction\": \"CoNLL_model_to_SciERC_data\", \"sample_f1_pct_zero_ner\": 98.06, \"rho_sj_ner\": -0.186, \"rho_fk_ner\": -0.069, \"note\": \"Schema incompatibility (CoNLL PER/ORG/LOC/MISC vs SciERC Task/Method/Material) causes catastrophic failure. Cannot evaluate confidence signals.\"}, \"hypothesis\": \"Out-of-domain transfer test: CoNLL-trained model on SciERC data. Tests if confidence signals retain correlation with quality under severe schema mismatch (CoNLL PER/ORG/LOC/MISC vs SciERC Task/Method/Material).\"}, \"exp_freeform_seed789_v3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T19:24:26.805Z\", \"updated_at\": \"2026-05-17T02:56:11.818Z\", \"spec\": {\"log_path\": \"~/runs/struct_self_consist_ie/exp_freeform_seed789_v3.log\", \"checkpoint_path\": \"results/exp_freeform_ablation_seed789/\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T19:30:51.048Z\", \"metrics\": {\"n_instances\": 551, \"n_samples\": 8, \"parse_rate_pct\": 100, \"elapsed_seconds\": 229.7, \"freeform_ner_selection_gap\": 0.0028, \"freeform_re_selection_gap\": 0.0219, \"freeform_lp_std\": 0.0183, \"freeform_lp_range\": 0.054908, \"freeform_tied_pct\": 59, \"re_lp_flip_positive\": true, \"variance_ratio_std\": 0.89, \"variance_ratio_range\": 0.88}, \"hypothesis\": \"Free-form SciERC seed=789 v3 (bugfix rerun): corrected version of free-form inference after fixing parsing/generation issues in v1/v2. Provides clean data point for 4-seed free-form analysis.\"}, \"exp_freeform_seed789\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T18:38:29.851Z\", \"updated_at\": \"2026-05-17T02:56:09.888Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && python run_freeform_inference.py --seed 789 --num_samples 8 --temperature 1.0 --max_tokens 1024 --output_dir results/exp_freeform_ablation_seed789\\\"\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:3\"], \"pid\": \"216722\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_freeform_seed789.log\", \"submitted_at\": \"2026-05-15T18:58:46.406Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 92.2, \"gpu_hours\": 0.03}, \"notes\": \"Rerun with fixed seed-passing code on cuda:3. Original run was killed for GPU reallocation. Parse rate 100%, 227.5s elapsed. LP compression confirmed: tied_pct=59.0% (vs constrained 59.7%), variance_ratio=0.89x.\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T19:00:18.576Z\", \"metrics\": {\"inference\": {\"n_instances\": 551, \"n_samples\": 8, \"total_samples\": 4408, \"total_parsed\": 4408, \"parse_rate_pct\": 100, \"elapsed_seconds\": 227.5}, \"freeform\": {\"selection_ner\": {\"greedy\": 0.6205, \"selected\": 0.6232, \"gap\": 0.0027}, \"selection_re\": {\"greedy\": 0.2909, \"selected\": 0.31, \"gap\": 0.0191}, \"logprob_variance\": {\"mean_std\": 0.0183, \"mean_range\": 0.054908, \"tied_pct\": 59}, \"qe_ner\": {\"n\": 529, \"SJ\": {\"rho\": 0.393995, \"auroc\": 0.734474}, \"FK\": {\"rho\": 0.312292, \"auroc\": 0.794384}, \"LP\": {\"rho\": 0.247096, \"auroc\": 0.677824}, \"EM\": {\"rho\": 0.320383, \"auroc\": 0.527033}, \"VC\": {\"rho\": 0.420625, \"auroc\": 0.768111}}, \"qe_re\": {\"n\": 397, \"SJ\": {\"rho\": 0.201746, \"auroc\": 0.574388}, \"FK\": {\"rho\": 0.2202, \"auroc\": 0.633014}, \"LP\": {\"rho\": 0.295765, \"auroc\": 0.687067}, \"EM\": {\"rho\": 0.103633, \"auroc\": 0.474737}, \"VC\": {\"rho\": 0.306868, \"auroc\": 0.642197}}}, \"constrained_ref\": {\"selection_ner\": {\"greedy\": 0.6182, \"selected\": 0.6241, \"gap\": 0.0059}, \"selection_re\": {\"greedy\": 0.2913, \"selected\": 0.2845, \"gap\": -0.0068}, \"logprob_variance\": {\"mean_std\": 0.020589, \"mean_range\": 0.062305, \"tied_pct\": 59.7}}, \"comparison\": {\"variance_ratio_std\": 0.89, \"variance_ratio_range\": 0.88, \"tied_reduction_pp\": 0.7}}, \"hypothesis\": \"Free-form SciERC seed=789: multi-seed replication of free-form ablation. Validates LP compression persistence and structural signal robustness across sampling seeds under unconstrained generation.\"}, \"exp_freeform_seed456\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T17:14:48.842Z\", \"updated_at\": \"2026-05-17T02:56:09.256Z\", \"spec\": {\"hypothesis\": \"Multi-seed free-form ablation (seed=456): verify RE LP flip and NER gap stability\", \"command\": \"python run_freeform_inference.py --seed 456 --num_samples 8 --temperature 1.0 --max_tokens 1024 --output_dir results/exp_freeform_ablation_seed456\", \"server\": \"autodl-5090\", \"data_path\": \"data/scierc/processed_data\", \"data_count\": 551, \"model_name\": \"qwen3-8b-scierc-merged-v2\", \"seed\": 456, \"gpu\": \"cuda:2\", \"tmux_session\": \"exp_freeform_seed456\", \"log_path\": \"results/exp_freeform_ablation_seed456/run_summary.json\", \"checkpoint_path\": \"results/exp_freeform_ablation_seed456\"}, \"metrics\": {\"inference\": {\"n_instances\": 551, \"n_samples\": 8, \"total_samples\": 4408, \"total_parsed\": 4407, \"parse_rate_pct\": 99.98, \"elapsed_seconds\": 232.4}, \"freeform\": {\"selection_ner\": {\"greedy\": 0.6198, \"selected\": 0.6205, \"gap\": 0.0007}, \"selection_re\": {\"greedy\": 0.2908, \"selected\": 0.3108, \"gap\": 0.02}, \"logprob_variance\": {\"mean_std\": 0.018631, \"mean_range\": 0.056792, \"tied_pct\": 58.4}, \"qe_ner\": {\"n\": 529, \"SJ\": {\"rho\": 0.378498, \"auroc\": 0.707769}, \"FK\": {\"rho\": 0.286163, \"auroc\": 0.754779}, \"LP\": {\"rho\": 0.227089, \"auroc\": 0.672081}, \"EM\": {\"rho\": 0.319997, \"auroc\": 0.47789}, \"VC\": {\"rho\": 0.416853, \"auroc\": 0.756543}}, \"qe_re\": {\"n\": 397, \"SJ\": {\"rho\": 0.211331, \"auroc\": 0.572335}, \"FK\": {\"rho\": 0.259074, \"auroc\": 0.652998}, \"LP\": {\"rho\": 0.306382, \"auroc\": 0.70134}, \"EM\": {\"rho\": 0.1043, \"auroc\": 0.461641}, \"VC\": {\"rho\": 0.301507, \"auroc\": 0.628873}}}, \"constrained_ref\": {\"selection_ner\": {\"greedy\": 0.6182, \"selected\": 0.6241, \"gap\": 0.0059}, \"selection_re\": {\"greedy\": 0.2913, \"selected\": 0.2845, \"gap\": -0.0068}, \"logprob_variance\": {\"mean_std\": 0.020589, \"mean_range\": 0.062305, \"tied_pct\": 59.7}}, \"comparison\": {\"variance_ratio_std\": 0.9, \"variance_ratio_range\": 0.91, \"tied_reduction_pp\": 1.3}}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T19:12:29.413Z\", \"hypothesis\": \"Free-form SciERC seed=456: multi-seed replication of free-form ablation. Validates LP compression persistence and structural signal robustness across sampling seeds under unconstrained generation.\"}, \"exp_freeform_seed123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T17:14:47.765Z\", \"updated_at\": \"2026-05-17T02:56:06.903Z\", \"spec\": {\"hypothesis\": \"Multi-seed free-form ablation (seed=123): verify RE LP flip and NER gap stability\", \"command\": \"python run_freeform_inference.py --seed 123 --num_samples 8 --temperature 1.0 --max_tokens 1024 --output_dir results/exp_freeform_ablation_seed123\", \"server\": \"autodl-5090\", \"data_path\": \"data/scierc/processed_data\", \"data_count\": 551, \"model_name\": \"qwen3-8b-scierc-merged-v2\", \"seed\": 123, \"gpu\": \"cuda:1\", \"tmux_session\": \"exp_freeform_seed123\", \"log_path\": \"results/exp_freeform_ablation_seed123/run_summary.json\", \"checkpoint_path\": \"results/exp_freeform_ablation_seed123\"}, \"metrics\": {\"inference\": {\"n_instances\": 551, \"n_samples\": 8, \"total_samples\": 4408, \"total_parsed\": 4406, \"parse_rate_pct\": 99.95, \"elapsed_seconds\": 228.1}, \"freeform\": {\"selection_ner\": {\"greedy\": 0.6194, \"selected\": 0.6222, \"gap\": 0.0028}, \"selection_re\": {\"greedy\": 0.2874, \"selected\": 0.305, \"gap\": 0.0176}, \"logprob_variance\": {\"mean_std\": 0.019881, \"mean_range\": 0.059864, \"tied_pct\": 57.7}, \"qe_ner\": {\"n\": 529, \"SJ\": {\"rho\": 0.384214, \"auroc\": 0.748728}, \"FK\": {\"rho\": 0.323956, \"auroc\": 0.766039}, \"logprob\": {\"rho\": 0.217297, \"auroc\": 0.701657}, \"EM\": {\"rho\": 0.326887, \"auroc\": 0.52533}, \"voting_conf\": {\"rho\": 0.407893, \"auroc\": 0.799676}}, \"qe_re\": {\"n\": 397, \"SJ\": {\"rho\": 0.272776, \"auroc\": 0.614056}, \"FK\": {\"rho\": 0.314429, \"auroc\": 0.678534}, \"logprob\": {\"rho\": 0.309673, \"auroc\": 0.70414}, \"EM\": {\"rho\": 0.137216, \"auroc\": 0.487342}, \"voting_conf\": {\"rho\": 0.316667, \"auroc\": 0.647442}}}, \"constrained_ref\": {\"selection_ner\": {\"greedy\": 0.6182, \"selected\": 0.6241, \"gap\": 0.0059}, \"selection_re\": {\"greedy\": 0.2913, \"selected\": 0.2845, \"gap\": -0.0068}}, \"comparison\": {\"variance_ratio_std\": 0.97, \"variance_ratio_range\": 0.96, \"tied_reduction_pp\": 2}}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T19:29:48.939Z\", \"hypothesis\": \"Free-form SciERC seed=123: multi-seed replication of free-form ablation. Validates LP compression persistence and structural signal robustness across sampling seeds under unconstrained generation.\"}, \"exp_009_capability_stratification\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T14:59:24.201Z\", \"updated_at\": \"2026-05-17T02:56:02.685Z\", \"spec\": {\"command\": \"python code/exp009_stratification_analysis.py\", \"server\": \"autodl-5090\", \"data_path\": \"output/exp001_n16_seed42 + output/exp008_re_n16 + output/exp002_conll2003\", \"data_count\": 4555, \"model_name\": \"analysis_only\", \"seed\": 42}, \"conclusion\": \"success\", \"checkpoint_path\": \"output/exp009_stratification_results.json\", \"log_path\": \"/tmp/exp009.log\", \"completed_at\": \"2026-05-14T14:59:46.463Z\", \"metrics\": {\"scierc_ner\": {\"n\": 551, \"sj_rho_overall\": 0.398, \"by_greedy_f1\": {\"hard_0_25_sj_rho\": 0.159, \"med_low_sj_rho\": 0.139, \"med_high_sj_rho\": 0.09, \"easy_sj_rho\": 0.23}, \"by_sent_len\": {\"Q1_sj_rho\": 0.461, \"Q2_sj_rho\": 0.401, \"Q3_sj_rho\": 0.296, \"Q4_sj_rho\": 0.382}, \"by_ent_count\": {\"0_sj_rho\": 0.689, \"1_2_sj_rho\": 0.415, \"3_5_sj_rho\": 0.353, \"6plus_sj_rho\": 0.547}}, \"scierc_re\": {\"n\": 551, \"by_greedy_f1\": {\"hard_0_25_sj_rho\": -0.043, \"easy_sj_rho\": 0.21}, \"by_sent_len\": {\"Q1_sj_rho\": 0.447, \"Q4_sj_rho\": 0.54}, \"by_rel_count\": {\"0_sj_rho\": 0.62, \"1_2_sj_rho\": 0.275, \"6plus_sj_rho\": 0.527}}, \"conll_ner\": {\"n\": 3453, \"by_sent_len\": {\"Q1_sj_rho\": 0.334, \"Q3_sj_rho\": 0.518}}, \"proxy_independence\": {\"scierc_ner_f1_vs_slen\": -0.021, \"scierc_ner_f1_vs_ecnt\": 0.007, \"scierc_re_f1_vs_slen\": -0.147}}, \"notes\": \"Registry metrics are PRE-gold-filter (n=551). Paper uses exp_009_v2_re_rerun (gold-filtered n=397): RE Q1_sj_rho=0.110, Q4_sj_rho=0.473. Registry values (Q1=0.447, Q4=0.540) are SUPERSEDED.\", \"hypothesis\": \"Capability stratification analysis: test if SJ signal effectiveness varies with instance difficulty (greedy F1 quartiles), sentence length, and entity/relation count. Identifies which instance subpopulations benefit most from structural consistency signals.\"}, \"exp_023_lora_rank8\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T10:29:59.501Z\", \"updated_at\": \"2026-05-17T02:55:50.540Z\", \"spec\": {\"hypothesis\": \"LoRA rank=8 ablation: does reducing rank from 32 to 8 significantly affect correlation-selection patterns?\", \"model_name\": \"Qwen/Qwen3-8B\", \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/data/llmfactory_train.json\", \"data_count\": 1861, \"server\": \"autodl-5090\", \"seed\": 42, \"parent\": \"ft_002_v2\", \"method\": \"LoRA r=8 alpha=16, 5 epochs, batch=2 grad_accum=8 gradient_checkpointing=true\", \"gpu\": \"cuda:2\", \"pid\": 288382, \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/logs/exp023_rank8_train.log\", \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen3-8b-scierc-lora-rank8\", \"command\": \"CUDA_VISIBLE_DEVICES=2 llamafactory-cli train train_config_rank8.yaml\", \"trainable_params\": \"21.8M\", \"total_steps\": 585, \"estimated_runtime\": \"26min\"}, \"conclusion\": \"success\", \"metrics\": {\"train_loss\": 0.1018, \"eval_loss\": 0.0776, \"train_runtime\": \"28m45s\", \"ner_full\": {\"n\": 529, \"greedy_f1\": 0.6397, \"oracle_f1\": 0.7998, \"oracle_headroom\": 0.1601, \"degeneracy_rate\": 0.072, \"SJ_rho\": 0.3649, \"FK_rho\": 0.2838, \"VC_rho\": 0.394, \"EM_rho\": 0.2562, \"LP_rho\": 0.2105, \"SJ_auroc\": 0.689, \"FK_auroc\": 0.6002, \"VC_auroc\": 0.6886, \"EM_auroc\": 0.7265, \"LP_auroc\": 0.6054, \"sel_SJ\": 0.6306, \"sel_FK\": 0.6265, \"sel_VC\": 0.5919, \"sel_EM\": 0.6073, \"sel_LP\": 0.635}, \"ner_cond\": {\"n\": 477, \"SJ_rho\": 0.3056, \"FK_rho\": 0.1452, \"VC_rho\": 0.3191, \"EM_rho\": 0.3558, \"LP_rho\": 0.169}, \"re_full\": {\"n\": 397, \"greedy_f1\": 0.3712, \"oracle_f1\": 0.609, \"oracle_headroom\": 0.2378, \"degeneracy_rate\": 0.217, \"SJ_rho\": 0.2244, \"FK_rho\": 0.3448, \"VC_rho\": 0.3617, \"EM_rho\": 0.068, \"LP_rho\": 0.2737, \"SJ_auroc\": 0.7092, \"FK_auroc\": 0.6469, \"VC_auroc\": 0.7533, \"EM_auroc\": 0.7306, \"LP_auroc\": 0.6325, \"sel_SJ\": 0.3584, \"sel_FK\": 0.3498, \"sel_VC\": 0.3715, \"sel_EM\": 0.3291, \"sel_LP\": 0.3606}, \"re_cond\": {\"n\": 242, \"SJ_rho\": 0.3601, \"FK_rho\": 0.2343, \"VC_rho\": 0.3703, \"EM_rho\": 0.4613, \"LP_rho\": 0.1809}}, \"completed_at\": \"2026-05-16T11:22:34.576Z\", \"hypothesis\": \"LoRA rank=8 ablation on SciERC: test if reduced model capacity (rank 8 vs 32) changes signal effectiveness ranking or correlation-selection gap pattern. Verifies findings are not rank-specific artifacts.\", \"parent\": \"exp_012_rerun_1024\"}, \"exp_022_seed789\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T10:08:27.375Z\", \"updated_at\": \"2026-05-17T02:55:49.870Z\", \"hypothesis\": \"3rd seed SciERC inference (seed=789) with ft_002_v2 (Qwen3-8B). N=8, T=1.0, joint NER+RE, logprobs collected. Complements seed42 (exp_012_rerun_1024) and seed123/456 for multi-seed analysis.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 PYTHONPATH=code python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc/processed_data --dataset scierc --subtask joint --n_samples 8 --temperature 1.0 --seed 789 --num_test 9999 --max_tokens 1024 --collect_logprobs --output_dir output/exp_022_seed789/\", \"server\": \"autodl-5090\", \"data_path\": \"data/scierc/processed_data\", \"data_count\": 551, \"model_name\": \"Qwen3-8B (qwen3-8b-scierc-merged-v2)\", \"seed\": 789, \"checkpoint_path\": \"checkpoints/qwen3-8b-scierc-merged-v2\", \"log_path\": \"output/exp_022_seed789/run.log\", \"gpu\": \"cuda:0\", \"pid\": 286743, \"account\": \"root\", \"backend\": \"tmux\", \"tmux_session\": \"exp_022_seed789\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T14:25:17.461Z\", \"parent\": \"exp_012_rerun_1024\"}, \"exp_025_n32\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T13:38:26.420Z\", \"updated_at\": \"2026-05-17T02:55:46.212Z\", \"spec\": {\"checkpoint_path\": \"checkpoints/qwen3-8b-scierc-merged-v2\", \"log_path\": \"output/exp_025_n32/run.log\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T14:25:39.849Z\", \"metrics\": {\"n_samples\": 32, \"degeneracy_pct\": 4, \"lp_range\": 0.0781, \"oracle_f1\": 0.8412, \"greedy_f1\": 0.6615, \"oracle_gap\": 0.1797, \"selection_f1_lp_delta\": 0.54, \"selection_f1_sj_delta\": 0.16, \"selection_f1_fk_delta\": 0.6, \"selection_f1_em_delta\": 0.68, \"selection_f1_vc_delta\": -5.21, \"best_signal\": \"EM\", \"best_delta\": 0.68, \"metric_space\": \"micro_f1_filtered_529inst\", \"note\": \"corrected via n_ablation_fixed.py, greedy from inst['greedy'] field\"}, \"hypothesis\": \"N=32 sample ablation on SciERC: test if increasing samples from 8→32 reduces degeneracy and improves selection F1, particularly for structural signals. Validates whether sample count is the bottleneck for signal effectiveness.\", \"parent\": \"exp_012_rerun_1024\"}, \"exp_021_fewnerd_full\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T16:33:44.079Z\", \"updated_at\": \"2026-05-17T02:55:45.560Z\", \"hypothesis\": \"Full Few-NERD LoRA fine-tune (rank=32, α=64, 3 epochs) on SUPERVISED coarse 8-type NER (131k train). 4-GPU DDP on autodl-5090. Post-training: N=8 inference on full test set, T=1.0, seed=42, collect logprobs for SCS metrics.\", \"spec\": {\"gpu\": \"cuda:0,cuda:1,cuda:2,cuda:3\", \"gpu_count\": 4, \"training_mode\": \"DDP\", \"checkpoint_path\": \"output/exp_021_fewnerd_full/checkpoint-6177\", \"log_path\": \"output/exp_021_inference/\"}, \"conclusion\": \"success\", \"metrics\": {\"total_steps\": 6177, \"train_loss\": 0.048, \"eval_loss\": 0.0275, \"train_runtime\": \"3h57m\", \"epochs\": 3, \"final_checkpoint\": \"output/exp_021_fewnerd_full/checkpoint-6177\", \"adapter_path\": \"output/exp_021_fewnerd_full/adapter_model.safetensors\", \"inference_instances\": 37648, \"inference_filtered\": 32565, \"inference_n_samples\": 8, \"greedy_macro_f1\": 0.7478, \"oracle_macro_f1\": 0.8719, \"headroom\": 0.124, \"zero_f1_rate\": 0.119, \"degeneracy_rate\": 0.101, \"lp_within_range_mean\": 0.0879, \"lp_within_range_median\": 0.0662, \"lp_global_rho\": 0.4215, \"lp_cond_rho\": 0.4225, \"sj_global_rho\": 0.3002, \"sj_cond_rho\": 0.2937, \"fk_global_rho\": 0.3132, \"fk_cond_rho\": 0.3093, \"em_global_rho\": 0.2871, \"em_cond_rho\": 0.271, \"vc_global_rho\": 0.3858, \"vc_cond_rho\": 0.3234, \"lp_selection_delta_pp\": 1.36, \"vc_selection_delta_pp\": -1.79, \"sj_selection_delta_pp\": -2.14, \"fk_selection_delta_pp\": -2.26, \"em_selection_delta_pp\": -3.85, \"lp_bootstrap_ci_95_pp\": [1.18, 1.53], \"lp_sample_auroc\": 0.5782, \"vc_sample_auroc\": 0.5354, \"fk_sample_auroc\": 0.521, \"sj_sample_auroc\": 0.5197, \"em_sample_auroc\": 0.5137, \"scenario\": \"A_partial\", \"note\": \"Full analysis (gold-filtered n=32565). Prior simplified analysis used unfiltered data with different metrics.\"}, \"completed_at\": \"2026-05-16T22:04:16.683Z\", \"parent\": \"exp_020_fewnerd_smoke\"}, \"exp_015_metrics_expansion\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T11:47:36.569Z\", \"updated_at\": \"2026-05-17T02:55:35.391Z\", \"spec\": {\"hypothesis\": \"Comprehensive evaluation of all 5 confidence signals with extended metrics\", \"model_name\": \"N/A (reuse pilot_004 samples)\", \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_012_logprob/samples_with_logprobs.jsonl\", \"data_count\": 551, \"server\": \"autodl-5090\", \"seed\": 42, \"parent\": \"exp_012_logprob_baseline\", \"method\": \"CPU-only analysis: 6 metrics x 5 signals x 2 subtasks (NER+RE)\", \"command\": \"python code/analyze_exp015_metrics_expansion.py\", \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/mvp_pilot_004\", \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp015_metrics_expansion\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T12:22:32.661Z\", \"metrics\": {\"data_source\": \"exp_012_logprob/samples_with_logprobs.jsonl\", \"config\": \"N=8, T=1.0, seed=42, model=qwen3-8b-scierc-merged-v2\", \"ner\": {\"n_valid\": 529, \"n_cond\": 501, \"voting_rho_full\": 0.5018, \"voting_rho_cond\": 0.4497, \"voting_auroc\": 0.7279, \"voting_tau\": 0.3766, \"sj_rho_full\": 0.3565, \"sj_rho_cond\": 0.412, \"sj_auroc\": 0.6656, \"sj_tau\": 0.2658, \"em_rho_full\": 0.2566, \"em_rho_cond\": 0.3427, \"em_auroc\": 0.623, \"em_tau\": 0.1924, \"fk_rho_full\": 0.2651, \"fk_rho_cond\": 0.306, \"fk_auroc\": 0.6243, \"fk_tau\": 0.2027, \"logprob_rho_full\": 0.1396, \"logprob_rho_cond\": 0.1627, \"logprob_auroc\": 0.5585, \"logprob_tau\": 0.1006}, \"re\": {\"n_valid\": 397, \"n_cond\": 296, \"voting_rho_full\": 0.4217, \"voting_rho_cond\": 0.463, \"voting_auroc\": 0.7162, \"voting_tau\": 0.327, \"sj_rho_full\": 0.2112, \"sj_rho_cond\": 0.3683, \"sj_auroc\": 0.5816, \"sj_tau\": 0.1619, \"em_rho_full\": 0.1002, \"em_rho_cond\": 0.3607, \"em_auroc\": 0.5036, \"em_tau\": 0.0839, \"fk_rho_full\": 0.2528, \"fk_rho_cond\": 0.3168, \"fk_auroc\": 0.6308, \"fk_tau\": 0.1967, \"logprob_rho_full\": 0.2467, \"logprob_rho_cond\": 0.1457, \"logprob_auroc\": 0.6354, \"logprob_tau\": 0.1808}, \"diagnosis\": \"Unified 5-signal evaluation on single data source. Voting leads NER full (ρ=0.502), SJ retains strength in NER cond (ρ=0.412). All structural signals beat logprob on NER. RE: voting leads both full and cond.\"}, \"notes\": \"RE logprob_rho_cond=0.1457 uses WRONG conditional filter (any sample F1>0, n=331). Correct value: 0.0112 from exp_012_rerun_1024 (greedy_f1>0, n=238). This entry's RE cond values are DEPRECATED.\", \"hypothesis\": \"Unified 5-signal evaluation (SJ/FK/EM/VC/LP) on single canonical data source (exp_012 logprobs). Establishes complete signal ranking with ρ, AUROC, and τ metrics for both NER and RE under consistent conditions.\"}, \"exp_020_fewnerd_smoke\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T10:29:25.272Z\", \"updated_at\": \"2026-05-16T16:33:59.109Z\", \"spec\": {\"checkpoint_path\": \"checkpoints/ft_fewnerd_smoke\", \"log_path\": \"checkpoints/fewnerd_train.log\"}, \"hypothesis\": \"1-epoch LoRA (r16) fine-tune Qwen3-8B on Few-NERD INTRA coarse 8-type (131k train), then N=8 T=1.0 pilot inference on 200 test instances. Re-started training 2026-05-16 18:29 CST on cuda:1, PID 288683. ETA ~22:55 CST.\", \"conclusion\": \"success\", \"metrics\": {\"final_loss\": 0.031, \"total_steps\": 8236, \"training_time\": \"5h54m\", \"pilot_greedy_f1\": 0.8037, \"pilot_instances\": 200, \"merged_model_path\": \"checkpoints/qwen3-8b-fewnerd-merged\"}, \"completed_at\": \"2026-05-16T16:33:59.109Z\"}, \"exp_vc_lp_cascade_selection\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T04:44:02.658Z\", \"updated_at\": \"2026-05-16T06:31:26.755Z\", \"hypothesis\": \"VC-filtered LP selection cascade: test if combining VC (pre-filter) + LP (rank) improves selection F1 over single-signal selection. Addresses SF3 reviewer suggestion. Pure analysis on existing data.\", \"conclusion\": \"killed\", \"spec\": {\"command\": \"N/A - cancelled before execution\", \"server\": \"N/A\", \"data_path\": \"N/A\", \"data_count\": 0, \"model_name\": \"N/A\", \"seed\": 0, \"checkpoint_path\": \"N/A\", \"log_path\": \"N/A\"}, \"completed_at\": \"2026-05-16T06:31:26.755Z\"}, \"exp_tacred_re_benchmark\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T04:43:59.002Z\", \"updated_at\": \"2026-05-16T06:31:25.273Z\", \"hypothesis\": \"TACRED RE benchmark: replicate SciERC RE experiment flow on second RE dataset. Verify correlation-selection gap generalizes beyond SciERC. D104 highest priority — addresses R11 MF1 consensus weakness.\", \"conclusion\": \"killed\", \"spec\": {\"command\": \"N/A - cancelled before execution\", \"server\": \"N/A\", \"data_path\": \"N/A\", \"data_count\": 0, \"model_name\": \"N/A\", \"seed\": 0, \"checkpoint_path\": \"N/A\", \"log_path\": \"N/A\"}, \"completed_at\": \"2026-05-16T06:31:25.273Z\"}, \"exp_vc_quartile_analysis\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T04:48:35.263Z\", \"updated_at\": \"2026-05-16T05:00:36.736Z\", \"hypothesis\": \"VC quartile stratification: split instances by VC score into Q1-Q4, compute LP selection F1 per quartile. Test if LP selection ability recovers in high-VC instances. Addresses SF3.\", \"spec\": {\"command\": \"python vc_quartile_analysis.py\", \"server\": \"autodl-5090\", \"data_path\": \"output/exp_012_rerun_1024/samples.jsonl + output/exp_002_conll_n8_seed42/samples.jsonl\", \"data_count\": 3682, \"model_name\": \"analysis_only (Qwen3-8B data)\", \"seed\": 42}, \"conclusion\": \"success\", \"checkpoint_path\": \"artifacts/vc_quartile_analysis/results.json\", \"log_path\": \"artifacts/vc_quartile_analysis/report.md\", \"completed_at\": \"2026-05-16T05:00:30.439Z\", \"metrics\": {\"scierc_ner\": {\"Q1_lp_delta\": 0.016, \"Q2_lp_delta\": -0.006, \"Q3_lp_delta\": 0.02, \"Q4_lp_delta\": -0.004, \"Q4_mean_vc\": 0.921, \"Q1_headroom\": 0.169, \"Q4_headroom\": 0.048, \"overall_lp_delta\": 0.006, \"n\": 529}, \"scierc_re\": {\"Q1_lp_delta\": -0.036, \"Q2_lp_delta\": -0.021, \"Q3_lp_delta\": -0.022, \"Q4_lp_delta\": 0.04, \"Q4_mean_vc\": 0.894, \"Q1_headroom\": 0.211, \"Q4_headroom\": 0.145, \"overall_lp_delta\": -0.009, \"n\": 397}, \"conll_ner\": {\"Q1_lp_delta\": -0.037, \"Q2_lp_delta\": -0.005, \"Q3_lp_delta\": 0, \"Q4_lp_delta\": 0, \"overall_lp_delta\": -0.01, \"n\": 2756, \"note\": \"Q3/Q4 degenerate (VC=1.0, all samples identical)\"}, \"conclusion\": \"VC stratification does not solve LP compression for NER. RE Q4 is only exception (+0.040).\"}}, \"exp_llama3b_scierc_ablation\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T02:45:23.638Z\", \"updated_at\": \"2026-05-16T03:59:26.005Z\", \"hypothesis\": \"Cross-family scale ablation: LLaMA 3.2-3B on SciERC NER. Verify correlation-selection gap generalizes across model families AND scales. Compare with LLaMA 8B results.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 PYTHONPATH=code python code/run_mvp_pilot.py --model_path checkpoints/llama3.2-3b-scierc-merged --data_dir data/scierc/processed_data --dataset scierc --subtask ner --n_samples 8 --temperature 1.0 --seed 42 --num_test 9999 --max_tokens 1024 --collect_logprobs --output_dir output/review_round9_experiments/llama3b_scierc/\", \"server\": \"autodl-5090\", \"data_path\": \"data/scierc/processed_data\", \"data_count\": 551, \"model_name\": \"LLaMA-3.2-3B-Instruct (LoRA r=32 SciERC fine-tuned)\", \"seed\": 42, \"checkpoint_path\": \"checkpoints/llama3.2-3b-scierc-merged\", \"log_path\": \"output/review_round9_experiments/llama3b_scierc/inference.log\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T03:59:16.198Z\", \"metrics\": {\"ner_full\": {\"SJ_rho\": 0.3754, \"FK_rho\": 0.2676, \"LP_rho\": 0.2662, \"EM_rho\": 0.3341, \"VC_rho\": 0.4602, \"SJ_auroc\": 0.7383, \"FK_auroc\": 0.6714, \"LP_auroc\": 0.633, \"EM_auroc\": 0.7763, \"VC_auroc\": 0.7429, \"n\": 529}, \"ner_cond\": {\"SJ_rho\": 0.3445, \"FK_rho\": 0.2125, \"LP_rho\": 0.2099, \"EM_rho\": 0.3952, \"VC_rho\": 0.3815, \"SJ_auroc\": 0.7292, \"FK_auroc\": 0.66, \"LP_auroc\": 0.6156, \"EM_auroc\": 0.7822, \"VC_auroc\": 0.7222, \"n\": 476}, \"greedy_f1\": 0.6267, \"oracle_f1\": 0.763, \"oracle_headroom\": 0.1363, \"selection_f1_SJ\": 0.6328, \"selection_f1_VC\": 0.6113, \"selection_f1_FK\": 0.6295, \"selection_f1_EM\": 0.6174, \"selection_f1_LP\": 0.6279, \"n_gold_empty\": 22, \"structural_beats_surface\": true, \"rho_advantage_SJ_over_FK\": 0.1078}}, \"exp_freeform_conll_4seed\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T02:45:17.133Z\", \"updated_at\": \"2026-05-16T03:04:49.550Z\", \"hypothesis\": \"Free-form CoNLL NER 4-seed ablation: verify LP compression is cross-dataset intrinsic (not SciERC-specific). 4 seeds × N=8, T=1.0 on CoNLL, compare LP range distribution with constrained decoding.\", \"spec\": {\"command\": \"python run_freeform_conll.py --seed {42,123,456,789} --gpu {0,1,2,3} --n_samples 8 --temperature 1.0\", \"server\": \"autodl-4x5090\", \"data_path\": \"data/conll2003/test.jsonl\", \"data_count\": 3453, \"model_name\": \"checkpoints/qwen3-8b-conll2003-merged\", \"seed\": \"42,123,456,789\"}, \"checkpoint_path\": \"N/A (inference-only experiment)\", \"log_path\": \"output/review_round9_experiments/freeform_conll/\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T03:04:40.278Z\", \"metrics\": {\"greedy_f1\": \"0.9035±0.0004\", \"oracle_f1\": \"0.9460±0.0023\", \"lp_range_median\": \"0.0581±0.0072\", \"rho_sj\": \"0.4606±0.0188\", \"rho_fk\": \"0.4372±0.0209\", \"rho_em\": \"0.4714±0.0168\", \"rho_vc\": \"0.4606±0.0138\", \"rho_lp\": \"0.3262±0.0120\", \"sel_f1_sj\": \"0.8994±0.0014\", \"sel_f1_vc\": \"0.9006±0.0026\", \"sel_f1_lp\": \"0.8958±0.0009\", \"seeds\": [42, 123, 456, 789], \"n_samples\": 8, \"temperature\": 1, \"instances\": 2756, \"gold_empty_filtered\": 697}}, \"exp_qwen3_4b_conll_merge_inference_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T19:42:42.107Z\", \"updated_at\": \"2026-05-15T20:07:12.593Z\", \"hypothesis\": \"CoNLL 4B checkpoint-4200 (best from resume training) merge + SCS inference. Replaces v1 which used checkpoint-3800 merged model. Cross-scale evidence for correlation-selection gap.\", \"spec\": {\"command\": \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && CUDA_VISIBLE_DEVICES=1 PYTHONPATH=code python code/run_mvp_pilot.py --model_path checkpoints/qwen3-4b-conll2003-merged-ckpt4200 --data_dir data/conll2003 --dataset conll2003 --subtask ner --n_samples 8 --temperature 1.0 --seed 42 --num_test 9999 --max_tokens 1024 --collect_logprobs --output_dir output/exp_qwen3_4b_conll_merge_inference_v2\", \"server\": \"autodl-5090\", \"data_path\": \"data/conll2003\", \"data_count\": 3453, \"model_name\": \"Qwen3-4B (LoRA merged, ckpt-4200)\", \"seed\": 42, \"checkpoint_source\": \"exp_qwen3_4b_conll_finetune_resume (checkpoint-4200)\"}, \"checkpoint_path\": \"N/A - duplicate\", \"log_path\": \"N/A - duplicate\", \"conclusion\": \"killed\", \"notes\": \"Superseded by exp_qwen3_4b_conll_scs_inference_v2. Output was empty (dead experiment), functionally duplicate.\", \"completed_at\": \"2026-05-15T20:03:47.431Z\"}, \"exp_qwen3_4b_scierc_merge_inference\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T19:42:43.332Z\", \"updated_at\": \"2026-05-15T20:04:15.433Z\", \"hypothesis\": \"SciERC 4B best checkpoint merge + SCS inference. Complete 2x2 scale matrix (4B SciERC cell). Cross-scale + cross-task evidence for correlation-selection gap.\", \"checkpoint_path\": \"N/A - superseded\", \"log_path\": \"N/A - superseded\", \"conclusion\": \"killed\", \"notes\": \"Superseded by exp_qwen3_4b_scierc_scs_inference. Never launched (stuck in PREPARING). Killed during registry cleanup.\", \"completed_at\": \"2026-05-15T20:04:15.433Z\"}, \"exp_qwen3_4b_scierc_finetune_v3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T19:24:45.518Z\", \"updated_at\": \"2026-05-15T19:39:04.438Z\", \"spec\": {\"command\": \"llamafactory-cli train train_config_scierc_4b.yaml\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:2\"], \"pid\": \"226610\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_qwen3_4b_scierc_finetune_v3.log\", \"submitted_at\": \"2026-05-15T19:24:55.461Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/scierc/processed_data\", \"data_count\": 551, \"model_name\": \"Qwen3-4B\", \"seed\": 42, \"wall_clock_seconds\": 849.0, \"gpu_hours\": 0.24}, \"conclusion\": \"failed\", \"notes\": \"OOM on cuda:2 — freeform inference (seed789, 8B) 占满 GPU 2。未实际训练。重启为 v4 on cuda:0。\", \"completed_at\": \"2026-05-15T19:39:04.438Z\"}, \"exp_qwen3_4b_conll_finetune_resume\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T19:38:19.388Z\", \"updated_at\": \"2026-05-15T19:38:43.468Z\", \"hypothesis\": \"CoNLL 4B NER LoRA fine-tune resume from checkpoint-3800. Cross-scale evidence for correlation-selection gap.\", \"spec\": {\"hypothesis\": \"CoNLL2003 NER LoRA fine-tune with Qwen3-4B, resume from checkpoint-3800 to complete 5 epochs\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && llamafactory-cli train train_config_conll2003_4b_resume.yaml\\\"\", \"server\": \"autodl-5090\", \"gpu\": \"cuda:1\", \"data_path\": \"data/conll2003/llmfactory_train.json\", \"data_count\": 14042, \"model_name\": \"Qwen3-4B\", \"seed\": 42, \"resume_from\": \"checkpoint-3800\", \"lora_rank\": 32, \"lora_alpha\": 64, \"num_train_epochs\": 5, \"learning_rate\": 0.0002, \"batch_size\": \"2 x 8 grad_accum\", \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen3-4b-conll2003-lora\", \"best_checkpoint\": \"checkpoint-4200\", \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen3-4b-conll2003-lora/trainer_state.json\"}, \"conclusion\": \"success\", \"metrics\": {\"train_loss\": 0.001136, \"eval_loss\": 0.0225, \"best_global_step\": 4200, \"best_metric_eval_loss\": 0.0225, \"total_steps\": 4390, \"epochs\": 5, \"train_runtime_sec\": 1185.8, \"train_samples_per_second\": 59.2, \"resumed_from_step\": 3800}, \"completed_at\": \"2026-05-15T19:38:43.468Z\"}, \"exp_qwen3_4b_scierc_finetune_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T19:03:49.204Z\", \"updated_at\": \"2026-05-15T19:24:32.466Z\", \"spec\": {\"command\": \"llamafactory-cli train train_config_scierc_4b.yaml\", \"server\": \"autodl-5090\", \"gpu\": \"cuda:3\", \"pid\": \"219830\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_qwen3_4b_scierc_finetune_v2.log\", \"submitted_at\": \"2026-05-15T19:05:31.524Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/scierc/processed_data\", \"data_count\": 1861, \"model_name\": \"Qwen3-4B\", \"seed\": 42, \"plan_id\": \"D096\", \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen3-4b-scierc-lora/\", \"wall_clock_seconds\": 1122.6, \"gpu_hours\": 0.31}, \"conclusion\": \"failed\", \"completed_at\": \"2026-05-15T19:24:14.124Z\", \"notes\": \"PID 219830 已死，仅完成 step 10，无 checkpoint。需彻底重启。\"}, \"exp_qwen3_4b_conll_finetune\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-15T17:18:35.501Z\", \"updated_at\": \"2026-05-15T19:10:24.822Z\", \"hypothesis\": \"Scale ablation: Qwen3-4B CoNLL NER LoRA fine-tune to provide cross-scale evidence (vs 8B). Verify correlation-selection gap, SJ>FK ordering, and LP compression generalize across model scale.\", \"reproduce\": {\"finished_at\": \"2026-05-15T18:45:42.215Z\"}, \"failure_reason\": \"\", \"completed_at\": \"2026-05-15T18:45:43.672Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-15T18:45:49.686191+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\"}}, \"spec\": {\"command\": \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && CUDA_VISIBLE_DEVICES=0 llamafactory-cli train train_config_conll2003_4b.yaml\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:0\"], \"data_path\": \"data/conll2003\", \"data_count\": 14041, \"model_name\": \"Qwen3-4B\", \"seed\": 42, \"plan_id\": \"D096\", \"log_path\": \"checkpoints/qwen3-4b-conll2003-lora/trainer_log.jsonl\", \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen3-4b-conll2003-lora\", \"lora_config\": {\"trainable_params\": \"66M / 4.09B (1.62%)\", \"target_modules\": \"q_proj, k_proj, v_proj, o_proj, gate_proj, up_proj, down_proj\", \"epochs\": 5, \"batch_size\": 16, \"total_steps\": 4390, \"enable_thinking\": false}}, \"conclusion\": \"success\", \"notes\": \"Training stopped at step 3920/4390 (89.3%, epoch 4.46/5). No error log or tmux session found. checkpoint-3800 is valid (adapter_model.safetensors 264MB, eval_loss=0.023). Proceeding with checkpoint-3800 for merge+inference.\", \"metrics\": {\"final_loss\": 0.0086, \"total_steps_completed\": 3920, \"total_steps_target\": 4390, \"epochs_completed\": 4.46, \"epochs_target\": 5, \"best_checkpoint\": \"checkpoint-3800\", \"note\": \"Training stopped at 89.3% completion (no error log found). Using checkpoint-3800 (loss ~0.01) for merge.\"}}, \"exp_freeform_seed789_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T19:02:03.813Z\", \"updated_at\": \"2026-05-15T19:06:44.537Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && python run_freeform_inference.py --seed 789 --num_samples 8 --temperature 1.0 --max_tokens 1024 --output_dir results/exp_freeform_ablation_seed789\\\"\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:2\"], \"pid\": \"218882\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_freeform_seed789_v2.log\", \"submitted_at\": \"2026-05-15T19:02:03.527Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"hypothesis\": \"Multi-seed free-form ablation (seed=789): third seed for 3-seed mean±σ statistical significance. Verify RE LP flip and NER gap stability.\", \"data_path\": \"data/scierc/processed_data\", \"data_count\": 551, \"model_name\": \"qwen3-8b-scierc-merged-v2\", \"seed\": 789, \"wall_clock_seconds\": 274.9, \"gpu_hours\": 0.08}, \"reproduce\": {\"finished_at\": \"2026-05-15T19:06:37.887Z\"}, \"failure_reason\": \"EXIT_CODE=143 (SIGTERM — graceful kill)\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-15T19:06:38.388Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-15T19:06:53.109123+00:00\"}]}}, \"exp_qwen3_4b_scierc_finetune\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T18:58:58.948Z\", \"updated_at\": \"2026-05-15T19:03:05.505Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && CUDA_VISIBLE_DEVICES=0 llamafactory-cli train train_config_scierc_4b.yaml\\\"\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:3\"], \"pid\": \"218258\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_qwen3_4b_scierc_finetune.log\", \"submitted_at\": \"2026-05-15T19:00:10.234Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 175.3, \"gpu_hours\": 0.05}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-15T19:03:05.505Z\"}, \"exp_lp_t07_scierc\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T15:34:12.094Z\", \"updated_at\": \"2026-05-15T16:30:35.531Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && PYTHONPATH=code python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc/processed_data --dataset scierc --subtask ner --n_samples 8 --temperature 0.7 --seed 42 --num_test 9999 --max_tokens 1024 --collect_logprobs --output_dir output/exp_lp_t07_scierc\\\"\", \"server\": \"autodl-5090\", \"data_path\": \"data/scierc/processed_data\", \"data_count\": 551, \"model_name\": \"Qwen3-8B (LoRA fine-tuned on SciERC, ft_002_v2 merged)\", \"seed\": 42, \"gpu\": \"cuda:1\", \"hyperparams\": {\"n_samples\": 8, \"temperature\": 0.7, \"max_tokens\": 1024}}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-15T16:28:29.563Z\"}, \"exp_lp_scierc_t07\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T15:34:06.918Z\", \"updated_at\": \"2026-05-15T16:03:13.881Z\", \"hypothesis\": \"LP T=0.7 推理：验证低温下 LP score compression 是否依然存在，强化 \\\"LP compression is model/task intrinsic\\\" claim。对比 T=1.0 的 LP range 分布。\", \"spec\": {\"command\": \"python run_sc_ie.py --dataset scierc --subtask ner --model qwen --n_samples 8 --temperature 0.7 --use_logprob --output_dir /root/autodl-tmp/struct_self_consist_ie/output/exp_lp_scierc_t07\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:1\"], \"pid\": \"196993\", \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_lp_scierc_t07/\", \"submitted_at\": \"2026-05-15T15:35:31.692Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"SciERC\", \"data_count\": 500, \"model_name\": \"Qwen3-8B\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_lp_scierc_t07/report.json\", \"wall_clock_seconds\": 1206.2, \"gpu_hours\": 0.34}, \"conclusion\": \"success\", \"metrics\": {\"ner_greedy_f1\": 0.662, \"ner_oracle_f1\": 0.764, \"ner_headroom_pp\": 10.2, \"ner_rho_sj_full\": 0.365, \"ner_rho_sj_cond\": 0.363, \"ner_rho_fk_full\": 0.289, \"ner_rho_fk_cond\": 0.255, \"lp_rho_full\": 0.249, \"lp_rho_cond\": 0.185, \"ner_rho_advantage\": 0.076, \"zero_f1_pct\": 11, \"full_n\": 529, \"cond_n\": 477, \"verdict\": \"success_supports_LP_compression_claim\"}, \"completed_at\": \"2026-05-15T15:55:37.889Z\"}, \"exp_re_scierc_seed456\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T15:40:40.607Z\", \"updated_at\": \"2026-05-15T15:55:41.890Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && CUDA_VISIBLE_DEVICES=3 PYTHONPATH=code python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc/processed_data --dataset scierc --subtask joint --n_samples 8 --temperature 1.0 --max_tokens 1024 --seed 456 --num_test 9999 --collect_logprobs --output_dir output/exp_re_scierc_seed456\\\"\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:3\"], \"pid\": \"199161\", \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_re_scierc_seed456/\", \"submitted_at\": \"2026-05-15T15:40:59.585Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"SciERC\", \"data_count\": 500, \"model_name\": \"Qwen3-8B (SciERC merged)\", \"seed\": 456, \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_re_scierc_seed456/report.json\", \"wall_clock_seconds\": 882.3, \"gpu_hours\": 0.25}, \"hypothesis\": \"SciERC RE 多种子验证 (seed456): 解决 R4-W1/R7-C1 single-seed RE 弱点。与 seed42 (exp_012_rerun_1024) 对齐，joint subtask N=8 T=1.0。目标: 3-seed RE selection F1 mean±σ。\", \"conclusion\": \"negative\", \"metrics\": {\"ner_greedy_f1\": 0.664, \"ner_oracle_f1\": 0.775, \"ner_headroom_pp\": 11.1, \"ner_rho_sj_cond\": 0.283, \"ner_rho_fk_cond\": 0.145, \"re_greedy_f1\": 0.417, \"re_oracle_f1\": 0.581, \"re_headroom_pp\": 16.3, \"re_rho_sj_cond\": 0.315, \"re_rho_fk_cond\": 0.123, \"re_zero_f1_pct\": 45.3, \"verdict\": \"FAIL_re_rho_sj_below_040\"}, \"completed_at\": \"2026-05-15T15:55:41.890Z\"}, \"exp_re_scierc_seed123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T15:40:38.271Z\", \"updated_at\": \"2026-05-15T15:55:40.000Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && CUDA_VISIBLE_DEVICES=2 PYTHONPATH=code python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc/processed_data --dataset scierc --subtask joint --n_samples 8 --temperature 1.0 --max_tokens 1024 --seed 123 --num_test 9999 --collect_logprobs --output_dir output/exp_re_scierc_seed123\\\"\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:2\"], \"pid\": \"199021\", \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_re_scierc_seed123/\", \"submitted_at\": \"2026-05-15T15:40:58.073Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"SciERC\", \"data_count\": 500, \"model_name\": \"Qwen3-8B (SciERC merged)\", \"seed\": 123, \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_re_scierc_seed123/report.json\", \"wall_clock_seconds\": 881.9, \"gpu_hours\": 0.24}, \"hypothesis\": \"SciERC RE 多种子验证 (seed123): 解决 R4-W1/R7-C1 single-seed RE 弱点。与 seed42 (exp_012_rerun_1024) 对齐，joint subtask N=8 T=1.0。目标: 3-seed RE selection F1 mean±σ。\", \"conclusion\": \"negative\", \"metrics\": {\"ner_greedy_f1\": 0.663, \"ner_oracle_f1\": 0.786, \"ner_headroom_pp\": 12.3, \"ner_rho_sj_cond\": 0.404, \"ner_rho_fk_cond\": 0.182, \"re_greedy_f1\": 0.42, \"re_oracle_f1\": 0.593, \"re_headroom_pp\": 17.3, \"re_rho_sj_cond\": 0.277, \"re_rho_fk_cond\": 0.063, \"re_zero_f1_pct\": 43.6, \"verdict\": \"FAIL_re_rho_sj_below_040\"}, \"completed_at\": \"2026-05-15T15:55:40.000Z\"}, \"exp_017_llama_conll_n8_t07\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T15:29:34.595Z\", \"updated_at\": \"2026-05-15T15:46:22.722Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && CUDA_VISIBLE_DEVICES=0 PYTHONPATH=code python code/run_mvp_pilot.py --model_path checkpoints/llama3.1-8b-conll2003-merged --data_dir data/conll2003 --dataset conll2003 --subtask ner --n_samples 8 --temperature 0.7 --seed 42 --num_test 9999 --max_tokens 1024 --collect_logprobs --output_dir output/exp_017_llama_conll_n8_t07\\\"\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:0\"], \"pid\": \"195927\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_017_llama_conll_n8_t07.log\", \"submitted_at\": \"2026-05-15T15:31:17.989Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 881.3, \"gpu_hours\": 0.24}, \"hypothesis\": \"LLaMA CoNLL N=8 T=0.7 防御性实验：填补\\\"LLaMA 仅在 SciERC 上测过\\\"的弱点，验证 cross-model consistency（vs Qwen CoNLL）。T=0.7 低温下 confidence signals 的 correlation-selection gap 是否依然存在。\", \"parent\": \"exp_017_llama_conll\", \"server\": \"autodl-5090\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"reproduce\": {\"server\": \"autodl-5090\", \"gpu\": \"cuda:0\", \"started_at\": \"2026-05-15T15:31:15.772Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && CUDA_VISIBLE_DEVICES=0 PYTHONPATH=code python code/run_mvp_pilot.py --model_path checkpoints/llama3.1-8b-conll2003-merged --data_dir data/conll2003 --dataset conll2003 --subtask ner --n_samples 8 --temperature 0.7 --seed 42 --num_test 9999 --max_tokens 1024 --collect_logprobs --output_dir output/exp_017_llama_conll_n8_t07\\\"\", \"finished_at\": \"2026-05-15T15:40:02.605Z\", \"training_hours\": 0.15}, \"pid\": \"195927\", \"log_path\": \"/root/runs/struct_self_consist_ie/exp_017_llama_conll_n8_t07.log\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T15:40:08.277684+00:00\"}]}, \"metrics\": {\"n_valid\": 2756, \"greedy_f1\": 0.9242, \"oracle_f1\": 0.9391, \"lp_range_median\": 1.1e-05, \"lp_tied_fraction_005\": 0.9579, \"signals\": {\"SJ\": {\"rho\": 0.3934, \"auroc\": 0.6506}, \"FK\": {\"rho\": 0.3879, \"auroc\": 0.6488}, \"VC\": {\"rho\": 0.375, \"auroc\": 0.6551}, \"EM\": {\"rho\": 0.3888, \"auroc\": 0.6494}, \"LP\": {\"rho\": 0.2951, \"auroc\": 0.7509}}, \"selection_f1\": {\"SJ\": 0.9247, \"FK\": 0.9254, \"VC\": 0.9264, \"EM\": 0.9255, \"LP\": 0.9248}}, \"conclusion\": \"success\", \"checkpoint_path\": \"N/A (inference-only)\", \"completed_at\": \"2026-05-15T15:45:59.311Z\"}, \"exp008_re_n16\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T12:09:50.987Z\", \"updated_at\": \"2026-05-15T12:41:39.774Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && mkdir -p output/exp008_re_n16 && CUDA_VISIBLE_DEVICES=2 PYTHONPATH=code python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc/processed_data --dataset scierc --subtask joint --n_samples 16 --temperature 1.0 --seed 42 --output_dir output/exp008_re_n16 --collect_logprobs 2>&1 | tee output/exp008_re_n16/run.log\\\"\", \"server\": \"gpu-5090-4x-2\", \"gpu\": [\"cuda:2\"], \"pid\": \"53600\", \"log_path\": \"~/runs/struct_self_consist_ie/exp008_re_n16.log\", \"submitted_at\": \"2026-05-14T12:15:14.917Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"failure_reason\": \"Superseded by exp_008_re_n16_v2 (full 551-instance run on autodl-5090)\", \"wall_clock_seconds\": 87984.9, \"gpu_hours\": 24.44}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-15T12:41:39.774Z\"}, \"exp001_seed456\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T12:09:48.078Z\", \"updated_at\": \"2026-05-15T12:41:32.192Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && mkdir -p output/exp001_n16_seed456 && CUDA_VISIBLE_DEVICES=1 PYTHONPATH=code python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc/processed_data --dataset scierc --subtask joint --n_samples 16 --temperature 1.0 --seed 456 --output_dir output/exp001_n16_seed456 --collect_logprobs 2>&1 | tee output/exp001_n16_seed456/run.log\\\"\", \"server\": \"gpu-5090-4x-2\", \"gpu\": [\"cuda:1\"], \"pid\": \"50302\", \"log_path\": \"~/runs/struct_self_consist_ie/exp001_seed456.log\", \"submitted_at\": \"2026-05-14T12:12:41.206Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"failure_reason\": \"Superseded by exp_001_seed456_v2_ner (NER-only on autodl-5090)\", \"wall_clock_seconds\": 88131.0, \"gpu_hours\": 24.48}, \"conclusion\": \"killed\", \"failure_reason\": \"superseded by v2\", \"completed_at\": \"2026-05-15T12:41:32.192Z\"}, \"exp001_seed123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T12:09:45.739Z\", \"updated_at\": \"2026-05-15T12:41:31.168Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && mkdir -p output/exp001_n16_seed123 && CUDA_VISIBLE_DEVICES=0 PYTHONPATH=code python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc/processed_data --dataset scierc --subtask joint --n_samples 16 --temperature 1.0 --seed 123 --output_dir output/exp001_n16_seed123 --collect_logprobs 2>&1 | tee output/exp001_n16_seed123/run.log\\\"\", \"server\": \"gpu-5090-4x-2\", \"gpu\": [\"cuda:0\"], \"pid\": \"48530\", \"log_path\": \"~/runs/struct_self_consist_ie/exp001_seed123.log\", \"submitted_at\": \"2026-05-14T12:09:45.674Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"failure_reason\": \"Superseded by exp_001_seed123_v2 (NER-only, 551 instances on autodl-5090)\", \"wall_clock_seconds\": 88305.5, \"gpu_hours\": 24.53}, \"conclusion\": \"killed\", \"failure_reason\": \"superseded by v2\", \"completed_at\": \"2026-05-15T12:41:31.168Z\"}, \"exp_001_n16_seed456_full\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T12:44:31.348Z\", \"updated_at\": \"2026-05-15T12:41:30.065Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && CUDA_VISIBLE_DEVICES=1 python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc/processed_data --dataset scierc --subtask joint --n_samples 16 --temperature 1.0 --seed 456 --collect_logprobs --num_test 9999 --output_dir output/exp001_n16_seed456/\\\"\", \"server\": \"gpu-5090-4x-2\", \"gpu\": [\"cuda:1\"], \"pid\": \"62170\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_001_n16_seed456_full.log\", \"submitted_at\": \"2026-05-14T12:44:31.087Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"failure_reason\": \"Superseded by exp_001_seed456_v2_ner (NER-only on autodl-5090)\", \"wall_clock_seconds\": 86219.0, \"gpu_hours\": 23.95}, \"conclusion\": \"killed\", \"failure_reason\": \"superseded by v2\", \"completed_at\": \"2026-05-15T12:41:30.065Z\"}, \"exp_001_n16_seed123_full\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T12:43:47.915Z\", \"updated_at\": \"2026-05-15T12:41:29.068Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && CUDA_VISIBLE_DEVICES=0 python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc/processed_data --dataset scierc --subtask joint --n_samples 16 --temperature 1.0 --seed 123 --collect_logprobs --num_test 9999 --output_dir output/exp001_n16_seed123_full/\\\"\", \"server\": \"gpu-5090-4x-2\", \"gpu\": [\"cuda:0\"], \"pid\": \"61812\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_001_n16_seed123_full.log\", \"submitted_at\": \"2026-05-14T12:44:06.059Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"failure_reason\": \"Superseded by exp_001_seed123_v2 (NER-only on autodl-5090)\", \"wall_clock_seconds\": 86243.0, \"gpu_hours\": 23.96}, \"conclusion\": \"killed\", \"failure_reason\": \"superseded by v2\", \"completed_at\": \"2026-05-15T12:41:29.068Z\"}, \"exp_007_ner_llama\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T11:42:21.510Z\", \"updated_at\": \"2026-05-15T12:41:27.410Z\", \"spec\": {\"description\": \"Fine-tune LLaMA-3.1-8B on SciERC + NER pilot (N=8, T=0.7). Model-agnostic validation.\", \"hypothesis\": \"SJ advantage is model-agnostic, not Qwen3-specific\", \"plan_id\": \"exp-007\", \"claim\": 1, \"model_name\": \"llama-3.1-8b-instruct (new fine-tune)\", \"dataset\": \"SciERC\", \"priority\": \"P0\", \"failure_reason\": \"Superseded by exp_007_ner_multi_model + exp_007_llama_inference (completed on autodl-5090)\"}, \"conclusion\": \"killed\", \"failure_reason\": \"superseded by exp_007_llama_inference (DONE)\", \"notes\": \"Completed as exp_007_llama_n16 on autodl-5090. Registry status corrected.\", \"completed_at\": \"2026-05-15T12:41:27.410Z\"}, \"exp_002_merge_conll2003\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T12:25:56.211Z\", \"updated_at\": \"2026-05-15T12:41:26.419Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && CUDA_VISIBLE_DEVICES=0 llamafactory-cli export export_config_conll2003.yaml > /tmp/merge_conll2003.log 2>&1 && echo 'MERGE_DONE' >> /tmp/merge_conll2003.log\\\"\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:0\"], \"pid\": \"57524\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_002_merge_conll2003.log\", \"submitted_at\": \"2026-05-14T12:25:56.139Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"failure_reason\": \"Superseded by exp_002_ner_conll2003 (completed on autodl-5090)\", \"wall_clock_seconds\": 87330.3, \"gpu_hours\": 24.26}, \"conclusion\": \"killed\", \"failure_reason\": \"superseded by exp_002_ner_conll2003 (DONE)\", \"notes\": \"Completed as exp_002_conll_n16 on autodl-5090. Registry status corrected.\", \"completed_at\": \"2026-05-15T12:41:26.419Z\"}, \"exp_019_supervised_verifier\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T10:08:54.395Z\", \"updated_at\": \"2026-05-15T12:40:53.995Z\", \"spec\": {\"hypothesis\": \"Supervised verifier (DeBERTa-v3-large) can close the correlation-selection gap, proving the gap is closable with supervision\", \"plan_id\": \"exp-019\", \"model_name\": \"microsoft/deberta-v3-large\", \"data_path\": \"output/exp_012_rerun_1024/samples.jsonl\", \"data_count\": 551, \"seed\": 42}, \"conclusion\": \"killed\", \"notes\": \"Cancelled by Director: DDL risk too high (3-4 days for implementation+training+eval+paper), scope creep for analytical paper, free-form ablation already provides sufficient mechanistic evidence\", \"completed_at\": \"2026-05-15T12:40:53.995Z\"}, \"exp_018_llama_scierc_seed456\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T06:07:15.150Z\", \"updated_at\": \"2026-05-15T06:22:40.868Z\", \"spec\": {\"hypothesis\": \"Multi-seed robustness: LLaMA SciERC N=8 seed=456, max_tokens=1024. Fresh inference (D066 decision: replace exp_007 re-analysis with independent replication).\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && PYTHONPATH=code python code/run_mvp_pilot.py --model_path checkpoints/llama3.1-8b-scierc-merged --data_dir data/scierc/processed_data --dataset scierc --subtask joint --n_samples 8 --temperature 1.0 --seed 456 --max_tokens 1024 --num_test 9999 --collect_logprobs --output_dir output/exp_018_llama_scierc_seed456_r1024\\\"\", \"server\": \"autodl-5090\", \"seed\": 456, \"model_name\": \"LLaMA-3.1-8B-SciERC-merged\", \"model_path\": \"checkpoints/llama3.1-8b-scierc-merged\", \"dataset\": \"SciERC\", \"subtask\": \"joint\", \"data_path\": \"data/scierc/processed_data\", \"data_count\": 551, \"N\": 8, \"T\": 1, \"max_tokens\": 1024, \"is_new_inference\": true, \"checkpoint_path\": \"output/exp_018_llama_scierc_seed456_r1024/\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_018_llama_scierc_seed456_r1024.log\"}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-15T06:08:05.756Z\", \"notes\": \"SUPERSEDED by exp_018_llama_scierc_seed456_r1024 (D066). Original data was re-analysis of exp_007_llama_seed456, not independent inference. Fresh rerun with explicit max_tokens=1024 now canonical.\"}, \"exp_002_conll_n16_r1024\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T22:16:57.682Z\", \"updated_at\": \"2026-05-15T01:20:53.108Z\", \"spec\": {\"hypothesis\": \"D054 rerun: max_tokens=1024. Verify truncation impact on Qwen CoNLL N=16.\", \"parent\": \"exp_002_conll_n16\", \"model_name\": \"qwen3-8b-conll2003-merged\", \"dataset\": \"CoNLL-2003\", \"seed\": 42, \"server\": \"autodl-5090\", \"command\": \"CUDA_VISIBLE_DEVICES=2 python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-conll2003-merged --data_dir data/conll2003 --dataset conll2003 --subtask ner --n_samples 16 --temperature 1.0 --seed 42 --num_test 9999 --max_tokens 1024 --collect_logprobs --output_dir output/exp_002_conll_n16_r1024\", \"data_path\": \"data/conll2003\", \"data_count\": 3453}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-15T01:20:53.108Z\"}, \"exp_007_llama_n16_r1024\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T22:16:59.685Z\", \"updated_at\": \"2026-05-15T01:20:52.194Z\", \"spec\": {\"hypothesis\": \"D054 rerun: max_tokens=1024. Verify truncation impact on LLaMA SciERC N=16.\", \"parent\": \"exp_007_llama_n16\", \"model_name\": \"llama3.1-8b-scierc-merged\", \"dataset\": \"SciERC\", \"seed\": 42, \"server\": \"autodl-5090\", \"command\": \"CUDA_VISIBLE_DEVICES=3 PYTHONPATH=code python code/run_mvp_pilot.py --model_path checkpoints/llama3.1-8b-scierc-merged --data_dir data/scierc/processed_data --dataset scierc --subtask ner --n_samples 16 --temperature 1.0 --seed 42 --num_test 9999 --max_tokens 1024 --collect_logprobs --output_dir output/exp_007_llama_n16_r1024\", \"data_path\": \"data/scierc/processed_data\", \"data_count\": 9999}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-15T01:20:52.194Z\"}, \"exp_001_seed123_v2_r1024\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T22:16:54.442Z\", \"updated_at\": \"2026-05-15T01:20:49.812Z\", \"spec\": {\"hypothesis\": \"D054 rerun: max_tokens=1024. Verify truncation impact on Qwen SciERC N=16 seed123.\", \"parent\": \"exp_001_seed123_v2\", \"model_name\": \"qwen3-8b-scierc-merged-v2\", \"dataset\": \"SciERC\", \"seed\": 123, \"server\": \"autodl-5090\", \"command\": \"CUDA_VISIBLE_DEVICES=1 PYTHONPATH=code python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc/processed_data --dataset scierc --subtask ner --n_samples 16 --temperature 1.0 --seed 123 --num_test 9999 --max_tokens 1024 --collect_logprobs --output_dir output/exp_001_seed123_v2_r1024\", \"data_path\": \"data/scierc/processed_data\", \"data_count\": 529}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-15T01:20:49.812Z\"}, \"exp_001_seed456_v2_ner_r1024\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T22:16:55.975Z\", \"updated_at\": \"2026-05-15T01:20:48.914Z\", \"spec\": {\"hypothesis\": \"D054 rerun: max_tokens=1024. Verify truncation impact on Qwen SciERC N=16 seed456.\", \"parent\": \"exp_001_seed456_v2_ner\", \"model_name\": \"qwen3-8b-scierc-merged-v2\", \"dataset\": \"SciERC\", \"seed\": 456, \"server\": \"autodl-5090\", \"command\": \"CUDA_VISIBLE_DEVICES=1 PYTHONPATH=code python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc/processed_data --dataset scierc --subtask ner --n_samples 16 --temperature 1.0 --seed 456 --num_test 9999 --max_tokens 1024 --collect_logprobs --output_dir output/exp_001_seed456_v2_ner_r1024\", \"data_path\": \"data/scierc/processed_data\", \"data_count\": 9999}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-15T01:20:48.914Z\"}, \"exp_001_seed42_v2_r1024\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T22:16:52.571Z\", \"updated_at\": \"2026-05-14T22:28:53.686Z\", \"spec\": {\"hypothesis\": \"D054 rerun: max_tokens=1024. Verify truncation impact on Qwen SciERC N=16 seed42.\", \"parent\": \"exp_001_seed42_v2\", \"model_name\": \"qwen3-8b-scierc-merged-v2\", \"dataset\": \"SciERC\", \"seed\": 42, \"server\": \"autodl-5090\", \"command\": \"CUDA_VISIBLE_DEVICES=0 PYTHONPATH=code python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc/processed_data --dataset scierc --subtask ner --n_samples 16 --temperature 1.0 --seed 42 --num_test 9999 --max_tokens 1024 --collect_logprobs --output_dir output/exp_001_seed42_v2_r1024\", \"data_path\": \"data/scierc/processed_data\", \"data_count\": 9999}, \"conclusion\": \"killed\", \"metrics\": {\"greedy_f1\": 0.6647, \"oracle_f1\": 0.8106, \"softjaccard_rho_full\": 0.3928, \"fleiss_rho_full\": 0.2489, \"logprob_rho_full\": 0.2136, \"softjaccard_rho_cond\": 0.3455, \"fleiss_rho_cond\": 0.163, \"logprob_rho_cond\": 0.1624, \"verdict\": \"MARGINAL\"}, \"checkpoint_path\": \"output/exp_001_seed42_v2_r1024\", \"log_path\": \"output/exp_001_seed42_v2_r1024/run.log\", \"completed_at\": \"2026-05-14T22:27:43.836Z\"}, \"exp_017_llama_conll_n16_s456\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T19:23:21.987Z\", \"updated_at\": \"2026-05-14T20:24:45.875Z\", \"hypothesis\": \"LLaMA CoNLL N=16 seed=456: structural>surface ranking preserved across seeds, complementing Qwen SciERC 3-seed protocol\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 python code/run_mvp_pilot.py --model_path checkpoints/llama3.1-8b-conll2003-merged --data_dir data/conll2003 --dataset conll2003 --subtask ner --n_samples 16 --temperature 1.0 --seed 456 --collect_logprobs --num_test 9999 --output_dir output/exp_017_llama_conll_n16_s456\", \"server\": \"autodl-5090\", \"data_path\": \"data/conll2003\", \"data_count\": 3453, \"model_name\": \"llama3.1-8b-conll2003-merged\", \"seed\": 456}, \"metrics\": {\"greedy_f1\": 0.9243, \"oracle_f1\": 0.9488, \"oracle_headroom\": 0.0245, \"n_instances\": 3453, \"n_valid\": 2756, \"n_conditional\": 2642, \"structural_beats_surface\": true, \"full\": {\"SJ_rho\": 0.4552, \"SJ_AUROC\": 0.7288, \"SJ_ECE\": 0.1134, \"FK_rho\": 0.4478, \"FK_AUROC\": 0.7248, \"FK_ECE\": 0.109, \"logprob_rho\": 0.3078, \"logprob_AUROC\": 0.7612, \"logprob_ECE\": 0.1289, \"EM_rho\": 0.452, \"EM_AUROC\": 0.7275, \"EM_ECE\": 0.1082, \"voting_conf_rho\": 0.4571, \"voting_conf_AUROC\": 0.7348, \"voting_conf_ECE\": 0.0863}, \"conditional\": {\"SJ_rho\": 0.4505, \"SJ_AUROC\": 0.7449, \"SJ_ECE\": 0.0826, \"FK_rho\": 0.4422, \"FK_AUROC\": 0.7401, \"FK_ECE\": 0.0835, \"logprob_rho\": 0.3242, \"logprob_AUROC\": 0.8067, \"logprob_ECE\": 0.0921, \"EM_rho\": 0.451, \"EM_AUROC\": 0.745, \"EM_ECE\": 0.0756, \"voting_conf_rho\": 0.3962, \"voting_conf_AUROC\": 0.7202, \"voting_conf_ECE\": 0.0746}, \"best_of_n\": {\"greedy\": 0.9243, \"random_avg\": 0.9215, \"sj_best\": 0.9243, \"logprob_best\": 0.9243, \"voting_conf_best\": 0.9243, \"oracle\": 0.9488}, \"n8_vs_n16_delta\": {\"full_SJ_rho_delta\": 0.0238, \"full_FK_rho_delta\": 0.0201, \"full_logprob_rho_delta\": 0.0006, \"full_EM_rho_delta\": 0.0214, \"full_voting_conf_rho_delta\": 0.0315, \"cond_SJ_rho_delta\": 0.0149, \"cond_FK_rho_delta\": 0.0112, \"cond_logprob_rho_delta\": -0.004, \"cond_EM_rho_delta\": 0.0107, \"cond_voting_conf_rho_delta\": 0.0219}}, \"checkpoint_path\": \"output/exp_017_llama_conll_n16_s456/samples.jsonl\", \"log_path\": \"output/exp_017_llama_conll_n16_s456/all_signals_report.json\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T20:24:45.875Z\"}, \"exp_017_llama_conll_n16_s123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T19:23:21.084Z\", \"updated_at\": \"2026-05-14T19:43:06.607Z\", \"hypothesis\": \"LLaMA CoNLL N=16 seed=123: structural>surface ranking preserved across seeds, complementing Qwen SciERC 3-seed protocol\", \"spec\": {\"hypothesis\": \"LLaMA CoNLL-2003 NER N=16 seed=123: cross-seed robustness check against N=8 seed=42 baseline (exp_017_llama_conll_infer)\", \"command\": \"CUDA_VISIBLE_DEVICES=1 python code/run_mvp_pilot.py --model_path checkpoints/llama3.1-8b-conll2003-merged --data_dir data/conll2003 --dataset conll2003 --subtask ner --n_samples 16 --temperature 1.0 --seed 123 --collect_logprobs --num_test 9999 --output_dir output/exp_017_llama_conll_n16_s123\", \"server\": \"autodl-5090\", \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/data/conll2003\", \"data_count\": 3453, \"model_name\": \"llama3.1-8b-conll2003-merged\", \"seed\": 123, \"checkpoint_source\": \"checkpoints/llama3.1-8b-conll2003-merged\", \"eval_data\": \"data/conll2003\", \"checkpoint_path\": \"output/exp_017_llama_conll_n16_s123/samples.jsonl\", \"log_path\": \"output/exp_017_llama_conll_n16_s123.log\"}, \"metrics\": {\"greedy_f1\": 0.9266, \"oracle_f1\": 0.9497, \"oracle_headroom\": 0.0231, \"n_instances\": 3453, \"n_valid\": 2756, \"n_conditional\": 2642, \"structural_beats_surface\": true, \"full\": {\"SJ_rho\": 0.4698, \"SJ_AUROC\": 0.7402, \"SJ_ECE\": 0.1135, \"FK_rho\": 0.4594, \"FK_AUROC\": 0.7351, \"FK_ECE\": 0.1114, \"logprob_rho\": 0.3161, \"logprob_AUROC\": 0.768, \"logprob_ECE\": 0.129, \"EM_rho\": 0.4676, \"EM_AUROC\": 0.7399, \"EM_ECE\": 0.1082, \"voting_conf_rho\": 0.4612, \"voting_conf_AUROC\": 0.7429, \"voting_conf_ECE\": 0.0832}, \"conditional\": {\"SJ_rho\": 0.4712, \"SJ_AUROC\": 0.7609, \"SJ_ECE\": 0.0828, \"FK_rho\": 0.4595, \"FK_AUROC\": 0.7547, \"FK_ECE\": 0.0858, \"logprob_rho\": 0.3314, \"logprob_AUROC\": 0.8134, \"logprob_ECE\": 0.0922, \"EM_rho\": 0.4732, \"EM_AUROC\": 0.7626, \"EM_ECE\": 0.075, \"voting_conf_rho\": 0.4086, \"voting_conf_AUROC\": 0.7338, \"voting_conf_ECE\": 0.0706}, \"best_of_n\": {\"greedy\": 0.9242, \"random_avg\": 0.9216, \"sj_best\": 0.9247, \"logprob_best\": 0.9253, \"voting_conf_best\": 0.9255, \"oracle\": 0.9486}, \"n8_vs_n16_delta\": {\"full_SJ_rho_delta\": 0.0384, \"full_FK_rho_delta\": 0.0317, \"full_logprob_rho_delta\": 0.0089, \"full_SJ_AUROC_delta\": 0.0363, \"full_FK_AUROC_delta\": 0.0325, \"full_logprob_AUROC_delta\": 0.007, \"cond_SJ_rho_delta\": 0.0356, \"cond_FK_rho_delta\": 0.0285, \"cond_logprob_rho_delta\": 0.0032}}, \"log_path\": \"output/exp_017_llama_conll_n16_s123.log\", \"checkpoint_path\": \"output/exp_017_llama_conll_n16_s123/samples.jsonl\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T19:43:06.607Z\"}, \"exp_008_re_n16_full\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T12:45:10.852Z\", \"updated_at\": \"2026-05-14T17:51:43.957Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && CUDA_VISIBLE_DEVICES=2 python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc/processed_data --dataset scierc --subtask re --n_samples 16 --temperature 1.0 --seed 42 --collect_logprobs --num_test 9999 --output_dir output/exp008_re_n16/\\\"\", \"server\": \"gpu-5090-4x-2\", \"gpu\": [\"cuda:2\"], \"pid\": \"62585\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_008_re_n16_full.log\", \"submitted_at\": \"2026-05-14T12:45:10.764Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 18393.2, \"gpu_hours\": 5.11}, \"conclusion\": \"killed\", \"failure_reason\": \"superseded by exp_008_re_n16_t10_full (full 551-instance RE-only run on autodl-5090)\", \"completed_at\": \"2026-05-14T17:51:43.957Z\"}, \"exp_001_n16_seed123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T12:10:29.393Z\", \"updated_at\": \"2026-05-14T12:42:58.393Z\", \"spec\": {\"command\": \"python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc/processed_data --dataset scierc --subtask joint --n_samples 16 --temperature 1.0 --seed 123 --collect_logprobs\", \"server\": \"gpu-5090-4x-2\", \"data_path\": \"data/scierc/processed_data\", \"data_count\": 551, \"model_name\": \"qwen3-8b-scierc-merged-v2\", \"seed\": 123, \"num_instances\": 200, \"partial\": true, \"note\": \"Only 200/551 instances due to --num_test default bug. Needs full rerun.\"}, \"metrics\": {\"ner\": {\"greedy_f1\": 0.655, \"oracle_f1\": 0.8028, \"headroom\": 0.1478, \"rho_sj_full\": 0.4076, \"rho_fk_full\": 0.2799, \"rho_logprob_full\": 0.3189, \"rho_sj_cond\": 0.4271, \"rho_fk_cond\": 0.2743, \"rho_logprob_cond\": 0.2835, \"sj_beats_fk\": true, \"rho_advantage\": 0.1277}, \"re\": {\"greedy_f1\": 0.4243, \"oracle_f1\": 0.6771, \"headroom\": 0.2528, \"rho_sj_full\": 0.2943, \"rho_fk_full\": 0.2657, \"rho_logprob_full\": 0.3005, \"rho_sj_cond\": 0.4003, \"rho_fk_cond\": 0.313, \"rho_logprob_cond\": 0.2317, \"sj_beats_fk\": true, \"rho_advantage\": 0.0286}, \"verdict\": \"FAIL\"}, \"conclusion\": \"success\", \"checkpoint_path\": \"N/A\", \"log_path\": \"output/exp001_n16_seed123/\", \"completed_at\": \"2026-05-14T12:28:38.104Z\"}, \"exp_016_signal_ensemble\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T12:15:23.771Z\", \"updated_at\": \"2026-05-14T12:42:55.931Z\", \"spec\": {\"command\": \"python code/analyze_exp016_ensemble.py\", \"server\": \"autodl-5090\", \"data_path\": \"output/exp_012_logprob/samples_with_logprobs.jsonl\", \"data_count\": 551, \"model_name\": \"N/A (CPU-only analysis)\", \"seed\": 42, \"checkpoint_source\": \"N/A\", \"eval_data\": \"pilot_004\", \"checkpoint_path\": \"N/A\", \"log_path\": \"output/exp016_signal_ensemble/\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T12:15:53.341Z\", \"metrics\": {\"sj_logprob_pearson_ner\": 0.57, \"sj_logprob_pearson_re\": 0.42, \"best_linear_ner\": {\"combo\": \"SJ+voting_conf\", \"alpha\": 0.3, \"rho\": 0.489}, \"best_linear_re\": {\"combo\": \"voting_conf+logprob\", \"alpha\": 0.6, \"rho\": 0.429}, \"ensemble_ner_auroc\": 0.735, \"ensemble_re_auroc\": 0.719, \"best_single_ner_auroc\": 0.7, \"best_single_re_auroc\": 0.721, \"ensemble_ner_delta\": 0.035, \"selection_f1_ner\": {\"greedy\": 0.609, \"logprob\": 0.609, \"sj\": 0.604, \"ensemble\": 0.604, \"voting\": 0.596, \"random\": 0.58, \"oracle\": 0.769}, \"selection_f1_re\": {\"logprob\": 0.397, \"greedy\": 0.374, \"sj\": 0.368, \"ensemble\": 0.367, \"voting\": 0.338, \"random\": 0.338, \"oracle\": 0.561}, \"diagnosis\": \"SJ+voting_conf linear combo boosts NER ρ to 0.489 (+23%). RE: logprob-best is ONLY method beating greedy (0.397 vs 0.374). Ensemble AUROC +0.035 on NER. Oracle gap still huge.\"}}, \"exp_001_ner_n16_scierc\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T11:42:10.898Z\", \"updated_at\": \"2026-05-14T12:42:49.592Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && CUDA_VISIBLE_DEVICES=0 python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc/processed_data --dataset scierc --subtask joint --n_samples 16 --temperature 1.0 --seed 42 --output_dir output/exp001_n16_seed42 --num_test 9999 --collect_logprobs 2>&1 | tee output/exp001_n16_seed42_run.log\\\"\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:0\"], \"pid\": \"54357\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_001_ner_n16_scierc.log\", \"submitted_at\": \"2026-05-14T12:15:46.646Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"server\": \"autodl-5090\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"reproduce\": {\"server\": \"autodl-5090\", \"gpu\": \"cuda:0\", \"started_at\": \"2026-05-14T11:43:48.643Z\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T11:55:45.664Z\", \"metrics\": {\"n_instances\": 551, \"ner_n\": 529, \"re_n\": 397, \"N\": 16, \"T\": 1, \"seed\": 42, \"full_test_set\": true, \"ner_voting_conf_rho\": 0.399, \"ner_sj_rho\": 0.398, \"ner_em_rho\": 0.339, \"ner_fk_rho\": 0.288, \"ner_logprob_rho\": 0.237, \"ner_voting_conf_auroc\": 0.704, \"ner_sj_auroc\": 0.697, \"ner_cond_em_rho\": 0.414, \"ner_cond_sj_rho\": 0.349, \"ner_cond_vc_rho\": 0.34, \"re_voting_conf_rho\": 0.38, \"re_logprob_rho\": 0.293, \"re_fk_rho\": 0.281, \"re_sj_rho\": 0.277, \"re_em_rho\": 0.148, \"re_voting_conf_auroc\": 0.699, \"re_cond_em_rho\": 0.475, \"re_cond_sj_rho\": 0.318, \"re_cond_vc_rho\": 0.35, \"re_cond_em_auroc\": 0.742, \"diagnosis\": \"551 instances T=1.0: voting_conf best on full set (NER 0.399, RE 0.380). EM SURPRISE best on conditional set (NER cond 0.414, RE cond 0.475). RE full FAIL (SJ 0.277 < 0.40). Previous N-scaling 'breakthrough' was artifact of 200 instances + T=0.7.\"}}, \"exp_002\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T12:39:53.226Z\", \"updated_at\": \"2026-05-14T12:40:17.202Z\", \"spec\": {\"command\": \"python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-conll2003-merged --dataset conll2003 --subtask ner --n_samples 8 --temperature 1.0 --collect_logprobs --num_test 99999\", \"server\": \"autodl-5090\", \"data_path\": \"data/conll2003\", \"data_count\": 3453, \"model_name\": \"qwen3-8b-conll2003-lora-merged\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen3-8b-conll2003-merged\", \"log_path\": \"/tmp/pilot_conll2003.log\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T12:40:08.402Z\", \"metrics\": {\"sj_rho_full\": 0.4357, \"sj_tau_full\": 0.3851, \"sj_auroc_full\": 0.8008, \"sj_rho_cond\": 0.4511, \"fk_rho_full\": 0.3998, \"fk_tau_full\": 0.3568, \"fk_auroc_full\": 0.7741, \"fk_rho_cond\": 0.4064, \"logprob_rho_full\": 0.3157, \"logprob_tau_full\": 0.2469, \"logprob_auroc_full\": 0.7532, \"logprob_rho_cond\": 0.3562, \"em_rho_full\": 0.4507, \"em_tau_full\": 0.4002, \"em_auroc_full\": 0.8156, \"em_rho_cond\": 0.4799, \"ev_rho_full\": 0.4237, \"ev_tau_full\": 0.3777, \"ev_auroc_full\": 0.7889, \"ev_rho_cond\": 0.4127, \"greedy_f1\": 0.9123, \"oracle_f1\": 0.9543, \"voting_f1\": 0.9141, \"oracle_headroom\": 0.042, \"sj_vs_logprob_delta_rho\": 0.12, \"sj_vs_logprob_ci_low\": 0.0881, \"sj_vs_logprob_ci_high\": 0.154, \"sj_vs_logprob_significant\": true, \"n_instances\": 3453, \"n_valid\": 2756, \"n_samples\": 8, \"temperature\": 1}}, \"exp_002_ner_conll2003\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T11:42:15.223Z\", \"updated_at\": \"2026-05-14T12:27:35.413Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && CUDA_VISIBLE_DEVICES=0 python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-conll2003-merged --data_dir data/conll2003 --dataset conll2003 --subtask ner --n_samples 8 --temperature 1.0 --max_tokens 1024 --output_dir output/exp002_conll2003 --num_test 99999 --seed 42 --collect_logprobs 2>&1 | tee /tmp/pilot_conll2003.log\\\"\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:0\"], \"pid\": \"58208\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_002_ner_conll2003.log\", \"submitted_at\": \"2026-05-14T12:27:35.337Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"server\": \"autodl-5090\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"reproduce\": {\"server\": \"autodl-5090\", \"gpu\": \"cuda:1\", \"started_at\": \"2026-05-14T11:43:49.959Z\"}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen3-8b-conll2003-lora\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_002_ner_conll2003.log\", \"completed_at\": \"2026-05-14T12:18:04.097Z\"}, \"exp_004_re_diagnostic\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T11:49:44.497Z\", \"updated_at\": \"2026-05-14T11:50:24.620Z\", \"spec\": {\"hypothesis\": \"RE diagnostic: per-relation-type breakdown reveals which types drive low RE rho; error propagation and threshold sensitivity clarify the gap between NER and RE consistency signals\", \"model_name\": \"N/A (reuse pilot_004 samples)\", \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/mvp_pilot_004\", \"data_count\": 551, \"server\": \"autodl-5090\", \"seed\": 42, \"parent\": \"mvp_pilot_004\", \"method\": \"Per-relation-type SJ/FK/voting rho, error propagation classification, threshold sensitivity, bootstrap CI, Fisher z-test NER vs RE\", \"command\": \"python3 code/analyze_exp004_re_diagnostic.py\", \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp004_re_diagnostic\", \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp004_re_diagnostic/\", \"checkpoint_source\": \"mvp_pilot_004\", \"eval_data\": \"scierc_test_551\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T11:50:04.662Z\", \"metrics\": {\"per_relation_type\": {\"HYPONYM-OF\": {\"n\": 36, \"rho_sj\": 0.545, \"rho_fk\": 0.646, \"rho_vc\": 0.628, \"mean_f1\": 0.513}, \"CONJUNCTION\": {\"n\": 86, \"rho_sj\": 0.383, \"rho_fk\": 0.35, \"rho_vc\": 0.484, \"mean_f1\": 0.48}, \"USED-FOR\": {\"n\": 299, \"rho_sj\": 0.236, \"rho_fk\": 0.255, \"rho_vc\": 0.286, \"mean_f1\": 0.422}, \"PART-OF\": {\"n\": 44, \"rho_sj\": 0.239, \"rho_fk\": 0.348, \"rho_vc\": 0.283, \"mean_f1\": 0.297}, \"EVALUATE-FOR\": {\"n\": 62, \"rho_sj\": 0.172, \"rho_fk\": 0.255, \"rho_vc\": 0.226, \"mean_f1\": 0.365}, \"COMPARE\": {\"n\": 35, \"rho_sj\": 0.168, \"rho_fk\": 0.184, \"rho_vc\": 0.18, \"mean_f1\": 0.453}, \"FEATURE-OF\": {\"n\": 50, \"rho_sj\": 0.004, \"rho_fk\": 0.052, \"rho_vc\": 0.014, \"mean_f1\": 0.254}}, \"error_propagation\": {\"total_fn\": 553, \"tail_error_pct\": 21.9, \"full_error_pct\": 21.7, \"head_error_pct\": 17.7, \"head_tail_error_pct\": 15.9, \"type_error_pct\": 8.3, \"worst_consistency\": \"head_type_error (sj=0.411)\", \"best_consistency\": \"head_error (sj=0.613)\"}, \"threshold_sensitivity\": {\"thr_0.00_rho_sj\": 0.3161, \"thr_0.00_rho_vc\": 0.3841, \"thr_0.00_n\": 313, \"thr_0.05_rho_sj\": 0.2682, \"thr_0.05_rho_vc\": 0.2364, \"thr_0.05_n\": 239}, \"bootstrap_ci_95\": {\"ner_sj\": [0.2946, 0.4586], \"ner_voting_conf\": [0.3048, 0.4656], \"re_sj\": [0.1422, 0.3391], \"re_voting_conf\": [0.1818, 0.3721], \"re_cond_sj\": [0.2161, 0.4102], \"re_cond_voting_conf\": [0.2825, 0.474]}, \"fisher_z_ner_vs_re\": {\"sj_z\": 2.31, \"sj_p\": 0.0209, \"sj_significant\": true, \"fk_z\": -0.31, \"fk_p\": 0.756, \"fk_significant\": false, \"voting_z\": 1.914, \"voting_p\": 0.0556, \"voting_significant\": false}, \"diagnosis\": \"FEATURE-OF is near-zero rho across all signals (n=50, F1=0.254). HYPONYM-OF strongest (rho_fk=0.646). Entity span errors (head+tail) account for 55.5% of RE FN. NER rho_sj significantly > RE rho_sj (p=0.021). Voting_conf is best RE signal in conditional set (rho=0.384).\"}}, \"exp_005\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T11:45:16.360Z\", \"updated_at\": \"2026-05-14T11:45:38.570Z\", \"spec\": {\"hypothesis\": \"Temperature sensitivity: systematic comparison of T=0.7 vs T=1.0 on all 5 confidence signals\", \"method\": \"CPU-only analysis from checkpoint metrics (pilot_004 T=1.0, pilot_005 T=0.7, exp_012/013/014)\", \"data_count\": 551, \"model_name\": \"Qwen3-8B-SciERC-LoRA-v2\", \"data_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/exp005_temperature/\", \"server\": \"local\", \"seed\": 42, \"parent\": \"mvp_pilot_004,mvp_pilot_005\", \"command\": \"python3 analyze_exp005_temperature.py\", \"checkpoint_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/exp005_temperature/\", \"log_path\": \"N/A\", \"checkpoint_source\": \"pilot_004+pilot_005 checkpoint metrics\", \"eval_data\": \"SciERC test set (n=551)\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T11:45:38.570Z\"}, \"exp_014_entity_majority_voting\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T10:53:21.203Z\", \"updated_at\": \"2026-05-14T11:33:30.085Z\", \"spec\": {\"hypothesis\": \"Entity-level majority voting confidence beats SJ as correlation signal\", \"model_name\": \"N/A (reuse pilot_004 samples)\", \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/mvp_pilot_004\", \"data_count\": 551, \"server\": \"autodl-5090\", \"seed\": 42, \"parent\": \"mvp_pilot_004\", \"method\": \"Per-entity voting across N=8 samples, consensus construction, confidence = mean voting rate\", \"command\": \"python code/analyze_entity_voting.py\", \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/mvp_pilot_004\", \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/mvp_pilot_004/exp014_entity_voting_report.json\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T11:18:09.468Z\", \"metrics\": {\"ner_full_rho\": 0.3915, \"ner_full_p\": 8.1e-21, \"ner_full_tau\": 0.2906, \"ner_full_auroc\": 0.7039, \"re_full_rho\": 0.3403, \"re_full_p\": 3.21e-12, \"re_full_tau\": 0.256, \"re_full_auroc\": 0.6668, \"ner_voting_f1\": 0.6246, \"ner_greedy_f1\": 0.6483, \"ner_oracle_f1\": 0.7793, \"re_voting_f1\": 0.3577, \"re_greedy_f1\": 0.4022, \"re_oracle_f1\": 0.5886, \"diagnosis\": \"Voting confidence BEATS SJ on both NER (rho 0.392 vs 0.383) and RE (0.340 vs 0.244). But voting as selection strategy LOSES to greedy.\"}}, \"exp_013_exact_match_voting\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T10:53:18.753Z\", \"updated_at\": \"2026-05-14T11:33:22.644Z\", \"spec\": {\"hypothesis\": \"Exact-match voting rate correlates with F1\", \"model_name\": \"N/A (reuse pilot_004 samples)\", \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/mvp_pilot_004\", \"data_count\": 551, \"server\": \"autodl-5090\", \"seed\": 42, \"parent\": \"mvp_pilot_004\", \"method\": \"Count exact-match duplicates across N=8 samples\", \"command\": \"python code/analyze_exact_match_voting.py\", \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/mvp_pilot_004\", \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/mvp_pilot_004/exp013_exact_match_report.json\"}, \"conclusion\": \"negative\", \"completed_at\": \"2026-05-14T11:18:09.026Z\", \"metrics\": {\"ner_full_rho\": 0.2941, \"ner_full_p\": 5.12e-12, \"ner_full_tau\": 0.2181, \"ner_full_auroc\": 0.6398, \"re_full_rho\": 0.1562, \"re_full_p\": 0.0018, \"re_full_tau\": 0.1185, \"re_full_auroc\": 0.5863, \"diagnosis\": \"EM between SJ and FK on NER, weakest on RE. Too coarse-grained.\"}}, \"exp_012_logprob_baseline\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T10:53:16.166Z\", \"updated_at\": \"2026-05-14T11:13:30.240Z\", \"spec\": {\"hypothesis\": \"Log-probability baseline: mean sequence log-prob correlates with F1 as well as or better than SJ\", \"model_name\": \"ft_002_v2 (qwen3-8b-scierc-merged-v2)\", \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/mvp_pilot_004\", \"data_count\": 551, \"server\": \"autodl-5090\", \"seed\": 42, \"parent\": \"mvp_pilot_004\", \"method\": \"vLLM forward pass for log-probs + Spearman rho + AUROC + Kendall tau\", \"command\": \"python3 code/extract_logprobs.py\", \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/mvp_pilot_004\", \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/mvp_pilot_004/logprob_analysis.log\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T11:06:42.542Z\", \"metrics\": {\"ner_full_rho_sj\": 0.3565, \"ner_full_rho_fk\": 0.2651, \"ner_full_rho_logprob\": 0.1396, \"ner_full_rho_greedy_logprob\": 0.1615, \"ner_full_tau_sj\": 0.2658, \"ner_full_tau_logprob\": 0.1006, \"ner_full_auroc_sj\": 0.6892, \"ner_full_auroc_fk\": 0.6292, \"ner_full_auroc_logprob\": 0.5907, \"ner_full_n\": 529, \"ner_sj_vs_logprob_delta\": 0.2169, \"re_full_rho_sj\": 0.2112, \"re_full_rho_fk\": 0.2528, \"re_full_rho_logprob\": 0.2467, \"re_full_auroc_sj\": 0.5916, \"re_full_auroc_fk\": 0.6262, \"re_full_auroc_logprob\": 0.6186, \"re_full_n\": 397, \"re_cond_rho_sj\": 0.3683, \"re_cond_rho_fk\": 0.3168, \"re_cond_rho_logprob\": 0.1457, \"re_cond_auroc_sj\": 0.6839, \"re_cond_auroc_logprob\": 0.5487, \"re_cond_n\": 296, \"diagnosis\": \"NER: SJ crushes logprob (rho +0.217). RE full: logprob slightly ahead. RE cond: SJ crushes logprob (rho +0.223). SJ unique value CONFIRMED.\"}}, \"mvp_pilot_005\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T09:14:09.456Z\", \"updated_at\": \"2026-05-14T09:47:06.597Z\", \"spec\": {\"hypothesis\": \"T=0.7 降低 RE zero rate，恢复 SJ>FK，rho_sj 可能 ≥ 0.30 (MARGINAL threshold)\", \"model_name\": \"Qwen3-8B-SciERC-LoRA-v2 (ft_002_v2 final)\", \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/data/scierc/processed_data\", \"data_count\": 551, \"server\": \"autodl-5090\", \"seed\": 42, \"parent\": \"ft_002_v2\", \"method\": \"N=8 sampling T=0.7 + XGrammar + span realignment + max_tokens=1024 + gold-empty filter + conditional rho\", \"command\": \"CUDA_VISIBLE_DEVICES=0 python3 code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc/processed_data --dataset scierc --subtask joint --n_samples 8 --temperature 0.7 --max_tokens 1024 --output_dir output/mvp_pilot_005 --num_test 551 --seed 42 --tensor_parallel 1\", \"gpu\": \"cuda:0\", \"pid\": 32456, \"tmux_session\": \"mvp_pilot_005\", \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/mvp_pilot_005/train.log\"}, \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/mvp_pilot_005\", \"metrics\": {\"ner_greedy_f1\": 0.6619, \"ner_oracle_f1\": 0.7585, \"ner_headroom\": 0.0966, \"ner_fleiss_kappa_mean\": 0.4722, \"ner_soft_jaccard_mean\": 0.7757, \"ner_full_rho_sj\": 0.3875, \"ner_full_rho_fk\": 0.3211, \"ner_full_n\": 529, \"ner_cond_rho_sj\": 0.3868, \"ner_cond_rho_fk\": 0.305, \"ner_cond_n\": 504, \"ner_sj_beats_fk_full\": true, \"ner_sj_beats_fk_cond\": true, \"ner_rho_advantage\": 0.0664, \"ner_sample_f1_mean\": 0.6243, \"ner_sample_f1_std\": 0.3131, \"ner_sample_f1_pct_zero\": 11.2, \"ner_gold_empty_filtered\": 22, \"ner_all_zero_filtered\": 25, \"re_greedy_f1\": 0.4219, \"re_oracle_f1\": 0.5532, \"re_headroom\": 0.1313, \"re_fleiss_kappa_mean\": 0.3829, \"re_soft_jaccard_mean\": 0.687, \"re_full_rho_sj\": 0.2343, \"re_full_rho_fk\": 0.1835, \"re_full_n\": 397, \"re_cond_rho_sj\": 0.3716, \"re_cond_rho_fk\": 0.2533, \"re_cond_n\": 301, \"re_sj_beats_fk_full\": true, \"re_sj_beats_fk_cond\": true, \"re_rho_advantage\": 0.0508, \"re_sample_f1_mean\": 0.3782, \"re_sample_f1_std\": 0.3845, \"re_sample_f1_pct_zero\": 42.4, \"re_gold_empty_filtered\": 154, \"re_all_zero_filtered\": 96, \"parse_failures\": 0, \"verdict\": \"FAIL\", \"verdict_note\": \"RE full rho_sj=0.234 < 0.40; RE cond rho_sj=0.372 passes conditional but not full threshold\"}, \"conclusion\": \"negative\", \"completed_at\": \"2026-05-14T09:47:06.597Z\"}, \"e1_component_wise_re_sj\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T09:15:17.262Z\", \"updated_at\": \"2026-05-14T09:23:38.818Z\", \"spec\": {\"hypothesis\": \"RE SJ 乘性惩罚是 root cause：分解后 head_sj ρ ≈ NER ρ (~0.38)，tail_sj 和乘性组合拖低整体 ρ\", \"model_name\": \"N/A (reuse pilot_004 samples)\", \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/mvp_pilot_004\", \"data_count\": 397, \"server\": \"autodl-5090\", \"seed\": 42, \"parent\": \"mvp_pilot_004\", \"method\": \"Component-wise decomposition: head_sj, tail_sj, type_match 分别计算 Spearman ρ vs per-instance RE F1\", \"command\": \"python3 code/analyze_component_wise_re.py\", \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/mvp_pilot_004\", \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/mvp_pilot_004/e1_component_analysis.log\"}, \"conclusion\": \"negative\", \"metrics\": {\"full_head_sj_rho\": 0.21, \"full_tail_sj_rho\": 0.201, \"full_type_match_rho\": 0.201, \"full_multiplicative_rho\": 0.244, \"full_additive_rho\": 0.243, \"full_fleiss_kappa_rho\": 0.278, \"cond_head_sj_rho\": 0.27, \"cond_tail_sj_rho\": 0.259, \"cond_type_match_rho\": 0.252, \"cond_multiplicative_rho\": 0.316, \"cond_additive_rho\": 0.306, \"cond_fleiss_kappa_rho\": 0.307, \"n_full\": 397, \"n_conditional\": 313, \"diagnosis\": \"head_sj rho=0.210 FAR from NER rho=0.383. Multiplicative penalty hypothesis REJECTED. Problem is fundamental: span-level SJ lacks discriminative power for RE.\"}, \"completed_at\": \"2026-05-14T09:22:26.155Z\"}, \"mvp_pilot_004\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T08:51:38.203Z\", \"updated_at\": \"2026-05-14T09:10:40.918Z\", \"spec\": {\"hypothesis\": \"With improved RE quality (F1=41.8%), structural self-consistency (soft Jaccard) correlates with per-instance F1 better than surface Fleiss Kappa, reaching rho_sj >= 0.40 on RE\", \"model_name\": \"Qwen3-8B-SciERC-LoRA-v2 (ft_002_v2 final)\", \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/data/scierc/processed_data\", \"data_count\": 551, \"server\": \"autodl-5090\", \"seed\": 42, \"parent\": \"ft_002_v2\", \"method\": \"N=8 sampling T=1.0 + XGrammar + span realignment + max_tokens=1024 + gold-empty filter + conditional rho\", \"command\": \"CUDA_VISIBLE_DEVICES=0 python3 code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc/processed_data --dataset scierc --subtask joint --n_samples 8 --temperature 1.0 --max_tokens 1024 --output_dir output/mvp_pilot_004 --num_test 551 --seed 42 --tensor_parallel 1\", \"gpu\": \"cuda:0\", \"pid\": 31041, \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/mvp_pilot_004/mvp_pilot_004.log\", \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/mvp_pilot_004\"}, \"metrics\": {\"ner_greedy_f1\": 0.6671, \"ner_oracle_f1\": 0.7756, \"ner_headroom\": 0.1085, \"ner_fleiss_kappa_mean\": 0.4048, \"ner_soft_jaccard_mean\": 0.7008, \"ner_full_rho_fk\": 0.259, \"ner_full_rho_sj\": 0.3825, \"ner_full_n\": 529, \"ner_cond_rho_fk\": 0.2352, \"ner_cond_rho_sj\": 0.3762, \"ner_cond_n\": 508, \"ner_sj_beats_fk_full\": true, \"ner_sj_beats_fk_cond\": true, \"ner_sample_f1_mean\": 0.6084, \"ner_sample_f1_std\": 0.3174, \"ner_sample_f1_pct_zero\": 12.19, \"ner_gold_empty_filtered\": 22, \"ner_all_zero_filtered\": 21, \"re_greedy_f1\": 0.4208, \"re_oracle_f1\": 0.5882, \"re_headroom\": 0.1674, \"re_fleiss_kappa_mean\": 0.2996, \"re_soft_jaccard_mean\": 0.6114, \"re_full_rho_fk\": 0.2782, \"re_full_rho_sj\": 0.2441, \"re_full_n\": 397, \"re_cond_rho_fk\": 0.3067, \"re_cond_rho_sj\": 0.3161, \"re_cond_n\": 313, \"re_sj_beats_fk_full\": false, \"re_sj_beats_fk_cond\": true, \"re_sample_f1_mean\": 0.3612, \"re_sample_f1_std\": 0.383, \"re_sample_f1_pct_zero\": 44.3, \"re_gold_empty_filtered\": 154, \"re_all_zero_filtered\": 84, \"parse_failures\": 0, \"verdict\": \"FAIL\"}, \"conclusion\": \"negative\", \"completed_at\": \"2026-05-14T09:10:40.918Z\"}, \"ft_002_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T08:28:40.861Z\", \"updated_at\": \"2026-05-14T08:51:32.405Z\", \"spec\": {\"hypothesis\": \"Extended training (5 epochs, LoRA r=32) with OOM fix improves RE F1 above 40% threshold\", \"model_name\": \"Qwen/Qwen3-8B\", \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/data/llmfactory_train.json\", \"data_count\": 1861, \"server\": \"autodl-5090\", \"seed\": 42, \"parent\": \"ft_001\", \"method\": \"LoRA r=32 alpha=64, 5 epochs, batch=2 grad_accum=8 gradient_checkpointing=true\", \"gpu\": \"cuda:1\", \"pid\": 24947, \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/ft_002v2_train.log\", \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen3-8b-scierc-lora-v2\", \"command\": \"CUDA_VISIBLE_DEVICES=1 llamafactory-cli train train_config_v2.yaml\"}, \"conclusion\": \"success\", \"metrics\": {\"epoch\": 5, \"train_loss\": 0.0806, \"eval_loss\": 0.089, \"train_runtime\": \"28m41s\", \"train_samples_per_second\": 5.407, \"train_steps_per_second\": 0.34, \"total_steps\": 585, \"checkpoints\": [\"checkpoint-400\", \"checkpoint-500\", \"checkpoint-585\"], \"gate0_final_ner_f1\": 0.6615, \"gate0_final_re_f1\": 0.4177, \"gate0_final_parse_failures\": 0, \"gate0_final_ner_pass\": true, \"gate0_final_re_pass\": true, \"gate0_final_pass\": true, \"gate0_ckpt400_ner_f1\": 0.6475, \"gate0_ckpt400_re_f1\": 0.3793, \"gate0_ckpt400_parse_failures\": 0, \"gate0_ckpt400_verdict\": \"FAIL\", \"gate0_ckpt400_re_sample_f1_pct_zero\": 58.8, \"gate0_ckpt400_warning\": \">30% samples F1=0\"}, \"completed_at\": \"2026-05-14T08:51:32.405Z\"}, \"mvp_pilot_002\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T08:02:16.991Z\", \"updated_at\": \"2026-05-14T08:48:14.040Z\", \"spec\": {\"hypothesis\": \"Structural self-consistency (soft Jaccard) correlates with per-instance F1 better than surface Fleiss Kappa on fine-tuned Qwen3-8B SciERC\", \"model_name\": \"Qwen3-8B-SciERC-LoRA (ft_001)\", \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/data/scierc\", \"data_count\": 551, \"server\": \"autodl-5090\", \"seed\": 42, \"parent\": \"ft_001\", \"method\": \"N=8 sampling T=1.0 + XGrammar + span realignment + gold-empty filter + conditional rho\", \"gpu\": \"cuda:0\", \"note\": \"Rerun of mvp_pilot_001 which crashed silently\", \"command\": \"CUDA_VISIBLE_DEVICES=0 python3 code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-lora --data_dir data/scierc --dataset scierc --subtask joint --n_samples 8 --temperature 1.0 --max_tokens 512 --output_dir output/mvp_pilot_001 --num_test 551 --seed 42 --tensor_parallel 1\", \"failure_reason\": \"Worker used LoRA adapter path instead of merged model path; vLLM cannot load LoRA adapter directly\"}, \"conclusion\": \"failed\", \"completed_at\": \"2026-05-14T08:48:14.040Z\"}, \"ft_002\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T07:39:18.640Z\", \"updated_at\": \"2026-05-14T08:28:00.590Z\", \"spec\": {\"hypothesis\": \"Extended training (5 epochs, LoRA r=32) improves RE F1 above 40% threshold\", \"model_name\": \"Qwen/Qwen3-8B\", \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/data/llmfactory_train.json\", \"data_count\": 1861, \"server\": \"autodl-5090\", \"seed\": 42, \"parent\": \"ft_001\", \"method\": \"LoRA r=32 alpha=64, 5 epochs, relation direction hint\", \"command\": \"llamafactory-cli train /root/autodl-tmp/struct_self_consist_ie/train_config_v2.yaml\", \"gpu\": \"cuda:1\", \"pid\": 19666, \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/ft_002_train.log\", \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen3-8b-scierc-lora-v2\", \"total_steps\": 585, \"trainable_params\": \"87.3M\", \"estimated_runtime\": \"29min\"}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-14T08:02:30.390Z\", \"metrics\": {\"last_step\": 70, \"total_steps\": 585, \"progress_pct\": 11.97, \"last_loss\": 0.1134, \"last_lr\": 0.00019982, \"elapsed\": \"3m32s\", \"failure_reason\": \"OOM at step 73, batch_size=4 too large for 32GB RTX 5090\"}}, \"ft_001\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T06:04:28.030Z\", \"updated_at\": \"2026-05-14T08:27:58.182Z\", \"spec\": {\"hypothesis\": \"Fine-tuned Qwen3-8B on SciERC UIE can achieve NER F1 >= 73 and serve as base model for structural consistency MVP\", \"model_name\": \"Qwen/Qwen3-8B\", \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/data/scierc\", \"data_count\": 1861, \"server\": \"autodl-5090\", \"seed\": 42, \"method\": \"LoRA r=16 alpha=32\", \"framework\": \"LLaMA Factory 0.9.4\", \"command\": \"sft training qwen3-8b on scierc with lora\", \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen3-8b-scierc-lora/\", \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/checkpoints/ft_001_train.log\", \"train_loss\": 0.1099, \"eval_loss\": 0.0771, \"epoch\": 3, \"train_runtime\": \"0:17:49\", \"note\": \"gate0: NER PASS 60.4% / RE FAIL 33.8%\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T06:30:32.889Z\", \"metrics\": {\"train_loss\": 0.1099, \"eval_loss\": 0.0771, \"gate0_ner_f1_strict\": 0.1143, \"gate0_re_f1_strict\": 0.0125, \"gate0_ner_f1_text\": 0.606, \"gate0_re_f1_text\": 0.3392, \"gate0_offset_accuracy\": 0.1665, \"gate0_parse_failures\": 43, \"gate0_pass\": false, \"gate0_realigned_ner_f1\": 0.6045, \"gate0_realigned_re_f1\": 0.338, \"gate0_realigned_entity_offset_accuracy\": 1, \"gate0_realigned_relation_offset_accuracy\": 1, \"gate0_realigned_ner_pass\": true, \"gate0_realigned_re_pass\": false, \"gate0_realigned_pass\": false, \"gate0_ner_f1_delta_realign\": 0.4901, \"gate0_re_f1_delta_realign\": 0.3255, \"verdict_note\": \"partial: NER PASS (60.4%) / RE FAIL (33.8% < 40%)\"}}, \"mvp_pilot_003\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T08:21:09.847Z\", \"updated_at\": \"2026-05-14T08:21:44.983Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python code/run_mvp_pilot.py --model_path /root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen3-8b-scierc-merged --data_dir /root/autodl-tmp/struct_self_consist_ie/data/scierc/processed_data --dataset scierc --subtask joint --n_samples 8 --temperature 1.0 --max_tokens 1024 --output_dir /root/autodl-tmp/struct_self_consist_ie/output/mvp_pilot_003 --num_test 551 --seed 42 --tensor_parallel 1\", \"server\": \"autodl-5090\", \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/data/scierc/processed_data\", \"data_count\": 551, \"model_name\": \"qwen3-8b-scierc-merged\", \"seed\": 42}, \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/mvp_pilot_003.log\", \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/mvp_pilot_003\", \"conclusion\": \"negative\", \"completed_at\": \"2026-05-14T08:21:30.319Z\", \"metrics\": {\"ner_greedy_f1\": 0.6362, \"ner_oracle_f1\": 0.792, \"ner_headroom\": 0.1559, \"ner_fleiss_kappa_mean\": 0.2488, \"ner_soft_jaccard_mean\": 0.5066, \"ner_full_rho_sj\": 0.3808, \"ner_full_rho_fk\": 0.3362, \"ner_full_p_sj\": 1.07e-19, \"ner_full_p_fk\": 1.93e-15, \"ner_full_n\": 529, \"ner_cond_rho_sj\": 0.3836, \"ner_cond_rho_fk\": 0.3187, \"ner_cond_p_sj\": 1.83e-19, \"ner_cond_p_fk\": 1.33e-13, \"ner_cond_n\": 514, \"ner_sj_beats_fk_full\": true, \"ner_sj_beats_fk_cond\": true, \"ner_rho_advantage\": 0.0446, \"ner_sample_f1_mean\": 0.5153, \"ner_sample_f1_std\": 0.3334, \"ner_sample_f1_pct_zero\": 19.9, \"ner_gold_empty_filtered\": 22, \"ner_all_zero_filtered\": 15, \"re_greedy_f1\": 0.3774, \"re_oracle_f1\": 0.5939, \"re_headroom\": 0.2165, \"re_fleiss_kappa_mean\": 0.0879, \"re_soft_jaccard_mean\": 0.3958, \"re_full_rho_sj\": 0.2367, \"re_full_rho_fk\": 0.2221, \"re_full_p_sj\": 1.85e-06, \"re_full_p_fk\": 7.92e-06, \"re_full_n\": 397, \"re_cond_rho_sj\": 0.3004, \"re_cond_rho_fk\": 0.2374, \"re_cond_p_sj\": 2.25e-08, \"re_cond_p_fk\": 1.19e-05, \"re_cond_n\": 333, \"re_sj_beats_fk_full\": true, \"re_sj_beats_fk_cond\": true, \"re_rho_advantage\": 0.0146, \"re_sample_f1_mean\": 0.1977, \"re_sample_f1_std\": 0.3251, \"re_sample_f1_pct_zero\": 67.6, \"re_gold_empty_filtered\": 154, \"re_all_zero_filtered\": 64, \"parse_failures_stochastic\": 0, \"parse_failures_greedy\": 0, \"total_stochastic_samples\": 4408, \"total_greedy\": 551, \"verdict\": \"FAIL\", \"verdict_reason\": \"RE full rho_sj=0.2367 < 0.40 threshold; strong signal exists but below PASS bar\"}}, \"mvp_pilot_001\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T07:39:16.313Z\", \"updated_at\": \"2026-05-14T08:05:34.348Z\", \"spec\": {\"hypothesis\": \"Structural self-consistency (soft Jaccard) correlates with per-instance F1 better than surface Fleiss Kappa on fine-tuned Qwen3-8B SciERC\", \"model_name\": \"qwen3-8b-scierc-merged\", \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/data/test.jsonl\", \"data_count\": 551, \"server\": \"autodl-5090\", \"seed\": 42, \"parent\": \"ft_001\", \"method\": \"N=8 sampling T=1.0 + XGrammar + span realignment\", \"command\": \"CUDA_VISIBLE_DEVICES=0 python3 code/mvp_pilot.py\", \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen3-8b-scierc-merged\", \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/mvp_pilot_001.log\"}, \"conclusion\": \"negative\", \"completed_at\": \"2026-05-14T07:52:47.006Z\", \"metrics\": {\"ner_greedy_f1\": 0.611, \"ner_oracle_f1\": 0.78, \"ner_headroom\": 0.169, \"ner_fleiss_kappa_mean\": 0.2449, \"ner_soft_jaccard_mean\": 0.5041, \"ner_full_rho_sj\": 0.3616, \"ner_full_rho_fk\": 0.3515, \"ner_full_n\": 529, \"ner_cond_rho_sj\": 0.3688, \"ner_cond_rho_fk\": 0.3569, \"ner_cond_n\": 510, \"ner_sj_beats_fk_full\": true, \"ner_sj_beats_fk_cond\": true, \"ner_sample_f1_pct_zero\": 20.4, \"ner_gold_empty_filtered\": 22, \"ner_all_zero_filtered\": 19, \"re_greedy_f1\": 0.355, \"re_oracle_f1\": 0.572, \"re_headroom\": 0.217, \"re_fleiss_kappa_mean\": 0.0681, \"re_soft_jaccard_mean\": 0.3635, \"re_full_rho_sj\": 0.2535, \"re_full_rho_fk\": 0.2885, \"re_full_n\": 397, \"re_cond_rho_sj\": 0.3515, \"re_cond_rho_fk\": 0.3107, \"re_cond_n\": 320, \"re_sj_beats_fk_full\": false, \"re_sj_beats_fk_cond\": true, \"re_sample_f1_pct_zero\": 58.3, \"re_gold_empty_filtered\": 154, \"re_all_zero_filtered\": 77, \"parse_failures_stochastic\": 164, \"parse_failures_greedy\": 29, \"total_stochastic_samples\": 4408, \"total_greedy\": 551, \"verdict\": \"FAIL\", \"verdict_reason\": \"RE full rho_sj=0.2535 < 0.40; SJ does not beat FK on RE full set\"}}}, \"count\": 171, \"total\": 171, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.2261}}"
    }
  },
  "sourceToolAssistantUUID": "5a4763d9-0be9-4c23-9fed-845e289fa17e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "a6ae7e35-390a-442a-93d4-9958c82c9e3b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-19T13:51:23.110Z_

<details><summary>↩ Tool result · `toolu_013MPHfzCBgYUuHgHyYDSHS6`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/report.md\", \"content\": \"# Handover — 2026-05-19\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\\n|--------|------|------|---------|-----|\\n| exp_qwen25_72b_zeroshot | A larger zero-shot model (72B) will show higher greedy F1 and wider oracle-greedy gap than fine-tuned smaller models, because increased capacity enables more diverse valid extractions per stochastic sample, making self-consistency signals (SJ, FK, VC, EM) more informative for quality estimation. | — | — | — |\\n| exp_qwen25_14b_fewnerd | The correlation-selection gap pattern is consistent at 14B scale, filling the gap between 8B and 32B. Qwen2.5-14B QLoRA fine-tuned on FewNERD should show intermediate degeneracy rates and similar signal ranking patterns, providing a smooth scaling curve for the diagnostic findings. | — | — | — |\\n| exp_qwen25_32b_fewnerd | Scaling from Qwen3-8B to Qwen2.5-32B-Instruct with QLoRA fine-tuning on FewNERD will improve structured self-consistency IE performance due to stronger base model capabilities in instruction following and entity recognition. | — | — | — |\\n\\n## 待处理\\n（无）\\n\\n## 近期结论\\n- **exp_wnut17_qwen25_7b** (negative): The correlation-selection gap extends to noisy social media NER (WNUT-17). Unlike formal-domain datasets (SciERC/CoNLL/FewNERD), WNUT-17 has higher surface-level noise which may affect structural signal reliability differently. This tests domain generalization of the diagnostic framework.\\n- **exp_llama_fewnerd_inference** (success): LLaMA-3.1-8B fine-tuned on FewNERD shows the same structured self-consistency phenomena (degeneracy, LP-F1 alignment, signal ranking) as Qwen models, providing cross-model generalization evidence. 3-seed inference (42/123/456) for statistical robustness. ← 基于 exp_llama_fewnerd_lora\\n- **exp_entity_construction** (success): Entity-level majority vote construction is the correct self-consistency analogy for structured IE: instead of selecting the best instance-level output, assemble a better output from entity-level consensus across N samples. Construction should outperform both greedy and best-of-N selection.\\n\\n## 趋势\\n成功 101 / 负向 34 / 失败 4 / 共 167\\n\\n## 下一步\\n（无活跃 idea，请通过 ideas.md 添加）\\n\\n## 资源状态\\nautodl-5090: 空闲 cuda:0, cuda:1, cuda:2, cuda:3\\nautodl-5090-b: 空闲 cuda:0, cuda:1, cuda:2, cuda:3\\nautodl-5090-c: 空闲 cuda:0, cuda:1, cuda:2, cuda:3\\n\\n## 告警\\n- ft_002: 已被终止 — unknown\\n- mvp_pilot_002: 训练失败 — unknown\\n- exp_007_ner_llama: 已被终止 — unknown\\n- exp001_seed123: 已被终止 — unknown\\n- exp001_seed456: 已被终止 — unknown\\n- exp008_re_n16: 已被终止 — unknown\\n- exp_002_merge_conll2003: 已被终止 — unknown\\n- exp_001_n16_seed123_full: 已被终止 — unknown\\n- exp_001_n16_seed456_full: 已被终止 — unknown\\n- exp_008_re_n16_full: 已被终止 — unknown\\n- exp_001_seed42_v2_r1024: 已被终止 — unknown\\n- exp_001_seed123_v2_r1024: 已被终止 — unknown\\n- exp_001_seed456_v2_ner_r1024: 已被终止 — unknown\\n- exp_002_conll_n16_r1024: 已被终止 — unknown\\n- exp_007_llama_n16_r1024: 已被终止 — unknown\\n- exp_018_llama_scierc_seed456: 已被终止 — unknown\\n- exp_019_supervised_verifier: 已被终止 — unknown\\n- exp_lp_t07_scierc: 已被终止 — unknown\\n- exp_qwen3_4b_scierc_finetune: 已被终止 — unknown\\n- exp_freeform_seed789_v2: 训练失败 — unknown\\n- exp_qwen3_4b_scierc_finetune_v2: 训练失败 — unknown\\n- exp_qwen3_4b_scierc_finetune_v3: 训练失败 — unknown\\n- exp_qwen3_4b_conll_merge_inference_v2: 已被终止 — unknown\\n- exp_qwen3_4b_scierc_merge_inference: 已被终止 — unknown\\n- exp_tacred_re_benchmark: 已被终止 — unknown\\n- exp_vc_lp_cascade_selection: 已被终止 — unknown\\n- hidden_state_probe_conll_v2: 已被终止 — unknown\\n- hidden_state_probe_conll_full: 已被终止 — unknown\\n- dgs_pilot: 已被终止 — unknown\\n- mbr_pilot: 已被终止 — unknown\\n- exp_031_fewnerd_t12: 已被终止 — unknown\\n- exp_030_conll_t12: 已被终止 — unknown\\n\", \"total_chars\": 3628, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d3421077-f97e-472d-9701-2f62c08fb1b7",
  "isSidechain": false,
  "promptId": "2279f609-b135-4e34-8568-a1f529688be0",
  "type": "user",
  "uuid": "8b6999f8-7918-447e-8c28-372cfc075efc",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/report.md\\\", \\\"content\\\": \\\"# Handover — 2026-05-19\\\\n\\\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\\\n\\\\n## 运行中\\\\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\\\\n|--------|------|------|---------|-----|\\\\n| exp_qwen25_72b_zeroshot | A larger zero-shot model (72B) will show higher greedy F1 and wider oracle-greedy gap than fine-tuned smaller models, because increased capacity enables more diverse valid extractions per stochastic sample, making self-consistency signals (SJ, FK, VC, EM) more informative for quality estimation. | — | — | — |\\\\n| exp_qwen25_14b_fewnerd | The correlation-selection gap pattern is consistent at 14B scale, filling the gap between 8B and 32B. Qwen2.5-14B QLoRA fine-tuned on FewNERD should show intermediate degeneracy rates and similar signal ranking patterns, providing a smooth scaling curve for the diagnostic findings. | — | — | — |\\\\n| exp_qwen25_32b_fewnerd | Scaling from Qwen3-8B to Qwen2.5-32B-Instruct with QLoRA fine-tuning on FewNERD will improve structured self-consistency IE performance due to stronger base model capabilities in instruction following and entity recognition. | — | — | — |\\\\n\\\\n## 待处理\\\\n（无）\\\\n\\\\n## 近期结论\\\\n- **exp_wnut17_qwen25_7b** (negative): The correlation-selection gap extends to noisy social media NER (WNUT-17). Unlike formal-domain datasets (SciERC/CoNLL/FewNERD), WNUT-17 has higher surface-level noise which may affect structural signal reliability differently. This tests domain generalization of the diagnostic framework.\\\\n- **exp_llama_fewnerd_inference** (success): LLaMA-3.1-8B fine-tuned on FewNERD shows the same structured self-consistency phenomena (degeneracy, LP-F1 alignment, signal ranking) as Qwen models, providing cross-model generalization evidence. 3-seed inference (42/123/456) for statistical robustness. ← 基于 exp_llama_fewnerd_lora\\\\n- **exp_entity_construction** (success): Entity-level majority vote construction is the correct self-consistency analogy for structured IE: instead of selecting the best instance-level output, assemble a better output from entity-level consensus across N samples. Construction should outperform both greedy and best-of-N selection.\\\\n\\\\n## 趋势\\\\n成功 101 / 负向 34 / 失败 4 / 共 167\\\\n\\\\n## 下一步\\\\n（无活跃 idea，请通过 ideas.md 添加）\\\\n\\\\n## 资源状态\\\\nautodl-5090: 空闲 cuda:0, cuda:1, cuda:2, cuda:3\\\\nautodl-5090-b: 空闲 cuda:0, cuda:1, cuda:2, cuda:3\\\\nautodl-5090-c: 空闲 cuda:0, cuda:1, cuda:2, cuda:3\\\\n\\\\n## 告警\\\\n- ft_002: 已被终止 — unknown\\\\n- mvp_pilot_002: 训练失败 — unknown\\\\n- exp_007_ner_llama: 已被终止 — unknown\\\\n- exp001_seed123: 已被终止 — unknown\\\\n- exp001_seed456: 已被终止 — unknown\\\\n- exp008_re_n16: 已被终止 — unknown\\\\n- exp_002_merge_conll2003: 已被终止 — unknown\\\\n- exp_001_n16_seed123_full: 已被终止 — unknown\\\\n- exp_001_n16_seed456_full: 已被终止 — unknown\\\\n- exp_008_re_n16_full: 已被终止 — unknown\\\\n- exp_001_seed42_v2_r1024: 已被终止 — unknown\\\\n- exp_001_seed123_v2_r1024: 已被终止 — unknown\\\\n- exp_001_seed456_v2_ner_r1024: 已被终止 — unknown\\\\n- exp_002_conll_n16_r1024: 已被终止 — unknown\\\\n- exp_007_llama_n16_r1024: 已被终止 — unknown\\\\n- exp_018_llama_scierc_seed456: 已被终止 — unknown\\\\n- exp_019_supervised_verifier: 已被终止 — unknown\\\\n- exp_lp_t07_scierc: 已被终止 — unknown\\\\n- exp_qwen3_4b_scierc_finetune: 已被终止 — unknown\\\\n- exp_freeform_seed789_v2: 训练失败 — unknown\\\\n- exp_qwen3_4b_scierc_finetune_v2: 训练失败 — unknown\\\\n- exp_qwen3_4b_scierc_finetune_v3: 训练失败 — unknown\\\\n- exp_qwen3_4b_conll_merge_inference_v2: 已被终止 — unknown\\\\n- exp_qwen3_4b_scierc_merge_inference: 已被终止 — unknown\\\\n- exp_tacred_re_benchmark: 已被终止 — unknown\\\\n- exp_vc_lp_cascade_selection: 已被终止 — unknown\\\\n- hidden_state_probe_conll_v2: 已被终止 — unknown\\\\n- hidden_state_probe_conll_full: 已被终止 — unknown\\\\n- dgs_pilot: 已被终止 — unknown\\\\n- mbr_pilot: 已被终止 — unknown\\\\n- exp_031_fewnerd_t12: 已被终止 — unknown\\\\n- exp_030_conll_t12: 已被终止 — unknown\\\\n\\\", \\\"total_chars\\\": 3628, \\\"truncated\\\": false}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/report.md\", \"content\": \"# Handover — 2026-05-19\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\\n|--------|------|------|---------|-----|\\n| exp_qwen25_72b_zeroshot | A larger zero-shot model (72B) will show higher greedy F1 and wider oracle-greedy gap than fine-tuned smaller models, because increased capacity enables more diverse valid extractions per stochastic sample, making self-consistency signals (SJ, FK, VC, EM) more informative for quality estimation. | — | — | — |\\n| exp_qwen25_14b_fewnerd | The correlation-selection gap pattern is consistent at 14B scale, filling the gap between 8B and 32B. Qwen2.5-14B QLoRA fine-tuned on FewNERD should show intermediate degeneracy rates and similar signal ranking patterns, providing a smooth scaling curve for the diagnostic findings. | — | — | — |\\n| exp_qwen25_32b_fewnerd | Scaling from Qwen3-8B to Qwen2.5-32B-Instruct with QLoRA fine-tuning on FewNERD will improve structured self-consistency IE performance due to stronger base model capabilities in instruction following and entity recognition. | — | — | — |\\n\\n## 待处理\\n（无）\\n\\n## 近期结论\\n- **exp_wnut17_qwen25_7b** (negative): The correlation-selection gap extends to noisy social media NER (WNUT-17). Unlike formal-domain datasets (SciERC/CoNLL/FewNERD), WNUT-17 has higher surface-level noise which may affect structural signal reliability differently. This tests domain generalization of the diagnostic framework.\\n- **exp_llama_fewnerd_inference** (success): LLaMA-3.1-8B fine-tuned on FewNERD shows the same structured self-consistency phenomena (degeneracy, LP-F1 alignment, signal ranking) as Qwen models, providing cross-model generalization evidence. 3-seed inference (42/123/456) for statistical robustness. ← 基于 exp_llama_fewnerd_lora\\n- **exp_entity_construction** (success): Entity-level majority vote construction is the correct self-consistency analogy for structured IE: instead of selecting the best instance-level output, assemble a better output from entity-level consensus across N samples. Construction should outperform both greedy and best-of-N selection.\\n\\n## 趋势\\n成功 101 / 负向 34 / 失败 4 / 共 167\\n\\n## 下一步\\n（无活跃 idea，请通过 ideas.md 添加）\\n\\n## 资源状态\\nautodl-5090: 空闲 cuda:0, cuda:1, cuda:2, cuda:3\\nautodl-5090-b: 空闲 cuda:0, cuda:1, cuda:2, cuda:3\\nautodl-5090-c: 空闲 cuda:0, cuda:1, cuda:2, cuda:3\\n\\n## 告警\\n- ft_002: 已被终止 — unknown\\n- mvp_pilot_002: 训练失败 — unknown\\n- exp_007_ner_llama: 已被终止 — unknown\\n- exp001_seed123: 已被终止 — unknown\\n- exp001_seed456: 已被终止 — unknown\\n- exp008_re_n16: 已被终止 — unknown\\n- exp_002_merge_conll2003: 已被终止 — unknown\\n- exp_001_n16_seed123_full: 已被终止 — unknown\\n- exp_001_n16_seed456_full: 已被终止 — unknown\\n- exp_008_re_n16_full: 已被终止 — unknown\\n- exp_001_seed42_v2_r1024: 已被终止 — unknown\\n- exp_001_seed123_v2_r1024: 已被终止 — unknown\\n- exp_001_seed456_v2_ner_r1024: 已被终止 — unknown\\n- exp_002_conll_n16_r1024: 已被终止 — unknown\\n- exp_007_llama_n16_r1024: 已被终止 — unknown\\n- exp_018_llama_scierc_seed456: 已被终止 — unknown\\n- exp_019_supervised_verifier: 已被终止 — unknown\\n- exp_lp_t07_scierc: 已被终止 — unknown\\n- exp_qwen3_4b_scierc_finetune: 已被终止 — unknown\\n- exp_freeform_seed789_v2: 训练失败 — unknown\\n- exp_qwen3_4b_scierc_finetune_v2: 训练失败 — unknown\\n- exp_qwen3_4b_scierc_finetune_v3: 训练失败 — unknown\\n- exp_qwen3_4b_conll_merge_inference_v2: 已被终止 — unknown\\n- exp_qwen3_4b_scierc_merge_inference: 已被终止 — unknown\\n- exp_tacred_re_benchmark: 已被终止 — unknown\\n- exp_vc_lp_cascade_selection: 已被终止 — unknown\\n- hidden_state_probe_conll_v2: 已被终止 — unknown\\n- hidden_state_probe_conll_full: 已被终止 — unknown\\n- dgs_pilot: 已被终止 — unknown\\n- mbr_pilot: 已被终止 — unknown\\n- exp_031_fewnerd_t12: 已被终止 — unknown\\n- exp_030_conll_t12: 已被终止 — unknown\\n\", \"total_chars\": 3628, \"truncated\": false}, \"error\": null, \"metadata\": {}}"
    }
  },
  "sourceToolAssistantUUID": "d3421077-f97e-472d-9701-2f62c08fb1b7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "a6ae7e35-390a-442a-93d4-9958c82c9e3b",
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
  "lastPrompt": "[System 触发审查]: 收到你的 critical 审查报告，6 个数据一致性问题全部确认。已派 Agent 紧急调查修复。  请你重点关注 P0-1 SciERC AUROC 问题：如果 EM AUROC 确实是 0.749 而非 0.614，论文中以下叙述可能需要修改： 1. Table 1 信号排序结论（EM 可能超过 VC 成为 SciERC 最高 AUROC） 2. 正文中关于\"s…",
  "leafUuid": "8b6999f8-7918-447e-8c28-372cfc075efc",
  "sessionId": "a6ae7e35-390a-442a-93d4-9958c82c9e3b"
}
```

---

### Runtime record

_source line 17_

```json
{
  "type": "ai-title",
  "aiTitle": "Verify SciERC AUROC data consistency issues",
  "sessionId": "a6ae7e35-390a-442a-93d4-9958c82c9e3b"
}
```

---

### Assistant

_source line 18 · 2026-05-19T13:51:28.468Z_

<details><summary>Logged reasoning block</summary>

```text
Registry is too large. Let me use agents to extract the specific experiments I need to verify. I need to focus on:

1. P0-1: SciERC AUROC issue - specifically EM AUROC 0.749 vs 0.614
2. P1-6: CoNLL degen N=16 混用问题

Let me use subagents to extract the relevant experiments from the registry, and also read the paper-related files.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8b6999f8-7918-447e-8c28-372cfc075efc",
  "isSidechain": false,
  "requestId": "req_011CbC35cejvP8EZjHBrVN6N",
  "type": "assistant",
  "uuid": "39bd5119-213b-48d5-aa46-38542c8f78dd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "a6ae7e35-390a-442a-93d4-9958c82c9e3b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KhHNFTUmbCNQgUUQTrkaS1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2473,
      "cache_read_input_tokens": 34572,
      "output_tokens": 1032,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2473,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1032,
          "cache_read_input_tokens": 34572,
          "cache_creation_input_tokens": 2473,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2473
          },
          "type": "message"
        }
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

_source line 19 · 2026-05-19T13:51:28.966Z_

Registry 太大，用子 agent 并行提取关键数据。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "39bd5119-213b-48d5-aa46-38542c8f78dd",
  "isSidechain": false,
  "requestId": "req_011CbC35cejvP8EZjHBrVN6N",
  "type": "assistant",
  "uuid": "e810b117-3273-42f9-aba5-1de16412ad19",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "a6ae7e35-390a-442a-93d4-9958c82c9e3b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KhHNFTUmbCNQgUUQTrkaS1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2473,
      "cache_read_input_tokens": 34572,
      "output_tokens": 1032,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2473,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1032,
          "cache_read_input_tokens": 34572,
          "cache_creation_input_tokens": 2473,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2473
          },
          "type": "message"
        }
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

_source line 20 · 2026-05-19T13:51:36.652Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01Xbjos3jEpmBpHyGezc7zXL`</summary>

```json
{
  "description": "Extract SciERC AUROC data from registry",
  "prompt": "I need to extract specific experiment data from a large JSON registry file. The file is at:\n/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-reviewer-0064dd56/a6ae7e35-390a-442a-93d4-9958c82c9e3b/tool-results/mcp-agent-ml-research-read_registry-1779198683077.txt\n\nThis is JSON with schema: {result: string} — the `result` field is a YAML string containing experiment records.\n\nI need ALL experiments related to SciERC that contain AUROC metrics or signal ranking data (EM, VC, SJ, FK, LP signals). Specifically I'm looking for:\n1. Any experiment where EM AUROC on SciERC is reported (looking for values around 0.614 or 0.749)\n2. Any experiment that reports signal rankings or Table 1 style data for SciERC\n3. The exp IDs, their metrics, conclusions, and spec fields\n\nAlso extract any experiments related to CoNLL that mention \"degen\" or \"degeneracy\" rates, especially anything about N=8 vs N=16 confusion.\n\nUse jq or python to parse the file. Return the COMPLETE relevant experiment records (exp_id, status, metrics, conclusion, spec) — don't summarize, quote verbatim. This is for a data audit so accuracy matters.",
  "subagent_type": "general-purpose"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e810b117-3273-42f9-aba5-1de16412ad19",
  "isSidechain": false,
  "requestId": "req_011CbC35cejvP8EZjHBrVN6N",
  "type": "assistant",
  "uuid": "07181889-b90e-465b-bd6b-7a6d51b1b75e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "a6ae7e35-390a-442a-93d4-9958c82c9e3b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KhHNFTUmbCNQgUUQTrkaS1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2473,
      "cache_read_input_tokens": 34572,
      "output_tokens": 1032,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2473,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1032,
          "cache_read_input_tokens": 34572,
          "cache_creation_input_tokens": 2473,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2473
          },
          "type": "message"
        }
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

_source line 21 · 2026-05-19T13:51:44.786Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01PNDt4iWsXL91WHwxoeXVPH`</summary>

```json
{
  "description": "Read paper LaTeX for Table 1 and signal claims",
  "prompt": "I need to find and read the current paper LaTeX source for a project called \"struct_self_consist_ie\". The paper likely contains:\n1. A Table 1 with signal ranking data (AUROC values for EM, VC, SJ, FK, LP across datasets like SciERC, CoNLL, FewNERD)\n2. Text discussing \"structural signals > LP\" or signal quality claims\n3. Abstract and Conclusion sections with claims about signal quality\n\nThe paper source files are likely in one of these locations:\n- /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/\n- /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/paper/\n- Or find them with: find /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/ -name \"*.tex\" -type f\n\nFind all .tex files, then read the relevant sections. I need:\n1. The EXACT content of Table 1 (or whatever table shows AUROC per signal per dataset)\n2. Any text in the paper body that discusses SciERC EM AUROC specifically or signal rankings\n3. The Abstract text\n4. The Conclusion text\n5. Any text mentioning \"structural signals\" superiority over LP\n\nReturn the exact LaTeX source for these sections — don't summarize, quote verbatim. This is for a data consistency audit.",
  "subagent_type": "general-purpose"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "07181889-b90e-465b-bd6b-7a6d51b1b75e",
  "isSidechain": false,
  "requestId": "req_011CbC35cejvP8EZjHBrVN6N",
  "type": "assistant",
  "uuid": "181390d4-3aed-4a4b-80dc-49bd7e769783",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "a6ae7e35-390a-442a-93d4-9958c82c9e3b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KhHNFTUmbCNQgUUQTrkaS1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2473,
      "cache_read_input_tokens": 34572,
      "output_tokens": 1032,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2473,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1032,
          "cache_read_input_tokens": 34572,
          "cache_creation_input_tokens": 2473,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2473
          },
          "type": "message"
        }
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

_source line 22 · 2026-05-19T13:53:32.777Z_

<details><summary>↩ Tool result · `toolu_01PNDt4iWsXL91WHwxoeXVPH`</summary>

````text
Here is the complete verbatim LaTeX source for all requested sections. There are **two versions** of the paper: the current main version at `docs/paper/` and an older artifact version at `artifacts/_project/paper/`. The two differ significantly in Table 1 numbers and narrative framing. I'll present both.

---

## 1. Table 1 (Quality Estimation — AUROC per signal per dataset)

### Current version (`docs/paper/sections/experiments.tex`, lines 22-41):

```latex
\begin{table*}[t]
\centering
\small
\caption{NER quality estimation ($\rho$ and AUROC; $N{=}8$, primary seed${=}42$; 3-seed stability $\sigma{\leq}0.026$ in Table~\ref{tab:multiseed}). Best in \textbf{bold}. RE results in Appendix~\ref{app:re_extension}. $N{=}16$ in Table~\ref{tab:robustness}.}
\label{tab:quality_estimation}
\begin{tabular}{ll cc cc cc}
\toprule
& & \multicolumn{2}{c}{\textbf{SciERC}} & \multicolumn{2}{c}{\textbf{CoNLL (Qwen)}} & \multicolumn{2}{c}{\textbf{CoNLL (LLaMA)}} \\
\cmidrule(lr){3-4} \cmidrule(lr){5-6} \cmidrule(lr){7-8}
Signal & Family & $\rho$ & AUC & $\rho$ & AUC & $\rho$ & AUC \\
\midrule
VC & Structural & \textbf{.379} & \textbf{.663} & .424 & .789 & .426 & .709 \\
SJ  & Structural & .360 & .650 & .436 & .801 & \textbf{.431} & .704 \\
FK & Surface & .267 & .602 & .400 & .774 & .428 & .703 \\
EM  & Surface    & .295 & .614 & \textbf{.451} & \textbf{.816} & \textbf{.431} & .705 \\
\midrule
LP     & Model      & .205 & .578 & .316 & .753 & .307 & \textbf{.761} \\
\bottomrule
\end{tabular}
\end{table*}
```

### Older artifact version (`artifacts/_project/paper/experiments.tex`, lines 41-59):

```latex
\begin{table*}[t]
\centering
\small
\caption{Quality estimation across tasks and models (Spearman $\rho$ and AUROC). All results use $N{=}8$ samples at $T{=}1.0$. Best value per column in \textbf{bold}. SciERC evaluates joint NER (6 types) and RE (7 types); CoNLL evaluates NER (4 types) with two model families. RE results are preliminary (single dataset).}
\label{tab:quality_estimation}
\begin{tabular}{ll cc cc cc cc}
\toprule
& & \multicolumn{2}{c}{\textbf{SciERC NER}} & \multicolumn{2}{c}{\textbf{SciERC RE}} & \multicolumn{2}{c}{\textbf{CoNLL (Qwen)}} & \multicolumn{2}{c}{\textbf{CoNLL (LLaMA)}} \\
\cmidrule(lr){3-4} \cmidrule(lr){5-6} \cmidrule(lr){7-8} \cmidrule(lr){9-10}
Signal & Family & $\rho$ & AUC & $\rho$ & AUC & $\rho$ & AUC & $\rho$ & AUC \\
\midrule
Voting Conf. & Structural & \textbf{.502} & \textbf{.728} & \textbf{.422} & \textbf{.716} & .424 & .789 & .426 & .709 \\
Soft Jaccard  & Structural & .357 & .666 & .211 & .582 & .436 & .801 & \textbf{.431} & .704 \\
Fleiss' $\kappa$ & Surface & .265 & .624 & .253 & .631 & .400 & .774 & .428 & .703 \\
Exact Match  & Surface    & .257 & .623 & .100 & .504 & \textbf{.451} & \textbf{.816} & \textbf{.431} & .705 \\
Log-prob     & Model      & .140 & .559 & .247 & .635 & .316 & .753 & .307 & \textbf{.761} \\
\bottomrule
\end{tabular}
\end{table*}
```

**Key difference in SciERC NER numbers between the two versions:**

| Signal | Old version (artifacts) rho/AUC | New version (docs) rho/AUC |
|--------|------|------|
| VC | .502 / .728 | .379 / .663 |
| SJ | .357 / .666 | .360 / .650 |
| FK | .265 / .624 | .267 / .602 |
| EM | .257 / .623 | .295 / .614 |
| LP | .140 / .559 | .205 / .578 |

The old version also includes SciERC RE columns; the new version drops RE from the main table (moved to appendix).

---

## 2. Text discussing SciERC EM AUROC and signal rankings

From `docs/paper/sections/experiments.tex`, lines 45-49:

```latex
\paragraph{Signal rankings are difficulty-dependent.}
On SciERC (medium difficulty), structural signals lead (VC $\rho{=}0.379$, SJ $0.360$) over LP ($0.205$); bootstrap CIs confirm the gap ($\Delta\rho{=}{+}0.155$; Appendix~\ref{app:bootstrap_signal}).
On CoNLL (single-sample F1${\approx}$0.91), EM leads both $\rho$ and AUROC ($0.816$).
At the signal-collapse boundary (WNUT-17, macro F1${\approx}$42\%), full-set correlations are dominated by the zero/non-zero boundary (VC $\rho{=}0.724$ but conditional $\rho{=}0.038$; Table~\ref{tab:wnut}); LP shows the reverse (conditional $\rho{=}0.350$; Figure~\ref{fig:signal_heatmap}).
This collapse illustrates a regime where model capability is insufficient to produce meaningful inter-sample variation: 52\% of instances yield zero F1 across all samples, and consistency signals merely detect this floor rather than discriminating quality among non-trivial outputs.
```

---

## 3. Abstract

### Current version (`docs/paper/sections/abstract.tex`):

```latex
\begin{abstract}
Self-consistency yields large gains on discrete-answer tasks, but named entity recognition (NER) produces \textit{sets} of entities with partial overlap, where no majority vote analog exists.
We evaluate five confidence signals for quality estimation (QE) and sample selection on four NER benchmarks using fine-tuned 4B\textendash 8B models.
All signals achieve reliable QE ($\rho$ up to 0.45 on CoNLL-2003, area under the ROC curve [AUROC] up to 0.82), enabling selective prediction ($+5$--$8$\,pp F1 at 80\% coverage).
For instance-level selection, log-probability (LP) succeeds only where LP-quality alignment is strong, and gains are absent elsewhere despite large oracle headroom (the \textbf{correlation-selection gap}).
We identify three qualitative factors: instance degeneracy, oracle headroom, and LP-quality alignment; degeneracy causally modulates LP within fixed settings but does not predict cross-dataset direction.
The diagnostic naturally motivates entity-level \textit{construction}, adapting entity voting to stochastic sampling: LP-weighted aggregation improves F1 by $+1.40$\,pp on Few-NERD and $+1.02$\,pp on SciERC (multi-seed mean, $p{<}0.005$). Construction and LP selection are complementary, governed by LP-quality alignment.
\end{abstract}
```

### Older artifact version (`artifacts/_project/paper/abstract.tex`):

```latex
\begin{abstract}
Test-time scaling through multi-sample generation promises quality improvements for LLM-based information extraction, but which confidence signals best serve quality estimation versus sample selection remains unclear.
We systematically compare five confidence signals from three families---structural (entity voting, Soft Jaccard), surface (exact match, Fleiss' $\kappa$), and model-internal (log-probability)---across NER and relation extraction on SciERC and CoNLL-2003, with WNUT-17 as a boundary probe, using two model families (Qwen3-8B, LLaMA-3.1-8B).
We find that entity voting achieves $\rho{=}0.50$ and AUROC${=}0.73$ for quality estimation, with structural signals dominating on complex schemas while surface signals lead on simpler tasks; however, this strong correlation does not translate into selection gains---no signal surpasses greedy decoding on NER best-of-$N$, while only log-probability helps on relation extraction (+2.3~pp).
We term this disconnect the \textit{correlation-selection gap}: instance-level consistency signals predict which inputs the model handles reliably, not which output is best among $N$ candidates.
Signal rankings further depend on task difficulty---exact match dominates easy tasks, structural signals dominate hard tasks, and all signals converge when model capability is insufficient---establishing that signal choice should be guided by task difficulty and intended application.
These results reframe consistency signals as quality estimators rather than output selectors for structured IE.
\end{abstract}
```

---

## 4. Conclusion

### Current version (`docs/paper/sections/conclusion.tex`):

```latex
\section{Conclusion}\label{sec:conclusion}

Five confidence signals achieve reliable NER quality estimation ($\rho$ up to 0.45, AUROC up to 0.82), enabling selective prediction ($+5$--$8$\,pp F1 at 80\% coverage). Instance-level selection fails due to degeneracy and LP compression; entity-level construction yields $+1.40$\,pp on Few-NERD and $+1.02$\,pp on SciERC ($p{<}0.005$), complementary with LP selection and governed by LP-quality alignment. For practitioners: use QE for selective prediction; apply construction when multi-sample generation is feasible; assess LP-alignment to route between strategies. As models improve, degeneracy rises and the selection window narrows; content-aware verifiers \cite{cobbe2021verifiers} may be needed to close the remaining gap.
```

### Older artifact version (`artifacts/_project/paper/conclusion.tex`):

```latex
\section{Conclusion}\label{sec:conclusion}

This work provides the first systematic evaluation of confidence signals for test-time scaling in generative information extraction.
By comparing five signals from three families---structural, surface, and model-internal---across NER and RE tasks of varying difficulty, we disentangle two objectives that prior work has conflated: quality estimation (ranking instances by expected performance) and sample selection (choosing the best output among $N$ candidates).
Our experiments on SciERC, CoNLL-2003, and WNUT-17 with Qwen3-8B and LLaMA-3.1-8B reveal that these objectives require fundamentally different signal properties.

Three findings anchor our analysis.
First, consistency-based signals are effective quality estimators: entity voting achieves Spearman $\rho{=}0.50$ and AUROC${=}0.73$ on SciERC NER, with structural signals outperforming alternatives on complex schemas.
Second, the \textit{correlation-selection gap} shows that strong instance-level correlation does not yield selection gains---no consistency signal surpasses greedy decoding on NER best-of-$N$, and only log-probability helps on RE (+2.3~pp)---because instance-level signals cannot discriminate among candidates with similar consistency profiles.
Third, signal rankings depend on task difficulty: exact match leads on easy tasks, Soft Jaccard and voting lead on hard tasks, and all signals converge when model capability is insufficient, establishing practical guidance for signal choice.

Ablations confirm the gap's robustness: it persists at 4B scale and under free-form decoding without grammar constraints (\S\ref{sec:experiments}).

Several directions remain open.
Trained verifiers or reward models could close the selection gap by learning per-sample quality discrimination that unsupervised consistency signals lack.
Cross-task transfer of confidence signals beyond IE---to structured prediction tasks such as semantic parsing and code generation---would test the generality of our findings.
Integration with conformal prediction could convert continuous confidence scores into calibrated coverage guarantees.
Finally, scaling analysis with larger models (70B+) and more diverse IE tasks would clarify whether increased model capability narrows or widens the correlation-selection gap.
```

---

## 5. Text discussing "structural signals superiority over LP"

Key passages from `docs/paper/sections/experiments.tex`:

**Line 46:**
```latex
On SciERC (medium difficulty), structural signals lead (VC $\rho{=}0.379$, SJ $0.360$) over LP ($0.205$); bootstrap CIs confirm the gap ($\Delta\rho{=}{+}0.155$; Appendix~\ref{app:bootstrap_signal}).
```

**Lines 129:**
```latex
Few-NERD (Table~\ref{tab:fewnerd}) confirms LP selection at low degeneracy: $+1.39$~pp ($p{<}0.001$), while structural signals degrade selection (VC $-1.79$, SJ $-2.14$~pp).
```

**Line 143:**
```latex
Structural signals remain negative regardless of sample budget; $N$-scaling analyses are in Appendix~\ref{app:n_scaling}.
```

**Line 204:**
```latex
Structural signals remain positive but reduced (VC $\rho{=}0.277$ on SciERC, SJ $\rho{=}0.304$ on CoNLL).
```

From `docs/paper/sections/appendix.tex`, **line 258:**
```latex
This asymmetry gives structural signals a relative advantage in the compute-constrained regime: at $N{=}8$, SJ already achieves $\rho{=}0.431$ on LLaMA CoNLL (vs.\ LP $\rho{=}0.307$, $\Delta{=}{+}0.124$), and the gap \textit{widens} at $N{=}16$ ($\Delta{=}{+}0.163$) because structural signals continue to benefit from additional pairwise evidence while LP does not.
```

From `docs/paper/sections/appendix.tex`, **line 1271:**
```latex
(1)~All five signals achieve positive QE ($\rho$ 0.22--0.39); quality estimation works on Few-NERD. VC leads ($\rho{=}0.39$), followed by FK ($0.31$), SJ ($0.30$), EM ($0.29$), LP ($0.22$); the ranking matches SciERC where structural signals also outperform LP for quality estimation.
```

---

**Summary of the two-version situation:**

The **current main paper** (`docs/paper/`) reports SciERC VC rho=.379, AUROC=.663, adds Few-NERD as a fourth dataset, drops RE from the main table, and reframes the narrative around "correlation-selection gap" + "entity-level construction" as mitigation.

The **older artifact version** (`artifacts/_project/paper/`) reports SciERC VC rho=.502, AUROC=.728, includes RE columns in Table 1, and has a different abstract/conclusion that claims "structural signals dominating on complex schemas while surface signals lead on simpler tasks" more strongly. The older version's conclusion still quotes rho=0.50 / AUROC=0.73 which are the old numbers.

agentId: a751620db879accde (use SendMessage with to: 'a751620db879accde' to continue this agent)
&lt;usage>total_tokens: 59457
tool_uses: 13
duration_ms: 107988&lt;/usage>
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "parentUuid": "181390d4-3aed-4a4b-80dc-49bd7e769783",
  "isSidechain": false,
  "promptId": "2279f609-b135-4e34-8568-a1f529688be0",
  "type": "user",
  "uuid": "13731a0f-d0c0-4b14-af2d-41eeaf401991",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I need to find and read the current paper LaTeX source for a project called \"struct_self_consist_ie\". The paper likely contains:\n1. A Table 1 with signal ranking data (AUROC values for EM, VC, SJ, FK, LP across datasets like SciERC, CoNLL, FewNERD)\n2. Text discussing \"structural signals > LP\" or signal quality claims\n3. Abstract and Conclusion sections with claims about signal quality\n\nThe paper source files are likely in one of these locations:\n- /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/\n- /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/paper/\n- Or find them with: find /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/ -name \"*.tex\" -type f\n\nFind all .tex files, then read the relevant sections. I need:\n1. The EXACT content of Table 1 (or whatever table shows AUROC per signal per dataset)\n2. Any text in the paper body that discusses SciERC EM AUROC specifically or signal rankings\n3. The Abstract text\n4. The Conclusion text\n5. Any text mentioning \"structural signals\" superiority over LP\n\nReturn the exact LaTeX source for these sections — don't summarize, quote verbatim. This is for a data consistency audit.",
    "agentId": "a751620db879accde",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Here is the complete verbatim LaTeX source for all requested sections. There are **two versions** of the paper: the current main version at `docs/paper/` and an older artifact version at `artifacts/_project/paper/`. The two differ significantly in Table 1 numbers and narrative framing. I'll present both.\n\n---\n\n## 1. Table 1 (Quality Estimation — AUROC per signal per dataset)\n\n### Current version (`docs/paper/sections/experiments.tex`, lines 22-41):\n\n```latex\n\\begin{table*}[t]\n\\centering\n\\small\n\\caption{NER quality estimation ($\\rho$ and AUROC; $N{=}8$, primary seed${=}42$; 3-seed stability $\\sigma{\\leq}0.026$ in Table~\\ref{tab:multiseed}). Best in \\textbf{bold}. RE results in Appendix~\\ref{app:re_extension}. $N{=}16$ in Table~\\ref{tab:robustness}.}\n\\label{tab:quality_estimation}\n\\begin{tabular}{ll cc cc cc}\n\\toprule\n& & \\multicolumn{2}{c}{\\textbf{SciERC}} & \\multicolumn{2}{c}{\\textbf{CoNLL (Qwen)}} & \\multicolumn{2}{c}{\\textbf{CoNLL (LLaMA)}} \\\\\n\\cmidrule(lr){3-4} \\cmidrule(lr){5-6} \\cmidrule(lr){7-8}\nSignal & Family & $\\rho$ & AUC & $\\rho$ & AUC & $\\rho$ & AUC \\\\\n\\midrule\nVC & Structural & \\textbf{.379} & \\textbf{.663} & .424 & .789 & .426 & .709 \\\\\nSJ  & Structural & .360 & .650 & .436 & .801 & \\textbf{.431} & .704 \\\\\nFK & Surface & .267 & .602 & .400 & .774 & .428 & .703 \\\\\nEM  & Surface    & .295 & .614 & \\textbf{.451} & \\textbf{.816} & \\textbf{.431} & .705 \\\\\n\\midrule\nLP     & Model      & .205 & .578 & .316 & .753 & .307 & \\textbf{.761} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n```\n\n### Older artifact version (`artifacts/_project/paper/experiments.tex`, lines 41-59):\n\n```latex\n\\begin{table*}[t]\n\\centering\n\\small\n\\caption{Quality estimation across tasks and models (Spearman $\\rho$ and AUROC). All results use $N{=}8$ samples at $T{=}1.0$. Best value per column in \\textbf{bold}. SciERC evaluates joint NER (6 types) and RE (7 types); CoNLL evaluates NER (4 types) with two model families. RE results are preliminary (single dataset).}\n\\label{tab:quality_estimation}\n\\begin{tabular}{ll cc cc cc cc}\n\\toprule\n& & \\multicolumn{2}{c}{\\textbf{SciERC NER}} & \\multicolumn{2}{c}{\\textbf{SciERC RE}} & \\multicolumn{2}{c}{\\textbf{CoNLL (Qwen)}} & \\multicolumn{2}{c}{\\textbf{CoNLL (LLaMA)}} \\\\\n\\cmidrule(lr){3-4} \\cmidrule(lr){5-6} \\cmidrule(lr){7-8} \\cmidrule(lr){9-10}\nSignal & Family & $\\rho$ & AUC & $\\rho$ & AUC & $\\rho$ & AUC & $\\rho$ & AUC \\\\\n\\midrule\nVoting Conf. & Structural & \\textbf{.502} & \\textbf{.728} & \\textbf{.422} & \\textbf{.716} & .424 & .789 & .426 & .709 \\\\\nSoft Jaccard  & Structural & .357 & .666 & .211 & .582 & .436 & .801 & \\textbf{.431} & .704 \\\\\nFleiss' $\\kappa$ & Surface & .265 & .624 & .253 & .631 & .400 & .774 & .428 & .703 \\\\\nExact Match  & Surface    & .257 & .623 & .100 & .504 & \\textbf{.451} & \\textbf{.816} & \\textbf{.431} & .705 \\\\\nLog-prob     & Model      & .140 & .559 & .247 & .635 & .316 & .753 & .307 & \\textbf{.761} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n```\n\n**Key difference in SciERC NER numbers between the two versions:**\n\n| Signal | Old version (artifacts) rho/AUC | New version (docs) rho/AUC |\n|--------|------|------|\n| VC | .502 / .728 | .379 / .663 |\n| SJ | .357 / .666 | .360 / .650 |\n| FK | .265 / .624 | .267 / .602 |\n| EM | .257 / .623 | .295 / .614 |\n| LP | .140 / .559 | .205 / .578 |\n\nThe old version also includes SciERC RE columns; the new version drops RE from the main table (moved to appendix).\n\n---\n\n## 2. Text discussing SciERC EM AUROC and signal rankings\n\nFrom `docs/paper/sections/experiments.tex`, lines 45-49:\n\n```latex\n\\paragraph{Signal rankings are difficulty-dependent.}\nOn SciERC (medium difficulty), structural signals lead (VC $\\rho{=}0.379$, SJ $0.360$) over LP ($0.205$); bootstrap CIs confirm the gap ($\\Delta\\rho{=}{+}0.155$; Appendix~\\ref{app:bootstrap_signal}).\nOn CoNLL (single-sample F1${\\approx}$0.91), EM leads both $\\rho$ and AUROC ($0.816$).\nAt the signal-collapse boundary (WNUT-17, macro F1${\\approx}$42\\%), full-set correlations are dominated by the zero/non-zero boundary (VC $\\rho{=}0.724$ but conditional $\\rho{=}0.038$; Table~\\ref{tab:wnut}); LP shows the reverse (conditional $\\rho{=}0.350$; Figure~\\ref{fig:signal_heatmap}).\nThis collapse illustrates a regime where model capability is insufficient to produce meaningful inter-sample variation: 52\\% of instances yield zero F1 across all samples, and consistency signals merely detect this floor rather than discriminating quality among non-trivial outputs.\n```\n\n---\n\n## 3. Abstract\n\n### Current version (`docs/paper/sections/abstract.tex`):\n\n```latex\n\\begin{abstract}\nSelf-consistency yields large gains on discrete-answer tasks, but named entity recognition (NER) produces \\textit{sets} of entities with partial overlap, where no majority vote analog exists.\nWe evaluate five confidence signals for quality estimation (QE) and sample selection on four NER benchmarks using fine-tuned 4B\\textendash 8B models.\nAll signals achieve reliable QE ($\\rho$ up to 0.45 on CoNLL-2003, area under the ROC curve [AUROC] up to 0.82), enabling selective prediction ($+5$--$8$\\,pp F1 at 80\\% coverage).\nFor instance-level selection, log-probability (LP) succeeds only where LP-quality alignment is strong, and gains are absent elsewhere despite large oracle headroom (the \\textbf{correlation-selection gap}).\nWe identify three qualitative factors: instance degeneracy, oracle headroom, and LP-quality alignment; degeneracy causally modulates LP within fixed settings but does not predict cross-dataset direction.\nThe diagnostic naturally motivates entity-level \\textit{construction}, adapting entity voting to stochastic sampling: LP-weighted aggregation improves F1 by $+1.40$\\,pp on Few-NERD and $+1.02$\\,pp on SciERC (multi-seed mean, $p{<}0.005$). Construction and LP selection are complementary, governed by LP-quality alignment.\n\\end{abstract}\n```\n\n### Older artifact version (`artifacts/_project/paper/abstract.tex`):\n\n```latex\n\\begin{abstract}\nTest-time scaling through multi-sample generation promises quality improvements for LLM-based information extraction, but which confidence signals best serve quality estimation versus sample selection remains unclear.\nWe systematically compare five confidence signals from three families---structural (entity voting, Soft Jaccard), surface (exact match, Fleiss' $\\kappa$), and model-internal (log-probability)---across NER and relation extraction on SciERC and CoNLL-2003, with WNUT-17 as a boundary probe, using two model families (Qwen3-8B, LLaMA-3.1-8B).\nWe find that entity voting achieves $\\rho{=}0.50$ and AUROC${=}0.73$ for quality estimation, with structural signals dominating on complex schemas while surface signals lead on simpler tasks; however, this strong correlation does not translate into selection gains---no signal surpasses greedy decoding on NER best-of-$N$, while only log-probability helps on relation extraction (+2.3~pp).\nWe term this disconnect the \\textit{correlation-selection gap}: instance-level consistency signals predict which inputs the model handles reliably, not which output is best among $N$ candidates.\nSignal rankings further depend on task difficulty---exact match dominates easy tasks, structural signals dominate hard tasks, and all signals converge when model capability is insufficient---establishing that signal choice should be guided by task difficulty and intended application.\nThese results reframe consistency signals as quality estimators rather than output selectors for structured IE.\n\\end{abstract}\n```\n\n---\n\n## 4. Conclusion\n\n### Current version (`docs/paper/sections/conclusion.tex`):\n\n```latex\n\\section{Conclusion}\\label{sec:conclusion}\n\nFive confidence signals achieve reliable NER quality estimation ($\\rho$ up to 0.45, AUROC up to 0.82), enabling selective prediction ($+5$--$8$\\,pp F1 at 80\\% coverage). Instance-level selection fails due to degeneracy and LP compression; entity-level construction yields $+1.40$\\,pp on Few-NERD and $+1.02$\\,pp on SciERC ($p{<}0.005$), complementary with LP selection and governed by LP-quality alignment. For practitioners: use QE for selective prediction; apply construction when multi-sample generation is feasible; assess LP-alignment to route between strategies. As models improve, degeneracy rises and the selection window narrows; content-aware verifiers \\cite{cobbe2021verifiers} may be needed to close the remaining gap.\n```\n\n### Older artifact version (`artifacts/_project/paper/conclusion.tex`):\n\n```latex\n\\section{Conclusion}\\label{sec:conclusion}\n\nThis work provides the first systematic evaluation of confidence signals for test-time scaling in generative information extraction.\nBy comparing five signals from three families---structural, surface, and model-internal---across NER and RE tasks of varying difficulty, we disentangle two objectives that prior work has conflated: quality estimation (ranking instances by expected performance) and sample selection (choosing the best output among $N$ candidates).\nOur experiments on SciERC, CoNLL-2003, and WNUT-17 with Qwen3-8B and LLaMA-3.1-8B reveal that these objectives require fundamentally different signal properties.\n\nThree findings anchor our analysis.\nFirst, consistency-based signals are effective quality estimators: entity voting achieves Spearman $\\rho{=}0.50$ and AUROC${=}0.73$ on SciERC NER, with structural signals outperforming alternatives on complex schemas.\nSecond, the \\textit{correlation-selection gap} shows that strong instance-level correlation does not yield selection gains---no consistency signal surpasses greedy decoding on NER best-of-$N$, and only log-probability helps on RE (+2.3~pp)---because instance-level signals cannot discriminate among candidates with similar consistency profiles.\nThird, signal rankings depend on task difficulty: exact match leads on easy tasks, Soft Jaccard and voting lead on hard tasks, and all signals converge when model capability is insufficient, establishing practical guidance for signal choice.\n\nAblations confirm the gap's robustness: it persists at 4B scale and under free-form decoding without grammar constraints (\\S\\ref{sec:experiments}).\n\nSeveral directions remain open.\nTrained verifiers or reward models could close the selection gap by learning per-sample quality discrimination that unsupervised consistency signals lack.\nCross-task transfer of confidence signals beyond IE---to structured prediction tasks such as semantic parsing and code generation---would test the generality of our findings.\nIntegration with conformal prediction could convert continuous confidence scores into calibrated coverage guarantees.\nFinally, scaling analysis with larger models (70B+) and more diverse IE tasks would clarify whether increased model capability narrows or widens the correlation-selection gap.\n```\n\n---\n\n## 5. Text discussing \"structural signals superiority over LP\"\n\nKey passages from `docs/paper/sections/experiments.tex`:\n\n**Line 46:**\n```latex\nOn SciERC (medium difficulty), structural signals lead (VC $\\rho{=}0.379$, SJ $0.360$) over LP ($0.205$); bootstrap CIs confirm the gap ($\\Delta\\rho{=}{+}0.155$; Appendix~\\ref{app:bootstrap_signal}).\n```\n\n**Lines 129:**\n```latex\nFew-NERD (Table~\\ref{tab:fewnerd}) confirms LP selection at low degeneracy: $+1.39$~pp ($p{<}0.001$), while structural signals degrade selection (VC $-1.79$, SJ $-2.14$~pp).\n```\n\n**Line 143:**\n```latex\nStructural signals remain negative regardless of sample budget; $N$-scaling analyses are in Appendix~\\ref{app:n_scaling}.\n```\n\n**Line 204:**\n```latex\nStructural signals remain positive but reduced (VC $\\rho{=}0.277$ on SciERC, SJ $\\rho{=}0.304$ on CoNLL).\n```\n\nFrom `docs/paper/sections/appendix.tex`, **line 258:**\n```latex\nThis asymmetry gives structural signals a relative advantage in the compute-constrained regime: at $N{=}8$, SJ already achieves $\\rho{=}0.431$ on LLaMA CoNLL (vs.\\ LP $\\rho{=}0.307$, $\\Delta{=}{+}0.124$), and the gap \\textit{widens} at $N{=}16$ ($\\Delta{=}{+}0.163$) because structural signals continue to benefit from additional pairwise evidence while LP does not.\n```\n\nFrom `docs/paper/sections/appendix.tex`, **line 1271:**\n```latex\n(1)~All five signals achieve positive QE ($\\rho$ 0.22--0.39); quality estimation works on Few-NERD. VC leads ($\\rho{=}0.39$), followed by FK ($0.31$), SJ ($0.30$), EM ($0.29$), LP ($0.22$); the ranking matches SciERC where structural signals also outperform LP for quality estimation.\n```\n\n---\n\n**Summary of the two-version situation:**\n\nThe **current main paper** (`docs/paper/`) reports SciERC VC rho=.379, AUROC=.663, adds Few-NERD as a fourth dataset, drops RE from the main table, and reframes the narrative around \"correlation-selection gap\" + \"entity-level construction\" as mitigation.\n\nThe **older artifact version** (`artifacts/_project/paper/`) reports SciERC VC rho=.502, AUROC=.728, includes RE columns in Table 1, and has a different abstract/conclusion that claims \"structural signals dominating on complex schemas while surface signals lead on simpler tasks\" more strongly. The older version's conclusion still quotes rho=0.50 / AUROC=0.73 which are the old numbers."
      }
    ],
    "totalDurationMs": 107988,
    "totalTokens": 59457,
    "totalToolUseCount": 13,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 690,
      "cache_read_input_tokens": 54634,
      "output_tokens": 4132,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 690
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 4132,
          "cache_read_input_tokens": 54634,
          "cache_creation_input_tokens": 690,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 690,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 10,
      "searchCount": 3,
      "bashCount": 0,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 0
    }
  },
  "sourceToolAssistantUUID": "181390d4-3aed-4a4b-80dc-49bd7e769783",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "a6ae7e35-390a-442a-93d4-9958c82c9e3b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
````

</details>

---

### Runtime record

_source line 23_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[System 触发审查]: 收到你的 critical 审查报告，6 个数据一致性问题全部确认。已派 Agent 紧急调查修复。  请你重点关注 P0-1 SciERC AUROC 问题：如果 EM AUROC 确实是 0.749 而非 0.614，论文中以下叙述可能需要修改： 1. Table 1 信号排序结论（EM 可能超过 VC 成为 SciERC 最高 AUROC） 2. 正文中关于\"s…",
  "leafUuid": "13731a0f-d0c0-4b14-af2d-41eeaf401991",
  "sessionId": "a6ae7e35-390a-442a-93d4-9958c82c9e3b"
}
```

---

### Runtime record

_source line 24_

```json
{
  "type": "ai-title",
  "aiTitle": "Verify SciERC AUROC data consistency issues",
  "sessionId": "a6ae7e35-390a-442a-93d4-9958c82c9e3b"
}
```

---

### Tool result

_source line 25 · 2026-05-19T13:54:48.895Z_

<details><summary>↩ Tool result · `toolu_01Xbjos3jEpmBpHyGezc7zXL`</summary>

```text
All requested data has been extracted. Here is the complete summary of what was found:

---

## SciERC Experiments with AUROC Metrics and Signal Ranking Data

### Experiments containing the specific values 0.614 / 0.749:

1. **exp_010_selection_curves** — Best-of-N selection curves analysis. SciERC NER N=8: FK=0.614, SJ=0.614 (selection F1). SciERC NER N=16: SJ=0.620, FK=0.621. The 0.614 appears as selection F1 values, not AUROC.

2. **exp_012_rerun_1024** — Canonical SciERC baseline with max_tokens=1024, Qwen3-8B, N=8, T=1.0, seed=42. Contains the most complete 5-signal AUROC data:
   - NER full: EM AUROC=0.7493, SJ AUROC=0.6917, FK AUROC=0.629, VC AUROC=0.6841, LP AUROC=0.5783
   - NER cond: EM AUROC=0.7556, SJ AUROC=0.6772, FK AUROC=0.6078, VC AUROC=0.6618, LP AUROC=0.5633
   - Contains provenance_note: "exp_015_v2 scierc_n8_logprob used exp_012_logprob (max_tokens=512 truncated data). voting_conf was inflated 0.502→0.379, logprob was suppressed 0.140→0.205."

3. **exp_freeform_seed123** — Free-form SciERC seed=123. qe_ner SJ auroc=0.748728, FK auroc=0.766039, EM auroc=0.52533, VC auroc=0.799676, LP auroc=0.701657. The 0.749 value matches SJ auroc here.

4. **exp_007_llama_seed456** — LLaMA SciERC seed=456. NER soft_jaccard=0.7491 (this is the SJ metric value, not AUROC). NER logprob_auroc=0.5989, RE logprob_auroc=0.6678. Conclusion: negative.

### Key SciERC AUROC experiments by model/configuration:

**Qwen3-8B SciERC (Table 1 style):**
- **exp_001_ner_n16_scierc** (N=16, seed=42): SJ AUROC=0.697, VC AUROC=0.704, RE EM cond AUROC=0.742
- **exp_001_n16_seed456** (N=16, seed=456): SJ AUROC=0.6823, VC AUROC=0.6981, EM AUROC=0.649, FK AUROC=0.6179, LP AUROC=0.5885
- **exp_001_seed456_v2_ner** (N=16, seed=456, NER-only): EM cond AUROC=0.78, SJ cond AUROC=0.699, full EM AUROC=0.768, full SJ AUROC=0.711
- **exp_015_metrics_expansion** (N=8, seed=42, 5-signal): NER SJ AUROC=0.6656, NER EM AUROC=0.623, NER VC AUROC=0.7279; RE VC AUROC=0.7162. Notes: "RE cond values are DEPRECATED"
- **exp_015_v2** (multi-model averages): NER EM AUROC=0.7873, SJ AUROC=0.7394, VC AUROC=0.7367; RE EM AUROC=0.715

**LLaMA-8B SciERC:**
- **exp_018_llama_scierc_seed42_r1024** (N=8, seed=42): NER full EM AUROC=0.7174, SJ AUROC=0.6683, VC AUROC=0.6967; RE full EM AUROC=0.7697, SJ AUROC=0.7244, VC AUROC=0.7337
- **exp_007_llama_n16** (N=16, seed=42): NER full EM AUROC=0.7686, SJ AUROC=0.717, VC AUROC=0.7266, LP AUROC=0.5656
- **exp_007_llama_scierc_seed123**: SJ AUROC (full)=0.7092, EM AUROC (full)=0.7468; degen_rate=0.2665
- **exp_llama_scierc_seed456**: EM AUROC full=0.7538, SJ AUROC full=0.7061; degen_rate=0.2741

**LLaMA-3.2-3B SciERC:**
- **exp_llama3b_scierc_ablation**: NER full EM AUROC=0.7763, SJ AUROC=0.7383, VC AUROC=0.7429, FK AUROC=0.6714, LP AUROC=0.633

**LoRA rank=8 ablation:**
- **exp_023_lora_rank8**: NER full EM AUROC=0.7265, SJ AUROC=0.689, VC AUROC=0.6886, FK AUROC=0.6002, LP AUROC=0.6054

**Temperature ablation (SciERC, Qwen3-8B, N=8):**
- **exp_026_T05** (T=0.5): SJ AUROC=0.644, LP AUROC=0.577; degen_rate=0.414
- **exp_026_T08** (T=0.8): SJ AUROC=0.662, LP AUROC=0.571; degen_rate=0.2382
- **exp_026_T12** (T=1.2): SJ AUROC=0.683, LP AUROC=0.566; degen_rate=0.1493

**Verbalized confidence baseline:**
- **exp_verbalized_confidence**: SciERC VerbConf AUROC=0.6811, rho=0.2965; CoNLL VerbConf AUROC=0.7469, rho=0.3366

**Free-form ablation (3 seeds):**
- **exp_freeform_seed123**: NER SJ AUROC=0.7487, FK=0.766, VC=0.7997, EM=0.5253, LP=0.7017
- **exp_freeform_seed456**: NER SJ AUROC=0.7078, FK=0.7548, VC=0.7565, EM=0.4779, LP=0.6721
- **exp_freeform_seed789**: NER SJ AUROC=0.7345, FK=0.7944, VC=0.7681, EM=0.5270, LP=0.6778

---

## CoNLL Degeneracy Experiments

### Key degeneracy rates by model/config:

**Qwen3-8B CoNLL N=16:**
- **exp_002_conll_n16** (seed=42): degen_rate=0.4844
- **exp_002_conll_n16_seed123**: degen_rate=0.471
- **exp_002_conll_n16_seed456**: degen_rate=0.5544

**LLaMA-8B CoNLL N=16:**
- **exp_017_llama_conll_n16_r1024** (seed=42): degen_rate=0.8647
- **exp_017_llama_conll_n16_s123_r1024**: degen_rate=0.8636
- **exp_017_llama_conll_n16_s456_r1024**: degen_rate=0.8672
- **exp_017_llama_conll** (3-seed aggregated analysis, N=8): degeneracy_cf1_gold_filtered=0.894
- **exp_017_llama_conll_finetune** (re-finetuned): degeneracy_rate=0.853

**Qwen3-4B CoNLL N=8:**
- **exp_qwen3_4b_conll_scs_inference**: degen_rate=0.9057
- **exp_qwen3_4b_conll_scs_inference_v2**: degen_rate=0.9057

### N=8 vs N=16 confusion:

**exp_030_conll_t12** is the critical record here — it was **killed** with explicit note: "数据不可用于论文：N不一致(N=8 vs T=1.0基准的N=16)". This confirms there was a known N=8 vs N=16 inconsistency issue that led to this experiment being invalidated.

**exp_002_conll_n16** contains explicit `n8_vs_n16_delta_rho_full` comparing N=8→N=16 deltas: EM +0.012, FK -0.007, SJ +0.0139, LP -0.0011, VC +0.0049.

**exp_entity_construction** has both n8 and n16 results: n8 CoNLL uniform CV: -0.39pp (not sig); n16 CoNLL uniform CV: +0.10pp (not sig, p=0.303). Notes "adaptive_combination: INVALIDATED - gold label leakage confirmed".

**exp_freeform_conll_4seed** used N=8 with 4 seeds on CoNLL free-form, with LP range median=0.0581 (much higher than constrained).

agentId: a93f1505099f6b26c (use SendMessage with to: 'a93f1505099f6b26c' to continue this agent)
&lt;usage>total_tokens: 82873
tool_uses: 12
duration_ms: 192239&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "07181889-b90e-465b-bd6b-7a6d51b1b75e",
  "isSidechain": false,
  "promptId": "2279f609-b135-4e34-8568-a1f529688be0",
  "type": "user",
  "uuid": "1b1b46ca-1627-4d00-8ac8-a7012b3a9cff",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I need to extract specific experiment data from a large JSON registry file. The file is at:\n/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-reviewer-0064dd56/a6ae7e35-390a-442a-93d4-9958c82c9e3b/tool-results/mcp-agent-ml-research-read_registry-1779198683077.txt\n\nThis is JSON with schema: {result: string} — the `result` field is a YAML string containing experiment records.\n\nI need ALL experiments related to SciERC that contain AUROC metrics or signal ranking data (EM, VC, SJ, FK, LP signals). Specifically I'm looking for:\n1. Any experiment where EM AUROC on SciERC is reported (looking for values around 0.614 or 0.749)\n2. Any experiment that reports signal rankings or Table 1 style data for SciERC\n3. The exp IDs, their metrics, conclusions, and spec fields\n\nAlso extract any experiments related to CoNLL that mention \"degen\" or \"degeneracy\" rates, especially anything about N=8 vs N=16 confusion.\n\nUse jq or python to parse the file. Return the COMPLETE relevant experiment records (exp_id, status, metrics, conclusion, spec) — don't summarize, quote verbatim. This is for a data audit so accuracy matters.",
    "agentId": "a93f1505099f6b26c",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "All requested data has been extracted. Here is the complete summary of what was found:\n\n---\n\n## SciERC Experiments with AUROC Metrics and Signal Ranking Data\n\n### Experiments containing the specific values 0.614 / 0.749:\n\n1. **exp_010_selection_curves** — Best-of-N selection curves analysis. SciERC NER N=8: FK=0.614, SJ=0.614 (selection F1). SciERC NER N=16: SJ=0.620, FK=0.621. The 0.614 appears as selection F1 values, not AUROC.\n\n2. **exp_012_rerun_1024** — Canonical SciERC baseline with max_tokens=1024, Qwen3-8B, N=8, T=1.0, seed=42. Contains the most complete 5-signal AUROC data:\n   - NER full: EM AUROC=0.7493, SJ AUROC=0.6917, FK AUROC=0.629, VC AUROC=0.6841, LP AUROC=0.5783\n   - NER cond: EM AUROC=0.7556, SJ AUROC=0.6772, FK AUROC=0.6078, VC AUROC=0.6618, LP AUROC=0.5633\n   - Contains provenance_note: \"exp_015_v2 scierc_n8_logprob used exp_012_logprob (max_tokens=512 truncated data). voting_conf was inflated 0.502→0.379, logprob was suppressed 0.140→0.205.\"\n\n3. **exp_freeform_seed123** — Free-form SciERC seed=123. qe_ner SJ auroc=0.748728, FK auroc=0.766039, EM auroc=0.52533, VC auroc=0.799676, LP auroc=0.701657. The 0.749 value matches SJ auroc here.\n\n4. **exp_007_llama_seed456** — LLaMA SciERC seed=456. NER soft_jaccard=0.7491 (this is the SJ metric value, not AUROC). NER logprob_auroc=0.5989, RE logprob_auroc=0.6678. Conclusion: negative.\n\n### Key SciERC AUROC experiments by model/configuration:\n\n**Qwen3-8B SciERC (Table 1 style):**\n- **exp_001_ner_n16_scierc** (N=16, seed=42): SJ AUROC=0.697, VC AUROC=0.704, RE EM cond AUROC=0.742\n- **exp_001_n16_seed456** (N=16, seed=456): SJ AUROC=0.6823, VC AUROC=0.6981, EM AUROC=0.649, FK AUROC=0.6179, LP AUROC=0.5885\n- **exp_001_seed456_v2_ner** (N=16, seed=456, NER-only): EM cond AUROC=0.78, SJ cond AUROC=0.699, full EM AUROC=0.768, full SJ AUROC=0.711\n- **exp_015_metrics_expansion** (N=8, seed=42, 5-signal): NER SJ AUROC=0.6656, NER EM AUROC=0.623, NER VC AUROC=0.7279; RE VC AUROC=0.7162. Notes: \"RE cond values are DEPRECATED\"\n- **exp_015_v2** (multi-model averages): NER EM AUROC=0.7873, SJ AUROC=0.7394, VC AUROC=0.7367; RE EM AUROC=0.715\n\n**LLaMA-8B SciERC:**\n- **exp_018_llama_scierc_seed42_r1024** (N=8, seed=42): NER full EM AUROC=0.7174, SJ AUROC=0.6683, VC AUROC=0.6967; RE full EM AUROC=0.7697, SJ AUROC=0.7244, VC AUROC=0.7337\n- **exp_007_llama_n16** (N=16, seed=42): NER full EM AUROC=0.7686, SJ AUROC=0.717, VC AUROC=0.7266, LP AUROC=0.5656\n- **exp_007_llama_scierc_seed123**: SJ AUROC (full)=0.7092, EM AUROC (full)=0.7468; degen_rate=0.2665\n- **exp_llama_scierc_seed456**: EM AUROC full=0.7538, SJ AUROC full=0.7061; degen_rate=0.2741\n\n**LLaMA-3.2-3B SciERC:**\n- **exp_llama3b_scierc_ablation**: NER full EM AUROC=0.7763, SJ AUROC=0.7383, VC AUROC=0.7429, FK AUROC=0.6714, LP AUROC=0.633\n\n**LoRA rank=8 ablation:**\n- **exp_023_lora_rank8**: NER full EM AUROC=0.7265, SJ AUROC=0.689, VC AUROC=0.6886, FK AUROC=0.6002, LP AUROC=0.6054\n\n**Temperature ablation (SciERC, Qwen3-8B, N=8):**\n- **exp_026_T05** (T=0.5): SJ AUROC=0.644, LP AUROC=0.577; degen_rate=0.414\n- **exp_026_T08** (T=0.8): SJ AUROC=0.662, LP AUROC=0.571; degen_rate=0.2382\n- **exp_026_T12** (T=1.2): SJ AUROC=0.683, LP AUROC=0.566; degen_rate=0.1493\n\n**Verbalized confidence baseline:**\n- **exp_verbalized_confidence**: SciERC VerbConf AUROC=0.6811, rho=0.2965; CoNLL VerbConf AUROC=0.7469, rho=0.3366\n\n**Free-form ablation (3 seeds):**\n- **exp_freeform_seed123**: NER SJ AUROC=0.7487, FK=0.766, VC=0.7997, EM=0.5253, LP=0.7017\n- **exp_freeform_seed456**: NER SJ AUROC=0.7078, FK=0.7548, VC=0.7565, EM=0.4779, LP=0.6721\n- **exp_freeform_seed789**: NER SJ AUROC=0.7345, FK=0.7944, VC=0.7681, EM=0.5270, LP=0.6778\n\n---\n\n## CoNLL Degeneracy Experiments\n\n### Key degeneracy rates by model/config:\n\n**Qwen3-8B CoNLL N=16:**\n- **exp_002_conll_n16** (seed=42): degen_rate=0.4844\n- **exp_002_conll_n16_seed123**: degen_rate=0.471\n- **exp_002_conll_n16_seed456**: degen_rate=0.5544\n\n**LLaMA-8B CoNLL N=16:**\n- **exp_017_llama_conll_n16_r1024** (seed=42): degen_rate=0.8647\n- **exp_017_llama_conll_n16_s123_r1024**: degen_rate=0.8636\n- **exp_017_llama_conll_n16_s456_r1024**: degen_rate=0.8672\n- **exp_017_llama_conll** (3-seed aggregated analysis, N=8): degeneracy_cf1_gold_filtered=0.894\n- **exp_017_llama_conll_finetune** (re-finetuned): degeneracy_rate=0.853\n\n**Qwen3-4B CoNLL N=8:**\n- **exp_qwen3_4b_conll_scs_inference**: degen_rate=0.9057\n- **exp_qwen3_4b_conll_scs_inference_v2**: degen_rate=0.9057\n\n### N=8 vs N=16 confusion:\n\n**exp_030_conll_t12** is the critical record here — it was **killed** with explicit note: \"数据不可用于论文：N不一致(N=8 vs T=1.0基准的N=16)\". This confirms there was a known N=8 vs N=16 inconsistency issue that led to this experiment being invalidated.\n\n**exp_002_conll_n16** contains explicit `n8_vs_n16_delta_rho_full` comparing N=8→N=16 deltas: EM +0.012, FK -0.007, SJ +0.0139, LP -0.0011, VC +0.0049.\n\n**exp_entity_construction** has both n8 and n16 results: n8 CoNLL uniform CV: -0.39pp (not sig); n16 CoNLL uniform CV: +0.10pp (not sig, p=0.303). Notes \"adaptive_combination: INVALIDATED - gold label leakage confirmed\".\n\n**exp_freeform_conll_4seed** used N=8 with 4 seeds on CoNLL free-form, with LP range median=0.0581 (much higher than constrained)."
      }
    ],
    "totalDurationMs": 192239,
    "totalTokens": 82873,
    "totalToolUseCount": 12,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3088,
      "cache_read_input_tokens": 77270,
      "output_tokens": 2514,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3088
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2514,
          "cache_read_input_tokens": 77270,
          "cache_creation_input_tokens": 3088,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3088,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 1,
      "searchCount": 0,
      "bashCount": 11,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 0
    }
  },
  "sourceToolAssistantUUID": "07181889-b90e-465b-bd6b-7a6d51b1b75e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "a6ae7e35-390a-442a-93d4-9958c82c9e3b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 26 · 2026-05-19T13:55:26.914Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a comprehensive picture. Let me analyze the critical issues:

## P0-1: SciERC EM AUROC

The current paper's Table 1 reports EM AUROC = 0.614 on SciERC. But from the registry, exp_012_rerun_1024 (which is the canonical SciERC baseline - Qwen3-8B, N=8, T=1.0, seed=42) shows:
- NER full: EM AUROC = 0.7493


- NER cond: EM AUROC = 0.7556

So the paper says 0.614 but the registry says 0.749 - a massive discrepancy. Looking at the full Table 1 breakdown across all entity types (VC, SJ, FK, EM, LP) and comparing against the registry results, there's a fundamental mismatch in what's being reported versus what the actual baseline achieved.

If EM truly reaches 0.749, it would completely reshape the narrative - EM would be the strongest signal on SciERC, not VC as currently shown in the paper. This would contradict the claim that structural signals dominate, since EM is a surface-level signal. I need to trace where the 0.614 figure actually comes from, since the registry shows 0.749 but other experiment logs show values closer to 0.623.

Looking at the provenance trail, exp_015 had inflated numbers that were corrected in exp_012_rerun_1024, but the paper's Table 1 doesn't seem to match either experiment exactly. I'm trying to figure out which specific run produced the VC and SJ values currently reported in the table.

Now examining the full results from exp_012_rerun_1024 and exp_015_metrics_expansion to see if any subset matches the paper's reported numbers, but none of them align cleanly with what's published—the EM AUROC of 0.614 in particular doesn't correspond to any single experiment I can identify.

The provenance note about the VC correction (0.502→0.379) indicates the paper should be using post-correction data, yet the EM value of 0.614 contradicts exp_012's canonical result of 0.749, which points directly to the P0-1 issue the Director flagged. If the corrected EM AUROC is actually 0.749, then the paper's 0.614 is wrong and would shift the entire signal ranking in Table 1.

With the corrected value, EM jumps to the top signal on SciERC, fundamentally changing the narrative about structural signals leading over surface signals—the rho claims might still hold, but the AUROC story flips, weakening the paper's core argument about signal family hierarchy on complex tasks.

I'm also noticing discrepancies in the reported numbers. The NER full and conditional AUROC values I'm seeing don't match what the paper claims, which suggests either different experimental runs or a data mismatch. And looking at the registry, there's a flagged experiment on CoNLL that was explicitly marked as unusable for the paper due to inconsistent sample sizes—N=8 versus the baseline N=16—which raises questions about data integrity in that comparison.

I need to trace back through the provenance file to see exactly which experiments feed into Table 1, then verify those results directly on the server to understand where these discrepancies are coming from.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1b1b46ca-1627-4d00-8ac8-a7012b3a9cff",
  "isSidechain": false,
  "requestId": "req_011CbC3LnYDy8MNiyH2QdQNP",
  "type": "assistant",
  "uuid": "dfcf967e-f097-444b-9418-06bf4c31c71e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "a6ae7e35-390a-442a-93d4-9958c82c9e3b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Huxd6tgZmMAF1BcTukw4RG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4226,
      "cache_creation_input_tokens": 3649,
      "cache_read_input_tokens": 37045,
      "output_tokens": 2157,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3649,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 4226,
          "output_tokens": 2157,
          "cache_read_input_tokens": 37045,
          "cache_creation_input_tokens": 3649,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3649
          },
          "type": "message"
        }
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

_source line 27 · 2026-05-19T13:55:27.860Z_

数据已提取完毕。P0-1 问题非常明确：exp_012_rerun_1024（canonical baseline，Qwen3-8B, N=8, seed=42）的 EM AUROC=0.7493，但论文 Table 1 写的是 0.614。现在需要追溯数据来源并评估影响。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dfcf967e-f097-444b-9418-06bf4c31c71e",
  "isSidechain": false,
  "requestId": "req_011CbC3LnYDy8MNiyH2QdQNP",
  "type": "assistant",
  "uuid": "1767b48e-dd12-42b6-b282-f7a8e6373c09",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "a6ae7e35-390a-442a-93d4-9958c82c9e3b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Huxd6tgZmMAF1BcTukw4RG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4226,
      "cache_creation_input_tokens": 3649,
      "cache_read_input_tokens": 37045,
      "output_tokens": 2157,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3649,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 4226,
          "output_tokens": 2157,
          "cache_read_input_tokens": 37045,
          "cache_creation_input_tokens": 3649,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3649
          },
          "type": "message"
        }
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

_source line 28 · 2026-05-19T13:55:29.222Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_019bh4B8Yuda5EY1kRFYsUMX`</summary>

```json
{
  "project": "struct_self_consist_ie",
  "file": "paper_provenance.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1767b48e-dd12-42b6-b282-f7a8e6373c09",
  "isSidechain": false,
  "requestId": "req_011CbC3LnYDy8MNiyH2QdQNP",
  "type": "assistant",
  "uuid": "48ec8556-919d-4a44-b77b-41d41a712173",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "a6ae7e35-390a-442a-93d4-9958c82c9e3b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Huxd6tgZmMAF1BcTukw4RG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4226,
      "cache_creation_input_tokens": 3649,
      "cache_read_input_tokens": 37045,
      "output_tokens": 2157,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3649,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 4226,
          "output_tokens": 2157,
          "cache_read_input_tokens": 37045,
          "cache_creation_input_tokens": 3649,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3649
          },
          "type": "message"
        }
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

_source line 29 · 2026-05-19T13:55:29.242Z_

<details><summary>↩ Tool result · `toolu_019bh4B8Yuda5EY1kRFYsUMX`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/paper_provenance.yaml\", \"content\": \"paper:\\n  title: 'Strong Predictors, Weak Selectors: A Systematic Comparison of Confidence\\n    Signals for Test-Time Scaling in Information Extraction'\\n  version: 169\\n  generated_at: '2026-05-18T15:39:48.035618+00:00'\\n  source: manual provenance build by Paper Agent\\nclaims:\\n- id: c001_voting_rho_scierc_ner\\n  text: Voting Confidence achieves ρ=0.379 on SciERC NER (corrected from 0.502 truncation\\n    artifact)\\n  sections:\\n  - abstract\\n  - introduction\\n  - experiments\\n  - conclusion\\n  - discussion\\n  - related_work\\n  tier: 1\\n  evidence:\\n  - exp_id: exp_012_rerun_1024\\n    metric: ner.voting_rho_full\\n    value: 0.379\\n  note: Old value 0.502 from exp_015 was inflated by max_tokens=512 truncation. Corrected\\n    via exp_012_rerun_1024 (max_tokens=1024).\\n- id: c002_auroc_dissociation_scierc\\n  text: ρ-AUROC dissociation on SciERC — EM leads AUROC (NER 0.749, RE 0.706) while\\n    Voting leads ρ (NER 0.379, RE 0.422)\\n  sections:\\n  - abstract\\n  - introduction\\n  - experiments\\n  - conclusion\\n  - discussion\\n  tier: 1\\n  evidence:\\n  - exp_id: exp_012_rerun_1024\\n    metric: ner.em_auroc\\n    value: 0.749\\n  - exp_id: exp_012_rerun_1024\\n    metric: re.em_auroc\\n    value: 0.706\\n  - exp_id: exp_012_rerun_1024\\n    metric: ner.voting_auroc\\n    value: 0.684\\n  note: Old Table 1 had Voting NER AUROC=.741 (from exp_015 truncated). Corrected\\n    to .684 via exp_012_rerun_1024. EM now leads AUROC on both NER and RE. Headline\\n    claim changed from \\\"entity voting achieves ρ=0.38 and AUROC=0.74\\\" to split ρ (Voting\\n    0.38) / AUROC (EM 0.75) claim.\\n- id: c003_sj_rho_scierc_ner\\n  text: SJ achieves ρ=0.360 on SciERC NER (corrected from 0.357)\\n  sections:\\n  - experiments\\n  tier: 1\\n  evidence:\\n  - exp_id: exp_012_rerun_1024\\n    metric: ner.sj_rho_full\\n    value: 0.36\\n  - exp_id: exp_004_re_diagnostic\\n    metric: bootstrap_ci_95.ner_sj\\n    value:\\n    - 0.2946\\n    - 0.4586\\n- id: c004_voting_leads_re\\n  text: Voting leads RE full set (ρ=0.350, corrected from 0.422)\\n  sections:\\n  - experiments\\n  tier: 1\\n  evidence:\\n  - exp_id: exp_012_rerun_1024\\n    metric: re.voting_rho_full\\n    value: 0.35\\n  note: Corrected from exp_015_metrics_expansion (0.4217) via exp_012_rerun_1024.\\n- id: c005_fk_beats_sj_re\\n  text: FK (ρ=0.275) exceeds SJ (ρ=0.250) on RE—a reversal from NER\\n  sections:\\n  - experiments\\n  tier: 1\\n  evidence:\\n  - exp_id: exp_012_rerun_1024\\n    metric: re.fk_rho_full\\n    value: 0.275\\n  - exp_id: exp_012_rerun_1024\\n    metric: re.sj_rho_full\\n    value: 0.25\\n  note: Corrected from exp_015 (FK 0.253, SJ 0.211) via exp_012_rerun_1024.\\n- id: c006_re_40pct_zero_f1\\n  text: 40% of RE instances receive zero F1 (N=8, seed=42; 159/397)\\n  sections:\\n  - experiments\\n  - discussion\\n  tier: 1\\n  evidence:\\n  - exp_id: mvp_pilot_004\\n    metric: re_sample_f1_pct_zero\\n    value: 44.3\\n    note: 44.3% from mvp_pilot_004; paper uses 40% from primary config (N=8, seed=42)\\n  - exp_id: exp_008_re_n16_v2\\n    metric: f1_zero_pct\\n    value: 44.3\\n    note: 44.3% at N=16; zero-F1 fraction varies with N and seed\\n- id: c007_em_leads_conll\\n  text: EM leads CoNLL with ρ=0.451 and AUROC=0.816\\n  sections:\\n  - experiments\\n  tier: 1\\n  evidence:\\n  - exp_id: exp_002\\n    metric: em_rho_full\\n    value: 0.4507\\n  - exp_id: exp_002\\n    metric: em_auroc_full\\n    value: 0.8156\\n  - exp_id: exp_015_v2\\n    metric: auroc_best.EM.conll_ner\\n    value: 0.8156\\n- id: c008_cross_model_sj_stability\\n  text: 'SJ cross-model gap: ρ=0.436 (Qwen) vs 0.431 (LLaMA), Δ=0.005'\\n  sections:\\n  - experiments\\n  tier: 1\\n  evidence:\\n  - exp_id: exp_002\\n    metric: sj_rho_full\\n    value: 0.4357\\n  - exp_id: exp_017_llama_conll_infer\\n    metric: full.SJ_rho\\n    value: 0.4314\\n- id: c009_logprob_paradox\\n  text: Logprob achieves highest AUROC (0.761) yet lowest ρ (0.307) on CoNLL LLaMA\\n  sections:\\n  - experiments\\n  - discussion\\n  tier: 1\\n  evidence:\\n  - exp_id: exp_017_llama_conll_infer\\n    metric: full.logprob_AUROC\\n    value: 0.761\\n  - exp_id: exp_017_llama_conll_infer\\n    metric: full.logprob_rho\\n    value: 0.3072\\n- id: c010_conll_oracle_headroom\\n  text: 'CoNLL oracle headroom: +4.2pp (Qwen), +1.8pp (LLaMA)'\\n  sections:\\n  - experiments\\n  tier: 1\\n  evidence:\\n  - exp_id: exp_002\\n    metric: oracle_headroom\\n    value: 0.042\\n  - exp_id: exp_017_llama_conll_infer\\n    metric: oracle_headroom\\n    value: 0.0177\\n- id: c011_ner_no_reliable_selection\\n  text: No signal reliably surpasses greedy on NER (logprob +0.6pp, p=0.39, 3-seed\\n    bootstrap)\\n  sections:\\n  - abstract\\n  - introduction\\n  - experiments\\n  - conclusion\\n  - discussion\\n  - related_work\\n  tier: 1\\n  evidence:\\n  - exp_id: exp_016_rerun_1024_bootstrap\\n    metric: selection_f1_ner\\n    value:\\n      greedy: 0.644\\n      logprob: 0.65\\n      sj: 0.645\\n      voting: 0.634\\n      random: 0.608\\n      oracle: 0.776\\n  - exp_id: exp_016_rerun_1024_bootstrap\\n    metric: bootstrap_selection_test\\n    value:\\n      logprob_vs_greedy_p: 0.39\\n      ci_95:\\n      - -0.03\\n      - 0.042\\n      cohens_d: 0.038\\n      sign_test: 61W/70L\\n  note: 3-seed bootstrap confirms +0.6pp is NOT statistically significant. Unified\\n    with c012 — no signal reliably helps on either task.\\n- id: c012_re_no_signal_beats_greedy\\n  text: No signal surpasses greedy on RE; logprob drops to −0.9pp\\n  sections:\\n  - abstract\\n  - introduction\\n  - experiments\\n  - conclusion\\n  - discussion\\n  tier: 1\\n  evidence:\\n  - exp_id: exp_016_rerun_1024_bootstrap\\n    metric: selection_f1_re\\n    value:\\n      greedy: 0.404\\n      logprob: 0.395\\n      sj: 0.386\\n      voting: 0.359\\n      random: 0.354\\n      oracle: 0.585\\n  note: CLAIM REVERSED from exp_016 (max_tokens=512). Old claim was \\\"only logprob\\n    helps on RE (+2.3pp)\\\". Corrected via exp_016_rerun_1024_bootstrap.\\n- id: c013_oracle_headroom_ner\\n  text: Oracle upper bound 0.776, 13.2pp above greedy 0.644 on NER\\n  sections:\\n  - experiments\\n  - discussion\\n  tier: 1\\n  evidence:\\n  - exp_id: exp_016_rerun_1024_bootstrap\\n    metric: selection_f1_ner.oracle\\n    value: 0.776\\n  - exp_id: exp_016_rerun_1024_bootstrap\\n    metric: selection_f1_ner.greedy\\n    value: 0.644\\n- id: c014_re_oracle_headroom\\n  text: 'RE oracle gap: 18.1pp (0.585 vs 0.404)'\\n  sections:\\n  - experiments\\n  - discussion\\n  tier: 1\\n  evidence:\\n  - exp_id: exp_016_rerun_1024_bootstrap\\n    metric: selection_f1_re.oracle\\n    value: 0.585\\n  - exp_id: exp_016_rerun_1024_bootstrap\\n    metric: selection_f1_re.greedy\\n    value: 0.404\\n- id: c015_ensemble_auroc\\n  text: SJ+Voting ensemble AUROC=0.666, below best individual signal EM (0.749)\\n  sections:\\n  - discussion\\n  tier: 1\\n  evidence:\\n  - exp_id: exp_016_rerun_1024_bootstrap\\n    metric: ensemble_ner_auroc\\n    value: 0.666\\n  note: Ensemble does NOT improve over best individual. Changed from positive to negative\\n    finding.\\n- id: c016_ece_calibration\\n  text: NER reasonably well-calibrated (calibration ECE 0.069-0.096), RE shows greater\\n    miscalibration (ECE 0.109-0.339)\\n  sections:\\n  - experiments\\n  tier: 1\\n  evidence:\\n  - exp_id: exp_016_rerun_1024_bootstrap\\n    metric: calibration_ece\\n    value:\\n      ner_range: 0.069-0.096\\n      re_range: 0.109-0.339\\n  note: Previous c016 used binary ECE (0.27-0.77) which was incorrect metric. Calibration\\n    ECE (signal confidence → mean F1 deviation) shows NER is well-calibrated, RE has\\n    moderate miscalibration. Consistent with fig_reliability_1024.\\n- id: c017_fisher_z_ner_vs_re\\n  text: 'Fisher''s z-test ρ_SJ NER vs RE: z=2.31, p=0.021'\\n  sections:\\n  - experiments\\n  tier: 1\\n  evidence:\\n  - exp_id: exp_004_re_diagnostic\\n    metric: fisher_z_ner_vs_re.sj_z\\n    value: 2.31\\n  - exp_id: exp_004_re_diagnostic\\n    metric: fisher_z_ner_vs_re.sj_p\\n    value: 0.0209\\n- id: c018_per_relation_diagnostic\\n  text: Feature-Of ρ≈0.004, Hyponym-Of ρ=0.646\\n  sections:\\n  - experiments\\n  tier: 1\\n  evidence:\\n  - exp_id: exp_004_re_diagnostic\\n    metric: per_relation_type.FEATURE-OF.rho_sj\\n    value: 0.004\\n  - exp_id: exp_004_re_diagnostic\\n    metric: per_relation_type.HYPONYM-OF.rho_fk\\n    value: 0.646\\n- id: c019_entity_span_errors\\n  text: Entity span errors account for 55.5% of RE false negatives\\n  sections:\\n  - experiments\\n  tier: 1\\n  evidence:\\n  - exp_id: exp_004_re_diagnostic\\n    metric: error_propagation\\n    value: head_error 17.7% + tail_error (derived) + head_tail_error 15.9% + full_error\\n      21.7% → entity span errors ~55.5%\\n  note: Computed from error_propagation breakdown in exp_004\\n- id: c020_capability_stratification_ner\\n  text: SJ ρ=0.547 on SciERC instances with 6+ entities, vs 0.415 for 1-2 entities\\n  sections:\\n  - experiments\\n  tier: 1\\n  evidence:\\n  - exp_id: exp_009_capability_stratification\\n    metric: scierc_ner.by_ent_count.6plus_sj_rho\\n    value: 0.547\\n  - exp_id: exp_009_capability_stratification\\n    metric: scierc_ner.by_ent_count.1_2_sj_rho\\n    value: 0.415\\n- id: c021_wnut_boundary\\n  text: 'WNUT-17: SJ ρ=0.089 (p=0.020), 54% zero F1'\\n  sections:\\n  - experiments\\n  - conclusion\\n  tier: 1\\n  evidence:\\n  - exp_id: exp_003_wnut17_eval\\n    metric: rho_sj\\n    value: 0.089\\n  - exp_id: exp_003_wnut17_eval\\n    metric: sample_f1_pct_zero\\n    value: 53.7\\n  note: 'Corrected 2026-05-16: paper uses ρ=0.089 from exp003_wnut17_eval (gold-filtered\\n    n=689, p=0.020). Old value 0.062 was untraceable — only in deprecated draft.'\\n- id: c022_wnut_logprob_negative\\n  text: WNUT logprob shows strong negative correlation\\n  sections:\\n  - experiments\\n  tier: 1\\n  evidence:\\n  - exp_id: exp_003_ner_wnut17\\n    metric: ner.rho_logprob_full\\n    value: -0.414\\n  - exp_id: exp_003_wnut17_eval\\n    metric: rho_logprob_full\\n    value: -0.409\\n- id: c023_re_sent_length_sj\\n  text: 'RE SJ ρ increases with sentence length: Q1 0.110 → Q4 0.473 (Fisher p=0.004)'\\n  sections:\\n  - experiments\\n  tier: 2\\n  evidence:\\n  - exp_id: exp_009_v2_re_rerun\\n    metric: by_sent_len_quartiles\\n    value:\\n      Q1_sj_rho: 0.11\\n      Q4_sj_rho: 0.473\\n      fisher_z_p: 0.004\\n  note: 'Corrected 2026-05-16: source is exp_009_v2_re_rerun (gold-filtered n=397).\\n    Old registry exp_009 values (Q1=0.447, Q4=0.540) used unfiltered n=551.'\\n- id: c024_high_complexity_re_subset\\n  text: 'High-complexity RE subset (n=81): Voting ρ=0.630, logprob ρ=0.554, SJ ρ=0.502'\\n  sections:\\n  - experiments\\n  tier: 2\\n  evidence:\\n  - exp_id: exp_009_capability_stratification\\n    metric: scierc_re.by_rel_count\\n    value:\\n      6plus_sj_rho: 0.527\\n  note: Registry has 6plus_sj_rho=0.527; paper may use exp_009_v2 data. Voting and\\n    logprob values not in registry summary.\\n- id: c025_temperature_sj_stable\\n  text: SJ NER ρ shifts from 0.388 (T=0.7) to 0.360 (T=1.0), Δ=0.028\\n  sections:\\n  - experiments\\n  tier: 1\\n  evidence:\\n  - exp_id: exp_005\\n    metric: sj_rho_t07_ner\\n    value: 0.388\\n  - exp_id: exp_012_rerun_1024\\n    metric: ner.sj_rho_full\\n    value: 0.36\\n  note: T=0.7 data from exp_005; T=1.0 from exp_015\\n- id: c026_n_scaling_sj\\n  text: SJ N=8→N=16 improves ρ from 0.360 to 0.412±0.025 (3-seed, +0.052) on Qwen\\n    SciERC NER\\n  sections:\\n  - experiments\\n  tier: 1\\n  evidence:\\n  - exp_id: exp_012_rerun_1024\\n    metric: ner.sj_rho_full\\n    value: 0.36\\n  - exp_id: exp_001_seed42_v2\\n    metric: sj_rho_full\\n    value: 0.428\\n  - exp_id: exp_001_seed123_v2\\n    metric: sj_rho_full\\n    value: 0.424\\n  - exp_id: exp_001_seed456_v2_ner\\n    metric: full.SJ.rho\\n    value: 0.384\\n  note: '3-seed mean: (0.428+0.424+0.384)/3 ≈ 0.412, σ=0.025'\\n- id: c027_llama_conll_3seed\\n  text: 'LLaMA CoNLL N=16 3-seed: SJ ρ=0.463±0.007, logprob ρ=0.310±0.005'\\n  sections:\\n  - experiments\\n  tier: 1\\n  evidence:\\n  - exp_id: exp_017_llama_conll_n16\\n    metric: full.SJ_rho\\n    value: 0.4642\\n  - exp_id: exp_017_llama_conll_n16_s123\\n    metric: full.SJ_rho\\n    value: 0.4698\\n  - exp_id: exp_017_llama_conll_n16_s456\\n    metric: full.SJ_rho\\n    value: 0.4552\\n  - exp_id: exp_017_llama_conll_n16\\n    metric: full.logprob_rho\\n    value: 0.3058\\n  - exp_id: exp_017_llama_conll_n16_s123\\n    metric: full.logprob_rho\\n    value: 0.3161\\n  - exp_id: exp_017_llama_conll_n16_s456\\n    metric: full.logprob_rho\\n    value: 0.3078\\n- id: c028_loo_sj_circularity\\n  text: LOO-SJ Δρ=-0.014, max per-instance Δρ=3.1×10⁻⁴—circularity negligible\\n  sections:\\n  - experiments\\n  tier: 1\\n  evidence:\\n  - exp_id: exp_015_v2\\n    metric: loo_sj.max_delta_rho\\n    value: 0.000305\\n  - exp_id: exp_015_v2\\n    metric: loo_sj.all_no_circularity\\n    value: true\\n- id: c029_llama_scierc_cross_model\\n  text: 'LLaMA replicates structural-over-surface on SciERC: NER SJ ρ=0.363 > FK ρ=0.327;\\n    conditional RE SJ ρ=0.405 > FK ρ=0.259'\\n  sections:\\n  - experiments\\n  tier: 1\\n  evidence:\\n  - exp_id: exp_007_llama_inference\\n    metric: ner.rho_sj\\n    value: 0.363\\n  - exp_id: exp_007_llama_inference\\n    metric: ner.rho_fk\\n    value: 0.327\\n  - exp_id: exp_007_llama_inference\\n    metric: re.sj_rho_cond\\n    value: 0.405\\n  - exp_id: exp_007_llama_inference\\n    metric: re.fk_rho_cond\\n    value: 0.259\\n- id: c030_em_conditional_dominance\\n  text: 'EM ranks #1 on conditional set across all 4 configurations'\\n  sections:\\n  - experiments\\n  tier: 1\\n  evidence:\\n  - exp_id: exp_015_metrics_expansion\\n    metric: ner.em_rho_cond\\n    value: 0.3427\\n  - exp_id: exp_015_metrics_expansion\\n    metric: re.em_rho_cond\\n    value: 0.3607\\n  - exp_id: exp_002_conll_n16\\n    metric: conditional.EM_rho\\n    value: 0.4658\\n  - exp_id: exp_017_llama_conll_n16_s123\\n    metric: conditional.EM_rho\\n    value: 0.4732\\n  note: 'Paper cites EM conditional: SciERC NER 0.408, RE 0.485, CoNLL Qwen N=16 0.466,\\n    CoNLL LLaMA 3-seed 0.462. Registry has slightly different values from different\\n    seed/N combinations.'\\n- id: c031_em_conditional_scierc\\n  text: 'EM conditional: NER ρ=0.408, RE ρ=0.485'\\n  sections:\\n  - experiments\\n  tier: 1\\n  evidence:\\n  - exp_id: exp_001_ner_n16_scierc\\n    metric: ner_cond_em_rho\\n    value: 0.414\\n  - exp_id: exp_001_ner_n16_scierc\\n    metric: re_cond_em_rho\\n    value: 0.475\\n  note: 'Paper rounds: 0.414→0.408, 0.475→0.485. May use different seed/N baseline.'\\n- id: c032_logprob_re_cond_collapse\\n  text: Logprob conditional RE collapses to ρ=0.011\\n  sections:\\n  - experiments\\n  tier: 1\\n  evidence:\\n  - exp_id: exp_012_rerun_1024\\n    metric: re_cond.logprob.rho\\n    value: 0.0112\\n  note: 'Corrected 2026-05-16: source is exp_012_rerun_1024 (greedy_f1>0 filter, n=238).\\n    Old exp_015 value 0.1457 used wrong filter (any sample F1>0, n=331). Old text\\n    0.002 was stale and untraceable.'\\n- id: c033_sj_n16_cond_re\\n  text: At N=16, SJ maintains ρ=0.308 on conditional RE while logprob drops to -0.026\\n  sections:\\n  - experiments\\n  - discussion\\n  tier: 1\\n  evidence:\\n  - exp_id: exp_008_re_n16_v2\\n    metric: sj_rho_cond\\n    value: 0.308\\n- id: c034_structural_over_logprob_n16\\n  text: Structural-over-logprob advantage holds across all 4 N=16 settings (Δ=+0.124\\n    to +0.175)\\n  sections:\\n  - experiments\\n  - discussion\\n  tier: 1\\n  evidence:\\n  - exp_id: exp_001_ner_n16_scierc\\n    metric: ner_voting_conf_rho\\n    value: 0.399\\n  - exp_id: exp_001_ner_n16_scierc\\n    metric: ner_logprob_rho\\n    value: 0.237\\n  - exp_id: exp_002_conll_n16\\n    metric: full.EM_rho\\n    value: 0.4627\\n  - exp_id: exp_002_conll_n16\\n    metric: full.logprob_rho\\n    value: 0.3146\\n  - exp_id: exp_007_llama_n16\\n    metric: full.voting_conf_rho\\n    value: 0.4515\\n  - exp_id: exp_007_llama_n16\\n    metric: full.logprob_rho\\n    value: 0.2041\\n  - exp_id: exp_017_llama_conll_n16\\n    metric: full.SJ_rho\\n    value: 0.4642\\n  - exp_id: exp_017_llama_conll_n16\\n    metric: full.logprob_rho\\n    value: 0.3058\\n- id: c035_n_scaling_diminishing\\n  text: 'SJ N-scaling gains are sublinear: +0.052 Qwen SciERC, +0.032 LLaMA CoNLL'\\n  sections:\\n  - discussion\\n  tier: 1\\n  evidence:\\n  - exp_id: exp_001_seed42_v2\\n    metric: sj_rho_full\\n    value: 0.428\\n  - exp_id: exp_015_metrics_expansion\\n    metric: ner.sj_rho_full\\n    value: 0.3565\\n  - exp_id: exp_017_llama_conll_n16\\n    metric: full.SJ_rho\\n    value: 0.4642\\n  - exp_id: exp_017_llama_conll_infer\\n    metric: full.SJ_rho\\n    value: 0.4314\\n  note: 'Qwen SciERC: 0.412 (3-seed mean) - 0.360 = +0.052. LLaMA CoNLL: 0.463 (3-seed)\\n    - 0.431 = +0.032'\\n- id: c036_sj_ece_calibration\\n  text: '[DEPRECATED] SJ achieves lowest calibration error (ECE=0.075-0.102 across\\n    settings)'\\n  sections: []\\n  tier: X\\n  evidence: []\\n  note: DEPRECATED — reversed by c016_ece_miscalibration. Old ECE values (0.075-0.102)\\n    were from exp_015 (max_tokens=512 truncation artifact). Corrected data shows all\\n    signals ECE 0.27-0.77.\\n- id: C001\\n  location:\\n    section: abstract\\n    paragraph: 0\\n    sentence: 0\\n  text: No signal significantly improves sample selection over greedy decoding despite\\n    13-18pp oracle headroom\\n  type: empirical\\n  evidence:\\n  - exp_012_rerun_1024\\n  decisions:\\n  - D070\\n  - D071\\n  deprecated: false\\n- id: C003\\n  location:\\n    section: abstract\\n    paragraph: 0\\n    sentence: 0\\n  text: LP scores compressed into effective ties for 60% of instances under constrained\\n    decoding\\n  type: empirical\\n  evidence:\\n  - exp_012_rerun_1024\\n  decisions: []\\n  deprecated: false\\n- id: C006\\n  location:\\n    section: abstract\\n    paragraph: 0\\n    sentence: 0\\n  text: Where LP compression is absent, selection recovers +2.9pp (p=0.01)\\n  type: empirical\\n  evidence:\\n  - exp_012_rerun_1024\\n  decisions: []\\n  deprecated: false\\n- id: C010\\n  location:\\n    section: abstract\\n    paragraph: 0\\n    sentence: 0\\n  text: Constrained-decoding score compression is the primary bottleneck\\n  type: empirical\\n  evidence:\\n  - exp_012_rerun_1024\\n  decisions: []\\n  deprecated: false\\n- id: C011\\n  location:\\n    section: discussion\\n    paragraph: 0\\n    sentence: 0\\n  text: LP carries useful per-sample quality information; score compression is the\\n    primary bottleneck\\n  type: empirical\\n  evidence:\\n  - exp_012_rerun_1024\\n  decisions:\\n  - D071\\n  deprecated: false\\n- id: C013\\n  location:\\n    section: discussion\\n    paragraph: 0\\n    sentence: 0\\n  text: MBR utility correlates with F1 across instances but not within\\n  type: empirical\\n  evidence:\\n  - exp_012_rerun_1024\\n  decisions: []\\n  deprecated: false\\n- id: C016\\n  location:\\n    section: discussion\\n    paragraph: 0\\n    sentence: 0\\n  text: Free-form ablation would test if bottleneck is decoding-regime-specific\\n  type: planned\\n  evidence: []\\n  decisions:\\n  - D071\\n  deprecated: false\\n- id: C017\\n  location:\\n    section: conclusion\\n    paragraph: 0\\n    sentence: 0\\n  text: Consistency signals effective QE (rho up to 0.38, AUROC up to 0.75) but fail\\n    at selection\\n  type: empirical\\n  evidence:\\n  - exp_012_rerun_1024\\n  decisions: []\\n  deprecated: false\\n- id: C019\\n  location:\\n    section: conclusion\\n    paragraph: 0\\n    sentence: 0\\n  text: LP fails due to constrained-decoding score compression\\n  type: empirical\\n  evidence:\\n  - exp_012_rerun_1024\\n  decisions: []\\n  deprecated: false\\n- id: C022\\n  location:\\n    section: conclusion\\n    paragraph: 0\\n    sentence: 0\\n  text: RE findings preliminary, single benchmark\\n  type: scope_limitation\\n  evidence:\\n  - exp_012_rerun_1024\\n  decisions: []\\n  deprecated: false\\n- id: C023\\n  location:\\n    section: sections/discussion\\n    paragraph: 0\\n    sentence: 0\\n  text: Entity-token LP exhibits 4x higher within-instance variance than full-sequence\\n    LP on SciERC, but selection performs worse (-2.0pp)\\n  type: quantitative\\n  evidence:\\n  - exp_id: exp_entity_token_lp\\n    metric: scierc_entity_lp_variance_ratio\\n    value: 4.0x\\n  - exp_id: exp_entity_token_lp\\n    metric: scierc_entity_lp_selection_delta\\n    value: -1.68\\n  decisions: []\\n  deprecated: false\\n- id: C024\\n  location:\\n    section: sections/discussion\\n    paragraph: 0\\n    sentence: 0\\n  text: On CoNLL, entity-token LP variance collapses to near-zero (median 2e-10) with\\n    79% tied\\n  type: quantitative\\n  evidence:\\n  - exp_id: exp_entity_token_lp\\n    metric: conll_entity_lp_variance_median\\n    value: 2e-10\\n  - exp_id: exp_entity_token_lp\\n    metric: conll_entity_lp_tied_fraction\\n    value: 0.794\\n  decisions: []\\n  deprecated: false\\n- id: C025\\n  location:\\n    section: sections/discussion\\n    paragraph: 0\\n    sentence: 0\\n  text: Entity-token LP rules out format-token dilution as primary cause; points to\\n    intrinsic model overconfidence on entity tokens\\n  type: interpretive\\n  evidence:\\n  - exp_id: exp_entity_token_lp\\n  decisions: []\\n  deprecated: false\\n- id: C026\\n  location:\\n    section: sections/limitations\\n    paragraph: 0\\n    sentence: 0\\n  text: Entity-token LP is the only tested remedy; LP×VC and calibration approaches\\n    are unexplored\\n  type: scope\\n  evidence:\\n  - exp_id: exp_entity_token_lp\\n  decisions: []\\n  deprecated: false\\n- id: C027\\n  location:\\n    section: sections/introduction\\n    paragraph: 0\\n    sentence: 0\\n  text: 'C1 reframe: instance-level nature is setup, LP compression + MBR within-instance\\n    failure are the findings'\\n  type: structural\\n  evidence: []\\n  decisions: []\\n  deprecated: false\\n- id: C028\\n  location:\\n    section: sections/introduction\\n    paragraph: 0\\n    sentence: 0\\n  text: 'SF4: 60% tied replaced with pooled within-instance ρ(LP,F1)=0.248 continuous\\n    characterization'\\n  type: structural\\n  evidence: []\\n  decisions: []\\n  deprecated: false\\n- id: C029\\n  location:\\n    section: sections/introduction\\n    paragraph: 0\\n    sentence: 0\\n  text: 'C2 reframe: entity-token LP added as diagnostic ablation contribution'\\n  type: structural\\n  evidence:\\n  - exp_id: exp_entity_token_lp\\n  decisions: []\\n  deprecated: false\\n- id: C030\\n  location:\\n    section: sections/abstract\\n    paragraph: 0\\n    sentence: 0\\n  text: 'SF3: RE removed from abstract; SF1: ρ=0.38 sourced to SciERC primary, up\\n    to 0.45 on ceiling control; MF2(a): benchmark roles explicit; M2: streamlined\\n    from 9 to 6 sentences'\\n  type: structural\\n  evidence: []\\n  decisions: []\\n  deprecated: false\\n- id: C031\\n  location:\\n    section: sections/discussion\\n    paragraph: 0\\n    sentence: 0\\n  text: 21% of SciERC instances produce identical F1 across all N samples\\n  type: quantitative\\n  evidence: Q1 within-instance analysis\\n  decisions: []\\n  deprecated: false\\n- id: C032\\n  location:\\n    section: sections/discussion\\n    paragraph: 0\\n    sentence: 0\\n  text: 58% of CoNLL instances produce identical F1 across all N samples\\n  type: quantitative\\n  evidence: Q1 within-instance analysis\\n  decisions: []\\n  deprecated: false\\n- id: C033\\n  location:\\n    section: sections/discussion\\n    paragraph: 0\\n    sentence: 0\\n  text: 13% of SciERC instances yield constant utility scores\\n  type: quantitative\\n  evidence: Q1 within-instance analysis\\n  decisions: []\\n  deprecated: false\\n- id: C034\\n  location:\\n    section: sections/discussion\\n    paragraph: 0\\n    sentence: 0\\n  text: 49% of CoNLL instances yield constant utility scores\\n  type: quantitative\\n  evidence: Q1 within-instance analysis\\n  decisions: []\\n  deprecated: false\\n- id: C035\\n  location:\\n    section: sections/discussion\\n    paragraph: 0\\n    sentence: 0\\n  text: SJ median within-instance rho = 0.524 on SciERC\\n  type: quantitative\\n  evidence: Q1 within-instance analysis\\n  decisions: []\\n  deprecated: false\\n- id: C036\\n  location:\\n    section: sections/discussion\\n    paragraph: 0\\n    sentence: 0\\n  text: SJ median within-instance rho = 0.994 on CoNLL\\n  type: quantitative\\n  evidence: Q1 within-instance analysis\\n  decisions: []\\n  deprecated: false\\n- id: C037\\n  location:\\n    section: sections/discussion\\n    paragraph: 0\\n    sentence: 0\\n  text: MBR closes 23% of oracle gap on non-degenerate SciERC instances\\n  type: quantitative\\n  evidence: Q1 within-instance analysis\\n  decisions: []\\n  deprecated: false\\n- id: C038\\n  location:\\n    section: sections/discussion\\n    paragraph: 0\\n    sentence: 0\\n  text: MBR closes 41% of oracle gap on non-degenerate CoNLL instances\\n  type: quantitative\\n  evidence: Q1 within-instance analysis\\n  decisions: []\\n  deprecated: false\\n- id: C039\\n  location:\\n    section: sections/discussion\\n    paragraph: 0\\n    sentence: 0\\n  text: Greedy T=0 achieves F1=0.663 on SciERC, surpassing all N=8 selection strategies\\n  type: quantitative\\n  evidence: SF4 greedy data\\n  decisions: []\\n  deprecated: false\\n- id: C040\\n  location:\\n    section: sections/discussion\\n    paragraph: 0\\n    sentence: 0\\n  text: SciERC 3-epoch rho=0.32 vs 5-epoch rho=0.28; LP delta -1.18 vs +0.62 pp\\n  type: quantitative\\n  evidence: tab:epoch_scierc\\n  decisions: []\\n  deprecated: false\\n- id: C041\\n  location:\\n    section: sections/discussion\\n    paragraph: 0\\n    sentence: 0\\n  text: Entity-level majority voting yields +0.76pp on SciERC (5.8% gap recovery)\\n  type: quantitative\\n  evidence: []\\n  decisions: []\\n  deprecated: false\\n- id: C042\\n  location:\\n    section: sections/discussion\\n    paragraph: 0\\n    sentence: 0\\n  text: Entity-level majority voting yields -0.64pp on CoNLL\\n  type: quantitative\\n  evidence: []\\n  decisions: []\\n  deprecated: false\\n- id: C043\\n  location:\\n    section: sections/discussion\\n    paragraph: 0\\n    sentence: 0\\n  text: Entity-level majority voting yields -3.21pp on Few-NERD\\n  type: quantitative\\n  evidence: []\\n  decisions: []\\n  deprecated: false\\n- id: C044\\n  location:\\n    section: sections/discussion\\n    paragraph: 0\\n    sentence: 0\\n  text: On degenerate subsets, merge is uniformly negative across all three datasets\\n  type: quantitative\\n  evidence: []\\n  decisions: []\\n  deprecated: false\\n- id: C045\\n  location:\\n    section: sections/appendix\\n    paragraph: 0\\n    sentence: 0\\n  text: Exact permutation p=0.005 for per-type degeneracy-headroom correlation\\n  type: quantitative\\n  evidence: []\\n  decisions: []\\n  deprecated: false\\n- id: C046\\n  location:\\n    section: sections/appendix\\n    paragraph: 0\\n    sentence: 0\\n  text: Under conservative df=4 adjustment, p=0.033\\n  type: quantitative\\n  evidence: []\\n  decisions: []\\n  deprecated: false\\n- id: C047\\n  location:\\n    section: sections/appendix\\n    paragraph: 0\\n    sentence: 0\\n  text: 3-epoch SciERC mean within-instance rho=0.273\\n  type: quantitative\\n  evidence: []\\n  decisions: []\\n  deprecated: false\\n- id: C048\\n  location:\\n    section: sections/appendix\\n    paragraph: 0\\n    sentence: 0\\n  text: 5-epoch SciERC mean within-instance rho=0.179\\n  type: quantitative\\n  evidence: []\\n  decisions: []\\n  deprecated: false\\n- id: C049\\n  location:\\n    section: sections/appendix\\n    paragraph: 0\\n    sentence: 0\\n  text: 76.4% of instances show positive LP-quality correlation at 3 epochs\\n  type: quantitative\\n  evidence: []\\n  decisions: []\\n  deprecated: false\\n- id: C050\\n  location:\\n    section: sections/appendix\\n    paragraph: 0\\n    sentence: 0\\n  text: 64.1% of instances show positive LP-quality correlation at 5 epochs\\n  type: quantitative\\n  evidence: []\\n  decisions: []\\n  deprecated: false\\n- id: C051\\n  location:\\n    section: sections/appendix\\n    paragraph: 0\\n    sentence: 0\\n  text: Epoch-to-epoch alignment variation is 0.057 median rho, small vs cross-dataset\\n    gap\\n  type: quantitative\\n  evidence: []\\n  decisions: []\\n  deprecated: false\\n- id: C052\\n  location:\\n    section: sections/appendix\\n    paragraph: 0\\n    sentence: 0\\n  text: 'Optimal DALS tau spans 2 orders of magnitude: FN 0.001, SciERC 0.05, CoNLL\\n    0.10'\\n  type: quantitative\\n  evidence: []\\n  decisions: []\\n  deprecated: false\\n- id: C053\\n  location:\\n    section: sections/appendix\\n    paragraph: 0\\n    sentence: 0\\n  text: LOO regret ranges from 0.51 to 1.21pp\\n  type: quantitative\\n  evidence: []\\n  decisions: []\\n  deprecated: false\\n- id: C054\\n  location:\\n    section: sections/appendix\\n    paragraph: 0\\n    sentence: 0\\n  text: Even with oracle tau, CoNLL remains at -0.31pp\\n  type: quantitative\\n  evidence: []\\n  decisions: []\\n  deprecated: false\\n- id: C055\\n  location:\\n    section: sections/appendix\\n    paragraph: 0\\n    sentence: 0\\n  text: 'SciERC entity merge best k=3: +1.57pp, 11.9% recovery'\\n  type: quantitative\\n  evidence: []\\n  decisions: []\\n  deprecated: false\\n- id: C056\\n  location:\\n    section: sections/appendix\\n    paragraph: 0\\n    sentence: 0\\n  text: 'CoNLL entity merge best k=3: -0.38pp, -9.0% recovery'\\n  type: quantitative\\n  evidence: []\\n  decisions: []\\n  deprecated: false\\n- id: C057\\n  location:\\n    section: sections/appendix\\n    paragraph: 0\\n    sentence: 0\\n  text: 'FewNERD entity merge best k=2: -0.43pp, -3.6% recovery'\\n  type: quantitative\\n  evidence: []\\n  decisions: []\\n  deprecated: false\\n- id: C058\\n  location:\\n    section: sections/experiments\\n    paragraph: 0\\n    sentence: 0\\n  text: 'Conditional decomp SciERC favorable: +2.47pp CI [+0.30, +4.70]'\\n  type: quantitative\\n  evidence: []\\n  decisions: []\\n  deprecated: false\\n- id: C059\\n  location:\\n    section: sections/experiments\\n    paragraph: 0\\n    sentence: 0\\n  text: 'Conditional decomp FewNERD favorable: +0.63pp CI [-0.02, +1.30], marginal'\\n  type: quantitative\\n  evidence: []\\n  decisions: []\\n  deprecated: false\\n- id: C060\\n  location:\\n    section: sections/experiments\\n    paragraph: 0\\n    sentence: 0\\n  text: 'Conditional decomp CoNLL favorable: -1.78pp CI [-2.83, -0.76], negative'\\n  type: quantitative\\n  evidence: []\\n  decisions: []\\n  deprecated: false\\n- id: C061\\n  location:\\n    section: sections/appendix\\n    paragraph: 0\\n    sentence: 0\\n  text: Entity-token LP has 4x higher within-instance variance (0.000644 vs 0.000161)\\n  type: quantitative\\n  evidence: []\\n  decisions: []\\n  deprecated: false\\n- id: C062\\n  location:\\n    section: sections/appendix\\n    paragraph: 0\\n    sentence: 0\\n  text: Entity-token LP rho=0.440 vs full-sequence 0.297\\n  type: quantitative\\n  evidence: []\\n  decisions: []\\n  deprecated: false\\n- id: C063\\n  location:\\n    section: sections/appendix\\n    paragraph: 0\\n    sentence: 0\\n  text: Entity-token LP selection -0.73pp vs full-sequence +0.35pp\\n  type: quantitative\\n  evidence: []\\n  decisions: []\\n  deprecated: false\\ntables:\\n- id: tab:notation\\n  section: method\\n  caption: Notation used throughout the paper\\n  evidence: []\\n  note: Notation table—no experimental data.\\n- id: tab:quality_estimation\\n  section: experiments\\n  caption: Quality estimation across tasks and models (Spearman ρ and AUROC)\\n  evidence:\\n  - exp_id: exp_012_rerun_1024\\n    role: SciERC NER ρ values (N=8, Qwen) — corrected from exp_015 (truncation artifact)\\n  - exp_id: exp_015_metrics_expansion\\n    role: SciERC RE ρ values (N=8, Qwen) — RE values unaffected by truncation fix\\n  - exp_id: exp_015_v2\\n    role: AUROC values across settings\\n  - exp_id: exp_002\\n    role: CoNLL Qwen N=8 ρ and AUROC\\n  - exp_id: exp_017_llama_conll_infer\\n    role: CoNLL LLaMA N=8 ρ and AUROC\\n  - exp_id: exp_017_llama_conll_n16\\n    role: LLaMA CoNLL N=16 3-seed (seed=42)\\n  - exp_id: exp_017_llama_conll_n16_s123\\n    role: LLaMA CoNLL N=16 3-seed (seed=123)\\n  - exp_id: exp_017_llama_conll_n16_s456\\n    role: LLaMA CoNLL N=16 3-seed (seed=456)\\n- id: tab:selection\\n  section: experiments\\n  caption: Best-of-N selection F1 on SciERC (N=8, T=1.0)\\n  evidence:\\n  - exp_id: exp_016_signal_ensemble\\n    role: All selection F1 values (NER and RE)\\n- id: tab:robustness\\n  section: experiments\\n  caption: Signal robustness across configurations (Spearman ρ)\\n  evidence:\\n  - exp_id: exp_005\\n    role: Temperature block (T=0.7 vs T=1.0, Qwen SciERC)\\n  - exp_id: exp_015_metrics_expansion\\n    role: N=8 baseline values\\n  - exp_id: exp_001_seed42_v2\\n    role: N=16 SJ ρ seed=42\\n  - exp_id: exp_001_seed123_v2\\n    role: N=16 SJ ρ seed=123\\n  - exp_id: exp_001_seed456_v2_ner\\n    role: N=16 SJ ρ seed=456\\n  - exp_id: exp_017_llama_conll_n16\\n    role: 'Cross-model block: LLaMA CoNLL N=16 seed=42'\\n  - exp_id: exp_017_llama_conll_n16_s123\\n    role: 'Cross-model block: LLaMA CoNLL N=16 seed=123'\\n  - exp_id: exp_017_llama_conll_n16_s456\\n    role: 'Cross-model block: LLaMA CoNLL N=16 seed=456'\\nfigures:\\n- id: fig:overview\\n  section: introduction\\n  caption: The correlation-selection gap conceptual diagram\\n  evidence:\\n  - exp_id: exp_015_metrics_expansion\\n    role: Quality estimation data (ρ, AUROC for left panel)\\n  - exp_id: exp_016_signal_ensemble\\n    role: Selection F1 data (right panel)\\n- id: fig:signal_heatmap\\n  section: experiments\\n  caption: Quality estimation heatmap (Spearman ρ) across five signals and four configurations\\n  evidence:\\n  - exp_id: exp_015_metrics_expansion\\n    role: Full set ρ values for SciERC NER/RE (Qwen, N=8)\\n  - exp_id: exp_002\\n    role: CoNLL Qwen full set ρ values\\n  - exp_id: exp_001_ner_n16_scierc\\n    role: Conditional set ρ values\\n- id: fig:selection_gap\\n  section: experiments\\n  caption: The correlation-selection gap on SciERC (N=8)\\n  evidence:\\n  - exp_id: exp_016_signal_ensemble\\n    role: Best-of-N selection F1 bars and quality estimation ρ line\\n- id: fig:temperature_robustness\\n  section: experiments\\n  caption: Temperature robustness on SciERC (N=8)\\n  evidence:\\n  - exp_id: exp_005\\n    role: SJ, FK ρ values at T=0.7 and T=1.0\\n- id: fig:reliability\\n  section: experiments\\n  caption: Reliability diagrams on SciERC (N=8, T=1.0)\\n  evidence:\\n  - exp_id: exp_015_metrics_expansion\\n    role: Calibration/ECE data for all signals\\n  - exp_id: exp_002\\n    role: ECE values across signals\\n_completeness:\\n  coverage: 59/92\\n  claims: 87\\n  tables: 4\\n  figures: 5\\n  tier_counts:\\n    tier1: 0\\n    tier2: 59\\n    tier3: 33\\n    tierX: 0\\n  last_checked: '2026-05-18T15:39:48.035668+00:00'\\n\", \"total_chars\": 32730, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "48ec8556-919d-4a44-b77b-41d41a712173",
  "isSidechain": false,
  "promptId": "2279f609-b135-4e34-8568-a1f529688be0",
  "type": "user",
  "uuid": "510e364c-5ca9-4b9e-b58e-5f0d8977856b",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/paper_provenance.yaml\\\", \\\"content\\\": \\\"paper:\\\\n  title: 'Strong Predictors, Weak Selectors: A Systematic Comparison of Confidence\\\\n    Signals for Test-Time Scaling in Information Extraction'\\\\n  version: 169\\\\n  generated_at: '2026-05-18T15:39:48.035618+00:00'\\\\n  source: manual provenance build by Paper Agent\\\\nclaims:\\\\n- id: c001_voting_rho_scierc_ner\\\\n  text: Voting Confidence achieves ρ=0.379 on SciERC NER (corrected from 0.502 truncation\\\\n    artifact)\\\\n  sections:\\\\n  - abstract\\\\n  - introduction\\\\n  - experiments\\\\n  - conclusion\\\\n  - discussion\\\\n  - related_work\\\\n  tier: 1\\\\n  evidence:\\\\n  - exp_id: exp_012_rerun_1024\\\\n    metric: ner.voting_rho_full\\\\n    value: 0.379\\\\n  note: Old value 0.502 from exp_015 was inflated by max_tokens=512 truncation. Corrected\\\\n    via exp_012_rerun_1024 (max_tokens=1024).\\\\n- id: c002_auroc_dissociation_scierc\\\\n  text: ρ-AUROC dissociation on SciERC — EM leads AUROC (NER 0.749, RE 0.706) while\\\\n    Voting leads ρ (NER 0.379, RE 0.422)\\\\n  sections:\\\\n  - abstract\\\\n  - introduction\\\\n  - experiments\\\\n  - conclusion\\\\n  - discussion\\\\n  tier: 1\\\\n  evidence:\\\\n  - exp_id: exp_012_rerun_1024\\\\n    metric: ner.em_auroc\\\\n    value: 0.749\\\\n  - exp_id: exp_012_rerun_1024\\\\n    metric: re.em_auroc\\\\n    value: 0.706\\\\n  - exp_id: exp_012_rerun_1024\\\\n    metric: ner.voting_auroc\\\\n    value: 0.684\\\\n  note: Old Table 1 had Voting NER AUROC=.741 (from exp_015 truncated). Corrected\\\\n    to .684 via exp_012_rerun_1024. EM now leads AUROC on both NER and RE. Headline\\\\n    claim changed from \\\\\\\"entity voting achieves ρ=0.38 and AUROC=0.74\\\\\\\" to split ρ (Voting\\\\n    0.38) / AUROC (EM 0.75) claim.\\\\n- id: c003_sj_rho_scierc_ner\\\\n  text: SJ achieves ρ=0.360 on SciERC NER (corrected from 0.357)\\\\n  sections:\\\\n  - experiments\\\\n  tier: 1\\\\n  evidence:\\\\n  - exp_id: exp_012_rerun_1024\\\\n    metric: ner.sj_rho_full\\\\n    value: 0.36\\\\n  - exp_id: exp_004_re_diagnostic\\\\n    metric: bootstrap_ci_95.ner_sj\\\\n    value:\\\\n    - 0.2946\\\\n    - 0.4586\\\\n- id: c004_voting_leads_re\\\\n  text: Voting leads RE full set (ρ=0.350, corrected from 0.422)\\\\n  sections:\\\\n  - experiments\\\\n  tier: 1\\\\n  evidence:\\\\n  - exp_id: exp_012_rerun_1024\\\\n    metric: re.voting_rho_full\\\\n    value: 0.35\\\\n  note: Corrected from exp_015_metrics_expansion (0.4217) via exp_012_rerun_1024.\\\\n- id: c005_fk_beats_sj_re\\\\n  text: FK (ρ=0.275) exceeds SJ (ρ=0.250) on RE—a reversal from NER\\\\n  sections:\\\\n  - experiments\\\\n  tier: 1\\\\n  evidence:\\\\n  - exp_id: exp_012_rerun_1024\\\\n    metric: re.fk_rho_full\\\\n    value: 0.275\\\\n  - exp_id: exp_012_rerun_1024\\\\n    metric: re.sj_rho_full\\\\n    value: 0.25\\\\n  note: Corrected from exp_015 (FK 0.253, SJ 0.211) via exp_012_rerun_1024.\\\\n- id: c006_re_40pct_zero_f1\\\\n  text: 40% of RE instances receive zero F1 (N=8, seed=42; 159/397)\\\\n  sections:\\\\n  - experiments\\\\n  - discussion\\\\n  tier: 1\\\\n  evidence:\\\\n  - exp_id: mvp_pilot_004\\\\n    metric: re_sample_f1_pct_zero\\\\n    value: 44.3\\\\n    note: 44.3% from mvp_pilot_004; paper uses 40% from primary config (N=8, seed=42)\\\\n  - exp_id: exp_008_re_n16_v2\\\\n    metric: f1_zero_pct\\\\n    value: 44.3\\\\n    note: 44.3% at N=16; zero-F1 fraction varies with N and seed\\\\n- id: c007_em_leads_conll\\\\n  text: EM leads CoNLL with ρ=0.451 and AUROC=0.816\\\\n  sections:\\\\n  - experiments\\\\n  tier: 1\\\\n  evidence:\\\\n  - exp_id: exp_002\\\\n    metric: em_rho_full\\\\n    value: 0.4507\\\\n  - exp_id: exp_002\\\\n    metric: em_auroc_full\\\\n    value: 0.8156\\\\n  - exp_id: exp_015_v2\\\\n    metric: auroc_best.EM.conll_ner\\\\n    value: 0.8156\\\\n- id: c008_cross_model_sj_stability\\\\n  text: 'SJ cross-model gap: ρ=0.436 (Qwen) vs 0.431 (LLaMA), Δ=0.005'\\\\n  sections:\\\\n  - experiments\\\\n  tier: 1\\\\n  evidence:\\\\n  - exp_id: exp_002\\\\n    metric: sj_rho_full\\\\n    value: 0.4357\\\\n  - exp_id: exp_017_llama_conll_infer\\\\n    metric: full.SJ_rho\\\\n    value: 0.4314\\\\n- id: c009_logprob_paradox\\\\n  text: Logprob achieves highest AUROC (0.761) yet lowest ρ (0.307) on CoNLL LLaMA\\\\n  sections:\\\\n  - experiments\\\\n  - discussion\\\\n  tier: 1\\\\n  evidence:\\\\n  - exp_id: exp_017_llama_conll_infer\\\\n    metric: full.logprob_AUROC\\\\n    value: 0.761\\\\n  - exp_id: exp_017_llama_conll_infer\\\\n    metric: full.logprob_rho\\\\n    value: 0.3072\\\\n- id: c010_conll_oracle_headroom\\\\n  text: 'CoNLL oracle headroom: +4.2pp (Qwen), +1.8pp (LLaMA)'\\\\n  sections:\\\\n  - experiments\\\\n  tier: 1\\\\n  evidence:\\\\n  - exp_id: exp_002\\\\n    metric: oracle_headroom\\\\n    value: 0.042\\\\n  - exp_id: exp_017_llama_conll_infer\\\\n    metric: oracle_headroom\\\\n    value: 0.0177\\\\n- id: c011_ner_no_reliable_selection\\\\n  text: No signal reliably surpasses greedy on NER (logprob +0.6pp, p=0.39, 3-seed\\\\n    bootstrap)\\\\n  sections:\\\\n  - abstract\\\\n  - introduction\\\\n  - experiments\\\\n  - conclusion\\\\n  - discussion\\\\n  - related_work\\\\n  tier: 1\\\\n  evidence:\\\\n  - exp_id: exp_016_rerun_1024_bootstrap\\\\n    metric: selection_f1_ner\\\\n    value:\\\\n      greedy: 0.644\\\\n      logprob: 0.65\\\\n      sj: 0.645\\\\n      voting: 0.634\\\\n      random: 0.608\\\\n      oracle: 0.776\\\\n  - exp_id: exp_016_rerun_1024_bootstrap\\\\n    metric: bootstrap_selection_test\\\\n    value:\\\\n      logprob_vs_greedy_p: 0.39\\\\n      ci_95:\\\\n      - -0.03\\\\n      - 0.042\\\\n      cohens_d: 0.038\\\\n      sign_test: 61W/70L\\\\n  note: 3-seed bootstrap confirms +0.6pp is NOT statistically significant. Unified\\\\n    with c012 — no signal reliably helps on either task.\\\\n- id: c012_re_no_signal_beats_greedy\\\\n  text: No signal surpasses greedy on RE; logprob drops to −0.9pp\\\\n  sections:\\\\n  - abstract\\\\n  - introduction\\\\n  - experiments\\\\n  - conclusion\\\\n  - discussion\\\\n  tier: 1\\\\n  evidence:\\\\n  - exp_id: exp_016_rerun_1024_bootstrap\\\\n    metric: selection_f1_re\\\\n    value:\\\\n      greedy: 0.404\\\\n      logprob: 0.395\\\\n      sj: 0.386\\\\n      voting: 0.359\\\\n      random: 0.354\\\\n      oracle: 0.585\\\\n  note: CLAIM REVERSED from exp_016 (max_tokens=512). Old claim was \\\\\\\"only logprob\\\\n    helps on RE (+2.3pp)\\\\\\\". Corrected via exp_016_rerun_1024_bootstrap.\\\\n- id: c013_oracle_headroom_ner\\\\n  text: Oracle upper bound 0.776, 13.2pp above greedy 0.644 on NER\\\\n  sections:\\\\n  - experiments\\\\n  - discussion\\\\n  tier: 1\\\\n  evidence:\\\\n  - exp_id: exp_016_rerun_1024_bootstrap\\\\n    metric: selection_f1_ner.oracle\\\\n    value: 0.776\\\\n  - exp_id: exp_016_rerun_1024_bootstrap\\\\n    metric: selection_f1_ner.greedy\\\\n    value: 0.644\\\\n- id: c014_re_oracle_headroom\\\\n  text: 'RE oracle gap: 18.1pp (0.585 vs 0.404)'\\\\n  sections:\\\\n  - experiments\\\\n  - discussion\\\\n  tier: 1\\\\n  evidence:\\\\n  - exp_id: exp_016_rerun_1024_bootstrap\\\\n    metric: selection_f1_re.oracle\\\\n    value: 0.585\\\\n  - exp_id: exp_016_rerun_1024_bootstrap\\\\n    metric: selection_f1_re.greedy\\\\n    value: 0.404\\\\n- id: c015_ensemble_auroc\\\\n  text: SJ+Voting ensemble AUROC=0.666, below best individual signal EM (0.749)\\\\n  sections:\\\\n  - discussion\\\\n  tier: 1\\\\n  evidence:\\\\n  - exp_id: exp_016_rerun_1024_bootstrap\\\\n    metric: ensemble_ner_auroc\\\\n    value: 0.666\\\\n  note: Ensemble does NOT improve over best individual. Changed from positive to negative\\\\n    finding.\\\\n- id: c016_ece_calibration\\\\n  text: NER reasonably well-calibrated (calibration ECE 0.069-0.096), RE shows greater\\\\n    miscalibration (ECE 0.109-0.339)\\\\n  sections:\\\\n  - experiments\\\\n  tier: 1\\\\n  evidence:\\\\n  - exp_id: exp_016_rerun_1024_bootstrap\\\\n    metric: calibration_ece\\\\n    value:\\\\n      ner_range: 0.069-0.096\\\\n      re_range: 0.109-0.339\\\\n  note: Previous c016 used binary ECE (0.27-0.77) which was incorrect metric. Calibration\\\\n    ECE (signal confidence → mean F1 deviation) shows NER is well-calibrated, RE has\\\\n    moderate miscalibration. Consistent with fig_reliability_1024.\\\\n- id: c017_fisher_z_ner_vs_re\\\\n  text: 'Fisher''s z-test ρ_SJ NER vs RE: z=2.31, p=0.021'\\\\n  sections:\\\\n  - experiments\\\\n  tier: 1\\\\n  evidence:\\\\n  - exp_id: exp_004_re_diagnostic\\\\n    metric: fisher_z_ner_vs_re.sj_z\\\\n    value: 2.31\\\\n  - exp_id: exp_004_re_diagnostic\\\\n    metric: fisher_z_ner_vs_re.sj_p\\\\n    value: 0.0209\\\\n- id: c018_per_relation_diagnostic\\\\n  text: Feature-Of ρ≈0.004, Hyponym-Of ρ=0.646\\\\n  sections:\\\\n  - experiments\\\\n  tier: 1\\\\n  evidence:\\\\n  - exp_id: exp_004_re_diagnostic\\\\n    metric: per_relation_type.FEATURE-OF.rho_sj\\\\n    value: 0.004\\\\n  - exp_id: exp_004_re_diagnostic\\\\n    metric: per_relation_type.HYPONYM-OF.rho_fk\\\\n    value: 0.646\\\\n- id: c019_entity_span_errors\\\\n  text: Entity span errors account for 55.5% of RE false negatives\\\\n  sections:\\\\n  - experiments\\\\n  tier: 1\\\\n  evidence:\\\\n  - exp_id: exp_004_re_diagnostic\\\\n    metric: error_propagation\\\\n    value: head_error 17.7% + tail_error (derived) + head_tail_error 15.9% + full_error\\\\n      21.7% → entity span errors ~55.5%\\\\n  note: Computed from error_propagation breakdown in exp_004\\\\n- id: c020_capability_stratification_ner\\\\n  text: SJ ρ=0.547 on SciERC instances with 6+ entities, vs 0.415 for 1-2 entities\\\\n  sections:\\\\n  - experiments\\\\n  tier: 1\\\\n  evidence:\\\\n  - exp_id: exp_009_capability_stratification\\\\n    metric: scierc_ner.by_ent_count.6plus_sj_rho\\\\n    value: 0.547\\\\n  - exp_id: exp_009_capability_stratification\\\\n    metric: scierc_ner.by_ent_count.1_2_sj_rho\\\\n    value: 0.415\\\\n- id: c021_wnut_boundary\\\\n  text: 'WNUT-17: SJ ρ=0.089 (p=0.020), 54% zero F1'\\\\n  sections:\\\\n  - experiments\\\\n  - conclusion\\\\n  tier: 1\\\\n  evidence:\\\\n  - exp_id: exp_003_wnut17_eval\\\\n    metric: rho_sj\\\\n    value: 0.089\\\\n  - exp_id: exp_003_wnut17_eval\\\\n    metric: sample_f1_pct_zero\\\\n    value: 53.7\\\\n  note: 'Corrected 2026-05-16: paper uses ρ=0.089 from exp003_wnut17_eval (gold-filtered\\\\n    n=689, p=0.020). Old value 0.062 was untraceable — only in deprecated draft.'\\\\n- id: c022_wnut_logprob_negative\\\\n  text: WNUT logprob shows strong negative correlation\\\\n  sections:\\\\n  - experiments\\\\n  tier: 1\\\\n  evidence:\\\\n  - exp_id: exp_003_ner_wnut17\\\\n    metric: ner.rho_logprob_full\\\\n    value: -0.414\\\\n  - exp_id: exp_003_wnut17_eval\\\\n    metric: rho_logprob_full\\\\n    value: -0.409\\\\n- id: c023_re_sent_length_sj\\\\n  text: 'RE SJ ρ increases with sentence length: Q1 0.110 → Q4 0.473 (Fisher p=0.004)'\\\\n  sections:\\\\n  - experiments\\\\n  tier: 2\\\\n  evidence:\\\\n  - exp_id: exp_009_v2_re_rerun\\\\n    metric: by_sent_len_quartiles\\\\n    value:\\\\n      Q1_sj_rho: 0.11\\\\n      Q4_sj_rho: 0.473\\\\n      fisher_z_p: 0.004\\\\n  note: 'Corrected 2026-05-16: source is exp_009_v2_re_rerun (gold-filtered n=397).\\\\n    Old registry exp_009 values (Q1=0.447, Q4=0.540) used unfiltered n=551.'\\\\n- id: c024_high_complexity_re_subset\\\\n  text: 'High-complexity RE subset (n=81): Voting ρ=0.630, logprob ρ=0.554, SJ ρ=0.502'\\\\n  sections:\\\\n  - experiments\\\\n  tier: 2\\\\n  evidence:\\\\n  - exp_id: exp_009_capability_stratification\\\\n    metric: scierc_re.by_rel_count\\\\n    value:\\\\n      6plus_sj_rho: 0.527\\\\n  note: Registry has 6plus_sj_rho=0.527; paper may use exp_009_v2 data. Voting and\\\\n    logprob values not in registry summary.\\\\n- id: c025_temperature_sj_stable\\\\n  text: SJ NER ρ shifts from 0.388 (T=0.7) to 0.360 (T=1.0), Δ=0.028\\\\n  sections:\\\\n  - experiments\\\\n  tier: 1\\\\n  evidence:\\\\n  - exp_id: exp_005\\\\n    metric: sj_rho_t07_ner\\\\n    value: 0.388\\\\n  - exp_id: exp_012_rerun_1024\\\\n    metric: ner.sj_rho_full\\\\n    value: 0.36\\\\n  note: T=0.7 data from exp_005; T=1.0 from exp_015\\\\n- id: c026_n_scaling_sj\\\\n  text: SJ N=8→N=16 improves ρ from 0.360 to 0.412±0.025 (3-seed, +0.052) on Qwen\\\\n    SciERC NER\\\\n  sections:\\\\n  - experiments\\\\n  tier: 1\\\\n  evidence:\\\\n  - exp_id: exp_012_rerun_1024\\\\n    metric: ner.sj_rho_full\\\\n    value: 0.36\\\\n  - exp_id: exp_001_seed42_v2\\\\n    metric: sj_rho_full\\\\n    value: 0.428\\\\n  - exp_id: exp_001_seed123_v2\\\\n    metric: sj_rho_full\\\\n    value: 0.424\\\\n  - exp_id: exp_001_seed456_v2_ner\\\\n    metric: full.SJ.rho\\\\n    value: 0.384\\\\n  note: '3-seed mean: (0.428+0.424+0.384)/3 ≈ 0.412, σ=0.025'\\\\n- id: c027_llama_conll_3seed\\\\n  text: 'LLaMA CoNLL N=16 3-seed: SJ ρ=0.463±0.007, logprob ρ=0.310±0.005'\\\\n  sections:\\\\n  - experiments\\\\n  tier: 1\\\\n  evidence:\\\\n  - exp_id: exp_017_llama_conll_n16\\\\n    metric: full.SJ_rho\\\\n    value: 0.4642\\\\n  - exp_id: exp_017_llama_conll_n16_s123\\\\n    metric: full.SJ_rho\\\\n    value: 0.4698\\\\n  - exp_id: exp_017_llama_conll_n16_s456\\\\n    metric: full.SJ_rho\\\\n    value: 0.4552\\\\n  - exp_id: exp_017_llama_conll_n16\\\\n    metric: full.logprob_rho\\\\n    value: 0.3058\\\\n  - exp_id: exp_017_llama_conll_n16_s123\\\\n    metric: full.logprob_rho\\\\n    value: 0.3161\\\\n  - exp_id: exp_017_llama_conll_n16_s456\\\\n    metric: full.logprob_rho\\\\n    value: 0.3078\\\\n- id: c028_loo_sj_circularity\\\\n  text: LOO-SJ Δρ=-0.014, max per-instance Δρ=3.1×10⁻⁴—circularity negligible\\\\n  sections:\\\\n  - experiments\\\\n  tier: 1\\\\n  evidence:\\\\n  - exp_id: exp_015_v2\\\\n    metric: loo_sj.max_delta_rho\\\\n    value: 0.000305\\\\n  - exp_id: exp_015_v2\\\\n    metric: loo_sj.all_no_circularity\\\\n    value: true\\\\n- id: c029_llama_scierc_cross_model\\\\n  text: 'LLaMA replicates structural-over-surface on SciERC: NER SJ ρ=0.363 > FK ρ=0.327;\\\\n    conditional RE SJ ρ=0.405 > FK ρ=0.259'\\\\n  sections:\\\\n  - experiments\\\\n  tier: 1\\\\n  evidence:\\\\n  - exp_id: exp_007_llama_inference\\\\n    metric: ner.rho_sj\\\\n    value: 0.363\\\\n  - exp_id: exp_007_llama_inference\\\\n    metric: ner.rho_fk\\\\n    value: 0.327\\\\n  - exp_id: exp_007_llama_inference\\\\n    metric: re.sj_rho_cond\\\\n    value: 0.405\\\\n  - exp_id: exp_007_llama_inference\\\\n    metric: re.fk_rho_cond\\\\n    value: 0.259\\\\n- id: c030_em_conditional_dominance\\\\n  text: 'EM ranks #1 on conditional set across all 4 configurations'\\\\n  sections:\\\\n  - experiments\\\\n  tier: 1\\\\n  evidence:\\\\n  - exp_id: exp_015_metrics_expansion\\\\n    metric: ner.em_rho_cond\\\\n    value: 0.3427\\\\n  - exp_id: exp_015_metrics_expansion\\\\n    metric: re.em_rho_cond\\\\n    value: 0.3607\\\\n  - exp_id: exp_002_conll_n16\\\\n    metric: conditional.EM_rho\\\\n    value: 0.4658\\\\n  - exp_id: exp_017_llama_conll_n16_s123\\\\n    metric: conditional.EM_rho\\\\n    value: 0.4732\\\\n  note: 'Paper cites EM conditional: SciERC NER 0.408, RE 0.485, CoNLL Qwen N=16 0.466,\\\\n    CoNLL LLaMA 3-seed 0.462. Registry has slightly different values from different\\\\n    seed/N combinations.'\\\\n- id: c031_em_conditional_scierc\\\\n  text: 'EM conditional: NER ρ=0.408, RE ρ=0.485'\\\\n  sections:\\\\n  - experiments\\\\n  tier: 1\\\\n  evidence:\\\\n  - exp_id: exp_001_ner_n16_scierc\\\\n    metric: ner_cond_em_rho\\\\n    value: 0.414\\\\n  - exp_id: exp_001_ner_n16_scierc\\\\n    metric: re_cond_em_rho\\\\n    value: 0.475\\\\n  note: 'Paper rounds: 0.414→0.408, 0.475→0.485. May use different seed/N baseline.'\\\\n- id: c032_logprob_re_cond_collapse\\\\n  text: Logprob conditional RE collapses to ρ=0.011\\\\n  sections:\\\\n  - experiments\\\\n  tier: 1\\\\n  evidence:\\\\n  - exp_id: exp_012_rerun_1024\\\\n    metric: re_cond.logprob.rho\\\\n    value: 0.0112\\\\n  note: 'Corrected 2026-05-16: source is exp_012_rerun_1024 (greedy_f1>0 filter, n=238).\\\\n    Old exp_015 value 0.1457 used wrong filter (any sample F1>0, n=331). Old text\\\\n    0.002 was stale and untraceable.'\\\\n- id: c033_sj_n16_cond_re\\\\n  text: At N=16, SJ maintains ρ=0.308 on conditional RE while logprob drops to -0.026\\\\n  sections:\\\\n  - experiments\\\\n  - discussion\\\\n  tier: 1\\\\n  evidence:\\\\n  - exp_id: exp_008_re_n16_v2\\\\n    metric: sj_rho_cond\\\\n    value: 0.308\\\\n- id: c034_structural_over_logprob_n16\\\\n  text: Structural-over-logprob advantage holds across all 4 N=16 settings (Δ=+0.124\\\\n    to +0.175)\\\\n  sections:\\\\n  - experiments\\\\n  - discussion\\\\n  tier: 1\\\\n  evidence:\\\\n  - exp_id: exp_001_ner_n16_scierc\\\\n    metric: ner_voting_conf_rho\\\\n    value: 0.399\\\\n  - exp_id: exp_001_ner_n16_scierc\\\\n    metric: ner_logprob_rho\\\\n    value: 0.237\\\\n  - exp_id: exp_002_conll_n16\\\\n    metric: full.EM_rho\\\\n    value: 0.4627\\\\n  - exp_id: exp_002_conll_n16\\\\n    metric: full.logprob_rho\\\\n    value: 0.3146\\\\n  - exp_id: exp_007_llama_n16\\\\n    metric: full.voting_conf_rho\\\\n    value: 0.4515\\\\n  - exp_id: exp_007_llama_n16\\\\n    metric: full.logprob_rho\\\\n    value: 0.2041\\\\n  - exp_id: exp_017_llama_conll_n16\\\\n    metric: full.SJ_rho\\\\n    value: 0.4642\\\\n  - exp_id: exp_017_llama_conll_n16\\\\n    metric: full.logprob_rho\\\\n    value: 0.3058\\\\n- id: c035_n_scaling_diminishing\\\\n  text: 'SJ N-scaling gains are sublinear: +0.052 Qwen SciERC, +0.032 LLaMA CoNLL'\\\\n  sections:\\\\n  - discussion\\\\n  tier: 1\\\\n  evidence:\\\\n  - exp_id: exp_001_seed42_v2\\\\n    metric: sj_rho_full\\\\n    value: 0.428\\\\n  - exp_id: exp_015_metrics_expansion\\\\n    metric: ner.sj_rho_full\\\\n    value: 0.3565\\\\n  - exp_id: exp_017_llama_conll_n16\\\\n    metric: full.SJ_rho\\\\n    value: 0.4642\\\\n  - exp_id: exp_017_llama_conll_infer\\\\n    metric: full.SJ_rho\\\\n    value: 0.4314\\\\n  note: 'Qwen SciERC: 0.412 (3-seed mean) - 0.360 = +0.052. LLaMA CoNLL: 0.463 (3-seed)\\\\n    - 0.431 = +0.032'\\\\n- id: c036_sj_ece_calibration\\\\n  text: '[DEPRECATED] SJ achieves lowest calibration error (ECE=0.075-0.102 across\\\\n    settings)'\\\\n  sections: []\\\\n  tier: X\\\\n  evidence: []\\\\n  note: DEPRECATED — reversed by c016_ece_miscalibration. Old ECE values (0.075-0.102)\\\\n    were from exp_015 (max_tokens=512 truncation artifact). Corrected data shows all\\\\n    signals ECE 0.27-0.77.\\\\n- id: C001\\\\n  location:\\\\n    section: abstract\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: No signal significantly improves sample selection over greedy decoding despite\\\\n    13-18pp oracle headroom\\\\n  type: empirical\\\\n  evidence:\\\\n  - exp_012_rerun_1024\\\\n  decisions:\\\\n  - D070\\\\n  - D071\\\\n  deprecated: false\\\\n- id: C003\\\\n  location:\\\\n    section: abstract\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: LP scores compressed into effective ties for 60% of instances under constrained\\\\n    decoding\\\\n  type: empirical\\\\n  evidence:\\\\n  - exp_012_rerun_1024\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C006\\\\n  location:\\\\n    section: abstract\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: Where LP compression is absent, selection recovers +2.9pp (p=0.01)\\\\n  type: empirical\\\\n  evidence:\\\\n  - exp_012_rerun_1024\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C010\\\\n  location:\\\\n    section: abstract\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: Constrained-decoding score compression is the primary bottleneck\\\\n  type: empirical\\\\n  evidence:\\\\n  - exp_012_rerun_1024\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C011\\\\n  location:\\\\n    section: discussion\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: LP carries useful per-sample quality information; score compression is the\\\\n    primary bottleneck\\\\n  type: empirical\\\\n  evidence:\\\\n  - exp_012_rerun_1024\\\\n  decisions:\\\\n  - D071\\\\n  deprecated: false\\\\n- id: C013\\\\n  location:\\\\n    section: discussion\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: MBR utility correlates with F1 across instances but not within\\\\n  type: empirical\\\\n  evidence:\\\\n  - exp_012_rerun_1024\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C016\\\\n  location:\\\\n    section: discussion\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: Free-form ablation would test if bottleneck is decoding-regime-specific\\\\n  type: planned\\\\n  evidence: []\\\\n  decisions:\\\\n  - D071\\\\n  deprecated: false\\\\n- id: C017\\\\n  location:\\\\n    section: conclusion\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: Consistency signals effective QE (rho up to 0.38, AUROC up to 0.75) but fail\\\\n    at selection\\\\n  type: empirical\\\\n  evidence:\\\\n  - exp_012_rerun_1024\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C019\\\\n  location:\\\\n    section: conclusion\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: LP fails due to constrained-decoding score compression\\\\n  type: empirical\\\\n  evidence:\\\\n  - exp_012_rerun_1024\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C022\\\\n  location:\\\\n    section: conclusion\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: RE findings preliminary, single benchmark\\\\n  type: scope_limitation\\\\n  evidence:\\\\n  - exp_012_rerun_1024\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C023\\\\n  location:\\\\n    section: sections/discussion\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: Entity-token LP exhibits 4x higher within-instance variance than full-sequence\\\\n    LP on SciERC, but selection performs worse (-2.0pp)\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: exp_entity_token_lp\\\\n    metric: scierc_entity_lp_variance_ratio\\\\n    value: 4.0x\\\\n  - exp_id: exp_entity_token_lp\\\\n    metric: scierc_entity_lp_selection_delta\\\\n    value: -1.68\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C024\\\\n  location:\\\\n    section: sections/discussion\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: On CoNLL, entity-token LP variance collapses to near-zero (median 2e-10) with\\\\n    79% tied\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: exp_entity_token_lp\\\\n    metric: conll_entity_lp_variance_median\\\\n    value: 2e-10\\\\n  - exp_id: exp_entity_token_lp\\\\n    metric: conll_entity_lp_tied_fraction\\\\n    value: 0.794\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C025\\\\n  location:\\\\n    section: sections/discussion\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: Entity-token LP rules out format-token dilution as primary cause; points to\\\\n    intrinsic model overconfidence on entity tokens\\\\n  type: interpretive\\\\n  evidence:\\\\n  - exp_id: exp_entity_token_lp\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C026\\\\n  location:\\\\n    section: sections/limitations\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: Entity-token LP is the only tested remedy; LP×VC and calibration approaches\\\\n    are unexplored\\\\n  type: scope\\\\n  evidence:\\\\n  - exp_id: exp_entity_token_lp\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C027\\\\n  location:\\\\n    section: sections/introduction\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: 'C1 reframe: instance-level nature is setup, LP compression + MBR within-instance\\\\n    failure are the findings'\\\\n  type: structural\\\\n  evidence: []\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C028\\\\n  location:\\\\n    section: sections/introduction\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: 'SF4: 60% tied replaced with pooled within-instance ρ(LP,F1)=0.248 continuous\\\\n    characterization'\\\\n  type: structural\\\\n  evidence: []\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C029\\\\n  location:\\\\n    section: sections/introduction\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: 'C2 reframe: entity-token LP added as diagnostic ablation contribution'\\\\n  type: structural\\\\n  evidence:\\\\n  - exp_id: exp_entity_token_lp\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C030\\\\n  location:\\\\n    section: sections/abstract\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: 'SF3: RE removed from abstract; SF1: ρ=0.38 sourced to SciERC primary, up\\\\n    to 0.45 on ceiling control; MF2(a): benchmark roles explicit; M2: streamlined\\\\n    from 9 to 6 sentences'\\\\n  type: structural\\\\n  evidence: []\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C031\\\\n  location:\\\\n    section: sections/discussion\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: 21% of SciERC instances produce identical F1 across all N samples\\\\n  type: quantitative\\\\n  evidence: Q1 within-instance analysis\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C032\\\\n  location:\\\\n    section: sections/discussion\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: 58% of CoNLL instances produce identical F1 across all N samples\\\\n  type: quantitative\\\\n  evidence: Q1 within-instance analysis\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C033\\\\n  location:\\\\n    section: sections/discussion\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: 13% of SciERC instances yield constant utility scores\\\\n  type: quantitative\\\\n  evidence: Q1 within-instance analysis\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C034\\\\n  location:\\\\n    section: sections/discussion\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: 49% of CoNLL instances yield constant utility scores\\\\n  type: quantitative\\\\n  evidence: Q1 within-instance analysis\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C035\\\\n  location:\\\\n    section: sections/discussion\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: SJ median within-instance rho = 0.524 on SciERC\\\\n  type: quantitative\\\\n  evidence: Q1 within-instance analysis\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C036\\\\n  location:\\\\n    section: sections/discussion\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: SJ median within-instance rho = 0.994 on CoNLL\\\\n  type: quantitative\\\\n  evidence: Q1 within-instance analysis\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C037\\\\n  location:\\\\n    section: sections/discussion\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: MBR closes 23% of oracle gap on non-degenerate SciERC instances\\\\n  type: quantitative\\\\n  evidence: Q1 within-instance analysis\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C038\\\\n  location:\\\\n    section: sections/discussion\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: MBR closes 41% of oracle gap on non-degenerate CoNLL instances\\\\n  type: quantitative\\\\n  evidence: Q1 within-instance analysis\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C039\\\\n  location:\\\\n    section: sections/discussion\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: Greedy T=0 achieves F1=0.663 on SciERC, surpassing all N=8 selection strategies\\\\n  type: quantitative\\\\n  evidence: SF4 greedy data\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C040\\\\n  location:\\\\n    section: sections/discussion\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: SciERC 3-epoch rho=0.32 vs 5-epoch rho=0.28; LP delta -1.18 vs +0.62 pp\\\\n  type: quantitative\\\\n  evidence: tab:epoch_scierc\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C041\\\\n  location:\\\\n    section: sections/discussion\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: Entity-level majority voting yields +0.76pp on SciERC (5.8% gap recovery)\\\\n  type: quantitative\\\\n  evidence: []\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C042\\\\n  location:\\\\n    section: sections/discussion\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: Entity-level majority voting yields -0.64pp on CoNLL\\\\n  type: quantitative\\\\n  evidence: []\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C043\\\\n  location:\\\\n    section: sections/discussion\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: Entity-level majority voting yields -3.21pp on Few-NERD\\\\n  type: quantitative\\\\n  evidence: []\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C044\\\\n  location:\\\\n    section: sections/discussion\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: On degenerate subsets, merge is uniformly negative across all three datasets\\\\n  type: quantitative\\\\n  evidence: []\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C045\\\\n  location:\\\\n    section: sections/appendix\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: Exact permutation p=0.005 for per-type degeneracy-headroom correlation\\\\n  type: quantitative\\\\n  evidence: []\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C046\\\\n  location:\\\\n    section: sections/appendix\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: Under conservative df=4 adjustment, p=0.033\\\\n  type: quantitative\\\\n  evidence: []\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C047\\\\n  location:\\\\n    section: sections/appendix\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: 3-epoch SciERC mean within-instance rho=0.273\\\\n  type: quantitative\\\\n  evidence: []\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C048\\\\n  location:\\\\n    section: sections/appendix\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: 5-epoch SciERC mean within-instance rho=0.179\\\\n  type: quantitative\\\\n  evidence: []\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C049\\\\n  location:\\\\n    section: sections/appendix\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: 76.4% of instances show positive LP-quality correlation at 3 epochs\\\\n  type: quantitative\\\\n  evidence: []\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C050\\\\n  location:\\\\n    section: sections/appendix\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: 64.1% of instances show positive LP-quality correlation at 5 epochs\\\\n  type: quantitative\\\\n  evidence: []\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C051\\\\n  location:\\\\n    section: sections/appendix\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: Epoch-to-epoch alignment variation is 0.057 median rho, small vs cross-dataset\\\\n    gap\\\\n  type: quantitative\\\\n  evidence: []\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C052\\\\n  location:\\\\n    section: sections/appendix\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: 'Optimal DALS tau spans 2 orders of magnitude: FN 0.001, SciERC 0.05, CoNLL\\\\n    0.10'\\\\n  type: quantitative\\\\n  evidence: []\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C053\\\\n  location:\\\\n    section: sections/appendix\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: LOO regret ranges from 0.51 to 1.21pp\\\\n  type: quantitative\\\\n  evidence: []\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C054\\\\n  location:\\\\n    section: sections/appendix\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: Even with oracle tau, CoNLL remains at -0.31pp\\\\n  type: quantitative\\\\n  evidence: []\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C055\\\\n  location:\\\\n    section: sections/appendix\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: 'SciERC entity merge best k=3: +1.57pp, 11.9% recovery'\\\\n  type: quantitative\\\\n  evidence: []\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C056\\\\n  location:\\\\n    section: sections/appendix\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: 'CoNLL entity merge best k=3: -0.38pp, -9.0% recovery'\\\\n  type: quantitative\\\\n  evidence: []\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C057\\\\n  location:\\\\n    section: sections/appendix\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: 'FewNERD entity merge best k=2: -0.43pp, -3.6% recovery'\\\\n  type: quantitative\\\\n  evidence: []\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C058\\\\n  location:\\\\n    section: sections/experiments\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: 'Conditional decomp SciERC favorable: +2.47pp CI [+0.30, +4.70]'\\\\n  type: quantitative\\\\n  evidence: []\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C059\\\\n  location:\\\\n    section: sections/experiments\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: 'Conditional decomp FewNERD favorable: +0.63pp CI [-0.02, +1.30], marginal'\\\\n  type: quantitative\\\\n  evidence: []\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C060\\\\n  location:\\\\n    section: sections/experiments\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: 'Conditional decomp CoNLL favorable: -1.78pp CI [-2.83, -0.76], negative'\\\\n  type: quantitative\\\\n  evidence: []\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C061\\\\n  location:\\\\n    section: sections/appendix\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: Entity-token LP has 4x higher within-instance variance (0.000644 vs 0.000161)\\\\n  type: quantitative\\\\n  evidence: []\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C062\\\\n  location:\\\\n    section: sections/appendix\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: Entity-token LP rho=0.440 vs full-sequence 0.297\\\\n  type: quantitative\\\\n  evidence: []\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C063\\\\n  location:\\\\n    section: sections/appendix\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: Entity-token LP selection -0.73pp vs full-sequence +0.35pp\\\\n  type: quantitative\\\\n  evidence: []\\\\n  decisions: []\\\\n  deprecated: false\\\\ntables:\\\\n- id: tab:notation\\\\n  section: method\\\\n  caption: Notation used throughout the paper\\\\n  evidence: []\\\\n  note: Notation table—no experimental data.\\\\n- id: tab:quality_estimation\\\\n  section: experiments\\\\n  caption: Quality estimation across tasks and models (Spearman ρ and AUROC)\\\\n  evidence:\\\\n  - exp_id: exp_012_rerun_1024\\\\n    role: SciERC NER ρ values (N=8, Qwen) — corrected from exp_015 (truncation artifact)\\\\n  - exp_id: exp_015_metrics_expansion\\\\n    role: SciERC RE ρ values (N=8, Qwen) — RE values unaffected by truncation fix\\\\n  - exp_id: exp_015_v2\\\\n    role: AUROC values across settings\\\\n  - exp_id: exp_002\\\\n    role: CoNLL Qwen N=8 ρ and AUROC\\\\n  - exp_id: exp_017_llama_conll_infer\\\\n    role: CoNLL LLaMA N=8 ρ and AUROC\\\\n  - exp_id: exp_017_llama_conll_n16\\\\n    role: LLaMA CoNLL N=16 3-seed (seed=42)\\\\n  - exp_id: exp_017_llama_conll_n16_s123\\\\n    role: LLaMA CoNLL N=16 3-seed (seed=123)\\\\n  - exp_id: exp_017_llama_conll_n16_s456\\\\n    role: LLaMA CoNLL N=16 3-seed (seed=456)\\\\n- id: tab:selection\\\\n  section: experiments\\\\n  caption: Best-of-N selection F1 on SciERC (N=8, T=1.0)\\\\n  evidence:\\\\n  - exp_id: exp_016_signal_ensemble\\\\n    role: All selection F1 values (NER and RE)\\\\n- id: tab:robustness\\\\n  section: experiments\\\\n  caption: Signal robustness across configurations (Spearman ρ)\\\\n  evidence:\\\\n  - exp_id: exp_005\\\\n    role: Temperature block (T=0.7 vs T=1.0, Qwen SciERC)\\\\n  - exp_id: exp_015_metrics_expansion\\\\n    role: N=8 baseline values\\\\n  - exp_id: exp_001_seed42_v2\\\\n    role: N=16 SJ ρ seed=42\\\\n  - exp_id: exp_001_seed123_v2\\\\n    role: N=16 SJ ρ seed=123\\\\n  - exp_id: exp_001_seed456_v2_ner\\\\n    role: N=16 SJ ρ seed=456\\\\n  - exp_id: exp_017_llama_conll_n16\\\\n    role: 'Cross-model block: LLaMA CoNLL N=16 seed=42'\\\\n  - exp_id: exp_017_llama_conll_n16_s123\\\\n    role: 'Cross-model block: LLaMA CoNLL N=16 seed=123'\\\\n  - exp_id: exp_017_llama_conll_n16_s456\\\\n    role: 'Cross-model block: LLaMA CoNLL N=16 seed=456'\\\\nfigures:\\\\n- id: fig:overview\\\\n  section: introduction\\\\n  caption: The correlation-selection gap conceptual diagram\\\\n  evidence:\\\\n  - exp_id: exp_015_metrics_expansion\\\\n    role: Quality estimation data (ρ, AUROC for left panel)\\\\n  - exp_id: exp_016_signal_ensemble\\\\n    role: Selection F1 data (right panel)\\\\n- id: fig:signal_heatmap\\\\n  section: experiments\\\\n  caption: Quality estimation heatmap (Spearman ρ) across five signals and four configurations\\\\n  evidence:\\\\n  - exp_id: exp_015_metrics_expansion\\\\n    role: Full set ρ values for SciERC NER/RE (Qwen, N=8)\\\\n  - exp_id: exp_002\\\\n    role: CoNLL Qwen full set ρ values\\\\n  - exp_id: exp_001_ner_n16_scierc\\\\n    role: Conditional set ρ values\\\\n- id: fig:selection_gap\\\\n  section: experiments\\\\n  caption: The correlation-selection gap on SciERC (N=8)\\\\n  evidence:\\\\n  - exp_id: exp_016_signal_ensemble\\\\n    role: Best-of-N selection F1 bars and quality estimation ρ line\\\\n- id: fig:temperature_robustness\\\\n  section: experiments\\\\n  caption: Temperature robustness on SciERC (N=8)\\\\n  evidence:\\\\n  - exp_id: exp_005\\\\n    role: SJ, FK ρ values at T=0.7 and T=1.0\\\\n- id: fig:reliability\\\\n  section: experiments\\\\n  caption: Reliability diagrams on SciERC (N=8, T=1.0)\\\\n  evidence:\\\\n  - exp_id: exp_015_metrics_expansion\\\\n    role: Calibration/ECE data for all signals\\\\n  - exp_id: exp_002\\\\n    role: ECE values across signals\\\\n_completeness:\\\\n  coverage: 59/92\\\\n  claims: 87\\\\n  tables: 4\\\\n  figures: 5\\\\n  tier_counts:\\\\n    tier1: 0\\\\n    tier2: 59\\\\n    tier3: 33\\\\n    tierX: 0\\\\n  last_checked: '2026-05-18T15:39:48.035668+00:00'\\\\n\\\", \\\"total_chars\\\": 32730, \\\"truncated\\\": false}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/paper_provenance.yaml\", \"content\": \"paper:\\n  title: 'Strong Predictors, Weak Selectors: A Systematic Comparison of Confidence\\n    Signals for Test-Time Scaling in Information Extraction'\\n  version: 169\\n  generated_at: '2026-05-18T15:39:48.035618+00:00'\\n  source: manual provenance build by Paper Agent\\nclaims:\\n- id: c001_voting_rho_scierc_ner\\n  text: Voting Confidence achieves ρ=0.379 on SciERC NER (corrected from 0.502 truncation\\n    artifact)\\n  sections:\\n  - abstract\\n  - introduction\\n  - experiments\\n  - conclusion\\n  - discussion\\n  - related_work\\n  tier: 1\\n  evidence:\\n  - exp_id: exp_012_rerun_1024\\n    metric: ner.voting_rho_full\\n    value: 0.379\\n  note: Old value 0.502 from exp_015 was inflated by max_tokens=512 truncation. Corrected\\n    via exp_012_rerun_1024 (max_tokens=1024).\\n- id: c002_auroc_dissociation_scierc\\n  text: ρ-AUROC dissociation on SciERC — EM leads AUROC (NER 0.749, RE 0.706) while\\n    Voting leads ρ (NER 0.379, RE 0.422)\\n  sections:\\n  - abstract\\n  - introduction\\n  - experiments\\n  - conclusion\\n  - discussion\\n  tier: 1\\n  evidence:\\n  - exp_id: exp_012_rerun_1024\\n    metric: ner.em_auroc\\n    value: 0.749\\n  - exp_id: exp_012_rerun_1024\\n    metric: re.em_auroc\\n    value: 0.706\\n  - exp_id: exp_012_rerun_1024\\n    metric: ner.voting_auroc\\n    value: 0.684\\n  note: Old Table 1 had Voting NER AUROC=.741 (from exp_015 truncated). Corrected\\n    to .684 via exp_012_rerun_1024. EM now leads AUROC on both NER and RE. Headline\\n    claim changed from \\\"entity voting achieves ρ=0.38 and AUROC=0.74\\\" to split ρ (Voting\\n    0.38) / AUROC (EM 0.75) claim.\\n- id: c003_sj_rho_scierc_ner\\n  text: SJ achieves ρ=0.360 on SciERC NER (corrected from 0.357)\\n  sections:\\n  - experiments\\n  tier: 1\\n  evidence:\\n  - exp_id: exp_012_rerun_1024\\n    metric: ner.sj_rho_full\\n    value: 0.36\\n  - exp_id: exp_004_re_diagnostic\\n    metric: bootstrap_ci_95.ner_sj\\n    value:\\n    - 0.2946\\n    - 0.4586\\n- id: c004_voting_leads_re\\n  text: Voting leads RE full set (ρ=0.350, corrected from 0.422)\\n  sections:\\n  - experiments\\n  tier: 1\\n  evidence:\\n  - exp_id: exp_012_rerun_1024\\n    metric: re.voting_rho_full\\n    value: 0.35\\n  note: Corrected from exp_015_metrics_expansion (0.4217) via exp_012_rerun_1024.\\n- id: c005_fk_beats_sj_re\\n  text: FK (ρ=0.275) exceeds SJ (ρ=0.250) on RE—a reversal from NER\\n  sections:\\n  - experiments\\n  tier: 1\\n  evidence:\\n  - exp_id: exp_012_rerun_1024\\n    metric: re.fk_rho_full\\n    value: 0.275\\n  - exp_id: exp_012_rerun_1024\\n    metric: re.sj_rho_full\\n    value: 0.25\\n  note: Corrected from exp_015 (FK 0.253, SJ 0.211) via exp_012_rerun_1024.\\n- id: c006_re_40pct_zero_f1\\n  text: 40% of RE instances receive zero F1 (N=8, seed=42; 159/397)\\n  sections:\\n  - experiments\\n  - discussion\\n  tier: 1\\n  evidence:\\n  - exp_id: mvp_pilot_004\\n    metric: re_sample_f1_pct_zero\\n    value: 44.3\\n    note: 44.3% from mvp_pilot_004; paper uses 40% from primary config (N=8, seed=42)\\n  - exp_id: exp_008_re_n16_v2\\n    metric: f1_zero_pct\\n    value: 44.3\\n    note: 44.3% at N=16; zero-F1 fraction varies with N and seed\\n- id: c007_em_leads_conll\\n  text: EM leads CoNLL with ρ=0.451 and AUROC=0.816\\n  sections:\\n  - experiments\\n  tier: 1\\n  evidence:\\n  - exp_id: exp_002\\n    metric: em_rho_full\\n    value: 0.4507\\n  - exp_id: exp_002\\n    metric: em_auroc_full\\n    value: 0.8156\\n  - exp_id: exp_015_v2\\n    metric: auroc_best.EM.conll_ner\\n    value: 0.8156\\n- id: c008_cross_model_sj_stability\\n  text: 'SJ cross-model gap: ρ=0.436 (Qwen) vs 0.431 (LLaMA), Δ=0.005'\\n  sections:\\n  - experiments\\n  tier: 1\\n  evidence:\\n  - exp_id: exp_002\\n    metric: sj_rho_full\\n    value: 0.4357\\n  - exp_id: exp_017_llama_conll_infer\\n    metric: full.SJ_rho\\n    value: 0.4314\\n- id: c009_logprob_paradox\\n  text: Logprob achieves highest AUROC (0.761) yet lowest ρ (0.307) on CoNLL LLaMA\\n  sections:\\n  - experiments\\n  - discussion\\n  tier: 1\\n  evidence:\\n  - exp_id: exp_017_llama_conll_infer\\n    metric: full.logprob_AUROC\\n    value: 0.761\\n  - exp_id: exp_017_llama_conll_infer\\n    metric: full.logprob_rho\\n    value: 0.3072\\n- id: c010_conll_oracle_headroom\\n  text: 'CoNLL oracle headroom: +4.2pp (Qwen), +1.8pp (LLaMA)'\\n  sections:\\n  - experiments\\n  tier: 1\\n  evidence:\\n  - exp_id: exp_002\\n    metric: oracle_headroom\\n    value: 0.042\\n  - exp_id: exp_017_llama_conll_infer\\n    metric: oracle_headroom\\n    value: 0.0177\\n- id: c011_ner_no_reliable_selection\\n  text: No signal reliably surpasses greedy on NER (logprob +0.6pp, p=0.39, 3-seed\\n    bootstrap)\\n  sections:\\n  - abstract\\n  - introduction\\n  - experiments\\n  - conclusion\\n  - discussion\\n  - related_work\\n  tier: 1\\n  evidence:\\n  - exp_id: exp_016_rerun_1024_bootstrap\\n    metric: selection_f1_ner\\n    value:\\n      greedy: 0.644\\n      logprob: 0.65\\n      sj: 0.645\\n      voting: 0.634\\n      random: 0.608\\n      oracle: 0.776\\n  - exp_id: exp_016_rerun_1024_bootstrap\\n    metric: bootstrap_selection_test\\n    value:\\n      logprob_vs_greedy_p: 0.39\\n      ci_95:\\n      - -0.03\\n      - 0.042\\n      cohens_d: 0.038\\n      sign_test: 61W/70L\\n  note: 3-seed bootstrap confirms +0.6pp is NOT statistically significant. Unified\\n    with c012 — no signal reliably helps on either task.\\n- id: c012_re_no_signal_beats_greedy\\n  text: No signal surpasses greedy on RE; logprob drops to −0.9pp\\n  sections:\\n  - abstract\\n  - introduction\\n  - experiments\\n  - conclusion\\n  - discussion\\n  tier: 1\\n  evidence:\\n  - exp_id: exp_016_rerun_1024_bootstrap\\n    metric: selection_f1_re\\n    value:\\n      greedy: 0.404\\n      logprob: 0.395\\n      sj: 0.386\\n      voting: 0.359\\n      random: 0.354\\n      oracle: 0.585\\n  note: CLAIM REVERSED from exp_016 (max_tokens=512). Old claim was \\\"only logprob\\n    helps on RE (+2.3pp)\\\". Corrected via exp_016_rerun_1024_bootstrap.\\n- id: c013_oracle_headroom_ner\\n  text: Oracle upper bound 0.776, 13.2pp above greedy 0.644 on NER\\n  sections:\\n  - experiments\\n  - discussion\\n  tier: 1\\n  evidence:\\n  - exp_id: exp_016_rerun_1024_bootstrap\\n    metric: selection_f1_ner.oracle\\n    value: 0.776\\n  - exp_id: exp_016_rerun_1024_bootstrap\\n    metric: selection_f1_ner.greedy\\n    value: 0.644\\n- id: c014_re_oracle_headroom\\n  text: 'RE oracle gap: 18.1pp (0.585 vs 0.404)'\\n  sections:\\n  - experiments\\n  - discussion\\n  tier: 1\\n  evidence:\\n  - exp_id: exp_016_rerun_1024_bootstrap\\n    metric: selection_f1_re.oracle\\n    value: 0.585\\n  - exp_id: exp_016_rerun_1024_bootstrap\\n    metric: selection_f1_re.greedy\\n    value: 0.404\\n- id: c015_ensemble_auroc\\n  text: SJ+Voting ensemble AUROC=0.666, below best individual signal EM (0.749)\\n  sections:\\n  - discussion\\n  tier: 1\\n  evidence:\\n  - exp_id: exp_016_rerun_1024_bootstrap\\n    metric: ensemble_ner_auroc\\n    value: 0.666\\n  note: Ensemble does NOT improve over best individual. Changed from positive to negative\\n    finding.\\n- id: c016_ece_calibration\\n  text: NER reasonably well-calibrated (calibration ECE 0.069-0.096), RE shows greater\\n    miscalibration (ECE 0.109-0.339)\\n  sections:\\n  - experiments\\n  tier: 1\\n  evidence:\\n  - exp_id: exp_016_rerun_1024_bootstrap\\n    metric: calibration_ece\\n    value:\\n      ner_range: 0.069-0.096\\n      re_range: 0.109-0.339\\n  note: Previous c016 used binary ECE (0.27-0.77) which was incorrect metric. Calibration\\n    ECE (signal confidence → mean F1 deviation) shows NER is well-calibrated, RE has\\n    moderate miscalibration. Consistent with fig_reliability_1024.\\n- id: c017_fisher_z_ner_vs_re\\n  text: 'Fisher''s z-test ρ_SJ NER vs RE: z=2.31, p=0.021'\\n  sections:\\n  - experiments\\n  tier: 1\\n  evidence:\\n  - exp_id: exp_004_re_diagnostic\\n    metric: fisher_z_ner_vs_re.sj_z\\n    value: 2.31\\n  - exp_id: exp_004_re_diagnostic\\n    metric: fisher_z_ner_vs_re.sj_p\\n    value: 0.0209\\n- id: c018_per_relation_diagnostic\\n  text: Feature-Of ρ≈0.004, Hyponym-Of ρ=0.646\\n  sections:\\n  - experiments\\n  tier: 1\\n  evidence:\\n  - exp_id: exp_004_re_diagnostic\\n    metric: per_relation_type.FEATURE-OF.rho_sj\\n    value: 0.004\\n  - exp_id: exp_004_re_diagnostic\\n    metric: per_relation_type.HYPONYM-OF.rho_fk\\n    value: 0.646\\n- id: c019_entity_span_errors\\n  text: Entity span errors account for 55.5% of RE false negatives\\n  sections:\\n  - experiments\\n  tier: 1\\n  evidence:\\n  - exp_id: exp_004_re_diagnostic\\n    metric: error_propagation\\n    value: head_error 17.7% + tail_error (derived) + head_tail_error 15.9% + full_error\\n      21.7% → entity span errors ~55.5%\\n  note: Computed from error_propagation breakdown in exp_004\\n- id: c020_capability_stratification_ner\\n  text: SJ ρ=0.547 on SciERC instances with 6+ entities, vs 0.415 for 1-2 entities\\n  sections:\\n  - experiments\\n  tier: 1\\n  evidence:\\n  - exp_id: exp_009_capability_stratification\\n    metric: scierc_ner.by_ent_count.6plus_sj_rho\\n    value: 0.547\\n  - exp_id: exp_009_capability_stratification\\n    metric: scierc_ner.by_ent_count.1_2_sj_rho\\n    value: 0.415\\n- id: c021_wnut_boundary\\n  text: 'WNUT-17: SJ ρ=0.089 (p=0.020), 54% zero F1'\\n  sections:\\n  - experiments\\n  - conclusion\\n  tier: 1\\n  evidence:\\n  - exp_id: exp_003_wnut17_eval\\n    metric: rho_sj\\n    value: 0.089\\n  - exp_id: exp_003_wnut17_eval\\n    metric: sample_f1_pct_zero\\n    value: 53.7\\n  note: 'Corrected 2026-05-16: paper uses ρ=0.089 from exp003_wnut17_eval (gold-filtered\\n    n=689, p=0.020). Old value 0.062 was untraceable — only in deprecated draft.'\\n- id: c022_wnut_logprob_negative\\n  text: WNUT logprob shows strong negative correlation\\n  sections:\\n  - experiments\\n  tier: 1\\n  evidence:\\n  - exp_id: exp_003_ner_wnut17\\n    metric: ner.rho_logprob_full\\n    value: -0.414\\n  - exp_id: exp_003_wnut17_eval\\n    metric: rho_logprob_full\\n    value: -0.409\\n- id: c023_re_sent_length_sj\\n  text: 'RE SJ ρ increases with sentence length: Q1 0.110 → Q4 0.473 (Fisher p=0.004)'\\n  sections:\\n  - experiments\\n  tier: 2\\n  evidence:\\n  - exp_id: exp_009_v2_re_rerun\\n    metric: by_sent_len_quartiles\\n    value:\\n      Q1_sj_rho: 0.11\\n      Q4_sj_rho: 0.473\\n      fisher_z_p: 0.004\\n  note: 'Corrected 2026-05-16: source is exp_009_v2_re_rerun (gold-filtered n=397).\\n    Old registry exp_009 values (Q1=0.447, Q4=0.540) used unfiltered n=551.'\\n- id: c024_high_complexity_re_subset\\n  text: 'High-complexity RE subset (n=81): Voting ρ=0.630, logprob ρ=0.554, SJ ρ=0.502'\\n  sections:\\n  - experiments\\n  tier: 2\\n  evidence:\\n  - exp_id: exp_009_capability_stratification\\n    metric: scierc_re.by_rel_count\\n    value:\\n      6plus_sj_rho: 0.527\\n  note: Registry has 6plus_sj_rho=0.527; paper may use exp_009_v2 data. Voting and\\n    logprob values not in registry summary.\\n- id: c025_temperature_sj_stable\\n  text: SJ NER ρ shifts from 0.388 (T=0.7) to 0.360 (T=1.0), Δ=0.028\\n  sections:\\n  - experiments\\n  tier: 1\\n  evidence:\\n  - exp_id: exp_005\\n    metric: sj_rho_t07_ner\\n    value: 0.388\\n  - exp_id: exp_012_rerun_1024\\n    metric: ner.sj_rho_full\\n    value: 0.36\\n  note: T=0.7 data from exp_005; T=1.0 from exp_015\\n- id: c026_n_scaling_sj\\n  text: SJ N=8→N=16 improves ρ from 0.360 to 0.412±0.025 (3-seed, +0.052) on Qwen\\n    SciERC NER\\n  sections:\\n  - experiments\\n  tier: 1\\n  evidence:\\n  - exp_id: exp_012_rerun_1024\\n    metric: ner.sj_rho_full\\n    value: 0.36\\n  - exp_id: exp_001_seed42_v2\\n    metric: sj_rho_full\\n    value: 0.428\\n  - exp_id: exp_001_seed123_v2\\n    metric: sj_rho_full\\n    value: 0.424\\n  - exp_id: exp_001_seed456_v2_ner\\n    metric: full.SJ.rho\\n    value: 0.384\\n  note: '3-seed mean: (0.428+0.424+0.384)/3 ≈ 0.412, σ=0.025'\\n- id: c027_llama_conll_3seed\\n  text: 'LLaMA CoNLL N=16 3-seed: SJ ρ=0.463±0.007, logprob ρ=0.310±0.005'\\n  sections:\\n  - experiments\\n  tier: 1\\n  evidence:\\n  - exp_id: exp_017_llama_conll_n16\\n    metric: full.SJ_rho\\n    value: 0.4642\\n  - exp_id: exp_017_llama_conll_n16_s123\\n    metric: full.SJ_rho\\n    value: 0.4698\\n  - exp_id: exp_017_llama_conll_n16_s456\\n    metric: full.SJ_rho\\n    value: 0.4552\\n  - exp_id: exp_017_llama_conll_n16\\n    metric: full.logprob_rho\\n    value: 0.3058\\n  - exp_id: exp_017_llama_conll_n16_s123\\n    metric: full.logprob_rho\\n    value: 0.3161\\n  - exp_id: exp_017_llama_conll_n16_s456\\n    metric: full.logprob_rho\\n    value: 0.3078\\n- id: c028_loo_sj_circularity\\n  text: LOO-SJ Δρ=-0.014, max per-instance Δρ=3.1×10⁻⁴—circularity negligible\\n  sections:\\n  - experiments\\n  tier: 1\\n  evidence:\\n  - exp_id: exp_015_v2\\n    metric: loo_sj.max_delta_rho\\n    value: 0.000305\\n  - exp_id: exp_015_v2\\n    metric: loo_sj.all_no_circularity\\n    value: true\\n- id: c029_llama_scierc_cross_model\\n  text: 'LLaMA replicates structural-over-surface on SciERC: NER SJ ρ=0.363 > FK ρ=0.327;\\n    conditional RE SJ ρ=0.405 > FK ρ=0.259'\\n  sections:\\n  - experiments\\n  tier: 1\\n  evidence:\\n  - exp_id: exp_007_llama_inference\\n    metric: ner.rho_sj\\n    value: 0.363\\n  - exp_id: exp_007_llama_inference\\n    metric: ner.rho_fk\\n    value: 0.327\\n  - exp_id: exp_007_llama_inference\\n    metric: re.sj_rho_cond\\n    value: 0.405\\n  - exp_id: exp_007_llama_inference\\n    metric: re.fk_rho_cond\\n    value: 0.259\\n- id: c030_em_conditional_dominance\\n  text: 'EM ranks #1 on conditional set across all 4 configurations'\\n  sections:\\n  - experiments\\n  tier: 1\\n  evidence:\\n  - exp_id: exp_015_metrics_expansion\\n    metric: ner.em_rho_cond\\n    value: 0.3427\\n  - exp_id: exp_015_metrics_expansion\\n    metric: re.em_rho_cond\\n    value: 0.3607\\n  - exp_id: exp_002_conll_n16\\n    metric: conditional.EM_rho\\n    value: 0.4658\\n  - exp_id: exp_017_llama_conll_n16_s123\\n    metric: conditional.EM_rho\\n    value: 0.4732\\n  note: 'Paper cites EM conditional: SciERC NER 0.408, RE 0.485, CoNLL Qwen N=16 0.466,\\n    CoNLL LLaMA 3-seed 0.462. Registry has slightly different values from different\\n    seed/N combinations.'\\n- id: c031_em_conditional_scierc\\n  text: 'EM conditional: NER ρ=0.408, RE ρ=0.485'\\n  sections:\\n  - experiments\\n  tier: 1\\n  evidence:\\n  - exp_id: exp_001_ner_n16_scierc\\n    metric: ner_cond_em_rho\\n    value: 0.414\\n  - exp_id: exp_001_ner_n16_scierc\\n    metric: re_cond_em_rho\\n    value: 0.475\\n  note: 'Paper rounds: 0.414→0.408, 0.475→0.485. May use different seed/N baseline.'\\n- id: c032_logprob_re_cond_collapse\\n  text: Logprob conditional RE collapses to ρ=0.011\\n  sections:\\n  - experiments\\n  tier: 1\\n  evidence:\\n  - exp_id: exp_012_rerun_1024\\n    metric: re_cond.logprob.rho\\n    value: 0.0112\\n  note: 'Corrected 2026-05-16: source is exp_012_rerun_1024 (greedy_f1>0 filter, n=238).\\n    Old exp_015 value 0.1457 used wrong filter (any sample F1>0, n=331). Old text\\n    0.002 was stale and untraceable.'\\n- id: c033_sj_n16_cond_re\\n  text: At N=16, SJ maintains ρ=0.308 on conditional RE while logprob drops to -0.026\\n  sections:\\n  - experiments\\n  - discussion\\n  tier: 1\\n  evidence:\\n  - exp_id: exp_008_re_n16_v2\\n    metric: sj_rho_cond\\n    value: 0.308\\n- id: c034_structural_over_logprob_n16\\n  text: Structural-over-logprob advantage holds across all 4 N=16 settings (Δ=+0.124\\n    to +0.175)\\n  sections:\\n  - experiments\\n  - discussion\\n  tier: 1\\n  evidence:\\n  - exp_id: exp_001_ner_n16_scierc\\n    metric: ner_voting_conf_rho\\n    value: 0.399\\n  - exp_id: exp_001_ner_n16_scierc\\n    metric: ner_logprob_rho\\n    value: 0.237\\n  - exp_id: exp_002_conll_n16\\n    metric: full.EM_rho\\n    value: 0.4627\\n  - exp_id: exp_002_conll_n16\\n    metric: full.logprob_rho\\n    value: 0.3146\\n  - exp_id: exp_007_llama_n16\\n    metric: full.voting_conf_rho\\n    value: 0.4515\\n  - exp_id: exp_007_llama_n16\\n    metric: full.logprob_rho\\n    value: 0.2041\\n  - exp_id: exp_017_llama_conll_n16\\n    metric: full.SJ_rho\\n    value: 0.4642\\n  - exp_id: exp_017_llama_conll_n16\\n    metric: full.logprob_rho\\n    value: 0.3058\\n- id: c035_n_scaling_diminishing\\n  text: 'SJ N-scaling gains are sublinear: +0.052 Qwen SciERC, +0.032 LLaMA CoNLL'\\n  sections:\\n  - discussion\\n  tier: 1\\n  evidence:\\n  - exp_id: exp_001_seed42_v2\\n    metric: sj_rho_full\\n    value: 0.428\\n  - exp_id: exp_015_metrics_expansion\\n    metric: ner.sj_rho_full\\n    value: 0.3565\\n  - exp_id: exp_017_llama_conll_n16\\n    metric: full.SJ_rho\\n    value: 0.4642\\n  - exp_id: exp_017_llama_conll_infer\\n    metric: full.SJ_rho\\n    value: 0.4314\\n  note: 'Qwen SciERC: 0.412 (3-seed mean) - 0.360 = +0.052. LLaMA CoNLL: 0.463 (3-seed)\\n    - 0.431 = +0.032'\\n- id: c036_sj_ece_calibration\\n  text: '[DEPRECATED] SJ achieves lowest calibration error (ECE=0.075-0.102 across\\n    settings)'\\n  sections: []\\n  tier: X\\n  evidence: []\\n  note: DEPRECATED — reversed by c016_ece_miscalibration. Old ECE values (0.075-0.102)\\n    were from exp_015 (max_tokens=512 truncation artifact). Corrected data shows all\\n    signals ECE 0.27-0.77.\\n- id: C001\\n  location:\\n    section: abstract\\n    paragraph: 0\\n    sentence: 0\\n  text: No signal significantly improves sample selection over greedy decoding despite\\n    13-18pp oracle headroom\\n  type: empirical\\n  evidence:\\n  - exp_012_rerun_1024\\n  decisions:\\n  - D070\\n  - D071\\n  deprecated: false\\n- id: C003\\n  location:\\n    section: abstract\\n    paragraph: 0\\n    sentence: 0\\n  text: LP scores compressed into effective ties for 60% of instances under constrained\\n    decoding\\n  type: empirical\\n  evidence:\\n  - exp_012_rerun_1024\\n  decisions: []\\n  deprecated: false\\n- id: C006\\n  location:\\n    section: abstract\\n    paragraph: 0\\n    sentence: 0\\n  text: Where LP compression is absent, selection recovers +2.9pp (p=0.01)\\n  type: empirical\\n  evidence:\\n  - exp_012_rerun_1024\\n  decisions: []\\n  deprecated: false\\n- id: C010\\n  location:\\n    section: abstract\\n    paragraph: 0\\n    sentence: 0\\n  text: Constrained-decoding score compression is the primary bottleneck\\n  type: empirical\\n  evidence:\\n  - exp_012_rerun_1024\\n  decisions: []\\n  deprecated: false\\n- id: C011\\n  location:\\n    section: discussion\\n    paragraph: 0\\n    sentence: 0\\n  text: LP carries useful per-sample quality information; score compression is the\\n    primary bottleneck\\n  type: empirical\\n  evidence:\\n  - exp_012_rerun_1024\\n  decisions:\\n  - D071\\n  deprecated: false\\n- id: C013\\n  location:\\n    section: discussion\\n    paragraph: 0\\n    sentence: 0\\n  text: MBR utility correlates with F1 across instances but not within\\n  type: empirical\\n  evidence:\\n  - exp_012_rerun_1024\\n  decisions: []\\n  deprecated: false\\n- id: C016\\n  location:\\n    section: discussion\\n    paragraph: 0\\n    sentence: 0\\n  text: Free-form ablation would test if bottleneck is decoding-regime-specific\\n  type: planned\\n  evidence: []\\n  decisions:\\n  - D071\\n  deprecated: false\\n- id: C017\\n  location:\\n    section: conclusion\\n    paragraph: 0\\n    sentence: 0\\n  text: Consistency signals effective QE (rho up to 0.38, AUROC up to 0.75) but fail\\n    at selection\\n  type: empirical\\n  evidence:\\n  - exp_012_rerun_1024\\n  decisions: []\\n  deprecated: false\\n- id: C019\\n  location:\\n    section: conclusion\\n    paragraph: 0\\n    sentence: 0\\n  text: LP fails due to constrained-decoding score compression\\n  type: empirical\\n  evidence:\\n  - exp_012_rerun_1024\\n  decisions: []\\n  deprecated: false\\n- id: C022\\n  location:\\n    section: conclusion\\n    paragraph: 0\\n    sentence: 0\\n  text: RE findings preliminary, single benchmark\\n  type: scope_limitation\\n  evidence:\\n  - exp_012_rerun_1024\\n  decisions: []\\n  deprecated: false\\n- id: C023\\n  location:\\n    section: sections/discussion\\n    paragraph: 0\\n    sentence: 0\\n  text: Entity-token LP exhibits 4x higher within-instance variance than full-sequence\\n    LP on SciERC, but selection performs worse (-2.0pp)\\n  type: quantitative\\n  evidence:\\n  - exp_id: exp_entity_token_lp\\n    metric: scierc_entity_lp_variance_ratio\\n    value: 4.0x\\n  - exp_id: exp_entity_token_lp\\n    metric: scierc_entity_lp_selection_delta\\n    value: -1.68\\n  decisions: []\\n  deprecated: false\\n- id: C024\\n  location:\\n    section: sections/discussion\\n    paragraph: 0\\n    sentence: 0\\n  text: On CoNLL, entity-token LP variance collapses to near-zero (median 2e-10) with\\n    79% tied\\n  type: quantitative\\n  evidence:\\n  - exp_id: exp_entity_token_lp\\n    metric: conll_entity_lp_variance_median\\n    value: 2e-10\\n  - exp_id: exp_entity_token_lp\\n    metric: conll_entity_lp_tied_fraction\\n    value: 0.794\\n  decisions: []\\n  deprecated: false\\n- id: C025\\n  location:\\n    section: sections/discussion\\n    paragraph: 0\\n    sentence: 0\\n  text: Entity-token LP rules out format-token dilution as primary cause; points to\\n    intrinsic model overconfidence on entity tokens\\n  type: interpretive\\n  evidence:\\n  - exp_id: exp_entity_token_lp\\n  decisions: []\\n  deprecated: false\\n- id: C026\\n  location:\\n    section: sections/limitations\\n    paragraph: 0\\n    sentence: 0\\n  text: Entity-token LP is the only tested remedy; LP×VC and calibration approaches\\n    are unexplored\\n  type: scope\\n  evidence:\\n  - exp_id: exp_entity_token_lp\\n  decisions: []\\n  deprecated: false\\n- id: C027\\n  location:\\n    section: sections/introduction\\n    paragraph: 0\\n    sentence: 0\\n  text: 'C1 reframe: instance-level nature is setup, LP compression + MBR within-instance\\n    failure are the findings'\\n  type: structural\\n  evidence: []\\n  decisions: []\\n  deprecated: false\\n- id: C028\\n  location:\\n    section: sections/introduction\\n    paragraph: 0\\n    sentence: 0\\n  text: 'SF4: 60% tied replaced with pooled within-instance ρ(LP,F1)=0.248 continuous\\n    characterization'\\n  type: structural\\n  evidence: []\\n  decisions: []\\n  deprecated: false\\n- id: C029\\n  location:\\n    section: sections/introduction\\n    paragraph: 0\\n    sentence: 0\\n  text: 'C2 reframe: entity-token LP added as diagnostic ablation contribution'\\n  type: structural\\n  evidence:\\n  - exp_id: exp_entity_token_lp\\n  decisions: []\\n  deprecated: false\\n- id: C030\\n  location:\\n    section: sections/abstract\\n    paragraph: 0\\n    sentence: 0\\n  text: 'SF3: RE removed from abstract; SF1: ρ=0.38 sourced to SciERC primary, up\\n    to 0.45 on ceiling control; MF2(a): benchmark roles explicit; M2: streamlined\\n    from 9 to 6 sentences'\\n  type: structural\\n  evidence: []\\n  decisions: []\\n  deprecated: false\\n- id: C031\\n  location:\\n    section: sections/discussion\\n    paragraph: 0\\n    sentence: 0\\n  text: 21% of SciERC instances produce identical F1 across all N samples\\n  type: quantitative\\n  evidence: Q1 within-instance analysis\\n  decisions: []\\n  deprecated: false\\n- id: C032\\n  location:\\n    section: sections/discussion\\n    paragraph: 0\\n    sentence: 0\\n  text: 58% of CoNLL instances produce identical F1 across all N samples\\n  type: quantitative\\n  evidence: Q1 within-instance analysis\\n  decisions: []\\n  deprecated: false\\n- id: C033\\n  location:\\n    section: sections/discussion\\n    paragraph: 0\\n    sentence: 0\\n  text: 13% of SciERC instances yield constant utility scores\\n  type: quantitative\\n  evidence: Q1 within-instance analysis\\n  decisions: []\\n  deprecated: false\\n- id: C034\\n  location:\\n    section: sections/discussion\\n    paragraph: 0\\n    sentence: 0\\n  text: 49% of CoNLL instances yield constant utility scores\\n  type: quantitative\\n  evidence: Q1 within-instance analysis\\n  decisions: []\\n  deprecated: false\\n- id: C035\\n  location:\\n    section: sections/discussion\\n    paragraph: 0\\n    sentence: 0\\n  text: SJ median within-instance rho = 0.524 on SciERC\\n  type: quantitative\\n  evidence: Q1 within-instance analysis\\n  decisions: []\\n  deprecated: false\\n- id: C036\\n  location:\\n    section: sections/discussion\\n    paragraph: 0\\n    sentence: 0\\n  text: SJ median within-instance rho = 0.994 on CoNLL\\n  type: quantitative\\n  evidence: Q1 within-instance analysis\\n  decisions: []\\n  deprecated: false\\n- id: C037\\n  location:\\n    section: sections/discussion\\n    paragraph: 0\\n    sentence: 0\\n  text: MBR closes 23% of oracle gap on non-degenerate SciERC instances\\n  type: quantitative\\n  evidence: Q1 within-instance analysis\\n  decisions: []\\n  deprecated: false\\n- id: C038\\n  location:\\n    section: sections/discussion\\n    paragraph: 0\\n    sentence: 0\\n  text: MBR closes 41% of oracle gap on non-degenerate CoNLL instances\\n  type: quantitative\\n  evidence: Q1 within-instance analysis\\n  decisions: []\\n  deprecated: false\\n- id: C039\\n  location:\\n    section: sections/discussion\\n    paragraph: 0\\n    sentence: 0\\n  text: Greedy T=0 achieves F1=0.663 on SciERC, surpassing all N=8 selection strategies\\n  type: quantitative\\n  evidence: SF4 greedy data\\n  decisions: []\\n  deprecated: false\\n- id: C040\\n  location:\\n    section: sections/discussion\\n    paragraph: 0\\n    sentence: 0\\n  text: SciERC 3-epoch rho=0.32 vs 5-epoch rho=0.28; LP delta -1.18 vs +0.62 pp\\n  type: quantitative\\n  evidence: tab:epoch_scierc\\n  decisions: []\\n  deprecated: false\\n- id: C041\\n  location:\\n    section: sections/discussion\\n    paragraph: 0\\n    sentence: 0\\n  text: Entity-level majority voting yields +0.76pp on SciERC (5.8% gap recovery)\\n  type: quantitative\\n  evidence: []\\n  decisions: []\\n  deprecated: false\\n- id: C042\\n  location:\\n    section: sections/discussion\\n    paragraph: 0\\n    sentence: 0\\n  text: Entity-level majority voting yields -0.64pp on CoNLL\\n  type: quantitative\\n  evidence: []\\n  decisions: []\\n  deprecated: false\\n- id: C043\\n  location:\\n    section: sections/discussion\\n    paragraph: 0\\n    sentence: 0\\n  text: Entity-level majority voting yields -3.21pp on Few-NERD\\n  type: quantitative\\n  evidence: []\\n  decisions: []\\n  deprecated: false\\n- id: C044\\n  location:\\n    section: sections/discussion\\n    paragraph: 0\\n    sentence: 0\\n  text: On degenerate subsets, merge is uniformly negative across all three datasets\\n  type: quantitative\\n  evidence: []\\n  decisions: []\\n  deprecated: false\\n- id: C045\\n  location:\\n    section: sections/appendix\\n    paragraph: 0\\n    sentence: 0\\n  text: Exact permutation p=0.005 for per-type degeneracy-headroom correlation\\n  type: quantitative\\n  evidence: []\\n  decisions: []\\n  deprecated: false\\n- id: C046\\n  location:\\n    section: sections/appendix\\n    paragraph: 0\\n    sentence: 0\\n  text: Under conservative df=4 adjustment, p=0.033\\n  type: quantitative\\n  evidence: []\\n  decisions: []\\n  deprecated: false\\n- id: C047\\n  location:\\n    section: sections/appendix\\n    paragraph: 0\\n    sentence: 0\\n  text: 3-epoch SciERC mean within-instance rho=0.273\\n  type: quantitative\\n  evidence: []\\n  decisions: []\\n  deprecated: false\\n- id: C048\\n  location:\\n    section: sections/appendix\\n    paragraph: 0\\n    sentence: 0\\n  text: 5-epoch SciERC mean within-instance rho=0.179\\n  type: quantitative\\n  evidence: []\\n  decisions: []\\n  deprecated: false\\n- id: C049\\n  location:\\n    section: sections/appendix\\n    paragraph: 0\\n    sentence: 0\\n  text: 76.4% of instances show positive LP-quality correlation at 3 epochs\\n  type: quantitative\\n  evidence: []\\n  decisions: []\\n  deprecated: false\\n- id: C050\\n  location:\\n    section: sections/appendix\\n    paragraph: 0\\n    sentence: 0\\n  text: 64.1% of instances show positive LP-quality correlation at 5 epochs\\n  type: quantitative\\n  evidence: []\\n  decisions: []\\n  deprecated: false\\n- id: C051\\n  location:\\n    section: sections/appendix\\n    paragraph: 0\\n    sentence: 0\\n  text: Epoch-to-epoch alignment variation is 0.057 median rho, small vs cross-dataset\\n    gap\\n  type: quantitative\\n  evidence: []\\n  decisions: []\\n  deprecated: false\\n- id: C052\\n  location:\\n    section: sections/appendix\\n    paragraph: 0\\n    sentence: 0\\n  text: 'Optimal DALS tau spans 2 orders of magnitude: FN 0.001, SciERC 0.05, CoNLL\\n    0.10'\\n  type: quantitative\\n  evidence: []\\n  decisions: []\\n  deprecated: false\\n- id: C053\\n  location:\\n    section: sections/appendix\\n    paragraph: 0\\n    sentence: 0\\n  text: LOO regret ranges from 0.51 to 1.21pp\\n  type: quantitative\\n  evidence: []\\n  decisions: []\\n  deprecated: false\\n- id: C054\\n  location:\\n    section: sections/appendix\\n    paragraph: 0\\n    sentence: 0\\n  text: Even with oracle tau, CoNLL remains at -0.31pp\\n  type: quantitative\\n  evidence: []\\n  decisions: []\\n  deprecated: false\\n- id: C055\\n  location:\\n    section: sections/appendix\\n    paragraph: 0\\n    sentence: 0\\n  text: 'SciERC entity merge best k=3: +1.57pp, 11.9% recovery'\\n  type: quantitative\\n  evidence: []\\n  decisions: []\\n  deprecated: false\\n- id: C056\\n  location:\\n    section: sections/appendix\\n    paragraph: 0\\n    sentence: 0\\n  text: 'CoNLL entity merge best k=3: -0.38pp, -9.0% recovery'\\n  type: quantitative\\n  evidence: []\\n  decisions: []\\n  deprecated: false\\n- id: C057\\n  location:\\n    section: sections/appendix\\n    paragraph: 0\\n    sentence: 0\\n  text: 'FewNERD entity merge best k=2: -0.43pp, -3.6% recovery'\\n  type: quantitative\\n  evidence: []\\n  decisions: []\\n  deprecated: false\\n- id: C058\\n  location:\\n    section: sections/experiments\\n    paragraph: 0\\n    sentence: 0\\n  text: 'Conditional decomp SciERC favorable: +2.47pp CI [+0.30, +4.70]'\\n  type: quantitative\\n  evidence: []\\n  decisions: []\\n  deprecated: false\\n- id: C059\\n  location:\\n    section: sections/experiments\\n    paragraph: 0\\n    sentence: 0\\n  text: 'Conditional decomp FewNERD favorable: +0.63pp CI [-0.02, +1.30], marginal'\\n  type: quantitative\\n  evidence: []\\n  decisions: []\\n  deprecated: false\\n- id: C060\\n  location:\\n    section: sections/experiments\\n    paragraph: 0\\n    sentence: 0\\n  text: 'Conditional decomp CoNLL favorable: -1.78pp CI [-2.83, -0.76], negative'\\n  type: quantitative\\n  evidence: []\\n  decisions: []\\n  deprecated: false\\n- id: C061\\n  location:\\n    section: sections/appendix\\n    paragraph: 0\\n    sentence: 0\\n  text: Entity-token LP has 4x higher within-instance variance (0.000644 vs 0.000161)\\n  type: quantitative\\n  evidence: []\\n  decisions: []\\n  deprecated: false\\n- id: C062\\n  location:\\n    section: sections/appendix\\n    paragraph: 0\\n    sentence: 0\\n  text: Entity-token LP rho=0.440 vs full-sequence 0.297\\n  type: quantitative\\n  evidence: []\\n  decisions: []\\n  deprecated: false\\n- id: C063\\n  location:\\n    section: sections/appendix\\n    paragraph: 0\\n    sentence: 0\\n  text: Entity-token LP selection -0.73pp vs full-sequence +0.35pp\\n  type: quantitative\\n  evidence: []\\n  decisions: []\\n  deprecated: false\\ntables:\\n- id: tab:notation\\n  section: method\\n  caption: Notation used throughout the paper\\n  evidence: []\\n  note: Notation table—no experimental data.\\n- id: tab:quality_estimation\\n  section: experiments\\n  caption: Quality estimation across tasks and models (Spearman ρ and AUROC)\\n  evidence:\\n  - exp_id: exp_012_rerun_1024\\n    role: SciERC NER ρ values (N=8, Qwen) — corrected from exp_015 (truncation artifact)\\n  - exp_id: exp_015_metrics_expansion\\n    role: SciERC RE ρ values (N=8, Qwen) — RE values unaffected by truncation fix\\n  - exp_id: exp_015_v2\\n    role: AUROC values across settings\\n  - exp_id: exp_002\\n    role: CoNLL Qwen N=8 ρ and AUROC\\n  - exp_id: exp_017_llama_conll_infer\\n    role: CoNLL LLaMA N=8 ρ and AUROC\\n  - exp_id: exp_017_llama_conll_n16\\n    role: LLaMA CoNLL N=16 3-seed (seed=42)\\n  - exp_id: exp_017_llama_conll_n16_s123\\n    role: LLaMA CoNLL N=16 3-seed (seed=123)\\n  - exp_id: exp_017_llama_conll_n16_s456\\n    role: LLaMA CoNLL N=16 3-seed (seed=456)\\n- id: tab:selection\\n  section: experiments\\n  caption: Best-of-N selection F1 on SciERC (N=8, T=1.0)\\n  evidence:\\n  - exp_id: exp_016_signal_ensemble\\n    role: All selection F1 values (NER and RE)\\n- id: tab:robustness\\n  section: experiments\\n  caption: Signal robustness across configurations (Spearman ρ)\\n  evidence:\\n  - exp_id: exp_005\\n    role: Temperature block (T=0.7 vs T=1.0, Qwen SciERC)\\n  - exp_id: exp_015_metrics_expansion\\n    role: N=8 baseline values\\n  - exp_id: exp_001_seed42_v2\\n    role: N=16 SJ ρ seed=42\\n  - exp_id: exp_001_seed123_v2\\n    role: N=16 SJ ρ seed=123\\n  - exp_id: exp_001_seed456_v2_ner\\n    role: N=16 SJ ρ seed=456\\n  - exp_id: exp_017_llama_conll_n16\\n    role: 'Cross-model block: LLaMA CoNLL N=16 seed=42'\\n  - exp_id: exp_017_llama_conll_n16_s123\\n    role: 'Cross-model block: LLaMA CoNLL N=16 seed=123'\\n  - exp_id: exp_017_llama_conll_n16_s456\\n    role: 'Cross-model block: LLaMA CoNLL N=16 seed=456'\\nfigures:\\n- id: fig:overview\\n  section: introduction\\n  caption: The correlation-selection gap conceptual diagram\\n  evidence:\\n  - exp_id: exp_015_metrics_expansion\\n    role: Quality estimation data (ρ, AUROC for left panel)\\n  - exp_id: exp_016_signal_ensemble\\n    role: Selection F1 data (right panel)\\n- id: fig:signal_heatmap\\n  section: experiments\\n  caption: Quality estimation heatmap (Spearman ρ) across five signals and four configurations\\n  evidence:\\n  - exp_id: exp_015_metrics_expansion\\n    role: Full set ρ values for SciERC NER/RE (Qwen, N=8)\\n  - exp_id: exp_002\\n    role: CoNLL Qwen full set ρ values\\n  - exp_id: exp_001_ner_n16_scierc\\n    role: Conditional set ρ values\\n- id: fig:selection_gap\\n  section: experiments\\n  caption: The correlation-selection gap on SciERC (N=8)\\n  evidence:\\n  - exp_id: exp_016_signal_ensemble\\n    role: Best-of-N selection F1 bars and quality estimation ρ line\\n- id: fig:temperature_robustness\\n  section: experiments\\n  caption: Temperature robustness on SciERC (N=8)\\n  evidence:\\n  - exp_id: exp_005\\n    role: SJ, FK ρ values at T=0.7 and T=1.0\\n- id: fig:reliability\\n  section: experiments\\n  caption: Reliability diagrams on SciERC (N=8, T=1.0)\\n  evidence:\\n  - exp_id: exp_015_metrics_expansion\\n    role: Calibration/ECE data for all signals\\n  - exp_id: exp_002\\n    role: ECE values across signals\\n_completeness:\\n  coverage: 59/92\\n  claims: 87\\n  tables: 4\\n  figures: 5\\n  tier_counts:\\n    tier1: 0\\n    tier2: 59\\n    tier3: 33\\n    tierX: 0\\n  last_checked: '2026-05-18T15:39:48.035668+00:00'\\n\", \"total_chars\": 32730, \"truncated\": false}, \"error\": null, \"metadata\": {}}"
    }
  },
  "sourceToolAssistantUUID": "48ec8556-919d-4a44-b77b-41d41a712173",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "a6ae7e35-390a-442a-93d4-9958c82c9e3b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-19T13:55:30.567Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01Jp9yni6FXAWKAbWxjo6UoV`</summary>

```json
{
  "server": "autodl-5090",
  "command": "find /root/autodl-tmp/struct_self_consist_ie -name \"quality_estimation*\" -path \"*exp_012*\" -type f"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "510e364c-5ca9-4b9e-b58e-5f0d8977856b",
  "isSidechain": false,
  "requestId": "req_011CbC3LnYDy8MNiyH2QdQNP",
  "type": "assistant",
  "uuid": "1f451f22-9207-4b2d-bfd6-5475630305e8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "a6ae7e35-390a-442a-93d4-9958c82c9e3b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Huxd6tgZmMAF1BcTukw4RG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4226,
      "cache_creation_input_tokens": 3649,
      "cache_read_input_tokens": 37045,
      "output_tokens": 2157,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3649,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 4226,
          "output_tokens": 2157,
          "cache_read_input_tokens": 37045,
          "cache_creation_input_tokens": 3649,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3649
          },
          "type": "message"
        }
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

_source line 31 · 2026-05-19T13:55:31.168Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01NajERzs4SxgcSGqQmALXmf`</summary>

```json
{
  "server": "autodl-5090",
  "command": "find /root/autodl-tmp/struct_self_consist_ie -name \"auroc*\" -path \"*scierc*\" -type f"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1f451f22-9207-4b2d-bfd6-5475630305e8",
  "isSidechain": false,
  "requestId": "req_011CbC3LnYDy8MNiyH2QdQNP",
  "type": "assistant",
  "uuid": "4e801a9e-047c-4d68-966c-4372d9faba27",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "a6ae7e35-390a-442a-93d4-9958c82c9e3b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Huxd6tgZmMAF1BcTukw4RG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4226,
      "cache_creation_input_tokens": 3649,
      "cache_read_input_tokens": 37045,
      "output_tokens": 2157,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3649,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 4226,
          "output_tokens": 2157,
          "cache_read_input_tokens": 37045,
          "cache_creation_input_tokens": 3649,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3649
          },
          "type": "message"
        }
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

_source line 32_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[System 触发审查]: 收到你的 critical 审查报告，6 个数据一致性问题全部确认。已派 Agent 紧急调查修复。  请你重点关注 P0-1 SciERC AUROC 问题：如果 EM AUROC 确实是 0.749 而非 0.614，论文中以下叙述可能需要修改： 1. Table 1 信号排序结论（EM 可能超过 VC 成为 SciERC 最高 AUROC） 2. 正文中关于\"s…",
  "leafUuid": "4e801a9e-047c-4d68-966c-4372d9faba27",
  "sessionId": "a6ae7e35-390a-442a-93d4-9958c82c9e3b"
}
```

---

### Runtime record

_source line 33_

```json
{
  "type": "ai-title",
  "aiTitle": "Verify SciERC AUROC data consistency issues",
  "sessionId": "a6ae7e35-390a-442a-93d4-9958c82c9e3b"
}
```

---

### Tool result

_source line 34 · 2026-05-19T13:55:31.584Z_

<details><summary>↩ Tool result · `toolu_01Jp9yni6FXAWKAbWxjo6UoV`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.01}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1f451f22-9207-4b2d-bfd6-5475630305e8",
  "isSidechain": false,
  "promptId": "2279f609-b135-4e34-8568-a1f529688be0",
  "type": "user",
  "uuid": "9389b9a8-6260-4f0f-8296-cb6b8895de9f",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 1.01}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.01}}"
    }
  },
  "sourceToolAssistantUUID": "1f451f22-9207-4b2d-bfd6-5475630305e8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "a6ae7e35-390a-442a-93d4-9958c82c9e3b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-19T13:55:32.024Z_

<details><summary>↩ Tool result · `toolu_01NajERzs4SxgcSGqQmALXmf`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4e801a9e-047c-4d68-966c-4372d9faba27",
  "isSidechain": false,
  "promptId": "2279f609-b135-4e34-8568-a1f529688be0",
  "type": "user",
  "uuid": "2acac171-182c-4072-84be-701492e0f40f",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.43}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"
    }
  },
  "sourceToolAssistantUUID": "4e801a9e-047c-4d68-966c-4372d9faba27",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "a6ae7e35-390a-442a-93d4-9958c82c9e3b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 36 · 2026-05-19T13:55:32.028Z_

```json
{
  "parentUuid": "2acac171-182c-4072-84be-701492e0f40f",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "df362ef5-0860-4972-b890-df1e5922956e",
  "timestamp": "2026-05-19T13:55:32.028Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "a6ae7e35-390a-442a-93d4-9958c82c9e3b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 37 · 2026-05-19T13:56:16.569Z_

<details><summary>Logged reasoning block</summary>

```text
Very important findings from paper_provenance.yaml:

1. **c002_auroc_dissociation_scierc** explicitly states: "ρ-AUROC dissociation on SciERC — EM leads AUROC (NER 0.749, RE 0.706) while Voting leads ρ (NER 0.379, RE 0.422)". Evidence is from exp_012_rerun_1024, metric: ner.em_auroc, value: 0.749.

2. **tab:quality_estimation** lists evidence sources. The AUROC values are sourced from **exp_015_v2** (not exp_012_rerun_1024). 

The rho values come from exp_012_rerun_1024, but the AUROC values in the table are from exp_015_v2, which might contain outdated numbers. The provenance confirms the correct EM AUROC should be 0.749, yet the table still displays 0.614—suggesting the paper wasn't updated when the provenance was corrected. Looking at the actual values from exp_012_rerun_1024, almost every AUROC number in the paper is incorrect—only LP matches at 0.578, while EM should be 0.749 instead of 0.614, SJ should be 0.692 instead of 0.650, FK should be 0.629 instead of 0.602, and VC should be 0.684 instead of 0.663. This completely reverses the ranking, with EM actually leading rather than trailing as the paper suggests.

The narrative about structural signals leading becomes more complicated because while the rho values do show VC and SJ ahead of LP as the paper claims, the AUROC story tells a different story where EM dominates—so the paper's conclusions about which signals matter most appear to be based on incomplete or incorrect data. The conclusion's aggregate numbers (ρ up to 0.45, AUROC up to 0.82) are actually correct since they're pulling from CoNLL with the EM signal, but the real problem is that Table 1's SciERC column still shows the wrong AUROC values—it should reflect EM's 0.749 instead of VC's 0.663. I'm checking the provenance table to see what exp_015_v2 actually reports for these AUROC values across the different datasets. Looking at the CoNLL data, the paper's Qwen values (EM rho=0.451, AUROC=0.816) match exp_002 from the registry (em_rho_full=0.4507, em_auroc_full=0.8156), which the provenance confirms is N=8. But I'm seeing exp_002_conll_n16 in the registry too, so I need to figure out whether exp_002 itself is the N=8 version or if there's a separate designation.

For the P1-6 issue about mixing N=8 and N=16 data in degeneracy rates, I need to search the paper text for any degeneracy claims and verify they're using consistent sample sizes. Let me check the experiments file for where degeneracy is discussed.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "df362ef5-0860-4972-b890-df1e5922956e",
  "isSidechain": false,
  "requestId": "req_011CbC3Pxv93WgQzk1DKwMVV",
  "type": "assistant",
  "uuid": "d5e28a62-f670-4acd-8210-54fb8c6d0662",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "a6ae7e35-390a-442a-93d4-9958c82c9e3b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011jjkmKY2LB54THfWCyG2US",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 20622,
      "cache_read_input_tokens": 40694,
      "output_tokens": 2413,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 20622,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2413,
          "cache_read_input_tokens": 40694,
          "cache_creation_input_tokens": 20622,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 20622
          },
          "type": "message"
        }
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

_source line 38 · 2026-05-19T13:56:16.801Z_

关键发现：paper_provenance.yaml c002 已明确记录 "EM leads AUROC (NER 0.749)"，但论文 Table 1 仍写 0.614。现在检查论文中 degeneracy 相关叙述和 N=8/N=16 混用风险。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d5e28a62-f670-4acd-8210-54fb8c6d0662",
  "isSidechain": false,
  "requestId": "req_011CbC3Pxv93WgQzk1DKwMVV",
  "type": "assistant",
  "uuid": "72ca8e3b-8de8-4f3c-bcb2-3c710d903c18",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "a6ae7e35-390a-442a-93d4-9958c82c9e3b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011jjkmKY2LB54THfWCyG2US",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 20622,
      "cache_read_input_tokens": 40694,
      "output_tokens": 2413,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 20622,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2413,
          "cache_read_input_tokens": 40694,
          "cache_creation_input_tokens": 20622,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 20622
          },
          "type": "message"
        }
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

_source line 39 · 2026-05-19T13:56:19.160Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01K5qF2doGHQuKoUzMtGrcVw`</summary>

```json
{
  "pattern": "degen|N.?=.?16|N.?=.?8",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper",
  "output_mode": "content",
  "-n": true,
  "-i": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "72ca8e3b-8de8-4f3c-bcb2-3c710d903c18",
  "isSidechain": false,
  "requestId": "req_011CbC3Pxv93WgQzk1DKwMVV",
  "type": "assistant",
  "uuid": "86d8657a-d9ed-407b-9d00-16dc11baeb83",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "a6ae7e35-390a-442a-93d4-9958c82c9e3b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011jjkmKY2LB54THfWCyG2US",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 20622,
      "cache_read_input_tokens": 40694,
      "output_tokens": 2413,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 20622,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2413,
          "cache_read_input_tokens": 40694,
          "cache_creation_input_tokens": 20622,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 20622
          },
          "type": "message"
        }
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

_source line 40 · 2026-05-19T13:56:20.210Z_

<details><summary>↩ Tool result · `toolu_01XjZ2APjZSKQ5EDBhYNyDgv`</summary>

```text
&lt;persisted-output>
Output too large (47.7KB). Full output saved to: /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-reviewer-0064dd56/a6ae7e35-390a-442a-93d4-9958c82c9e3b/tool-results/toolu_01XjZ2APjZSKQ5EDBhYNyDgv.txt

Preview (first 2KB):
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.fls-322-INPUT /usr/share/texlive/texmf-dist/fonts/tfm/public/cm/cmbx10.tfm
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.fls-323-INPUT /usr/share/texlive/texmf-dist/fonts/tfm/public/cm/cmbx8.tfm
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.fls:324:INPUT ./figures/fig_degeneracy_lp_scatter.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.fls:325:INPUT ./figures/fig_degeneracy_lp_scatter.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.fls:326:INPUT ./figures/fig_degeneracy_lp_scatter.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.fls:327:INPUT ./figures/fig_degeneracy_lp_scatter.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.fls:328:INPUT ./figures/fig_degeneracy_lp_scatter.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.fls-329-INPUT /usr/share/texlive/texmf-dist/fonts/vf/adobe/times/ptmb8t.vf
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.fls-330-INPUT /usr/share/texlive/texmf-dist/fonts/tfm/adobe/times/ptmb8r.tfm
--
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.bbl-226-Ari Holtzman, Jan Buys, Li~Du, Maxwell Forbes, and Yejin Choi. 2020.
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.bbl-227-\newblock \href {https://openreview.net/forum?id=rygGQyrFvH} {The curious case
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.bbl:228:  of neural text degeneration}.
...
&lt;/persisted-output>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2fae23d2-b5a0-47cd-83c7-cfefc7eb209b",
  "isSidechain": false,
  "promptId": "2279f609-b135-4e34-8568-a1f529688be0",
  "type": "user",
  "uuid": "eb344fe9-a9c9-4807-b133-fd7c8f9bf748",
  "toolUseResult": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.fls-322-INPUT /usr/share/texlive/texmf-dist/fonts/tfm/public/cm/cmbx10.tfm\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.fls-323-INPUT /usr/share/texlive/texmf-dist/fonts/tfm/public/cm/cmbx8.tfm\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.fls:324:INPUT ./figures/fig_degeneracy_lp_scatter.pdf\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.fls:325:INPUT ./figures/fig_degeneracy_lp_scatter.pdf\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.fls:326:INPUT ./figures/fig_degeneracy_lp_scatter.pdf\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.fls:327:INPUT ./figures/fig_degeneracy_lp_scatter.pdf\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.fls:328:INPUT ./figures/fig_degeneracy_lp_scatter.pdf\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.fls-329-INPUT /usr/share/texlive/texmf-dist/fonts/vf/adobe/times/ptmb8t.vf\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.fls-330-INPUT /usr/share/texlive/texmf-dist/fonts/tfm/adobe/times/ptmb8r.tfm\n--\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.bbl-226-Ari Holtzman, Jan Buys, Li~Du, Maxwell Forbes, and Yejin Choi. 2020.\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.bbl-227-\\newblock \\href {https://openreview.net/forum?id=rygGQyrFvH} {The curious case\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.bbl:228:  of neural text degeneration}.\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.bbl-229-\\newblock In \\emph{Proceedings of the Eighth International Conference on\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.bbl-230-  Learning Representations (ICLR)}.\n--\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.log-637-(pdftex.def)             Requested size: 219.08614pt x 133.98662pt.\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.log-638-[5 <./figures/fig_selection_gap.pdf>]\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.log:639:&lt;figures/fig_degeneracy_lp_scatter.pdf, id=835, 496.89139pt x 338.86536pt>\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.log:640:File: figures/fig_degeneracy_lp_scatter.pdf Graphic file (type pdf)\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.log:641:&lt;use figures/fig_degeneracy_lp_scatter.pdf>\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.log:642:Package pdftex.def Info: figures/fig_degeneracy_lp_scatter.pdf  used on input l\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.log-643-ine 138.\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.log-644-(pdftex.def)             Requested size: 219.08614pt x 149.41145pt.\n--\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.log-653- []\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.log-654-\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.log:655:[7 <./figures/fig_degeneracy_lp_scatter.pdf>]\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.log-656-Underfull \\hbox (badness 1394) in paragraph at lines 249--254\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.log-657-\\T1/ptm/m/n/10.95 (+20) Sci-ERC $\\OT1/cmr/m/n/10.95 0\\OML/cmm/m/it/10.95 :\\OT1/\n--\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.log-1146-\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.log-1147-Underfull \\hbox (badness 1715) in paragraph at lines 1435--1439\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.log:1148:\\T1/ptm/m/n/10.95 (+20) vari-a-tion re-mains un-ver-i-fied; high-degeneracy\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.log-1149- []\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.log-1150-\n--\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex-5-Test-time scaling studies \\cite{snell2025scaling, brown2024monkeys} and reward-free selectors \\cite{taubenfeld2025cisc, kang2025selfcertainty, wang2025rankedvoting, oh2026latentsc} rely on answer-level agreement.\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex-6-Adaptive variants gate on answer agreement \\cite{aggarwal2023adaptive}, input difficulty \\cite{wang2025make, feng2025optimal}, or response confidence \\cite{kim2026reasc}; \\citet{chen2025twofailures} diagnose SC failure modes without proposing gating.\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex:7:All target discrete-answer reasoning; structured prediction requires different gating signals because degeneracy operates at the entity-set level.\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex-8-\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex-9-\\paragraph{Consistency for structured IE.}\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex:10:\\citet{yao2026consistency} show consistency correlates with accuracy for LLM-based NER/RE; we show correlation alone does not ensure selection gains, diagnosing degeneracy and compression as blocking mechanisms.\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex-11-CoCoA \\cite{vashurin2025cocoa} fuses confidence with consistency; our supervised baseline confirms combination is not the bottleneck (\\S\\ref{sec:robustness_main}).\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex-12-Earlier work on confidence for structured prediction \\cite{culotta2004confidence, mejer2010confidence, fomicheva2020unsupervised} establishes the paradigm we extend to set-valued outputs.\n--\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex-19-\\paragraph{Uncertainty estimation and MBR decoding.}\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex-20-Surveys cover confidence estimation \\cite{geng2024confidence}, uncertainty quantification \\cite{xia2025survey}, and calibration \\cite{hobelsberger2025systematic}; semantic uncertainty \\cite{kuhn2023semantic, farquhar2024detecting} and P(True) \\cite{kadavath2022language} provide model-internal alternatives.\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex:21:Our selection strategies instantiate MBR decoding \\cite{eikema2022sampling, deguchi2024centroid}; unlike MT where MBR yields consistent gains \\cite{freitag2022high} and code generation where execution-based MBR improves selection \\cite{shi2022mbr}, instance degeneracy eliminates the headroom MBR needs even when utility is well-aligned ($\\rho{=}0.52$; \\S\\ref{sec:discussion}).\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex:22:\\citet{eikema2025structured} find MBR utilities degrade on structured outputs; our diagnosis is complementary: degeneracy, not utility misalignment, is the primary bottleneck.\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex-23-Our QE results connect to selective prediction \\cite{geifman2017selective, kuleshov2015calibrated, varshney2022investigating}: signals with AUROC up to 0.82 support abstention policies independent of sample selection.\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex-24-\n--\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex-8-We evaluate on four English NER benchmarks spanning a difficulty gradient, each serving a distinct role.\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex-9-\\textbf{SciERC} \\cite{luan2018scierc} (551 test instances, 6 entity types) is the primary medium-difficulty test bed where models achieve ${\\approx}$65\\% F1.\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex:10:\\textbf{Few-NERD} \\cite{ding2021fewnerd} (INTRA coarse; 37{,}648 instances, 8 entity types, ${\\approx}$75\\% F1) provides a low-degeneracy contrast where LP selection succeeds (\\S\\ref{sec:fewnerd}).\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex-11-\\textbf{CoNLL-2003} \\cite{tjongkimsang2003conll} (3{,}453 test sentences, 4 entity types, ${\\approx}$91\\% F1) serves as a ceiling-effect control where limited oracle headroom constrains selection gains.\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex-12-\\textbf{WNUT-17} \\cite{derczynski2017wnut} (1{,}287 social media instances, 51\\% zero F1) probes the signal-collapse boundary where model capability is insufficient.\n--\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex-55-Four of five signals (SJ, FK, EM, VC) assign identical scores to all candidates from the same input by construction (\\S\\ref{sec:formulation}); they can estimate quality across instances but cannot rank candidates within an instance.\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex-56-The empirical question is whether LP, the sole per-sample signal, can exploit its candidate-discriminative nature for selection.\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex:57:LP selection effectiveness is primarily determined by LP-quality alignment rather than degeneracy level (\\S\\ref{sec:discussion}).\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex-58-Cross-instance $\\rho$ (Table~\\ref{tab:quality_estimation}) is attenuated by varying instance difficulty; within-instance $\\rho$ directly measures whether LP discriminates candidates for a fixed input, making it the relevant predictor of selection success.\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex-59-\n--\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex-97-On SciERC ($n{=}529$, 2-seed sign tests\\footnote{MDE${\\approx}$1.5~pp at 80\\% power ($n{=}529$); Few-NERD ($n{=}32{,}565$; MDE${\\approx}$0.22~pp) provides the definitive test.}), the oracle (0.775) reveals 13.0~pp of headroom, but LP achieves $+0.2$~pp ($p{=}0.29$), below the MDE (${\\approx}$1.5~pp); selection effects below this threshold cannot be reliably detected.\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex-98-The pattern holds across CoNLL and WNUT-17 (Table~\\ref{tab:cross_selection}); under stringent TOST anchors, some configurations show significant \\textit{degradation} (Appendix~\\ref{app:tost}).\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex:99:Few-NERD provides the definitive contrast: LP achieves $+1.39$~pp ($p{<}0.001$) at low degeneracy (\\S\\ref{sec:fewnerd}), while structural signals still degrade selection.\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex-100-\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex-101-\\paragraph{Qualitative factors governing selection effectiveness.}\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex:102:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex:103:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex-104-Yet QE remains effective on WNUT-17 (VC $\\rho{=}0.724$; Table~\\ref{tab:wnut}), confirming QE-selection decoupling at this boundary.\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex-105-This characterization is qualitative: the three factors do not combine into a predictive model ($R^2{<}0$ across 23 configurations), but each factor's role is individually supported by controlled ablations (\\S\\ref{sec:fewnerd}, \\S\\ref{sec:discussion}).\n--\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex-127-\\end{table}\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex-128-\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex:129:Few-NERD (Table~\\ref{tab:fewnerd}) confirms LP selection at low degeneracy: $+1.39$~pp ($p{<}0.001$), while structural signals degrade selection (VC $-1.79$, SJ $-2.14$~pp). LP is 50$\\times$ more seed-stable ($\\sigma{=}0.04$ vs.\\ SJ $2.02$~pp) and generalizes to LLaMA-3.1-8B (Table~\\ref{tab:cross_selection}).\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex:130:Training convergence modulates degeneracy: 5-epoch Few-NERD raises degeneracy to 31\\% and halves LP gains (Appendix~\\ref{app:epoch_confound}).\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex-131-\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex-132-\\paragraph{Degeneracy alone does not predict LP selection direction.}\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex:133:Across 23 configurations, degeneracy does not predict LP gain ($\\rho{=}0.052$, $p{=}0.81$; Figure~\\ref{fig:degeneracy_scatter}), though within fixed settings it causally modulates LP ($\\rho{=}{-}0.881$; Appendix~\\ref{app:per_type_lp}).\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex-134-Cross-dataset prediction requires LP signal quality: Few-NERD ($\\rho{\\approx}0.5$--$0.7$) shows consistent gains, SciERC ($\\rho{\\approx}0.26$) does not (Appendix~\\ref{app:conditional_decomp}).\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex-135-\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex-136-\\begin{figure}[t]\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex-137-\\centering\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex:138:\\includegraphics[width=\\columnwidth]{figures/fig_degeneracy_lp_scatter.pdf}\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex:139:\\caption{Instance degeneracy vs.\\ LP selection gain across 23 configurations ($N{=}8$; $\\rho{=}0.052$, $p{=}0.81$). Within Few-NERD per-entity-type analysis ($\\rho{=}{-}0.881$; Appendix~\\ref{app:per_type_lp}), degeneracy predicts LP gain when alignment is held constant.}\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex:140:\\label{fig:degeneracy_scatter}\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex-141-\\end{figure}\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex-142-\n--\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex-168-\\paragraph{Scale robustness.}\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex-169-With Qwen3-4B (Table~\\ref{tab:scale_ablation}), QE is comparable (mean $|\\Delta\\rho|{=}0.042$), yet selection remains below greedy despite 13.0~pp headroom. Task difficulty is a stronger predictor than model scale within the 3B--8B range (Appendix~\\ref{app:llama3b}).\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex:170:Degeneracy scales with capability: 8B shows 17.8\\% vs.\\ 4B's 10.4\\% on SciERC (Table~\\ref{tab:degeneracy}).\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex-171-\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex-172-\\paragraph{LoRA-rank ablation.}\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex:173:LoRA rank${=}8$ (vs.\\ 32) lowers degeneracy to 7.2\\% but LP remains below greedy ($\\rho(\\text{LP}, \\text{F1}){\\approx}0.24$); temperature manipulation ($T{=}1.2$; \\S\\ref{sec:discussion}) confirms that low degeneracy and adequate alignment are independently necessary.\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex-174-\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex-175-\\paragraph{Supervised signal combination and hidden probes.}\n--\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex-204-Structural signals remain positive but reduced (VC $\\rho{=}0.277$ on SciERC, SJ $\\rho{=}0.304$ on CoNLL). LP-weighted construction partially compensates on SciERC ($+1.5$\\,pp, 41.4\\% vs.\\ 39.9\\% greedy) but not on CoNLL ($-0.37$\\,pp), where limited headroom (5.3~pp) leaves little room for aggregation.\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex-205-\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex:206:\\textcolor{red}{TODO: (1) Add 72B fine-tuned results to determine whether fine-tuning at larger scale recovers signal quality. (2) Report degeneracy percentages for 72B zero-shot.}\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex-207-\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex-208-\\begin{figure}[t]\n--\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex-244-\\end{table}\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex-245-\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex:246:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex-247-\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex-248-\\paragraph{LP-alignment gating (preliminary diagnostic).}\n--\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/conclusion.tex-1-\\section{Conclusion}\\label{sec:conclusion}\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/conclusion.tex-2-\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/conclusion.tex:3:[Omitted long matching line]\n--\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex-2-\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex-3-The decoupling of $\\rho$, AUROC, and selection F1 means single-metric evaluation risks selecting the wrong signal; effective selection likely requires content-aware verifiers \\cite{cobbe2021verifiers, venktesh2025trust}.\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex:4:Three factors qualitatively constrain selection: instance degeneracy (17.8--67.9\\%) compresses the candidate space, limited oracle headroom bounds achievable gains, and LP compression (within-instance $\\rho$ 0.043--0.667) prevents exploiting the remainder; within non-degenerate instances, MBR utility correlates positively with F1 (SJ median $\\rho{=}0.524$) \\cite{eikema2022sampling}.\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex-5-Where compression is mitigated (LP range ${\\geq}0.05$, $n{=}210$), LP selection yields $+2.9$~pp ($p{=}0.004$; Table~\\ref{tab:nontied_main}), but $\\varepsilon{=}0.05$ is post-hoc ($p_{\\text{adj}}{=}0.14$ after joint correction; Appendix~\\ref{app:epsilon_robustness}), so this is exploratory evidence.\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex:6:Temperature disentangles degeneracy from alignment: at $T{=}1.2$, degeneracy drops to 14.9\\% yet LP does not improve (median $\\rho{=}0.225$; Table~\\ref{tab:t_degeneracy}); the selection window narrows as models improve \\cite{wang2023selfconsistency, snell2025scaling}.\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex-7-\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex-8-\\paragraph{From diagnosis to practice.}\\label{sec:selection_method}\n--\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex-59-Best-of-$N$ F1: per-sample signals (LP) directly rank candidates; instance-level signals rank via consensus-proximity (MBR utility; see SJ definition above).\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex-60-Baselines: \\textit{oracle} (highest-F1 sample) and \\textit{greedy} ($T{=}0$ argmax decoding).\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex:61:We define \\textbf{instance degeneracy} as the fraction of instances where all $N$ samples yield identical F1;\\footnote{``Identical F1'' means constant F1 across all $N$ samples for a given instance, not necessarily F1${=}1.0$. Samples may differ in surface form but produce the same entity set and thus the same score.} for these instances, no signal can improve selection.\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex-62-We report F1 under the protocol matching each experiment's configuration (seed, epoch, $N$). SciERC greedy F1 appears as four values across tables (0.640, 0.644, 0.645, 0.650) due to protocol variants: primary seed vs.\\ multi-seed mean, 5-epoch vs.\\ 3-epoch checkpoint, and gold-filtered vs.\\ full test set. Each table specifies its protocol.\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex-63-\n--\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex-2-All experiments use English-language datasets; cross-lingual generalization remains untested.\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex-3-Entity-level construction assumes the model produces useful partial outputs across samples; when model capability is insufficient (WNUT-17, 51\\% F1${=}0$), this precondition fails and construction cannot improve over greedy.\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex:4:We cover 4B\\textendash 8B scale; whether the gap holds for 70B+ models or closed-source APIs is untested. Larger models may produce more diverse samples (potentially reducing degeneracy), but their LP-quality alignment behavior is unknown, and these two factors may shift in opposite directions.\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex-5-Our supervised approaches (DeBERTa verifier, hidden state probes, MLP/RF on signal combinations) all fail to close the oracle gap; whether content-aware verifiers with access to task-specific structure could succeed remains open.\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex-6-\n--\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex-4-All signals achieve reliable QE ($\\rho$ up to 0.45 on CoNLL-2003, area under the ROC curve [AUROC] up to 0.82), enabling selective prediction ($+5$--$8$\\,pp F1 at 80\\% coverage).\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex-5-For instance-level selection, log-probability (LP) succeeds only where LP-quality alignment is strong, and gains are absent elsewhere despite large oracle headroom (the \\textbf{correlation-selection gap}).\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex:6:We identify three qualitative factors: instance degeneracy, oracle headroom, and LP-quality alignment; degeneracy causally modulates LP within fixed settings but does not predict cross-dataset direction.\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex-7-The diagnostic naturally motivates entity-level \\textit{construction}, adapting entity voting to stochastic sampling: LP-weighted aggregation improves F1 by $+1.40$\\,pp on Few-NERD and $+1.02$\\,pp on SciERC (multi-seed mean, $p{<}0.005$). Construction and LP selection are complementary, governed by LP-quality alignment.\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex-8-\\end{abstract}\n--\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex-229-Table~\\ref{tab:cross_selection} extends the selection analysis to five additional configurations.\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex-230-On LLaMA SciERC, where output diversity remains substantial (18\\% identical outputs, 39\\% unique), LP achieves the highest selection F1 (0.652) at $N{=}8$ but still falls within bootstrap noise of single-sample (0.646), replicating the gap observed on Qwen SciERC (Table~\\ref{tab:selection}).\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:231:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex-232-On CoNLL, 48--87\\% of instances produce identical outputs across all $N$ samples; this reflects a ceiling effect (single-sample F1 ${\\approx}$0.91--0.92) rather than signal failure, and selection analysis on these configurations is uninformative because there is little per-sample variance for any signal to exploit.\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex-233-\n--\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex-348-This rules out insufficient diversity as an explanation for the correlation-selection gap.\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex-349-\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:350:\\paragraph{Instance degeneracy statistics.}\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:351:Table~\\ref{tab:degeneracy} quantifies instance degeneracy across configurations. ``Constant F1'' denotes instances where all $N$ samples receive identical instance-level F1; ``Constant utility'' denotes instances where MBR (SJ) utility is identical across candidates, preventing ranking.\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex-352-\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex-353-\\begin{table}[t]\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex-354-\\centering\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex-355-\\small\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:356:\\caption{Instance degeneracy statistics ($T{=}1.0$). ``Constant F1'': all $N$ samples receive identical instance-level F1. ``Constant utility'': MBR (SJ) utility identical across candidates. 4B data confirms degeneracy scales with model capability.}\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:357:\\label{tab:degeneracy}\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex-358-\\begin{tabular}{lccc}\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex-359-\\toprule\n--\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex-422-(a)~Models with poor calibration or in-context learning setups (without fine-tuning) produce more diverse outputs, widening the gap between candidates that consistency signals can exploit.\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex-423-(b)~Closed-source APIs where log-probabilities are unavailable make consistency signals the only viable selection mechanism; our structural signals (SJ, VC, FK, EM) provide quality estimation ($\\rho$ up to 0.45) even without model-internal access.\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:424:(c)~Ensemble or mixture-of-experts settings generate structurally diverse candidates by design, reducing instance degeneracy below the levels observed in our single-model sampling.\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex-425-(d)~Tasks where the model exhibits systematic overconfidence (e.g., hallucination-prone generation) may benefit from consensus filtering, as disagreement among samples would carry more discriminative signal than in our well-calibrated fine-tuned regime.\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex-426-\n--\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex-683-\\paragraph{Within-instance LP-quality alignment.}\\label{app:within_instance_rho}\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex-684-\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:685:Table~\\ref{tab:within_rho} reports median within-instance $\\rho(\\text{LP}, \\text{F1})$ across datasets, computed over non-degenerate instances (those with ${\\geq}2$ distinct F1 values across $N{=}8$ samples).\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex-686-Few-NERD exhibits substantially stronger alignment ($\\rho{=}0.667$) than SciERC ($\\rho{=}0.262$), directly explaining why LP selection succeeds only on Few-NERD.\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:687:CoNLL alignment is moderate ($\\rho{\\approx}0.51$), but the valid-instance fraction is low (41\\% for Qwen, 11\\% for LLaMA) because degeneracy eliminates most headroom before alignment can operate.\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:688:LP-quality alignment is the primary predictor of selection direction; degeneracy constrains headroom but does not independently predict whether LP selection gains materialize (\\S\\ref{sec:discussion}).\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex-689-\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex-690-\\begin{table}[h]\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex-691-\\centering\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex-692-\\small\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:693:\\caption{Within-instance LP-quality alignment across datasets ($N{=}8$, $T{=}1.0$). $\\rho$: median Spearman correlation between LP and F1 within each instance, over non-degenerate instances ($n_{\\text{valid}}$: ${\\geq}2$ distinct F1 values).}\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex-694-\\label{tab:within_rho}\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex-695-\\resizebox{\\columnwidth}{!}{%\n--\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex-828-\\paragraph{Connection to MBR decoding.}\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex-829-Our selection strategies instantiate minimum Bayes risk (MBR) decoding \\cite{eikema2022sampling, muller2021understanding}: each selects $\\hat{y} = \\arg\\max_{y_i} \\sum_{j \\neq i} U(y_i, y_j)$ with utility $U$ defined by SJ, EM, or entity overlap.\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:830:Despite MBR's success in machine translation \\cite{freitag2022high} and its extension to summarization, code generation, and captioning \\cite{jinnai2024mbr}, all variants fail here: despite positive within-instance utility--F1 correlation, selection gains are limited by instance degeneracy, the core of the correlation-selection gap.\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex-831-\\citet{eikema2025structured} study structure-conditional MBR decoding and find that standard utility functions degrade on structured outputs, consistent with our finding that consensus-proximity selection fails in IE despite its success in machine translation.\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex-832-\n--\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex-1036-\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex-1037-\\paragraph{$N$-scaling: selection headroom vs.\\ selection gain.}\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:1038:Table~\\ref{tab:n_scaling_selection} traces the effect of sample count on degeneracy, oracle headroom, and per-signal selection gain.\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex-1039-Oracle headroom grows roughly linearly with $N$ ($+4.4$~pp at $N{=}2$ to $+20.0$~pp at $N{=}32$).\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:1040:LP selection improves monotonically with $N$ ($+0.39$~pp at $N{=}8$ to $+0.95$~pp at $N{=}32$), but even at $N{=}32$, where degeneracy falls to 4\\% and oracle headroom reaches ${\\sim}20$~pp, the best signal captures less than 5\\% of the available improvement.\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:1041:Degeneracy drops monotonically (43\\% at $N{=}2$ to 4\\% at $N{=}32$), yet reduced degeneracy does not unlock selection, consistent with the LoRA-rank ablation finding (\\S\\ref{sec:robustness_main}).\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex-1042-VC selection degrades with increasing $N$ ($-2.66$~pp at $N{=}2$ to $-4.35$~pp at $N{=}32$), consistent with mode-seeking bias in voting-based selection as the candidate pool grows.\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex-1043-\n--\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex-1115-The $T{=}0.7$ and $T{=}1.0$ comparison in Table~\\ref{tab:robustness} is consistent with the trends reported here.\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex-1116-\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:1117:\\paragraph{Temperature controls degeneracy and LP spread.}\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:1118:Table~\\ref{tab:t_degeneracy} reports instance degeneracy (constant F1, gold-filtered) and median within-instance LP range across four temperatures on SciERC.\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:1119:Both quantities are strictly monotonic in $T$: degeneracy falls from 41.4\\% ($T{=}0.5$) to 14.9\\% ($T{=}1.2$), while LP range increases from 0.015 to 0.058 nats.\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:1120:Temperature thus provides a direct lever for practitioners to shift the degeneracy regime.\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:1121:However, even at $T{=}1.2$ where degeneracy (14.9\\%) approaches Few-NERD levels (${\\sim}$14\\%), within-instance $\\rho(\\text{LP}, \\text{F1})$ remains at 0.225, far below Few-NERD's ${\\sim}$0.5.\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:1122:This confirms that temperature controls degeneracy but cannot improve LP-quality alignment, which is largely determined by task structure and remains relatively stable across generation configurations (\\S\\ref{app:epoch_confound}). LP-quality alignment, not degeneracy, is the primary predictor of LP selection direction (\\S\\ref{sec:discussion}).\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex-1123-\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex-1124-\\begin{table}[h]\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex-1125-\\centering\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex-1126-\\small\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:1127:\\caption{Temperature sensitivity of degeneracy and LP spread (SciERC NER, Qwen3-8B, $N{=}8$). Degeneracy: constant-F1, gold-filtered. LP range: median within-instance range.}\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:1128:\\label{tab:t_degeneracy}\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex-1129-\\begin{tabular}{ccccc}\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex-1130-\\toprule\n--\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex-1246-Table~\\ref{tab:fewnerd_full} reports the complete Few-NERD INTRA coarse evaluation (Qwen3-8B, LoRA rank${=}32$, 3 epochs, $N{=}8$, $T{=}1.0$).\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex-1247-After gold-filtering (removing instances with no gold entities), the evaluation set contains $n{=}32{,}565$ instances across 8 coarse entity types; 11.9\\% receive zero F1 under greedy decoding.\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:1248:Instance degeneracy is 13.8\\% (vs.\\ 17.8\\% on SciERC, 48.4\\% on CoNLL).\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex-1249-\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex-1250-\\begin{table}[t]\n--\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex-1272-(2)~LP is the only signal achieving significant positive selection ($+1.39$~pp, $p{<}0.001$, CI excludes zero). The sample-level AUROC of 0.578 confirms LP provides per-sample discriminability beyond instance-level quality prediction.\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex-1273-(3)~Despite positive $\\rho$, all structural signals degrade selection ($-1.79$ to $-3.85$~pp), further confirming that the correlation-selection gap is not an artifact of weak QE.\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:1274:(4)~Low degeneracy (13.8\\%) combined with strong LP-quality alignment ($\\rho{\\approx}0.5$--$0.7$) enables LP selection: candidates differ in F1 more often, and LP can rank them effectively. This contrasts with SciERC (17.8\\% degeneracy but weak alignment $\\rho{\\approx}0.24$, LP $+0.61$~pp) and CoNLL (48.4\\%, LP $-0.85$~pp).\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex-1275-\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex-1276-\\section{Per-Entity-Type LP Selection Analysis}\\label{app:per_type_lp}\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex-1277-\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:1278:Table~\\ref{tab:per_type_lp} stratifies LP selection by entity type on Few-NERD, sorted by degeneracy rate.\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:1279:The degeneracy-gating mechanism holds at entity-type granularity: 7 of 8 types show positive LP selection gains, and the sole negative type (Art, $-0.17$~pp) has the highest degeneracy (19.8\\%).\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:1280:The correlation between per-type degeneracy and oracle headroom is strong and significant (Spearman $\\rho{=}{-}0.881$, $p{=}0.004$; exact permutation $p{=}0.005$); degeneracy directly constrains the headroom available for selection.\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex-1281-Under a conservative $\\text{df}{=}4$ adjustment for within-type dependence, the correlation remains significant ($p{=}0.033$).\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex-1282-Entity types show near-zero intra-class correlation (ICC $= -0.004$), supporting the independence assumption underlying per-type analysis.\n--\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex-1285-\\centering\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex-1286-\\small\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:1287:\\caption{Per-entity-type LP selection on Few-NERD INTRA coarse (Qwen3-8B, $N{=}8$, $T{=}1.0$), sorted by degeneracy. LP $\\Delta$: LP selection F1 minus greedy. 7/8 types show positive $\\Delta$; Art (highest degeneracy) is the sole exception.}\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex-1288-\\label{tab:per_type_lp}\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex-1289-\\begin{tabular}{lrrrrrrr}\n--\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex-1306-\\centering\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex-1307-\\small\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:1308:\\caption{CoNLL-2003 per-type LP selection (Qwen3-8B, $N{=}16$, $T{=}1.0$). All types exceed 20\\% degeneracy and show negative LP selection, consistent with the dataset's ceiling-regime performance (F1 $>$ 90\\%).}\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex-1309-\\label{tab:per_type_lp_conll}\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex-1310-\\begin{tabular}{lrrr}\n--\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex-1323-\\centering\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex-1324-\\small\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:1325:\\caption{SciERC per-type LP selection (Qwen3-8B, $N{=}8$, $T{=}1.0$). Within-dataset, degeneracy alone does not predict LP effectiveness (Spearman $\\rho{=}0.14$, $p{=}0.79$); additional type-specific factors likely modulate selection at this granularity.}\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex-1326-\\label{tab:per_type_lp_scierc}\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex-1327-\\begin{tabular}{lrrr}\n--",
    "numLines": 250,
    "appliedLimit": 250
  },
  "sourceToolAssistantUUID": "2fae23d2-b5a0-47cd-83c7-cfefc7eb209b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "a6ae7e35-390a-442a-93d4-9958c82c9e3b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 41 · 2026-05-19T13:56:19.186Z_

<details><summary>↩ Tool result · `toolu_01K5qF2doGHQuKoUzMtGrcVw`</summary>

```text
&lt;persisted-output>
Output too large (78.5KB). Full output saved to: /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-reviewer-0064dd56/a6ae7e35-390a-442a-93d4-9958c82c9e3b/tool-results/toolu_01K5qF2doGHQuKoUzMtGrcVw.txt

Preview (first 2KB):
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.fls:324:INPUT ./figures/fig_degeneracy_lp_scatter.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.fls:325:INPUT ./figures/fig_degeneracy_lp_scatter.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.fls:326:INPUT ./figures/fig_degeneracy_lp_scatter.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.fls:327:INPUT ./figures/fig_degeneracy_lp_scatter.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.fls:328:INPUT ./figures/fig_degeneracy_lp_scatter.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex:7:All target discrete-answer reasoning; structured prediction requires different gating signals because degeneracy operates at the entity-set level.
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex:10:\citet{yao2026consistency} show consistency correlates with accuracy for LLM-based NER/RE; we show correlation alone does not ensure selection gains, diagnosing degeneracy and compression as blocking mechanisms.
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex:21:Our selection strategies instantiate MBR decoding \cite{eikema2022sampling, deguchi2024centroid}; unlike MT where MBR yields consistent gains \cite{freitag2022high} and code generation where execution-based MBR improves selection \cite{shi2022mbr}, instance degeneracy eliminates the headroom MBR needs even when utility is well-aligned ($\rho{=}0.52$; \S\ref{sec:discussion}).
...
&lt;/persisted-output>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "86d8657a-d9ed-407b-9d00-16dc11baeb83",
  "isSidechain": false,
  "promptId": "2279f609-b135-4e34-8568-a1f529688be0",
  "type": "user",
  "uuid": "a9973ca9-06cd-4bb8-ae38-3d7eed32574d",
  "toolUseResult": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.fls:324:INPUT ./figures/fig_degeneracy_lp_scatter.pdf\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.fls:325:INPUT ./figures/fig_degeneracy_lp_scatter.pdf\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.fls:326:INPUT ./figures/fig_degeneracy_lp_scatter.pdf\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.fls:327:INPUT ./figures/fig_degeneracy_lp_scatter.pdf\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.fls:328:INPUT ./figures/fig_degeneracy_lp_scatter.pdf\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex:7:All target discrete-answer reasoning; structured prediction requires different gating signals because degeneracy operates at the entity-set level.\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex:10:\\citet{yao2026consistency} show consistency correlates with accuracy for LLM-based NER/RE; we show correlation alone does not ensure selection gains, diagnosing degeneracy and compression as blocking mechanisms.\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex:21:Our selection strategies instantiate MBR decoding \\cite{eikema2022sampling, deguchi2024centroid}; unlike MT where MBR yields consistent gains \\cite{freitag2022high} and code generation where execution-based MBR improves selection \\cite{shi2022mbr}, instance degeneracy eliminates the headroom MBR needs even when utility is well-aligned ($\\rho{=}0.52$; \\S\\ref{sec:discussion}).\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex:22:\\citet{eikema2025structured} find MBR utilities degrade on structured outputs; our diagnosis is complementary: degeneracy, not utility misalignment, is the primary bottleneck.\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex:10:\\textbf{Few-NERD} \\cite{ding2021fewnerd} (INTRA coarse; 37{,}648 instances, 8 entity types, ${\\approx}$75\\% F1) provides a low-degeneracy contrast where LP selection succeeds (\\S\\ref{sec:fewnerd}).\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex:16:We draw $N{=}8$ samples at $T{=}1.0$ (primary) with vLLM constrained decoding \\cite{willard2023guided}, with $N{=}16$ for scaling experiments (Appendix~\\ref{app:n_scaling}).\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex:25:\\caption{NER quality estimation ($\\rho$ and AUROC; $N{=}8$, primary seed${=}42$; 3-seed stability $\\sigma{\\leq}0.026$ in Table~\\ref{tab:multiseed}). Best in \\textbf{bold}. RE results in Appendix~\\ref{app:re_extension}. $N{=}16$ in Table~\\ref{tab:robustness}.}\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex:57:LP selection effectiveness is primarily determined by LP-quality alignment rather than degeneracy level (\\S\\ref{sec:discussion}).\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex:63:\\caption{Best-of-$N$ NER selection (macro F1) on SciERC ($N{=}8$, $T{=}1.0$, 2-seed mean${\\pm}\\sigma$). LP is per-sample; others use consensus-proximity. Best non-oracle in \\textbf{bold}. Non-tied subset in \\S\\ref{sec:discussion}; RE in Appendix~\\ref{app:re_extension}. $^\\dagger$Instance-level signals assign one score per input; per-sample ranking $p$-values are undefined.}\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex:89:\\caption{The correlation-selection gap on SciERC ($N{=}8$, $T{=}1.0$). Bars: quality estimation $\\rho$ (seed 42); line with error bars: $\\Delta$F1 vs.\\ greedy (3-seed mean, seeds 42/123/456). Despite $\\rho$ up to 0.38, no signal significantly outperforms greedy (all $p{>}0.05$; Table~\\ref{tab:selection}). Dashed green: oracle upper bound ($+13.1$~pp); dotted gray: random baseline.}\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex:99:Few-NERD provides the definitive contrast: LP achieves $+1.39$~pp ($p{<}0.001$) at low degeneracy (\\S\\ref{sec:fewnerd}), while structural signals still degrade selection.\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex:102:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex:103:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex:114:\\caption{LP selection across datasets (Qwen3-8B, $N{=}8$, $T{=}1.0$, gold-filtered). Few-NERD/CoNLL: 3-seed means; SciERC: single-seed (3-seed in Table~\\ref{tab:multiseed}). $p$: paired bootstrap.}\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex:119:Dataset & $n$ & Greedy & Degen.\\% & LP $\\rho$ & LP $\\Delta$ & $p$ \\\\\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex:129:Few-NERD (Table~\\ref{tab:fewnerd}) confirms LP selection at low degeneracy: $+1.39$~pp ($p{<}0.001$), while structural signals degrade selection (VC $-1.79$, SJ $-2.14$~pp). LP is 50$\\times$ more seed-stable ($\\sigma{=}0.04$ vs.\\ SJ $2.02$~pp) and generalizes to LLaMA-3.1-8B (Table~\\ref{tab:cross_selection}).\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex:130:Training convergence modulates degeneracy: 5-epoch Few-NERD raises degeneracy to 31\\% and halves LP gains (Appendix~\\ref{app:epoch_confound}).\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex:132:\\paragraph{Degeneracy alone does not predict LP selection direction.}\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex:133:Across 23 configurations, degeneracy does not predict LP gain ($\\rho{=}0.052$, $p{=}0.81$; Figure~\\ref{fig:degeneracy_scatter}), though within fixed settings it causally modulates LP ($\\rho{=}{-}0.881$; Appendix~\\ref{app:per_type_lp}).\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex:138:\\includegraphics[width=\\columnwidth]{figures/fig_degeneracy_lp_scatter.pdf}\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex:139:\\caption{Instance degeneracy vs.\\ LP selection gain across 23 configurations ($N{=}8$; $\\rho{=}0.052$, $p{=}0.81$). Within Few-NERD per-entity-type analysis ($\\rho{=}{-}0.881$; Appendix~\\ref{app:per_type_lp}), degeneracy predicts LP gain when alignment is held constant.}\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex:140:\\label{fig:degeneracy_scatter}\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex:154:\\caption{Scale ablation: 8B vs.\\ 4B QE $\\rho$ ($N{=}8$, $T{=}1.0$, seed 42). RE in Appendix~\\ref{app:re_extension}.}\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex:170:Degeneracy scales with capability: 8B shows 17.8\\% vs.\\ 4B's 10.4\\% on SciERC (Table~\\ref{tab:degeneracy}).\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex:173:LoRA rank${=}8$ (vs.\\ 32) lowers degeneracy to 7.2\\% but LP remains below greedy ($\\rho(\\text{LP}, \\text{F1}){\\approx}0.24$); temperature manipulation ($T{=}1.2$; \\S\\ref{sec:discussion}) confirms that low degeneracy and adequate alignment are independently necessary.\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex:176:Supervised classifiers (LR, MLP, RF; 5-fold CV, $N{=}16$) and a DeBERTa-v3-base verifier all fail to close the selection gap (Appendix~\\ref{app:supervised_combination}).\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex:188:\\caption{Fine-tuned 8B vs.\\ zero-shot 72B ($N{=}8$, $T{=}1.0$). Hdr.\\ = oracle $-$ greedy (pp).}\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex:206:\\textcolor{red}{TODO: (1) Add 72B fine-tuned results to determine whether fine-tuning at larger scale recovers signal quality. (2) Report degeneracy percentages for 72B zero-shot.}\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex:228:\\caption{Entity construction vs.\\ greedy ($\\Delta$ macro F1; $N{=}8$, $T{=}1.0$, Qwen3-8B, multi-seed mean${\\pm}\\sigma$). $\\theta{=}2/N$. $p$: paired bootstrap vs.\\ greedy. Best in \\textbf{bold}.}\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex:246:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex:250:We estimate within-instance $\\rho(\\text{LP}, \\text{F1})$ on 50 held-out instances with bootstrap CIs (1000 resamples). Degeneracy-adjusted $\\rho_{\\text{adj}}$: Few-NERD $0.516$ [0.459, 0.759], SciERC $0.167$ [0.146, 0.281], CoNLL $0.065$ [$-$0.061, 0.620], WNUT-17 ${\\approx}0$ (n.s.).\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/conclusion.tex:3:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/checklist.tex:48:Partially. Model sizes (4B, 8B parameters) are stated in Section~\\ref{sec:introduction}. LoRA configuration and training hyperparameters are in Appendix~\\ref{app:training}. Computing infrastructure: 4$\\times$ NVIDIA RTX 5090 GPUs. We do not report total GPU hours; each model fine-tunes in under 2 hours and inference for $N{=}8$ samples across all test sets completes in under 1 hour per configuration.\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex:4:Three factors qualitatively constrain selection: instance degeneracy (17.8--67.9\\%) compresses the candidate space, limited oracle headroom bounds achievable gains, and LP compression (within-instance $\\rho$ 0.043--0.667) prevents exploiting the remainder; within non-degenerate instances, MBR utility correlates positively with F1 (SJ median $\\rho{=}0.524$) \\cite{eikema2022sampling}.\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex:6:Temperature disentangles degeneracy from alignment: at $T{=}1.2$, degeneracy drops to 14.9\\% yet LP does not improve (median $\\rho{=}0.225$; Table~\\ref{tab:t_degeneracy}); the selection window narrows as models improve \\cite{wang2023selfconsistency, snell2025scaling}.\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex:61:We define \\textbf{instance degeneracy} as the fraction of instances where all $N$ samples yield identical F1;\\footnote{``Identical F1'' means constant F1 across all $N$ samples for a given instance, not necessarily F1${=}1.0$. Samples may differ in surface form but produce the same entity set and thus the same score.} for these instances, no signal can improve selection.\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex:4:We cover 4B\\textendash 8B scale; whether the gap holds for 70B+ models or closed-source APIs is untested. Larger models may produce more diverse samples (potentially reducing degeneracy), but their LP-quality alignment behavior is unknown, and these two factors may shift in opposite directions.\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex:7:We evaluate at $N{=}8$ (primary) and $N{=}16$; behavior at larger sample sizes is unknown (Appendix~\\ref{app:n_scaling}).\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex:6:We identify three qualitative factors: instance degeneracy, oracle headroom, and LP-quality alignment; degeneracy causally modulates LP within fixed settings but does not predict cross-dataset direction.\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.bbl:228:  of neural text degeneration}.\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:37:\\caption{Signal robustness across configurations (Spearman $\\rho$). Top: temperature on Qwen SciERC. Middle: sample size on Qwen SciERC. Bottom: transfer across model families (both 8B) (LLaMA CoNLL $N{=}16$, 3-seed mean $\\pm\\sigma$). $^\\dagger$Mean over 3 seeds ($\\sigma{=}0.013$; individual: 0.398, 0.423, 0.410). $\\sigma$ computed as sample standard deviation.}\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:43:\\multicolumn{4}{l}{\\textit{Temperature} (Qwen SciERC, $N{=}8$)} \\\\\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:52:\\quad SJ & $N{=}8$  & 0.360 & 0.250 \\\\\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:53:\\quad SJ & $N{=}16$ & 0.411$^\\dagger$ & 0.281 \\\\\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:54:\\quad FK & $N{=}8$  & 0.267 & 0.275 \\\\\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:55:\\quad FK & $N{=}16$ & 0.283 & 0.279 \\\\\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:57:\\multicolumn{4}{l}{\\textit{Across model families} (LLaMA CoNLL, $N{=}16$, 3 seeds)} \\\\\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:70:\\caption{Temperature robustness on SciERC ($N{=}8$). Top: NER; bottom: RE. SJ maintains stable $\\rho$ across $T{=}0.7$ and $T{=}1.0$, while FK shows mixed sensitivity. LP shows the largest NER temperature effect ($\\Delta\\rho{=}{+}0.044$); RE $T{=}0.7$ LP data unavailable.}\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:81:Increasing from $N{=}8$ to $N{=}16$ improves SJ on Qwen SciERC NER: $\\rho$ rises from 0.360 to $0.411{\\pm}0.010$ (three seeds: 0.398, 0.423, 0.410), a gain of $+0.047$.\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:87:At $N{=}16$, SJ converges to comparable NER performance with VC ($\\Delta{=}0.002$) while exhibiting lower cross-seed variance ($\\sigma{=}0.010$ vs.\\ $0.026$), a more stable alternative at higher sample sizes.\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:92:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:125:\\caption{Reliability diagrams on SciERC ($N{=}8$, $T{=}1.0$). Top: mean F1 vs.\\ binned confidence; bottom: instance counts per bin. Left: NER; right: RE. NER signals are reasonably well-calibrated (calibration ECE 0.069--0.096), while RE shows greater miscalibration (ECE 0.109--0.339), RE calibration remains challenging for compound extraction tasks.}\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:153:On the high-complexity RE subset ($n{=}81$, high relation count), signals improve substantially: VC reaches $\\rho{=}0.630$, LP $\\rho{=}0.554$, and SJ $\\rho{=}0.502$, all far above the full-set levels.\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:162:\\caption{Output length vs.\\ mean log-probability on SciERC ($N{=}8$, $T{=}1.0$). Positive correlations (NER: $\\rho{=}0.386$; RE: $\\rho{=}0.326$) rule out length-penalty confounding.}\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:176:Table~\\ref{tab:sj_normalizer} compares the two normalizers across all six model--dataset combinations ($N{=}8$, $T{=}1.0$, seed${=}42$): $|\\Delta\\rho|{<}0.01$ in every case, the choice between max and union normalization does not affect conclusions.\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:181:\\caption{SJ normalizer comparison (Spearman $\\rho$; $N{=}8$, $T{=}1.0$, seed${=}42$). Max: $\\max(|g_i|,|g_j|)$; Union: $|g_i \\cup g_j|$.}\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:199:At $N{=}16$, the divergence persists: SJ maintains $\\rho{=}0.308$ on conditional RE while LP drops to $\\rho{=}{-}0.026$.\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:200:EM ranks first across all four tested conditional configurations: SciERC NER ($\\rho{=}0.360$), CoNLL Qwen $N{=}16$ ($\\rho{=}0.466$), CoNLL LLaMA 3-seed ($\\rho{=}0.462$), and SciERC RE ($\\rho{=}0.417$). This holds despite full-set rankings ranging from \\#1 (CoNLL Qwen) to \\#5 (SciERC RE).\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:211:\\caption{Quality estimation on WNUT-17 (Qwen, $N{=}16$, $T{=}1.0$, $n{=}689$). Cond: non-zero F1 instances ($n{=}334$). Full-set $\\rho$ reflects binary success prediction; conditional $\\rho$ measures quality gradation. LP's conditional $\\rho$ is highest despite negative full-set $\\rho$.}\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:230:On LLaMA SciERC, where output diversity remains substantial (18\\% identical outputs, 39\\% unique), LP achieves the highest selection F1 (0.652) at $N{=}8$ but still falls within bootstrap noise of single-sample (0.646), replicating the gap observed on Qwen SciERC (Table~\\ref{tab:selection}).\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:231:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:237:\\caption{Best-of-$N$ selection F1 (macro, instance-averaged) across configurations ($T{=}1.0$, 3-seed mean). Best non-oracle signal per row in \\textbf{bold}. LP is the only signal with positive selection on both FewNERD configurations (Qwen $+1.39$~pp, Table~\\ref{tab:fewnerd}; LLaMA $+0.36$~pp). At $N{=}16$ on LLaMA CoNLL, VC achieves small but significant gains ($+0.28$~pp, $p{<}0.03$; see text below). CoNLL shows especially tight clustering where greedy already exceeds 0.90.}\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:243:LLaMA/SciERC $N{=}8$ & 529 & .646 & .778 & .643 & .639 & .634 & \\textbf{.652} & .633 \\\\\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:244:LLaMA/SciERC $N{=}16$ & 529 & .645 & .806 & \\textbf{.649} & \\textbf{.649} & .640 & .646 & .640 \\\\\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:246:LLaMA/FewNERD $N{=}8$ & 32{,}565 & .784 & .884 & .779 & .779 & .774 & \\textbf{.788} & .760 \\\\\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:248:Qwen/CoNLL $N{=}8$ & 2{,}756 & .908 & .957 & \\textbf{.899} & .893 & .898 & .897 & .895 \\\\\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:249:LLaMA/CoNLL $N{=}8$ & 2{,}756 & .924 & .943 & .924 & \\textbf{.925} & .924 & .924 & .923 \\\\\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:255:Our $N{=}8$ and $N{=}16$ comparisons (Table~\\ref{tab:robustness}) characterize the marginal value of additional samples for test-time scaling \\cite{brown2024monkeys, snell2025scaling}.\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:256:For quality estimation, structural signals benefit consistently but sublinearly: SJ $\\rho$ improves by $+0.047$ (Qwen SciERC, 3-seed mean) and $+0.032$ (LLaMA CoNLL, 3-seed mean) when doubling from $N{=}8$ to $N{=}16$, while log-probability is approximately $N$-invariant ($\\Delta\\rho{\\leq}0.021$).\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:257:Structural signals use $\\binom{N}{2}$ pairwise comparisons (28 pairs at $N{=}8$, 120 at $N{=}16$), but the $\\rho$ improvement is far less than proportional, each additional comparison yields diminishing information.\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:258:This asymmetry gives structural signals a relative advantage in the compute-constrained regime: at $N{=}8$, SJ already achieves $\\rho{=}0.431$ on LLaMA CoNLL (vs.\\ LP $\\rho{=}0.307$, $\\Delta{=}{+}0.124$), and the gap \\textit{widens} at $N{=}16$ ($\\Delta{=}{+}0.163$) because structural signals continue to benefit from additional pairwise evidence while LP does not.\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:260:The practical implication is that $N{=}8$ captures most of the achievable quality estimation benefit; further scaling widens rather than closes the correlation-selection gap absent stronger per-sample selectors.\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:262:\\paragraph{$N{=}16$ CoNLL selection: small but significant.}\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:263:While quality estimation benefits sublinearly from $N$-scaling, selection behavior at $N{=}16$ reveals a nuanced exception on LLaMA CoNLL.\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:265:These gains are statistically significant but practically minimal: oracle headroom at $N{=}16$ is only 2.5~pp, so VC captures approximately 10\\% of the available headroom.\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:270:Table~\\ref{tab:bootstrap_signal_ci} reports bootstrap confidence intervals for individual signal $\\rho$ and pairwise $\\Delta\\rho$ on SciERC NER ($N{=}8$, $n{=}529$, $B{=}10{,}000$, seed${=}42$).\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:278:\\caption{Bootstrap 95\\% CIs for signal $\\rho$ on SciERC NER ($N{=}8$, $n{=}529$, $B{=}10{,}000$, seed${=}42$). Top: individual signals. Bottom: pairwise $\\Delta\\rho$; ``Sig.'' indicates whether the 95\\% CI excludes zero.}\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:308:At $N{=}16$ ($B{=}10{,}000$, permutation test), the structural advantage extends to FK comparisons.\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:318:On SciERC, output diversity is substantial: Qwen produces 43\\% unique outputs per instance (mean 3.5 distinct out of $N{=}8$), with per-sample F1 standard deviation of 0.144 and mean pairwise SJ of 0.703.\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:326:\\caption{Output diversity across configurations ($N{=}8$, $T{=}1.0$). ``Identical'' = fraction of instances with all $N$ outputs identical. ``Unique'' = mean fraction of distinct outputs per instance.}\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:350:\\paragraph{Instance degeneracy statistics.}\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:351:Table~\\ref{tab:degeneracy} quantifies instance degeneracy across configurations. ``Constant F1'' denotes instances where all $N$ samples receive identical instance-level F1; ``Constant utility'' denotes instances where MBR (SJ) utility is identical across candidates, preventing ranking.\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:356:\\caption{Instance degeneracy statistics ($T{=}1.0$). ``Constant F1'': all $N$ samples receive identical instance-level F1. ``Constant utility'': MBR (SJ) utility identical across candidates. 4B data confirms degeneracy scales with model capability.}\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:357:\\label{tab:degeneracy}\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:360:& \\shortstack{SciERC 8B\\\\($N{=}8$)} & \\shortstack{SciERC 4B\\\\($N{=}8$)} & \\shortstack{CoNLL 8B\\\\($N{=}16$)} \\\\\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:384:\\caption{TOST equivalence testing: signals vs.\\ single-sample on SciERC ($N{=}8$, $T{=}1.0$). \\checkmark: equivalent at $p{<}0.05$; \\texttimes: not equivalent. $\\Delta$: mean F1 difference (signal $-$ single-sample).}\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:424:(c)~Ensemble or mixture-of-experts settings generate structurally diverse candidates by design, reducing instance degeneracy below the levels observed in our single-model sampling.\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:431:Supervised classifiers (logistic regression, MLP, random forest) trained on all five signals (5-fold CV, 3-seed mean, SciERC, $N{=}16$, $+17.9$~pp headroom) all perform at or below greedy (F1${=}0.644$; LR: $-0.4$~pp; MLP: $-1.6$~pp; RF: $-3.1$~pp).\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:444:For each of $N{=}8$ samples per instance, we extract the mean-pooled final-layer hidden state ($d{=}4096$) from the generating Qwen3-8B model and train a linear probe and a two-layer MLP (hidden dim${=}256$) to predict per-sample F1 (5-fold CV, 3 seeds).\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:475:Table~\\ref{tab:multiseed} reports quality estimation metrics across three random seeds for both model families on SciERC ($N{=}8$, $T{=}1.0$).\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:483:\\caption{Multi-seed quality estimation on SciERC ($N{=}8$, $T{=}1.0$, seeds: 42, 123, 456). NER: both models; RE: Qwen only (preliminary). Signal ranking is stable across seeds ($\\sigma{\\leq}0.025$). $\\sigma$ is population standard deviation over 3 seeds.}\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:586:\\caption{CDF of within-instance LP range on SciERC NER ($N{=}8$, $n{=}529$). The median LP range is 0.041 nats (dashed line), below $\\varepsilon{=}0.05$. The smooth CDF confirms compression is pervasive, not bimodal.}\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:593:\\caption{Log-probability score compression on SciERC NER ($N{=}8$, $n{=}529$). ``Tied'' = fraction of instances where within-instance LP range ${<}\\varepsilon$.}\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:620:\\caption{$\\varepsilon$ sensitivity sweep for LP selection on SciERC NER ($N{=}8$, seed${=}42$, $n{=}529$). ``Tied\\%'' = fraction with within-instance LP range ${<}\\varepsilon$. $\\Delta$: selection F1 gain over single-sample on the non-tied subset. The tied fraction increases smoothly; $\\varepsilon{=}0.05$ yields the strongest statistical separation.}\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:669:\\caption{Non-tied subset analysis (SciERC, Qwen3-8B, $N{=}8$, $T{=}1.0$). Instances split at LP range $\\varepsilon{=}0.05$. Within-instance $\\rho$ and selection gain both concentrate in the non-tied subset. Full $\\varepsilon$ sweep in Table~\\ref{tab:epsilon_sweep}.}\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:685:Table~\\ref{tab:within_rho} reports median within-instance $\\rho(\\text{LP}, \\text{F1})$ across datasets, computed over non-degenerate instances (those with ${\\geq}2$ distinct F1 values across $N{=}8$ samples).\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:687:CoNLL alignment is moderate ($\\rho{\\approx}0.51$), but the valid-instance fraction is low (41\\% for Qwen, 11\\% for LLaMA) because degeneracy eliminates most headroom before alignment can operate.\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:688:LP-quality alignment is the primary predictor of selection direction; degeneracy constrains headroom but does not independently predict whether LP selection gains materialize (\\S\\ref{sec:discussion}).\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:693:\\caption{Within-instance LP-quality alignment across datasets ($N{=}8$, $T{=}1.0$). $\\rho$: median Spearman correlation between LP and F1 within each instance, over non-degenerate instances ($n_{\\text{valid}}$: ${\\geq}2$ distinct F1 values).}\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:715:\\caption{Selection $\\Delta$ (pp over single-sample) stratified by VC quartile on SciERC ($N{=}8$, Qwen3-8B). Oracle headroom collapses at Q4; LP rankings are unreliable at Q1--Q2. Neither quartile supports consistent selection gains.}\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:748:All RE results use Qwen3-8B unless noted; single-seed ($\\text{seed}{=}42$) for $N{=}8$ analyses, 3-seed for $N{=}16$.\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:756:Table~\\ref{tab:re_cond_selection} presents RE selection at $N{=}8$: no signal outperforms single-sample (0.404) on the full set ($n{=}397$) or the non-zero subset ($n{=}238$), with 18.1~pp of unrealized oracle headroom.\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:757:At $N{=}16$ (Qwen3-4B, Table~\\ref{tab:re_n16_selection}), LP is the sole positive signal ($\\Delta{=}{+}0.7$~pp, $p{=}0.058$), consistent with LP being the strongest RE selection signal across scales.\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:760:At 4B scale (Qwen3-4B, $N{=}8$, $\\text{seed}{=}42$), RE quality estimation shows FK $\\rho{=}0.359$ and LP $\\rho{=}0.351$, both above their 8B counterparts (FK 0.275, LP 0.266), while SJ declines ($0.267$ vs.\\ $0.250$).\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:777:\\caption{RE selection F1 (macro, instance-averaged) on SciERC ($N{=}8$, $T{=}1.0$). Full set ($n{=}397$) and non-zero F1 subset ($n{=}238$). No signal outperforms greedy on either subset.}\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:795:\\subsection{RE $N{=}16$ Selection Analysis}\\label{app:re_n16_selection}\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:797:Table~\\ref{tab:re_n16_selection} extends the selection analysis to RE at $N{=}16$ with 3-seed statistics.\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:806:\\caption{RE best-of-$N$ selection F1 (macro, instance-averaged) on SciERC (Qwen3-4B, $N{=}16$, $T{=}1.0$, 3-seed mean${\\pm}\\sigma$, $n{=}551$). Fisher combined $p$ vs.\\ greedy. LP is the only signal with positive $\\Delta$. $\\sigma$ is population standard deviation over 3 seeds.}\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:830:Despite MBR's success in machine translation \\cite{freitag2022high} and its extension to summarization, code generation, and captioning \\cite{jinnai2024mbr}, all variants fail here: despite positive within-instance utility--F1 correlation, selection gains are limited by instance degeneracy, the core of the correlation-selection gap.\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:845:Table~\\ref{tab:freeform_ablation} compares constrained and free-form decoding across four dimensions on SciERC ($N{=}8$, $T{=}1.0$, Qwen3-8B; seed${=}42$ shown, 4-seed RE statistics below).\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:854:\\caption{Comparison of constrained vs.\\ free-form decoding on SciERC (Qwen3-8B, $N{=}8$, $T{=}1.0$, seed${=}42$; RE selection gap replicates across 4 seeds: $+1.84{\\pm}0.12$~pp).}\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:929:Extending the free-form ablation to CoNLL NER (Qwen3-8B, 4 seeds, $N{=}8$, $T{=}1.0$), LP range median is $0.058{\\pm}0.007$ across seeds, higher than SciERC ($0.041$) but still compressed given CoNLL's 86.8\\% tied fraction under constrained decoding.\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:932:The failure to improve selection despite reduced compression is consistent with CoNLL's low oracle headroom (5.0~pp at $N{=}8$), which limits the selection space regardless of score distribution quality.\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:936:We analyze RE LP selection failures across three random seeds (constrained decoding, $N{=}8$, $T{=}1.0$, Qwen3-8B) to assess whether failures are systematic or stochastic.\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:950:\\caption{RE LP selection failure stability across 3 seeds (SciERC, $N{=}8$). Stable failures concentrate on relation-dense instances with high single-sample F1.}\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:1034:Signal rankings are consistent across our 3 seeds (Kendall's $W{=}1.000$ for NER at $N{=}8$, both models), dropping to $W{=}0.956$ at $N{=}16$ where SJ and VC converge (Table~\\ref{tab:ranking-stability}); however, with only $n{=}3$ seeds statistical power is insufficient to confirm stability, and additional seeds may reveal ranking changes.\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:1038:Table~\\ref{tab:n_scaling_selection} traces the effect of sample count on degeneracy, oracle headroom, and per-signal selection gain.\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:1040:LP selection improves monotonically with $N$ ($+0.39$~pp at $N{=}8$ to $+0.95$~pp at $N{=}32$), but even at $N{=}32$, where degeneracy falls to 4\\% and oracle headroom reaches ${\\sim}20$~pp, the best signal captures less than 5\\% of the available improvement.\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:1041:Degeneracy drops monotonically (43\\% at $N{=}2$ to 4\\% at $N{=}32$), yet reduced degeneracy does not unlock selection, consistent with the LoRA-rank ablation finding (\\S\\ref{sec:robustness_main}).\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:1051:$N$ & Degen.\\% & Oracle (pp) & LP & SJ & FK & EM & VC & Best $\\Delta$ \\\\\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:1096:\\caption{Temperature ablation on SciERC NER (Qwen3-8B, $N{=}8$, seed${=}42$). Oracle gap and QE $\\rho$ across four temperatures. $\\kappa$: Fleiss' $\\kappa$ (inter-sample agreement). $T{=}0.5$ and $T{=}1.0$ use joint (NER+RE) subtask; $T{=}0.8$ and $T{=}1.2$ use NER-only.}\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:1117:\\paragraph{Temperature controls degeneracy and LP spread.}\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:1118:Table~\\ref{tab:t_degeneracy} reports instance degeneracy (constant F1, gold-filtered) and median within-instance LP range across four temperatures on SciERC.\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:1119:Both quantities are strictly monotonic in $T$: degeneracy falls from 41.4\\% ($T{=}0.5$) to 14.9\\% ($T{=}1.2$), while LP range increases from 0.015 to 0.058 nats.\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:1120:Temperature thus provides a direct lever for practitioners to shift the degeneracy regime.\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:1121:However, even at $T{=}1.2$ where degeneracy (14.9\\%) approaches Few-NERD levels (${\\sim}$14\\%), within-instance $\\rho(\\text{LP}, \\text{F1})$ remains at 0.225, far below Few-NERD's ${\\sim}$0.5.\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:1122:This confirms that temperature controls degeneracy but cannot improve LP-quality alignment, which is largely determined by task structure and remains relatively stable across generation configurations (\\S\\ref{app:epoch_confound}). LP-quality alignment, not degeneracy, is the primary predictor of LP selection direction (\\S\\ref{sec:discussion}).\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:1127:\\caption{Temperature sensitivity of degeneracy and LP spread (SciERC NER, Qwen3-8B, $N{=}8$). Degeneracy: constant-F1, gold-filtered. LP range: median within-instance range.}\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:1128:\\label{tab:t_degeneracy}\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:1131:$T$ & Degen.\\% & LP range (nats) & Fleiss' $\\kappa$ & SJ mean \\\\\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:1148:\\caption{Cross-dataset OOD quality estimation (Spearman $\\rho$, Qwen3-8B, $N{=}8$, $T{=}1.0$, seed${=}42$). SciERC$\\to$CoNLL: SciERC-trained model on CoNLL instances ($n{=}2756$). CoNLL$\\to$SciERC: CoNLL-trained model on SciERC instances ($n{=}529$, excluded from conclusions due to catastrophic model failure). In-domain $\\rho$ from Table~\\ref{tab:quality_estimation} (same model, same seed). \\textsuperscript{***}$p{<}0.001$, \\textsuperscript{*}$p{<}0.05$.}\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:1166:When the SciERC-trained model (6 NER types) is applied to CoNLL (4 types), all signals remain significant ($p{<}0.001$) and structural signals improve over their in-domain levels (same model, seed${=}42$, $N{=}8$; in-domain $\\rho$ from Table~\\ref{tab:quality_estimation}): VC reaches $\\rho{=}0.469$ (in-domain $0.379$, $\\Delta{=}{+}0.090$), SJ $\\rho{=}0.378$ (in-domain $0.360$, $\\Delta{=}{+}0.018$), and FK $\\rho{=}0.285$ (in-domain $0.267$, $\\Delta{=}{+}0.018$).\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:1187:\\caption{Verbalized confidence (VerbConf) vs.\\ log-probability selection (Qwen3-8B, $N{=}8$, $T{=}1.0$, seed${=}42$). Parse fail: fraction of samples where the confidence score could not be extracted.}\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:1222:\\caption{LLaMA-3.2-3B SciERC NER quality estimation and selection ($N{=}8$, $T{=}1.0$, seed${=}42$). Greedy F1${=}0.627$, Oracle F1${=}0.763$, headroom${=}13.63$~pp.}\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:1246:Table~\\ref{tab:fewnerd_full} reports the complete Few-NERD INTRA coarse evaluation (Qwen3-8B, LoRA rank${=}32$, 3 epochs, $N{=}8$, $T{=}1.0$).\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:1248:Instance degeneracy is 13.8\\% (vs.\\ 17.8\\% on SciERC, 48.4\\% on CoNLL).\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:1253:\\caption{Few-NERD INTRA coarse: complete quality estimation and selection results (Qwen3-8B, $N{=}8$, $T{=}1.0$, gold-filtered $n{=}32{,}565$). $\\rho$: Spearman correlation with instance F1. Sample AUROC: per-sample LP discrimination. Sel.\\ $\\Delta$: selection F1 minus greedy (0.748). CI: bootstrap 95\\% confidence interval.}\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:1274:(4)~Low degeneracy (13.8\\%) combined with strong LP-quality alignment ($\\rho{\\approx}0.5$--$0.7$) enables LP selection: candidates differ in F1 more often, and LP can rank them effectively. This contrasts with SciERC (17.8\\% degeneracy but weak alignment $\\rho{\\approx}0.24$, LP $+0.61$~pp) and CoNLL (48.4\\%, LP $-0.85$~pp).\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:1278:Table~\\ref{tab:per_type_lp} stratifies LP selection by entity type on Few-NERD, sorted by degeneracy rate.\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:1279:The degeneracy-gating mechanism holds at entity-type granularity: 7 of 8 types show positive LP selection gains, and the sole negative type (Art, $-0.17$~pp) has the highest degeneracy (19.8\\%).\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:1280:The correlation between per-type degeneracy and oracle headroom is strong and significant (Spearman $\\rho{=}{-}0.881$, $p{=}0.004$; exact permutation $p{=}0.005$); degeneracy directly constrains the headroom available for selection.\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:1287:\\caption{Per-entity-type LP selection on Few-NERD INTRA coarse (Qwen3-8B, $N{=}8$, $T{=}1.0$), sorted by degeneracy. LP $\\Delta$: LP selection F1 minus greedy. 7/8 types show positive $\\Delta$; Art (highest degeneracy) is the sole exception.}\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:1291:Entity Type & $n$ & Degen.\\% & Greedy & LP Sel & $\\Delta$ (pp) & LP $\\rho$ & Headroom \\\\\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:1308:\\caption{CoNLL-2003 per-type LP selection (Qwen3-8B, $N{=}16$, $T{=}1.0$). All types exceed 20\\% degeneracy and show negative LP selection, consistent with the dataset's ceiling-regime performance (F1 $>$ 90\\%).}\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:1312:Entity Type & Degen.\\% & LP $\\Delta$ (pp) \\\\\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:1325:\\caption{SciERC per-type LP selection (Qwen3-8B, $N{=}8$, $T{=}1.0$). Within-dataset, degeneracy alone does not predict LP effectiveness (Spearman $\\rho{=}0.14$, $p{=}0.79$); additional type-specific factors likely modulate selection at this granularity.}\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:1329:Entity Type & Degen.\\% & LP $\\Delta$ (pp) \\\\\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:1341:The cross-dataset degeneracy gradient (48.4\\% $\\to$ 17.8\\% $\\to$ 13.8\\%) is inversely associated with LP selection effectiveness at the macro level ($n{=}3$ datasets; exploratory).\\footnote{Partial Spearman correlation controlling for entity-type frequency yields $\\rho{=}{-}0.47$ (vs.\\ raw $\\rho{=}{-}0.38$); type frequency does not confound the degeneracy--LP relationship.}\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:1342:At finer per-type granularity, selection depends on the interaction of degeneracy, oracle headroom, and type-specific LP-quality alignment.\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:1344:Low degeneracy alone does not ensure selection gains: CoNLL MISC (23\\%, headroom 12.6~pp) and SciERC OtherScientificTerm (6.2\\%, headroom 12.5~pp) both show negative LP selection despite available headroom; LP correlation strength with the type-specific quality function is an additional prerequisite.\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:1359:\\caption{Calibration baseline results ($N{=}8$, $T{=}1.0$). Platt and TempScale are monotonic transforms of LP that preserve the within-instance argmax (selection F1 $\\equiv$ Raw LP, omitted). MF-Platt uses LP $+$ token count $+$ entity count; $p$: bootstrap test vs.\\ Raw LP.}\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:1376:\\paragraph{Training convergence modulates degeneracy.}\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:1377:Table~\\ref{tab:epoch_confound} compares the 3-epoch model (used throughout the main text) with a 5-epoch variant on Few-NERD (Qwen3-8B, $N{=}8$, $T{=}1.0$).\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:1378:Extended training increases greedy F1 by $+2.95$~pp (0.748 $\\to$ 0.777) but nearly triples instance degeneracy (11.1\\% $\\to$ 31.3\\%), reducing the fraction of instances with non-degenerate outputs from 85.6\\% to 68.7\\%.\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:1379:LP selection gains drop correspondingly ($+1.37$~pp $\\to$ $+0.62$~pp), consistent with the degeneracy-gating mechanism identified in the main text (\\S\\ref{sec:discussion}).\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:1383:Standard early stopping practice thus naturally selects the low-degeneracy regime where LP selection is most effective.\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:1384:This finding refines the narrative: degeneracy is not a fixed property of datasets but is modulated by the degree of training convergence. Over-trained models compress their output distributions, collapsing diversity even on datasets that support it under well-regularized training.\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:1389:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:1396:Instance degen.\\ (\\%) & 11.1 & 31.3 \\\\\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:1406:Table~\\ref{tab:epoch_scierc} extends the analysis to SciERC with a 3-point curve (3, 5, 10 epochs; Qwen3-8B, $N{=}8$, $T{=}1.0$).\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:1407:Degeneracy increases monotonically (6.4\\% $\\to$ 17.8\\% $\\to$ 47.8\\%), and within-instance LP-quality correlation degrades in tandem (median $\\rho$: 0.319 $\\to$ 0.262 $\\to$ 0.112; mean $\\rho$: 0.273 $\\to$ 0.179 $\\to$ 0.066), confirming that overtraining erodes both diversity and LP alignment simultaneously.\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:1410:The 3-epoch model has higher within-instance alignment ($\\rho{=}0.319$) than the 5-epoch model ($\\rho{=}0.262$), yet LP selection is worse ($-1.24$ vs.\\ $+0.64$~pp): at 6.4\\% degeneracy, more non-degenerate instances enter the candidate pool, but LP ranking precision is too low to exploit them, so the broader pool hurts rather than helps. This illustrates that low degeneracy does not ensure selection gains; LP-quality alignment determines selection direction.\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:1411:At 10 epochs, the model retains competitive greedy F1 (0.649 vs.\\ 0.650 at 3 epochs) yet conditions are unfavorable: 47.8\\% degenerate instances and $\\rho{=}0.112$.\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:1412:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:1418:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:1425:Instance degen.\\ (\\%) & 6.4 & 17.8 & 47.8 \\\\\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:1435:The Few-NERD epoch analysis covers 2 points (3 vs.\\ 5 epochs); the SciERC curve provides a 3-point gradient showing monotonic degeneracy increase with simultaneous within-instance alignment degradation.\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:1436:CoNLL epoch variation remains unverified; high-degeneracy datasets (CoNLL at 59--89\\%) may exhibit a ceiling effect where additional training has limited marginal impact.\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:1440:\\subsection{Degeneracy-Aware LP Selection}\\label{app:dals}\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:1442:The non-tied subset analysis (Table~\\ref{tab:nontied_main}) identifies within-instance LP range (max minus min LP across $N$ samples) as a per-instance degeneracy proxy: instances with near-zero LP range carry no discriminative signal.\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:1443:Degeneracy-aware LP selection (DALS) operationalizes this: when LP range exceeds $\\tau{=}0.05$ (the threshold independently motivated by the non-tied analysis; Appendix~\\ref{app:epsilon_robustness}), select the highest-LP sample; otherwise fall back to greedy.\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:1445:DALS improves over pure LP selection when degeneracy is moderate, provides partial damage control when LP selection is harmful, and defaults to greedy when LP range signals no information.\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:1446:While gains are modest and seed-sensitive, LP range serves as an operationally accessible degeneracy proxy, though the mixed cross-dataset results confirm that degeneracy gating alone cannot ensure positive selection outcomes.\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:1452:This sensitivity reinforces the diagnostic framing of DALS: per-dataset $\\tau$ tuning is required for positive gains, and even optimally tuned DALS cannot overcome weak LP-quality alignment on high-degeneracy datasets.\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:1456:To test whether LP-quality alignment drives selection gains within datasets, we restrict LP selection to the favorable subset: non-degenerate instances whose within-instance LP range exceeds the dataset-specific median (SciERC: 0.040 nats, CoNLL: 0.062, Few-NERD: 0.067).\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:1462:\\caption{LP selection on the favorable subset (non-degenerate instances with LP range above the dataset-specific median) per dataset (Qwen3-8B, $N{=}8$, $T{=}1.0$). CI: bootstrap 95\\% confidence interval.}\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:1475:On SciERC, restricting to the favorable subset recovers a significant LP gain, consistent with LP-quality alignment driving selection within the non-degenerate pool.\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:1483:Table~\\ref{tab:entity_token_lp} compares the two aggregation strategies on SciERC (Qwen3-8B, $N{=}8$, $T{=}1.0$).\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:1488:\\caption{Full-sequence vs.\\ entity-token LP on SciERC NER (Qwen3-8B, $N{=}8$, $T{=}1.0$). Entity-token LP has higher variance and stronger correlation, yet selection degrades.}\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:1506:We sweep $k \\in \\{2, 3, \\ldots, 8\\}$ on each dataset (Qwen3-8B, $N{=}8$, $T{=}1.0$) and report the best threshold per dataset.\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:1511:\\caption{Entity-level majority voting results (Qwen3-8B, $N{=}8$, $T{=}1.0$). ``Greedy'': $T{=}0$ baseline. ``Best merge'': optimal $k$ per dataset from sweep $k \\in \\{2, \\ldots, 8\\}$. ``$\\Delta$'': merge F1 minus greedy. ``Recovery'': $\\Delta$ / (oracle $-$ greedy). Only SciERC shows positive recovery; even with oracle $k$, CoNLL and Few-NERD degrade.}\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:1524:On degenerate subsets (instances where all $N$ samples yield identical F1), merge is uniformly negative across all three datasets, confirming that entity-level aggregation cannot bypass the diversity bottleneck identified in the main text (\\S\\ref{sec:discussion}).\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:1529:Table~\\ref{tab:theta_sweep} reports entity construction F1 as a function of the confirmation threshold $\\theta$ across three datasets (Qwen3-8B, $N{=}8$, $T{=}1.0$). The default $\\theta{=}2/N{=}0.25$ achieves the best LP-weighted $\\Delta$F1 on Few-NERD and is within 0.04\\,pp of the optimum on SciERC. Performance is stable across $\\theta \\in [0.15, 0.35]$; below 0.15, spurious entities degrade precision, and above 0.40, aggressive filtering removes correct low-frequency entities.\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:1532:\\caption{Entity construction threshold sensitivity ($N{=}8$, Qwen3-8B, $T{=}1.0$). $\\Delta$: F1 difference vs.\\ greedy in percentage points. Best $\\Delta$ per dataset--weighting pair in \\textbf{bold}.}\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.log:639:&lt;figures/fig_degeneracy_lp_scatter.pdf, id=835, 496.89139pt x 338.86536pt>\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.log:640:File: figures/fig_degeneracy_lp_scatter.pdf Graphic file (type pdf)\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.log:641:&lt;use figures/fig_degeneracy_lp_scatter.pdf>\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.log:642:Package pdftex.def Info: figures/fig_degeneracy_lp_scatter.pdf  used on input l\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.log:655:[7 <./figures/fig_degeneracy_lp_scatter.pdf>]\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.log:1148:\\T1/ptm/m/n/10.95 (+20) vari-a-tion re-mains un-ver-i-fied; high-degeneracy\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex:8:Unlike \\citet{yao2026consistency}, who demonstrate that self-consistency correlates with task accuracy, we provide the first systematic empirical characterization of \\textit{when and why} LP-based selection succeeds or fails for structured prediction, diagnosing degeneracy and compression as the two blocking mechanisms.\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex:13:For selection, LP achieves $+1.39$~pp on Few-NERD ($p{<}0.001$) in settings where both low instance degeneracy and adequate alignment are present, with gains scaling with $N$.\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex:15:Three factors qualitatively shape this gap: (a)~\\textit{instance degeneracy} (13\\textendash 87\\% across our benchmarks) compresses the candidate space; (b)~\\textit{oracle headroom} bounds the achievable gain; (c)~\\textit{LP-quality alignment} (within-instance $\\rho(\\text{LP}, \\text{F1})$) determines whether LP can discriminate candidates in non-degenerate instances (\\S\\ref{sec:selection_gap}).\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex:16:Our diagnosis is complementary to minimum Bayes risk (MBR) utility misalignment \\cite{eikema2025structured}: where MBR failures in structured prediction stem from poorly chosen utility functions, we find that degeneracy eliminates candidate diversity before utility alignment matters.\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex:17:Within non-degenerate instances, MBR utility correlates positively with F1 ($\\rho{=}0.52$; \\S\\ref{sec:discussion}).\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex:18:Both mechanisms intensify with model capability: degeneracy rises with scale and training convergence (\\S\\ref{sec:discussion}). This creates a tension between model quality and test-time improvability.\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex:27:We evaluate five signals from three families (structural, surface, and model-internal) on SciERC \\cite{luan2018scierc} as a primary medium-difficulty test bed, with Few-NERD \\cite{ding2021fewnerd} (low-degeneracy contrast), CoNLL-2003 \\cite{tjongkimsang2003conll} (ceiling-effect control), and WNUT-17 \\cite{derczynski2017wnut} (signal-collapse boundary), using two 8B models (Qwen3-8B, LLaMA-3.1-8B) with a 4B ablation (Qwen3-4B).\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex:38:    Instance degeneracy causally modulates LP within fixed settings (epoch and temperature ablations), but does not predict cross-dataset direction ($\\rho{=}0.052$, 23 configurations); structural signals fail by construction; supervised combinations and hidden state probes (Appendix~\\ref{app:hidden_probe}) confirm the gap persists.\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.fdb_latexmk:177:  \"figures/fig_degeneracy_lp_scatter.pdf\" 1779142597.47711 23704 4047110cb8d4964d79aee9015c571c39 \"\"\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/references.bib:450:  title = {The Curious Case of Neural Text Degeneration},\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.aux:480:\\@writefile{lof}{\\contentsline {figure}{\\numberline {2}{\\ignorespaces The correlation-selection gap on SciERC ($N{=}8$, $T{=}1.0$). Bars: quality estimation $\\rho $ (seed 42); line with error bars: $\\Delta $F1 vs.\\ greedy (3-seed mean, seeds 42/123/456). Despite $\\rho $ up to 0.38, no signal significantly outperforms greedy (all $p{>}0.05$; Table~\\ref {tab:selection}). Dashed green: oracle upper bound ($+13.1$~pp); dotted gray: random baseline.}}{5}{figure.caption.18}\\protected@file@percent }\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.aux:481:\\newlabel{fig:selection_gap}{{2}{5}{The correlation-selection gap on SciERC ($N{=}8$, $T{=}1.0$). Bars: quality estimation $\\rho $ (seed 42); line with error bars: $\\Delta $F1 vs.\\ greedy (3-seed mean, seeds 42/123/456). Despite $\\rho $ up to 0.38, no signal significantly outperforms greedy (all $p{>}0.05$; Table~\\ref {tab:selection}). Dashed green: oracle upper bound ($+13.1$~pp); dotted gray: random baseline}{figure.caption.18}{}}\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.aux:515:\\@writefile{lot}{\\contentsline {table}{\\numberline {1}{\\ignorespaces NER quality estimation ($\\rho $ and AUROC; $N{=}8$, primary seed${=}42$; 3-seed stability $\\sigma {\\leq }0.026$ in Table~\\ref {tab:multiseed}). Best in \\textbf  {bold}. RE results in Appendix~\\ref {app:re_extension}. $N{=}16$ in Table~\\ref {tab:robustness}.}}{6}{table.caption.15}\\protected@file@percent }\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.aux:516:\\newlabel{tab:quality_estimation}{{1}{6}{NER quality estimation ($\\rho $ and AUROC; $N{=}8$, primary seed${=}42$; 3-seed stability $\\sigma {\\leq }0.026$ in Table~\\ref {tab:multiseed}). Best in \\textbf {bold}. RE results in Appendix~\\ref {app:re_extension}. $N{=}16$ in Table~\\ref {tab:robustness}}{table.caption.15}{}}\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.aux:518:\\@writefile{lot}{\\contentsline {table}{\\numberline {2}{\\ignorespaces Best-of-$N$ NER selection (macro F1) on SciERC ($N{=}8$, $T{=}1.0$, 2-seed mean${\\pm }\\sigma $). LP is per-sample; others use consensus-proximity. Best non-oracle in \\textbf  {bold}. Non-tied subset in \\S  \\ref {sec:discussion}; RE in Appendix~\\ref {app:re_extension}. $^\\dagger $Instance-level signals assign one score per input; per-sample ranking $p$-values are undefined.}}{6}{table.caption.17}\\protected@file@percent }\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.aux:519:\\newlabel{tab:selection}{{2}{6}{Best-of-$N$ NER selection (macro F1) on SciERC ($N{=}8$, $T{=}1.0$, 2-seed mean${\\pm }\\sigma $). LP is per-sample; others use consensus-proximity. Best non-oracle in \\textbf {bold}. Non-tied subset in \\S \\ref {sec:discussion}; RE in Appendix~\\ref {app:re_extension}. $^\\dagger $Instance-level signals assign one score per input; per-sample ranking $p$-values are undefined}{table.caption.17}{}}\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.aux:544:\\@writefile{lot}{\\contentsline {table}{\\numberline {3}{\\ignorespaces LP selection across datasets (Qwen3-8B, $N{=}8$, $T{=}1.0$, gold-filtered). Few-NERD/CoNLL: 3-seed means; SciERC: single-seed (3-seed in Table~\\ref {tab:multiseed}). $p$: paired bootstrap.}}{6}{table.caption.21}\\protected@file@percent }\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.aux:545:\\newlabel{tab:fewnerd}{{3}{6}{LP selection across datasets (Qwen3-8B, $N{=}8$, $T{=}1.0$, gold-filtered). Few-NERD/CoNLL: 3-seed means; SciERC: single-seed (3-seed in Table~\\ref {tab:multiseed}). $p$: paired bootstrap}{table.caption.21}{}}\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.aux:571:\\@writefile{toc}{\\contentsline {paragraph}{Degeneracy alone does not predict LP selection direction.}{6}{section*.22}\\protected@file@percent }\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.aux:580:\\@writefile{lof}{\\contentsline {figure}{\\numberline {3}{\\ignorespaces Instance degeneracy vs.\\ LP selection gain across 23 configurations ($N{=}8$; $\\rho {=}0.052$, $p{=}0.81$). Within Few-NERD per-entity-type analysis ($\\rho {=}{-}0.881$; Appendix~\\ref {app:per_type_lp}), degeneracy predicts LP gain when alignment is held constant.}}{7}{figure.caption.23}\\protected@file@percent }\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.aux:581:\\newlabel{fig:degeneracy_scatter}{{3}{7}{Instance degeneracy vs.\\ LP selection gain across 23 configurations ($N{=}8$; $\\rho {=}0.052$, $p{=}0.81$). Within Few-NERD per-entity-type analysis ($\\rho {=}{-}0.881$; Appendix~\\ref {app:per_type_lp}), degeneracy predicts LP gain when alignment is held constant}{figure.caption.23}{}}\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.aux:582:\\@writefile{lot}{\\contentsline {table}{\\numberline {4}{\\ignorespaces Scale ablation: 8B vs.\\ 4B QE $\\rho $ ($N{=}8$, $T{=}1.0$, seed 42). RE in Appendix~\\ref {app:re_extension}.}}{7}{table.caption.24}\\protected@file@percent }\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.aux:583:\\newlabel{tab:scale_ablation}{{4}{7}{Scale ablation: 8B vs.\\ 4B QE $\\rho $ ($N{=}8$, $T{=}1.0$, seed 42). RE in Appendix~\\ref {app:re_extension}}{table.caption.24}{}}\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.aux:614:\\@writefile{lot}{\\contentsline {table}{\\numberline {5}{\\ignorespaces Fine-tuned 8B vs.\\ zero-shot 72B ($N{=}8$, $T{=}1.0$). Hdr.\\ = oracle $-$ greedy (pp).}}{7}{table.caption.28}\\protected@file@percent }\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.aux:615:\\newlabel{tab:scale_comparison}{{5}{7}{Fine-tuned 8B vs.\\ zero-shot 72B ($N{=}8$, $T{=}1.0$). Hdr.\\ = oracle $-$ greedy (pp)}{table.caption.28}{}}\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.aux:659:\\@writefile{lot}{\\contentsline {table}{\\numberline {6}{\\ignorespaces Entity construction vs.\\ greedy ($\\Delta $ macro F1; $N{=}8$, $T{=}1.0$, Qwen3-8B, multi-seed mean${\\pm }\\sigma $). $\\theta {=}2/N$. $p$: paired bootstrap vs.\\ greedy. Best in \\textbf  {bold}.}}{8}{table.caption.31}\\protected@file@percent }\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.aux:660:\\newlabel{tab:entity_construction}{{6}{8}{Entity construction vs.\\ greedy ($\\Delta $ macro F1; $N{=}8$, $T{=}1.0$, Qwen3-8B, multi-seed mean${\\pm }\\sigma $). $\\theta {=}2/N$. $p$: paired bootstrap vs.\\ greedy. Best in \\textbf {bold}}{table.caption.31}{}}\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.aux:1489:\\@writefile{lot}{\\contentsline {table}{\\numberline {8}{\\ignorespaces Signal robustness across configurations (Spearman $\\rho $). Top: temperature on Qwen SciERC. Middle: sample size on Qwen SciERC. Bottom: transfer across model families (both 8B) (LLaMA CoNLL $N{=}16$, 3-seed mean $\\pm \\sigma $). $^\\dagger $Mean over 3 seeds ($\\sigma {=}0.013$; individual: 0.398, 0.423, 0.410). $\\sigma $ computed as sample standard deviation.}}{15}{table.caption.46}\\protected@file@percent }\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.aux:1490:\\newlabel{tab:robustness}{{8}{15}{Signal robustness across configurations (Spearman $\\rho $). Top: temperature on Qwen SciERC. Middle: sample size on Qwen SciERC. Bottom: transfer across model families (both 8B) (LLaMA CoNLL $N{=}16$, 3-seed mean $\\pm \\sigma $). $^\\dagger $Mean over 3 seeds ($\\sigma {=}0.013$; individual: 0.398, 0.423, 0.410). $\\sigma $ computed as sample standard deviation}{table.caption.46}{}}\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.aux:1508:\\@writefile{lof}{\\contentsline {figure}{\\numberline {5}{\\ignorespaces Temperature robustness on SciERC ($N{=}8$). Top: NER; bottom: RE. SJ maintains stable $\\rho $ across $T{=}0.7$ and $T{=}1.0$, while FK shows mixed sensitivity. LP shows the largest NER temperature effect ($\\Delta \\rho {=}{+}0.044$); RE $T{=}0.7$ LP data unavailable.}}{15}{figure.caption.47}\\protected@file@percent }\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.aux:1509:\\newlabel{fig:temperature_robustness}{{5}{15}{Temperature robustness on SciERC ($N{=}8$). Top: NER; bottom: RE. SJ maintains stable $\\rho $ across $T{=}0.7$ and $T{=}1.0$, while FK shows mixed sensitivity. LP shows the largest NER temperature effect ($\\Delta \\rho {=}{+}0.044$); RE $T{=}0.7$ LP data unavailable}{figure.caption.47}{}}\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.aux:1647:\\@writefile{lof}{\\contentsline {figure}{\\numberline {6}{\\ignorespaces Reliability diagrams on SciERC ($N{=}8$, $T{=}1.0$). Top: mean F1 vs.\\ binned confidence; bottom: instance counts per bin. Left: NER; right: RE. NER signals are reasonably well-calibrated (calibration ECE 0.069--0.096), while RE shows greater miscalibration (ECE 0.109--0.339), RE calibration remains challenging for compound extraction tasks.}}{17}{figure.caption.53}\\protected@file@percent }\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.aux:1648:\\newlabel{fig:reliability}{{6}{17}{Reliability diagrams on SciERC ($N{=}8$, $T{=}1.0$). Top: mean F1 vs.\\ binned confidence; bottom: instance counts per bin. Left: NER; right: RE. NER signals are reasonably well-calibrated (calibration ECE 0.069--0.096), while RE shows greater miscalibration (ECE 0.109--0.339), RE calibration remains challenging for compound extraction tasks}{figure.caption.53}{}}\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.aux:1682:\\@writefile{lot}{\\contentsline {table}{\\numberline {10}{\\ignorespaces SJ normalizer comparison (Spearman $\\rho $; $N{=}8$, $T{=}1.0$, seed${=}42$). Max: $\\max (|g_i|,|g_j|)$; Union: $|g_i \\cup g_j|$.}}{17}{table.caption.61}\\protected@file@percent }\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.aux:1683:\\newlabel{tab:sj_normalizer}{{10}{17}{SJ normalizer comparison (Spearman $\\rho $; $N{=}8$, $T{=}1.0$, seed${=}42$). Max: $\\max (|g_i|,|g_j|)$; Union: $|g_i \\cup g_j|$}{table.caption.61}{}}\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.aux:1705:\\@writefile{lof}{\\contentsline {figure}{\\numberline {8}{\\ignorespaces Output length vs.\\ mean log-probability on SciERC ($N{=}8$, $T{=}1.0$). Positive correlations (NER: $\\rho {=}0.386$; RE: $\\rho {=}0.326$) rule out length-penalty confounding.}}{18}{figure.caption.58}\\protected@file@percent }\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.aux:1706:\\newlabel{fig:length_logprob_scatter}{{8}{18}{Output length vs.\\ mean log-probability on SciERC ($N{=}8$, $T{=}1.0$). Positive correlations (NER: $\\rho {=}0.386$; RE: $\\rho {=}0.326$) rule out length-penalty confounding}{figure.caption.58}{}}\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.aux:1729:\\@writefile{lot}{\\contentsline {table}{\\numberline {11}{\\ignorespaces Quality estimation on WNUT-17 (Qwen, $N{=}16$, $T{=}1.0$, $n{=}689$). Cond: non-zero F1 instances ($n{=}334$). Full-set $\\rho $ reflects binary success prediction; conditional $\\rho $ measures quality gradation. LP's conditional $\\rho $ is highest despite negative full-set $\\rho $.}}{18}{table.caption.64}\\protected@file@percent }\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.aux:1730:\\newlabel{tab:wnut}{{11}{18}{Quality estimation on WNUT-17 (Qwen, $N{=}16$, $T{=}1.0$, $n{=}689$). Cond: non-zero F1 instances ($n{=}334$). Full-set $\\rho $ reflects binary success prediction; conditional $\\rho $ measures quality gradation. LP's conditional $\\rho $ is highest despite negative full-set $\\rho $}{table.caption.64}{}}\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.aux:1794:\\@writefile{toc}{\\contentsline {paragraph}{$N{=}16$ CoNLL selection: small but significant.}{19}{section*.68}\\protected@file@percent }\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.aux:1859:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.aux:1860:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.aux:1862:\\@writefile{lot}{\\contentsline {table}{\\numberline {13}{\\ignorespaces Bootstrap 95\\% CIs for signal $\\rho $ on SciERC NER ($N{=}8$, $n{=}529$, $B{=}10{,}000$, seed${=}42$). Top: individual signals. Bottom: pairwise $\\Delta \\rho $; ``Sig.'' indicates whether the 95\\% CI excludes zero.}}{20}{table.caption.69}\\protected@file@percent }\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.aux:1863:\\newlabel{tab:bootstrap_signal_ci}{{13}{20}{Bootstrap 95\\% CIs for signal $\\rho $ on SciERC NER ($N{=}8$, $n{=}529$, $B{=}10{,}000$, seed${=}42$). Top: individual signals. Bottom: pairwise $\\Delta \\rho $; ``Sig.'' indicates whether the 95\\% CI excludes zero}{table.caption.69}{}}\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.aux:1881:\\@writefile{toc}{\\contentsline {paragraph}{Instance degeneracy statistics.}{20}{section*.74}\\protected@file@percent }\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.aux:1887:\\@writefile{lot}{\\contentsline {table}{\\numberline {14}{\\ignorespaces Output diversity across configurations ($N{=}8$, $T{=}1.0$). ``Identical'' = fraction of instances with all $N$ outputs identical. ``Unique'' = mean fraction of distinct outputs per instance.}}{20}{table.caption.71}\\protected@file@percent }\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.aux:1888:\\newlabel{tab:diversity}{{14}{20}{Output diversity across configurations ($N{=}8$, $T{=}1.0$). ``Identical'' = fraction of instances with all $N$ outputs identical. ``Unique'' = mean fraction of distinct outputs per instance}{table.caption.71}{}}\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.aux:1889:\\@writefile{lot}{\\contentsline {table}{\\numberline {15}{\\ignorespaces Instance degeneracy statistics ($T{=}1.0$). ``Constant F1'': all $N$ samples receive identical instance-level F1. ``Constant utility'': MBR (SJ) utility identical across candidates. 4B data confirms degeneracy scales with model capability.}}{20}{table.caption.75}\\protected@file@percent }\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.aux:1890:\\newlabel{tab:degeneracy}{{15}{20}{Instance degeneracy statistics ($T{=}1.0$). ``Constant F1'': all $N$ samples receive identical instance-level F1. ``Constant utility'': MBR (SJ) utility identical across candidates. 4B data confirms degeneracy scales with model capability}{table.caption.75}{}}\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.aux:1912:\\@writefile{lot}{\\contentsline {table}{\\numberline {16}{\\ignorespaces TOST equivalence testing: signals vs.\\ single-sample on SciERC ($N{=}8$, $T{=}1.0$). \\text  {$\\mathsurround \\z@ \\mathchar \"558$}: equivalent at $p{<}0.05$; \\texttimes : not equivalent. $\\Delta $: mean F1 difference (signal $-$ single-sample).}}{21}{table.caption.77}\\protected@file@percent }\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.aux:1913:\\newlabel{tab:tost}{{16}{21}{TOST equivalence testing: signals vs.\\ single-sample on SciERC ($N{=}8$, $T{=}1.0$). \\checkmark : equivalent at $p{<}0.05$; \\texttimes : not equivalent. $\\Delta $: mean F1 difference (signal $-$ single-sample)}{table.caption.77}{}}\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.aux:2114:\\@writefile{lot}{\\contentsline {table}{\\numberline {18}{\\ignorespaces Multi-seed quality estimation on SciERC ($N{=}8$, $T{=}1.0$, seeds: 42, 123, 456). NER: both models; RE: Qwen only (preliminary). Signal ranking is stable across seeds ($\\sigma {\\leq }0.025$). $\\sigma $ is population standard deviation over 3 seeds.}}{23}{table.caption.84}\\protected@file@percent }\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.aux:2115:\\newlabel{tab:multiseed}{{18}{23}{Multi-seed quality estimation on SciERC ($N{=}8$, $T{=}1.0$, seeds: 42, 123, 456). NER: both models; RE: Qwen only (preliminary). Signal ranking is stable across seeds ($\\sigma {\\leq }0.025$). $\\sigma $ is population standard deviation over 3 seeds}{table.caption.84}{}}\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.aux:2186:\\@writefile{lof}{\\contentsline {figure}{\\numberline {9}{\\ignorespaces CDF of within-instance LP range on SciERC NER ($N{=}8$, $n{=}529$). The median LP range is 0.041 nats (dashed line), below $\\varepsilon {=}0.05$. The smooth CDF confirms compression is pervasive, not bimodal.}}{24}{figure.caption.91}\\protected@file@percent }\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.aux:2187:\\newlabel{fig:lp_range_cdf}{{9}{24}{CDF of within-instance LP range on SciERC NER ($N{=}8$, $n{=}529$). The median LP range is 0.041 nats (dashed line), below $\\varepsilon {=}0.05$. The smooth CDF confirms compression is pervasive, not bimodal}{figure.caption.91}{}}",
    "numLines": 250,
    "appliedLimit": 250
  },
  "sourceToolAssistantUUID": "86d8657a-d9ed-407b-9d00-16dc11baeb83",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "a6ae7e35-390a-442a-93d4-9958c82c9e3b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 42 · 2026-05-19T13:56:20.192Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01XjZ2APjZSKQ5EDBhYNyDgv`</summary>

```json
{
  "pattern": "degen",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper",
  "output_mode": "content",
  "-n": true,
  "context": 2
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a9973ca9-06cd-4bb8-ae38-3d7eed32574d",
  "isSidechain": false,
  "requestId": "req_011CbC3Pxv93WgQzk1DKwMVV",
  "type": "assistant",
  "uuid": "2fae23d2-b5a0-47cd-83c7-cfefc7eb209b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "a6ae7e35-390a-442a-93d4-9958c82c9e3b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011jjkmKY2LB54THfWCyG2US",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 20622,
      "cache_read_input_tokens": 40694,
      "output_tokens": 2413,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 20622,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2413,
          "cache_read_input_tokens": 40694,
          "cache_creation_input_tokens": 20622,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 20622
          },
          "type": "message"
        }
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

_source line 43_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[System 触发审查]: 收到你的 critical 审查报告，6 个数据一致性问题全部确认。已派 Agent 紧急调查修复。  请你重点关注 P0-1 SciERC AUROC 问题：如果 EM AUROC 确实是 0.749 而非 0.614，论文中以下叙述可能需要修改： 1. Table 1 信号排序结论（EM 可能超过 VC 成为 SciERC 最高 AUROC） 2. 正文中关于\"s…",
  "leafUuid": "eb344fe9-a9c9-4807-b133-fd7c8f9bf748",
  "sessionId": "a6ae7e35-390a-442a-93d4-9958c82c9e3b"
}
```

---

### Runtime record

_source line 44_

```json
{
  "type": "ai-title",
  "aiTitle": "Verify SciERC AUROC data consistency issues",
  "sessionId": "a6ae7e35-390a-442a-93d4-9958c82c9e3b"
}
```

---

### Assistant

_source line 45 · 2026-05-19T13:56:23.566Z_

<details><summary>Logged reasoning block</summary>

```text
The output is too large. Let me focus on reading the specific sections of the paper that mention degeneracy and N values. Let me read the experiments.tex and discussion.tex more carefully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "eb344fe9-a9c9-4807-b133-fd7c8f9bf748",
  "isSidechain": false,
  "requestId": "req_011CbC3TX5jmJ87xXARk35SE",
  "type": "assistant",
  "uuid": "40871541-8257-4785-95cb-215e80cdc12f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "a6ae7e35-390a-442a-93d4-9958c82c9e3b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AyR5Ldnzg5UHXW9e26zBYn",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4161,
      "cache_read_input_tokens": 61316,
      "output_tokens": 146,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4161,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 146,
          "cache_read_input_tokens": 61316,
          "cache_creation_input_tokens": 4161,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4161
          },
          "type": "message"
        }
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

_source line 46 · 2026-05-19T13:56:23.718Z_

<details open><summary>🔧 Tool call — Read · `toolu_01JA8kzAvVaSdEkq4UZutQfY`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "40871541-8257-4785-95cb-215e80cdc12f",
  "isSidechain": false,
  "requestId": "req_011CbC3TX5jmJ87xXARk35SE",
  "type": "assistant",
  "uuid": "09681f1f-3f0c-4fa2-8b67-03823c91cd75",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "a6ae7e35-390a-442a-93d4-9958c82c9e3b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AyR5Ldnzg5UHXW9e26zBYn",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4161,
      "cache_read_input_tokens": 61316,
      "output_tokens": 146,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4161,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 146,
          "cache_read_input_tokens": 61316,
          "cache_creation_input_tokens": 4161,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4161
          },
          "type": "message"
        }
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

_source line 47 · 2026-05-19T13:56:23.726Z_

<details><summary>↩ Tool result · `toolu_01JA8kzAvVaSdEkq4UZutQfY`</summary>

```text
1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	\label{sec:setup}
6	
7	\paragraph{Datasets.}
8	We evaluate on four English NER benchmarks spanning a difficulty gradient, each serving a distinct role.
9	\textbf{SciERC} \cite{luan2018scierc} (551 test instances, 6 entity types) is the primary medium-difficulty test bed where models achieve ${\approx}$65\% F1.
10	\textbf{Few-NERD} \cite{ding2021fewnerd} (INTRA coarse; 37{,}648 instances, 8 entity types, ${\approx}$75\% F1) provides a low-degeneracy contrast where LP selection succeeds (\S\ref{sec:fewnerd}).
11	\textbf{CoNLL-2003} \cite{tjongkimsang2003conll} (3{,}453 test sentences, 4 entity types, ${\approx}$91\% F1) serves as a ceiling-effect control where limited oracle headroom constrains selection gains.
12	\textbf{WNUT-17} \cite{derczynski2017wnut} (1{,}287 social media instances, 51\% zero F1) probes the signal-collapse boundary where model capability is insufficient.
13	
14	\paragraph{Models and sampling.}
15	\textbf{Qwen3-8B} and \textbf{LLaMA-3.1-8B-Instruct} are LoRA fine-tuned using LLaMA Factory \cite{zheng2024llamafactory} (training details in Appendix~\ref{app:training}; Few-NERD uses 3 epochs vs.\ 5 for others due to earlier convergence; Appendix~\ref{app:epoch_confound}).
16	We draw $N{=}8$ samples at $T{=}1.0$ (primary) with vLLM constrained decoding \cite{willard2023guided}, with $N{=}16$ for scaling experiments (Appendix~\ref{app:n_scaling}).
17	
18	%% ============================================================
19	\subsection{Quality Estimation Results}
20	\label{sec:qe_results}
21	
22	\begin{table*}[t]
23	\centering
24	\small
25	\caption{NER quality estimation ($\rho$ and AUROC; $N{=}8$, primary seed${=}42$; 3-seed stability $\sigma{\leq}0.026$ in Table~\ref{tab:multiseed}). Best in \textbf{bold}. RE results in Appendix~\ref{app:re_extension}. $N{=}16$ in Table~\ref{tab:robustness}.}
26	\label{tab:quality_estimation}
27	\begin{tabular}{ll cc cc cc}
28	\toprule
29	& & \multicolumn{2}{c}{\textbf{SciERC}} & \multicolumn{2}{c}{\textbf{CoNLL (Qwen)}} & \multicolumn{2}{c}{\textbf{CoNLL (LLaMA)}} \\
30	\cmidrule(lr){3-4} \cmidrule(lr){5-6} \cmidrule(lr){7-8}
31	Signal & Family & $\rho$ & AUC & $\rho$ & AUC & $\rho$ & AUC \\
32	\midrule
33	VC & Structural & \textbf{.379} & \textbf{.663} & .424 & .789 & .426 & .709 \\
34	SJ  & Structural & .360 & .650 & .436 & .801 & \textbf{.431} & .704 \\
35	FK & Surface & .267 & .602 & .400 & .774 & .428 & .703 \\
36	EM  & Surface    & .295 & .614 & \textbf{.451} & \textbf{.816} & \textbf{.431} & .705 \\
37	\midrule
38	LP     & Model      & .205 & .578 & .316 & .753 & .307 & \textbf{.761} \\
39	\bottomrule
40	\end{tabular}
41	\end{table*}
42	
43	Table~\ref{tab:quality_estimation} presents $\rho$ and AUROC for five signals across tasks and models ($\varepsilon$-free; $\varepsilon{=}0.05$ applies to selection only, stable across $[0, 0.2]$, Appendix~\ref{app:epsilon_robustness}).
44	
45	\paragraph{Signal rankings are difficulty-dependent.}
46	On SciERC (medium difficulty), structural signals lead (VC $\rho{=}0.379$, SJ $0.360$) over LP ($0.205$); bootstrap CIs confirm the gap ($\Delta\rho{=}{+}0.155$; Appendix~\ref{app:bootstrap_signal}).
47	On CoNLL (single-sample F1${\approx}$0.91), EM leads both $\rho$ and AUROC ($0.816$).
48	At the signal-collapse boundary (WNUT-17, macro F1${\approx}$42\%), full-set correlations are dominated by the zero/non-zero boundary (VC $\rho{=}0.724$ but conditional $\rho{=}0.038$; Table~\ref{tab:wnut}); LP shows the reverse (conditional $\rho{=}0.350$; Figure~\ref{fig:signal_heatmap}).
49	This collapse illustrates a regime where model capability is insufficient to produce meaningful inter-sample variation: 51\% of instances yield zero F1 across all samples, and consistency signals merely detect this floor rather than discriminating quality among non-trivial outputs.
50	
51	%% ============================================================
52	\subsection{The Correlation-Selection Gap}
53	\label{sec:selection_gap}
54	
55	Four of five signals (SJ, FK, EM, VC) assign identical scores to all candidates from the same input by construction (\S\ref{sec:formulation}); they can estimate quality across instances but cannot rank candidates within an instance.
56	The empirical question is whether LP, the sole per-sample signal, can exploit its candidate-discriminative nature for selection.
57	LP selection effectiveness is primarily determined by LP-quality alignment rather than degeneracy level (\S\ref{sec:discussion}).
58	Cross-instance $\rho$ (Table~\ref{tab:quality_estimation}) is attenuated by varying instance difficulty; within-instance $\rho$ directly measures whether LP discriminates candidates for a fixed input, making it the relevant predictor of selection success.
59	
60	\begin{table}[t]
61	\centering
62	\small
63	\caption{Best-of-$N$ NER selection (macro F1) on SciERC ($N{=}8$, $T{=}1.0$, 2-seed mean${\pm}\sigma$). LP is per-sample; others use consensus-proximity. Best non-oracle in \textbf{bold}. Non-tied subset in \S\ref{sec:discussion}; RE in Appendix~\ref{app:re_extension}. $^\dagger$Instance-level signals assign one score per input; per-sample ranking $p$-values are undefined.}
64	\label{tab:selection}
65	\begin{tabular}{lcc}
66	\toprule
67	Method & NER F1 & $p$ \\
68	\midrule
69	Oracle & $0.775 \pm 0.001$ & --- \\
70	Greedy ($T{=}0$) & $0.645 \pm 0.001$ & --- \\
71	\midrule
72	\multicolumn{3}{l}{\textit{Per-sample signal}} \\
73	LP           & $\mathbf{0.647} \pm 0.005$ & .29 \\
74	\midrule
75	\multicolumn{3}{l}{\textit{Instance-level signals (consensus-proximity selection)}} \\
76	SJ           & $0.646 \pm 0.002$ & .67 \\
77	FK           & $0.646 \pm 0.001$ & .79 \\
78	EM           & $0.637 \pm 0.001$ & n/a$^\dagger$ \\
79	VC           & $0.623 \pm 0.004$ & n/a$^\dagger$ \\
80	\midrule
81	Random           & $0.610 \pm 0.003$ & --- \\
82	\bottomrule
83	\end{tabular}
84	\end{table}
85	
86	\begin{figure}[t]
87	\centering
88	\includegraphics[width=\columnwidth]{fig_selection_gap}
89	\caption{The correlation-selection gap on SciERC ($N{=}8$, $T{=}1.0$). Bars: quality estimation $\rho$ (seed 42); line with error bars: $\Delta$F1 vs.\ greedy (3-seed mean, seeds 42/123/456). Despite $\rho$ up to 0.38, no signal significantly outperforms greedy (all $p{>}0.05$; Table~\ref{tab:selection}). Dashed green: oracle upper bound ($+13.1$~pp); dotted gray: random baseline.}
90	\label{fig:selection_gap}
91	\end{figure}
92	
93	Instance-level signals assign identical QE scores to all candidates; MBR conversion does not improve over greedy on the primary test bed (Table~\ref{tab:selection}; Figure~\ref{fig:selection_gap}).
94	Instance-level signals predict \textit{which inputs} the model handles reliably, not \textit{which output} is best.
95	
96	\paragraph{LP: the sole per-sample signal also fails.}
97	On SciERC ($n{=}529$, 2-seed sign tests\footnote{MDE${\approx}$1.5~pp at 80\% power ($n{=}529$); Few-NERD ($n{=}32{,}565$; MDE${\approx}$0.22~pp) provides the definitive test.}), the oracle (0.775) reveals 13.0~pp of headroom, but LP achieves $+0.2$~pp ($p{=}0.29$), below the MDE (${\approx}$1.5~pp); selection effects below this threshold cannot be reliably detected.
98	The pattern holds across CoNLL and WNUT-17 (Table~\ref{tab:cross_selection}); under stringent TOST anchors, some configurations show significant \textit{degradation} (Appendix~\ref{app:tost}).
99	Few-NERD provides the definitive contrast: LP achieves $+1.39$~pp ($p{<}0.001$) at low degeneracy (\S\ref{sec:fewnerd}), while structural signals still degrade selection.
100	
101	\paragraph{Qualitative factors governing selection effectiveness.}
102	Three factors qualitatively shape LP selection gains: (1)~\textit{instance degeneracy} compresses the candidate space, leaving fewer instances where any signal can improve over greedy (SciERC 17.8\%, CoNLL 48.4\%; Table~\ref{tab:fewnerd}); (2)~\textit{oracle headroom} bounds the maximum achievable gain (CoNLL ${\approx}2$\,pp vs.\ SciERC 13.1\,pp); (3)~\textit{LP-quality alignment}, measured as within-instance $\rho(\text{LP}, \text{F1})$, determines whether LP can discriminate candidates in the remaining non-degenerate instances (Few-NERD $\rho{\approx}0.5$--$0.7$ vs.\ SciERC $\rho{\approx}0.26$).
103	These factors are consistent with the observed pattern (Table~\ref{tab:fewnerd}): Few-NERD (low degeneracy, strong alignment) shows the largest LP gain ($+1.39$\,pp), SciERC (weak alignment) shows unreliable gains ($+0.04{\pm}0.48$\,pp, 3-seed; Table~\ref{tab:multiseed}), CoNLL (high degeneracy, minimal headroom) shows no gain, and WNUT-17 represents the signal-collapse boundary: LP $\rho{=}{-}0.446$ (the model assigns higher log-probabilities to confidently wrong outputs), within-instance alignment absent ($\rho{=}0.043$, n.s.), and construction ineffective ($p{>}0.05$, mixed sign) because 51\% of instances yield F1${=}0$.
104	Yet QE remains effective on WNUT-17 (VC $\rho{=}0.724$; Table~\ref{tab:wnut}), confirming QE-selection decoupling at this boundary.
105	This characterization is qualitative: the three factors do not combine into a predictive model ($R^2{<}0$ across 23 configurations), but each factor's role is individually supported by controlled ablations (\S\ref{sec:fewnerd}, \S\ref{sec:discussion}).
106	
107	%% ============================================================
108	\subsection{Cross-Dataset Contrast: Few-NERD}
109	\label{sec:fewnerd}
110	
111	\begin{table}[t]
112	\centering
113	\small
114	\caption{LP selection across datasets (Qwen3-8B, $N{=}8$, $T{=}1.0$, gold-filtered). Few-NERD/CoNLL: 3-seed means; SciERC: single-seed (3-seed in Table~\ref{tab:multiseed}). $p$: paired bootstrap.}
115	\label{tab:fewnerd}
116	\resizebox{\columnwidth}{!}{%
117	\begin{tabular}{@{}lrccccr@{}}
118	\toprule
119	Dataset & $n$ & Greedy & Degen.\% & LP $\rho$ & LP $\Delta$ & $p$ \\
120	\midrule
121	WNUT-17 & 1{,}287 & .452 & 67.9\% & $-$.446 & $-$0.45\,pp & .72 \\
122	CoNLL & 2{,}756 & .908 & 48.4\% & .302 & $-$0.85\,pp & 1.0 \\
123	SciERC & 529 & .644 & 17.8\% & .205 & $+$0.61\,pp & .193 \\
124	Few-NERD & 32{,}565 & .748 & 13.8\% & .220 & $\mathbf{+1.39}$\,pp & ${<}.001$ \\
125	\bottomrule
126	\end{tabular}}
127	\end{table}
128	
129	Few-NERD (Table~\ref{tab:fewnerd}) confirms LP selection at low degeneracy: $+1.39$~pp ($p{<}0.001$), while structural signals degrade selection (VC $-1.79$, SJ $-2.14$~pp). LP is 50$\times$ more seed-stable ($\sigma{=}0.04$ vs.\ SJ $2.02$~pp) and generalizes to LLaMA-3.1-8B (Table~\ref{tab:cross_selection}).
130	Training convergence modulates degeneracy: 5-epoch Few-NERD raises degeneracy to 31\% and halves LP gains (Appendix~\ref{app:epoch_confound}).
131	
132	\paragraph{Degeneracy alone does not predict LP selection direction.}
133	Across 23 configurations, degeneracy does not predict LP gain ($\rho{=}0.052$, $p{=}0.81$; Figure~\ref{fig:degeneracy_scatter}), though within fixed settings it causally modulates LP ($\rho{=}{-}0.881$; Appendix~\ref{app:per_type_lp}).
134	Cross-dataset prediction requires LP signal quality: Few-NERD ($\rho{\approx}0.5$--$0.7$) shows consistent gains, SciERC ($\rho{\approx}0.26$) does not (Appendix~\ref{app:conditional_decomp}).
135	
136	\begin{figure}[t]
137	\centering
138	\includegraphics[width=\columnwidth]{figures/fig_degeneracy_lp_scatter.pdf}
139	\caption{Instance degeneracy vs.\ LP selection gain across 23 configurations ($N{=}8$; $\rho{=}0.052$, $p{=}0.81$). Within Few-NERD per-entity-type analysis ($\rho{=}{-}0.881$; Appendix~\ref{app:per_type_lp}), degeneracy predicts LP gain when alignment is held constant.}
140	\label{fig:degeneracy_scatter}
141	\end{figure}
142	
143	Structural signals remain negative regardless of sample budget; $N$-scaling analyses are in Appendix~\ref{app:n_scaling}.
144	
145	%% ============================================================
146	\subsection{Robustness}
147	\label{sec:robustness_main}
148	
149	Consistency signals are robust across $T{\in}\{0.7, 1.0\}$ with sublinear $N$-scaling gains (Table~\ref{tab:robustness}); signal rankings are stable across seeds ($W{=}1.0$; Table~\ref{tab:ranking-stability}). NER calibration is reasonable (ECE 0.069--0.096; Appendix~\ref{app:calibration}).
150	
151	\begin{table}[t]
152	\centering
153	\small
154	\caption{Scale ablation: 8B vs.\ 4B QE $\rho$ ($N{=}8$, $T{=}1.0$, seed 42). RE in Appendix~\ref{app:re_extension}.}
155	\label{tab:scale_ablation}
156	\begin{tabular}{@{}ll cc r@{}}
157	\toprule
158	& & \textbf{8B} & \textbf{4B} & $\Delta$ \\
159	\midrule
160	CoNLL & SJ & .436 & .422 & $-$.014 \\
161	      & FK & .400 & .418 & $+$.018 \\
162	SciERC & SJ & .360 & .422 & $+$.062 \\
163	       & FK & .267 & .326 & $+$.059 \\
164	\bottomrule
165	\end{tabular}
166	\end{table}
167	
168	\paragraph{Scale robustness.}
169	With Qwen3-4B (Table~\ref{tab:scale_ablation}), QE is comparable (mean $|\Delta\rho|{=}0.042$), yet selection remains below greedy despite 13.0~pp headroom. Task difficulty is a stronger predictor than model scale within the 3B--8B range (Appendix~\ref{app:llama3b}).
170	Degeneracy scales with capability: 8B shows 17.8\% vs.\ 4B's 10.4\% on SciERC (Table~\ref{tab:degeneracy}).
171	
172	\paragraph{LoRA-rank ablation.}
173	LoRA rank${=}8$ (vs.\ 32) lowers degeneracy to 7.2\% but LP remains below greedy ($\rho(\text{LP}, \text{F1}){\approx}0.24$); temperature manipulation ($T{=}1.2$; \S\ref{sec:discussion}) confirms that low degeneracy and adequate alignment are independently necessary.
174	
175	\paragraph{Supervised signal combination and hidden probes.}
176	Supervised classifiers (LR, MLP, RF; 5-fold CV, $N{=}16$) and a DeBERTa-v3-base verifier all fail to close the selection gap (Appendix~\ref{app:supervised_combination}).
177	Hidden state probes improve correlation ($+37$\% on SciERC) but not selection (gap closure $-5.1$\%; Appendix~\ref{app:hidden_probe}); the bottleneck extends to model-internal representations.
178	
179	%% ============================================================
180	\subsection{Scaling Behavior}
181	\label{sec:scaling}
182	
183	We evaluate Qwen2.5-72B-Instruct in a zero-shot setting to test whether the gap persists at larger scale without fine-tuning.
184	
185	\begin{table}[t]
186	\centering
187	\small
188	\caption{Fine-tuned 8B vs.\ zero-shot 72B ($N{=}8$, $T{=}1.0$). Hdr.\ = oracle $-$ greedy (pp).}
189	\label{tab:scale_comparison}
190	\begin{tabular}{@{}llcccccc@{}}
191	\toprule
192	Dataset & Regime & Greedy & Hdr. & VC & SJ & FK & LP \\
193	\midrule
194	SciERC & 8B FT  & .645 & 13.0 & .379 & .360 & .267 & .205 \\
195	       & 72B ZS & .399 & 15.0 & .277 & .217 & .227 & .081 \\
196	\midrule
197	CoNLL  & 8B FT  & .908 & ${\approx}$2 & .424 & .436 & .400 & .302 \\
198	       & 72B ZS & .712 & 5.3  & .297 & .304 & .302 & $-$.002 \\
199	\bottomrule
200	\end{tabular}
201	\end{table}
202	
203	Zero-shot 72B produces lower greedy F1 but larger oracle headroom (Table~\ref{tab:scale_comparison}). LP $\rho$ drops from $0.205$ to $0.081$ on SciERC and from $0.302$ to near zero on CoNLL; LP selection fails in both datasets (SciERC $-0.1$~pp, CoNLL $-0.4$~pp), confirming that the gap is a structural property of the task rather than a fine-tuning artifact.
204	Structural signals remain positive but reduced (VC $\rho{=}0.277$ on SciERC, SJ $\rho{=}0.304$ on CoNLL). LP-weighted construction partially compensates on SciERC ($+1.5$\,pp, 41.4\% vs.\ 39.9\% greedy) but not on CoNLL ($-0.37$\,pp), where limited headroom (5.3~pp) leaves little room for aggregation.
205	
206	\textcolor{red}{TODO: (1) Add 72B fine-tuned results to determine whether fine-tuning at larger scale recovers signal quality. (2) Report degeneracy percentages for 72B zero-shot.}
207	
208	\begin{figure}[t]
209	\centering
210	% \includegraphics[width=\columnwidth]{figures/fig_scaling_curve.pdf}
211	\textcolor{red}{TODO: Scaling curve. X-axis: model scale (4B, 8B, 72B). Panels: (a) greedy/oracle F1 and headroom, (b) signal $\rho$. Separate lines for fine-tuned vs.\ zero-shot.}
212	\caption{\textcolor{red}{TODO: Signal quality and oracle headroom across model scales.}}
213	\label{fig:scaling_curve}
214	\end{figure}
215	
216	%% ============================================================
217	\subsection{Prescriptive Results}
218	\label{sec:prescriptive}
219	
220	The preceding sections establish that instance-level selection fails for structured IE. We now present two approaches that extract value from multi-sample generation without relying on sample ranking.
221	
222	\paragraph{Entity-level construction.}
223	Rather than selecting one of $N$ complete outputs, we aggregate entities across all samples, retaining those exceeding a confirmation threshold $\theta{=}2/N$ (${\geq}2$ of $N$ samples), with LP-weighted or uniform frequency scoring. Under fine-tuning, this default achieves the best or near-best F1 across all datasets ($\theta$ stable within $[0.15, 0.35]$; Appendix~\ref{app:theta_sweep}). In the zero-shot regime, uniform voting degrades (SciERC $-0.52$\,pp, CoNLL $-0.92$\,pp) because greater output diversity admits noise entities; LP-weighting is necessary for construction to succeed without fine-tuning (SciERC $+1.5$\,pp; \S\ref{sec:scaling}).
224	
225	\begin{table}[t]
226	\centering
227	\small
228	\caption{Entity construction vs.\ greedy ($\Delta$ macro F1; $N{=}8$, $T{=}1.0$, Qwen3-8B, multi-seed mean${\pm}\sigma$). $\theta{=}2/N$. $p$: paired bootstrap vs.\ greedy. Best in \textbf{bold}.}
229	\label{tab:entity_construction}
230	\resizebox{\columnwidth}{!}{%
231	\begin{tabular}{@{}llcccc@{}}
232	\toprule
233	Dataset & Wt. & Greedy & Constr. & $\Delta$ & $p$ \\
234	\midrule
235	SciERC & LP & $.646{\pm}.002$ & $\mathbf{.656{\pm}.003}$ & $+1.02{\pm}0.49$\,pp & .004 \\
236	       & Unif. & $.646{\pm}.002$ & $.653{\pm}.006$ & $+0.74{\pm}0.71$\,pp & .023 \\
237	\addlinespace
238	Few-NERD & LP & $.748$ & $\mathbf{.762{\pm}.005}$ & $+1.40{\pm}0.51$\,pp & ${<}.001$ \\
239	         & Unif. & $.748$ & $.756{\pm}.006$ & $+0.74{\pm}0.58$\,pp & .003 \\
240	\addlinespace
241	CoNLL & Unif. & .908 & .904 & $-0.39$\,pp & n.s. \\
242	\bottomrule
243	\end{tabular}}
244	\end{table}
245	
246	LP-weighted construction improves over greedy on Few-NERD ($+1.40{\pm}0.51$\,pp, $p{<}0.001$) and SciERC ($+1.02{\pm}0.49$\,pp, $p{=}0.004$; Table~\ref{tab:entity_construction}), positive across all 7 seed-dataset combinations, recovering ${\approx}$8\% (SciERC) and 11\% (Few-NERD) of oracle headroom. CoNLL shows no gain ($-0.39$\,pp), consistent with ceiling-regime degeneracy. The mechanism is recall-driven: aggregating low-frequency correct entities recovers mentions that no single sample captures ($N$-scaling in Appendix~\ref{app:n_scaling}).
247	
248	\paragraph{LP-alignment gating (preliminary diagnostic).}
249	Construction and LP selection are complementary: construction dominates on SciERC ($+1.02$\,pp vs.\ LP $+0.04{\pm}0.48$\,pp, n.s.; $\rho{\approx}0.2$), while on Few-NERD both yield comparable gains ($+1.40$ vs.\ $+1.39$\,pp; $\rho{\approx}0.5$--$0.7$).
250	We estimate within-instance $\rho(\text{LP}, \text{F1})$ on 50 held-out instances with bootstrap CIs (1000 resamples). Degeneracy-adjusted $\rho_{\text{adj}}$: Few-NERD $0.516$ [0.459, 0.759], SciERC $0.167$ [0.146, 0.281], CoNLL $0.065$ [$-$0.061, 0.620], WNUT-17 ${\approx}0$ (n.s.).
251	The protocol performs three-way routing: (1)~$\rho_{\text{adj}} \geq \tau{=}0.3$: apply LP selection; (2)~$\rho_{\text{adj}} < \tau$ and construction shows positive dev-set gain: apply construction; (3)~otherwise: retain greedy decoding.
252	This routes Few-NERD to LP selection ($+1.39$\,pp); SciERC, CoNLL, and WNUT-17 fall below $\tau$ and route to greedy. The conservative protocol trades SciERC's missed construction gain ($+1.02$\,pp) for protection against negative outcomes (CoNLL $-0.39$\,pp, WNUT-17 n.s.).
253	Routing is stable across $\tau{\in}[0.2, 0.4]$ and matches test-set direction for all four datasets; narrower inter-dataset margins remain untested.
254	
255	\paragraph{Selective prediction.}
256	Orthogonal to construction, QE signals support selective prediction: at 80\% coverage, filtering low-confidence instances yields $+5$--$8$\,pp F1 (AUPRC 0.70--0.92; Table~\ref{tab:cross_selection}).
257	
258	\phantomsection\label{sec:selection_results}
259	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "09681f1f-3f0c-4fa2-8b67-03823c91cd75",
  "isSidechain": false,
  "promptId": "2279f609-b135-4e34-8568-a1f529688be0",
  "type": "user",
  "uuid": "b6f31cd4-59b5-4ca6-8ec0-36dd5914a77d",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex",
      "content": "\\section{Experiments}\n\\label{sec:experiments}\n\n\\subsection{Experimental Setup}\n\\label{sec:setup}\n\n\\paragraph{Datasets.}\nWe evaluate on four English NER benchmarks spanning a difficulty gradient, each serving a distinct role.\n\\textbf{SciERC} \\cite{luan2018scierc} (551 test instances, 6 entity types) is the primary medium-difficulty test bed where models achieve ${\\approx}$65\\% F1.\n\\textbf{Few-NERD} \\cite{ding2021fewnerd} (INTRA coarse; 37{,}648 instances, 8 entity types, ${\\approx}$75\\% F1) provides a low-degeneracy contrast where LP selection succeeds (\\S\\ref{sec:fewnerd}).\n\\textbf{CoNLL-2003} \\cite{tjongkimsang2003conll} (3{,}453 test sentences, 4 entity types, ${\\approx}$91\\% F1) serves as a ceiling-effect control where limited oracle headroom constrains selection gains.\n\\textbf{WNUT-17} \\cite{derczynski2017wnut} (1{,}287 social media instances, 51\\% zero F1) probes the signal-collapse boundary where model capability is insufficient.\n\n\\paragraph{Models and sampling.}\n\\textbf{Qwen3-8B} and \\textbf{LLaMA-3.1-8B-Instruct} are LoRA fine-tuned using LLaMA Factory \\cite{zheng2024llamafactory} (training details in Appendix~\\ref{app:training}; Few-NERD uses 3 epochs vs.\\ 5 for others due to earlier convergence; Appendix~\\ref{app:epoch_confound}).\nWe draw $N{=}8$ samples at $T{=}1.0$ (primary) with vLLM constrained decoding \\cite{willard2023guided}, with $N{=}16$ for scaling experiments (Appendix~\\ref{app:n_scaling}).\n\n%% ============================================================\n\\subsection{Quality Estimation Results}\n\\label{sec:qe_results}\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\caption{NER quality estimation ($\\rho$ and AUROC; $N{=}8$, primary seed${=}42$; 3-seed stability $\\sigma{\\leq}0.026$ in Table~\\ref{tab:multiseed}). Best in \\textbf{bold}. RE results in Appendix~\\ref{app:re_extension}. $N{=}16$ in Table~\\ref{tab:robustness}.}\n\\label{tab:quality_estimation}\n\\begin{tabular}{ll cc cc cc}\n\\toprule\n& & \\multicolumn{2}{c}{\\textbf{SciERC}} & \\multicolumn{2}{c}{\\textbf{CoNLL (Qwen)}} & \\multicolumn{2}{c}{\\textbf{CoNLL (LLaMA)}} \\\\\n\\cmidrule(lr){3-4} \\cmidrule(lr){5-6} \\cmidrule(lr){7-8}\nSignal & Family & $\\rho$ & AUC & $\\rho$ & AUC & $\\rho$ & AUC \\\\\n\\midrule\nVC & Structural & \\textbf{.379} & \\textbf{.663} & .424 & .789 & .426 & .709 \\\\\nSJ  & Structural & .360 & .650 & .436 & .801 & \\textbf{.431} & .704 \\\\\nFK & Surface & .267 & .602 & .400 & .774 & .428 & .703 \\\\\nEM  & Surface    & .295 & .614 & \\textbf{.451} & \\textbf{.816} & \\textbf{.431} & .705 \\\\\n\\midrule\nLP     & Model      & .205 & .578 & .316 & .753 & .307 & \\textbf{.761} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\nTable~\\ref{tab:quality_estimation} presents $\\rho$ and AUROC for five signals across tasks and models ($\\varepsilon$-free; $\\varepsilon{=}0.05$ applies to selection only, stable across $[0, 0.2]$, Appendix~\\ref{app:epsilon_robustness}).\n\n\\paragraph{Signal rankings are difficulty-dependent.}\nOn SciERC (medium difficulty), structural signals lead (VC $\\rho{=}0.379$, SJ $0.360$) over LP ($0.205$); bootstrap CIs confirm the gap ($\\Delta\\rho{=}{+}0.155$; Appendix~\\ref{app:bootstrap_signal}).\nOn CoNLL (single-sample F1${\\approx}$0.91), EM leads both $\\rho$ and AUROC ($0.816$).\nAt the signal-collapse boundary (WNUT-17, macro F1${\\approx}$42\\%), full-set correlations are dominated by the zero/non-zero boundary (VC $\\rho{=}0.724$ but conditional $\\rho{=}0.038$; Table~\\ref{tab:wnut}); LP shows the reverse (conditional $\\rho{=}0.350$; Figure~\\ref{fig:signal_heatmap}).\nThis collapse illustrates a regime where model capability is insufficient to produce meaningful inter-sample variation: 51\\% of instances yield zero F1 across all samples, and consistency signals merely detect this floor rather than discriminating quality among non-trivial outputs.\n\n%% ============================================================\n\\subsection{The Correlation-Selection Gap}\n\\label{sec:selection_gap}\n\nFour of five signals (SJ, FK, EM, VC) assign identical scores to all candidates from the same input by construction (\\S\\ref{sec:formulation}); they can estimate quality across instances but cannot rank candidates within an instance.\nThe empirical question is whether LP, the sole per-sample signal, can exploit its candidate-discriminative nature for selection.\nLP selection effectiveness is primarily determined by LP-quality alignment rather than degeneracy level (\\S\\ref{sec:discussion}).\nCross-instance $\\rho$ (Table~\\ref{tab:quality_estimation}) is attenuated by varying instance difficulty; within-instance $\\rho$ directly measures whether LP discriminates candidates for a fixed input, making it the relevant predictor of selection success.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Best-of-$N$ NER selection (macro F1) on SciERC ($N{=}8$, $T{=}1.0$, 2-seed mean${\\pm}\\sigma$). LP is per-sample; others use consensus-proximity. Best non-oracle in \\textbf{bold}. Non-tied subset in \\S\\ref{sec:discussion}; RE in Appendix~\\ref{app:re_extension}. $^\\dagger$Instance-level signals assign one score per input; per-sample ranking $p$-values are undefined.}\n\\label{tab:selection}\n\\begin{tabular}{lcc}\n\\toprule\nMethod & NER F1 & $p$ \\\\\n\\midrule\nOracle & $0.775 \\pm 0.001$ & --- \\\\\nGreedy ($T{=}0$) & $0.645 \\pm 0.001$ & --- \\\\\n\\midrule\n\\multicolumn{3}{l}{\\textit{Per-sample signal}} \\\\\nLP           & $\\mathbf{0.647} \\pm 0.005$ & .29 \\\\\n\\midrule\n\\multicolumn{3}{l}{\\textit{Instance-level signals (consensus-proximity selection)}} \\\\\nSJ           & $0.646 \\pm 0.002$ & .67 \\\\\nFK           & $0.646 \\pm 0.001$ & .79 \\\\\nEM           & $0.637 \\pm 0.001$ & n/a$^\\dagger$ \\\\\nVC           & $0.623 \\pm 0.004$ & n/a$^\\dagger$ \\\\\n\\midrule\nRandom           & $0.610 \\pm 0.003$ & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig_selection_gap}\n\\caption{The correlation-selection gap on SciERC ($N{=}8$, $T{=}1.0$). Bars: quality estimation $\\rho$ (seed 42); line with error bars: $\\Delta$F1 vs.\\ greedy (3-seed mean, seeds 42/123/456). Despite $\\rho$ up to 0.38, no signal significantly outperforms greedy (all $p{>}0.05$; Table~\\ref{tab:selection}). Dashed green: oracle upper bound ($+13.1$~pp); dotted gray: random baseline.}\n\\label{fig:selection_gap}\n\\end{figure}\n\nInstance-level signals assign identical QE scores to all candidates; MBR conversion does not improve over greedy on the primary test bed (Table~\\ref{tab:selection}; Figure~\\ref{fig:selection_gap}).\nInstance-level signals predict \\textit{which inputs} the model handles reliably, not \\textit{which output} is best.\n\n\\paragraph{LP: the sole per-sample signal also fails.}\nOn SciERC ($n{=}529$, 2-seed sign tests\\footnote{MDE${\\approx}$1.5~pp at 80\\% power ($n{=}529$); Few-NERD ($n{=}32{,}565$; MDE${\\approx}$0.22~pp) provides the definitive test.}), the oracle (0.775) reveals 13.0~pp of headroom, but LP achieves $+0.2$~pp ($p{=}0.29$), below the MDE (${\\approx}$1.5~pp); selection effects below this threshold cannot be reliably detected.\nThe pattern holds across CoNLL and WNUT-17 (Table~\\ref{tab:cross_selection}); under stringent TOST anchors, some configurations show significant \\textit{degradation} (Appendix~\\ref{app:tost}).\nFew-NERD provides the definitive contrast: LP achieves $+1.39$~pp ($p{<}0.001$) at low degeneracy (\\S\\ref{sec:fewnerd}), while structural signals still degrade selection.\n\n\\paragraph{Qualitative factors governing selection effectiveness.}\nThree factors qualitatively shape LP selection gains: (1)~\\textit{instance degeneracy} compresses the candidate space, leaving fewer instances where any signal can improve over greedy (SciERC 17.8\\%, CoNLL 48.4\\%; Table~\\ref{tab:fewnerd}); (2)~\\textit{oracle headroom} bounds the maximum achievable gain (CoNLL ${\\approx}2$\\,pp vs.\\ SciERC 13.1\\,pp); (3)~\\textit{LP-quality alignment}, measured as within-instance $\\rho(\\text{LP}, \\text{F1})$, determines whether LP can discriminate candidates in the remaining non-degenerate instances (Few-NERD $\\rho{\\approx}0.5$--$0.7$ vs.\\ SciERC $\\rho{\\approx}0.26$).\nThese factors are consistent with the observed pattern (Table~\\ref{tab:fewnerd}): Few-NERD (low degeneracy, strong alignment) shows the largest LP gain ($+1.39$\\,pp), SciERC (weak alignment) shows unreliable gains ($+0.04{\\pm}0.48$\\,pp, 3-seed; Table~\\ref{tab:multiseed}), CoNLL (high degeneracy, minimal headroom) shows no gain, and WNUT-17 represents the signal-collapse boundary: LP $\\rho{=}{-}0.446$ (the model assigns higher log-probabilities to confidently wrong outputs), within-instance alignment absent ($\\rho{=}0.043$, n.s.), and construction ineffective ($p{>}0.05$, mixed sign) because 51\\% of instances yield F1${=}0$.\nYet QE remains effective on WNUT-17 (VC $\\rho{=}0.724$; Table~\\ref{tab:wnut}), confirming QE-selection decoupling at this boundary.\nThis characterization is qualitative: the three factors do not combine into a predictive model ($R^2{<}0$ across 23 configurations), but each factor's role is individually supported by controlled ablations (\\S\\ref{sec:fewnerd}, \\S\\ref{sec:discussion}).\n\n%% ============================================================\n\\subsection{Cross-Dataset Contrast: Few-NERD}\n\\label{sec:fewnerd}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{LP selection across datasets (Qwen3-8B, $N{=}8$, $T{=}1.0$, gold-filtered). Few-NERD/CoNLL: 3-seed means; SciERC: single-seed (3-seed in Table~\\ref{tab:multiseed}). $p$: paired bootstrap.}\n\\label{tab:fewnerd}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}lrccccr@{}}\n\\toprule\nDataset & $n$ & Greedy & Degen.\\% & LP $\\rho$ & LP $\\Delta$ & $p$ \\\\\n\\midrule\nWNUT-17 & 1{,}287 & .452 & 67.9\\% & $-$.446 & $-$0.45\\,pp & .72 \\\\\nCoNLL & 2{,}756 & .908 & 48.4\\% & .302 & $-$0.85\\,pp & 1.0 \\\\\nSciERC & 529 & .644 & 17.8\\% & .205 & $+$0.61\\,pp & .193 \\\\\nFew-NERD & 32{,}565 & .748 & 13.8\\% & .220 & $\\mathbf{+1.39}$\\,pp & ${<}.001$ \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\nFew-NERD (Table~\\ref{tab:fewnerd}) confirms LP selection at low degeneracy: $+1.39$~pp ($p{<}0.001$), while structural signals degrade selection (VC $-1.79$, SJ $-2.14$~pp). LP is 50$\\times$ more seed-stable ($\\sigma{=}0.04$ vs.\\ SJ $2.02$~pp) and generalizes to LLaMA-3.1-8B (Table~\\ref{tab:cross_selection}).\nTraining convergence modulates degeneracy: 5-epoch Few-NERD raises degeneracy to 31\\% and halves LP gains (Appendix~\\ref{app:epoch_confound}).\n\n\\paragraph{Degeneracy alone does not predict LP selection direction.}\nAcross 23 configurations, degeneracy does not predict LP gain ($\\rho{=}0.052$, $p{=}0.81$; Figure~\\ref{fig:degeneracy_scatter}), though within fixed settings it causally modulates LP ($\\rho{=}{-}0.881$; Appendix~\\ref{app:per_type_lp}).\nCross-dataset prediction requires LP signal quality: Few-NERD ($\\rho{\\approx}0.5$--$0.7$) shows consistent gains, SciERC ($\\rho{\\approx}0.26$) does not (Appendix~\\ref{app:conditional_decomp}).\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_degeneracy_lp_scatter.pdf}\n\\caption{Instance degeneracy vs.\\ LP selection gain across 23 configurations ($N{=}8$; $\\rho{=}0.052$, $p{=}0.81$). Within Few-NERD per-entity-type analysis ($\\rho{=}{-}0.881$; Appendix~\\ref{app:per_type_lp}), degeneracy predicts LP gain when alignment is held constant.}\n\\label{fig:degeneracy_scatter}\n\\end{figure}\n\nStructural signals remain negative regardless of sample budget; $N$-scaling analyses are in Appendix~\\ref{app:n_scaling}.\n\n%% ============================================================\n\\subsection{Robustness}\n\\label{sec:robustness_main}\n\nConsistency signals are robust across $T{\\in}\\{0.7, 1.0\\}$ with sublinear $N$-scaling gains (Table~\\ref{tab:robustness}); signal rankings are stable across seeds ($W{=}1.0$; Table~\\ref{tab:ranking-stability}). NER calibration is reasonable (ECE 0.069--0.096; Appendix~\\ref{app:calibration}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Scale ablation: 8B vs.\\ 4B QE $\\rho$ ($N{=}8$, $T{=}1.0$, seed 42). RE in Appendix~\\ref{app:re_extension}.}\n\\label{tab:scale_ablation}\n\\begin{tabular}{@{}ll cc r@{}}\n\\toprule\n& & \\textbf{8B} & \\textbf{4B} & $\\Delta$ \\\\\n\\midrule\nCoNLL & SJ & .436 & .422 & $-$.014 \\\\\n      & FK & .400 & .418 & $+$.018 \\\\\nSciERC & SJ & .360 & .422 & $+$.062 \\\\\n       & FK & .267 & .326 & $+$.059 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Scale robustness.}\nWith Qwen3-4B (Table~\\ref{tab:scale_ablation}), QE is comparable (mean $|\\Delta\\rho|{=}0.042$), yet selection remains below greedy despite 13.0~pp headroom. Task difficulty is a stronger predictor than model scale within the 3B--8B range (Appendix~\\ref{app:llama3b}).\nDegeneracy scales with capability: 8B shows 17.8\\% vs.\\ 4B's 10.4\\% on SciERC (Table~\\ref{tab:degeneracy}).\n\n\\paragraph{LoRA-rank ablation.}\nLoRA rank${=}8$ (vs.\\ 32) lowers degeneracy to 7.2\\% but LP remains below greedy ($\\rho(\\text{LP}, \\text{F1}){\\approx}0.24$); temperature manipulation ($T{=}1.2$; \\S\\ref{sec:discussion}) confirms that low degeneracy and adequate alignment are independently necessary.\n\n\\paragraph{Supervised signal combination and hidden probes.}\nSupervised classifiers (LR, MLP, RF; 5-fold CV, $N{=}16$) and a DeBERTa-v3-base verifier all fail to close the selection gap (Appendix~\\ref{app:supervised_combination}).\nHidden state probes improve correlation ($+37$\\% on SciERC) but not selection (gap closure $-5.1$\\%; Appendix~\\ref{app:hidden_probe}); the bottleneck extends to model-internal representations.\n\n%% ============================================================\n\\subsection{Scaling Behavior}\n\\label{sec:scaling}\n\nWe evaluate Qwen2.5-72B-Instruct in a zero-shot setting to test whether the gap persists at larger scale without fine-tuning.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Fine-tuned 8B vs.\\ zero-shot 72B ($N{=}8$, $T{=}1.0$). Hdr.\\ = oracle $-$ greedy (pp).}\n\\label{tab:scale_comparison}\n\\begin{tabular}{@{}llcccccc@{}}\n\\toprule\nDataset & Regime & Greedy & Hdr. & VC & SJ & FK & LP \\\\\n\\midrule\nSciERC & 8B FT  & .645 & 13.0 & .379 & .360 & .267 & .205 \\\\\n       & 72B ZS & .399 & 15.0 & .277 & .217 & .227 & .081 \\\\\n\\midrule\nCoNLL  & 8B FT  & .908 & ${\\approx}$2 & .424 & .436 & .400 & .302 \\\\\n       & 72B ZS & .712 & 5.3  & .297 & .304 & .302 & $-$.002 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nZero-shot 72B produces lower greedy F1 but larger oracle headroom (Table~\\ref{tab:scale_comparison}). LP $\\rho$ drops from $0.205$ to $0.081$ on SciERC and from $0.302$ to near zero on CoNLL; LP selection fails in both datasets (SciERC $-0.1$~pp, CoNLL $-0.4$~pp), confirming that the gap is a structural property of the task rather than a fine-tuning artifact.\nStructural signals remain positive but reduced (VC $\\rho{=}0.277$ on SciERC, SJ $\\rho{=}0.304$ on CoNLL). LP-weighted construction partially compensates on SciERC ($+1.5$\\,pp, 41.4\\% vs.\\ 39.9\\% greedy) but not on CoNLL ($-0.37$\\,pp), where limited headroom (5.3~pp) leaves little room for aggregation.\n\n\\textcolor{red}{TODO: (1) Add 72B fine-tuned results to determine whether fine-tuning at larger scale recovers signal quality. (2) Report degeneracy percentages for 72B zero-shot.}\n\n\\begin{figure}[t]\n\\centering\n% \\includegraphics[width=\\columnwidth]{figures/fig_scaling_curve.pdf}\n\\textcolor{red}{TODO: Scaling curve. X-axis: model scale (4B, 8B, 72B). Panels: (a) greedy/oracle F1 and headroom, (b) signal $\\rho$. Separate lines for fine-tuned vs.\\ zero-shot.}\n\\caption{\\textcolor{red}{TODO: Signal quality and oracle headroom across model scales.}}\n\\label{fig:scaling_curve}\n\\end{figure}\n\n%% ============================================================\n\\subsection{Prescriptive Results}\n\\label{sec:prescriptive}\n\nThe preceding sections establish that instance-level selection fails for structured IE. We now present two approaches that extract value from multi-sample generation without relying on sample ranking.\n\n\\paragraph{Entity-level construction.}\nRather than selecting one of $N$ complete outputs, we aggregate entities across all samples, retaining those exceeding a confirmation threshold $\\theta{=}2/N$ (${\\geq}2$ of $N$ samples), with LP-weighted or uniform frequency scoring. Under fine-tuning, this default achieves the best or near-best F1 across all datasets ($\\theta$ stable within $[0.15, 0.35]$; Appendix~\\ref{app:theta_sweep}). In the zero-shot regime, uniform voting degrades (SciERC $-0.52$\\,pp, CoNLL $-0.92$\\,pp) because greater output diversity admits noise entities; LP-weighting is necessary for construction to succeed without fine-tuning (SciERC $+1.5$\\,pp; \\S\\ref{sec:scaling}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Entity construction vs.\\ greedy ($\\Delta$ macro F1; $N{=}8$, $T{=}1.0$, Qwen3-8B, multi-seed mean${\\pm}\\sigma$). $\\theta{=}2/N$. $p$: paired bootstrap vs.\\ greedy. Best in \\textbf{bold}.}\n\\label{tab:entity_construction}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}llcccc@{}}\n\\toprule\nDataset & Wt. & Greedy & Constr. & $\\Delta$ & $p$ \\\\\n\\midrule\nSciERC & LP & $.646{\\pm}.002$ & $\\mathbf{.656{\\pm}.003}$ & $+1.02{\\pm}0.49$\\,pp & .004 \\\\\n       & Unif. & $.646{\\pm}.002$ & $.653{\\pm}.006$ & $+0.74{\\pm}0.71$\\,pp & .023 \\\\\n\\addlinespace\nFew-NERD & LP & $.748$ & $\\mathbf{.762{\\pm}.005}$ & $+1.40{\\pm}0.51$\\,pp & ${<}.001$ \\\\\n         & Unif. & $.748$ & $.756{\\pm}.006$ & $+0.74{\\pm}0.58$\\,pp & .003 \\\\\n\\addlinespace\nCoNLL & Unif. & .908 & .904 & $-0.39$\\,pp & n.s. \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\nLP-weighted construction improves over greedy on Few-NERD ($+1.40{\\pm}0.51$\\,pp, $p{<}0.001$) and SciERC ($+1.02{\\pm}0.49$\\,pp, $p{=}0.004$; Table~\\ref{tab:entity_construction}), positive across all 7 seed-dataset combinations, recovering ${\\approx}$8\\% (SciERC) and 11\\% (Few-NERD) of oracle headroom. CoNLL shows no gain ($-0.39$\\,pp), consistent with ceiling-regime degeneracy. The mechanism is recall-driven: aggregating low-frequency correct entities recovers mentions that no single sample captures ($N$-scaling in Appendix~\\ref{app:n_scaling}).\n\n\\paragraph{LP-alignment gating (preliminary diagnostic).}\nConstruction and LP selection are complementary: construction dominates on SciERC ($+1.02$\\,pp vs.\\ LP $+0.04{\\pm}0.48$\\,pp, n.s.; $\\rho{\\approx}0.2$), while on Few-NERD both yield comparable gains ($+1.40$ vs.\\ $+1.39$\\,pp; $\\rho{\\approx}0.5$--$0.7$).\nWe estimate within-instance $\\rho(\\text{LP}, \\text{F1})$ on 50 held-out instances with bootstrap CIs (1000 resamples). Degeneracy-adjusted $\\rho_{\\text{adj}}$: Few-NERD $0.516$ [0.459, 0.759], SciERC $0.167$ [0.146, 0.281], CoNLL $0.065$ [$-$0.061, 0.620], WNUT-17 ${\\approx}0$ (n.s.).\nThe protocol performs three-way routing: (1)~$\\rho_{\\text{adj}} \\geq \\tau{=}0.3$: apply LP selection; (2)~$\\rho_{\\text{adj}} < \\tau$ and construction shows positive dev-set gain: apply construction; (3)~otherwise: retain greedy decoding.\nThis routes Few-NERD to LP selection ($+1.39$\\,pp); SciERC, CoNLL, and WNUT-17 fall below $\\tau$ and route to greedy. The conservative protocol trades SciERC's missed construction gain ($+1.02$\\,pp) for protection against negative outcomes (CoNLL $-0.39$\\,pp, WNUT-17 n.s.).\nRouting is stable across $\\tau{\\in}[0.2, 0.4]$ and matches test-set direction for all four datasets; narrower inter-dataset margins remain untested.\n\n\\paragraph{Selective prediction.}\nOrthogonal to construction, QE signals support selective prediction: at 80\\% coverage, filtering low-confidence instances yields $+5$--$8$\\,pp F1 (AUPRC 0.70--0.92; Table~\\ref{tab:cross_selection}).\n\n\\phantomsection\\label{sec:selection_results}\n",
      "numLines": 259,
      "startLine": 1,
      "totalLines": 259
    }
  },
  "sourceToolAssistantUUID": "09681f1f-3f0c-4fa2-8b67-03823c91cd75",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "a6ae7e35-390a-442a-93d4-9958c82c9e3b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 48_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[System 触发审查]: 收到你的 critical 审查报告，6 个数据一致性问题全部确认。已派 Agent 紧急调查修复。  请你重点关注 P0-1 SciERC AUROC 问题：如果 EM AUROC 确实是 0.749 而非 0.614，论文中以下叙述可能需要修改： 1. Table 1 信号排序结论（EM 可能超过 VC 成为 SciERC 最高 AUROC） 2. 正文中关于\"s…",
  "leafUuid": "b6f31cd4-59b5-4ca6-8ec0-36dd5914a77d",
  "sessionId": "a6ae7e35-390a-442a-93d4-9958c82c9e3b"
}
```

---

### Runtime record

_source line 49_

```json
{
  "type": "ai-title",
  "aiTitle": "Verify SciERC AUROC data consistency issues",
  "sessionId": "a6ae7e35-390a-442a-93d4-9958c82c9e3b"
}
```

---

### Assistant

_source line 50 · 2026-05-19T13:57:10.533Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a comprehensive picture. Let me also check the discussion section for degeneracy-related claims and the appendix for N=8/N=16 data.

Key observations so far:

1. **P0-1 SciERC AUROC**: The paper Table 1 shows EM AUROC = .614 on SciERC, but exp_012_rerun_1024 has EM AUROC = 0.7493. The provenance c002 already knows this: "EM leads AUROC (NER 0.749, RE 0.706) while Voting leads ρ (NER 0.379, RE 0.422)". 

The provenance was updated but the paper table wasn't. This completely flips the SciERC AUROC ranking—EM jumps from third place to first, and SJ overtakes VC, which fundamentally changes the signal ranking the paper presents.

2. **Narrative impact**: The text on line 46 says "On SciERC (medium difficulty), structural signals lead (VC ρ=0.379, SJ 0.360) over LP (0.205)". The rho values are actually correct from the updated experiment, but the table bolds VC's AUROC (.663) as if it's the best signal. If I correct the AUROC values, VC would still lead on rho (.379 > .360 > .295 > .267 > .205), but EM would dominate AUROC (.749 > .692 > .684 > .629 > .578)—a ρ-AUROC dissociation the paper doesn't address.

3. **Source of the error**: The provenance tab shows the AUROC values are coming from exp_015_v2, not the corrected exp_012.

The provenance note acknowledges the correction was made (VC AUROC changed from .741 to .684), but the paper still displays .663, which doesn't match either the old experiment (.728) or the corrected one (.684). I'm trying to trace where .663 actually comes from—it doesn't appear in any of the experiments I'm looking at.

Checking exp_015_metrics_expansion more closely, the values are close to what's in the paper but not exact matches. The provenance for exp_012_rerun_1024 shows voting_auroc should be .684 and em_auroc should be .749, yet the paper has .663 and .614 respectively. These numbers seem to come from a source I haven't identified yet.

For the CoNLL degeneracy issue, the paper's table shows 48.4% at N=8, but exp_002_conll_n16 has a degeneracy rate of 0.4844 — which is from N=16 data. This suggests the paper might have mixed up results from different experimental runs, reporting N=16 metrics under the N=8 label.

Now I'm trying to figure out the actual relationship between sample size and degeneracy — whether higher N makes it harder or easier for all samples to agree depends on how degeneracy is defined, and that's affecting how I interpret whether this mismatch is actually an error.

But there's a smoking gun: exp_030 was explicitly killed with a note about N-inconsistency (N=8 vs N=16), which confirms there was a known mixing issue in the experiments. The real question is whether that contamination made it into the published results. Looking at the paper's CoNLL line, the n=2756 and 48.4% degeneracy match what I'd expect from exp_002, and the EM metrics align with the N=8 experiment, so it seems the right data was used — but I need to verify this isn't masking a deeper problem.

I'm realizing the SciERC AUROC discrepancies might be systematic across the board, not isolated to one metric, which would suggest a more fundamental issue with how those results were reported. Let me pull the exact degeneracy rates from both the N=8 and N=16 versions to confirm what actually went into the paper, then I can assess the full scope of what needs to be flagged.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b6f31cd4-59b5-4ca6-8ec0-36dd5914a77d",
  "isSidechain": false,
  "requestId": "req_011CbC3TnAbUGWHJNhy3GhjX",
  "type": "assistant",
  "uuid": "7968492a-f8f7-4d0c-8ef0-fd7c004946a8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "a6ae7e35-390a-442a-93d4-9958c82c9e3b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0177Vnan7hSoG4fg6Kzo9J6X",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8018,
      "cache_read_input_tokens": 65477,
      "output_tokens": 2437,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 8018,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2437,
          "cache_read_input_tokens": 65477,
          "cache_creation_input_tokens": 8018,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 8018
          },
          "type": "message"
        }
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

_source line 51 · 2026-05-19T13:57:10.884Z_

发现更大的问题：不仅 EM AUROC 错，SciERC 所有 AUROC 值都可能是错的。同时发现 CoNLL degeneracy 48.4% 可能来自 N=16 实验。需要进一步核实。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7968492a-f8f7-4d0c-8ef0-fd7c004946a8",
  "isSidechain": false,
  "requestId": "req_011CbC3TnAbUGWHJNhy3GhjX",
  "type": "assistant",
  "uuid": "21cbe068-7456-4794-9d92-412a0d51a881",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "a6ae7e35-390a-442a-93d4-9958c82c9e3b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0177Vnan7hSoG4fg6Kzo9J6X",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8018,
      "cache_read_input_tokens": 65477,
      "output_tokens": 2437,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 8018,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2437,
          "cache_read_input_tokens": 65477,
          "cache_creation_input_tokens": 8018,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 8018
          },
          "type": "message"
        }
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

_source line 52 · 2026-05-19T13:57:22.977Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01CXqjVUH1xjJbeKCUMgWVb3`</summary>

```json
{
  "description": "Extract CoNLL degeneracy rates N=8 vs N=16",
  "prompt": "I need to extract very specific data from a large registry JSON file to audit a potential N=8/N=16 data mixing issue.\n\nThe file is at:\n/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-reviewer-0064dd56/a6ae7e35-390a-442a-93d4-9958c82c9e3b/tool-results/mcp-agent-ml-research-read_registry-1779198683077.txt\n\nThis is JSON with schema: {result: string} — the `result` field is a YAML string.\n\nI need to find:\n\n1. **exp_002** (NOT exp_002_conll_n16, just exp_002): What is the sample size N used? Is there a degen_rate or degeneracy metric? What's its value? Quote the full spec and metrics sections.\n\n2. **exp_002_conll_n16**: What N was used? Degen_rate? Full spec and metrics.\n\n3. Any OTHER experiment that reports CoNLL degeneracy at N=8 specifically. Search for degen_rate fields in any CoNLL-related experiment.\n\n4. For exp_012_rerun_1024: Extract the FULL metrics section with all AUROC values (both full and cond, both NER and RE). Also the full spec.\n\n5. For exp_015_metrics_expansion: Extract the FULL metrics section. I need to know what AUROC values this experiment reports for SciERC.\n\n6. For exp_015_v2: Extract the FULL metrics section — this is supposedly the source of AUROC values for Table 1.\n\nUse python or jq to parse. Return ALL field values verbatim — this is a data audit, precision matters. Don't summarize.",
  "subagent_type": "general-purpose"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "21cbe068-7456-4794-9d92-412a0d51a881",
  "isSidechain": false,
  "requestId": "req_011CbC3TnAbUGWHJNhy3GhjX",
  "type": "assistant",
  "uuid": "a7dbeec1-7355-4b91-b81b-2a7deb3be1c9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "a6ae7e35-390a-442a-93d4-9958c82c9e3b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0177Vnan7hSoG4fg6Kzo9J6X",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8018,
      "cache_read_input_tokens": 65477,
      "output_tokens": 2437,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 8018,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2437,
          "cache_read_input_tokens": 65477,
          "cache_creation_input_tokens": 8018,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 8018
          },
          "type": "message"
        }
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

_source line 53 · 2026-05-19T14:00:03.726Z_

<details><summary>↩ Tool result · `toolu_01CXqjVUH1xjJbeKCUMgWVb3`</summary>

```text
Here is the complete extracted data:

---

## 1. exp_002 (CoNLL, Qwen3-8B)

**N = 8** (from command: `--n_samples 8`; also `metrics.n_samples: 8`)

**No `degen_rate` field exists in this experiment's metrics.** The metrics contain `n_valid: 2756` out of `n_instances: 3453`, but degeneracy rate was not computed/recorded.

**Full spec:**
- command: `python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-conll2003-merged --dataset conll2003 --subtask ner --n_samples 8 --temperature 1.0 --collect_logprobs --num_test 99999`
- model: `qwen3-8b-conll2003-lora-merged`
- seed: 42
- server: autodl-5090
- data: `data/conll2003`, 3453 instances

**Full metrics:**
- `greedy_f1: 0.9123`, `voting_f1: 0.9141`, `oracle_f1: 0.9543`, `oracle_headroom: 0.042`
- `n_samples: 8`, `n_instances: 3453`, `n_valid: 2756`, `temperature: 1`
- SJ: `auroc_full=0.8008`, `rho_full=0.4357`, `rho_cond=0.4511`, `tau_full=0.3851`
- EM: `auroc_full=0.8156`, `rho_full=0.4507`, `rho_cond=0.4799`, `tau_full=0.4002`
- FK: `auroc_full=0.7741`, `rho_full=0.3998`, `rho_cond=0.4064`, `tau_full=0.3568`
- EV: `auroc_full=0.7889`, `rho_full=0.4237`, `rho_cond=0.4127`, `tau_full=0.3777`
- logprob: `auroc_full=0.7532`, `rho_full=0.3157`, `rho_cond=0.3562`, `tau_full=0.2469`
- SJ vs logprob delta: `0.12` (significant=true, CI=[0.0881, 0.154])

---

## 2. exp_002_conll_n16 (CoNLL, Qwen3-8B)

**N = 16** (explicit in `metrics.N: 16` and command `--n_samples 16`)

**degen_rate = 0.4844** (source: `unified_metrics_constant_f1_gold_filtered`)

**Full spec:**
- command: `--n_samples 16 --temperature 1.0 --seed 42 --num_test 9999 --collect_logprobs`
- model: `qwen3-8b-conll2003-merged`
- parent: `exp_002_ner_conll2003`
- plan_id: `exp-002`
- seed: 42
- server: autodl-5090

**Full metrics (condensed):**
- `greedy_f1: 0.907`, `n_instances: 3453`, `n_valid: 2756`, `n_conditional: 2614`
- `degen_rate: 0.4844`
- Full AUROC: EM=0.8409, FK=0.7821, SJ=0.8264, logprob=0.7531, voting_conf=0.8071
- Full rho: EM=0.4627, FK=0.3928, SJ=0.4496, logprob=0.3146, voting_conf=0.4286
- Cond AUROC: EM=0.8781, FK=0.7819, SJ=0.8405, logprob=0.8259, voting_conf=0.7951
- Cond rho: EM=0.4658, FK=0.3494, SJ=0.4208, logprob=0.3756, voting_conf=0.3654
- n8_vs_n16_delta_rho_full: EM=+0.012, FK=-0.007, SJ=+0.0139, logprob=-0.0011, voting_conf=+0.0049

---

## 3. CoNLL N=8 experiments with degen_rate

**No Qwen3-8B CoNLL N=8 experiment reports degen_rate.** `exp_002` (which IS Qwen3-8B CoNLL N=8) has **no degen_rate field**.

The only CoNLL N=8 experiments with degen_rate are both **Qwen3-4B** (different model scale):
- `exp_qwen3_4b_conll_scs_inference`: N=8, degen_rate=**0.9057**
- `exp_qwen3_4b_conll_scs_inference_v2`: N=8, degen_rate=**0.9057**

These are 4B model scale ablation experiments, not the 8B model used in Table 1.

**Key finding: There is NO degen_rate recorded for the canonical Qwen3-8B CoNLL N=8 configuration (exp_002).** The degen_rate was only added to the pipeline later (for N=16 experiments and 4B ablations). If Table 1 or any paper claim uses a CoNLL N=8 degen_rate for the 8B model, it has no registry source.

---

## 4. exp_012_rerun_1024 (SciERC, Qwen3-8B, N=8, max_tokens=1024)

**degen_rate = 0.1777**

**Full spec:**
- command: `CUDA_VISIBLE_DEVICES=0 python3 code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc/processed_data --dataset scierc --subtask joint --n_samples 8 --temperature 1.0 --max_tokens 1024 --seed 42 --num_test 9999 --collect_logprobs --output_dir output/exp_012_rerun_1024`
- model: `qwen3-8b-scierc-merged-v2`
- dataset: SciERC
- parent: `exp_012_logprob_baseline`
- seed: 42
- server: autodl-5090

**Full metrics (all AUROC values):**

| Signal | NER full AUROC | NER cond AUROC | RE full AUROC | RE cond AUROC |
|--------|---------------|----------------|--------------|---------------|
| EM     | 0.7493        | 0.7556         | 0.7059       | 0.7515        |
| FK     | 0.6290        | 0.6078         | 0.6089       | 0.5510        |
| SJ     | 0.6917        | 0.6772         | 0.6702       | 0.6463        |
| logprob| 0.5783        | 0.5633         | 0.6005       | 0.5186        |
| voting | 0.6841        | 0.6618         | 0.6935       | 0.6420        |

**Full rho values:**

| Signal | NER full rho | NER cond rho | RE full rho | RE cond rho |
|--------|-------------|--------------|------------|-------------|
| EM     | 0.2945      | 0.3596       | 0.1344     | 0.4165      |
| FK     | 0.2665      | 0.1761       | 0.2752     | 0.1139      |
| SJ     | 0.3599      | 0.3113       | 0.2503     | 0.2457      |
| logprob| 0.2052      | 0.1538       | 0.2662     | 0.0112      |
| voting | 0.3792      | 0.3000       | 0.3498     | 0.2409      |

n: NER full=529, NER cond=477, RE full=397, RE cond=238

**provenance_note:** "exp_015_v2 scierc_n8_logprob used exp_012_logprob (max_tokens=512 truncated data). voting_conf was inflated 0.502->0.379, logprob was suppressed 0.140->0.205."

---

## 5. exp_015_metrics_expansion (SciERC analysis, reuses exp_012 data)

**CRITICAL NOTE in the record itself:** `notes: 'RE logprob_rho_cond=0.1457 uses WRONG conditional filter (any sample F1>0, n=331). Correct value: 0.0112 from exp_012_rerun_1024 (greedy_f1>0, n=238). This entry's RE cond values are DEPRECATED.'`

**Data source:** `exp_012_logprob/samples_with_logprobs.jsonl` (this is the OLD max_tokens=512 data, NOT the 1024 rerun)

**SciERC NER metrics:**
- `em_auroc: 0.623`, `em_rho_full: 0.2566`, `em_rho_cond: 0.3427`
- `fk_auroc: 0.6243`, `fk_rho_full: 0.2651`, `fk_rho_cond: 0.306`
- `sj_auroc: 0.6656`, `sj_rho_full: 0.3565`, `sj_rho_cond: 0.412`
- `logprob_auroc: 0.5585`, `logprob_rho_full: 0.1396`, `logprob_rho_cond: 0.1627`
- `voting_auroc: 0.7279`, `voting_rho_full: 0.5018`, `voting_rho_cond: 0.4497`
- n_valid=529, n_cond=501

**SciERC RE metrics:**
- `em_auroc: 0.5036`, `em_rho_full: 0.1002`, `em_rho_cond: 0.3607`
- `fk_auroc: 0.6308`, `fk_rho_full: 0.2528`, `fk_rho_cond: 0.3168`
- `sj_auroc: 0.5816`, `sj_rho_full: 0.2112`, `sj_rho_cond: 0.3683`
- `logprob_auroc: 0.6354`, `logprob_rho_full: 0.2467`, `logprob_rho_cond: 0.1457` **(DEPRECATED - wrong filter)**
- `voting_auroc: 0.7162`, `voting_rho_full: 0.4217`, `voting_rho_cond: 0.463`
- n_valid=397, n_cond=296

---

## 6. exp_015_v2 (multi-model/multi-seed averaged AUROC)

This experiment stores only **averaged AUROC** values across 10 datasets (multi-model Qwen3-8B + LLaMA, multi-seed 42/123/456). It does NOT contain per-seed or per-dataset breakdowns, rho values, or raw data.

**SciERC NER averages:**
- `em_auroc: 0.7873`
- `fk_auroc: 0.6172`
- `logprob_auroc: 0.5918`
- `sj_auroc: 0.7394`
- `voting_auroc: 0.7367`

**SciERC RE averages:**
- `em_auroc: 0.7150`
- `fk_auroc: 0.5939`
- `logprob_auroc: 0.5849`
- `sj_auroc: 0.6746`
- `voting_auroc: 0.7234`

**Spec:** data_count=9148, data_path="output/ (10 datasets)", model="Qwen3-8B + LLaMA (multi-model)", seeds="42,123,456 (multi-seed)"

---

## Key audit observations

1. **exp_002 (Qwen3-8B CoNLL N=8) has NO degen_rate.** If any document claims a specific CoNLL N=8 degeneracy rate for the 8B model, it cannot be traced to registry.

2. **exp_015_metrics_expansion is built on max_tokens=512 (truncated) data** from `exp_012_logprob`, not from `exp_012_rerun_1024` (max_tokens=1024). The record itself flags RE conditional values as DEPRECATED.

3. **exp_015_v2 only stores averaged AUROC** -- no rho, no per-experiment breakdowns, no CIs. If Table 1 cites specific rho or per-dataset values and attributes them to exp_015_v2, those values are not in this record.

4. **The provenance_note in exp_012_rerun_1024** explicitly states that exp_015_v2's SciERC N=8 logprob values came from the wrong (truncated) data source, with voting_conf inflated from 0.502 to 0.379 and logprob suppressed from 0.140 to 0.205.

agentId: a64b58073ea7a72a5 (use SendMessage with to: 'a64b58073ea7a72a5' to continue this agent)
&lt;usage>total_tokens: 49798
tool_uses: 13
duration_ms: 160745&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a7dbeec1-7355-4b91-b81b-2a7deb3be1c9",
  "isSidechain": false,
  "promptId": "2279f609-b135-4e34-8568-a1f529688be0",
  "type": "user",
  "uuid": "1ed8475c-ac7f-4104-a323-911da6e6f96e",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I need to extract very specific data from a large registry JSON file to audit a potential N=8/N=16 data mixing issue.\n\nThe file is at:\n/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-reviewer-0064dd56/a6ae7e35-390a-442a-93d4-9958c82c9e3b/tool-results/mcp-agent-ml-research-read_registry-1779198683077.txt\n\nThis is JSON with schema: {result: string} — the `result` field is a YAML string.\n\nI need to find:\n\n1. **exp_002** (NOT exp_002_conll_n16, just exp_002): What is the sample size N used? Is there a degen_rate or degeneracy metric? What's its value? Quote the full spec and metrics sections.\n\n2. **exp_002_conll_n16**: What N was used? Degen_rate? Full spec and metrics.\n\n3. Any OTHER experiment that reports CoNLL degeneracy at N=8 specifically. Search for degen_rate fields in any CoNLL-related experiment.\n\n4. For exp_012_rerun_1024: Extract the FULL metrics section with all AUROC values (both full and cond, both NER and RE). Also the full spec.\n\n5. For exp_015_metrics_expansion: Extract the FULL metrics section. I need to know what AUROC values this experiment reports for SciERC.\n\n6. For exp_015_v2: Extract the FULL metrics section — this is supposedly the source of AUROC values for Table 1.\n\nUse python or jq to parse. Return ALL field values verbatim — this is a data audit, precision matters. Don't summarize.",
    "agentId": "a64b58073ea7a72a5",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Here is the complete extracted data:\n\n---\n\n## 1. exp_002 (CoNLL, Qwen3-8B)\n\n**N = 8** (from command: `--n_samples 8`; also `metrics.n_samples: 8`)\n\n**No `degen_rate` field exists in this experiment's metrics.** The metrics contain `n_valid: 2756` out of `n_instances: 3453`, but degeneracy rate was not computed/recorded.\n\n**Full spec:**\n- command: `python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-conll2003-merged --dataset conll2003 --subtask ner --n_samples 8 --temperature 1.0 --collect_logprobs --num_test 99999`\n- model: `qwen3-8b-conll2003-lora-merged`\n- seed: 42\n- server: autodl-5090\n- data: `data/conll2003`, 3453 instances\n\n**Full metrics:**\n- `greedy_f1: 0.9123`, `voting_f1: 0.9141`, `oracle_f1: 0.9543`, `oracle_headroom: 0.042`\n- `n_samples: 8`, `n_instances: 3453`, `n_valid: 2756`, `temperature: 1`\n- SJ: `auroc_full=0.8008`, `rho_full=0.4357`, `rho_cond=0.4511`, `tau_full=0.3851`\n- EM: `auroc_full=0.8156`, `rho_full=0.4507`, `rho_cond=0.4799`, `tau_full=0.4002`\n- FK: `auroc_full=0.7741`, `rho_full=0.3998`, `rho_cond=0.4064`, `tau_full=0.3568`\n- EV: `auroc_full=0.7889`, `rho_full=0.4237`, `rho_cond=0.4127`, `tau_full=0.3777`\n- logprob: `auroc_full=0.7532`, `rho_full=0.3157`, `rho_cond=0.3562`, `tau_full=0.2469`\n- SJ vs logprob delta: `0.12` (significant=true, CI=[0.0881, 0.154])\n\n---\n\n## 2. exp_002_conll_n16 (CoNLL, Qwen3-8B)\n\n**N = 16** (explicit in `metrics.N: 16` and command `--n_samples 16`)\n\n**degen_rate = 0.4844** (source: `unified_metrics_constant_f1_gold_filtered`)\n\n**Full spec:**\n- command: `--n_samples 16 --temperature 1.0 --seed 42 --num_test 9999 --collect_logprobs`\n- model: `qwen3-8b-conll2003-merged`\n- parent: `exp_002_ner_conll2003`\n- plan_id: `exp-002`\n- seed: 42\n- server: autodl-5090\n\n**Full metrics (condensed):**\n- `greedy_f1: 0.907`, `n_instances: 3453`, `n_valid: 2756`, `n_conditional: 2614`\n- `degen_rate: 0.4844`\n- Full AUROC: EM=0.8409, FK=0.7821, SJ=0.8264, logprob=0.7531, voting_conf=0.8071\n- Full rho: EM=0.4627, FK=0.3928, SJ=0.4496, logprob=0.3146, voting_conf=0.4286\n- Cond AUROC: EM=0.8781, FK=0.7819, SJ=0.8405, logprob=0.8259, voting_conf=0.7951\n- Cond rho: EM=0.4658, FK=0.3494, SJ=0.4208, logprob=0.3756, voting_conf=0.3654\n- n8_vs_n16_delta_rho_full: EM=+0.012, FK=-0.007, SJ=+0.0139, logprob=-0.0011, voting_conf=+0.0049\n\n---\n\n## 3. CoNLL N=8 experiments with degen_rate\n\n**No Qwen3-8B CoNLL N=8 experiment reports degen_rate.** `exp_002` (which IS Qwen3-8B CoNLL N=8) has **no degen_rate field**.\n\nThe only CoNLL N=8 experiments with degen_rate are both **Qwen3-4B** (different model scale):\n- `exp_qwen3_4b_conll_scs_inference`: N=8, degen_rate=**0.9057**\n- `exp_qwen3_4b_conll_scs_inference_v2`: N=8, degen_rate=**0.9057**\n\nThese are 4B model scale ablation experiments, not the 8B model used in Table 1.\n\n**Key finding: There is NO degen_rate recorded for the canonical Qwen3-8B CoNLL N=8 configuration (exp_002).** The degen_rate was only added to the pipeline later (for N=16 experiments and 4B ablations). If Table 1 or any paper claim uses a CoNLL N=8 degen_rate for the 8B model, it has no registry source.\n\n---\n\n## 4. exp_012_rerun_1024 (SciERC, Qwen3-8B, N=8, max_tokens=1024)\n\n**degen_rate = 0.1777**\n\n**Full spec:**\n- command: `CUDA_VISIBLE_DEVICES=0 python3 code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc/processed_data --dataset scierc --subtask joint --n_samples 8 --temperature 1.0 --max_tokens 1024 --seed 42 --num_test 9999 --collect_logprobs --output_dir output/exp_012_rerun_1024`\n- model: `qwen3-8b-scierc-merged-v2`\n- dataset: SciERC\n- parent: `exp_012_logprob_baseline`\n- seed: 42\n- server: autodl-5090\n\n**Full metrics (all AUROC values):**\n\n| Signal | NER full AUROC | NER cond AUROC | RE full AUROC | RE cond AUROC |\n|--------|---------------|----------------|--------------|---------------|\n| EM     | 0.7493        | 0.7556         | 0.7059       | 0.7515        |\n| FK     | 0.6290        | 0.6078         | 0.6089       | 0.5510        |\n| SJ     | 0.6917        | 0.6772         | 0.6702       | 0.6463        |\n| logprob| 0.5783        | 0.5633         | 0.6005       | 0.5186        |\n| voting | 0.6841        | 0.6618         | 0.6935       | 0.6420        |\n\n**Full rho values:**\n\n| Signal | NER full rho | NER cond rho | RE full rho | RE cond rho |\n|--------|-------------|--------------|------------|-------------|\n| EM     | 0.2945      | 0.3596       | 0.1344     | 0.4165      |\n| FK     | 0.2665      | 0.1761       | 0.2752     | 0.1139      |\n| SJ     | 0.3599      | 0.3113       | 0.2503     | 0.2457      |\n| logprob| 0.2052      | 0.1538       | 0.2662     | 0.0112      |\n| voting | 0.3792      | 0.3000       | 0.3498     | 0.2409      |\n\nn: NER full=529, NER cond=477, RE full=397, RE cond=238\n\n**provenance_note:** \"exp_015_v2 scierc_n8_logprob used exp_012_logprob (max_tokens=512 truncated data). voting_conf was inflated 0.502->0.379, logprob was suppressed 0.140->0.205.\"\n\n---\n\n## 5. exp_015_metrics_expansion (SciERC analysis, reuses exp_012 data)\n\n**CRITICAL NOTE in the record itself:** `notes: 'RE logprob_rho_cond=0.1457 uses WRONG conditional filter (any sample F1>0, n=331). Correct value: 0.0112 from exp_012_rerun_1024 (greedy_f1>0, n=238). This entry's RE cond values are DEPRECATED.'`\n\n**Data source:** `exp_012_logprob/samples_with_logprobs.jsonl` (this is the OLD max_tokens=512 data, NOT the 1024 rerun)\n\n**SciERC NER metrics:**\n- `em_auroc: 0.623`, `em_rho_full: 0.2566`, `em_rho_cond: 0.3427`\n- `fk_auroc: 0.6243`, `fk_rho_full: 0.2651`, `fk_rho_cond: 0.306`\n- `sj_auroc: 0.6656`, `sj_rho_full: 0.3565`, `sj_rho_cond: 0.412`\n- `logprob_auroc: 0.5585`, `logprob_rho_full: 0.1396`, `logprob_rho_cond: 0.1627`\n- `voting_auroc: 0.7279`, `voting_rho_full: 0.5018`, `voting_rho_cond: 0.4497`\n- n_valid=529, n_cond=501\n\n**SciERC RE metrics:**\n- `em_auroc: 0.5036`, `em_rho_full: 0.1002`, `em_rho_cond: 0.3607`\n- `fk_auroc: 0.6308`, `fk_rho_full: 0.2528`, `fk_rho_cond: 0.3168`\n- `sj_auroc: 0.5816`, `sj_rho_full: 0.2112`, `sj_rho_cond: 0.3683`\n- `logprob_auroc: 0.6354`, `logprob_rho_full: 0.2467`, `logprob_rho_cond: 0.1457` **(DEPRECATED - wrong filter)**\n- `voting_auroc: 0.7162`, `voting_rho_full: 0.4217`, `voting_rho_cond: 0.463`\n- n_valid=397, n_cond=296\n\n---\n\n## 6. exp_015_v2 (multi-model/multi-seed averaged AUROC)\n\nThis experiment stores only **averaged AUROC** values across 10 datasets (multi-model Qwen3-8B + LLaMA, multi-seed 42/123/456). It does NOT contain per-seed or per-dataset breakdowns, rho values, or raw data.\n\n**SciERC NER averages:**\n- `em_auroc: 0.7873`\n- `fk_auroc: 0.6172`\n- `logprob_auroc: 0.5918`\n- `sj_auroc: 0.7394`\n- `voting_auroc: 0.7367`\n\n**SciERC RE averages:**\n- `em_auroc: 0.7150`\n- `fk_auroc: 0.5939`\n- `logprob_auroc: 0.5849`\n- `sj_auroc: 0.6746`\n- `voting_auroc: 0.7234`\n\n**Spec:** data_count=9148, data_path=\"output/ (10 datasets)\", model=\"Qwen3-8B + LLaMA (multi-model)\", seeds=\"42,123,456 (multi-seed)\"\n\n---\n\n## Key audit observations\n\n1. **exp_002 (Qwen3-8B CoNLL N=8) has NO degen_rate.** If any document claims a specific CoNLL N=8 degeneracy rate for the 8B model, it cannot be traced to registry.\n\n2. **exp_015_metrics_expansion is built on max_tokens=512 (truncated) data** from `exp_012_logprob`, not from `exp_012_rerun_1024` (max_tokens=1024). The record itself flags RE conditional values as DEPRECATED.\n\n3. **exp_015_v2 only stores averaged AUROC** -- no rho, no per-experiment breakdowns, no CIs. If Table 1 cites specific rho or per-dataset values and attributes them to exp_015_v2, those values are not in this record.\n\n4. **The provenance_note in exp_012_rerun_1024** explicitly states that exp_015_v2's SciERC N=8 logprob values came from the wrong (truncated) data source, with voting_conf inflated from 0.502 to 0.379 and logprob suppressed from 0.140 to 0.205."
      }
    ],
    "totalDurationMs": 160745,
    "totalTokens": 49798,
    "totalToolUseCount": 13,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2291,
      "cache_read_input_tokens": 44006,
      "output_tokens": 3500,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2291
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3500,
          "cache_read_input_tokens": 44006,
          "cache_creation_input_tokens": 2291,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2291,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 1,
      "searchCount": 0,
      "bashCount": 12,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 0
    }
  },
  "sourceToolAssistantUUID": "a7dbeec1-7355-4b91-b81b-2a7deb3be1c9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "a6ae7e35-390a-442a-93d4-9958c82c9e3b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 54_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[System 触发审查]: 收到你的 critical 审查报告，6 个数据一致性问题全部确认。已派 Agent 紧急调查修复。  请你重点关注 P0-1 SciERC AUROC 问题：如果 EM AUROC 确实是 0.749 而非 0.614，论文中以下叙述可能需要修改： 1. Table 1 信号排序结论（EM 可能超过 VC 成为 SciERC 最高 AUROC） 2. 正文中关于\"s…",
  "leafUuid": "1ed8475c-ac7f-4104-a323-911da6e6f96e",
  "sessionId": "a6ae7e35-390a-442a-93d4-9958c82c9e3b"
}
```

---

### Runtime record

_source line 55_

```json
{
  "type": "ai-title",
  "aiTitle": "Verify SciERC AUROC data consistency issues",
  "sessionId": "a6ae7e35-390a-442a-93d4-9958c82c9e3b"
}
```

---

### Assistant

_source line 56 · 2026-05-19T14:01:10.903Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a very clear picture. Let me compile the critical findings:

## P0-1: SciERC AUROC — CRITICAL

The paper Table 1 SciERC AUROC values are:
- VC: .663
- SJ: .650
- FK: .602
- EM: .614
- LP: .578

These values DON'T match ANY single experiment in the registry:

| Signal | exp_015_metrics_expansion (old, truncated) | exp_012_rerun_1024 (correct) | exp_015_v2 (multi-model avg) | Paper Table 1 |


|--------|-------------------------------------------|------------------------------|------------------------------|---------------|
| VC     | 0.7279                                    | 0.6841                       | 0.7367                       | 0.663         |
| SJ     | 0.6656                                    | 0.6917                       | 0.7394                       | 0.650         |
| FK     | 0.6243                                    | 0.6290                       | 0.6172                       | 0.602         |
| EM     | 0.623                                     | 0.7493                       | 0.7873                       | 0.614         |
| LP     | 0.5585                                    | (incomplete)                 | (incomplete)                 | 0.578         |

Looking at this comparison, none of the experimental runs produce the exact paper values—exp_012_rerun_1024 is closest for some signals but diverges significantly for others like EM, while the multi-model averages in exp_015_v2 are consistently higher across the board. The conditional values from exp_012_rerun_1024 don't match either—VC is off by about 0.002, and LP doesn't align at all. Let me reconsider the source attribution: the provenance tab indicates AUROC values should come from exp_015_v2, so I need to check whether these paper values actually correspond to that experiment instead. Looking at exp_015_metrics_expansion, none of those AUROC values match the paper's numbers either—they're all in the ballpark but off by varying amounts. The provenance note about the rho value changes between exp_015 and exp_012 is interesting though, suggesting the paper may have mixed metrics from different experimental runs rather than pulling everything from a single source. The AUROC values in the paper don't match exp_012 either, and exp_015's metrics are labeled differently without the "full" vs "cond" distinction, so I can't trace where those paper values actually came from. It seems like the rho values came from exp_012 but the AUROC values might be from some other intermediate computation or older run that's no longer in the registry.

If I use the canonical exp_012_rerun_1024 NER full values instead, the AUROC rankings shift dramatically — EM jumps to first place at .749 instead of third at .614, while VC drops from first to third. The rho values stay relatively consistent across sources, but the AUROC discrepancies completely change how the signals rank against each other.

This creates a critical revision for Table 1: VC should keep the bold for rho on SciERC, but EM needs the bold for AUROC instead. The narrative about structural signals leading on SciERC remains accurate for rho comparisons, but I need to reconsider whether that claim holds up when looking at the full picture across both metrics.

The team's provenance notes already capture this ρ-AUROC dissociation explicitly—EM dominates AUROC while VC leads rho—so this finding exists in their documentation but hasn't made it into the paper itself. The abstract correctly cites CoNLL numbers, but I should verify the SciERC-specific metrics are accurate: rho up to 0.38 and AUROC up to 0.75 for that dataset.

The difficulty-dependent signal ranking section needs to highlight that SciERC shows a structural vs. surface-level split—where structural signals rank highest for rho but EM/surface methods win on AUROC—which is actually a compelling insight that adds nuance to the findings.

Now I'm tracking down a critical issue with the CoNLL degeneration rate: the paper's table shows 48.4% for N=8, but the actual N=8 experiment has no degeneration metric recorded, while the N=16 run shows exactly 48.44%, suggesting the numbers got mixed up between experimental conditions. -8B N=8 degen_rate in the registry.**

48.4% is suspiciously close to 0.4844 (48.44%). This strongly suggests the paper's CoNLL N=8 degeneracy rate was taken from the N=16 experiment.

This is indeed a systemic data management issue. The degen_rate metric was only added to later experiments and was never backfilled for exp_002 (the N=8 canonical). Someone then needed a CoNLL degen_rate and grabbed it from exp_002_conll_n16 without realizing it was N=16.

Impact:
- If N=16 degen_rate (48.4%) is used to describe N=8 behavior, it may be misleading
- Degeneracy should actually be LOWER at N=16 (harder for all 16 samples to agree),

Actually, I need to think through the direction here. If degeneracy means all N samples produce identical outputs, then it's more likely at N=8 than N=16 — eight samples are easier to align than sixteen. So the N=8 rate should actually be higher than 48.4%, not lower. But I'm seeing 48.4% for the N=16 experiment, which would mean the N=8 rate should exceed that if my logic is right.

The real problem is I can't verify the N=8 degen_rate without recomputing it. The paper likely used the N=16 value as a proxy, and without the original N=8 metric, there's no way to know how much error this introduces.

Now I'm organizing the critical findings to report: the SciERC AUROC values in Table 1 are completely untraceable and don't match the correct source experiment, while the CoNLL degen_rate of 48.4% comes from the N=16 run since N=8 has no recorded value. I need to assess how these issues affect the paper's main claims and identify exactly which sections need correction.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1ed8475c-ac7f-4104-a323-911da6e6f96e",
  "isSidechain": false,
  "requestId": "req_011CbC3jzZvH2mB99s92zPMy",
  "type": "assistant",
  "uuid": "be87f285-4cf5-4e11-a0ca-ba237a376db1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "a6ae7e35-390a-442a-93d4-9958c82c9e3b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LzSLazeT5Qmnkk5QbN8N4R",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6016,
      "cache_read_input_tokens": 73495,
      "output_tokens": 5601,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6016,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 5601,
          "cache_read_input_tokens": 73495,
          "cache_creation_input_tokens": 6016,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6016
          },
          "type": "message"
        }
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

_source line 57 · 2026-05-19T14:01:10.908Z_

审计完成。数据追溯清楚了，问题比最初报告的更严重。现在向 Director 发送详细审查报告。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "be87f285-4cf5-4e11-a0ca-ba237a376db1",
  "isSidechain": false,
  "requestId": "req_011CbC3jzZvH2mB99s92zPMy",
  "type": "assistant",
  "uuid": "5584fe18-c575-4e5e-8cb0-53f43eda3d53",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "a6ae7e35-390a-442a-93d4-9958c82c9e3b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LzSLazeT5Qmnkk5QbN8N4R",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6016,
      "cache_read_input_tokens": 73495,
      "output_tokens": 5601,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6016,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 5601,
          "cache_read_input_tokens": 73495,
          "cache_creation_input_tokens": 6016,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6016
          },
          "type": "message"
        }
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

_source line 58 · 2026-05-19T14:01:50.176Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__reviewer_post_to_director · `toolu_01TphXsihLEcEtk5F3FbpQZE`</summary>

```json
{
  "text": "[severity: critical] SciERC AUROC 审查 + CoNLL degen 混用核实 — 独立追溯报告\n\n## 1. P0-1 升级为 CRITICAL：SciERC Table 1 所有 AUROC 值均不可溯源\n\n论文 Table 1 SciERC 列 AUROC 值无法追溯到 registry 中任何单一实验：\n\n| Signal | 论文 Table 1 | exp_012_rerun_1024 (正确源) | exp_015 (已废弃/截断) | exp_015_v2 (多模型均值) |\n|--------|-------------|---------------------------|----------------------|----------------------|\n| VC     | .663        | .684                      | .728                 | .737                 |\n| SJ     | .650        | .692                      | .666                 | .739                 |\n| FK     | .602        | .629                      | .624                 | .617                 |\n| EM     | **.614**    | **.749**                  | .623                 | .787                 |\n| LP     | .578        | .578                      | .559                 | .592                 |\n\n**结论：不仅 EM 是错的，SciERC 全部 5 个 AUROC 值中只有 LP (.578) 与 exp_012 匹配。其余 4 个均有偏差。** 论文的值不匹配 exp_012（正确）、不匹配 exp_015（旧/截断）、不匹配 exp_015_v2（多模型均值）。它们来源不明。\n\nrho 值无误——全部匹配 exp_012_rerun_1024 NER full rho：VC=.379, SJ=.360, EM=.295, FK=.267, LP=.205 ✓\n\n### AUROC 排序完全翻转\n\n- **论文当前排序**: VC(.663) > SJ(.650) > EM(.614) > FK(.602) > LP(.578)\n- **exp_012 正确排序**: **EM(.749)** > SJ(.692) > VC(.684) > FK(.629) > LP(.578)\n\nEM 从第 3 跃升至第 1，SJ 超越 VC。\n\n### 对论文叙事的影响\n\n**(a) Table 1 加粗需要修改：** 当前 VC 同时加粗 rho 和 AUROC。纠正后 VC 保留 rho 加粗，EM 应加粗 AUROC。\n\n**(b) \"structural signals lead\" 叙述（experiments.tex L46）：** \"On SciERC (medium difficulty), structural signals lead (VC ρ=0.379, SJ 0.360) over LP (0.205)\" — rho 部分仍然成立。但此段未区分 rho vs AUROC 排序差异。修正后需增加 ρ-AUROC dissociation 讨论：VC 领先 rho，EM（surface signal）领先 AUROC。\n\n**(c) provenance c002 已经知道这个现象：** \"ρ-AUROC dissociation on SciERC — EM leads AUROC (NER 0.749, RE 0.706) while Voting leads ρ\"。但论文正文完全没有体现这个发现。这实际上是一个有趣的发现，反而能强化 \"signal rankings are difficulty-dependent\" 的论述。\n\n**(d) Abstract/Conclusion 的 \"ρ up to 0.45, AUROC up to 0.82\"：** 这些是 CoNLL 数据，不受影响。但 provenance C017 引用的 \"AUROC up to 0.75\" 暗示需要在 SciERC context 中提及 EM 0.749。\n\n**(e) Signal family story 变化：** 当前暗示 \"结构信号在复杂任务（SciERC）全面领先\"。修正后变为 \"结构信号在 rho 排序上领先，但 surface signal EM 在 AUROC 上领先\"——需要更细致的叙述。\n\n### 根因推测\n\nprovenance tab:quality_estimation 声明 AUROC 值来自 exp_015_v2（多模型均值），rho 来自 exp_012。但 Paper Agent 在生成 Table 1 时可能用了某个中间计算的值（既非 exp_015_v2 的均值，也非 exp_012 的正确值），导致了不可溯源的数字。\n\n**建议：Agent 修复时必须直接从 exp_012_rerun_1024 NER full 取值，不经过任何中间计算。**\n\n---\n\n## 2. P1-6 确认：CoNLL degen 48.4% 确实来自 N=16\n\n**证据链：**\n- 论文 Table tab:fewnerd（experiments.tex L122）CoNLL Degen% = 48.4%，表头标注 N=8\n- exp_002（Qwen3-8B CoNLL N=8，canonical）：**registry 中没有 degen_rate 字段**\n- exp_002_conll_n16（N=16）：degen_rate = **0.4844** = 48.44% → 与论文的 48.4% 完全匹配\n- 没有任何其他 Qwen3-8B CoNLL N=8 实验记录了 degen_rate\n\n**结论：论文中标注为 N=8 的 CoNLL degeneracy rate 48.4% 实际来自 N=16 实验。**\n\n### 系统性问题\n\ndegen_rate metric 是后期添加到 pipeline 中的，未对早期实验（exp_002）回填。当 Paper Agent 需要 CoNLL N=8 degen_rate 时，无 registry 源可用，很可能从 exp_002_conll_n16 误取。\n\n**需要做的修复：**\n1. 在 exp_002 的输出数据上重新计算 N=8 degen_rate（ssh_read_only 读 output/exp_002 的 jsonl 数据，用同一计算逻辑）\n2. 用正确的 N=8 值替换论文中的 48.4%\n3. 全面排查：论文中所有引用 degen_rate 的位置，核对 N 是否匹配\n\n### N=8 vs N=16 degeneracy 预期方向\n\nN=8 degeneracy 应**高于** N=16（8 个样本全部一致比 16 个更容易）。所以真实的 CoNLL N=8 degen_rate 可能 >48.4%。如果确实如此，论文的 \"48.4% degeneracy\" 叙述实际**低估**了真实情况——这不改变定性结论但影响定量准确性。\n\n---\n\n## 3. 审查判定\n\n| 问题 | Severity | 修复要求 |\n|------|----------|---------|\n| SciERC Table 1 全部 AUROC 不可溯源 | CRITICAL | 从 exp_012_rerun_1024 NER full 取值重写 |\n| EM AUROC 排序翻转 | CRITICAL | 修改 Table 1 加粗 + 增加 ρ-AUROC dissociation 讨论 |\n| CoNLL degen_rate N=16→N=8 混用 | CRITICAL | 重算 N=8 degen_rate + 替换论文值 |\n| \"structural signals lead\" 叙述过度简化 | WARNING | 区分 rho vs AUROC ranking |\n| degen_rate 未回填到早期实验 | WARNING | 系统性回填 exp_002 等缺失实验 |\n\n**Agent 修复后我将独立验证：(1) Table 1 所有数字与 exp_012 一致性；(2) CoNLL N=8 degen_rate 重算值；(3) 正文叙述与新排序的一致性。**",
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5584fe18-c575-4e5e-8cb0-53f43eda3d53",
  "isSidechain": false,
  "requestId": "req_011CbC3jzZvH2mB99s92zPMy",
  "type": "assistant",
  "uuid": "692dd33b-6b24-485a-94f6-883bc154acdb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "a6ae7e35-390a-442a-93d4-9958c82c9e3b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LzSLazeT5Qmnkk5QbN8N4R",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6016,
      "cache_read_input_tokens": 73495,
      "output_tokens": 5601,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6016,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 5601,
          "cache_read_input_tokens": 73495,
          "cache_creation_input_tokens": 6016,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6016
          },
          "type": "message"
        }
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

_source line 59 · 2026-05-19T14:01:53.948Z_

<details><summary>↩ Tool result · `toolu_01TphXsihLEcEtk5F3FbpQZE`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"director_session\": \"feishu:group:oc_1b56445332d8ca2b4964b30f300f0e00:director\"}, \"error\": \"\"}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "692dd33b-6b24-485a-94f6-883bc154acdb",
  "isSidechain": false,
  "promptId": "2279f609-b135-4e34-8568-a1f529688be0",
  "type": "user",
  "uuid": "b99da0e3-4532-4150-8dbc-55fd8f848d83",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"director_session\\\": \\\"feishu:group:oc_1b56445332d8ca2b4964b30f300f0e00:director\\\"}, \\\"error\\\": \\\"\\\"}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"director_session\": \"feishu:group:oc_1b56445332d8ca2b4964b30f300f0e00:director\"}, \"error\": \"\"}"
    }
  },
  "sourceToolAssistantUUID": "692dd33b-6b24-485a-94f6-883bc154acdb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "a6ae7e35-390a-442a-93d4-9958c82c9e3b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---
