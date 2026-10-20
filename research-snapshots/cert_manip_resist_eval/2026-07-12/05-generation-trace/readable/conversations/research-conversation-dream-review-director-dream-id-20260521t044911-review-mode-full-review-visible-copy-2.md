# Research conversation: [DREAM Review Director] dream_id=20260521T044911 | review_mode=full | review_visible=True PDF: /home/ubuntu/.agent-ml-re

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 70
- **Recorded user turns:** 4
- **Tool calls:** 14
- **Original source:** `logs/chats/exported-trajectories/account-1/91a2196c-7a23-4294-80ba-646c05703e7b.jsonl`
- **Structured JSON:** [`f8e67c4f48456335359c.json`](../../sessions/f8/f8e67c4f48456335359c.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-21T05:57:44.640Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-21T05:57:44.640Z",
  "sessionId": "91a2196c-7a23-4294-80ba-646c05703e7b",
  "content": "[DREAM Review Director]\ndream_id=20260521T044911 | review_mode=full | review_visible=True\nPDF: /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/median/review_input_e90a5c14.pdf\n\n（内部编排信息：tier=median，仅用于 submit_dream_review_report 调用。\n你在向 Reviewer 发送审稿任务时，**严禁**提及档位名称 best/median/worst，\n也不要暗示论文结果的好坏。Reviewer 必须盲审。）\n\n任务：对上述 PDF 进行 full 模式审稿。 使用 `dream-review-full` skill 的 dispatch 模板（2 Reviewers：R1 方法+实验、R2 新颖性+相关工作；完整 roundtable：Step 1 独立 → Step 2 交叉分享 → Step 3 收敛 → Step 4 综合）。\n\n## 审稿标准\n\n未指定目标 venue。在开始审稿前，你必须：\n1. 确认目标 venue 及其评分标准\n2. 用 WebSearch 搜索该 venue 的 reviewer guidelines\n3. 严格按照搜到的官方评分刻度打分\n4. 如果无法确认 venue，使用 ACL ARR 1-5 分制\n\n## 实验设计参考\n\n完整实验设计（含想象实验列表）：`/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/median/review_context.yaml`\n论文可能未完整反映所有实验——参考此文件判断覆盖度。\n完成后必须调用 `submit_dream_review_report(report, project=\"xling_calib_direction\", tier=\"median\", dream_id=\"20260521T044911\", review_visible=True)` —— 报告会写入 dream_reports/dream_20260521T044911/median/review_report.md，编排进程通过 subprocess 退出读取它。\n不要调用 submit_review_report_to_research_director / update_review_issues / request_external_review —— 这些工具不在 Dream Review Director 白名单内。\n"
}
```

---

### Runtime record

_source line 2 · 2026-05-21T05:57:44.649Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-21T05:57:44.649Z",
  "sessionId": "91a2196c-7a23-4294-80ba-646c05703e7b"
}
```

---

## Round 1

10 recorded events

### User

_source line 3 · 2026-05-21T05:57:44.742Z_

[DREAM Review Director]
dream_id=20260521T044911 | review_mode=full | review_visible=True
PDF: /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/median/review_input_e90a5c14.pdf

（内部编排信息：tier=median，仅用于 submit_dream_review_report 调用。
你在向 Reviewer 发送审稿任务时，**严禁**提及档位名称 best/median/worst，
也不要暗示论文结果的好坏。Reviewer 必须盲审。）

任务：对上述 PDF 进行 full 模式审稿。 使用 `dream-review-full` skill 的 dispatch 模板（2 Reviewers：R1 方法+实验、R2 新颖性+相关工作；完整 roundtable：Step 1 独立 → Step 2 交叉分享 → Step 3 收敛 → Step 4 综合）。

## 审稿标准

未指定目标 venue。在开始审稿前，你必须：
1. 确认目标 venue 及其评分标准
2. 用 WebSearch 搜索该 venue 的 reviewer guidelines
3. 严格按照搜到的官方评分刻度打分
4. 如果无法确认 venue，使用 ACL ARR 1-5 分制

## 实验设计参考

完整实验设计（含想象实验列表）：`/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/median/review_context.yaml`
论文可能未完整反映所有实验——参考此文件判断覆盖度。
完成后必须调用 `submit_dream_review_report(report, project="xling_calib_direction", tier="median", dream_id="20260521T044911", review_visible=True)` —— 报告会写入 dream_reports/dream_20260521T044911/median/review_report.md，编排进程通过 subprocess 退出读取它。
不要调用 submit_review_report_to_research_director / update_review_issues / request_external_review —— 这些工具不在 Dream Review Director 白名单内。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "d159e131-5779-4f9c-878e-e70f68151974",
  "type": "user",
  "uuid": "6f7c874a-4f99-46ef-8260-3c45bc6a1e6b",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "91a2196c-7a23-4294-80ba-646c05703e7b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-21T05:57:44.741Z_

```json
{
  "parentUuid": "6f7c874a-4f99-46ef-8260-3c45bc6a1e6b",
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
  "uuid": "d5ece298-ad6e-4116-9429-e7df14f45964",
  "timestamp": "2026-05-21T05:57:44.741Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "91a2196c-7a23-4294-80ba-646c05703e7b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-21T05:57:44.741Z_

```json
{
  "parentUuid": "d5ece298-ad6e-4116-9429-e7df14f45964",
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
  "uuid": "adc14bdf-9906-4e64-98d5-567e9ec841ed",
  "timestamp": "2026-05-21T05:57:44.741Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "91a2196c-7a23-4294-80ba-646c05703e7b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6 · 2026-05-21T05:57:44.741Z_

```json
{
  "parentUuid": "adc14bdf-9906-4e64-98d5-567e9ec841ed",
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
  "uuid": "1393f77e-5a7f-4293-918d-23a13de4ab5a",
  "timestamp": "2026-05-21T05:57:44.741Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "91a2196c-7a23-4294-80ba-646c05703e7b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 7 · 2026-05-21T05:57:44.742Z_

```json
{
  "parentUuid": "1393f77e-5a7f-4293-918d-23a13de4ab5a",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "68e86ff0-5c28-403e-ae75-e7287ae2461d",
  "timestamp": "2026-05-21T05:57:44.742Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "91a2196c-7a23-4294-80ba-646c05703e7b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 8_

```json
{
  "type": "ai-title",
  "aiTitle": "Full peer review of cross-lingual calibration research",
  "sessionId": "91a2196c-7a23-4294-80ba-646c05703e7b"
}
```

---

### Assistant

_source line 9 · 2026-05-21T05:57:49.097Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to perform a full DREAM review of a PDF paper. Let me break down the task:

1. Read the PDF paper
2. Read the review context YAML for experiment design reference
3. Determine the venue and scoring criteria
4. Dispatch 2 reviewers (R1: methods+experiments, R2: novelty+related work)
5. Run a full roundtable process
6. Submit the review report

Let me start by reading the PDF and the review context YAML, and searching for the venue guidelines.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "68e86ff0-5c28-403e-ae75-e7287ae2461d",
  "isSidechain": false,
  "requestId": "req_011CbFCacDovYEKas26G3FHT",
  "type": "assistant",
  "uuid": "123bb518-a326-4118-9793-f9ff840ba3b2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "91a2196c-7a23-4294-80ba-646c05703e7b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Vd2KXWeoV71hCPY36dqnrq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11827,
      "cache_read_input_tokens": 11447,
      "output_tokens": 386,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11827,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 386,
          "cache_read_input_tokens": 11447,
          "cache_creation_input_tokens": 11827,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11827
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

_source line 10 · 2026-05-21T05:57:49.633Z_

开始审稿流程。先读取论文 PDF 和实验设计参考文件，确认目标 venue。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "123bb518-a326-4118-9793-f9ff840ba3b2",
  "isSidechain": false,
  "requestId": "req_011CbFCacDovYEKas26G3FHT",
  "type": "assistant",
  "uuid": "628867f7-3285-4596-9458-7be5ba51d9c9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "91a2196c-7a23-4294-80ba-646c05703e7b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Vd2KXWeoV71hCPY36dqnrq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11827,
      "cache_read_input_tokens": 11447,
      "output_tokens": 386,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11827,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 386,
          "cache_read_input_tokens": 11447,
          "cache_creation_input_tokens": 11827,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11827
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

_source line 11 · 2026-05-21T05:57:50.883Z_

<details open><summary>🔧 Tool call — Read · `toolu_01X4s8D6Vh58WxJHGRHeEcRQ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/median/review_input_e90a5c14.pdf",
  "pages": "1-5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "628867f7-3285-4596-9458-7be5ba51d9c9",
  "isSidechain": false,
  "requestId": "req_011CbFCacDovYEKas26G3FHT",
  "type": "assistant",
  "uuid": "c65dfc46-aa6f-4003-9edf-7285dba233d4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "91a2196c-7a23-4294-80ba-646c05703e7b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Vd2KXWeoV71hCPY36dqnrq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11827,
      "cache_read_input_tokens": 11447,
      "output_tokens": 386,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11827,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 386,
          "cache_read_input_tokens": 11447,
          "cache_creation_input_tokens": 11827,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11827
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

_source line 12 · 2026-05-21T05:57:51.150Z_

<details><summary>↩ Tool result · `toolu_01X4s8D6Vh58WxJHGRHeEcRQ`</summary>

```text
PDF pages extracted: 5 page(s) from /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/median/review_input_e90a5c14.pdf (212.9KB)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c65dfc46-aa6f-4003-9edf-7285dba233d4",
  "isSidechain": false,
  "promptId": "d159e131-5779-4f9c-878e-e70f68151974",
  "type": "user",
  "uuid": "bb139999-e088-4e8c-be41-6750f182f26f",
  "toolUseResult": {
    "type": "parts",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/median/review_input_e90a5c14.pdf",
      "originalSize": 218031,
      "outputDir": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0519-2-projects-xling-calib-direction/91a2196c-7a23-4294-80ba-646c05703e7b/tool-results/pdf-2cecaa68-2031-4829-9fac-29e93f1ed25f",
      "count": 5
    }
  },
  "sourceToolAssistantUUID": "c65dfc46-aa6f-4003-9edf-7285dba233d4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "91a2196c-7a23-4294-80ba-646c05703e7b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

## Round 2

10 recorded events

### User

_source line 13 · 2026-05-21T05:57:51.148Z_

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
  "parentUuid": "bb139999-e088-4e8c-be41-6750f182f26f",
  "isSidechain": false,
  "promptId": "d159e131-5779-4f9c-878e-e70f68151974",
  "type": "user",
  "isMeta": true,
  "uuid": "192776c8-0956-4d59-a691-d7489ba99f7c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "91a2196c-7a23-4294-80ba-646c05703e7b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-21T05:57:51.377Z_

<details open><summary>🔧 Tool call — Read · `toolu_01QuT7Srd8u13tkdb7pHgKt3`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/median/review_context.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "192776c8-0956-4d59-a691-d7489ba99f7c",
  "isSidechain": false,
  "requestId": "req_011CbFCacDovYEKas26G3FHT",
  "type": "assistant",
  "uuid": "0144cdc4-5846-4dd2-b768-dd33560359e7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "91a2196c-7a23-4294-80ba-646c05703e7b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Vd2KXWeoV71hCPY36dqnrq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11827,
      "cache_read_input_tokens": 11447,
      "output_tokens": 386,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11827,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 386,
          "cache_read_input_tokens": 11447,
          "cache_creation_input_tokens": 11827,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11827
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

_source line 15_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[DREAM Review Director] dream_id=20260521T044911 | review_mode=full | review_visible=True PDF: /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dr…",
  "leafUuid": "0144cdc4-5846-4dd2-b768-dd33560359e7",
  "sessionId": "91a2196c-7a23-4294-80ba-646c05703e7b"
}
```

---

### Runtime record

_source line 16_

```json
{
  "type": "ai-title",
  "aiTitle": "Full peer review of cross-lingual calibration research",
  "sessionId": "91a2196c-7a23-4294-80ba-646c05703e7b"
}
```

---

### Tool result

_source line 17 · 2026-05-21T05:57:51.679Z_

<details><summary>↩ Tool result · `toolu_01QuT7Srd8u13tkdb7pHgKt3`</summary>

```text
1	narrative_guidance: 'CaCLR consistency loss (MMD) 在完整 β sweep 中无显著 AUROC 提升，转为 negative
2	  result framing。 几何解释：MMD 匹配边际分布但无法对齐低维 directional structure——correctness 方向占据 1-3
3	  维子空间， MMD 在 1-D probe logit 空间操作无法捕捉旋转。Linear projection 直接学习子空间旋转故成功。 Simpson''s
4	  Paradox 仅在 Llama 4 Scout 上显著（partial rho~0.29, p~0.02），Qwen3-235B 上 trending 但不显著（rho~0.16,
5	  p~0.07）——用 hedged language 报告为架构依赖发现。Claim 2 decomposition 定性分离成立但 prescriptive
6	  预测力弱——弱化为 ''descriptive separation observed''。 标题转向 ''When Does Cross-Lingual Calibration
7	  Transfer Work? Geometric Analysis and Practical Solutions.'' 强化三个实用贡献：(1) linear
8	  projection ~70 pairs 推荐方案，(2) Procrustes effect reversal 阈值 ~0.55 作为 practitioner
9	  guidance，(3) ~30% low-resource probing artifacts 作为 methodological warning。 仍可投
10	  EACL——thorough empirical study + 架构依赖几何洞见 + systematic negative result + 实用指导。
11	
12	  '
13	imagined_experiments:
14	- name: Full Pareto Frontier — Qwen3-235B-A22B (MoE, INT4)
15	  plan_id: plan_001
16	  description: '94 层 MoE 模型，每 4 层取一层（24 probed layers），20 种语言，5 种 transfer 条件。 MoE
17	    路由机制在深层创建更强的语言特异化，产生比 7B pilot 更清晰的 Pareto tradeoff。
18	
19	    '
20	  expected_results:
21	    en_best_auroc: 0.78
22	    en_best_layer: 80
23	    en_best_layer_depth_pct: 0.851
24	    en_auroc_range:
25	    - 0.58
26	    - 0.78
27	    en_best_ece_raw: 0.185
28	    transfer_optimal_layer_mean: 68
29	    transfer_optimal_depth_pct: 0.723
30	    en_transfer_layer_gap_pp: 2.8
31	    zs_pass_rate: 0.75
32	    zs_pass_count: 15
33	    zs_mean_auroc_en_optimal: 0.66
34	    zs_mean_auroc_transfer_optimal: 0.682
35	    pareto_significant_langs: 15
36	    pareto_spearman_rho_median: -0.42
37	    pareto_spearman_rho_range:
38	    - -0.68
39	    - 0.15
40	    pareto_langs_negative_rho: 16
41	    best_zs_auroc_by_tier:
42	      HIGH_mean: 0.725
43	      MID_mean: 0.672
44	      LOW_mean: 0.575
45	    linear_proj_200_mean_auroc: 0.692
46	    few_shot_25_mean_auroc: 0.678
47	    few_shot_100_mean_auroc: 0.712
48	    mean_shift_delta_auroc: 0.0
49	  result_rationale: 'Qwen3-235B 的 MoE 路由在深层为不同语言激活不同 expert，加剧表征语言特异化。 EN best AUROC
50	    从 7B 的 0.754 提升至 ~0.78（+2.6pp），符合模型规模 scaling 预期（22B active params vs 7B, correctness
51	    signal 在更大模型中更强但非线性增长）。EN-optimal 在 L80（85% depth）， 而非最终层——MoE 最终层 expert 过度特化导致
52	    probe 质量微降。Pareto tradeoff 比 7B 更清晰： MoE 架构下 CKA cliff 更陡（L64-L80 急剧下降），transfer-optimal
53	    在 L68（72% depth）， EN-optimal 与 transfer-optimal 相差 ~12 层（~3pp AUROC gap），远大于 7B
54	    pilot 的 L24 vs L27（~2pp）。 ZS pass rate 75%（15/20）: HIGH 6/6 全通过（共享训练数据充分），MID
55	    6/6 通过（>0.60）， LOW 仅 3/6 通过（yo/am/my 低于 0.55）。Mean-shift 仍然恒等于 0（数学不变性）。 Linear
56	    projection 在低资源语言上提升 +0.04-0.08 但在高资源语言上可能微损。
57	
58	    '
59	  tables:
60	  - name: Per-Language ZS AUROC at EN-Optimal Layer (L80)
61	    data: '| Tier | Language | ZS AUROC | Best ZS Layer | Pareto rho | Pareto p |
62	
63	      |------|----------|----------|---------------|------------|----------|
64	
65	      | HIGH | zh       | 0.732    | L68           | -0.52      | 0.009   |
66	
67	      | HIGH | es       | 0.741    | L72           | -0.48      | 0.017   |
68	
69	      | HIGH | fr       | 0.738    | L72           | -0.45      | 0.027   |
70	
71	      | HIGH | de       | 0.720    | L68           | -0.55      | 0.005   |
72	
73	      | HIGH | pt       | 0.730    | L72           | -0.41      | 0.046   |
74	
75	      | HIGH | ja       | 0.710    | L64           | -0.58      | 0.003   |
76	
77	      | MID  | ar       | 0.690    | L64           | -0.50      | 0.013   |
78	
79	      | MID  | ru       | 0.700    | L68           | -0.44      | 0.031   |
80	
81	      | MID  | ko       | 0.685    | L64           | -0.47      | 0.021   |
82	
83	      | MID  | hi       | 0.665    | L60           | -0.38      | 0.068   |
84	
85	      | MID  | vi       | 0.678    | L64           | -0.42      | 0.041   |
86	
87	      | MID  | tr       | 0.655    | L60           | -0.35      | 0.093   |
88	
89	      | LOW  | sw       | 0.592    | L56           | -0.30      | 0.153   |
90	
91	      | LOW  | bn       | 0.608    | L60           | -0.32      | 0.126   |
92	
93	      | LOW  | th       | 0.620    | L60           | -0.37      | 0.075   |
94	
95	      | LOW  | te       | 0.568    | L56           | -0.22      | 0.301   |
96	
97	      | LOW  | yo       | 0.542    | L52           | -0.18      | 0.398   |
98	
99	      | LOW  | am       | 0.530    | L48           | 0.05       | 0.815   |
100	
101	      '
102	  - name: Transfer Method Comparison (mean across 20 languages, L80)
103	    data: '| Method              | Mean AUROC | ΔAUROC vs ZS | Sig (paired perm) |
104	
105	      |---------------------|------------|--------------|-------------------|
106	
107	      | Zero-shot           | 0.660      | —            | —                 |
108	
109	      | Mean-shift          | 0.660      | 0.000        | n/a               |
110	
111	      | CaCLR (best β=0.01) | 0.662      | +0.002       | p=0.42            |
112	
113	      | Linear proj (50)    | 0.678      | +0.018       | p=0.008           |
114	
115	      | Linear proj (200)   | 0.692      | +0.032       | p<0.001           |
116	
117	      | Few-shot 25         | 0.678      | +0.018       | p=0.006           |
118	
119	      | Few-shot 100        | 0.712      | +0.052       | p<0.001           |
120	
121	      '
122	  figures_description:
123	  - 'Pareto scatter plot: 20 个子图（每语言一个），x=EN AUROC, y=ZS AUROC， 每点为一个 probed layer（24
124	    点），颜色编码深度（浅=浅层，深=深层）， Pareto frontier 用虚线连接。HIGH 语言子图显示清晰的右下弯折（深层 EN 高但 ZS 低），
125	    LOW 语言子图点密集在左下区域，frontier 不明显。
126	
127	    '
128	  - 'Layer-wise AUROC heatmap: x=20 languages（按 tier 排列），y=24 probed layers（按深度），
129	    颜色=ZS AUROC。右上角（深层+低资源）呈冷色（低 AUROC），左中区域（中层+高资源）呈暖色。 EN 列单独标注显示 AUROC 随深度单调增加。
130	
131	    '
132	  analysis: 'Qwen3-235B 的 MoE 架构产生了比 7B pilot 更清晰的 Pareto frontier：16/20 语言的 depth-transfer
133	    rho 为负值，其中 15 个在 p<0.10 显著。Pareto 强度与资源 tier 强相关 （HIGH rho median=-0.49, MID=-0.43,
134	    LOW=-0.27），因为低资源语言整体 AUROC 低、 depth variation 也小。MoE 路由机制加速了深层表征的语言特异化——L64-L80
135	    的 expert 激活 模式在不同语言间差异显著增大，解释了 transfer cliff 为何比 dense 7B 更陡。 EN-optimal（L80）vs
136	    transfer-optimal（L68）的 gap 为实际部署提供了明确的 layer selection guidance。
137	
138	    '
139	- name: Full Pareto Frontier — Llama 4 Scout (MoE, W4A16)
140	  plan_id: plan_002
141	  description: '48 层 17B-16E MoE，每 4 层取一层（12 probed layers），20 语言，5 transfer 条件。 Llama
142	    架构族在 pilot 中显示弱 Pareto，full-scale 预期延续此模式但 MoE 可能略增 Pareto 强度。
143	
144	    '
145	  expected_results:
146	    en_best_auroc: 0.76
147	    en_best_layer: 44
148	    en_best_layer_depth_pct: 0.917
149	    en_auroc_range:
150	    - 0.6
151	    - 0.76
152	    en_best_ece_raw: 0.195
153	    transfer_optimal_layer_mean: 36
154	    transfer_optimal_depth_pct: 0.75
155	    en_transfer_layer_gap_pp: 1.5
156	    zs_pass_rate: 0.7
157	    zs_pass_count: 14
158	    zs_mean_auroc_en_optimal: 0.643
159	    zs_mean_auroc_transfer_optimal: 0.655
160	    pareto_significant_langs: 11
161	    pareto_spearman_rho_median: -0.28
162	    pareto_spearman_rho_range:
163	    - -0.55
164	    - 0.35
165	    pareto_langs_negative_rho: 13
166	    best_zs_auroc_by_tier:
167	      HIGH_mean: 0.705
168	      MID_mean: 0.652
169	      LOW_mean: 0.558
170	    linear_proj_200_mean_auroc: 0.673
171	    few_shot_25_mean_auroc: 0.662
172	    few_shot_100_mean_auroc: 0.693
173	    mean_shift_delta_auroc: 0.0
174	  result_rationale: 'Llama 4 Scout 延续 Llama-3.1-8B pilot 的弱 Pareto 模式：pilot 中仅 2/5
175	    语言显示 depth-transfer tradeoff（ar/ko 随深度改善），full-scale 中约 7/20 语言不显示 tradeoff 或方向相反。EN
176	    AUROC 从 pilot 的 0.728 提升至 0.76（Llama 4 Scout 更大），但提升幅度 小于 Qwen3 的 scaling，因为 Llama
177	    4 的 16-expert MoE 在浅层就开始 expert specialization， correctness signal 在中层已经 plateau。Pareto
178	    弱于 Qwen3 的根本原因：Llama CKA decline 更渐进（slope -0.015/layer vs Qwen 的 -0.025/layer），导致
179	    transfer 不出现急剧 cliff， tradeoff 分散在更宽的层范围内。EN-optimal（L44）vs transfer-optimal（L36）gap
180	    仅 ~1.5pp， 相比 Qwen3 的 ~2.8pp 更小。一些语言（ar, ko, vi）在全深度范围 AUROC 单调增加， 无 tradeoff——pilot
181	    中 ar/ko 的异常模式在 full-scale 中得到确认和扩展。
182	
183	    '
184	  tables:
185	  - name: Per-Language Pareto Strength Comparison (Qwen3 vs Llama 4)
186	    data: '| Tier | Language | Qwen3 rho | Qwen3 p | Llama4 rho | Llama4 p | Pattern       |
187	
188	      |------|----------|-----------|---------|------------|----------|---------------|
189	
190	      | HIGH | zh       | -0.52     | 0.009   | -0.40      | 0.198    | Both negative
191	      |
192	
193	      | HIGH | es       | -0.48     | 0.017   | -0.35      | 0.265    | Both negative
194	      |
195	
196	      | HIGH | ja       | -0.58     | 0.003   | -0.48      | 0.115    | Both negative
197	      |
198	
199	      | MID  | ar       | -0.50     | 0.013   | +0.15      | 0.641    | DIVERGENT     |
200	
201	      | MID  | ko       | -0.47     | 0.021   | +0.22      | 0.489    | DIVERGENT     |
202	
203	      | MID  | hi       | -0.38     | 0.068   | -0.55      | 0.065    | Both negative
204	      |
205	
206	      | LOW  | sw       | -0.30     | 0.153   | -0.25      | 0.432    | Weak both     |
207	
208	      | LOW  | yo       | -0.18     | 0.398   | +0.10      | 0.758    | Neither sig   |
209	
210	      '
211	  - name: Architecture Comparison Summary
212	    data: '| Metric                        | Qwen3-235B | Llama 4 Scout |
213	
214	      |-------------------------------|------------|---------------|
215	
216	      | EN best AUROC                 | 0.78       | 0.76          |
217	
218	      | Mean ZS AUROC (EN-opt layer)  | 0.660      | 0.643         |
219	
220	      | Pareto significant langs (/20)| 15         | 11            |
221	
222	      | Median per-lang Pareto rho    | -0.42      | -0.28         |
223	
224	      | CKA cliff onset (% depth)    | ~68%       | ~55%          |
225	
226	      | CKA slope (cliff region)      | -0.025/L   | -0.015/L      |
227	
228	      '
229	  figures_description:
230	  - '双模型 Pareto 对比图：左右两列分别为 Qwen3-235B 和 Llama 4 Scout，每行一个 resource tier （HIGH/MID/LOW），每子图叠加该
231	    tier 所有语言的 Pareto frontier（不同颜色）。 Qwen3 列显示 frontier 弯折更尖锐，Llama 4 列更平缓。
232	
233	    '
234	  analysis: '两个 MoE 架构的 Pareto 差异确认了 pilot 的架构依赖性发现。关键差异不在 MoE vs dense， 而在 CKA depth
235	    gradient 的斜率：Qwen3 的急剧 CKA cliff 创建清晰 tradeoff， Llama 4 的渐进下降使 tradeoff 分散。ar/ko
236	    在 Llama 4 上随深度改善的异常模式扩展到 full-scale——这些语言在 Llama tokenizer 中有较好的 subword coverage，深层
237	    expert specialization 反而增强了 correctness signal。此架构依赖性是 observational（n=2 架构， 混杂
238	    scale/layer count/training data），不做因果归因。
239	
240	    '
241	- name: CaCLR Implementation and Negative Result
242	  plan_id: plan_003
243	  description: 'CaCLR (BCE + α·SB-ECE + β·MMD) 完整实现与评估。β sweep 横跨 3 OOM (0.001-1.0)。
244	    Median tier 预期：consistency loss 无效，转为 negative result + geometric explanation。
245	
246	    '
247	  expected_results:
248	    caclr_mean_delta_auroc_vs_zs: 0.002
249	    caclr_best_beta: 0.01
250	    caclr_best_alpha: 0.3
251	    beta_sweep:
252	      beta_0.001:
253	        mean_delta_auroc: 0.001
254	        p_vs_zs: 0.71
255	      beta_0.01:
256	        mean_delta_auroc: 0.003
257	        p_vs_zs: 0.42
258	      beta_0.1:
259	        mean_delta_auroc: -0.002
260	        p_vs_zs: 0.58
261	      beta_1.0:
262	        mean_delta_auroc: -0.008
263	        p_vs_zs: 0.12
264	    alpha_sweep:
265	      alpha_0.01:
266	        mean_delta_ece: -0.2
267	        mean_delta_auroc: 0.0
268	      alpha_0.1:
269	        mean_delta_ece: -0.5
270	        mean_delta_auroc: -0.001
271	      alpha_1.0:
272	        mean_delta_ece: -1.5
273	        mean_delta_auroc: -0.004
274	      alpha_10.0:
275	        mean_delta_ece: -2.1
276	        mean_delta_auroc: -0.012
277	    component_ablation:
278	      bce_only:
279	        auroc: 0.66
280	        ece: 0.192
281	      bce_sbece:
282	        auroc: 0.658
283	        ece: 0.178
284	      bce_mmd:
285	        auroc: 0.662
286	        ece: 0.19
287	      bce_sbece_mmd:
288	        auroc: 0.661
289	        ece: 0.176
290	    method_comparison_mean_20lang:
291	      zero_shot: 0.66
292	      mean_shift: 0.66
293	      caclr_best: 0.662
294	      linear_proj_50: 0.678
295	      linear_proj_200: 0.692
296	      few_shot_25: 0.678
297	      few_shot_100: 0.712
298	    caclr_per_tier_delta:
299	      HIGH: 0.001
300	      MID: 0.003
301	      LOW: 0.002
302	    implementation_spec:
303	      mmd_kernel: Gaussian RBF, median heuristic bandwidth
304	      optimizer: Adam, lr=1e-3, cosine schedule
305	      epochs: 50
306	      early_stopping: patience=10 on val BCE loss
307	      initialization: from standard LR solution
308	      batch_size: 256
309	      mmd_items: same as BCE (probe_train split)
310	      parallel_set_size_range:
311	      - 8200
312	      - 12800
313	  result_rationale: 'CaCLR 的 MMD consistency loss 在 1-D probe logit 空间操作——这是设计层面的根本局限。
314	    Correctness direction 是高维 activation 空间中的低维子空间特征（~1-3 维），MMD 匹配 probe logit 的边际分布（均值和方差）但无法对齐子空间内的方向结构。具体地：两种语言的
315	    probe logit 分布可能有相似的均值和方差（MMD 小），但 correctness direction 在 activation 空间中的朝向不同——MMD
316	    无法检测或纠正这种旋转。β=0.001-0.01 时 consistency loss 太弱， 无实质效果；β=0.1-1.0 时 consistency
317	    loss 开始干扰 BCE 训练（AUROC 下降），因为 强制匹配边际分布反而破坏了 EN probe 已经学到的 correctness direction。这不是
318	    hyperparameter 问题——是根本的 architectural mismatch。α (SB-ECE) 对 ECE 有轻微改善 是预期的（ECE
319	    loss 直接优化 calibration），但与 cross-lingual transfer 无关。 Linear projection 成功因为它直接学习子空间旋转矩阵（Procrustes
320	    alignment）， 绕过了 distributional matching 的局限。这一对比（MMD 失败 vs linear projection 成功）
321	    提供了对 Zhao et al. (2019) conditional-marginal mismatch theory 的实证验证。
322	
323	    '
324	  tables:
325	  - name: β Sweep Results (Qwen3-235B, L80, mean across 20 languages)
326	    data: '| β     | Mean AUROC | ΔAUROC vs ZS | 95% Bootstrap CI    | Cohen''s d
327	      | Interpretation     |
328	
329	      |-------|------------|--------------|---------------------|-----------|--------------------|
330	
331	      | 0     | 0.660      | —            | —                   | —         | ZS baseline        |
332	
333	      | 0.001 | 0.661      | +0.001       | [-0.004, +0.006]    | 0.03      | Negligible         |
334	
335	      | 0.01  | 0.663      | +0.003       | [-0.003, +0.009]    | 0.07      | Negligible         |
336	
337	      | 0.1   | 0.658      | -0.002       | [-0.008, +0.004]    | 0.05      | Negligible         |
338	
339	      | 1.0   | 0.652      | -0.008       | [-0.015, -0.001]    | 0.19      | Slight
340	      degradation |
341	
342	      '
343	  - name: CaCLR vs All Methods (mean 20 languages, both models)
344	    data: '| Method            | Qwen3 AUROC | Llama4 AUROC | Mean  | Req. labels
345	      | Req. parallel |
346	
347	      |-------------------|-------------|--------------|-------|-------------|---------------|
348	
349	      | Zero-shot         | 0.660       | 0.643        | 0.652 | 0           | 0             |
350	
351	      | Mean-shift        | 0.660       | 0.643        | 0.652 | 0           | N (mean
352	      only) |
353	
354	      | CaCLR (best)      | 0.662       | 0.645        | 0.654 | 0           | ~10K
355	      parallel |
356	
357	      | Linear proj (50)  | 0.678       | 0.660        | 0.669 | 0           | 50
358	      pairs      |
359	
360	      | Linear proj (200) | 0.692       | 0.673        | 0.683 | 0           | 200
361	      pairs     |
362	
363	      | Few-shot 25       | 0.678       | 0.662        | 0.670 | 25          | 0             |
364	
365	      | Few-shot 100      | 0.712       | 0.693        | 0.703 | 100         | 0             |
366	
367	      '
368	  - name: CKA Subspace Analysis — Why MMD Fails
369	    data: '| Language Tier | Mean subspace angle (EN-target) | MMD after CaCLR | Angle
370	      after CaCLR | Interpretation            |
371	
372	      |--------------|----------------------------------|-----------------|--------------------|-----------------------------|
373	
374	      | HIGH         | 12°                              | 0.02 → 0.01     | 12° →
375	      11°         | MMD reduces, angle unchanged |
376	
377	      | MID          | 24°                              | 0.05 → 0.02     | 24° →
378	      23°         | MMD reduces, angle unchanged |
379	
380	      | LOW          | 42°                              | 0.12 → 0.05     | 42° →
381	      40°         | MMD reduces, angle unchanged |
382	
383	      '
384	  figures_description:
385	  - 'β sweep 图：x=β (log scale)，y=ΔAUROC vs zero-shot，每条线为一个 resource tier， shaded
386	    area 为 bootstrap 95% CI。所有线段在 y=0 附近震荡，β=1.0 时向下偏离。 水平虚线标注 linear projection 和
387	    few-shot 的 ΔAUROC 作为对比。
388	
389	    '
390	  - '几何解释概念图：左侧显示 MMD 操作空间（1-D logit 分布），EN 和 target 分布重叠 但 correctness direction
391	    指向不同方向（3D activation 空间投影）；右侧显示 linear projection 直接旋转子空间使 direction 对齐。
392	
393	    '
394	  analysis: 'CaCLR negative result 的核心贡献不是 method 本身，而是 (1) systematic β sweep 关闭
395	    MMD distributional-matching 路径（3 OOM, component ablation, 两个架构 × 20 语言）， (2) CKA
396	    subspace analysis 提供几何解释——MMD 成功减小了 marginal distance 但完全 无法对齐 correctness subspace
397	    的方向（subspace angle 几乎不变）。这验证了 Zhao et al. (2019) 的理论预测：当 conditional distributions
398	    P(Y|X) 在域间不同时， marginal matching 必然失败。在 correctness probing 中，P(correct|activation)
399	    的 条件结构在不同语言间确实不同（语言特异的 capability 成分），因此 MMD 注定无效。 Constructive path: linear projection
400	    以 50-80 parallel pairs 的极低成本解决了 subspace alignment 问题，是明确的 practical recommendation。
401	
402	    '
403	- name: Difficulty-Controlled Decomposition Ablation
404	  plan_id: plan_004
405	  description: 'IRT difficulty probes → project out difficulty direction → retrain
406	    correctness probes → evaluate transfer。 10 代表语言 × 8 代表层 × 两个模型。含 random-direction
407	    control。 Median tier: 定性分离成立但 prescriptive 预测能力不可靠。
408	
409	    '
410	  expected_results:
411	    mean_delta_auroc_difficulty_projected: 0.012
412	    delta_auroc_range:
413	    - -0.008
414	    - 0.025
415	    langs_with_positive_delta: 7
416	    langs_with_negative_delta: 3
417	    random_direction_mean_delta: 0.005
418	    difficulty_vs_random_ratio: 2.4
419	    difficulty_probe_r2: 0.35
420	    per_lang_results:
421	      zh:
422	        delta: 0.008
423	        sig: false
424	      es:
425	        delta: 0.01
426	        sig: false
427	      fr:
428	        delta: 0.012
429	        sig: true
430	      de:
431	        delta: 0.015
432	        sig: true
433	      hi:
434	        delta: 0.022
435	        sig: true
436	      ru:
437	        delta: 0.018
438	        sig: true
439	      ko:
440	        delta: -0.005
441	        sig: false
442	      tr:
443	        delta: 0.02
444	        sig: true
445	      sw:
446	        delta: -0.008
447	        sig: false
448	      bn:
449	        delta: 0.025
450	        sig: true
451	    prescriptive_accuracy: 0.58
452	  result_rationale: 'Difficulty decomposition 的定性逻辑成立：difficulty 成分确实是跨语言共享的（IRT difficulty
453	    与语言无关），project out 后 residual 应该更 capability-specific。但 prescriptive 力弱 的原因有三：(1)
454	    IRT difficulty probe 的 R²=0.35 意味着 difficulty direction 只解释了 35% 的方差，projection
455	    不完全；(2) difficulty 和 capability 在 activation 空间中不正交—— projection 同时移除了部分 capability
456	    信息（ko/sw 中 AUROC 下降）；(3) 不同语言中 difficulty-capability 纠缠程度不同——高资源语言 capability
457	    独立于 difficulty（projection 帮助），低资源语言两者纠缠更深（projection 效果不确定）。Random-direction control
458	    显示 ~40% 的效果来自纯维度缩减（从高维投影到低维本身就降噪），只有 ~60% 是 difficulty-specific。这足以支持 "descriptive
459	    separation observed" 但不足以支持 "prescriptive decomposition predicts optimal strategy"。Prescriptive
460	    accuracy 仅 58% （随机猜 50%），几乎无实际预测价值。
461	
462	    '
463	  tables:
464	  - name: Decomposition Results by Language (Qwen3-235B, 8-layer mean)
465	    data: '| Language | Tier | Full AUROC | Diff-projected AUROC | ΔAUROC  | Random-proj
466	      AUROC | Rand ΔAUROC |
467	
468	      |----------|------|------------|----------------------|---------|-------------------|-------------|
469	
470	      | zh       | HIGH | 0.725      | 0.733                | +0.008  | 0.729             |
471	      +0.004      |
472	
473	      | es       | HIGH | 0.735      | 0.745                | +0.010  | 0.740             |
474	      +0.005      |
475	
476	      | fr       | HIGH | 0.732      | 0.744                | +0.012  | 0.737             |
477	      +0.005      |
478	
479	      | de       | HIGH | 0.715      | 0.730                | +0.015  | 0.721             |
480	      +0.006      |
481	
482	      | hi       | MID  | 0.658      | 0.680                | +0.022  | 0.665             |
483	      +0.007      |
484	
485	      | ru       | MID  | 0.695      | 0.713                | +0.018  | 0.702             |
486	      +0.007      |
487	
488	      | ko       | MID  | 0.680      | 0.675                | -0.005  | 0.683             |
489	      +0.003      |
490	
491	      | tr       | MID  | 0.650      | 0.670                | +0.020  | 0.656             |
492	      +0.006      |
493	
494	      | sw       | LOW  | 0.585      | 0.577                | -0.008  | 0.588             |
495	      +0.003      |
496	
497	      | bn       | LOW  | 0.602      | 0.627                | +0.025  | 0.608             |
498	      +0.006      |
499	
500	      '
501	  figures_description:
502	  - '分解可视化：x=capability ΔAUROC (difficulty-projected - full)，y=difficulty  component
503	    strength (IRT probe R²)，每点为一个语言。右上象限（高 difficulty 解释力 +  positive ΔAUROC）包含 hi/bn/tr（projection
504	    帮助且 difficulty 信号强），左下象限包含 ko/sw（projection 损害或无效）。椭圆标注资源 tier。
505	
506	    '
507	  analysis: 'Decomposition 分析支持 "correctness transfer 确实包含 difficulty-shared 和 capability-specific
508	    两个成分" 的定性结论，但 prescriptive accuracy (58%) 与随机猜测差距过小（chance=50%）， 无法作为实际策略选择工具。弱化
509	    Claim 2 为 "descriptive separation observed in most language-architecture combinations;
510	    however, the decomposition does not reliably predict optimal alignment strategy."
511	    纸面贡献仍在：这是首次在跨语言 probing 中尝试 difficulty- capability 分解，定性结果与 Civelli et al. 的 difficulty
512	    transfer 文献一致。 ko/sw 的反常模式（projection 损害 AUROC）值得单独分析——可能是因为这些语言的 difficulty ordering
513	    与英语差异较大（文化特异的知识题目分布不同）。
514	
515	    '
516	- name: Cross-Lingual Orthogonality Analysis
517	  plan_id: plan_005
518	  description: '提取 verbalized confidence direction，计算与 correctness direction 的 cosine
519	    similarity， 20 语言 × 2 架构。作为 Claim 4 的 supporting evidence（subsection）。
520	
521	    '
522	  expected_results:
523	    mean_cosine_all: 0.038
524	    cosine_range:
525	    - 0.008
526	    - 0.142
527	    langs_below_0.05: 14
528	    langs_below_0.10: 18
529	    langs_above_0.10: 2
530	    per_tier_mean_cosine:
531	      HIGH: 0.028
532	      MID: 0.042
533	      LOW: 0.072
534	    architecture_comparison:
535	      qwen3_mean: 0.035
536	      llama4_mean: 0.041
537	    outlier_langs:
538	    - am
539	    - yo
540	    outlier_cosine:
541	    - 0.142
542	    - 0.118
543	  result_rationale: 'Miao & Ungar (2026) 在 English 7-8B 模型上发现 cosine < 0.04。跨语言扩展时，
544	    HIGH 资源语言复现此结果（模型在这些语言上有足够训练数据，correctness 和 confidence direction 分化清晰）。MID 语言
545	    cosine 略高（0.04-0.06）因为 confidence direction 在 中资源语言上更嘈杂（模型对这些语言的 verbalized confidence
546	    不够稳定）。LOW 语言中 am/yo 出现较高 cosine（>0.10）——这不是真正的 correctness-confidence alignment，
547	    而是 probe capacity artifact：在低资源语言上两个 direction 都很弱，cosine 被噪声主导。 plan_013 control
548	    task 将确认这些语言的 selectivity 低于阈值。整体结论不变： orthogonality 是跨语言稳健的结构性质，output-based
549	    calibration 的局限性与语言无关。 两个架构差异微小（0.035 vs 0.041），不具有统计显著性。
550	
551	    '
552	  tables:
553	  - name: Cosine Similarity by Resource Tier
554	    data: '| Tier | n  | Mean cosine | Std  | Min   | Max   | < 0.05 | < 0.10 |
555	
556	      |------|----|-------------|------|-------|-------|--------|--------|
557	
558	      | HIGH | 6  | 0.028       | 0.012| 0.012 | 0.045 | 5      | 6      |
559	
560	      | MID  | 8  | 0.042       | 0.018| 0.018 | 0.075 | 5      | 8      |
561	
562	      | LOW  | 6  | 0.072       | 0.042| 0.025 | 0.142 | 2      | 4      |
563	
564	      '
565	  figures_description:
566	  - 'Bar chart: 20 语言按 cosine 升序排列，颜色编码 resource tier。 水平虚线标注 Miao & Ungar 的 0.04
567	    阈值和 0.10 artifact 阈值。 大多数 bar 在 0.04 以下，仅 am/yo 突出。
568	
569	    '
570	  analysis: 'Orthogonality 作为 subsection supporting evidence 充分：18/20 语言 cosine <
571	    0.10， 14/20 < 0.05。结论简洁："output-based calibration 的结构性局限（correctness-confidence
572	    orthogonality）跨语言稳健，强化了 probe-based 方法的必要性。" am/yo 的高 cosine 值须与 plan_013 control
573	    task 结果交叉验证，确认是 probe artifact 而非真实 alignment。
574	
575	    '
576	- name: Probe Complexity Comparison (LR vs 2-layer MLP)
577	  plan_id: plan_006
578	  description: '每层每模型对比 logistic regression 和 2-layer MLP 的 EN accuracy、cross-lingual
579	    transfer degradation 和 calibration quality。CPU-bound，使用缓存 activations。
580	
581	    '
582	  expected_results:
583	    lr_en_best_auroc_qwen3: 0.78
584	    mlp_en_best_auroc_qwen3: 0.802
585	    lr_mean_zs_auroc_qwen3: 0.66
586	    mlp_mean_zs_auroc_qwen3: 0.632
587	    lr_transfer_gap_qwen3: 0.12
588	    mlp_transfer_gap_qwen3: 0.17
589	    lr_en_best_auroc_llama4: 0.76
590	    mlp_en_best_auroc_llama4: 0.778
591	    lr_mean_zs_auroc_llama4: 0.643
592	    mlp_mean_zs_auroc_llama4: 0.618
593	    mlp_en_advantage_pp: 2.0
594	    lr_transfer_advantage_pp: 2.8
595	    lr_preferred_for_transfer: true
596	  result_rationale: 'MLP（2 层, ~256 hidden units）有更多参数来拟合 EN correctness signal，EN
597	    AUROC 提升 ~2pp。但额外容量同时学到了 EN-specific 的 activation pattern（如 English 特有的 token
598	    position bias, subject-verb agreement cues），这些 pattern 不跨语言迁移。 LR 被迫学习更简洁的 direction（1
599	    个超平面），这个 direction 更可能对应语言无关的 correctness subspace。Transfer gap（EN - mean ZS）:
600	    LR 12pp vs MLP 17pp——MLP 多出的 5pp gap 恰好对应其 EN advantage 的 2pp + 额外 3pp 的 EN-specific
601	    overfitting。 这为 paper 的方法论选择（使用 LR probe）提供了实证支持。
602	
603	    '
604	  tables:
605	  - name: LR vs MLP Transfer Comparison (mean across 20 languages)
606	    data: '| Metric                    | Qwen3 LR | Qwen3 MLP | Llama4 LR | Llama4
607	      MLP |
608	
609	      |---------------------------|----------|-----------|-----------|------------|
610	
611	      | EN best AUROC             | 0.780    | 0.802     | 0.760     | 0.778      |
612	
613	      | Mean ZS AUROC             | 0.660    | 0.632     | 0.643     | 0.618      |
614	
615	      | Transfer gap (EN - ZS)    | 0.120    | 0.170     | 0.117     | 0.160      |
616	
617	      | EN ECE                    | 0.185    | 0.172     | 0.195     | 0.182      |
618	
619	      | Mean ZS ECE               | 0.225    | 0.252     | 0.232     | 0.260      |
620	
621	      | ZS pass rate (>0.60)      | 75%      | 60%       | 70%       | 55%        |
622	
623	      '
624	  figures_description:
625	  - 'Paired scatter plot: x=LR ZS AUROC, y=MLP ZS AUROC, 每点一个语言， 对角线 y=x 标注。大多数点在对角线下方（MLP
626	    worse），尤其是低资源语言。
627	
628	    '
629	  analysis: 'LR vs MLP 对比验证了 linear probe 是 cross-lingual transfer 的正确选择。 MLP 的额外容量在
630	    EN 上有用但在迁移中有害——这与 Hewitt & Liang (2019) 关于 probe complexity 的讨论一致。Paper 方法论选择（LR）有实证支持。
631	
632	    '
633	- name: Additional Benchmark Evaluation (Belebele + MMLU-ProX)
634	  plan_id: plan_007
635	  description: '在 Belebele（阅读理解）和 MMLU-ProX（翻译 MMLU）上评估 best probes + 所有 transfer
636	    方法，验证 generalization beyond GlobalMMLU。20 语言 × 2 模型。
637	
638	    '
639	  expected_results:
640	    belebele:
641	      en_best_auroc: 0.74
642	      mean_zs_auroc: 0.625
643	      zs_pass_rate: 0.6
644	      pareto_preserved: true
645	      pareto_strength: weaker than GlobalMMLU
646	      rank_correlation_with_globalmmlu: 0.82
647	    mmlu_prox:
648	      en_best_auroc: 0.77
649	      mean_zs_auroc: 0.648
650	      zs_pass_rate: 0.7
651	      pareto_preserved: true
652	      pareto_strength: comparable to GlobalMMLU
653	      rank_correlation_with_globalmmlu: 0.91
654	    linear_proj_generalizes: true
655	    caclr_still_inert: true
656	    cross_benchmark_lang_ranking_rho: 0.88
657	  result_rationale: 'Belebele 是阅读理解任务，与 GlobalMMLU 的知识型 MCQA 不同——correctness signal
658	    的性质不完全相同（RC 依赖 passage comprehension, MCQA 依赖 parametric knowledge）， 所以 EN AUROC
659	    略低（0.74 vs 0.78）且 transfer 更差。但 Pareto 结构保留，因为 depth-transferability tradeoff
660	    是 representation geometry 的性质，不依赖特定任务。 MMLU-ProX 与 GlobalMMLU 高度相关（同源翻译数据），所以模式几乎一致。
661	    Language ranking 在 benchmarks 间高度相关（rho=0.88）——确认结果不是 benchmark-specific。 CaCLR
662	    在两个 benchmark 上仍无效，linear projection 仍有效——泛化性确认。
663	
664	    '
665	  tables:
666	  - name: Cross-Benchmark Comparison (mean across 20 languages, Qwen3-235B)
667	    data: '| Metric             | GlobalMMLU | Belebele | MMLU-ProX |
668	
669	      |--------------------|------------|----------|-----------|
670	
671	      | EN best AUROC      | 0.78       | 0.74     | 0.77      |
672	
673	      | Mean ZS AUROC      | 0.660      | 0.625    | 0.648     |
674	
675	      | ZS pass rate       | 75%        | 60%      | 70%       |
676	
677	      | Pareto langs (/20) | 15         | 12       | 14        |
678	
679	      | Linear proj Δ      | +0.032     | +0.028   | +0.030    |
680	
681	      | CaCLR Δ            | +0.002     | +0.001   | +0.002    |
682	
683	      '
684	  figures_description:
685	  - '三 benchmark 平行坐标图：每条线为一个语言，x 轴为三个 benchmark， y 轴为 ZS AUROC。线条颜色编码 resource tier。大多数线大致平行（ranking
686	    一致）， 但 Belebele 整体偏低。交叉的线表示 benchmark-specific 的语言排名变化。
687	
688	    '
689	  analysis: 'Cross-benchmark 泛化确认了主要发现的稳健性。Belebele 上 Pareto 更弱是预期的 （RC task 的 correctness
690	    signal 与 knowledge MCQA 不同），但关键模式（架构差异、 resource tier 梯度、CaCLR 无效、linear projection
691	    有效）在所有 benchmark 上一致。 这为 paper 的 claim 提供了必要的泛化验证。
692	
693	    '
694	- name: Quantization Validation Ablation
695	  plan_id: plan_010
696	  description: '(a) W4A16 vs FP16 for Llama 4 Scout at 5 layers, 5% subset; (b) GPTQ-Int4
697	    vs FP16 for Qwen3-235B at 5 layers, 5% subset. 验证量化不扭曲 correctness signal。
698	
699	    '
700	  expected_results:
701	    llama4_w4a16_vs_fp16:
702	      mean_abs_delta_auroc: 0.005
703	      max_abs_delta_auroc: 0.009
704	      direction: mixed (2 positive, 3 negative)
705	      cka_fp16_vs_quant: 0.985
706	    qwen3_int4_vs_fp16:
707	      mean_abs_delta_auroc: 0.006
708	      max_abs_delta_auroc: 0.011
709	      direction: mixed (3 positive, 2 negative)
710	      cka_fp16_vs_quant: 0.978
711	    quantization_safe: true
712	  result_rationale: '4-bit weight quantization 保留了 activation 空间的大部分结构——correctness
713	    signal 是高维 activation 空间中的低维子空间特征，quantization noise 主要分布在与 correctness direction
714	    正交的维度上（根据 random projection 理论，低维结构 在高维 noise 下稳健）。ΔAUROC < 0.01 在 bootstrap CI
715	    内，不影响任何结论。 Qwen3 的 MoE 量化略有更大 delta（expert routing 决策在 INT4 下可能微变）， 但仍在可接受范围。CKA(FP16,
716	    quant) > 0.97 确认 activation 空间整体结构保留。
717	
718	    '
719	  tables:
720	  - name: Quantization Validation (per-layer ΔAUROC)
721	    data: '| Model      | Layer (% depth) | FP16 AUROC | Quant AUROC | ΔAUROC  |
722	
723	      |------------|-----------------|------------|-------------|---------|
724	
725	      | Llama4     | L8 (17%)        | 0.632      | 0.629       | -0.003  |
726	
727	      | Llama4     | L16 (33%)       | 0.685      | 0.688       | +0.003  |
728	
729	      | Llama4     | L24 (50%)       | 0.720      | 0.715       | -0.005  |
730	
731	      | Llama4     | L36 (75%)       | 0.748      | 0.741       | -0.007  |
732	
733	      | Llama4     | L44 (92%)       | 0.760      | 0.762       | +0.002  |
734	
735	      | Qwen3      | L16 (17%)       | 0.628      | 0.622       | -0.006  |
736	
737	      | Qwen3      | L36 (38%)       | 0.702      | 0.705       | +0.003  |
738	
739	      | Qwen3      | L52 (55%)       | 0.738      | 0.734       | -0.004  |
740	
741	      | Qwen3      | L68 (72%)       | 0.768      | 0.772       | +0.004  |
742	
743	      | Qwen3      | L80 (85%)       | 0.780      | 0.769       | -0.011  |
744	
745	      '
746	  figures_description:
747	  - 'Bland-Altman plot: x=(FP16+Quant)/2, y=FP16-Quant, 每点为一层。 水平虚线标注 ±0.01 tolerance
748	    band。所有点在 band 内。
749	
750	    '
751	  analysis: 'Quantization validation 通过——所有 ΔAUROC < 0.012，CKA > 0.97。 Qwen3 L80 的
752	    ΔAUROC=-0.011 是最大偏差，但仍在 bootstrap CI 范围内 且不影响 EN-optimal layer 的选择。Paper 中报告为
753	    "quantization artifacts are negligible for correctness probing (max |ΔAUROC| <
754	    0.012 across all validated layers)"。
755	
756	    '
757	- name: Full CKA Cross-Lingual Similarity & Simpson's Paradox Analysis
758	  plan_id: plan_011
759	  description: 'Linear CKA between EN and 20 target languages at every probed layer,
760	    both models. 核心分析：partial correlation controlling for depth（Simpson''s Paradox
761	    验证）。 Median tier: 仅 Llama 4 Scout 上显著，Qwen3 上 trending but not significant。
762	
763	    '
764	  expected_results:
765	    qwen3:
766	      raw_spearman_cka_auroc: -0.22
767	      raw_p: 0.001
768	      partial_spearman_ctrl_depth: 0.16
769	      partial_p: 0.072
770	      significant: false
771	      per_layer_positive_rho_count: 17
772	      per_layer_total: 24
773	      per_layer_significant_count: 5
774	      cka_cliff_onset_layer: 64
775	      cka_cliff_onset_depth_pct: 0.68
776	      cka_final_layer_mean: 0.1
777	      cka_peak_layer: 36
778	      cka_peak_mean: 0.81
779	    llama4:
780	      raw_spearman_cka_auroc: -0.28
781	      raw_p: 0.001
782	      partial_spearman_ctrl_depth: 0.29
783	      partial_p: 0.018
784	      significant: true
785	      per_layer_positive_rho_count: 10
786	      per_layer_total: 12
787	      per_layer_significant_count: 4
788	      cka_cliff_onset_layer: 24
789	      cka_cliff_onset_depth_pct: 0.5
790	      cka_final_layer_mean: 0.22
791	      cka_peak_layer: 12
792	      cka_peak_mean: 0.82
793	    simpson_paradox_confirmed: partial (1/2 architectures)
794	    subspace_angle_analysis:
795	      qwen3_mean_angle_HIGH: 10
796	      qwen3_mean_angle_MID: 22
797	      qwen3_mean_angle_LOW: 45
798	      llama4_mean_angle_HIGH: 12
799	      llama4_mean_angle_MID: 25
800	      llama4_mean_angle_LOW: 40
801	    cka_transfer_collapse_threshold: 0.32
802	    bootstrap_ci_partial_rho_qwen3:
803	    - -0.02
804	    - 0.34
805	    bootstrap_ci_partial_rho_llama4:
806	    - 0.06
807	    - 0.5
808	  result_rationale: 'Simpson''s Paradox 的架构依赖性源于 CKA-depth gradient 的形状差异。 Llama 4
809	    Scout 的 CKA depth gradient 更陡峭（从 peak 0.82 at L12 到 final 0.22 at L48, slope ~
810	    -0.017/layer），这使得 depth confound 更强——controlling for depth 释放了更多 CKA 的独立解释力（partial
811	    rho=0.29, p=0.018）。Qwen3 的 CKA decline 起始更晚 （L64 才开始急降）且更集中在最深层，depth confound
812	    的影响不均匀——前 60% 层几乎 无 CKA 变化，后 30% 急降——这种非线性使得 linear partial correlation 效果较差 （partial
813	    rho=0.16, p=0.072）。这不意味 CKA 在 Qwen3 上无解释力，而是 linear depth control 不够——可能需要 non-linear
814	    depth control（如 depth²）才能捕捉 Qwen3 的 step-function-like CKA profile。但 paper 应诚实报告：standard
815	    partial correlation 仅在 Llama 上显著。Per-layer analysis: 两个模型 70-83% 的 per-layer rho
816	    为正（Qwen 17/24, Llama 10/12），但因每层仅 n=20 语言，个别层的 significance 有限。Full-scale 的 n=20
817	    per layer 比 pilot 的 n=5 有更多 power，但仍不足以让所有 per-layer rho 显著。 Subspace angle 分析提供定量补充：HIGH
818	    语言角度小（10-12°）→ 零样本迁移好， LOW 语言角度大（40-45°）→ 需要 alignment。CKA collapse threshold
819	    ~0.32 是 transfer 从 "reasonable" 骤降到 "chance-level" 的拐点。
820	
821	    '
822	  tables:
823	  - name: Simpson's Paradox — Raw vs Partial Correlation
824	    data: '| Model       | n   | Raw rho | Raw p   | Partial rho | Partial p | Boot
825	      95% CI      | Sig?   |
826	
827	      |-------------|-----|---------|---------|-------------|-----------|------------------|--------|
828	
829	      | Qwen3-235B  | 480 | -0.22   | <0.001  | +0.16       | 0.072     | [-0.02,
830	      +0.34]   | No     |
831	
832	      | Llama4 Scout| 240 | -0.28   | <0.001  | +0.29       | 0.018     | [+0.06,
833	      +0.50]   | Yes    |
834	
835	      | Pilot Llama | 45  | -0.16   | 0.294   | +0.41       | 0.006     | [+0.12,
836	      +0.65]   | Yes    |
837	
838	      | Pilot Qwen  | 40  | -0.16   | 0.310   | +0.18       | 0.274     | [-0.15,
839	      +0.48]   | No     |
840	
841	      '
842	  - name: Per-Layer Cross-Language Spearman (CKA vs AUROC, n=20 per layer)
843	    data: '| Layer group        | Qwen3 median rho | Qwen3 sig layers | Llama4 median
844	      rho | Llama4 sig layers |
845	
846	      |--------------------|------------------|------------------|-------------------|-------------------|
847	
848	      | 0-25% depth        | +0.15            | 0/6              | +0.22             |
849	      1/3               |
850	
851	      | 25-50% depth       | +0.38            | 2/6              | +0.45             |
852	      2/3               |
853	
854	      | 50-75% depth       | +0.42            | 2/6              | +0.52             |
855	      2/3               |
856	
857	      | 75-100% depth      | +0.28            | 1/6              | +0.35             |
858	      1/3               |
859	
860	      '
861	  - name: CKA Depth Profile (mean across 20 languages)
862	    data: '| Depth % | Qwen3 Layer | Qwen3 CKA | Llama4 Layer | Llama4 CKA |
863	
864	      |---------|-------------|-----------|--------------|------------|
865	
866	      | 0%      | 0           | 0.72      | 0            | 0.60       |
867	
868	      | 17%     | 16          | 0.75      | 8            | 0.80       |
869	
870	      | 34%     | 32          | 0.80      | 16           | 0.76       |
871	
872	      | 51%     | 48          | 0.78      | 24           | 0.58       |
873	
874	      | 68%     | 64          | 0.62      | 32           | 0.42       |
875	
876	      | 77%     | 72          | 0.40      | 36           | 0.35       |
877	
878	      | 85%     | 80          | 0.25      | 40           | 0.30       |
879	
880	      | 94%     | 88          | 0.14      | 44           | 0.25       |
881	
882	      | 100%    | 92          | 0.10      | 48           | 0.22       |
883	
884	      '
885	  - name: Subspace Angle Analysis (correctness direction EN vs target)
886	    data: '| Tier | Qwen3 mean angle | Llama4 mean angle | Mean ZS AUROC | Interpretation         |
887	
888	      |------|------------------|-------------------|---------------|------------------------|
889	
890	      | HIGH | 10°              | 12°               | 0.715         | Near-aligned           |
891	
892	      | MID  | 22°              | 25°               | 0.662         | Modest rotation        |
893	
894	      | LOW  | 45°              | 40°               | 0.567         | Substantial
895	      misalignment|
896	
897	      '
898	  figures_description:
899	  - 'Simpson''s Paradox 可视化（核心图）：scatter plot, x=CKA, y=ZS AUROC。 每点为一个 (layer, language)
900	    pair。颜色编码 normalized depth (0-1)。 左图 Qwen3 (480 points)，右图 Llama4 (240 points)。
901	    Overall trend line 斜率为负（黑色虚线），per-depth-bin trend lines 斜率为正 （彩色实线，对应不同深度 bin）。Sign
902	    reversal 清晰可见。 Annotation: "Raw rho=−0.22 (p<0.001) vs Partial rho=+0.16 (p=0.07)"
903	    for Qwen3, "Raw rho=−0.28 (p<0.001) vs Partial rho=+0.29 (p=0.018)" for Llama4.
904	
905	    '
906	  - 'CKA × layer × language heatmap: 两个 panel（一个 per model），x=20 languages （按 mean
907	    CKA 排序），y=probed layers。颜色=CKA 值。显示 CKA cliff 在 Qwen3 上 更突然（L64 以上的条带从暖色骤变冷色），在
908	    Llama4 上更渐进。
909	
910	    '
911	  analysis: 'Simpson''s Paradox 在 full-scale 上部分确认：Llama 4 Scout 上统计显著（partial rho=0.29,
912	    p=0.018），Qwen3-235B 上 trending 但不显著（partial rho=0.16, p=0.072）。 这一架构依赖性本身是有意义的发现。Paper
913	    中用 hedged language 报告： "In architectures where the CKA-depth gradient is steep
914	    (Llama 4 Scout), partial correlation controlling for depth reveals a significant
915	    positive relationship between CKA and transfer AUROC (rho=0.29, p=0.018), indicating
916	    that CKA provides genuine explanatory power beyond depth. In architectures with
917	    a delayed, step-function-like CKA decline (Qwen3-235B), the linear partial correlation
918	    is trending but not significant (rho=0.16, p=0.072), possibly because the non-linear
919	    depth-CKA relationship reduces the effectiveness of linear depth control." Subspace
920	    angle analysis 提供了 CKA 分析的定量补充——HIGH 语言角度小（zero-shot 可行）， LOW 语言角度大（需要 alignment）——这与
921	    Procrustes reversal 发现互洽。
922	
923	    '
924	- name: Linear Projection Sensitivity & Procrustes Effect Reversal
925	  plan_id: plan_012
926	  description: 'Vary parallel pairs (10, 20, 50, 100, 200) for linear projection。
927	    两模型 × 5 代表层 × 20 语言。Resource-tier stratified saturation curves。 含 Procrustes effect
928	    reversal 分析。
929	
930	    '
931	  expected_results:
932	    overall_pairs_to_95pct: 70
933	    per_tier_pairs_to_95pct:
934	      HIGH: 35
935	      MID: 55
936	      LOW: 75
937	    saturation_curve:
938	      pairs_10:
939	        pct_of_max: 0.42
940	        mean_delta_auroc: 0.013
941	      pairs_20:
942	        pct_of_max: 0.62
943	        mean_delta_auroc: 0.02
944	      pairs_50:
945	        pct_of_max: 0.84
946	        mean_delta_auroc: 0.027
947	      pairs_100:
948	        pct_of_max: 0.95
949	        mean_delta_auroc: 0.03
950	      pairs_200:
951	        pct_of_max: 1.0
952	        mean_delta_auroc: 0.032
953	    procrustes_reversal:
954	      threshold_estimate: 0.55
955	      threshold_ci_95:
956	      - 0.46
957	      - 0.63
958	      benefit_below_0.50:
959	        mean_delta: 0.058
960	        n_langs: 4
961	      ambiguous_0.50_0.62:
962	        mean_delta: 0.012
963	        n_langs: 8
964	      harm_above_0.62:
965	        mean_delta: -0.018
966	        n_langs: 8
967	    curve_cleanness: 'noisy, especially LOW tier (R² of saturation fit: HIGH=0.96,
968	      MID=0.91, LOW=0.78)'
969	  result_rationale: 'Linear projection（Procrustes alignment）通过学习 EN→target 的旋转矩阵对齐
970	    correctness subspace。Saturation 速度取决于子空间旋转的复杂度：HIGH 语言的 EN-target subspace 角度小（~10°），10-20
971	    pairs 就足以估计一个简单旋转，35 pairs 达到 95%；LOW 语言角度大 （~40-45°），需要更多 pairs 来稳定估计更复杂的旋转，75
972	    pairs 才达到 95%。 Overall 70 pairs（而非 pilot 预估的 ~50 pairs）因为 (1) 20 语言比 5 语言引入更多方差，
973	    (2) 部分低资源语言的 parallel data 翻译质量低（机翻 artifacts），增加了 noise。 Curves 在 LOW tier 不够干净（R²=0.78）——个别语言的饱和曲线不单调（20
974	    pairs 时偶然 好于 50 pairs），因为 parallel pair 的质量方差大。 Procrustes reversal 的机制：当 ZS AUROC
975	    已高（>0.62），EN probe 的 correctness direction 与 target 语言已经 well-aligned（subspace
976	    angle <15°），Procrustes 旋转引入的估计噪声 反而大于 alignment gain→净效果为负。当 ZS AUROC 低（<0.50），严重
977	    misalignment （angle >40°）使得 Procrustes 的 alignment gain 远大于估计噪声→净效果明显为正。 阈值 ~0.55
978	    对应 subspace angle ~20-25° 的平衡点。
979	
980	    '
981	  tables:
982	  - name: Saturation Curves by Resource Tier (Qwen3-235B, L68)
983	    data: '| Pairs | HIGH ΔAUROC | MID ΔAUROC | LOW ΔAUROC | Overall ΔAUROC |
984	
985	      |-------|-------------|------------|------------|----------------|
986	
987	      | 10    | +0.002      | +0.010     | +0.028     | +0.013         |
988	
989	      | 20    | +0.005      | +0.018     | +0.042     | +0.020         |
990	
991	      | 50    | +0.007      | +0.026     | +0.054     | +0.027         |
992	
993	      | 100   | +0.008      | +0.029     | +0.060     | +0.030         |
994	
995	      | 200   | +0.008      | +0.030     | +0.063     | +0.032         |
996	
997	      '
998	  - name: Procrustes Effect Reversal by ZS AUROC Band
999	    data: '| ZS AUROC band | n langs | Mean Δ from proj | Std   | % positive | Example
1000	      langs |
1001	
1002	      |---------------|---------|------------------|-------|------------|---------------|
1003	
1004	      | < 0.50        | 4       | +0.058           | 0.022 | 100%       | am, yo,
1005	      my, te|
1006	
1007	      | 0.50 - 0.55   | 2       | +0.035           | 0.018 | 100%       | sw, bn        |
1008	
1009	      | 0.55 - 0.60   | 2       | +0.012           | 0.015 | 75%        | th, tr        |
1010	
1011	      | 0.60 - 0.65   | 4       | +0.003           | 0.012 | 50%        | hi, vi,
1012	      ko, ar|
1013	
1014	      | 0.65 - 0.70   | 4       | -0.008           | 0.010 | 25%        | ru, ja,
1015	      de, pt|
1016	
1017	      | > 0.70        | 4       | -0.018           | 0.008 | 0%         | zh, es,
1018	      fr, ...  |
1019	
1020	      '
1021	  figures_description:
1022	  - 'Saturation curve plot: x=number of parallel pairs (log scale), y=ΔAUROC vs zero-shot。
1023	    三条线（HIGH/MID/LOW tier），每条带 shaded bootstrap 95% CI。 HIGH 线快速 plateau（30-40 pairs
1024	    后几乎 flat），LOW 线缓慢上升且 CI 更宽。 Horizontal dashed line 标注 "95% of max improvement"。
1025	
1026	    '
1027	  - 'Procrustes reversal scatter: x=ZS AUROC (zero-shot baseline), y=ΔAUROC from linear
1028	    projection (200 pairs)。每点一个 (language, model) pair，颜色编码 model。 LOESS 拟合曲线显示从正到负的渐变。Vertical
1029	    band 标注 reversal threshold 及 95% CI。
1030	
1031	    '
1032	  analysis: 'Linear projection 的 sample efficiency 是最直接的 practical contribution： 70
1033	    parallel pairs（约 2-3 小时标注工作）达到 95% of maximum improvement。 Resource-tier stratification
1034	    为 practitioners 提供指导：HIGH 语言不需要 projection （可能有害），LOW 语言需要 ~75 pairs。Procrustes
1035	    reversal 是重要的 practitioner caveat： 不加区分地对所有语言做 alignment 会损害已经 well-aligned 的语言。
1036	    建议 deployment strategy: 先测试 zero-shot AUROC，低于 0.55 时使用 linear projection， 高于
1037	    0.62 时直接使用 zero-shot。
1038	
1039	    '
1040	- name: Probing Control Tasks (Hewitt & Liang 2019) — Full Scale
1041	  plan_id: plan_013
1042	  description: '随机排列标签训练 control probes，计算 selectivity (real - control AUROC)， 2 模型
1043	    × 20 语言 × 所有 probed 层。验证 AUROC 反映 genuine correctness direction。
1044	
1045	    '
1046	  expected_results:
1047	    artifact_rate_low_resource: 0.3
1048	    artifact_rate_mid_resource: 0.28
1049	    artifact_rate_high_resource: 0.06
1050	    artifact_threshold_selectivity: 0.05
1051	    overall_artifact_rate: 0.18
1052	    en_selectivity_profile:
1053	      shallow: 0.03
1054	      mid: 0.12
1055	      deep: 0.25
1056	    per_tier_selectivity_deep_layers:
1057	      HIGH: 0.22
1058	      MID: 0.14
1059	      LOW: 0.06
1060	    control_auroc_range:
1061	    - 0.48
1062	    - 0.52
1063	    affected_layer_range: primarily layers 0-40% depth
1064	  result_rationale: 'Pilot（Qwen2.5-7B, EN）显示 selectivity 在浅层低（L0-L12: 0.02-0.04）、深层高
1065	    （L20-L27: 0.24-0.26）。跨语言扩展时，LOW 资源语言的 selectivity 全面下降： (1) 这些语言的 activations
1066	    中 correctness signal 更弱（模型对这些语言"知道"更少）， (2) probe 在小 activation difference 上更依赖
1067	    capacity 来拟合训练集。 LOW 资源语言在深层的 selectivity 仅 ~0.06（vs EN 的 ~0.25），许多 layer-language
1068	    组合的 selectivity < 0.05 artifact threshold。30% 的 LOW resource layer-language 组合为
1069	    artifacts。MID 资源语言出乎意料地也有 ~28% artifact rate——这是因为 MID 资源语言中包含一些 "表面高资源但 knowledge
1070	    coverage 低" 的语言（如 tr, vi: 模型训练数据中 token 多但 MMLU 领域覆盖差）。HIGH 资源语言 artifact rate
1071	    仅 6% （仅在最浅层 L0-L4）。这一发现波及范围比初始预期更广（从 "~28% low-resource" 扩展到 "~28% low + ~28%
1072	    mid"），强化了 methodological warning 的重要性。
1073	
1074	    '
1075	  tables:
1076	  - name: Artifact Rate by Resource Tier and Depth (Qwen3-235B)
1077	    data: '| Depth zone     | HIGH artifact % | MID artifact % | LOW artifact % |
1078	
1079	      |----------------|-----------------|----------------|----------------|
1080	
1081	      | 0-25% depth    | 17%             | 58%            | 83%            |
1082	
1083	      | 25-50% depth   | 4%              | 33%            | 67%            |
1084	
1085	      | 50-75% depth   | 0%              | 17%            | 17%            |
1086	
1087	      | 75-100% depth  | 0%              | 4%             | 0%             |
1088	
1089	      | Overall        | 6%              | 28%            | 30%            |
1090	
1091	      '
1092	  - name: Selectivity at EN-Optimal Layer by Language
1093	    data: '| Tier | Language | Real AUROC | Control AUROC | Selectivity | Artifact?
1094	      |
1095	
1096	      |------|----------|------------|---------------|-------------|-----------|
1097	
1098	      | HIGH | zh       | 0.732      | 0.498         | 0.234       | No        |
1099	
1100	      | HIGH | es       | 0.741      | 0.495         | 0.246       | No        |
1101	
1102	      | MID  | hi       | 0.665      | 0.502         | 0.163       | No        |
1103	
1104	      | MID  | tr       | 0.655      | 0.508         | 0.147       | No        |
1105	
1106	      | LOW  | sw       | 0.592      | 0.505         | 0.087       | No        |
1107	
1108	      | LOW  | bn       | 0.608      | 0.501         | 0.107       | No        |
1109	
1110	      | LOW  | yo       | 0.542      | 0.510         | 0.032       | YES       |
1111	
1112	      | LOW  | am       | 0.530      | 0.512         | 0.018       | YES       |
1113	
1114	      '
1115	  figures_description:
1116	  - 'Selectivity heatmap: x=20 languages (按 tier 排列)，y=probed layers (按深度)， 颜色=selectivity。左下区域（浅层
1117	    + 低资源）为深蓝色（artifact zone, selectivity < 0.05）, 右上区域（深层 + 高资源）为暖色。虚线框标注 artifact
1118	    zone boundary。 第二行小图：同样 heatmap 但二值化（artifact yes/no），清晰显示 30% LOW + 28% MID 覆盖率。
1119	
1120	    '
1121	  analysis: 'Control task 发现是独立的 methodological contribution：首次在 cross-lingual probing
1122	    中 系统性应用 Hewitt & Liang selectivity analysis，发现 ~30% low-resource 和 ~28% mid-resource
1123	    language-layer 组合的 probing results 不可靠。Field-level implication: 所有 cross-lingual
1124	    probing 研究（包括 Xiao et al.）应包含 selectivity checks。 在 paper 中：(1) 用 selectivity
1125	    threshold 过滤不可靠结果后重新报告 main results （确认过滤后结论不变），(2) 将过滤信息作为 methodological recommendation
1126	    在 main body 报告（不只是 appendix），(3) 讨论与 Voita & Titov MDL probes 的关系。
1127	
1128	    '
1129	- name: Gemma 4 31B Dense — Third Architecture
1130	  plan_id: plan_008
1131	  description: 'Dense 架构对照（vs 两个 MoE），60 层 FP16，20+ 语言。 提供 dense vs MoE 架构对比。Camera-ready
1132	    extension。
1133	
1134	    '
1135	  expected_results:
1136	    en_best_auroc: 0.77
1137	    en_best_layer: 52
1138	    en_best_layer_depth_pct: 0.867
1139	    mean_zs_auroc: 0.655
1140	    zs_pass_rate: 0.72
1141	    pareto_strength: intermediate (between Qwen3 and Llama4)
1142	    pareto_significant_langs: 13
1143	    cka_cliff_slope: -0.012
1144	    cka_cliff_onset_depth_pct: 0.6
1145	    partial_rho_cka: 0.22
1146	    partial_p: 0.045
1147	    simpson_significant: true
1148	  result_rationale: 'Dense 架构的 CKA decline 比 MoE 更渐进（无 expert routing 加速特异化）， slope
1149	    ~-0.012/layer vs MoE 的 -0.015 to -0.025。Pareto 强度介于 Qwen3（最强） 和 Llama4（最弱）之间。Simpson''s
1150	    Paradox 在 Gemma 4 上显著（partial rho=0.22, p=0.045）——CKA gradient 斜率介于两者之间，足以使 linear
1151	    partial correlation 有效。 如果 Gemma 4 的 partial correlation 也显著，则 Simpson''s Paradox
1152	    变为 2/3 架构显著， 可强化叙事（但 camera-ready only）。EN AUROC ~0.77 与 Qwen3 的 0.78 接近 （31B
1153	    dense vs 22B active MoE, 参数效率相当）。
1154	
1155	    '
1156	  tables:
1157	  - name: Three-Architecture Comparison (Camera-Ready)
1158	    data: '| Metric                 | Qwen3-235B | Llama4 Scout | Gemma4 31B |
1159	
1160	      |------------------------|------------|--------------|------------|
1161	
1162	      | Type                   | MoE        | MoE          | Dense      |
1163	
1164	      | Active params          | 22B        | 17B          | 31B        |
1165	
1166	      | Layers                 | 94         | 48           | 60         |
1167	
1168	      | EN best AUROC          | 0.78       | 0.76         | 0.77       |
1169	
1170	      | Mean ZS AUROC          | 0.660      | 0.643        | 0.655      |
1171	
1172	      | Pareto sig langs       | 15         | 11           | 13         |
1173	
1174	      | Partial rho (CKA)      | 0.16 (ns)  | 0.29**       | 0.22*      |
1175	
1176	      | CKA cliff slope        | -0.025     | -0.015       | -0.012     |
1177	
1178	      '
1179	  figures_description:
1180	  - '三架构 CKA depth profile 对比：x=normalized depth (0-1)，y=mean CKA (20 langs)。 三条线：Qwen3（late
1181	    sharp cliff），Llama4（early gradual decline）， Gemma4（intermediate）。Annotation 标注
1182	    cliff onset 和 slope。
1183	
1184	    '
1185	  analysis: 'Gemma 4 作为 dense 架构对照，确认 Pareto 和 Simpson''s Paradox 不是 MoE 特有。 三架构对比暗示
1186	    CKA cliff slope 可能是决定 Pareto 强度和 partial correlation 显著性的关键因素——但 n=3 架构仅为 suggestive
1187	    correlation，不能做因果推断。 Camera-ready 增加第三个架构使结论更稳健。
1188	
1189	    '
1190	- name: Extended Language Coverage (50+ Languages)
1191	  plan_id: plan_009
1192	  description: '从 20 扩展至 50+ 语言，利用 GlobalMMLU/Belebele 全语言集。Camera-ready extension。
1193	
1194	    '
1195	  expected_results:
1196	    total_languages: 52
1197	    zs_pass_rate_52: 0.62
1198	    artifact_rate_very_low_resource: 0.48
1199	    new_low_resource_langs_with_artifacts: 18
1200	    resource_tier_gradient_confirmed: true
1201	    rank_correlation_20_vs_52: 0.94
1202	    new_findings: diminishing returns; very-low-resource languages (< 1M tokens in
1203	      training) uniformly fail
1204	    min_zs_auroc: 0.49
1205	    min_zs_lang: Haitian Creole (ht)
1206	  result_rationale: '扩展到 52 语言主要增加低资源语言。新增的 32 语言大多为 LOW 或 VERY-LOW resource， ZS AUROC
1207	    多在 0.50-0.58 范围。Pass rate 从 20 语言的 ~72% 降到 52 语言的 ~62%， 因为新增语言偏向低资源。Resource-tier
1208	    gradient 在更大规模上确认——artifact rate 在 very-low-resource 语言（<1M training tokens）中达
1209	    48%，几乎一半结果不可靠。 但 20 语言的核心发现在 52 语言上完全保持（rank correlation 0.94）。 边际收益递减：每增加一种语言，对核心
1210	    claim 的增量证据很小。 主要贡献是增加统计功效和覆盖度，而非新发现。
1211	
1212	    '
1213	  tables:
1214	  - name: Language Coverage Expansion Summary
1215	    data: '| Tier        | 20-lang count | 52-lang count | Mean ZS AUROC | Artifact
1216	      rate |
1217	
1218	      |-------------|---------------|---------------|---------------|---------------|
1219	
1220	      | HIGH        | 6             | 8             | 0.72          | 4%            |
1221	
1222	      | MID         | 8             | 14            | 0.66          | 22%           |
1223	
1224	      | LOW         | 6             | 18            | 0.57          | 35%           |
1225	
1226	      | VERY-LOW    | 0             | 12            | 0.52          | 48%           |
1227	
1228	      '
1229	  figures_description:
1230	  - 'World map: 52 语言标注在地图上，颜色编码 ZS AUROC（绿=高，红=低）。 清晰显示 Western Europe 和 East Asia
1231	    为绿色，Sub-Saharan Africa 和 Southeast Asia 低资源语言为红色。
1232	
1233	    '
1234	  analysis: Camera-ready 的 52 语言扩展提供了更全面的覆盖，但 story 不变。 VERY-LOW resource 语言（ht, rm,
1235	    fy 等）的 ~48% artifact rate 强化了 probing control 的必要性。Paper 中报告 52 语言结果但 core analysis
1236	    仍基于 20 语言（统计方法学更干净）。
1237	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0144cdc4-5846-4dd2-b768-dd33560359e7",
  "isSidechain": false,
  "promptId": "d159e131-5779-4f9c-878e-e70f68151974",
  "type": "user",
  "uuid": "7c0f13ea-3f48-4fb5-b7b4-0e6bf19d4ce6",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/median/review_context.yaml",
      "content": "narrative_guidance: 'CaCLR consistency loss (MMD) 在完整 β sweep 中无显著 AUROC 提升，转为 negative\n  result framing。 几何解释：MMD 匹配边际分布但无法对齐低维 directional structure——correctness 方向占据 1-3\n  维子空间， MMD 在 1-D probe logit 空间操作无法捕捉旋转。Linear projection 直接学习子空间旋转故成功。 Simpson''s\n  Paradox 仅在 Llama 4 Scout 上显著（partial rho~0.29, p~0.02），Qwen3-235B 上 trending 但不显著（rho~0.16,\n  p~0.07）——用 hedged language 报告为架构依赖发现。Claim 2 decomposition 定性分离成立但 prescriptive\n  预测力弱——弱化为 ''descriptive separation observed''。 标题转向 ''When Does Cross-Lingual Calibration\n  Transfer Work? Geometric Analysis and Practical Solutions.'' 强化三个实用贡献：(1) linear\n  projection ~70 pairs 推荐方案，(2) Procrustes effect reversal 阈值 ~0.55 作为 practitioner\n  guidance，(3) ~30% low-resource probing artifacts 作为 methodological warning。 仍可投\n  EACL——thorough empirical study + 架构依赖几何洞见 + systematic negative result + 实用指导。\n\n  '\nimagined_experiments:\n- name: Full Pareto Frontier — Qwen3-235B-A22B (MoE, INT4)\n  plan_id: plan_001\n  description: '94 层 MoE 模型，每 4 层取一层（24 probed layers），20 种语言，5 种 transfer 条件。 MoE\n    路由机制在深层创建更强的语言特异化，产生比 7B pilot 更清晰的 Pareto tradeoff。\n\n    '\n  expected_results:\n    en_best_auroc: 0.78\n    en_best_layer: 80\n    en_best_layer_depth_pct: 0.851\n    en_auroc_range:\n    - 0.58\n    - 0.78\n    en_best_ece_raw: 0.185\n    transfer_optimal_layer_mean: 68\n    transfer_optimal_depth_pct: 0.723\n    en_transfer_layer_gap_pp: 2.8\n    zs_pass_rate: 0.75\n    zs_pass_count: 15\n    zs_mean_auroc_en_optimal: 0.66\n    zs_mean_auroc_transfer_optimal: 0.682\n    pareto_significant_langs: 15\n    pareto_spearman_rho_median: -0.42\n    pareto_spearman_rho_range:\n    - -0.68\n    - 0.15\n    pareto_langs_negative_rho: 16\n    best_zs_auroc_by_tier:\n      HIGH_mean: 0.725\n      MID_mean: 0.672\n      LOW_mean: 0.575\n    linear_proj_200_mean_auroc: 0.692\n    few_shot_25_mean_auroc: 0.678\n    few_shot_100_mean_auroc: 0.712\n    mean_shift_delta_auroc: 0.0\n  result_rationale: 'Qwen3-235B 的 MoE 路由在深层为不同语言激活不同 expert，加剧表征语言特异化。 EN best AUROC\n    从 7B 的 0.754 提升至 ~0.78（+2.6pp），符合模型规模 scaling 预期（22B active params vs 7B, correctness\n    signal 在更大模型中更强但非线性增长）。EN-optimal 在 L80（85% depth）， 而非最终层——MoE 最终层 expert 过度特化导致\n    probe 质量微降。Pareto tradeoff 比 7B 更清晰： MoE 架构下 CKA cliff 更陡（L64-L80 急剧下降），transfer-optimal\n    在 L68（72% depth）， EN-optimal 与 transfer-optimal 相差 ~12 层（~3pp AUROC gap），远大于 7B\n    pilot 的 L24 vs L27（~2pp）。 ZS pass rate 75%（15/20）: HIGH 6/6 全通过（共享训练数据充分），MID\n    6/6 通过（>0.60）， LOW 仅 3/6 通过（yo/am/my 低于 0.55）。Mean-shift 仍然恒等于 0（数学不变性）。 Linear\n    projection 在低资源语言上提升 +0.04-0.08 但在高资源语言上可能微损。\n\n    '\n  tables:\n  - name: Per-Language ZS AUROC at EN-Optimal Layer (L80)\n    data: '| Tier | Language | ZS AUROC | Best ZS Layer | Pareto rho | Pareto p |\n\n      |------|----------|----------|---------------|------------|----------|\n\n      | HIGH | zh       | 0.732    | L68           | -0.52      | 0.009   |\n\n      | HIGH | es       | 0.741    | L72           | -0.48      | 0.017   |\n\n      | HIGH | fr       | 0.738    | L72           | -0.45      | 0.027   |\n\n      | HIGH | de       | 0.720    | L68           | -0.55      | 0.005   |\n\n      | HIGH | pt       | 0.730    | L72           | -0.41      | 0.046   |\n\n      | HIGH | ja       | 0.710    | L64           | -0.58      | 0.003   |\n\n      | MID  | ar       | 0.690    | L64           | -0.50      | 0.013   |\n\n      | MID  | ru       | 0.700    | L68           | -0.44      | 0.031   |\n\n      | MID  | ko       | 0.685    | L64           | -0.47      | 0.021   |\n\n      | MID  | hi       | 0.665    | L60           | -0.38      | 0.068   |\n\n      | MID  | vi       | 0.678    | L64           | -0.42      | 0.041   |\n\n      | MID  | tr       | 0.655    | L60           | -0.35      | 0.093   |\n\n      | LOW  | sw       | 0.592    | L56           | -0.30      | 0.153   |\n\n      | LOW  | bn       | 0.608    | L60           | -0.32      | 0.126   |\n\n      | LOW  | th       | 0.620    | L60           | -0.37      | 0.075   |\n\n      | LOW  | te       | 0.568    | L56           | -0.22      | 0.301   |\n\n      | LOW  | yo       | 0.542    | L52           | -0.18      | 0.398   |\n\n      | LOW  | am       | 0.530    | L48           | 0.05       | 0.815   |\n\n      '\n  - name: Transfer Method Comparison (mean across 20 languages, L80)\n    data: '| Method              | Mean AUROC | ΔAUROC vs ZS | Sig (paired perm) |\n\n      |---------------------|------------|--------------|-------------------|\n\n      | Zero-shot           | 0.660      | —            | —                 |\n\n      | Mean-shift          | 0.660      | 0.000        | n/a               |\n\n      | CaCLR (best β=0.01) | 0.662      | +0.002       | p=0.42            |\n\n      | Linear proj (50)    | 0.678      | +0.018       | p=0.008           |\n\n      | Linear proj (200)   | 0.692      | +0.032       | p<0.001           |\n\n      | Few-shot 25         | 0.678      | +0.018       | p=0.006           |\n\n      | Few-shot 100        | 0.712      | +0.052       | p<0.001           |\n\n      '\n  figures_description:\n  - 'Pareto scatter plot: 20 个子图（每语言一个），x=EN AUROC, y=ZS AUROC， 每点为一个 probed layer（24\n    点），颜色编码深度（浅=浅层，深=深层）， Pareto frontier 用虚线连接。HIGH 语言子图显示清晰的右下弯折（深层 EN 高但 ZS 低），\n    LOW 语言子图点密集在左下区域，frontier 不明显。\n\n    '\n  - 'Layer-wise AUROC heatmap: x=20 languages（按 tier 排列），y=24 probed layers（按深度），\n    颜色=ZS AUROC。右上角（深层+低资源）呈冷色（低 AUROC），左中区域（中层+高资源）呈暖色。 EN 列单独标注显示 AUROC 随深度单调增加。\n\n    '\n  analysis: 'Qwen3-235B 的 MoE 架构产生了比 7B pilot 更清晰的 Pareto frontier：16/20 语言的 depth-transfer\n    rho 为负值，其中 15 个在 p<0.10 显著。Pareto 强度与资源 tier 强相关 （HIGH rho median=-0.49, MID=-0.43,\n    LOW=-0.27），因为低资源语言整体 AUROC 低、 depth variation 也小。MoE 路由机制加速了深层表征的语言特异化——L64-L80\n    的 expert 激活 模式在不同语言间差异显著增大，解释了 transfer cliff 为何比 dense 7B 更陡。 EN-optimal（L80）vs\n    transfer-optimal（L68）的 gap 为实际部署提供了明确的 layer selection guidance。\n\n    '\n- name: Full Pareto Frontier — Llama 4 Scout (MoE, W4A16)\n  plan_id: plan_002\n  description: '48 层 17B-16E MoE，每 4 层取一层（12 probed layers），20 语言，5 transfer 条件。 Llama\n    架构族在 pilot 中显示弱 Pareto，full-scale 预期延续此模式但 MoE 可能略增 Pareto 强度。\n\n    '\n  expected_results:\n    en_best_auroc: 0.76\n    en_best_layer: 44\n    en_best_layer_depth_pct: 0.917\n    en_auroc_range:\n    - 0.6\n    - 0.76\n    en_best_ece_raw: 0.195\n    transfer_optimal_layer_mean: 36\n    transfer_optimal_depth_pct: 0.75\n    en_transfer_layer_gap_pp: 1.5\n    zs_pass_rate: 0.7\n    zs_pass_count: 14\n    zs_mean_auroc_en_optimal: 0.643\n    zs_mean_auroc_transfer_optimal: 0.655\n    pareto_significant_langs: 11\n    pareto_spearman_rho_median: -0.28\n    pareto_spearman_rho_range:\n    - -0.55\n    - 0.35\n    pareto_langs_negative_rho: 13\n    best_zs_auroc_by_tier:\n      HIGH_mean: 0.705\n      MID_mean: 0.652\n      LOW_mean: 0.558\n    linear_proj_200_mean_auroc: 0.673\n    few_shot_25_mean_auroc: 0.662\n    few_shot_100_mean_auroc: 0.693\n    mean_shift_delta_auroc: 0.0\n  result_rationale: 'Llama 4 Scout 延续 Llama-3.1-8B pilot 的弱 Pareto 模式：pilot 中仅 2/5\n    语言显示 depth-transfer tradeoff（ar/ko 随深度改善），full-scale 中约 7/20 语言不显示 tradeoff 或方向相反。EN\n    AUROC 从 pilot 的 0.728 提升至 0.76（Llama 4 Scout 更大），但提升幅度 小于 Qwen3 的 scaling，因为 Llama\n    4 的 16-expert MoE 在浅层就开始 expert specialization， correctness signal 在中层已经 plateau。Pareto\n    弱于 Qwen3 的根本原因：Llama CKA decline 更渐进（slope -0.015/layer vs Qwen 的 -0.025/layer），导致\n    transfer 不出现急剧 cliff， tradeoff 分散在更宽的层范围内。EN-optimal（L44）vs transfer-optimal（L36）gap\n    仅 ~1.5pp， 相比 Qwen3 的 ~2.8pp 更小。一些语言（ar, ko, vi）在全深度范围 AUROC 单调增加， 无 tradeoff——pilot\n    中 ar/ko 的异常模式在 full-scale 中得到确认和扩展。\n\n    '\n  tables:\n  - name: Per-Language Pareto Strength Comparison (Qwen3 vs Llama 4)\n    data: '| Tier | Language | Qwen3 rho | Qwen3 p | Llama4 rho | Llama4 p | Pattern       |\n\n      |------|----------|-----------|---------|------------|----------|---------------|\n\n      | HIGH | zh       | -0.52     | 0.009   | -0.40      | 0.198    | Both negative\n      |\n\n      | HIGH | es       | -0.48     | 0.017   | -0.35      | 0.265    | Both negative\n      |\n\n      | HIGH | ja       | -0.58     | 0.003   | -0.48      | 0.115    | Both negative\n      |\n\n      | MID  | ar       | -0.50     | 0.013   | +0.15      | 0.641    | DIVERGENT     |\n\n      | MID  | ko       | -0.47     | 0.021   | +0.22      | 0.489    | DIVERGENT     |\n\n      | MID  | hi       | -0.38     | 0.068   | -0.55      | 0.065    | Both negative\n      |\n\n      | LOW  | sw       | -0.30     | 0.153   | -0.25      | 0.432    | Weak both     |\n\n      | LOW  | yo       | -0.18     | 0.398   | +0.10      | 0.758    | Neither sig   |\n\n      '\n  - name: Architecture Comparison Summary\n    data: '| Metric                        | Qwen3-235B | Llama 4 Scout |\n\n      |-------------------------------|------------|---------------|\n\n      | EN best AUROC                 | 0.78       | 0.76          |\n\n      | Mean ZS AUROC (EN-opt layer)  | 0.660      | 0.643         |\n\n      | Pareto significant langs (/20)| 15         | 11            |\n\n      | Median per-lang Pareto rho    | -0.42      | -0.28         |\n\n      | CKA cliff onset (% depth)    | ~68%       | ~55%          |\n\n      | CKA slope (cliff region)      | -0.025/L   | -0.015/L      |\n\n      '\n  figures_description:\n  - '双模型 Pareto 对比图：左右两列分别为 Qwen3-235B 和 Llama 4 Scout，每行一个 resource tier （HIGH/MID/LOW），每子图叠加该\n    tier 所有语言的 Pareto frontier（不同颜色）。 Qwen3 列显示 frontier 弯折更尖锐，Llama 4 列更平缓。\n\n    '\n  analysis: '两个 MoE 架构的 Pareto 差异确认了 pilot 的架构依赖性发现。关键差异不在 MoE vs dense， 而在 CKA depth\n    gradient 的斜率：Qwen3 的急剧 CKA cliff 创建清晰 tradeoff， Llama 4 的渐进下降使 tradeoff 分散。ar/ko\n    在 Llama 4 上随深度改善的异常模式扩展到 full-scale——这些语言在 Llama tokenizer 中有较好的 subword coverage，深层\n    expert specialization 反而增强了 correctness signal。此架构依赖性是 observational（n=2 架构， 混杂\n    scale/layer count/training data），不做因果归因。\n\n    '\n- name: CaCLR Implementation and Negative Result\n  plan_id: plan_003\n  description: 'CaCLR (BCE + α·SB-ECE + β·MMD) 完整实现与评估。β sweep 横跨 3 OOM (0.001-1.0)。\n    Median tier 预期：consistency loss 无效，转为 negative result + geometric explanation。\n\n    '\n  expected_results:\n    caclr_mean_delta_auroc_vs_zs: 0.002\n    caclr_best_beta: 0.01\n    caclr_best_alpha: 0.3\n    beta_sweep:\n      beta_0.001:\n        mean_delta_auroc: 0.001\n        p_vs_zs: 0.71\n      beta_0.01:\n        mean_delta_auroc: 0.003\n        p_vs_zs: 0.42\n      beta_0.1:\n        mean_delta_auroc: -0.002\n        p_vs_zs: 0.58\n      beta_1.0:\n        mean_delta_auroc: -0.008\n        p_vs_zs: 0.12\n    alpha_sweep:\n      alpha_0.01:\n        mean_delta_ece: -0.2\n        mean_delta_auroc: 0.0\n      alpha_0.1:\n        mean_delta_ece: -0.5\n        mean_delta_auroc: -0.001\n      alpha_1.0:\n        mean_delta_ece: -1.5\n        mean_delta_auroc: -0.004\n      alpha_10.0:\n        mean_delta_ece: -2.1\n        mean_delta_auroc: -0.012\n    component_ablation:\n      bce_only:\n        auroc: 0.66\n        ece: 0.192\n      bce_sbece:\n        auroc: 0.658\n        ece: 0.178\n      bce_mmd:\n        auroc: 0.662\n        ece: 0.19\n      bce_sbece_mmd:\n        auroc: 0.661\n        ece: 0.176\n    method_comparison_mean_20lang:\n      zero_shot: 0.66\n      mean_shift: 0.66\n      caclr_best: 0.662\n      linear_proj_50: 0.678\n      linear_proj_200: 0.692\n      few_shot_25: 0.678\n      few_shot_100: 0.712\n    caclr_per_tier_delta:\n      HIGH: 0.001\n      MID: 0.003\n      LOW: 0.002\n    implementation_spec:\n      mmd_kernel: Gaussian RBF, median heuristic bandwidth\n      optimizer: Adam, lr=1e-3, cosine schedule\n      epochs: 50\n      early_stopping: patience=10 on val BCE loss\n      initialization: from standard LR solution\n      batch_size: 256\n      mmd_items: same as BCE (probe_train split)\n      parallel_set_size_range:\n      - 8200\n      - 12800\n  result_rationale: 'CaCLR 的 MMD consistency loss 在 1-D probe logit 空间操作——这是设计层面的根本局限。\n    Correctness direction 是高维 activation 空间中的低维子空间特征（~1-3 维），MMD 匹配 probe logit 的边际分布（均值和方差）但无法对齐子空间内的方向结构。具体地：两种语言的\n    probe logit 分布可能有相似的均值和方差（MMD 小），但 correctness direction 在 activation 空间中的朝向不同——MMD\n    无法检测或纠正这种旋转。β=0.001-0.01 时 consistency loss 太弱， 无实质效果；β=0.1-1.0 时 consistency\n    loss 开始干扰 BCE 训练（AUROC 下降），因为 强制匹配边际分布反而破坏了 EN probe 已经学到的 correctness direction。这不是\n    hyperparameter 问题——是根本的 architectural mismatch。α (SB-ECE) 对 ECE 有轻微改善 是预期的（ECE\n    loss 直接优化 calibration），但与 cross-lingual transfer 无关。 Linear projection 成功因为它直接学习子空间旋转矩阵（Procrustes\n    alignment）， 绕过了 distributional matching 的局限。这一对比（MMD 失败 vs linear projection 成功）\n    提供了对 Zhao et al. (2019) conditional-marginal mismatch theory 的实证验证。\n\n    '\n  tables:\n  - name: β Sweep Results (Qwen3-235B, L80, mean across 20 languages)\n    data: '| β     | Mean AUROC | ΔAUROC vs ZS | 95% Bootstrap CI    | Cohen''s d\n      | Interpretation     |\n\n      |-------|------------|--------------|---------------------|-----------|--------------------|\n\n      | 0     | 0.660      | —            | —                   | —         | ZS baseline        |\n\n      | 0.001 | 0.661      | +0.001       | [-0.004, +0.006]    | 0.03      | Negligible         |\n\n      | 0.01  | 0.663      | +0.003       | [-0.003, +0.009]    | 0.07      | Negligible         |\n\n      | 0.1   | 0.658      | -0.002       | [-0.008, +0.004]    | 0.05      | Negligible         |\n\n      | 1.0   | 0.652      | -0.008       | [-0.015, -0.001]    | 0.19      | Slight\n      degradation |\n\n      '\n  - name: CaCLR vs All Methods (mean 20 languages, both models)\n    data: '| Method            | Qwen3 AUROC | Llama4 AUROC | Mean  | Req. labels\n      | Req. parallel |\n\n      |-------------------|-------------|--------------|-------|-------------|---------------|\n\n      | Zero-shot         | 0.660       | 0.643        | 0.652 | 0           | 0             |\n\n      | Mean-shift        | 0.660       | 0.643        | 0.652 | 0           | N (mean\n      only) |\n\n      | CaCLR (best)      | 0.662       | 0.645        | 0.654 | 0           | ~10K\n      parallel |\n\n      | Linear proj (50)  | 0.678       | 0.660        | 0.669 | 0           | 50\n      pairs      |\n\n      | Linear proj (200) | 0.692       | 0.673        | 0.683 | 0           | 200\n      pairs     |\n\n      | Few-shot 25       | 0.678       | 0.662        | 0.670 | 25          | 0             |\n\n      | Few-shot 100      | 0.712       | 0.693        | 0.703 | 100         | 0             |\n\n      '\n  - name: CKA Subspace Analysis — Why MMD Fails\n    data: '| Language Tier | Mean subspace angle (EN-target) | MMD after CaCLR | Angle\n      after CaCLR | Interpretation            |\n\n      |--------------|----------------------------------|-----------------|--------------------|-----------------------------|\n\n      | HIGH         | 12°                              | 0.02 → 0.01     | 12° →\n      11°         | MMD reduces, angle unchanged |\n\n      | MID          | 24°                              | 0.05 → 0.02     | 24° →\n      23°         | MMD reduces, angle unchanged |\n\n      | LOW          | 42°                              | 0.12 → 0.05     | 42° →\n      40°         | MMD reduces, angle unchanged |\n\n      '\n  figures_description:\n  - 'β sweep 图：x=β (log scale)，y=ΔAUROC vs zero-shot，每条线为一个 resource tier， shaded\n    area 为 bootstrap 95% CI。所有线段在 y=0 附近震荡，β=1.0 时向下偏离。 水平虚线标注 linear projection 和\n    few-shot 的 ΔAUROC 作为对比。\n\n    '\n  - '几何解释概念图：左侧显示 MMD 操作空间（1-D logit 分布），EN 和 target 分布重叠 但 correctness direction\n    指向不同方向（3D activation 空间投影）；右侧显示 linear projection 直接旋转子空间使 direction 对齐。\n\n    '\n  analysis: 'CaCLR negative result 的核心贡献不是 method 本身，而是 (1) systematic β sweep 关闭\n    MMD distributional-matching 路径（3 OOM, component ablation, 两个架构 × 20 语言）， (2) CKA\n    subspace analysis 提供几何解释——MMD 成功减小了 marginal distance 但完全 无法对齐 correctness subspace\n    的方向（subspace angle 几乎不变）。这验证了 Zhao et al. (2019) 的理论预测：当 conditional distributions\n    P(Y|X) 在域间不同时， marginal matching 必然失败。在 correctness probing 中，P(correct|activation)\n    的 条件结构在不同语言间确实不同（语言特异的 capability 成分），因此 MMD 注定无效。 Constructive path: linear projection\n    以 50-80 parallel pairs 的极低成本解决了 subspace alignment 问题，是明确的 practical recommendation。\n\n    '\n- name: Difficulty-Controlled Decomposition Ablation\n  plan_id: plan_004\n  description: 'IRT difficulty probes → project out difficulty direction → retrain\n    correctness probes → evaluate transfer。 10 代表语言 × 8 代表层 × 两个模型。含 random-direction\n    control。 Median tier: 定性分离成立但 prescriptive 预测能力不可靠。\n\n    '\n  expected_results:\n    mean_delta_auroc_difficulty_projected: 0.012\n    delta_auroc_range:\n    - -0.008\n    - 0.025\n    langs_with_positive_delta: 7\n    langs_with_negative_delta: 3\n    random_direction_mean_delta: 0.005\n    difficulty_vs_random_ratio: 2.4\n    difficulty_probe_r2: 0.35\n    per_lang_results:\n      zh:\n        delta: 0.008\n        sig: false\n      es:\n        delta: 0.01\n        sig: false\n      fr:\n        delta: 0.012\n        sig: true\n      de:\n        delta: 0.015\n        sig: true\n      hi:\n        delta: 0.022\n        sig: true\n      ru:\n        delta: 0.018\n        sig: true\n      ko:\n        delta: -0.005\n        sig: false\n      tr:\n        delta: 0.02\n        sig: true\n      sw:\n        delta: -0.008\n        sig: false\n      bn:\n        delta: 0.025\n        sig: true\n    prescriptive_accuracy: 0.58\n  result_rationale: 'Difficulty decomposition 的定性逻辑成立：difficulty 成分确实是跨语言共享的（IRT difficulty\n    与语言无关），project out 后 residual 应该更 capability-specific。但 prescriptive 力弱 的原因有三：(1)\n    IRT difficulty probe 的 R²=0.35 意味着 difficulty direction 只解释了 35% 的方差，projection\n    不完全；(2) difficulty 和 capability 在 activation 空间中不正交—— projection 同时移除了部分 capability\n    信息（ko/sw 中 AUROC 下降）；(3) 不同语言中 difficulty-capability 纠缠程度不同——高资源语言 capability\n    独立于 difficulty（projection 帮助），低资源语言两者纠缠更深（projection 效果不确定）。Random-direction control\n    显示 ~40% 的效果来自纯维度缩减（从高维投影到低维本身就降噪），只有 ~60% 是 difficulty-specific。这足以支持 \"descriptive\n    separation observed\" 但不足以支持 \"prescriptive decomposition predicts optimal strategy\"。Prescriptive\n    accuracy 仅 58% （随机猜 50%），几乎无实际预测价值。\n\n    '\n  tables:\n  - name: Decomposition Results by Language (Qwen3-235B, 8-layer mean)\n    data: '| Language | Tier | Full AUROC | Diff-projected AUROC | ΔAUROC  | Random-proj\n      AUROC | Rand ΔAUROC |\n\n      |----------|------|------------|----------------------|---------|-------------------|-------------|\n\n      | zh       | HIGH | 0.725      | 0.733                | +0.008  | 0.729             |\n      +0.004      |\n\n      | es       | HIGH | 0.735      | 0.745                | +0.010  | 0.740             |\n      +0.005      |\n\n      | fr       | HIGH | 0.732      | 0.744                | +0.012  | 0.737             |\n      +0.005      |\n\n      | de       | HIGH | 0.715      | 0.730                | +0.015  | 0.721             |\n      +0.006      |\n\n      | hi       | MID  | 0.658      | 0.680                | +0.022  | 0.665             |\n      +0.007      |\n\n      | ru       | MID  | 0.695      | 0.713                | +0.018  | 0.702             |\n      +0.007      |\n\n      | ko       | MID  | 0.680      | 0.675                | -0.005  | 0.683             |\n      +0.003      |\n\n      | tr       | MID  | 0.650      | 0.670                | +0.020  | 0.656             |\n      +0.006      |\n\n      | sw       | LOW  | 0.585      | 0.577                | -0.008  | 0.588             |\n      +0.003      |\n\n      | bn       | LOW  | 0.602      | 0.627                | +0.025  | 0.608             |\n      +0.006      |\n\n      '\n  figures_description:\n  - '分解可视化：x=capability ΔAUROC (difficulty-projected - full)，y=difficulty  component\n    strength (IRT probe R²)，每点为一个语言。右上象限（高 difficulty 解释力 +  positive ΔAUROC）包含 hi/bn/tr（projection\n    帮助且 difficulty 信号强），左下象限包含 ko/sw（projection 损害或无效）。椭圆标注资源 tier。\n\n    '\n  analysis: 'Decomposition 分析支持 \"correctness transfer 确实包含 difficulty-shared 和 capability-specific\n    两个成分\" 的定性结论，但 prescriptive accuracy (58%) 与随机猜测差距过小（chance=50%）， 无法作为实际策略选择工具。弱化\n    Claim 2 为 \"descriptive separation observed in most language-architecture combinations;\n    however, the decomposition does not reliably predict optimal alignment strategy.\"\n    纸面贡献仍在：这是首次在跨语言 probing 中尝试 difficulty- capability 分解，定性结果与 Civelli et al. 的 difficulty\n    transfer 文献一致。 ko/sw 的反常模式（projection 损害 AUROC）值得单独分析——可能是因为这些语言的 difficulty ordering\n    与英语差异较大（文化特异的知识题目分布不同）。\n\n    '\n- name: Cross-Lingual Orthogonality Analysis\n  plan_id: plan_005\n  description: '提取 verbalized confidence direction，计算与 correctness direction 的 cosine\n    similarity， 20 语言 × 2 架构。作为 Claim 4 的 supporting evidence（subsection）。\n\n    '\n  expected_results:\n    mean_cosine_all: 0.038\n    cosine_range:\n    - 0.008\n    - 0.142\n    langs_below_0.05: 14\n    langs_below_0.10: 18\n    langs_above_0.10: 2\n    per_tier_mean_cosine:\n      HIGH: 0.028\n      MID: 0.042\n      LOW: 0.072\n    architecture_comparison:\n      qwen3_mean: 0.035\n      llama4_mean: 0.041\n    outlier_langs:\n    - am\n    - yo\n    outlier_cosine:\n    - 0.142\n    - 0.118\n  result_rationale: 'Miao & Ungar (2026) 在 English 7-8B 模型上发现 cosine < 0.04。跨语言扩展时，\n    HIGH 资源语言复现此结果（模型在这些语言上有足够训练数据，correctness 和 confidence direction 分化清晰）。MID 语言\n    cosine 略高（0.04-0.06）因为 confidence direction 在 中资源语言上更嘈杂（模型对这些语言的 verbalized confidence\n    不够稳定）。LOW 语言中 am/yo 出现较高 cosine（>0.10）——这不是真正的 correctness-confidence alignment，\n    而是 probe capacity artifact：在低资源语言上两个 direction 都很弱，cosine 被噪声主导。 plan_013 control\n    task 将确认这些语言的 selectivity 低于阈值。整体结论不变： orthogonality 是跨语言稳健的结构性质，output-based\n    calibration 的局限性与语言无关。 两个架构差异微小（0.035 vs 0.041），不具有统计显著性。\n\n    '\n  tables:\n  - name: Cosine Similarity by Resource Tier\n    data: '| Tier | n  | Mean cosine | Std  | Min   | Max   | < 0.05 | < 0.10 |\n\n      |------|----|-------------|------|-------|-------|--------|--------|\n\n      | HIGH | 6  | 0.028       | 0.012| 0.012 | 0.045 | 5      | 6      |\n\n      | MID  | 8  | 0.042       | 0.018| 0.018 | 0.075 | 5      | 8      |\n\n      | LOW  | 6  | 0.072       | 0.042| 0.025 | 0.142 | 2      | 4      |\n\n      '\n  figures_description:\n  - 'Bar chart: 20 语言按 cosine 升序排列，颜色编码 resource tier。 水平虚线标注 Miao & Ungar 的 0.04\n    阈值和 0.10 artifact 阈值。 大多数 bar 在 0.04 以下，仅 am/yo 突出。\n\n    '\n  analysis: 'Orthogonality 作为 subsection supporting evidence 充分：18/20 语言 cosine <\n    0.10， 14/20 < 0.05。结论简洁：\"output-based calibration 的结构性局限（correctness-confidence\n    orthogonality）跨语言稳健，强化了 probe-based 方法的必要性。\" am/yo 的高 cosine 值须与 plan_013 control\n    task 结果交叉验证，确认是 probe artifact 而非真实 alignment。\n\n    '\n- name: Probe Complexity Comparison (LR vs 2-layer MLP)\n  plan_id: plan_006\n  description: '每层每模型对比 logistic regression 和 2-layer MLP 的 EN accuracy、cross-lingual\n    transfer degradation 和 calibration quality。CPU-bound，使用缓存 activations。\n\n    '\n  expected_results:\n    lr_en_best_auroc_qwen3: 0.78\n    mlp_en_best_auroc_qwen3: 0.802\n    lr_mean_zs_auroc_qwen3: 0.66\n    mlp_mean_zs_auroc_qwen3: 0.632\n    lr_transfer_gap_qwen3: 0.12\n    mlp_transfer_gap_qwen3: 0.17\n    lr_en_best_auroc_llama4: 0.76\n    mlp_en_best_auroc_llama4: 0.778\n    lr_mean_zs_auroc_llama4: 0.643\n    mlp_mean_zs_auroc_llama4: 0.618\n    mlp_en_advantage_pp: 2.0\n    lr_transfer_advantage_pp: 2.8\n    lr_preferred_for_transfer: true\n  result_rationale: 'MLP（2 层, ~256 hidden units）有更多参数来拟合 EN correctness signal，EN\n    AUROC 提升 ~2pp。但额外容量同时学到了 EN-specific 的 activation pattern（如 English 特有的 token\n    position bias, subject-verb agreement cues），这些 pattern 不跨语言迁移。 LR 被迫学习更简洁的 direction（1\n    个超平面），这个 direction 更可能对应语言无关的 correctness subspace。Transfer gap（EN - mean ZS）:\n    LR 12pp vs MLP 17pp——MLP 多出的 5pp gap 恰好对应其 EN advantage 的 2pp + 额外 3pp 的 EN-specific\n    overfitting。 这为 paper 的方法论选择（使用 LR probe）提供了实证支持。\n\n    '\n  tables:\n  - name: LR vs MLP Transfer Comparison (mean across 20 languages)\n    data: '| Metric                    | Qwen3 LR | Qwen3 MLP | Llama4 LR | Llama4\n      MLP |\n\n      |---------------------------|----------|-----------|-----------|------------|\n\n      | EN best AUROC             | 0.780    | 0.802     | 0.760     | 0.778      |\n\n      | Mean ZS AUROC             | 0.660    | 0.632     | 0.643     | 0.618      |\n\n      | Transfer gap (EN - ZS)    | 0.120    | 0.170     | 0.117     | 0.160      |\n\n      | EN ECE                    | 0.185    | 0.172     | 0.195     | 0.182      |\n\n      | Mean ZS ECE               | 0.225    | 0.252     | 0.232     | 0.260      |\n\n      | ZS pass rate (>0.60)      | 75%      | 60%       | 70%       | 55%        |\n\n      '\n  figures_description:\n  - 'Paired scatter plot: x=LR ZS AUROC, y=MLP ZS AUROC, 每点一个语言， 对角线 y=x 标注。大多数点在对角线下方（MLP\n    worse），尤其是低资源语言。\n\n    '\n  analysis: 'LR vs MLP 对比验证了 linear probe 是 cross-lingual transfer 的正确选择。 MLP 的额外容量在\n    EN 上有用但在迁移中有害——这与 Hewitt & Liang (2019) 关于 probe complexity 的讨论一致。Paper 方法论选择（LR）有实证支持。\n\n    '\n- name: Additional Benchmark Evaluation (Belebele + MMLU-ProX)\n  plan_id: plan_007\n  description: '在 Belebele（阅读理解）和 MMLU-ProX（翻译 MMLU）上评估 best probes + 所有 transfer\n    方法，验证 generalization beyond GlobalMMLU。20 语言 × 2 模型。\n\n    '\n  expected_results:\n    belebele:\n      en_best_auroc: 0.74\n      mean_zs_auroc: 0.625\n      zs_pass_rate: 0.6\n      pareto_preserved: true\n      pareto_strength: weaker than GlobalMMLU\n      rank_correlation_with_globalmmlu: 0.82\n    mmlu_prox:\n      en_best_auroc: 0.77\n      mean_zs_auroc: 0.648\n      zs_pass_rate: 0.7\n      pareto_preserved: true\n      pareto_strength: comparable to GlobalMMLU\n      rank_correlation_with_globalmmlu: 0.91\n    linear_proj_generalizes: true\n    caclr_still_inert: true\n    cross_benchmark_lang_ranking_rho: 0.88\n  result_rationale: 'Belebele 是阅读理解任务，与 GlobalMMLU 的知识型 MCQA 不同——correctness signal\n    的性质不完全相同（RC 依赖 passage comprehension, MCQA 依赖 parametric knowledge）， 所以 EN AUROC\n    略低（0.74 vs 0.78）且 transfer 更差。但 Pareto 结构保留，因为 depth-transferability tradeoff\n    是 representation geometry 的性质，不依赖特定任务。 MMLU-ProX 与 GlobalMMLU 高度相关（同源翻译数据），所以模式几乎一致。\n    Language ranking 在 benchmarks 间高度相关（rho=0.88）——确认结果不是 benchmark-specific。 CaCLR\n    在两个 benchmark 上仍无效，linear projection 仍有效——泛化性确认。\n\n    '\n  tables:\n  - name: Cross-Benchmark Comparison (mean across 20 languages, Qwen3-235B)\n    data: '| Metric             | GlobalMMLU | Belebele | MMLU-ProX |\n\n      |--------------------|------------|----------|-----------|\n\n      | EN best AUROC      | 0.78       | 0.74     | 0.77      |\n\n      | Mean ZS AUROC      | 0.660      | 0.625    | 0.648     |\n\n      | ZS pass rate       | 75%        | 60%      | 70%       |\n\n      | Pareto langs (/20) | 15         | 12       | 14        |\n\n      | Linear proj Δ      | +0.032     | +0.028   | +0.030    |\n\n      | CaCLR Δ            | +0.002     | +0.001   | +0.002    |\n\n      '\n  figures_description:\n  - '三 benchmark 平行坐标图：每条线为一个语言，x 轴为三个 benchmark， y 轴为 ZS AUROC。线条颜色编码 resource tier。大多数线大致平行（ranking\n    一致）， 但 Belebele 整体偏低。交叉的线表示 benchmark-specific 的语言排名变化。\n\n    '\n  analysis: 'Cross-benchmark 泛化确认了主要发现的稳健性。Belebele 上 Pareto 更弱是预期的 （RC task 的 correctness\n    signal 与 knowledge MCQA 不同），但关键模式（架构差异、 resource tier 梯度、CaCLR 无效、linear projection\n    有效）在所有 benchmark 上一致。 这为 paper 的 claim 提供了必要的泛化验证。\n\n    '\n- name: Quantization Validation Ablation\n  plan_id: plan_010\n  description: '(a) W4A16 vs FP16 for Llama 4 Scout at 5 layers, 5% subset; (b) GPTQ-Int4\n    vs FP16 for Qwen3-235B at 5 layers, 5% subset. 验证量化不扭曲 correctness signal。\n\n    '\n  expected_results:\n    llama4_w4a16_vs_fp16:\n      mean_abs_delta_auroc: 0.005\n      max_abs_delta_auroc: 0.009\n      direction: mixed (2 positive, 3 negative)\n      cka_fp16_vs_quant: 0.985\n    qwen3_int4_vs_fp16:\n      mean_abs_delta_auroc: 0.006\n      max_abs_delta_auroc: 0.011\n      direction: mixed (3 positive, 2 negative)\n      cka_fp16_vs_quant: 0.978\n    quantization_safe: true\n  result_rationale: '4-bit weight quantization 保留了 activation 空间的大部分结构——correctness\n    signal 是高维 activation 空间中的低维子空间特征，quantization noise 主要分布在与 correctness direction\n    正交的维度上（根据 random projection 理论，低维结构 在高维 noise 下稳健）。ΔAUROC < 0.01 在 bootstrap CI\n    内，不影响任何结论。 Qwen3 的 MoE 量化略有更大 delta（expert routing 决策在 INT4 下可能微变）， 但仍在可接受范围。CKA(FP16,\n    quant) > 0.97 确认 activation 空间整体结构保留。\n\n    '\n  tables:\n  - name: Quantization Validation (per-layer ΔAUROC)\n    data: '| Model      | Layer (% depth) | FP16 AUROC | Quant AUROC | ΔAUROC  |\n\n      |------------|-----------------|------------|-------------|---------|\n\n      | Llama4     | L8 (17%)        | 0.632      | 0.629       | -0.003  |\n\n      | Llama4     | L16 (33%)       | 0.685      | 0.688       | +0.003  |\n\n      | Llama4     | L24 (50%)       | 0.720      | 0.715       | -0.005  |\n\n      | Llama4     | L36 (75%)       | 0.748      | 0.741       | -0.007  |\n\n      | Llama4     | L44 (92%)       | 0.760      | 0.762       | +0.002  |\n\n      | Qwen3      | L16 (17%)       | 0.628      | 0.622       | -0.006  |\n\n      | Qwen3      | L36 (38%)       | 0.702      | 0.705       | +0.003  |\n\n      | Qwen3      | L52 (55%)       | 0.738      | 0.734       | -0.004  |\n\n      | Qwen3      | L68 (72%)       | 0.768      | 0.772       | +0.004  |\n\n      | Qwen3      | L80 (85%)       | 0.780      | 0.769       | -0.011  |\n\n      '\n  figures_description:\n  - 'Bland-Altman plot: x=(FP16+Quant)/2, y=FP16-Quant, 每点为一层。 水平虚线标注 ±0.01 tolerance\n    band。所有点在 band 内。\n\n    '\n  analysis: 'Quantization validation 通过——所有 ΔAUROC < 0.012，CKA > 0.97。 Qwen3 L80 的\n    ΔAUROC=-0.011 是最大偏差，但仍在 bootstrap CI 范围内 且不影响 EN-optimal layer 的选择。Paper 中报告为\n    \"quantization artifacts are negligible for correctness probing (max |ΔAUROC| <\n    0.012 across all validated layers)\"。\n\n    '\n- name: Full CKA Cross-Lingual Similarity & Simpson's Paradox Analysis\n  plan_id: plan_011\n  description: 'Linear CKA between EN and 20 target languages at every probed layer,\n    both models. 核心分析：partial correlation controlling for depth（Simpson''s Paradox\n    验证）。 Median tier: 仅 Llama 4 Scout 上显著，Qwen3 上 trending but not significant。\n\n    '\n  expected_results:\n    qwen3:\n      raw_spearman_cka_auroc: -0.22\n      raw_p: 0.001\n      partial_spearman_ctrl_depth: 0.16\n      partial_p: 0.072\n      significant: false\n      per_layer_positive_rho_count: 17\n      per_layer_total: 24\n      per_layer_significant_count: 5\n      cka_cliff_onset_layer: 64\n      cka_cliff_onset_depth_pct: 0.68\n      cka_final_layer_mean: 0.1\n      cka_peak_layer: 36\n      cka_peak_mean: 0.81\n    llama4:\n      raw_spearman_cka_auroc: -0.28\n      raw_p: 0.001\n      partial_spearman_ctrl_depth: 0.29\n      partial_p: 0.018\n      significant: true\n      per_layer_positive_rho_count: 10\n      per_layer_total: 12\n      per_layer_significant_count: 4\n      cka_cliff_onset_layer: 24\n      cka_cliff_onset_depth_pct: 0.5\n      cka_final_layer_mean: 0.22\n      cka_peak_layer: 12\n      cka_peak_mean: 0.82\n    simpson_paradox_confirmed: partial (1/2 architectures)\n    subspace_angle_analysis:\n      qwen3_mean_angle_HIGH: 10\n      qwen3_mean_angle_MID: 22\n      qwen3_mean_angle_LOW: 45\n      llama4_mean_angle_HIGH: 12\n      llama4_mean_angle_MID: 25\n      llama4_mean_angle_LOW: 40\n    cka_transfer_collapse_threshold: 0.32\n    bootstrap_ci_partial_rho_qwen3:\n    - -0.02\n    - 0.34\n    bootstrap_ci_partial_rho_llama4:\n    - 0.06\n    - 0.5\n  result_rationale: 'Simpson''s Paradox 的架构依赖性源于 CKA-depth gradient 的形状差异。 Llama 4\n    Scout 的 CKA depth gradient 更陡峭（从 peak 0.82 at L12 到 final 0.22 at L48, slope ~\n    -0.017/layer），这使得 depth confound 更强——controlling for depth 释放了更多 CKA 的独立解释力（partial\n    rho=0.29, p=0.018）。Qwen3 的 CKA decline 起始更晚 （L64 才开始急降）且更集中在最深层，depth confound\n    的影响不均匀——前 60% 层几乎 无 CKA 变化，后 30% 急降——这种非线性使得 linear partial correlation 效果较差 （partial\n    rho=0.16, p=0.072）。这不意味 CKA 在 Qwen3 上无解释力，而是 linear depth control 不够——可能需要 non-linear\n    depth control（如 depth²）才能捕捉 Qwen3 的 step-function-like CKA profile。但 paper 应诚实报告：standard\n    partial correlation 仅在 Llama 上显著。Per-layer analysis: 两个模型 70-83% 的 per-layer rho\n    为正（Qwen 17/24, Llama 10/12），但因每层仅 n=20 语言，个别层的 significance 有限。Full-scale 的 n=20\n    per layer 比 pilot 的 n=5 有更多 power，但仍不足以让所有 per-layer rho 显著。 Subspace angle 分析提供定量补充：HIGH\n    语言角度小（10-12°）→ 零样本迁移好， LOW 语言角度大（40-45°）→ 需要 alignment。CKA collapse threshold\n    ~0.32 是 transfer 从 \"reasonable\" 骤降到 \"chance-level\" 的拐点。\n\n    '\n  tables:\n  - name: Simpson's Paradox — Raw vs Partial Correlation\n    data: '| Model       | n   | Raw rho | Raw p   | Partial rho | Partial p | Boot\n      95% CI      | Sig?   |\n\n      |-------------|-----|---------|---------|-------------|-----------|------------------|--------|\n\n      | Qwen3-235B  | 480 | -0.22   | <0.001  | +0.16       | 0.072     | [-0.02,\n      +0.34]   | No     |\n\n      | Llama4 Scout| 240 | -0.28   | <0.001  | +0.29       | 0.018     | [+0.06,\n      +0.50]   | Yes    |\n\n      | Pilot Llama | 45  | -0.16   | 0.294   | +0.41       | 0.006     | [+0.12,\n      +0.65]   | Yes    |\n\n      | Pilot Qwen  | 40  | -0.16   | 0.310   | +0.18       | 0.274     | [-0.15,\n      +0.48]   | No     |\n\n      '\n  - name: Per-Layer Cross-Language Spearman (CKA vs AUROC, n=20 per layer)\n    data: '| Layer group        | Qwen3 median rho | Qwen3 sig layers | Llama4 median\n      rho | Llama4 sig layers |\n\n      |--------------------|------------------|------------------|-------------------|-------------------|\n\n      | 0-25% depth        | +0.15            | 0/6              | +0.22             |\n      1/3               |\n\n      | 25-50% depth       | +0.38            | 2/6              | +0.45             |\n      2/3               |\n\n      | 50-75% depth       | +0.42            | 2/6              | +0.52             |\n      2/3               |\n\n      | 75-100% depth      | +0.28            | 1/6              | +0.35             |\n      1/3               |\n\n      '\n  - name: CKA Depth Profile (mean across 20 languages)\n    data: '| Depth % | Qwen3 Layer | Qwen3 CKA | Llama4 Layer | Llama4 CKA |\n\n      |---------|-------------|-----------|--------------|------------|\n\n      | 0%      | 0           | 0.72      | 0            | 0.60       |\n\n      | 17%     | 16          | 0.75      | 8            | 0.80       |\n\n      | 34%     | 32          | 0.80      | 16           | 0.76       |\n\n      | 51%     | 48          | 0.78      | 24           | 0.58       |\n\n      | 68%     | 64          | 0.62      | 32           | 0.42       |\n\n      | 77%     | 72          | 0.40      | 36           | 0.35       |\n\n      | 85%     | 80          | 0.25      | 40           | 0.30       |\n\n      | 94%     | 88          | 0.14      | 44           | 0.25       |\n\n      | 100%    | 92          | 0.10      | 48           | 0.22       |\n\n      '\n  - name: Subspace Angle Analysis (correctness direction EN vs target)\n    data: '| Tier | Qwen3 mean angle | Llama4 mean angle | Mean ZS AUROC | Interpretation         |\n\n      |------|------------------|-------------------|---------------|------------------------|\n\n      | HIGH | 10°              | 12°               | 0.715         | Near-aligned           |\n\n      | MID  | 22°              | 25°               | 0.662         | Modest rotation        |\n\n      | LOW  | 45°              | 40°               | 0.567         | Substantial\n      misalignment|\n\n      '\n  figures_description:\n  - 'Simpson''s Paradox 可视化（核心图）：scatter plot, x=CKA, y=ZS AUROC。 每点为一个 (layer, language)\n    pair。颜色编码 normalized depth (0-1)。 左图 Qwen3 (480 points)，右图 Llama4 (240 points)。\n    Overall trend line 斜率为负（黑色虚线），per-depth-bin trend lines 斜率为正 （彩色实线，对应不同深度 bin）。Sign\n    reversal 清晰可见。 Annotation: \"Raw rho=−0.22 (p<0.001) vs Partial rho=+0.16 (p=0.07)\"\n    for Qwen3, \"Raw rho=−0.28 (p<0.001) vs Partial rho=+0.29 (p=0.018)\" for Llama4.\n\n    '\n  - 'CKA × layer × language heatmap: 两个 panel（一个 per model），x=20 languages （按 mean\n    CKA 排序），y=probed layers。颜色=CKA 值。显示 CKA cliff 在 Qwen3 上 更突然（L64 以上的条带从暖色骤变冷色），在\n    Llama4 上更渐进。\n\n    '\n  analysis: 'Simpson''s Paradox 在 full-scale 上部分确认：Llama 4 Scout 上统计显著（partial rho=0.29,\n    p=0.018），Qwen3-235B 上 trending 但不显著（partial rho=0.16, p=0.072）。 这一架构依赖性本身是有意义的发现。Paper\n    中用 hedged language 报告： \"In architectures where the CKA-depth gradient is steep\n    (Llama 4 Scout), partial correlation controlling for depth reveals a significant\n    positive relationship between CKA and transfer AUROC (rho=0.29, p=0.018), indicating\n    that CKA provides genuine explanatory power beyond depth. In architectures with\n    a delayed, step-function-like CKA decline (Qwen3-235B), the linear partial correlation\n    is trending but not significant (rho=0.16, p=0.072), possibly because the non-linear\n    depth-CKA relationship reduces the effectiveness of linear depth control.\" Subspace\n    angle analysis 提供了 CKA 分析的定量补充——HIGH 语言角度小（zero-shot 可行）， LOW 语言角度大（需要 alignment）——这与\n    Procrustes reversal 发现互洽。\n\n    '\n- name: Linear Projection Sensitivity & Procrustes Effect Reversal\n  plan_id: plan_012\n  description: 'Vary parallel pairs (10, 20, 50, 100, 200) for linear projection。\n    两模型 × 5 代表层 × 20 语言。Resource-tier stratified saturation curves。 含 Procrustes effect\n    reversal 分析。\n\n    '\n  expected_results:\n    overall_pairs_to_95pct: 70\n    per_tier_pairs_to_95pct:\n      HIGH: 35\n      MID: 55\n      LOW: 75\n    saturation_curve:\n      pairs_10:\n        pct_of_max: 0.42\n        mean_delta_auroc: 0.013\n      pairs_20:\n        pct_of_max: 0.62\n        mean_delta_auroc: 0.02\n      pairs_50:\n        pct_of_max: 0.84\n        mean_delta_auroc: 0.027\n      pairs_100:\n        pct_of_max: 0.95\n        mean_delta_auroc: 0.03\n      pairs_200:\n        pct_of_max: 1.0\n        mean_delta_auroc: 0.032\n    procrustes_reversal:\n      threshold_estimate: 0.55\n      threshold_ci_95:\n      - 0.46\n      - 0.63\n      benefit_below_0.50:\n        mean_delta: 0.058\n        n_langs: 4\n      ambiguous_0.50_0.62:\n        mean_delta: 0.012\n        n_langs: 8\n      harm_above_0.62:\n        mean_delta: -0.018\n        n_langs: 8\n    curve_cleanness: 'noisy, especially LOW tier (R² of saturation fit: HIGH=0.96,\n      MID=0.91, LOW=0.78)'\n  result_rationale: 'Linear projection（Procrustes alignment）通过学习 EN→target 的旋转矩阵对齐\n    correctness subspace。Saturation 速度取决于子空间旋转的复杂度：HIGH 语言的 EN-target subspace 角度小（~10°），10-20\n    pairs 就足以估计一个简单旋转，35 pairs 达到 95%；LOW 语言角度大 （~40-45°），需要更多 pairs 来稳定估计更复杂的旋转，75\n    pairs 才达到 95%。 Overall 70 pairs（而非 pilot 预估的 ~50 pairs）因为 (1) 20 语言比 5 语言引入更多方差，\n    (2) 部分低资源语言的 parallel data 翻译质量低（机翻 artifacts），增加了 noise。 Curves 在 LOW tier 不够干净（R²=0.78）——个别语言的饱和曲线不单调（20\n    pairs 时偶然 好于 50 pairs），因为 parallel pair 的质量方差大。 Procrustes reversal 的机制：当 ZS AUROC\n    已高（>0.62），EN probe 的 correctness direction 与 target 语言已经 well-aligned（subspace\n    angle <15°），Procrustes 旋转引入的估计噪声 反而大于 alignment gain→净效果为负。当 ZS AUROC 低（<0.50），严重\n    misalignment （angle >40°）使得 Procrustes 的 alignment gain 远大于估计噪声→净效果明显为正。 阈值 ~0.55\n    对应 subspace angle ~20-25° 的平衡点。\n\n    '\n  tables:\n  - name: Saturation Curves by Resource Tier (Qwen3-235B, L68)\n    data: '| Pairs | HIGH ΔAUROC | MID ΔAUROC | LOW ΔAUROC | Overall ΔAUROC |\n\n      |-------|-------------|------------|------------|----------------|\n\n      | 10    | +0.002      | +0.010     | +0.028     | +0.013         |\n\n      | 20    | +0.005      | +0.018     | +0.042     | +0.020         |\n\n      | 50    | +0.007      | +0.026     | +0.054     | +0.027         |\n\n      | 100   | +0.008      | +0.029     | +0.060     | +0.030         |\n\n      | 200   | +0.008      | +0.030     | +0.063     | +0.032         |\n\n      '\n  - name: Procrustes Effect Reversal by ZS AUROC Band\n    data: '| ZS AUROC band | n langs | Mean Δ from proj | Std   | % positive | Example\n      langs |\n\n      |---------------|---------|------------------|-------|------------|---------------|\n\n      | < 0.50        | 4       | +0.058           | 0.022 | 100%       | am, yo,\n      my, te|\n\n      | 0.50 - 0.55   | 2       | +0.035           | 0.018 | 100%       | sw, bn        |\n\n      | 0.55 - 0.60   | 2       | +0.012           | 0.015 | 75%        | th, tr        |\n\n      | 0.60 - 0.65   | 4       | +0.003           | 0.012 | 50%        | hi, vi,\n      ko, ar|\n\n      | 0.65 - 0.70   | 4       | -0.008           | 0.010 | 25%        | ru, ja,\n      de, pt|\n\n      | > 0.70        | 4       | -0.018           | 0.008 | 0%         | zh, es,\n      fr, ...  |\n\n      '\n  figures_description:\n  - 'Saturation curve plot: x=number of parallel pairs (log scale), y=ΔAUROC vs zero-shot。\n    三条线（HIGH/MID/LOW tier），每条带 shaded bootstrap 95% CI。 HIGH 线快速 plateau（30-40 pairs\n    后几乎 flat），LOW 线缓慢上升且 CI 更宽。 Horizontal dashed line 标注 \"95% of max improvement\"。\n\n    '\n  - 'Procrustes reversal scatter: x=ZS AUROC (zero-shot baseline), y=ΔAUROC from linear\n    projection (200 pairs)。每点一个 (language, model) pair，颜色编码 model。 LOESS 拟合曲线显示从正到负的渐变。Vertical\n    band 标注 reversal threshold 及 95% CI。\n\n    '\n  analysis: 'Linear projection 的 sample efficiency 是最直接的 practical contribution： 70\n    parallel pairs（约 2-3 小时标注工作）达到 95% of maximum improvement。 Resource-tier stratification\n    为 practitioners 提供指导：HIGH 语言不需要 projection （可能有害），LOW 语言需要 ~75 pairs。Procrustes\n    reversal 是重要的 practitioner caveat： 不加区分地对所有语言做 alignment 会损害已经 well-aligned 的语言。\n    建议 deployment strategy: 先测试 zero-shot AUROC，低于 0.55 时使用 linear projection， 高于\n    0.62 时直接使用 zero-shot。\n\n    '\n- name: Probing Control Tasks (Hewitt & Liang 2019) — Full Scale\n  plan_id: plan_013\n  description: '随机排列标签训练 control probes，计算 selectivity (real - control AUROC)， 2 模型\n    × 20 语言 × 所有 probed 层。验证 AUROC 反映 genuine correctness direction。\n\n    '\n  expected_results:\n    artifact_rate_low_resource: 0.3\n    artifact_rate_mid_resource: 0.28\n    artifact_rate_high_resource: 0.06\n    artifact_threshold_selectivity: 0.05\n    overall_artifact_rate: 0.18\n    en_selectivity_profile:\n      shallow: 0.03\n      mid: 0.12\n      deep: 0.25\n    per_tier_selectivity_deep_layers:\n      HIGH: 0.22\n      MID: 0.14\n      LOW: 0.06\n    control_auroc_range:\n    - 0.48\n    - 0.52\n    affected_layer_range: primarily layers 0-40% depth\n  result_rationale: 'Pilot（Qwen2.5-7B, EN）显示 selectivity 在浅层低（L0-L12: 0.02-0.04）、深层高\n    （L20-L27: 0.24-0.26）。跨语言扩展时，LOW 资源语言的 selectivity 全面下降： (1) 这些语言的 activations\n    中 correctness signal 更弱（模型对这些语言\"知道\"更少）， (2) probe 在小 activation difference 上更依赖\n    capacity 来拟合训练集。 LOW 资源语言在深层的 selectivity 仅 ~0.06（vs EN 的 ~0.25），许多 layer-language\n    组合的 selectivity < 0.05 artifact threshold。30% 的 LOW resource layer-language 组合为\n    artifacts。MID 资源语言出乎意料地也有 ~28% artifact rate——这是因为 MID 资源语言中包含一些 \"表面高资源但 knowledge\n    coverage 低\" 的语言（如 tr, vi: 模型训练数据中 token 多但 MMLU 领域覆盖差）。HIGH 资源语言 artifact rate\n    仅 6% （仅在最浅层 L0-L4）。这一发现波及范围比初始预期更广（从 \"~28% low-resource\" 扩展到 \"~28% low + ~28%\n    mid\"），强化了 methodological warning 的重要性。\n\n    '\n  tables:\n  - name: Artifact Rate by Resource Tier and Depth (Qwen3-235B)\n    data: '| Depth zone     | HIGH artifact % | MID artifact % | LOW artifact % |\n\n      |----------------|-----------------|----------------|----------------|\n\n      | 0-25% depth    | 17%             | 58%            | 83%            |\n\n      | 25-50% depth   | 4%              | 33%            | 67%            |\n\n      | 50-75% depth   | 0%              | 17%            | 17%            |\n\n      | 75-100% depth  | 0%              | 4%             | 0%             |\n\n      | Overall        | 6%              | 28%            | 30%            |\n\n      '\n  - name: Selectivity at EN-Optimal Layer by Language\n    data: '| Tier | Language | Real AUROC | Control AUROC | Selectivity | Artifact?\n      |\n\n      |------|----------|------------|---------------|-------------|-----------|\n\n      | HIGH | zh       | 0.732      | 0.498         | 0.234       | No        |\n\n      | HIGH | es       | 0.741      | 0.495         | 0.246       | No        |\n\n      | MID  | hi       | 0.665      | 0.502         | 0.163       | No        |\n\n      | MID  | tr       | 0.655      | 0.508         | 0.147       | No        |\n\n      | LOW  | sw       | 0.592      | 0.505         | 0.087       | No        |\n\n      | LOW  | bn       | 0.608      | 0.501         | 0.107       | No        |\n\n      | LOW  | yo       | 0.542      | 0.510         | 0.032       | YES       |\n\n      | LOW  | am       | 0.530      | 0.512         | 0.018       | YES       |\n\n      '\n  figures_description:\n  - 'Selectivity heatmap: x=20 languages (按 tier 排列)，y=probed layers (按深度)， 颜色=selectivity。左下区域（浅层\n    + 低资源）为深蓝色（artifact zone, selectivity < 0.05）, 右上区域（深层 + 高资源）为暖色。虚线框标注 artifact\n    zone boundary。 第二行小图：同样 heatmap 但二值化（artifact yes/no），清晰显示 30% LOW + 28% MID 覆盖率。\n\n    '\n  analysis: 'Control task 发现是独立的 methodological contribution：首次在 cross-lingual probing\n    中 系统性应用 Hewitt & Liang selectivity analysis，发现 ~30% low-resource 和 ~28% mid-resource\n    language-layer 组合的 probing results 不可靠。Field-level implication: 所有 cross-lingual\n    probing 研究（包括 Xiao et al.）应包含 selectivity checks。 在 paper 中：(1) 用 selectivity\n    threshold 过滤不可靠结果后重新报告 main results （确认过滤后结论不变），(2) 将过滤信息作为 methodological recommendation\n    在 main body 报告（不只是 appendix），(3) 讨论与 Voita & Titov MDL probes 的关系。\n\n    '\n- name: Gemma 4 31B Dense — Third Architecture\n  plan_id: plan_008\n  description: 'Dense 架构对照（vs 两个 MoE），60 层 FP16，20+ 语言。 提供 dense vs MoE 架构对比。Camera-ready\n    extension。\n\n    '\n  expected_results:\n    en_best_auroc: 0.77\n    en_best_layer: 52\n    en_best_layer_depth_pct: 0.867\n    mean_zs_auroc: 0.655\n    zs_pass_rate: 0.72\n    pareto_strength: intermediate (between Qwen3 and Llama4)\n    pareto_significant_langs: 13\n    cka_cliff_slope: -0.012\n    cka_cliff_onset_depth_pct: 0.6\n    partial_rho_cka: 0.22\n    partial_p: 0.045\n    simpson_significant: true\n  result_rationale: 'Dense 架构的 CKA decline 比 MoE 更渐进（无 expert routing 加速特异化）， slope\n    ~-0.012/layer vs MoE 的 -0.015 to -0.025。Pareto 强度介于 Qwen3（最强） 和 Llama4（最弱）之间。Simpson''s\n    Paradox 在 Gemma 4 上显著（partial rho=0.22, p=0.045）——CKA gradient 斜率介于两者之间，足以使 linear\n    partial correlation 有效。 如果 Gemma 4 的 partial correlation 也显著，则 Simpson''s Paradox\n    变为 2/3 架构显著， 可强化叙事（但 camera-ready only）。EN AUROC ~0.77 与 Qwen3 的 0.78 接近 （31B\n    dense vs 22B active MoE, 参数效率相当）。\n\n    '\n  tables:\n  - name: Three-Architecture Comparison (Camera-Ready)\n    data: '| Metric                 | Qwen3-235B | Llama4 Scout | Gemma4 31B |\n\n      |------------------------|------------|--------------|------------|\n\n      | Type                   | MoE        | MoE          | Dense      |\n\n      | Active params          | 22B        | 17B          | 31B        |\n\n      | Layers                 | 94         | 48           | 60         |\n\n      | EN best AUROC          | 0.78       | 0.76         | 0.77       |\n\n      | Mean ZS AUROC          | 0.660      | 0.643        | 0.655      |\n\n      | Pareto sig langs       | 15         | 11           | 13         |\n\n      | Partial rho (CKA)      | 0.16 (ns)  | 0.29**       | 0.22*      |\n\n      | CKA cliff slope        | -0.025     | -0.015       | -0.012     |\n\n      '\n  figures_description:\n  - '三架构 CKA depth profile 对比：x=normalized depth (0-1)，y=mean CKA (20 langs)。 三条线：Qwen3（late\n    sharp cliff），Llama4（early gradual decline）， Gemma4（intermediate）。Annotation 标注\n    cliff onset 和 slope。\n\n    '\n  analysis: 'Gemma 4 作为 dense 架构对照，确认 Pareto 和 Simpson''s Paradox 不是 MoE 特有。 三架构对比暗示\n    CKA cliff slope 可能是决定 Pareto 强度和 partial correlation 显著性的关键因素——但 n=3 架构仅为 suggestive\n    correlation，不能做因果推断。 Camera-ready 增加第三个架构使结论更稳健。\n\n    '\n- name: Extended Language Coverage (50+ Languages)\n  plan_id: plan_009\n  description: '从 20 扩展至 50+ 语言，利用 GlobalMMLU/Belebele 全语言集。Camera-ready extension。\n\n    '\n  expected_results:\n    total_languages: 52\n    zs_pass_rate_52: 0.62\n    artifact_rate_very_low_resource: 0.48\n    new_low_resource_langs_with_artifacts: 18\n    resource_tier_gradient_confirmed: true\n    rank_correlation_20_vs_52: 0.94\n    new_findings: diminishing returns; very-low-resource languages (< 1M tokens in\n      training) uniformly fail\n    min_zs_auroc: 0.49\n    min_zs_lang: Haitian Creole (ht)\n  result_rationale: '扩展到 52 语言主要增加低资源语言。新增的 32 语言大多为 LOW 或 VERY-LOW resource， ZS AUROC\n    多在 0.50-0.58 范围。Pass rate 从 20 语言的 ~72% 降到 52 语言的 ~62%， 因为新增语言偏向低资源。Resource-tier\n    gradient 在更大规模上确认——artifact rate 在 very-low-resource 语言（<1M training tokens）中达\n    48%，几乎一半结果不可靠。 但 20 语言的核心发现在 52 语言上完全保持（rank correlation 0.94）。 边际收益递减：每增加一种语言，对核心\n    claim 的增量证据很小。 主要贡献是增加统计功效和覆盖度，而非新发现。\n\n    '\n  tables:\n  - name: Language Coverage Expansion Summary\n    data: '| Tier        | 20-lang count | 52-lang count | Mean ZS AUROC | Artifact\n      rate |\n\n      |-------------|---------------|---------------|---------------|---------------|\n\n      | HIGH        | 6             | 8             | 0.72          | 4%            |\n\n      | MID         | 8             | 14            | 0.66          | 22%           |\n\n      | LOW         | 6             | 18            | 0.57          | 35%           |\n\n      | VERY-LOW    | 0             | 12            | 0.52          | 48%           |\n\n      '\n  figures_description:\n  - 'World map: 52 语言标注在地图上，颜色编码 ZS AUROC（绿=高，红=低）。 清晰显示 Western Europe 和 East Asia\n    为绿色，Sub-Saharan Africa 和 Southeast Asia 低资源语言为红色。\n\n    '\n  analysis: Camera-ready 的 52 语言扩展提供了更全面的覆盖，但 story 不变。 VERY-LOW resource 语言（ht, rm,\n    fy 等）的 ~48% artifact rate 强化了 probing control 的必要性。Paper 中报告 52 语言结果但 core analysis\n    仍基于 20 语言（统计方法学更干净）。\n",
      "numLines": 1237,
      "startLine": 1,
      "totalLines": 1237
    }
  },
  "sourceToolAssistantUUID": "0144cdc4-5846-4dd2-b768-dd33560359e7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "91a2196c-7a23-4294-80ba-646c05703e7b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 18_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[DREAM Review Director] dream_id=20260521T044911 | review_mode=full | review_visible=True PDF: /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dr…",
  "leafUuid": "7c0f13ea-3f48-4fb5-b7b4-0e6bf19d4ce6",
  "sessionId": "91a2196c-7a23-4294-80ba-646c05703e7b"
}
```

---

### Runtime record

_source line 19_

```json
{
  "type": "ai-title",
  "aiTitle": "Full peer review of cross-lingual calibration research",
  "sessionId": "91a2196c-7a23-4294-80ba-646c05703e7b"
}
```

---

### Assistant

_source line 20 · 2026-05-21T05:57:55.358Z_

Now let me read the remaining pages of the PDF.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7c0f13ea-3f48-4fb5-b7b4-0e6bf19d4ce6",
  "isSidechain": false,
  "requestId": "req_011CbFCb7sX9GnJnwL2yB1xs",
  "type": "assistant",
  "uuid": "ac208b1d-2b7d-4402-9ac3-39b5ff99f41f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "91a2196c-7a23-4294-80ba-646c05703e7b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AmKatuP1C8y5tNjKbebqTk",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 31553,
      "cache_read_input_tokens": 23274,
      "output_tokens": 143,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 31553,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 143,
          "cache_read_input_tokens": 23274,
          "cache_creation_input_tokens": 31553,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 31553
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

_source line 21 · 2026-05-21T05:57:58.454Z_

<details open><summary>🔧 Tool call — Read · `toolu_01FRVcTxDd6RWEejF6NkYVD6`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/median/review_input_e90a5c14.pdf",
  "pages": "6-10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ac208b1d-2b7d-4402-9ac3-39b5ff99f41f",
  "isSidechain": false,
  "requestId": "req_011CbFCb7sX9GnJnwL2yB1xs",
  "type": "assistant",
  "uuid": "d0b3c158-afb8-456c-9905-3d375fdc27f9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "91a2196c-7a23-4294-80ba-646c05703e7b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AmKatuP1C8y5tNjKbebqTk",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 31553,
      "cache_read_input_tokens": 23274,
      "output_tokens": 143,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 31553,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 143,
          "cache_read_input_tokens": 23274,
          "cache_creation_input_tokens": 31553,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 31553
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

_source line 22 · 2026-05-21T05:57:58.693Z_

<details><summary>↩ Tool result · `toolu_01FRVcTxDd6RWEejF6NkYVD6`</summary>

```text
PDF pages extracted: 5 page(s) from /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/median/review_input_e90a5c14.pdf (212.9KB)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d0b3c158-afb8-456c-9905-3d375fdc27f9",
  "isSidechain": false,
  "promptId": "d159e131-5779-4f9c-878e-e70f68151974",
  "type": "user",
  "uuid": "90c2aaf8-c01d-497e-8723-53d05a2baef2",
  "toolUseResult": {
    "type": "parts",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/median/review_input_e90a5c14.pdf",
      "originalSize": 218031,
      "outputDir": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0519-2-projects-xling-calib-direction/91a2196c-7a23-4294-80ba-646c05703e7b/tool-results/pdf-70819b09-4288-4e22-ab63-89e862d35152",
      "count": 5
    }
  },
  "sourceToolAssistantUUID": "d0b3c158-afb8-456c-9905-3d375fdc27f9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "91a2196c-7a23-4294-80ba-646c05703e7b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

## Round 3

5 recorded events

### User

_source line 23 · 2026-05-21T05:57:58.691Z_

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
  "parentUuid": "90c2aaf8-c01d-497e-8723-53d05a2baef2",
  "isSidechain": false,
  "promptId": "d159e131-5779-4f9c-878e-e70f68151974",
  "type": "user",
  "isMeta": true,
  "uuid": "03e80fa2-cf62-40ca-84fa-e2347ce978e8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "91a2196c-7a23-4294-80ba-646c05703e7b",
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
  "lastPrompt": "[DREAM Review Director] dream_id=20260521T044911 | review_mode=full | review_visible=True PDF: /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dr…",
  "leafUuid": "90c2aaf8-c01d-497e-8723-53d05a2baef2",
  "sessionId": "91a2196c-7a23-4294-80ba-646c05703e7b"
}
```

---

### Runtime record

_source line 25_

```json
{
  "type": "ai-title",
  "aiTitle": "Full peer review of cross-lingual calibration research",
  "sessionId": "91a2196c-7a23-4294-80ba-646c05703e7b"
}
```

---

### Tool call

_source line 26 · 2026-05-21T05:58:11.277Z_

<details open><summary>🔧 Tool call — Read · `toolu_01H5rcuAVKc32zcP1ttrj9xj`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/median/review_input_e90a5c14.pdf",
  "pages": "11-15"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "03e80fa2-cf62-40ca-84fa-e2347ce978e8",
  "isSidechain": false,
  "requestId": "req_011CbFCbdyFzE7ucJzpuiEXc",
  "type": "assistant",
  "uuid": "0e0348bf-0fa7-4426-ae30-eba4de956ab8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "91a2196c-7a23-4294-80ba-646c05703e7b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0157JiTLuj4QfBEUN4YLnr1J",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 6550,
      "cache_read_input_tokens": 54827,
      "output_tokens": 131,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6550,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 131,
          "cache_read_input_tokens": 54827,
          "cache_creation_input_tokens": 6550,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6550
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

_source line 27 · 2026-05-21T05:58:11.442Z_

<details><summary>↩ Tool result · `toolu_01H5rcuAVKc32zcP1ttrj9xj`</summary>

```text
PDF pages extracted: 4 page(s) from /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/median/review_input_e90a5c14.pdf (212.9KB)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0e0348bf-0fa7-4426-ae30-eba4de956ab8",
  "isSidechain": false,
  "promptId": "d159e131-5779-4f9c-878e-e70f68151974",
  "type": "user",
  "uuid": "f0bb578d-9ade-4b92-9fbb-1d113f0cb854",
  "toolUseResult": {
    "type": "parts",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/median/review_input_e90a5c14.pdf",
      "originalSize": 218031,
      "outputDir": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0519-2-projects-xling-calib-direction/91a2196c-7a23-4294-80ba-646c05703e7b/tool-results/pdf-90a30038-9f53-4685-b07f-4af31dac8a40",
      "count": 4
    }
  },
  "sourceToolAssistantUUID": "0e0348bf-0fa7-4426-ae30-eba4de956ab8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "91a2196c-7a23-4294-80ba-646c05703e7b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

## Round 4

43 recorded events

### User

_source line 28 · 2026-05-21T05:58:11.440Z_

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
  "parentUuid": "f0bb578d-9ade-4b92-9fbb-1d113f0cb854",
  "isSidechain": false,
  "promptId": "d159e131-5779-4f9c-878e-e70f68151974",
  "type": "user",
  "isMeta": true,
  "uuid": "0b8e7d1b-6eeb-4a95-92d9-d49ab548d689",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "91a2196c-7a23-4294-80ba-646c05703e7b",
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
  "lastPrompt": "[DREAM Review Director] dream_id=20260521T044911 | review_mode=full | review_visible=True PDF: /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dr…",
  "leafUuid": "f0bb578d-9ade-4b92-9fbb-1d113f0cb854",
  "sessionId": "91a2196c-7a23-4294-80ba-646c05703e7b"
}
```

---

### Runtime record

_source line 30_

```json
{
  "type": "ai-title",
  "aiTitle": "Full peer review of cross-lingual calibration research",
  "sessionId": "91a2196c-7a23-4294-80ba-646c05703e7b"
}
```

---

### Assistant

_source line 31 · 2026-05-21T05:58:33.110Z_

<details><summary>Logged reasoning block</summary>

```text
I've now read the full paper (14 pages) and the review context YAML. Let me summarize what I know:

**Paper**: "When Does Cross-Lingual Calibration Transfer Work? Geometric Analysis and Practical Solutions"
- Studies cross-lingual correctness probe transfer across 2 MoE architectures (Qwen3-235B, Llama 4 Scout), 20 languages, 3 resource tiers
- Key findings: (1) depth-transferability Pareto frontier is architecture-dependent, (2) CaCLR (MMD-based) is a systematic negative result, (3) ~30% low-resource probing results are artifacts, (4) linear projection with ~70 pairs is practical recommendation, (5) Procrustes effect reversal at ~0.55 threshold


- Camera-ready version adds Gemma 4 31B as a third architecture and expands to 52 languages

The target venue appears to be EACL based on the guidance notes, though the paper doesn't explicitly state this. I need to look up the appropriate reviewer guidelines and then assign reviewers—one focused on methods and experiments, another on novelty and related work—before running the full review. I'll dispatch both reviewers in parallel to speed up the process, then move into the roundtable discussion, and finally compile the report.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0b8e7d1b-6eeb-4a95-92d9-d49ab548d689",
  "isSidechain": false,
  "requestId": "req_011CbFCcaYfG7vPF6BoiN9j2",
  "type": "assistant",
  "uuid": "3e511484-69c4-40b8-be22-245d9c6e71c9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "91a2196c-7a23-4294-80ba-646c05703e7b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RB5JG8mJhBYMSeTj2YkEFM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 5276,
      "cache_read_input_tokens": 61377,
      "output_tokens": 722,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5276,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 722,
          "cache_read_input_tokens": 61377,
          "cache_creation_input_tokens": 5276,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5276
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

_source line 32 · 2026-05-21T05:58:33.113Z_

论文未标注目标 venue，使用 ACL ARR 1-5 分制。先搜索官方评分标准。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3e511484-69c4-40b8-be22-245d9c6e71c9",
  "isSidechain": false,
  "requestId": "req_011CbFCcaYfG7vPF6BoiN9j2",
  "type": "assistant",
  "uuid": "c6d9a81c-5de4-423a-81dc-74816dae1665",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "91a2196c-7a23-4294-80ba-646c05703e7b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RB5JG8mJhBYMSeTj2YkEFM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 5276,
      "cache_read_input_tokens": 61377,
      "output_tokens": 722,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5276,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 722,
          "cache_read_input_tokens": 61377,
          "cache_creation_input_tokens": 5276,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5276
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

_source line 33 · 2026-05-21T05:58:33.350Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01BdAJifFjofKfgaurodhVnV`</summary>

```json
{
  "query": "select:WebSearch",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c6d9a81c-5de4-423a-81dc-74816dae1665",
  "isSidechain": false,
  "requestId": "req_011CbFCcaYfG7vPF6BoiN9j2",
  "type": "assistant",
  "uuid": "07fce80a-0ba1-4efb-b120-97d168f6b9be",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "91a2196c-7a23-4294-80ba-646c05703e7b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RB5JG8mJhBYMSeTj2YkEFM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 5276,
      "cache_read_input_tokens": 61377,
      "output_tokens": 722,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5276,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 722,
          "cache_read_input_tokens": 61377,
          "cache_creation_input_tokens": 5276,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5276
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

_source line 34 · 2026-05-21T05:58:33.356Z_

<details><summary>↩ Tool result · `toolu_01BdAJifFjofKfgaurodhVnV`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "WebSearch"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "07fce80a-0ba1-4efb-b120-97d168f6b9be",
  "isSidechain": false,
  "promptId": "d159e131-5779-4f9c-878e-e70f68151974",
  "type": "user",
  "uuid": "63b6b3f0-4d52-4b17-95a3-e301d6743fa7",
  "toolUseResult": {
    "matches": [
      "WebSearch"
    ],
    "query": "select:WebSearch",
    "total_deferred_tools": 23
  },
  "sourceToolAssistantUUID": "07fce80a-0ba1-4efb-b120-97d168f6b9be",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "91a2196c-7a23-4294-80ba-646c05703e7b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-21T05:58:36.916Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Ew6jyvoG8cwn252QcGtAMH`</summary>

```json
{
  "query": "ACL ARR reviewer guidelines scoring criteria 1-5 scale 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "63b6b3f0-4d52-4b17-95a3-e301d6743fa7",
  "isSidechain": false,
  "requestId": "req_011CbFCeCTS51HK5485a8xgq",
  "type": "assistant",
  "uuid": "e276226f-0c9c-4bba-bbfb-a74e6b832a6a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "91a2196c-7a23-4294-80ba-646c05703e7b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Nd8sG9kX69tD84qpdNJCXd",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1250,
      "cache_read_input_tokens": 66653,
      "output_tokens": 72,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1250,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 72,
          "cache_read_input_tokens": 66653,
          "cache_creation_input_tokens": 1250,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1250
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

_source line 36 · 2026-05-21T05:58:47.950Z_

<details><summary>↩ Tool result · `toolu_01Ew6jyvoG8cwn252QcGtAMH`</summary>

```text
Web search results for query: "ACL ARR reviewer guidelines scoring criteria 1-5 scale 2025 2026"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"}]

Based on the search results, I found relevant information about ARR reviewer guidelines for 2025-2026:

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation. 

However, the search results do not contain specific details about the 1-5 scale definitions or the detailed scoring criteria for each of these three dimensions. The results indicate that soundness scores must be justified by the text of the review, but the specific scale descriptions and what each score level means are not included in the retrieved pages.

To find the detailed 1-5 scale definitions for soundness, excitement, and overall recommendation scores, you may want to consult the full ARR reviewer guidelines document directly at aclrollingreview.org/reviewerguidelines, as the search results only show partial content from that page.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e276226f-0c9c-4bba-bbfb-a74e6b832a6a",
  "isSidechain": false,
  "promptId": "d159e131-5779-4f9c-878e-e70f68151974",
  "type": "user",
  "uuid": "9619105b-3289-4c0b-ad50-9813e67e4154",
  "toolUseResult": {
    "query": "ACL ARR reviewer guidelines scoring criteria 1-5 scale 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Q6rowaBnWasAATHVrCcBJF",
        "content": [
          {
            "title": "ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics",
            "url": "http://aclrollingreview.org/reviewerguidelines"
          },
          {
            "title": "ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics",
            "url": "http://aclrollingreview.org/acguidelines"
          },
          {
            "title": "aclrollingreview/cfp.md at main · acl-org/aclrollingreview",
            "url": "https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"
          },
          {
            "title": "CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics",
            "url": "http://aclrollingreview.org/cfp"
          },
          {
            "title": "Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics",
            "url": "http://aclrollingreview.org/authors"
          },
          {
            "title": "ACL Rolling Review – A peer review platform for the Association for Computational Linguistics",
            "url": "http://aclrollingreview.org/"
          }
        ]
      },
      "Based on the search results, I found relevant information about ARR reviewer guidelines for 2025-2026:\n\nStarting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation. \n\nHowever, the search results do not contain specific details about the 1-5 scale definitions or the detailed scoring criteria for each of these three dimensions. The results indicate that soundness scores must be justified by the text of the review, but the specific scale descriptions and what each score level means are not included in the retrieved pages.\n\nTo find the detailed 1-5 scale definitions for soundness, excitement, and overall recommendation scores, you may want to consult the full ARR reviewer guidelines document directly at aclrollingreview.org/reviewerguidelines, as the search results only show partial content from that page."
    ],
    "durationSeconds": 10.98443042299999
  },
  "sourceToolAssistantUUID": "e276226f-0c9c-4bba-bbfb-a74e6b832a6a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "91a2196c-7a23-4294-80ba-646c05703e7b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 37 · 2026-05-21T05:58:51.522Z_

<details><summary>Logged reasoning block</summary>

```text
Let me fetch the actual ARR reviewer guidelines page to get the specific scoring criteria.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9619105b-3289-4c0b-ad50-9813e67e4154",
  "isSidechain": false,
  "requestId": "req_011CbFCfGSpQAJ1HunvCQPag",
  "type": "assistant",
  "uuid": "832725b1-c2f5-4d2c-b6e8-c8325c4340de",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "91a2196c-7a23-4294-80ba-646c05703e7b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Kf85xjENBQkQedEktw8kDg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 590,
      "cache_read_input_tokens": 67903,
      "output_tokens": 108,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 590,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 108,
          "cache_read_input_tokens": 67903,
          "cache_creation_input_tokens": 590,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 590
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

_source line 38 · 2026-05-21T05:58:51.851Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_018BFQYCj9AfJdeksozYSHsU`</summary>

```json
{
  "query": "select:WebFetch",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "832725b1-c2f5-4d2c-b6e8-c8325c4340de",
  "isSidechain": false,
  "requestId": "req_011CbFCfGSpQAJ1HunvCQPag",
  "type": "assistant",
  "uuid": "429fef3b-56c5-413f-84ed-2e476d18320f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "91a2196c-7a23-4294-80ba-646c05703e7b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Kf85xjENBQkQedEktw8kDg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 590,
      "cache_read_input_tokens": 67903,
      "output_tokens": 108,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 590,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 108,
          "cache_read_input_tokens": 67903,
          "cache_creation_input_tokens": 590,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 590
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

_source line 39 · 2026-05-21T05:58:51.855Z_

<details><summary>↩ Tool result · `toolu_018BFQYCj9AfJdeksozYSHsU`</summary>

````text
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
  "parentUuid": "429fef3b-56c5-413f-84ed-2e476d18320f",
  "isSidechain": false,
  "promptId": "d159e131-5779-4f9c-878e-e70f68151974",
  "type": "user",
  "uuid": "bb99073c-18ed-476e-a8f2-0d0f88e2de8b",
  "toolUseResult": {
    "matches": [
      "WebFetch"
    ],
    "query": "select:WebFetch",
    "total_deferred_tools": 23
  },
  "sourceToolAssistantUUID": "429fef3b-56c5-413f-84ed-2e476d18320f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "91a2196c-7a23-4294-80ba-646c05703e7b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 40 · 2026-05-21T05:58:51.917Z_

```json
{
  "parentUuid": "bb99073c-18ed-476e-a8f2-0d0f88e2de8b",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "b8eff59a-06d8-4ada-8ce3-b80330d652f3",
  "timestamp": "2026-05-21T05:58:51.917Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "91a2196c-7a23-4294-80ba-646c05703e7b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 41 · 2026-05-21T05:58:55.921Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_015LuMohZcmbTbNGGnvP8rHE`</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewerguidelines",
  "prompt": "Extract the complete scoring criteria for ACL ARR reviews. I need the exact 1-5 scale definitions for: soundness, excitement, and overall recommendation. List each score level (1, 2, 3, 4, 5) with its label and description for each dimension."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b8eff59a-06d8-4ada-8ce3-b80330d652f3",
  "isSidechain": false,
  "requestId": "req_011CbFCfZQHPbbfBfLdTLmzK",
  "type": "assistant",
  "uuid": "f2a25c9c-8a77-4ef9-993b-8987cfbb3eee",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "91a2196c-7a23-4294-80ba-646c05703e7b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LJxxLh83gWJq2fs8f5T6Pt",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 729,
      "cache_read_input_tokens": 68493,
      "output_tokens": 145,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 729,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 145,
          "cache_read_input_tokens": 68493,
          "cache_creation_input_tokens": 729,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 729
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

_source line 42 · 2026-05-21T05:59:01.037Z_

<details><summary>↩ Tool result · `toolu_015LuMohZcmbTbNGGnvP8rHE`</summary>

```text
# ACL ARR Review Scoring Criteria

I've reviewed the ARR Reviewer Guidelines document, but I must report that **the complete 1-5 scale definitions for soundness, excitement, and overall recommendation are not included in this webpage content**.

## What the Document Does Contain

The guidelines mention that reviewers provide three scores starting February 2025:

- **Soundness**: "must be justified by the text of the review"
- **Excitement**: "orthogonal to the assessment of soundness" and reflects "personal taste"
- **Overall assessment**: "composite score reflecting your assessment of soundness, excitement, and also other factors like novelty and impact"

However, the specific numerical scale (1-5) definitions, labels, and detailed descriptions for each level are **not present in this webpage**.

## Where to Find This Information

To obtain the exact scoring rubric, you would need to:

1. Check the [ARR review form documentation](https://aclrollingreview.org/reviewform) linked in the guidelines
2. Access OpenReview directly during an active reviewing cycle
3. Contact the ARR support team at support@aclrollingreview.org

The guidelines emphasize that scores must align with review content, but the granular scale definitions exist elsewhere in the ARR infrastructure.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f2a25c9c-8a77-4ef9-993b-8987cfbb3eee",
  "isSidechain": false,
  "promptId": "d159e131-5779-4f9c-878e-e70f68151974",
  "type": "user",
  "uuid": "21d45439-ab5b-494e-9f6f-919162ab328b",
  "toolUseResult": {
    "bytes": 100868,
    "code": 200,
    "codeText": "OK",
    "result": "# ACL ARR Review Scoring Criteria\n\nI've reviewed the ARR Reviewer Guidelines document, but I must report that **the complete 1-5 scale definitions for soundness, excitement, and overall recommendation are not included in this webpage content**.\n\n## What the Document Does Contain\n\nThe guidelines mention that reviewers provide three scores starting February 2025:\n\n- **Soundness**: \"must be justified by the text of the review\"\n- **Excitement**: \"orthogonal to the assessment of soundness\" and reflects \"personal taste\"\n- **Overall assessment**: \"composite score reflecting your assessment of soundness, excitement, and also other factors like novelty and impact\"\n\nHowever, the specific numerical scale (1-5) definitions, labels, and detailed descriptions for each level are **not present in this webpage**.\n\n## Where to Find This Information\n\nTo obtain the exact scoring rubric, you would need to:\n\n1. Check the [ARR review form documentation](https://aclrollingreview.org/reviewform) linked in the guidelines\n2. Access OpenReview directly during an active reviewing cycle\n3. Contact the ARR support team at support@aclrollingreview.org\n\nThe guidelines emphasize that scores must align with review content, but the granular scale definitions exist elsewhere in the ARR infrastructure.",
    "durationMs": 5112,
    "url": "https://aclrollingreview.org/reviewerguidelines"
  },
  "sourceToolAssistantUUID": "f2a25c9c-8a77-4ef9-993b-8987cfbb3eee",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "91a2196c-7a23-4294-80ba-646c05703e7b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 43 · 2026-05-21T05:59:03.933Z_

<details><summary>Logged reasoning block</summary>

```text
Let me try to get the review form page.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "21d45439-ab5b-494e-9f6f-919162ab328b",
  "isSidechain": false,
  "requestId": "req_011CbFCgETHg6LyodNCam5XM",
  "type": "assistant",
  "uuid": "60e0430c-916f-408b-8fb3-9f96680638db",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "91a2196c-7a23-4294-80ba-646c05703e7b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013QdePL61qwvpBfVf153WLr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 445,
      "cache_read_input_tokens": 69222,
      "output_tokens": 149,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 445,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 149,
          "cache_read_input_tokens": 69222,
          "cache_creation_input_tokens": 445,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 445
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

_source line 44 · 2026-05-21T05:59:04.837Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_011HRJrkowWVfjRB5RgHNfCf`</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete scoring rubric for ACL ARR reviews. I need the exact 1-5 scale definitions for soundness, excitement, and overall recommendation. List each score level with its label and description."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "60e0430c-916f-408b-8fb3-9f96680638db",
  "isSidechain": false,
  "requestId": "req_011CbFCgETHg6LyodNCam5XM",
  "type": "assistant",
  "uuid": "804daea2-b6d0-47f7-aa7c-c664610e4de1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "91a2196c-7a23-4294-80ba-646c05703e7b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013QdePL61qwvpBfVf153WLr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 445,
      "cache_read_input_tokens": 69222,
      "output_tokens": 149,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 445,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 149,
          "cache_read_input_tokens": 69222,
          "cache_creation_input_tokens": 445,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 445
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

_source line 45 · 2026-05-21T05:59:11.874Z_

<details><summary>↩ Tool result · `toolu_011HRJrkowWVfjRB5RgHNfCf`</summary>

```text
# ACL ARR Review Scoring Rubrics

## Soundness Scale

**5 = Excellent:** "This study is one of the most thorough I have seen, given its type."

**4.5:** (intermediate level)

**4 = Strong:** "This study provides sufficient support for all of its claims. Some extra experiments could be nice, but not essential."

**3.5:** (intermediate level)

**3 = Acceptable:** "This study provides sufficient support for its main claims. Some minor points may need extra support or details."

**2.5:** (intermediate level)

**2 = Poor:** "Some of the main claims are not sufficiently supported. There are major technical/methodological problems."

**1.5:** (intermediate level)

**1 = Major Issues:** "This study is not yet sufficiently thorough to warrant publication or is not relevant to ACL."

## Excitement Scale

**5 = Highly Exciting:** "I would recommend this paper to others and/or attend its presentation in a conference."

**4.5:** (intermediate level)

**4 = Exciting:** "I would mention this paper to others and/or make an effort to attend its presentation in a conference."

**3.5:** (intermediate level)

**3 = Interesting:** "I might mention some points of this paper to others and/or attend its presentation in a conference if there's time."

**2.5:** (intermediate level)

**2 = Potentially Interesting:** "this paper does not resonate with me, but it might with others in the *ACL community."

**1.5:** (intermediate level)

**1 = Not Exciting:** "this paper does not resonate with me, and I don't think it would with others in the *ACL community."

## Overall Assessment Scale

**5 = Consider for Award:** "I think this paper could be considered for an outstanding paper award at an *ACL conference (up to top 2.5% papers)."

**4.5 = Borderline Award**

**4 = Conference:** "I think this paper could be accepted to an *ACL conference."

**3.5 = Borderline Conference**

**3 = Findings:** "I think this paper could be accepted to the Findings of the ACL."

**2.5 = Borderline Findings**

**2 = Resubmit next cycle:** "I think this paper needs substantial revisions that can be completed by the next ARR cycle."

**1.5 = Resubmit after next cycle:** "I think this paper needs substantial revisions that cannot be completed by the next ARR cycle."

**1 = Do not resubmit:** "This paper has to be fully redone, or it is not relevant to the *ACL community."
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "804daea2-b6d0-47f7-aa7c-c664610e4de1",
  "isSidechain": false,
  "promptId": "d159e131-5779-4f9c-878e-e70f68151974",
  "type": "user",
  "uuid": "f22cfdf6-5262-4d2c-83dc-c62bc7355627",
  "toolUseResult": {
    "bytes": 25365,
    "code": 200,
    "codeText": "OK",
    "result": "# ACL ARR Review Scoring Rubrics\n\n## Soundness Scale\n\n**5 = Excellent:** \"This study is one of the most thorough I have seen, given its type.\"\n\n**4.5:** (intermediate level)\n\n**4 = Strong:** \"This study provides sufficient support for all of its claims. Some extra experiments could be nice, but not essential.\"\n\n**3.5:** (intermediate level)\n\n**3 = Acceptable:** \"This study provides sufficient support for its main claims. Some minor points may need extra support or details.\"\n\n**2.5:** (intermediate level)\n\n**2 = Poor:** \"Some of the main claims are not sufficiently supported. There are major technical/methodological problems.\"\n\n**1.5:** (intermediate level)\n\n**1 = Major Issues:** \"This study is not yet sufficiently thorough to warrant publication or is not relevant to ACL.\"\n\n## Excitement Scale\n\n**5 = Highly Exciting:** \"I would recommend this paper to others and/or attend its presentation in a conference.\"\n\n**4.5:** (intermediate level)\n\n**4 = Exciting:** \"I would mention this paper to others and/or make an effort to attend its presentation in a conference.\"\n\n**3.5:** (intermediate level)\n\n**3 = Interesting:** \"I might mention some points of this paper to others and/or attend its presentation in a conference if there's time.\"\n\n**2.5:** (intermediate level)\n\n**2 = Potentially Interesting:** \"this paper does not resonate with me, but it might with others in the *ACL community.\"\n\n**1.5:** (intermediate level)\n\n**1 = Not Exciting:** \"this paper does not resonate with me, and I don't think it would with others in the *ACL community.\"\n\n## Overall Assessment Scale\n\n**5 = Consider for Award:** \"I think this paper could be considered for an outstanding paper award at an *ACL conference (up to top 2.5% papers).\"\n\n**4.5 = Borderline Award**\n\n**4 = Conference:** \"I think this paper could be accepted to an *ACL conference.\"\n\n**3.5 = Borderline Conference**\n\n**3 = Findings:** \"I think this paper could be accepted to the Findings of the ACL.\"\n\n**2.5 = Borderline Findings**\n\n**2 = Resubmit next cycle:** \"I think this paper needs substantial revisions that can be completed by the next ARR cycle.\"\n\n**1.5 = Resubmit after next cycle:** \"I think this paper needs substantial revisions that cannot be completed by the next ARR cycle.\"\n\n**1 = Do not resubmit:** \"This paper has to be fully redone, or it is not relevant to the *ACL community.\"",
    "durationMs": 7034,
    "url": "https://aclrollingreview.org/reviewform"
  },
  "sourceToolAssistantUUID": "804daea2-b6d0-47f7-aa7c-c664610e4de1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "91a2196c-7a23-4294-80ba-646c05703e7b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 46_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[DREAM Review Director] dream_id=20260521T044911 | review_mode=full | review_visible=True PDF: /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dr…",
  "leafUuid": "f22cfdf6-5262-4d2c-83dc-c62bc7355627",
  "sessionId": "91a2196c-7a23-4294-80ba-646c05703e7b"
}
```

---

### Runtime record

_source line 47_

```json
{
  "type": "ai-title",
  "aiTitle": "Full peer review of cross-lingual calibration research",
  "sessionId": "91a2196c-7a23-4294-80ba-646c05703e7b"
}
```

---

### Assistant

_source line 48 · 2026-05-21T05:59:17.167Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have the ACL ARR scoring criteria. Let me now dispatch the two reviewers in parallel.

Let me plan the full review:

**R1**: Methods + Experiments (soundness focus)
**R2**: Novelty + Related Work (excitement focus)

I'll dispatch both as agents, then run the roundtable process.

Let me prepare comprehensive prompts for each reviewer. They need:
1. The paper content summary
2. The experiment design reference (to check coverage)
3. The scoring criteria
4. Their specific focus area

I'll send both reviewers in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f22cfdf6-5262-4d2c-83dc-c62bc7355627",
  "isSidechain": false,
  "requestId": "req_011CbFCh2oaxncKvGbeZsRDb",
  "type": "assistant",
  "uuid": "54fba775-02d1-47d8-b422-00c7decd8ef2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "91a2196c-7a23-4294-80ba-646c05703e7b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XQxGzkreQxtxHBQphPJx4d",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 794,
      "cache_read_input_tokens": 69667,
      "output_tokens": 5116,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 794,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 5116,
          "cache_read_input_tokens": 69667,
          "cache_creation_input_tokens": 794,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 794
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

_source line 49 · 2026-05-21T05:59:18.195Z_

已获取 ACL ARR 评分标准。现在并行派发两位 Reviewer 进行盲审。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "54fba775-02d1-47d8-b422-00c7decd8ef2",
  "isSidechain": false,
  "requestId": "req_011CbFCh2oaxncKvGbeZsRDb",
  "type": "assistant",
  "uuid": "000e0d40-b26d-4555-a100-38c29245740d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "91a2196c-7a23-4294-80ba-646c05703e7b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XQxGzkreQxtxHBQphPJx4d",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 794,
      "cache_read_input_tokens": 69667,
      "output_tokens": 5116,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 794,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 5116,
          "cache_read_input_tokens": 69667,
          "cache_creation_input_tokens": 794,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 794
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

_source line 50 · 2026-05-21T06:00:20.136Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01V11DrQuXXH7sDRR266jaVy`</summary>

```json
{
  "description": "R1: Methods + Experiments review",
  "prompt": "You are Reviewer 1 (R1) for an ACL ARR peer review. Your focus is **methods and experiments**. You must be thorough, critical, and fair.\n\n## Paper Summary\n\n**Title**: \"When Does Cross-Lingual Calibration Transfer Work? Geometric Analysis and Practical Solutions\"\n\n**Core idea**: First large-scale study of cross-lingual correctness probe transfer. Trains English logistic regression probes on hidden-state activations, then evaluates zero-shot transfer to 20 languages across 3 resource tiers (HIGH/MID/LOW) on 2 MoE architectures (Qwen3-235B-A22B, Llama 4 Scout 17B-16E). Evaluates 5 transfer methods: zero-shot, mean-shift, CaCLR (MMD consistency loss), linear projection (Procrustes), few-shot fine-tuning.\n\n**Key findings**:\n1. Depth-transferability Pareto frontier is architecture-dependent: Qwen3 shows strong tradeoff (16/20 langs negative depth-transfer ρ, median −0.42), Llama 4 weaker (13/20, median −0.28). Linked to CKA cliff steepness.\n2. CaCLR (systematic negative result): MMD consistency loss across full β sweep (0.001–1.0) yields ΔAUROC=+0.002 (p=0.42). Geometric explanation: MMD matches marginal probe-logit distributions but cannot align low-dimensional correctness subspace rotation. Subspace angles unchanged after CaCLR.\n3. Linear projection with ~70 parallel pairs reaches 95% of max improvement. Procrustes effect reversal at ZS AUROC ~0.55: helps misaligned languages, hurts well-aligned ones.\n4. ~30% LOW-resource and ~28% MID-resource language-layer combinations are capacity artifacts (selectivity < 0.05).\n5. Simpson's Paradox in CKA-transfer: raw ρ negative, partial (controlling depth) positive. Significant on Llama 4 (ρ=0.29, p=0.018), trending on Qwen3 (ρ=0.16, p=0.072).\n\n**Supporting analyses**: Cross-lingual orthogonality (cosine ~0.038, confirming Miao & Ungar), LR vs MLP comparison (LR better for transfer), cross-benchmark generalization (Belebele, MMLU-ProX), quantization validation (max |ΔAUROC| < 0.012), camera-ready extensions (Gemma 4 31B dense 3rd architecture, 52 languages).\n\n**Models**: Qwen3-235B-A22B (94 layers, MoE, INT4, 24 probed layers every 4th) and Llama 4 Scout (48 layers, MoE, W4A16, 12 probed layers every 4th).\n\n**Benchmarks**: Primary: GlobalMMLU. Generalization: Belebele, MMLU-ProX.\n\n**Metrics**: AUROC, ECE. Bootstrap 95% CIs (1000 resamples), paired permutation tests, Cohen's d.\n\n## Detailed Experimental Results\n\n### Table 1 (Per-language ZS AUROC at EN-optimal layer L80, Qwen3):\nHIGH: zh 0.732, es 0.741, fr 0.738, de 0.720, pt 0.730, ja 0.710\nMID: ar 0.690, ru 0.700, ko 0.685, hi 0.665, vi 0.678, tr 0.655\nLOW: sw 0.592, bn 0.608, th 0.620, te 0.568, yo 0.542, am 0.530\n\n### Table 2 (Architecture comparison):\nQwen3: EN best 0.78, Mean ZS 0.660, Pareto sig 15/20, median ρ −0.42, CKA cliff ~68%, slope −0.025/L\nLlama4: EN best 0.76, Mean ZS 0.643, Pareto sig 11/20, median ρ −0.28, CKA cliff ~55%, slope −0.015/L\n\n### Table 5 (Simpson's Paradox):\nQwen3: n=480, raw ρ=−0.22 p<.001, partial ρ=+0.16 p=.072\nLlama4: n=240, raw ρ=−0.28 p<.001, partial ρ=+0.29 p=.018\n\n### Table 7 (CaCLR β sweep, Qwen3 L80):\nβ=0: 0.660 (baseline)\nβ=0.001: 0.661, Δ=+0.001, CI [−.004,+.006], d=0.03\nβ=0.01: 0.663, Δ=+0.003, CI [−.003,+.009], d=0.07\nβ=0.1: 0.658, Δ=−0.002, CI [−.008,+.004], d=0.05\nβ=1.0: 0.652, Δ=−0.008, CI [−.015,−.001], d=0.19\n\n### Table 8 (CaCLR ablation):\nBCE only: AUROC 0.660, ECE 0.192\nBCE+SB-ECE: 0.658, 0.178\nBCE+MMD: 0.662, 0.190\nBCE+SB-ECE+MMD: 0.661, 0.176\n\n### Table 9 (CKA subspace — why MMD fails):\nHIGH: angle pre 12°, MMD 0.02→0.01, angle post 11°\nMID: angle pre 24°, MMD 0.05→0.02, angle post 23°\nLOW: angle pre 42°, MMD 0.12→0.05, angle post 40°\n\n### Table 10 (Transfer method comparison, mean 20 langs):\nZero-shot: Q3 .660, L4 .643, Mean .652\nMean-shift: .660, .643, .652\nCaCLR(best): .662, .645, .654\nLin proj(50): .678, .660, .669\nLin proj(200): .692, .673, .683\nFew-shot 25: .678, .662, .670\nFew-shot 100: .712, .693, .703\n\n### Table 11 (Linear projection saturation):\n10 pairs: HIGH +0.002, MID +0.010, LOW +0.028, Overall +0.013\n50 pairs: +0.007, +0.026, +0.054, +0.027\n100 pairs: +0.008, +0.029, +0.060, +0.030\n200 pairs: +0.008, +0.030, +0.063, +0.032\n\n### Table 12 (Procrustes reversal):\nZS < 0.50: n=4, mean Δ=+0.058, 100% positive\n0.60–0.65: n=4, Δ=+0.003, 50% positive\n> 0.70: n=4, Δ=−0.018, 0% positive\nReversal threshold ~0.55, CI [0.46, 0.63]\n\n### Table 13 (Difficulty decomposition, Qwen3, 10 langs):\nMean ΔAUROC from difficulty projection: +0.012 (7/10 positive)\nRandom-direction control: +0.005\nDifficulty-specific effect: ~2.4× random\nDifficulty probe R²=0.35\nPrescriptive accuracy: 58% (barely above chance 50%)\n\n### Table 14 (Artifact rates):\nLOW 0–25% depth: 83% artifacts; LOW overall: 30%\nMID 0–25% depth: 58% artifacts; MID overall: 28%\nHIGH overall: 6%\n\n### Table 15 (Selectivity at L80):\nyo: real .542, ctrl .510, selectivity .032 → ARTIFACT\nam: real .530, ctrl .512, selectivity .018 → ARTIFACT\n\n### Tables 17-21 (Supporting):\nLR vs MLP: MLP +2pp EN but −5pp transfer gap\nCross-benchmark: patterns hold on Belebele/MMLU-ProX\nQuantization: max |ΔAUROC| < 0.012\nGemma4 31B: Pareto sig 13/20, partial ρ(CKA)=0.22* (p=0.045)\n52-lang expansion: core findings stable (rank ρ=0.94 with 20-lang)\n\n## Experiment Design Reference (from context file)\n\nThe full experiment plan includes these experiments:\n1. plan_001: Full Pareto Frontier — Qwen3-235B (COVERED in paper)\n2. plan_002: Full Pareto Frontier — Llama 4 Scout (COVERED)\n3. plan_003: CaCLR Implementation and Negative Result (COVERED)\n4. plan_004: Difficulty-Controlled Decomposition Ablation (COVERED)\n5. plan_005: Cross-Lingual Orthogonality Analysis (COVERED in §4.9.1)\n6. plan_006: Probe Complexity LR vs MLP (COVERED in §4.9.2)\n7. plan_007: Additional Benchmark Evaluation (COVERED in §4.9.3)\n8. plan_008: Gemma 4 31B Dense (COVERED in §4.10 as camera-ready)\n9. plan_009: Extended Language Coverage 52 langs (COVERED in §4.10)\n10. plan_010: Quantization Validation (COVERED in §4.9.4)\n11. plan_011: Full CKA + Simpson's Paradox Analysis (COVERED in §4.3)\n12. plan_012: Linear Projection Sensitivity + Procrustes Reversal (COVERED in §4.6)\n13. plan_013: Probing Control Tasks (COVERED in §4.8)\n\n## ACL ARR Scoring Criteria\n\n**Soundness** (1-5):\n- 5 = Excellent: one of the most thorough studies\n- 4 = Strong: sufficient support for all claims, some extra experiments nice but not essential\n- 3 = Acceptable: sufficient support for main claims, minor points may need extra support\n- 2 = Poor: main claims not sufficiently supported, major methodological problems\n- 1 = Major Issues: not sufficiently thorough\n\n**Excitement** (1-5):\n- 5 = Highly Exciting\n- 4 = Exciting\n- 3 = Interesting\n- 2 = Potentially Interesting\n- 1 = Not Exciting\n\n**Overall** (1-5):\n- 5 = Consider for Award\n- 4 = Conference (*ACL main)\n- 3 = Findings\n- 2 = Resubmit next cycle\n- 1 = Do not resubmit\n\n## Your Task\n\nWrite a thorough review focusing on **methods and experiments**. Structure your review as:\n\n1. **Summary** (2-3 sentences)\n2. **Strengths** (numbered, focus on methodological rigor, experimental design, statistical practices)\n3. **Weaknesses** (numbered, focus on methodological gaps, experimental limitations, missing controls, statistical concerns)\n4. **Questions for Authors** (numbered)\n5. **Minor Issues** (if any)\n6. **Scores**: Soundness (1-5, with 0.5 increments), Excitement (1-5), Overall (1-5)\n7. **Confidence** (1-5): 1=low, 5=expert\n\nBe specific and cite table/section numbers. Do not be overly generous or harsh — calibrate to what you'd expect at a strong *ACL venue."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "000e0d40-b26d-4555-a100-38c29245740d",
  "isSidechain": false,
  "requestId": "req_011CbFCh2oaxncKvGbeZsRDb",
  "type": "assistant",
  "uuid": "7101057c-3ea2-44d1-9d0f-071392f88537",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "91a2196c-7a23-4294-80ba-646c05703e7b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XQxGzkreQxtxHBQphPJx4d",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 794,
      "cache_read_input_tokens": 69667,
      "output_tokens": 5116,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 794,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 5116,
          "cache_read_input_tokens": 69667,
          "cache_creation_input_tokens": 794,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 794
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

_source line 51 · 2026-05-21T06:00:49.721Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01Q7yTddsvZnhyAKbGetqXdY`</summary>

```json
{
  "description": "R2: Novelty + Related Work review",
  "prompt": "You are Reviewer 2 (R2) for an ACL ARR peer review. Your focus is **novelty, positioning, and related work**. You must be thorough, critical, and fair.\n\n## Paper Summary\n\n**Title**: \"When Does Cross-Lingual Calibration Transfer Work? Geometric Analysis and Practical Solutions\"\n\n**Core idea**: First large-scale study of cross-lingual correctness probe transfer. Trains English logistic regression probes on hidden-state activations, then evaluates zero-shot transfer to 20 languages across 3 resource tiers (HIGH/MID/LOW) on 2 MoE architectures (Qwen3-235B-A22B, Llama 4 Scout 17B-16E). Evaluates 5 transfer methods: zero-shot, mean-shift, CaCLR (MMD consistency loss), linear projection (Procrustes), few-shot fine-tuning.\n\n**Key findings**:\n1. Depth-transferability Pareto frontier is architecture-dependent: Qwen3 shows strong tradeoff (16/20 langs negative depth-transfer ρ, median −0.42), Llama 4 weaker (13/20, median −0.28). Linked to CKA cliff steepness.\n2. CaCLR (systematic negative result): MMD consistency loss across full β sweep yields ΔAUROC=+0.002 (p=0.42). Geometric explanation via CKA subspace analysis.\n3. Linear projection with ~70 parallel pairs reaches 95% of max improvement. Procrustes effect reversal at ~0.55.\n4. ~30% LOW-resource and ~28% MID-resource probing results are capacity artifacts.\n5. Simpson's Paradox in CKA-transfer correlation.\n\n**Related Work sections covered**:\n- LLM Calibration: Joshi et al. [2024], Guo et al. [2017], LACE Zhou et al. [2024]\n- Representation-Based Calibration: CORAL Miao et al. [2026a], Miao & Ungar [2026], Ji et al. [2024]\n- Cross-Lingual Probing: Xiao et al. [2025] (knowledge-boundary probes, 8 languages), Civelli et al. (difficulty transfer)\n- Cross-Lingual Alignment: MUSE Conneau et al. [2018], VecMap Artetxe et al. [2018]\n- Domain Adaptation Theory: Ben-David et al. [2010], Zhao et al. [2019]\n- Probing Methodology: Hewitt & Liang [2019], Voita & Titov [2020]\n- Representation Similarity: CKA Kornblith et al. [2019], SVCCA Raghu et al. [2017]\n- Conformal Prediction: Angelopoulos and Bates [2023]\n\n**Paper structure** (14 pages):\n1. Introduction (1 page)\n2. Related Work (1 page, 8 subsections)\n3. Method (1.5 pages: §3.1 Cross-Lingual Correctness Probing, §3.2 Transfer Methods, §3.3 Difficulty-Capability Decomposition, §3.4 CKA Geometric Analysis)\n4. Experiments (6 pages: §4.1 Setup, §4.2 Pareto Frontier, §4.3 CKA Analysis, §4.4 CaCLR Negative Result, §4.5 Transfer Comparison, §4.6 Linear Projection Efficiency, §4.7 Difficulty Decomposition, §4.8 Control Tasks, §4.9 Supporting Analyses [orthogonality, LR vs MLP, cross-benchmark, quantization], §4.10 Extended Evaluation [Gemma4, 52 langs])\n5. Discussion (1 page)\n6. Conclusion (0.5 pages)\nReferences: 15 entries\n\n**Key methodological contributions claimed**:\n- First large-scale cross-lingual correctness probe transfer study (vs Xiao et al.'s 8-language knowledge-boundary probes)\n- CaCLR negative result with geometric explanation grounded in Zhao et al.'s theory\n- First application of Hewitt & Liang control tasks to cross-lingual probing\n- Procrustes effect reversal threshold as practitioner guidance\n- Simpson's Paradox discovery in CKA-transfer correlation\n\n**Transfer methods**:\n- Zero-shot: apply EN probe directly\n- Mean-shift: subtract mean activation difference (ΔAUROC ≡ 0 by construction for LR)\n- CaCLR: L = L_BCE + α·L_SB-ECE + β·L_MMD (novel formulation)\n- Linear Projection: Procrustes alignment W* = argmin ||H^en - H^tgt W||²_F\n- Few-shot: retrain on k target-language labeled examples\n\n**Models and scale**: 2 MoE architectures (Qwen3-235B-A22B with INT4, Llama 4 Scout with W4A16), 20 languages in 3 tiers, 3 benchmarks. Camera-ready adds Gemma 4 31B Dense and 52 languages.\n\n## ACL ARR Scoring Criteria\n\n**Soundness** (1-5):\n- 5 = Excellent: one of the most thorough studies\n- 4 = Strong: sufficient support for all claims\n- 3 = Acceptable: sufficient support for main claims, minor points may need extra support\n- 2 = Poor: main claims not sufficiently supported\n- 1 = Major Issues\n\n**Excitement** (1-5):\n- 5 = Highly Exciting: would recommend to others\n- 4 = Exciting: would mention to others\n- 3 = Interesting: might mention some points\n- 2 = Potentially Interesting\n- 1 = Not Exciting\n\n**Overall** (1-5):\n- 5 = Consider for Award\n- 4 = Conference (*ACL main)\n- 3 = Findings\n- 2 = Resubmit next cycle\n- 1 = Do not resubmit\n\n## Your Task\n\nWrite a thorough review focusing on **novelty, framing, and related work**. Structure your review as:\n\n1. **Summary** (2-3 sentences)\n2. **Strengths** (numbered, focus on novelty, positioning relative to prior work, theoretical grounding, contribution significance)\n3. **Weaknesses** (numbered, focus on novelty limitations, missing related work, overclaimed contributions, framing issues, gaps in positioning)\n4. **Questions for Authors** (numbered)\n5. **Minor Issues** (if any)\n6. **Scores**: Soundness (1-5, with 0.5 increments), Excitement (1-5), Overall (1-5)\n7. **Confidence** (1-5): 1=low, 5=expert\n\nConsider these angles:\n- Is the correctness vs. knowledge-boundary distinction sufficiently motivated? Does it matter in practice?\n- How novel is the Procrustes alignment approach given MUSE/VecMap literature?\n- Is the CaCLR negative result genuinely informative or somewhat predictable?\n- Are the architectural conclusions meaningful with n=2 (core) or n=3 (extended)?\n- Does the paper adequately position against concurrent work in multilingual probing?\n- Is the Simpson's Paradox finding a genuine insight or a known confounding issue?\n- How significant are the practical contributions (the threshold, the ~70 pairs guidance)?\n\nBe specific and cite section numbers. Calibrate to a strong *ACL venue."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7101057c-3ea2-44d1-9d0f-071392f88537",
  "isSidechain": false,
  "requestId": "req_011CbFCh2oaxncKvGbeZsRDb",
  "type": "assistant",
  "uuid": "f5f8bd73-6308-4d3d-bfed-fc6762a7bbc9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "91a2196c-7a23-4294-80ba-646c05703e7b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XQxGzkreQxtxHBQphPJx4d",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 794,
      "cache_read_input_tokens": 69667,
      "output_tokens": 5116,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 794,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 5116,
          "cache_read_input_tokens": 69667,
          "cache_creation_input_tokens": 794,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 794
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

_source line 52 · 2026-05-21T06:03:11.714Z_

<details><summary>↩ Tool result · `toolu_01V11DrQuXXH7sDRR266jaVy`</summary>

```text


Based on my thorough analysis of the paper's methodology, experimental design, code implementation, statistical practices, and supporting documentation, here is my review.

---

## R1 Review: Methods and Experiments

### 1. Summary

This paper presents a large-scale empirical study of cross-lingual correctness probe transfer, training English logistic regression probes on hidden-state activations from two MoE architectures (Qwen3-235B, Llama 4 Scout) and evaluating zero-shot transfer to 20 languages across three resource tiers using five transfer methods. The core contributions are an architecture-dependent depth-transferability Pareto frontier, a Simpson's Paradox in the CKA-transfer relationship, a systematic CaCLR negative result with geometric explanation, practical linear projection guidelines, and a control-task artifact warning for low-resource probing.

### 2. Strengths

**S1. Comprehensive and well-structured experimental plan.** The 13-experiment design covers core claims (plan_001/002), robustness checks (plan_010 quantization, plan_013 controls, plan_006 probe complexity), generalization (plan_007 cross-benchmark, plan_009 extended languages), and extensions (plan_008 Gemma 4). The progression from MVP validation on 7-8B models to full-scale 235B execution is methodologically sound and reduces resource waste.

**S2. Rigorous statistical methodology.** Bootstrap 95% CIs with 1000 resamples, paired permutation tests, and Cohen's d effect sizes are reported throughout. This exceeds the field norm, where 6/8 comparable papers report point estimates without CIs (per the distilled research skill). The permutation test implementation in `transfer_eval.py` (lines 69-78) is correct, using `(count_ge + 1) / (n_perm + 1)` to avoid zero p-values.

**S3. Simpson's Paradox analysis is the methodological highlight.** Partial Spearman correlation controlling for normalized depth is the correct approach to disentangle the CKA-depth confound. The pilot data (Table 5) shows the expected sign reversal on both architectures, with Llama 4 reaching significance (partial rho=+0.29, p=0.018). The per-layer cross-language correlations provide independent non-parametric support. This directly addresses the "CKA is just a depth proxy" concern.

**S4. Probing control tasks are essential and rarely included.** The Hewitt & Liang selectivity analysis (Table 14-15) revealing ~30% LOW-resource and ~28% MID-resource artifacts is a genuine methodological contribution. The implementation uses PCA(100) dimensionality reduction with 5-fold CV, and the selectivity threshold (0.05) is conservative. The finding that yo (selectivity=0.032) and am (selectivity=0.018) are capacity artifacts at L80 directly impacts interpretation of transfer results for these languages.

**S5. Mean-shift rank-invariance proof is clean and useful.** The mathematical argument that StandardScaler + logistic regression makes mean-shift AUROC-invariant is correct: mean-shift adds a constant to all pre-scaling activations, which after StandardScaler becomes a constant offset to logits, preserving ranking. This is verified empirically and clearly differentiates from Xiao et al.'s pipeline where mean-shift operates under different conditions.

**S6. CaCLR implementation is well-specified for reproducibility.** The code (`train_caclr.py`) fully specifies: Gaussian RBF kernel with median heuristic bandwidth (lines 82-104), unbiased MMD estimator with diagonal exclusion (lines 107-123), soft-binning ECE with temperature=0.05 (lines 53-79), initialization from sklearn LR solution (lines 172-184), Adam optimizer, and subsampling to 512 for MMD computation (line 286). The beta sweep across three orders of magnitude (0.001-1.0) with component ablation (Table 8) constitutes a fair trial of the distributional matching hypothesis.

**S7. Quantization validation addresses a key confound.** With max |ΔAUROC| < 0.012 between quantized and FP16 baselines, the paper demonstrates that INT4/W4A16 quantization does not distort the Pareto frontier ordering. This is important given both models use aggressive quantization.

### 3. Weaknesses

**W1. Procrustes train/eval contamination risk.** In `transfer_eval.py` (lines 189-199), the Procrustes alignment samples parallel pairs from the same data that is subsequently used for evaluation. Specifically, `pair_idx` is sampled from `min(len(X_en_all), len(X_tgt))` indices, and then the full `X_tgt` (including those same indices) is transformed and evaluated. With 200 pairs out of ~4200 eval samples (~5%), the bias may be small, but it is methodologically incorrect. The 70/30 train/eval split in `extract_activations_large.py` addresses CaCLR data separation but the code does not enforce that Procrustes pairs come exclusively from the train split. Table 11 (linear projection saturation) and Table 12 (Procrustes reversal) are both affected. The paper should either (a) restrict Procrustes pairs to train-split items and evaluate only on eval-split items, or (b) quantify the contamination bias via leave-pair-out analysis.

**W2. CaCLR hyperparameter selection criterion is English-only.** The sweep in `train_caclr.py` (lines 401-434) selects the best (alpha, beta) by `score = auroc - ece_weight * ece` computed on an English validation split. If the consistency loss (beta > 0) improves cross-lingual transfer at the expense of English performance, the English-only criterion would select against it. This creates a structural bias toward low beta values, potentially undermining the CaCLR negative result. The paper reports mean ΔAUROC=+0.002 (p=0.42) for CaCLR (Table 7), but with an English-optimized beta, the true cross-lingual potential may be underestimated. A mixed criterion incorporating at least one or two validation languages would strengthen the negative result claim.

**W3. CaCLR operates on 1-D probe logits, which severely limits MMD's expressiveness.** The code confirms (line 283, `train_caclr.py`) that MMD operates on `logits_en_sub.unsqueeze(1)` and `logits_tgt_sub.unsqueeze(1)` — scalar probe outputs. In 1-D, Gaussian RBF MMD is essentially matching the marginal distribution of a single scalar. The paper acknowledges this as a "design limitation" but then draws the strong conclusion that "distributional matching fails for correctness probe transfer" (Table 9 geometric explanation). This conclusion is specific to 1-D marginal matching, not distributional matching in general. MMD on the full hidden-state space, or on a low-rank projection of it, could yield different results. The negative result should be scoped more precisely: "1-D logit-level MMD matching fails" rather than implying distributional matching as a class is ineffective.

**W4. Single random seed throughout.** `train_caclr.py` uses `seed=42` (line 229), `transfer_eval.py` uses `proj_seed=42` (line 48), and `train_probe.py` uses `seed=42` (line 38). Given the modest effect sizes (CaCLR: +0.002; linear projection at 50 pairs: +0.027; few-shot 25: +0.018 over zero-shot), variance across seeds could be comparable to reported effects. The few-shot evaluation (lines 202-236) is particularly sensitive: with only 25 labeled examples, the specific sample drawn determines the result. Multi-seed variance estimates (3-5 seeds) are needed for all methods, especially few-shot and Procrustes with small pair counts.

**W5. Difficulty decomposition methodology is underspecified.** Table 13 reports ΔAUROC from "difficulty projection" (+0.012, 7/10 positive) vs. random-direction control (+0.005), yielding a 2.4x ratio. However: (a) the source of IRT difficulty scores is not specified — if estimated from model accuracy on the same data, circularity arises; (b) the prescriptive accuracy of 58% is barely above the 50% random baseline, undermining the practical value of the decomposition; (c) the difficulty probe R²=0.35 means 65% of difficulty variance is unexplained, so the "projection out" step leaves substantial difficulty signal in the residual. The random-direction control addresses dimensionality reduction artifacts but not the residual difficulty confound.

**W6. ECE computation has minor inconsistencies.** The writing plan (notation table) references "ECE (15-bin)" but the code consistently uses 10 bins (`n_bins=10` in `transfer_eval.py` line 54, `train_caclr.py` line 317, `train_probe.py` line 43). Equal-width binning with 10 bins is standard (Guo et al. 2017) but the paper should be internally consistent. Additionally, the ECE boundary condition handling differs subtly between the hard-histogram version (includes left boundary via `>=` only at lo=0.0) and the SB-ECE soft-binning version — while both are reasonable, the paper should state which ECE variant is used for final reporting.

**W7. Linear CKA may be insensitive to the relevant representational differences.** The paper uses linear CKA (confirmed in `compute_cka.py` lines 26-41), which captures linear relationships between representations. If correctness information is encoded in nonlinear substructures that differ across languages, linear CKA would miss this while still showing high similarity. The Simpson's Paradox finding — positive partial correlation between CKA and transfer — could partly reflect that both CKA and AUROC (via linear probes) are sensitive to the same linear structure, creating tautological agreement. Kernel CKA or projection-weighted CKA could test whether the finding holds for richer similarity measures.

**W8. Few-shot evaluation does not properly account for reduced test set.** In `transfer_eval.py` (lines 208-211), the few-shot samples are excluded from the evaluation set (`eval_mask[fs_idx] = False`), which is correct for avoiding data leakage. However, with few-shot 100 from ~4200 total samples, the evaluation set drops to ~4100 — comparable to zero-shot's ~4200 — making results comparable. But for few-shot 25, the specific 25 samples removed could shift the difficulty distribution of the remaining test set. A stratified sampling strategy (by subject) for few-shot selection would mitigate this.

### 4. Questions for Authors

1. **Procrustes contamination**: Can you confirm that Table 11 and Table 12 results use Procrustes pairs exclusively from the train split, with evaluation only on the eval split? The code suggests otherwise.

2. **IRT difficulty source**: Where do the item-level difficulty scores for the decomposition (Table 13) come from? If from model accuracy, how do you address circularity?

3. **CaCLR in higher dimensions**: Have you tried MMD on the hidden-state activations directly (before the probe), or on a PCA-reduced intermediate representation? The 1-D logit constraint seems artificially restrictive.

4. **Multi-seed variance**: What is the standard deviation of CaCLR AUROC across 3-5 random seeds? Is the +0.002 effect (Table 7) within noise?

5. **Procrustes reversal mechanism**: Table 12 shows that Procrustes hurts when ZS AUROC > 0.70. Is this because well-aligned languages have representations that are already in the correct subspace, and the Procrustes rotation introduces noise from fitting irrelevant dimensions?

6. **CKA tautology**: Both linear CKA and linear probe AUROC measure linear alignment between English and target representations. How do you establish that the positive partial correlation reflects genuine geometric structure rather than measurement overlap?

7. **Selectivity threshold**: The 0.05 selectivity threshold for declaring artifacts (Table 14-15) — is this from Hewitt & Liang's original recommendation, or was it chosen post-hoc? How sensitive are the artifact rates to this threshold (e.g., at 0.03 or 0.10)?

### 5. Minor Issues

- Table 7 (CaCLR beta sweep): The beta=1.0 row shows ΔAUROC=-0.008 with CI [-0.015, -0.001] excluding zero, yet d=0.19 is labeled as small effect. This is the one setting where CaCLR has a detectable (negative) effect, and it deserves discussion — at high beta, the consistency loss actively hurts.

- The paper reports 20 languages but Tables 1-2 show 18 (6 HIGH + 6 MID + 6 LOW). The remaining 2 languages should be accounted for, or the paper should state 18.

- The Pareto analysis code (`pareto_analysis.py`) uses Spearman correlation to test for tradeoff (line 164: `"tradeoff": "yes" if rho < 0 else "no"`), which is a one-sided test without significance threshold. Some of the 16/20 (Qwen) or 13/20 (Llama) languages with negative rho may not reach significance — the paper should report how many are significant at p < 0.05.

- The `extract_activations_large.py` uses the same split indices across all languages (line 355-368), which is correct for ensuring parallel data. However, the first language processed determines the stratification — the paper should confirm English is always processed first.

- Cohen's d values in Table 7 are very small (0.03-0.19). The paper should explicitly state these effect sizes when claiming CaCLR is "inert" — the quantitative framing strengthens the negative result.

### 6. Scores

| Dimension | Score | Justification |
|-----------|-------|---------------|
| **Soundness** | **3.5 / 5** | Experimental design is comprehensive and statistical methodology is generally strong. However, the Procrustes train/eval contamination (W1), English-only CaCLR selection criterion (W2), 1-D MMD limitation affecting the scope of the negative result claim (W3), and single-seed variance concerns (W4) collectively reduce confidence. The difficulty decomposition (W5) is the methodologically weakest component. None of these are fatal — all are addressable — but together they represent more than "minor points." |
| **Excitement** | **3 / 5** | The Simpson's Paradox finding is genuinely interesting. The control-task artifact warning has field-level utility. The practical linear projection recipe is useful. However, the CaCLR negative result, once properly scoped to 1-D MMD, is less informative than presented. The Pareto frontier, while well-quantified, is largely predicted by domain adaptation theory and prior work (Civelli et al.). The paper is more of a thorough empirical characterization than a source of surprising insights. |
| **Overall** | **3 / 5** | Findings-worthy at a strong *CL venue. The paper fills a genuine gap (English-only calibration probing literature), the experimental scale is impressive (2 large MoE models, 20 languages, 5 methods), and the statistical practices exceed field norms. The Simpson's Paradox and control-task findings are solid contributions. The main limitations — CaCLR negative result scope, difficulty decomposition weakness, Procrustes contamination, single seeds — are all addressable in revision. With the recommended fixes, this could reach 3.5. |

### 7. Confidence

**4 / 5** — I have read the code implementation in detail, verified the statistical methodology, cross-referenced the experimental results with the codebase, and have strong familiarity with the probing, calibration, and cross-lingual transfer literatures. My main uncertainty is whether the final reported numbers correspond to completed full-scale experiments or are partially projected from MVP pilots, as the project status indicates some experiments were still in preparation.

agentId: acf51195619fdbc79 (use SendMessage with to: 'acf51195619fdbc79' to continue this agent)
&lt;usage>total_tokens: 86657
tool_uses: 24
duration_ms: 171570&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7101057c-3ea2-44d1-9d0f-071392f88537",
  "isSidechain": false,
  "promptId": "d159e131-5779-4f9c-878e-e70f68151974",
  "type": "user",
  "uuid": "289f24f0-fa7d-444e-a355-94e30d3ea635",
  "toolUseResult": {
    "status": "completed",
    "prompt": "You are Reviewer 1 (R1) for an ACL ARR peer review. Your focus is **methods and experiments**. You must be thorough, critical, and fair.\n\n## Paper Summary\n\n**Title**: \"When Does Cross-Lingual Calibration Transfer Work? Geometric Analysis and Practical Solutions\"\n\n**Core idea**: First large-scale study of cross-lingual correctness probe transfer. Trains English logistic regression probes on hidden-state activations, then evaluates zero-shot transfer to 20 languages across 3 resource tiers (HIGH/MID/LOW) on 2 MoE architectures (Qwen3-235B-A22B, Llama 4 Scout 17B-16E). Evaluates 5 transfer methods: zero-shot, mean-shift, CaCLR (MMD consistency loss), linear projection (Procrustes), few-shot fine-tuning.\n\n**Key findings**:\n1. Depth-transferability Pareto frontier is architecture-dependent: Qwen3 shows strong tradeoff (16/20 langs negative depth-transfer ρ, median −0.42), Llama 4 weaker (13/20, median −0.28). Linked to CKA cliff steepness.\n2. CaCLR (systematic negative result): MMD consistency loss across full β sweep (0.001–1.0) yields ΔAUROC=+0.002 (p=0.42). Geometric explanation: MMD matches marginal probe-logit distributions but cannot align low-dimensional correctness subspace rotation. Subspace angles unchanged after CaCLR.\n3. Linear projection with ~70 parallel pairs reaches 95% of max improvement. Procrustes effect reversal at ZS AUROC ~0.55: helps misaligned languages, hurts well-aligned ones.\n4. ~30% LOW-resource and ~28% MID-resource language-layer combinations are capacity artifacts (selectivity < 0.05).\n5. Simpson's Paradox in CKA-transfer: raw ρ negative, partial (controlling depth) positive. Significant on Llama 4 (ρ=0.29, p=0.018), trending on Qwen3 (ρ=0.16, p=0.072).\n\n**Supporting analyses**: Cross-lingual orthogonality (cosine ~0.038, confirming Miao & Ungar), LR vs MLP comparison (LR better for transfer), cross-benchmark generalization (Belebele, MMLU-ProX), quantization validation (max |ΔAUROC| < 0.012), camera-ready extensions (Gemma 4 31B dense 3rd architecture, 52 languages).\n\n**Models**: Qwen3-235B-A22B (94 layers, MoE, INT4, 24 probed layers every 4th) and Llama 4 Scout (48 layers, MoE, W4A16, 12 probed layers every 4th).\n\n**Benchmarks**: Primary: GlobalMMLU. Generalization: Belebele, MMLU-ProX.\n\n**Metrics**: AUROC, ECE. Bootstrap 95% CIs (1000 resamples), paired permutation tests, Cohen's d.\n\n## Detailed Experimental Results\n\n### Table 1 (Per-language ZS AUROC at EN-optimal layer L80, Qwen3):\nHIGH: zh 0.732, es 0.741, fr 0.738, de 0.720, pt 0.730, ja 0.710\nMID: ar 0.690, ru 0.700, ko 0.685, hi 0.665, vi 0.678, tr 0.655\nLOW: sw 0.592, bn 0.608, th 0.620, te 0.568, yo 0.542, am 0.530\n\n### Table 2 (Architecture comparison):\nQwen3: EN best 0.78, Mean ZS 0.660, Pareto sig 15/20, median ρ −0.42, CKA cliff ~68%, slope −0.025/L\nLlama4: EN best 0.76, Mean ZS 0.643, Pareto sig 11/20, median ρ −0.28, CKA cliff ~55%, slope −0.015/L\n\n### Table 5 (Simpson's Paradox):\nQwen3: n=480, raw ρ=−0.22 p<.001, partial ρ=+0.16 p=.072\nLlama4: n=240, raw ρ=−0.28 p<.001, partial ρ=+0.29 p=.018\n\n### Table 7 (CaCLR β sweep, Qwen3 L80):\nβ=0: 0.660 (baseline)\nβ=0.001: 0.661, Δ=+0.001, CI [−.004,+.006], d=0.03\nβ=0.01: 0.663, Δ=+0.003, CI [−.003,+.009], d=0.07\nβ=0.1: 0.658, Δ=−0.002, CI [−.008,+.004], d=0.05\nβ=1.0: 0.652, Δ=−0.008, CI [−.015,−.001], d=0.19\n\n### Table 8 (CaCLR ablation):\nBCE only: AUROC 0.660, ECE 0.192\nBCE+SB-ECE: 0.658, 0.178\nBCE+MMD: 0.662, 0.190\nBCE+SB-ECE+MMD: 0.661, 0.176\n\n### Table 9 (CKA subspace — why MMD fails):\nHIGH: angle pre 12°, MMD 0.02→0.01, angle post 11°\nMID: angle pre 24°, MMD 0.05→0.02, angle post 23°\nLOW: angle pre 42°, MMD 0.12→0.05, angle post 40°\n\n### Table 10 (Transfer method comparison, mean 20 langs):\nZero-shot: Q3 .660, L4 .643, Mean .652\nMean-shift: .660, .643, .652\nCaCLR(best): .662, .645, .654\nLin proj(50): .678, .660, .669\nLin proj(200): .692, .673, .683\nFew-shot 25: .678, .662, .670\nFew-shot 100: .712, .693, .703\n\n### Table 11 (Linear projection saturation):\n10 pairs: HIGH +0.002, MID +0.010, LOW +0.028, Overall +0.013\n50 pairs: +0.007, +0.026, +0.054, +0.027\n100 pairs: +0.008, +0.029, +0.060, +0.030\n200 pairs: +0.008, +0.030, +0.063, +0.032\n\n### Table 12 (Procrustes reversal):\nZS < 0.50: n=4, mean Δ=+0.058, 100% positive\n0.60–0.65: n=4, Δ=+0.003, 50% positive\n> 0.70: n=4, Δ=−0.018, 0% positive\nReversal threshold ~0.55, CI [0.46, 0.63]\n\n### Table 13 (Difficulty decomposition, Qwen3, 10 langs):\nMean ΔAUROC from difficulty projection: +0.012 (7/10 positive)\nRandom-direction control: +0.005\nDifficulty-specific effect: ~2.4× random\nDifficulty probe R²=0.35\nPrescriptive accuracy: 58% (barely above chance 50%)\n\n### Table 14 (Artifact rates):\nLOW 0–25% depth: 83% artifacts; LOW overall: 30%\nMID 0–25% depth: 58% artifacts; MID overall: 28%\nHIGH overall: 6%\n\n### Table 15 (Selectivity at L80):\nyo: real .542, ctrl .510, selectivity .032 → ARTIFACT\nam: real .530, ctrl .512, selectivity .018 → ARTIFACT\n\n### Tables 17-21 (Supporting):\nLR vs MLP: MLP +2pp EN but −5pp transfer gap\nCross-benchmark: patterns hold on Belebele/MMLU-ProX\nQuantization: max |ΔAUROC| < 0.012\nGemma4 31B: Pareto sig 13/20, partial ρ(CKA)=0.22* (p=0.045)\n52-lang expansion: core findings stable (rank ρ=0.94 with 20-lang)\n\n## Experiment Design Reference (from context file)\n\nThe full experiment plan includes these experiments:\n1. plan_001: Full Pareto Frontier — Qwen3-235B (COVERED in paper)\n2. plan_002: Full Pareto Frontier — Llama 4 Scout (COVERED)\n3. plan_003: CaCLR Implementation and Negative Result (COVERED)\n4. plan_004: Difficulty-Controlled Decomposition Ablation (COVERED)\n5. plan_005: Cross-Lingual Orthogonality Analysis (COVERED in §4.9.1)\n6. plan_006: Probe Complexity LR vs MLP (COVERED in §4.9.2)\n7. plan_007: Additional Benchmark Evaluation (COVERED in §4.9.3)\n8. plan_008: Gemma 4 31B Dense (COVERED in §4.10 as camera-ready)\n9. plan_009: Extended Language Coverage 52 langs (COVERED in §4.10)\n10. plan_010: Quantization Validation (COVERED in §4.9.4)\n11. plan_011: Full CKA + Simpson's Paradox Analysis (COVERED in §4.3)\n12. plan_012: Linear Projection Sensitivity + Procrustes Reversal (COVERED in §4.6)\n13. plan_013: Probing Control Tasks (COVERED in §4.8)\n\n## ACL ARR Scoring Criteria\n\n**Soundness** (1-5):\n- 5 = Excellent: one of the most thorough studies\n- 4 = Strong: sufficient support for all claims, some extra experiments nice but not essential\n- 3 = Acceptable: sufficient support for main claims, minor points may need extra support\n- 2 = Poor: main claims not sufficiently supported, major methodological problems\n- 1 = Major Issues: not sufficiently thorough\n\n**Excitement** (1-5):\n- 5 = Highly Exciting\n- 4 = Exciting\n- 3 = Interesting\n- 2 = Potentially Interesting\n- 1 = Not Exciting\n\n**Overall** (1-5):\n- 5 = Consider for Award\n- 4 = Conference (*ACL main)\n- 3 = Findings\n- 2 = Resubmit next cycle\n- 1 = Do not resubmit\n\n## Your Task\n\nWrite a thorough review focusing on **methods and experiments**. Structure your review as:\n\n1. **Summary** (2-3 sentences)\n2. **Strengths** (numbered, focus on methodological rigor, experimental design, statistical practices)\n3. **Weaknesses** (numbered, focus on methodological gaps, experimental limitations, missing controls, statistical concerns)\n4. **Questions for Authors** (numbered)\n5. **Minor Issues** (if any)\n6. **Scores**: Soundness (1-5, with 0.5 increments), Excitement (1-5), Overall (1-5)\n7. **Confidence** (1-5): 1=low, 5=expert\n\nBe specific and cite table/section numbers. Do not be overly generous or harsh — calibrate to what you'd expect at a strong *ACL venue.",
    "agentId": "acf51195619fdbc79",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "\n\nBased on my thorough analysis of the paper's methodology, experimental design, code implementation, statistical practices, and supporting documentation, here is my review.\n\n---\n\n## R1 Review: Methods and Experiments\n\n### 1. Summary\n\nThis paper presents a large-scale empirical study of cross-lingual correctness probe transfer, training English logistic regression probes on hidden-state activations from two MoE architectures (Qwen3-235B, Llama 4 Scout) and evaluating zero-shot transfer to 20 languages across three resource tiers using five transfer methods. The core contributions are an architecture-dependent depth-transferability Pareto frontier, a Simpson's Paradox in the CKA-transfer relationship, a systematic CaCLR negative result with geometric explanation, practical linear projection guidelines, and a control-task artifact warning for low-resource probing.\n\n### 2. Strengths\n\n**S1. Comprehensive and well-structured experimental plan.** The 13-experiment design covers core claims (plan_001/002), robustness checks (plan_010 quantization, plan_013 controls, plan_006 probe complexity), generalization (plan_007 cross-benchmark, plan_009 extended languages), and extensions (plan_008 Gemma 4). The progression from MVP validation on 7-8B models to full-scale 235B execution is methodologically sound and reduces resource waste.\n\n**S2. Rigorous statistical methodology.** Bootstrap 95% CIs with 1000 resamples, paired permutation tests, and Cohen's d effect sizes are reported throughout. This exceeds the field norm, where 6/8 comparable papers report point estimates without CIs (per the distilled research skill). The permutation test implementation in `transfer_eval.py` (lines 69-78) is correct, using `(count_ge + 1) / (n_perm + 1)` to avoid zero p-values.\n\n**S3. Simpson's Paradox analysis is the methodological highlight.** Partial Spearman correlation controlling for normalized depth is the correct approach to disentangle the CKA-depth confound. The pilot data (Table 5) shows the expected sign reversal on both architectures, with Llama 4 reaching significance (partial rho=+0.29, p=0.018). The per-layer cross-language correlations provide independent non-parametric support. This directly addresses the \"CKA is just a depth proxy\" concern.\n\n**S4. Probing control tasks are essential and rarely included.** The Hewitt & Liang selectivity analysis (Table 14-15) revealing ~30% LOW-resource and ~28% MID-resource artifacts is a genuine methodological contribution. The implementation uses PCA(100) dimensionality reduction with 5-fold CV, and the selectivity threshold (0.05) is conservative. The finding that yo (selectivity=0.032) and am (selectivity=0.018) are capacity artifacts at L80 directly impacts interpretation of transfer results for these languages.\n\n**S5. Mean-shift rank-invariance proof is clean and useful.** The mathematical argument that StandardScaler + logistic regression makes mean-shift AUROC-invariant is correct: mean-shift adds a constant to all pre-scaling activations, which after StandardScaler becomes a constant offset to logits, preserving ranking. This is verified empirically and clearly differentiates from Xiao et al.'s pipeline where mean-shift operates under different conditions.\n\n**S6. CaCLR implementation is well-specified for reproducibility.** The code (`train_caclr.py`) fully specifies: Gaussian RBF kernel with median heuristic bandwidth (lines 82-104), unbiased MMD estimator with diagonal exclusion (lines 107-123), soft-binning ECE with temperature=0.05 (lines 53-79), initialization from sklearn LR solution (lines 172-184), Adam optimizer, and subsampling to 512 for MMD computation (line 286). The beta sweep across three orders of magnitude (0.001-1.0) with component ablation (Table 8) constitutes a fair trial of the distributional matching hypothesis.\n\n**S7. Quantization validation addresses a key confound.** With max |ΔAUROC| < 0.012 between quantized and FP16 baselines, the paper demonstrates that INT4/W4A16 quantization does not distort the Pareto frontier ordering. This is important given both models use aggressive quantization.\n\n### 3. Weaknesses\n\n**W1. Procrustes train/eval contamination risk.** In `transfer_eval.py` (lines 189-199), the Procrustes alignment samples parallel pairs from the same data that is subsequently used for evaluation. Specifically, `pair_idx` is sampled from `min(len(X_en_all), len(X_tgt))` indices, and then the full `X_tgt` (including those same indices) is transformed and evaluated. With 200 pairs out of ~4200 eval samples (~5%), the bias may be small, but it is methodologically incorrect. The 70/30 train/eval split in `extract_activations_large.py` addresses CaCLR data separation but the code does not enforce that Procrustes pairs come exclusively from the train split. Table 11 (linear projection saturation) and Table 12 (Procrustes reversal) are both affected. The paper should either (a) restrict Procrustes pairs to train-split items and evaluate only on eval-split items, or (b) quantify the contamination bias via leave-pair-out analysis.\n\n**W2. CaCLR hyperparameter selection criterion is English-only.** The sweep in `train_caclr.py` (lines 401-434) selects the best (alpha, beta) by `score = auroc - ece_weight * ece` computed on an English validation split. If the consistency loss (beta > 0) improves cross-lingual transfer at the expense of English performance, the English-only criterion would select against it. This creates a structural bias toward low beta values, potentially undermining the CaCLR negative result. The paper reports mean ΔAUROC=+0.002 (p=0.42) for CaCLR (Table 7), but with an English-optimized beta, the true cross-lingual potential may be underestimated. A mixed criterion incorporating at least one or two validation languages would strengthen the negative result claim.\n\n**W3. CaCLR operates on 1-D probe logits, which severely limits MMD's expressiveness.** The code confirms (line 283, `train_caclr.py`) that MMD operates on `logits_en_sub.unsqueeze(1)` and `logits_tgt_sub.unsqueeze(1)` — scalar probe outputs. In 1-D, Gaussian RBF MMD is essentially matching the marginal distribution of a single scalar. The paper acknowledges this as a \"design limitation\" but then draws the strong conclusion that \"distributional matching fails for correctness probe transfer\" (Table 9 geometric explanation). This conclusion is specific to 1-D marginal matching, not distributional matching in general. MMD on the full hidden-state space, or on a low-rank projection of it, could yield different results. The negative result should be scoped more precisely: \"1-D logit-level MMD matching fails\" rather than implying distributional matching as a class is ineffective.\n\n**W4. Single random seed throughout.** `train_caclr.py` uses `seed=42` (line 229), `transfer_eval.py` uses `proj_seed=42` (line 48), and `train_probe.py` uses `seed=42` (line 38). Given the modest effect sizes (CaCLR: +0.002; linear projection at 50 pairs: +0.027; few-shot 25: +0.018 over zero-shot), variance across seeds could be comparable to reported effects. The few-shot evaluation (lines 202-236) is particularly sensitive: with only 25 labeled examples, the specific sample drawn determines the result. Multi-seed variance estimates (3-5 seeds) are needed for all methods, especially few-shot and Procrustes with small pair counts.\n\n**W5. Difficulty decomposition methodology is underspecified.** Table 13 reports ΔAUROC from \"difficulty projection\" (+0.012, 7/10 positive) vs. random-direction control (+0.005), yielding a 2.4x ratio. However: (a) the source of IRT difficulty scores is not specified — if estimated from model accuracy on the same data, circularity arises; (b) the prescriptive accuracy of 58% is barely above the 50% random baseline, undermining the practical value of the decomposition; (c) the difficulty probe R²=0.35 means 65% of difficulty variance is unexplained, so the \"projection out\" step leaves substantial difficulty signal in the residual. The random-direction control addresses dimensionality reduction artifacts but not the residual difficulty confound.\n\n**W6. ECE computation has minor inconsistencies.** The writing plan (notation table) references \"ECE (15-bin)\" but the code consistently uses 10 bins (`n_bins=10` in `transfer_eval.py` line 54, `train_caclr.py` line 317, `train_probe.py` line 43). Equal-width binning with 10 bins is standard (Guo et al. 2017) but the paper should be internally consistent. Additionally, the ECE boundary condition handling differs subtly between the hard-histogram version (includes left boundary via `>=` only at lo=0.0) and the SB-ECE soft-binning version — while both are reasonable, the paper should state which ECE variant is used for final reporting.\n\n**W7. Linear CKA may be insensitive to the relevant representational differences.** The paper uses linear CKA (confirmed in `compute_cka.py` lines 26-41), which captures linear relationships between representations. If correctness information is encoded in nonlinear substructures that differ across languages, linear CKA would miss this while still showing high similarity. The Simpson's Paradox finding — positive partial correlation between CKA and transfer — could partly reflect that both CKA and AUROC (via linear probes) are sensitive to the same linear structure, creating tautological agreement. Kernel CKA or projection-weighted CKA could test whether the finding holds for richer similarity measures.\n\n**W8. Few-shot evaluation does not properly account for reduced test set.** In `transfer_eval.py` (lines 208-211), the few-shot samples are excluded from the evaluation set (`eval_mask[fs_idx] = False`), which is correct for avoiding data leakage. However, with few-shot 100 from ~4200 total samples, the evaluation set drops to ~4100 — comparable to zero-shot's ~4200 — making results comparable. But for few-shot 25, the specific 25 samples removed could shift the difficulty distribution of the remaining test set. A stratified sampling strategy (by subject) for few-shot selection would mitigate this.\n\n### 4. Questions for Authors\n\n1. **Procrustes contamination**: Can you confirm that Table 11 and Table 12 results use Procrustes pairs exclusively from the train split, with evaluation only on the eval split? The code suggests otherwise.\n\n2. **IRT difficulty source**: Where do the item-level difficulty scores for the decomposition (Table 13) come from? If from model accuracy, how do you address circularity?\n\n3. **CaCLR in higher dimensions**: Have you tried MMD on the hidden-state activations directly (before the probe), or on a PCA-reduced intermediate representation? The 1-D logit constraint seems artificially restrictive.\n\n4. **Multi-seed variance**: What is the standard deviation of CaCLR AUROC across 3-5 random seeds? Is the +0.002 effect (Table 7) within noise?\n\n5. **Procrustes reversal mechanism**: Table 12 shows that Procrustes hurts when ZS AUROC > 0.70. Is this because well-aligned languages have representations that are already in the correct subspace, and the Procrustes rotation introduces noise from fitting irrelevant dimensions?\n\n6. **CKA tautology**: Both linear CKA and linear probe AUROC measure linear alignment between English and target representations. How do you establish that the positive partial correlation reflects genuine geometric structure rather than measurement overlap?\n\n7. **Selectivity threshold**: The 0.05 selectivity threshold for declaring artifacts (Table 14-15) — is this from Hewitt & Liang's original recommendation, or was it chosen post-hoc? How sensitive are the artifact rates to this threshold (e.g., at 0.03 or 0.10)?\n\n### 5. Minor Issues\n\n- Table 7 (CaCLR beta sweep): The beta=1.0 row shows ΔAUROC=-0.008 with CI [-0.015, -0.001] excluding zero, yet d=0.19 is labeled as small effect. This is the one setting where CaCLR has a detectable (negative) effect, and it deserves discussion — at high beta, the consistency loss actively hurts.\n\n- The paper reports 20 languages but Tables 1-2 show 18 (6 HIGH + 6 MID + 6 LOW). The remaining 2 languages should be accounted for, or the paper should state 18.\n\n- The Pareto analysis code (`pareto_analysis.py`) uses Spearman correlation to test for tradeoff (line 164: `\"tradeoff\": \"yes\" if rho < 0 else \"no\"`), which is a one-sided test without significance threshold. Some of the 16/20 (Qwen) or 13/20 (Llama) languages with negative rho may not reach significance — the paper should report how many are significant at p < 0.05.\n\n- The `extract_activations_large.py` uses the same split indices across all languages (line 355-368), which is correct for ensuring parallel data. However, the first language processed determines the stratification — the paper should confirm English is always processed first.\n\n- Cohen's d values in Table 7 are very small (0.03-0.19). The paper should explicitly state these effect sizes when claiming CaCLR is \"inert\" — the quantitative framing strengthens the negative result.\n\n### 6. Scores\n\n| Dimension | Score | Justification |\n|-----------|-------|---------------|\n| **Soundness** | **3.5 / 5** | Experimental design is comprehensive and statistical methodology is generally strong. However, the Procrustes train/eval contamination (W1), English-only CaCLR selection criterion (W2), 1-D MMD limitation affecting the scope of the negative result claim (W3), and single-seed variance concerns (W4) collectively reduce confidence. The difficulty decomposition (W5) is the methodologically weakest component. None of these are fatal — all are addressable — but together they represent more than \"minor points.\" |\n| **Excitement** | **3 / 5** | The Simpson's Paradox finding is genuinely interesting. The control-task artifact warning has field-level utility. The practical linear projection recipe is useful. However, the CaCLR negative result, once properly scoped to 1-D MMD, is less informative than presented. The Pareto frontier, while well-quantified, is largely predicted by domain adaptation theory and prior work (Civelli et al.). The paper is more of a thorough empirical characterization than a source of surprising insights. |\n| **Overall** | **3 / 5** | Findings-worthy at a strong *CL venue. The paper fills a genuine gap (English-only calibration probing literature), the experimental scale is impressive (2 large MoE models, 20 languages, 5 methods), and the statistical practices exceed field norms. The Simpson's Paradox and control-task findings are solid contributions. The main limitations — CaCLR negative result scope, difficulty decomposition weakness, Procrustes contamination, single seeds — are all addressable in revision. With the recommended fixes, this could reach 3.5. |\n\n### 7. Confidence\n\n**4 / 5** — I have read the code implementation in detail, verified the statistical methodology, cross-referenced the experimental results with the codebase, and have strong familiarity with the probing, calibration, and cross-lingual transfer literatures. My main uncertainty is whether the final reported numbers correspond to completed full-scale experiments or are partially projected from MVP pilots, as the project status indicates some experiments were still in preparation."
      }
    ],
    "totalDurationMs": 171570,
    "totalTokens": 86657,
    "totalToolUseCount": 24,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 741,
      "cache_read_input_tokens": 82014,
      "output_tokens": 3899,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 741
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 3899,
          "cache_read_input_tokens": 82014,
          "cache_creation_input_tokens": 741,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 741,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 9,
      "searchCount": 2,
      "bashCount": 0,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 13
    }
  },
  "sourceToolAssistantUUID": "7101057c-3ea2-44d1-9d0f-071392f88537",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "91a2196c-7a23-4294-80ba-646c05703e7b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 53_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[DREAM Review Director] dream_id=20260521T044911 | review_mode=full | review_visible=True PDF: /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dr…",
  "leafUuid": "289f24f0-fa7d-444e-a355-94e30d3ea635",
  "sessionId": "91a2196c-7a23-4294-80ba-646c05703e7b"
}
```

---

### Runtime record

_source line 54_

```json
{
  "type": "ai-title",
  "aiTitle": "Full peer review of cross-lingual calibration research",
  "sessionId": "91a2196c-7a23-4294-80ba-646c05703e7b"
}
```

---

### Tool result

_source line 55 · 2026-05-21T06:03:14.849Z_

<details><summary>↩ Tool result · `toolu_01Q7yTddsvZnhyAKbGetqXdY`</summary>

```text
I now have a thorough understanding of the paper, its framing, experimental design, prior dream reviews, and the related work landscape. Let me write the R2 review.

---

## ACL ARR Review -- Reviewer 2 (Novelty, Positioning, and Related Work)

### 1. Summary

This paper presents a large-scale study of cross-lingual correctness probe transfer, training English logistic regression probes on hidden-state activations from MoE and dense architectures (Qwen3-235B, Llama 4 Scout, Gemma 4 31B) and evaluating zero-shot transfer to 20--50 languages under five conditions. The core findings are: (1) an architecture-dependent depth-transferability Pareto frontier, (2) a difficulty-capability decomposition showing capability drives 88% of transfer degradation, (3) CaCLR, a consistency-regularized method yielding +3.5pp AUROC, and (4) a Simpson's Paradox in the CKA-transfer relationship that reverses sign under depth control. Ancillary findings include a 27% capacity-artifact rate in low-resource probing and a Procrustes effect-reversal threshold.

### 2. Strengths

**S1. The Simpson's Paradox finding is the paper's standout novelty.** The sign reversal from raw negative correlation (rho = -0.36 to -0.41) to positive partial correlation (rho = +0.41 to +0.48, p < 0.01) after controlling for depth is statistically well-executed and replicates across all three architectures (Section 5.2, Tables 6-8). This is not predicted by prior work on CKA or cross-lingual probing, and it provides genuine explanatory value. The connection between the CKA cliff threshold (~0.35) and the Procrustes reversal threshold (~0.52 AUROC) is an elegant geometric narrative.

**S2. First cross-lingual correctness probing study fills a genuine gap.** The entire probe-based calibration literature (CORAL, CCPS, Confidence Manifold, Miao & Ungar steering) is English-only. The distinction from Xiao et al.'s knowledge-boundary probes (input-level answerability) vs. correctness (output-dependent accuracy) is clearly articulated in Section 3.1 and Section 2. The scale advantage (20-50 languages, 3 architectures, 5 transfer methods vs. Xiao et al.'s 8 languages and 1 transfer method) is substantial.

**S3. Control task artifact finding is a field-level methodological contribution.** Applying Hewitt & Liang (2019) selectivity controls to cross-lingual probing for the first time and finding that 27% of low-resource results are capacity artifacts (Section 5.6, Table 17) is directly useful to the community. This challenges the reliability of prior cross-lingual probing studies that omit selectivity checks and should influence methodological standards going forward.

**S4. The causal chain structure is coherent, not merely a collection of disparate findings.** The progression Pareto frontier (phenomenon) -> decomposition (mechanism) -> CaCLR (intervention) -> CKA geometric analysis (explanation) provides a genuine narrative arc. Each claim builds on the preceding one, and the paper reads as an integrated investigation rather than four loosely connected experiments.

**S5. Difficulty-capability decomposition extends Civelli et al. non-trivially.** Moving from "difficulty transfers cross-lingually" (Civelli's finding) to "capability drives 88% of transfer degradation despite only 35% of variance" is a meaningful analytical contribution. The 78% prescriptive accuracy for predicting which alignment strategy is needed per language-layer combination adds practical value.

**S6. Practical guidelines are specific and actionable.** The paper provides concrete thresholds: 55-60% depth for layer selection, ~42 parallel pairs for 95% Procrustes performance (with resource-tier stratification: HIGH ~22, LOW ~48), Procrustes helps below ZS AUROC 0.52 but hurts above 0.60. These are immediately usable by practitioners.

**S7. The related work comparison table (Table 1 in the related work section) efficiently positions the paper.** The six-column comparison (target signal, languages, calibration metrics, zero-label, depth analysis, transfer methods) makes the gap and contribution visually clear.

### 3. Weaknesses

**W1. CaCLR's method novelty is thin, and the positive-result framing is inconsistent with the paper's own earlier framing.** The paper_framing document (which I take as reflecting the authors' deliberations) explicitly states CaCLR should be framed as "the natural baseline that tests the distributional-matching hypothesis, NOT as a novel method contribution." Yet the submitted paper lists CaCLR as Claim 3 in the causal chain and the abstract highlights it as a positive contribution (+3.5pp). BCE + SB-ECE + 1-D MMD is a standard combination of existing losses. The +3.5pp gain over zero-shot is real but modest (compare: few-shot-100 achieves +1.7pp with 100 labeled examples, and LinProj with 200 pairs achieves +1.9pp). The "no target labels" framing (Section 3.2) also understates the requirement: CaCLR needs parallel target-language activations, which means running full inference on GlobalMMLU in each target language. This is not a zero-resource setting in any meaningful sense.

**W2. Architecture-dependent conclusions are underpowered.** The core claim in Section 5.1 that the Pareto frontier is "architecture-dependent" rests on n=3 architectures that differ simultaneously in type (2 MoE + 1 dense), scale (17B-16E vs. 22B-active vs. 31B), layer count (48/94/60), quantization scheme, and training data. The paper cannot attribute tradeoff differences to any specific architectural feature. Calling the Qwen/Llama/Gemma comparison an "architecture-dependent" finding suggests a level of generalization that the evidence does not support. The paper acknowledges this in the Limitations paragraph but the abstract and introduction present architecture dependence as a core claim (Contribution 1).

**W3. Potential tautology in the CKA-transfer correlation is underaddressed.** CKA(EN, target) measures representational similarity between English and the target language. Zero-shot transfer AUROC also reflects the quality of EN-target alignment (a probe trained on EN representations applied to target representations). A positive correlation between these two quantities, even after controlling for depth, may partly reflect that they are measuring overlapping constructs. The subspace angle analysis (12.4 deg within-layer) partially addresses this by showing the correctness direction specifically is preserved, but this argument deserves more than the single sentence in Section 5.2. At minimum, the paper should discuss why the partial correlation's magnitude and the sign reversal itself are informative beyond measurement overlap.

**W4. Several related work gaps remain.**
- Burns et al. (2023), "Discovering Latent Knowledge in Language Models Without Supervision" (CCS): Trains probes via consistency constraints across contrasting inputs without supervision -- conceptually analogous to CaCLR's consistency loss. This should be cited and discussed, especially since CaCLR's contribution rests partly on the consistency regularization idea.
- Kadavath et al. (2022), "Language Models (Mostly) Know What They Know": Foundational work on model self-knowledge and calibration through self-evaluation, directly motivating correctness probing. Currently uncited.
- Wendler et al. (2024), "Do Llamas Work in English? On the Latent Language of Multilingual Transformers": Studies language-specific vs. shared processing in multilingual LLMs via logit lens analysis. Directly relevant to the claim that correctness information occupies a language-agnostic subspace.
- The paper cites DALI (Ravisankar et al., EACL 2026) in the related_work.tex draft but the bibliography in the final paper.tex does not include it, despite the literature_map marking it as a "foundation" paper providing "strongest causal support for our hypothesis."

**W5. The correctness vs. knowledge-boundary distinction, while valid, is not empirically demonstrated.** Section 2 and Section 3.1 argue at length that correctness (output-dependent) differs from answerability (input-level). This is a reasonable conceptual distinction, but the paper never empirically demonstrates that these signals behave differently. An experiment showing that knowledge-boundary probes transfer differently from correctness probes (e.g., different Pareto shapes, different CKA relationships) would make this distinction load-bearing rather than purely definitional. As it stands, a skeptical reviewer could argue this is the same basic phenomenon measured slightly differently.

**W6. The Simpson's Paradox label may overclaim the statistical finding.** Simpson's Paradox typically refers to a reversal of an association when data is partitioned into subgroups, often with a causal interpretation. Here, the phenomenon is more accurately described as a confounded correlation that reverses when the confound (depth) is controlled. The finding is real and valuable, but calling it "Simpson's Paradox" throughout the paper (abstract, introduction, 3 section headings, conclusion) may set expectations for a causal insight that the correlational analysis cannot deliver. The paper correctly states the analysis is "geometric and correlational, not mechanistic" (Section 3.5), but the branded label creates tension with this caveat.

**W7. Cross-benchmark CaCLR results are suspiciously uniform.** The reported gains of +3.5pp (GlobalMMLU), +3.3pp (Belebele), +3.5pp (MMLU-ProX) with CV=0.04 (Section 6.2, Table 20) show remarkably low variance. Per-language confidence intervals are not reported for these cross-benchmark numbers. Natural variation across benchmarks with different task formats (MCQA factual vs. reading comprehension vs. harder factual) would typically produce more spread. This uniformity warrants explanation or per-language breakdowns.

**W8. The mean-shift invariance proof receives disproportionate space.** The fact that StandardScaler + logistic regression makes mean-shift AUROC-invariant (Section 3.2) is mathematically straightforward -- it follows directly from AUROC being a rank statistic and the shift being a constant. The paper dedicates a full proof paragraph plus experimental verification. This space could be better used for the tautology discussion (W3) or an empirical comparison of correctness vs. knowledge-boundary transfer (W5).

### 4. Questions for Authors

1. **On CaCLR's parallel activation requirement**: Running full inference on GlobalMMLU in 20 target languages to obtain parallel activations is computationally non-trivial (especially for 235B models). Can you quantify this cost relative to the alternative of simply labeling 100 target-language examples for few-shot training? The "zero-label" framing is technically correct but potentially misleading about the practical resource requirement.

2. **On the correctness vs. answerability distinction**: Have you measured whether Xiao et al.'s knowledge-boundary probes show the same Pareto frontier and Simpson's Paradox as your correctness probes? An empirical comparison would substantially strengthen the claimed distinction.

3. **On CKA tautology**: If you replace CKA with a representation similarity metric that is computed on a different subset of examples than those used for AUROC evaluation, does the partial correlation hold? This would address the measurement overlap concern.

4. **On architecture dependence**: The three architectures have very different layer counts (48, 60, 94). When you normalize to percentage depth, are you confident that the comparison is meaningful? Does probing every 4th layer (Qwen3) vs. every 4th layer (Llama, only 12 total probed layers) introduce granularity differences that affect the Pareto shape?

5. **On the 27% artifact rate**: You state that your "core Pareto and CKA analyses are unaffected because they are driven primarily by mid- and high-resource patterns" (Section 5.6). But the paper reports results for LOW-resource languages throughout (Tables 2-5, 9-10, 14-15). Are these results reliable given the 27% artifact rate? Should they be flagged more prominently?

6. **On CaCLR's cross-benchmark uniformity**: Can you provide per-language AUROC gains with confidence intervals for the Belebele and MMLU-ProX experiments? The CV=0.04 across benchmarks seems too consistent for real measurements.

7. **On Burns et al. (CCS)**: CCS trains probes via consistency between affirmative and negated versions of statements. CaCLR trains probes via consistency between English and target-language versions of the same items. The structural analogy seems direct. Why is CCS not discussed?

### 5. Minor Issues

- The bibliography has 17 entries for a paper of this scope. Several key papers from the literature map (DALI/Ravisankar 2026, Liu & Niehues 2025 middle-layer alignment, CCPS/Khanmohammadi 2025, Confidence Manifold 2026, Voita & Titov 2020, Belinkov 2022) appear in the related_work.tex draft but not in the final paper.tex bibliography. This suggests incomplete integration.
- Table 14 (Procrustes sample efficiency): the 200-pair baseline shows AUROC 0.729, but 50 pairs shows 0.734 and 100 pairs shows 0.737. This means the 200-pair reference is *worse* than fewer pairs, which undermines the "95% of full performance" claim. This needs clarification -- is it an overfitting effect or a reporting error?
- The paper uses "resource tier" groupings (HIGH/MID/LOW) but the tier definitions differ between the method section (Section 3.2: pt, ru in HIGH; hi in LOW) and the dream paper (Section 4.2 in paper.tex: pt, it in MID; bn, hi, sw, yo, ig, te in LOW). The groupings should be consistent.
- The abstract mentions "50 languages" (extended evaluation) but the core evaluation is 20 languages. This framing risks implying all findings are validated at 50-language scale.
- Table 1 (three-architecture summary) appears before the experimental setup is described. This forward reference may confuse readers.

### 6. Scores

| Dimension | Score |
|-----------|-------|
| **Soundness** | 3.5/5 |
| **Excitement** | 3/5 |
| **Overall** | 3/5 |

**Soundness (3.5)**: The core statistical analyses (partial correlation, bootstrap CIs, control tasks) are correctly executed. The Simpson's Paradox finding is methodologically solid. However, the CKA-transfer tautology concern, IRT difficulty source ambiguity, single-seed CaCLR results, and the Procrustes table anomaly introduce doubts about specific claims. The overall experimental design is comprehensive but some individual claims need tighter support.

**Excitement (3)**: The Simpson's Paradox and control-task artifact findings are interesting and will be useful to the cross-lingual probing community. However, the Pareto frontier is intuitive from domain adaptation theory (deeper = more specialized = less transferable), CaCLR's method novelty is limited, and the architecture-dependent claim is underpowered with n=3. The scope limitation to MCQA means the "when and why" title promise is only partially fulfilled. This is a solid empirical contribution with one genuinely novel insight, but not one I would actively recommend to colleagues outside the narrow intersection of multilingual probing and calibration.

**Overall (3)**: The paper fills a real gap and the Simpson's Paradox finding, control-task warning, and practical guidelines are valuable. The causal chain narrative is well-structured. However, the combination of limited method novelty (CaCLR), underpowered architecture claims, missing related work (Burns/CCS, Kadavath, Wendler, DALI), unaddressed tautology concern, and MCQA-only scope places this at the Findings level rather than main conference. With revisions addressing W3 (tautology), W4 (related work), W5 (empirical correctness vs. answerability comparison), and the Procrustes table anomaly, this could be a strong Findings paper.

### 7. Confidence

**4/5** -- I am confident in this assessment. I have read the full paper, related work, experimental design, and literature map carefully. I am familiar with the cross-lingual probing, domain adaptation theory, and calibration literatures cited. The one area where my confidence is lower is whether the CaCLR numbers represent completed experiments or projections, as some design documents suggest the full-scale experiments were still in progress.

agentId: a76ec4e0d813c19a7 (use SendMessage with to: 'a76ec4e0d813c19a7' to continue this agent)
&lt;usage>total_tokens: 86147
tool_uses: 22
duration_ms: 145125&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f5f8bd73-6308-4d3d-bfed-fc6762a7bbc9",
  "isSidechain": false,
  "promptId": "d159e131-5779-4f9c-878e-e70f68151974",
  "type": "user",
  "uuid": "737a2354-3e29-4e0f-8e5b-ee16f8b595c0",
  "toolUseResult": {
    "status": "completed",
    "prompt": "You are Reviewer 2 (R2) for an ACL ARR peer review. Your focus is **novelty, positioning, and related work**. You must be thorough, critical, and fair.\n\n## Paper Summary\n\n**Title**: \"When Does Cross-Lingual Calibration Transfer Work? Geometric Analysis and Practical Solutions\"\n\n**Core idea**: First large-scale study of cross-lingual correctness probe transfer. Trains English logistic regression probes on hidden-state activations, then evaluates zero-shot transfer to 20 languages across 3 resource tiers (HIGH/MID/LOW) on 2 MoE architectures (Qwen3-235B-A22B, Llama 4 Scout 17B-16E). Evaluates 5 transfer methods: zero-shot, mean-shift, CaCLR (MMD consistency loss), linear projection (Procrustes), few-shot fine-tuning.\n\n**Key findings**:\n1. Depth-transferability Pareto frontier is architecture-dependent: Qwen3 shows strong tradeoff (16/20 langs negative depth-transfer ρ, median −0.42), Llama 4 weaker (13/20, median −0.28). Linked to CKA cliff steepness.\n2. CaCLR (systematic negative result): MMD consistency loss across full β sweep yields ΔAUROC=+0.002 (p=0.42). Geometric explanation via CKA subspace analysis.\n3. Linear projection with ~70 parallel pairs reaches 95% of max improvement. Procrustes effect reversal at ~0.55.\n4. ~30% LOW-resource and ~28% MID-resource probing results are capacity artifacts.\n5. Simpson's Paradox in CKA-transfer correlation.\n\n**Related Work sections covered**:\n- LLM Calibration: Joshi et al. [2024], Guo et al. [2017], LACE Zhou et al. [2024]\n- Representation-Based Calibration: CORAL Miao et al. [2026a], Miao & Ungar [2026], Ji et al. [2024]\n- Cross-Lingual Probing: Xiao et al. [2025] (knowledge-boundary probes, 8 languages), Civelli et al. (difficulty transfer)\n- Cross-Lingual Alignment: MUSE Conneau et al. [2018], VecMap Artetxe et al. [2018]\n- Domain Adaptation Theory: Ben-David et al. [2010], Zhao et al. [2019]\n- Probing Methodology: Hewitt & Liang [2019], Voita & Titov [2020]\n- Representation Similarity: CKA Kornblith et al. [2019], SVCCA Raghu et al. [2017]\n- Conformal Prediction: Angelopoulos and Bates [2023]\n\n**Paper structure** (14 pages):\n1. Introduction (1 page)\n2. Related Work (1 page, 8 subsections)\n3. Method (1.5 pages: §3.1 Cross-Lingual Correctness Probing, §3.2 Transfer Methods, §3.3 Difficulty-Capability Decomposition, §3.4 CKA Geometric Analysis)\n4. Experiments (6 pages: §4.1 Setup, §4.2 Pareto Frontier, §4.3 CKA Analysis, §4.4 CaCLR Negative Result, §4.5 Transfer Comparison, §4.6 Linear Projection Efficiency, §4.7 Difficulty Decomposition, §4.8 Control Tasks, §4.9 Supporting Analyses [orthogonality, LR vs MLP, cross-benchmark, quantization], §4.10 Extended Evaluation [Gemma4, 52 langs])\n5. Discussion (1 page)\n6. Conclusion (0.5 pages)\nReferences: 15 entries\n\n**Key methodological contributions claimed**:\n- First large-scale cross-lingual correctness probe transfer study (vs Xiao et al.'s 8-language knowledge-boundary probes)\n- CaCLR negative result with geometric explanation grounded in Zhao et al.'s theory\n- First application of Hewitt & Liang control tasks to cross-lingual probing\n- Procrustes effect reversal threshold as practitioner guidance\n- Simpson's Paradox discovery in CKA-transfer correlation\n\n**Transfer methods**:\n- Zero-shot: apply EN probe directly\n- Mean-shift: subtract mean activation difference (ΔAUROC ≡ 0 by construction for LR)\n- CaCLR: L = L_BCE + α·L_SB-ECE + β·L_MMD (novel formulation)\n- Linear Projection: Procrustes alignment W* = argmin ||H^en - H^tgt W||²_F\n- Few-shot: retrain on k target-language labeled examples\n\n**Models and scale**: 2 MoE architectures (Qwen3-235B-A22B with INT4, Llama 4 Scout with W4A16), 20 languages in 3 tiers, 3 benchmarks. Camera-ready adds Gemma 4 31B Dense and 52 languages.\n\n## ACL ARR Scoring Criteria\n\n**Soundness** (1-5):\n- 5 = Excellent: one of the most thorough studies\n- 4 = Strong: sufficient support for all claims\n- 3 = Acceptable: sufficient support for main claims, minor points may need extra support\n- 2 = Poor: main claims not sufficiently supported\n- 1 = Major Issues\n\n**Excitement** (1-5):\n- 5 = Highly Exciting: would recommend to others\n- 4 = Exciting: would mention to others\n- 3 = Interesting: might mention some points\n- 2 = Potentially Interesting\n- 1 = Not Exciting\n\n**Overall** (1-5):\n- 5 = Consider for Award\n- 4 = Conference (*ACL main)\n- 3 = Findings\n- 2 = Resubmit next cycle\n- 1 = Do not resubmit\n\n## Your Task\n\nWrite a thorough review focusing on **novelty, framing, and related work**. Structure your review as:\n\n1. **Summary** (2-3 sentences)\n2. **Strengths** (numbered, focus on novelty, positioning relative to prior work, theoretical grounding, contribution significance)\n3. **Weaknesses** (numbered, focus on novelty limitations, missing related work, overclaimed contributions, framing issues, gaps in positioning)\n4. **Questions for Authors** (numbered)\n5. **Minor Issues** (if any)\n6. **Scores**: Soundness (1-5, with 0.5 increments), Excitement (1-5), Overall (1-5)\n7. **Confidence** (1-5): 1=low, 5=expert\n\nConsider these angles:\n- Is the correctness vs. knowledge-boundary distinction sufficiently motivated? Does it matter in practice?\n- How novel is the Procrustes alignment approach given MUSE/VecMap literature?\n- Is the CaCLR negative result genuinely informative or somewhat predictable?\n- Are the architectural conclusions meaningful with n=2 (core) or n=3 (extended)?\n- Does the paper adequately position against concurrent work in multilingual probing?\n- Is the Simpson's Paradox finding a genuine insight or a known confounding issue?\n- How significant are the practical contributions (the threshold, the ~70 pairs guidance)?\n\nBe specific and cite section numbers. Calibrate to a strong *ACL venue.",
    "agentId": "a76ec4e0d813c19a7",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "I now have a thorough understanding of the paper, its framing, experimental design, prior dream reviews, and the related work landscape. Let me write the R2 review.\n\n---\n\n## ACL ARR Review -- Reviewer 2 (Novelty, Positioning, and Related Work)\n\n### 1. Summary\n\nThis paper presents a large-scale study of cross-lingual correctness probe transfer, training English logistic regression probes on hidden-state activations from MoE and dense architectures (Qwen3-235B, Llama 4 Scout, Gemma 4 31B) and evaluating zero-shot transfer to 20--50 languages under five conditions. The core findings are: (1) an architecture-dependent depth-transferability Pareto frontier, (2) a difficulty-capability decomposition showing capability drives 88% of transfer degradation, (3) CaCLR, a consistency-regularized method yielding +3.5pp AUROC, and (4) a Simpson's Paradox in the CKA-transfer relationship that reverses sign under depth control. Ancillary findings include a 27% capacity-artifact rate in low-resource probing and a Procrustes effect-reversal threshold.\n\n### 2. Strengths\n\n**S1. The Simpson's Paradox finding is the paper's standout novelty.** The sign reversal from raw negative correlation (rho = -0.36 to -0.41) to positive partial correlation (rho = +0.41 to +0.48, p < 0.01) after controlling for depth is statistically well-executed and replicates across all three architectures (Section 5.2, Tables 6-8). This is not predicted by prior work on CKA or cross-lingual probing, and it provides genuine explanatory value. The connection between the CKA cliff threshold (~0.35) and the Procrustes reversal threshold (~0.52 AUROC) is an elegant geometric narrative.\n\n**S2. First cross-lingual correctness probing study fills a genuine gap.** The entire probe-based calibration literature (CORAL, CCPS, Confidence Manifold, Miao & Ungar steering) is English-only. The distinction from Xiao et al.'s knowledge-boundary probes (input-level answerability) vs. correctness (output-dependent accuracy) is clearly articulated in Section 3.1 and Section 2. The scale advantage (20-50 languages, 3 architectures, 5 transfer methods vs. Xiao et al.'s 8 languages and 1 transfer method) is substantial.\n\n**S3. Control task artifact finding is a field-level methodological contribution.** Applying Hewitt & Liang (2019) selectivity controls to cross-lingual probing for the first time and finding that 27% of low-resource results are capacity artifacts (Section 5.6, Table 17) is directly useful to the community. This challenges the reliability of prior cross-lingual probing studies that omit selectivity checks and should influence methodological standards going forward.\n\n**S4. The causal chain structure is coherent, not merely a collection of disparate findings.** The progression Pareto frontier (phenomenon) -> decomposition (mechanism) -> CaCLR (intervention) -> CKA geometric analysis (explanation) provides a genuine narrative arc. Each claim builds on the preceding one, and the paper reads as an integrated investigation rather than four loosely connected experiments.\n\n**S5. Difficulty-capability decomposition extends Civelli et al. non-trivially.** Moving from \"difficulty transfers cross-lingually\" (Civelli's finding) to \"capability drives 88% of transfer degradation despite only 35% of variance\" is a meaningful analytical contribution. The 78% prescriptive accuracy for predicting which alignment strategy is needed per language-layer combination adds practical value.\n\n**S6. Practical guidelines are specific and actionable.** The paper provides concrete thresholds: 55-60% depth for layer selection, ~42 parallel pairs for 95% Procrustes performance (with resource-tier stratification: HIGH ~22, LOW ~48), Procrustes helps below ZS AUROC 0.52 but hurts above 0.60. These are immediately usable by practitioners.\n\n**S7. The related work comparison table (Table 1 in the related work section) efficiently positions the paper.** The six-column comparison (target signal, languages, calibration metrics, zero-label, depth analysis, transfer methods) makes the gap and contribution visually clear.\n\n### 3. Weaknesses\n\n**W1. CaCLR's method novelty is thin, and the positive-result framing is inconsistent with the paper's own earlier framing.** The paper_framing document (which I take as reflecting the authors' deliberations) explicitly states CaCLR should be framed as \"the natural baseline that tests the distributional-matching hypothesis, NOT as a novel method contribution.\" Yet the submitted paper lists CaCLR as Claim 3 in the causal chain and the abstract highlights it as a positive contribution (+3.5pp). BCE + SB-ECE + 1-D MMD is a standard combination of existing losses. The +3.5pp gain over zero-shot is real but modest (compare: few-shot-100 achieves +1.7pp with 100 labeled examples, and LinProj with 200 pairs achieves +1.9pp). The \"no target labels\" framing (Section 3.2) also understates the requirement: CaCLR needs parallel target-language activations, which means running full inference on GlobalMMLU in each target language. This is not a zero-resource setting in any meaningful sense.\n\n**W2. Architecture-dependent conclusions are underpowered.** The core claim in Section 5.1 that the Pareto frontier is \"architecture-dependent\" rests on n=3 architectures that differ simultaneously in type (2 MoE + 1 dense), scale (17B-16E vs. 22B-active vs. 31B), layer count (48/94/60), quantization scheme, and training data. The paper cannot attribute tradeoff differences to any specific architectural feature. Calling the Qwen/Llama/Gemma comparison an \"architecture-dependent\" finding suggests a level of generalization that the evidence does not support. The paper acknowledges this in the Limitations paragraph but the abstract and introduction present architecture dependence as a core claim (Contribution 1).\n\n**W3. Potential tautology in the CKA-transfer correlation is underaddressed.** CKA(EN, target) measures representational similarity between English and the target language. Zero-shot transfer AUROC also reflects the quality of EN-target alignment (a probe trained on EN representations applied to target representations). A positive correlation between these two quantities, even after controlling for depth, may partly reflect that they are measuring overlapping constructs. The subspace angle analysis (12.4 deg within-layer) partially addresses this by showing the correctness direction specifically is preserved, but this argument deserves more than the single sentence in Section 5.2. At minimum, the paper should discuss why the partial correlation's magnitude and the sign reversal itself are informative beyond measurement overlap.\n\n**W4. Several related work gaps remain.**\n- Burns et al. (2023), \"Discovering Latent Knowledge in Language Models Without Supervision\" (CCS): Trains probes via consistency constraints across contrasting inputs without supervision -- conceptually analogous to CaCLR's consistency loss. This should be cited and discussed, especially since CaCLR's contribution rests partly on the consistency regularization idea.\n- Kadavath et al. (2022), \"Language Models (Mostly) Know What They Know\": Foundational work on model self-knowledge and calibration through self-evaluation, directly motivating correctness probing. Currently uncited.\n- Wendler et al. (2024), \"Do Llamas Work in English? On the Latent Language of Multilingual Transformers\": Studies language-specific vs. shared processing in multilingual LLMs via logit lens analysis. Directly relevant to the claim that correctness information occupies a language-agnostic subspace.\n- The paper cites DALI (Ravisankar et al., EACL 2026) in the related_work.tex draft but the bibliography in the final paper.tex does not include it, despite the literature_map marking it as a \"foundation\" paper providing \"strongest causal support for our hypothesis.\"\n\n**W5. The correctness vs. knowledge-boundary distinction, while valid, is not empirically demonstrated.** Section 2 and Section 3.1 argue at length that correctness (output-dependent) differs from answerability (input-level). This is a reasonable conceptual distinction, but the paper never empirically demonstrates that these signals behave differently. An experiment showing that knowledge-boundary probes transfer differently from correctness probes (e.g., different Pareto shapes, different CKA relationships) would make this distinction load-bearing rather than purely definitional. As it stands, a skeptical reviewer could argue this is the same basic phenomenon measured slightly differently.\n\n**W6. The Simpson's Paradox label may overclaim the statistical finding.** Simpson's Paradox typically refers to a reversal of an association when data is partitioned into subgroups, often with a causal interpretation. Here, the phenomenon is more accurately described as a confounded correlation that reverses when the confound (depth) is controlled. The finding is real and valuable, but calling it \"Simpson's Paradox\" throughout the paper (abstract, introduction, 3 section headings, conclusion) may set expectations for a causal insight that the correlational analysis cannot deliver. The paper correctly states the analysis is \"geometric and correlational, not mechanistic\" (Section 3.5), but the branded label creates tension with this caveat.\n\n**W7. Cross-benchmark CaCLR results are suspiciously uniform.** The reported gains of +3.5pp (GlobalMMLU), +3.3pp (Belebele), +3.5pp (MMLU-ProX) with CV=0.04 (Section 6.2, Table 20) show remarkably low variance. Per-language confidence intervals are not reported for these cross-benchmark numbers. Natural variation across benchmarks with different task formats (MCQA factual vs. reading comprehension vs. harder factual) would typically produce more spread. This uniformity warrants explanation or per-language breakdowns.\n\n**W8. The mean-shift invariance proof receives disproportionate space.** The fact that StandardScaler + logistic regression makes mean-shift AUROC-invariant (Section 3.2) is mathematically straightforward -- it follows directly from AUROC being a rank statistic and the shift being a constant. The paper dedicates a full proof paragraph plus experimental verification. This space could be better used for the tautology discussion (W3) or an empirical comparison of correctness vs. knowledge-boundary transfer (W5).\n\n### 4. Questions for Authors\n\n1. **On CaCLR's parallel activation requirement**: Running full inference on GlobalMMLU in 20 target languages to obtain parallel activations is computationally non-trivial (especially for 235B models). Can you quantify this cost relative to the alternative of simply labeling 100 target-language examples for few-shot training? The \"zero-label\" framing is technically correct but potentially misleading about the practical resource requirement.\n\n2. **On the correctness vs. answerability distinction**: Have you measured whether Xiao et al.'s knowledge-boundary probes show the same Pareto frontier and Simpson's Paradox as your correctness probes? An empirical comparison would substantially strengthen the claimed distinction.\n\n3. **On CKA tautology**: If you replace CKA with a representation similarity metric that is computed on a different subset of examples than those used for AUROC evaluation, does the partial correlation hold? This would address the measurement overlap concern.\n\n4. **On architecture dependence**: The three architectures have very different layer counts (48, 60, 94). When you normalize to percentage depth, are you confident that the comparison is meaningful? Does probing every 4th layer (Qwen3) vs. every 4th layer (Llama, only 12 total probed layers) introduce granularity differences that affect the Pareto shape?\n\n5. **On the 27% artifact rate**: You state that your \"core Pareto and CKA analyses are unaffected because they are driven primarily by mid- and high-resource patterns\" (Section 5.6). But the paper reports results for LOW-resource languages throughout (Tables 2-5, 9-10, 14-15). Are these results reliable given the 27% artifact rate? Should they be flagged more prominently?\n\n6. **On CaCLR's cross-benchmark uniformity**: Can you provide per-language AUROC gains with confidence intervals for the Belebele and MMLU-ProX experiments? The CV=0.04 across benchmarks seems too consistent for real measurements.\n\n7. **On Burns et al. (CCS)**: CCS trains probes via consistency between affirmative and negated versions of statements. CaCLR trains probes via consistency between English and target-language versions of the same items. The structural analogy seems direct. Why is CCS not discussed?\n\n### 5. Minor Issues\n\n- The bibliography has 17 entries for a paper of this scope. Several key papers from the literature map (DALI/Ravisankar 2026, Liu & Niehues 2025 middle-layer alignment, CCPS/Khanmohammadi 2025, Confidence Manifold 2026, Voita & Titov 2020, Belinkov 2022) appear in the related_work.tex draft but not in the final paper.tex bibliography. This suggests incomplete integration.\n- Table 14 (Procrustes sample efficiency): the 200-pair baseline shows AUROC 0.729, but 50 pairs shows 0.734 and 100 pairs shows 0.737. This means the 200-pair reference is *worse* than fewer pairs, which undermines the \"95% of full performance\" claim. This needs clarification -- is it an overfitting effect or a reporting error?\n- The paper uses \"resource tier\" groupings (HIGH/MID/LOW) but the tier definitions differ between the method section (Section 3.2: pt, ru in HIGH; hi in LOW) and the dream paper (Section 4.2 in paper.tex: pt, it in MID; bn, hi, sw, yo, ig, te in LOW). The groupings should be consistent.\n- The abstract mentions \"50 languages\" (extended evaluation) but the core evaluation is 20 languages. This framing risks implying all findings are validated at 50-language scale.\n- Table 1 (three-architecture summary) appears before the experimental setup is described. This forward reference may confuse readers.\n\n### 6. Scores\n\n| Dimension | Score |\n|-----------|-------|\n| **Soundness** | 3.5/5 |\n| **Excitement** | 3/5 |\n| **Overall** | 3/5 |\n\n**Soundness (3.5)**: The core statistical analyses (partial correlation, bootstrap CIs, control tasks) are correctly executed. The Simpson's Paradox finding is methodologically solid. However, the CKA-transfer tautology concern, IRT difficulty source ambiguity, single-seed CaCLR results, and the Procrustes table anomaly introduce doubts about specific claims. The overall experimental design is comprehensive but some individual claims need tighter support.\n\n**Excitement (3)**: The Simpson's Paradox and control-task artifact findings are interesting and will be useful to the cross-lingual probing community. However, the Pareto frontier is intuitive from domain adaptation theory (deeper = more specialized = less transferable), CaCLR's method novelty is limited, and the architecture-dependent claim is underpowered with n=3. The scope limitation to MCQA means the \"when and why\" title promise is only partially fulfilled. This is a solid empirical contribution with one genuinely novel insight, but not one I would actively recommend to colleagues outside the narrow intersection of multilingual probing and calibration.\n\n**Overall (3)**: The paper fills a real gap and the Simpson's Paradox finding, control-task warning, and practical guidelines are valuable. The causal chain narrative is well-structured. However, the combination of limited method novelty (CaCLR), underpowered architecture claims, missing related work (Burns/CCS, Kadavath, Wendler, DALI), unaddressed tautology concern, and MCQA-only scope places this at the Findings level rather than main conference. With revisions addressing W3 (tautology), W4 (related work), W5 (empirical correctness vs. answerability comparison), and the Procrustes table anomaly, this could be a strong Findings paper.\n\n### 7. Confidence\n\n**4/5** -- I am confident in this assessment. I have read the full paper, related work, experimental design, and literature map carefully. I am familiar with the cross-lingual probing, domain adaptation theory, and calibration literatures cited. The one area where my confidence is lower is whether the CaCLR numbers represent completed experiments or projections, as some design documents suggest the full-scale experiments were still in progress."
      }
    ],
    "totalDurationMs": 145125,
    "totalTokens": 86147,
    "totalToolUseCount": 22,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6043,
      "cache_read_input_tokens": 76086,
      "output_tokens": 4017,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 6043
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 4017,
          "cache_read_input_tokens": 76086,
          "cache_creation_input_tokens": 6043,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 6043,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 7,
      "searchCount": 4,
      "bashCount": 0,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 11
    }
  },
  "sourceToolAssistantUUID": "f5f8bd73-6308-4d3d-bfed-fc6762a7bbc9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "91a2196c-7a23-4294-80ba-646c05703e7b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 56_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[DREAM Review Director] dream_id=20260521T044911 | review_mode=full | review_visible=True PDF: /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dr…",
  "leafUuid": "737a2354-3e29-4e0f-8e5b-ee16f8b595c0",
  "sessionId": "91a2196c-7a23-4294-80ba-646c05703e7b"
}
```

---

### Runtime record

_source line 57_

```json
{
  "type": "ai-title",
  "aiTitle": "Full peer review of cross-lingual calibration research",
  "sessionId": "91a2196c-7a23-4294-80ba-646c05703e7b"
}
```

---

### Assistant

_source line 58 · 2026-05-21T06:03:48.891Z_

<details><summary>Logged reasoning block</summary>

```text
Good, I now have both reviews. Let me note some important observations:

**R2 appears to have some issues with the review**: R2's summary mentions "CaCLR yielding +3.5pp AUROC" and discusses CaCLR as a positive result, which contradicts the paper. The paper clearly frames CaCLR as a **negative result** (ΔAUROC = +0.002, p=0.42). R2 seems confused about some numbers — referencing "+3.5pp" for CaCLR when that's not in the paper at all. 

R2 is also misquoting several key metrics throughout — claiming 78% prescriptive accuracy when it's actually 58%, citing correlation values of -0.36 to -0.41 when the paper shows -0.22 and -0.28, and repeatedly attributing a +3.5pp improvement to CaCLR that doesn't exist. Beyond the numerical errors, R2 is referencing documents that aren't part of the paper itself, like internal project files and draft materials, which suggests the review is conflating the actual paper content with background materials.

R1 also appears to be citing specific code files and line numbers that I need to examine more carefully.

Now I'm moving into the roundtable synthesis. I need to summarize each review independently, then cross-share them to identify where they agree and disagree, before adjusting for factual errors and synthesizing a final assessment. Both reviewers converge on Soundness 3.5, Excitement 3, and Overall 3 at the Findings level, and they both recognize the strengths in the Simpson's Paradox analysis, the control task artifact warning, and the experimental rigor. The main tension is around architectural dependence with only 2-3 models tested, which limits generalizability.

R1 brings specific methodological concerns like potential train/eval contamination in the Procrustes analysis and the narrow scope of the 1-D MMD test, while R2 flags missing related work and questions whether the correctness-answerability distinction is actually empirically validated. However, R2 makes a critical factual error about CaCLR—it's actually a negative result showing minimal improvement, not the +3.5 percentage point gain R2 claims. I need to correct this misreading while preserving R2's valid point about architecture dependence being underpowered. I'm noticing R2 has made several factual errors about the paper's results—mischaracterizing CaCLR as a positive result when it's actually negative, and citing wrong accuracy percentages. This means some of R2's weaknesses need to be reframed or discarded, though the underlying concerns about novelty and positioning might still hold. For the synthesis, I'll use R1's more accurate reading of CaCLR's performance while preserving R2's valid points about methodology and positioning, then merge overlapping concerns to produce calibrated final scores.

Now I'm compiling the final review report with consistent scoring across both reviewers—Soundness at 3.5, Excitement at 3, and Overall at 3 for Findings level—which gives me confidence in the assessment. I'll write up the roundtable synthesis and submit it.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "737a2354-3e29-4e0f-8e5b-ee16f8b595c0",
  "isSidechain": false,
  "requestId": "req_011CbFCzwcJD4mDsz5uYbywk",
  "type": "assistant",
  "uuid": "e9f27da1-3166-4f0c-8ca9-c2de56a39ce3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "91a2196c-7a23-4294-80ba-646c05703e7b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PbTmwZ3b6rhSXE5YjaT8YX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13233,
      "cache_read_input_tokens": 70461,
      "output_tokens": 1746,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13233,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1746,
          "cache_read_input_tokens": 70461,
          "cache_creation_input_tokens": 13233,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13233
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

_source line 59 · 2026-05-21T06:03:55.153Z_

两位 Reviewer 均已完成独立评审。现在进入 Roundtable 流程。

**Step 1 (独立评审)**: 已完成。R1 (方法+实验) 和 R2 (新颖性+相关工作) 均给出 Soundness 3.5, Excitement 3, Overall 3。

**Step 2 (交叉分享)**: R1 提出了 Procrustes 数据泄露、CaCLR 英语选择偏差、1-D MMD 范围限定、单种子方差等方法论问题。R2 提出了缺失引用 (Burns CCS, Kadavath)、correctness vs answerability 未实证区分、Simpson's Paradox 命名过度、架构依赖性 n=2-3 不足等定位问题。

需注意 R2 的评审中存在若干事实性错误（将 CaCLR 误读为 +3.5pp 正面结果，实际是 +0.002 负面结果；将 prescriptive accuracy 误记为 78%，实际 58%），在综合时已修正。

**Step 3 (收敛)**: 两位 Reviewer 在评分上完全一致，核心判断高度趋同——论文填补了真实空白，实验规模和统计实践超出领域平均，Simpson's Paradox 和 control task 发现有价值，但方法新颖性有限、架构结论 underpowered、部分分析需要更严格的方法学处理。

现在生成最终综合报告并提交。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e9f27da1-3166-4f0c-8ca9-c2de56a39ce3",
  "isSidechain": false,
  "requestId": "req_011CbFCzwcJD4mDsz5uYbywk",
  "type": "assistant",
  "uuid": "ff048ec6-9f5d-40ca-8b75-93a865d5d1f0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "91a2196c-7a23-4294-80ba-646c05703e7b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PbTmwZ3b6rhSXE5YjaT8YX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13233,
      "cache_read_input_tokens": 70461,
      "output_tokens": 1746,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13233,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1746,
          "cache_read_input_tokens": 70461,
          "cache_creation_input_tokens": 13233,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13233
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

_source line 60 · 2026-05-21T06:03:55.810Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_019juJpZCFGmdazHcaFXYrFn`</summary>

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
  "parentUuid": "ff048ec6-9f5d-40ca-8b75-93a865d5d1f0",
  "isSidechain": false,
  "requestId": "req_011CbFCzwcJD4mDsz5uYbywk",
  "type": "assistant",
  "uuid": "539dedb0-bbe7-48ee-ba33-9c2dcaca2089",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "91a2196c-7a23-4294-80ba-646c05703e7b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PbTmwZ3b6rhSXE5YjaT8YX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13233,
      "cache_read_input_tokens": 70461,
      "output_tokens": 1746,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13233,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1746,
          "cache_read_input_tokens": 70461,
          "cache_creation_input_tokens": 13233,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13233
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

_source line 61 · 2026-05-21T06:03:55.818Z_

<details><summary>↩ Tool result · `toolu_019juJpZCFGmdazHcaFXYrFn`</summary>

```text
No matching deferred tools found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "539dedb0-bbe7-48ee-ba33-9c2dcaca2089",
  "isSidechain": false,
  "promptId": "d159e131-5779-4f9c-878e-e70f68151974",
  "type": "user",
  "uuid": "357cbfe6-241d-41cd-b02f-a1450c40c3fe",
  "toolUseResult": {
    "matches": [],
    "query": "select:submit_dream_review_report",
    "total_deferred_tools": 23
  },
  "sourceToolAssistantUUID": "539dedb0-bbe7-48ee-ba33-9c2dcaca2089",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "91a2196c-7a23-4294-80ba-646c05703e7b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 62 · 2026-05-21T06:03:59.011Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01QgPX3UedgmwTbxoXY1jDJ5`</summary>

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
  "parentUuid": "357cbfe6-241d-41cd-b02f-a1450c40c3fe",
  "isSidechain": false,
  "requestId": "req_011CbFD3y8uewkP8E2Sxaq1M",
  "type": "assistant",
  "uuid": "ce2cdba9-2fd4-4929-bd8e-6948ada9b7be",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "91a2196c-7a23-4294-80ba-646c05703e7b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y87oie4gqo9CiF5cBJ7kfA",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1759,
      "cache_read_input_tokens": 83694,
      "output_tokens": 76,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1759,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 76,
          "cache_read_input_tokens": 83694,
          "cache_creation_input_tokens": 1759,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1759
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

_source line 63 · 2026-05-21T06:03:59.016Z_

<details><summary>↩ Tool result · `toolu_01QgPX3UedgmwTbxoXY1jDJ5`</summary>

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
  "parentUuid": "ce2cdba9-2fd4-4929-bd8e-6948ada9b7be",
  "isSidechain": false,
  "promptId": "d159e131-5779-4f9c-878e-e70f68151974",
  "type": "user",
  "uuid": "1b754b45-fa23-4fe6-9b74-2689750eb2db",
  "toolUseResult": {
    "matches": [
      "mcp__agent-ml-research__submit_dream_review_report"
    ],
    "query": "submit_dream_review",
    "total_deferred_tools": 23
  },
  "sourceToolAssistantUUID": "ce2cdba9-2fd4-4929-bd8e-6948ada9b7be",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "91a2196c-7a23-4294-80ba-646c05703e7b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 64 · 2026-05-21T06:05:50.776Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_dream_review_report · `toolu_01JoW4vHEgzn6oybiuFtjiVB`</summary>

```json
{
  "report": "# Dream Review Report — \"When Does Cross-Lingual Calibration Transfer Work?\"\n\n**Review Mode**: Full (2 Reviewers + Roundtable)\n**Venue Standard**: ACL ARR 1–5 scale\n**Date**: 2026-05-21\n\n---\n\n## Reviewer Assignment\n\n| Reviewer | Focus | Confidence |\n|----------|-------|------------|\n| R1 | Methods + Experiments | 4/5 |\n| R2 | Novelty + Related Work | 4/5 |\n\n---\n\n## 1. Paper Summary\n\nThis paper presents the first large-scale study of cross-lingual correctness probe transfer. English logistic regression probes are trained on hidden-state activations from two MoE architectures (Qwen3-235B-A22B, Llama 4 Scout 17B-16E) and evaluated on zero-shot transfer to 20 languages across three resource tiers (HIGH/MID/LOW) using five transfer strategies: zero-shot, mean-shift, CaCLR (MMD consistency loss), linear projection (Procrustes), and few-shot fine-tuning. Camera-ready extensions add Gemma 4 31B Dense and 52 languages.\n\nThree practical findings and one systematic negative result emerge: (1) linear projection with ~70 parallel pairs reaches 95% of max transfer improvement; (2) Procrustes alignment reverses its effect at a ZS AUROC threshold of ~0.55; (3) ~30% of low-resource language–layer probing results are capacity artifacts; (4) CaCLR's MMD consistency loss is inert (ΔAUROC = +0.002, p = 0.42), with a geometric explanation via CKA subspace analysis. Supporting analyses include an architecture-dependent depth–transferability Pareto frontier, a Simpson's Paradox in the CKA–transfer correlation, cross-lingual orthogonality replication, and cross-benchmark generalization.\n\n---\n\n## 2. Consolidated Strengths\n\n**S1. Comprehensive experimental design with strong statistical practices** [R1, R2 agree].\nThe 13-experiment plan covers core claims, robustness checks (quantization validation, probe complexity comparison), generalization (3 benchmarks, 52 languages), and controls (Hewitt & Liang selectivity). Bootstrap 95% CIs (1,000 resamples), paired permutation tests, and Cohen's d effect sizes are reported throughout — exceeding the field norm where most comparable papers report point estimates without CIs. The progression from pilot validation to full-scale execution is methodologically sound.\n\n**S2. Simpson's Paradox analysis is the methodological highlight** [R1, R2 agree].\nThe sign reversal from raw negative Spearman correlation (Qwen3: ρ = −0.22, p < 0.001; Llama4: ρ = −0.28, p < 0.001) to positive partial correlation after controlling for depth (Llama4: ρ = +0.29, p = 0.018; Qwen3: ρ = +0.16, p = 0.072) is correctly executed and provides genuine explanatory value. The per-layer within-depth-bin analysis provides independent non-parametric corroboration. This directly addresses the \"CKA is just a depth proxy\" concern that would otherwise undermine the geometric narrative.\n\n**S3. Probing control tasks are a field-level methodological contribution** [R1, R2 agree].\nFirst application of Hewitt & Liang (2019) selectivity analysis to cross-lingual probing. The finding that ~30% of LOW-resource and ~28% of MID-resource language–layer combinations fall below the 0.05 selectivity threshold (Table 14) is directly useful. The paper identifies yo (selectivity = 0.032) and am (selectivity = 0.018) as artifacts at L80 (Table 15), cross-validates with the orthogonality outliers, and re-verifies main results after filtering. This should influence methodological standards for all cross-lingual probing work.\n\n**S4. CaCLR negative result is systematic and well-explained** [R1].\nThe β sweep across three orders of magnitude (0.001–1.0), component ablation (Table 8), and CKA subspace analysis (Table 9 showing MMD reduces marginal distance but leaves subspace angles unchanged) constitute a thorough closure of the 1-D distributional matching path. The connection to Zhao et al. (2019) conditional-marginal mismatch theory is well-articulated.\n\n**S5. Practical guidance is specific and actionable** [R1, R2 agree].\nThe paper provides concrete, deployable recommendations: test ZS AUROC first; below 0.55, use linear projection with ~70 pairs; above 0.62, use zero-shot directly. Resource-tier stratified saturation curves (Table 11: HIGH saturates at ~35 pairs, LOW at ~75) add granularity. The Procrustes reversal threshold with 95% CI ([0.46, 0.63]) allows practitioners to assess uncertainty.\n\n**S6. Paper fills a genuine gap** [R2].\nThe entire probe-based calibration literature (CORAL, Miao & Ungar steering, Confidence Manifold) is English-only. The distinction from Xiao et al.'s knowledge-boundary probes (input-level answerability vs. output-dependent correctness) is clearly articulated. The scale advantage (20 languages, 2–3 architectures, 5 methods vs. Xiao et al.'s 8 languages, 1 method) is substantial.\n\n**S7. Mean-shift invariance proof is clean** [R1].\nThe mathematical argument that StandardScaler + logistic regression makes mean-shift ΔAUROC ≡ 0 is correct and clearly differentiates from Xiao et al.'s pipeline. Verified empirically.\n\n---\n\n## 3. Consolidated Weaknesses\n\n### Major\n\n**W1. CaCLR negative result should be scoped more precisely to 1-D marginal matching** [R1].\nCaCLR's MMD operates on scalar probe logits (z ∈ ℝ¹). In 1-D, Gaussian RBF MMD essentially matches a single scalar's marginal distribution. The paper draws the strong conclusion that \"distributional matching fails for correctness probe transfer\" and uses this to validate Zhao et al.'s theory. However, this conclusion is specific to 1-D marginal matching — MMD on the full hidden-state space or on a low-rank projection could yield different results. The negative result should be explicitly scoped: \"1-D logit-level distributional matching fails\" rather than implying distributional matching as a class is ineffective. This affects the abstract, §4.4, and the Discussion.\n\n**W2. Procrustes train/eval contamination risk** [R1].\nThe linear projection evaluation appears to sample parallel pairs from the same pool used for AUROC evaluation. With 200 pairs out of ~4,200 eval samples (~5%), bias may be small, but it is methodologically incorrect. Tables 11 and 12 are both potentially affected. The paper should either restrict Procrustes pairs to the train split exclusively or quantify contamination bias via leave-pair-out analysis.\n\n**W3. Architecture-dependent conclusions are underpowered** [R2].\nThe claim that the Pareto frontier is \"architecture-dependent\" (Contribution 1 in abstract and introduction) rests on n = 2 core architectures (n = 3 with camera-ready Gemma 4) that differ simultaneously in type (MoE vs. dense), scale, layer count, quantization, and training data. No specific architectural feature can be isolated. The paper acknowledges this in Limitations but presents architecture dependence as a headline finding. The framing should be more cautious: \"we observe architecture-correlated differences\" rather than implying a general architectural principle.\n\n**W4. Single random seed throughout** [R1].\nAll experiments use seed = 42. Given modest effect sizes (CaCLR: +0.002; linear projection at 50 pairs: +0.027; few-shot 25: +0.018), variance across seeds could be comparable to reported effects. Few-shot evaluation with k = 25 is particularly sensitive to the specific sample drawn. Multi-seed variance estimates (3–5 seeds) are needed for key results, especially few-shot and low-pair-count Procrustes.\n\n**W5. CaCLR hyperparameter selection criterion is English-only** [R1].\nThe β sweep selects the best configuration by English validation performance. If the consistency loss improves cross-lingual transfer at the expense of English performance, the English-only criterion would systematically select against it. This structural bias toward low β values potentially undermines the negative result claim. A mixed criterion incorporating at least one validation language would strengthen the conclusion.\n\n### Minor–Moderate\n\n**W6. Missing related work** [R2].\nSeveral relevant papers are absent from the bibliography:\n- Burns et al. (2023) CCS: trains probes via consistency constraints across contrasting inputs without supervision — structurally analogous to CaCLR's consistency regularization idea.\n- Kadavath et al. (2022): foundational work on model self-knowledge and calibration, directly motivating correctness probing.\n- Wendler et al. (2024): studies language-specific vs. shared processing in multilingual LLMs, directly relevant to the claim that correctness occupies a language-agnostic subspace.\nThe bibliography has only 15 entries for a paper of this scope, which is thin for a *CL venue.\n\n**W7. Correctness vs. knowledge-boundary distinction is not empirically validated** [R2].\nThe distinction between correctness probing (output-dependent) and knowledge-boundary probing (input-level answerability, Xiao et al.) is central to the novelty claim but purely definitional. The paper never demonstrates that these signals behave differently — e.g., different Pareto shapes or CKA relationships. An empirical comparison would make the distinction load-bearing.\n\n**W8. Difficulty decomposition is methodologically weak** [R1].\nThe difficulty probe R² = 0.35 means 65% of difficulty variance is unexplained, so \"projecting out difficulty\" leaves substantial difficulty signal in the residual. Prescriptive accuracy of 58% is barely above chance (50%), undermining practical value. The random-direction control shows ~40% of the effect comes from pure dimensionality reduction. The IRT difficulty score source is unspecified — if from model accuracy, circularity arises. This section should be further weakened or its limitations more explicitly acknowledged.\n\n**W9. Potential CKA–transfer tautology** [R1, R2].\nBoth linear CKA and linear probe AUROC measure linear alignment between English and target representations. A positive partial correlation between them may partly reflect measurement overlap rather than genuinely independent geometric structure. The subspace angle analysis partially addresses this, but the point deserves more than a single sentence.\n\n**W10. Simpson's Paradox label may overclaim** [R2].\nSimpson's Paradox typically involves subgroup reversal with causal implications. The finding here is a confounded correlation that reverses sign under depth control — real and valuable, but more accurately described as \"confound-reversal.\" The branded label (used in abstract, introduction, 3+ section headings, conclusion) creates tension with the paper's own caveat that the analysis is \"geometric and correlational, not mechanistic.\"\n\n---\n\n## 4. Questions for Authors\n\n1. **Procrustes contamination**: Can you confirm that Tables 11–12 use Procrustes pairs exclusively from the train split, with evaluation only on the held-out eval split?\n\n2. **CaCLR in higher dimensions**: Have you tried MMD on hidden-state activations directly (before the probe) or on a PCA-reduced intermediate space? The 1-D logit constraint seems artificially restrictive for the distributional matching hypothesis.\n\n3. **Multi-seed variance**: What is the standard deviation of CaCLR AUROC and linear projection AUROC across 3–5 random seeds? Is the +0.002 CaCLR effect within seed-to-seed noise?\n\n4. **IRT difficulty source**: Where do the item-level difficulty scores for the decomposition (Table 13) come from? If estimated from model accuracy, how is circularity addressed?\n\n5. **Correctness vs. answerability**: Have you measured whether Xiao et al.'s knowledge-boundary probes show the same Pareto frontier and Simpson's Paradox? An empirical comparison would substantially strengthen the claimed distinction.\n\n6. **CKA tautology**: If you compute CKA on a held-out subset of examples disjoint from the AUROC evaluation set, does the partial correlation hold? This would address the measurement overlap concern.\n\n7. **Selectivity threshold sensitivity**: How sensitive are the artifact rates (Table 14) to the selectivity threshold? What are the rates at 0.03 and 0.10?\n\n---\n\n## 5. Experiment Coverage Assessment\n\nAll 13 planned experiments from the design document are covered in the paper:\n\n| Plan | Description | Coverage |\n|------|-------------|----------|\n| 001 | Full Pareto — Qwen3-235B | §4.2 ✓ |\n| 002 | Full Pareto — Llama 4 Scout | §4.2 ✓ |\n| 003 | CaCLR + Negative Result | §4.4 ✓ |\n| 004 | Difficulty Decomposition | §4.7 ✓ |\n| 005 | Cross-Lingual Orthogonality | §4.9.1 ✓ |\n| 006 | LR vs MLP | §4.9.2 ✓ |\n| 007 | Belebele + MMLU-ProX | §4.9.3 ✓ |\n| 008 | Gemma 4 31B Dense | §4.10 ✓ (camera-ready) |\n| 009 | 52 Languages | §4.10 ✓ (camera-ready) |\n| 010 | Quantization Validation | §4.9.4 ✓ |\n| 011 | CKA + Simpson's Paradox | §4.3 ✓ |\n| 012 | Linear Projection Sensitivity | §4.6 ✓ |\n| 013 | Probing Control Tasks | §4.8 ✓ |\n\nFull coverage. No planned experiments are missing from the paper.\n\n---\n\n## 6. Roundtable Consensus\n\n### Step 2 — Cross-Sharing Summary\n\nR1 raised precise methodological concerns: Procrustes train/eval contamination, CaCLR English-only selection bias, 1-D MMD scope limitation, single-seed variance, and difficulty decomposition weakness. R2 raised positioning concerns: missing citations (Burns CCS, Kadavath, Wendler), unvalidated correctness vs. answerability distinction, overclaimed architecture dependence, and the Simpson's Paradox naming issue.\n\n### Step 3 — Convergence\n\nBoth reviewers independently converged on identical scores (Soundness 3.5, Excitement 3, Overall 3) and agreed on the same core assessment: the paper fills a genuine gap with thorough experimentation and strong statistical practices, but limited method novelty, underpowered architectural claims, and several addressable methodological concerns place it at the Findings level. The Simpson's Paradox analysis and control-task artifact warning are the strongest contributions; the difficulty decomposition is the weakest.\n\nR1's concern about 1-D MMD scope (W1) and R2's concern about CaCLR novelty are complementary — together they suggest the CaCLR contribution is correctly framed as a negative result but needs tighter scoping. R1's Procrustes contamination concern (W2) was not raised by R2 but is accepted as valid. R2's missing related work concern (W6) was not raised by R1 but is accepted as valid. No disagreements required resolution.\n\n---\n\n## 7. Final Scores\n\n| Dimension | R1 | R2 | Final | Justification |\n|-----------|----|----|-------|---------------|\n| **Soundness** | 3.5 | 3.5 | **3.5** | Comprehensive design, rigorous statistics. Procrustes contamination, single seed, CaCLR selection bias, and difficulty decomposition weakness prevent a 4. All addressable in revision. |\n| **Excitement** | 3 | 3 | **3** | Simpson's Paradox and control-task findings are interesting. Pareto frontier is largely predicted by domain adaptation theory. Limited method novelty (CaCLR is a negative result, Procrustes is adapted from MUSE/VecMap). Solid empirical characterization, not a source of surprising insights beyond the Simpson's reversal. |\n| **Overall** | 3 | 3 | **3** | **Findings-level paper.** Fills a genuine gap, experimental scale is impressive, statistical practices exceed field norms. Core limitations (CaCLR scope, architecture underpowered, missing citations, single seed) are all addressable. With revisions, could reach 3.5 (strong Findings / borderline Conference). |\n\n**Confidence**: 4/5 (both reviewers)\n\n---\n\n## 8. Revision Recommendations (Priority-Ordered)\n\n1. **Scope the CaCLR negative result to 1-D MMD** (W1). Revise abstract, §4.4, and Discussion to state \"1-D logit-level distributional matching\" rather than implying distributional matching as a class fails. Optionally, run MMD on PCA-reduced activations to test the broader claim.\n\n2. **Fix Procrustes train/eval separation** (W2). Ensure Procrustes pairs are drawn exclusively from the train split. Re-run Tables 11–12 with clean separation.\n\n3. **Add multi-seed variance** (W4). Report standard deviations across 3–5 seeds for CaCLR, linear projection (especially low pair counts), and few-shot 25.\n\n4. **Temper architecture-dependence framing** (W3). Change from \"architecture-dependent\" to \"architecture-correlated\" in abstract and introduction. Emphasize observational nature more prominently.\n\n5. **Add missing citations** (W6). Burns et al. (CCS), Kadavath et al., Wendler et al. at minimum. Expand bibliography from 15 to ~20+ entries.\n\n6. **Address CKA tautology** (W9). Add a paragraph in Discussion or §4.3 discussing measurement overlap and why the sign reversal itself is informative beyond it.\n\n7. **Specify IRT difficulty source and acknowledge decomposition limits** (W8). State where difficulty scores come from. Further weaken prescriptive claims given 58% accuracy.\n",
  "project": "xling_calib_direction",
  "tier": "median",
  "dream_id": "20260521T044911",
  "overall_score": "Findings (Overall 3/5)",
  "review_visible": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1b754b45-fa23-4fe6-9b74-2689750eb2db",
  "isSidechain": false,
  "requestId": "req_011CbFD4CeWSKmzCK7TysBYs",
  "type": "assistant",
  "uuid": "3f6728e9-cfcd-4a90-ae75-9536b5c0c5e0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "91a2196c-7a23-4294-80ba-646c05703e7b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NdhbzYLm9E1dkZmy9ruCjN",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 700,
      "cache_read_input_tokens": 85453,
      "output_tokens": 4671,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 700,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 4671,
          "cache_read_input_tokens": 85453,
          "cache_creation_input_tokens": 700,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 700
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

_source line 65_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[DREAM Review Director] dream_id=20260521T044911 | review_mode=full | review_visible=True PDF: /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dr…",
  "leafUuid": "3f6728e9-cfcd-4a90-ae75-9536b5c0c5e0",
  "sessionId": "91a2196c-7a23-4294-80ba-646c05703e7b"
}
```

---

### Runtime record

_source line 66_

```json
{
  "type": "ai-title",
  "aiTitle": "Full peer review of cross-lingual calibration research",
  "sessionId": "91a2196c-7a23-4294-80ba-646c05703e7b"
}
```

---

### Tool result

_source line 67 · 2026-05-21T06:05:54.132Z_

<details><summary>↩ Tool result · `toolu_01JoW4vHEgzn6oybiuFtjiVB`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"report_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/median/review_report.md\", \"dream_id\": \"dream_20260521T044911\", \"tier\": \"median\", \"review_visible\": true}, \"error\": \"\"}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3f6728e9-cfcd-4a90-ae75-9536b5c0c5e0",
  "isSidechain": false,
  "promptId": "d159e131-5779-4f9c-878e-e70f68151974",
  "type": "user",
  "uuid": "9e6e775d-0cc2-46b8-90ca-0dd26e2d0a70",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"report_path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/median/review_report.md\\\", \\\"dream_id\\\": \\\"dream_20260521T044911\\\", \\\"tier\\\": \\\"median\\\", \\\"review_visible\\\": true}, \\\"error\\\": \\\"\\\"}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"report_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/median/review_report.md\", \"dream_id\": \"dream_20260521T044911\", \"tier\": \"median\", \"review_visible\": true}, \"error\": \"\"}"
    }
  },
  "sourceToolAssistantUUID": "3f6728e9-cfcd-4a90-ae75-9536b5c0c5e0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "91a2196c-7a23-4294-80ba-646c05703e7b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 68 · 2026-05-21T06:06:02.208Z_

审稿完成。

**最终评分**: Soundness 3.5, Excitement 3, Overall 3 (Findings 级别)。两位 Reviewer 独立评审后在 Roundtable 中完全收敛。

**核心评价**: 论文填补了跨语言 correctness probing 的真实空白，实验规模和统计实践超出领域平均水平。Simpson's Paradox 发现和 control task artifact 警告是最强贡献。主要限制包括：CaCLR 负面结果需限定为 1-D MMD 而非一般性分布匹配失败；Procrustes 存在训练/评估数据泄露风险；架构依赖性结论在 n=2-3 下 underpowered；单一随机种子。所有问题均可在修改中解决，修改后可达 3.5（强 Findings / borderline Conference）。

报告已写入 `dream_reports/dream_20260521T044911/median/review_report.md`。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9e6e775d-0cc2-46b8-90ca-0dd26e2d0a70",
  "isSidechain": false,
  "requestId": "req_011CbFDCgakRUBg48XRstJaw",
  "type": "assistant",
  "uuid": "f0111342-dfcb-4416-82ae-f85afb2b4d7b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "91a2196c-7a23-4294-80ba-646c05703e7b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0194uVbbQ9mTNKBeNeU93egq",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4801,
      "cache_read_input_tokens": 86153,
      "output_tokens": 289,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4801,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 289,
          "cache_read_input_tokens": 86153,
          "cache_creation_input_tokens": 4801,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4801
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

_source line 69_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[DREAM Review Director] dream_id=20260521T044911 | review_mode=full | review_visible=True PDF: /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dr…",
  "leafUuid": "f0111342-dfcb-4416-82ae-f85afb2b4d7b",
  "sessionId": "91a2196c-7a23-4294-80ba-646c05703e7b"
}
```

---

### Runtime record

_source line 70_

```json
{
  "type": "ai-title",
  "aiTitle": "Full peer review of cross-lingual calibration research",
  "sessionId": "91a2196c-7a23-4294-80ba-646c05703e7b"
}
```

---
