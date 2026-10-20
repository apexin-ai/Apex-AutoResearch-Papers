# Research conversation: [DREAM Review Director] dream_id=20260521T032808 | review_mode=simple | review_visible=True PDF: /home/ubuntu/.agent-ml-

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 45
- **Recorded user turns:** 4
- **Tool calls:** 8
- **Original source:** `logs/chats/exported-trajectories/account-3/89f74592-e632-4d87-adff-4e5f492e3598.jsonl`
- **Structured JSON:** [`9f4b2cfe266cab336ad8.json`](../../sessions/9f/9f4b2cfe266cab336ad8.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-21T04:26:38.839Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-21T04:26:38.839Z",
  "sessionId": "89f74592-e632-4d87-adff-4e5f492e3598",
  "content": "[DREAM Review Director]\ndream_id=20260521T032808 | review_mode=simple | review_visible=True\nPDF: /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/worst/review_input_f5f46a62.pdf\n\n（内部编排信息：tier=worst，仅用于 submit_dream_review_report 调用。\n你在向 Reviewer 发送审稿任务时，**严禁**提及档位名称 best/median/worst，\n也不要暗示论文结果的好坏。Reviewer 必须盲审。）\n\n任务：对上述 PDF 进行 simple 模式审稿。 使用 `dream-review-simple` skill 的 dispatch 模板（1 Reviewer 全面覆盖，跳过 Step 2 交叉分享 + Step 3 收敛）。\n\n## 审稿标准\n\n未指定目标 venue。请按 top ML venue 通用标准审稿（接受率 ~25%，6 分制：1=Strong Reject … 6=Strong Accept）。\n\n## 实验设计参考\n\n完整实验设计（含想象实验列表）：`/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/worst/review_context.yaml`\n论文可能未完整反映所有实验——参考此文件判断覆盖度。\n完成后必须调用 `submit_dream_review_report(report, project=\"xling_calib_direction\", tier=\"worst\", dream_id=\"20260521T032808\", review_visible=True)` —— 报告会写入 dream_reports/dream_20260521T032808/worst/review_report.md，编排进程通过 subprocess 退出读取它。\n不要调用 submit_review_report_to_research_director / update_review_issues / request_external_review —— 这些工具不在 Dream Review Director 白名单内。\n"
}
```

---

### Runtime record

_source line 2 · 2026-05-21T04:26:38.842Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-21T04:26:38.842Z",
  "sessionId": "89f74592-e632-4d87-adff-4e5f492e3598"
}
```

---

## Round 1

20 recorded events

### User

_source line 3 · 2026-05-21T04:26:38.868Z_

[DREAM Review Director]
dream_id=20260521T032808 | review_mode=simple | review_visible=True
PDF: /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/worst/review_input_f5f46a62.pdf

（内部编排信息：tier=worst，仅用于 submit_dream_review_report 调用。
你在向 Reviewer 发送审稿任务时，**严禁**提及档位名称 best/median/worst，
也不要暗示论文结果的好坏。Reviewer 必须盲审。）

任务：对上述 PDF 进行 simple 模式审稿。 使用 `dream-review-simple` skill 的 dispatch 模板（1 Reviewer 全面覆盖，跳过 Step 2 交叉分享 + Step 3 收敛）。

## 审稿标准

未指定目标 venue。请按 top ML venue 通用标准审稿（接受率 ~25%，6 分制：1=Strong Reject … 6=Strong Accept）。

## 实验设计参考

完整实验设计（含想象实验列表）：`/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/worst/review_context.yaml`
论文可能未完整反映所有实验——参考此文件判断覆盖度。
完成后必须调用 `submit_dream_review_report(report, project="xling_calib_direction", tier="worst", dream_id="20260521T032808", review_visible=True)` —— 报告会写入 dream_reports/dream_20260521T032808/worst/review_report.md，编排进程通过 subprocess 退出读取它。
不要调用 submit_review_report_to_research_director / update_review_issues / request_external_review —— 这些工具不在 Dream Review Director 白名单内。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "221e9c50-d73e-4401-b409-8fd8dd5897a7",
  "type": "user",
  "uuid": "ee315a05-f787-4cac-b23f-0011965cf5a8",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "89f74592-e632-4d87-adff-4e5f492e3598",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-21T04:26:38.867Z_

```json
{
  "parentUuid": "ee315a05-f787-4cac-b23f-0011965cf5a8",
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
  "uuid": "ffebea36-e06c-43f3-9d1e-dd44d7f09334",
  "timestamp": "2026-05-21T04:26:38.867Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "89f74592-e632-4d87-adff-4e5f492e3598",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-21T04:26:38.867Z_

```json
{
  "parentUuid": "ffebea36-e06c-43f3-9d1e-dd44d7f09334",
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
  "uuid": "96a18f8d-b3ca-41c4-8a6b-5d72bd41fdae",
  "timestamp": "2026-05-21T04:26:38.867Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "89f74592-e632-4d87-adff-4e5f492e3598",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6 · 2026-05-21T04:26:38.867Z_

```json
{
  "parentUuid": "96a18f8d-b3ca-41c4-8a6b-5d72bd41fdae",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "78c473dd-45a1-473f-bfa7-a75ce94ca903",
  "timestamp": "2026-05-21T04:26:38.867Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "89f74592-e632-4d87-adff-4e5f492e3598",
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
  "aiTitle": "Review cross-lingual calibration research paper",
  "sessionId": "89f74592-e632-4d87-adff-4e5f492e3598"
}
```

---

### Assistant

_source line 8 · 2026-05-21T04:26:43.287Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to review a PDF paper using the "dream-review-simple" skill. Let me first load the necessary tools and read the relevant files to understand the task.

Let me start by:
1. Reading the PDF paper
2. Reading the review context YAML
3. Loading the dream-review-simple skill or understanding what it entails

Let me first load the tools I'll need and read the files.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "78c473dd-45a1-473f-bfa7-a75ce94ca903",
  "isSidechain": false,
  "requestId": "req_011CbF5dhScC3Bi5RUUJkhEv",
  "type": "assistant",
  "uuid": "12646afc-8c78-4d56-85ff-429c54c27211",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "89f74592-e632-4d87-adff-4e5f492e3598",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UGVhXGofqd2raSc1TJUFg9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11327,
      "cache_read_input_tokens": 11841,
      "output_tokens": 403,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11327,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 403,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11327,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11327
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

_source line 9 · 2026-05-21T04:26:44.327Z_

我来执行 dream-review-simple 审稿流程。先读取论文 PDF 和实验设计上下文。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "12646afc-8c78-4d56-85ff-429c54c27211",
  "isSidechain": false,
  "requestId": "req_011CbF5dhScC3Bi5RUUJkhEv",
  "type": "assistant",
  "uuid": "bb0a4147-aaa0-4e79-ae7d-04a2eafc023d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "89f74592-e632-4d87-adff-4e5f492e3598",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UGVhXGofqd2raSc1TJUFg9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11327,
      "cache_read_input_tokens": 11841,
      "output_tokens": 403,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11327,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 403,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11327,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11327
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

_source line 10 · 2026-05-21T04:26:44.825Z_

<details open><summary>🔧 Tool call — Read · `toolu_01MmbmNJ9bX1NrvgV5iEgouk`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/worst/review_input_f5f46a62.pdf"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bb0a4147-aaa0-4e79-ae7d-04a2eafc023d",
  "isSidechain": false,
  "requestId": "req_011CbF5dhScC3Bi5RUUJkhEv",
  "type": "assistant",
  "uuid": "07ce7d07-ce09-4bd8-ad9d-121ae490bb0a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "89f74592-e632-4d87-adff-4e5f492e3598",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UGVhXGofqd2raSc1TJUFg9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11327,
      "cache_read_input_tokens": 11841,
      "output_tokens": 403,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11327,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 403,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11327,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11327
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

_source line 11 · 2026-05-21T04:26:46.771Z_

<details><summary>↩ Tool result · `toolu_01EtFvm8z6epdT5F1XwhRU5U`</summary>

```text
No matching deferred tools found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9569d631-74c4-4c04-9124-6eec52d5cb63",
  "isSidechain": false,
  "promptId": "221e9c50-d73e-4401-b409-8fd8dd5897a7",
  "type": "user",
  "uuid": "836bf680-9dfc-491e-b0ca-bb806657361f",
  "toolUseResult": {
    "matches": [],
    "query": "select:submit_dream_review_report",
    "total_deferred_tools": 23
  },
  "sourceToolAssistantUUID": "9569d631-74c4-4c04-9124-6eec52d5cb63",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "89f74592-e632-4d87-adff-4e5f492e3598",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-21T04:26:44.858Z_

<details><summary>↩ Tool result · reported error · `toolu_01MmbmNJ9bX1NrvgV5iEgouk`</summary>

```text
This PDF has 13 pages, which is too many to read at once. Use the pages parameter to read specific page ranges (e.g., pages: "1-5"). Maximum 20 pages per request.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "07ce7d07-ce09-4bd8-ad9d-121ae490bb0a",
  "isSidechain": false,
  "promptId": "221e9c50-d73e-4401-b409-8fd8dd5897a7",
  "type": "user",
  "uuid": "219b2c72-8480-4910-b24b-52c93541e0d0",
  "toolUseResult": "Error: This PDF has 13 pages, which is too many to read at once. Use the pages parameter to read specific page ranges (e.g., pages: \"1-5\"). Maximum 20 pages per request.",
  "sourceToolAssistantUUID": "07ce7d07-ce09-4bd8-ad9d-121ae490bb0a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "89f74592-e632-4d87-adff-4e5f492e3598",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-21T04:26:46.630Z_

<details open><summary>🔧 Tool call — Read · `toolu_01FiELemFewrpUuhXd6k2mar`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/worst/review_context.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "219b2c72-8480-4910-b24b-52c93541e0d0",
  "isSidechain": false,
  "requestId": "req_011CbF5dhScC3Bi5RUUJkhEv",
  "type": "assistant",
  "uuid": "19a2f8c3-e0a4-4915-9be6-5f30e98b2602",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "89f74592-e632-4d87-adff-4e5f492e3598",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UGVhXGofqd2raSc1TJUFg9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11327,
      "cache_read_input_tokens": 11841,
      "output_tokens": 403,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11327,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 403,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11327,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11327
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

_source line 14 · 2026-05-21T04:26:46.763Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01EtFvm8z6epdT5F1XwhRU5U`</summary>

```json
{
  "query": "select:submit_dream_review_report",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "19a2f8c3-e0a4-4915-9be6-5f30e98b2602",
  "isSidechain": false,
  "requestId": "req_011CbF5dhScC3Bi5RUUJkhEv",
  "type": "assistant",
  "uuid": "9569d631-74c4-4c04-9124-6eec52d5cb63",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "89f74592-e632-4d87-adff-4e5f492e3598",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UGVhXGofqd2raSc1TJUFg9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11327,
      "cache_read_input_tokens": 11841,
      "output_tokens": 403,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11327,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 403,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11327,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11327
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

_source line 15 · 2026-05-21T04:26:46.900Z_

<details><summary>↩ Tool result · `toolu_01FiELemFewrpUuhXd6k2mar`</summary>

```text
1	narrative_guidance: '核心 reframe：从 ''cross-lingual calibration method'' 转为 ''cross-lingual
2	  probing viability boundary + methodological warning''。 Headline: ''Stress-testing
3	  probe-based calibration beyond English: viability boundaries, capacity artifacts,
4	  and when cross-lingual transfer breaks down.'' 大模型（235B MoE / Scout MoE）的 correctness
5	  signal 比 7B dense 更分散——MoE routing 将信息分散到更多 expert，导致 probe AUROC 提升有限且 noisy。 Pareto
6	  frontier 在两个 MoE 架构上均 noisy（rho 接近零），无法支撑 clean architecture contrast。 CaCLR 失败且
7	  linear projection 在低/中资源语言不稳定。CKA partial correlation 控制 depth 后 n.s.。 Control task
8	  揭示 >30% 的 lang-layer 组合是 capacity artifacts，低资源语言几乎全部受影响。 贡献重构为：(1) viability boundary
9	  刻画；(2) capacity artifact 问题揭露（Hewitt & Liang 多语言扩展）；(3) 方法论框架。 目标 venue 不降级（EACL）——需增加
10	  discussion 篇幅，补充 few-shot escalation 实验作为 constructive path forward。
11	
12	  '
13	imagined_experiments:
14	- name: Qwen3-235B-A22B Full Pareto Frontier (20 langs × 24 layers × 5 transfer conditions)
15	  plan_id: plan_001
16	  description: '在 Qwen3-235B-A22B（94 层 MoE, INT4）上提取每隔 4 层的激活（24 个 probed layers），
17	    20 种语言训练英语 correctness probes（LR + MLP），评估 5 种 transfer 条件。 报告 per-language Spearman
18	    rho（depth vs transfer AUROC）和 global rho。
19	
20	    '
21	  expected_results:
22	    en_best_auroc: 0.76
23	    en_best_layer: L72 (约 77% depth)
24	    en_auroc_range:
25	    - 0.58
26	    - 0.76
27	    en_best_ece_raw: 0.175
28	    zs_transfer_auroc_avg_20lang: 0.59
29	    zs_transfer_auroc_high_resource_avg: 0.65
30	    zs_transfer_auroc_mid_resource_avg: 0.59
31	    zs_transfer_auroc_low_resource_avg: 0.53
32	    zs_transfer_success_rate_above_060: 11/20 (55%)
33	    pareto_global_spearman_rho: -0.18
34	    pareto_global_spearman_p: 0.12
35	    pareto_per_lang_rho_median: -0.14
36	    pareto_per_lang_significant_count: 3/19 (zh, es, fr — 仅高资源)
37	    pareto_per_lang_positive_rho_count: 6/19 (ar, ko, bn, sw, te, vi — 方向反转)
38	    mean_shift_delta_auroc_avg: 0.0
39	    linear_proj_50pairs_delta_auroc_avg: 0.015
40	    linear_proj_50pairs_delta_auroc_high: 0.025
41	    linear_proj_50pairs_delta_auroc_low: -0.005
42	    fewshot_25_delta_auroc_avg: 0.035
43	    fewshot_100_delta_auroc_avg: 0.065
44	    linear_proj_std_across_seeds_low_resource: 0.028
45	    zs_auroc_std_across_layers_top10: 0.04
46	  result_rationale: '235B MoE 架构有 94 层但仅 22B 激活参数——expert routing 机制将 correctness
47	    信息分散到不同 expert 子网络中， probe 在 shared representation 上只能捕获部分信号，因此 AUROC 相比 7B dense（0.754）提升极有限（→0.76）。
48	    MoE 的 expert 选择是 input-dependent 的，不同语言激活不同 expert 子集，导致跨语言激活空间异质性更高。 这直接破坏了 Pareto
49	    frontier 的一致性：不同语言的 "最优 transfer 层" 受 expert routing pattern 影响而高度分散， global rho
50	    被拉向零。高资源语言（zh/es/fr）与英语共享更多 expert 激活模式，仍显示弱 Pareto； 低资源语言与英语 expert overlap 极低，transfer
51	    AUROC 在深层反而因 expert divergence 而改善（正 rho）。 Linear projection 在低资源上不稳定，因为 50 parallel
52	    pairs 不足以学习 MoE 碎片化空间的旋转矩阵。
53	
54	    '
55	  tables:
56	  - title: 'Table 1: Qwen3-235B Zero-Shot Transfer AUROC by Language (EN-optimal layer
57	      L72)'
58	    columns:
59	    - Language
60	    - Family
61	    - Resource_Tier
62	    - ZS_AUROC
63	    - 95% CI
64	    - vs EN Δ
65	    rows:
66	    - - en
67	      - Germanic
68	      - source
69	      - 0.76
70	      - '[0.74, 0.78]'
71	      - —
72	    - - zh
73	      - Sinitic
74	      - HIGH
75	      - 0.672
76	      - '[0.65, 0.69]'
77	      - -0.088
78	    - - es
79	      - Romance
80	      - HIGH
81	      - 0.668
82	      - '[0.64, 0.69]'
83	      - -0.092
84	    - - fr
85	      - Romance
86	      - HIGH
87	      - 0.662
88	      - '[0.64, 0.68]'
89	      - -0.098
90	    - - de
91	      - Germanic
92	      - HIGH
93	      - 0.653
94	      - '[0.63, 0.68]'
95	      - -0.107
96	    - - ja
97	      - Japonic
98	      - MID
99	      - 0.631
100	      - '[0.60, 0.66]'
101	      - -0.129
102	    - - pt
103	      - Romance
104	      - MID
105	      - 0.624
106	      - '[0.60, 0.65]'
107	      - -0.136
108	    - - ru
109	      - Slavic
110	      - MID
111	      - 0.608
112	      - '[0.58, 0.64]'
113	      - -0.152
114	    - - ko
115	      - Koreanic
116	      - MID
117	      - 0.602
118	      - '[0.57, 0.63]'
119	      - -0.158
120	    - - nl
121	      - Germanic
122	      - MID
123	      - 0.598
124	      - '[0.57, 0.63]'
125	      - -0.162
126	    - - hi
127	      - Indo-Aryan
128	      - MID
129	      - 0.588
130	      - '[0.56, 0.62]'
131	      - -0.172
132	    - - pl
133	      - Slavic
134	      - MID
135	      - 0.582
136	      - '[0.55, 0.61]'
137	      - -0.178
138	    - - id
139	      - Austronesian
140	      - MID
141	      - 0.577
142	      - '[0.55, 0.61]'
143	      - -0.183
144	    - - tr
145	      - Turkic
146	      - MID
147	      - 0.571
148	      - '[0.54, 0.60]'
149	      - -0.189
150	    - - vi
151	      - Austroasiatic
152	      - MID
153	      - 0.563
154	      - '[0.53, 0.60]'
155	      - -0.197
156	    - - uk
157	      - Slavic
158	      - MID
159	      - 0.558
160	      - '[0.53, 0.59]'
161	      - -0.202
162	    - - ar
163	      - Semitic
164	      - MID
165	      - 0.555
166	      - '[0.52, 0.59]'
167	      - -0.205
168	    - - bn
169	      - Indo-Aryan
170	      - LOW
171	      - 0.538
172	      - '[0.50, 0.57]'
173	      - -0.222
174	    - - te
175	      - Dravidian
176	      - LOW
177	      - 0.521
178	      - '[0.49, 0.55]'
179	      - -0.239
180	    - - sw
181	      - Niger-Congo
182	      - LOW
183	      - 0.508
184	      - '[0.48, 0.54]'
185	      - -0.252
186	  - title: 'Table 2: Qwen3-235B Pareto Spearman ρ (depth vs ZS AUROC) per Language'
187	    columns:
188	    - Language
189	    - Spearman_rho
190	    - p_value
191	    - Direction
192	    - Significant
193	    rows:
194	    - - zh
195	      - -0.52
196	      - 0.009
197	      - expected
198	      - ✓
199	    - - es
200	      - -0.44
201	      - 0.031
202	      - expected
203	      - ✓
204	    - - fr
205	      - -0.41
206	      - 0.046
207	      - expected
208	      - ✓
209	    - - de
210	      - -0.33
211	      - 0.11
212	      - expected
213	      - ✗
214	    - - ja
215	      - -0.25
216	      - 0.24
217	      - expected
218	      - ✗
219	    - - ru
220	      - -0.18
221	      - 0.4
222	      - expected
223	      - ✗
224	    - - ko
225	      - -0.06
226	      - 0.79
227	      - flat
228	      - ✗
229	    - - hi
230	      - -0.03
231	      - 0.89
232	      - flat
233	      - ✗
234	    - - tr
235	      - 0.02
236	      - 0.93
237	      - flat
238	      - ✗
239	    - - id
240	      - -0.11
241	      - 0.61
242	      - expected
243	      - ✗
244	    - - pt
245	      - -0.28
246	      - 0.19
247	      - expected
248	      - ✗
249	    - - nl
250	      - -0.22
251	      - 0.3
252	      - expected
253	      - ✗
254	    - - pl
255	      - -0.08
256	      - 0.71
257	      - flat
258	      - ✗
259	    - - vi
260	      - 0.12
261	      - 0.58
262	      - reversed
263	      - ✗
264	    - - uk
265	      - -0.15
266	      - 0.48
267	      - expected
268	      - ✗
269	    - - ar
270	      - 0.09
271	      - 0.67
272	      - reversed
273	      - ✗
274	    - - bn
275	      - 0.18
276	      - 0.4
277	      - reversed
278	      - ✗
279	    - - te
280	      - 0.22
281	      - 0.3
282	      - reversed
283	      - ✗
284	    - - sw
285	      - 0.15
286	      - 0.48
287	      - reversed
288	      - ✗
289	    - - global
290	      - -0.18
291	      - 0.12
292	      - —
293	      - ✗
294	  figures_description:
295	  - 'Fig 1: 20-panel Pareto frontier heatmap (x=normalized depth, y=language sorted
296	    by resource tier), color=ZS AUROC。高资源区域呈现弱对角梯度（浅层 transfer 好→深层差），中/低资源区域为 noisy
297	    棋盘格，无一致趋势。'
298	  - 'Fig 2: Per-language Spearman rho bar chart with 95% bootstrap CI。3 条显著阈值线；大部分
299	    CI 跨零。'
300	  analysis: 'Qwen3-235B 的 Pareto frontier 远弱于 7B dense MVP 预期。Global rho=-0.18 不显著，
301	    仅 3/19 target 语言有显著负相关（均为高资源）。6/19 语言出现方向反转（正 rho）， 集中在低资源。MoE routing 的 input-dependent
302	    expert selection 使得不同语言在不同深度 激活完全不同的子网络，破坏了 "更深=更好英语但更差 transfer" 的简单叙事。 这意味着
303	    Pareto frontier 在 MoE 架构上不是稳定的 architecture-level property， 而是 language-specific
304	    的。对 worst tier 叙事：这直接支持 "viability boundary" reframe—— Pareto analysis 仅在高资源+特定架构上有清晰信号。
305	
306	    '
307	- name: Llama 4 Scout Full Pareto Frontier (20 langs × 12 layers × 5 transfer conditions)
308	  plan_id: plan_002
309	  description: '在 Llama 4 Scout（48 层 MoE, W4A16）上提取激活（12 probed layers）， 20 种语言，5
310	    种 transfer 条件。报告 per-language Spearman rho。
311	
312	    '
313	  expected_results:
314	    en_best_auroc: 0.74
315	    en_best_layer: L40 (约 83% depth)
316	    en_auroc_range:
317	    - 0.6
318	    - 0.74
319	    en_best_ece_raw: 0.185
320	    zs_transfer_auroc_avg_20lang: 0.57
321	    zs_transfer_auroc_high_resource_avg: 0.63
322	    zs_transfer_auroc_mid_resource_avg: 0.57
323	    zs_transfer_auroc_low_resource_avg: 0.51
324	    zs_transfer_success_rate_above_060: 8/20 (40%)
325	    pareto_global_spearman_rho: -0.05
326	    pareto_global_spearman_p: 0.62
327	    pareto_per_lang_rho_median: -0.02
328	    pareto_per_lang_significant_count: 1/19 (仅 zh)
329	    pareto_per_lang_positive_rho_count: 8/19
330	    mean_shift_delta_auroc_avg: 0.0
331	    linear_proj_50pairs_delta_auroc_avg: 0.008
332	    linear_proj_50pairs_delta_auroc_low: -0.01
333	    fewshot_25_delta_auroc_avg: 0.028
334	    fewshot_100_delta_auroc_avg: 0.055
335	    linear_proj_std_across_seeds_low_resource: 0.035
336	  result_rationale: 'Llama 4 Scout 是 17B-16E MoE（272B total, 17B active），48 层比 Qwen3
337	    的 94 层少得多， probed layers 仅 12 个，Spearman rho 的统计检验力极低（n=12 时需要 |rho|>0.58 才显著）。
338	    MVP 阶段 Llama-3.1-8B dense 已经是 weak Pareto（仅 2/5 显著），Scout MoE 继承了 Llama 家族 的弱
339	    depth-transfer tradeoff 特征（可能因为 Llama 训练数据中多语言比例高于 Qwen， 导致深层 representation 已经部分语言对齐），加上
340	    MoE routing 碎片化效应， global rho 被进一步推向零。W4A16 量化可能引入额外 noise（权重 4-bit 但激活 16-bit，
341	    correctness probe 依赖的微弱方向性信号可能在权重量化中丢失部分精度）。 12 个 probed layers 的粗糙采样使得 per-language
342	    rho 高度不稳定， 微小的 AUROC 波动就能翻转 rho 方向。
343	
344	    '
345	  tables:
346	  - title: 'Table 3: Llama 4 Scout Zero-Shot Transfer AUROC (EN-optimal L40)'
347	    columns:
348	    - Language
349	    - Resource_Tier
350	    - ZS_AUROC
351	    - 95% CI
352	    rows:
353	    - - en
354	      - source
355	      - 0.74
356	      - '[0.72, 0.76]'
357	    - - zh
358	      - HIGH
359	      - 0.648
360	      - '[0.62, 0.67]'
361	    - - es
362	      - HIGH
363	      - 0.643
364	      - '[0.62, 0.67]'
365	    - - fr
366	      - HIGH
367	      - 0.635
368	      - '[0.61, 0.66]'
369	    - - de
370	      - HIGH
371	      - 0.628
372	      - '[0.60, 0.65]'
373	    - - ja
374	      - MID
375	      - 0.601
376	      - '[0.57, 0.63]'
377	    - - ru
378	      - MID
379	      - 0.588
380	      - '[0.56, 0.62]'
381	    - - ko
382	      - MID
383	      - 0.583
384	      - '[0.55, 0.61]'
385	    - - pt
386	      - MID
387	      - 0.595
388	      - '[0.57, 0.62]'
389	    - - hi
390	      - MID
391	      - 0.568
392	      - '[0.54, 0.60]'
393	    - - nl
394	      - MID
395	      - 0.575
396	      - '[0.54, 0.61]'
397	    - - pl
398	      - MID
399	      - 0.562
400	      - '[0.53, 0.59]'
401	    - - id
402	      - MID
403	      - 0.555
404	      - '[0.52, 0.59]'
405	    - - tr
406	      - MID
407	      - 0.548
408	      - '[0.52, 0.58]'
409	    - - vi
410	      - MID
411	      - 0.541
412	      - '[0.51, 0.57]'
413	    - - uk
414	      - MID
415	      - 0.545
416	      - '[0.51, 0.58]'
417	    - - ar
418	      - MID
419	      - 0.538
420	      - '[0.51, 0.57]'
421	    - - bn
422	      - LOW
423	      - 0.518
424	      - '[0.49, 0.55]'
425	    - - te
426	      - LOW
427	      - 0.505
428	      - '[0.47, 0.54]'
429	    - - sw
430	      - LOW
431	      - 0.495
432	      - '[0.46, 0.53]'
433	  - title: 'Table 4: Llama 4 Scout Pareto ρ per Language'
434	    columns:
435	    - Language
436	    - Spearman_rho
437	    - p_value
438	    - Significant
439	    rows:
440	    - - zh
441	      - -0.62
442	      - 0.031
443	      - ✓
444	    - - es
445	      - -0.38
446	      - 0.22
447	      - ✗
448	    - - fr
449	      - -0.29
450	      - 0.36
451	      - ✗
452	    - - de
453	      - -0.15
454	      - 0.64
455	      - ✗
456	    - - ja
457	      - -0.08
458	      - 0.8
459	      - ✗
460	    - - ru
461	      - 0.05
462	      - 0.88
463	      - ✗
464	    - - ko
465	      - 0.22
466	      - 0.49
467	      - ✗
468	    - - hi
469	      - 0.11
470	      - 0.73
471	      - ✗
472	    - - tr
473	      - 0.08
474	      - 0.8
475	      - ✗
476	    - - id
477	      - -0.03
478	      - 0.93
479	      - ✗
480	    - - pt
481	      - -0.18
482	      - 0.58
483	      - ✗
484	    - - nl
485	      - -0.12
486	      - 0.71
487	      - ✗
488	    - - pl
489	      - 0.15
490	      - 0.64
491	      - ✗
492	    - - vi
493	      - 0.25
494	      - 0.43
495	      - ✗
496	    - - uk
497	      - 0.03
498	      - 0.93
499	      - ✗
500	    - - ar
501	      - 0.18
502	      - 0.58
503	      - ✗
504	    - - bn
505	      - 0.28
506	      - 0.38
507	      - ✗
508	    - - te
509	      - 0.35
510	      - 0.26
511	      - ✗
512	    - - sw
513	      - 0.31
514	      - 0.33
515	      - ✗
516	    - - global
517	      - -0.05
518	      - 0.62
519	      - ✗
520	  figures_description:
521	  - 'Fig 3: Llama 4 Scout Pareto heatmap——几乎全为 noise，仅 zh 一行可见微弱梯度。'
522	  - 'Fig 4: 两架构 global rho 对比 bar chart（Qwen -0.18 vs Scout -0.05），两者 CI 均跨零。'
523	  analysis: 'Scout 上 Pareto 完全崩溃——global rho=-0.05 (p=0.62)，仅 zh 显著。n=12 的采样密度 使得统计检验力不足以检测中等效应。与
524	    Qwen3 对比：两个 MoE 架构都无法支撑 "clean architecture contrast"， 因为 rho 都不显著（Qwen -0.18
525	    p=0.12, Scout -0.05 p=0.62）。MVP 阶段观察到的 Qwen(strong)/Llama(weak) 对比在大模型上被 MoE noise
526	    冲刷。这强化了 worst tier 叙事：Pareto frontier 作为分析工具 仅在 7B dense + 高资源语言上有效——对 MoE 架构的泛化失败是方法论局限性的核心发现。
527	
528	    '
529	- name: CaCLR Comparative Evaluation (2 models × 20 langs × Pareto frontier)
530	  plan_id: plan_003
531	  description: 'CaCLR (L_BCE + α·L_SB-ECE + β·L_consistency) 与 zero-shot/mean-shift/linear
532	    projection/few-shot 在两个模型全 Pareto frontier 上的对比。α sweep (0.01-10.0), β sweep 3
533	    OOM (0.001-1.0)。
534	
535	    '
536	  expected_results:
537	    caclr_best_beta_auroc_delta_vs_zeroshot_avg: 0.002
538	    caclr_best_beta_auroc_delta_high_resource: 0.005
539	    caclr_best_beta_auroc_delta_low_resource: -0.008
540	    caclr_best_beta_auroc_delta_range:
541	    - -0.01
542	    - 0.005
543	    beta_0001_delta_auroc: 0.001
544	    beta_001_delta_auroc: 0.002
545	    beta_01_delta_auroc: 0.001
546	    beta_1_delta_auroc: -0.003
547	    beta_sweep_variance_across_seeds: 0.006
548	    caclr_delta_ece_vs_tempscaling_avg: 0.008
549	    caclr_delta_ece_vs_tempscaling_range:
550	    - -0.005
551	    - 0.02
552	    bce_only_auroc_delta: 0.0
553	    bce_sbece_auroc_delta: 0.001
554	    bce_mmd_auroc_delta: 0.002
555	    bce_sbece_mmd_auroc_delta: 0.002
556	    linear_proj_50pairs_delta_auroc_avg: 0.015
557	    linear_proj_50pairs_wins_over_caclr: 14/19 languages
558	    fewshot_25_delta_auroc_avg: 0.032
559	    fewshot_100_delta_auroc_avg: 0.061
560	    alpha_optimal: 0.1
561	    alpha_sensitivity: robust in [0.01, 1.0], degrades at α=10
562	  result_rationale: 'CaCLR 的 MMD consistency loss 在 1-D probe logit 空间上操作——这是根本性的设计缺陷。
563	    MMD 匹配的是 probe output 的边缘分布，但跨语言 correctness 失败的原因不是边缘分布不匹配， 而是条件分布 P(correct|representation)
564	    在不同语言上不同（Zhao et al. 2019 的核心结论）。 在 MoE 架构上，不同语言激活不同 expert 子集，representation
565	    space 的拓扑结构完全不同—— MMD 在低维投影空间上的匹配无法 capture 这种高维结构差异。 β sweep 跨 3 OOM 但 delta
566	    AUROC 始终在 noise level（±0.005），因为 MMD loss 的梯度信号太弱（1-D logit，bandwidth 由 median
567	    heuristic 决定，在接近正态的分布上 几乎所有 bandwidth 都给出相似的 gradient）。低资源语言上 CaCLR 甚至略微 hurt（-0.008），
568	    因为 MMD penalty 迫使 probe 偏离英语最优解但又无法真正对齐目标语言。 Linear projection（50 pairs）在 14/19
569	    语言上赢过 CaCLR，因为它直接学习子空间旋转 而不是间接匹配分布。但 linear projection 本身在低资源上不稳定（seed variance
570	    高）。
571	
572	    '
573	  tables:
574	  - title: 'Table 5: Transfer Method Comparison — Δ AUROC vs Zero-Shot (Qwen3-235B,
575	      EN-optimal layer)'
576	    columns:
577	    - Method
578	    - HIGH_avg
579	    - MID_avg
580	    - LOW_avg
581	    - ALL_avg
582	    - Wins/19
583	    rows:
584	    - - Mean-shift
585	      - 0.0
586	      - 0.0
587	      - 0.0
588	      - 0.0
589	      - 0/19
590	    - - CaCLR (best β)
591	      - 0.005
592	      - 0.003
593	      - -0.008
594	      - 0.002
595	      - 8/19
596	    - - Linear proj (50)
597	      - 0.025
598	      - 0.015
599	      - -0.005
600	      - 0.015
601	      - 14/19
602	    - - Few-shot (25)
603	      - 0.038
604	      - 0.03
605	      - 0.022
606	      - 0.032
607	      - 17/19
608	    - - Few-shot (100)
609	      - 0.072
610	      - 0.058
611	      - 0.045
612	      - 0.061
613	      - 19/19
614	  - title: 'Table 6: CaCLR β Sweep (avg Δ AUROC across 20 langs, Qwen3-235B)'
615	    columns:
616	    - β
617	    - Δ_AUROC_mean
618	    - Δ_AUROC_std
619	    - Δ_ECE_mean
620	    - p (vs ZS)
621	    rows:
622	    - - 0.001
623	      - 0.001
624	      - 0.006
625	      - 0.003
626	      - 0.72
627	    - - 0.01
628	      - 0.002
629	      - 0.007
630	      - 0.005
631	      - 0.58
632	    - - 0.1
633	      - 0.001
634	      - 0.008
635	      - 0.008
636	      - 0.63
637	    - - 1.0
638	      - -0.003
639	      - 0.011
640	      - 0.012
641	      - 0.41
642	    - - 0 (BCE only)
643	      - 0.0
644	      - 0.005
645	      - 0.001
646	      - —
647	  - title: 'Table 7: CaCLR Component Ablation (Qwen3-235B, avg 20 langs)'
648	    columns:
649	    - Components
650	    - Δ_AUROC
651	    - Δ_ECE
652	    - Note
653	    rows:
654	    - - BCE only
655	      - 0.0
656	      - 0.001
657	      - baseline (= zero-shot retrain)
658	    - - BCE + SB-ECE
659	      - 0.001
660	      - -0.002
661	      - α=0.1; ECE marginally better
662	    - - BCE + MMD
663	      - 0.002
664	      - 0.004
665	      - β=0.01; MMD alone slightly helps AUROC but hurts ECE
666	    - - BCE + SB-ECE + MMD
667	      - 0.002
668	      - 0.006
669	      - joint ≈ max of components, no synergy
670	  figures_description:
671	  - 'Fig 5: β sweep curve (x=log β, y=Δ AUROC) with 95% CI——flat line 在零附近，所有 CI 跨零。'
672	  - 'Fig 6: 5-method transfer comparison grouped bar chart (high/mid/low resource)——CaCLR
673	    与 zero-shot 不可区分，linear projection 和 few-shot 逐步改善。'
674	  - 'Fig 7: Per-language CaCLR Δ AUROC scatter (x=resource tier proxy, y=delta)——低资源侧系统性偏负。'
675	  analysis: 'CaCLR 的 consistency loss 完全 inert。β sweep 跨 3 个数量级（0.001→1.0）， 平均 Δ AUROC
676	    从未超过 noise level（+0.002 ± 0.007）。配对置换检验 p 值全部 >0.4。 Component ablation 确认：SB-ECE
677	    提供微弱 ECE 改善（-0.002），MMD 提供微弱 AUROC 改善（+0.002）， 但两者无协同效应，且均在 noise 范围内。核心 negative
678	    result：MMD-based distributional matching 对 correctness probe transfer 无效——与 Zhao
679	    et al. (2019) 理论预测一致（边缘匹配在条件分布不同时失效）。 Linear projection（50 pairs）作为最强 zero-label
680	    替代方案，但在低资源语言上也不稳定。 Few-shot 25/100 是唯一 consistently 有效的路径——支持 "constructive path
681	    forward" 叙事。
682	
683	    '
684	- name: Difficulty-Controlled Decomposition Ablation (10 langs × 8 layers × 2 models)
685	  plan_id: plan_004
686	  description: '训练 IRT difficulty probes，投影出 difficulty direction，在 residuals 上重训
687	    correctness probes， 评估 transfer。10 种代表性语言 × 8 层 × 2 模型。含 random-direction control。
688	
689	    '
690	  expected_results:
691	    difficulty_probe_r2_en_avg: 0.35
692	    difficulty_probe_r2_range:
693	    - 0.18
694	    - 0.48
695	    en_auroc_after_projection_avg_delta: -0.025
696	    difficulty_projection_transfer_delta_high_resource: 0.012
697	    difficulty_projection_transfer_delta_mid_resource: 0.003
698	    difficulty_projection_transfer_delta_low_resource: -0.008
699	    difficulty_projection_transfer_delta_avg: 0.005
700	    difficulty_projection_transfer_delta_range:
701	    - -0.01
702	    - 0.015
703	    random_projection_transfer_delta_avg: -0.015
704	    random_vs_difficulty_significant: 4/10 languages (all high-resource)
705	    difficulty_shared_fraction_estimate: 0.20-0.55 range across langs, no consistent
706	      pattern
707	    capability_specific_fraction_variance: high (std=0.18 across languages)
708	  result_rationale: 'Decomposition 在 worst tier 下被 noise dominate，原因有三： (1) IRT difficulty
709	    scores 本身 noisy（GlobalMMLU 的 difficulty 基于 human performance， 与 LLM-perceived
710	    difficulty 仅中等相关，r²~0.35）； (2) MoE 架构中 difficulty direction 不是一条 clean linear
711	    direction——不同 expert  以不同方式 encode difficulty，Ridge regression 只能捕获 average effect；
712	    (3) 投影出 difficulty 后的 residual space 维度仍然很高（4096-D），correctness probe  在 residuals
713	    上重训的 noise floor 与原始空间接近。 结果：projecting out difficulty 对 transfer 的平均效果极小（+0.005），
714	    且高度 language-dependent。高资源语言略有改善（+0.012，因为 difficulty 确实是 shared component）， 低资源语言反而变差（-0.008，因为
715	    difficulty probe 本身在低资源上就不准确， 投影出的实际上是 noise direction）。Random-direction control
716	    确认投影本身 会降低信号（-0.015），difficulty projection 只是 "比 random 好一点"， 但差异仅在 4/10 语言上显著——无法支撑
717	    "decomposition is prescriptive" 的强 claim。
718	
719	    '
720	  tables:
721	  - title: 'Table 8: Difficulty Decomposition — Transfer Δ AUROC (vs no-projection
722	      baseline)'
723	    columns:
724	    - Language
725	    - Tier
726	    - Difficulty_proj_Δ
727	    - Random_proj_Δ
728	    - Diff-Rand gap
729	    - p_value
730	    rows:
731	    - - zh
732	      - HIGH
733	      - 0.015
734	      - -0.012
735	      - 0.027
736	      - 0.031
737	    - - es
738	      - HIGH
739	      - 0.013
740	      - -0.014
741	      - 0.027
742	      - 0.028
743	    - - fr
744	      - HIGH
745	      - 0.011
746	      - -0.016
747	      - 0.027
748	      - 0.035
749	    - - de
750	      - HIGH
751	      - 0.008
752	      - -0.013
753	      - 0.021
754	      - 0.062
755	    - - hi
756	      - MID
757	      - 0.005
758	      - -0.015
759	      - 0.02
760	      - 0.088
761	    - - ru
762	      - MID
763	      - 0.003
764	      - -0.018
765	      - 0.021
766	      - 0.075
767	    - - ko
768	      - MID
769	      - 0.002
770	      - -0.014
771	      - 0.016
772	      - 0.145
773	    - - tr
774	      - MID
775	      - 0.001
776	      - -0.017
777	      - 0.018
778	      - 0.118
779	    - - sw
780	      - LOW
781	      - -0.005
782	      - -0.019
783	      - 0.014
784	      - 0.212
785	    - - bn
786	      - LOW
787	      - -0.01
788	      - -0.016
789	      - 0.006
790	      - 0.481
791	  figures_description:
792	  - 'Fig 8: Decomposition effect scatter (x=resource tier, y=Δ transfer AUROC) with
793	    difficulty vs random overlay——两条线接近，difficulty 仅略高。'
794	  analysis: 'Decomposition 效果被 noise dominate。平均 +0.005 transfer delta 远小于 few-shot
795	    25 的 +0.032。 "Difficulty-shared vs capability-specific" 分解的 fraction 估计高度不稳定（std=0.18），
796	    无法形成 consistent 叙事。对 worst tier：Claim 2 需要大幅弱化——从 "prescriptive decomposition"
797	    降为 "exploratory decomposition suggests difficulty component exists but is not
798	    cleanly separable in MoE architectures"。仍有方法论价值（展示了 how to decompose），但不是 strong
799	    empirical finding。
800	
801	    '
802	- name: Cross-Lingual Orthogonality Analysis (20 langs × 2 architectures)
803	  plan_id: plan_005
804	  description: '提取 verbalized confidence direction，计算与 correctness direction 的 cosine
805	    similarity， 20 种语言 × 2 架构。按 resource tier 和 language family 分析。
806	
807	    '
808	  expected_results:
809	    cosine_median_all: 0.06
810	    cosine_range:
811	    - 0.02
812	    - 0.18
813	    cosine_below_004_fraction: 7/40 (17.5%)
814	    cosine_above_010_fraction: 12/40 (30%)
815	    cosine_above_015_fraction: 6/40 (15%)
816	    cosine_high_resource_mean: 0.04
817	    cosine_mid_resource_mean: 0.07
818	    cosine_low_resource_mean: 0.13
819	    cosine_qwen_mean: 0.07
820	    cosine_scout_mean: 0.08
821	    worst_lang_cosine: 'sw@Scout: 0.18'
822	    worst_cases_above_015:
823	    - sw@Scout
824	    - bn@Scout
825	    - te@Qwen
826	    - sw@Qwen
827	    - bn@Qwen
828	    - te@Scout
829	  result_rationale: 'Miao & Ungar (2026) 在英语 7-8B 上报告 cosine<0.04（近乎正交）。 在大模型 MoE
830	    + 多语言设置下正交性部分退化，原因： (1) MoE expert 内部空间维度有效降低——当 correctness 和 confidence 信号都被
831	    route 到 少量共享 expert 时，方向会更 "拥挤"，cosine 从零偏移； (2) 低资源语言的 confidence direction 本身就
832	    noisy（模型在低资源上的 verbalized confidence 更随机，probe 拟合的方向不稳定），noise 方向与 correctness
833	    的 cosine 期望值 ~1/√d 而非精确零； (3) 部分低资源语言（sw, bn, te）可能存在 capacity artifact——probe
834	    学到的不是真正的 correctness/confidence 方向而是 dataset regularities，这两种 artifact 方向可能有非零相关。
835	    高资源语言维持 cosine~0.04，但 15% 的 lang×arch 组合 cosine>0.15， "universally orthogonal"
836	    的表述不再成立。
837	
838	    '
839	  tables:
840	  - title: 'Table 9: Correctness-Confidence Cosine Similarity (selected languages
841	      × 2 architectures)'
842	    columns:
843	    - Language
844	    - Tier
845	    - Qwen3_cosine
846	    - Scout_cosine
847	    - Avg
848	    rows:
849	    - - en
850	      - source
851	      - 0.03
852	      - 0.03
853	      - 0.03
854	    - - zh
855	      - HIGH
856	      - 0.04
857	      - 0.03
858	      - 0.035
859	    - - es
860	      - HIGH
861	      - 0.03
862	      - 0.04
863	      - 0.035
864	    - - fr
865	      - HIGH
866	      - 0.04
867	      - 0.05
868	      - 0.045
869	    - - de
870	      - HIGH
871	      - 0.04
872	      - 0.04
873	      - 0.04
874	    - - ja
875	      - MID
876	      - 0.05
877	      - 0.06
878	      - 0.055
879	    - - ru
880	      - MID
881	      - 0.05
882	      - 0.06
883	      - 0.055
884	    - - ko
885	      - MID
886	      - 0.06
887	      - 0.07
888	      - 0.065
889	    - - hi
890	      - MID
891	      - 0.07
892	      - 0.08
893	      - 0.075
894	    - - tr
895	      - MID
896	      - 0.08
897	      - 0.09
898	      - 0.085
899	    - - ar
900	      - MID
901	      - 0.06
902	      - 0.07
903	      - 0.065
904	    - - bn
905	      - LOW
906	      - 0.12
907	      - 0.14
908	      - 0.13
909	    - - te
910	      - LOW
911	      - 0.15
912	      - 0.13
913	      - 0.14
914	    - - sw
915	      - LOW
916	      - 0.14
917	      - 0.18
918	      - 0.16
919	  figures_description:
920	  - 'Fig 9: Cosine similarity heatmap (lang × arch)——高资源区域冷色（<0.05），低资源区域暖色（>0.10），清晰的
921	    resource-tier gradient。'
922	  - 'Fig 10: Cosine vs resource tier scatter with regression line——正相关，r=-0.65（resource
923	    level 越低 cosine 越高）。'
924	  analysis: 'Orthogonality 在高资源语言上 robustly holds（cosine<0.05），但低资源语言系统性偏离， 15% 的
925	    lang×arch 组合 cosine>0.15。这意味着 "correctness-confidence orthogonality is universal"
926	    (Miao & Ungar) 需要 qualify——仅在 resource-adequate languages 上成立。 对 worst tier：这是有价值的发现，但方向从
927	    "positive extension" 变为 "qualification + warning"。 需要讨论 capacity artifact 的混淆：低资源
928	    cosine 升高可能不是 "真正的结构性非正交"， 而是 probe quality 太差导致方向估计 noisy。与 plan_013 control
929	    task 结果联合解读。
930	
931	    '
932	- name: 'Probe Complexity: Logistic Regression vs 2-Layer MLP (2 models × all layers)'
933	  plan_id: plan_006
934	  description: '比较 LR 和 2-layer MLP 在两个模型每层上的英语 AUROC、cross-lingual transfer degradation
935	    和 calibration 质量。
936	
937	    '
938	  expected_results:
939	    mlp_en_auroc_advantage_avg: 0.025
940	    mlp_en_auroc_advantage_range:
941	    - 0.01
942	    - 0.04
943	    lr_zs_transfer_degradation_avg: 0.155
944	    mlp_zs_transfer_degradation_avg: 0.195
945	    mlp_zs_degradation_excess: 0.04
946	    mlp_excess_degradation_high: 0.02
947	    mlp_excess_degradation_mid: 0.04
948	    mlp_excess_degradation_low: 0.065
949	    lr_ece_avg: 0.18
950	    mlp_ece_avg: 0.22
951	    lr_transfers_better_significant: 14/19 languages (bootstrap p<0.05)
952	  result_rationale: 'Linear probes transfer better cross-lingually 这个假设在 7B dense
953	    上 well-supported （更简单的 probe 拟合的 direction 更 language-agnostic），在大模型 MoE 上同样成立但差异更大。
954	    MLP 在英语上多学到 ~2.5pp（利用非线性语言特异性模式），但这些模式在 transfer 时成为负担。 MoE 架构放大了这个效应：MLP 可以学习
955	    expert-routing-dependent 的非线性模式， 这些模式在不同语言 routing 不同时完全不 transfer。低资源上 MLP excess
956	    degradation 最大（6.5pp）， 因为低资源语言的 expert routing 与英语差异最大。 这支持了 "linear probe is
957	    the right methodological choice" 但也意味着 probe 捕获的信号上限 被 linearity constraint 限制——在
958	    MoE 上，correctness signal 可能本质上需要非线性访问。
959	
960	    '
961	  tables:
962	  - title: 'Table 10: Probe Complexity — LR vs MLP (Qwen3-235B, EN-optimal layer)'
963	    columns:
964	    - Metric
965	    - LR
966	    - MLP
967	    - Δ
968	    - p_value
969	    rows:
970	    - - EN AUROC
971	      - 0.76
972	      - 0.785
973	      - 0.025
974	      - <0.001
975	    - - ZS AUROC avg (20 lang)
976	      - 0.59
977	      - 0.575
978	      - -0.015
979	      - 0.042
980	    - - Transfer degradation avg
981	      - 0.155
982	      - 0.195
983	      - 0.04
984	      - 0.008
985	    - - ECE avg (20 lang)
986	      - 0.18
987	      - 0.22
988	      - 0.04
989	      - 0.015
990	  figures_description:
991	  - 'Fig 11: LR vs MLP transfer degradation scatter (x=LR degradation, y=MLP degradation)
992	    per language——所有点在 y=x 线上方，MLP 一致更差。'
993	  analysis: '确认 linear probe 是跨语言 transfer 的正确选择。MLP 的英语优势（+2.5pp）在 transfer 中 被完全
994	    offset 且反转。方法论含义：correctness signal 的 linearly accessible component 是唯一 cross-lingually
995	    stable 的部分。这与 "low-dimensional language-agnostic subspace" 叙事一致。
996	
997	    '
998	- name: Belebele + MMLU-ProX Generalization (20 langs × best probes + CaCLR)
999	  plan_id: plan_007
1000	  description: '在 Belebele（阅读理解）和 MMLU-ProX（20 languages）上评估最佳 probes 和 CaCLR， 验证
1001	    GlobalMMLU 之外的泛化。
1002	
1003	    '
1004	  expected_results:
1005	    belebele_en_auroc: 0.72
1006	    belebele_zs_avg_20lang: 0.56
1007	    belebele_vs_globalmmlu_en_delta: -0.04
1008	    belebele_vs_globalmmlu_zs_delta: -0.03
1009	    belebele_caclr_delta_vs_zs: 0.001
1010	    belebele_rank_correlation_with_globalmmlu: 0.82
1011	    mmlupx_en_auroc: 0.74
1012	    mmlupx_zs_avg_20lang: 0.57
1013	    mmlupx_vs_globalmmlu_en_delta: -0.02
1014	    mmlupx_vs_globalmmlu_zs_delta: -0.02
1015	    mmlupx_caclr_delta_vs_zs: 0.002
1016	    mmlupx_rank_correlation_with_globalmmlu: 0.88
1017	    language_ranking_kendall_tau: 0.78
1018	    low_resource_auroc_drop_consistent: true
1019	  result_rationale: 'Belebele 是阅读理解任务（与 MCQA knowledge 不同），correctness probe 的 transferability  预期更差因为
1020	    task-specific 信号不同。MMLU-ProX 与 GlobalMMLU 同源但翻译质量可能不同， 期望更高一致性。两个 benchmark 上的绝对性能均低于
1021	    GlobalMMLU（因为 probe 是在 GlobalMMLU 上训练的）， 但语言排序高度一致（Kendall tau=0.78），说明 cross-lingual
1022	    transfer degradation pattern 是 task-general 的。CaCLR 在两个 benchmark 上同样 inert（delta~0），进一步确认负面结果
1023	    不是 benchmark-specific artifact。
1024	
1025	    '
1026	  tables:
1027	  - title: 'Table 11: Cross-Benchmark Generalization (Qwen3-235B)'
1028	    columns:
1029	    - Benchmark
1030	    - EN_AUROC
1031	    - ZS_avg
1032	    - CaCLR_Δ
1033	    - Rank_corr_w_GlobalMMLU
1034	    rows:
1035	    - - GlobalMMLU
1036	      - 0.76
1037	      - 0.59
1038	      - 0.002
1039	      - —
1040	    - - Belebele
1041	      - 0.72
1042	      - 0.56
1043	      - 0.001
1044	      - 0.82
1045	    - - MMLU-ProX
1046	      - 0.74
1047	      - 0.57
1048	      - 0.002
1049	      - 0.88
1050	  figures_description:
1051	  - 'Fig 12: 三 benchmark 语言排序 parallel coordinates plot——高度一致的降序趋势。'
1052	  analysis: 'Cross-benchmark generalization 支持 findings 的 robustness：language ranking
1053	    一致（tau=0.78）， CaCLR 一致 inert，low-resource drop 一致。Belebele 上 AUROC 稍低（阅读理解 vs
1054	    知识 MCQA）， 但 degradation pattern 相同。这为 "viability boundary" 提供了 cross-task evidence。
1055	
1056	    '
1057	- name: Quantization Validation Ablation (W4A16 vs FP16 / INT4 vs FP16)
1058	  plan_id: plan_010
1059	  description: '(a) Llama 4 Scout W4A16 vs FP16 at 5 layers on 5% subset; (b) Qwen3-235B
1060	    GPTQ-Int4 vs FP16 at 5 layers on 5% subset.
1061	
1062	    '
1063	  expected_results:
1064	    scout_w4a16_vs_fp16_auroc_delta_avg: -0.008
1065	    scout_w4a16_vs_fp16_auroc_delta_range:
1066	    - -0.015
1067	    - 0.002
1068	    scout_w4a16_vs_fp16_correlation: 0.985
1069	    scout_w4a16_vs_fp16_rank_agreement: 98%
1070	    qwen_int4_vs_fp16_auroc_delta_avg: -0.012
1071	    qwen_int4_vs_fp16_auroc_delta_range:
1072	    - -0.022
1073	    - -0.003
1074	    qwen_int4_vs_fp16_correlation: 0.978
1075	    qwen_int4_vs_fp16_rank_agreement: 96%
1076	    deep_layer_quant_delta: -0.018
1077	    shallow_layer_quant_delta: -0.005
1078	  result_rationale: '量化（INT4/W4A16）对 correctness probe 的影响在 worst tier 下比 best tier
1079	    更大， 但仍在可接受范围内。4-bit 权重量化引入的噪声在浅层影响小（-0.005 AUROC）， 在深层影响更大（-0.018），因为深层 representation
1080	    的 correctness signal 更细微 （signal-to-noise ratio 更低），量化 noise 更容易掩盖信号。 Qwen3-235B
1081	    的 INT4 (GPTQ) 影响比 Scout W4A16 更大（-0.012 vs -0.008）， 因为 GPTQ 是 post-training quantization
1082	    而 W4A16 保留了 16-bit 激活。 但 rank agreement >96% 说明量化不改变 per-item correctness 排序——
1083	    AUROC 降低主要来自 decision boundary 模糊，不是信号方向改变。 结论：量化引入的 AUROC 降低（~1pp）远小于 cross-lingual
1084	    transfer degradation（~10-15pp）， 不影响核心发现。需要在论文中报告为 limitation。
1085	
1086	    '
1087	  tables:
1088	  - title: 'Table 12: Quantization Impact on Probe AUROC'
1089	    columns:
1090	    - Model
1091	    - Quant
1092	    - Layer
1093	    - FP16_AUROC
1094	    - Quant_AUROC
1095	    - Δ
1096	    rows:
1097	    - - Scout
1098	      - W4A16
1099	      - L8
1100	      - 0.645
1101	      - 0.642
1102	      - -0.003
1103	    - - Scout
1104	      - W4A16
1105	      - L16
1106	      - 0.668
1107	      - 0.66
1108	      - -0.008
1109	    - - Scout
1110	      - W4A16
1111	      - L24
1112	      - 0.695
1113	      - 0.685
1114	      - -0.01
1115	    - - Scout
1116	      - W4A16
1117	      - L32
1118	      - 0.718
1119	      - 0.706
1120	      - -0.012
1121	    - - Scout
1122	      - W4A16
1123	      - L40
1124	      - 0.74
1125	      - 0.725
1126	      - -0.015
1127	    - - Qwen3
1128	      - INT4
1129	      - L16
1130	      - 0.64
1131	      - 0.635
1132	      - -0.005
1133	    - - Qwen3
1134	      - INT4
1135	      - L36
1136	      - 0.685
1137	      - 0.675
1138	      - -0.01
1139	    - - Qwen3
1140	      - INT4
1141	      - L52
1142	      - 0.72
1143	      - 0.705
1144	      - -0.015
1145	    - - Qwen3
1146	      - INT4
1147	      - L72
1148	      - 0.762
1149	      - 0.742
1150	      - -0.02
1151	    - - Qwen3
1152	      - INT4
1153	      - L88
1154	      - 0.745
1155	      - 0.723
1156	      - -0.022
1157	  figures_description:
1158	  - 'Fig 13: FP16 vs Quantized AUROC scatter per layer——点紧贴 y=x 线但系统性偏下，深层偏移更大。'
1159	  analysis: '量化影响存在但可控。深层损失更大是预期的（信号更弱），但 rank agreement >96%  保证了相对 ordering 可信。Worst
1160	    tier 下这个结果的含义：已经偏低的 EN AUROC（0.76） 中约 1-2pp 来自量化 artifact，真实 FP16 AUROC 可能在 0.77-0.78
1161	    区间—— 但即使如此也远低于 best tier 预期的 0.82+。在论文中作为 acknowledged limitation 报告。
1162	
1163	    '
1164	- name: CKA Full-Scale Analysis (20 langs × all layers × 2 models)
1165	  plan_id: plan_011
1166	  description: '计算 CKA（linear kernel）between English and each target language at every
1167	    probed layer。 包含 partial correlation controlling depth、same-layer cross-language
1168	    correlation、 per-language Spearman、subspace angle analysis。
1169	
1170	    '
1171	  expected_results:
1172	    cka_degradation_pooled_rho_qwen: -0.28
1173	    cka_degradation_pooled_p_qwen: 0.008
1174	    cka_degradation_pooled_rho_scout: -0.35
1175	    cka_degradation_pooled_p_scout: 0.003
1176	    cka_partial_corr_controlling_depth_qwen: 0.04
1177	    cka_partial_corr_p_qwen: 0.58
1178	    cka_partial_corr_controlling_depth_scout: 0.08
1179	    cka_partial_corr_p_scout: 0.35
1180	    same_layer_cka_vs_degradation_rho_avg: -0.42
1181	    same_layer_significant_layers: 3/24 Qwen, 2/12 Scout
1182	    per_lang_rho_significant_count_qwen: 4/19
1183	    per_lang_rho_significant_count_scout: 2/19
1184	    per_lang_rho_reversed_count: 3/19 (ko, vi, te)
1185	    cka_cliff_depth_qwen: 75-85% depth
1186	    cka_cliff_depth_scout: 70-80% depth
1187	    cka_cliff_steepness_qwen: -0.08
1188	    cka_cliff_steepness_scout: -0.05
1189	    subspace_angle_range:
1190	    - 12
1191	    - 58
1192	    subspace_angle_high_resource_mean: 18
1193	    subspace_angle_low_resource_mean: 45
1194	  result_rationale: 'CKA partial correlation controlling depth 是决定性分析——在 worst tier
1195	    下完全 n.s. （Qwen r=0.04 p=0.58, Scout r=0.08 p=0.35）。这意味着 pilot 阶段观察到的 CKA-degradation
1196	    负相关（Llama rho=-0.52 p=0.001）主要被 depth confound 驱动： 深层 CKA 低 + 深层 transfer 差，但这不是因为
1197	    "CKA 低导致 transfer 差"， 而是 "depth 同时驱动两者"。控制 depth 后 CKA 的独立解释力归零。 Pooled correlation
1198	    仍显著（p<0.01），但这是 Simpson''s paradox 的变体—— between-language 差异（高资源 CKA 高 + degradation
1199	    低 vs 低资源反之） 和 within-language depth 效应混淆。Same-layer 分析（n=19 per layer）部分有效： 在给定层深度，CKA
1200	    较高的语言确实 transfer 更好（rho=-0.42）， 但仅在少数层（5/36）达到显著——样本量不够或 CKA range 太窄。 结论：CKA
1201	    从 "geometric analysis" 降级为 "suggestive correlational observation"。
1202	
1203	    '
1204	  tables:
1205	  - title: 'Table 13: CKA Partial Correlation Controlling Depth (THE critical test)'
1206	    columns:
1207	    - Model
1208	    - Partial_r
1209	    - p_value
1210	    - Pooled rho (no control)
1211	    - Pooled p
1212	    - Interpretation
1213	    rows:
1214	    - - Qwen3-235B
1215	      - 0.04
1216	      - 0.58
1217	      - -0.28
1218	      - 0.008
1219	      - depth confound explains all
1220	    - - Llama 4 Scout
1221	      - 0.08
1222	      - 0.35
1223	      - -0.35
1224	      - 0.003
1225	      - depth confound explains all
1226	  - title: 'Table 14: Same-Layer CKA vs Degradation (Qwen3-235B, representative layers)'
1227	    columns:
1228	    - Layer
1229	    - n (langs)
1230	    - rho
1231	    - p_value
1232	    - Significant
1233	    rows:
1234	    - - L16
1235	      - 19
1236	      - -0.35
1237	      - 0.14
1238	      - ✗
1239	    - - L32
1240	      - 19
1241	      - -0.48
1242	      - 0.037
1243	      - ✓
1244	    - - L48
1245	      - 19
1246	      - -0.52
1247	      - 0.022
1248	      - ✓
1249	    - - L64
1250	      - 19
1251	      - -0.41
1252	      - 0.081
1253	      - ✗
1254	    - - L72
1255	      - 19
1256	      - -0.45
1257	      - 0.053
1258	      - ✗
1259	    - - L80
1260	      - 19
1261	      - -0.38
1262	      - 0.11
1263	      - ✗
1264	    - - L88
1265	      - 19
1266	      - -0.28
1267	      - 0.24
1268	      - ✗
1269	  - title: 'Table 15: Subspace Angle (degrees) between EN and Target Correctness Direction'
1270	    columns:
1271	    - Language
1272	    - Tier
1273	    - L48_angle
1274	    - L72_angle
1275	    - L88_angle
1276	    rows:
1277	    - - zh
1278	      - HIGH
1279	      - 15
1280	      - 22
1281	      - 35
1282	    - - es
1283	      - HIGH
1284	      - 14
1285	      - 20
1286	      - 32
1287	    - - de
1288	      - HIGH
1289	      - 18
1290	      - 25
1291	      - 38
1292	    - - ko
1293	      - MID
1294	      - 25
1295	      - 35
1296	      - 48
1297	    - - hi
1298	      - MID
1299	      - 28
1300	      - 38
1301	      - 52
1302	    - - sw
1303	      - LOW
1304	      - 38
1305	      - 48
1306	      - 58
1307	    - - bn
1308	      - LOW
1309	      - 35
1310	      - 45
1311	      - 55
1312	    - - te
1313	      - LOW
1314	      - 40
1315	      - 50
1316	      - 58
1317	  figures_description:
1318	  - 'Fig 14: CKA × layer heatmap (20 langs × 24 layers, Qwen3)——clear depth gradient
1319	    从黄(high CKA)到蓝(low CKA)，但 between-language variance 有限。'
1320	  - 'Fig 15: Partial correlation forest plot——CI 宽且跨零，与 pooled correlation 的显著结果形成鲜明对比。'
1321	  - 'Fig 16: Subspace angle vs depth (3 resource tiers)——所有 tier 随深度增加但低资源起点就高，斜率无显著
1322	    tier 差异。'
1323	  analysis: 'CKA 分析的核心发现是负面的：partial correlation 控制 depth 后 n.s.。 这在 worst tier 叙事中反而成为贡献——证明了
1324	    naively 使用 CKA 解释 transfer degradation  是 misleading 的（depth confound），这是对 CKA-based
1325	    representation analysis 方法论的 warning。 Same-layer 分析保留了 "languages with higher
1326	    CKA transfer better" 的弱 claim（between-language）， 但不足以支撑 "CKA 作为 transfer 预测器"
1327	    的 quantitative tool。 Subspace angle 分析提供了更直接的 geometric evidence：correctness direction
1328	    的  language specialization 随深度增加，低资源语言的 angle 在浅层就已经很大（35-40°）， 说明 representation
1329	    从未真正 align。
1330	
1331	    '
1332	- name: Linear Projection Sample Efficiency (10-200 pairs × 20 langs × 2 models)
1333	  plan_id: plan_012
1334	  description: '变化 parallel pair 数量 (10, 20, 50, 100, 200)，评估 linear projection transfer，
1335	    2 模型 × 5 representative layers × 20 语言。
1336	
1337	    '
1338	  expected_results:
1339	    proj_10pairs_auroc_delta: 0.005
1340	    proj_20pairs_auroc_delta: 0.01
1341	    proj_50pairs_auroc_delta: 0.015
1342	    proj_100pairs_auroc_delta: 0.022
1343	    proj_200pairs_auroc_delta: 0.028
1344	    proj_10pairs_std: 0.032
1345	    proj_20pairs_std: 0.025
1346	    proj_50pairs_std: 0.02
1347	    proj_100pairs_std: 0.014
1348	    proj_200pairs_std: 0.01
1349	    proj_50_high_resource_delta: 0.025
1350	    proj_50_mid_resource_delta: 0.015
1351	    proj_50_low_resource_delta: -0.005
1352	    proj_50_low_resource_std: 0.028
1353	    min_pairs_for_positive_avg_delta: 20
1354	    min_pairs_for_consistent_improvement: 100 (still fails for sw, bn, te)
1355	    proj_50_wins_over_zeroshot: 14/19 languages
1356	    proj_50_significantly_better: 7/19 languages (bootstrap p<0.05)
1357	  result_rationale: 'Linear projection 在 worst tier 下表现不稳定，核心原因是 MoE 架构的高维异质性。 50
1358	    parallel pairs 学习的 rotation matrix 有效自由度为 min(50, d)=50 远小于 d=4096， 只能 capture
1359	    低秩近似。在高资源语言上这足够了（correctness subspace 旋转 angle 小， 低秩近似够用），但低资源语言 angle 大（45-58°）且
1360	    variance 高，50 pairs 不足以 稳定估计旋转矩阵。200 pairs 改善了稳定性但 delta 仍然只有 +0.028 avg—— 说明瓶颈不只是
1361	    estimation noise，而是 correctness direction 在低资源上可能不存在  clean linear correspondence（capacity
1362	    artifact 问题，见 plan_013）。 Low resource 上 10-50 pairs 的 delta 可以是负的（-0.005 at 50
1363	    pairs）， 说明 learned projection 比 identity map（zero-shot）更差——投影 noise 比不投影更有害。
1364	
1365	    '
1366	  tables:
1367	  - title: 'Table 16: Linear Projection — Δ AUROC by Pair Count (avg across 20 langs,
1368	      Qwen3-235B)'
1369	    columns:
1370	    - N_pairs
1371	    - Δ_AUROC_avg
1372	    - std
1373	    - Wins/19
1374	    - Sig wins (p<0.05)
1375	    rows:
1376	    - - 10
1377	      - 0.005
1378	      - 0.032
1379	      - 10/19
1380	      - 2/19
1381	    - - 20
1382	      - 0.01
1383	      - 0.025
1384	      - 12/19
1385	      - 4/19
1386	    - - 50
1387	      - 0.015
1388	      - 0.02
1389	      - 14/19
1390	      - 7/19
1391	    - - 100
1392	      - 0.022
1393	      - 0.014
1394	      - 16/19
1395	      - 10/19
1396	    - - 200
1397	      - 0.028
1398	      - 0.01
1399	      - 17/19
1400	      - 13/19
1401	  - title: 'Table 17: Linear Projection 50 Pairs — By Resource Tier'
1402	    columns:
1403	    - Tier
1404	    - Δ_AUROC_avg
1405	    - std
1406	    - Sig improvement
1407	    rows:
1408	    - - HIGH (4 langs)
1409	      - 0.025
1410	      - 0.012
1411	      - 3/4
1412	    - - MID (13 langs)
1413	      - 0.015
1414	      - 0.018
1415	      - 4/13
1416	    - - LOW (3 langs)
1417	      - -0.005
1418	      - 0.028
1419	      - 0/3
1420	  figures_description:
1421	  - 'Fig 17: Sample efficiency curve (x=N pairs, y=Δ AUROC) with 3 tier bands——HIGH
1422	    快速饱和，MID 缓慢爬升，LOW 在零附近或偏负。'
1423	  - 'Fig 18: Per-language 50-pair Δ AUROC bar chart sorted by magnitude——clear resource-tier
1424	    gradient。'
1425	  analysis: 'Linear projection 是 "surprisingly strong baseline" 但仅限于高/中资源语言。 在低资源上不稳定（std>0.028）且平均效果为负。200
1426	    pairs 是 practical minimum for consistency 但 3 种低资源语言 even at 200 pairs 仍未一致改善。这为
1427	    viability boundary 提供了 另一条 evidence line：linear alignment 需要 source-target correctness
1428	    subspace 有足够 overlap， 低资源语言不满足这个前提条件。
1429	
1430	    '
1431	- name: Probing Control Tasks — Full 20 Languages × 2 Models
1432	  plan_id: plan_013
1433	  description: '在 20 语言 × 2 模型上训练 control probes（permuted labels），计算 selectivity。
1434	    已完成英语 Qwen-7B baseline（plan_013 registry），现扩展到大模型全语言。
1435	
1436	    '
1437	  expected_results:
1438	    selectivity_below_005_fraction_overall: 0.38
1439	    selectivity_below_005_fraction_high_resource: 0.15
1440	    selectivity_below_005_fraction_mid_resource: 0.35
1441	    selectivity_below_005_fraction_low_resource: 0.72
1442	    selectivity_below_005_qwen: 0.35
1443	    selectivity_below_005_scout: 0.41
1444	    selectivity_below_005_shallow_half: 0.55
1445	    selectivity_below_005_deep_half: 0.22
1446	    en_selectivity_deep_layers: 0.25
1447	    zh_selectivity_deep_avg: 0.18
1448	    es_selectivity_deep_avg: 0.17
1449	    hi_selectivity_deep_avg: 0.1
1450	    ko_selectivity_deep_avg: 0.09
1451	    sw_selectivity_deep_avg: 0.03
1452	    bn_selectivity_deep_avg: 0.02
1453	    te_selectivity_deep_avg: 0.02
1454	    capacity_artifact_lang_layer_pairs: ~180/912 total (38%)
1455	    low_resource_artifact_rate: 72% of low-resource lang-layer combinations
1456	  result_rationale: 'Control task 分析是 worst tier 的核心贡献之一。在大模型 MoE 上，shallow layers
1457	    的  selectivity 普遍低于 0.05——probe 在 permuted labels 上也能达到接近 real labels 的 AUROC，
1458	    说明信号来自 memorization/capacity 而非 genuine correctness direction。 低资源语言几乎全部受影响（72%
1459	    artifact rate），原因： (1) GlobalMMLU 低资源翻译质量差→test items 有系统性 pattern（如翻译 artifacts）
1460	    可被 probe 利用但与 correctness 无关； (2) 低资源 representation 本身 less structured，probe
1461	    在 real/permuted labels 上 表现差异小； (3) MoE expert routing 在低资源上更 random（缺乏 consistent
1462	    routing pattern）， probe 拟合的是 routing noise 而非 semantic content。 38% overall artifact
1463	    rate 大幅超过英语的 plan_013 baseline（浅层 0.02-0.04）， 说明英语 selectivity 分析严重低估了多语言场景的 capacity
1464	    artifact 问题。 这是对 Hewitt & Liang (2019) 框架在多语言场景下的重要扩展—— 原论文仅考虑英语单任务，未预见到跨语言 probing
1465	    的 artifact 放大效应。
1466	
1467	    '
1468	  tables:
1469	  - title: 'Table 18: Selectivity by Resource Tier and Depth (Qwen3-235B)'
1470	    columns:
1471	    - Tier
1472	    - Shallow_sel
1473	    - Mid_sel
1474	    - Deep_sel
1475	    - Artifact rate (<0.05)
1476	    rows:
1477	    - - EN (source)
1478	      - 0.03
1479	      - 0.12
1480	      - 0.25
1481	      - 25%
1482	    - - HIGH (4 langs)
1483	      - 0.03
1484	      - 0.09
1485	      - 0.18
1486	      - 32%
1487	    - - MID (12 langs)
1488	      - 0.02
1489	      - 0.06
1490	      - 0.1
1491	      - 48%
1492	    - - LOW (3 langs)
1493	      - 0.01
1494	      - 0.03
1495	      - 0.03
1496	      - 72%
1497	  - title: 'Table 19: Capacity Artifact Language Breakdown (deep layers only, selectivity
1498	      < 0.05)'
1499	    columns:
1500	    - Language
1501	    - Tier
1502	    - Sel_best_layer
1503	    - Is_artifact
1504	    - Real_AUROC
1505	    - Ctrl_AUROC
1506	    rows:
1507	    - - en
1508	      - source
1509	      - 0.25
1510	      - ✗
1511	      - 0.76
1512	      - 0.51
1513	    - - zh
1514	      - HIGH
1515	      - 0.18
1516	      - ✗
1517	      - 0.672
1518	      - 0.492
1519	    - - es
1520	      - HIGH
1521	      - 0.17
1522	      - ✗
1523	      - 0.668
1524	      - 0.498
1525	    - - fr
1526	      - HIGH
1527	      - 0.15
1528	      - ✗
1529	      - 0.662
1530	      - 0.512
1531	    - - de
1532	      - HIGH
1533	      - 0.14
1534	      - ✗
1535	      - 0.653
1536	      - 0.513
1537	    - - ko
1538	      - MID
1539	      - 0.09
1540	      - ✗
1541	      - 0.602
1542	      - 0.512
1543	    - - hi
1544	      - MID
1545	      - 0.1
1546	      - ✗
1547	      - 0.588
1548	      - 0.488
1549	    - - ru
1550	      - MID
1551	      - 0.08
1552	      - ✗
1553	      - 0.608
1554	      - 0.528
1555	    - - tr
1556	      - MID
1557	      - 0.06
1558	      - '~'
1559	      - 0.571
1560	      - 0.511
1561	    - - ar
1562	      - MID
1563	      - 0.05
1564	      - '~'
1565	      - 0.555
1566	      - 0.505
1567	    - - sw
1568	      - LOW
1569	      - 0.03
1570	      - ✓
1571	      - 0.508
1572	      - 0.478
1573	    - - bn
1574	      - LOW
1575	      - 0.02
1576	      - ✓
1577	      - 0.538
1578	      - 0.518
1579	    - - te
1580	      - LOW
1581	      - 0.02
1582	      - ✓
1583	      - 0.521
1584	      - 0.501
1585	  figures_description:
1586	  - 'Fig 19: Selectivity heatmap (20 langs × 24 layers, Qwen3)——clear gradient: 右下角（deep+high
1587	    resource）高 selectivity，左上角和右上低资源区域全部低 selectivity。这是论文核心 figure 之一。'
1588	  - 'Fig 20: Selectivity vs ZS AUROC scatter——低 selectivity 区域的 ZS AUROC ''success''
1589	    可能全是 artifact，red zone 标记。'
1590	  analysis: '这是 worst tier 最重要的发现：38% 的 lang-layer 组合 selectivity<0.05，意味着 probe AUROC
1591	    "success" 中近四成可能是 false positive。低资源语言的 72% artifact rate 意味着 sw/bn/te 的所有 probing
1592	    结果都不可信——它们的 "transfer success" 和 "AUROC>0.50" 可能完全来自 capacity artifact。这从根本上改变了
1593	    Claim 1 的解读： Pareto frontier 分析中使用的 ZS AUROC 值在低资源端是 corrupted 的， frontier 上的低资源数据点需要标注为
1594	    "artifact-suspect"。 对论文叙事：这是 Hewitt & Liang 框架的多语言扩展，本身就是 paper-worthy 的发现， 也为
1595	    "viability boundary" 提供了最强的 evidence——probing-based calibration  在低资源语言上不 viable，不是因为
1596	    transfer 失败，而是因为 probe 本身不可信。
1597	
1598	    '
1599	- name: Gemma 4 31B Dense Full Pareto (P2 Camera-Ready)
1600	  plan_id: plan_008
1601	  description: '第三个架构（dense, 60 layers, FP16），提供 dense vs MoE architectural contrast。
1602	
1603	    '
1604	  expected_results:
1605	    en_best_auroc: 0.78
1606	    en_best_layer: L48 (80% depth)
1607	    zs_transfer_auroc_avg_20lang: 0.61
1608	    pareto_global_spearman_rho: -0.48
1609	    pareto_global_spearman_p: 0.002
1610	    pareto_per_lang_significant_count: 9/19
1611	    selectivity_below_005_fraction: 0.22
1612	    linear_proj_50pairs_delta_avg: 0.028
1613	  result_rationale: 'Dense 架构是 Pareto frontier 分析的最佳场景——没有 MoE routing 碎片化， 所有语言共享同一
1614	    expert（整个 FFN），representation 连续性更强。 预期 Gemma 31B Dense 的 global rho 回到 MVP 阶段
1615	    Qwen-7B 的水平（-0.48, p=0.002）， 约一半语言显著。Selectivity 也更好（22% artifact rate vs MoE
1616	    的 38%）。 EN AUROC 可能是三个模型中最高的（0.78），因为 dense 中 correctness signal 更集中。 但这是 camera-ready
1617	    P2 extension——如果 worst tier 的核心叙事已经 established （MoE Pareto noisy, control task
1618	    artifact），dense 结果成为对比证据： "dense architecture recovers Pareto tradeoff; MoE disrupts
1619	    it"—— 这实际上加强了 architecture-dependent viability boundary 的 claim。
1620	
1621	    '
1622	  tables:
1623	  - title: 'Table 20: Architecture Comparison Summary'
1624	    columns:
1625	    - Model
1626	    - Type
1627	    - Global_rho
1628	    - p
1629	    - Sig langs
1630	    - Artifact%
1631	    rows:
1632	    - - Qwen3-235B
1633	      - MoE
1634	      - -0.18
1635	      - 0.12
1636	      - 3/19
1637	      - 38%
1638	    - - Llama4 Scout
1639	      - MoE
1640	      - -0.05
1641	      - 0.62
1642	      - 1/19
1643	      - 41%
1644	    - - Gemma4 31B
1645	      - Dense
1646	      - -0.48
1647	      - 0.002
1648	      - 9/19
1649	      - 22%
1650	  figures_description:
1651	  - 'Fig 21: 3-architecture Pareto rho comparison——dense 明显强于两个 MoE，支持 architecture-dependent
1652	    narrative。'
1653	  analysis: 'Gemma 结果是 worst tier 叙事的关键对照——证明 Pareto frontier 在 dense 架构上仍然有效， MoE
1654	    的 failure 是 architecture-specific 的。这把 worst tier 从 "method completely fails"
1655	    转为 "method works under specific architectural conditions"——更有 nuance 的 viability
1656	    boundary。
1657	
1658	    '
1659	- name: Extended Language Coverage (50+ languages, P2 Camera-Ready)
1660	  plan_id: plan_009
1661	  description: '从 20 扩展到 50+ 语言，利用 GlobalMMLU/Belebele 的完整语言集。
1662	
1663	    '
1664	  expected_results:
1665	    total_languages_tested: 52
1666	    zs_transfer_success_rate_060: 22/51 (43%)
1667	    artifact_rate_overall: 0.42
1668	    artifact_rate_new_low_resource: 0.85
1669	    viability_boundary_clear: 'AUROC>0.60 AND selectivity>0.05: only 18/51 languages'
1670	    new_language_families_covered: 6
1671	  result_rationale: '扩展到 50+ 语言主要增加低资源语言（GlobalMMLU 覆盖的尾部语言）， 这些语言的 representation
1672	    quality 更差，artifact rate 更高（85%+）， 进一步支持 viability boundary 叙事。真正 viable 的语言仅
1673	    18/51（35%）， 全部是高/中资源。这个数字本身就是论文的核心 finding： probe-based calibration 仅对约 1/3 的测试语言可行。
1674	
1675	    '
1676	  tables:
1677	  - title: 'Table 21: Viability Classification (52 languages)'
1678	    columns:
1679	    - Category
1680	    - Count
1681	    - Criterion
1682	    - Example_langs
1683	    rows:
1684	    - - Viable
1685	      - 18
1686	      - AUROC>0.60 + sel>0.05
1687	      - en, zh, es, fr, de, ja, pt, ru, ko, nl...
1688	    - - Marginal
1689	      - 12
1690	      - AUROC>0.55 + sel 0.03-0.05
1691	      - hi, tr, pl, id, uk, ar...
1692	    - - Non-viable
1693	      - 22
1694	      - AUROC<0.55 OR sel<0.03
1695	      - sw, bn, te, am, yo, ha, ig...
1696	  figures_description:
1697	  - 'Fig 22: World map with viability color coding——欧洲/东亚 viable，撒哈拉以南非洲/南亚大部 non-viable。'
1698	  analysis: 52 语言版本强化了 viability boundary 叙事的 impact——从 "20 语言上的发现"  扩展为 "across majority
1699	    of world's languages, probe-based calibration is not viable"。 18/51 viable rate
1700	    是 headline-worthy 的。但注意这可能 overstate the problem： 低资源语言的 non-viability 部分来自 GlobalMMLU
1701	    翻译质量差， 而非 representation 本身的缺陷——需要在 discussion 中 acknowledge。
1702	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "19a2f8c3-e0a4-4915-9be6-5f30e98b2602",
  "isSidechain": false,
  "promptId": "221e9c50-d73e-4401-b409-8fd8dd5897a7",
  "type": "user",
  "uuid": "7c568fc3-93e0-4ca9-9c63-0c2b245c799a",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/worst/review_context.yaml",
      "content": "narrative_guidance: '核心 reframe：从 ''cross-lingual calibration method'' 转为 ''cross-lingual\n  probing viability boundary + methodological warning''。 Headline: ''Stress-testing\n  probe-based calibration beyond English: viability boundaries, capacity artifacts,\n  and when cross-lingual transfer breaks down.'' 大模型（235B MoE / Scout MoE）的 correctness\n  signal 比 7B dense 更分散——MoE routing 将信息分散到更多 expert，导致 probe AUROC 提升有限且 noisy。 Pareto\n  frontier 在两个 MoE 架构上均 noisy（rho 接近零），无法支撑 clean architecture contrast。 CaCLR 失败且\n  linear projection 在低/中资源语言不稳定。CKA partial correlation 控制 depth 后 n.s.。 Control task\n  揭示 >30% 的 lang-layer 组合是 capacity artifacts，低资源语言几乎全部受影响。 贡献重构为：(1) viability boundary\n  刻画；(2) capacity artifact 问题揭露（Hewitt & Liang 多语言扩展）；(3) 方法论框架。 目标 venue 不降级（EACL）——需增加\n  discussion 篇幅，补充 few-shot escalation 实验作为 constructive path forward。\n\n  '\nimagined_experiments:\n- name: Qwen3-235B-A22B Full Pareto Frontier (20 langs × 24 layers × 5 transfer conditions)\n  plan_id: plan_001\n  description: '在 Qwen3-235B-A22B（94 层 MoE, INT4）上提取每隔 4 层的激活（24 个 probed layers），\n    20 种语言训练英语 correctness probes（LR + MLP），评估 5 种 transfer 条件。 报告 per-language Spearman\n    rho（depth vs transfer AUROC）和 global rho。\n\n    '\n  expected_results:\n    en_best_auroc: 0.76\n    en_best_layer: L72 (约 77% depth)\n    en_auroc_range:\n    - 0.58\n    - 0.76\n    en_best_ece_raw: 0.175\n    zs_transfer_auroc_avg_20lang: 0.59\n    zs_transfer_auroc_high_resource_avg: 0.65\n    zs_transfer_auroc_mid_resource_avg: 0.59\n    zs_transfer_auroc_low_resource_avg: 0.53\n    zs_transfer_success_rate_above_060: 11/20 (55%)\n    pareto_global_spearman_rho: -0.18\n    pareto_global_spearman_p: 0.12\n    pareto_per_lang_rho_median: -0.14\n    pareto_per_lang_significant_count: 3/19 (zh, es, fr — 仅高资源)\n    pareto_per_lang_positive_rho_count: 6/19 (ar, ko, bn, sw, te, vi — 方向反转)\n    mean_shift_delta_auroc_avg: 0.0\n    linear_proj_50pairs_delta_auroc_avg: 0.015\n    linear_proj_50pairs_delta_auroc_high: 0.025\n    linear_proj_50pairs_delta_auroc_low: -0.005\n    fewshot_25_delta_auroc_avg: 0.035\n    fewshot_100_delta_auroc_avg: 0.065\n    linear_proj_std_across_seeds_low_resource: 0.028\n    zs_auroc_std_across_layers_top10: 0.04\n  result_rationale: '235B MoE 架构有 94 层但仅 22B 激活参数——expert routing 机制将 correctness\n    信息分散到不同 expert 子网络中， probe 在 shared representation 上只能捕获部分信号，因此 AUROC 相比 7B dense（0.754）提升极有限（→0.76）。\n    MoE 的 expert 选择是 input-dependent 的，不同语言激活不同 expert 子集，导致跨语言激活空间异质性更高。 这直接破坏了 Pareto\n    frontier 的一致性：不同语言的 \"最优 transfer 层\" 受 expert routing pattern 影响而高度分散， global rho\n    被拉向零。高资源语言（zh/es/fr）与英语共享更多 expert 激活模式，仍显示弱 Pareto； 低资源语言与英语 expert overlap 极低，transfer\n    AUROC 在深层反而因 expert divergence 而改善（正 rho）。 Linear projection 在低资源上不稳定，因为 50 parallel\n    pairs 不足以学习 MoE 碎片化空间的旋转矩阵。\n\n    '\n  tables:\n  - title: 'Table 1: Qwen3-235B Zero-Shot Transfer AUROC by Language (EN-optimal layer\n      L72)'\n    columns:\n    - Language\n    - Family\n    - Resource_Tier\n    - ZS_AUROC\n    - 95% CI\n    - vs EN Δ\n    rows:\n    - - en\n      - Germanic\n      - source\n      - 0.76\n      - '[0.74, 0.78]'\n      - —\n    - - zh\n      - Sinitic\n      - HIGH\n      - 0.672\n      - '[0.65, 0.69]'\n      - -0.088\n    - - es\n      - Romance\n      - HIGH\n      - 0.668\n      - '[0.64, 0.69]'\n      - -0.092\n    - - fr\n      - Romance\n      - HIGH\n      - 0.662\n      - '[0.64, 0.68]'\n      - -0.098\n    - - de\n      - Germanic\n      - HIGH\n      - 0.653\n      - '[0.63, 0.68]'\n      - -0.107\n    - - ja\n      - Japonic\n      - MID\n      - 0.631\n      - '[0.60, 0.66]'\n      - -0.129\n    - - pt\n      - Romance\n      - MID\n      - 0.624\n      - '[0.60, 0.65]'\n      - -0.136\n    - - ru\n      - Slavic\n      - MID\n      - 0.608\n      - '[0.58, 0.64]'\n      - -0.152\n    - - ko\n      - Koreanic\n      - MID\n      - 0.602\n      - '[0.57, 0.63]'\n      - -0.158\n    - - nl\n      - Germanic\n      - MID\n      - 0.598\n      - '[0.57, 0.63]'\n      - -0.162\n    - - hi\n      - Indo-Aryan\n      - MID\n      - 0.588\n      - '[0.56, 0.62]'\n      - -0.172\n    - - pl\n      - Slavic\n      - MID\n      - 0.582\n      - '[0.55, 0.61]'\n      - -0.178\n    - - id\n      - Austronesian\n      - MID\n      - 0.577\n      - '[0.55, 0.61]'\n      - -0.183\n    - - tr\n      - Turkic\n      - MID\n      - 0.571\n      - '[0.54, 0.60]'\n      - -0.189\n    - - vi\n      - Austroasiatic\n      - MID\n      - 0.563\n      - '[0.53, 0.60]'\n      - -0.197\n    - - uk\n      - Slavic\n      - MID\n      - 0.558\n      - '[0.53, 0.59]'\n      - -0.202\n    - - ar\n      - Semitic\n      - MID\n      - 0.555\n      - '[0.52, 0.59]'\n      - -0.205\n    - - bn\n      - Indo-Aryan\n      - LOW\n      - 0.538\n      - '[0.50, 0.57]'\n      - -0.222\n    - - te\n      - Dravidian\n      - LOW\n      - 0.521\n      - '[0.49, 0.55]'\n      - -0.239\n    - - sw\n      - Niger-Congo\n      - LOW\n      - 0.508\n      - '[0.48, 0.54]'\n      - -0.252\n  - title: 'Table 2: Qwen3-235B Pareto Spearman ρ (depth vs ZS AUROC) per Language'\n    columns:\n    - Language\n    - Spearman_rho\n    - p_value\n    - Direction\n    - Significant\n    rows:\n    - - zh\n      - -0.52\n      - 0.009\n      - expected\n      - ✓\n    - - es\n      - -0.44\n      - 0.031\n      - expected\n      - ✓\n    - - fr\n      - -0.41\n      - 0.046\n      - expected\n      - ✓\n    - - de\n      - -0.33\n      - 0.11\n      - expected\n      - ✗\n    - - ja\n      - -0.25\n      - 0.24\n      - expected\n      - ✗\n    - - ru\n      - -0.18\n      - 0.4\n      - expected\n      - ✗\n    - - ko\n      - -0.06\n      - 0.79\n      - flat\n      - ✗\n    - - hi\n      - -0.03\n      - 0.89\n      - flat\n      - ✗\n    - - tr\n      - 0.02\n      - 0.93\n      - flat\n      - ✗\n    - - id\n      - -0.11\n      - 0.61\n      - expected\n      - ✗\n    - - pt\n      - -0.28\n      - 0.19\n      - expected\n      - ✗\n    - - nl\n      - -0.22\n      - 0.3\n      - expected\n      - ✗\n    - - pl\n      - -0.08\n      - 0.71\n      - flat\n      - ✗\n    - - vi\n      - 0.12\n      - 0.58\n      - reversed\n      - ✗\n    - - uk\n      - -0.15\n      - 0.48\n      - expected\n      - ✗\n    - - ar\n      - 0.09\n      - 0.67\n      - reversed\n      - ✗\n    - - bn\n      - 0.18\n      - 0.4\n      - reversed\n      - ✗\n    - - te\n      - 0.22\n      - 0.3\n      - reversed\n      - ✗\n    - - sw\n      - 0.15\n      - 0.48\n      - reversed\n      - ✗\n    - - global\n      - -0.18\n      - 0.12\n      - —\n      - ✗\n  figures_description:\n  - 'Fig 1: 20-panel Pareto frontier heatmap (x=normalized depth, y=language sorted\n    by resource tier), color=ZS AUROC。高资源区域呈现弱对角梯度（浅层 transfer 好→深层差），中/低资源区域为 noisy\n    棋盘格，无一致趋势。'\n  - 'Fig 2: Per-language Spearman rho bar chart with 95% bootstrap CI。3 条显著阈值线；大部分\n    CI 跨零。'\n  analysis: 'Qwen3-235B 的 Pareto frontier 远弱于 7B dense MVP 预期。Global rho=-0.18 不显著，\n    仅 3/19 target 语言有显著负相关（均为高资源）。6/19 语言出现方向反转（正 rho）， 集中在低资源。MoE routing 的 input-dependent\n    expert selection 使得不同语言在不同深度 激活完全不同的子网络，破坏了 \"更深=更好英语但更差 transfer\" 的简单叙事。 这意味着\n    Pareto frontier 在 MoE 架构上不是稳定的 architecture-level property， 而是 language-specific\n    的。对 worst tier 叙事：这直接支持 \"viability boundary\" reframe—— Pareto analysis 仅在高资源+特定架构上有清晰信号。\n\n    '\n- name: Llama 4 Scout Full Pareto Frontier (20 langs × 12 layers × 5 transfer conditions)\n  plan_id: plan_002\n  description: '在 Llama 4 Scout（48 层 MoE, W4A16）上提取激活（12 probed layers）， 20 种语言，5\n    种 transfer 条件。报告 per-language Spearman rho。\n\n    '\n  expected_results:\n    en_best_auroc: 0.74\n    en_best_layer: L40 (约 83% depth)\n    en_auroc_range:\n    - 0.6\n    - 0.74\n    en_best_ece_raw: 0.185\n    zs_transfer_auroc_avg_20lang: 0.57\n    zs_transfer_auroc_high_resource_avg: 0.63\n    zs_transfer_auroc_mid_resource_avg: 0.57\n    zs_transfer_auroc_low_resource_avg: 0.51\n    zs_transfer_success_rate_above_060: 8/20 (40%)\n    pareto_global_spearman_rho: -0.05\n    pareto_global_spearman_p: 0.62\n    pareto_per_lang_rho_median: -0.02\n    pareto_per_lang_significant_count: 1/19 (仅 zh)\n    pareto_per_lang_positive_rho_count: 8/19\n    mean_shift_delta_auroc_avg: 0.0\n    linear_proj_50pairs_delta_auroc_avg: 0.008\n    linear_proj_50pairs_delta_auroc_low: -0.01\n    fewshot_25_delta_auroc_avg: 0.028\n    fewshot_100_delta_auroc_avg: 0.055\n    linear_proj_std_across_seeds_low_resource: 0.035\n  result_rationale: 'Llama 4 Scout 是 17B-16E MoE（272B total, 17B active），48 层比 Qwen3\n    的 94 层少得多， probed layers 仅 12 个，Spearman rho 的统计检验力极低（n=12 时需要 |rho|>0.58 才显著）。\n    MVP 阶段 Llama-3.1-8B dense 已经是 weak Pareto（仅 2/5 显著），Scout MoE 继承了 Llama 家族 的弱\n    depth-transfer tradeoff 特征（可能因为 Llama 训练数据中多语言比例高于 Qwen， 导致深层 representation 已经部分语言对齐），加上\n    MoE routing 碎片化效应， global rho 被进一步推向零。W4A16 量化可能引入额外 noise（权重 4-bit 但激活 16-bit，\n    correctness probe 依赖的微弱方向性信号可能在权重量化中丢失部分精度）。 12 个 probed layers 的粗糙采样使得 per-language\n    rho 高度不稳定， 微小的 AUROC 波动就能翻转 rho 方向。\n\n    '\n  tables:\n  - title: 'Table 3: Llama 4 Scout Zero-Shot Transfer AUROC (EN-optimal L40)'\n    columns:\n    - Language\n    - Resource_Tier\n    - ZS_AUROC\n    - 95% CI\n    rows:\n    - - en\n      - source\n      - 0.74\n      - '[0.72, 0.76]'\n    - - zh\n      - HIGH\n      - 0.648\n      - '[0.62, 0.67]'\n    - - es\n      - HIGH\n      - 0.643\n      - '[0.62, 0.67]'\n    - - fr\n      - HIGH\n      - 0.635\n      - '[0.61, 0.66]'\n    - - de\n      - HIGH\n      - 0.628\n      - '[0.60, 0.65]'\n    - - ja\n      - MID\n      - 0.601\n      - '[0.57, 0.63]'\n    - - ru\n      - MID\n      - 0.588\n      - '[0.56, 0.62]'\n    - - ko\n      - MID\n      - 0.583\n      - '[0.55, 0.61]'\n    - - pt\n      - MID\n      - 0.595\n      - '[0.57, 0.62]'\n    - - hi\n      - MID\n      - 0.568\n      - '[0.54, 0.60]'\n    - - nl\n      - MID\n      - 0.575\n      - '[0.54, 0.61]'\n    - - pl\n      - MID\n      - 0.562\n      - '[0.53, 0.59]'\n    - - id\n      - MID\n      - 0.555\n      - '[0.52, 0.59]'\n    - - tr\n      - MID\n      - 0.548\n      - '[0.52, 0.58]'\n    - - vi\n      - MID\n      - 0.541\n      - '[0.51, 0.57]'\n    - - uk\n      - MID\n      - 0.545\n      - '[0.51, 0.58]'\n    - - ar\n      - MID\n      - 0.538\n      - '[0.51, 0.57]'\n    - - bn\n      - LOW\n      - 0.518\n      - '[0.49, 0.55]'\n    - - te\n      - LOW\n      - 0.505\n      - '[0.47, 0.54]'\n    - - sw\n      - LOW\n      - 0.495\n      - '[0.46, 0.53]'\n  - title: 'Table 4: Llama 4 Scout Pareto ρ per Language'\n    columns:\n    - Language\n    - Spearman_rho\n    - p_value\n    - Significant\n    rows:\n    - - zh\n      - -0.62\n      - 0.031\n      - ✓\n    - - es\n      - -0.38\n      - 0.22\n      - ✗\n    - - fr\n      - -0.29\n      - 0.36\n      - ✗\n    - - de\n      - -0.15\n      - 0.64\n      - ✗\n    - - ja\n      - -0.08\n      - 0.8\n      - ✗\n    - - ru\n      - 0.05\n      - 0.88\n      - ✗\n    - - ko\n      - 0.22\n      - 0.49\n      - ✗\n    - - hi\n      - 0.11\n      - 0.73\n      - ✗\n    - - tr\n      - 0.08\n      - 0.8\n      - ✗\n    - - id\n      - -0.03\n      - 0.93\n      - ✗\n    - - pt\n      - -0.18\n      - 0.58\n      - ✗\n    - - nl\n      - -0.12\n      - 0.71\n      - ✗\n    - - pl\n      - 0.15\n      - 0.64\n      - ✗\n    - - vi\n      - 0.25\n      - 0.43\n      - ✗\n    - - uk\n      - 0.03\n      - 0.93\n      - ✗\n    - - ar\n      - 0.18\n      - 0.58\n      - ✗\n    - - bn\n      - 0.28\n      - 0.38\n      - ✗\n    - - te\n      - 0.35\n      - 0.26\n      - ✗\n    - - sw\n      - 0.31\n      - 0.33\n      - ✗\n    - - global\n      - -0.05\n      - 0.62\n      - ✗\n  figures_description:\n  - 'Fig 3: Llama 4 Scout Pareto heatmap——几乎全为 noise，仅 zh 一行可见微弱梯度。'\n  - 'Fig 4: 两架构 global rho 对比 bar chart（Qwen -0.18 vs Scout -0.05），两者 CI 均跨零。'\n  analysis: 'Scout 上 Pareto 完全崩溃——global rho=-0.05 (p=0.62)，仅 zh 显著。n=12 的采样密度 使得统计检验力不足以检测中等效应。与\n    Qwen3 对比：两个 MoE 架构都无法支撑 \"clean architecture contrast\"， 因为 rho 都不显著（Qwen -0.18\n    p=0.12, Scout -0.05 p=0.62）。MVP 阶段观察到的 Qwen(strong)/Llama(weak) 对比在大模型上被 MoE noise\n    冲刷。这强化了 worst tier 叙事：Pareto frontier 作为分析工具 仅在 7B dense + 高资源语言上有效——对 MoE 架构的泛化失败是方法论局限性的核心发现。\n\n    '\n- name: CaCLR Comparative Evaluation (2 models × 20 langs × Pareto frontier)\n  plan_id: plan_003\n  description: 'CaCLR (L_BCE + α·L_SB-ECE + β·L_consistency) 与 zero-shot/mean-shift/linear\n    projection/few-shot 在两个模型全 Pareto frontier 上的对比。α sweep (0.01-10.0), β sweep 3\n    OOM (0.001-1.0)。\n\n    '\n  expected_results:\n    caclr_best_beta_auroc_delta_vs_zeroshot_avg: 0.002\n    caclr_best_beta_auroc_delta_high_resource: 0.005\n    caclr_best_beta_auroc_delta_low_resource: -0.008\n    caclr_best_beta_auroc_delta_range:\n    - -0.01\n    - 0.005\n    beta_0001_delta_auroc: 0.001\n    beta_001_delta_auroc: 0.002\n    beta_01_delta_auroc: 0.001\n    beta_1_delta_auroc: -0.003\n    beta_sweep_variance_across_seeds: 0.006\n    caclr_delta_ece_vs_tempscaling_avg: 0.008\n    caclr_delta_ece_vs_tempscaling_range:\n    - -0.005\n    - 0.02\n    bce_only_auroc_delta: 0.0\n    bce_sbece_auroc_delta: 0.001\n    bce_mmd_auroc_delta: 0.002\n    bce_sbece_mmd_auroc_delta: 0.002\n    linear_proj_50pairs_delta_auroc_avg: 0.015\n    linear_proj_50pairs_wins_over_caclr: 14/19 languages\n    fewshot_25_delta_auroc_avg: 0.032\n    fewshot_100_delta_auroc_avg: 0.061\n    alpha_optimal: 0.1\n    alpha_sensitivity: robust in [0.01, 1.0], degrades at α=10\n  result_rationale: 'CaCLR 的 MMD consistency loss 在 1-D probe logit 空间上操作——这是根本性的设计缺陷。\n    MMD 匹配的是 probe output 的边缘分布，但跨语言 correctness 失败的原因不是边缘分布不匹配， 而是条件分布 P(correct|representation)\n    在不同语言上不同（Zhao et al. 2019 的核心结论）。 在 MoE 架构上，不同语言激活不同 expert 子集，representation\n    space 的拓扑结构完全不同—— MMD 在低维投影空间上的匹配无法 capture 这种高维结构差异。 β sweep 跨 3 OOM 但 delta\n    AUROC 始终在 noise level（±0.005），因为 MMD loss 的梯度信号太弱（1-D logit，bandwidth 由 median\n    heuristic 决定，在接近正态的分布上 几乎所有 bandwidth 都给出相似的 gradient）。低资源语言上 CaCLR 甚至略微 hurt（-0.008），\n    因为 MMD penalty 迫使 probe 偏离英语最优解但又无法真正对齐目标语言。 Linear projection（50 pairs）在 14/19\n    语言上赢过 CaCLR，因为它直接学习子空间旋转 而不是间接匹配分布。但 linear projection 本身在低资源上不稳定（seed variance\n    高）。\n\n    '\n  tables:\n  - title: 'Table 5: Transfer Method Comparison — Δ AUROC vs Zero-Shot (Qwen3-235B,\n      EN-optimal layer)'\n    columns:\n    - Method\n    - HIGH_avg\n    - MID_avg\n    - LOW_avg\n    - ALL_avg\n    - Wins/19\n    rows:\n    - - Mean-shift\n      - 0.0\n      - 0.0\n      - 0.0\n      - 0.0\n      - 0/19\n    - - CaCLR (best β)\n      - 0.005\n      - 0.003\n      - -0.008\n      - 0.002\n      - 8/19\n    - - Linear proj (50)\n      - 0.025\n      - 0.015\n      - -0.005\n      - 0.015\n      - 14/19\n    - - Few-shot (25)\n      - 0.038\n      - 0.03\n      - 0.022\n      - 0.032\n      - 17/19\n    - - Few-shot (100)\n      - 0.072\n      - 0.058\n      - 0.045\n      - 0.061\n      - 19/19\n  - title: 'Table 6: CaCLR β Sweep (avg Δ AUROC across 20 langs, Qwen3-235B)'\n    columns:\n    - β\n    - Δ_AUROC_mean\n    - Δ_AUROC_std\n    - Δ_ECE_mean\n    - p (vs ZS)\n    rows:\n    - - 0.001\n      - 0.001\n      - 0.006\n      - 0.003\n      - 0.72\n    - - 0.01\n      - 0.002\n      - 0.007\n      - 0.005\n      - 0.58\n    - - 0.1\n      - 0.001\n      - 0.008\n      - 0.008\n      - 0.63\n    - - 1.0\n      - -0.003\n      - 0.011\n      - 0.012\n      - 0.41\n    - - 0 (BCE only)\n      - 0.0\n      - 0.005\n      - 0.001\n      - —\n  - title: 'Table 7: CaCLR Component Ablation (Qwen3-235B, avg 20 langs)'\n    columns:\n    - Components\n    - Δ_AUROC\n    - Δ_ECE\n    - Note\n    rows:\n    - - BCE only\n      - 0.0\n      - 0.001\n      - baseline (= zero-shot retrain)\n    - - BCE + SB-ECE\n      - 0.001\n      - -0.002\n      - α=0.1; ECE marginally better\n    - - BCE + MMD\n      - 0.002\n      - 0.004\n      - β=0.01; MMD alone slightly helps AUROC but hurts ECE\n    - - BCE + SB-ECE + MMD\n      - 0.002\n      - 0.006\n      - joint ≈ max of components, no synergy\n  figures_description:\n  - 'Fig 5: β sweep curve (x=log β, y=Δ AUROC) with 95% CI——flat line 在零附近，所有 CI 跨零。'\n  - 'Fig 6: 5-method transfer comparison grouped bar chart (high/mid/low resource)——CaCLR\n    与 zero-shot 不可区分，linear projection 和 few-shot 逐步改善。'\n  - 'Fig 7: Per-language CaCLR Δ AUROC scatter (x=resource tier proxy, y=delta)——低资源侧系统性偏负。'\n  analysis: 'CaCLR 的 consistency loss 完全 inert。β sweep 跨 3 个数量级（0.001→1.0）， 平均 Δ AUROC\n    从未超过 noise level（+0.002 ± 0.007）。配对置换检验 p 值全部 >0.4。 Component ablation 确认：SB-ECE\n    提供微弱 ECE 改善（-0.002），MMD 提供微弱 AUROC 改善（+0.002）， 但两者无协同效应，且均在 noise 范围内。核心 negative\n    result：MMD-based distributional matching 对 correctness probe transfer 无效——与 Zhao\n    et al. (2019) 理论预测一致（边缘匹配在条件分布不同时失效）。 Linear projection（50 pairs）作为最强 zero-label\n    替代方案，但在低资源语言上也不稳定。 Few-shot 25/100 是唯一 consistently 有效的路径——支持 \"constructive path\n    forward\" 叙事。\n\n    '\n- name: Difficulty-Controlled Decomposition Ablation (10 langs × 8 layers × 2 models)\n  plan_id: plan_004\n  description: '训练 IRT difficulty probes，投影出 difficulty direction，在 residuals 上重训\n    correctness probes， 评估 transfer。10 种代表性语言 × 8 层 × 2 模型。含 random-direction control。\n\n    '\n  expected_results:\n    difficulty_probe_r2_en_avg: 0.35\n    difficulty_probe_r2_range:\n    - 0.18\n    - 0.48\n    en_auroc_after_projection_avg_delta: -0.025\n    difficulty_projection_transfer_delta_high_resource: 0.012\n    difficulty_projection_transfer_delta_mid_resource: 0.003\n    difficulty_projection_transfer_delta_low_resource: -0.008\n    difficulty_projection_transfer_delta_avg: 0.005\n    difficulty_projection_transfer_delta_range:\n    - -0.01\n    - 0.015\n    random_projection_transfer_delta_avg: -0.015\n    random_vs_difficulty_significant: 4/10 languages (all high-resource)\n    difficulty_shared_fraction_estimate: 0.20-0.55 range across langs, no consistent\n      pattern\n    capability_specific_fraction_variance: high (std=0.18 across languages)\n  result_rationale: 'Decomposition 在 worst tier 下被 noise dominate，原因有三： (1) IRT difficulty\n    scores 本身 noisy（GlobalMMLU 的 difficulty 基于 human performance， 与 LLM-perceived\n    difficulty 仅中等相关，r²~0.35）； (2) MoE 架构中 difficulty direction 不是一条 clean linear\n    direction——不同 expert  以不同方式 encode difficulty，Ridge regression 只能捕获 average effect；\n    (3) 投影出 difficulty 后的 residual space 维度仍然很高（4096-D），correctness probe  在 residuals\n    上重训的 noise floor 与原始空间接近。 结果：projecting out difficulty 对 transfer 的平均效果极小（+0.005），\n    且高度 language-dependent。高资源语言略有改善（+0.012，因为 difficulty 确实是 shared component）， 低资源语言反而变差（-0.008，因为\n    difficulty probe 本身在低资源上就不准确， 投影出的实际上是 noise direction）。Random-direction control\n    确认投影本身 会降低信号（-0.015），difficulty projection 只是 \"比 random 好一点\"， 但差异仅在 4/10 语言上显著——无法支撑\n    \"decomposition is prescriptive\" 的强 claim。\n\n    '\n  tables:\n  - title: 'Table 8: Difficulty Decomposition — Transfer Δ AUROC (vs no-projection\n      baseline)'\n    columns:\n    - Language\n    - Tier\n    - Difficulty_proj_Δ\n    - Random_proj_Δ\n    - Diff-Rand gap\n    - p_value\n    rows:\n    - - zh\n      - HIGH\n      - 0.015\n      - -0.012\n      - 0.027\n      - 0.031\n    - - es\n      - HIGH\n      - 0.013\n      - -0.014\n      - 0.027\n      - 0.028\n    - - fr\n      - HIGH\n      - 0.011\n      - -0.016\n      - 0.027\n      - 0.035\n    - - de\n      - HIGH\n      - 0.008\n      - -0.013\n      - 0.021\n      - 0.062\n    - - hi\n      - MID\n      - 0.005\n      - -0.015\n      - 0.02\n      - 0.088\n    - - ru\n      - MID\n      - 0.003\n      - -0.018\n      - 0.021\n      - 0.075\n    - - ko\n      - MID\n      - 0.002\n      - -0.014\n      - 0.016\n      - 0.145\n    - - tr\n      - MID\n      - 0.001\n      - -0.017\n      - 0.018\n      - 0.118\n    - - sw\n      - LOW\n      - -0.005\n      - -0.019\n      - 0.014\n      - 0.212\n    - - bn\n      - LOW\n      - -0.01\n      - -0.016\n      - 0.006\n      - 0.481\n  figures_description:\n  - 'Fig 8: Decomposition effect scatter (x=resource tier, y=Δ transfer AUROC) with\n    difficulty vs random overlay——两条线接近，difficulty 仅略高。'\n  analysis: 'Decomposition 效果被 noise dominate。平均 +0.005 transfer delta 远小于 few-shot\n    25 的 +0.032。 \"Difficulty-shared vs capability-specific\" 分解的 fraction 估计高度不稳定（std=0.18），\n    无法形成 consistent 叙事。对 worst tier：Claim 2 需要大幅弱化——从 \"prescriptive decomposition\"\n    降为 \"exploratory decomposition suggests difficulty component exists but is not\n    cleanly separable in MoE architectures\"。仍有方法论价值（展示了 how to decompose），但不是 strong\n    empirical finding。\n\n    '\n- name: Cross-Lingual Orthogonality Analysis (20 langs × 2 architectures)\n  plan_id: plan_005\n  description: '提取 verbalized confidence direction，计算与 correctness direction 的 cosine\n    similarity， 20 种语言 × 2 架构。按 resource tier 和 language family 分析。\n\n    '\n  expected_results:\n    cosine_median_all: 0.06\n    cosine_range:\n    - 0.02\n    - 0.18\n    cosine_below_004_fraction: 7/40 (17.5%)\n    cosine_above_010_fraction: 12/40 (30%)\n    cosine_above_015_fraction: 6/40 (15%)\n    cosine_high_resource_mean: 0.04\n    cosine_mid_resource_mean: 0.07\n    cosine_low_resource_mean: 0.13\n    cosine_qwen_mean: 0.07\n    cosine_scout_mean: 0.08\n    worst_lang_cosine: 'sw@Scout: 0.18'\n    worst_cases_above_015:\n    - sw@Scout\n    - bn@Scout\n    - te@Qwen\n    - sw@Qwen\n    - bn@Qwen\n    - te@Scout\n  result_rationale: 'Miao & Ungar (2026) 在英语 7-8B 上报告 cosine<0.04（近乎正交）。 在大模型 MoE\n    + 多语言设置下正交性部分退化，原因： (1) MoE expert 内部空间维度有效降低——当 correctness 和 confidence 信号都被\n    route 到 少量共享 expert 时，方向会更 \"拥挤\"，cosine 从零偏移； (2) 低资源语言的 confidence direction 本身就\n    noisy（模型在低资源上的 verbalized confidence 更随机，probe 拟合的方向不稳定），noise 方向与 correctness\n    的 cosine 期望值 ~1/√d 而非精确零； (3) 部分低资源语言（sw, bn, te）可能存在 capacity artifact——probe\n    学到的不是真正的 correctness/confidence 方向而是 dataset regularities，这两种 artifact 方向可能有非零相关。\n    高资源语言维持 cosine~0.04，但 15% 的 lang×arch 组合 cosine>0.15， \"universally orthogonal\"\n    的表述不再成立。\n\n    '\n  tables:\n  - title: 'Table 9: Correctness-Confidence Cosine Similarity (selected languages\n      × 2 architectures)'\n    columns:\n    - Language\n    - Tier\n    - Qwen3_cosine\n    - Scout_cosine\n    - Avg\n    rows:\n    - - en\n      - source\n      - 0.03\n      - 0.03\n      - 0.03\n    - - zh\n      - HIGH\n      - 0.04\n      - 0.03\n      - 0.035\n    - - es\n      - HIGH\n      - 0.03\n      - 0.04\n      - 0.035\n    - - fr\n      - HIGH\n      - 0.04\n      - 0.05\n      - 0.045\n    - - de\n      - HIGH\n      - 0.04\n      - 0.04\n      - 0.04\n    - - ja\n      - MID\n      - 0.05\n      - 0.06\n      - 0.055\n    - - ru\n      - MID\n      - 0.05\n      - 0.06\n      - 0.055\n    - - ko\n      - MID\n      - 0.06\n      - 0.07\n      - 0.065\n    - - hi\n      - MID\n      - 0.07\n      - 0.08\n      - 0.075\n    - - tr\n      - MID\n      - 0.08\n      - 0.09\n      - 0.085\n    - - ar\n      - MID\n      - 0.06\n      - 0.07\n      - 0.065\n    - - bn\n      - LOW\n      - 0.12\n      - 0.14\n      - 0.13\n    - - te\n      - LOW\n      - 0.15\n      - 0.13\n      - 0.14\n    - - sw\n      - LOW\n      - 0.14\n      - 0.18\n      - 0.16\n  figures_description:\n  - 'Fig 9: Cosine similarity heatmap (lang × arch)——高资源区域冷色（<0.05），低资源区域暖色（>0.10），清晰的\n    resource-tier gradient。'\n  - 'Fig 10: Cosine vs resource tier scatter with regression line——正相关，r=-0.65（resource\n    level 越低 cosine 越高）。'\n  analysis: 'Orthogonality 在高资源语言上 robustly holds（cosine<0.05），但低资源语言系统性偏离， 15% 的\n    lang×arch 组合 cosine>0.15。这意味着 \"correctness-confidence orthogonality is universal\"\n    (Miao & Ungar) 需要 qualify——仅在 resource-adequate languages 上成立。 对 worst tier：这是有价值的发现，但方向从\n    \"positive extension\" 变为 \"qualification + warning\"。 需要讨论 capacity artifact 的混淆：低资源\n    cosine 升高可能不是 \"真正的结构性非正交\"， 而是 probe quality 太差导致方向估计 noisy。与 plan_013 control\n    task 结果联合解读。\n\n    '\n- name: 'Probe Complexity: Logistic Regression vs 2-Layer MLP (2 models × all layers)'\n  plan_id: plan_006\n  description: '比较 LR 和 2-layer MLP 在两个模型每层上的英语 AUROC、cross-lingual transfer degradation\n    和 calibration 质量。\n\n    '\n  expected_results:\n    mlp_en_auroc_advantage_avg: 0.025\n    mlp_en_auroc_advantage_range:\n    - 0.01\n    - 0.04\n    lr_zs_transfer_degradation_avg: 0.155\n    mlp_zs_transfer_degradation_avg: 0.195\n    mlp_zs_degradation_excess: 0.04\n    mlp_excess_degradation_high: 0.02\n    mlp_excess_degradation_mid: 0.04\n    mlp_excess_degradation_low: 0.065\n    lr_ece_avg: 0.18\n    mlp_ece_avg: 0.22\n    lr_transfers_better_significant: 14/19 languages (bootstrap p<0.05)\n  result_rationale: 'Linear probes transfer better cross-lingually 这个假设在 7B dense\n    上 well-supported （更简单的 probe 拟合的 direction 更 language-agnostic），在大模型 MoE 上同样成立但差异更大。\n    MLP 在英语上多学到 ~2.5pp（利用非线性语言特异性模式），但这些模式在 transfer 时成为负担。 MoE 架构放大了这个效应：MLP 可以学习\n    expert-routing-dependent 的非线性模式， 这些模式在不同语言 routing 不同时完全不 transfer。低资源上 MLP excess\n    degradation 最大（6.5pp）， 因为低资源语言的 expert routing 与英语差异最大。 这支持了 \"linear probe is\n    the right methodological choice\" 但也意味着 probe 捕获的信号上限 被 linearity constraint 限制——在\n    MoE 上，correctness signal 可能本质上需要非线性访问。\n\n    '\n  tables:\n  - title: 'Table 10: Probe Complexity — LR vs MLP (Qwen3-235B, EN-optimal layer)'\n    columns:\n    - Metric\n    - LR\n    - MLP\n    - Δ\n    - p_value\n    rows:\n    - - EN AUROC\n      - 0.76\n      - 0.785\n      - 0.025\n      - <0.001\n    - - ZS AUROC avg (20 lang)\n      - 0.59\n      - 0.575\n      - -0.015\n      - 0.042\n    - - Transfer degradation avg\n      - 0.155\n      - 0.195\n      - 0.04\n      - 0.008\n    - - ECE avg (20 lang)\n      - 0.18\n      - 0.22\n      - 0.04\n      - 0.015\n  figures_description:\n  - 'Fig 11: LR vs MLP transfer degradation scatter (x=LR degradation, y=MLP degradation)\n    per language——所有点在 y=x 线上方，MLP 一致更差。'\n  analysis: '确认 linear probe 是跨语言 transfer 的正确选择。MLP 的英语优势（+2.5pp）在 transfer 中 被完全\n    offset 且反转。方法论含义：correctness signal 的 linearly accessible component 是唯一 cross-lingually\n    stable 的部分。这与 \"low-dimensional language-agnostic subspace\" 叙事一致。\n\n    '\n- name: Belebele + MMLU-ProX Generalization (20 langs × best probes + CaCLR)\n  plan_id: plan_007\n  description: '在 Belebele（阅读理解）和 MMLU-ProX（20 languages）上评估最佳 probes 和 CaCLR， 验证\n    GlobalMMLU 之外的泛化。\n\n    '\n  expected_results:\n    belebele_en_auroc: 0.72\n    belebele_zs_avg_20lang: 0.56\n    belebele_vs_globalmmlu_en_delta: -0.04\n    belebele_vs_globalmmlu_zs_delta: -0.03\n    belebele_caclr_delta_vs_zs: 0.001\n    belebele_rank_correlation_with_globalmmlu: 0.82\n    mmlupx_en_auroc: 0.74\n    mmlupx_zs_avg_20lang: 0.57\n    mmlupx_vs_globalmmlu_en_delta: -0.02\n    mmlupx_vs_globalmmlu_zs_delta: -0.02\n    mmlupx_caclr_delta_vs_zs: 0.002\n    mmlupx_rank_correlation_with_globalmmlu: 0.88\n    language_ranking_kendall_tau: 0.78\n    low_resource_auroc_drop_consistent: true\n  result_rationale: 'Belebele 是阅读理解任务（与 MCQA knowledge 不同），correctness probe 的 transferability  预期更差因为\n    task-specific 信号不同。MMLU-ProX 与 GlobalMMLU 同源但翻译质量可能不同， 期望更高一致性。两个 benchmark 上的绝对性能均低于\n    GlobalMMLU（因为 probe 是在 GlobalMMLU 上训练的）， 但语言排序高度一致（Kendall tau=0.78），说明 cross-lingual\n    transfer degradation pattern 是 task-general 的。CaCLR 在两个 benchmark 上同样 inert（delta~0），进一步确认负面结果\n    不是 benchmark-specific artifact。\n\n    '\n  tables:\n  - title: 'Table 11: Cross-Benchmark Generalization (Qwen3-235B)'\n    columns:\n    - Benchmark\n    - EN_AUROC\n    - ZS_avg\n    - CaCLR_Δ\n    - Rank_corr_w_GlobalMMLU\n    rows:\n    - - GlobalMMLU\n      - 0.76\n      - 0.59\n      - 0.002\n      - —\n    - - Belebele\n      - 0.72\n      - 0.56\n      - 0.001\n      - 0.82\n    - - MMLU-ProX\n      - 0.74\n      - 0.57\n      - 0.002\n      - 0.88\n  figures_description:\n  - 'Fig 12: 三 benchmark 语言排序 parallel coordinates plot——高度一致的降序趋势。'\n  analysis: 'Cross-benchmark generalization 支持 findings 的 robustness：language ranking\n    一致（tau=0.78）， CaCLR 一致 inert，low-resource drop 一致。Belebele 上 AUROC 稍低（阅读理解 vs\n    知识 MCQA）， 但 degradation pattern 相同。这为 \"viability boundary\" 提供了 cross-task evidence。\n\n    '\n- name: Quantization Validation Ablation (W4A16 vs FP16 / INT4 vs FP16)\n  plan_id: plan_010\n  description: '(a) Llama 4 Scout W4A16 vs FP16 at 5 layers on 5% subset; (b) Qwen3-235B\n    GPTQ-Int4 vs FP16 at 5 layers on 5% subset.\n\n    '\n  expected_results:\n    scout_w4a16_vs_fp16_auroc_delta_avg: -0.008\n    scout_w4a16_vs_fp16_auroc_delta_range:\n    - -0.015\n    - 0.002\n    scout_w4a16_vs_fp16_correlation: 0.985\n    scout_w4a16_vs_fp16_rank_agreement: 98%\n    qwen_int4_vs_fp16_auroc_delta_avg: -0.012\n    qwen_int4_vs_fp16_auroc_delta_range:\n    - -0.022\n    - -0.003\n    qwen_int4_vs_fp16_correlation: 0.978\n    qwen_int4_vs_fp16_rank_agreement: 96%\n    deep_layer_quant_delta: -0.018\n    shallow_layer_quant_delta: -0.005\n  result_rationale: '量化（INT4/W4A16）对 correctness probe 的影响在 worst tier 下比 best tier\n    更大， 但仍在可接受范围内。4-bit 权重量化引入的噪声在浅层影响小（-0.005 AUROC）， 在深层影响更大（-0.018），因为深层 representation\n    的 correctness signal 更细微 （signal-to-noise ratio 更低），量化 noise 更容易掩盖信号。 Qwen3-235B\n    的 INT4 (GPTQ) 影响比 Scout W4A16 更大（-0.012 vs -0.008）， 因为 GPTQ 是 post-training quantization\n    而 W4A16 保留了 16-bit 激活。 但 rank agreement >96% 说明量化不改变 per-item correctness 排序——\n    AUROC 降低主要来自 decision boundary 模糊，不是信号方向改变。 结论：量化引入的 AUROC 降低（~1pp）远小于 cross-lingual\n    transfer degradation（~10-15pp）， 不影响核心发现。需要在论文中报告为 limitation。\n\n    '\n  tables:\n  - title: 'Table 12: Quantization Impact on Probe AUROC'\n    columns:\n    - Model\n    - Quant\n    - Layer\n    - FP16_AUROC\n    - Quant_AUROC\n    - Δ\n    rows:\n    - - Scout\n      - W4A16\n      - L8\n      - 0.645\n      - 0.642\n      - -0.003\n    - - Scout\n      - W4A16\n      - L16\n      - 0.668\n      - 0.66\n      - -0.008\n    - - Scout\n      - W4A16\n      - L24\n      - 0.695\n      - 0.685\n      - -0.01\n    - - Scout\n      - W4A16\n      - L32\n      - 0.718\n      - 0.706\n      - -0.012\n    - - Scout\n      - W4A16\n      - L40\n      - 0.74\n      - 0.725\n      - -0.015\n    - - Qwen3\n      - INT4\n      - L16\n      - 0.64\n      - 0.635\n      - -0.005\n    - - Qwen3\n      - INT4\n      - L36\n      - 0.685\n      - 0.675\n      - -0.01\n    - - Qwen3\n      - INT4\n      - L52\n      - 0.72\n      - 0.705\n      - -0.015\n    - - Qwen3\n      - INT4\n      - L72\n      - 0.762\n      - 0.742\n      - -0.02\n    - - Qwen3\n      - INT4\n      - L88\n      - 0.745\n      - 0.723\n      - -0.022\n  figures_description:\n  - 'Fig 13: FP16 vs Quantized AUROC scatter per layer——点紧贴 y=x 线但系统性偏下，深层偏移更大。'\n  analysis: '量化影响存在但可控。深层损失更大是预期的（信号更弱），但 rank agreement >96%  保证了相对 ordering 可信。Worst\n    tier 下这个结果的含义：已经偏低的 EN AUROC（0.76） 中约 1-2pp 来自量化 artifact，真实 FP16 AUROC 可能在 0.77-0.78\n    区间—— 但即使如此也远低于 best tier 预期的 0.82+。在论文中作为 acknowledged limitation 报告。\n\n    '\n- name: CKA Full-Scale Analysis (20 langs × all layers × 2 models)\n  plan_id: plan_011\n  description: '计算 CKA（linear kernel）between English and each target language at every\n    probed layer。 包含 partial correlation controlling depth、same-layer cross-language\n    correlation、 per-language Spearman、subspace angle analysis。\n\n    '\n  expected_results:\n    cka_degradation_pooled_rho_qwen: -0.28\n    cka_degradation_pooled_p_qwen: 0.008\n    cka_degradation_pooled_rho_scout: -0.35\n    cka_degradation_pooled_p_scout: 0.003\n    cka_partial_corr_controlling_depth_qwen: 0.04\n    cka_partial_corr_p_qwen: 0.58\n    cka_partial_corr_controlling_depth_scout: 0.08\n    cka_partial_corr_p_scout: 0.35\n    same_layer_cka_vs_degradation_rho_avg: -0.42\n    same_layer_significant_layers: 3/24 Qwen, 2/12 Scout\n    per_lang_rho_significant_count_qwen: 4/19\n    per_lang_rho_significant_count_scout: 2/19\n    per_lang_rho_reversed_count: 3/19 (ko, vi, te)\n    cka_cliff_depth_qwen: 75-85% depth\n    cka_cliff_depth_scout: 70-80% depth\n    cka_cliff_steepness_qwen: -0.08\n    cka_cliff_steepness_scout: -0.05\n    subspace_angle_range:\n    - 12\n    - 58\n    subspace_angle_high_resource_mean: 18\n    subspace_angle_low_resource_mean: 45\n  result_rationale: 'CKA partial correlation controlling depth 是决定性分析——在 worst tier\n    下完全 n.s. （Qwen r=0.04 p=0.58, Scout r=0.08 p=0.35）。这意味着 pilot 阶段观察到的 CKA-degradation\n    负相关（Llama rho=-0.52 p=0.001）主要被 depth confound 驱动： 深层 CKA 低 + 深层 transfer 差，但这不是因为\n    \"CKA 低导致 transfer 差\"， 而是 \"depth 同时驱动两者\"。控制 depth 后 CKA 的独立解释力归零。 Pooled correlation\n    仍显著（p<0.01），但这是 Simpson''s paradox 的变体—— between-language 差异（高资源 CKA 高 + degradation\n    低 vs 低资源反之） 和 within-language depth 效应混淆。Same-layer 分析（n=19 per layer）部分有效： 在给定层深度，CKA\n    较高的语言确实 transfer 更好（rho=-0.42）， 但仅在少数层（5/36）达到显著——样本量不够或 CKA range 太窄。 结论：CKA\n    从 \"geometric analysis\" 降级为 \"suggestive correlational observation\"。\n\n    '\n  tables:\n  - title: 'Table 13: CKA Partial Correlation Controlling Depth (THE critical test)'\n    columns:\n    - Model\n    - Partial_r\n    - p_value\n    - Pooled rho (no control)\n    - Pooled p\n    - Interpretation\n    rows:\n    - - Qwen3-235B\n      - 0.04\n      - 0.58\n      - -0.28\n      - 0.008\n      - depth confound explains all\n    - - Llama 4 Scout\n      - 0.08\n      - 0.35\n      - -0.35\n      - 0.003\n      - depth confound explains all\n  - title: 'Table 14: Same-Layer CKA vs Degradation (Qwen3-235B, representative layers)'\n    columns:\n    - Layer\n    - n (langs)\n    - rho\n    - p_value\n    - Significant\n    rows:\n    - - L16\n      - 19\n      - -0.35\n      - 0.14\n      - ✗\n    - - L32\n      - 19\n      - -0.48\n      - 0.037\n      - ✓\n    - - L48\n      - 19\n      - -0.52\n      - 0.022\n      - ✓\n    - - L64\n      - 19\n      - -0.41\n      - 0.081\n      - ✗\n    - - L72\n      - 19\n      - -0.45\n      - 0.053\n      - ✗\n    - - L80\n      - 19\n      - -0.38\n      - 0.11\n      - ✗\n    - - L88\n      - 19\n      - -0.28\n      - 0.24\n      - ✗\n  - title: 'Table 15: Subspace Angle (degrees) between EN and Target Correctness Direction'\n    columns:\n    - Language\n    - Tier\n    - L48_angle\n    - L72_angle\n    - L88_angle\n    rows:\n    - - zh\n      - HIGH\n      - 15\n      - 22\n      - 35\n    - - es\n      - HIGH\n      - 14\n      - 20\n      - 32\n    - - de\n      - HIGH\n      - 18\n      - 25\n      - 38\n    - - ko\n      - MID\n      - 25\n      - 35\n      - 48\n    - - hi\n      - MID\n      - 28\n      - 38\n      - 52\n    - - sw\n      - LOW\n      - 38\n      - 48\n      - 58\n    - - bn\n      - LOW\n      - 35\n      - 45\n      - 55\n    - - te\n      - LOW\n      - 40\n      - 50\n      - 58\n  figures_description:\n  - 'Fig 14: CKA × layer heatmap (20 langs × 24 layers, Qwen3)——clear depth gradient\n    从黄(high CKA)到蓝(low CKA)，但 between-language variance 有限。'\n  - 'Fig 15: Partial correlation forest plot——CI 宽且跨零，与 pooled correlation 的显著结果形成鲜明对比。'\n  - 'Fig 16: Subspace angle vs depth (3 resource tiers)——所有 tier 随深度增加但低资源起点就高，斜率无显著\n    tier 差异。'\n  analysis: 'CKA 分析的核心发现是负面的：partial correlation 控制 depth 后 n.s.。 这在 worst tier 叙事中反而成为贡献——证明了\n    naively 使用 CKA 解释 transfer degradation  是 misleading 的（depth confound），这是对 CKA-based\n    representation analysis 方法论的 warning。 Same-layer 分析保留了 \"languages with higher\n    CKA transfer better\" 的弱 claim（between-language）， 但不足以支撑 \"CKA 作为 transfer 预测器\"\n    的 quantitative tool。 Subspace angle 分析提供了更直接的 geometric evidence：correctness direction\n    的  language specialization 随深度增加，低资源语言的 angle 在浅层就已经很大（35-40°）， 说明 representation\n    从未真正 align。\n\n    '\n- name: Linear Projection Sample Efficiency (10-200 pairs × 20 langs × 2 models)\n  plan_id: plan_012\n  description: '变化 parallel pair 数量 (10, 20, 50, 100, 200)，评估 linear projection transfer，\n    2 模型 × 5 representative layers × 20 语言。\n\n    '\n  expected_results:\n    proj_10pairs_auroc_delta: 0.005\n    proj_20pairs_auroc_delta: 0.01\n    proj_50pairs_auroc_delta: 0.015\n    proj_100pairs_auroc_delta: 0.022\n    proj_200pairs_auroc_delta: 0.028\n    proj_10pairs_std: 0.032\n    proj_20pairs_std: 0.025\n    proj_50pairs_std: 0.02\n    proj_100pairs_std: 0.014\n    proj_200pairs_std: 0.01\n    proj_50_high_resource_delta: 0.025\n    proj_50_mid_resource_delta: 0.015\n    proj_50_low_resource_delta: -0.005\n    proj_50_low_resource_std: 0.028\n    min_pairs_for_positive_avg_delta: 20\n    min_pairs_for_consistent_improvement: 100 (still fails for sw, bn, te)\n    proj_50_wins_over_zeroshot: 14/19 languages\n    proj_50_significantly_better: 7/19 languages (bootstrap p<0.05)\n  result_rationale: 'Linear projection 在 worst tier 下表现不稳定，核心原因是 MoE 架构的高维异质性。 50\n    parallel pairs 学习的 rotation matrix 有效自由度为 min(50, d)=50 远小于 d=4096， 只能 capture\n    低秩近似。在高资源语言上这足够了（correctness subspace 旋转 angle 小， 低秩近似够用），但低资源语言 angle 大（45-58°）且\n    variance 高，50 pairs 不足以 稳定估计旋转矩阵。200 pairs 改善了稳定性但 delta 仍然只有 +0.028 avg—— 说明瓶颈不只是\n    estimation noise，而是 correctness direction 在低资源上可能不存在  clean linear correspondence（capacity\n    artifact 问题，见 plan_013）。 Low resource 上 10-50 pairs 的 delta 可以是负的（-0.005 at 50\n    pairs）， 说明 learned projection 比 identity map（zero-shot）更差——投影 noise 比不投影更有害。\n\n    '\n  tables:\n  - title: 'Table 16: Linear Projection — Δ AUROC by Pair Count (avg across 20 langs,\n      Qwen3-235B)'\n    columns:\n    - N_pairs\n    - Δ_AUROC_avg\n    - std\n    - Wins/19\n    - Sig wins (p<0.05)\n    rows:\n    - - 10\n      - 0.005\n      - 0.032\n      - 10/19\n      - 2/19\n    - - 20\n      - 0.01\n      - 0.025\n      - 12/19\n      - 4/19\n    - - 50\n      - 0.015\n      - 0.02\n      - 14/19\n      - 7/19\n    - - 100\n      - 0.022\n      - 0.014\n      - 16/19\n      - 10/19\n    - - 200\n      - 0.028\n      - 0.01\n      - 17/19\n      - 13/19\n  - title: 'Table 17: Linear Projection 50 Pairs — By Resource Tier'\n    columns:\n    - Tier\n    - Δ_AUROC_avg\n    - std\n    - Sig improvement\n    rows:\n    - - HIGH (4 langs)\n      - 0.025\n      - 0.012\n      - 3/4\n    - - MID (13 langs)\n      - 0.015\n      - 0.018\n      - 4/13\n    - - LOW (3 langs)\n      - -0.005\n      - 0.028\n      - 0/3\n  figures_description:\n  - 'Fig 17: Sample efficiency curve (x=N pairs, y=Δ AUROC) with 3 tier bands——HIGH\n    快速饱和，MID 缓慢爬升，LOW 在零附近或偏负。'\n  - 'Fig 18: Per-language 50-pair Δ AUROC bar chart sorted by magnitude——clear resource-tier\n    gradient。'\n  analysis: 'Linear projection 是 \"surprisingly strong baseline\" 但仅限于高/中资源语言。 在低资源上不稳定（std>0.028）且平均效果为负。200\n    pairs 是 practical minimum for consistency 但 3 种低资源语言 even at 200 pairs 仍未一致改善。这为\n    viability boundary 提供了 另一条 evidence line：linear alignment 需要 source-target correctness\n    subspace 有足够 overlap， 低资源语言不满足这个前提条件。\n\n    '\n- name: Probing Control Tasks — Full 20 Languages × 2 Models\n  plan_id: plan_013\n  description: '在 20 语言 × 2 模型上训练 control probes（permuted labels），计算 selectivity。\n    已完成英语 Qwen-7B baseline（plan_013 registry），现扩展到大模型全语言。\n\n    '\n  expected_results:\n    selectivity_below_005_fraction_overall: 0.38\n    selectivity_below_005_fraction_high_resource: 0.15\n    selectivity_below_005_fraction_mid_resource: 0.35\n    selectivity_below_005_fraction_low_resource: 0.72\n    selectivity_below_005_qwen: 0.35\n    selectivity_below_005_scout: 0.41\n    selectivity_below_005_shallow_half: 0.55\n    selectivity_below_005_deep_half: 0.22\n    en_selectivity_deep_layers: 0.25\n    zh_selectivity_deep_avg: 0.18\n    es_selectivity_deep_avg: 0.17\n    hi_selectivity_deep_avg: 0.1\n    ko_selectivity_deep_avg: 0.09\n    sw_selectivity_deep_avg: 0.03\n    bn_selectivity_deep_avg: 0.02\n    te_selectivity_deep_avg: 0.02\n    capacity_artifact_lang_layer_pairs: ~180/912 total (38%)\n    low_resource_artifact_rate: 72% of low-resource lang-layer combinations\n  result_rationale: 'Control task 分析是 worst tier 的核心贡献之一。在大模型 MoE 上，shallow layers\n    的  selectivity 普遍低于 0.05——probe 在 permuted labels 上也能达到接近 real labels 的 AUROC，\n    说明信号来自 memorization/capacity 而非 genuine correctness direction。 低资源语言几乎全部受影响（72%\n    artifact rate），原因： (1) GlobalMMLU 低资源翻译质量差→test items 有系统性 pattern（如翻译 artifacts）\n    可被 probe 利用但与 correctness 无关； (2) 低资源 representation 本身 less structured，probe\n    在 real/permuted labels 上 表现差异小； (3) MoE expert routing 在低资源上更 random（缺乏 consistent\n    routing pattern）， probe 拟合的是 routing noise 而非 semantic content。 38% overall artifact\n    rate 大幅超过英语的 plan_013 baseline（浅层 0.02-0.04）， 说明英语 selectivity 分析严重低估了多语言场景的 capacity\n    artifact 问题。 这是对 Hewitt & Liang (2019) 框架在多语言场景下的重要扩展—— 原论文仅考虑英语单任务，未预见到跨语言 probing\n    的 artifact 放大效应。\n\n    '\n  tables:\n  - title: 'Table 18: Selectivity by Resource Tier and Depth (Qwen3-235B)'\n    columns:\n    - Tier\n    - Shallow_sel\n    - Mid_sel\n    - Deep_sel\n    - Artifact rate (<0.05)\n    rows:\n    - - EN (source)\n      - 0.03\n      - 0.12\n      - 0.25\n      - 25%\n    - - HIGH (4 langs)\n      - 0.03\n      - 0.09\n      - 0.18\n      - 32%\n    - - MID (12 langs)\n      - 0.02\n      - 0.06\n      - 0.1\n      - 48%\n    - - LOW (3 langs)\n      - 0.01\n      - 0.03\n      - 0.03\n      - 72%\n  - title: 'Table 19: Capacity Artifact Language Breakdown (deep layers only, selectivity\n      < 0.05)'\n    columns:\n    - Language\n    - Tier\n    - Sel_best_layer\n    - Is_artifact\n    - Real_AUROC\n    - Ctrl_AUROC\n    rows:\n    - - en\n      - source\n      - 0.25\n      - ✗\n      - 0.76\n      - 0.51\n    - - zh\n      - HIGH\n      - 0.18\n      - ✗\n      - 0.672\n      - 0.492\n    - - es\n      - HIGH\n      - 0.17\n      - ✗\n      - 0.668\n      - 0.498\n    - - fr\n      - HIGH\n      - 0.15\n      - ✗\n      - 0.662\n      - 0.512\n    - - de\n      - HIGH\n      - 0.14\n      - ✗\n      - 0.653\n      - 0.513\n    - - ko\n      - MID\n      - 0.09\n      - ✗\n      - 0.602\n      - 0.512\n    - - hi\n      - MID\n      - 0.1\n      - ✗\n      - 0.588\n      - 0.488\n    - - ru\n      - MID\n      - 0.08\n      - ✗\n      - 0.608\n      - 0.528\n    - - tr\n      - MID\n      - 0.06\n      - '~'\n      - 0.571\n      - 0.511\n    - - ar\n      - MID\n      - 0.05\n      - '~'\n      - 0.555\n      - 0.505\n    - - sw\n      - LOW\n      - 0.03\n      - ✓\n      - 0.508\n      - 0.478\n    - - bn\n      - LOW\n      - 0.02\n      - ✓\n      - 0.538\n      - 0.518\n    - - te\n      - LOW\n      - 0.02\n      - ✓\n      - 0.521\n      - 0.501\n  figures_description:\n  - 'Fig 19: Selectivity heatmap (20 langs × 24 layers, Qwen3)——clear gradient: 右下角（deep+high\n    resource）高 selectivity，左上角和右上低资源区域全部低 selectivity。这是论文核心 figure 之一。'\n  - 'Fig 20: Selectivity vs ZS AUROC scatter——低 selectivity 区域的 ZS AUROC ''success''\n    可能全是 artifact，red zone 标记。'\n  analysis: '这是 worst tier 最重要的发现：38% 的 lang-layer 组合 selectivity<0.05，意味着 probe AUROC\n    \"success\" 中近四成可能是 false positive。低资源语言的 72% artifact rate 意味着 sw/bn/te 的所有 probing\n    结果都不可信——它们的 \"transfer success\" 和 \"AUROC>0.50\" 可能完全来自 capacity artifact。这从根本上改变了\n    Claim 1 的解读： Pareto frontier 分析中使用的 ZS AUROC 值在低资源端是 corrupted 的， frontier 上的低资源数据点需要标注为\n    \"artifact-suspect\"。 对论文叙事：这是 Hewitt & Liang 框架的多语言扩展，本身就是 paper-worthy 的发现， 也为\n    \"viability boundary\" 提供了最强的 evidence——probing-based calibration  在低资源语言上不 viable，不是因为\n    transfer 失败，而是因为 probe 本身不可信。\n\n    '\n- name: Gemma 4 31B Dense Full Pareto (P2 Camera-Ready)\n  plan_id: plan_008\n  description: '第三个架构（dense, 60 layers, FP16），提供 dense vs MoE architectural contrast。\n\n    '\n  expected_results:\n    en_best_auroc: 0.78\n    en_best_layer: L48 (80% depth)\n    zs_transfer_auroc_avg_20lang: 0.61\n    pareto_global_spearman_rho: -0.48\n    pareto_global_spearman_p: 0.002\n    pareto_per_lang_significant_count: 9/19\n    selectivity_below_005_fraction: 0.22\n    linear_proj_50pairs_delta_avg: 0.028\n  result_rationale: 'Dense 架构是 Pareto frontier 分析的最佳场景——没有 MoE routing 碎片化， 所有语言共享同一\n    expert（整个 FFN），representation 连续性更强。 预期 Gemma 31B Dense 的 global rho 回到 MVP 阶段\n    Qwen-7B 的水平（-0.48, p=0.002）， 约一半语言显著。Selectivity 也更好（22% artifact rate vs MoE\n    的 38%）。 EN AUROC 可能是三个模型中最高的（0.78），因为 dense 中 correctness signal 更集中。 但这是 camera-ready\n    P2 extension——如果 worst tier 的核心叙事已经 established （MoE Pareto noisy, control task\n    artifact），dense 结果成为对比证据： \"dense architecture recovers Pareto tradeoff; MoE disrupts\n    it\"—— 这实际上加强了 architecture-dependent viability boundary 的 claim。\n\n    '\n  tables:\n  - title: 'Table 20: Architecture Comparison Summary'\n    columns:\n    - Model\n    - Type\n    - Global_rho\n    - p\n    - Sig langs\n    - Artifact%\n    rows:\n    - - Qwen3-235B\n      - MoE\n      - -0.18\n      - 0.12\n      - 3/19\n      - 38%\n    - - Llama4 Scout\n      - MoE\n      - -0.05\n      - 0.62\n      - 1/19\n      - 41%\n    - - Gemma4 31B\n      - Dense\n      - -0.48\n      - 0.002\n      - 9/19\n      - 22%\n  figures_description:\n  - 'Fig 21: 3-architecture Pareto rho comparison——dense 明显强于两个 MoE，支持 architecture-dependent\n    narrative。'\n  analysis: 'Gemma 结果是 worst tier 叙事的关键对照——证明 Pareto frontier 在 dense 架构上仍然有效， MoE\n    的 failure 是 architecture-specific 的。这把 worst tier 从 \"method completely fails\"\n    转为 \"method works under specific architectural conditions\"——更有 nuance 的 viability\n    boundary。\n\n    '\n- name: Extended Language Coverage (50+ languages, P2 Camera-Ready)\n  plan_id: plan_009\n  description: '从 20 扩展到 50+ 语言，利用 GlobalMMLU/Belebele 的完整语言集。\n\n    '\n  expected_results:\n    total_languages_tested: 52\n    zs_transfer_success_rate_060: 22/51 (43%)\n    artifact_rate_overall: 0.42\n    artifact_rate_new_low_resource: 0.85\n    viability_boundary_clear: 'AUROC>0.60 AND selectivity>0.05: only 18/51 languages'\n    new_language_families_covered: 6\n  result_rationale: '扩展到 50+ 语言主要增加低资源语言（GlobalMMLU 覆盖的尾部语言）， 这些语言的 representation\n    quality 更差，artifact rate 更高（85%+）， 进一步支持 viability boundary 叙事。真正 viable 的语言仅\n    18/51（35%）， 全部是高/中资源。这个数字本身就是论文的核心 finding： probe-based calibration 仅对约 1/3 的测试语言可行。\n\n    '\n  tables:\n  - title: 'Table 21: Viability Classification (52 languages)'\n    columns:\n    - Category\n    - Count\n    - Criterion\n    - Example_langs\n    rows:\n    - - Viable\n      - 18\n      - AUROC>0.60 + sel>0.05\n      - en, zh, es, fr, de, ja, pt, ru, ko, nl...\n    - - Marginal\n      - 12\n      - AUROC>0.55 + sel 0.03-0.05\n      - hi, tr, pl, id, uk, ar...\n    - - Non-viable\n      - 22\n      - AUROC<0.55 OR sel<0.03\n      - sw, bn, te, am, yo, ha, ig...\n  figures_description:\n  - 'Fig 22: World map with viability color coding——欧洲/东亚 viable，撒哈拉以南非洲/南亚大部 non-viable。'\n  analysis: 52 语言版本强化了 viability boundary 叙事的 impact——从 \"20 语言上的发现\"  扩展为 \"across majority\n    of world's languages, probe-based calibration is not viable\"。 18/51 viable rate\n    是 headline-worthy 的。但注意这可能 overstate the problem： 低资源语言的 non-viability 部分来自 GlobalMMLU\n    翻译质量差， 而非 representation 本身的缺陷——需要在 discussion 中 acknowledge。\n",
      "numLines": 1702,
      "startLine": 1,
      "totalLines": 1702
    }
  },
  "sourceToolAssistantUUID": "19a2f8c3-e0a4-4915-9be6-5f30e98b2602",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "89f74592-e632-4d87-adff-4e5f492e3598",
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
  "lastPrompt": "[DREAM Review Director] dream_id=20260521T032808 | review_mode=simple | review_visible=True PDF: /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/…",
  "leafUuid": "7c568fc3-93e0-4ca9-9c63-0c2b245c799a",
  "sessionId": "89f74592-e632-4d87-adff-4e5f492e3598"
}
```

---

### Runtime record

_source line 17_

```json
{
  "type": "ai-title",
  "aiTitle": "Review cross-lingual calibration research paper",
  "sessionId": "89f74592-e632-4d87-adff-4e5f492e3598"
}
```

---

### Assistant

_source line 18 · 2026-05-21T04:26:50.173Z_

<details><summary>Logged reasoning block</summary>

```text
Let me read the PDF in chunks and also search for the submit tool.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7c568fc3-93e0-4ca9-9c63-0c2b245c799a",
  "isSidechain": false,
  "requestId": "req_011CbF5eHcRSE5z5m9DSQUEH",
  "type": "assistant",
  "uuid": "598e7cc6-87bc-44bd-96c4-4b473eae0e4c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "89f74592-e632-4d87-adff-4e5f492e3598",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WgyXb6ZJiwVGScxLJLiHs8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 38,
      "cache_creation_input_tokens": 26257,
      "cache_read_input_tokens": 23168,
      "output_tokens": 251,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 26257,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 38,
          "output_tokens": 251,
          "cache_read_input_tokens": 23168,
          "cache_creation_input_tokens": 26257,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 26257
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

_source line 19 · 2026-05-21T04:26:50.440Z_

让我分批读取 PDF 并搜索提交工具。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "598e7cc6-87bc-44bd-96c4-4b473eae0e4c",
  "isSidechain": false,
  "requestId": "req_011CbF5eHcRSE5z5m9DSQUEH",
  "type": "assistant",
  "uuid": "a2e3bd32-b2a9-4ca2-83ba-0c795f1857ea",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "89f74592-e632-4d87-adff-4e5f492e3598",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WgyXb6ZJiwVGScxLJLiHs8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 38,
      "cache_creation_input_tokens": 26257,
      "cache_read_input_tokens": 23168,
      "output_tokens": 251,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 26257,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 38,
          "output_tokens": 251,
          "cache_read_input_tokens": 23168,
          "cache_creation_input_tokens": 26257,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 26257
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

_source line 20 · 2026-05-21T04:26:53.139Z_

<details open><summary>🔧 Tool call — Read · `toolu_01M3oF9p6TMUvrttT7xJ4usN`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/worst/review_input_f5f46a62.pdf",
  "pages": "1-5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a2e3bd32-b2a9-4ca2-83ba-0c795f1857ea",
  "isSidechain": false,
  "requestId": "req_011CbF5eHcRSE5z5m9DSQUEH",
  "type": "assistant",
  "uuid": "b63ca6b4-1ffd-4dc2-af2f-66b4c9724186",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "89f74592-e632-4d87-adff-4e5f492e3598",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WgyXb6ZJiwVGScxLJLiHs8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 38,
      "cache_creation_input_tokens": 26257,
      "cache_read_input_tokens": 23168,
      "output_tokens": 251,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 26257,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 38,
          "output_tokens": 251,
          "cache_read_input_tokens": 23168,
          "cache_creation_input_tokens": 26257,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 26257
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

_source line 21 · 2026-05-21T04:26:53.861Z_

<details><summary>↩ Tool result · `toolu_01ACZWiXxXYnwwM1T8TSvmo2`</summary>

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
  "parentUuid": "d0d073e7-bd0b-441c-8175-f5dbe41c6155",
  "isSidechain": false,
  "promptId": "221e9c50-d73e-4401-b409-8fd8dd5897a7",
  "type": "user",
  "uuid": "8916cfa6-d381-4a50-a846-bad77ab6cd5e",
  "toolUseResult": {
    "matches": [
      "mcp__agent-ml-research__submit_dream_review_report"
    ],
    "query": "select:mcp__agent-ml-research__submit_dream_review_report",
    "total_deferred_tools": 23
  },
  "sourceToolAssistantUUID": "d0d073e7-bd0b-441c-8175-f5dbe41c6155",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "89f74592-e632-4d87-adff-4e5f492e3598",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-21T04:26:53.373Z_

<details><summary>↩ Tool result · `toolu_01M3oF9p6TMUvrttT7xJ4usN`</summary>

```text
PDF pages extracted: 5 page(s) from /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/worst/review_input_f5f46a62.pdf (195.5KB)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b63ca6b4-1ffd-4dc2-af2f-66b4c9724186",
  "isSidechain": false,
  "promptId": "221e9c50-d73e-4401-b409-8fd8dd5897a7",
  "type": "user",
  "uuid": "4769e091-8dd0-417d-b47a-7be34132ac4e",
  "toolUseResult": {
    "type": "parts",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/worst/review_input_f5f46a62.pdf",
      "originalSize": 200195,
      "outputDir": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0519-2-projects-xling-calib-direction/89f74592-e632-4d87-adff-4e5f492e3598/tool-results/pdf-6b6d5dd8-fd53-4fec-a238-de76c82b79d2",
      "count": 5
    }
  },
  "sourceToolAssistantUUID": "b63ca6b4-1ffd-4dc2-af2f-66b4c9724186",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "89f74592-e632-4d87-adff-4e5f492e3598",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

## Round 2

7 recorded events

### User

_source line 23 · 2026-05-21T04:26:53.372Z_

```json
{
  "type": "image",
  "source": {
    "type": "base64",
    "media_type": "image/jpeg",
    "data": "[ATTACHMENT_DATA_REDACTED]"
  }
}
```

```json
{
  "type": "image",
  "source": {
    "type": "base64",
    "media_type": "image/jpeg",
    "data": "[ATTACHMENT_DATA_REDACTED]"
  }
}
```

```json
{
  "type": "image",
  "source": {
    "type": "base64",
    "media_type": "image/jpeg",
    "data": "[ATTACHMENT_DATA_REDACTED]"
  }
}
```

```json
{
  "type": "image",
  "source": {
    "type": "base64",
    "media_type": "image/jpeg",
    "data": "[ATTACHMENT_DATA_REDACTED]"
  }
}
```

```json
{
  "type": "image",
  "source": {
    "type": "base64",
    "media_type": "image/jpeg",
    "data": "[ATTACHMENT_DATA_REDACTED]"
  }
}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4769e091-8dd0-417d-b47a-7be34132ac4e",
  "isSidechain": false,
  "promptId": "221e9c50-d73e-4401-b409-8fd8dd5897a7",
  "type": "user",
  "isMeta": true,
  "uuid": "117ee0e9-e90f-4445-a634-8ed499b9896d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "89f74592-e632-4d87-adff-4e5f492e3598",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-21T04:26:53.858Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01ACZWiXxXYnwwM1T8TSvmo2`</summary>

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
  "parentUuid": "117ee0e9-e90f-4445-a634-8ed499b9896d",
  "isSidechain": false,
  "requestId": "req_011CbF5eHcRSE5z5m9DSQUEH",
  "type": "assistant",
  "uuid": "d0d073e7-bd0b-441c-8175-f5dbe41c6155",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "89f74592-e632-4d87-adff-4e5f492e3598",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WgyXb6ZJiwVGScxLJLiHs8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 38,
      "cache_creation_input_tokens": 26257,
      "cache_read_input_tokens": 23168,
      "output_tokens": 251,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 26257,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 38,
          "output_tokens": 251,
          "cache_read_input_tokens": 23168,
          "cache_creation_input_tokens": 26257,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 26257
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

_source line 25_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[DREAM Review Director] dream_id=20260521T032808 | review_mode=simple | review_visible=True PDF: /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/…",
  "leafUuid": "8916cfa6-d381-4a50-a846-bad77ab6cd5e",
  "sessionId": "89f74592-e632-4d87-adff-4e5f492e3598"
}
```

---

### Runtime record

_source line 26_

```json
{
  "type": "ai-title",
  "aiTitle": "Review cross-lingual calibration research paper",
  "sessionId": "89f74592-e632-4d87-adff-4e5f492e3598"
}
```

---

### Assistant

_source line 27 · 2026-05-21T04:26:58.388Z_

Reading remaining pages of the PDF.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8916cfa6-d381-4a50-a846-bad77ab6cd5e",
  "isSidechain": false,
  "requestId": "req_011CbF5ep12d3Qp8YkQBQNif",
  "type": "assistant",
  "uuid": "bce64c2d-d6c0-4744-9554-e6761afdac67",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "89f74592-e632-4d87-adff-4e5f492e3598",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XiF3wZNt8f1WDJqEPy52Aq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7345,
      "cache_read_input_tokens": 49425,
      "output_tokens": 252,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7345,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 252,
          "cache_read_input_tokens": 49425,
          "cache_creation_input_tokens": 7345,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7345
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

_source line 28 · 2026-05-21T04:27:01.788Z_

<details open><summary>🔧 Tool call — Read · `toolu_01XAnnAsTXgx9Noyf4Q9BxQb`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/worst/review_input_f5f46a62.pdf",
  "pages": "6-10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bce64c2d-d6c0-4744-9554-e6761afdac67",
  "isSidechain": false,
  "requestId": "req_011CbF5ep12d3Qp8YkQBQNif",
  "type": "assistant",
  "uuid": "aa540212-6fa7-403e-a0fa-fccf4cd014e9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "89f74592-e632-4d87-adff-4e5f492e3598",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XiF3wZNt8f1WDJqEPy52Aq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7345,
      "cache_read_input_tokens": 49425,
      "output_tokens": 252,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7345,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 252,
          "cache_read_input_tokens": 49425,
          "cache_creation_input_tokens": 7345,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7345
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

_source line 29 · 2026-05-21T04:27:01.985Z_

<details><summary>↩ Tool result · `toolu_01XAnnAsTXgx9Noyf4Q9BxQb`</summary>

```text
PDF pages extracted: 5 page(s) from /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/worst/review_input_f5f46a62.pdf (195.5KB)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "aa540212-6fa7-403e-a0fa-fccf4cd014e9",
  "isSidechain": false,
  "promptId": "221e9c50-d73e-4401-b409-8fd8dd5897a7",
  "type": "user",
  "uuid": "f9e73d54-de46-4ab0-8ec5-53bf24f4befe",
  "toolUseResult": {
    "type": "parts",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/worst/review_input_f5f46a62.pdf",
      "originalSize": 200195,
      "outputDir": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0519-2-projects-xling-calib-direction/89f74592-e632-4d87-adff-4e5f492e3598/tool-results/pdf-47ee6c12-10b1-40dc-a8bb-de2d476b2df3",
      "count": 5
    }
  },
  "sourceToolAssistantUUID": "aa540212-6fa7-403e-a0fa-fccf4cd014e9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "89f74592-e632-4d87-adff-4e5f492e3598",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

## Round 3

3 recorded events

### User

_source line 30 · 2026-05-21T04:27:01.984Z_

```json
{
  "type": "image",
  "source": {
    "type": "base64",
    "media_type": "image/jpeg",
    "data": "[ATTACHMENT_DATA_REDACTED]"
  }
}
```

```json
{
  "type": "image",
  "source": {
    "type": "base64",
    "media_type": "image/jpeg",
    "data": "[ATTACHMENT_DATA_REDACTED]"
  }
}
```

```json
{
  "type": "image",
  "source": {
    "type": "base64",
    "media_type": "image/jpeg",
    "data": "[ATTACHMENT_DATA_REDACTED]"
  }
}
```

```json
{
  "type": "image",
  "source": {
    "type": "base64",
    "media_type": "image/jpeg",
    "data": "[ATTACHMENT_DATA_REDACTED]"
  }
}
```

```json
{
  "type": "image",
  "source": {
    "type": "base64",
    "media_type": "image/jpeg",
    "data": "[ATTACHMENT_DATA_REDACTED]"
  }
}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f9e73d54-de46-4ab0-8ec5-53bf24f4befe",
  "isSidechain": false,
  "promptId": "221e9c50-d73e-4401-b409-8fd8dd5897a7",
  "type": "user",
  "isMeta": true,
  "uuid": "31ddca5f-2873-48a3-bbce-ee6232be2953",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "89f74592-e632-4d87-adff-4e5f492e3598",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-21T04:27:02.430Z_

<details open><summary>🔧 Tool call — Read · `toolu_01G7ASx4UTB5SRueeYb2tioi`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/worst/review_input_f5f46a62.pdf",
  "pages": "11-13"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "31ddca5f-2873-48a3-bbce-ee6232be2953",
  "isSidechain": false,
  "requestId": "req_011CbF5ep12d3Qp8YkQBQNif",
  "type": "assistant",
  "uuid": "d1c82e4a-de73-4ffb-8aec-180dc214bc95",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "89f74592-e632-4d87-adff-4e5f492e3598",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XiF3wZNt8f1WDJqEPy52Aq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7345,
      "cache_read_input_tokens": 49425,
      "output_tokens": 252,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7345,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 252,
          "cache_read_input_tokens": 49425,
          "cache_creation_input_tokens": 7345,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7345
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

_source line 32 · 2026-05-21T04:27:02.555Z_

<details><summary>↩ Tool result · `toolu_01G7ASx4UTB5SRueeYb2tioi`</summary>

```text
PDF pages extracted: 3 page(s) from /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/worst/review_input_f5f46a62.pdf (195.5KB)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d1c82e4a-de73-4ffb-8aec-180dc214bc95",
  "isSidechain": false,
  "promptId": "221e9c50-d73e-4401-b409-8fd8dd5897a7",
  "type": "user",
  "uuid": "542c0af8-6b45-4594-8679-b2791ce0f3cb",
  "toolUseResult": {
    "type": "parts",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/worst/review_input_f5f46a62.pdf",
      "originalSize": 200195,
      "outputDir": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0519-2-projects-xling-calib-direction/89f74592-e632-4d87-adff-4e5f492e3598/tool-results/pdf-21a312f4-f754-463f-bd27-d83f93a44f8b",
      "count": 3
    }
  },
  "sourceToolAssistantUUID": "d1c82e4a-de73-4ffb-8aec-180dc214bc95",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "89f74592-e632-4d87-adff-4e5f492e3598",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

## Round 4

13 recorded events

### User

_source line 33 · 2026-05-21T04:27:02.553Z_

```json
{
  "type": "image",
  "source": {
    "type": "base64",
    "media_type": "image/jpeg",
    "data": "[ATTACHMENT_DATA_REDACTED]"
  }
}
```

```json
{
  "type": "image",
  "source": {
    "type": "base64",
    "media_type": "image/jpeg",
    "data": "[ATTACHMENT_DATA_REDACTED]"
  }
}
```

```json
{
  "type": "image",
  "source": {
    "type": "base64",
    "media_type": "image/jpeg",
    "data": "[ATTACHMENT_DATA_REDACTED]"
  }
}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "542c0af8-6b45-4594-8679-b2791ce0f3cb",
  "isSidechain": false,
  "promptId": "221e9c50-d73e-4401-b409-8fd8dd5897a7",
  "type": "user",
  "isMeta": true,
  "uuid": "dc49e8ba-3bc6-47d9-8ee9-00f83ebdf310",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "89f74592-e632-4d87-adff-4e5f492e3598",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 34 · 2026-05-21T04:27:02.560Z_

```json
{
  "parentUuid": "dc49e8ba-3bc6-47d9-8ee9-00f83ebdf310",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "d87101d8-390b-4f4f-a205-33ef50c682c0",
  "timestamp": "2026-05-21T04:27:02.560Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "89f74592-e632-4d87-adff-4e5f492e3598",
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
  "lastPrompt": "[DREAM Review Director] dream_id=20260521T032808 | review_mode=simple | review_visible=True PDF: /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/…",
  "leafUuid": "d87101d8-390b-4f4f-a205-33ef50c682c0",
  "sessionId": "89f74592-e632-4d87-adff-4e5f492e3598"
}
```

---

### Runtime record

_source line 36_

```json
{
  "type": "ai-title",
  "aiTitle": "Review cross-lingual calibration research paper",
  "sessionId": "89f74592-e632-4d87-adff-4e5f492e3598"
}
```

---

### Assistant

_source line 37 · 2026-05-21T04:27:44.797Z_

<details><summary>Logged reasoning block</summary>

```text
I've now read the complete paper (13 pages) and the review context YAML. Let me compile a thorough review. 

The paper is titled "Stress-Testing Probe-Based Calibration Beyond English: Viability Boundaries, Capacity Artifacts, and When Cross-Lingual Transfer Breaks Down."

Let me now write the review, assessing against top ML venue standards (acceptance rate ~25%, 6-point scale).

Key observations from the paper:

**Summary**: The paper evaluates cross-lingual correctness probe transfer for LLM calibration across 52 languages, 3 architectures (2 MoE, 1 dense), and 5 transfer strategies. 

The main findings reveal that the depth-transferability tradeoff is architecture-dependent—showing up clearly on dense models but disappearing on MoE architectures—while distributional matching approaches prove ineffective. A significant portion of language-layer combinations (38% overall, 72% for low-resource languages) turn out to be capacity artifacts rather than genuine calibration improvements, and only 18 of 51 languages actually meet the viability criteria for reliable probe transfer.

**Strengths**: This addresses a critical gap since all existing probe-based calibration work focuses exclusively on English, making this the first systematic cross-lingual evaluation. The negative results around distributional matching are particularly well-characterized through parameter sweeps and component ablations.

The control task analysis extending prior work to multilingual settings represents a genuine methodological contribution, and the experimental scope is impressive—covering three architectures, 52 languages, and multiple benchmarks. The authors are transparent about their limitations, and the partial correlation analysis using CKA to isolate depth confounds shows sophisticated statistical thinking.

**Weaknesses**: The paper is largely a collection of negative results using existing techniques applied to a new domain rather than introducing novel methodology. The "viability boundary" framing, while compelling, may conflate representational limitations with translation quality issues in GlobalMMLU—a significant confound even if acknowledged. The MoE comparison relies on just two examples versus one dense model, which is too limited to support causal claims about routing behavior. The analysis cuts off here, but there appear to be additional concerns about the experimental design.

Now I'm reviewing the experimental coverage against the planned studies to see what was actually executed. All thirteen planned experiments check out across the paper—this is solid coverage. Now I'm moving into the formal review, starting with the overall assessment of whether the empirical characterization of these failure modes constitutes a meaningful contribution beyond what prior work like Zhao et al. already suggested about multilingual model limitations.

The viability boundary finding stands out as the strongest angle, though it's complicated by the confound between translation quality and what the representations actually capture. Reconsidering the score in context of a top-tier venue with typical acceptance rates, the systematic cross-lingual probe calibration and the control task artifact discovery are genuinely valuable contributions, and the experimental scope across three architectures, fifty-two languages, and multiple benchmarks demonstrates real rigor. But the lack of any proposed method to address these limitations is a significant gap—the paper identifies problems without offering solutions, which pushes it toward rejection despite the thorough empirical work.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d87101d8-390b-4f4f-a205-33ef50c682c0",
  "isSidechain": false,
  "requestId": "req_011CbF5fSYxoEVTudY2h4CyB",
  "type": "assistant",
  "uuid": "4cabe310-604e-4185-b18c-6c806d134a5e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "89f74592-e632-4d87-adff-4e5f492e3598",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y5vsT8jjr474fm2FHyK2SL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 10675,
      "cache_read_input_tokens": 56770,
      "output_tokens": 5158,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 10675,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 5158,
          "cache_read_input_tokens": 56770,
          "cache_creation_input_tokens": 10675,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 10675
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

_source line 38 · 2026-05-21T04:27:45.756Z_

I've read the full 13-page paper and the experiment design context. Now I'll compile the review and submit it.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4cabe310-604e-4185-b18c-6c806d134a5e",
  "isSidechain": false,
  "requestId": "req_011CbF5fSYxoEVTudY2h4CyB",
  "type": "assistant",
  "uuid": "cf730a2c-5d8d-4bf4-ab67-9908c90a0a58",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "89f74592-e632-4d87-adff-4e5f492e3598",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y5vsT8jjr474fm2FHyK2SL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 10675,
      "cache_read_input_tokens": 56770,
      "output_tokens": 5158,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 10675,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 5158,
          "cache_read_input_tokens": 56770,
          "cache_creation_input_tokens": 10675,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 10675
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

_source line 39 · 2026-05-21T04:29:06.692Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_dream_review_report · `toolu_01XCfWrUnv64SwKeqWFXCn7x`</summary>

```json
{
  "report": "# Review Report: Stress-Testing Probe-Based Calibration Beyond English\n\n## Paper Summary\n\nThis paper presents the first systematic evaluation of cross-lingual correctness probe transfer for LLM calibration, spanning 52 languages, three architectures (Qwen3-235B MoE, Llama 4 Scout MoE, Gemma 4 31B Dense), and five transfer strategies (zero-shot, mean-shift, linear projection, CaCLR, few-shot). The key findings are: (1) the depth–transferability Pareto frontier is architecture-dependent, significant only on the dense model and collapsing on both MoE architectures; (2) CaCLR (MMD-based distributional matching) is inert across all configurations; (3) 38% of language–layer probing combinations are capacity artifacts (72% for low-resource languages); and (4) only 18/51 target languages (35%) meet a joint viability criterion (AUROC>0.60 and selectivity>0.05). Few-shot target-language probes (25–100 examples) are the only consistently effective path forward.\n\n---\n\n## Strengths\n\n**S1. Important and timely research question.** All prior probe-based calibration work (Burns et al. 2023; Miao et al. 2026; Miao & Ungar 2026) is English-only. The paper asks the natural next question—does this extend cross-lingually?—and provides a systematic, honest answer. The community needs this kind of stress-testing before the probe-calibration paradigm is assumed to generalize.\n\n**S2. Thorough experimental coverage.** The paper covers 13 distinct experimental analyses across 3 architectures, 52 languages, 3 benchmarks, and 5 transfer methods. The inclusion of quantization validation (§5.11), cross-benchmark generalization (§5.10), and probe complexity ablation (§5.8) demonstrates careful attention to potential confounds. The scope is genuinely impressive for a single paper.\n\n**S3. Control task analysis is a real contribution.** Extending Hewitt & Liang's (2019) control task framework to multilingual probing and discovering that 72% of low-resource language–layer combinations are capacity artifacts is the paper's strongest finding. This is not merely a replication—the dramatic amplification of artifacts in the multilingual setting (72% vs. ~25% for English) is both surprising and consequential. Table 9 and Table 10 are compelling.\n\n**S4. CKA depth confound is a useful methodological warning.** The paper's demonstration that naively correlating CKA with transfer degradation produces a significant spurious correlation (pooled ρ=−0.28/−0.35, both p<0.01) that vanishes under partial correlation controlling for depth (r=0.04/0.08, both n.s.) is a cautionary finding that the representation similarity literature should heed (§5.5, Table 11).\n\n**S5. Honest framing of negative results.** The paper does not oversell. The discussion acknowledges limitations (MCQA-only, correlational MoE claim, translation quality confound) and the viability boundary is presented as \"a boundary condition the field must acknowledge\" rather than a fatal indictment. The tone is appropriate.\n\n---\n\n## Weaknesses\n\n**W1. No methodological novelty—the paper applies existing tools to a new setting.** The probing framework, CaCLR loss, control tasks, CKA analysis, and linear projection are all drawn directly from prior work. The sole \"new\" element is combining them in a cross-lingual evaluation. While empirical contributions have value, at a top ML venue the bar requires either (a) a novel method that partially solves the identified problem, or (b) a surprising theoretical insight explaining why the problem exists. The paper offers neither. The \"constructive paths forward\" (§6: few-shot, multilingual training, dense models) are all obvious; none are actually developed or evaluated beyond the basic few-shot experiment.\n\n**W2. Many negative results are predictable from prior theory.** CaCLR's failure is essentially a direct consequence of Zhao et al. (2019), which the paper itself cites: marginal distribution matching fails when conditional distributions P(Y|X) differ across domains. Since cross-lingual representations have different conditional distributions almost by definition, CaCLR's inertness is theoretically expected. The Pareto frontier collapse on MoE can be anticipated from the known input-dependence of expert routing. The paper would be substantially stronger if it derived these predictions before testing them, rather than framing them as empirical discoveries.\n\n**W3. The central \"viability boundary\" is confounded by evaluation data quality.** The paper acknowledges in the limitations that \"low-resource non-viability may partly reflect GlobalMMLU translation quality rather than representational limitations.\" This is not a minor caveat—it is a fundamental confound. If low-resource languages in GlobalMMLU have poor translations introducing systematic patterns that probes can exploit (contributing to capacity artifacts) or failing to provide a clean correctness signal (contributing to low AUROC), then the 35% viability rate may be an artifact of the evaluation data, not a property of the models' representations. The cross-benchmark generalization to Belebele and MMLU-ProX (§5.10) partially addresses this, but these benchmarks share similar translation pipelines and low-resource coverage issues. A validation on naturally-authored (non-translated) multilingual data would be needed to disentangle this.\n\n**W4. Statistical power issues are severe for some analyses.** Llama 4 Scout has only 12 probed layers, meaning Spearman ρ per language is computed on n=12 points. At this sample size, |ρ|>0.58 is needed for significance—the paper correctly reports this but still draws substantive conclusions from the Scout results (e.g., \"Pareto collapses on MoE\"). With n=12, the absence of significant ρ is expected even if a real effect exists. The architecture contrast would be more convincing if both MoE models had comparable sampling density to the dense model.\n\n**W5. Dense vs. MoE comparison is underpowered (n=2 MoE vs. n=1 dense).** The claim that MoE routing \"disrupts the monotonic depth–transfer relationship\" is based on comparing 2 MoE models against 1 dense model. This is correlational evidence at best. The two MoE models also differ in many other dimensions (parameter count, training data, quantization scheme, layer count) that could explain the Pareto collapse. A stronger design would include multiple dense models and ideally a dense/MoE pair from the same model family.\n\n**W6. Difficulty decomposition adds little.** Section 5.6 reports that projecting out the difficulty direction yields Δ AUROC = +0.005, far smaller than few-shot (+0.032). The difficulty-vs-random gap is significant in only 4/10 languages. This analysis occupies space but doesn't meaningfully advance the paper's claims—it could be cut or relegated to an appendix without loss.\n\n**W7. Paper is overloaded with results subsections.** Sections 5.1–5.12 present 12 distinct analyses, many with small marginal contributions (§5.6 difficulty decomposition, §5.7 orthogonality, §5.8 LR vs MLP, §5.11 quantization). The breadth comes at the cost of depth—several important findings (control task artifacts, Pareto architecture-dependence) deserve more thorough treatment. The paper reads as a collection of experiments rather than a coherent narrative building toward a central insight.\n\n---\n\n## Detailed Comments\n\n1. **Abstract**: The abstract is dense but effective. Consider leading with the viability boundary finding rather than the Pareto frontier—the former is the more impactful contribution.\n\n2. **§3.3 Mean-shift**: The proof that mean-shift produces ΔAUROC≡0 under standardized LR is elegant and should be stated more prominently—it saves the reader from wondering why mean-shift is even tested.\n\n3. **Table 1**: This is the most important table in the paper—placing it on page 4 (before Methods are fully described) is disorienting. Consider moving it to the Results section.\n\n4. **§5.3 CaCLR**: The explanation of *why* MMD fails (operating on 1-D probe logits, matching marginals not conditionals) is strong. However, this analysis could have been done a priori before running the expensive β sweep. The paper would benefit from acknowledging that CaCLR's 1-D logit formulation was arguably doomed from the start.\n\n5. **§5.4 Capacity artifacts**: This is the paper's strongest section. The selectivity heatmap (Table 9) is striking. One concern: the 0.05 selectivity threshold is borrowed from Hewitt & Liang but was calibrated for English syntactic probing. Is this threshold appropriate for multilingual correctness probing? A sensitivity analysis around the threshold (e.g., 0.03, 0.05, 0.10) would strengthen the claim.\n\n6. **§5.5 CKA**: The partial correlation analysis is the right test to run. The \"Simpson's paradox\" framing is apt. However, the same-layer analysis (Table showing only 5/36 significant) actually suggests CKA has some between-language signal at fixed depth—this nuance gets lost in the section's negative framing.\n\n7. **§5.9 Linear projection**: Tables 16–17 are informative. The finding that low-resource languages show *negative* Δ at 50 pairs is important—it means well-intentioned alignment can actively harm performance for the languages that need it most.\n\n8. **§5.12 Extended language coverage**: Table 20 is the paper's headline result but appears on the last content page with minimal discussion. This deserves more prominence.\n\n9. **Missing experiments/analyses**: \n   - No analysis of *which* items probes get wrong cross-lingually (error analysis)\n   - No evaluation of whether combining viable languages' probes could help marginal languages\n   - No investigation of whether the viability boundary correlates with model pretraining data distribution\n\n10. **References**: The reference list is appropriately sized (15 entries) for the paper length. All key prior works appear cited. Xiao et al. (2025) on knowledge-boundary probes is correctly distinguished from correctness probes.\n\n---\n\n## Questions for Authors\n\n1. Have you considered testing on a non-translated multilingual benchmark (e.g., naturally-authored QA data) to disentangle the translation quality confound from the representational viability boundary?\n\n2. For the control task analysis, what happens if you use MDL-based probing (Voita & Titov 2020) instead of the selectivity threshold? MDL may provide a more principled separation of memorization from genuine signal.\n\n3. The paper notes MoE routing as the mechanism for Pareto collapse, but doesn't directly test this (e.g., by analyzing expert activation overlap between English and target languages). Could you provide evidence that languages sharing more experts with English show stronger Pareto trends?\n\n4. Why was CaCLR restricted to operating on 1-D probe logits rather than on the full representation space? A version operating on higher-dimensional projections might perform differently.\n\n---\n\n## Experiment Coverage Assessment\n\nComparing against the full experimental design, the paper covers all 13 planned experiments:\n- Plans 001–002 (Pareto frontiers): §5.1, Tables 1–3 ✓\n- Plan 003 (CaCLR): §5.3, Tables 6–8 ✓\n- Plan 004 (Difficulty decomposition): §5.6, Table 13 ✓\n- Plan 005 (Orthogonality): §5.7, Table 14 ✓\n- Plan 006 (LR vs MLP): §5.8, Table 15 ✓\n- Plan 007 (Cross-benchmark): §5.10, Table 18 ✓\n- Plan 008 (Gemma dense): Appendix B, Table 1 ✓\n- Plan 009 (52 languages): §5.12, Table 20 ✓\n- Plan 010 (Quantization): §5.11, Table 19 ✓\n- Plan 011 (CKA): §5.5, Tables 11–12 ✓\n- Plan 012 (Linear projection efficiency): §5.9, Tables 16–17 ✓\n- Plan 013 (Control tasks): §5.4, Tables 9–10 ✓\n\nCoverage is comprehensive. The Gemma dense results (plan_008) are compressed into an appendix, which is reasonable for a camera-ready extension. The 52-language extension (plan_009) appears only as a classification table (Table 20) without detailed per-language results—more detail in supplementary would strengthen the claim.\n\n---\n\n## Minor Issues\n\n- Table numbering in the PDF text doesn't always match the actual table numbers (e.g., the text references \"Table 20\" for viability classification but it appears to be the last table)\n- The paper switches between \"19 target languages\" and \"20 languages\" (including English)—be consistent\n- §3.3: \"ΔAUROC≡0 mathematically\" deserves a footnote or one-line proof\n- The 52-language extended evaluation lacks a per-family breakdown that would be informative given the typological diversity claim\n\n---\n\n## Overall Assessment\n\n**Score: 3 / 6 (Weak Reject)**\n\n**Confidence: 4 / 5**\n\nThe paper tackles an important question—whether probe-based calibration extends beyond English—and provides a thorough empirical answer. The control task artifact finding (72% for low-resource) and the CKA depth confound are genuine contributions. However, the paper falls below the acceptance bar for a top ML venue for three reasons: (1) it applies existing methods to a new setting without proposing any novel technique that advances the state of the art; (2) several of the negative results (CaCLR inertness, MoE routing disruption) are predictable from prior theory rather than empirically surprising; and (3) the central viability boundary claim has an unresolved confound with evaluation data quality that limits the strength of the headline finding. The paper would benefit from either (a) proposing and validating a novel transfer method that pushes the viability boundary, or (b) providing theoretical analysis that explains *why* the boundary falls where it does and makes testable predictions. As currently written, it is a solid empirical survey that would be a strong fit for a Findings track or workshop paper but lacks the novelty or surprise factor for a top venue main conference.",
  "project": "xling_calib_direction",
  "tier": "worst",
  "dream_id": "20260521T032808",
  "overall_score": "3 — Weak Reject",
  "review_visible": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cf730a2c-5d8d-4bf4-ab67-9908c90a0a58",
  "isSidechain": false,
  "requestId": "req_011CbF5fSYxoEVTudY2h4CyB",
  "type": "assistant",
  "uuid": "113a2a65-fc33-4ff0-b65d-2ac7da1c90e9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "89f74592-e632-4d87-adff-4e5f492e3598",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y5vsT8jjr474fm2FHyK2SL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 10675,
      "cache_read_input_tokens": 56770,
      "output_tokens": 5158,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 10675,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 5158,
          "cache_read_input_tokens": 56770,
          "cache_creation_input_tokens": 10675,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 10675
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

_source line 40 · 2026-05-21T04:29:09.972Z_

<details><summary>↩ Tool result · `toolu_01XCfWrUnv64SwKeqWFXCn7x`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"report_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/worst/review_report.md\", \"dream_id\": \"dream_20260521T032808\", \"tier\": \"worst\", \"review_visible\": true}, \"error\": \"\"}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "113a2a65-fc33-4ff0-b65d-2ac7da1c90e9",
  "isSidechain": false,
  "promptId": "221e9c50-d73e-4401-b409-8fd8dd5897a7",
  "type": "user",
  "uuid": "a811aaa3-d5fa-4d40-8054-0ce97eb9c8d7",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"report_path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/worst/review_report.md\\\", \\\"dream_id\\\": \\\"dream_20260521T032808\\\", \\\"tier\\\": \\\"worst\\\", \\\"review_visible\\\": true}, \\\"error\\\": \\\"\\\"}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"report_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/worst/review_report.md\", \"dream_id\": \"dream_20260521T032808\", \"tier\": \"worst\", \"review_visible\": true}, \"error\": \"\"}"
    }
  },
  "sourceToolAssistantUUID": "113a2a65-fc33-4ff0-b65d-2ac7da1c90e9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "89f74592-e632-4d87-adff-4e5f492e3598",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 41 · 2026-05-21T04:29:20.641Z_

审稿完成。评分 **3/6 (Weak Reject)**。

核心判断：
- **最强贡献**：control task 揭示 72% 低资源 lang-layer 组合为 capacity artifact（Hewitt & Liang 多语言扩展），CKA depth confound 的方法论警示
- **主要不足**：无方法论创新（全部使用已有工具）；多个负面结果可从先验理论预测（CaCLR 失败 = Zhao et al. 2019 的直接推论）；viability boundary 的核心 claim 与评测数据翻译质量混淆未解决
- **建议提升方向**：提出至少一个新 transfer 方法推进 viability boundary，或提供理论分析解释 boundary 位置并给出可验证预测

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a811aaa3-d5fa-4d40-8054-0ce97eb9c8d7",
  "isSidechain": false,
  "requestId": "req_011CbF5pqUMsMjJ3guzvhsaH",
  "type": "assistant",
  "uuid": "fbcb50b7-0724-4769-9b82-52f352e3fa0e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "89f74592-e632-4d87-adff-4e5f492e3598",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018k85Dkz45zAi3gkhYuahTb",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5285,
      "cache_read_input_tokens": 67445,
      "output_tokens": 237,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5285,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 237,
          "cache_read_input_tokens": 67445,
          "cache_creation_input_tokens": 5285,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5285
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
  "lastPrompt": "[DREAM Review Director] dream_id=20260521T032808 | review_mode=simple | review_visible=True PDF: /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/…",
  "leafUuid": "fbcb50b7-0724-4769-9b82-52f352e3fa0e",
  "sessionId": "89f74592-e632-4d87-adff-4e5f492e3598"
}
```

---

### Runtime record

_source line 43_

```json
{
  "type": "ai-title",
  "aiTitle": "Review cross-lingual calibration research paper",
  "sessionId": "89f74592-e632-4d87-adff-4e5f492e3598"
}
```

---

### Runtime record

_source line 44_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[DREAM Review Director] dream_id=20260521T032808 | review_mode=simple | review_visible=True PDF: /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/…",
  "leafUuid": "fbcb50b7-0724-4769-9b82-52f352e3fa0e",
  "sessionId": "89f74592-e632-4d87-adff-4e5f492e3598"
}
```

---

### Runtime record

_source line 45_

```json
{
  "type": "ai-title",
  "aiTitle": "Review cross-lingual calibration research paper",
  "sessionId": "89f74592-e632-4d87-adff-4e5f492e3598"
}
```

---
