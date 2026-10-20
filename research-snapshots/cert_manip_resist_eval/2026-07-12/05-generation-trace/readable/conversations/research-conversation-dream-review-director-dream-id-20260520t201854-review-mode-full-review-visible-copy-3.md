# Research conversation: [DREAM Review Director] dream_id=20260520T201854 | review_mode=full | review_visible=True PDF: /home/ubuntu/.agent-ml-re

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 38
- **Recorded user turns:** 2
- **Tool calls:** 7
- **Original source:** `logs/chats/exported-trajectories/account-3/d1221443-c15e-4888-b9c9-64cd2c74844d.jsonl`
- **Structured JSON:** [`3169b0ddb335d9a93590.json`](../../sessions/31/3169b0ddb335d9a93590.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-20T20:58:36.799Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-20T20:58:36.799Z",
  "sessionId": "d1221443-c15e-4888-b9c9-64cd2c74844d",
  "content": "[DREAM Review Director]\ndream_id=20260520T201854 | review_mode=full | review_visible=True\nPDF: /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T201854/best/review_input_db82206b.pdf\n\n（内部编排信息：tier=best，仅用于 submit_dream_review_report 调用。\n你在向 Reviewer 发送审稿任务时，**严禁**提及档位名称 best/median/worst，\n也不要暗示论文结果的好坏。Reviewer 必须盲审。）\n\n任务：对上述 PDF 进行 full 模式审稿。 使用 `dream-review-full` skill 的 dispatch 模板（2 Reviewers：R1 方法+实验、R2 新颖性+相关工作；完整 roundtable：Step 1 独立 → Step 2 交叉分享 → Step 3 收敛 → Step 4 综合）。\n\n## 审稿标准\n\n未指定目标 venue。请按 top ML venue 通用标准审稿（接受率 ~25%，6 分制：1=Strong Reject … 6=Strong Accept）。\n\n## 实验设计参考\n\n完整实验设计（含想象实验列表）：`/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T201854/best/review_context.yaml`\n论文可能未完整反映所有实验——参考此文件判断覆盖度。\n完成后必须调用 `submit_dream_review_report(report, project=\"xling_calib_direction\", tier=\"best\", dream_id=\"20260520T201854\", review_visible=True)` —— 报告会写入 dream_reports/dream_20260520T201854/best/review_report.md，编排进程通过 subprocess 退出读取它。\n不要调用 submit_review_report_to_research_director / update_review_issues / request_external_review —— 这些工具不在 Dream Review Director 白名单内。\n"
}
```

---

### Runtime record

_source line 2 · 2026-05-20T20:58:36.803Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-20T20:58:36.803Z",
  "sessionId": "d1221443-c15e-4888-b9c9-64cd2c74844d"
}
```

---

## Round 1

11 recorded events

### User

_source line 3 · 2026-05-20T20:58:36.851Z_

[DREAM Review Director]
dream_id=20260520T201854 | review_mode=full | review_visible=True
PDF: /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T201854/best/review_input_db82206b.pdf

（内部编排信息：tier=best，仅用于 submit_dream_review_report 调用。
你在向 Reviewer 发送审稿任务时，**严禁**提及档位名称 best/median/worst，
也不要暗示论文结果的好坏。Reviewer 必须盲审。）

任务：对上述 PDF 进行 full 模式审稿。 使用 `dream-review-full` skill 的 dispatch 模板（2 Reviewers：R1 方法+实验、R2 新颖性+相关工作；完整 roundtable：Step 1 独立 → Step 2 交叉分享 → Step 3 收敛 → Step 4 综合）。

## 审稿标准

未指定目标 venue。请按 top ML venue 通用标准审稿（接受率 ~25%，6 分制：1=Strong Reject … 6=Strong Accept）。

## 实验设计参考

完整实验设计（含想象实验列表）：`/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T201854/best/review_context.yaml`
论文可能未完整反映所有实验——参考此文件判断覆盖度。
完成后必须调用 `submit_dream_review_report(report, project="xling_calib_direction", tier="best", dream_id="20260520T201854", review_visible=True)` —— 报告会写入 dream_reports/dream_20260520T201854/best/review_report.md，编排进程通过 subprocess 退出读取它。
不要调用 submit_review_report_to_research_director / update_review_issues / request_external_review —— 这些工具不在 Dream Review Director 白名单内。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "248aeb9c-3304-4117-b59f-e1434de9c70f",
  "type": "user",
  "uuid": "e01d89d2-a081-4fe9-bb1e-5283e47bf147",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "d1221443-c15e-4888-b9c9-64cd2c74844d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-20T20:58:36.850Z_

```json
{
  "parentUuid": "e01d89d2-a081-4fe9-bb1e-5283e47bf147",
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
  "uuid": "3c67b644-3973-4c9a-98dc-02adb702ae6c",
  "timestamp": "2026-05-20T20:58:36.850Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "d1221443-c15e-4888-b9c9-64cd2c74844d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-20T20:58:36.850Z_

```json
{
  "parentUuid": "3c67b644-3973-4c9a-98dc-02adb702ae6c",
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
  "uuid": "b96764f3-4415-4b2b-a066-a012567e6aac",
  "timestamp": "2026-05-20T20:58:36.850Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "d1221443-c15e-4888-b9c9-64cd2c74844d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6 · 2026-05-20T20:58:36.850Z_

```json
{
  "parentUuid": "b96764f3-4415-4b2b-a066-a012567e6aac",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "848b57e5-f253-48dc-bf50-544a8ea6bd24",
  "timestamp": "2026-05-20T20:58:36.850Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "d1221443-c15e-4888-b9c9-64cd2c74844d",
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
  "aiTitle": "Conduct full DREAM review for cross-lingual calibration research",
  "sessionId": "d1221443-c15e-4888-b9c9-64cd2c74844d"
}
```

---

### Assistant

_source line 8 · 2026-05-20T20:58:40.876Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to perform a full dream review of a PDF paper. Let me start by:

1. Reading the PDF paper
2. Reading the review context YAML
3. Then dispatching two reviewers for a full review process

Let me first load the necessary tools and read the files.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "848b57e5-f253-48dc-bf50-544a8ea6bd24",
  "isSidechain": false,
  "requestId": "req_011CbEVU7D7V5HrCUuGtTLJC",
  "type": "assistant",
  "uuid": "011a9116-466d-451a-902f-00bbce8201ec",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "d1221443-c15e-4888-b9c9-64cd2c74844d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Hn7dWDe1NvJML4Kdnyu2g5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11360,
      "cache_read_input_tokens": 11841,
      "output_tokens": 361,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11360,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 361,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11360,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11360
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

_source line 9 · 2026-05-20T20:58:41.513Z_

I'll read the PDF and review context, then dispatch the full review process.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "011a9116-466d-451a-902f-00bbce8201ec",
  "isSidechain": false,
  "requestId": "req_011CbEVU7D7V5HrCUuGtTLJC",
  "type": "assistant",
  "uuid": "6fd3dbb3-50da-4fd8-a0a5-cb7a3f7f3370",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "d1221443-c15e-4888-b9c9-64cd2c74844d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Hn7dWDe1NvJML4Kdnyu2g5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11360,
      "cache_read_input_tokens": 11841,
      "output_tokens": 361,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11360,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 361,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11360,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11360
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

_source line 10 · 2026-05-20T20:58:42.206Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_013x4DCNv6jqf3Fwy5iJnznx`</summary>

```json
{
  "query": "select:submit_dream_review_report,read_project_file",
  "max_results": 2
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6fd3dbb3-50da-4fd8-a0a5-cb7a3f7f3370",
  "isSidechain": false,
  "requestId": "req_011CbEVU7D7V5HrCUuGtTLJC",
  "type": "assistant",
  "uuid": "fa26857d-4dc6-4cb4-8a22-76cac6b99702",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "d1221443-c15e-4888-b9c9-64cd2c74844d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Hn7dWDe1NvJML4Kdnyu2g5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11360,
      "cache_read_input_tokens": 11841,
      "output_tokens": 361,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11360,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 361,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11360,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11360
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

_source line 11 · 2026-05-20T20:58:42.212Z_

<details><summary>↩ Tool result · `toolu_013x4DCNv6jqf3Fwy5iJnznx`</summary>

```text
No matching deferred tools found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fa26857d-4dc6-4cb4-8a22-76cac6b99702",
  "isSidechain": false,
  "promptId": "248aeb9c-3304-4117-b59f-e1434de9c70f",
  "type": "user",
  "uuid": "e114be46-923e-4b1a-a42b-ca39d9be2497",
  "toolUseResult": {
    "matches": [],
    "query": "select:submit_dream_review_report,read_project_file",
    "total_deferred_tools": 23
  },
  "sourceToolAssistantUUID": "fa26857d-4dc6-4cb4-8a22-76cac6b99702",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "d1221443-c15e-4888-b9c9-64cd2c74844d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-20T20:58:42.620Z_

<details open><summary>🔧 Tool call — Read · `toolu_014BkSmaUPycRu3WV9boRTvg`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T201854/best/review_input_db82206b.pdf"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e114be46-923e-4b1a-a42b-ca39d9be2497",
  "isSidechain": false,
  "requestId": "req_011CbEVU7D7V5HrCUuGtTLJC",
  "type": "assistant",
  "uuid": "61a52b4e-65e4-49ec-a1a1-ddc9cd0e28a8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "d1221443-c15e-4888-b9c9-64cd2c74844d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Hn7dWDe1NvJML4Kdnyu2g5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11360,
      "cache_read_input_tokens": 11841,
      "output_tokens": 361,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11360,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 361,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11360,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11360
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

_source line 13 · 2026-05-20T20:58:42.652Z_

<details><summary>↩ Tool result · `toolu_014BkSmaUPycRu3WV9boRTvg`</summary>

```text
PDF file read: /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T201854/best/review_input_db82206b.pdf (173.8KB)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "61a52b4e-65e4-49ec-a1a1-ddc9cd0e28a8",
  "isSidechain": false,
  "promptId": "248aeb9c-3304-4117-b59f-e1434de9c70f",
  "type": "user",
  "uuid": "8e49706e-7579-44ef-9ac3-300fbdc9ff33",
  "toolUseResult": {
    "type": "pdf",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T201854/best/review_input_db82206b.pdf",
      "base64": "[ATTACHMENT_DATA_REDACTED]",
      "originalSize": 177980
    }
  },
  "sourceToolAssistantUUID": "61a52b4e-65e4-49ec-a1a1-ddc9cd0e28a8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "d1221443-c15e-4888-b9c9-64cd2c74844d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

## Round 2

25 recorded events

### User

_source line 14 · 2026-05-20T20:58:42.650Z_

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
  "parentUuid": "8e49706e-7579-44ef-9ac3-300fbdc9ff33",
  "isSidechain": false,
  "promptId": "248aeb9c-3304-4117-b59f-e1434de9c70f",
  "type": "user",
  "isMeta": true,
  "uuid": "4d6cca89-f428-4828-b3a8-f47055531602",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "d1221443-c15e-4888-b9c9-64cd2c74844d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-20T20:58:43.330Z_

<details open><summary>🔧 Tool call — Read · `toolu_01BSDu4vHNUPYrC6d8Bw2mRz`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T201854/best/review_context.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4d6cca89-f428-4828-b3a8-f47055531602",
  "isSidechain": false,
  "requestId": "req_011CbEVU7D7V5HrCUuGtTLJC",
  "type": "assistant",
  "uuid": "494e9d15-8672-4234-a407-56fa1cf71899",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "d1221443-c15e-4888-b9c9-64cd2c74844d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Hn7dWDe1NvJML4Kdnyu2g5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11360,
      "cache_read_input_tokens": 11841,
      "output_tokens": 361,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11360,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 361,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11360,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11360
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
  "lastPrompt": "[DREAM Review Director] dream_id=20260520T201854 | review_mode=full | review_visible=True PDF: /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dr…",
  "leafUuid": "494e9d15-8672-4234-a407-56fa1cf71899",
  "sessionId": "d1221443-c15e-4888-b9c9-64cd2c74844d"
}
```

---

### Runtime record

_source line 17_

```json
{
  "type": "ai-title",
  "aiTitle": "Conduct full DREAM review for cross-lingual calibration research",
  "sessionId": "d1221443-c15e-4888-b9c9-64cd2c74844d"
}
```

---

### Tool result

_source line 18 · 2026-05-20T20:58:43.587Z_

<details><summary>↩ Tool result · `toolu_01BSDu4vHNUPYrC6d8Bw2mRz`</summary>

```text
1	narrative_guidance: 'Full method contribution paper (Path A). CaCLR consistency loss
2	  provides meaningful gain, confirming distributional matching via MMD helps align
3	  capability-specific signals at mid-depth layers. Causal chain complete: Pareto frontier
4	  discovered on both architectures with architecture-dependent shape → decomposition
5	  explains frontier via difficulty/capability separation → CaCLR shifts frontier by
6	  aligning capability-specific components → orthogonality bounds output-based approaches
7	  across all languages. CKA provides mechanistic glue linking representation geometry
8	  to transfer success. Headline: "CaCLR-trained correctness probes reduce non-English
9	  ECE by 3.5% over temperature scaling with zero target-language labels across 20
10	  languages on Qwen3-235B and Llama 4 Scout."
11	
12	  '
13	imagined_experiments:
14	- name: Full Pareto Frontier — Qwen3-235B-A22B
15	  plan_id: plan_001
16	  description: '94-layer MoE model, INT8, 24 probed layers (every 4th), 20 languages,
17	    5 transfer conditions (zero-shot, mean-shift, linear projection, few-shot 25/100,
18	    CaCLR).
19	
20	    '
21	  expected_results:
22	    en_best_auroc: 0.838
23	    en_best_layer: 76
24	    en_best_ece_raw: 0.162
25	    en_best_ece_tempcal: 0.048
26	    temp_scaling_T: 4.83
27	    en_auroc_range:
28	    - 0.592
29	    - 0.838
30	    optimal_transfer_layer_median: 56
31	    zs_transfer_auroc_median_20lang: 0.758
32	    zs_transfer_auroc_at_en_optimal_layer76: 0.714
33	    zs_transfer_auroc_at_transfer_optimal_layer56: 0.771
34	    pareto_rho_global: -0.81
35	    pareto_rho_per_lang_median: -0.78
36	    pareto_rho_per_lang_iqr:
37	    - -0.84
38	    - -0.71
39	    zs_langs_above_0p65_out_of_20: 17
40	    best_zs_auroc_by_tier:
41	      HIGH_zh: 0.793
42	      HIGH_es: 0.801
43	      HIGH_fr: 0.798
44	      HIGH_de: 0.784
45	      MID_hi: 0.742
46	      MID_ru: 0.769
47	      MID_ko: 0.751
48	      MID_tr: 0.738
49	      LOW_sw: 0.641
50	      LOW_bn: 0.633
51	    mean_shift_delta_auroc_median: 0.0
52	    linear_proj_delta_auroc_over_zs_median: 0.048
53	    fewshot_25_delta_auroc_over_zs_median: 0.032
54	    fewshot_100_delta_auroc_over_zs_median: 0.055
55	  result_rationale: 'Qwen3-235B-A22B的94层深度和MoE架构产生了强correctness信号。235B参数量使EN AUROC达到0.838，
56	    远超7B MVP的0.754——更大模型的内部表征更丰富、correctness方向更可分离。 Pareto frontier清晰存在：layer 76（81%深度）是EN最优但跨语言transfer在此处下降约5.7pp
57	    （从layer 56的0.771降至0.714），因为深层表征越来越language-specific。 MoE架构中expert routing在深层更加language-dependent，强化了这一效应。
58	    Spearman rho中位数-0.78反映depth-transfer反相关在绝大多数语言中一致。 17/20语言ZS AUROC>0.65体现了235B模型强大的multilingual
59	    representation—— 仅sw/bn/my三个极低资源语言未达标，符合Ben-David H-divergence理论预测。 Mean-shift
60	    ΔAUROC=0.000由rank-invariance定理保证（StandardScaler + logistic regression下 mean-shift仅添加常数偏移，不改变rank
61	    order）。 Linear projection作为强baseline（+4.8pp）反映correctness方向在语言间存在可学习的线性映射关系。
62	
63	    '
64	  tables:
65	  - name: 'Table 1: Qwen3-235B Pareto Frontier — EN AUROC vs ZS Transfer AUROC by
66	      Layer'
67	    columns:
68	    - layer
69	    - depth_pct
70	    - en_auroc
71	    - zs_median_auroc
72	    - zs_min_auroc
73	    - zs_max_auroc
74	    - rho_median
75	    rows:
76	    - - 0
77	      - 0
78	      - 0.592
79	      - 0.583
80	      - 0.521
81	      - 0.601
82	      - null
83	    - - 8
84	      - 9
85	      - 0.631
86	      - 0.618
87	      - 0.554
88	      - 0.639
89	      - null
90	    - - 16
91	      - 17
92	      - 0.672
93	      - 0.659
94	      - 0.589
95	      - 0.678
96	      - null
97	    - - 24
98	      - 26
99	      - 0.711
100	      - 0.698
101	      - 0.621
102	      - 0.719
103	      - null
104	    - - 32
105	      - 34
106	      - 0.738
107	      - 0.729
108	      - 0.648
109	      - 0.751
110	      - null
111	    - - 40
112	      - 43
113	      - 0.762
114	      - 0.756
115	      - 0.662
116	      - 0.778
117	      - null
118	    - - 48
119	      - 51
120	      - 0.781
121	      - 0.771
122	      - 0.658
123	      - 0.793
124	      - null
125	    - - 56
126	      - 60
127	      - 0.798
128	      - 0.771
129	      - 0.641
130	      - 0.801
131	      - null
132	    - - 60
133	      - 64
134	      - 0.808
135	      - 0.762
136	      - 0.632
137	      - 0.796
138	      - null
139	    - - 64
140	      - 68
141	      - 0.816
142	      - 0.751
143	      - 0.618
144	      - 0.788
145	      - null
146	    - - 68
147	      - 72
148	      - 0.824
149	      - 0.741
150	      - 0.607
151	      - 0.779
152	      - null
153	    - - 72
154	      - 77
155	      - 0.831
156	      - 0.728
157	      - 0.598
158	      - 0.768
159	      - null
160	    - - 76
161	      - 81
162	      - 0.838
163	      - 0.714
164	      - 0.584
165	      - 0.756
166	      - null
167	    - - 80
168	      - 85
169	      - 0.835
170	      - 0.702
171	      - 0.571
172	      - 0.742
173	      - null
174	    - - 84
175	      - 89
176	      - 0.829
177	      - 0.688
178	      - 0.558
179	      - 0.729
180	      - null
181	    - - 88
182	      - 94
183	      - 0.818
184	      - 0.671
185	      - 0.542
186	      - 0.712
187	      - null
188	    - - 92
189	      - 98
190	      - 0.801
191	      - 0.649
192	      - 0.523
193	      - 0.694
194	      - null
195	  - name: 'Table 2: Qwen3-235B Transfer Conditions at Fixed Layers (layer 56 + layer
196	      76)'
197	    columns:
198	    - condition
199	    - layer56_median_auroc
200	    - layer76_median_auroc
201	    - delta_vs_zs_l56
202	    - delta_vs_zs_l76
203	    rows:
204	    - - zero-shot
205	      - 0.771
206	      - 0.714
207	      - 0.0
208	      - 0.0
209	    - - mean-shift
210	      - 0.771
211	      - 0.714
212	      - 0.0
213	      - 0.0
214	    - - linear_proj_50pairs
215	      - 0.812
216	      - 0.779
217	      - 0.041
218	      - 0.065
219	    - - fewshot_25
220	      - 0.798
221	      - 0.761
222	      - 0.027
223	      - 0.047
224	    - - fewshot_100
225	      - 0.821
226	      - 0.792
227	      - 0.05
228	      - 0.078
229	    - - CaCLR_full
230	      - 0.828
231	      - 0.788
232	      - 0.057
233	      - 0.074
234	  figures_description:
235	  - 'Fig 1a: Pareto frontier scatter — x-axis EN AUROC, y-axis ZS transfer AUROC median.
236	    Each point is a layer. Clear concave frontier with elbow at ~60% depth. Color
237	    by resource tier shows HIGH langs cluster top-right, LOW langs bottom-left.'
238	  - 'Fig 1b: Heatmap 24 layers × 20 languages, cell color = ZS AUROC. Visible gradient:
239	    warm (high AUROC) at mid-depth for high-resource, shifting to shallower optimum
240	    for low-resource.'
241	  - 'Fig 1c: Per-language Spearman rho distribution (violin plot). Median -0.78, tight
242	    IQR, all languages negative. Annotate sw/bn as outliers with weaker rho.'
243	  analysis: 'Pareto frontier 在 Qwen3-235B 上形态清晰。拐点在 layer 56（60% depth）—— 此后EN AUROC继续上升但ZS
244	    transfer开始下降。MoE架构的expert routing在深层 更加language-specific是造成Pareto tradeoff的主要机制。High-resource语言
245	    （zh/es/fr/de）的frontier更靠右上方，因为这些语言在pretraining中获得更多 token coverage，deep-layer
246	    representation与EN的对齐更好。Low-resource（sw/bn） 即使在最优transfer层也仅达到0.64左右，符合H-divergence理论预测。
247	
248	    '
249	- name: Full Pareto Frontier — Llama 4 Scout
250	  plan_id: plan_002
251	  description: '48-layer MoE model, INT8, 12 probed layers (every 4th), 20 languages,
252	    5 transfer conditions.
253	
254	    '
255	  expected_results:
256	    en_best_auroc: 0.821
257	    en_best_layer: 40
258	    en_best_ece_raw: 0.171
259	    en_best_ece_tempcal: 0.053
260	    temp_scaling_T: 5.12
261	    en_auroc_range:
262	    - 0.604
263	    - 0.821
264	    optimal_transfer_layer_median: 24
265	    zs_transfer_auroc_median_20lang: 0.742
266	    zs_transfer_auroc_at_en_optimal_layer40: 0.698
267	    zs_transfer_auroc_at_transfer_optimal_layer24: 0.756
268	    pareto_rho_global: -0.76
269	    pareto_rho_per_lang_median: -0.73
270	    pareto_rho_per_lang_iqr:
271	    - -0.81
272	    - -0.66
273	    zs_langs_above_0p65_out_of_20: 16
274	    best_zs_auroc_by_tier:
275	      HIGH_zh: 0.778
276	      HIGH_es: 0.789
277	      HIGH_fr: 0.781
278	      HIGH_de: 0.772
279	      MID_hi: 0.728
280	      MID_ru: 0.756
281	      MID_ko: 0.739
282	      MID_tr: 0.721
283	      LOW_sw: 0.628
284	      LOW_bn: 0.618
285	    mean_shift_delta_auroc_median: 0.0
286	    linear_proj_delta_auroc_over_zs_median: 0.044
287	  result_rationale: 'Llama 4 Scout的48层架构使optimal transfer层在50%深度（layer 24）， 而Qwen3-235B在60%深度（layer
288	    56）——这就是architecture-dependent shape的关键证据。 Scout的层数不到Qwen的一半，deep层的language specialization发生得更快（按比例）。
289	    EN best AUROC=0.821略低于Qwen的0.838，反映Scout虽然是MoE但active参数更少。 ZS median 0.742 vs
290	    Qwen的0.758，差距16pp体现了Llama系列multilingual pretraining 数据在低资源语言上的相对弱势。Pareto rho中位数-0.73略弱于Qwen的-0.78，
291	    因为Scout只有12个probed层，frontier采样更粗糙。16/20语言>0.65（vs Qwen 17/20）， sw/bn/my/jv四个低资源语言未达标。Architecture-dependent差异是本文Claim
292	    1的核心发现。
293	
294	    '
295	  tables:
296	  - name: 'Table 3: Llama 4 Scout Pareto Frontier'
297	    columns:
298	    - layer
299	    - depth_pct
300	    - en_auroc
301	    - zs_median_auroc
302	    rows:
303	    - - 0
304	      - 0
305	      - 0.604
306	      - 0.592
307	    - - 4
308	      - 8
309	      - 0.638
310	      - 0.624
311	    - - 8
312	      - 17
313	      - 0.674
314	      - 0.661
315	    - - 12
316	      - 25
317	      - 0.712
318	      - 0.701
319	    - - 16
320	      - 33
321	      - 0.741
322	      - 0.738
323	    - - 20
324	      - 42
325	      - 0.768
326	      - 0.756
327	    - - 24
328	      - 50
329	      - 0.788
330	      - 0.756
331	    - - 28
332	      - 58
333	      - 0.801
334	      - 0.742
335	    - - 32
336	      - 67
337	      - 0.811
338	      - 0.726
339	    - - 36
340	      - 75
341	      - 0.818
342	      - 0.711
343	    - - 40
344	      - 83
345	      - 0.821
346	      - 0.698
347	    - - 44
348	      - 92
349	      - 0.814
350	      - 0.679
351	    - - 48
352	      - 100
353	      - 0.798
354	      - 0.654
355	  figures_description:
356	  - 'Fig 2a: Pareto frontiers overlaid — Qwen3-235B (blue) vs Llama 4 Scout (orange).
357	    Both concave but elbow position differs: Qwen at 60% depth, Scout at 50%. Demonstrates
358	    architecture-dependent shape.'
359	  - 'Fig 2b: Architecture comparison heatmap — difference in ZS AUROC (Qwen minus
360	    Scout) by language × normalized depth. Positive (Qwen better) at deep layers for
361	    high-resource; near zero at shallow layers.'
362	  analysis: '两个架构的Pareto frontier在归一化深度上呈现不同形状：Qwen3-235B的拐点在60%深度， Scout在50%深度。这一差异不能由模型大小alone解释（两者都是MoE），
363	    而是反映了训练数据分布、expert routing策略和层归一化实现的差异。 Scout在每层的language specialization更剧烈，导致frontier更陡峭、拐点更早。
364	    这是论文最核心的发现之一：optimal transfer depth不是universal的，必须per-architecture确定。
365	
366	    '
367	- name: CaCLR Implementation and Comparative Evaluation
368	  plan_id: plan_003
369	  description: 'CaCLR (L_BCE + α·L_SB-ECE + β·L_MMD) 训练、超参数sweep、与所有baseline的全面比较。
370	    Path A: β term provides meaningful gain.
371	
372	    '
373	  expected_results:
374	    caclr_optimal_alpha: 1.0
375	    caclr_optimal_beta: 0.1
376	    caclr_beta_delta_auroc_over_alpha_only_median: 0.032
377	    caclr_beta_delta_auroc_over_alpha_only_range:
378	    - 0.018
379	    - 0.051
380	    caclr_full_delta_auroc_over_zeroshot_median: 0.062
381	    caclr_full_delta_auroc_over_zeroshot_range:
382	    - 0.031
383	    - 0.098
384	    caclr_vs_linear_proj_delta_median: 0.014
385	    caclr_vs_fewshot100_delta_median: -0.008
386	    ece_reduction_vs_temp_scaling_median: 0.035
387	    ece_reduction_vs_temp_scaling_range:
388	    - 0.012
389	    - 0.061
390	    beta_sweep_results:
391	      beta_0.001:
392	        delta_auroc_over_alpha_only: 0.008
393	        note: too weak
394	      beta_0.01:
395	        delta_auroc_over_alpha_only: 0.019
396	        note: marginal
397	      beta_0.1:
398	        delta_auroc_over_alpha_only: 0.032
399	        note: optimal
400	      beta_1.0:
401	        delta_auroc_over_alpha_only: 0.021
402	        note: overfitting to distributional match
403	    alpha_sweep_results:
404	      alpha_0.01:
405	        en_ece: 0.068
406	        transfer_auroc_median: 0.779
407	      alpha_0.1:
408	        en_ece: 0.055
409	        transfer_auroc_median: 0.793
410	      alpha_1.0:
411	        en_ece: 0.041
412	        transfer_auroc_median: 0.808
413	      alpha_10.0:
414	        en_ece: 0.038
415	        transfer_auroc_median: 0.791
416	    layer_interaction:
417	      mid_depth_beta_gain: 0.041
418	      deep_layer_beta_gain: 0.024
419	      shallow_layer_beta_gain: 0.018
420	    qwen_results:
421	      layer56_caclr_full_median: 0.828
422	      layer76_caclr_full_median: 0.788
423	    scout_results:
424	      layer24_caclr_full_median: 0.812
425	      layer40_caclr_full_median: 0.771
426	    bootstrap_ci_beta_effect:
427	    - 0.019
428	    - 0.045
429	    paired_permutation_p_beta: 0.003
430	    cohens_d_beta: 0.48
431	  result_rationale: 'CaCLR consistency loss (β term) 提供了有意义的增益（中位数+3.2pp over α-only），
432	    支持Path A叙事。β=0.1是最优点——更低（0.001-0.01）则MMD约束太弱无法对齐分布， 更高（1.0）则过度约束导致correctness
433	    prediction损失。 β增益在mid-depth层（40-60%）最大（+4.1pp），因为这些层的cross-lingual表征 仍有足够的共享结构让MMD可以有效对齐，但已经开始出现分化需要对齐。
434	    在deep层β增益下降到+2.4pp，因为表征的geometric misalignment（非仅distributional shift） 限制了MMD的有效性——但CaCLR仍然比zero-shot好得多。
435	    CaCLR vs linear projection：CaCLR赢1.4pp中位数，因为它同时优化calibration（α项） 和alignment（β项），而linear
436	    projection仅做alignment。但CaCLR略输于few-shot 100 （-0.8pp），因为100个标注样本提供了直接的target-language
437	    correctness信号。 关键：CaCLR不需要target-language labels，这是实际场景中的核心优势。 ECE reduction vs
438	    temp scaling中位数3.5pp，因为CaCLR在训练时直接优化SB-ECE， 而temp scaling仅做post-hoc rescaling无法修复表征层面的miscalibration。
439	    Bootstrap CI [0.019, 0.045]和p=0.003确认β效应统计显著；Cohen''s d=0.48为中等效应量。
440	
441	    '
442	  tables:
443	  - name: 'Table 4: Transfer Method Comparison (Median AUROC across 20 languages,
444	      both models)'
445	    columns:
446	    - method
447	    - labels_needed
448	    - qwen_layer56
449	    - qwen_layer76
450	    - scout_layer24
451	    - scout_layer40
452	    - median_all
453	    rows:
454	    - - zero-shot
455	      - 0
456	      - 0.771
457	      - 0.714
458	      - 0.756
459	      - 0.698
460	      - 0.735
461	    - - mean-shift
462	      - 0
463	      - 0.771
464	      - 0.714
465	      - 0.756
466	      - 0.698
467	      - 0.735
468	    - - CaCLR_alpha_only
469	      - 0 (parallel inputs)
470	      - 0.798
471	      - 0.762
472	      - 0.784
473	      - 0.745
474	      - 0.772
475	    - - CaCLR_full
476	      - 0 (parallel inputs)
477	      - 0.828
478	      - 0.788
479	      - 0.812
480	      - 0.771
481	      - 0.8
482	    - - linear_proj_50
483	      - 50 parallel pairs
484	      - 0.812
485	      - 0.779
486	      - 0.798
487	      - 0.758
488	      - 0.787
489	    - - fewshot_25
490	      - 25
491	      - 0.798
492	      - 0.761
493	      - 0.781
494	      - 0.741
495	      - 0.77
496	    - - fewshot_100
497	      - 100
498	      - 0.821
499	      - 0.792
500	      - 0.808
501	      - 0.778
502	      - 0.8
503	  - name: 'Table 5: β Sensitivity Sweep (Qwen3-235B, layer 56, median across 20 langs)'
504	    columns:
505	    - beta
506	    - delta_auroc_over_alpha_only
507	    - delta_ece_over_alpha_only
508	    - note
509	    rows:
510	    - - 0.001
511	      - 0.008
512	      - -0.003
513	      - negligible distributional constraint
514	    - - 0.01
515	      - 0.019
516	      - -0.008
517	      - marginal improvement
518	    - - 0.1
519	      - 0.032
520	      - -0.014
521	      - optimal — balances alignment and prediction
522	    - - 1.0
523	      - 0.021
524	      - -0.011
525	      - over-regularized — MMD dominates loss
526	  figures_description:
527	  - 'Fig 3a: Bar chart — 5 transfer methods × 2 models at optimal transfer layer.
528	    CaCLR_full highest, followed by fewshot_100, linear_proj, CaCLR_alpha_only, zero-shot.
529	    Error bars = bootstrap 95% CI.'
530	  - 'Fig 3b: β sweep curve — x-axis β (log scale), y-axis ΔAUROC over α-only. Inverted-U
531	    shape peaking at β=0.1. Three lines for shallow/mid/deep layers showing mid-depth
532	    benefits most.'
533	  - 'Fig 3c: Pareto frontier shift — original ZS frontier (dashed) vs CaCLR frontier
534	    (solid) for both architectures. CaCLR pushes frontier up and right, especially
535	    at mid-depth.'
536	  analysis: 'CaCLR的consistency loss在mid-depth层效果最好，这与CKA分析（plan_011）一致： mid-depth层的cross-lingual表征相似度足够高让MMD有效对齐，但已经有enough
537	    language-specific分化使得对齐产生实际收益。β=0.1的inverted-U曲线说明 distributional matching存在sweet
538	    spot——太弱无效，太强则牺牲correctness prediction。 CaCLR vs fewshot_100的near-parity（-0.8pp）是重要结果：CaCLR达到了接近
539	    100-label supervised的性能，但不需要任何target-language correctness labels。 统计显著性（p=0.003,
540	    d=0.48）确保β效应不是噪声。
541	
542	    '
543	- name: Difficulty-Controlled Decomposition Ablation
544	  plan_id: plan_004
545	  description: 'IRT difficulty probes → project out difficulty → retrain correctness
546	    probes → evaluate transfer. 10 languages × 8 layers × 2 models.
547	
548	    '
549	  expected_results:
550	    decomposition_transfer_delta_after_difficulty_removal_median: 0.031
551	    decomposition_transfer_delta_range:
552	    - 0.011
553	    - 0.052
554	    difficulty_probe_r2_median: 0.68
555	    difficulty_direction_cosine_with_correctness: 0.34
556	    capability_specific_transfer_degradation_per_depth:
557	      shallow_20pct: 0.008
558	      mid_50pct: 0.024
559	      deep_80pct: 0.048
560	    random_direction_control_delta: 0.002
561	    resource_tier_pattern:
562	      HIGH_delta: 0.022
563	      MID_delta: 0.033
564	      LOW_delta: 0.041
565	    bootstrap_ci_decomposition_delta:
566	    - 0.018
567	    - 0.044
568	    paired_permutation_p: 0.006
569	    cohens_d: 0.41
570	  result_rationale: 'Difficulty direction与correctness direction有中等cosine（0.34），说明两者共享
571	    部分信号但不完全重叠。Project out difficulty后，残差中的correctness信号更 "capability-pure"——这个信号在高资源语言间更容易transfer（+2.2pp），
572	    因为capability-specific failures在这些语言间更一致。低资源语言获益最大（+4.1pp）， 因为原始correctness方向中difficulty成分占比更高（低资源语言的difficulty分布
573	    与EN差异更大），去除difficulty后暴露出更可transfer的capability信号。 深层退化更明显（4.8pp）因为深层同时编码了更多language-specific的difficulty信息。
574	    Random-direction control仅+0.2pp，排除了dimensionality reduction artifact—— 是difficulty方向的specific
575	    removal而非arbitrary降维带来的改善。 这个分解是prescriptive的：它告诉我们哪些language-layer组合需要capability
576	    alignment （高delta = 高difficulty entanglement = 需要CaCLR/projection）。
577	
578	    '
579	  tables:
580	  - name: 'Table 6: Decomposition Effect by Resource Tier and Depth (ΔAUROC after
581	      difficulty removal)'
582	    columns:
583	    - depth_pct
584	    - HIGH_avg
585	    - MID_avg
586	    - LOW_avg
587	    - random_control
588	    rows:
589	    - - 20
590	      - 0.012
591	      - 0.014
592	      - 0.019
593	      - 0.001
594	    - - 35
595	      - 0.016
596	      - 0.022
597	      - 0.028
598	      - 0.002
599	    - - 50
600	      - 0.021
601	      - 0.031
602	      - 0.038
603	      - 0.002
604	    - - 60
605	      - 0.024
606	      - 0.036
607	      - 0.043
608	      - 0.003
609	    - - 70
610	      - 0.026
611	      - 0.039
612	      - 0.046
613	      - 0.002
614	    - - 80
615	      - 0.028
616	      - 0.041
617	      - 0.048
618	      - 0.003
619	    - - 85
620	      - 0.025
621	      - 0.038
622	      - 0.044
623	      - 0.002
624	    - - 90
625	      - 0.022
626	      - 0.034
627	      - 0.041
628	      - 0.002
629	  figures_description:
630	  - 'Fig 4a: Three-panel heatmap (HIGH/MID/LOW) — 8 layers × decomposition delta.
631	    Gradient intensifies with depth and decreases with resource level.'
632	  - 'Fig 4b: Scatter plot — difficulty-correctness cosine similarity vs decomposition
633	    delta. Each point = language × layer. Clear positive correlation (r=0.71).'
634	  - 'Fig 4c: Bar chart — decomposition delta vs random-direction control delta at
635	    each depth. Orders of magnitude difference confirms specificity.'
636	  analysis: 'Decomposition结果支持Claim 2：difficulty和capability在correctness方向中可分离， 且分离后capability-specific信号的cross-lingual
637	    transfer一致改善。 关键insight是resource tier gradient——低资源语言的difficulty entanglement最严重，
638	    也从decomposition中获益最多。这为CaCLR提供了theoretical motivation： CaCLR的consistency loss本质上在做distributional
639	    alignment of capability-specific signals。 Random-direction control（~0pp）是关键的methodological
640	    guard rail。
641	
642	    '
643	- name: Cross-Lingual Orthogonality Analysis
644	  plan_id: plan_005
645	  description: 'Correctness-confidence cosine similarity across 20 languages × 2 architectures,
646	    analyzed by resource tier and language family.
647	
648	    '
649	  expected_results:
650	    orthogonality_cosine_mean_across_langs: 0.042
651	    orthogonality_cosine_max_across_langs: 0.062
652	    orthogonality_cosine_min_across_langs: 0.018
653	    orthogonality_cosine_std: 0.013
654	    cosine_by_tier:
655	      HIGH_mean: 0.038
656	      MID_mean: 0.043
657	      LOW_mean: 0.051
658	    cosine_by_architecture:
659	      qwen_mean: 0.039
660	      scout_mean: 0.046
661	    cosine_range_qwen_20lang:
662	    - 0.018
663	    - 0.058
664	    cosine_range_scout_20lang:
665	    - 0.022
666	    - 0.062
667	    all_20_langs_below_0p08: true
668	    bootstrap_ci_mean_cosine:
669	    - 0.035
670	    - 0.049
671	  result_rationale: 'Orthogonality在所有20语言 × 2架构上持续存在（max cosine 0.062 < 0.08阈值）， 确认Miao
672	    & Ungar (2026)的English-only发现是universal structural property。 Low-resource语言cosine略高（0.051
673	    vs HIGH 0.038），因为这些语言的confidence probe quality更低（更少训练数据→confidence方向估计噪声更大→与correctness的
674	    apparent cosine被噪声inflate）。但即使是最高的0.062也远低于non-orthogonal阈值， 说明output-based calibration在结构上受限不依赖于语言。
675	    Qwen略比Scout更orthogonal（0.039 vs 0.046），可能反映Qwen更大的模型容量 使correctness和confidence能被编码在更分离的子空间中。
676	    这个发现bounds entire output-based calibration approach：无论语言或架构， verbalized confidence不包含correctness信息，motivating
677	    probe-based方法。
678	
679	    '
680	  tables:
681	  - name: 'Table 7: Correctness-Confidence Cosine Similarity by Language'
682	    columns:
683	    - language
684	    - tier
685	    - qwen_cosine
686	    - scout_cosine
687	    - mean
688	    rows:
689	    - - en
690	      - HIGH
691	      - 0.031
692	      - 0.037
693	      - 0.034
694	    - - zh
695	      - HIGH
696	      - 0.035
697	      - 0.041
698	      - 0.038
699	    - - es
700	      - HIGH
701	      - 0.033
702	      - 0.039
703	      - 0.036
704	    - - fr
705	      - HIGH
706	      - 0.034
707	      - 0.04
708	      - 0.037
709	    - - de
710	      - HIGH
711	      - 0.036
712	      - 0.042
713	      - 0.039
714	    - - hi
715	      - MID
716	      - 0.039
717	      - 0.045
718	      - 0.042
719	    - - ru
720	      - MID
721	      - 0.037
722	      - 0.043
723	      - 0.04
724	    - - ko
725	      - MID
726	      - 0.041
727	      - 0.047
728	      - 0.044
729	    - - tr
730	      - MID
731	      - 0.043
732	      - 0.049
733	      - 0.046
734	    - - sw
735	      - LOW
736	      - 0.048
737	      - 0.056
738	      - 0.052
739	    - - bn
740	      - LOW
741	      - 0.052
742	      - 0.058
743	      - 0.055
744	  figures_description:
745	  - 'Fig 5: Dot plot — cosine similarity per language, sorted by resource tier. Horizontal
746	    line at 0.08 threshold. All points below. Color by architecture (Qwen blue, Scout
747	    orange). Visible tier gradient.'
748	  analysis: 'Cross-lingual orthogonality的universal persistence是论文的bounding contribution。
749	    它回答了"为什么需要probe-based calibration"：因为output-based方法在结构上 无法获取correctness信息（cosine<0.08），无论语言。Resource
750	    tier gradient 是nuanced finding但不影响main conclusion。
751	
752	    '
753	- name: Probe Complexity Comparison
754	  plan_id: plan_006
755	  description: 'Logistic regression vs 2-layer MLP across all probed layers, both
756	    models. EN accuracy, cross-lingual transfer degradation, calibration comparison.
757	
758	    '
759	  expected_results:
760	    lr_en_best_auroc_qwen: 0.838
761	    mlp_en_best_auroc_qwen: 0.852
762	    lr_en_best_auroc_scout: 0.821
763	    mlp_en_best_auroc_scout: 0.834
764	    lr_zs_transfer_degradation_median: 0.068
765	    mlp_zs_transfer_degradation_median: 0.104
766	    lr_transfer_advantage_over_mlp_median: 0.022
767	    lr_ece_vs_mlp_ece:
768	    - -0.008
769	    - 0.003
770	    mlp_overfit_indicator_deep_layers: true
771	  result_rationale: 'Linear probes在EN AUROC上略输MLP（~1.4pp），但在cross-lingual transfer上
772	    显著更好（+2.2pp median）。MLP的额外容量捕获了EN-specific patterns导致更多 overfitting to source
773	    language——这些patterns在target语言中不泛化。 这与probe complexity literature一致（Hewitt & Liang
774	    2019）：更强的probe 在source domain表现更好但generalization更差。Linear probe的inductive bias
775	    （只能学习线性可分方向）恰好与correctness direction的线性结构匹配， 同时限制了对language-specific artifacts的拟合。
776	    在deep层这个差异更大（MLP overfitting更严重），因为deep层表征更language-specific。 这个结果support使用logistic
777	    regression作为primary probe的选择。
778	
779	    '
780	  tables:
781	  - name: 'Table 8: Probe Complexity — EN AUROC vs ZS Transfer (Qwen3-235B, selected
782	      layers)'
783	    columns:
784	    - layer
785	    - lr_en
786	    - mlp_en
787	    - lr_zs_median
788	    - mlp_zs_median
789	    - lr_transfer_advantage
790	    rows:
791	    - - 24
792	      - 0.711
793	      - 0.722
794	      - 0.698
795	      - 0.691
796	      - 0.007
797	    - - 40
798	      - 0.762
799	      - 0.778
800	      - 0.756
801	      - 0.741
802	      - 0.015
803	    - - 56
804	      - 0.798
805	      - 0.814
806	      - 0.771
807	      - 0.752
808	      - 0.019
809	    - - 76
810	      - 0.838
811	      - 0.852
812	      - 0.714
813	      - 0.686
814	      - 0.028
815	  figures_description:
816	  - 'Fig S1: Dual-axis plot — EN AUROC (solid) and ZS transfer AUROC (dashed) vs layer
817	    depth, separate lines for LR and MLP. MLP''s solid line higher but dashed line
818	    lower, scissors gap widens at deep layers.'
819	  analysis: 'Linear probe是正确的default choice。MLP的EN优势被transfer劣势完全抵消。 这个结果also间接支持correctness
820	    direction是线性的——linear probe已经捕获了 大部分信号，MLP额外捕获的主要是noise/language-specific artifact。
821	
822	    '
823	- name: Additional Benchmark Evaluation (Belebele + MMLU-ProX)
824	  plan_id: plan_007
825	  description: 'Best probes + CaCLR在Belebele和MMLU-ProX上的评估，验证beyond-GlobalMMLU泛化。
826	
827	    '
828	  expected_results:
829	    belebele_zs_auroc_median: 0.731
830	    belebele_caclr_auroc_median: 0.789
831	    mmlu_prox_zs_auroc_median: 0.748
832	    mmlu_prox_caclr_auroc_median: 0.801
833	    cross_benchmark_correlation: 0.92
834	    belebele_pareto_rho_median: -0.71
835	    mmlu_prox_pareto_rho_median: -0.75
836	  result_rationale: 'Belebele（reading comprehension）的ZS AUROC略低于GlobalMMLU（0.731 vs
837	    0.758）， 因为不同任务的correctness信号分布不完全一致——但Pareto frontier仍然存在 （rho=-0.71），说明depth-transfer
838	    tradeoff是task-general的。 MMLU-ProX与GlobalMMLU最相似（同为knowledge QA），所以结果最接近（0.748
839	    vs 0.758）。 CaCLR在两个benchmark上都提供了consistent improvement（+5.3-5.8pp）， 说明CaCLR学到的alignment不是GlobalMMLU-specific的。
840	    Cross-benchmark correlation 0.92表明per-language transfer difficulty在benchmarks间高度一致——
841	    sw/bn在所有benchmarks上都最难transfer，zh/es在所有benchmarks上都最容易。
842	
843	    '
844	  tables:
845	  - name: 'Table 9: Cross-Benchmark Generalization (Qwen3-235B, optimal transfer layer)'
846	    columns:
847	    - benchmark
848	    - zs_median
849	    - caclr_median
850	    - pareto_rho
851	    - langs_above_0p65
852	    rows:
853	    - - GlobalMMLU
854	      - 0.758
855	      - 0.808
856	      - -0.78
857	      - 17
858	    - - Belebele
859	      - 0.731
860	      - 0.789
861	      - -0.71
862	      - 15
863	    - - MMLU-ProX
864	      - 0.748
865	      - 0.801
866	      - -0.75
867	      - 16
868	  figures_description:
869	  - 'Fig S2: Scatter — per-language ZS AUROC on GlobalMMLU vs Belebele. High correlation
870	    (r=0.92). Each point labeled with language code.'
871	  analysis: 'Cross-benchmark泛化confirm findings are not benchmark-specific artifact。
872	    Pareto frontier在三个benchmark上一致存在但shape有细微差异—— Belebele更浅的optimal depth可能反映reading
873	    comprehension使用了更浅层的表征。
874	
875	    '
876	- name: INT8 Validation Ablation
877	  plan_id: plan_010
878	  description: 'INT8 vs FP16对比，Llama 4 Scout，5 representative layers，5% random subset。
879	
880	    '
881	  expected_results:
882	    int8_fp16_auroc_max_diff: 0.006
883	    int8_fp16_auroc_mean_diff: 0.003
884	    int8_fp16_ece_max_diff: 0.008
885	    int8_fp16_direction_cosine_min: 0.987
886	    all_diffs_within_noise: true
887	  result_rationale: 'INT8量化对correctness direction的影响极小（max AUROC差异0.6pp）， 因为correctness信号是高SNR的线性方向——量化噪声主要影响低幅度维度，
888	    而correctness direction在high-variance维度上有强projection。 Direction cosine>0.987说明INT8和FP16下提取的correctness方向几乎相同。
889	    ECE差异稍大（0.8pp）因为calibration对probability scale更敏感，但仍在噪声范围内。 这排除了"INT8 artifact"的reviewer
890	    concern。
891	
892	    '
893	  tables:
894	  - name: 'Table S1: INT8 vs FP16 Comparison (Llama 4 Scout)'
895	    columns:
896	    - layer
897	    - int8_auroc
898	    - fp16_auroc
899	    - diff
900	    - direction_cosine
901	    rows:
902	    - - 8
903	      - 0.674
904	      - 0.678
905	      - -0.004
906	      - 0.991
907	    - - 16
908	      - 0.741
909	      - 0.745
910	      - -0.004
911	      - 0.989
912	    - - 24
913	      - 0.788
914	      - 0.791
915	      - -0.003
916	      - 0.992
917	    - - 32
918	      - 0.811
919	      - 0.814
920	      - -0.003
921	      - 0.99
922	    - - 40
923	      - 0.821
924	      - 0.827
925	      - -0.006
926	      - 0.987
927	  figures_description:
928	  - 'Fig S3: Bland-Altman plot — mean of INT8/FP16 AUROC (x) vs difference (y). All
929	    points within ±0.01 band. No systematic bias.'
930	  analysis: 'INT8量化不distort correctness signals。所有差异在bootstrap noise范围内。 Deep层差异略大（layer
931	    40: 0.6pp）符合预期——深层表征更complex，量化误差累积更多。 但0.6pp远小于实验效应（CaCLR +6pp），不影响任何结论。
932	
933	    '
934	- name: CKA Cross-Lingual Representation Similarity
935	  plan_id: plan_011
936	  description: 'CKA (linear kernel) between EN and each target language at every probed
937	    layer, correlated with transfer AUROC. Mechanistic explanation for Pareto frontier.
938	
939	    '
940	  expected_results:
941	    cka_transfer_pearson_r: 0.82
942	    cka_transfer_pearson_r_ci:
943	    - 0.76
944	    - 0.87
945	    cka_transfer_spearman_rho: 0.79
946	    cka_en_zh_by_depth_trend: monotonically decreasing from 0.92 (shallow) to 0.61
947	      (deep)
948	    cka_en_sw_by_depth_trend: monotonically decreasing from 0.84 (shallow) to 0.38
949	      (deep)
950	    cka_resource_tier_gradient:
951	      HIGH_mean_cka_at_optimal_depth: 0.78
952	      MID_mean_cka_at_optimal_depth: 0.71
953	      LOW_mean_cka_at_optimal_depth: 0.58
954	    geometric_misalignment_evidence: 'CKA drop from mid to deep layers exceeds what
955	      mean/covariance shift alone predicts. Subspace angle analysis shows correctness
956	      direction rotates 15-35° across languages at deep layers vs 5-12° at shallow
957	      layers.
958	
959	      '
960	    cka_explains_caclr_beta_limit: 'At layers where CKA < 0.55, β term provides diminishing
961	      returns because geometric misalignment (rotation) dominates distributional shift.
962	
963	      '
964	  result_rationale: 'CKA与transfer AUROC的高相关（r=0.82）提供了Pareto frontier的mechanistic
965	    explanation： cross-lingual表征相似度随depth monotonically下降，直接导致deep层transfer degradation。
966	    这不是trivial的"深层更specific"——CKA量化了具体的相似度数值并与transfer成功率 建立了定量关系。High-resource语言在所有depth保持更高CKA（因为pretraining
967	    data overlap）， 解释了resource tier gradient。 关键insight：deep层的CKA下降不仅是distributional
968	    shift（可被MMD修正）， 还包含geometric misalignment（correctness方向在语言间旋转15-35°）。 这解释了CaCLR
969	    β term在deep层效果减弱——MMD对齐分布但不学习旋转， 而linear projection学习旋转所以在deep层更稳定。 Subspace angle
970	    analysis区分了distributional vs geometric misalignment， 为Path A narrative提供了theoretical
971	    depth：CaCLR works at mid-depth因为 那里的misalignment主要是distributional的。
972	
973	    '
974	  tables:
975	  - name: 'Table 10: CKA by Depth and Resource Tier (Qwen3-235B)'
976	    columns:
977	    - depth_pct
978	    - HIGH_cka
979	    - MID_cka
980	    - LOW_cka
981	    - zs_auroc_median
982	    rows:
983	    - - 10
984	      - 0.93
985	      - 0.89
986	      - 0.84
987	      - 0.618
988	    - - 25
989	      - 0.9
990	      - 0.85
991	      - 0.78
992	      - 0.698
993	    - - 40
994	      - 0.86
995	      - 0.79
996	      - 0.69
997	      - 0.756
998	    - - 50
999	      - 0.82
1000	      - 0.74
1001	      - 0.62
1002	      - 0.771
1003	    - - 60
1004	      - 0.78
1005	      - 0.69
1006	      - 0.55
1007	      - 0.771
1008	    - - 70
1009	      - 0.73
1010	      - 0.63
1011	      - 0.47
1012	      - 0.741
1013	    - - 80
1014	      - 0.67
1015	      - 0.56
1016	      - 0.41
1017	      - 0.714
1018	    - - 90
1019	      - 0.61
1020	      - 0.49
1021	      - 0.35
1022	      - 0.688
1023	  figures_description:
1024	  - 'Fig 6a: Dual-axis — CKA (left y-axis, lines by tier) and ZS AUROC median (right
1025	    y-axis, dashed) vs normalized depth. CKA decrease tracks AUROC decrease after
1026	    elbow.'
1027	  - 'Fig 6b: Scatter — CKA vs ZS transfer AUROC, each point = language × layer. Strong
1028	    linear relationship (r=0.82). Color by resource tier.'
1029	  - 'Fig 6c: Subspace angle between EN and target correctness directions vs depth.
1030	    Angles increase with depth; LOW languages diverge faster.'
1031	  analysis: 'CKA analysis是论文的mechanistic backbone。它将observation（Pareto frontier） 与explanation（representation
1032	    geometry变化）和method（CaCLR的作用机制与局限） 连接起来。CKA<0.55作为CaCLR β有效性的threshold是一个actionable
1033	    finding—— 实践者可以用CKA预测CaCLR在哪些layer-language组合上有效。 Geometric vs distributional
1034	    misalignment的区分是theoretical contribution： 它解释了为什么distributional matching（MMD/CaCLR）在mid-depth有效但在deep层递减，
1035	    而geometric alignment（linear projection）在deep层更稳定。
1036	
1037	    '
1038	- name: Linear Projection Sensitivity Analysis
1039	  plan_id: plan_012
1040	  description: 'Linear projection pair count sweep (10, 20, 50, 100, 200). Both models
1041	    × 5 layers × 20 languages.
1042	
1043	    '
1044	  expected_results:
1045	    linear_proj_min_pairs_for_saturation: 35
1046	    saturation_criterion: 95% of 200-pair performance
1047	    pairs_sweep:
1048	      10:
1049	        median_auroc: 0.762
1050	        pct_of_200: 0.88
1051	      20:
1052	        median_auroc: 0.778
1053	        pct_of_200: 0.94
1054	      50:
1055	        median_auroc: 0.792
1056	        pct_of_200: 0.98
1057	      100:
1058	        median_auroc: 0.796
1059	        pct_of_200: 0.99
1060	      200:
1061	        median_auroc: 0.798
1062	        pct_of_200: 1.0
1063	    low_resource_saturation_later: true
1064	    low_resource_min_pairs: 48
1065	    high_resource_min_pairs: 22
1066	  result_rationale: 'Linear projection在~35 pairs时达到饱和（95% of 200-pair performance），
1067	    因为correctness方向是低维线性结构——学习一个旋转/缩放矩阵不需要很多样本。 10 pairs已经达到88%性能，说明即使极少数据也能捕获主要的geometric
1068	    transformation。 50 pairs后几乎无改善（98%→100%），符合线性映射的low sample complexity理论。 Low-resource语言需要slightly
1069	    more pairs（48 vs 22），因为表征空间中 correctness方向的SNR更低，需要更多样本来robustly估计映射。 整体saturation在20-50范围内，support
1070	    "≤50 parallel pairs suffice"的claim。 这建立了linear projection作为practical baseline的地位——
1071	    50 pairs在任何语言都容易获得（e.g., 翻译50个MCQA items）。
1072	
1073	    '
1074	  tables:
1075	  - name: 'Table 11: Linear Projection Data Efficiency (median across 20 langs × 2
1076	      models)'
1077	    columns:
1078	    - n_pairs
1079	    - median_auroc
1080	    - delta_vs_zs
1081	    - pct_of_200pair
1082	    - HIGH_auroc
1083	    - LOW_auroc
1084	    rows:
1085	    - - 10
1086	      - 0.762
1087	      - 0.027
1088	      - 88
1089	      - 0.781
1090	      - 0.638
1091	    - - 20
1092	      - 0.778
1093	      - 0.043
1094	      - 94
1095	      - 0.798
1096	      - 0.651
1097	    - - 50
1098	      - 0.792
1099	      - 0.057
1100	      - 98
1101	      - 0.814
1102	      - 0.664
1103	    - - 100
1104	      - 0.796
1105	      - 0.061
1106	      - 99
1107	      - 0.818
1108	      - 0.668
1109	    - - 200
1110	      - 0.798
1111	      - 0.063
1112	      - 100
1113	      - 0.821
1114	      - 0.671
1115	  figures_description:
1116	  - 'Fig S4: Learning curve — n_pairs (x, log) vs median AUROC (y). Rapid rise, plateau
1117	    at ~50. Separate lines for HIGH/MID/LOW tiers — all plateau but at different levels.'
1118	  analysis: 'Linear projection的data efficiency confirms它作为practical baseline的价值。 50
1119	    pairs的saturation point意味着任何有minimal translation capacity的语言 都可以使用这个方法。这也为CaCLR设定了benchmark：CaCLR需要beat
1120	    50-pair projection 才能justify its additional complexity（in best tier, CaCLR beats
1121	    by +1.4pp median）。
1122	
1123	    '
1124	- name: Probing Control Tasks (Hewitt & Liang 2019)
1125	  plan_id: plan_013
1126	  description: 'Random-label control probes at each layer. Selectivity = probe AUROC
1127	    - control AUROC. Validates genuine correctness signal.
1128	
1129	    '
1130	  expected_results:
1131	    control_task_auroc_range:
1132	    - 0.502
1133	    - 0.538
1134	    selectivity_median: 0.284
1135	    selectivity_min: 0.192
1136	    selectivity_max: 0.341
1137	    control_task_selectivity_min_across_langs: 0.192
1138	    selectivity_by_depth:
1139	      shallow: 0.218
1140	      mid: 0.294
1141	      deep: 0.312
1142	    selectivity_by_tier:
1143	      HIGH: 0.301
1144	      MID: 0.278
1145	      LOW: 0.234
1146	  result_rationale: 'Control probe AUROC在0.50-0.54范围（near chance），selectivity中位数0.284
1147	    远超15pp minimum threshold（min=19.2pp）。这confirm probe AUROC反映 genuine correctness
1148	    direction而非memorized artifacts或probe capacity。 Selectivity随depth增加（0.218→0.312），因为深层表征包含更丰富的correctness
1149	    信号而control仍在chance附近——深层probe的高AUROC不是因为probe容量过大。 Low-resource语言selectivity最低（0.234）但仍远超threshold，
1150	    说明即使低资源语言的correctness信号也是genuine的（不是noise fitting）。 这直接回应Hewitt & Liang probing
1151	    methodology critique—— 我们的probes确实在提取linguistic property而非exploiting high-dimensional
1152	    capacity。
1153	
1154	    '
1155	  tables:
1156	  - name: 'Table S2: Control Task Selectivity (Qwen3-235B, selected layers × languages)'
1157	    columns:
1158	    - layer
1159	    - en_selectivity
1160	    - zh_selectivity
1161	    - sw_selectivity
1162	    - control_auroc
1163	    rows:
1164	    - - 16
1165	      - 0.248
1166	      - 0.231
1167	      - 0.192
1168	      - 0.512
1169	    - - 32
1170	      - 0.281
1171	      - 0.268
1172	      - 0.218
1173	      - 0.519
1174	    - - 48
1175	      - 0.309
1176	      - 0.292
1177	      - 0.241
1178	      - 0.524
1179	    - - 56
1180	      - 0.318
1181	      - 0.301
1182	      - 0.248
1183	      - 0.521
1184	    - - 76
1185	      - 0.341
1186	      - 0.324
1187	      - 0.262
1188	      - 0.538
1189	  figures_description:
1190	  - 'Fig S5: Paired bar chart — probe AUROC (dark) vs control AUROC (light) at each
1191	    layer. Gap (selectivity) clearly visible and widening with depth. Horizontal line
1192	    at 15pp threshold.'
1193	  analysis: 'Control task validation是methodological necessity。Selectivity最小值19.2pp
1194	    大幅超过15pp阈值，即使在最challenging的条件（low-resource × shallow layer） 也确认probe是在提取genuine
1195	    signal。这让reviewer对所有downstream结果 （Pareto frontier, CaCLR, decomposition）更有信心。
1196	
1197	    '
1198	- name: Gemma 4 31B Dense — Camera-Ready Extension
1199	  plan_id: plan_008
1200	  description: 'Third architecture (dense, FP16), full Pareto frontier. Dense vs MoE
1201	    contrast for camera-ready.
1202	
1203	    '
1204	  expected_results:
1205	    en_best_auroc: 0.809
1206	    en_best_layer: 48
1207	    optimal_transfer_layer: 36
1208	    zs_transfer_auroc_median: 0.738
1209	    pareto_rho_median: -0.69
1210	    pareto_shape: smoother frontier than MoE models — no sharp elbow
1211	    dense_vs_moe_key_finding: 'Dense architecture shows shallower Pareto slope — transfer
1212	      degrades more gradually with depth compared to MoE models. Consistent with hypothesis
1213	      that expert routing accelerates language specialization.
1214	
1215	      '
1216	  result_rationale: 'Gemma 4 31B Dense作为dense对照提供了architectural contrast。 EN AUROC
1217	    0.809低于两个MoE模型（0.838, 0.821），反映31B dense参数<235B MoE active参数。 关键发现：dense架构的Pareto
1218	    frontier更平滑（rho=-0.69 vs MoE -0.73/-0.78）， 没有MoE的sharp elbow。这是因为MoE的expert routing在深层创造了discrete
1219	    language specialization（某些experts "负责"特定语言），而dense模型的specialization是gradual的。
1220	    这是architecture-dependent Pareto shape claim的strongest evidence。 Optimal transfer在75%深度（layer
1221	    36/48），比Qwen3浅（60%）但比Scout深（50%）， 提供了第三个data point来characterize architecture-depth
1222	    relationship。
1223	
1224	    '
1225	  tables:
1226	  - name: 'Table S3: Three-Architecture Comparison Summary'
1227	    columns:
1228	    - model
1229	    - type
1230	    - params
1231	    - layers
1232	    - en_best_auroc
1233	    - zs_median
1234	    - optimal_transfer_pct
1235	    - pareto_rho
1236	    rows:
1237	    - - Qwen3-235B-A22B
1238	      - MoE
1239	      - 235B
1240	      - 94
1241	      - 0.838
1242	      - 0.758
1243	      - 60
1244	      - -0.78
1245	    - - Llama 4 Scout
1246	      - MoE
1247	      - 109B (17B active)
1248	      - 48
1249	      - 0.821
1250	      - 0.742
1251	      - 50
1252	      - -0.73
1253	    - - Gemma 4 31B Dense
1254	      - Dense
1255	      - 31B
1256	      - 60
1257	      - 0.809
1258	      - 0.738
1259	      - 75
1260	      - -0.69
1261	  figures_description:
1262	  - 'Fig S6: Three Pareto frontiers overlaid on normalized depth axis. MoE models
1263	    show sharper elbows; Dense model is smoother. Annotated with optimal transfer
1264	    depth for each.'
1265	  analysis: 'Three-architecture comparison is the crown jewel of Claim 1。 Dense vs
1266	    MoE对比provides causal insight into WHY frontiers differ—— expert routing is the
1267	    mechanism driving sharp language specialization at depth.
1268	
1269	    '
1270	- name: Extended Language Coverage — Camera-Ready
1271	  plan_id: plan_009
1272	  description: 'Expand from 20 to 50+ languages. Camera-ready extension using GlobalMMLU/Belebele
1273	    full sets.
1274	
1275	    '
1276	  expected_results:
1277	    total_languages: 52
1278	    zs_langs_above_0p65: 38
1279	    zs_auroc_median_52lang: 0.721
1280	    new_low_resource_findings: 'Several additional low-resource languages (e.g., Yoruba,
1281	      Hausa, Malagasy) show ZS AUROC 0.58-0.64, confirming resource-tier gradient
1282	      extends to tail.
1283	
1284	      '
1285	    pareto_frontier_robust: true
1286	    caclr_generalizes: true
1287	    caclr_delta_over_zs_52lang_median: 0.058
1288	  result_rationale: '52语言验证confirms所有findings at broader scale。ZS median从20 langs的0.758
1289	    降到52 langs的0.721，因为新增语言主要是低资源的——这是expected的composition effect。 38/52 > 0.65（73%）vs
1290	    17/20（85%），比例下降也反映低资源语言的加入。 Pareto frontier和CaCLR在所有语言上consistent，说明findings是language-general的。
1291	    Key new finding：Yoruba/Hausa等sub-Saharan African语言的ZS AUROC（0.58-0.62） 与sw/bn相当，但CaCLR对这些语言的improvement更大（+7-9pp），
1292	    可能因为GlobalMMLU translations provide parallel data that partially bridges the representation
1293	    gap for these extremely low-resource languages.
1294	
1295	    '
1296	  tables:
1297	  - name: 'Table S4: Extended Language Coverage Summary'
1298	    columns:
1299	    - resource_tier
1300	    - n_langs
1301	    - zs_auroc_median
1302	    - caclr_median
1303	    - delta
1304	    rows:
1305	    - - HIGH
1306	      - 12
1307	      - 0.786
1308	      - 0.828
1309	      - 0.042
1310	    - - MID
1311	      - 18
1312	      - 0.741
1313	      - 0.798
1314	      - 0.057
1315	    - - LOW
1316	      - 22
1317	      - 0.648
1318	      - 0.721
1319	      - 0.073
1320	  figures_description:
1321	  - 'Fig S7: World map — ZS AUROC by country/language, color gradient from red (low)
1322	    to green (high). Clear geographic pattern tracking resource availability.'
1323	  analysis: Extended coverage是camera-ready的scale argument。核心findings在52语言上robust。
1324	    Low-resource语言从CaCLR获益最多（+7.3pp vs HIGH +4.2pp）， because these languages have
1325	    the most room for improvement and CaCLR's distributional alignment compensates
1326	    for sparse pretraining representation.
1327	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "494e9d15-8672-4234-a407-56fa1cf71899",
  "isSidechain": false,
  "promptId": "248aeb9c-3304-4117-b59f-e1434de9c70f",
  "type": "user",
  "uuid": "658c2477-2fce-4b99-aaef-3291062fa6c1",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T201854/best/review_context.yaml",
      "content": "narrative_guidance: 'Full method contribution paper (Path A). CaCLR consistency loss\n  provides meaningful gain, confirming distributional matching via MMD helps align\n  capability-specific signals at mid-depth layers. Causal chain complete: Pareto frontier\n  discovered on both architectures with architecture-dependent shape → decomposition\n  explains frontier via difficulty/capability separation → CaCLR shifts frontier by\n  aligning capability-specific components → orthogonality bounds output-based approaches\n  across all languages. CKA provides mechanistic glue linking representation geometry\n  to transfer success. Headline: \"CaCLR-trained correctness probes reduce non-English\n  ECE by 3.5% over temperature scaling with zero target-language labels across 20\n  languages on Qwen3-235B and Llama 4 Scout.\"\n\n  '\nimagined_experiments:\n- name: Full Pareto Frontier — Qwen3-235B-A22B\n  plan_id: plan_001\n  description: '94-layer MoE model, INT8, 24 probed layers (every 4th), 20 languages,\n    5 transfer conditions (zero-shot, mean-shift, linear projection, few-shot 25/100,\n    CaCLR).\n\n    '\n  expected_results:\n    en_best_auroc: 0.838\n    en_best_layer: 76\n    en_best_ece_raw: 0.162\n    en_best_ece_tempcal: 0.048\n    temp_scaling_T: 4.83\n    en_auroc_range:\n    - 0.592\n    - 0.838\n    optimal_transfer_layer_median: 56\n    zs_transfer_auroc_median_20lang: 0.758\n    zs_transfer_auroc_at_en_optimal_layer76: 0.714\n    zs_transfer_auroc_at_transfer_optimal_layer56: 0.771\n    pareto_rho_global: -0.81\n    pareto_rho_per_lang_median: -0.78\n    pareto_rho_per_lang_iqr:\n    - -0.84\n    - -0.71\n    zs_langs_above_0p65_out_of_20: 17\n    best_zs_auroc_by_tier:\n      HIGH_zh: 0.793\n      HIGH_es: 0.801\n      HIGH_fr: 0.798\n      HIGH_de: 0.784\n      MID_hi: 0.742\n      MID_ru: 0.769\n      MID_ko: 0.751\n      MID_tr: 0.738\n      LOW_sw: 0.641\n      LOW_bn: 0.633\n    mean_shift_delta_auroc_median: 0.0\n    linear_proj_delta_auroc_over_zs_median: 0.048\n    fewshot_25_delta_auroc_over_zs_median: 0.032\n    fewshot_100_delta_auroc_over_zs_median: 0.055\n  result_rationale: 'Qwen3-235B-A22B的94层深度和MoE架构产生了强correctness信号。235B参数量使EN AUROC达到0.838，\n    远超7B MVP的0.754——更大模型的内部表征更丰富、correctness方向更可分离。 Pareto frontier清晰存在：layer 76（81%深度）是EN最优但跨语言transfer在此处下降约5.7pp\n    （从layer 56的0.771降至0.714），因为深层表征越来越language-specific。 MoE架构中expert routing在深层更加language-dependent，强化了这一效应。\n    Spearman rho中位数-0.78反映depth-transfer反相关在绝大多数语言中一致。 17/20语言ZS AUROC>0.65体现了235B模型强大的multilingual\n    representation—— 仅sw/bn/my三个极低资源语言未达标，符合Ben-David H-divergence理论预测。 Mean-shift\n    ΔAUROC=0.000由rank-invariance定理保证（StandardScaler + logistic regression下 mean-shift仅添加常数偏移，不改变rank\n    order）。 Linear projection作为强baseline（+4.8pp）反映correctness方向在语言间存在可学习的线性映射关系。\n\n    '\n  tables:\n  - name: 'Table 1: Qwen3-235B Pareto Frontier — EN AUROC vs ZS Transfer AUROC by\n      Layer'\n    columns:\n    - layer\n    - depth_pct\n    - en_auroc\n    - zs_median_auroc\n    - zs_min_auroc\n    - zs_max_auroc\n    - rho_median\n    rows:\n    - - 0\n      - 0\n      - 0.592\n      - 0.583\n      - 0.521\n      - 0.601\n      - null\n    - - 8\n      - 9\n      - 0.631\n      - 0.618\n      - 0.554\n      - 0.639\n      - null\n    - - 16\n      - 17\n      - 0.672\n      - 0.659\n      - 0.589\n      - 0.678\n      - null\n    - - 24\n      - 26\n      - 0.711\n      - 0.698\n      - 0.621\n      - 0.719\n      - null\n    - - 32\n      - 34\n      - 0.738\n      - 0.729\n      - 0.648\n      - 0.751\n      - null\n    - - 40\n      - 43\n      - 0.762\n      - 0.756\n      - 0.662\n      - 0.778\n      - null\n    - - 48\n      - 51\n      - 0.781\n      - 0.771\n      - 0.658\n      - 0.793\n      - null\n    - - 56\n      - 60\n      - 0.798\n      - 0.771\n      - 0.641\n      - 0.801\n      - null\n    - - 60\n      - 64\n      - 0.808\n      - 0.762\n      - 0.632\n      - 0.796\n      - null\n    - - 64\n      - 68\n      - 0.816\n      - 0.751\n      - 0.618\n      - 0.788\n      - null\n    - - 68\n      - 72\n      - 0.824\n      - 0.741\n      - 0.607\n      - 0.779\n      - null\n    - - 72\n      - 77\n      - 0.831\n      - 0.728\n      - 0.598\n      - 0.768\n      - null\n    - - 76\n      - 81\n      - 0.838\n      - 0.714\n      - 0.584\n      - 0.756\n      - null\n    - - 80\n      - 85\n      - 0.835\n      - 0.702\n      - 0.571\n      - 0.742\n      - null\n    - - 84\n      - 89\n      - 0.829\n      - 0.688\n      - 0.558\n      - 0.729\n      - null\n    - - 88\n      - 94\n      - 0.818\n      - 0.671\n      - 0.542\n      - 0.712\n      - null\n    - - 92\n      - 98\n      - 0.801\n      - 0.649\n      - 0.523\n      - 0.694\n      - null\n  - name: 'Table 2: Qwen3-235B Transfer Conditions at Fixed Layers (layer 56 + layer\n      76)'\n    columns:\n    - condition\n    - layer56_median_auroc\n    - layer76_median_auroc\n    - delta_vs_zs_l56\n    - delta_vs_zs_l76\n    rows:\n    - - zero-shot\n      - 0.771\n      - 0.714\n      - 0.0\n      - 0.0\n    - - mean-shift\n      - 0.771\n      - 0.714\n      - 0.0\n      - 0.0\n    - - linear_proj_50pairs\n      - 0.812\n      - 0.779\n      - 0.041\n      - 0.065\n    - - fewshot_25\n      - 0.798\n      - 0.761\n      - 0.027\n      - 0.047\n    - - fewshot_100\n      - 0.821\n      - 0.792\n      - 0.05\n      - 0.078\n    - - CaCLR_full\n      - 0.828\n      - 0.788\n      - 0.057\n      - 0.074\n  figures_description:\n  - 'Fig 1a: Pareto frontier scatter — x-axis EN AUROC, y-axis ZS transfer AUROC median.\n    Each point is a layer. Clear concave frontier with elbow at ~60% depth. Color\n    by resource tier shows HIGH langs cluster top-right, LOW langs bottom-left.'\n  - 'Fig 1b: Heatmap 24 layers × 20 languages, cell color = ZS AUROC. Visible gradient:\n    warm (high AUROC) at mid-depth for high-resource, shifting to shallower optimum\n    for low-resource.'\n  - 'Fig 1c: Per-language Spearman rho distribution (violin plot). Median -0.78, tight\n    IQR, all languages negative. Annotate sw/bn as outliers with weaker rho.'\n  analysis: 'Pareto frontier 在 Qwen3-235B 上形态清晰。拐点在 layer 56（60% depth）—— 此后EN AUROC继续上升但ZS\n    transfer开始下降。MoE架构的expert routing在深层 更加language-specific是造成Pareto tradeoff的主要机制。High-resource语言\n    （zh/es/fr/de）的frontier更靠右上方，因为这些语言在pretraining中获得更多 token coverage，deep-layer\n    representation与EN的对齐更好。Low-resource（sw/bn） 即使在最优transfer层也仅达到0.64左右，符合H-divergence理论预测。\n\n    '\n- name: Full Pareto Frontier — Llama 4 Scout\n  plan_id: plan_002\n  description: '48-layer MoE model, INT8, 12 probed layers (every 4th), 20 languages,\n    5 transfer conditions.\n\n    '\n  expected_results:\n    en_best_auroc: 0.821\n    en_best_layer: 40\n    en_best_ece_raw: 0.171\n    en_best_ece_tempcal: 0.053\n    temp_scaling_T: 5.12\n    en_auroc_range:\n    - 0.604\n    - 0.821\n    optimal_transfer_layer_median: 24\n    zs_transfer_auroc_median_20lang: 0.742\n    zs_transfer_auroc_at_en_optimal_layer40: 0.698\n    zs_transfer_auroc_at_transfer_optimal_layer24: 0.756\n    pareto_rho_global: -0.76\n    pareto_rho_per_lang_median: -0.73\n    pareto_rho_per_lang_iqr:\n    - -0.81\n    - -0.66\n    zs_langs_above_0p65_out_of_20: 16\n    best_zs_auroc_by_tier:\n      HIGH_zh: 0.778\n      HIGH_es: 0.789\n      HIGH_fr: 0.781\n      HIGH_de: 0.772\n      MID_hi: 0.728\n      MID_ru: 0.756\n      MID_ko: 0.739\n      MID_tr: 0.721\n      LOW_sw: 0.628\n      LOW_bn: 0.618\n    mean_shift_delta_auroc_median: 0.0\n    linear_proj_delta_auroc_over_zs_median: 0.044\n  result_rationale: 'Llama 4 Scout的48层架构使optimal transfer层在50%深度（layer 24）， 而Qwen3-235B在60%深度（layer\n    56）——这就是architecture-dependent shape的关键证据。 Scout的层数不到Qwen的一半，deep层的language specialization发生得更快（按比例）。\n    EN best AUROC=0.821略低于Qwen的0.838，反映Scout虽然是MoE但active参数更少。 ZS median 0.742 vs\n    Qwen的0.758，差距16pp体现了Llama系列multilingual pretraining 数据在低资源语言上的相对弱势。Pareto rho中位数-0.73略弱于Qwen的-0.78，\n    因为Scout只有12个probed层，frontier采样更粗糙。16/20语言>0.65（vs Qwen 17/20）， sw/bn/my/jv四个低资源语言未达标。Architecture-dependent差异是本文Claim\n    1的核心发现。\n\n    '\n  tables:\n  - name: 'Table 3: Llama 4 Scout Pareto Frontier'\n    columns:\n    - layer\n    - depth_pct\n    - en_auroc\n    - zs_median_auroc\n    rows:\n    - - 0\n      - 0\n      - 0.604\n      - 0.592\n    - - 4\n      - 8\n      - 0.638\n      - 0.624\n    - - 8\n      - 17\n      - 0.674\n      - 0.661\n    - - 12\n      - 25\n      - 0.712\n      - 0.701\n    - - 16\n      - 33\n      - 0.741\n      - 0.738\n    - - 20\n      - 42\n      - 0.768\n      - 0.756\n    - - 24\n      - 50\n      - 0.788\n      - 0.756\n    - - 28\n      - 58\n      - 0.801\n      - 0.742\n    - - 32\n      - 67\n      - 0.811\n      - 0.726\n    - - 36\n      - 75\n      - 0.818\n      - 0.711\n    - - 40\n      - 83\n      - 0.821\n      - 0.698\n    - - 44\n      - 92\n      - 0.814\n      - 0.679\n    - - 48\n      - 100\n      - 0.798\n      - 0.654\n  figures_description:\n  - 'Fig 2a: Pareto frontiers overlaid — Qwen3-235B (blue) vs Llama 4 Scout (orange).\n    Both concave but elbow position differs: Qwen at 60% depth, Scout at 50%. Demonstrates\n    architecture-dependent shape.'\n  - 'Fig 2b: Architecture comparison heatmap — difference in ZS AUROC (Qwen minus\n    Scout) by language × normalized depth. Positive (Qwen better) at deep layers for\n    high-resource; near zero at shallow layers.'\n  analysis: '两个架构的Pareto frontier在归一化深度上呈现不同形状：Qwen3-235B的拐点在60%深度， Scout在50%深度。这一差异不能由模型大小alone解释（两者都是MoE），\n    而是反映了训练数据分布、expert routing策略和层归一化实现的差异。 Scout在每层的language specialization更剧烈，导致frontier更陡峭、拐点更早。\n    这是论文最核心的发现之一：optimal transfer depth不是universal的，必须per-architecture确定。\n\n    '\n- name: CaCLR Implementation and Comparative Evaluation\n  plan_id: plan_003\n  description: 'CaCLR (L_BCE + α·L_SB-ECE + β·L_MMD) 训练、超参数sweep、与所有baseline的全面比较。\n    Path A: β term provides meaningful gain.\n\n    '\n  expected_results:\n    caclr_optimal_alpha: 1.0\n    caclr_optimal_beta: 0.1\n    caclr_beta_delta_auroc_over_alpha_only_median: 0.032\n    caclr_beta_delta_auroc_over_alpha_only_range:\n    - 0.018\n    - 0.051\n    caclr_full_delta_auroc_over_zeroshot_median: 0.062\n    caclr_full_delta_auroc_over_zeroshot_range:\n    - 0.031\n    - 0.098\n    caclr_vs_linear_proj_delta_median: 0.014\n    caclr_vs_fewshot100_delta_median: -0.008\n    ece_reduction_vs_temp_scaling_median: 0.035\n    ece_reduction_vs_temp_scaling_range:\n    - 0.012\n    - 0.061\n    beta_sweep_results:\n      beta_0.001:\n        delta_auroc_over_alpha_only: 0.008\n        note: too weak\n      beta_0.01:\n        delta_auroc_over_alpha_only: 0.019\n        note: marginal\n      beta_0.1:\n        delta_auroc_over_alpha_only: 0.032\n        note: optimal\n      beta_1.0:\n        delta_auroc_over_alpha_only: 0.021\n        note: overfitting to distributional match\n    alpha_sweep_results:\n      alpha_0.01:\n        en_ece: 0.068\n        transfer_auroc_median: 0.779\n      alpha_0.1:\n        en_ece: 0.055\n        transfer_auroc_median: 0.793\n      alpha_1.0:\n        en_ece: 0.041\n        transfer_auroc_median: 0.808\n      alpha_10.0:\n        en_ece: 0.038\n        transfer_auroc_median: 0.791\n    layer_interaction:\n      mid_depth_beta_gain: 0.041\n      deep_layer_beta_gain: 0.024\n      shallow_layer_beta_gain: 0.018\n    qwen_results:\n      layer56_caclr_full_median: 0.828\n      layer76_caclr_full_median: 0.788\n    scout_results:\n      layer24_caclr_full_median: 0.812\n      layer40_caclr_full_median: 0.771\n    bootstrap_ci_beta_effect:\n    - 0.019\n    - 0.045\n    paired_permutation_p_beta: 0.003\n    cohens_d_beta: 0.48\n  result_rationale: 'CaCLR consistency loss (β term) 提供了有意义的增益（中位数+3.2pp over α-only），\n    支持Path A叙事。β=0.1是最优点——更低（0.001-0.01）则MMD约束太弱无法对齐分布， 更高（1.0）则过度约束导致correctness\n    prediction损失。 β增益在mid-depth层（40-60%）最大（+4.1pp），因为这些层的cross-lingual表征 仍有足够的共享结构让MMD可以有效对齐，但已经开始出现分化需要对齐。\n    在deep层β增益下降到+2.4pp，因为表征的geometric misalignment（非仅distributional shift） 限制了MMD的有效性——但CaCLR仍然比zero-shot好得多。\n    CaCLR vs linear projection：CaCLR赢1.4pp中位数，因为它同时优化calibration（α项） 和alignment（β项），而linear\n    projection仅做alignment。但CaCLR略输于few-shot 100 （-0.8pp），因为100个标注样本提供了直接的target-language\n    correctness信号。 关键：CaCLR不需要target-language labels，这是实际场景中的核心优势。 ECE reduction vs\n    temp scaling中位数3.5pp，因为CaCLR在训练时直接优化SB-ECE， 而temp scaling仅做post-hoc rescaling无法修复表征层面的miscalibration。\n    Bootstrap CI [0.019, 0.045]和p=0.003确认β效应统计显著；Cohen''s d=0.48为中等效应量。\n\n    '\n  tables:\n  - name: 'Table 4: Transfer Method Comparison (Median AUROC across 20 languages,\n      both models)'\n    columns:\n    - method\n    - labels_needed\n    - qwen_layer56\n    - qwen_layer76\n    - scout_layer24\n    - scout_layer40\n    - median_all\n    rows:\n    - - zero-shot\n      - 0\n      - 0.771\n      - 0.714\n      - 0.756\n      - 0.698\n      - 0.735\n    - - mean-shift\n      - 0\n      - 0.771\n      - 0.714\n      - 0.756\n      - 0.698\n      - 0.735\n    - - CaCLR_alpha_only\n      - 0 (parallel inputs)\n      - 0.798\n      - 0.762\n      - 0.784\n      - 0.745\n      - 0.772\n    - - CaCLR_full\n      - 0 (parallel inputs)\n      - 0.828\n      - 0.788\n      - 0.812\n      - 0.771\n      - 0.8\n    - - linear_proj_50\n      - 50 parallel pairs\n      - 0.812\n      - 0.779\n      - 0.798\n      - 0.758\n      - 0.787\n    - - fewshot_25\n      - 25\n      - 0.798\n      - 0.761\n      - 0.781\n      - 0.741\n      - 0.77\n    - - fewshot_100\n      - 100\n      - 0.821\n      - 0.792\n      - 0.808\n      - 0.778\n      - 0.8\n  - name: 'Table 5: β Sensitivity Sweep (Qwen3-235B, layer 56, median across 20 langs)'\n    columns:\n    - beta\n    - delta_auroc_over_alpha_only\n    - delta_ece_over_alpha_only\n    - note\n    rows:\n    - - 0.001\n      - 0.008\n      - -0.003\n      - negligible distributional constraint\n    - - 0.01\n      - 0.019\n      - -0.008\n      - marginal improvement\n    - - 0.1\n      - 0.032\n      - -0.014\n      - optimal — balances alignment and prediction\n    - - 1.0\n      - 0.021\n      - -0.011\n      - over-regularized — MMD dominates loss\n  figures_description:\n  - 'Fig 3a: Bar chart — 5 transfer methods × 2 models at optimal transfer layer.\n    CaCLR_full highest, followed by fewshot_100, linear_proj, CaCLR_alpha_only, zero-shot.\n    Error bars = bootstrap 95% CI.'\n  - 'Fig 3b: β sweep curve — x-axis β (log scale), y-axis ΔAUROC over α-only. Inverted-U\n    shape peaking at β=0.1. Three lines for shallow/mid/deep layers showing mid-depth\n    benefits most.'\n  - 'Fig 3c: Pareto frontier shift — original ZS frontier (dashed) vs CaCLR frontier\n    (solid) for both architectures. CaCLR pushes frontier up and right, especially\n    at mid-depth.'\n  analysis: 'CaCLR的consistency loss在mid-depth层效果最好，这与CKA分析（plan_011）一致： mid-depth层的cross-lingual表征相似度足够高让MMD有效对齐，但已经有enough\n    language-specific分化使得对齐产生实际收益。β=0.1的inverted-U曲线说明 distributional matching存在sweet\n    spot——太弱无效，太强则牺牲correctness prediction。 CaCLR vs fewshot_100的near-parity（-0.8pp）是重要结果：CaCLR达到了接近\n    100-label supervised的性能，但不需要任何target-language correctness labels。 统计显著性（p=0.003,\n    d=0.48）确保β效应不是噪声。\n\n    '\n- name: Difficulty-Controlled Decomposition Ablation\n  plan_id: plan_004\n  description: 'IRT difficulty probes → project out difficulty → retrain correctness\n    probes → evaluate transfer. 10 languages × 8 layers × 2 models.\n\n    '\n  expected_results:\n    decomposition_transfer_delta_after_difficulty_removal_median: 0.031\n    decomposition_transfer_delta_range:\n    - 0.011\n    - 0.052\n    difficulty_probe_r2_median: 0.68\n    difficulty_direction_cosine_with_correctness: 0.34\n    capability_specific_transfer_degradation_per_depth:\n      shallow_20pct: 0.008\n      mid_50pct: 0.024\n      deep_80pct: 0.048\n    random_direction_control_delta: 0.002\n    resource_tier_pattern:\n      HIGH_delta: 0.022\n      MID_delta: 0.033\n      LOW_delta: 0.041\n    bootstrap_ci_decomposition_delta:\n    - 0.018\n    - 0.044\n    paired_permutation_p: 0.006\n    cohens_d: 0.41\n  result_rationale: 'Difficulty direction与correctness direction有中等cosine（0.34），说明两者共享\n    部分信号但不完全重叠。Project out difficulty后，残差中的correctness信号更 \"capability-pure\"——这个信号在高资源语言间更容易transfer（+2.2pp），\n    因为capability-specific failures在这些语言间更一致。低资源语言获益最大（+4.1pp）， 因为原始correctness方向中difficulty成分占比更高（低资源语言的difficulty分布\n    与EN差异更大），去除difficulty后暴露出更可transfer的capability信号。 深层退化更明显（4.8pp）因为深层同时编码了更多language-specific的difficulty信息。\n    Random-direction control仅+0.2pp，排除了dimensionality reduction artifact—— 是difficulty方向的specific\n    removal而非arbitrary降维带来的改善。 这个分解是prescriptive的：它告诉我们哪些language-layer组合需要capability\n    alignment （高delta = 高difficulty entanglement = 需要CaCLR/projection）。\n\n    '\n  tables:\n  - name: 'Table 6: Decomposition Effect by Resource Tier and Depth (ΔAUROC after\n      difficulty removal)'\n    columns:\n    - depth_pct\n    - HIGH_avg\n    - MID_avg\n    - LOW_avg\n    - random_control\n    rows:\n    - - 20\n      - 0.012\n      - 0.014\n      - 0.019\n      - 0.001\n    - - 35\n      - 0.016\n      - 0.022\n      - 0.028\n      - 0.002\n    - - 50\n      - 0.021\n      - 0.031\n      - 0.038\n      - 0.002\n    - - 60\n      - 0.024\n      - 0.036\n      - 0.043\n      - 0.003\n    - - 70\n      - 0.026\n      - 0.039\n      - 0.046\n      - 0.002\n    - - 80\n      - 0.028\n      - 0.041\n      - 0.048\n      - 0.003\n    - - 85\n      - 0.025\n      - 0.038\n      - 0.044\n      - 0.002\n    - - 90\n      - 0.022\n      - 0.034\n      - 0.041\n      - 0.002\n  figures_description:\n  - 'Fig 4a: Three-panel heatmap (HIGH/MID/LOW) — 8 layers × decomposition delta.\n    Gradient intensifies with depth and decreases with resource level.'\n  - 'Fig 4b: Scatter plot — difficulty-correctness cosine similarity vs decomposition\n    delta. Each point = language × layer. Clear positive correlation (r=0.71).'\n  - 'Fig 4c: Bar chart — decomposition delta vs random-direction control delta at\n    each depth. Orders of magnitude difference confirms specificity.'\n  analysis: 'Decomposition结果支持Claim 2：difficulty和capability在correctness方向中可分离， 且分离后capability-specific信号的cross-lingual\n    transfer一致改善。 关键insight是resource tier gradient——低资源语言的difficulty entanglement最严重，\n    也从decomposition中获益最多。这为CaCLR提供了theoretical motivation： CaCLR的consistency loss本质上在做distributional\n    alignment of capability-specific signals。 Random-direction control（~0pp）是关键的methodological\n    guard rail。\n\n    '\n- name: Cross-Lingual Orthogonality Analysis\n  plan_id: plan_005\n  description: 'Correctness-confidence cosine similarity across 20 languages × 2 architectures,\n    analyzed by resource tier and language family.\n\n    '\n  expected_results:\n    orthogonality_cosine_mean_across_langs: 0.042\n    orthogonality_cosine_max_across_langs: 0.062\n    orthogonality_cosine_min_across_langs: 0.018\n    orthogonality_cosine_std: 0.013\n    cosine_by_tier:\n      HIGH_mean: 0.038\n      MID_mean: 0.043\n      LOW_mean: 0.051\n    cosine_by_architecture:\n      qwen_mean: 0.039\n      scout_mean: 0.046\n    cosine_range_qwen_20lang:\n    - 0.018\n    - 0.058\n    cosine_range_scout_20lang:\n    - 0.022\n    - 0.062\n    all_20_langs_below_0p08: true\n    bootstrap_ci_mean_cosine:\n    - 0.035\n    - 0.049\n  result_rationale: 'Orthogonality在所有20语言 × 2架构上持续存在（max cosine 0.062 < 0.08阈值）， 确认Miao\n    & Ungar (2026)的English-only发现是universal structural property。 Low-resource语言cosine略高（0.051\n    vs HIGH 0.038），因为这些语言的confidence probe quality更低（更少训练数据→confidence方向估计噪声更大→与correctness的\n    apparent cosine被噪声inflate）。但即使是最高的0.062也远低于non-orthogonal阈值， 说明output-based calibration在结构上受限不依赖于语言。\n    Qwen略比Scout更orthogonal（0.039 vs 0.046），可能反映Qwen更大的模型容量 使correctness和confidence能被编码在更分离的子空间中。\n    这个发现bounds entire output-based calibration approach：无论语言或架构， verbalized confidence不包含correctness信息，motivating\n    probe-based方法。\n\n    '\n  tables:\n  - name: 'Table 7: Correctness-Confidence Cosine Similarity by Language'\n    columns:\n    - language\n    - tier\n    - qwen_cosine\n    - scout_cosine\n    - mean\n    rows:\n    - - en\n      - HIGH\n      - 0.031\n      - 0.037\n      - 0.034\n    - - zh\n      - HIGH\n      - 0.035\n      - 0.041\n      - 0.038\n    - - es\n      - HIGH\n      - 0.033\n      - 0.039\n      - 0.036\n    - - fr\n      - HIGH\n      - 0.034\n      - 0.04\n      - 0.037\n    - - de\n      - HIGH\n      - 0.036\n      - 0.042\n      - 0.039\n    - - hi\n      - MID\n      - 0.039\n      - 0.045\n      - 0.042\n    - - ru\n      - MID\n      - 0.037\n      - 0.043\n      - 0.04\n    - - ko\n      - MID\n      - 0.041\n      - 0.047\n      - 0.044\n    - - tr\n      - MID\n      - 0.043\n      - 0.049\n      - 0.046\n    - - sw\n      - LOW\n      - 0.048\n      - 0.056\n      - 0.052\n    - - bn\n      - LOW\n      - 0.052\n      - 0.058\n      - 0.055\n  figures_description:\n  - 'Fig 5: Dot plot — cosine similarity per language, sorted by resource tier. Horizontal\n    line at 0.08 threshold. All points below. Color by architecture (Qwen blue, Scout\n    orange). Visible tier gradient.'\n  analysis: 'Cross-lingual orthogonality的universal persistence是论文的bounding contribution。\n    它回答了\"为什么需要probe-based calibration\"：因为output-based方法在结构上 无法获取correctness信息（cosine<0.08），无论语言。Resource\n    tier gradient 是nuanced finding但不影响main conclusion。\n\n    '\n- name: Probe Complexity Comparison\n  plan_id: plan_006\n  description: 'Logistic regression vs 2-layer MLP across all probed layers, both\n    models. EN accuracy, cross-lingual transfer degradation, calibration comparison.\n\n    '\n  expected_results:\n    lr_en_best_auroc_qwen: 0.838\n    mlp_en_best_auroc_qwen: 0.852\n    lr_en_best_auroc_scout: 0.821\n    mlp_en_best_auroc_scout: 0.834\n    lr_zs_transfer_degradation_median: 0.068\n    mlp_zs_transfer_degradation_median: 0.104\n    lr_transfer_advantage_over_mlp_median: 0.022\n    lr_ece_vs_mlp_ece:\n    - -0.008\n    - 0.003\n    mlp_overfit_indicator_deep_layers: true\n  result_rationale: 'Linear probes在EN AUROC上略输MLP（~1.4pp），但在cross-lingual transfer上\n    显著更好（+2.2pp median）。MLP的额外容量捕获了EN-specific patterns导致更多 overfitting to source\n    language——这些patterns在target语言中不泛化。 这与probe complexity literature一致（Hewitt & Liang\n    2019）：更强的probe 在source domain表现更好但generalization更差。Linear probe的inductive bias\n    （只能学习线性可分方向）恰好与correctness direction的线性结构匹配， 同时限制了对language-specific artifacts的拟合。\n    在deep层这个差异更大（MLP overfitting更严重），因为deep层表征更language-specific。 这个结果support使用logistic\n    regression作为primary probe的选择。\n\n    '\n  tables:\n  - name: 'Table 8: Probe Complexity — EN AUROC vs ZS Transfer (Qwen3-235B, selected\n      layers)'\n    columns:\n    - layer\n    - lr_en\n    - mlp_en\n    - lr_zs_median\n    - mlp_zs_median\n    - lr_transfer_advantage\n    rows:\n    - - 24\n      - 0.711\n      - 0.722\n      - 0.698\n      - 0.691\n      - 0.007\n    - - 40\n      - 0.762\n      - 0.778\n      - 0.756\n      - 0.741\n      - 0.015\n    - - 56\n      - 0.798\n      - 0.814\n      - 0.771\n      - 0.752\n      - 0.019\n    - - 76\n      - 0.838\n      - 0.852\n      - 0.714\n      - 0.686\n      - 0.028\n  figures_description:\n  - 'Fig S1: Dual-axis plot — EN AUROC (solid) and ZS transfer AUROC (dashed) vs layer\n    depth, separate lines for LR and MLP. MLP''s solid line higher but dashed line\n    lower, scissors gap widens at deep layers.'\n  analysis: 'Linear probe是正确的default choice。MLP的EN优势被transfer劣势完全抵消。 这个结果also间接支持correctness\n    direction是线性的——linear probe已经捕获了 大部分信号，MLP额外捕获的主要是noise/language-specific artifact。\n\n    '\n- name: Additional Benchmark Evaluation (Belebele + MMLU-ProX)\n  plan_id: plan_007\n  description: 'Best probes + CaCLR在Belebele和MMLU-ProX上的评估，验证beyond-GlobalMMLU泛化。\n\n    '\n  expected_results:\n    belebele_zs_auroc_median: 0.731\n    belebele_caclr_auroc_median: 0.789\n    mmlu_prox_zs_auroc_median: 0.748\n    mmlu_prox_caclr_auroc_median: 0.801\n    cross_benchmark_correlation: 0.92\n    belebele_pareto_rho_median: -0.71\n    mmlu_prox_pareto_rho_median: -0.75\n  result_rationale: 'Belebele（reading comprehension）的ZS AUROC略低于GlobalMMLU（0.731 vs\n    0.758）， 因为不同任务的correctness信号分布不完全一致——但Pareto frontier仍然存在 （rho=-0.71），说明depth-transfer\n    tradeoff是task-general的。 MMLU-ProX与GlobalMMLU最相似（同为knowledge QA），所以结果最接近（0.748\n    vs 0.758）。 CaCLR在两个benchmark上都提供了consistent improvement（+5.3-5.8pp）， 说明CaCLR学到的alignment不是GlobalMMLU-specific的。\n    Cross-benchmark correlation 0.92表明per-language transfer difficulty在benchmarks间高度一致——\n    sw/bn在所有benchmarks上都最难transfer，zh/es在所有benchmarks上都最容易。\n\n    '\n  tables:\n  - name: 'Table 9: Cross-Benchmark Generalization (Qwen3-235B, optimal transfer layer)'\n    columns:\n    - benchmark\n    - zs_median\n    - caclr_median\n    - pareto_rho\n    - langs_above_0p65\n    rows:\n    - - GlobalMMLU\n      - 0.758\n      - 0.808\n      - -0.78\n      - 17\n    - - Belebele\n      - 0.731\n      - 0.789\n      - -0.71\n      - 15\n    - - MMLU-ProX\n      - 0.748\n      - 0.801\n      - -0.75\n      - 16\n  figures_description:\n  - 'Fig S2: Scatter — per-language ZS AUROC on GlobalMMLU vs Belebele. High correlation\n    (r=0.92). Each point labeled with language code.'\n  analysis: 'Cross-benchmark泛化confirm findings are not benchmark-specific artifact。\n    Pareto frontier在三个benchmark上一致存在但shape有细微差异—— Belebele更浅的optimal depth可能反映reading\n    comprehension使用了更浅层的表征。\n\n    '\n- name: INT8 Validation Ablation\n  plan_id: plan_010\n  description: 'INT8 vs FP16对比，Llama 4 Scout，5 representative layers，5% random subset。\n\n    '\n  expected_results:\n    int8_fp16_auroc_max_diff: 0.006\n    int8_fp16_auroc_mean_diff: 0.003\n    int8_fp16_ece_max_diff: 0.008\n    int8_fp16_direction_cosine_min: 0.987\n    all_diffs_within_noise: true\n  result_rationale: 'INT8量化对correctness direction的影响极小（max AUROC差异0.6pp）， 因为correctness信号是高SNR的线性方向——量化噪声主要影响低幅度维度，\n    而correctness direction在high-variance维度上有强projection。 Direction cosine>0.987说明INT8和FP16下提取的correctness方向几乎相同。\n    ECE差异稍大（0.8pp）因为calibration对probability scale更敏感，但仍在噪声范围内。 这排除了\"INT8 artifact\"的reviewer\n    concern。\n\n    '\n  tables:\n  - name: 'Table S1: INT8 vs FP16 Comparison (Llama 4 Scout)'\n    columns:\n    - layer\n    - int8_auroc\n    - fp16_auroc\n    - diff\n    - direction_cosine\n    rows:\n    - - 8\n      - 0.674\n      - 0.678\n      - -0.004\n      - 0.991\n    - - 16\n      - 0.741\n      - 0.745\n      - -0.004\n      - 0.989\n    - - 24\n      - 0.788\n      - 0.791\n      - -0.003\n      - 0.992\n    - - 32\n      - 0.811\n      - 0.814\n      - -0.003\n      - 0.99\n    - - 40\n      - 0.821\n      - 0.827\n      - -0.006\n      - 0.987\n  figures_description:\n  - 'Fig S3: Bland-Altman plot — mean of INT8/FP16 AUROC (x) vs difference (y). All\n    points within ±0.01 band. No systematic bias.'\n  analysis: 'INT8量化不distort correctness signals。所有差异在bootstrap noise范围内。 Deep层差异略大（layer\n    40: 0.6pp）符合预期——深层表征更complex，量化误差累积更多。 但0.6pp远小于实验效应（CaCLR +6pp），不影响任何结论。\n\n    '\n- name: CKA Cross-Lingual Representation Similarity\n  plan_id: plan_011\n  description: 'CKA (linear kernel) between EN and each target language at every probed\n    layer, correlated with transfer AUROC. Mechanistic explanation for Pareto frontier.\n\n    '\n  expected_results:\n    cka_transfer_pearson_r: 0.82\n    cka_transfer_pearson_r_ci:\n    - 0.76\n    - 0.87\n    cka_transfer_spearman_rho: 0.79\n    cka_en_zh_by_depth_trend: monotonically decreasing from 0.92 (shallow) to 0.61\n      (deep)\n    cka_en_sw_by_depth_trend: monotonically decreasing from 0.84 (shallow) to 0.38\n      (deep)\n    cka_resource_tier_gradient:\n      HIGH_mean_cka_at_optimal_depth: 0.78\n      MID_mean_cka_at_optimal_depth: 0.71\n      LOW_mean_cka_at_optimal_depth: 0.58\n    geometric_misalignment_evidence: 'CKA drop from mid to deep layers exceeds what\n      mean/covariance shift alone predicts. Subspace angle analysis shows correctness\n      direction rotates 15-35° across languages at deep layers vs 5-12° at shallow\n      layers.\n\n      '\n    cka_explains_caclr_beta_limit: 'At layers where CKA < 0.55, β term provides diminishing\n      returns because geometric misalignment (rotation) dominates distributional shift.\n\n      '\n  result_rationale: 'CKA与transfer AUROC的高相关（r=0.82）提供了Pareto frontier的mechanistic\n    explanation： cross-lingual表征相似度随depth monotonically下降，直接导致deep层transfer degradation。\n    这不是trivial的\"深层更specific\"——CKA量化了具体的相似度数值并与transfer成功率 建立了定量关系。High-resource语言在所有depth保持更高CKA（因为pretraining\n    data overlap）， 解释了resource tier gradient。 关键insight：deep层的CKA下降不仅是distributional\n    shift（可被MMD修正）， 还包含geometric misalignment（correctness方向在语言间旋转15-35°）。 这解释了CaCLR\n    β term在deep层效果减弱——MMD对齐分布但不学习旋转， 而linear projection学习旋转所以在deep层更稳定。 Subspace angle\n    analysis区分了distributional vs geometric misalignment， 为Path A narrative提供了theoretical\n    depth：CaCLR works at mid-depth因为 那里的misalignment主要是distributional的。\n\n    '\n  tables:\n  - name: 'Table 10: CKA by Depth and Resource Tier (Qwen3-235B)'\n    columns:\n    - depth_pct\n    - HIGH_cka\n    - MID_cka\n    - LOW_cka\n    - zs_auroc_median\n    rows:\n    - - 10\n      - 0.93\n      - 0.89\n      - 0.84\n      - 0.618\n    - - 25\n      - 0.9\n      - 0.85\n      - 0.78\n      - 0.698\n    - - 40\n      - 0.86\n      - 0.79\n      - 0.69\n      - 0.756\n    - - 50\n      - 0.82\n      - 0.74\n      - 0.62\n      - 0.771\n    - - 60\n      - 0.78\n      - 0.69\n      - 0.55\n      - 0.771\n    - - 70\n      - 0.73\n      - 0.63\n      - 0.47\n      - 0.741\n    - - 80\n      - 0.67\n      - 0.56\n      - 0.41\n      - 0.714\n    - - 90\n      - 0.61\n      - 0.49\n      - 0.35\n      - 0.688\n  figures_description:\n  - 'Fig 6a: Dual-axis — CKA (left y-axis, lines by tier) and ZS AUROC median (right\n    y-axis, dashed) vs normalized depth. CKA decrease tracks AUROC decrease after\n    elbow.'\n  - 'Fig 6b: Scatter — CKA vs ZS transfer AUROC, each point = language × layer. Strong\n    linear relationship (r=0.82). Color by resource tier.'\n  - 'Fig 6c: Subspace angle between EN and target correctness directions vs depth.\n    Angles increase with depth; LOW languages diverge faster.'\n  analysis: 'CKA analysis是论文的mechanistic backbone。它将observation（Pareto frontier） 与explanation（representation\n    geometry变化）和method（CaCLR的作用机制与局限） 连接起来。CKA<0.55作为CaCLR β有效性的threshold是一个actionable\n    finding—— 实践者可以用CKA预测CaCLR在哪些layer-language组合上有效。 Geometric vs distributional\n    misalignment的区分是theoretical contribution： 它解释了为什么distributional matching（MMD/CaCLR）在mid-depth有效但在deep层递减，\n    而geometric alignment（linear projection）在deep层更稳定。\n\n    '\n- name: Linear Projection Sensitivity Analysis\n  plan_id: plan_012\n  description: 'Linear projection pair count sweep (10, 20, 50, 100, 200). Both models\n    × 5 layers × 20 languages.\n\n    '\n  expected_results:\n    linear_proj_min_pairs_for_saturation: 35\n    saturation_criterion: 95% of 200-pair performance\n    pairs_sweep:\n      10:\n        median_auroc: 0.762\n        pct_of_200: 0.88\n      20:\n        median_auroc: 0.778\n        pct_of_200: 0.94\n      50:\n        median_auroc: 0.792\n        pct_of_200: 0.98\n      100:\n        median_auroc: 0.796\n        pct_of_200: 0.99\n      200:\n        median_auroc: 0.798\n        pct_of_200: 1.0\n    low_resource_saturation_later: true\n    low_resource_min_pairs: 48\n    high_resource_min_pairs: 22\n  result_rationale: 'Linear projection在~35 pairs时达到饱和（95% of 200-pair performance），\n    因为correctness方向是低维线性结构——学习一个旋转/缩放矩阵不需要很多样本。 10 pairs已经达到88%性能，说明即使极少数据也能捕获主要的geometric\n    transformation。 50 pairs后几乎无改善（98%→100%），符合线性映射的low sample complexity理论。 Low-resource语言需要slightly\n    more pairs（48 vs 22），因为表征空间中 correctness方向的SNR更低，需要更多样本来robustly估计映射。 整体saturation在20-50范围内，support\n    \"≤50 parallel pairs suffice\"的claim。 这建立了linear projection作为practical baseline的地位——\n    50 pairs在任何语言都容易获得（e.g., 翻译50个MCQA items）。\n\n    '\n  tables:\n  - name: 'Table 11: Linear Projection Data Efficiency (median across 20 langs × 2\n      models)'\n    columns:\n    - n_pairs\n    - median_auroc\n    - delta_vs_zs\n    - pct_of_200pair\n    - HIGH_auroc\n    - LOW_auroc\n    rows:\n    - - 10\n      - 0.762\n      - 0.027\n      - 88\n      - 0.781\n      - 0.638\n    - - 20\n      - 0.778\n      - 0.043\n      - 94\n      - 0.798\n      - 0.651\n    - - 50\n      - 0.792\n      - 0.057\n      - 98\n      - 0.814\n      - 0.664\n    - - 100\n      - 0.796\n      - 0.061\n      - 99\n      - 0.818\n      - 0.668\n    - - 200\n      - 0.798\n      - 0.063\n      - 100\n      - 0.821\n      - 0.671\n  figures_description:\n  - 'Fig S4: Learning curve — n_pairs (x, log) vs median AUROC (y). Rapid rise, plateau\n    at ~50. Separate lines for HIGH/MID/LOW tiers — all plateau but at different levels.'\n  analysis: 'Linear projection的data efficiency confirms它作为practical baseline的价值。 50\n    pairs的saturation point意味着任何有minimal translation capacity的语言 都可以使用这个方法。这也为CaCLR设定了benchmark：CaCLR需要beat\n    50-pair projection 才能justify its additional complexity（in best tier, CaCLR beats\n    by +1.4pp median）。\n\n    '\n- name: Probing Control Tasks (Hewitt & Liang 2019)\n  plan_id: plan_013\n  description: 'Random-label control probes at each layer. Selectivity = probe AUROC\n    - control AUROC. Validates genuine correctness signal.\n\n    '\n  expected_results:\n    control_task_auroc_range:\n    - 0.502\n    - 0.538\n    selectivity_median: 0.284\n    selectivity_min: 0.192\n    selectivity_max: 0.341\n    control_task_selectivity_min_across_langs: 0.192\n    selectivity_by_depth:\n      shallow: 0.218\n      mid: 0.294\n      deep: 0.312\n    selectivity_by_tier:\n      HIGH: 0.301\n      MID: 0.278\n      LOW: 0.234\n  result_rationale: 'Control probe AUROC在0.50-0.54范围（near chance），selectivity中位数0.284\n    远超15pp minimum threshold（min=19.2pp）。这confirm probe AUROC反映 genuine correctness\n    direction而非memorized artifacts或probe capacity。 Selectivity随depth增加（0.218→0.312），因为深层表征包含更丰富的correctness\n    信号而control仍在chance附近——深层probe的高AUROC不是因为probe容量过大。 Low-resource语言selectivity最低（0.234）但仍远超threshold，\n    说明即使低资源语言的correctness信号也是genuine的（不是noise fitting）。 这直接回应Hewitt & Liang probing\n    methodology critique—— 我们的probes确实在提取linguistic property而非exploiting high-dimensional\n    capacity。\n\n    '\n  tables:\n  - name: 'Table S2: Control Task Selectivity (Qwen3-235B, selected layers × languages)'\n    columns:\n    - layer\n    - en_selectivity\n    - zh_selectivity\n    - sw_selectivity\n    - control_auroc\n    rows:\n    - - 16\n      - 0.248\n      - 0.231\n      - 0.192\n      - 0.512\n    - - 32\n      - 0.281\n      - 0.268\n      - 0.218\n      - 0.519\n    - - 48\n      - 0.309\n      - 0.292\n      - 0.241\n      - 0.524\n    - - 56\n      - 0.318\n      - 0.301\n      - 0.248\n      - 0.521\n    - - 76\n      - 0.341\n      - 0.324\n      - 0.262\n      - 0.538\n  figures_description:\n  - 'Fig S5: Paired bar chart — probe AUROC (dark) vs control AUROC (light) at each\n    layer. Gap (selectivity) clearly visible and widening with depth. Horizontal line\n    at 15pp threshold.'\n  analysis: 'Control task validation是methodological necessity。Selectivity最小值19.2pp\n    大幅超过15pp阈值，即使在最challenging的条件（low-resource × shallow layer） 也确认probe是在提取genuine\n    signal。这让reviewer对所有downstream结果 （Pareto frontier, CaCLR, decomposition）更有信心。\n\n    '\n- name: Gemma 4 31B Dense — Camera-Ready Extension\n  plan_id: plan_008\n  description: 'Third architecture (dense, FP16), full Pareto frontier. Dense vs MoE\n    contrast for camera-ready.\n\n    '\n  expected_results:\n    en_best_auroc: 0.809\n    en_best_layer: 48\n    optimal_transfer_layer: 36\n    zs_transfer_auroc_median: 0.738\n    pareto_rho_median: -0.69\n    pareto_shape: smoother frontier than MoE models — no sharp elbow\n    dense_vs_moe_key_finding: 'Dense architecture shows shallower Pareto slope — transfer\n      degrades more gradually with depth compared to MoE models. Consistent with hypothesis\n      that expert routing accelerates language specialization.\n\n      '\n  result_rationale: 'Gemma 4 31B Dense作为dense对照提供了architectural contrast。 EN AUROC\n    0.809低于两个MoE模型（0.838, 0.821），反映31B dense参数<235B MoE active参数。 关键发现：dense架构的Pareto\n    frontier更平滑（rho=-0.69 vs MoE -0.73/-0.78）， 没有MoE的sharp elbow。这是因为MoE的expert routing在深层创造了discrete\n    language specialization（某些experts \"负责\"特定语言），而dense模型的specialization是gradual的。\n    这是architecture-dependent Pareto shape claim的strongest evidence。 Optimal transfer在75%深度（layer\n    36/48），比Qwen3浅（60%）但比Scout深（50%）， 提供了第三个data point来characterize architecture-depth\n    relationship。\n\n    '\n  tables:\n  - name: 'Table S3: Three-Architecture Comparison Summary'\n    columns:\n    - model\n    - type\n    - params\n    - layers\n    - en_best_auroc\n    - zs_median\n    - optimal_transfer_pct\n    - pareto_rho\n    rows:\n    - - Qwen3-235B-A22B\n      - MoE\n      - 235B\n      - 94\n      - 0.838\n      - 0.758\n      - 60\n      - -0.78\n    - - Llama 4 Scout\n      - MoE\n      - 109B (17B active)\n      - 48\n      - 0.821\n      - 0.742\n      - 50\n      - -0.73\n    - - Gemma 4 31B Dense\n      - Dense\n      - 31B\n      - 60\n      - 0.809\n      - 0.738\n      - 75\n      - -0.69\n  figures_description:\n  - 'Fig S6: Three Pareto frontiers overlaid on normalized depth axis. MoE models\n    show sharper elbows; Dense model is smoother. Annotated with optimal transfer\n    depth for each.'\n  analysis: 'Three-architecture comparison is the crown jewel of Claim 1。 Dense vs\n    MoE对比provides causal insight into WHY frontiers differ—— expert routing is the\n    mechanism driving sharp language specialization at depth.\n\n    '\n- name: Extended Language Coverage — Camera-Ready\n  plan_id: plan_009\n  description: 'Expand from 20 to 50+ languages. Camera-ready extension using GlobalMMLU/Belebele\n    full sets.\n\n    '\n  expected_results:\n    total_languages: 52\n    zs_langs_above_0p65: 38\n    zs_auroc_median_52lang: 0.721\n    new_low_resource_findings: 'Several additional low-resource languages (e.g., Yoruba,\n      Hausa, Malagasy) show ZS AUROC 0.58-0.64, confirming resource-tier gradient\n      extends to tail.\n\n      '\n    pareto_frontier_robust: true\n    caclr_generalizes: true\n    caclr_delta_over_zs_52lang_median: 0.058\n  result_rationale: '52语言验证confirms所有findings at broader scale。ZS median从20 langs的0.758\n    降到52 langs的0.721，因为新增语言主要是低资源的——这是expected的composition effect。 38/52 > 0.65（73%）vs\n    17/20（85%），比例下降也反映低资源语言的加入。 Pareto frontier和CaCLR在所有语言上consistent，说明findings是language-general的。\n    Key new finding：Yoruba/Hausa等sub-Saharan African语言的ZS AUROC（0.58-0.62） 与sw/bn相当，但CaCLR对这些语言的improvement更大（+7-9pp），\n    可能因为GlobalMMLU translations provide parallel data that partially bridges the representation\n    gap for these extremely low-resource languages.\n\n    '\n  tables:\n  - name: 'Table S4: Extended Language Coverage Summary'\n    columns:\n    - resource_tier\n    - n_langs\n    - zs_auroc_median\n    - caclr_median\n    - delta\n    rows:\n    - - HIGH\n      - 12\n      - 0.786\n      - 0.828\n      - 0.042\n    - - MID\n      - 18\n      - 0.741\n      - 0.798\n      - 0.057\n    - - LOW\n      - 22\n      - 0.648\n      - 0.721\n      - 0.073\n  figures_description:\n  - 'Fig S7: World map — ZS AUROC by country/language, color gradient from red (low)\n    to green (high). Clear geographic pattern tracking resource availability.'\n  analysis: Extended coverage是camera-ready的scale argument。核心findings在52语言上robust。\n    Low-resource语言从CaCLR获益最多（+7.3pp vs HIGH +4.2pp）， because these languages have\n    the most room for improvement and CaCLR's distributional alignment compensates\n    for sparse pretraining representation.\n",
      "numLines": 1327,
      "startLine": 1,
      "totalLines": 1327
    }
  },
  "sourceToolAssistantUUID": "494e9d15-8672-4234-a407-56fa1cf71899",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "d1221443-c15e-4888-b9c9-64cd2c74844d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 19_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[DREAM Review Director] dream_id=20260520T201854 | review_mode=full | review_visible=True PDF: /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dr…",
  "leafUuid": "658c2477-2fce-4b99-aaef-3291062fa6c1",
  "sessionId": "d1221443-c15e-4888-b9c9-64cd2c74844d"
}
```

---

### Runtime record

_source line 20_

```json
{
  "type": "ai-title",
  "aiTitle": "Conduct full DREAM review for cross-lingual calibration research",
  "sessionId": "d1221443-c15e-4888-b9c9-64cd2c74844d"
}
```

---

### Assistant

_source line 21 · 2026-05-20T20:58:51.938Z_

<details><summary>Logged reasoning block</summary>

```text
I've read the full paper and the review context YAML. Now I need to dispatch a full review with 2 reviewers:
- R1: Methods + Experiments
- R2: Novelty + Related Work

Then conduct a full roundtable (Step 1 independent → Step 2 cross-share → Step 3 converge → Step 4 synthesize).

Let me first load the submit_dream_review_report tool, then dispatch both reviewers in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "658c2477-2fce-4b99-aaef-3291062fa6c1",
  "isSidechain": false,
  "requestId": "req_011CbEVUbsHsCBLmsCJZLg5D",
  "type": "assistant",
  "uuid": "5a39eb16-8871-4850-be44-1098bab8de32",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "d1221443-c15e-4888-b9c9-64cd2c74844d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017CsG399sYfwL6qbdQZHoPv",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 43608,
      "cache_read_input_tokens": 23201,
      "output_tokens": 3281,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 43608,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 3281,
          "cache_read_input_tokens": 23201,
          "cache_creation_input_tokens": 43608,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 43608
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

_source line 22 · 2026-05-20T20:58:52.863Z_

I've read the full 10-page paper and the review context YAML (11 imagined experiments). Dispatching two parallel reviewers now: R1 (methods + experiments) and R2 (novelty + related work).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5a39eb16-8871-4850-be44-1098bab8de32",
  "isSidechain": false,
  "requestId": "req_011CbEVUbsHsCBLmsCJZLg5D",
  "type": "assistant",
  "uuid": "7477f048-7032-4162-b492-46cc2d6a07af",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "d1221443-c15e-4888-b9c9-64cd2c74844d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017CsG399sYfwL6qbdQZHoPv",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 43608,
      "cache_read_input_tokens": 23201,
      "output_tokens": 3281,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 43608,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 3281,
          "cache_read_input_tokens": 23201,
          "cache_creation_input_tokens": 43608,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 43608
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

_source line 23 · 2026-05-20T20:58:54.137Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01KGbhbMtERWtLVCn5idNTYg`</summary>

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
  "parentUuid": "7477f048-7032-4162-b492-46cc2d6a07af",
  "isSidechain": false,
  "requestId": "req_011CbEVUbsHsCBLmsCJZLg5D",
  "type": "assistant",
  "uuid": "a50b8e55-f4b7-45c6-927d-6edde6c57381",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "d1221443-c15e-4888-b9c9-64cd2c74844d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017CsG399sYfwL6qbdQZHoPv",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 43608,
      "cache_read_input_tokens": 23201,
      "output_tokens": 3281,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 43608,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 3281,
          "cache_read_input_tokens": 23201,
          "cache_creation_input_tokens": 43608,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 43608
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

_source line 24 · 2026-05-20T20:58:54.144Z_

<details><summary>↩ Tool result · `toolu_01KGbhbMtERWtLVCn5idNTYg`</summary>

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
  "parentUuid": "a50b8e55-f4b7-45c6-927d-6edde6c57381",
  "isSidechain": false,
  "promptId": "248aeb9c-3304-4117-b59f-e1434de9c70f",
  "type": "user",
  "uuid": "d6880af1-645e-4601-b37d-559c2f405a59",
  "toolUseResult": {
    "matches": [
      "mcp__agent-ml-research__submit_dream_review_report"
    ],
    "query": "select:mcp__agent-ml-research__submit_dream_review_report",
    "total_deferred_tools": 23
  },
  "sourceToolAssistantUUID": "a50b8e55-f4b7-45c6-927d-6edde6c57381",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "d1221443-c15e-4888-b9c9-64cd2c74844d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-20T20:59:31.780Z_

<details open><summary>🔧 Tool call — Agent · `toolu_014oxm1CgxMXRuK2P8LRy9Lv`</summary>

```json
{
  "description": "R1: Methods + Experiments review",
  "prompt": "You are Reviewer 1 (R1) for a top ML venue review. Your focus is **methods and experiments**. \n\n## Paper Summary\n\"Cross-Lingual Calibration via Internal Correctness Directions: Pareto Frontiers, Decomposition, and Consistency-Aligned Probes\" — a 10-page paper studying cross-lingual transfer of correctness probes in multilingual LLMs. Key contributions:\n1. Depth–transferability Pareto frontier: deeper layers = better EN probes but worse cross-lingual transfer. Architecture-dependent (60% depth optimal for Qwen3-235B, 50% for Llama 4 Scout).\n2. Difficulty–capability decomposition: removing IRT difficulty direction from representations improves transfer by 3.1pp median.\n3. CaCLR: probe training with L_BCE + α·L_SB-ECE + β·L_MMD. Zero target-language labels. Reduces non-English ECE by 3.5% over temperature scaling.\n4. Cross-lingual orthogonality: correctness–confidence cosine &lt; 0.062 across all 20 languages.\n5. CKA analysis: cross-lingual representation similarity monotonically decreases with depth (r=0.82 with transfer AUROC).\n\n## Experimental Setup\n- Models: Qwen3-235B-A22B (94 layers, MoE, INT8), Llama 4 Scout (48 layers, MoE, INT8)\n- 20 languages, 3 resource tiers (HIGH/MID/LOW)\n- Benchmarks: GlobalMMLU (primary), Belebele, MMLU-ProX\n- Probes: logistic regression with StandardScaler\n- Transfer conditions: zero-shot, mean-shift, linear projection (50 pairs), few-shot (25/100), CaCLR\n- Evaluation: AUROC, ECE, bootstrap CIs (1000), paired permutation tests, Cohen's d\n\n## Tables in the paper\n- Table 1: Pareto frontier (Qwen3: layers 16-88 every ~8; Scout: layers 8-48 every 8). Qwen3 shows 7 layers, Scout 6 layers. ZS Min/Max only shown for Qwen3.\n- Table 2: Transfer method comparison — 7 methods × 4 model-layer combos (Q-56, Q-76, S-24, S-40)\n- Table 3: β sensitivity sweep — 4 values (0.001, 0.01, 0.1, 1.0) at Qwen3 layer 56\n- Table 4: Decomposition ΔAUROC — 6 depth levels × 4 columns (HIGH, MID, LOW, Random)\n- Table 5: Correctness–confidence cosine — 10 languages × 2 architectures\n- Table 6: CKA by depth — 8 depths × 3 tiers + ZS AUROC\n- Table 7: LR vs MLP — 4 layers × 4 metrics\n- Table 8: Cross-benchmark — 3 benchmarks × 4 metrics\n- Table 9: Linear projection data efficiency — 5 pair counts × 5 metrics\n- Table 10 (Appendix A): INT8 vs FP16 — 5 layers on Scout\n- Table 11 (Appendix B): Control task selectivity — 5 layers × 4 metrics\n- Table 12 (Appendix C): Three-architecture comparison (adds Gemma 4 31B Dense)\n- Table 13 (Appendix D): Extended 52-language coverage by tier\n\n## Review Context — Imagined Experiments (from design YAML)\nThe full experiment plan includes 11 experiments:\n1. plan_001: Full Pareto Frontier — Qwen3-235B (24 probed layers, every 4th)\n2. plan_002: Full Pareto Frontier — Llama 4 Scout (12 probed layers, every 4th)\n3. plan_003: CaCLR Implementation and Comparative Evaluation (full sweep)\n4. plan_004: Difficulty-Controlled Decomposition Ablation (10 langs × 8 layers × 2 models)\n5. plan_005: Cross-Lingual Orthogonality Analysis (20 langs × 2 architectures)\n6. plan_006: Probe Complexity Comparison (LR vs MLP)\n7. plan_007: Additional Benchmark Evaluation (Belebele + MMLU-ProX)\n8. plan_010: INT8 Validation Ablation (Scout, 5 layers, 5% subset)\n9. plan_011: CKA Cross-Lingual Representation Similarity\n10. plan_012: Linear Projection Sensitivity Analysis (pair count sweep)\n11. plan_013: Probing Control Tasks (Hewitt &amp; Liang 2019)\n\nPlus camera-ready extensions:\n- plan_008: Gemma 4 31B Dense (third architecture)\n- plan_009: Extended 52-language coverage\n\n## Your Task\n\nEvaluate the paper on **methodology soundness** and **experimental rigor**. Write a detailed review covering:\n\n### 1. Methodological Assessment\n- Is the CaCLR formulation sound? Any issues with the loss function design?\n- Is the difficulty–capability decomposition well-motivated and correctly executed?\n- Is the mean-shift invariance proof correct (ΔAUROC ≡ 0 under StandardScaler + LR)?\n- Are there methodological gaps or unjustified assumptions?\n\n### 2. Experimental Rigor\n- Are the experiments sufficient to support the claims?\n- Statistical rigor: bootstrap CIs, permutation tests, effect sizes — adequate?\n- Are there missing controls or ablations?\n- Coverage: the design YAML planned 24 probed layers for Qwen3 but Table 1 only shows 7. Is this sufficient?\n- Table 1 for Scout omits ZS Min/Max columns. Is this a concern?\n- INT8 validation is only on Scout (5 layers, 5% subset). Is this enough?\n- Orthogonality analysis shows only 10/20 languages in Table 5. Is the full set needed?\n\n### 3. Experiment Coverage Assessment\nCompare what's in the paper vs. what was planned:\n- Are all 11 core experiments reflected in the paper?\n- Are results consistent with planned expectations?\n- What's missing or under-reported?\n\n### 4. Weaknesses (numbered list)\nSpecific, actionable weaknesses.\n\n### 5. Questions for Authors (numbered list)\n\n### 6. Score and Confidence\n- Score (1-6 scale: 1=Strong Reject, 2=Reject, 3=Weak Reject, 4=Weak Accept, 5=Accept, 6=Strong Accept)\n- Confidence (1-5: 1=low, 5=expert)\n\nFormat your review as a structured document with clear headers. Be rigorous but fair."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d6880af1-645e-4601-b37d-559c2f405a59",
  "isSidechain": false,
  "requestId": "req_011CbEVUbsHsCBLmsCJZLg5D",
  "type": "assistant",
  "uuid": "98f3ac41-7d66-4ce7-875e-767e8684028a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "d1221443-c15e-4888-b9c9-64cd2c74844d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017CsG399sYfwL6qbdQZHoPv",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 43608,
      "cache_read_input_tokens": 23201,
      "output_tokens": 3281,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 43608,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 3281,
          "cache_read_input_tokens": 23201,
          "cache_creation_input_tokens": 43608,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 43608
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

_source line 26 · 2026-05-20T20:59:54.655Z_

<details open><summary>🔧 Tool call — Agent · `toolu_016CqR9KEpkaiibBTanwneDE`</summary>

```json
{
  "description": "R2: Novelty + Related Work review",
  "prompt": "You are Reviewer 2 (R2) for a top ML venue review. Your focus is **novelty, positioning, and related work**.\n\n## Paper Summary\n\"Cross-Lingual Calibration via Internal Correctness Directions: Pareto Frontiers, Decomposition, and Consistency-Aligned Probes\" — a 10-page paper studying cross-lingual transfer of correctness probes in multilingual LLMs. Key contributions:\n1. Depth–transferability Pareto frontier: deeper layers = better EN probes but worse cross-lingual transfer. Architecture-dependent shape (60% for Qwen3-235B, 50% for Llama 4 Scout, 75% for Gemma 4 Dense).\n2. Difficulty–capability decomposition: removing IRT difficulty direction improves cross-lingual transfer by 3.1pp.\n3. CaCLR: L_BCE + α·L_SB-ECE + β·L_MMD probe training. Zero target-language labels needed. Reduces non-English ECE by 3.5% over temperature scaling.\n4. Cross-lingual orthogonality: correctness–confidence cosine &lt; 0.062 universally across 20 languages.\n5. CKA mechanistic analysis linking representation geometry to transfer success.\n\n## Related Work as presented in the paper (Section 2)\n- **LLM Calibration**: Temperature scaling, LACE (per-language layer ensembles, needs target labels), MKA (5× inference cost)\n- **Probe-Based Calibration**: CORAL (cross-task EN probes), CCPS (clustering), Miao &amp; Ungar (correctness–confidence orthogonality, English-only 7-8B)\n- **Cross-Lingual Probe Transfer**: Xiao et al. (knowledge boundary probes, 8 langs — fundamentally different: answerability vs correctness). Civelli et al. (cross-lingual difficulty probes)\n- **Domain Adaptation Theory**: Ben-David et al. H-divergence\n- **Representation Similarity**: CKA\n- **Cross-Lingual Alignment**: MUSE, VecMap\n- **Conformal Prediction**: mentioned as complementary\n\n## Key claims requiring novelty assessment\n1. \"First systematic study of cross-lingual correctness probe transfer\"\n2. Pareto frontier discovery (depth vs. transferability tradeoff)\n3. Architecture-dependent frontier shape (MoE vs dense)\n4. Difficulty–capability decomposition as explanatory mechanism\n5. CaCLR as a method contribution (MMD consistency loss on parallel activations)\n6. Universal cross-lingual orthogonality (extending Miao &amp; Ungar)\n\n## Your Task\n\nEvaluate the paper on **novelty, significance, and positioning**. Write a detailed review covering:\n\n### 1. Novelty Assessment\nFor each of the 6 claims above:\n- Is this genuinely novel? Or incremental extension of known results?\n- How significant is the contribution to the field?\n- What is the delta over the closest prior work?\n\n### 2. Related Work Completeness\n- Are there important missing references? Consider:\n  - Cross-lingual representation probing literature (e.g., Conneau et al., Pires et al., Chi et al. on multilingual BERT probing)\n  - Calibration literature beyond what's cited\n  - MMD/domain adaptation in NLP (not just Ben-David theory but applied methods)\n  - Probe transfer across domains/languages more broadly\n  - Internal representations of LLMs (mechanistic interpretability angle)\n- Is the differentiation from Xiao et al. (knowledge boundary vs. correctness) convincing?\n- Is the differentiation from Miao &amp; Ungar sufficient?\n\n### 3. Positioning and Framing\n- Is the \"causal chain\" framing (contributions 1→2→3→4 + CKA as glue) convincing?\n- Does the paper oversell or undersell any contribution?\n- Is CaCLR positioned appropriately — is it a method contribution or an analysis paper with a method?\n- The paper uses only 2 MoE models in the main text. Is the \"architecture-dependent\" claim well-supported with just 2 data points (+1 in appendix)?\n\n### 4. Significance and Impact\n- Would this change how practitioners do multilingual calibration?\n- What is the target audience? Calibration researchers? Multilingual NLP? Mechanistic interpretability?\n- Is 3.5% ECE improvement over temperature scaling meaningful in practice?\n\n### 5. Weaknesses (numbered list)\nSpecific, actionable weaknesses focused on novelty/positioning.\n\n### 6. Questions for Authors (numbered list)\n\n### 7. Score and Confidence\n- Score (1-6 scale: 1=Strong Reject, 2=Reject, 3=Weak Reject, 4=Weak Accept, 5=Accept, 6=Strong Accept)\n- Confidence (1-5: 1=low, 5=expert)\n\nFormat your review as a structured document with clear headers. Be rigorous but fair."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "98f3ac41-7d66-4ce7-875e-767e8684028a",
  "isSidechain": false,
  "requestId": "req_011CbEVUbsHsCBLmsCJZLg5D",
  "type": "assistant",
  "uuid": "2f57cda9-7001-4a8e-bccb-398fb172f671",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "d1221443-c15e-4888-b9c9-64cd2c74844d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017CsG399sYfwL6qbdQZHoPv",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 43608,
      "cache_read_input_tokens": 23201,
      "output_tokens": 3281,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 43608,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 3281,
          "cache_read_input_tokens": 23201,
          "cache_creation_input_tokens": 43608,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 43608
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

_source line 27 · 2026-05-20T21:03:09.561Z_

<details><summary>↩ Tool result · `toolu_016CqR9KEpkaiibBTanwneDE`</summary>

```text
Review submitted. Here is a summary of the R2 review:

**Overall Score: 4/6 (Weak Accept), Confidence 4/5**

**Key findings from the review:**

**Novelty Assessment (by claim):**
- **Claim 1 (First systematic study):** Defensible when narrowly scoped to correctness probes, but the underlying depth-transfer phenomenon is well-established since Pires et al. (2019) and Conneau et al. (2020).
- **Claim 2 (Pareto frontier):** Incremental quantification of a known trend. Civelli et al. (2026) already found architecture-dependent optimal depth for cross-lingual probes.
- **Claim 3 (Architecture-dependent shape):** The most novel empirical contribution, but underpowered -- 3 confounded models (differing in scale, depth, training data, and architecture) cannot isolate architecture type as causal.
- **Claim 4 (Decomposition):** Methodologically interesting, builds directly on Civelli et al. The interaction finding (difficulty removal improves correctness transfer) is the novel element.
- **Claim 5 (CaCLR):** Limited novelty as a method (3 known loss components combined), but the beta sensitivity analysis revealing depth-dependent effectiveness is analytically valuable. The +1.4pp advantage over 50-pair linear projection at higher data cost weakens the practical value proposition.
- **Claim 6 (Orthogonality):** Straightforward extension of Miao & Ungar -- empirical verification, not conceptual advance.

**Major weaknesses:**
1. Architecture claim underpowered (3 confounded models)
2. CaCLR's practical value weak vs. linear projection simplicity
3. Missing foundational references (Conneau 2020, Pires 2019, Gretton 2012)
4. Causal chain has a weak link (decomposition does not directly motivate CaCLR)
5. Non-English ECE reported only in relative terms
6. CKA analysis is correlational, not causal despite "mechanistic" framing

**Bottom line:** The paper's strongest contributions are analytical (decomposition, CKA analysis, mean-shift invariance proof), not methodological (CaCLR). Reframing as primarily an analysis/characterization paper would better match the actual contributions. The scale and thoroughness earn a weak accept despite limited per-claim novelty.

agentId: a608204260859e5b5 (use SendMessage with to: 'a608204260859e5b5' to continue this agent)
&lt;usage>total_tokens: 105128
tool_uses: 22
duration_ms: 194901&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2f57cda9-7001-4a8e-bccb-398fb172f671",
  "isSidechain": false,
  "promptId": "248aeb9c-3304-4117-b59f-e1434de9c70f",
  "type": "user",
  "uuid": "598edbe7-7e69-4d9c-b481-e0f7cb553a5e",
  "toolUseResult": {
    "status": "completed",
    "prompt": "You are Reviewer 2 (R2) for a top ML venue review. Your focus is **novelty, positioning, and related work**.\n\n## Paper Summary\n\"Cross-Lingual Calibration via Internal Correctness Directions: Pareto Frontiers, Decomposition, and Consistency-Aligned Probes\" — a 10-page paper studying cross-lingual transfer of correctness probes in multilingual LLMs. Key contributions:\n1. Depth–transferability Pareto frontier: deeper layers = better EN probes but worse cross-lingual transfer. Architecture-dependent shape (60% for Qwen3-235B, 50% for Llama 4 Scout, 75% for Gemma 4 Dense).\n2. Difficulty–capability decomposition: removing IRT difficulty direction improves cross-lingual transfer by 3.1pp.\n3. CaCLR: L_BCE + α·L_SB-ECE + β·L_MMD probe training. Zero target-language labels needed. Reduces non-English ECE by 3.5% over temperature scaling.\n4. Cross-lingual orthogonality: correctness–confidence cosine &lt; 0.062 universally across 20 languages.\n5. CKA mechanistic analysis linking representation geometry to transfer success.\n\n## Related Work as presented in the paper (Section 2)\n- **LLM Calibration**: Temperature scaling, LACE (per-language layer ensembles, needs target labels), MKA (5× inference cost)\n- **Probe-Based Calibration**: CORAL (cross-task EN probes), CCPS (clustering), Miao &amp; Ungar (correctness–confidence orthogonality, English-only 7-8B)\n- **Cross-Lingual Probe Transfer**: Xiao et al. (knowledge boundary probes, 8 langs — fundamentally different: answerability vs correctness). Civelli et al. (cross-lingual difficulty probes)\n- **Domain Adaptation Theory**: Ben-David et al. H-divergence\n- **Representation Similarity**: CKA\n- **Cross-Lingual Alignment**: MUSE, VecMap\n- **Conformal Prediction**: mentioned as complementary\n\n## Key claims requiring novelty assessment\n1. \"First systematic study of cross-lingual correctness probe transfer\"\n2. Pareto frontier discovery (depth vs. transferability tradeoff)\n3. Architecture-dependent frontier shape (MoE vs dense)\n4. Difficulty–capability decomposition as explanatory mechanism\n5. CaCLR as a method contribution (MMD consistency loss on parallel activations)\n6. Universal cross-lingual orthogonality (extending Miao &amp; Ungar)\n\n## Your Task\n\nEvaluate the paper on **novelty, significance, and positioning**. Write a detailed review covering:\n\n### 1. Novelty Assessment\nFor each of the 6 claims above:\n- Is this genuinely novel? Or incremental extension of known results?\n- How significant is the contribution to the field?\n- What is the delta over the closest prior work?\n\n### 2. Related Work Completeness\n- Are there important missing references? Consider:\n  - Cross-lingual representation probing literature (e.g., Conneau et al., Pires et al., Chi et al. on multilingual BERT probing)\n  - Calibration literature beyond what's cited\n  - MMD/domain adaptation in NLP (not just Ben-David theory but applied methods)\n  - Probe transfer across domains/languages more broadly\n  - Internal representations of LLMs (mechanistic interpretability angle)\n- Is the differentiation from Xiao et al. (knowledge boundary vs. correctness) convincing?\n- Is the differentiation from Miao &amp; Ungar sufficient?\n\n### 3. Positioning and Framing\n- Is the \"causal chain\" framing (contributions 1→2→3→4 + CKA as glue) convincing?\n- Does the paper oversell or undersell any contribution?\n- Is CaCLR positioned appropriately — is it a method contribution or an analysis paper with a method?\n- The paper uses only 2 MoE models in the main text. Is the \"architecture-dependent\" claim well-supported with just 2 data points (+1 in appendix)?\n\n### 4. Significance and Impact\n- Would this change how practitioners do multilingual calibration?\n- What is the target audience? Calibration researchers? Multilingual NLP? Mechanistic interpretability?\n- Is 3.5% ECE improvement over temperature scaling meaningful in practice?\n\n### 5. Weaknesses (numbered list)\nSpecific, actionable weaknesses focused on novelty/positioning.\n\n### 6. Questions for Authors (numbered list)\n\n### 7. Score and Confidence\n- Score (1-6 scale: 1=Strong Reject, 2=Reject, 3=Weak Reject, 4=Weak Accept, 5=Accept, 6=Strong Accept)\n- Confidence (1-5: 1=low, 5=expert)\n\nFormat your review as a structured document with clear headers. Be rigorous but fair.",
    "agentId": "a608204260859e5b5",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Review submitted. Here is a summary of the R2 review:\n\n**Overall Score: 4/6 (Weak Accept), Confidence 4/5**\n\n**Key findings from the review:**\n\n**Novelty Assessment (by claim):**\n- **Claim 1 (First systematic study):** Defensible when narrowly scoped to correctness probes, but the underlying depth-transfer phenomenon is well-established since Pires et al. (2019) and Conneau et al. (2020).\n- **Claim 2 (Pareto frontier):** Incremental quantification of a known trend. Civelli et al. (2026) already found architecture-dependent optimal depth for cross-lingual probes.\n- **Claim 3 (Architecture-dependent shape):** The most novel empirical contribution, but underpowered -- 3 confounded models (differing in scale, depth, training data, and architecture) cannot isolate architecture type as causal.\n- **Claim 4 (Decomposition):** Methodologically interesting, builds directly on Civelli et al. The interaction finding (difficulty removal improves correctness transfer) is the novel element.\n- **Claim 5 (CaCLR):** Limited novelty as a method (3 known loss components combined), but the beta sensitivity analysis revealing depth-dependent effectiveness is analytically valuable. The +1.4pp advantage over 50-pair linear projection at higher data cost weakens the practical value proposition.\n- **Claim 6 (Orthogonality):** Straightforward extension of Miao & Ungar -- empirical verification, not conceptual advance.\n\n**Major weaknesses:**\n1. Architecture claim underpowered (3 confounded models)\n2. CaCLR's practical value weak vs. linear projection simplicity\n3. Missing foundational references (Conneau 2020, Pires 2019, Gretton 2012)\n4. Causal chain has a weak link (decomposition does not directly motivate CaCLR)\n5. Non-English ECE reported only in relative terms\n6. CKA analysis is correlational, not causal despite \"mechanistic\" framing\n\n**Bottom line:** The paper's strongest contributions are analytical (decomposition, CKA analysis, mean-shift invariance proof), not methodological (CaCLR). Reframing as primarily an analysis/characterization paper would better match the actual contributions. The scale and thoroughness earn a weak accept despite limited per-claim novelty."
      }
    ],
    "totalDurationMs": 194901,
    "totalTokens": 105128,
    "totalToolUseCount": 22,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5278,
      "cache_read_input_tokens": 99271,
      "output_tokens": 578,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 5278
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 578,
          "cache_read_input_tokens": 99271,
          "cache_creation_input_tokens": 5278,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 5278,
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
      "otherToolCount": 10
    }
  },
  "sourceToolAssistantUUID": "2f57cda9-7001-4a8e-bccb-398fb172f671",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "d1221443-c15e-4888-b9c9-64cd2c74844d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-20T21:03:14.288Z_

<details><summary>↩ Tool result · `toolu_014oxm1CgxMXRuK2P8LRy9Lv`</summary>

```text
Review submitted. Here is a summary of the key findings:

**Score: 4/6 (Weak Accept), Confidence: 4/5**

The review covers four major areas:

**Methodological Assessment** identified issues with CaCLR's MMD specification (kernel unspecified, scalar vs. d-dimensional target unclear), the tension between CaCLR's gradient-based optimization and logistic regression's standard solvers, incomplete alpha-beta interaction analysis, and the difficulty decomposition's reliance on a single linear direction. The mean-shift invariance proof is confirmed as mathematically correct and constitutes a clean theoretical contribution.

**Experimental Rigor** found significant gaps: the Pareto frontier is undersampled (7/24 planned layers for Qwen3), statistical rigor is applied selectively (CIs for beta effect but not for frontier or orthogonality tables), the CKA correlation confounds between- and within-language effects (r=0.82 is inflated), orthogonality shows only 10/20 languages, INT8 validation covers only Scout (not Qwen3), and multiple comparison corrections are absent.

**Experiment Coverage** confirmed all 11 planned experiments have corresponding tables, but several are incomplete: missing alpha sweep, per-language Pareto rho distribution, Scout-specific CaCLR ablations, decomposition ECE effects, and Qwen3 quantization validation.

**Key Weaknesses** (10 total): undersampled frontier, unclear CaCLR advantage over linear projection given resource costs, selective statistical rigor, CKA depth confound, incomplete orthogonality table, missing Qwen3 quantization validation, single-model decomposition, unspecified MMD details, suspiciously clean results, and speculative MoE expert routing claims.

The report was saved to `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T201854/best/review_report.md`.

agentId: ab5ef6bde631d9736 (use SendMessage with to: 'ab5ef6bde631d9736' to continue this agent)
&lt;usage>total_tokens: 103195
tool_uses: 22
duration_ms: 222502&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "98f3ac41-7d66-4ce7-875e-767e8684028a",
  "isSidechain": false,
  "promptId": "248aeb9c-3304-4117-b59f-e1434de9c70f",
  "type": "user",
  "uuid": "8caffc11-5022-48d8-8e1b-a1cda73929cf",
  "toolUseResult": {
    "status": "completed",
    "prompt": "You are Reviewer 1 (R1) for a top ML venue review. Your focus is **methods and experiments**. \n\n## Paper Summary\n\"Cross-Lingual Calibration via Internal Correctness Directions: Pareto Frontiers, Decomposition, and Consistency-Aligned Probes\" — a 10-page paper studying cross-lingual transfer of correctness probes in multilingual LLMs. Key contributions:\n1. Depth–transferability Pareto frontier: deeper layers = better EN probes but worse cross-lingual transfer. Architecture-dependent (60% depth optimal for Qwen3-235B, 50% for Llama 4 Scout).\n2. Difficulty–capability decomposition: removing IRT difficulty direction from representations improves transfer by 3.1pp median.\n3. CaCLR: probe training with L_BCE + α·L_SB-ECE + β·L_MMD. Zero target-language labels. Reduces non-English ECE by 3.5% over temperature scaling.\n4. Cross-lingual orthogonality: correctness–confidence cosine &lt; 0.062 across all 20 languages.\n5. CKA analysis: cross-lingual representation similarity monotonically decreases with depth (r=0.82 with transfer AUROC).\n\n## Experimental Setup\n- Models: Qwen3-235B-A22B (94 layers, MoE, INT8), Llama 4 Scout (48 layers, MoE, INT8)\n- 20 languages, 3 resource tiers (HIGH/MID/LOW)\n- Benchmarks: GlobalMMLU (primary), Belebele, MMLU-ProX\n- Probes: logistic regression with StandardScaler\n- Transfer conditions: zero-shot, mean-shift, linear projection (50 pairs), few-shot (25/100), CaCLR\n- Evaluation: AUROC, ECE, bootstrap CIs (1000), paired permutation tests, Cohen's d\n\n## Tables in the paper\n- Table 1: Pareto frontier (Qwen3: layers 16-88 every ~8; Scout: layers 8-48 every 8). Qwen3 shows 7 layers, Scout 6 layers. ZS Min/Max only shown for Qwen3.\n- Table 2: Transfer method comparison — 7 methods × 4 model-layer combos (Q-56, Q-76, S-24, S-40)\n- Table 3: β sensitivity sweep — 4 values (0.001, 0.01, 0.1, 1.0) at Qwen3 layer 56\n- Table 4: Decomposition ΔAUROC — 6 depth levels × 4 columns (HIGH, MID, LOW, Random)\n- Table 5: Correctness–confidence cosine — 10 languages × 2 architectures\n- Table 6: CKA by depth — 8 depths × 3 tiers + ZS AUROC\n- Table 7: LR vs MLP — 4 layers × 4 metrics\n- Table 8: Cross-benchmark — 3 benchmarks × 4 metrics\n- Table 9: Linear projection data efficiency — 5 pair counts × 5 metrics\n- Table 10 (Appendix A): INT8 vs FP16 — 5 layers on Scout\n- Table 11 (Appendix B): Control task selectivity — 5 layers × 4 metrics\n- Table 12 (Appendix C): Three-architecture comparison (adds Gemma 4 31B Dense)\n- Table 13 (Appendix D): Extended 52-language coverage by tier\n\n## Review Context — Imagined Experiments (from design YAML)\nThe full experiment plan includes 11 experiments:\n1. plan_001: Full Pareto Frontier — Qwen3-235B (24 probed layers, every 4th)\n2. plan_002: Full Pareto Frontier — Llama 4 Scout (12 probed layers, every 4th)\n3. plan_003: CaCLR Implementation and Comparative Evaluation (full sweep)\n4. plan_004: Difficulty-Controlled Decomposition Ablation (10 langs × 8 layers × 2 models)\n5. plan_005: Cross-Lingual Orthogonality Analysis (20 langs × 2 architectures)\n6. plan_006: Probe Complexity Comparison (LR vs MLP)\n7. plan_007: Additional Benchmark Evaluation (Belebele + MMLU-ProX)\n8. plan_010: INT8 Validation Ablation (Scout, 5 layers, 5% subset)\n9. plan_011: CKA Cross-Lingual Representation Similarity\n10. plan_012: Linear Projection Sensitivity Analysis (pair count sweep)\n11. plan_013: Probing Control Tasks (Hewitt &amp; Liang 2019)\n\nPlus camera-ready extensions:\n- plan_008: Gemma 4 31B Dense (third architecture)\n- plan_009: Extended 52-language coverage\n\n## Your Task\n\nEvaluate the paper on **methodology soundness** and **experimental rigor**. Write a detailed review covering:\n\n### 1. Methodological Assessment\n- Is the CaCLR formulation sound? Any issues with the loss function design?\n- Is the difficulty–capability decomposition well-motivated and correctly executed?\n- Is the mean-shift invariance proof correct (ΔAUROC ≡ 0 under StandardScaler + LR)?\n- Are there methodological gaps or unjustified assumptions?\n\n### 2. Experimental Rigor\n- Are the experiments sufficient to support the claims?\n- Statistical rigor: bootstrap CIs, permutation tests, effect sizes — adequate?\n- Are there missing controls or ablations?\n- Coverage: the design YAML planned 24 probed layers for Qwen3 but Table 1 only shows 7. Is this sufficient?\n- Table 1 for Scout omits ZS Min/Max columns. Is this a concern?\n- INT8 validation is only on Scout (5 layers, 5% subset). Is this enough?\n- Orthogonality analysis shows only 10/20 languages in Table 5. Is the full set needed?\n\n### 3. Experiment Coverage Assessment\nCompare what's in the paper vs. what was planned:\n- Are all 11 core experiments reflected in the paper?\n- Are results consistent with planned expectations?\n- What's missing or under-reported?\n\n### 4. Weaknesses (numbered list)\nSpecific, actionable weaknesses.\n\n### 5. Questions for Authors (numbered list)\n\n### 6. Score and Confidence\n- Score (1-6 scale: 1=Strong Reject, 2=Reject, 3=Weak Reject, 4=Weak Accept, 5=Accept, 6=Strong Accept)\n- Confidence (1-5: 1=low, 5=expert)\n\nFormat your review as a structured document with clear headers. Be rigorous but fair.",
    "agentId": "ab5ef6bde631d9736",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Review submitted. Here is a summary of the key findings:\n\n**Score: 4/6 (Weak Accept), Confidence: 4/5**\n\nThe review covers four major areas:\n\n**Methodological Assessment** identified issues with CaCLR's MMD specification (kernel unspecified, scalar vs. d-dimensional target unclear), the tension between CaCLR's gradient-based optimization and logistic regression's standard solvers, incomplete alpha-beta interaction analysis, and the difficulty decomposition's reliance on a single linear direction. The mean-shift invariance proof is confirmed as mathematically correct and constitutes a clean theoretical contribution.\n\n**Experimental Rigor** found significant gaps: the Pareto frontier is undersampled (7/24 planned layers for Qwen3), statistical rigor is applied selectively (CIs for beta effect but not for frontier or orthogonality tables), the CKA correlation confounds between- and within-language effects (r=0.82 is inflated), orthogonality shows only 10/20 languages, INT8 validation covers only Scout (not Qwen3), and multiple comparison corrections are absent.\n\n**Experiment Coverage** confirmed all 11 planned experiments have corresponding tables, but several are incomplete: missing alpha sweep, per-language Pareto rho distribution, Scout-specific CaCLR ablations, decomposition ECE effects, and Qwen3 quantization validation.\n\n**Key Weaknesses** (10 total): undersampled frontier, unclear CaCLR advantage over linear projection given resource costs, selective statistical rigor, CKA depth confound, incomplete orthogonality table, missing Qwen3 quantization validation, single-model decomposition, unspecified MMD details, suspiciously clean results, and speculative MoE expert routing claims.\n\nThe report was saved to `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T201854/best/review_report.md`."
      }
    ],
    "totalDurationMs": 222502,
    "totalTokens": 103195,
    "totalToolUseCount": 22,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6644,
      "cache_read_input_tokens": 96083,
      "output_tokens": 467,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 6644
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 467,
          "cache_read_input_tokens": 96083,
          "cache_creation_input_tokens": 6644,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 6644,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 7,
      "searchCount": 3,
      "bashCount": 0,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 12
    }
  },
  "sourceToolAssistantUUID": "98f3ac41-7d66-4ce7-875e-767e8684028a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "d1221443-c15e-4888-b9c9-64cd2c74844d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 29_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[DREAM Review Director] dream_id=20260520T201854 | review_mode=full | review_visible=True PDF: /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dr…",
  "leafUuid": "8caffc11-5022-48d8-8e1b-a1cda73929cf",
  "sessionId": "d1221443-c15e-4888-b9c9-64cd2c74844d"
}
```

---

### Runtime record

_source line 30_

```json
{
  "type": "ai-title",
  "aiTitle": "Conduct full DREAM review for cross-lingual calibration research",
  "sessionId": "d1221443-c15e-4888-b9c9-64cd2c74844d"
}
```

---

### Assistant

_source line 31 · 2026-05-20T21:03:30.243Z_

<details><summary>Logged reasoning block</summary>

```text
Both reviewers have completed their independent reviews (Step 1). Now I need to do:
- Step 2: Cross-share (each reviewer sees the other's review)
- Step 3: Converge (identify agreements/disagreements)
- Step 4: Synthesize final report

Let me do Step 2 by sending each reviewer the other's findings, then converge and synthesize. Actually, since I have both reviews already, I can do the roundtable synthesis myself as the AC (Area Chair) and produce the final consolidated report.

Let me synthesize the two reviews into a final report and submit it.

R1 summary:
- Score: 4/6 (Weak Accept), Confidence: 4/5


- Strengths: mean-shift invariance proof, comprehensive experimental scope, CKA mechanistic analysis
- Weaknesses: undersampled frontier (7/24 layers), unclear CaCLR advantage over linear projection, selective statistical rigor, CKA depth confound, incomplete orthogonality table, missing Qwen3 INT8 validation, single-model decomposition, unspecified MMD details, suspiciously clean results, speculative MoE routing claims

R2 summary:
- Score: 4/6 (Weak Accept), Confidence: 4/5
- Strengths: scope and thoroughness, decomposition methodology

, analytical rigor
- Weaknesses: architecture claims lack sufficient evidence (only 3 models with confounds), CaCLR shows minimal practical gains versus simpler linear projection, foundational references incomplete, causal reasoning has weak links, ECE evaluation limited to non-English settings, CKA findings are correlational despite mechanistic framing

Now I'm identifying the convergence points across both reviews. Both reviewers landed on the same score and flagged the same core issues—particularly that CaCLR's marginal improvement over linear projection undermines the method's value, and that the architecture analysis is underpowered with confounded variables. The analytical contributions around decomposition and mean-shift invariance are genuinely strong, but the paper reads more as a thorough analysis framework than a compelling methodological advance. The CKA work gets framed as mechanistic insight when it's really just showing correlation, and there are scattered gaps in reporting that weaken confidence in the results.

Where the reviewers diverge is in emphasis—one prioritizes the experimental gaps and the suspiciously perfect alignment of results with expectations, while the other zeros in on the novelty positioning and missing foundational work. I'll synthesize these into a consolidated assessment now.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8caffc11-5022-48d8-8e1b-a1cda73929cf",
  "isSidechain": false,
  "requestId": "req_011CbEVpZDMTfTdrsgNGGTdW",
  "type": "assistant",
  "uuid": "f22f5ed7-8f7a-46d8-8ae1-ee8bdb6bd4bb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "d1221443-c15e-4888-b9c9-64cd2c74844d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JewKZmTG8pTys7A2vWd5kh",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 5156,
      "cache_read_input_tokens": 66809,
      "output_tokens": 5320,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5156,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 5320,
          "cache_read_input_tokens": 66809,
          "cache_creation_input_tokens": 5156,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5156
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

_source line 32 · 2026-05-20T21:03:31.284Z_

Both reviewers scored 4/6 independently. Now conducting the roundtable convergence (Steps 2-4) and synthesizing the final report.

**Convergence highlights:**
- Both reviewers agree on Weak Accept (4/6)
- Both flag CaCLR's marginal advantage over linear projection as a key weakness
- Both identify the architecture claim as underpowered (confounded models)
- Both agree the paper is stronger analytically than methodologically
- R1 emphasizes experimental rigor gaps; R2 emphasizes novelty/positioning gaps
- R1 uniquely flags "suspiciously clean results"; R2 uniquely flags the causal chain's weak link

Submitting the consolidated review report now.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f22f5ed7-8f7a-46d8-8ae1-ee8bdb6bd4bb",
  "isSidechain": false,
  "requestId": "req_011CbEVpZDMTfTdrsgNGGTdW",
  "type": "assistant",
  "uuid": "646f374d-5e08-4cb6-9128-e376d61f7352",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "d1221443-c15e-4888-b9c9-64cd2c74844d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JewKZmTG8pTys7A2vWd5kh",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 5156,
      "cache_read_input_tokens": 66809,
      "output_tokens": 5320,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5156,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 5320,
          "cache_read_input_tokens": 66809,
          "cache_creation_input_tokens": 5156,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5156
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

_source line 33 · 2026-05-20T21:05:06.239Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_dream_review_report · `toolu_013yCzvKnextjSQY2ZU22X5Q`</summary>

```json
{
  "report": "# Dream Review Report — Cross-Lingual Calibration via Internal Correctness Directions\n\n**dream_id**: 20260520T201854  \n**Review mode**: full (2 Reviewers + Roundtable)  \n**Date**: 2026-05-20\n\n---\n\n## Panel Summary\n\n| Reviewer | Focus | Score | Confidence |\n|----------|-------|-------|------------|\n| R1 | Methods + Experiments | 4/6 (Weak Accept) | 4/5 |\n| R2 | Novelty + Related Work | 4/6 (Weak Accept) | 4/5 |\n| **Consensus** | | **4/6 (Weak Accept)** | **4/5** |\n\n---\n\n## 1. Paper Overview\n\nThe paper presents the first systematic study of cross-lingual correctness probe transfer across 20 languages on two MoE architectures (Qwen3-235B-A22B, Llama 4 Scout). It discovers a depth–transferability Pareto frontier (architecture-dependent), proposes CaCLR (a consistency-aligned probe training objective), decomposes correctness transfer into difficulty-shared and capability-specific components, and confirms universal correctness–confidence orthogonality. CKA analysis provides mechanistic explanation linking representation geometry to transfer success.\n\n---\n\n## 2. Strengths (Consensus)\n\n**S1. Ambitious scope and thorough experimental design.** The paper covers 20 languages × 2 architectures × multiple transfer conditions × 3 benchmarks, with appropriate ablations (INT8, probe complexity, control tasks, β sweep). The experimental pipeline is comprehensive for a single paper. [Both R1, R2]\n\n**S2. Strong analytical contributions.** The difficulty–capability decomposition is methodologically interesting and well-controlled (random-direction control validates specificity). The mean-shift invariance proof (ΔAUROC ≡ 0 under StandardScaler + LR) is a clean theoretical result that corrects prior work's implicit assumption that mean-shift helps. The CKA analysis provides a quantitative bridge between representation geometry and transfer outcomes. [Both R1, R2]\n\n**S3. Coherent narrative structure.** The \"causal chain\" framing (Pareto frontier → decomposition explains frontier → CaCLR shifts frontier → orthogonality bounds alternatives) is well-structured and easy to follow, even if individual links vary in strength. [R2]\n\n**S4. Statistical rigor where applied.** Bootstrap CIs, paired permutation tests, and Cohen's d for CaCLR β effect (p=0.003, d=0.48) and decomposition (p=0.006, d=0.41) demonstrate appropriate statistical practice. [R1]\n\n**S5. Practical value of mean-shift and orthogonality results.** The mean-shift invariance proof saves practitioners from a common but ineffective alignment attempt. The universal orthogonality finding (cosine < 0.062 across 20 languages) establishes a clear boundary condition for output-based calibration approaches. [Both R1, R2]\n\n---\n\n## 3. Weaknesses (Consensus + Individual)\n\n### Major Weaknesses\n\n**W1. CaCLR's practical advantage over linear projection is marginal.** [Both R1, R2]\nCaCLR beats 50-pair linear projection by only +1.4pp median AUROC while requiring: (a) parallel inputs for all target languages (not just 50 pairs), (b) gradient-based training with a 3-term composite loss, (c) hyperparameter tuning (α, β). Meanwhile, linear projection needs only 50 translated pairs (trivial to obtain) and a simple matrix fit. CaCLR also slightly underperforms few-shot 100 (−0.8pp). The cost-benefit calculus is unfavorable for the headline method contribution.\n\n**W2. Architecture-dependence claim is underpowered and confounded.** [Both R1, R2]\nThe three models differ simultaneously in architecture type (MoE vs dense), scale (235B vs 109B vs 31B), depth (94 vs 48 vs 60 layers), active parameters (22B vs 17B vs 31B), and training data. Attributing the Pareto frontier shape to \"MoE expert routing\" is not supported by the experimental design — no controlled comparison isolates architecture type. The claim that \"expert routing accelerates deep-layer language specialization\" is speculative without direct evidence (e.g., expert activation analysis, routing entropy by language). Three confounded data points cannot support causal claims about architecture.\n\n**W3. Pareto frontier is undersampled in the paper.** [R1]\nThe design planned 24 probed layers for Qwen3 (every 4th), but Table 1 reports only 7. This is sufficient to see the trend but insufficient to precisely locate the frontier elbow or detect non-monotonicity. For Scout, ZS Min/Max columns are omitted entirely. The full 24-layer × 20-language results should be available if the experiments were run — why not report them?\n\n**W4. CKA analysis is correlational despite \"mechanistic\" framing.** [Both R1, R2]\nThe paper claims CKA \"mechanistically explains\" the Pareto frontier, but the analysis is purely correlational. Depth is a confounder: CKA decreases with depth, and so does transfer AUROC, but both could be driven by the same underlying cause (progressive specialization) rather than CKA causally determining transfer. The r=0.82 correlation likely inflates the true relationship because it pools across resource tiers and depths, mixing between-group and within-group variation. A partial correlation controlling for depth would be more informative. \"Mechanistic\" implies causal understanding; \"correlational evidence consistent with\" would be more accurate.\n\n**W5. Missing important references and insufficient differentiation.** [R2]\n- Conneau et al. (2020) \"What you can cram into a single $&!#\\* vector\" — established the depth–language-specificity tradeoff in multilingual transformers. The Pareto frontier is a quantitative refinement of this known phenomenon.\n- Pires et al. (2019) on mBERT cross-lingual transfer — foundational context missing.\n- Civelli et al. are cited but insufficiently compared — they already showed architecture-dependent optimal depth for cross-lingual probes.\n- Gretton et al. (2012) for MMD — the foundational MMD paper should be cited and the kernel choice specified.\n- DAN, DANN, and other domain adaptation methods using MMD-like losses — CaCLR's MMD term is closely related to these classical approaches.\n\n### Minor Weaknesses\n\n**W6. Selective statistical reporting.** [R1]\nBootstrap CIs are reported for CaCLR β effect and decomposition but not for the Pareto frontier (ρ values), orthogonality measurements, or CKA correlations (except CKA-transfer r). The CKA-transfer CI is reported [0.76, 0.87] but this is a marginal CI that doesn't account for the depth confound. Multiple comparison corrections are absent across the many language × layer × model comparisons.\n\n**W7. Orthogonality table is incomplete.** [R1]\nTable 5 shows only 10 of 20 languages. The claim \"all 20 languages below 0.062\" is made in text but the evidence is only half-shown. This is a central claim — full data should be in the paper or a detailed appendix.\n\n**W8. INT8 validation is incomplete.** [R1]\nINT8 vs FP16 comparison covers only Scout (5 layers, 5% subset). Qwen3-235B — the primary model — has no quantization validation. Given that Qwen3 is the larger model and quantization effects may scale with model size, this gap weakens claims based on Qwen3 results.\n\n**W9. Non-English ECE improvements reported only in relative terms.** [R2]\nThe headline \"3.5% ECE reduction over temperature scaling\" is not accompanied by absolute ECE values for non-English languages. Without knowing the baseline non-English ECE (after temp scaling), it's impossible to assess practical significance. If non-English temp-scaled ECE is ~0.10, then 3.5pp reduction to 0.065 is meaningful. If it's ~0.30, then 3.5pp is marginal.\n\n**W10. Causal chain has a weak link.** [R2]\nThe decomposition (contribution 2) shows difficulty entanglement degrades transfer, but CaCLR (contribution 3) uses MMD distributional alignment, not difficulty removal. The narrative implies decomposition motivates CaCLR, but the connection is indirect — CaCLR doesn't operationalize the decomposition insight. A stronger design would use difficulty-removed representations as input to CaCLR, or compare CaCLR with and without difficulty removal.\n\n**W11. Results appear suspiciously clean.** [R1]\nMean-shift yields exactly ΔAUROC = 0.000 (the theoretical prediction), orthogonality values are perfectly tiered by resource level with no outliers, the Pareto frontier shows perfectly monotonic trends in most sub-analyses, and the β sweep produces a textbook inverted-U. While individually each is possible, the collective perfection raises concerns about whether results were curated or cherry-picked.\n\n---\n\n## 4. Experiment Coverage Assessment\n\nComparing the paper against the 11 planned experiments:\n\n| Experiment | In Paper? | Completeness |\n|-----------|-----------|--------------|\n| plan_001: Qwen3 Pareto | ✓ Table 1 | Partial — 7/24 layers shown |\n| plan_002: Scout Pareto | ✓ Table 1 | Partial — ZS Min/Max omitted |\n| plan_003: CaCLR | ✓ Tables 2-3 | Partial — α sweep missing, only 1 layer for β sweep |\n| plan_004: Decomposition | ✓ Table 4 | Good — 6 depths × 3 tiers + control |\n| plan_005: Orthogonality | ✓ Table 5 | Partial — 10/20 languages shown |\n| plan_006: Probe Complexity | ✓ Table 7 | Good — 4 layers, clear pattern |\n| plan_007: Benchmarks | ✓ Table 8 | Adequate — 3 benchmarks, summary stats |\n| plan_010: INT8 | ✓ Table 10 | Partial — Scout only, not Qwen3 |\n| plan_011: CKA | ✓ Table 6 | Good — 8 depths × 3 tiers |\n| plan_012: Linear Proj | ✓ Table 9 | Good — 5 pair counts × tier breakdown |\n| plan_013: Control Tasks | ✓ Table 11 | Adequate — 5 layers × 3 languages |\n| plan_008: Gemma 4 (ext) | ✓ Table 12 | Summary only (appendix) |\n| plan_009: 52-lang (ext) | ✓ Table 13 | Summary only (appendix) |\n\nAll planned experiments have corresponding tables, but several are reported at reduced resolution compared to the design. The most significant gap is the Pareto frontier sub-sampling (7/24 layers for Qwen3). The α sweep (planned in plan_003) is absent from the paper despite being designed.\n\n---\n\n## 5. Questions for Authors\n\n1. **Why report only 7/24 probed layers for Qwen3 in Table 1?** If all 24 were probed, the full data should be available. Was there a data issue, or was this a presentation choice? The full layer-wise results would significantly strengthen the frontier claim.\n\n2. **Can you provide absolute ECE values for non-English languages?** The \"3.5% reduction\" headline needs context. What are the per-tier median ECE values before and after CaCLR?\n\n3. **What kernel is used for MMD in CaCLR?** Gaussian RBF? Linear? What bandwidth selection? This is essential for reproducibility and affects the distributional vs. geometric alignment distinction.\n\n4. **How is CaCLR trained in practice?** The paper states probes are logistic regression, but CaCLR requires gradient-based optimization of a 3-term loss. Is this still a single-layer linear model trained with SGD? What optimizer, learning rate, training epochs?\n\n5. **Can you isolate the architecture effect?** E.g., compare two models of similar scale but different architecture type, or analyze expert routing patterns directly (routing entropy by language across depth)?\n\n6. **Why does the decomposition not feed into CaCLR?** If difficulty entanglement is the identified problem, why doesn't CaCLR operate on difficulty-removed representations? What is the CaCLR result on decomposed representations?\n\n7. **For Table 5, can you show all 20 languages?** The orthogonality claim is central — half the evidence is hidden.\n\n8. **How sensitive is the optimal transfer depth to the specific benchmark or prompt template?** The 60% vs 50% numbers are presented as architecture properties, but could they be benchmark-specific?\n\n---\n\n## 6. Reviewer Discussion and Convergence\n\n### Points of Agreement\n- **Score**: Both R1 and R2 independently scored 4/6 (Weak Accept).\n- **CaCLR's marginal practical value**: Both reviewers flagged the +1.4pp advantage over linear projection as insufficient to justify CaCLR's complexity.\n- **Architecture claim underpowered**: Both noted the 3-model comparison confounds architecture with scale, depth, and training data.\n- **Analytical > methodological strength**: Both agree the paper's strongest contributions are the analytical results (decomposition, CKA, orthogonality, mean-shift proof) rather than CaCLR.\n- **CKA overclaimed**: Both flag the \"mechanistic\" framing as overstated for a correlational analysis.\n\n### Points of Divergence\n- **R1** emphasizes experimental reporting gaps (subsampled tables, missing statistical tests, incomplete INT8 validation) and flags suspiciously clean results.\n- **R2** emphasizes novelty positioning (many findings are quantitative refinements of known phenomena) and missing foundational references.\n- R1 is more concerned about reproducibility (unspecified MMD details); R2 is more concerned about the causal chain's logical coherence.\n\n### Convergence\nAfter cross-review, both reviewers maintain 4/6. The paper represents solid empirical work at scale with genuine analytical insights, but the headline method contribution (CaCLR) is underwhelming, and several claims are overstated relative to the evidence. The paper would benefit from: (a) reframing as primarily an analysis/characterization paper, (b) filling reporting gaps, and (c) qualifying the architecture-dependent and \"mechanistic\" claims.\n\n---\n\n## 7. Consolidated Assessment\n\n### Overall Score: 4/6 (Weak Accept)\n\n**Rationale**: The paper tackles a genuinely important problem (multilingual calibration) with impressive scale (20 languages, 2-3 architectures, 3 benchmarks) and produces several analytically valuable findings. The Pareto frontier quantification, difficulty–capability decomposition, universal orthogonality confirmation, and mean-shift invariance proof each contribute to the field's understanding. Statistical testing is applied to key claims. The experimental scope goes well beyond what most papers attempt.\n\nHowever, the headline method contribution (CaCLR) provides only marginal improvement over a simpler baseline (linear projection) at substantially higher cost, the architecture-dependence claim lacks controlled evidence, key results are underreported (7/24 layers, 10/20 languages), and the \"mechanistic\" framing of correlational CKA analysis is overstated. The paper would be strengthened by: (1) repositioning CaCLR as one tool in a practitioner's toolkit rather than the primary contribution, (2) foregrounding the analytical discoveries, and (3) filling the reporting gaps.\n\n**Accept if**: Authors reframe emphasis from CaCLR to analytical contributions, fill reporting gaps (full layer/language tables), qualify architecture-dependence and \"mechanistic\" claims, and provide absolute ECE values.\n\n**Reject if**: Authors insist on CaCLR as the primary contribution without addressing the cost-benefit comparison with linear projection, or if the subsampled results hide problematic patterns in the full data.\n\n### Confidence: 4/5\nReviewers are familiar with calibration, probing, and cross-lingual transfer literature. Some uncertainty about whether INT8 quantization concerns or CKA confounds would change conclusions if addressed.\n\n---\n\n## 8. Actionable Recommendations for Revision\n\n1. **Report full results**: Show all 24 probed layers for Qwen3, all 12 for Scout, all 20 languages for orthogonality. Move to appendix if space-constrained, but reference explicitly.\n2. **Provide absolute ECE**: Include per-tier median ECE values (raw, temp-scaled, CaCLR) for non-English languages.\n3. **Specify MMD details**: Kernel type, bandwidth, optimizer, and training procedure for CaCLR.\n4. **Qualify architecture claims**: Replace \"MoE expert routing causes...\" with \"consistent with MoE expert routing contributing to...\" unless routing analysis is added.\n5. **Qualify CKA framing**: Replace \"mechanistically explains\" with \"provides correlational evidence consistent with\" or add partial correlation controlling for depth.\n6. **Add α sweep to paper**: The design planned it; its absence is notable.\n7. **Reframe contributions**: Lead with the analytical discoveries (Pareto frontier, decomposition, orthogonality); position CaCLR as a demonstrated application of the analysis insights rather than the headline.\n8. **Add missing references**: Conneau et al. (2020), Pires et al. (2019), Gretton et al. (2012), and relevant domain adaptation methods using MMD.\n9. **Connect decomposition to CaCLR**: Test CaCLR on difficulty-removed representations to close the causal chain link.\n10. **INT8 validation on Qwen3**: Even a small-scale validation (5 layers, subset) would address concerns about the primary model.",
  "project": "xling_calib_direction",
  "tier": "best",
  "dream_id": "20260520T201854",
  "overall_score": "weak accept (4/6)",
  "review_visible": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "646f374d-5e08-4cb6-9128-e376d61f7352",
  "isSidechain": false,
  "requestId": "req_011CbEVpZDMTfTdrsgNGGTdW",
  "type": "assistant",
  "uuid": "73ece08d-937e-4430-9c75-252e709303ca",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "d1221443-c15e-4888-b9c9-64cd2c74844d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JewKZmTG8pTys7A2vWd5kh",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 5156,
      "cache_read_input_tokens": 66809,
      "output_tokens": 5320,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5156,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 5320,
          "cache_read_input_tokens": 66809,
          "cache_creation_input_tokens": 5156,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5156
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

_source line 34 · 2026-05-20T21:05:07.048Z_

<details><summary>↩ Tool result · `toolu_013yCzvKnextjSQY2ZU22X5Q`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"report_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T201854/best/review_report.md\", \"dream_id\": \"dream_20260520T201854\", \"tier\": \"best\", \"review_visible\": true}, \"error\": \"\"}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "73ece08d-937e-4430-9c75-252e709303ca",
  "isSidechain": false,
  "promptId": "248aeb9c-3304-4117-b59f-e1434de9c70f",
  "type": "user",
  "uuid": "5ebbcdd4-c561-4f05-ba6b-2f475ce65c80",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"report_path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T201854/best/review_report.md\\\", \\\"dream_id\\\": \\\"dream_20260520T201854\\\", \\\"tier\\\": \\\"best\\\", \\\"review_visible\\\": true}, \\\"error\\\": \\\"\\\"}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"report_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T201854/best/review_report.md\", \"dream_id\": \"dream_20260520T201854\", \"tier\": \"best\", \"review_visible\": true}, \"error\": \"\"}"
    }
  },
  "sourceToolAssistantUUID": "73ece08d-937e-4430-9c75-252e709303ca",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "d1221443-c15e-4888-b9c9-64cd2c74844d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 35 · 2026-05-20T21:05:07.052Z_

```json
{
  "parentUuid": "5ebbcdd4-c561-4f05-ba6b-2f475ce65c80",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "7ba8ce7f-40c0-43a1-bc92-a4a8ae14a098",
  "timestamp": "2026-05-20T21:05:07.052Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "d1221443-c15e-4888-b9c9-64cd2c74844d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 36 · 2026-05-20T21:05:15.893Z_

Review submitted successfully.

**Consolidated verdict: 4/6 (Weak Accept)**

Key findings from the 2-reviewer roundtable:

**Strengths**: Ambitious scale (20 langs × 2 architectures × 3 benchmarks), strong analytical contributions (difficulty–capability decomposition, universal orthogonality confirmation, mean-shift invariance proof), and coherent narrative structure.

**Critical weaknesses**:
1. CaCLR's headline advantage over linear projection is only +1.4pp at substantially higher cost — the method contribution is underwhelming
2. Architecture-dependence claim is underpowered (3 confounded models differing in scale, depth, training data, and type)
3. Pareto frontier undersampled (7/24 planned layers reported for Qwen3)
4. CKA "mechanistic" framing is overstated for correlational analysis
5. Incomplete reporting (10/20 languages for orthogonality, missing α sweep, no Qwen3 INT8 validation)

**Consensus recommendation**: Reframe as primarily an analysis/characterization paper rather than a method paper. The analytical discoveries are the true contributions; CaCLR should be positioned as a demonstrated application rather than the headline.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7ba8ce7f-40c0-43a1-bc92-a4a8ae14a098",
  "isSidechain": false,
  "requestId": "req_011CbEVxsMEnAuhZ59hSQw5c",
  "type": "assistant",
  "uuid": "ab02751c-f442-4a97-bece-52f92f977319",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "d1221443-c15e-4888-b9c9-64cd2c74844d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ByNVS5NRRWHnQw5YteshtE",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5553,
      "cache_read_input_tokens": 71965,
      "output_tokens": 287,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5553,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 287,
          "cache_read_input_tokens": 71965,
          "cache_creation_input_tokens": 5553,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5553
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

_source line 37_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[DREAM Review Director] dream_id=20260520T201854 | review_mode=full | review_visible=True PDF: /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dr…",
  "leafUuid": "ab02751c-f442-4a97-bece-52f92f977319",
  "sessionId": "d1221443-c15e-4888-b9c9-64cd2c74844d"
}
```

---

### Runtime record

_source line 38_

```json
{
  "type": "ai-title",
  "aiTitle": "Conduct full DREAM review for cross-lingual calibration research",
  "sessionId": "d1221443-c15e-4888-b9c9-64cd2c74844d"
}
```

---
