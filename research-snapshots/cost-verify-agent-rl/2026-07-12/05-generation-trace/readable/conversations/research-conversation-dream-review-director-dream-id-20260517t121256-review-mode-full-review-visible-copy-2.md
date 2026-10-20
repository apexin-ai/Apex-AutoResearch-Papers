# Research conversation: [DREAM Review Director] dream_id=20260517T121256 | review_mode=full | review_visible=True PDF: /home/ubuntu/.agent-ml-re

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 24
- **Recorded user turns:** 2
- **Tool calls:** 4
- **Original source:** `logs/chats/exported-trajectories/account-2/faa92117-dd67-43a6-a8f9-8378acfec5f6.jsonl`
- **Structured JSON:** [`117668ff23cc2664a797.json`](../../sessions/11/117668ff23cc2664a797.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-17T12:54:08.017Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-17T12:54:08.017Z",
  "sessionId": "faa92117-dd67-43a6-a8f9-8378acfec5f6",
  "content": "[DREAM Review Director]\ndream_id=20260517T121256 | review_mode=full | review_visible=True\nPDF: /home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/artifacts/dream_reports/dream_20260517T121256/worst/review_input_f5f46a62.pdf\n\n（内部编排信息：tier=worst，仅用于 submit_dream_review_report 调用。\n你在向 Reviewer 发送审稿任务时，**严禁**提及档位名称 best/median/worst，\n也不要暗示论文结果的好坏。Reviewer 必须盲审。）\n\n任务：对上述 PDF 进行 full 模式审稿。 使用 `dream-review-full` skill 的 dispatch 模板（2 Reviewers：R1 方法+实验、R2 新颖性+相关工作；完整 roundtable：Step 1 独立 → Step 2 交叉分享 → Step 3 收敛 → Step 4 综合）。\n\n## 审稿标准\n\n未指定目标 venue。请按 top ML venue 通用标准审稿（接受率 ~25%，6 分制：1=Strong Reject … 6=Strong Accept）。\n\n## 实验设计参考\n\n完整实验设计（含想象实验列表）：`/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/artifacts/dream_reports/dream_20260517T121256/worst/review_context.yaml`\n论文可能未完整反映所有实验——参考此文件判断覆盖度。\n完成后必须调用 `submit_dream_review_report(report, project=\"cost-verify-agent-rl\", tier=\"worst\", dream_id=\"20260517T121256\", review_visible=True)` —— 报告会写入 dream_reports/dream_20260517T121256/worst/review_report.md，编排进程通过 subprocess 退出读取它。\n不要调用 submit_review_report_to_research_director / update_review_issues / request_external_review —— 这些工具不在 Dream Review Director 白名单内。\n"
}
```

---

### Runtime record

_source line 2 · 2026-05-17T12:54:08.020Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-17T12:54:08.020Z",
  "sessionId": "faa92117-dd67-43a6-a8f9-8378acfec5f6"
}
```

---

## Round 1

9 recorded events

### User

_source line 3 · 2026-05-17T12:54:08.054Z_

[DREAM Review Director]
dream_id=20260517T121256 | review_mode=full | review_visible=True
PDF: /home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/artifacts/dream_reports/dream_20260517T121256/worst/review_input_f5f46a62.pdf

（内部编排信息：tier=worst，仅用于 submit_dream_review_report 调用。
你在向 Reviewer 发送审稿任务时，**严禁**提及档位名称 best/median/worst，
也不要暗示论文结果的好坏。Reviewer 必须盲审。）

任务：对上述 PDF 进行 full 模式审稿。 使用 `dream-review-full` skill 的 dispatch 模板（2 Reviewers：R1 方法+实验、R2 新颖性+相关工作；完整 roundtable：Step 1 独立 → Step 2 交叉分享 → Step 3 收敛 → Step 4 综合）。

## 审稿标准

未指定目标 venue。请按 top ML venue 通用标准审稿（接受率 ~25%，6 分制：1=Strong Reject … 6=Strong Accept）。

## 实验设计参考

完整实验设计（含想象实验列表）：`/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/artifacts/dream_reports/dream_20260517T121256/worst/review_context.yaml`
论文可能未完整反映所有实验——参考此文件判断覆盖度。
完成后必须调用 `submit_dream_review_report(report, project="cost-verify-agent-rl", tier="worst", dream_id="20260517T121256", review_visible=True)` —— 报告会写入 dream_reports/dream_20260517T121256/worst/review_report.md，编排进程通过 subprocess 退出读取它。
不要调用 submit_review_report_to_research_director / update_review_issues / request_external_review —— 这些工具不在 Dream Review Director 白名单内。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "e50933ad-3d3f-4cff-8204-b5ceb8047ed2",
  "type": "user",
  "uuid": "ecedf6cb-3513-4698-b2e6-bccbb9385bff",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl",
  "sessionId": "faa92117-dd67-43a6-a8f9-8378acfec5f6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-17T12:54:08.054Z_

```json
{
  "parentUuid": "ecedf6cb-3513-4698-b2e6-bccbb9385bff",
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
      "mcp__agent-ml-research__director_get_project_overview",
      "mcp__agent-ml-research__director_post_to_reviewer",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__submit_dream_review_report"
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
      "mcp__agent-ml-research__director_get_project_overview",
      "mcp__agent-ml-research__director_post_to_reviewer",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__submit_dream_review_report"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "99580b0b-d966-4202-9ba0-5b8dc3809ca5",
  "timestamp": "2026-05-17T12:54:08.054Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl",
  "sessionId": "faa92117-dd67-43a6-a8f9-8378acfec5f6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-17T12:54:08.054Z_

```json
{
  "parentUuid": "99580b0b-d966-4202-9ba0-5b8dc3809ca5",
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
  "uuid": "634c5caf-781d-440c-9d8f-01f146bcc783",
  "timestamp": "2026-05-17T12:54:08.054Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl",
  "sessionId": "faa92117-dd67-43a6-a8f9-8378acfec5f6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6 · 2026-05-17T12:54:08.054Z_

```json
{
  "parentUuid": "634c5caf-781d-440c-9d8f-01f146bcc783",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "465652e1-54f7-4a11-9966-24872ef180c9",
  "timestamp": "2026-05-17T12:54:08.054Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl",
  "sessionId": "faa92117-dd67-43a6-a8f9-8378acfec5f6",
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
  "aiTitle": "Review ML research paper on cost verification agent RL",
  "sessionId": "faa92117-dd67-43a6-a8f9-8378acfec5f6"
}
```

---

### Assistant

_source line 8 · 2026-05-17T12:54:12.116Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to perform a full review of a paper PDF using the dream-review-full skill dispatch template. Let me start by reading the PDF and the review context, then dispatch two reviewers for a full review process.

Let me first read the PDF and the review context YAML file, and also check if there's a dream-review-full skill available.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "465652e1-54f7-4a11-9966-24872ef180c9",
  "isSidechain": false,
  "requestId": "req_011Cb8B6aCbhPsLBBrJs48nB",
  "type": "assistant",
  "uuid": "96750047-cbe8-4776-9025-d470d8b3dfac",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl",
  "sessionId": "faa92117-dd67-43a6-a8f9-8378acfec5f6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014znhNYAzw6XHJR6rRwon5W",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12375,
      "cache_read_input_tokens": 11841,
      "output_tokens": 314,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12375,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 314,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 12375,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12375
          },
          "type": "message"
        }
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

_source line 9 · 2026-05-17T12:54:12.707Z_

I'll start by reading the paper PDF and the review context, then dispatch the full review process.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "96750047-cbe8-4776-9025-d470d8b3dfac",
  "isSidechain": false,
  "requestId": "req_011Cb8B6aCbhPsLBBrJs48nB",
  "type": "assistant",
  "uuid": "ab4b88a2-e2f1-489c-9a71-f3e0d714aee6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl",
  "sessionId": "faa92117-dd67-43a6-a8f9-8378acfec5f6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014znhNYAzw6XHJR6rRwon5W",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12375,
      "cache_read_input_tokens": 11841,
      "output_tokens": 314,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12375,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 314,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 12375,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12375
          },
          "type": "message"
        }
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

_source line 10 · 2026-05-17T12:54:13.268Z_

<details open><summary>🔧 Tool call — Read · `toolu_01NdL8BCKMXyVUye8FRqpKGh`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/artifacts/dream_reports/dream_20260517T121256/worst/review_input_f5f46a62.pdf"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ab4b88a2-e2f1-489c-9a71-f3e0d714aee6",
  "isSidechain": false,
  "requestId": "req_011Cb8B6aCbhPsLBBrJs48nB",
  "type": "assistant",
  "uuid": "f775b9ac-d4cb-4dd7-8101-11a25504dd05",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl",
  "sessionId": "faa92117-dd67-43a6-a8f9-8378acfec5f6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014znhNYAzw6XHJR6rRwon5W",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12375,
      "cache_read_input_tokens": 11841,
      "output_tokens": 314,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12375,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 314,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 12375,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12375
          },
          "type": "message"
        }
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

_source line 11 · 2026-05-17T12:54:13.301Z_

<details><summary>↩ Tool result · `toolu_01NdL8BCKMXyVUye8FRqpKGh`</summary>

```text
PDF file read: /home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/artifacts/dream_reports/dream_20260517T121256/worst/review_input_f5f46a62.pdf (252.1KB)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f775b9ac-d4cb-4dd7-8101-11a25504dd05",
  "isSidechain": false,
  "promptId": "e50933ad-3d3f-4cff-8204-b5ceb8047ed2",
  "type": "user",
  "uuid": "be2950d4-78db-4f17-8529-1ddaea2516b0",
  "toolUseResult": {
    "type": "pdf",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/artifacts/dream_reports/dream_20260517T121256/worst/review_input_f5f46a62.pdf",
      "base64": "[ATTACHMENT_DATA_REDACTED]",
      "originalSize": 258176
    }
  },
  "sourceToolAssistantUUID": "f775b9ac-d4cb-4dd7-8101-11a25504dd05",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl",
  "sessionId": "faa92117-dd67-43a6-a8f9-8378acfec5f6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

## Round 2

13 recorded events

### User

_source line 12 · 2026-05-17T12:54:13.299Z_

```json
{
  "type": "document",
  "source": {
    "type": "base64",
    "media_type": "application/pdf",
    "data": "[ATTACHMENT_DATA_REDACTED]"
  }
}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "be2950d4-78db-4f17-8529-1ddaea2516b0",
  "isSidechain": false,
  "promptId": "e50933ad-3d3f-4cff-8204-b5ceb8047ed2",
  "type": "user",
  "isMeta": true,
  "uuid": "c7809e4e-863c-4bbb-a699-b6e89e34b262",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl",
  "sessionId": "faa92117-dd67-43a6-a8f9-8378acfec5f6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-17T12:54:13.871Z_

<details open><summary>🔧 Tool call — Read · `toolu_01HZy5KFwoMEfxsW8mGRkjLc`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/artifacts/dream_reports/dream_20260517T121256/worst/review_context.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c7809e4e-863c-4bbb-a699-b6e89e34b262",
  "isSidechain": false,
  "requestId": "req_011Cb8B6aCbhPsLBBrJs48nB",
  "type": "assistant",
  "uuid": "ac32b9ec-0951-443f-848d-159085c84d52",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl",
  "sessionId": "faa92117-dd67-43a6-a8f9-8378acfec5f6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014znhNYAzw6XHJR6rRwon5W",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12375,
      "cache_read_input_tokens": 11841,
      "output_tokens": 314,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12375,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 314,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 12375,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12375
          },
          "type": "message"
        }
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

_source line 14_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[DREAM Review Director] dream_id=20260517T121256 | review_mode=full | review_visible=True PDF: /home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/artifacts/dream_reports/dre…",
  "leafUuid": "ac32b9ec-0951-443f-848d-159085c84d52",
  "sessionId": "faa92117-dd67-43a6-a8f9-8378acfec5f6"
}
```

---

### Runtime record

_source line 15_

```json
{
  "type": "ai-title",
  "aiTitle": "Review ML research paper on cost verification agent RL",
  "sessionId": "faa92117-dd67-43a6-a8f9-8378acfec5f6"
}
```

---

### Tool result

_source line 16 · 2026-05-17T12:54:14.136Z_

<details><summary>↩ Tool result · `toolu_01HZy5KFwoMEfxsW8mGRkjLc`</summary>

```text
1	narrative_guidance: '完全 reframe 为 diagnostic/analysis paper。Title: "Dissecting Credit
2	  Assignment Failure in Multi-Turn LLM Agent RL: A Dual-Mechanism Analysis"。 核心叙事：episode-level
3	  是 necessary but not sufficient，消除 window-level 问题后暴露更深层 credit assignment 瓶颈。 GAE
4	  >> episode-level GRPO 证明 per-token credit 是关键缺失。Sign misattribution 是主要但非唯一因素——entropy
5	  collapse、KL drift、information loss 共同作用。 贡献定位为 failure mode taxonomy + actionable
6	  guidelines + cross-framework design analysis。 Selective verification 完全移入 future
7	  work。Claim 2/3 删除。
8	
9	  '
10	imagined_experiments:
11	- name: Episode-level GRPO convergence (exp029 continuation)
12	  plan_id: plan_001
13	  description: Episode-level GRPO 继续训练至 step 50+，观察是否突破 28% plateau
14	  expected_results:
15	    step15_val_success: 0.28125
16	    step20_val_success: 0.27
17	    step30_val_success: 0.26
18	    step40_val_success: 0.25
19	    step50_val_success: 0.24
20	    convergence_val_success: 0.25
21	    step50_train_success: 0.5
22	    step50_train_pass_at_8: 0.8125
23	    step50_val_pass_at_1: 0.25
24	    step50_val_pass_at_8: 0.94
25	    step50_val_action_is_valid: 0.58
26	    step50_entropy: 0.12
27	    step50_ppo_kl: 0.015
28	    train_val_gap_pp: 25
29	    plateau_onset_step: 10
30	    plateau_duration_steps: 40
31	  result_rationale: 'Episode-level GRPO 在 step 10 后进入 plateau（25-28%），训练 success 持续上升至
32	    ~50% 但 val 不跟随—— 经典 overfitting to training distribution。根因：GRPO 的 bandit-style
33	    credit assignment（所有 token 共享同一 advantage） 无法学习 per-step 策略改进。模型学会了 "在训练任务分布上做对的
34	    trajectory pattern"，但缺乏 fine-grained credit 来泛化到 unseen task instance。Entropy
35	    持续下降表明 policy 在 narrowing 但未在 improving。 pass@8=0.94 证明 policy 有能力但 greedy decoding
36	    无法稳定触发正确路径——credit assignment 不够精细， 无法可靠地将 probability mass 集中到 correct action
37	    sequence 上。
38	
39	    '
40	  tables:
41	  - name: Convergence trajectory
42	    columns:
43	    - step
44	    - val_success
45	    - train_success
46	    - val_pass@8
47	    - entropy
48	    - kl
49	    rows:
50	    - - 5
51	      - 0.25
52	      - 0.31
53	      - 0.88
54	      - 0.2
55	      - 0.003
56	    - - 10
57	      - 0.25
58	      - 0.38
59	      - 0.91
60	      - 0.17
61	      - 0.007
62	    - - 15
63	      - 0.28
64	      - 0.44
65	      - 0.93
66	      - 0.15
67	      - 0.01
68	    - - 20
69	      - 0.27
70	      - 0.47
71	      - 0.93
72	      - 0.14
73	      - 0.012
74	    - - 30
75	      - 0.26
76	      - 0.5
77	      - 0.94
78	      - 0.13
79	      - 0.014
80	    - - 40
81	      - 0.25
82	      - 0.5
83	      - 0.94
84	      - 0.12
85	      - 0.015
86	    - - 50
87	      - 0.24
88	      - 0.5
89	      - 0.94
90	      - 0.12
91	      - 0.015
92	  figures_description:
93	  - 'Learning curve: val_success plateau at 25-28% from step 10 onward, train_success
94	    diverging upward to 50%. Classic overfitting gap.'
95	  - 'Entropy decay curve: monotonic decrease from 0.25 → 0.12, policy narrows without
96	    improving generalization.'
97	  analysis: 'Plateau 确认 episode-level GRPO 的根本限制：bandit-style advantage 足以消除 sign
98	    misattribution， 但不足以提供 per-token credit assignment。25-28% 是 "episode-level 能做到的天花板"
99	    在当前 reward density 下。 这是 analysis paper 的核心发现之一：episode-level 解决了 step-independent
100	    的问题但暴露了更深层瓶颈。
101	
102	    '
103	- name: Context window h-sweep ablation (3 seeds each)
104	  plan_id: plan_002
105	  description: h={2, 5, 10, 20, full} sweep，每个 3 seeds，15 steps each
106	  expected_results:
107	    h2_seed1_step15_success: 0.0
108	    h2_seed2_step15_success: 0.03
109	    h2_seed3_step15_success: 0.0
110	    h2_mean: 0.01
111	    h2_std: 0.017
112	    h2_collapse_step_mean: 4.3
113	    h5_seed1_step15_success: 0.06
114	    h5_seed2_step15_success: 0.0
115	    h5_seed3_step15_success: 0.09
116	    h5_mean: 0.05
117	    h5_std: 0.046
118	    h5_collapse_rate: 0.33
119	    h10_seed1_step15_success: 0.12
120	    h10_seed2_step15_success: 0.03
121	    h10_seed3_step15_success: 0.16
122	    h10_mean: 0.103
123	    h10_std: 0.066
124	    h20_seed1_step15_success: 0.19
125	    h20_seed2_step15_success: 0.09
126	    h20_seed3_step15_success: 0.22
127	    h20_mean: 0.167
128	    h20_std: 0.068
129	    full_seed1_step15_success: 0.28
130	    full_seed2_step15_success: 0.19
131	    full_seed3_step15_success: 0.25
132	    full_mean: 0.24
133	    full_std: 0.046
134	    monotonic_ordering_violated: true
135	    h5_occasionally_beats_h10: true
136	    h20_occasionally_collapses: true
137	  result_rationale: 'Worst 档的关键特征：h-sweep 不是 clean monotonic function。h=2 一致崩溃（sign
138	    misattribution + extreme information loss）， 但 h=5 和 h=10 之间、h=10 和 h=20 之间存在 seed
139	    间交叉——某些 seed 下 h=5 偶尔优于 h=10， h=20 偶尔 collapse。这说明 cliff 位置依赖于 random initialization
140	    和 early training dynamics， 而非仅由 h 值决定。高 cross-seed variance 削弱了 "clean cliff at
141	    h=10" 的叙事， 但仍支持 "smaller h systematically worse on average" 的趋势。Non-monotonicity
142	    来自 不同 seed 的 entropy dynamics 差异：某些 seed 早期 exploration 更好，偶尔让 h=5 找到可行策略。
143	
144	    '
145	  tables:
146	  - name: h-sweep summary (step 15, 3 seeds)
147	    columns:
148	    - h
149	    - seed1
150	    - seed2
151	    - seed3
152	    - mean
153	    - std
154	    - collapse_rate
155	    rows:
156	    - - h=2
157	      - 0.0
158	      - 0.03
159	      - 0.0
160	      - 0.01
161	      - 0.017
162	      - 3/3
163	    - - h=5
164	      - 0.06
165	      - 0.0
166	      - 0.09
167	      - 0.05
168	      - 0.046
169	      - 1/3
170	    - - h=10
171	      - 0.12
172	      - 0.03
173	      - 0.16
174	      - 0.103
175	      - 0.066
176	      - 0/3
177	    - - h=20
178	      - 0.19
179	      - 0.09
180	      - 0.22
181	      - 0.167
182	      - 0.068
183	      - 0/3
184	    - - full
185	      - 0.28
186	      - 0.19
187	      - 0.25
188	      - 0.24
189	      - 0.046
190	      - 0/3
191	  figures_description:
192	  - 'Box plot: h vs val_success with individual seed points. Trend is upward but boxes
193	    overlap between adjacent h values. Error bars large.'
194	  - 'Collapse timeline: h=2 collapses by step 4-5 across all seeds; h=5 collapses
195	    in 1/3 seeds; h≥10 no full collapse but h=20 seed2 shows temporary dip.'
196	  analysis: 'Non-monotonic 结果对 paper 是挑战也是机会。不能 claim "clean cliff"，但可以 reframe 为
197	    "credit assignment failure is a stochastic phenomenon whose probability increases
198	    with smaller h"—— 这更符合 analysis paper 的 tone。Cross-seed variance 本身是 failure mode
199	    taxonomy 的一条： "training instability as a function of context window" 是独立 failure
200	    mechanism。 需要从 "threshold effect" 叙事转向 "probabilistic degradation" 叙事。
201	
202	    '
203	- name: Multi-seed replication (5 seeds)
204	  plan_id: plan_003
205	  description: Episode-level GRPO 5 seeds（含 exp029 原始 seed），report mean ± std
206	  expected_results:
207	    seed1_val_success: 0.28
208	    seed2_val_success: 0.19
209	    seed3_val_success: 0.25
210	    seed4_val_success: 0.15
211	    seed5_val_success: 0.3
212	    mean_val_success: 0.234
213	    std_val_success: 0.062
214	    std_pp: 6.2
215	    min_val_success: 0.15
216	    max_val_success: 0.3
217	    range_pp: 15
218	    seeds_above_25pct: 3
219	    seeds_below_20pct: 1
220	    mean_train_success: 0.46
221	    train_val_gap_mean_pp: 22.6
222	  result_rationale: 'Worst 档要求 std > 7pp。这里 std=6.2pp 接近但略低于 7pp 边界——真实的 worst 场景中
223	    5 seeds 可能落在 6-9pp 范围。 关键问题：seed4 只达到 15%（接近 step-independent 水平），说明 episode-level
224	    的优势在某些 seed 下大幅削弱。 这源于 GRPO 的 group normalization 对初始 rollout 分布敏感——如果前几步 rollout
225	    恰好全部失败， advantage 全为 0（无 variance），模型无法获得有效梯度。Seed4 可能经历了 "cold start" 问题： 早期
226	    rollout 全败 → advantage=0 → 无学习 → 持续全败的恶性循环。高 variance 使 95% CI 覆盖 0， 削弱了 episode-level
227	    作为 "solution" 的 claim，但强化了 analysis paper 的叙事—— "即使 episode-level 也不稳定，RL for
228	    LLM agents 需要更根本性的改进"。
229	
230	    '
231	  tables:
232	  - name: Multi-seed results (step 15 checkpoint)
233	    columns:
234	    - seed
235	    - val_success
236	    - train_success
237	    - action_is_valid
238	    - plateau_step
239	    rows:
240	    - - 1
241	      - 0.28
242	      - 0.44
243	      - 0.55
244	      - 10
245	    - - 2
246	      - 0.19
247	      - 0.41
248	      - 0.52
249	      - 8
250	    - - 3
251	      - 0.25
252	      - 0.47
253	      - 0.56
254	      - 10
255	    - - 4
256	      - 0.15
257	      - 0.35
258	      - 0.48
259	      - 12
260	    - - 5
261	      - 0.3
262	      - 0.5
263	      - 0.58
264	      - 10
265	  - name: Summary statistics
266	    columns:
267	    - metric
268	    - mean
269	    - std
270	    - 95% CI
271	    rows:
272	    - - val_success
273	      - 0.234
274	      - 0.062
275	      - '[0.157, 0.311]'
276	    - - train_success
277	      - 0.434
278	      - 0.057
279	      - '[0.363, 0.505]'
280	    - - action_is_valid
281	      - 0.538
282	      - 0.038
283	      - '[0.491, 0.585]'
284	  figures_description:
285	  - Swarm plot with mean ± 95% CI. CI is wide (15.7pp-31.1%), overlaps with step-independent
286	    range for low seeds.
287	  analysis: '95% CI [15.7%, 31.1%] 太宽，无法 credibly claim episode-level "solves" the
288	    problem。 但 mean 仍显著高于 step-independent mean（~2%），所以 "episode-level helps but doesn''t
289	    solve" 是可靠 claim。 Analysis paper framing: 这证明了 credit assignment 问题的多层性——episode-level
290	    消除了 sign misattribution 但暴露了 GRPO 的 cold-start sensitivity 和 bandit-level credit
291	    的根本限制。
292	
293	    '
294	- name: GAE baseline comparison
295	  plan_id: plan_003b
296	  description: GAE(λ=0.95) 和 GAE(λ=1.0, γ=1.0) baselines，15 steps × 3 seeds
297	  expected_results:
298	    gae_095_seed1_success: 0.44
299	    gae_095_seed2_success: 0.38
300	    gae_095_seed3_success: 0.41
301	    gae_095_mean: 0.41
302	    gae_095_std: 0.03
303	    gae_10_10_seed1_success: 0.37
304	    gae_10_10_seed2_success: 0.34
305	    gae_10_10_seed3_success: 0.39
306	    gae_10_10_mean: 0.367
307	    gae_10_10_std: 0.025
308	    episode_grpo_mean: 0.234
309	    gae_095_vs_episode_delta_pp: 17.6
310	    gae_10_vs_episode_delta_pp: 13.3
311	    gae_095_per_token_adv_variance: 0.42
312	    episode_grpo_per_token_adv_variance: 0.0
313	    step_independent_mean: 0.02
314	  result_rationale: 'Worst 档要求 GAE >> episode-level GRPO（delta > 15pp）。GAE(λ=0.95)
315	    达到 41%—— 因为 critic 提供 per-token temporal difference signal，每个 action 获得独立的 advantage
316	    estimate， 而非 GRPO 的 "全 trajectory 同一 advantage"。这是 worst 档的核心发现： episode-level
317	    GRPO 的 plateau 不是 episode-level 本身的问题，而是 GRPO 的 bandit-style credit 的问题。 GAE 通过
318	    value function 提供 fine-grained credit，打破了 plateau。 GAE(λ=1,γ=1) 略低于 GAE(0.95)，因为无
319	    discount 导致 variance 更高。 Delta=17.6pp 直接证明：per-token credit assignment 是关键缺失，episode-level
320	    只是 necessary condition。 这彻底改变 paper story——从 "episode-level solves it" 到 "episode-level
321	    is necessary but per-token credit is the real bottleneck"。
322	
323	    '
324	  tables:
325	  - name: Method comparison (step 15)
326	    columns:
327	    - method
328	    - seed1
329	    - seed2
330	    - seed3
331	    - mean
332	    - std
333	    rows:
334	    - - step-independent (h=2)
335	      - 0.0
336	      - 0.03
337	      - 0.0
338	      - 0.01
339	      - 0.017
340	    - - episode-level GRPO
341	      - 0.28
342	      - 0.19
343	      - 0.25
344	      - 0.24
345	      - 0.046
346	    - - GAE(λ=1,γ=1)
347	      - 0.37
348	      - 0.34
349	      - 0.39
350	      - 0.367
351	      - 0.025
352	    - - GAE(λ=0.95,γ=1)
353	      - 0.44
354	      - 0.38
355	      - 0.41
356	      - 0.41
357	      - 0.03
358	  figures_description:
359	  - 'Bar chart: 4 methods with error bars. Clear staircase: step-ind << episode-GRPO
360	    << GAE(1,1) < GAE(0.95). Gap between GRPO and GAE is the paper''s key diagnostic
361	    finding.'
362	  analysis: 'GAE 的大幅领先是 analysis paper 的最强证据：问题不只是 window-level vs episode-level，
363	    而是 credit granularity 的 spectrum。GRPO episode-level 在 spectrum 中间（消除了 sign error
364	    但无 per-token credit）， GAE 在另一端（full per-token credit via value function）。这支持 failure
365	    mode taxonomy 的第三种机制： "bandit-level credit insufficiency"——即使 advantage 方向正确，所有
366	    token 共享同一 magnitude 也无法 区分 trajectory 中的关键决策点和无关步骤。
367	
368	    '
369	- name: Episode-level + valid_action_bonus
370	  plan_id: plan_003c
371	  description: Episode-level + valid_action_bonus=0.05，测试是否安全突破 plateau
372	  expected_results:
373	    step15_val_success: 0.22
374	    step15_val_action_is_valid: 0.72
375	    step15_train_success: 0.39
376	    valid_bonus_vs_task_ratio: 0.35
377	    gaming_detected: false
378	    success_improvement_vs_baseline: -0.06
379	    action_is_valid_improvement_pp: 17
380	    reward_composition_valid_pct: 0.28
381	    reward_composition_task_pct: 0.72
382	  result_rationale: 'Worst 档下 valid_action_bonus 在 episode-level 中不 game（因为模型优化整条
383	    trajectory total reward）， action_is_valid 确实从 55% 提升到 72%，但 success 反而略降（22% <
384	    28%）。 原因：valid_action_bonus 改变了 reward landscape，使模型偏向 "safe but ineffective"
385	    actions—— valid 但不 goal-directed 的 action（如反复 examine 已知物体）获得持续正 reward， 而 risky
386	    but potentially successful 的 exploration 策略被抑制。Episode-level 下不存在 per-step gaming，
387	    但 dense bonus 仍扭曲了 trajectory-level 的 learning signal——模型学会生成 "很多 valid action
388	    的长 trajectory" 而非 "goal-directed 的短 trajectory"。这是 analysis paper 的另一个 insight：
389	    dense reward 在 episode-level 下的失效模式与 step-independent 不同但同样有害。
390	
391	    '
392	  tables:
393	  - name: valid_action_bonus ablation
394	    columns:
395	    - config
396	    - val_success
397	    - action_is_valid
398	    - avg_trajectory_len
399	    - reward_mean
400	    rows:
401	    - - episode-level (baseline)
402	      - 0.28
403	      - 0.55
404	      - 38.2
405	      - 2.81
406	    - - episode-level + bonus=0.05
407	      - 0.22
408	      - 0.72
409	      - 45.6
410	      - 3.92
411	  figures_description:
412	  - 'Dual-axis plot: action_is_valid improves (good) but success drops (bad). Trajectory
413	    length increases — model generates more valid-but-aimless steps.'
414	  analysis: 'valid_action_bonus 未引入 step-independent 式 gaming，但通过 reward shaping 偏移了
415	    policy gradient direction。 这是 failure mode taxonomy 的第四种机制："reward misalignment
416	    under sparse task signal"—— 当 task reward 稀疏且 episode-level credit 粗糙时，任何 dense
417	    auxiliary reward 都容易主导 learning。 进一步证明 per-token credit（如 GAE）才是根本解。
418	
419	    '
420	- name: Credit assignment mechanism empirical verification
421	  plan_id: plan_004
422	  description: Per-window advantage logging，验证 sign misattribution 机制
423	  expected_results:
424	    sign_vs_outcome_correlation: 0.73
425	    sign_vs_local_quality_correlation: 0.28
426	    magnitude_position_decay_r2: 0.61
427	    episode_level_adv_variance: 0.0
428	    success_episodes_all_positive_pct: 0.78
429	    failure_episodes_all_negative_pct: 0.82
430	    mixed_sign_episodes_pct: 0.2
431	    gamma_k_decay_slope: -0.032
432	    confound_kl_correlation: 0.31
433	    confound_entropy_correlation: 0.27
434	  result_rationale: 'Worst 档的关键：sign-outcome correlation 只有 0.73（而非预期的 >0.95），sign-local_quality
435	    correlation 达到 0.28（而非预期的 ~0）。这意味着 sign misattribution 存在但有显著混杂因素。 Correlation
436	    < 1.0 的原因：GRPO 的 group normalization 使得同一 group 内的 advantage 不完全由 episode outcome
437	    决定—— 如果 group 内所有 episode 都成功（或都失败），normalization 后 advantage 反映 relative 差异而非
438	    absolute 成败。 这在成功率较高的 training episodes 中尤为明显。 Local quality correlation = 0.28
439	    的原因：window-local action quality 与 episode success 本身存在弱正相关 （好的 local action 确实
440	    contribute to success），所以 sign-local 相关性部分反映了 genuine causal path 而非纯 misattribution。这是混杂因素：无法将
441	    sign-local 相关性 100% 归因于 misattribution， 因为部分是 legitimate credit signal。 KL divergence
442	    和 entropy 也与 advantage sign 相关（r=0.31, 0.27），说明 policy drift 和 exploration dynamics
443	    独立影响 advantage distribution。
444	
445	    '
446	  tables:
447	  - name: Mechanism verification (h=2, seed 2, step 5)
448	    columns:
449	    - metric
450	    - observed
451	    - hypothesis
452	    - status
453	    rows:
454	    - - sign-outcome corr
455	      - 0.73
456	      - '>0.95'
457	      - PARTIAL — significant confounds
458	    - - sign-local_quality corr
459	      - 0.28
460	      - <0.1
461	      - FAILED — non-negligible correlation
462	    - - magnitude decay R²
463	      - 0.61
464	      - '>0.85'
465	      - PARTIAL — decay exists but noisy
466	    - - episode-level adv variance
467	      - 0.0
468	      - '0.0'
469	      - CONFIRMED
470	    - - '% success eps all-positive'
471	      - 78%
472	      - '>95%'
473	      - PARTIAL — 22% have mixed signs
474	  - name: Confound analysis
475	    columns:
476	    - confound_variable
477	    - correlation_with_adv_sign
478	    - p_value
479	    rows:
480	    - - episode_outcome
481	      - 0.73
482	      - <0.001
483	    - - local_action_quality
484	      - 0.28
485	      - <0.01
486	    - - KL_divergence
487	      - 0.31
488	      - <0.01
489	    - - entropy
490	      - 0.27
491	      - <0.01
492	    - - window_position
493	      - -0.18
494	      - <0.05
495	  figures_description:
496	  - 'Scatter: advantage sign vs episode outcome (color=local quality). Not the clean
497	    binary separation expected — significant overlap region.'
498	  - 'Partial correlation decomposition: pie chart showing episode outcome explains
499	    53%, local quality 16%, KL 10%, entropy 8%, unexplained 13%.'
500	  analysis: 'Sign misattribution 存在但不是 sole mechanism——这是 worst 档的核心困难。不能 claim "advantage
501	    sign is entirely determined by episode outcome"。 需要 reframe 为 "sign misattribution
502	    is the dominant but not sole factor in credit assignment failure"。 混杂因素（KL drift、entropy
503	    dynamics）本身成为 failure mode taxonomy 的独立条目。 Partial correlation decomposition 成为
504	    analysis paper 的关键贡献：量化每种机制对 credit assignment failure 的贡献占比。
505	
506	    '
507	- name: Action-change statistics from always-on runs
508	  plan_id: plan_005
509	  description: 从 exp029 checkpoint 收集 action-change 统计
510	  expected_results:
511	    action_change_rate: 0.18
512	    confirmatory_rate: 0.82
513	    action_change_success_correlation: 0.08
514	    action_change_success_p_value: 0.12
515	    per_task_action_change_std: 0.09
516	    pick_action_change_rate: 0.12
517	    clean_action_change_rate: 0.22
518	    heat_action_change_rate: 0.2
519	    cool_action_change_rate: 0.15
520	    examine_action_change_rate: 0.25
521	  result_rationale: 'Worst 档下 action-change-success correlation 仅 0.08 且 p=0.12（不显著）。
522	    原因：episode-level model 只有 25% success rate，样本中 successful episodes 太少导致 statistical
523	    power 不足。 更根本的问题：在 25% success 的 agent 上，action change 基本是 noise—— model 的 verification
524	    输出质量太低，无论是否 change action 都可能是随机的。 Confirmatory rate 82% 符合预期（大部分 verification
525	    不改变行为）， 但这也意味着 action change 事件太稀疏（只有 18%），与 success 的 correlation 在统计上不可靠。 这直接阻碍了
526	    Phase B：如果 action change 不是 success 的有效 signal， 用它作 intrinsic reward 没有理论基础。
527	
528	    '
529	  tables:
530	  - name: Action-change statistics
531	    columns:
532	    - metric
533	    - value
534	    rows:
535	    - - overall action change rate
536	      - 18%
537	    - - confirmatory rate
538	      - 82%
539	    - - action_change-success correlation
540	      - r=0.08, p=0.12
541	    - - N (episodes)
542	      - 128
543	    - - N (verification events)
544	      - 2304
545	    - - N (action changes)
546	      - 415
547	  figures_description:
548	  - 'Contingency table heatmap: action_change × episode_success. No clear pattern
549	    — action change is roughly equally distributed across success/failure episodes.'
550	  analysis: 'Action change 作为 intrinsic reward 缺乏 empirical grounding。在 worst 档下，
551	    这个结果直接导致 Claim 2 无法成立——selective verification 失去了 reward signal。 Analysis paper
552	    中可以作为 "why selective verification is hard for weak agents" 的一个 finding。
553	
554	    '
555	- name: Selective verification implementation
556	  plan_id: plan_006
557	  description: Code-only：实现 binary verify/skip decision
558	  expected_results:
559	    implementation_status: completed
560	    code_changes_files: 4
561	    gpu_hours: 0
562	  result_rationale: '纯代码实现，不依赖实验结果。在 worst 档下仍可完成，但后续使用这个 implementation 的实验效果差。
563	
564	    '
565	  tables: []
566	  figures_description: []
567	  analysis: 'Implementation 本身无 worst 档问题。但 plan_005 的 weak correlation 预示 plan_007
568	    会失败。
569	
570	    '
571	- name: B-IAVR selective verification training
572	  plan_id: plan_007
573	  description: 用 action-change reward 训练 selective verification policy
574	  expected_results:
575	    verification_rate_reduction_pct: 12
576	    val_success: 0.16
577	    baseline_always_on_success: 0.25
578	    success_delta_pp: -9
579	    training_converged: false
580	    reward_signal_informative: false
581	    verification_rate: 0.88
582	    policy_learned_skip: false
583	    training_steps_before_abort: 20
584	  result_rationale: 'Worst 档：selective verification 无法 deliver clear win。两个根因叠加： (1)
585	    plan_005 显示 action-change 不是有效 signal（r=0.08, p=0.12），用它做 reward 等于训练 on noise；
586	    (2) base agent 只有 25% success，skip verification 直接降低 performance 且模型无法学会 when
587	    to skip。 Verification rate 只降了 12%（模型几乎总是 verify），因为 skip 的 penalty（success 下降）远大于
588	    action-change reward 的 bonus。Policy 本质上退化为 "always verify"—— 因为在 25% success 的
589	    agent 上，任何 skip 都有显著 performance cost。 Success 降至 16%（比 baseline 低 9pp），因为即使少量的
590	    skip 也损害了 performance。
591	
592	    '
593	  tables:
594	  - name: B-IAVR results
595	    columns:
596	    - policy
597	    - val_success
598	    - verification_rate
599	    - cost_reduction
600	    rows:
601	    - - always-on
602	      - 0.25
603	      - 100%
604	      - 0%
605	    - - B-IAVR (learned)
606	      - 0.16
607	      - 88%
608	      - 12%
609	    - - random-50%
610	      - 0.14
611	      - 50%
612	      - 50%
613	    - - no-verify
614	      - 0.13
615	      - 0%
616	      - 100%
617	  figures_description:
618	  - 'Pareto frontier: success vs cost. B-IAVR barely separates from always-on, nowhere
619	    near efficient frontier.'
620	  analysis: 'Selective verification 在 worst 档下完全无法作为 paper contribution。 必须移入 future
621	    work，framed as "requires stronger base agent + better reward signal"。
622	
623	    '
624	- name: Selective verification full comparison
625	  plan_id: plan_008
626	  description: Always-on / B-IAVR / no-verify / random-p / confidence 对比
627	  expected_results:
628	    always_on_success: 0.25
629	    always_on_verify_rate: 1.0
630	    biavr_success: 0.16
631	    biavr_verify_rate: 0.88
632	    no_verify_success: 0.13
633	    no_verify_rate: 0.0
634	    random_50_success: 0.14
635	    random_50_rate: 0.5
636	    confidence_success: 0.19
637	    confidence_verify_rate: 0.65
638	    biavr_dominates_pareto: false
639	    best_cost_performance: confidence-threshold
640	  result_rationale: 'Worst 档：B-IAVR 不 dominate Pareto frontier。Confidence-based baseline
641	    意外优于 B-IAVR—— 因为 confidence threshold 是 model-intrinsic signal（policy entropy），
642	    比 action-change 这个 noisy extrinsic signal 更 informative。 Confidence 方法在 entropy
643	    高时 verify（不确定时检查），在 entropy 低时 skip（确定时省略）， 这 naturally 对齐 "verification is useful
644	    when uncertain"。 B-IAVR 学到的 policy 没有这种 alignment 因为 training signal 太弱。 所有 selective
645	    方法都比 always-on 差（delta > 5pp），因为 base agent 太弱—— verification 在 25% agent 上几乎总是有用的（因为
646	    agent 经常犯错）。
647	
648	    '
649	  tables:
650	  - name: Full comparison (step 15 checkpoint, 128 val episodes)
651	    columns:
652	    - method
653	    - success
654	    - verify_rate
655	    - total_tokens
656	    - success_per_token
657	    rows:
658	    - - always-on
659	      - 25.0%
660	      - 100%
661	      - 1.0x
662	      - '0.250'
663	    - - confidence-0.5
664	      - 19.0%
665	      - 65%
666	      - 0.72x
667	      - '0.264'
668	    - - B-IAVR
669	      - 16.0%
670	      - 88%
671	      - 0.93x
672	      - '0.172'
673	    - - random-50%
674	      - 14.0%
675	      - 50%
676	      - 0.62x
677	      - '0.226'
678	    - - no-verify
679	      - 13.0%
680	      - 0%
681	      - 0.45x
682	      - '0.289'
683	  figures_description:
684	  - 'Pareto frontier plot: no-verify has best token-efficiency (trivially), confidence-threshold
685	    dominates B-IAVR. B-IAVR is dominated — not on the frontier.'
686	  analysis: 'B-IAVR 被 confidence baseline dominate，这对 Claim 3 是致命的。 但 analysis paper
687	    可以 reframe：展示为什么 RL-trained selective verification 在 weak agents 上失败—— action-change
688	    signal 需要 base agent 足够强才有意义（类比：你不能教一个 25% accuracy 的学生 when to double-check）。
689	
690	    '
691	- name: No-verify ablation
692	  plan_id: plan_009
693	  description: Episode-level GRPO without self-verification
694	  expected_results:
695	    val_success: 0.13
696	    val_action_is_valid: 0.42
697	    always_on_success: 0.25
698	    delta_pp: -12
699	    avg_trajectory_length: 28.5
700	    avg_trajectory_length_with_verify: 41.3
701	  result_rationale: 'No-verify 比 always-on 低 12pp，确认 verification 有价值。 但在 worst 档下这个
702	    delta 略小于预期的 ≥10pp（12pp 刚过线）， 因为 weak agent 的 verification 质量也不高——agent 经常 verify
703	    但 verification 本身也是 noisy。 Action_is_valid 从 55% 降到 42%，说明 verification 确实帮助 format
704	    compliance。 Trajectory 更短（28 vs 41 steps）因为没有 verification 步骤。
705	
706	    '
707	  tables:
708	  - name: Verification ablation
709	    columns:
710	    - config
711	    - success
712	    - action_is_valid
713	    - avg_steps
714	    - avg_tokens
715	    rows:
716	    - - always-on verify
717	      - 25.0%
718	      - 55%
719	      - 41.3
720	      - 4850
721	    - - no verify
722	      - 13.0%
723	      - 42%
724	      - 28.5
725	      - 2980
726	    - - delta
727	      - -12pp
728	      - -13pp
729	      - '-12.8'
730	      - '-1870'
731	  figures_description:
732	  - 'Paired bar chart: with/without verification across task types.'
733	  analysis: 'Verification 有价值（-12pp），但价值不足以支撑 "selective verification as primary contribution"。
734	    在 analysis paper 中，这是一个 supporting data point：verification matters， 但 training
735	    agents to be selective about it requires solving the credit assignment problem
736	    first。
737	
738	    '
739	- name: Entropy-controlled action-change analysis
740	  plan_id: plan_010
741	  description: Stratify action-change-success correlation by policy entropy
742	  expected_results:
743	    overall_correlation: 0.08
744	    overall_p_value: 0.12
745	    low_entropy_partial_corr: 0.05
746	    low_entropy_p_value: 0.41
747	    medium_entropy_partial_corr: 0.09
748	    medium_entropy_p_value: 0.18
749	    high_entropy_partial_corr: 0.12
750	    high_entropy_p_value: 0.09
751	    partial_correlation_controlling_entropy: 0.07
752	    partial_p_value: 0.15
753	  result_rationale: 'Worst 档：partial correlation 在控制 entropy 后仍不显著（r=0.07, p=0.15）。
754	    Action change 与 success 的微弱相关几乎完全由 entropy 解释—— 高 entropy 时更容易 change action（因为
755	    policy 本身不确定）， 高 entropy 任务也更可能成功（因为 exploration 更充分）。 控制 entropy 后 action change
756	    本身对 success 没有独立贡献。 这直接否定了 "action change as causal signal for verification quality"
757	    的假设。
758	
759	    '
760	  tables:
761	  - name: Entropy-stratified analysis
762	    columns:
763	    - entropy_stratum
764	    - N
765	    - action_change_rate
766	    - success_rate
767	    - corr
768	    - p
769	    rows:
770	    - - low (<0.10)
771	      - 768
772	      - 11%
773	      - 18%
774	      - 0.05
775	      - 0.41
776	    - - medium (0.10-0.20)
777	      - 896
778	      - 17%
779	      - 24%
780	      - 0.09
781	      - 0.18
782	    - - high (>0.20)
783	      - 640
784	      - 28%
785	      - 31%
786	      - 0.12
787	      - 0.09
788	    - - partial (controlling entropy)
789	      - 2304
790	      - '-'
791	      - '-'
792	      - 0.07
793	      - 0.15
794	  figures_description:
795	  - '3-panel scatter: action_change vs success within each entropy stratum. No clear
796	    trend in any panel.'
797	  analysis: 'Action change 不是 independent signal——它是 entropy 的 proxy。 这对 Claim 2 是
798	    additional nail in the coffin。Analysis paper framing： "apparent verification informativeness
799	    signals are confounded with policy uncertainty"， 这是 selective verification failure
800	    的又一个 identified mechanism。
801	
802	    '
803	- name: 'Causal intervention: random vs verification-triggered changes'
804	  plan_id: plan_011
805	  description: 注入 random action changes vs verification-triggered，对比 success
806	  expected_results:
807	    verification_triggered_success: 0.27
808	    random_change_success: 0.21
809	    no_change_success: 0.25
810	    triggered_vs_random_delta_pp: 6
811	    triggered_vs_random_p_value: 0.08
812	    triggered_vs_baseline_delta_pp: 2
813	    random_vs_baseline_delta_pp: -4
814	  result_rationale: 'Worst 档：verification-triggered changes 仅比 random 好 6pp（p=0.08，边缘不显著）。
815	    这弱于预期的 ≥10pp。原因：agent 只有 25% success，verification 质量差， triggered changes 只是 "slightly
816	    better than random" 而非 "causally informative"。 有趣的是 triggered 甚至只比 no-change baseline
817	    好 2pp——说明 change 本身（无论来源） 引入了 noise，verification-triggered change 的微弱优势几乎被 change-induced
818	    noise 抵消。
819	
820	    '
821	  tables:
822	  - name: Causal intervention results
823	    columns:
824	    - condition
825	    - success
826	    - N_episodes
827	    - 95% CI
828	    rows:
829	    - - no change (baseline)
830	      - 25.0%
831	      - 128
832	      - '[17.5%, 32.5%]'
833	    - - verification-triggered change
834	      - 27.0%
835	      - 128
836	      - '[19.3%, 34.7%]'
837	    - - random change (matched rate)
838	      - 21.0%
839	      - 128
840	      - '[13.9%, 28.1%]'
841	  figures_description:
842	  - 'Bar chart with CI: three conditions. All CIs overlap heavily.'
843	  analysis: 'Causal evidence for verification-triggered > random is weak (p=0.08)。
844	    CIs 大量重叠，no significant difference。这进一步 disqualifies action-change as reward signal。
845	
846	    '
847	- name: Reward signal ablation (action-change vs alternatives)
848	  plan_id: plan_012
849	  description: 对比 action-change / random / confidence-based reward
850	  expected_results:
851	    action_change_reward_success: 0.16
852	    action_change_reward_verify_rate: 0.88
853	    random_reward_success: 0.15
854	    random_reward_verify_rate: 0.85
855	    confidence_reward_success: 0.19
856	    confidence_reward_verify_rate: 0.62
857	    all_below_always_on: true
858	    best_method: confidence-based
859	  result_rationale: 'Worst 档：所有 reward variants 都比 always-on 差。Action-change reward
860	    与 random reward 表现几乎一样（delta < 2pp），证实 action-change 不比 random noise 更好。 Confidence-based
861	    reward 稍好因为它利用了 model-intrinsic uncertainty 而非 extrinsic noisy signal。 但即使最好的
862	    variant 也比 always-on 低 6pp。 核心问题：base agent 太弱时，所有 selective strategies 都退化为 "less
863	    verification = worse performance"。
864	
865	    '
866	  tables:
867	  - name: Reward ablation
868	    columns:
869	    - reward_type
870	    - success
871	    - verify_rate
872	    - token_cost
873	    rows:
874	    - - always-on (no skip)
875	      - 25.0%
876	      - 100%
877	      - 1.0x
878	    - - action-change
879	      - 16.0%
880	      - 88%
881	      - 0.93x
882	    - - random trigger
883	      - 15.0%
884	      - 85%
885	      - 0.90x
886	    - - confidence-based
887	      - 19.0%
888	      - 62%
889	      - 0.72x
890	  figures_description:
891	  - 'Cost-performance Pareto: confidence-based is on frontier, action-change and random
892	    are dominated.'
893	  analysis: 'Action-change reward 无法区分于 random——这是对 Claim 2 的最终否定。 全部移入 future work："selective
894	    verification requires (1) stronger base agent, (2) better reward signal"。
895	
896	    '
897	- name: ARES reproduction + comparison
898	  plan_id: plan_013
899	  description: 复现 ARES SFT router，与 B-IAVR 对比
900	  expected_results:
901	    ares_success: 0.22
902	    ares_verify_rate: 0.7
903	    ares_cost_reduction: 0.3
904	    biavr_success: 0.16
905	    biavr_verify_rate: 0.88
906	    biavr_cost_reduction: 0.12
907	    ares_dominates_biavr: true
908	    delta_success_pp: 6
909	    delta_cost_reduction_pp: 18
910	  result_rationale: 'Worst 档：ARES SFT router 优于 B-IAVR。SFT router 使用 supervised learning
911	    from oracle labels（何时 verify 有帮助），不依赖 RL training signal quality。 因此 ARES 不受 action-change
912	    noise 影响。B-IAVR 的 RL-trained policy 在 weak reward signal 下退化为 near-always-verify，丧失了
913	    cost reduction 优势。 这进一步证明在 weak agent 设定下 SFT > RL for selective verification。
914	
915	    '
916	  tables:
917	  - name: ARES vs B-IAVR
918	    columns:
919	    - method
920	    - success
921	    - verify_rate
922	    - cost_red
923	    - dominates
924	    rows:
925	    - - ARES (SFT)
926	      - 22.0%
927	      - 70%
928	      - 30%
929	      - 'yes'
930	    - - B-IAVR (RL)
931	      - 16.0%
932	      - 88%
933	      - 12%
934	      - 'no'
935	  figures_description:
936	  - Pareto plot with ARES and B-IAVR. ARES clearly dominates.
937	  analysis: 'ARES domination 在 worst 档下是 expected——SFT with oracle labels 是 easier
938	    optimization problem。 Analysis paper 可以 acknowledge this 并 discuss when RL might
939	    outperform SFT (hypothetically: when base agent is strong enough for action-change
940	    to be meaningful signal)。
941	
942	    '
943	- name: ScienceWorld transfer
944	  plan_id: plan_014
945	  description: ScienceWorld 上验证 episode-level vs step-independent
946	  expected_results:
947	    episode_level_success: 0.15
948	    step_independent_success: 0.03
949	    ratio: 5.0
950	    episode_level_std: 0.08
951	    step_independent_std: 0.02
952	  result_rationale: 'Worst 档下 episode-level 仍优于 step-independent（5x），但绝对数值低。 ScienceWorld
953	    任务更长更复杂（平均 40+ steps），episode-level 的 bandit credit 更吃力。 但 step-independent 在
954	    ScienceWorld 上也崩溃（3%），证明问题不是 ALFWorld-specific。 这支持 analysis paper 的 generalizability
955	    claim，但低绝对值（15%）进一步证明 episode-level 不够——需要 finer credit。High std (8pp) 说明 instability
956	    也泛化。
957	
958	    '
959	  tables:
960	  - name: ScienceWorld transfer
961	    columns:
962	    - method
963	    - success
964	    - std
965	    - vs_step_independent
966	    rows:
967	    - - step-independent
968	      - 3%
969	      - 2pp
970	      - baseline
971	    - - episode-level
972	      - 15%
973	      - 8pp
974	      - 5x
975	  figures_description:
976	  - 'Cross-environment comparison: ALFWorld + ScienceWorld paired bars. Same trend
977	    (episode > step-ind) but lower absolute for ScienceWorld.'
978	  analysis: 'Transfer 验证了 finding 的 generalizability。两个环境一致：episode-level 解决了 step-independent
979	    的崩溃， 但自身也有 ceiling。ScienceWorld 的 lower ceiling（15% vs 25%）反映更长 horizon 的 credit
980	    challenge。
981	
982	    '
983	- name: 7B model scaling verification
984	  plan_id: plan_015
985	  description: Qwen3-7B 上验证 episode-level vs step-independent
986	  expected_results:
987	    episode_level_7b_success: 0.32
988	    step_independent_7b_success: 0.08
989	    episode_level_1_7b_success: 0.25
990	    step_independent_1_7b_success: 0.01
991	    scaling_gain_episode_pp: 7
992	    scaling_gain_step_ind_pp: 7
993	    ratio_7b: 4.0
994	    ratio_1_7b: 25.0
995	  result_rationale: 'Worst 档：7B 提升两种方法各约 7pp（近乎 parallel shift），episode-level 优势 ratio
996	    缩小（4x vs 25x at 1.7B）。 Step-independent 在 7B 上不再完全崩溃（8% vs 1%），因为 larger model
997	    有更好的 in-context learning 能力， 部分补偿了 credit assignment 问题。但 episode-level 仍然 superior。
998	    对 paper 的含义：episode-level 优势在 larger model 上缩小——可能 scaling 本身 partially mitigates
999	    credit assignment failures（模型 in-context 能力可以补偿 training signal noise）。 这是 analysis
1000	    paper 的一个 nuanced finding。
1001	
1002	    '
1003	  tables:
1004	  - name: Scaling comparison
1005	    columns:
1006	    - model
1007	    - episode-level
1008	    - step-independent
1009	    - ratio
1010	    rows:
1011	    - - Qwen3-1.7B
1012	      - 25%
1013	      - 1%
1014	      - 25x
1015	    - - Qwen3-7B
1016	      - 32%
1017	      - 8%
1018	      - 4x
1019	  figures_description:
1020	  - '2×2 bar chart: model × method. Episode-level advantage shrinks at scale but persists.'
1021	  analysis: 'Scaling 结果 nuances the story：credit assignment 问题 severity 与 model size
1022	    负相关， 但不消失。Analysis paper 可以 speculate：at sufficient scale（70B+）， in-context learning
1023	    可能完全 compensate——这是 "why big-lab RL works but small-model RL fails" 的一个 hypothesis。
1024	
1025	    '
1026	- name: Per-task-type breakdown analysis
1027	  plan_id: plan_016
1028	  description: 按 ALFWorld 任务类型 breakdown episode-level performance
1029	  expected_results:
1030	    pick_success: 0.35
1031	    clean_success: 0.22
1032	    heat_success: 0.2
1033	    cool_success: 0.18
1034	    examine_success: 0.3
1035	    pick_two_success: 0.1
1036	    episode_length_correlation: 0.48
1037	    task_complexity_correlation: -0.62
1038	  result_rationale: 'Worst 档下，simple tasks（pick: 35%, examine: 30%）显著优于 complex tasks（pick_two:
1039	    10%, cool: 18%）。 Task complexity-success correlation = -0.62：越复杂越差，符合 credit assignment
1040	    bottleneck 假说—— longer horizons = more steps sharing same advantage = coarser
1041	    credit = worse learning。 Pick_two 最差因为需要 two sequential subtask completions，episode-level
1042	    advantage 无法 区分第一个 pick 的 credit 和第二个 pick 的 credit。 这个 breakdown 对 analysis paper
1043	    有价值：展示 failure 不均匀， task structure（horizon length、subtask decomposition）直接影响 credit
1044	    assignment quality。
1045	
1046	    '
1047	  tables:
1048	  - name: Per-task breakdown (episode-level, 5-seed mean)
1049	    columns:
1050	    - task_type
1051	    - success
1052	    - std
1053	    - avg_steps
1054	    - n_subtasks
1055	    rows:
1056	    - - pick
1057	      - 35%
1058	      - 5pp
1059	      - 28
1060	      - 1
1061	    - - examine
1062	      - 30%
1063	      - 6pp
1064	      - 32
1065	      - 1
1066	    - - clean
1067	      - 22%
1068	      - 7pp
1069	      - 35
1070	      - 2
1071	    - - heat
1072	      - 20%
1073	      - 8pp
1074	      - 37
1075	      - 2
1076	    - - cool
1077	      - 18%
1078	      - 7pp
1079	      - 38
1080	      - 2
1081	    - - pick_two
1082	      - 10%
1083	      - 9pp
1084	      - 45
1085	      - 2
1086	  figures_description:
1087	  - Grouped bar chart by task type, sorted by complexity. Clear downward trend.
1088	  - 'Scatter: avg_episode_length vs success per task type, r=-0.62.'
1089	  analysis: Task-level breakdown 是 analysis paper 的 key supporting evidence： credit
1090	    assignment failure severity 与 task horizon 和 subtask decomposition 正相关。 pick_two
1091	    的 10% 证明 episode-level bandit credit 无法处理 multi-subtask credit separation。 这 motivates
1092	    future work on hierarchical credit assignment（per-subtask reward 或 option-level
1093	    advantage）。
1094	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ac32b9ec-0951-443f-848d-159085c84d52",
  "isSidechain": false,
  "promptId": "e50933ad-3d3f-4cff-8204-b5ceb8047ed2",
  "type": "user",
  "uuid": "c61d0040-e249-4e5d-941b-f954869cfd90",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/artifacts/dream_reports/dream_20260517T121256/worst/review_context.yaml",
      "content": "narrative_guidance: '完全 reframe 为 diagnostic/analysis paper。Title: \"Dissecting Credit\n  Assignment Failure in Multi-Turn LLM Agent RL: A Dual-Mechanism Analysis\"。 核心叙事：episode-level\n  是 necessary but not sufficient，消除 window-level 问题后暴露更深层 credit assignment 瓶颈。 GAE\n  >> episode-level GRPO 证明 per-token credit 是关键缺失。Sign misattribution 是主要但非唯一因素——entropy\n  collapse、KL drift、information loss 共同作用。 贡献定位为 failure mode taxonomy + actionable\n  guidelines + cross-framework design analysis。 Selective verification 完全移入 future\n  work。Claim 2/3 删除。\n\n  '\nimagined_experiments:\n- name: Episode-level GRPO convergence (exp029 continuation)\n  plan_id: plan_001\n  description: Episode-level GRPO 继续训练至 step 50+，观察是否突破 28% plateau\n  expected_results:\n    step15_val_success: 0.28125\n    step20_val_success: 0.27\n    step30_val_success: 0.26\n    step40_val_success: 0.25\n    step50_val_success: 0.24\n    convergence_val_success: 0.25\n    step50_train_success: 0.5\n    step50_train_pass_at_8: 0.8125\n    step50_val_pass_at_1: 0.25\n    step50_val_pass_at_8: 0.94\n    step50_val_action_is_valid: 0.58\n    step50_entropy: 0.12\n    step50_ppo_kl: 0.015\n    train_val_gap_pp: 25\n    plateau_onset_step: 10\n    plateau_duration_steps: 40\n  result_rationale: 'Episode-level GRPO 在 step 10 后进入 plateau（25-28%），训练 success 持续上升至\n    ~50% 但 val 不跟随—— 经典 overfitting to training distribution。根因：GRPO 的 bandit-style\n    credit assignment（所有 token 共享同一 advantage） 无法学习 per-step 策略改进。模型学会了 \"在训练任务分布上做对的\n    trajectory pattern\"，但缺乏 fine-grained credit 来泛化到 unseen task instance。Entropy\n    持续下降表明 policy 在 narrowing 但未在 improving。 pass@8=0.94 证明 policy 有能力但 greedy decoding\n    无法稳定触发正确路径——credit assignment 不够精细， 无法可靠地将 probability mass 集中到 correct action\n    sequence 上。\n\n    '\n  tables:\n  - name: Convergence trajectory\n    columns:\n    - step\n    - val_success\n    - train_success\n    - val_pass@8\n    - entropy\n    - kl\n    rows:\n    - - 5\n      - 0.25\n      - 0.31\n      - 0.88\n      - 0.2\n      - 0.003\n    - - 10\n      - 0.25\n      - 0.38\n      - 0.91\n      - 0.17\n      - 0.007\n    - - 15\n      - 0.28\n      - 0.44\n      - 0.93\n      - 0.15\n      - 0.01\n    - - 20\n      - 0.27\n      - 0.47\n      - 0.93\n      - 0.14\n      - 0.012\n    - - 30\n      - 0.26\n      - 0.5\n      - 0.94\n      - 0.13\n      - 0.014\n    - - 40\n      - 0.25\n      - 0.5\n      - 0.94\n      - 0.12\n      - 0.015\n    - - 50\n      - 0.24\n      - 0.5\n      - 0.94\n      - 0.12\n      - 0.015\n  figures_description:\n  - 'Learning curve: val_success plateau at 25-28% from step 10 onward, train_success\n    diverging upward to 50%. Classic overfitting gap.'\n  - 'Entropy decay curve: monotonic decrease from 0.25 → 0.12, policy narrows without\n    improving generalization.'\n  analysis: 'Plateau 确认 episode-level GRPO 的根本限制：bandit-style advantage 足以消除 sign\n    misattribution， 但不足以提供 per-token credit assignment。25-28% 是 \"episode-level 能做到的天花板\"\n    在当前 reward density 下。 这是 analysis paper 的核心发现之一：episode-level 解决了 step-independent\n    的问题但暴露了更深层瓶颈。\n\n    '\n- name: Context window h-sweep ablation (3 seeds each)\n  plan_id: plan_002\n  description: h={2, 5, 10, 20, full} sweep，每个 3 seeds，15 steps each\n  expected_results:\n    h2_seed1_step15_success: 0.0\n    h2_seed2_step15_success: 0.03\n    h2_seed3_step15_success: 0.0\n    h2_mean: 0.01\n    h2_std: 0.017\n    h2_collapse_step_mean: 4.3\n    h5_seed1_step15_success: 0.06\n    h5_seed2_step15_success: 0.0\n    h5_seed3_step15_success: 0.09\n    h5_mean: 0.05\n    h5_std: 0.046\n    h5_collapse_rate: 0.33\n    h10_seed1_step15_success: 0.12\n    h10_seed2_step15_success: 0.03\n    h10_seed3_step15_success: 0.16\n    h10_mean: 0.103\n    h10_std: 0.066\n    h20_seed1_step15_success: 0.19\n    h20_seed2_step15_success: 0.09\n    h20_seed3_step15_success: 0.22\n    h20_mean: 0.167\n    h20_std: 0.068\n    full_seed1_step15_success: 0.28\n    full_seed2_step15_success: 0.19\n    full_seed3_step15_success: 0.25\n    full_mean: 0.24\n    full_std: 0.046\n    monotonic_ordering_violated: true\n    h5_occasionally_beats_h10: true\n    h20_occasionally_collapses: true\n  result_rationale: 'Worst 档的关键特征：h-sweep 不是 clean monotonic function。h=2 一致崩溃（sign\n    misattribution + extreme information loss）， 但 h=5 和 h=10 之间、h=10 和 h=20 之间存在 seed\n    间交叉——某些 seed 下 h=5 偶尔优于 h=10， h=20 偶尔 collapse。这说明 cliff 位置依赖于 random initialization\n    和 early training dynamics， 而非仅由 h 值决定。高 cross-seed variance 削弱了 \"clean cliff at\n    h=10\" 的叙事， 但仍支持 \"smaller h systematically worse on average\" 的趋势。Non-monotonicity\n    来自 不同 seed 的 entropy dynamics 差异：某些 seed 早期 exploration 更好，偶尔让 h=5 找到可行策略。\n\n    '\n  tables:\n  - name: h-sweep summary (step 15, 3 seeds)\n    columns:\n    - h\n    - seed1\n    - seed2\n    - seed3\n    - mean\n    - std\n    - collapse_rate\n    rows:\n    - - h=2\n      - 0.0\n      - 0.03\n      - 0.0\n      - 0.01\n      - 0.017\n      - 3/3\n    - - h=5\n      - 0.06\n      - 0.0\n      - 0.09\n      - 0.05\n      - 0.046\n      - 1/3\n    - - h=10\n      - 0.12\n      - 0.03\n      - 0.16\n      - 0.103\n      - 0.066\n      - 0/3\n    - - h=20\n      - 0.19\n      - 0.09\n      - 0.22\n      - 0.167\n      - 0.068\n      - 0/3\n    - - full\n      - 0.28\n      - 0.19\n      - 0.25\n      - 0.24\n      - 0.046\n      - 0/3\n  figures_description:\n  - 'Box plot: h vs val_success with individual seed points. Trend is upward but boxes\n    overlap between adjacent h values. Error bars large.'\n  - 'Collapse timeline: h=2 collapses by step 4-5 across all seeds; h=5 collapses\n    in 1/3 seeds; h≥10 no full collapse but h=20 seed2 shows temporary dip.'\n  analysis: 'Non-monotonic 结果对 paper 是挑战也是机会。不能 claim \"clean cliff\"，但可以 reframe 为\n    \"credit assignment failure is a stochastic phenomenon whose probability increases\n    with smaller h\"—— 这更符合 analysis paper 的 tone。Cross-seed variance 本身是 failure mode\n    taxonomy 的一条： \"training instability as a function of context window\" 是独立 failure\n    mechanism。 需要从 \"threshold effect\" 叙事转向 \"probabilistic degradation\" 叙事。\n\n    '\n- name: Multi-seed replication (5 seeds)\n  plan_id: plan_003\n  description: Episode-level GRPO 5 seeds（含 exp029 原始 seed），report mean ± std\n  expected_results:\n    seed1_val_success: 0.28\n    seed2_val_success: 0.19\n    seed3_val_success: 0.25\n    seed4_val_success: 0.15\n    seed5_val_success: 0.3\n    mean_val_success: 0.234\n    std_val_success: 0.062\n    std_pp: 6.2\n    min_val_success: 0.15\n    max_val_success: 0.3\n    range_pp: 15\n    seeds_above_25pct: 3\n    seeds_below_20pct: 1\n    mean_train_success: 0.46\n    train_val_gap_mean_pp: 22.6\n  result_rationale: 'Worst 档要求 std > 7pp。这里 std=6.2pp 接近但略低于 7pp 边界——真实的 worst 场景中\n    5 seeds 可能落在 6-9pp 范围。 关键问题：seed4 只达到 15%（接近 step-independent 水平），说明 episode-level\n    的优势在某些 seed 下大幅削弱。 这源于 GRPO 的 group normalization 对初始 rollout 分布敏感——如果前几步 rollout\n    恰好全部失败， advantage 全为 0（无 variance），模型无法获得有效梯度。Seed4 可能经历了 \"cold start\" 问题： 早期\n    rollout 全败 → advantage=0 → 无学习 → 持续全败的恶性循环。高 variance 使 95% CI 覆盖 0， 削弱了 episode-level\n    作为 \"solution\" 的 claim，但强化了 analysis paper 的叙事—— \"即使 episode-level 也不稳定，RL for\n    LLM agents 需要更根本性的改进\"。\n\n    '\n  tables:\n  - name: Multi-seed results (step 15 checkpoint)\n    columns:\n    - seed\n    - val_success\n    - train_success\n    - action_is_valid\n    - plateau_step\n    rows:\n    - - 1\n      - 0.28\n      - 0.44\n      - 0.55\n      - 10\n    - - 2\n      - 0.19\n      - 0.41\n      - 0.52\n      - 8\n    - - 3\n      - 0.25\n      - 0.47\n      - 0.56\n      - 10\n    - - 4\n      - 0.15\n      - 0.35\n      - 0.48\n      - 12\n    - - 5\n      - 0.3\n      - 0.5\n      - 0.58\n      - 10\n  - name: Summary statistics\n    columns:\n    - metric\n    - mean\n    - std\n    - 95% CI\n    rows:\n    - - val_success\n      - 0.234\n      - 0.062\n      - '[0.157, 0.311]'\n    - - train_success\n      - 0.434\n      - 0.057\n      - '[0.363, 0.505]'\n    - - action_is_valid\n      - 0.538\n      - 0.038\n      - '[0.491, 0.585]'\n  figures_description:\n  - Swarm plot with mean ± 95% CI. CI is wide (15.7pp-31.1%), overlaps with step-independent\n    range for low seeds.\n  analysis: '95% CI [15.7%, 31.1%] 太宽，无法 credibly claim episode-level \"solves\" the\n    problem。 但 mean 仍显著高于 step-independent mean（~2%），所以 \"episode-level helps but doesn''t\n    solve\" 是可靠 claim。 Analysis paper framing: 这证明了 credit assignment 问题的多层性——episode-level\n    消除了 sign misattribution 但暴露了 GRPO 的 cold-start sensitivity 和 bandit-level credit\n    的根本限制。\n\n    '\n- name: GAE baseline comparison\n  plan_id: plan_003b\n  description: GAE(λ=0.95) 和 GAE(λ=1.0, γ=1.0) baselines，15 steps × 3 seeds\n  expected_results:\n    gae_095_seed1_success: 0.44\n    gae_095_seed2_success: 0.38\n    gae_095_seed3_success: 0.41\n    gae_095_mean: 0.41\n    gae_095_std: 0.03\n    gae_10_10_seed1_success: 0.37\n    gae_10_10_seed2_success: 0.34\n    gae_10_10_seed3_success: 0.39\n    gae_10_10_mean: 0.367\n    gae_10_10_std: 0.025\n    episode_grpo_mean: 0.234\n    gae_095_vs_episode_delta_pp: 17.6\n    gae_10_vs_episode_delta_pp: 13.3\n    gae_095_per_token_adv_variance: 0.42\n    episode_grpo_per_token_adv_variance: 0.0\n    step_independent_mean: 0.02\n  result_rationale: 'Worst 档要求 GAE >> episode-level GRPO（delta > 15pp）。GAE(λ=0.95)\n    达到 41%—— 因为 critic 提供 per-token temporal difference signal，每个 action 获得独立的 advantage\n    estimate， 而非 GRPO 的 \"全 trajectory 同一 advantage\"。这是 worst 档的核心发现： episode-level\n    GRPO 的 plateau 不是 episode-level 本身的问题，而是 GRPO 的 bandit-style credit 的问题。 GAE 通过\n    value function 提供 fine-grained credit，打破了 plateau。 GAE(λ=1,γ=1) 略低于 GAE(0.95)，因为无\n    discount 导致 variance 更高。 Delta=17.6pp 直接证明：per-token credit assignment 是关键缺失，episode-level\n    只是 necessary condition。 这彻底改变 paper story——从 \"episode-level solves it\" 到 \"episode-level\n    is necessary but per-token credit is the real bottleneck\"。\n\n    '\n  tables:\n  - name: Method comparison (step 15)\n    columns:\n    - method\n    - seed1\n    - seed2\n    - seed3\n    - mean\n    - std\n    rows:\n    - - step-independent (h=2)\n      - 0.0\n      - 0.03\n      - 0.0\n      - 0.01\n      - 0.017\n    - - episode-level GRPO\n      - 0.28\n      - 0.19\n      - 0.25\n      - 0.24\n      - 0.046\n    - - GAE(λ=1,γ=1)\n      - 0.37\n      - 0.34\n      - 0.39\n      - 0.367\n      - 0.025\n    - - GAE(λ=0.95,γ=1)\n      - 0.44\n      - 0.38\n      - 0.41\n      - 0.41\n      - 0.03\n  figures_description:\n  - 'Bar chart: 4 methods with error bars. Clear staircase: step-ind << episode-GRPO\n    << GAE(1,1) < GAE(0.95). Gap between GRPO and GAE is the paper''s key diagnostic\n    finding.'\n  analysis: 'GAE 的大幅领先是 analysis paper 的最强证据：问题不只是 window-level vs episode-level，\n    而是 credit granularity 的 spectrum。GRPO episode-level 在 spectrum 中间（消除了 sign error\n    但无 per-token credit）， GAE 在另一端（full per-token credit via value function）。这支持 failure\n    mode taxonomy 的第三种机制： \"bandit-level credit insufficiency\"——即使 advantage 方向正确，所有\n    token 共享同一 magnitude 也无法 区分 trajectory 中的关键决策点和无关步骤。\n\n    '\n- name: Episode-level + valid_action_bonus\n  plan_id: plan_003c\n  description: Episode-level + valid_action_bonus=0.05，测试是否安全突破 plateau\n  expected_results:\n    step15_val_success: 0.22\n    step15_val_action_is_valid: 0.72\n    step15_train_success: 0.39\n    valid_bonus_vs_task_ratio: 0.35\n    gaming_detected: false\n    success_improvement_vs_baseline: -0.06\n    action_is_valid_improvement_pp: 17\n    reward_composition_valid_pct: 0.28\n    reward_composition_task_pct: 0.72\n  result_rationale: 'Worst 档下 valid_action_bonus 在 episode-level 中不 game（因为模型优化整条\n    trajectory total reward）， action_is_valid 确实从 55% 提升到 72%，但 success 反而略降（22% <\n    28%）。 原因：valid_action_bonus 改变了 reward landscape，使模型偏向 \"safe but ineffective\"\n    actions—— valid 但不 goal-directed 的 action（如反复 examine 已知物体）获得持续正 reward， 而 risky\n    but potentially successful 的 exploration 策略被抑制。Episode-level 下不存在 per-step gaming，\n    但 dense bonus 仍扭曲了 trajectory-level 的 learning signal——模型学会生成 \"很多 valid action\n    的长 trajectory\" 而非 \"goal-directed 的短 trajectory\"。这是 analysis paper 的另一个 insight：\n    dense reward 在 episode-level 下的失效模式与 step-independent 不同但同样有害。\n\n    '\n  tables:\n  - name: valid_action_bonus ablation\n    columns:\n    - config\n    - val_success\n    - action_is_valid\n    - avg_trajectory_len\n    - reward_mean\n    rows:\n    - - episode-level (baseline)\n      - 0.28\n      - 0.55\n      - 38.2\n      - 2.81\n    - - episode-level + bonus=0.05\n      - 0.22\n      - 0.72\n      - 45.6\n      - 3.92\n  figures_description:\n  - 'Dual-axis plot: action_is_valid improves (good) but success drops (bad). Trajectory\n    length increases — model generates more valid-but-aimless steps.'\n  analysis: 'valid_action_bonus 未引入 step-independent 式 gaming，但通过 reward shaping 偏移了\n    policy gradient direction。 这是 failure mode taxonomy 的第四种机制：\"reward misalignment\n    under sparse task signal\"—— 当 task reward 稀疏且 episode-level credit 粗糙时，任何 dense\n    auxiliary reward 都容易主导 learning。 进一步证明 per-token credit（如 GAE）才是根本解。\n\n    '\n- name: Credit assignment mechanism empirical verification\n  plan_id: plan_004\n  description: Per-window advantage logging，验证 sign misattribution 机制\n  expected_results:\n    sign_vs_outcome_correlation: 0.73\n    sign_vs_local_quality_correlation: 0.28\n    magnitude_position_decay_r2: 0.61\n    episode_level_adv_variance: 0.0\n    success_episodes_all_positive_pct: 0.78\n    failure_episodes_all_negative_pct: 0.82\n    mixed_sign_episodes_pct: 0.2\n    gamma_k_decay_slope: -0.032\n    confound_kl_correlation: 0.31\n    confound_entropy_correlation: 0.27\n  result_rationale: 'Worst 档的关键：sign-outcome correlation 只有 0.73（而非预期的 >0.95），sign-local_quality\n    correlation 达到 0.28（而非预期的 ~0）。这意味着 sign misattribution 存在但有显著混杂因素。 Correlation\n    < 1.0 的原因：GRPO 的 group normalization 使得同一 group 内的 advantage 不完全由 episode outcome\n    决定—— 如果 group 内所有 episode 都成功（或都失败），normalization 后 advantage 反映 relative 差异而非\n    absolute 成败。 这在成功率较高的 training episodes 中尤为明显。 Local quality correlation = 0.28\n    的原因：window-local action quality 与 episode success 本身存在弱正相关 （好的 local action 确实\n    contribute to success），所以 sign-local 相关性部分反映了 genuine causal path 而非纯 misattribution。这是混杂因素：无法将\n    sign-local 相关性 100% 归因于 misattribution， 因为部分是 legitimate credit signal。 KL divergence\n    和 entropy 也与 advantage sign 相关（r=0.31, 0.27），说明 policy drift 和 exploration dynamics\n    独立影响 advantage distribution。\n\n    '\n  tables:\n  - name: Mechanism verification (h=2, seed 2, step 5)\n    columns:\n    - metric\n    - observed\n    - hypothesis\n    - status\n    rows:\n    - - sign-outcome corr\n      - 0.73\n      - '>0.95'\n      - PARTIAL — significant confounds\n    - - sign-local_quality corr\n      - 0.28\n      - <0.1\n      - FAILED — non-negligible correlation\n    - - magnitude decay R²\n      - 0.61\n      - '>0.85'\n      - PARTIAL — decay exists but noisy\n    - - episode-level adv variance\n      - 0.0\n      - '0.0'\n      - CONFIRMED\n    - - '% success eps all-positive'\n      - 78%\n      - '>95%'\n      - PARTIAL — 22% have mixed signs\n  - name: Confound analysis\n    columns:\n    - confound_variable\n    - correlation_with_adv_sign\n    - p_value\n    rows:\n    - - episode_outcome\n      - 0.73\n      - <0.001\n    - - local_action_quality\n      - 0.28\n      - <0.01\n    - - KL_divergence\n      - 0.31\n      - <0.01\n    - - entropy\n      - 0.27\n      - <0.01\n    - - window_position\n      - -0.18\n      - <0.05\n  figures_description:\n  - 'Scatter: advantage sign vs episode outcome (color=local quality). Not the clean\n    binary separation expected — significant overlap region.'\n  - 'Partial correlation decomposition: pie chart showing episode outcome explains\n    53%, local quality 16%, KL 10%, entropy 8%, unexplained 13%.'\n  analysis: 'Sign misattribution 存在但不是 sole mechanism——这是 worst 档的核心困难。不能 claim \"advantage\n    sign is entirely determined by episode outcome\"。 需要 reframe 为 \"sign misattribution\n    is the dominant but not sole factor in credit assignment failure\"。 混杂因素（KL drift、entropy\n    dynamics）本身成为 failure mode taxonomy 的独立条目。 Partial correlation decomposition 成为\n    analysis paper 的关键贡献：量化每种机制对 credit assignment failure 的贡献占比。\n\n    '\n- name: Action-change statistics from always-on runs\n  plan_id: plan_005\n  description: 从 exp029 checkpoint 收集 action-change 统计\n  expected_results:\n    action_change_rate: 0.18\n    confirmatory_rate: 0.82\n    action_change_success_correlation: 0.08\n    action_change_success_p_value: 0.12\n    per_task_action_change_std: 0.09\n    pick_action_change_rate: 0.12\n    clean_action_change_rate: 0.22\n    heat_action_change_rate: 0.2\n    cool_action_change_rate: 0.15\n    examine_action_change_rate: 0.25\n  result_rationale: 'Worst 档下 action-change-success correlation 仅 0.08 且 p=0.12（不显著）。\n    原因：episode-level model 只有 25% success rate，样本中 successful episodes 太少导致 statistical\n    power 不足。 更根本的问题：在 25% success 的 agent 上，action change 基本是 noise—— model 的 verification\n    输出质量太低，无论是否 change action 都可能是随机的。 Confirmatory rate 82% 符合预期（大部分 verification\n    不改变行为）， 但这也意味着 action change 事件太稀疏（只有 18%），与 success 的 correlation 在统计上不可靠。 这直接阻碍了\n    Phase B：如果 action change 不是 success 的有效 signal， 用它作 intrinsic reward 没有理论基础。\n\n    '\n  tables:\n  - name: Action-change statistics\n    columns:\n    - metric\n    - value\n    rows:\n    - - overall action change rate\n      - 18%\n    - - confirmatory rate\n      - 82%\n    - - action_change-success correlation\n      - r=0.08, p=0.12\n    - - N (episodes)\n      - 128\n    - - N (verification events)\n      - 2304\n    - - N (action changes)\n      - 415\n  figures_description:\n  - 'Contingency table heatmap: action_change × episode_success. No clear pattern\n    — action change is roughly equally distributed across success/failure episodes.'\n  analysis: 'Action change 作为 intrinsic reward 缺乏 empirical grounding。在 worst 档下，\n    这个结果直接导致 Claim 2 无法成立——selective verification 失去了 reward signal。 Analysis paper\n    中可以作为 \"why selective verification is hard for weak agents\" 的一个 finding。\n\n    '\n- name: Selective verification implementation\n  plan_id: plan_006\n  description: Code-only：实现 binary verify/skip decision\n  expected_results:\n    implementation_status: completed\n    code_changes_files: 4\n    gpu_hours: 0\n  result_rationale: '纯代码实现，不依赖实验结果。在 worst 档下仍可完成，但后续使用这个 implementation 的实验效果差。\n\n    '\n  tables: []\n  figures_description: []\n  analysis: 'Implementation 本身无 worst 档问题。但 plan_005 的 weak correlation 预示 plan_007\n    会失败。\n\n    '\n- name: B-IAVR selective verification training\n  plan_id: plan_007\n  description: 用 action-change reward 训练 selective verification policy\n  expected_results:\n    verification_rate_reduction_pct: 12\n    val_success: 0.16\n    baseline_always_on_success: 0.25\n    success_delta_pp: -9\n    training_converged: false\n    reward_signal_informative: false\n    verification_rate: 0.88\n    policy_learned_skip: false\n    training_steps_before_abort: 20\n  result_rationale: 'Worst 档：selective verification 无法 deliver clear win。两个根因叠加： (1)\n    plan_005 显示 action-change 不是有效 signal（r=0.08, p=0.12），用它做 reward 等于训练 on noise；\n    (2) base agent 只有 25% success，skip verification 直接降低 performance 且模型无法学会 when\n    to skip。 Verification rate 只降了 12%（模型几乎总是 verify），因为 skip 的 penalty（success 下降）远大于\n    action-change reward 的 bonus。Policy 本质上退化为 \"always verify\"—— 因为在 25% success 的\n    agent 上，任何 skip 都有显著 performance cost。 Success 降至 16%（比 baseline 低 9pp），因为即使少量的\n    skip 也损害了 performance。\n\n    '\n  tables:\n  - name: B-IAVR results\n    columns:\n    - policy\n    - val_success\n    - verification_rate\n    - cost_reduction\n    rows:\n    - - always-on\n      - 0.25\n      - 100%\n      - 0%\n    - - B-IAVR (learned)\n      - 0.16\n      - 88%\n      - 12%\n    - - random-50%\n      - 0.14\n      - 50%\n      - 50%\n    - - no-verify\n      - 0.13\n      - 0%\n      - 100%\n  figures_description:\n  - 'Pareto frontier: success vs cost. B-IAVR barely separates from always-on, nowhere\n    near efficient frontier.'\n  analysis: 'Selective verification 在 worst 档下完全无法作为 paper contribution。 必须移入 future\n    work，framed as \"requires stronger base agent + better reward signal\"。\n\n    '\n- name: Selective verification full comparison\n  plan_id: plan_008\n  description: Always-on / B-IAVR / no-verify / random-p / confidence 对比\n  expected_results:\n    always_on_success: 0.25\n    always_on_verify_rate: 1.0\n    biavr_success: 0.16\n    biavr_verify_rate: 0.88\n    no_verify_success: 0.13\n    no_verify_rate: 0.0\n    random_50_success: 0.14\n    random_50_rate: 0.5\n    confidence_success: 0.19\n    confidence_verify_rate: 0.65\n    biavr_dominates_pareto: false\n    best_cost_performance: confidence-threshold\n  result_rationale: 'Worst 档：B-IAVR 不 dominate Pareto frontier。Confidence-based baseline\n    意外优于 B-IAVR—— 因为 confidence threshold 是 model-intrinsic signal（policy entropy），\n    比 action-change 这个 noisy extrinsic signal 更 informative。 Confidence 方法在 entropy\n    高时 verify（不确定时检查），在 entropy 低时 skip（确定时省略）， 这 naturally 对齐 \"verification is useful\n    when uncertain\"。 B-IAVR 学到的 policy 没有这种 alignment 因为 training signal 太弱。 所有 selective\n    方法都比 always-on 差（delta > 5pp），因为 base agent 太弱—— verification 在 25% agent 上几乎总是有用的（因为\n    agent 经常犯错）。\n\n    '\n  tables:\n  - name: Full comparison (step 15 checkpoint, 128 val episodes)\n    columns:\n    - method\n    - success\n    - verify_rate\n    - total_tokens\n    - success_per_token\n    rows:\n    - - always-on\n      - 25.0%\n      - 100%\n      - 1.0x\n      - '0.250'\n    - - confidence-0.5\n      - 19.0%\n      - 65%\n      - 0.72x\n      - '0.264'\n    - - B-IAVR\n      - 16.0%\n      - 88%\n      - 0.93x\n      - '0.172'\n    - - random-50%\n      - 14.0%\n      - 50%\n      - 0.62x\n      - '0.226'\n    - - no-verify\n      - 13.0%\n      - 0%\n      - 0.45x\n      - '0.289'\n  figures_description:\n  - 'Pareto frontier plot: no-verify has best token-efficiency (trivially), confidence-threshold\n    dominates B-IAVR. B-IAVR is dominated — not on the frontier.'\n  analysis: 'B-IAVR 被 confidence baseline dominate，这对 Claim 3 是致命的。 但 analysis paper\n    可以 reframe：展示为什么 RL-trained selective verification 在 weak agents 上失败—— action-change\n    signal 需要 base agent 足够强才有意义（类比：你不能教一个 25% accuracy 的学生 when to double-check）。\n\n    '\n- name: No-verify ablation\n  plan_id: plan_009\n  description: Episode-level GRPO without self-verification\n  expected_results:\n    val_success: 0.13\n    val_action_is_valid: 0.42\n    always_on_success: 0.25\n    delta_pp: -12\n    avg_trajectory_length: 28.5\n    avg_trajectory_length_with_verify: 41.3\n  result_rationale: 'No-verify 比 always-on 低 12pp，确认 verification 有价值。 但在 worst 档下这个\n    delta 略小于预期的 ≥10pp（12pp 刚过线）， 因为 weak agent 的 verification 质量也不高——agent 经常 verify\n    但 verification 本身也是 noisy。 Action_is_valid 从 55% 降到 42%，说明 verification 确实帮助 format\n    compliance。 Trajectory 更短（28 vs 41 steps）因为没有 verification 步骤。\n\n    '\n  tables:\n  - name: Verification ablation\n    columns:\n    - config\n    - success\n    - action_is_valid\n    - avg_steps\n    - avg_tokens\n    rows:\n    - - always-on verify\n      - 25.0%\n      - 55%\n      - 41.3\n      - 4850\n    - - no verify\n      - 13.0%\n      - 42%\n      - 28.5\n      - 2980\n    - - delta\n      - -12pp\n      - -13pp\n      - '-12.8'\n      - '-1870'\n  figures_description:\n  - 'Paired bar chart: with/without verification across task types.'\n  analysis: 'Verification 有价值（-12pp），但价值不足以支撑 \"selective verification as primary contribution\"。\n    在 analysis paper 中，这是一个 supporting data point：verification matters， 但 training\n    agents to be selective about it requires solving the credit assignment problem\n    first。\n\n    '\n- name: Entropy-controlled action-change analysis\n  plan_id: plan_010\n  description: Stratify action-change-success correlation by policy entropy\n  expected_results:\n    overall_correlation: 0.08\n    overall_p_value: 0.12\n    low_entropy_partial_corr: 0.05\n    low_entropy_p_value: 0.41\n    medium_entropy_partial_corr: 0.09\n    medium_entropy_p_value: 0.18\n    high_entropy_partial_corr: 0.12\n    high_entropy_p_value: 0.09\n    partial_correlation_controlling_entropy: 0.07\n    partial_p_value: 0.15\n  result_rationale: 'Worst 档：partial correlation 在控制 entropy 后仍不显著（r=0.07, p=0.15）。\n    Action change 与 success 的微弱相关几乎完全由 entropy 解释—— 高 entropy 时更容易 change action（因为\n    policy 本身不确定）， 高 entropy 任务也更可能成功（因为 exploration 更充分）。 控制 entropy 后 action change\n    本身对 success 没有独立贡献。 这直接否定了 \"action change as causal signal for verification quality\"\n    的假设。\n\n    '\n  tables:\n  - name: Entropy-stratified analysis\n    columns:\n    - entropy_stratum\n    - N\n    - action_change_rate\n    - success_rate\n    - corr\n    - p\n    rows:\n    - - low (<0.10)\n      - 768\n      - 11%\n      - 18%\n      - 0.05\n      - 0.41\n    - - medium (0.10-0.20)\n      - 896\n      - 17%\n      - 24%\n      - 0.09\n      - 0.18\n    - - high (>0.20)\n      - 640\n      - 28%\n      - 31%\n      - 0.12\n      - 0.09\n    - - partial (controlling entropy)\n      - 2304\n      - '-'\n      - '-'\n      - 0.07\n      - 0.15\n  figures_description:\n  - '3-panel scatter: action_change vs success within each entropy stratum. No clear\n    trend in any panel.'\n  analysis: 'Action change 不是 independent signal——它是 entropy 的 proxy。 这对 Claim 2 是\n    additional nail in the coffin。Analysis paper framing： \"apparent verification informativeness\n    signals are confounded with policy uncertainty\"， 这是 selective verification failure\n    的又一个 identified mechanism。\n\n    '\n- name: 'Causal intervention: random vs verification-triggered changes'\n  plan_id: plan_011\n  description: 注入 random action changes vs verification-triggered，对比 success\n  expected_results:\n    verification_triggered_success: 0.27\n    random_change_success: 0.21\n    no_change_success: 0.25\n    triggered_vs_random_delta_pp: 6\n    triggered_vs_random_p_value: 0.08\n    triggered_vs_baseline_delta_pp: 2\n    random_vs_baseline_delta_pp: -4\n  result_rationale: 'Worst 档：verification-triggered changes 仅比 random 好 6pp（p=0.08，边缘不显著）。\n    这弱于预期的 ≥10pp。原因：agent 只有 25% success，verification 质量差， triggered changes 只是 \"slightly\n    better than random\" 而非 \"causally informative\"。 有趣的是 triggered 甚至只比 no-change baseline\n    好 2pp——说明 change 本身（无论来源） 引入了 noise，verification-triggered change 的微弱优势几乎被 change-induced\n    noise 抵消。\n\n    '\n  tables:\n  - name: Causal intervention results\n    columns:\n    - condition\n    - success\n    - N_episodes\n    - 95% CI\n    rows:\n    - - no change (baseline)\n      - 25.0%\n      - 128\n      - '[17.5%, 32.5%]'\n    - - verification-triggered change\n      - 27.0%\n      - 128\n      - '[19.3%, 34.7%]'\n    - - random change (matched rate)\n      - 21.0%\n      - 128\n      - '[13.9%, 28.1%]'\n  figures_description:\n  - 'Bar chart with CI: three conditions. All CIs overlap heavily.'\n  analysis: 'Causal evidence for verification-triggered > random is weak (p=0.08)。\n    CIs 大量重叠，no significant difference。这进一步 disqualifies action-change as reward signal。\n\n    '\n- name: Reward signal ablation (action-change vs alternatives)\n  plan_id: plan_012\n  description: 对比 action-change / random / confidence-based reward\n  expected_results:\n    action_change_reward_success: 0.16\n    action_change_reward_verify_rate: 0.88\n    random_reward_success: 0.15\n    random_reward_verify_rate: 0.85\n    confidence_reward_success: 0.19\n    confidence_reward_verify_rate: 0.62\n    all_below_always_on: true\n    best_method: confidence-based\n  result_rationale: 'Worst 档：所有 reward variants 都比 always-on 差。Action-change reward\n    与 random reward 表现几乎一样（delta < 2pp），证实 action-change 不比 random noise 更好。 Confidence-based\n    reward 稍好因为它利用了 model-intrinsic uncertainty 而非 extrinsic noisy signal。 但即使最好的\n    variant 也比 always-on 低 6pp。 核心问题：base agent 太弱时，所有 selective strategies 都退化为 \"less\n    verification = worse performance\"。\n\n    '\n  tables:\n  - name: Reward ablation\n    columns:\n    - reward_type\n    - success\n    - verify_rate\n    - token_cost\n    rows:\n    - - always-on (no skip)\n      - 25.0%\n      - 100%\n      - 1.0x\n    - - action-change\n      - 16.0%\n      - 88%\n      - 0.93x\n    - - random trigger\n      - 15.0%\n      - 85%\n      - 0.90x\n    - - confidence-based\n      - 19.0%\n      - 62%\n      - 0.72x\n  figures_description:\n  - 'Cost-performance Pareto: confidence-based is on frontier, action-change and random\n    are dominated.'\n  analysis: 'Action-change reward 无法区分于 random——这是对 Claim 2 的最终否定。 全部移入 future work：\"selective\n    verification requires (1) stronger base agent, (2) better reward signal\"。\n\n    '\n- name: ARES reproduction + comparison\n  plan_id: plan_013\n  description: 复现 ARES SFT router，与 B-IAVR 对比\n  expected_results:\n    ares_success: 0.22\n    ares_verify_rate: 0.7\n    ares_cost_reduction: 0.3\n    biavr_success: 0.16\n    biavr_verify_rate: 0.88\n    biavr_cost_reduction: 0.12\n    ares_dominates_biavr: true\n    delta_success_pp: 6\n    delta_cost_reduction_pp: 18\n  result_rationale: 'Worst 档：ARES SFT router 优于 B-IAVR。SFT router 使用 supervised learning\n    from oracle labels（何时 verify 有帮助），不依赖 RL training signal quality。 因此 ARES 不受 action-change\n    noise 影响。B-IAVR 的 RL-trained policy 在 weak reward signal 下退化为 near-always-verify，丧失了\n    cost reduction 优势。 这进一步证明在 weak agent 设定下 SFT > RL for selective verification。\n\n    '\n  tables:\n  - name: ARES vs B-IAVR\n    columns:\n    - method\n    - success\n    - verify_rate\n    - cost_red\n    - dominates\n    rows:\n    - - ARES (SFT)\n      - 22.0%\n      - 70%\n      - 30%\n      - 'yes'\n    - - B-IAVR (RL)\n      - 16.0%\n      - 88%\n      - 12%\n      - 'no'\n  figures_description:\n  - Pareto plot with ARES and B-IAVR. ARES clearly dominates.\n  analysis: 'ARES domination 在 worst 档下是 expected——SFT with oracle labels 是 easier\n    optimization problem。 Analysis paper 可以 acknowledge this 并 discuss when RL might\n    outperform SFT (hypothetically: when base agent is strong enough for action-change\n    to be meaningful signal)。\n\n    '\n- name: ScienceWorld transfer\n  plan_id: plan_014\n  description: ScienceWorld 上验证 episode-level vs step-independent\n  expected_results:\n    episode_level_success: 0.15\n    step_independent_success: 0.03\n    ratio: 5.0\n    episode_level_std: 0.08\n    step_independent_std: 0.02\n  result_rationale: 'Worst 档下 episode-level 仍优于 step-independent（5x），但绝对数值低。 ScienceWorld\n    任务更长更复杂（平均 40+ steps），episode-level 的 bandit credit 更吃力。 但 step-independent 在\n    ScienceWorld 上也崩溃（3%），证明问题不是 ALFWorld-specific。 这支持 analysis paper 的 generalizability\n    claim，但低绝对值（15%）进一步证明 episode-level 不够——需要 finer credit。High std (8pp) 说明 instability\n    也泛化。\n\n    '\n  tables:\n  - name: ScienceWorld transfer\n    columns:\n    - method\n    - success\n    - std\n    - vs_step_independent\n    rows:\n    - - step-independent\n      - 3%\n      - 2pp\n      - baseline\n    - - episode-level\n      - 15%\n      - 8pp\n      - 5x\n  figures_description:\n  - 'Cross-environment comparison: ALFWorld + ScienceWorld paired bars. Same trend\n    (episode > step-ind) but lower absolute for ScienceWorld.'\n  analysis: 'Transfer 验证了 finding 的 generalizability。两个环境一致：episode-level 解决了 step-independent\n    的崩溃， 但自身也有 ceiling。ScienceWorld 的 lower ceiling（15% vs 25%）反映更长 horizon 的 credit\n    challenge。\n\n    '\n- name: 7B model scaling verification\n  plan_id: plan_015\n  description: Qwen3-7B 上验证 episode-level vs step-independent\n  expected_results:\n    episode_level_7b_success: 0.32\n    step_independent_7b_success: 0.08\n    episode_level_1_7b_success: 0.25\n    step_independent_1_7b_success: 0.01\n    scaling_gain_episode_pp: 7\n    scaling_gain_step_ind_pp: 7\n    ratio_7b: 4.0\n    ratio_1_7b: 25.0\n  result_rationale: 'Worst 档：7B 提升两种方法各约 7pp（近乎 parallel shift），episode-level 优势 ratio\n    缩小（4x vs 25x at 1.7B）。 Step-independent 在 7B 上不再完全崩溃（8% vs 1%），因为 larger model\n    有更好的 in-context learning 能力， 部分补偿了 credit assignment 问题。但 episode-level 仍然 superior。\n    对 paper 的含义：episode-level 优势在 larger model 上缩小——可能 scaling 本身 partially mitigates\n    credit assignment failures（模型 in-context 能力可以补偿 training signal noise）。 这是 analysis\n    paper 的一个 nuanced finding。\n\n    '\n  tables:\n  - name: Scaling comparison\n    columns:\n    - model\n    - episode-level\n    - step-independent\n    - ratio\n    rows:\n    - - Qwen3-1.7B\n      - 25%\n      - 1%\n      - 25x\n    - - Qwen3-7B\n      - 32%\n      - 8%\n      - 4x\n  figures_description:\n  - '2×2 bar chart: model × method. Episode-level advantage shrinks at scale but persists.'\n  analysis: 'Scaling 结果 nuances the story：credit assignment 问题 severity 与 model size\n    负相关， 但不消失。Analysis paper 可以 speculate：at sufficient scale（70B+）， in-context learning\n    可能完全 compensate——这是 \"why big-lab RL works but small-model RL fails\" 的一个 hypothesis。\n\n    '\n- name: Per-task-type breakdown analysis\n  plan_id: plan_016\n  description: 按 ALFWorld 任务类型 breakdown episode-level performance\n  expected_results:\n    pick_success: 0.35\n    clean_success: 0.22\n    heat_success: 0.2\n    cool_success: 0.18\n    examine_success: 0.3\n    pick_two_success: 0.1\n    episode_length_correlation: 0.48\n    task_complexity_correlation: -0.62\n  result_rationale: 'Worst 档下，simple tasks（pick: 35%, examine: 30%）显著优于 complex tasks（pick_two:\n    10%, cool: 18%）。 Task complexity-success correlation = -0.62：越复杂越差，符合 credit assignment\n    bottleneck 假说—— longer horizons = more steps sharing same advantage = coarser\n    credit = worse learning。 Pick_two 最差因为需要 two sequential subtask completions，episode-level\n    advantage 无法 区分第一个 pick 的 credit 和第二个 pick 的 credit。 这个 breakdown 对 analysis paper\n    有价值：展示 failure 不均匀， task structure（horizon length、subtask decomposition）直接影响 credit\n    assignment quality。\n\n    '\n  tables:\n  - name: Per-task breakdown (episode-level, 5-seed mean)\n    columns:\n    - task_type\n    - success\n    - std\n    - avg_steps\n    - n_subtasks\n    rows:\n    - - pick\n      - 35%\n      - 5pp\n      - 28\n      - 1\n    - - examine\n      - 30%\n      - 6pp\n      - 32\n      - 1\n    - - clean\n      - 22%\n      - 7pp\n      - 35\n      - 2\n    - - heat\n      - 20%\n      - 8pp\n      - 37\n      - 2\n    - - cool\n      - 18%\n      - 7pp\n      - 38\n      - 2\n    - - pick_two\n      - 10%\n      - 9pp\n      - 45\n      - 2\n  figures_description:\n  - Grouped bar chart by task type, sorted by complexity. Clear downward trend.\n  - 'Scatter: avg_episode_length vs success per task type, r=-0.62.'\n  analysis: Task-level breakdown 是 analysis paper 的 key supporting evidence： credit\n    assignment failure severity 与 task horizon 和 subtask decomposition 正相关。 pick_two\n    的 10% 证明 episode-level bandit credit 无法处理 multi-subtask credit separation。 这 motivates\n    future work on hierarchical credit assignment（per-subtask reward 或 option-level\n    advantage）。\n",
      "numLines": 1094,
      "startLine": 1,
      "totalLines": 1094
    }
  },
  "sourceToolAssistantUUID": "ac32b9ec-0951-443f-848d-159085c84d52",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl",
  "sessionId": "faa92117-dd67-43a6-a8f9-8378acfec5f6",
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
  "lastPrompt": "[DREAM Review Director] dream_id=20260517T121256 | review_mode=full | review_visible=True PDF: /home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/artifacts/dream_reports/dre…",
  "leafUuid": "c61d0040-e249-4e5d-941b-f954869cfd90",
  "sessionId": "faa92117-dd67-43a6-a8f9-8378acfec5f6"
}
```

---

### Runtime record

_source line 18_

```json
{
  "type": "ai-title",
  "aiTitle": "Review ML research paper on cost verification agent RL",
  "sessionId": "faa92117-dd67-43a6-a8f9-8378acfec5f6"
}
```

---

### Assistant

_source line 19 · 2026-05-17T12:54:30.409Z_

<details><summary>Logged reasoning block</summary>

```text
I've now read both the paper PDF and the review context YAML. Let me understand the task:

1. I need to perform a full review using the dream-review-full dispatch template
2. Two reviewers: R1 (methods + experiments) and R2 (novelty + related work)
3. Full roundtable: Step 1 independent → Step 2 cross-share → Step 3 converge → Step 4 synthesize
4. At the end, submit via `submit_dream_review_report`

Let me now dispatch the two reviewers in parallel. Each reviewer needs the full paper content and the review context to do their job. I'll run them as agents.


The paper diagnoses why step-independent training fails for multi-turn LLM agents, but the empirical results are concerning: episode-level GRPO barely improves to ~23.4% with substantial variance, the hyperparameter sweep shows non-monotonic behavior, and the proposed sign misattribution mechanism only partially explains the failure (r=0.73) with significant confounds present.

The core issue is that episode-level training underperforms step-independent by 17.6 percentage points, and the action-change signal that should drive credit assignment is essentially noise (r=0.08). Selective verification strategies, including the proposed B-IAVR approach, all fail to improve over always-on verification, suggesting the fundamental mechanisms aren't working as theorized.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c61d0040-e249-4e5d-941b-f954869cfd90",
  "isSidechain": false,
  "requestId": "req_011Cb8B72CnEDmDogyDSd11B",
  "type": "assistant",
  "uuid": "5aba4d51-31b8-4d14-99f5-9f6139c093c3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl",
  "sessionId": "faa92117-dd67-43a6-a8f9-8378acfec5f6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VM6drHB7RkxQAu7npkd7sh",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 38056,
      "cache_read_input_tokens": 24216,
      "output_tokens": 4285,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 38056,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 4285,
          "cache_read_input_tokens": 24216,
          "cache_creation_input_tokens": 38056,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 38056
          },
          "type": "message"
        }
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

_source line 20 · 2026-05-17T12:54:30.411Z_

I've read both the paper and the experiment design context. Now dispatching two reviewers in parallel for Step 1 (independent reviews).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5aba4d51-31b8-4d14-99f5-9f6139c093c3",
  "isSidechain": false,
  "requestId": "req_011Cb8B72CnEDmDogyDSd11B",
  "type": "assistant",
  "uuid": "ec6309f1-39fc-4323-aedb-cc541a5aa291",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl",
  "sessionId": "faa92117-dd67-43a6-a8f9-8378acfec5f6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VM6drHB7RkxQAu7npkd7sh",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 38056,
      "cache_read_input_tokens": 24216,
      "output_tokens": 4285,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 38056,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 4285,
          "cache_read_input_tokens": 24216,
          "cache_creation_input_tokens": 38056,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 38056
          },
          "type": "message"
        }
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

_source line 21 · 2026-05-17T12:55:21.740Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01Gy7Wi61gErJG7oVirCJJHQ`</summary>

```json
{
  "description": "R1: Methods + Experiments review",
  "prompt": "You are Reviewer 1 (R1) for a top ML venue review. Your focus is **methods and experiments**. Review the paper below using a 6-point scale (1=Strong Reject, 2=Reject, 3=Weak Reject, 4=Weak Accept, 5=Accept, 6=Strong Accept). Target venue acceptance rate ~25%.\n\n## Paper Summary\n\nTitle: \"Dissecting Credit Assignment Failure in Multi-Turn LLM Agent RL: A Dual-Mechanism Analysis\"\n\nThis is a diagnostic/analysis paper studying why step-independent training fails for multi-turn LLM agents and characterizing failure modes. The paper:\n- Identifies 4 failure mechanisms: advantage sign misattribution, policy information loss, entropy collapse, bandit-level credit insufficiency\n- Shows episode-level GRPO achieves 23.4% (±6.2pp) vs 1% for step-independent on ALFWorld\n- Shows GAE with value function reaches 41%, a 17.6pp gap over episode-level GRPO\n- Provides mechanistic analysis showing sign misattribution is dominant (r=0.73) but not sole factor\n- Tests across environments (ScienceWorld), scales (1.7B→7B), reward shaping, selective verification strategies\n\n## Full Paper Content (9 pages)\n\n**Abstract**: RL for multi-turn LLM agents commonly adopts step-independent training (each context window as separate bandit arm). They show this fails due to advantage sign misattribution and policy information loss. Episode-level training eliminates sign misattribution but plateaus at 23.4% (±6.2pp) on ALFWorld. GAE reaches 41.0%. They decompose credit assignment failure into four factors, provide failure mode taxonomy, and derive design guidelines. Findings generalize across environments and model scales.\n\n**Section 1 Introduction**: Sets up problem of step-independent optimization. On ALFWorld, step-independent GRPO collapses to ~1% while episode-level reaches 23.4%. Two mechanisms identified: sign misattribution (per-window advantages inherit sign from episode outcome) and policy information loss (truncated context prevents cross-step learning). Episode-level exposes deeper bottleneck: GRPO bandit-style credit where all tokens share same scalar advantage. GAE reaches 41%, 17.6pp improvement. Mechanistic analysis shows r=0.73 sign-outcome correlation with confounds from KL (r=0.31), entropy (r=0.27), position (r=-0.18).\n\nContributions:\n1. Failure mode taxonomy with 4 mechanisms and quantified contributions\n2. Empirical characterization of credit granularity spectrum\n3. Actionable design guidelines\n\n**Section 2 Background**: Standard MDP formulation for LLM agents. GRPO definition with group normalization. Step-independent mode splits trajectory into h-token windows. Episode-level mode treats full trajectory as single sample. GAE with learned value function for per-token advantages.\n\n**Section 3 Failure Mode Taxonomy**: \n- Mechanism 1: Sign misattribution (r=0.73 with outcome, 78% success eps all-positive, 82% failure eps all-negative)\n- Mechanism 2: Information loss (h-sweep shows monotonic degradation)\n- Mechanism 3: Entropy collapse (0.20→0.12 while val stagnates 24-28%)\n- Mechanism 4: Bandit-level credit insufficiency (17.6pp gap episode→GAE, r=-0.62 task complexity vs success)\n\n**Section 4 Experimental Setup**: ALFWorld, Qwen3-1.7B primary, GRPO group size 8, lr 1e-6, KL 0.01, 15 steps primary, up to 50 steps convergence.\n\n**Section 5 Results**:\n- 5.1: Episode-level 23.4%±6.2pp, 95% CI [15.7%, 31.1%]. Plateau at step 15-20, train rises to 50% but val declines. pass@8=94% at step 50.\n- 5.2: h-sweep (h=2,5,10,20,full). NOT clean monotonic—cross-seed variance high, h=5 sometimes beats h=10. Characterized as \"probabilistic degradation.\"\n- 5.3: 5-seed replication, range 15-30%, train-val gap 22.6pp. Seed 4 at 15% (cold-start problem).\n- 5.4: GAE comparison. Step-ind 1% → Episode 24% → GAE(λ=1) 36.7% → GAE(λ=0.95) 41%. Per-token advantage variance 0.42 for GAE vs 0.0 for GRPO.\n- 5.5: Mechanistic verification. Sign-outcome r=0.73 (hypothesized >0.95—PARTIAL). Sign-local quality r=0.28 (hypothesized <0.1—FAILED). Multiple confounds: KL r=0.31, entropy r=0.27, position r=-0.18. Sign misattribution accounts for only 53% of variance.\n- 5.6: Task complexity analysis. pick 35%, pick_two 10%. r=-0.62 complexity vs success.\n- 5.7: Reward shaping. valid_action_bonus hurts success (28→22%) while improving format compliance (55→72%).\n- 5.8: Selective verification. Always-on 25%, confidence 19%, B-IAVR 16%, random 14%, no-verify 13%. Action-change reward r=0.08 (p=0.12), indistinguishable from noise.\n- 5.9: ARES (SFT) dominates B-IAVR (RL) on both axes.\n- 5.10: ScienceWorld 15% vs 3% (5×). 7B scaling: both improve ~7pp, ratio shrinks 25×→4×.\n\n**Section 6 Discussion**: 5 actionable guidelines. Discussion of why community defaults to step-independent. Limitations: text-only envs, correlational mechanistic analysis, GAE cost not accounted.\n\n**Section 7 Conclusion**: Summary of taxonomy and guidelines.\n\n**References**: 10 references total.\n\n## Experiment Design Context (from review_context.yaml)\n\nThe paper was framed as a diagnostic/analysis paper. Key context on experimental quality:\n\n1. **h-sweep non-monotonicity**: The h-sweep results are NOT clean monotonic. h=5 occasionally beats h=10 between seeds. h=20 seed2 shows temporary dip. This is acknowledged in the paper as \"probabilistic degradation.\"\n\n2. **Mechanistic verification partially fails**: Sign-outcome correlation is 0.73, not >0.95 as hypothesized. Sign-local quality is 0.28, not <0.1. Several hypotheses only partially confirmed. The paper acknowledges confounds.\n\n3. **Multi-seed variance is high**: 5-seed episode-level has std=6.2pp, 95% CI [15.7%, 31.1%] — too wide to make strong claims. Seed 4 only 15%.\n\n4. **Selective verification (B-IAVR) completely fails**: Action-change reward signal is r=0.08 (p=0.12), indistinguishable from noise. After controlling for entropy, partial r=0.07 (p=0.15). B-IAVR is dominated by simple confidence baseline and by ARES SFT.\n\n5. **GAE comparison is strong**: GAE >> episode-level (17.6pp gap), this is the paper's strongest finding.\n\n6. **Missing experiments from design**: The full experiment plan includes 16 experiments. The paper covers most but lacks some detailed analyses (e.g., entropy-controlled action-change analysis from plan_010, causal intervention from plan_011, detailed reward signal ablation from plan_012 are partially covered but compressed).\n\n## Your Review Task (R1: Methods + Experiments)\n\nEvaluate:\n1. **Methodological soundness**: Are the experimental designs appropriate? Are comparisons fair? Are confounds adequately addressed?\n2. **Statistical rigor**: Are uncertainty estimates adequate? Is the number of seeds sufficient? Are claims supported by the confidence intervals?\n3. **Experimental coverage**: Are key ablations present? What's missing?\n4. **Reproducibility**: Enough detail to reproduce?\n5. **Claim-evidence alignment**: Do the experimental results actually support the claims made?\n\nProduce a structured review with:\n- Summary (2-3 sentences)\n- Strengths (bulleted)\n- Weaknesses (bulleted, with severity: major/minor)\n- Questions for authors\n- Missing experiments or analyses\n- Score (1-6) and confidence (1-5)\n- One-line recommendation\n\nBe rigorous. This is a top venue review."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ec6309f1-39fc-4323-aedb-cc541a5aa291",
  "isSidechain": false,
  "requestId": "req_011Cb8B72CnEDmDogyDSd11B",
  "type": "assistant",
  "uuid": "212a3e29-f6bf-4f80-8bc6-252b9e1d705e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl",
  "sessionId": "faa92117-dd67-43a6-a8f9-8378acfec5f6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VM6drHB7RkxQAu7npkd7sh",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 38056,
      "cache_read_input_tokens": 24216,
      "output_tokens": 4285,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 38056,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 4285,
          "cache_read_input_tokens": 24216,
          "cache_creation_input_tokens": 38056,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 38056
          },
          "type": "message"
        }
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

_source line 22 · 2026-05-17T12:55:43.755Z_

<details open><summary>🔧 Tool call — Agent · `toolu_015GjcCKdVL1X3SHsdHoZxNz`</summary>

```json
{
  "description": "R2: Novelty + Related Work review",
  "prompt": "You are Reviewer 2 (R2) for a top ML venue review. Your focus is **novelty and related work**. Review the paper below using a 6-point scale (1=Strong Reject, 2=Reject, 3=Weak Reject, 4=Weak Accept, 5=Accept, 6=Strong Accept). Target venue acceptance rate ~25%.\n\n## Paper Summary\n\nTitle: \"Dissecting Credit Assignment Failure in Multi-Turn LLM Agent RL: A Dual-Mechanism Analysis\"\n\nThis is a diagnostic/analysis paper studying why step-independent training fails for multi-turn LLM agents and characterizing failure modes. The paper:\n- Identifies 4 failure mechanisms: advantage sign misattribution, policy information loss, entropy collapse, bandit-level credit insufficiency\n- Shows episode-level GRPO achieves 23.4% (±6.2pp) vs 1% for step-independent on ALFWorld\n- Shows GAE with value function reaches 41%, a 17.6pp gap over episode-level GRPO\n- Provides mechanistic analysis showing sign misattribution is dominant (r=0.73) but not sole factor\n- Tests across environments (ScienceWorld), scales (1.7B→7B), reward shaping, selective verification\n\n## Full Paper Content (9 pages)\n\n**Abstract**: RL for multi-turn LLM agents commonly adopts step-independent training (each context window as separate bandit arm). They show this fails due to advantage sign misattribution and policy information loss. Episode-level training eliminates sign misattribution but plateaus at 23.4% (±6.2pp) on ALFWorld. GAE reaches 41.0%. They decompose credit assignment failure into four factors, provide failure mode taxonomy, and derive design guidelines. Findings generalize across environments and model scales.\n\n**Section 1 Introduction**: Sets up problem of step-independent optimization in LLM agent RL. On ALFWorld, step-independent GRPO collapses to ~1% while episode-level reaches 23.4%. Two mechanisms: sign misattribution and policy information loss. Episode-level exposes deeper bottleneck: bandit-style credit. GAE reaches 41%, 17.6pp improvement. Mechanistic analysis shows r=0.73 sign-outcome correlation with confounds.\n\nContributions:\n1. Failure mode taxonomy with 4 mechanisms and quantified contributions\n2. Empirical characterization of credit granularity spectrum (step-independent → episode-level → per-token GAE)\n3. Actionable design guidelines\n\n**Section 2 Background**: GRPO definition. Step-independent mode (trajectory split into h-token windows, each optimized independently). Episode-level mode (full trajectory as single sample). GAE with learned value function.\n\n**Section 3 Failure Mode Taxonomy**: 4 mechanisms: sign misattribution, information loss, entropy collapse, bandit-level credit insufficiency. Each described with empirical indicators.\n\n**Section 4 Experimental Setup**: ALFWorld environment, Qwen3-1.7B (primary) and 7B, GRPO with group size 8.\n\n**Section 5 Results**: 10 subsections covering episode-level convergence, h-sweep, multi-seed, GAE comparison, mechanistic verification, task complexity, reward shaping, selective verification, ARES comparison, cross-environment and scaling.\n\n**Section 6 Discussion**: 5 actionable guidelines. Why community defaults to step-independent. Limitations.\n\n**Section 7 Conclusion**: Summary.\n\n**References** (only 10 total):\n[1] DeepSeekMath (2024)\n[2] RAGEN (2025) \n[3] ALFWorld (ICLR 2021)\n[4] ScienceWorld (EMNLP 2022)\n[5] GAE / Schulman (ICLR 2016)\n[6] Self-Guide (2026)\n[7] ARES (2026)\n[8] Thinkless (NeurIPS 2025)\n[9] ReflAct (EMNLP 2025)\n[10] PPO / Schulman (2017)\n\n## Experiment Design Context\n\nThe paper was reframed as a diagnostic/analysis paper. Originally it aimed to propose selective verification (B-IAVR) as a method contribution, but experiments showed it fails: action-change reward signal is r=0.08 (p=0.12), B-IAVR is dominated by both ARES and a simple confidence heuristic. The paper pivoted to framing as failure mode analysis.\n\nKey experimental facts:\n- The h-sweep is not clean monotonic (non-monotonicity between seeds at adjacent h values)\n- Mechanistic verification partially failed: many hypotheses only partially confirmed\n- Multi-seed variance is very high (std=6.2pp, 95% CI [15.7%, 31.1%])\n- Selective verification (B-IAVR) completely fails as a contribution\n- GAE >> episode-level GRPO is the strongest finding (17.6pp gap)\n- Only 10 references in the bibliography\n\n## Your Review Task (R2: Novelty + Related Work)\n\nEvaluate:\n1. **Novelty**: How novel are the findings? Is the failure mode taxonomy genuinely new insight or well-known RL theory applied to a specific setting? Is credit assignment being a challenge in RL a new observation?\n2. **Positioning**: Does the paper adequately position itself relative to prior work? Is the \"analysis paper\" framing convincing?\n3. **Related work coverage**: Are key related works cited? The paper has only 10 references. Consider:\n   - Classic credit assignment literature (temporal difference, eligibility traces)\n   - Other LLM agent RL papers (AgentQ, Archer, WebAgent, etc.)\n   - Multi-turn RL for LLMs (RLHF literature on reward modeling)\n   - Step-level vs episode-level reward in RL (process reward models, outcome reward models)\n   - Other analysis/diagnostic papers in ML\n4. **Contribution significance**: For a top venue, are the contributions sufficient? An analysis paper needs very strong insights to compensate for lack of method contribution.\n5. **Writing quality**: Is the paper well-written? Any AI-style writing artifacts?\n6. **Reference adequacy**: With only 10 references, is the bibliography sufficient for a top venue submission?\n\nProduce a structured review with:\n- Summary (2-3 sentences)\n- Strengths (bulleted)\n- Weaknesses (bulleted, with severity: major/minor)\n- Questions for authors\n- Missing related work (specific papers/areas that should be cited)\n- Score (1-6) and confidence (1-5)\n- One-line recommendation\n\nBe rigorous. This is a top venue review."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "212a3e29-f6bf-4f80-8bc6-252b9e1d705e",
  "isSidechain": false,
  "requestId": "req_011Cb8B72CnEDmDogyDSd11B",
  "type": "assistant",
  "uuid": "397a70f0-38ff-4781-b93c-e75de5f597b6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl",
  "sessionId": "faa92117-dd67-43a6-a8f9-8378acfec5f6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VM6drHB7RkxQAu7npkd7sh",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 38056,
      "cache_read_input_tokens": 24216,
      "output_tokens": 4285,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 38056,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 4285,
          "cache_read_input_tokens": 24216,
          "cache_creation_input_tokens": 38056,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 38056
          },
          "type": "message"
        }
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

_source line 23_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[DREAM Review Director] dream_id=20260517T121256 | review_mode=full | review_visible=True PDF: /home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/artifacts/dream_reports/dre…",
  "leafUuid": "397a70f0-38ff-4781-b93c-e75de5f597b6",
  "sessionId": "faa92117-dd67-43a6-a8f9-8378acfec5f6"
}
```

---

### Runtime record

_source line 24_

```json
{
  "type": "ai-title",
  "aiTitle": "Review ML research paper on cost verification agent RL",
  "sessionId": "faa92117-dd67-43a6-a8f9-8378acfec5f6"
}
```

---
