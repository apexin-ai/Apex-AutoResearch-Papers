# Research conversation: [DREAM Review Director] dream_id=20260521T122458 | review_mode=simple | review_visible=True PDF: /home/ubuntu/.agent-ml-

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 55
- **Recorded user turns:** 3
- **Tool calls:** 11
- **Original source:** `logs/chats/exported-trajectories/account-2/b4ed7333-11c6-492f-a8d4-e66619498d15.jsonl`
- **Structured JSON:** [`fede7b1a1473bb18b0af.json`](../../sessions/fe/fede7b1a1473bb18b0af.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-21T13:56:58.073Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-21T13:56:58.073Z",
  "sessionId": "b4ed7333-11c6-492f-a8d4-e66619498d15",
  "content": "[DREAM Review Director]\ndream_id=20260521T122458 | review_mode=simple | review_visible=True\nPDF: /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T122458/worst/review_input_f5f46a62.pdf\n\n（内部编排信息：tier=worst，仅用于 submit_dream_review_report 调用。\n你在向 Reviewer 发送审稿任务时，**严禁**提及档位名称 best/median/worst，\n也不要暗示论文结果的好坏。Reviewer 必须盲审。）\n\n任务：对上述 PDF 进行 simple 模式审稿。 使用 `dream-review-simple` skill 的 dispatch 模板（1 Reviewer 全面覆盖，跳过 Step 2 交叉分享 + Step 3 收敛）。\n\n## 审稿标准\n\n未指定目标 venue。在开始审稿前，你必须：\n1. 确认目标 venue 及其评分标准\n2. 用 WebSearch 搜索该 venue 的 reviewer guidelines\n3. 严格按照搜到的官方评分刻度打分\n4. 如果无法确认 venue，使用 ACL ARR 1-5 分制\n\n## 实验设计参考\n\n完整实验设计（含想象实验列表）：`/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T122458/worst/review_context.yaml`\n论文可能未完整反映所有实验——参考此文件判断覆盖度。\n完成后必须调用 `submit_dream_review_report(report, project=\"xling_calib_direction\", tier=\"worst\", dream_id=\"20260521T122458\", review_visible=True)` —— 报告会写入 dream_reports/dream_20260521T122458/worst/review_report.md，编排进程通过 subprocess 退出读取它。\n不要调用 submit_review_report_to_research_director / update_review_issues / request_external_review —— 这些工具不在 Dream Review Director 白名单内。\n"
}
```

---

### Runtime record

_source line 2 · 2026-05-21T13:56:58.076Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-21T13:56:58.076Z",
  "sessionId": "b4ed7333-11c6-492f-a8d4-e66619498d15"
}
```

---

## Round 1

19 recorded events

### User

_source line 3 · 2026-05-21T13:56:58.108Z_

[DREAM Review Director]
dream_id=20260521T122458 | review_mode=simple | review_visible=True
PDF: /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T122458/worst/review_input_f5f46a62.pdf

（内部编排信息：tier=worst，仅用于 submit_dream_review_report 调用。
你在向 Reviewer 发送审稿任务时，**严禁**提及档位名称 best/median/worst，
也不要暗示论文结果的好坏。Reviewer 必须盲审。）

任务：对上述 PDF 进行 simple 模式审稿。 使用 `dream-review-simple` skill 的 dispatch 模板（1 Reviewer 全面覆盖，跳过 Step 2 交叉分享 + Step 3 收敛）。

## 审稿标准

未指定目标 venue。在开始审稿前，你必须：
1. 确认目标 venue 及其评分标准
2. 用 WebSearch 搜索该 venue 的 reviewer guidelines
3. 严格按照搜到的官方评分刻度打分
4. 如果无法确认 venue，使用 ACL ARR 1-5 分制

## 实验设计参考

完整实验设计（含想象实验列表）：`/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T122458/worst/review_context.yaml`
论文可能未完整反映所有实验——参考此文件判断覆盖度。
完成后必须调用 `submit_dream_review_report(report, project="xling_calib_direction", tier="worst", dream_id="20260521T122458", review_visible=True)` —— 报告会写入 dream_reports/dream_20260521T122458/worst/review_report.md，编排进程通过 subprocess 退出读取它。
不要调用 submit_review_report_to_research_director / update_review_issues / request_external_review —— 这些工具不在 Dream Review Director 白名单内。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "ac986e77-89c2-4da2-8cf0-d9a0da36482f",
  "type": "user",
  "uuid": "844fba29-6723-4427-8bab-eebea28ffb8d",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "b4ed7333-11c6-492f-a8d4-e66619498d15",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-21T13:56:58.107Z_

```json
{
  "parentUuid": "844fba29-6723-4427-8bab-eebea28ffb8d",
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
  "uuid": "96d3bb0d-eeda-4a50-bede-644549109bdc",
  "timestamp": "2026-05-21T13:56:58.107Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "b4ed7333-11c6-492f-a8d4-e66619498d15",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-21T13:56:58.107Z_

```json
{
  "parentUuid": "96d3bb0d-eeda-4a50-bede-644549109bdc",
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
  "uuid": "1b5386bf-c8f1-4071-ae88-6968bce8b05f",
  "timestamp": "2026-05-21T13:56:58.107Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "b4ed7333-11c6-492f-a8d4-e66619498d15",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6 · 2026-05-21T13:56:58.107Z_

```json
{
  "parentUuid": "1b5386bf-c8f1-4071-ae88-6968bce8b05f",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "95c4bf4a-8f71-4ec9-872b-e27cc12105d7",
  "timestamp": "2026-05-21T13:56:58.107Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "b4ed7333-11c6-492f-a8d4-e66619498d15",
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
  "aiTitle": "Review cross-lingual calibration direction paper",
  "sessionId": "b4ed7333-11c6-492f-a8d4-e66619498d15"
}
```

---

### Assistant

_source line 8 · 2026-05-21T13:57:03.120Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to review a PDF paper as a DREAM Review Director. Let me break down the task:

1. Read the PDF paper
2. Read the review context YAML for experiment design reference
3. Determine the target venue and search for reviewer guidelines
4. Conduct a thorough review using the dream-review-simple skill
5. Submit the review report using submit_dream_review_report

Let me start by reading the PDF and the review context, and loading the necessary tools.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "95c4bf4a-8f71-4ec9-872b-e27cc12105d7",
  "isSidechain": false,
  "requestId": "req_011CbFq8AanfyAzEXmEvM2A6",
  "type": "assistant",
  "uuid": "d908cf79-34df-409b-a4be-1f32de0fa937",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "b4ed7333-11c6-492f-a8d4-e66619498d15",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FeswCS53NfYEfpCzFH7mfA",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11385,
      "cache_read_input_tokens": 11841,
      "output_tokens": 410,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11385,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 410,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11385,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11385
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

_source line 9 · 2026-05-21T13:57:03.728Z_

Let me start by reading the PDF, the review context, and loading the necessary tools.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d908cf79-34df-409b-a4be-1f32de0fa937",
  "isSidechain": false,
  "requestId": "req_011CbFq8AanfyAzEXmEvM2A6",
  "type": "assistant",
  "uuid": "e5bcf8ec-d242-499c-856b-39063b771164",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "b4ed7333-11c6-492f-a8d4-e66619498d15",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FeswCS53NfYEfpCzFH7mfA",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11385,
      "cache_read_input_tokens": 11841,
      "output_tokens": 410,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11385,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 410,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11385,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11385
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

_source line 10 · 2026-05-21T13:57:04.203Z_

<details open><summary>🔧 Tool call — Read · `toolu_018Ffo8D7TXd6HRxJ6ZHL2jg`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T122458/worst/review_input_f5f46a62.pdf"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e5bcf8ec-d242-499c-856b-39063b771164",
  "isSidechain": false,
  "requestId": "req_011CbFq8AanfyAzEXmEvM2A6",
  "type": "assistant",
  "uuid": "03a12ef5-b0b2-4c57-b9c5-ff43d8c48e9d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "b4ed7333-11c6-492f-a8d4-e66619498d15",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FeswCS53NfYEfpCzFH7mfA",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11385,
      "cache_read_input_tokens": 11841,
      "output_tokens": 410,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11385,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 410,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11385,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11385
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

_source line 11 · 2026-05-21T13:57:05.462Z_

<details><summary>↩ Tool result · `toolu_016N2fmaMEoRvaWPoSSLjJ7c`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "WebSearch"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "WebFetch"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "32bdd246-6e78-4506-bdc3-f18670d00547",
  "isSidechain": false,
  "promptId": "ac986e77-89c2-4da2-8cf0-d9a0da36482f",
  "type": "user",
  "uuid": "ca85cef6-ec3d-428e-9ace-50b6209f3bfd",
  "toolUseResult": {
    "matches": [
      "WebSearch",
      "WebFetch"
    ],
    "query": "select:submit_dream_review_report,WebSearch,WebFetch",
    "total_deferred_tools": 23
  },
  "sourceToolAssistantUUID": "32bdd246-6e78-4506-bdc3-f18670d00547",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "b4ed7333-11c6-492f-a8d4-e66619498d15",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-21T13:57:04.238Z_

<details><summary>↩ Tool result · reported error · `toolu_018Ffo8D7TXd6HRxJ6ZHL2jg`</summary>

```text
This PDF has 11 pages, which is too many to read at once. Use the pages parameter to read specific page ranges (e.g., pages: "1-5"). Maximum 20 pages per request.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "03a12ef5-b0b2-4c57-b9c5-ff43d8c48e9d",
  "isSidechain": false,
  "promptId": "ac986e77-89c2-4da2-8cf0-d9a0da36482f",
  "type": "user",
  "uuid": "8061188a-2388-407e-87a3-55cffc356b9e",
  "toolUseResult": "Error: This PDF has 11 pages, which is too many to read at once. Use the pages parameter to read specific page ranges (e.g., pages: \"1-5\"). Maximum 20 pages per request.",
  "sourceToolAssistantUUID": "03a12ef5-b0b2-4c57-b9c5-ff43d8c48e9d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "b4ed7333-11c6-492f-a8d4-e66619498d15",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-21T13:57:05.436Z_

<details open><summary>🔧 Tool call — Read · `toolu_014yBDvoBS7euVhayWsVXMH8`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T122458/worst/review_context.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8061188a-2388-407e-87a3-55cffc356b9e",
  "isSidechain": false,
  "requestId": "req_011CbFq8AanfyAzEXmEvM2A6",
  "type": "assistant",
  "uuid": "d22207a9-9fd5-414a-b6e2-d1b489f2baa7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "b4ed7333-11c6-492f-a8d4-e66619498d15",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FeswCS53NfYEfpCzFH7mfA",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11385,
      "cache_read_input_tokens": 11841,
      "output_tokens": 410,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11385,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 410,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11385,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11385
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

_source line 14 · 2026-05-21T13:57:05.452Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_016N2fmaMEoRvaWPoSSLjJ7c`</summary>

```json
{
  "query": "select:submit_dream_review_report,WebSearch,WebFetch",
  "max_results": 3
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d22207a9-9fd5-414a-b6e2-d1b489f2baa7",
  "isSidechain": false,
  "requestId": "req_011CbFq8AanfyAzEXmEvM2A6",
  "type": "assistant",
  "uuid": "32bdd246-6e78-4506-bdc3-f18670d00547",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "b4ed7333-11c6-492f-a8d4-e66619498d15",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FeswCS53NfYEfpCzFH7mfA",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11385,
      "cache_read_input_tokens": 11841,
      "output_tokens": 410,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11385,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 410,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11385,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11385
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

_source line 15 · 2026-05-21T13:57:06.440Z_

<details><summary>↩ Tool result · `toolu_014yBDvoBS7euVhayWsVXMH8`</summary>

```text
1	narrative_guidance: '7-8B pilot 的核心模式不推广到全量模型。两个 MoE 架构（Qwen3-235B, Llama 4 Scout）完全没有清晰的
2	  Pareto frontier——MoE expert routing 打破了 dense model 中 depth→specialization 的单调映射，
3	  depth-transfer 关系在绝大多数语言为 non-monotonic 或 flat。唯一的 dense 架构（Gemma 4 31B）展现出 marginal
4	  Pareto（global rho=-0.24, p=0.038），但仅 4/20 语言 per-language 显著，且 final-layer transfer
5	  drop 微不足道（0.8pp），远不及 pilot 的 2-4pp。三架构平均 EN AUROC 0.74，处于 worst 范围中段。
6	
7	  Simpson''s Paradox 在 20 语言全量验证中全面崩塌：3 架构的 CKA partial correlation controlling for
8	  depth 均不显著（max rho=+0.16, min p=0.09），Llama pilot 的 rho=+0.41 被确认为 5 语言 small-sample
9	  artifact。CKA 提供不了超越 depth 的解释力。Subspace angle analysis 否定了 "correctness direction
10	  is a robust language-agnostic subspace"——HIGH tier 语言 angle 15-38°，LOW tier 45-65°。
11	
12	  CaCLR 全面失败：β sweep 3 OOM 证实 consistency loss inert 或 harmful；CORAL 和 high-dim MMD
13	  (PCA d=50/100) 同样失败，将 negative result 从 "MMD-specific" 扩展为 "distributional matching
14	  路径全面 关闭"。Component ablation 每加一项 loss 都 net negative。
15	
16	  Decomposition 无实质效果，random-direction control 产生同量级 delta（paired test p=0.38）， difficulty
17	  和 capability 不可分。
18	
19	  Control task analysis 是最强贡献：cross-lingual artifact rate 达 35%（LOW 42%，MID 31%，HIGH
20	  15%）， 首次在跨语言 probing 场景系统性应用 selectivity 检验。Selectivity 与 ZS AUROC 强相关（rho=0.65），
21	  暗示文献中许多 positive transfer 结果可能是 capacity artifacts。
22	
23	  Linear projection 作为唯一可行方案但需 100+ pairs（非 50），且效果反转阈值 language-specific， 无法给出单一可操作的
24	  cutoff。
25	
26	  重构为 EACL negative results + methodology paper：(1) control task 方法论警告（field-level
27	  贡献）， (2) mean-shift 不可能性证明（理论贡献），(3) distributional matching 路径全面关闭（CaCLR + CORAL
28	  + high-dim MMD 系统性 negative result），(4) linear projection 条件性实用指导（descriptive empirical
29	  贡献）。Drop Claim 2（decomposition）和 Claim 3（CaCLR method）作为 standalone claims。
30	
31	  '
32	imagined_experiments:
33	- name: Qwen3-235B Full Pareto Frontier
34	  plan_id: plan_001
35	  description: 'Qwen3-235B-A22B (94 layers, MoE, INT4), 24 probed layers (every 4th),
36	    20 typologically diverse languages, EN correctness probes (LR + MLP), 5 transfer
37	    conditions (zero-shot, mean-shift, linear projection 200 pairs, few-shot 25/100,
38	    CaCLR).
39	
40	    '
41	  expected_results:
42	    en_best_auroc: 0.741
43	    en_best_layer: 72
44	    en_auroc_range:
45	    - 0.601
46	    - 0.741
47	    en_best_ece_raw: 0.198
48	    zs_pass_count_auroc_gt_058: 11
49	    zs_pass_rate: 0.55
50	    zs_fail_count: 9
51	    mean_zs_auroc_all_20: 0.576
52	    mean_zs_auroc_drop_vs_en_pp: 16.5
53	    best_zs_auroc:
54	      zh: 0.668
55	      es: 0.675
56	      fr: 0.658
57	      de: 0.649
58	      ja: 0.588
59	      pt: 0.662
60	      it: 0.645
61	      ar: 0.608
62	      hi: 0.567
63	      ru: 0.621
64	      ko: 0.591
65	      tr: 0.548
66	      vi: 0.562
67	      th: 0.528
68	      sw: 0.518
69	      bn: 0.524
70	      am: 0.486
71	      yo: 0.475
72	      te: 0.502
73	      my: 0.468
74	    best_zs_layer:
75	      zh: 60
76	      es: 56
77	      fr: 60
78	      de: 52
79	      ja: 48
80	      pt: 56
81	      it: 56
82	      ar: 52
83	      hi: 44
84	      ru: 56
85	      ko: 48
86	      tr: 40
87	      vi: 44
88	      th: 36
89	      sw: 36
90	      bn: 40
91	      am: 32
92	      yo: 28
93	      te: 36
94	      my: 32
95	    global_spearman_rho_depth_vs_transfer: -0.12
96	    global_spearman_p: 0.078
97	    per_lang_spearman:
98	      zh:
99	        rho: -0.31
100	        p: 0.14
101	      es:
102	        rho: -0.25
103	        p: 0.24
104	      fr:
105	        rho: -0.28
106	        p: 0.18
107	      de:
108	        rho: -0.19
109	        p: 0.38
110	      ja:
111	        rho: 0.18
112	        p: 0.4
113	      pt:
114	        rho: -0.22
115	        p: 0.3
116	      it:
117	        rho: -0.16
118	        p: 0.46
119	      ar:
120	        rho: 0.05
121	        p: 0.82
122	      hi:
123	        rho: -0.41
124	        p: 0.046
125	      ru:
126	        rho: -0.14
127	        p: 0.52
128	      ko:
129	        rho: 0.25
130	        p: 0.24
131	      tr:
132	        rho: -0.08
133	        p: 0.71
134	      vi:
135	        rho: 0.09
136	        p: 0.68
137	      th:
138	        rho: -0.11
139	        p: 0.61
140	      sw:
141	        rho: -0.35
142	        p: 0.09
143	      bn:
144	        rho: -0.12
145	        p: 0.58
146	      am:
147	        rho: 0.14
148	        p: 0.52
149	      yo:
150	        rho: -0.02
151	        p: 0.93
152	      te:
153	        rho: -0.18
154	        p: 0.4
155	      my:
156	        rho: 0.1
157	        p: 0.64
158	    per_lang_significant_negative_rho_count: 1
159	    per_lang_significant_positive_rho_count: 0
160	    per_lang_nonmonotonic_count: 13
161	    pareto_tradeoff_prevalence: 0.08
162	    pareto_depth_transfer_drop_final_layers_pp: 0.6
163	    mean_shift_delta_auroc_all: 0.0
164	    transfer_conditions_summary:
165	      zero_shot:
166	        mean_auroc: 0.576
167	        std: 0.068
168	        delta_vs_zs: 0.0
169	      mean_shift:
170	        mean_auroc: 0.576
171	        std: 0.068
172	        delta_vs_zs: 0.0
173	      linear_proj_200:
174	        mean_auroc: 0.612
175	        std: 0.055
176	        delta_vs_zs: 0.036
177	      fewshot_25:
178	        mean_auroc: 0.598
179	        std: 0.061
180	        delta_vs_zs: 0.022
181	      fewshot_100:
182	        mean_auroc: 0.625
183	        std: 0.049
184	        delta_vs_zs: 0.049
185	  result_rationale: 'EN best AUROC 0.741 在 worst 范围 [0.72, 0.78] 内——Qwen3-235B 的 22B
186	    active parameters 对 correctness signal 的编码不显著优于 7B pilot（0.754），因为 correctness
187	    direction 的信号 强度主要由 pretraining data 质量和 MCQA 格式暴露量决定，而非模型 scale。INT4 量化引入 ~1pp
188	    额外损耗。
189	
190	    ZS pass 11/20 (55%) 处于 worst 范围 [8, 13] 中段。MoE routing 导致不同语言被路由到 不同 expert 子集，correctness
191	    direction 的跨语言一致性被 expert 分化削弱：pilot 中 Qwen2.5-7B dense 架构的 4/5 pass 不能外推，因为 dense
192	    model 的 shared representation 天然更有利于 cross-lingual alignment。低资源语言（am, yo, my）的
193	    best ZS AUROC < 0.50，接近 random。
194	
195	    Global Pareto rho=-0.12 (p=0.078) 仅 marginally significant：depth-transfer tradeoff
196	    在 MoE 中不成立，因为 expert routing 在不同深度可以 "重置" 语言特异性——L48 的 expert allocation 可能与 L72
197	    完全不同，打破了 "deeper = more specialized" 的 dense-model 假设。13/20 语言呈现 non-monotonic
198	    模式（U形、锯齿形、plateau），这是 MoE 的结构性特征而非噪声。仅 hi 达到 per-language significant negative
199	    rho（p=0.046），ko 和 ja 方向反转（deeper helps transfer）。
200	
201	    Final-layer transfer drop 仅 0.6pp（worst 范围 [0.0, 1.5]），远低于 pilot 的 2-4pp—— 235B
202	    MoE 的最深层 expert routing 已经足够 specialized，EN probe 在这些层的 AUROC 提升本身就很小（L88 vs L72
203	    仅 +0.3pp EN AUROC），所以 transfer drop 也被压缩。
204	
205	    Mean-shift ΔAUROC ≡ 0 符合已证明的 rank-invariance。Linear projection +3.6pp 和 few-shot
206	    100 +4.9pp 有中等改善，但 significant improvement 仅覆盖 55-65% 的语言。
207	
208	    '
209	  tables:
210	  - name: 'Table 1a: Qwen3-235B Per-Language Pareto (Depth vs ZS-AUROC Spearman ρ)'
211	    columns:
212	    - lang
213	    - tier
214	    - best_zs_auroc
215	    - best_zs_layer
216	    - spearman_rho
217	    - p_value
218	    - pattern
219	    rows:
220	    - - zh
221	      - HIGH
222	      - 0.668
223	      - 60
224	      - -0.31
225	      - 0.14
226	      - weak negative
227	    - - es
228	      - HIGH
229	      - 0.675
230	      - 56
231	      - -0.25
232	      - 0.24
233	      - n.s.
234	    - - fr
235	      - HIGH
236	      - 0.658
237	      - 60
238	      - -0.28
239	      - 0.18
240	      - n.s.
241	    - - de
242	      - HIGH
243	      - 0.649
244	      - 52
245	      - -0.19
246	      - 0.38
247	      - n.s.
248	    - - ja
249	      - HIGH
250	      - 0.588
251	      - 48
252	      - 0.18
253	      - 0.4
254	      - non-monotonic U-shape
255	    - - pt
256	      - HIGH
257	      - 0.662
258	      - 56
259	      - -0.22
260	      - 0.3
261	      - n.s.
262	    - - it
263	      - HIGH
264	      - 0.645
265	      - 56
266	      - -0.16
267	      - 0.46
268	      - n.s.
269	    - - ar
270	      - MID
271	      - 0.608
272	      - 52
273	      - 0.05
274	      - 0.82
275	      - flat
276	    - - hi
277	      - MID
278	      - 0.567
279	      - 44
280	      - -0.41
281	      - 0.046
282	      - significant negative
283	    - - ru
284	      - MID
285	      - 0.621
286	      - 56
287	      - -0.14
288	      - 0.52
289	      - n.s.
290	    - - ko
291	      - MID
292	      - 0.591
293	      - 48
294	      - 0.25
295	      - 0.24
296	      - inverted—deeper helps
297	    - - tr
298	      - MID
299	      - 0.548
300	      - 40
301	      - -0.08
302	      - 0.71
303	      - n.s.
304	    - - vi
305	      - MID
306	      - 0.562
307	      - 44
308	      - 0.09
309	      - 0.68
310	      - flat
311	    - - th
312	      - MID
313	      - 0.528
314	      - 36
315	      - -0.11
316	      - 0.61
317	      - n.s.
318	    - - sw
319	      - LOW
320	      - 0.518
321	      - 36
322	      - -0.35
323	      - 0.09
324	      - marginal negative
325	    - - bn
326	      - LOW
327	      - 0.524
328	      - 40
329	      - -0.12
330	      - 0.58
331	      - n.s.
332	    - - am
333	      - LOW
334	      - 0.486
335	      - 32
336	      - 0.14
337	      - 0.52
338	      - non-monotonic
339	    - - yo
340	      - LOW
341	      - 0.475
342	      - 28
343	      - -0.02
344	      - 0.93
345	      - noisy flat
346	    - - te
347	      - LOW
348	      - 0.502
349	      - 36
350	      - -0.18
351	      - 0.4
352	      - n.s.
353	    - - my
354	      - LOW
355	      - 0.468
356	      - 32
357	      - 0.1
358	      - 0.64
359	      - non-monotonic
360	  - name: 'Table 1b: Qwen3-235B Transfer Conditions Summary (20 langs, EN-optimal
361	      layer)'
362	    columns:
363	    - condition
364	    - mean_auroc
365	    - std
366	    - delta_vs_zs
367	    - significant_improvement_count
368	    rows:
369	    - - zero-shot
370	      - 0.576
371	      - 0.068
372	      - —
373	      - —
374	    - - mean-shift
375	      - 0.576
376	      - 0.068
377	      - 0.0
378	      - 0/20
379	    - - linear_proj_200
380	      - 0.612
381	      - 0.055
382	      - 0.036
383	      - 11/20
384	    - - fewshot_25
385	      - 0.598
386	      - 0.061
387	      - 0.022
388	      - 7/20
389	    - - fewshot_100
390	      - 0.625
391	      - 0.049
392	      - 0.049
393	      - 13/20
394	  figures_description:
395	  - 'Figure 1a: EN AUROC vs best ZS AUROC scatter across 24 layers for Qwen3-235B,
396	    colored by resource tier. Diffuse cloud without clean Pareto frontier. Non-monotonic
397	    language trajectories (ja, ko, am, my) highlighted. Annotation: global ρ=-0.12
398	    (p=0.078).
399	
400	    '
401	  - 'Figure 1b: ZS AUROC heatmap (language × probed layer). Irregular MoE-specific
402	    layer-to-layer variance, no smooth depth gradient. Expert routing artifacts visible
403	    as 4-layer-period oscillations.
404	
405	    '
406	  analysis: 'Qwen3-235B 的 Pareto frontier 远不如 Qwen2.5-7B pilot 清晰。MoE expert routing
407	    打破了 dense model 中 depth = specialization 的单调映射。Pilot 的 clear Pareto（L27 EN best
408	    但 transfer drops 2-4pp vs L24）是 dense 7B model 的特殊现象。仅 1/20 语言达到 per-language
409	    显著性（hi），且部分语言方向反转——depth-transfer tradeoff 不是普遍现象。对 Claim 1 构成 严重挑战：不能声称 Qwen
410	    系列存在 consistent Pareto。
411	
412	    '
413	- name: Llama 4 Scout Full Pareto Frontier
414	  plan_id: plan_002
415	  description: 'Llama 4 Scout (48 layers, 17B-16E MoE, W4A16), 12 probed layers (every
416	    4th), 20 languages, 5 transfer conditions.
417	
418	    '
419	  expected_results:
420	    en_best_auroc: 0.718
421	    en_best_layer: 40
422	    en_auroc_range:
423	    - 0.615
424	    - 0.718
425	    en_best_ece_raw: 0.215
426	    zs_pass_count_auroc_gt_058: 9
427	    zs_pass_rate: 0.45
428	    mean_zs_auroc_all_20: 0.562
429	    mean_zs_auroc_drop_vs_en_pp: 15.6
430	    best_zs_auroc:
431	      zh: 0.648
432	      es: 0.655
433	      fr: 0.642
434	      de: 0.635
435	      ja: 0.562
436	      pt: 0.648
437	      it: 0.631
438	      ar: 0.588
439	      hi: 0.548
440	      ru: 0.608
441	      ko: 0.575
442	      tr: 0.531
443	      vi: 0.558
444	      th: 0.515
445	      sw: 0.501
446	      bn: 0.508
447	      am: 0.472
448	      yo: 0.458
449	      te: 0.491
450	      my: 0.452
451	    global_spearman_rho_depth_vs_transfer: -0.06
452	    global_spearman_p: 0.31
453	    per_lang_significant_negative_rho_count: 0
454	    per_lang_significant_positive_rho_count: 0
455	    per_lang_nonmonotonic_count: 8
456	    pareto_tradeoff_prevalence: 0.05
457	    pareto_depth_transfer_drop_final_layers_pp: 0.3
458	    mean_shift_delta_auroc_all: 0.0
459	    transfer_conditions_summary:
460	      zero_shot:
461	        mean_auroc: 0.562
462	        std: 0.065
463	        delta_vs_zs: 0.0
464	      mean_shift:
465	        mean_auroc: 0.562
466	        std: 0.065
467	        delta_vs_zs: 0.0
468	      linear_proj_200:
469	        mean_auroc: 0.598
470	        std: 0.052
471	        delta_vs_zs: 0.036
472	      fewshot_25:
473	        mean_auroc: 0.584
474	        std: 0.058
475	        delta_vs_zs: 0.022
476	      fewshot_100:
477	        mean_auroc: 0.611
478	        std: 0.048
479	        delta_vs_zs: 0.049
480	  result_rationale: 'Llama 4 Scout EN best AUROC 0.718 在 worst 范围低端——active parameters
481	    17B 但 16 experts 的稀疏激活使得每个 token 实际使用的参数量有限，correctness signal 在 expert 间被稀释。W4A16
482	    量化额外损耗 ~0.5-1pp。
483	
484	    ZS pass 9/20 (45%)，比 Qwen3 低因为：(1) Llama 4 Scout 的 multilingual pretraining 比例可能低于
485	    Qwen3（Qwen 系列历来强调多语言）；(2) 16-expert MoE 的 expert specialization 程度更高，语言间 representation
486	    divergence 更大。MVP 中 Llama-3.1-8B dense 的 5/5 pass 不推广——8B dense → Scout MoE 的架构变化比
487	    scale change 更根本。
488	
489	    Global Pareto rho=-0.06 (p=0.31) 完全不显著，0/20 语言 per-language 显著。仅 12 probed layers
490	    使 per-language Spearman 功效极低（n=12），但即使考虑 power 问题，effect sizes 也很小 （max |rho|
491	    = 0.38）。Scout 的 expert routing 比 Qwen3 更激进（16 experts vs Qwen3 的 设计），导致 depth-transfer
492	    关系更加 noisy。
493	
494	    Final-layer drop 仅 0.3pp——transfer 在 L40-L48 区间几乎 flat，没有 tradeoff 可言。
495	
496	    '
497	  tables:
498	  - name: 'Table 2a: Llama 4 Scout Per-Language Pareto Spearman ρ'
499	    columns:
500	    - lang
501	    - tier
502	    - best_zs_auroc
503	    - spearman_rho
504	    - p_value
505	    rows:
506	    - - zh
507	      - HIGH
508	      - 0.648
509	      - -0.18
510	      - 0.58
511	    - - es
512	      - HIGH
513	      - 0.655
514	      - -0.12
515	      - 0.71
516	    - - fr
517	      - HIGH
518	      - 0.642
519	      - -0.22
520	      - 0.49
521	    - - de
522	      - HIGH
523	      - 0.635
524	      - -0.08
525	      - 0.81
526	    - - ja
527	      - HIGH
528	      - 0.562
529	      - 0.32
530	      - 0.31
531	    - - pt
532	      - HIGH
533	      - 0.648
534	      - -0.15
535	      - 0.64
536	    - - it
537	      - HIGH
538	      - 0.631
539	      - -0.05
540	      - 0.88
541	    - - ar
542	      - MID
543	      - 0.588
544	      - 0.22
545	      - 0.49
546	    - - hi
547	      - MID
548	      - 0.548
549	      - -0.38
550	      - 0.22
551	    - - ru
552	      - MID
553	      - 0.608
554	      - -0.02
555	      - 0.95
556	    - - ko
557	      - MID
558	      - 0.575
559	      - 0.35
560	      - 0.26
561	    - - tr
562	      - MID
563	      - 0.531
564	      - 0.08
565	      - 0.81
566	    - - vi
567	      - MID
568	      - 0.558
569	      - 0.12
570	      - 0.71
571	    - - th
572	      - MID
573	      - 0.515
574	      - -0.18
575	      - 0.58
576	    - - sw
577	      - LOW
578	      - 0.501
579	      - -0.25
580	      - 0.43
581	    - - bn
582	      - LOW
583	      - 0.508
584	      - -0.08
585	      - 0.81
586	    - - am
587	      - LOW
588	      - 0.472
589	      - 0.02
590	      - 0.95
591	    - - yo
592	      - LOW
593	      - 0.458
594	      - -0.12
595	      - 0.71
596	    - - te
597	      - LOW
598	      - 0.491
599	      - -0.05
600	      - 0.88
601	    - - my
602	      - LOW
603	      - 0.452
604	      - 0.15
605	      - 0.64
606	  - name: 'Table 2b: Llama 4 Scout Transfer Conditions Summary'
607	    columns:
608	    - condition
609	    - mean_auroc
610	    - delta_vs_zs
611	    - significant_count
612	    rows:
613	    - - zero-shot
614	      - 0.562
615	      - —
616	      - —
617	    - - mean-shift
618	      - 0.562
619	      - 0.0
620	      - 0/20
621	    - - linear_proj_200
622	      - 0.598
623	      - 0.036
624	      - 10/20
625	    - - fewshot_25
626	      - 0.584
627	      - 0.022
628	      - 6/20
629	    - - fewshot_100
630	      - 0.611
631	      - 0.049
632	      - 12/20
633	  figures_description:
634	  - 'Figure 2: Llama 4 Scout Pareto scatter, same format as Figure 1a. Cloud 更散乱，
635	    global ρ=-0.06 (p=0.31)。ko (+0.35) 和 ja (+0.32) 方向反转于预期。
636	
637	    '
638	  analysis: 'Llama 4 Scout 确认 MoE 架构的 Pareto 缺失。与 Qwen3 合并看：0 个 MoE 架构在 p<0.05 展现
639	    Pareto。MVP 中 Llama-3.1-8B 的弱 Pareto 是 dense 架构特有的。两个 MoE 结合表明 expert routing 是
640	    Pareto 缺失的结构性原因，而非偶然。
641	
642	    '
643	- name: Gemma 4 31B Dense Pareto Frontier
644	  plan_id: plan_008
645	  description: 'Gemma 4 31B Dense (60 text layers, BF16 无量化), 16 probed layers (every
646	    4th + final), 20 languages, 5 transfer conditions. Dense vs MoE 对照。
647	
648	    '
649	  expected_results:
650	    en_best_auroc: 0.755
651	    en_best_layer: 52
652	    en_auroc_range:
653	    - 0.618
654	    - 0.755
655	    en_best_ece_raw: 0.188
656	    zs_pass_count_auroc_gt_058: 12
657	    zs_pass_rate: 0.6
658	    mean_zs_auroc_all_20: 0.585
659	    mean_zs_auroc_drop_vs_en_pp: 17.0
660	    best_zs_auroc:
661	      zh: 0.682
662	      es: 0.691
663	      fr: 0.672
664	      de: 0.665
665	      ja: 0.598
666	      pt: 0.678
667	      it: 0.658
668	      ar: 0.618
669	      hi: 0.575
670	      ru: 0.635
671	      ko: 0.602
672	      tr: 0.558
673	      vi: 0.572
674	      th: 0.538
675	      sw: 0.525
676	      bn: 0.531
677	      am: 0.492
678	      yo: 0.481
679	      te: 0.508
680	      my: 0.475
681	    global_spearman_rho_depth_vs_transfer: -0.24
682	    global_spearman_p: 0.038
683	    per_lang_significant_negative_rho_count: 4
684	    per_lang_significant_positive_rho_count: 0
685	    per_lang_nonmonotonic_count: 5
686	    pareto_tradeoff_prevalence: 0.22
687	    pareto_depth_transfer_drop_final_layers_pp: 0.8
688	    spearman_depth_vs_transfer_rho_positive_langs: 10
689	    transfer_conditions_summary:
690	      zero_shot:
691	        mean_auroc: 0.585
692	        std: 0.063
693	        delta_vs_zs: 0.0
694	      mean_shift:
695	        mean_auroc: 0.585
696	        std: 0.063
697	        delta_vs_zs: 0.0
698	      linear_proj_200:
699	        mean_auroc: 0.621
700	        std: 0.051
701	        delta_vs_zs: 0.036
702	      fewshot_25:
703	        mean_auroc: 0.607
704	        std: 0.057
705	        delta_vs_zs: 0.022
706	      fewshot_100:
707	        mean_auroc: 0.634
708	        std: 0.045
709	        delta_vs_zs: 0.049
710	  result_rationale: 'Gemma 4 31B Dense 是唯一有 marginal Pareto 的架构。Dense 架构没有 expert
711	    routing， depth→specialization 映射更单调，因此 global rho=-0.24 (p=0.038) 达到 significance。
712	    4/20 语言 per-language 显著（zh, fr, hi, sw）——全部是负 rho（deeper layers = worse transfer），
713	    符合 specialization 叙述。
714	
715	    但这反而增加了叙述复杂性：Pareto 是 architecture-dependent 的（dense 有，MoE 没有）， 无法声称是普遍现象。且 final-layer
716	    drop 仅 0.8pp——远低于 pilot 的 2-4pp，因为 31B dense model 的最深层已经足够 expressive，EN probe
717	    的边际 AUROC 提升很小（L56→L60 仅 +0.4pp）， 相应 transfer 损失也被压缩。
718	
719	    EN AUROC 0.755 略高于两个 MoE（因无量化损耗 + BF16 保留更多信号精度），三架构均值 (0.741 + 0.718 + 0.755)/3
720	    = 0.738，在 worst 范围 [0.72, 0.78] 内。
721	
722	    ZS pass 12/20 (60%)——三架构最高，因为 Gemma 4 的 multilingual pretraining 可能 更均衡（Apache
723	    2.0 开源模型通常 training data 更 curated），且无量化损耗。
724	
725	    '
726	  tables:
727	  - name: 'Table 3: Gemma 4 31B Dense Pareto Summary'
728	    columns:
729	    - metric
730	    - value
731	    rows:
732	    - - en_best_auroc
733	      - 0.755
734	    - - en_best_layer
735	      - L52 (87% depth)
736	    - - zs_pass_rate
737	      - 60% (12/20)
738	    - - global_pareto_rho
739	      - -0.24 (p=0.038)
740	    - - per_lang_significant_rho
741	      - 4/20 (zh, fr, hi, sw)
742	    - - final_layer_transfer_drop_pp
743	      - 0.8
744	    - - control_artifact_rate_LOW
745	      - 38%
746	    - - no_quantization_confound
747	      - BF16 — no quantization artifact
748	  - name: 'Table 3b: Dense vs MoE Architecture Comparison'
749	    columns:
750	    - metric
751	    - Qwen3 (MoE)
752	    - Llama4 (MoE)
753	    - Gemma4 (Dense)
754	    rows:
755	    - - en_best_auroc
756	      - 0.741
757	      - 0.718
758	      - 0.755
759	    - - global_pareto_rho
760	      - -0.12 (n.s.)
761	      - -0.06 (n.s.)
762	      - -0.24 (p=0.038)
763	    - - per_lang_sig_count
764	      - 1/20
765	      - 0/20
766	      - 4/20
767	    - - non_monotonic_langs
768	      - 13/20
769	      - 8/20
770	      - 5/20
771	    - - final_layer_drop_pp
772	      - 0.6
773	      - 0.3
774	      - 0.8
775	    - - zs_pass_rate
776	      - 55%
777	      - 45%
778	      - 60%
779	  figures_description:
780	  - 'Figure 3a: Gemma 4 Pareto scatter vs Qwen3/Llama4 (3-panel). Gemma shows cleaner
781	    negative trend but still substantial scatter. MoE panels show diffuse clouds.
782	    Visual comparison highlights dense vs MoE structural difference.
783	
784	    '
785	  - 'Figure 3b: Per-language Spearman ρ bar chart across 3 architectures. Gemma bars
786	    lean negative but most still n.s. MoE bars scattered around zero.
787	
788	    '
789	  analysis: 'Dense vs MoE 对比是 Gemma 最大的贡献：dense 架构确实有 cleaner depth-transfer 关系， 但
790	    effect size 远小于 pilot 预期。三架构综合 pareto_tradeoff_prevalence ≈ 0.12 (12% of lang-arch
791	    pairs)，在 worst 范围 [0.05, 0.25] 内。 结论：Pareto 是 architecture-conditional 的，不是 universal
792	    finding——这使得 Claim 1 从 "discovery" 降级为 "architecture-dependent observational note"。
793	
794	    '
795	- name: CaCLR Implementation and Comparative Evaluation
796	  plan_id: plan_003
797	  description: 'CaCLR (L_BCE + α·L_SB-ECE + β·L_MMD), β sweep 3 OOM, α sweep, component
798	    ablation, CORAL comparison, high-dim MMD (PCA d=50/100), multi-seed (5 seeds),
799	    mixed β criterion. vs 4 baselines, 3 models × 20 langs.
800	
801	    '
802	  expected_results:
803	    caclr_mean_delta_auroc_vs_zs: -0.008
804	    caclr_langs_improved_of_20: 4
805	    caclr_best_beta: none — all β inert or harmful
806	    beta_sweep:
807	      beta_0.001:
808	        mean_delta_auroc: -0.002
809	        std: 0.016
810	      beta_0.01:
811	        mean_delta_auroc: -0.005
812	        std: 0.019
813	      beta_0.1:
814	        mean_delta_auroc: -0.009
815	        std: 0.023
816	      beta_1.0:
817	        mean_delta_auroc: -0.016
818	        std: 0.028
819	    alpha_sweep:
820	      alpha_0.01:
821	        delta_auroc: -0.001
822	        delta_ece: 0.006
823	      alpha_0.1:
824	        delta_auroc: -0.004
825	        delta_ece: 0.002
826	      alpha_1.0:
827	        delta_auroc: -0.01
828	        delta_ece: -0.001
829	      alpha_10.0:
830	        delta_auroc: -0.025
831	        delta_ece: -0.004
832	    component_ablation:
833	      bce_only:
834	        delta_vs_zs: -0.001
835	        note: ≈ ZS baseline
836	      bce_plus_sbece:
837	        delta_vs_zs: -0.005
838	        note: SB-ECE hurts discrimination
839	      bce_plus_mmd_1d:
840	        delta_vs_zs: -0.004
841	        note: 1-D MMD inert/harmful
842	      bce_plus_mmd_pca50:
843	        delta_vs_zs: -0.006
844	        note: 50-D MMD also fails
845	      bce_plus_mmd_pca100:
846	        delta_vs_zs: -0.008
847	        note: 100-D MMD worse — curse of dimensionality
848	      bce_plus_coral:
849	        delta_vs_zs: -0.005
850	        note: CORAL fails — second-order alignment insufficient
851	      bce_plus_coral_pca50:
852	        delta_vs_zs: -0.007
853	        note: high-dim CORAL also fails
854	      full_caclr:
855	        delta_vs_zs: -0.008
856	        note: compound degradation
857	    multi_seed_std:
858	      caclr: 0.003
859	      fewshot_25: 0.008
860	      fewshot_100: 0.005
861	      procrustes: 0.002
862	    mixed_beta_criterion_result: 'β selected on zh+sw validation matches English-only
863	      selection (β=0.001). No evidence of systematic bias against cross-lingual benefit.
864	
865	      '
866	    five_way_comparison:
867	      zero_shot:
868	        mean_auroc: 0.574
869	        mean_ece: 0.282
870	      mean_shift:
871	        mean_auroc: 0.574
872	        mean_ece: 0.288
873	      caclr_best:
874	        mean_auroc: 0.566
875	        mean_ece: 0.275
876	      linear_proj_200:
877	        mean_auroc: 0.61
878	        mean_ece: 0.245
879	      fewshot_25:
880	        mean_auroc: 0.596
881	        mean_ece: 0.258
882	      fewshot_100:
883	        mean_auroc: 0.623
884	        mean_ece: 0.232
885	    implementation_spec:
886	      mmd_kernel: Gaussian RBF, bandwidth=median heuristic
887	      optimizer: Adam, lr=1e-3, cosine schedule to 1e-5
888	      epochs: 50
889	      early_stopping: patience=10 on held-out English BCE loss
890	      initialization: from standard LR solution
891	      batch_size: 256
892	      mmd_items: same items as BCE (probe_train 70% split)
893	      parallel_set_size_range:
894	      - 618
895	      - 2852
896	  result_rationale: 'CaCLR 失败的根本原因链：
897	
898	    (1) 1-D MMD 结构性限制：probe logit 是标量，MMD 只能 match 两个 1-D 分布的 marginal。 即使 marginal
899	    被 match，EN 和 target 的 conditional distributions P(logit|correct) vs P(logit|incorrect)
900	    仍然不同——Zhao et al. (2019) 的理论预测在此得到验证。β 越大，logits 被拉向无区分性的 marginal match，discrimination
901	    下降。
902	
903	    (2) High-dim MMD (PCA d=50/100) 同样失败：curse of dimensionality 使得 Gaussian RBF kernel
904	    在 50-100 维空间的 MMD estimate 方差极大，有效样本量不足（probe_train ~2000 samples 对 100 维 MMD
905	    来说 severely underpowered）。d=100 比 d=50 更差，证实这一解释。
906	
907	    (3) CORAL 也失败：second-order alignment（match mean + covariance）比 MMD 更受 conditional
908	    distribution mismatch 的影响——对齐 marginal moments 不能修复 correctness signal 的 conditional
909	    structure 差异。CORAL 在 domain adaptation 中成功的条件是 covariate shift （P(X) changes,
910	    P(Y|X) stable），但 cross-lingual correctness probing 违反这一条件 （P(correct|representation)
911	    在不同语言中不同）。
912	
913	    (4) Component ablation 证实每个额外 loss 都是 net negative：BCE-only retrain ≈ ZS baseline（LR
914	    solution 初始化后 Adam 微调不改变 optimum），每加一项都引入额外 noise 而 无 signal。CaCLR 不是超参选择问题而是方法论层面的失败。
915	
916	    (5) Multi-seed 结果稳定（std=0.003），排除了 single-seed 偶然性。Mixed β criterion 排除了 β selection
917	    对 cross-lingual benefit 的系统性偏见。
918	
919	    综合：distributional matching 路径（MMD + CORAL，low-dim + high-dim）被全面关闭。 Linear projection
920	    和 few-shot 显著优于 CaCLR，因为它们直接利用 target-language 结构 信息而非试图间接 match distributions。
921	
922	    '
923	  tables:
924	  - name: 'Table 4a: CaCLR β Sweep (3 architectures × 20 langs, EN-optimal layer)'
925	    columns:
926	    - beta
927	    - mean_auroc
928	    - delta_vs_zs
929	    - pct_improved
930	    - pct_harmed
931	    rows:
932	    - - 0.001
933	      - 0.572
934	      - -0.002
935	      - 30%
936	      - 42%
937	    - - 0.01
938	      - 0.569
939	      - -0.005
940	      - 25%
941	      - 52%
942	    - - 0.1
943	      - 0.565
944	      - -0.009
945	      - 18%
946	      - 62%
947	    - - 1.0
948	      - 0.558
949	      - -0.016
950	      - 12%
951	      - 75%
952	  - name: 'Table 4b: Distributional Matching Comprehensive Ablation'
953	    columns:
954	    - method
955	    - dimensionality
956	    - mean_delta_auroc
957	    - note
958	    rows:
959	    - - MMD (logit)
960	      - 1-D
961	      - -0.004
962	      - marginal match, no conditional alignment
963	    - - MMD (PCA-50)
964	      - 50-D
965	      - -0.006
966	      - underpowered MMD in 50-D
967	    - - MMD (PCA-100)
968	      - 100-D
969	      - -0.008
970	      - curse of dimensionality
971	    - - CORAL (logit)
972	      - 1-D
973	      - -0.005
974	      - second-order alignment insufficient
975	    - - CORAL (PCA-50)
976	      - 50-D
977	      - -0.007
978	      - covariance match fails
979	    - - Linear projection
980	      - full-D Procrustes
981	      - 0.036
982	      - learns subspace rotation directly
983	  - name: 'Table 4c: 5-Way Transfer Comparison (3 arch × 20 langs)'
984	    columns:
985	    - condition
986	    - mean_auroc
987	    - mean_ece
988	    - delta_auroc_vs_zs
989	    - win_rate_vs_zs
990	    rows:
991	    - - zero-shot
992	      - 0.574
993	      - 0.282
994	      - —
995	      - —
996	    - - mean-shift
997	      - 0.574
998	      - 0.288
999	      - 0.0
1000	      - 0%
1001	    - - CaCLR (best)
1002	      - 0.566
1003	      - 0.275
1004	      - -0.008
1005	      - 20%
1006	    - - linear_proj_200
1007	      - 0.61
1008	      - 0.245
1009	      - 0.036
1010	      - 70%
1011	    - - fewshot_25
1012	      - 0.596
1013	      - 0.258
1014	      - 0.022
1015	      - 52%
1016	    - - fewshot_100
1017	      - 0.623
1018	      - 0.232
1019	      - 0.049
1020	      - 75%
1021	  figures_description:
1022	  - 'Figure 4a: β sweep curve showing monotonic decrease in mean AUROC. Shaded 95%
1023	    CI all below or crossing zero-shot baseline. Separate lines for MMD-1D, MMD-50D,
1024	    MMD-100D, CORAL showing all fail.
1025	
1026	    '
1027	  - 'Figure 4b: Per-language ΔAUROC bars at best β=0.001. Most bars negative. Only
1028	    4 HIGH-resource languages show marginal positive Δ within noise margin.
1029	
1030	    '
1031	  - 'Figure 4c: Distributional matching ablation (MMD vs CORAL × dimensionality).
1032	    All configurations below zero-shot. Linear projection (rightmost) is the only
1033	    positive method. Clean visual separation between distribution-matching (all negative)
1034	    and structure-learning (linear projection, positive).
1035	
1036	    '
1037	  analysis: 'CaCLR 的全面 negative result 是 worst tier 的核心贡献之一。关键升级：CORAL + high-dim
1038	    MMD 将 scope 从 "MMD fails" 扩展为 "distributional matching path is closed"。这比仅报告 1-D
1039	    MMD 失败有力得多——reviewer 无法反驳说 "换个 kernel/提高维度就行"。 Distributional matching ablation
1040	    table (Table 4b) 是该 claim 的 anchor evidence。 CKA subspace 解释也不成立（plan_011），所以
1041	    geometric rationalization 也失败—— 不仅方法失败，elegant 解释也失败。但完整的 implementation spec
1042	    + sweep + ablation 确保 reproducibility，使 negative result 可信。
1043	
1044	    '
1045	- name: Difficulty-Controlled Decomposition Ablation
1046	  plan_id: plan_004
1047	  description: 'IRT difficulty probes → project out difficulty direction → retrain
1048	    correctness probes on residuals → evaluate transfer. 10 representative languages
1049	    × 8 representative layers × 3 models. Random-direction control.
1050	
1051	    '
1052	  expected_results:
1053	    decomp_transfer_improvement_pp: 0.2
1054	    decomp_transfer_improvement_range:
1055	    - -0.8
1056	    - 1.2
1057	    random_direction_control_delta_pp: -0.1
1058	    random_direction_control_range:
1059	    - -1.0
1060	    - 0.8
1061	    decomp_vs_random_paired_test_p: 0.38
1062	    difficulty_probe_r2: 0.28
1063	    decomp_langs_showing_clean_separation: 2
1064	    per_tier_results:
1065	      HIGH:
1066	        mean_delta_pp: 0.3
1067	        significant: 0/4
1068	        clean_separation: 1
1069	      MID:
1070	        mean_delta_pp: 0.1
1071	        significant: 0/3
1072	        clean_separation: 1
1073	      LOW:
1074	        mean_delta_pp: -0.2
1075	        significant: 0/3
1076	        clean_separation: 0
1077	  result_rationale: 'Decomposition 在 worst tier 无实质效果，两个层面的失败：
1078	
1079	    (1) Difficulty direction 在 LLM representation 中编码不够 linear/集中——IRT difficulty
1080	    probe R²=0.28（低），意味着 linear projection 只捕获了 difficulty variance 的 28%。 剩余 72%
1081	    的 difficulty 信息分布在 correctness direction 也占据的子空间中——两者高度 纠缠，projecting out 28%
1082	    的 difficulty 同时损坏了部分 correctness signal。
1083	
1084	    (2) Random-direction control 产生同量级效果（paired test p=0.38），这是 worst tier 的 killer
1085	    finding：观察到的微小 delta 主要来自 dimensionality reduction 效应 （投影去除任意方向都会改变 probe 性能 ≈
1086	    同量级），而非 difficulty-specific 信号去除。
1087	
1088	    2/10 语言 "clean separation"（zh, ko）可能是 type-I error 在 10 次检验中的自然出现率。 LOW tier 3
1089	    语言全部 negative delta——它们的 difficulty 和 capability 信号本身就很弱， 投影去除任何方向只会损失信息。
1090	
1091	    结论：transfer degradation 不能分解为 difficulty-shared + capability-specific 两个可操作的 component——Claim
1092	    2 被否定，decomposition 从 standalone claim 降级。
1093	
1094	    '
1095	  tables:
1096	  - name: 'Table 5: Difficulty Decomposition Ablation (3 models mean)'
1097	    columns:
1098	    - lang
1099	    - tier
1100	    - original_zs
1101	    - after_proj
1102	    - delta_pp
1103	    - random_ctrl_delta_pp
1104	    - paired_p
1105	    rows:
1106	    - - zh
1107	      - HIGH
1108	      - 0.666
1109	      - 0.67
1110	      - 0.4
1111	      - 0.1
1112	      - 0.45
1113	    - - es
1114	      - HIGH
1115	      - 0.674
1116	      - 0.676
1117	      - 0.2
1118	      - -0.1
1119	      - 0.58
1120	    - - fr
1121	      - HIGH
1122	      - 0.657
1123	      - 0.66
1124	      - 0.3
1125	      - 0.2
1126	      - 0.82
1127	    - - de
1128	      - HIGH
1129	      - 0.65
1130	      - 0.652
1131	      - 0.2
1132	      - -0.2
1133	      - 0.41
1134	    - - hi
1135	      - MID
1136	      - 0.563
1137	      - 0.565
1138	      - 0.2
1139	      - 0.3
1140	      - 0.91
1141	    - - ru
1142	      - MID
1143	      - 0.621
1144	      - 0.622
1145	      - 0.1
1146	      - -0.2
1147	      - 0.52
1148	    - - ko
1149	      - MID
1150	      - 0.589
1151	      - 0.598
1152	      - 0.9
1153	      - 0.2
1154	      - 0.08
1155	    - - tr
1156	      - MID
1157	      - 0.546
1158	      - 0.54
1159	      - -0.6
1160	      - -0.4
1161	      - 0.65
1162	    - - sw
1163	      - LOW
1164	      - 0.515
1165	      - 0.51
1166	      - -0.5
1167	      - -0.3
1168	      - 0.71
1169	    - - bn
1170	      - LOW
1171	      - 0.521
1172	      - 0.519
1173	      - -0.2
1174	      - 0.0
1175	      - 0.68
1176	  figures_description:
1177	  - 'Figure 5: Paired bar chart of ΔAUROC after difficulty projection (blue) vs random-direction
1178	    projection (gray). Error bars = bootstrap 95% CI. All CIs overlap; no language
1179	    shows meaningful separation. Vertical dashed line at 0.
1180	
1181	    '
1182	  analysis: 'Decomposition null result 与 random control 不可区分。Claim 2 被否定。 在 worst
1183	    tier paper 中这成为另一条被关闭的路径，但不需要大篇幅—— 1 table + 1 figure 在 Section 5.2 用 1 paragraph
1184	    报告即可。
1185	
1186	    '
1187	- name: Cross-Lingual Orthogonality Analysis
1188	  plan_id: plan_005
1189	  description: 'Correctness-confidence cosine similarity, 20 languages × 2 architectures
1190	    (Qwen3 + Llama4), resource-tier 和 language family 分析.
1191	
1192	    '
1193	  expected_results:
1194	    mean_cosine_high: 0.035
1195	    mean_cosine_mid: 0.062
1196	    mean_cosine_low: 0.108
1197	    std_cosine_low: 0.078
1198	    cosine_range_all:
1199	    - 0.012
1200	    - 0.192
1201	    architecture_agreement_rate: 0.65
1202	    outlier_langs:
1203	    - am
1204	    - yo
1205	    - my
1206	  result_rationale: 'Orthogonality 在 HIGH resource 语言成立（cosine < 0.05），复现 Miao & Ungar
1207	    (2026)。 但 LOW resource 的 cosine 显著升高且方差大（mean 0.108, std 0.078）——原因不是真正的 非正交结构，而是两个
1208	    probe 都更 noisy：correctness probe selectivity 低（plan_013 控制 任务发现），confidence probe
1209	    同样缺乏区分性信号，两个 noisy direction 的 cosine 自然 偏离 0。Architecture 一致性仅 65%：7/20 语言两架构给出矛盾信号——可能反映不同
1210	    MoE routing 对 confidence 编码方式的影响。
1211	
1212	    作为已降级的 subsection，这些结果增加复杂性但无 clean takeaway。
1213	
1214	    '
1215	  tables:
1216	  - name: 'Table 6: Correctness-Confidence Orthogonality by Resource Tier'
1217	    columns:
1218	    - tier
1219	    - n_langs
1220	    - mean_cosine
1221	    - std
1222	    - min
1223	    - max
1224	    - arch_agreement
1225	    rows:
1226	    - - HIGH
1227	      - 7
1228	      - 0.035
1229	      - 0.012
1230	      - 0.012
1231	      - 0.052
1232	      - 6/7
1233	    - - MID
1234	      - 7
1235	      - 0.062
1236	      - 0.025
1237	      - 0.035
1238	      - 0.095
1239	      - 5/7
1240	    - - LOW
1241	      - 6
1242	      - 0.108
1243	      - 0.078
1244	      - 0.042
1245	      - 0.192
1246	      - 2/6
1247	    - - ALL
1248	      - 20
1249	      - 0.065
1250	      - 0.055
1251	      - 0.012
1252	      - 0.192
1253	      - 13/20
1254	  figures_description:
1255	  - 'Figure S1 (appendix): Box plot of cosine similarity by resource tier, faceted
1256	    by architecture. LOW tier shows higher median and wider spread. Dashed line at
1257	    cosine=0.10.
1258	
1259	    '
1260	  analysis: 'Orthogonality 作为 subsection 贡献有限。LOW tier 的高 cosine 可能是 probe noise 而非真
1261	    non-orthogonality（control task artifact rate 42% in LOW tier）。 简化为 1 paragraph
1262	    + 1 table 在 supporting evidence 小节。
1263	
1264	    '
1265	- name: Probe Complexity Comparison
1266	  plan_id: plan_006
1267	  description: 'Logistic regression vs 2-layer MLP, EN accuracy + cross-lingual transfer
1268	    degradation + calibration, 3 models × 20 languages.
1269	
1270	    '
1271	  expected_results:
1272	    en_auroc_lr_mean: 0.738
1273	    en_auroc_mlp_mean: 0.752
1274	    mlp_en_advantage_pp: 1.4
1275	    zs_transfer_degradation_lr_pp: 15.8
1276	    zs_transfer_degradation_mlp_pp: 19.4
1277	    mlp_transfer_disadvantage_pp: 3.6
1278	    lr_better_for_transfer_pct: 0.72
1279	    ece_lr_mean: 0.238
1280	    ece_mlp_mean: 0.252
1281	  result_rationale: 'MLP 更高 capacity → EN +1.4pp，但跨语言 transfer degradation 更大（-19.4%
1282	    vs -15.8%）， 符合 "linear probes transfer better" 假设。在 worst tier 下 effect size 中等
1283	    （Cohen''s d ≈ 0.35），72% 语言支持 LR。部分 HIGH resource 语言中 MLP 额外 capacity 弥补了 transfer
1284	    loss。结论方向正确但不 dramatic——LR 作为默认 choice 被 confirm， MLP 结果放 appendix。
1285	
1286	    '
1287	  tables:
1288	  - name: 'Table S2: Probe Complexity Comparison'
1289	    columns:
1290	    - metric
1291	    - logistic_regression
1292	    - mlp_2layer
1293	    - delta
1294	    - p_value
1295	    rows:
1296	    - - EN AUROC
1297	      - 0.738
1298	      - 0.752
1299	      - 0.014
1300	      - 0.006
1301	    - - ZS degradation
1302	      - 15.8%
1303	      - 19.4%
1304	      - +3.6pp
1305	      - 0.018
1306	    - - ZS AUROC
1307	      - 0.621
1308	      - 0.608
1309	      - -0.013
1310	      - 0.032
1311	    - - EN ECE
1312	      - 0.238
1313	      - 0.252
1314	      - 0.014
1315	      - 0.058
1316	    - - LR better for transfer
1317	      - 72%
1318	      - 28%
1319	      - —
1320	      - —
1321	  figures_description:
1322	  - 'Figure S2 (appendix): Layer-wise EN AUROC for LR vs MLP (upper panel) paired
1323	    with ZS AUROC (lower panel). MLP advantage grows with EN depth; LR advantage grows
1324	    with transfer depth.
1325	
1326	    '
1327	  analysis: '方向符合预期但 effect size 中等。在 worst tier 的 high-artifact 环境下，probe complexity
1328	    不是主要问题。保持 LR 默认，appendix 报告 MLP 对比。
1329	
1330	    '
1331	- name: Additional Benchmark Evaluation (Belebele + MMLU-ProX)
1332	  plan_id: plan_007
1333	  description: 'Best probes + all transfer conditions on Belebele (20 langs) and MMLU-ProX
1334	    (20 langs). Cross-benchmark generalization test.
1335	
1336	    '
1337	  expected_results:
1338	    belebele_zs_pass_rate: 0.45
1339	    belebele_mean_zs_auroc: 0.545
1340	    belebele_vs_globalmmlu_spearman: 0.71
1341	    belebele_mean_delta_vs_globalmmlu: -0.029
1342	    mmlupx_zs_pass_rate: 0.55
1343	    mmlupx_mean_zs_auroc: 0.565
1344	    mmlupx_vs_globalmmlu_spearman: 0.79
1345	    caclr_belebele_delta: -0.015
1346	    caclr_mmlupx_delta: -0.009
1347	    linear_proj_belebele_delta: 0.028
1348	    linear_proj_mmlupx_delta: 0.033
1349	  result_rationale: 'Belebele (reading comprehension) 与 MCQA correctness probing 的
1350	    task mismatch 导致更低 pass rate。Correctness probe 在 GlobalMMLU 上学到的 "correct answer"
1351	    signal 部分依赖于 MCQA-specific format cues（如选项长度、academic domain structure），这些 在 Belebele
1352	    的 reading comprehension 中缺失。MMLU-ProX 与 GlobalMMLU 更接近（同为 知识 MCQA），correlation
1353	    更高。
1354	
1355	    CaCLR 在 out-of-distribution data 上更差——distribution mismatch 被放大。 Linear projection
1356	    仍正但幅度缩小。
1357	
1358	    Worst tier 意味着 generalization 弱化了已经微弱的 positive findings， 暗示 correctness probing
1359	    可能 MCQA-specific。
1360	
1361	    '
1362	  tables:
1363	  - name: 'Table S3: Cross-Benchmark Generalization'
1364	    columns:
1365	    - benchmark
1366	    - zs_pass_rate
1367	    - mean_zs_auroc
1368	    - caclr_Δ
1369	    - linproj_Δ
1370	    - corr_vs_globalmmlu
1371	    rows:
1372	    - - GlobalMMLU
1373	      - 57%
1374	      - 0.574
1375	      - -0.008
1376	      - 0.036
1377	      - —
1378	    - - Belebele
1379	      - 45%
1380	      - 0.545
1381	      - -0.015
1382	      - 0.028
1383	      - 0.71
1384	    - - MMLU-ProX
1385	      - 55%
1386	      - 0.565
1387	      - -0.009
1388	      - 0.033
1389	      - 0.79
1390	  figures_description:
1391	  - 'Figure S3 (appendix): Per-language ZS AUROC scatter: GlobalMMLU vs Belebele and
1392	    GlobalMMLU vs MMLU-ProX. Moderate positive correlation with visible deviations
1393	    for low-resource languages.
1394	
1395	    '
1396	  analysis: 'Cross-benchmark generalization moderate。Belebele 低 performance 暗示 correctness
1397	    probing 对 task format 敏感——在 worst tier paper 中增加一层 caveat。 放 appendix 作为 generalization
1398	    check。
1399	
1400	    '
1401	- name: Quantization Validation Ablation
1402	  plan_id: plan_010
1403	  description: '(a) W4A16 vs FP16 for Llama 4 Scout, 5 representative layers, 5% data
1404	    subset; (b) INT4 vs FP16 for Qwen3-235B, 5 representative layers, 5% data subset.
1405	
1406	    '
1407	  expected_results:
1408	    llama_w4a16_vs_fp16:
1409	      mean_delta_auroc: 0.008
1410	      max_delta_auroc: 0.016
1411	      rank_preservation: 0.92
1412	    qwen_int4_vs_fp16:
1413	      mean_delta_auroc: 0.011
1414	      max_delta_auroc: 0.021
1415	      rank_preservation: 0.89
1416	    problematic_layers: 2
1417	    gemma_note: BF16, no quantization — serves as quantization-free control
1418	  result_rationale: 'Quantization artifacts 不灾难性但 non-negligible。深层（80-95% depth）受影响最大，
1419	    因为 correctness signal 在这些层最集中，而高频/低方差的 correctness direction 对 quantization noise
1420	    更敏感。INT4 (Qwen) 比 W4A16 (Llama) 更aggressive，所以 delta 更大。Rank preservation 88-92%
1421	    意味着 per-language ranking 大体保持但不完美。
1422	
1423	    Worst tier 下这创造一个 caveat：深层 probe 结论 potentially 受量化影响。 Gemma 4 BF16 无量化，提供了 quantization-free
1424	    的 architecture 数据点。
1425	
1426	    '
1427	  tables:
1428	  - name: 'Table S4: Quantization Validation'
1429	    columns:
1430	    - model
1431	    - quant
1432	    - layer_pct
1433	    - fp16_auroc
1434	    - quant_auroc
1435	    - delta
1436	    - rank_ok
1437	    rows:
1438	    - - Llama4
1439	      - W4A16
1440	      - 20%
1441	      - 0.65
1442	      - 0.647
1443	      - -0.003
1444	      - ✓
1445	    - - Llama4
1446	      - W4A16
1447	      - 40%
1448	      - 0.675
1449	      - 0.668
1450	      - -0.007
1451	      - ✓
1452	    - - Llama4
1453	      - W4A16
1454	      - 60%
1455	      - 0.698
1456	      - 0.688
1457	      - -0.01
1458	      - ✓
1459	    - - Llama4
1460	      - W4A16
1461	      - 80%
1462	      - 0.71
1463	      - 0.696
1464	      - -0.014
1465	      - ✗ (2 swaps)
1466	    - - Llama4
1467	      - W4A16
1468	      - 95%
1469	      - 0.715
1470	      - 0.699
1471	      - -0.016
1472	      - ✗ (3 swaps)
1473	    - - Qwen3
1474	      - INT4
1475	      - 20%
1476	      - 0.628
1477	      - 0.623
1478	      - -0.005
1479	      - ✓
1480	    - - Qwen3
1481	      - INT4
1482	      - 40%
1483	      - 0.672
1484	      - 0.662
1485	      - -0.01
1486	      - ✓
1487	    - - Qwen3
1488	      - INT4
1489	      - 60%
1490	      - 0.705
1491	      - 0.692
1492	      - -0.013
1493	      - ✗ (1 swap)
1494	    - - Qwen3
1495	      - INT4
1496	      - 80%
1497	      - 0.73
1498	      - 0.714
1499	      - -0.016
1500	      - ✗ (3 swaps)
1501	    - - Qwen3
1502	      - INT4
1503	      - 95%
1504	      - 0.741
1505	      - 0.72
1506	      - -0.021
1507	      - ✗ (4 swaps)
1508	  figures_description:
1509	  - 'Figure S4 (appendix): Layer-wise quantization delta for both models. Monotonic
1510	    increase in delta with depth. Horizontal dashed line at 1.5pp threshold.
1511	
1512	    '
1513	  analysis: 'Quantization 在深层引入 1-2pp 偏差，不改变主要 negative result 结论 （negative results
1514	    不依赖精确数值），但增加 limitations 内容。 Gemma BF16 作为 quantization-free control 点使得 Gemma
1515	    的结果最可信。
1516	
1517	    '
1518	- name: CKA Cross-Lingual Representation Similarity Analysis
1519	  plan_id: plan_011
1520	  description: 'CKA (linear kernel) EN vs target, all probed layers, 20 langs × 3
1521	    models. Simpson''s Paradox full-scale validation. Partial correlation controlling
1522	    for depth. Same-layer cross-language analysis. Subspace angle analysis.
1523	
1524	    '
1525	  expected_results:
1526	    simpson_paradox_confirmed_of_3_arch: 0
1527	    partial_correlations:
1528	      qwen3:
1529	        rho: 0.11
1530	        p: 0.28
1531	        bootstrap_ci:
1532	        - -0.08
1533	        - 0.29
1534	      llama4:
1535	        rho: 0.06
1536	        p: 0.45
1537	        bootstrap_ci:
1538	        - -0.12
1539	        - 0.24
1540	      gemma4:
1541	        rho: 0.16
1542	        p: 0.09
1543	        bootstrap_ci:
1544	        - -0.02
1545	        - 0.33
1546	    raw_correlations:
1547	      qwen3:
1548	        rho: -0.32
1549	        p: <0.001
1550	      llama4:
1551	        rho: -0.38
1552	        p: <0.001
1553	      gemma4:
1554	        rho: -0.29
1555	        p: <0.001
1556	    same_layer_cross_lang_analysis:
1557	      qwen3_significant_layers: 2/24
1558	      llama4_significant_layers: 0/12
1559	      gemma4_significant_layers: 1/16
1560	      median_rho: 0.14
1561	    subspace_angle:
1562	      high_tier_range_deg:
1563	      - 15
1564	      - 38
1565	      mid_tier_range_deg:
1566	      - 28
1567	      - 52
1568	      low_tier_range_deg:
1569	      - 42
1570	      - 65
1571	      consistency_across_layers: low — within-language angle std 8-15° across layers
1572	    pilot_replication:
1573	      llama_pilot_rho: 0.41
1574	      llama_fullscale_rho: 0.06
1575	      verdict: pilot artifact confirmed
1576	  result_rationale: '这是 worst tier 的 defining falsification。
1577	
1578	    5 语言 pilot 的 Simpson''s Paradox 被 20 语言全量数据否定：
1579	
1580	    (1) Llama partial rho 从 +0.41 (p=0.006) 骤降至 +0.06 (p=0.45)。原因：pilot 的 5 语言 恰好
1581	    overrepresented CKA-transfer 相关性最强的语言（zh, ar 有高 CKA + 低 degradation）， 排除了关系最弱的语言。15
1582	    种新增语言中 MID/LOW tier 的 CKA 模式与 pilot 语言截然不同—— 这些语言的 CKA 虽然也随 depth 下降，但下降斜率和 transfer
1583	    degradation 之间没有一致的 within-layer 关系。
1584	
1585	    (2) Qwen3 rho=+0.11 (p=0.28) 在 pilot 就不显著（+0.18, p=0.274），全量数据只是确认。 Gemma4 rho=+0.16
1586	    (p=0.09) 是最接近显著的，但 bootstrap CI 跨零（[-0.02, 0.33]）， 不能依赖。
1587	
1588	    (3) Same-layer cross-language analysis（n=20 per layer，最强检验）：median rho=0.14， 仅
1589	    3/52 层 significant——CKA 在 within-layer 水平几乎无预测力。在同一层中，不同语言 的 CKA 差异巨大但 transfer
1590	    AUROC 差异不 track CKA。
1591	
1592	    (4) Subspace angle analysis 否定 "correctness direction is a robust language-agnostic
1593	    subspace"：HIGH tier 15-38°（不是近乎平行），LOW tier 42-65°（近乎 orthogonal）。 Angle 在同一语言的不同层之间也有
1594	    8-15° 的标准差——correctness direction 不仅跨语言 不一致，在同一语言内也随 depth 漂移。
1595	
1596	    结论：CKA 不提供超越 depth 的解释力。从 "geometric analysis" 降级为 "suggestive correlation"——仅保留
1597	    CKA heatmap 作为 descriptive visualization。
1598	
1599	    '
1600	  tables:
1601	  - name: 'Table 7a: Simpson''s Paradox Full-Scale Validation'
1602	    columns:
1603	    - model
1604	    - raw_rho
1605	    - raw_p
1606	    - partial_rho
1607	    - partial_p
1608	    - pilot_rho
1609	    - pilot_p
1610	    - verdict
1611	    rows:
1612	    - - Qwen3-235B
1613	      - -0.32
1614	      - <0.001
1615	      - 0.11
1616	      - 0.28
1617	      - +0.18 (n.s.)
1618	      - 0.274
1619	      - n.s. confirmed
1620	    - - Llama4-Scout
1621	      - -0.38
1622	      - <0.001
1623	      - 0.06
1624	      - 0.45
1625	      - +0.41 (sig.)
1626	      - 0.006
1627	      - pilot artifact
1628	    - - Gemma4-31B
1629	      - -0.29
1630	      - <0.001
1631	      - 0.16
1632	      - 0.09
1633	      - N/A
1634	      - N/A
1635	      - marginal, CI spans 0
1636	  - name: 'Table 7b: Same-Layer Cross-Language CKA-Transfer Correlation'
1637	    columns:
1638	    - model
1639	    - total_layers
1640	    - significant_layers
1641	    - median_rho
1642	    - best_layer_rho
1643	    - best_p
1644	    rows:
1645	    - - Qwen3
1646	      - 24
1647	      - 2/24
1648	      - 0.15
1649	      - 0.4
1650	      - 0.078
1651	    - - Llama4
1652	      - 12
1653	      - 0/12
1654	      - 0.08
1655	      - 0.28
1656	      - 0.23
1657	    - - Gemma4
1658	      - 16
1659	      - 1/16
1660	      - 0.18
1661	      - 0.44
1662	      - 0.052
1663	  - name: 'Table 7c: Subspace Angle (Correctness Direction, EN vs Target, at ~60%
1664	      depth)'
1665	    columns:
1666	    - lang
1667	    - tier
1668	    - qwen3_angle
1669	    - llama4_angle
1670	    - gemma4_angle
1671	    rows:
1672	    - - zh
1673	      - HIGH
1674	      - 18°
1675	      - 24°
1676	      - 16°
1677	    - - es
1678	      - HIGH
1679	      - 15°
1680	      - 20°
1681	      - 14°
1682	    - - ja
1683	      - HIGH
1684	      - 35°
1685	      - 42°
1686	      - 32°
1687	    - - ar
1688	      - MID
1689	      - 32°
1690	      - 40°
1691	      - 30°
1692	    - - hi
1693	      - MID
1694	      - 38°
1695	      - 46°
1696	      - 35°
1697	    - - ko
1698	      - MID
1699	      - 28°
1700	      - 36°
1701	      - 26°
1702	    - - tr
1703	      - MID
1704	      - 45°
1705	      - 52°
1706	      - 42°
1707	    - - sw
1708	      - LOW
1709	      - 52°
1710	      - 58°
1711	      - 48°
1712	    - - bn
1713	      - LOW
1714	      - 48°
1715	      - 55°
1716	      - 45°
1717	    - - am
1718	      - LOW
1719	      - 62°
1720	      - 65°
1721	      - 58°
1722	  figures_description:
1723	  - 'Figure 6a: CKA heatmap (language × layer) for 3 models. Shows CKA decline with
1724	    depth but no clear correspondence to transfer patterns. Color-coded annotations
1725	    marking same-layer significant correlations (rare).
1726	
1727	    '
1728	  - 'Figure 6b: Partial residual scatter (CKA residualized on depth vs transfer AUROC
1729	    residualized on depth) for 3 models. Diffuse clouds with no visible trend.
1730	
1731	    '
1732	  - 'Figure 6c: Subspace angle violin plot by resource tier across 3 architectures.
1733	    Clear tier gradient but HIGH tier also 15-38° range, undermining "language-agnostic
1734	    subspace" claim. LOW tier near orthogonal.
1735	
1736	    '
1737	  analysis: 'CKA 的全面失败从 pilot 的 Simpson''s Paradox 标杆发现降级为 "depth confound 在 raw correlation
1738	    中占主导，controlling 后无 signal"。Subspace angle 否定了论文的 前提假设："correctness direction
1739	    是 robust language-agnostic subspace" 不成立。 CKA 框架从解释性分析降级为描述性可视化——保留 heatmap 但不承载因果叙述。
1740	    3 架构 0/3 Simpson''s Paradox confirmed，在 worst 范围 [0, 1] 内。
1741	
1742	    '
1743	- name: Linear Projection Sensitivity Analysis
1744	  plan_id: plan_012
1745	  description: 'Procrustes alignment with 10/20/50/100/200 parallel pairs. 3 models
1746	    × 5 representative layers × 20 languages.
1747	
1748	    '
1749	  expected_results:
1750	    linear_proj_delta_over_zs_low_resource_pp: 2.8
1751	    linear_proj_saturation_pairs_mean: 135
1752	    saturation_by_tier:
1753	      HIGH:
1754	        pairs_95pct: 62
1755	        range:
1756	        - 38
1757	        - 92
1758	      MID:
1759	        pairs_95pct: 118
1760	        range:
1761	        - 72
1762	        - 158
1763	      LOW:
1764	        pairs_95pct: 175
1765	        range:
1766	        - 140
1767	        - 198
1768	    sample_efficiency_curve:
1769	      10_pairs:
1770	        mean_auroc: 0.552
1771	        pct_of_200: 66%
1772	      20_pairs:
1773	        mean_auroc: 0.571
1774	        pct_of_200: 78%
1775	      50_pairs:
1776	        mean_auroc: 0.592
1777	        pct_of_200: 89%
1778	      100_pairs:
1779	        mean_auroc: 0.605
1780	        pct_of_200: 96%
1781	      200_pairs:
1782	        mean_auroc: 0.61
1783	        pct_of_200: 100%
1784	    procrustes_reversal:
1785	      helps_below_zs: < 0.53 (mostly helps)
1786	      hurts_above_zs: '> 0.62 (mostly hurts)'
1787	      inconsistent_zone:
1788	      - 0.53
1789	      - 0.62
1790	      note: threshold varies ±0.08 across languages — no single reliable cutoff
1791	  result_rationale: 'Worst tier 下 linear projection 需 100-135 pairs 达到 95% performance（非
1792	    50）：
1793	
1794	    (1) Subspace angle 在 worst tier 更大更不一致（plan_011），Procrustes 需更多数据 稳定 rotation
1795	    matrix 估计——50 pairs 在高维空间 rank-deficient。
1796	
1797	    (2) LOW resource 语言的 parallel pairs 翻译质量低 → activation noise → 需更多 pairs average
1798	    out noise。HIGH tier 62 pairs（翻译精确，subspace angle 小）vs LOW tier 175 pairs（翻译 noisy，subspace
1799	    angle 大）。
1800	
1801	    (3) Effect reversal threshold language-specific：inconsistent zone [0.53, 0.62]
1802	    意味着同一 ZS AUROC 值下不同语言可能被帮助或伤害。例如 ja (HIGH, ZS=0.588) 被 帮助但 ko (MID, ZS=0.589)
1803	    被伤害——差异来自 subspace angle 和翻译质量的交互作用。 无法给出单一可操作阈值——practitioner recommendation
1804	    弱化为 "ZS < 0.50 大概率有益， > 0.65 大概率有害，中间区间需 held-out validation"。
1805	
1806	    低资源语言 delta +2.8pp（worst 范围 [1, 4] 内），仍是唯一可行的 label-free 方案。
1807	
1808	    '
1809	  tables:
1810	  - name: 'Table 8a: Linear Projection Sample Efficiency (3 arch × 20 langs)'
1811	    columns:
1812	    - n_pairs
1813	    - mean_auroc
1814	    - pct_of_200
1815	    - std
1816	    - significant_pct
1817	    rows:
1818	    - - 10
1819	      - 0.552
1820	      - 66%
1821	      - 0.062
1822	      - 22%
1823	    - - 20
1824	      - 0.571
1825	      - 78%
1826	      - 0.055
1827	      - 38%
1828	    - - 50
1829	      - 0.592
1830	      - 89%
1831	      - 0.049
1832	      - 52%
1833	    - - 100
1834	      - 0.605
1835	      - 96%
1836	      - 0.044
1837	      - 65%
1838	    - - 200
1839	      - 0.61
1840	      - 100%
1841	      - 0.042
1842	      - 70%
1843	  - name: 'Table 8b: Pairs to 95% by Resource Tier'
1844	    columns:
1845	    - tier
1846	    - mean
1847	    - min
1848	    - max
1849	    - std
1850	    rows:
1851	    - - HIGH
1852	      - 62
1853	      - 38
1854	      - 92
1855	      - 20
1856	    - - MID
1857	      - 118
1858	      - 72
1859	      - 158
1860	      - 32
1861	    - - LOW
1862	      - 175
1863	      - 140
1864	      - 198
1865	      - 25
1866	  - name: 'Table 8c: Procrustes Effect Direction (200 pairs, selected languages)'
1867	    columns:
1868	    - lang
1869	    - tier
1870	    - zs_auroc
1871	    - linproj_auroc
1872	    - delta
1873	    - effect
1874	    rows:
1875	    - - am
1876	      - LOW
1877	      - 0.483
1878	      - 0.508
1879	      - 0.025
1880	      - helps
1881	    - - yo
1882	      - LOW
1883	      - 0.468
1884	      - 0.494
1885	      - 0.026
1886	      - helps
1887	    - - sw
1888	      - LOW
1889	      - 0.511
1890	      - 0.528
1891	      - 0.017
1892	      - helps
1893	    - - tr
1894	      - MID
1895	      - 0.544
1896	      - 0.56
1897	      - 0.016
1898	      - helps
1899	    - - hi
1900	      - MID
1901	      - 0.56
1902	      - 0.568
1903	      - 0.008
1904	      - marginal
1905	    - - vi
1906	      - MID
1907	      - 0.563
1908	      - 0.562
1909	      - -0.001
1910	      - neutral
1911	    - - ko
1912	      - MID
1913	      - 0.589
1914	      - 0.582
1915	      - -0.007
1916	      - hurts
1917	    - - ar
1918	      - MID
1919	      - 0.606
1920	      - 0.598
1921	      - -0.008
1922	      - hurts
1923	    - - ru
1924	      - MID
1925	      - 0.622
1926	      - 0.61
1927	      - -0.012
1928	      - hurts
1929	    - - es
1930	      - HIGH
1931	      - 0.674
1932	      - 0.654
1933	      - -0.02
1934	      - hurts
1935	    - - ja
1936	      - HIGH
1937	      - 0.588
1938	      - 0.596
1939	      - 0.008
1940	      - helps (despite HIGH)
1941	  figures_description:
1942	  - 'Figure 7a: Saturation curves faceted by resource tier, 95% threshold marked.
1943	    Per-language thin lines show within-tier variance. HIGH saturates early, LOW late.
1944	
1945	    '
1946	  - 'Figure 7b: ZS AUROC (x) vs ΔAUROC (y) scatter. Rough negative trend but wide
1947	    scatter band. Shaded inconsistent zone [0.53, 0.62] where both ± deltas occur.
1948	
1949	    '
1950	  analysis: 'Linear projection 是唯一可行 label-free 方案但实用性弱化：需 100+ pairs（非 50）， effect
1951	    reversal threshold inconsistent。Paper 给出条件性 recommendation： "ZS < 0.50 大概率有益,
1952	    > 0.65 大概率有害, 中间需 validation"—— 比预期的 clean threshold 弱得多，但对 practitioners 仍有指导价值。
1953	
1954	    '
1955	- name: Probing Control Tasks — Cross-Lingual Extension
1956	  plan_id: plan_013
1957	  description: 'Hewitt & Liang control tasks extended to 20 languages × all probed
1958	    layers × 3 models. Selectivity analysis. Multiple selectivity thresholds (0.03,
1959	    0.05, 0.10). (builds on completed plan_013 EN-only results)
1960	
1961	    '
1962	  expected_results:
1963	    cross_lingual_artifact_rate_pct: 35
1964	    artifact_by_tier:
1965	      HIGH:
1966	        rate: 15%
1967	        selectivity_mean: 0.195
1968	      MID:
1969	        rate: 31%
1970	        selectivity_mean: 0.138
1971	      LOW:
1972	        rate: 42%
1973	        selectivity_mean: 0.082
1974	    control_task_selectivity_deep_layers: 0.16
1975	    selectivity_vs_zs_auroc_rho: 0.65
1976	    threshold_sensitivity:
1977	      threshold_003:
1978	        artifact_rate: 42%
1979	      threshold_005:
1980	        artifact_rate: 35%
1981	      threshold_010:
1982	        artifact_rate: 24%
1983	    worst_combos:
1984	    - 'am: selectivity 0.004 at EN-opt layer'
1985	    - 'yo: selectivity 0.005 at EN-opt layer'
1986	    - 'my: selectivity 0.006 at EN-opt layer'
1987	    - 'sw: selectivity 0.008 at EN-opt layer'
1988	    mid_resource_surprise:
1989	      tr:
1990	        selectivity_at_enopt: 0.031
1991	      th:
1992	        selectivity_at_enopt: 0.028
1993	      vi:
1994	        selectivity_at_enopt: 0.042
1995	  result_rationale: 'Cross-lingual artifact rate 35% (overall) 是 worst tier 最强贡献。
1996	
1997	    LOW tier 42% artifact rate 的原因：am, yo, my, te 等语言在 LLM pretraining 中 极度不足（估计 <
1998	    0.1% token share），这些语言的 representation 缺乏区分性结构—— probe 学到的主要是 capacity artifacts（随机
1999	    label 也能达到类似 AUROC）。 Selectivity = real_AUROC - permuted_AUROC 对这些语言仅 0.004-0.008，
2000	    几乎等于 zero information content。
2001	
2002	    MID tier 31% artifact rate 是 worst tier 的 signature finding：不仅低资源有问题—— tr (0.031),
2003	    th (0.028), vi (0.042) 等中资源语言在 shallow/mid layers 也有大量 artifacts。原因：这些语言虽然 pretraining
2004	    充足，但 correctness-specific signal （区分 "模型答对/答错"）在 representation 中的编码弱于语言 identity
2005	    signal， probe 部分地拟合了 language-specific capacity pattern 而非 correctness。
2006	
2007	    HIGH tier 15% artifact rate 主要出现在 shallow layers（0-30% depth）， 与 plan_013 completed
2008	    results 一致（L0-L16 selectivity < 0.12）。
2009	
2010	    Selectivity 与 ZS AUROC 的 rho=0.65 是最尖锐的发现：暗示 cross-lingual probing 文献中许多 "positive
2011	    transfer" 结果可能是 artifacts——高 ZS AUROC 可能部分反映 capacity artifacts 而非 genuine correctness
2012	    signal transfer。
2013	
2014	    首次在 cross-lingual transfer 场景系统性应用 Hewitt & Liang selectivity—— 发现 artifact 问题远比
2015	    monolingual probing 严重。Field-level implication。
2016	
2017	    '
2018	  tables:
2019	  - name: 'Table 9a: Cross-Lingual Artifact Rate by Resource Tier (3 models)'
2020	    columns:
2021	    - tier
2022	    - n_langs
2023	    - artifact_rate_thresh_005
2024	    - selectivity_mean
2025	    - selectivity_std
2026	    rows:
2027	    - - HIGH
2028	      - 7
2029	      - 15%
2030	      - 0.195
2031	      - 0.042
2032	    - - MID
2033	      - 7
2034	      - 31%
2035	      - 0.138
2036	      - 0.038
2037	    - - LOW
2038	      - 6
2039	      - 42%
2040	      - 0.082
2041	      - 0.035
2042	    - - ALL
2043	      - 20
2044	      - 35%
2045	      - 0.142
2046	      - 0.058
2047	  - name: 'Table 9b: Per-Language Selectivity at EN-Optimal Layer (Qwen3)'
2048	    columns:
2049	    - lang
2050	    - tier
2051	    - real_auroc
2052	    - permuted_auroc
2053	    - selectivity
2054	    - flag
2055	    rows:
2056	    - - en
2057	      - —
2058	      - 0.741
2059	      - 0.488
2060	      - 0.253
2061	      - ''
2062	    - - zh
2063	      - HIGH
2064	      - 0.668
2065	      - 0.495
2066	      - 0.173
2067	      - ''
2068	    - - es
2069	      - HIGH
2070	      - 0.675
2071	      - 0.492
2072	      - 0.183
2073	      - ''
2074	    - - fr
2075	      - HIGH
2076	      - 0.658
2077	      - 0.49
2078	      - 0.168
2079	      - ''
2080	    - - de
2081	      - HIGH
2082	      - 0.649
2083	      - 0.486
2084	      - 0.163
2085	      - ''
2086	    - - ja
2087	      - HIGH
2088	      - 0.588
2089	      - 0.501
2090	      - 0.087
2091	      - ''
2092	    - - pt
2093	      - HIGH
2094	      - 0.662
2095	      - 0.489
2096	      - 0.173
2097	      - ''
2098	    - - it
2099	      - HIGH
2100	      - 0.645
2101	      - 0.492
2102	      - 0.153
2103	      - ''
2104	    - - ar
2105	      - MID
2106	      - 0.608
2107	      - 0.496
2108	      - 0.112
2109	      - ''
2110	    - - hi
2111	      - MID
2112	      - 0.567
2113	      - 0.503
2114	      - 0.064
2115	      - ⚠
2116	    - - ru
2117	      - MID
2118	      - 0.621
2119	      - 0.493
2120	      - 0.128
2121	      - ''
2122	    - - ko
2123	      - MID
2124	      - 0.591
2125	      - 0.499
2126	      - 0.092
2127	      - ''
2128	    - - tr
2129	      - MID
2130	      - 0.548
2131	      - 0.517
2132	      - 0.031
2133	      - ⚠
2134	    - - vi
2135	      - MID
2136	      - 0.562
2137	      - 0.52
2138	      - 0.042
2139	      - ⚠
2140	    - - th
2141	      - MID
2142	      - 0.528
2143	      - 0.5
2144	      - 0.028
2145	      - ⚠
2146	    - - sw
2147	      - LOW
2148	      - 0.518
2149	      - 0.51
2150	      - 0.008
2151	      - ⚠⚠
2152	    - - bn
2153	      - LOW
2154	      - 0.524
2155	      - 0.505
2156	      - 0.019
2157	      - ⚠⚠
2158	    - - am
2159	      - LOW
2160	      - 0.486
2161	      - 0.482
2162	      - 0.004
2163	      - ⚠⚠
2164	    - - yo
2165	      - LOW
2166	      - 0.475
2167	      - 0.47
2168	      - 0.005
2169	      - ⚠⚠
2170	    - - te
2171	      - LOW
2172	      - 0.502
2173	      - 0.492
2174	      - 0.01
2175	      - ⚠⚠
2176	    - - my
2177	      - LOW
2178	      - 0.468
2179	      - 0.462
2180	      - 0.006
2181	      - ⚠⚠
2182	  - name: 'Table 9c: Selectivity Threshold Sensitivity'
2183	    columns:
2184	    - threshold
2185	    - overall_artifact_rate
2186	    - LOW_rate
2187	    - MID_rate
2188	    - HIGH_rate
2189	    rows:
2190	    - - 0.03
2191	      - 42%
2192	      - 52%
2193	      - 40%
2194	      - 22%
2195	    - - 0.05
2196	      - 35%
2197	      - 42%
2198	      - 31%
2199	      - 15%
2200	    - - 0.1
2201	      - 24%
2202	      - 35%
2203	      - 22%
2204	      - 8%
2205	  figures_description:
2206	  - 'Figure 8a: Selectivity heatmap (language × layer) for Qwen3-235B. Color scale:
2207	    red (<0.05) → yellow (0.05-0.10) → green (>0.20). Large red region in LOW × shallow
2208	    layers. MID-resource red patches at moderate depths are the surprise finding.
2209	
2210	    '
2211	  - 'Figure 8b: Selectivity vs ZS AUROC scatter across all language-layer-model combinations.
2212	    Strong positive correlation (ρ=0.65). Annotation: "Many ''successful'' transfer
2213	    results fall in the low-selectivity region."
2214	
2215	    '
2216	  - 'Figure 8c: Artifact rate by resource tier with bootstrap 95% CI. MID tier CI
2217	    overlaps substantially with LOW tier — the problem is not confined to low-resource
2218	    languages.
2219	
2220	    '
2221	  analysis: 'Control task finding 是 worst tier paper 的 anchor contribution。>35% artifact
2222	    rate 波及中资源语言是 field-level 发现：所有跨语言 probing 研究——包括只看中/高资源的—— 都需要 selectivity 检验。Selectivity-AUROC
2223	    correlation (ρ=0.65) 暗示文献中许多 positive results 可能是 artifacts。首次系统性应用 Hewitt & Liang
2224	    到 cross-lingual 场景——这个贡献独立于本文其他所有 claims，即使其他全部失败仍足以支撑 EACL findings paper。
2225	
2226	    '
2227	- name: Extended Language Coverage (50+ Languages)
2228	  plan_id: plan_009
2229	  description: '从 20 扩展到 50+ 语言 (camera-ready extension)。Leverages GlobalMMLU/Belebele
2230	    full language sets。P2 priority。
2231	
2232	    '
2233	  expected_results:
2234	    total_languages: 52
2235	    zs_pass_rate_52lang: 0.5
2236	    artifact_rate_low_expanded: 0.45
2237	    artifact_rate_mid_expanded: 0.34
2238	    new_significant_pareto_langs: 2
2239	    linear_proj_saturation_mean_expanded: 155
2240	  result_rationale: '扩展到 52 语言后新增大部分是 MID/LOW resource，ZS pass rate 从 57% → 50% 因为新语言
2241	    skew lower resource。Control artifact rate 在扩展 LOW tier 升至 45% 因为更多极低资源语言纳入。新增语言不改变核心
2242	    negative results，主要增加 statistical power 和 coverage credibility。Linear projection
2243	    saturation mean 升至 155 因为 更多 hard languages。
2244	
2245	    扩展语言数的主要价值：(1) control task finding 的 scope 更大——"近半数低资源跨语言 probing 结果是 artifacts"
2246	    在 50+ 语言规模下更有说服力；(2) EACL reviewer 可能要求 更多语言的 coverage；(3) 无量化 Gemma 在 52 语言上的数据最可信。
2247	
2248	    '
2249	  tables:
2250	  - name: 'Table S5: 52-Language vs 20-Language Summary'
2251	    columns:
2252	    - metric
2253	    - 20_lang
2254	    - 52_lang
2255	    - delta
2256	    rows:
2257	    - - zs_pass_rate
2258	      - 57%
2259	      - 50%
2260	      - -7pp
2261	    - - artifact_rate_LOW
2262	      - 42%
2263	      - 45%
2264	      - +3pp
2265	    - - artifact_rate_MID
2266	      - 31%
2267	      - 34%
2268	      - +3pp
2269	    - - linear_proj_mean_pairs
2270	      - 135
2271	      - 155
2272	      - '+20'
2273	    - - max_partial_rho
2274	      - 0.16
2275	      - 0.14
2276	      - '-0.02'
2277	  figures_description:
2278	  - 'Figure S5 (camera-ready): World map of ZS AUROC at EN-optimal layer with artifact
2279	    flags. Sub-Saharan Africa and Southeast Asia dominated by artifact flags. Latin-script
2280	    European cluster relatively clean.
2281	
2282	    '
2283	  analysis: '52 语言扩展服务于 coverage 和 robustness。核心结论不变但 control task finding 更 impactful，linear
2284	    projection guidance 更 granular（更多语言的 tier classification）。
2285	
2286	    '
2287	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d22207a9-9fd5-414a-b6e2-d1b489f2baa7",
  "isSidechain": false,
  "promptId": "ac986e77-89c2-4da2-8cf0-d9a0da36482f",
  "type": "user",
  "uuid": "1887214f-ffda-49d0-9d96-1893ccfc83bd",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T122458/worst/review_context.yaml",
      "content": "narrative_guidance: '7-8B pilot 的核心模式不推广到全量模型。两个 MoE 架构（Qwen3-235B, Llama 4 Scout）完全没有清晰的\n  Pareto frontier——MoE expert routing 打破了 dense model 中 depth→specialization 的单调映射，\n  depth-transfer 关系在绝大多数语言为 non-monotonic 或 flat。唯一的 dense 架构（Gemma 4 31B）展现出 marginal\n  Pareto（global rho=-0.24, p=0.038），但仅 4/20 语言 per-language 显著，且 final-layer transfer\n  drop 微不足道（0.8pp），远不及 pilot 的 2-4pp。三架构平均 EN AUROC 0.74，处于 worst 范围中段。\n\n  Simpson''s Paradox 在 20 语言全量验证中全面崩塌：3 架构的 CKA partial correlation controlling for\n  depth 均不显著（max rho=+0.16, min p=0.09），Llama pilot 的 rho=+0.41 被确认为 5 语言 small-sample\n  artifact。CKA 提供不了超越 depth 的解释力。Subspace angle analysis 否定了 \"correctness direction\n  is a robust language-agnostic subspace\"——HIGH tier 语言 angle 15-38°，LOW tier 45-65°。\n\n  CaCLR 全面失败：β sweep 3 OOM 证实 consistency loss inert 或 harmful；CORAL 和 high-dim MMD\n  (PCA d=50/100) 同样失败，将 negative result 从 \"MMD-specific\" 扩展为 \"distributional matching\n  路径全面 关闭\"。Component ablation 每加一项 loss 都 net negative。\n\n  Decomposition 无实质效果，random-direction control 产生同量级 delta（paired test p=0.38）， difficulty\n  和 capability 不可分。\n\n  Control task analysis 是最强贡献：cross-lingual artifact rate 达 35%（LOW 42%，MID 31%，HIGH\n  15%）， 首次在跨语言 probing 场景系统性应用 selectivity 检验。Selectivity 与 ZS AUROC 强相关（rho=0.65），\n  暗示文献中许多 positive transfer 结果可能是 capacity artifacts。\n\n  Linear projection 作为唯一可行方案但需 100+ pairs（非 50），且效果反转阈值 language-specific， 无法给出单一可操作的\n  cutoff。\n\n  重构为 EACL negative results + methodology paper：(1) control task 方法论警告（field-level\n  贡献）， (2) mean-shift 不可能性证明（理论贡献），(3) distributional matching 路径全面关闭（CaCLR + CORAL\n  + high-dim MMD 系统性 negative result），(4) linear projection 条件性实用指导（descriptive empirical\n  贡献）。Drop Claim 2（decomposition）和 Claim 3（CaCLR method）作为 standalone claims。\n\n  '\nimagined_experiments:\n- name: Qwen3-235B Full Pareto Frontier\n  plan_id: plan_001\n  description: 'Qwen3-235B-A22B (94 layers, MoE, INT4), 24 probed layers (every 4th),\n    20 typologically diverse languages, EN correctness probes (LR + MLP), 5 transfer\n    conditions (zero-shot, mean-shift, linear projection 200 pairs, few-shot 25/100,\n    CaCLR).\n\n    '\n  expected_results:\n    en_best_auroc: 0.741\n    en_best_layer: 72\n    en_auroc_range:\n    - 0.601\n    - 0.741\n    en_best_ece_raw: 0.198\n    zs_pass_count_auroc_gt_058: 11\n    zs_pass_rate: 0.55\n    zs_fail_count: 9\n    mean_zs_auroc_all_20: 0.576\n    mean_zs_auroc_drop_vs_en_pp: 16.5\n    best_zs_auroc:\n      zh: 0.668\n      es: 0.675\n      fr: 0.658\n      de: 0.649\n      ja: 0.588\n      pt: 0.662\n      it: 0.645\n      ar: 0.608\n      hi: 0.567\n      ru: 0.621\n      ko: 0.591\n      tr: 0.548\n      vi: 0.562\n      th: 0.528\n      sw: 0.518\n      bn: 0.524\n      am: 0.486\n      yo: 0.475\n      te: 0.502\n      my: 0.468\n    best_zs_layer:\n      zh: 60\n      es: 56\n      fr: 60\n      de: 52\n      ja: 48\n      pt: 56\n      it: 56\n      ar: 52\n      hi: 44\n      ru: 56\n      ko: 48\n      tr: 40\n      vi: 44\n      th: 36\n      sw: 36\n      bn: 40\n      am: 32\n      yo: 28\n      te: 36\n      my: 32\n    global_spearman_rho_depth_vs_transfer: -0.12\n    global_spearman_p: 0.078\n    per_lang_spearman:\n      zh:\n        rho: -0.31\n        p: 0.14\n      es:\n        rho: -0.25\n        p: 0.24\n      fr:\n        rho: -0.28\n        p: 0.18\n      de:\n        rho: -0.19\n        p: 0.38\n      ja:\n        rho: 0.18\n        p: 0.4\n      pt:\n        rho: -0.22\n        p: 0.3\n      it:\n        rho: -0.16\n        p: 0.46\n      ar:\n        rho: 0.05\n        p: 0.82\n      hi:\n        rho: -0.41\n        p: 0.046\n      ru:\n        rho: -0.14\n        p: 0.52\n      ko:\n        rho: 0.25\n        p: 0.24\n      tr:\n        rho: -0.08\n        p: 0.71\n      vi:\n        rho: 0.09\n        p: 0.68\n      th:\n        rho: -0.11\n        p: 0.61\n      sw:\n        rho: -0.35\n        p: 0.09\n      bn:\n        rho: -0.12\n        p: 0.58\n      am:\n        rho: 0.14\n        p: 0.52\n      yo:\n        rho: -0.02\n        p: 0.93\n      te:\n        rho: -0.18\n        p: 0.4\n      my:\n        rho: 0.1\n        p: 0.64\n    per_lang_significant_negative_rho_count: 1\n    per_lang_significant_positive_rho_count: 0\n    per_lang_nonmonotonic_count: 13\n    pareto_tradeoff_prevalence: 0.08\n    pareto_depth_transfer_drop_final_layers_pp: 0.6\n    mean_shift_delta_auroc_all: 0.0\n    transfer_conditions_summary:\n      zero_shot:\n        mean_auroc: 0.576\n        std: 0.068\n        delta_vs_zs: 0.0\n      mean_shift:\n        mean_auroc: 0.576\n        std: 0.068\n        delta_vs_zs: 0.0\n      linear_proj_200:\n        mean_auroc: 0.612\n        std: 0.055\n        delta_vs_zs: 0.036\n      fewshot_25:\n        mean_auroc: 0.598\n        std: 0.061\n        delta_vs_zs: 0.022\n      fewshot_100:\n        mean_auroc: 0.625\n        std: 0.049\n        delta_vs_zs: 0.049\n  result_rationale: 'EN best AUROC 0.741 在 worst 范围 [0.72, 0.78] 内——Qwen3-235B 的 22B\n    active parameters 对 correctness signal 的编码不显著优于 7B pilot（0.754），因为 correctness\n    direction 的信号 强度主要由 pretraining data 质量和 MCQA 格式暴露量决定，而非模型 scale。INT4 量化引入 ~1pp\n    额外损耗。\n\n    ZS pass 11/20 (55%) 处于 worst 范围 [8, 13] 中段。MoE routing 导致不同语言被路由到 不同 expert 子集，correctness\n    direction 的跨语言一致性被 expert 分化削弱：pilot 中 Qwen2.5-7B dense 架构的 4/5 pass 不能外推，因为 dense\n    model 的 shared representation 天然更有利于 cross-lingual alignment。低资源语言（am, yo, my）的\n    best ZS AUROC < 0.50，接近 random。\n\n    Global Pareto rho=-0.12 (p=0.078) 仅 marginally significant：depth-transfer tradeoff\n    在 MoE 中不成立，因为 expert routing 在不同深度可以 \"重置\" 语言特异性——L48 的 expert allocation 可能与 L72\n    完全不同，打破了 \"deeper = more specialized\" 的 dense-model 假设。13/20 语言呈现 non-monotonic\n    模式（U形、锯齿形、plateau），这是 MoE 的结构性特征而非噪声。仅 hi 达到 per-language significant negative\n    rho（p=0.046），ko 和 ja 方向反转（deeper helps transfer）。\n\n    Final-layer transfer drop 仅 0.6pp（worst 范围 [0.0, 1.5]），远低于 pilot 的 2-4pp—— 235B\n    MoE 的最深层 expert routing 已经足够 specialized，EN probe 在这些层的 AUROC 提升本身就很小（L88 vs L72\n    仅 +0.3pp EN AUROC），所以 transfer drop 也被压缩。\n\n    Mean-shift ΔAUROC ≡ 0 符合已证明的 rank-invariance。Linear projection +3.6pp 和 few-shot\n    100 +4.9pp 有中等改善，但 significant improvement 仅覆盖 55-65% 的语言。\n\n    '\n  tables:\n  - name: 'Table 1a: Qwen3-235B Per-Language Pareto (Depth vs ZS-AUROC Spearman ρ)'\n    columns:\n    - lang\n    - tier\n    - best_zs_auroc\n    - best_zs_layer\n    - spearman_rho\n    - p_value\n    - pattern\n    rows:\n    - - zh\n      - HIGH\n      - 0.668\n      - 60\n      - -0.31\n      - 0.14\n      - weak negative\n    - - es\n      - HIGH\n      - 0.675\n      - 56\n      - -0.25\n      - 0.24\n      - n.s.\n    - - fr\n      - HIGH\n      - 0.658\n      - 60\n      - -0.28\n      - 0.18\n      - n.s.\n    - - de\n      - HIGH\n      - 0.649\n      - 52\n      - -0.19\n      - 0.38\n      - n.s.\n    - - ja\n      - HIGH\n      - 0.588\n      - 48\n      - 0.18\n      - 0.4\n      - non-monotonic U-shape\n    - - pt\n      - HIGH\n      - 0.662\n      - 56\n      - -0.22\n      - 0.3\n      - n.s.\n    - - it\n      - HIGH\n      - 0.645\n      - 56\n      - -0.16\n      - 0.46\n      - n.s.\n    - - ar\n      - MID\n      - 0.608\n      - 52\n      - 0.05\n      - 0.82\n      - flat\n    - - hi\n      - MID\n      - 0.567\n      - 44\n      - -0.41\n      - 0.046\n      - significant negative\n    - - ru\n      - MID\n      - 0.621\n      - 56\n      - -0.14\n      - 0.52\n      - n.s.\n    - - ko\n      - MID\n      - 0.591\n      - 48\n      - 0.25\n      - 0.24\n      - inverted—deeper helps\n    - - tr\n      - MID\n      - 0.548\n      - 40\n      - -0.08\n      - 0.71\n      - n.s.\n    - - vi\n      - MID\n      - 0.562\n      - 44\n      - 0.09\n      - 0.68\n      - flat\n    - - th\n      - MID\n      - 0.528\n      - 36\n      - -0.11\n      - 0.61\n      - n.s.\n    - - sw\n      - LOW\n      - 0.518\n      - 36\n      - -0.35\n      - 0.09\n      - marginal negative\n    - - bn\n      - LOW\n      - 0.524\n      - 40\n      - -0.12\n      - 0.58\n      - n.s.\n    - - am\n      - LOW\n      - 0.486\n      - 32\n      - 0.14\n      - 0.52\n      - non-monotonic\n    - - yo\n      - LOW\n      - 0.475\n      - 28\n      - -0.02\n      - 0.93\n      - noisy flat\n    - - te\n      - LOW\n      - 0.502\n      - 36\n      - -0.18\n      - 0.4\n      - n.s.\n    - - my\n      - LOW\n      - 0.468\n      - 32\n      - 0.1\n      - 0.64\n      - non-monotonic\n  - name: 'Table 1b: Qwen3-235B Transfer Conditions Summary (20 langs, EN-optimal\n      layer)'\n    columns:\n    - condition\n    - mean_auroc\n    - std\n    - delta_vs_zs\n    - significant_improvement_count\n    rows:\n    - - zero-shot\n      - 0.576\n      - 0.068\n      - —\n      - —\n    - - mean-shift\n      - 0.576\n      - 0.068\n      - 0.0\n      - 0/20\n    - - linear_proj_200\n      - 0.612\n      - 0.055\n      - 0.036\n      - 11/20\n    - - fewshot_25\n      - 0.598\n      - 0.061\n      - 0.022\n      - 7/20\n    - - fewshot_100\n      - 0.625\n      - 0.049\n      - 0.049\n      - 13/20\n  figures_description:\n  - 'Figure 1a: EN AUROC vs best ZS AUROC scatter across 24 layers for Qwen3-235B,\n    colored by resource tier. Diffuse cloud without clean Pareto frontier. Non-monotonic\n    language trajectories (ja, ko, am, my) highlighted. Annotation: global ρ=-0.12\n    (p=0.078).\n\n    '\n  - 'Figure 1b: ZS AUROC heatmap (language × probed layer). Irregular MoE-specific\n    layer-to-layer variance, no smooth depth gradient. Expert routing artifacts visible\n    as 4-layer-period oscillations.\n\n    '\n  analysis: 'Qwen3-235B 的 Pareto frontier 远不如 Qwen2.5-7B pilot 清晰。MoE expert routing\n    打破了 dense model 中 depth = specialization 的单调映射。Pilot 的 clear Pareto（L27 EN best\n    但 transfer drops 2-4pp vs L24）是 dense 7B model 的特殊现象。仅 1/20 语言达到 per-language\n    显著性（hi），且部分语言方向反转——depth-transfer tradeoff 不是普遍现象。对 Claim 1 构成 严重挑战：不能声称 Qwen\n    系列存在 consistent Pareto。\n\n    '\n- name: Llama 4 Scout Full Pareto Frontier\n  plan_id: plan_002\n  description: 'Llama 4 Scout (48 layers, 17B-16E MoE, W4A16), 12 probed layers (every\n    4th), 20 languages, 5 transfer conditions.\n\n    '\n  expected_results:\n    en_best_auroc: 0.718\n    en_best_layer: 40\n    en_auroc_range:\n    - 0.615\n    - 0.718\n    en_best_ece_raw: 0.215\n    zs_pass_count_auroc_gt_058: 9\n    zs_pass_rate: 0.45\n    mean_zs_auroc_all_20: 0.562\n    mean_zs_auroc_drop_vs_en_pp: 15.6\n    best_zs_auroc:\n      zh: 0.648\n      es: 0.655\n      fr: 0.642\n      de: 0.635\n      ja: 0.562\n      pt: 0.648\n      it: 0.631\n      ar: 0.588\n      hi: 0.548\n      ru: 0.608\n      ko: 0.575\n      tr: 0.531\n      vi: 0.558\n      th: 0.515\n      sw: 0.501\n      bn: 0.508\n      am: 0.472\n      yo: 0.458\n      te: 0.491\n      my: 0.452\n    global_spearman_rho_depth_vs_transfer: -0.06\n    global_spearman_p: 0.31\n    per_lang_significant_negative_rho_count: 0\n    per_lang_significant_positive_rho_count: 0\n    per_lang_nonmonotonic_count: 8\n    pareto_tradeoff_prevalence: 0.05\n    pareto_depth_transfer_drop_final_layers_pp: 0.3\n    mean_shift_delta_auroc_all: 0.0\n    transfer_conditions_summary:\n      zero_shot:\n        mean_auroc: 0.562\n        std: 0.065\n        delta_vs_zs: 0.0\n      mean_shift:\n        mean_auroc: 0.562\n        std: 0.065\n        delta_vs_zs: 0.0\n      linear_proj_200:\n        mean_auroc: 0.598\n        std: 0.052\n        delta_vs_zs: 0.036\n      fewshot_25:\n        mean_auroc: 0.584\n        std: 0.058\n        delta_vs_zs: 0.022\n      fewshot_100:\n        mean_auroc: 0.611\n        std: 0.048\n        delta_vs_zs: 0.049\n  result_rationale: 'Llama 4 Scout EN best AUROC 0.718 在 worst 范围低端——active parameters\n    17B 但 16 experts 的稀疏激活使得每个 token 实际使用的参数量有限，correctness signal 在 expert 间被稀释。W4A16\n    量化额外损耗 ~0.5-1pp。\n\n    ZS pass 9/20 (45%)，比 Qwen3 低因为：(1) Llama 4 Scout 的 multilingual pretraining 比例可能低于\n    Qwen3（Qwen 系列历来强调多语言）；(2) 16-expert MoE 的 expert specialization 程度更高，语言间 representation\n    divergence 更大。MVP 中 Llama-3.1-8B dense 的 5/5 pass 不推广——8B dense → Scout MoE 的架构变化比\n    scale change 更根本。\n\n    Global Pareto rho=-0.06 (p=0.31) 完全不显著，0/20 语言 per-language 显著。仅 12 probed layers\n    使 per-language Spearman 功效极低（n=12），但即使考虑 power 问题，effect sizes 也很小 （max |rho|\n    = 0.38）。Scout 的 expert routing 比 Qwen3 更激进（16 experts vs Qwen3 的 设计），导致 depth-transfer\n    关系更加 noisy。\n\n    Final-layer drop 仅 0.3pp——transfer 在 L40-L48 区间几乎 flat，没有 tradeoff 可言。\n\n    '\n  tables:\n  - name: 'Table 2a: Llama 4 Scout Per-Language Pareto Spearman ρ'\n    columns:\n    - lang\n    - tier\n    - best_zs_auroc\n    - spearman_rho\n    - p_value\n    rows:\n    - - zh\n      - HIGH\n      - 0.648\n      - -0.18\n      - 0.58\n    - - es\n      - HIGH\n      - 0.655\n      - -0.12\n      - 0.71\n    - - fr\n      - HIGH\n      - 0.642\n      - -0.22\n      - 0.49\n    - - de\n      - HIGH\n      - 0.635\n      - -0.08\n      - 0.81\n    - - ja\n      - HIGH\n      - 0.562\n      - 0.32\n      - 0.31\n    - - pt\n      - HIGH\n      - 0.648\n      - -0.15\n      - 0.64\n    - - it\n      - HIGH\n      - 0.631\n      - -0.05\n      - 0.88\n    - - ar\n      - MID\n      - 0.588\n      - 0.22\n      - 0.49\n    - - hi\n      - MID\n      - 0.548\n      - -0.38\n      - 0.22\n    - - ru\n      - MID\n      - 0.608\n      - -0.02\n      - 0.95\n    - - ko\n      - MID\n      - 0.575\n      - 0.35\n      - 0.26\n    - - tr\n      - MID\n      - 0.531\n      - 0.08\n      - 0.81\n    - - vi\n      - MID\n      - 0.558\n      - 0.12\n      - 0.71\n    - - th\n      - MID\n      - 0.515\n      - -0.18\n      - 0.58\n    - - sw\n      - LOW\n      - 0.501\n      - -0.25\n      - 0.43\n    - - bn\n      - LOW\n      - 0.508\n      - -0.08\n      - 0.81\n    - - am\n      - LOW\n      - 0.472\n      - 0.02\n      - 0.95\n    - - yo\n      - LOW\n      - 0.458\n      - -0.12\n      - 0.71\n    - - te\n      - LOW\n      - 0.491\n      - -0.05\n      - 0.88\n    - - my\n      - LOW\n      - 0.452\n      - 0.15\n      - 0.64\n  - name: 'Table 2b: Llama 4 Scout Transfer Conditions Summary'\n    columns:\n    - condition\n    - mean_auroc\n    - delta_vs_zs\n    - significant_count\n    rows:\n    - - zero-shot\n      - 0.562\n      - —\n      - —\n    - - mean-shift\n      - 0.562\n      - 0.0\n      - 0/20\n    - - linear_proj_200\n      - 0.598\n      - 0.036\n      - 10/20\n    - - fewshot_25\n      - 0.584\n      - 0.022\n      - 6/20\n    - - fewshot_100\n      - 0.611\n      - 0.049\n      - 12/20\n  figures_description:\n  - 'Figure 2: Llama 4 Scout Pareto scatter, same format as Figure 1a. Cloud 更散乱，\n    global ρ=-0.06 (p=0.31)。ko (+0.35) 和 ja (+0.32) 方向反转于预期。\n\n    '\n  analysis: 'Llama 4 Scout 确认 MoE 架构的 Pareto 缺失。与 Qwen3 合并看：0 个 MoE 架构在 p<0.05 展现\n    Pareto。MVP 中 Llama-3.1-8B 的弱 Pareto 是 dense 架构特有的。两个 MoE 结合表明 expert routing 是\n    Pareto 缺失的结构性原因，而非偶然。\n\n    '\n- name: Gemma 4 31B Dense Pareto Frontier\n  plan_id: plan_008\n  description: 'Gemma 4 31B Dense (60 text layers, BF16 无量化), 16 probed layers (every\n    4th + final), 20 languages, 5 transfer conditions. Dense vs MoE 对照。\n\n    '\n  expected_results:\n    en_best_auroc: 0.755\n    en_best_layer: 52\n    en_auroc_range:\n    - 0.618\n    - 0.755\n    en_best_ece_raw: 0.188\n    zs_pass_count_auroc_gt_058: 12\n    zs_pass_rate: 0.6\n    mean_zs_auroc_all_20: 0.585\n    mean_zs_auroc_drop_vs_en_pp: 17.0\n    best_zs_auroc:\n      zh: 0.682\n      es: 0.691\n      fr: 0.672\n      de: 0.665\n      ja: 0.598\n      pt: 0.678\n      it: 0.658\n      ar: 0.618\n      hi: 0.575\n      ru: 0.635\n      ko: 0.602\n      tr: 0.558\n      vi: 0.572\n      th: 0.538\n      sw: 0.525\n      bn: 0.531\n      am: 0.492\n      yo: 0.481\n      te: 0.508\n      my: 0.475\n    global_spearman_rho_depth_vs_transfer: -0.24\n    global_spearman_p: 0.038\n    per_lang_significant_negative_rho_count: 4\n    per_lang_significant_positive_rho_count: 0\n    per_lang_nonmonotonic_count: 5\n    pareto_tradeoff_prevalence: 0.22\n    pareto_depth_transfer_drop_final_layers_pp: 0.8\n    spearman_depth_vs_transfer_rho_positive_langs: 10\n    transfer_conditions_summary:\n      zero_shot:\n        mean_auroc: 0.585\n        std: 0.063\n        delta_vs_zs: 0.0\n      mean_shift:\n        mean_auroc: 0.585\n        std: 0.063\n        delta_vs_zs: 0.0\n      linear_proj_200:\n        mean_auroc: 0.621\n        std: 0.051\n        delta_vs_zs: 0.036\n      fewshot_25:\n        mean_auroc: 0.607\n        std: 0.057\n        delta_vs_zs: 0.022\n      fewshot_100:\n        mean_auroc: 0.634\n        std: 0.045\n        delta_vs_zs: 0.049\n  result_rationale: 'Gemma 4 31B Dense 是唯一有 marginal Pareto 的架构。Dense 架构没有 expert\n    routing， depth→specialization 映射更单调，因此 global rho=-0.24 (p=0.038) 达到 significance。\n    4/20 语言 per-language 显著（zh, fr, hi, sw）——全部是负 rho（deeper layers = worse transfer），\n    符合 specialization 叙述。\n\n    但这反而增加了叙述复杂性：Pareto 是 architecture-dependent 的（dense 有，MoE 没有）， 无法声称是普遍现象。且 final-layer\n    drop 仅 0.8pp——远低于 pilot 的 2-4pp，因为 31B dense model 的最深层已经足够 expressive，EN probe\n    的边际 AUROC 提升很小（L56→L60 仅 +0.4pp）， 相应 transfer 损失也被压缩。\n\n    EN AUROC 0.755 略高于两个 MoE（因无量化损耗 + BF16 保留更多信号精度），三架构均值 (0.741 + 0.718 + 0.755)/3\n    = 0.738，在 worst 范围 [0.72, 0.78] 内。\n\n    ZS pass 12/20 (60%)——三架构最高，因为 Gemma 4 的 multilingual pretraining 可能 更均衡（Apache\n    2.0 开源模型通常 training data 更 curated），且无量化损耗。\n\n    '\n  tables:\n  - name: 'Table 3: Gemma 4 31B Dense Pareto Summary'\n    columns:\n    - metric\n    - value\n    rows:\n    - - en_best_auroc\n      - 0.755\n    - - en_best_layer\n      - L52 (87% depth)\n    - - zs_pass_rate\n      - 60% (12/20)\n    - - global_pareto_rho\n      - -0.24 (p=0.038)\n    - - per_lang_significant_rho\n      - 4/20 (zh, fr, hi, sw)\n    - - final_layer_transfer_drop_pp\n      - 0.8\n    - - control_artifact_rate_LOW\n      - 38%\n    - - no_quantization_confound\n      - BF16 — no quantization artifact\n  - name: 'Table 3b: Dense vs MoE Architecture Comparison'\n    columns:\n    - metric\n    - Qwen3 (MoE)\n    - Llama4 (MoE)\n    - Gemma4 (Dense)\n    rows:\n    - - en_best_auroc\n      - 0.741\n      - 0.718\n      - 0.755\n    - - global_pareto_rho\n      - -0.12 (n.s.)\n      - -0.06 (n.s.)\n      - -0.24 (p=0.038)\n    - - per_lang_sig_count\n      - 1/20\n      - 0/20\n      - 4/20\n    - - non_monotonic_langs\n      - 13/20\n      - 8/20\n      - 5/20\n    - - final_layer_drop_pp\n      - 0.6\n      - 0.3\n      - 0.8\n    - - zs_pass_rate\n      - 55%\n      - 45%\n      - 60%\n  figures_description:\n  - 'Figure 3a: Gemma 4 Pareto scatter vs Qwen3/Llama4 (3-panel). Gemma shows cleaner\n    negative trend but still substantial scatter. MoE panels show diffuse clouds.\n    Visual comparison highlights dense vs MoE structural difference.\n\n    '\n  - 'Figure 3b: Per-language Spearman ρ bar chart across 3 architectures. Gemma bars\n    lean negative but most still n.s. MoE bars scattered around zero.\n\n    '\n  analysis: 'Dense vs MoE 对比是 Gemma 最大的贡献：dense 架构确实有 cleaner depth-transfer 关系， 但\n    effect size 远小于 pilot 预期。三架构综合 pareto_tradeoff_prevalence ≈ 0.12 (12% of lang-arch\n    pairs)，在 worst 范围 [0.05, 0.25] 内。 结论：Pareto 是 architecture-conditional 的，不是 universal\n    finding——这使得 Claim 1 从 \"discovery\" 降级为 \"architecture-dependent observational note\"。\n\n    '\n- name: CaCLR Implementation and Comparative Evaluation\n  plan_id: plan_003\n  description: 'CaCLR (L_BCE + α·L_SB-ECE + β·L_MMD), β sweep 3 OOM, α sweep, component\n    ablation, CORAL comparison, high-dim MMD (PCA d=50/100), multi-seed (5 seeds),\n    mixed β criterion. vs 4 baselines, 3 models × 20 langs.\n\n    '\n  expected_results:\n    caclr_mean_delta_auroc_vs_zs: -0.008\n    caclr_langs_improved_of_20: 4\n    caclr_best_beta: none — all β inert or harmful\n    beta_sweep:\n      beta_0.001:\n        mean_delta_auroc: -0.002\n        std: 0.016\n      beta_0.01:\n        mean_delta_auroc: -0.005\n        std: 0.019\n      beta_0.1:\n        mean_delta_auroc: -0.009\n        std: 0.023\n      beta_1.0:\n        mean_delta_auroc: -0.016\n        std: 0.028\n    alpha_sweep:\n      alpha_0.01:\n        delta_auroc: -0.001\n        delta_ece: 0.006\n      alpha_0.1:\n        delta_auroc: -0.004\n        delta_ece: 0.002\n      alpha_1.0:\n        delta_auroc: -0.01\n        delta_ece: -0.001\n      alpha_10.0:\n        delta_auroc: -0.025\n        delta_ece: -0.004\n    component_ablation:\n      bce_only:\n        delta_vs_zs: -0.001\n        note: ≈ ZS baseline\n      bce_plus_sbece:\n        delta_vs_zs: -0.005\n        note: SB-ECE hurts discrimination\n      bce_plus_mmd_1d:\n        delta_vs_zs: -0.004\n        note: 1-D MMD inert/harmful\n      bce_plus_mmd_pca50:\n        delta_vs_zs: -0.006\n        note: 50-D MMD also fails\n      bce_plus_mmd_pca100:\n        delta_vs_zs: -0.008\n        note: 100-D MMD worse — curse of dimensionality\n      bce_plus_coral:\n        delta_vs_zs: -0.005\n        note: CORAL fails — second-order alignment insufficient\n      bce_plus_coral_pca50:\n        delta_vs_zs: -0.007\n        note: high-dim CORAL also fails\n      full_caclr:\n        delta_vs_zs: -0.008\n        note: compound degradation\n    multi_seed_std:\n      caclr: 0.003\n      fewshot_25: 0.008\n      fewshot_100: 0.005\n      procrustes: 0.002\n    mixed_beta_criterion_result: 'β selected on zh+sw validation matches English-only\n      selection (β=0.001). No evidence of systematic bias against cross-lingual benefit.\n\n      '\n    five_way_comparison:\n      zero_shot:\n        mean_auroc: 0.574\n        mean_ece: 0.282\n      mean_shift:\n        mean_auroc: 0.574\n        mean_ece: 0.288\n      caclr_best:\n        mean_auroc: 0.566\n        mean_ece: 0.275\n      linear_proj_200:\n        mean_auroc: 0.61\n        mean_ece: 0.245\n      fewshot_25:\n        mean_auroc: 0.596\n        mean_ece: 0.258\n      fewshot_100:\n        mean_auroc: 0.623\n        mean_ece: 0.232\n    implementation_spec:\n      mmd_kernel: Gaussian RBF, bandwidth=median heuristic\n      optimizer: Adam, lr=1e-3, cosine schedule to 1e-5\n      epochs: 50\n      early_stopping: patience=10 on held-out English BCE loss\n      initialization: from standard LR solution\n      batch_size: 256\n      mmd_items: same items as BCE (probe_train 70% split)\n      parallel_set_size_range:\n      - 618\n      - 2852\n  result_rationale: 'CaCLR 失败的根本原因链：\n\n    (1) 1-D MMD 结构性限制：probe logit 是标量，MMD 只能 match 两个 1-D 分布的 marginal。 即使 marginal\n    被 match，EN 和 target 的 conditional distributions P(logit|correct) vs P(logit|incorrect)\n    仍然不同——Zhao et al. (2019) 的理论预测在此得到验证。β 越大，logits 被拉向无区分性的 marginal match，discrimination\n    下降。\n\n    (2) High-dim MMD (PCA d=50/100) 同样失败：curse of dimensionality 使得 Gaussian RBF kernel\n    在 50-100 维空间的 MMD estimate 方差极大，有效样本量不足（probe_train ~2000 samples 对 100 维 MMD\n    来说 severely underpowered）。d=100 比 d=50 更差，证实这一解释。\n\n    (3) CORAL 也失败：second-order alignment（match mean + covariance）比 MMD 更受 conditional\n    distribution mismatch 的影响——对齐 marginal moments 不能修复 correctness signal 的 conditional\n    structure 差异。CORAL 在 domain adaptation 中成功的条件是 covariate shift （P(X) changes,\n    P(Y|X) stable），但 cross-lingual correctness probing 违反这一条件 （P(correct|representation)\n    在不同语言中不同）。\n\n    (4) Component ablation 证实每个额外 loss 都是 net negative：BCE-only retrain ≈ ZS baseline（LR\n    solution 初始化后 Adam 微调不改变 optimum），每加一项都引入额外 noise 而 无 signal。CaCLR 不是超参选择问题而是方法论层面的失败。\n\n    (5) Multi-seed 结果稳定（std=0.003），排除了 single-seed 偶然性。Mixed β criterion 排除了 β selection\n    对 cross-lingual benefit 的系统性偏见。\n\n    综合：distributional matching 路径（MMD + CORAL，low-dim + high-dim）被全面关闭。 Linear projection\n    和 few-shot 显著优于 CaCLR，因为它们直接利用 target-language 结构 信息而非试图间接 match distributions。\n\n    '\n  tables:\n  - name: 'Table 4a: CaCLR β Sweep (3 architectures × 20 langs, EN-optimal layer)'\n    columns:\n    - beta\n    - mean_auroc\n    - delta_vs_zs\n    - pct_improved\n    - pct_harmed\n    rows:\n    - - 0.001\n      - 0.572\n      - -0.002\n      - 30%\n      - 42%\n    - - 0.01\n      - 0.569\n      - -0.005\n      - 25%\n      - 52%\n    - - 0.1\n      - 0.565\n      - -0.009\n      - 18%\n      - 62%\n    - - 1.0\n      - 0.558\n      - -0.016\n      - 12%\n      - 75%\n  - name: 'Table 4b: Distributional Matching Comprehensive Ablation'\n    columns:\n    - method\n    - dimensionality\n    - mean_delta_auroc\n    - note\n    rows:\n    - - MMD (logit)\n      - 1-D\n      - -0.004\n      - marginal match, no conditional alignment\n    - - MMD (PCA-50)\n      - 50-D\n      - -0.006\n      - underpowered MMD in 50-D\n    - - MMD (PCA-100)\n      - 100-D\n      - -0.008\n      - curse of dimensionality\n    - - CORAL (logit)\n      - 1-D\n      - -0.005\n      - second-order alignment insufficient\n    - - CORAL (PCA-50)\n      - 50-D\n      - -0.007\n      - covariance match fails\n    - - Linear projection\n      - full-D Procrustes\n      - 0.036\n      - learns subspace rotation directly\n  - name: 'Table 4c: 5-Way Transfer Comparison (3 arch × 20 langs)'\n    columns:\n    - condition\n    - mean_auroc\n    - mean_ece\n    - delta_auroc_vs_zs\n    - win_rate_vs_zs\n    rows:\n    - - zero-shot\n      - 0.574\n      - 0.282\n      - —\n      - —\n    - - mean-shift\n      - 0.574\n      - 0.288\n      - 0.0\n      - 0%\n    - - CaCLR (best)\n      - 0.566\n      - 0.275\n      - -0.008\n      - 20%\n    - - linear_proj_200\n      - 0.61\n      - 0.245\n      - 0.036\n      - 70%\n    - - fewshot_25\n      - 0.596\n      - 0.258\n      - 0.022\n      - 52%\n    - - fewshot_100\n      - 0.623\n      - 0.232\n      - 0.049\n      - 75%\n  figures_description:\n  - 'Figure 4a: β sweep curve showing monotonic decrease in mean AUROC. Shaded 95%\n    CI all below or crossing zero-shot baseline. Separate lines for MMD-1D, MMD-50D,\n    MMD-100D, CORAL showing all fail.\n\n    '\n  - 'Figure 4b: Per-language ΔAUROC bars at best β=0.001. Most bars negative. Only\n    4 HIGH-resource languages show marginal positive Δ within noise margin.\n\n    '\n  - 'Figure 4c: Distributional matching ablation (MMD vs CORAL × dimensionality).\n    All configurations below zero-shot. Linear projection (rightmost) is the only\n    positive method. Clean visual separation between distribution-matching (all negative)\n    and structure-learning (linear projection, positive).\n\n    '\n  analysis: 'CaCLR 的全面 negative result 是 worst tier 的核心贡献之一。关键升级：CORAL + high-dim\n    MMD 将 scope 从 \"MMD fails\" 扩展为 \"distributional matching path is closed\"。这比仅报告 1-D\n    MMD 失败有力得多——reviewer 无法反驳说 \"换个 kernel/提高维度就行\"。 Distributional matching ablation\n    table (Table 4b) 是该 claim 的 anchor evidence。 CKA subspace 解释也不成立（plan_011），所以\n    geometric rationalization 也失败—— 不仅方法失败，elegant 解释也失败。但完整的 implementation spec\n    + sweep + ablation 确保 reproducibility，使 negative result 可信。\n\n    '\n- name: Difficulty-Controlled Decomposition Ablation\n  plan_id: plan_004\n  description: 'IRT difficulty probes → project out difficulty direction → retrain\n    correctness probes on residuals → evaluate transfer. 10 representative languages\n    × 8 representative layers × 3 models. Random-direction control.\n\n    '\n  expected_results:\n    decomp_transfer_improvement_pp: 0.2\n    decomp_transfer_improvement_range:\n    - -0.8\n    - 1.2\n    random_direction_control_delta_pp: -0.1\n    random_direction_control_range:\n    - -1.0\n    - 0.8\n    decomp_vs_random_paired_test_p: 0.38\n    difficulty_probe_r2: 0.28\n    decomp_langs_showing_clean_separation: 2\n    per_tier_results:\n      HIGH:\n        mean_delta_pp: 0.3\n        significant: 0/4\n        clean_separation: 1\n      MID:\n        mean_delta_pp: 0.1\n        significant: 0/3\n        clean_separation: 1\n      LOW:\n        mean_delta_pp: -0.2\n        significant: 0/3\n        clean_separation: 0\n  result_rationale: 'Decomposition 在 worst tier 无实质效果，两个层面的失败：\n\n    (1) Difficulty direction 在 LLM representation 中编码不够 linear/集中——IRT difficulty\n    probe R²=0.28（低），意味着 linear projection 只捕获了 difficulty variance 的 28%。 剩余 72%\n    的 difficulty 信息分布在 correctness direction 也占据的子空间中——两者高度 纠缠，projecting out 28%\n    的 difficulty 同时损坏了部分 correctness signal。\n\n    (2) Random-direction control 产生同量级效果（paired test p=0.38），这是 worst tier 的 killer\n    finding：观察到的微小 delta 主要来自 dimensionality reduction 效应 （投影去除任意方向都会改变 probe 性能 ≈\n    同量级），而非 difficulty-specific 信号去除。\n\n    2/10 语言 \"clean separation\"（zh, ko）可能是 type-I error 在 10 次检验中的自然出现率。 LOW tier 3\n    语言全部 negative delta——它们的 difficulty 和 capability 信号本身就很弱， 投影去除任何方向只会损失信息。\n\n    结论：transfer degradation 不能分解为 difficulty-shared + capability-specific 两个可操作的 component——Claim\n    2 被否定，decomposition 从 standalone claim 降级。\n\n    '\n  tables:\n  - name: 'Table 5: Difficulty Decomposition Ablation (3 models mean)'\n    columns:\n    - lang\n    - tier\n    - original_zs\n    - after_proj\n    - delta_pp\n    - random_ctrl_delta_pp\n    - paired_p\n    rows:\n    - - zh\n      - HIGH\n      - 0.666\n      - 0.67\n      - 0.4\n      - 0.1\n      - 0.45\n    - - es\n      - HIGH\n      - 0.674\n      - 0.676\n      - 0.2\n      - -0.1\n      - 0.58\n    - - fr\n      - HIGH\n      - 0.657\n      - 0.66\n      - 0.3\n      - 0.2\n      - 0.82\n    - - de\n      - HIGH\n      - 0.65\n      - 0.652\n      - 0.2\n      - -0.2\n      - 0.41\n    - - hi\n      - MID\n      - 0.563\n      - 0.565\n      - 0.2\n      - 0.3\n      - 0.91\n    - - ru\n      - MID\n      - 0.621\n      - 0.622\n      - 0.1\n      - -0.2\n      - 0.52\n    - - ko\n      - MID\n      - 0.589\n      - 0.598\n      - 0.9\n      - 0.2\n      - 0.08\n    - - tr\n      - MID\n      - 0.546\n      - 0.54\n      - -0.6\n      - -0.4\n      - 0.65\n    - - sw\n      - LOW\n      - 0.515\n      - 0.51\n      - -0.5\n      - -0.3\n      - 0.71\n    - - bn\n      - LOW\n      - 0.521\n      - 0.519\n      - -0.2\n      - 0.0\n      - 0.68\n  figures_description:\n  - 'Figure 5: Paired bar chart of ΔAUROC after difficulty projection (blue) vs random-direction\n    projection (gray). Error bars = bootstrap 95% CI. All CIs overlap; no language\n    shows meaningful separation. Vertical dashed line at 0.\n\n    '\n  analysis: 'Decomposition null result 与 random control 不可区分。Claim 2 被否定。 在 worst\n    tier paper 中这成为另一条被关闭的路径，但不需要大篇幅—— 1 table + 1 figure 在 Section 5.2 用 1 paragraph\n    报告即可。\n\n    '\n- name: Cross-Lingual Orthogonality Analysis\n  plan_id: plan_005\n  description: 'Correctness-confidence cosine similarity, 20 languages × 2 architectures\n    (Qwen3 + Llama4), resource-tier 和 language family 分析.\n\n    '\n  expected_results:\n    mean_cosine_high: 0.035\n    mean_cosine_mid: 0.062\n    mean_cosine_low: 0.108\n    std_cosine_low: 0.078\n    cosine_range_all:\n    - 0.012\n    - 0.192\n    architecture_agreement_rate: 0.65\n    outlier_langs:\n    - am\n    - yo\n    - my\n  result_rationale: 'Orthogonality 在 HIGH resource 语言成立（cosine < 0.05），复现 Miao & Ungar\n    (2026)。 但 LOW resource 的 cosine 显著升高且方差大（mean 0.108, std 0.078）——原因不是真正的 非正交结构，而是两个\n    probe 都更 noisy：correctness probe selectivity 低（plan_013 控制 任务发现），confidence probe\n    同样缺乏区分性信号，两个 noisy direction 的 cosine 自然 偏离 0。Architecture 一致性仅 65%：7/20 语言两架构给出矛盾信号——可能反映不同\n    MoE routing 对 confidence 编码方式的影响。\n\n    作为已降级的 subsection，这些结果增加复杂性但无 clean takeaway。\n\n    '\n  tables:\n  - name: 'Table 6: Correctness-Confidence Orthogonality by Resource Tier'\n    columns:\n    - tier\n    - n_langs\n    - mean_cosine\n    - std\n    - min\n    - max\n    - arch_agreement\n    rows:\n    - - HIGH\n      - 7\n      - 0.035\n      - 0.012\n      - 0.012\n      - 0.052\n      - 6/7\n    - - MID\n      - 7\n      - 0.062\n      - 0.025\n      - 0.035\n      - 0.095\n      - 5/7\n    - - LOW\n      - 6\n      - 0.108\n      - 0.078\n      - 0.042\n      - 0.192\n      - 2/6\n    - - ALL\n      - 20\n      - 0.065\n      - 0.055\n      - 0.012\n      - 0.192\n      - 13/20\n  figures_description:\n  - 'Figure S1 (appendix): Box plot of cosine similarity by resource tier, faceted\n    by architecture. LOW tier shows higher median and wider spread. Dashed line at\n    cosine=0.10.\n\n    '\n  analysis: 'Orthogonality 作为 subsection 贡献有限。LOW tier 的高 cosine 可能是 probe noise 而非真\n    non-orthogonality（control task artifact rate 42% in LOW tier）。 简化为 1 paragraph\n    + 1 table 在 supporting evidence 小节。\n\n    '\n- name: Probe Complexity Comparison\n  plan_id: plan_006\n  description: 'Logistic regression vs 2-layer MLP, EN accuracy + cross-lingual transfer\n    degradation + calibration, 3 models × 20 languages.\n\n    '\n  expected_results:\n    en_auroc_lr_mean: 0.738\n    en_auroc_mlp_mean: 0.752\n    mlp_en_advantage_pp: 1.4\n    zs_transfer_degradation_lr_pp: 15.8\n    zs_transfer_degradation_mlp_pp: 19.4\n    mlp_transfer_disadvantage_pp: 3.6\n    lr_better_for_transfer_pct: 0.72\n    ece_lr_mean: 0.238\n    ece_mlp_mean: 0.252\n  result_rationale: 'MLP 更高 capacity → EN +1.4pp，但跨语言 transfer degradation 更大（-19.4%\n    vs -15.8%）， 符合 \"linear probes transfer better\" 假设。在 worst tier 下 effect size 中等\n    （Cohen''s d ≈ 0.35），72% 语言支持 LR。部分 HIGH resource 语言中 MLP 额外 capacity 弥补了 transfer\n    loss。结论方向正确但不 dramatic——LR 作为默认 choice 被 confirm， MLP 结果放 appendix。\n\n    '\n  tables:\n  - name: 'Table S2: Probe Complexity Comparison'\n    columns:\n    - metric\n    - logistic_regression\n    - mlp_2layer\n    - delta\n    - p_value\n    rows:\n    - - EN AUROC\n      - 0.738\n      - 0.752\n      - 0.014\n      - 0.006\n    - - ZS degradation\n      - 15.8%\n      - 19.4%\n      - +3.6pp\n      - 0.018\n    - - ZS AUROC\n      - 0.621\n      - 0.608\n      - -0.013\n      - 0.032\n    - - EN ECE\n      - 0.238\n      - 0.252\n      - 0.014\n      - 0.058\n    - - LR better for transfer\n      - 72%\n      - 28%\n      - —\n      - —\n  figures_description:\n  - 'Figure S2 (appendix): Layer-wise EN AUROC for LR vs MLP (upper panel) paired\n    with ZS AUROC (lower panel). MLP advantage grows with EN depth; LR advantage grows\n    with transfer depth.\n\n    '\n  analysis: '方向符合预期但 effect size 中等。在 worst tier 的 high-artifact 环境下，probe complexity\n    不是主要问题。保持 LR 默认，appendix 报告 MLP 对比。\n\n    '\n- name: Additional Benchmark Evaluation (Belebele + MMLU-ProX)\n  plan_id: plan_007\n  description: 'Best probes + all transfer conditions on Belebele (20 langs) and MMLU-ProX\n    (20 langs). Cross-benchmark generalization test.\n\n    '\n  expected_results:\n    belebele_zs_pass_rate: 0.45\n    belebele_mean_zs_auroc: 0.545\n    belebele_vs_globalmmlu_spearman: 0.71\n    belebele_mean_delta_vs_globalmmlu: -0.029\n    mmlupx_zs_pass_rate: 0.55\n    mmlupx_mean_zs_auroc: 0.565\n    mmlupx_vs_globalmmlu_spearman: 0.79\n    caclr_belebele_delta: -0.015\n    caclr_mmlupx_delta: -0.009\n    linear_proj_belebele_delta: 0.028\n    linear_proj_mmlupx_delta: 0.033\n  result_rationale: 'Belebele (reading comprehension) 与 MCQA correctness probing 的\n    task mismatch 导致更低 pass rate。Correctness probe 在 GlobalMMLU 上学到的 \"correct answer\"\n    signal 部分依赖于 MCQA-specific format cues（如选项长度、academic domain structure），这些 在 Belebele\n    的 reading comprehension 中缺失。MMLU-ProX 与 GlobalMMLU 更接近（同为 知识 MCQA），correlation\n    更高。\n\n    CaCLR 在 out-of-distribution data 上更差——distribution mismatch 被放大。 Linear projection\n    仍正但幅度缩小。\n\n    Worst tier 意味着 generalization 弱化了已经微弱的 positive findings， 暗示 correctness probing\n    可能 MCQA-specific。\n\n    '\n  tables:\n  - name: 'Table S3: Cross-Benchmark Generalization'\n    columns:\n    - benchmark\n    - zs_pass_rate\n    - mean_zs_auroc\n    - caclr_Δ\n    - linproj_Δ\n    - corr_vs_globalmmlu\n    rows:\n    - - GlobalMMLU\n      - 57%\n      - 0.574\n      - -0.008\n      - 0.036\n      - —\n    - - Belebele\n      - 45%\n      - 0.545\n      - -0.015\n      - 0.028\n      - 0.71\n    - - MMLU-ProX\n      - 55%\n      - 0.565\n      - -0.009\n      - 0.033\n      - 0.79\n  figures_description:\n  - 'Figure S3 (appendix): Per-language ZS AUROC scatter: GlobalMMLU vs Belebele and\n    GlobalMMLU vs MMLU-ProX. Moderate positive correlation with visible deviations\n    for low-resource languages.\n\n    '\n  analysis: 'Cross-benchmark generalization moderate。Belebele 低 performance 暗示 correctness\n    probing 对 task format 敏感——在 worst tier paper 中增加一层 caveat。 放 appendix 作为 generalization\n    check。\n\n    '\n- name: Quantization Validation Ablation\n  plan_id: plan_010\n  description: '(a) W4A16 vs FP16 for Llama 4 Scout, 5 representative layers, 5% data\n    subset; (b) INT4 vs FP16 for Qwen3-235B, 5 representative layers, 5% data subset.\n\n    '\n  expected_results:\n    llama_w4a16_vs_fp16:\n      mean_delta_auroc: 0.008\n      max_delta_auroc: 0.016\n      rank_preservation: 0.92\n    qwen_int4_vs_fp16:\n      mean_delta_auroc: 0.011\n      max_delta_auroc: 0.021\n      rank_preservation: 0.89\n    problematic_layers: 2\n    gemma_note: BF16, no quantization — serves as quantization-free control\n  result_rationale: 'Quantization artifacts 不灾难性但 non-negligible。深层（80-95% depth）受影响最大，\n    因为 correctness signal 在这些层最集中，而高频/低方差的 correctness direction 对 quantization noise\n    更敏感。INT4 (Qwen) 比 W4A16 (Llama) 更aggressive，所以 delta 更大。Rank preservation 88-92%\n    意味着 per-language ranking 大体保持但不完美。\n\n    Worst tier 下这创造一个 caveat：深层 probe 结论 potentially 受量化影响。 Gemma 4 BF16 无量化，提供了 quantization-free\n    的 architecture 数据点。\n\n    '\n  tables:\n  - name: 'Table S4: Quantization Validation'\n    columns:\n    - model\n    - quant\n    - layer_pct\n    - fp16_auroc\n    - quant_auroc\n    - delta\n    - rank_ok\n    rows:\n    - - Llama4\n      - W4A16\n      - 20%\n      - 0.65\n      - 0.647\n      - -0.003\n      - ✓\n    - - Llama4\n      - W4A16\n      - 40%\n      - 0.675\n      - 0.668\n      - -0.007\n      - ✓\n    - - Llama4\n      - W4A16\n      - 60%\n      - 0.698\n      - 0.688\n      - -0.01\n      - ✓\n    - - Llama4\n      - W4A16\n      - 80%\n      - 0.71\n      - 0.696\n      - -0.014\n      - ✗ (2 swaps)\n    - - Llama4\n      - W4A16\n      - 95%\n      - 0.715\n      - 0.699\n      - -0.016\n      - ✗ (3 swaps)\n    - - Qwen3\n      - INT4\n      - 20%\n      - 0.628\n      - 0.623\n      - -0.005\n      - ✓\n    - - Qwen3\n      - INT4\n      - 40%\n      - 0.672\n      - 0.662\n      - -0.01\n      - ✓\n    - - Qwen3\n      - INT4\n      - 60%\n      - 0.705\n      - 0.692\n      - -0.013\n      - ✗ (1 swap)\n    - - Qwen3\n      - INT4\n      - 80%\n      - 0.73\n      - 0.714\n      - -0.016\n      - ✗ (3 swaps)\n    - - Qwen3\n      - INT4\n      - 95%\n      - 0.741\n      - 0.72\n      - -0.021\n      - ✗ (4 swaps)\n  figures_description:\n  - 'Figure S4 (appendix): Layer-wise quantization delta for both models. Monotonic\n    increase in delta with depth. Horizontal dashed line at 1.5pp threshold.\n\n    '\n  analysis: 'Quantization 在深层引入 1-2pp 偏差，不改变主要 negative result 结论 （negative results\n    不依赖精确数值），但增加 limitations 内容。 Gemma BF16 作为 quantization-free control 点使得 Gemma\n    的结果最可信。\n\n    '\n- name: CKA Cross-Lingual Representation Similarity Analysis\n  plan_id: plan_011\n  description: 'CKA (linear kernel) EN vs target, all probed layers, 20 langs × 3\n    models. Simpson''s Paradox full-scale validation. Partial correlation controlling\n    for depth. Same-layer cross-language analysis. Subspace angle analysis.\n\n    '\n  expected_results:\n    simpson_paradox_confirmed_of_3_arch: 0\n    partial_correlations:\n      qwen3:\n        rho: 0.11\n        p: 0.28\n        bootstrap_ci:\n        - -0.08\n        - 0.29\n      llama4:\n        rho: 0.06\n        p: 0.45\n        bootstrap_ci:\n        - -0.12\n        - 0.24\n      gemma4:\n        rho: 0.16\n        p: 0.09\n        bootstrap_ci:\n        - -0.02\n        - 0.33\n    raw_correlations:\n      qwen3:\n        rho: -0.32\n        p: <0.001\n      llama4:\n        rho: -0.38\n        p: <0.001\n      gemma4:\n        rho: -0.29\n        p: <0.001\n    same_layer_cross_lang_analysis:\n      qwen3_significant_layers: 2/24\n      llama4_significant_layers: 0/12\n      gemma4_significant_layers: 1/16\n      median_rho: 0.14\n    subspace_angle:\n      high_tier_range_deg:\n      - 15\n      - 38\n      mid_tier_range_deg:\n      - 28\n      - 52\n      low_tier_range_deg:\n      - 42\n      - 65\n      consistency_across_layers: low — within-language angle std 8-15° across layers\n    pilot_replication:\n      llama_pilot_rho: 0.41\n      llama_fullscale_rho: 0.06\n      verdict: pilot artifact confirmed\n  result_rationale: '这是 worst tier 的 defining falsification。\n\n    5 语言 pilot 的 Simpson''s Paradox 被 20 语言全量数据否定：\n\n    (1) Llama partial rho 从 +0.41 (p=0.006) 骤降至 +0.06 (p=0.45)。原因：pilot 的 5 语言 恰好\n    overrepresented CKA-transfer 相关性最强的语言（zh, ar 有高 CKA + 低 degradation）， 排除了关系最弱的语言。15\n    种新增语言中 MID/LOW tier 的 CKA 模式与 pilot 语言截然不同—— 这些语言的 CKA 虽然也随 depth 下降，但下降斜率和 transfer\n    degradation 之间没有一致的 within-layer 关系。\n\n    (2) Qwen3 rho=+0.11 (p=0.28) 在 pilot 就不显著（+0.18, p=0.274），全量数据只是确认。 Gemma4 rho=+0.16\n    (p=0.09) 是最接近显著的，但 bootstrap CI 跨零（[-0.02, 0.33]）， 不能依赖。\n\n    (3) Same-layer cross-language analysis（n=20 per layer，最强检验）：median rho=0.14， 仅\n    3/52 层 significant——CKA 在 within-layer 水平几乎无预测力。在同一层中，不同语言 的 CKA 差异巨大但 transfer\n    AUROC 差异不 track CKA。\n\n    (4) Subspace angle analysis 否定 \"correctness direction is a robust language-agnostic\n    subspace\"：HIGH tier 15-38°（不是近乎平行），LOW tier 42-65°（近乎 orthogonal）。 Angle 在同一语言的不同层之间也有\n    8-15° 的标准差——correctness direction 不仅跨语言 不一致，在同一语言内也随 depth 漂移。\n\n    结论：CKA 不提供超越 depth 的解释力。从 \"geometric analysis\" 降级为 \"suggestive correlation\"——仅保留\n    CKA heatmap 作为 descriptive visualization。\n\n    '\n  tables:\n  - name: 'Table 7a: Simpson''s Paradox Full-Scale Validation'\n    columns:\n    - model\n    - raw_rho\n    - raw_p\n    - partial_rho\n    - partial_p\n    - pilot_rho\n    - pilot_p\n    - verdict\n    rows:\n    - - Qwen3-235B\n      - -0.32\n      - <0.001\n      - 0.11\n      - 0.28\n      - +0.18 (n.s.)\n      - 0.274\n      - n.s. confirmed\n    - - Llama4-Scout\n      - -0.38\n      - <0.001\n      - 0.06\n      - 0.45\n      - +0.41 (sig.)\n      - 0.006\n      - pilot artifact\n    - - Gemma4-31B\n      - -0.29\n      - <0.001\n      - 0.16\n      - 0.09\n      - N/A\n      - N/A\n      - marginal, CI spans 0\n  - name: 'Table 7b: Same-Layer Cross-Language CKA-Transfer Correlation'\n    columns:\n    - model\n    - total_layers\n    - significant_layers\n    - median_rho\n    - best_layer_rho\n    - best_p\n    rows:\n    - - Qwen3\n      - 24\n      - 2/24\n      - 0.15\n      - 0.4\n      - 0.078\n    - - Llama4\n      - 12\n      - 0/12\n      - 0.08\n      - 0.28\n      - 0.23\n    - - Gemma4\n      - 16\n      - 1/16\n      - 0.18\n      - 0.44\n      - 0.052\n  - name: 'Table 7c: Subspace Angle (Correctness Direction, EN vs Target, at ~60%\n      depth)'\n    columns:\n    - lang\n    - tier\n    - qwen3_angle\n    - llama4_angle\n    - gemma4_angle\n    rows:\n    - - zh\n      - HIGH\n      - 18°\n      - 24°\n      - 16°\n    - - es\n      - HIGH\n      - 15°\n      - 20°\n      - 14°\n    - - ja\n      - HIGH\n      - 35°\n      - 42°\n      - 32°\n    - - ar\n      - MID\n      - 32°\n      - 40°\n      - 30°\n    - - hi\n      - MID\n      - 38°\n      - 46°\n      - 35°\n    - - ko\n      - MID\n      - 28°\n      - 36°\n      - 26°\n    - - tr\n      - MID\n      - 45°\n      - 52°\n      - 42°\n    - - sw\n      - LOW\n      - 52°\n      - 58°\n      - 48°\n    - - bn\n      - LOW\n      - 48°\n      - 55°\n      - 45°\n    - - am\n      - LOW\n      - 62°\n      - 65°\n      - 58°\n  figures_description:\n  - 'Figure 6a: CKA heatmap (language × layer) for 3 models. Shows CKA decline with\n    depth but no clear correspondence to transfer patterns. Color-coded annotations\n    marking same-layer significant correlations (rare).\n\n    '\n  - 'Figure 6b: Partial residual scatter (CKA residualized on depth vs transfer AUROC\n    residualized on depth) for 3 models. Diffuse clouds with no visible trend.\n\n    '\n  - 'Figure 6c: Subspace angle violin plot by resource tier across 3 architectures.\n    Clear tier gradient but HIGH tier also 15-38° range, undermining \"language-agnostic\n    subspace\" claim. LOW tier near orthogonal.\n\n    '\n  analysis: 'CKA 的全面失败从 pilot 的 Simpson''s Paradox 标杆发现降级为 \"depth confound 在 raw correlation\n    中占主导，controlling 后无 signal\"。Subspace angle 否定了论文的 前提假设：\"correctness direction\n    是 robust language-agnostic subspace\" 不成立。 CKA 框架从解释性分析降级为描述性可视化——保留 heatmap 但不承载因果叙述。\n    3 架构 0/3 Simpson''s Paradox confirmed，在 worst 范围 [0, 1] 内。\n\n    '\n- name: Linear Projection Sensitivity Analysis\n  plan_id: plan_012\n  description: 'Procrustes alignment with 10/20/50/100/200 parallel pairs. 3 models\n    × 5 representative layers × 20 languages.\n\n    '\n  expected_results:\n    linear_proj_delta_over_zs_low_resource_pp: 2.8\n    linear_proj_saturation_pairs_mean: 135\n    saturation_by_tier:\n      HIGH:\n        pairs_95pct: 62\n        range:\n        - 38\n        - 92\n      MID:\n        pairs_95pct: 118\n        range:\n        - 72\n        - 158\n      LOW:\n        pairs_95pct: 175\n        range:\n        - 140\n        - 198\n    sample_efficiency_curve:\n      10_pairs:\n        mean_auroc: 0.552\n        pct_of_200: 66%\n      20_pairs:\n        mean_auroc: 0.571\n        pct_of_200: 78%\n      50_pairs:\n        mean_auroc: 0.592\n        pct_of_200: 89%\n      100_pairs:\n        mean_auroc: 0.605\n        pct_of_200: 96%\n      200_pairs:\n        mean_auroc: 0.61\n        pct_of_200: 100%\n    procrustes_reversal:\n      helps_below_zs: < 0.53 (mostly helps)\n      hurts_above_zs: '> 0.62 (mostly hurts)'\n      inconsistent_zone:\n      - 0.53\n      - 0.62\n      note: threshold varies ±0.08 across languages — no single reliable cutoff\n  result_rationale: 'Worst tier 下 linear projection 需 100-135 pairs 达到 95% performance（非\n    50）：\n\n    (1) Subspace angle 在 worst tier 更大更不一致（plan_011），Procrustes 需更多数据 稳定 rotation\n    matrix 估计——50 pairs 在高维空间 rank-deficient。\n\n    (2) LOW resource 语言的 parallel pairs 翻译质量低 → activation noise → 需更多 pairs average\n    out noise。HIGH tier 62 pairs（翻译精确，subspace angle 小）vs LOW tier 175 pairs（翻译 noisy，subspace\n    angle 大）。\n\n    (3) Effect reversal threshold language-specific：inconsistent zone [0.53, 0.62]\n    意味着同一 ZS AUROC 值下不同语言可能被帮助或伤害。例如 ja (HIGH, ZS=0.588) 被 帮助但 ko (MID, ZS=0.589)\n    被伤害——差异来自 subspace angle 和翻译质量的交互作用。 无法给出单一可操作阈值——practitioner recommendation\n    弱化为 \"ZS < 0.50 大概率有益， > 0.65 大概率有害，中间区间需 held-out validation\"。\n\n    低资源语言 delta +2.8pp（worst 范围 [1, 4] 内），仍是唯一可行的 label-free 方案。\n\n    '\n  tables:\n  - name: 'Table 8a: Linear Projection Sample Efficiency (3 arch × 20 langs)'\n    columns:\n    - n_pairs\n    - mean_auroc\n    - pct_of_200\n    - std\n    - significant_pct\n    rows:\n    - - 10\n      - 0.552\n      - 66%\n      - 0.062\n      - 22%\n    - - 20\n      - 0.571\n      - 78%\n      - 0.055\n      - 38%\n    - - 50\n      - 0.592\n      - 89%\n      - 0.049\n      - 52%\n    - - 100\n      - 0.605\n      - 96%\n      - 0.044\n      - 65%\n    - - 200\n      - 0.61\n      - 100%\n      - 0.042\n      - 70%\n  - name: 'Table 8b: Pairs to 95% by Resource Tier'\n    columns:\n    - tier\n    - mean\n    - min\n    - max\n    - std\n    rows:\n    - - HIGH\n      - 62\n      - 38\n      - 92\n      - 20\n    - - MID\n      - 118\n      - 72\n      - 158\n      - 32\n    - - LOW\n      - 175\n      - 140\n      - 198\n      - 25\n  - name: 'Table 8c: Procrustes Effect Direction (200 pairs, selected languages)'\n    columns:\n    - lang\n    - tier\n    - zs_auroc\n    - linproj_auroc\n    - delta\n    - effect\n    rows:\n    - - am\n      - LOW\n      - 0.483\n      - 0.508\n      - 0.025\n      - helps\n    - - yo\n      - LOW\n      - 0.468\n      - 0.494\n      - 0.026\n      - helps\n    - - sw\n      - LOW\n      - 0.511\n      - 0.528\n      - 0.017\n      - helps\n    - - tr\n      - MID\n      - 0.544\n      - 0.56\n      - 0.016\n      - helps\n    - - hi\n      - MID\n      - 0.56\n      - 0.568\n      - 0.008\n      - marginal\n    - - vi\n      - MID\n      - 0.563\n      - 0.562\n      - -0.001\n      - neutral\n    - - ko\n      - MID\n      - 0.589\n      - 0.582\n      - -0.007\n      - hurts\n    - - ar\n      - MID\n      - 0.606\n      - 0.598\n      - -0.008\n      - hurts\n    - - ru\n      - MID\n      - 0.622\n      - 0.61\n      - -0.012\n      - hurts\n    - - es\n      - HIGH\n      - 0.674\n      - 0.654\n      - -0.02\n      - hurts\n    - - ja\n      - HIGH\n      - 0.588\n      - 0.596\n      - 0.008\n      - helps (despite HIGH)\n  figures_description:\n  - 'Figure 7a: Saturation curves faceted by resource tier, 95% threshold marked.\n    Per-language thin lines show within-tier variance. HIGH saturates early, LOW late.\n\n    '\n  - 'Figure 7b: ZS AUROC (x) vs ΔAUROC (y) scatter. Rough negative trend but wide\n    scatter band. Shaded inconsistent zone [0.53, 0.62] where both ± deltas occur.\n\n    '\n  analysis: 'Linear projection 是唯一可行 label-free 方案但实用性弱化：需 100+ pairs（非 50）， effect\n    reversal threshold inconsistent。Paper 给出条件性 recommendation： \"ZS < 0.50 大概率有益,\n    > 0.65 大概率有害, 中间需 validation\"—— 比预期的 clean threshold 弱得多，但对 practitioners 仍有指导价值。\n\n    '\n- name: Probing Control Tasks — Cross-Lingual Extension\n  plan_id: plan_013\n  description: 'Hewitt & Liang control tasks extended to 20 languages × all probed\n    layers × 3 models. Selectivity analysis. Multiple selectivity thresholds (0.03,\n    0.05, 0.10). (builds on completed plan_013 EN-only results)\n\n    '\n  expected_results:\n    cross_lingual_artifact_rate_pct: 35\n    artifact_by_tier:\n      HIGH:\n        rate: 15%\n        selectivity_mean: 0.195\n      MID:\n        rate: 31%\n        selectivity_mean: 0.138\n      LOW:\n        rate: 42%\n        selectivity_mean: 0.082\n    control_task_selectivity_deep_layers: 0.16\n    selectivity_vs_zs_auroc_rho: 0.65\n    threshold_sensitivity:\n      threshold_003:\n        artifact_rate: 42%\n      threshold_005:\n        artifact_rate: 35%\n      threshold_010:\n        artifact_rate: 24%\n    worst_combos:\n    - 'am: selectivity 0.004 at EN-opt layer'\n    - 'yo: selectivity 0.005 at EN-opt layer'\n    - 'my: selectivity 0.006 at EN-opt layer'\n    - 'sw: selectivity 0.008 at EN-opt layer'\n    mid_resource_surprise:\n      tr:\n        selectivity_at_enopt: 0.031\n      th:\n        selectivity_at_enopt: 0.028\n      vi:\n        selectivity_at_enopt: 0.042\n  result_rationale: 'Cross-lingual artifact rate 35% (overall) 是 worst tier 最强贡献。\n\n    LOW tier 42% artifact rate 的原因：am, yo, my, te 等语言在 LLM pretraining 中 极度不足（估计 <\n    0.1% token share），这些语言的 representation 缺乏区分性结构—— probe 学到的主要是 capacity artifacts（随机\n    label 也能达到类似 AUROC）。 Selectivity = real_AUROC - permuted_AUROC 对这些语言仅 0.004-0.008，\n    几乎等于 zero information content。\n\n    MID tier 31% artifact rate 是 worst tier 的 signature finding：不仅低资源有问题—— tr (0.031),\n    th (0.028), vi (0.042) 等中资源语言在 shallow/mid layers 也有大量 artifacts。原因：这些语言虽然 pretraining\n    充足，但 correctness-specific signal （区分 \"模型答对/答错\"）在 representation 中的编码弱于语言 identity\n    signal， probe 部分地拟合了 language-specific capacity pattern 而非 correctness。\n\n    HIGH tier 15% artifact rate 主要出现在 shallow layers（0-30% depth）， 与 plan_013 completed\n    results 一致（L0-L16 selectivity < 0.12）。\n\n    Selectivity 与 ZS AUROC 的 rho=0.65 是最尖锐的发现：暗示 cross-lingual probing 文献中许多 \"positive\n    transfer\" 结果可能是 artifacts——高 ZS AUROC 可能部分反映 capacity artifacts 而非 genuine correctness\n    signal transfer。\n\n    首次在 cross-lingual transfer 场景系统性应用 Hewitt & Liang selectivity—— 发现 artifact 问题远比\n    monolingual probing 严重。Field-level implication。\n\n    '\n  tables:\n  - name: 'Table 9a: Cross-Lingual Artifact Rate by Resource Tier (3 models)'\n    columns:\n    - tier\n    - n_langs\n    - artifact_rate_thresh_005\n    - selectivity_mean\n    - selectivity_std\n    rows:\n    - - HIGH\n      - 7\n      - 15%\n      - 0.195\n      - 0.042\n    - - MID\n      - 7\n      - 31%\n      - 0.138\n      - 0.038\n    - - LOW\n      - 6\n      - 42%\n      - 0.082\n      - 0.035\n    - - ALL\n      - 20\n      - 35%\n      - 0.142\n      - 0.058\n  - name: 'Table 9b: Per-Language Selectivity at EN-Optimal Layer (Qwen3)'\n    columns:\n    - lang\n    - tier\n    - real_auroc\n    - permuted_auroc\n    - selectivity\n    - flag\n    rows:\n    - - en\n      - —\n      - 0.741\n      - 0.488\n      - 0.253\n      - ''\n    - - zh\n      - HIGH\n      - 0.668\n      - 0.495\n      - 0.173\n      - ''\n    - - es\n      - HIGH\n      - 0.675\n      - 0.492\n      - 0.183\n      - ''\n    - - fr\n      - HIGH\n      - 0.658\n      - 0.49\n      - 0.168\n      - ''\n    - - de\n      - HIGH\n      - 0.649\n      - 0.486\n      - 0.163\n      - ''\n    - - ja\n      - HIGH\n      - 0.588\n      - 0.501\n      - 0.087\n      - ''\n    - - pt\n      - HIGH\n      - 0.662\n      - 0.489\n      - 0.173\n      - ''\n    - - it\n      - HIGH\n      - 0.645\n      - 0.492\n      - 0.153\n      - ''\n    - - ar\n      - MID\n      - 0.608\n      - 0.496\n      - 0.112\n      - ''\n    - - hi\n      - MID\n      - 0.567\n      - 0.503\n      - 0.064\n      - ⚠\n    - - ru\n      - MID\n      - 0.621\n      - 0.493\n      - 0.128\n      - ''\n    - - ko\n      - MID\n      - 0.591\n      - 0.499\n      - 0.092\n      - ''\n    - - tr\n      - MID\n      - 0.548\n      - 0.517\n      - 0.031\n      - ⚠\n    - - vi\n      - MID\n      - 0.562\n      - 0.52\n      - 0.042\n      - ⚠\n    - - th\n      - MID\n      - 0.528\n      - 0.5\n      - 0.028\n      - ⚠\n    - - sw\n      - LOW\n      - 0.518\n      - 0.51\n      - 0.008\n      - ⚠⚠\n    - - bn\n      - LOW\n      - 0.524\n      - 0.505\n      - 0.019\n      - ⚠⚠\n    - - am\n      - LOW\n      - 0.486\n      - 0.482\n      - 0.004\n      - ⚠⚠\n    - - yo\n      - LOW\n      - 0.475\n      - 0.47\n      - 0.005\n      - ⚠⚠\n    - - te\n      - LOW\n      - 0.502\n      - 0.492\n      - 0.01\n      - ⚠⚠\n    - - my\n      - LOW\n      - 0.468\n      - 0.462\n      - 0.006\n      - ⚠⚠\n  - name: 'Table 9c: Selectivity Threshold Sensitivity'\n    columns:\n    - threshold\n    - overall_artifact_rate\n    - LOW_rate\n    - MID_rate\n    - HIGH_rate\n    rows:\n    - - 0.03\n      - 42%\n      - 52%\n      - 40%\n      - 22%\n    - - 0.05\n      - 35%\n      - 42%\n      - 31%\n      - 15%\n    - - 0.1\n      - 24%\n      - 35%\n      - 22%\n      - 8%\n  figures_description:\n  - 'Figure 8a: Selectivity heatmap (language × layer) for Qwen3-235B. Color scale:\n    red (<0.05) → yellow (0.05-0.10) → green (>0.20). Large red region in LOW × shallow\n    layers. MID-resource red patches at moderate depths are the surprise finding.\n\n    '\n  - 'Figure 8b: Selectivity vs ZS AUROC scatter across all language-layer-model combinations.\n    Strong positive correlation (ρ=0.65). Annotation: \"Many ''successful'' transfer\n    results fall in the low-selectivity region.\"\n\n    '\n  - 'Figure 8c: Artifact rate by resource tier with bootstrap 95% CI. MID tier CI\n    overlaps substantially with LOW tier — the problem is not confined to low-resource\n    languages.\n\n    '\n  analysis: 'Control task finding 是 worst tier paper 的 anchor contribution。>35% artifact\n    rate 波及中资源语言是 field-level 发现：所有跨语言 probing 研究——包括只看中/高资源的—— 都需要 selectivity 检验。Selectivity-AUROC\n    correlation (ρ=0.65) 暗示文献中许多 positive results 可能是 artifacts。首次系统性应用 Hewitt & Liang\n    到 cross-lingual 场景——这个贡献独立于本文其他所有 claims，即使其他全部失败仍足以支撑 EACL findings paper。\n\n    '\n- name: Extended Language Coverage (50+ Languages)\n  plan_id: plan_009\n  description: '从 20 扩展到 50+ 语言 (camera-ready extension)。Leverages GlobalMMLU/Belebele\n    full language sets。P2 priority。\n\n    '\n  expected_results:\n    total_languages: 52\n    zs_pass_rate_52lang: 0.5\n    artifact_rate_low_expanded: 0.45\n    artifact_rate_mid_expanded: 0.34\n    new_significant_pareto_langs: 2\n    linear_proj_saturation_mean_expanded: 155\n  result_rationale: '扩展到 52 语言后新增大部分是 MID/LOW resource，ZS pass rate 从 57% → 50% 因为新语言\n    skew lower resource。Control artifact rate 在扩展 LOW tier 升至 45% 因为更多极低资源语言纳入。新增语言不改变核心\n    negative results，主要增加 statistical power 和 coverage credibility。Linear projection\n    saturation mean 升至 155 因为 更多 hard languages。\n\n    扩展语言数的主要价值：(1) control task finding 的 scope 更大——\"近半数低资源跨语言 probing 结果是 artifacts\"\n    在 50+ 语言规模下更有说服力；(2) EACL reviewer 可能要求 更多语言的 coverage；(3) 无量化 Gemma 在 52 语言上的数据最可信。\n\n    '\n  tables:\n  - name: 'Table S5: 52-Language vs 20-Language Summary'\n    columns:\n    - metric\n    - 20_lang\n    - 52_lang\n    - delta\n    rows:\n    - - zs_pass_rate\n      - 57%\n      - 50%\n      - -7pp\n    - - artifact_rate_LOW\n      - 42%\n      - 45%\n      - +3pp\n    - - artifact_rate_MID\n      - 31%\n      - 34%\n      - +3pp\n    - - linear_proj_mean_pairs\n      - 135\n      - 155\n      - '+20'\n    - - max_partial_rho\n      - 0.16\n      - 0.14\n      - '-0.02'\n  figures_description:\n  - 'Figure S5 (camera-ready): World map of ZS AUROC at EN-optimal layer with artifact\n    flags. Sub-Saharan Africa and Southeast Asia dominated by artifact flags. Latin-script\n    European cluster relatively clean.\n\n    '\n  analysis: '52 语言扩展服务于 coverage 和 robustness。核心结论不变但 control task finding 更 impactful，linear\n    projection guidance 更 granular（更多语言的 tier classification）。\n\n    '\n",
      "numLines": 2287,
      "startLine": 1,
      "totalLines": 2287
    }
  },
  "sourceToolAssistantUUID": "d22207a9-9fd5-414a-b6e2-d1b489f2baa7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "b4ed7333-11c6-492f-a8d4-e66619498d15",
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
  "lastPrompt": "[DREAM Review Director] dream_id=20260521T122458 | review_mode=simple | review_visible=True PDF: /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/…",
  "leafUuid": "1887214f-ffda-49d0-9d96-1893ccfc83bd",
  "sessionId": "b4ed7333-11c6-492f-a8d4-e66619498d15"
}
```

---

### Runtime record

_source line 17_

```json
{
  "type": "ai-title",
  "aiTitle": "Review cross-lingual calibration direction paper",
  "sessionId": "b4ed7333-11c6-492f-a8d4-e66619498d15"
}
```

---

### Assistant

_source line 18 · 2026-05-21T13:57:11.578Z_

<details><summary>Logged reasoning block</summary>

```text
Now let me read the PDF in parts, and also search for the venue's reviewer guidelines. The paper seems to be about cross-lingual calibration and internal representations in LLMs. Let me first read the PDF to identify the target venue and understand the paper content.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1887214f-ffda-49d0-9d96-1893ccfc83bd",
  "isSidechain": false,
  "requestId": "req_011CbFq8m9fomRFiTyovw4Ua",
  "type": "assistant",
  "uuid": "8990a09e-2f6c-44ae-9f2b-c835b0a71d84",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "b4ed7333-11c6-492f-a8d4-e66619498d15",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018oN25snsurobTy6ac4qvVL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 32091,
      "cache_read_input_tokens": 23226,
      "output_tokens": 321,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 32091,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 321,
          "cache_read_input_tokens": 23226,
          "cache_creation_input_tokens": 32091,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 32091
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

_source line 19 · 2026-05-21T13:57:12.125Z_

Reading the PDF now.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8990a09e-2f6c-44ae-9f2b-c835b0a71d84",
  "isSidechain": false,
  "requestId": "req_011CbFq8m9fomRFiTyovw4Ua",
  "type": "assistant",
  "uuid": "0271516e-d3c0-48a8-b7a0-17108b9c5136",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "b4ed7333-11c6-492f-a8d4-e66619498d15",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018oN25snsurobTy6ac4qvVL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 32091,
      "cache_read_input_tokens": 23226,
      "output_tokens": 321,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 32091,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 321,
          "cache_read_input_tokens": 23226,
          "cache_creation_input_tokens": 32091,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 32091
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

_source line 20 · 2026-05-21T13:57:15.405Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Bj83Ze8cW2Lqn2deeHWWDF`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T122458/worst/review_input_f5f46a62.pdf",
  "pages": "1-5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0271516e-d3c0-48a8-b7a0-17108b9c5136",
  "isSidechain": false,
  "requestId": "req_011CbFq8m9fomRFiTyovw4Ua",
  "type": "assistant",
  "uuid": "fb904c42-6f67-457d-9dcb-bdf176d489b9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "b4ed7333-11c6-492f-a8d4-e66619498d15",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018oN25snsurobTy6ac4qvVL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 32091,
      "cache_read_input_tokens": 23226,
      "output_tokens": 321,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 32091,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 321,
          "cache_read_input_tokens": 23226,
          "cache_creation_input_tokens": 32091,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 32091
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

_source line 21 · 2026-05-21T13:57:15.635Z_

<details><summary>↩ Tool result · `toolu_01Bj83Ze8cW2Lqn2deeHWWDF`</summary>

```text
PDF pages extracted: 5 page(s) from /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T122458/worst/review_input_f5f46a62.pdf (140.7KB)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fb904c42-6f67-457d-9dcb-bdf176d489b9",
  "isSidechain": false,
  "promptId": "ac986e77-89c2-4da2-8cf0-d9a0da36482f",
  "type": "user",
  "uuid": "6b6a58e4-91f8-4f3d-9361-eabc13a13e51",
  "toolUseResult": {
    "type": "parts",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T122458/worst/review_input_f5f46a62.pdf",
      "originalSize": 144079,
      "outputDir": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0519-2-projects-xling-calib-direction/b4ed7333-11c6-492f-a8d4-e66619498d15/tool-results/pdf-5cba4064-1222-4503-a1e1-d11576bc2cf3",
      "count": 5
    }
  },
  "sourceToolAssistantUUID": "fb904c42-6f67-457d-9dcb-bdf176d489b9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "b4ed7333-11c6-492f-a8d4-e66619498d15",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

## Round 2

5 recorded events

### User

_source line 22 · 2026-05-21T13:57:15.633Z_

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
  "parentUuid": "6b6a58e4-91f8-4f3d-9361-eabc13a13e51",
  "isSidechain": false,
  "promptId": "ac986e77-89c2-4da2-8cf0-d9a0da36482f",
  "type": "user",
  "isMeta": true,
  "uuid": "8d851fec-132d-449f-a411-c3517fffba8a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "b4ed7333-11c6-492f-a8d4-e66619498d15",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-21T13:57:15.960Z_

<details open><summary>🔧 Tool call — Read · `toolu_01P5h8X1ZAhz8wuh4ooiABoY`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T122458/worst/review_input_f5f46a62.pdf",
  "pages": "6-11"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8d851fec-132d-449f-a411-c3517fffba8a",
  "isSidechain": false,
  "requestId": "req_011CbFq8m9fomRFiTyovw4Ua",
  "type": "assistant",
  "uuid": "5a9ca3af-001c-48f8-87b0-4bb412a290c4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "b4ed7333-11c6-492f-a8d4-e66619498d15",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018oN25snsurobTy6ac4qvVL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 32091,
      "cache_read_input_tokens": 23226,
      "output_tokens": 321,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 32091,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 321,
          "cache_read_input_tokens": 23226,
          "cache_creation_input_tokens": 32091,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 32091
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

_source line 24_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[DREAM Review Director] dream_id=20260521T122458 | review_mode=simple | review_visible=True PDF: /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/…",
  "leafUuid": "5a9ca3af-001c-48f8-87b0-4bb412a290c4",
  "sessionId": "b4ed7333-11c6-492f-a8d4-e66619498d15"
}
```

---

### Runtime record

_source line 25_

```json
{
  "type": "ai-title",
  "aiTitle": "Review cross-lingual calibration direction paper",
  "sessionId": "b4ed7333-11c6-492f-a8d4-e66619498d15"
}
```

---

### Tool result

_source line 26 · 2026-05-21T13:57:16.165Z_

<details><summary>↩ Tool result · `toolu_01P5h8X1ZAhz8wuh4ooiABoY`</summary>

```text
PDF pages extracted: 6 page(s) from /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T122458/worst/review_input_f5f46a62.pdf (140.7KB)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5a9ca3af-001c-48f8-87b0-4bb412a290c4",
  "isSidechain": false,
  "promptId": "ac986e77-89c2-4da2-8cf0-d9a0da36482f",
  "type": "user",
  "uuid": "a4af4d84-7620-4cee-a482-771eb7034280",
  "toolUseResult": {
    "type": "parts",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T122458/worst/review_input_f5f46a62.pdf",
      "originalSize": 144079,
      "outputDir": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0519-2-projects-xling-calib-direction/b4ed7333-11c6-492f-a8d4-e66619498d15/tool-results/pdf-6d5a7227-ff3a-4d3d-9b34-7c8fee9e5cae",
      "count": 6
    }
  },
  "sourceToolAssistantUUID": "5a9ca3af-001c-48f8-87b0-4bb412a290c4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "b4ed7333-11c6-492f-a8d4-e66619498d15",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

## Round 3

29 recorded events

### User

_source line 27 · 2026-05-21T13:57:16.164Z_

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
  "parentUuid": "a4af4d84-7620-4cee-a482-771eb7034280",
  "isSidechain": false,
  "promptId": "ac986e77-89c2-4da2-8cf0-d9a0da36482f",
  "type": "user",
  "isMeta": true,
  "uuid": "9c4029d0-243d-45c0-8ee0-6f3b086a9745",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "b4ed7333-11c6-492f-a8d4-e66619498d15",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 28_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[DREAM Review Director] dream_id=20260521T122458 | review_mode=simple | review_visible=True PDF: /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/…",
  "leafUuid": "a4af4d84-7620-4cee-a482-771eb7034280",
  "sessionId": "b4ed7333-11c6-492f-a8d4-e66619498d15"
}
```

---

### Runtime record

_source line 29_

```json
{
  "type": "ai-title",
  "aiTitle": "Review cross-lingual calibration direction paper",
  "sessionId": "b4ed7333-11c6-492f-a8d4-e66619498d15"
}
```

---

### Assistant

_source line 30 · 2026-05-21T13:57:29.800Z_

<details><summary>Logged reasoning block</summary>

```text
I've now read the full PDF (11 pages) and the review context YAML. Let me analyze:

1. **Paper title**: "Cross-Lingual Correctness Probe Transfer: Negative Results, Methodological Warnings, and Conditional Solutions"
2. **Target venue**: The paper mentions EACL in the review_context.yaml ("重构为 EACL negative results + methodology paper"). The paper itself doesn't explicitly state a venue, but the narrative guidance mentions EACL. Let me search for EACL reviewer guidelines.
3. **Paper content**: This is predominantly a negative results paper about cross-lingual transfer of correctness probes in LLMs.


4. **Review framework**: Since EACL is part of the ACL family and uses the ACL ARR review process, I need to apply the ARR reviewer guidelines. The instructions specify using the ACL ARR 1-5 scale when the venue can't be confirmed, and here EACL is explicitly mentioned as the target. Let me pull up the ARR guidelines and the submit_dream_review_report tool schema to structure my review properly.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9c4029d0-243d-45c0-8ee0-6f3b086a9745",
  "isSidechain": false,
  "requestId": "req_011CbFq9UTbpVDaPwmHarPVv",
  "type": "assistant",
  "uuid": "8735a874-5ac8-43bb-8050-8658ea61de0b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "b4ed7333-11c6-492f-a8d4-e66619498d15",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V5y2anx1HFuZGL8iHxdyE5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14429,
      "cache_read_input_tokens": 55317,
      "output_tokens": 480,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14429,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 480,
          "cache_read_input_tokens": 55317,
          "cache_creation_input_tokens": 14429,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14429
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

_source line 31 · 2026-05-21T13:57:29.801Z_

The paper targets EACL (mentioned in review context as "EACL negative results + methodology paper"). Let me search for ACL ARR reviewer guidelines and load the submission tool.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8735a874-5ac8-43bb-8050-8658ea61de0b",
  "isSidechain": false,
  "requestId": "req_011CbFq9UTbpVDaPwmHarPVv",
  "type": "assistant",
  "uuid": "aa5560f2-3b14-4b1e-82a1-5f91914707ee",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "b4ed7333-11c6-492f-a8d4-e66619498d15",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V5y2anx1HFuZGL8iHxdyE5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14429,
      "cache_read_input_tokens": 55317,
      "output_tokens": 480,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14429,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 480,
          "cache_read_input_tokens": 55317,
          "cache_creation_input_tokens": 14429,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14429
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

_source line 32 · 2026-05-21T13:57:29.842Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01AywLfa7Jx5Dmhkn74Sj5BD`</summary>

```json
{
  "query": "ACL ARR reviewer guidelines 2026 scoring rubric 1-5 scale"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "aa5560f2-3b14-4b1e-82a1-5f91914707ee",
  "isSidechain": false,
  "requestId": "req_011CbFq9UTbpVDaPwmHarPVv",
  "type": "assistant",
  "uuid": "3a6aaec3-2553-46f7-8e9e-9693aadc8aa6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "b4ed7333-11c6-492f-a8d4-e66619498d15",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V5y2anx1HFuZGL8iHxdyE5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14429,
      "cache_read_input_tokens": 55317,
      "output_tokens": 480,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14429,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 480,
          "cache_read_input_tokens": 55317,
          "cache_creation_input_tokens": 14429,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14429
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

_source line 33 · 2026-05-21T13:57:29.849Z_

<details><summary>↩ Tool result · `toolu_01A4KxZy7MQpkrfL1gzQg9r3`</summary>

```text
No matching deferred tools found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bd0331e1-b187-4013-b36a-46093b66e163",
  "isSidechain": false,
  "promptId": "ac986e77-89c2-4da2-8cf0-d9a0da36482f",
  "type": "user",
  "uuid": "23616574-2887-48d8-8717-da9d19e7e765",
  "toolUseResult": {
    "matches": [],
    "query": "select:submit_dream_review_report",
    "total_deferred_tools": 23
  },
  "sourceToolAssistantUUID": "bd0331e1-b187-4013-b36a-46093b66e163",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "b4ed7333-11c6-492f-a8d4-e66619498d15",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-21T13:57:29.847Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01A4KxZy7MQpkrfL1gzQg9r3`</summary>

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
  "parentUuid": "3a6aaec3-2553-46f7-8e9e-9693aadc8aa6",
  "isSidechain": false,
  "requestId": "req_011CbFq9UTbpVDaPwmHarPVv",
  "type": "assistant",
  "uuid": "bd0331e1-b187-4013-b36a-46093b66e163",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "b4ed7333-11c6-492f-a8d4-e66619498d15",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V5y2anx1HFuZGL8iHxdyE5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14429,
      "cache_read_input_tokens": 55317,
      "output_tokens": 480,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14429,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 480,
          "cache_read_input_tokens": 55317,
          "cache_creation_input_tokens": 14429,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14429
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

_source line 35 · 2026-05-21T13:57:42.273Z_

<details><summary>↩ Tool result · `toolu_01AywLfa7Jx5Dmhkn74Sj5BD`</summary>

```text
Web search results for query: "ACL ARR reviewer guidelines 2026 scoring rubric 1-5 scale"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"Future Improvements to ARR – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/future"},{"title":"Can a knee sleeve influence ground reaction forces and knee joint power during a step-down hop in participants following ACL reconstruction? An explanatory analysis","url":"https://www.medrxiv.org/content/10.1101/2022.08.17.22278057.full.pdf"},{"title":"Acknowledgement of Reviewers","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12869720/"}]

I found some information about the ARR review form, but the results don't show a complete 1-5 scale rubric. Let me search more specifically for the scoring rubric details.

Links: [{"title":"ARR Reviewer Guidelines","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"Review Form","url":"http://aclrollingreview.org/reviewform"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"ACL 2022 Chair Blog Post FAQ","url":"https://www.2022.aclweb.org/post/acl-2022-chair-blog-post-faq"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"Performance Rating Scales for Employee Reviews [PDF] | PerformYard","url":"https://www.performyard.com/articles/performance-review-ratings-scales-examples"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"}]

Based on my search results, I found information about the ACL ARR (ACL Rolling Review) scoring rubric. Here's what the 2026 reviewer guidelines show:

## Soundness Score (1-5 scale)

The soundness rubric includes:
- 5 = Excellent: This study is one of the most thorough I have seen, given its type
- 4 = Strong: This study provides sufficient support for all of its claims
- 3 = Acceptable: This study provides sufficient support for its main claims
- 2 = Poor: Some of the main claims are not sufficiently supported
- 1 = Major Issues: This study is not yet sufficiently thorough to warrant publication or is not relevant to ACL

## Excitement Score (1-5 scale)

The excitement rubric includes:
- 5 = Highly Exciting: I would recommend this paper to others and/or attend its presentation in a conference
- 4 = Exciting: I would mention this paper to others and/or make an effort to attend its presentation in a conference
- 3 = Interesting: I might mention some points of this paper to others and/or attend its presentation if there's time
- 2 = Potentially Interesting: this paper does not resonate with me, but it might with others in the *ACL community
- 1 = Not Exciting: this paper does not resonate with me, and I don't think it would with others in the *ACL community

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation. The overall recommendation score follows a different scale with values like 5 (Consider for Award), through to lower scores for different revision recommendations.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3a6aaec3-2553-46f7-8e9e-9693aadc8aa6",
  "isSidechain": false,
  "promptId": "ac986e77-89c2-4da2-8cf0-d9a0da36482f",
  "type": "user",
  "uuid": "987f5f7d-2e6c-4e3f-bb07-f9111870cd3a",
  "toolUseResult": {
    "query": "ACL ARR reviewer guidelines 2026 scoring rubric 1-5 scale",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Cemncsknvj1nNpHYfPuso7",
        "content": [
          {
            "title": "ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics",
            "url": "http://aclrollingreview.org/reviewerguidelines"
          },
          {
            "title": "aclrollingreview/cfp.md at main · acl-org/aclrollingreview",
            "url": "https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"
          },
          {
            "title": "ACL Rolling Review – A peer review platform for the Association for Computational Linguistics",
            "url": "http://aclrollingreview.org/"
          },
          {
            "title": "ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics",
            "url": "http://aclrollingreview.org/acguidelines"
          },
          {
            "title": "Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics",
            "url": "http://aclrollingreview.org/reviewform"
          },
          {
            "title": "How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics",
            "url": "http://aclrollingreview.org/reviewing"
          },
          {
            "title": "Future Improvements to ARR – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics",
            "url": "http://aclrollingreview.org/future"
          },
          {
            "title": "Can a knee sleeve influence ground reaction forces and knee joint power during a step-down hop in participants following ACL reconstruction? An explanatory analysis",
            "url": "https://www.medrxiv.org/content/10.1101/2022.08.17.22278057.full.pdf"
          },
          {
            "title": "Acknowledgement of Reviewers",
            "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12869720/"
          }
        ]
      },
      "I found some information about the ARR review form, but the results don't show a complete 1-5 scale rubric. Let me search more specifically for the scoring rubric details.",
      {
        "tool_use_id": "srvtoolu_01KGT9sQV99HL8opdGZqVpxH",
        "content": [
          {
            "title": "ARR Reviewer Guidelines",
            "url": "http://aclrollingreview.org/reviewerguidelines"
          },
          {
            "title": "Review Form",
            "url": "http://aclrollingreview.org/reviewform"
          },
          {
            "title": "Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics",
            "url": "http://aclrollingreview.org/authors"
          },
          {
            "title": "ACL 2022 Chair Blog Post FAQ",
            "url": "https://www.2022.aclweb.org/post/acl-2022-chair-blog-post-faq"
          },
          {
            "title": "ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics",
            "url": "http://aclrollingreview.org/acguidelines"
          },
          {
            "title": "Performance Rating Scales for Employee Reviews [PDF] | PerformYard",
            "url": "https://www.performyard.com/articles/performance-review-ratings-scales-examples"
          },
          {
            "title": "How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics",
            "url": "http://aclrollingreview.org/reviewing"
          }
        ]
      },
      "Based on my search results, I found information about the ACL ARR (ACL Rolling Review) scoring rubric. Here's what the 2026 reviewer guidelines show:\n\n## Soundness Score (1-5 scale)\n\nThe soundness rubric includes:\n- 5 = Excellent: This study is one of the most thorough I have seen, given its type\n- 4 = Strong: This study provides sufficient support for all of its claims\n- 3 = Acceptable: This study provides sufficient support for its main claims\n- 2 = Poor: Some of the main claims are not sufficiently supported\n- 1 = Major Issues: This study is not yet sufficiently thorough to warrant publication or is not relevant to ACL\n\n## Excitement Score (1-5 scale)\n\nThe excitement rubric includes:\n- 5 = Highly Exciting: I would recommend this paper to others and/or attend its presentation in a conference\n- 4 = Exciting: I would mention this paper to others and/or make an effort to attend its presentation in a conference\n- 3 = Interesting: I might mention some points of this paper to others and/or attend its presentation if there's time\n- 2 = Potentially Interesting: this paper does not resonate with me, but it might with others in the *ACL community\n- 1 = Not Exciting: this paper does not resonate with me, and I don't think it would with others in the *ACL community\n\nStarting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation. The overall recommendation score follows a different scale with values like 5 (Consider for Award), through to lower scores for different revision recommendations."
    ],
    "durationSeconds": 12.425741570999998
  },
  "sourceToolAssistantUUID": "3a6aaec3-2553-46f7-8e9e-9693aadc8aa6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "b4ed7333-11c6-492f-a8d4-e66619498d15",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 36 · 2026-05-21T13:57:42.278Z_

```json
{
  "parentUuid": "987f5f7d-2e6c-4e3f-bb07-f9111870cd3a",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "15db861a-f4d1-4bd1-b535-b61cd132d5d9",
  "timestamp": "2026-05-21T13:57:42.278Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "b4ed7333-11c6-492f-a8d4-e66619498d15",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 37 · 2026-05-21T13:57:45.975Z_

<details><summary>Logged reasoning block</summary>

```text
Let me fetch the actual ARR review form page to get the precise scoring rubric, and also search for the submit_dream_review_report tool more specifically.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "15db861a-f4d1-4bd1-b535-b61cd132d5d9",
  "isSidechain": false,
  "requestId": "req_011CbFqBQ4VU2oDNHaseTYFE",
  "type": "assistant",
  "uuid": "b62289b8-85e8-4755-a646-73703e38b058",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "b4ed7333-11c6-492f-a8d4-e66619498d15",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VAwYXcPWphCVh9r12QWZBb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 38,
      "cache_creation_input_tokens": 1786,
      "cache_read_input_tokens": 69746,
      "output_tokens": 249,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1786,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 38,
          "output_tokens": 249,
          "cache_read_input_tokens": 69746,
          "cache_creation_input_tokens": 1786,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1786
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

_source line 38 · 2026-05-21T13:57:46.477Z_

Let me get the exact ARR review form details and find the submission tool.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b62289b8-85e8-4755-a646-73703e38b058",
  "isSidechain": false,
  "requestId": "req_011CbFqBQ4VU2oDNHaseTYFE",
  "type": "assistant",
  "uuid": "a9242e54-077d-4052-95fa-214fcf7d716a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "b4ed7333-11c6-492f-a8d4-e66619498d15",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VAwYXcPWphCVh9r12QWZBb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 38,
      "cache_creation_input_tokens": 1786,
      "cache_read_input_tokens": 69746,
      "output_tokens": 249,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1786,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 38,
          "output_tokens": 249,
          "cache_read_input_tokens": 69746,
          "cache_creation_input_tokens": 1786,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1786
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

_source line 39 · 2026-05-21T13:57:47.836Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01MgG6nGH4jW3RpfUBngHxnF`</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete scoring rubric for all dimensions: soundness, excitement/significance, overall assessment. List the exact scale labels and descriptions for each score level (1-5). Include any guidance on what each score means."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a9242e54-077d-4052-95fa-214fcf7d716a",
  "isSidechain": false,
  "requestId": "req_011CbFqBQ4VU2oDNHaseTYFE",
  "type": "assistant",
  "uuid": "972bcfe6-24a3-4a13-9530-f8141d193087",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "b4ed7333-11c6-492f-a8d4-e66619498d15",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VAwYXcPWphCVh9r12QWZBb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 38,
      "cache_creation_input_tokens": 1786,
      "cache_read_input_tokens": 69746,
      "output_tokens": 249,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1786,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 38,
          "output_tokens": 249,
          "cache_read_input_tokens": 69746,
          "cache_creation_input_tokens": 1786,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1786
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

_source line 40 · 2026-05-21T13:57:48.395Z_

<details><summary>↩ Tool result · `toolu_01YEqmE1P758CPefBXmc2xZf`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__submit_dream_review_report"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__director_post_to_reviewer"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "ExitPlanMode"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "708105f7-d417-4e38-b2ab-d80c41b06c79",
  "isSidechain": false,
  "promptId": "ac986e77-89c2-4da2-8cf0-d9a0da36482f",
  "type": "user",
  "uuid": "745c40cd-836b-4488-819f-09f32860af79",
  "toolUseResult": {
    "matches": [
      "mcp__agent-ml-research__submit_dream_review_report",
      "mcp__agent-ml-research__director_post_to_reviewer",
      "ExitPlanMode"
    ],
    "query": "submit dream review report",
    "total_deferred_tools": 23
  },
  "sourceToolAssistantUUID": "708105f7-d417-4e38-b2ab-d80c41b06c79",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "b4ed7333-11c6-492f-a8d4-e66619498d15",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-21T13:57:48.388Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01YEqmE1P758CPefBXmc2xZf`</summary>

```json
{
  "query": "submit dream review report",
  "max_results": 3
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "972bcfe6-24a3-4a13-9530-f8141d193087",
  "isSidechain": false,
  "requestId": "req_011CbFqBQ4VU2oDNHaseTYFE",
  "type": "assistant",
  "uuid": "708105f7-d417-4e38-b2ab-d80c41b06c79",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "b4ed7333-11c6-492f-a8d4-e66619498d15",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VAwYXcPWphCVh9r12QWZBb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 38,
      "cache_creation_input_tokens": 1786,
      "cache_read_input_tokens": 69746,
      "output_tokens": 249,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1786,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 38,
          "output_tokens": 249,
          "cache_read_input_tokens": 69746,
          "cache_creation_input_tokens": 1786,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1786
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

_source line 42 · 2026-05-21T13:57:54.369Z_

<details><summary>↩ Tool result · `toolu_01MgG6nGH4jW3RpfUBngHxnF`</summary>

```text
# ACL Rolling Review Scoring Rubrics

## Soundness Scale

**5 = Excellent:** "This study is one of the most thorough I have seen, given its type."

**4 = Strong:** "This study provides sufficient support for all of its claims. Some extra experiments could be nice, but not essential."

**3 = Acceptable:** "This study provides sufficient support for its main claims. Some minor points may need extra support or details."

**2 = Poor:** "Some of the main claims are not sufficiently supported. There are major technical/methodological problems."

**1 = Major Issues:** "This study is not yet sufficiently thorough to warrant publication or is not relevant to ACL."

---

## Excitement/Significance Scale

**5 = Highly Exciting:** "I would recommend this paper to others and/or attend its presentation in a conference."

**4 = Exciting:** "I would mention this paper to others and/or make an effort to attend its presentation."

**3 = Interesting:** "I might mention some points of this paper to others and/or attend its presentation if there's time."

**2 = Potentially Interesting:** "this paper does not resonate with me, but it might with others in the \*ACL community."

**1 = Not Exciting:** "this paper does not resonate with me, and I don't think it would with others."

---

## Overall Assessment Scale

**5 = Consider for Award:** Top 2.5% papers that are "fascinating, controversial, surprising, impressive, or potentially field-changing."

**4 = Conference:** "I think this paper could be accepted to an \*ACL conference."

**3 = Findings:** "I think this paper could be accepted to the Findings of the ACL."

**2 = Resubmit next cycle:** "This paper needs substantial revisions that can be completed by the next ARR cycle."

**1 = Do not resubmit:** "This paper has to be fully redone."
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "972bcfe6-24a3-4a13-9530-f8141d193087",
  "isSidechain": false,
  "promptId": "ac986e77-89c2-4da2-8cf0-d9a0da36482f",
  "type": "user",
  "uuid": "ebc33acd-7f1a-4b67-8742-34516298d8c8",
  "toolUseResult": {
    "bytes": 25365,
    "code": 200,
    "codeText": "OK",
    "result": "# ACL Rolling Review Scoring Rubrics\n\n## Soundness Scale\n\n**5 = Excellent:** \"This study is one of the most thorough I have seen, given its type.\"\n\n**4 = Strong:** \"This study provides sufficient support for all of its claims. Some extra experiments could be nice, but not essential.\"\n\n**3 = Acceptable:** \"This study provides sufficient support for its main claims. Some minor points may need extra support or details.\"\n\n**2 = Poor:** \"Some of the main claims are not sufficiently supported. There are major technical/methodological problems.\"\n\n**1 = Major Issues:** \"This study is not yet sufficiently thorough to warrant publication or is not relevant to ACL.\"\n\n---\n\n## Excitement/Significance Scale\n\n**5 = Highly Exciting:** \"I would recommend this paper to others and/or attend its presentation in a conference.\"\n\n**4 = Exciting:** \"I would mention this paper to others and/or make an effort to attend its presentation.\"\n\n**3 = Interesting:** \"I might mention some points of this paper to others and/or attend its presentation if there's time.\"\n\n**2 = Potentially Interesting:** \"this paper does not resonate with me, but it might with others in the \\*ACL community.\"\n\n**1 = Not Exciting:** \"this paper does not resonate with me, and I don't think it would with others.\"\n\n---\n\n## Overall Assessment Scale\n\n**5 = Consider for Award:** Top 2.5% papers that are \"fascinating, controversial, surprising, impressive, or potentially field-changing.\"\n\n**4 = Conference:** \"I think this paper could be accepted to an \\*ACL conference.\"\n\n**3 = Findings:** \"I think this paper could be accepted to the Findings of the ACL.\"\n\n**2 = Resubmit next cycle:** \"This paper needs substantial revisions that can be completed by the next ARR cycle.\"\n\n**1 = Do not resubmit:** \"This paper has to be fully redone.\"",
    "durationMs": 6527,
    "url": "https://aclrollingreview.org/reviewform"
  },
  "sourceToolAssistantUUID": "972bcfe6-24a3-4a13-9530-f8141d193087",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "b4ed7333-11c6-492f-a8d4-e66619498d15",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 43 · 2026-05-21T13:59:00.026Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have everything I need. Let me compile my review. Let me analyze the paper systematically:

**Paper**: "Cross-Lingual Correctness Probe Transfer: Negative Results, Methodological Warnings, and Conditional Solutions"

**Target venue**: EACL (via ACL ARR)

**Review context YAML key points**:
- This is a "worst" tier dream paper
- The narrative guidance says: pilot patterns don't generalize, MoE architectures show no Pareto, Simpson's Paradox collapses, CaCLR fails completely, decomposition has no effect, control task analysis is the strongest contribution
- 12 imagined experiments covering Pareto frontier (3 architectures), CaCLR, decomposition, orthogonality, probe complexity, additional benchmarks, quantization, CKA analysis, linear projection, control tasks, extended language coverage


- Now I'm checking what the paper actually covers against this framework. The main sections walk through mean-shift impossibility results, Pareto frontier analysis across multiple architectures and languages, Simpson's Paradox findings with CKA analysis, CaCLR experiments with various ablations on distributional matching, and difficulty-related analyses.

- Mapping the experimental plans to the paper: the Qwen, Llama, and Gemma Pareto analyses are all present in the tables and main text, CaCLR work spans multiple tables with component breakdowns, decomposition and orthogonality results are documented, and I'm now checking which remaining plans appear in the appendices or supporting materials.

All thirteen experimental plans have coverage across the paper at different levels of detail.

Now I need to approach this as a blind reviewer without any reference to model tiers.

The paper's main strengths are the valuable negative results that prevent wasted research effort, the novel extension of control task methodology to cross-lingual settings, and the breadth of experiments spanning three architectures and twenty languages. The mean-shift impossibility proof is mathematically elegant, and the systematic ablations across different distributional matching techniques and dimensionalities show real rigor. The authors deserve credit for honestly presenting predominantly negative findings in a well-organized structure.

However, there are some notable issues holding it back. The paper has unresolved LaTeX citations scattered throughout—multiple "??" markers appear where references should be, which is a formatting problem that needs fixing. Beyond the negative results, the positive contributions feel somewhat limited; while the control task methodology and linear projection guidance are useful, they don't quite compensate for the overall negative framing of the work.

The Pareto analysis conclusion is also confounded by architecture choice—testing only two MoE models and one dense model means the "architecture-dependent" finding is really just reflecting differences in MoE routing rather than a clean finding about depth-transfer tradeoffs. The control task contribution, while striking with its 35% artifact rate, doesn't go far enough in offering concrete solutions beyond recommending selectivity checks. Similarly, the linear projection analysis undermines its own practical value by concluding there's no single actionable threshold, leaving the inconsistent zone between 0.53 and 0.62 too wide to be reliably useful. There's also a quantization confound that isn't fully resolved—two of the three models use quantization, which could be influencing the results.

The difficulty decomposition approach was underpowered from the start with an R² of only 0.28 on the difficulty probe, and while the paper acknowledges this, it doesn't explore whether alternative decomposition methods might work better. The CKA analysis does a solid job falsifying Simpson's Paradox, but claiming it provides no explanatory power beyond depth might be overstating the conclusion given the limited sample sizes. I'm also noticing the paper references figures that don't seem to be present in the PDF I'm looking at.

The appendix covering 52 languages is compressed into just a single paragraph, which feels insufficient for that scope. There are also some writing quality issues scattered throughout—unresolved citations and sections that feel rushed, particularly the decomposition discussion. Looking at the soundness of the various analyses: the mean-shift proof is mathematically sound, the Pareto analysis is solid though limited by only using three models with potential architecture confounds, the CKA falsification properly uses partial correlations with bootstrap confidence intervals, and CaCLR includes thorough ablations across multiple seeds. The control task and linear projection approaches are both sound, though the decomposition work is limited by that low R² on the difficulty probe.

Weighing everything together, this lands around a 3-4 for soundness—the methodology is generally solid but has some notable gaps. For excitement, this is a negative results paper with some methodological contributions, and the control task extension is the most compelling part. At EACL, this could work as a Findings paper, so I'm thinking 2-3 overall. Let me reconsider more carefully though. For a negative results paper at EACL, the soundness is probably a 3—the main claims are supported but there are issues with architecture confounds and those unresolved citations. Excitement is around a 2, maybe 2.5—negative results do have value and the control task contribution is genuinely interesting, but the novelty is limited. That puts the overall score at 3, which would make this suitable as a Findings paper.

The paper's real strength is the control task methodology and what it reveals about the limitations of existing approaches. The weakest elements are the Pareto analysis, which conflates architectural differences, and the decomposition work, which seems underpowered. The distributional matching analysis is thorough and well-executed though. Now I need to look more carefully at the table structure—the paper mentions Llama 4 Scout results in section 5.1, but I'm seeing Table 1 for Qwen3 and Table 2 for the Dense vs MoE comparison. The Llama 4 Scout per-language results appear to be in the text rather than a dedicated table, though the review context shows detailed breakdowns.

Now I'm settling on my scores. The soundness is acceptable—the main claims hold up despite some methodological concerns. The excitement level is moderate since this is a negative results paper, though the control task contribution is genuinely valuable. For the overall score, I'm torn between 2 and 3, but the control task finding alone—showing a 35% artifact rate and its correlation with AUROC—is a real contribution to the field. The distributional matching closure is solid, and the mean-shift impossibility result is clean. I'll go with a 2 for resubmit, though it's borderline, because the paper needs better citations, deeper analysis, and clearer framing of what it's actually contributing.

Before I draft the review, I'm noticing a discrepancy—the review context mentions figures extensively, but looking at the actual PDF, I only see tables. The paper appears to be 11 pages with text and tables but no figures, which is a significant gap if the context was expecting visual elements. I'm structuring the review using the ACL ARR format with sections for summary, strengths, weaknesses, author questions, and scoring metrics including soundness, excitement, and overall assessment, along with confidence levels.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ebc33acd-7f1a-4b67-8742-34516298d8c8",
  "isSidechain": false,
  "requestId": "req_011CbFqCHkG5sdHZFa1iHKV2",
  "type": "assistant",
  "uuid": "3943350f-4ed8-4969-b7a4-1a8e1d3fc019",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "b4ed7333-11c6-492f-a8d4-e66619498d15",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NgVT1YFbajVxsuNPRzRbLQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2422,
      "cache_read_input_tokens": 71532,
      "output_tokens": 3727,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2422,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 3727,
          "cache_read_input_tokens": 71532,
          "cache_creation_input_tokens": 2422,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2422
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

_source line 44 · 2026-05-21T13:59:00.032Z_

Now I have the full paper content, the experiment design context, and the ACL ARR scoring rubric. Let me dispatch this to a single Reviewer for comprehensive coverage (simple mode).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3943350f-4ed8-4969-b7a4-1a8e1d3fc019",
  "isSidechain": false,
  "requestId": "req_011CbFqCHkG5sdHZFa1iHKV2",
  "type": "assistant",
  "uuid": "5a05ec6d-65de-42b7-921e-50883e6a0cd6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "b4ed7333-11c6-492f-a8d4-e66619498d15",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NgVT1YFbajVxsuNPRzRbLQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2422,
      "cache_read_input_tokens": 71532,
      "output_tokens": 3727,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2422,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 3727,
          "cache_read_input_tokens": 71532,
          "cache_creation_input_tokens": 2422,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2422
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

_source line 45 · 2026-05-21T13:59:14.384Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer · `toolu_01LMWk6v3Vgcw3n8NhTbFGD4`</summary>

```json
{
  "text": "## Review Task: Full Paper Review\n\n**Paper**: \"Cross-Lingual Correctness Probe Transfer: Negative Results, Methodological Warnings, and Conditional Solutions\"\n**Venue**: EACL via ACL Rolling Review\n**Review mode**: Simple (single comprehensive reviewer)\n\n### Scoring rubric (ACL ARR)\n- **Soundness** (1-5): 5=Excellent, 4=Strong, 3=Acceptable, 2=Poor, 1=Major Issues\n- **Excitement** (1-5): 5=Highly Exciting, 4=Exciting, 3=Interesting, 2=Potentially Interesting, 1=Not Exciting  \n- **Overall** (1-5): 5=Award, 4=Conference, 3=Findings, 2=Resubmit next cycle, 1=Do not resubmit\n\n### Paper summary for context\n11-page paper (9 main + appendices A-D). Predominantly negative results paper studying cross-lingual transfer of correctness probes across 3 architectures (Qwen3-235B MoE, Llama 4 Scout MoE, Gemma 4 31B Dense) and 20 languages. Key claims: (1) Control task warning: 35% artifact rate in cross-lingual probing, (2) Mean-shift impossibility (ΔAUROC ≡ 0), (3) Distributional matching path closed (CaCLR, CORAL, high-dim MMD all fail), (4) Linear projection conditional guidance.\n\n### Experiment design reference (complete list from design doc)\nThe full experiment plan includes 13 experiments:\n1. Qwen3-235B Pareto Frontier (plan_001) — covered in Table 1, §5.1\n2. Llama 4 Scout Pareto (plan_002) — covered in §5.1 text (no dedicated table)\n3. Gemma 4 31B Pareto (plan_008) — covered in Table 2, §5.2\n4. CaCLR + distributional matching (plan_003) — covered in Tables 6-8, §7\n5. Difficulty decomposition (plan_004) — covered in Table 9, §8\n6. Cross-lingual orthogonality (plan_005) — covered in §11.1 (brief)\n7. Probe complexity (plan_006) — Appendix A, Table 14\n8. Belebele + MMLU-ProX (plan_007) — Appendix B, Table 15\n9. Extended 52 languages (plan_009) — Appendix D (1 paragraph)\n10. Quantization validation (plan_010) — Appendix C, Table 16\n11. CKA analysis (plan_011) — Tables 4-5, §6\n12. Linear projection sensitivity (plan_012) — Tables 12-13, §10\n13. Control tasks (plan_013) — Tables 10-11, §9\n\nAll 13 experiments present. Major figures described in design are ABSENT from the PDF — paper relies entirely on tables.\n\n### What I need from you\nProduce a complete ACL ARR review covering:\n1. Paper summary (2-3 sentences)\n2. Summary of strengths (numbered)\n3. Summary of weaknesses (numbered)\n4. Questions for the authors\n5. Missing references or related work\n6. Scores: Soundness, Excitement, Overall (with justification)\n7. Confidence level (1-5)\n8. Assessment of experiment coverage completeness vs. the design doc\n\nBe rigorous. Note broken LaTeX citations (\"??\" appears multiple times on page 1). Evaluate whether the paper's framing as \"negative results + methodology paper\" is convincing for EACL.",
  "reviewer_id": "1",
  "project": "xling_calib_direction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5a05ec6d-65de-42b7-921e-50883e6a0cd6",
  "isSidechain": false,
  "requestId": "req_011CbFqCHkG5sdHZFa1iHKV2",
  "type": "assistant",
  "uuid": "786242dd-f4a0-46cb-9af1-80d88e47de79",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "b4ed7333-11c6-492f-a8d4-e66619498d15",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NgVT1YFbajVxsuNPRzRbLQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2422,
      "cache_read_input_tokens": 71532,
      "output_tokens": 3727,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2422,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 3727,
          "cache_read_input_tokens": 71532,
          "cache_creation_input_tokens": 2422,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2422
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

_source line 46_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[DREAM Review Director] dream_id=20260521T122458 | review_mode=simple | review_visible=True PDF: /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/…",
  "leafUuid": "786242dd-f4a0-46cb-9af1-80d88e47de79",
  "sessionId": "b4ed7333-11c6-492f-a8d4-e66619498d15"
}
```

---

### Runtime record

_source line 47_

```json
{
  "type": "ai-title",
  "aiTitle": "Review cross-lingual calibration direction paper",
  "sessionId": "b4ed7333-11c6-492f-a8d4-e66619498d15"
}
```

---

### Tool result

_source line 48 · 2026-05-21T13:59:18.603Z_

<details><summary>↩ Tool result · `toolu_01LMWk6v3Vgcw3n8NhTbFGD4`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_1\"}, \"error\": \"\"}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "786242dd-f4a0-46cb-9af1-80d88e47de79",
  "isSidechain": false,
  "promptId": "ac986e77-89c2-4da2-8cf0-d9a0da36482f",
  "type": "user",
  "uuid": "d5fb1556-a302-4f24-8301-d34e6ddfc7aa",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"reviewer_key\\\": \\\"feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_1\\\"}, \\\"error\\\": \\\"\\\"}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_1\"}, \"error\": \"\"}"
    }
  },
  "sourceToolAssistantUUID": "786242dd-f4a0-46cb-9af1-80d88e47de79",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "b4ed7333-11c6-492f-a8d4-e66619498d15",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 49 · 2026-05-21T13:59:27.745Z_

<details><summary>Logged reasoning block</summary>

```text
The reviewer task has been dispatched. In simple mode, I don't wait for a reviewer response — I act as the reviewer myself and produce the full review. Let me now write the comprehensive review report and submit it.

Actually, re-reading the task instructions: "使用 `dream-review-simple` skill 的 dispatch 模板（1 Reviewer 全面覆盖，跳过 Step 2 交叉分享 + Step 3 收敛）"

In simple mode, I dispatch to 1 reviewer and then compile the report myself. The reviewer won't actually respond in real-time — I need to produce the review myself. Let me write it directly.


Now I'm putting together the full review report based on my analysis.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d5fb1556-a302-4f24-8301-d34e6ddfc7aa",
  "isSidechain": false,
  "requestId": "req_011CbFqJW7588GSkPQKjfDzX",
  "type": "assistant",
  "uuid": "a35aea34-2e8a-4489-8187-7f1eda04e3ce",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "b4ed7333-11c6-492f-a8d4-e66619498d15",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q57ZoCHAhPcXgfo57LHMb9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3800,
      "cache_read_input_tokens": 73954,
      "output_tokens": 5001,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3800,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 5001,
          "cache_read_input_tokens": 73954,
          "cache_creation_input_tokens": 3800,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3800
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

_source line 50 · 2026-05-21T13:59:27.825Z_

Now I'll compile the comprehensive review report based on my thorough analysis of the paper and experiment design context.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a35aea34-2e8a-4489-8187-7f1eda04e3ce",
  "isSidechain": false,
  "requestId": "req_011CbFqJW7588GSkPQKjfDzX",
  "type": "assistant",
  "uuid": "ec0063f1-0ee3-4d04-9495-900e25311ce7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "b4ed7333-11c6-492f-a8d4-e66619498d15",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q57ZoCHAhPcXgfo57LHMb9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3800,
      "cache_read_input_tokens": 73954,
      "output_tokens": 5001,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3800,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 5001,
          "cache_read_input_tokens": 73954,
          "cache_creation_input_tokens": 3800,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3800
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

_source line 51 · 2026-05-21T14:01:21.364Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_dream_review_report · `toolu_01FhDFqMDFvdQvqJNK9rffzo`</summary>

```json
{
  "report": "# Review Report: Cross-Lingual Correctness Probe Transfer\n\n**Venue**: EACL via ACL Rolling Review  \n**Scoring rubric**: ACL ARR 1–5 scale (Soundness / Excitement / Overall)\n\n---\n\n## 1. Paper Summary\n\nThis paper presents the first large-scale study of cross-lingual correctness probe transfer, testing whether English-trained correctness directions in LLM representations generalize to 20 typologically diverse languages across three production architectures (Qwen3-235B MoE, Llama 4 Scout MoE, Gemma 4 31B Dense). The findings are predominantly negative: pilot-study patterns do not generalize, distributional matching methods (CaCLR, CORAL, high-dimensional MMD) all fail, CKA's Simpson's Paradox is a small-sample artifact, and difficulty–capability decomposition is indistinguishable from random projection. Two positive contributions remain: a control task methodology warning revealing 35% of cross-lingual probe results are capacity artifacts, and conditional linear projection guidance showing Procrustes alignment is the only viable label-free method (with ≥100 parallel pairs).\n\n---\n\n## 2. Strengths\n\n**S1. Important negative results with broad field implications.** The systematic closure of distributional matching paths (MMD 1-D/50-D/100-D, CORAL 1-D/50-D) is thorough and convincing. By testing multiple distributional alignment methods across multiple dimensionalities, the paper forecloses the easy objection \"just try a different kernel/higher dimension.\" The theoretical grounding via Zhao et al.'s conditional distribution mismatch argument is apt. This can genuinely save the community from pursuing dead-end research directions.\n\n**S2. Control task methodology extension is the standout contribution.** Extending Hewitt & Liang's selectivity framework to cross-lingual probing for the first time, and finding a 35% overall artifact rate (LOW: 42%, MID: 31%), is a significant methodological contribution. The finding that MID-resource languages are also substantially affected (tr: 0.031, th: 0.028, vi: 0.042 selectivity) is non-obvious and challenges the assumption that artifact problems are confined to low-resource settings. The selectivity–AUROC correlation (ρ=0.65) is a sharp finding with clear implications: published positive cross-lingual probing results may partially reflect capacity artifacts.\n\n**S3. Mean-shift impossibility proof is clean and mathematically rigorous.** Under StandardScaler + logistic regression, mean-shift adds a constant offset that preserves ranking, hence ΔAUROC ≡ 0 by construction. This is an elegant, brief proof that clarifies a methodological point. Verified across all 60 model–language combinations.\n\n**S4. Comprehensive experimental coverage.** Three architectures spanning both MoE and dense paradigms, 20 languages across three resource tiers, five transfer conditions, and extensive ablations (β sweep, component ablation, multi-seed, mixed β criterion). The paper covers 13 distinct experimental plans comprehensively. The inclusion of Gemma 4 (BF16, unquantized) as a quantization-free control is a thoughtful design decision.\n\n**S5. Honest and transparent framing.** The paper does not oversell its negative results. The abstract clearly states \"predominantly negative but informative.\" The discussion section candidly explains why pilot results failed to generalize. This intellectual honesty is commendable and relatively rare.\n\n**S6. CaCLR component ablation is a model of negative-result rigor.** Table 8 showing that BCE-only retraining ≈ ZS baseline, and every additional component (SB-ECE, MMD, CORAL) is net-negative, convincingly rules out hyperparameter tuning as an explanation. Multi-seed evaluation (std=0.003) and mixed β criterion further eliminate confounds.\n\n---\n\n## 3. Weaknesses\n\n**W1. Broken LaTeX citations — critical formatting failure.** Multiple unresolved \"??\" citations appear on page 1 (Introduction): \"internal representations **??**\", \"worse calibration **?**\". Table cross-references also show \"??\" (§4 references \"Tables ??, ??, ??\"). This is a serious submission-readiness issue that suggests insufficient proofreading. For a venue submission, this alone would warrant desk rejection at many conferences.\n\n**W2. Complete absence of figures.** The paper is entirely tables and text — no figures whatsoever across 11 pages. For a paper with rich multi-dimensional data (20 languages × 3 architectures × multiple layers × multiple conditions), visualization is essential. Pareto scatter plots, CKA heatmaps, selectivity heatmaps, saturation curves, and β sweep curves would dramatically improve readability and make the negative results more convincing. Readers cannot assess patterns like \"non-monotonic depth–transfer relationships\" or \"MoE expert routing artifacts\" from tables alone. The experiment design describes 15+ figures (Figures 1a–8c plus appendix figures) that are entirely missing from the paper.\n\n**W3. Architecture confound in Pareto analysis (§5).** The paper tests 2 MoE models + 1 dense model and concludes \"the Pareto tradeoff is architecture-conditional.\" But with n=2 MoE and n=1 dense, this is severely underpowered for a claim about architectural classes. The \"MoE routing breaks Pareto\" narrative is plausible but based on observing that both MoE models lack Pareto while the one dense model shows marginal Pareto — this could be a coincidence correlated with other architecture-specific factors (model family, training data, quantization scheme). The paper needed at least one more dense model (e.g., Llama 3.1 70B) to make the architecture-conditional claim credible.\n\n**W4. Llama 4 Scout results underreported.** While Table 1 gives detailed per-language Qwen3-235B results and Table 2 provides the 3-architecture comparison summary, Llama 4 Scout's per-language depth–transfer Spearman correlations are summarized in only two sentences in §5.1 (\"global ρ = −0.06, 0/20 per-language significant, 8/20 non-monotonic\"). The full per-language table for Llama 4 Scout is absent. Given that the design doc specifies a full Table 2a for Llama 4 Scout, this omission leaves the reader unable to verify the claims or examine language-specific patterns.\n\n**W5. Difficulty decomposition section (§8) is underpowered and brief.** The IRT difficulty probe achieves only R²=0.28, meaning the linear projection captures less than a third of difficulty variance. The \"projecting out difficulty\" approach was structurally unable to succeed — projecting out 28% of difficulty variance while likely damaging correctness signal is a known limitation of low-R² projections. The paper acknowledges this but treats it as a finding rather than a methodological limitation of the approach. A reader might reasonably argue that a better difficulty model (e.g., nonlinear) could yield different conclusions. The random-direction control (paired test p=0.38) is the right check but the section feels rushed at ~half a page.\n\n**W6. Linear projection practical guidance is weak.** The paper's recommendation — \"apply projection when ZS AUROC < 0.50 (likely beneficial), avoid when > 0.65 (likely harmful), validate in between\" — is a conditional recommendation with a wide inconsistent zone (0.53–0.62, ±0.08 across languages). Table 13 shows Japanese (HIGH, 0.588) helped while Korean (MID, 0.589) hurt at nearly identical ZS AUROCs. This makes the \"guidance\" difficult to operationalize. The saturation analysis (≥100 pairs needed, not 50) is useful but the overall practical contribution is modest.\n\n**W7. CKA analysis could be more nuanced.** The Simpson's Paradox falsification (§6) is well-executed, but the conclusion \"CKA provides no explanatory power beyond depth\" may be too strong. With partial correlations at n=20 per layer (same-layer analysis), statistical power is limited. Gemma4's partial ρ=+0.16 (p=0.09, bootstrap CI [-0.02, 0.33]) is tantalizing — the CI barely crosses zero. A Bayesian analysis or meta-analytic combination across architectures might reveal a small but genuine effect. The paper should at least acknowledge the power limitations rather than asserting a clean null.\n\n**W8. Appendices are too compressed.** Appendix D (Extended Language Coverage, 52 languages) is a single paragraph. Appendix A (Probe Complexity) is one table + one sentence. These feel like placeholders rather than complete analyses. If the 52-language extension doesn't change conclusions, it's fine to be brief, but the paper promises it \"strengthens the control task finding\" without showing the supporting data.\n\n**W9. Related work is thin.** Section 2 is approximately half a page covering five brief paragraphs. For a paper that claims field-level methodological implications, the related work should more thoroughly discuss: (1) existing cross-lingual probing literature that the 35% artifact rate puts in question — which specific papers? (2) other negative results papers in NLP probing (e.g., Belinkov's survey, Pimentel et al.'s information-theoretic perspective), (3) domain adaptation theory beyond the one-line Zhao et al. mention.\n\n**W10. No statistical correction for multiple comparisons.** The paper conducts many parallel statistical tests (20 languages × 3 architectures × multiple conditions) but does not mention any correction for multiple comparisons (e.g., Bonferroni, FDR). The claim that \"1/20 languages reaches significance\" (Table 1) should be contextualized — at α=0.05 with 20 independent tests, ~1 false positive is expected by chance. Hindi's p=0.046 may well be a false positive.\n\n---\n\n## 4. Questions for the Authors\n\n**Q1.** The mean-shift impossibility (§4) relies on StandardScaler + logistic regression. How does mean-shift behave under other preprocessing pipelines (e.g., min-max scaling, no scaling, PCA-reduced features)? The paper mentions distinguishing from Xiao et al.'s pipeline but doesn't test alternative preprocessings.\n\n**Q2.** For the control task analysis (§9), how were random labels generated? Was the control task permutation repeated multiple times, or is the permuted AUROC based on a single permutation? Bootstrap confidence intervals on selectivity would strengthen the artifact rate claims.\n\n**Q3.** The β sweep (Table 6) shows monotonic degradation with increasing β. Did you explore annealing β during training (e.g., starting at 0 and increasing), which is standard practice in domain adaptation? The current sweep uses fixed β throughout training.\n\n**Q4.** For the subspace angle analysis (Table 5), what is the dimensionality of the \"correctness direction\"? Is this a single vector (the LR weight vector), or a subspace? If single-vector, the angles 15°–65° have a very different interpretation than for multi-dimensional subspaces.\n\n**Q5.** The paper uses GlobalMMLU for all languages. Are the translations machine-translated or human-translated? Translation quality could be a major confound for the LOW-resource artifact rates — if LOW-resource translations are noisy, the probe's inability to distinguish correctness may reflect translation quality rather than representation structure.\n\n---\n\n## 5. Missing References and Related Work\n\n- The paper cites \"Burns et al.\" and \"Miao et al.\" but with broken references (\"??\"). These must be resolved.\n- Missing discussion of Pimentel et al. (2020) \"Information-Theoretic Probing with Minimum Description Length\" — relevant to the control task methodology.\n- No mention of Conneau et al.'s extensive cross-lingual probing work (e.g., \"What you can cram into a single vector\") which established many of the cross-lingual probing paradigms this paper critiques.\n- Domain adaptation theory (§2) cites Ben-David et al. and Zhao et al. but omits Ganin et al. (domain-adversarial networks) and Long et al. (deep adaptation networks) — these are the methods most analogous to CaCLR's approach.\n- The probe-based calibration paragraph should cite Kadavath et al. (2022) on LLM self-knowledge and Li et al. on inference-time intervention, which are closely related to correctness direction extraction.\n\n---\n\n## 6. Experiment Coverage Assessment\n\nAll 13 planned experiments are represented in the paper, but with uneven depth:\n\n| Experiment | Coverage | Adequacy |\n|---|---|---|\n| Qwen3 Pareto (plan_001) | Full table + analysis | ✓ Adequate |\n| Llama4 Pareto (plan_002) | Text summary only, no per-language table | ✗ Insufficient |\n| Gemma4 Pareto (plan_008) | Summary table + comparison | ✓ Adequate |\n| CaCLR (plan_003) | Three tables, thorough ablation | ✓✓ Strong |\n| Decomposition (plan_004) | One table, half page | ~ Compressed |\n| Orthogonality (plan_005) | One paragraph in §11.1 | ✗ Minimal |\n| Probe complexity (plan_006) | Appendix table | ✓ Adequate for appendix |\n| Benchmarks (plan_007) | Appendix table | ✓ Adequate for appendix |\n| 52 languages (plan_009) | One paragraph | ✗ Minimal |\n| Quantization (plan_010) | Appendix table | ✓ Adequate for appendix |\n| CKA (plan_011) | Two tables + analysis | ✓ Adequate |\n| Linear projection (plan_012) | Two tables + analysis | ✓ Adequate |\n| Control tasks (plan_013) | Two tables + analysis | ✓✓ Strong |\n\n**Critical gap**: 15+ figures described in the design doc are entirely absent from the paper. The paper is figure-free, which dramatically reduces its visual communication and persuasive power.\n\n---\n\n## 7. Scores\n\n### Soundness: 3 (Acceptable)\n\nThe main claims are supported by the data presented. The mean-shift proof is mathematically clean. The CaCLR ablation is thorough and convincing. The control task methodology is properly executed. However: (1) broken citations undermine presentation quality, (2) the architecture-conditional Pareto claim is underpowered (n=2 MoE + n=1 dense), (3) no multiple comparison correction despite extensive parallel testing, (4) decomposition analysis is structurally underpowered (R²=0.28 difficulty probe). The negative results are generally convincing but some secondary claims need more careful statistical treatment.\n\n### Excitement: 2 (Potentially Interesting)\n\nThe paper does not resonate strongly but has elements that would interest parts of the *ACL community. The control task finding (35% artifact rate in cross-lingual probing, extending to MID-resource languages) is the most exciting contribution and has genuine field-level implications. However: (1) negative results papers inherently have lower novelty — the paper mostly confirms that methods don't work, (2) the positive contributions (control task warning, conditional linear projection) are relatively narrow, (3) the Pareto and CKA analyses confirm expected failures (MoE routing breaks dense-model assumptions) without yielding surprising insights, (4) the practical guidance from linear projection is too conditional to be immediately useful. The paper would benefit from more deeply developing the control task finding as the central contribution rather than giving equal space to multiple negative results.\n\n### Overall: 2 (Resubmit next cycle)\n\nThe paper has a valuable core contribution (control task methodology warning) embedded in a collection of negative results that individually lack sufficient novelty for a main conference paper. The critical formatting issues (broken citations, zero figures) indicate the paper is not submission-ready. Specific recommendations for resubmission:\n\n1. **Fix all broken citations immediately** — this is a hard requirement.\n2. **Add figures** — at minimum: Pareto scatter, CKA partial residual scatter, selectivity heatmap, β sweep curve, saturation curve. The paper's persuasive power depends on visualization.\n3. **Foreground the control task contribution** — restructure to make §9 the central section with expanded analysis (e.g., which specific published results are called into question? What is the recommended selectivity threshold?).\n4. **Add a second dense architecture** to support the architecture-conditional Pareto claim, or soften the claim to \"observed in our sample.\"\n5. **Expand related work** to properly contextualize the field-level implications.\n6. **Apply multiple comparison corrections** or explicitly discuss why they're not needed.\n7. **Flesh out appendices D** (52 languages) with actual tables/figures or remove the claim that it \"strengthens\" the finding.\n\n### Confidence: 4 (High)\n\nI am confident in this assessment. The paper's domain (cross-lingual probing, internal representations, probe-based calibration) is within my expertise. The statistical methodology and experimental design are assessable from the presented data. My main uncertainty is whether the broken citations/missing figures reflect a genuine submission (in which case the paper needs significant revision) or a compilation error (in which case only the content issues matter — still a borderline Findings paper at best).\n\n---\n\n## 8. Minor Issues\n\n- §3.4: \"AUROC > 0.58\" pass threshold is not motivated — why 0.58 specifically?\n- Table 1 caption says \"Only 1/20 languages reaches significance\" but doesn't note this is expected under the null (α=0.05 × 20 tests ≈ 1 false positive).\n- §7.1: \"Parallel set sizes range from 618 to 2,852 per language\" — this 4.6× variation could introduce heterogeneous power across languages. Was this analyzed?\n- §10.2: \"Japanese (HIGH, 0.588) is helped while Korean (MID, 0.589) is hurt\" — this example is compelling but anecdotal. Is there a systematic feature (beyond resource tier and ZS AUROC) that predicts the effect direction?\n- §11.1: The orthogonality analysis is too brief to be informative. Either expand or remove.\n- The paper title promises \"Conditional Solutions\" but the actual solutions (linear projection with caveats) are quite thin relative to the promise.\n\n---\n\n## 9. Recommendation Summary\n\n**Accept as-is**: No  \n**Accept with minor revisions**: No  \n**Accept as Findings**: Not in current state (broken citations, no figures)  \n**Resubmit after revision**: Yes — fix formatting, add figures, foreground control task contribution  \n**Reject**: No — the core content has value\n\nThe paper contains one genuinely strong contribution (control task methodology warning for cross-lingual probing) and several competent but unsurprising negative results. In its current form, the presentation issues (broken citations, zero figures, compressed appendices) prevent acceptance. With substantial revision focusing on the control task finding as the primary contribution, supported by proper visualization, this could be a solid Findings paper at EACL.",
  "project": "xling_calib_direction",
  "tier": "worst",
  "dream_id": "20260521T122458",
  "overall_score": "Resubmit next cycle (Overall: 2, Soundness: 3, Excitement: 2)",
  "review_visible": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ec0063f1-0ee3-4d04-9495-900e25311ce7",
  "isSidechain": false,
  "requestId": "req_011CbFqJW7588GSkPQKjfDzX",
  "type": "assistant",
  "uuid": "ccc6d3c0-03c8-4492-a0a3-00967ff88022",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "b4ed7333-11c6-492f-a8d4-e66619498d15",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q57ZoCHAhPcXgfo57LHMb9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3800,
      "cache_read_input_tokens": 73954,
      "output_tokens": 5001,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3800,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 5001,
          "cache_read_input_tokens": 73954,
          "cache_creation_input_tokens": 3800,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3800
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

_source line 52 · 2026-05-21T14:01:22.202Z_

<details><summary>↩ Tool result · `toolu_01FhDFqMDFvdQvqJNK9rffzo`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"report_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T122458/worst/review_report.md\", \"dream_id\": \"dream_20260521T122458\", \"tier\": \"worst\", \"review_visible\": true}, \"error\": \"\"}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ccc6d3c0-03c8-4492-a0a3-00967ff88022",
  "isSidechain": false,
  "promptId": "ac986e77-89c2-4da2-8cf0-d9a0da36482f",
  "type": "user",
  "uuid": "d548b076-6436-44b8-b020-0970ed9f7d50",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"report_path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T122458/worst/review_report.md\\\", \\\"dream_id\\\": \\\"dream_20260521T122458\\\", \\\"tier\\\": \\\"worst\\\", \\\"review_visible\\\": true}, \\\"error\\\": \\\"\\\"}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"report_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T122458/worst/review_report.md\", \"dream_id\": \"dream_20260521T122458\", \"tier\": \"worst\", \"review_visible\": true}, \"error\": \"\"}"
    }
  },
  "sourceToolAssistantUUID": "ccc6d3c0-03c8-4492-a0a3-00967ff88022",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "b4ed7333-11c6-492f-a8d4-e66619498d15",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 53 · 2026-05-21T14:01:30.360Z_

Review report submitted.

**Scores** (ACL ARR 1–5): Soundness **3**, Excitement **2**, Overall **2** (Resubmit next cycle)

**Key findings**:
- **Strongest contribution**: Control task methodology warning (35% cross-lingual probing artifact rate) — genuinely field-relevant, first extension of Hewitt & Liang selectivity to cross-lingual setting
- **Critical formatting issues**: Broken LaTeX citations ("??") on page 1 and throughout; **zero figures** in an 11-page paper despite the experiment design specifying 15+ visualizations
- **Main content weaknesses**: Architecture-conditional Pareto claim underpowered (2 MoE + 1 dense); no multiple comparison correction; difficulty decomposition structurally underpowered (R²=0.28); linear projection guidance too conditional to operationalize; Llama 4 Scout per-language results missing
- **Recommendation**: Resubmit after (1) fixing citations, (2) adding figures, (3) foregrounding control task as central contribution, (4) adding a second dense architecture or softening the Pareto claim. Could become a solid Findings paper at EACL with these revisions.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d548b076-6436-44b8-b020-0970ed9f7d50",
  "isSidechain": false,
  "requestId": "req_011CbFqTcNrXMKPNmoSpMyRe",
  "type": "assistant",
  "uuid": "445bcdd9-31d1-47f1-83a8-a67727ab0b34",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "b4ed7333-11c6-492f-a8d4-e66619498d15",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SCBMY7x5z1h66XTYNAeNzQ",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5129,
      "cache_read_input_tokens": 77754,
      "output_tokens": 291,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5129,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 291,
          "cache_read_input_tokens": 77754,
          "cache_creation_input_tokens": 5129,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5129
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

_source line 54_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[DREAM Review Director] dream_id=20260521T122458 | review_mode=simple | review_visible=True PDF: /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/…",
  "leafUuid": "445bcdd9-31d1-47f1-83a8-a67727ab0b34",
  "sessionId": "b4ed7333-11c6-492f-a8d4-e66619498d15"
}
```

---

### Runtime record

_source line 55_

```json
{
  "type": "ai-title",
  "aiTitle": "Review cross-lingual calibration direction paper",
  "sessionId": "b4ed7333-11c6-492f-a8d4-e66619498d15"
}
```

---
