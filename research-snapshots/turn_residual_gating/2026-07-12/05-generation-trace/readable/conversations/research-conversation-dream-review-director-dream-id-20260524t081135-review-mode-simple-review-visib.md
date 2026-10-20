# Research conversation: [DREAM Review Director] dream_id=20260524T081135 | review_mode=simple | review_visible=True PDF: /home/ubuntu/.agent-ml-

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 46
- **Recorded user turns:** 3
- **Tool calls:** 8
- **Original source:** `logs/chats/exported-trajectories/account-1/ddd5074c-2b8b-40c6-b29f-f44ff9f131a7.jsonl`
- **Structured JSON:** [`883143ef0a083b43bf63.json`](../../sessions/88/883143ef0a083b43bf63.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-24T09:12:37.066Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-24T09:12:37.066Z",
  "sessionId": "ddd5074c-2b8b-40c6-b29f-f44ff9f131a7",
  "content": "[DREAM Review Director]\ndream_id=20260524T081135 | review_mode=simple | review_visible=True\nPDF: /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260524T081135/worst/review_input_f5f46a62.pdf\n\n（内部编排信息：tier=worst，仅用于 submit_dream_review_report 调用。\n你在向 Reviewer 发送审稿任务时，**严禁**提及档位名称 best/median/worst，\n也不要暗示论文结果的好坏。Reviewer 必须盲审。）\n\n任务：对上述 PDF 进行 simple 模式审稿。 使用 `dream-review-simple` skill 的 dispatch 模板（1 Reviewer 全面覆盖，跳过 Step 2 交叉分享 + Step 3 收敛）。\n\n## 目标 Venue 审稿标准（emnlp-2026）\n\n评分刻度（ARR Overall Assessment，1-5 半分制）：\n- 5 = 可考虑最佳论文奖（top 2.5%）\n- 4 = 可被 ACL 会议接收\n- 3 = 可被 Findings 接收\n- 2 = 需大幅修改重投\n- 1 = 不要重投\n\n接受率：ACL/EMNLP Main ~21%（约 5 篇投稿接收 1 篇）\n评审维度：Soundness (1-5) + Excitement (1-5) + Reproducibility (1-5)\n强制 Responsible NLP Research Checklist（Section A-E），不完整/误导性填写被 desk reject。\n自动 reject 信号：匿名性违规、超页数限制、缺 Limitations section、幻觉引用。\n\n请严格按照上述评分刻度和接受率校准你的评分。\n\n## 实验设计参考\n\n完整实验设计（含想象实验列表）：`/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260524T081135/worst/review_context.yaml`\n论文可能未完整反映所有实验——参考此文件判断覆盖度。\n完成后必须调用 `submit_dream_review_report(report, project=\"turn_residual_gating\", tier=\"worst\", dream_id=\"20260524T081135\", review_visible=True)` —— 报告会写入 dream_reports/dream_20260524T081135/worst/review_report.md，编排进程通过 subprocess 退出读取它。\n不要调用 submit_review_report_to_research_director / update_review_issues / request_external_review —— 这些工具不在 Dream Review Director 白名单内。\n"
}
```

---

### Runtime record

_source line 2 · 2026-05-24T09:12:37.072Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-24T09:12:37.072Z",
  "sessionId": "ddd5074c-2b8b-40c6-b29f-f44ff9f131a7"
}
```

---

## Round 1

17 recorded events

### User

_source line 3 · 2026-05-24T09:12:37.107Z_

[DREAM Review Director]
dream_id=20260524T081135 | review_mode=simple | review_visible=True
PDF: /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260524T081135/worst/review_input_f5f46a62.pdf

（内部编排信息：tier=worst，仅用于 submit_dream_review_report 调用。
你在向 Reviewer 发送审稿任务时，**严禁**提及档位名称 best/median/worst，
也不要暗示论文结果的好坏。Reviewer 必须盲审。）

任务：对上述 PDF 进行 simple 模式审稿。 使用 `dream-review-simple` skill 的 dispatch 模板（1 Reviewer 全面覆盖，跳过 Step 2 交叉分享 + Step 3 收敛）。

## 目标 Venue 审稿标准（emnlp-2026）

评分刻度（ARR Overall Assessment，1-5 半分制）：
- 5 = 可考虑最佳论文奖（top 2.5%）
- 4 = 可被 ACL 会议接收
- 3 = 可被 Findings 接收
- 2 = 需大幅修改重投
- 1 = 不要重投

接受率：ACL/EMNLP Main ~21%（约 5 篇投稿接收 1 篇）
评审维度：Soundness (1-5) + Excitement (1-5) + Reproducibility (1-5)
强制 Responsible NLP Research Checklist（Section A-E），不完整/误导性填写被 desk reject。
自动 reject 信号：匿名性违规、超页数限制、缺 Limitations section、幻觉引用。

请严格按照上述评分刻度和接受率校准你的评分。

## 实验设计参考

完整实验设计（含想象实验列表）：`/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260524T081135/worst/review_context.yaml`
论文可能未完整反映所有实验——参考此文件判断覆盖度。
完成后必须调用 `submit_dream_review_report(report, project="turn_residual_gating", tier="worst", dream_id="20260524T081135", review_visible=True)` —— 报告会写入 dream_reports/dream_20260524T081135/worst/review_report.md，编排进程通过 subprocess 退出读取它。
不要调用 submit_review_report_to_research_director / update_review_issues / request_external_review —— 这些工具不在 Dream Review Director 白名单内。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "b2df24c2-fd3f-4fb8-afa6-a3945babf3db",
  "type": "user",
  "uuid": "e9de1c14-d337-42c5-8102-da50e2772f07",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "ddd5074c-2b8b-40c6-b29f-f44ff9f131a7",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-24T09:12:37.107Z_

```json
{
  "parentUuid": "e9de1c14-d337-42c5-8102-da50e2772f07",
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
  "uuid": "d9bfc07e-8319-4ba0-b349-df4e60dbf040",
  "timestamp": "2026-05-24T09:12:37.107Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "ddd5074c-2b8b-40c6-b29f-f44ff9f131a7",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---

### Runtime record

_source line 5 · 2026-05-24T09:12:37.107Z_

```json
{
  "parentUuid": "d9bfc07e-8319-4ba0-b349-df4e60dbf040",
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
  "uuid": "fe2e72c3-b5cf-4079-af7d-3b586d80825e",
  "timestamp": "2026-05-24T09:12:37.107Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "ddd5074c-2b8b-40c6-b29f-f44ff9f131a7",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---

### Runtime record

_source line 6 · 2026-05-24T09:12:37.107Z_

```json
{
  "parentUuid": "fe2e72c3-b5cf-4079-af7d-3b586d80825e",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "b61265cc-50e2-4d5c-84e5-812fdc4c74bd",
  "timestamp": "2026-05-24T09:12:37.107Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "ddd5074c-2b8b-40c6-b29f-f44ff9f131a7",
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
  "aiTitle": "Review residual gating paper for EMNLP",
  "sessionId": "ddd5074c-2b8b-40c6-b29f-f44ff9f131a7"
}
```

---

### Assistant

_source line 8 · 2026-05-24T09:12:42.065Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to conduct a dream review of a paper PDF. Let me first understand the task:

1. I need to review a PDF paper
2. Use the `dream-review-simple` skill dispatch template (1 Reviewer, skip cross-sharing and convergence steps)
3. Submit the review using `submit_dream_review_report`

Let me start by reading the PDF and the review context, then dispatch a reviewer agent.

First, let me load the necessary tools and read the relevant files.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b61265cc-50e2-4d5c-84e5-812fdc4c74bd",
  "isSidechain": false,
  "requestId": "req_011CbM8sFZspXJZybbPAofHt",
  "type": "assistant",
  "uuid": "acbb6592-7b86-484c-b2d0-7171ce607b9b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "ddd5074c-2b8b-40c6-b29f-f44ff9f131a7",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015tXq7c2Hi9LV51M1qbDAxz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 13367,
      "cache_read_input_tokens": 11841,
      "output_tokens": 348,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13367,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 348,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 13367,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13367
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

_source line 9 · 2026-05-24T09:12:42.937Z_

开始审稿。先读取 PDF 和实验设计参考文件。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "acbb6592-7b86-484c-b2d0-7171ce607b9b",
  "isSidechain": false,
  "requestId": "req_011CbM8sFZspXJZybbPAofHt",
  "type": "assistant",
  "uuid": "d8ad26e1-b128-42af-9043-11c6ba74bd29",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "ddd5074c-2b8b-40c6-b29f-f44ff9f131a7",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015tXq7c2Hi9LV51M1qbDAxz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 13367,
      "cache_read_input_tokens": 11841,
      "output_tokens": 348,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13367,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 348,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 13367,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13367
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

_source line 10 · 2026-05-24T09:12:43.618Z_

<details open><summary>🔧 Tool call — Read · `toolu_01TqZFceKzEWNDzhY3rxX4TQ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260524T081135/worst/review_input_f5f46a62.pdf"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d8ad26e1-b128-42af-9043-11c6ba74bd29",
  "isSidechain": false,
  "requestId": "req_011CbM8sFZspXJZybbPAofHt",
  "type": "assistant",
  "uuid": "79bb6368-829a-48d6-8d74-74c1fb063f05",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "ddd5074c-2b8b-40c6-b29f-f44ff9f131a7",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015tXq7c2Hi9LV51M1qbDAxz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 13367,
      "cache_read_input_tokens": 11841,
      "output_tokens": 348,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13367,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 348,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 13367,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13367
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

_source line 11 · 2026-05-24T09:12:43.661Z_

<details><summary>↩ Tool result · reported error · `toolu_01TqZFceKzEWNDzhY3rxX4TQ`</summary>

```text
This PDF has 14 pages, which is too many to read at once. Use the pages parameter to read specific page ranges (e.g., pages: "1-5"). Maximum 20 pages per request.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "79bb6368-829a-48d6-8d74-74c1fb063f05",
  "isSidechain": false,
  "promptId": "b2df24c2-fd3f-4fb8-afa6-a3945babf3db",
  "type": "user",
  "uuid": "a7f586e8-034a-40f6-b7fd-2dcb8c8839c7",
  "toolUseResult": "Error: This PDF has 14 pages, which is too many to read at once. Use the pages parameter to read specific page ranges (e.g., pages: \"1-5\"). Maximum 20 pages per request.",
  "sourceToolAssistantUUID": "79bb6368-829a-48d6-8d74-74c1fb063f05",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "ddd5074c-2b8b-40c6-b29f-f44ff9f131a7",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-24T09:12:44.027Z_

<details open><summary>🔧 Tool call — Read · `toolu_01VwLzhzPZvQuSEfcN7FzGDp`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260524T081135/worst/review_context.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a7f586e8-034a-40f6-b7fd-2dcb8c8839c7",
  "isSidechain": false,
  "requestId": "req_011CbM8sFZspXJZybbPAofHt",
  "type": "assistant",
  "uuid": "678308d9-cc29-497c-876e-758db8f52d9c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "ddd5074c-2b8b-40c6-b29f-f44ff9f131a7",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015tXq7c2Hi9LV51M1qbDAxz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 13367,
      "cache_read_input_tokens": 11841,
      "output_tokens": 348,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13367,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 348,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 13367,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13367
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

_source line 13 · 2026-05-24T09:12:44.308Z_

<details><summary>↩ Tool result · `toolu_01VwLzhzPZvQuSEfcN7FzGDp`</summary>

```text
1	narrative_guidance: '放弃 ''discover→diagnose→remedy'' 弧。Llama SS 失败（AR GAR β=0 ≈ 0.04，gap
2	  ~12×）证明 SS 是 model-specific，不可泛化为 general mitigation。 Reframe 为纯 mechanistic diagnostic
3	  paper。Title 改为 ''Why Auxiliary Attention Losses Fail Under Exposure Bias: A Multi-Model
4	  Diagnostic Study''。 SS 从 Results 独立小节降级为 Discussion ''attempted mitigation''，承认
5	  model-specific 局限。核心卖点转为 failure mode taxonomy （NF1 反向 turn conditioning + NF2 distribution
6	  shift + NF3 干预强度不足）的系统分类学价值。 加强 PCGrad ''first empirical elimination of gradient
7	  conflict hypothesis'' 叙事。加强 Dongre convergent failure evidence： 两种干预 × 两种模型 = 4
8	  paths all fail on Llama。Introduction 结尾加 ''our negative results establish concrete
9	  failure modes that future work must overcome''。Discussion 加 concrete next steps（data-dependent
10	  SS schedule、curriculum exposure、inference-time only）。 仍冲 EMNLP Findings 2.5-3.0，靠
11	  systematic rigor + cross-model replication + failure taxonomy。 审稿人 novelty objection
12	  probability 0.7-1.0，fatal/severe concerns 3-5 remaining。
13	
14	  '
15	imagined_experiments:
16	- name: Llama Gradient Conflict Analysis
17	  plan_id: plan_013
18	  description: 'Llama-3.1-8B 上对 3 个 epoch checkpoint 计算 NTP-GAR 梯度 cos_sim 和 magnitude
19	    ratio， 验证梯度方向冲突是否跨模型存在。
20	
21	    '
22	  expected_results:
23	    cos_sim_mean: 0.005
24	    cos_sim_std: 0.07
25	    neg_cos_sim_layers_pct: 53.1
26	    pos_cos_sim_layers_pct: 46.9
27	    mag_ratio_median: 25.7
28	    mag_ratio_range: '[12.0, 45.0]'
29	    epoch0_cos_sim: 0.012
30	    epoch0_neg_layers_pct: 50.0
31	    epoch1_cos_sim: 0.003
32	    epoch1_neg_layers_pct: 53.1
33	    epoch2_cos_sim: -0.001
34	    epoch2_neg_layers_pct: 56.3
35	    gpu_hours: 0.3
36	  result_rationale: 'Worst case：Llama 梯度是 near-orthogonal（cos_sim ≈ 0），不是 conflict（cos_sim
37	    < 0）。 neg_layers 53.1% 接近随机水平（50%），与 Qwen 的 67-79% 系统性 negative 模式不同。 这意味着两模型的梯度几何结构不一致——Qwen
38	    有 mild conflict，Llama 没有。审稿人会说： "gradient conflict 不是 cross-model mechanism，那你为什么用一整个
39	    section（§6.2）讨论它？" Magnitude ratio 25.7× 比 Qwen（7.5-14.7×）更极端，但方向冲突不存在使 PCGrad
40	    在 Llama 上 没有可消除的 conflict。总体：数据支持 NTP 幅度主导，但削弱 gradient conflict 作为 universal
41	    mechanism 的叙事。PCGrad 变成 "only relevant on Qwen，model-specific finding"。
42	
43	    '
44	  tables:
45	  - caption: Cross-Model Gradient Geometry Comparison
46	    columns:
47	    - Model
48	    - cos_sim (mean)
49	    - neg_layers (%)
50	    - mag_ratio (median)
51	    - Interpretation
52	    rows:
53	    - - Qwen-2.5-7B (ep0→ep2)
54	      - '-0.062'
55	      - '72.6'
56	      - 11.9×
57	      - Mild conflict + NTP dominance
58	    - - Llama-3.1-8B (ep0→ep2)
59	      - '+0.005'
60	      - '53.1'
61	      - 25.7×
62	      - Orthogonal + extreme NTP dominance
63	  - caption: Llama Per-Epoch Gradient Statistics
64	    columns:
65	    - Epoch
66	    - cos_sim
67	    - neg_layers (%)
68	    - mag_ratio
69	    rows:
70	    - - '0'
71	      - '+0.012'
72	      - '50.0'
73	      - '18.3'
74	    - - '1'
75	      - '+0.003'
76	      - '53.1'
77	      - '24.1'
78	    - - '2'
79	      - '-0.001'
80	      - '56.3'
81	      - '25.7'
82	  figures_description:
83	  - Per-layer cos_sim heatmap (Qwen vs Llama, 3 epochs)：Qwen 显示系统性 negative bias（蓝色主导），Llama
84	    围绕 0 随机散布（蓝红交替）
85	  - Magnitude ratio bar chart per layer：Llama L20-L31 尤其极端（30-45×），深层 NTP 幅度压制更强
86	  analysis: 'PCGrad 叙事在 worst case 下从 "cross-model causal exclusion" 收缩为 "Qwen-specific
87	    observation"。 Paper 需改叙事为 "NTP magnitude dominance is the universal mechanism;
88	    gradient direction geometry varies by model but is inconsequential in both cases—on
89	    Qwen because PCGrad removes conflict without changing outcomes, on Llama because
90	    conflict doesn''t exist." 这让 PCGrad section 的 weight 降低，审稿人可能认为 ''PCGrad ablation
91	    on one model is insufficient evidence for a general claim about gradient conflict
92	    irrelevance.''
93	
94	    '
95	- name: Expanded Eval Set (200 Conversations)
96	  plan_id: plan_020
97	  description: 'TF eval 从 50 扩展到 200 conversations（idx>=7000 from UltraChat），提高 bootstrap
98	    CI 统计功效。 AR eval 保持 N=50（效应量极端，无需扩展）。
99	
100	    '
101	  expected_results:
102	    tf_n200_tg_gar_ours: 0.501
103	    tf_n200_tg_gar_ours_ci95:
104	    - 0.488
105	    - 0.514
106	    tf_n200_lo_gar_ours: 0.497
107	    tf_n200_lo_gar_ours_ci95:
108	    - 0.484
109	    - 0.51
110	    tf_n200_ug_gar_ours: 0.503
111	    tf_n200_ug_gar_ours_ci95:
112	    - 0.49
113	    - 0.516
114	    tf_n200_tg_minus_lo_ci95:
115	    - -0.008
116	    - 0.016
117	    tf_n200_tg_minus_lo_p: 0.52
118	    tf_n200_ppl_tg: 2.78
119	    tf_n200_ppl_lo: 2.78
120	    tf_n200_ppl_ug: 2.78
121	    tf_n200_base_gar_ours: 0.013
122	    ar_n50_unchanged: true
123	    gpu_hours: 1.5
124	  result_rationale: '扩展到 200 convs 后 CI 更窄但 TG-LO 差异仍包含 0（[-0.008, +0.016]），统计确认 gating
125	    zero-increment。但这只是 TF eval——审稿人关注 AR eval 不关注 TF。TF convergence 是 trivially expected，200
126	    conversations 只是让已知结论更精确。Worst case：per-conversation variance 暴露部分对话 TG GAR <
127	    LO GAR，让 gating 故事更 noisy。不产生新 insight， 不改变 paper score。审稿人可能说 ''N=200 for teacher-forcing
128	    is overkill; the real test is autoregressive where you only have N=50.''
129	
130	    '
131	  tables:
132	  - caption: 'TF Eval: N=50 vs N=200 Comparison'
133	    columns:
134	    - Variant
135	    - GAR-ours (N=50)
136	    - GAR-ours (N=200)
137	    - 95% CI (N=200)
138	    - PPL
139	    rows:
140	    - - TG v7
141	      - '0.504'
142	      - '0.501'
143	      - '[0.488, 0.514]'
144	      - '2.78'
145	    - - LoRA-only
146	      - '0.498'
147	      - '0.497'
148	      - '[0.484, 0.510]'
149	      - '2.78'
150	    - - UG
151	      - '0.505'
152	      - '0.503'
153	      - '[0.490, 0.516]'
154	      - '2.78'
155	    - - Base
156	      - '0.013'
157	      - '0.013'
158	      - '[0.010, 0.016]'
159	      - '4.34'
160	  - caption: Pairwise Differences (N=200, 95% Bootstrap CI)
161	    columns:
162	    - Comparison
163	    - Mean Diff
164	    - 95% CI
165	    - Contains 0?
166	    rows:
167	    - - TG - LO
168	      - '+0.004'
169	      - '[-0.008, +0.016]'
170	      - 'Yes'
171	    - - UG - LO
172	      - '+0.006'
173	      - '[-0.006, +0.018]'
174	      - 'Yes'
175	    - - TG - UG
176	      - '-0.002'
177	      - '[-0.014, +0.010]'
178	      - 'Yes'
179	  figures_description:
180	  - Per-conversation GAR violin plot (N=200)：三个训练变体高度重叠，约 15% 的对话中 TG < LO
181	  analysis: 'N=200 TF eval 在 worst case 下是 low-value experiment。确认 gating zero-increment
182	    但审稿人 不在意 TF regime。GPU 预算（1.5h）不高，可保留为 Appendix 但不应在 main text 突出。 不改变 paper 竞争力评估。
183	
184	    '
185	- name: λ_GAR Sensitivity Analysis
186	  plan_id: plan_022
187	  description: '训练 v7 with λ_GAR=10（1 epoch）和 λ_GAR=0.1（1 epoch），展示梯度竞争在不同 loss 权重下的表现。
188	
189	    '
190	  expected_results:
191	    lambda10_epoch1_ntp_loss: 1.05
192	    lambda10_epoch1_gar_loss: 0.015
193	    lambda10_epoch1_total_loss: 1.2
194	    lambda10_gate_mean: 0.82
195	    lambda10_gate_std: 0.12
196	    lambda10_gate_min: 0.45
197	    lambda10_ppl: 3.8
198	    lambda10_tf_gar_ours: 0.52
199	    lambda10_ar_gar_ours: 0.018
200	    lambda10_gap_ratio: 28.9
201	    lambda10_training_stable: false
202	    lambda10_ntp_ppl_degradation_pct: 36.7
203	    lambda01_epoch1_ntp_loss: 0.93
204	    lambda01_epoch1_gar_loss: 0.0003
205	    lambda01_gate_mean: 0.98
206	    lambda01_gate_std: 0.01
207	    lambda01_ppl: 2.78
208	    lambda01_tf_gar_ours: 0.49
209	    lambda01_ar_gar_ours: 0.015
210	    lambda01_gap_ratio: 32.7
211	    gpu_hours: 2.0
212	  result_rationale: 'λ=10：gate 远离 identity（mean 0.82，min 0.45），TF GAR 略高（0.52），但 PPL
213	    严重恶化（3.80， +36.7% vs v7 2.78）。关键：AR GAR 仍崩溃到 0.018，gap 28.9×——distribution shift
214	    不随 λ 改变。 Gate 学到更激进的 TF-context-specific attenuation，推理时这些模式无用。训练不稳定（loss oscillation）。
215	    λ=0.1：GAR 信号太弱（loss 0.0003），gate frozen near 1.0（std 0.01），等价 LoRA-only。Gap 更大
216	    32.7×。 两端都不改变核心结论。审稿人会说 ''obviously increasing λ hurts NTP and decreasing it removes
217	    GAR signal—this is a trivial sensitivity analysis that adds nothing new.'' 特别是
218	    worst case 下审稿人 已认为 negative result incremental，再加一个 ''trivial sensitivity'' 只会
219	    reinforce 这个印象。
220	
221	    '
222	  tables:
223	  - caption: 'λ_GAR Sensitivity: Impact on Training-Inference Gap'
224	    columns:
225	    - λ_GAR
226	    - TF GAR-ours
227	    - AR GAR-ours
228	    - Gap Ratio
229	    - PPL
230	    - Training Stable?
231	    rows:
232	    - - '0.1'
233	      - '0.49'
234	      - '0.015'
235	      - 32.7×
236	      - '2.78'
237	      - Yes (≈ LoRA-only)
238	    - - 1.0 (v7 default)
239	      - '0.50'
240	      - '0.016'
241	      - 31.3×
242	      - '2.78'
243	      - 'Yes'
244	    - - '10.0'
245	      - '0.52'
246	      - '0.018'
247	      - 28.9×
248	      - '3.80'
249	      - No (oscillation)
250	  figures_description:
251	  - Gate profile comparison (λ=0.1/1.0/10.0)：λ=10 显示 aggressive deep-layer attenuation（L3-L5
252	    ≈ 0.5），λ=0.1 flat at 1.0
253	  - Training loss curve (λ=10, 1 epoch)：NTP-GAR seesaw oscillation，未收敛
254	  analysis: 'λ sensitivity 在 worst case 下可放入 Appendix 但 paper value 极低。核心 takeaway（distribution
255	    shift independent of λ）是 correct 但 trivially expected。审稿人 ''this confirms what
256	    we already know—the problem is not hyperparameter tuning but fundamental distribution
257	    mismatch.'' 不给 novelty credit。 建议：仅在 Discussion 一句带过 ''λ sensitivity analysis
258	    (Appendix X) confirms gap independence from loss weighting''，不要展开讨论。
259	
260	    '
261	- name: TF vs AR Attention KL Divergence
262	  plan_id: plan_025
263	  description: '计算 per-head KL(P_TF || P_AR) 量化 attention distribution shift。 测试 GAR-relevant
264	    heads 是否显示更大 KL → exposure bias 的机制证据。
265	
266	    '
267	  expected_results:
268	    tg_mean_kl: 0.054
269	    base_mean_kl: 0.043
270	    tg_max_kl_layer: L23
271	    tg_max_kl_value: 0.15
272	    high_kl_layers: L9, L23-L27
273	    gate_kl_correlation: 0.11
274	    gate_kl_p_value: 0.18
275	    gar_relevant_heads_mean_kl: 0.072
276	    non_gar_relevant_heads_mean_kl: 0.048
277	    kl_ratio_gar_vs_nongar: 1.5
278	    n_conversations: 50
279	    n_heads_per_layer: 28
280	    n_layers: 28
281	    n_total_head_layer_pairs: 784
282	    gpu_hours: 0
283	  result_rationale: 'KL divergence 整体偏小（mean 0.054 nat），不到 0.1。虽然 GAR-relevant heads
284	    略高（0.072 vs 0.048）， ratio 仅 1.5×——不够 dramatic 来解释 8× GAR gap。Gate-KL correlation
285	    极弱（r=0.11, p=0.18 不显著）， 说明 gate 与 attention distribution shift 无关联——gate 未学到在
286	    high-shift layers 做更强干预。 High-KL layers（L23-L27）在深层，但与 gate attenuation 集中层不完全吻合（gate
287	    最低在 L3-L5）。 审稿人两个攻击角度：(1) "KL 0.054 解释不了 8× gap——一定有其他因素（error accumulation、 sequential
288	    compounding）你没测到"；(2) "gate-KL 无相关说明 gate 根本不 tracking the relevant signal"。 总体：提供
289	    weak supplementary evidence，但不能作为 independent contribution。
290	
291	    '
292	  tables:
293	  - caption: Per-Layer-Group Attention KL Divergence (TF→AR)
294	    columns:
295	    - Layer Group
296	    - Mean KL (TG)
297	    - Mean KL (Base)
298	    - Mean Gate Value
299	    rows:
300	    - - L0-L7 (shallow)
301	      - '0.032'
302	      - '0.029'
303	      - '0.94'
304	    - - L8-L15 (mid)
305	      - '0.048'
306	      - '0.039'
307	      - '0.93'
308	    - - L16-L23 (deep-mid)
309	      - '0.065'
310	      - '0.050'
311	      - '0.92'
312	    - - L24-L27 (deep)
313	      - '0.089'
314	      - '0.068'
315	      - '0.95'
316	  - caption: GAR-Relevant vs Non-Relevant Head KL
317	    columns:
318	    - Head Category
319	    - Mean KL
320	    - N heads
321	    - Interpretation
322	    rows:
323	    - - GAR-relevant (top-10% goal-attention)
324	      - '0.072'
325	      - '78'
326	      - Slightly higher shift
327	    - - Non-GAR-relevant
328	      - '0.048'
329	      - '706'
330	      - Background level
331	    - - Ratio
332	      - 1.50×
333	      - '-'
334	      - Weak selectivity signal
335	  figures_description:
336	  - Per-layer KL heatmap (28 layers × 28 heads)：scattered high-KL spots，无 clear systematic
337	    pattern
338	  - 'Scatter plot: gate value vs layer KL divergence, r=0.11, p=0.18 — no significant
339	    correlation'
340	  analysis: 'KL 分析在 worst case 下是 underwhelming supplementary evidence。0.054 mean
341	    KL 是 small effect， 不足以 standalone support distribution shift claim。作为 Appendix
342	    可保留（诚实报告），但 main text 不应过度强调。审稿人可能 ignore 或 attack："if KL is this small, maybe
343	    distribution shift isn''t really the mechanism—maybe it''s something else entirely
344	    that you haven''t measured." Worst case 下这部分损害论文更多（给审稿人攻击弹药）而非帮助。建议 Appendix only。
345	
346	    '
347	- name: Llama-3.1-8B Scheduled Sampling
348	  plan_id: plan_026
349	  description: '在 Llama-3.1-8B 上复现 SS 训练（time-scheduled sampling + GAR auxiliary loss），
350	    验证 gap 压缩是否跨模型泛化。若 Llama gap 同样压缩 → SS 是 general mitigation。
351	
352	    '
353	  expected_results:
354	    training_converged: true
355	    epochs_completed: 3
356	    total_steps: 3000
357	    wall_clock_hours: 10.5
358	    final_ntp_loss: 0.928
359	    final_gar_loss: 0.0012
360	    final_gate_mean: 0.92
361	    final_gate_std: 0.065
362	    ss_ratio_final: 0.5
363	    ss_steps_used: 5100
364	    tf_eval:
365	      gar_ours: 0.47
366	      gar_dongre: 0.35
367	      ppl: 2.6
368	      n_conversations: 50
369	    ar_eval_beta0:
370	      gar_ours: 0.04
371	      gar_ours_std: 0.03
372	      gar_dongre: 0.025
373	      ppl: 1.4
374	      n_conversations: 20
375	    ar_eval_beta3:
376	      gar_ours: 0.52
377	      ppl: 1.58
378	    ar_eval_beta5:
379	      gar_ours: 0.68
380	      ppl: 1.75
381	    gap_ratio_beta0: 11.75
382	    gap_ratio_vs_llama_tg: 0.74
383	    gap_ratio_vs_qwen_ss: Qwen 1.3× vs Llama 11.75×
384	    ss_independent_benefit_beta0: 0.01
385	  result_rationale: '这是 worst tier 的 defining failure point。Llama SS 训练正常收敛（loss 与
386	    Llama TG v7 comparable）， TF eval 显示 SS 确实学到 GAR pattern（TF GAR 0.47 ≈ Llama TG
387	    0.48）。但 AR eval β=0 仅 0.04， 远低于 Qwen SS 的 0.39。Gap ratio 11.75× 仍是 dramatic failure。
388	
389	    SS 在 Llama 上失败的可能机制： (1) Llama tokenizer 与 Qwen 不同（BPE vocab 128k vs 151k），model-generated
390	    text 的分布偏离 gold text 更远——SS 暴露的分布与推理分布仍不匹配。 (2) Llama 32 层 + 更深的 gate attenuation
391	    pattern（L25 gate 0.719）意味着 SS 需更长训练 才能 penetrate deeper layers。3 epochs 不够。 (3)
392	    Llama base GAR 更低（0.009 vs Qwen 0.019），从更低起点恢复更困难。 (4) Llama 在 SS step 上生成文本质量更低（更多
393	    hallucination/repetition），SS exposure 引入的分布 noise 大于 signal。
394	
395	    β=3/5 时 inference-time steering 仍有效（0.52, 0.68），但这是 steering 功劳而非 SS。 SS 在 Llama
396	    上的 independent value（β=0 增量 +0.01 over TG baseline 0.03）接近 0。
397	
398	    结论：SS 是 model-specific mitigation，不是 general solution。论文必须放弃 ''discover→diagnose→remedy''
399	    弧，SS 不能作为第 5 个 contribution。
400	
401	    '
402	  tables:
403	  - caption: Scheduled Sampling Cross-Model Comparison (β=0, AR eval)
404	    columns:
405	    - Model
406	    - SS TF GAR
407	    - SS AR GAR (β=0)
408	    - Gap Ratio
409	    - TG AR GAR (β=0)
410	    - SS Benefit
411	    rows:
412	    - - Qwen-2.5-7B (3-seed)
413	      - 0.498±0.004
414	      - 0.390±0.036
415	      - 1.28×
416	      - '0.064'
417	      - '+0.326'
418	    - - Llama-3.1-8B
419	      - '0.47'
420	      - '0.04'
421	      - 11.75×
422	      - '0.030'
423	      - '+0.010'
424	  - caption: Llama SS β-Sweep (AR eval, N=20)
425	    columns:
426	    - β
427	    - SS AR GAR
428	    - TG AR GAR (no SS)
429	    - SS Incremental
430	    - PPL
431	    rows:
432	    - - '0'
433	      - '0.040'
434	      - '0.030'
435	      - '+0.010'
436	      - '1.40'
437	    - - '3'
438	      - '0.520'
439	      - '0.556'
440	      - '-0.036'
441	      - '1.58'
442	    - - '5'
443	      - '0.680'
444	      - '0.727'
445	      - '-0.047'
446	      - '1.75'
447	  - caption: Llama TF Eval Comparison
448	    columns:
449	    - Variant
450	    - GAR-ours
451	    - GAR-Dongre
452	    - PPL
453	    rows:
454	    - - Base
455	      - '0.017'
456	      - '0.004'
457	      - '3.45'
458	    - - TG v7
459	      - '0.484'
460	      - '0.018'
461	      - '2.57'
462	    - - SS
463	      - '0.470'
464	      - '0.350'
465	      - '2.60'
466	  figures_description:
467	  - 'Cross-model SS gap comparison: Qwen bar (green, 1.3×) vs Llama bar (red, 11.75×)'
468	  - 'Llama SS training curve: TF GAR 正常上升，periodic AR checkpoints 始终 <0.05'
469	  - 'β-sweep overlay (Qwen SS vs Llama SS vs Llama TG): β=0 时 Llama SS ≈ Llama TG（SS
470	    无增量），β=5 时三者接近'
471	  analysis: 'Llama SS failure 是 worst tier 的 cascade trigger： (1) SS 不能作为论文第 5 个 contribution——cross-model
472	    failure 意味着 ''SS transfers to multi-turn transformer attention objectives'' 的
473	    claim 不成立（只在 1/2 模型上成立）。 (2) 论文必须放弃完整弧叙事。Title 不能暗示 recovery/remedy。 (3) SS 降级为
474	    Discussion 的 ''attempted mitigation, model-specific partial success''。 (4) 但 SS
475	    failure 本身有 diagnostic value：even explicitly exposing model to its own generation
476	    doesn''t bridge distribution shift on Llama → 更强的 impossibility signal。 (5) 与
477	    Dongre convergent evidence 更强：gating fails × 2 models + SS fails on Llama =  5/6
478	    intervention-model combinations fail（只有 Qwen SS 成功）。 (6) Paper score 从 best-case
479	    3.5 降到 2.5-3.0。Main conference 无望，Findings borderline。
480	
481	    '
482	- name: SS 3-Seed Validation (Qwen)
483	  plan_id: plan_027
484	  description: 'Qwen SS 3 seeds (s42/s123/s456) 的 AR eval with β=0,3,5，提供 mean±std。回应
485	    W7 单 seed 质疑。
486	
487	    '
488	  expected_results:
489	    tf_gar_ours:
490	      s42: 0.503
491	      s123: 0.495
492	      s456: 0.496
493	      mean: 0.498
494	      std: 0.004
495	    ar_beta0_gar:
496	      s42: 0.347
497	      s123: 0.4
498	      s456: 0.422
499	      mean: 0.39
500	      std: 0.036
501	      cv_pct: 9.2
502	    ar_beta3_gar:
503	      s42: 0.593
504	      s123: 0.59
505	      s456: 0.605
506	      mean: 0.596
507	      std: 0.008
508	    ar_beta5_gar:
509	      s42: 0.717
510	      s123: 0.717
511	      s456: 0.716
512	      mean: 0.717
513	      std: 0.001
514	    ppl_beta0:
515	      s42: 1.44
516	      s123: 1.441
517	      s456: 1.442
518	      mean: 1.441
519	      std: 0.001
520	    gap_ratio:
521	      s42: 1.45
522	      s123: 1.24
523	      s456: 1.18
524	      mean: 1.29
525	      range: '[1.18, 1.45]'
526	    s42_is_outlier_at_beta0: true
527	    n_ar_conversations_per_seed: 39
528	  result_rationale: '3-seed mean AR GAR β=0 = 0.390 在 worst 范围 [0.38, 0.45] 的下端。s42
529	    是明显 outlier （0.347 vs s123 0.400 / s456 0.422），std = 0.036，CV = 9.2%。
530	
531	    Worst case 审稿人攻击角度： (1) "CV 9.2% 对 main result 偏高——3 seeds 中 s42 远低于其他两个，说明结果对
532	    initialization 敏感。" (2) "s42 恰好是你 main paper 中展示的 seed，也是最差的——虽然不是 cherry-pick，但
533	    optics 不好。" (3) β=3/5 极稳定（std<0.01）说明 high-β steering 效果 robust，但 β=0 的 SS independent
534	    value 有 seed sensitivity。SS 真正的 independent contribution（β=0 without steering
535	    assist）不够 stable。 (4) 结合 Llama SS failure："3 seeds on one model proves nothing
536	    when the other model fails completely."
537	
538	    PPL 方差极小（±0.001），确认 SS 无 PPL cost。但 worst case 下审稿人不给 PPL neutrality credit。
539	
540	    '
541	  tables:
542	  - caption: SS 3-Seed AR Eval Results (Qwen-2.5-7B, N=39 valid conversations per
543	      seed)
544	    columns:
545	    - Metric
546	    - s42
547	    - s123
548	    - s456
549	    - Mean±Std
550	    rows:
551	    - - TF GAR-ours
552	      - '0.503'
553	      - '0.495'
554	      - '0.496'
555	      - 0.498±0.004
556	    - - AR GAR β=0
557	      - '0.347'
558	      - '0.400'
559	      - '0.422'
560	      - 0.390±0.036
561	    - - AR GAR β=3
562	      - '0.593'
563	      - '0.590'
564	      - '0.605'
565	      - 0.596±0.008
566	    - - AR GAR β=5
567	      - '0.717'
568	      - '0.717'
569	      - '0.716'
570	      - 0.717±0.001
571	    - - PPL β=0
572	      - '1.440'
573	      - '1.441'
574	      - '1.442'
575	      - 1.441±0.001
576	    - - Gap Ratio
577	      - 1.45×
578	      - 1.24×
579	      - 1.18×
580	      - 1.29±0.14
581	  figures_description:
582	  - 3-seed β-sweep with error bars：β=0 有 visible error bar（±0.036），β=3/5 error bars
583	    几乎不可见
584	  - Per-seed gap ratio bar chart：s42 1.45×（red）, s123 1.24×, s456 1.18×（green）
585	  analysis: '3-seed 在 worst case 下是 necessary but insufficient。W7 partially addressed（有
586	    variance estimate）， 但审稿人重心转移到 Llama failure。''You showed 3 seeds on the model
587	    where it works, but it completely fails on the other model. The 3-seed result
588	    is uninteresting because cross-model generalization is the real test, and you
589	    failed it.'' SS contribution 无论在 Qwen 上多稳定， 只要 Llama 失败就无法 claim generalizability。在
590	    worst tier 中 SS 从 contribution #5 移除， 3-seed 数据放 Appendix。
591	
592	    '
593	- name: Alternative GAR Definition Robustness
594	  plan_id: plan_028
595	  description: '4 种 token selection（last/all/first/goal-only）× 3 checkpoints（Base/TG/SS），
596	    测试 GAR 改善是否 robust across definitions。需 GPU re-eval（raw attention 未保存）。
597	
598	    '
599	  expected_results:
600	    base:
601	      last_token: 0.019
602	      all_token: 0.022
603	      first_token: 0.021
604	      goal_only: 0.015
605	    tg:
606	      last_token: 0.325
607	      all_token: 0.025
608	      first_token: 0.039
609	      goal_only: 0.018
610	    ss:
611	      last_token: 0.39
612	      all_token: 0.062
613	      first_token: 0.045
614	      goal_only: 0.03
615	    n_defs_tg_improves_clearly: 1
616	    n_defs_ss_improves_clearly: 1
617	    n_defs_ss_improves_marginally: 1
618	    improved_definition: last-token (ours)
619	    marginal_definition: all-token
620	    not_improved:
621	    - first-token
622	    - goal-only
623	    gpu_hours: 0.5
624	  result_rationale: 'Worst case：alternative_gar_defs_ss_improves 在 [0, 2] 范围内，取 1。
625	
626	    TG 只改善 last-token（0.325 vs base 0.019, 17×），all/first/goal-only 接近 baseline。 这说明
627	    TG 学到的 attention pattern 高度 position-specific：只对 assistant response 最后 一个 token
628	    的 goal attention 有效，对其他 response token positions 无效。
629	
630	    SS 同样主要改善 last-token（0.390），all-token 有 marginal 提升（0.062 vs 0.022, 2.8×） 但绝对值仍很低。First-token
631	    和 goal-only 基本无改善（2× within noise level）。
632	
633	    审稿人会用这个数据攻击 GAR metric 本身的 validity： (1) "GAR improvement is position-specific
634	    overfitting to last-token——不是真正改善了 goal attention"。 (2) "All-token GAR（最接近 Dongre
635	    定义）在 SS 后仍然很低（0.062），说明你的方法没有 真正 address Dongre 发现的问题"。 (3) W3 escalation 加剧：GAR
636	    作为代理指标的 validity 被质疑 + instruction retention r=0.2 太弱 + 换个 GAR 定义结果就消失 = triple
637	    weakness。
638	
639	    '
640	  tables:
641	  - caption: GAR Across Token Selection Definitions (AR eval, Qwen-2.5-7B)
642	    columns:
643	    - Token Selection
644	    - Base
645	    - TG v7
646	    - SS v8b
647	    - SS/Base Ratio
648	    - Clearly Improved?
649	    rows:
650	    - - Last-token (ours)
651	      - '0.019'
652	      - '0.325'
653	      - '0.390'
654	      - 20.5×
655	      - 'Yes'
656	    - - All-token (≈Dongre)
657	      - '0.022'
658	      - '0.025'
659	      - '0.062'
660	      - 2.8×
661	      - Marginal
662	    - - First-token
663	      - '0.021'
664	      - '0.039'
665	      - '0.045'
666	      - 2.1×
667	      - No (within noise)
668	    - - Goal-only tokens
669	      - '0.015'
670	      - '0.018'
671	      - '0.030'
672	      - 2.0×
673	      - No (within noise)
674	  figures_description:
675	  - 'Grouped bar chart: 4 definitions × 3 models. 只有 last-token 显示 dramatic SS improvement（tall
676	    green bar），其他三个定义 SS bar 几乎与 base 等高'
677	  analysis: 'Alternative GAR 分析在 worst case 下 damages the paper more than it helps。
678	    审稿人会认为 GAR 改善是 metric-specific artifact：只有特定的 last-token summary-position 定义下才有效果。这触发
679	    W3 escalation chain： (1) GAR 只对 last-token 有效 → metric fragility (2) Instruction
680	    retention r=0.2 → weak downstream correlation (3) Alternative definitions 无改善
681	    → ''what exactly are you measuring?'' 建议：在 worst case 叙事中将此放入 Appendix，main text
682	    仅一句提及 ''robustness analysis in Appendix X shows improvement concentrated on summary-position
683	    tokens, consistent with the training objective design.'' 不要让审稿人在 main text 看到这个弱点。
684	
685	    '
686	- name: SS 4th Seed (s789)
687	  plan_id: plan_029
688	  description: '第 4 个 Qwen SS seed 加强统计。ROI 低于 Llama SS 实验。
689	
690	    '
691	  expected_results:
692	    training:
693	      epochs_completed: 3
694	      wall_clock_hours: 6.5
695	      final_loss: 0.932
696	      final_gate_mean: 0.955
697	      ss_ratio_final: 0.5
698	    s789_tf_gar_ours: 0.5
699	    s789_ar_beta0_gar: 0.3
700	    s789_ar_beta3_gar: 0.58
701	    s789_ar_beta5_gar: 0.71
702	    s789_ppl_beta0: 1.442
703	    s789_gap_ratio: 1.67
704	    four_seed_stats:
705	      mean_beta0: 0.367
706	      std_beta0: 0.054
707	      cv_beta0_pct: 14.7
708	      range_beta0: '[0.300, 0.422]'
709	      mean_gap: 1.39
710	      std_gap: 0.22
711	    vs_three_seed:
712	      mean_delta: -0.023
713	      std_delta: 0.018
714	      cv_delta: 5.5
715	  result_rationale: 's789 是 worst case 中的 low outlier（AR GAR β=0 = 0.300，gap 1.67×）。4-seed
716	    mean 拉低到 0.367，std 从 0.036 升到 0.054，CV 从 9.2% 升到 14.7%。
717	
718	    更多 seeds 反而暴露更大 variance，削弱 SS 可靠性叙事： (1) "CV 14.7% 意味着 SS 的 independent value（β=0）高度依赖
719	    random initialization"。 (2) "4 seeds 范围 0.30-0.42，跨越了 ''meaningful improvement''
720	    和 ''marginal'' 的分界线"。 (3) "s789 gap 1.67× 接近 Qwen TG v7 的 gap regime，说明某些 seed
721	    下 SS 几乎不起作用"。
722	
723	    β=3/5 仍然稳定（0.580/0.710），因为 high-β steering 效果 dominant 且 seed-insensitive。 但 β=0
724	    是 SS 独立价值的唯一指标，14.7% CV 不够 convincing。
725	
726	    强烈建议 worst case 下 NOT running s789。3-seed 的 0.390±0.036 虽不完美但可接受。 第 4 个 seed 如果拉低
727	    mean 是自找麻烦。审稿人要求时可在 rebuttal 中补充。
728	
729	    '
730	  tables:
731	  - caption: SS 4-Seed Comparison (if run)
732	    columns:
733	    - Seed
734	    - AR GAR β=0
735	    - AR GAR β=3
736	    - AR GAR β=5
737	    - Gap Ratio
738	    rows:
739	    - - '42'
740	      - '0.347'
741	      - '0.593'
742	      - '0.717'
743	      - 1.45×
744	    - - '123'
745	      - '0.400'
746	      - '0.590'
747	      - '0.717'
748	      - 1.24×
749	    - - '456'
750	      - '0.422'
751	      - '0.605'
752	      - '0.716'
753	      - 1.18×
754	    - - '789'
755	      - '0.300'
756	      - '0.580'
757	      - '0.710'
758	      - 1.67×
759	    - - 4-seed Mean±Std
760	      - 0.367±0.054
761	      - 0.592±0.010
762	      - 0.715±0.003
763	      - 1.39±0.22
764	  figures_description:
765	  - '4-seed strip plot: s789 clearly below the cluster of s42/s123/s456, pulling distribution
766	    left'
767	  analysis: '在 worst case 下 s789 是 actively harmful data point。建议决策矩阵： - 如果 s789 ≥
768	    0.37：加入增强统计 → run - 如果 s789 < 0.35：拉低 mean + 增大 CV → do not report - Worst case
769	    s789 = 0.30 → definitely do not run / do not include 此实验应 deprioritize below Llama
770	    SS 和所有 P0/P1 实验。8 GPU-hours 可更好地用于 Llama SS 或 paper writing。
771	
772	    '
773	- name: Long Conversation Eval (>10 turns)
774	  plan_id: plan_030
775	  description: '测试 exposure bias gap 是否随对话长度增加而恶化。需从 UltraChat 筛选长对话。
776	
777	    '
778	  expected_results:
779	    turns_5:
780	      base_ar_gar: 0.02
781	      tg_ar_gar: 0.06
782	      ss_ar_gar: 0.42
783	      ss_benefit: 0.4
784	    turns_10:
785	      base_ar_gar: 0.01
786	      tg_ar_gar: 0.02
787	      ss_ar_gar: 0.38
788	      ss_benefit: 0.37
789	    turns_15:
790	      base_ar_gar: 0.006
791	      tg_ar_gar: 0.008
792	      ss_ar_gar: 0.22
793	      ss_benefit: 0.214
794	    turns_20:
795	      base_ar_gar: 0.004
796	      tg_ar_gar: 0.005
797	      ss_ar_gar: 0.12
798	      ss_benefit: 0.116
799	    ss_decay_rate_per_5turns_after_10: ~48%
800	    tg_base_convergence_at_turns: 15
801	    n_long_conversations: 10
802	    eval_tokens_per_conversation: ~8000-12000
803	    gpu_hours: 2.0
804	  result_rationale: 'SS 在 ≤10 turns 维持 0.38-0.42 AR GAR（与 3-seed mean 一致），但 15 turns
805	    后急剧下降到 0.22，20 turns 降到 0.12。每 5 turns 衰减约 48%。
806	
807	    机制推测：SS 训练数据中 model-generated context 比例线性递增（scheduled），但长对话中 error accumulation
808	    是 super-linear——每个 turn 的小偏差在后续 turns 被 compound。SS 暴露 的训练分布（线性 mix）与 20-turn
809	    推理分布（exponential error accumulation）仍有 gap。
810	
811	    审稿人 devastating critique： (1) "SS 只在短对话（≤10 turns）有效，但 GAR 退化本身就是长对话问题（Dongre
812	    测了 50 turns） ——你的 mitigation 恰好在最需要的地方失效。" (2) "你论文的 motivation 来自 Dongre 的 50-turn
813	    scenario，但你的 fix 在 15+ turns 就崩溃。" (3) "这与 scope limitation（W2/R1）结合——不仅 method-specific
814	    + model-specific，还 length-specific。"
815	
816	    TG 和 Base 在 15+ turns 已无区分（0.008 vs 0.006），再次确认 gating zero-increment 在长对话中成立。
817	
818	    但有一个 silver lining：SS 衰减曲线本身是有价值的 diagnostic insight——它量化了 SS 暴露 与真实推理分布的 gap
819	    如何随 conversation length 增长。可作为 Discussion 中 ''limitations of time-scheduled SS''
820	    的 empirical evidence。
821	
822	    '
823	  tables:
824	  - caption: GAR by Conversation Length (AR eval, Qwen-2.5-7B)
825	    columns:
826	    - Turns
827	    - Base
828	    - TG v7
829	    - SS v8b
830	    - SS Benefit vs Base
831	    rows:
832	    - - '5'
833	      - '0.020'
834	      - '0.060'
835	      - '0.420'
836	      - '+0.400'
837	    - - '10'
838	      - '0.010'
839	      - '0.020'
840	      - '0.380'
841	      - '+0.370'
842	    - - '15'
843	      - '0.006'
844	      - '0.008'
845	      - '0.220'
846	      - '+0.214'
847	    - - '20'
848	      - '0.004'
849	      - '0.005'
850	      - '0.120'
851	      - '+0.116'
852	  - caption: SS Effectiveness Decay
853	    columns:
854	    - Turn Range
855	    - SS AR GAR
856	    - Δ from turns 5
857	    - Decay (%)
858	    rows:
859	    - - 1-5
860	      - '0.420'
861	      - '-'
862	      - '-'
863	    - - 6-10
864	      - '0.380'
865	      - '-0.040'
866	      - 9.5%
867	    - - 11-15
868	      - '0.220'
869	      - '-0.200'
870	      - 47.6%
871	    - - 16-20
872	      - '0.120'
873	      - '-0.300'
874	      - 71.4%
875	  figures_description:
876	  - 'Line plot: GAR vs conversation length (Base/TG/SS). SS 在 turn 10 后加速下降（convex
877	    decay curve）'
878	  - SS benefit (SS - Base) vs turns：从 +0.40 at turn 5 衰减到 +0.12 at turn 20
879	  analysis: 'Long conversation eval 在 worst case 下提供 damaging but honest evidence。它表明
880	    SS mitigation 有 limited effective range（≤10 turns）。结合 Llama failure，SS 的 contribution
881	    变成 ''limited preliminary result on one model for short conversations only''——不够
882	    conference contribution。 建议：在 worst case diagnostic paper 中诚实报告此 limitation，放入
883	    Discussion §7.3 ''Scalability Limitations of Scheduled Sampling''。诚实承认 limitation
884	    可能 earn reviewer respect (''self-aware about limitations'')，比隐瞒好。但不改变 paper 从
885	    3.0 以上下降的趋势。
886	
887	    总体 worst case paper structure 调整： §5 Results 只含 main negative findings（NF1-NF3,
888	    gating zero-increment, cross-model replication）。 §6 Analysis 含 PCGrad causal exclusion
889	    + distribution shift。 §7 Discussion 含 SS attempted mitigation（Qwen partial success,
890	    Llama failure, length limitation） + Dongre convergent evidence + concrete future
891	    directions。 §8 Conclusion 重述 failure mode taxonomy 的系统分类学价值。 Expected Findings
892	    score: 2.5-3.0。'
893	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "678308d9-cc29-497c-876e-758db8f52d9c",
  "isSidechain": false,
  "promptId": "b2df24c2-fd3f-4fb8-afa6-a3945babf3db",
  "type": "user",
  "uuid": "027f4ba7-a902-41fa-b571-2c8080bd739d",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260524T081135/worst/review_context.yaml",
      "content": "narrative_guidance: '放弃 ''discover→diagnose→remedy'' 弧。Llama SS 失败（AR GAR β=0 ≈ 0.04，gap\n  ~12×）证明 SS 是 model-specific，不可泛化为 general mitigation。 Reframe 为纯 mechanistic diagnostic\n  paper。Title 改为 ''Why Auxiliary Attention Losses Fail Under Exposure Bias: A Multi-Model\n  Diagnostic Study''。 SS 从 Results 独立小节降级为 Discussion ''attempted mitigation''，承认\n  model-specific 局限。核心卖点转为 failure mode taxonomy （NF1 反向 turn conditioning + NF2 distribution\n  shift + NF3 干预强度不足）的系统分类学价值。 加强 PCGrad ''first empirical elimination of gradient\n  conflict hypothesis'' 叙事。加强 Dongre convergent failure evidence： 两种干预 × 两种模型 = 4\n  paths all fail on Llama。Introduction 结尾加 ''our negative results establish concrete\n  failure modes that future work must overcome''。Discussion 加 concrete next steps（data-dependent\n  SS schedule、curriculum exposure、inference-time only）。 仍冲 EMNLP Findings 2.5-3.0，靠\n  systematic rigor + cross-model replication + failure taxonomy。 审稿人 novelty objection\n  probability 0.7-1.0，fatal/severe concerns 3-5 remaining。\n\n  '\nimagined_experiments:\n- name: Llama Gradient Conflict Analysis\n  plan_id: plan_013\n  description: 'Llama-3.1-8B 上对 3 个 epoch checkpoint 计算 NTP-GAR 梯度 cos_sim 和 magnitude\n    ratio， 验证梯度方向冲突是否跨模型存在。\n\n    '\n  expected_results:\n    cos_sim_mean: 0.005\n    cos_sim_std: 0.07\n    neg_cos_sim_layers_pct: 53.1\n    pos_cos_sim_layers_pct: 46.9\n    mag_ratio_median: 25.7\n    mag_ratio_range: '[12.0, 45.0]'\n    epoch0_cos_sim: 0.012\n    epoch0_neg_layers_pct: 50.0\n    epoch1_cos_sim: 0.003\n    epoch1_neg_layers_pct: 53.1\n    epoch2_cos_sim: -0.001\n    epoch2_neg_layers_pct: 56.3\n    gpu_hours: 0.3\n  result_rationale: 'Worst case：Llama 梯度是 near-orthogonal（cos_sim ≈ 0），不是 conflict（cos_sim\n    < 0）。 neg_layers 53.1% 接近随机水平（50%），与 Qwen 的 67-79% 系统性 negative 模式不同。 这意味着两模型的梯度几何结构不一致——Qwen\n    有 mild conflict，Llama 没有。审稿人会说： \"gradient conflict 不是 cross-model mechanism，那你为什么用一整个\n    section（§6.2）讨论它？\" Magnitude ratio 25.7× 比 Qwen（7.5-14.7×）更极端，但方向冲突不存在使 PCGrad\n    在 Llama 上 没有可消除的 conflict。总体：数据支持 NTP 幅度主导，但削弱 gradient conflict 作为 universal\n    mechanism 的叙事。PCGrad 变成 \"only relevant on Qwen，model-specific finding\"。\n\n    '\n  tables:\n  - caption: Cross-Model Gradient Geometry Comparison\n    columns:\n    - Model\n    - cos_sim (mean)\n    - neg_layers (%)\n    - mag_ratio (median)\n    - Interpretation\n    rows:\n    - - Qwen-2.5-7B (ep0→ep2)\n      - '-0.062'\n      - '72.6'\n      - 11.9×\n      - Mild conflict + NTP dominance\n    - - Llama-3.1-8B (ep0→ep2)\n      - '+0.005'\n      - '53.1'\n      - 25.7×\n      - Orthogonal + extreme NTP dominance\n  - caption: Llama Per-Epoch Gradient Statistics\n    columns:\n    - Epoch\n    - cos_sim\n    - neg_layers (%)\n    - mag_ratio\n    rows:\n    - - '0'\n      - '+0.012'\n      - '50.0'\n      - '18.3'\n    - - '1'\n      - '+0.003'\n      - '53.1'\n      - '24.1'\n    - - '2'\n      - '-0.001'\n      - '56.3'\n      - '25.7'\n  figures_description:\n  - Per-layer cos_sim heatmap (Qwen vs Llama, 3 epochs)：Qwen 显示系统性 negative bias（蓝色主导），Llama\n    围绕 0 随机散布（蓝红交替）\n  - Magnitude ratio bar chart per layer：Llama L20-L31 尤其极端（30-45×），深层 NTP 幅度压制更强\n  analysis: 'PCGrad 叙事在 worst case 下从 \"cross-model causal exclusion\" 收缩为 \"Qwen-specific\n    observation\"。 Paper 需改叙事为 \"NTP magnitude dominance is the universal mechanism;\n    gradient direction geometry varies by model but is inconsequential in both cases—on\n    Qwen because PCGrad removes conflict without changing outcomes, on Llama because\n    conflict doesn''t exist.\" 这让 PCGrad section 的 weight 降低，审稿人可能认为 ''PCGrad ablation\n    on one model is insufficient evidence for a general claim about gradient conflict\n    irrelevance.''\n\n    '\n- name: Expanded Eval Set (200 Conversations)\n  plan_id: plan_020\n  description: 'TF eval 从 50 扩展到 200 conversations（idx>=7000 from UltraChat），提高 bootstrap\n    CI 统计功效。 AR eval 保持 N=50（效应量极端，无需扩展）。\n\n    '\n  expected_results:\n    tf_n200_tg_gar_ours: 0.501\n    tf_n200_tg_gar_ours_ci95:\n    - 0.488\n    - 0.514\n    tf_n200_lo_gar_ours: 0.497\n    tf_n200_lo_gar_ours_ci95:\n    - 0.484\n    - 0.51\n    tf_n200_ug_gar_ours: 0.503\n    tf_n200_ug_gar_ours_ci95:\n    - 0.49\n    - 0.516\n    tf_n200_tg_minus_lo_ci95:\n    - -0.008\n    - 0.016\n    tf_n200_tg_minus_lo_p: 0.52\n    tf_n200_ppl_tg: 2.78\n    tf_n200_ppl_lo: 2.78\n    tf_n200_ppl_ug: 2.78\n    tf_n200_base_gar_ours: 0.013\n    ar_n50_unchanged: true\n    gpu_hours: 1.5\n  result_rationale: '扩展到 200 convs 后 CI 更窄但 TG-LO 差异仍包含 0（[-0.008, +0.016]），统计确认 gating\n    zero-increment。但这只是 TF eval——审稿人关注 AR eval 不关注 TF。TF convergence 是 trivially expected，200\n    conversations 只是让已知结论更精确。Worst case：per-conversation variance 暴露部分对话 TG GAR <\n    LO GAR，让 gating 故事更 noisy。不产生新 insight， 不改变 paper score。审稿人可能说 ''N=200 for teacher-forcing\n    is overkill; the real test is autoregressive where you only have N=50.''\n\n    '\n  tables:\n  - caption: 'TF Eval: N=50 vs N=200 Comparison'\n    columns:\n    - Variant\n    - GAR-ours (N=50)\n    - GAR-ours (N=200)\n    - 95% CI (N=200)\n    - PPL\n    rows:\n    - - TG v7\n      - '0.504'\n      - '0.501'\n      - '[0.488, 0.514]'\n      - '2.78'\n    - - LoRA-only\n      - '0.498'\n      - '0.497'\n      - '[0.484, 0.510]'\n      - '2.78'\n    - - UG\n      - '0.505'\n      - '0.503'\n      - '[0.490, 0.516]'\n      - '2.78'\n    - - Base\n      - '0.013'\n      - '0.013'\n      - '[0.010, 0.016]'\n      - '4.34'\n  - caption: Pairwise Differences (N=200, 95% Bootstrap CI)\n    columns:\n    - Comparison\n    - Mean Diff\n    - 95% CI\n    - Contains 0?\n    rows:\n    - - TG - LO\n      - '+0.004'\n      - '[-0.008, +0.016]'\n      - 'Yes'\n    - - UG - LO\n      - '+0.006'\n      - '[-0.006, +0.018]'\n      - 'Yes'\n    - - TG - UG\n      - '-0.002'\n      - '[-0.014, +0.010]'\n      - 'Yes'\n  figures_description:\n  - Per-conversation GAR violin plot (N=200)：三个训练变体高度重叠，约 15% 的对话中 TG < LO\n  analysis: 'N=200 TF eval 在 worst case 下是 low-value experiment。确认 gating zero-increment\n    但审稿人 不在意 TF regime。GPU 预算（1.5h）不高，可保留为 Appendix 但不应在 main text 突出。 不改变 paper 竞争力评估。\n\n    '\n- name: λ_GAR Sensitivity Analysis\n  plan_id: plan_022\n  description: '训练 v7 with λ_GAR=10（1 epoch）和 λ_GAR=0.1（1 epoch），展示梯度竞争在不同 loss 权重下的表现。\n\n    '\n  expected_results:\n    lambda10_epoch1_ntp_loss: 1.05\n    lambda10_epoch1_gar_loss: 0.015\n    lambda10_epoch1_total_loss: 1.2\n    lambda10_gate_mean: 0.82\n    lambda10_gate_std: 0.12\n    lambda10_gate_min: 0.45\n    lambda10_ppl: 3.8\n    lambda10_tf_gar_ours: 0.52\n    lambda10_ar_gar_ours: 0.018\n    lambda10_gap_ratio: 28.9\n    lambda10_training_stable: false\n    lambda10_ntp_ppl_degradation_pct: 36.7\n    lambda01_epoch1_ntp_loss: 0.93\n    lambda01_epoch1_gar_loss: 0.0003\n    lambda01_gate_mean: 0.98\n    lambda01_gate_std: 0.01\n    lambda01_ppl: 2.78\n    lambda01_tf_gar_ours: 0.49\n    lambda01_ar_gar_ours: 0.015\n    lambda01_gap_ratio: 32.7\n    gpu_hours: 2.0\n  result_rationale: 'λ=10：gate 远离 identity（mean 0.82，min 0.45），TF GAR 略高（0.52），但 PPL\n    严重恶化（3.80， +36.7% vs v7 2.78）。关键：AR GAR 仍崩溃到 0.018，gap 28.9×——distribution shift\n    不随 λ 改变。 Gate 学到更激进的 TF-context-specific attenuation，推理时这些模式无用。训练不稳定（loss oscillation）。\n    λ=0.1：GAR 信号太弱（loss 0.0003），gate frozen near 1.0（std 0.01），等价 LoRA-only。Gap 更大\n    32.7×。 两端都不改变核心结论。审稿人会说 ''obviously increasing λ hurts NTP and decreasing it removes\n    GAR signal—this is a trivial sensitivity analysis that adds nothing new.'' 特别是\n    worst case 下审稿人 已认为 negative result incremental，再加一个 ''trivial sensitivity'' 只会\n    reinforce 这个印象。\n\n    '\n  tables:\n  - caption: 'λ_GAR Sensitivity: Impact on Training-Inference Gap'\n    columns:\n    - λ_GAR\n    - TF GAR-ours\n    - AR GAR-ours\n    - Gap Ratio\n    - PPL\n    - Training Stable?\n    rows:\n    - - '0.1'\n      - '0.49'\n      - '0.015'\n      - 32.7×\n      - '2.78'\n      - Yes (≈ LoRA-only)\n    - - 1.0 (v7 default)\n      - '0.50'\n      - '0.016'\n      - 31.3×\n      - '2.78'\n      - 'Yes'\n    - - '10.0'\n      - '0.52'\n      - '0.018'\n      - 28.9×\n      - '3.80'\n      - No (oscillation)\n  figures_description:\n  - Gate profile comparison (λ=0.1/1.0/10.0)：λ=10 显示 aggressive deep-layer attenuation（L3-L5\n    ≈ 0.5），λ=0.1 flat at 1.0\n  - Training loss curve (λ=10, 1 epoch)：NTP-GAR seesaw oscillation，未收敛\n  analysis: 'λ sensitivity 在 worst case 下可放入 Appendix 但 paper value 极低。核心 takeaway（distribution\n    shift independent of λ）是 correct 但 trivially expected。审稿人 ''this confirms what\n    we already know—the problem is not hyperparameter tuning but fundamental distribution\n    mismatch.'' 不给 novelty credit。 建议：仅在 Discussion 一句带过 ''λ sensitivity analysis\n    (Appendix X) confirms gap independence from loss weighting''，不要展开讨论。\n\n    '\n- name: TF vs AR Attention KL Divergence\n  plan_id: plan_025\n  description: '计算 per-head KL(P_TF || P_AR) 量化 attention distribution shift。 测试 GAR-relevant\n    heads 是否显示更大 KL → exposure bias 的机制证据。\n\n    '\n  expected_results:\n    tg_mean_kl: 0.054\n    base_mean_kl: 0.043\n    tg_max_kl_layer: L23\n    tg_max_kl_value: 0.15\n    high_kl_layers: L9, L23-L27\n    gate_kl_correlation: 0.11\n    gate_kl_p_value: 0.18\n    gar_relevant_heads_mean_kl: 0.072\n    non_gar_relevant_heads_mean_kl: 0.048\n    kl_ratio_gar_vs_nongar: 1.5\n    n_conversations: 50\n    n_heads_per_layer: 28\n    n_layers: 28\n    n_total_head_layer_pairs: 784\n    gpu_hours: 0\n  result_rationale: 'KL divergence 整体偏小（mean 0.054 nat），不到 0.1。虽然 GAR-relevant heads\n    略高（0.072 vs 0.048）， ratio 仅 1.5×——不够 dramatic 来解释 8× GAR gap。Gate-KL correlation\n    极弱（r=0.11, p=0.18 不显著）， 说明 gate 与 attention distribution shift 无关联——gate 未学到在\n    high-shift layers 做更强干预。 High-KL layers（L23-L27）在深层，但与 gate attenuation 集中层不完全吻合（gate\n    最低在 L3-L5）。 审稿人两个攻击角度：(1) \"KL 0.054 解释不了 8× gap——一定有其他因素（error accumulation、 sequential\n    compounding）你没测到\"；(2) \"gate-KL 无相关说明 gate 根本不 tracking the relevant signal\"。 总体：提供\n    weak supplementary evidence，但不能作为 independent contribution。\n\n    '\n  tables:\n  - caption: Per-Layer-Group Attention KL Divergence (TF→AR)\n    columns:\n    - Layer Group\n    - Mean KL (TG)\n    - Mean KL (Base)\n    - Mean Gate Value\n    rows:\n    - - L0-L7 (shallow)\n      - '0.032'\n      - '0.029'\n      - '0.94'\n    - - L8-L15 (mid)\n      - '0.048'\n      - '0.039'\n      - '0.93'\n    - - L16-L23 (deep-mid)\n      - '0.065'\n      - '0.050'\n      - '0.92'\n    - - L24-L27 (deep)\n      - '0.089'\n      - '0.068'\n      - '0.95'\n  - caption: GAR-Relevant vs Non-Relevant Head KL\n    columns:\n    - Head Category\n    - Mean KL\n    - N heads\n    - Interpretation\n    rows:\n    - - GAR-relevant (top-10% goal-attention)\n      - '0.072'\n      - '78'\n      - Slightly higher shift\n    - - Non-GAR-relevant\n      - '0.048'\n      - '706'\n      - Background level\n    - - Ratio\n      - 1.50×\n      - '-'\n      - Weak selectivity signal\n  figures_description:\n  - Per-layer KL heatmap (28 layers × 28 heads)：scattered high-KL spots，无 clear systematic\n    pattern\n  - 'Scatter plot: gate value vs layer KL divergence, r=0.11, p=0.18 — no significant\n    correlation'\n  analysis: 'KL 分析在 worst case 下是 underwhelming supplementary evidence。0.054 mean\n    KL 是 small effect， 不足以 standalone support distribution shift claim。作为 Appendix\n    可保留（诚实报告），但 main text 不应过度强调。审稿人可能 ignore 或 attack：\"if KL is this small, maybe\n    distribution shift isn''t really the mechanism—maybe it''s something else entirely\n    that you haven''t measured.\" Worst case 下这部分损害论文更多（给审稿人攻击弹药）而非帮助。建议 Appendix only。\n\n    '\n- name: Llama-3.1-8B Scheduled Sampling\n  plan_id: plan_026\n  description: '在 Llama-3.1-8B 上复现 SS 训练（time-scheduled sampling + GAR auxiliary loss），\n    验证 gap 压缩是否跨模型泛化。若 Llama gap 同样压缩 → SS 是 general mitigation。\n\n    '\n  expected_results:\n    training_converged: true\n    epochs_completed: 3\n    total_steps: 3000\n    wall_clock_hours: 10.5\n    final_ntp_loss: 0.928\n    final_gar_loss: 0.0012\n    final_gate_mean: 0.92\n    final_gate_std: 0.065\n    ss_ratio_final: 0.5\n    ss_steps_used: 5100\n    tf_eval:\n      gar_ours: 0.47\n      gar_dongre: 0.35\n      ppl: 2.6\n      n_conversations: 50\n    ar_eval_beta0:\n      gar_ours: 0.04\n      gar_ours_std: 0.03\n      gar_dongre: 0.025\n      ppl: 1.4\n      n_conversations: 20\n    ar_eval_beta3:\n      gar_ours: 0.52\n      ppl: 1.58\n    ar_eval_beta5:\n      gar_ours: 0.68\n      ppl: 1.75\n    gap_ratio_beta0: 11.75\n    gap_ratio_vs_llama_tg: 0.74\n    gap_ratio_vs_qwen_ss: Qwen 1.3× vs Llama 11.75×\n    ss_independent_benefit_beta0: 0.01\n  result_rationale: '这是 worst tier 的 defining failure point。Llama SS 训练正常收敛（loss 与\n    Llama TG v7 comparable）， TF eval 显示 SS 确实学到 GAR pattern（TF GAR 0.47 ≈ Llama TG\n    0.48）。但 AR eval β=0 仅 0.04， 远低于 Qwen SS 的 0.39。Gap ratio 11.75× 仍是 dramatic failure。\n\n    SS 在 Llama 上失败的可能机制： (1) Llama tokenizer 与 Qwen 不同（BPE vocab 128k vs 151k），model-generated\n    text 的分布偏离 gold text 更远——SS 暴露的分布与推理分布仍不匹配。 (2) Llama 32 层 + 更深的 gate attenuation\n    pattern（L25 gate 0.719）意味着 SS 需更长训练 才能 penetrate deeper layers。3 epochs 不够。 (3)\n    Llama base GAR 更低（0.009 vs Qwen 0.019），从更低起点恢复更困难。 (4) Llama 在 SS step 上生成文本质量更低（更多\n    hallucination/repetition），SS exposure 引入的分布 noise 大于 signal。\n\n    β=3/5 时 inference-time steering 仍有效（0.52, 0.68），但这是 steering 功劳而非 SS。 SS 在 Llama\n    上的 independent value（β=0 增量 +0.01 over TG baseline 0.03）接近 0。\n\n    结论：SS 是 model-specific mitigation，不是 general solution。论文必须放弃 ''discover→diagnose→remedy''\n    弧，SS 不能作为第 5 个 contribution。\n\n    '\n  tables:\n  - caption: Scheduled Sampling Cross-Model Comparison (β=0, AR eval)\n    columns:\n    - Model\n    - SS TF GAR\n    - SS AR GAR (β=0)\n    - Gap Ratio\n    - TG AR GAR (β=0)\n    - SS Benefit\n    rows:\n    - - Qwen-2.5-7B (3-seed)\n      - 0.498±0.004\n      - 0.390±0.036\n      - 1.28×\n      - '0.064'\n      - '+0.326'\n    - - Llama-3.1-8B\n      - '0.47'\n      - '0.04'\n      - 11.75×\n      - '0.030'\n      - '+0.010'\n  - caption: Llama SS β-Sweep (AR eval, N=20)\n    columns:\n    - β\n    - SS AR GAR\n    - TG AR GAR (no SS)\n    - SS Incremental\n    - PPL\n    rows:\n    - - '0'\n      - '0.040'\n      - '0.030'\n      - '+0.010'\n      - '1.40'\n    - - '3'\n      - '0.520'\n      - '0.556'\n      - '-0.036'\n      - '1.58'\n    - - '5'\n      - '0.680'\n      - '0.727'\n      - '-0.047'\n      - '1.75'\n  - caption: Llama TF Eval Comparison\n    columns:\n    - Variant\n    - GAR-ours\n    - GAR-Dongre\n    - PPL\n    rows:\n    - - Base\n      - '0.017'\n      - '0.004'\n      - '3.45'\n    - - TG v7\n      - '0.484'\n      - '0.018'\n      - '2.57'\n    - - SS\n      - '0.470'\n      - '0.350'\n      - '2.60'\n  figures_description:\n  - 'Cross-model SS gap comparison: Qwen bar (green, 1.3×) vs Llama bar (red, 11.75×)'\n  - 'Llama SS training curve: TF GAR 正常上升，periodic AR checkpoints 始终 <0.05'\n  - 'β-sweep overlay (Qwen SS vs Llama SS vs Llama TG): β=0 时 Llama SS ≈ Llama TG（SS\n    无增量），β=5 时三者接近'\n  analysis: 'Llama SS failure 是 worst tier 的 cascade trigger： (1) SS 不能作为论文第 5 个 contribution——cross-model\n    failure 意味着 ''SS transfers to multi-turn transformer attention objectives'' 的\n    claim 不成立（只在 1/2 模型上成立）。 (2) 论文必须放弃完整弧叙事。Title 不能暗示 recovery/remedy。 (3) SS 降级为\n    Discussion 的 ''attempted mitigation, model-specific partial success''。 (4) 但 SS\n    failure 本身有 diagnostic value：even explicitly exposing model to its own generation\n    doesn''t bridge distribution shift on Llama → 更强的 impossibility signal。 (5) 与\n    Dongre convergent evidence 更强：gating fails × 2 models + SS fails on Llama =  5/6\n    intervention-model combinations fail（只有 Qwen SS 成功）。 (6) Paper score 从 best-case\n    3.5 降到 2.5-3.0。Main conference 无望，Findings borderline。\n\n    '\n- name: SS 3-Seed Validation (Qwen)\n  plan_id: plan_027\n  description: 'Qwen SS 3 seeds (s42/s123/s456) 的 AR eval with β=0,3,5，提供 mean±std。回应\n    W7 单 seed 质疑。\n\n    '\n  expected_results:\n    tf_gar_ours:\n      s42: 0.503\n      s123: 0.495\n      s456: 0.496\n      mean: 0.498\n      std: 0.004\n    ar_beta0_gar:\n      s42: 0.347\n      s123: 0.4\n      s456: 0.422\n      mean: 0.39\n      std: 0.036\n      cv_pct: 9.2\n    ar_beta3_gar:\n      s42: 0.593\n      s123: 0.59\n      s456: 0.605\n      mean: 0.596\n      std: 0.008\n    ar_beta5_gar:\n      s42: 0.717\n      s123: 0.717\n      s456: 0.716\n      mean: 0.717\n      std: 0.001\n    ppl_beta0:\n      s42: 1.44\n      s123: 1.441\n      s456: 1.442\n      mean: 1.441\n      std: 0.001\n    gap_ratio:\n      s42: 1.45\n      s123: 1.24\n      s456: 1.18\n      mean: 1.29\n      range: '[1.18, 1.45]'\n    s42_is_outlier_at_beta0: true\n    n_ar_conversations_per_seed: 39\n  result_rationale: '3-seed mean AR GAR β=0 = 0.390 在 worst 范围 [0.38, 0.45] 的下端。s42\n    是明显 outlier （0.347 vs s123 0.400 / s456 0.422），std = 0.036，CV = 9.2%。\n\n    Worst case 审稿人攻击角度： (1) \"CV 9.2% 对 main result 偏高——3 seeds 中 s42 远低于其他两个，说明结果对\n    initialization 敏感。\" (2) \"s42 恰好是你 main paper 中展示的 seed，也是最差的——虽然不是 cherry-pick，但\n    optics 不好。\" (3) β=3/5 极稳定（std<0.01）说明 high-β steering 效果 robust，但 β=0 的 SS independent\n    value 有 seed sensitivity。SS 真正的 independent contribution（β=0 without steering\n    assist）不够 stable。 (4) 结合 Llama SS failure：\"3 seeds on one model proves nothing\n    when the other model fails completely.\"\n\n    PPL 方差极小（±0.001），确认 SS 无 PPL cost。但 worst case 下审稿人不给 PPL neutrality credit。\n\n    '\n  tables:\n  - caption: SS 3-Seed AR Eval Results (Qwen-2.5-7B, N=39 valid conversations per\n      seed)\n    columns:\n    - Metric\n    - s42\n    - s123\n    - s456\n    - Mean±Std\n    rows:\n    - - TF GAR-ours\n      - '0.503'\n      - '0.495'\n      - '0.496'\n      - 0.498±0.004\n    - - AR GAR β=0\n      - '0.347'\n      - '0.400'\n      - '0.422'\n      - 0.390±0.036\n    - - AR GAR β=3\n      - '0.593'\n      - '0.590'\n      - '0.605'\n      - 0.596±0.008\n    - - AR GAR β=5\n      - '0.717'\n      - '0.717'\n      - '0.716'\n      - 0.717±0.001\n    - - PPL β=0\n      - '1.440'\n      - '1.441'\n      - '1.442'\n      - 1.441±0.001\n    - - Gap Ratio\n      - 1.45×\n      - 1.24×\n      - 1.18×\n      - 1.29±0.14\n  figures_description:\n  - 3-seed β-sweep with error bars：β=0 有 visible error bar（±0.036），β=3/5 error bars\n    几乎不可见\n  - Per-seed gap ratio bar chart：s42 1.45×（red）, s123 1.24×, s456 1.18×（green）\n  analysis: '3-seed 在 worst case 下是 necessary but insufficient。W7 partially addressed（有\n    variance estimate）， 但审稿人重心转移到 Llama failure。''You showed 3 seeds on the model\n    where it works, but it completely fails on the other model. The 3-seed result\n    is uninteresting because cross-model generalization is the real test, and you\n    failed it.'' SS contribution 无论在 Qwen 上多稳定， 只要 Llama 失败就无法 claim generalizability。在\n    worst tier 中 SS 从 contribution #5 移除， 3-seed 数据放 Appendix。\n\n    '\n- name: Alternative GAR Definition Robustness\n  plan_id: plan_028\n  description: '4 种 token selection（last/all/first/goal-only）× 3 checkpoints（Base/TG/SS），\n    测试 GAR 改善是否 robust across definitions。需 GPU re-eval（raw attention 未保存）。\n\n    '\n  expected_results:\n    base:\n      last_token: 0.019\n      all_token: 0.022\n      first_token: 0.021\n      goal_only: 0.015\n    tg:\n      last_token: 0.325\n      all_token: 0.025\n      first_token: 0.039\n      goal_only: 0.018\n    ss:\n      last_token: 0.39\n      all_token: 0.062\n      first_token: 0.045\n      goal_only: 0.03\n    n_defs_tg_improves_clearly: 1\n    n_defs_ss_improves_clearly: 1\n    n_defs_ss_improves_marginally: 1\n    improved_definition: last-token (ours)\n    marginal_definition: all-token\n    not_improved:\n    - first-token\n    - goal-only\n    gpu_hours: 0.5\n  result_rationale: 'Worst case：alternative_gar_defs_ss_improves 在 [0, 2] 范围内，取 1。\n\n    TG 只改善 last-token（0.325 vs base 0.019, 17×），all/first/goal-only 接近 baseline。 这说明\n    TG 学到的 attention pattern 高度 position-specific：只对 assistant response 最后 一个 token\n    的 goal attention 有效，对其他 response token positions 无效。\n\n    SS 同样主要改善 last-token（0.390），all-token 有 marginal 提升（0.062 vs 0.022, 2.8×） 但绝对值仍很低。First-token\n    和 goal-only 基本无改善（2× within noise level）。\n\n    审稿人会用这个数据攻击 GAR metric 本身的 validity： (1) \"GAR improvement is position-specific\n    overfitting to last-token——不是真正改善了 goal attention\"。 (2) \"All-token GAR（最接近 Dongre\n    定义）在 SS 后仍然很低（0.062），说明你的方法没有 真正 address Dongre 发现的问题\"。 (3) W3 escalation 加剧：GAR\n    作为代理指标的 validity 被质疑 + instruction retention r=0.2 太弱 + 换个 GAR 定义结果就消失 = triple\n    weakness。\n\n    '\n  tables:\n  - caption: GAR Across Token Selection Definitions (AR eval, Qwen-2.5-7B)\n    columns:\n    - Token Selection\n    - Base\n    - TG v7\n    - SS v8b\n    - SS/Base Ratio\n    - Clearly Improved?\n    rows:\n    - - Last-token (ours)\n      - '0.019'\n      - '0.325'\n      - '0.390'\n      - 20.5×\n      - 'Yes'\n    - - All-token (≈Dongre)\n      - '0.022'\n      - '0.025'\n      - '0.062'\n      - 2.8×\n      - Marginal\n    - - First-token\n      - '0.021'\n      - '0.039'\n      - '0.045'\n      - 2.1×\n      - No (within noise)\n    - - Goal-only tokens\n      - '0.015'\n      - '0.018'\n      - '0.030'\n      - 2.0×\n      - No (within noise)\n  figures_description:\n  - 'Grouped bar chart: 4 definitions × 3 models. 只有 last-token 显示 dramatic SS improvement（tall\n    green bar），其他三个定义 SS bar 几乎与 base 等高'\n  analysis: 'Alternative GAR 分析在 worst case 下 damages the paper more than it helps。\n    审稿人会认为 GAR 改善是 metric-specific artifact：只有特定的 last-token summary-position 定义下才有效果。这触发\n    W3 escalation chain： (1) GAR 只对 last-token 有效 → metric fragility (2) Instruction\n    retention r=0.2 → weak downstream correlation (3) Alternative definitions 无改善\n    → ''what exactly are you measuring?'' 建议：在 worst case 叙事中将此放入 Appendix，main text\n    仅一句提及 ''robustness analysis in Appendix X shows improvement concentrated on summary-position\n    tokens, consistent with the training objective design.'' 不要让审稿人在 main text 看到这个弱点。\n\n    '\n- name: SS 4th Seed (s789)\n  plan_id: plan_029\n  description: '第 4 个 Qwen SS seed 加强统计。ROI 低于 Llama SS 实验。\n\n    '\n  expected_results:\n    training:\n      epochs_completed: 3\n      wall_clock_hours: 6.5\n      final_loss: 0.932\n      final_gate_mean: 0.955\n      ss_ratio_final: 0.5\n    s789_tf_gar_ours: 0.5\n    s789_ar_beta0_gar: 0.3\n    s789_ar_beta3_gar: 0.58\n    s789_ar_beta5_gar: 0.71\n    s789_ppl_beta0: 1.442\n    s789_gap_ratio: 1.67\n    four_seed_stats:\n      mean_beta0: 0.367\n      std_beta0: 0.054\n      cv_beta0_pct: 14.7\n      range_beta0: '[0.300, 0.422]'\n      mean_gap: 1.39\n      std_gap: 0.22\n    vs_three_seed:\n      mean_delta: -0.023\n      std_delta: 0.018\n      cv_delta: 5.5\n  result_rationale: 's789 是 worst case 中的 low outlier（AR GAR β=0 = 0.300，gap 1.67×）。4-seed\n    mean 拉低到 0.367，std 从 0.036 升到 0.054，CV 从 9.2% 升到 14.7%。\n\n    更多 seeds 反而暴露更大 variance，削弱 SS 可靠性叙事： (1) \"CV 14.7% 意味着 SS 的 independent value（β=0）高度依赖\n    random initialization\"。 (2) \"4 seeds 范围 0.30-0.42，跨越了 ''meaningful improvement''\n    和 ''marginal'' 的分界线\"。 (3) \"s789 gap 1.67× 接近 Qwen TG v7 的 gap regime，说明某些 seed\n    下 SS 几乎不起作用\"。\n\n    β=3/5 仍然稳定（0.580/0.710），因为 high-β steering 效果 dominant 且 seed-insensitive。 但 β=0\n    是 SS 独立价值的唯一指标，14.7% CV 不够 convincing。\n\n    强烈建议 worst case 下 NOT running s789。3-seed 的 0.390±0.036 虽不完美但可接受。 第 4 个 seed 如果拉低\n    mean 是自找麻烦。审稿人要求时可在 rebuttal 中补充。\n\n    '\n  tables:\n  - caption: SS 4-Seed Comparison (if run)\n    columns:\n    - Seed\n    - AR GAR β=0\n    - AR GAR β=3\n    - AR GAR β=5\n    - Gap Ratio\n    rows:\n    - - '42'\n      - '0.347'\n      - '0.593'\n      - '0.717'\n      - 1.45×\n    - - '123'\n      - '0.400'\n      - '0.590'\n      - '0.717'\n      - 1.24×\n    - - '456'\n      - '0.422'\n      - '0.605'\n      - '0.716'\n      - 1.18×\n    - - '789'\n      - '0.300'\n      - '0.580'\n      - '0.710'\n      - 1.67×\n    - - 4-seed Mean±Std\n      - 0.367±0.054\n      - 0.592±0.010\n      - 0.715±0.003\n      - 1.39±0.22\n  figures_description:\n  - '4-seed strip plot: s789 clearly below the cluster of s42/s123/s456, pulling distribution\n    left'\n  analysis: '在 worst case 下 s789 是 actively harmful data point。建议决策矩阵： - 如果 s789 ≥\n    0.37：加入增强统计 → run - 如果 s789 < 0.35：拉低 mean + 增大 CV → do not report - Worst case\n    s789 = 0.30 → definitely do not run / do not include 此实验应 deprioritize below Llama\n    SS 和所有 P0/P1 实验。8 GPU-hours 可更好地用于 Llama SS 或 paper writing。\n\n    '\n- name: Long Conversation Eval (>10 turns)\n  plan_id: plan_030\n  description: '测试 exposure bias gap 是否随对话长度增加而恶化。需从 UltraChat 筛选长对话。\n\n    '\n  expected_results:\n    turns_5:\n      base_ar_gar: 0.02\n      tg_ar_gar: 0.06\n      ss_ar_gar: 0.42\n      ss_benefit: 0.4\n    turns_10:\n      base_ar_gar: 0.01\n      tg_ar_gar: 0.02\n      ss_ar_gar: 0.38\n      ss_benefit: 0.37\n    turns_15:\n      base_ar_gar: 0.006\n      tg_ar_gar: 0.008\n      ss_ar_gar: 0.22\n      ss_benefit: 0.214\n    turns_20:\n      base_ar_gar: 0.004\n      tg_ar_gar: 0.005\n      ss_ar_gar: 0.12\n      ss_benefit: 0.116\n    ss_decay_rate_per_5turns_after_10: ~48%\n    tg_base_convergence_at_turns: 15\n    n_long_conversations: 10\n    eval_tokens_per_conversation: ~8000-12000\n    gpu_hours: 2.0\n  result_rationale: 'SS 在 ≤10 turns 维持 0.38-0.42 AR GAR（与 3-seed mean 一致），但 15 turns\n    后急剧下降到 0.22，20 turns 降到 0.12。每 5 turns 衰减约 48%。\n\n    机制推测：SS 训练数据中 model-generated context 比例线性递增（scheduled），但长对话中 error accumulation\n    是 super-linear——每个 turn 的小偏差在后续 turns 被 compound。SS 暴露 的训练分布（线性 mix）与 20-turn\n    推理分布（exponential error accumulation）仍有 gap。\n\n    审稿人 devastating critique： (1) \"SS 只在短对话（≤10 turns）有效，但 GAR 退化本身就是长对话问题（Dongre\n    测了 50 turns） ——你的 mitigation 恰好在最需要的地方失效。\" (2) \"你论文的 motivation 来自 Dongre 的 50-turn\n    scenario，但你的 fix 在 15+ turns 就崩溃。\" (3) \"这与 scope limitation（W2/R1）结合——不仅 method-specific\n    + model-specific，还 length-specific。\"\n\n    TG 和 Base 在 15+ turns 已无区分（0.008 vs 0.006），再次确认 gating zero-increment 在长对话中成立。\n\n    但有一个 silver lining：SS 衰减曲线本身是有价值的 diagnostic insight——它量化了 SS 暴露 与真实推理分布的 gap\n    如何随 conversation length 增长。可作为 Discussion 中 ''limitations of time-scheduled SS''\n    的 empirical evidence。\n\n    '\n  tables:\n  - caption: GAR by Conversation Length (AR eval, Qwen-2.5-7B)\n    columns:\n    - Turns\n    - Base\n    - TG v7\n    - SS v8b\n    - SS Benefit vs Base\n    rows:\n    - - '5'\n      - '0.020'\n      - '0.060'\n      - '0.420'\n      - '+0.400'\n    - - '10'\n      - '0.010'\n      - '0.020'\n      - '0.380'\n      - '+0.370'\n    - - '15'\n      - '0.006'\n      - '0.008'\n      - '0.220'\n      - '+0.214'\n    - - '20'\n      - '0.004'\n      - '0.005'\n      - '0.120'\n      - '+0.116'\n  - caption: SS Effectiveness Decay\n    columns:\n    - Turn Range\n    - SS AR GAR\n    - Δ from turns 5\n    - Decay (%)\n    rows:\n    - - 1-5\n      - '0.420'\n      - '-'\n      - '-'\n    - - 6-10\n      - '0.380'\n      - '-0.040'\n      - 9.5%\n    - - 11-15\n      - '0.220'\n      - '-0.200'\n      - 47.6%\n    - - 16-20\n      - '0.120'\n      - '-0.300'\n      - 71.4%\n  figures_description:\n  - 'Line plot: GAR vs conversation length (Base/TG/SS). SS 在 turn 10 后加速下降（convex\n    decay curve）'\n  - SS benefit (SS - Base) vs turns：从 +0.40 at turn 5 衰减到 +0.12 at turn 20\n  analysis: 'Long conversation eval 在 worst case 下提供 damaging but honest evidence。它表明\n    SS mitigation 有 limited effective range（≤10 turns）。结合 Llama failure，SS 的 contribution\n    变成 ''limited preliminary result on one model for short conversations only''——不够\n    conference contribution。 建议：在 worst case diagnostic paper 中诚实报告此 limitation，放入\n    Discussion §7.3 ''Scalability Limitations of Scheduled Sampling''。诚实承认 limitation\n    可能 earn reviewer respect (''self-aware about limitations'')，比隐瞒好。但不改变 paper 从\n    3.0 以上下降的趋势。\n\n    总体 worst case paper structure 调整： §5 Results 只含 main negative findings（NF1-NF3,\n    gating zero-increment, cross-model replication）。 §6 Analysis 含 PCGrad causal exclusion\n    + distribution shift。 §7 Discussion 含 SS attempted mitigation（Qwen partial success,\n    Llama failure, length limitation） + Dongre convergent evidence + concrete future\n    directions。 §8 Conclusion 重述 failure mode taxonomy 的系统分类学价值。 Expected Findings\n    score: 2.5-3.0。'\n",
      "numLines": 893,
      "startLine": 1,
      "totalLines": 893
    }
  },
  "sourceToolAssistantUUID": "678308d9-cc29-497c-876e-758db8f52d9c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "ddd5074c-2b8b-40c6-b29f-f44ff9f131a7",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 14_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[DREAM Review Director] dream_id=20260524T081135 | review_mode=simple | review_visible=True PDF: /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/…",
  "leafUuid": "027f4ba7-a902-41fa-b571-2c8080bd739d",
  "sessionId": "ddd5074c-2b8b-40c6-b29f-f44ff9f131a7"
}
```

---

### Runtime record

_source line 15_

```json
{
  "type": "ai-title",
  "aiTitle": "Review residual gating paper for EMNLP",
  "sessionId": "ddd5074c-2b8b-40c6-b29f-f44ff9f131a7"
}
```

---

### Assistant

_source line 16 · 2026-05-24T09:12:53.433Z_

<details><summary>Logged reasoning block</summary>

```text
Now let me read the PDF in parts.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "027f4ba7-a902-41fa-b571-2c8080bd739d",
  "isSidechain": false,
  "requestId": "req_011CbM8snEbkcGEX8LKc4YUu",
  "type": "assistant",
  "uuid": "73a79f67-0795-4124-8384-65e2473a212f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "ddd5074c-2b8b-40c6-b29f-f44ff9f131a7",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MamEGHYAg1NsPFKZwYCQmk",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15156,
      "cache_read_input_tokens": 25208,
      "output_tokens": 278,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 15156,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 278,
          "cache_read_input_tokens": 25208,
          "cache_creation_input_tokens": 15156,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 15156
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

_source line 17 · 2026-05-24T09:12:54.066Z_

读取 PDF 论文内容。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "73a79f67-0795-4124-8384-65e2473a212f",
  "isSidechain": false,
  "requestId": "req_011CbM8snEbkcGEX8LKc4YUu",
  "type": "assistant",
  "uuid": "a500ddd6-dca1-424b-a346-49042a86c893",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "ddd5074c-2b8b-40c6-b29f-f44ff9f131a7",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MamEGHYAg1NsPFKZwYCQmk",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15156,
      "cache_read_input_tokens": 25208,
      "output_tokens": 278,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 15156,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 278,
          "cache_read_input_tokens": 25208,
          "cache_creation_input_tokens": 15156,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 15156
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

_source line 18 · 2026-05-24T09:12:57.417Z_

<details open><summary>🔧 Tool call — Read · `toolu_01MTPuAYPNd3DWb4DZrToB6e`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260524T081135/worst/review_input_f5f46a62.pdf",
  "pages": "1-7"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a500ddd6-dca1-424b-a346-49042a86c893",
  "isSidechain": false,
  "requestId": "req_011CbM8snEbkcGEX8LKc4YUu",
  "type": "assistant",
  "uuid": "45d6f42e-e729-4306-9198-91fea8c1df27",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "ddd5074c-2b8b-40c6-b29f-f44ff9f131a7",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MamEGHYAg1NsPFKZwYCQmk",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15156,
      "cache_read_input_tokens": 25208,
      "output_tokens": 278,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 15156,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 278,
          "cache_read_input_tokens": 25208,
          "cache_creation_input_tokens": 15156,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 15156
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

_source line 19 · 2026-05-24T09:12:57.714Z_

<details><summary>↩ Tool result · `toolu_01MTPuAYPNd3DWb4DZrToB6e`</summary>

```text
PDF pages extracted: 7 page(s) from /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260524T081135/worst/review_input_f5f46a62.pdf (185KB)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "45d6f42e-e729-4306-9198-91fea8c1df27",
  "isSidechain": false,
  "promptId": "b2df24c2-fd3f-4fb8-afa6-a3945babf3db",
  "type": "user",
  "uuid": "b1b8c1a5-f9fb-42a2-b4f0-47062a61f711",
  "toolUseResult": {
    "type": "parts",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260524T081135/worst/review_input_f5f46a62.pdf",
      "originalSize": 189488,
      "outputDir": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-turn-residual-gating/ddd5074c-2b8b-40c6-b29f-f44ff9f131a7/tool-results/pdf-070ecb35-544b-4519-ae74-639d526ac663",
      "count": 7
    }
  },
  "sourceToolAssistantUUID": "45d6f42e-e729-4306-9198-91fea8c1df27",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "ddd5074c-2b8b-40c6-b29f-f44ff9f131a7",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

## Round 2

5 recorded events

### User

_source line 20 · 2026-05-24T09:12:57.712Z_

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
  "parentUuid": "b1b8c1a5-f9fb-42a2-b4f0-47062a61f711",
  "isSidechain": false,
  "promptId": "b2df24c2-fd3f-4fb8-afa6-a3945babf3db",
  "type": "user",
  "isMeta": true,
  "uuid": "c6351e0c-532c-432f-81e6-578aff81a4b3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "ddd5074c-2b8b-40c6-b29f-f44ff9f131a7",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-24T09:12:57.981Z_

<details open><summary>🔧 Tool call — Read · `toolu_015fZp7nyaBjPuYLWCGr74jE`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260524T081135/worst/review_input_f5f46a62.pdf",
  "pages": "8-14"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c6351e0c-532c-432f-81e6-578aff81a4b3",
  "isSidechain": false,
  "requestId": "req_011CbM8snEbkcGEX8LKc4YUu",
  "type": "assistant",
  "uuid": "d346f348-55d9-4a68-8fd0-38f408b1f7e8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "ddd5074c-2b8b-40c6-b29f-f44ff9f131a7",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MamEGHYAg1NsPFKZwYCQmk",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15156,
      "cache_read_input_tokens": 25208,
      "output_tokens": 278,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 15156,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 278,
          "cache_read_input_tokens": 25208,
          "cache_creation_input_tokens": 15156,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 15156
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

_source line 22_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[DREAM Review Director] dream_id=20260524T081135 | review_mode=simple | review_visible=True PDF: /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/…",
  "leafUuid": "d346f348-55d9-4a68-8fd0-38f408b1f7e8",
  "sessionId": "ddd5074c-2b8b-40c6-b29f-f44ff9f131a7"
}
```

---

### Runtime record

_source line 23_

```json
{
  "type": "ai-title",
  "aiTitle": "Review residual gating paper for EMNLP",
  "sessionId": "ddd5074c-2b8b-40c6-b29f-f44ff9f131a7"
}
```

---

### Tool result

_source line 24 · 2026-05-24T09:12:58.236Z_

<details><summary>↩ Tool result · `toolu_015fZp7nyaBjPuYLWCGr74jE`</summary>

```text
PDF pages extracted: 7 page(s) from /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260524T081135/worst/review_input_f5f46a62.pdf (185KB)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d346f348-55d9-4a68-8fd0-38f408b1f7e8",
  "isSidechain": false,
  "promptId": "b2df24c2-fd3f-4fb8-afa6-a3945babf3db",
  "type": "user",
  "uuid": "bd6acc6a-cc36-4543-a108-1396723e5b02",
  "toolUseResult": {
    "type": "parts",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260524T081135/worst/review_input_f5f46a62.pdf",
      "originalSize": 189488,
      "outputDir": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-turn-residual-gating/ddd5074c-2b8b-40c6-b29f-f44ff9f131a7/tool-results/pdf-f44bedcc-3023-44e5-acef-000a917e31f2",
      "count": 7
    }
  },
  "sourceToolAssistantUUID": "d346f348-55d9-4a68-8fd0-38f408b1f7e8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "ddd5074c-2b8b-40c6-b29f-f44ff9f131a7",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

## Round 3

22 recorded events

### User

_source line 25 · 2026-05-24T09:12:58.234Z_

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
  "parentUuid": "bd6acc6a-cc36-4543-a108-1396723e5b02",
  "isSidechain": false,
  "promptId": "b2df24c2-fd3f-4fb8-afa6-a3945babf3db",
  "type": "user",
  "isMeta": true,
  "uuid": "98a64b66-7d32-4507-9723-8e6dc42bd0d0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "ddd5074c-2b8b-40c6-b29f-f44ff9f131a7",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 26_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[DREAM Review Director] dream_id=20260524T081135 | review_mode=simple | review_visible=True PDF: /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/…",
  "leafUuid": "bd6acc6a-cc36-4543-a108-1396723e5b02",
  "sessionId": "ddd5074c-2b8b-40c6-b29f-f44ff9f131a7"
}
```

---

### Runtime record

_source line 27_

```json
{
  "type": "ai-title",
  "aiTitle": "Review residual gating paper for EMNLP",
  "sessionId": "ddd5074c-2b8b-40c6-b29f-f44ff9f131a7"
}
```

---

### Assistant

_source line 28 · 2026-05-24T09:13:10.627Z_

<details><summary>Logged reasoning block</summary>

```text
I've now read the full paper and the review context. Let me now dispatch a single reviewer agent to conduct the full review, as per the `dream-review-simple` skill (1 Reviewer, skip cross-sharing and convergence steps).

Let me compose a comprehensive review prompt for the reviewer agent, then collect the review and submit it via `submit_dream_review_report`.

First, let me load the tool schema for `submit_dream_review_report`.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "98a64b66-7d32-4507-9723-8e6dc42bd0d0",
  "isSidechain": false,
  "requestId": "req_011CbM8toqce5Mg75YEGyVWP",
  "type": "assistant",
  "uuid": "4760a00c-83f8-4a07-9dcf-319849b49633",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "ddd5074c-2b8b-40c6-b29f-f44ff9f131a7",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012CYBig6hYnoSdcozu3n7S8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 17890,
      "cache_read_input_tokens": 40364,
      "output_tokens": 3185,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 17890,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 3185,
          "cache_read_input_tokens": 40364,
          "cache_creation_input_tokens": 17890,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 17890
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

_source line 29 · 2026-05-24T09:13:11.756Z_

论文已读完。派出 Reviewer 进行盲审。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4760a00c-83f8-4a07-9dcf-319849b49633",
  "isSidechain": false,
  "requestId": "req_011CbM8toqce5Mg75YEGyVWP",
  "type": "assistant",
  "uuid": "9203f7fb-0540-415a-84ec-8987a6a2b008",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "ddd5074c-2b8b-40c6-b29f-f44ff9f131a7",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012CYBig6hYnoSdcozu3n7S8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 17890,
      "cache_read_input_tokens": 40364,
      "output_tokens": 3185,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 17890,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 3185,
          "cache_read_input_tokens": 40364,
          "cache_creation_input_tokens": 17890,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 17890
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

_source line 30 · 2026-05-24T09:13:12.237Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01HdFPYm9ZJTh4BLnRtdhAEg`</summary>

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
  "parentUuid": "9203f7fb-0540-415a-84ec-8987a6a2b008",
  "isSidechain": false,
  "requestId": "req_011CbM8toqce5Mg75YEGyVWP",
  "type": "assistant",
  "uuid": "f4f409c6-f1ca-4945-81ad-238d20c57ca0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "ddd5074c-2b8b-40c6-b29f-f44ff9f131a7",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012CYBig6hYnoSdcozu3n7S8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 17890,
      "cache_read_input_tokens": 40364,
      "output_tokens": 3185,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 17890,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 3185,
          "cache_read_input_tokens": 40364,
          "cache_creation_input_tokens": 17890,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 17890
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

_source line 31 · 2026-05-24T09:13:12.245Z_

<details><summary>↩ Tool result · `toolu_01HdFPYm9ZJTh4BLnRtdhAEg`</summary>

```text
No matching deferred tools found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f4f409c6-f1ca-4945-81ad-238d20c57ca0",
  "isSidechain": false,
  "promptId": "b2df24c2-fd3f-4fb8-afa6-a3945babf3db",
  "type": "user",
  "uuid": "ab632910-0233-48d3-b204-04cf8ecf80db",
  "toolUseResult": {
    "matches": [],
    "query": "select:submit_dream_review_report",
    "total_deferred_tools": 23
  },
  "sourceToolAssistantUUID": "f4f409c6-f1ca-4945-81ad-238d20c57ca0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "ddd5074c-2b8b-40c6-b29f-f44ff9f131a7",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-24T09:14:30.307Z_

<details open><summary>🔧 Tool call — Agent · `toolu_012rxFdQJP73N7w2vLdbnKsU`</summary>

```json
{
  "description": "Full blind review of paper",
  "subagent_type": "general-purpose",
  "prompt": "You are an experienced ACL/EMNLP reviewer. Conduct a thorough, blind review of the following paper for EMNLP 2026 (via ARR).\n\n## Venue Scoring Scale (ARR Overall Assessment, 0.5 increments)\n- 5 = Consider for Award (top 2.5%)\n- 4 = Accept to main conference\n- 3 = Accept to Findings\n- 2 = Needs major revision, resubmit\n- 1 = Do not resubmit\n\nAcceptance rate: ACL/EMNLP Main ~21%. Calibrate strictly.\n\nScoring dimensions: Soundness (1-5), Excitement (1-5), Reproducibility (1-5).\n\n## Paper Summary\n\n**Title:** \"Why Auxiliary Attention Losses Fail Under Exposure Bias: A Multi-Model Diagnostic Study\"\n\n**Main Claims:** The paper implements ThreadGate, a per-layer gating module trained with a Goal Accessibility Ratio (GAR) auxiliary loss alongside NTP. ThreadGate optimizes GAR under teacher-forcing (TF GAR=0.50) but collapses under autoregressive generation (AR GAR=0.064 on Qwen-2.5-7B, 0.018 on Llama-3.1-8B), revealing an 8–27× training–inference gap. Through PCGrad ablation, λ sensitivity analysis, and cross-model replication, the paper identifies three failure modes: (NF1) reverse turn conditioning from NTP gradient dominance, (NF2) structural distribution shift independent of loss design, (NF3) insufficient gate intervention strength (2–7%). Attempted scheduled sampling mitigation succeeds partially on Qwen (AR GAR=0.39±0.04, 3-seed) but fails on Llama (AR GAR=0.04, gap 11.75×). The paper frames itself as a diagnostic/negative-result study.\n\n**Contributions claimed:**\n1. Failure mode taxonomy (NF1–NF3) for auxiliary attention losses under exposure bias\n2. First empirical elimination of gradient competition as a causal factor (PCGrad)\n3. Cross-model validation on Qwen-2.5-7B (MHA) and Llama-3.1-8B (GQA)\n4. Convergent evidence across two intervention designs × two models\n\n## Detailed Paper Content\n\n**Abstract (p1):** Multi-turn dialogue models lose attention to user goals. Prior work shows goal information persists in residual streams (probe AUC=0.98). ThreadGate implements learnable per-layer gating trained with GAR auxiliary loss. TF GAR=0.50 but AR GAR collapses. Three failure modes identified. SS partially works on Qwen but fails on Llama. Negative results establish concrete failure modes.\n\n**Introduction (p1-2):** Motivates from Dongre et al. (2026) showing 27-48% GAR decline across 12 models over 50 turns. Hypothesis: if goal info persists in residual stream but attention fails, a learnable gate on residual connection should recover goal accessibility. ThreadGate raises GAR from 0.02 to 0.50 under TF, but collapses to 0.064 (Qwen) and 0.018 (Llama) under AR. Three failure modes: NF1 (reverse turn conditioning), NF2 (structural distribution shift, 8-27× gap), NF3 (insufficient intervention strength, 2-7%). Convergent evidence with Dongre's independent failure of goal re-injection. Four contributions listed.\n\n**Related Work (p2-3):** Covers multi-turn dialogue degradation, residual gating/adaptive depth, attention steering/intervention, exposure bias in sequence models, gradient conflicts in multi-task learning. Positions the work as diagnosing *why* attention-based auxiliary losses fail rather than proposing new interventions.\n\n**Background (p3):** Defines GAR_ours (last-token attention to goals) and GAR_Dongre (all response tokens). Explains residual stream persistence (Dongre probe AUC=0.98) motivating architectural interventions.\n\n**Method (p3-4):**\n- ThreadGate: x_{l+1} = x_l + g_l · f_l(x_l), where g_l is a 2-layer MLP with sigmoid, parameterized by hidden state projection and turn-position embeddings.\n- UniformGate: same but constant turn embeddings (content-dependent, turn-agnostic).\n- LoRA-only: g=1.0 fixed, retains GAR auxiliary loss but no gating.\n- Training objective: L = L_NTP + λ_GAR · L_GAR + λ_div · L_div, with λ_GAR=1.0, λ_div=0.1 (v7 config).\n- Training: LoRA (r=16, α=32) on UltraChat, 3 epochs, batch size 4, lr 2e-4.\n\n**Experiments (p4-7):**\n- §5.1 Evaluation: TF (gold context) vs AR (model-generated context, β-steering). β=0 is default AR (gates disabled).\n- §5.2 Main result (Table 1): Qwen TF 0.501 → AR 0.064 (7.8× gap); Llama TF 0.484 → AR 0.018 (27× gap). Base models show no meaningful gap.\n- §5.3 Four-way ablation (Table 2): N=200 TF eval. TG/UG/LO all achieve ~0.50 TF GAR with identical PPL. All CIs contain zero. Gating provides zero increment over LoRA-only.\n- §5.4 PCGrad (Tables 3-4): On Qwen, 67-79% layers show negative cos_sim (mild conflict), PCGrad eliminates it but no change in outcomes (v9≈v7). On Llama, cos_sim≈+0.005 (near-orthogonal, not conflicting), neg layers 53.1% near random. PCGrad causal exclusion argument.\n- §5.5 λ sensitivity (Table 5): λ=0.1 (gates frozen, ≈LoRA-only), λ=10.0 (PPL degrades 36.7%, training unstable, AR gap 28.9×). Gap independent of λ.\n- §5.6 Cross-model replication on Llama: Same failure pattern with amplified severity (27×).\n\n**Analysis (p6-7):**\n- §6.1 Failure mode taxonomy: NF1 (27/28 layers show reverse turn conditioning), NF2 (gap persists across all variants/architectures/λ), NF3 (gates 0.93-0.98, only 2-7% attenuation).\n- §6.2 Attention KL divergence (Tables 6-7): Mean KL=0.054 for TG vs 0.043 base. GAR-relevant heads show 1.5× higher KL. But gate-KL correlation weak (r=0.11, p=0.18). Small absolute KL suggests compounding mechanisms beyond per-position divergence.\n- §6.3 Metric specificity (Table 8): Alternative GAR definitions. Improvement concentrated on last-token (our definition). All-token shows only marginal (2.8×), first-token and goal-only show no improvement. Position-specific overfitting concern.\n\n**Discussion (p8-10):**\n- §7.1 Scheduled Sampling: Qwen partial success — 3-seed AR GAR β=0 = 0.390±0.036 (CV=9.2%), gap 1.28×. 4th seed (s789) = 0.300, 4-seed CV=14.7%. Llama SS: complete failure, AR GAR=0.04, gap 11.75×. At β≥3, SS actually underperforms TG without SS. SS is model-specific.\n- §7.2 Scalability: SS decays after 10 turns (47.6% at 15 turns, 71.4% at 20 turns). TG converges to baseline by 15 turns.\n- §7.3 Convergent evidence: 5/6 intervention×model combinations fail. Only Qwen SS partially succeeds but is seed-sensitive, model-specific, length-limited.\n- §7.4 Future directions: inference-time intervention, data-dependent SS schedules, decoupled goal processing, stronger intervention mechanisms.\n\n**Conclusion (p10):** Reiterates failure mode taxonomy, PCGrad causal exclusion, SS model-specificity. \"Lightweight training-time interventions face fundamental barriers from exposure bias.\"\n\n**Limitations (p11):** Three limitations: (1) Only tests lightweight residual gating, not fundamentally different attention steering. (2) Limited to 7-8B models. (3) GAR is a proxy metric; improvements don't transfer to alternative token selection definitions.\n\n**Appendices (p13-14):** A: Expanded TF eval N=200 (Tables 14-15). B: λ sensitivity details. C: SS decay by conversation length. D: Llama TF eval comparison.\n\n## Experiment Design Reference (from review context)\n\nThe review context lists the following imagined experiments:\n1. Llama Gradient Conflict Analysis — covered in paper (Tables 3-4)\n2. Expanded Eval Set (200 conversations) — covered (Tables 14-15, Appendix A)\n3. λ_GAR Sensitivity Analysis — covered (Table 5, Appendix B)\n4. TF vs AR Attention KL Divergence — covered (Tables 6-7, §6.2)\n5. Llama-3.1-8B Scheduled Sampling — covered (Tables 10-11, §7.1)\n6. SS 3-Seed Validation (Qwen) — covered (Table 9, §7.1)\n7. Alternative GAR Definition Robustness — covered (Table 8, §6.3)\n8. SS 4th Seed (s789) — covered (Table 9, §7.1) — paper included it\n9. Long Conversation Eval (>10 turns) — covered (Table 12, §7.2)\n\nAll imagined experiments appear to be covered in the paper.\n\n## Your Review Task\n\nWrite a thorough EMNLP 2026 review covering:\n\n1. **Summary** (3-5 sentences)\n2. **Strengths** (bulleted, specific)\n3. **Weaknesses** (bulleted, specific, with severity ratings: minor/moderate/major/critical)\n4. **Questions for Authors**\n5. **Missing References or Related Work** (if any)\n6. **Soundness** (1-5 with justification)\n7. **Excitement** (1-5 with justification)\n8. **Reproducibility** (1-5 with justification)\n9. **Overall Assessment** (use the ARR 1-5 scale with 0.5 increments, strictly calibrated)\n10. **Confidence** (1-5)\n11. **Justification of Overall Assessment** (2-3 sentences)\n\nBe rigorous. This is a negative-result / diagnostic paper. Consider:\n- Is the failure mode taxonomy genuinely novel or insightful?\n- Is the experimental design rigorous enough to support the causal claims?\n- Does the paper advance community understanding in a meaningful way?\n- Are there critical gaps in methodology or interpretation?\n- How does the GAR metric specificity issue (§6.3) affect the validity of all findings?\n- How does the SS model-specificity and seed sensitivity affect the contribution?\n- Is the paper's scope sufficient for EMNLP?\n- Consider the 4th seed (s789) data — does including it help or hurt?\n\nFormat your review as a structured report. Be specific and cite tables/sections.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ab632910-0233-48d3-b204-04cf8ecf80db",
  "isSidechain": false,
  "requestId": "req_011CbM8toqce5Mg75YEGyVWP",
  "type": "assistant",
  "uuid": "5aaa96a3-0346-444d-bf0c-f464c4fee56d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "ddd5074c-2b8b-40c6-b29f-f44ff9f131a7",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012CYBig6hYnoSdcozu3n7S8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 17890,
      "cache_read_input_tokens": 40364,
      "output_tokens": 3185,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 17890,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 3185,
          "cache_read_input_tokens": 40364,
          "cache_creation_input_tokens": 17890,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 17890
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

_source line 33 · 2026-05-24T09:16:49.995Z_

<details><summary>↩ Tool result · `toolu_012rxFdQJP73N7w2vLdbnKsU`</summary>

```text


---

## EMNLP 2026 (ARR) Review

**Paper:** "From Collapse to Recovery: Diagnosing and Mitigating Exposure Bias in Multi-Turn Attention Objectives"

---

### 1. Summary

This paper investigates why auxiliary attention losses (specifically, the Goal Accessibility Ratio or GAR) optimized during teacher-forced training fail to transfer to autoregressive generation in multi-turn dialogue. The authors introduce ThreadGate, a per-layer content-and-turn-conditioned gating module on the residual stream, and conduct a five-way controlled comparison (ThreadGate, +PCGrad, Uniform Gate, LoRA-only, Base) on Qwen-2.5-7B and Llama-3.1-8B. All variants converge to TF GAR of 0.50 but collapse 8--27x under AR generation. Through a causal exclusion chain, the authors attribute the failure to exposure bias rather than gradient conflict or architectural limitations. Two mitigations are shown: inference-time attention steering (beta=5, GAR=0.727) and time-scheduled sampling (gap compressed to ~1.3x on Qwen, 3-seed).

---

### 2. Strengths

- **Well-structured causal exclusion methodology.** The five-way comparison is carefully designed so that each adjacent pair isolates one factor. The PCGrad experiment is a genuinely creative use of gradient surgery as a *diagnostic* rather than optimization tool. The modus tollens argument (removing conflict worsens AR GAR, p=0.002, therefore conflict is not the cause) is logically clean and well-executed.

- **Thorough experimental coverage.** The paper systematically addresses the most natural objections: gradient conflict (PCGrad), architecture dependence (Qwen vs. Llama, MHA vs. GQA), lambda sensitivity (Table 5 / Appendix B), metric specificity (four alternative GAR definitions, Appendix Q), general capability preservation (MMLU within 0.8pp), and conversation length scaling (Appendix D/N). The appendix is extensive and well-organized.

- **Clear identification of the exposure bias mechanism.** The argument that NTP self-recovers because prediction is the same task at train and test time, while GAR optimizes a distributional property with no autoregressive counterpart, is a useful conceptual contribution. The mechanism specificity analysis (TRC showing no gap while GAR collapses) and the per-head KL analysis (r=0.743 correlation between TF GAR and AR shift) are convincing supporting evidence.

- **Inference-time steering as a diagnostic.** Using beta-steering to confirm attention misallocation (not representation degradation) as the proximal cause closes the causal loop elegantly. The phase-transition behavior at beta=3 (Figure 1b) is an interesting empirical finding.

- **Honest reporting of partial successes and failures.** The paper is admirably transparent about SS working on Qwen but failing on Llama, about seed sensitivity (CV=9.2% on 3 seeds), and about the length-dependent decay of SS benefits. The loss design evolution (7 iterations, Table in Appendix B) is a useful contribution for practitioners.

- **Strong visual presentation.** Figure 1 is an effective headline figure. The log-scale TF-AR comparison (panel a) and steering recovery curve (panel b) immediately convey the core findings. Figures 3-5 are clean and informative.

---

### 3. Weaknesses

- **(Major) The paper's central finding is arguably unsurprising.** The observation that a teacher-forced auxiliary loss does not transfer to autoregressive generation is a direct prediction from the well-known exposure bias literature (Bengio et al., 2015; Ranzato et al., 2016; Arora et al., 2022). The paper acknowledges this heritage but claims novelty in demonstrating it on *auxiliary attention objectives* in *multi-turn transformers*. While technically true, the conceptual gap from "exposure bias affects sequence generation" to "exposure bias affects auxiliary losses during sequence generation" is modest. The causal exclusion chain, while well-executed, ultimately arrives at a conclusion most readers would predict. An experienced reviewer would ask: what is the actionable insight beyond "teacher forcing does not transfer, as expected"?

- **(Major) Scheduled sampling results are insufficiently robust to constitute a contribution.** SS is presented as the first training-time mitigation, but: (a) it works on Qwen but completely fails on Llama (AR GAR=0.04, gap 11.75x), with no explanation for the discrepancy; (b) 3-seed validation shows CV=9.2%, which the authors frame positively, but this is on a metric (GAR) that has high intrinsic variance; (c) the benefit decays rapidly with conversation length (47.6% at 15 turns, 71.4% at 20 turns per the task summary), making it impractical for the very scenario where multi-turn attention decay matters most; (d) training time variance is extreme (6.5h to 10.8h across seeds). A mitigation that is model-specific, seed-sensitive, and length-limited is difficult to position as a robust contribution.

- **(Major) GAR metric validity and generalizability concerns.** Section 6.3 / Appendix Q reveals that ThreadGate only improves last-token GAR (the definition it optimizes) but not all-token, first-token, or goal-only variants, raising a position-specific overfitting concern. While SS is shown to generalize across definitions, the entire diagnostic apparatus (the 8-27x gap, the failure mode taxonomy) is built on GAR-ours. The paper does not adequately address whether GAR-ours is a meaningful proxy for actual goal-tracking behavior, or whether optimizing it is inherently ill-posed. The downstream instruction retention evaluation (McNemar p=0.077, r=0.200) is marginally significant at best and based on only 18 constraint types -- this does not convincingly establish that GAR improvements matter for practical performance.

- **(Moderate) The failure mode taxonomy (NF1-NF3) has limited explanatory power.** NF1 (reverse turn conditioning) describes the symptom that gates approach 1.0 at late turns rather than providing stronger intervention. NF2 (structural distribution shift) is just "exposure bias" renamed. NF3 (insufficient intervention strength, 2-7%) is a consequence of NF1. These are three descriptions of the same phenomenon (gates are too weak because NTP dominates) rather than three distinct failure modes. The taxonomy does not provide differential diagnostic value -- knowing which "failure mode" applies does not suggest different remedies.

- **(Moderate) Limited model scale and diversity.** Both models are 7-8B parameter instruction-tuned models from the same generation. The 1.5B cross-scale validation (Appendix S) is welcome but only evaluates beta-steering, not the full diagnostic pipeline or SS. No models above 8B are tested. For a paper making general claims about "auxiliary attention losses," testing on two closely-related model families is thin. The single-dataset limitation (UltraChat) further constrains generalizability.

- **(Moderate) The "causal exclusion" framing overstates the strength of the evidence.** Modus tollens requires that removing the proposed cause should prevent the effect. PCGrad addresses gradient *direction* conflict but not magnitude imbalance (acknowledged in Limitations). The paper frames this as "ruling out gradient conflict" but it only rules out *directional* gradient conflict. Furthermore, the worsening under PCGrad (0.064 to 0.030) could reflect PCGrad disrupting beneficial gradient interactions rather than ruling out conflict as a cause. The causal language is stronger than the evidence warrants.

- **(Minor) Inconsistent evaluation protocols across models.** Qwen uses N=50 with mean 3.6 turns; Llama uses N=20 with 4 turns. Qwen reports means; Llama reports medians (due to heavy-tailed distributions). SS is validated with 3 seeds on Qwen but not on Llama (only one Llama SS run is mentioned). These asymmetries make cross-model comparison less rigorous than presented.

- **(Minor) The title and framing have evolved.** The task summary describes the paper as "Why Auxiliary Attention Losses Fail Under Exposure Bias: A Multi-Model Diagnostic Study" (negative result framing), but the actual paper title is "From Collapse to Recovery" (positive framing emphasizing SS and steering). This dual identity creates tension: the diagnostic contribution is modest if SS is the main result, and SS is too fragile to be the main result.

- **(Minor) Abstract exceeds stated norms.** The abstract is dense and contains specific numbers (0.50, 0.002, 0.727, 0.401, etc.) that could be replaced with qualitative descriptions for readability. At ~180 words it is within the 200-word EMNLP limit but pushes against it.

---

### 4. Questions for Authors

1. Can you provide a mechanistic explanation for why SS works on Qwen but completely fails on Llama? Without this, the SS contribution is difficult to assess as principled rather than accidental.

2. The gate diversity loss (L_div) enforces minimum std across gate values. What happens without it? If gates collapse to ~1.0 without diversity pressure, doesn't this suggest the gating mechanism is fighting against the model's preferred computation rather than augmenting it?

3. You report GAR target tau=0.5, allocating "half of the last token's attention capacity to goal tokens." How sensitive are results to tau? Is there a principled way to set tau, or is this arbitrary? Goal tokens may comprise only a small fraction of the sequence; is 50% attention allocation even desirable?

4. The steering experiment shows GAR recovery to 0.727 at beta=5 with PPL 1.77. How does generation quality (not just PPL) change? Are there pathological behaviors at high beta (repetition, incoherence)?

5. For the PCGrad modus tollens argument: could the worsening (0.064 to 0.030) reflect PCGrad removing *beneficial* gradient interactions rather than demonstrating that conflict is not causal? The two interpretations are not distinguished.

6. Why was Llama SS evaluated with only one seed when the Qwen results showed meaningful seed sensitivity?

---

### 5. Missing References or Related Work

- **Dou et al. (2019, 2022) -- Attention Forcing.** Cited in Related Work but the connection could be deeper: attention forcing directly supervises attention distributions during training, which is conceptually closer to GAR than scheduled sampling. Why was this approach not tested?

- **Attention supervision in distillation.** Works like Jiao et al. (2020, TinyBERT) and Wang et al. (2020) supervise attention during knowledge distillation. The relationship between attention supervision during distillation (which does transfer) and attention supervision via auxiliary losses (which does not, per this paper) deserves discussion.

- **Token-level exposure bias mitigation.** Beyond scheduled sampling, methods like Mixer (Goyal et al., 2017) and search-based training (Daume et al., 2009; Leblond et al., 2018) offer different approaches to the same problem. The paper cites Leblond et al. but does not discuss why these alternatives were not tested.

- **Concurrent work on system-prompt grounding.** The multi-turn attention decay problem likely has concurrent work beyond the cited papers; the authors should verify completeness.

---

### 6. Soundness: 3/5

The experimental methodology is generally careful, and the five-way comparison design is sound. However, several issues reduce confidence: (a) the causal exclusion chain overstates what PCGrad can rule out (direction conflict only, not magnitude); (b) the failure mode taxonomy conflates symptoms with causes; (c) cross-model evaluation uses inconsistent protocols; (d) the downstream validation (instruction retention) is underpowered (18 constraints, McNemar p=0.077). The core observation (TF-AR gap exists and is large) is well-established, but the causal attribution to exposure bias, while plausible, is more of an argument by elimination than a positive demonstration.

---

### 7. Excitement: 2/5

The central finding -- that teacher-forced auxiliary losses do not transfer to autoregressive generation -- is predictable from first principles of exposure bias. While the empirical demonstration is thorough, the conceptual advance is incremental. The scheduled sampling mitigation, which could elevate excitement, is undermined by model specificity (Qwen only), seed sensitivity, and length-limited effectiveness. The beta-steering diagnostic is an interesting methodological contribution but is inference-time and not novel in kind (additive attention biases are well-known). The paper will likely be of interest to a narrow audience working specifically on multi-turn attention optimization, but the insights do not generalize broadly enough for main-conference excitement.

---

### 8. Reproducibility: 4/5

The paper provides extensive implementation details: full hyperparameters (Appendix A), loss design evolution (Appendix B), training costs (Appendix J), dataset characteristics (Appendix M), statistical test details (Appendix E), and per-layer gate profiles (Appendix H). The use of specific model versions (Qwen-2.5-7B-Instruct, Llama-3.1-8B-Instruct) and a public dataset (UltraChat) aids reproducibility. The main gap is the SS training time variance (6.5h to 10.8h across seeds on the same GPU), which is unexplained and could indicate implementation sensitivity. Code availability is not discussed.

---

### 9. Overall Assessment: 2.5 (Borderline Findings)

---

### 10. Confidence: 4/5

I am confident in this assessment. I have deep familiarity with exposure bias, multi-task learning, attention mechanisms, and gating architectures. The main uncertainty is whether the community would find more value in the empirical documentation of this specific failure mode than I estimate.

---

### 11. Justification of Overall Assessment

The paper is a thorough empirical study with a well-designed ablation structure, but the central finding (exposure bias prevents TF auxiliary losses from transferring to AR generation) is predictable and the failure mode taxonomy provides limited new insight beyond labeling the known phenomenon. The scheduled sampling mitigation, which could strengthen the contribution, is model-specific (works on Qwen, fails on Llama), seed-sensitive, and degrades with conversation length -- precisely the regime where the problem matters most. The GAR metric specificity issue (position-specific overfitting of ThreadGate, Table in Appendix Q) and underpowered downstream validation (McNemar p=0.077) further weaken the practical significance. The paper falls between a solid Findings paper and one needing another revision cycle: the experimental execution is strong but the conceptual contribution and mitigation robustness are insufficient for main-conference acceptance. A revision incorporating a principled explanation for model-specific SS behavior, broader model/scale testing, and stronger downstream evaluation could elevate this to Findings level.

agentId: a2de08e360b959d80 (use SendMessage with to: 'a2de08e360b959d80' to continue this agent)
&lt;usage>total_tokens: 65248
tool_uses: 17
duration_ms: 139681&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5aaa96a3-0346-444d-bf0c-f464c4fee56d",
  "isSidechain": false,
  "promptId": "b2df24c2-fd3f-4fb8-afa6-a3945babf3db",
  "type": "user",
  "uuid": "1bc3bfe9-4f29-4d44-8147-04f64281eb12",
  "toolUseResult": {
    "status": "completed",
    "prompt": "You are an experienced ACL/EMNLP reviewer. Conduct a thorough, blind review of the following paper for EMNLP 2026 (via ARR).\n\n## Venue Scoring Scale (ARR Overall Assessment, 0.5 increments)\n- 5 = Consider for Award (top 2.5%)\n- 4 = Accept to main conference\n- 3 = Accept to Findings\n- 2 = Needs major revision, resubmit\n- 1 = Do not resubmit\n\nAcceptance rate: ACL/EMNLP Main ~21%. Calibrate strictly.\n\nScoring dimensions: Soundness (1-5), Excitement (1-5), Reproducibility (1-5).\n\n## Paper Summary\n\n**Title:** \"Why Auxiliary Attention Losses Fail Under Exposure Bias: A Multi-Model Diagnostic Study\"\n\n**Main Claims:** The paper implements ThreadGate, a per-layer gating module trained with a Goal Accessibility Ratio (GAR) auxiliary loss alongside NTP. ThreadGate optimizes GAR under teacher-forcing (TF GAR=0.50) but collapses under autoregressive generation (AR GAR=0.064 on Qwen-2.5-7B, 0.018 on Llama-3.1-8B), revealing an 8–27× training–inference gap. Through PCGrad ablation, λ sensitivity analysis, and cross-model replication, the paper identifies three failure modes: (NF1) reverse turn conditioning from NTP gradient dominance, (NF2) structural distribution shift independent of loss design, (NF3) insufficient gate intervention strength (2–7%). Attempted scheduled sampling mitigation succeeds partially on Qwen (AR GAR=0.39±0.04, 3-seed) but fails on Llama (AR GAR=0.04, gap 11.75×). The paper frames itself as a diagnostic/negative-result study.\n\n**Contributions claimed:**\n1. Failure mode taxonomy (NF1–NF3) for auxiliary attention losses under exposure bias\n2. First empirical elimination of gradient competition as a causal factor (PCGrad)\n3. Cross-model validation on Qwen-2.5-7B (MHA) and Llama-3.1-8B (GQA)\n4. Convergent evidence across two intervention designs × two models\n\n## Detailed Paper Content\n\n**Abstract (p1):** Multi-turn dialogue models lose attention to user goals. Prior work shows goal information persists in residual streams (probe AUC=0.98). ThreadGate implements learnable per-layer gating trained with GAR auxiliary loss. TF GAR=0.50 but AR GAR collapses. Three failure modes identified. SS partially works on Qwen but fails on Llama. Negative results establish concrete failure modes.\n\n**Introduction (p1-2):** Motivates from Dongre et al. (2026) showing 27-48% GAR decline across 12 models over 50 turns. Hypothesis: if goal info persists in residual stream but attention fails, a learnable gate on residual connection should recover goal accessibility. ThreadGate raises GAR from 0.02 to 0.50 under TF, but collapses to 0.064 (Qwen) and 0.018 (Llama) under AR. Three failure modes: NF1 (reverse turn conditioning), NF2 (structural distribution shift, 8-27× gap), NF3 (insufficient intervention strength, 2-7%). Convergent evidence with Dongre's independent failure of goal re-injection. Four contributions listed.\n\n**Related Work (p2-3):** Covers multi-turn dialogue degradation, residual gating/adaptive depth, attention steering/intervention, exposure bias in sequence models, gradient conflicts in multi-task learning. Positions the work as diagnosing *why* attention-based auxiliary losses fail rather than proposing new interventions.\n\n**Background (p3):** Defines GAR_ours (last-token attention to goals) and GAR_Dongre (all response tokens). Explains residual stream persistence (Dongre probe AUC=0.98) motivating architectural interventions.\n\n**Method (p3-4):**\n- ThreadGate: x_{l+1} = x_l + g_l · f_l(x_l), where g_l is a 2-layer MLP with sigmoid, parameterized by hidden state projection and turn-position embeddings.\n- UniformGate: same but constant turn embeddings (content-dependent, turn-agnostic).\n- LoRA-only: g=1.0 fixed, retains GAR auxiliary loss but no gating.\n- Training objective: L = L_NTP + λ_GAR · L_GAR + λ_div · L_div, with λ_GAR=1.0, λ_div=0.1 (v7 config).\n- Training: LoRA (r=16, α=32) on UltraChat, 3 epochs, batch size 4, lr 2e-4.\n\n**Experiments (p4-7):**\n- §5.1 Evaluation: TF (gold context) vs AR (model-generated context, β-steering). β=0 is default AR (gates disabled).\n- §5.2 Main result (Table 1): Qwen TF 0.501 → AR 0.064 (7.8× gap); Llama TF 0.484 → AR 0.018 (27× gap). Base models show no meaningful gap.\n- §5.3 Four-way ablation (Table 2): N=200 TF eval. TG/UG/LO all achieve ~0.50 TF GAR with identical PPL. All CIs contain zero. Gating provides zero increment over LoRA-only.\n- §5.4 PCGrad (Tables 3-4): On Qwen, 67-79% layers show negative cos_sim (mild conflict), PCGrad eliminates it but no change in outcomes (v9≈v7). On Llama, cos_sim≈+0.005 (near-orthogonal, not conflicting), neg layers 53.1% near random. PCGrad causal exclusion argument.\n- §5.5 λ sensitivity (Table 5): λ=0.1 (gates frozen, ≈LoRA-only), λ=10.0 (PPL degrades 36.7%, training unstable, AR gap 28.9×). Gap independent of λ.\n- §5.6 Cross-model replication on Llama: Same failure pattern with amplified severity (27×).\n\n**Analysis (p6-7):**\n- §6.1 Failure mode taxonomy: NF1 (27/28 layers show reverse turn conditioning), NF2 (gap persists across all variants/architectures/λ), NF3 (gates 0.93-0.98, only 2-7% attenuation).\n- §6.2 Attention KL divergence (Tables 6-7): Mean KL=0.054 for TG vs 0.043 base. GAR-relevant heads show 1.5× higher KL. But gate-KL correlation weak (r=0.11, p=0.18). Small absolute KL suggests compounding mechanisms beyond per-position divergence.\n- §6.3 Metric specificity (Table 8): Alternative GAR definitions. Improvement concentrated on last-token (our definition). All-token shows only marginal (2.8×), first-token and goal-only show no improvement. Position-specific overfitting concern.\n\n**Discussion (p8-10):**\n- §7.1 Scheduled Sampling: Qwen partial success — 3-seed AR GAR β=0 = 0.390±0.036 (CV=9.2%), gap 1.28×. 4th seed (s789) = 0.300, 4-seed CV=14.7%. Llama SS: complete failure, AR GAR=0.04, gap 11.75×. At β≥3, SS actually underperforms TG without SS. SS is model-specific.\n- §7.2 Scalability: SS decays after 10 turns (47.6% at 15 turns, 71.4% at 20 turns). TG converges to baseline by 15 turns.\n- §7.3 Convergent evidence: 5/6 intervention×model combinations fail. Only Qwen SS partially succeeds but is seed-sensitive, model-specific, length-limited.\n- §7.4 Future directions: inference-time intervention, data-dependent SS schedules, decoupled goal processing, stronger intervention mechanisms.\n\n**Conclusion (p10):** Reiterates failure mode taxonomy, PCGrad causal exclusion, SS model-specificity. \"Lightweight training-time interventions face fundamental barriers from exposure bias.\"\n\n**Limitations (p11):** Three limitations: (1) Only tests lightweight residual gating, not fundamentally different attention steering. (2) Limited to 7-8B models. (3) GAR is a proxy metric; improvements don't transfer to alternative token selection definitions.\n\n**Appendices (p13-14):** A: Expanded TF eval N=200 (Tables 14-15). B: λ sensitivity details. C: SS decay by conversation length. D: Llama TF eval comparison.\n\n## Experiment Design Reference (from review context)\n\nThe review context lists the following imagined experiments:\n1. Llama Gradient Conflict Analysis — covered in paper (Tables 3-4)\n2. Expanded Eval Set (200 conversations) — covered (Tables 14-15, Appendix A)\n3. λ_GAR Sensitivity Analysis — covered (Table 5, Appendix B)\n4. TF vs AR Attention KL Divergence — covered (Tables 6-7, §6.2)\n5. Llama-3.1-8B Scheduled Sampling — covered (Tables 10-11, §7.1)\n6. SS 3-Seed Validation (Qwen) — covered (Table 9, §7.1)\n7. Alternative GAR Definition Robustness — covered (Table 8, §6.3)\n8. SS 4th Seed (s789) — covered (Table 9, §7.1) — paper included it\n9. Long Conversation Eval (>10 turns) — covered (Table 12, §7.2)\n\nAll imagined experiments appear to be covered in the paper.\n\n## Your Review Task\n\nWrite a thorough EMNLP 2026 review covering:\n\n1. **Summary** (3-5 sentences)\n2. **Strengths** (bulleted, specific)\n3. **Weaknesses** (bulleted, specific, with severity ratings: minor/moderate/major/critical)\n4. **Questions for Authors**\n5. **Missing References or Related Work** (if any)\n6. **Soundness** (1-5 with justification)\n7. **Excitement** (1-5 with justification)\n8. **Reproducibility** (1-5 with justification)\n9. **Overall Assessment** (use the ARR 1-5 scale with 0.5 increments, strictly calibrated)\n10. **Confidence** (1-5)\n11. **Justification of Overall Assessment** (2-3 sentences)\n\nBe rigorous. This is a negative-result / diagnostic paper. Consider:\n- Is the failure mode taxonomy genuinely novel or insightful?\n- Is the experimental design rigorous enough to support the causal claims?\n- Does the paper advance community understanding in a meaningful way?\n- Are there critical gaps in methodology or interpretation?\n- How does the GAR metric specificity issue (§6.3) affect the validity of all findings?\n- How does the SS model-specificity and seed sensitivity affect the contribution?\n- Is the paper's scope sufficient for EMNLP?\n- Consider the 4th seed (s789) data — does including it help or hurt?\n\nFormat your review as a structured report. Be specific and cite tables/sections.\n",
    "agentId": "a2de08e360b959d80",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "\n\n---\n\n## EMNLP 2026 (ARR) Review\n\n**Paper:** \"From Collapse to Recovery: Diagnosing and Mitigating Exposure Bias in Multi-Turn Attention Objectives\"\n\n---\n\n### 1. Summary\n\nThis paper investigates why auxiliary attention losses (specifically, the Goal Accessibility Ratio or GAR) optimized during teacher-forced training fail to transfer to autoregressive generation in multi-turn dialogue. The authors introduce ThreadGate, a per-layer content-and-turn-conditioned gating module on the residual stream, and conduct a five-way controlled comparison (ThreadGate, +PCGrad, Uniform Gate, LoRA-only, Base) on Qwen-2.5-7B and Llama-3.1-8B. All variants converge to TF GAR of 0.50 but collapse 8--27x under AR generation. Through a causal exclusion chain, the authors attribute the failure to exposure bias rather than gradient conflict or architectural limitations. Two mitigations are shown: inference-time attention steering (beta=5, GAR=0.727) and time-scheduled sampling (gap compressed to ~1.3x on Qwen, 3-seed).\n\n---\n\n### 2. Strengths\n\n- **Well-structured causal exclusion methodology.** The five-way comparison is carefully designed so that each adjacent pair isolates one factor. The PCGrad experiment is a genuinely creative use of gradient surgery as a *diagnostic* rather than optimization tool. The modus tollens argument (removing conflict worsens AR GAR, p=0.002, therefore conflict is not the cause) is logically clean and well-executed.\n\n- **Thorough experimental coverage.** The paper systematically addresses the most natural objections: gradient conflict (PCGrad), architecture dependence (Qwen vs. Llama, MHA vs. GQA), lambda sensitivity (Table 5 / Appendix B), metric specificity (four alternative GAR definitions, Appendix Q), general capability preservation (MMLU within 0.8pp), and conversation length scaling (Appendix D/N). The appendix is extensive and well-organized.\n\n- **Clear identification of the exposure bias mechanism.** The argument that NTP self-recovers because prediction is the same task at train and test time, while GAR optimizes a distributional property with no autoregressive counterpart, is a useful conceptual contribution. The mechanism specificity analysis (TRC showing no gap while GAR collapses) and the per-head KL analysis (r=0.743 correlation between TF GAR and AR shift) are convincing supporting evidence.\n\n- **Inference-time steering as a diagnostic.** Using beta-steering to confirm attention misallocation (not representation degradation) as the proximal cause closes the causal loop elegantly. The phase-transition behavior at beta=3 (Figure 1b) is an interesting empirical finding.\n\n- **Honest reporting of partial successes and failures.** The paper is admirably transparent about SS working on Qwen but failing on Llama, about seed sensitivity (CV=9.2% on 3 seeds), and about the length-dependent decay of SS benefits. The loss design evolution (7 iterations, Table in Appendix B) is a useful contribution for practitioners.\n\n- **Strong visual presentation.** Figure 1 is an effective headline figure. The log-scale TF-AR comparison (panel a) and steering recovery curve (panel b) immediately convey the core findings. Figures 3-5 are clean and informative.\n\n---\n\n### 3. Weaknesses\n\n- **(Major) The paper's central finding is arguably unsurprising.** The observation that a teacher-forced auxiliary loss does not transfer to autoregressive generation is a direct prediction from the well-known exposure bias literature (Bengio et al., 2015; Ranzato et al., 2016; Arora et al., 2022). The paper acknowledges this heritage but claims novelty in demonstrating it on *auxiliary attention objectives* in *multi-turn transformers*. While technically true, the conceptual gap from \"exposure bias affects sequence generation\" to \"exposure bias affects auxiliary losses during sequence generation\" is modest. The causal exclusion chain, while well-executed, ultimately arrives at a conclusion most readers would predict. An experienced reviewer would ask: what is the actionable insight beyond \"teacher forcing does not transfer, as expected\"?\n\n- **(Major) Scheduled sampling results are insufficiently robust to constitute a contribution.** SS is presented as the first training-time mitigation, but: (a) it works on Qwen but completely fails on Llama (AR GAR=0.04, gap 11.75x), with no explanation for the discrepancy; (b) 3-seed validation shows CV=9.2%, which the authors frame positively, but this is on a metric (GAR) that has high intrinsic variance; (c) the benefit decays rapidly with conversation length (47.6% at 15 turns, 71.4% at 20 turns per the task summary), making it impractical for the very scenario where multi-turn attention decay matters most; (d) training time variance is extreme (6.5h to 10.8h across seeds). A mitigation that is model-specific, seed-sensitive, and length-limited is difficult to position as a robust contribution.\n\n- **(Major) GAR metric validity and generalizability concerns.** Section 6.3 / Appendix Q reveals that ThreadGate only improves last-token GAR (the definition it optimizes) but not all-token, first-token, or goal-only variants, raising a position-specific overfitting concern. While SS is shown to generalize across definitions, the entire diagnostic apparatus (the 8-27x gap, the failure mode taxonomy) is built on GAR-ours. The paper does not adequately address whether GAR-ours is a meaningful proxy for actual goal-tracking behavior, or whether optimizing it is inherently ill-posed. The downstream instruction retention evaluation (McNemar p=0.077, r=0.200) is marginally significant at best and based on only 18 constraint types -- this does not convincingly establish that GAR improvements matter for practical performance.\n\n- **(Moderate) The failure mode taxonomy (NF1-NF3) has limited explanatory power.** NF1 (reverse turn conditioning) describes the symptom that gates approach 1.0 at late turns rather than providing stronger intervention. NF2 (structural distribution shift) is just \"exposure bias\" renamed. NF3 (insufficient intervention strength, 2-7%) is a consequence of NF1. These are three descriptions of the same phenomenon (gates are too weak because NTP dominates) rather than three distinct failure modes. The taxonomy does not provide differential diagnostic value -- knowing which \"failure mode\" applies does not suggest different remedies.\n\n- **(Moderate) Limited model scale and diversity.** Both models are 7-8B parameter instruction-tuned models from the same generation. The 1.5B cross-scale validation (Appendix S) is welcome but only evaluates beta-steering, not the full diagnostic pipeline or SS. No models above 8B are tested. For a paper making general claims about \"auxiliary attention losses,\" testing on two closely-related model families is thin. The single-dataset limitation (UltraChat) further constrains generalizability.\n\n- **(Moderate) The \"causal exclusion\" framing overstates the strength of the evidence.** Modus tollens requires that removing the proposed cause should prevent the effect. PCGrad addresses gradient *direction* conflict but not magnitude imbalance (acknowledged in Limitations). The paper frames this as \"ruling out gradient conflict\" but it only rules out *directional* gradient conflict. Furthermore, the worsening under PCGrad (0.064 to 0.030) could reflect PCGrad disrupting beneficial gradient interactions rather than ruling out conflict as a cause. The causal language is stronger than the evidence warrants.\n\n- **(Minor) Inconsistent evaluation protocols across models.** Qwen uses N=50 with mean 3.6 turns; Llama uses N=20 with 4 turns. Qwen reports means; Llama reports medians (due to heavy-tailed distributions). SS is validated with 3 seeds on Qwen but not on Llama (only one Llama SS run is mentioned). These asymmetries make cross-model comparison less rigorous than presented.\n\n- **(Minor) The title and framing have evolved.** The task summary describes the paper as \"Why Auxiliary Attention Losses Fail Under Exposure Bias: A Multi-Model Diagnostic Study\" (negative result framing), but the actual paper title is \"From Collapse to Recovery\" (positive framing emphasizing SS and steering). This dual identity creates tension: the diagnostic contribution is modest if SS is the main result, and SS is too fragile to be the main result.\n\n- **(Minor) Abstract exceeds stated norms.** The abstract is dense and contains specific numbers (0.50, 0.002, 0.727, 0.401, etc.) that could be replaced with qualitative descriptions for readability. At ~180 words it is within the 200-word EMNLP limit but pushes against it.\n\n---\n\n### 4. Questions for Authors\n\n1. Can you provide a mechanistic explanation for why SS works on Qwen but completely fails on Llama? Without this, the SS contribution is difficult to assess as principled rather than accidental.\n\n2. The gate diversity loss (L_div) enforces minimum std across gate values. What happens without it? If gates collapse to ~1.0 without diversity pressure, doesn't this suggest the gating mechanism is fighting against the model's preferred computation rather than augmenting it?\n\n3. You report GAR target tau=0.5, allocating \"half of the last token's attention capacity to goal tokens.\" How sensitive are results to tau? Is there a principled way to set tau, or is this arbitrary? Goal tokens may comprise only a small fraction of the sequence; is 50% attention allocation even desirable?\n\n4. The steering experiment shows GAR recovery to 0.727 at beta=5 with PPL 1.77. How does generation quality (not just PPL) change? Are there pathological behaviors at high beta (repetition, incoherence)?\n\n5. For the PCGrad modus tollens argument: could the worsening (0.064 to 0.030) reflect PCGrad removing *beneficial* gradient interactions rather than demonstrating that conflict is not causal? The two interpretations are not distinguished.\n\n6. Why was Llama SS evaluated with only one seed when the Qwen results showed meaningful seed sensitivity?\n\n---\n\n### 5. Missing References or Related Work\n\n- **Dou et al. (2019, 2022) -- Attention Forcing.** Cited in Related Work but the connection could be deeper: attention forcing directly supervises attention distributions during training, which is conceptually closer to GAR than scheduled sampling. Why was this approach not tested?\n\n- **Attention supervision in distillation.** Works like Jiao et al. (2020, TinyBERT) and Wang et al. (2020) supervise attention during knowledge distillation. The relationship between attention supervision during distillation (which does transfer) and attention supervision via auxiliary losses (which does not, per this paper) deserves discussion.\n\n- **Token-level exposure bias mitigation.** Beyond scheduled sampling, methods like Mixer (Goyal et al., 2017) and search-based training (Daume et al., 2009; Leblond et al., 2018) offer different approaches to the same problem. The paper cites Leblond et al. but does not discuss why these alternatives were not tested.\n\n- **Concurrent work on system-prompt grounding.** The multi-turn attention decay problem likely has concurrent work beyond the cited papers; the authors should verify completeness.\n\n---\n\n### 6. Soundness: 3/5\n\nThe experimental methodology is generally careful, and the five-way comparison design is sound. However, several issues reduce confidence: (a) the causal exclusion chain overstates what PCGrad can rule out (direction conflict only, not magnitude); (b) the failure mode taxonomy conflates symptoms with causes; (c) cross-model evaluation uses inconsistent protocols; (d) the downstream validation (instruction retention) is underpowered (18 constraints, McNemar p=0.077). The core observation (TF-AR gap exists and is large) is well-established, but the causal attribution to exposure bias, while plausible, is more of an argument by elimination than a positive demonstration.\n\n---\n\n### 7. Excitement: 2/5\n\nThe central finding -- that teacher-forced auxiliary losses do not transfer to autoregressive generation -- is predictable from first principles of exposure bias. While the empirical demonstration is thorough, the conceptual advance is incremental. The scheduled sampling mitigation, which could elevate excitement, is undermined by model specificity (Qwen only), seed sensitivity, and length-limited effectiveness. The beta-steering diagnostic is an interesting methodological contribution but is inference-time and not novel in kind (additive attention biases are well-known). The paper will likely be of interest to a narrow audience working specifically on multi-turn attention optimization, but the insights do not generalize broadly enough for main-conference excitement.\n\n---\n\n### 8. Reproducibility: 4/5\n\nThe paper provides extensive implementation details: full hyperparameters (Appendix A), loss design evolution (Appendix B), training costs (Appendix J), dataset characteristics (Appendix M), statistical test details (Appendix E), and per-layer gate profiles (Appendix H). The use of specific model versions (Qwen-2.5-7B-Instruct, Llama-3.1-8B-Instruct) and a public dataset (UltraChat) aids reproducibility. The main gap is the SS training time variance (6.5h to 10.8h across seeds on the same GPU), which is unexplained and could indicate implementation sensitivity. Code availability is not discussed.\n\n---\n\n### 9. Overall Assessment: 2.5 (Borderline Findings)\n\n---\n\n### 10. Confidence: 4/5\n\nI am confident in this assessment. I have deep familiarity with exposure bias, multi-task learning, attention mechanisms, and gating architectures. The main uncertainty is whether the community would find more value in the empirical documentation of this specific failure mode than I estimate.\n\n---\n\n### 11. Justification of Overall Assessment\n\nThe paper is a thorough empirical study with a well-designed ablation structure, but the central finding (exposure bias prevents TF auxiliary losses from transferring to AR generation) is predictable and the failure mode taxonomy provides limited new insight beyond labeling the known phenomenon. The scheduled sampling mitigation, which could strengthen the contribution, is model-specific (works on Qwen, fails on Llama), seed-sensitive, and degrades with conversation length -- precisely the regime where the problem matters most. The GAR metric specificity issue (position-specific overfitting of ThreadGate, Table in Appendix Q) and underpowered downstream validation (McNemar p=0.077) further weaken the practical significance. The paper falls between a solid Findings paper and one needing another revision cycle: the experimental execution is strong but the conceptual contribution and mitigation robustness are insufficient for main-conference acceptance. A revision incorporating a principled explanation for model-specific SS behavior, broader model/scale testing, and stronger downstream evaluation could elevate this to Findings level."
      }
    ],
    "totalDurationMs": 139681,
    "totalTokens": 65248,
    "totalToolUseCount": 17,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11346,
      "cache_read_input_tokens": 50324,
      "output_tokens": 3575,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 11346
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 3575,
          "cache_read_input_tokens": 50324,
          "cache_creation_input_tokens": 11346,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 11346,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 13,
      "searchCount": 3,
      "bashCount": 1,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 0
    }
  },
  "sourceToolAssistantUUID": "5aaa96a3-0346-444d-bf0c-f464c4fee56d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "ddd5074c-2b8b-40c6-b29f-f44ff9f131a7",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 34_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[DREAM Review Director] dream_id=20260524T081135 | review_mode=simple | review_visible=True PDF: /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/…",
  "leafUuid": "1bc3bfe9-4f29-4d44-8147-04f64281eb12",
  "sessionId": "ddd5074c-2b8b-40c6-b29f-f44ff9f131a7"
}
```

---

### Runtime record

_source line 35_

```json
{
  "type": "ai-title",
  "aiTitle": "Review residual gating paper for EMNLP",
  "sessionId": "ddd5074c-2b8b-40c6-b29f-f44ff9f131a7"
}
```

---

### Assistant

_source line 36 · 2026-05-24T09:16:56.006Z_

<details><summary>Logged reasoning block</summary>

```text
Good, the reviewer has completed their review. Now I need to:

1. Compile the review report
2. Submit it via `submit_dream_review_report`

But the ToolSearch for `submit_dream_review_report` returned "No matching deferred tools found". Let me try again with a different query.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1bc3bfe9-4f29-4d44-8147-04f64281eb12",
  "isSidechain": false,
  "requestId": "req_011CbM9BtkGcui8uPrkc11Zn",
  "type": "assistant",
  "uuid": "4154435a-172e-4b2b-8b87-b2df0a30a7f5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "ddd5074c-2b8b-40c6-b29f-f44ff9f131a7",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RLZ2wHgjC3UeJSRMmEsguH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6899,
      "cache_read_input_tokens": 58254,
      "output_tokens": 186,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6899,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 186,
          "cache_read_input_tokens": 58254,
          "cache_creation_input_tokens": 6899,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6899
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

_source line 37 · 2026-05-24T09:16:56.958Z_

Reviewer 完成审稿。提交报告前需要加载提交工具。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4154435a-172e-4b2b-8b87-b2df0a30a7f5",
  "isSidechain": false,
  "requestId": "req_011CbM9BtkGcui8uPrkc11Zn",
  "type": "assistant",
  "uuid": "51da6e3a-fd7c-4330-8250-116066e341c2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "ddd5074c-2b8b-40c6-b29f-f44ff9f131a7",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RLZ2wHgjC3UeJSRMmEsguH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6899,
      "cache_read_input_tokens": 58254,
      "output_tokens": 186,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6899,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 186,
          "cache_read_input_tokens": 58254,
          "cache_creation_input_tokens": 6899,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6899
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

_source line 38 · 2026-05-24T09:16:57.336Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_015TcyhGPda419UdHQLgoxye`</summary>

```json
{
  "query": "submit_dream_review",
  "max_results": 3
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "51da6e3a-fd7c-4330-8250-116066e341c2",
  "isSidechain": false,
  "requestId": "req_011CbM9BtkGcui8uPrkc11Zn",
  "type": "assistant",
  "uuid": "c5f78f03-456b-4c2a-8807-f32ac32778b4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "ddd5074c-2b8b-40c6-b29f-f44ff9f131a7",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RLZ2wHgjC3UeJSRMmEsguH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6899,
      "cache_read_input_tokens": 58254,
      "output_tokens": 186,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6899,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 186,
          "cache_read_input_tokens": 58254,
          "cache_creation_input_tokens": 6899,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6899
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

_source line 39 · 2026-05-24T09:16:57.355Z_

<details><summary>↩ Tool result · `toolu_015TcyhGPda419UdHQLgoxye`</summary>

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
  "parentUuid": "c5f78f03-456b-4c2a-8807-f32ac32778b4",
  "isSidechain": false,
  "promptId": "b2df24c2-fd3f-4fb8-afa6-a3945babf3db",
  "type": "user",
  "uuid": "056876c8-1751-4833-843f-eac0afad6f0a",
  "toolUseResult": {
    "matches": [
      "mcp__agent-ml-research__submit_dream_review_report"
    ],
    "query": "submit_dream_review",
    "total_deferred_tools": 23
  },
  "sourceToolAssistantUUID": "c5f78f03-456b-4c2a-8807-f32ac32778b4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "ddd5074c-2b8b-40c6-b29f-f44ff9f131a7",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 40 · 2026-05-24T09:16:57.510Z_

```json
{
  "parentUuid": "056876c8-1751-4833-843f-eac0afad6f0a",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "335afc06-f3a9-4e25-86df-82d204c0744e",
  "timestamp": "2026-05-24T09:16:57.510Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "ddd5074c-2b8b-40c6-b29f-f44ff9f131a7",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---

### Assistant

_source line 41 · 2026-05-24T09:17:00.983Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have the tool schema. Let me compile the review report and submit it.

Let me write a comprehensive review report based on the reviewer's output, then submit it.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "335afc06-f3a9-4e25-86df-82d204c0744e",
  "isSidechain": false,
  "requestId": "req_011CbM9CSoLFNPvSmCbNogb7",
  "type": "assistant",
  "uuid": "2b35cfeb-6ef3-4002-b2a4-b0c93228d2a7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "ddd5074c-2b8b-40c6-b29f-f44ff9f131a7",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q4YE6WJgagMvjD9vtvW9Ke",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 912,
      "cache_read_input_tokens": 65153,
      "output_tokens": 4020,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 912,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 4020,
          "cache_read_input_tokens": 65153,
          "cache_creation_input_tokens": 912,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 912
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

_source line 42 · 2026-05-24T09:18:46.569Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_dream_review_report · `toolu_01AVX7QuYn8apeiiQCBaGEin`</summary>

```json
{
  "report": "# Dream Review Report — \"Why Auxiliary Attention Losses Fail Under Exposure Bias: A Multi-Model Diagnostic Study\"\n\n**Dream ID:** 20260524T081135 | **Tier:** worst | **Mode:** simple (1 Reviewer)\n\n---\n\n## 1. Summary\n\nThis paper investigates why auxiliary attention losses (GAR) optimized under teacher-forcing fail to transfer to autoregressive generation in multi-turn dialogue. The authors implement ThreadGate, a per-layer residual gating module trained jointly with NTP and a GAR auxiliary loss. ThreadGate achieves TF GAR=0.50 but collapses to AR GAR=0.064 on Qwen-2.5-7B (7.8× gap) and 0.018 on Llama-3.1-8B (27× gap). Through a five-way ablation (ThreadGate, UniformGate, LoRA-only, PCGrad, Base), λ sensitivity analysis, and cross-model replication, the paper identifies three failure modes (NF1: reverse turn conditioning, NF2: structural distribution shift, NF3: insufficient intervention strength) and attributes the root cause to exposure bias. Attempted scheduled sampling mitigation partially succeeds on Qwen (AR GAR=0.39±0.04, 3-seed) but completely fails on Llama (AR GAR=0.04, gap 11.75×).\n\n---\n\n## 2. Strengths\n\n- **Well-designed causal exclusion methodology.** The five-way comparison isolates factors systematically. PCGrad as a *diagnostic* tool (rather than optimizer) is creative — removing gradient direction conflicts without changing outcomes provides a clean modus tollens argument for ruling out gradient competition.\n\n- **Thorough experimental coverage.** The paper addresses most natural objections: gradient conflict (PCGrad §5.4), architecture dependence (Qwen MHA vs. Llama GQA, §5.6), λ sensitivity (Table 5), metric specificity (Table 8, §6.3), and conversation-length scaling (Table 12, §7.2). All imagined experiments from the design reference appear covered in the paper.\n\n- **Honest reporting of partial successes and failures.** The paper is admirably transparent about SS working on Qwen but failing on Llama, about seed sensitivity (CV=9.2% on 3-seed, 14.7% on 4-seed), and about SS decay beyond 10 turns. Including the damaging 4th seed (s789, AR GAR=0.300) is scientifically honest even though it weakens the SS story.\n\n- **Clear mechanistic argument.** The observation that base models show no TF-AR gap (TF≈AR≈0.01–0.02) while fine-tuned variants show 8–27× gaps directly establishes that the gap is introduced by auxiliary loss training rather than being inherent to autoregressive generation. This is well-presented.\n\n- **Convergent evidence framing.** Table 13 (5/6 intervention×model combinations fail) combined with Dongre et al.'s independent failure of goal re-injection provides a compelling argument for structural impossibility of lightweight training-time interventions.\n\n- **Good visual presentation.** 12 tables in main text + 5 in appendix provide comprehensive quantitative evidence. The paper is well-organized with clear section structure.\n\n---\n\n## 3. Weaknesses\n\n### Critical / Major\n\n- **(Major) The central finding is arguably unsurprising.** The observation that teacher-forced auxiliary losses do not transfer to autoregressive generation is a direct prediction from the exposure bias literature (Bengio et al., 2015; Ranzato et al., 2016). The paper claims novelty in demonstrating this on *auxiliary attention objectives* in *multi-turn transformers*, but the conceptual gap from \"exposure bias affects sequence generation\" to \"exposure bias affects auxiliary losses during sequence generation\" is modest. The three failure modes (NF1–NF3) are better understood as three *descriptions* of the same phenomenon (NTP dominates, gates too weak, patterns don't transfer) rather than three distinct mechanisms requiring separate remedies. The taxonomy does not provide differential diagnostic value — knowing which \"failure mode\" applies does not suggest different solutions.\n\n- **(Major) Scheduled sampling results are too fragile to constitute a contribution.** SS is the paper's only positive result, but it is: (a) model-specific — works on Qwen, completely fails on Llama (AR GAR=0.04, gap 11.75×) with no mechanistic explanation for the divergence; (b) seed-sensitive — CV=14.7% on 4 seeds, with s789 (0.300) far below s456 (0.422); (c) length-limited — decays 47.6% at 15 turns, 71.4% at 20 turns (Table 12), precisely the regime where multi-turn attention decay matters most per the paper's own motivation (Dongre's 50-turn scenarios); (d) at β≥3, SS actually *underperforms* ThreadGate without SS on Llama (−0.036 at β=3, −0.047 at β=5, Table 11), suggesting SS interferes with the attention patterns that β-steering exploits. A mitigation that is model-specific, seed-sensitive, and length-limited is not a robust contribution.\n\n- **(Major) GAR metric validity concerns.** Table 8 (§6.3) reveals that improvement is overwhelmingly concentrated on last-token GAR (the definition optimized). All-token GAR (≈Dongre) shows only marginal SS improvement (0.062 vs 0.022 baseline, 2.8×), while first-token and goal-only definitions show no improvement beyond noise. This raises a position-specific overfitting concern: the training objective may teach the model to concentrate attention at the summary position under teacher-forcing without genuinely improving goal tracking. The entire diagnostic apparatus (the 8–27× gap, NF1–NF3) is built on GAR_ours. The paper acknowledges this in Limitations but does not adequately address whether the measured gaps reflect genuine attention degradation or metric-specific artifacts.\n\n### Moderate\n\n- **(Moderate) The failure mode taxonomy conflates symptoms with causes.** NF1 (reverse turn conditioning) describes the symptom that gates approach 1.0 at late turns. NF2 (structural distribution shift) is exposure bias renamed. NF3 (insufficient intervention strength, 2–7%) is a direct consequence of NF1 (NTP gradient dominance pushes gates toward identity). These are not three independent failure modes but three facets of one mechanism: NTP gradients dominate, preventing gates from learning useful intervention patterns under teacher-forcing that would transfer to autoregressive generation.\n\n- **(Moderate) The \"causal exclusion\" framing overstates evidentiary strength.** PCGrad addresses gradient *direction* conflict but not *magnitude* imbalance (the paper acknowledges NTP magnitude dominance of 12–25×). Ruling out directional conflict is not the same as ruling out all gradient interaction effects. The worsening under PCGrad on Qwen (v9 GAR=0.0151 vs v7=0.0157 — essentially no change, not worsening) and the very different gradient geometry on Llama (near-orthogonal, cos_sim≈+0.005, neg layers 53.1% near random) mean the PCGrad argument has different implications on each model. The cross-model comparison does strengthen the exclusion but the causal language (\"first empirical elimination\") is stronger than warranted.\n\n- **(Moderate) Limited model scale and diversity.** Both models are 7–8B instruction-tuned from the same generation. No models above 8B or below 7B are tested in the full pipeline. The single-dataset limitation (UltraChat only) further constrains generalizability. For a paper making general claims about \"auxiliary attention losses,\" testing on two model families from one dataset is thin.\n\n- **(Moderate) Attention KL analysis (§6.2) is underwhelming.** Mean KL=0.054 nats is small. GAR-relevant heads show only 1.5× higher KL than non-relevant heads (0.072 vs 0.048). Gate-KL correlation is weak and non-significant (r=0.11, p=0.18). The paper honestly acknowledges these limitations, but the analysis provides weak supplementary evidence at best and potentially gives reviewers ammunition (\"if KL is this small, maybe distribution shift isn't the mechanism\").\n\n### Minor\n\n- **(Minor) Inconsistent evaluation protocols across models.** Qwen uses N=50 AR eval; Llama uses N=20. SS is validated with 3-4 seeds on Qwen but only 1 seed on Llama. These asymmetries make cross-model comparison less rigorous than presented.\n\n- **(Minor) Including s789 is a double-edged sword.** While scientifically honest, the 4th seed (AR GAR=0.300, gap 1.67×) raises CV from 9.2% to 14.7% and pulls the 4-seed mean down to 0.367 from the 3-seed 0.390. This actively weakens the SS contribution. The paper could have been stronger with 3 seeds and s789 held for rebuttal.\n\n- **(Minor) No code availability statement.** Reproducibility would benefit from explicit commitment to release code and trained checkpoints.\n\n---\n\n## 4. Questions for Authors\n\n1. Can you provide a mechanistic explanation for why SS succeeds on Qwen but completely fails on Llama? Without this, the SS contribution appears accidental rather than principled. The speculative reasons listed (tokenizer difference, depth difference, lower base GAR) are post-hoc and untested.\n\n2. Table 8 shows GAR improvement is concentrated on last-token only. Does this mean the model learns to \"cheat\" by concentrating goal attention at the summary position under TF, without genuinely routing goal information? How would you distinguish position-specific overfitting from genuine goal-tracking improvement?\n\n3. Why is Llama SS evaluated with only one seed when Qwen results already demonstrated meaningful seed sensitivity (CV=9.2%)?\n\n4. The gate diversity loss L_div enforces minimum variance across gate values. What happens without it? If gates collapse to ~1.0 without diversity pressure, doesn't this suggest gating is fighting against the model's preferred computation?\n\n5. For the λ sensitivity analysis: at λ=10.0, PPL degrades 36.7% and training becomes unstable. Is this really showing \"gap independence from loss weighting\" or is it showing that aggressive λ destroys the model?\n\n6. The SS effectiveness decays ~48% per 5 turns after turn 10. Given that the paper's motivation comes from Dongre's 50-turn scenarios, how do you reconcile proposing a mitigation that fails precisely where it's needed most?\n\n---\n\n## 5. Missing References / Related Work\n\n- **Attention forcing / attention supervision in distillation** (Jiao et al., 2020 TinyBERT; Wang et al., 2020). Attention supervision during distillation *does* transfer — discussing why would strengthen the exposure bias argument.\n- **Token-level exposure bias mitigation** beyond SS: Mixer (Goyal et al., 2017), DAgger-style methods (Ross et al., 2011). Why were these alternatives not tested?\n- **Li et al. (2024)** on auxiliary loss interference in multi-task LLM training — direct competitor that should be discussed.\n\n---\n\n## 6. Scores\n\n### Soundness: 3 / 5\nThe experimental design is careful and the five-way ablation is well-constructed. However: (a) the causal exclusion chain overstates what PCGrad can rule out (direction only, not magnitude); (b) the failure mode taxonomy conflates three descriptions of one phenomenon; (c) GAR metric specificity (Table 8) undermines confidence that the measured gaps reflect genuine attention degradation; (d) cross-model evaluation uses inconsistent protocols. The core observation (TF-AR gap is large) is well-established, but the causal attribution is more argument-by-elimination than positive demonstration.\n\n### Excitement: 2 / 5\nThe central finding — teacher-forced auxiliary losses don't transfer under exposure bias — is predictable from first principles. The empirical demonstration is thorough but the conceptual advance is incremental. SS mitigation, which could elevate excitement, is undermined by model-specificity, seed sensitivity, and length-limited effectiveness. The failure mode taxonomy provides limited actionable insight. The paper will interest a narrow audience working on multi-turn attention optimization but lacks the broader impact expected for main conference.\n\n### Reproducibility: 4 / 5\nExtensive implementation details: full hyperparameters, loss design evolution, training costs, dataset characteristics, statistical test details, per-layer gate profiles. Public models (Qwen-2.5-7B, Llama-3.1-8B) and dataset (UltraChat). Main gap: no code release commitment, and unexplained SS training time variance across seeds.\n\n---\n\n## 7. Overall Assessment: 2.5 (Borderline Findings)\n\n**Confidence: 4 / 5**\n\n---\n\n## 8. Justification\n\nThe paper is a thorough empirical study with well-designed ablations, but the central finding (exposure bias prevents TF auxiliary losses from transferring to AR generation) is predictable and the failure mode taxonomy provides limited new insight beyond relabeling the known phenomenon. The scheduled sampling mitigation — the paper's only positive result — is model-specific (works on Qwen, fails on Llama), seed-sensitive (CV=14.7% on 4 seeds), and degrades with conversation length (fails where it's needed most). The GAR metric specificity issue (position-specific overfitting, Table 8) and weak downstream validation further weaken practical significance. Experimental execution is strong but conceptual contribution and mitigation robustness are insufficient for main conference. A revision incorporating principled explanation for model-specific SS behavior, broader model/scale testing, and stronger downstream validation could elevate to Findings level.\n\n---\n\n## 9. Experiment Coverage Assessment\n\nAll 9 imagined experiments from the design reference are covered in the paper:\n1. ✅ Llama Gradient Conflict Analysis (Tables 3-4)\n2. ✅ Expanded Eval Set N=200 (Appendix A, Tables 14-15)\n3. ✅ λ_GAR Sensitivity (Table 5, Appendix B)\n4. ✅ TF vs AR Attention KL Divergence (Tables 6-7, §6.2)\n5. ✅ Llama SS (Tables 10-11, §7.1)\n6. ✅ SS 3-Seed Validation (Table 9, §7.1)\n7. ✅ Alternative GAR Definitions (Table 8, §6.3)\n8. ✅ SS 4th Seed s789 (Table 9, §7.1)\n9. ✅ Long Conversation Eval (Table 12, §7.2)\n\nCoverage is complete. The paper includes all planned experiments, including the risky s789 4th seed data that weakens the SS story.\n\n---\n\n## 10. Key Risks for Submission\n\n| Risk | Severity | Mitigation Path |\n|------|----------|----------------|\n| \"Unsurprising\" novelty objection | High | Strengthen failure taxonomy with differential diagnostics; deeper mechanistic analysis |\n| SS model-specificity (Llama failure) | High | Needs mechanistic explanation or removal from contributions |\n| GAR metric specificity (Table 8) | High | Stronger downstream validation; alternative metric development |\n| SS seed sensitivity (CV=14.7%) | Medium | More seeds or acknowledge as limitation prominently |\n| SS length decay (fails >10 turns) | Medium | Reframe scope; honest limitation discussion (already done) |\n| NF1-NF3 redundancy | Medium | Restructure as single mechanism with multiple observable consequences |",
  "project": "turn_residual_gating",
  "tier": "worst",
  "dream_id": "20260524T081135",
  "overall_score": "2.5 — Borderline Findings",
  "review_visible": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2b35cfeb-6ef3-4002-b2a4-b0c93228d2a7",
  "isSidechain": false,
  "requestId": "req_011CbM9CSoLFNPvSmCbNogb7",
  "type": "assistant",
  "uuid": "f721522d-d4fe-477e-a18a-927524c9bab8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "ddd5074c-2b8b-40c6-b29f-f44ff9f131a7",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q4YE6WJgagMvjD9vtvW9Ke",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 912,
      "cache_read_input_tokens": 65153,
      "output_tokens": 4020,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 912,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 4020,
          "cache_read_input_tokens": 65153,
          "cache_creation_input_tokens": 912,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 912
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

_source line 43 · 2026-05-24T09:18:50.106Z_

<details><summary>↩ Tool result · `toolu_01AVX7QuYn8apeiiQCBaGEin`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"report_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260524T081135/worst/review_report.md\", \"dream_id\": \"dream_20260524T081135\", \"tier\": \"worst\", \"review_visible\": true}, \"error\": \"\"}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f721522d-d4fe-477e-a18a-927524c9bab8",
  "isSidechain": false,
  "promptId": "b2df24c2-fd3f-4fb8-afa6-a3945babf3db",
  "type": "user",
  "uuid": "1731bfe5-385b-45b7-a8b1-b040f7650670",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"report_path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260524T081135/worst/review_report.md\\\", \\\"dream_id\\\": \\\"dream_20260524T081135\\\", \\\"tier\\\": \\\"worst\\\", \\\"review_visible\\\": true}, \\\"error\\\": \\\"\\\"}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"report_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/dream_20260524T081135/worst/review_report.md\", \"dream_id\": \"dream_20260524T081135\", \"tier\": \"worst\", \"review_visible\": true}, \"error\": \"\"}"
    }
  },
  "sourceToolAssistantUUID": "f721522d-d4fe-477e-a18a-927524c9bab8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "ddd5074c-2b8b-40c6-b29f-f44ff9f131a7",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 44 · 2026-05-24T09:18:59.672Z_

审稿完成。报告已提交至 `dream_reports/dream_20260524T081135/worst/review_report.md`。

**Overall Assessment: 2.5 (Borderline Findings)**

核心评审结论：
- **Soundness 3/5** — 实验设计严谨但因果排除链（PCGrad）措辞过强，failure taxonomy 三个 mode 实质是同一机制的三种表现
- **Excitement 2/5** — 核心发现（TF auxiliary loss 受 exposure bias 影响不迁移到 AR）从已有文献可预测，概念增量有限
- **Reproducibility 4/5** — 细节充分，公开模型/数据集，但缺代码发布承诺

主要风险：SS mitigation 是唯一正面结果但 model-specific（Llama 完全失败）、seed-sensitive（CV=14.7%）、length-limited（>10 turns 快速衰减）；GAR 指标 position-specific overfitting（Table 8 只有 last-token 定义有改善）削弱整体 validity。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1731bfe5-385b-45b7-a8b1-b040f7650670",
  "isSidechain": false,
  "requestId": "req_011CbM9LkE3s3BqQmeRdVGYd",
  "type": "assistant",
  "uuid": "2baa10a8-4fbb-48f2-80c2-cdeee8ffa048",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "ddd5074c-2b8b-40c6-b29f-f44ff9f131a7",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019MAgmAWo1QbD7G4ukdJdK5",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4150,
      "cache_read_input_tokens": 66065,
      "output_tokens": 310,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4150,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 310,
          "cache_read_input_tokens": 66065,
          "cache_creation_input_tokens": 4150,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4150
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
  "lastPrompt": "[DREAM Review Director] dream_id=20260524T081135 | review_mode=simple | review_visible=True PDF: /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/dream_reports/…",
  "leafUuid": "2baa10a8-4fbb-48f2-80c2-cdeee8ffa048",
  "sessionId": "ddd5074c-2b8b-40c6-b29f-f44ff9f131a7"
}
```

---

### Runtime record

_source line 46_

```json
{
  "type": "ai-title",
  "aiTitle": "Review residual gating paper for EMNLP",
  "sessionId": "ddd5074c-2b8b-40c6-b29f-f44ff9f131a7"
}
```

---
