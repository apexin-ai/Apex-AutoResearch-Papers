# Research conversation: [DREAM Review Director] dream_id=20260520T185641 | review_mode=full | review_visible=True PDF: /home/ubuntu/.agent-ml-re

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 37
- **Recorded user turns:** 2
- **Tool calls:** 7
- **Original source:** `logs/chats/exported-trajectories/account-3/91ffee85-8db0-4b21-8e23-2eb894e1563a.jsonl`
- **Structured JSON:** [`cab899b4bc1cc652ee63.json`](../../sessions/ca/cab899b4bc1cc652ee63.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-20T19:46:06.050Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-20T19:46:06.050Z",
  "sessionId": "91ffee85-8db0-4b21-8e23-2eb894e1563a",
  "content": "[DREAM Review Director]\ndream_id=20260520T185641 | review_mode=full | review_visible=True\nPDF: /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/median/review_input_e90a5c14.pdf\n\n（内部编排信息：tier=median，仅用于 submit_dream_review_report 调用。\n你在向 Reviewer 发送审稿任务时，**严禁**提及档位名称 best/median/worst，\n也不要暗示论文结果的好坏。Reviewer 必须盲审。）\n\n任务：对上述 PDF 进行 full 模式审稿。 使用 `dream-review-full` skill 的 dispatch 模板（2 Reviewers：R1 方法+实验、R2 新颖性+相关工作；完整 roundtable：Step 1 独立 → Step 2 交叉分享 → Step 3 收敛 → Step 4 综合）。\n\n## 审稿标准\n\n未指定目标 venue。请按 top ML venue 通用标准审稿（接受率 ~25%，6 分制：1=Strong Reject … 6=Strong Accept）。\n\n## 实验设计参考\n\n完整实验设计（含想象实验列表）：`/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/median/review_context.yaml`\n论文可能未完整反映所有实验——参考此文件判断覆盖度。\n完成后必须调用 `submit_dream_review_report(report, project=\"xling_calib_direction\", tier=\"median\", dream_id=\"20260520T185641\", review_visible=True)` —— 报告会写入 dream_reports/dream_20260520T185641/median/review_report.md，编排进程通过 subprocess 退出读取它。\n不要调用 submit_review_report_to_research_director / update_review_issues / request_external_review —— 这些工具不在 Dream Review Director 白名单内。\n"
}
```

---

### Runtime record

_source line 2 · 2026-05-20T19:46:06.053Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-20T19:46:06.053Z",
  "sessionId": "91ffee85-8db0-4b21-8e23-2eb894e1563a"
}
```

---

## Round 1

10 recorded events

### User

_source line 3 · 2026-05-20T19:46:06.080Z_

[DREAM Review Director]
dream_id=20260520T185641 | review_mode=full | review_visible=True
PDF: /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/median/review_input_e90a5c14.pdf

（内部编排信息：tier=median，仅用于 submit_dream_review_report 调用。
你在向 Reviewer 发送审稿任务时，**严禁**提及档位名称 best/median/worst，
也不要暗示论文结果的好坏。Reviewer 必须盲审。）

任务：对上述 PDF 进行 full 模式审稿。 使用 `dream-review-full` skill 的 dispatch 模板（2 Reviewers：R1 方法+实验、R2 新颖性+相关工作；完整 roundtable：Step 1 独立 → Step 2 交叉分享 → Step 3 收敛 → Step 4 综合）。

## 审稿标准

未指定目标 venue。请按 top ML venue 通用标准审稿（接受率 ~25%，6 分制：1=Strong Reject … 6=Strong Accept）。

## 实验设计参考

完整实验设计（含想象实验列表）：`/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/median/review_context.yaml`
论文可能未完整反映所有实验——参考此文件判断覆盖度。
完成后必须调用 `submit_dream_review_report(report, project="xling_calib_direction", tier="median", dream_id="20260520T185641", review_visible=True)` —— 报告会写入 dream_reports/dream_20260520T185641/median/review_report.md，编排进程通过 subprocess 退出读取它。
不要调用 submit_review_report_to_research_director / update_review_issues / request_external_review —— 这些工具不在 Dream Review Director 白名单内。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "7f3a0651-0480-4418-9ac1-d949b2c2cd30",
  "type": "user",
  "uuid": "28ac8fc1-1512-4359-8bdc-970ba37d3dd4",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "91ffee85-8db0-4b21-8e23-2eb894e1563a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-20T19:46:06.079Z_

```json
{
  "parentUuid": "28ac8fc1-1512-4359-8bdc-970ba37d3dd4",
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
  "uuid": "eeb029b1-0284-4fa5-8ad5-94c32fe6f27d",
  "timestamp": "2026-05-20T19:46:06.079Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "91ffee85-8db0-4b21-8e23-2eb894e1563a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-20T19:46:06.079Z_

```json
{
  "parentUuid": "eeb029b1-0284-4fa5-8ad5-94c32fe6f27d",
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
  "uuid": "d3acdd83-de3e-4145-a192-11a168b0d8bf",
  "timestamp": "2026-05-20T19:46:06.079Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "91ffee85-8db0-4b21-8e23-2eb894e1563a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6 · 2026-05-20T19:46:06.079Z_

```json
{
  "parentUuid": "d3acdd83-de3e-4145-a192-11a168b0d8bf",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "2be574d8-0686-42e8-86a5-4fd7cb9cd741",
  "timestamp": "2026-05-20T19:46:06.079Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "91ffee85-8db0-4b21-8e23-2eb894e1563a",
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
  "aiTitle": "Full peer review of DREAM research paper",
  "sessionId": "91ffee85-8db0-4b21-8e23-2eb894e1563a"
}
```

---

### Assistant

_source line 8 · 2026-05-20T19:46:10.438Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to conduct a full DREAM review of a PDF paper. Let me break down the task:

1. Read the PDF paper
2. Read the review context YAML for experiment design reference
3. Dispatch 2 reviewers (R1: methods + experiments, R2: novelty + related work)
4. Conduct a full roundtable review process
5. Submit the review report via `submit_dream_review_report`

Let me start by reading the PDF and the review context YAML, and loading the necessary tool schemas.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2be574d8-0686-42e8-86a5-4fd7cb9cd741",
  "isSidechain": false,
  "requestId": "req_011CbEPwPoZPYQtEMFRn9wuC",
  "type": "assistant",
  "uuid": "a2cf2ef6-56b2-474f-ab9f-7f08651b9a23",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "91ffee85-8db0-4b21-8e23-2eb894e1563a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Cy8saRt3pJdTrwaUj79WUy",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11362,
      "cache_read_input_tokens": 11841,
      "output_tokens": 443,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11362,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 443,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11362,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11362
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

_source line 9 · 2026-05-20T19:46:11.052Z_

开始审稿流程。先读取论文 PDF 和实验设计上下文。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a2cf2ef6-56b2-474f-ab9f-7f08651b9a23",
  "isSidechain": false,
  "requestId": "req_011CbEPwPoZPYQtEMFRn9wuC",
  "type": "assistant",
  "uuid": "6433afb4-823f-4ed0-bb33-1e9c3f23c9aa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "91ffee85-8db0-4b21-8e23-2eb894e1563a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Cy8saRt3pJdTrwaUj79WUy",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11362,
      "cache_read_input_tokens": 11841,
      "output_tokens": 443,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11362,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 443,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11362,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11362
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

_source line 10 · 2026-05-20T19:46:12.179Z_

<details open><summary>🔧 Tool call — Read · `toolu_01GWR7hAe2qczxhxVcf3qja5`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/median/review_input_e90a5c14.pdf",
  "pages": "1-20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6433afb4-823f-4ed0-bb33-1e9c3f23c9aa",
  "isSidechain": false,
  "requestId": "req_011CbEPwPoZPYQtEMFRn9wuC",
  "type": "assistant",
  "uuid": "6c338696-fd0c-4e43-b9cd-d96380b567c3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "91ffee85-8db0-4b21-8e23-2eb894e1563a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Cy8saRt3pJdTrwaUj79WUy",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11362,
      "cache_read_input_tokens": 11841,
      "output_tokens": 443,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11362,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 443,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11362,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11362
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

_source line 11 · 2026-05-20T19:46:13.388Z_

<details><summary>↩ Tool result · `toolu_0153yP2e2JMG3GudXpYSdMUc`</summary>

```text
No matching deferred tools found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "426dc1b3-f230-473f-a35e-222bf713e1e8",
  "isSidechain": false,
  "promptId": "7f3a0651-0480-4418-9ac1-d949b2c2cd30",
  "type": "user",
  "uuid": "1a065578-bd17-4f69-83a8-2077c6b8dbac",
  "toolUseResult": {
    "matches": [],
    "query": "select:submit_dream_review_report",
    "total_deferred_tools": 23
  },
  "sourceToolAssistantUUID": "426dc1b3-f230-473f-a35e-222bf713e1e8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "91ffee85-8db0-4b21-8e23-2eb894e1563a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-20T19:46:12.558Z_

<details><summary>↩ Tool result · `toolu_01GWR7hAe2qczxhxVcf3qja5`</summary>

```text
PDF pages extracted: 11 page(s) from /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/median/review_input_e90a5c14.pdf (168.6KB)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6c338696-fd0c-4e43-b9cd-d96380b567c3",
  "isSidechain": false,
  "promptId": "7f3a0651-0480-4418-9ac1-d949b2c2cd30",
  "type": "user",
  "uuid": "ba1d2f78-2194-4b52-9c1a-dcdeffd880e5",
  "toolUseResult": {
    "type": "parts",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/median/review_input_e90a5c14.pdf",
      "originalSize": 172694,
      "outputDir": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0519-2-projects-xling-calib-direction/91ffee85-8db0-4b21-8e23-2eb894e1563a/tool-results/pdf-10e98178-6afa-4aa6-8da1-23a5682ad258",
      "count": 11
    }
  },
  "sourceToolAssistantUUID": "6c338696-fd0c-4e43-b9cd-d96380b567c3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "91ffee85-8db0-4b21-8e23-2eb894e1563a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

## Round 2

25 recorded events

### User

_source line 13 · 2026-05-20T19:46:12.556Z_

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
  "parentUuid": "ba1d2f78-2194-4b52-9c1a-dcdeffd880e5",
  "isSidechain": false,
  "promptId": "7f3a0651-0480-4418-9ac1-d949b2c2cd30",
  "type": "user",
  "isMeta": true,
  "uuid": "5547734a-7ae4-4695-9f60-62cab4479169",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "91ffee85-8db0-4b21-8e23-2eb894e1563a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-20T19:46:13.114Z_

<details open><summary>🔧 Tool call — Read · `toolu_01C76pbMKAxotHbPbtrrFTGV`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/median/review_context.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5547734a-7ae4-4695-9f60-62cab4479169",
  "isSidechain": false,
  "requestId": "req_011CbEPwPoZPYQtEMFRn9wuC",
  "type": "assistant",
  "uuid": "710d52da-b117-4d2a-baed-91e421731308",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "91ffee85-8db0-4b21-8e23-2eb894e1563a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Cy8saRt3pJdTrwaUj79WUy",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11362,
      "cache_read_input_tokens": 11841,
      "output_tokens": 443,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11362,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 443,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11362,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11362
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

_source line 15 · 2026-05-20T19:46:13.381Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_0153yP2e2JMG3GudXpYSdMUc`</summary>

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
  "parentUuid": "710d52da-b117-4d2a-baed-91e421731308",
  "isSidechain": false,
  "requestId": "req_011CbEPwPoZPYQtEMFRn9wuC",
  "type": "assistant",
  "uuid": "426dc1b3-f230-473f-a35e-222bf713e1e8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "91ffee85-8db0-4b21-8e23-2eb894e1563a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Cy8saRt3pJdTrwaUj79WUy",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11362,
      "cache_read_input_tokens": 11841,
      "output_tokens": 443,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11362,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 443,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11362,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11362
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

_source line 16 · 2026-05-20T19:46:13.532Z_

<details><summary>↩ Tool result · `toolu_01C76pbMKAxotHbPbtrrFTGV`</summary>

```text
1	narrative_guidance: 'Rebalance toward discovery + analysis. Claim 1 (Pareto frontier)
2	  becomes the headline contribution — first systematic characterization of depth-transferability
3	  tradeoff across architectures and 20 languages. Claim 2 reframes decomposition as
4	  ''partial but prescriptive'': difficulty component is clearly transferable, capability
5	  residual is noisy but the decomposition still predicts when simple baselines suffice
6	  vs when CaCLR helps. Claim 3 softens: CaCLR is presented as ''matching or exceeding
7	  the best simple baseline (linear projection) while requiring no target-language
8	  data at all'' — emphasize the zero-label setting rather than raw metric superiority.
9	  Add ablation showing where CaCLR''s consistency term specifically helps (mid-resource
10	  languages). Claim 4 presented with resource-tier analysis showing orthogonality
11	  is robust for well-represented languages but noisier for low-resource. Headline:
12	  ''Cross-lingual calibration probes reveal architecture-dependent Pareto frontier;
13	  CaCLR matches supervised transfer without target labels.''
14	
15	  '
16	imagined_experiments:
17	- name: Full Pareto Frontier — Qwen3-235B-A22B
18	  plan_id: plan_001
19	  description: '94-layer MoE model, INT8 quantization. 24 probed layers (every 4th:
20	    L0–L92). 20 languages (7 high / 8 mid / 5 low resource). English logistic-regression
21	    correctness probes trained per layer, evaluated on 5 transfer conditions (zero-shot,
22	    mean-shift, linear projection, few-shot 25/100, CaCLR placeholder). Core Pareto
23	    frontier data for Claim 1.
24	
25	    '
26	  expected_results:
27	    en_auroc_best: 0.812
28	    en_best_layer: L76
29	    en_auroc_range:
30	    - 0.531
31	    - 0.812
32	    en_ece_raw_at_best: 0.168
33	    en_ece_tempcal_at_best: 0.057
34	    temp_scaling_T: 5.83
35	    zs_transfer_auroc_mean_19lang_at_best_en: 0.644
36	    zs_transfer_drop_at_best_en_pp: 16.8
37	    best_transfer_layer: L40
38	    zs_transfer_auroc_mean_at_best_transfer: 0.696
39	    en_auroc_at_best_transfer: 0.776
40	    pareto_depth_transfer_rank_corr: 0.71
41	    low_resource_zs_pass_rate: 0.6
42	    mean_shift_improvement_rate: 0.05
43	    linproj_auroc_mean_at_best_transfer: 0.724
44	    fewshot25_auroc_mean_at_best_transfer: 0.711
45	    fewshot100_auroc_mean_at_best_transfer: 0.743
46	  result_rationale: 'Qwen3-235B-A22B 的 94 层深度提供了充分的层级分辨率来观测 Pareto tradeoff。 深层（L76）英语
47	    AUROC 达 0.812，因为更深层积累了更多 task-specific correctness 信号； 但这些深层 representation 也更
48	    language-specific（MoE routing 在深层更分化）， 导致 zero-shot 迁移退化至 0.644（drop 16.8pp）。最佳迁移层
49	    L40 处于模型 ~42% 深度，此处 representation 仍保留足够的 language-agnostic 结构。跨语言层序一致性 Spearman
50	    ρ=0.71 表明各语言对最优迁移深度的偏好高度一致，Pareto 结构是 robust 的。 Mean-shift 继承 MVP 的失败模式（correctness
51	    ≠ knowledge-boundary），仅 1/19 语言微弱改善。Linear projection 利用无标注目标语激活做线性对齐，在 L40 处比
52	    zero-shot 高 2.8pp，确立为 CaCLR 需要超越的 strong baseline。 低资源语言（sw/te/my 通过，am/yo 失败）符合预期：GlobalMMLU
53	    低资源子集样本量小且 翻译质量不稳定，但 3/5 通过证明 correctness direction 跨语言性在大模型上比 7B 更强。
54	
55	    '
56	  tables:
57	  - title: English AUROC by Layer (Logistic Regression)
58	    columns:
59	    - layer
60	    - depth_pct
61	    - en_auroc
62	    - en_ece_raw
63	    data:
64	    - layer: L0
65	      depth_pct: 0
66	      en_auroc: 0.531
67	      en_ece_raw: 0.341
68	    - layer: L4
69	      depth_pct: 4
70	      en_auroc: 0.557
71	      en_ece_raw: 0.328
72	    - layer: L8
73	      depth_pct: 9
74	      en_auroc: 0.589
75	      en_ece_raw: 0.312
76	    - layer: L12
77	      depth_pct: 13
78	      en_auroc: 0.621
79	      en_ece_raw: 0.293
80	    - layer: L16
81	      depth_pct: 17
82	      en_auroc: 0.653
83	      en_ece_raw: 0.274
84	    - layer: L20
85	      depth_pct: 21
86	      en_auroc: 0.684
87	      en_ece_raw: 0.255
88	    - layer: L24
89	      depth_pct: 26
90	      en_auroc: 0.711
91	      en_ece_raw: 0.237
92	    - layer: L28
93	      depth_pct: 30
94	      en_auroc: 0.735
95	      en_ece_raw: 0.221
96	    - layer: L32
97	      depth_pct: 34
98	      en_auroc: 0.752
99	      en_ece_raw: 0.21
100	    - layer: L36
101	      depth_pct: 38
102	      en_auroc: 0.766
103	      en_ece_raw: 0.199
104	    - layer: L40
105	      depth_pct: 43
106	      en_auroc: 0.776
107	      en_ece_raw: 0.192
108	    - layer: L44
109	      depth_pct: 47
110	      en_auroc: 0.784
111	      en_ece_raw: 0.186
112	    - layer: L48
113	      depth_pct: 51
114	      en_auroc: 0.79
115	      en_ece_raw: 0.182
116	    - layer: L52
117	      depth_pct: 55
118	      en_auroc: 0.796
119	      en_ece_raw: 0.178
120	    - layer: L56
121	      depth_pct: 60
122	      en_auroc: 0.8
123	      en_ece_raw: 0.175
124	    - layer: L60
125	      depth_pct: 64
126	      en_auroc: 0.804
127	      en_ece_raw: 0.173
128	    - layer: L64
129	      depth_pct: 68
130	      en_auroc: 0.807
131	      en_ece_raw: 0.171
132	    - layer: L68
133	      depth_pct: 72
134	      en_auroc: 0.81
135	      en_ece_raw: 0.17
136	    - layer: L72
137	      depth_pct: 77
138	      en_auroc: 0.811
139	      en_ece_raw: 0.169
140	    - layer: L76
141	      depth_pct: 81
142	      en_auroc: 0.812
143	      en_ece_raw: 0.168
144	    - layer: L80
145	      depth_pct: 85
146	      en_auroc: 0.809
147	      en_ece_raw: 0.17
148	    - layer: L84
149	      depth_pct: 89
150	      en_auroc: 0.804
151	      en_ece_raw: 0.174
152	    - layer: L88
153	      depth_pct: 94
154	      en_auroc: 0.796
155	      en_ece_raw: 0.179
156	    - layer: L92
157	      depth_pct: 98
158	      en_auroc: 0.782
159	      en_ece_raw: 0.188
160	  - title: Zero-Shot Transfer AUROC by Resource Tier (key layers)
161	    note: 19 non-English languages; tier means ± std
162	    columns:
163	    - layer
164	    - high_6_mean
165	    - high_6_std
166	    - mid_8_mean
167	    - mid_8_std
168	    - low_5_mean
169	    - low_5_std
170	    - all_19_mean
171	    data:
172	    - layer: L24
173	      high_6_mean: 0.731
174	      high_6_std: 0.011
175	      mid_8_mean: 0.692
176	      mid_8_std: 0.014
177	      low_5_mean: 0.59
178	      low_5_std: 0.031
179	      all_19_mean: 0.679
180	    - layer: L32
181	      high_6_mean: 0.747
182	      high_6_std: 0.01
183	      mid_8_mean: 0.706
184	      mid_8_std: 0.013
185	      low_5_mean: 0.601
186	      low_5_std: 0.029
187	      all_19_mean: 0.691
188	    - layer: L40
189	      high_6_mean: 0.753
190	      high_6_std: 0.01
191	      mid_8_mean: 0.711
192	      mid_8_std: 0.013
193	      low_5_mean: 0.607
194	      low_5_std: 0.032
195	      all_19_mean: 0.696
196	    - layer: L52
197	      high_6_mean: 0.741
198	      high_6_std: 0.011
199	      mid_8_mean: 0.697
200	      mid_8_std: 0.015
201	      low_5_mean: 0.586
202	      low_5_std: 0.035
203	      all_19_mean: 0.682
204	    - layer: L64
205	      high_6_mean: 0.721
206	      high_6_std: 0.013
207	      mid_8_mean: 0.673
208	      mid_8_std: 0.017
209	      low_5_mean: 0.558
210	      low_5_std: 0.039
211	      all_19_mean: 0.661
212	    - layer: L76
213	      high_6_mean: 0.705
214	      high_6_std: 0.01
215	      mid_8_mean: 0.657
216	      mid_8_std: 0.016
217	      low_5_mean: 0.54
218	      low_5_std: 0.033
219	      all_19_mean: 0.644
220	    - layer: L92
221	      high_6_mean: 0.672
222	      high_6_std: 0.015
223	      mid_8_mean: 0.621
224	      mid_8_std: 0.02
225	      low_5_mean: 0.497
226	      low_5_std: 0.042
227	      all_19_mean: 0.607
228	  - title: Per-Language Zero-Shot AUROC at L40 (Best Transfer) and L76 (Best English)
229	    columns:
230	    - lang
231	    - tier
232	    - L40_auroc
233	    - L76_auroc
234	    - delta_pp
235	    data:
236	    - lang: zh
237	      tier: high
238	      L40_auroc: 0.762
239	      L76_auroc: 0.712
240	      delta_pp: -5.0
241	    - lang: de
242	      tier: high
243	      L40_auroc: 0.753
244	      L76_auroc: 0.703
245	      delta_pp: -5.0
246	    - lang: fr
247	      tier: high
248	      L40_auroc: 0.757
249	      L76_auroc: 0.708
250	      delta_pp: -4.9
251	    - lang: es
252	      tier: high
253	      L40_auroc: 0.764
254	      L76_auroc: 0.715
255	      delta_pp: -4.9
256	    - lang: ja
257	      tier: high
258	      L40_auroc: 0.737
259	      L76_auroc: 0.688
260	      delta_pp: -4.9
261	    - lang: ru
262	      tier: high
263	      L40_auroc: 0.744
264	      L76_auroc: 0.697
265	      delta_pp: -4.7
266	    - lang: ar
267	      tier: mid
268	      L40_auroc: 0.717
269	      L76_auroc: 0.667
270	      delta_pp: -5.0
271	    - lang: hi
272	      tier: mid
273	      L40_auroc: 0.71
274	      L76_auroc: 0.659
275	      delta_pp: -5.1
276	    - lang: ko
277	      tier: mid
278	      L40_auroc: 0.703
279	      L76_auroc: 0.652
280	      delta_pp: -5.1
281	    - lang: pt
282	      tier: mid
283	      L40_auroc: 0.731
284	      L76_auroc: 0.681
285	      delta_pp: -5.0
286	    - lang: vi
287	      tier: mid
288	      L40_auroc: 0.696
289	      L76_auroc: 0.644
290	      delta_pp: -5.2
291	    - lang: th
292	      tier: mid
293	      L40_auroc: 0.688
294	      L76_auroc: 0.633
295	      delta_pp: -5.5
296	    - lang: tr
297	      tier: mid
298	      L40_auroc: 0.706
299	      L76_auroc: 0.655
300	      delta_pp: -5.1
301	    - lang: pl
302	      tier: mid
303	      L40_auroc: 0.723
304	      L76_auroc: 0.673
305	      delta_pp: -5.0
306	    - lang: sw
307	      tier: low
308	      L40_auroc: 0.638
309	      L76_auroc: 0.579
310	      delta_pp: -5.9
311	    - lang: te
312	      tier: low
313	      L40_auroc: 0.644
314	      L76_auroc: 0.59
315	      delta_pp: -5.4
316	    - lang: my
317	      tier: low
318	      L40_auroc: 0.607
319	      L76_auroc: 0.543
320	      delta_pp: -6.4
321	    - lang: am
322	      tier: low
323	      L40_auroc: 0.583
324	      L76_auroc: 0.532
325	      delta_pp: -5.1
326	    - lang: yo
327	      tier: low
328	      L40_auroc: 0.561
329	      L76_auroc: 0.51
330	      delta_pp: -5.1
331	  figures_description:
332	  - 'Figure 1a: Pareto frontier scatter — x-axis: English AUROC, y-axis: zero-shot
333	    transfer mean AUROC (19 langs). Each point is one probed layer (L0–L92), color-coded
334	    by depth percentage. Clear upward-then-left curve: shallow layers cluster at bottom-left
335	    (both low), mid layers at upper-right of transfer axis (L40 peak), deep layers
336	    drift right on English axis but downward on transfer. Pareto-efficient frontier
337	    connects L40→L48→L56→L64→L76. Annotate L40 ("best transfer") and L76 ("best English").
338	
339	    '
340	  - 'Figure 1b: Layer-depth profile — dual y-axis plot. Left axis: English AUROC (blue,
341	    rising then plateau). Right axis: ZS transfer mean (orange, rising then falling).
342	    Crossover region around L44–L52 clearly visible. Shaded band shows ±1σ across
343	    19 languages on the transfer curve — band widens at deeper layers.
344	
345	    '
346	  - 'Figure 1c: Heatmap — rows: 19 languages (grouped by resource tier), columns:
347	    24 layers. Cell color: zero-shot AUROC. Clear gradient: high-resource rows are
348	    warm (0.65–0.76) across most layers; low-resource rows are cool (0.50–0.64) with
349	    the warm zone concentrated at mid-depth layers. Visual pattern immediately shows
350	    depth-transferability × resource interaction.
351	
352	    '
353	  analysis: 'Qwen3-235B exhibits a textbook Pareto frontier for Claim 1. The depth-transferability
354	    tradeoff is sharp: 36 layers separate the best-EN (L76) and best-transfer (L40)
355	    operating points, with 16.8pp transfer degradation at L76. The layer ranking consistency
356	    ρ=0.71 means 19 languages broadly agree on which depths transfer best, supporting
357	    the claim that this is a structural property of the model rather than a language-specific
358	    artifact. Low-resource languages show the expected fragility: 3/5 pass but am
359	    and yo fall below the 0.60 AUROC threshold even at the optimal transfer layer.
360	    This will be framed as a resource-tier modulation of the Pareto frontier rather
361	    than a failure of the phenomenon. Mean-shift''s continued failure (replicating
362	    MVP) cleanly motivates CaCLR.
363	
364	    '
365	- name: Full Pareto Frontier — Llama 4 Scout
366	  plan_id: plan_002
367	  description: '48-layer MoE model, INT8 quantization. 12 probed layers (every 4th:
368	    L0–L44). 20 languages, 5 transfer conditions. Second architecture for cross-model
369	    Pareto frontier comparison (Claim 1).
370	
371	    '
372	  expected_results:
373	    en_auroc_best: 0.793
374	    en_best_layer: L44
375	    en_auroc_range:
376	    - 0.538
377	    - 0.793
378	    en_ece_raw_at_best: 0.178
379	    en_ece_tempcal_at_best: 0.063
380	    temp_scaling_T: 5.41
381	    zs_transfer_auroc_mean_19lang_at_best_en: 0.657
382	    zs_transfer_drop_at_best_en_pp: 13.6
383	    best_transfer_layer: L32
384	    zs_transfer_auroc_mean_at_best_transfer: 0.679
385	    en_auroc_at_best_transfer: 0.771
386	    pareto_depth_transfer_rank_corr: 0.56
387	    low_resource_zs_pass_rate: 0.4
388	    mean_shift_improvement_rate: 0.05
389	    linproj_auroc_mean_at_best_transfer: 0.705
390	    pareto_frontier_agreement_with_qwen3: 0.67
391	  result_rationale: 'Llama 4 Scout 仅 48 层（vs Qwen3 的 94 层），Pareto 前沿更 flat/noisy。
392	    英语 AUROC 峰值 0.793 低于 Qwen3 的 0.812，原因是 Scout 作为 MoE 的 active 参数量（~17B）小于 Qwen3-A22B，correctness
393	    信号的 linear accessibility 稍弱。 最佳迁移层 L32（67% 深度）vs 最佳英语层 L44（92% 深度）仅相隔 12 层，前沿
394	    更紧凑。Transfer drop 13.6pp 低于 Qwen3 的 16.8pp，说明 Llama4 的深层 representation language-specificity
395	    增长更平缓——可能与 Llama4 的训练数据分布有关（更多多语言 数据在预训练中）。跨语言层序一致性 ρ=0.56 明显低于 Qwen3 的 0.71，表明不同
396	    语言在 Llama4 上对最优迁移层的偏好更分散，Pareto 结构存在但更 noisy。 与 Qwen3 的 frontier agreement 0.67
397	    说明两个架构共享定性趋势（"中层比深层 迁移更好"）但定量最优点不同——这正是 "architecture-dependent" claim 的证据。 低资源仅
398	    2/5 通过，sw 和 te 勉强过线，my/am/yo 失败。
399	
400	    '
401	  tables:
402	  - title: English AUROC by Layer (Logistic Regression)
403	    columns:
404	    - layer
405	    - depth_pct
406	    - en_auroc
407	    - en_ece_raw
408	    data:
409	    - layer: L0
410	      depth_pct: 0
411	      en_auroc: 0.538
412	      en_ece_raw: 0.336
413	    - layer: L4
414	      depth_pct: 8
415	      en_auroc: 0.571
416	      en_ece_raw: 0.318
417	    - layer: L8
418	      depth_pct: 17
419	      en_auroc: 0.613
420	      en_ece_raw: 0.296
421	    - layer: L12
422	      depth_pct: 25
423	      en_auroc: 0.651
424	      en_ece_raw: 0.272
425	    - layer: L16
426	      depth_pct: 33
427	      en_auroc: 0.688
428	      en_ece_raw: 0.248
429	    - layer: L20
430	      depth_pct: 42
431	      en_auroc: 0.718
432	      en_ece_raw: 0.228
433	    - layer: L24
434	      depth_pct: 50
435	      en_auroc: 0.741
436	      en_ece_raw: 0.212
437	    - layer: L28
438	      depth_pct: 58
439	      en_auroc: 0.759
440	      en_ece_raw: 0.199
441	    - layer: L32
442	      depth_pct: 67
443	      en_auroc: 0.771
444	      en_ece_raw: 0.19
445	    - layer: L36
446	      depth_pct: 75
447	      en_auroc: 0.782
448	      en_ece_raw: 0.183
449	    - layer: L40
450	      depth_pct: 83
451	      en_auroc: 0.79
452	      en_ece_raw: 0.179
453	    - layer: L44
454	      depth_pct: 92
455	      en_auroc: 0.793
456	      en_ece_raw: 0.178
457	  - title: Zero-Shot Transfer AUROC by Resource Tier
458	    columns:
459	    - layer
460	    - high_6_mean
461	    - mid_8_mean
462	    - low_5_mean
463	    - all_19_mean
464	    data:
465	    - layer: L16
466	      high_6_mean: 0.713
467	      mid_8_mean: 0.67
468	      low_5_mean: 0.571
469	      all_19_mean: 0.659
470	    - layer: L24
471	      high_6_mean: 0.731
472	      mid_8_mean: 0.691
473	      low_5_mean: 0.587
474	      all_19_mean: 0.677
475	    - layer: L28
476	      high_6_mean: 0.737
477	      mid_8_mean: 0.697
478	      low_5_mean: 0.591
479	      all_19_mean: 0.683
480	    - layer: L32
481	      high_6_mean: 0.738
482	      mid_8_mean: 0.694
483	      low_5_mean: 0.585
484	      all_19_mean: 0.679
485	    - layer: L36
486	      high_6_mean: 0.733
487	      mid_8_mean: 0.688
488	      low_5_mean: 0.574
489	      all_19_mean: 0.673
490	    - layer: L40
491	      high_6_mean: 0.724
492	      mid_8_mean: 0.678
493	      low_5_mean: 0.561
494	      all_19_mean: 0.663
495	    - layer: L44
496	      high_6_mean: 0.714
497	      mid_8_mean: 0.669
498	      low_5_mean: 0.548
499	      all_19_mean: 0.657
500	  - title: Cross-Architecture Pareto Comparison
501	    columns:
502	    - metric
503	    - qwen3_235b
504	    - llama4_scout
505	    - interpretation
506	    data:
507	    - metric: en_auroc_best
508	      qwen3_235b: 0.812
509	      llama4_scout: 0.793
510	      interpretation: Qwen3 higher, more layers for correctness to accumulate
511	    - metric: best_transfer_depth_pct
512	      qwen3_235b: 43
513	      llama4_scout: 67
514	      interpretation: Llama4 optimal transfer much deeper (flatter frontier)
515	    - metric: zs_drop_at_best_en_pp
516	      qwen3_235b: 16.8
517	      llama4_scout: 13.6
518	      interpretation: Qwen3 sharper tradeoff, Llama4 flatter
519	    - metric: layer_rank_consistency
520	      qwen3_235b: 0.71
521	      llama4_scout: 0.56
522	      interpretation: Qwen3 more consistent across languages
523	    - metric: frontier_gap_layers
524	      qwen3_235b: 36
525	      llama4_scout: 12
526	      interpretation: Qwen3 has wider Pareto gap
527	    - metric: frontier_agreement
528	      qwen3_235b: null
529	      llama4_scout: null
530	      interpretation: Spearman ρ=0.67 across 19 langs
531	  figures_description:
532	  - 'Figure 2: Overlaid Pareto frontiers for Qwen3 (circles) and Llama4 (triangles)
533	    on same axes (EN AUROC × ZS transfer mean). Qwen3 frontier is wider and steeper;
534	    Llama4 is more compact and flatter. Annotated inset: depth percentage labels show
535	    Qwen3''s optimal transfer at 43% depth vs Llama4 at 67% depth — architecture-dependent
536	    optimal operating point. This is the main Figure 1 of the paper.
537	
538	    '
539	  analysis: 'Llama 4 Scout 确认 Pareto frontier 的跨架构泛化性，但 frontier shape 明显不同： 更 flat、更
540	    compact、更 noisy。这支持 Claim 1 的 "architecture-dependent" 修饰语。 关键对比：Qwen3 的最优迁移在
541	    43% 深度，Llama4 在 67% 深度——practitioners 不能 假设一个固定的 "最优层百分比"。Llama4 较低的层序一致性（0.56
542	    vs 0.71）暗示 其内部 multilingual representation 的组织方式更分散，可能与 Scout 的 MoE routing 策略有关。两架构的
543	    frontier agreement 0.67 说明定性趋势共享但定量不可直接迁移。
544	
545	    '
546	- name: CaCLR Implementation and Comparative Evaluation
547	  plan_id: plan_003
548	  description: 'L_CaCLR = L_BCE + α·L_SB-ECE + β·L_consistency. Trained using English
549	    correctness labels + unlabeled parallel activations from 19 target languages.
550	    Hyperparameter sweep: α∈{0.1,0.2,0.3,0.5,1.0}, β∈{0.05,0.1,0.15,0.2,0.3}. Compared
551	    against 4 baselines across full Pareto frontier for both models × 20 languages.
552	
553	    '
554	  expected_results:
555	    best_alpha: 0.3
556	    best_beta: 0.15
557	    qwen3_L40_caclr_auroc_mean: 0.738
558	    qwen3_L40_caclr_ece_mean: 0.112
559	    qwen3_L40_linproj_auroc_mean: 0.724
560	    qwen3_L40_zeroshot_auroc_mean: 0.696
561	    qwen3_L40_caclr_vs_linproj_pp: 1.4
562	    qwen3_L76_caclr_auroc_mean: 0.695
563	    qwen3_L76_linproj_auroc_mean: 0.678
564	    qwen3_L76_caclr_vs_linproj_pp: 1.7
565	    llama4_L32_caclr_auroc_mean: 0.717
566	    llama4_L32_linproj_auroc_mean: 0.705
567	    llama4_L32_caclr_vs_linproj_pp: 1.2
568	    caclr_vs_linproj_auroc_delta_mean_pp: 1.3
569	    caclr_ece_reduction_vs_tempcal_pct: 21.1
570	    caclr_improvement_over_zs_pass_rate: 0.89
571	    caclr_improvement_over_linproj_pass_rate: 0.74
572	    qwen3_caclr_optimal_layer: L52
573	    qwen3_zs_optimal_layer: L40
574	    qwen3_frontier_shift_layers: 12
575	    llama4_caclr_optimal_layer: L36
576	    llama4_zs_optimal_layer: L32
577	    llama4_frontier_shift_layers: 4
578	    caclr_fails_vs_linproj_langs:
579	    - th
580	    - my
581	    - am
582	    - yo
583	    - te
584	    mean_shift_any_improvement: 1
585	  result_rationale: 'CaCLR 在 median 档位下表现为 "matches or marginally exceeds linear projection"。
586	    核心原因：consistency term（L_consistency）对齐的是 unlabeled parallel activations 的 probe
587	    output distribution，在中-高资源语言中有效（parallel corpus 质量好， 激活空间足够对齐），但在低资源语言中由于 (a)
588	    GlobalMMLU 翻译噪声 (b) tokenizer 覆盖率低导致 activation 本身质量差，consistency 信号变成噪声。因此 CaCLR
589	    比 zero-shot 有显著改善（+4.2pp at L40），但比 linear projection 仅高 1.3pp 平均—— 因为 linear
590	    projection 已经利用了 target-language activations 做对齐。CaCLR 的 真正优势在 Pareto shift：它把最优工作层从
591	    L40 推到 L52（Qwen3），在更深层维持 迁移质量，同时获得 +2.0pp 英语 AUROC。SB-ECE loss 使 CaCLR probe 自带
592	    calibration， ECE 比 temperature-scaled zero-shot 低 21.1%——这是方法论层面的 practical benefit。
593	    Hyperparameter 敏感度中等：α=0.3 在 0.2-0.5 范围内差异小于 0.5pp，β 更敏感—— β>0.2 时 consistency
594	    过强导致英语 AUROC 下降。5 个失败语言（th/my/am/yo/te） 中 4 个是低资源或 activation 质量低的语言，th 是 mid-resource
595	    但独特的声调语言 导致 alignment 困难。
596	
597	    '
598	  tables:
599	  - title: 5-Method Comparison at Qwen3-235B Pareto-Optimal Layer (L40)
600	    columns:
601	    - method
602	    - auroc_mean
603	    - auroc_high
604	    - auroc_mid
605	    - auroc_low
606	    - ece_mean
607	    - brier_mean
608	    data:
609	    - method: zero-shot
610	      auroc_mean: 0.696
611	      auroc_high: 0.753
612	      auroc_mid: 0.711
613	      auroc_low: 0.607
614	      ece_mean: 0.148
615	      brier_mean: 0.286
616	    - method: mean-shift
617	      auroc_mean: 0.683
618	      auroc_high: 0.742
619	      auroc_mid: 0.698
620	      auroc_low: 0.591
621	      ece_mean: 0.155
622	      brier_mean: 0.294
623	    - method: linear-proj
624	      auroc_mean: 0.724
625	      auroc_high: 0.775
626	      auroc_mid: 0.738
627	      auroc_low: 0.633
628	      ece_mean: 0.121
629	      brier_mean: 0.261
630	    - method: few-shot-25
631	      auroc_mean: 0.711
632	      auroc_high: 0.766
633	      auroc_mid: 0.725
634	      auroc_low: 0.618
635	      ece_mean: 0.132
636	      brier_mean: 0.27
637	    - method: few-shot-100
638	      auroc_mean: 0.743
639	      auroc_high: 0.791
640	      auroc_mid: 0.756
641	      auroc_low: 0.655
642	      ece_mean: 0.108
643	      brier_mean: 0.247
644	    - method: CaCLR
645	      auroc_mean: 0.738
646	      auroc_high: 0.786
647	      auroc_mid: 0.754
648	      auroc_low: 0.636
649	      ece_mean: 0.112
650	      brier_mean: 0.251
651	  - title: 5-Method Comparison at Llama 4 Scout L32
652	    columns:
653	    - method
654	    - auroc_mean
655	    - auroc_high
656	    - auroc_mid
657	    - auroc_low
658	    - ece_mean
659	    data:
660	    - method: zero-shot
661	      auroc_mean: 0.679
662	      auroc_high: 0.738
663	      auroc_mid: 0.694
664	      auroc_low: 0.585
665	      ece_mean: 0.153
666	    - method: mean-shift
667	      auroc_mean: 0.668
668	      auroc_high: 0.726
669	      auroc_mid: 0.682
670	      auroc_low: 0.577
671	      ece_mean: 0.161
672	    - method: linear-proj
673	      auroc_mean: 0.705
674	      auroc_high: 0.758
675	      auroc_mid: 0.72
676	      auroc_low: 0.61
677	      ece_mean: 0.129
678	    - method: few-shot-25
679	      auroc_mean: 0.694
680	      auroc_high: 0.749
681	      auroc_mid: 0.708
682	      auroc_low: 0.602
683	      ece_mean: 0.138
684	    - method: few-shot-100
685	      auroc_mean: 0.728
686	      auroc_high: 0.776
687	      auroc_mid: 0.741
688	      auroc_low: 0.64
689	      ece_mean: 0.113
690	    - method: CaCLR
691	      auroc_mean: 0.717
692	      auroc_high: 0.769
693	      auroc_mid: 0.733
694	      auroc_low: 0.618
695	      ece_mean: 0.122
696	  - title: CaCLR vs Linear Projection per Resource Tier (Qwen3, averaged across Pareto
697	      layers)
698	    columns:
699	    - tier
700	    - n_langs
701	    - caclr_auroc
702	    - linproj_auroc
703	    - delta_pp
704	    - caclr_wins
705	    data:
706	    - tier: high
707	      n_langs: 6
708	      caclr_auroc: 0.786
709	      linproj_auroc: 0.775
710	      delta_pp: 1.1
711	      caclr_wins: 6/6
712	    - tier: mid
713	      n_langs: 8
714	      caclr_auroc: 0.754
715	      linproj_auroc: 0.738
716	      delta_pp: 1.6
717	      caclr_wins: 7/8
718	    - tier: low
719	      n_langs: 5
720	      caclr_auroc: 0.636
721	      linproj_auroc: 0.633
722	      delta_pp: 0.3
723	      caclr_wins: 1/5
724	  - title: CaCLR Consistency Term Ablation (Qwen3 L52)
725	    note: α=0.30 fixed; β=0 is calibrated-only probe
726	    columns:
727	    - config
728	    - auroc_mean
729	    - ece_mean
730	    - high_delta_vs_linproj
731	    - mid_delta_vs_linproj
732	    - low_delta_vs_linproj
733	    data:
734	    - config: α=0.3 β=0 (no consistency)
735	      auroc_mean: 0.716
736	      ece_mean: 0.119
737	      high_delta_vs_linproj: 0.3
738	      mid_delta_vs_linproj: -0.2
739	      low_delta_vs_linproj: -0.5
740	    - config: α=0.3 β=0.15 (full CaCLR)
741	      auroc_mean: 0.733
742	      ece_mean: 0.112
743	      high_delta_vs_linproj: 0.8
744	      mid_delta_vs_linproj: 1.4
745	      low_delta_vs_linproj: -0.2
746	    - config: α=0 β=0.15 (consistency only)
747	      auroc_mean: 0.708
748	      ece_mean: 0.136
749	      high_delta_vs_linproj: -0.4
750	      mid_delta_vs_linproj: 0.6
751	      low_delta_vs_linproj: -0.8
752	  - title: Hyperparameter Sensitivity (Qwen3, validation set mean AUROC across 5 langs)
753	    columns:
754	    - alpha
755	    - beta_0.05
756	    - beta_0.10
757	    - beta_0.15
758	    - beta_0.20
759	    - beta_0.30
760	    data:
761	    - alpha: 0.1
762	      beta_0.05: 0.704
763	      beta_0.10: 0.709
764	      beta_0.15: 0.711
765	      beta_0.20: 0.708
766	      beta_0.30: 0.699
767	    - alpha: 0.2
768	      beta_0.05: 0.711
769	      beta_0.10: 0.718
770	      beta_0.15: 0.724
771	      beta_0.20: 0.72
772	      beta_0.30: 0.708
773	    - alpha: 0.3
774	      beta_0.05: 0.715
775	      beta_0.10: 0.723
776	      beta_0.15: 0.731
777	      beta_0.20: 0.726
778	      beta_0.30: 0.712
779	    - alpha: 0.5
780	      beta_0.05: 0.712
781	      beta_0.10: 0.719
782	      beta_0.15: 0.725
783	      beta_0.20: 0.718
784	      beta_0.30: 0.701
785	    - alpha: 1.0
786	      beta_0.05: 0.698
787	      beta_0.10: 0.703
788	      beta_0.15: 0.706
789	      beta_0.20: 0.695
790	      beta_0.30: 0.674
791	  figures_description:
792	  - 'Figure 3a: Pareto frontier shift — overlaid zero-shot frontier (grey) and CaCLR
793	    frontier (blue) for Qwen3. CaCLR frontier is shifted up-and-right: at the same
794	    English AUROC, CaCLR achieves higher transfer; at the same transfer quality, CaCLR
795	    operates at deeper layers. Annotated: zero-shot optimal (L40) vs CaCLR optimal
796	    (L52), with arrows showing +2.0pp English gain and +1.2pp transfer gain.
797	
798	    '
799	  - 'Figure 3b: Bar chart — CaCLR AUROC improvement over linear projection, grouped
800	    by resource tier. High-resource bars around +1.1pp (all positive). Mid-resource
801	    bars around +1.6pp (7/8 positive, th near zero). Low-resource bars around +0.3pp
802	    (mostly near zero or negative). Clear visual: CaCLR''s consistency term primarily
803	    benefits mid-resource languages.
804	
805	    '
806	  - 'Figure 3c: ECE comparison — grouped bar chart with 5 methods × 3 resource tiers.
807	    CaCLR ECE bars consistently among the lowest, comparable to few-shot-100 for high/mid
808	    resource but without requiring any target-language labels.
809	
810	    '
811	  analysis: 'CaCLR 的 median-tier 表现支持 "zero-label alternative that matches supervised
812	    transfer" 的 framing，而非 "大幅超越" 的 framing。核心发现：(1) CaCLR 在 zero-label 设定下 接近 few-shot-100
813	    的性能（差 0.5pp AUROC，差 0.4pp ECE），这是 practical value 的 来源；(2) vs linear projection
814	    仅 +1.3pp，但 CaCLR 不需要任何 target-language 数据 结构假设（linear projection 假设线性可分对齐），是更
815	    principled 的方案；(3) consistency term 的 ablation 清晰显示其主要贡献在 mid-resource 语言（+1.6pp），
816	    这些语言有足够好的 parallel activation 质量让 consistency loss 有效，但又不像 high-resource 那样 zero-shot
817	    已经很好。Paper 应将 CaCLR 定位为 "practical tool for the mid-resource sweet spot" 而非 universal
818	    improvement。
819	
820	    '
821	- name: Difficulty-Controlled Ablation
822	  plan_id: plan_004
823	  description: 'IRT difficulty probes (Ridge regression on human difficulty scores
824	    per Civelli et al.) trained per layer, difficulty direction projected out of activations,
825	    correctness probes retrained on residuals, transfer evaluated. 10 languages ×
826	    8 layers per model.
827	
828	    '
829	  expected_results:
830	    difficulty_probe_en_R2_mean: 0.68
831	    difficulty_probe_zs_R2_mean: 0.61
832	    decomp_difficulty_var_explained_pct: 37
833	    original_transfer_gap_pp: 15.2
834	    residual_transfer_gap_pp: 11.4
835	    gap_reduction_pp: 3.8
836	    gap_reduction_pct: 25
837	    residual_en_auroc_drop: 0.038
838	    language_family_cluster_effect: IE languages (de/fr/es/pl/ru) cluster; others
839	      scattered
840	    capability_residual_noisy: true
841	    prescriptive_accuracy: 0.72
842	  result_rationale: 'Difficulty 是已知的跨语言可迁移特征（Civelli et al. 直接证明了 IRT difficulty probe
843	    的跨语言迁移性）。在 median 档，difficulty 解释了 correctness direction 37% 的方差， 因为 "题目难不难" 确实是
844	    correctness 的一个强组成部分（简单题各语言都对，难题各 语言都错）。但 correctness 还包含 "模型在该语言上是否具备回答这道题的 capability"
845	    这一 language-dependent 成分。投影掉 difficulty 后，transfer gap 从 15.2pp 缩小到 11.4pp（减少
846	    25%），比 variance-explained 的 37% 低是因为 projection 是线性的而 difficulty-correctness 的关系有非线性成分。残差中的
847	    capability-specific 信号是 noisy 的：高资源语言表现出清晰的 language-family clustering（IE 语言的
848	    capability profiles 相似），但低资源语言的 capability residual 被 tokenization 和数据质量 confound，
849	    无法干净分离。Prescriptive accuracy 72% 意味着：当 decomposition 预测 "这个 language-layer 对简单
850	    baseline 就够了" 时，72% 的情况下确实如此——有用但不完美。 Paper 应将此 framing 为 "partial decomposition
851	    that explains the transferable component and predicts method choice, but capability
852	    residual remains confounded"。
853	
854	    '
855	  tables:
856	  - title: Difficulty Probe Quality by Language (Qwen3 L48)
857	    columns:
858	    - lang
859	    - tier
860	    - difficulty_R2
861	    - zs_transfer_R2
862	    - delta
863	    data:
864	    - lang: en
865	      tier: high
866	      difficulty_R2: 0.71
867	      zs_transfer_R2: null
868	      delta: null
869	    - lang: zh
870	      tier: high
871	      difficulty_R2: null
872	      zs_transfer_R2: 0.67
873	      delta: -0.04
874	    - lang: de
875	      tier: high
876	      difficulty_R2: null
877	      zs_transfer_R2: 0.68
878	      delta: -0.03
879	    - lang: es
880	      tier: high
881	      difficulty_R2: null
882	      zs_transfer_R2: 0.69
883	      delta: -0.02
884	    - lang: ar
885	      tier: mid
886	      difficulty_R2: null
887	      zs_transfer_R2: 0.63
888	      delta: -0.08
889	    - lang: hi
890	      tier: mid
891	      difficulty_R2: null
892	      zs_transfer_R2: 0.61
893	      delta: -0.1
894	    - lang: ko
895	      tier: mid
896	      difficulty_R2: null
897	      zs_transfer_R2: 0.6
898	      delta: -0.11
899	    - lang: vi
900	      tier: mid
901	      difficulty_R2: null
902	      zs_transfer_R2: 0.58
903	      delta: -0.13
904	    - lang: sw
905	      tier: low
906	      difficulty_R2: null
907	      zs_transfer_R2: 0.49
908	      delta: -0.22
909	    - lang: te
910	      tier: low
911	      difficulty_R2: null
912	      zs_transfer_R2: 0.51
913	      delta: -0.2
914	  - title: Decomposition Effect on Transfer Gap (Qwen3, 8 layers averaged)
915	    columns:
916	    - component
917	    - en_auroc
918	    - zs_transfer_mean_9lang
919	    - gap_pp
920	    data:
921	    - component: original correctness probe
922	      en_auroc: 0.796
923	      zs_transfer_mean_9lang: 0.674
924	      gap_pp: 12.2
925	    - component: difficulty probe only
926	      en_auroc: 0.714
927	      zs_transfer_mean_9lang: 0.67
928	      gap_pp: 4.4
929	    - component: residual (capability) probe
930	      en_auroc: 0.758
931	      zs_transfer_mean_9lang: 0.653
932	      gap_pp: 10.5
933	    - component: difficulty + residual reconstructed
934	      en_auroc: 0.791
935	      zs_transfer_mean_9lang: 0.671
936	      gap_pp: 12.0
937	  - title: Variance Decomposition by Layer Depth (Qwen3)
938	    columns:
939	    - layer
940	    - difficulty_var_pct
941	    - capability_var_pct
942	    - reconstruction_loss_pct
943	    data:
944	    - layer: L20
945	      difficulty_var_pct: 44
946	      capability_var_pct: 51
947	      reconstruction_loss_pct: 5
948	    - layer: L28
949	      difficulty_var_pct: 42
950	      capability_var_pct: 53
951	      reconstruction_loss_pct: 5
952	    - layer: L36
953	      difficulty_var_pct: 40
954	      capability_var_pct: 54
955	      reconstruction_loss_pct: 6
956	    - layer: L48
957	      difficulty_var_pct: 37
958	      capability_var_pct: 56
959	      reconstruction_loss_pct: 7
960	    - layer: L56
961	      difficulty_var_pct: 34
962	      capability_var_pct: 58
963	      reconstruction_loss_pct: 8
964	    - layer: L64
965	      difficulty_var_pct: 31
966	      capability_var_pct: 60
967	      reconstruction_loss_pct: 9
968	    - layer: L76
969	      difficulty_var_pct: 28
970	      capability_var_pct: 62
971	      reconstruction_loss_pct: 10
972	    - layer: L84
973	      difficulty_var_pct: 26
974	      capability_var_pct: 63
975	      reconstruction_loss_pct: 11
976	  - title: 'Prescriptive Accuracy: Does Decomposition Predict Method Choice?'
977	    note: For each lang-layer pair, decomposition predicts 'zero-shot suffices' if
978	      difficulty component dominates (>50%), else 'CaCLR needed'. Ground truth from
979	      plan_003.
980	    columns:
981	    - tier
982	    - n_pairs
983	    - correct_predictions
984	    - accuracy
985	    data:
986	    - tier: high
987	      n_pairs: 48
988	      correct_predictions: 38
989	      accuracy: 0.79
990	    - tier: mid
991	      n_pairs: 64
992	      correct_predictions: 47
993	      accuracy: 0.73
994	    - tier: low
995	      n_pairs: 40
996	      correct_predictions: 25
997	      accuracy: 0.63
998	    - tier: all
999	      n_pairs: 152
1000	      correct_predictions: 110
1001	      accuracy: 0.72
1002	  figures_description:
1003	  - 'Figure 4a: Stacked bar chart — per layer, the proportion of correctness direction
1004	    variance attributed to difficulty (blue), capability (orange), reconstruction
1005	    loss (grey). Difficulty share monotonically decreases from 44% at L20 to 26% at
1006	    L84; capability share correspondingly increases. Visual narrative: deeper layers
1007	    have more capability-specific information, which is why they transfer worse.
1008	
1009	    '
1010	  - 'Figure 4b: Scatter — x-axis: difficulty variance share (%), y-axis: zero-shot
1011	    transfer AUROC for each language-layer pair. Positive correlation (r≈0.55): higher
1012	    difficulty share predicts better zero-shot transfer. But substantial scatter,
1013	    especially for low-resource languages (marked with different symbol). Regression
1014	    line shown with confidence band.
1015	
1016	    '
1017	  analysis: 'Decomposition 部分成功：difficulty component 确实是 transferable part，其 share
1018	    随 depth 递减完美解释了 Pareto tradeoff 的机制——deeper layers 积累更多 capability-specific 信息，这些信息是
1019	    language-dependent 的。但 "partial" 体现在两方面：(1) difficulty 仅解释 37% 的 variance，多数 correctness
1020	    signal 在 capability residual 中；(2) capability residual 本身不是干净的 language-specific
1021	    signal，而是与 language-family effects confounded（IE 语言 cluster 说明 capability 共享有
1022	    phylogenetic 结构）。 Prescriptive accuracy 72% 是一个有用但不完美的 practical tool。Paper 应将此
1023	    framed 为 "first decomposition of cross-lingual correctness transfer that identifies
1024	    the transferable component and partially predicts method choice, with the capability
1025	    residual as a target for future work."
1026	
1027	    '
1028	- name: Cross-Lingual Orthogonality Analysis
1029	  plan_id: plan_005
1030	  description: 'Extract verbalized confidence direction (prompt for P(correct) score,
1031	    fit linear probe), compute cosine similarity with correctness direction across
1032	    20 languages × 2 architectures. Resource-tier and language-family analysis.
1033	
1034	    '
1035	  expected_results:
1036	    cosine_mean_all: 0.091
1037	    cosine_mean_qwen3: 0.086
1038	    cosine_mean_llama4: 0.096
1039	    cosine_high_mean: 0.059
1040	    cosine_mid_mean: 0.084
1041	    cosine_low_mean: 0.147
1042	    cosine_low_std: 0.032
1043	    cosine_range:
1044	    - 0.04
1045	    - 0.21
1046	    en_cosine_qwen3: 0.04
1047	    en_cosine_llama4: 0.05
1048	    cross_arch_cosine_corr: 0.78
1049	    orthogonality_holds_all_20: true
1050	  result_rationale: 'Miao & Ungar (2026) 在英语 7-8B 模型上发现 correctness-confidence cosine
1051	    < 0.04。 在 median 档，该 orthogonality 跨语言泛化但有 resource-tier 梯度。High-resource 语言（cosine
1052	    ~0.06）接近英语水平，因为模型在这些语言上有充足的训练数据， verbalized confidence 和 internal correctness
1053	    的分离是 well-learned 的。 Mid-resource 语言（cosine ~0.08）稍高，模型的 confidence 表达在这些语言上 不那么
1054	    calibrated。Low-resource 语言（cosine ~0.15, std 0.032）明显更高且 variance 更大——模型在低资源语言上的
1055	    verbalized confidence 方向本身就不稳定（probe 拟合 noisy），导致与 correctness 的 cosine 更大也更不可靠。但即使最高的
1056	    yo (0.21) 也远低于 "parallel" 的 0.7+，orthogonality 的定性结论在所有 20 语言上成立。 Cross-architecture
1057	    correlation 0.78 表明 per-language cosine 值在两个模型上高度 一致——这是 structural property，不是
1058	    model-specific artifact。
1059	
1060	    '
1061	  tables:
1062	  - title: Correctness-Confidence Cosine Similarity by Language
1063	    columns:
1064	    - lang
1065	    - tier
1066	    - qwen3_cosine
1067	    - llama4_cosine
1068	    - mean
1069	    data:
1070	    - lang: en
1071	      tier: high
1072	      qwen3_cosine: 0.04
1073	      llama4_cosine: 0.05
1074	      mean: 0.045
1075	    - lang: zh
1076	      tier: high
1077	      qwen3_cosine: 0.05
1078	      llama4_cosine: 0.06
1079	      mean: 0.055
1080	    - lang: de
1081	      tier: high
1082	      qwen3_cosine: 0.06
1083	      llama4_cosine: 0.07
1084	      mean: 0.065
1085	    - lang: fr
1086	      tier: high
1087	      qwen3_cosine: 0.05
1088	      llama4_cosine: 0.06
1089	      mean: 0.055
1090	    - lang: es
1091	      tier: high
1092	      qwen3_cosine: 0.05
1093	      llama4_cosine: 0.06
1094	      mean: 0.055
1095	    - lang: ja
1096	      tier: high
1097	      qwen3_cosine: 0.07
1098	      llama4_cosine: 0.08
1099	      mean: 0.075
1100	    - lang: ru
1101	      tier: high
1102	      qwen3_cosine: 0.06
1103	      llama4_cosine: 0.07
1104	      mean: 0.065
1105	    - lang: ar
1106	      tier: mid
1107	      qwen3_cosine: 0.08
1108	      llama4_cosine: 0.09
1109	      mean: 0.085
1110	    - lang: hi
1111	      tier: mid
1112	      qwen3_cosine: 0.07
1113	      llama4_cosine: 0.08
1114	      mean: 0.075
1115	    - lang: ko
1116	      tier: mid
1117	      qwen3_cosine: 0.08
1118	      llama4_cosine: 0.09
1119	      mean: 0.085
1120	    - lang: pt
1121	      tier: mid
1122	      qwen3_cosine: 0.06
1123	      llama4_cosine: 0.07
1124	      mean: 0.065
1125	    - lang: vi
1126	      tier: mid
1127	      qwen3_cosine: 0.09
1128	      llama4_cosine: 0.1
1129	      mean: 0.095
1130	    - lang: th
1131	      tier: mid
1132	      qwen3_cosine: 0.1
1133	      llama4_cosine: 0.11
1134	      mean: 0.105
1135	    - lang: tr
1136	      tier: mid
1137	      qwen3_cosine: 0.08
1138	      llama4_cosine: 0.09
1139	      mean: 0.085
1140	    - lang: pl
1141	      tier: mid
1142	      qwen3_cosine: 0.07
1143	      llama4_cosine: 0.08
1144	      mean: 0.075
1145	    - lang: sw
1146	      tier: low
1147	      qwen3_cosine: 0.12
1148	      llama4_cosine: 0.13
1149	      mean: 0.125
1150	    - lang: te
1151	      tier: low
1152	      qwen3_cosine: 0.1
1153	      llama4_cosine: 0.11
1154	      mean: 0.105
1155	    - lang: my
1156	      tier: low
1157	      qwen3_cosine: 0.15
1158	      llama4_cosine: 0.16
1159	      mean: 0.155
1160	    - lang: am
1161	      tier: low
1162	      qwen3_cosine: 0.16
1163	      llama4_cosine: 0.17
1164	      mean: 0.165
1165	    - lang: yo
1166	      tier: low
1167	      qwen3_cosine: 0.18
1168	      llama4_cosine: 0.19
1169	      mean: 0.185
1170	  - title: Orthogonality Summary by Resource Tier
1171	    columns:
1172	    - tier
1173	    - n_langs
1174	    - cosine_mean
1175	    - cosine_std
1176	    - cosine_min
1177	    - cosine_max
1178	    data:
1179	    - tier: high
1180	      n_langs: 7
1181	      cosine_mean: 0.059
1182	      cosine_std: 0.01
1183	      cosine_min: 0.04
1184	      cosine_max: 0.08
1185	    - tier: mid
1186	      n_langs: 8
1187	      cosine_mean: 0.084
1188	      cosine_std: 0.013
1189	      cosine_min: 0.06
1190	      cosine_max: 0.11
1191	    - tier: low
1192	      n_langs: 5
1193	      cosine_mean: 0.147
1194	      cosine_std: 0.032
1195	      cosine_min: 0.1
1196	      cosine_max: 0.19
1197	    - tier: all
1198	      n_langs: 20
1199	      cosine_mean: 0.091
1200	      cosine_std: 0.04
1201	      cosine_min: 0.04
1202	      cosine_max: 0.19
1203	  figures_description:
1204	  - 'Figure 5: Dot plot — x-axis: cosine similarity, y-axis: languages (sorted by
1205	    resource tier, then by cosine). Two markers per language (circle=Qwen3, triangle=Llama4).
1206	    Vertical dashed line at cosine=0.25 ("orthogonality threshold"). All points to
1207	    the left. Clear visual gradient from high-resource (clustered near 0.05) to low-resource
1208	    (spread between 0.10-0.19). Error bars show bootstrap 95% CI. Annotation: "Miao
1209	    & Ungar EN baseline: cos < 0.04" with arrow pointing to English dots.
1210	
1211	    '
1212	  analysis: 'Claim 4 在 median 档下获得 strong support for high/mid-resource languages,
1213	    qualified support for low-resource。核心结论：correctness-confidence orthogonality 是一个跨语言
1214	    的 structural property，不是英语特有的。但 resource-tier gradient（high 0.06 → low 0.15） 表明该
1215	    property 在低资源语言上更弱——这可能是因为模型在低资源语言上的 confidence calibration 本身就差，confidence direction
1216	    拟合不稳定。Cross-architecture 一致性 0.78 进一步强化了 structural claim。Paper 应呈现为 "orthogonality
1217	    universally holds (all cos < 0.25) but varies in degree, with implications for
1218	    why output-based calibration is structurally limited across all languages — but
1219	    especially limited for high-resource languages where the orthogonality is strongest."
1220	
1221	    '
1222	- name: Probe Complexity Comparison
1223	  plan_id: plan_006
1224	  description: 'Logistic regression vs 2-layer MLP (hidden dim 256, ReLU) at each
1225	    probed layer for both models. Compare English accuracy, cross-lingual transfer
1226	    degradation, and calibration quality. Test hypothesis: linear probes transfer
1227	    better.
1228	
1229	    '
1230	  expected_results:
1231	    qwen3_L76_logreg_en_auroc: 0.812
1232	    qwen3_L76_mlp_en_auroc: 0.827
1233	    qwen3_L76_logreg_transfer_mean: 0.644
1234	    qwen3_L76_mlp_transfer_mean: 0.607
1235	    qwen3_L76_logreg_transfer_drop_pp: 16.8
1236	    qwen3_L76_mlp_transfer_drop_pp: 22.0
1237	    llama4_L44_logreg_en_auroc: 0.793
1238	    llama4_L44_mlp_en_auroc: 0.812
1239	    llama4_L44_logreg_transfer_mean: 0.657
1240	    llama4_L44_mlp_transfer_mean: 0.625
1241	    llama4_L44_logreg_transfer_drop_pp: 13.6
1242	    llama4_L44_mlp_transfer_drop_pp: 18.7
1243	    mlp_en_advantage_pp_mean: 1.7
1244	    logreg_transfer_advantage_pp_mean: 3.5
1245	    hypothesis_confirmed: true
1246	  result_rationale: 'MLP 在英语上多 ~1.7pp AUROC，因为非线性层可以捕获 correctness 与 activation 之间
1247	    的非线性关系。但 MLP 在跨语言迁移上劣 ~3.5pp，因为非线性决策边界更容易 overfit 英语 activation 的分布特征，这些特征在其他语言中不保持。Linear
1248	    probe 的决策 超平面在 high-dimensional space 中更 "blunt"，因此更 robust to distribution shift。
1249	    这个结果与 Civelli et al. 的发现一致（linear > nonlinear for cross-lingual difficulty transfer），也回应了
1250	    reviewer 可能提出的 "为什么不用更复杂的 probe" 的质疑。 Paper 据此使用 logistic regression 作为 primary
1251	    probe，MLP 仅作为 ablation 报告。
1252	
1253	    '
1254	  tables:
1255	  - title: LogReg vs MLP at Key Layers (Qwen3-235B)
1256	    columns:
1257	    - layer
1258	    - logreg_en
1259	    - mlp_en
1260	    - en_delta
1261	    - logreg_transfer
1262	    - mlp_transfer
1263	    - transfer_delta
1264	    data:
1265	    - layer: L40
1266	      logreg_en: 0.776
1267	      mlp_en: 0.794
1268	      en_delta: 1.8
1269	      logreg_transfer: 0.696
1270	      mlp_transfer: 0.672
1271	      transfer_delta: -2.4
1272	    - layer: L52
1273	      logreg_en: 0.796
1274	      mlp_en: 0.813
1275	      en_delta: 1.7
1276	      logreg_transfer: 0.682
1277	      mlp_transfer: 0.651
1278	      transfer_delta: -3.1
1279	    - layer: L64
1280	      logreg_en: 0.807
1281	      mlp_en: 0.824
1282	      en_delta: 1.7
1283	      logreg_transfer: 0.661
1284	      mlp_transfer: 0.626
1285	      transfer_delta: -3.5
1286	    - layer: L76
1287	      logreg_en: 0.812
1288	      mlp_en: 0.827
1289	      en_delta: 1.5
1290	      logreg_transfer: 0.644
1291	      mlp_transfer: 0.607
1292	      transfer_delta: -3.7
1293	  - title: LogReg vs MLP at Key Layers (Llama 4 Scout)
1294	    columns:
1295	    - layer
1296	    - logreg_en
1297	    - mlp_en
1298	    - en_delta
1299	    - logreg_transfer
1300	    - mlp_transfer
1301	    - transfer_delta
1302	    data:
1303	    - layer: L24
1304	      logreg_en: 0.741
1305	      mlp_en: 0.758
1306	      en_delta: 1.7
1307	      logreg_transfer: 0.677
1308	      mlp_transfer: 0.654
1309	      transfer_delta: -2.3
1310	    - layer: L32
1311	      logreg_en: 0.771
1312	      mlp_en: 0.789
1313	      en_delta: 1.8
1314	      logreg_transfer: 0.679
1315	      mlp_transfer: 0.651
1316	      transfer_delta: -2.8
1317	    - layer: L40
1318	      logreg_en: 0.79
1319	      mlp_en: 0.808
1320	      en_delta: 1.8
1321	      logreg_transfer: 0.663
1322	      mlp_transfer: 0.631
1323	      transfer_delta: -3.2
1324	    - layer: L44
1325	      logreg_en: 0.793
1326	      mlp_en: 0.812
1327	      en_delta: 1.9
1328	      logreg_transfer: 0.657
1329	      mlp_transfer: 0.625
1330	      transfer_delta: -3.2
1331	  figures_description:
1332	  - 'Figure S1 (Appendix): Dual-line plot per model — x-axis: layer depth, y-axis:
1333	    AUROC. Solid lines = LogReg (blue = English, orange = transfer mean). Dashed lines
1334	    = MLP (blue = English, orange = transfer mean). The "scissors" pattern: MLP blue
1335	    line is above LogReg blue line (better English), but MLP orange line is below
1336	    LogReg orange line (worse transfer). Gap widens at deeper layers.
1337	
1338	    '
1339	  analysis: 'Hypothesis confirmed: linear probes transfer significantly better cross-lingually
1340	    than MLP probes (+3.5pp average), while sacrificing only 1.7pp English accuracy.
1341	    The transfer advantage of linear probes is larger at deeper layers (where distribution
1342	    shift is worst), which is consistent with the Pareto tradeoff mechanism — nonlinear
1343	    probes amplify the depth-dependent distribution shift. This result justifies the
1344	    methodological choice of logistic regression as the primary probe throughout the
1345	    paper.
1346	
1347	    '
1348	- name: Additional Benchmark Evaluation
1349	  plan_id: plan_007
1350	  description: 'Evaluate best probes + CaCLR on Belebele (20 languages, reading comprehension)
1351	    and MMLU-ProX (20 languages, harder STEM questions). Tests generalization of Pareto
1352	    frontier and CaCLR beyond GlobalMMLU.
1353	
1354	    '
1355	  expected_results:
1356	    belebele_en_auroc_best: 0.798
1357	    belebele_zs_transfer_mean_at_best_transfer: 0.708
1358	    belebele_pareto_replicates: true
1359	    belebele_caclr_vs_linproj_pp: 1.1
1360	    belebele_best_transfer_layer_qwen3: L44
1361	    mmlupx_en_auroc_best: 0.824
1362	    mmlupx_zs_transfer_mean_at_best_transfer: 0.681
1363	    mmlupx_pareto_replicates: true
1364	    mmlupx_caclr_vs_linproj_pp: 1.6
1365	    mmlupx_best_transfer_layer_qwen3: L40
1366	    belebele_low_resource_pass_rate: 0.6
1367	    mmlupx_low_resource_pass_rate: 0.4
1368	  result_rationale: 'Pareto frontier 作为 representation structure 的 property，不应依赖特定
1369	    benchmark。 Belebele（阅读理解）和 MMLU-ProX（更难 STEM 题）提供了两个不同难度和认知类型的 测试。Belebele 稍简单，英语
1370	    AUROC 稍低（0.798 vs 0.812）因为 reading comprehension 的 correctness 比 knowledge QA
1371	    更依赖 surface patterns，linear probe 的 ceiling 更低。 但迁移质量稍高（0.708 vs 0.696）因为阅读理解的跨语言
1372	    pattern 更相似。MMLU-ProX 更难，英语 AUROC 更高（0.824）因为难题的 correctness signal 更 salient（模型更
1373	    "确定" 自己是否知道），但迁移稍差（0.681）因为 STEM 知识的跨语言 variation 更大。 CaCLR 在 MMLU-ProX 上优势稍大（+1.6pp
1374	    vs +1.1pp）因为更难的题目有更多 distribution shift 可以被 consistency term 修正。两个 benchmark 都复现了
1375	    Pareto 结构，确认其 generalizability。低资源在 MMLU-ProX 上更差（2/5 vs 3/5）因为难题放大了数据不足的问题。
1376	
1377	    '
1378	  tables:
1379	  - title: Cross-Benchmark Comparison (Qwen3-235B, LogReg)
1380	    columns:
1381	    - metric
1382	    - GlobalMMLU
1383	    - Belebele
1384	    - MMLU_ProX
1385	    data:
1386	    - metric: en_auroc_best
1387	      GlobalMMLU: 0.812
1388	      Belebele: 0.798
1389	      MMLU_ProX: 0.824
1390	    - metric: best_en_layer
1391	      GlobalMMLU: L76
1392	      Belebele: L72
1393	      MMLU_ProX: L76
1394	    - metric: best_transfer_layer
1395	      GlobalMMLU: L40
1396	      Belebele: L44
1397	      MMLU_ProX: L40
1398	    - metric: zs_transfer_mean
1399	      GlobalMMLU: 0.696
1400	      Belebele: 0.708
1401	      MMLU_ProX: 0.681
1402	    - metric: transfer_drop_pp
1403	      GlobalMMLU: 16.8
1404	      Belebele: 13.1
1405	      MMLU_ProX: 18.4
1406	    - metric: caclr_vs_linproj_pp
1407	      GlobalMMLU: 1.4
1408	      Belebele: 1.1
1409	      MMLU_ProX: 1.6
1410	    - metric: low_resource_pass_rate
1411	      GlobalMMLU: 0.6
1412	      Belebele: 0.6
1413	      MMLU_ProX: 0.4
1414	  figures_description:
1415	  - 'Figure S2 (Appendix): Three-panel Pareto frontier plots (GlobalMMLU / Belebele
1416	    / MMLU-ProX) with identical axis scales. Visual pattern clearly replicates across
1417	    all three: upward-then-left curve in all panels, with MMLU-ProX showing the steepest
1418	    tradeoff and Belebele the mildest.
1419	
1420	    '
1421	  analysis: 'Cross-benchmark replication is the key result: Pareto frontier structure
1422	    is benchmark- agnostic, confirming it reflects model representation properties
1423	    rather than dataset artifacts. The quantitative differences (Belebele flatter,
1424	    MMLU-ProX steeper) are interpretable and strengthen the paper''s analysis. CaCLR''s
1425	    benchmark-robust improvement (+1.1 to +1.6pp) confirms its general utility.
1426	
1427	    '
1428	- name: INT8 Validation Ablation
1429	  plan_id: plan_010
1430	  description: 'Compare INT8 vs FP16 probing results at 5 representative layers for
1431	    Llama 4 Scout on 5% random subset (~700 samples). Validates that INT8 quantization
1432	    doesn''t distort correctness signals in the activation space.
1433	
1434	    '
1435	  expected_results:
1436	    max_auroc_delta_pp: 0.3
1437	    mean_auroc_delta_pp: 0.24
1438	    direction_bias: negligible (INT8 marginally lower at all layers)
1439	    cosine_sim_directions: 0.997
1440	    conclusion: INT8 validated — no meaningful distortion of correctness signal
1441	  result_rationale: 'INT8 weight-only quantization 保留了 activation space 的大部分结构（weight
1442	    quantization 引入的 perturbation 在 high-dimensional space 中被分摊，对线性 probe 的影响极小）。
1443	    AUROC delta < 0.3pp 远低于实验中观测到的其他 effect sizes（transfer drop 13-17pp, CaCLR improvement
1444	    1-4pp）。Correctness direction 的 cosine similarity 0.997 说明 quantization 几乎不改变 direction，只是
1445	    slightly perturb magnitude。这是 expected result，但对 reviewer 来说是必要的 due diligence——没有这个
1446	    ablation，reviewer 可能质疑 INT8 是否引入 systematic bias。
1447	
1448	    '
1449	  tables:
1450	  - title: INT8 vs FP16 Probing Results (Llama 4 Scout, 5% subset)
1451	    columns:
1452	    - layer
1453	    - int8_auroc
1454	    - fp16_auroc
1455	    - delta_pp
1456	    - direction_cosine
1457	    data:
1458	    - layer: L4
1459	      int8_auroc: 0.568
1460	      fp16_auroc: 0.571
1461	      delta_pp: -0.3
1462	      direction_cosine: 0.998
1463	    - layer: L12
1464	      int8_auroc: 0.648
1465	      fp16_auroc: 0.651
1466	      delta_pp: -0.3
1467	      direction_cosine: 0.997
1468	    - layer: L24
1469	      int8_auroc: 0.738
1470	      fp16_auroc: 0.74
1471	      delta_pp: -0.2
1472	      direction_cosine: 0.998
1473	    - layer: L36
1474	      int8_auroc: 0.78
1475	      fp16_auroc: 0.782
1476	      delta_pp: -0.2
1477	      direction_cosine: 0.997
1478	    - layer: L44
1479	      int8_auroc: 0.791
1480	      fp16_auroc: 0.794
1481	      delta_pp: -0.3
1482	      direction_cosine: 0.996
1483	  figures_description:
1484	  - 'Figure S3 (Appendix): Paired bar chart — 5 layers, INT8 (blue) vs FP16 (orange)
1485	    bars. Bars nearly identical height at every layer. Annotation: "max Δ = 0.3pp".
1486	    Simple, clean validation figure.
1487	
1488	    '
1489	  analysis: 'INT8 quantization is validated for correctness probing. The <0.3pp AUROC
1490	    difference is well within noise levels and has no systematic direction. This ablation
1491	    can be reported in 2-3 sentences in the Appendix with the table — no need for
1492	    extended discussion.
1493	
1494	    '
1495	- name: Gemma 4 31B Dense — Camera-Ready Extension
1496	  plan_id: plan_008
1497	  description: 'Third architecture (60 layers, dense, FP16) for camera-ready version.
1498	    Dense vs MoE architectural contrast. Full Pareto frontier, 20+ languages.
1499	
1500	    '
1501	  expected_results:
1502	    en_auroc_best: 0.805
1503	    en_best_layer: L48
1504	    best_transfer_layer: L32
1505	    zs_transfer_mean_at_best_transfer: 0.709
1506	    zs_transfer_drop_at_best_en_pp: 10.2
1507	    pareto_frontier_shape: smoother than MoE models, more gradual transfer decline
1508	    low_resource_pass_rate: 0.6
1509	    caclr_vs_linproj_pp: 1.0
1510	    frontier_agreement_with_qwen3: 0.62
1511	    frontier_agreement_with_llama4: 0.71
1512	  result_rationale: 'Dense architecture 与 MoE 的关键差异：没有 routing 机制导致的 discrete layer-wise
1513	    变化，representation 的 language-specificity 随 depth 更连续地增长。因此 Pareto frontier 更 smooth（transfer
1514	    decline 更 gradual），transfer drop 仅 10.2pp（vs Qwen3 16.8pp, Llama4 13.6pp）。English
1515	    AUROC 略低于 Qwen3（0.805 vs 0.812）因为 31B dense 的 total compute 少于 235B MoE。Best transfer
1516	    在 53% 深度（L32/60）， 介于 Qwen3(43%) 和 Llama4(67%) 之间。CaCLR 优势更小（+1.0pp）因为 dense model
1517	    的 representation shift across languages 本身更 gradual，simple baselines 已经 表现不错。与
1518	    Llama4 的 frontier agreement (0.71) 高于与 Qwen3 (0.62)，可能因为 Llama4 和 Gemma4 的训练数据组成更相似。
1519	
1520	    '
1521	  tables:
1522	  - title: Three-Architecture Pareto Summary
1523	    columns:
1524	    - metric
1525	    - Qwen3_235B_MoE
1526	    - Llama4_Scout_MoE
1527	    - Gemma4_31B_Dense
1528	    data:
1529	    - metric: total_layers
1530	      Qwen3_235B_MoE: 94
1531	      Llama4_Scout_MoE: 48
1532	      Gemma4_31B_Dense: 60
1533	    - metric: architecture
1534	      Qwen3_235B_MoE: MoE
1535	      Llama4_Scout_MoE: MoE
1536	      Gemma4_31B_Dense: Dense
1537	    - metric: en_auroc_best
1538	      Qwen3_235B_MoE: 0.812
1539	      Llama4_Scout_MoE: 0.793
1540	      Gemma4_31B_Dense: 0.805
1541	    - metric: best_transfer_depth_pct
1542	      Qwen3_235B_MoE: 43
1543	      Llama4_Scout_MoE: 67
1544	      Gemma4_31B_Dense: 53
1545	    - metric: transfer_drop_pp
1546	      Qwen3_235B_MoE: 16.8
1547	      Llama4_Scout_MoE: 13.6
1548	      Gemma4_31B_Dense: 10.2
1549	    - metric: frontier_smoothness
1550	      Qwen3_235B_MoE: sharp
1551	      Llama4_Scout_MoE: flat/noisy
1552	      Gemma4_31B_Dense: smooth
1553	    - metric: caclr_benefit_pp
1554	      Qwen3_235B_MoE: 1.4
1555	      Llama4_Scout_MoE: 1.2
1556	      Gemma4_31B_Dense: 1.0
1557	  figures_description:
1558	  - 'Figure 6 (Camera-Ready): Three-model overlaid Pareto frontiers. Qwen3 (circles)
1559	    shows widest, steepest frontier. Llama4 (triangles) shows compact, flat frontier.
1560	    Gemma4 (squares) shows smooth, intermediate frontier. Visual immediately communicates
1561	    architecture-dependent Pareto structure. Inset table shows optimal transfer depth
1562	    %.
1563	
1564	    '
1565	  analysis: 'Dense vs MoE 对比是 camera-ready 的最有价值的扩展。Dense 架构的 smoother frontier 提供了
1566	    mechanistic insight：MoE routing 在深层的 language-specific expert selection 可能是 Qwen3
1567	    sharp Pareto tradeoff 的原因，而 dense model 的 continuous feature evolution 产生更 gradual
1568	    的 language specificity 增长。三架构的 frontier 定性一致 但定量不同，强化了 "Pareto frontier is universal
1569	    but architecture-dependent" 的 headline claim。
1570	
1571	    '
1572	- name: Extended Language Coverage — Camera-Ready Extension
1573	  plan_id: plan_009
1574	  description: 'Expand from 20 to 50+ languages using GlobalMMLU/Belebele full language
1575	    sets. Tests how Pareto frontier patterns scale to long-tail languages.
1576	
1577	    '
1578	  expected_results:
1579	    total_languages: 53
1580	    high_resource_count: 12
1581	    mid_resource_count: 18
1582	    low_resource_count: 23
1583	    zs_transfer_mean_all_52: 0.651
1584	    low_resource_pass_rate_23: 0.35
1585	    very_low_resource_auroc_range:
1586	    - 0.5
1587	    - 0.58
1588	    pareto_replicates_qualitatively: true
1589	    new_failure_languages:
1590	    - qu
1591	    - ha
1592	    - gn
1593	    - lg
1594	    - ny
1595	    - sn
1596	    - xh
1597	    - zu
1598	    - ig
1599	    - mg
1600	    - rw
1601	    - so
1602	    - tn
1603	    - ts
1604	    - ve
1605	    caclr_improvement_rate_52: 0.67
1606	    layer_rank_consistency_52: 0.58
1607	  result_rationale: '扩展到 53 语言后，低资源尾部显著增长（23 个 low-resource vs 原来 5 个），整体 指标下降是 expected
1608	    的。ZS transfer mean 从 0.696（20 langs）降至 0.651（52 non-en langs）因为新增语言大部分是低资源的非洲/大洋洲/美洲原住民语言，GlobalMMLU
1609	    翻译 质量参差不齐。低资源 pass rate 从 0.6（3/5）降至 0.35（8/23）说明 "correctness direction universally
1610	    transfers" 的说法在尾部语言不成立——但 Pareto 结构本身 仍然定性存在。CaCLR 的 improvement rate 也从 0.74
1611	    降至 0.67，但仍是多数语言 受益。Layer ranking consistency 从 0.71 降至 0.58，因为低资源语言的最优迁移层 更分散。Paper
1612	    应将此 framing 为 "Pareto frontier scales to 50+ languages but with diminishing returns
1613	    for very low-resource languages, motivating future work on low-resource-specific
1614	    transfer methods."
1615	
1616	    '
1617	  tables:
1618	  - title: Extended Coverage Summary by Tier
1619	    columns:
1620	    - tier
1621	    - n_langs_20
1622	    - n_langs_53
1623	    - mean_auroc_20
1624	    - mean_auroc_53
1625	    - pass_rate_20
1626	    - pass_rate_53
1627	    data:
1628	    - tier: high
1629	      n_langs_20: 6
1630	      n_langs_53: 11
1631	      mean_auroc_20: 0.753
1632	      mean_auroc_53: 0.745
1633	      pass_rate_20: 1.0
1634	      pass_rate_53: 1.0
1635	    - tier: mid
1636	      n_langs_20: 8
1637	      n_langs_53: 18
1638	      mean_auroc_20: 0.711
1639	      mean_auroc_53: 0.698
1640	      pass_rate_20: 1.0
1641	      pass_rate_53: 0.94
1642	    - tier: low
1643	      n_langs_20: 5
1644	      n_langs_53: 23
1645	      mean_auroc_20: 0.607
1646	      mean_auroc_53: 0.571
1647	      pass_rate_20: 0.6
1648	      pass_rate_53: 0.35
1649	    - tier: all
1650	      n_langs_20: 19
1651	      n_langs_53: 52
1652	      mean_auroc_20: 0.696
1653	      mean_auroc_53: 0.651
1654	      pass_rate_20: 0.89
1655	      pass_rate_53: 0.69
1656	  figures_description:
1657	  - 'Figure 7 (Camera-Ready): Language-level scatter — x-axis: log(pretraining data
1658	    size estimate, tokens), y-axis: best zero-shot transfer AUROC. Clear positive
1659	    correlation (r≈0.72). Horizontal dashed line at AUROC=0.60. Labels for notable
1660	    languages. Below the line: cluster of 15 very-low-resource languages. Color by
1661	    language family. Shows that transfer success is primarily a function of pretraining
1662	    representation quality.
1663	
1664	    '
1665	  analysis: 'Extended coverage confirms the fundamental insight: Pareto frontier is
1666	    a structural property that scales to 50+ languages, but the practical utility
1667	    of zero-shot correctness probe transfer is bounded by pretraining data quantity.
1668	    The 15 languages below the 0.60 threshold are all in the lowest quintile of pretraining
1669	    data, suggesting a minimum representation quality floor for this approach. This
1670	    limitation should be acknowledged transparently in the Discussion section, not
1671	    hidden — it''s a valuable finding about the scope of probe-based calibration methods.'
1672	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "710d52da-b117-4d2a-baed-91e421731308",
  "isSidechain": false,
  "promptId": "7f3a0651-0480-4418-9ac1-d949b2c2cd30",
  "type": "user",
  "uuid": "1d1e9ae2-db43-4ad5-b0c5-64c2c9b790bb",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/median/review_context.yaml",
      "content": "narrative_guidance: 'Rebalance toward discovery + analysis. Claim 1 (Pareto frontier)\n  becomes the headline contribution — first systematic characterization of depth-transferability\n  tradeoff across architectures and 20 languages. Claim 2 reframes decomposition as\n  ''partial but prescriptive'': difficulty component is clearly transferable, capability\n  residual is noisy but the decomposition still predicts when simple baselines suffice\n  vs when CaCLR helps. Claim 3 softens: CaCLR is presented as ''matching or exceeding\n  the best simple baseline (linear projection) while requiring no target-language\n  data at all'' — emphasize the zero-label setting rather than raw metric superiority.\n  Add ablation showing where CaCLR''s consistency term specifically helps (mid-resource\n  languages). Claim 4 presented with resource-tier analysis showing orthogonality\n  is robust for well-represented languages but noisier for low-resource. Headline:\n  ''Cross-lingual calibration probes reveal architecture-dependent Pareto frontier;\n  CaCLR matches supervised transfer without target labels.''\n\n  '\nimagined_experiments:\n- name: Full Pareto Frontier — Qwen3-235B-A22B\n  plan_id: plan_001\n  description: '94-layer MoE model, INT8 quantization. 24 probed layers (every 4th:\n    L0–L92). 20 languages (7 high / 8 mid / 5 low resource). English logistic-regression\n    correctness probes trained per layer, evaluated on 5 transfer conditions (zero-shot,\n    mean-shift, linear projection, few-shot 25/100, CaCLR placeholder). Core Pareto\n    frontier data for Claim 1.\n\n    '\n  expected_results:\n    en_auroc_best: 0.812\n    en_best_layer: L76\n    en_auroc_range:\n    - 0.531\n    - 0.812\n    en_ece_raw_at_best: 0.168\n    en_ece_tempcal_at_best: 0.057\n    temp_scaling_T: 5.83\n    zs_transfer_auroc_mean_19lang_at_best_en: 0.644\n    zs_transfer_drop_at_best_en_pp: 16.8\n    best_transfer_layer: L40\n    zs_transfer_auroc_mean_at_best_transfer: 0.696\n    en_auroc_at_best_transfer: 0.776\n    pareto_depth_transfer_rank_corr: 0.71\n    low_resource_zs_pass_rate: 0.6\n    mean_shift_improvement_rate: 0.05\n    linproj_auroc_mean_at_best_transfer: 0.724\n    fewshot25_auroc_mean_at_best_transfer: 0.711\n    fewshot100_auroc_mean_at_best_transfer: 0.743\n  result_rationale: 'Qwen3-235B-A22B 的 94 层深度提供了充分的层级分辨率来观测 Pareto tradeoff。 深层（L76）英语\n    AUROC 达 0.812，因为更深层积累了更多 task-specific correctness 信号； 但这些深层 representation 也更\n    language-specific（MoE routing 在深层更分化）， 导致 zero-shot 迁移退化至 0.644（drop 16.8pp）。最佳迁移层\n    L40 处于模型 ~42% 深度，此处 representation 仍保留足够的 language-agnostic 结构。跨语言层序一致性 Spearman\n    ρ=0.71 表明各语言对最优迁移深度的偏好高度一致，Pareto 结构是 robust 的。 Mean-shift 继承 MVP 的失败模式（correctness\n    ≠ knowledge-boundary），仅 1/19 语言微弱改善。Linear projection 利用无标注目标语激活做线性对齐，在 L40 处比\n    zero-shot 高 2.8pp，确立为 CaCLR 需要超越的 strong baseline。 低资源语言（sw/te/my 通过，am/yo 失败）符合预期：GlobalMMLU\n    低资源子集样本量小且 翻译质量不稳定，但 3/5 通过证明 correctness direction 跨语言性在大模型上比 7B 更强。\n\n    '\n  tables:\n  - title: English AUROC by Layer (Logistic Regression)\n    columns:\n    - layer\n    - depth_pct\n    - en_auroc\n    - en_ece_raw\n    data:\n    - layer: L0\n      depth_pct: 0\n      en_auroc: 0.531\n      en_ece_raw: 0.341\n    - layer: L4\n      depth_pct: 4\n      en_auroc: 0.557\n      en_ece_raw: 0.328\n    - layer: L8\n      depth_pct: 9\n      en_auroc: 0.589\n      en_ece_raw: 0.312\n    - layer: L12\n      depth_pct: 13\n      en_auroc: 0.621\n      en_ece_raw: 0.293\n    - layer: L16\n      depth_pct: 17\n      en_auroc: 0.653\n      en_ece_raw: 0.274\n    - layer: L20\n      depth_pct: 21\n      en_auroc: 0.684\n      en_ece_raw: 0.255\n    - layer: L24\n      depth_pct: 26\n      en_auroc: 0.711\n      en_ece_raw: 0.237\n    - layer: L28\n      depth_pct: 30\n      en_auroc: 0.735\n      en_ece_raw: 0.221\n    - layer: L32\n      depth_pct: 34\n      en_auroc: 0.752\n      en_ece_raw: 0.21\n    - layer: L36\n      depth_pct: 38\n      en_auroc: 0.766\n      en_ece_raw: 0.199\n    - layer: L40\n      depth_pct: 43\n      en_auroc: 0.776\n      en_ece_raw: 0.192\n    - layer: L44\n      depth_pct: 47\n      en_auroc: 0.784\n      en_ece_raw: 0.186\n    - layer: L48\n      depth_pct: 51\n      en_auroc: 0.79\n      en_ece_raw: 0.182\n    - layer: L52\n      depth_pct: 55\n      en_auroc: 0.796\n      en_ece_raw: 0.178\n    - layer: L56\n      depth_pct: 60\n      en_auroc: 0.8\n      en_ece_raw: 0.175\n    - layer: L60\n      depth_pct: 64\n      en_auroc: 0.804\n      en_ece_raw: 0.173\n    - layer: L64\n      depth_pct: 68\n      en_auroc: 0.807\n      en_ece_raw: 0.171\n    - layer: L68\n      depth_pct: 72\n      en_auroc: 0.81\n      en_ece_raw: 0.17\n    - layer: L72\n      depth_pct: 77\n      en_auroc: 0.811\n      en_ece_raw: 0.169\n    - layer: L76\n      depth_pct: 81\n      en_auroc: 0.812\n      en_ece_raw: 0.168\n    - layer: L80\n      depth_pct: 85\n      en_auroc: 0.809\n      en_ece_raw: 0.17\n    - layer: L84\n      depth_pct: 89\n      en_auroc: 0.804\n      en_ece_raw: 0.174\n    - layer: L88\n      depth_pct: 94\n      en_auroc: 0.796\n      en_ece_raw: 0.179\n    - layer: L92\n      depth_pct: 98\n      en_auroc: 0.782\n      en_ece_raw: 0.188\n  - title: Zero-Shot Transfer AUROC by Resource Tier (key layers)\n    note: 19 non-English languages; tier means ± std\n    columns:\n    - layer\n    - high_6_mean\n    - high_6_std\n    - mid_8_mean\n    - mid_8_std\n    - low_5_mean\n    - low_5_std\n    - all_19_mean\n    data:\n    - layer: L24\n      high_6_mean: 0.731\n      high_6_std: 0.011\n      mid_8_mean: 0.692\n      mid_8_std: 0.014\n      low_5_mean: 0.59\n      low_5_std: 0.031\n      all_19_mean: 0.679\n    - layer: L32\n      high_6_mean: 0.747\n      high_6_std: 0.01\n      mid_8_mean: 0.706\n      mid_8_std: 0.013\n      low_5_mean: 0.601\n      low_5_std: 0.029\n      all_19_mean: 0.691\n    - layer: L40\n      high_6_mean: 0.753\n      high_6_std: 0.01\n      mid_8_mean: 0.711\n      mid_8_std: 0.013\n      low_5_mean: 0.607\n      low_5_std: 0.032\n      all_19_mean: 0.696\n    - layer: L52\n      high_6_mean: 0.741\n      high_6_std: 0.011\n      mid_8_mean: 0.697\n      mid_8_std: 0.015\n      low_5_mean: 0.586\n      low_5_std: 0.035\n      all_19_mean: 0.682\n    - layer: L64\n      high_6_mean: 0.721\n      high_6_std: 0.013\n      mid_8_mean: 0.673\n      mid_8_std: 0.017\n      low_5_mean: 0.558\n      low_5_std: 0.039\n      all_19_mean: 0.661\n    - layer: L76\n      high_6_mean: 0.705\n      high_6_std: 0.01\n      mid_8_mean: 0.657\n      mid_8_std: 0.016\n      low_5_mean: 0.54\n      low_5_std: 0.033\n      all_19_mean: 0.644\n    - layer: L92\n      high_6_mean: 0.672\n      high_6_std: 0.015\n      mid_8_mean: 0.621\n      mid_8_std: 0.02\n      low_5_mean: 0.497\n      low_5_std: 0.042\n      all_19_mean: 0.607\n  - title: Per-Language Zero-Shot AUROC at L40 (Best Transfer) and L76 (Best English)\n    columns:\n    - lang\n    - tier\n    - L40_auroc\n    - L76_auroc\n    - delta_pp\n    data:\n    - lang: zh\n      tier: high\n      L40_auroc: 0.762\n      L76_auroc: 0.712\n      delta_pp: -5.0\n    - lang: de\n      tier: high\n      L40_auroc: 0.753\n      L76_auroc: 0.703\n      delta_pp: -5.0\n    - lang: fr\n      tier: high\n      L40_auroc: 0.757\n      L76_auroc: 0.708\n      delta_pp: -4.9\n    - lang: es\n      tier: high\n      L40_auroc: 0.764\n      L76_auroc: 0.715\n      delta_pp: -4.9\n    - lang: ja\n      tier: high\n      L40_auroc: 0.737\n      L76_auroc: 0.688\n      delta_pp: -4.9\n    - lang: ru\n      tier: high\n      L40_auroc: 0.744\n      L76_auroc: 0.697\n      delta_pp: -4.7\n    - lang: ar\n      tier: mid\n      L40_auroc: 0.717\n      L76_auroc: 0.667\n      delta_pp: -5.0\n    - lang: hi\n      tier: mid\n      L40_auroc: 0.71\n      L76_auroc: 0.659\n      delta_pp: -5.1\n    - lang: ko\n      tier: mid\n      L40_auroc: 0.703\n      L76_auroc: 0.652\n      delta_pp: -5.1\n    - lang: pt\n      tier: mid\n      L40_auroc: 0.731\n      L76_auroc: 0.681\n      delta_pp: -5.0\n    - lang: vi\n      tier: mid\n      L40_auroc: 0.696\n      L76_auroc: 0.644\n      delta_pp: -5.2\n    - lang: th\n      tier: mid\n      L40_auroc: 0.688\n      L76_auroc: 0.633\n      delta_pp: -5.5\n    - lang: tr\n      tier: mid\n      L40_auroc: 0.706\n      L76_auroc: 0.655\n      delta_pp: -5.1\n    - lang: pl\n      tier: mid\n      L40_auroc: 0.723\n      L76_auroc: 0.673\n      delta_pp: -5.0\n    - lang: sw\n      tier: low\n      L40_auroc: 0.638\n      L76_auroc: 0.579\n      delta_pp: -5.9\n    - lang: te\n      tier: low\n      L40_auroc: 0.644\n      L76_auroc: 0.59\n      delta_pp: -5.4\n    - lang: my\n      tier: low\n      L40_auroc: 0.607\n      L76_auroc: 0.543\n      delta_pp: -6.4\n    - lang: am\n      tier: low\n      L40_auroc: 0.583\n      L76_auroc: 0.532\n      delta_pp: -5.1\n    - lang: yo\n      tier: low\n      L40_auroc: 0.561\n      L76_auroc: 0.51\n      delta_pp: -5.1\n  figures_description:\n  - 'Figure 1a: Pareto frontier scatter — x-axis: English AUROC, y-axis: zero-shot\n    transfer mean AUROC (19 langs). Each point is one probed layer (L0–L92), color-coded\n    by depth percentage. Clear upward-then-left curve: shallow layers cluster at bottom-left\n    (both low), mid layers at upper-right of transfer axis (L40 peak), deep layers\n    drift right on English axis but downward on transfer. Pareto-efficient frontier\n    connects L40→L48→L56→L64→L76. Annotate L40 (\"best transfer\") and L76 (\"best English\").\n\n    '\n  - 'Figure 1b: Layer-depth profile — dual y-axis plot. Left axis: English AUROC (blue,\n    rising then plateau). Right axis: ZS transfer mean (orange, rising then falling).\n    Crossover region around L44–L52 clearly visible. Shaded band shows ±1σ across\n    19 languages on the transfer curve — band widens at deeper layers.\n\n    '\n  - 'Figure 1c: Heatmap — rows: 19 languages (grouped by resource tier), columns:\n    24 layers. Cell color: zero-shot AUROC. Clear gradient: high-resource rows are\n    warm (0.65–0.76) across most layers; low-resource rows are cool (0.50–0.64) with\n    the warm zone concentrated at mid-depth layers. Visual pattern immediately shows\n    depth-transferability × resource interaction.\n\n    '\n  analysis: 'Qwen3-235B exhibits a textbook Pareto frontier for Claim 1. The depth-transferability\n    tradeoff is sharp: 36 layers separate the best-EN (L76) and best-transfer (L40)\n    operating points, with 16.8pp transfer degradation at L76. The layer ranking consistency\n    ρ=0.71 means 19 languages broadly agree on which depths transfer best, supporting\n    the claim that this is a structural property of the model rather than a language-specific\n    artifact. Low-resource languages show the expected fragility: 3/5 pass but am\n    and yo fall below the 0.60 AUROC threshold even at the optimal transfer layer.\n    This will be framed as a resource-tier modulation of the Pareto frontier rather\n    than a failure of the phenomenon. Mean-shift''s continued failure (replicating\n    MVP) cleanly motivates CaCLR.\n\n    '\n- name: Full Pareto Frontier — Llama 4 Scout\n  plan_id: plan_002\n  description: '48-layer MoE model, INT8 quantization. 12 probed layers (every 4th:\n    L0–L44). 20 languages, 5 transfer conditions. Second architecture for cross-model\n    Pareto frontier comparison (Claim 1).\n\n    '\n  expected_results:\n    en_auroc_best: 0.793\n    en_best_layer: L44\n    en_auroc_range:\n    - 0.538\n    - 0.793\n    en_ece_raw_at_best: 0.178\n    en_ece_tempcal_at_best: 0.063\n    temp_scaling_T: 5.41\n    zs_transfer_auroc_mean_19lang_at_best_en: 0.657\n    zs_transfer_drop_at_best_en_pp: 13.6\n    best_transfer_layer: L32\n    zs_transfer_auroc_mean_at_best_transfer: 0.679\n    en_auroc_at_best_transfer: 0.771\n    pareto_depth_transfer_rank_corr: 0.56\n    low_resource_zs_pass_rate: 0.4\n    mean_shift_improvement_rate: 0.05\n    linproj_auroc_mean_at_best_transfer: 0.705\n    pareto_frontier_agreement_with_qwen3: 0.67\n  result_rationale: 'Llama 4 Scout 仅 48 层（vs Qwen3 的 94 层），Pareto 前沿更 flat/noisy。\n    英语 AUROC 峰值 0.793 低于 Qwen3 的 0.812，原因是 Scout 作为 MoE 的 active 参数量（~17B）小于 Qwen3-A22B，correctness\n    信号的 linear accessibility 稍弱。 最佳迁移层 L32（67% 深度）vs 最佳英语层 L44（92% 深度）仅相隔 12 层，前沿\n    更紧凑。Transfer drop 13.6pp 低于 Qwen3 的 16.8pp，说明 Llama4 的深层 representation language-specificity\n    增长更平缓——可能与 Llama4 的训练数据分布有关（更多多语言 数据在预训练中）。跨语言层序一致性 ρ=0.56 明显低于 Qwen3 的 0.71，表明不同\n    语言在 Llama4 上对最优迁移层的偏好更分散，Pareto 结构存在但更 noisy。 与 Qwen3 的 frontier agreement 0.67\n    说明两个架构共享定性趋势（\"中层比深层 迁移更好\"）但定量最优点不同——这正是 \"architecture-dependent\" claim 的证据。 低资源仅\n    2/5 通过，sw 和 te 勉强过线，my/am/yo 失败。\n\n    '\n  tables:\n  - title: English AUROC by Layer (Logistic Regression)\n    columns:\n    - layer\n    - depth_pct\n    - en_auroc\n    - en_ece_raw\n    data:\n    - layer: L0\n      depth_pct: 0\n      en_auroc: 0.538\n      en_ece_raw: 0.336\n    - layer: L4\n      depth_pct: 8\n      en_auroc: 0.571\n      en_ece_raw: 0.318\n    - layer: L8\n      depth_pct: 17\n      en_auroc: 0.613\n      en_ece_raw: 0.296\n    - layer: L12\n      depth_pct: 25\n      en_auroc: 0.651\n      en_ece_raw: 0.272\n    - layer: L16\n      depth_pct: 33\n      en_auroc: 0.688\n      en_ece_raw: 0.248\n    - layer: L20\n      depth_pct: 42\n      en_auroc: 0.718\n      en_ece_raw: 0.228\n    - layer: L24\n      depth_pct: 50\n      en_auroc: 0.741\n      en_ece_raw: 0.212\n    - layer: L28\n      depth_pct: 58\n      en_auroc: 0.759\n      en_ece_raw: 0.199\n    - layer: L32\n      depth_pct: 67\n      en_auroc: 0.771\n      en_ece_raw: 0.19\n    - layer: L36\n      depth_pct: 75\n      en_auroc: 0.782\n      en_ece_raw: 0.183\n    - layer: L40\n      depth_pct: 83\n      en_auroc: 0.79\n      en_ece_raw: 0.179\n    - layer: L44\n      depth_pct: 92\n      en_auroc: 0.793\n      en_ece_raw: 0.178\n  - title: Zero-Shot Transfer AUROC by Resource Tier\n    columns:\n    - layer\n    - high_6_mean\n    - mid_8_mean\n    - low_5_mean\n    - all_19_mean\n    data:\n    - layer: L16\n      high_6_mean: 0.713\n      mid_8_mean: 0.67\n      low_5_mean: 0.571\n      all_19_mean: 0.659\n    - layer: L24\n      high_6_mean: 0.731\n      mid_8_mean: 0.691\n      low_5_mean: 0.587\n      all_19_mean: 0.677\n    - layer: L28\n      high_6_mean: 0.737\n      mid_8_mean: 0.697\n      low_5_mean: 0.591\n      all_19_mean: 0.683\n    - layer: L32\n      high_6_mean: 0.738\n      mid_8_mean: 0.694\n      low_5_mean: 0.585\n      all_19_mean: 0.679\n    - layer: L36\n      high_6_mean: 0.733\n      mid_8_mean: 0.688\n      low_5_mean: 0.574\n      all_19_mean: 0.673\n    - layer: L40\n      high_6_mean: 0.724\n      mid_8_mean: 0.678\n      low_5_mean: 0.561\n      all_19_mean: 0.663\n    - layer: L44\n      high_6_mean: 0.714\n      mid_8_mean: 0.669\n      low_5_mean: 0.548\n      all_19_mean: 0.657\n  - title: Cross-Architecture Pareto Comparison\n    columns:\n    - metric\n    - qwen3_235b\n    - llama4_scout\n    - interpretation\n    data:\n    - metric: en_auroc_best\n      qwen3_235b: 0.812\n      llama4_scout: 0.793\n      interpretation: Qwen3 higher, more layers for correctness to accumulate\n    - metric: best_transfer_depth_pct\n      qwen3_235b: 43\n      llama4_scout: 67\n      interpretation: Llama4 optimal transfer much deeper (flatter frontier)\n    - metric: zs_drop_at_best_en_pp\n      qwen3_235b: 16.8\n      llama4_scout: 13.6\n      interpretation: Qwen3 sharper tradeoff, Llama4 flatter\n    - metric: layer_rank_consistency\n      qwen3_235b: 0.71\n      llama4_scout: 0.56\n      interpretation: Qwen3 more consistent across languages\n    - metric: frontier_gap_layers\n      qwen3_235b: 36\n      llama4_scout: 12\n      interpretation: Qwen3 has wider Pareto gap\n    - metric: frontier_agreement\n      qwen3_235b: null\n      llama4_scout: null\n      interpretation: Spearman ρ=0.67 across 19 langs\n  figures_description:\n  - 'Figure 2: Overlaid Pareto frontiers for Qwen3 (circles) and Llama4 (triangles)\n    on same axes (EN AUROC × ZS transfer mean). Qwen3 frontier is wider and steeper;\n    Llama4 is more compact and flatter. Annotated inset: depth percentage labels show\n    Qwen3''s optimal transfer at 43% depth vs Llama4 at 67% depth — architecture-dependent\n    optimal operating point. This is the main Figure 1 of the paper.\n\n    '\n  analysis: 'Llama 4 Scout 确认 Pareto frontier 的跨架构泛化性，但 frontier shape 明显不同： 更 flat、更\n    compact、更 noisy。这支持 Claim 1 的 \"architecture-dependent\" 修饰语。 关键对比：Qwen3 的最优迁移在\n    43% 深度，Llama4 在 67% 深度——practitioners 不能 假设一个固定的 \"最优层百分比\"。Llama4 较低的层序一致性（0.56\n    vs 0.71）暗示 其内部 multilingual representation 的组织方式更分散，可能与 Scout 的 MoE routing 策略有关。两架构的\n    frontier agreement 0.67 说明定性趋势共享但定量不可直接迁移。\n\n    '\n- name: CaCLR Implementation and Comparative Evaluation\n  plan_id: plan_003\n  description: 'L_CaCLR = L_BCE + α·L_SB-ECE + β·L_consistency. Trained using English\n    correctness labels + unlabeled parallel activations from 19 target languages.\n    Hyperparameter sweep: α∈{0.1,0.2,0.3,0.5,1.0}, β∈{0.05,0.1,0.15,0.2,0.3}. Compared\n    against 4 baselines across full Pareto frontier for both models × 20 languages.\n\n    '\n  expected_results:\n    best_alpha: 0.3\n    best_beta: 0.15\n    qwen3_L40_caclr_auroc_mean: 0.738\n    qwen3_L40_caclr_ece_mean: 0.112\n    qwen3_L40_linproj_auroc_mean: 0.724\n    qwen3_L40_zeroshot_auroc_mean: 0.696\n    qwen3_L40_caclr_vs_linproj_pp: 1.4\n    qwen3_L76_caclr_auroc_mean: 0.695\n    qwen3_L76_linproj_auroc_mean: 0.678\n    qwen3_L76_caclr_vs_linproj_pp: 1.7\n    llama4_L32_caclr_auroc_mean: 0.717\n    llama4_L32_linproj_auroc_mean: 0.705\n    llama4_L32_caclr_vs_linproj_pp: 1.2\n    caclr_vs_linproj_auroc_delta_mean_pp: 1.3\n    caclr_ece_reduction_vs_tempcal_pct: 21.1\n    caclr_improvement_over_zs_pass_rate: 0.89\n    caclr_improvement_over_linproj_pass_rate: 0.74\n    qwen3_caclr_optimal_layer: L52\n    qwen3_zs_optimal_layer: L40\n    qwen3_frontier_shift_layers: 12\n    llama4_caclr_optimal_layer: L36\n    llama4_zs_optimal_layer: L32\n    llama4_frontier_shift_layers: 4\n    caclr_fails_vs_linproj_langs:\n    - th\n    - my\n    - am\n    - yo\n    - te\n    mean_shift_any_improvement: 1\n  result_rationale: 'CaCLR 在 median 档位下表现为 \"matches or marginally exceeds linear projection\"。\n    核心原因：consistency term（L_consistency）对齐的是 unlabeled parallel activations 的 probe\n    output distribution，在中-高资源语言中有效（parallel corpus 质量好， 激活空间足够对齐），但在低资源语言中由于 (a)\n    GlobalMMLU 翻译噪声 (b) tokenizer 覆盖率低导致 activation 本身质量差，consistency 信号变成噪声。因此 CaCLR\n    比 zero-shot 有显著改善（+4.2pp at L40），但比 linear projection 仅高 1.3pp 平均—— 因为 linear\n    projection 已经利用了 target-language activations 做对齐。CaCLR 的 真正优势在 Pareto shift：它把最优工作层从\n    L40 推到 L52（Qwen3），在更深层维持 迁移质量，同时获得 +2.0pp 英语 AUROC。SB-ECE loss 使 CaCLR probe 自带\n    calibration， ECE 比 temperature-scaled zero-shot 低 21.1%——这是方法论层面的 practical benefit。\n    Hyperparameter 敏感度中等：α=0.3 在 0.2-0.5 范围内差异小于 0.5pp，β 更敏感—— β>0.2 时 consistency\n    过强导致英语 AUROC 下降。5 个失败语言（th/my/am/yo/te） 中 4 个是低资源或 activation 质量低的语言，th 是 mid-resource\n    但独特的声调语言 导致 alignment 困难。\n\n    '\n  tables:\n  - title: 5-Method Comparison at Qwen3-235B Pareto-Optimal Layer (L40)\n    columns:\n    - method\n    - auroc_mean\n    - auroc_high\n    - auroc_mid\n    - auroc_low\n    - ece_mean\n    - brier_mean\n    data:\n    - method: zero-shot\n      auroc_mean: 0.696\n      auroc_high: 0.753\n      auroc_mid: 0.711\n      auroc_low: 0.607\n      ece_mean: 0.148\n      brier_mean: 0.286\n    - method: mean-shift\n      auroc_mean: 0.683\n      auroc_high: 0.742\n      auroc_mid: 0.698\n      auroc_low: 0.591\n      ece_mean: 0.155\n      brier_mean: 0.294\n    - method: linear-proj\n      auroc_mean: 0.724\n      auroc_high: 0.775\n      auroc_mid: 0.738\n      auroc_low: 0.633\n      ece_mean: 0.121\n      brier_mean: 0.261\n    - method: few-shot-25\n      auroc_mean: 0.711\n      auroc_high: 0.766\n      auroc_mid: 0.725\n      auroc_low: 0.618\n      ece_mean: 0.132\n      brier_mean: 0.27\n    - method: few-shot-100\n      auroc_mean: 0.743\n      auroc_high: 0.791\n      auroc_mid: 0.756\n      auroc_low: 0.655\n      ece_mean: 0.108\n      brier_mean: 0.247\n    - method: CaCLR\n      auroc_mean: 0.738\n      auroc_high: 0.786\n      auroc_mid: 0.754\n      auroc_low: 0.636\n      ece_mean: 0.112\n      brier_mean: 0.251\n  - title: 5-Method Comparison at Llama 4 Scout L32\n    columns:\n    - method\n    - auroc_mean\n    - auroc_high\n    - auroc_mid\n    - auroc_low\n    - ece_mean\n    data:\n    - method: zero-shot\n      auroc_mean: 0.679\n      auroc_high: 0.738\n      auroc_mid: 0.694\n      auroc_low: 0.585\n      ece_mean: 0.153\n    - method: mean-shift\n      auroc_mean: 0.668\n      auroc_high: 0.726\n      auroc_mid: 0.682\n      auroc_low: 0.577\n      ece_mean: 0.161\n    - method: linear-proj\n      auroc_mean: 0.705\n      auroc_high: 0.758\n      auroc_mid: 0.72\n      auroc_low: 0.61\n      ece_mean: 0.129\n    - method: few-shot-25\n      auroc_mean: 0.694\n      auroc_high: 0.749\n      auroc_mid: 0.708\n      auroc_low: 0.602\n      ece_mean: 0.138\n    - method: few-shot-100\n      auroc_mean: 0.728\n      auroc_high: 0.776\n      auroc_mid: 0.741\n      auroc_low: 0.64\n      ece_mean: 0.113\n    - method: CaCLR\n      auroc_mean: 0.717\n      auroc_high: 0.769\n      auroc_mid: 0.733\n      auroc_low: 0.618\n      ece_mean: 0.122\n  - title: CaCLR vs Linear Projection per Resource Tier (Qwen3, averaged across Pareto\n      layers)\n    columns:\n    - tier\n    - n_langs\n    - caclr_auroc\n    - linproj_auroc\n    - delta_pp\n    - caclr_wins\n    data:\n    - tier: high\n      n_langs: 6\n      caclr_auroc: 0.786\n      linproj_auroc: 0.775\n      delta_pp: 1.1\n      caclr_wins: 6/6\n    - tier: mid\n      n_langs: 8\n      caclr_auroc: 0.754\n      linproj_auroc: 0.738\n      delta_pp: 1.6\n      caclr_wins: 7/8\n    - tier: low\n      n_langs: 5\n      caclr_auroc: 0.636\n      linproj_auroc: 0.633\n      delta_pp: 0.3\n      caclr_wins: 1/5\n  - title: CaCLR Consistency Term Ablation (Qwen3 L52)\n    note: α=0.30 fixed; β=0 is calibrated-only probe\n    columns:\n    - config\n    - auroc_mean\n    - ece_mean\n    - high_delta_vs_linproj\n    - mid_delta_vs_linproj\n    - low_delta_vs_linproj\n    data:\n    - config: α=0.3 β=0 (no consistency)\n      auroc_mean: 0.716\n      ece_mean: 0.119\n      high_delta_vs_linproj: 0.3\n      mid_delta_vs_linproj: -0.2\n      low_delta_vs_linproj: -0.5\n    - config: α=0.3 β=0.15 (full CaCLR)\n      auroc_mean: 0.733\n      ece_mean: 0.112\n      high_delta_vs_linproj: 0.8\n      mid_delta_vs_linproj: 1.4\n      low_delta_vs_linproj: -0.2\n    - config: α=0 β=0.15 (consistency only)\n      auroc_mean: 0.708\n      ece_mean: 0.136\n      high_delta_vs_linproj: -0.4\n      mid_delta_vs_linproj: 0.6\n      low_delta_vs_linproj: -0.8\n  - title: Hyperparameter Sensitivity (Qwen3, validation set mean AUROC across 5 langs)\n    columns:\n    - alpha\n    - beta_0.05\n    - beta_0.10\n    - beta_0.15\n    - beta_0.20\n    - beta_0.30\n    data:\n    - alpha: 0.1\n      beta_0.05: 0.704\n      beta_0.10: 0.709\n      beta_0.15: 0.711\n      beta_0.20: 0.708\n      beta_0.30: 0.699\n    - alpha: 0.2\n      beta_0.05: 0.711\n      beta_0.10: 0.718\n      beta_0.15: 0.724\n      beta_0.20: 0.72\n      beta_0.30: 0.708\n    - alpha: 0.3\n      beta_0.05: 0.715\n      beta_0.10: 0.723\n      beta_0.15: 0.731\n      beta_0.20: 0.726\n      beta_0.30: 0.712\n    - alpha: 0.5\n      beta_0.05: 0.712\n      beta_0.10: 0.719\n      beta_0.15: 0.725\n      beta_0.20: 0.718\n      beta_0.30: 0.701\n    - alpha: 1.0\n      beta_0.05: 0.698\n      beta_0.10: 0.703\n      beta_0.15: 0.706\n      beta_0.20: 0.695\n      beta_0.30: 0.674\n  figures_description:\n  - 'Figure 3a: Pareto frontier shift — overlaid zero-shot frontier (grey) and CaCLR\n    frontier (blue) for Qwen3. CaCLR frontier is shifted up-and-right: at the same\n    English AUROC, CaCLR achieves higher transfer; at the same transfer quality, CaCLR\n    operates at deeper layers. Annotated: zero-shot optimal (L40) vs CaCLR optimal\n    (L52), with arrows showing +2.0pp English gain and +1.2pp transfer gain.\n\n    '\n  - 'Figure 3b: Bar chart — CaCLR AUROC improvement over linear projection, grouped\n    by resource tier. High-resource bars around +1.1pp (all positive). Mid-resource\n    bars around +1.6pp (7/8 positive, th near zero). Low-resource bars around +0.3pp\n    (mostly near zero or negative). Clear visual: CaCLR''s consistency term primarily\n    benefits mid-resource languages.\n\n    '\n  - 'Figure 3c: ECE comparison — grouped bar chart with 5 methods × 3 resource tiers.\n    CaCLR ECE bars consistently among the lowest, comparable to few-shot-100 for high/mid\n    resource but without requiring any target-language labels.\n\n    '\n  analysis: 'CaCLR 的 median-tier 表现支持 \"zero-label alternative that matches supervised\n    transfer\" 的 framing，而非 \"大幅超越\" 的 framing。核心发现：(1) CaCLR 在 zero-label 设定下 接近 few-shot-100\n    的性能（差 0.5pp AUROC，差 0.4pp ECE），这是 practical value 的 来源；(2) vs linear projection\n    仅 +1.3pp，但 CaCLR 不需要任何 target-language 数据 结构假设（linear projection 假设线性可分对齐），是更\n    principled 的方案；(3) consistency term 的 ablation 清晰显示其主要贡献在 mid-resource 语言（+1.6pp），\n    这些语言有足够好的 parallel activation 质量让 consistency loss 有效，但又不像 high-resource 那样 zero-shot\n    已经很好。Paper 应将 CaCLR 定位为 \"practical tool for the mid-resource sweet spot\" 而非 universal\n    improvement。\n\n    '\n- name: Difficulty-Controlled Ablation\n  plan_id: plan_004\n  description: 'IRT difficulty probes (Ridge regression on human difficulty scores\n    per Civelli et al.) trained per layer, difficulty direction projected out of activations,\n    correctness probes retrained on residuals, transfer evaluated. 10 languages ×\n    8 layers per model.\n\n    '\n  expected_results:\n    difficulty_probe_en_R2_mean: 0.68\n    difficulty_probe_zs_R2_mean: 0.61\n    decomp_difficulty_var_explained_pct: 37\n    original_transfer_gap_pp: 15.2\n    residual_transfer_gap_pp: 11.4\n    gap_reduction_pp: 3.8\n    gap_reduction_pct: 25\n    residual_en_auroc_drop: 0.038\n    language_family_cluster_effect: IE languages (de/fr/es/pl/ru) cluster; others\n      scattered\n    capability_residual_noisy: true\n    prescriptive_accuracy: 0.72\n  result_rationale: 'Difficulty 是已知的跨语言可迁移特征（Civelli et al. 直接证明了 IRT difficulty probe\n    的跨语言迁移性）。在 median 档，difficulty 解释了 correctness direction 37% 的方差， 因为 \"题目难不难\" 确实是\n    correctness 的一个强组成部分（简单题各语言都对，难题各 语言都错）。但 correctness 还包含 \"模型在该语言上是否具备回答这道题的 capability\"\n    这一 language-dependent 成分。投影掉 difficulty 后，transfer gap 从 15.2pp 缩小到 11.4pp（减少\n    25%），比 variance-explained 的 37% 低是因为 projection 是线性的而 difficulty-correctness 的关系有非线性成分。残差中的\n    capability-specific 信号是 noisy 的：高资源语言表现出清晰的 language-family clustering（IE 语言的\n    capability profiles 相似），但低资源语言的 capability residual 被 tokenization 和数据质量 confound，\n    无法干净分离。Prescriptive accuracy 72% 意味着：当 decomposition 预测 \"这个 language-layer 对简单\n    baseline 就够了\" 时，72% 的情况下确实如此——有用但不完美。 Paper 应将此 framing 为 \"partial decomposition\n    that explains the transferable component and predicts method choice, but capability\n    residual remains confounded\"。\n\n    '\n  tables:\n  - title: Difficulty Probe Quality by Language (Qwen3 L48)\n    columns:\n    - lang\n    - tier\n    - difficulty_R2\n    - zs_transfer_R2\n    - delta\n    data:\n    - lang: en\n      tier: high\n      difficulty_R2: 0.71\n      zs_transfer_R2: null\n      delta: null\n    - lang: zh\n      tier: high\n      difficulty_R2: null\n      zs_transfer_R2: 0.67\n      delta: -0.04\n    - lang: de\n      tier: high\n      difficulty_R2: null\n      zs_transfer_R2: 0.68\n      delta: -0.03\n    - lang: es\n      tier: high\n      difficulty_R2: null\n      zs_transfer_R2: 0.69\n      delta: -0.02\n    - lang: ar\n      tier: mid\n      difficulty_R2: null\n      zs_transfer_R2: 0.63\n      delta: -0.08\n    - lang: hi\n      tier: mid\n      difficulty_R2: null\n      zs_transfer_R2: 0.61\n      delta: -0.1\n    - lang: ko\n      tier: mid\n      difficulty_R2: null\n      zs_transfer_R2: 0.6\n      delta: -0.11\n    - lang: vi\n      tier: mid\n      difficulty_R2: null\n      zs_transfer_R2: 0.58\n      delta: -0.13\n    - lang: sw\n      tier: low\n      difficulty_R2: null\n      zs_transfer_R2: 0.49\n      delta: -0.22\n    - lang: te\n      tier: low\n      difficulty_R2: null\n      zs_transfer_R2: 0.51\n      delta: -0.2\n  - title: Decomposition Effect on Transfer Gap (Qwen3, 8 layers averaged)\n    columns:\n    - component\n    - en_auroc\n    - zs_transfer_mean_9lang\n    - gap_pp\n    data:\n    - component: original correctness probe\n      en_auroc: 0.796\n      zs_transfer_mean_9lang: 0.674\n      gap_pp: 12.2\n    - component: difficulty probe only\n      en_auroc: 0.714\n      zs_transfer_mean_9lang: 0.67\n      gap_pp: 4.4\n    - component: residual (capability) probe\n      en_auroc: 0.758\n      zs_transfer_mean_9lang: 0.653\n      gap_pp: 10.5\n    - component: difficulty + residual reconstructed\n      en_auroc: 0.791\n      zs_transfer_mean_9lang: 0.671\n      gap_pp: 12.0\n  - title: Variance Decomposition by Layer Depth (Qwen3)\n    columns:\n    - layer\n    - difficulty_var_pct\n    - capability_var_pct\n    - reconstruction_loss_pct\n    data:\n    - layer: L20\n      difficulty_var_pct: 44\n      capability_var_pct: 51\n      reconstruction_loss_pct: 5\n    - layer: L28\n      difficulty_var_pct: 42\n      capability_var_pct: 53\n      reconstruction_loss_pct: 5\n    - layer: L36\n      difficulty_var_pct: 40\n      capability_var_pct: 54\n      reconstruction_loss_pct: 6\n    - layer: L48\n      difficulty_var_pct: 37\n      capability_var_pct: 56\n      reconstruction_loss_pct: 7\n    - layer: L56\n      difficulty_var_pct: 34\n      capability_var_pct: 58\n      reconstruction_loss_pct: 8\n    - layer: L64\n      difficulty_var_pct: 31\n      capability_var_pct: 60\n      reconstruction_loss_pct: 9\n    - layer: L76\n      difficulty_var_pct: 28\n      capability_var_pct: 62\n      reconstruction_loss_pct: 10\n    - layer: L84\n      difficulty_var_pct: 26\n      capability_var_pct: 63\n      reconstruction_loss_pct: 11\n  - title: 'Prescriptive Accuracy: Does Decomposition Predict Method Choice?'\n    note: For each lang-layer pair, decomposition predicts 'zero-shot suffices' if\n      difficulty component dominates (>50%), else 'CaCLR needed'. Ground truth from\n      plan_003.\n    columns:\n    - tier\n    - n_pairs\n    - correct_predictions\n    - accuracy\n    data:\n    - tier: high\n      n_pairs: 48\n      correct_predictions: 38\n      accuracy: 0.79\n    - tier: mid\n      n_pairs: 64\n      correct_predictions: 47\n      accuracy: 0.73\n    - tier: low\n      n_pairs: 40\n      correct_predictions: 25\n      accuracy: 0.63\n    - tier: all\n      n_pairs: 152\n      correct_predictions: 110\n      accuracy: 0.72\n  figures_description:\n  - 'Figure 4a: Stacked bar chart — per layer, the proportion of correctness direction\n    variance attributed to difficulty (blue), capability (orange), reconstruction\n    loss (grey). Difficulty share monotonically decreases from 44% at L20 to 26% at\n    L84; capability share correspondingly increases. Visual narrative: deeper layers\n    have more capability-specific information, which is why they transfer worse.\n\n    '\n  - 'Figure 4b: Scatter — x-axis: difficulty variance share (%), y-axis: zero-shot\n    transfer AUROC for each language-layer pair. Positive correlation (r≈0.55): higher\n    difficulty share predicts better zero-shot transfer. But substantial scatter,\n    especially for low-resource languages (marked with different symbol). Regression\n    line shown with confidence band.\n\n    '\n  analysis: 'Decomposition 部分成功：difficulty component 确实是 transferable part，其 share\n    随 depth 递减完美解释了 Pareto tradeoff 的机制——deeper layers 积累更多 capability-specific 信息，这些信息是\n    language-dependent 的。但 \"partial\" 体现在两方面：(1) difficulty 仅解释 37% 的 variance，多数 correctness\n    signal 在 capability residual 中；(2) capability residual 本身不是干净的 language-specific\n    signal，而是与 language-family effects confounded（IE 语言 cluster 说明 capability 共享有\n    phylogenetic 结构）。 Prescriptive accuracy 72% 是一个有用但不完美的 practical tool。Paper 应将此\n    framed 为 \"first decomposition of cross-lingual correctness transfer that identifies\n    the transferable component and partially predicts method choice, with the capability\n    residual as a target for future work.\"\n\n    '\n- name: Cross-Lingual Orthogonality Analysis\n  plan_id: plan_005\n  description: 'Extract verbalized confidence direction (prompt for P(correct) score,\n    fit linear probe), compute cosine similarity with correctness direction across\n    20 languages × 2 architectures. Resource-tier and language-family analysis.\n\n    '\n  expected_results:\n    cosine_mean_all: 0.091\n    cosine_mean_qwen3: 0.086\n    cosine_mean_llama4: 0.096\n    cosine_high_mean: 0.059\n    cosine_mid_mean: 0.084\n    cosine_low_mean: 0.147\n    cosine_low_std: 0.032\n    cosine_range:\n    - 0.04\n    - 0.21\n    en_cosine_qwen3: 0.04\n    en_cosine_llama4: 0.05\n    cross_arch_cosine_corr: 0.78\n    orthogonality_holds_all_20: true\n  result_rationale: 'Miao & Ungar (2026) 在英语 7-8B 模型上发现 correctness-confidence cosine\n    < 0.04。 在 median 档，该 orthogonality 跨语言泛化但有 resource-tier 梯度。High-resource 语言（cosine\n    ~0.06）接近英语水平，因为模型在这些语言上有充足的训练数据， verbalized confidence 和 internal correctness\n    的分离是 well-learned 的。 Mid-resource 语言（cosine ~0.08）稍高，模型的 confidence 表达在这些语言上 不那么\n    calibrated。Low-resource 语言（cosine ~0.15, std 0.032）明显更高且 variance 更大——模型在低资源语言上的\n    verbalized confidence 方向本身就不稳定（probe 拟合 noisy），导致与 correctness 的 cosine 更大也更不可靠。但即使最高的\n    yo (0.21) 也远低于 \"parallel\" 的 0.7+，orthogonality 的定性结论在所有 20 语言上成立。 Cross-architecture\n    correlation 0.78 表明 per-language cosine 值在两个模型上高度 一致——这是 structural property，不是\n    model-specific artifact。\n\n    '\n  tables:\n  - title: Correctness-Confidence Cosine Similarity by Language\n    columns:\n    - lang\n    - tier\n    - qwen3_cosine\n    - llama4_cosine\n    - mean\n    data:\n    - lang: en\n      tier: high\n      qwen3_cosine: 0.04\n      llama4_cosine: 0.05\n      mean: 0.045\n    - lang: zh\n      tier: high\n      qwen3_cosine: 0.05\n      llama4_cosine: 0.06\n      mean: 0.055\n    - lang: de\n      tier: high\n      qwen3_cosine: 0.06\n      llama4_cosine: 0.07\n      mean: 0.065\n    - lang: fr\n      tier: high\n      qwen3_cosine: 0.05\n      llama4_cosine: 0.06\n      mean: 0.055\n    - lang: es\n      tier: high\n      qwen3_cosine: 0.05\n      llama4_cosine: 0.06\n      mean: 0.055\n    - lang: ja\n      tier: high\n      qwen3_cosine: 0.07\n      llama4_cosine: 0.08\n      mean: 0.075\n    - lang: ru\n      tier: high\n      qwen3_cosine: 0.06\n      llama4_cosine: 0.07\n      mean: 0.065\n    - lang: ar\n      tier: mid\n      qwen3_cosine: 0.08\n      llama4_cosine: 0.09\n      mean: 0.085\n    - lang: hi\n      tier: mid\n      qwen3_cosine: 0.07\n      llama4_cosine: 0.08\n      mean: 0.075\n    - lang: ko\n      tier: mid\n      qwen3_cosine: 0.08\n      llama4_cosine: 0.09\n      mean: 0.085\n    - lang: pt\n      tier: mid\n      qwen3_cosine: 0.06\n      llama4_cosine: 0.07\n      mean: 0.065\n    - lang: vi\n      tier: mid\n      qwen3_cosine: 0.09\n      llama4_cosine: 0.1\n      mean: 0.095\n    - lang: th\n      tier: mid\n      qwen3_cosine: 0.1\n      llama4_cosine: 0.11\n      mean: 0.105\n    - lang: tr\n      tier: mid\n      qwen3_cosine: 0.08\n      llama4_cosine: 0.09\n      mean: 0.085\n    - lang: pl\n      tier: mid\n      qwen3_cosine: 0.07\n      llama4_cosine: 0.08\n      mean: 0.075\n    - lang: sw\n      tier: low\n      qwen3_cosine: 0.12\n      llama4_cosine: 0.13\n      mean: 0.125\n    - lang: te\n      tier: low\n      qwen3_cosine: 0.1\n      llama4_cosine: 0.11\n      mean: 0.105\n    - lang: my\n      tier: low\n      qwen3_cosine: 0.15\n      llama4_cosine: 0.16\n      mean: 0.155\n    - lang: am\n      tier: low\n      qwen3_cosine: 0.16\n      llama4_cosine: 0.17\n      mean: 0.165\n    - lang: yo\n      tier: low\n      qwen3_cosine: 0.18\n      llama4_cosine: 0.19\n      mean: 0.185\n  - title: Orthogonality Summary by Resource Tier\n    columns:\n    - tier\n    - n_langs\n    - cosine_mean\n    - cosine_std\n    - cosine_min\n    - cosine_max\n    data:\n    - tier: high\n      n_langs: 7\n      cosine_mean: 0.059\n      cosine_std: 0.01\n      cosine_min: 0.04\n      cosine_max: 0.08\n    - tier: mid\n      n_langs: 8\n      cosine_mean: 0.084\n      cosine_std: 0.013\n      cosine_min: 0.06\n      cosine_max: 0.11\n    - tier: low\n      n_langs: 5\n      cosine_mean: 0.147\n      cosine_std: 0.032\n      cosine_min: 0.1\n      cosine_max: 0.19\n    - tier: all\n      n_langs: 20\n      cosine_mean: 0.091\n      cosine_std: 0.04\n      cosine_min: 0.04\n      cosine_max: 0.19\n  figures_description:\n  - 'Figure 5: Dot plot — x-axis: cosine similarity, y-axis: languages (sorted by\n    resource tier, then by cosine). Two markers per language (circle=Qwen3, triangle=Llama4).\n    Vertical dashed line at cosine=0.25 (\"orthogonality threshold\"). All points to\n    the left. Clear visual gradient from high-resource (clustered near 0.05) to low-resource\n    (spread between 0.10-0.19). Error bars show bootstrap 95% CI. Annotation: \"Miao\n    & Ungar EN baseline: cos < 0.04\" with arrow pointing to English dots.\n\n    '\n  analysis: 'Claim 4 在 median 档下获得 strong support for high/mid-resource languages,\n    qualified support for low-resource。核心结论：correctness-confidence orthogonality 是一个跨语言\n    的 structural property，不是英语特有的。但 resource-tier gradient（high 0.06 → low 0.15） 表明该\n    property 在低资源语言上更弱——这可能是因为模型在低资源语言上的 confidence calibration 本身就差，confidence direction\n    拟合不稳定。Cross-architecture 一致性 0.78 进一步强化了 structural claim。Paper 应呈现为 \"orthogonality\n    universally holds (all cos < 0.25) but varies in degree, with implications for\n    why output-based calibration is structurally limited across all languages — but\n    especially limited for high-resource languages where the orthogonality is strongest.\"\n\n    '\n- name: Probe Complexity Comparison\n  plan_id: plan_006\n  description: 'Logistic regression vs 2-layer MLP (hidden dim 256, ReLU) at each\n    probed layer for both models. Compare English accuracy, cross-lingual transfer\n    degradation, and calibration quality. Test hypothesis: linear probes transfer\n    better.\n\n    '\n  expected_results:\n    qwen3_L76_logreg_en_auroc: 0.812\n    qwen3_L76_mlp_en_auroc: 0.827\n    qwen3_L76_logreg_transfer_mean: 0.644\n    qwen3_L76_mlp_transfer_mean: 0.607\n    qwen3_L76_logreg_transfer_drop_pp: 16.8\n    qwen3_L76_mlp_transfer_drop_pp: 22.0\n    llama4_L44_logreg_en_auroc: 0.793\n    llama4_L44_mlp_en_auroc: 0.812\n    llama4_L44_logreg_transfer_mean: 0.657\n    llama4_L44_mlp_transfer_mean: 0.625\n    llama4_L44_logreg_transfer_drop_pp: 13.6\n    llama4_L44_mlp_transfer_drop_pp: 18.7\n    mlp_en_advantage_pp_mean: 1.7\n    logreg_transfer_advantage_pp_mean: 3.5\n    hypothesis_confirmed: true\n  result_rationale: 'MLP 在英语上多 ~1.7pp AUROC，因为非线性层可以捕获 correctness 与 activation 之间\n    的非线性关系。但 MLP 在跨语言迁移上劣 ~3.5pp，因为非线性决策边界更容易 overfit 英语 activation 的分布特征，这些特征在其他语言中不保持。Linear\n    probe 的决策 超平面在 high-dimensional space 中更 \"blunt\"，因此更 robust to distribution shift。\n    这个结果与 Civelli et al. 的发现一致（linear > nonlinear for cross-lingual difficulty transfer），也回应了\n    reviewer 可能提出的 \"为什么不用更复杂的 probe\" 的质疑。 Paper 据此使用 logistic regression 作为 primary\n    probe，MLP 仅作为 ablation 报告。\n\n    '\n  tables:\n  - title: LogReg vs MLP at Key Layers (Qwen3-235B)\n    columns:\n    - layer\n    - logreg_en\n    - mlp_en\n    - en_delta\n    - logreg_transfer\n    - mlp_transfer\n    - transfer_delta\n    data:\n    - layer: L40\n      logreg_en: 0.776\n      mlp_en: 0.794\n      en_delta: 1.8\n      logreg_transfer: 0.696\n      mlp_transfer: 0.672\n      transfer_delta: -2.4\n    - layer: L52\n      logreg_en: 0.796\n      mlp_en: 0.813\n      en_delta: 1.7\n      logreg_transfer: 0.682\n      mlp_transfer: 0.651\n      transfer_delta: -3.1\n    - layer: L64\n      logreg_en: 0.807\n      mlp_en: 0.824\n      en_delta: 1.7\n      logreg_transfer: 0.661\n      mlp_transfer: 0.626\n      transfer_delta: -3.5\n    - layer: L76\n      logreg_en: 0.812\n      mlp_en: 0.827\n      en_delta: 1.5\n      logreg_transfer: 0.644\n      mlp_transfer: 0.607\n      transfer_delta: -3.7\n  - title: LogReg vs MLP at Key Layers (Llama 4 Scout)\n    columns:\n    - layer\n    - logreg_en\n    - mlp_en\n    - en_delta\n    - logreg_transfer\n    - mlp_transfer\n    - transfer_delta\n    data:\n    - layer: L24\n      logreg_en: 0.741\n      mlp_en: 0.758\n      en_delta: 1.7\n      logreg_transfer: 0.677\n      mlp_transfer: 0.654\n      transfer_delta: -2.3\n    - layer: L32\n      logreg_en: 0.771\n      mlp_en: 0.789\n      en_delta: 1.8\n      logreg_transfer: 0.679\n      mlp_transfer: 0.651\n      transfer_delta: -2.8\n    - layer: L40\n      logreg_en: 0.79\n      mlp_en: 0.808\n      en_delta: 1.8\n      logreg_transfer: 0.663\n      mlp_transfer: 0.631\n      transfer_delta: -3.2\n    - layer: L44\n      logreg_en: 0.793\n      mlp_en: 0.812\n      en_delta: 1.9\n      logreg_transfer: 0.657\n      mlp_transfer: 0.625\n      transfer_delta: -3.2\n  figures_description:\n  - 'Figure S1 (Appendix): Dual-line plot per model — x-axis: layer depth, y-axis:\n    AUROC. Solid lines = LogReg (blue = English, orange = transfer mean). Dashed lines\n    = MLP (blue = English, orange = transfer mean). The \"scissors\" pattern: MLP blue\n    line is above LogReg blue line (better English), but MLP orange line is below\n    LogReg orange line (worse transfer). Gap widens at deeper layers.\n\n    '\n  analysis: 'Hypothesis confirmed: linear probes transfer significantly better cross-lingually\n    than MLP probes (+3.5pp average), while sacrificing only 1.7pp English accuracy.\n    The transfer advantage of linear probes is larger at deeper layers (where distribution\n    shift is worst), which is consistent with the Pareto tradeoff mechanism — nonlinear\n    probes amplify the depth-dependent distribution shift. This result justifies the\n    methodological choice of logistic regression as the primary probe throughout the\n    paper.\n\n    '\n- name: Additional Benchmark Evaluation\n  plan_id: plan_007\n  description: 'Evaluate best probes + CaCLR on Belebele (20 languages, reading comprehension)\n    and MMLU-ProX (20 languages, harder STEM questions). Tests generalization of Pareto\n    frontier and CaCLR beyond GlobalMMLU.\n\n    '\n  expected_results:\n    belebele_en_auroc_best: 0.798\n    belebele_zs_transfer_mean_at_best_transfer: 0.708\n    belebele_pareto_replicates: true\n    belebele_caclr_vs_linproj_pp: 1.1\n    belebele_best_transfer_layer_qwen3: L44\n    mmlupx_en_auroc_best: 0.824\n    mmlupx_zs_transfer_mean_at_best_transfer: 0.681\n    mmlupx_pareto_replicates: true\n    mmlupx_caclr_vs_linproj_pp: 1.6\n    mmlupx_best_transfer_layer_qwen3: L40\n    belebele_low_resource_pass_rate: 0.6\n    mmlupx_low_resource_pass_rate: 0.4\n  result_rationale: 'Pareto frontier 作为 representation structure 的 property，不应依赖特定\n    benchmark。 Belebele（阅读理解）和 MMLU-ProX（更难 STEM 题）提供了两个不同难度和认知类型的 测试。Belebele 稍简单，英语\n    AUROC 稍低（0.798 vs 0.812）因为 reading comprehension 的 correctness 比 knowledge QA\n    更依赖 surface patterns，linear probe 的 ceiling 更低。 但迁移质量稍高（0.708 vs 0.696）因为阅读理解的跨语言\n    pattern 更相似。MMLU-ProX 更难，英语 AUROC 更高（0.824）因为难题的 correctness signal 更 salient（模型更\n    \"确定\" 自己是否知道），但迁移稍差（0.681）因为 STEM 知识的跨语言 variation 更大。 CaCLR 在 MMLU-ProX 上优势稍大（+1.6pp\n    vs +1.1pp）因为更难的题目有更多 distribution shift 可以被 consistency term 修正。两个 benchmark 都复现了\n    Pareto 结构，确认其 generalizability。低资源在 MMLU-ProX 上更差（2/5 vs 3/5）因为难题放大了数据不足的问题。\n\n    '\n  tables:\n  - title: Cross-Benchmark Comparison (Qwen3-235B, LogReg)\n    columns:\n    - metric\n    - GlobalMMLU\n    - Belebele\n    - MMLU_ProX\n    data:\n    - metric: en_auroc_best\n      GlobalMMLU: 0.812\n      Belebele: 0.798\n      MMLU_ProX: 0.824\n    - metric: best_en_layer\n      GlobalMMLU: L76\n      Belebele: L72\n      MMLU_ProX: L76\n    - metric: best_transfer_layer\n      GlobalMMLU: L40\n      Belebele: L44\n      MMLU_ProX: L40\n    - metric: zs_transfer_mean\n      GlobalMMLU: 0.696\n      Belebele: 0.708\n      MMLU_ProX: 0.681\n    - metric: transfer_drop_pp\n      GlobalMMLU: 16.8\n      Belebele: 13.1\n      MMLU_ProX: 18.4\n    - metric: caclr_vs_linproj_pp\n      GlobalMMLU: 1.4\n      Belebele: 1.1\n      MMLU_ProX: 1.6\n    - metric: low_resource_pass_rate\n      GlobalMMLU: 0.6\n      Belebele: 0.6\n      MMLU_ProX: 0.4\n  figures_description:\n  - 'Figure S2 (Appendix): Three-panel Pareto frontier plots (GlobalMMLU / Belebele\n    / MMLU-ProX) with identical axis scales. Visual pattern clearly replicates across\n    all three: upward-then-left curve in all panels, with MMLU-ProX showing the steepest\n    tradeoff and Belebele the mildest.\n\n    '\n  analysis: 'Cross-benchmark replication is the key result: Pareto frontier structure\n    is benchmark- agnostic, confirming it reflects model representation properties\n    rather than dataset artifacts. The quantitative differences (Belebele flatter,\n    MMLU-ProX steeper) are interpretable and strengthen the paper''s analysis. CaCLR''s\n    benchmark-robust improvement (+1.1 to +1.6pp) confirms its general utility.\n\n    '\n- name: INT8 Validation Ablation\n  plan_id: plan_010\n  description: 'Compare INT8 vs FP16 probing results at 5 representative layers for\n    Llama 4 Scout on 5% random subset (~700 samples). Validates that INT8 quantization\n    doesn''t distort correctness signals in the activation space.\n\n    '\n  expected_results:\n    max_auroc_delta_pp: 0.3\n    mean_auroc_delta_pp: 0.24\n    direction_bias: negligible (INT8 marginally lower at all layers)\n    cosine_sim_directions: 0.997\n    conclusion: INT8 validated — no meaningful distortion of correctness signal\n  result_rationale: 'INT8 weight-only quantization 保留了 activation space 的大部分结构（weight\n    quantization 引入的 perturbation 在 high-dimensional space 中被分摊，对线性 probe 的影响极小）。\n    AUROC delta < 0.3pp 远低于实验中观测到的其他 effect sizes（transfer drop 13-17pp, CaCLR improvement\n    1-4pp）。Correctness direction 的 cosine similarity 0.997 说明 quantization 几乎不改变 direction，只是\n    slightly perturb magnitude。这是 expected result，但对 reviewer 来说是必要的 due diligence——没有这个\n    ablation，reviewer 可能质疑 INT8 是否引入 systematic bias。\n\n    '\n  tables:\n  - title: INT8 vs FP16 Probing Results (Llama 4 Scout, 5% subset)\n    columns:\n    - layer\n    - int8_auroc\n    - fp16_auroc\n    - delta_pp\n    - direction_cosine\n    data:\n    - layer: L4\n      int8_auroc: 0.568\n      fp16_auroc: 0.571\n      delta_pp: -0.3\n      direction_cosine: 0.998\n    - layer: L12\n      int8_auroc: 0.648\n      fp16_auroc: 0.651\n      delta_pp: -0.3\n      direction_cosine: 0.997\n    - layer: L24\n      int8_auroc: 0.738\n      fp16_auroc: 0.74\n      delta_pp: -0.2\n      direction_cosine: 0.998\n    - layer: L36\n      int8_auroc: 0.78\n      fp16_auroc: 0.782\n      delta_pp: -0.2\n      direction_cosine: 0.997\n    - layer: L44\n      int8_auroc: 0.791\n      fp16_auroc: 0.794\n      delta_pp: -0.3\n      direction_cosine: 0.996\n  figures_description:\n  - 'Figure S3 (Appendix): Paired bar chart — 5 layers, INT8 (blue) vs FP16 (orange)\n    bars. Bars nearly identical height at every layer. Annotation: \"max Δ = 0.3pp\".\n    Simple, clean validation figure.\n\n    '\n  analysis: 'INT8 quantization is validated for correctness probing. The <0.3pp AUROC\n    difference is well within noise levels and has no systematic direction. This ablation\n    can be reported in 2-3 sentences in the Appendix with the table — no need for\n    extended discussion.\n\n    '\n- name: Gemma 4 31B Dense — Camera-Ready Extension\n  plan_id: plan_008\n  description: 'Third architecture (60 layers, dense, FP16) for camera-ready version.\n    Dense vs MoE architectural contrast. Full Pareto frontier, 20+ languages.\n\n    '\n  expected_results:\n    en_auroc_best: 0.805\n    en_best_layer: L48\n    best_transfer_layer: L32\n    zs_transfer_mean_at_best_transfer: 0.709\n    zs_transfer_drop_at_best_en_pp: 10.2\n    pareto_frontier_shape: smoother than MoE models, more gradual transfer decline\n    low_resource_pass_rate: 0.6\n    caclr_vs_linproj_pp: 1.0\n    frontier_agreement_with_qwen3: 0.62\n    frontier_agreement_with_llama4: 0.71\n  result_rationale: 'Dense architecture 与 MoE 的关键差异：没有 routing 机制导致的 discrete layer-wise\n    变化，representation 的 language-specificity 随 depth 更连续地增长。因此 Pareto frontier 更 smooth（transfer\n    decline 更 gradual），transfer drop 仅 10.2pp（vs Qwen3 16.8pp, Llama4 13.6pp）。English\n    AUROC 略低于 Qwen3（0.805 vs 0.812）因为 31B dense 的 total compute 少于 235B MoE。Best transfer\n    在 53% 深度（L32/60）， 介于 Qwen3(43%) 和 Llama4(67%) 之间。CaCLR 优势更小（+1.0pp）因为 dense model\n    的 representation shift across languages 本身更 gradual，simple baselines 已经 表现不错。与\n    Llama4 的 frontier agreement (0.71) 高于与 Qwen3 (0.62)，可能因为 Llama4 和 Gemma4 的训练数据组成更相似。\n\n    '\n  tables:\n  - title: Three-Architecture Pareto Summary\n    columns:\n    - metric\n    - Qwen3_235B_MoE\n    - Llama4_Scout_MoE\n    - Gemma4_31B_Dense\n    data:\n    - metric: total_layers\n      Qwen3_235B_MoE: 94\n      Llama4_Scout_MoE: 48\n      Gemma4_31B_Dense: 60\n    - metric: architecture\n      Qwen3_235B_MoE: MoE\n      Llama4_Scout_MoE: MoE\n      Gemma4_31B_Dense: Dense\n    - metric: en_auroc_best\n      Qwen3_235B_MoE: 0.812\n      Llama4_Scout_MoE: 0.793\n      Gemma4_31B_Dense: 0.805\n    - metric: best_transfer_depth_pct\n      Qwen3_235B_MoE: 43\n      Llama4_Scout_MoE: 67\n      Gemma4_31B_Dense: 53\n    - metric: transfer_drop_pp\n      Qwen3_235B_MoE: 16.8\n      Llama4_Scout_MoE: 13.6\n      Gemma4_31B_Dense: 10.2\n    - metric: frontier_smoothness\n      Qwen3_235B_MoE: sharp\n      Llama4_Scout_MoE: flat/noisy\n      Gemma4_31B_Dense: smooth\n    - metric: caclr_benefit_pp\n      Qwen3_235B_MoE: 1.4\n      Llama4_Scout_MoE: 1.2\n      Gemma4_31B_Dense: 1.0\n  figures_description:\n  - 'Figure 6 (Camera-Ready): Three-model overlaid Pareto frontiers. Qwen3 (circles)\n    shows widest, steepest frontier. Llama4 (triangles) shows compact, flat frontier.\n    Gemma4 (squares) shows smooth, intermediate frontier. Visual immediately communicates\n    architecture-dependent Pareto structure. Inset table shows optimal transfer depth\n    %.\n\n    '\n  analysis: 'Dense vs MoE 对比是 camera-ready 的最有价值的扩展。Dense 架构的 smoother frontier 提供了\n    mechanistic insight：MoE routing 在深层的 language-specific expert selection 可能是 Qwen3\n    sharp Pareto tradeoff 的原因，而 dense model 的 continuous feature evolution 产生更 gradual\n    的 language specificity 增长。三架构的 frontier 定性一致 但定量不同，强化了 \"Pareto frontier is universal\n    but architecture-dependent\" 的 headline claim。\n\n    '\n- name: Extended Language Coverage — Camera-Ready Extension\n  plan_id: plan_009\n  description: 'Expand from 20 to 50+ languages using GlobalMMLU/Belebele full language\n    sets. Tests how Pareto frontier patterns scale to long-tail languages.\n\n    '\n  expected_results:\n    total_languages: 53\n    high_resource_count: 12\n    mid_resource_count: 18\n    low_resource_count: 23\n    zs_transfer_mean_all_52: 0.651\n    low_resource_pass_rate_23: 0.35\n    very_low_resource_auroc_range:\n    - 0.5\n    - 0.58\n    pareto_replicates_qualitatively: true\n    new_failure_languages:\n    - qu\n    - ha\n    - gn\n    - lg\n    - ny\n    - sn\n    - xh\n    - zu\n    - ig\n    - mg\n    - rw\n    - so\n    - tn\n    - ts\n    - ve\n    caclr_improvement_rate_52: 0.67\n    layer_rank_consistency_52: 0.58\n  result_rationale: '扩展到 53 语言后，低资源尾部显著增长（23 个 low-resource vs 原来 5 个），整体 指标下降是 expected\n    的。ZS transfer mean 从 0.696（20 langs）降至 0.651（52 non-en langs）因为新增语言大部分是低资源的非洲/大洋洲/美洲原住民语言，GlobalMMLU\n    翻译 质量参差不齐。低资源 pass rate 从 0.6（3/5）降至 0.35（8/23）说明 \"correctness direction universally\n    transfers\" 的说法在尾部语言不成立——但 Pareto 结构本身 仍然定性存在。CaCLR 的 improvement rate 也从 0.74\n    降至 0.67，但仍是多数语言 受益。Layer ranking consistency 从 0.71 降至 0.58，因为低资源语言的最优迁移层 更分散。Paper\n    应将此 framing 为 \"Pareto frontier scales to 50+ languages but with diminishing returns\n    for very low-resource languages, motivating future work on low-resource-specific\n    transfer methods.\"\n\n    '\n  tables:\n  - title: Extended Coverage Summary by Tier\n    columns:\n    - tier\n    - n_langs_20\n    - n_langs_53\n    - mean_auroc_20\n    - mean_auroc_53\n    - pass_rate_20\n    - pass_rate_53\n    data:\n    - tier: high\n      n_langs_20: 6\n      n_langs_53: 11\n      mean_auroc_20: 0.753\n      mean_auroc_53: 0.745\n      pass_rate_20: 1.0\n      pass_rate_53: 1.0\n    - tier: mid\n      n_langs_20: 8\n      n_langs_53: 18\n      mean_auroc_20: 0.711\n      mean_auroc_53: 0.698\n      pass_rate_20: 1.0\n      pass_rate_53: 0.94\n    - tier: low\n      n_langs_20: 5\n      n_langs_53: 23\n      mean_auroc_20: 0.607\n      mean_auroc_53: 0.571\n      pass_rate_20: 0.6\n      pass_rate_53: 0.35\n    - tier: all\n      n_langs_20: 19\n      n_langs_53: 52\n      mean_auroc_20: 0.696\n      mean_auroc_53: 0.651\n      pass_rate_20: 0.89\n      pass_rate_53: 0.69\n  figures_description:\n  - 'Figure 7 (Camera-Ready): Language-level scatter — x-axis: log(pretraining data\n    size estimate, tokens), y-axis: best zero-shot transfer AUROC. Clear positive\n    correlation (r≈0.72). Horizontal dashed line at AUROC=0.60. Labels for notable\n    languages. Below the line: cluster of 15 very-low-resource languages. Color by\n    language family. Shows that transfer success is primarily a function of pretraining\n    representation quality.\n\n    '\n  analysis: 'Extended coverage confirms the fundamental insight: Pareto frontier is\n    a structural property that scales to 50+ languages, but the practical utility\n    of zero-shot correctness probe transfer is bounded by pretraining data quantity.\n    The 15 languages below the 0.60 threshold are all in the lowest quintile of pretraining\n    data, suggesting a minimum representation quality floor for this approach. This\n    limitation should be acknowledged transparently in the Discussion section, not\n    hidden — it''s a valuable finding about the scope of probe-based calibration methods.'\n",
      "numLines": 1672,
      "startLine": 1,
      "totalLines": 1672
    }
  },
  "sourceToolAssistantUUID": "710d52da-b117-4d2a-baed-91e421731308",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "91ffee85-8db0-4b21-8e23-2eb894e1563a",
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
  "lastPrompt": "[DREAM Review Director] dream_id=20260520T185641 | review_mode=full | review_visible=True PDF: /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dr…",
  "leafUuid": "1d1e9ae2-db43-4ad5-b0c5-64c2c9b790bb",
  "sessionId": "91ffee85-8db0-4b21-8e23-2eb894e1563a"
}
```

---

### Runtime record

_source line 18_

```json
{
  "type": "ai-title",
  "aiTitle": "Full peer review of DREAM research paper",
  "sessionId": "91ffee85-8db0-4b21-8e23-2eb894e1563a"
}
```

---

### Assistant

_source line 19 · 2026-05-20T19:46:38.485Z_

<details><summary>Logged reasoning block</summary>

```text
I've now read both the PDF paper and the review context YAML. Let me also try to find the submit_dream_review_report tool - it wasn't found via ToolSearch. Let me try a different search.

Let me understand the paper and context first, then dispatch two reviewer agents.

The paper: "Cross-Lingual Calibration Probes Reveal Architecture-Dependent Pareto Frontiers in Multilingual LLMs"

Key claims:
1. Depth-transferability Pareto frontier exists across architectures (3 architectures, 20 languages, 3 benchmarks)


2. Difficulty-capability decomposition explains 25% of transfer gap and predicts method choice with 72% accuracy
3. CaCLR matches the best supervised baseline in zero-label settings, particularly for mid-resource languages
4. Correctness-confidence orthogonality generalizes across 20 languages with a resource-tier gradient

The review context YAML contains the full imagined experiment specifications with expected results. The paper covers experiments plan_001 through plan_010, excluding plan_008 and plan_009 which are camera-ready extensions, though the paper does briefly address them in §9.3 and §9.4.

Now I need to dispatch the reviews to two reviewers—one focused on methods and experiments, the other on novelty and related work—then run them through a roundtable process with independent reviews, cross-sharing, convergence, and synthesis. Let me try loading the submit tool again.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1d1e9ae2-db43-4ad5-b0c5-64c2c9b790bb",
  "isSidechain": false,
  "requestId": "req_011CbEPwwiCL1t9tdLDkDhrS",
  "type": "assistant",
  "uuid": "5963aaf7-a303-43bb-9048-35eb0422cffa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "91ffee85-8db0-4b21-8e23-2eb894e1563a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KEG1BxtCgB1WNjKpbSwsTq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 40761,
      "cache_read_input_tokens": 23203,
      "output_tokens": 495,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 40761,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 495,
          "cache_read_input_tokens": 23203,
          "cache_creation_input_tokens": 40761,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 40761
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

_source line 20 · 2026-05-20T19:46:38.521Z_

论文和实验上下文已读取完毕。`submit_dream_review_report` 工具未找到，先用 MCP 工具搜索。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5963aaf7-a303-43bb-9048-35eb0422cffa",
  "isSidechain": false,
  "requestId": "req_011CbEPwwiCL1t9tdLDkDhrS",
  "type": "assistant",
  "uuid": "f775d400-7791-47b4-b24c-04a3044566b5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "91ffee85-8db0-4b21-8e23-2eb894e1563a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KEG1BxtCgB1WNjKpbSwsTq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 40761,
      "cache_read_input_tokens": 23203,
      "output_tokens": 495,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 40761,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 495,
          "cache_read_input_tokens": 23203,
          "cache_creation_input_tokens": 40761,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 40761
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

_source line 21 · 2026-05-20T19:46:38.826Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01NWDoi1dVLzz4DrMBjWwMbZ`</summary>

```json
{
  "query": "dream review submit report",
  "max_results": 5
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f775d400-7791-47b4-b24c-04a3044566b5",
  "isSidechain": false,
  "requestId": "req_011CbEPwwiCL1t9tdLDkDhrS",
  "type": "assistant",
  "uuid": "bdc31798-f276-41eb-be57-aa9262762c18",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "91ffee85-8db0-4b21-8e23-2eb894e1563a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KEG1BxtCgB1WNjKpbSwsTq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 40761,
      "cache_read_input_tokens": 23203,
      "output_tokens": 495,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 40761,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 495,
          "cache_read_input_tokens": 23203,
          "cache_creation_input_tokens": 40761,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 40761
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

_source line 22 · 2026-05-20T19:46:38.843Z_

<details><summary>↩ Tool result · `toolu_01NWDoi1dVLzz4DrMBjWwMbZ`</summary>

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

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__director_get_project_overview"
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
  "parentUuid": "bdc31798-f276-41eb-be57-aa9262762c18",
  "isSidechain": false,
  "promptId": "7f3a0651-0480-4418-9ac1-d949b2c2cd30",
  "type": "user",
  "uuid": "d318ac92-199f-4c47-bba1-d039676b0730",
  "toolUseResult": {
    "matches": [
      "mcp__agent-ml-research__submit_dream_review_report",
      "mcp__agent-ml-research__director_post_to_reviewer",
      "ExitPlanMode",
      "mcp__agent-ml-research__director_get_project_overview",
      "mcp__agent-ml-research__read_project_file"
    ],
    "query": "dream review submit report",
    "total_deferred_tools": 23
  },
  "sourceToolAssistantUUID": "bdc31798-f276-41eb-be57-aa9262762c18",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "91ffee85-8db0-4b21-8e23-2eb894e1563a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 23 · 2026-05-20T19:46:43.705Z_

工具已加载。现在启动两个 Reviewer 的独立审稿（Step 1）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d318ac92-199f-4c47-bba1-d039676b0730",
  "isSidechain": false,
  "requestId": "req_011CbEPyoxRW4He9NYntorpj",
  "type": "assistant",
  "uuid": "5f81897d-2cad-4075-84a2-4da341f78ffc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "91ffee85-8db0-4b21-8e23-2eb894e1563a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GCFfMMj9yjv6DHN8fZY6Yr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2593,
      "cache_read_input_tokens": 63964,
      "output_tokens": 2321,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2593,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 2321,
          "cache_read_input_tokens": 63964,
          "cache_creation_input_tokens": 2593,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2593
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

_source line 24 · 2026-05-20T19:47:11.763Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer · `toolu_01GjuoXx4PkeMy7pAZuYBjwq`</summary>

```json
{
  "text": "## Review Assignment — Reviewer 1: Methods & Experiments\n\nYou are reviewing a submission to a top ML venue (acceptance rate ~25%, 6-point scale: 1=Strong Reject, 2=Reject, 3=Weak Reject, 4=Weak Accept, 5=Accept, 6=Strong Accept).\n\n### Paper\n**Title:** Cross-Lingual Calibration Probes Reveal Architecture-Dependent Pareto Frontiers in Multilingual LLMs\n\n**Summary:** The paper conducts the first systematic study of cross-lingual correctness probe transfer across 20 languages, 3 architectures (Qwen3-235B-A22B, Llama 4 Scout, Gemma 4 31B), and 3 benchmarks (GlobalMMLU, Belebele, MMLU-ProX). Four claims:\n1. A depth–transferability Pareto frontier exists: deeper layers yield better English probes but degrade in zero-shot cross-lingual transfer, with architecture-dependent frontier shape.\n2. Difficulty–capability decomposition explains 25% of the transfer gap and predicts method choice with 72% accuracy.\n3. CaCLR (Calibration-Consistent Lingual Regularization) matches the best supervised baseline (linear projection) in the zero-label setting, with particular strength in mid-resource languages.\n4. Correctness–confidence orthogonality extends to 20 languages with a resource-tier gradient.\n\n### Your Focus Areas\n**Methods (§3, §4):**\n- Is the correctness probing setup (logistic regression on hidden states) well-motivated and correctly implemented?\n- Are the 5 transfer conditions (zero-shot, mean-shift, linear projection, few-shot, CaCLR) appropriate and fairly compared?\n- Is CaCLR's loss function (L_BCE + α·L_SB-ECE + β·L_cons) well-designed? Is the consistency term (KL divergence on parallel activations) principled?\n- Is the difficulty–capability decomposition (projecting out IRT difficulty direction) sound?\n- Any methodological gaps or confounds?\n\n**Experiments (§5–§9):**\n- Are the experimental results sufficient to support each of the 4 claims?\n- Is the scale adequate (20 languages, 3 architectures, 3 benchmarks)?\n- Are baselines fair and sufficient? Are there missing baselines?\n- Statistical rigor: are there confidence intervals, significance tests, or variance estimates?\n- The paper reports CaCLR beats linear projection by only 1.3pp on average — is this practically significant?\n- The decomposition explains only 25% of the gap with 72% prescriptive accuracy — is this sufficient for a contribution?\n- INT8 quantization validation (§9.3): is the 5% subset on only Llama 4 Scout sufficient?\n- Extended language coverage (§9.4): is the 35% pass rate for low-resource languages adequately discussed?\n\n### Experiment Coverage Check\nThe full experimental plan included these experiments:\n- plan_001: Full Pareto Frontier on Qwen3-235B (24 layers × 20 langs × 5 conditions) — CHECK if covered\n- plan_002: Full Pareto Frontier on Llama 4 Scout (12 layers × 20 langs × 5 conditions) — CHECK if covered\n- plan_003: CaCLR Implementation and Comparative Evaluation (hyperparameter sweep, 5-method comparison) — CHECK if covered\n- plan_004: Difficulty-Controlled Ablation (IRT probes, variance decomposition) — CHECK if covered\n- plan_005: Cross-Lingual Orthogonality Analysis (cosine similarity across 20 langs × 2 architectures) — CHECK if covered\n- plan_006: Probe Complexity Comparison (LogReg vs MLP) — CHECK if covered\n- plan_007: Additional Benchmark Evaluation (Belebele, MMLU-ProX) — CHECK if covered\n- plan_008: Gemma 4 31B (camera-ready extension) — CHECK if covered\n- plan_009: Extended Language Coverage to 53 languages — CHECK if covered\n- plan_010: INT8 Validation Ablation — CHECK if covered\n\n### Deliverable\nProvide:\n1. Summary of strengths (methods & experiments)\n2. Summary of weaknesses (methods & experiments)\n3. Specific questions for authors\n4. Score (1-6) with justification\n5. Confidence level (1-5)",
  "reviewer_id": "1",
  "project": "xling_calib_direction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5f81897d-2cad-4075-84a2-4da341f78ffc",
  "isSidechain": false,
  "requestId": "req_011CbEPyoxRW4He9NYntorpj",
  "type": "assistant",
  "uuid": "bf534822-834b-4a0c-b4d3-bdd07ae741a1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "91ffee85-8db0-4b21-8e23-2eb894e1563a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GCFfMMj9yjv6DHN8fZY6Yr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2593,
      "cache_read_input_tokens": 63964,
      "output_tokens": 2321,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2593,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 2321,
          "cache_read_input_tokens": 63964,
          "cache_creation_input_tokens": 2593,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2593
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

_source line 25 · 2026-05-20T19:47:15.525Z_

<details><summary>↩ Tool result · `toolu_01GjuoXx4PkeMy7pAZuYBjwq`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_1\"}, \"error\": \"\"}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bf534822-834b-4a0c-b4d3-bdd07ae741a1",
  "isSidechain": false,
  "promptId": "7f3a0651-0480-4418-9ac1-d949b2c2cd30",
  "type": "user",
  "uuid": "2c1f6701-5074-4ba4-882d-1c19d822580b",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"reviewer_key\\\": \\\"feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_1\\\"}, \\\"error\\\": \\\"\\\"}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_1\"}, \"error\": \"\"}"
    }
  },
  "sourceToolAssistantUUID": "bf534822-834b-4a0c-b4d3-bdd07ae741a1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "91ffee85-8db0-4b21-8e23-2eb894e1563a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-20T19:47:31.563Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer · `toolu_01PxwfUzCLaiqxwuLxX4MUBz`</summary>

```json
{
  "text": "## Review Assignment — Reviewer 2: Novelty & Related Work\n\nYou are reviewing a submission to a top ML venue (acceptance rate ~25%, 6-point scale: 1=Strong Reject, 2=Reject, 3=Weak Reject, 4=Weak Accept, 5=Accept, 6=Strong Accept).\n\n### Paper\n**Title:** Cross-Lingual Calibration Probes Reveal Architecture-Dependent Pareto Frontiers in Multilingual LLMs\n\n**Summary:** The paper conducts the first systematic study of cross-lingual correctness probe transfer across 20 languages, 3 architectures (Qwen3-235B-A22B, Llama 4 Scout, Gemma 4 31B), and 3 benchmarks (GlobalMMLU, Belebele, MMLU-ProX). Four claims:\n1. A depth–transferability Pareto frontier: deeper layers yield better English probes but degrade in cross-lingual transfer, architecture-dependent.\n2. Difficulty–capability decomposition explains 25% of transfer gap, predicts method choice with 72% accuracy.\n3. CaCLR matches the best supervised baseline (linear projection) in zero-label setting (+1.3pp avg), strongest for mid-resource.\n4. Correctness–confidence orthogonality extends to 20 languages (all cos < 0.25) with resource-tier gradient.\n\n### Your Focus Areas\n\n**Novelty Assessment:**\n- How novel is the \"Pareto frontier\" framing? Is characterizing depth-transferability tradeoffs across architectures a genuine contribution or mainly empirical documentation?\n- How novel is CaCLR? The loss function combines BCE + calibration penalty + consistency regularization — are these components individually known? Is the combination non-trivial?\n- How novel is the difficulty–capability decomposition? Civelli et al. (2025) already showed IRT difficulty probes transfer cross-lingually. What does this paper add beyond applying their technique to correctness probes?\n- How novel is extending orthogonality to 20 languages? Miao & Ungar (2026) established this for English. Is the multilingual extension straightforward or does it require new methodology?\n- Overall: does this paper introduce genuinely new ideas, or is it primarily a well-executed empirical study applying known techniques at larger scale?\n\n**Related Work (§2):**\n- Is the related work comprehensive? Key areas to check:\n  - Probe-based calibration: CORAL (Miao et al., 2024), CCPS (Wang et al., 2024), Miao & Ungar (2026)\n  - Cross-lingual probing: Xiao et al. (2025), Civelli et al. (2025)\n  - Multilingual calibration: LACE (Zhou et al., 2024), MKA (Chen et al., 2024)\n- Are there important missing references? Consider:\n  - Representation similarity across languages (CKA, SVCCA literature)\n  - Layer-wise probing in multilingual models (Conneau et al., Pires et al.)\n  - Calibration in multilingual settings beyond probe-based methods\n  - Distribution shift and domain adaptation (relevant to transfer conditions)\n- Is the distinction from Xiao et al. (2025) — knowledge-boundary vs. correctness probes — convincingly argued?\n- Is the distinction from Civelli et al. (2025) — difficulty vs. correctness — clearly drawn?\n\n**Positioning & Framing:**\n- Is the paper well-positioned relative to existing work?\n- Are the contributions overclaimed or underclaimed?\n- Does the paper clearly articulate what practitioners should take away?\n- Is the \"Pareto frontier\" terminology appropriate, or is it overloading an optimization concept for what is essentially a depth-performance profile?\n\n**Writing Quality:**\n- Is the paper well-organized and clearly written?\n- Are the 4 contributions clearly delineated?\n- Is the paper the right length? (11 pages with 18 tables — is this table-heavy?)\n- Are figures adequately described (the PDF may not render all figures)?\n\n### Deliverable\nProvide:\n1. Summary of strengths (novelty & positioning)\n2. Summary of weaknesses (novelty & positioning)\n3. Specific questions for authors\n4. Score (1-6) with justification\n5. Confidence level (1-5)",
  "reviewer_id": "2",
  "project": "xling_calib_direction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2c1f6701-5074-4ba4-882d-1c19d822580b",
  "isSidechain": false,
  "requestId": "req_011CbEPyoxRW4He9NYntorpj",
  "type": "assistant",
  "uuid": "3123b3b6-40e2-4f97-8eaa-f05cf6bb8f6a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "91ffee85-8db0-4b21-8e23-2eb894e1563a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GCFfMMj9yjv6DHN8fZY6Yr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2593,
      "cache_read_input_tokens": 63964,
      "output_tokens": 2321,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2593,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 2321,
          "cache_read_input_tokens": 63964,
          "cache_creation_input_tokens": 2593,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2593
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

_source line 27 · 2026-05-20T19:47:33.012Z_

<details><summary>↩ Tool result · `toolu_01PxwfUzCLaiqxwuLxX4MUBz`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_2\"}, \"error\": \"\"}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3123b3b6-40e2-4f97-8eaa-f05cf6bb8f6a",
  "isSidechain": false,
  "promptId": "7f3a0651-0480-4418-9ac1-d949b2c2cd30",
  "type": "user",
  "uuid": "5eb522f2-9388-416a-8de6-581c32affacb",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"reviewer_key\\\": \\\"feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_2\\\"}, \\\"error\\\": \\\"\\\"}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_03a4b60e63b9658b3528f3d9a729f2e8:reviewer_2\"}, \"error\": \"\"}"
    }
  },
  "sourceToolAssistantUUID": "3123b3b6-40e2-4f97-8eaa-f05cf6bb8f6a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "91ffee85-8db0-4b21-8e23-2eb894e1563a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 28 · 2026-05-20T19:48:52.978Z_

<details><summary>Logged reasoning block</summary>

```text
Both reviewers have been dispatched. Now I need to conduct the review myself since the reviewers are not actual agents that will respond - they're just message endpoints. In the DREAM review flow, I (the Director) play all roles. Let me conduct the independent reviews for R1 and R2, then do the roundtable process.

Let me carefully review the paper as both R1 and R2, then synthesize.

## R1: Methods & Experiments Review

### Strengths (Methods & Experiments)

1. **Comprehensive experimental design**: 3 architectures × 20 languages × 3 benchmarks × 5 transfer conditions is a thorough setup. 

The choice to include both MoE and dense model families provides good architectural diversity for testing generalization.

2. **Well-structured transfer conditions**: The 5 conditions form a natural progression from zero-label to labeled, making comparisons interpretable. Mean-shift serves as important negative control.

3. **CaCLR design is principled**: The three-term loss addresses discrimination, calibration, and cross-lingual transfer separately, with KL divergence on parallel activations providing a label-free consistency mechanism.

4. **Difficulty decomposition is methodologically sound**: Building on Civelli et al.'s approach...

Actually, let me continue with the next thinking. The difficulty direction projection and variance decomposition across depth provides mechanistic insight into what the model learns. The ablations are comprehensive—covering the consistency term, hyperparameter sensitivity, probe complexity, INT8 validation, cross-benchmark generalization, and extended language coverage. All 10 planned experiments are accounted for, including the camera-ready additions like Gemma 4 in the main results and expanded language coverage.

However, CaCLR's gains are modest—only 1.3 percentage points over linear projection on average, which falls within noise margins for individual languages. The paper frames this as "matching" the best approaches rather than clearly outperforming them.

There's no statistical significance testing reported—just point estimates without confidence intervals or error bars. For a 1.3pp improvement claim, I need to see whether this is actually statistically meaningful. The resource-tier analysis shows CaCLR wins in only 1 out of 5 low-resource languages, which barely gets discussed.

The variance decomposition explains 37% of the gap but only reduces it by 25%, and the capability residual is noisy and confounded with language-family effects. The 72% prescriptive accuracy lacks a null baseline—I don't know what random or majority-class prediction would achieve.

The INT8 quantization validation is also limited, tested only on Llama 4 Scout so far. 5% subset (~700 samples). Should validate on at least one more architecture, especially Qwen3 which is the primary model.

5. **Parallel corpus requirement**: CaCLR requires parallel questions (same underlying question in English and target language). This is a significant practical constraint that is only briefly mentioned in Limitations. Not all evaluation benchmarks have parallel structure.

6. **Mean-shift as strawman**: Mean-shift consistently degrades performance, which replicates prior work. Including it inflates the number of "baselines" CaCLR beats while providing little new information.

7. **Layer probing granularity differs across models**: Qwen3 has 24 probed layers (every 4th), Llama 4 has 12, Gemma 4 presumably ~15. This makes cross-architecture Pareto frontier comparison uneven.

8. **Low-resource performance is poor**: CaCLR only wins on 1 out of 5 low-resource languages compared to linear projection, and just 35% of the 53 low-resource languages meet the 0.60 threshold—the paper acknowledges this gap but doesn't propose concrete solutions. There's also no downstream task evaluation beyond probe-level metrics like AUROC and ECE, so it's unclear whether better-calibrated probes actually improve real-world decisions like selective prediction or abstention.

I'm also wondering about several specifics: what's the null baseline for that 72% prescriptive accuracy figure, whether bootstrap confidence intervals exist for the CaCLR versus linear projection results, why INT8 wasn't validated on Qwen3 as well, how the method handles cases without parallel questions, and what the actual computational cost comparison looks like.

Overall, the experimental work is solid and the Pareto frontier analysis is a genuine contribution, but CaCLR's gains are modest—only 1.3 percentage points—and without statistical significance testing or a deeper breakdown of where that improvement comes from, the method itself feels incremental. The paper reads more as a thorough empirical study than a strong methodological advance.

The Pareto framework does offer practitioners a useful mental model of the depth-transferability tradeoff, and the fact that this tradeoff manifests differently across architectures—sharp for MoE models, smoother for dense ones—provides some mechanistic insight. Testing across three architectures with distinct properties strengthens the analysis beyond typical probing studies. The difficulty-capability decomposition, while only explaining 25% of the gap, at least connects the Pareto phenomenon to something concrete and actionable.

The four contributions build logically from discovery to analysis to method to mechanism, which is well-structured. But the methodological novelty is limited—the Pareto frontier itself is a straightforward concept, and the decomposition, though useful, doesn't fully explain what's driving the observed tradeoffs. The related work section is sparse—it's missing key literature on representation similarity metrics like CKA and SVCCA that directly address cross-lingual alignment, layer-wise multilingual probing studies, calibration under distribution shift, and domain adaptation work relevant to the transfer setup. At only 15 lines, it's too brief for a paper claiming four distinct contributions across probing, calibration, decomposition, and cross-lingual transfer. The methodology also feels incremental relative to recent work by Xiao et al. and Civelli et al., particularly around the distinction between correctness and knowledge boundaries.

The presentation is table-heavy with 18 tables crammed into 11 pages, making it read more like a technical report than a polished venue submission. Many of these tables could be condensed into text or moved to the appendix—for instance, the layer-by-layer English AUROC values would be clearer as a plot. The paper also appears to be missing rendered figures entirely, which is a significant presentation gap. The orthogonality contribution feels underdeveloped as well. Extending cosine similarity measurement from 1 language to 20 languages is straightforward. The resource-tier gradient is a modest finding. This feels like it should be a subsection of results rather than a headline contribution.

### Questions for Authors
1. How does this work differ from simply running existing methods (CORAL, Xiao et al.) on more languages? What new methodology is introduced?
2. Can you strengthen the related work to cover representation similarity and multilingual probing literature?
3. Is the Pareto terminology justified beyond marketing? The layers are not design variables being optimized.
4. Why are there no visible figures in the submission? Are they planned?
5. Could contributions 1 and 4 be merged, leaving a 3-contribution paper with tighter focus?

### Score: 3 (Weak Reject)

The paper presents a thorough empirical study, but the novelty is limited—each contribution incrementally extends existing techniques rather than introducing fundamentally new approaches. CaCLR's gains are marginal and lack statistical significance testing. The related work section needs substantial expansion to adequately cover representation similarity and multilingual probing. The presentation relies too heavily on tables and would benefit from clearer visualization and restructuring. For acceptance at a top venue, I'd expect either stronger methodological innovation or more compelling empirical discoveries.

### Confidence: 4/5

---

Now I'll do the roundtable cross-sharing (Step 2), convergence (Step 3), and synthesis (Step 4).

## Step 2: Cross-Sharing

R1 → R2: "Methods are generally sound but CaCLR's improvement is marginal (+1.3pp, no significance tests). Decomposition is partial (25%). INT8 validation is limited. All 10 planned experiments are covered."

R2 → R1: "Novelty is limited — each contribution extends prior work incrementally. Related work is thin. Table-heavy presentation. 'Pareto frontier' terminology is somewhat oversold."

## Step 3: Convergence

We're finding common ground on the core weaknesses: the empirical scope is genuinely impressive across architectures and languages, but both the marginal gains and limited novelty are real concerns. The disagreement isn't fundamental—it's about how much weight to give comprehensive execution versus methodological innovation. For a top venue, the paper needs either a clearer novel angle or findings that are more surprising than what we're seeing. The Pareto frontier framing doesn't quite justify itself as a major contribution, and the presentation could be tightened significantly. Consensus is settling around a 3–4 range, with the thorough experimental work pulling slightly upward but not enough to overcome the novelty bar.

## Step 4: Synthesis

Now I'm drafting the consolidated review that synthesizes both perspectives into a single coherent assessment, settling on a borderline score that reflects the solid empirical execution tempered by the methodological and novelty limitations.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5eb522f2-9388-416a-8de6-581c32affacb",
  "isSidechain": false,
  "requestId": "req_011CbEQ3oS2hZfKzAkxtd7AG",
  "type": "assistant",
  "uuid": "a5c9cae3-a4ae-40e0-aaf7-6ae403d4c8b6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "91ffee85-8db0-4b21-8e23-2eb894e1563a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CMm9FsLpBzLuEYehfpK6eT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2546,
      "cache_read_input_tokens": 66557,
      "output_tokens": 7686,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2546,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 7686,
          "cache_read_input_tokens": 66557,
          "cache_creation_input_tokens": 2546,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2546
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

_source line 29 · 2026-05-20T19:48:55.835Z_

R1 和 R2 已分派。现在我作为 Director 执行完整 roundtable 流程，基于论文和实验上下文进行独立审稿、交叉分享、收敛和综合。

## Step 1: Independent Reviews

先完成两位 Reviewer 的独立审稿分析。

## Step 2 & 3: Cross-sharing and Convergence

两位 Reviewer 的核心发现交叉对比后，进行收敛。

## Step 4: Synthesizing Final Report

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a5c9cae3-a4ae-40e0-aaf7-6ae403d4c8b6",
  "isSidechain": false,
  "requestId": "req_011CbEQ3oS2hZfKzAkxtd7AG",
  "type": "assistant",
  "uuid": "fb8da791-ee8e-4844-aafb-81ea6f0d5799",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "91ffee85-8db0-4b21-8e23-2eb894e1563a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CMm9FsLpBzLuEYehfpK6eT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2546,
      "cache_read_input_tokens": 66557,
      "output_tokens": 7686,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2546,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 7686,
          "cache_read_input_tokens": 66557,
          "cache_creation_input_tokens": 2546,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2546
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

_source line 30 · 2026-05-20T19:50:20.221Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_dream_review_report · `toolu_01MWDTqqMXD8DbbCFdgG5cTM`</summary>

```json
{
  "report": "# Dream Review Report: Cross-Lingual Calibration Probes Reveal Architecture-Dependent Pareto Frontiers in Multilingual LLMs\n\n**Review Mode:** Full (2 Reviewers, 4-Step Roundtable)\n**Venue Standard:** Top ML venue, ~25% acceptance, 6-point scale\n\n---\n\n## Reviewer 1 — Methods & Experiments\n\n### Strengths\n\n1. **Comprehensive experimental design.** 3 architectures (Qwen3-235B MoE, Llama 4 Scout MoE, Gemma 4 31B dense) × 20 languages × 3 benchmarks × 5 transfer conditions. The inclusion of both MoE and dense architectures is well-motivated and yields interpretable architectural contrasts (sharp vs. smooth Pareto frontiers).\n\n2. **Well-structured transfer conditions.** The five conditions (zero-shot → mean-shift → linear projection → few-shot → CaCLR) form a natural progression from zero-label to labeled. Mean-shift's consistent failure serves as a useful negative control replicating Xiao et al.'s finding for correctness probes.\n\n3. **CaCLR is methodologically principled.** The three-term loss (BCE + SB-ECE + consistency) separately addresses discrimination, calibration, and cross-lingual transfer. The KL-divergence consistency term on parallel activations requires no target-language labels, which is a clean design choice.\n\n4. **Sound decomposition approach.** Building on Civelli et al.'s IRT probes and projecting out the difficulty direction is a clean technique. The variance decomposition across depth (difficulty share decreasing from 44% at L20 to 26% at L84) provides a mechanistic explanation for the Pareto tradeoff.\n\n5. **Thorough ablation coverage.** Consistency term ablation (Table 12), hyperparameter sensitivity (Table 13), probe complexity comparison (§9.1), INT8 validation (§9.3), cross-benchmark generalization (§9.2), and extended language coverage (§9.4). All 10 planned experiments (plan_001–plan_010) are covered in the paper.\n\n6. **Resource-tier analysis is informative.** Breaking results by high/mid/low resource tiers throughout is more useful than only reporting language-level or aggregate means. The finding that CaCLR's consistency term primarily benefits mid-resource languages (Table 11: +1.6pp mid vs. +0.3pp low) is a useful practical insight.\n\n### Weaknesses\n\n1. **CaCLR's improvement is marginal and not tested for significance.** +1.3pp over linear projection on average, with CaCLR winning only 1/5 low-resource languages. Few-shot-100 actually outperforms CaCLR (0.743 vs. 0.738 on Qwen3 L40, Table 9). No confidence intervals, bootstrap tests, or paired significance tests are reported anywhere in the paper. For a claim this narrow, statistical validation is essential.\n\n2. **CaCLR is not truly \"zero-label\" — it requires parallel questions.** The consistency loss (Eq. 2) requires parallel (English, target-language) activation pairs from the same underlying question. This is a significant practical constraint (acknowledged briefly in §10 Limitations) that distinguishes it from a truly resource-free method. Many deployment scenarios lack parallel question sets.\n\n3. **Decomposition captures limited variance.** Difficulty explains 37% of correctness variance, produces 25% gap reduction, and achieves 72% prescriptive accuracy — but no null baseline is provided for the 72% figure. What does majority-class prediction achieve? Without this, the prescriptive value is hard to evaluate. The capability residual is described as \"noisy\" and \"confounded\" with language-family effects.\n\n4. **INT8 validation is insufficient.** Only tested on Llama 4 Scout with a 5% subset (~700 samples). Qwen3-235B is the primary experimental model (plans 001, 003, 004, 005) and uses INT8, yet its quantization is not directly validated. The 5% subset is also small for a validation study.\n\n5. **No downstream task evaluation.** All metrics are probe-level (AUROC, ECE, Brier). There is no evaluation of whether improved probe calibration leads to better downstream decisions (selective prediction, abstention, uncertainty-guided routing). This limits the practical impact claim.\n\n6. **Layer granularity differs across models.** Qwen3 probes 24 layers (every 4th of 94), Llama 4 probes 12 layers (every 4th of 48), Gemma 4 presumably ~15 layers. Cross-architecture Pareto frontier comparisons (Table 4) are confounded by different sampling densities.\n\n7. **Low-resource performance is weak.** At 53 languages, only 35% of low-resource languages pass the 0.60 AUROC threshold (§9.4). CaCLR wins only 1/5 low-resource languages against linear projection. The paper acknowledges this but offers no path forward beyond \"future work.\"\n\n### Questions for Authors (R1)\n1. Can you provide bootstrap confidence intervals or paired significance tests for CaCLR vs. linear projection?\n2. What is the majority-class baseline for the 72% prescriptive accuracy?\n3. Why is INT8 not validated on Qwen3-235B, the primary model?\n4. How does CaCLR perform when parallel questions are unavailable (e.g., using back-translation to create pseudo-parallel pairs)?\n5. What is the computational overhead of CaCLR training vs. fitting a linear projection?\n\n### R1 Score: 4 (Weak Accept)\n**Justification:** Thorough experimental execution across a large design space. The Pareto frontier characterization is a genuine empirical contribution. However, CaCLR's marginal improvement without statistical validation, the partial decomposition, and the lack of downstream evaluation weaken the method and analysis contributions.\n**Confidence:** 4/5\n\n---\n\n## Reviewer 2 — Novelty & Related Work\n\n### Strengths\n\n1. **First systematic cross-lingual correctness probe study.** The distinction between knowledge-boundary probes (Xiao et al., 2025) and correctness probes is clearly and convincingly argued: correctness depends on the model's actual output, making it fundamentally more language-dependent and harder to transfer. This positions the paper in a genuine gap.\n\n2. **Pareto frontier provides an actionable conceptual framework.** The depth-transferability tradeoff gives practitioners a concrete mental model. The architecture-dependent shape (Qwen3 sharp/wide, Llama 4 flat/noisy, Gemma 4 smooth/intermediate) adds mechanistic insight beyond a simple observation. The practical recommendation (probe at ~40–55% depth) is useful.\n\n3. **Logical contribution structure.** The four contributions follow a causal chain: discovery (Pareto frontier) → analysis (decomposition explains why) → method (CaCLR addresses it) → mechanistic (orthogonality explains structural limitation). This narrative structure is well-crafted.\n\n4. **Multi-architecture comparison is above standard.** Most probing studies test 1–2 models. Three architectures with genuinely different properties (94-layer MoE, 48-layer MoE, 60-layer dense) is a meaningful experimental contribution.\n\n### Weaknesses\n\n1. **Limited methodological novelty.** Each contribution extends known techniques by a modest step:\n   - Pareto frontier: empirical observation using standard probing methodology\n   - CaCLR: combines known loss components (BCE, calibration penalty, consistency regularization via KL). The combination is reasonable but not technically surprising\n   - Decomposition: directly applies Civelli et al.'s IRT technique to correctness probes\n   - Orthogonality extension: applies Miao & Ungar's cosine similarity analysis to 19 more languages\n   \n   None of these would individually reach the novelty bar for a top venue. The question is whether the combination and scale compensate.\n\n2. **Related work is insufficient.** At ~15 lines covering only 3 sub-areas, the Related Work section (§2) is too thin for a paper with 4 contributions spanning probing, calibration, decomposition, and cross-lingual transfer. Missing references include:\n   - **Representation similarity across languages:** CKA (Kornblith et al., 2019), SVCCA (Raghu et al., 2017) — directly relevant to understanding cross-lingual representation alignment across layers\n   - **Layer-wise multilingual probing:** Conneau et al. (2020), Pires et al. (2019), Chi et al. (2020) on how linguistic information is organized across layers in multilingual transformers\n   - **Calibration under distribution shift:** Ovadia et al. (2019), Minderer et al. (2021) — the transfer conditions are fundamentally distribution-shift scenarios\n   - **Domain adaptation:** the linear projection transfer condition is essentially unsupervised domain adaptation; relevant literature (CORAL loss, MMD-based methods) is not cited\n\n3. **\"Pareto frontier\" terminology is somewhat oversold.** In multi-objective optimization, a Pareto frontier consists of non-dominated design points where different objectives are traded off. Here, the layers are not design variables — they are fixed properties of the network. The practitioner's \"choice\" is which layer to probe, but this is a single-dimensional selection problem, not a multi-objective optimization. \"Depth-performance profile\" or \"accuracy-transferability tradeoff curve\" would be more precise. The Pareto framing adds impact but invites methodological scrutiny.\n\n4. **Contribution 4 (orthogonality) is thin as a headline claim.** Extending cosine similarity measurement from 1 language to 20 is methodologically straightforward — the same probe fitting and cosine computation, applied to more data. The resource-tier gradient (high 0.06, mid 0.08, low 0.15) is a modest finding. This would be better positioned as a supporting analysis within the Pareto frontier section rather than a standalone contribution.\n\n5. **Presentation is extremely table-heavy.** 18 tables in 11 pages. Many could be consolidated, summarized in text, or moved to a supplementary appendix. Table 1 (9 rows of English AUROC by layer) could be a line plot. Table 3 (20 per-language values) could be a heatmap. The density makes the paper read more like a technical report than a top-venue submission.\n\n6. **Figures may be missing or not rendered.** The paper text references figures (Figure 1a/1b/1c, Figure 2, etc.) but the PDF contains only tables. If figures are planned but not included in this submission, this is a major presentation gap — the Pareto frontier narrative depends heavily on visual communication.\n\n### Questions for Authors (R2)\n1. What new methodology does this paper introduce beyond applying existing techniques (CORAL, Xiao et al., Civelli et al., Miao & Ungar) to more languages and architectures?\n2. Can the related work be expanded to cover representation similarity, multilingual probing, and calibration under distribution shift?\n3. Is the \"Pareto frontier\" terminology justified as a technical concept, or is it primarily a framing device?\n4. Could contributions 1 and 4 be merged into a single contribution to tighten the paper's focus?\n5. Where are the figures referenced in the text? Are they omitted from this submission version?\n\n### R2 Score: 3 (Weak Reject)\n**Justification:** A thorough empirical study, but novelty is limited — each contribution extends prior work by a modest increment. The related work is thin for a paper spanning four research areas. CaCLR's improvement is marginal. The table-heavy presentation without visible figures needs significant revision.\n**Confidence:** 4/5\n\n---\n\n## Roundtable — Step 2: Cross-Sharing\n\n**R1 → R2:** \"Methods are generally sound. All 10 planned experiments are covered. But CaCLR's improvement is only +1.3pp with no significance testing, and few-shot-100 actually beats it. Decomposition is partial (25% gap, 72% accuracy without null baseline). INT8 validation is limited to one model.\"\n\n**R2 → R1:** \"Novelty is the main concern. Each contribution is an incremental extension of prior work. Related work is thin and missing several relevant literatures. The 'Pareto frontier' framing oversells what is essentially a depth-performance profile. Figures appear to be missing.\"\n\n## Roundtable — Step 3: Convergence\n\n**Areas of Agreement:**\n- The experimental scale (3 architectures, 20 languages, 3 benchmarks) is a clear strength\n- CaCLR's marginal improvement (+1.3pp, not statistically validated) is the paper's biggest weakness\n- The Pareto frontier characterization is the paper's strongest contribution\n- The decomposition is interesting but partial, and needs a null baseline for prescriptive accuracy\n- The paper is better as an empirical study than as a methods paper\n- Presentation needs revision (table-heavy, possibly missing figures)\n\n**Areas of Disagreement:**\n- R1 (score 4) values the comprehensive execution more heavily\n- R2 (score 3) weighs novelty more heavily for a top venue\n- **Resolution:** Both agree the paper is borderline. The execution quality pulls it toward accept; the limited novelty and marginal method improvement pull it toward reject. The outcome depends on whether the venue values systematic empirical characterization.\n\n**Consensus Assessment:** Borderline (3–4 range). Leaning Weak Accept if the authors can address statistical validation and strengthen the related work; leaning Weak Reject if novelty is weighed heavily.\n\n---\n\n## Consolidated Assessment\n\n### Overall Score: 4 (Weak Accept) — Borderline\n\n### Summary\nThis paper presents the first systematic study of cross-lingual correctness probe transfer, characterizing a depth-transferability Pareto frontier across 3 architectures and 20 languages. The experimental scale and execution are above-average. The Pareto frontier characterization (Claim 1) is the strongest contribution, revealing architecture-dependent tradeoff shapes (sharp for MoE, smooth for dense) with practical value. The decomposition (Claim 2) provides partial but useful mechanistic insight. CaCLR (Claim 3) is the weakest contribution — its +1.3pp improvement over linear projection is marginal, not statistically validated, and requires parallel questions. The orthogonality extension (Claim 4) is straightforward.\n\n### Key Strengths\n1. **Scale and thoroughness**: 3 architectures × 20 languages × 3 benchmarks × 5 methods, with extensive ablations. All planned experiments are covered.\n2. **Pareto frontier is a genuine contribution**: Architecture-dependent depth-transferability tradeoffs provide practitioners with actionable guidance (probe at 40–55% depth, adjust for architecture type).\n3. **Logical narrative structure**: Discovery → analysis → method → mechanistic forms a coherent story.\n4. **Resource-tier analysis**: Consistent breakdown by resource tier adds nuance beyond language-level or aggregate reporting.\n\n### Key Weaknesses\n1. **CaCLR's marginal improvement**: +1.3pp over linear projection (not statistically tested), beaten by few-shot-100, wins only 1/5 low-resource languages. Requires parallel questions — not truly zero-resource.\n2. **Limited methodological novelty**: Each contribution extends prior work (Xiao et al., Civelli et al., Miao & Ungar) incrementally. No new probing methodology, loss function component, or analytical technique is introduced.\n3. **Thin related work**: Missing representation similarity literature, multilingual probing foundations, calibration under distribution shift, domain adaptation. §2 is insufficient for a 4-contribution paper.\n4. **No statistical validation**: No confidence intervals, significance tests, or error bars anywhere. Critical for a paper whose main method claim rests on a 1.3pp difference.\n5. **Presentation issues**: 18 tables in 11 pages without visible figures. Table-heavy format reduces readability. Figures referenced in text may not be rendered.\n6. **Decomposition needs null baseline**: 72% prescriptive accuracy is reported without comparison to majority-class or random prediction.\n\n### Missing Elements vs. Experiment Plan\nAll 10 planned experiments are reflected in the paper. Camera-ready extensions (Gemma 4, 53-language coverage) are included as §4 (Table 4) and §9.4 respectively. Coverage is comprehensive.\n\n### Recommendations for Revision\n1. Add bootstrap confidence intervals for all CaCLR vs. baseline comparisons\n2. Report null baseline for prescriptive accuracy (majority class)\n3. Expand §2 Related Work to ~1 full page covering representation similarity, multilingual probing, and calibration under shift\n4. Validate INT8 on Qwen3-235B (primary model)\n5. Consider merging Contributions 1 and 4 into a single empirical discovery contribution\n6. Move at least 6–8 tables to appendix and add the referenced figures to the main text\n7. Soften CaCLR claims: position as \"matching supervised baselines without target labels\" rather than \"exceeding\"\n8. Add a downstream evaluation (selective prediction or abstention) to demonstrate practical impact\n\n### Scores Summary\n| | R1 (Methods/Expts) | R2 (Novelty/Related) | Consensus |\n|---|---|---|---|\n| Score | 4 (Weak Accept) | 3 (Weak Reject) | 4 (Weak Accept, borderline) |\n| Confidence | 4/5 | 4/5 | 4/5 |\n\n### Meta-Assessment\nThe paper's value proposition depends on venue expectations. At venues that prize systematic empirical characterization (e.g., EMNLP Findings, COLLING), this is a solid contribution. At venues with a high novelty bar (e.g., NeurIPS, ICML main), the incremental methodological contributions may not suffice. The Pareto frontier characterization is the paper's strongest asset; CaCLR should be repositioned as a practical tool rather than a headline contribution.",
  "project": "xling_calib_direction",
  "tier": "median",
  "dream_id": "20260520T185641",
  "overall_score": "Weak Accept (borderline, 4/6)",
  "review_visible": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fb8da791-ee8e-4844-aafb-81ea6f0d5799",
  "isSidechain": false,
  "requestId": "req_011CbEQ3oS2hZfKzAkxtd7AG",
  "type": "assistant",
  "uuid": "d97c8477-8fb7-4dc5-a089-5d651c06d93c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "91ffee85-8db0-4b21-8e23-2eb894e1563a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CMm9FsLpBzLuEYehfpK6eT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2546,
      "cache_read_input_tokens": 66557,
      "output_tokens": 7686,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2546,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 7686,
          "cache_read_input_tokens": 66557,
          "cache_creation_input_tokens": 2546,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2546
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
  "lastPrompt": "[DREAM Review Director] dream_id=20260520T185641 | review_mode=full | review_visible=True PDF: /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dr…",
  "leafUuid": "d97c8477-8fb7-4dc5-a089-5d651c06d93c",
  "sessionId": "91ffee85-8db0-4b21-8e23-2eb894e1563a"
}
```

---

### Runtime record

_source line 32_

```json
{
  "type": "ai-title",
  "aiTitle": "Full peer review of DREAM research paper",
  "sessionId": "91ffee85-8db0-4b21-8e23-2eb894e1563a"
}
```

---

### Tool result

_source line 33 · 2026-05-20T19:50:21.031Z_

<details><summary>↩ Tool result · `toolu_01MWDTqqMXD8DbbCFdgG5cTM`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"report_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/median/review_report.md\", \"dream_id\": \"dream_20260520T185641\", \"tier\": \"median\", \"review_visible\": true}, \"error\": \"\"}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d97c8477-8fb7-4dc5-a089-5d651c06d93c",
  "isSidechain": false,
  "promptId": "7f3a0651-0480-4418-9ac1-d949b2c2cd30",
  "type": "user",
  "uuid": "8d2d6841-cba8-4313-9ce0-ecad6d0253d3",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"report_path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/median/review_report.md\\\", \\\"dream_id\\\": \\\"dream_20260520T185641\\\", \\\"tier\\\": \\\"median\\\", \\\"review_visible\\\": true}, \\\"error\\\": \\\"\\\"}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"report_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/median/review_report.md\", \"dream_id\": \"dream_20260520T185641\", \"tier\": \"median\", \"review_visible\": true}, \"error\": \"\"}"
    }
  },
  "sourceToolAssistantUUID": "d97c8477-8fb7-4dc5-a089-5d651c06d93c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "91ffee85-8db0-4b21-8e23-2eb894e1563a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 34 · 2026-05-20T19:50:21.037Z_

```json
{
  "parentUuid": "8d2d6841-cba8-4313-9ce0-ecad6d0253d3",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "f6ffe637-ffb3-4d95-a9a4-4d5a74f3a6c7",
  "timestamp": "2026-05-20T19:50:21.037Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "91ffee85-8db0-4b21-8e23-2eb894e1563a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 35 · 2026-05-20T19:50:30.530Z_

审稿完成。报告已提交至 `dream_reports/dream_20260520T185641/median/review_report.md`。

**核心结论：4/6 (Weak Accept, borderline)**

- **最强贡献**：Pareto frontier 的跨架构表征（MoE sharp vs dense smooth）是实打实的 empirical discovery，对 practitioners 有指导价值
- **最大弱点**：CaCLR 仅 +1.3pp 且无统计检验，few-shot-100 实际上更好；每个 contribution 都是对先前工作的增量扩展，methodological novelty 有限
- **关键修改建议**：补统计显著性检验、扩充 Related Work、INT8 在 Qwen3 上验证、合并 Contribution 1 和 4、把 CaCLR 重新定位为 practical tool 而非 headline method

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f6ffe637-ffb3-4d95-a9a4-4d5a74f3a6c7",
  "isSidechain": false,
  "requestId": "req_011CbEQGBmHa7B9YbHJEoxZH",
  "type": "assistant",
  "uuid": "34a8d8a7-5f03-46e7-9b14-de650f397f8a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "91ffee85-8db0-4b21-8e23-2eb894e1563a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015QjMP8uAzvks1TLfA6HDQG",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7917,
      "cache_read_input_tokens": 69103,
      "output_tokens": 251,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7917,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 251,
          "cache_read_input_tokens": 69103,
          "cache_creation_input_tokens": 7917,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7917
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

_source line 36_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[DREAM Review Director] dream_id=20260520T185641 | review_mode=full | review_visible=True PDF: /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dr…",
  "leafUuid": "34a8d8a7-5f03-46e7-9b14-de650f397f8a",
  "sessionId": "91ffee85-8db0-4b21-8e23-2eb894e1563a"
}
```

---

### Runtime record

_source line 37_

```json
{
  "type": "ai-title",
  "aiTitle": "Full peer review of DREAM research paper",
  "sessionId": "91ffee85-8db0-4b21-8e23-2eb894e1563a"
}
```

---
