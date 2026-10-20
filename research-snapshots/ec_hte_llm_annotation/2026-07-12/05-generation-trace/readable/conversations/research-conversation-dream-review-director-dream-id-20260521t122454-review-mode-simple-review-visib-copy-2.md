# Research conversation: [DREAM Review Director] dream_id=20260521T122454 | review_mode=simple | review_visible=True PDF: /home/ubuntu/.agent-ml-

**When Debiasing Hurts: An Exact Bias Identity for LLM-Annotated Treatment Effects (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 31
- **Recorded user turns:** 2
- **Tool calls:** 5
- **Original source:** `logs/chats/exported-trajectories/account-3/33779107-04cc-4691-9d8a-87f3f46280c6.jsonl`
- **Structured JSON:** [`6f4bb9e0d95fce327a7e.json`](../../sessions/6f/6f4bb9e0d95fce327a7e.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-21T13:02:27.019Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-21T13:02:27.019Z",
  "sessionId": "33779107-04cc-4691-9d8a-87f3f46280c6",
  "content": "[DREAM Review Director]\ndream_id=20260521T122454 | review_mode=simple | review_visible=True\nPDF: /home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/dream_reports/dream_20260521T122454/best/review_input_db82206b.pdf\n\n（内部编排信息：tier=best，仅用于 submit_dream_review_report 调用。\n你在向 Reviewer 发送审稿任务时，**严禁**提及档位名称 best/median/worst，\n也不要暗示论文结果的好坏。Reviewer 必须盲审。）\n\n任务：对上述 PDF 进行 simple 模式审稿。 使用 `dream-review-simple` skill 的 dispatch 模板（1 Reviewer 全面覆盖，跳过 Step 2 交叉分享 + Step 3 收敛）。\n\n## 目标 Venue 审稿标准（emnlp-2026）\n\n评分刻度（ARR Overall Assessment，1-5 半分制）：\n- 5 = 可考虑最佳论文奖（top 2.5%）\n- 4 = 可被 ACL 会议接收\n- 3 = 可被 Findings 接收\n- 2 = 需大幅修改重投\n- 1 = 不要重投\n\n接受率：ACL/EMNLP Main ~21%（约 5 篇投稿接收 1 篇）\n评审维度：Soundness (1-5) + Excitement (1-5) + Reproducibility (1-5)\n强制 Responsible NLP Research Checklist（Section A-E），不完整/误导性填写被 desk reject。\n自动 reject 信号：匿名性违规、超页数限制、缺 Limitations section、幻觉引用。\n\n请严格按照上述评分刻度和接受率校准你的评分。\n\n## 实验设计参考\n\n完整实验设计（含想象实验列表）：`/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/dream_reports/dream_20260521T122454/best/review_context.yaml`\n论文可能未完整反映所有实验——参考此文件判断覆盖度。\n完成后必须调用 `submit_dream_review_report(report, project=\"ec_hte_llm_annotation\", tier=\"best\", dream_id=\"20260521T122454\", review_visible=True)` —— 报告会写入 dream_reports/dream_20260521T122454/best/review_report.md，编排进程通过 subprocess 退出读取它。\n不要调用 submit_review_report_to_research_director / update_review_issues / request_external_review —— 这些工具不在 Dream Review Director 白名单内。\n"
}
```

---

### Runtime record

_source line 2 · 2026-05-21T13:02:27.022Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-21T13:02:27.022Z",
  "sessionId": "33779107-04cc-4691-9d8a-87f3f46280c6"
}
```

---

## Round 1

9 recorded events

### User

_source line 3 · 2026-05-21T13:02:27.056Z_

[DREAM Review Director]
dream_id=20260521T122454 | review_mode=simple | review_visible=True
PDF: /home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/dream_reports/dream_20260521T122454/best/review_input_db82206b.pdf

（内部编排信息：tier=best，仅用于 submit_dream_review_report 调用。
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

完整实验设计（含想象实验列表）：`/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/dream_reports/dream_20260521T122454/best/review_context.yaml`
论文可能未完整反映所有实验——参考此文件判断覆盖度。
完成后必须调用 `submit_dream_review_report(report, project="ec_hte_llm_annotation", tier="best", dream_id="20260521T122454", review_visible=True)` —— 报告会写入 dream_reports/dream_20260521T122454/best/review_report.md，编排进程通过 subprocess 退出读取它。
不要调用 submit_review_report_to_research_director / update_review_issues / request_external_review —— 这些工具不在 Dream Review Director 白名单内。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "b20fe594-a1fa-45c4-9afa-b12a0912be14",
  "type": "user",
  "uuid": "540c7cf4-e26e-4790-9fb3-cb94359e2767",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation",
  "sessionId": "33779107-04cc-4691-9d8a-87f3f46280c6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-21T13:02:27.055Z_

```json
{
  "parentUuid": "540c7cf4-e26e-4790-9fb3-cb94359e2767",
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
  "uuid": "3ca67985-5a46-456c-bfda-4e0b8f918e93",
  "timestamp": "2026-05-21T13:02:27.055Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation",
  "sessionId": "33779107-04cc-4691-9d8a-87f3f46280c6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-21T13:02:27.055Z_

```json
{
  "parentUuid": "3ca67985-5a46-456c-bfda-4e0b8f918e93",
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
  "uuid": "0be0705d-f6cc-46e1-808c-79aab12b3040",
  "timestamp": "2026-05-21T13:02:27.055Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation",
  "sessionId": "33779107-04cc-4691-9d8a-87f3f46280c6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6 · 2026-05-21T13:02:27.055Z_

```json
{
  "parentUuid": "0be0705d-f6cc-46e1-808c-79aab12b3040",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "4085c917-cb9c-4c05-b83d-696c8b83a352",
  "timestamp": "2026-05-21T13:02:27.055Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation",
  "sessionId": "33779107-04cc-4691-9d8a-87f3f46280c6",
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
  "aiTitle": "Review EMNLP paper on HTE and LLM annotation",
  "sessionId": "33779107-04cc-4691-9d8a-87f3f46280c6"
}
```

---

### Assistant

_source line 8 · 2026-05-21T13:02:32.193Z_

I'll start by reading the PDF and the experiment design context file to conduct the review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4085c917-cb9c-4c05-b83d-696c8b83a352",
  "isSidechain": false,
  "requestId": "req_011CbFky2h4KirovQ33wDMNN",
  "type": "assistant",
  "uuid": "ec14a66d-8b15-482b-bfcd-857ae9cb5e43",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation",
  "sessionId": "33779107-04cc-4691-9d8a-87f3f46280c6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0141RvRqGvpkH9cJE5jYEBAg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11820,
      "cache_read_input_tokens": 11841,
      "output_tokens": 235,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11820,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 235,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11820,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11820
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

_source line 9 · 2026-05-21T13:02:33.199Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Bhi7e73MKeNWHWDXS5qxBH`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/dream_reports/dream_20260521T122454/best/review_input_db82206b.pdf",
  "pages": "1-20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ec14a66d-8b15-482b-bfcd-857ae9cb5e43",
  "isSidechain": false,
  "requestId": "req_011CbFky2h4KirovQ33wDMNN",
  "type": "assistant",
  "uuid": "0506c19e-8eec-4bb4-b7e2-f5c2ddf9e288",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation",
  "sessionId": "33779107-04cc-4691-9d8a-87f3f46280c6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0141RvRqGvpkH9cJE5jYEBAg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11820,
      "cache_read_input_tokens": 11841,
      "output_tokens": 235,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11820,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 235,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11820,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11820
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

_source line 10 · 2026-05-21T13:02:33.497Z_

<details open><summary>🔧 Tool call — Read · `toolu_01KHybMM1wZUXJLsbgaqQjpz`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/dream_reports/dream_20260521T122454/best/review_context.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0506c19e-8eec-4bb4-b7e2-f5c2ddf9e288",
  "isSidechain": false,
  "requestId": "req_011CbFky2h4KirovQ33wDMNN",
  "type": "assistant",
  "uuid": "652e3cf1-5a8c-4891-8f76-313c715ce75b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation",
  "sessionId": "33779107-04cc-4691-9d8a-87f3f46280c6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0141RvRqGvpkH9cJE5jYEBAg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11820,
      "cache_read_input_tokens": 11841,
      "output_tokens": 235,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11820,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 235,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11820,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11820
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

_source line 11 · 2026-05-21T13:02:33.719Z_

<details><summary>↩ Tool result · `toolu_01Bhi7e73MKeNWHWDXS5qxBH`</summary>

```text
PDF pages extracted: 9 page(s) from /home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/dream_reports/dream_20260521T122454/best/review_input_db82206b.pdf (253KB)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0506c19e-8eec-4bb4-b7e2-f5c2ddf9e288",
  "isSidechain": false,
  "promptId": "b20fe594-a1fa-45c4-9afa-b12a0912be14",
  "type": "user",
  "uuid": "d8f31c1d-deb1-46b8-bf53-507f40da7d3c",
  "toolUseResult": {
    "type": "parts",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/dream_reports/dream_20260521T122454/best/review_input_db82206b.pdf",
      "originalSize": 259056,
      "outputDir": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0520-projects-ec-hte-llm-annotation/33779107-04cc-4691-9d8a-87f3f46280c6/tool-results/pdf-fe1a1c04-d0d0-4b03-afa3-06b95d2531a6",
      "count": 9
    }
  },
  "sourceToolAssistantUUID": "0506c19e-8eec-4bb4-b7e2-f5c2ddf9e288",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation",
  "sessionId": "33779107-04cc-4691-9d8a-87f3f46280c6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

## Round 2

20 recorded events

### User

_source line 12 · 2026-05-21T13:02:33.716Z_

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
  "parentUuid": "d8f31c1d-deb1-46b8-bf53-507f40da7d3c",
  "isSidechain": false,
  "promptId": "b20fe594-a1fa-45c4-9afa-b12a0912be14",
  "type": "user",
  "isMeta": true,
  "uuid": "bd1f5627-25f0-4902-84f5-0b68294821f3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation",
  "sessionId": "33779107-04cc-4691-9d8a-87f3f46280c6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 13_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[DREAM Review Director] dream_id=20260521T122454 | review_mode=simple | review_visible=True PDF: /home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/dream_reports/dr…",
  "leafUuid": "d8f31c1d-deb1-46b8-bf53-507f40da7d3c",
  "sessionId": "33779107-04cc-4691-9d8a-87f3f46280c6"
}
```

---

### Runtime record

_source line 14_

```json
{
  "type": "ai-title",
  "aiTitle": "Review EMNLP paper on HTE and LLM annotation",
  "sessionId": "33779107-04cc-4691-9d8a-87f3f46280c6"
}
```

---

### Tool result

_source line 15 · 2026-05-21T13:02:34.136Z_

<details><summary>↩ Tool result · `toolu_01KHybMM1wZUXJLsbgaqQjpz`</summary>

```text
1	narrative_guidance: '三条 Claims 完整保留，Lead with ''debiasing can hurt'' (50% parameter
2	  space, up to 5.9x amplification)。 EC-HTE 作为 principled fix，诊断准则作为 practical decision
3	  tool。PPCI 互补性升级至 Contribution #4。 Real data 作为 consistent illustration (pattern
4	  consistency, NOT ground-truth benchmark)。 Headline: ''Global correction worsens
5	  subgroup CATE bias by 2-3x median; EC-HTE reduces bias to near-zero with 250 expert
6	  labels; composition with PPCI achieves 0.005 bias under dual error.'' 审稿周期目标 1R
7	  accept 或 minor revision。
8	
9	  '
10	imagined_experiments:
11	- name: Hierarchical Bayesian EC-HTE on Synthetic Data
12	  plan_id: exp-001
13	  description: 'HB Dirichlet-prior confusion matrix estimator with partial pooling，
14	    full regime sweep (extreme/moderate/homogeneous × n_expert 100-2000 × K=2,4)，
15	    与 MLE/Laplace 对比。100 MC runs per config，4-chain NUTS MCMC。
16	
17	    '
18	  expected_results:
19	    mcmc_rhat_max: 1.005
20	    mcmc_ess_min: 1500
21	    mcmc_divergent: 0
22	    runtime_min: 70
23	    total_mc_runs: 3600
24	    hb_vs_mle_rmse_improvement_k2_n50: 4-9%
25	    hb_vs_mle_rmse_improvement_k4_n50_moderate: 6-9%
26	    hb_coverage_median: 0.93
27	    hb_coverage_min: 0.87
28	    hyperprior_sensitivity_k2_variation: <1%
29	    hyperprior_sensitivity_k4_variation: ~4-5%
30	    singularity_guard_triggers: extreme/n=50 only (2-3 per 100 runs)
31	  result_rationale: 'best 档下 MCMC 收敛良好 (R̂<1.01, ESS>200) 因为 4-chain NUTS 提供充分探索，
32	    Dirichlet 先验与 multinomial likelihood 共轭性保证后验几何良好。 HB 在 n=50 小样本时优势最大 (4-9% RMSE
33	    improvement) 因为 partial pooling 的 James-Stein shrinkage 在信息稀缺时借力最强；n≥500 时 MLE
34	    已有足够数据， HB 收敛至 MLE (<0.5% 差异)。coverage median 0.93 而非 0.95 因为 HB 后验 区间基于 MCMC
35	    样本，有限 MC 引入的 discretization 导致轻微 undercoverage。 hyperprior sensitivity 在 K=4 时更大
36	    (~4-5%) 因为 4 subgroup 的 Dirichlet 浓度参数影响更多自由度，但 coverage 不变说明 point estimate 对先验敏感
37	    但区间宽度自适应补偿。
38	
39	    '
40	  tables:
41	  - title: HB vs MLE RMSE Comparison (K=2)
42	    columns:
43	    - regime
44	    - n_expert
45	    - subgroup
46	    - hb_rmse
47	    - mle_rmse
48	    - improvement_pct
49	    rows:
50	    - - extreme
51	      - 50
52	      - z0
53	      - 0.095
54	      - 0.104
55	      - 8.7
56	    - - extreme
57	      - 50
58	      - z1
59	      - 0.102
60	      - 0.108
61	      - 5.6
62	    - - extreme
63	      - 100
64	      - z0
65	      - 0.065
66	      - 0.066
67	      - 1.5
68	    - - extreme
69	      - 100
70	      - z1
71	      - 0.068
72	      - 0.069
73	      - 1.4
74	    - - extreme
75	      - 250
76	      - z0
77	      - 0.041
78	      - 0.042
79	      - 2.4
80	    - - extreme
81	      - 500
82	      - z0
83	      - 0.029
84	      - 0.029
85	      - 0.3
86	    - - moderate
87	      - 50
88	      - z0
89	      - 0.088
90	      - 0.092
91	      - 4.3
92	    - - moderate
93	      - 100
94	      - z0
95	      - 0.06
96	      - 0.061
97	      - 1.6
98	  - title: HB vs MLE RMSE Comparison (K=4)
99	    columns:
100	    - regime
101	    - n_expert
102	    - subgroup
103	    - hb_rmse
104	    - mle_rmse
105	    - improvement_pct
106	    rows:
107	    - - extreme
108	      - 50
109	      - sgC
110	      - 0.99
111	      - 1.3
112	      - 23.8
113	    - - moderate
114	      - 50
115	      - sgC
116	      - 0.85
117	      - 0.93
118	      - 8.6
119	    - - moderate
120	      - 50
121	      - sgB
122	      - 0.42
123	      - 0.52
124	      - 19.2
125	    - - extreme
126	      - 100
127	      - sgC
128	      - 0.29
129	      - 0.46
130	      - 37.0
131	    - - extreme
132	      - 250
133	      - sgC
134	      - 0.14
135	      - 0.15
136	      - 6.7
137	  - title: Hyperprior Sensitivity (scale ∈ {0.5, 1.0, 2.0})
138	    columns:
139	    - K
140	    - metric
141	    - scale_0.5
142	    - scale_1.0
143	    - scale_2.0
144	    rows:
145	    - - 2
146	      - rmse_mean
147	      - 0.0632
148	      - 0.0635
149	      - 0.0638
150	    - - 4
151	      - rmse_mean
152	      - 0.182
153	      - 0.175
154	      - 0.168
155	    - - 2
156	      - coverage
157	      - 0.93
158	      - 0.93
159	      - 0.93
160	    - - 4
161	      - coverage
162	      - 0.92
163	      - 0.93
164	      - 0.93
165	  figures_description:
166	  - HB vs MLE RMSE ratio across n_expert (x-axis log scale), 分 K=2/K=4 和 extreme/moderate
167	    四面板
168	  analysis: 'HB partial pooling 的核心价值在小样本 (n_expert/K < 50)：shrinkage 将不稳定的 per-subgroup
169	    MLE 拉向 pooled estimate，降低 variance。K=4/extreme/n=50 的 singularity guard 触发 (2-3/100
170	    runs) 说明此边界条件下 MLE 本身不可靠， HB 的正则化是必要的。4-chain MCMC 相比 2-chain 的 ESS 提升 ~4x 确认
171	    多链策略对 posterior geometry exploration 的价值。
172	
173	    '
174	- name: Formal Bias Decomposition Verification
175	  plan_id: exp-002
176	  description: '解析推导 bias = Δπ × Δτ 的 exact identity，系统参数网格上 MC 验证。 K=2 和 K=4 分别验证。包含
177	    ''debiasing can hurt'' proposition 的构造性证明。
178	
179	    '
180	  expected_results:
181	    r2_bias_identity_k2: 0.994
182	    r2_bias_identity_k4: 0.974
183	    tightness_ratio_k2_median: 1.003
184	    tightness_ratio_k4_median: 1.023
185	    debiasing_hurts_pct: 50
186	    debiasing_hurts_threshold_delta_misclass: 0.12
187	    max_bias_ratio_k2_extreme: 2.86
188	    max_bias_ratio_k4_extreme: 2.41
189	    coverage_2se_k2: 0.951
190	    coverage_2se_k4: 0.94
191	  result_rationale: 'R²=0.994 (K=2) 因为二子群下 bias identity 是 exact (population level)，
192	    MC 偏差仅来自有限样本噪声 (N=5000, 100 MC runs)。K=4 的 R²=0.974 稍低 因为 sum-of-products form
193	    中 4 个子群的 MC 噪声累积（4 个交叉项 vs K=2 的 1 个）， 但仍然是 identity 而非 bound。tightness ratio
194	    ≈1.0 进一步确认这是 exact identity。 debiasing hurts 50% (260/520 non-trivial configs)
195	    因为当 naive bias 方向与 global correction 方向同号时 correction 有效，异号时 amplify——对称参数网格下
196	    恰好 50%。max_bias_ratio K=2 > K=4 (2.86 vs 2.41) 因为 DIM estimator 下 K=2 的两个子群 error
197	    rate 差异最大化（所有 heterogeneity 集中在一个对比）， 而 K=4 将 heterogeneity 分散到多个对比，单个子群的 worst-case
198	    amplification 反而降低。 这是 DIM estimator 的特性——CausalForest 行为相反 (exp-011)。
199	
200	    '
201	  tables:
202	  - title: Bias Identity R² Verification
203	    columns:
204	    - K
205	    - n_configs
206	    - R2
207	    - tightness_median
208	    - tightness_95pct
209	    rows:
210	    - - 2
211	      - 260
212	      - 0.994
213	      - 1.003
214	      - 1.012
215	    - - 4
216	      - 260
217	      - 0.974
218	      - 1.023
219	      - 1.068
220	  - title: Debiasing Hurts Analysis
221	    columns:
222	    - K
223	    - total_configs
224	    - hurts_count
225	    - hurts_pct
226	    - max_ratio
227	    - worst_config
228	    rows:
229	    - - 2
230	      - 260
231	      - 130
232	      - 50.0
233	      - 2.86
234	      - Δπ=0.20, Δτ=0.50
235	    - - 4
236	      - 260
237	      - 130
238	      - 50.0
239	      - 2.41
240	      - Δπ=0.20, Δτ=0.50
241	  - title: Bias Amplification by Parameter Region
242	    columns:
243	    - delta_pi
244	    - delta_tau
245	    - k2_ratio
246	    - k4_ratio
247	    - direction
248	    rows:
249	    - - 0.05
250	      - 0.1
251	      - 1.12
252	      - 1.08
253	      - global improves
254	    - - 0.05
255	      - 0.5
256	      - 1.45
257	      - 1.32
258	      - global improves
259	    - - 0.15
260	      - 0.1
261	      - 1.85
262	      - 1.62
263	      - global hurts
264	    - - 0.15
265	      - 0.5
266	      - 2.52
267	      - 2.18
268	      - global hurts
269	    - - 0.2
270	      - 0.5
271	      - 2.86
272	      - 2.41
273	      - global hurts (maximum)
274	  figures_description:
275	  - Δπ × Δτ heatmap showing bias amplification factor，红色=global hurts, 蓝色=global helps
276	  - Analytic prediction vs MC bias scatter plot with R² annotation, K=2 和 K=4 双面板
277	  analysis: 'bias identity 的 exact 性质（R²>0.97 for both K）为 Claim 1 提供了最强支撑。 50% hurts
278	    rate 是对称参数网格的自然结果，但实际应用中 heterogeneity 方向未知， 因此 50% 是 prior probability of harm——足以证明
279	    global correction 不可盲目应用。 K-dependence 的 non-monotonicity (K=2 > K=4 for DIM)
280	    是一个需要在论文中 显式讨论的 subtle point，避免审稿人误读为 "more subgroups → always worse"。
281	
282	    '
283	- name: Semi-Synthetic CSS Benchmark (TweetEval Sentiment)
284	  plan_id: exp-003
285	  description: 'TweetEval sentiment (N=45K) 上注入已知 CATE heterogeneity structure， GPT-4.1
286	    annotation，K=4 subgroups (text features: has_hashtag × text_length)， 100 MC runs，5
287	    methods 对比 (oracle/naive/global/stratified_mle/hb_ec_hte)。
288	
289	    '
290	  expected_results:
291	    n_subgroups: 4
292	    misclass_rates:
293	      S0: 0.05
294	      S1: 0.1
295	      S2: 0.15
296	      S3: 0.25
297	    subgroup_sizes:
298	      S0: ~38%
299	      S1: ~38%
300	      S2: ~12%
301	      S3: ~12%
302	    delta_pi: 0.2
303	    debiasing_hurts_confirmed: true
304	    mc_runs: 100
305	    hb_vs_mle_n100_S3_extreme_rmse_improvement: +60%
306	    hb_vs_mle_n100_S3_moderate_rmse_improvement: +24%
307	    hb_vs_mle_n250_S3_rmse_improvement: +5-17%
308	    hb_vs_mle_n500_convergence: <1.6% difference
309	    boundary_condition: n_expert≥100 recommended
310	    n50_S3_hb_worse: true
311	    n50_S3_hb_degradation: -57% RMSE
312	  result_rationale: 'S3 (highest error subgroup, ~12% of data) 是 EC-HTE 的 critical
313	    test： n=100 时 HB 大幅优于 MLE (+60%) 因为 S3 仅有 ~12 expert labels (100×0.12)， MLE 的
314	    confusion matrix 估计极不稳定，而 HB 从其他 3 个子群借力。 n=50 时 HB 反而 worse (-57%) 因为每子群仅 ~6
315	    labels，所有子群的 CM 估计 都不可靠，shrinkage target (pooled estimate) 本身也有大方差——这是 boundary
316	    condition (n_expert/K < 25) 的直接体现。Δπ=0.20 落在 best 档 [0.1, 0.2] 上界， 因为 semi-synthetic
317	    设定中 text features 提供了真实的 annotation difficulty 变异 (hashtag presence 增加 misclassification
318	    ~0.07-0.10)。debiasing hurts 在 S0 (lowest error) 最显著：global correction 对已经几乎正确的子群过度校正。
319	
320	    '
321	  tables:
322	  - title: Method Comparison — K=4, Extreme Regime
323	    columns:
324	    - n_expert
325	    - subgroup
326	    - oracle_rmse
327	    - naive_rmse
328	    - global_rmse
329	    - mle_rmse
330	    - hb_rmse
331	    rows:
332	    - - 100
333	      - S0
334	      - 0.025
335	      - 0.042
336	      - 0.068
337	      - 0.055
338	      - 0.048
339	    - - 100
340	      - S1
341	      - 0.025
342	      - 0.058
343	      - 0.052
344	      - 0.061
345	      - 0.054
346	    - - 100
347	      - S2
348	      - 0.035
349	      - 0.085
350	      - 0.072
351	      - 0.098
352	      - 0.075
353	    - - 100
354	      - S3
355	      - 0.04
356	      - 0.125
357	      - 0.095
358	      - 0.28
359	      - 0.112
360	    - - 250
361	      - S3
362	      - 0.04
363	      - 0.125
364	      - 0.095
365	      - 0.085
366	      - 0.081
367	    - - 500
368	      - S3
369	      - 0.04
370	      - 0.125
371	      - 0.095
372	      - 0.072
373	      - 0.071
374	  - title: Debiasing Hurts Verification (Global vs Naive |bias|)
375	    columns:
376	    - subgroup
377	    - naive_bias
378	    - global_bias
379	    - ratio
380	    - direction
381	    rows:
382	    - - S0
383	      - 0.008
384	      - 0.035
385	      - 4.4
386	      - global hurts
387	    - - S1
388	      - 0.025
389	      - 0.022
390	      - 0.9
391	      - global helps slightly
392	    - - S2
393	      - 0.045
394	      - 0.038
395	      - 0.8
396	      - global helps
397	    - - S3
398	      - 0.095
399	      - 0.065
400	      - 0.7
401	      - global helps
402	  figures_description:
403	  - Per-subgroup RMSE across n_expert, 5 methods 分色, S3 单独高亮
404	  - 'Debiasing hurts demonstration: S0 的 naive vs global bias bar chart'
405	  analysis: 'semi-synthetic 设定的价值在于保留了 real text features 的 annotation difficulty
406	    structure (Δπ 来自真实 GPT-4.1 misclassification patterns)，同时 ground-truth CATE 已知。S3
407	    是 minority subgroup (12%) with highest error——这是 CSS 场景中的 typical pattern (rare
408	    categories harder to classify)。HB 的 sweet spot n=100-250 对应 实际预算中 reasonable expert
409	    label investment。boundary condition n<50 的公开 增强 paper credibility。
410	
411	    '
412	- name: Real-Data Case Study (UC Berkeley Hate Speech)
413	  plan_id: exp-004
414	  description: 'UC Berkeley Measuring Hate Speech 数据集上的 pattern consistency 分析。 GPT-4.1
415	    annotation，platform_group × text_length 定义 4 subgroups， 展示 global vs EC-HTE 产生
416	    qualitatively different CATE 分布。
417	
418	    '
419	  expected_results:
420	    dataset: UC Berkeley Measuring Hate Speech
421	    n_comments: 2496
422	    subgroups:
423	      plat0_long: 624
424	      plat0_short: 624
425	      plat23_long: 624
426	      plat23_short: 624
427	    delta_pi: 0.117
428	    global_FPR: 0.139
429	    global_FNR: 0.533
430	    misclass_heterogeneity_confirmed: true
431	    ec_hte_vs_global_qualitative_difference: true
432	    bootstrap_ci_overlap: wide, inconclusive on point estimates
433	    avg_abs_bias_naive: 0.21
434	    avg_abs_bias_global: 0.273
435	    avg_abs_bias_ec_hte: 0.313
436	  result_rationale: 'Δπ=0.117 落在 best 档 [0.1, 0.2] 下界附近，因为 text features (platform
437	    × length) 提供的 misclassification heterogeneity 是 moderate 的——不如 demographic subgroups
438	    那么极端，但足以证明 heterogeneity 是 structural 而非 artifact。 EC-HTE avg |bias| (0.313) 高于
439	    global (0.273) 看似 counterintuitive，但在 best 档下 这是可接受的：(1) 高 FNR (53%) 意味着 confusion
440	    matrix 严重 asymmetric， correction 的 variance 很大；(2) 无 ground-truth CATE，这些 "bias"
441	    数值 是相对于 semi-synthetic injected CATEs 的 proxy；(3) best 档的 narrative 将此 framed
442	    as "pattern consistency illustration" 而非 "EC-HTE outperforms"。 核心 deliverable
443	    是 Δπ>0.1 在 real data 上的确认，以及 qualitative difference in CATE distributions——审稿人需要看到方法在
444	    real data 上产生 non-trivial 差异。
445	
446	    '
447	  tables:
448	  - title: Subgroup Misclassification Rates (GPT-4.1)
449	    columns:
450	    - subgroup
451	    - n
452	    - misclass_rate
453	    - FPR
454	    - FNR
455	    rows:
456	    - - plat0_long
457	      - 624
458	      - 0.266
459	      - 0.08
460	      - 0.55
461	    - - plat0_short
462	      - 624
463	      - 0.337
464	      - 0.12
465	      - 0.62
466	    - - plat23_long
467	      - 624
468	      - 0.303
469	      - 0.1
470	      - 0.58
471	    - - plat23_short
472	      - 624
473	      - 0.383
474	      - 0.18
475	      - 0.65
476	  - title: CATE Estimate Comparison (bootstrap means)
477	    columns:
478	    - subgroup
479	    - naive_cate
480	    - global_cate
481	    - ec_hte_cate
482	    - ci_width
483	    rows:
484	    - - plat0_long
485	      - 0.15
486	      - 0.22
487	      - 0.19
488	      - 0.35
489	    - - plat0_short
490	      - 0.08
491	      - 0.14
492	      - 0.11
493	      - 0.38
494	    - - plat23_long
495	      - 0.21
496	      - 0.28
497	      - 0.24
498	      - 0.32
499	    - - plat23_short
500	      - 0.12
501	      - 0.18
502	      - 0.15
503	      - 0.4
504	  figures_description:
505	  - Global vs EC-HTE CATE distribution comparison (4 subgroups, bootstrap violin plots)
506	  analysis: 'real data 的角色在 best 档中被精确定位为 "consistent illustration"： (1) Δπ=0.117
507	    确认 misclassification heterogeneity 在 real data 上存在且 non-trivial； (2) 三种方法产生 qualitatively
508	    different CATE distributions； (3) wide bootstrap CIs 诚实地报告了估计的不确定性。 高 FNR (53%)
509	    本身是有价值的 finding——说明 LLM 在 hate speech detection 上 系统性 under-classify dehumanization，为
510	    EC-HTE 的 practical relevance 提供动机。 审稿人可能 question 为什么 EC-HTE 不 outperform global——response
511	    是 "这正是 Claim 3 diagnostic criterion 的价值：Δπ×Δτ 在此 dataset 上 moderate， full stratified
512	    correction 的 variance cost 不完全 justified"。
513	
514	    '
515	- name: Diagnostic Criterion Validation (Cross-Validated)
516	  plan_id: exp-005
517	  description: 'Δπ×Δτ product 作为 diagnostic criterion 的 ROC 分析。 必须使用 leave-one-setting-out
518	    CV 而非 in-sample AUC。 从 exp-001/003 的所有 experimental settings 中计算 criterion。
519	
520	    '
521	  expected_results:
522	    subgroup_level_auc_insample: 0.833
523	    subgroup_correlation: 0.86
524	    diagnostic_auc_cv: 0.78
525	    setting_level_auc_insample: 0.49
526	    low_pi_hurt_pct: 84.6
527	    high_pi_hurt_pct: 15.4
528	    cv_method: leave-one-setting-out
529	    optimal_threshold_cv: 0.035
530	    sensitivity_at_threshold: 0.82
531	    specificity_at_threshold: 0.71
532	  result_rationale: 'CV AUC 0.78 落在 best 档 [0.75, 0.85]。in-sample subgroup AUC=0.833
533	    降至 CV 0.78 因为 leave-one-setting-out 移除了同一 setting 内子群间的相关性—— 同一 regime 下的子群共享
534	    CATE heterogeneity 参数，in-sample 时这是 "information leak"。 0.78 的 CV AUC 仍然 strong
535	    enough 因为 diagnostic criterion 的实用性 不要求完美分类：false negatives (低 Δπ×Δτ 但 global
536	    仍 hurts) 的代价是 unnecessarily using global correction (效率损失但不引入 bias)， 而 false positives
537	    的代价是 unnecessarily stratifying (多花 expert labels)。 两种 error 的 asymmetric cost
538	    使得 0.78 AUC 在 practical decision-making 中 足够有效。setting-level AUC=0.49 (near random)
539	    是因为 setting 内混合了 hurt/help 子群，setting-level prediction 本质上是 ill-defined—— 这恰好支持了
540	    subgroup-level diagnostic 的必要性。
541	
542	    '
543	  tables:
544	  - title: Diagnostic Criterion ROC Summary
545	    columns:
546	    - evaluation
547	    - AUC
548	    - n_settings
549	    - n_subgroups
550	    - method
551	    rows:
552	    - - in-sample subgroup
553	      - 0.833
554	      - 24
555	      - 72
556	      - logistic regression on Δπ×Δτ
557	    - - CV subgroup
558	      - 0.78
559	      - 24
560	      - 72
561	      - leave-one-setting-out
562	    - - in-sample setting
563	      - 0.49
564	      - 24
565	      - 24
566	      - majority vote
567	  - title: Threshold Analysis (CV)
568	    columns:
569	    - threshold
570	    - sensitivity
571	    - specificity
572	    - F1
573	    - n_flagged
574	    rows:
575	    - - 0.02
576	      - 0.92
577	      - 0.55
578	      - 0.68
579	      - 42
580	    - - 0.035
581	      - 0.82
582	      - 0.71
583	      - 0.76
584	      - 35
585	    - - 0.05
586	      - 0.7
587	      - 0.82
588	      - 0.76
589	      - 28
590	    - - 0.075
591	      - 0.55
592	      - 0.9
593	      - 0.68
594	      - 20
595	  figures_description:
596	  - 'ROC curve: in-sample vs CV, with optimal threshold annotated'
597	  - 'Scatter plot: Δπ×Δτ product vs actual |bias ratio|, colored by CV fold'
598	  analysis: 'diagnostic criterion 从 setting-level 重构为 subgroup-level 预测任务后 AUC 从 0.49
599	    跃升至 0.78 (CV)，确认了 best 档的核心假设。 in-sample 到 CV 的 drop (~0.05) 是 moderate 的，说明 criterion
600	    的 generalization 合理。optimal threshold 0.035 可直接用于 practical guideline： "if Δπ×Δτ
601	    > 0.035 from pilot data, use EC-HTE; otherwise global correction is safe"。
602	
603	    '
604	- name: Expert Label Budget Sensitivity
605	  plan_id: exp-006
606	  description: '系统性 sweep n_expert ∈ {50,100,250,500,1000,2000} × K ∈ {2,4,8} × regime
607	    ∈ {extreme,moderate}。 找到 EC-HTE > Global 的 RMSE crossover point。验证 HB partial
608	    pooling 在小 n 的价值。
609	
610	    '
611	  expected_results:
612	    n_mc: 100
613	    total_configs: 36
614	    crossover_hb_beats_global:
615	      K2_extreme: 250
616	      K2_moderate: never (global always better)
617	      K4_extreme: 1000
618	      K4_moderate: 2000
619	      K8_extreme: 1500
620	      K8_moderate: never
621	    hb_vs_mle_pct_configs_hb_better: 87.5
622	    hb_best_improvement_K4_moderate_n50: +42.4% RMSE
623	    convergence_threshold: 'n≥1000: HB ≈ MLE <0.5%'
624	  result_rationale: 'crossover at K=2/extreme n=250 落在 best 档 [200, 300] 因为 2 subgroups
625	    with extreme heterogeneity (Δπ≥0.15) 意味着 per-subgroup CM estimation 只需 ~125 labels/subgroup
626	    即可击败 global pooling 的 systematic bias。 K=4/extreme 需要 n=1000 (更高) 因为 4 subgroups
627	    分摊 expert budget， per-subgroup labels 仅 ~250——需要更多总量才能让 stratified estimation
628	    的 variance 低于 global 的 bias。K=2/moderate "never crosses" 因为 moderate heterogeneity
629	    (Δπ~0.05) 下 global correction 的 bias 小于 stratified 的 additional variance——这是 diagnostic
630	    criterion (Claim 3) 正确预测的情形。 K=8 介于 K=4 和 "too many subgroups" 之间，crossover at
631	    1500 for extreme 说明 K=8 仍然 feasible 但 cost-prohibitive for most studies。 HB 在
632	    87.5% configs 优于 MLE 因为 symmetric DGP 下 partial pooling 几乎 never hurts (worst
633	    case: 0.1% worse when all subgroups have identical error)。
634	
635	    '
636	  tables:
637	  - title: RMSE Crossover Points (n_expert where EC-HTE < Global)
638	    columns:
639	    - K
640	    - regime
641	    - crossover_n
642	    - per_subgroup_at_crossover
643	    - practical_feasibility
644	    rows:
645	    - - 2
646	      - extreme
647	      - 250
648	      - 125
649	      - feasible
650	    - - 2
651	      - moderate
652	      - ∞
653	      - N/A
654	      - global always better
655	    - - 4
656	      - extreme
657	      - 1000
658	      - 250
659	      - feasible but expensive
660	    - - 4
661	      - moderate
662	      - 2000
663	      - 500
664	      - expensive
665	    - - 8
666	      - extreme
667	      - 1500
668	      - 188
669	      - expensive
670	    - - 8
671	      - moderate
672	      - ∞
673	      - N/A
674	      - global always better
675	  - title: HB vs MLE Improvement Summary
676	    columns:
677	    - K
678	    - n_expert
679	    - configs_hb_better
680	    - best_improvement
681	    - worst_degradation
682	    rows:
683	    - - 2
684	      - 50
685	      - 3/4
686	      - +8.7%
687	      - -0.2%
688	    - - 4
689	      - 50
690	      - 7/8
691	      - +42.4%
692	      - -1.1%
693	    - - 2
694	      - 1000
695	      - 2/4
696	      - +0.3%
697	      - -0.1%
698	    - - 4
699	      - 1000
700	      - 4/8
701	      - +0.5%
702	      - -0.3%
703	  figures_description:
704	  - 'Budget crossover curves: RMSE(EC-HTE)/RMSE(Global) vs n_expert, 分 K 和 regime
705	    六面板'
706	  analysis: 'budget sensitivity 的核心 narrative：EC-HTE 值得投资 IFF (1) diagnostic criterion
707	    flags high heterogeneity (extreme regime) AND (2) budget ≥ crossover threshold。
708	    这直接连接 Claim 2 (method) 和 Claim 3 (diagnostic)。 Expert Budget Recommendation subsection
709	    的数据基础完备。
710	
711	    '
712	- name: PPCI + DSL Baseline Comparison
713	  plan_id: exp-007
714	  description: '(a) PPCI vs EC-HTE on 4 DGPs (covariate-only, outcome-only, both,
715	    none)； (b) per-subgroup DSL baseline；(c) EC-HTE+PPCI composition； (d) pure covariate-error
716	    control condition。8 methods × 4 DGPs × 100 MC。
717	
718	    '
719	  expected_results:
720	    total_rows: 6912
721	    methods: 8
722	    dgps:
723	    - A_covariate_only
724	    - B_outcome_only
725	    - C_both_errors
726	    - D_no_error
727	    mc_runs: 100
728	    dgp_c_extreme_n250_k2:
729	      ec_hte_ppci_bias_z0: 0.005
730	      ec_hte_ppci_rmse_z0: 0.225
731	      ec_hte_bias_z0: 0.178
732	      ec_hte_rmse_z0: 0.226
733	      ppci_bias_z0: 0.004
734	      ppci_rmse_z0: 0.261
735	      naive_bias_z0: 0.251
736	    ec_hte_ppci_bias_reduction_vs_ec_hte: 35x
737	    dgp_a_ec_hte_dominates_ppci: true
738	    dgp_b_ppci_dominates_ec_hte: true
739	    dsl_per_subgroup_vs_ec_hte: EC-HTE wins by 15-25% RMSE via shrinkage
740	    coverage_ec_hte_ppci: 1.0
741	  result_rationale: 'DGP C (both errors) 中 ec_hte_ppci 的 0.005 bias 落在 best 档 [0.002,
742	    0.01] 因为 EC-HTE 和 PPCI 在 composition 中是 necessary and sufficient： EC-HTE 的 M⁻¹
743	    correction 消除 structured covariate error (从 0.251 → 0.178)， PPCI 的 residual rectifier
744	    消除 remaining outcome error (从 0.178 → 0.005)。 residual 0.005 来自有限样本 MC noise，不是
745	    systematic bias。 35x improvement 因为 ec_hte alone 在 DGP C 中仅修正了 covariate-side，
746	    outcome-side error (FNR/FPR asymmetry) 贡献了 ~0.17 的 residual bias。 DGP A 中 EC-HTE
747	    dominates PPCI 因为 PPCI 的 general-purpose rectifier 不利用 confusion matrix structure——对
748	    pure covariate error， structured correction (M⁻¹) 比 nonparametric rectifier 更
749	    efficient。 DSL per-subgroup 比 EC-HTE 差 15-25% RMSE 因为缺少 cross-subgroup shrinkage，
750	    每个子群独立估计 correction factor，variance 更高。
751	
752	    '
753	  tables:
754	  - title: DGP C — Method Comparison (K=2, extreme, n=250)
755	    columns:
756	    - method
757	    - bias_z0
758	    - rmse_z0
759	    - coverage_z0
760	    - bias_z1
761	    - rmse_z1
762	    rows:
763	    - - naive
764	      - 0.251
765	      - 0.269
766	      - 0.82
767	      - 0.195
768	      - 0.225
769	    - - global
770	      - 0.185
771	      - 0.215
772	      - 0.85
773	      - 0.142
774	      - 0.185
775	    - - ec_hte
776	      - 0.178
777	      - 0.226
778	      - 0.92
779	      - 0.125
780	      - 0.195
781	    - - ppci
782	      - 0.004
783	      - 0.261
784	      - 1.0
785	      - 0.003
786	      - 0.248
787	    - - ec_hte_ppci
788	      - 0.005
789	      - 0.225
790	      - 1.0
791	      - 0.004
792	      - 0.212
793	    - - dsl_subgroup
794	      - 0.008
795	      - 0.275
796	      - 0.95
797	      - 0.006
798	      - 0.26
799	  - title: Complementarity Matrix (which method dominates in which DGP)
800	    columns:
801	    - DGP
802	    - best_method
803	    - bias
804	    - rationale
805	    rows:
806	    - - A_covariate
807	      - ec_hte
808	      - 0.008
809	      - structured M⁻¹ correction optimal
810	    - - B_outcome
811	      - ppci
812	      - 0.003
813	      - rectifier captures outcome error
814	    - - C_both
815	      - ec_hte_ppci
816	      - 0.005
817	      - composition covers both error types
818	    - - D_none
819	      - oracle≈naive
820	      - 0.002
821	      - no correction needed
822	  figures_description:
823	  - '4-panel DGP comparison: bias bar chart per method, DGP A-D'
824	  - 'EC-HTE + PPCI composition diagram: covariate correction → outcome correction
825	    pipeline'
826	  analysis: 'complementarity structure 完美支撑 Contribution #4：ec_hte 和 ppci 各自 necessary
827	    (单独都不足以处理 dual error)，composition sufficient (bias → near-zero)。 这不是 trivial 的
828	    stacking——ec_hte 的 M⁻¹ correction 改变了 PPCI 的 input distribution， 使 rectifier 只需处理
829	    residual outcome error 而非混合的 covariate+outcome error。 DSL per-subgroup 作为 baseline
830	    展示了 shrinkage 的价值。
831	
832	    '
833	- name: Multiple LLM Annotator Comparison
834	  plan_id: exp-008
835	  description: 'GPT-3.5-turbo, GPT-4.1, GPT-4o, GPT-4o-mini, GPT-4-turbo, GPT-5.4
836	    六个模型 在 TweetEval sentiment 上的 misclassification heterogeneity patterns。 验证 heterogeneity
837	    是 structural (跨模型一致) 而非 model-specific artifact。
838	
839	    '
840	  expected_results:
841	    models_completed: 6
842	    effective_delta_pi:
843	      gpt-3.5-turbo: 0.198
844	      gpt-4-turbo: 0.149
845	      gpt-4.1: 0.098
846	      gpt-4o: 0.08
847	      gpt-4o-mini: 0.136
848	      gpt-5.4: 0.114
849	    all_delta_pi_above_005: true
850	    multi_llm_delta_pi_min: 0.08
851	    worst_subgroup_consensus: True_medium (5/6 models)
852	    cross_model_spearman_significant_pairs: 4
853	  result_rationale: '所有 6 个模型 Δπ > 0.05 (best 档 min [0.05, 0.08] 的 0.080 落在范围内) 因为
854	    misclassification heterogeneity 的 root cause 是 text features (hashtag, length)
855	    对 annotation difficulty 的 structural effect——不同模型有不同 overall accuracy， 但 difficulty
856	    ranking 相似 (True_medium 最难: 含 hashtag 的中等长度 text 语义歧义最大)。GPT-3.5-turbo Δπ 最高 (0.198)
857	    因为 overall accuracy 最低时 per-subgroup variance 也最大；GPT-4o Δπ 最低 (0.080) 因为是最强模型，
858	    error rates 被压缩但 heterogeneity 的 relative pattern 仍存。 significant Spearman pairs
859	    (4/15) 受限于仅 4 个 subgroups 的 statistical power—— 但 qualitative agreement (5/6 agree
860	    on worst subgroup) 提供了 stronger evidence。
861	
862	    '
863	  tables:
864	  - title: Cross-Model Misclassification Heterogeneity
865	    columns:
866	    - model
867	    - overall_accuracy
868	    - delta_pi
869	    - worst_subgroup
870	    - best_subgroup
871	    rows:
872	    - - gpt-3.5-turbo
873	      - 0.72
874	      - 0.198
875	      - True_medium
876	      - False_medium
877	    - - gpt-4-turbo
878	      - 0.81
879	      - 0.149
880	      - True_medium
881	      - False_medium
882	    - - gpt-4.1
883	      - 0.86
884	      - 0.098
885	      - True_medium
886	      - False_short
887	    - - gpt-4o
888	      - 0.88
889	      - 0.08
890	      - True_medium
891	      - False_medium
892	    - - gpt-4o-mini
893	      - 0.83
894	      - 0.136
895	      - True_medium
896	      - False_medium
897	    - - gpt-5.4
898	      - 0.9
899	      - 0.114
900	      - True_short
901	      - False_medium
902	  - title: Per-Subgroup Misclass Rates by Model
903	    columns:
904	    - model
905	    - False_medium
906	    - False_short
907	    - True_medium
908	    - True_short
909	    rows:
910	    - - gpt-3.5-turbo
911	      - 0.12
912	      - 0.15
913	      - 0.32
914	      - 0.25
915	    - - gpt-4.1
916	      - 0.1
917	      - 0.14
918	      - 0.2
919	      - 0.17
920	    - - gpt-4o
921	      - 0.08
922	      - 0.11
923	      - 0.16
924	      - 0.14
925	    - - gpt-5.4
926	      - 0.07
927	      - 0.1
928	      - 0.18
929	      - 0.15
930	  figures_description:
931	  - Per-subgroup misclass rate profile across 6 models (parallel coordinates plot)
932	  analysis: 'multi-LLM evidence 将 paper 的 contribution 从 "GPT-4.1-specific finding"
933	    提升为 "structural phenomenon across LLM generations"。worst_subgroup consensus (True_medium,
934	    5/6) 说明 text features 对 annotation difficulty 的 effect 是 robust to model architecture/scale。这直接支持了
935	    "heterogeneity is inherent to the task, not the model" 的 narrative，strengthening
936	    Claim 1 的 practical relevance。 Move to appendix per writing requirements (exp-008/009
937	    → appendix)。
938	
939	    '
940	- name: Adaptive Expert Annotation Allocation
941	  plan_id: exp-009
942	  description: 'CATE-weighted allocation (targeting high-CATE × high-error subgroups)
943	    vs uniform allocation vs uncertainty-only allocation。100 MC runs， K=4, extreme
944	    regime, n_expert ∈ {100, 250, 500}。
945	
946	    '
947	  expected_results:
948	    n_mc: 100
949	    K: 4
950	    regime: extreme
951	    n_expert_grid:
952	    - 100
953	    - 250
954	    - 500
955	    allocation_strategies:
956	    - uniform
957	    - uncertainty_only
958	    - cate_weighted
959	    rmse_improvement_cate_weighted_vs_uniform:
960	      n100: 8-15%
961	      n250: 5-10%
962	      n500: 2-5%
963	    bias_improvement_cate_weighted_vs_uniform:
964	      n100: 12-20%
965	      n250: 8-12%
966	      n500: 3-6%
967	    uncertainty_only_vs_uniform: 3-8% RMSE improvement
968	    optimal_allocation_fraction_high_error_subgroup: ~2x proportional
969	    diminishing_returns_at_n500: true
970	  result_rationale: 'CATE-weighted allocation 在 n=100 时改进最大 (8-15% RMSE) 因为 budget
971	    最紧张时 将 disproportionate labels 分配给 high-CATE × high-error 子群的 marginal value 最高：
972	    这些子群同时具有 (1) 最不稳定的 CM 估计 (high error → high variance) 和 (2) 最高的 CATE bias impact
973	    (high CATE → bias 对 final estimate 影响最大)。 n=500 时 diminishing returns (2-5%) 因为所有子群的
974	    CM 估计都已 reasonably stable， allocation 优化的 marginal gain 被 Monte Carlo noise 淹没。
975	    uncertainty_only (仅 target high error, 不考虑 CATE magnitude) 比 uniform 好但 不如 cate_weighted
976	    因为忽略了 CATE heterogeneity——high-error 但 near-zero CATE 的 子群对 overall CATE 估计的影响有限。optimal
977	    allocation ~2x proportional 到 high-error subgroup 是 bias-variance tradeoff 的结果：过度分配
978	    (>3x) 牺牲了 其他子群的 estimation quality。
979	
980	    '
981	  tables:
982	  - title: Allocation Strategy Comparison (K=4, extreme)
983	    columns:
984	    - n_expert
985	    - strategy
986	    - mean_rmse
987	    - mean_bias
988	    - coverage
989	    - alloc_sgC
990	    rows:
991	    - - 100
992	      - uniform
993	      - 0.185
994	      - 0.095
995	      - 0.88
996	      - 25
997	    - - 100
998	      - uncertainty
999	      - 0.172
1000	      - 0.085
1001	      - 0.9
1002	      - 35
1003	    - - 100
1004	      - cate_weighted
1005	      - 0.16
1006	      - 0.078
1007	      - 0.91
1008	      - 42
1009	    - - 250
1010	      - uniform
1011	      - 0.12
1012	      - 0.058
1013	      - 0.92
1014	      - 62
1015	    - - 250
1016	      - uncertainty
1017	      - 0.112
1018	      - 0.052
1019	      - 0.93
1020	      - 88
1021	    - - 250
1022	      - cate_weighted
1023	      - 0.108
1024	      - 0.048
1025	      - 0.94
1026	      - 105
1027	    - - 500
1028	      - uniform
1029	      - 0.082
1030	      - 0.032
1031	      - 0.94
1032	      - 125
1033	    - - 500
1034	      - uncertainty
1035	      - 0.079
1036	      - 0.03
1037	      - 0.95
1038	      - 175
1039	    - - 500
1040	      - cate_weighted
1041	      - 0.078
1042	      - 0.029
1043	      - 0.95
1044	      - 210
1045	  - title: Improvement Summary
1046	    columns:
1047	    - n_expert
1048	    - cate_weighted_vs_uniform_rmse
1049	    - cate_weighted_vs_uncertainty_rmse
1050	    rows:
1051	    - - 100
1052	      - +13.5%
1053	      - +7.0%
1054	    - - 250
1055	      - +10.0%
1056	      - +3.6%
1057	    - - 500
1058	      - +4.9%
1059	      - +1.3%
1060	  figures_description:
1061	  - Three allocation strategies' RMSE curves across n_expert, with per-subgroup breakdown
1062	  analysis: 'adaptive allocation 是 P2 实验，在 best 档下放入 appendix。其价值在于回应 审稿人可能的 "how
1063	    to optimally spend expert budget" 问题。CATE-weighted allocation 的 8-15% improvement
1064	    at n=100 说明 budget-constrained 场景下 allocation matters，但 n≥500 时差异消失——consistent
1065	    with exp-006 的 convergence。 这为 future work 提供了一个 concrete extension point 而不是
1066	    current paper 的 core contribution。
1067	
1068	    '
1069	- name: Robustness to Misspecified Subgroup Structure
1070	  plan_id: exp-010
1071	  description: '测试 EC-HTE 在 subgroup 定义含噪声或 misaligned 时的 graceful degradation。 noise_level
1072	    ∈ {0, 0.1, 0.25, 0.5}，K=2 和 K=4。
1073	
1074	    '
1075	  expected_results:
1076	    n_mc: 100
1077	    noise_levels:
1078	    - 0
1079	    - 0.1
1080	    - 0.25
1081	    - 0.5
1082	    coverage_hb_range:
1083	    - 0.945
1084	    - 0.96
1085	    coverage_naive_range:
1086	    - 0.875
1087	    - 0.92
1088	    coverage_global_range:
1089	    - 0.925
1090	    - 0.953
1091	    hb_beats_mle_all_configs: true
1092	    graceful_convergence_at_50pct: true
1093	    hb_improvement_over_mle_range: +0.1% to +0.9% RMSE
1094	  result_rationale: 'HB coverage 在所有 noise levels 保持 0.945-0.960 (落在 best 档 [0.92,
1095	    0.97]) 因为 partial pooling 的核心机制：当 subgroup labels 含噪声时，per-subgroup CM 估计变差，但
1096	    HB 的 shrinkage 自动增加 pooling weight，将估计拉向 global mean—— 效果等同于自适应地从 "full stratification"
1097	    回退到 "global correction"。 noise=0.5 时 HB ≈ Global 因为 50% random label swap 使 subgroup
1098	    membership 几乎 uninformative，HB 正确地近乎完全 pool。这是 James-Stein shrinkage 的 经典行为。naive
1099	    coverage 低 (87-92%) 因为不做 correction 的 CI 不 account for misclassification error。graceful
1100	    degradation 而非 catastrophic failure 直接回应了 Anticipated Reviewer Concern #4。
1101	
1102	    '
1103	  tables:
1104	  - title: Coverage Across Noise Levels
1105	    columns:
1106	    - K
1107	    - noise
1108	    - coverage_naive
1109	    - coverage_global
1110	    - coverage_hb
1111	    - hb_vs_mle_rmse
1112	    rows:
1113	    - - 2
1114	      - 0.0
1115	      - 0.875
1116	      - 0.925
1117	      - 0.958
1118	      - +0.8%
1119	    - - 2
1120	      - 0.1
1121	      - 0.877
1122	      - 0.935
1123	      - 0.948
1124	      - +0.6%
1125	    - - 2
1126	      - 0.25
1127	      - 0.89
1128	      - 0.932
1129	      - 0.95
1130	      - +0.4%
1131	    - - 2
1132	      - 0.5
1133	      - 0.897
1134	      - 0.945
1135	      - 0.945
1136	      - +0.1%
1137	    - - 4
1138	      - 0.0
1139	      - 0.904
1140	      - 0.93
1141	      - 0.956
1142	      - +0.9%
1143	    - - 4
1144	      - 0.1
1145	      - 0.916
1146	      - 0.953
1147	      - 0.958
1148	      - +0.7%
1149	    - - 4
1150	      - 0.25
1151	      - 0.909
1152	      - 0.948
1153	      - 0.96
1154	      - +0.5%
1155	    - - 4
1156	      - 0.5
1157	      - 0.919
1158	      - 0.944
1159	      - 0.946
1160	      - +0.1%
1161	  figures_description:
1162	  - Coverage vs noise level, 3 methods 分色, K=2/K=4 双面板
1163	  analysis: 'coverage 作为 decisive metric (而非 bias 或 RMSE) 的定位在 best 档下特别有效： naive
1164	    87-92% = systematically under-covers，EC-HTE 95-96% = near-nominal， global 93-95%
1165	    = intermediate。HB 的 graceful degradation 是方法论上的 strong point， 直接回应 "misspecified
1166	    subgroups" 的审稿人顾虑。
1167	
1168	    '
1169	- name: Causal Forest Integration
1170	  plan_id: exp-011
1171	  description: 'EC-HTE post-hoc correction on CausalForestDML subgroup CATE estimates。
1172	    naive_forest vs global_forest vs ec_hte_forest，100 MC，8 configs。 验证 nonlinear
1173	    estimator 下 debiasing-hurts amplification (up to 5.9x for K=4)。
1174	
1175	    '
1176	  expected_results:
1177	    n_mc: 100
1178	    n_configs: 8
1179	    mean_abs_bias:
1180	      naive_forest: 0.156
1181	      global_forest: 0.107
1182	      ec_hte_forest: 0.061
1183	    mean_rmse:
1184	      naive_forest: 0.178
1185	      global_forest: 0.166
1186	      ec_hte_forest: 0.229
1187	    debiasing_hurts_max_ratio: 5.9
1188	    debiasing_hurts_detail: 'K=4/extreme/sg0: global 5.9x worse than naive'
1189	    k2_n500_ec_hte_bias_range:
1190	    - 0.004
1191	    - 0.013
1192	    bias_amplification_max_cf: 5.9
1193	    ec_hte_bias_reduction_factor_vs_global: 2.6
1194	  result_rationale: 'CausalForest 的 5.9x amplification (best 档 [5.0, 6.5]) 显著高于 DIM
1195	    的 2.41-2.86x 因为 tree-based estimator 在 subgroup 内部进一步分裂， 每个 leaf 的 CATE 估计噪声在
1196	    global correction 时被 heterogeneously amplified。 具体机制：CausalForest 的 honest splitting
1197	    将 sample 减半， per-leaf sample size 更小 → CM correction 的 M⁻¹ operation 放大了 leaf-level
1198	    estimation noise → subgroup aggregation 时 noise 不 cancel 而 compound。 K=4/extreme
1199	    最严重因为 4 个子群中 sg0 (lowest error) 被 global CM 过度校正， 且 forest 的 nonlinear estimation
1200	    使得 over-correction 的 propagation 是 multiplicative 而非 additive。ec_hte_forest 的
1201	    mean |bias| 0.061 (vs global 0.107) 代表 ~2.6x bias reduction (落在 best 档 [2.0, 4.5])。RMSE
1202	    0.229 > global 0.166 体现了 bias-RMSE tradeoff (per-subgroup CM estimation variance
1203	    在 forest 上更大)， 这是 Writing Requirement #11 要求 disclose 的。
1204	
1205	    '
1206	  tables:
1207	  - title: CausalForest Method Comparison (mean across 8 configs)
1208	    columns:
1209	    - method
1210	    - mean_abs_bias
1211	    - mean_rmse
1212	    - debiasing_hurts_cases
1213	    rows:
1214	    - - naive_forest
1215	      - 0.156
1216	      - 0.178
1217	      - —
1218	    - - global_forest
1219	      - 0.107
1220	      - 0.166
1221	      - 9
1222	    - - ec_hte_forest
1223	      - 0.061
1224	      - 0.229
1225	      - 0
1226	  - title: Debiasing Hurts — CausalForest vs DIM
1227	    columns:
1228	    - estimator
1229	    - K
1230	    - max_ratio
1231	    - worst_config
1232	    - mechanism
1233	    rows:
1234	    - - DIM
1235	      - 2
1236	      - 2.86
1237	      - extreme/sg0
1238	      - additive over-correction
1239	    - - DIM
1240	      - 4
1241	      - 2.41
1242	      - extreme/sg0
1243	      - distributed over-correction
1244	    - - CausalForest
1245	      - 2
1246	      - 3.2
1247	      - extreme/sg0
1248	      - multiplicative via leaves
1249	    - - CausalForest
1250	      - 4
1251	      - 5.9
1252	      - extreme/sg0
1253	      - compounding leaf noise
1254	  - title: K=2, n_expert=500 — Near-Zero Bias Detail
1255	    columns:
1256	    - config
1257	    - ec_hte_bias
1258	    - global_bias
1259	    - naive_bias
1260	    - reduction_factor
1261	    rows:
1262	    - - extreme/sg0
1263	      - 0.004
1264	      - 0.109
1265	      - 0.052
1266	      - 27.3
1267	    - - extreme/sg1
1268	      - 0.013
1269	      - 0.033
1270	      - 0.085
1271	      - 2.5
1272	    - - moderate/sg0
1273	      - 0.008
1274	      - 0.045
1275	      - 0.028
1276	      - 5.6
1277	    - - moderate/sg1
1278	      - 0.011
1279	      - 0.022
1280	      - 0.065
1281	      - 2.0
1282	  figures_description:
1283	  - DIM vs CausalForest debiasing-hurts amplification comparison (grouped bar chart)
1284	  - ec_hte_forest bias across n_expert, showing convergence to near-zero
1285	  analysis: 'CausalForest integration 是 Claim 2 的 critical evidence：paper claims "CausalForestDML"
1286	    但仅有 DIM results 会被审稿人视为 claim-evidence gap。5.9x amplification strengthens Claim
1287	    1 ("debiasing can hurt even more with nonlinear estimators")。 bias-RMSE tradeoff
1288	    (ec_hte RMSE 38% higher than global) 必须在 paper 中 诚实讨论——defense: (1) bias 是 primary
1289	    metric for policy decisions， (2) RMSE 在 n≥500 时 competitive，(3) coverage 仍然 near-nominal。'
1290	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "652e3cf1-5a8c-4891-8f76-313c715ce75b",
  "isSidechain": false,
  "promptId": "b20fe594-a1fa-45c4-9afa-b12a0912be14",
  "type": "user",
  "uuid": "fd96649e-8bf9-4ec4-b93b-a737d7bde0f7",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/dream_reports/dream_20260521T122454/best/review_context.yaml",
      "content": "narrative_guidance: '三条 Claims 完整保留，Lead with ''debiasing can hurt'' (50% parameter\n  space, up to 5.9x amplification)。 EC-HTE 作为 principled fix，诊断准则作为 practical decision\n  tool。PPCI 互补性升级至 Contribution #4。 Real data 作为 consistent illustration (pattern\n  consistency, NOT ground-truth benchmark)。 Headline: ''Global correction worsens\n  subgroup CATE bias by 2-3x median; EC-HTE reduces bias to near-zero with 250 expert\n  labels; composition with PPCI achieves 0.005 bias under dual error.'' 审稿周期目标 1R\n  accept 或 minor revision。\n\n  '\nimagined_experiments:\n- name: Hierarchical Bayesian EC-HTE on Synthetic Data\n  plan_id: exp-001\n  description: 'HB Dirichlet-prior confusion matrix estimator with partial pooling，\n    full regime sweep (extreme/moderate/homogeneous × n_expert 100-2000 × K=2,4)，\n    与 MLE/Laplace 对比。100 MC runs per config，4-chain NUTS MCMC。\n\n    '\n  expected_results:\n    mcmc_rhat_max: 1.005\n    mcmc_ess_min: 1500\n    mcmc_divergent: 0\n    runtime_min: 70\n    total_mc_runs: 3600\n    hb_vs_mle_rmse_improvement_k2_n50: 4-9%\n    hb_vs_mle_rmse_improvement_k4_n50_moderate: 6-9%\n    hb_coverage_median: 0.93\n    hb_coverage_min: 0.87\n    hyperprior_sensitivity_k2_variation: <1%\n    hyperprior_sensitivity_k4_variation: ~4-5%\n    singularity_guard_triggers: extreme/n=50 only (2-3 per 100 runs)\n  result_rationale: 'best 档下 MCMC 收敛良好 (R̂<1.01, ESS>200) 因为 4-chain NUTS 提供充分探索，\n    Dirichlet 先验与 multinomial likelihood 共轭性保证后验几何良好。 HB 在 n=50 小样本时优势最大 (4-9% RMSE\n    improvement) 因为 partial pooling 的 James-Stein shrinkage 在信息稀缺时借力最强；n≥500 时 MLE\n    已有足够数据， HB 收敛至 MLE (<0.5% 差异)。coverage median 0.93 而非 0.95 因为 HB 后验 区间基于 MCMC\n    样本，有限 MC 引入的 discretization 导致轻微 undercoverage。 hyperprior sensitivity 在 K=4 时更大\n    (~4-5%) 因为 4 subgroup 的 Dirichlet 浓度参数影响更多自由度，但 coverage 不变说明 point estimate 对先验敏感\n    但区间宽度自适应补偿。\n\n    '\n  tables:\n  - title: HB vs MLE RMSE Comparison (K=2)\n    columns:\n    - regime\n    - n_expert\n    - subgroup\n    - hb_rmse\n    - mle_rmse\n    - improvement_pct\n    rows:\n    - - extreme\n      - 50\n      - z0\n      - 0.095\n      - 0.104\n      - 8.7\n    - - extreme\n      - 50\n      - z1\n      - 0.102\n      - 0.108\n      - 5.6\n    - - extreme\n      - 100\n      - z0\n      - 0.065\n      - 0.066\n      - 1.5\n    - - extreme\n      - 100\n      - z1\n      - 0.068\n      - 0.069\n      - 1.4\n    - - extreme\n      - 250\n      - z0\n      - 0.041\n      - 0.042\n      - 2.4\n    - - extreme\n      - 500\n      - z0\n      - 0.029\n      - 0.029\n      - 0.3\n    - - moderate\n      - 50\n      - z0\n      - 0.088\n      - 0.092\n      - 4.3\n    - - moderate\n      - 100\n      - z0\n      - 0.06\n      - 0.061\n      - 1.6\n  - title: HB vs MLE RMSE Comparison (K=4)\n    columns:\n    - regime\n    - n_expert\n    - subgroup\n    - hb_rmse\n    - mle_rmse\n    - improvement_pct\n    rows:\n    - - extreme\n      - 50\n      - sgC\n      - 0.99\n      - 1.3\n      - 23.8\n    - - moderate\n      - 50\n      - sgC\n      - 0.85\n      - 0.93\n      - 8.6\n    - - moderate\n      - 50\n      - sgB\n      - 0.42\n      - 0.52\n      - 19.2\n    - - extreme\n      - 100\n      - sgC\n      - 0.29\n      - 0.46\n      - 37.0\n    - - extreme\n      - 250\n      - sgC\n      - 0.14\n      - 0.15\n      - 6.7\n  - title: Hyperprior Sensitivity (scale ∈ {0.5, 1.0, 2.0})\n    columns:\n    - K\n    - metric\n    - scale_0.5\n    - scale_1.0\n    - scale_2.0\n    rows:\n    - - 2\n      - rmse_mean\n      - 0.0632\n      - 0.0635\n      - 0.0638\n    - - 4\n      - rmse_mean\n      - 0.182\n      - 0.175\n      - 0.168\n    - - 2\n      - coverage\n      - 0.93\n      - 0.93\n      - 0.93\n    - - 4\n      - coverage\n      - 0.92\n      - 0.93\n      - 0.93\n  figures_description:\n  - HB vs MLE RMSE ratio across n_expert (x-axis log scale), 分 K=2/K=4 和 extreme/moderate\n    四面板\n  analysis: 'HB partial pooling 的核心价值在小样本 (n_expert/K < 50)：shrinkage 将不稳定的 per-subgroup\n    MLE 拉向 pooled estimate，降低 variance。K=4/extreme/n=50 的 singularity guard 触发 (2-3/100\n    runs) 说明此边界条件下 MLE 本身不可靠， HB 的正则化是必要的。4-chain MCMC 相比 2-chain 的 ESS 提升 ~4x 确认\n    多链策略对 posterior geometry exploration 的价值。\n\n    '\n- name: Formal Bias Decomposition Verification\n  plan_id: exp-002\n  description: '解析推导 bias = Δπ × Δτ 的 exact identity，系统参数网格上 MC 验证。 K=2 和 K=4 分别验证。包含\n    ''debiasing can hurt'' proposition 的构造性证明。\n\n    '\n  expected_results:\n    r2_bias_identity_k2: 0.994\n    r2_bias_identity_k4: 0.974\n    tightness_ratio_k2_median: 1.003\n    tightness_ratio_k4_median: 1.023\n    debiasing_hurts_pct: 50\n    debiasing_hurts_threshold_delta_misclass: 0.12\n    max_bias_ratio_k2_extreme: 2.86\n    max_bias_ratio_k4_extreme: 2.41\n    coverage_2se_k2: 0.951\n    coverage_2se_k4: 0.94\n  result_rationale: 'R²=0.994 (K=2) 因为二子群下 bias identity 是 exact (population level)，\n    MC 偏差仅来自有限样本噪声 (N=5000, 100 MC runs)。K=4 的 R²=0.974 稍低 因为 sum-of-products form\n    中 4 个子群的 MC 噪声累积（4 个交叉项 vs K=2 的 1 个）， 但仍然是 identity 而非 bound。tightness ratio\n    ≈1.0 进一步确认这是 exact identity。 debiasing hurts 50% (260/520 non-trivial configs)\n    因为当 naive bias 方向与 global correction 方向同号时 correction 有效，异号时 amplify——对称参数网格下\n    恰好 50%。max_bias_ratio K=2 > K=4 (2.86 vs 2.41) 因为 DIM estimator 下 K=2 的两个子群 error\n    rate 差异最大化（所有 heterogeneity 集中在一个对比）， 而 K=4 将 heterogeneity 分散到多个对比，单个子群的 worst-case\n    amplification 反而降低。 这是 DIM estimator 的特性——CausalForest 行为相反 (exp-011)。\n\n    '\n  tables:\n  - title: Bias Identity R² Verification\n    columns:\n    - K\n    - n_configs\n    - R2\n    - tightness_median\n    - tightness_95pct\n    rows:\n    - - 2\n      - 260\n      - 0.994\n      - 1.003\n      - 1.012\n    - - 4\n      - 260\n      - 0.974\n      - 1.023\n      - 1.068\n  - title: Debiasing Hurts Analysis\n    columns:\n    - K\n    - total_configs\n    - hurts_count\n    - hurts_pct\n    - max_ratio\n    - worst_config\n    rows:\n    - - 2\n      - 260\n      - 130\n      - 50.0\n      - 2.86\n      - Δπ=0.20, Δτ=0.50\n    - - 4\n      - 260\n      - 130\n      - 50.0\n      - 2.41\n      - Δπ=0.20, Δτ=0.50\n  - title: Bias Amplification by Parameter Region\n    columns:\n    - delta_pi\n    - delta_tau\n    - k2_ratio\n    - k4_ratio\n    - direction\n    rows:\n    - - 0.05\n      - 0.1\n      - 1.12\n      - 1.08\n      - global improves\n    - - 0.05\n      - 0.5\n      - 1.45\n      - 1.32\n      - global improves\n    - - 0.15\n      - 0.1\n      - 1.85\n      - 1.62\n      - global hurts\n    - - 0.15\n      - 0.5\n      - 2.52\n      - 2.18\n      - global hurts\n    - - 0.2\n      - 0.5\n      - 2.86\n      - 2.41\n      - global hurts (maximum)\n  figures_description:\n  - Δπ × Δτ heatmap showing bias amplification factor，红色=global hurts, 蓝色=global helps\n  - Analytic prediction vs MC bias scatter plot with R² annotation, K=2 和 K=4 双面板\n  analysis: 'bias identity 的 exact 性质（R²>0.97 for both K）为 Claim 1 提供了最强支撑。 50% hurts\n    rate 是对称参数网格的自然结果，但实际应用中 heterogeneity 方向未知， 因此 50% 是 prior probability of harm——足以证明\n    global correction 不可盲目应用。 K-dependence 的 non-monotonicity (K=2 > K=4 for DIM)\n    是一个需要在论文中 显式讨论的 subtle point，避免审稿人误读为 \"more subgroups → always worse\"。\n\n    '\n- name: Semi-Synthetic CSS Benchmark (TweetEval Sentiment)\n  plan_id: exp-003\n  description: 'TweetEval sentiment (N=45K) 上注入已知 CATE heterogeneity structure， GPT-4.1\n    annotation，K=4 subgroups (text features: has_hashtag × text_length)， 100 MC runs，5\n    methods 对比 (oracle/naive/global/stratified_mle/hb_ec_hte)。\n\n    '\n  expected_results:\n    n_subgroups: 4\n    misclass_rates:\n      S0: 0.05\n      S1: 0.1\n      S2: 0.15\n      S3: 0.25\n    subgroup_sizes:\n      S0: ~38%\n      S1: ~38%\n      S2: ~12%\n      S3: ~12%\n    delta_pi: 0.2\n    debiasing_hurts_confirmed: true\n    mc_runs: 100\n    hb_vs_mle_n100_S3_extreme_rmse_improvement: +60%\n    hb_vs_mle_n100_S3_moderate_rmse_improvement: +24%\n    hb_vs_mle_n250_S3_rmse_improvement: +5-17%\n    hb_vs_mle_n500_convergence: <1.6% difference\n    boundary_condition: n_expert≥100 recommended\n    n50_S3_hb_worse: true\n    n50_S3_hb_degradation: -57% RMSE\n  result_rationale: 'S3 (highest error subgroup, ~12% of data) 是 EC-HTE 的 critical\n    test： n=100 时 HB 大幅优于 MLE (+60%) 因为 S3 仅有 ~12 expert labels (100×0.12)， MLE 的\n    confusion matrix 估计极不稳定，而 HB 从其他 3 个子群借力。 n=50 时 HB 反而 worse (-57%) 因为每子群仅 ~6\n    labels，所有子群的 CM 估计 都不可靠，shrinkage target (pooled estimate) 本身也有大方差——这是 boundary\n    condition (n_expert/K < 25) 的直接体现。Δπ=0.20 落在 best 档 [0.1, 0.2] 上界， 因为 semi-synthetic\n    设定中 text features 提供了真实的 annotation difficulty 变异 (hashtag presence 增加 misclassification\n    ~0.07-0.10)。debiasing hurts 在 S0 (lowest error) 最显著：global correction 对已经几乎正确的子群过度校正。\n\n    '\n  tables:\n  - title: Method Comparison — K=4, Extreme Regime\n    columns:\n    - n_expert\n    - subgroup\n    - oracle_rmse\n    - naive_rmse\n    - global_rmse\n    - mle_rmse\n    - hb_rmse\n    rows:\n    - - 100\n      - S0\n      - 0.025\n      - 0.042\n      - 0.068\n      - 0.055\n      - 0.048\n    - - 100\n      - S1\n      - 0.025\n      - 0.058\n      - 0.052\n      - 0.061\n      - 0.054\n    - - 100\n      - S2\n      - 0.035\n      - 0.085\n      - 0.072\n      - 0.098\n      - 0.075\n    - - 100\n      - S3\n      - 0.04\n      - 0.125\n      - 0.095\n      - 0.28\n      - 0.112\n    - - 250\n      - S3\n      - 0.04\n      - 0.125\n      - 0.095\n      - 0.085\n      - 0.081\n    - - 500\n      - S3\n      - 0.04\n      - 0.125\n      - 0.095\n      - 0.072\n      - 0.071\n  - title: Debiasing Hurts Verification (Global vs Naive |bias|)\n    columns:\n    - subgroup\n    - naive_bias\n    - global_bias\n    - ratio\n    - direction\n    rows:\n    - - S0\n      - 0.008\n      - 0.035\n      - 4.4\n      - global hurts\n    - - S1\n      - 0.025\n      - 0.022\n      - 0.9\n      - global helps slightly\n    - - S2\n      - 0.045\n      - 0.038\n      - 0.8\n      - global helps\n    - - S3\n      - 0.095\n      - 0.065\n      - 0.7\n      - global helps\n  figures_description:\n  - Per-subgroup RMSE across n_expert, 5 methods 分色, S3 单独高亮\n  - 'Debiasing hurts demonstration: S0 的 naive vs global bias bar chart'\n  analysis: 'semi-synthetic 设定的价值在于保留了 real text features 的 annotation difficulty\n    structure (Δπ 来自真实 GPT-4.1 misclassification patterns)，同时 ground-truth CATE 已知。S3\n    是 minority subgroup (12%) with highest error——这是 CSS 场景中的 typical pattern (rare\n    categories harder to classify)。HB 的 sweet spot n=100-250 对应 实际预算中 reasonable expert\n    label investment。boundary condition n<50 的公开 增强 paper credibility。\n\n    '\n- name: Real-Data Case Study (UC Berkeley Hate Speech)\n  plan_id: exp-004\n  description: 'UC Berkeley Measuring Hate Speech 数据集上的 pattern consistency 分析。 GPT-4.1\n    annotation，platform_group × text_length 定义 4 subgroups， 展示 global vs EC-HTE 产生\n    qualitatively different CATE 分布。\n\n    '\n  expected_results:\n    dataset: UC Berkeley Measuring Hate Speech\n    n_comments: 2496\n    subgroups:\n      plat0_long: 624\n      plat0_short: 624\n      plat23_long: 624\n      plat23_short: 624\n    delta_pi: 0.117\n    global_FPR: 0.139\n    global_FNR: 0.533\n    misclass_heterogeneity_confirmed: true\n    ec_hte_vs_global_qualitative_difference: true\n    bootstrap_ci_overlap: wide, inconclusive on point estimates\n    avg_abs_bias_naive: 0.21\n    avg_abs_bias_global: 0.273\n    avg_abs_bias_ec_hte: 0.313\n  result_rationale: 'Δπ=0.117 落在 best 档 [0.1, 0.2] 下界附近，因为 text features (platform\n    × length) 提供的 misclassification heterogeneity 是 moderate 的——不如 demographic subgroups\n    那么极端，但足以证明 heterogeneity 是 structural 而非 artifact。 EC-HTE avg |bias| (0.313) 高于\n    global (0.273) 看似 counterintuitive，但在 best 档下 这是可接受的：(1) 高 FNR (53%) 意味着 confusion\n    matrix 严重 asymmetric， correction 的 variance 很大；(2) 无 ground-truth CATE，这些 \"bias\"\n    数值 是相对于 semi-synthetic injected CATEs 的 proxy；(3) best 档的 narrative 将此 framed\n    as \"pattern consistency illustration\" 而非 \"EC-HTE outperforms\"。 核心 deliverable\n    是 Δπ>0.1 在 real data 上的确认，以及 qualitative difference in CATE distributions——审稿人需要看到方法在\n    real data 上产生 non-trivial 差异。\n\n    '\n  tables:\n  - title: Subgroup Misclassification Rates (GPT-4.1)\n    columns:\n    - subgroup\n    - n\n    - misclass_rate\n    - FPR\n    - FNR\n    rows:\n    - - plat0_long\n      - 624\n      - 0.266\n      - 0.08\n      - 0.55\n    - - plat0_short\n      - 624\n      - 0.337\n      - 0.12\n      - 0.62\n    - - plat23_long\n      - 624\n      - 0.303\n      - 0.1\n      - 0.58\n    - - plat23_short\n      - 624\n      - 0.383\n      - 0.18\n      - 0.65\n  - title: CATE Estimate Comparison (bootstrap means)\n    columns:\n    - subgroup\n    - naive_cate\n    - global_cate\n    - ec_hte_cate\n    - ci_width\n    rows:\n    - - plat0_long\n      - 0.15\n      - 0.22\n      - 0.19\n      - 0.35\n    - - plat0_short\n      - 0.08\n      - 0.14\n      - 0.11\n      - 0.38\n    - - plat23_long\n      - 0.21\n      - 0.28\n      - 0.24\n      - 0.32\n    - - plat23_short\n      - 0.12\n      - 0.18\n      - 0.15\n      - 0.4\n  figures_description:\n  - Global vs EC-HTE CATE distribution comparison (4 subgroups, bootstrap violin plots)\n  analysis: 'real data 的角色在 best 档中被精确定位为 \"consistent illustration\"： (1) Δπ=0.117\n    确认 misclassification heterogeneity 在 real data 上存在且 non-trivial； (2) 三种方法产生 qualitatively\n    different CATE distributions； (3) wide bootstrap CIs 诚实地报告了估计的不确定性。 高 FNR (53%)\n    本身是有价值的 finding——说明 LLM 在 hate speech detection 上 系统性 under-classify dehumanization，为\n    EC-HTE 的 practical relevance 提供动机。 审稿人可能 question 为什么 EC-HTE 不 outperform global——response\n    是 \"这正是 Claim 3 diagnostic criterion 的价值：Δπ×Δτ 在此 dataset 上 moderate， full stratified\n    correction 的 variance cost 不完全 justified\"。\n\n    '\n- name: Diagnostic Criterion Validation (Cross-Validated)\n  plan_id: exp-005\n  description: 'Δπ×Δτ product 作为 diagnostic criterion 的 ROC 分析。 必须使用 leave-one-setting-out\n    CV 而非 in-sample AUC。 从 exp-001/003 的所有 experimental settings 中计算 criterion。\n\n    '\n  expected_results:\n    subgroup_level_auc_insample: 0.833\n    subgroup_correlation: 0.86\n    diagnostic_auc_cv: 0.78\n    setting_level_auc_insample: 0.49\n    low_pi_hurt_pct: 84.6\n    high_pi_hurt_pct: 15.4\n    cv_method: leave-one-setting-out\n    optimal_threshold_cv: 0.035\n    sensitivity_at_threshold: 0.82\n    specificity_at_threshold: 0.71\n  result_rationale: 'CV AUC 0.78 落在 best 档 [0.75, 0.85]。in-sample subgroup AUC=0.833\n    降至 CV 0.78 因为 leave-one-setting-out 移除了同一 setting 内子群间的相关性—— 同一 regime 下的子群共享\n    CATE heterogeneity 参数，in-sample 时这是 \"information leak\"。 0.78 的 CV AUC 仍然 strong\n    enough 因为 diagnostic criterion 的实用性 不要求完美分类：false negatives (低 Δπ×Δτ 但 global\n    仍 hurts) 的代价是 unnecessarily using global correction (效率损失但不引入 bias)， 而 false positives\n    的代价是 unnecessarily stratifying (多花 expert labels)。 两种 error 的 asymmetric cost\n    使得 0.78 AUC 在 practical decision-making 中 足够有效。setting-level AUC=0.49 (near random)\n    是因为 setting 内混合了 hurt/help 子群，setting-level prediction 本质上是 ill-defined—— 这恰好支持了\n    subgroup-level diagnostic 的必要性。\n\n    '\n  tables:\n  - title: Diagnostic Criterion ROC Summary\n    columns:\n    - evaluation\n    - AUC\n    - n_settings\n    - n_subgroups\n    - method\n    rows:\n    - - in-sample subgroup\n      - 0.833\n      - 24\n      - 72\n      - logistic regression on Δπ×Δτ\n    - - CV subgroup\n      - 0.78\n      - 24\n      - 72\n      - leave-one-setting-out\n    - - in-sample setting\n      - 0.49\n      - 24\n      - 24\n      - majority vote\n  - title: Threshold Analysis (CV)\n    columns:\n    - threshold\n    - sensitivity\n    - specificity\n    - F1\n    - n_flagged\n    rows:\n    - - 0.02\n      - 0.92\n      - 0.55\n      - 0.68\n      - 42\n    - - 0.035\n      - 0.82\n      - 0.71\n      - 0.76\n      - 35\n    - - 0.05\n      - 0.7\n      - 0.82\n      - 0.76\n      - 28\n    - - 0.075\n      - 0.55\n      - 0.9\n      - 0.68\n      - 20\n  figures_description:\n  - 'ROC curve: in-sample vs CV, with optimal threshold annotated'\n  - 'Scatter plot: Δπ×Δτ product vs actual |bias ratio|, colored by CV fold'\n  analysis: 'diagnostic criterion 从 setting-level 重构为 subgroup-level 预测任务后 AUC 从 0.49\n    跃升至 0.78 (CV)，确认了 best 档的核心假设。 in-sample 到 CV 的 drop (~0.05) 是 moderate 的，说明 criterion\n    的 generalization 合理。optimal threshold 0.035 可直接用于 practical guideline： \"if Δπ×Δτ\n    > 0.035 from pilot data, use EC-HTE; otherwise global correction is safe\"。\n\n    '\n- name: Expert Label Budget Sensitivity\n  plan_id: exp-006\n  description: '系统性 sweep n_expert ∈ {50,100,250,500,1000,2000} × K ∈ {2,4,8} × regime\n    ∈ {extreme,moderate}。 找到 EC-HTE > Global 的 RMSE crossover point。验证 HB partial\n    pooling 在小 n 的价值。\n\n    '\n  expected_results:\n    n_mc: 100\n    total_configs: 36\n    crossover_hb_beats_global:\n      K2_extreme: 250\n      K2_moderate: never (global always better)\n      K4_extreme: 1000\n      K4_moderate: 2000\n      K8_extreme: 1500\n      K8_moderate: never\n    hb_vs_mle_pct_configs_hb_better: 87.5\n    hb_best_improvement_K4_moderate_n50: +42.4% RMSE\n    convergence_threshold: 'n≥1000: HB ≈ MLE <0.5%'\n  result_rationale: 'crossover at K=2/extreme n=250 落在 best 档 [200, 300] 因为 2 subgroups\n    with extreme heterogeneity (Δπ≥0.15) 意味着 per-subgroup CM estimation 只需 ~125 labels/subgroup\n    即可击败 global pooling 的 systematic bias。 K=4/extreme 需要 n=1000 (更高) 因为 4 subgroups\n    分摊 expert budget， per-subgroup labels 仅 ~250——需要更多总量才能让 stratified estimation\n    的 variance 低于 global 的 bias。K=2/moderate \"never crosses\" 因为 moderate heterogeneity\n    (Δπ~0.05) 下 global correction 的 bias 小于 stratified 的 additional variance——这是 diagnostic\n    criterion (Claim 3) 正确预测的情形。 K=8 介于 K=4 和 \"too many subgroups\" 之间，crossover at\n    1500 for extreme 说明 K=8 仍然 feasible 但 cost-prohibitive for most studies。 HB 在\n    87.5% configs 优于 MLE 因为 symmetric DGP 下 partial pooling 几乎 never hurts (worst\n    case: 0.1% worse when all subgroups have identical error)。\n\n    '\n  tables:\n  - title: RMSE Crossover Points (n_expert where EC-HTE < Global)\n    columns:\n    - K\n    - regime\n    - crossover_n\n    - per_subgroup_at_crossover\n    - practical_feasibility\n    rows:\n    - - 2\n      - extreme\n      - 250\n      - 125\n      - feasible\n    - - 2\n      - moderate\n      - ∞\n      - N/A\n      - global always better\n    - - 4\n      - extreme\n      - 1000\n      - 250\n      - feasible but expensive\n    - - 4\n      - moderate\n      - 2000\n      - 500\n      - expensive\n    - - 8\n      - extreme\n      - 1500\n      - 188\n      - expensive\n    - - 8\n      - moderate\n      - ∞\n      - N/A\n      - global always better\n  - title: HB vs MLE Improvement Summary\n    columns:\n    - K\n    - n_expert\n    - configs_hb_better\n    - best_improvement\n    - worst_degradation\n    rows:\n    - - 2\n      - 50\n      - 3/4\n      - +8.7%\n      - -0.2%\n    - - 4\n      - 50\n      - 7/8\n      - +42.4%\n      - -1.1%\n    - - 2\n      - 1000\n      - 2/4\n      - +0.3%\n      - -0.1%\n    - - 4\n      - 1000\n      - 4/8\n      - +0.5%\n      - -0.3%\n  figures_description:\n  - 'Budget crossover curves: RMSE(EC-HTE)/RMSE(Global) vs n_expert, 分 K 和 regime\n    六面板'\n  analysis: 'budget sensitivity 的核心 narrative：EC-HTE 值得投资 IFF (1) diagnostic criterion\n    flags high heterogeneity (extreme regime) AND (2) budget ≥ crossover threshold。\n    这直接连接 Claim 2 (method) 和 Claim 3 (diagnostic)。 Expert Budget Recommendation subsection\n    的数据基础完备。\n\n    '\n- name: PPCI + DSL Baseline Comparison\n  plan_id: exp-007\n  description: '(a) PPCI vs EC-HTE on 4 DGPs (covariate-only, outcome-only, both,\n    none)； (b) per-subgroup DSL baseline；(c) EC-HTE+PPCI composition； (d) pure covariate-error\n    control condition。8 methods × 4 DGPs × 100 MC。\n\n    '\n  expected_results:\n    total_rows: 6912\n    methods: 8\n    dgps:\n    - A_covariate_only\n    - B_outcome_only\n    - C_both_errors\n    - D_no_error\n    mc_runs: 100\n    dgp_c_extreme_n250_k2:\n      ec_hte_ppci_bias_z0: 0.005\n      ec_hte_ppci_rmse_z0: 0.225\n      ec_hte_bias_z0: 0.178\n      ec_hte_rmse_z0: 0.226\n      ppci_bias_z0: 0.004\n      ppci_rmse_z0: 0.261\n      naive_bias_z0: 0.251\n    ec_hte_ppci_bias_reduction_vs_ec_hte: 35x\n    dgp_a_ec_hte_dominates_ppci: true\n    dgp_b_ppci_dominates_ec_hte: true\n    dsl_per_subgroup_vs_ec_hte: EC-HTE wins by 15-25% RMSE via shrinkage\n    coverage_ec_hte_ppci: 1.0\n  result_rationale: 'DGP C (both errors) 中 ec_hte_ppci 的 0.005 bias 落在 best 档 [0.002,\n    0.01] 因为 EC-HTE 和 PPCI 在 composition 中是 necessary and sufficient： EC-HTE 的 M⁻¹\n    correction 消除 structured covariate error (从 0.251 → 0.178)， PPCI 的 residual rectifier\n    消除 remaining outcome error (从 0.178 → 0.005)。 residual 0.005 来自有限样本 MC noise，不是\n    systematic bias。 35x improvement 因为 ec_hte alone 在 DGP C 中仅修正了 covariate-side，\n    outcome-side error (FNR/FPR asymmetry) 贡献了 ~0.17 的 residual bias。 DGP A 中 EC-HTE\n    dominates PPCI 因为 PPCI 的 general-purpose rectifier 不利用 confusion matrix structure——对\n    pure covariate error， structured correction (M⁻¹) 比 nonparametric rectifier 更\n    efficient。 DSL per-subgroup 比 EC-HTE 差 15-25% RMSE 因为缺少 cross-subgroup shrinkage，\n    每个子群独立估计 correction factor，variance 更高。\n\n    '\n  tables:\n  - title: DGP C — Method Comparison (K=2, extreme, n=250)\n    columns:\n    - method\n    - bias_z0\n    - rmse_z0\n    - coverage_z0\n    - bias_z1\n    - rmse_z1\n    rows:\n    - - naive\n      - 0.251\n      - 0.269\n      - 0.82\n      - 0.195\n      - 0.225\n    - - global\n      - 0.185\n      - 0.215\n      - 0.85\n      - 0.142\n      - 0.185\n    - - ec_hte\n      - 0.178\n      - 0.226\n      - 0.92\n      - 0.125\n      - 0.195\n    - - ppci\n      - 0.004\n      - 0.261\n      - 1.0\n      - 0.003\n      - 0.248\n    - - ec_hte_ppci\n      - 0.005\n      - 0.225\n      - 1.0\n      - 0.004\n      - 0.212\n    - - dsl_subgroup\n      - 0.008\n      - 0.275\n      - 0.95\n      - 0.006\n      - 0.26\n  - title: Complementarity Matrix (which method dominates in which DGP)\n    columns:\n    - DGP\n    - best_method\n    - bias\n    - rationale\n    rows:\n    - - A_covariate\n      - ec_hte\n      - 0.008\n      - structured M⁻¹ correction optimal\n    - - B_outcome\n      - ppci\n      - 0.003\n      - rectifier captures outcome error\n    - - C_both\n      - ec_hte_ppci\n      - 0.005\n      - composition covers both error types\n    - - D_none\n      - oracle≈naive\n      - 0.002\n      - no correction needed\n  figures_description:\n  - '4-panel DGP comparison: bias bar chart per method, DGP A-D'\n  - 'EC-HTE + PPCI composition diagram: covariate correction → outcome correction\n    pipeline'\n  analysis: 'complementarity structure 完美支撑 Contribution #4：ec_hte 和 ppci 各自 necessary\n    (单独都不足以处理 dual error)，composition sufficient (bias → near-zero)。 这不是 trivial 的\n    stacking——ec_hte 的 M⁻¹ correction 改变了 PPCI 的 input distribution， 使 rectifier 只需处理\n    residual outcome error 而非混合的 covariate+outcome error。 DSL per-subgroup 作为 baseline\n    展示了 shrinkage 的价值。\n\n    '\n- name: Multiple LLM Annotator Comparison\n  plan_id: exp-008\n  description: 'GPT-3.5-turbo, GPT-4.1, GPT-4o, GPT-4o-mini, GPT-4-turbo, GPT-5.4\n    六个模型 在 TweetEval sentiment 上的 misclassification heterogeneity patterns。 验证 heterogeneity\n    是 structural (跨模型一致) 而非 model-specific artifact。\n\n    '\n  expected_results:\n    models_completed: 6\n    effective_delta_pi:\n      gpt-3.5-turbo: 0.198\n      gpt-4-turbo: 0.149\n      gpt-4.1: 0.098\n      gpt-4o: 0.08\n      gpt-4o-mini: 0.136\n      gpt-5.4: 0.114\n    all_delta_pi_above_005: true\n    multi_llm_delta_pi_min: 0.08\n    worst_subgroup_consensus: True_medium (5/6 models)\n    cross_model_spearman_significant_pairs: 4\n  result_rationale: '所有 6 个模型 Δπ > 0.05 (best 档 min [0.05, 0.08] 的 0.080 落在范围内) 因为\n    misclassification heterogeneity 的 root cause 是 text features (hashtag, length)\n    对 annotation difficulty 的 structural effect——不同模型有不同 overall accuracy， 但 difficulty\n    ranking 相似 (True_medium 最难: 含 hashtag 的中等长度 text 语义歧义最大)。GPT-3.5-turbo Δπ 最高 (0.198)\n    因为 overall accuracy 最低时 per-subgroup variance 也最大；GPT-4o Δπ 最低 (0.080) 因为是最强模型，\n    error rates 被压缩但 heterogeneity 的 relative pattern 仍存。 significant Spearman pairs\n    (4/15) 受限于仅 4 个 subgroups 的 statistical power—— 但 qualitative agreement (5/6 agree\n    on worst subgroup) 提供了 stronger evidence。\n\n    '\n  tables:\n  - title: Cross-Model Misclassification Heterogeneity\n    columns:\n    - model\n    - overall_accuracy\n    - delta_pi\n    - worst_subgroup\n    - best_subgroup\n    rows:\n    - - gpt-3.5-turbo\n      - 0.72\n      - 0.198\n      - True_medium\n      - False_medium\n    - - gpt-4-turbo\n      - 0.81\n      - 0.149\n      - True_medium\n      - False_medium\n    - - gpt-4.1\n      - 0.86\n      - 0.098\n      - True_medium\n      - False_short\n    - - gpt-4o\n      - 0.88\n      - 0.08\n      - True_medium\n      - False_medium\n    - - gpt-4o-mini\n      - 0.83\n      - 0.136\n      - True_medium\n      - False_medium\n    - - gpt-5.4\n      - 0.9\n      - 0.114\n      - True_short\n      - False_medium\n  - title: Per-Subgroup Misclass Rates by Model\n    columns:\n    - model\n    - False_medium\n    - False_short\n    - True_medium\n    - True_short\n    rows:\n    - - gpt-3.5-turbo\n      - 0.12\n      - 0.15\n      - 0.32\n      - 0.25\n    - - gpt-4.1\n      - 0.1\n      - 0.14\n      - 0.2\n      - 0.17\n    - - gpt-4o\n      - 0.08\n      - 0.11\n      - 0.16\n      - 0.14\n    - - gpt-5.4\n      - 0.07\n      - 0.1\n      - 0.18\n      - 0.15\n  figures_description:\n  - Per-subgroup misclass rate profile across 6 models (parallel coordinates plot)\n  analysis: 'multi-LLM evidence 将 paper 的 contribution 从 \"GPT-4.1-specific finding\"\n    提升为 \"structural phenomenon across LLM generations\"。worst_subgroup consensus (True_medium,\n    5/6) 说明 text features 对 annotation difficulty 的 effect 是 robust to model architecture/scale。这直接支持了\n    \"heterogeneity is inherent to the task, not the model\" 的 narrative，strengthening\n    Claim 1 的 practical relevance。 Move to appendix per writing requirements (exp-008/009\n    → appendix)。\n\n    '\n- name: Adaptive Expert Annotation Allocation\n  plan_id: exp-009\n  description: 'CATE-weighted allocation (targeting high-CATE × high-error subgroups)\n    vs uniform allocation vs uncertainty-only allocation。100 MC runs， K=4, extreme\n    regime, n_expert ∈ {100, 250, 500}。\n\n    '\n  expected_results:\n    n_mc: 100\n    K: 4\n    regime: extreme\n    n_expert_grid:\n    - 100\n    - 250\n    - 500\n    allocation_strategies:\n    - uniform\n    - uncertainty_only\n    - cate_weighted\n    rmse_improvement_cate_weighted_vs_uniform:\n      n100: 8-15%\n      n250: 5-10%\n      n500: 2-5%\n    bias_improvement_cate_weighted_vs_uniform:\n      n100: 12-20%\n      n250: 8-12%\n      n500: 3-6%\n    uncertainty_only_vs_uniform: 3-8% RMSE improvement\n    optimal_allocation_fraction_high_error_subgroup: ~2x proportional\n    diminishing_returns_at_n500: true\n  result_rationale: 'CATE-weighted allocation 在 n=100 时改进最大 (8-15% RMSE) 因为 budget\n    最紧张时 将 disproportionate labels 分配给 high-CATE × high-error 子群的 marginal value 最高：\n    这些子群同时具有 (1) 最不稳定的 CM 估计 (high error → high variance) 和 (2) 最高的 CATE bias impact\n    (high CATE → bias 对 final estimate 影响最大)。 n=500 时 diminishing returns (2-5%) 因为所有子群的\n    CM 估计都已 reasonably stable， allocation 优化的 marginal gain 被 Monte Carlo noise 淹没。\n    uncertainty_only (仅 target high error, 不考虑 CATE magnitude) 比 uniform 好但 不如 cate_weighted\n    因为忽略了 CATE heterogeneity——high-error 但 near-zero CATE 的 子群对 overall CATE 估计的影响有限。optimal\n    allocation ~2x proportional 到 high-error subgroup 是 bias-variance tradeoff 的结果：过度分配\n    (>3x) 牺牲了 其他子群的 estimation quality。\n\n    '\n  tables:\n  - title: Allocation Strategy Comparison (K=4, extreme)\n    columns:\n    - n_expert\n    - strategy\n    - mean_rmse\n    - mean_bias\n    - coverage\n    - alloc_sgC\n    rows:\n    - - 100\n      - uniform\n      - 0.185\n      - 0.095\n      - 0.88\n      - 25\n    - - 100\n      - uncertainty\n      - 0.172\n      - 0.085\n      - 0.9\n      - 35\n    - - 100\n      - cate_weighted\n      - 0.16\n      - 0.078\n      - 0.91\n      - 42\n    - - 250\n      - uniform\n      - 0.12\n      - 0.058\n      - 0.92\n      - 62\n    - - 250\n      - uncertainty\n      - 0.112\n      - 0.052\n      - 0.93\n      - 88\n    - - 250\n      - cate_weighted\n      - 0.108\n      - 0.048\n      - 0.94\n      - 105\n    - - 500\n      - uniform\n      - 0.082\n      - 0.032\n      - 0.94\n      - 125\n    - - 500\n      - uncertainty\n      - 0.079\n      - 0.03\n      - 0.95\n      - 175\n    - - 500\n      - cate_weighted\n      - 0.078\n      - 0.029\n      - 0.95\n      - 210\n  - title: Improvement Summary\n    columns:\n    - n_expert\n    - cate_weighted_vs_uniform_rmse\n    - cate_weighted_vs_uncertainty_rmse\n    rows:\n    - - 100\n      - +13.5%\n      - +7.0%\n    - - 250\n      - +10.0%\n      - +3.6%\n    - - 500\n      - +4.9%\n      - +1.3%\n  figures_description:\n  - Three allocation strategies' RMSE curves across n_expert, with per-subgroup breakdown\n  analysis: 'adaptive allocation 是 P2 实验，在 best 档下放入 appendix。其价值在于回应 审稿人可能的 \"how\n    to optimally spend expert budget\" 问题。CATE-weighted allocation 的 8-15% improvement\n    at n=100 说明 budget-constrained 场景下 allocation matters，但 n≥500 时差异消失——consistent\n    with exp-006 的 convergence。 这为 future work 提供了一个 concrete extension point 而不是\n    current paper 的 core contribution。\n\n    '\n- name: Robustness to Misspecified Subgroup Structure\n  plan_id: exp-010\n  description: '测试 EC-HTE 在 subgroup 定义含噪声或 misaligned 时的 graceful degradation。 noise_level\n    ∈ {0, 0.1, 0.25, 0.5}，K=2 和 K=4。\n\n    '\n  expected_results:\n    n_mc: 100\n    noise_levels:\n    - 0\n    - 0.1\n    - 0.25\n    - 0.5\n    coverage_hb_range:\n    - 0.945\n    - 0.96\n    coverage_naive_range:\n    - 0.875\n    - 0.92\n    coverage_global_range:\n    - 0.925\n    - 0.953\n    hb_beats_mle_all_configs: true\n    graceful_convergence_at_50pct: true\n    hb_improvement_over_mle_range: +0.1% to +0.9% RMSE\n  result_rationale: 'HB coverage 在所有 noise levels 保持 0.945-0.960 (落在 best 档 [0.92,\n    0.97]) 因为 partial pooling 的核心机制：当 subgroup labels 含噪声时，per-subgroup CM 估计变差，但\n    HB 的 shrinkage 自动增加 pooling weight，将估计拉向 global mean—— 效果等同于自适应地从 \"full stratification\"\n    回退到 \"global correction\"。 noise=0.5 时 HB ≈ Global 因为 50% random label swap 使 subgroup\n    membership 几乎 uninformative，HB 正确地近乎完全 pool。这是 James-Stein shrinkage 的 经典行为。naive\n    coverage 低 (87-92%) 因为不做 correction 的 CI 不 account for misclassification error。graceful\n    degradation 而非 catastrophic failure 直接回应了 Anticipated Reviewer Concern #4。\n\n    '\n  tables:\n  - title: Coverage Across Noise Levels\n    columns:\n    - K\n    - noise\n    - coverage_naive\n    - coverage_global\n    - coverage_hb\n    - hb_vs_mle_rmse\n    rows:\n    - - 2\n      - 0.0\n      - 0.875\n      - 0.925\n      - 0.958\n      - +0.8%\n    - - 2\n      - 0.1\n      - 0.877\n      - 0.935\n      - 0.948\n      - +0.6%\n    - - 2\n      - 0.25\n      - 0.89\n      - 0.932\n      - 0.95\n      - +0.4%\n    - - 2\n      - 0.5\n      - 0.897\n      - 0.945\n      - 0.945\n      - +0.1%\n    - - 4\n      - 0.0\n      - 0.904\n      - 0.93\n      - 0.956\n      - +0.9%\n    - - 4\n      - 0.1\n      - 0.916\n      - 0.953\n      - 0.958\n      - +0.7%\n    - - 4\n      - 0.25\n      - 0.909\n      - 0.948\n      - 0.96\n      - +0.5%\n    - - 4\n      - 0.5\n      - 0.919\n      - 0.944\n      - 0.946\n      - +0.1%\n  figures_description:\n  - Coverage vs noise level, 3 methods 分色, K=2/K=4 双面板\n  analysis: 'coverage 作为 decisive metric (而非 bias 或 RMSE) 的定位在 best 档下特别有效： naive\n    87-92% = systematically under-covers，EC-HTE 95-96% = near-nominal， global 93-95%\n    = intermediate。HB 的 graceful degradation 是方法论上的 strong point， 直接回应 \"misspecified\n    subgroups\" 的审稿人顾虑。\n\n    '\n- name: Causal Forest Integration\n  plan_id: exp-011\n  description: 'EC-HTE post-hoc correction on CausalForestDML subgroup CATE estimates。\n    naive_forest vs global_forest vs ec_hte_forest，100 MC，8 configs。 验证 nonlinear\n    estimator 下 debiasing-hurts amplification (up to 5.9x for K=4)。\n\n    '\n  expected_results:\n    n_mc: 100\n    n_configs: 8\n    mean_abs_bias:\n      naive_forest: 0.156\n      global_forest: 0.107\n      ec_hte_forest: 0.061\n    mean_rmse:\n      naive_forest: 0.178\n      global_forest: 0.166\n      ec_hte_forest: 0.229\n    debiasing_hurts_max_ratio: 5.9\n    debiasing_hurts_detail: 'K=4/extreme/sg0: global 5.9x worse than naive'\n    k2_n500_ec_hte_bias_range:\n    - 0.004\n    - 0.013\n    bias_amplification_max_cf: 5.9\n    ec_hte_bias_reduction_factor_vs_global: 2.6\n  result_rationale: 'CausalForest 的 5.9x amplification (best 档 [5.0, 6.5]) 显著高于 DIM\n    的 2.41-2.86x 因为 tree-based estimator 在 subgroup 内部进一步分裂， 每个 leaf 的 CATE 估计噪声在\n    global correction 时被 heterogeneously amplified。 具体机制：CausalForest 的 honest splitting\n    将 sample 减半， per-leaf sample size 更小 → CM correction 的 M⁻¹ operation 放大了 leaf-level\n    estimation noise → subgroup aggregation 时 noise 不 cancel 而 compound。 K=4/extreme\n    最严重因为 4 个子群中 sg0 (lowest error) 被 global CM 过度校正， 且 forest 的 nonlinear estimation\n    使得 over-correction 的 propagation 是 multiplicative 而非 additive。ec_hte_forest 的\n    mean |bias| 0.061 (vs global 0.107) 代表 ~2.6x bias reduction (落在 best 档 [2.0, 4.5])。RMSE\n    0.229 > global 0.166 体现了 bias-RMSE tradeoff (per-subgroup CM estimation variance\n    在 forest 上更大)， 这是 Writing Requirement #11 要求 disclose 的。\n\n    '\n  tables:\n  - title: CausalForest Method Comparison (mean across 8 configs)\n    columns:\n    - method\n    - mean_abs_bias\n    - mean_rmse\n    - debiasing_hurts_cases\n    rows:\n    - - naive_forest\n      - 0.156\n      - 0.178\n      - —\n    - - global_forest\n      - 0.107\n      - 0.166\n      - 9\n    - - ec_hte_forest\n      - 0.061\n      - 0.229\n      - 0\n  - title: Debiasing Hurts — CausalForest vs DIM\n    columns:\n    - estimator\n    - K\n    - max_ratio\n    - worst_config\n    - mechanism\n    rows:\n    - - DIM\n      - 2\n      - 2.86\n      - extreme/sg0\n      - additive over-correction\n    - - DIM\n      - 4\n      - 2.41\n      - extreme/sg0\n      - distributed over-correction\n    - - CausalForest\n      - 2\n      - 3.2\n      - extreme/sg0\n      - multiplicative via leaves\n    - - CausalForest\n      - 4\n      - 5.9\n      - extreme/sg0\n      - compounding leaf noise\n  - title: K=2, n_expert=500 — Near-Zero Bias Detail\n    columns:\n    - config\n    - ec_hte_bias\n    - global_bias\n    - naive_bias\n    - reduction_factor\n    rows:\n    - - extreme/sg0\n      - 0.004\n      - 0.109\n      - 0.052\n      - 27.3\n    - - extreme/sg1\n      - 0.013\n      - 0.033\n      - 0.085\n      - 2.5\n    - - moderate/sg0\n      - 0.008\n      - 0.045\n      - 0.028\n      - 5.6\n    - - moderate/sg1\n      - 0.011\n      - 0.022\n      - 0.065\n      - 2.0\n  figures_description:\n  - DIM vs CausalForest debiasing-hurts amplification comparison (grouped bar chart)\n  - ec_hte_forest bias across n_expert, showing convergence to near-zero\n  analysis: 'CausalForest integration 是 Claim 2 的 critical evidence：paper claims \"CausalForestDML\"\n    但仅有 DIM results 会被审稿人视为 claim-evidence gap。5.9x amplification strengthens Claim\n    1 (\"debiasing can hurt even more with nonlinear estimators\")。 bias-RMSE tradeoff\n    (ec_hte RMSE 38% higher than global) 必须在 paper 中 诚实讨论——defense: (1) bias 是 primary\n    metric for policy decisions， (2) RMSE 在 n≥500 时 competitive，(3) coverage 仍然 near-nominal。'\n",
      "numLines": 1290,
      "startLine": 1,
      "totalLines": 1290
    }
  },
  "sourceToolAssistantUUID": "652e3cf1-5a8c-4891-8f76-313c715ce75b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation",
  "sessionId": "33779107-04cc-4691-9d8a-87f3f46280c6",
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
  "lastPrompt": "[DREAM Review Director] dream_id=20260521T122454 | review_mode=simple | review_visible=True PDF: /home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/dream_reports/dr…",
  "leafUuid": "fd96649e-8bf9-4ec4-b93b-a737d7bde0f7",
  "sessionId": "33779107-04cc-4691-9d8a-87f3f46280c6"
}
```

---

### Runtime record

_source line 17_

```json
{
  "type": "ai-title",
  "aiTitle": "Review EMNLP paper on HTE and LLM annotation",
  "sessionId": "33779107-04cc-4691-9d8a-87f3f46280c6"
}
```

---

### Assistant

_source line 18 · 2026-05-21T13:03:28.931Z_

<details><summary>Logged reasoning block</summary>

```text
Let me now carefully review this paper and prepare the review report. I've read both the PDF and the experiment design context. Let me now dispatch a thorough review.

Let me analyze the paper systematically:

**Title**: "When Debiasing Backfires: Heterogeneous Misclassification Bias in LLM-Annotated Treatment Effect Estimation"

**Summary**: The paper identifies that applying global (pooled) confusion-matrix correction to subgroup-level CATE estimates introduces systematic bias proportional to Δπ × Δτ (product of misclassification heterogeneity and CATE heterogeneity). 

The authors propose EC-HTE, a hierarchical Bayesian approach that performs correction at the subgroup level rather than globally, and they introduce a diagnostic criterion based on cross-validation AUC to assess when this matters. They validate their approach across synthetic, semi-synthetic, and real datasets including TweetEval and UC Berkeley hate speech data, and show it integrates well with CausalForest.

Now assessing against EMNLP 2026 standards.

**Strengths:**
1. Well-defined problem with clear practical relevance - LLMs are widely used for annotation in CSS, and the bias mechanism identified is non-obvious
2. Strong theoretical contribution - exact bias decomposition identity (Theorem 1), not just a bound
3. Comprehensive experimental validation spanning 3,600 Monte Carlo runs across multiple data regimes and integration with causal forest methods
4. Honest reporting of boundary conditions and tradeoffs, with real data framed appropriately as pattern consistency rather than ground truth
5. Practical diagnostic criterion with cross-validation evaluation
6. Multi-LLM analysis demonstrating the structural nature of heterogeneity
7. PPCI composition shows genuine complementarity between approaches

**Weaknesses:**
1. Theorem 1's presentation lacks precision - the bias decomposition is stated as a function of annotation rate and effect heterogeneity differences, but the exact form only holds for K=2 cases while the general case remains somewhat informal

.

2. The diagnostic criterion achieves CV AUC of 0.78, which is moderate at best, and the leave-one-setting-out evaluation uses only 24 settings with 72 subgroup observations - a small sample that raises questions about generalization beyond these specific configurations.

3. The real data case study shows EC-HTE doesn't actually outperform global correction, and while the paper acknowledges this honestly, it undermines the practical value proposition; the CATE estimates have wide confidence intervals that make it difficult to draw firm conclusions.

4. The non-differential misclassification assumption for LLMs is quite stringent and may not hold in practice.

5. LLM errors likely correlate with outcomes and treatments, which the limitations mention but don't thoroughly investigate for robustness.

6. Expert labels are treated as noise-free, which is unrealistic for many content screening tasks.

7. Scalability becomes problematic with many subgroups - K=8 requires n=1500 for crossover effects, and moderate heterogeneity never crosses over, suggesting the practical utility is limited to K=2-4 with extreme heterogeneity and n≥250.

8. The evaluation focuses on TweetEval sentiment and UC Berkeley hate speech, both standard tasks, without demonstrating generalization to other domains like political stance or moral foundations.

9. The baseline comparisons are narrow, testing only DSL per-subgroup as a non-trivial alternative rather than exploring other Bayesian approaches to measurement error correction.

Now I'm checking which experiments are covered in the paper sections and tables.

All 11 experiments are accounted for across the main sections and appendices. For the soundness assessment, the theoretical framework is generally solid though Theorem 1 could be more precise in its general form, and the experimental methodology is rigorous with proper Monte Carlo replication and cross-validation.

The excitement factor sits at a moderate level—while the counterintuitive finding that debiasing can actually harm performance is genuinely surprising and has practical value, the proposed solution relies on established Bayesian methods like Dirichlet priors and partial pooling applied to this new context, which feels somewhat incremental. The diagnostic criterion adds utility but the moderate AUC values limit its broader impact.

On reproducibility, the experiments are well-documented with clear specifications for sample sizes, number of regimes, and Monte Carlo runs, and the synthetic data generation is fully transparent. The semi-synthetic experiments use publicly available TweetEval data and the real data comes from the UC Berkeley corpus, with MCMC diagnostics properly reported. The main gaps are that code availability isn't mentioned and reproducing the GPT-4.1 annotations would require direct API access.

Reconsidering the overall contribution—the paper identifies a previously overlooked bias mechanism, derives an exact identity, proposes a practical correction framework with a diagnostic criterion, and demonstrates composition with existing methods. Combined with the experimental rigor (11 experiments, 3,600 Monte Carlo runs, multiple estimators and LLMs tested), this feels like a more complete package than initially assessed. The writing is clear and the authors are transparent about limitations, which strengthens the work for a venue like EMNLP.

That said, the Bayesian techniques themselves aren't novel—the real value lies in problem identification and formalization rather than methodological innovation. A score of 3.5 seems right: it's a solid contribution with meaningful insights, but the limited technical novelty may keep it from reaching the excitement threshold for the main conference.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fd96649e-8bf9-4ec4-b93b-a737d7bde0f7",
  "isSidechain": false,
  "requestId": "req_011CbFkyYNFq6cuXdyygenHQ",
  "type": "assistant",
  "uuid": "2afb6fd0-87e0-435b-a1fa-8cbd28a9d7ad",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation",
  "sessionId": "33779107-04cc-4691-9d8a-87f3f46280c6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017DxSEWa4dhv21bzC71VMty",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 30023,
      "cache_read_input_tokens": 23661,
      "output_tokens": 1911,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 30023,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1911,
          "cache_read_input_tokens": 23661,
          "cache_creation_input_tokens": 30023,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 30023
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

_source line 19 · 2026-05-21T13:03:28.934Z_

Now I'll load the skill and submit tool schemas.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2afb6fd0-87e0-435b-a1fa-8cbd28a9d7ad",
  "isSidechain": false,
  "requestId": "req_011CbFkyYNFq6cuXdyygenHQ",
  "type": "assistant",
  "uuid": "2979bccd-ada9-413a-9cc3-f428082c418a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation",
  "sessionId": "33779107-04cc-4691-9d8a-87f3f46280c6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017DxSEWa4dhv21bzC71VMty",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 30023,
      "cache_read_input_tokens": 23661,
      "output_tokens": 1911,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 30023,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1911,
          "cache_read_input_tokens": 23661,
          "cache_creation_input_tokens": 30023,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 30023
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

_source line 20 · 2026-05-21T13:03:28.943Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01RBGBkd68ci8GTqbX7uA4ab`</summary>

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
  "parentUuid": "2979bccd-ada9-413a-9cc3-f428082c418a",
  "isSidechain": false,
  "requestId": "req_011CbFkyYNFq6cuXdyygenHQ",
  "type": "assistant",
  "uuid": "0e7b569b-c426-43af-9e10-3a7414323d79",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation",
  "sessionId": "33779107-04cc-4691-9d8a-87f3f46280c6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017DxSEWa4dhv21bzC71VMty",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 30023,
      "cache_read_input_tokens": 23661,
      "output_tokens": 1911,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 30023,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1911,
          "cache_read_input_tokens": 23661,
          "cache_creation_input_tokens": 30023,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 30023
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

_source line 21 · 2026-05-21T13:03:28.952Z_

<details><summary>↩ Tool result · `toolu_01RBGBkd68ci8GTqbX7uA4ab`</summary>

```text
No matching deferred tools found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0e7b569b-c426-43af-9e10-3a7414323d79",
  "isSidechain": false,
  "promptId": "b20fe594-a1fa-45c4-9afa-b12a0912be14",
  "type": "user",
  "uuid": "b3e84f80-55b3-4a62-ab02-a145b7e0589c",
  "toolUseResult": {
    "matches": [],
    "query": "select:submit_dream_review_report",
    "total_deferred_tools": 23
  },
  "sourceToolAssistantUUID": "0e7b569b-c426-43af-9e10-3a7414323d79",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation",
  "sessionId": "33779107-04cc-4691-9d8a-87f3f46280c6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-21T13:03:33.261Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01Q33Y4FbsfGBVyk6MM99c6d`</summary>

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
  "parentUuid": "b3e84f80-55b3-4a62-ab02-a145b7e0589c",
  "isSidechain": false,
  "requestId": "req_011CbFm3ax9AMYF9PYZHUayG",
  "type": "assistant",
  "uuid": "6c1f29c8-e00e-4caf-b44c-4e8a78cf021d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation",
  "sessionId": "33779107-04cc-4691-9d8a-87f3f46280c6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018p9uWv1L6He3fEsccxzSFi",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1926,
      "cache_read_input_tokens": 53684,
      "output_tokens": 89,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1926,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 89,
          "cache_read_input_tokens": 53684,
          "cache_creation_input_tokens": 1926,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1926
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

_source line 23 · 2026-05-21T13:03:33.264Z_

<details><summary>↩ Tool result · `toolu_01Q33Y4FbsfGBVyk6MM99c6d`</summary>

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
  "parentUuid": "6c1f29c8-e00e-4caf-b44c-4e8a78cf021d",
  "isSidechain": false,
  "promptId": "b20fe594-a1fa-45c4-9afa-b12a0912be14",
  "type": "user",
  "uuid": "c4c9bf6b-1d36-4398-bc41-183ba6db0711",
  "toolUseResult": {
    "matches": [
      "mcp__agent-ml-research__submit_dream_review_report"
    ],
    "query": "select:mcp__agent-ml-research__submit_dream_review_report",
    "total_deferred_tools": 23
  },
  "sourceToolAssistantUUID": "6c1f29c8-e00e-4caf-b44c-4e8a78cf021d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation",
  "sessionId": "33779107-04cc-4691-9d8a-87f3f46280c6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 24 · 2026-05-21T13:03:37.156Z_

Now I have the full paper and experiment context. Let me compile the review report.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c4c9bf6b-1d36-4398-bc41-183ba6db0711",
  "isSidechain": false,
  "requestId": "req_011CbFm3uKgnfJR77kfcMsgc",
  "type": "assistant",
  "uuid": "85057b2a-ffe2-40df-ab36-efaf4dcfa4db",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation",
  "sessionId": "33779107-04cc-4691-9d8a-87f3f46280c6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JB78rdUbg2vCqQ7Z6kAvmh",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 713,
      "cache_read_input_tokens": 55610,
      "output_tokens": 3289,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 713,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 3289,
          "cache_read_input_tokens": 55610,
          "cache_creation_input_tokens": 713,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 713
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

_source line 25 · 2026-05-21T13:04:39.865Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_dream_review_report · `toolu_01NsgtGHGses8r5iG6kApEeW`</summary>

```json
{
  "report": "\n# Review Report: \"When Debiasing Backfires: Heterogeneous Misclassification Bias in LLM-Annotated Treatment Effect Estimation\"\n\n**Venue:** EMNLP 2026 (ARR)\n\n---\n\n## Summary\n\nThe paper identifies a previously unrecognized bias mechanism in LLM-annotated heterogeneous treatment effect (HTE) estimation: applying a global (pooled) confusion-matrix correction to subgroup-level CATE estimates introduces systematic bias proportional to Δπ × Δτ—the product of misclassification heterogeneity and CATE heterogeneity. This \"debiasing can hurt\" phenomenon affects ~50% of the parameter space, with amplification up to 5.9× for nonlinear estimators. The authors propose EC-HTE, a hierarchical Bayesian framework performing subgroup-stratified correction with partial pooling, a diagnostic criterion (CV AUC = 0.78) for when stratified correction is worthwhile, and show that EC-HTE composes with PPCI to handle dual covariate+outcome error (bias = 0.005). Experiments span synthetic data (3,600 MC runs), semi-synthetic CSS benchmarks (TweetEval with GPT-4.1), a real-data case study (UC Berkeley hate speech), CausalForest integration, and six-LLM robustness analysis.\n\n---\n\n## Scores\n\n| Dimension | Score |\n|-----------|-------|\n| **Soundness** | 3.5 / 5 |\n| **Excitement** | 3.5 / 5 |\n| **Reproducibility** | 4 / 5 |\n| **Overall Assessment** | 3.5 (Borderline Conference) |\n\n**Confidence:** 4 / 5\n\n---\n\n## Strengths\n\n**S1. Well-identified, practically important problem.** The observation that global misclassification correction can *amplify* subgroup CATE bias is non-obvious and directly relevant to a growing body of CSS work using LLM annotations as effect modifiers. The \"debiasing can hurt\" framing is compelling and the 50% parameter-space figure, combined with the 5.9× amplification for CausalForest, makes a strong case that this is not a corner case.\n\n**S2. Exact bias decomposition identity (Theorem 1).** The theoretical contribution goes beyond a bound—it is an exact identity verified empirically with R² = 0.994 (K=2) and 0.974 (K=4) across 260 configurations. This is clean, interpretable, and directly actionable. The tightness ratios near 1.0 confirm this is not loose.\n\n**S3. Thorough and honest experimental validation.** The paper covers 11 distinct experiments across synthetic, semi-synthetic, and real data with multiple estimators (DIM, CausalForest). The 3,600 MC runs for synthetic experiments provide strong statistical grounding. Importantly, the paper is honest about boundary conditions (n_expert/K < 25 degrades HB), the bias-RMSE tradeoff for CausalForest (RMSE 0.229 vs. 0.166), and the real-data case study being \"pattern consistency, not ground-truth benchmarking.\" This intellectual honesty strengthens credibility.\n\n**S4. Complete contribution package.** The paper delivers: (1) problem identification + theory, (2) a practical solution (EC-HTE), (3) a diagnostic decision tool, (4) composition with PPCI for dual error, and (5) multi-LLM evidence of structural heterogeneity. Each piece supports the others coherently.\n\n**S5. Multi-LLM analysis demonstrates structural heterogeneity.** Testing across 6 LLMs (GPT-3.5-turbo through GPT-5.4) with consistent difficulty ranking (5/6 agree on worst subgroup) elevates the finding from model-specific artifact to structural phenomenon. This is placed appropriately in the appendix.\n\n**S6. Well-written and well-structured.** The paper reads clearly, the notation is consistent, tables are informative, and the narrative arc from problem → theory → method → experiments → practical guidance is logical.\n\n---\n\n## Weaknesses\n\n**W1. Theorem 1's general-K formulation is imprecise.** Equation (1) states the additional bias equals \"f(Δπ_k, Δτ_k), a function that is zero when either Δπ_k = 0 or Δτ_k = 0, and whose magnitude scales with the product |Δπ_k| · |Δτ_k|.\" For K=2 this reduces to an exact product form, but for K>2 the explicit functional form is not given—only qualitative properties. For a paper whose lead contribution is an \"exact identity,\" this vagueness for the general case is a notable gap. The R² = 0.974 for K=4 confirms it works empirically, but the theorem as stated is more of a characterization than a closed-form identity for K>2.\n\n**W2. Narrow practical sweet spot.** The budget sensitivity analysis (Table 11) reveals that EC-HTE only outperforms global correction under *extreme* heterogeneity (Δπ ≥ 0.15). Under moderate heterogeneity, global correction is *always* preferable for K=2 and K=8. Even under extreme heterogeneity, K=4 requires n_expert = 1,000 (250 per subgroup). This means the practical applicability is constrained to scenarios with (a) strong misclassification heterogeneity AND (b) sufficient expert budget AND (c) few subgroups. The paper should discuss more explicitly what fraction of real CSS studies fall in this regime.\n\n**W3. Diagnostic criterion has moderate discriminative power.** CV AUC = 0.78 on only 24 experimental settings (72 subgroup-level observations) from the authors' own experiments is a small and potentially optimistic evaluation. The leave-one-setting-out CV removes correlation within settings, but all settings share the same DGP families. Generalization to substantially different data-generating processes, different CSS domains, or different subgroup structures is untested. The practical utility of the 0.035 threshold recommendation hinges on this generalization.\n\n**W4. Non-differential misclassification assumption (A1) is strong for LLMs.** LLM annotation errors are likely to correlate with treatment or outcome—e.g., a hate speech classifier may be more accurate for clearly hateful content (which may correlate with treatment intensity). The paper acknowledges this in limitations but provides no robustness analysis to A1 violations. This is a substantive concern because the entire theoretical framework rests on this assumption. Even a simulation showing graceful degradation under moderate A1 violations would strengthen the paper.\n\n**W5. Real-data case study is inconclusive.** In Section 4.4, EC-HTE does not outperform global correction—the CATE estimates differ qualitatively but bootstrap CIs are wide (0.32–0.40) and overlapping. Without ground-truth CATEs, the real-data experiment cannot validate the method's accuracy. The paper frames this appropriately as \"pattern consistency,\" but the reader is left without a real-data success story. The finding that GPT-4.1 has 53% FNR for dehumanizing content is interesting but tangential.\n\n**W6. Limited methodological novelty in the solution.** EC-HTE applies well-known techniques—Dirichlet priors with partial pooling, NUTS MCMC—to a new problem. The innovation is in *identifying the problem* and *formalizing it*, not in the Bayesian machinery. While applying known methods to new problems is valid, reviewers seeking methodological novelty may find the framework incremental.\n\n**W7. Missing baselines and comparisons.** The paper compares against naive, global, MLE-stratified, DSL per-subgroup, and PPCI. Missing comparisons include: (a) other Bayesian measurement error models (e.g., latent class models beyond Dawid-Skene), (b) bootstrap-based stratified correction, (c) empirical Bayes approaches that avoid full MCMC. The DSL per-subgroup baseline is included but only in one table (Table 7).\n\n---\n\n## Questions for Authors\n\n1. Can you provide the explicit closed-form expression for f(Δπ_k, Δτ_k) in Theorem 1 for general K? If the form involves cross-terms across subgroups, this should be stated.\n\n2. What fraction of published CSS studies using LLM annotations would you estimate fall in the \"extreme heterogeneity\" regime where EC-HTE provides benefit? Can you cite any survey or meta-analysis?\n\n3. Have you tested robustness to violations of Assumption A1 (non-differential misclassification)? Even a limited simulation where misclassification rates depend on Y or W would be informative.\n\n4. The boundary condition n_expert/K < 25 where HB degrades (−57% RMSE for S3 at n=50)—is there a principled way to detect this regime and fall back to global correction automatically?\n\n5. PPCI composition (Section 3.4): is the ordering (EC-HTE first, then PPCI) important? Would PPCI → EC-HTE yield different results?\n\n---\n\n## Experiment Coverage Assessment\n\nAll 11 planned experiments are represented in the paper:\n- **exp-001** (HB synthetic): §4.1, Tables 1, 3, 4 ✓\n- **exp-002** (Bias decomposition): §2.2, Tables 1, 2 ✓\n- **exp-003** (Semi-synthetic TweetEval): §4.2, Tables 9, 10 ✓\n- **exp-004** (Real-data UC Berkeley): §4.4, Tables 12, 13 ✓\n- **exp-005** (Diagnostic criterion): §3.3, Tables 6, 18 ✓\n- **exp-006** (Budget sensitivity): §4.3, Table 11 ✓\n- **exp-007** (PPCI + DSL): §3.4, Tables 7, 8 ✓\n- **exp-008** (Multi-LLM): Appendix A, Tables 14, 15 ✓\n- **exp-009** (Adaptive allocation): Appendix B, Table 16 ✓\n- **exp-010** (Robustness to misspecified subgroups): Appendix C, Table 17 ✓\n- **exp-011** (CausalForest): §3.2, Table 5 ✓\n\nCoverage is complete. The paper makes good decisions about what goes in the main text vs. appendix—core claims (bias identity, EC-HTE, diagnostic, PPCI, CausalForest) are in the main body, while supporting analyses (multi-LLM, adaptive allocation, robustness, threshold details) are properly placed in appendices.\n\n---\n\n## Minor Issues\n\n- Table 9 caption references \"extreme regime\" but does not specify n_expert for the first four rows (it appears to vary based on context from surrounding text). Adding n to the table would help readability.\n- The paper mentions \"Ashwin et al., 2025\" as a key motivation but cites it as \"Preprint\"—if this has since been published, update the citation.\n- Section 3.4 references \"Sui et al., 2026\" for PPCI—also a preprint. Two key methodological building blocks being unpublished preprints is a minor concern for reviewer confidence.\n- The Limitations section is appropriately concise (3 points) per EMNLP 2026 guidelines.\n- No Responsible NLP Research Checklist is visible in the PDF—this is mandatory for EMNLP 2026 and would result in desk reject if missing at submission.\n\n---\n\n## Overall Assessment\n\nThis paper identifies a genuine and practically important bias mechanism (global correction amplifies subgroup CATE bias) and formalizes it with a clean theoretical identity. The experimental validation is thorough, honest, and covers the claim space comprehensively. The EC-HTE framework is a sensible solution, though methodologically incremental (known Bayesian techniques applied to a new problem). The diagnostic criterion provides practical guidance but has moderate discriminative power validated on limited settings.\n\nThe paper's main strength is *problem identification and formalization*—showing that a common practice in CSS can systematically backfire is a valuable contribution. The main weaknesses are the narrow practical sweet spot (extreme heterogeneity + sufficient budget + few subgroups), the strong non-differential misclassification assumption without robustness analysis, and the inconclusive real-data case study.\n\nAt the 3.5 level (Borderline Conference): the paper has clear merit and is above the Findings threshold, but reaching the main conference would require strengthening the general-K theory, broadening the diagnostic criterion evaluation, and providing at least partial robustness analysis to A1 violations.\n",
  "project": "ec_hte_llm_annotation",
  "tier": "best",
  "dream_id": "20260521T122454",
  "overall_score": "3.5 — Borderline Conference",
  "review_visible": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "85057b2a-ffe2-40df-ab36-efaf4dcfa4db",
  "isSidechain": false,
  "requestId": "req_011CbFm3uKgnfJR77kfcMsgc",
  "type": "assistant",
  "uuid": "71a69fbb-ee5c-4197-a682-c9a8337c8fd7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation",
  "sessionId": "33779107-04cc-4691-9d8a-87f3f46280c6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JB78rdUbg2vCqQ7Z6kAvmh",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 713,
      "cache_read_input_tokens": 55610,
      "output_tokens": 3289,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 713,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 3289,
          "cache_read_input_tokens": 55610,
          "cache_creation_input_tokens": 713,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 713
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

_source line 26_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[DREAM Review Director] dream_id=20260521T122454 | review_mode=simple | review_visible=True PDF: /home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/dream_reports/dr…",
  "leafUuid": "71a69fbb-ee5c-4197-a682-c9a8337c8fd7",
  "sessionId": "33779107-04cc-4691-9d8a-87f3f46280c6"
}
```

---

### Runtime record

_source line 27_

```json
{
  "type": "ai-title",
  "aiTitle": "Review EMNLP paper on HTE and LLM annotation",
  "sessionId": "33779107-04cc-4691-9d8a-87f3f46280c6"
}
```

---

### Tool result

_source line 28 · 2026-05-21T13:04:43.281Z_

<details><summary>↩ Tool result · `toolu_01NsgtGHGses8r5iG6kApEeW`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"report_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/dream_reports/dream_20260521T122454/best/review_report.md\", \"dream_id\": \"dream_20260521T122454\", \"tier\": \"best\", \"review_visible\": true}, \"error\": \"\"}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "71a69fbb-ee5c-4197-a682-c9a8337c8fd7",
  "isSidechain": false,
  "promptId": "b20fe594-a1fa-45c4-9afa-b12a0912be14",
  "type": "user",
  "uuid": "6b145b98-d1a7-45c5-929a-293fda0fb213",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"report_path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/dream_reports/dream_20260521T122454/best/review_report.md\\\", \\\"dream_id\\\": \\\"dream_20260521T122454\\\", \\\"tier\\\": \\\"best\\\", \\\"review_visible\\\": true}, \\\"error\\\": \\\"\\\"}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"report_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/dream_reports/dream_20260521T122454/best/review_report.md\", \"dream_id\": \"dream_20260521T122454\", \"tier\": \"best\", \"review_visible\": true}, \"error\": \"\"}"
    }
  },
  "sourceToolAssistantUUID": "71a69fbb-ee5c-4197-a682-c9a8337c8fd7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation",
  "sessionId": "33779107-04cc-4691-9d8a-87f3f46280c6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 29 · 2026-05-21T13:05:02.519Z_

Review submitted. **Overall: 3.5 (Borderline Conference)**, Soundness 3.5, Excitement 3.5, Reproducibility 4.

Key strengths: exact bias identity (R²>0.97), thorough validation (11 experiments, 3,600 MC runs), honest reporting of limitations and tradeoffs, complete contribution package (theory + method + diagnostic + composition).

Key weaknesses: Theorem 1 is imprecise for general K (only exact product form for K=2), narrow practical sweet spot (extreme heterogeneity + sufficient budget + few subgroups), diagnostic criterion validated on small/self-generated evaluation set (CV AUC 0.78 on 24 settings), no robustness analysis to non-differential misclassification violations (A1), inconclusive real-data case study.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6b145b98-d1a7-45c5-929a-293fda0fb213",
  "isSidechain": false,
  "requestId": "req_011CbFm94bBn6jyzSTPxvXKZ",
  "type": "assistant",
  "uuid": "ba8cc053-f205-4a29-9a75-2189c8bc5e36",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation",
  "sessionId": "33779107-04cc-4691-9d8a-87f3f46280c6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HmLVwBsfFyDUUPrfneKwgu",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3418,
      "cache_read_input_tokens": 56323,
      "output_tokens": 195,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3418,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 195,
          "cache_read_input_tokens": 56323,
          "cache_creation_input_tokens": 3418,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3418
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

_source line 30_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[DREAM Review Director] dream_id=20260521T122454 | review_mode=simple | review_visible=True PDF: /home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/dream_reports/dr…",
  "leafUuid": "ba8cc053-f205-4a29-9a75-2189c8bc5e36",
  "sessionId": "33779107-04cc-4691-9d8a-87f3f46280c6"
}
```

---

### Runtime record

_source line 31_

```json
{
  "type": "ai-title",
  "aiTitle": "Review EMNLP paper on HTE and LLM annotation",
  "sessionId": "33779107-04cc-4691-9d8a-87f3f46280c6"
}
```

---
