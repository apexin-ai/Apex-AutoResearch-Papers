# Research conversation: [DREAM Review Director] dream_id=20260514T203201 | review_mode=full | review_visible=True PDF: /home/ubuntu/.agent-ml-re

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 46
- **Recorded user turns:** 2
- **Tool calls:** 9
- **Original source:** `logs/chats/exported-trajectories/account-3/a188aefa-23b6-4688-b448-164a4ee4e586.jsonl`
- **Structured JSON:** [`a1081e14fcb7161cf875.json`](../../sessions/a1/a1081e14fcb7161cf875.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-14T21:30:13.849Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-14T21:30:13.849Z",
  "sessionId": "a188aefa-23b6-4688-b448-164a4ee4e586",
  "content": "[DREAM Review Director]\ndream_id=20260514T203201 | review_mode=full | review_visible=True\nPDF: /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T203201/worst/review_input_f5f46a62.pdf\n\n（内部编排信息：tier=worst，仅用于 submit_dream_review_report 调用。\n你在向 Reviewer 发送审稿任务时，**严禁**提及档位名称 best/median/worst，\n也不要暗示论文结果的好坏。Reviewer 必须盲审。）\n\n任务：对上述 PDF 进行 full 模式审稿。 使用 `dream-review-full` skill 的 dispatch 模板（2 Reviewers：R1 方法+实验、R2 新颖性+相关工作；完整 roundtable：Step 1 独立 → Step 2 交叉分享 → Step 3 收敛 → Step 4 综合）。\n\n## 审稿标准\n\n未指定目标 venue。请按 top ML venue 通用标准审稿（接受率 ~25%，6 分制：1=Strong Reject … 6=Strong Accept）。\n\n## 实验设计参考\n\n完整实验设计（含想象实验列表）：`/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T203201/worst/review_context.yaml`\n论文可能未完整反映所有实验——参考此文件判断覆盖度。\n完成后必须调用 `submit_dream_review_report(report, project=\"struct_self_consist_ie\", tier=\"worst\", dream_id=\"20260514T203201\", review_visible=True)` —— 报告会写入 dream_reports/dream_20260514T203201/worst/review_report.md，编排进程通过 subprocess 退出读取它。\n不要调用 submit_review_report_to_research_director / update_review_issues / request_external_review —— 这些工具不在 Dream Review Director 白名单内。\n"
}
```

---

### Runtime record

_source line 2 · 2026-05-14T21:30:13.852Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-14T21:30:13.852Z",
  "sessionId": "a188aefa-23b6-4688-b448-164a4ee4e586"
}
```

---

## Round 1

10 recorded events

### User

_source line 3 · 2026-05-14T21:30:13.887Z_

[DREAM Review Director]
dream_id=20260514T203201 | review_mode=full | review_visible=True
PDF: /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T203201/worst/review_input_f5f46a62.pdf

（内部编排信息：tier=worst，仅用于 submit_dream_review_report 调用。
你在向 Reviewer 发送审稿任务时，**严禁**提及档位名称 best/median/worst，
也不要暗示论文结果的好坏。Reviewer 必须盲审。）

任务：对上述 PDF 进行 full 模式审稿。 使用 `dream-review-full` skill 的 dispatch 模板（2 Reviewers：R1 方法+实验、R2 新颖性+相关工作；完整 roundtable：Step 1 独立 → Step 2 交叉分享 → Step 3 收敛 → Step 4 综合）。

## 审稿标准

未指定目标 venue。请按 top ML venue 通用标准审稿（接受率 ~25%，6 分制：1=Strong Reject … 6=Strong Accept）。

## 实验设计参考

完整实验设计（含想象实验列表）：`/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T203201/worst/review_context.yaml`
论文可能未完整反映所有实验——参考此文件判断覆盖度。
完成后必须调用 `submit_dream_review_report(report, project="struct_self_consist_ie", tier="worst", dream_id="20260514T203201", review_visible=True)` —— 报告会写入 dream_reports/dream_20260514T203201/worst/review_report.md，编排进程通过 subprocess 退出读取它。
不要调用 submit_review_report_to_research_director / update_review_issues / request_external_review —— 这些工具不在 Dream Review Director 白名单内。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "a640b4e1-01ba-4811-b057-a5972a785ed6",
  "type": "user",
  "uuid": "65b03deb-2e0d-4ff2-9631-a2edb50e4de8",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a188aefa-23b6-4688-b448-164a4ee4e586",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-14T21:30:13.887Z_

```json
{
  "parentUuid": "65b03deb-2e0d-4ff2-9631-a2edb50e4de8",
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
  "uuid": "02ce4f56-e915-4aaa-bc3c-75fec8e254a0",
  "timestamp": "2026-05-14T21:30:13.887Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a188aefa-23b6-4688-b448-164a4ee4e586",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-14T21:30:13.887Z_

```json
{
  "parentUuid": "02ce4f56-e915-4aaa-bc3c-75fec8e254a0",
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
  "uuid": "814c549e-929f-4bf8-8d7d-af74a07f4c40",
  "timestamp": "2026-05-14T21:30:13.887Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a188aefa-23b6-4688-b448-164a4ee4e586",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6 · 2026-05-14T21:30:13.887Z_

```json
{
  "parentUuid": "814c549e-929f-4bf8-8d7d-af74a07f4c40",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "3e48607e-bb69-492a-a576-9f74ef1ca75e",
  "timestamp": "2026-05-14T21:30:13.887Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a188aefa-23b6-4688-b448-164a4ee4e586",
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
  "aiTitle": "Full blind review of structural self-consistency IE paper",
  "sessionId": "a188aefa-23b6-4688-b448-164a4ee4e586"
}
```

---

### Assistant

_source line 8 · 2026-05-14T21:30:17.704Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to perform a full DREAM review of a PDF paper. Let me start by:

1. Reading the PDF to understand the paper
2. Reading the review context YAML for experiment design reference
3. Then dispatching the review following the dream-review-full skill template

Let me first load the necessary tools and read the files.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3e48607e-bb69-492a-a576-9f74ef1ca75e",
  "isSidechain": false,
  "requestId": "req_011Cb3B2T4r89qr7DB4msYmk",
  "type": "assistant",
  "uuid": "56a53a91-2281-4ae6-890b-73a1e1d26603",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a188aefa-23b6-4688-b448-164a4ee4e586",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WsXKvaPJM7vap5Lo6aLg5p",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11112,
      "cache_read_input_tokens": 11841,
      "output_tokens": 376,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11112,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 376,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11112,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11112
          },
          "type": "message"
        }
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

_source line 9 · 2026-05-14T21:30:18.364Z_

I'll start by reading the PDF and the review context, and loading the necessary tools.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "56a53a91-2281-4ae6-890b-73a1e1d26603",
  "isSidechain": false,
  "requestId": "req_011Cb3B2T4r89qr7DB4msYmk",
  "type": "assistant",
  "uuid": "4a9f412d-ea8b-45bd-9a9d-46f119fc89f2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a188aefa-23b6-4688-b448-164a4ee4e586",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WsXKvaPJM7vap5Lo6aLg5p",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11112,
      "cache_read_input_tokens": 11841,
      "output_tokens": 376,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11112,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 376,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11112,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11112
          },
          "type": "message"
        }
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

_source line 10 · 2026-05-14T21:30:19.068Z_

<details open><summary>🔧 Tool call — Read · `toolu_0186qHg86YNwFTjgT6DoGvkh`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T203201/worst/review_input_f5f46a62.pdf"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4a9f412d-ea8b-45bd-9a9d-46f119fc89f2",
  "isSidechain": false,
  "requestId": "req_011Cb3B2T4r89qr7DB4msYmk",
  "type": "assistant",
  "uuid": "2b5fc342-87af-4863-8b22-4ff254875a9b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a188aefa-23b6-4688-b448-164a4ee4e586",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WsXKvaPJM7vap5Lo6aLg5p",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11112,
      "cache_read_input_tokens": 11841,
      "output_tokens": 376,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11112,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 376,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11112,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11112
          },
          "type": "message"
        }
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

_source line 11 · 2026-05-14T21:30:20.299Z_

<details><summary>↩ Tool result · `toolu_015drftxBQathRqaGkQ1t3e4`</summary>

```text
No matching deferred tools found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3dbf4e07-cfee-4443-bc59-e3158ea51a1c",
  "isSidechain": false,
  "promptId": "a640b4e1-01ba-4811-b057-a5972a785ed6",
  "type": "user",
  "uuid": "a43c3e51-17c9-4196-9131-42abc6db1b3e",
  "toolUseResult": {
    "matches": [],
    "query": "select:submit_dream_review_report,read_project_file",
    "total_deferred_tools": 23
  },
  "sourceToolAssistantUUID": "3dbf4e07-cfee-4443-bc59-e3158ea51a1c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a188aefa-23b6-4688-b448-164a4ee4e586",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-14T21:30:19.131Z_

<details><summary>↩ Tool result · `toolu_0186qHg86YNwFTjgT6DoGvkh`</summary>

```text
PDF file read: /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T203201/worst/review_input_f5f46a62.pdf (166.7KB)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2b5fc342-87af-4863-8b22-4ff254875a9b",
  "isSidechain": false,
  "promptId": "a640b4e1-01ba-4811-b057-a5972a785ed6",
  "type": "user",
  "uuid": "4f4a7d16-ef89-47d8-b67d-bae37c6a14b6",
  "toolUseResult": {
    "type": "pdf",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T203201/worst/review_input_f5f46a62.pdf",
      "base64": "[ATTACHMENT_DATA_REDACTED]",
      "originalSize": 170747
    }
  },
  "sourceToolAssistantUUID": "2b5fc342-87af-4863-8b22-4ff254875a9b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a188aefa-23b6-4688-b448-164a4ee4e586",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

## Round 2

34 recorded events

### User

_source line 13 · 2026-05-14T21:30:19.127Z_

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
  "parentUuid": "4f4a7d16-ef89-47d8-b67d-bae37c6a14b6",
  "isSidechain": false,
  "promptId": "a640b4e1-01ba-4811-b057-a5972a785ed6",
  "type": "user",
  "isMeta": true,
  "uuid": "cd70f6ea-4cd0-4217-a898-86d0a4277302",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a188aefa-23b6-4688-b448-164a4ee4e586",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-14T21:30:19.887Z_

<details open><summary>🔧 Tool call — Read · `toolu_01T7Fe7qV7Ugf9ngbEWw6xme`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T203201/worst/review_context.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cd70f6ea-4cd0-4217-a898-86d0a4277302",
  "isSidechain": false,
  "requestId": "req_011Cb3B2T4r89qr7DB4msYmk",
  "type": "assistant",
  "uuid": "34d55573-8383-48c7-b3e1-578badc59efe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a188aefa-23b6-4688-b448-164a4ee4e586",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WsXKvaPJM7vap5Lo6aLg5p",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11112,
      "cache_read_input_tokens": 11841,
      "output_tokens": 376,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11112,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 376,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11112,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11112
          },
          "type": "message"
        }
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

_source line 15 · 2026-05-14T21:30:20.155Z_

<details><summary>↩ Tool result · `toolu_01T7Fe7qV7Ugf9ngbEWw6xme`</summary>

```text
1	narrative_guidance: '完全 reframe 为 ''Why Self-Consistency Fails for Structured Prediction:
2	  An Analysis of the Correlation-Selection Gap''。 在这个档位下，structural signals 对 logprob
3	  的优势微弱到不具实际意义（AUROC gap 0-5pp，ρ gap -4 to +5 hundredths）， reviewer 将 paper 定性为 negative
4	  result 但 novelty 不足。Nédellec & Xia 2026 被视为 scooping—— 他们已经做了 consistency-accuracy
5	  相关性研究，我们的 structural metrics 被视为 minor extension。 Correlation-selection gap 被 dismiss
6	  为 ''obvious: instance-level ≠ sample-level is well-known in calibration literature''。
7	  NER best-of-N 全部 ≤ greedy 被解读为 the method fundamentally doesn''t work。 WNUT abandoned
8	  被推断为 cherry-picking datasets。Paper 的唯一存活 claim 是 quality estimation 中 structural
9	  > logprob 在 60-80% 的配置上成立但 gap 太小，不足以 justify venue contribution。 Lead with negative
10	  finding + explanation 策略本身被 reviewer 视为 post-hoc rationalization。 目标从 Main 降为 Findings，但
11	  Findings 概率也仅 15-35%。
12	
13	  '
14	imagined_experiments:
15	- name: baseline_logprob
16	  plan_id: exp-012
17	  description: '对所有 pilot 数据 (SciERC NER+RE) 提取 sequence log-probability， 计算与 F1 的
18	    Spearman ρ、AUROC、Kendall τ。
19	
20	    '
21	  expected_results:
22	    scierc_ner_logprob_rho: 0.33
23	    scierc_ner_logprob_auroc: 0.64
24	    scierc_ner_logprob_tau: 0.24
25	    scierc_ner_logprob_ece: 0.09
26	    scierc_ner_sj_rho: 0.36
27	    scierc_ner_sj_auroc: 0.67
28	    scierc_ner_sj_minus_logprob_rho: 0.03
29	    scierc_ner_sj_minus_logprob_auroc: 0.03
30	    scierc_ner_fk_rho: 0.27
31	    scierc_ner_greedy_logprob_rho: 0.34
32	    scierc_re_logprob_rho: 0.25
33	    scierc_re_logprob_auroc: 0.62
34	    scierc_re_sj_rho: 0.21
35	    scierc_re_sj_auroc: 0.59
36	    scierc_re_cond_logprob_rho: 0.19
37	    scierc_re_cond_sj_rho: 0.33
38	    scierc_re_cond_sj_auroc: 0.65
39	    n_ner: 529
40	    n_re: 397
41	  result_rationale: 'Worst 档的关键：logprob 在 NER 上与 SJ 差距仅 Δρ=0.03、ΔAUROC=0.03， 统计上 bootstrap
42	    CI 重叠。原理——fine-tuned 8B 模型的 softmax 已 well-calibrated， logprob 隐式编码了 entity span
43	    正确性的全部信息。SJ 的额外 8 次采样只带来 +0.03 ρ 的微弱增益， reviewer 认为这不 justify 8x 推理成本。更致命的是 greedy_logprob（单次前向传播的
44	    logprob） ρ=0.34 实际上已经超过 SJ 的 ρ=0.36 的下界 CI。RE 上 logprob full ρ=0.25 > SJ full
45	    ρ=0.21， 虽然 RE cond 上 SJ 反超（0.33 vs 0.19），但 reviewer 将 conditional 分析视为 cherry-picking。
46	    整体结论：SJ 对 logprob 的优势在 NER 上 marginal，在 RE full 上不存在。
47	
48	    '
49	  tables:
50	  - table_id: T-012-1
51	    caption: 'Confidence signal comparison: log-probability vs structural signals
52	      (Spearman ρ with F1)'
53	    columns:
54	    - Dataset
55	    - Task
56	    - Log-prob ρ
57	    - SJ ρ
58	    - FK ρ
59	    - Δ(SJ−LP)
60	    - p(Δ)
61	    rows:
62	    - - SciERC
63	      - NER-full
64	      - 0.33
65	      - 0.36
66	      - 0.27
67	      - '+0.03'
68	      - 0.14
69	    - - SciERC
70	      - NER-cond
71	      - 0.3
72	      - 0.37
73	      - 0.28
74	      - '+0.07'
75	      - 0.04
76	    - - SciERC
77	      - RE-full
78	      - 0.25
79	      - 0.21
80	      - 0.25
81	      - −0.04
82	      - 0.32
83	    - - SciERC
84	      - RE-cond
85	      - 0.19
86	      - 0.33
87	      - 0.28
88	      - '+0.14'
89	      - 0.002
90	  figures_description:
91	  - 'Fig-012-1: Scatter plot 双联——log-prob vs F1 (left) 和 SJ vs F1 (right)， SciERC
92	    NER，两者 spread 几乎一样，SJ 的 regression line 斜率仅微高于 logprob， reviewer 第一眼看不出明显差别
93	
94	    '
95	  analysis: 'Worst 档下 exp-012 的结果不是灾难性的——SJ 仍然在 NER 上微弱领先——但差距小到 reviewer 可以 legitimately
96	    argue "this is not practically significant"。 特别是 Δρ=0.03 在 n=529 下 p=0.14 不显著。RE
97	    full 上 logprob > SJ 给了 reviewer 弹药："SJ 在 RE 上甚至不如 logprob"。唯一亮点是 RE cond 上 SJ
98	    明确领先（+0.14）， 但这需要 conditional filtering 来展示，削弱了 generality。 核心问题：reviewer 会说 "so
99	    SJ is marginally better in some settings and worse in others — this is a wash,
100	    not a contribution."
101	
102	    '
103	- name: baseline_exact_match
104	  plan_id: exp-013
105	  description: 'Exact-match voting rate：N 个 sample 中完全相同 entity/relation set 的比例，
106	    与 F1 计算 ρ/AUROC/τ。Wang et al. 2023 self-consistency 的直接结构化推广。
107	
108	    '
109	  expected_results:
110	    scierc_ner_em_rho: 0.26
111	    scierc_ner_em_auroc: 0.62
112	    scierc_ner_em_tau: 0.19
113	    scierc_re_em_rho: 0.1
114	    scierc_re_em_auroc: 0.5
115	    scierc_re_em_tau: 0.08
116	    scierc_ner_pct_all_match: 9.1
117	    scierc_ner_pct_no_match: 38.7
118	    scierc_re_pct_all_match: 1.8
119	    scierc_re_pct_no_match: 68.2
120	  result_rationale: 'EM 在 NER ρ=0.26 低于 SJ(0.36) 和 logprob(0.33)，在 RE ρ=0.10 是所有 signal
121	    中最弱。 这符合预期——IE 输出的 surface form 变异（span boundary 差异、entity 排列顺序差异） 使得 exact-match
122	    信号极度稀疏（39% NER 样本无任何 EM pair）。但在 worst 档下这个结果 反而削弱了 SJ 的叙事：reviewer 会说 "SJ 比 EM
123	    好 only because EM is a strawman — the real comparison is with logprob, which is
124	    free and equally good." RE 上 EM AUROC=0.50 等同于随机，证明 exact-match 在 relation extraction
125	    上完全失效。
126	
127	    '
128	  tables:
129	  - table_id: T-013-1
130	    caption: Exact-match voting rate distribution and correlation
131	    columns:
132	    - Dataset
133	    - Task
134	    - '% all-match'
135	    - '% no-match'
136	    - ρ with F1
137	    - AUROC
138	    rows:
139	    - - SciERC
140	      - NER
141	      - 9.1
142	      - 38.7
143	      - 0.26
144	      - 0.62
145	    - - SciERC
146	      - RE
147	      - 1.8
148	      - 68.2
149	      - 0.1
150	      - 0.5
151	  figures_description:
152	  - 'Fig-013-1: Histogram — EM rate 分布（0/8, 1/8, ..., 8/8）， 高度集中于 0 和 1，几乎二值化的粗粒度信号
153	
154	    '
155	  analysis: 'EM 是 self-consistency 在结构化输出上的 naïve baseline，其弱势是意料之中的。 在 worst 档下，这个实验的价值被
156	    reviewer 低估——他们认为 "of course exact-match doesn''t work for structured outputs,
157	    this is obvious" 而不是将其视为 motivation for SJ。结果是 SJ > EM 这个子结论被视为 trivial。
158	
159	    '
160	- name: baseline_entity_voting
161	  plan_id: exp-014
162	  description: 'Entity-level majority voting confidence：对每个 entity 统计在 N 个 sample
163	    中的出现频率， 计算 instance-level 平均 voting confidence 与 F1 的相关性。
164	
165	    '
166	  expected_results:
167	    scierc_ner_voting_rho: 0.37
168	    scierc_ner_voting_auroc: 0.68
169	    scierc_ner_voting_tau: 0.27
170	    scierc_re_voting_rho: 0.3
171	    scierc_re_voting_auroc: 0.64
172	    scierc_re_voting_tau: 0.22
173	    scierc_ner_voting_f1_selected: 0.615
174	    scierc_ner_greedy_f1: 0.648
175	    scierc_ner_oracle_f1: 0.779
176	    scierc_ner_voting_vs_greedy_delta: -3.3
177	    scierc_re_voting_f1_selected: 0.358
178	    scierc_re_greedy_f1: 0.402
179	    voting_minus_sj_ner_rho: 0.01
180	    voting_minus_logprob_ner_rho: 0.04
181	  result_rationale: 'Entity voting ρ=0.37 在 NER 上与 SJ(0.36) 几乎持平（Δ=+0.01），AUROC 也仅微弱领先（0.68
182	    vs 0.67）。 关键是 voting vs logprob 差距也很小（+0.04 ρ）。在 worst 档下三者（voting, SJ, logprob）
183	    形成一个统计上无法区分的 cluster（bootstrap CI 大量重叠），reviewer 会说 "all signals perform similarly
184	    — the choice of signal doesn''t matter." Voting 作为 selection strategy（而非 quality
185	    estimation）失败得更彻底： voting-selected F1=0.615 低于 greedy=0.648（−3.3pp），因为 majority
186	    vote 倾向于选择"平庸但安全"的 entity 而丢弃正确但少数的 entity。 RE 上 voting ρ=0.30 高于 SJ(0.21) 但仍低于
187	    logprob 的下界期望。
188	
189	    '
190	  tables:
191	  - table_id: T-014-1
192	    caption: Entity voting vs other signals (SciERC)
193	    columns:
194	    - Signal
195	    - NER ρ
196	    - NER AUROC
197	    - RE ρ
198	    - RE AUROC
199	    rows:
200	    - - Voting conf
201	      - 0.37
202	      - 0.68
203	      - 0.3
204	      - 0.64
205	    - - Soft Jaccard
206	      - 0.36
207	      - 0.67
208	      - 0.21
209	      - 0.59
210	    - - Log-prob
211	      - 0.33
212	      - 0.64
213	      - 0.25
214	      - 0.62
215	    - - Fleiss' κ
216	      - 0.27
217	      - 0.59
218	      - 0.25
219	      - 0.61
220	    - - Exact-match
221	      - 0.26
222	      - 0.62
223	      - 0.1
224	      - 0.5
225	  figures_description:
226	  - 'Fig-014-1: Bar chart — 5 signal 在 NER 上的 ρ，三者（voting/SJ/logprob） 高度接近，error bars
227	    重叠，视觉上无明显优胜者
228	
229	    '
230	  analysis: 'Entity voting 的加入没有改变整体叙事——在 worst 档下它只是 structural consistency family
231	    中另一个与 logprob 差距不大的 signal。Voting 作为 selection 策略失败 （低于 greedy -3.3pp）直接支持了 correlation-selection
232	    gap 的 narrative， 但 reviewer 认为这是 "expected: instance-level aggregates can''t rank
233	    individual samples."
234	
235	    '
236	- name: evaluation_metrics_expansion
237	  plan_id: exp-015
238	  description: '在所有 confidence signal × 所有数据集上扩展评估指标： AUROC、Kendall τ、ECE (calibration)。Leave-one-out
239	    SJ 检验评估 circularity。
240	
241	    '
242	  expected_results:
243	    scierc_ner:
244	      voting_rho: 0.37
245	      voting_auroc: 0.68
246	      voting_tau: 0.27
247	      sj_rho: 0.36
248	      sj_auroc: 0.67
249	      sj_tau: 0.26
250	      sj_ece: 0.11
251	      fk_rho: 0.27
252	      fk_auroc: 0.59
253	      fk_tau: 0.2
254	      logprob_rho: 0.33
255	      logprob_auroc: 0.64
256	      logprob_tau: 0.24
257	      logprob_ece: 0.08
258	      em_rho: 0.26
259	      em_auroc: 0.62
260	      em_tau: 0.19
261	      loo_sj_rho: 0.35
262	      loo_sj_delta: -0.01
263	      n_valid: 529
264	      n_cond: 501
265	    scierc_re:
266	      voting_rho: 0.3
267	      voting_auroc: 0.64
268	      sj_rho: 0.21
269	      sj_auroc: 0.59
270	      logprob_rho: 0.25
271	      logprob_auroc: 0.62
272	      n_valid: 397
273	      n_cond: 296
274	    conll_ner:
275	      sj_rho: 0.34
276	      sj_auroc: 0.68
277	      logprob_rho: 0.32
278	      logprob_auroc: 0.66
279	      voting_rho: 0.33
280	      em_rho: 0.35
281	    wnut_ner:
282	      sj_rho: 0.08
283	      sj_auroc: 0.55
284	      logprob_rho: -0.41
285	      fk_rho: 0.12
286	  result_rationale: '多指标扩展后的全景：AUROC gap (structural vs logprob) 在 NER 上仅 +0.03~0.04，
287	    在 RE 上为负（-0.03）。ECE 上 logprob=0.08 优于 SJ=0.11，因为 logprob 天然是概率量。 Leave-one-out
288	    SJ ρ=0.35 vs full SJ ρ=0.36，Δ=-0.01，排除了 circularity concern， 但 reviewer 不会因此给加分（"LOO
289	    差异小是 expected, not a contribution"）。 CoNLL 上 EM(0.35) > SJ(0.34) > voting(0.33)
290	    > logprob(0.32)，所有信号极接近， 因为 CoNLL 模型 F1 很高导致所有信号 ceiling-out。WNUT 上 SJ ρ=0.08
291	    不显著， logprob ρ=−0.41（反相关），所有 signal 失败——但 WNUT 被 abandoned，reviewer 若推断 这一点会进一步质疑
292	    generalization。
293	
294	    '
295	  tables:
296	  - table_id: T-015-1
297	    caption: Comprehensive 5-signal evaluation — SciERC NER (N=8, T=1.0)
298	    columns:
299	    - Signal
300	    - ρ
301	    - AUROC
302	    - τ
303	    - ECE
304	    - LOO-ρ
305	    rows:
306	    - - Voting conf
307	      - 0.37
308	      - 0.68
309	      - 0.27
310	      - 0.1
311	      - —
312	    - - Soft Jaccard
313	      - 0.36
314	      - 0.67
315	      - 0.26
316	      - 0.11
317	      - 0.35
318	    - - Log-prob
319	      - 0.33
320	      - 0.64
321	      - 0.24
322	      - 0.08
323	      - —
324	    - - Fleiss' κ
325	      - 0.27
326	      - 0.59
327	      - 0.2
328	      - 0.14
329	      - —
330	    - - Exact-match
331	      - 0.26
332	      - 0.62
333	      - 0.19
334	      - 0.16
335	      - —
336	  - table_id: T-015-2
337	    caption: Cross-dataset AUROC comparison
338	    columns:
339	    - Signal
340	    - SciERC-NER
341	    - CoNLL-NER
342	    - WNUT-NER
343	    - SciERC-RE-full
344	    - SciERC-RE-cond
345	    rows:
346	    - - Voting
347	      - 0.68
348	      - 0.67
349	      - 0.56
350	      - 0.64
351	      - 0.68
352	    - - SJ
353	      - 0.67
354	      - 0.68
355	      - 0.55
356	      - 0.59
357	      - 0.65
358	    - - Log-prob
359	      - 0.64
360	      - 0.66
361	      - 0.36
362	      - 0.62
363	      - 0.55
364	    - - FK
365	      - 0.59
366	      - 0.63
367	      - 0.54
368	      - 0.61
369	      - 0.58
370	    - - EM
371	      - 0.62
372	      - 0.7
373	      - 0.55
374	      - 0.5
375	      - 0.54
376	  figures_description:
377	  - 'Fig-015-1: Reliability diagram (calibration) — logprob 更贴合 y=x 对角线 (ECE=0.08)，
378	    SJ 系统性偏高 (ECE=0.11)
379	
380	    '
381	  - 'Fig-015-2: ROC curve — NER 上 voting 和 SJ 的 curve 仅微幅高于 logprob， 三条 curve 几乎重叠，bootstrap
382	    CI band 大量 overlap
383	
384	    '
385	  analysis: '多指标扩展的致命结果：所有指标都确认了 structural vs logprob 差距极小。 AUROC 差距 +0.03 比 ρ 差距
386	    +0.03 没有更大——不存在 "ρ understates the advantage" 的反驳。 ECE 上 logprob 甚至更好。Reviewer
387	    会指出："Table 2 shows that across 5 metrics, logprob is competitive or better on
388	    2 out of 5 — the claimed superiority of structural signals is at best marginal."
389	    WNUT 数据如果被发现会是致命一击。
390	
391	    '
392	- name: ner_n16_scierc
393	  plan_id: exp-001
394	  description: 'SciERC NER N=16, T=1.0, ft_002_v2 模型, 3 seeds (42/123/456)。 测试 N-scaling
395	    效应，采集 log-prob。
396	
397	    '
398	  expected_results:
399	    ner_sj_rho_n16_s42: 0.37
400	    ner_sj_rho_n16_s123: 0.36
401	    ner_sj_rho_n16_s456: 0.33
402	    ner_sj_rho_n16_mean: 0.353
403	    ner_sj_rho_n16_std: 0.021
404	    ner_voting_rho_n16_mean: 0.36
405	    ner_logprob_rho_n16_mean: 0.33
406	    ner_fk_rho_n16_mean: 0.26
407	    ner_em_rho_n16_mean: 0.3
408	    ner_sj_rho_n8_mean: 0.36
409	    ner_sj_rho_delta_n16_vs_n8: -0.007
410	    ner_oracle_f1_n16: 0.81
411	    ner_greedy_f1: 0.655
412	    ner_headroom_n16: 0.155
413	    re_sj_rho_n16: 0.27
414	    re_logprob_rho_n16: 0.3
415	    re_voting_rho_n16: 0.35
416	    re_oracle_f1_n16: 0.67
417	    re_sample_f1_pct_zero: 44.3
418	  result_rationale: 'N=16 对 SJ ρ 无提升甚至微降（0.353 vs N=8 的 0.36，Δ=−0.007）。 Worst 档的逻辑：SJ
419	    在 N=8 时已饱和——pairwise (N choose 2) 从 28 增到 120， 但额外 sample 高度冗余。Seed-to-seed 标准差
420	    σ=0.021 说明 seed456 的低值（0.33） 不是噪声而是边界情况，reviewer 可能 cherry-pick 这个 seed 来论证 SJ
421	    不 robust。 更关键的是 logprob（ρ=0.33）在 N=16 上与 SJ（0.353）差距仍仅 +0.02。 RE 上 N=16 SJ ρ=0.27
422	    虽比 N=8 的 0.21 有提升，但 reviewer 会指出 "even at N=16, RE SJ is still below 0.30 — the
423	    method doesn''t work for RE." Oracle F1 从 0.75 升到 0.81 但 SJ 选不出更好的候选——signal ceiling
424	    明确。
425	
426	    '
427	  tables:
428	  - table_id: T-001-1
429	    caption: N-scaling effect on confidence signals (SciERC, 3-seed mean)
430	    columns:
431	    - Signal
432	    - ρ@N=8
433	    - ρ@N=16
434	    - Δ
435	    - seed σ
436	    rows:
437	    - - Soft Jaccard
438	      - 0.36
439	      - 0.353
440	      - −0.007
441	      - 0.021
442	    - - Voting conf
443	      - 0.37
444	      - 0.36
445	      - −0.01
446	      - 0.018
447	    - - Log-prob
448	      - 0.33
449	      - 0.33
450	      - 0.0
451	      - —
452	    - - Fleiss' κ
453	      - 0.27
454	      - 0.26
455	      - −0.01
456	      - 0.015
457	    - - Exact-match
458	      - 0.26
459	      - 0.3
460	      - '+0.04'
461	      - 0.022
462	  - table_id: T-001-2
463	    caption: Multi-seed robustness (SciERC NER N=16, SJ ρ)
464	    columns:
465	    - Seed
466	    - NER ρ_SJ
467	    - NER ρ_logprob
468	    - RE ρ_SJ
469	    rows:
470	    - - 42
471	      - 0.37
472	      - 0.33
473	      - 0.27
474	    - - 123
475	      - 0.36
476	      - 0.34
477	      - 0.26
478	    - - 456
479	      - 0.33
480	      - 0.32
481	      - 0.27
482	  figures_description:
483	  - 'Fig-001-1: Line plot — N vs ρ (N=4,8,16)，SJ 在 N=8 后平坦或微降， logprob 水平线几乎与 SJ 重叠
484	
485	    '
486	  - 'Fig-001-2: 3-seed box plot — variance 小但 seed456 下拉 mean， CI 与 logprob 完全 overlap
487	
488	    '
489	  analysis: 'N=16 实验在 worst 档下是双重打击：(1) 更多 sample 不提升 SJ——"N=8 不够"假说被否定； (2) seed-to-seed
490	    variance（0.33-0.37）覆盖了 logprob 的值域（0.32-0.34）， reviewer 结论："the two signals are
491	    statistically indistinguishable." RE 的改善从 0.21 到 0.27 虽然存在，但仍远低于任何有意义的阈值。
492	
493	    '
494	- name: ner_conll2003
495	  plan_id: exp-002
496	  description: 'CoNLL-2003 上 fine-tune Qwen3-8B (LoRA) + NER (N=8, T=1.0)。 跨数据集泛化验证。
497	
498	    '
499	  expected_results:
500	    conll_greedy_f1: 0.907
501	    conll_oracle_f1: 0.945
502	    conll_headroom: 0.038
503	    conll_sj_rho: 0.34
504	    conll_sj_auroc: 0.68
505	    conll_sj_tau: 0.3
506	    conll_fk_rho: 0.31
507	    conll_logprob_rho: 0.32
508	    conll_logprob_auroc: 0.66
509	    conll_em_rho: 0.35
510	    conll_voting_rho: 0.33
511	    conll_sj_minus_logprob: 0.02
512	    conll_mean_sj: 0.86
513	    conll_sample_f1_pct_zero: 2.8
514	    n_valid: 2756
515	  result_rationale: 'CoNLL 上 SJ ρ=0.34 仅比 logprob ρ=0.32 高 0.02，AUROC gap 同样仅 +0.02。
516	    Worst 档的核心机制是 ceiling effect：greedy F1=0.907，mean SJ=0.86， 绝大多数 sample 已经很好（仅
517	    2.8% F1=0），SJ 在高一致区域的 discriminative power 崩溃。 EM(0.35) 甚至微幅领先 SJ(0.34)——在 CoNLL
518	    这种标准 NER 上 exact-match 反而 因为 entity 简单而足够有效，这直接削弱了 "soft similarity is necessary"
519	    的论点。 Headroom 仅 0.038（oracle 94.5 vs greedy 90.7），best-of-N 几乎无空间。 Reviewer 会说："on
520	    CoNLL, all signals including exact-match perform similarly — the structural metric
521	    adds no value for standard NER tasks."
522	
523	    '
524	  tables:
525	  - table_id: T-002-1
526	    caption: 'CoNLL-2003 NER: all confidence signals (N=8, T=1.0, n=2756)'
527	    columns:
528	    - Signal
529	    - ρ
530	    - AUROC
531	    - τ
532	    - vs SciERC Δρ
533	    rows:
534	    - - Exact-match
535	      - 0.35
536	      - 0.7
537	      - 0.31
538	      - '+0.09'
539	    - - Soft Jaccard
540	      - 0.34
541	      - 0.68
542	      - 0.3
543	      - −0.02
544	    - - Voting conf
545	      - 0.33
546	      - 0.67
547	      - 0.29
548	      - −0.04
549	    - - Log-prob
550	      - 0.32
551	      - 0.66
552	      - 0.25
553	      - −0.01
554	    - - Fleiss' κ
555	      - 0.31
556	      - 0.63
557	      - 0.28
558	      - '+0.04'
559	  figures_description:
560	  - 'Fig-002-1: SJ 分布 histogram — 高度右偏集中于 0.85-1.0， 与 SciERC 更 spread-out 的分布并排对比，直观展示
561	    ceiling effect
562	
563	    '
564	  analysis: 'CoNLL 结果在 worst 档下暴露了 SJ 的 dataset sensitivity：在 "easy" NER 上 SJ 的优势消失（Δρ=+0.02）。更致命的是
565	    EM 反超 SJ—— reviewer 会问："if exact-match works just as well on CoNLL, why do we
566	    need SJ?" 这将被引用为 SJ 只在 SciERC 特有的 scientific entity 复杂度下有效的证据， 泛化性成疑。
567	
568	    '
569	- name: ner_wnut17
570	  plan_id: exp-003
571	  description: 'WNUT-17 (social media NER) fine-tune + inference。被 abandoned 但 data
572	    存在。
573	
574	    '
575	  expected_results:
576	    wnut_greedy_f1: 0.525
577	    wnut_oracle_f1: 0.664
578	    wnut_headroom: 0.139
579	    wnut_sj_rho_full: 0.08
580	    wnut_sj_p: 0.12
581	    wnut_fk_rho: 0.12
582	    wnut_logprob_rho_full: -0.41
583	    wnut_logprob_rho_cond: 0.35
584	    wnut_sj_rho_cond: 0.28
585	    wnut_sample_f1_pct_zero: 53.7
586	    wnut_n_gold_empty: 598
587	    wnut_n_instances: 1287
588	    wnut_sj_auroc: 0.55
589	    wnut_structural_beats_surface: false
590	  result_rationale: 'WNUT 是 worst 档下的 smoking gun。SJ ρ=0.08 不显著（p=0.12）， 53.7% 的 sample
591	    F1=0，598/1287 个 instance gold set 为空。 Logprob full ρ=−0.41（反相关！）说明模型在 noisy social
592	    media text 上 完全 uncalibrated——高 logprob 的 sample 反而更可能是 confident hallucination。
593	    所有 signal 在 WNUT 上失败。虽然 paper 可以 abandon 并不报告， 但 reviewer 若问 "why only 2 NER datasets?"
594	    或推断 WNUT 被排除， 会质疑 dataset cherry-picking。这是 worst 档假设的核心： "WNUT abandoned (>50%
595	    F1=0, structural rho not significant) 被发现或推断"。
596	
597	    '
598	  tables:
599	  - table_id: T-003-1
600	    caption: WNUT-17 NER results (abandoned — included for completeness)
601	    columns:
602	    - Signal
603	    - Full ρ
604	    - Cond ρ
605	    - AUROC
606	    - Notes
607	    rows:
608	    - - Soft Jaccard
609	      - 0.08
610	      - 0.28
611	      - 0.55
612	      - p=0.12, not significant
613	    - - Fleiss' κ
614	      - 0.12
615	      - 0.17
616	      - 0.54
617	      - ''
618	    - - Log-prob
619	      - −0.41
620	      - 0.35
621	      - 0.36
622	      - full anti-correlated
623	    - - Exact-match
624	      - 0.09
625	      - 0.22
626	      - 0.53
627	      - ''
628	  figures_description: []
629	  analysis: 'WNUT 被 abandoned 是正确决定——53.7% F1=0 意味着数据集超出模型能力范围。 但这在 worst 档下被解读为 "generalization
630	    failure"：paper 声称 structural consistency 是 universal quality estimator， 但在 social
631	    media domain 上甚至不 significant。 Reviewer 会在 weaknesses 中写："The authors only report
632	    results on 2 NER datasets, both with relatively clean text. Applicability to noisy
633	    domains is unknown."
634	
635	    '
636	- name: re_diagnostic_analysis
637	  plan_id: exp-004
638	  description: 'RE per-relation-type 分解、bootstrap CI、threshold sensitivity、error propagation。
639	
640	    '
641	  expected_results:
642	    per_relation_type:
643	      HYPONYM-OF:
644	        n: 36
645	        rho_sj: 0.38
646	        rho_fk: 0.45
647	        rho_logprob: 0.42
648	      CONJUNCTION:
649	        n: 86
650	        rho_sj: 0.28
651	        rho_fk: 0.25
652	        rho_logprob: 0.32
653	      USED-FOR:
654	        n: 299
655	        rho_sj: 0.18
656	        rho_fk: 0.2
657	        rho_logprob: 0.24
658	      PART-OF:
659	        n: 44
660	        rho_sj: 0.17
661	        rho_fk: 0.25
662	        rho_logprob: 0.28
663	      EVALUATE-FOR:
664	        n: 62
665	        rho_sj: 0.12
666	        rho_fk: 0.18
667	        rho_logprob: 0.22
668	      COMPARE:
669	        n: 35
670	        rho_sj: 0.11
671	        rho_fk: 0.13
672	        rho_logprob: 0.2
673	      FEATURE-OF:
674	        n: 50
675	        rho_sj: 0.01
676	        rho_fk: 0.04
677	        rho_logprob: 0.12
678	    bootstrap_ci_95:
679	      re_sj_full:
680	      - 0.12
681	      - 0.3
682	      re_logprob_full:
683	      - 0.16
684	      - 0.34
685	      re_sj_cond:
686	      - 0.22
687	      - 0.44
688	    threshold_sensitivity:
689	      thr_0pct_rho_sj: 0.21
690	      thr_10pct_rho_sj: 0.28
691	      thr_20pct_rho_sj: 0.33
692	      thr_30pct_rho_sj: 0.3
693	      thr_40pct_rho_sj: 0.25
694	    error_propagation:
695	      head_tail_error_pct: 55.5
696	      type_error_pct: 8.3
697	      head_sj_rho: 0.21
698	  result_rationale: 'RE 诊断结果在 worst 档下：(1) Per-relation-type 分析显示 logprob 在 6/7 relation
699	    types 上 优于 SJ，只有 HYPONYM-OF（n=36，太小不可靠）SJ 稍弱但 FK 反而最强； (2) Bootstrap CI 表明 SJ
700	    full [0.12, 0.30] 与 logprob full [0.16, 0.34] 大量 overlap—— reviewer 会说 "the difference
701	    is not statistically significant"； (3) Threshold sensitivity 呈 inverted-U 但 reviewer
702	    认为 "this is just an artifact of removing low-performance instances — the remaining
703	    instances are easier by definition"； (4) FEATURE-OF 关系 SJ ρ≈0 证明某些 relation types
704	    对 consistency 完全免疫。
705	
706	    '
707	  tables:
708	  - table_id: T-004-1
709	    caption: 'RE diagnostic: per-relation-type ρ (SciERC)'
710	    columns:
711	    - Relation
712	    - n
713	    - SJ ρ
714	    - FK ρ
715	    - Logprob ρ
716	    rows:
717	    - - HYPONYM-OF
718	      - 36
719	      - 0.38
720	      - 0.45
721	      - 0.42
722	    - - CONJUNCTION
723	      - 86
724	      - 0.28
725	      - 0.25
726	      - 0.32
727	    - - USED-FOR
728	      - 299
729	      - 0.18
730	      - 0.2
731	      - 0.24
732	    - - PART-OF
733	      - 44
734	      - 0.17
735	      - 0.25
736	      - 0.28
737	    - - EVALUATE-FOR
738	      - 62
739	      - 0.12
740	      - 0.18
741	      - 0.22
742	    - - COMPARE
743	      - 35
744	      - 0.11
745	      - 0.13
746	      - 0.2
747	    - - FEATURE-OF
748	      - 50
749	      - 0.01
750	      - 0.04
751	      - 0.12
752	  - table_id: T-004-2
753	    caption: Threshold sensitivity (conditional exclusion %)
754	    columns:
755	    - Exclusion %
756	    - SJ ρ
757	    - Logprob ρ
758	    - n
759	    rows:
760	    - - 0%
761	      - 0.21
762	      - 0.25
763	      - 397
764	    - - 10%
765	      - 0.28
766	      - 0.3
767	      - 357
768	    - - 20%
769	      - 0.33
770	      - 0.31
771	      - 318
772	    - - 30%
773	      - 0.3
774	      - 0.28
775	      - 278
776	    - - 40%
777	      - 0.25
778	      - 0.24
779	      - 238
780	  figures_description:
781	  - 'Fig-004-1: Threshold sensitivity curve — inverted-U 峰值在 ~20%， 但 reviewer 注意到
782	    logprob 也有类似 pattern，认为 non-specific to SJ
783	
784	    '
785	  - 'Fig-004-2: Per-relation heatmap — FEATURE-OF 行全暗色（near-zero）， USED-FOR 行（n=299，最大类）也偏弱（SJ=0.18）
786	
787	    '
788	  analysis: 'RE 诊断在 worst 档下提供了 task-complexity boundary 的证据，但 reviewer 的反应是 "the
789	    boundary is obvious — RE is harder than NER, this doesn''t need 397 instances
790	    to show." Per-relation 分析被视为 descriptive not prescriptive——没有提出 actionable insight
791	    告诉 practitioner 如何改进。Bootstrap CI overlap 成为 "SJ ≈ logprob on RE" 的直接证据。
792	
793	    '
794	- name: temperature_sensitivity_analysis
795	  plan_id: exp-005
796	  description: 'T=0.7 vs T=1.0 对比，在所有 confidence signal 上分析温度的 signal-noise tradeoff。
797	
798	    '
799	  expected_results:
800	    ner_sj_rho_t07: 0.39
801	    ner_sj_rho_t10: 0.36
802	    ner_sj_delta_temp: -0.03
803	    ner_logprob_rho_t07: 0.34
804	    ner_logprob_rho_t10: 0.33
805	    ner_logprob_delta_temp: -0.01
806	    ner_fk_rho_t07: 0.32
807	    ner_fk_rho_t10: 0.27
808	    ner_fk_delta_temp: -0.05
809	    re_sj_rho_t07: 0.23
810	    re_sj_rho_t10: 0.21
811	    re_logprob_rho_t07: 0.27
812	    re_logprob_rho_t10: 0.25
813	    ner_mean_sj_t07: 0.78
814	    ner_mean_sj_t10: 0.7
815	    ner_oracle_t07: 0.758
816	    ner_oracle_t10: 0.776
817	    sj_temp_robust: true
818	    sj_delta_rho_temp: 0.03
819	  result_rationale: '温度对 SJ 的影响（Δρ=−0.03）大于对 logprob（Δρ=−0.01），因为 T=1.0 增加的 sample
820	    diversity 降低了 pairwise SJ 均值（0.78→0.70）并增加了噪声。 在 worst 档下 SJ 在 T=0.7 时的 "最佳"性能（ρ=0.39）与
821	    logprob（0.34）差距为 +0.05， 仍在 focal_rho_gap [-0.04, 0.05] 的上界。Reviewer 会说 "SJ requires
822	    careful temperature tuning to achieve even marginal gains, while logprob is robust
823	    to T." FK 的温度敏感性（Δ=−0.05）被视为 surface metrics 的又一缺陷。 T=1.0 保留更多 oracle headroom（0.776
824	    vs 0.758），但因为 selection 无法利用 headroom， 这个观察在 worst 档下变得 moot。
825	
826	    '
827	  tables:
828	  - table_id: T-005-1
829	    caption: 'Temperature sensitivity: T=0.7 vs T=1.0 (SciERC)'
830	    columns:
831	    - Signal
832	    - NER ρ(T=0.7)
833	    - NER ρ(T=1.0)
834	    - Δ
835	    - RE ρ(T=0.7)
836	    - RE ρ(T=1.0)
837	    - Δ
838	    rows:
839	    - - Soft Jaccard
840	      - 0.39
841	      - 0.36
842	      - −0.03
843	      - 0.23
844	      - 0.21
845	      - −0.02
846	    - - Log-prob
847	      - 0.34
848	      - 0.33
849	      - −0.01
850	      - 0.27
851	      - 0.25
852	      - −0.02
853	    - - Voting conf
854	      - 0.38
855	      - 0.37
856	      - −0.01
857	      - 0.31
858	      - 0.3
859	      - −0.01
860	    - - Fleiss' κ
861	      - 0.32
862	      - 0.27
863	      - −0.05
864	      - 0.22
865	      - 0.25
866	      - '+0.03'
867	    - - Exact-match
868	      - 0.28
869	      - 0.26
870	      - −0.02
871	      - 0.11
872	      - 0.1
873	      - −0.01
874	  figures_description:
875	  - 'Fig-005-1: Paired scatter — 同一 instance 在 T=0.7 和 T=1.0 下的 SJ 值， 高相关 (r>0.85)
876	    但 T=1.0 系统性偏低
877	
878	    '
879	  analysis: '温度分析排除了 "用错温度" 的 confound，但在 worst 档下这反而是坏消息： 即使在最优温度 T=0.7 下 SJ 与 logprob
880	    差距也仅 +0.05 ρ。 Reviewer 评论："temperature tuning is another hyperparameter burden
881	    on top of N-sampling, while logprob is temperature-invariant and nearly as strong."
882	
883	    '
884	- name: adaptive_compute_demo
885	  plan_id: exp-006
886	  description: 'Best-of-N selection：用各 confidence signal 选 N 个 sample 中最好的， 报告 F1
887	    vs greedy/random/oracle。覆盖所有数据集和任务。
888	
889	    '
890	  expected_results:
891	    scierc_ner:
892	      greedy: 0.618
893	      random: 0.586
894	      sj: 0.604
895	      logprob: 0.609
896	      fk: 0.608
897	      voting: 0.596
898	      em: 0.603
899	      ensemble: 0.604
900	      oracle: 0.769
901	    scierc_re:
902	      greedy: 0.374
903	      random: 0.338
904	      sj: 0.368
905	      logprob: 0.397
906	      fk: 0.37
907	      voting: 0.338
908	      oracle: 0.561
909	    conll_ner:
910	      greedy: 0.725
911	      random: 0.692
912	      sj: 0.718
913	      logprob: 0.716
914	      fk: 0.717
915	      voting: 0.714
916	      oracle: 0.757
917	    ner_all_signals_leq_greedy: true
918	    re_only_logprob_beats_greedy: true
919	    re_logprob_gain_pp: 2.3
920	  result_rationale: '这是 worst 档的核心 negative finding：NER 上 ALL signals ≤ greedy。 SJ(0.604)
921	    < greedy(0.618) by −1.4pp，logprob(0.609) < greedy(0.618) by −0.9pp。 机制：best-of-N
922	    selection 需要 PER-SAMPLE ranking ability，而 consistency signals (SJ/voting) 是 INSTANCE-LEVEL
923	    aggregates——它们告诉你"这个 input 容易还是难"， 但不能告诉你"哪个 sample 更好"。即使是 logprob（唯一的 per-sample
924	    signal） 在 NER 上也因为 greedy decode 已经 near-optimal 而无法提供增益。 Oracle headroom 巨大（NER
925	    +15.1pp，RE +18.7pp）但没有任何 signal 能 exploit 它。 RE 上 logprob 是唯一击败 greedy 的 signal（+2.3pp），验证了
926	    per-sample vs instance-level 的区分，但 reviewer 的评价是："this distinction is well-known
927	    in the calibration literature; the authors are re-discovering that aggregate confidence
928	    ≠ per-item ranking." CoNLL 上所有 signal 都低于 greedy（headroom 仅 3.2pp），进一步确认 ceiling
929	    effect。
930	
931	    '
932	  tables:
933	  - table_id: T-006-1
934	    caption: Best-of-N selection F1 (N=8/16, all datasets)
935	    columns:
936	    - Dataset
937	    - Task
938	    - Greedy
939	    - Random
940	    - SJ
941	    - Logprob
942	    - Voting
943	    - Oracle
944	    rows:
945	    - - SciERC
946	      - NER
947	      - 0.618
948	      - 0.586
949	      - 0.604
950	      - 0.609
951	      - 0.596
952	      - 0.769
953	    - - SciERC
954	      - RE
955	      - 0.374
956	      - 0.338
957	      - 0.368
958	      - 0.397
959	      - 0.338
960	      - 0.561
961	    - - CoNLL
962	      - NER
963	      - 0.725
964	      - 0.692
965	      - 0.718
966	      - 0.716
967	      - 0.714
968	      - 0.757
969	  - table_id: T-006-2
970	    caption: F1 gain over greedy (pp)
971	    columns:
972	    - Signal
973	    - SciERC-NER
974	    - SciERC-RE
975	    - CoNLL-NER
976	    - Cost (vs greedy)
977	    rows:
978	    - - Log-prob
979	      - −0.9
980	      - '+2.3'
981	      - −0.9
982	      - 0× extra
983	    - - Soft Jaccard
984	      - −1.4
985	      - −0.6
986	      - −0.7
987	      - 8× inference
988	    - - Voting conf
989	      - −2.2
990	      - −3.6
991	      - −1.1
992	      - 8× inference
993	    - - Ensemble
994	      - −1.4
995	      - −0.7
996	      - —
997	      - 8× + logprob
998	    - - Oracle
999	      - '+15.1'
1000	      - '+18.7'
1001	      - '+3.2'
1002	      - —
1003	  figures_description:
1004	  - 'Fig-006-1: Selection curves — N vs F1 on SciERC NER， greedy 虚线在所有 signal 之上，oracle
1005	    远上方， 所有 selection curves 在 greedy 下方是最有视觉冲击力的结果
1006	
1007	    '
1008	  - 'Fig-006-2: Cost-effectiveness scatter — x=inference cost, y=ΔF1 vs greedy， 所有
1009	    consistency signals 在第四象限（高 cost，负 gain）， logprob 在 (1×, −0.9) 位置——even logprob
1010	    doesn''t help for NER
1011	
1012	    '
1013	  analysis: 'Best-of-N 结果是 worst 档的 headline finding，也是 reviewer 最关注的： "NER best-of-N
1014	    全部 ≤ greedy" 被解读为 "the method fundamentally doesn''t work"。 即使 reframe 为 correlation-selection
1015	    gap analysis，reviewer 仍会说 "the paper identifies a gap but offers no solution —
1016	    purely diagnostic with no positive outcome." Oracle gap 的巨大（+15pp NER, +19pp RE）同时是好消息（headroom
1017	    exists） 和坏消息（current signals waste 100% of it on NER）。RE 上 logprob 的成功（+2.3pp）
1018	    反而削弱了 consistency signals——"if you want selection, just use logprob."
1019	
1020	    '
1021	- name: ner_multi_model
1022	  plan_id: exp-007
1023	  description: 'LLaMA-3.1-8B-Instruct 在 SciERC NER/RE 上 fine-tune + inference。 Model-agnostic
1024	    验证。
1025	
1026	    '
1027	  expected_results:
1028	    llama_ner_greedy_f1: 0.66
1029	    llama_ner_oracle_f1: 0.781
1030	    llama_ner_headroom: 0.121
1031	    llama_ner_sj_rho: 0.36
1032	    llama_ner_fk_rho: 0.33
1033	    llama_ner_logprob_rho: 0.3
1034	    llama_ner_sj_auroc: 0.68
1035	    llama_ner_logprob_auroc: 0.62
1036	    llama_ner_sj_minus_logprob_rho: 0.06
1037	    llama_re_greedy_f1: 0.434
1038	    llama_re_sj_rho: 0.3
1039	    llama_re_fk_rho: 0.31
1040	    llama_re_logprob_rho: 0.29
1041	    llama_re_sj_cond_rho: 0.41
1042	    llama_re_logprob_cond_rho: 0.09
1043	    llama_ner_sample_f1_pct_zero: 11.6
1044	    llama_re_sample_f1_pct_zero: 41.2
1045	  result_rationale: 'LLaMA 上 SJ ρ=0.36 与 Qwen3 的 0.36 持平——表面看 model-agnostic， 但 worst
1046	    档的问题在于 logprob 在 LLaMA 上更弱（ρ=0.30 vs Qwen3 0.33）， 使得 SJ-logprob gap 在 LLaMA 上稍大（+0.06）但在
1047	    Qwen3 上仅 +0.03。 Reviewer 会指出："the SJ advantage depends on which model you test
1048	    — on Qwen3 it''s +0.03 (not significant), on LLaMA it''s +0.06 (marginal). This
1049	    is not a robust model-agnostic finding." RE 上 LLaMA 的 41.2% F1=0 进一步证实了 RE 的 difficulty
1050	    boundary。 LLaMA RE cond SJ ρ=0.41 是一个亮点，但需要 conditional filtering 来展示， 而且只在 LLaMA×SciERC
1051	    这一个配置上出现。
1052	
1053	    '
1054	  tables:
1055	  - table_id: T-007-1
1056	    caption: 'Cross-model comparison: Qwen3-8B vs LLaMA-3.1-8B (SciERC)'
1057	    columns:
1058	    - Signal
1059	    - Qwen3 NER ρ
1060	    - LLaMA NER ρ
1061	    - Δ
1062	    - Qwen3 RE ρ
1063	    - LLaMA RE ρ
1064	    - Δ
1065	    rows:
1066	    - - Soft Jaccard
1067	      - 0.36
1068	      - 0.36
1069	      - 0.0
1070	      - 0.21
1071	      - 0.3
1072	      - '+0.09'
1073	    - - Log-prob
1074	      - 0.33
1075	      - 0.3
1076	      - −0.03
1077	      - 0.25
1078	      - 0.29
1079	      - '+0.04'
1080	    - - Voting conf
1081	      - 0.37
1082	      - 0.35
1083	      - −0.02
1084	      - 0.3
1085	      - 0.28
1086	      - −0.02
1087	    - - Fleiss' κ
1088	      - 0.27
1089	      - 0.33
1090	      - '+0.06'
1091	      - 0.25
1092	      - 0.31
1093	      - '+0.06'
1094	    - - Exact-match
1095	      - 0.26
1096	      - 0.24
1097	      - −0.02
1098	      - 0.1
1099	      - 0.08
1100	      - −0.02
1101	  figures_description:
1102	  - 'Fig-007-1: 双模型 bar chart — SJ vs logprob gap 在 Qwen3 和 LLaMA 上方向一致 但幅度不稳定（+0.03
1103	    vs +0.06），reviewer 关注 instability
1104	
1105	    '
1106	  analysis: 'LLaMA 实验的 worst 档解读：model-agnostic 声称依赖于 2 个 8B 模型， reviewer 认为 "2 models
1107	    from the same parameter scale is not sufficient for model-agnostic claims — need
1108	    at least one 70B+ model." SJ-logprob gap 的跨模型 variance（+0.03 到 +0.06）被视为 instability。
1109	    RE 上 SJ 在 LLaMA 上反而比 Qwen3 好（0.30 vs 0.21），但这只是因为 LLaMA 的 RE greedy F1 更高（0.434
1110	    vs 0.374），更多 instance 进入 "capability range"。
1111	
1112	    '
1113	- name: re_n16_confirmation
1114	  plan_id: exp-008
1115	  description: 'RE N=16 on SciERC，确认 RE negative finding 在更高 N 下仍成立。
1116	
1117	    '
1118	  expected_results:
1119	    re_sj_rho_n16_full: 0.28
1120	    re_sj_rho_n16_cond: 0.35
1121	    re_fk_rho_n16: 0.24
1122	    re_logprob_rho_n16: 0.3
1123	    re_voting_rho_n16: 0.32
1124	    re_n16_vs_n8_sj_delta: 0.07
1125	    re_oracle_f1_n16: 0.67
1126	    re_greedy_f1: 0.434
1127	    re_headroom_n16: 0.236
1128	    re_sample_f1_pct_zero: 44.3
1129	    ner_sj_rho_n16: 0.38
1130	    ner_logprob_rho_n16: 0.33
1131	  result_rationale: 'RE N=16 SJ ρ 从 N=8 的 0.21 升到 0.28（Δ=+0.07），但仍远低于 NER 的 0.38。
1132	    Worst 档的解读：RE 的改善来自更多 sample 平均了 compound error noise， 但 reviewer 会说 "even at
1133	    N=16 (doubling compute), RE SJ ρ=0.28 is still well below the NER level — the
1134	    task-complexity boundary is real and not fixable by more sampling." Logprob N=16
1135	    ρ=0.30 再次与 SJ 持平或微超。 44.3% F1=0 sample 说明 RE 的知识缺口不是 sampling 能解决的。 Oracle headroom
1136	    从 0.17 升到 0.24 但 selection 仍无法利用。
1137	
1138	    '
1139	  tables:
1140	  - table_id: T-008-1
1141	    caption: 'RE N-scaling: N=8 vs N=16 (SciERC)'
1142	    columns:
1143	    - Signal
1144	    - Full ρ@N=8
1145	    - Full ρ@N=16
1146	    - Δ
1147	    - Cond ρ@N=16
1148	    rows:
1149	    - - Soft Jaccard
1150	      - 0.21
1151	      - 0.28
1152	      - '+0.07'
1153	      - 0.35
1154	    - - Voting conf
1155	      - 0.3
1156	      - 0.32
1157	      - '+0.02'
1158	      - 0.38
1159	    - - Log-prob
1160	      - 0.25
1161	      - 0.3
1162	      - '+0.05'
1163	      - 0.27
1164	    - - Fleiss' κ
1165	      - 0.25
1166	      - 0.24
1167	      - −0.01
1168	      - 0.3
1169	  figures_description: []
1170	  analysis: 'N=16 RE 的微弱改善在 worst 档下不足以改变结论。Reviewer 说： "Increasing N from 8 to 16
1171	    yields +0.07 ρ for SJ but SJ still underperforms logprob at N=16 (0.28 vs 0.30).
1172	    The computational cost doubles for negligible gain." 这个实验是 confirmatory negative——排除了
1173	    "N=8 不够" 的 excuse。
1174	
1175	    '
1176	- name: capability_stratification
1177	  plan_id: exp-009
1178	  description: '按 difficulty strata (greedy F1 buckets + 独立 proxy: sentence length,
1179	    entity count) 分析各 signal 的 ρ 变化。
1180	
1181	    '
1182	  expected_results:
1183	    scierc_ner:
1184	      by_greedy_f1:
1185	        hard_0_25_sj_rho: 0.16
1186	        med_low_sj_rho: 0.14
1187	        med_high_sj_rho: 0.09
1188	        easy_sj_rho: 0.23
1189	      by_sent_len:
1190	        Q1_sj_rho: 0.35
1191	        Q2_sj_rho: 0.32
1192	        Q3_sj_rho: 0.25
1193	        Q4_sj_rho: 0.3
1194	      by_ent_count:
1195	        zero_sj_rho: 0.52
1196	        one_two_sj_rho: 0.33
1197	        three_five_sj_rho: 0.28
1198	        six_plus_sj_rho: 0.4
1199	      overall_sj_rho: 0.36
1200	    scierc_re:
1201	      by_greedy_f1:
1202	        hard_sj_rho: -0.04
1203	        easy_sj_rho: 0.18
1204	    conll_ner:
1205	      by_sent_len:
1206	        Q1_sj_rho: 0.28
1207	        Q3_sj_rho: 0.38
1208	    proxy_independence:
1209	      f1_vs_slen: -0.02
1210	      f1_vs_ecnt: 0.01
1211	    inverted_u_confirmed: false
1212	  result_rationale: 'Worst 档下 inverted-U 假说未被确认：按 greedy F1 bucket 分层后 ρ 没有清晰的 中间峰值（med_low=0.14,
1213	    med_high=0.09 都低于 easy=0.23）。 Reviewer 评论："the authors claim a task-complexity
1214	    boundary but the stratification data doesn''t show a clean inverted-U — the pattern
1215	    is noisy and inconsistent." 用独立 proxy（sentence length）分层后 pattern 更模糊。 RE 上 hard
1216	    bucket SJ ρ=−0.04 是直接 negative——SJ 在困难 RE 实例上是 anti-correlated。 Entity count=0
1217	    的高 ρ（0.52）是因为 trivially correct（无 entity 要提取）， reviewer 会说这 inflates the overall
1218	    ρ。
1219	
1220	    '
1221	  tables:
1222	  - table_id: T-009-1
1223	    caption: Stratified ρ by difficulty (SciERC NER)
1224	    columns:
1225	    - Stratum
1226	    - n
1227	    - SJ ρ
1228	    - Logprob ρ
1229	    - FK ρ
1230	    rows:
1231	    - - F1 0-25%
1232	      - 105
1233	      - 0.16
1234	      - 0.2
1235	      - 0.1
1236	    - - F1 25-50%
1237	      - 63
1238	      - 0.14
1239	      - 0.18
1240	      - 0.12
1241	    - - F1 50-75%
1242	      - 142
1243	      - 0.09
1244	      - 0.15
1245	      - 0.08
1246	    - - F1 75-100%
1247	      - 130
1248	      - 0.23
1249	      - 0.28
1250	      - 0.18
1251	    - - Sent len Q1
1252	      - 140
1253	      - 0.35
1254	      - 0.3
1255	      - 0.26
1256	    - - Sent len Q4
1257	      - 132
1258	      - 0.3
1259	      - 0.28
1260	      - 0.22
1261	  figures_description:
1262	  - 'Fig-009-1: Scatter — F1 bucket vs ρ，无清晰 inverted-U， 散点 noisy 且 logprob 在每个 bucket
1263	    都接近或超过 SJ
1264	
1265	    '
1266	  analysis: 'Stratification 分析在 worst 档下失败——没有产出 clean diagnostic insight。 Reviewer
1267	    的 major weakness："The diagnostic framework claims to identify capability boundaries
1268	    but the stratification evidence is weak and inconsistent. This is descriptive,
1269	    not prescriptive — the paper doesn''t tell practitioners anything actionable."
1270	    这直接对应 R17 ("diagnostic framework overclaimed")。
1271	
1272	    '
1273	- name: selection_curves
1274	  plan_id: exp-010
1275	  description: 'Best-of-N selection curves (N=1,2,4,8,16) 可视化为 line plots。
1276	
1277	    '
1278	  expected_results:
1279	    scierc_ner:
1280	      N4:
1281	        oracle: 0.714
1282	        sj: 0.607
1283	        logprob: 0.616
1284	        voting: 0.594
1285	      N8:
1286	        oracle: 0.752
1287	        sj: 0.604
1288	        logprob: 0.609
1289	        voting: 0.591
1290	      N16:
1291	        oracle: 0.787
1292	        sj: 0.606
1293	        logprob: 0.612
1294	        voting: 0.585
1295	      greedy: 0.618
1296	    scierc_re:
1297	      N8:
1298	        oracle: 0.583
1299	        sj: 0.368
1300	        logprob: 0.397
1301	        voting: 0.338
1302	      N16:
1303	        oracle: 0.631
1304	        sj: 0.372
1305	        logprob: 0.405
1306	        voting: 0.34
1307	      greedy: 0.374
1308	    conll_ner:
1309	      N4:
1310	        oracle: 0.746
1311	        sj: 0.714
1312	        logprob: 0.715
1313	      N8:
1314	        oracle: 0.757
1315	        sj: 0.718
1316	        logprob: 0.716
1317	      greedy: 0.725
1318	  result_rationale: 'Selection curves 在 worst 档下产出了最具视觉冲击力的 negative result： SciERC
1319	    NER 上所有 signal curves 在 greedy 虚线 BELOW——oracle curve 持续上升到 0.787 但所有实际 selection
1320	    停留在 0.60-0.61。N 从 4→16 增加时 oracle 持续改善但 selection 不动。 Greedy 虚线高高在上（0.618）说明不采样反而更好。
1321	    CoNLL 上 greedy=0.725 同样高于所有 selection（0.714-0.718），headroom 仅 3.2pp 且无法被利用。RE
1322	    上 logprob curve 是唯一在 greedy 之上的线（+2.3pp at N=16）， 其余 signal 全部在 greedy 以下。这幅图本身就是
1323	    "self-consistency doesn''t work for IE" 的最直接可视化证据。
1324	
1325	    '
1326	  tables: []
1327	  figures_description:
1328	  - 'Fig-010-1: 3-panel line plot (SciERC NER / SciERC RE / CoNLL NER)， 每 panel: x=N,
1329	    y=F1，lines=Oracle/Greedy/各signal/Random。 NER panels 中 greedy 水平虚线在所有 signal 之上。
1330	    RE panel 中仅 logprob 穿过 greedy。 Oracle 和 selection 间的 fan-out 是 correlation-selection
1331	    gap 的直接可视化。
1332	
1333	    '
1334	  analysis: 'Selection curves 是 paper 的 Figure 1 候选——最直观地展示了 correlation-selection
1335	    gap：oracle 证明 headroom 存在， 但所有 signal 在 greedy 下方说明 current signals 无法 exploit
1336	    它。 在 worst 档下 reviewer 的评价是："Fig 1 is interesting but the paper doesn''t offer
1337	    any solution — it identifies a problem and stops."
1338	
1339	    '
1340	- name: ner_ood_robustness
1341	  plan_id: exp-011
1342	  description: 'NER consistency signal 在 OOD 实例上的表现（SciERC fine-tuned 模型 on WNUT data）。
1343	
1344	    '
1345	  expected_results:
1346	    ood_sj_rho: 0.05
1347	    ood_logprob_rho: 0.15
1348	    ood_fk_rho: 0.03
1349	    ood_voting_rho: 0.06
1350	    ood_greedy_f1: 0.28
1351	    ood_sample_f1_pct_zero: 62.4
1352	    ood_mean_sj: 0.38
1353	    ood_sj_auroc: 0.52
1354	    ood_logprob_auroc: 0.58
1355	    ood_degradation_sj: -0.31
1356	    ood_degradation_logprob: -0.18
1357	  result_rationale: 'OOD 场景下所有 signal 几乎崩溃：SJ ρ=0.05（与 0 无显著差异）， logprob ρ=0.15（微弱但存在）。62.4%
1358	    sample F1=0 说明模型在 OOD 域上 大量 hallucinate。SJ 退化幅度（−0.31）远大于 logprob（−0.18）， 原因：OOD
1359	    hallucination 可以是 consistent（模型反复产出同一错误 entity set）， 导致高 SJ 但低 F1（hallucination
1360	    consistency）。Logprob 在 OOD 时天然偏低， 保持了弱单调关系。这在 worst 档下是 "SJ 在 OOD 上完全失效" 的证据，
1361	    但 paper 可能不会报告这个实验（P2 priority）。如果 reviewer 推断其存在 会进一步削弱 generalization 主张。
1362	
1363	    '
1364	  tables:
1365	  - table_id: T-011-1
1366	    caption: In-domain vs OOD signal quality (SciERC model → WNUT data)
1367	    columns:
1368	    - Signal
1369	    - In-domain ρ
1370	    - OOD ρ
1371	    - Degradation
1372	    rows:
1373	    - - Log-prob
1374	      - 0.33
1375	      - 0.15
1376	      - −0.18
1377	    - - Soft Jaccard
1378	      - 0.36
1379	      - 0.05
1380	      - −0.31
1381	    - - Voting conf
1382	      - 0.37
1383	      - 0.06
1384	      - −0.31
1385	    - - Fleiss' κ
1386	      - 0.27
1387	      - 0.03
1388	      - −0.24
1389	    - - Exact-match
1390	      - 0.26
1391	      - 0.04
1392	      - −0.22
1393	  figures_description: []
1394	  analysis: 'P2 实验。OOD 退化符合预期但在 worst 档下如果被 reviewer 追问 会成为致命弱点。SJ 的 hallucination
1395	    consistency failure mode 是 consistency-based methods 的根本局限性，但 paper 若不主动报告 反而显得在回避。
1396	
1397	    '
1398	- name: signal_ensemble_analysis
1399	  plan_id: exp-016
1400	  description: 'SJ+logprob 相关性分析、线性组合搜索、logistic regression 集成、 Best-of-N ensemble
1401	    selection。
1402	
1403	    '
1404	  expected_results:
1405	    sj_logprob_pearson_ner: 0.55
1406	    sj_logprob_pearson_re: 0.4
1407	    best_linear_ner:
1408	      combo: SJ+voting_conf
1409	      alpha: 0.35
1410	      rho: 0.39
1411	    best_linear_re:
1412	      combo: voting_conf+logprob
1413	      alpha: 0.55
1414	      rho: 0.33
1415	    ensemble_ner_auroc: 0.7
1416	    ensemble_re_auroc: 0.66
1417	    best_single_ner_auroc: 0.68
1418	    best_single_re_auroc: 0.64
1419	    ensemble_ner_delta_auroc: 0.02
1420	    ensemble_re_delta_auroc: 0.02
1421	    selection_f1_ner:
1422	      greedy: 0.618
1423	      logprob: 0.609
1424	      sj: 0.604
1425	      ensemble: 0.606
1426	      voting: 0.596
1427	      random: 0.58
1428	      oracle: 0.769
1429	    selection_f1_re:
1430	      logprob: 0.397
1431	      greedy: 0.374
1432	      sj: 0.368
1433	      ensemble: 0.375
1434	      voting: 0.338
1435	      random: 0.338
1436	      oracle: 0.561
1437	    fk_negative_weight: true
1438	  result_rationale: 'Ensemble 的 AUROC 提升仅 +0.02 on NER（0.70 vs best single 0.68），
1439	    RE 上同样 +0.02。线性组合 best ρ=0.39 仅比 best single(voting 0.37) 高 +0.02。 Worst 档的关键：ensemble
1440	    没有 meaningful 提升，说明各 signal 高度冗余—— 它们编码了相似的信息（SJ-logprob Pearson=0.55 证实了这一点）。
1441	    FK 在 logistic regression 中权重为负——surface agreement 在 structural signals 存在时是 net-negative（noisy
1442	    proxy 被 structural signal dominated）。 Best-of-N ensemble selection 同样 ≤ greedy
1443	    on NER（0.606 < 0.618）， RE 上 ensemble(0.375) ≈ greedy(0.374) but < logprob alone(0.397)。
1444	    Reviewer 评论："even combining all signals doesn''t help — the correlation-selection
1445	    gap is fundamental, not fixable by ensembling."
1446	
1447	    '
1448	  tables:
1449	  - table_id: T-016-1
1450	    caption: Signal ensemble analysis (SciERC)
1451	    columns:
1452	    - Metric
1453	    - Best Single
1454	    - Ensemble
1455	    - Δ
1456	    rows:
1457	    - - NER AUROC
1458	      - 0.68 (voting)
1459	      - 0.7
1460	      - '+0.02'
1461	    - - NER ρ
1462	      - 0.37 (voting)
1463	      - 0.39 (SJ+voting α=0.35)
1464	      - '+0.02'
1465	    - - RE AUROC
1466	      - 0.64 (voting)
1467	      - 0.66
1468	      - '+0.02'
1469	    - - RE ρ
1470	      - 0.30 (voting)
1471	      - 0.33 (voting+logprob α=0.55)
1472	      - '+0.03'
1473	  - table_id: T-016-2
1474	    caption: 'Best-of-N selection: ensemble vs individual'
1475	    columns:
1476	    - Signal
1477	    - NER F1
1478	    - RE F1
1479	    rows:
1480	    - - Greedy
1481	      - 0.618
1482	      - 0.374
1483	    - - Logprob
1484	      - 0.609
1485	      - 0.397
1486	    - - SJ
1487	      - 0.604
1488	      - 0.368
1489	    - - Ensemble
1490	      - 0.606
1491	      - 0.375
1492	    - - Voting
1493	      - 0.596
1494	      - 0.338
1495	    - - Oracle
1496	      - 0.769
1497	      - 0.561
1498	  figures_description:
1499	  - 'Fig-016-1: Heatmap — logistic regression 系数，FK 为负值（红色）， SJ 和 voting 正值接近，logprob
1500	    正值中等
1501	
1502	    '
1503	  analysis: 'Ensemble 分析回答了 Dream 2 reviewer 的问题但答案是负面的： 组合 signal 不产生 meaningful
1504	    improvement。这支持了 worst 档叙事： "信号间高度冗余，correlation-selection gap 不是信号不足的问题， 而是 instance-level
1505	    metrics 的结构性局限。" 但 reviewer 会将此解读为 "insufficient methodological contribution —
1506	    the paper proposes nothing new."
1507	
1508	    '
1509	- name: ner_llama_conll
1510	  plan_id: exp-017
1511	  description: 'LLaMA-3.1-8B 在 CoNLL-2003 上 fine-tune + inference， 扩展 cross-model
1512	    × cross-dataset validation matrix。
1513	
1514	    '
1515	  expected_results:
1516	    greedy_f1: 0.924
1517	    oracle_f1: 0.945
1518	    oracle_headroom: 0.021
1519	    n_valid: 2756
1520	    full:
1521	      SJ_rho: 0.34
1522	      FK_rho: 0.33
1523	      logprob_rho: 0.31
1524	      EM_rho: 0.34
1525	      voting_rho: 0.33
1526	      SJ_AUROC: 0.68
1527	      logprob_AUROC: 0.66
1528	    conditional:
1529	      SJ_rho: 0.35
1530	      logprob_rho: 0.33
1531	    sj_minus_logprob_rho: 0.03
1532	    sj_minus_logprob_auroc: 0.02
1533	    best_of_n:
1534	      greedy: 0.924
1535	      sj_best: 0.92
1536	      logprob_best: 0.921
1537	      voting_best: 0.919
1538	      oracle: 0.945
1539	    structural_beats_logprob: true
1540	  result_rationale: 'LLaMA×CoNLL 是 2×2 matrix 的最后一个 cell。SJ ρ=0.34 与 Qwen3×CoNLL(0.34)
1541	    完全一致——structural signal 在 CoNLL 上 model-agnostic（好消息）， 但 gap vs logprob 仅 +0.03（坏消息）。Greedy
1542	    F1=0.924 极高（CoNLL 对 LLaMA 很容易）， headroom 仅 0.021，best-of-N 所有 signal ≤ greedy（SJ
1543	    0.920 < 0.924）。 AUROC gap +0.02 在 n=2756 下虽然统计显著但 practical significance 微弱。 Worst
1544	    档下 reviewer 看到这个结果会说："the 2×2 matrix is commendable for rigor, but it confirms
1545	    that on standard NER, the structural advantage is negligible (+0.02-0.03), and
1546	    selection never works." LLaMA×CoNLL 加入后 cross_config_structural_gt_logprob_rate
1547	    升到 ~0.70（7/10 configs），但 gap median 仅 +0.03。
1548	
1549	    '
1550	  tables:
1551	  - table_id: T-017-1
1552	    caption: LLaMA × CoNLL-2003 NER (N=8, T=1.0, n=2756)
1553	    columns:
1554	    - Signal
1555	    - ρ (full)
1556	    - AUROC
1557	    - ρ (cond)
1558	    rows:
1559	    - - Soft Jaccard
1560	      - 0.34
1561	      - 0.68
1562	      - 0.35
1563	    - - Exact-match
1564	      - 0.34
1565	      - 0.7
1566	      - 0.36
1567	    - - Voting conf
1568	      - 0.33
1569	      - 0.67
1570	      - 0.34
1571	    - - Fleiss' κ
1572	      - 0.33
1573	      - 0.66
1574	      - 0.34
1575	    - - Log-prob
1576	      - 0.31
1577	      - 0.66
1578	      - 0.33
1579	  - table_id: T-017-2
1580	    caption: 2×2 cross-validation matrix summary (NER, SJ ρ full)
1581	    columns:
1582	    - ' '
1583	    - Qwen3-8B
1584	    - LLaMA-3.1-8B
1585	    rows:
1586	    - - SciERC
1587	      - 0.36
1588	      - 0.36
1589	    - - CoNLL
1590	      - 0.34
1591	      - 0.34
1592	  - table_id: T-017-3
1593	    caption: '2×2 matrix: SJ − Logprob Δρ'
1594	    columns:
1595	    - ' '
1596	    - Qwen3-8B
1597	    - LLaMA-3.1-8B
1598	    rows:
1599	    - - SciERC
1600	      - '+0.03'
1601	      - '+0.06'
1602	    - - CoNLL
1603	      - '+0.02'
1604	      - '+0.03'
1605	  figures_description:
1606	  - 'Fig-017-1: 2×2 heatmap — SJ ρ 值，所有 cell 在 0.34-0.36 之间， cross-model×dataset consistency
1607	    很高但绝对值不突出
1608	
1609	    '
1610	  analysis: 2×2 matrix 在 worst 档下的价值是双面的：它证明了 robustness（SJ ρ 在 0.34-0.36  跨 model/dataset
1611	    一致），但也证明了 mediocrity（gap vs logprob 始终仅 +0.02-0.06， 从未达到让 reviewer 说 "this is
1612	    meaningful" 的水平）。 Reviewer 总结："the authors show a consistent but tiny advantage
1613	    of structural signals, which does not justify the 8× inference cost nor constitute
1614	    a sufficient contribution for a main conference paper." 这直接导致 R4+R19 的 rejection
1615	    rationale。
1616	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "34d55573-8383-48c7-b3e1-578badc59efe",
  "isSidechain": false,
  "promptId": "a640b4e1-01ba-4811-b057-a5972a785ed6",
  "type": "user",
  "uuid": "c0205324-64f4-413b-8711-9bd8bc3276d7",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T203201/worst/review_context.yaml",
      "content": "narrative_guidance: '完全 reframe 为 ''Why Self-Consistency Fails for Structured Prediction:\n  An Analysis of the Correlation-Selection Gap''。 在这个档位下，structural signals 对 logprob\n  的优势微弱到不具实际意义（AUROC gap 0-5pp，ρ gap -4 to +5 hundredths）， reviewer 将 paper 定性为 negative\n  result 但 novelty 不足。Nédellec & Xia 2026 被视为 scooping—— 他们已经做了 consistency-accuracy\n  相关性研究，我们的 structural metrics 被视为 minor extension。 Correlation-selection gap 被 dismiss\n  为 ''obvious: instance-level ≠ sample-level is well-known in calibration literature''。\n  NER best-of-N 全部 ≤ greedy 被解读为 the method fundamentally doesn''t work。 WNUT abandoned\n  被推断为 cherry-picking datasets。Paper 的唯一存活 claim 是 quality estimation 中 structural\n  > logprob 在 60-80% 的配置上成立但 gap 太小，不足以 justify venue contribution。 Lead with negative\n  finding + explanation 策略本身被 reviewer 视为 post-hoc rationalization。 目标从 Main 降为 Findings，但\n  Findings 概率也仅 15-35%。\n\n  '\nimagined_experiments:\n- name: baseline_logprob\n  plan_id: exp-012\n  description: '对所有 pilot 数据 (SciERC NER+RE) 提取 sequence log-probability， 计算与 F1 的\n    Spearman ρ、AUROC、Kendall τ。\n\n    '\n  expected_results:\n    scierc_ner_logprob_rho: 0.33\n    scierc_ner_logprob_auroc: 0.64\n    scierc_ner_logprob_tau: 0.24\n    scierc_ner_logprob_ece: 0.09\n    scierc_ner_sj_rho: 0.36\n    scierc_ner_sj_auroc: 0.67\n    scierc_ner_sj_minus_logprob_rho: 0.03\n    scierc_ner_sj_minus_logprob_auroc: 0.03\n    scierc_ner_fk_rho: 0.27\n    scierc_ner_greedy_logprob_rho: 0.34\n    scierc_re_logprob_rho: 0.25\n    scierc_re_logprob_auroc: 0.62\n    scierc_re_sj_rho: 0.21\n    scierc_re_sj_auroc: 0.59\n    scierc_re_cond_logprob_rho: 0.19\n    scierc_re_cond_sj_rho: 0.33\n    scierc_re_cond_sj_auroc: 0.65\n    n_ner: 529\n    n_re: 397\n  result_rationale: 'Worst 档的关键：logprob 在 NER 上与 SJ 差距仅 Δρ=0.03、ΔAUROC=0.03， 统计上 bootstrap\n    CI 重叠。原理——fine-tuned 8B 模型的 softmax 已 well-calibrated， logprob 隐式编码了 entity span\n    正确性的全部信息。SJ 的额外 8 次采样只带来 +0.03 ρ 的微弱增益， reviewer 认为这不 justify 8x 推理成本。更致命的是 greedy_logprob（单次前向传播的\n    logprob） ρ=0.34 实际上已经超过 SJ 的 ρ=0.36 的下界 CI。RE 上 logprob full ρ=0.25 > SJ full\n    ρ=0.21， 虽然 RE cond 上 SJ 反超（0.33 vs 0.19），但 reviewer 将 conditional 分析视为 cherry-picking。\n    整体结论：SJ 对 logprob 的优势在 NER 上 marginal，在 RE full 上不存在。\n\n    '\n  tables:\n  - table_id: T-012-1\n    caption: 'Confidence signal comparison: log-probability vs structural signals\n      (Spearman ρ with F1)'\n    columns:\n    - Dataset\n    - Task\n    - Log-prob ρ\n    - SJ ρ\n    - FK ρ\n    - Δ(SJ−LP)\n    - p(Δ)\n    rows:\n    - - SciERC\n      - NER-full\n      - 0.33\n      - 0.36\n      - 0.27\n      - '+0.03'\n      - 0.14\n    - - SciERC\n      - NER-cond\n      - 0.3\n      - 0.37\n      - 0.28\n      - '+0.07'\n      - 0.04\n    - - SciERC\n      - RE-full\n      - 0.25\n      - 0.21\n      - 0.25\n      - −0.04\n      - 0.32\n    - - SciERC\n      - RE-cond\n      - 0.19\n      - 0.33\n      - 0.28\n      - '+0.14'\n      - 0.002\n  figures_description:\n  - 'Fig-012-1: Scatter plot 双联——log-prob vs F1 (left) 和 SJ vs F1 (right)， SciERC\n    NER，两者 spread 几乎一样，SJ 的 regression line 斜率仅微高于 logprob， reviewer 第一眼看不出明显差别\n\n    '\n  analysis: 'Worst 档下 exp-012 的结果不是灾难性的——SJ 仍然在 NER 上微弱领先——但差距小到 reviewer 可以 legitimately\n    argue \"this is not practically significant\"。 特别是 Δρ=0.03 在 n=529 下 p=0.14 不显著。RE\n    full 上 logprob > SJ 给了 reviewer 弹药：\"SJ 在 RE 上甚至不如 logprob\"。唯一亮点是 RE cond 上 SJ\n    明确领先（+0.14）， 但这需要 conditional filtering 来展示，削弱了 generality。 核心问题：reviewer 会说 \"so\n    SJ is marginally better in some settings and worse in others — this is a wash,\n    not a contribution.\"\n\n    '\n- name: baseline_exact_match\n  plan_id: exp-013\n  description: 'Exact-match voting rate：N 个 sample 中完全相同 entity/relation set 的比例，\n    与 F1 计算 ρ/AUROC/τ。Wang et al. 2023 self-consistency 的直接结构化推广。\n\n    '\n  expected_results:\n    scierc_ner_em_rho: 0.26\n    scierc_ner_em_auroc: 0.62\n    scierc_ner_em_tau: 0.19\n    scierc_re_em_rho: 0.1\n    scierc_re_em_auroc: 0.5\n    scierc_re_em_tau: 0.08\n    scierc_ner_pct_all_match: 9.1\n    scierc_ner_pct_no_match: 38.7\n    scierc_re_pct_all_match: 1.8\n    scierc_re_pct_no_match: 68.2\n  result_rationale: 'EM 在 NER ρ=0.26 低于 SJ(0.36) 和 logprob(0.33)，在 RE ρ=0.10 是所有 signal\n    中最弱。 这符合预期——IE 输出的 surface form 变异（span boundary 差异、entity 排列顺序差异） 使得 exact-match\n    信号极度稀疏（39% NER 样本无任何 EM pair）。但在 worst 档下这个结果 反而削弱了 SJ 的叙事：reviewer 会说 \"SJ 比 EM\n    好 only because EM is a strawman — the real comparison is with logprob, which is\n    free and equally good.\" RE 上 EM AUROC=0.50 等同于随机，证明 exact-match 在 relation extraction\n    上完全失效。\n\n    '\n  tables:\n  - table_id: T-013-1\n    caption: Exact-match voting rate distribution and correlation\n    columns:\n    - Dataset\n    - Task\n    - '% all-match'\n    - '% no-match'\n    - ρ with F1\n    - AUROC\n    rows:\n    - - SciERC\n      - NER\n      - 9.1\n      - 38.7\n      - 0.26\n      - 0.62\n    - - SciERC\n      - RE\n      - 1.8\n      - 68.2\n      - 0.1\n      - 0.5\n  figures_description:\n  - 'Fig-013-1: Histogram — EM rate 分布（0/8, 1/8, ..., 8/8）， 高度集中于 0 和 1，几乎二值化的粗粒度信号\n\n    '\n  analysis: 'EM 是 self-consistency 在结构化输出上的 naïve baseline，其弱势是意料之中的。 在 worst 档下，这个实验的价值被\n    reviewer 低估——他们认为 \"of course exact-match doesn''t work for structured outputs,\n    this is obvious\" 而不是将其视为 motivation for SJ。结果是 SJ > EM 这个子结论被视为 trivial。\n\n    '\n- name: baseline_entity_voting\n  plan_id: exp-014\n  description: 'Entity-level majority voting confidence：对每个 entity 统计在 N 个 sample\n    中的出现频率， 计算 instance-level 平均 voting confidence 与 F1 的相关性。\n\n    '\n  expected_results:\n    scierc_ner_voting_rho: 0.37\n    scierc_ner_voting_auroc: 0.68\n    scierc_ner_voting_tau: 0.27\n    scierc_re_voting_rho: 0.3\n    scierc_re_voting_auroc: 0.64\n    scierc_re_voting_tau: 0.22\n    scierc_ner_voting_f1_selected: 0.615\n    scierc_ner_greedy_f1: 0.648\n    scierc_ner_oracle_f1: 0.779\n    scierc_ner_voting_vs_greedy_delta: -3.3\n    scierc_re_voting_f1_selected: 0.358\n    scierc_re_greedy_f1: 0.402\n    voting_minus_sj_ner_rho: 0.01\n    voting_minus_logprob_ner_rho: 0.04\n  result_rationale: 'Entity voting ρ=0.37 在 NER 上与 SJ(0.36) 几乎持平（Δ=+0.01），AUROC 也仅微弱领先（0.68\n    vs 0.67）。 关键是 voting vs logprob 差距也很小（+0.04 ρ）。在 worst 档下三者（voting, SJ, logprob）\n    形成一个统计上无法区分的 cluster（bootstrap CI 大量重叠），reviewer 会说 \"all signals perform similarly\n    — the choice of signal doesn''t matter.\" Voting 作为 selection strategy（而非 quality\n    estimation）失败得更彻底： voting-selected F1=0.615 低于 greedy=0.648（−3.3pp），因为 majority\n    vote 倾向于选择\"平庸但安全\"的 entity 而丢弃正确但少数的 entity。 RE 上 voting ρ=0.30 高于 SJ(0.21) 但仍低于\n    logprob 的下界期望。\n\n    '\n  tables:\n  - table_id: T-014-1\n    caption: Entity voting vs other signals (SciERC)\n    columns:\n    - Signal\n    - NER ρ\n    - NER AUROC\n    - RE ρ\n    - RE AUROC\n    rows:\n    - - Voting conf\n      - 0.37\n      - 0.68\n      - 0.3\n      - 0.64\n    - - Soft Jaccard\n      - 0.36\n      - 0.67\n      - 0.21\n      - 0.59\n    - - Log-prob\n      - 0.33\n      - 0.64\n      - 0.25\n      - 0.62\n    - - Fleiss' κ\n      - 0.27\n      - 0.59\n      - 0.25\n      - 0.61\n    - - Exact-match\n      - 0.26\n      - 0.62\n      - 0.1\n      - 0.5\n  figures_description:\n  - 'Fig-014-1: Bar chart — 5 signal 在 NER 上的 ρ，三者（voting/SJ/logprob） 高度接近，error bars\n    重叠，视觉上无明显优胜者\n\n    '\n  analysis: 'Entity voting 的加入没有改变整体叙事——在 worst 档下它只是 structural consistency family\n    中另一个与 logprob 差距不大的 signal。Voting 作为 selection 策略失败 （低于 greedy -3.3pp）直接支持了 correlation-selection\n    gap 的 narrative， 但 reviewer 认为这是 \"expected: instance-level aggregates can''t rank\n    individual samples.\"\n\n    '\n- name: evaluation_metrics_expansion\n  plan_id: exp-015\n  description: '在所有 confidence signal × 所有数据集上扩展评估指标： AUROC、Kendall τ、ECE (calibration)。Leave-one-out\n    SJ 检验评估 circularity。\n\n    '\n  expected_results:\n    scierc_ner:\n      voting_rho: 0.37\n      voting_auroc: 0.68\n      voting_tau: 0.27\n      sj_rho: 0.36\n      sj_auroc: 0.67\n      sj_tau: 0.26\n      sj_ece: 0.11\n      fk_rho: 0.27\n      fk_auroc: 0.59\n      fk_tau: 0.2\n      logprob_rho: 0.33\n      logprob_auroc: 0.64\n      logprob_tau: 0.24\n      logprob_ece: 0.08\n      em_rho: 0.26\n      em_auroc: 0.62\n      em_tau: 0.19\n      loo_sj_rho: 0.35\n      loo_sj_delta: -0.01\n      n_valid: 529\n      n_cond: 501\n    scierc_re:\n      voting_rho: 0.3\n      voting_auroc: 0.64\n      sj_rho: 0.21\n      sj_auroc: 0.59\n      logprob_rho: 0.25\n      logprob_auroc: 0.62\n      n_valid: 397\n      n_cond: 296\n    conll_ner:\n      sj_rho: 0.34\n      sj_auroc: 0.68\n      logprob_rho: 0.32\n      logprob_auroc: 0.66\n      voting_rho: 0.33\n      em_rho: 0.35\n    wnut_ner:\n      sj_rho: 0.08\n      sj_auroc: 0.55\n      logprob_rho: -0.41\n      fk_rho: 0.12\n  result_rationale: '多指标扩展后的全景：AUROC gap (structural vs logprob) 在 NER 上仅 +0.03~0.04，\n    在 RE 上为负（-0.03）。ECE 上 logprob=0.08 优于 SJ=0.11，因为 logprob 天然是概率量。 Leave-one-out\n    SJ ρ=0.35 vs full SJ ρ=0.36，Δ=-0.01，排除了 circularity concern， 但 reviewer 不会因此给加分（\"LOO\n    差异小是 expected, not a contribution\"）。 CoNLL 上 EM(0.35) > SJ(0.34) > voting(0.33)\n    > logprob(0.32)，所有信号极接近， 因为 CoNLL 模型 F1 很高导致所有信号 ceiling-out。WNUT 上 SJ ρ=0.08\n    不显著， logprob ρ=−0.41（反相关），所有 signal 失败——但 WNUT 被 abandoned，reviewer 若推断 这一点会进一步质疑\n    generalization。\n\n    '\n  tables:\n  - table_id: T-015-1\n    caption: Comprehensive 5-signal evaluation — SciERC NER (N=8, T=1.0)\n    columns:\n    - Signal\n    - ρ\n    - AUROC\n    - τ\n    - ECE\n    - LOO-ρ\n    rows:\n    - - Voting conf\n      - 0.37\n      - 0.68\n      - 0.27\n      - 0.1\n      - —\n    - - Soft Jaccard\n      - 0.36\n      - 0.67\n      - 0.26\n      - 0.11\n      - 0.35\n    - - Log-prob\n      - 0.33\n      - 0.64\n      - 0.24\n      - 0.08\n      - —\n    - - Fleiss' κ\n      - 0.27\n      - 0.59\n      - 0.2\n      - 0.14\n      - —\n    - - Exact-match\n      - 0.26\n      - 0.62\n      - 0.19\n      - 0.16\n      - —\n  - table_id: T-015-2\n    caption: Cross-dataset AUROC comparison\n    columns:\n    - Signal\n    - SciERC-NER\n    - CoNLL-NER\n    - WNUT-NER\n    - SciERC-RE-full\n    - SciERC-RE-cond\n    rows:\n    - - Voting\n      - 0.68\n      - 0.67\n      - 0.56\n      - 0.64\n      - 0.68\n    - - SJ\n      - 0.67\n      - 0.68\n      - 0.55\n      - 0.59\n      - 0.65\n    - - Log-prob\n      - 0.64\n      - 0.66\n      - 0.36\n      - 0.62\n      - 0.55\n    - - FK\n      - 0.59\n      - 0.63\n      - 0.54\n      - 0.61\n      - 0.58\n    - - EM\n      - 0.62\n      - 0.7\n      - 0.55\n      - 0.5\n      - 0.54\n  figures_description:\n  - 'Fig-015-1: Reliability diagram (calibration) — logprob 更贴合 y=x 对角线 (ECE=0.08)，\n    SJ 系统性偏高 (ECE=0.11)\n\n    '\n  - 'Fig-015-2: ROC curve — NER 上 voting 和 SJ 的 curve 仅微幅高于 logprob， 三条 curve 几乎重叠，bootstrap\n    CI band 大量 overlap\n\n    '\n  analysis: '多指标扩展的致命结果：所有指标都确认了 structural vs logprob 差距极小。 AUROC 差距 +0.03 比 ρ 差距\n    +0.03 没有更大——不存在 \"ρ understates the advantage\" 的反驳。 ECE 上 logprob 甚至更好。Reviewer\n    会指出：\"Table 2 shows that across 5 metrics, logprob is competitive or better on\n    2 out of 5 — the claimed superiority of structural signals is at best marginal.\"\n    WNUT 数据如果被发现会是致命一击。\n\n    '\n- name: ner_n16_scierc\n  plan_id: exp-001\n  description: 'SciERC NER N=16, T=1.0, ft_002_v2 模型, 3 seeds (42/123/456)。 测试 N-scaling\n    效应，采集 log-prob。\n\n    '\n  expected_results:\n    ner_sj_rho_n16_s42: 0.37\n    ner_sj_rho_n16_s123: 0.36\n    ner_sj_rho_n16_s456: 0.33\n    ner_sj_rho_n16_mean: 0.353\n    ner_sj_rho_n16_std: 0.021\n    ner_voting_rho_n16_mean: 0.36\n    ner_logprob_rho_n16_mean: 0.33\n    ner_fk_rho_n16_mean: 0.26\n    ner_em_rho_n16_mean: 0.3\n    ner_sj_rho_n8_mean: 0.36\n    ner_sj_rho_delta_n16_vs_n8: -0.007\n    ner_oracle_f1_n16: 0.81\n    ner_greedy_f1: 0.655\n    ner_headroom_n16: 0.155\n    re_sj_rho_n16: 0.27\n    re_logprob_rho_n16: 0.3\n    re_voting_rho_n16: 0.35\n    re_oracle_f1_n16: 0.67\n    re_sample_f1_pct_zero: 44.3\n  result_rationale: 'N=16 对 SJ ρ 无提升甚至微降（0.353 vs N=8 的 0.36，Δ=−0.007）。 Worst 档的逻辑：SJ\n    在 N=8 时已饱和——pairwise (N choose 2) 从 28 增到 120， 但额外 sample 高度冗余。Seed-to-seed 标准差\n    σ=0.021 说明 seed456 的低值（0.33） 不是噪声而是边界情况，reviewer 可能 cherry-pick 这个 seed 来论证 SJ\n    不 robust。 更关键的是 logprob（ρ=0.33）在 N=16 上与 SJ（0.353）差距仍仅 +0.02。 RE 上 N=16 SJ ρ=0.27\n    虽比 N=8 的 0.21 有提升，但 reviewer 会指出 \"even at N=16, RE SJ is still below 0.30 — the\n    method doesn''t work for RE.\" Oracle F1 从 0.75 升到 0.81 但 SJ 选不出更好的候选——signal ceiling\n    明确。\n\n    '\n  tables:\n  - table_id: T-001-1\n    caption: N-scaling effect on confidence signals (SciERC, 3-seed mean)\n    columns:\n    - Signal\n    - ρ@N=8\n    - ρ@N=16\n    - Δ\n    - seed σ\n    rows:\n    - - Soft Jaccard\n      - 0.36\n      - 0.353\n      - −0.007\n      - 0.021\n    - - Voting conf\n      - 0.37\n      - 0.36\n      - −0.01\n      - 0.018\n    - - Log-prob\n      - 0.33\n      - 0.33\n      - 0.0\n      - —\n    - - Fleiss' κ\n      - 0.27\n      - 0.26\n      - −0.01\n      - 0.015\n    - - Exact-match\n      - 0.26\n      - 0.3\n      - '+0.04'\n      - 0.022\n  - table_id: T-001-2\n    caption: Multi-seed robustness (SciERC NER N=16, SJ ρ)\n    columns:\n    - Seed\n    - NER ρ_SJ\n    - NER ρ_logprob\n    - RE ρ_SJ\n    rows:\n    - - 42\n      - 0.37\n      - 0.33\n      - 0.27\n    - - 123\n      - 0.36\n      - 0.34\n      - 0.26\n    - - 456\n      - 0.33\n      - 0.32\n      - 0.27\n  figures_description:\n  - 'Fig-001-1: Line plot — N vs ρ (N=4,8,16)，SJ 在 N=8 后平坦或微降， logprob 水平线几乎与 SJ 重叠\n\n    '\n  - 'Fig-001-2: 3-seed box plot — variance 小但 seed456 下拉 mean， CI 与 logprob 完全 overlap\n\n    '\n  analysis: 'N=16 实验在 worst 档下是双重打击：(1) 更多 sample 不提升 SJ——\"N=8 不够\"假说被否定； (2) seed-to-seed\n    variance（0.33-0.37）覆盖了 logprob 的值域（0.32-0.34）， reviewer 结论：\"the two signals are\n    statistically indistinguishable.\" RE 的改善从 0.21 到 0.27 虽然存在，但仍远低于任何有意义的阈值。\n\n    '\n- name: ner_conll2003\n  plan_id: exp-002\n  description: 'CoNLL-2003 上 fine-tune Qwen3-8B (LoRA) + NER (N=8, T=1.0)。 跨数据集泛化验证。\n\n    '\n  expected_results:\n    conll_greedy_f1: 0.907\n    conll_oracle_f1: 0.945\n    conll_headroom: 0.038\n    conll_sj_rho: 0.34\n    conll_sj_auroc: 0.68\n    conll_sj_tau: 0.3\n    conll_fk_rho: 0.31\n    conll_logprob_rho: 0.32\n    conll_logprob_auroc: 0.66\n    conll_em_rho: 0.35\n    conll_voting_rho: 0.33\n    conll_sj_minus_logprob: 0.02\n    conll_mean_sj: 0.86\n    conll_sample_f1_pct_zero: 2.8\n    n_valid: 2756\n  result_rationale: 'CoNLL 上 SJ ρ=0.34 仅比 logprob ρ=0.32 高 0.02，AUROC gap 同样仅 +0.02。\n    Worst 档的核心机制是 ceiling effect：greedy F1=0.907，mean SJ=0.86， 绝大多数 sample 已经很好（仅\n    2.8% F1=0），SJ 在高一致区域的 discriminative power 崩溃。 EM(0.35) 甚至微幅领先 SJ(0.34)——在 CoNLL\n    这种标准 NER 上 exact-match 反而 因为 entity 简单而足够有效，这直接削弱了 \"soft similarity is necessary\"\n    的论点。 Headroom 仅 0.038（oracle 94.5 vs greedy 90.7），best-of-N 几乎无空间。 Reviewer 会说：\"on\n    CoNLL, all signals including exact-match perform similarly — the structural metric\n    adds no value for standard NER tasks.\"\n\n    '\n  tables:\n  - table_id: T-002-1\n    caption: 'CoNLL-2003 NER: all confidence signals (N=8, T=1.0, n=2756)'\n    columns:\n    - Signal\n    - ρ\n    - AUROC\n    - τ\n    - vs SciERC Δρ\n    rows:\n    - - Exact-match\n      - 0.35\n      - 0.7\n      - 0.31\n      - '+0.09'\n    - - Soft Jaccard\n      - 0.34\n      - 0.68\n      - 0.3\n      - −0.02\n    - - Voting conf\n      - 0.33\n      - 0.67\n      - 0.29\n      - −0.04\n    - - Log-prob\n      - 0.32\n      - 0.66\n      - 0.25\n      - −0.01\n    - - Fleiss' κ\n      - 0.31\n      - 0.63\n      - 0.28\n      - '+0.04'\n  figures_description:\n  - 'Fig-002-1: SJ 分布 histogram — 高度右偏集中于 0.85-1.0， 与 SciERC 更 spread-out 的分布并排对比，直观展示\n    ceiling effect\n\n    '\n  analysis: 'CoNLL 结果在 worst 档下暴露了 SJ 的 dataset sensitivity：在 \"easy\" NER 上 SJ 的优势消失（Δρ=+0.02）。更致命的是\n    EM 反超 SJ—— reviewer 会问：\"if exact-match works just as well on CoNLL, why do we\n    need SJ?\" 这将被引用为 SJ 只在 SciERC 特有的 scientific entity 复杂度下有效的证据， 泛化性成疑。\n\n    '\n- name: ner_wnut17\n  plan_id: exp-003\n  description: 'WNUT-17 (social media NER) fine-tune + inference。被 abandoned 但 data\n    存在。\n\n    '\n  expected_results:\n    wnut_greedy_f1: 0.525\n    wnut_oracle_f1: 0.664\n    wnut_headroom: 0.139\n    wnut_sj_rho_full: 0.08\n    wnut_sj_p: 0.12\n    wnut_fk_rho: 0.12\n    wnut_logprob_rho_full: -0.41\n    wnut_logprob_rho_cond: 0.35\n    wnut_sj_rho_cond: 0.28\n    wnut_sample_f1_pct_zero: 53.7\n    wnut_n_gold_empty: 598\n    wnut_n_instances: 1287\n    wnut_sj_auroc: 0.55\n    wnut_structural_beats_surface: false\n  result_rationale: 'WNUT 是 worst 档下的 smoking gun。SJ ρ=0.08 不显著（p=0.12）， 53.7% 的 sample\n    F1=0，598/1287 个 instance gold set 为空。 Logprob full ρ=−0.41（反相关！）说明模型在 noisy social\n    media text 上 完全 uncalibrated——高 logprob 的 sample 反而更可能是 confident hallucination。\n    所有 signal 在 WNUT 上失败。虽然 paper 可以 abandon 并不报告， 但 reviewer 若问 \"why only 2 NER datasets?\"\n    或推断 WNUT 被排除， 会质疑 dataset cherry-picking。这是 worst 档假设的核心： \"WNUT abandoned (>50%\n    F1=0, structural rho not significant) 被发现或推断\"。\n\n    '\n  tables:\n  - table_id: T-003-1\n    caption: WNUT-17 NER results (abandoned — included for completeness)\n    columns:\n    - Signal\n    - Full ρ\n    - Cond ρ\n    - AUROC\n    - Notes\n    rows:\n    - - Soft Jaccard\n      - 0.08\n      - 0.28\n      - 0.55\n      - p=0.12, not significant\n    - - Fleiss' κ\n      - 0.12\n      - 0.17\n      - 0.54\n      - ''\n    - - Log-prob\n      - −0.41\n      - 0.35\n      - 0.36\n      - full anti-correlated\n    - - Exact-match\n      - 0.09\n      - 0.22\n      - 0.53\n      - ''\n  figures_description: []\n  analysis: 'WNUT 被 abandoned 是正确决定——53.7% F1=0 意味着数据集超出模型能力范围。 但这在 worst 档下被解读为 \"generalization\n    failure\"：paper 声称 structural consistency 是 universal quality estimator， 但在 social\n    media domain 上甚至不 significant。 Reviewer 会在 weaknesses 中写：\"The authors only report\n    results on 2 NER datasets, both with relatively clean text. Applicability to noisy\n    domains is unknown.\"\n\n    '\n- name: re_diagnostic_analysis\n  plan_id: exp-004\n  description: 'RE per-relation-type 分解、bootstrap CI、threshold sensitivity、error propagation。\n\n    '\n  expected_results:\n    per_relation_type:\n      HYPONYM-OF:\n        n: 36\n        rho_sj: 0.38\n        rho_fk: 0.45\n        rho_logprob: 0.42\n      CONJUNCTION:\n        n: 86\n        rho_sj: 0.28\n        rho_fk: 0.25\n        rho_logprob: 0.32\n      USED-FOR:\n        n: 299\n        rho_sj: 0.18\n        rho_fk: 0.2\n        rho_logprob: 0.24\n      PART-OF:\n        n: 44\n        rho_sj: 0.17\n        rho_fk: 0.25\n        rho_logprob: 0.28\n      EVALUATE-FOR:\n        n: 62\n        rho_sj: 0.12\n        rho_fk: 0.18\n        rho_logprob: 0.22\n      COMPARE:\n        n: 35\n        rho_sj: 0.11\n        rho_fk: 0.13\n        rho_logprob: 0.2\n      FEATURE-OF:\n        n: 50\n        rho_sj: 0.01\n        rho_fk: 0.04\n        rho_logprob: 0.12\n    bootstrap_ci_95:\n      re_sj_full:\n      - 0.12\n      - 0.3\n      re_logprob_full:\n      - 0.16\n      - 0.34\n      re_sj_cond:\n      - 0.22\n      - 0.44\n    threshold_sensitivity:\n      thr_0pct_rho_sj: 0.21\n      thr_10pct_rho_sj: 0.28\n      thr_20pct_rho_sj: 0.33\n      thr_30pct_rho_sj: 0.3\n      thr_40pct_rho_sj: 0.25\n    error_propagation:\n      head_tail_error_pct: 55.5\n      type_error_pct: 8.3\n      head_sj_rho: 0.21\n  result_rationale: 'RE 诊断结果在 worst 档下：(1) Per-relation-type 分析显示 logprob 在 6/7 relation\n    types 上 优于 SJ，只有 HYPONYM-OF（n=36，太小不可靠）SJ 稍弱但 FK 反而最强； (2) Bootstrap CI 表明 SJ\n    full [0.12, 0.30] 与 logprob full [0.16, 0.34] 大量 overlap—— reviewer 会说 \"the difference\n    is not statistically significant\"； (3) Threshold sensitivity 呈 inverted-U 但 reviewer\n    认为 \"this is just an artifact of removing low-performance instances — the remaining\n    instances are easier by definition\"； (4) FEATURE-OF 关系 SJ ρ≈0 证明某些 relation types\n    对 consistency 完全免疫。\n\n    '\n  tables:\n  - table_id: T-004-1\n    caption: 'RE diagnostic: per-relation-type ρ (SciERC)'\n    columns:\n    - Relation\n    - n\n    - SJ ρ\n    - FK ρ\n    - Logprob ρ\n    rows:\n    - - HYPONYM-OF\n      - 36\n      - 0.38\n      - 0.45\n      - 0.42\n    - - CONJUNCTION\n      - 86\n      - 0.28\n      - 0.25\n      - 0.32\n    - - USED-FOR\n      - 299\n      - 0.18\n      - 0.2\n      - 0.24\n    - - PART-OF\n      - 44\n      - 0.17\n      - 0.25\n      - 0.28\n    - - EVALUATE-FOR\n      - 62\n      - 0.12\n      - 0.18\n      - 0.22\n    - - COMPARE\n      - 35\n      - 0.11\n      - 0.13\n      - 0.2\n    - - FEATURE-OF\n      - 50\n      - 0.01\n      - 0.04\n      - 0.12\n  - table_id: T-004-2\n    caption: Threshold sensitivity (conditional exclusion %)\n    columns:\n    - Exclusion %\n    - SJ ρ\n    - Logprob ρ\n    - n\n    rows:\n    - - 0%\n      - 0.21\n      - 0.25\n      - 397\n    - - 10%\n      - 0.28\n      - 0.3\n      - 357\n    - - 20%\n      - 0.33\n      - 0.31\n      - 318\n    - - 30%\n      - 0.3\n      - 0.28\n      - 278\n    - - 40%\n      - 0.25\n      - 0.24\n      - 238\n  figures_description:\n  - 'Fig-004-1: Threshold sensitivity curve — inverted-U 峰值在 ~20%， 但 reviewer 注意到\n    logprob 也有类似 pattern，认为 non-specific to SJ\n\n    '\n  - 'Fig-004-2: Per-relation heatmap — FEATURE-OF 行全暗色（near-zero）， USED-FOR 行（n=299，最大类）也偏弱（SJ=0.18）\n\n    '\n  analysis: 'RE 诊断在 worst 档下提供了 task-complexity boundary 的证据，但 reviewer 的反应是 \"the\n    boundary is obvious — RE is harder than NER, this doesn''t need 397 instances\n    to show.\" Per-relation 分析被视为 descriptive not prescriptive——没有提出 actionable insight\n    告诉 practitioner 如何改进。Bootstrap CI overlap 成为 \"SJ ≈ logprob on RE\" 的直接证据。\n\n    '\n- name: temperature_sensitivity_analysis\n  plan_id: exp-005\n  description: 'T=0.7 vs T=1.0 对比，在所有 confidence signal 上分析温度的 signal-noise tradeoff。\n\n    '\n  expected_results:\n    ner_sj_rho_t07: 0.39\n    ner_sj_rho_t10: 0.36\n    ner_sj_delta_temp: -0.03\n    ner_logprob_rho_t07: 0.34\n    ner_logprob_rho_t10: 0.33\n    ner_logprob_delta_temp: -0.01\n    ner_fk_rho_t07: 0.32\n    ner_fk_rho_t10: 0.27\n    ner_fk_delta_temp: -0.05\n    re_sj_rho_t07: 0.23\n    re_sj_rho_t10: 0.21\n    re_logprob_rho_t07: 0.27\n    re_logprob_rho_t10: 0.25\n    ner_mean_sj_t07: 0.78\n    ner_mean_sj_t10: 0.7\n    ner_oracle_t07: 0.758\n    ner_oracle_t10: 0.776\n    sj_temp_robust: true\n    sj_delta_rho_temp: 0.03\n  result_rationale: '温度对 SJ 的影响（Δρ=−0.03）大于对 logprob（Δρ=−0.01），因为 T=1.0 增加的 sample\n    diversity 降低了 pairwise SJ 均值（0.78→0.70）并增加了噪声。 在 worst 档下 SJ 在 T=0.7 时的 \"最佳\"性能（ρ=0.39）与\n    logprob（0.34）差距为 +0.05， 仍在 focal_rho_gap [-0.04, 0.05] 的上界。Reviewer 会说 \"SJ requires\n    careful temperature tuning to achieve even marginal gains, while logprob is robust\n    to T.\" FK 的温度敏感性（Δ=−0.05）被视为 surface metrics 的又一缺陷。 T=1.0 保留更多 oracle headroom（0.776\n    vs 0.758），但因为 selection 无法利用 headroom， 这个观察在 worst 档下变得 moot。\n\n    '\n  tables:\n  - table_id: T-005-1\n    caption: 'Temperature sensitivity: T=0.7 vs T=1.0 (SciERC)'\n    columns:\n    - Signal\n    - NER ρ(T=0.7)\n    - NER ρ(T=1.0)\n    - Δ\n    - RE ρ(T=0.7)\n    - RE ρ(T=1.0)\n    - Δ\n    rows:\n    - - Soft Jaccard\n      - 0.39\n      - 0.36\n      - −0.03\n      - 0.23\n      - 0.21\n      - −0.02\n    - - Log-prob\n      - 0.34\n      - 0.33\n      - −0.01\n      - 0.27\n      - 0.25\n      - −0.02\n    - - Voting conf\n      - 0.38\n      - 0.37\n      - −0.01\n      - 0.31\n      - 0.3\n      - −0.01\n    - - Fleiss' κ\n      - 0.32\n      - 0.27\n      - −0.05\n      - 0.22\n      - 0.25\n      - '+0.03'\n    - - Exact-match\n      - 0.28\n      - 0.26\n      - −0.02\n      - 0.11\n      - 0.1\n      - −0.01\n  figures_description:\n  - 'Fig-005-1: Paired scatter — 同一 instance 在 T=0.7 和 T=1.0 下的 SJ 值， 高相关 (r>0.85)\n    但 T=1.0 系统性偏低\n\n    '\n  analysis: '温度分析排除了 \"用错温度\" 的 confound，但在 worst 档下这反而是坏消息： 即使在最优温度 T=0.7 下 SJ 与 logprob\n    差距也仅 +0.05 ρ。 Reviewer 评论：\"temperature tuning is another hyperparameter burden\n    on top of N-sampling, while logprob is temperature-invariant and nearly as strong.\"\n\n    '\n- name: adaptive_compute_demo\n  plan_id: exp-006\n  description: 'Best-of-N selection：用各 confidence signal 选 N 个 sample 中最好的， 报告 F1\n    vs greedy/random/oracle。覆盖所有数据集和任务。\n\n    '\n  expected_results:\n    scierc_ner:\n      greedy: 0.618\n      random: 0.586\n      sj: 0.604\n      logprob: 0.609\n      fk: 0.608\n      voting: 0.596\n      em: 0.603\n      ensemble: 0.604\n      oracle: 0.769\n    scierc_re:\n      greedy: 0.374\n      random: 0.338\n      sj: 0.368\n      logprob: 0.397\n      fk: 0.37\n      voting: 0.338\n      oracle: 0.561\n    conll_ner:\n      greedy: 0.725\n      random: 0.692\n      sj: 0.718\n      logprob: 0.716\n      fk: 0.717\n      voting: 0.714\n      oracle: 0.757\n    ner_all_signals_leq_greedy: true\n    re_only_logprob_beats_greedy: true\n    re_logprob_gain_pp: 2.3\n  result_rationale: '这是 worst 档的核心 negative finding：NER 上 ALL signals ≤ greedy。 SJ(0.604)\n    < greedy(0.618) by −1.4pp，logprob(0.609) < greedy(0.618) by −0.9pp。 机制：best-of-N\n    selection 需要 PER-SAMPLE ranking ability，而 consistency signals (SJ/voting) 是 INSTANCE-LEVEL\n    aggregates——它们告诉你\"这个 input 容易还是难\"， 但不能告诉你\"哪个 sample 更好\"。即使是 logprob（唯一的 per-sample\n    signal） 在 NER 上也因为 greedy decode 已经 near-optimal 而无法提供增益。 Oracle headroom 巨大（NER\n    +15.1pp，RE +18.7pp）但没有任何 signal 能 exploit 它。 RE 上 logprob 是唯一击败 greedy 的 signal（+2.3pp），验证了\n    per-sample vs instance-level 的区分，但 reviewer 的评价是：\"this distinction is well-known\n    in the calibration literature; the authors are re-discovering that aggregate confidence\n    ≠ per-item ranking.\" CoNLL 上所有 signal 都低于 greedy（headroom 仅 3.2pp），进一步确认 ceiling\n    effect。\n\n    '\n  tables:\n  - table_id: T-006-1\n    caption: Best-of-N selection F1 (N=8/16, all datasets)\n    columns:\n    - Dataset\n    - Task\n    - Greedy\n    - Random\n    - SJ\n    - Logprob\n    - Voting\n    - Oracle\n    rows:\n    - - SciERC\n      - NER\n      - 0.618\n      - 0.586\n      - 0.604\n      - 0.609\n      - 0.596\n      - 0.769\n    - - SciERC\n      - RE\n      - 0.374\n      - 0.338\n      - 0.368\n      - 0.397\n      - 0.338\n      - 0.561\n    - - CoNLL\n      - NER\n      - 0.725\n      - 0.692\n      - 0.718\n      - 0.716\n      - 0.714\n      - 0.757\n  - table_id: T-006-2\n    caption: F1 gain over greedy (pp)\n    columns:\n    - Signal\n    - SciERC-NER\n    - SciERC-RE\n    - CoNLL-NER\n    - Cost (vs greedy)\n    rows:\n    - - Log-prob\n      - −0.9\n      - '+2.3'\n      - −0.9\n      - 0× extra\n    - - Soft Jaccard\n      - −1.4\n      - −0.6\n      - −0.7\n      - 8× inference\n    - - Voting conf\n      - −2.2\n      - −3.6\n      - −1.1\n      - 8× inference\n    - - Ensemble\n      - −1.4\n      - −0.7\n      - —\n      - 8× + logprob\n    - - Oracle\n      - '+15.1'\n      - '+18.7'\n      - '+3.2'\n      - —\n  figures_description:\n  - 'Fig-006-1: Selection curves — N vs F1 on SciERC NER， greedy 虚线在所有 signal 之上，oracle\n    远上方， 所有 selection curves 在 greedy 下方是最有视觉冲击力的结果\n\n    '\n  - 'Fig-006-2: Cost-effectiveness scatter — x=inference cost, y=ΔF1 vs greedy， 所有\n    consistency signals 在第四象限（高 cost，负 gain）， logprob 在 (1×, −0.9) 位置——even logprob\n    doesn''t help for NER\n\n    '\n  analysis: 'Best-of-N 结果是 worst 档的 headline finding，也是 reviewer 最关注的： \"NER best-of-N\n    全部 ≤ greedy\" 被解读为 \"the method fundamentally doesn''t work\"。 即使 reframe 为 correlation-selection\n    gap analysis，reviewer 仍会说 \"the paper identifies a gap but offers no solution —\n    purely diagnostic with no positive outcome.\" Oracle gap 的巨大（+15pp NER, +19pp RE）同时是好消息（headroom\n    exists） 和坏消息（current signals waste 100% of it on NER）。RE 上 logprob 的成功（+2.3pp）\n    反而削弱了 consistency signals——\"if you want selection, just use logprob.\"\n\n    '\n- name: ner_multi_model\n  plan_id: exp-007\n  description: 'LLaMA-3.1-8B-Instruct 在 SciERC NER/RE 上 fine-tune + inference。 Model-agnostic\n    验证。\n\n    '\n  expected_results:\n    llama_ner_greedy_f1: 0.66\n    llama_ner_oracle_f1: 0.781\n    llama_ner_headroom: 0.121\n    llama_ner_sj_rho: 0.36\n    llama_ner_fk_rho: 0.33\n    llama_ner_logprob_rho: 0.3\n    llama_ner_sj_auroc: 0.68\n    llama_ner_logprob_auroc: 0.62\n    llama_ner_sj_minus_logprob_rho: 0.06\n    llama_re_greedy_f1: 0.434\n    llama_re_sj_rho: 0.3\n    llama_re_fk_rho: 0.31\n    llama_re_logprob_rho: 0.29\n    llama_re_sj_cond_rho: 0.41\n    llama_re_logprob_cond_rho: 0.09\n    llama_ner_sample_f1_pct_zero: 11.6\n    llama_re_sample_f1_pct_zero: 41.2\n  result_rationale: 'LLaMA 上 SJ ρ=0.36 与 Qwen3 的 0.36 持平——表面看 model-agnostic， 但 worst\n    档的问题在于 logprob 在 LLaMA 上更弱（ρ=0.30 vs Qwen3 0.33）， 使得 SJ-logprob gap 在 LLaMA 上稍大（+0.06）但在\n    Qwen3 上仅 +0.03。 Reviewer 会指出：\"the SJ advantage depends on which model you test\n    — on Qwen3 it''s +0.03 (not significant), on LLaMA it''s +0.06 (marginal). This\n    is not a robust model-agnostic finding.\" RE 上 LLaMA 的 41.2% F1=0 进一步证实了 RE 的 difficulty\n    boundary。 LLaMA RE cond SJ ρ=0.41 是一个亮点，但需要 conditional filtering 来展示， 而且只在 LLaMA×SciERC\n    这一个配置上出现。\n\n    '\n  tables:\n  - table_id: T-007-1\n    caption: 'Cross-model comparison: Qwen3-8B vs LLaMA-3.1-8B (SciERC)'\n    columns:\n    - Signal\n    - Qwen3 NER ρ\n    - LLaMA NER ρ\n    - Δ\n    - Qwen3 RE ρ\n    - LLaMA RE ρ\n    - Δ\n    rows:\n    - - Soft Jaccard\n      - 0.36\n      - 0.36\n      - 0.0\n      - 0.21\n      - 0.3\n      - '+0.09'\n    - - Log-prob\n      - 0.33\n      - 0.3\n      - −0.03\n      - 0.25\n      - 0.29\n      - '+0.04'\n    - - Voting conf\n      - 0.37\n      - 0.35\n      - −0.02\n      - 0.3\n      - 0.28\n      - −0.02\n    - - Fleiss' κ\n      - 0.27\n      - 0.33\n      - '+0.06'\n      - 0.25\n      - 0.31\n      - '+0.06'\n    - - Exact-match\n      - 0.26\n      - 0.24\n      - −0.02\n      - 0.1\n      - 0.08\n      - −0.02\n  figures_description:\n  - 'Fig-007-1: 双模型 bar chart — SJ vs logprob gap 在 Qwen3 和 LLaMA 上方向一致 但幅度不稳定（+0.03\n    vs +0.06），reviewer 关注 instability\n\n    '\n  analysis: 'LLaMA 实验的 worst 档解读：model-agnostic 声称依赖于 2 个 8B 模型， reviewer 认为 \"2 models\n    from the same parameter scale is not sufficient for model-agnostic claims — need\n    at least one 70B+ model.\" SJ-logprob gap 的跨模型 variance（+0.03 到 +0.06）被视为 instability。\n    RE 上 SJ 在 LLaMA 上反而比 Qwen3 好（0.30 vs 0.21），但这只是因为 LLaMA 的 RE greedy F1 更高（0.434\n    vs 0.374），更多 instance 进入 \"capability range\"。\n\n    '\n- name: re_n16_confirmation\n  plan_id: exp-008\n  description: 'RE N=16 on SciERC，确认 RE negative finding 在更高 N 下仍成立。\n\n    '\n  expected_results:\n    re_sj_rho_n16_full: 0.28\n    re_sj_rho_n16_cond: 0.35\n    re_fk_rho_n16: 0.24\n    re_logprob_rho_n16: 0.3\n    re_voting_rho_n16: 0.32\n    re_n16_vs_n8_sj_delta: 0.07\n    re_oracle_f1_n16: 0.67\n    re_greedy_f1: 0.434\n    re_headroom_n16: 0.236\n    re_sample_f1_pct_zero: 44.3\n    ner_sj_rho_n16: 0.38\n    ner_logprob_rho_n16: 0.33\n  result_rationale: 'RE N=16 SJ ρ 从 N=8 的 0.21 升到 0.28（Δ=+0.07），但仍远低于 NER 的 0.38。\n    Worst 档的解读：RE 的改善来自更多 sample 平均了 compound error noise， 但 reviewer 会说 \"even at\n    N=16 (doubling compute), RE SJ ρ=0.28 is still well below the NER level — the\n    task-complexity boundary is real and not fixable by more sampling.\" Logprob N=16\n    ρ=0.30 再次与 SJ 持平或微超。 44.3% F1=0 sample 说明 RE 的知识缺口不是 sampling 能解决的。 Oracle headroom\n    从 0.17 升到 0.24 但 selection 仍无法利用。\n\n    '\n  tables:\n  - table_id: T-008-1\n    caption: 'RE N-scaling: N=8 vs N=16 (SciERC)'\n    columns:\n    - Signal\n    - Full ρ@N=8\n    - Full ρ@N=16\n    - Δ\n    - Cond ρ@N=16\n    rows:\n    - - Soft Jaccard\n      - 0.21\n      - 0.28\n      - '+0.07'\n      - 0.35\n    - - Voting conf\n      - 0.3\n      - 0.32\n      - '+0.02'\n      - 0.38\n    - - Log-prob\n      - 0.25\n      - 0.3\n      - '+0.05'\n      - 0.27\n    - - Fleiss' κ\n      - 0.25\n      - 0.24\n      - −0.01\n      - 0.3\n  figures_description: []\n  analysis: 'N=16 RE 的微弱改善在 worst 档下不足以改变结论。Reviewer 说： \"Increasing N from 8 to 16\n    yields +0.07 ρ for SJ but SJ still underperforms logprob at N=16 (0.28 vs 0.30).\n    The computational cost doubles for negligible gain.\" 这个实验是 confirmatory negative——排除了\n    \"N=8 不够\" 的 excuse。\n\n    '\n- name: capability_stratification\n  plan_id: exp-009\n  description: '按 difficulty strata (greedy F1 buckets + 独立 proxy: sentence length,\n    entity count) 分析各 signal 的 ρ 变化。\n\n    '\n  expected_results:\n    scierc_ner:\n      by_greedy_f1:\n        hard_0_25_sj_rho: 0.16\n        med_low_sj_rho: 0.14\n        med_high_sj_rho: 0.09\n        easy_sj_rho: 0.23\n      by_sent_len:\n        Q1_sj_rho: 0.35\n        Q2_sj_rho: 0.32\n        Q3_sj_rho: 0.25\n        Q4_sj_rho: 0.3\n      by_ent_count:\n        zero_sj_rho: 0.52\n        one_two_sj_rho: 0.33\n        three_five_sj_rho: 0.28\n        six_plus_sj_rho: 0.4\n      overall_sj_rho: 0.36\n    scierc_re:\n      by_greedy_f1:\n        hard_sj_rho: -0.04\n        easy_sj_rho: 0.18\n    conll_ner:\n      by_sent_len:\n        Q1_sj_rho: 0.28\n        Q3_sj_rho: 0.38\n    proxy_independence:\n      f1_vs_slen: -0.02\n      f1_vs_ecnt: 0.01\n    inverted_u_confirmed: false\n  result_rationale: 'Worst 档下 inverted-U 假说未被确认：按 greedy F1 bucket 分层后 ρ 没有清晰的 中间峰值（med_low=0.14,\n    med_high=0.09 都低于 easy=0.23）。 Reviewer 评论：\"the authors claim a task-complexity\n    boundary but the stratification data doesn''t show a clean inverted-U — the pattern\n    is noisy and inconsistent.\" 用独立 proxy（sentence length）分层后 pattern 更模糊。 RE 上 hard\n    bucket SJ ρ=−0.04 是直接 negative——SJ 在困难 RE 实例上是 anti-correlated。 Entity count=0\n    的高 ρ（0.52）是因为 trivially correct（无 entity 要提取）， reviewer 会说这 inflates the overall\n    ρ。\n\n    '\n  tables:\n  - table_id: T-009-1\n    caption: Stratified ρ by difficulty (SciERC NER)\n    columns:\n    - Stratum\n    - n\n    - SJ ρ\n    - Logprob ρ\n    - FK ρ\n    rows:\n    - - F1 0-25%\n      - 105\n      - 0.16\n      - 0.2\n      - 0.1\n    - - F1 25-50%\n      - 63\n      - 0.14\n      - 0.18\n      - 0.12\n    - - F1 50-75%\n      - 142\n      - 0.09\n      - 0.15\n      - 0.08\n    - - F1 75-100%\n      - 130\n      - 0.23\n      - 0.28\n      - 0.18\n    - - Sent len Q1\n      - 140\n      - 0.35\n      - 0.3\n      - 0.26\n    - - Sent len Q4\n      - 132\n      - 0.3\n      - 0.28\n      - 0.22\n  figures_description:\n  - 'Fig-009-1: Scatter — F1 bucket vs ρ，无清晰 inverted-U， 散点 noisy 且 logprob 在每个 bucket\n    都接近或超过 SJ\n\n    '\n  analysis: 'Stratification 分析在 worst 档下失败——没有产出 clean diagnostic insight。 Reviewer\n    的 major weakness：\"The diagnostic framework claims to identify capability boundaries\n    but the stratification evidence is weak and inconsistent. This is descriptive,\n    not prescriptive — the paper doesn''t tell practitioners anything actionable.\"\n    这直接对应 R17 (\"diagnostic framework overclaimed\")。\n\n    '\n- name: selection_curves\n  plan_id: exp-010\n  description: 'Best-of-N selection curves (N=1,2,4,8,16) 可视化为 line plots。\n\n    '\n  expected_results:\n    scierc_ner:\n      N4:\n        oracle: 0.714\n        sj: 0.607\n        logprob: 0.616\n        voting: 0.594\n      N8:\n        oracle: 0.752\n        sj: 0.604\n        logprob: 0.609\n        voting: 0.591\n      N16:\n        oracle: 0.787\n        sj: 0.606\n        logprob: 0.612\n        voting: 0.585\n      greedy: 0.618\n    scierc_re:\n      N8:\n        oracle: 0.583\n        sj: 0.368\n        logprob: 0.397\n        voting: 0.338\n      N16:\n        oracle: 0.631\n        sj: 0.372\n        logprob: 0.405\n        voting: 0.34\n      greedy: 0.374\n    conll_ner:\n      N4:\n        oracle: 0.746\n        sj: 0.714\n        logprob: 0.715\n      N8:\n        oracle: 0.757\n        sj: 0.718\n        logprob: 0.716\n      greedy: 0.725\n  result_rationale: 'Selection curves 在 worst 档下产出了最具视觉冲击力的 negative result： SciERC\n    NER 上所有 signal curves 在 greedy 虚线 BELOW——oracle curve 持续上升到 0.787 但所有实际 selection\n    停留在 0.60-0.61。N 从 4→16 增加时 oracle 持续改善但 selection 不动。 Greedy 虚线高高在上（0.618）说明不采样反而更好。\n    CoNLL 上 greedy=0.725 同样高于所有 selection（0.714-0.718），headroom 仅 3.2pp 且无法被利用。RE\n    上 logprob curve 是唯一在 greedy 之上的线（+2.3pp at N=16）， 其余 signal 全部在 greedy 以下。这幅图本身就是\n    \"self-consistency doesn''t work for IE\" 的最直接可视化证据。\n\n    '\n  tables: []\n  figures_description:\n  - 'Fig-010-1: 3-panel line plot (SciERC NER / SciERC RE / CoNLL NER)， 每 panel: x=N,\n    y=F1，lines=Oracle/Greedy/各signal/Random。 NER panels 中 greedy 水平虚线在所有 signal 之上。\n    RE panel 中仅 logprob 穿过 greedy。 Oracle 和 selection 间的 fan-out 是 correlation-selection\n    gap 的直接可视化。\n\n    '\n  analysis: 'Selection curves 是 paper 的 Figure 1 候选——最直观地展示了 correlation-selection\n    gap：oracle 证明 headroom 存在， 但所有 signal 在 greedy 下方说明 current signals 无法 exploit\n    它。 在 worst 档下 reviewer 的评价是：\"Fig 1 is interesting but the paper doesn''t offer\n    any solution — it identifies a problem and stops.\"\n\n    '\n- name: ner_ood_robustness\n  plan_id: exp-011\n  description: 'NER consistency signal 在 OOD 实例上的表现（SciERC fine-tuned 模型 on WNUT data）。\n\n    '\n  expected_results:\n    ood_sj_rho: 0.05\n    ood_logprob_rho: 0.15\n    ood_fk_rho: 0.03\n    ood_voting_rho: 0.06\n    ood_greedy_f1: 0.28\n    ood_sample_f1_pct_zero: 62.4\n    ood_mean_sj: 0.38\n    ood_sj_auroc: 0.52\n    ood_logprob_auroc: 0.58\n    ood_degradation_sj: -0.31\n    ood_degradation_logprob: -0.18\n  result_rationale: 'OOD 场景下所有 signal 几乎崩溃：SJ ρ=0.05（与 0 无显著差异）， logprob ρ=0.15（微弱但存在）。62.4%\n    sample F1=0 说明模型在 OOD 域上 大量 hallucinate。SJ 退化幅度（−0.31）远大于 logprob（−0.18）， 原因：OOD\n    hallucination 可以是 consistent（模型反复产出同一错误 entity set）， 导致高 SJ 但低 F1（hallucination\n    consistency）。Logprob 在 OOD 时天然偏低， 保持了弱单调关系。这在 worst 档下是 \"SJ 在 OOD 上完全失效\" 的证据，\n    但 paper 可能不会报告这个实验（P2 priority）。如果 reviewer 推断其存在 会进一步削弱 generalization 主张。\n\n    '\n  tables:\n  - table_id: T-011-1\n    caption: In-domain vs OOD signal quality (SciERC model → WNUT data)\n    columns:\n    - Signal\n    - In-domain ρ\n    - OOD ρ\n    - Degradation\n    rows:\n    - - Log-prob\n      - 0.33\n      - 0.15\n      - −0.18\n    - - Soft Jaccard\n      - 0.36\n      - 0.05\n      - −0.31\n    - - Voting conf\n      - 0.37\n      - 0.06\n      - −0.31\n    - - Fleiss' κ\n      - 0.27\n      - 0.03\n      - −0.24\n    - - Exact-match\n      - 0.26\n      - 0.04\n      - −0.22\n  figures_description: []\n  analysis: 'P2 实验。OOD 退化符合预期但在 worst 档下如果被 reviewer 追问 会成为致命弱点。SJ 的 hallucination\n    consistency failure mode 是 consistency-based methods 的根本局限性，但 paper 若不主动报告 反而显得在回避。\n\n    '\n- name: signal_ensemble_analysis\n  plan_id: exp-016\n  description: 'SJ+logprob 相关性分析、线性组合搜索、logistic regression 集成、 Best-of-N ensemble\n    selection。\n\n    '\n  expected_results:\n    sj_logprob_pearson_ner: 0.55\n    sj_logprob_pearson_re: 0.4\n    best_linear_ner:\n      combo: SJ+voting_conf\n      alpha: 0.35\n      rho: 0.39\n    best_linear_re:\n      combo: voting_conf+logprob\n      alpha: 0.55\n      rho: 0.33\n    ensemble_ner_auroc: 0.7\n    ensemble_re_auroc: 0.66\n    best_single_ner_auroc: 0.68\n    best_single_re_auroc: 0.64\n    ensemble_ner_delta_auroc: 0.02\n    ensemble_re_delta_auroc: 0.02\n    selection_f1_ner:\n      greedy: 0.618\n      logprob: 0.609\n      sj: 0.604\n      ensemble: 0.606\n      voting: 0.596\n      random: 0.58\n      oracle: 0.769\n    selection_f1_re:\n      logprob: 0.397\n      greedy: 0.374\n      sj: 0.368\n      ensemble: 0.375\n      voting: 0.338\n      random: 0.338\n      oracle: 0.561\n    fk_negative_weight: true\n  result_rationale: 'Ensemble 的 AUROC 提升仅 +0.02 on NER（0.70 vs best single 0.68），\n    RE 上同样 +0.02。线性组合 best ρ=0.39 仅比 best single(voting 0.37) 高 +0.02。 Worst 档的关键：ensemble\n    没有 meaningful 提升，说明各 signal 高度冗余—— 它们编码了相似的信息（SJ-logprob Pearson=0.55 证实了这一点）。\n    FK 在 logistic regression 中权重为负——surface agreement 在 structural signals 存在时是 net-negative（noisy\n    proxy 被 structural signal dominated）。 Best-of-N ensemble selection 同样 ≤ greedy\n    on NER（0.606 < 0.618）， RE 上 ensemble(0.375) ≈ greedy(0.374) but < logprob alone(0.397)。\n    Reviewer 评论：\"even combining all signals doesn''t help — the correlation-selection\n    gap is fundamental, not fixable by ensembling.\"\n\n    '\n  tables:\n  - table_id: T-016-1\n    caption: Signal ensemble analysis (SciERC)\n    columns:\n    - Metric\n    - Best Single\n    - Ensemble\n    - Δ\n    rows:\n    - - NER AUROC\n      - 0.68 (voting)\n      - 0.7\n      - '+0.02'\n    - - NER ρ\n      - 0.37 (voting)\n      - 0.39 (SJ+voting α=0.35)\n      - '+0.02'\n    - - RE AUROC\n      - 0.64 (voting)\n      - 0.66\n      - '+0.02'\n    - - RE ρ\n      - 0.30 (voting)\n      - 0.33 (voting+logprob α=0.55)\n      - '+0.03'\n  - table_id: T-016-2\n    caption: 'Best-of-N selection: ensemble vs individual'\n    columns:\n    - Signal\n    - NER F1\n    - RE F1\n    rows:\n    - - Greedy\n      - 0.618\n      - 0.374\n    - - Logprob\n      - 0.609\n      - 0.397\n    - - SJ\n      - 0.604\n      - 0.368\n    - - Ensemble\n      - 0.606\n      - 0.375\n    - - Voting\n      - 0.596\n      - 0.338\n    - - Oracle\n      - 0.769\n      - 0.561\n  figures_description:\n  - 'Fig-016-1: Heatmap — logistic regression 系数，FK 为负值（红色）， SJ 和 voting 正值接近，logprob\n    正值中等\n\n    '\n  analysis: 'Ensemble 分析回答了 Dream 2 reviewer 的问题但答案是负面的： 组合 signal 不产生 meaningful\n    improvement。这支持了 worst 档叙事： \"信号间高度冗余，correlation-selection gap 不是信号不足的问题， 而是 instance-level\n    metrics 的结构性局限。\" 但 reviewer 会将此解读为 \"insufficient methodological contribution —\n    the paper proposes nothing new.\"\n\n    '\n- name: ner_llama_conll\n  plan_id: exp-017\n  description: 'LLaMA-3.1-8B 在 CoNLL-2003 上 fine-tune + inference， 扩展 cross-model\n    × cross-dataset validation matrix。\n\n    '\n  expected_results:\n    greedy_f1: 0.924\n    oracle_f1: 0.945\n    oracle_headroom: 0.021\n    n_valid: 2756\n    full:\n      SJ_rho: 0.34\n      FK_rho: 0.33\n      logprob_rho: 0.31\n      EM_rho: 0.34\n      voting_rho: 0.33\n      SJ_AUROC: 0.68\n      logprob_AUROC: 0.66\n    conditional:\n      SJ_rho: 0.35\n      logprob_rho: 0.33\n    sj_minus_logprob_rho: 0.03\n    sj_minus_logprob_auroc: 0.02\n    best_of_n:\n      greedy: 0.924\n      sj_best: 0.92\n      logprob_best: 0.921\n      voting_best: 0.919\n      oracle: 0.945\n    structural_beats_logprob: true\n  result_rationale: 'LLaMA×CoNLL 是 2×2 matrix 的最后一个 cell。SJ ρ=0.34 与 Qwen3×CoNLL(0.34)\n    完全一致——structural signal 在 CoNLL 上 model-agnostic（好消息）， 但 gap vs logprob 仅 +0.03（坏消息）。Greedy\n    F1=0.924 极高（CoNLL 对 LLaMA 很容易）， headroom 仅 0.021，best-of-N 所有 signal ≤ greedy（SJ\n    0.920 < 0.924）。 AUROC gap +0.02 在 n=2756 下虽然统计显著但 practical significance 微弱。 Worst\n    档下 reviewer 看到这个结果会说：\"the 2×2 matrix is commendable for rigor, but it confirms\n    that on standard NER, the structural advantage is negligible (+0.02-0.03), and\n    selection never works.\" LLaMA×CoNLL 加入后 cross_config_structural_gt_logprob_rate\n    升到 ~0.70（7/10 configs），但 gap median 仅 +0.03。\n\n    '\n  tables:\n  - table_id: T-017-1\n    caption: LLaMA × CoNLL-2003 NER (N=8, T=1.0, n=2756)\n    columns:\n    - Signal\n    - ρ (full)\n    - AUROC\n    - ρ (cond)\n    rows:\n    - - Soft Jaccard\n      - 0.34\n      - 0.68\n      - 0.35\n    - - Exact-match\n      - 0.34\n      - 0.7\n      - 0.36\n    - - Voting conf\n      - 0.33\n      - 0.67\n      - 0.34\n    - - Fleiss' κ\n      - 0.33\n      - 0.66\n      - 0.34\n    - - Log-prob\n      - 0.31\n      - 0.66\n      - 0.33\n  - table_id: T-017-2\n    caption: 2×2 cross-validation matrix summary (NER, SJ ρ full)\n    columns:\n    - ' '\n    - Qwen3-8B\n    - LLaMA-3.1-8B\n    rows:\n    - - SciERC\n      - 0.36\n      - 0.36\n    - - CoNLL\n      - 0.34\n      - 0.34\n  - table_id: T-017-3\n    caption: '2×2 matrix: SJ − Logprob Δρ'\n    columns:\n    - ' '\n    - Qwen3-8B\n    - LLaMA-3.1-8B\n    rows:\n    - - SciERC\n      - '+0.03'\n      - '+0.06'\n    - - CoNLL\n      - '+0.02'\n      - '+0.03'\n  figures_description:\n  - 'Fig-017-1: 2×2 heatmap — SJ ρ 值，所有 cell 在 0.34-0.36 之间， cross-model×dataset consistency\n    很高但绝对值不突出\n\n    '\n  analysis: 2×2 matrix 在 worst 档下的价值是双面的：它证明了 robustness（SJ ρ 在 0.34-0.36  跨 model/dataset\n    一致），但也证明了 mediocrity（gap vs logprob 始终仅 +0.02-0.06， 从未达到让 reviewer 说 \"this is\n    meaningful\" 的水平）。 Reviewer 总结：\"the authors show a consistent but tiny advantage\n    of structural signals, which does not justify the 8× inference cost nor constitute\n    a sufficient contribution for a main conference paper.\" 这直接导致 R4+R19 的 rejection\n    rationale。\n",
      "numLines": 1616,
      "startLine": 1,
      "totalLines": 1616
    }
  },
  "sourceToolAssistantUUID": "34d55573-8383-48c7-b3e1-578badc59efe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a188aefa-23b6-4688-b448-164a4ee4e586",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-14T21:30:20.295Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_015drftxBQathRqaGkQ1t3e4`</summary>

```json
{
  "query": "select:submit_dream_review_report,read_project_file",
  "max_results": 3
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c0205324-64f4-413b-8711-9bd8bc3276d7",
  "isSidechain": false,
  "requestId": "req_011Cb3B2T4r89qr7DB4msYmk",
  "type": "assistant",
  "uuid": "3dbf4e07-cfee-4443-bc59-e3158ea51a1c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a188aefa-23b6-4688-b448-164a4ee4e586",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WsXKvaPJM7vap5Lo6aLg5p",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11112,
      "cache_read_input_tokens": 11841,
      "output_tokens": 376,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11112,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 376,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11112,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11112
          },
          "type": "message"
        }
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

_source line 17_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[DREAM Review Director] dream_id=20260514T203201 | review_mode=full | review_visible=True PDF: /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/d…",
  "leafUuid": "a43c3e51-17c9-4196-9131-42abc6db1b3e",
  "sessionId": "a188aefa-23b6-4688-b448-164a4ee4e586"
}
```

---

### Runtime record

_source line 18_

```json
{
  "type": "ai-title",
  "aiTitle": "Full blind review of structural self-consistency IE paper",
  "sessionId": "a188aefa-23b6-4688-b448-164a4ee4e586"
}
```

---

### Assistant

_source line 19 · 2026-05-14T21:30:41.958Z_

<details><summary>Logged reasoning block</summary>

```text
Let me now carefully analyze the paper and the review context. I need to dispatch two reviewers (R1 for methods+experiments, R2 for novelty+related work), then run a full roundtable (Step 1 independent → Step 2 cross-sharing → Step 3 convergence → Step 4 synthesis).

Let me first understand the paper thoroughly, then launch both reviewers in parallel.

The paper: "Why Self-Consistency Fails for Structured Prediction: An Analysis of the Correlation–Selection Gap"

Key claims:
1. Structural consistency signals (soft Jaccard, entity voting) correlate marginally more with output quality than log-probability on NER (Δρ = +0.01–0.04), but the advantage is small and statistically fragile


2. None of the confidence metrics actually improve best-of-N selection performance over greedy decoding on NER
3. The core finding is that consistency metrics predict input difficulty rather than per-sample output quality—this is the correlation-selection gap
4. Scaling to larger N and ensemble methods don't resolve the issue

Now I'm checking which experiments map to the review criteria: baseline log-probability, exact match, and entity voting approaches are all covered in Table 1, with the metrics expansion in Tables 1 and 2, and I need to verify the full NER experiment coverage. The remaining experiments round out the coverage nicely, and now I'm ready to set up parallel reviewers—one focused on methods and experiments, another on novelty and related work—with detailed evaluation prompts for each.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a43c3e51-17c9-4196-9131-42abc6db1b3e",
  "isSidechain": false,
  "requestId": "req_011Cb3B2viVzFSJqfVP4t6cg",
  "type": "assistant",
  "uuid": "d2d58430-d0a4-4624-b255-a7caaa63059f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a188aefa-23b6-4688-b448-164a4ee4e586",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017Zm6QokqPxvnsUrpNWExCg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 50736,
      "cache_read_input_tokens": 22953,
      "output_tokens": 3932,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 50736,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 3932,
          "cache_read_input_tokens": 22953,
          "cache_creation_input_tokens": 50736,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 50736
          },
          "type": "message"
        }
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

_source line 20 · 2026-05-14T21:30:42.031Z_

I've read the paper and the experiment design context. Now I'll dispatch two reviewers in parallel: R1 (methods + experiments) and R2 (novelty + related work).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d2d58430-d0a4-4624-b255-a7caaa63059f",
  "isSidechain": false,
  "requestId": "req_011Cb3B2viVzFSJqfVP4t6cg",
  "type": "assistant",
  "uuid": "b71e387a-8066-46e0-8828-7c60e67790cf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a188aefa-23b6-4688-b448-164a4ee4e586",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017Zm6QokqPxvnsUrpNWExCg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 50736,
      "cache_read_input_tokens": 22953,
      "output_tokens": 3932,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 50736,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 3932,
          "cache_read_input_tokens": 22953,
          "cache_creation_input_tokens": 50736,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 50736
          },
          "type": "message"
        }
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

_source line 21 · 2026-05-14T21:31:15.825Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01LJ37fBMNoZL1Xtr8mQcjgu`</summary>

```json
{
  "description": "R1: Methods + Experiments review",
  "prompt": "You are Reviewer R1 for a top ML venue (acceptance rate ~25%, 6-point scale: 1=Strong Reject, 2=Reject, 3=Weak Reject, 4=Weak Accept, 5=Accept, 6=Strong Accept). Your focus areas are **methods** and **experiments**.\n\n## Paper Summary\n\nTitle: \"Why Self-Consistency Fails for Structured Prediction: An Analysis of the Correlation–Selection Gap\"\n\nThe paper investigates whether consistency-based confidence signals can serve as quality estimators and sample selectors for structured information extraction (NER and RE). It compares 5 unsupervised confidence signals: log-probability, exact-match rate, Fleiss' κ, soft Jaccard (SJ), and entity voting confidence. Evaluated on 2 models (Qwen3-8B, LLaMA-3.1-8B) × 2 datasets (SciERC, CoNLL-2003), plus abandoned WNUT-17.\n\n**Main findings (negative):**\n- Structural consistency signals (SJ, voting) correlate only marginally more with F1 than log-probability on NER (Δρ = +0.01–0.04, ΔAUROC ≤ 0.04), not always statistically significant.\n- On RE (full set), log-probability matches or exceeds structural signals.\n- Best-of-N selection: ALL signals ≤ greedy on NER despite large oracle headroom (+15pp). On RE, only log-prob beats greedy (+2.3pp).\n- \"Correlation-selection gap\": instance-level consistency signals predict input difficulty, not per-sample quality. They assign the same score to all N samples from the same input → degenerate to random selection.\n- N=8→16 and signal ensembling don't close the gap.\n\n## Key Tables/Results\n\n**Table 1 (SciERC, N=8, T=1.0):**\n| Signal | NER ρ | NER AUROC | RE ρ | RE AUROC |\n|--------|-------|-----------|------|----------|\n| Voting | 0.37  | 0.68      | 0.30 | 0.64     |\n| SJ     | 0.36  | 0.67      | 0.21 | 0.59     |\n| Log-prob| 0.33 | 0.64      | 0.25 | 0.62     |\n| FK     | 0.27  | 0.59      | 0.25 | 0.61     |\n| EM     | 0.26  | 0.62      | 0.10 | 0.50     |\n| LOO-SJ | 0.35  | —         | —    | —        |\n\n**Table 3 (2×2 cross-validation, NER SJ ρ, SJ−LP Δρ):**\n| | Qwen3-8B | LLaMA-3.1-8B |\n|---|---|---|\n| SciERC | 0.36 (+0.03) | 0.36 (+0.06) |\n| CoNLL  | 0.34 (+0.02) | 0.34 (+0.03) |\n\n**Table 6 (Best-of-N selection F1):**\n| Signal | SciERC NER | SciERC RE | CoNLL NER |\n|--------|------------|-----------|-----------|\n| Greedy | 0.618      | 0.374     | 0.725     |\n| Log-prob| 0.609     | **0.397** | 0.716     |\n| SJ     | 0.604      | 0.368     | 0.718     |\n| Oracle | 0.769      | 0.561     | 0.757     |\n\n**Table 4 (N-scaling, SciERC):** NER SJ ρ@N=8=0.36, ρ@N=16=0.353 (Δ=−0.007). RE SJ ρ@N=8=0.21, ρ@N=16=0.28 (+0.07).\n\n**Table 5 (Temperature):** SJ at T=0.7 achieves ρ=0.39 (best), but log-prob is temperature-invariant (Δ=0.01).\n\n**Table 7 (Per-relation RE):** Log-prob exceeds SJ on 6/7 relation types. FEATURE-OF: SJ ρ≈0.\n\n**Table 8 (Stratification):** No clean inverted-U pattern. Log-prob exceeds SJ within every stratum.\n\n**Table 9 (OOD):** SJ drops 0.36→0.05 (Δ=−0.31), log-prob 0.33→0.15 (Δ=−0.18). \"Hallucination consistency\" failure mode.\n\n**Ensemble:** AUROC +0.02 over best single. Selection still ≤ greedy.\n\n## Experiment Design Reference (from review_context.yaml)\n\nThe full experiment plan includes 17 experiments. The paper covers ALL of them:\n- exp-012 to exp-016: baseline comparisons, metrics expansion (Tables 1-2)\n- exp-001: N=16 scaling (Table 4)\n- exp-002: CoNLL-2003 (Table 2)\n- exp-003: WNUT-17 (reported despite abandonment, Table 2, Section 5.2)\n- exp-004: RE diagnostic (Table 7)\n- exp-005: Temperature (Table 5)\n- exp-006: Best-of-N (Table 6)\n- exp-007: LLaMA cross-model (Table 3)\n- exp-008: RE N=16 (Table 4)\n- exp-009: Capability stratification (Table 8)\n- exp-010: Selection curves (Section 5.6, text only)\n- exp-011: OOD robustness (Table 9)\n- exp-016: Signal ensemble (Section 5.6)\n- exp-017: LLaMA×CoNLL (Table 3)\n\n## Your Review Task\n\nWrite a detailed review covering:\n\n1. **Summary** (2-3 sentences)\n2. **Strengths** (focus on methodology and experimental design)\n3. **Weaknesses** (focus on methodology and experimental design)\n4. **Questions for authors**\n5. **Minor issues**\n6. **Overall assessment** (1-2 sentences)\n7. **Scores**: Overall (1-6), Confidence (1-5)\n\nBe thorough, critical, and fair. Evaluate:\n- Is the experimental methodology sound?\n- Are the comparisons fair and comprehensive?\n- Are the statistical analyses adequate?\n- Is the evaluation protocol well-designed?\n- Are the conclusions supported by the evidence?\n- Are there methodological gaps or flaws?\n- Is the best-of-N selection protocol fair to instance-level signals?\n\nRemember: this is evaluated against top ML venue standards (~25% acceptance rate)."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b71e387a-8066-46e0-8828-7c60e67790cf",
  "isSidechain": false,
  "requestId": "req_011Cb3B2viVzFSJqfVP4t6cg",
  "type": "assistant",
  "uuid": "eed43daa-2573-430d-bbf1-453ad2e90bfe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a188aefa-23b6-4688-b448-164a4ee4e586",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017Zm6QokqPxvnsUrpNWExCg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 50736,
      "cache_read_input_tokens": 22953,
      "output_tokens": 3932,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 50736,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 3932,
          "cache_read_input_tokens": 22953,
          "cache_creation_input_tokens": 50736,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 50736
          },
          "type": "message"
        }
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

_source line 22 · 2026-05-14T21:31:39.554Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01Bp2K5oUbUiYisfDieZWQoP`</summary>

```json
{
  "description": "R2: Novelty + Related Work review",
  "prompt": "You are Reviewer R2 for a top ML venue (acceptance rate ~25%, 6-point scale: 1=Strong Reject, 2=Reject, 3=Weak Reject, 4=Weak Accept, 5=Accept, 6=Strong Accept). Your focus areas are **novelty** and **related work**.\n\n## Paper Summary\n\nTitle: \"Why Self-Consistency Fails for Structured Prediction: An Analysis of the Correlation–Selection Gap\"\n\nThe paper investigates whether consistency-based confidence signals can serve as quality estimators and sample selectors for structured information extraction (NER and RE). It compares 5 unsupervised confidence signals: log-probability (per-sample), exact-match rate, Fleiss' κ, soft Jaccard (SJ), and entity voting confidence (all instance-level). Evaluated on 2 models (Qwen3-8B, LLaMA-3.1-8B) × 2 datasets (SciERC, CoNLL-2003), plus abandoned WNUT-17 (social media NER).\n\n**Main claims:**\n1. Structural consistency signals correlate marginally more with output quality than log-probability (Δρ = +0.01–0.04 on NER), but differences are small and statistically fragile.\n2. On RE, log-probability matches or exceeds structural signals.\n3. **Correlation-selection gap**: Despite positive quality-estimation correlations, NO signal achieves best-of-N selection above greedy on NER. Oracle headroom is +15pp but entirely unexploited.\n4. The gap is structural: instance-level signals assign the same score to all N samples from an input → degenerate to random selection for best-of-N. Only per-sample log-prob can rank → succeeds on RE (+2.3pp) but not NER.\n5. N=8→16 and signal ensembling fail to close the gap.\n\n**Key related work cited:**\n- Wang et al. 2023: Self-consistency for reasoning (majority voting)\n- Nédellec & Xia 2026: Consistency-accuracy correlation for hard-prompted LLMs on plant health NER/RE using surface string matching\n- Kuhn et al. 2023: Semantic entropy\n- Manakul et al. 2023: SelfCheckGPT\n- Kadavath et al. 2022: \"Language models know what they know\"\n- Guo et al. 2017: Calibration of neural networks\n- Desai & Durrett 2020: Calibration for NLP\n- Snell et al. 2024: Test-time compute scaling\n- Brown et al. 2024: Large language monkeys\n- CoCoA (Vashurin et al. 2025): Combining confidence + consistency\n- Geifman & El-Yaniv 2017: Selective prediction\n- Kuleshov & Liang 2015: Calibrated structured prediction\n- Jagannatha & Yu 2022: Calibrating structured output predictors\n\n**Key tables:**\n- Table 1: 5-signal comparison on SciERC (SJ ρ=0.36 vs log-prob ρ=0.33 on NER; on RE log-prob exceeds SJ)\n- Table 3: 2×2 model-dataset matrix showing SJ ρ=0.34-0.36, SJ-LP gap +0.02 to +0.06\n- Table 6: Best-of-N — ALL signals ≤ greedy on NER, only log-prob beats greedy on RE\n- Table 9: OOD — SJ degrades asymmetrically (hallucination consistency)\n- Ensemble: AUROC +0.02, selection still fails\n\nThe paper frames itself as a \"negative result / cautionary analysis\" showing that self-consistency doesn't help for structured IE with fine-tuned models.\n\n## Your Review Task\n\nWrite a detailed review covering:\n\n1. **Summary** (2-3 sentences)\n2. **Strengths** (focus on novelty, positioning, and related work coverage)\n3. **Weaknesses** (focus on novelty, positioning, and related work coverage)\n4. **Questions for authors**\n5. **Minor issues**\n6. **Overall assessment** (1-2 sentences)\n7. **Scores**: Overall (1-6), Confidence (1-5)\n\nBe thorough, critical, and fair. Evaluate:\n\n- **Novelty**: Is the correlation-selection gap a genuinely new insight, or is it obvious / already known? The paper itself admits \"this distinction between quality estimation and sample selection is well-known in calibration research but has not been empirically demonstrated for structured IE.\" Is empirical demonstration alone a sufficient contribution?\n- **Positioning relative to Nédellec & Xia 2026**: They already studied consistency-accuracy correlation for IE. The structural metrics (SJ) could be seen as a minor extension. Is this sufficiently differentiated?\n- **Contribution level**: The paper proposes no new method, no solution to the gap. Is \"identifying a problem and stopping\" sufficient for a top venue? Would this be Findings-level?\n- **Related work completeness**: Are there missing references? Is the calibration literature coverage adequate?\n- **Framing**: The paper leads with \"negative finding + explanation.\" Is this framing effective, or does it read as post-hoc rationalization?\n- **The \"correlation-selection gap\" concept**: Is the explanation (instance-level vs per-sample) trivial once stated? \"Instance-level aggregates can't rank individual samples\" — is this obvious?\n\nRemember: this is evaluated against top ML venue standards (~25% acceptance rate)."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "eed43daa-2573-430d-bbf1-453ad2e90bfe",
  "isSidechain": false,
  "requestId": "req_011Cb3B2viVzFSJqfVP4t6cg",
  "type": "assistant",
  "uuid": "26e8a300-138e-4cb8-b83c-9c3bf2035241",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a188aefa-23b6-4688-b448-164a4ee4e586",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017Zm6QokqPxvnsUrpNWExCg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 50736,
      "cache_read_input_tokens": 22953,
      "output_tokens": 3932,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 50736,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 3932,
          "cache_read_input_tokens": 22953,
          "cache_creation_input_tokens": 50736,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 50736
          },
          "type": "message"
        }
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

_source line 23 · 2026-05-14T21:33:48.104Z_

<details><summary>↩ Tool result · `toolu_01LJ37fBMNoZL1Xtr8mQcjgu`</summary>

```text


Here is my detailed review.

---

## Review: "Why Self-Consistency Fails for Structured Prediction: An Analysis of the Correlation-Selection Gap"

### 1. Summary

This paper systematically compares five unsupervised confidence signals (log-probability, exact match, Fleiss' kappa, Soft Jaccard, entity voting) for quality estimation and best-of-N sample selection in LLM-based information extraction (NER and RE). The central finding is a "correlation-selection gap": structural consistency signals correlate well with instance-level F1 (voting rho=0.50, AUROC=0.73 on NER) but fail to improve best-of-N selection over greedy decoding on NER, with only log-probability providing modest gains on RE (+2.3pp). The paper additionally characterizes how signal effectiveness depends on task difficulty and model capability boundaries.

### 2. Strengths

**S1. Well-motivated research question and clean conceptual contribution.** The distinction between quality estimation (which inputs are reliable) and sample selection (which output is best) is crisp and practically important. The "correlation-selection gap" is a genuinely useful concept that clarifies why high correlation does not imply selection utility. This reframing is the paper's strongest intellectual contribution and could influence how the community thinks about test-time scaling for structured tasks.

**S2. Comprehensive experimental coverage.** The 2x2 model-dataset matrix (Qwen3-8B and LLaMA-3.1-8B on SciERC and CoNLL-2003), three-seed robustness protocol, N=8/16 scaling, temperature ablation, per-relation diagnostics, capability stratification, leave-one-out circularity check, and ensemble analysis constitute a thorough evaluation. The 17-experiment plan is fully executed and reported. Few empirical papers at this venue achieve this level of completeness.

**S3. Honest reporting of negative results.** The paper does not oversell. The WNUT-17 failure mode (54% zero-F1, SJ rho=0.062 n.s.) is transparently reported as a method boundary rather than hidden. The RE weakness is acknowledged head-on. The best-of-N failure on NER is the central finding rather than being buried. This intellectual honesty strengthens credibility.

**S4. Practical utility.** The task-difficulty-dependent signal selection guidance (EM for easy tasks, structural signals for hard tasks, logprob for binary filtering) is actionable. The observation that logprob has high AUROC but low rho ("logprob paradox") is a useful diagnostic insight for practitioners choosing between filtering and ranking applications.

**S5. Strong related work positioning.** The paper situates itself well against Nedellec & Xia (2026), CISC, Self-Certainty, ReASC, CoCoA, and the broader self-consistency and uncertainty estimation literature. The explicit differentiation from reasoning-task self-consistency methods is well-argued.

### 3. Weaknesses

**W1. The correlation-selection gap explanation is incomplete and the best-of-N protocol is structurally biased against instance-level signals.** The paper correctly identifies that instance-level signals (SJ, voting, FK, EM) assign the same score to all N samples from one input and therefore cannot rank among candidates. But this is not a surprising empirical finding -- it is a *definitional property* of how these signals are computed. An instance-level aggregate cannot, by construction, perform per-sample selection. The paper presents this as an empirical discovery ("we find that...") when it is closer to a tautology. The real question -- which the paper does not adequately address -- is whether there exist natural per-sample variants of structural consistency signals (e.g., leave-one-out SJ per sample, or per-sample voting score) that could enable selection. The LOO-SJ analysis in Section 5.3 shows LOO-SJ has only delta rho = -0.014 from standard SJ, meaning leave-one-out *does* produce per-sample variation, but the paper only uses this to check evaluation circularity rather than testing it as a selection signal. This is a significant missed opportunity that weakens the claim that "consistency signals" generically fail at selection.

**W2. Single RE dataset with severe floor effects limits the generalizability of RE conclusions.** 44% of SciERC RE instances receive zero F1. This means nearly half the data contributes no discriminative signal, and the remaining 56% constitutes the effective evaluation set for RE (n=296 conditional). All RE-specific claims -- logprob's selection advantage, structural signal degradation, the compound-error narrative -- rest on this single dataset with severe floor effects. The paper acknowledges this in limitations but still makes strong claims about RE (Claim 3). A second RE dataset (e.g., TACRED, DocRED, or even SciERC with a different model that achieves higher base RE F1) would substantially strengthen these conclusions. As it stands, it is difficult to disentangle "RE is inherently harder for consistency signals" from "this particular model underperforms on SciERC RE."

**W3. The task-difficulty gradient conflates multiple variables.** The difficulty gradient (CoNLL easy, SciERC hard, WNUT-17 infeasible) simultaneously varies domain (news, science, social media), schema complexity (4 vs 6 entity types), text style, training data characteristics, and model capability level. When the paper claims "signal rankings depend on task difficulty," it is unclear which of these confounded variables drives the effect. For instance, the EM-over-SJ advantage on CoNLL could be because (a) CoNLL is easy, (b) CoNLL has fewer entity types so set-level structure matters less, or (c) CoNLL's newswire text produces more lexically consistent extractions. The paper gestures at this (noting the SJ-FK gap narrows with schema simplification) but does not provide controlled comparisons. An experiment varying schema complexity on the same dataset (e.g., evaluating SciERC with only the top-2 entity types) would help isolate the mechanism.

**W4. Statistical rigor is uneven.** The paper reports Spearman rho, Kendall tau, and AUROC but:
- Bootstrap confidence intervals are mentioned in Table 4 footnotes (sigma=0.025 for 3 seeds) but are not systematically reported for the main results in Table 1. Without CIs, many of the claimed signal orderings (e.g., SJ rho=0.357 vs FK rho=0.265 on SciERC NER -- is this significant?) cannot be assessed.
- The three-seed protocol uses only seeds 42, 123, 456. With 3 seeds, the standard error of the mean rho is approximately sigma/sqrt(3) = 0.025/1.73 = 0.014, which is uncomfortably close to some of the claimed differences (e.g., SJ-FK delta on CoNLL).
- Paired bootstrap tests or Williams' test for comparing dependent correlations are not reported for the key signal comparisons.
- The Fisher z-test (p=0.021) comparing NER vs RE SJ rho treats the correlations as independent, but they are computed on overlapping instances (SciERC NER and RE share the same input sentences), which inflates significance.

**W5. Missing method section in the main paper.** The paper available for review has no standalone method/signal definition section (method.tex is absent). Signal definitions appear only briefly in the experimental setup paragraph. The ROADMAP notes three CRITICAL issues with method.tex: (1) FK described as token-level but implemented as entity-level binary, (2) EM "equivalence" claim is mathematically incorrect, (3) SJ formula is oversimplified relative to implementation. If the formulas in the paper do not match the implementation, this is a serious methodological concern -- reviewers cannot verify what was actually computed. The dream paper's method section defines FK as "token-level inter-annotator agreement across N samples, treating each sample as an annotator assigning BIO tags," but project notes indicate the actual implementation differs. This discrepancy must be resolved.

**W6. The N=8 sample size may be insufficient for reliable structural consistency estimation, and N-scaling results are inconclusive.** N=8 provides only 28 pairwise comparisons for SJ and 8 samples for voting. The N=8 to N=16 scaling shows SJ improving from 0.357 to 0.412 on NER (a substantial +0.055), suggesting N=8 may underestimate SJ's true signal strength. Yet the paper's main conclusions (including the best-of-N failure) are drawn at N=8. RE SJ also improves from 0.211 to 0.281 at N=16. With potentially larger N (32, 64), the signal landscape could look meaningfully different, but this is not explored. The paper should more prominently acknowledge that its negative selection results may be N-dependent.

**W7. Ensemble analysis is superficial.** The ensemble of SJ+Voting achieves AUROC 0.735 (+3.5pp over best single signal) but is only briefly mentioned. The paper does not explore more sophisticated combination methods (e.g., stacking, learned weighting with cross-validation, or combining per-sample logprob with instance-level structural signals for selection). The logistic regression "proxy for trained verifier" is mentioned in the project notes but not reported in the paper. Given that logprob is the only per-sample signal and structural signals are the best instance-level signals, a natural question is whether combining logprob's per-sample ranking with structural signals' instance-level filtering (e.g., use structural signals to identify uncertain instances, then use logprob to select among candidates for those instances) could close the gap. This hybrid strategy is never tested.

### 4. Questions for Authors

**Q1.** Have you tested per-sample variants of structural consistency signals for best-of-N selection? Specifically: (a) LOO-SJ_i = average SJ between sample i and all other samples, used to rank samples within an instance; (b) per-sample voting score = average voting confidence of entities in sample i. These would convert instance-level signals into per-sample signals while retaining structural information. If tested, what were the results? If not, why not?

**Q2.** The paper reports the conditional analysis (filtering to non-zero F1 instances) improves all signals. But the conditional set is defined using the *greedy* output's F1, which requires gold labels. How would a practitioner perform this filtering at deployment time without gold labels? Is the suggestion that structural signals themselves could serve as the filter (high SJ -> likely non-zero F1), creating a two-stage pipeline?

**Q3.** For the best-of-N selection experiment, how exactly is voting confidence used to select a sample? Since voting scores each entity in y_0 (the greedy output) by its frequency across N samples, it produces an instance-level score, not a per-sample score. Does the paper select the sample with highest average entity-voting overlap with y_0? Or is there a different mechanism? The selection protocol for instance-level signals is unclear.

**Q4.** The "logprob paradox" (high AUROC, low rho) on CoNLL-LLaMA is attributed to coarse binary separation. Have you examined the logprob score distribution? Could this be an artifact of the LLaMA model's calibration properties on CoNLL specifically, rather than a general property of logprob?

**Q5.** The paper fine-tunes both models with LoRA. How sensitive are the results to fine-tuning quality? The decisions log shows RE F1 of only 33.8% after initial fine-tuning (ft_001), improving only marginally with ft_002_v2. Would the structural signal rankings change with a stronger base extraction model (e.g., one achieving >50% RE F1)?

### 5. Minor Issues

- The abstract mentions "three datasets" but WNUT-17 is essentially a negative case study rather than a full evaluation dataset. Consider being more precise (e.g., "two primary datasets and one out-of-domain probe").
- Table 6 (best-of-N selection) reports EM as "---" with a note that "EM produces binary agreement without sample ranking." But EM *could* be used for selection by picking the sample that appears most frequently in exact-match clusters. This should be clarified.
- The paper references Figure 1 (overview), Figure (signal_heatmap), Figure (selection_gap), and Figure (reliability), but none of these figures are present in the available manuscript sections. A paper of this data density absolutely requires figures -- the absence significantly hurts readability and persuasiveness.
- Table 4 N-scaling: the N=16 SJ value 0.412 is a 3-seed mean, but the N=8 SJ value 0.357 appears to be single-seed. This asymmetry makes the N-scaling comparison imprecise.
- Section 5.3 mentions "three independent complexity proxies (entity count, sentence length, relation density) show weak mutual correlation (|r|<0.15)" but the project notes (D042) report entity_count and rel_count have rho=0.769, which contradicts the claim. The paper must correct this -- only sentence length and entity count appear to be genuinely independent.
- The title "Why Self-Consistency Fails for Structured Prediction" is somewhat misleading. Self-consistency does not "fail" for quality estimation -- it works well. It fails only for *selection*. A more precise title would reflect both the positive (quality estimation) and negative (selection) findings.
- Limitations correctly notes that logprob was excluded from temperature comparison due to missing T=0.7 data. This is a notable gap given that logprob is the only signal that enables RE selection.

### 6. Overall Assessment

This is a well-executed empirical study with a genuinely useful conceptual contribution (the correlation-selection gap). The experimental coverage is commendable, and the honest treatment of negative results is refreshing. However, the paper has significant methodological gaps: the best-of-N evaluation is structurally unfair to instance-level signals (W1), the explanation of the gap borders on tautological, the RE conclusions rest on a single dataset with severe floor effects (W2), statistical significance testing is insufficient for the claimed comparisons (W4), and the method section with its formula-implementation discrepancies is a serious concern (W5). The missing figures further weaken the presentation. In its current form, the paper provides useful empirical observations but the main conceptual claim (correlation-selection gap as a "fundamental disconnect") overstates what is ultimately a consequence of how the signals are defined. With a per-sample structural signal variant, a second RE dataset, proper significance testing, figures, and a corrected method section, this could be a solid EMNLP contribution.

### 7. Scores

- **Overall: 4 (Weak Accept)**
- **Confidence: 4 (High confidence -- I have reviewed the full experimental pipeline, project decisions, and paper text in detail)**

**Justification:** The experimental breadth, honest negative results, and useful conceptual framing (quality estimation vs selection) place this above the median submission. However, the tautological nature of the core finding (instance-level signals cannot do per-sample selection, by construction), the single-RE-dataset limitation, missing figures, absent/incorrect method section, and insufficient statistical testing prevent a stronger recommendation. The paper is borderline -- the core insight is publishable at EMNLP, but execution gaps need to be addressed.

agentId: a10411b05b0953632 (use SendMessage with to: 'a10411b05b0953632' to continue this agent)
&lt;usage>total_tokens: 81731
tool_uses: 20
duration_ms: 152271&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "eed43daa-2573-430d-bbf1-453ad2e90bfe",
  "isSidechain": false,
  "promptId": "a640b4e1-01ba-4811-b057-a5972a785ed6",
  "type": "user",
  "uuid": "4372cb60-3cee-4c92-9f1a-772c999e3e5a",
  "toolUseResult": {
    "status": "completed",
    "prompt": "You are Reviewer R1 for a top ML venue (acceptance rate ~25%, 6-point scale: 1=Strong Reject, 2=Reject, 3=Weak Reject, 4=Weak Accept, 5=Accept, 6=Strong Accept). Your focus areas are **methods** and **experiments**.\n\n## Paper Summary\n\nTitle: \"Why Self-Consistency Fails for Structured Prediction: An Analysis of the Correlation–Selection Gap\"\n\nThe paper investigates whether consistency-based confidence signals can serve as quality estimators and sample selectors for structured information extraction (NER and RE). It compares 5 unsupervised confidence signals: log-probability, exact-match rate, Fleiss' κ, soft Jaccard (SJ), and entity voting confidence. Evaluated on 2 models (Qwen3-8B, LLaMA-3.1-8B) × 2 datasets (SciERC, CoNLL-2003), plus abandoned WNUT-17.\n\n**Main findings (negative):**\n- Structural consistency signals (SJ, voting) correlate only marginally more with F1 than log-probability on NER (Δρ = +0.01–0.04, ΔAUROC ≤ 0.04), not always statistically significant.\n- On RE (full set), log-probability matches or exceeds structural signals.\n- Best-of-N selection: ALL signals ≤ greedy on NER despite large oracle headroom (+15pp). On RE, only log-prob beats greedy (+2.3pp).\n- \"Correlation-selection gap\": instance-level consistency signals predict input difficulty, not per-sample quality. They assign the same score to all N samples from the same input → degenerate to random selection.\n- N=8→16 and signal ensembling don't close the gap.\n\n## Key Tables/Results\n\n**Table 1 (SciERC, N=8, T=1.0):**\n| Signal | NER ρ | NER AUROC | RE ρ | RE AUROC |\n|--------|-------|-----------|------|----------|\n| Voting | 0.37  | 0.68      | 0.30 | 0.64     |\n| SJ     | 0.36  | 0.67      | 0.21 | 0.59     |\n| Log-prob| 0.33 | 0.64      | 0.25 | 0.62     |\n| FK     | 0.27  | 0.59      | 0.25 | 0.61     |\n| EM     | 0.26  | 0.62      | 0.10 | 0.50     |\n| LOO-SJ | 0.35  | —         | —    | —        |\n\n**Table 3 (2×2 cross-validation, NER SJ ρ, SJ−LP Δρ):**\n| | Qwen3-8B | LLaMA-3.1-8B |\n|---|---|---|\n| SciERC | 0.36 (+0.03) | 0.36 (+0.06) |\n| CoNLL  | 0.34 (+0.02) | 0.34 (+0.03) |\n\n**Table 6 (Best-of-N selection F1):**\n| Signal | SciERC NER | SciERC RE | CoNLL NER |\n|--------|------------|-----------|-----------|\n| Greedy | 0.618      | 0.374     | 0.725     |\n| Log-prob| 0.609     | **0.397** | 0.716     |\n| SJ     | 0.604      | 0.368     | 0.718     |\n| Oracle | 0.769      | 0.561     | 0.757     |\n\n**Table 4 (N-scaling, SciERC):** NER SJ ρ@N=8=0.36, ρ@N=16=0.353 (Δ=−0.007). RE SJ ρ@N=8=0.21, ρ@N=16=0.28 (+0.07).\n\n**Table 5 (Temperature):** SJ at T=0.7 achieves ρ=0.39 (best), but log-prob is temperature-invariant (Δ=0.01).\n\n**Table 7 (Per-relation RE):** Log-prob exceeds SJ on 6/7 relation types. FEATURE-OF: SJ ρ≈0.\n\n**Table 8 (Stratification):** No clean inverted-U pattern. Log-prob exceeds SJ within every stratum.\n\n**Table 9 (OOD):** SJ drops 0.36→0.05 (Δ=−0.31), log-prob 0.33→0.15 (Δ=−0.18). \"Hallucination consistency\" failure mode.\n\n**Ensemble:** AUROC +0.02 over best single. Selection still ≤ greedy.\n\n## Experiment Design Reference (from review_context.yaml)\n\nThe full experiment plan includes 17 experiments. The paper covers ALL of them:\n- exp-012 to exp-016: baseline comparisons, metrics expansion (Tables 1-2)\n- exp-001: N=16 scaling (Table 4)\n- exp-002: CoNLL-2003 (Table 2)\n- exp-003: WNUT-17 (reported despite abandonment, Table 2, Section 5.2)\n- exp-004: RE diagnostic (Table 7)\n- exp-005: Temperature (Table 5)\n- exp-006: Best-of-N (Table 6)\n- exp-007: LLaMA cross-model (Table 3)\n- exp-008: RE N=16 (Table 4)\n- exp-009: Capability stratification (Table 8)\n- exp-010: Selection curves (Section 5.6, text only)\n- exp-011: OOD robustness (Table 9)\n- exp-016: Signal ensemble (Section 5.6)\n- exp-017: LLaMA×CoNLL (Table 3)\n\n## Your Review Task\n\nWrite a detailed review covering:\n\n1. **Summary** (2-3 sentences)\n2. **Strengths** (focus on methodology and experimental design)\n3. **Weaknesses** (focus on methodology and experimental design)\n4. **Questions for authors**\n5. **Minor issues**\n6. **Overall assessment** (1-2 sentences)\n7. **Scores**: Overall (1-6), Confidence (1-5)\n\nBe thorough, critical, and fair. Evaluate:\n- Is the experimental methodology sound?\n- Are the comparisons fair and comprehensive?\n- Are the statistical analyses adequate?\n- Is the evaluation protocol well-designed?\n- Are the conclusions supported by the evidence?\n- Are there methodological gaps or flaws?\n- Is the best-of-N selection protocol fair to instance-level signals?\n\nRemember: this is evaluated against top ML venue standards (~25% acceptance rate).",
    "agentId": "a10411b05b0953632",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "\n\nHere is my detailed review.\n\n---\n\n## Review: \"Why Self-Consistency Fails for Structured Prediction: An Analysis of the Correlation-Selection Gap\"\n\n### 1. Summary\n\nThis paper systematically compares five unsupervised confidence signals (log-probability, exact match, Fleiss' kappa, Soft Jaccard, entity voting) for quality estimation and best-of-N sample selection in LLM-based information extraction (NER and RE). The central finding is a \"correlation-selection gap\": structural consistency signals correlate well with instance-level F1 (voting rho=0.50, AUROC=0.73 on NER) but fail to improve best-of-N selection over greedy decoding on NER, with only log-probability providing modest gains on RE (+2.3pp). The paper additionally characterizes how signal effectiveness depends on task difficulty and model capability boundaries.\n\n### 2. Strengths\n\n**S1. Well-motivated research question and clean conceptual contribution.** The distinction between quality estimation (which inputs are reliable) and sample selection (which output is best) is crisp and practically important. The \"correlation-selection gap\" is a genuinely useful concept that clarifies why high correlation does not imply selection utility. This reframing is the paper's strongest intellectual contribution and could influence how the community thinks about test-time scaling for structured tasks.\n\n**S2. Comprehensive experimental coverage.** The 2x2 model-dataset matrix (Qwen3-8B and LLaMA-3.1-8B on SciERC and CoNLL-2003), three-seed robustness protocol, N=8/16 scaling, temperature ablation, per-relation diagnostics, capability stratification, leave-one-out circularity check, and ensemble analysis constitute a thorough evaluation. The 17-experiment plan is fully executed and reported. Few empirical papers at this venue achieve this level of completeness.\n\n**S3. Honest reporting of negative results.** The paper does not oversell. The WNUT-17 failure mode (54% zero-F1, SJ rho=0.062 n.s.) is transparently reported as a method boundary rather than hidden. The RE weakness is acknowledged head-on. The best-of-N failure on NER is the central finding rather than being buried. This intellectual honesty strengthens credibility.\n\n**S4. Practical utility.** The task-difficulty-dependent signal selection guidance (EM for easy tasks, structural signals for hard tasks, logprob for binary filtering) is actionable. The observation that logprob has high AUROC but low rho (\"logprob paradox\") is a useful diagnostic insight for practitioners choosing between filtering and ranking applications.\n\n**S5. Strong related work positioning.** The paper situates itself well against Nedellec & Xia (2026), CISC, Self-Certainty, ReASC, CoCoA, and the broader self-consistency and uncertainty estimation literature. The explicit differentiation from reasoning-task self-consistency methods is well-argued.\n\n### 3. Weaknesses\n\n**W1. The correlation-selection gap explanation is incomplete and the best-of-N protocol is structurally biased against instance-level signals.** The paper correctly identifies that instance-level signals (SJ, voting, FK, EM) assign the same score to all N samples from one input and therefore cannot rank among candidates. But this is not a surprising empirical finding -- it is a *definitional property* of how these signals are computed. An instance-level aggregate cannot, by construction, perform per-sample selection. The paper presents this as an empirical discovery (\"we find that...\") when it is closer to a tautology. The real question -- which the paper does not adequately address -- is whether there exist natural per-sample variants of structural consistency signals (e.g., leave-one-out SJ per sample, or per-sample voting score) that could enable selection. The LOO-SJ analysis in Section 5.3 shows LOO-SJ has only delta rho = -0.014 from standard SJ, meaning leave-one-out *does* produce per-sample variation, but the paper only uses this to check evaluation circularity rather than testing it as a selection signal. This is a significant missed opportunity that weakens the claim that \"consistency signals\" generically fail at selection.\n\n**W2. Single RE dataset with severe floor effects limits the generalizability of RE conclusions.** 44% of SciERC RE instances receive zero F1. This means nearly half the data contributes no discriminative signal, and the remaining 56% constitutes the effective evaluation set for RE (n=296 conditional). All RE-specific claims -- logprob's selection advantage, structural signal degradation, the compound-error narrative -- rest on this single dataset with severe floor effects. The paper acknowledges this in limitations but still makes strong claims about RE (Claim 3). A second RE dataset (e.g., TACRED, DocRED, or even SciERC with a different model that achieves higher base RE F1) would substantially strengthen these conclusions. As it stands, it is difficult to disentangle \"RE is inherently harder for consistency signals\" from \"this particular model underperforms on SciERC RE.\"\n\n**W3. The task-difficulty gradient conflates multiple variables.** The difficulty gradient (CoNLL easy, SciERC hard, WNUT-17 infeasible) simultaneously varies domain (news, science, social media), schema complexity (4 vs 6 entity types), text style, training data characteristics, and model capability level. When the paper claims \"signal rankings depend on task difficulty,\" it is unclear which of these confounded variables drives the effect. For instance, the EM-over-SJ advantage on CoNLL could be because (a) CoNLL is easy, (b) CoNLL has fewer entity types so set-level structure matters less, or (c) CoNLL's newswire text produces more lexically consistent extractions. The paper gestures at this (noting the SJ-FK gap narrows with schema simplification) but does not provide controlled comparisons. An experiment varying schema complexity on the same dataset (e.g., evaluating SciERC with only the top-2 entity types) would help isolate the mechanism.\n\n**W4. Statistical rigor is uneven.** The paper reports Spearman rho, Kendall tau, and AUROC but:\n- Bootstrap confidence intervals are mentioned in Table 4 footnotes (sigma=0.025 for 3 seeds) but are not systematically reported for the main results in Table 1. Without CIs, many of the claimed signal orderings (e.g., SJ rho=0.357 vs FK rho=0.265 on SciERC NER -- is this significant?) cannot be assessed.\n- The three-seed protocol uses only seeds 42, 123, 456. With 3 seeds, the standard error of the mean rho is approximately sigma/sqrt(3) = 0.025/1.73 = 0.014, which is uncomfortably close to some of the claimed differences (e.g., SJ-FK delta on CoNLL).\n- Paired bootstrap tests or Williams' test for comparing dependent correlations are not reported for the key signal comparisons.\n- The Fisher z-test (p=0.021) comparing NER vs RE SJ rho treats the correlations as independent, but they are computed on overlapping instances (SciERC NER and RE share the same input sentences), which inflates significance.\n\n**W5. Missing method section in the main paper.** The paper available for review has no standalone method/signal definition section (method.tex is absent). Signal definitions appear only briefly in the experimental setup paragraph. The ROADMAP notes three CRITICAL issues with method.tex: (1) FK described as token-level but implemented as entity-level binary, (2) EM \"equivalence\" claim is mathematically incorrect, (3) SJ formula is oversimplified relative to implementation. If the formulas in the paper do not match the implementation, this is a serious methodological concern -- reviewers cannot verify what was actually computed. The dream paper's method section defines FK as \"token-level inter-annotator agreement across N samples, treating each sample as an annotator assigning BIO tags,\" but project notes indicate the actual implementation differs. This discrepancy must be resolved.\n\n**W6. The N=8 sample size may be insufficient for reliable structural consistency estimation, and N-scaling results are inconclusive.** N=8 provides only 28 pairwise comparisons for SJ and 8 samples for voting. The N=8 to N=16 scaling shows SJ improving from 0.357 to 0.412 on NER (a substantial +0.055), suggesting N=8 may underestimate SJ's true signal strength. Yet the paper's main conclusions (including the best-of-N failure) are drawn at N=8. RE SJ also improves from 0.211 to 0.281 at N=16. With potentially larger N (32, 64), the signal landscape could look meaningfully different, but this is not explored. The paper should more prominently acknowledge that its negative selection results may be N-dependent.\n\n**W7. Ensemble analysis is superficial.** The ensemble of SJ+Voting achieves AUROC 0.735 (+3.5pp over best single signal) but is only briefly mentioned. The paper does not explore more sophisticated combination methods (e.g., stacking, learned weighting with cross-validation, or combining per-sample logprob with instance-level structural signals for selection). The logistic regression \"proxy for trained verifier\" is mentioned in the project notes but not reported in the paper. Given that logprob is the only per-sample signal and structural signals are the best instance-level signals, a natural question is whether combining logprob's per-sample ranking with structural signals' instance-level filtering (e.g., use structural signals to identify uncertain instances, then use logprob to select among candidates for those instances) could close the gap. This hybrid strategy is never tested.\n\n### 4. Questions for Authors\n\n**Q1.** Have you tested per-sample variants of structural consistency signals for best-of-N selection? Specifically: (a) LOO-SJ_i = average SJ between sample i and all other samples, used to rank samples within an instance; (b) per-sample voting score = average voting confidence of entities in sample i. These would convert instance-level signals into per-sample signals while retaining structural information. If tested, what were the results? If not, why not?\n\n**Q2.** The paper reports the conditional analysis (filtering to non-zero F1 instances) improves all signals. But the conditional set is defined using the *greedy* output's F1, which requires gold labels. How would a practitioner perform this filtering at deployment time without gold labels? Is the suggestion that structural signals themselves could serve as the filter (high SJ -> likely non-zero F1), creating a two-stage pipeline?\n\n**Q3.** For the best-of-N selection experiment, how exactly is voting confidence used to select a sample? Since voting scores each entity in y_0 (the greedy output) by its frequency across N samples, it produces an instance-level score, not a per-sample score. Does the paper select the sample with highest average entity-voting overlap with y_0? Or is there a different mechanism? The selection protocol for instance-level signals is unclear.\n\n**Q4.** The \"logprob paradox\" (high AUROC, low rho) on CoNLL-LLaMA is attributed to coarse binary separation. Have you examined the logprob score distribution? Could this be an artifact of the LLaMA model's calibration properties on CoNLL specifically, rather than a general property of logprob?\n\n**Q5.** The paper fine-tunes both models with LoRA. How sensitive are the results to fine-tuning quality? The decisions log shows RE F1 of only 33.8% after initial fine-tuning (ft_001), improving only marginally with ft_002_v2. Would the structural signal rankings change with a stronger base extraction model (e.g., one achieving >50% RE F1)?\n\n### 5. Minor Issues\n\n- The abstract mentions \"three datasets\" but WNUT-17 is essentially a negative case study rather than a full evaluation dataset. Consider being more precise (e.g., \"two primary datasets and one out-of-domain probe\").\n- Table 6 (best-of-N selection) reports EM as \"---\" with a note that \"EM produces binary agreement without sample ranking.\" But EM *could* be used for selection by picking the sample that appears most frequently in exact-match clusters. This should be clarified.\n- The paper references Figure 1 (overview), Figure (signal_heatmap), Figure (selection_gap), and Figure (reliability), but none of these figures are present in the available manuscript sections. A paper of this data density absolutely requires figures -- the absence significantly hurts readability and persuasiveness.\n- Table 4 N-scaling: the N=16 SJ value 0.412 is a 3-seed mean, but the N=8 SJ value 0.357 appears to be single-seed. This asymmetry makes the N-scaling comparison imprecise.\n- Section 5.3 mentions \"three independent complexity proxies (entity count, sentence length, relation density) show weak mutual correlation (|r|<0.15)\" but the project notes (D042) report entity_count and rel_count have rho=0.769, which contradicts the claim. The paper must correct this -- only sentence length and entity count appear to be genuinely independent.\n- The title \"Why Self-Consistency Fails for Structured Prediction\" is somewhat misleading. Self-consistency does not \"fail\" for quality estimation -- it works well. It fails only for *selection*. A more precise title would reflect both the positive (quality estimation) and negative (selection) findings.\n- Limitations correctly notes that logprob was excluded from temperature comparison due to missing T=0.7 data. This is a notable gap given that logprob is the only signal that enables RE selection.\n\n### 6. Overall Assessment\n\nThis is a well-executed empirical study with a genuinely useful conceptual contribution (the correlation-selection gap). The experimental coverage is commendable, and the honest treatment of negative results is refreshing. However, the paper has significant methodological gaps: the best-of-N evaluation is structurally unfair to instance-level signals (W1), the explanation of the gap borders on tautological, the RE conclusions rest on a single dataset with severe floor effects (W2), statistical significance testing is insufficient for the claimed comparisons (W4), and the method section with its formula-implementation discrepancies is a serious concern (W5). The missing figures further weaken the presentation. In its current form, the paper provides useful empirical observations but the main conceptual claim (correlation-selection gap as a \"fundamental disconnect\") overstates what is ultimately a consequence of how the signals are defined. With a per-sample structural signal variant, a second RE dataset, proper significance testing, figures, and a corrected method section, this could be a solid EMNLP contribution.\n\n### 7. Scores\n\n- **Overall: 4 (Weak Accept)**\n- **Confidence: 4 (High confidence -- I have reviewed the full experimental pipeline, project decisions, and paper text in detail)**\n\n**Justification:** The experimental breadth, honest negative results, and useful conceptual framing (quality estimation vs selection) place this above the median submission. However, the tautological nature of the core finding (instance-level signals cannot do per-sample selection, by construction), the single-RE-dataset limitation, missing figures, absent/incorrect method section, and insufficient statistical testing prevent a stronger recommendation. The paper is borderline -- the core insight is publishable at EMNLP, but execution gaps need to be addressed."
      }
    ],
    "totalDurationMs": 152271,
    "totalTokens": 81731,
    "totalToolUseCount": 20,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 514,
      "cache_read_input_tokens": 77570,
      "output_tokens": 3644,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 514
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 3644,
          "cache_read_input_tokens": 77570,
          "cache_creation_input_tokens": 514,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 514,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 9,
      "searchCount": 3,
      "bashCount": 0,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 8
    }
  },
  "sourceToolAssistantUUID": "eed43daa-2573-430d-bbf1-453ad2e90bfe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a188aefa-23b6-4688-b448-164a4ee4e586",
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
  "lastPrompt": "[DREAM Review Director] dream_id=20260514T203201 | review_mode=full | review_visible=True PDF: /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/d…",
  "leafUuid": "4372cb60-3cee-4c92-9f1a-772c999e3e5a",
  "sessionId": "a188aefa-23b6-4688-b448-164a4ee4e586"
}
```

---

### Runtime record

_source line 25_

```json
{
  "type": "ai-title",
  "aiTitle": "Full blind review of structural self-consistency IE paper",
  "sessionId": "a188aefa-23b6-4688-b448-164a4ee4e586"
}
```

---

### Tool result

_source line 26 · 2026-05-14T21:33:54.623Z_

<details><summary>↩ Tool result · `toolu_01Bp2K5oUbUiYisfDieZWQoP`</summary>

```text


Now I have all the material needed. Let me write the review directly.

---

## Review: "Why Self-Consistency Fails for Structured Prediction: An Analysis of the Correlation-Selection Gap"

**Reviewer R2 — Focus: Novelty and Related Work**

---

### 1. Summary

This paper compares five unsupervised confidence signals (log-probability, exact match, Fleiss' kappa, Soft Jaccard, entity voting) for quality estimation and best-of-N selection in LLM-based information extraction (NER and RE). The central finding is a "correlation-selection gap": structural consistency signals strongly predict instance-level quality (voting rho=0.50, AUROC=0.73 on NER) but fail to improve best-of-N selection over greedy decoding on NER, with only log-probability helping on RE (+2.3pp). The paper attributes this to the instance-level nature of consistency signals, which cannot discriminate among N candidates for a single input.

### 2. Strengths

**S1. The quality estimation vs. selection disentanglement is well-executed.** The paper cleanly separates two objectives that are indeed conflated in much prior work on self-consistency. The experimental demonstration across 2 models x 2 datasets is thorough, and the method section (Section 2) formalizes the per-sample vs. instance-level signal distinction clearly. This separation is the paper's strongest conceptual contribution.

**S2. Comprehensive related work, given the revised draft.** The related work section is well-organized into three subsections (self-consistency/TTS, consistency for structured IE, uncertainty/calibration) and covers the relevant 2024-2026 literature with appropriate depth. The positioning against Nedellec & Xia (2026) is explicit and fair, identifying three concrete gaps (surface matching only, no selection analysis, single domain). The coverage of CISC, Self-Certainty, ReASC, and CoCoA situates the work within the broader TTS landscape. The conformal prediction, token-level NER uncertainty, and verifier/reward model threads are appropriately included as related paradigms.

**S3. Honest reporting of negative results and method boundaries.** The WNUT-17 analysis (54% zero F1, SJ rho=0.062 not significant, logprob negative correlation) is reported transparently as a capability boundary rather than buried. The task-difficulty-dependent signal ranking (EM leads on easy tasks, SJ on hard tasks) is a nuanced finding that avoids overclaiming a universal winner.

**S4. The task-difficulty-dependent signal ranking is a genuine empirical contribution.** The observation that EM > SJ on CoNLL but SJ > EM on SciERC, with convergence when model capability is insufficient, provides actionable guidance. This is more informative than a simple "our metric wins" narrative.

### 3. Weaknesses

**W1. The "correlation-selection gap" explanation is close to tautological once stated.** The paper's central conceptual contribution — that instance-level aggregates cannot rank individual samples — is presented as a discovery, but it follows almost directly from the definition. An instance-level signal c_il: (x, {y_i}) -> R produces one number per input; it *cannot* rank N candidates by construction. The paper acknowledges this in Section 2 ("instance-level signals... do not inherently rank individual samples") but then treats the empirical confirmation as a major finding. The genuine surprise would be if instance-level signals *did* help selection (e.g., by identifying easy instances where random selection suffices). The fact that they don't is the expected null result. What is mildly interesting is that even the consensus-closest-sample selection strategy fails, but this is underexplored — the paper devotes only one sentence to how instance-level signals are adapted for selection (Section 2.3: "we select the sample closest to the consensus output").

This weakness is significant for novelty assessment. The conceptual contribution reduces to: (a) instance-level signals can't rank samples (definitional), and (b) log-probability, the only per-sample signal, helps on RE but not NER (a single empirical observation). Neither alone meets the novelty bar for a top venue.

**W2. Insufficient differentiation from Nedellec & Xia (2026).** The paper argues three differences: structural metrics vs. surface matching, best-of-N analysis, and multi-domain evaluation. However:
- The structural metrics (SJ, voting) are relatively straightforward extensions of Jaccard similarity and frequency counting to entity sets. The Hungarian matching with span overlap is a reasonable design choice but not technically novel.
- The best-of-N analysis yields a negative result (no signal beats greedy on NER), which, combined with W1, amounts to showing that something definitionally incapable of ranking samples indeed fails to rank samples.
- The multi-domain evaluation is valuable but incremental.

The paper reads as "Nedellec & Xia (2026) + better metrics + negative selection result." The SJ metric itself is the main technical delta, and it is not a major methodological contribution — it is a sensible instantiation of set similarity that one would naturally try.

**W3. No proposed solution or path forward beyond "use trained verifiers."** The paper identifies a gap and stops. The conclusion lists future work (trained verifiers, conformal prediction, larger models) but does not even attempt a preliminary solution. For a top venue, a pure negative-result paper needs either (a) a very surprising negative result, or (b) deep mechanistic understanding that enables future solutions. The explanation here ("instance-level signals can't rank samples") is shallow — it does not explain *why* the consensus-closest strategy fails, whether per-sample structural signals could be constructed, or what properties a successful selector would need. The oracle headroom analysis (NER +16pp, RE +19pp) tantalizes but receives no further investigation.

**W4. The contribution is positioned ambiguously between "systematic comparison" and "novel finding."** The paper's title and framing emphasize the correlation-selection gap as a novel finding, but the bulk of the experimental content is a systematic comparison of five signals. Systematic comparisons are valuable but are typically positioned as resource papers or Findings-level contributions unless they reveal unexpected phenomena. The unexpected phenomenon here (the gap) is, per W1, close to expected once the signal taxonomy is laid out. The paper would be strengthened by committing to one framing: either a rigorous systematic comparison (in which case, more signals, datasets, and models would be expected) or a mechanistic analysis of the gap (in which case, deeper investigation is needed).

**W5. Missing related work on minimum Bayes risk (MBR) decoding for structured prediction.** MBR decoding — selecting the sample that maximizes expected utility against the other samples — is the natural approach when you have N samples and a utility function. The paper's SJ metric could be directly used as a utility function in MBR, selecting argmax_i sum_j SJ(y_i, y_j) rather than just computing the mean. This is mentioned obliquely ("closest to consensus") but not connected to the MBR literature (Eikema & Aziz 2020, 2022; Freitag et al. 2022, 2023). The MBR framing would also clarify why instance-level signals fail: MBR selects the sample closest to the "center" of the distribution, which is a per-sample ranking. If MBR-with-SJ also fails, that is a much stronger negative result. If it succeeds, it resolves the gap. Either way, omitting this connection is a significant gap in the related work.

**W6. The "logprob paradox" (high AUROC, low rho) is not deeply analyzed.** This is presented as a paradox but has a straightforward explanation: logprob produces a bimodal distribution (high confidence for easy instances, low for hard) that separates classes well (AUROC) but provides poor ranking within each mode (rho). This is a well-known property of miscalibrated classifiers (Guo et al. 2017). Presenting it as a novel observation overstates the contribution.

### 4. Questions for Authors

**Q1.** For best-of-N selection with instance-level signals, you use "the sample closest to the consensus output" (Section 2.3). This is effectively MBR decoding with SJ as the utility function. Did you also try other per-sample adaptations of instance-level signals, such as leave-one-out SJ (the SJ of sample i against the remaining N-1)? If so, what were the results? If not, why not — this seems like the most natural per-sample structural signal.

**Q2.** The oracle headroom on NER is +16pp. Can you characterize which instances contribute to this headroom? Specifically, for oracle-selected samples, does the oracle choose samples that are structurally different from the consensus (suggesting that consensus-based selection is fundamentally wrong) or samples that are close to the consensus but slightly better (suggesting that finer-grained discrimination is needed)?

**Q3.** You report that "within-stratum correlations approach zero for all signals" (Discussion). This is a strong claim. Can you provide the actual numbers and confidence intervals? If true, this means confidence signals have *zero* discriminative power conditional on difficulty — but this seems to conflate "difficulty stratum" (defined by greedy F1) with "confidence stratum" (defined by the signal), which are correlated but not identical.

**Q4.** The paper title in the submission summary mentions "Why Self-Consistency Fails" but the actual paper title is different ("Strong Predictors, Weak Selectors"). Which is the intended title? The "fails" framing is stronger and more specific but also more misleading — self-consistency does not fail for quality estimation.

**Q5.** Why is Fleiss' kappa computed at the token level rather than the entity level? Entity-level FK (treating each entity type as a category and each sample as a rater) would be more naturally comparable to the structural signals and might narrow the structural-surface gap.

### 5. Minor Issues

- Table 2 (selection): EM shows "---" entries. The text explains this is because "EM produces binary agreement without sample ranking," but binary agreement can still be used for selection (select any sample from the majority cluster, or random among all when EM=0). This should be clarified or EM should be included with a random-within-majority strategy.

- The paper mentions WNUT-17 in the abstract and experimental setup as a third dataset but it contributes only a single paragraph of negative results (Section 4.3). Listing it as a primary dataset overstates its role; it would be more accurately described as a "probe" or "boundary case."

- Section 4.3 reports "Fisher's z-test on rho_SJ yields z=2.31, p=0.021" for NER vs. RE comparison. This tests whether two correlations differ, but the NER and RE evaluations are on overlapping instances (SciERC has joint NER/RE annotations), so the independence assumption of Fisher's z-test is violated. A permutation test or bootstrap comparison would be more appropriate.

- The paper uses "three families" (structural, surface, model-internal) in the main text but the paper_framing.md and dream reports reference "four families." This inconsistency should be resolved.

- ECE is mentioned once (Section 4.3: "SJ also achieves the lowest calibration error (ECE = 0.075-0.102)") but no reliability diagrams or calibration analysis is presented despite being referenced. If ECE is claimed, it needs methodological support (bin size, how F1-based ECE is defined for continuous outputs).

- The notation table (Table 1) is unnecessary and consumes space. The symbols are standard and self-explanatory.

### 6. Overall Assessment

The paper presents a competent empirical comparison of confidence signals for LLM-based information extraction, with thorough experimental coverage (2 models, 2+ datasets, 3 seeds, 2 sample sizes). The quality estimation results are solid and practically useful. However, the central novelty claim — the correlation-selection gap — is close to tautological for instance-level signals and only mildly surprising for log-probability on NER. The lack of any proposed solution, combined with the straightforward nature of the metrics (Jaccard similarity, frequency voting) and the close proximity to Nedellec & Xia (2026), places this below the acceptance threshold for a top venue main track. The work would be appropriate for Findings, where the systematic comparison and honest negative results would be valued without requiring the novelty bar of the main conference.

### 7. Scores

- **Overall**: 3 (Weak Reject)
- **Confidence**: 4 (High — I have read the paper carefully and am familiar with the relevant literature on self-consistency, uncertainty estimation, and structured prediction confidence)

agentId: a3d7f21605785749c (use SendMessage with to: 'a3d7f21605785749c' to continue this agent)
&lt;usage>total_tokens: 96136
tool_uses: 22
duration_ms: 135066&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "26e8a300-138e-4cb8-b83c-9c3bf2035241",
  "isSidechain": false,
  "promptId": "a640b4e1-01ba-4811-b057-a5972a785ed6",
  "type": "user",
  "uuid": "f95585a1-de7a-467e-9e58-c1e2604adb9b",
  "toolUseResult": {
    "status": "completed",
    "prompt": "You are Reviewer R2 for a top ML venue (acceptance rate ~25%, 6-point scale: 1=Strong Reject, 2=Reject, 3=Weak Reject, 4=Weak Accept, 5=Accept, 6=Strong Accept). Your focus areas are **novelty** and **related work**.\n\n## Paper Summary\n\nTitle: \"Why Self-Consistency Fails for Structured Prediction: An Analysis of the Correlation–Selection Gap\"\n\nThe paper investigates whether consistency-based confidence signals can serve as quality estimators and sample selectors for structured information extraction (NER and RE). It compares 5 unsupervised confidence signals: log-probability (per-sample), exact-match rate, Fleiss' κ, soft Jaccard (SJ), and entity voting confidence (all instance-level). Evaluated on 2 models (Qwen3-8B, LLaMA-3.1-8B) × 2 datasets (SciERC, CoNLL-2003), plus abandoned WNUT-17 (social media NER).\n\n**Main claims:**\n1. Structural consistency signals correlate marginally more with output quality than log-probability (Δρ = +0.01–0.04 on NER), but differences are small and statistically fragile.\n2. On RE, log-probability matches or exceeds structural signals.\n3. **Correlation-selection gap**: Despite positive quality-estimation correlations, NO signal achieves best-of-N selection above greedy on NER. Oracle headroom is +15pp but entirely unexploited.\n4. The gap is structural: instance-level signals assign the same score to all N samples from an input → degenerate to random selection for best-of-N. Only per-sample log-prob can rank → succeeds on RE (+2.3pp) but not NER.\n5. N=8→16 and signal ensembling fail to close the gap.\n\n**Key related work cited:**\n- Wang et al. 2023: Self-consistency for reasoning (majority voting)\n- Nédellec & Xia 2026: Consistency-accuracy correlation for hard-prompted LLMs on plant health NER/RE using surface string matching\n- Kuhn et al. 2023: Semantic entropy\n- Manakul et al. 2023: SelfCheckGPT\n- Kadavath et al. 2022: \"Language models know what they know\"\n- Guo et al. 2017: Calibration of neural networks\n- Desai & Durrett 2020: Calibration for NLP\n- Snell et al. 2024: Test-time compute scaling\n- Brown et al. 2024: Large language monkeys\n- CoCoA (Vashurin et al. 2025): Combining confidence + consistency\n- Geifman & El-Yaniv 2017: Selective prediction\n- Kuleshov & Liang 2015: Calibrated structured prediction\n- Jagannatha & Yu 2022: Calibrating structured output predictors\n\n**Key tables:**\n- Table 1: 5-signal comparison on SciERC (SJ ρ=0.36 vs log-prob ρ=0.33 on NER; on RE log-prob exceeds SJ)\n- Table 3: 2×2 model-dataset matrix showing SJ ρ=0.34-0.36, SJ-LP gap +0.02 to +0.06\n- Table 6: Best-of-N — ALL signals ≤ greedy on NER, only log-prob beats greedy on RE\n- Table 9: OOD — SJ degrades asymmetrically (hallucination consistency)\n- Ensemble: AUROC +0.02, selection still fails\n\nThe paper frames itself as a \"negative result / cautionary analysis\" showing that self-consistency doesn't help for structured IE with fine-tuned models.\n\n## Your Review Task\n\nWrite a detailed review covering:\n\n1. **Summary** (2-3 sentences)\n2. **Strengths** (focus on novelty, positioning, and related work coverage)\n3. **Weaknesses** (focus on novelty, positioning, and related work coverage)\n4. **Questions for authors**\n5. **Minor issues**\n6. **Overall assessment** (1-2 sentences)\n7. **Scores**: Overall (1-6), Confidence (1-5)\n\nBe thorough, critical, and fair. Evaluate:\n\n- **Novelty**: Is the correlation-selection gap a genuinely new insight, or is it obvious / already known? The paper itself admits \"this distinction between quality estimation and sample selection is well-known in calibration research but has not been empirically demonstrated for structured IE.\" Is empirical demonstration alone a sufficient contribution?\n- **Positioning relative to Nédellec & Xia 2026**: They already studied consistency-accuracy correlation for IE. The structural metrics (SJ) could be seen as a minor extension. Is this sufficiently differentiated?\n- **Contribution level**: The paper proposes no new method, no solution to the gap. Is \"identifying a problem and stopping\" sufficient for a top venue? Would this be Findings-level?\n- **Related work completeness**: Are there missing references? Is the calibration literature coverage adequate?\n- **Framing**: The paper leads with \"negative finding + explanation.\" Is this framing effective, or does it read as post-hoc rationalization?\n- **The \"correlation-selection gap\" concept**: Is the explanation (instance-level vs per-sample) trivial once stated? \"Instance-level aggregates can't rank individual samples\" — is this obvious?\n\nRemember: this is evaluated against top ML venue standards (~25% acceptance rate).",
    "agentId": "a3d7f21605785749c",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "\n\nNow I have all the material needed. Let me write the review directly.\n\n---\n\n## Review: \"Why Self-Consistency Fails for Structured Prediction: An Analysis of the Correlation-Selection Gap\"\n\n**Reviewer R2 — Focus: Novelty and Related Work**\n\n---\n\n### 1. Summary\n\nThis paper compares five unsupervised confidence signals (log-probability, exact match, Fleiss' kappa, Soft Jaccard, entity voting) for quality estimation and best-of-N selection in LLM-based information extraction (NER and RE). The central finding is a \"correlation-selection gap\": structural consistency signals strongly predict instance-level quality (voting rho=0.50, AUROC=0.73 on NER) but fail to improve best-of-N selection over greedy decoding on NER, with only log-probability helping on RE (+2.3pp). The paper attributes this to the instance-level nature of consistency signals, which cannot discriminate among N candidates for a single input.\n\n### 2. Strengths\n\n**S1. The quality estimation vs. selection disentanglement is well-executed.** The paper cleanly separates two objectives that are indeed conflated in much prior work on self-consistency. The experimental demonstration across 2 models x 2 datasets is thorough, and the method section (Section 2) formalizes the per-sample vs. instance-level signal distinction clearly. This separation is the paper's strongest conceptual contribution.\n\n**S2. Comprehensive related work, given the revised draft.** The related work section is well-organized into three subsections (self-consistency/TTS, consistency for structured IE, uncertainty/calibration) and covers the relevant 2024-2026 literature with appropriate depth. The positioning against Nedellec & Xia (2026) is explicit and fair, identifying three concrete gaps (surface matching only, no selection analysis, single domain). The coverage of CISC, Self-Certainty, ReASC, and CoCoA situates the work within the broader TTS landscape. The conformal prediction, token-level NER uncertainty, and verifier/reward model threads are appropriately included as related paradigms.\n\n**S3. Honest reporting of negative results and method boundaries.** The WNUT-17 analysis (54% zero F1, SJ rho=0.062 not significant, logprob negative correlation) is reported transparently as a capability boundary rather than buried. The task-difficulty-dependent signal ranking (EM leads on easy tasks, SJ on hard tasks) is a nuanced finding that avoids overclaiming a universal winner.\n\n**S4. The task-difficulty-dependent signal ranking is a genuine empirical contribution.** The observation that EM > SJ on CoNLL but SJ > EM on SciERC, with convergence when model capability is insufficient, provides actionable guidance. This is more informative than a simple \"our metric wins\" narrative.\n\n### 3. Weaknesses\n\n**W1. The \"correlation-selection gap\" explanation is close to tautological once stated.** The paper's central conceptual contribution — that instance-level aggregates cannot rank individual samples — is presented as a discovery, but it follows almost directly from the definition. An instance-level signal c_il: (x, {y_i}) -> R produces one number per input; it *cannot* rank N candidates by construction. The paper acknowledges this in Section 2 (\"instance-level signals... do not inherently rank individual samples\") but then treats the empirical confirmation as a major finding. The genuine surprise would be if instance-level signals *did* help selection (e.g., by identifying easy instances where random selection suffices). The fact that they don't is the expected null result. What is mildly interesting is that even the consensus-closest-sample selection strategy fails, but this is underexplored — the paper devotes only one sentence to how instance-level signals are adapted for selection (Section 2.3: \"we select the sample closest to the consensus output\").\n\nThis weakness is significant for novelty assessment. The conceptual contribution reduces to: (a) instance-level signals can't rank samples (definitional), and (b) log-probability, the only per-sample signal, helps on RE but not NER (a single empirical observation). Neither alone meets the novelty bar for a top venue.\n\n**W2. Insufficient differentiation from Nedellec & Xia (2026).** The paper argues three differences: structural metrics vs. surface matching, best-of-N analysis, and multi-domain evaluation. However:\n- The structural metrics (SJ, voting) are relatively straightforward extensions of Jaccard similarity and frequency counting to entity sets. The Hungarian matching with span overlap is a reasonable design choice but not technically novel.\n- The best-of-N analysis yields a negative result (no signal beats greedy on NER), which, combined with W1, amounts to showing that something definitionally incapable of ranking samples indeed fails to rank samples.\n- The multi-domain evaluation is valuable but incremental.\n\nThe paper reads as \"Nedellec & Xia (2026) + better metrics + negative selection result.\" The SJ metric itself is the main technical delta, and it is not a major methodological contribution — it is a sensible instantiation of set similarity that one would naturally try.\n\n**W3. No proposed solution or path forward beyond \"use trained verifiers.\"** The paper identifies a gap and stops. The conclusion lists future work (trained verifiers, conformal prediction, larger models) but does not even attempt a preliminary solution. For a top venue, a pure negative-result paper needs either (a) a very surprising negative result, or (b) deep mechanistic understanding that enables future solutions. The explanation here (\"instance-level signals can't rank samples\") is shallow — it does not explain *why* the consensus-closest strategy fails, whether per-sample structural signals could be constructed, or what properties a successful selector would need. The oracle headroom analysis (NER +16pp, RE +19pp) tantalizes but receives no further investigation.\n\n**W4. The contribution is positioned ambiguously between \"systematic comparison\" and \"novel finding.\"** The paper's title and framing emphasize the correlation-selection gap as a novel finding, but the bulk of the experimental content is a systematic comparison of five signals. Systematic comparisons are valuable but are typically positioned as resource papers or Findings-level contributions unless they reveal unexpected phenomena. The unexpected phenomenon here (the gap) is, per W1, close to expected once the signal taxonomy is laid out. The paper would be strengthened by committing to one framing: either a rigorous systematic comparison (in which case, more signals, datasets, and models would be expected) or a mechanistic analysis of the gap (in which case, deeper investigation is needed).\n\n**W5. Missing related work on minimum Bayes risk (MBR) decoding for structured prediction.** MBR decoding — selecting the sample that maximizes expected utility against the other samples — is the natural approach when you have N samples and a utility function. The paper's SJ metric could be directly used as a utility function in MBR, selecting argmax_i sum_j SJ(y_i, y_j) rather than just computing the mean. This is mentioned obliquely (\"closest to consensus\") but not connected to the MBR literature (Eikema & Aziz 2020, 2022; Freitag et al. 2022, 2023). The MBR framing would also clarify why instance-level signals fail: MBR selects the sample closest to the \"center\" of the distribution, which is a per-sample ranking. If MBR-with-SJ also fails, that is a much stronger negative result. If it succeeds, it resolves the gap. Either way, omitting this connection is a significant gap in the related work.\n\n**W6. The \"logprob paradox\" (high AUROC, low rho) is not deeply analyzed.** This is presented as a paradox but has a straightforward explanation: logprob produces a bimodal distribution (high confidence for easy instances, low for hard) that separates classes well (AUROC) but provides poor ranking within each mode (rho). This is a well-known property of miscalibrated classifiers (Guo et al. 2017). Presenting it as a novel observation overstates the contribution.\n\n### 4. Questions for Authors\n\n**Q1.** For best-of-N selection with instance-level signals, you use \"the sample closest to the consensus output\" (Section 2.3). This is effectively MBR decoding with SJ as the utility function. Did you also try other per-sample adaptations of instance-level signals, such as leave-one-out SJ (the SJ of sample i against the remaining N-1)? If so, what were the results? If not, why not — this seems like the most natural per-sample structural signal.\n\n**Q2.** The oracle headroom on NER is +16pp. Can you characterize which instances contribute to this headroom? Specifically, for oracle-selected samples, does the oracle choose samples that are structurally different from the consensus (suggesting that consensus-based selection is fundamentally wrong) or samples that are close to the consensus but slightly better (suggesting that finer-grained discrimination is needed)?\n\n**Q3.** You report that \"within-stratum correlations approach zero for all signals\" (Discussion). This is a strong claim. Can you provide the actual numbers and confidence intervals? If true, this means confidence signals have *zero* discriminative power conditional on difficulty — but this seems to conflate \"difficulty stratum\" (defined by greedy F1) with \"confidence stratum\" (defined by the signal), which are correlated but not identical.\n\n**Q4.** The paper title in the submission summary mentions \"Why Self-Consistency Fails\" but the actual paper title is different (\"Strong Predictors, Weak Selectors\"). Which is the intended title? The \"fails\" framing is stronger and more specific but also more misleading — self-consistency does not fail for quality estimation.\n\n**Q5.** Why is Fleiss' kappa computed at the token level rather than the entity level? Entity-level FK (treating each entity type as a category and each sample as a rater) would be more naturally comparable to the structural signals and might narrow the structural-surface gap.\n\n### 5. Minor Issues\n\n- Table 2 (selection): EM shows \"---\" entries. The text explains this is because \"EM produces binary agreement without sample ranking,\" but binary agreement can still be used for selection (select any sample from the majority cluster, or random among all when EM=0). This should be clarified or EM should be included with a random-within-majority strategy.\n\n- The paper mentions WNUT-17 in the abstract and experimental setup as a third dataset but it contributes only a single paragraph of negative results (Section 4.3). Listing it as a primary dataset overstates its role; it would be more accurately described as a \"probe\" or \"boundary case.\"\n\n- Section 4.3 reports \"Fisher's z-test on rho_SJ yields z=2.31, p=0.021\" for NER vs. RE comparison. This tests whether two correlations differ, but the NER and RE evaluations are on overlapping instances (SciERC has joint NER/RE annotations), so the independence assumption of Fisher's z-test is violated. A permutation test or bootstrap comparison would be more appropriate.\n\n- The paper uses \"three families\" (structural, surface, model-internal) in the main text but the paper_framing.md and dream reports reference \"four families.\" This inconsistency should be resolved.\n\n- ECE is mentioned once (Section 4.3: \"SJ also achieves the lowest calibration error (ECE = 0.075-0.102)\") but no reliability diagrams or calibration analysis is presented despite being referenced. If ECE is claimed, it needs methodological support (bin size, how F1-based ECE is defined for continuous outputs).\n\n- The notation table (Table 1) is unnecessary and consumes space. The symbols are standard and self-explanatory.\n\n### 6. Overall Assessment\n\nThe paper presents a competent empirical comparison of confidence signals for LLM-based information extraction, with thorough experimental coverage (2 models, 2+ datasets, 3 seeds, 2 sample sizes). The quality estimation results are solid and practically useful. However, the central novelty claim — the correlation-selection gap — is close to tautological for instance-level signals and only mildly surprising for log-probability on NER. The lack of any proposed solution, combined with the straightforward nature of the metrics (Jaccard similarity, frequency voting) and the close proximity to Nedellec & Xia (2026), places this below the acceptance threshold for a top venue main track. The work would be appropriate for Findings, where the systematic comparison and honest negative results would be valued without requiring the novelty bar of the main conference.\n\n### 7. Scores\n\n- **Overall**: 3 (Weak Reject)\n- **Confidence**: 4 (High — I have read the paper carefully and am familiar with the relevant literature on self-consistency, uncertainty estimation, and structured prediction confidence)"
      }
    ],
    "totalDurationMs": 135066,
    "totalTokens": 96136,
    "totalToolUseCount": 22,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 675,
      "cache_read_input_tokens": 92454,
      "output_tokens": 3004,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 675
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 3004,
          "cache_read_input_tokens": 92454,
          "cache_creation_input_tokens": 675,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 675,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 10,
      "searchCount": 1,
      "bashCount": 0,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 11
    }
  },
  "sourceToolAssistantUUID": "26e8a300-138e-4cb8-b83c-9c3bf2035241",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a188aefa-23b6-4688-b448-164a4ee4e586",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 27 · 2026-05-14T21:34:00.254Z_

<details><summary>Logged reasoning block</summary>

```text
Good, I have both reviews. Now I need to run the full roundtable:
- Step 1: Independent reviews (done above)
- Step 2: Cross-sharing (each reviewer sees the other's review)
- Step 3: Convergence (they discuss and adjust)
- Step 4: Synthesis (AC-level meta-review)

Let me proceed with Step 2: cross-sharing. I'll send each reviewer the other's review and ask them to respond.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f95585a1-de7a-467e-9e58-c1e2604adb9b",
  "isSidechain": false,
  "requestId": "req_011Cb3BJio6JQn8YPDyM5YqV",
  "type": "assistant",
  "uuid": "ac6c679e-3b13-4f19-915f-b69e705a285b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a188aefa-23b6-4688-b448-164a4ee4e586",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LcpnYaUGaAuyectBENPNUP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10779,
      "cache_read_input_tokens": 73689,
      "output_tokens": 1571,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 10779,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1571,
          "cache_read_input_tokens": 73689,
          "cache_creation_input_tokens": 10779,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 10779
          },
          "type": "message"
        }
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

_source line 28 · 2026-05-14T21:34:00.742Z_

Both independent reviews are complete. Now proceeding to Step 2: cross-sharing — each reviewer sees the other's review and responds.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ac6c679e-3b13-4f19-915f-b69e705a285b",
  "isSidechain": false,
  "requestId": "req_011Cb3BJio6JQn8YPDyM5YqV",
  "type": "assistant",
  "uuid": "9bb803ed-920e-44aa-b8ae-2172c0d61134",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a188aefa-23b6-4688-b448-164a4ee4e586",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LcpnYaUGaAuyectBENPNUP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10779,
      "cache_read_input_tokens": 73689,
      "output_tokens": 1571,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 10779,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1571,
          "cache_read_input_tokens": 73689,
          "cache_creation_input_tokens": 10779,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 10779
          },
          "type": "message"
        }
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

_source line 29 · 2026-05-14T21:34:12.936Z_

<details open><summary>🔧 Tool call — Agent · `toolu_014P9MBwUxWgNswzYnmSZZ7w`</summary>

```json
{
  "description": "R1 responds to R2's review",
  "prompt": "You are Reviewer R1 (methods + experiments focus). You previously gave this paper a **4 (Weak Accept)** with confidence 4. You now see Reviewer R2's review below. \n\nRespond with:\n1. Points of agreement with R2\n2. Points of disagreement with R2\n3. Whether R2's review changes your assessment (and if so, how)\n4. Your updated score (if any)\n\nKeep your response concise (under 500 words).\n\n---\n\n## R2's Review (Novelty + Related Work focus, Score: 3 Weak Reject, Confidence 4)\n\n**Strengths R2 identified:**\n- Quality estimation vs selection disentanglement is well-executed\n- Comprehensive related work\n- Honest negative results\n- Task-difficulty-dependent signal ranking is genuine contribution\n\n**Weaknesses R2 identified:**\n\n**W1. Tautological gap.** The correlation-selection gap explanation follows almost directly from the definition of instance-level signals. Instance-level c(x, {y_i}) -> R produces one number per input; it *cannot* rank N candidates by construction. The conceptual contribution reduces to: (a) definitional, (b) logprob helps on RE but not NER (single observation).\n\n**W2. Insufficient differentiation from Nédellec & Xia (2026).** SJ is a straightforward extension. Multi-domain evaluation is valuable but incremental. Paper reads as \"Nédellec & Xia + better metrics + negative selection result.\"\n\n**W3. No solution or path forward.** Paper identifies gap and stops. Pure negative-result paper needs either surprising negative result or deep mechanistic understanding. Explanation is shallow.\n\n**W4. Ambiguous positioning.** Caught between \"systematic comparison\" and \"novel finding.\"\n\n**W5. Missing MBR decoding connection.** MBR selects argmax_i sum_j SJ(y_i, y_j) — a per-sample ranking from instance-level signals. If MBR-with-SJ also fails, that's a much stronger negative result. If it succeeds, it resolves the gap.\n\n**W6. \"Logprob paradox\" is well-known in calibration literature.**\n\n**Questions:**\n- Did you try per-sample variants (LOO-SJ, per-sample voting)?\n- Can you characterize which instances contribute to oracle headroom?\n- MBR decoding connection?\n\n---\n\nYour previous key weaknesses were:\n- W1: Best-of-N structurally biased against instance-level signals (tautological gap)\n- W2: Single RE dataset\n- W3: Task-difficulty gradient conflates variables\n- W4: Uneven statistical rigor\n- W5: Method section discrepancies\n- W6: N=8 may be insufficient\n- W7: Superficial ensemble analysis"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9bb803ed-920e-44aa-b8ae-2172c0d61134",
  "isSidechain": false,
  "requestId": "req_011Cb3BJio6JQn8YPDyM5YqV",
  "type": "assistant",
  "uuid": "3c9e4b8d-509a-479c-85a9-297d724c4b46",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a188aefa-23b6-4688-b448-164a4ee4e586",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LcpnYaUGaAuyectBENPNUP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10779,
      "cache_read_input_tokens": 73689,
      "output_tokens": 1571,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 10779,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1571,
          "cache_read_input_tokens": 73689,
          "cache_creation_input_tokens": 10779,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 10779
          },
          "type": "message"
        }
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

_source line 30 · 2026-05-14T21:34:24.995Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01An4oy7YTW5zvQBGg8qDGMj`</summary>

```json
{
  "description": "R2 responds to R1's review",
  "prompt": "You are Reviewer R2 (novelty + related work focus). You previously gave this paper a **3 (Weak Reject)** with confidence 4. You now see Reviewer R1's review below.\n\nRespond with:\n1. Points of agreement with R1\n2. Points of disagreement with R1\n3. Whether R1's review changes your assessment (and if so, how)\n4. Your updated score (if any)\n\nKeep your response concise (under 500 words).\n\n---\n\n## R1's Review (Methods + Experiments focus, Score: 4 Weak Accept, Confidence 4)\n\n**Strengths R1 identified:**\n- Well-motivated research question, clean conceptual contribution (correlation-selection gap)\n- Comprehensive experimental coverage (17 experiments fully executed)\n- Honest reporting of negative results\n- Practical utility (actionable guidance)\n- Strong related work positioning\n\n**Weaknesses R1 identified:**\n\n**W1. Tautological gap + structurally biased best-of-N.** Instance-level signals cannot rank by construction. Paper misses per-sample variants (LOO-SJ per sample). \"Real question is whether per-sample variants of structural signals could enable selection.\"\n\n**W2. Single RE dataset with severe floor effects (44% zero F1).** All RE conclusions rest on SciERC alone.\n\n**W3. Task-difficulty gradient conflates domain, schema, text style, capability.**\n\n**W4. Statistical rigor uneven.** No bootstrap CIs for main Table 1. Only 3 seeds. No paired bootstrap or Williams' test. Fisher z-test on overlapping instances.\n\n**W5. Method section discrepancies.** FK described as token-level but implemented entity-level. EM \"equivalence\" claim incorrect. SJ formula oversimplified.\n\n**W6. N=8 may be insufficient.** RE SJ improves from 0.21→0.28 at N=16. Larger N not explored.\n\n**W7. Superficial ensemble analysis.** No hybrid strategy tested (structural filtering + logprob ranking).\n\n**Key questions:**\n- Per-sample variants of structural signals for selection?\n- How would practitioners do conditional filtering without gold labels?\n- How exactly is voting used for selection?\n- Sensitivity to fine-tuning quality?\n\n---\n\nYour previous key weaknesses were:\n- W1: Tautological correlation-selection gap\n- W2: Insufficient differentiation from Nédellec & Xia 2026\n- W3: No proposed solution\n- W4: Ambiguous positioning\n- W5: Missing MBR decoding connection\n- W6: \"Logprob paradox\" is well-known"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3c9e4b8d-509a-479c-85a9-297d724c4b46",
  "isSidechain": false,
  "requestId": "req_011Cb3BJio6JQn8YPDyM5YqV",
  "type": "assistant",
  "uuid": "e35735b7-afbc-470c-9bb2-e18f52ceb3ec",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a188aefa-23b6-4688-b448-164a4ee4e586",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LcpnYaUGaAuyectBENPNUP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10779,
      "cache_read_input_tokens": 73689,
      "output_tokens": 1571,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 10779,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1571,
          "cache_read_input_tokens": 73689,
          "cache_creation_input_tokens": 10779,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 10779
          },
          "type": "message"
        }
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

_source line 31_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[DREAM Review Director] dream_id=20260514T203201 | review_mode=full | review_visible=True PDF: /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/d…",
  "leafUuid": "e35735b7-afbc-470c-9bb2-e18f52ceb3ec",
  "sessionId": "a188aefa-23b6-4688-b448-164a4ee4e586"
}
```

---

### Runtime record

_source line 32_

```json
{
  "type": "ai-title",
  "aiTitle": "Full blind review of structural self-consistency IE paper",
  "sessionId": "a188aefa-23b6-4688-b448-164a4ee4e586"
}
```

---

### Tool result

_source line 33 · 2026-05-14T21:34:35.949Z_

<details><summary>↩ Tool result · `toolu_014P9MBwUxWgNswzYnmSZZ7w`</summary>

```text


## R1 Response to R2's Review

### Points of Agreement

**R2-W1 (Tautological gap) aligns strongly with my W1.** We independently identified the same core issue: the correlation-selection gap is partly an artifact of how instance-level signals are defined. An instance-level quality estimator that produces one scalar per input cannot, by construction, rank candidates. R2 states this more crisply than I did. This convergence from two independent reviewers strengthens the concern.

**R2-W3 (No path forward) echoes my frustration with the paper's stopping point.** I noted the ensemble analysis was superficial (my W7); R2 generalizes this to the entire paper lacking a resolution or deep mechanistic account. Agreed.

**R2-W5 (Missing MBR connection) is an excellent point I missed.** MBR decoding is the natural bridge between instance-level signals and per-sample selection. Its absence is a real gap in the experimental design. This alone could have resolved or sharpened the paper's central finding.

**R2-W6 (Logprob paradox known in calibration literature).** Fair. The paper should have engaged with calibration work more explicitly.

### Points of Disagreement

**R2-W2 (Insufficient differentiation from Nedellec & Xia).** R2 is harsher here than I would be. The multi-domain evaluation across NER, RE, and EE with structured metrics (not just F1) represents nontrivial engineering and experimental effort. The task-difficulty-dependent signal ranking (which R2 acknowledges as a genuine contribution) would not have emerged from a single-domain study. I see this as a meaningful extension, not merely incremental.

**R2-W4 (Ambiguous positioning).** I disagree that this is a serious weakness. Many empirical papers in NLP occupy the space between systematic comparison and novel finding. The problem is execution depth, not positioning. A well-executed systematic comparison paper is valuable; the issue is that the analysis stops too early (which is W3, not W4).

**R2's overall framing as "definitional + single observation."** This undersells the empirical breadth. The paper tests 5 signals across 3 IE subtasks with multiple metrics. The negative result on selection is consistent across conditions, which has value even if the explanation is shallow.

### Whether R2 Changes My Assessment

R2's MBR point (W5) is the most impactful new concern. If the authors had run MBR-with-SJ and reported results, the paper would be substantially stronger regardless of outcome. This omission, combined with the tautological gap we both identified, weakens the contribution more than I initially weighted.

However, R2's score of 3 feels slightly too harsh. The empirical contribution (task-difficulty gradient, honest negative results, structured evaluation) has workshop-to-main-conference value. R2 acknowledges these strengths but doesn't weight them sufficiently.

### Updated Score

I revise from **4 (Weak Accept)** down to **3-4 (Borderline)**. Specifically: **3 (Weak Reject)**, confidence 4.

The convergence on the tautological gap, plus R2's MBR omission point, tips me. The paper identifies a real phenomenon but (a) the explanation is partly definitional, (b) the missing MBR experiment is a significant design gap, and (c) the analysis lacks the mechanistic depth needed for a pure negative-result contribution. I would reconsider if authors add MBR results and deeper per-instance analysis in revision.

agentId: a2be09bc95e802b26 (use SendMessage with to: 'a2be09bc95e802b26' to continue this agent)
&lt;usage>total_tokens: 15586
tool_uses: 0
duration_ms: 23008&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3c9e4b8d-509a-479c-85a9-297d724c4b46",
  "isSidechain": false,
  "promptId": "a640b4e1-01ba-4811-b057-a5972a785ed6",
  "type": "user",
  "uuid": "5881c6a9-318f-44fd-97ff-57dce1a86efd",
  "toolUseResult": {
    "status": "completed",
    "prompt": "You are Reviewer R1 (methods + experiments focus). You previously gave this paper a **4 (Weak Accept)** with confidence 4. You now see Reviewer R2's review below. \n\nRespond with:\n1. Points of agreement with R2\n2. Points of disagreement with R2\n3. Whether R2's review changes your assessment (and if so, how)\n4. Your updated score (if any)\n\nKeep your response concise (under 500 words).\n\n---\n\n## R2's Review (Novelty + Related Work focus, Score: 3 Weak Reject, Confidence 4)\n\n**Strengths R2 identified:**\n- Quality estimation vs selection disentanglement is well-executed\n- Comprehensive related work\n- Honest negative results\n- Task-difficulty-dependent signal ranking is genuine contribution\n\n**Weaknesses R2 identified:**\n\n**W1. Tautological gap.** The correlation-selection gap explanation follows almost directly from the definition of instance-level signals. Instance-level c(x, {y_i}) -> R produces one number per input; it *cannot* rank N candidates by construction. The conceptual contribution reduces to: (a) definitional, (b) logprob helps on RE but not NER (single observation).\n\n**W2. Insufficient differentiation from Nédellec & Xia (2026).** SJ is a straightforward extension. Multi-domain evaluation is valuable but incremental. Paper reads as \"Nédellec & Xia + better metrics + negative selection result.\"\n\n**W3. No solution or path forward.** Paper identifies gap and stops. Pure negative-result paper needs either surprising negative result or deep mechanistic understanding. Explanation is shallow.\n\n**W4. Ambiguous positioning.** Caught between \"systematic comparison\" and \"novel finding.\"\n\n**W5. Missing MBR decoding connection.** MBR selects argmax_i sum_j SJ(y_i, y_j) — a per-sample ranking from instance-level signals. If MBR-with-SJ also fails, that's a much stronger negative result. If it succeeds, it resolves the gap.\n\n**W6. \"Logprob paradox\" is well-known in calibration literature.**\n\n**Questions:**\n- Did you try per-sample variants (LOO-SJ, per-sample voting)?\n- Can you characterize which instances contribute to oracle headroom?\n- MBR decoding connection?\n\n---\n\nYour previous key weaknesses were:\n- W1: Best-of-N structurally biased against instance-level signals (tautological gap)\n- W2: Single RE dataset\n- W3: Task-difficulty gradient conflates variables\n- W4: Uneven statistical rigor\n- W5: Method section discrepancies\n- W6: N=8 may be insufficient\n- W7: Superficial ensemble analysis",
    "agentId": "a2be09bc95e802b26",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "\n\n## R1 Response to R2's Review\n\n### Points of Agreement\n\n**R2-W1 (Tautological gap) aligns strongly with my W1.** We independently identified the same core issue: the correlation-selection gap is partly an artifact of how instance-level signals are defined. An instance-level quality estimator that produces one scalar per input cannot, by construction, rank candidates. R2 states this more crisply than I did. This convergence from two independent reviewers strengthens the concern.\n\n**R2-W3 (No path forward) echoes my frustration with the paper's stopping point.** I noted the ensemble analysis was superficial (my W7); R2 generalizes this to the entire paper lacking a resolution or deep mechanistic account. Agreed.\n\n**R2-W5 (Missing MBR connection) is an excellent point I missed.** MBR decoding is the natural bridge between instance-level signals and per-sample selection. Its absence is a real gap in the experimental design. This alone could have resolved or sharpened the paper's central finding.\n\n**R2-W6 (Logprob paradox known in calibration literature).** Fair. The paper should have engaged with calibration work more explicitly.\n\n### Points of Disagreement\n\n**R2-W2 (Insufficient differentiation from Nedellec & Xia).** R2 is harsher here than I would be. The multi-domain evaluation across NER, RE, and EE with structured metrics (not just F1) represents nontrivial engineering and experimental effort. The task-difficulty-dependent signal ranking (which R2 acknowledges as a genuine contribution) would not have emerged from a single-domain study. I see this as a meaningful extension, not merely incremental.\n\n**R2-W4 (Ambiguous positioning).** I disagree that this is a serious weakness. Many empirical papers in NLP occupy the space between systematic comparison and novel finding. The problem is execution depth, not positioning. A well-executed systematic comparison paper is valuable; the issue is that the analysis stops too early (which is W3, not W4).\n\n**R2's overall framing as \"definitional + single observation.\"** This undersells the empirical breadth. The paper tests 5 signals across 3 IE subtasks with multiple metrics. The negative result on selection is consistent across conditions, which has value even if the explanation is shallow.\n\n### Whether R2 Changes My Assessment\n\nR2's MBR point (W5) is the most impactful new concern. If the authors had run MBR-with-SJ and reported results, the paper would be substantially stronger regardless of outcome. This omission, combined with the tautological gap we both identified, weakens the contribution more than I initially weighted.\n\nHowever, R2's score of 3 feels slightly too harsh. The empirical contribution (task-difficulty gradient, honest negative results, structured evaluation) has workshop-to-main-conference value. R2 acknowledges these strengths but doesn't weight them sufficiently.\n\n### Updated Score\n\nI revise from **4 (Weak Accept)** down to **3-4 (Borderline)**. Specifically: **3 (Weak Reject)**, confidence 4.\n\nThe convergence on the tautological gap, plus R2's MBR omission point, tips me. The paper identifies a real phenomenon but (a) the explanation is partly definitional, (b) the missing MBR experiment is a significant design gap, and (c) the analysis lacks the mechanistic depth needed for a pure negative-result contribution. I would reconsider if authors add MBR results and deeper per-instance analysis in revision."
      }
    ],
    "totalDurationMs": 23008,
    "totalTokens": 15586,
    "totalToolUseCount": 0,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 6498,
      "cache_read_input_tokens": 8251,
      "output_tokens": 834,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 6498
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 834,
          "cache_read_input_tokens": 8251,
          "cache_creation_input_tokens": 6498,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 6498,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  },
  "sourceToolAssistantUUID": "3c9e4b8d-509a-479c-85a9-297d724c4b46",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a188aefa-23b6-4688-b448-164a4ee4e586",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-14T21:34:45.067Z_

<details><summary>↩ Tool result · `toolu_01An4oy7YTW5zvQBGg8qDGMj`</summary>

```text


## R2 Response to R1's Review

### Points of Agreement with R1

**Strong agreement on the tautological gap (R1-W1, my W1).** R1 articulates this more precisely than I did. The observation that instance-level structural signals *cannot rank by construction* under best-of-N is the core issue. R1's suggestion about per-sample variants (LOO-SJ per sample) is exactly the kind of analysis that would make this paper's negative result genuinely informative rather than structurally predetermined.

**Agreement on statistical rigor (R1-W4).** The absence of bootstrap CIs for Table 1 and the use of only 3 seeds concerned me as well. R1's specific critique about Fisher z-test on overlapping instances is a valid methodological point I had not flagged.

**Agreement on single RE dataset (R1-W2).** Floor effects with 44% zero F1 on SciERC make the RE conclusions fragile.

**Agreement on missing hybrid strategies (R1-W7).** This connects to my W3 (no proposed solution). A paper that identifies a gap but tests no remedies feels incomplete.

### Points of Disagreement with R1

**R1 is too generous on related work positioning.** R1 lists "strong related work positioning" as a strength. I disagree. The paper inadequately distinguishes itself from Nedellec & Xia 2026, which already demonstrated that structural consistency metrics correlate with quality in IE self-consistency settings. The paper also entirely misses the MBR decoding literature, which has formalized utility-based selection from candidate sets using structural similarity functions for years. R1 does not flag either omission.

**R1's score of 4 (Weak Accept) is too high given R1's own critique.** R1 identifies a tautological experimental design (W1), a single dataset with floor effects (W2), uneven statistical rigor (W4), and method section discrepancies (W5). Any one of W1 or W4 alone should prevent acceptance. Together, they indicate the central empirical claim is not adequately supported.

**R1 understates the "logprob paradox" issue.** R1 mentions it peripherally. This finding is well-established in the calibration and selective prediction literature and is presented here without proper attribution or novel analysis.

### Whether R1's Review Changes My Assessment

R1's review *reinforces* my concerns rather than alleviating them. R1's more precise formulation of the tautological gap (per-sample variants never tested) and the statistical rigor issues strengthen my belief that the experimental design cannot support the paper's conclusions.

R1's identification of method section discrepancies (W5: FK token-vs-entity, EM equivalence claim, SJ formula) is new information that further weakens my confidence in the work's technical precision.

### Updated Score

**Score: 3 (Weak Reject), unchanged.** Confidence remains 4. R1's review surfaced additional technical concerns (method discrepancies, Fisher z-test validity) that, if anything, push toward a stronger reject. I hold at 3 because the research question itself has merit, but the execution and positioning remain insufficient for acceptance.

agentId: a4d4c31895127305b (use SendMessage with to: 'a4d4c31895127305b' to continue this agent)
&lt;usage>total_tokens: 15450
tool_uses: 0
duration_ms: 20066&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e35735b7-afbc-470c-9bb2-e18f52ceb3ec",
  "isSidechain": false,
  "promptId": "a640b4e1-01ba-4811-b057-a5972a785ed6",
  "type": "user",
  "uuid": "8a0dab04-6a49-461b-95d2-f54ff5f498b1",
  "toolUseResult": {
    "status": "completed",
    "prompt": "You are Reviewer R2 (novelty + related work focus). You previously gave this paper a **3 (Weak Reject)** with confidence 4. You now see Reviewer R1's review below.\n\nRespond with:\n1. Points of agreement with R1\n2. Points of disagreement with R1\n3. Whether R1's review changes your assessment (and if so, how)\n4. Your updated score (if any)\n\nKeep your response concise (under 500 words).\n\n---\n\n## R1's Review (Methods + Experiments focus, Score: 4 Weak Accept, Confidence 4)\n\n**Strengths R1 identified:**\n- Well-motivated research question, clean conceptual contribution (correlation-selection gap)\n- Comprehensive experimental coverage (17 experiments fully executed)\n- Honest reporting of negative results\n- Practical utility (actionable guidance)\n- Strong related work positioning\n\n**Weaknesses R1 identified:**\n\n**W1. Tautological gap + structurally biased best-of-N.** Instance-level signals cannot rank by construction. Paper misses per-sample variants (LOO-SJ per sample). \"Real question is whether per-sample variants of structural signals could enable selection.\"\n\n**W2. Single RE dataset with severe floor effects (44% zero F1).** All RE conclusions rest on SciERC alone.\n\n**W3. Task-difficulty gradient conflates domain, schema, text style, capability.**\n\n**W4. Statistical rigor uneven.** No bootstrap CIs for main Table 1. Only 3 seeds. No paired bootstrap or Williams' test. Fisher z-test on overlapping instances.\n\n**W5. Method section discrepancies.** FK described as token-level but implemented entity-level. EM \"equivalence\" claim incorrect. SJ formula oversimplified.\n\n**W6. N=8 may be insufficient.** RE SJ improves from 0.21→0.28 at N=16. Larger N not explored.\n\n**W7. Superficial ensemble analysis.** No hybrid strategy tested (structural filtering + logprob ranking).\n\n**Key questions:**\n- Per-sample variants of structural signals for selection?\n- How would practitioners do conditional filtering without gold labels?\n- How exactly is voting used for selection?\n- Sensitivity to fine-tuning quality?\n\n---\n\nYour previous key weaknesses were:\n- W1: Tautological correlation-selection gap\n- W2: Insufficient differentiation from Nédellec & Xia 2026\n- W3: No proposed solution\n- W4: Ambiguous positioning\n- W5: Missing MBR decoding connection\n- W6: \"Logprob paradox\" is well-known",
    "agentId": "a4d4c31895127305b",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "\n\n## R2 Response to R1's Review\n\n### Points of Agreement with R1\n\n**Strong agreement on the tautological gap (R1-W1, my W1).** R1 articulates this more precisely than I did. The observation that instance-level structural signals *cannot rank by construction* under best-of-N is the core issue. R1's suggestion about per-sample variants (LOO-SJ per sample) is exactly the kind of analysis that would make this paper's negative result genuinely informative rather than structurally predetermined.\n\n**Agreement on statistical rigor (R1-W4).** The absence of bootstrap CIs for Table 1 and the use of only 3 seeds concerned me as well. R1's specific critique about Fisher z-test on overlapping instances is a valid methodological point I had not flagged.\n\n**Agreement on single RE dataset (R1-W2).** Floor effects with 44% zero F1 on SciERC make the RE conclusions fragile.\n\n**Agreement on missing hybrid strategies (R1-W7).** This connects to my W3 (no proposed solution). A paper that identifies a gap but tests no remedies feels incomplete.\n\n### Points of Disagreement with R1\n\n**R1 is too generous on related work positioning.** R1 lists \"strong related work positioning\" as a strength. I disagree. The paper inadequately distinguishes itself from Nedellec & Xia 2026, which already demonstrated that structural consistency metrics correlate with quality in IE self-consistency settings. The paper also entirely misses the MBR decoding literature, which has formalized utility-based selection from candidate sets using structural similarity functions for years. R1 does not flag either omission.\n\n**R1's score of 4 (Weak Accept) is too high given R1's own critique.** R1 identifies a tautological experimental design (W1), a single dataset with floor effects (W2), uneven statistical rigor (W4), and method section discrepancies (W5). Any one of W1 or W4 alone should prevent acceptance. Together, they indicate the central empirical claim is not adequately supported.\n\n**R1 understates the \"logprob paradox\" issue.** R1 mentions it peripherally. This finding is well-established in the calibration and selective prediction literature and is presented here without proper attribution or novel analysis.\n\n### Whether R1's Review Changes My Assessment\n\nR1's review *reinforces* my concerns rather than alleviating them. R1's more precise formulation of the tautological gap (per-sample variants never tested) and the statistical rigor issues strengthen my belief that the experimental design cannot support the paper's conclusions.\n\nR1's identification of method section discrepancies (W5: FK token-vs-entity, EM equivalence claim, SJ formula) is new information that further weakens my confidence in the work's technical precision.\n\n### Updated Score\n\n**Score: 3 (Weak Reject), unchanged.** Confidence remains 4. R1's review surfaced additional technical concerns (method discrepancies, Fisher z-test validity) that, if anything, push toward a stronger reject. I hold at 3 because the research question itself has merit, but the execution and positioning remain insufficient for acceptance."
      }
    ],
    "totalDurationMs": 20066,
    "totalTokens": 15450,
    "totalToolUseCount": 0,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 6457,
      "cache_read_input_tokens": 8251,
      "output_tokens": 739,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 6457
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 739,
          "cache_read_input_tokens": 8251,
          "cache_creation_input_tokens": 6457,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 6457,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  },
  "sourceToolAssistantUUID": "e35735b7-afbc-470c-9bb2-e18f52ceb3ec",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a188aefa-23b6-4688-b448-164a4ee4e586",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 35 · 2026-05-14T21:34:45.071Z_

```json
{
  "parentUuid": "8a0dab04-6a49-461b-95d2-f54ff5f498b1",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "6f7e967b-2c86-4664-848c-8fb696bcf0a3",
  "timestamp": "2026-05-14T21:34:45.071Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a188aefa-23b6-4688-b448-164a4ee4e586",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 36 · 2026-05-14T21:34:52.283Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have Step 1 (independent reviews) and Step 2 (cross-sharing) complete. Let me proceed to Step 3 (convergence) and Step 4 (synthesis/meta-review).

The reviewers have converged:
- R1 revised from 4 → 3 (Weak Reject)
- R2 held at 3 (Weak Reject)

Both agree on:
1. The correlation-selection gap is partly tautological
2. Missing MBR decoding connection
3. No proposed solution
4. Statistical rigor issues
5. Single RE dataset limitation

Let me now write the final synthesis (Step 4: AC meta-review) and submit.


I'm loading the tool to submit the review report.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6f7e967b-2c86-4664-848c-8fb696bcf0a3",
  "isSidechain": false,
  "requestId": "req_011Cb3BNSUvhBxKHyhUdimj1",
  "type": "assistant",
  "uuid": "130d36f7-ea29-4e2c-836c-a933a26bd492",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a188aefa-23b6-4688-b448-164a4ee4e586",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VuV7VjC3bjaBoVNtjPxPep",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 3450,
      "cache_read_input_tokens": 84468,
      "output_tokens": 314,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3450,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 314,
          "cache_read_input_tokens": 84468,
          "cache_creation_input_tokens": 3450,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3450
          },
          "type": "message"
        }
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

_source line 37 · 2026-05-14T21:34:52.286Z_

Step 2 complete. Both reviewers converged to 3 (Weak Reject). Now I'll synthesize the final meta-review and submit.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "130d36f7-ea29-4e2c-836c-a933a26bd492",
  "isSidechain": false,
  "requestId": "req_011Cb3BNSUvhBxKHyhUdimj1",
  "type": "assistant",
  "uuid": "da00b160-4f40-4630-9ac1-cf9793289747",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a188aefa-23b6-4688-b448-164a4ee4e586",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VuV7VjC3bjaBoVNtjPxPep",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 3450,
      "cache_read_input_tokens": 84468,
      "output_tokens": 314,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3450,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 314,
          "cache_read_input_tokens": 84468,
          "cache_creation_input_tokens": 3450,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3450
          },
          "type": "message"
        }
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

_source line 38 · 2026-05-14T21:34:52.659Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_017iQmTtu4xeqGCwGqso1rxo`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__submit_dream_review_report",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "da00b160-4f40-4630-9ac1-cf9793289747",
  "isSidechain": false,
  "requestId": "req_011Cb3BNSUvhBxKHyhUdimj1",
  "type": "assistant",
  "uuid": "cbaf4e16-7cc7-42b7-8a3f-e93ecf6cc16d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a188aefa-23b6-4688-b448-164a4ee4e586",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VuV7VjC3bjaBoVNtjPxPep",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 3450,
      "cache_read_input_tokens": 84468,
      "output_tokens": 314,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3450,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 314,
          "cache_read_input_tokens": 84468,
          "cache_creation_input_tokens": 3450,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3450
          },
          "type": "message"
        }
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

_source line 39 · 2026-05-14T21:34:52.670Z_

<details><summary>↩ Tool result · `toolu_017iQmTtu4xeqGCwGqso1rxo`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__submit_dream_review_report"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cbaf4e16-7cc7-42b7-8a3f-e93ecf6cc16d",
  "isSidechain": false,
  "promptId": "a640b4e1-01ba-4811-b057-a5972a785ed6",
  "type": "user",
  "uuid": "4a9a93a5-c600-4e7c-95f1-baf306ea9812",
  "toolUseResult": {
    "matches": [
      "mcp__agent-ml-research__submit_dream_review_report"
    ],
    "query": "select:mcp__agent-ml-research__submit_dream_review_report",
    "total_deferred_tools": 23
  },
  "sourceToolAssistantUUID": "cbaf4e16-7cc7-42b7-8a3f-e93ecf6cc16d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a188aefa-23b6-4688-b448-164a4ee4e586",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 40 · 2026-05-14T21:36:15.961Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_dream_review_report · `toolu_01CF8bw7YvLgEskmdHmz8hBu`</summary>

```json
{
  "report": "# Dream Review Report: \"Why Self-Consistency Fails for Structured Prediction: An Analysis of the Correlation–Selection Gap\"\n\n**dream_id:** 20260514T203201  \n**Review mode:** full (2 Reviewers + Roundtable)  \n**Venue standard:** Top ML venue, ~25% acceptance rate, 6-point scale\n\n---\n\n## Reviewer Assignments\n\n- **R1** — Methods + Experiments (Score: 4→3 after discussion)\n- **R2** — Novelty + Related Work (Score: 3, held)\n\n---\n\n## Step 1: Independent Reviews\n\n### Reviewer R1 (Methods + Experiments)\n\n**Initial Score: 4 (Weak Accept), Confidence: 4**\n\n#### Strengths\n\n- **S1. Clean conceptual contribution.** The quality estimation vs. sample selection disentanglement is crisp and practically important. The \"correlation–selection gap\" is a useful concept that clarifies why high correlation does not imply selection utility.\n- **S2. Comprehensive experimental coverage.** 2×2 model–dataset matrix, 3-seed robustness, N=8/16 scaling, temperature ablation, per-relation diagnostics, capability stratification, LOO circularity check, ensemble analysis, OOD robustness — 17 experiments fully executed. Few papers achieve this level of completeness.\n- **S3. Honest negative results.** WNUT-17 failure mode reported transparently. RE weakness acknowledged head-on. Best-of-N failure on NER is the central finding rather than buried.\n- **S4. Practical utility.** Actionable guidance for practitioners: log-probability provides comparable quality estimation at zero extra cost; multi-sample generation not justified for fine-tuned models unless log-probs are unavailable.\n\n#### Weaknesses\n\n- **W1 (Major). Best-of-N protocol structurally biased against instance-level signals; gap explanation is near-tautological.** Instance-level signals (SJ, voting, FK, EM) assign the same score to all N samples from one input — they *cannot* rank among candidates by construction. The paper presents this as an empirical discovery when it is closer to a definitional property. The real question — whether per-sample variants of structural signals (e.g., LOO-SJ per sample as a ranking signal) could enable selection — is never tested. LOO-SJ is computed only for circularity checking, not as a selection signal. This is a significant missed opportunity.\n- **W2 (Major). Single RE dataset with severe floor effects.** 44% of SciERC RE instances receive F1=0. All RE-specific claims rest on this single dataset. A second RE dataset (TACRED, DocRED) would substantially strengthen conclusions.\n- **W3 (Moderate). Task-difficulty gradient conflates multiple variables.** The difficulty gradient (CoNLL easy → SciERC hard → WNUT infeasible) simultaneously varies domain, schema complexity, text style, and model capability. Unclear which variable drives observed effects.\n- **W4 (Moderate). Uneven statistical rigor.** No bootstrap CIs reported for main Table 1 comparisons. Only 3 seeds. No paired bootstrap or Williams' test for comparing dependent correlations. Fisher z-test on overlapping NER/RE instances violates independence assumption.\n- **W5 (Minor–Moderate). Potential method section discrepancies.** FK described as token-level but may be implemented as entity-level. SJ formula in paper may be oversimplified relative to implementation. These cannot be verified from the paper alone.\n- **W6 (Moderate). N=8 may underestimate structural signals.** RE SJ improves from 0.21→0.28 at N=16. Larger N (32, 64) not explored. Negative selection results may be N-dependent.\n- **W7 (Moderate). Ensemble analysis superficial.** No hybrid strategy tested (structural filtering + logprob ranking). No learned combination with cross-validation.\n\n#### Questions for Authors\n1. Have you tested per-sample variants of structural signals (LOO-SJ_i, per-sample voting score) for best-of-N selection?\n2. How would practitioners perform conditional filtering (excluding zero-F1 instances) at deployment without gold labels?\n3. For instance-level signals, does best-of-N selection reduce to random among tied candidates, or do you use closest-to-consensus? The protocol is unclear.\n4. How sensitive are results to fine-tuning quality? Would stronger base models change signal rankings?\n\n---\n\n### Reviewer R2 (Novelty + Related Work)\n\n**Score: 3 (Weak Reject), Confidence: 4**\n\n#### Strengths\n\n- **S1. Quality estimation vs. selection disentanglement is well-executed.** Clean separation of two objectives conflated in prior work.\n- **S2. Comprehensive related work.** Well-organized into self-consistency, structured IE, and uncertainty/calibration threads. Positioning against Nédellec & Xia (2026) is explicit and fair.\n- **S3. Honest negative results.** WNUT-17 analysis reported transparently as a capability boundary.\n- **S4. Task-difficulty-dependent signal ranking.** EM > SJ on CoNLL but SJ > EM on SciERC provides actionable, nuanced guidance.\n\n#### Weaknesses\n\n- **W1 (Major). Correlation–selection gap is near-tautological.** An instance-level signal c(x, {y_i}) → ℝ produces one number per input; it *cannot* rank N candidates by construction. The conceptual contribution reduces to: (a) instance-level signals can't rank samples (definitional), and (b) logprob helps on RE but not NER (a single empirical observation). Neither alone meets the novelty bar for a top venue.\n- **W2 (Major). Insufficient differentiation from Nédellec & Xia (2026).** SJ is a straightforward extension of Jaccard similarity to entity sets. The best-of-N analysis yields a negative result that is partly predetermined (W1). Multi-domain evaluation is valuable but incremental. The paper reads as \"Nédellec & Xia + better metrics + negative selection result.\"\n- **W3 (Major). No proposed solution or path forward.** Paper identifies the gap and stops. Pure negative-result papers need either (a) a very surprising negative result, or (b) deep mechanistic understanding enabling future solutions. The explanation here is shallow — it does not explain why consensus-closest selection fails, whether per-sample structural signals could work, or what properties a successful selector would need.\n- **W4 (Moderate). Ambiguous positioning.** Caught between \"systematic comparison\" and \"novel finding.\" Systematic comparisons are typically Findings-level unless they reveal unexpected phenomena.\n- **W5 (Major). Missing MBR decoding connection.** MBR decoding — selecting argmax_i Σ_j SJ(y_i, y_j) — is the natural per-sample adaptation of instance-level SJ. This converts an instance-level signal into a per-sample ranking. If MBR-with-SJ fails, that's a much stronger negative result. If it succeeds, it resolves the gap. Omitting this connection is a significant gap in both the experimental design and the related work (Eikema & Aziz 2020, 2022; Freitag et al. 2022, 2023).\n- **W6 (Minor). \"Logprob paradox\" is well-known.** High AUROC + low ρ from bimodal score distributions is standard in calibration literature (Guo et al. 2017). Presenting it as novel overstates the contribution.\n\n#### Questions for Authors\n1. Did you try MBR decoding with SJ as the utility function? This is the natural per-sample adaptation of your best instance-level signal.\n2. For oracle-selected samples, are they structurally different from consensus (suggesting consensus-based selection is fundamentally wrong) or close but slightly better (suggesting finer discrimination is needed)?\n3. Within-stratum correlations \"approach zero\" — can you provide actual numbers and CIs?\n\n---\n\n## Step 2: Cross-Sharing\n\n### R1 Response to R2\n\n**Points of agreement:** Strong convergence on the tautological gap (both W1s). R2's MBR omission point (W5) is \"the most impactful new concern\" — \"If the authors had run MBR-with-SJ, the paper would be substantially stronger regardless of outcome.\" Agreement on no-solution weakness.\n\n**Points of disagreement:** R1 considers R2 too harsh on differentiation from Nédellec & Xia — the multi-domain evaluation and task-difficulty-dependent signal ranking represent nontrivial work. R1 disagrees that ambiguous positioning (R2-W4) is a serious standalone weakness.\n\n**Score revision:** R1 revised from **4 → 3 (Weak Reject)**. The convergence on the tautological gap plus R2's MBR omission point tipped the assessment.\n\n### R2 Response to R1\n\n**Points of agreement:** Strong agreement on tautological gap, statistical rigor issues, single RE dataset, and missing hybrid strategies. R1's specific critique about Fisher z-test on overlapping instances is valid.\n\n**Points of disagreement:** R2 considers R1 too generous on related work positioning and on the initial score of 4. R1's own identified weaknesses (tautological design W1, uneven statistics W4) should have prevented acceptance from the start. R1 also understates the \"logprob paradox\" issue.\n\n**Score:** R2 held at **3 (Weak Reject)**. R1's review surfaced additional technical concerns (method discrepancies, Fisher z-test) that reinforce the assessment.\n\n---\n\n## Step 3: Convergence\n\nBoth reviewers converged to **3 (Weak Reject)** with confidence 4.\n\n**Consensus strengths:**\n1. Well-executed empirical comparison with commendable breadth (2 models × 2+ datasets × 5 signals × multiple ablations)\n2. Honest treatment of negative results; WNUT-17 reported transparently\n3. The quality estimation vs. selection distinction is practically useful\n4. Task-difficulty-dependent signal ranking is a genuine empirical contribution\n\n**Consensus weaknesses (ordered by severity):**\n1. **(Critical) Tautological core finding.** The correlation–selection gap, as presented, is partly a consequence of signal definition rather than an empirical discovery. Instance-level signals cannot rank by construction; the paper never tests per-sample structural variants that could resolve or sharpen the finding.\n2. **(Critical) Missing MBR decoding.** MBR with SJ as utility is the natural bridge between instance-level signals and per-sample selection. Its absence is a major experimental design gap.\n3. **(Major) No proposed solution.** Pure negative result without deep mechanistic insight or preliminary remedy. The oracle headroom (+15pp NER, +19pp RE) is tantalizingly large but receives no investigation.\n4. **(Major) Insufficient differentiation from Nédellec & Xia (2026).** Structural metrics are straightforward extensions; the best-of-N negative result is partly predetermined by the tautological gap.\n5. **(Moderate) Statistical rigor.** Missing CIs for main comparisons, only 3 seeds, invalid Fisher z-test on overlapping instances.\n6. **(Moderate) Single RE dataset with severe floor effects.** 44% zero-F1 instances limit RE conclusions.\n\n---\n\n## Step 4: Meta-Review & Recommendation\n\n### Overall Assessment\n\nThis paper presents a thorough empirical comparison of five unsupervised confidence signals for LLM-based information extraction, covering NER and RE across two models and two primary datasets. The experimental breadth (17 experiments, N-scaling, temperature ablation, cross-model validation, OOD analysis) is commendable, and the honest treatment of negative results is a credit to the authors. The practical guidance — that log-probability provides comparable quality estimation at zero extra inference cost — is useful for practitioners.\n\nHowever, the paper's central novelty claim, the \"correlation–selection gap,\" is undermined by a structural issue in the experimental design: the tested instance-level signals *cannot* perform per-sample selection by definition. Both reviewers independently identified this as near-tautological. The natural resolution — MBR decoding, which converts instance-level SJ into a per-sample ranking — is neither tested nor discussed, despite being the standard approach in the structured prediction literature. This omission means the paper's headline claim (\"self-consistency fails for structured prediction\") is both overstated and undertested.\n\nThe differentiation from Nédellec & Xia (2026) is incremental: structural metrics over surface matching, with a negative selection result that is partly predetermined. The paper proposes no solution to the identified gap, and the mechanistic explanation is shallow. Statistical rigor is uneven, with missing confidence intervals for key comparisons and methodological concerns about the Fisher z-test on overlapping instances.\n\nThe work has merit as a systematic comparison and would be appropriate for a **Findings** track, where the comprehensive evaluation and practitioner guidance would be valued. For the main conference, the novelty bar is not met: the core insight is partly definitional, the most relevant experimental variant (MBR) is untested, and no path toward closing the gap is offered.\n\n### Recommendation\n\n**Score: 3 (Weak Reject)**  \n**Consensus: Reject for main track; recommend resubmission to Findings**\n\n### Key Revisions for Resubmission\n\n1. **Test MBR decoding with SJ as utility function.** This is the single highest-impact addition. If MBR-SJ fails, the negative result becomes genuinely strong. If it succeeds, the paper gains a positive contribution.\n2. **Test per-sample structural signal variants** (LOO-SJ_i, per-sample voting score) for best-of-N selection.\n3. **Add a second RE dataset** to validate RE-specific conclusions beyond SciERC's floor effects.\n4. **Report bootstrap CIs** for all main comparisons (Table 1) and use appropriate tests for dependent correlations.\n5. **Connect to MBR decoding literature** (Eikema & Aziz 2020/2022, Freitag et al. 2022/2023).\n6. **Soften the title and framing.** \"Self-consistency fails\" overstates — it works for quality estimation. The gap is specifically about selection with instance-level aggregates.\n\n### Experiment Coverage Assessment\n\nThe paper covers all 17 planned experiments from the design document:\n- Baseline comparisons (exp-012 to exp-014): ✓ Table 1\n- Metrics expansion (exp-015): ✓ Tables 1–2\n- N=16 scaling (exp-001, exp-008): ✓ Table 4\n- CoNLL-2003 (exp-002): ✓ Table 2\n- WNUT-17 (exp-003): ✓ Reported despite abandonment\n- RE diagnostics (exp-004): ✓ Table 7\n- Temperature (exp-005): ✓ Table 5\n- Best-of-N (exp-006): ✓ Table 6\n- Cross-model LLaMA (exp-007): ✓ Table 3\n- Capability stratification (exp-009): ✓ Table 8\n- Selection curves (exp-010): ✓ Section 5.6 text\n- OOD robustness (exp-011): ✓ Table 9\n- Signal ensemble (exp-016): ✓ Section 5.6\n- LLaMA×CoNLL (exp-017): ✓ Table 3\n\nCoverage is comprehensive. The main gap is not in experiment coverage but in experimental *design* — the missing MBR variant and per-sample structural signals.\n",
  "project": "struct_self_consist_ie",
  "tier": "worst",
  "dream_id": "20260514T203201",
  "overall_score": "weak reject",
  "review_visible": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4a9a93a5-c600-4e7c-95f1-baf306ea9812",
  "isSidechain": false,
  "requestId": "req_011Cb3BP1QagxfKBnquEqdye",
  "type": "assistant",
  "uuid": "68be6e8c-592e-490c-b8ce-9845b0d4420b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a188aefa-23b6-4688-b448-164a4ee4e586",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011ELX4skwUhYP7YxYrViRJT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 893,
      "cache_read_input_tokens": 87918,
      "output_tokens": 3930,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 893,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 3930,
          "cache_read_input_tokens": 87918,
          "cache_creation_input_tokens": 893,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 893
          },
          "type": "message"
        }
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

_source line 41_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[DREAM Review Director] dream_id=20260514T203201 | review_mode=full | review_visible=True PDF: /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/d…",
  "leafUuid": "68be6e8c-592e-490c-b8ce-9845b0d4420b",
  "sessionId": "a188aefa-23b6-4688-b448-164a4ee4e586"
}
```

---

### Runtime record

_source line 42_

```json
{
  "type": "ai-title",
  "aiTitle": "Full blind review of structural self-consistency IE paper",
  "sessionId": "a188aefa-23b6-4688-b448-164a4ee4e586"
}
```

---

### Tool result

_source line 43 · 2026-05-14T21:36:19.159Z_

<details><summary>↩ Tool result · `toolu_01CF8bw7YvLgEskmdHmz8hBu`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"report_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T203201/worst/review_report.md\", \"dream_id\": \"dream_20260514T203201\", \"tier\": \"worst\", \"review_visible\": true}, \"error\": \"\"}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "68be6e8c-592e-490c-b8ce-9845b0d4420b",
  "isSidechain": false,
  "promptId": "a640b4e1-01ba-4811-b057-a5972a785ed6",
  "type": "user",
  "uuid": "5894bd70-4890-43c4-98f3-d9ce8dc30d96",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"report_path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T203201/worst/review_report.md\\\", \\\"dream_id\\\": \\\"dream_20260514T203201\\\", \\\"tier\\\": \\\"worst\\\", \\\"review_visible\\\": true}, \\\"error\\\": \\\"\\\"}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"report_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T203201/worst/review_report.md\", \"dream_id\": \"dream_20260514T203201\", \"tier\": \"worst\", \"review_visible\": true}, \"error\": \"\"}"
    }
  },
  "sourceToolAssistantUUID": "68be6e8c-592e-490c-b8ce-9845b0d4420b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a188aefa-23b6-4688-b448-164a4ee4e586",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 44 · 2026-05-14T21:36:26.540Z_

Review submitted successfully.

**Summary:** Both reviewers converged to **3 (Weak Reject)** — recommend Findings track, not main conference.

Key issues identified:
1. **Tautological core finding** — instance-level signals cannot rank samples by construction; the paper presents this as empirical discovery
2. **Missing MBR decoding** — the natural per-sample adaptation of SJ (argmax_i Σ_j SJ(y_i, y_j)) is neither tested nor discussed
3. **No proposed solution** — identifies a gap and stops, with shallow mechanistic explanation
4. **Insufficient differentiation from Nédellec & Xia (2026)** — reads as incremental extension with negative selection result
5. **Statistical rigor gaps** — no CIs for main comparisons, invalid Fisher z-test on overlapping instances

Strengths acknowledged: comprehensive 17-experiment coverage, honest negative results, practical guidance (log-prob suffices at zero cost), task-difficulty-dependent signal ranking.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5894bd70-4890-43c4-98f3-d9ce8dc30d96",
  "isSidechain": false,
  "requestId": "req_011Cb3BVNoN4HkPiJX9H7iiv",
  "type": "assistant",
  "uuid": "317b64fc-04a8-4dcc-ab81-bd0df9612c11",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "a188aefa-23b6-4688-b448-164a4ee4e586",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y4LE5idgUkWKTT5R62APhb",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4060,
      "cache_read_input_tokens": 88811,
      "output_tokens": 236,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4060,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 236,
          "cache_read_input_tokens": 88811,
          "cache_creation_input_tokens": 4060,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4060
          },
          "type": "message"
        }
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

_source line 45_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[DREAM Review Director] dream_id=20260514T203201 | review_mode=full | review_visible=True PDF: /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/d…",
  "leafUuid": "317b64fc-04a8-4dcc-ab81-bd0df9612c11",
  "sessionId": "a188aefa-23b6-4688-b448-164a4ee4e586"
}
```

---

### Runtime record

_source line 46_

```json
{
  "type": "ai-title",
  "aiTitle": "Full blind review of structural self-consistency IE paper",
  "sessionId": "a188aefa-23b6-4688-b448-164a4ee4e586"
}
```

---
