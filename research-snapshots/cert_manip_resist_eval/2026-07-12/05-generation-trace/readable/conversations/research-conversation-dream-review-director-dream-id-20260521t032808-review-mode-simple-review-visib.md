# Research conversation: [DREAM Review Director] dream_id=20260521T032808 | review_mode=simple | review_visible=True PDF: /home/ubuntu/.agent-ml-

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 46
- **Recorded user turns:** 4
- **Tool calls:** 8
- **Original source:** `logs/chats/exported-trajectories/account-3/5336efaf-2e22-419f-b322-39a8a1fc07df.jsonl`
- **Structured JSON:** [`3fe1502a67ebdba9da65.json`](../../sessions/3f/3fe1502a67ebdba9da65.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-21T04:22:13.115Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-21T04:22:13.115Z",
  "sessionId": "5336efaf-2e22-419f-b322-39a8a1fc07df",
  "content": "[DREAM Review Director]\ndream_id=20260521T032808 | review_mode=simple | review_visible=True\nPDF: /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/best/review_input_db82206b.pdf\n\n（内部编排信息：tier=best，仅用于 submit_dream_review_report 调用。\n你在向 Reviewer 发送审稿任务时，**严禁**提及档位名称 best/median/worst，\n也不要暗示论文结果的好坏。Reviewer 必须盲审。）\n\n任务：对上述 PDF 进行 simple 模式审稿。 使用 `dream-review-simple` skill 的 dispatch 模板（1 Reviewer 全面覆盖，跳过 Step 2 交叉分享 + Step 3 收敛）。\n\n## 审稿标准\n\n未指定目标 venue。请按 top ML venue 通用标准审稿（接受率 ~25%，6 分制：1=Strong Reject … 6=Strong Accept）。\n\n## 实验设计参考\n\n完整实验设计（含想象实验列表）：`/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/best/review_context.yaml`\n论文可能未完整反映所有实验——参考此文件判断覆盖度。\n完成后必须调用 `submit_dream_review_report(report, project=\"xling_calib_direction\", tier=\"best\", dream_id=\"20260521T032808\", review_visible=True)` —— 报告会写入 dream_reports/dream_20260521T032808/best/review_report.md，编排进程通过 subprocess 退出读取它。\n不要调用 submit_review_report_to_research_director / update_review_issues / request_external_review —— 这些工具不在 Dream Review Director 白名单内。\n"
}
```

---

### Runtime record

_source line 2 · 2026-05-21T04:22:13.118Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-21T04:22:13.118Z",
  "sessionId": "5336efaf-2e22-419f-b322-39a8a1fc07df"
}
```

---

## Round 1

20 recorded events

### User

_source line 3 · 2026-05-21T04:22:13.160Z_

[DREAM Review Director]
dream_id=20260521T032808 | review_mode=simple | review_visible=True
PDF: /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/best/review_input_db82206b.pdf

（内部编排信息：tier=best，仅用于 submit_dream_review_report 调用。
你在向 Reviewer 发送审稿任务时，**严禁**提及档位名称 best/median/worst，
也不要暗示论文结果的好坏。Reviewer 必须盲审。）

任务：对上述 PDF 进行 simple 模式审稿。 使用 `dream-review-simple` skill 的 dispatch 模板（1 Reviewer 全面覆盖，跳过 Step 2 交叉分享 + Step 3 收敛）。

## 审稿标准

未指定目标 venue。请按 top ML venue 通用标准审稿（接受率 ~25%，6 分制：1=Strong Reject … 6=Strong Accept）。

## 实验设计参考

完整实验设计（含想象实验列表）：`/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/best/review_context.yaml`
论文可能未完整反映所有实验——参考此文件判断覆盖度。
完成后必须调用 `submit_dream_review_report(report, project="xling_calib_direction", tier="best", dream_id="20260521T032808", review_visible=True)` —— 报告会写入 dream_reports/dream_20260521T032808/best/review_report.md，编排进程通过 subprocess 退出读取它。
不要调用 submit_review_report_to_research_director / update_review_issues / request_external_review —— 这些工具不在 Dream Review Director 白名单内。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "29945050-684f-4c5e-9353-e8166e9d5912",
  "type": "user",
  "uuid": "e96b774d-84e9-4714-abe6-aac35bf5b285",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "5336efaf-2e22-419f-b322-39a8a1fc07df",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-21T04:22:13.159Z_

```json
{
  "parentUuid": "e96b774d-84e9-4714-abe6-aac35bf5b285",
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
  "uuid": "514ce8b7-6596-4af4-988c-250c2949486a",
  "timestamp": "2026-05-21T04:22:13.159Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "5336efaf-2e22-419f-b322-39a8a1fc07df",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-21T04:22:13.159Z_

```json
{
  "parentUuid": "514ce8b7-6596-4af4-988c-250c2949486a",
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
  "uuid": "69c4a6e0-ffad-4a55-96b0-2cd83687e62d",
  "timestamp": "2026-05-21T04:22:13.159Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "5336efaf-2e22-419f-b322-39a8a1fc07df",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6 · 2026-05-21T04:22:13.159Z_

```json
{
  "parentUuid": "69c4a6e0-ffad-4a55-96b0-2cd83687e62d",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "8f098039-88cf-42c3-8b75-9fc1a67d808d",
  "timestamp": "2026-05-21T04:22:13.159Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "5336efaf-2e22-419f-b322-39a8a1fc07df",
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
  "sessionId": "5336efaf-2e22-419f-b322-39a8a1fc07df"
}
```

---

### Assistant

_source line 8 · 2026-05-21T04:22:20.006Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to perform a DREAM review of a PDF paper. Let me first understand the task:

1. I need to review a PDF paper located at a specific path
2. I should use the `dream-review-simple` skill dispatch template (1 Reviewer, skip cross-sharing and convergence steps)
3. Review against top ML venue standards (acceptance rate ~25%, 6-point scale)
4. Reference the experimental design context file
5. Submit the review via `submit_dream_review_report`

Let me start by:
1. Reading the PDF
2. Reading the review context YAML


3. Loading the necessary tools and files to conduct the review and submit it.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8f098039-88cf-42c3-8b75-9fc1a67d808d",
  "isSidechain": false,
  "requestId": "req_011CbF5J7RC2VAZDruT1Kvby",
  "type": "assistant",
  "uuid": "a6689d0a-14b6-48d5-a3cf-9a25617d9f25",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "5336efaf-2e22-419f-b322-39a8a1fc07df",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0193cr4ZatbGcSmYHb88mok6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11325,
      "cache_read_input_tokens": 11841,
      "output_tokens": 465,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11325,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 465,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11325,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11325
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

_source line 9 · 2026-05-21T04:22:20.026Z_

我来审稿这篇论文。先读取 PDF、实验设计上下文和所需工具。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a6689d0a-14b6-48d5-a3cf-9a25617d9f25",
  "isSidechain": false,
  "requestId": "req_011CbF5J7RC2VAZDruT1Kvby",
  "type": "assistant",
  "uuid": "8f3e8587-1748-4d9a-8f53-e31feb890084",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "5336efaf-2e22-419f-b322-39a8a1fc07df",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0193cr4ZatbGcSmYHb88mok6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11325,
      "cache_read_input_tokens": 11841,
      "output_tokens": 465,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11325,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 465,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11325,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11325
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

_source line 10 · 2026-05-21T04:22:21.229Z_

<details open><summary>🔧 Tool call — Read · `toolu_01NqB8wPJF7XDxJmGvfMT1LV`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/best/review_input_db82206b.pdf"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8f3e8587-1748-4d9a-8f53-e31feb890084",
  "isSidechain": false,
  "requestId": "req_011CbF5J7RC2VAZDruT1Kvby",
  "type": "assistant",
  "uuid": "abc56df2-d416-4eaf-a9c5-874ddfeabcc1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "5336efaf-2e22-419f-b322-39a8a1fc07df",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0193cr4ZatbGcSmYHb88mok6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11325,
      "cache_read_input_tokens": 11841,
      "output_tokens": 465,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11325,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 465,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11325,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11325
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

_source line 11 · 2026-05-21T04:22:22.083Z_

<details><summary>↩ Tool result · `toolu_01MXw6RMXh7R19kREPhUqSmt`</summary>

```text
No matching deferred tools found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3c46fe35-1388-476a-8310-92dd22d4c079",
  "isSidechain": false,
  "promptId": "29945050-684f-4c5e-9353-e8166e9d5912",
  "type": "user",
  "uuid": "9dee5b92-b834-44f9-a7d7-294597ba063a",
  "toolUseResult": {
    "matches": [],
    "query": "select:submit_dream_review_report",
    "total_deferred_tools": 23
  },
  "sourceToolAssistantUUID": "3c46fe35-1388-476a-8310-92dd22d4c079",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "5336efaf-2e22-419f-b322-39a8a1fc07df",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-21T04:22:21.262Z_

<details><summary>↩ Tool result · reported error · `toolu_01NqB8wPJF7XDxJmGvfMT1LV`</summary>

```text
This PDF has 12 pages, which is too many to read at once. Use the pages parameter to read specific page ranges (e.g., pages: "1-5"). Maximum 20 pages per request.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "abc56df2-d416-4eaf-a9c5-874ddfeabcc1",
  "isSidechain": false,
  "promptId": "29945050-684f-4c5e-9353-e8166e9d5912",
  "type": "user",
  "uuid": "c3ebd686-4da3-48d4-8e1b-47917d327399",
  "toolUseResult": "Error: This PDF has 12 pages, which is too many to read at once. Use the pages parameter to read specific page ranges (e.g., pages: \"1-5\"). Maximum 20 pages per request.",
  "sourceToolAssistantUUID": "abc56df2-d416-4eaf-a9c5-874ddfeabcc1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "5336efaf-2e22-419f-b322-39a8a1fc07df",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-21T04:22:21.580Z_

<details open><summary>🔧 Tool call — Read · `toolu_01PayrvButsVwsQcMD8XcaYg`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/best/review_context.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c3ebd686-4da3-48d4-8e1b-47917d327399",
  "isSidechain": false,
  "requestId": "req_011CbF5J7RC2VAZDruT1Kvby",
  "type": "assistant",
  "uuid": "25caf90b-58a8-462f-b3a8-1f47df11e3bb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "5336efaf-2e22-419f-b322-39a8a1fc07df",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0193cr4ZatbGcSmYHb88mok6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11325,
      "cache_read_input_tokens": 11841,
      "output_tokens": 465,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11325,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 465,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11325,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11325
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

_source line 14 · 2026-05-21T04:22:21.862Z_

<details><summary>↩ Tool result · `toolu_01PayrvButsVwsQcMD8XcaYg`</summary>

```text
1	narrative_guidance: 'CaCLR 是正面方法贡献——β > 0 的 MMD consistency loss 在 probe logits 空间成功
2	
3	  对齐 correctness subspace，使零标签跨语言校准成为可能。Pareto frontier 在两种
4	
5	  架构上均 robust：Qwen3-235B 呈强负相关 (ρ ≈ -0.65)，Llama 4 Scout 呈弱但一致
6	
7	  的负相关 (ρ ≈ -0.33)。CKA partial correlation 控制 depth 后仍显著 (r ≈ 0.42,
8	
9	  p < 0.01)，支撑 geometric analysis framing。四个 claims 均以强形式提出，论文
10	
11	  以 method + discovery 双重贡献投稿。
12	
13	  Headline: "CaCLR enables zero-label cross-lingual calibration, reducing non-English
14	
15	  ECE by 22% vs temperature scaling across 20 languages on two architectures."
16	
17	  '
18	imagined_experiments:
19	- name: Qwen3-235B Full Pareto Frontier
20	  plan_id: plan_001
21	  description: 94层 MoE (INT4), 24 probed layers (每4层), 20语言, 4 transfer conditions
22	    (CaCLR 在 plan_003)
23	  expected_results:
24	    en_best_auroc: 0.832
25	    en_best_layer: 72
26	    en_auroc_range:
27	    - 0.548
28	    - 0.832
29	    en_best_ece_raw: 0.126
30	    zs_transfer_auroc_avg_20lang: 0.713
31	    zs_transfer_success_rate: 0.95
32	    zs_fail_langs:
33	    - am
34	    pareto_spearman_rho_global: -0.65
35	    pareto_spearman_rho_per_lang_range:
36	    - -0.82
37	    - -0.41
38	    zs_auroc_by_tier:
39	      HIGH_avg: 0.773
40	      MID_avg: 0.719
41	      LOW_avg: 0.635
42	    zs_best_by_lang:
43	      zh:
44	        auroc: 0.79
45	        best_layer: 56
46	      es:
47	        auroc: 0.78
48	        best_layer: 60
49	      fr:
50	        auroc: 0.77
51	        best_layer: 56
52	      de:
53	        auroc: 0.77
54	        best_layer: 60
55	      ja:
56	        auroc: 0.75
57	        best_layer: 52
58	      pt:
59	        auroc: 0.78
60	        best_layer: 56
61	      it:
62	        auroc: 0.77
63	        best_layer: 60
64	      hi:
65	        auroc: 0.73
66	        best_layer: 48
67	      ru:
68	        auroc: 0.74
69	        best_layer: 52
70	      ko:
71	        auroc: 0.73
72	        best_layer: 52
73	      tr:
74	        auroc: 0.7
75	        best_layer: 44
76	      vi:
77	        auroc: 0.71
78	        best_layer: 48
79	      ar:
80	        auroc: 0.72
81	        best_layer: 52
82	      th:
83	        auroc: 0.7
84	        best_layer: 44
85	      sw:
86	        auroc: 0.65
87	        best_layer: 40
88	      bn:
89	        auroc: 0.66
90	        best_layer: 44
91	      yo:
92	        auroc: 0.61
93	        best_layer: 36
94	      te:
95	        auroc: 0.66
96	        best_layer: 44
97	      my:
98	        auroc: 0.63
99	        best_layer: 36
100	      am:
101	        auroc: 0.598
102	        best_layer: 36
103	    depth_transfer_snapshot:
104	      en_at_L72: 0.832
105	      zs_avg_at_L72: 0.672
106	      en_at_L56: 0.812
107	      zs_avg_at_L56: 0.728
108	      en_at_L40: 0.762
109	      zs_avg_at_L40: 0.706
110	    mean_shift_delta_auroc: 0.0
111	    linear_proj_50_delta_auroc_avg: 0.062
112	    fewshot_25_auroc_avg: 0.738
113	    fewshot_100_auroc_avg: 0.768
114	    bootstrap_ci_width_auroc: 0.018
115	  result_rationale: '235B MoE 拥有远比 7B 更结构化的内部表征。MVP Qwen2.5-7B EN best AUROC = 0.754;
116	
117	    235B 的 correctness direction 在中高层 (L48-L72) 线性可分度大幅提升至 0.83，
118	
119	    与 probing 文献中 "larger model → more linearly accessible features" 的规律一致。
120	
121	    更大模型的多语言预训练数据量级增加约 5-10x，跨语言对齐更强，zero-shot transfer
122	
123	    avg 从 MVP ~0.65 提升至 ~0.71。94 层结构提供精细 depth 分辨率：EN-optimal L72
124	
125	    (77% depth) 与 transfer-optimal zone L52-56 (55-60% depth) 间有 ~16 层间距，
126	
127	    产生清晰的强负相关 ρ ≈ -0.65。低资源语言的 ρ 更负 (sw -0.79, yo -0.82)，
128	
129	    因为这些语言在深层的表征特化最剧烈——模型的 language-specific expert routing
130	
131	    在深层对高资源语言保持跨语言共享，但对低资源语言已切换至 language-specific pathway。
132	
133	    Mean-shift AUROC delta 严格为零 (数学证明: StandardScaler + LR → 常数偏移 → rank
134	
135	    不变 → AUROC 不变)。仅 am (Amharic) 以 0.598 未达 0.60 阈值，因为 Qwen3 的
136	
137	    Amharic 预训练数据极少。
138	
139	    '
140	  tables:
141	  - name: 'Table 1: Qwen3-235B Pareto Frontier — Per-Language Summary'
142	    columns:
143	    - Language
144	    - Family
145	    - Resource
146	    - Best_ZS_AUROC
147	    - Best_ZS_Layer
148	    - EN_AUROC_at_Same_Layer
149	    - Spearman_rho
150	    - rho_p
151	    representative_rows:
152	    - - zh
153	      - Sinitic
154	      - HIGH
155	      - 0.79
156	      - L56
157	      - 0.812
158	      - -0.58
159	      - 0.003
160	    - - es
161	      - Romance
162	      - HIGH
163	      - 0.78
164	      - L60
165	      - 0.821
166	      - -0.53
167	      - 0.008
168	    - - ja
169	      - Japonic
170	      - HIGH
171	      - 0.75
172	      - L52
173	      - 0.802
174	      - -0.62
175	      - 0.001
176	    - - hi
177	      - Indo-Aryan
178	      - MID
179	      - 0.73
180	      - L48
181	      - 0.789
182	      - -0.67
183	      - <0.001
184	    - - ko
185	      - Koreanic
186	      - MID
187	      - 0.73
188	      - L52
189	      - 0.802
190	      - -0.61
191	      - 0.002
192	    - - ar
193	      - Semitic
194	      - MID
195	      - 0.72
196	      - L52
197	      - 0.802
198	      - -0.59
199	      - 0.003
200	    - - sw
201	      - Bantu
202	      - LOW
203	      - 0.65
204	      - L40
205	      - 0.762
206	      - -0.79
207	      - <0.001
208	    - - yo
209	      - Volta-Niger
210	      - LOW
211	      - 0.61
212	      - L36
213	      - 0.721
214	      - -0.82
215	      - <0.001
216	    - - am
217	      - Ethiosemitic
218	      - LOW
219	      - 0.598
220	      - L36
221	      - 0.721
222	      - -0.81
223	      - <0.001
224	  - name: 'Table 2: Transfer Conditions Comparison (Qwen3-235B, L56 Pareto Zone)'
225	    columns:
226	    - Condition
227	    - AUROC_Avg_20L
228	    - AUROC_HIGH
229	    - AUROC_MID
230	    - AUROC_LOW
231	    - ECE_Avg
232	    rows:
233	    - - Zero-shot
234	      - 0.728
235	      - 0.773
236	      - 0.726
237	      - 0.648
238	      - 0.165
239	    - - Mean-shift
240	      - 0.728
241	      - 0.773
242	      - 0.726
243	      - 0.648
244	      - 0.168
245	    - - Linear_proj_50
246	      - 0.79
247	      - 0.821
248	      - 0.789
249	      - 0.728
250	      - 0.139
251	    - - Few-shot_25
252	      - 0.745
253	      - 0.789
254	      - 0.742
255	      - 0.668
256	      - 0.152
257	    - - Few-shot_100
258	      - 0.774
259	      - 0.811
260	      - 0.773
261	      - 0.702
262	      - 0.136
263	  figures_description:
264	  - 'Fig 1a: Heatmap (y=24 layers, x=20 langs sorted by resource tier). Color = ZS
265	    AUROC. 深层左侧 (高资源) 保持暖色，深层右侧 (低资源) 转冷，显示 resource-dependent depth degradation.'
266	  - 'Fig 1b: Pareto scatter — x=EN AUROC, y=avg ZS transfer AUROC (each point = one
267	    layer, color = normalized depth). 清晰负斜率 ρ=-0.65, 右下角 (深层) 聚集.'
268	  - 'Fig 1c: Per-language Spearman ρ bar chart (grouped by resource tier). 低资源 bars
269	    更长 (更负).'
270	  analysis: 'Qwen3-235B 呈现教科书级 Pareto frontier。关键发现：(1) ρ=-0.65 远强于 MVP
271	
272	    7B 的约 -0.4，confirming 更大模型 → 更 structured representations → 更清晰
273	
274	    tradeoff；(2) transfer-optimal zone 在 40-60% depth (L36-L56)，EN-optimal 在
275	
276	    77% (L72)，gap = 16 层；(3) resource tier gradient: HIGH 0.77 > MID 0.72 > LOW
277	
278	    0.64，三级分明；(4) 19/20 languages transfer 成功，仅 am 失败。Linear proj
279	
280	    (50 pairs) 是最强迁移方法 (+6.2pp over ZS)，few-shot 100 紧随 (+4.6pp)。
281	
282	    '
283	- name: Llama 4 Scout Full Pareto Frontier
284	  plan_id: plan_002
285	  description: 48层 MoE (W4A16), 12 probed layers, 20语言, 4 transfer conditions
286	  expected_results:
287	    en_best_auroc: 0.811
288	    en_best_layer: 40
289	    en_auroc_range:
290	    - 0.574
291	    - 0.811
292	    en_best_ece_raw: 0.139
293	    zs_transfer_auroc_avg_20lang: 0.684
294	    zs_transfer_success_rate: 0.85
295	    zs_fail_langs:
296	    - yo
297	    - my
298	    - am
299	    pareto_spearman_rho_global: -0.33
300	    pareto_spearman_rho_per_lang_range:
301	    - -0.68
302	    - 0.18
303	    zs_auroc_by_tier:
304	      HIGH_avg: 0.743
305	      MID_avg: 0.694
306	      LOW_avg: 0.602
307	    zs_best_by_lang:
308	      zh:
309	        auroc: 0.76
310	        best_layer: 36
311	      es:
312	        auroc: 0.75
313	        best_layer: 36
314	      fr:
315	        auroc: 0.74
316	        best_layer: 32
317	      de:
318	        auroc: 0.74
319	        best_layer: 36
320	      ja:
321	        auroc: 0.72
322	        best_layer: 32
323	      pt:
324	        auroc: 0.75
325	        best_layer: 36
326	      it:
327	        auroc: 0.74
328	        best_layer: 36
329	      hi:
330	        auroc: 0.7
331	        best_layer: 36
332	      ru:
333	        auroc: 0.72
334	        best_layer: 40
335	      ko:
336	        auroc: 0.71
337	        best_layer: 40
338	      tr:
339	        auroc: 0.67
340	        best_layer: 32
341	      vi:
342	        auroc: 0.69
343	        best_layer: 32
344	      ar:
345	        auroc: 0.7
346	        best_layer: 40
347	      th:
348	        auroc: 0.67
349	        best_layer: 28
350	      sw:
351	        auroc: 0.62
352	        best_layer: 28
353	      bn:
354	        auroc: 0.63
355	        best_layer: 28
356	      yo:
357	        auroc: 0.57
358	        best_layer: 24
359	      te:
360	        auroc: 0.64
361	        best_layer: 28
362	      my:
363	        auroc: 0.58
364	        best_layer: 24
365	      am:
366	        auroc: 0.57
367	        best_layer: 24
368	    depth_transfer_snapshot:
369	      en_at_L40: 0.811
370	      zs_avg_at_L40: 0.654
371	      en_at_L32: 0.781
372	      zs_avg_at_L32: 0.691
373	      en_at_L24: 0.732
374	      zs_avg_at_L24: 0.682
375	    langs_with_positive_depth_rho:
376	    - ru
377	    - ko
378	    - ar
379	    mean_shift_delta_auroc: 0.0
380	    linear_proj_50_delta_auroc_avg: 0.058
381	    fewshot_25_auroc_avg: 0.706
382	    fewshot_100_auroc_avg: 0.741
383	  result_rationale: 'Llama 4 Scout (17B active × 16 experts, ~109B total) 的 EN AUROC
384	    达到 0.811，
385	
386	    低于 Qwen3-235B 但显著高于 MVP Llama-3.1-8B (0.728)。Pareto frontier 呈弱
387	
388	    负相关 ρ ≈ -0.33，延续 MVP 中 Llama 架构的模式：部分语言 (ru, ko, ar) 随
389	
390	    depth 增加迁移不退化甚至略微改善 (ρ > 0)，而 sw/yo/am 退化严重 (ρ < -0.60)。
391	
392	    这种异质性源于 Llama 4 的 16-expert MoE routing：对 ru/ko/ar 等中高资源语言，
393	
394	    深层 expert routing 倾向于重用与 English 共享的 expert；对低资源语言则分配到
395	
396	    specialized expert，导致表征分离。三种低资源语言 (yo 0.57, my 0.58, am 0.57)
397	
398	    未通过 0.60 阈值，success rate 17/20 = 0.85 达到 best tier 下限。48 层仅
399	
400	    12 probed layers，depth 分辨率低于 Qwen3 (24 layers)，ρ 估计的统计功效较低
401	
402	    (n=12 vs n=24)。
403	
404	    '
405	  tables:
406	  - name: 'Table 3: Llama 4 Scout Pareto Frontier — Per-Language Summary'
407	    columns:
408	    - Language
409	    - Family
410	    - Resource
411	    - Best_ZS_AUROC
412	    - Best_ZS_Layer
413	    - Spearman_rho
414	    - rho_p
415	    representative_rows:
416	    - - zh
417	      - Sinitic
418	      - HIGH
419	      - 0.76
420	      - L36
421	      - -0.45
422	      - 0.14
423	    - - es
424	      - Romance
425	      - HIGH
426	      - 0.75
427	      - L36
428	      - -0.41
429	      - 0.18
430	    - - ru
431	      - Slavic
432	      - MID
433	      - 0.72
434	      - L40
435	      - 0.05
436	      - 0.88
437	    - - ko
438	      - Koreanic
439	      - MID
440	      - 0.71
441	      - L40
442	      - 0.18
443	      - 0.57
444	    - - ar
445	      - Semitic
446	      - MID
447	      - 0.7
448	      - L40
449	      - -0.12
450	      - 0.71
451	    - - sw
452	      - Bantu
453	      - LOW
454	      - 0.62
455	      - L28
456	      - -0.62
457	      - 0.03
458	    - - yo
459	      - Volta-Niger
460	      - LOW
461	      - 0.57
462	      - L24
463	      - -0.68
464	      - 0.02
465	    - - am
466	      - Ethiosemitic
467	      - LOW
468	      - 0.57
469	      - L24
470	      - -0.65
471	      - 0.02
472	  figures_description:
473	  - 'Fig 2a: Pareto scatter (同 Fig 1b 格式) — 扁平斜率 ρ=-0.33, scatter 更大. ru/ko 偏离主趋势
474	    (正方向).'
475	  - 'Fig 2b: Per-language ρ comparison — Qwen3 vs Llama4 并排 bar chart. Qwen3 全负; Llama4
476	    有 3 语言正值.'
477	  - 'Fig 2c: Language-specific depth trajectory — 选 ru (上升), zh (平), sw (下降) 对比 Llama4
478	    的异质性.'
479	  analysis: 'Llama 4 Scout 的 Pareto 显著弱于 Qwen3-235B，core finding: architecture
480	
481	    determines tradeoff shape。ρ_Qwen=-0.65 vs ρ_Llama=-0.33, 且 Llama 呈现
482	
483	    language-specific 异质性 (3 种语言 ρ > 0)。这不是 Pareto 不存在——global ρ
484	
485	    仍为负——而是 tradeoff 在不同语言上表现不同。论文中框架为 "strong vs weak
486	
487	    Pareto" 的架构对比。
488	
489	    '
490	- name: CaCLR Full Evaluation
491	  plan_id: plan_003
492	  description: L_CaCLR = L_BCE + α·L_SB-ECE + β·L_MMD, 两种架构×20语言完整评估
493	  expected_results:
494	    best_alpha: 1.0
495	    best_beta: 0.1
496	    alpha_sweep:
497	      0.01:
498	        auroc: 0.741
499	        ece: 0.148
500	      0.1:
501	        auroc: 0.749
502	        ece: 0.138
503	      1.0:
504	        auroc: 0.763
505	        ece: 0.121
506	      10.0:
507	        auroc: 0.752
508	        ece: 0.128
509	    beta_sweep:
510	      0.0:
511	        auroc: 0.724
512	        ece: 0.148
513	      0.001:
514	        auroc: 0.728
515	        ece: 0.145
516	      0.01:
517	        auroc: 0.738
518	        ece: 0.137
519	      0.1:
520	        auroc: 0.763
521	        ece: 0.121
522	      1.0:
523	        auroc: 0.731
524	        ece: 0.141
525	    qwen_L56_pareto_zone:
526	      caclr_auroc_avg: 0.763
527	      zeroshot_auroc_avg: 0.728
528	      delta_auroc: 0.035
529	      caclr_ece_avg: 0.121
530	      tempscaling_ece_avg: 0.155
531	      delta_ece_vs_tempscaling: -0.034
532	    qwen_L72_en_optimal:
533	      caclr_auroc_avg: 0.728
534	      zeroshot_auroc_avg: 0.672
535	      delta_auroc: 0.056
536	      caclr_ece_avg: 0.132
537	      tempscaling_ece_avg: 0.171
538	      delta_ece_vs_tempscaling: -0.039
539	    qwen_oracle_per_lang:
540	      caclr_auroc_avg: 0.76
541	      zeroshot_auroc_avg: 0.713
542	      delta_auroc: 0.047
543	    llama_L32_pareto_zone:
544	      caclr_auroc_avg: 0.732
545	      zeroshot_auroc_avg: 0.691
546	      delta_auroc: 0.041
547	      caclr_ece_avg: 0.131
548	      tempscaling_ece_avg: 0.163
549	      delta_ece_vs_tempscaling: -0.032
550	    llama_L40_en_optimal:
551	      caclr_auroc_avg: 0.697
552	      zeroshot_auroc_avg: 0.654
553	      delta_auroc: 0.043
554	      caclr_ece_avg: 0.142
555	      tempscaling_ece_avg: 0.176
556	      delta_ece_vs_tempscaling: -0.034
557	    ablation:
558	      bce_only:
559	        auroc: 0.728
560	        ece: 0.165
561	      bce_sbece:
562	        auroc: 0.724
563	        ece: 0.148
564	      bce_mmd:
565	        auroc: 0.751
566	        ece: 0.136
567	      bce_sbece_mmd:
568	        auroc: 0.763
569	        ece: 0.121
570	    beta_vs_zero_paired_permutation_p: 0.003
571	    beta_vs_zero_cohens_d: 0.52
572	    beta_vs_zero_bootstrap_ci:
573	    - 0.024
574	    - 0.058
575	    caclr_delta_by_tier:
576	      HIGH: 0.031
577	      MID: 0.048
578	      LOW: 0.068
579	    pareto_rho_without_caclr: -0.65
580	    pareto_rho_with_caclr: -0.51
581	    pareto_shift_interpretation: CaCLR 减弱 Pareto tradeoff (rho 从 -0.65 到 -0.51), 因为深层迁移退化被部分修复
582	    mmd_kernel: Gaussian RBF, bandwidth=median heuristic
583	    optimizer: Adam, lr=1e-3, cosine decay to 1e-5
584	    epochs: 50
585	    early_stopping: patience=10, monitor val BCE loss
586	    initialization: warm-start from standard LR solution
587	    batch_size: 256
588	    mmd_items: same items as BCE (probe_train portion)
589	    parallel_set_size_per_lang_avg: 630
590	    parallel_set_size_per_lang_min: 580
591	    translation_quality_note: am/yo/my translations spot-checked, ~8% semantic drift
592	      vs high-resource
593	  result_rationale: 'Best tier 核心假设："MMD on probe logits 成功对齐 correctness subspace
594	    cross-
595	
596	    lingually"。为何成立：(1) 235B 模型的 correctness direction 占据低维语言无关
597	
598	    子空间 (CKA 分析支持)，因此 1D probe logit 的分布差异主要反映 subspace rotation
599	
600	    而非 intrinsic signal difference；MMD 通过匹配 logit 分布有效纠正这个 rotation。
601	
602	    (2) β=0.1 是 sweet spot——足以施加对齐压力 (MMD loss ~0.3 量级) 但不 overwhelm
603	
604	    BCE loss (初始 ~0.65 量级)；β=1.0 过大导致 MMD dominate，probe 为匹配分布而
605	
606	    牺牲判别力。(3) SB-ECE 单独贡献有限 (+0.006 AUROC)，但与 MMD 叠加有协同：
607	
608	    SB-ECE 改善 probability calibration 后，MMD 在更好校准的 logit 空间上匹配更
609	
610	    有效。(4) 低资源语言获益最大 (+0.068)，因为 zero-shot distribution gap 最大，
611	
612	    MMD 的边际对齐收益最高——与 Ben-David et al. H-divergence 理论一致。(5) 在
613	
614	    EN-optimal 深层 L72，CaCLR 增益更大 (+0.056 > +0.035)，因为深层迁移退化更
615	
616	    严重，recovery space 更大——直接证明 "CaCLR shifts the Pareto frontier"。
617	
618	    统计显著性: paired permutation test p=0.003, Cohen''s d=0.52 (medium effect),
619	
620	    bootstrap 95% CI [0.024, 0.058] 不含零。
621	
622	    '
623	  tables:
624	  - name: 'Table 4: CaCLR vs All Baselines (Fixed Layer, Pareto Zone)'
625	    columns:
626	    - Method
627	    - Qwen3_AUROC
628	    - Qwen3_ECE
629	    - Llama4_AUROC
630	    - Llama4_ECE
631	    - Labels_Required
632	    rows:
633	    - - Zero-shot
634	      - 0.728
635	      - 0.165
636	      - 0.691
637	      - 0.179
638	      - EN only
639	    - - Mean-shift
640	      - 0.728
641	      - 0.168
642	      - 0.691
643	      - 0.183
644	      - EN only
645	    - - Temp scaling
646	      - 0.728
647	      - 0.155
648	      - 0.691
649	      - 0.163
650	      - EN only
651	    - - CaCLR (α=1 β=0.1)
652	      - 0.763
653	      - 0.121
654	      - 0.732
655	      - 0.131
656	      - EN only + parallel inputs
657	    - - Linear proj (50)
658	      - 0.79
659	      - 0.139
660	      - 0.749
661	      - 0.146
662	      - 50 parallel pairs
663	    - - Few-shot (25)
664	      - 0.745
665	      - 0.152
666	      - 0.712
667	      - 0.159
668	      - 25 target labels
669	    - - Few-shot (100)
670	      - 0.774
671	      - 0.136
672	      - 0.745
673	      - 0.142
674	      - 100 target labels
675	  - name: 'Table 5: Component Ablation (Qwen3-235B, L56, Avg 20 Langs)'
676	    columns:
677	    - Components
678	    - AUROC
679	    - ECE
680	    - Delta_AUROC_vs_ZS
681	    rows:
682	    - - BCE only (= zero-shot)
683	      - 0.728
684	      - 0.165
685	      - —
686	    - - BCE + SB-ECE
687	      - 0.724
688	      - 0.148
689	      - -0.004
690	    - - BCE + MMD
691	      - 0.751
692	      - 0.136
693	      - 0.023
694	    - - BCE + SB-ECE + MMD
695	      - 0.763
696	      - 0.121
697	      - 0.035
698	  - name: 'Table 6: β Sensitivity (α=1.0 fixed, Qwen3 L56)'
699	    columns:
700	    - beta
701	    - AUROC
702	    - ECE
703	    - Delta_vs_beta0
704	    rows:
705	    - - 0.0
706	      - 0.724
707	      - 0.148
708	      - —
709	    - - 0.001
710	      - 0.728
711	      - 0.145
712	      - 0.004
713	    - - 0.01
714	      - 0.738
715	      - 0.137
716	      - 0.014
717	    - - 0.1
718	      - 0.763
719	      - 0.121
720	      - 0.039
721	    - - 1.0
722	      - 0.731
723	      - 0.141
724	      - 0.007
725	  figures_description:
726	  - 'Fig 3a: α-β grid heatmap (AUROC as color). Peak region around (α=1.0, β=0.1),
727	    smooth gradient.'
728	  - 'Fig 3b: CaCLR Pareto shift — Qwen3 scatter overlay: gray=zero-shot per-layer,
729	    red=CaCLR per-layer. Red points shifted up-right, ρ flattens from -0.65 to -0.51.'
730	  - 'Fig 3c: Per-language CaCLR gain (Δ AUROC), grouped by resource tier. LOW tier
731	    bars tallest.'
732	  - 'Fig 3d: β sweep curve (log scale x, AUROC y). Inverted-U, peak at β=0.1.'
733	  analysis: 'β > 0 统计显著地改善跨语言迁移 (p=0.003, d=0.52)。CaCLR 的核心价值：完全不需要
734	
735	    target-language correctness labels，仅需 parallel inputs (已通过 GlobalMMLU
736	
737	    翻译存在)。CaCLR 未超过 linear projection (50 pairs): 0.763 vs 0.790，但
738	
739	    CaCLR 无需 paired correctness labels。Two methods 互补：CaCLR 适用于无 parallel
740	
741	    pairs 的场景，linear projection 在有少量 parallel data 时更优。CaCLR 在深层
742	
743	    (EN-optimal) 增益更大 (+0.056) 证明它 shifts Pareto frontier，不只是 uniform
744	
745	    improvement。ECE reduction 22% vs temp scaling 构成论文 headline。
746	
747	    '
748	- name: Difficulty-Controlled Decomposition
749	  plan_id: plan_004
750	  description: IRT difficulty probe → project out → retrain → transfer delta. 10 langs
751	    × 8 layers × 2 models
752	  expected_results:
753	    difficulty_probe_r2_avg: 0.61
754	    difficulty_probe_r2_range:
755	    - 0.43
756	    - 0.76
757	    difficulty_probe_r2_by_lang:
758	      zh: 0.72
759	      es: 0.76
760	      de: 0.68
761	      fr: 0.71
762	      hi: 0.58
763	      ru: 0.65
764	      ko: 0.63
765	      tr: 0.53
766	      sw: 0.43
767	      bn: 0.47
768	    avg_transfer_delta_after_projection: 0.035
769	    delta_by_lang_category:
770	      capability_dominated:
771	        langs:
772	        - zh
773	        - es
774	        - fr
775	        - de
776	        - ru
777	        - ko
778	        delta: 0.042
779	        ci:
780	        - 0.031
781	        - 0.054
782	      difficulty_dominated:
783	        langs:
784	        - hi
785	        - tr
786	        - sw
787	        - bn
788	        delta: -0.018
789	        ci:
790	        - -0.029
791	        - -0.007
792	    random_projection_delta_avg: -0.003
793	    random_projection_delta_std: 0.008
794	    random_projection_delta_ci:
795	    - -0.011
796	    - 0.005
797	    delta_by_depth:
798	      20%: 0.012
799	      35%: 0.021
800	      50%: 0.035
801	      65%: 0.043
802	      80%: 0.051
803	      90%: 0.048
804	    qwen_avg_delta: 0.038
805	    llama_avg_delta: 0.031
806	    predicted_vs_actual_alignment_strategy_accuracy: 0.82
807	  result_rationale: 'Correctness signal 是 difficulty (跨语言共享——哪些题目本身更难) 和 capability
808	
809	    (语言特异性——模型在该语言上的推理能力) 的纠缠。对于 capability-dominated 语言
810	
811	    (高资源, 模型具备强推理)，difficulty 是共享但无用的噪声维度：projecting out
812	
813	    移除了对迁移有害的 confound，暴露纯粹的 capability signal，transfer 改善
814	
815	    +4.2pp。对于 difficulty-dominated 语言 (低资源, 模型 capability 弱)，difficulty
816	
817	    本身是 correctness 的主要来源 (模型答对题目主要靠题目简单，而非语言能力)——
818	
819	    移除它丢失了唯一可迁移的信号，transfer 下降 -1.8pp。深层 delta 更大 (80%
820	
821	    depth: +5.1pp vs 20%: +1.2pp)，因为 capability 特化在深层更强，difficulty
822	
823	    confound 的 relative 权重在深层更大。Random direction control 的 delta ≈ 0
824	
825	    排除了纯降维的 artifact。IRT difficulty probe R² 呈 resource gradient (zh 0.72
826	
827	    > sw 0.43)，因为 IRT difficulty scores 基于高资源语言的人类答题数据，低资源
828	
829	    语言的 difficulty 编码较弱。Prescriptive accuracy 82% 表明 decomposition
830	
831	    能正确预测 8/10 语言应该用哪种 alignment strategy。
832	
833	    '
834	  tables:
835	  - name: 'Table 7: Difficulty Decomposition Effect by Language Category'
836	    columns:
837	    - Category
838	    - Languages
839	    - N_langs
840	    - Delta_AUROC
841	    - CI_95
842	    - Random_Control
843	    rows:
844	    - - Capability-dominated
845	      - zh/es/fr/de/ru/ko
846	      - 6
847	      - 0.042
848	      - '[0.031, 0.054]'
849	      - -0.002
850	    - - Difficulty-dominated
851	      - hi/tr/sw/bn
852	      - 4
853	      - -0.018
854	      - '[-0.029, -0.007]'
855	      - -0.004
856	    - - Overall
857	      - all 10
858	      - 10
859	      - 0.035
860	      - '[0.021, 0.049]'
861	      - -0.003
862	  - name: 'Table 8: Depth × Decomposition Interaction'
863	    columns:
864	    - Depth_Pct
865	    - EN_Probe_AUROC
866	    - ZS_Delta_After_Proj
867	    - ZS_Delta_Capability_Only
868	    - ZS_Delta_Difficulty_Only
869	    rows:
870	    - - 20%
871	      - 0.65
872	      - 0.012
873	      - 0.018
874	      - -0.008
875	    - - 50%
876	      - 0.78
877	      - 0.035
878	      - 0.042
879	      - -0.016
880	    - - 80%
881	      - 0.82
882	      - 0.051
883	      - 0.061
884	      - -0.023
885	  figures_description:
886	  - 'Fig 4a: Scatter — x = baseline ZS transfer AUROC (proxy for capability), y =
887	    Δ AUROC after difficulty projection. 正相关: capability 越高, projection 越有益. 虚线 =
888	    decision boundary (Δ=0).'
889	  - 'Fig 4b: Depth × delta line plot — separate lines for capability-dominated (上升)
890	    vs difficulty-dominated (下降) 语言.'
891	  analysis: 'Decomposition 成功分离 difficulty/capability，fulfilling Claim 2。Prescriptive
892	
893	    value: 对于 capability-dominated 语言 (baseline ZS > ~0.70)，projecting out
894	
895	    difficulty 是 free lunch (+4.2pp)。对于 difficulty-dominated 语言 (baseline ZS
896	
897	    < ~0.65)，应保留 difficulty 信号。82% prediction accuracy 表明这个规则可
898	
899	    自动化为 per-language strategy selector。
900	
901	    '
902	- name: Cross-Lingual Orthogonality
903	  plan_id: plan_005
904	  description: Correctness vs verbalized confidence direction cosine similarity, 20
905	    langs × 2 archs
906	  expected_results:
907	    cosine_range:
908	    - 0.012
909	    - 0.058
910	    cosine_mean: 0.032
911	    cosine_std: 0.013
912	    cosine_by_tier:
913	      HIGH: 0.027
914	      MID: 0.033
915	      LOW: 0.04
916	    cosine_by_arch:
917	      Qwen3: 0.029
918	      Llama4: 0.035
919	    cosine_extremes:
920	      min:
921	        lang: es
922	        arch: Qwen3
923	        value: 0.012
924	      max:
925	        lang: am
926	        arch: Llama4
927	        value: 0.058
928	    cosine_per_lang:
929	      en:
930	        qwen: 0.023
931	        llama: 0.03
932	      zh:
933	        qwen: 0.021
934	        llama: 0.028
935	      es:
936	        qwen: 0.012
937	        llama: 0.024
938	      hi:
939	        qwen: 0.032
940	        llama: 0.039
941	      sw:
942	        qwen: 0.042
943	        llama: 0.049
944	      am:
945	        qwen: 0.048
946	        llama: 0.058
947	    permutation_test_vs_random_p: <0.001
948	    cosine_vs_resource_rho: 0.34
949	    cosine_vs_resource_p: 0.042
950	  result_rationale: 'Correctness 和 verbalized confidence 的正交性 (cosine < 0.06) 是 transformer
951	
952	    架构的内在特征：模型学会了在独立的表征子空间中编码 "我是否答对了" (correctness)
953	
954	    和 "我认为我有多确定" (confidence)。这不是 English-specific 现象。正交性在
955	
956	    所有 20 种语言上持续成立，因为两个方向都由模型的参数化决定，不由输入语言决定。
957	
958	    低资源语言的 cosine 略高 (0.040 vs 0.027) 有两个原因：(1) confidence probe
959	
960	    在低资源语言上的 SNR 更低，噪声使 cosine 估计偏离零；(2) 低资源语言的表征
961	
962	    空间利用率低，两个方向在低维子空间中更容易有 spurious overlap。但即使最高
963	
964	    的 am=0.058 仍远低于表示有意义相关性的阈值 (~0.2)。
965	
966	    '
967	  tables:
968	  - name: 'Table 9: Correctness-Confidence Orthogonality Across Languages'
969	    columns:
970	    - Language
971	    - Resource
972	    - Qwen3_Cosine
973	    - Llama4_Cosine
974	    - Average
975	    representative_rows:
976	    - - en
977	      - —
978	      - 0.023
979	      - 0.03
980	      - 0.027
981	    - - zh
982	      - HIGH
983	      - 0.021
984	      - 0.028
985	      - 0.025
986	    - - es
987	      - HIGH
988	      - 0.012
989	      - 0.024
990	      - 0.018
991	    - - hi
992	      - MID
993	      - 0.032
994	      - 0.039
995	      - 0.036
996	    - - ko
997	      - MID
998	      - 0.028
999	      - 0.035
1000	      - 0.032
1001	    - - sw
1002	      - LOW
1003	      - 0.042
1004	      - 0.049
1005	      - 0.046
1006	    - - am
1007	      - LOW
1008	      - 0.048
1009	      - 0.058
1010	      - 0.053
1011	  figures_description:
1012	  - 'Fig 5: Cosine similarity dot plot — 每个点 = 一种语言, x = Qwen3 cosine, y = Llama4
1013	    cosine. 所有点聚集在 [0, 0.06] × [0, 0.06] 区域, 远离 identity line. 虚线 = Miao & Ungar English
1014	    reference (0.04).'
1015	  analysis: 'Claim 4 完全成立。Output-based calibration 的结构性限制是跨语言普遍的——
1016	
1017	    所有 40 个 (language, architecture) 组合的 cosine < 0.06。Resource tier 与
1018	
1019	    cosine 弱正相关 (ρ=0.34, p=0.042)，但 effect size 极小 (range 仅 0.013)。
1020	
1021	    这进一步 motivate probe-based calibration：output 层面的信息理论限制不随
1022	
1023	    语言变化。
1024	
1025	    '
1026	- name: Probe Complexity Comparison
1027	  plan_id: plan_006
1028	  description: 'Logistic regression vs 2-layer MLP: EN accuracy 和 cross-lingual transfer
1029	    对比'
1030	  expected_results:
1031	    lr_en_best_auroc: 0.832
1032	    mlp_en_best_auroc: 0.851
1033	    mlp_en_advantage: 0.019
1034	    lr_zs_auroc_avg: 0.713
1035	    mlp_zs_auroc_avg: 0.685
1036	    lr_zs_advantage: 0.028
1037	    lr_relative_degradation: 0.143
1038	    mlp_relative_degradation: 0.195
1039	    mlp_excess_degradation: 0.052
1040	    lr_zs_low: 0.635
1041	    mlp_zs_low: 0.581
1042	    lr_vs_mlp_gap_low: 0.054
1043	    lr_zs_high: 0.773
1044	    mlp_zs_high: 0.752
1045	    lr_vs_mlp_gap_high: 0.021
1046	    lr_ece_avg: 0.165
1047	    mlp_ece_avg: 0.184
1048	  result_rationale: 'MLP 在 English 上略优 (+1.9pp) 是因为 correctness signal 含有弱非线性成分——
1049	
1050	    某些层的 correctness 编码涉及特征交互。但 MLP 同时学到了 English-specific 的
1051	
1052	    非线性 pattern (e.g. English-specific token position interactions)，这些 pattern
1053	
1054	    在目标语言中不存在，导致 transfer 时引入负迁移。Linear probe 的 inductive bias
1055	
1056	    恰好匹配 correctness direction 的跨语言结构：线性投影只能捕获方向性信息，
1057	
1058	    而方向性信息正是跨语言共享的 (CKA 子空间分析支持)。差距在低资源语言最大
1059	
1060	    (LR +5.4pp vs MLP)，因为低资源表征的线性结构相对于英语更保守 (低维对齐
1061	
1062	    更强)，而 MLP 学到的非线性 feature 在低资源语境下完全失效。
1063	
1064	    '
1065	  tables:
1066	  - name: 'Table S3: Probe Complexity × Transfer'
1067	    columns:
1068	    - Metric
1069	    - LR
1070	    - MLP_2layer
1071	    - Delta
1072	    rows:
1073	    - - EN Best AUROC
1074	      - 0.832
1075	      - 0.851
1076	      - 0.019
1077	    - - ZS Transfer Avg 20L
1078	      - 0.713
1079	      - 0.685
1080	      - -0.028
1081	    - - Relative Degradation
1082	      - 14.3%
1083	      - 19.5%
1084	      - +5.2pp
1085	    - - ZS Low-Resource Avg
1086	      - 0.635
1087	      - 0.581
1088	      - -0.054
1089	    - - ECE Avg
1090	      - 0.165
1091	      - 0.184
1092	      - 0.019
1093	  figures_description:
1094	  - 'Fig S1: Per-language transfer AUROC comparison (LR vs MLP), connected dots. MLP
1095	    consistently below LR, gap widens rightward (low-resource).'
1096	  analysis: 'Linear probe 是跨语言 transfer 的正确选择。MLP 的 +1.9pp English 优势远不足以
1097	
1098	    补偿 -2.8pp transfer 劣势。论文中以此证明 LR 作为默认 probe 的合理性。
1099	
1100	    '
1101	- name: Additional Benchmarks (Belebele + MMLU-ProX)
1102	  plan_id: plan_007
1103	  description: 最优 probes + CaCLR 在 Belebele 和 MMLU-ProX 上的泛化验证
1104	  expected_results:
1105	    belebele_qwen_en_auroc: 0.814
1106	    belebele_qwen_zs_avg: 0.698
1107	    belebele_qwen_caclr_avg: 0.741
1108	    belebele_qwen_pareto_rho: -0.61
1109	    belebele_llama_en_auroc: 0.793
1110	    belebele_llama_zs_avg: 0.671
1111	    belebele_llama_caclr_avg: 0.712
1112	    mmlupx_qwen_en_auroc: 0.839
1113	    mmlupx_qwen_zs_avg: 0.721
1114	    mmlupx_qwen_caclr_avg: 0.767
1115	    mmlupx_qwen_pareto_rho: -0.67
1116	    mmlupx_llama_en_auroc: 0.818
1117	    mmlupx_llama_zs_avg: 0.694
1118	    mmlupx_llama_caclr_avg: 0.738
1119	    per_lang_rank_corr_gmmlu_belebele: 0.89
1120	    per_lang_rank_corr_gmmlu_mmlupx: 0.93
1121	  result_rationale: 'Belebele 是 reading comprehension，与 GlobalMMLU (knowledge QA)
1122	    的 domain 不同。
1123	
1124	    Correctness direction 有轻微 domain dependency：probe 在 knowledge-heavy items
1125	
1126	    上学到的 correctness signal 不完全迁移到 comprehension tasks，EN AUROC 略降
1127	
1128	    (0.814 vs 0.832)。但 Pareto 结构高度一致 (ρ=-0.61 vs -0.65)，因为 depth-
1129	
1130	    transferability tradeoff 是架构特征而非 task 特征。MMLU-ProX 与 GlobalMMLU
1131	
1132	    domain overlap 大 (同属 knowledge QA)，结果最相似。Per-language ranking 跨
1133	
1134	    benchmark 高度稳定 (ρ=0.89-0.93)——在 GlobalMMLU 上 transfer 好的语言在
1135	
1136	    Belebele 上也好。CaCLR 增益在 Belebele 上略小 (+4.3pp vs +4.7pp) 但仍正面。
1137	
1138	    '
1139	  tables:
1140	  - name: 'Table 10: Cross-Benchmark Generalization (Qwen3-235B)'
1141	    columns:
1142	    - Benchmark
1143	    - Domain
1144	    - EN_AUROC
1145	    - ZS_Avg
1146	    - CaCLR_Avg
1147	    - Pareto_rho
1148	    - CaCLR_Delta
1149	    rows:
1150	    - - GlobalMMLU
1151	      - Knowledge QA
1152	      - 0.832
1153	      - 0.713
1154	      - 0.76
1155	      - -0.65
1156	      - 0.047
1157	    - - Belebele
1158	      - Reading Comp
1159	      - 0.814
1160	      - 0.698
1161	      - 0.741
1162	      - -0.61
1163	      - 0.043
1164	    - - MMLU-ProX
1165	      - Knowledge QA
1166	      - 0.839
1167	      - 0.721
1168	      - 0.767
1169	      - -0.67
1170	      - 0.046
1171	  figures_description:
1172	  - 'Fig S2: Per-language ZS AUROC scatter — GlobalMMLU (x) vs Belebele (y). High
1173	    correlation (ρ=0.89), all points near identity.'
1174	  analysis: '三 benchmark 一致性强。Pareto frontier 和 CaCLR gains 跨 domain replicate。
1175	
1176	    Belebele 的略低结果 underscores domain dependency 但不 undermine core claims。
1177	
1178	    '
1179	- name: Quantization Validation
1180	  plan_id: plan_010
1181	  description: W4A16 vs FP16 (Llama) + GPTQ-INT4 vs FP16 (Qwen), 5 layers, 5% subset
1182	  expected_results:
1183	    llama_w4a16_vs_fp16:
1184	      auroc_diff_avg: 0.004
1185	      auroc_diff_max: 0.008
1186	      auroc_diff_per_layer:
1187	        L8: 0.002
1188	        L16: 0.003
1189	        L24: 0.005
1190	        L32: 0.006
1191	        L40: 0.008
1192	      cka_quantized_vs_fp16: 0.987
1193	      paired_t_p: 0.31
1194	    qwen_int4_vs_fp16:
1195	      auroc_diff_avg: 0.006
1196	      auroc_diff_max: 0.013
1197	      auroc_diff_per_layer:
1198	        L16: 0.003
1199	        L32: 0.005
1200	        L48: 0.006
1201	        L64: 0.008
1202	        L80: 0.013
1203	      cka_quantized_vs_fp16: 0.981
1204	      paired_t_p: 0.18
1205	  result_rationale: 'W4A16 仅压缩权重 (4-bit)，激活保持 16-bit，因此对 correctness direction (线性
1206	
1207	    probe 的目标) 影响极小——probe 训练使用的是 activation vectors，不直接依赖权重
1208	
1209	    精度。GPTQ-INT4 的误差略大因为 4-bit 量化是更激进的压缩，且 Qwen3 有 94 层
1210	
1211	    导致误差累积更多。最大偏差 1.3pp 出现在最深层 L80 (误差在 94 层中逐层累积)。
1212	
1213	    所有差异在 paired t-test 下不显著 (p > 0.15)，CKA > 0.98 表示量化前后表征
1214	
1215	    几乎等价。论文中报告此验证可消除 reviewer "INT4/W4A16 artifacts" 的顾虑。
1216	
1217	    '
1218	  tables:
1219	  - name: 'Table S4: Quantization Validation'
1220	    columns:
1221	    - Model
1222	    - Quantization
1223	    - Avg_Delta_AUROC
1224	    - Max_Delta_AUROC
1225	    - CKA
1226	    - Paired_t_p
1227	    rows:
1228	    - - Llama 4 Scout
1229	      - W4A16
1230	      - 0.004
1231	      - 0.008
1232	      - 0.987
1233	      - 0.31
1234	    - - Qwen3-235B
1235	      - GPTQ-INT4
1236	      - 0.006
1237	      - 0.013
1238	      - 0.981
1239	      - 0.18
1240	  figures_description:
1241	  - 'Fig S3: Quantized vs FP16 AUROC per layer (error bar plot). All within noise
1242	    band.'
1243	  analysis: '量化不影响核心结论。最大偏差 1.3pp 远小于实验主要效应 (Pareto gap ~6pp,
1244	
1245	    CaCLR gain ~4.5pp)。放入 appendix 即可。
1246	
1247	    '
1248	- name: CKA Cross-Lingual Geometric Analysis
1249	  plan_id: plan_011
1250	  description: CKA (linear kernel) 20 langs × all layers × 2 archs, partial correlation
1251	    + subspace angle
1252	  expected_results:
1253	    cka_partial_corr_controlling_depth: 0.42
1254	    cka_partial_corr_p: 0.008
1255	    same_layer_corr_by_depth:
1256	      25%:
1257	        rho: -0.48
1258	        p: 0.032
1259	      50%:
1260	        rho: -0.67
1261	        p: 0.001
1262	      75%:
1263	        rho: -0.73
1264	        p: <0.001
1265	    n_significant_layers: 18
1266	    qwen_cka_cliff:
1267	      location: L64 (68% depth)
1268	      cka_before: 0.72
1269	      cka_after: 0.41
1270	      drop_magnitude: 0.31
1271	    llama_cka_pattern: gradual decline, no cliff
1272	    llama_cka_at_L40: 0.52
1273	    llama_cka_at_L24: 0.71
1274	    qwen_pooled_rho: -0.58
1275	    qwen_pooled_p: <0.001
1276	    llama_pooled_rho: -0.43
1277	    llama_pooled_p: 0.002
1278	    between_lang_rho_at_50pct_depth: -0.67
1279	    between_lang_p_at_50pct_depth: 0.001
1280	    between_lang_rho_at_75pct_depth: -0.73
1281	    between_lang_p_at_75pct_depth: <0.001
1282	    correctness_subspace_angle_avg_deg: 12.3
1283	    correctness_subspace_angle_std_deg: 4.8
1284	    global_repr_angle_avg_deg: 38.7
1285	    global_repr_angle_std_deg: 9.2
1286	    subspace_angle_ratio: 3.15
1287	    cka_collapse_threshold: 0.35
1288	    langs_below_threshold_at_deepest:
1289	    - sw
1290	    - yo
1291	    - am
1292	    - my
1293	    per_lang_within_rho_significant: 14
1294	    per_lang_within_rho_avg: -0.48
1295	  result_rationale: 'Best tier 假设 "CKA partial correlation 控制 depth 后仍显著"。Partial
1296	    r=0.42
1297	
1298	    (p=0.008) 表示 CKA 对 transfer degradation 有独立于 depth 的解释力。核心
1299	
1300	    机制：correctness direction 占据低维语言无关子空间 (principal angle ~12°)，
1301	
1302	    而全局表征差异远大 (~39°)，ratio 3.15。这意味着即使两种语言的全局表征已
1303	
1304	    显著分化 (CKA 下降)，correctness 子空间仍可能保持对齐——直到 CKA 跌破临界
1305	
1306	    阈值 ~0.35，此时全局分化足够大以至于连低维子空间也被扰动。
1307	
1308	    Qwen3 的 CKA cliff (L64, 突降 0.31) 解释了为何 Qwen Pareto 清晰：在 cliff
1309	
1310	    之前 (L0-L60)，transfer 随 depth 缓慢退化；在 cliff 之后 (L64-L94)，transfer
1311	
1312	    急剧崩溃。这产生了强 Pareto (ρ=-0.65) 和清晰的 "optimal transfer zone" (L48-L60)。
1313	
1314	    Llama4 没有 cliff，CKA 渐降 → Pareto 弱且异质 (ρ=-0.33)。
1315	
1316	    Between-language 分析 (固定层, n=20) 是最强统计检验：在 50% depth，CKA 高的
1317	
1318	    语言 (zh 0.82, es 0.79) transfer 好，CKA 低的 (sw 0.48, am 0.42) transfer 差，
1319	
1320	    ρ=-0.67 (p=0.001)。在 75% depth 更强 (ρ=-0.73)，因为此处 CKA variance 更大。
1321	
1322	    20 languages 的密度使 per-language within-lang Spearman 首次有足够统计功效
1323	
1324	    (n=24 for Qwen vs MVP 的 n=9)：14/20 显著，avg ρ=-0.48，比 MVP pilot
1325	
1326	    (几乎全 n.s.) 大幅改善。
1327	
1328	    '
1329	  tables:
1330	  - name: 'Table 11: CKA Partial Correlation Analysis'
1331	    columns:
1332	    - Analysis
1333	    - Statistic
1334	    - Value
1335	    - p_value
1336	    - Interpretation
1337	    rows:
1338	    - - Raw CKA-degradation pooled
1339	      - rho
1340	      - -0.64
1341	      - <0.001
1342	      - Confounded by depth
1343	    - - Partial corr controlling depth
1344	      - r
1345	      - 0.42
1346	      - 0.008
1347	      - CKA adds info beyond depth
1348	    - - Between-lang at 50% depth (n=20)
1349	      - rho
1350	      - -0.67
1351	      - 0.001
1352	      - Strongest cross-lang test
1353	    - - Between-lang at 75% depth (n=20)
1354	      - rho
1355	      - -0.73
1356	      - <0.001
1357	      - Even stronger deep
1358	    - - Within-lang avg (n=24 layers)
1359	      - rho
1360	      - -0.48
1361	      - varies
1362	      - 14/20 langs significant
1363	  - name: 'Table 12: Subspace Angle Analysis (Quantitative)'
1364	    columns:
1365	    - Measure
1366	    - Qwen3_235B
1367	    - Llama4_Scout
1368	    - Interpretation
1369	    rows:
1370	    - - Correctness subspace angle (avg)
1371	      - 11.2°
1372	      - 13.5°
1373	      - Small — cross-ling shared
1374	    - - Correctness subspace angle (std)
1375	      - 3.9°
1376	      - 5.7°
1377	      - More variable in Llama
1378	    - - Global representation angle (avg)
1379	      - 41.3°
1380	      - 36.1°
1381	      - Large — language-specific
1382	    - - Global/correctness ratio
1383	      - 3.69
1384	      - 2.67
1385	      - 'Qwen: correctness 4x more stable'
1386	    - - CKA cliff location
1387	      - 68% depth
1388	      - no cliff
1389	      - Architecture difference
1390	    - - CKA cliff magnitude
1391	      - 0.31
1392	      - N/A
1393	      - Qwen only
1394	  figures_description:
1395	  - 'Fig 6a: CKA heatmap (y=layer, x=language sorted by resource) — Qwen3. L64 处水平色带突变.'
1396	  - 'Fig 6b: CKA vs transfer degradation partial regression plot (controlling depth).
1397	    20 langs × multiple layers.'
1398	  - 'Fig 6c: Subspace angle comparison — bar pairs (correctness angle vs global angle)
1399	    per language pair. Correctness bars 远短于 global bars.'
1400	  - 'Fig 6d: CKA depth trajectory comparison — Qwen3 (cliff at L64) vs Llama4 (gradual).
1401	    Shaded region = transfer collapse zone (CKA < 0.35).'
1402	  analysis: 'CKA geometric analysis 成立 (partial r=0.42, p=0.008)，支撑 "geometric analysis"
1403	
1404	    framing。三层 evidence：(1) partial correlation 证明 CKA 有 depth 以外的解释力；
1405	
1406	    (2) between-language correlation (ρ=-0.67) 是最直接证据；(3) subspace angle ratio
1407	
1408	    3.15 提供几何直觉。CKA cliff 的有/无解释 Qwen vs Llama Pareto 差异。这是
1409	
1410	    discovery 级别 finding——连接了 representation geometry 和 practical transfer。
1411	
1412	    '
1413	- name: Linear Projection Sample Efficiency
1414	  plan_id: plan_012
1415	  description: Parallel pairs 数量 (10-200) 对 linear projection transfer 的影响
1416	  expected_results:
1417	    qwen_L56:
1418	      pairs_10:
1419	        auroc: 0.739
1420	        delta: 0.011
1421	        ci_width: 0.034
1422	      pairs_20:
1423	        auroc: 0.758
1424	        delta: 0.03
1425	        ci_width: 0.023
1426	      pairs_50:
1427	        auroc: 0.79
1428	        delta: 0.062
1429	        ci_width: 0.015
1430	      pairs_100:
1431	        auroc: 0.798
1432	        delta: 0.07
1433	        ci_width: 0.01
1434	      pairs_200:
1435	        auroc: 0.802
1436	        delta: 0.074
1437	        ci_width: 0.007
1438	    llama_L32:
1439	      pairs_10:
1440	        auroc: 0.712
1441	        delta: 0.021
1442	        ci_width: 0.031
1443	      pairs_20:
1444	        auroc: 0.729
1445	        delta: 0.038
1446	        ci_width: 0.022
1447	      pairs_50:
1448	        auroc: 0.749
1449	        delta: 0.058
1450	        ci_width: 0.014
1451	      pairs_100:
1452	        auroc: 0.757
1453	        delta: 0.066
1454	        ci_width: 0.009
1455	      pairs_200:
1456	        auroc: 0.761
1457	        delta: 0.07
1458	        ci_width: 0.006
1459	    elbow_point: 50
1460	    marginal_gain_50_to_100: 0.008
1461	    marginal_gain_100_to_200: 0.004
1462	    caclr_equivalent_pairs: 35
1463	  result_rationale: 'Linear projection 学习 affine transformation 将 target 语言 correctness
1464	    subspace
1465	
1466	    旋转对齐到 English。Correctness direction 是低维的 (实际是 1D for LR probe)，
1467	
1468	    因此旋转矩阵的自由度极低——50 pairs 已充分约束 (条件数稳定)。10 pairs 时 CI
1469	
1470	    宽 0.034 (不稳定)，50 pairs CI 收窄至 0.015。超过 50 pairs，marginal gain
1471	
1472	    从 +2.2pp/50pairs 骤降至 +0.8pp/50pairs 和 +0.4pp/100pairs。CaCLR (无 parallel
1473	
1474	    pairs 的 labels) 等效于 ~35-pair linear projection (AUROC 0.763 vs pairs_35
1475	
1476	    插值约 0.76)，表明 MMD distributional matching 实现了部分但非完全的子空间
1477	
1478	    对齐。50 pairs 的实用意义大：几乎所有 GlobalMMLU 语言都有 600+ parallel items，
1479	
1480	    随机选 50 对即可达到 plateau。
1481	
1482	    '
1483	  tables:
1484	  - name: 'Table 13: Linear Projection Sample Efficiency (Qwen3, L56)'
1485	    columns:
1486	    - Pairs
1487	    - AUROC_Avg
1488	    - Delta_vs_ZS
1489	    - Marginal_Gain
1490	    - CI_95_Width
1491	    rows:
1492	    - - 10
1493	      - 0.739
1494	      - 0.011
1495	      - —
1496	      - 0.034
1497	    - - 20
1498	      - 0.758
1499	      - 0.03
1500	      - 0.019
1501	      - 0.023
1502	    - - 50
1503	      - 0.79
1504	      - 0.062
1505	      - 0.032
1506	      - 0.015
1507	    - - 100
1508	      - 0.798
1509	      - 0.07
1510	      - 0.008
1511	      - 0.01
1512	    - - 200
1513	      - 0.802
1514	      - 0.074
1515	      - 0.004
1516	      - 0.007
1517	  figures_description:
1518	  - 'Fig 7: Sample efficiency curve (log-scale x, AUROC y). Clear elbow at 50. Horizontal
1519	    line = CaCLR (0.763), intersects curve at ~35 pairs.'
1520	  analysis: '50 pairs 是实用甜点。Linear projection 在 50 pairs 时超过 CaCLR (0.790 vs
1521	
1522	    0.763)，但需要 parallel pairs with correctness labels。两方法互补：CaCLR
1523	
1524	    for zero-label 场景，linear projection for minimal-data 场景。
1525	
1526	    '
1527	- name: Full-Scale Probing Control Tasks
1528	  plan_id: plan_013
1529	  description: Hewitt & Liang control tasks, 20 langs × 2 archs × all layers (扩展 MVP
1530	    English-only 结果)
1531	  expected_results:
1532	    selectivity_below_005_fraction: 0.1
1533	    low_sel_distribution:
1534	      early_layers_pct: 0.72
1535	      low_resource_pct: 0.68
1536	      overlap_early_AND_low: 0.54
1537	    qwen_selectivity_avg: 0.178
1538	    llama_selectivity_avg: 0.152
1539	    control_auroc_avg: 0.491
1540	    control_auroc_std: 0.012
1541	    control_auroc_max: 0.518
1542	    selectivity_grid_qwen:
1543	      early_HIGH: 0.045
1544	      early_MID: 0.036
1545	      early_LOW: 0.019
1546	      mid_HIGH: 0.142
1547	      mid_MID: 0.118
1548	      mid_LOW: 0.078
1549	      deep_HIGH: 0.261
1550	      deep_MID: 0.242
1551	      deep_LOW: 0.188
1552	    problem_zone_cells: 48
1553	    total_cells: 480
1554	    problem_zone_pct: 0.1
1555	    english_selectivity_deep_layers: 0.255
1556	    cross_lingual_selectivity_deep_layers_avg: 0.212
1557	    cross_lingual_selectivity_deep_layers_low_resource: 0.168
1558	  result_rationale: 'Control task AUROC 稳定在 ~0.49 (理论 0.50)，confirming permuted labels
1559	    不被
1560	
1561	    probe 学到——probing capacity 有限，不会 memorize random labels。10% 的 grid
1562	
1563	    cells 有 selectivity < 0.05，集中在 (early layers, LOW resource) 象限：
1564	
1565	    (1) Early layers (L0-L20 Qwen / L0-L12 Llama): correctness signal 尚未形成，
1566	
1567	    real probe 和 control probe 表现接近，selectivity ≈ 0；(2) Low-resource
1568	
1569	    languages: 较少的预训练数据 → correctness 编码更弱 → real probe 提升有限。
1570	
1571	    交叉：54% 的 low-selectivity cells 同时满足 early + low-resource。MVP 的
1572	
1573	    English-only plan_013 结果 (selectivity 集中在 L20-L27) 与 full-scale 一致，
1574	
1575	    但 cross-lingual extension 揭示了资源维度——英语深层 selectivity 0.255 vs
1576	
1577	    低资源深层 0.168。这本身是 methodological contribution：跨语言 probing 中
1578	
1579	    ~10% 的结果需谨慎解读。
1580	
1581	    '
1582	  tables:
1583	  - name: 'Table S5: Selectivity by Depth × Resource Tier (Qwen3)'
1584	    columns:
1585	    - Depth_Range
1586	    - HIGH_Resource
1587	    - MID_Resource
1588	    - LOW_Resource
1589	    rows:
1590	    - - 0-33% (early)
1591	      - 0.045
1592	      - 0.036
1593	      - 0.019
1594	    - - 33-67% (mid)
1595	      - 0.142
1596	      - 0.118
1597	      - 0.078
1598	    - - 67-100% (deep)
1599	      - 0.261
1600	      - 0.242
1601	      - 0.188
1602	  figures_description:
1603	  - 'Fig S4: Selectivity heatmap (y=layer, x=language sorted by resource). 左下角 (low
1604	    resource × early layer) 颜色最浅 (selectivity → 0).'
1605	  analysis: '10% capacity artifact rate 在 best tier [0.05, 0.15] 范围内。核心 probing
1606	
1607	    results (中深层 × 中高资源) selectivity > 0.10，genuine signal。Low-resource ×
1608	
1609	    early-layer zone 应在 paper 中标注为 "interpret with caution"。
1610	
1611	    '
1612	- name: Gemma 4 31B Dense — Third Architecture
1613	  plan_id: plan_008
1614	  description: 60层 Dense (FP16), 第三架构提供 dense vs MoE 对比
1615	  expected_results:
1616	    en_best_auroc: 0.821
1617	    en_best_layer: 48
1618	    zs_transfer_auroc_avg_20lang: 0.702
1619	    zs_transfer_success_rate: 0.9
1620	    zs_fail_langs:
1621	    - yo
1622	    - am
1623	    pareto_spearman_rho_global: -0.52
1624	    cka_pattern: gradual decline, onset deeper than Llama (no cliff)
1625	    cka_correctness_subspace_angle_avg: 13.1
1626	    caclr_delta_auroc_avg: 0.039
1627	  result_rationale: 'Dense 31B 没有 MoE routing，表征特化更均匀 (无 expert 分配的 language-specific
1628	
1629	    路径)，Pareto ρ=-0.52 介于 Qwen3 (ρ=-0.65, 强 MoE cliff) 和 Llama4 (ρ=-0.33,
1630	
1631	    弱 MoE) 之间。EN AUROC 0.821 反映 31B dense 的容量低于 235B 但高于 17B active。
1632	
1633	    CKA 渐降模式接近 Llama 但 onset 更深——dense model 在中间层保持更强的跨语言
1634	
1635	    共享 (无 expert routing 导致的早期分化)。Dense 架构的 Pareto 中等强度提供了
1636	
1637	    theory-consistent 的三点比较：cliff MoE (Qwen) > dense (Gemma) > gradual MoE
1638	
1639	    (Llama)。仅 yo/am 失败 (2/20)，success rate 0.90。CaCLR delta +3.9pp 低于
1640	
1641	    Qwen (+4.7pp) 但高于 Llama (+4.1pp)——dense 的初始 ZS transfer 已较好 (CKA
1642	
1643	    更高)，CaCLR 的 marginal room 稍小。
1644	
1645	    '
1646	  tables:
1647	  - name: 'Table 14: Three-Architecture Comparison'
1648	    columns:
1649	    - Architecture
1650	    - Type
1651	    - EN_AUROC
1652	    - ZS_Avg
1653	    - Pareto_rho
1654	    - CKA_Pattern
1655	    - CaCLR_Delta
1656	    rows:
1657	    - - Qwen3-235B
1658	      - MoE (Int4)
1659	      - 0.832
1660	      - 0.713
1661	      - -0.65
1662	      - Cliff at 68%
1663	      - 0.047
1664	    - - Gemma4-31B
1665	      - Dense (FP16)
1666	      - 0.821
1667	      - 0.702
1668	      - -0.52
1669	      - Gradual, deep onset
1670	      - 0.039
1671	    - - Llama4-Scout
1672	      - MoE (W4A16)
1673	      - 0.811
1674	      - 0.684
1675	      - -0.33
1676	      - Gradual, early onset
1677	      - 0.041
1678	  figures_description:
1679	  - 'Fig 8: Three-architecture Pareto overlay — Qwen (steep, clear frontier), Gemma
1680	    (moderate), Llama (flat, scattered). 三种斜率直观展示 architecture dependence.'
1681	  analysis: '第三架构填充了 dense vs MoE 对比。Pareto 强度排序 (Qwen > Gemma > Llama) 与
1682	
1683	    架构差异一致：MoE cliff 产生最强 tradeoff，dense 渐降产生中等 tradeoff，
1684	
1685	    无 cliff 的 MoE 最弱。Camera-ready 的 n=3 架构虽仍不足以做因果归因 (type,
1686	
1687	    scale, layers, training data 均不同)，但三点一致的模式 strengthens "architecture-
1688	
1689	    dependent tradeoff" 的 observational claim。
1690	
1691	    '
1692	- name: Extended Language Coverage (50+)
1693	  plan_id: plan_009
1694	  description: 扩展至 50+ 语言 (GlobalMMLU + Belebele full sets)
1695	  expected_results:
1696	    total_languages: 53
1697	    zs_success_rate: 0.83
1698	    n_success: 44
1699	    n_fail: 9
1700	    fail_langs:
1701	    - am
1702	    - my
1703	    - yo
1704	    - si
1705	    - lo
1706	    - km
1707	    - gu
1708	    - or
1709	    - ne
1710	    pareto_rho_qwen_global_53: -0.62
1711	    pareto_rho_llama_global_53: -0.31
1712	    resource_tier_gradient_r2: 0.71
1713	    new_findings:
1714	      dravidian_cluster: ta/ml/kn 形成 cluster, ZS AUROC 0.64-0.68, transfer 特征接近 MID
1715	        tier
1716	      austronesian_cluster: id/ms/tl transfer 异常好 (0.72-0.74)，因为与英语的表征对齐度高
1717	      uralic_outlier: fi/hu ZS AUROC 差异大 (fi 0.69 vs hu 0.65)，尽管同为 Uralic
1718	    caclr_delta_avg_53: 0.044
1719	    caclr_delta_new_langs_avg: 0.041
1720	  result_rationale: '扩展至 53 语言后，成功率从 ~90% (20 langs) 降至 83% (53 langs)，因为新增
1721	
1722	    语言多为 extreme low-resource (si, lo, km 等)。但 Pareto ρ 和主要 patterns
1723	
1724	    保持稳定 (Qwen ρ=-0.62 vs -0.65 at 20 langs)，slight reduction 因为新增的
1725	
1726	    低资源语言削弱了 global correlation。Resource tier gradient 在更大样本下更
1727	
1728	    robust (R²=0.71, up from ~0.60 at 20 langs)。Austronesian 语言 (id/ms/tl)
1729	
1730	    transfer 异常好，因为这些语言在大模型预训练中常被 grouped with English-heavy
1731	
1732	    corpora (code-switching, romanization)。CaCLR 增益在新增语言上 (+4.1pp) 与
1733	
1734	    原 20 语言 (+4.7pp) 相当，confirming method generalizability。
1735	
1736	    '
1737	  tables:
1738	  - name: 'Table S6: Extended Language Coverage Summary'
1739	    columns:
1740	    - Metric
1741	    - 20_Langs
1742	    - 53_Langs
1743	    rows:
1744	    - - ZS Success Rate
1745	      - 95% (Qwen)
1746	      - 83%
1747	    - - Pareto ρ Qwen
1748	      - -0.65
1749	      - -0.62
1750	    - - Pareto ρ Llama
1751	      - -0.33
1752	      - -0.31
1753	    - - Resource Gradient R²
1754	      - ~0.60
1755	      - 0.71
1756	    - - CaCLR Δ AUROC avg
1757	      - 0.047
1758	      - 0.044
1759	  figures_description:
1760	  - 'Fig S5: 53-language ZS success rate by resource tier. Clear gradient: HIGH ~98%,
1761	    MID ~90%, LOW ~65%.'
1762	  analysis: 'Camera-ready 扩展确认 core findings 跨 50+ 语言成立。9 种 fail 语言均为
1763	
1764	    extreme low-resource (预训练 tokens < 100M)，consistent with domain adaptation
1765	
1766	    theory 的 H-divergence 预测。Austronesian cluster 的高 transfer 是 interesting
1767	
1768	    secondary finding。'
1769	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "25caf90b-58a8-462f-b3a8-1f47df11e3bb",
  "isSidechain": false,
  "promptId": "29945050-684f-4c5e-9353-e8166e9d5912",
  "type": "user",
  "uuid": "a1f86289-e4fa-4abe-8bee-e969dfb297ca",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/best/review_context.yaml",
      "content": "narrative_guidance: 'CaCLR 是正面方法贡献——β > 0 的 MMD consistency loss 在 probe logits 空间成功\n\n  对齐 correctness subspace，使零标签跨语言校准成为可能。Pareto frontier 在两种\n\n  架构上均 robust：Qwen3-235B 呈强负相关 (ρ ≈ -0.65)，Llama 4 Scout 呈弱但一致\n\n  的负相关 (ρ ≈ -0.33)。CKA partial correlation 控制 depth 后仍显著 (r ≈ 0.42,\n\n  p < 0.01)，支撑 geometric analysis framing。四个 claims 均以强形式提出，论文\n\n  以 method + discovery 双重贡献投稿。\n\n  Headline: \"CaCLR enables zero-label cross-lingual calibration, reducing non-English\n\n  ECE by 22% vs temperature scaling across 20 languages on two architectures.\"\n\n  '\nimagined_experiments:\n- name: Qwen3-235B Full Pareto Frontier\n  plan_id: plan_001\n  description: 94层 MoE (INT4), 24 probed layers (每4层), 20语言, 4 transfer conditions\n    (CaCLR 在 plan_003)\n  expected_results:\n    en_best_auroc: 0.832\n    en_best_layer: 72\n    en_auroc_range:\n    - 0.548\n    - 0.832\n    en_best_ece_raw: 0.126\n    zs_transfer_auroc_avg_20lang: 0.713\n    zs_transfer_success_rate: 0.95\n    zs_fail_langs:\n    - am\n    pareto_spearman_rho_global: -0.65\n    pareto_spearman_rho_per_lang_range:\n    - -0.82\n    - -0.41\n    zs_auroc_by_tier:\n      HIGH_avg: 0.773\n      MID_avg: 0.719\n      LOW_avg: 0.635\n    zs_best_by_lang:\n      zh:\n        auroc: 0.79\n        best_layer: 56\n      es:\n        auroc: 0.78\n        best_layer: 60\n      fr:\n        auroc: 0.77\n        best_layer: 56\n      de:\n        auroc: 0.77\n        best_layer: 60\n      ja:\n        auroc: 0.75\n        best_layer: 52\n      pt:\n        auroc: 0.78\n        best_layer: 56\n      it:\n        auroc: 0.77\n        best_layer: 60\n      hi:\n        auroc: 0.73\n        best_layer: 48\n      ru:\n        auroc: 0.74\n        best_layer: 52\n      ko:\n        auroc: 0.73\n        best_layer: 52\n      tr:\n        auroc: 0.7\n        best_layer: 44\n      vi:\n        auroc: 0.71\n        best_layer: 48\n      ar:\n        auroc: 0.72\n        best_layer: 52\n      th:\n        auroc: 0.7\n        best_layer: 44\n      sw:\n        auroc: 0.65\n        best_layer: 40\n      bn:\n        auroc: 0.66\n        best_layer: 44\n      yo:\n        auroc: 0.61\n        best_layer: 36\n      te:\n        auroc: 0.66\n        best_layer: 44\n      my:\n        auroc: 0.63\n        best_layer: 36\n      am:\n        auroc: 0.598\n        best_layer: 36\n    depth_transfer_snapshot:\n      en_at_L72: 0.832\n      zs_avg_at_L72: 0.672\n      en_at_L56: 0.812\n      zs_avg_at_L56: 0.728\n      en_at_L40: 0.762\n      zs_avg_at_L40: 0.706\n    mean_shift_delta_auroc: 0.0\n    linear_proj_50_delta_auroc_avg: 0.062\n    fewshot_25_auroc_avg: 0.738\n    fewshot_100_auroc_avg: 0.768\n    bootstrap_ci_width_auroc: 0.018\n  result_rationale: '235B MoE 拥有远比 7B 更结构化的内部表征。MVP Qwen2.5-7B EN best AUROC = 0.754;\n\n    235B 的 correctness direction 在中高层 (L48-L72) 线性可分度大幅提升至 0.83，\n\n    与 probing 文献中 \"larger model → more linearly accessible features\" 的规律一致。\n\n    更大模型的多语言预训练数据量级增加约 5-10x，跨语言对齐更强，zero-shot transfer\n\n    avg 从 MVP ~0.65 提升至 ~0.71。94 层结构提供精细 depth 分辨率：EN-optimal L72\n\n    (77% depth) 与 transfer-optimal zone L52-56 (55-60% depth) 间有 ~16 层间距，\n\n    产生清晰的强负相关 ρ ≈ -0.65。低资源语言的 ρ 更负 (sw -0.79, yo -0.82)，\n\n    因为这些语言在深层的表征特化最剧烈——模型的 language-specific expert routing\n\n    在深层对高资源语言保持跨语言共享，但对低资源语言已切换至 language-specific pathway。\n\n    Mean-shift AUROC delta 严格为零 (数学证明: StandardScaler + LR → 常数偏移 → rank\n\n    不变 → AUROC 不变)。仅 am (Amharic) 以 0.598 未达 0.60 阈值，因为 Qwen3 的\n\n    Amharic 预训练数据极少。\n\n    '\n  tables:\n  - name: 'Table 1: Qwen3-235B Pareto Frontier — Per-Language Summary'\n    columns:\n    - Language\n    - Family\n    - Resource\n    - Best_ZS_AUROC\n    - Best_ZS_Layer\n    - EN_AUROC_at_Same_Layer\n    - Spearman_rho\n    - rho_p\n    representative_rows:\n    - - zh\n      - Sinitic\n      - HIGH\n      - 0.79\n      - L56\n      - 0.812\n      - -0.58\n      - 0.003\n    - - es\n      - Romance\n      - HIGH\n      - 0.78\n      - L60\n      - 0.821\n      - -0.53\n      - 0.008\n    - - ja\n      - Japonic\n      - HIGH\n      - 0.75\n      - L52\n      - 0.802\n      - -0.62\n      - 0.001\n    - - hi\n      - Indo-Aryan\n      - MID\n      - 0.73\n      - L48\n      - 0.789\n      - -0.67\n      - <0.001\n    - - ko\n      - Koreanic\n      - MID\n      - 0.73\n      - L52\n      - 0.802\n      - -0.61\n      - 0.002\n    - - ar\n      - Semitic\n      - MID\n      - 0.72\n      - L52\n      - 0.802\n      - -0.59\n      - 0.003\n    - - sw\n      - Bantu\n      - LOW\n      - 0.65\n      - L40\n      - 0.762\n      - -0.79\n      - <0.001\n    - - yo\n      - Volta-Niger\n      - LOW\n      - 0.61\n      - L36\n      - 0.721\n      - -0.82\n      - <0.001\n    - - am\n      - Ethiosemitic\n      - LOW\n      - 0.598\n      - L36\n      - 0.721\n      - -0.81\n      - <0.001\n  - name: 'Table 2: Transfer Conditions Comparison (Qwen3-235B, L56 Pareto Zone)'\n    columns:\n    - Condition\n    - AUROC_Avg_20L\n    - AUROC_HIGH\n    - AUROC_MID\n    - AUROC_LOW\n    - ECE_Avg\n    rows:\n    - - Zero-shot\n      - 0.728\n      - 0.773\n      - 0.726\n      - 0.648\n      - 0.165\n    - - Mean-shift\n      - 0.728\n      - 0.773\n      - 0.726\n      - 0.648\n      - 0.168\n    - - Linear_proj_50\n      - 0.79\n      - 0.821\n      - 0.789\n      - 0.728\n      - 0.139\n    - - Few-shot_25\n      - 0.745\n      - 0.789\n      - 0.742\n      - 0.668\n      - 0.152\n    - - Few-shot_100\n      - 0.774\n      - 0.811\n      - 0.773\n      - 0.702\n      - 0.136\n  figures_description:\n  - 'Fig 1a: Heatmap (y=24 layers, x=20 langs sorted by resource tier). Color = ZS\n    AUROC. 深层左侧 (高资源) 保持暖色，深层右侧 (低资源) 转冷，显示 resource-dependent depth degradation.'\n  - 'Fig 1b: Pareto scatter — x=EN AUROC, y=avg ZS transfer AUROC (each point = one\n    layer, color = normalized depth). 清晰负斜率 ρ=-0.65, 右下角 (深层) 聚集.'\n  - 'Fig 1c: Per-language Spearman ρ bar chart (grouped by resource tier). 低资源 bars\n    更长 (更负).'\n  analysis: 'Qwen3-235B 呈现教科书级 Pareto frontier。关键发现：(1) ρ=-0.65 远强于 MVP\n\n    7B 的约 -0.4，confirming 更大模型 → 更 structured representations → 更清晰\n\n    tradeoff；(2) transfer-optimal zone 在 40-60% depth (L36-L56)，EN-optimal 在\n\n    77% (L72)，gap = 16 层；(3) resource tier gradient: HIGH 0.77 > MID 0.72 > LOW\n\n    0.64，三级分明；(4) 19/20 languages transfer 成功，仅 am 失败。Linear proj\n\n    (50 pairs) 是最强迁移方法 (+6.2pp over ZS)，few-shot 100 紧随 (+4.6pp)。\n\n    '\n- name: Llama 4 Scout Full Pareto Frontier\n  plan_id: plan_002\n  description: 48层 MoE (W4A16), 12 probed layers, 20语言, 4 transfer conditions\n  expected_results:\n    en_best_auroc: 0.811\n    en_best_layer: 40\n    en_auroc_range:\n    - 0.574\n    - 0.811\n    en_best_ece_raw: 0.139\n    zs_transfer_auroc_avg_20lang: 0.684\n    zs_transfer_success_rate: 0.85\n    zs_fail_langs:\n    - yo\n    - my\n    - am\n    pareto_spearman_rho_global: -0.33\n    pareto_spearman_rho_per_lang_range:\n    - -0.68\n    - 0.18\n    zs_auroc_by_tier:\n      HIGH_avg: 0.743\n      MID_avg: 0.694\n      LOW_avg: 0.602\n    zs_best_by_lang:\n      zh:\n        auroc: 0.76\n        best_layer: 36\n      es:\n        auroc: 0.75\n        best_layer: 36\n      fr:\n        auroc: 0.74\n        best_layer: 32\n      de:\n        auroc: 0.74\n        best_layer: 36\n      ja:\n        auroc: 0.72\n        best_layer: 32\n      pt:\n        auroc: 0.75\n        best_layer: 36\n      it:\n        auroc: 0.74\n        best_layer: 36\n      hi:\n        auroc: 0.7\n        best_layer: 36\n      ru:\n        auroc: 0.72\n        best_layer: 40\n      ko:\n        auroc: 0.71\n        best_layer: 40\n      tr:\n        auroc: 0.67\n        best_layer: 32\n      vi:\n        auroc: 0.69\n        best_layer: 32\n      ar:\n        auroc: 0.7\n        best_layer: 40\n      th:\n        auroc: 0.67\n        best_layer: 28\n      sw:\n        auroc: 0.62\n        best_layer: 28\n      bn:\n        auroc: 0.63\n        best_layer: 28\n      yo:\n        auroc: 0.57\n        best_layer: 24\n      te:\n        auroc: 0.64\n        best_layer: 28\n      my:\n        auroc: 0.58\n        best_layer: 24\n      am:\n        auroc: 0.57\n        best_layer: 24\n    depth_transfer_snapshot:\n      en_at_L40: 0.811\n      zs_avg_at_L40: 0.654\n      en_at_L32: 0.781\n      zs_avg_at_L32: 0.691\n      en_at_L24: 0.732\n      zs_avg_at_L24: 0.682\n    langs_with_positive_depth_rho:\n    - ru\n    - ko\n    - ar\n    mean_shift_delta_auroc: 0.0\n    linear_proj_50_delta_auroc_avg: 0.058\n    fewshot_25_auroc_avg: 0.706\n    fewshot_100_auroc_avg: 0.741\n  result_rationale: 'Llama 4 Scout (17B active × 16 experts, ~109B total) 的 EN AUROC\n    达到 0.811，\n\n    低于 Qwen3-235B 但显著高于 MVP Llama-3.1-8B (0.728)。Pareto frontier 呈弱\n\n    负相关 ρ ≈ -0.33，延续 MVP 中 Llama 架构的模式：部分语言 (ru, ko, ar) 随\n\n    depth 增加迁移不退化甚至略微改善 (ρ > 0)，而 sw/yo/am 退化严重 (ρ < -0.60)。\n\n    这种异质性源于 Llama 4 的 16-expert MoE routing：对 ru/ko/ar 等中高资源语言，\n\n    深层 expert routing 倾向于重用与 English 共享的 expert；对低资源语言则分配到\n\n    specialized expert，导致表征分离。三种低资源语言 (yo 0.57, my 0.58, am 0.57)\n\n    未通过 0.60 阈值，success rate 17/20 = 0.85 达到 best tier 下限。48 层仅\n\n    12 probed layers，depth 分辨率低于 Qwen3 (24 layers)，ρ 估计的统计功效较低\n\n    (n=12 vs n=24)。\n\n    '\n  tables:\n  - name: 'Table 3: Llama 4 Scout Pareto Frontier — Per-Language Summary'\n    columns:\n    - Language\n    - Family\n    - Resource\n    - Best_ZS_AUROC\n    - Best_ZS_Layer\n    - Spearman_rho\n    - rho_p\n    representative_rows:\n    - - zh\n      - Sinitic\n      - HIGH\n      - 0.76\n      - L36\n      - -0.45\n      - 0.14\n    - - es\n      - Romance\n      - HIGH\n      - 0.75\n      - L36\n      - -0.41\n      - 0.18\n    - - ru\n      - Slavic\n      - MID\n      - 0.72\n      - L40\n      - 0.05\n      - 0.88\n    - - ko\n      - Koreanic\n      - MID\n      - 0.71\n      - L40\n      - 0.18\n      - 0.57\n    - - ar\n      - Semitic\n      - MID\n      - 0.7\n      - L40\n      - -0.12\n      - 0.71\n    - - sw\n      - Bantu\n      - LOW\n      - 0.62\n      - L28\n      - -0.62\n      - 0.03\n    - - yo\n      - Volta-Niger\n      - LOW\n      - 0.57\n      - L24\n      - -0.68\n      - 0.02\n    - - am\n      - Ethiosemitic\n      - LOW\n      - 0.57\n      - L24\n      - -0.65\n      - 0.02\n  figures_description:\n  - 'Fig 2a: Pareto scatter (同 Fig 1b 格式) — 扁平斜率 ρ=-0.33, scatter 更大. ru/ko 偏离主趋势\n    (正方向).'\n  - 'Fig 2b: Per-language ρ comparison — Qwen3 vs Llama4 并排 bar chart. Qwen3 全负; Llama4\n    有 3 语言正值.'\n  - 'Fig 2c: Language-specific depth trajectory — 选 ru (上升), zh (平), sw (下降) 对比 Llama4\n    的异质性.'\n  analysis: 'Llama 4 Scout 的 Pareto 显著弱于 Qwen3-235B，core finding: architecture\n\n    determines tradeoff shape。ρ_Qwen=-0.65 vs ρ_Llama=-0.33, 且 Llama 呈现\n\n    language-specific 异质性 (3 种语言 ρ > 0)。这不是 Pareto 不存在——global ρ\n\n    仍为负——而是 tradeoff 在不同语言上表现不同。论文中框架为 \"strong vs weak\n\n    Pareto\" 的架构对比。\n\n    '\n- name: CaCLR Full Evaluation\n  plan_id: plan_003\n  description: L_CaCLR = L_BCE + α·L_SB-ECE + β·L_MMD, 两种架构×20语言完整评估\n  expected_results:\n    best_alpha: 1.0\n    best_beta: 0.1\n    alpha_sweep:\n      0.01:\n        auroc: 0.741\n        ece: 0.148\n      0.1:\n        auroc: 0.749\n        ece: 0.138\n      1.0:\n        auroc: 0.763\n        ece: 0.121\n      10.0:\n        auroc: 0.752\n        ece: 0.128\n    beta_sweep:\n      0.0:\n        auroc: 0.724\n        ece: 0.148\n      0.001:\n        auroc: 0.728\n        ece: 0.145\n      0.01:\n        auroc: 0.738\n        ece: 0.137\n      0.1:\n        auroc: 0.763\n        ece: 0.121\n      1.0:\n        auroc: 0.731\n        ece: 0.141\n    qwen_L56_pareto_zone:\n      caclr_auroc_avg: 0.763\n      zeroshot_auroc_avg: 0.728\n      delta_auroc: 0.035\n      caclr_ece_avg: 0.121\n      tempscaling_ece_avg: 0.155\n      delta_ece_vs_tempscaling: -0.034\n    qwen_L72_en_optimal:\n      caclr_auroc_avg: 0.728\n      zeroshot_auroc_avg: 0.672\n      delta_auroc: 0.056\n      caclr_ece_avg: 0.132\n      tempscaling_ece_avg: 0.171\n      delta_ece_vs_tempscaling: -0.039\n    qwen_oracle_per_lang:\n      caclr_auroc_avg: 0.76\n      zeroshot_auroc_avg: 0.713\n      delta_auroc: 0.047\n    llama_L32_pareto_zone:\n      caclr_auroc_avg: 0.732\n      zeroshot_auroc_avg: 0.691\n      delta_auroc: 0.041\n      caclr_ece_avg: 0.131\n      tempscaling_ece_avg: 0.163\n      delta_ece_vs_tempscaling: -0.032\n    llama_L40_en_optimal:\n      caclr_auroc_avg: 0.697\n      zeroshot_auroc_avg: 0.654\n      delta_auroc: 0.043\n      caclr_ece_avg: 0.142\n      tempscaling_ece_avg: 0.176\n      delta_ece_vs_tempscaling: -0.034\n    ablation:\n      bce_only:\n        auroc: 0.728\n        ece: 0.165\n      bce_sbece:\n        auroc: 0.724\n        ece: 0.148\n      bce_mmd:\n        auroc: 0.751\n        ece: 0.136\n      bce_sbece_mmd:\n        auroc: 0.763\n        ece: 0.121\n    beta_vs_zero_paired_permutation_p: 0.003\n    beta_vs_zero_cohens_d: 0.52\n    beta_vs_zero_bootstrap_ci:\n    - 0.024\n    - 0.058\n    caclr_delta_by_tier:\n      HIGH: 0.031\n      MID: 0.048\n      LOW: 0.068\n    pareto_rho_without_caclr: -0.65\n    pareto_rho_with_caclr: -0.51\n    pareto_shift_interpretation: CaCLR 减弱 Pareto tradeoff (rho 从 -0.65 到 -0.51), 因为深层迁移退化被部分修复\n    mmd_kernel: Gaussian RBF, bandwidth=median heuristic\n    optimizer: Adam, lr=1e-3, cosine decay to 1e-5\n    epochs: 50\n    early_stopping: patience=10, monitor val BCE loss\n    initialization: warm-start from standard LR solution\n    batch_size: 256\n    mmd_items: same items as BCE (probe_train portion)\n    parallel_set_size_per_lang_avg: 630\n    parallel_set_size_per_lang_min: 580\n    translation_quality_note: am/yo/my translations spot-checked, ~8% semantic drift\n      vs high-resource\n  result_rationale: 'Best tier 核心假设：\"MMD on probe logits 成功对齐 correctness subspace\n    cross-\n\n    lingually\"。为何成立：(1) 235B 模型的 correctness direction 占据低维语言无关\n\n    子空间 (CKA 分析支持)，因此 1D probe logit 的分布差异主要反映 subspace rotation\n\n    而非 intrinsic signal difference；MMD 通过匹配 logit 分布有效纠正这个 rotation。\n\n    (2) β=0.1 是 sweet spot——足以施加对齐压力 (MMD loss ~0.3 量级) 但不 overwhelm\n\n    BCE loss (初始 ~0.65 量级)；β=1.0 过大导致 MMD dominate，probe 为匹配分布而\n\n    牺牲判别力。(3) SB-ECE 单独贡献有限 (+0.006 AUROC)，但与 MMD 叠加有协同：\n\n    SB-ECE 改善 probability calibration 后，MMD 在更好校准的 logit 空间上匹配更\n\n    有效。(4) 低资源语言获益最大 (+0.068)，因为 zero-shot distribution gap 最大，\n\n    MMD 的边际对齐收益最高——与 Ben-David et al. H-divergence 理论一致。(5) 在\n\n    EN-optimal 深层 L72，CaCLR 增益更大 (+0.056 > +0.035)，因为深层迁移退化更\n\n    严重，recovery space 更大——直接证明 \"CaCLR shifts the Pareto frontier\"。\n\n    统计显著性: paired permutation test p=0.003, Cohen''s d=0.52 (medium effect),\n\n    bootstrap 95% CI [0.024, 0.058] 不含零。\n\n    '\n  tables:\n  - name: 'Table 4: CaCLR vs All Baselines (Fixed Layer, Pareto Zone)'\n    columns:\n    - Method\n    - Qwen3_AUROC\n    - Qwen3_ECE\n    - Llama4_AUROC\n    - Llama4_ECE\n    - Labels_Required\n    rows:\n    - - Zero-shot\n      - 0.728\n      - 0.165\n      - 0.691\n      - 0.179\n      - EN only\n    - - Mean-shift\n      - 0.728\n      - 0.168\n      - 0.691\n      - 0.183\n      - EN only\n    - - Temp scaling\n      - 0.728\n      - 0.155\n      - 0.691\n      - 0.163\n      - EN only\n    - - CaCLR (α=1 β=0.1)\n      - 0.763\n      - 0.121\n      - 0.732\n      - 0.131\n      - EN only + parallel inputs\n    - - Linear proj (50)\n      - 0.79\n      - 0.139\n      - 0.749\n      - 0.146\n      - 50 parallel pairs\n    - - Few-shot (25)\n      - 0.745\n      - 0.152\n      - 0.712\n      - 0.159\n      - 25 target labels\n    - - Few-shot (100)\n      - 0.774\n      - 0.136\n      - 0.745\n      - 0.142\n      - 100 target labels\n  - name: 'Table 5: Component Ablation (Qwen3-235B, L56, Avg 20 Langs)'\n    columns:\n    - Components\n    - AUROC\n    - ECE\n    - Delta_AUROC_vs_ZS\n    rows:\n    - - BCE only (= zero-shot)\n      - 0.728\n      - 0.165\n      - —\n    - - BCE + SB-ECE\n      - 0.724\n      - 0.148\n      - -0.004\n    - - BCE + MMD\n      - 0.751\n      - 0.136\n      - 0.023\n    - - BCE + SB-ECE + MMD\n      - 0.763\n      - 0.121\n      - 0.035\n  - name: 'Table 6: β Sensitivity (α=1.0 fixed, Qwen3 L56)'\n    columns:\n    - beta\n    - AUROC\n    - ECE\n    - Delta_vs_beta0\n    rows:\n    - - 0.0\n      - 0.724\n      - 0.148\n      - —\n    - - 0.001\n      - 0.728\n      - 0.145\n      - 0.004\n    - - 0.01\n      - 0.738\n      - 0.137\n      - 0.014\n    - - 0.1\n      - 0.763\n      - 0.121\n      - 0.039\n    - - 1.0\n      - 0.731\n      - 0.141\n      - 0.007\n  figures_description:\n  - 'Fig 3a: α-β grid heatmap (AUROC as color). Peak region around (α=1.0, β=0.1),\n    smooth gradient.'\n  - 'Fig 3b: CaCLR Pareto shift — Qwen3 scatter overlay: gray=zero-shot per-layer,\n    red=CaCLR per-layer. Red points shifted up-right, ρ flattens from -0.65 to -0.51.'\n  - 'Fig 3c: Per-language CaCLR gain (Δ AUROC), grouped by resource tier. LOW tier\n    bars tallest.'\n  - 'Fig 3d: β sweep curve (log scale x, AUROC y). Inverted-U, peak at β=0.1.'\n  analysis: 'β > 0 统计显著地改善跨语言迁移 (p=0.003, d=0.52)。CaCLR 的核心价值：完全不需要\n\n    target-language correctness labels，仅需 parallel inputs (已通过 GlobalMMLU\n\n    翻译存在)。CaCLR 未超过 linear projection (50 pairs): 0.763 vs 0.790，但\n\n    CaCLR 无需 paired correctness labels。Two methods 互补：CaCLR 适用于无 parallel\n\n    pairs 的场景，linear projection 在有少量 parallel data 时更优。CaCLR 在深层\n\n    (EN-optimal) 增益更大 (+0.056) 证明它 shifts Pareto frontier，不只是 uniform\n\n    improvement。ECE reduction 22% vs temp scaling 构成论文 headline。\n\n    '\n- name: Difficulty-Controlled Decomposition\n  plan_id: plan_004\n  description: IRT difficulty probe → project out → retrain → transfer delta. 10 langs\n    × 8 layers × 2 models\n  expected_results:\n    difficulty_probe_r2_avg: 0.61\n    difficulty_probe_r2_range:\n    - 0.43\n    - 0.76\n    difficulty_probe_r2_by_lang:\n      zh: 0.72\n      es: 0.76\n      de: 0.68\n      fr: 0.71\n      hi: 0.58\n      ru: 0.65\n      ko: 0.63\n      tr: 0.53\n      sw: 0.43\n      bn: 0.47\n    avg_transfer_delta_after_projection: 0.035\n    delta_by_lang_category:\n      capability_dominated:\n        langs:\n        - zh\n        - es\n        - fr\n        - de\n        - ru\n        - ko\n        delta: 0.042\n        ci:\n        - 0.031\n        - 0.054\n      difficulty_dominated:\n        langs:\n        - hi\n        - tr\n        - sw\n        - bn\n        delta: -0.018\n        ci:\n        - -0.029\n        - -0.007\n    random_projection_delta_avg: -0.003\n    random_projection_delta_std: 0.008\n    random_projection_delta_ci:\n    - -0.011\n    - 0.005\n    delta_by_depth:\n      20%: 0.012\n      35%: 0.021\n      50%: 0.035\n      65%: 0.043\n      80%: 0.051\n      90%: 0.048\n    qwen_avg_delta: 0.038\n    llama_avg_delta: 0.031\n    predicted_vs_actual_alignment_strategy_accuracy: 0.82\n  result_rationale: 'Correctness signal 是 difficulty (跨语言共享——哪些题目本身更难) 和 capability\n\n    (语言特异性——模型在该语言上的推理能力) 的纠缠。对于 capability-dominated 语言\n\n    (高资源, 模型具备强推理)，difficulty 是共享但无用的噪声维度：projecting out\n\n    移除了对迁移有害的 confound，暴露纯粹的 capability signal，transfer 改善\n\n    +4.2pp。对于 difficulty-dominated 语言 (低资源, 模型 capability 弱)，difficulty\n\n    本身是 correctness 的主要来源 (模型答对题目主要靠题目简单，而非语言能力)——\n\n    移除它丢失了唯一可迁移的信号，transfer 下降 -1.8pp。深层 delta 更大 (80%\n\n    depth: +5.1pp vs 20%: +1.2pp)，因为 capability 特化在深层更强，difficulty\n\n    confound 的 relative 权重在深层更大。Random direction control 的 delta ≈ 0\n\n    排除了纯降维的 artifact。IRT difficulty probe R² 呈 resource gradient (zh 0.72\n\n    > sw 0.43)，因为 IRT difficulty scores 基于高资源语言的人类答题数据，低资源\n\n    语言的 difficulty 编码较弱。Prescriptive accuracy 82% 表明 decomposition\n\n    能正确预测 8/10 语言应该用哪种 alignment strategy。\n\n    '\n  tables:\n  - name: 'Table 7: Difficulty Decomposition Effect by Language Category'\n    columns:\n    - Category\n    - Languages\n    - N_langs\n    - Delta_AUROC\n    - CI_95\n    - Random_Control\n    rows:\n    - - Capability-dominated\n      - zh/es/fr/de/ru/ko\n      - 6\n      - 0.042\n      - '[0.031, 0.054]'\n      - -0.002\n    - - Difficulty-dominated\n      - hi/tr/sw/bn\n      - 4\n      - -0.018\n      - '[-0.029, -0.007]'\n      - -0.004\n    - - Overall\n      - all 10\n      - 10\n      - 0.035\n      - '[0.021, 0.049]'\n      - -0.003\n  - name: 'Table 8: Depth × Decomposition Interaction'\n    columns:\n    - Depth_Pct\n    - EN_Probe_AUROC\n    - ZS_Delta_After_Proj\n    - ZS_Delta_Capability_Only\n    - ZS_Delta_Difficulty_Only\n    rows:\n    - - 20%\n      - 0.65\n      - 0.012\n      - 0.018\n      - -0.008\n    - - 50%\n      - 0.78\n      - 0.035\n      - 0.042\n      - -0.016\n    - - 80%\n      - 0.82\n      - 0.051\n      - 0.061\n      - -0.023\n  figures_description:\n  - 'Fig 4a: Scatter — x = baseline ZS transfer AUROC (proxy for capability), y =\n    Δ AUROC after difficulty projection. 正相关: capability 越高, projection 越有益. 虚线 =\n    decision boundary (Δ=0).'\n  - 'Fig 4b: Depth × delta line plot — separate lines for capability-dominated (上升)\n    vs difficulty-dominated (下降) 语言.'\n  analysis: 'Decomposition 成功分离 difficulty/capability，fulfilling Claim 2。Prescriptive\n\n    value: 对于 capability-dominated 语言 (baseline ZS > ~0.70)，projecting out\n\n    difficulty 是 free lunch (+4.2pp)。对于 difficulty-dominated 语言 (baseline ZS\n\n    < ~0.65)，应保留 difficulty 信号。82% prediction accuracy 表明这个规则可\n\n    自动化为 per-language strategy selector。\n\n    '\n- name: Cross-Lingual Orthogonality\n  plan_id: plan_005\n  description: Correctness vs verbalized confidence direction cosine similarity, 20\n    langs × 2 archs\n  expected_results:\n    cosine_range:\n    - 0.012\n    - 0.058\n    cosine_mean: 0.032\n    cosine_std: 0.013\n    cosine_by_tier:\n      HIGH: 0.027\n      MID: 0.033\n      LOW: 0.04\n    cosine_by_arch:\n      Qwen3: 0.029\n      Llama4: 0.035\n    cosine_extremes:\n      min:\n        lang: es\n        arch: Qwen3\n        value: 0.012\n      max:\n        lang: am\n        arch: Llama4\n        value: 0.058\n    cosine_per_lang:\n      en:\n        qwen: 0.023\n        llama: 0.03\n      zh:\n        qwen: 0.021\n        llama: 0.028\n      es:\n        qwen: 0.012\n        llama: 0.024\n      hi:\n        qwen: 0.032\n        llama: 0.039\n      sw:\n        qwen: 0.042\n        llama: 0.049\n      am:\n        qwen: 0.048\n        llama: 0.058\n    permutation_test_vs_random_p: <0.001\n    cosine_vs_resource_rho: 0.34\n    cosine_vs_resource_p: 0.042\n  result_rationale: 'Correctness 和 verbalized confidence 的正交性 (cosine < 0.06) 是 transformer\n\n    架构的内在特征：模型学会了在独立的表征子空间中编码 \"我是否答对了\" (correctness)\n\n    和 \"我认为我有多确定\" (confidence)。这不是 English-specific 现象。正交性在\n\n    所有 20 种语言上持续成立，因为两个方向都由模型的参数化决定，不由输入语言决定。\n\n    低资源语言的 cosine 略高 (0.040 vs 0.027) 有两个原因：(1) confidence probe\n\n    在低资源语言上的 SNR 更低，噪声使 cosine 估计偏离零；(2) 低资源语言的表征\n\n    空间利用率低，两个方向在低维子空间中更容易有 spurious overlap。但即使最高\n\n    的 am=0.058 仍远低于表示有意义相关性的阈值 (~0.2)。\n\n    '\n  tables:\n  - name: 'Table 9: Correctness-Confidence Orthogonality Across Languages'\n    columns:\n    - Language\n    - Resource\n    - Qwen3_Cosine\n    - Llama4_Cosine\n    - Average\n    representative_rows:\n    - - en\n      - —\n      - 0.023\n      - 0.03\n      - 0.027\n    - - zh\n      - HIGH\n      - 0.021\n      - 0.028\n      - 0.025\n    - - es\n      - HIGH\n      - 0.012\n      - 0.024\n      - 0.018\n    - - hi\n      - MID\n      - 0.032\n      - 0.039\n      - 0.036\n    - - ko\n      - MID\n      - 0.028\n      - 0.035\n      - 0.032\n    - - sw\n      - LOW\n      - 0.042\n      - 0.049\n      - 0.046\n    - - am\n      - LOW\n      - 0.048\n      - 0.058\n      - 0.053\n  figures_description:\n  - 'Fig 5: Cosine similarity dot plot — 每个点 = 一种语言, x = Qwen3 cosine, y = Llama4\n    cosine. 所有点聚集在 [0, 0.06] × [0, 0.06] 区域, 远离 identity line. 虚线 = Miao & Ungar English\n    reference (0.04).'\n  analysis: 'Claim 4 完全成立。Output-based calibration 的结构性限制是跨语言普遍的——\n\n    所有 40 个 (language, architecture) 组合的 cosine < 0.06。Resource tier 与\n\n    cosine 弱正相关 (ρ=0.34, p=0.042)，但 effect size 极小 (range 仅 0.013)。\n\n    这进一步 motivate probe-based calibration：output 层面的信息理论限制不随\n\n    语言变化。\n\n    '\n- name: Probe Complexity Comparison\n  plan_id: plan_006\n  description: 'Logistic regression vs 2-layer MLP: EN accuracy 和 cross-lingual transfer\n    对比'\n  expected_results:\n    lr_en_best_auroc: 0.832\n    mlp_en_best_auroc: 0.851\n    mlp_en_advantage: 0.019\n    lr_zs_auroc_avg: 0.713\n    mlp_zs_auroc_avg: 0.685\n    lr_zs_advantage: 0.028\n    lr_relative_degradation: 0.143\n    mlp_relative_degradation: 0.195\n    mlp_excess_degradation: 0.052\n    lr_zs_low: 0.635\n    mlp_zs_low: 0.581\n    lr_vs_mlp_gap_low: 0.054\n    lr_zs_high: 0.773\n    mlp_zs_high: 0.752\n    lr_vs_mlp_gap_high: 0.021\n    lr_ece_avg: 0.165\n    mlp_ece_avg: 0.184\n  result_rationale: 'MLP 在 English 上略优 (+1.9pp) 是因为 correctness signal 含有弱非线性成分——\n\n    某些层的 correctness 编码涉及特征交互。但 MLP 同时学到了 English-specific 的\n\n    非线性 pattern (e.g. English-specific token position interactions)，这些 pattern\n\n    在目标语言中不存在，导致 transfer 时引入负迁移。Linear probe 的 inductive bias\n\n    恰好匹配 correctness direction 的跨语言结构：线性投影只能捕获方向性信息，\n\n    而方向性信息正是跨语言共享的 (CKA 子空间分析支持)。差距在低资源语言最大\n\n    (LR +5.4pp vs MLP)，因为低资源表征的线性结构相对于英语更保守 (低维对齐\n\n    更强)，而 MLP 学到的非线性 feature 在低资源语境下完全失效。\n\n    '\n  tables:\n  - name: 'Table S3: Probe Complexity × Transfer'\n    columns:\n    - Metric\n    - LR\n    - MLP_2layer\n    - Delta\n    rows:\n    - - EN Best AUROC\n      - 0.832\n      - 0.851\n      - 0.019\n    - - ZS Transfer Avg 20L\n      - 0.713\n      - 0.685\n      - -0.028\n    - - Relative Degradation\n      - 14.3%\n      - 19.5%\n      - +5.2pp\n    - - ZS Low-Resource Avg\n      - 0.635\n      - 0.581\n      - -0.054\n    - - ECE Avg\n      - 0.165\n      - 0.184\n      - 0.019\n  figures_description:\n  - 'Fig S1: Per-language transfer AUROC comparison (LR vs MLP), connected dots. MLP\n    consistently below LR, gap widens rightward (low-resource).'\n  analysis: 'Linear probe 是跨语言 transfer 的正确选择。MLP 的 +1.9pp English 优势远不足以\n\n    补偿 -2.8pp transfer 劣势。论文中以此证明 LR 作为默认 probe 的合理性。\n\n    '\n- name: Additional Benchmarks (Belebele + MMLU-ProX)\n  plan_id: plan_007\n  description: 最优 probes + CaCLR 在 Belebele 和 MMLU-ProX 上的泛化验证\n  expected_results:\n    belebele_qwen_en_auroc: 0.814\n    belebele_qwen_zs_avg: 0.698\n    belebele_qwen_caclr_avg: 0.741\n    belebele_qwen_pareto_rho: -0.61\n    belebele_llama_en_auroc: 0.793\n    belebele_llama_zs_avg: 0.671\n    belebele_llama_caclr_avg: 0.712\n    mmlupx_qwen_en_auroc: 0.839\n    mmlupx_qwen_zs_avg: 0.721\n    mmlupx_qwen_caclr_avg: 0.767\n    mmlupx_qwen_pareto_rho: -0.67\n    mmlupx_llama_en_auroc: 0.818\n    mmlupx_llama_zs_avg: 0.694\n    mmlupx_llama_caclr_avg: 0.738\n    per_lang_rank_corr_gmmlu_belebele: 0.89\n    per_lang_rank_corr_gmmlu_mmlupx: 0.93\n  result_rationale: 'Belebele 是 reading comprehension，与 GlobalMMLU (knowledge QA)\n    的 domain 不同。\n\n    Correctness direction 有轻微 domain dependency：probe 在 knowledge-heavy items\n\n    上学到的 correctness signal 不完全迁移到 comprehension tasks，EN AUROC 略降\n\n    (0.814 vs 0.832)。但 Pareto 结构高度一致 (ρ=-0.61 vs -0.65)，因为 depth-\n\n    transferability tradeoff 是架构特征而非 task 特征。MMLU-ProX 与 GlobalMMLU\n\n    domain overlap 大 (同属 knowledge QA)，结果最相似。Per-language ranking 跨\n\n    benchmark 高度稳定 (ρ=0.89-0.93)——在 GlobalMMLU 上 transfer 好的语言在\n\n    Belebele 上也好。CaCLR 增益在 Belebele 上略小 (+4.3pp vs +4.7pp) 但仍正面。\n\n    '\n  tables:\n  - name: 'Table 10: Cross-Benchmark Generalization (Qwen3-235B)'\n    columns:\n    - Benchmark\n    - Domain\n    - EN_AUROC\n    - ZS_Avg\n    - CaCLR_Avg\n    - Pareto_rho\n    - CaCLR_Delta\n    rows:\n    - - GlobalMMLU\n      - Knowledge QA\n      - 0.832\n      - 0.713\n      - 0.76\n      - -0.65\n      - 0.047\n    - - Belebele\n      - Reading Comp\n      - 0.814\n      - 0.698\n      - 0.741\n      - -0.61\n      - 0.043\n    - - MMLU-ProX\n      - Knowledge QA\n      - 0.839\n      - 0.721\n      - 0.767\n      - -0.67\n      - 0.046\n  figures_description:\n  - 'Fig S2: Per-language ZS AUROC scatter — GlobalMMLU (x) vs Belebele (y). High\n    correlation (ρ=0.89), all points near identity.'\n  analysis: '三 benchmark 一致性强。Pareto frontier 和 CaCLR gains 跨 domain replicate。\n\n    Belebele 的略低结果 underscores domain dependency 但不 undermine core claims。\n\n    '\n- name: Quantization Validation\n  plan_id: plan_010\n  description: W4A16 vs FP16 (Llama) + GPTQ-INT4 vs FP16 (Qwen), 5 layers, 5% subset\n  expected_results:\n    llama_w4a16_vs_fp16:\n      auroc_diff_avg: 0.004\n      auroc_diff_max: 0.008\n      auroc_diff_per_layer:\n        L8: 0.002\n        L16: 0.003\n        L24: 0.005\n        L32: 0.006\n        L40: 0.008\n      cka_quantized_vs_fp16: 0.987\n      paired_t_p: 0.31\n    qwen_int4_vs_fp16:\n      auroc_diff_avg: 0.006\n      auroc_diff_max: 0.013\n      auroc_diff_per_layer:\n        L16: 0.003\n        L32: 0.005\n        L48: 0.006\n        L64: 0.008\n        L80: 0.013\n      cka_quantized_vs_fp16: 0.981\n      paired_t_p: 0.18\n  result_rationale: 'W4A16 仅压缩权重 (4-bit)，激活保持 16-bit，因此对 correctness direction (线性\n\n    probe 的目标) 影响极小——probe 训练使用的是 activation vectors，不直接依赖权重\n\n    精度。GPTQ-INT4 的误差略大因为 4-bit 量化是更激进的压缩，且 Qwen3 有 94 层\n\n    导致误差累积更多。最大偏差 1.3pp 出现在最深层 L80 (误差在 94 层中逐层累积)。\n\n    所有差异在 paired t-test 下不显著 (p > 0.15)，CKA > 0.98 表示量化前后表征\n\n    几乎等价。论文中报告此验证可消除 reviewer \"INT4/W4A16 artifacts\" 的顾虑。\n\n    '\n  tables:\n  - name: 'Table S4: Quantization Validation'\n    columns:\n    - Model\n    - Quantization\n    - Avg_Delta_AUROC\n    - Max_Delta_AUROC\n    - CKA\n    - Paired_t_p\n    rows:\n    - - Llama 4 Scout\n      - W4A16\n      - 0.004\n      - 0.008\n      - 0.987\n      - 0.31\n    - - Qwen3-235B\n      - GPTQ-INT4\n      - 0.006\n      - 0.013\n      - 0.981\n      - 0.18\n  figures_description:\n  - 'Fig S3: Quantized vs FP16 AUROC per layer (error bar plot). All within noise\n    band.'\n  analysis: '量化不影响核心结论。最大偏差 1.3pp 远小于实验主要效应 (Pareto gap ~6pp,\n\n    CaCLR gain ~4.5pp)。放入 appendix 即可。\n\n    '\n- name: CKA Cross-Lingual Geometric Analysis\n  plan_id: plan_011\n  description: CKA (linear kernel) 20 langs × all layers × 2 archs, partial correlation\n    + subspace angle\n  expected_results:\n    cka_partial_corr_controlling_depth: 0.42\n    cka_partial_corr_p: 0.008\n    same_layer_corr_by_depth:\n      25%:\n        rho: -0.48\n        p: 0.032\n      50%:\n        rho: -0.67\n        p: 0.001\n      75%:\n        rho: -0.73\n        p: <0.001\n    n_significant_layers: 18\n    qwen_cka_cliff:\n      location: L64 (68% depth)\n      cka_before: 0.72\n      cka_after: 0.41\n      drop_magnitude: 0.31\n    llama_cka_pattern: gradual decline, no cliff\n    llama_cka_at_L40: 0.52\n    llama_cka_at_L24: 0.71\n    qwen_pooled_rho: -0.58\n    qwen_pooled_p: <0.001\n    llama_pooled_rho: -0.43\n    llama_pooled_p: 0.002\n    between_lang_rho_at_50pct_depth: -0.67\n    between_lang_p_at_50pct_depth: 0.001\n    between_lang_rho_at_75pct_depth: -0.73\n    between_lang_p_at_75pct_depth: <0.001\n    correctness_subspace_angle_avg_deg: 12.3\n    correctness_subspace_angle_std_deg: 4.8\n    global_repr_angle_avg_deg: 38.7\n    global_repr_angle_std_deg: 9.2\n    subspace_angle_ratio: 3.15\n    cka_collapse_threshold: 0.35\n    langs_below_threshold_at_deepest:\n    - sw\n    - yo\n    - am\n    - my\n    per_lang_within_rho_significant: 14\n    per_lang_within_rho_avg: -0.48\n  result_rationale: 'Best tier 假设 \"CKA partial correlation 控制 depth 后仍显著\"。Partial\n    r=0.42\n\n    (p=0.008) 表示 CKA 对 transfer degradation 有独立于 depth 的解释力。核心\n\n    机制：correctness direction 占据低维语言无关子空间 (principal angle ~12°)，\n\n    而全局表征差异远大 (~39°)，ratio 3.15。这意味着即使两种语言的全局表征已\n\n    显著分化 (CKA 下降)，correctness 子空间仍可能保持对齐——直到 CKA 跌破临界\n\n    阈值 ~0.35，此时全局分化足够大以至于连低维子空间也被扰动。\n\n    Qwen3 的 CKA cliff (L64, 突降 0.31) 解释了为何 Qwen Pareto 清晰：在 cliff\n\n    之前 (L0-L60)，transfer 随 depth 缓慢退化；在 cliff 之后 (L64-L94)，transfer\n\n    急剧崩溃。这产生了强 Pareto (ρ=-0.65) 和清晰的 \"optimal transfer zone\" (L48-L60)。\n\n    Llama4 没有 cliff，CKA 渐降 → Pareto 弱且异质 (ρ=-0.33)。\n\n    Between-language 分析 (固定层, n=20) 是最强统计检验：在 50% depth，CKA 高的\n\n    语言 (zh 0.82, es 0.79) transfer 好，CKA 低的 (sw 0.48, am 0.42) transfer 差，\n\n    ρ=-0.67 (p=0.001)。在 75% depth 更强 (ρ=-0.73)，因为此处 CKA variance 更大。\n\n    20 languages 的密度使 per-language within-lang Spearman 首次有足够统计功效\n\n    (n=24 for Qwen vs MVP 的 n=9)：14/20 显著，avg ρ=-0.48，比 MVP pilot\n\n    (几乎全 n.s.) 大幅改善。\n\n    '\n  tables:\n  - name: 'Table 11: CKA Partial Correlation Analysis'\n    columns:\n    - Analysis\n    - Statistic\n    - Value\n    - p_value\n    - Interpretation\n    rows:\n    - - Raw CKA-degradation pooled\n      - rho\n      - -0.64\n      - <0.001\n      - Confounded by depth\n    - - Partial corr controlling depth\n      - r\n      - 0.42\n      - 0.008\n      - CKA adds info beyond depth\n    - - Between-lang at 50% depth (n=20)\n      - rho\n      - -0.67\n      - 0.001\n      - Strongest cross-lang test\n    - - Between-lang at 75% depth (n=20)\n      - rho\n      - -0.73\n      - <0.001\n      - Even stronger deep\n    - - Within-lang avg (n=24 layers)\n      - rho\n      - -0.48\n      - varies\n      - 14/20 langs significant\n  - name: 'Table 12: Subspace Angle Analysis (Quantitative)'\n    columns:\n    - Measure\n    - Qwen3_235B\n    - Llama4_Scout\n    - Interpretation\n    rows:\n    - - Correctness subspace angle (avg)\n      - 11.2°\n      - 13.5°\n      - Small — cross-ling shared\n    - - Correctness subspace angle (std)\n      - 3.9°\n      - 5.7°\n      - More variable in Llama\n    - - Global representation angle (avg)\n      - 41.3°\n      - 36.1°\n      - Large — language-specific\n    - - Global/correctness ratio\n      - 3.69\n      - 2.67\n      - 'Qwen: correctness 4x more stable'\n    - - CKA cliff location\n      - 68% depth\n      - no cliff\n      - Architecture difference\n    - - CKA cliff magnitude\n      - 0.31\n      - N/A\n      - Qwen only\n  figures_description:\n  - 'Fig 6a: CKA heatmap (y=layer, x=language sorted by resource) — Qwen3. L64 处水平色带突变.'\n  - 'Fig 6b: CKA vs transfer degradation partial regression plot (controlling depth).\n    20 langs × multiple layers.'\n  - 'Fig 6c: Subspace angle comparison — bar pairs (correctness angle vs global angle)\n    per language pair. Correctness bars 远短于 global bars.'\n  - 'Fig 6d: CKA depth trajectory comparison — Qwen3 (cliff at L64) vs Llama4 (gradual).\n    Shaded region = transfer collapse zone (CKA < 0.35).'\n  analysis: 'CKA geometric analysis 成立 (partial r=0.42, p=0.008)，支撑 \"geometric analysis\"\n\n    framing。三层 evidence：(1) partial correlation 证明 CKA 有 depth 以外的解释力；\n\n    (2) between-language correlation (ρ=-0.67) 是最直接证据；(3) subspace angle ratio\n\n    3.15 提供几何直觉。CKA cliff 的有/无解释 Qwen vs Llama Pareto 差异。这是\n\n    discovery 级别 finding——连接了 representation geometry 和 practical transfer。\n\n    '\n- name: Linear Projection Sample Efficiency\n  plan_id: plan_012\n  description: Parallel pairs 数量 (10-200) 对 linear projection transfer 的影响\n  expected_results:\n    qwen_L56:\n      pairs_10:\n        auroc: 0.739\n        delta: 0.011\n        ci_width: 0.034\n      pairs_20:\n        auroc: 0.758\n        delta: 0.03\n        ci_width: 0.023\n      pairs_50:\n        auroc: 0.79\n        delta: 0.062\n        ci_width: 0.015\n      pairs_100:\n        auroc: 0.798\n        delta: 0.07\n        ci_width: 0.01\n      pairs_200:\n        auroc: 0.802\n        delta: 0.074\n        ci_width: 0.007\n    llama_L32:\n      pairs_10:\n        auroc: 0.712\n        delta: 0.021\n        ci_width: 0.031\n      pairs_20:\n        auroc: 0.729\n        delta: 0.038\n        ci_width: 0.022\n      pairs_50:\n        auroc: 0.749\n        delta: 0.058\n        ci_width: 0.014\n      pairs_100:\n        auroc: 0.757\n        delta: 0.066\n        ci_width: 0.009\n      pairs_200:\n        auroc: 0.761\n        delta: 0.07\n        ci_width: 0.006\n    elbow_point: 50\n    marginal_gain_50_to_100: 0.008\n    marginal_gain_100_to_200: 0.004\n    caclr_equivalent_pairs: 35\n  result_rationale: 'Linear projection 学习 affine transformation 将 target 语言 correctness\n    subspace\n\n    旋转对齐到 English。Correctness direction 是低维的 (实际是 1D for LR probe)，\n\n    因此旋转矩阵的自由度极低——50 pairs 已充分约束 (条件数稳定)。10 pairs 时 CI\n\n    宽 0.034 (不稳定)，50 pairs CI 收窄至 0.015。超过 50 pairs，marginal gain\n\n    从 +2.2pp/50pairs 骤降至 +0.8pp/50pairs 和 +0.4pp/100pairs。CaCLR (无 parallel\n\n    pairs 的 labels) 等效于 ~35-pair linear projection (AUROC 0.763 vs pairs_35\n\n    插值约 0.76)，表明 MMD distributional matching 实现了部分但非完全的子空间\n\n    对齐。50 pairs 的实用意义大：几乎所有 GlobalMMLU 语言都有 600+ parallel items，\n\n    随机选 50 对即可达到 plateau。\n\n    '\n  tables:\n  - name: 'Table 13: Linear Projection Sample Efficiency (Qwen3, L56)'\n    columns:\n    - Pairs\n    - AUROC_Avg\n    - Delta_vs_ZS\n    - Marginal_Gain\n    - CI_95_Width\n    rows:\n    - - 10\n      - 0.739\n      - 0.011\n      - —\n      - 0.034\n    - - 20\n      - 0.758\n      - 0.03\n      - 0.019\n      - 0.023\n    - - 50\n      - 0.79\n      - 0.062\n      - 0.032\n      - 0.015\n    - - 100\n      - 0.798\n      - 0.07\n      - 0.008\n      - 0.01\n    - - 200\n      - 0.802\n      - 0.074\n      - 0.004\n      - 0.007\n  figures_description:\n  - 'Fig 7: Sample efficiency curve (log-scale x, AUROC y). Clear elbow at 50. Horizontal\n    line = CaCLR (0.763), intersects curve at ~35 pairs.'\n  analysis: '50 pairs 是实用甜点。Linear projection 在 50 pairs 时超过 CaCLR (0.790 vs\n\n    0.763)，但需要 parallel pairs with correctness labels。两方法互补：CaCLR\n\n    for zero-label 场景，linear projection for minimal-data 场景。\n\n    '\n- name: Full-Scale Probing Control Tasks\n  plan_id: plan_013\n  description: Hewitt & Liang control tasks, 20 langs × 2 archs × all layers (扩展 MVP\n    English-only 结果)\n  expected_results:\n    selectivity_below_005_fraction: 0.1\n    low_sel_distribution:\n      early_layers_pct: 0.72\n      low_resource_pct: 0.68\n      overlap_early_AND_low: 0.54\n    qwen_selectivity_avg: 0.178\n    llama_selectivity_avg: 0.152\n    control_auroc_avg: 0.491\n    control_auroc_std: 0.012\n    control_auroc_max: 0.518\n    selectivity_grid_qwen:\n      early_HIGH: 0.045\n      early_MID: 0.036\n      early_LOW: 0.019\n      mid_HIGH: 0.142\n      mid_MID: 0.118\n      mid_LOW: 0.078\n      deep_HIGH: 0.261\n      deep_MID: 0.242\n      deep_LOW: 0.188\n    problem_zone_cells: 48\n    total_cells: 480\n    problem_zone_pct: 0.1\n    english_selectivity_deep_layers: 0.255\n    cross_lingual_selectivity_deep_layers_avg: 0.212\n    cross_lingual_selectivity_deep_layers_low_resource: 0.168\n  result_rationale: 'Control task AUROC 稳定在 ~0.49 (理论 0.50)，confirming permuted labels\n    不被\n\n    probe 学到——probing capacity 有限，不会 memorize random labels。10% 的 grid\n\n    cells 有 selectivity < 0.05，集中在 (early layers, LOW resource) 象限：\n\n    (1) Early layers (L0-L20 Qwen / L0-L12 Llama): correctness signal 尚未形成，\n\n    real probe 和 control probe 表现接近，selectivity ≈ 0；(2) Low-resource\n\n    languages: 较少的预训练数据 → correctness 编码更弱 → real probe 提升有限。\n\n    交叉：54% 的 low-selectivity cells 同时满足 early + low-resource。MVP 的\n\n    English-only plan_013 结果 (selectivity 集中在 L20-L27) 与 full-scale 一致，\n\n    但 cross-lingual extension 揭示了资源维度——英语深层 selectivity 0.255 vs\n\n    低资源深层 0.168。这本身是 methodological contribution：跨语言 probing 中\n\n    ~10% 的结果需谨慎解读。\n\n    '\n  tables:\n  - name: 'Table S5: Selectivity by Depth × Resource Tier (Qwen3)'\n    columns:\n    - Depth_Range\n    - HIGH_Resource\n    - MID_Resource\n    - LOW_Resource\n    rows:\n    - - 0-33% (early)\n      - 0.045\n      - 0.036\n      - 0.019\n    - - 33-67% (mid)\n      - 0.142\n      - 0.118\n      - 0.078\n    - - 67-100% (deep)\n      - 0.261\n      - 0.242\n      - 0.188\n  figures_description:\n  - 'Fig S4: Selectivity heatmap (y=layer, x=language sorted by resource). 左下角 (low\n    resource × early layer) 颜色最浅 (selectivity → 0).'\n  analysis: '10% capacity artifact rate 在 best tier [0.05, 0.15] 范围内。核心 probing\n\n    results (中深层 × 中高资源) selectivity > 0.10，genuine signal。Low-resource ×\n\n    early-layer zone 应在 paper 中标注为 \"interpret with caution\"。\n\n    '\n- name: Gemma 4 31B Dense — Third Architecture\n  plan_id: plan_008\n  description: 60层 Dense (FP16), 第三架构提供 dense vs MoE 对比\n  expected_results:\n    en_best_auroc: 0.821\n    en_best_layer: 48\n    zs_transfer_auroc_avg_20lang: 0.702\n    zs_transfer_success_rate: 0.9\n    zs_fail_langs:\n    - yo\n    - am\n    pareto_spearman_rho_global: -0.52\n    cka_pattern: gradual decline, onset deeper than Llama (no cliff)\n    cka_correctness_subspace_angle_avg: 13.1\n    caclr_delta_auroc_avg: 0.039\n  result_rationale: 'Dense 31B 没有 MoE routing，表征特化更均匀 (无 expert 分配的 language-specific\n\n    路径)，Pareto ρ=-0.52 介于 Qwen3 (ρ=-0.65, 强 MoE cliff) 和 Llama4 (ρ=-0.33,\n\n    弱 MoE) 之间。EN AUROC 0.821 反映 31B dense 的容量低于 235B 但高于 17B active。\n\n    CKA 渐降模式接近 Llama 但 onset 更深——dense model 在中间层保持更强的跨语言\n\n    共享 (无 expert routing 导致的早期分化)。Dense 架构的 Pareto 中等强度提供了\n\n    theory-consistent 的三点比较：cliff MoE (Qwen) > dense (Gemma) > gradual MoE\n\n    (Llama)。仅 yo/am 失败 (2/20)，success rate 0.90。CaCLR delta +3.9pp 低于\n\n    Qwen (+4.7pp) 但高于 Llama (+4.1pp)——dense 的初始 ZS transfer 已较好 (CKA\n\n    更高)，CaCLR 的 marginal room 稍小。\n\n    '\n  tables:\n  - name: 'Table 14: Three-Architecture Comparison'\n    columns:\n    - Architecture\n    - Type\n    - EN_AUROC\n    - ZS_Avg\n    - Pareto_rho\n    - CKA_Pattern\n    - CaCLR_Delta\n    rows:\n    - - Qwen3-235B\n      - MoE (Int4)\n      - 0.832\n      - 0.713\n      - -0.65\n      - Cliff at 68%\n      - 0.047\n    - - Gemma4-31B\n      - Dense (FP16)\n      - 0.821\n      - 0.702\n      - -0.52\n      - Gradual, deep onset\n      - 0.039\n    - - Llama4-Scout\n      - MoE (W4A16)\n      - 0.811\n      - 0.684\n      - -0.33\n      - Gradual, early onset\n      - 0.041\n  figures_description:\n  - 'Fig 8: Three-architecture Pareto overlay — Qwen (steep, clear frontier), Gemma\n    (moderate), Llama (flat, scattered). 三种斜率直观展示 architecture dependence.'\n  analysis: '第三架构填充了 dense vs MoE 对比。Pareto 强度排序 (Qwen > Gemma > Llama) 与\n\n    架构差异一致：MoE cliff 产生最强 tradeoff，dense 渐降产生中等 tradeoff，\n\n    无 cliff 的 MoE 最弱。Camera-ready 的 n=3 架构虽仍不足以做因果归因 (type,\n\n    scale, layers, training data 均不同)，但三点一致的模式 strengthens \"architecture-\n\n    dependent tradeoff\" 的 observational claim。\n\n    '\n- name: Extended Language Coverage (50+)\n  plan_id: plan_009\n  description: 扩展至 50+ 语言 (GlobalMMLU + Belebele full sets)\n  expected_results:\n    total_languages: 53\n    zs_success_rate: 0.83\n    n_success: 44\n    n_fail: 9\n    fail_langs:\n    - am\n    - my\n    - yo\n    - si\n    - lo\n    - km\n    - gu\n    - or\n    - ne\n    pareto_rho_qwen_global_53: -0.62\n    pareto_rho_llama_global_53: -0.31\n    resource_tier_gradient_r2: 0.71\n    new_findings:\n      dravidian_cluster: ta/ml/kn 形成 cluster, ZS AUROC 0.64-0.68, transfer 特征接近 MID\n        tier\n      austronesian_cluster: id/ms/tl transfer 异常好 (0.72-0.74)，因为与英语的表征对齐度高\n      uralic_outlier: fi/hu ZS AUROC 差异大 (fi 0.69 vs hu 0.65)，尽管同为 Uralic\n    caclr_delta_avg_53: 0.044\n    caclr_delta_new_langs_avg: 0.041\n  result_rationale: '扩展至 53 语言后，成功率从 ~90% (20 langs) 降至 83% (53 langs)，因为新增\n\n    语言多为 extreme low-resource (si, lo, km 等)。但 Pareto ρ 和主要 patterns\n\n    保持稳定 (Qwen ρ=-0.62 vs -0.65 at 20 langs)，slight reduction 因为新增的\n\n    低资源语言削弱了 global correlation。Resource tier gradient 在更大样本下更\n\n    robust (R²=0.71, up from ~0.60 at 20 langs)。Austronesian 语言 (id/ms/tl)\n\n    transfer 异常好，因为这些语言在大模型预训练中常被 grouped with English-heavy\n\n    corpora (code-switching, romanization)。CaCLR 增益在新增语言上 (+4.1pp) 与\n\n    原 20 语言 (+4.7pp) 相当，confirming method generalizability。\n\n    '\n  tables:\n  - name: 'Table S6: Extended Language Coverage Summary'\n    columns:\n    - Metric\n    - 20_Langs\n    - 53_Langs\n    rows:\n    - - ZS Success Rate\n      - 95% (Qwen)\n      - 83%\n    - - Pareto ρ Qwen\n      - -0.65\n      - -0.62\n    - - Pareto ρ Llama\n      - -0.33\n      - -0.31\n    - - Resource Gradient R²\n      - ~0.60\n      - 0.71\n    - - CaCLR Δ AUROC avg\n      - 0.047\n      - 0.044\n  figures_description:\n  - 'Fig S5: 53-language ZS success rate by resource tier. Clear gradient: HIGH ~98%,\n    MID ~90%, LOW ~65%.'\n  analysis: 'Camera-ready 扩展确认 core findings 跨 50+ 语言成立。9 种 fail 语言均为\n\n    extreme low-resource (预训练 tokens < 100M)，consistent with domain adaptation\n\n    theory 的 H-divergence 预测。Austronesian cluster 的高 transfer 是 interesting\n\n    secondary finding。'\n",
      "numLines": 1769,
      "startLine": 1,
      "totalLines": 1769
    }
  },
  "sourceToolAssistantUUID": "25caf90b-58a8-462f-b3a8-1f47df11e3bb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "5336efaf-2e22-419f-b322-39a8a1fc07df",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-21T04:22:22.080Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01MXw6RMXh7R19kREPhUqSmt`</summary>

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
  "parentUuid": "a1f86289-e4fa-4abe-8bee-e969dfb297ca",
  "isSidechain": false,
  "requestId": "req_011CbF5J7RC2VAZDruT1Kvby",
  "type": "assistant",
  "uuid": "3c46fe35-1388-476a-8310-92dd22d4c079",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "5336efaf-2e22-419f-b322-39a8a1fc07df",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0193cr4ZatbGcSmYHb88mok6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11325,
      "cache_read_input_tokens": 11841,
      "output_tokens": 465,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11325,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 465,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11325,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11325
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

_source line 16_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[DREAM Review Director] dream_id=20260521T032808 | review_mode=simple | review_visible=True PDF: /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/…",
  "leafUuid": "9dee5b92-b834-44f9-a7d7-294597ba063a",
  "sessionId": "5336efaf-2e22-419f-b322-39a8a1fc07df"
}
```

---

### Runtime record

_source line 17_

```json
{
  "type": "ai-title",
  "aiTitle": "Review cross-lingual calibration research paper",
  "sessionId": "5336efaf-2e22-419f-b322-39a8a1fc07df"
}
```

---

### Assistant

_source line 18 · 2026-05-21T04:22:24.927Z_

<details><summary>Logged reasoning block</summary>

```text
Let me read the PDF in parts and also search for the submit tool.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9dee5b92-b834-44f9-a7d7-294597ba063a",
  "isSidechain": false,
  "requestId": "req_011CbF5JmcMQVu5SCAhpYohA",
  "type": "assistant",
  "uuid": "3374b624-aabe-49fa-b7af-70ee351a7128",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "5336efaf-2e22-419f-b322-39a8a1fc07df",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016k6kCPHVWKsJkUoiwS7B91",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 25223,
      "cache_read_input_tokens": 23166,
      "output_tokens": 242,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 25223,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 242,
          "cache_read_input_tokens": 23166,
          "cache_creation_input_tokens": 25223,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 25223
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

_source line 19 · 2026-05-21T04:22:25.475Z_

Let me read the PDF and find the submit tool.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3374b624-aabe-49fa-b7af-70ee351a7128",
  "isSidechain": false,
  "requestId": "req_011CbF5JmcMQVu5SCAhpYohA",
  "type": "assistant",
  "uuid": "33ee6962-ea10-4252-96d3-ed122d2de89e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "5336efaf-2e22-419f-b322-39a8a1fc07df",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016k6kCPHVWKsJkUoiwS7B91",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 25223,
      "cache_read_input_tokens": 23166,
      "output_tokens": 242,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 25223,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 242,
          "cache_read_input_tokens": 23166,
          "cache_creation_input_tokens": 25223,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 25223
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

_source line 20 · 2026-05-21T04:22:28.213Z_

<details open><summary>🔧 Tool call — Read · `toolu_01DwcTefi2a2UvZX1z1HFSu8`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/best/review_input_db82206b.pdf",
  "pages": "1-5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "33ee6962-ea10-4252-96d3-ed122d2de89e",
  "isSidechain": false,
  "requestId": "req_011CbF5JmcMQVu5SCAhpYohA",
  "type": "assistant",
  "uuid": "fe55028c-1478-4ea9-a9dd-9d5ab2801a1c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "5336efaf-2e22-419f-b322-39a8a1fc07df",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016k6kCPHVWKsJkUoiwS7B91",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 25223,
      "cache_read_input_tokens": 23166,
      "output_tokens": 242,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 25223,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 242,
          "cache_read_input_tokens": 23166,
          "cache_creation_input_tokens": 25223,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 25223
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

_source line 21 · 2026-05-21T04:22:29.370Z_

<details><summary>↩ Tool result · `toolu_011pTDS8XpGTEan2ZUVwiYNN`</summary>

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
  "parentUuid": "2cff45b1-6991-4d66-babb-62dd7fba1738",
  "isSidechain": false,
  "promptId": "29945050-684f-4c5e-9353-e8166e9d5912",
  "type": "user",
  "uuid": "92e6b576-0b3d-44fa-a662-db3d52d68f07",
  "toolUseResult": {
    "matches": [
      "mcp__agent-ml-research__submit_dream_review_report"
    ],
    "query": "select:mcp__agent-ml-research__submit_dream_review_report",
    "total_deferred_tools": 23
  },
  "sourceToolAssistantUUID": "2cff45b1-6991-4d66-babb-62dd7fba1738",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "5336efaf-2e22-419f-b322-39a8a1fc07df",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-21T04:22:28.433Z_

<details><summary>↩ Tool result · `toolu_01DwcTefi2a2UvZX1z1HFSu8`</summary>

```text
PDF pages extracted: 5 page(s) from /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/best/review_input_db82206b.pdf (269.1KB)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fe55028c-1478-4ea9-a9dd-9d5ab2801a1c",
  "isSidechain": false,
  "promptId": "29945050-684f-4c5e-9353-e8166e9d5912",
  "type": "user",
  "uuid": "264b9d69-5ea0-428d-b207-f9e165692a21",
  "toolUseResult": {
    "type": "parts",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/best/review_input_db82206b.pdf",
      "originalSize": 275554,
      "outputDir": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0519-2-projects-xling-calib-direction/5336efaf-2e22-419f-b322-39a8a1fc07df/tool-results/pdf-9c7b8c7f-1573-430c-9308-98cc027bd2a3",
      "count": 5
    }
  },
  "sourceToolAssistantUUID": "fe55028c-1478-4ea9-a9dd-9d5ab2801a1c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "5336efaf-2e22-419f-b322-39a8a1fc07df",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

## Round 2

6 recorded events

### User

_source line 23 · 2026-05-21T04:22:28.430Z_

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
  "parentUuid": "264b9d69-5ea0-428d-b207-f9e165692a21",
  "isSidechain": false,
  "promptId": "29945050-684f-4c5e-9353-e8166e9d5912",
  "type": "user",
  "isMeta": true,
  "uuid": "d729d373-90f1-4dce-85c9-b6a1fe85febf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "5336efaf-2e22-419f-b322-39a8a1fc07df",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-21T04:22:29.365Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_011pTDS8XpGTEan2ZUVwiYNN`</summary>

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
  "parentUuid": "d729d373-90f1-4dce-85c9-b6a1fe85febf",
  "isSidechain": false,
  "requestId": "req_011CbF5JmcMQVu5SCAhpYohA",
  "type": "assistant",
  "uuid": "2cff45b1-6991-4d66-babb-62dd7fba1738",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "5336efaf-2e22-419f-b322-39a8a1fc07df",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016k6kCPHVWKsJkUoiwS7B91",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 25223,
      "cache_read_input_tokens": 23166,
      "output_tokens": 242,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 25223,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 242,
          "cache_read_input_tokens": 23166,
          "cache_creation_input_tokens": 25223,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 25223
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
  "leafUuid": "92e6b576-0b3d-44fa-a662-db3d52d68f07",
  "sessionId": "5336efaf-2e22-419f-b322-39a8a1fc07df"
}
```

---

### Runtime record

_source line 26_

```json
{
  "type": "ai-title",
  "aiTitle": "Review cross-lingual calibration research paper",
  "sessionId": "5336efaf-2e22-419f-b322-39a8a1fc07df"
}
```

---

### Tool call

_source line 27 · 2026-05-21T04:22:34.863Z_

<details open><summary>🔧 Tool call — Read · `toolu_01TxuceKkWeb415mCTNwXCN4`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/best/review_input_db82206b.pdf",
  "pages": "6-10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "92e6b576-0b3d-44fa-a662-db3d52d68f07",
  "isSidechain": false,
  "requestId": "req_011CbF5KJdAUbnPRtLrryQ3Y",
  "type": "assistant",
  "uuid": "f669c91d-1767-4bbb-b090-1e386b18ef28",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "5336efaf-2e22-419f-b322-39a8a1fc07df",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XfR9t6Sgbw69DSRLtpQoQo",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7297,
      "cache_read_input_tokens": 48389,
      "output_tokens": 129,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7297,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 129,
          "cache_read_input_tokens": 48389,
          "cache_creation_input_tokens": 7297,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7297
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

_source line 28 · 2026-05-21T04:22:35.027Z_

<details><summary>↩ Tool result · `toolu_01TxuceKkWeb415mCTNwXCN4`</summary>

```text
PDF pages extracted: 5 page(s) from /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/best/review_input_db82206b.pdf (269.1KB)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f669c91d-1767-4bbb-b090-1e386b18ef28",
  "isSidechain": false,
  "promptId": "29945050-684f-4c5e-9353-e8166e9d5912",
  "type": "user",
  "uuid": "e895b132-4a15-43e4-80e4-73807cab391f",
  "toolUseResult": {
    "type": "parts",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/best/review_input_db82206b.pdf",
      "originalSize": 275554,
      "outputDir": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0519-2-projects-xling-calib-direction/5336efaf-2e22-419f-b322-39a8a1fc07df/tool-results/pdf-8cd04f28-9092-4629-9a3d-fa9917a53228",
      "count": 5
    }
  },
  "sourceToolAssistantUUID": "f669c91d-1767-4bbb-b090-1e386b18ef28",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "5336efaf-2e22-419f-b322-39a8a1fc07df",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

## Round 3

5 recorded events

### User

_source line 29 · 2026-05-21T04:22:35.026Z_

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
  "parentUuid": "e895b132-4a15-43e4-80e4-73807cab391f",
  "isSidechain": false,
  "promptId": "29945050-684f-4c5e-9353-e8166e9d5912",
  "type": "user",
  "isMeta": true,
  "uuid": "5668412f-8ce0-44d1-b9bf-9dfe98fbc659",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "5336efaf-2e22-419f-b322-39a8a1fc07df",
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
  "lastPrompt": "[DREAM Review Director] dream_id=20260521T032808 | review_mode=simple | review_visible=True PDF: /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/…",
  "leafUuid": "e895b132-4a15-43e4-80e4-73807cab391f",
  "sessionId": "5336efaf-2e22-419f-b322-39a8a1fc07df"
}
```

---

### Runtime record

_source line 31_

```json
{
  "type": "ai-title",
  "aiTitle": "Review cross-lingual calibration research paper",
  "sessionId": "5336efaf-2e22-419f-b322-39a8a1fc07df"
}
```

---

### Tool call

_source line 32 · 2026-05-21T04:22:42.140Z_

<details open><summary>🔧 Tool call — Read · `toolu_01DhSg8ot8g1wFo3gvKbQ251`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/best/review_input_db82206b.pdf",
  "pages": "11-12"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5668412f-8ce0-44d1-b9bf-9dfe98fbc659",
  "isSidechain": false,
  "requestId": "req_011CbF5KioTxMUgnRFgZHBaV",
  "type": "assistant",
  "uuid": "13f4ee38-79ea-4138-8440-b3bc463b2e71",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "5336efaf-2e22-419f-b322-39a8a1fc07df",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BKR31FBDQ8Jb7Q4aeSXssA",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 6535,
      "cache_read_input_tokens": 55686,
      "output_tokens": 129,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6535,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 129,
          "cache_read_input_tokens": 55686,
          "cache_creation_input_tokens": 6535,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6535
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

_source line 33 · 2026-05-21T04:22:42.209Z_

<details><summary>↩ Tool result · `toolu_01DhSg8ot8g1wFo3gvKbQ251`</summary>

```text
PDF pages extracted: 2 page(s) from /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/best/review_input_db82206b.pdf (269.1KB)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "13f4ee38-79ea-4138-8440-b3bc463b2e71",
  "isSidechain": false,
  "promptId": "29945050-684f-4c5e-9353-e8166e9d5912",
  "type": "user",
  "uuid": "ea77adc1-1dd0-409a-89ae-29f7a5e3b155",
  "toolUseResult": {
    "type": "parts",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/best/review_input_db82206b.pdf",
      "originalSize": 275554,
      "outputDir": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0519-2-projects-xling-calib-direction/5336efaf-2e22-419f-b322-39a8a1fc07df/tool-results/pdf-765d9294-da0b-423c-b518-c676bd4d037a",
      "count": 2
    }
  },
  "sourceToolAssistantUUID": "13f4ee38-79ea-4138-8440-b3bc463b2e71",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "5336efaf-2e22-419f-b322-39a8a1fc07df",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

## Round 4

13 recorded events

### User

_source line 34 · 2026-05-21T04:22:42.208Z_

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
  "parentUuid": "ea77adc1-1dd0-409a-89ae-29f7a5e3b155",
  "isSidechain": false,
  "promptId": "29945050-684f-4c5e-9353-e8166e9d5912",
  "type": "user",
  "isMeta": true,
  "uuid": "a0908e5b-0d6d-4560-a134-8b04624d1ba1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "5336efaf-2e22-419f-b322-39a8a1fc07df",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 35_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[DREAM Review Director] dream_id=20260521T032808 | review_mode=simple | review_visible=True PDF: /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/…",
  "leafUuid": "ea77adc1-1dd0-409a-89ae-29f7a5e3b155",
  "sessionId": "5336efaf-2e22-419f-b322-39a8a1fc07df"
}
```

---

### Runtime record

_source line 36_

```json
{
  "type": "ai-title",
  "aiTitle": "Review cross-lingual calibration research paper",
  "sessionId": "5336efaf-2e22-419f-b322-39a8a1fc07df"
}
```

---

### Assistant

_source line 37 · 2026-05-21T04:23:59.910Z_

<details><summary>Logged reasoning block</summary>

```text
I've now read the full paper (12 pages) and the review context YAML. Let me now conduct a thorough review of this paper.

Let me summarize what I've read:

**Title:** CaCLR: Zero-Label Cross-Lingual Calibration via Correctness-Direction Alignment in Large Language Models

**Core contributions:**
1. Pareto Frontier Discovery: depth-transferability tradeoff across 3 architectures (Qwen3-235B, Llama 4 Scout, Gemma 4 31B Dense) and 20 languages
2. Difficulty-Capability Decomposition: separates transfer into shared difficulty and language-specific capability components


3. CaCLR Method: combines BCE, SB-ECE, and MMD losses to enable zero-label cross-lingual calibration
4. Cross-Lingual Orthogonality: demonstrates that correctness-confidence orthogonality holds consistently across all languages

**Experimental setup:**
- 3 architectures, 20 languages (extended to 53), 3 benchmarks
- Quantization validation, control tasks, probe complexity comparison

Now I'm checking the review_context.yaml against the paper to see which experiments were actually conducted. Looking at the planned experiments, I can see coverage for the Qwen3-235B and Llama 4 Scout Pareto frontiers in the paper's main results.

Checking the remaining planned experiments against the paper sections and tables—all 13 imagined experiments appear to have corresponding results documented, from the CaCLR full evaluation through the linear projection sample efficiency studies.

Now I'm moving into a detailed review of the paper's strengths. The work addresses a clear gap in cross-lingual calibration that's been overlooked in prior probe-based approaches. The experimental scope is genuinely comprehensive, spanning multiple architectures, languages, and benchmarks with proper validation controls. The Pareto frontier insight about the depth-transferability tradeoff is a meaningful contribution that gives practitioners concrete guidance. The CaCLR method itself combines multiple loss components—binary cross-entropy, symmetric Brier ECE, and maximum mean discrepancy on probe logits—in a way that's well-justified, and the ablation study demonstrates each piece pulls its weight.

The difficulty-capability decomposition is particularly clever, achieving 82% accuracy in predicting which alignment strategy works best. The CKA analysis revealing architectural differences between models—a sharp cliff in Qwen versus gradual decline in Llama—provides real mechanistic insight. The paper includes solid controls throughout: quantization validation, established control tasks, random projection baselines, and comparisons between different probe types. The writing is clear and the narrative hangs together well.

On the weaknesses side, the actual performance gains from CaCLR are modest at around 3.5 percentage points.

The improvements are statistically significant but practically limited—a 3.5 pp AUROC gain and 3.4 pp ECE reduction compared to temperature scaling. The "22% ECE reduction" framing is misleading since it's relative improvement on a metric where absolute performance remains poor. More problematically, the "zero-label" claim is overstated because CaCLR actually requires parallel inputs across languages, which is a substantial requirement that the paper downplays.

When linear projection is given just 50 parallel pairs, it outperforms CaCLR (0.790 vs 0.763), suggesting CaCLR's practical advantage disappears once you have even minimal correctness labels. The architecture comparison is also confounded by multiple differences—model type, scale, layer count, quantization, and training data all vary simultaneously—making it impossible to isolate what's driving the performance differences.

The evaluation is limited to multiple-choice QA tasks, which constrain how correctness can be probed, while generalization to open-ended generation remains untested. The difficulty-capability decomposition only covers a small subset of the full parameter space and the categories largely rediscover the high-resource versus low-resource distinction already known in the field.

The orthogonality claim extends prior work on English to 20 languages, but this is more confirmatory than novel—if orthogonality is truly an architectural property, cross-lingual consistency is expected. The paper also glosses over why certain low-resource languages fail the AUROC threshold without investigating whether the correctness signal itself is unextractable or if the transfer mechanism specifically breaks down in those cases.

There's also substantial repetition across the abstract, introduction, methods, results, and conclusion that could be trimmed to allow for more substantive analysis. Additionally, CaCLR relies on MMD for domain alignment, but the paper doesn't benchmark against other established domain adaptation approaches like DANN or CORAL loss, despite citing domain adaptation theory. The table numbering appears consistent within the paper itself, though some appendix tables may be renumbered differently in the context.

A few minor inconsistencies stand out: the model is referred to as both "Llama 4 Scout 109B" and just "Llama 4," and Section 4.8 on cross-benchmark generalization feels underdeveloped given the effort of evaluating across three benchmarks. All 13 planned experiments are covered, so the experimental scope is thorough. I'm wondering about the practical implications of CaCLR's dependence on parallel inputs—specifically whether the ~8% semantic drift noted for certain language pairs impacts the MMD alignment, and whether testing MMD on higher-dimensional representations beyond the 1D logit space might yield better results. It would also strengthen the work to compare against other distributional alignment losses and explore how CaCLR interacts with depth selection strategies.

The core contribution—the Pareto frontier discovery—is solid and actionable, but CaCLR itself shows only modest improvements and gets outperformed by simpler linear projection approaches. The "zero-label" framing is somewhat misleading since parallel inputs are still required. The CKA analysis offers useful mechanistic insight, though the architecture comparison has some confounding factors. To make this stronger, the authors should be more transparent about CaCLR's actual requirements, benchmark it against alternative alignment methods, dig deeper into failure cases, and provide evidence beyond multiple-choice QA tasks. The experimental rigor across multiple architectures, languages, and benchmarks is genuinely impressive, and the Pareto frontier concept offers real practical value. However, the moderate effect sizes, narrow evaluation scope limited to multiple-choice questions, and the confounded nature of the architecture comparisons suggest this lands at a weak accept rather than a confident one. I'll settle on a 4 — the methodological strength and the Pareto frontier finding are solid contributions, but CaCLR's limited practical applicability and the MCQA-only evaluation prevent a stronger recommendation. Now I should write up the review.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a0908e5b-0d6d-4560-a134-8b04624d1ba1",
  "isSidechain": false,
  "requestId": "req_011CbF5LFZPeybj94QUqJDAF",
  "type": "assistant",
  "uuid": "7c5a57f3-42d5-44ba-8439-5e9355251099",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "5336efaf-2e22-419f-b322-39a8a1fc07df",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012ZNx8sCmZHoDDFeA5E5fWh",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2746,
      "cache_read_input_tokens": 62221,
      "output_tokens": 6081,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2746,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 6081,
          "cache_read_input_tokens": 62221,
          "cache_creation_input_tokens": 2746,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2746
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

_source line 38 · 2026-05-21T04:24:00.063Z_

I've read the full 12-page paper and all 13 planned experiments from the context YAML. Now I'll compile the review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7c5a57f3-42d5-44ba-8439-5e9355251099",
  "isSidechain": false,
  "requestId": "req_011CbF5LFZPeybj94QUqJDAF",
  "type": "assistant",
  "uuid": "9407ab28-142a-4b6e-a8c8-920d4aaf9871",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "5336efaf-2e22-419f-b322-39a8a1fc07df",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012ZNx8sCmZHoDDFeA5E5fWh",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2746,
      "cache_read_input_tokens": 62221,
      "output_tokens": 6081,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2746,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 6081,
          "cache_read_input_tokens": 62221,
          "cache_creation_input_tokens": 2746,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2746
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

_source line 39 · 2026-05-21T04:25:02.817Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_dream_review_report · `toolu_013CJM7uWaTr9QaHtqkiMLog`</summary>

```json
{
  "report": "# Review Report: CaCLR: Zero-Label Cross-Lingual Calibration via Correctness-Direction Alignment in Large Language Models\n\n## Summary\n\nThis paper presents the first systematic study of cross-lingual correctness-probe calibration, making four contributions: (1) discovering an architecture-dependent depth–transferability Pareto frontier across 3 architectures and 20 languages, (2) decomposing correctness transfer into difficulty-shared and capability-specific components, (3) proposing CaCLR (BCE + SB-ECE + MMD on probe logits) for zero-label cross-lingual calibration, and (4) extending the correctness–confidence orthogonality finding to 20 languages. Experiments cover 3 models (Qwen3-235B, Llama 4 Scout, Gemma 4 31B), 3 benchmarks (GlobalMMLU, Belebele, MMLU-ProX), with extension to 53 languages.\n\n---\n\n## Strengths\n\n**S1: Well-defined and important problem.** Cross-lingual calibration is practically important, and the observation that all existing probe-based calibration methods operate exclusively in English is a clear, well-motivated gap. The paper precisely characterizes what transfers, what doesn't, and why.\n\n**S2: The Pareto frontier concept is the paper's strongest contribution.** The depth–transferability tradeoff is a genuine, reproducible discovery with actionable implications: deeper layers yield better English probes but degrade cross-lingual transfer. Quantifying this via per-language Spearman ρ (ranging from −0.82 for yo to −0.41 for es on Qwen3) and showing architecture dependence (ρ = −0.65 Qwen3 vs −0.33 Llama 4 vs −0.52 Gemma 4) provides a useful framework for practitioners.\n\n**S3: Exceptional experimental thoroughness.** All 13 planned experiments from the design are represented in the paper: Pareto frontiers on 2 primary architectures, CaCLR with full ablation and β sensitivity, difficulty decomposition, orthogonality, probe complexity comparison, 3 benchmarks, quantization validation, CKA geometric analysis, linear projection sample efficiency, control tasks, a third architecture, and extended language coverage (53 languages). This breadth is commendable.\n\n**S4: CKA geometric analysis provides compelling mechanistic insight.** The CKA cliff in Qwen3 at L64 (68% depth, CKA drop from 0.72 to 0.41) directly explains why Qwen3 has a strong Pareto while Llama 4's gradual CKA decline produces a weaker tradeoff. The subspace angle analysis (correctness ~12° vs global ~39°, ratio 3.15×) provides geometric intuition for why transfer works at all. Partial correlation controlling for depth (r = 0.42, p = 0.008) is the right statistical test.\n\n**S5: Strong statistical methodology throughout.** Paired permutation tests, bootstrap CIs, Cohen's d, control tasks (Hewitt & Liang), random-direction projection controls, and quantization validation. The paper consistently avoids claiming significance without appropriate testing.\n\n**S6: CaCLR ablation is well-designed.** Table 5 cleanly isolates each component's contribution. The finding that SB-ECE alone slightly decreases AUROC (−0.4 pp) but synergizes with MMD (full model +3.5 pp) is non-obvious and well-documented. The β sensitivity sweep (Table 6) identifies the sweet spot and the inverted-U shape is interpretable.\n\n---\n\n## Weaknesses\n\n**W1: \"Zero-label\" framing is misleading (Major).** The title and abstract emphasize \"zero-label cross-lingual calibration,\" but CaCLR requires parallel inputs — the same items translated into each target language — to compute MMD on probe logits. Having parallel test items for 20+ languages is a non-trivial data requirement. \"Zero correctness-label\" would be more accurate. This matters because CaCLR's claimed advantage over linear projection (50 pairs) is the absence of paired correctness labels, yet both methods require parallel inputs. The practical gap between \"I have parallel inputs\" and \"I have parallel inputs with 50 correctness labels\" is small.\n\n**W2: CaCLR's practical niche is narrow (Major).** CaCLR (0.763 AUROC) is outperformed by linear projection with just 50 parallel pairs (0.790), and even by few-shot with 25 target labels (0.745 is close, 100 labels gives 0.774). Since CaCLR itself requires ~630 parallel items per language for MMD, any practitioner with this data could trivially obtain 50 correctness labels (just run the model and compare to ground truth on 50 items). The equivalence to ~35 pairs of linear projection (Section 4.10) makes CaCLR look like a less efficient version of a simpler method. The paper frames these as \"complementary,\" but the practical scenario where you have 630+ parallel items but zero correctness labels is unclear.\n\n**W3: Moderate effect sizes (Major).** CaCLR's primary improvements are +3.5 pp AUROC over zero-shot and −3.4 pp ECE vs temperature scaling (0.121 vs 0.155). While statistically significant (p = 0.003, d = 0.52), the practical significance is debatable. The headline \"22% ECE reduction\" uses a relative metric that inflates the impression — the absolute ECE of 0.121 is still quite high. A downstream evaluation showing that better-calibrated probes lead to better decisions (e.g., selective prediction, abstention) would strengthen the case.\n\n**W4: Confounded architecture comparison (Moderate).** The three architectures differ simultaneously in type (MoE vs dense), total parameters (235B vs 109B vs 31B), active parameters, layer count (94 vs 48 vs 60), quantization precision, and training data. The paper acknowledges this in Limitations but still frames interpretations like \"MoE routing sharpens the Pareto tradeoff\" (Section 4.7) and \"cliff MoE > dense > gradual MoE\" as if these were established findings rather than speculation from n = 3 confounded observations. The ordering ρ_Qwen > ρ_Gemma > ρ_Llama could equally be driven by model scale, training data quality, or layer count.\n\n**W5: MCQA-only evaluation (Moderate).** All experiments use multiple-choice QA formats. Correctness in MCQA is a clean binary signal, but real-world calibration needs extend to open-ended generation, where \"correctness\" is harder to define and calibration arguably matters more. The paper's conclusions about \"output-based calibration limits\" (Section 4.6) may not generalize beyond MCQA. The Limitations paragraph acknowledges this in one sentence, but the abstract and contributions make unqualified claims.\n\n**W6: Orthogonality contribution is incremental (Minor).** Miao & Ungar (2026) established correctness–confidence orthogonality in English. Extending this to 20 languages with cosine < 0.06 is confirmatory, not surprising — the paper itself argues this is an \"architectural property\" independent of input language. If true, cross-lingual persistence is the expected outcome, not a discovery. This is worth a paragraph in the results, not a numbered contribution.\n\n**W7: Difficulty-capability decomposition has limited statistical power (Minor).** The decomposition uses only 10 languages × 8 layers. The two categories (capability-dominated = zh/es/fr/de/ru/ko; difficulty-dominated = hi/tr/sw/bn) largely correspond to the high-resource / low-resource split already known from the Pareto analysis. The \"82% prediction accuracy\" is on N = 10 languages — one misclassification changes this to 72%. The prescriptive value is asserted but not validated on held-out languages.\n\n**W8: No comparison with alternative alignment methods (Minor).** CaCLR uses MMD with Gaussian RBF kernel. The domain adaptation literature offers many alternatives: CORAL loss (second-order alignment), adversarial discriminators (DANN), optimal transport, contrastive alignment. The paper cites domain adaptation theory (Ben-David et al., 2010; Zhao et al., 2019) but tests only one alignment loss. Even testing CORAL (which is trivial to implement) would contextualize CaCLR's design choices.\n\n---\n\n## Missing Experiments / Coverage Gaps\n\nAll 13 planned experiments are represented in the paper. The coverage is comprehensive.\n\nOne notable gap: failure case analysis for languages below the 0.60 threshold (am, yo, my). The paper notes these failures but doesn't analyze whether the correctness direction is not extractable in these languages vs. whether transfer specifically breaks down. CaCLR's per-language performance on these failing languages is not separately reported.\n\n---\n\n## Questions for Authors\n\n1. CaCLR requires ~630 parallel items per language. In what practical scenario would a user have this data but be unable to obtain even 50 correctness labels (which would allow linear projection to outperform CaCLR)?\n2. The context YAML notes ~8% semantic drift in am/yo/my translations. How sensitive is MMD alignment to translation quality? Have you tested with degraded translations?\n3. Why not compare CaCLR against CORAL loss or adversarial alignment, given the explicit framing around domain adaptation theory?\n4. The probe operates in 1D logit space. Have you attempted MMD on higher-dimensional intermediate representations before projection?\n5. What happens when CaCLR is applied at the Pareto-optimal depth (L56) rather than EN-optimal (L72)? Table 4 uses Pareto-optimal layers — does CaCLR at L72 combined with depth selection yield additional gains?\n\n---\n\n## Minor Issues\n\n- The paper uses both \"Llama 4 Scout 109B\" and \"Llama 4\" inconsistently.\n- Section 4.8 (cross-benchmark generalization) is very brief given the effort of running on 3 benchmarks. The per-language rank correlations (ρ = 0.89–0.93) are mentioned but the actual per-language data is not shown.\n- Appendix E (Linear Projection Sample Efficiency: Llama 4) has Table 19 but no accompanying text or analysis.\n- Some appendices (B: Probe Complexity) appear to have only a table with no prose.\n\n---\n\n## Overall Assessment\n\n**Score: 4 — Weak Accept**\n\nThis is a thorough and methodologically sound empirical study that addresses a genuine gap in the literature. The Pareto frontier discovery (Contribution 1) is the paper's strongest offering — it's a clear, reproducible finding with practical value, and the CKA geometric analysis provides compelling mechanistic explanation. The experimental coverage is exceptional for a conference paper.\n\nHowever, the proposed method (CaCLR) has moderate effect sizes (+3.5 pp AUROC), a narrow practical niche (outperformed by linear projection with minimal data, while requiring similar parallel data), and a somewhat misleading \"zero-label\" framing. The orthogonality extension is incremental, and the architecture comparison is confounded. The MCQA-only evaluation limits the scope of the conclusions.\n\nThe paper would benefit from: (1) more transparent framing of CaCLR's data requirements versus its baselines, (2) comparison with at least one alternative alignment objective, (3) downstream task evaluation showing practical impact of improved calibration, and (4) explicit qualification of claims to the MCQA setting.\n\n**Recommendation:** The paper is above the acceptance threshold based on the quality of the Pareto frontier analysis, CKA geometric insights, and experimental rigor. CaCLR as a method contribution is less compelling on its own. If the authors address the framing issues (W1) and add an alternative alignment comparison (W8), this would be a solid accept.\n\n**Confidence: 4/5** — I am confident in my assessment. The paper is in my area of expertise (representation probing, calibration, cross-lingual transfer). The main uncertainty is whether the practical niche for CaCLR is larger than I estimate.",
  "project": "xling_calib_direction",
  "tier": "best",
  "dream_id": "20260521T032808",
  "overall_score": "4 — Weak Accept",
  "review_visible": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9407ab28-142a-4b6e-a8c8-920d4aaf9871",
  "isSidechain": false,
  "requestId": "req_011CbF5LFZPeybj94QUqJDAF",
  "type": "assistant",
  "uuid": "8bbd8d0b-3dd9-419a-92d1-7cbc42907389",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "5336efaf-2e22-419f-b322-39a8a1fc07df",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012ZNx8sCmZHoDDFeA5E5fWh",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2746,
      "cache_read_input_tokens": 62221,
      "output_tokens": 6081,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2746,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 6081,
          "cache_read_input_tokens": 62221,
          "cache_creation_input_tokens": 2746,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2746
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

_source line 40_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[DREAM Review Director] dream_id=20260521T032808 | review_mode=simple | review_visible=True PDF: /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/…",
  "leafUuid": "8bbd8d0b-3dd9-419a-92d1-7cbc42907389",
  "sessionId": "5336efaf-2e22-419f-b322-39a8a1fc07df"
}
```

---

### Runtime record

_source line 41_

```json
{
  "type": "ai-title",
  "aiTitle": "Review cross-lingual calibration research paper",
  "sessionId": "5336efaf-2e22-419f-b322-39a8a1fc07df"
}
```

---

### Tool result

_source line 42 · 2026-05-21T04:25:06.616Z_

<details><summary>↩ Tool result · `toolu_013CJM7uWaTr9QaHtqkiMLog`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"report_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/best/review_report.md\", \"dream_id\": \"dream_20260521T032808\", \"tier\": \"best\", \"review_visible\": true}, \"error\": \"\"}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8bbd8d0b-3dd9-419a-92d1-7cbc42907389",
  "isSidechain": false,
  "promptId": "29945050-684f-4c5e-9353-e8166e9d5912",
  "type": "user",
  "uuid": "6ff2b4f2-daf7-499b-ad12-d68b251f35bf",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"report_path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/best/review_report.md\\\", \\\"dream_id\\\": \\\"dream_20260521T032808\\\", \\\"tier\\\": \\\"best\\\", \\\"review_visible\\\": true}, \\\"error\\\": \\\"\\\"}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"report_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T032808/best/review_report.md\", \"dream_id\": \"dream_20260521T032808\", \"tier\": \"best\", \"review_visible\": true}, \"error\": \"\"}"
    }
  },
  "sourceToolAssistantUUID": "8bbd8d0b-3dd9-419a-92d1-7cbc42907389",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "5336efaf-2e22-419f-b322-39a8a1fc07df",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 43 · 2026-05-21T04:25:06.625Z_

```json
{
  "parentUuid": "6ff2b4f2-daf7-499b-ad12-d68b251f35bf",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "f333fdab-d676-405d-9917-fd1b310d6fb5",
  "timestamp": "2026-05-21T04:25:06.625Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "5336efaf-2e22-419f-b322-39a8a1fc07df",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 44 · 2026-05-21T04:25:13.842Z_

审稿完成。评分 **4 — Weak Accept**。

核心判断：Pareto frontier 发现和 CKA 几何分析是最强贡献，实验覆盖全面（13 个计划实验全部呈现）。主要不足在于 CaCLR 效果量中等（+3.5pp AUROC），"zero-label"标题与实际需要 parallel inputs 的要求存在 framing 偏差，且被仅需 50 pairs 的 linear projection 超越。报告已写入 `dream_reports/dream_20260521T032808/best/review_report.md`。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f333fdab-d676-405d-9917-fd1b310d6fb5",
  "isSidechain": false,
  "requestId": "req_011CbF5WtxhoZW8WHYenQgzm",
  "type": "assistant",
  "uuid": "7d84141b-3680-4505-936f-d27147d8a318",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "5336efaf-2e22-419f-b322-39a8a1fc07df",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QJwEHiKA8S93SdVNjrWF38",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6306,
      "cache_read_input_tokens": 64967,
      "output_tokens": 177,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6306,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 177,
          "cache_read_input_tokens": 64967,
          "cache_creation_input_tokens": 6306,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6306
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
  "lastPrompt": "[DREAM Review Director] dream_id=20260521T032808 | review_mode=simple | review_visible=True PDF: /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/…",
  "leafUuid": "7d84141b-3680-4505-936f-d27147d8a318",
  "sessionId": "5336efaf-2e22-419f-b322-39a8a1fc07df"
}
```

---

### Runtime record

_source line 46_

```json
{
  "type": "ai-title",
  "aiTitle": "Review cross-lingual calibration research paper",
  "sessionId": "5336efaf-2e22-419f-b322-39a8a1fc07df"
}
```

---
