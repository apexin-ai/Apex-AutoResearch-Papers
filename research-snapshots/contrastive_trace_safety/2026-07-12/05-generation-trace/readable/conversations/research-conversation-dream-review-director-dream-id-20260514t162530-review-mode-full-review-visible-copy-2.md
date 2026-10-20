# Research conversation: [DREAM Review Director] dream_id=20260514T162530 | review_mode=full | review_visible=True PDF: /home/ubuntu/.agent-ml-re

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 60
- **Recorded user turns:** 3
- **Tool calls:** 12
- **Original source:** `logs/chats/exported-trajectories/account-3/ef1befa8-2efd-49dd-aab6-f69049f8448e.jsonl`
- **Structured JSON:** [`bb9e6c079d041ea3bb30.json`](../../sessions/bb/bb9e6c079d041ea3bb30.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-14T16:58:41.197Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-14T16:58:41.197Z",
  "sessionId": "ef1befa8-2efd-49dd-aab6-f69049f8448e",
  "content": "[DREAM Review Director]\ndream_id=20260514T162530 | review_mode=full | review_visible=True\nPDF: /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T162530/best/review_input_db82206b.pdf\n\n（内部编排信息：tier=best，仅用于 submit_dream_review_report 调用。\n你在向 Reviewer 发送审稿任务时，**严禁**提及档位名称 best/median/worst，\n也不要暗示论文结果的好坏。Reviewer 必须盲审。）\n\n任务：对上述 PDF 进行 full 模式审稿。 使用 `dream-review-full` skill 的 dispatch 模板（2 Reviewers：R1 方法+实验、R2 新颖性+相关工作；完整 roundtable：Step 1 独立 → Step 2 交叉分享 → Step 3 收敛 → Step 4 综合）。\n\n## 审稿标准\n\n未指定目标 venue。请按 top ML venue 通用标准审稿（接受率 ~25%，6 分制：1=Strong Reject … 6=Strong Accept）。\n\n## 实验设计参考\n\n完整实验设计（含想象实验列表）：`/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T162530/best/review_context.yaml`\n论文可能未完整反映所有实验——参考此文件判断覆盖度。\n完成后必须调用 `submit_dream_review_report(report, project=\"structfuse-context\", tier=\"best\", dream_id=\"20260514T162530\", review_visible=True)` —— 报告会写入 dream_reports/dream_20260514T162530/best/review_report.md，编排进程通过 subprocess 退出读取它。\n不要调用 submit_review_report_to_research_director / update_review_issues / request_external_review —— 这些工具不在 Dream Review Director 白名单内。\n"
}
```

---

### Runtime record

_source line 2 · 2026-05-14T16:58:41.200Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-14T16:58:41.200Z",
  "sessionId": "ef1befa8-2efd-49dd-aab6-f69049f8448e"
}
```

---

## Round 1

17 recorded events

### User

_source line 3 · 2026-05-14T16:58:41.234Z_

[DREAM Review Director]
dream_id=20260514T162530 | review_mode=full | review_visible=True
PDF: /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T162530/best/review_input_db82206b.pdf

（内部编排信息：tier=best，仅用于 submit_dream_review_report 调用。
你在向 Reviewer 发送审稿任务时，**严禁**提及档位名称 best/median/worst，
也不要暗示论文结果的好坏。Reviewer 必须盲审。）

任务：对上述 PDF 进行 full 模式审稿。 使用 `dream-review-full` skill 的 dispatch 模板（2 Reviewers：R1 方法+实验、R2 新颖性+相关工作；完整 roundtable：Step 1 独立 → Step 2 交叉分享 → Step 3 收敛 → Step 4 综合）。

## 审稿标准

未指定目标 venue。请按 top ML venue 通用标准审稿（接受率 ~25%，6 分制：1=Strong Reject … 6=Strong Accept）。

## 实验设计参考

完整实验设计（含想象实验列表）：`/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T162530/best/review_context.yaml`
论文可能未完整反映所有实验——参考此文件判断覆盖度。
完成后必须调用 `submit_dream_review_report(report, project="structfuse-context", tier="best", dream_id="20260514T162530", review_visible=True)` —— 报告会写入 dream_reports/dream_20260514T162530/best/review_report.md，编排进程通过 subprocess 退出读取它。
不要调用 submit_review_report_to_research_director / update_review_issues / request_external_review —— 这些工具不在 Dream Review Director 白名单内。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "0dbd644e-3638-4b84-b174-ff7865af1dfb",
  "type": "user",
  "uuid": "fd45a342-8a35-49aa-8088-7ce03e9d8b75",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "ef1befa8-2efd-49dd-aab6-f69049f8448e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-14T16:58:41.233Z_

```json
{
  "parentUuid": "fd45a342-8a35-49aa-8088-7ce03e9d8b75",
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
  "uuid": "6d7d50d4-9cff-482b-89ff-015184f54986",
  "timestamp": "2026-05-14T16:58:41.233Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "ef1befa8-2efd-49dd-aab6-f69049f8448e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-14T16:58:41.233Z_

```json
{
  "parentUuid": "6d7d50d4-9cff-482b-89ff-015184f54986",
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
  "uuid": "8ccbcd1a-f6c5-4621-bcd1-c7fc0c53cdd8",
  "timestamp": "2026-05-14T16:58:41.233Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "ef1befa8-2efd-49dd-aab6-f69049f8448e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6 · 2026-05-14T16:58:41.233Z_

```json
{
  "parentUuid": "8ccbcd1a-f6c5-4621-bcd1-c7fc0c53cdd8",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "125e0ec6-16fc-4076-90da-c02522f0adf2",
  "timestamp": "2026-05-14T16:58:41.233Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "ef1befa8-2efd-49dd-aab6-f69049f8448e",
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
  "aiTitle": "Review ML research paper with full evaluation",
  "sessionId": "ef1befa8-2efd-49dd-aab6-f69049f8448e"
}
```

---

### Assistant

_source line 8 · 2026-05-14T16:58:44.786Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to conduct a full review of a PDF paper using the dream-review-full process. Let me start by:

1. Reading the PDF and the review context YAML
2. Setting up the review process with 2 reviewers

Let me first load the necessary tools and read the files.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "125e0ec6-16fc-4076-90da-c02522f0adf2",
  "isSidechain": false,
  "requestId": "req_011Cb2pKSwRxVSnQckvkKAtf",
  "type": "assistant",
  "uuid": "c66b2f7f-dc66-4fd8-acbe-433eda60f194",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "ef1befa8-2efd-49dd-aab6-f69049f8448e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01N3wrE7XqrK3FrgQijFeXxx",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11082,
      "cache_read_input_tokens": 11841,
      "output_tokens": 300,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11082,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 300,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11082,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11082
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

_source line 9 · 2026-05-14T16:58:45.324Z_

开始审稿流程。先读取论文 PDF 和实验设计上下文。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c66b2f7f-dc66-4fd8-acbe-433eda60f194",
  "isSidechain": false,
  "requestId": "req_011Cb2pKSwRxVSnQckvkKAtf",
  "type": "assistant",
  "uuid": "12fced03-ea31-47b4-9805-8d649bcca70d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "ef1befa8-2efd-49dd-aab6-f69049f8448e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01N3wrE7XqrK3FrgQijFeXxx",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11082,
      "cache_read_input_tokens": 11841,
      "output_tokens": 300,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11082,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 300,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11082,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11082
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

_source line 10 · 2026-05-14T16:58:46.395Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Gb9ETRsGRy1GDFNNqfVmTc`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T162530/best/review_input_db82206b.pdf"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "12fced03-ea31-47b4-9805-8d649bcca70d",
  "isSidechain": false,
  "requestId": "req_011Cb2pKSwRxVSnQckvkKAtf",
  "type": "assistant",
  "uuid": "c3b83287-e7bc-4014-8198-0a6892fb916f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "ef1befa8-2efd-49dd-aab6-f69049f8448e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01N3wrE7XqrK3FrgQijFeXxx",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11082,
      "cache_read_input_tokens": 11841,
      "output_tokens": 300,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11082,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 300,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11082,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11082
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

_source line 11 · 2026-05-14T16:58:46.456Z_

<details><summary>↩ Tool result · reported error · `toolu_01Gb9ETRsGRy1GDFNNqfVmTc`</summary>

```text
This PDF has 11 pages, which is too many to read at once. Use the pages parameter to read specific page ranges (e.g., pages: "1-5"). Maximum 20 pages per request.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c3b83287-e7bc-4014-8198-0a6892fb916f",
  "isSidechain": false,
  "promptId": "0dbd644e-3638-4b84-b174-ff7865af1dfb",
  "type": "user",
  "uuid": "050e0d89-58c2-4110-9104-45b239da9456",
  "toolUseResult": "Error: This PDF has 11 pages, which is too many to read at once. Use the pages parameter to read specific page ranges (e.g., pages: \"1-5\"). Maximum 20 pages per request.",
  "sourceToolAssistantUUID": "c3b83287-e7bc-4014-8198-0a6892fb916f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "ef1befa8-2efd-49dd-aab6-f69049f8448e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-14T16:58:46.757Z_

<details open><summary>🔧 Tool call — Read · `toolu_01TfejZC5ZiwxWYKxoYXfKnJ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T162530/best/review_context.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "050e0d89-58c2-4110-9104-45b239da9456",
  "isSidechain": false,
  "requestId": "req_011Cb2pKSwRxVSnQckvkKAtf",
  "type": "assistant",
  "uuid": "fce96999-8a84-405e-84cf-1db0bd857861",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "ef1befa8-2efd-49dd-aab6-f69049f8448e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01N3wrE7XqrK3FrgQijFeXxx",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11082,
      "cache_read_input_tokens": 11841,
      "output_tokens": 300,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11082,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 300,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11082,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11082
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

_source line 13 · 2026-05-14T16:58:47.135Z_

<details><summary>↩ Tool result · `toolu_01TfejZC5ZiwxWYKxoYXfKnJ`</summary>

```text
1	narrative_guidance: '全 18 runs（9 seeds × 2 encoders × 3 strategies）完整复现 pilot pattern。
2	  Embedding mining 在两个 encoder 上均显著优于 random（Qwen +2.0pp, StarCoder +1.5pp, 95% CI
3	  下界 > 0）。 Dataflow 在 Qwen 上条件性获益（+1.0pp, CI 下界 > 0），StarCoder 上无显著差异（-0.2pp, CI 含零）。
4	  BM25 baseline 实证关闭 CoCoHaNeRe 论证（BM25 vs random: Qwen -2.5pp, StarCoder -2.7pp）。
5	  SWE-bench Lite downstream +2.5pp embedding, +3.2pp dataflow resolve rate delta。
6	  三条 claim 原样成立，EMNLP Main 强投 framing 无需调整。 M2 full anchors — Qwen random R@1=0.545,
7	  embedding=0.565, dataflow=0.555; StarCoder random R@1=0.460, embedding=0.475, dataflow=0.458。
8	
9	  '
10	imagined_experiments:
11	- name: SWE-bench Lite End-to-End Evaluation
12	  plan_id: plan_003
13	  description: '3 strategies × best Qwen checkpoint, Qwen3.6-27B agent, 300 SWE-bench
14	    Lite instances. Retriever 提供 top-k context files，agent 生成 patch，评估 resolve rate。
15	
16	    '
17	  expected_results:
18	    random_resolve_rate: 0.22
19	    random_resolved_count: 66
20	    embedding_resolve_rate: 0.245
21	    embedding_resolved_count: 73
22	    dataflow_resolve_rate: 0.252
23	    dataflow_resolved_count: 76
24	    embedding_minus_random_pp: 2.5
25	    dataflow_minus_random_pp: 3.2
26	    dataflow_minus_embedding_pp: 0.7
27	    total_instances: 300
28	    retriever_top_k: 5
29	    agent_model: Qwen3.6-27B
30	  result_rationale: 'Embedding retriever 在 SWE-bench 上提升 +2.5pp，因为 bug-fix patch 通常涉及与
31	    issue 描述 语义相似但非完全匹配的文件——embedding mining 训练使 retriever 更擅长区分"近似但无关" 与"近似且相关"的文件。Dataflow
32	    额外提升 +0.7pp（总 +3.2pp vs random）因为 SWE-bench patch 经常跨函数/跨模块（约 40% 涉及 caller-callee
33	    关系），dataflow negatives 训练使 retriever 理解"调用链上的文件更可能共同出现在 patch 中"。Delta 幅度从 retrieval
34	    R@1 的 +2.0/+1.0pp 放大到下游 resolve rate 的 +2.5/+3.2pp，符合检索质量在端到端任务中 的杠杆效应——正确检索一个关键文件可以使原本完全失败的
35	    patch 变为可解决。 效果幅度在 swebench_resolve_rate_delta_pp [1.5, 4.0] 范围内。
36	
37	    '
38	  tables:
39	  - name: 'Table 4: SWE-bench Lite Resolve Rate'
40	    columns:
41	    - Strategy
42	    - Resolved
43	    - Total
44	    - Rate (%)
45	    - Δ vs Random (pp)
46	    rows:
47	    - - random
48	      - 66
49	      - 300
50	      - 22.0
51	      - —
52	    - - embedding
53	      - 73
54	      - 300
55	      - 24.3
56	      - '+2.3'
57	    - - dataflow
58	      - 76
59	      - 300
60	      - 25.3
61	      - '+3.3'
62	  - name: 'Table 4b: SWE-bench by Patch Complexity'
63	    columns:
64	    - Patch Type
65	    - N
66	    - random (%)
67	    - embedding (%)
68	    - dataflow (%)
69	    rows:
70	    - - single-file
71	      - 189
72	      - 28.0
73	      - 30.7
74	      - 30.2
75	    - - multi-file
76	      - 111
77	      - 11.7
78	      - 14.4
79	      - 17.1
80	  figures_description:
81	  - 'Fig 5: SWE-bench resolve rate bar chart (3 strategies) with bootstrap 95% CI
82	    whiskers'
83	  - 'Fig 5b: Scatter plot — retrieval R@1 rank vs resolve rate per instance, colored
84	    by strategy'
85	  analysis: 'Multi-file patches（占 37%）是 dataflow 拉开差距的主要来源：dataflow 在 multi-file 上
86	    +5.4pp vs random，远大于 single-file 的 +2.2pp。这与 Claim 2 一致——dataflow negatives 使
87	    retriever 更好地理解跨模块依赖。Embedding vs random 在 multi-file 上也有 +2.7pp，说明更难的 negatives
88	    普遍有益。总体 resolve rate 22-25% 与 SweRank/SWE-Fixer 文献报告的 retriever-only baseline
89	    一致。
90	
91	    '
92	- name: RepoBench-R Cross-File Retrieval with Multi-Seed CIs
93	  plan_id: plan_004
94	  description: 'RepoBench-R test_easy (pool ~6) 和 test_hard (pool ~18) 上评估 9 seeds
95	    × 3 strategies × 2 encoders，报告 R@1 均值 + 95% bootstrap CI。
96	
97	    '
98	  expected_results:
99	    qwen_test_hard:
100	      random_R1_mean: 0.621
101	      random_R1_ci:
102	      - 0.614
103	      - 0.628
104	      embedding_R1_mean: 0.642
105	      embedding_R1_ci:
106	      - 0.634
107	      - 0.65
108	      dataflow_R1_mean: 0.633
109	      dataflow_R1_ci:
110	      - 0.624
111	      - 0.642
112	      embedding_minus_random_pp: 2.1
113	      dataflow_minus_random_pp: 1.2
114	    qwen_test_easy:
115	      random_R1_mean: 0.843
116	      embedding_R1_mean: 0.855
117	      dataflow_R1_mean: 0.85
118	      embedding_minus_random_pp: 1.2
119	    starcoder_test_hard:
120	      random_R1_mean: 0.574
121	      random_R1_ci:
122	      - 0.566
123	      - 0.582
124	      embedding_R1_mean: 0.589
125	      embedding_R1_ci:
126	      - 0.58
127	      - 0.598
128	      dataflow_R1_mean: 0.572
129	      dataflow_R1_ci:
130	      - 0.562
131	      - 0.582
132	      embedding_minus_random_pp: 1.5
133	      dataflow_minus_random_pp: -0.2
134	    starcoder_test_easy:
135	      random_R1_mean: 0.812
136	      embedding_R1_mean: 0.822
137	      dataflow_R1_mean: 0.81
138	    repobench_R1_delta_pp_embedding_avg: 1.8
139	    bootstrap_CI_width_R1_pp_avg: 1.2
140	  result_rationale: 'RepoBench-R 是 cross-file completion 任务，pool 更小（6-18），绝对 R@1 更高。
141	    Embedding mining 在两个 encoder 上均显著提升 test_hard R@1（Qwen +2.1pp, StarCoder +1.5pp），
142	    因为 pool=18 仍有足够 distractors 使 mining 质量差异体现。Test_easy pool=6 接近 ceiling，delta
143	    被压缩但方向一致。Dataflow 在 Qwen test_hard 上 +1.2pp 但 CI 刚好 排除零，StarCoder 上无效（-0.2pp，CI
144	    含零）——与 SWE-smith 上的 encoder-strategy interaction 完全一致，说明 pattern 跨 benchmark 稳定。CI
145	    宽度 ~1.2pp 在 bootstrap_CI_width_R1_pp [0.5, 2.0] 范围内，9 seeds 提供足够统计功效。
146	
147	    '
148	  tables:
149	  - name: 'Table 5: RepoBench-R Results (test_hard, pool≈18)'
150	    columns:
151	    - Encoder
152	    - Strategy
153	    - R@1 (%)
154	    - 95% CI
155	    - Δ vs Random (pp)
156	    rows:
157	    - - Qwen
158	      - random
159	      - 62.1
160	      - '[61.4, 62.8]'
161	      - —
162	    - - Qwen
163	      - embedding
164	      - 64.2
165	      - '[63.4, 65.0]'
166	      - '+2.1'
167	    - - Qwen
168	      - dataflow
169	      - 63.3
170	      - '[62.4, 64.2]'
171	      - '+1.2'
172	    - - StarCoder
173	      - random
174	      - 57.4
175	      - '[56.6, 58.2]'
176	      - —
177	    - - StarCoder
178	      - embedding
179	      - 58.9
180	      - '[58.0, 59.8]'
181	      - '+1.5'
182	    - - StarCoder
183	      - dataflow
184	      - 57.2
185	      - '[56.2, 58.2]'
186	      - −0.2
187	  figures_description:
188	  - 'Fig 6: RepoBench-R R@1 grouped bar chart (2 encoders × 3 strategies) with CI
189	    whiskers, test_easy vs test_hard side by side'
190	  analysis: 'Cross-benchmark 一致性是 best tier 的关键证据：embedding mining 在 SWE-smith 和 RepoBench-R
191	    上均显著提升两个 encoder，dataflow 条件性获益仅限 Qwen。这排除了 "结果仅限单一 benchmark" 的 reviewer concern。Test_easy
192	    上 delta 被压缩（pool=6 ceiling effect）是预期行为，反向验证了 pool size 对绝对效果幅度的调节作用。
193	
194	    '
195	- name: Stratified Analysis with Structural Coverage & Neg Difficulty Quartiles
196	  plan_id: plan_005
197	  description: '5 层分层分析：repo size / pool size / query-positive similarity / structural
198	    data availability (34% vs 66%) / neg_difficulty quartile。使用 M2 best checkpoints
199	    在 SWE-smith validation 上重新评估。
200	
201	    '
202	  expected_results:
203	    stratum_structural_available:
204	      with_dataflow_34pct:
205	        qwen_dataflow_minus_random_pp: 2.8
206	        qwen_dataflow_minus_embedding_pp: 1.3
207	        starcoder_dataflow_minus_random_pp: 0.1
208	        n_instances: ~5200
209	      fallback_66pct:
210	        qwen_dataflow_minus_random_pp: 0.1
211	        qwen_dataflow_minus_embedding_pp: -0.2
212	        starcoder_dataflow_minus_random_pp: -0.3
213	        n_instances: ~10000
214	    stratum_neg_difficulty_quartile:
215	      Q1_easiest:
216	        qwen_embedding_minus_random_pp: 0.8
217	        qwen_dataflow_minus_random_pp: 0.3
218	      Q2:
219	        qwen_embedding_minus_random_pp: 1.5
220	        qwen_dataflow_minus_random_pp: 0.7
221	      Q3:
222	        qwen_embedding_minus_random_pp: 2.4
223	        qwen_dataflow_minus_random_pp: 1.2
224	      Q4_hardest:
225	        qwen_embedding_minus_random_pp: 3.2
226	        qwen_dataflow_minus_random_pp: 2.1
227	    stratum_repo_size:
228	      small_lt50:
229	        embedding_delta_pp: 2.8
230	        n: ~500
231	      medium_50_200:
232	        embedding_delta_pp: 2.2
233	        n: ~4100
234	      large_200_500:
235	        embedding_delta_pp: 1.8
236	        n: ~5500
237	      xlarge_500plus:
238	        embedding_delta_pp: 1.6
239	        n: ~5100
240	    stratum_pool_size:
241	      pool_lt20:
242	        embedding_delta_pp: 1.0
243	        dataflow_delta_pp: 0.3
244	      pool_20_50:
245	        embedding_delta_pp: 2.1
246	        dataflow_delta_pp: 1.0
247	      pool_gt50:
248	        embedding_delta_pp: 2.5
249	        dataflow_delta_pp: 1.4
250	    stratum_query_pos_sim:
251	      high_sim_gt095:
252	        embedding_delta_pp: 2.6
253	        dataflow_delta_pp: 1.8
254	      medium_sim_085_095:
255	        embedding_delta_pp: 1.9
256	        dataflow_delta_pp: 0.8
257	      low_sim_lt085:
258	        embedding_delta_pp: 1.2
259	        dataflow_delta_pp: 0.2
260	  result_rationale: 'Structural-available stratum（34%）上 dataflow 优势放大到 +2.8pp（Qwen），因为这些
261	    instance 实际接收了 dataflow-disconnected negatives——真实训练信号未被 fallback 稀释。 Fallback
262	    stratum（66%）上 dataflow ≈ embedding（±0.2pp），因为 fallback 时 dataflow 策略退化为 embedding
263	    或 random 选择，无结构信号注入。这一分解直接回应 reviewer 关于 "34% coverage 稀释 signal" 的 concern——真实
264	    per-instance 效果是 +2.8pp 而非 pooled +1.0pp。Neg_difficulty Q4（最难 quartile）上 delta
265	    最大（embedding +3.2pp, dataflow +2.1pp），符合 representation saturation 理论——Qwen 在高
266	    pos_sim 区域最需要 harder negatives，而 Q4 恰好是 margin 最小、分辨最难的 instances。Q1（最容易）delta
267	    最小 因为 random negatives 已经足够容易区分。Repo size 上 small repo delta 更大因为 小 repo 的 candidate
268	    pool 更集中，mining 策略差异更容易体现。
269	
270	    '
271	  tables:
272	  - name: 'Table 7: Stratified R@1 Delta by Structural Data Availability (Qwen)'
273	    columns:
274	    - Stratum
275	    - N
276	    - random R@1
277	    - embedding R@1
278	    - dataflow R@1
279	    - df−rand (pp)
280	    rows:
281	    - - With dataflow (34%)
282	      - ~5.2K
283	      - 53.1
284	      - 55.4
285	      - 55.9
286	      - '+2.8'
287	    - - Fallback (66%)
288	      - ~10K
289	      - 55.2
290	      - 57.3
291	      - 55.3
292	      - '+0.1'
293	    - - Overall
294	      - ~15.2K
295	      - 54.5
296	      - 56.5
297	      - 55.5
298	      - '+1.0'
299	  - name: 'Table 7b: R@1 Delta by Neg Difficulty Quartile (Qwen)'
300	    columns:
301	    - Quartile
302	    - margin_mean
303	    - emb−rand (pp)
304	    - df−rand (pp)
305	    rows:
306	    - - Q1 (easiest)
307	      - 0.142
308	      - '+0.8'
309	      - '+0.3'
310	    - - Q2
311	      - 0.078
312	      - '+1.5'
313	      - '+0.7'
314	    - - Q3
315	      - 0.031
316	      - '+2.4'
317	      - '+1.2'
318	    - - Q4 (hardest)
319	      - 0.008
320	      - '+3.2'
321	      - '+2.1'
322	  figures_description:
323	  - 'Fig 7: Heatmap — R@1 delta (strategy × stratum), separate panels for Qwen and
324	    StarCoder'
325	  - 'Fig 8: Neg difficulty quartile vs R@1 delta line plot, 3 strategies overlaid'
326	  analysis: 'Stratified analysis 提供了论文中最强的 mechanistic 证据。Neg_difficulty Q4 的 +3.2pp
327	    embedding delta 是 overall +2.0pp 的 1.6 倍——越难的 instances 从 harder negatives 获益越多，这是
328	    representation saturation 理论的直接预测。Structural-available vs fallback 分解消除了 "diluted
329	    signal" concern 并揭示 dataflow 的真实 per-instance 效果（+2.8pp）远大于 pooled 报告值。
330	
331	    '
332	- name: Call-Graph Hop Depth Ablation (1/2/3-hop)
333	  plan_id: plan_007
334	  description: '比较 1-hop / 2-hop / 3-hop call-graph bounding 对 dataflow negative 质量的影响。
335	    Qwen encoder, 1 seed, SWE-smith validation。
336	
337	    '
338	  expected_results:
339	    hop_1:
340	      R1: 0.548
341	      connected_coverage_pct: 12.4
342	      negatives_per_query_mean: 18.2
343	    hop_2:
344	      R1: 0.555
345	      connected_coverage_pct: 34.3
346	      negatives_per_query_mean: 31.7
347	    hop_3:
348	      R1: 0.551
349	      connected_coverage_pct: 58.6
350	      negatives_per_query_mean: 42.1
351	    optimal_hop: 2
352	    hop2_minus_hop1_pp: 0.7
353	    hop3_minus_hop2_pp: -0.4
354	  result_rationale: '2-hop 是最优平衡点。1-hop 太保守——仅 12.4% coverage 意味着大部分 instance 没有足够的
355	    connected 节点来定义 "disconnected" negatives，退化为 random。3-hop 过于宽松——58.6% coverage
356	    下 "disconnected" 的定义变得太窄，许多语义相关但间接连接的文件被错误排除在 negative pool 外，引入噪声。2-hop 的 34.3%
357	    coverage（与 M1 extraction 的 structural data rate 一致）在 "enough connected nodes to
358	    define meaningful disconnection" 和 "disconnected set still contains genuinely
359	    unrelated files" 之间取得平衡。
360	
361	    '
362	  tables:
363	  - name: 'Table 9: Hop Depth Ablation (Qwen, dataflow strategy)'
364	    columns:
365	    - Hops
366	    - Coverage (%)
367	    - Neg/query
368	    - R@1 (%)
369	    - Δ vs 2-hop (pp)
370	    rows:
371	    - - 1
372	      - 12.4
373	      - 18.2
374	      - 54.8
375	      - −0.7
376	    - - 2
377	      - 34.3
378	      - 31.7
379	      - 55.5
380	      - —
381	    - - 3
382	      - 58.6
383	      - 42.1
384	      - 55.1
385	      - −0.4
386	  figures_description:
387	  - 'Fig S1: Hop depth vs R@1 line plot with coverage % on secondary y-axis'
388	  analysis: '2-hop optimal 符合 inter-procedural dataflow 的语义：1-hop = 直接 caller/callee，
389	    2-hop = caller 的 caller 或 callee 的 callee（一层间接调用），3-hop 开始包含 过于间接的关系。论文可以强调 2-hop
390	    选择有 principled 依据而非纯粹 empirical tuning。
391	
392	    '
393	- name: Training Data Size Scaling (1K/3K/5K)
394	  plan_id: plan_008
395	  description: '固定 Qwen encoder + embedding strategy，训练数据从 1K / 3K / 5K instances
396	    增长， 观察 R@1 变化和策略排名稳定性。
397	
398	    '
399	  expected_results:
400	    size_1K:
401	      random_R1: 0.51
402	      embedding_R1: 0.522
403	      dataflow_R1: 0.515
404	      embedding_minus_random_pp: 1.2
405	      seed_std: 0.015
406	    size_3K:
407	      random_R1: 0.532
408	      embedding_R1: 0.55
409	      dataflow_R1: 0.541
410	      embedding_minus_random_pp: 1.8
411	      seed_std: 0.01
412	    size_5K:
413	      random_R1: 0.545
414	      embedding_R1: 0.565
415	      dataflow_R1: 0.555
416	      embedding_minus_random_pp: 2.0
417	      seed_std: 0.008
418	    ranking_stable: true
419	    monotonic_improvement: true
420	  result_rationale: '策略排名在 1K/3K/5K 三个尺度上保持一致（embedding > dataflow > random），但 delta
421	    幅度随数据量增大而增大——1K 时 +1.2pp，5K 时 +2.0pp。这是因为更大的训练集提供更多 diverse negatives，使 mining
422	    策略的差异更充分地体现。1K 时 seed 方差较大（std=0.015） 因为 negative 多样性不足，个别 seed 的 negative 采样偶然性影响结果。5K
423	    时方差收敛 （std=0.008），mining 策略的信号超过采样噪声。No diminishing returns at 5K suggests further
424	    scaling could help, but is beyond scope。
425	
426	    '
427	  tables:
428	  - name: 'Table 10: Data Size Scaling (Qwen)'
429	    columns:
430	    - Size
431	    - random R@1
432	    - embedding R@1
433	    - dataflow R@1
434	    - emb−rand (pp)
435	    - σ across seeds
436	    rows:
437	    - - 1K
438	      - 51.0
439	      - 52.2
440	      - 51.5
441	      - '+1.2'
442	      - 1.5
443	    - - 3K
444	      - 53.2
445	      - 55.0
446	      - 54.1
447	      - '+1.8'
448	      - 1.0
449	    - - 5K
450	      - 54.5
451	      - 56.5
452	      - 55.5
453	      - '+2.0'
454	      - 0.8
455	  figures_description:
456	  - 'Fig S2: R@1 vs training size for 3 strategies, with shaded seed variance bands'
457	  analysis: 'Monotonic scaling + stable ranking 表明结果不是 small-data artifact。5K 时未见
458	    diminishing returns，暗示更大数据集可能进一步放大差异。这对 reviewer "effect size marginal" concern
459	    有价值——delta 仍在增长，当前 +2.0pp 是下界而非上界。
460	
461	    '
462	- name: Fusion Head Ablation
463	  plan_id: plan_009
464	  description: '比较 embedding-only / structural-features-only / combined fusion head，
465	    隔离 training-time mining 价值与 inference-time feature injection。
466	
467	    '
468	  expected_results:
469	    embedding_only:
470	      qwen_R1: 0.565
471	      starcoder_R1: 0.475
472	    structural_features_only:
473	      qwen_R1: 0.498
474	      starcoder_R1: 0.421
475	    combined_fusion:
476	      qwen_R1: 0.561
477	      starcoder_R1: 0.472
478	    embedding_only_minus_combined_pp: 0.4
479	    conclusion: mining > fusion; structural features at inference add noise
480	  result_rationale: 'Embedding-only（仅用 embedding mining 训练的 retriever，inference 时不注入结构特征）
481	    表现最好或 tied with combined。Combined fusion 略低 0.4pp 因为 inference-time structural
482	    features 引入了不精确的 CodeQL connectivity 信号——recall 某些 CodeQL extraction 失败的 instance
483	    反而被错误降权。Structural-features-only（不用 mining 训练， 仅在 inference 注入结构特征）远低于 embedding-only（-6.7pp
484	    Qwen），证明核心价值在 training-time negative mining 而非 inference-time feature engineering。
485	    这一结果对 paper framing 极为重要：StructFuse 的贡献是 mining strategy，不是 fusion。
486	
487	    '
488	  tables:
489	  - name: 'Table 11: Fusion Head Ablation'
490	    columns:
491	    - Configuration
492	    - Qwen R@1 (%)
493	    - StarCoder R@1 (%)
494	    rows:
495	    - - embedding-only (ours)
496	      - 56.5
497	      - 47.5
498	    - - structural-features-only
499	      - 49.8
500	      - 42.1
501	    - - combined fusion
502	      - 56.1
503	      - 47.2
504	  figures_description:
505	  - 'Fig S3: Ablation bar chart comparing 3 fusion configurations'
506	  analysis: '训练时注入 structural signal 通过 negative mining（间接信号）比 inference 时直接注入 structural
507	    features（直接信号）更有效。可能原因：mining 让 encoder 自己学习结构相关的 representation，而直接注入 features
508	    绕过了 encoder 的学习过程，且 CodeQL 34% coverage 意味着 66% instance 在 inference 时收到 zero-vector
509	    structural features，引入 noise。
510	
511	    '
512	- name: Dataflow-Distance Weighted vs Binary Negatives
513	  plan_id: plan_010
514	  description: '比较 binary connected/disconnected 与 dataflow-distance weighted negative
515	    sampling。 Weighted: disconnected 且 hop-distance 更远的文件被赋予更高采样概率。
516	
517	    '
518	  expected_results:
519	    binary_qwen_R1: 0.555
520	    weighted_qwen_R1: 0.558
521	    binary_starcoder_R1: 0.458
522	    weighted_starcoder_R1: 0.459
523	    weighted_minus_binary_qwen_pp: 0.3
524	    weighted_minus_binary_starcoder_pp: 0.1
525	  result_rationale: 'Weighted 在 Qwen 上仅微弱提升 +0.3pp（不显著），StarCoder 上几乎无差异。 原因：binary
526	    disconnected/connected 已经捕获了最关键的 structural distinction—— "是否在调用链上"。进一步按 hop distance
527	    加权引入的额外信号被 noise 抵消：距离更远 不一定意味着更好的 negative（一个完全无关的 utility 文件可能 hop=∞ 但也是 trivial
528	    negative）。 Binary 的简洁性是优势——fewer hyperparameters, same effect。
529	
530	    '
531	  tables:
532	  - name: 'Table S1: Weighted vs Binary Dataflow Negatives'
533	    columns:
534	    - Method
535	    - Qwen R@1 (%)
536	    - StarCoder R@1 (%)
537	    - Δ vs Binary (pp)
538	    rows:
539	    - - Binary (default)
540	      - 55.5
541	      - 45.8
542	      - —
543	    - - Distance-weighted
544	      - 55.8
545	      - 45.9
546	      - +0.3 / +0.1
547	  figures_description: []
548	  analysis: 'Binary is sufficient — complexity of weighted sampling not justified.
549	    论文可在 ablation section 用一句话报告这一 negative result， 强化 "simple binary structural signal
550	    is the key insight" 的 narrative。
551	
552	    '
553	- name: SWE-bench Failure Analysis (50 cases)
554	  plan_id: plan_011
555	  description: '从 random retriever 的 SWE-bench 失败案例中抽样 50 个，人工分类失败原因， 标注 dataflow
556	    信号是否可能帮助。
557	
558	    '
559	  expected_results:
560	    total_analyzed: 50
561	    category_breakdown:
562	      retrieval_failure_wrong_files: 22
563	      retrieval_success_but_agent_fail: 15
564	      insufficient_context_window: 7
565	      test_environment_issue: 4
566	      ambiguous_issue_description: 2
567	    dataflow_could_help:
568	      true: 14
569	      partially: 5
570	      false: 31
571	    dataflow_help_rate: 0.28
572	    key_pattern: '14/22 retrieval failures involve cross-module dependencies where
573	      the gold file is a caller/callee of a retrieved-but-wrong file — dataflow connectivity
574	      would directly address these.
575	
576	      '
577	  result_rationale: '50 个失败中 22 个是 retrieval failure（检索到错误文件），其中 14 个涉及跨模块依赖—— 被检索的文件和
578	    gold 文件有高文本相似度但分属不同 call chain。Dataflow negatives 训练 恰好针对这类 confound。15 个 retrieval
579	    success but agent fail 说明 retrieval 不是 唯一瓶颈——agent 的 patch 生成能力也是限制因素。这为论文提供了
580	    "ceiling analysis"： 即使 perfect retrieval，resolve rate 上限约 85%（15% 是 agent 能力限制）。
581	
582	    '
583	  tables:
584	  - name: 'Table S2: Failure Category Breakdown'
585	    columns:
586	    - Category
587	    - Count
588	    - '% of 50'
589	    - Dataflow Could Help?
590	    rows:
591	    - - 'Retrieval: wrong files'
592	      - 22
593	      - 44
594	      - 14/22 (64%)
595	    - - Retrieval OK, agent fail
596	      - 15
597	      - 30
598	      - N/A
599	    - - Context window limit
600	      - 7
601	      - 14
602	      - 5/7 partially
603	    - - Test env issue
604	      - 4
605	      - 8
606	      - 'No'
607	    - - Ambiguous issue
608	      - 2
609	      - 4
610	      - 'No'
611	  figures_description:
612	  - 'Fig S4: Sankey diagram — failure flow from retrieval stage to resolution outcome'
613	  analysis: '28% of failures could benefit from dataflow signal, consistent with the
614	    observed +3.2pp resolve rate improvement. The 64% rate within retrieval failures
615	    confirms that cross-module dependency is the primary retrieval challenge, directly
616	    supporting Claim 2''s motivation.
617	
618	    '
619	- name: Qualitative Examples (5-10 cases)
620	  plan_id: plan_012
621	  description: '从 SWE-bench 和 SWE-smith 中选取 5-10 个 dataflow negatives 改变检索结果的典型案例，
622	    展示 structural signal 的具体作用机制。
623	
624	    '
625	  expected_results:
626	    total_examples: 8
627	    example_categories:
628	      caller_callee_confusion: 3
629	      utility_file_distraction: 2
630	      cross_module_import_chain: 2
631	      test_file_vs_source: 1
632	    illustrative_example:
633	      issue: django/django#12345 — QuerySet.filter() returns wrong results with nested
634	        Q objects
635	      random_retriever_top1: django/db/models/query.py (text match on 'filter')
636	      dataflow_retriever_top1: django/db/models/sql/query.py (actual SQL generation
637	        called by filter)
638	      gold: django/db/models/sql/query.py
639	      explanation: 'Random retriever picks query.py (contains ''filter'' method signature)
640	        but the bug is in sql/query.py (the downstream SQL builder called by filter).
641	        Dataflow training teaches the model that sql/query.py is structurally connected
642	        to query.py via 2-hop call chain, making it a better negative for other instances,
643	        which in turn improves the model''s ability to rank the actual implementation
644	        file higher.
645	
646	        '
647	  result_rationale: '8 个案例覆盖 4 个失败模式：caller-callee confusion（3 个，最常见——文本相似的 wrapper
648	    函数 vs 实际实现）、utility file distraction（2 个——高文本重叠的 helper 文件干扰）、 cross-module import
649	    chain（2 个——A 导入 B 导入 C，bug 在 C 但文本匹配 A）、test vs source（1 个——test file 包含几乎完整的
650	    source code 复制）。这些案例具体展示了 "lexical similarity ≠ structural relevance" 的核心 insight。
651	
652	    '
653	  tables: []
654	  figures_description:
655	  - 'Fig 9: Side-by-side retrieval ranking visualization for 3 representative cases,
656	    showing file dependency graph with highlighted paths'
657	  analysis: 'Qualitative examples serve as the paper''s "aha moment" — they make the
658	    abstract representation geometry argument concrete. Reviewer-facing value: even
659	    skeptics who question statistical significance can see the mechanism operating
660	    on real code.
661	
662	    '
663	- name: Temperature Ablation τ ∈ {0.05, 0.1, 0.2}
664	  plan_id: plan_014
665	  description: '3 temperatures × 3 strategies × 2 encoders, 1 seed each. 测试 strategy
666	    ranking 是否 regime-specific。
667	
668	    '
669	  expected_results:
670	    tau_005:
671	      qwen_random_R1: 0.558
672	      qwen_embedding_R1: 0.577
673	      qwen_dataflow_R1: 0.569
674	      qwen_embedding_minus_random_pp: 1.9
675	      starcoder_random_R1: 0.47
676	      starcoder_embedding_R1: 0.485
677	      starcoder_dataflow_R1: 0.467
678	      starcoder_embedding_minus_random_pp: 1.5
679	    tau_010:
680	      qwen_random_R1: 0.545
681	      qwen_embedding_R1: 0.565
682	      qwen_dataflow_R1: 0.555
683	      qwen_embedding_minus_random_pp: 2.0
684	      starcoder_random_R1: 0.46
685	      starcoder_embedding_R1: 0.475
686	      starcoder_dataflow_R1: 0.458
687	      starcoder_embedding_minus_random_pp: 1.5
688	    tau_020:
689	      qwen_random_R1: 0.53
690	      qwen_embedding_R1: 0.546
691	      qwen_dataflow_R1: 0.538
692	      qwen_embedding_minus_random_pp: 1.6
693	      starcoder_random_R1: 0.448
694	      starcoder_embedding_R1: 0.461
695	      starcoder_dataflow_R1: 0.447
696	      starcoder_embedding_minus_random_pp: 1.3
697	    ranking_preserved_across_tau: true
698	    optimal_tau: 0.05
699	  result_rationale: 'Strategy ranking（embedding > dataflow > random for Qwen; embedding
700	    > random ≈ dataflow for StarCoder）在三个 temperature 下保持一致。τ=0.05 绝对性能最高因为 sharper
701	    temperature 使 contrastive loss 更有效地区分相似度差异（harder gradient signal）。 τ=0.2 下所有策略性能下降且
702	    delta 缩小（1.6pp vs 2.0pp），因为 softer temperature 减弱了 negative 选择质量的影响——当所有 similarity
703	    被压缩到窄范围内，hard vs easy negatives 的梯度差异变小。关键结论：findings 不是 temperature-regime-specific，
704	    直接回应 median reviewer 的 "τ=0.05 unusually low" concern。
705	
706	    '
707	  tables:
708	  - name: 'Table 8: Temperature Ablation (R@1 %)'
709	    columns:
710	    - τ
711	    - Encoder
712	    - random
713	    - embedding
714	    - dataflow
715	    - emb−rand (pp)
716	    rows:
717	    - - 0.05
718	      - Qwen
719	      - 55.8
720	      - 57.7
721	      - 56.9
722	      - '+1.9'
723	    - - 0.05
724	      - StarCoder
725	      - 47.0
726	      - 48.5
727	      - 46.7
728	      - '+1.5'
729	    - - 0.1
730	      - Qwen
731	      - 54.5
732	      - 56.5
733	      - 55.5
734	      - '+2.0'
735	    - - 0.1
736	      - StarCoder
737	      - 46.0
738	      - 47.5
739	      - 45.8
740	      - '+1.5'
741	    - - 0.2
742	      - Qwen
743	      - 53.0
744	      - 54.6
745	      - 53.8
746	      - '+1.6'
747	    - - 0.2
748	      - StarCoder
749	      - 44.8
750	      - 46.1
751	      - 44.7
752	      - '+1.3'
753	  figures_description:
754	  - 'Fig S5: Temperature × strategy interaction plot (R@1 on y-axis, τ on x-axis,
755	    separate lines per strategy)'
756	  analysis: 'Ranking stability across τ 是重要的 robustness evidence。τ=0.2 下 delta 缩小但
757	    不翻转，说明 mining quality 的价值在不同 loss sharpness 下都存在。Paper 可以报告 τ=0.05 作为 alternative
758	    best configuration 但选择 τ=0.1 作为 default（更常见的 literature default）。
759	
760	    '
761	- name: Dynamic vs Static Embedding Mining
762	  plan_id: plan_015
763	  description: 'Dynamic: 每 epoch 重新用当前 encoder 挖 embedding negatives。 Static: 仅用 pretrained
764	    encoder 挖一次（当前做法）。 Qwen + StarCoder, 1 seed each。
765	
766	    '
767	  expected_results:
768	    qwen_static_R1: 0.565
769	    qwen_dynamic_R1: 0.568
770	    qwen_dynamic_minus_static_pp: 0.3
771	    starcoder_static_R1: 0.475
772	    starcoder_dynamic_R1: 0.477
773	    starcoder_dynamic_minus_static_pp: 0.2
774	    dynamic_significant: false
775	    curriculum_confound_ruled_out: true
776	  result_rationale: 'Dynamic mining 仅微弱提升 +0.2-0.3pp（不显著），因为 LoRA rank 16 的 fine-tuning
777	    只轻微改变 embedding space——pretrained encoder 的 nearest neighbors 在训练后 仍然大部分相同。这排除了
778	    "static mining 的优势来自 curriculum effect（early epochs 看到 harder negatives 然后 negatives
779	    变 stale）" 的 confound——即使更新 negatives， 效果几乎不变。对 Claim 2 很重要：说明 mining strategy
780	    的选择（what to mine）比 mining schedule（when to mine）更关键。Dynamic mining 的 compute overhead（每
781	    epoch 重新 encode + kNN）不 justified。
782	
783	    '
784	  tables:
785	  - name: 'Table 13: Static vs Dynamic Embedding Mining'
786	    columns:
787	    - Encoder
788	    - Static R@1 (%)
789	    - Dynamic R@1 (%)
790	    - Δ (pp)
791	    - p-value
792	    rows:
793	    - - Qwen
794	      - 56.5
795	      - 56.8
796	      - '+0.3'
797	      - 0.41
798	    - - StarCoder
799	      - 47.5
800	      - 47.7
801	      - '+0.2'
802	      - 0.53
803	  figures_description:
804	  - 'Fig S6: Learning curves for static vs dynamic mining, overlaid'
805	  analysis: 'Static ≈ dynamic 是 clean negative result，强化了论文 narrative：关键是 negative
806	    的 semantic quality（embedding vs random vs dataflow），不是 freshness。 也简化了 practitioner
807	    recommendation——mine once from pretrained, no need for per-epoch re-mining。
808	
809	    '
810	- name: Bootstrap CIs for SWE-bench Lite Resolve Rate
811	  plan_id: plan_016
812	  description: '对 plan_003 的 SWE-bench 结果计算 10K bootstrap resamples 的 95% CI， 报告 paired
813	    difference CIs 和 p-values。
814	
815	    '
816	  expected_results:
817	    embedding_minus_random:
818	      delta_pp: 2.5
819	      ci_95:
820	      - 0.7
821	      - 4.3
822	      p_value: 0.018
823	      significant: true
824	    dataflow_minus_random:
825	      delta_pp: 3.2
826	      ci_95:
827	      - 1.0
828	      - 5.5
829	      p_value: 0.008
830	      significant: true
831	    dataflow_minus_embedding:
832	      delta_pp: 0.7
833	      ci_95:
834	      - -1.5
835	      - 2.9
836	      p_value: 0.134
837	      significant: false
838	    bootstrap_n: 10000
839	    sample_size: 300
840	  result_rationale: 'Embedding vs random CI [0.7, 4.3] 排除零（p=0.018），确认 embedding mining
841	    在下游 任务上的统计显著提升。Dataflow vs random 更显著（p=0.008）因为 delta 更大且 SWE-bench 中 cross-module
842	    patches 对 dataflow signal 响应一致。Dataflow vs embedding 不显著 （p=0.134, CI 含零）——300
843	    instances 的 power 不足以区分 +0.7pp 的小 delta，这是 expected：retrieval level 的 ~1pp 差异在下游
844	    binary resolve 结果上被放大和噪声化。 CI 宽度 ~3.6pp 反映 300 样本的 inherent variance——SWE-bench
845	    Lite 不是为精确 delta 估计设计的 benchmark。
846	
847	    '
848	  tables:
849	  - name: 'Table 4c: SWE-bench Bootstrap Significance Tests'
850	    columns:
851	    - Comparison
852	    - Δ (pp)
853	    - 95% CI
854	    - p-value
855	    rows:
856	    - - embedding − random
857	      - '+2.5'
858	      - '[+0.7, +4.3]'
859	      - 0.018
860	    - - dataflow − random
861	      - '+3.2'
862	      - '[+1.0, +5.5]'
863	      - 0.008
864	    - - dataflow − embedding
865	      - '+0.7'
866	      - '[−1.5, +2.9]'
867	      - 0.134
868	  figures_description:
869	  - 'Fig 5c: Bootstrap distribution histograms for the 3 pairwise comparisons'
870	  analysis: 'CI 下界 > 0 for both mining strategies vs random 是 EMNLP reviewer 需要的统计保证。
871	    Dataflow vs embedding 不显著是 honest reporting 且与 Claim 2 的 "conditional" framing
872	    一致——dataflow 的额外价值不是 universally separable at SWE-bench scale。
873	
874	    '
875	- name: Inference-Time Graph Method Literature Comparison
876	  plan_id: plan_017
877	  description: '文献分析（非实验）：与 CodexGraph, LocAgent, RANGER 等 inference-time 图方法的 系统比较。已完成
878	    8 篇论文 survey。
879	
880	    '
881	  expected_results:
882	    papers_surveyed: 8
883	    key_distinction: training-time mining (ours) vs inference-time graph navigation
884	    complementarity_evidence: 'All 8 methods operate at inference time; StructFuse
885	      mines at training time. The two approaches are complementary — StructFuse improves
886	      the base retriever that graph methods navigate over.
887	
888	      '
889	    papers_list:
890	    - CodexGraph
891	    - LocAgent
892	    - RANGER
893	    - GraphCoder
894	    - ARISE
895	    - RepoGraph
896	    - CodeGRAG
897	    - CodeRAG
898	  result_rationale: '8 篇 inference-time graph 方法均在推理阶段构建/遍历代码图，而 StructFuse 在训练阶段
899	    通过 negative mining 将结构信号蒸馏进 encoder。两者正交：StructFuse 产出更好的 base retriever，inference-time
900	    方法在此基础上进一步 re-rank/navigate。无直接可比性因为 实验设置完全不同（LocAgent 用 LLM agent + tool calls，我们用
901	    embedding retrieval）。 Discussion section 应明确 "complementary, not competing" 的定位。
902	
903	    '
904	  tables:
905	  - name: 'Table S3: Comparison with Inference-Time Graph Methods'
906	    columns:
907	    - Method
908	    - Graph Stage
909	    - Graph Type
910	    - Complementary?
911	    rows:
912	    - - StructFuse (ours)
913	      - Training
914	      - Dataflow (CodeQL)
915	      - —
916	    - - CodexGraph
917	      - Inference
918	      - Code graph DB
919	      - 'Yes'
920	    - - LocAgent
921	      - Inference
922	      - Repo structure
923	      - 'Yes'
924	    - - RANGER
925	      - Inference
926	      - Call graph
927	      - 'Yes'
928	    - - ARISE
929	      - Inference
930	      - Intra-proc dataflow
931	      - Partially (intra only)
932	  figures_description: []
933	  analysis: 'Discussion 中用 2 段落即可。不要 overclaim StructFuse 优于这些方法——它们解决不同问题。 Highlight:
934	    StructFuse 是唯一在 training time 利用结构信号的方法，且不增加 inference cost。
935	
936	    '
937	- name: BM25 Negative Baseline — Closing CoCoHaNeRe Argument
938	  plan_id: plan_018
939	  description: 'BM25-based hard negatives 作为第 4 策略，1+ seed × 2 encoders。 验证 CoCoHaNeRe
940	    报告的 "embedding negatives harm" 实际是 BM25-proxy artifact。
941	
942	    '
943	  expected_results:
944	    qwen:
945	      bm25_R1: 0.52
946	      random_R1: 0.545
947	      embedding_R1: 0.565
948	      dataflow_R1: 0.555
949	      bm25_minus_random_pp: -2.5
950	      embedding_minus_bm25_pp: 4.5
951	    starcoder:
952	      bm25_R1: 0.433
953	      random_R1: 0.46
954	      embedding_R1: 0.475
955	      dataflow_R1: 0.458
956	      bm25_minus_random_pp: -2.7
957	      embedding_minus_bm25_pp: 4.2
958	    bm25_harms_both_encoders: true
959	    cocohanere_artifact_confirmed: true
960	    bm25_minus_random_avg_pp: -2.6
961	  result_rationale: 'BM25 negatives 在两个 encoder 上均 harm performance（Qwen -2.5pp, StarCoder
962	    -2.7pp vs random），直接复现了 CoCoHaNeRe 报告的负面效果方向。关键 insight：BM25 negatives 选取的是 lexically
963	    similar 但 semantically ambiguous 的文件——它们与 query 共享大量 token overlap（function names,
964	    variable names, import patterns），但这种 overlap 恰恰是 contrastive learning 需要利用来区分
965	    positive/negative 的信号。用 BM25 选的 negatives 让模型学会 ignore lexical cues，但这些 cues 在
966	    code retrieval 中是有效信号。 相比之下，true embedding distance negatives 选取的是 semantically
967	    similar（在 pretrained embedding space 中近）但与 query 不同的文件，这迫使模型学习更 fine-grained semantic
968	    distinctions。BM25 vs embedding 的 4.5pp 差距（Qwen）是论文中最大的 single pairwise comparison，构成
969	    Claim 1 correction argument 的 empirical closure。 效果幅度在 bm25_minus_random_R1_pp
970	    [-4.0, -1.5] 范围内。
971	
972	    '
973	  tables:
974	  - name: 'Table 3: Full 4-Strategy Comparison Including BM25 Baseline'
975	    columns:
976	    - Encoder
977	    - Strategy
978	    - R@1 (%)
979	    - 95% CI
980	    - Δ vs Random (pp)
981	    rows:
982	    - - Qwen
983	      - BM25
984	      - 52.0
985	      - '[51.2, 52.8]'
986	      - −2.5
987	    - - Qwen
988	      - random
989	      - 54.5
990	      - '[53.8, 55.2]'
991	      - —
992	    - - Qwen
993	      - dataflow
994	      - 55.5
995	      - '[54.6, 56.4]'
996	      - '+1.0'
997	    - - Qwen
998	      - embedding
999	      - 56.5
1000	      - '[55.8, 57.2]'
1001	      - '+2.0'
1002	    - - StarCoder
1003	      - BM25
1004	      - 43.3
1005	      - '[42.3, 44.3]'
1006	      - −2.7
1007	    - - StarCoder
1008	      - random
1009	      - 46.0
1010	      - '[45.1, 46.9]'
1011	      - —
1012	    - - StarCoder
1013	      - dataflow
1014	      - 45.8
1015	      - '[44.8, 46.8]'
1016	      - −0.2
1017	    - - StarCoder
1018	      - embedding
1019	      - 47.5
1020	      - '[46.6, 48.4]'
1021	      - '+1.5'
1022	  figures_description:
1023	  - 'Fig 3: 4-strategy R@1 bar chart with BM25 highlighted in red, showing the harm
1024	    direction. Annotation arrow from BM25 to embedding with ''4.5pp gap — the CoCoHaNeRe
1025	    artifact'''
1026	  - 'Fig 4: Neg similarity distribution histograms for BM25 vs embedding vs random
1027	    vs dataflow, showing BM25 occupies a different region of similarity space'
1028	  analysis: 'BM25 baseline 是 best tier 论文的 crown jewel experiment。它将 Claim 1 从 "argumentative
1029	    correction" 升级为 "empirical demonstration"：我们不仅指出 CoCoHaNeRe 用了 BM25 proxy， 还实际运行
1030	    BM25 negatives 复现了 harm effect，然后展示 true embedding negatives 方向相反。 4-strategy
1031	    ordering BM25 < random < dataflow ≤ embedding 清晰展示了 negative mining strategy 的
1032	    quality spectrum。Reviewer 对 "correction without evidence" 的 concern 被彻底关闭。
1033	
1034	    '
1035	- name: Pool Size Sensitivity (50/100/200/500)
1036	  plan_id: plan_019
1037	  description: '在 SWE-smith validation 上用 pool={50, 100, 200, 500} 重新评估 M2 best checkpoints，
1038	    测试 strategy ranking 在更 realistic pool sizes 下的稳定性。
1039	
1040	    '
1041	  expected_results:
1042	    qwen:
1043	      pool_50:
1044	        random_R1: 0.545
1045	        embedding_R1: 0.565
1046	        dataflow_R1: 0.555
1047	        embedding_minus_random_pp: 2.0
1048	      pool_100:
1049	        random_R1: 0.428
1050	        embedding_R1: 0.447
1051	        dataflow_R1: 0.438
1052	        embedding_minus_random_pp: 1.9
1053	      pool_200:
1054	        random_R1: 0.342
1055	        embedding_R1: 0.359
1056	        dataflow_R1: 0.351
1057	        embedding_minus_random_pp: 1.7
1058	      pool_500:
1059	        random_R1: 0.261
1060	        embedding_R1: 0.276
1061	        dataflow_R1: 0.269
1062	        embedding_minus_random_pp: 1.5
1063	    starcoder:
1064	      pool_50:
1065	        random_R1: 0.46
1066	        embedding_R1: 0.475
1067	        dataflow_R1: 0.458
1068	        embedding_minus_random_pp: 1.5
1069	      pool_100:
1070	        random_R1: 0.358
1071	        embedding_R1: 0.372
1072	        dataflow_R1: 0.357
1073	        embedding_minus_random_pp: 1.4
1074	      pool_200:
1075	        random_R1: 0.282
1076	        embedding_R1: 0.295
1077	        dataflow_R1: 0.281
1078	        embedding_minus_random_pp: 1.3
1079	      pool_500:
1080	        random_R1: 0.214
1081	        embedding_R1: 0.225
1082	        dataflow_R1: 0.213
1083	        embedding_minus_random_pp: 1.1
1084	    ranking_stable_across_pools: true
1085	    pool_ranking_stable_pct: 100
1086	    delta_shrinkage_rate: ~0.15pp per doubling of pool size
1087	  result_rationale: 'Strategy ranking（embedding > dataflow > random for Qwen; embedding
1088	    > random ≈ dataflow for StarCoder）在 pool 50→500 全程保持稳定（pool_ranking_stable_pct
1089	    = 100%）。 绝对 R@1 随 pool 增大而下降（50→500 约 halved），因为 larger pool = more distractors
1090	    = harder task。Embedding-random delta 从 2.0pp (pool=50) 缓慢缩小至 1.5pp (pool=500)，
1091	    缩小幅度约 25%，但方向和显著性保持。原因：pool=500 时 random negatives 中偶然出现 "hard" negative 的概率增加（base
1092	    rate effect），部分缩小了 mining 策略的差异。 但核心 signal 不消失——embedding mining 在 pool=500 仍有
1093	    +1.5pp Qwen, +1.1pp StarCoder。 Dataflow 在 Qwen 上从 +1.0pp (pool=50) 降至 +0.8pp (pool=500)
1094	    但保持正值。 这直接回应 reviewer "pool=50 unrealistically small" concern：即使 10x pool 扩大，
1095	    strategy ranking 完全不翻转。
1096	
1097	    '
1098	  tables:
1099	  - name: 'Table 12: Pool Size Sensitivity (R@1 %)'
1100	    columns:
1101	    - Pool
1102	    - Encoder
1103	    - random
1104	    - embedding
1105	    - dataflow
1106	    - emb−rand (pp)
1107	    - Ranking
1108	    rows:
1109	    - - 50
1110	      - Qwen
1111	      - 54.5
1112	      - 56.5
1113	      - 55.5
1114	      - '+2.0'
1115	      - E>D>R
1116	    - - 100
1117	      - Qwen
1118	      - 42.8
1119	      - 44.7
1120	      - 43.8
1121	      - '+1.9'
1122	      - E>D>R
1123	    - - 200
1124	      - Qwen
1125	      - 34.2
1126	      - 35.9
1127	      - 35.1
1128	      - '+1.7'
1129	      - E>D>R
1130	    - - 500
1131	      - Qwen
1132	      - 26.1
1133	      - 27.6
1134	      - 26.9
1135	      - '+1.5'
1136	      - E>D>R
1137	    - - 50
1138	      - StarCoder
1139	      - 46.0
1140	      - 47.5
1141	      - 45.8
1142	      - '+1.5'
1143	      - E>R>D
1144	    - - 100
1145	      - StarCoder
1146	      - 35.8
1147	      - 37.2
1148	      - 35.7
1149	      - '+1.4'
1150	      - E>R>D
1151	    - - 200
1152	      - StarCoder
1153	      - 28.2
1154	      - 29.5
1155	      - 28.1
1156	      - '+1.3'
1157	      - E>R≈D
1158	    - - 500
1159	      - StarCoder
1160	      - 21.4
1161	      - 22.5
1162	      - 21.3
1163	      - '+1.1'
1164	      - E>R≈D
1165	  figures_description:
1166	  - 'Fig 10: Pool size (x-axis, log scale) vs R@1 (y-axis) for 3 strategies, separate
1167	    panels for Qwen and StarCoder. Shaded bands between embedding and random lines
1168	    highlight persistent delta.'
1169	  - 'Fig 10b: Delta (embedding − random) vs pool size, showing graceful degradation'
1170	  analysis: Pool size sensitivity 是外部有效性的关键证据。100% ranking stability 在 50→500 全程保持是
1171	    best tier 的标志。Delta 的 graceful degradation（非 collapse）说明 mining strategy 的价值是
1172	    robust 的。论文可以明确声明："Strategy rankings are stable across pool sizes spanning an
1173	    order of magnitude (50–500), with embedding mining maintaining a statistically
1174	    significant advantage even at the largest pool tested."
1175	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fce96999-8a84-405e-84cf-1db0bd857861",
  "isSidechain": false,
  "promptId": "0dbd644e-3638-4b84-b174-ff7865af1dfb",
  "type": "user",
  "uuid": "11925cc0-1e69-40e7-979d-23db2ba19f11",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T162530/best/review_context.yaml",
      "content": "narrative_guidance: '全 18 runs（9 seeds × 2 encoders × 3 strategies）完整复现 pilot pattern。\n  Embedding mining 在两个 encoder 上均显著优于 random（Qwen +2.0pp, StarCoder +1.5pp, 95% CI\n  下界 > 0）。 Dataflow 在 Qwen 上条件性获益（+1.0pp, CI 下界 > 0），StarCoder 上无显著差异（-0.2pp, CI 含零）。\n  BM25 baseline 实证关闭 CoCoHaNeRe 论证（BM25 vs random: Qwen -2.5pp, StarCoder -2.7pp）。\n  SWE-bench Lite downstream +2.5pp embedding, +3.2pp dataflow resolve rate delta。\n  三条 claim 原样成立，EMNLP Main 强投 framing 无需调整。 M2 full anchors — Qwen random R@1=0.545,\n  embedding=0.565, dataflow=0.555; StarCoder random R@1=0.460, embedding=0.475, dataflow=0.458。\n\n  '\nimagined_experiments:\n- name: SWE-bench Lite End-to-End Evaluation\n  plan_id: plan_003\n  description: '3 strategies × best Qwen checkpoint, Qwen3.6-27B agent, 300 SWE-bench\n    Lite instances. Retriever 提供 top-k context files，agent 生成 patch，评估 resolve rate。\n\n    '\n  expected_results:\n    random_resolve_rate: 0.22\n    random_resolved_count: 66\n    embedding_resolve_rate: 0.245\n    embedding_resolved_count: 73\n    dataflow_resolve_rate: 0.252\n    dataflow_resolved_count: 76\n    embedding_minus_random_pp: 2.5\n    dataflow_minus_random_pp: 3.2\n    dataflow_minus_embedding_pp: 0.7\n    total_instances: 300\n    retriever_top_k: 5\n    agent_model: Qwen3.6-27B\n  result_rationale: 'Embedding retriever 在 SWE-bench 上提升 +2.5pp，因为 bug-fix patch 通常涉及与\n    issue 描述 语义相似但非完全匹配的文件——embedding mining 训练使 retriever 更擅长区分\"近似但无关\" 与\"近似且相关\"的文件。Dataflow\n    额外提升 +0.7pp（总 +3.2pp vs random）因为 SWE-bench patch 经常跨函数/跨模块（约 40% 涉及 caller-callee\n    关系），dataflow negatives 训练使 retriever 理解\"调用链上的文件更可能共同出现在 patch 中\"。Delta 幅度从 retrieval\n    R@1 的 +2.0/+1.0pp 放大到下游 resolve rate 的 +2.5/+3.2pp，符合检索质量在端到端任务中 的杠杆效应——正确检索一个关键文件可以使原本完全失败的\n    patch 变为可解决。 效果幅度在 swebench_resolve_rate_delta_pp [1.5, 4.0] 范围内。\n\n    '\n  tables:\n  - name: 'Table 4: SWE-bench Lite Resolve Rate'\n    columns:\n    - Strategy\n    - Resolved\n    - Total\n    - Rate (%)\n    - Δ vs Random (pp)\n    rows:\n    - - random\n      - 66\n      - 300\n      - 22.0\n      - —\n    - - embedding\n      - 73\n      - 300\n      - 24.3\n      - '+2.3'\n    - - dataflow\n      - 76\n      - 300\n      - 25.3\n      - '+3.3'\n  - name: 'Table 4b: SWE-bench by Patch Complexity'\n    columns:\n    - Patch Type\n    - N\n    - random (%)\n    - embedding (%)\n    - dataflow (%)\n    rows:\n    - - single-file\n      - 189\n      - 28.0\n      - 30.7\n      - 30.2\n    - - multi-file\n      - 111\n      - 11.7\n      - 14.4\n      - 17.1\n  figures_description:\n  - 'Fig 5: SWE-bench resolve rate bar chart (3 strategies) with bootstrap 95% CI\n    whiskers'\n  - 'Fig 5b: Scatter plot — retrieval R@1 rank vs resolve rate per instance, colored\n    by strategy'\n  analysis: 'Multi-file patches（占 37%）是 dataflow 拉开差距的主要来源：dataflow 在 multi-file 上\n    +5.4pp vs random，远大于 single-file 的 +2.2pp。这与 Claim 2 一致——dataflow negatives 使\n    retriever 更好地理解跨模块依赖。Embedding vs random 在 multi-file 上也有 +2.7pp，说明更难的 negatives\n    普遍有益。总体 resolve rate 22-25% 与 SweRank/SWE-Fixer 文献报告的 retriever-only baseline\n    一致。\n\n    '\n- name: RepoBench-R Cross-File Retrieval with Multi-Seed CIs\n  plan_id: plan_004\n  description: 'RepoBench-R test_easy (pool ~6) 和 test_hard (pool ~18) 上评估 9 seeds\n    × 3 strategies × 2 encoders，报告 R@1 均值 + 95% bootstrap CI。\n\n    '\n  expected_results:\n    qwen_test_hard:\n      random_R1_mean: 0.621\n      random_R1_ci:\n      - 0.614\n      - 0.628\n      embedding_R1_mean: 0.642\n      embedding_R1_ci:\n      - 0.634\n      - 0.65\n      dataflow_R1_mean: 0.633\n      dataflow_R1_ci:\n      - 0.624\n      - 0.642\n      embedding_minus_random_pp: 2.1\n      dataflow_minus_random_pp: 1.2\n    qwen_test_easy:\n      random_R1_mean: 0.843\n      embedding_R1_mean: 0.855\n      dataflow_R1_mean: 0.85\n      embedding_minus_random_pp: 1.2\n    starcoder_test_hard:\n      random_R1_mean: 0.574\n      random_R1_ci:\n      - 0.566\n      - 0.582\n      embedding_R1_mean: 0.589\n      embedding_R1_ci:\n      - 0.58\n      - 0.598\n      dataflow_R1_mean: 0.572\n      dataflow_R1_ci:\n      - 0.562\n      - 0.582\n      embedding_minus_random_pp: 1.5\n      dataflow_minus_random_pp: -0.2\n    starcoder_test_easy:\n      random_R1_mean: 0.812\n      embedding_R1_mean: 0.822\n      dataflow_R1_mean: 0.81\n    repobench_R1_delta_pp_embedding_avg: 1.8\n    bootstrap_CI_width_R1_pp_avg: 1.2\n  result_rationale: 'RepoBench-R 是 cross-file completion 任务，pool 更小（6-18），绝对 R@1 更高。\n    Embedding mining 在两个 encoder 上均显著提升 test_hard R@1（Qwen +2.1pp, StarCoder +1.5pp），\n    因为 pool=18 仍有足够 distractors 使 mining 质量差异体现。Test_easy pool=6 接近 ceiling，delta\n    被压缩但方向一致。Dataflow 在 Qwen test_hard 上 +1.2pp 但 CI 刚好 排除零，StarCoder 上无效（-0.2pp，CI\n    含零）——与 SWE-smith 上的 encoder-strategy interaction 完全一致，说明 pattern 跨 benchmark 稳定。CI\n    宽度 ~1.2pp 在 bootstrap_CI_width_R1_pp [0.5, 2.0] 范围内，9 seeds 提供足够统计功效。\n\n    '\n  tables:\n  - name: 'Table 5: RepoBench-R Results (test_hard, pool≈18)'\n    columns:\n    - Encoder\n    - Strategy\n    - R@1 (%)\n    - 95% CI\n    - Δ vs Random (pp)\n    rows:\n    - - Qwen\n      - random\n      - 62.1\n      - '[61.4, 62.8]'\n      - —\n    - - Qwen\n      - embedding\n      - 64.2\n      - '[63.4, 65.0]'\n      - '+2.1'\n    - - Qwen\n      - dataflow\n      - 63.3\n      - '[62.4, 64.2]'\n      - '+1.2'\n    - - StarCoder\n      - random\n      - 57.4\n      - '[56.6, 58.2]'\n      - —\n    - - StarCoder\n      - embedding\n      - 58.9\n      - '[58.0, 59.8]'\n      - '+1.5'\n    - - StarCoder\n      - dataflow\n      - 57.2\n      - '[56.2, 58.2]'\n      - −0.2\n  figures_description:\n  - 'Fig 6: RepoBench-R R@1 grouped bar chart (2 encoders × 3 strategies) with CI\n    whiskers, test_easy vs test_hard side by side'\n  analysis: 'Cross-benchmark 一致性是 best tier 的关键证据：embedding mining 在 SWE-smith 和 RepoBench-R\n    上均显著提升两个 encoder，dataflow 条件性获益仅限 Qwen。这排除了 \"结果仅限单一 benchmark\" 的 reviewer concern。Test_easy\n    上 delta 被压缩（pool=6 ceiling effect）是预期行为，反向验证了 pool size 对绝对效果幅度的调节作用。\n\n    '\n- name: Stratified Analysis with Structural Coverage & Neg Difficulty Quartiles\n  plan_id: plan_005\n  description: '5 层分层分析：repo size / pool size / query-positive similarity / structural\n    data availability (34% vs 66%) / neg_difficulty quartile。使用 M2 best checkpoints\n    在 SWE-smith validation 上重新评估。\n\n    '\n  expected_results:\n    stratum_structural_available:\n      with_dataflow_34pct:\n        qwen_dataflow_minus_random_pp: 2.8\n        qwen_dataflow_minus_embedding_pp: 1.3\n        starcoder_dataflow_minus_random_pp: 0.1\n        n_instances: ~5200\n      fallback_66pct:\n        qwen_dataflow_minus_random_pp: 0.1\n        qwen_dataflow_minus_embedding_pp: -0.2\n        starcoder_dataflow_minus_random_pp: -0.3\n        n_instances: ~10000\n    stratum_neg_difficulty_quartile:\n      Q1_easiest:\n        qwen_embedding_minus_random_pp: 0.8\n        qwen_dataflow_minus_random_pp: 0.3\n      Q2:\n        qwen_embedding_minus_random_pp: 1.5\n        qwen_dataflow_minus_random_pp: 0.7\n      Q3:\n        qwen_embedding_minus_random_pp: 2.4\n        qwen_dataflow_minus_random_pp: 1.2\n      Q4_hardest:\n        qwen_embedding_minus_random_pp: 3.2\n        qwen_dataflow_minus_random_pp: 2.1\n    stratum_repo_size:\n      small_lt50:\n        embedding_delta_pp: 2.8\n        n: ~500\n      medium_50_200:\n        embedding_delta_pp: 2.2\n        n: ~4100\n      large_200_500:\n        embedding_delta_pp: 1.8\n        n: ~5500\n      xlarge_500plus:\n        embedding_delta_pp: 1.6\n        n: ~5100\n    stratum_pool_size:\n      pool_lt20:\n        embedding_delta_pp: 1.0\n        dataflow_delta_pp: 0.3\n      pool_20_50:\n        embedding_delta_pp: 2.1\n        dataflow_delta_pp: 1.0\n      pool_gt50:\n        embedding_delta_pp: 2.5\n        dataflow_delta_pp: 1.4\n    stratum_query_pos_sim:\n      high_sim_gt095:\n        embedding_delta_pp: 2.6\n        dataflow_delta_pp: 1.8\n      medium_sim_085_095:\n        embedding_delta_pp: 1.9\n        dataflow_delta_pp: 0.8\n      low_sim_lt085:\n        embedding_delta_pp: 1.2\n        dataflow_delta_pp: 0.2\n  result_rationale: 'Structural-available stratum（34%）上 dataflow 优势放大到 +2.8pp（Qwen），因为这些\n    instance 实际接收了 dataflow-disconnected negatives——真实训练信号未被 fallback 稀释。 Fallback\n    stratum（66%）上 dataflow ≈ embedding（±0.2pp），因为 fallback 时 dataflow 策略退化为 embedding\n    或 random 选择，无结构信号注入。这一分解直接回应 reviewer 关于 \"34% coverage 稀释 signal\" 的 concern——真实\n    per-instance 效果是 +2.8pp 而非 pooled +1.0pp。Neg_difficulty Q4（最难 quartile）上 delta\n    最大（embedding +3.2pp, dataflow +2.1pp），符合 representation saturation 理论——Qwen 在高\n    pos_sim 区域最需要 harder negatives，而 Q4 恰好是 margin 最小、分辨最难的 instances。Q1（最容易）delta\n    最小 因为 random negatives 已经足够容易区分。Repo size 上 small repo delta 更大因为 小 repo 的 candidate\n    pool 更集中，mining 策略差异更容易体现。\n\n    '\n  tables:\n  - name: 'Table 7: Stratified R@1 Delta by Structural Data Availability (Qwen)'\n    columns:\n    - Stratum\n    - N\n    - random R@1\n    - embedding R@1\n    - dataflow R@1\n    - df−rand (pp)\n    rows:\n    - - With dataflow (34%)\n      - ~5.2K\n      - 53.1\n      - 55.4\n      - 55.9\n      - '+2.8'\n    - - Fallback (66%)\n      - ~10K\n      - 55.2\n      - 57.3\n      - 55.3\n      - '+0.1'\n    - - Overall\n      - ~15.2K\n      - 54.5\n      - 56.5\n      - 55.5\n      - '+1.0'\n  - name: 'Table 7b: R@1 Delta by Neg Difficulty Quartile (Qwen)'\n    columns:\n    - Quartile\n    - margin_mean\n    - emb−rand (pp)\n    - df−rand (pp)\n    rows:\n    - - Q1 (easiest)\n      - 0.142\n      - '+0.8'\n      - '+0.3'\n    - - Q2\n      - 0.078\n      - '+1.5'\n      - '+0.7'\n    - - Q3\n      - 0.031\n      - '+2.4'\n      - '+1.2'\n    - - Q4 (hardest)\n      - 0.008\n      - '+3.2'\n      - '+2.1'\n  figures_description:\n  - 'Fig 7: Heatmap — R@1 delta (strategy × stratum), separate panels for Qwen and\n    StarCoder'\n  - 'Fig 8: Neg difficulty quartile vs R@1 delta line plot, 3 strategies overlaid'\n  analysis: 'Stratified analysis 提供了论文中最强的 mechanistic 证据。Neg_difficulty Q4 的 +3.2pp\n    embedding delta 是 overall +2.0pp 的 1.6 倍——越难的 instances 从 harder negatives 获益越多，这是\n    representation saturation 理论的直接预测。Structural-available vs fallback 分解消除了 \"diluted\n    signal\" concern 并揭示 dataflow 的真实 per-instance 效果（+2.8pp）远大于 pooled 报告值。\n\n    '\n- name: Call-Graph Hop Depth Ablation (1/2/3-hop)\n  plan_id: plan_007\n  description: '比较 1-hop / 2-hop / 3-hop call-graph bounding 对 dataflow negative 质量的影响。\n    Qwen encoder, 1 seed, SWE-smith validation。\n\n    '\n  expected_results:\n    hop_1:\n      R1: 0.548\n      connected_coverage_pct: 12.4\n      negatives_per_query_mean: 18.2\n    hop_2:\n      R1: 0.555\n      connected_coverage_pct: 34.3\n      negatives_per_query_mean: 31.7\n    hop_3:\n      R1: 0.551\n      connected_coverage_pct: 58.6\n      negatives_per_query_mean: 42.1\n    optimal_hop: 2\n    hop2_minus_hop1_pp: 0.7\n    hop3_minus_hop2_pp: -0.4\n  result_rationale: '2-hop 是最优平衡点。1-hop 太保守——仅 12.4% coverage 意味着大部分 instance 没有足够的\n    connected 节点来定义 \"disconnected\" negatives，退化为 random。3-hop 过于宽松——58.6% coverage\n    下 \"disconnected\" 的定义变得太窄，许多语义相关但间接连接的文件被错误排除在 negative pool 外，引入噪声。2-hop 的 34.3%\n    coverage（与 M1 extraction 的 structural data rate 一致）在 \"enough connected nodes to\n    define meaningful disconnection\" 和 \"disconnected set still contains genuinely\n    unrelated files\" 之间取得平衡。\n\n    '\n  tables:\n  - name: 'Table 9: Hop Depth Ablation (Qwen, dataflow strategy)'\n    columns:\n    - Hops\n    - Coverage (%)\n    - Neg/query\n    - R@1 (%)\n    - Δ vs 2-hop (pp)\n    rows:\n    - - 1\n      - 12.4\n      - 18.2\n      - 54.8\n      - −0.7\n    - - 2\n      - 34.3\n      - 31.7\n      - 55.5\n      - —\n    - - 3\n      - 58.6\n      - 42.1\n      - 55.1\n      - −0.4\n  figures_description:\n  - 'Fig S1: Hop depth vs R@1 line plot with coverage % on secondary y-axis'\n  analysis: '2-hop optimal 符合 inter-procedural dataflow 的语义：1-hop = 直接 caller/callee，\n    2-hop = caller 的 caller 或 callee 的 callee（一层间接调用），3-hop 开始包含 过于间接的关系。论文可以强调 2-hop\n    选择有 principled 依据而非纯粹 empirical tuning。\n\n    '\n- name: Training Data Size Scaling (1K/3K/5K)\n  plan_id: plan_008\n  description: '固定 Qwen encoder + embedding strategy，训练数据从 1K / 3K / 5K instances\n    增长， 观察 R@1 变化和策略排名稳定性。\n\n    '\n  expected_results:\n    size_1K:\n      random_R1: 0.51\n      embedding_R1: 0.522\n      dataflow_R1: 0.515\n      embedding_minus_random_pp: 1.2\n      seed_std: 0.015\n    size_3K:\n      random_R1: 0.532\n      embedding_R1: 0.55\n      dataflow_R1: 0.541\n      embedding_minus_random_pp: 1.8\n      seed_std: 0.01\n    size_5K:\n      random_R1: 0.545\n      embedding_R1: 0.565\n      dataflow_R1: 0.555\n      embedding_minus_random_pp: 2.0\n      seed_std: 0.008\n    ranking_stable: true\n    monotonic_improvement: true\n  result_rationale: '策略排名在 1K/3K/5K 三个尺度上保持一致（embedding > dataflow > random），但 delta\n    幅度随数据量增大而增大——1K 时 +1.2pp，5K 时 +2.0pp。这是因为更大的训练集提供更多 diverse negatives，使 mining\n    策略的差异更充分地体现。1K 时 seed 方差较大（std=0.015） 因为 negative 多样性不足，个别 seed 的 negative 采样偶然性影响结果。5K\n    时方差收敛 （std=0.008），mining 策略的信号超过采样噪声。No diminishing returns at 5K suggests further\n    scaling could help, but is beyond scope。\n\n    '\n  tables:\n  - name: 'Table 10: Data Size Scaling (Qwen)'\n    columns:\n    - Size\n    - random R@1\n    - embedding R@1\n    - dataflow R@1\n    - emb−rand (pp)\n    - σ across seeds\n    rows:\n    - - 1K\n      - 51.0\n      - 52.2\n      - 51.5\n      - '+1.2'\n      - 1.5\n    - - 3K\n      - 53.2\n      - 55.0\n      - 54.1\n      - '+1.8'\n      - 1.0\n    - - 5K\n      - 54.5\n      - 56.5\n      - 55.5\n      - '+2.0'\n      - 0.8\n  figures_description:\n  - 'Fig S2: R@1 vs training size for 3 strategies, with shaded seed variance bands'\n  analysis: 'Monotonic scaling + stable ranking 表明结果不是 small-data artifact。5K 时未见\n    diminishing returns，暗示更大数据集可能进一步放大差异。这对 reviewer \"effect size marginal\" concern\n    有价值——delta 仍在增长，当前 +2.0pp 是下界而非上界。\n\n    '\n- name: Fusion Head Ablation\n  plan_id: plan_009\n  description: '比较 embedding-only / structural-features-only / combined fusion head，\n    隔离 training-time mining 价值与 inference-time feature injection。\n\n    '\n  expected_results:\n    embedding_only:\n      qwen_R1: 0.565\n      starcoder_R1: 0.475\n    structural_features_only:\n      qwen_R1: 0.498\n      starcoder_R1: 0.421\n    combined_fusion:\n      qwen_R1: 0.561\n      starcoder_R1: 0.472\n    embedding_only_minus_combined_pp: 0.4\n    conclusion: mining > fusion; structural features at inference add noise\n  result_rationale: 'Embedding-only（仅用 embedding mining 训练的 retriever，inference 时不注入结构特征）\n    表现最好或 tied with combined。Combined fusion 略低 0.4pp 因为 inference-time structural\n    features 引入了不精确的 CodeQL connectivity 信号——recall 某些 CodeQL extraction 失败的 instance\n    反而被错误降权。Structural-features-only（不用 mining 训练， 仅在 inference 注入结构特征）远低于 embedding-only（-6.7pp\n    Qwen），证明核心价值在 training-time negative mining 而非 inference-time feature engineering。\n    这一结果对 paper framing 极为重要：StructFuse 的贡献是 mining strategy，不是 fusion。\n\n    '\n  tables:\n  - name: 'Table 11: Fusion Head Ablation'\n    columns:\n    - Configuration\n    - Qwen R@1 (%)\n    - StarCoder R@1 (%)\n    rows:\n    - - embedding-only (ours)\n      - 56.5\n      - 47.5\n    - - structural-features-only\n      - 49.8\n      - 42.1\n    - - combined fusion\n      - 56.1\n      - 47.2\n  figures_description:\n  - 'Fig S3: Ablation bar chart comparing 3 fusion configurations'\n  analysis: '训练时注入 structural signal 通过 negative mining（间接信号）比 inference 时直接注入 structural\n    features（直接信号）更有效。可能原因：mining 让 encoder 自己学习结构相关的 representation，而直接注入 features\n    绕过了 encoder 的学习过程，且 CodeQL 34% coverage 意味着 66% instance 在 inference 时收到 zero-vector\n    structural features，引入 noise。\n\n    '\n- name: Dataflow-Distance Weighted vs Binary Negatives\n  plan_id: plan_010\n  description: '比较 binary connected/disconnected 与 dataflow-distance weighted negative\n    sampling。 Weighted: disconnected 且 hop-distance 更远的文件被赋予更高采样概率。\n\n    '\n  expected_results:\n    binary_qwen_R1: 0.555\n    weighted_qwen_R1: 0.558\n    binary_starcoder_R1: 0.458\n    weighted_starcoder_R1: 0.459\n    weighted_minus_binary_qwen_pp: 0.3\n    weighted_minus_binary_starcoder_pp: 0.1\n  result_rationale: 'Weighted 在 Qwen 上仅微弱提升 +0.3pp（不显著），StarCoder 上几乎无差异。 原因：binary\n    disconnected/connected 已经捕获了最关键的 structural distinction—— \"是否在调用链上\"。进一步按 hop distance\n    加权引入的额外信号被 noise 抵消：距离更远 不一定意味着更好的 negative（一个完全无关的 utility 文件可能 hop=∞ 但也是 trivial\n    negative）。 Binary 的简洁性是优势——fewer hyperparameters, same effect。\n\n    '\n  tables:\n  - name: 'Table S1: Weighted vs Binary Dataflow Negatives'\n    columns:\n    - Method\n    - Qwen R@1 (%)\n    - StarCoder R@1 (%)\n    - Δ vs Binary (pp)\n    rows:\n    - - Binary (default)\n      - 55.5\n      - 45.8\n      - —\n    - - Distance-weighted\n      - 55.8\n      - 45.9\n      - +0.3 / +0.1\n  figures_description: []\n  analysis: 'Binary is sufficient — complexity of weighted sampling not justified.\n    论文可在 ablation section 用一句话报告这一 negative result， 强化 \"simple binary structural signal\n    is the key insight\" 的 narrative。\n\n    '\n- name: SWE-bench Failure Analysis (50 cases)\n  plan_id: plan_011\n  description: '从 random retriever 的 SWE-bench 失败案例中抽样 50 个，人工分类失败原因， 标注 dataflow\n    信号是否可能帮助。\n\n    '\n  expected_results:\n    total_analyzed: 50\n    category_breakdown:\n      retrieval_failure_wrong_files: 22\n      retrieval_success_but_agent_fail: 15\n      insufficient_context_window: 7\n      test_environment_issue: 4\n      ambiguous_issue_description: 2\n    dataflow_could_help:\n      true: 14\n      partially: 5\n      false: 31\n    dataflow_help_rate: 0.28\n    key_pattern: '14/22 retrieval failures involve cross-module dependencies where\n      the gold file is a caller/callee of a retrieved-but-wrong file — dataflow connectivity\n      would directly address these.\n\n      '\n  result_rationale: '50 个失败中 22 个是 retrieval failure（检索到错误文件），其中 14 个涉及跨模块依赖—— 被检索的文件和\n    gold 文件有高文本相似度但分属不同 call chain。Dataflow negatives 训练 恰好针对这类 confound。15 个 retrieval\n    success but agent fail 说明 retrieval 不是 唯一瓶颈——agent 的 patch 生成能力也是限制因素。这为论文提供了\n    \"ceiling analysis\"： 即使 perfect retrieval，resolve rate 上限约 85%（15% 是 agent 能力限制）。\n\n    '\n  tables:\n  - name: 'Table S2: Failure Category Breakdown'\n    columns:\n    - Category\n    - Count\n    - '% of 50'\n    - Dataflow Could Help?\n    rows:\n    - - 'Retrieval: wrong files'\n      - 22\n      - 44\n      - 14/22 (64%)\n    - - Retrieval OK, agent fail\n      - 15\n      - 30\n      - N/A\n    - - Context window limit\n      - 7\n      - 14\n      - 5/7 partially\n    - - Test env issue\n      - 4\n      - 8\n      - 'No'\n    - - Ambiguous issue\n      - 2\n      - 4\n      - 'No'\n  figures_description:\n  - 'Fig S4: Sankey diagram — failure flow from retrieval stage to resolution outcome'\n  analysis: '28% of failures could benefit from dataflow signal, consistent with the\n    observed +3.2pp resolve rate improvement. The 64% rate within retrieval failures\n    confirms that cross-module dependency is the primary retrieval challenge, directly\n    supporting Claim 2''s motivation.\n\n    '\n- name: Qualitative Examples (5-10 cases)\n  plan_id: plan_012\n  description: '从 SWE-bench 和 SWE-smith 中选取 5-10 个 dataflow negatives 改变检索结果的典型案例，\n    展示 structural signal 的具体作用机制。\n\n    '\n  expected_results:\n    total_examples: 8\n    example_categories:\n      caller_callee_confusion: 3\n      utility_file_distraction: 2\n      cross_module_import_chain: 2\n      test_file_vs_source: 1\n    illustrative_example:\n      issue: django/django#12345 — QuerySet.filter() returns wrong results with nested\n        Q objects\n      random_retriever_top1: django/db/models/query.py (text match on 'filter')\n      dataflow_retriever_top1: django/db/models/sql/query.py (actual SQL generation\n        called by filter)\n      gold: django/db/models/sql/query.py\n      explanation: 'Random retriever picks query.py (contains ''filter'' method signature)\n        but the bug is in sql/query.py (the downstream SQL builder called by filter).\n        Dataflow training teaches the model that sql/query.py is structurally connected\n        to query.py via 2-hop call chain, making it a better negative for other instances,\n        which in turn improves the model''s ability to rank the actual implementation\n        file higher.\n\n        '\n  result_rationale: '8 个案例覆盖 4 个失败模式：caller-callee confusion（3 个，最常见——文本相似的 wrapper\n    函数 vs 实际实现）、utility file distraction（2 个——高文本重叠的 helper 文件干扰）、 cross-module import\n    chain（2 个——A 导入 B 导入 C，bug 在 C 但文本匹配 A）、test vs source（1 个——test file 包含几乎完整的\n    source code 复制）。这些案例具体展示了 \"lexical similarity ≠ structural relevance\" 的核心 insight。\n\n    '\n  tables: []\n  figures_description:\n  - 'Fig 9: Side-by-side retrieval ranking visualization for 3 representative cases,\n    showing file dependency graph with highlighted paths'\n  analysis: 'Qualitative examples serve as the paper''s \"aha moment\" — they make the\n    abstract representation geometry argument concrete. Reviewer-facing value: even\n    skeptics who question statistical significance can see the mechanism operating\n    on real code.\n\n    '\n- name: Temperature Ablation τ ∈ {0.05, 0.1, 0.2}\n  plan_id: plan_014\n  description: '3 temperatures × 3 strategies × 2 encoders, 1 seed each. 测试 strategy\n    ranking 是否 regime-specific。\n\n    '\n  expected_results:\n    tau_005:\n      qwen_random_R1: 0.558\n      qwen_embedding_R1: 0.577\n      qwen_dataflow_R1: 0.569\n      qwen_embedding_minus_random_pp: 1.9\n      starcoder_random_R1: 0.47\n      starcoder_embedding_R1: 0.485\n      starcoder_dataflow_R1: 0.467\n      starcoder_embedding_minus_random_pp: 1.5\n    tau_010:\n      qwen_random_R1: 0.545\n      qwen_embedding_R1: 0.565\n      qwen_dataflow_R1: 0.555\n      qwen_embedding_minus_random_pp: 2.0\n      starcoder_random_R1: 0.46\n      starcoder_embedding_R1: 0.475\n      starcoder_dataflow_R1: 0.458\n      starcoder_embedding_minus_random_pp: 1.5\n    tau_020:\n      qwen_random_R1: 0.53\n      qwen_embedding_R1: 0.546\n      qwen_dataflow_R1: 0.538\n      qwen_embedding_minus_random_pp: 1.6\n      starcoder_random_R1: 0.448\n      starcoder_embedding_R1: 0.461\n      starcoder_dataflow_R1: 0.447\n      starcoder_embedding_minus_random_pp: 1.3\n    ranking_preserved_across_tau: true\n    optimal_tau: 0.05\n  result_rationale: 'Strategy ranking（embedding > dataflow > random for Qwen; embedding\n    > random ≈ dataflow for StarCoder）在三个 temperature 下保持一致。τ=0.05 绝对性能最高因为 sharper\n    temperature 使 contrastive loss 更有效地区分相似度差异（harder gradient signal）。 τ=0.2 下所有策略性能下降且\n    delta 缩小（1.6pp vs 2.0pp），因为 softer temperature 减弱了 negative 选择质量的影响——当所有 similarity\n    被压缩到窄范围内，hard vs easy negatives 的梯度差异变小。关键结论：findings 不是 temperature-regime-specific，\n    直接回应 median reviewer 的 \"τ=0.05 unusually low\" concern。\n\n    '\n  tables:\n  - name: 'Table 8: Temperature Ablation (R@1 %)'\n    columns:\n    - τ\n    - Encoder\n    - random\n    - embedding\n    - dataflow\n    - emb−rand (pp)\n    rows:\n    - - 0.05\n      - Qwen\n      - 55.8\n      - 57.7\n      - 56.9\n      - '+1.9'\n    - - 0.05\n      - StarCoder\n      - 47.0\n      - 48.5\n      - 46.7\n      - '+1.5'\n    - - 0.1\n      - Qwen\n      - 54.5\n      - 56.5\n      - 55.5\n      - '+2.0'\n    - - 0.1\n      - StarCoder\n      - 46.0\n      - 47.5\n      - 45.8\n      - '+1.5'\n    - - 0.2\n      - Qwen\n      - 53.0\n      - 54.6\n      - 53.8\n      - '+1.6'\n    - - 0.2\n      - StarCoder\n      - 44.8\n      - 46.1\n      - 44.7\n      - '+1.3'\n  figures_description:\n  - 'Fig S5: Temperature × strategy interaction plot (R@1 on y-axis, τ on x-axis,\n    separate lines per strategy)'\n  analysis: 'Ranking stability across τ 是重要的 robustness evidence。τ=0.2 下 delta 缩小但\n    不翻转，说明 mining quality 的价值在不同 loss sharpness 下都存在。Paper 可以报告 τ=0.05 作为 alternative\n    best configuration 但选择 τ=0.1 作为 default（更常见的 literature default）。\n\n    '\n- name: Dynamic vs Static Embedding Mining\n  plan_id: plan_015\n  description: 'Dynamic: 每 epoch 重新用当前 encoder 挖 embedding negatives。 Static: 仅用 pretrained\n    encoder 挖一次（当前做法）。 Qwen + StarCoder, 1 seed each。\n\n    '\n  expected_results:\n    qwen_static_R1: 0.565\n    qwen_dynamic_R1: 0.568\n    qwen_dynamic_minus_static_pp: 0.3\n    starcoder_static_R1: 0.475\n    starcoder_dynamic_R1: 0.477\n    starcoder_dynamic_minus_static_pp: 0.2\n    dynamic_significant: false\n    curriculum_confound_ruled_out: true\n  result_rationale: 'Dynamic mining 仅微弱提升 +0.2-0.3pp（不显著），因为 LoRA rank 16 的 fine-tuning\n    只轻微改变 embedding space——pretrained encoder 的 nearest neighbors 在训练后 仍然大部分相同。这排除了\n    \"static mining 的优势来自 curriculum effect（early epochs 看到 harder negatives 然后 negatives\n    变 stale）\" 的 confound——即使更新 negatives， 效果几乎不变。对 Claim 2 很重要：说明 mining strategy\n    的选择（what to mine）比 mining schedule（when to mine）更关键。Dynamic mining 的 compute overhead（每\n    epoch 重新 encode + kNN）不 justified。\n\n    '\n  tables:\n  - name: 'Table 13: Static vs Dynamic Embedding Mining'\n    columns:\n    - Encoder\n    - Static R@1 (%)\n    - Dynamic R@1 (%)\n    - Δ (pp)\n    - p-value\n    rows:\n    - - Qwen\n      - 56.5\n      - 56.8\n      - '+0.3'\n      - 0.41\n    - - StarCoder\n      - 47.5\n      - 47.7\n      - '+0.2'\n      - 0.53\n  figures_description:\n  - 'Fig S6: Learning curves for static vs dynamic mining, overlaid'\n  analysis: 'Static ≈ dynamic 是 clean negative result，强化了论文 narrative：关键是 negative\n    的 semantic quality（embedding vs random vs dataflow），不是 freshness。 也简化了 practitioner\n    recommendation——mine once from pretrained, no need for per-epoch re-mining。\n\n    '\n- name: Bootstrap CIs for SWE-bench Lite Resolve Rate\n  plan_id: plan_016\n  description: '对 plan_003 的 SWE-bench 结果计算 10K bootstrap resamples 的 95% CI， 报告 paired\n    difference CIs 和 p-values。\n\n    '\n  expected_results:\n    embedding_minus_random:\n      delta_pp: 2.5\n      ci_95:\n      - 0.7\n      - 4.3\n      p_value: 0.018\n      significant: true\n    dataflow_minus_random:\n      delta_pp: 3.2\n      ci_95:\n      - 1.0\n      - 5.5\n      p_value: 0.008\n      significant: true\n    dataflow_minus_embedding:\n      delta_pp: 0.7\n      ci_95:\n      - -1.5\n      - 2.9\n      p_value: 0.134\n      significant: false\n    bootstrap_n: 10000\n    sample_size: 300\n  result_rationale: 'Embedding vs random CI [0.7, 4.3] 排除零（p=0.018），确认 embedding mining\n    在下游 任务上的统计显著提升。Dataflow vs random 更显著（p=0.008）因为 delta 更大且 SWE-bench 中 cross-module\n    patches 对 dataflow signal 响应一致。Dataflow vs embedding 不显著 （p=0.134, CI 含零）——300\n    instances 的 power 不足以区分 +0.7pp 的小 delta，这是 expected：retrieval level 的 ~1pp 差异在下游\n    binary resolve 结果上被放大和噪声化。 CI 宽度 ~3.6pp 反映 300 样本的 inherent variance——SWE-bench\n    Lite 不是为精确 delta 估计设计的 benchmark。\n\n    '\n  tables:\n  - name: 'Table 4c: SWE-bench Bootstrap Significance Tests'\n    columns:\n    - Comparison\n    - Δ (pp)\n    - 95% CI\n    - p-value\n    rows:\n    - - embedding − random\n      - '+2.5'\n      - '[+0.7, +4.3]'\n      - 0.018\n    - - dataflow − random\n      - '+3.2'\n      - '[+1.0, +5.5]'\n      - 0.008\n    - - dataflow − embedding\n      - '+0.7'\n      - '[−1.5, +2.9]'\n      - 0.134\n  figures_description:\n  - 'Fig 5c: Bootstrap distribution histograms for the 3 pairwise comparisons'\n  analysis: 'CI 下界 > 0 for both mining strategies vs random 是 EMNLP reviewer 需要的统计保证。\n    Dataflow vs embedding 不显著是 honest reporting 且与 Claim 2 的 \"conditional\" framing\n    一致——dataflow 的额外价值不是 universally separable at SWE-bench scale。\n\n    '\n- name: Inference-Time Graph Method Literature Comparison\n  plan_id: plan_017\n  description: '文献分析（非实验）：与 CodexGraph, LocAgent, RANGER 等 inference-time 图方法的 系统比较。已完成\n    8 篇论文 survey。\n\n    '\n  expected_results:\n    papers_surveyed: 8\n    key_distinction: training-time mining (ours) vs inference-time graph navigation\n    complementarity_evidence: 'All 8 methods operate at inference time; StructFuse\n      mines at training time. The two approaches are complementary — StructFuse improves\n      the base retriever that graph methods navigate over.\n\n      '\n    papers_list:\n    - CodexGraph\n    - LocAgent\n    - RANGER\n    - GraphCoder\n    - ARISE\n    - RepoGraph\n    - CodeGRAG\n    - CodeRAG\n  result_rationale: '8 篇 inference-time graph 方法均在推理阶段构建/遍历代码图，而 StructFuse 在训练阶段\n    通过 negative mining 将结构信号蒸馏进 encoder。两者正交：StructFuse 产出更好的 base retriever，inference-time\n    方法在此基础上进一步 re-rank/navigate。无直接可比性因为 实验设置完全不同（LocAgent 用 LLM agent + tool calls，我们用\n    embedding retrieval）。 Discussion section 应明确 \"complementary, not competing\" 的定位。\n\n    '\n  tables:\n  - name: 'Table S3: Comparison with Inference-Time Graph Methods'\n    columns:\n    - Method\n    - Graph Stage\n    - Graph Type\n    - Complementary?\n    rows:\n    - - StructFuse (ours)\n      - Training\n      - Dataflow (CodeQL)\n      - —\n    - - CodexGraph\n      - Inference\n      - Code graph DB\n      - 'Yes'\n    - - LocAgent\n      - Inference\n      - Repo structure\n      - 'Yes'\n    - - RANGER\n      - Inference\n      - Call graph\n      - 'Yes'\n    - - ARISE\n      - Inference\n      - Intra-proc dataflow\n      - Partially (intra only)\n  figures_description: []\n  analysis: 'Discussion 中用 2 段落即可。不要 overclaim StructFuse 优于这些方法——它们解决不同问题。 Highlight:\n    StructFuse 是唯一在 training time 利用结构信号的方法，且不增加 inference cost。\n\n    '\n- name: BM25 Negative Baseline — Closing CoCoHaNeRe Argument\n  plan_id: plan_018\n  description: 'BM25-based hard negatives 作为第 4 策略，1+ seed × 2 encoders。 验证 CoCoHaNeRe\n    报告的 \"embedding negatives harm\" 实际是 BM25-proxy artifact。\n\n    '\n  expected_results:\n    qwen:\n      bm25_R1: 0.52\n      random_R1: 0.545\n      embedding_R1: 0.565\n      dataflow_R1: 0.555\n      bm25_minus_random_pp: -2.5\n      embedding_minus_bm25_pp: 4.5\n    starcoder:\n      bm25_R1: 0.433\n      random_R1: 0.46\n      embedding_R1: 0.475\n      dataflow_R1: 0.458\n      bm25_minus_random_pp: -2.7\n      embedding_minus_bm25_pp: 4.2\n    bm25_harms_both_encoders: true\n    cocohanere_artifact_confirmed: true\n    bm25_minus_random_avg_pp: -2.6\n  result_rationale: 'BM25 negatives 在两个 encoder 上均 harm performance（Qwen -2.5pp, StarCoder\n    -2.7pp vs random），直接复现了 CoCoHaNeRe 报告的负面效果方向。关键 insight：BM25 negatives 选取的是 lexically\n    similar 但 semantically ambiguous 的文件——它们与 query 共享大量 token overlap（function names,\n    variable names, import patterns），但这种 overlap 恰恰是 contrastive learning 需要利用来区分\n    positive/negative 的信号。用 BM25 选的 negatives 让模型学会 ignore lexical cues，但这些 cues 在\n    code retrieval 中是有效信号。 相比之下，true embedding distance negatives 选取的是 semantically\n    similar（在 pretrained embedding space 中近）但与 query 不同的文件，这迫使模型学习更 fine-grained semantic\n    distinctions。BM25 vs embedding 的 4.5pp 差距（Qwen）是论文中最大的 single pairwise comparison，构成\n    Claim 1 correction argument 的 empirical closure。 效果幅度在 bm25_minus_random_R1_pp\n    [-4.0, -1.5] 范围内。\n\n    '\n  tables:\n  - name: 'Table 3: Full 4-Strategy Comparison Including BM25 Baseline'\n    columns:\n    - Encoder\n    - Strategy\n    - R@1 (%)\n    - 95% CI\n    - Δ vs Random (pp)\n    rows:\n    - - Qwen\n      - BM25\n      - 52.0\n      - '[51.2, 52.8]'\n      - −2.5\n    - - Qwen\n      - random\n      - 54.5\n      - '[53.8, 55.2]'\n      - —\n    - - Qwen\n      - dataflow\n      - 55.5\n      - '[54.6, 56.4]'\n      - '+1.0'\n    - - Qwen\n      - embedding\n      - 56.5\n      - '[55.8, 57.2]'\n      - '+2.0'\n    - - StarCoder\n      - BM25\n      - 43.3\n      - '[42.3, 44.3]'\n      - −2.7\n    - - StarCoder\n      - random\n      - 46.0\n      - '[45.1, 46.9]'\n      - —\n    - - StarCoder\n      - dataflow\n      - 45.8\n      - '[44.8, 46.8]'\n      - −0.2\n    - - StarCoder\n      - embedding\n      - 47.5\n      - '[46.6, 48.4]'\n      - '+1.5'\n  figures_description:\n  - 'Fig 3: 4-strategy R@1 bar chart with BM25 highlighted in red, showing the harm\n    direction. Annotation arrow from BM25 to embedding with ''4.5pp gap — the CoCoHaNeRe\n    artifact'''\n  - 'Fig 4: Neg similarity distribution histograms for BM25 vs embedding vs random\n    vs dataflow, showing BM25 occupies a different region of similarity space'\n  analysis: 'BM25 baseline 是 best tier 论文的 crown jewel experiment。它将 Claim 1 从 \"argumentative\n    correction\" 升级为 \"empirical demonstration\"：我们不仅指出 CoCoHaNeRe 用了 BM25 proxy， 还实际运行\n    BM25 negatives 复现了 harm effect，然后展示 true embedding negatives 方向相反。 4-strategy\n    ordering BM25 < random < dataflow ≤ embedding 清晰展示了 negative mining strategy 的\n    quality spectrum。Reviewer 对 \"correction without evidence\" 的 concern 被彻底关闭。\n\n    '\n- name: Pool Size Sensitivity (50/100/200/500)\n  plan_id: plan_019\n  description: '在 SWE-smith validation 上用 pool={50, 100, 200, 500} 重新评估 M2 best checkpoints，\n    测试 strategy ranking 在更 realistic pool sizes 下的稳定性。\n\n    '\n  expected_results:\n    qwen:\n      pool_50:\n        random_R1: 0.545\n        embedding_R1: 0.565\n        dataflow_R1: 0.555\n        embedding_minus_random_pp: 2.0\n      pool_100:\n        random_R1: 0.428\n        embedding_R1: 0.447\n        dataflow_R1: 0.438\n        embedding_minus_random_pp: 1.9\n      pool_200:\n        random_R1: 0.342\n        embedding_R1: 0.359\n        dataflow_R1: 0.351\n        embedding_minus_random_pp: 1.7\n      pool_500:\n        random_R1: 0.261\n        embedding_R1: 0.276\n        dataflow_R1: 0.269\n        embedding_minus_random_pp: 1.5\n    starcoder:\n      pool_50:\n        random_R1: 0.46\n        embedding_R1: 0.475\n        dataflow_R1: 0.458\n        embedding_minus_random_pp: 1.5\n      pool_100:\n        random_R1: 0.358\n        embedding_R1: 0.372\n        dataflow_R1: 0.357\n        embedding_minus_random_pp: 1.4\n      pool_200:\n        random_R1: 0.282\n        embedding_R1: 0.295\n        dataflow_R1: 0.281\n        embedding_minus_random_pp: 1.3\n      pool_500:\n        random_R1: 0.214\n        embedding_R1: 0.225\n        dataflow_R1: 0.213\n        embedding_minus_random_pp: 1.1\n    ranking_stable_across_pools: true\n    pool_ranking_stable_pct: 100\n    delta_shrinkage_rate: ~0.15pp per doubling of pool size\n  result_rationale: 'Strategy ranking（embedding > dataflow > random for Qwen; embedding\n    > random ≈ dataflow for StarCoder）在 pool 50→500 全程保持稳定（pool_ranking_stable_pct\n    = 100%）。 绝对 R@1 随 pool 增大而下降（50→500 约 halved），因为 larger pool = more distractors\n    = harder task。Embedding-random delta 从 2.0pp (pool=50) 缓慢缩小至 1.5pp (pool=500)，\n    缩小幅度约 25%，但方向和显著性保持。原因：pool=500 时 random negatives 中偶然出现 \"hard\" negative 的概率增加（base\n    rate effect），部分缩小了 mining 策略的差异。 但核心 signal 不消失——embedding mining 在 pool=500 仍有\n    +1.5pp Qwen, +1.1pp StarCoder。 Dataflow 在 Qwen 上从 +1.0pp (pool=50) 降至 +0.8pp (pool=500)\n    但保持正值。 这直接回应 reviewer \"pool=50 unrealistically small\" concern：即使 10x pool 扩大，\n    strategy ranking 完全不翻转。\n\n    '\n  tables:\n  - name: 'Table 12: Pool Size Sensitivity (R@1 %)'\n    columns:\n    - Pool\n    - Encoder\n    - random\n    - embedding\n    - dataflow\n    - emb−rand (pp)\n    - Ranking\n    rows:\n    - - 50\n      - Qwen\n      - 54.5\n      - 56.5\n      - 55.5\n      - '+2.0'\n      - E>D>R\n    - - 100\n      - Qwen\n      - 42.8\n      - 44.7\n      - 43.8\n      - '+1.9'\n      - E>D>R\n    - - 200\n      - Qwen\n      - 34.2\n      - 35.9\n      - 35.1\n      - '+1.7'\n      - E>D>R\n    - - 500\n      - Qwen\n      - 26.1\n      - 27.6\n      - 26.9\n      - '+1.5'\n      - E>D>R\n    - - 50\n      - StarCoder\n      - 46.0\n      - 47.5\n      - 45.8\n      - '+1.5'\n      - E>R>D\n    - - 100\n      - StarCoder\n      - 35.8\n      - 37.2\n      - 35.7\n      - '+1.4'\n      - E>R>D\n    - - 200\n      - StarCoder\n      - 28.2\n      - 29.5\n      - 28.1\n      - '+1.3'\n      - E>R≈D\n    - - 500\n      - StarCoder\n      - 21.4\n      - 22.5\n      - 21.3\n      - '+1.1'\n      - E>R≈D\n  figures_description:\n  - 'Fig 10: Pool size (x-axis, log scale) vs R@1 (y-axis) for 3 strategies, separate\n    panels for Qwen and StarCoder. Shaded bands between embedding and random lines\n    highlight persistent delta.'\n  - 'Fig 10b: Delta (embedding − random) vs pool size, showing graceful degradation'\n  analysis: Pool size sensitivity 是外部有效性的关键证据。100% ranking stability 在 50→500 全程保持是\n    best tier 的标志。Delta 的 graceful degradation（非 collapse）说明 mining strategy 的价值是\n    robust 的。论文可以明确声明：\"Strategy rankings are stable across pool sizes spanning an\n    order of magnitude (50–500), with embedding mining maintaining a statistically\n    significant advantage even at the largest pool tested.\"\n",
      "numLines": 1175,
      "startLine": 1,
      "totalLines": 1175
    }
  },
  "sourceToolAssistantUUID": "fce96999-8a84-405e-84cf-1db0bd857861",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "ef1befa8-2efd-49dd-aab6-f69049f8448e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 14_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[DREAM Review Director] dream_id=20260514T162530 | review_mode=full | review_visible=True PDF: /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream…",
  "leafUuid": "11925cc0-1e69-40e7-979d-23db2ba19f11",
  "sessionId": "ef1befa8-2efd-49dd-aab6-f69049f8448e"
}
```

---

### Runtime record

_source line 15_

```json
{
  "type": "ai-title",
  "aiTitle": "Review ML research paper with full evaluation",
  "sessionId": "ef1befa8-2efd-49dd-aab6-f69049f8448e"
}
```

---

### Assistant

_source line 16 · 2026-05-14T16:58:49.393Z_

<details><summary>Logged reasoning block</summary>

```text
Now let me read the PDF in sections.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "11925cc0-1e69-40e7-979d-23db2ba19f11",
  "isSidechain": false,
  "requestId": "req_011Cb2pKtAjfRQi8XncwqZVF",
  "type": "assistant",
  "uuid": "4e8ce570-acde-4270-a7b5-e95cbaa3861d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "ef1befa8-2efd-49dd-aab6-f69049f8448e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Un4WnbxxrKBXxGJQRpKQYr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18371,
      "cache_read_input_tokens": 22923,
      "output_tokens": 267,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 18371,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 267,
          "cache_read_input_tokens": 22923,
          "cache_creation_input_tokens": 18371,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 18371
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

_source line 17 · 2026-05-14T16:58:49.836Z_

读取论文 PDF。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4e8ce570-acde-4270-a7b5-e95cbaa3861d",
  "isSidechain": false,
  "requestId": "req_011Cb2pKtAjfRQi8XncwqZVF",
  "type": "assistant",
  "uuid": "c8049e8e-a38e-4f19-848a-d19200d97fc2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "ef1befa8-2efd-49dd-aab6-f69049f8448e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Un4WnbxxrKBXxGJQRpKQYr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18371,
      "cache_read_input_tokens": 22923,
      "output_tokens": 267,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 18371,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 267,
          "cache_read_input_tokens": 22923,
          "cache_creation_input_tokens": 18371,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 18371
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

_source line 18 · 2026-05-14T16:58:52.726Z_

<details open><summary>🔧 Tool call — Read · `toolu_01DCPisAgsqUYqxPg1jMdLmC`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T162530/best/review_input_db82206b.pdf",
  "pages": "1-5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c8049e8e-a38e-4f19-848a-d19200d97fc2",
  "isSidechain": false,
  "requestId": "req_011Cb2pKtAjfRQi8XncwqZVF",
  "type": "assistant",
  "uuid": "6d52db30-e484-4a52-95fa-d6ce981676ca",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "ef1befa8-2efd-49dd-aab6-f69049f8448e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Un4WnbxxrKBXxGJQRpKQYr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18371,
      "cache_read_input_tokens": 22923,
      "output_tokens": 267,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 18371,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 267,
          "cache_read_input_tokens": 22923,
          "cache_creation_input_tokens": 18371,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 18371
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

_source line 19 · 2026-05-14T16:58:52.938Z_

<details><summary>↩ Tool result · `toolu_01DCPisAgsqUYqxPg1jMdLmC`</summary>

```text
PDF pages extracted: 5 page(s) from /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T162530/best/review_input_db82206b.pdf (235.3KB)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6d52db30-e484-4a52-95fa-d6ce981676ca",
  "isSidechain": false,
  "promptId": "0dbd644e-3638-4b84-b174-ff7865af1dfb",
  "type": "user",
  "uuid": "497d7822-bc4f-4c39-8fd4-beed124f475a",
  "toolUseResult": {
    "type": "parts",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T162530/best/review_input_db82206b.pdf",
      "originalSize": 240920,
      "outputDir": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-5-projects-structfuse-context/ef1befa8-2efd-49dd-aab6-f69049f8448e/tool-results/pdf-9512b507-f84d-40c0-901c-4bf979e5a7fb",
      "count": 5
    }
  },
  "sourceToolAssistantUUID": "6d52db30-e484-4a52-95fa-d6ce981676ca",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "ef1befa8-2efd-49dd-aab6-f69049f8448e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

## Round 2

3 recorded events

### User

_source line 20 · 2026-05-14T16:58:52.936Z_

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
  "parentUuid": "497d7822-bc4f-4c39-8fd4-beed124f475a",
  "isSidechain": false,
  "promptId": "0dbd644e-3638-4b84-b174-ff7865af1dfb",
  "type": "user",
  "isMeta": true,
  "uuid": "2383ea66-b620-4d4a-a196-50b0388c8920",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "ef1befa8-2efd-49dd-aab6-f69049f8448e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-14T16:58:53.225Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Gdj5gsXwYAetfXf9kuDFvv`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T162530/best/review_input_db82206b.pdf",
  "pages": "6-11"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2383ea66-b620-4d4a-a196-50b0388c8920",
  "isSidechain": false,
  "requestId": "req_011Cb2pKtAjfRQi8XncwqZVF",
  "type": "assistant",
  "uuid": "5c2f13d8-9899-47a4-b77a-c353060ee607",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "ef1befa8-2efd-49dd-aab6-f69049f8448e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Un4WnbxxrKBXxGJQRpKQYr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18371,
      "cache_read_input_tokens": 22923,
      "output_tokens": 267,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 18371,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 267,
          "cache_read_input_tokens": 22923,
          "cache_creation_input_tokens": 18371,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 18371
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

_source line 22 · 2026-05-14T16:58:53.398Z_

<details><summary>↩ Tool result · `toolu_01Gdj5gsXwYAetfXf9kuDFvv`</summary>

```text
PDF pages extracted: 6 page(s) from /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T162530/best/review_input_db82206b.pdf (235.3KB)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5c2f13d8-9899-47a4-b77a-c353060ee607",
  "isSidechain": false,
  "promptId": "0dbd644e-3638-4b84-b174-ff7865af1dfb",
  "type": "user",
  "uuid": "7479a812-f696-41e8-ad1a-b582ab258e1f",
  "toolUseResult": {
    "type": "parts",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T162530/best/review_input_db82206b.pdf",
      "originalSize": 240920,
      "outputDir": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-5-projects-structfuse-context/ef1befa8-2efd-49dd-aab6-f69049f8448e/tool-results/pdf-a5e5ac9e-5cb6-41d5-961b-263fbd51c7ca",
      "count": 6
    }
  },
  "sourceToolAssistantUUID": "5c2f13d8-9899-47a4-b77a-c353060ee607",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "ef1befa8-2efd-49dd-aab6-f69049f8448e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

## Round 3

38 recorded events

### User

_source line 23 · 2026-05-14T16:58:53.396Z_

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
  "parentUuid": "7479a812-f696-41e8-ad1a-b582ab258e1f",
  "isSidechain": false,
  "promptId": "0dbd644e-3638-4b84-b174-ff7865af1dfb",
  "type": "user",
  "isMeta": true,
  "uuid": "edaf121c-9487-46cb-a7ef-be8de8557c95",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "ef1befa8-2efd-49dd-aab6-f69049f8448e",
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
  "lastPrompt": "[DREAM Review Director] dream_id=20260514T162530 | review_mode=full | review_visible=True PDF: /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream…",
  "leafUuid": "7479a812-f696-41e8-ad1a-b582ab258e1f",
  "sessionId": "ef1befa8-2efd-49dd-aab6-f69049f8448e"
}
```

---

### Runtime record

_source line 25_

```json
{
  "type": "ai-title",
  "aiTitle": "Review ML research paper with full evaluation",
  "sessionId": "ef1befa8-2efd-49dd-aab6-f69049f8448e"
}
```

---

### Assistant

_source line 26 · 2026-05-14T16:59:14.627Z_

<details><summary>Logged reasoning block</summary>

```text
I've now read the full paper and the review context YAML. Let me organize my understanding before dispatching the two reviewers.

**Paper Summary:**
- Title: "What Makes Hard Negatives Work for Code Retrieval? A Systematic Study of Mining Strategies and Representation Geometry"
- Core contribution: Systematic comparison of 4 negative mining strategies (random, BM25, embedding-distance, dataflow/structure-grounded) for contrastive code retrieval training
- 3 claims: (1) True embedding mining helps (correcting CoCoHaNeRe), (2) Dataflow negatives conditionally help when encoder is saturated, (3) Mechanistic explanation via representation geometry


- Experiments: SWE-smith (main), SWE-bench Lite (downstream), RepoBench-R (cross-benchmark), extensive ablations

Now I'm checking the review context YAML against what's actually in the paper. The imagined experiments list 13 planned studies, and I can see several are present: SWE-bench Lite end-to-end evaluation appears in Tables 2-4, RepoBench-R cross-file results in Table 5, and stratified analysis across Tables 6-7. I need to track which planned experiments made it into the final submission and which didn't. I've confirmed all 15 experiments are accounted for in the paper with strong coverage. Now I'm setting up the review process with two parallel reviewers—one focusing on methods and experiments, the other on novelty and related work—then running them through the full roundtable discussion to converge on final assessments.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "edaf121c-9487-46cb-a7ef-be8de8557c95",
  "isSidechain": false,
  "requestId": "req_011Cb2pLM31TtdigKchaEtzy",
  "type": "assistant",
  "uuid": "3ee8fe01-3aef-4fa8-8a47-1c4735e950a8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "ef1befa8-2efd-49dd-aab6-f69049f8448e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DcNEbByZNy7XsuCoFZoMMg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14146,
      "cache_read_input_tokens": 41294,
      "output_tokens": 3334,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14146,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 3334,
          "cache_read_input_tokens": 41294,
          "cache_creation_input_tokens": 14146,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14146
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

_source line 27 · 2026-05-14T16:59:14.975Z_

论文和实验设计已读完。所有 15 个想象实验均已覆盖。现在派发两位 Reviewer 进行独立盲审。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3ee8fe01-3aef-4fa8-8a47-1c4735e950a8",
  "isSidechain": false,
  "requestId": "req_011Cb2pLM31TtdigKchaEtzy",
  "type": "assistant",
  "uuid": "4eaf93af-d597-4fbf-b316-006a4da89d47",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "ef1befa8-2efd-49dd-aab6-f69049f8448e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DcNEbByZNy7XsuCoFZoMMg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14146,
      "cache_read_input_tokens": 41294,
      "output_tokens": 3334,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14146,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 3334,
          "cache_read_input_tokens": 41294,
          "cache_creation_input_tokens": 14146,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14146
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

_source line 28 · 2026-05-14T16:59:47.922Z_

<details open><summary>🔧 Tool call — Agent · `toolu_0173ChWZFKfkzx686zBjgLNV`</summary>

````json
{
  "description": "R1: Methods + Experiments review",
  "prompt": "You are **Reviewer 1 (R1)** in a peer review of a machine learning paper. Your assigned focus areas are **Methods** and **Experiments**. You are reviewing for a top ML venue (acceptance rate ~25%), using a 6-point scale: 1=Strong Reject, 2=Reject, 3=Weak Reject, 4=Weak Accept, 5=Accept, 6=Strong Accept.\n\n## Paper Summary\n\n**Title:** \"What Makes Hard Negatives Work for Code Retrieval? A Systematic Study of Mining Strategies and Representation Geometry\"\n\n**Core idea:** Systematic comparison of 4 negative mining strategies for contrastive code retrieval: random, BM25, true embedding-distance, and structure-grounded (dataflow via CodeQL inter-procedural call graphs). Trained on two 3B decoder-only encoders (Qwen2.5-Coder-3B, StarCoder2-3B) with LoRA rank 16, 9 seeds each, InfoNCE loss.\n\n**Three claims:**\n1. True embedding-distance mining *consistently improves* retrieval (+2.0pp Qwen, +1.5pp StarCoder R@1), correcting CoCoHaNeRe's misconception that embedding negatives harm code retrieval (CoCoHaNeRe used BM25 proxy mislabeled as embedding-distance).\n2. Structure-grounded (dataflow) negatives provide *conditional* benefit: +1.0pp on Qwen (saturated representation, pos_sim=0.9855) but -0.2pp on StarCoder (healthy separation, pos_sim=0.7985). Stratified analysis shows true per-instance effect is +2.8pp on instances with structural data (34%), diluted by 66% fallback.\n3. Mechanistic explanation via representation geometry: negative difficulty quartile analysis shows monotonic improvement scaling (Q4 hardest: +3.2pp embedding delta vs Q1 easiest: +0.8pp).\n\n## Key Experimental Results\n\n**Main results (Table 1, SWE-smith validation, pool=50, 9-seed mean ± 95% CI):**\n- Ordering: BM25 < random < dataflow ≤ embedding (consistent across both encoders)\n- BM25 harms: Qwen -2.5pp, StarCoder -2.7pp vs random\n- Embedding helps: Qwen +2.0pp, StarCoder +1.5pp vs random\n- Dataflow: Qwen +1.0pp (CI excludes zero), StarCoder -0.2pp (CI includes zero)\n\n**SWE-bench Lite downstream (Table 2, 300 instances, Qwen3.6-27B agent):**\n- Random 22.0%, embedding 24.3% (+2.3pp), dataflow 25.3% (+3.3pp)\n- Bootstrap CIs (Table 3): embedding-random p=0.018, dataflow-random p=0.008, dataflow-embedding p=0.134\n\n**RepoBench-R (Table 5, test_hard pool≈18, 9-seed):**\n- Qwen embedding +2.1pp, dataflow +1.2pp; StarCoder embedding +1.5pp, dataflow -0.2pp\n- Cross-benchmark consistency confirmed\n\n**Stratified Analysis (Tables 6-7):**\n- Structural data available (34%): dataflow +2.8pp; Fallback (66%): +0.1pp\n- Neg difficulty quartiles: Q1 +0.8pp → Q4 +3.2pp (monotonic)\n- Repo size, pool size, query-positive similarity strata all reported\n\n**Ablations:**\n- Temperature (Table 8): τ∈{0.05,0.1,0.2}, rankings stable across all\n- Hop depth (Table 9): 2-hop optimal (34.3% coverage), 1-hop too sparse (12.4%), 3-hop too broad (58.6%)\n- Data size scaling (Table 10): 1K→3K→5K, rankings stable, delta grows\n- Fusion head (Table 11): embedding-only ≥ combined fusion > structural-features-only; core value is mining strategy not feature engineering\n- Pool size sensitivity (Table 12): 50→500, rankings 100% stable\n- Static vs dynamic mining (Table 13): negligible difference (+0.3pp/+0.2pp, not significant)\n- Weighted vs binary dataflow (Table 14): binary sufficient (+0.3/+0.1pp, not significant)\n- Failure analysis (Table 15): 50 cases, 44% retrieval failures, 64% of those involve cross-module dependencies\n\n**Limitations stated:** Only 2 decoder-only 3B encoders; 34% CodeQL coverage; SWE-bench Lite only 300 instances with single agent model.\n\n## Your Task\n\nProvide a detailed review focusing on:\n1. **Methodology soundness** — Is the experimental design rigorous? Are controls appropriate? Any confounds?\n2. **Statistical rigor** — Are the 9-seed CIs, bootstrap tests, and significance claims well-founded?\n3. **Ablation completeness** — Are the ablations sufficient to support the claims? Any missing?\n4. **Reproducibility** — Is enough detail provided to reproduce?\n5. **Weaknesses in experimental design** — What could be stronger?\n\n## Output Format\n\n```\n### R1 Review: Methods & Experiments\n\n**Summary:** (2-3 sentences)\n\n**Strengths:**\n- S1: ...\n- S2: ...\n- ...\n\n**Weaknesses:**\n- W1: ...\n- W2: ...\n- ...\n\n**Questions for Authors:**\n- Q1: ...\n- ...\n\n**Missing Experiments / Suggestions:**\n- ...\n\n**Soundness Score:** X/5\n**Overall Score:** X/6\n**Confidence:** X/5\n```\n"
}
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4eaf93af-d597-4fbf-b316-006a4da89d47",
  "isSidechain": false,
  "requestId": "req_011Cb2pLM31TtdigKchaEtzy",
  "type": "assistant",
  "uuid": "37ea87a9-e1ff-458e-820c-d51bcce54631",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "ef1befa8-2efd-49dd-aab6-f69049f8448e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DcNEbByZNy7XsuCoFZoMMg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14146,
      "cache_read_input_tokens": 41294,
      "output_tokens": 3334,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14146,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 3334,
          "cache_read_input_tokens": 41294,
          "cache_creation_input_tokens": 14146,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14146
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

_source line 29 · 2026-05-14T17:00:03.897Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01KqFxUgrzMKjo6CxzEJx7g1`</summary>

````json
{
  "description": "R2: Novelty + Related Work review",
  "prompt": "You are **Reviewer 2 (R2)** in a peer review of a machine learning paper. Your assigned focus areas are **Novelty/Significance** and **Related Work/Positioning**. You are reviewing for a top ML venue (acceptance rate ~25%), using a 6-point scale: 1=Strong Reject, 2=Reject, 3=Weak Reject, 4=Weak Accept, 5=Accept, 6=Strong Accept.\n\n## Paper Summary\n\n**Title:** \"What Makes Hard Negatives Work for Code Retrieval? A Systematic Study of Mining Strategies and Representation Geometry\"\n\n**Core idea:** Systematic comparison of 4 negative mining strategies for contrastive code retrieval: random, BM25, true embedding-distance, and structure-grounded (dataflow via CodeQL inter-procedural call graphs). Trained on two 3B decoder-only encoders (Qwen2.5-Coder-3B, StarCoder2-3B) with LoRA rank 16, 9 seeds each, InfoNCE loss.\n\n**Three claims:**\n1. True embedding-distance mining *consistently improves* retrieval (+2.0pp Qwen, +1.5pp StarCoder R@1), correcting CoCoHaNeRe's misconception that embedding negatives harm code retrieval (CoCoHaNeRe used BM25 proxy mislabeled as embedding-distance).\n2. Structure-grounded (dataflow) negatives provide *conditional* benefit: +1.0pp on Qwen (saturated representation, pos_sim=0.9855) but -0.2pp on StarCoder (healthy separation, pos_sim=0.7985). Stratified analysis shows true per-instance effect is +2.8pp on instances with structural data (34%), diluted by 66% fallback.\n3. Mechanistic explanation via representation geometry: negative difficulty quartile analysis shows monotonic improvement scaling (Q4 hardest: +3.2pp embedding delta vs Q1 easiest: +0.8pp).\n\n**Related work covered in paper:**\n- **Code Retrieval for SE:** SweRank, SWE-Fixer — contrastive retrievers trained on issue-file pairs from GitHub, rely on text-based similarity alone\n- **Hard Negative Mining:** ANCE (asynchronous index refresh), curriculum-based approaches, CoCoHaNeRe (reports embedding negatives harm code search)\n- **Graph-Based Code Understanding:** CodexGraph (code graph DB for LLM navigation), LocAgent (repo structure trees), RANGER (call graphs), ARISE (intra-procedural dataflow), GraphCodeBERT (dataflow in pretraining). All operate at inference time; StructFuse is first to inject structural signal at training time via negative mining. Table 16 provides systematic comparison.\n\n**Key contributions:**\n1. Correcting CoCoHaNeRe misconception (BM25 proxy artifact)\n2. Introducing structure-grounded negatives via inter-procedural dataflow\n3. Representation geometry analysis explaining encoder-strategy interaction\n4. Practical recommendations for practitioners\n\n**Paper structure:** 11 pages, 16 tables, multiple figures. Sections: Introduction, Related Work, Method, Experiments, Discussion, Conclusion.\n\n## Your Task\n\nProvide a detailed review focusing on:\n1. **Novelty assessment** — How novel is each of the three claimed contributions? Is it incremental or significant?\n2. **Significance** — Would this change how practitioners train code retrievers? Does it advance the field's understanding?\n3. **Related work completeness** — Are important baselines or comparisons missing? Is the positioning accurate?\n4. **Claim strength vs evidence** — Are the claims well-calibrated to the evidence?\n5. **Writing quality and presentation** — Is the paper well-organized and clearly written?\n6. **Broader impact** — Does this generalize beyond the specific setup tested?\n\n## Output Format\n\n```\n### R2 Review: Novelty & Related Work\n\n**Summary:** (2-3 sentences)\n\n**Strengths:**\n- S1: ...\n- S2: ...\n- ...\n\n**Weaknesses:**\n- W1: ...\n- W2: ...\n- ...\n\n**Questions for Authors:**\n- Q1: ...\n- ...\n\n**Novelty Score:** X/5\n**Overall Score:** X/6\n**Confidence:** X/5\n```\n"
}
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "37ea87a9-e1ff-458e-820c-d51bcce54631",
  "isSidechain": false,
  "requestId": "req_011Cb2pLM31TtdigKchaEtzy",
  "type": "assistant",
  "uuid": "34071f85-e77f-4f29-80c6-5a43c38f7505",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "ef1befa8-2efd-49dd-aab6-f69049f8448e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DcNEbByZNy7XsuCoFZoMMg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14146,
      "cache_read_input_tokens": 41294,
      "output_tokens": 3334,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14146,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 3334,
          "cache_read_input_tokens": 41294,
          "cache_creation_input_tokens": 14146,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14146
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

_source line 30 · 2026-05-14T17:02:10.558Z_

<details><summary>↩ Tool result · `toolu_0173ChWZFKfkzx686zBjgLNV`</summary>

```text


Based on my thorough examination of the paper summary, the full codebase (training scripts, mining strategies, evaluation pipelines, extraction code), the project's internal decision log (D001-D030), the paper framing document, the literature map, and the current experimental status, here is my review.

---

### R1 Review: Methods & Experiments

**Summary:** This paper presents a systematic comparison of four hard negative mining strategies (random, BM25, embedding-distance, dataflow-disconnected) for contrastive code retrieval, training two 3B decoder-only encoders with LoRA. The experimental design is ambitious and well-structured, with 9-seed replications, multiple ablations, and a mechanistic analysis via representation geometry. However, the paper suffers from several methodological concerns — most critically around the confounded dataflow mining pipeline, the low statistical power of key claims, and incomplete downstream evaluation infrastructure — that collectively weaken the strength of the conclusions.

**Strengths:**

- S1: **Unusually thorough seed replication.** 9 seeds per condition with 95% CIs is well above the community norm (typically 3-5 seeds). This is commendable and enables genuine statistical comparisons for the main R@1 claims.

- S2: **Comprehensive ablation battery.** Tables 8-15 cover temperature sensitivity, hop depth, data scaling, fusion head contribution, pool size, static vs. dynamic mining, weighted vs. binary dataflow, and failure analysis. This is a notably complete set of controls that anticipates many reviewer concerns.

- S3: **Dual-benchmark consistency.** Reporting results on both SWE-smith validation and RepoBench-R (Table 5) with consistent orderings strengthens external validity. The cross-benchmark consistency check (BM25 < random < dataflow <= embedding) is a meaningful contribution.

- S4: **Honest conditional framing of Claim 2.** Rather than overclaiming dataflow universally helps, the paper correctly frames it as conditional on encoder representation saturation (pos_sim threshold). The stratified analysis (Tables 6-7) showing +2.8pp on the 34% with structural data vs. +0.1pp on fallback is transparent.

- S5: **Mechanistic depth via negative difficulty quartile analysis.** The monotonic Q1(+0.8pp) to Q4(+3.2pp) scaling provides explanatory value beyond raw metric comparisons. This transforms the paper from a pure empirical comparison to one offering predictive insight.

- S6: **Correcting a prior methodological error.** Identifying that CoCoHaNeRe conflated BM25-proxy with true embedding-distance mining is a genuine service to the community, provided the BM25 baseline data (plan_018) fully supports the claim.

**Weaknesses:**

- W1: **Critical confound in dataflow mining — 66% fallback dilution.** The dataflow strategy has structural data for only 34% of instances; the remaining 66% fall back to random or embedding-based negatives. This means the "dataflow_aware" condition is actually a *mixture* of two strategies, and the reported +1.0pp (Qwen) and -0.2pp (StarCoder) reflect this mixture, not the pure effect of dataflow negatives. While the stratified analysis (Table 6, +2.8pp on structural subset) partially addresses this, the main table (Table 1) reports the diluted numbers as the headline, which is misleading. The paper should either (a) report stratified results as primary, or (b) run a matched comparison on only the 34% structural subset across all strategies.

- W2: **N=2 encoders is fundamentally insufficient for the interaction claim (Claim 2).** The mechanistic story — that dataflow negatives help when representations are "saturated" (pos_sim > 0.98) — is inferred from exactly two data points (Qwen: saturated, helps; StarCoder: healthy, doesn't help). This is a descriptive observation about n=2, not a validated mechanism. Any two-encoder comparison will yield *some* difference, and a post-hoc explanation can always be constructed. Without at least 4-5 encoders spanning a range of pos_sim values, the "representation saturation mediates dataflow benefit" claim has no statistical support. The paper should explicitly frame this as a hypothesis, not a finding.

- W3: **Static negative mining is a significant confound.** The code confirms negatives are mined once per epoch (line 325-332 of `train.py`), using pre-computed embeddings from the *pretrained* model, not the current training checkpoint. For the embedding_distance strategy, this means the "hard" negatives reflect the initial model's embedding space, which shifts during training. Table 13 reports "negligible difference" between static and dynamic mining (+0.3pp/+0.2pp, not significant), but this ablation may be underpowered given the small effect sizes throughout. The ANCE literature established that dynamic mining matters most in later training stages — the paper should discuss why their finding contradicts this (plausible: LoRA's limited capacity means small representation shift, or 1-2 epochs is too short for drift to matter).

- W4: **Pool size of 50 in main experiments is unrealistically small.** Real code repositories contain hundreds to thousands of files. Pool=50 inflates all recall metrics (R@10=1.0 ceiling in Table 1 analysis notes). While Table 12 shows rankings are stable at pool=500, the absolute metrics and effect sizes at pool=50 are not representative of deployment conditions. The main results should be reported at a more realistic pool size (e.g., 200 or 500).

- W5: **SWE-bench Lite evaluation (Table 2) has serious methodological gaps.** (a) Only 300 instances with a single LLM agent (Qwen3.6-27B) — confounding retrieval quality with LLM generation quality. (b) The evaluation code (`eval_swebench.py` line 364-387) contains a `run_swebench_tests` function that is explicitly a *placeholder* returning `"pending"` — raising questions about whether the reported downstream numbers used the actual SWE-bench harness or an approximation. (c) No control for LLM stochasticity (temperature=0.0 mitigates but doesn't eliminate this with different context). (d) Bootstrap CIs (Table 3) show dataflow-embedding p=0.134, meaning the downstream advantage of dataflow over embedding is not significant — yet the paper may overinterpret this.

- W6: **BM25 baseline was added late and may be incomplete.** From the project's decision log (D029-D030), the BM25 baseline was identified as the "#1 consensus gap" by internal dream review and was still in progress (plan_018). The BM25 mining code (`mine_bm25_negatives.py`) uses a simplistic whitespace+camelCase tokenizer and BM25Okapi with default parameters. If BM25 negatives turn out to be ~random rather than harmful, the entire "correcting CoCoHaNeRe" narrative collapses (the paper's own contingency plan acknowledges this). The strength of Claim 1 depends critically on BM25 performing distinctly worse than random.

- W7: **Learnable temperature complicates cross-strategy comparison.** The `StructFuseEncoder` initializes `log_temperature` as a learnable parameter (line 89 of `contrastive_model.py`: `nn.Parameter(torch.tensor(math.log(0.07)))`). If temperature is learned differently across strategies — which it likely is, since harder negatives produce different loss landscapes — then the learned temperatures become a confound. The temperature ablation (Table 8) fixes temperature but uses the same *initial* temperature; it does not report what temperatures each strategy *learns*. This should be reported.

- W8: **Positive weight by dataflow distance is under-examined.** The training code applies `pos_weight = exp(-alpha * dist)` (line 95 of `train.py`), weighting the per-sample InfoNCE loss by dataflow path distance. This means the dataflow_aware strategy differs from others in *two* ways: different negatives AND different positive weighting. The ablation set (Tables 8-15) does not isolate this factor. An ablation with uniform positive weights under the dataflow strategy would clarify whether the benefit comes from the negatives or the positive weighting.

- W9: **Checkpoint selection criterion ambiguity.** The project's internal decisions (D017, D018) explicitly flag that rankings change depending on whether checkpoints are selected by best-val-loss or best-R@1. The paper should report both and be transparent about which is used for each table. If different tables use different criteria, this is a form of cherry-picking.

**Questions for Authors:**

- Q1: What learned temperature values did each strategy converge to across the 9 seeds? If they differ systematically, this confounds the comparison.

- Q2: For the SWE-bench Lite evaluation (Table 2), was the actual SWE-bench harness used for test execution, or the placeholder shown in the codebase? Please provide the exact evaluation command.

- Q3: In the stratified analysis (Table 6), the +2.8pp for structural-available instances — is this computed on a matched set where all four strategies see the same instances, or does the "structural" stratum change across strategies?

- Q4: The embedding-distance miner uses pre-computed embeddings from the pretrained model. Did you verify that these embeddings are from the *same* pretrained checkpoint (before any LoRA training) across all seeds and strategies?

- Q5: Why is the Beniget fallback (intra-procedural only) used for 66% of instances rather than reporting a "dataflow-only" condition restricted to the 34% with CodeQL output? This would give a cleaner signal.

- Q6: The pos_weight_alpha is set to 1.0 for all strategies (line 428 of `train.py`). For the random strategy, what is `pos_dataflow_distance` set to? If it defaults to 1.0 (line 94), then `pos_weight = exp(-1.0) = 0.37` for all random samples — is this intentional?

- Q7: How were the 9 seeds selected? Were any seeds discarded for any reason (crashes, OOM, etc.)?

**Missing Experiments / Suggestions:**

- **Encoder-only models as additional baselines.** CodeBERT or GraphCodeBERT would test whether the representation saturation hypothesis holds beyond decoder-only architectures. At minimum, one encoder-only model would make the interaction claim more credible.

- **Controlled comparison on structural subset only.** Report all four strategies restricted to the 34% of instances with CodeQL structural data. This eliminates the fallback dilution confound (W1).

- **Positive weight ablation.** Run dataflow_aware with pos_weight_alpha=0 (uniform weighting) to isolate the negative mining effect from the positive weighting effect.

- **Report learned temperatures per strategy.** Simple to extract from saved checkpoints; addresses W7 at zero compute cost.

- **Larger-scale downstream evaluation.** 300 SWE-bench Lite instances with a single agent model is the minimum viable evaluation. SWE-bench Verified (500 instances) or multiple agent models would substantially strengthen Table 2.

- **Training dynamics comparison.** Plot validation loss and R@1 curves for all four strategies across training steps (not just final numbers). The project notes severe overfitting (best at step 1000 of 4242); readers need to see whether strategies differ in overfitting dynamics.

**Soundness Score:** 3/5
The core experimental design (4 strategies, 2 encoders, 9 seeds, InfoNCE) is sound, but multiple confounds (fallback dilution in dataflow, learnable temperature, positive weighting, static mining) are insufficiently controlled. The n=2 interaction claim lacks statistical grounding. The SWE-bench evaluation infrastructure appears incomplete.

**Overall Score:** 4/6 (Weak Accept)
The paper asks an important question (what makes hard negatives work for code retrieval?), provides a more systematic comparison than prior work, and offers a genuinely useful correction of the CoCoHaNeRe BM25-proxy confusion. The representation geometry analysis adds intellectual depth. However, the conditional dataflow claim rests on n=2 with confounds, the main results use an unrealistically small pool, and several ablations that would isolate key factors are missing. With revisions addressing the confounds (especially W1, W2, W7, W8) and a more complete downstream evaluation, this could be a solid empirical contribution.

**Confidence:** 4/5
I have examined the full codebase, training scripts, mining implementations, evaluation pipelines, and internal experimental records. My concerns about confounds (learnable temperature, positive weighting, static mining, fallback dilution) are grounded in the actual implementation, not speculation. The one area of lower confidence is the SWE-bench evaluation, where I cannot determine from the code alone whether the placeholder was replaced with actual harness calls in production runs.

agentId: abf4871b59eebc0f1 (use SendMessage with to: 'abf4871b59eebc0f1' to continue this agent)
&lt;usage>total_tokens: 88513
tool_uses: 22
duration_ms: 142615&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "parentUuid": "37ea87a9-e1ff-458e-820c-d51bcce54631",
  "isSidechain": false,
  "promptId": "0dbd644e-3638-4b84-b174-ff7865af1dfb",
  "type": "user",
  "uuid": "fc8785ad-7999-432b-93f1-e54cd69b302f",
  "toolUseResult": {
    "status": "completed",
    "prompt": "You are **Reviewer 1 (R1)** in a peer review of a machine learning paper. Your assigned focus areas are **Methods** and **Experiments**. You are reviewing for a top ML venue (acceptance rate ~25%), using a 6-point scale: 1=Strong Reject, 2=Reject, 3=Weak Reject, 4=Weak Accept, 5=Accept, 6=Strong Accept.\n\n## Paper Summary\n\n**Title:** \"What Makes Hard Negatives Work for Code Retrieval? A Systematic Study of Mining Strategies and Representation Geometry\"\n\n**Core idea:** Systematic comparison of 4 negative mining strategies for contrastive code retrieval: random, BM25, true embedding-distance, and structure-grounded (dataflow via CodeQL inter-procedural call graphs). Trained on two 3B decoder-only encoders (Qwen2.5-Coder-3B, StarCoder2-3B) with LoRA rank 16, 9 seeds each, InfoNCE loss.\n\n**Three claims:**\n1. True embedding-distance mining *consistently improves* retrieval (+2.0pp Qwen, +1.5pp StarCoder R@1), correcting CoCoHaNeRe's misconception that embedding negatives harm code retrieval (CoCoHaNeRe used BM25 proxy mislabeled as embedding-distance).\n2. Structure-grounded (dataflow) negatives provide *conditional* benefit: +1.0pp on Qwen (saturated representation, pos_sim=0.9855) but -0.2pp on StarCoder (healthy separation, pos_sim=0.7985). Stratified analysis shows true per-instance effect is +2.8pp on instances with structural data (34%), diluted by 66% fallback.\n3. Mechanistic explanation via representation geometry: negative difficulty quartile analysis shows monotonic improvement scaling (Q4 hardest: +3.2pp embedding delta vs Q1 easiest: +0.8pp).\n\n## Key Experimental Results\n\n**Main results (Table 1, SWE-smith validation, pool=50, 9-seed mean ± 95% CI):**\n- Ordering: BM25 < random < dataflow ≤ embedding (consistent across both encoders)\n- BM25 harms: Qwen -2.5pp, StarCoder -2.7pp vs random\n- Embedding helps: Qwen +2.0pp, StarCoder +1.5pp vs random\n- Dataflow: Qwen +1.0pp (CI excludes zero), StarCoder -0.2pp (CI includes zero)\n\n**SWE-bench Lite downstream (Table 2, 300 instances, Qwen3.6-27B agent):**\n- Random 22.0%, embedding 24.3% (+2.3pp), dataflow 25.3% (+3.3pp)\n- Bootstrap CIs (Table 3): embedding-random p=0.018, dataflow-random p=0.008, dataflow-embedding p=0.134\n\n**RepoBench-R (Table 5, test_hard pool≈18, 9-seed):**\n- Qwen embedding +2.1pp, dataflow +1.2pp; StarCoder embedding +1.5pp, dataflow -0.2pp\n- Cross-benchmark consistency confirmed\n\n**Stratified Analysis (Tables 6-7):**\n- Structural data available (34%): dataflow +2.8pp; Fallback (66%): +0.1pp\n- Neg difficulty quartiles: Q1 +0.8pp → Q4 +3.2pp (monotonic)\n- Repo size, pool size, query-positive similarity strata all reported\n\n**Ablations:**\n- Temperature (Table 8): τ∈{0.05,0.1,0.2}, rankings stable across all\n- Hop depth (Table 9): 2-hop optimal (34.3% coverage), 1-hop too sparse (12.4%), 3-hop too broad (58.6%)\n- Data size scaling (Table 10): 1K→3K→5K, rankings stable, delta grows\n- Fusion head (Table 11): embedding-only ≥ combined fusion > structural-features-only; core value is mining strategy not feature engineering\n- Pool size sensitivity (Table 12): 50→500, rankings 100% stable\n- Static vs dynamic mining (Table 13): negligible difference (+0.3pp/+0.2pp, not significant)\n- Weighted vs binary dataflow (Table 14): binary sufficient (+0.3/+0.1pp, not significant)\n- Failure analysis (Table 15): 50 cases, 44% retrieval failures, 64% of those involve cross-module dependencies\n\n**Limitations stated:** Only 2 decoder-only 3B encoders; 34% CodeQL coverage; SWE-bench Lite only 300 instances with single agent model.\n\n## Your Task\n\nProvide a detailed review focusing on:\n1. **Methodology soundness** — Is the experimental design rigorous? Are controls appropriate? Any confounds?\n2. **Statistical rigor** — Are the 9-seed CIs, bootstrap tests, and significance claims well-founded?\n3. **Ablation completeness** — Are the ablations sufficient to support the claims? Any missing?\n4. **Reproducibility** — Is enough detail provided to reproduce?\n5. **Weaknesses in experimental design** — What could be stronger?\n\n## Output Format\n\n```\n### R1 Review: Methods & Experiments\n\n**Summary:** (2-3 sentences)\n\n**Strengths:**\n- S1: ...\n- S2: ...\n- ...\n\n**Weaknesses:**\n- W1: ...\n- W2: ...\n- ...\n\n**Questions for Authors:**\n- Q1: ...\n- ...\n\n**Missing Experiments / Suggestions:**\n- ...\n\n**Soundness Score:** X/5\n**Overall Score:** X/6\n**Confidence:** X/5\n```\n",
    "agentId": "abf4871b59eebc0f1",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "\n\nBased on my thorough examination of the paper summary, the full codebase (training scripts, mining strategies, evaluation pipelines, extraction code), the project's internal decision log (D001-D030), the paper framing document, the literature map, and the current experimental status, here is my review.\n\n---\n\n### R1 Review: Methods & Experiments\n\n**Summary:** This paper presents a systematic comparison of four hard negative mining strategies (random, BM25, embedding-distance, dataflow-disconnected) for contrastive code retrieval, training two 3B decoder-only encoders with LoRA. The experimental design is ambitious and well-structured, with 9-seed replications, multiple ablations, and a mechanistic analysis via representation geometry. However, the paper suffers from several methodological concerns — most critically around the confounded dataflow mining pipeline, the low statistical power of key claims, and incomplete downstream evaluation infrastructure — that collectively weaken the strength of the conclusions.\n\n**Strengths:**\n\n- S1: **Unusually thorough seed replication.** 9 seeds per condition with 95% CIs is well above the community norm (typically 3-5 seeds). This is commendable and enables genuine statistical comparisons for the main R@1 claims.\n\n- S2: **Comprehensive ablation battery.** Tables 8-15 cover temperature sensitivity, hop depth, data scaling, fusion head contribution, pool size, static vs. dynamic mining, weighted vs. binary dataflow, and failure analysis. This is a notably complete set of controls that anticipates many reviewer concerns.\n\n- S3: **Dual-benchmark consistency.** Reporting results on both SWE-smith validation and RepoBench-R (Table 5) with consistent orderings strengthens external validity. The cross-benchmark consistency check (BM25 < random < dataflow <= embedding) is a meaningful contribution.\n\n- S4: **Honest conditional framing of Claim 2.** Rather than overclaiming dataflow universally helps, the paper correctly frames it as conditional on encoder representation saturation (pos_sim threshold). The stratified analysis (Tables 6-7) showing +2.8pp on the 34% with structural data vs. +0.1pp on fallback is transparent.\n\n- S5: **Mechanistic depth via negative difficulty quartile analysis.** The monotonic Q1(+0.8pp) to Q4(+3.2pp) scaling provides explanatory value beyond raw metric comparisons. This transforms the paper from a pure empirical comparison to one offering predictive insight.\n\n- S6: **Correcting a prior methodological error.** Identifying that CoCoHaNeRe conflated BM25-proxy with true embedding-distance mining is a genuine service to the community, provided the BM25 baseline data (plan_018) fully supports the claim.\n\n**Weaknesses:**\n\n- W1: **Critical confound in dataflow mining — 66% fallback dilution.** The dataflow strategy has structural data for only 34% of instances; the remaining 66% fall back to random or embedding-based negatives. This means the \"dataflow_aware\" condition is actually a *mixture* of two strategies, and the reported +1.0pp (Qwen) and -0.2pp (StarCoder) reflect this mixture, not the pure effect of dataflow negatives. While the stratified analysis (Table 6, +2.8pp on structural subset) partially addresses this, the main table (Table 1) reports the diluted numbers as the headline, which is misleading. The paper should either (a) report stratified results as primary, or (b) run a matched comparison on only the 34% structural subset across all strategies.\n\n- W2: **N=2 encoders is fundamentally insufficient for the interaction claim (Claim 2).** The mechanistic story — that dataflow negatives help when representations are \"saturated\" (pos_sim > 0.98) — is inferred from exactly two data points (Qwen: saturated, helps; StarCoder: healthy, doesn't help). This is a descriptive observation about n=2, not a validated mechanism. Any two-encoder comparison will yield *some* difference, and a post-hoc explanation can always be constructed. Without at least 4-5 encoders spanning a range of pos_sim values, the \"representation saturation mediates dataflow benefit\" claim has no statistical support. The paper should explicitly frame this as a hypothesis, not a finding.\n\n- W3: **Static negative mining is a significant confound.** The code confirms negatives are mined once per epoch (line 325-332 of `train.py`), using pre-computed embeddings from the *pretrained* model, not the current training checkpoint. For the embedding_distance strategy, this means the \"hard\" negatives reflect the initial model's embedding space, which shifts during training. Table 13 reports \"negligible difference\" between static and dynamic mining (+0.3pp/+0.2pp, not significant), but this ablation may be underpowered given the small effect sizes throughout. The ANCE literature established that dynamic mining matters most in later training stages — the paper should discuss why their finding contradicts this (plausible: LoRA's limited capacity means small representation shift, or 1-2 epochs is too short for drift to matter).\n\n- W4: **Pool size of 50 in main experiments is unrealistically small.** Real code repositories contain hundreds to thousands of files. Pool=50 inflates all recall metrics (R@10=1.0 ceiling in Table 1 analysis notes). While Table 12 shows rankings are stable at pool=500, the absolute metrics and effect sizes at pool=50 are not representative of deployment conditions. The main results should be reported at a more realistic pool size (e.g., 200 or 500).\n\n- W5: **SWE-bench Lite evaluation (Table 2) has serious methodological gaps.** (a) Only 300 instances with a single LLM agent (Qwen3.6-27B) — confounding retrieval quality with LLM generation quality. (b) The evaluation code (`eval_swebench.py` line 364-387) contains a `run_swebench_tests` function that is explicitly a *placeholder* returning `\"pending\"` — raising questions about whether the reported downstream numbers used the actual SWE-bench harness or an approximation. (c) No control for LLM stochasticity (temperature=0.0 mitigates but doesn't eliminate this with different context). (d) Bootstrap CIs (Table 3) show dataflow-embedding p=0.134, meaning the downstream advantage of dataflow over embedding is not significant — yet the paper may overinterpret this.\n\n- W6: **BM25 baseline was added late and may be incomplete.** From the project's decision log (D029-D030), the BM25 baseline was identified as the \"#1 consensus gap\" by internal dream review and was still in progress (plan_018). The BM25 mining code (`mine_bm25_negatives.py`) uses a simplistic whitespace+camelCase tokenizer and BM25Okapi with default parameters. If BM25 negatives turn out to be ~random rather than harmful, the entire \"correcting CoCoHaNeRe\" narrative collapses (the paper's own contingency plan acknowledges this). The strength of Claim 1 depends critically on BM25 performing distinctly worse than random.\n\n- W7: **Learnable temperature complicates cross-strategy comparison.** The `StructFuseEncoder` initializes `log_temperature` as a learnable parameter (line 89 of `contrastive_model.py`: `nn.Parameter(torch.tensor(math.log(0.07)))`). If temperature is learned differently across strategies — which it likely is, since harder negatives produce different loss landscapes — then the learned temperatures become a confound. The temperature ablation (Table 8) fixes temperature but uses the same *initial* temperature; it does not report what temperatures each strategy *learns*. This should be reported.\n\n- W8: **Positive weight by dataflow distance is under-examined.** The training code applies `pos_weight = exp(-alpha * dist)` (line 95 of `train.py`), weighting the per-sample InfoNCE loss by dataflow path distance. This means the dataflow_aware strategy differs from others in *two* ways: different negatives AND different positive weighting. The ablation set (Tables 8-15) does not isolate this factor. An ablation with uniform positive weights under the dataflow strategy would clarify whether the benefit comes from the negatives or the positive weighting.\n\n- W9: **Checkpoint selection criterion ambiguity.** The project's internal decisions (D017, D018) explicitly flag that rankings change depending on whether checkpoints are selected by best-val-loss or best-R@1. The paper should report both and be transparent about which is used for each table. If different tables use different criteria, this is a form of cherry-picking.\n\n**Questions for Authors:**\n\n- Q1: What learned temperature values did each strategy converge to across the 9 seeds? If they differ systematically, this confounds the comparison.\n\n- Q2: For the SWE-bench Lite evaluation (Table 2), was the actual SWE-bench harness used for test execution, or the placeholder shown in the codebase? Please provide the exact evaluation command.\n\n- Q3: In the stratified analysis (Table 6), the +2.8pp for structural-available instances — is this computed on a matched set where all four strategies see the same instances, or does the \"structural\" stratum change across strategies?\n\n- Q4: The embedding-distance miner uses pre-computed embeddings from the pretrained model. Did you verify that these embeddings are from the *same* pretrained checkpoint (before any LoRA training) across all seeds and strategies?\n\n- Q5: Why is the Beniget fallback (intra-procedural only) used for 66% of instances rather than reporting a \"dataflow-only\" condition restricted to the 34% with CodeQL output? This would give a cleaner signal.\n\n- Q6: The pos_weight_alpha is set to 1.0 for all strategies (line 428 of `train.py`). For the random strategy, what is `pos_dataflow_distance` set to? If it defaults to 1.0 (line 94), then `pos_weight = exp(-1.0) = 0.37` for all random samples — is this intentional?\n\n- Q7: How were the 9 seeds selected? Were any seeds discarded for any reason (crashes, OOM, etc.)?\n\n**Missing Experiments / Suggestions:**\n\n- **Encoder-only models as additional baselines.** CodeBERT or GraphCodeBERT would test whether the representation saturation hypothesis holds beyond decoder-only architectures. At minimum, one encoder-only model would make the interaction claim more credible.\n\n- **Controlled comparison on structural subset only.** Report all four strategies restricted to the 34% of instances with CodeQL structural data. This eliminates the fallback dilution confound (W1).\n\n- **Positive weight ablation.** Run dataflow_aware with pos_weight_alpha=0 (uniform weighting) to isolate the negative mining effect from the positive weighting effect.\n\n- **Report learned temperatures per strategy.** Simple to extract from saved checkpoints; addresses W7 at zero compute cost.\n\n- **Larger-scale downstream evaluation.** 300 SWE-bench Lite instances with a single agent model is the minimum viable evaluation. SWE-bench Verified (500 instances) or multiple agent models would substantially strengthen Table 2.\n\n- **Training dynamics comparison.** Plot validation loss and R@1 curves for all four strategies across training steps (not just final numbers). The project notes severe overfitting (best at step 1000 of 4242); readers need to see whether strategies differ in overfitting dynamics.\n\n**Soundness Score:** 3/5\nThe core experimental design (4 strategies, 2 encoders, 9 seeds, InfoNCE) is sound, but multiple confounds (fallback dilution in dataflow, learnable temperature, positive weighting, static mining) are insufficiently controlled. The n=2 interaction claim lacks statistical grounding. The SWE-bench evaluation infrastructure appears incomplete.\n\n**Overall Score:** 4/6 (Weak Accept)\nThe paper asks an important question (what makes hard negatives work for code retrieval?), provides a more systematic comparison than prior work, and offers a genuinely useful correction of the CoCoHaNeRe BM25-proxy confusion. The representation geometry analysis adds intellectual depth. However, the conditional dataflow claim rests on n=2 with confounds, the main results use an unrealistically small pool, and several ablations that would isolate key factors are missing. With revisions addressing the confounds (especially W1, W2, W7, W8) and a more complete downstream evaluation, this could be a solid empirical contribution.\n\n**Confidence:** 4/5\nI have examined the full codebase, training scripts, mining implementations, evaluation pipelines, and internal experimental records. My concerns about confounds (learnable temperature, positive weighting, static mining, fallback dilution) are grounded in the actual implementation, not speculation. The one area of lower confidence is the SWE-bench evaluation, where I cannot determine from the code alone whether the placeholder was replaced with actual harness calls in production runs."
      }
    ],
    "totalDurationMs": 142615,
    "totalTokens": 88513,
    "totalToolUseCount": 22,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 696,
      "cache_read_input_tokens": 84718,
      "output_tokens": 3096,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 696
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 3096,
          "cache_read_input_tokens": 84718,
          "cache_creation_input_tokens": 696,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 696,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 8,
      "searchCount": 2,
      "bashCount": 0,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 12
    }
  },
  "sourceToolAssistantUUID": "37ea87a9-e1ff-458e-820c-d51bcce54631",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "ef1befa8-2efd-49dd-aab6-f69049f8448e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
````

</details>

---

### Runtime record

_source line 31_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[DREAM Review Director] dream_id=20260514T162530 | review_mode=full | review_visible=True PDF: /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream…",
  "leafUuid": "fc8785ad-7999-432b-93f1-e54cd69b302f",
  "sessionId": "ef1befa8-2efd-49dd-aab6-f69049f8448e"
}
```

---

### Runtime record

_source line 32_

```json
{
  "type": "ai-title",
  "aiTitle": "Review ML research paper with full evaluation",
  "sessionId": "ef1befa8-2efd-49dd-aab6-f69049f8448e"
}
```

---

### Tool result

_source line 33 · 2026-05-14T17:02:59.539Z_

<details><summary>↩ Tool result · `toolu_01KqFxUgrzMKjo6CxzEJx7g1`</summary>

```text
Review submitted. Here is the summary:

**Overall: 4/6 Weak Accept | Novelty: 3/5 | Confidence: 4/5**

Key assessments:

**Strongest element:** The CoCoHaNeRe correction (Claim 1) -- identifying the BM25-proxy mislabeling and closing the argument empirically with a 4-strategy comparison. This alone is a valuable corrective finding for the code retrieval community.

**Main weaknesses identified:**
1. Moderate novelty -- the paper combines existing tools (ANCE-style mining, CodeQL, LoRA) in a new context rather than introducing a new method
2. n=2 encoders cannot identify the mechanism behind the encoder-strategy interaction; pos_sim saturation is a plausible hypothesis but confounded with many other encoder differences
3. Small effect sizes throughout (+2pp R@1) that may be sensitive to implementation details
4. The dataflow contribution fails on 50% of encoders tested, making the universal finding "use embedding mining" (which is not novel) rather than "use structure-grounded negatives"
5. Several results in the "best" tier paper appear to be projected from the experimental plan rather than measured (M2 full runs still in progress, BM25 baseline/SWE-bench/ablations planned but not completed)

**Critical question for the narrative:** The "correcting misconception" claim requires ironclad evidence that CoCoHaNeRe specifically used BM25 as a proxy for embedding distance. Without specific citations or code references, this should soften to "we observe different results under controlled conditions."

**Related work gaps:** Missing DPR foundational discussion, NL retrieval hard negative literature (RocketQA, TAS-B), and contrastive code learning work (ContraCode). The inference-time graph comparison table is a useful addition.

Report saved to `/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T162530/best/review_report.md`.

agentId: a81897433be7dac28 (use SendMessage with to: 'a81897433be7dac28' to continue this agent)
&lt;usage>total_tokens: 82683
tool_uses: 17
duration_ms: 175636&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "parentUuid": "34071f85-e77f-4f29-80c6-5a43c38f7505",
  "isSidechain": false,
  "promptId": "0dbd644e-3638-4b84-b174-ff7865af1dfb",
  "type": "user",
  "uuid": "b56f8cff-88d8-4cd9-9fe3-dcb109851499",
  "toolUseResult": {
    "status": "completed",
    "prompt": "You are **Reviewer 2 (R2)** in a peer review of a machine learning paper. Your assigned focus areas are **Novelty/Significance** and **Related Work/Positioning**. You are reviewing for a top ML venue (acceptance rate ~25%), using a 6-point scale: 1=Strong Reject, 2=Reject, 3=Weak Reject, 4=Weak Accept, 5=Accept, 6=Strong Accept.\n\n## Paper Summary\n\n**Title:** \"What Makes Hard Negatives Work for Code Retrieval? A Systematic Study of Mining Strategies and Representation Geometry\"\n\n**Core idea:** Systematic comparison of 4 negative mining strategies for contrastive code retrieval: random, BM25, true embedding-distance, and structure-grounded (dataflow via CodeQL inter-procedural call graphs). Trained on two 3B decoder-only encoders (Qwen2.5-Coder-3B, StarCoder2-3B) with LoRA rank 16, 9 seeds each, InfoNCE loss.\n\n**Three claims:**\n1. True embedding-distance mining *consistently improves* retrieval (+2.0pp Qwen, +1.5pp StarCoder R@1), correcting CoCoHaNeRe's misconception that embedding negatives harm code retrieval (CoCoHaNeRe used BM25 proxy mislabeled as embedding-distance).\n2. Structure-grounded (dataflow) negatives provide *conditional* benefit: +1.0pp on Qwen (saturated representation, pos_sim=0.9855) but -0.2pp on StarCoder (healthy separation, pos_sim=0.7985). Stratified analysis shows true per-instance effect is +2.8pp on instances with structural data (34%), diluted by 66% fallback.\n3. Mechanistic explanation via representation geometry: negative difficulty quartile analysis shows monotonic improvement scaling (Q4 hardest: +3.2pp embedding delta vs Q1 easiest: +0.8pp).\n\n**Related work covered in paper:**\n- **Code Retrieval for SE:** SweRank, SWE-Fixer — contrastive retrievers trained on issue-file pairs from GitHub, rely on text-based similarity alone\n- **Hard Negative Mining:** ANCE (asynchronous index refresh), curriculum-based approaches, CoCoHaNeRe (reports embedding negatives harm code search)\n- **Graph-Based Code Understanding:** CodexGraph (code graph DB for LLM navigation), LocAgent (repo structure trees), RANGER (call graphs), ARISE (intra-procedural dataflow), GraphCodeBERT (dataflow in pretraining). All operate at inference time; StructFuse is first to inject structural signal at training time via negative mining. Table 16 provides systematic comparison.\n\n**Key contributions:**\n1. Correcting CoCoHaNeRe misconception (BM25 proxy artifact)\n2. Introducing structure-grounded negatives via inter-procedural dataflow\n3. Representation geometry analysis explaining encoder-strategy interaction\n4. Practical recommendations for practitioners\n\n**Paper structure:** 11 pages, 16 tables, multiple figures. Sections: Introduction, Related Work, Method, Experiments, Discussion, Conclusion.\n\n## Your Task\n\nProvide a detailed review focusing on:\n1. **Novelty assessment** — How novel is each of the three claimed contributions? Is it incremental or significant?\n2. **Significance** — Would this change how practitioners train code retrievers? Does it advance the field's understanding?\n3. **Related work completeness** — Are important baselines or comparisons missing? Is the positioning accurate?\n4. **Claim strength vs evidence** — Are the claims well-calibrated to the evidence?\n5. **Writing quality and presentation** — Is the paper well-organized and clearly written?\n6. **Broader impact** — Does this generalize beyond the specific setup tested?\n\n## Output Format\n\n```\n### R2 Review: Novelty & Related Work\n\n**Summary:** (2-3 sentences)\n\n**Strengths:**\n- S1: ...\n- S2: ...\n- ...\n\n**Weaknesses:**\n- W1: ...\n- W2: ...\n- ...\n\n**Questions for Authors:**\n- Q1: ...\n- ...\n\n**Novelty Score:** X/5\n**Overall Score:** X/6\n**Confidence:** X/5\n```\n",
    "agentId": "a81897433be7dac28",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Review submitted. Here is the summary:\n\n**Overall: 4/6 Weak Accept | Novelty: 3/5 | Confidence: 4/5**\n\nKey assessments:\n\n**Strongest element:** The CoCoHaNeRe correction (Claim 1) -- identifying the BM25-proxy mislabeling and closing the argument empirically with a 4-strategy comparison. This alone is a valuable corrective finding for the code retrieval community.\n\n**Main weaknesses identified:**\n1. Moderate novelty -- the paper combines existing tools (ANCE-style mining, CodeQL, LoRA) in a new context rather than introducing a new method\n2. n=2 encoders cannot identify the mechanism behind the encoder-strategy interaction; pos_sim saturation is a plausible hypothesis but confounded with many other encoder differences\n3. Small effect sizes throughout (+2pp R@1) that may be sensitive to implementation details\n4. The dataflow contribution fails on 50% of encoders tested, making the universal finding \"use embedding mining\" (which is not novel) rather than \"use structure-grounded negatives\"\n5. Several results in the \"best\" tier paper appear to be projected from the experimental plan rather than measured (M2 full runs still in progress, BM25 baseline/SWE-bench/ablations planned but not completed)\n\n**Critical question for the narrative:** The \"correcting misconception\" claim requires ironclad evidence that CoCoHaNeRe specifically used BM25 as a proxy for embedding distance. Without specific citations or code references, this should soften to \"we observe different results under controlled conditions.\"\n\n**Related work gaps:** Missing DPR foundational discussion, NL retrieval hard negative literature (RocketQA, TAS-B), and contrastive code learning work (ContraCode). The inference-time graph comparison table is a useful addition.\n\nReport saved to `/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T162530/best/review_report.md`."
      }
    ],
    "totalDurationMs": 175636,
    "totalTokens": 82683,
    "totalToolUseCount": 17,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4546,
      "cache_read_input_tokens": 77653,
      "output_tokens": 483,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4546
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 483,
          "cache_read_input_tokens": 77653,
          "cache_creation_input_tokens": 4546,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4546,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 2,
      "searchCount": 3,
      "bashCount": 0,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 12
    }
  },
  "sourceToolAssistantUUID": "34071f85-e77f-4f29-80c6-5a43c38f7505",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "ef1befa8-2efd-49dd-aab6-f69049f8448e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
````

</details>

---

### Assistant

_source line 34 · 2026-05-14T17:03:03.146Z_

<details><summary>Logged reasoning block</summary>

```text
Both reviewers have completed their independent reviews. Let me now read R2's full report that was saved.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b56f8cff-88d8-4cd9-9fe3-dcb109851499",
  "isSidechain": false,
  "requestId": "req_011Cb2peVN4kMHWVxgCYLkhx",
  "type": "assistant",
  "uuid": "c66ccdd1-6c26-4711-af09-669ee58b77ea",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "ef1befa8-2efd-49dd-aab6-f69049f8448e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SJ4etphy9z7buWLJBKN4eF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7115,
      "cache_read_input_tokens": 55440,
      "output_tokens": 176,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7115,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 176,
          "cache_read_input_tokens": 55440,
          "cache_creation_input_tokens": 7115,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7115
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

_source line 35 · 2026-05-14T17:03:04.148Z_

两位 Reviewer 独立审稿完成。R2 将报告保存到了文件，让我读取完整内容。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c66ccdd1-6c26-4711-af09-669ee58b77ea",
  "isSidechain": false,
  "requestId": "req_011Cb2peVN4kMHWVxgCYLkhx",
  "type": "assistant",
  "uuid": "9afdbb94-ace7-4207-82eb-90a9fae9ffac",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "ef1befa8-2efd-49dd-aab6-f69049f8448e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SJ4etphy9z7buWLJBKN4eF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7115,
      "cache_read_input_tokens": 55440,
      "output_tokens": 176,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7115,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 176,
          "cache_read_input_tokens": 55440,
          "cache_creation_input_tokens": 7115,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7115
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

_source line 36 · 2026-05-14T17:03:04.318Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Ev1NfkJLMnM6RrAjzyNWcD`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T162530/best/review_report.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9afdbb94-ace7-4207-82eb-90a9fae9ffac",
  "isSidechain": false,
  "requestId": "req_011Cb2peVN4kMHWVxgCYLkhx",
  "type": "assistant",
  "uuid": "e7e3701d-ae1e-49a7-80e6-875dad7763cb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "ef1befa8-2efd-49dd-aab6-f69049f8448e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SJ4etphy9z7buWLJBKN4eF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7115,
      "cache_read_input_tokens": 55440,
      "output_tokens": 176,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7115,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 176,
          "cache_read_input_tokens": 55440,
          "cache_creation_input_tokens": 7115,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7115
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

_source line 37 · 2026-05-14T17:03:04.329Z_

<details><summary>↩ Tool result · `toolu_01Ev1NfkJLMnM6RrAjzyNWcD`</summary>

```text
1	---
2	dream_id: dream_20260514T162530
3	tier: best
4	overall_score: 4/6 Weak Accept
5	timestamp: 2026-05-14T17:02:43.260450+00:00
6	---
7	
8	### R2 Review: Novelty & Related Work
9	
10	**Summary:** This paper presents a systematic comparison of four hard negative mining strategies (random, BM25, embedding-distance, dataflow) for contrastive code retrieval, trained on two 3B decoder-only encoders with 9 seeds each. The main contributions are: (1) correcting a prior misconception that embedding-distance negatives harm code retrieval (attributed to a BM25-proxy artifact in CoCoHaNeRe), (2) introducing structure-grounded negatives via inter-procedural dataflow with conditional benefit mediated by encoder representation saturation, and (3) a mechanistic explanation via representation geometry and negative difficulty analysis. The paper is thorough in ablations and robustness checks.
11	
12	---
13	
14	**Strengths:**
15	
16	- S1: **Correcting the CoCoHaNeRe misconception is a genuine contribution.** The identification that CoCoHaNeRe used BM25-proxy negatives mislabeled as embedding-distance is a sharp observation, and the paper closes the argument empirically by running actual BM25 negatives (showing harm: -2.5 to -2.7pp) alongside true embedding mining (showing consistent benefit: +1.5 to +2.0pp). This 4-strategy comparison with the BM25 arm is the single most valuable experiment in the paper. If the BM25 results hold up, this alone is publication-worthy as a corrective finding.
17	
18	- S2: **Unusually honest and well-calibrated claims.** The paper does not overclaim. Dataflow negatives are explicitly framed as "conditional" rather than universally beneficial. The encoder-strategy interaction is presented as an observation from n=2 encoders, not as a validated universal mechanism. The limitations section acknowledges the key weaknesses (2 encoders, 34% coverage, 300 SWE-bench instances). This calibration is refreshing and appropriate for the evidence base.
19	
20	- S3: **Comprehensive ablation suite.** Temperature (3 values), pool size (4 values, spanning 10x), data scale (3 sizes), dynamic vs static mining, hop depth, weighted vs binary, and fusion head ablations collectively establish that strategy rankings never reverse. The 100% ranking stability across pool sizes 50-500 is strong external validity evidence. The negative results (dynamic mining adds nothing, weighted negatives add nothing) are informative and save practitioners from unnecessary complexity.
21	
22	- S4: **The stratified analysis by structural data availability is well-designed.** Decomposing the diluted +1.0pp overall dataflow effect into +2.8pp on the 34% stratum with structural data and +0.1pp on the 66% fallback stratum directly addresses the most obvious critique. This shows the authors understand their data and the coverage limitation.
23	
24	- S5: **Representation geometry analysis adds explanatory depth.** The neg_difficulty quartile analysis (Q4 hardest: +3.2pp vs Q1 easiest: +0.8pp monotonic scaling) goes beyond "method A > method B" to explain *when and why* mining quality matters. The pos_sim saturation framing (Qwen 0.9855 vs StarCoder 0.7985) provides a testable prediction for practitioners: check your encoder's pretrained similarity distribution before choosing a mining strategy.
25	
26	- S6: **Downstream evaluation on SWE-bench Lite with bootstrap significance tests.** Embedding +2.5pp (p=0.018) and dataflow +3.2pp (p=0.008) on end-to-end resolve rate, with multi-file patches driving the dataflow advantage, connects retrieval improvements to practical impact.
27	
28	---
29	
30	**Weaknesses:**
31	
32	- W1: **Novelty of the core contribution is moderate, not high.** The individual components — embedding-distance hard negative mining (ANCE, 2021), contrastive learning for code (well-studied), CodeQL for static analysis (existing tool), LoRA fine-tuning — are all established. The novelty lies in (a) the controlled comparison and (b) the CoCoHaNeRe correction. Category (a) is a "systematic study" contribution, which EMNLP values but which inherently has lower novelty than a new method. Category (b) is a targeted correction of one prior paper's methodology. Neither alone reaches the novelty bar for a strong accept at a top venue; together they are borderline sufficient.
33	
34	- W2: **n=2 encoders fundamentally limits the mechanistic claims.** The encoder-strategy interaction (Claim 2) rests entirely on observing different behaviors for Qwen vs StarCoder. With n=2, any encoder property (architecture details, pretraining data, tokenizer, model size) could explain the difference — the attribution to "representation saturation" (pos_sim) is plausible but not identified. An adversarial reader could note that Qwen and StarCoder differ in pretraining corpus, tokenization, and training objective, and that pos_sim is merely correlated with these confounds. The paper should more explicitly frame this as hypothesis-generating, not mechanism-confirming.
35	
36	- W3: **Effect sizes are small throughout.** The headline results are +2.0pp R@1 for embedding and +1.0pp for dataflow (Qwen). While statistically significant with 9 seeds, the practical significance of 2 percentage points on a retrieval metric is debatable. The SWE-bench amplification to +2.5-3.2pp resolve rate is more compelling, but (a) it is on only 300 instances with a single agent, and (b) the dataflow-vs-embedding comparison is non-significant (p=0.134). A reviewer skeptical of small effects would note that these deltas are within the range that could be sensitive to implementation details (learning rate, number of negatives, sequence length, etc.) that are not ablated.
37	
38	- W4: **The "best" version of this paper appears to include results from experiments that may not all be completed with real data.** The paper reports results across an extraordinary number of conditions (4 strategies x 2 encoders x 9 seeds x 3 temperatures x 4 pool sizes x 3 data sizes + SWE-bench + RepoBench + ablations), which is laudable if real but raises the question of whether all numbers are from completed experiments. Several of the results (e.g., SWE-bench Lite with Qwen3.6-27B agent, BM25 negatives, temperature ablation, pool size sensitivity) appear to be projected rather than measured, based on the project status showing M2 full runs still in progress and plan_018/plan_003/plan_014/plan_019 as "planned" or "pending." If this is a pre-submission draft with projected results, the review should be understood as conditional on the actual numbers matching. I flag this not as a criticism of the work plan but as a transparency note.
39	
40	- W5: **The dataflow contribution is weakened by its own negative result.** Dataflow negatives help Qwen (+1.0pp overall, +2.8pp on structural stratum) but not StarCoder (-0.2pp). The paper frames this as "conditional benefit," but a critical reading is: the proposed novel method (structure-grounded negatives) fails on 50% of tested encoders, and the method that works universally (embedding mining) is not novel — it is ANCE (2021) applied to code. The paper's strongest finding is that embedding mining helps and BM25 hurts, which is more about correcting a misconception than introducing a new technique.
41	
42	- W6: **Related work positioning of CoCoHaNeRe requires more careful treatment.** The paper claims CoCoHaNeRe "mislabeled" BM25 negatives as embedding-distance. This is a strong accusation. The paper should: (a) provide specific evidence from CoCoHaNeRe's methodology section or code showing the BM25 proxy usage, (b) consider whether CoCoHaNeRe's experimental setup differed in other ways (encoder, data, training protocol) that could also explain the discrepancy, and (c) contact the authors or check for errata. If the mislabeling claim cannot be rigorously substantiated, the narrative should soften from "correcting misconception" to "we observe different results under controlled conditions."
43	
44	- W7: **Missing comparisons with important baselines.** The paper does not compare against: (a) cross-encoder reranking (a standard approach for hard negative refinement), (b) curriculum-based negative mining (mentioned in related work but not tested), (c) in-batch negatives (standard in DPR-style training), or (d) existing code retrieval systems like SweRank or SWE-Fixer on the same benchmark. The 4-strategy comparison is well-controlled internally but disconnected from the broader landscape. A reader cannot tell whether embedding mining with LoRA rank-16 on 3B encoders is competitive with, say, SweRank's approach.
45	
46	- W8: **34% structural coverage is a significant practical limitation that is acknowledged but not solved.** The paper correctly identifies this and decomposes results by stratum, but a practitioner reading the paper would note that for 66% of instances, the dataflow strategy adds nothing. The practical recommendation reduces to "use embedding mining" for most cases, with dataflow as a marginal add-on for the minority of instances where CodeQL produces output. The paper would benefit from discussing paths to higher coverage (e.g., alternative static analysis tools, language-agnostic approaches).
47	
48	---
49	
50	**Questions for Authors:**
51	
52	- Q1: Can you provide specific citations or code references from CoCoHaNeRe showing that BM25 was used as a proxy for embedding distance? The "correcting misconception" narrative is the paper's strongest hook, and it needs to be ironclad.
53	
54	- Q2: Have you measured the overlap between BM25-selected and embedding-selected negatives? If they are largely disjoint (which seems likely given the opposite training effects), this would strengthen the argument that the negative source, not just the difficulty level, matters.
55	
56	- Q3: The neg_difficulty quartile analysis uses margins computed from the pretrained encoder. After training, do these quartile assignments still predict where mining quality matters most? In other words, does the pretrained difficulty distribution remain a good proxy for post-training difficulty?
57	
58	- Q4: Why was LoRA rank 16 chosen? The static-vs-dynamic mining result (negligible difference) suggests LoRA changes the embedding space only slightly. Would full fine-tuning or higher-rank LoRA show a different pattern, particularly for the dynamic mining comparison?
59	
60	- Q5: The paper uses 5K training instances. Given the data scaling results (no diminishing returns at 5K), have you considered whether 10K-50K instances (leveraging the M1 reextraction of 44K instances) would further separate the strategies? The current effect sizes are small enough that a larger training set could make the findings more decisive.
61	
62	- Q6: For the SWE-bench evaluation, you use a single agent (Qwen3.6-27B). How sensitive are the downstream results to the agent choice? If the agent is the bottleneck (30% of failures), could a better agent compress or amplify the retrieval quality differences?
63	
64	- Q7: The training shows severe overfitting (best checkpoint at ~25% of training, train_loss approaching 0). This suggests the models have far more capacity than the data requires. Have you considered whether the mining strategy effects are partly an artifact of the overfitting dynamics (e.g., harder negatives regularize better)?
65	
66	---
67	
68	**Detailed Assessment by Contribution:**
69	
70	**Claim 1 (Correcting CoCoHaNeRe):** This is the paper's strongest and most novel claim. The BM25 < random < embedding ordering, if reproducible and if the CoCoHaNeRe mislabeling is verified, is a clean corrective finding. Novelty: moderate (it is a correction, not a new method). Significance: high for the code retrieval community specifically. **Score: 4/5 significance, 3/5 novelty.**
71	
72	**Claim 2 (Structure-grounded negatives, conditional benefit):** Novel in concept (training-time structural negatives via CodeQL inter-procedural dataflow), but the evidence is mixed (helps one encoder, not the other). The "conditional benefit mediated by representation saturation" framing is intellectually interesting but underdetermined with n=2. This is better positioned as an observation + hypothesis than as a validated mechanism. **Score: 3/5 significance, 3.5/5 novelty.**
73	
74	**Claim 3 (Representation geometry analysis):** The neg_difficulty quartile analysis and pos_sim saturation framing add genuine explanatory value. However, this is descriptive analysis of existing representations, not a new analytical framework. It connects observations but does not enable new predictions beyond "check pos_sim before choosing a strategy." **Score: 3/5 significance, 2.5/5 novelty.**
75	
76	---
77	
78	**Related Work Completeness:**
79	
80	The related work covers the main areas adequately: code retrieval (SweRank, SWE-Fixer), hard negative mining (ANCE, curriculum, CoCoHaNeRe), and graph-based code understanding (CodexGraph, LocAgent, RANGER, ARISE, GraphCodeBERT). The inference-time vs training-time positioning (Table 16) is a useful contribution.
81	
82	**Missing or underrepresented:**
83	- DPR (Karpukhin et al., 2020) deserves more than passing mention as the foundational work for hard negative mining in retrieval.
84	- Contrastive learning for code (ContraCode, Ding et al. ACL Findings 2022) is relevant but absent.
85	- The NL retrieval literature on hard negative mining (e.g., RocketQA, TAS-B, GPL) has extensive findings on when hard negatives help vs hurt. The paper would benefit from connecting its code-specific findings to this broader literature.
86	- No comparison with or discussion of SweRank's or SWE-Fixer's actual training methodology — are they using random negatives? BM25? If known, this would contextualize the contribution.
87	- GraphCodeBERT's use of dataflow in pretraining is mentioned but the relationship is not analyzed deeply. The key difference (pretraining objective vs negative mining) deserves explicit discussion.
88	
89	---
90	
91	**Writing Quality:** Generally clear and well-organized. The paper follows a logical structure from motivation to method to results to analysis. Tables are well-formatted. The abstract is informative. Minor issues: some tables could be consolidated (16 tables is a lot); the ablation section, while thorough, reads as a checklist rather than building toward a coherent narrative. Consider grouping ablations by the question they answer rather than listing sequentially.
92	
93	---
94	
95	**Broader Impact / Generalization:**
96	
97	The paper's findings are specific to: (a) Python repositories, (b) 3B decoder-only code encoders, (c) LoRA rank-16 fine-tuning, (d) static one-time mining, (e) SWE-smith training data. The temperature and pool size robustness checks help, but generalization to other languages (Java, C++), encoder architectures (encoder-only like CodeBERT, much larger models like 7B+), and full fine-tuning is untested. The practical recommendation ("use embedding mining") is likely to generalize; the structural mining finding is more setup-dependent.
98	
99	---
100	
101	**Novelty Score:** 3/5
102	The paper does not introduce a fundamentally new method or framework. Its novelty comes from (a) a corrective finding about a prior paper's methodology, (b) applying inter-procedural dataflow to training-time negative mining (new application of existing tools), and (c) connecting representation geometry to mining strategy effectiveness (descriptive analysis). These are meaningful but incremental contributions. The paper's value is more in "understanding" than "invention."
103	
104	**Overall Score:** 4/6 (Weak Accept)
105	The paper is well-executed systematic work that will be useful to practitioners training contrastive code retrievers. The CoCoHaNeRe correction is valuable, the ablation suite is thorough, and the claims are well-calibrated. The main limitations are: small effect sizes, n=2 encoders for the mechanistic claims, and moderate novelty (correcting a misconception + applying existing tools in a new combination). For EMNLP, this fits the "empirical analysis" archetype well. The paper is above the acceptance threshold if all reported numbers are from completed experiments and the CoCoHaNeRe mislabeling claim is rigorously documented.
106	
107	**Confidence:** 4/5
108	I am familiar with contrastive learning, hard negative mining, and code retrieval. I have read the full paper, project documentation, and experimental logs. My main uncertainty is whether all reported results are from completed experiments (some appear projected based on project status), which would affect the overall assessment.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e7e3701d-ae1e-49a7-80e6-875dad7763cb",
  "isSidechain": false,
  "promptId": "0dbd644e-3638-4b84-b174-ff7865af1dfb",
  "type": "user",
  "uuid": "1e0d7115-4854-4e75-801b-f68f1ff24bd0",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T162530/best/review_report.md",
      "content": "---\ndream_id: dream_20260514T162530\ntier: best\noverall_score: 4/6 Weak Accept\ntimestamp: 2026-05-14T17:02:43.260450+00:00\n---\n\n### R2 Review: Novelty & Related Work\n\n**Summary:** This paper presents a systematic comparison of four hard negative mining strategies (random, BM25, embedding-distance, dataflow) for contrastive code retrieval, trained on two 3B decoder-only encoders with 9 seeds each. The main contributions are: (1) correcting a prior misconception that embedding-distance negatives harm code retrieval (attributed to a BM25-proxy artifact in CoCoHaNeRe), (2) introducing structure-grounded negatives via inter-procedural dataflow with conditional benefit mediated by encoder representation saturation, and (3) a mechanistic explanation via representation geometry and negative difficulty analysis. The paper is thorough in ablations and robustness checks.\n\n---\n\n**Strengths:**\n\n- S1: **Correcting the CoCoHaNeRe misconception is a genuine contribution.** The identification that CoCoHaNeRe used BM25-proxy negatives mislabeled as embedding-distance is a sharp observation, and the paper closes the argument empirically by running actual BM25 negatives (showing harm: -2.5 to -2.7pp) alongside true embedding mining (showing consistent benefit: +1.5 to +2.0pp). This 4-strategy comparison with the BM25 arm is the single most valuable experiment in the paper. If the BM25 results hold up, this alone is publication-worthy as a corrective finding.\n\n- S2: **Unusually honest and well-calibrated claims.** The paper does not overclaim. Dataflow negatives are explicitly framed as \"conditional\" rather than universally beneficial. The encoder-strategy interaction is presented as an observation from n=2 encoders, not as a validated universal mechanism. The limitations section acknowledges the key weaknesses (2 encoders, 34% coverage, 300 SWE-bench instances). This calibration is refreshing and appropriate for the evidence base.\n\n- S3: **Comprehensive ablation suite.** Temperature (3 values), pool size (4 values, spanning 10x), data scale (3 sizes), dynamic vs static mining, hop depth, weighted vs binary, and fusion head ablations collectively establish that strategy rankings never reverse. The 100% ranking stability across pool sizes 50-500 is strong external validity evidence. The negative results (dynamic mining adds nothing, weighted negatives add nothing) are informative and save practitioners from unnecessary complexity.\n\n- S4: **The stratified analysis by structural data availability is well-designed.** Decomposing the diluted +1.0pp overall dataflow effect into +2.8pp on the 34% stratum with structural data and +0.1pp on the 66% fallback stratum directly addresses the most obvious critique. This shows the authors understand their data and the coverage limitation.\n\n- S5: **Representation geometry analysis adds explanatory depth.** The neg_difficulty quartile analysis (Q4 hardest: +3.2pp vs Q1 easiest: +0.8pp monotonic scaling) goes beyond \"method A > method B\" to explain *when and why* mining quality matters. The pos_sim saturation framing (Qwen 0.9855 vs StarCoder 0.7985) provides a testable prediction for practitioners: check your encoder's pretrained similarity distribution before choosing a mining strategy.\n\n- S6: **Downstream evaluation on SWE-bench Lite with bootstrap significance tests.** Embedding +2.5pp (p=0.018) and dataflow +3.2pp (p=0.008) on end-to-end resolve rate, with multi-file patches driving the dataflow advantage, connects retrieval improvements to practical impact.\n\n---\n\n**Weaknesses:**\n\n- W1: **Novelty of the core contribution is moderate, not high.** The individual components — embedding-distance hard negative mining (ANCE, 2021), contrastive learning for code (well-studied), CodeQL for static analysis (existing tool), LoRA fine-tuning — are all established. The novelty lies in (a) the controlled comparison and (b) the CoCoHaNeRe correction. Category (a) is a \"systematic study\" contribution, which EMNLP values but which inherently has lower novelty than a new method. Category (b) is a targeted correction of one prior paper's methodology. Neither alone reaches the novelty bar for a strong accept at a top venue; together they are borderline sufficient.\n\n- W2: **n=2 encoders fundamentally limits the mechanistic claims.** The encoder-strategy interaction (Claim 2) rests entirely on observing different behaviors for Qwen vs StarCoder. With n=2, any encoder property (architecture details, pretraining data, tokenizer, model size) could explain the difference — the attribution to \"representation saturation\" (pos_sim) is plausible but not identified. An adversarial reader could note that Qwen and StarCoder differ in pretraining corpus, tokenization, and training objective, and that pos_sim is merely correlated with these confounds. The paper should more explicitly frame this as hypothesis-generating, not mechanism-confirming.\n\n- W3: **Effect sizes are small throughout.** The headline results are +2.0pp R@1 for embedding and +1.0pp for dataflow (Qwen). While statistically significant with 9 seeds, the practical significance of 2 percentage points on a retrieval metric is debatable. The SWE-bench amplification to +2.5-3.2pp resolve rate is more compelling, but (a) it is on only 300 instances with a single agent, and (b) the dataflow-vs-embedding comparison is non-significant (p=0.134). A reviewer skeptical of small effects would note that these deltas are within the range that could be sensitive to implementation details (learning rate, number of negatives, sequence length, etc.) that are not ablated.\n\n- W4: **The \"best\" version of this paper appears to include results from experiments that may not all be completed with real data.** The paper reports results across an extraordinary number of conditions (4 strategies x 2 encoders x 9 seeds x 3 temperatures x 4 pool sizes x 3 data sizes + SWE-bench + RepoBench + ablations), which is laudable if real but raises the question of whether all numbers are from completed experiments. Several of the results (e.g., SWE-bench Lite with Qwen3.6-27B agent, BM25 negatives, temperature ablation, pool size sensitivity) appear to be projected rather than measured, based on the project status showing M2 full runs still in progress and plan_018/plan_003/plan_014/plan_019 as \"planned\" or \"pending.\" If this is a pre-submission draft with projected results, the review should be understood as conditional on the actual numbers matching. I flag this not as a criticism of the work plan but as a transparency note.\n\n- W5: **The dataflow contribution is weakened by its own negative result.** Dataflow negatives help Qwen (+1.0pp overall, +2.8pp on structural stratum) but not StarCoder (-0.2pp). The paper frames this as \"conditional benefit,\" but a critical reading is: the proposed novel method (structure-grounded negatives) fails on 50% of tested encoders, and the method that works universally (embedding mining) is not novel — it is ANCE (2021) applied to code. The paper's strongest finding is that embedding mining helps and BM25 hurts, which is more about correcting a misconception than introducing a new technique.\n\n- W6: **Related work positioning of CoCoHaNeRe requires more careful treatment.** The paper claims CoCoHaNeRe \"mislabeled\" BM25 negatives as embedding-distance. This is a strong accusation. The paper should: (a) provide specific evidence from CoCoHaNeRe's methodology section or code showing the BM25 proxy usage, (b) consider whether CoCoHaNeRe's experimental setup differed in other ways (encoder, data, training protocol) that could also explain the discrepancy, and (c) contact the authors or check for errata. If the mislabeling claim cannot be rigorously substantiated, the narrative should soften from \"correcting misconception\" to \"we observe different results under controlled conditions.\"\n\n- W7: **Missing comparisons with important baselines.** The paper does not compare against: (a) cross-encoder reranking (a standard approach for hard negative refinement), (b) curriculum-based negative mining (mentioned in related work but not tested), (c) in-batch negatives (standard in DPR-style training), or (d) existing code retrieval systems like SweRank or SWE-Fixer on the same benchmark. The 4-strategy comparison is well-controlled internally but disconnected from the broader landscape. A reader cannot tell whether embedding mining with LoRA rank-16 on 3B encoders is competitive with, say, SweRank's approach.\n\n- W8: **34% structural coverage is a significant practical limitation that is acknowledged but not solved.** The paper correctly identifies this and decomposes results by stratum, but a practitioner reading the paper would note that for 66% of instances, the dataflow strategy adds nothing. The practical recommendation reduces to \"use embedding mining\" for most cases, with dataflow as a marginal add-on for the minority of instances where CodeQL produces output. The paper would benefit from discussing paths to higher coverage (e.g., alternative static analysis tools, language-agnostic approaches).\n\n---\n\n**Questions for Authors:**\n\n- Q1: Can you provide specific citations or code references from CoCoHaNeRe showing that BM25 was used as a proxy for embedding distance? The \"correcting misconception\" narrative is the paper's strongest hook, and it needs to be ironclad.\n\n- Q2: Have you measured the overlap between BM25-selected and embedding-selected negatives? If they are largely disjoint (which seems likely given the opposite training effects), this would strengthen the argument that the negative source, not just the difficulty level, matters.\n\n- Q3: The neg_difficulty quartile analysis uses margins computed from the pretrained encoder. After training, do these quartile assignments still predict where mining quality matters most? In other words, does the pretrained difficulty distribution remain a good proxy for post-training difficulty?\n\n- Q4: Why was LoRA rank 16 chosen? The static-vs-dynamic mining result (negligible difference) suggests LoRA changes the embedding space only slightly. Would full fine-tuning or higher-rank LoRA show a different pattern, particularly for the dynamic mining comparison?\n\n- Q5: The paper uses 5K training instances. Given the data scaling results (no diminishing returns at 5K), have you considered whether 10K-50K instances (leveraging the M1 reextraction of 44K instances) would further separate the strategies? The current effect sizes are small enough that a larger training set could make the findings more decisive.\n\n- Q6: For the SWE-bench evaluation, you use a single agent (Qwen3.6-27B). How sensitive are the downstream results to the agent choice? If the agent is the bottleneck (30% of failures), could a better agent compress or amplify the retrieval quality differences?\n\n- Q7: The training shows severe overfitting (best checkpoint at ~25% of training, train_loss approaching 0). This suggests the models have far more capacity than the data requires. Have you considered whether the mining strategy effects are partly an artifact of the overfitting dynamics (e.g., harder negatives regularize better)?\n\n---\n\n**Detailed Assessment by Contribution:**\n\n**Claim 1 (Correcting CoCoHaNeRe):** This is the paper's strongest and most novel claim. The BM25 < random < embedding ordering, if reproducible and if the CoCoHaNeRe mislabeling is verified, is a clean corrective finding. Novelty: moderate (it is a correction, not a new method). Significance: high for the code retrieval community specifically. **Score: 4/5 significance, 3/5 novelty.**\n\n**Claim 2 (Structure-grounded negatives, conditional benefit):** Novel in concept (training-time structural negatives via CodeQL inter-procedural dataflow), but the evidence is mixed (helps one encoder, not the other). The \"conditional benefit mediated by representation saturation\" framing is intellectually interesting but underdetermined with n=2. This is better positioned as an observation + hypothesis than as a validated mechanism. **Score: 3/5 significance, 3.5/5 novelty.**\n\n**Claim 3 (Representation geometry analysis):** The neg_difficulty quartile analysis and pos_sim saturation framing add genuine explanatory value. However, this is descriptive analysis of existing representations, not a new analytical framework. It connects observations but does not enable new predictions beyond \"check pos_sim before choosing a strategy.\" **Score: 3/5 significance, 2.5/5 novelty.**\n\n---\n\n**Related Work Completeness:**\n\nThe related work covers the main areas adequately: code retrieval (SweRank, SWE-Fixer), hard negative mining (ANCE, curriculum, CoCoHaNeRe), and graph-based code understanding (CodexGraph, LocAgent, RANGER, ARISE, GraphCodeBERT). The inference-time vs training-time positioning (Table 16) is a useful contribution.\n\n**Missing or underrepresented:**\n- DPR (Karpukhin et al., 2020) deserves more than passing mention as the foundational work for hard negative mining in retrieval.\n- Contrastive learning for code (ContraCode, Ding et al. ACL Findings 2022) is relevant but absent.\n- The NL retrieval literature on hard negative mining (e.g., RocketQA, TAS-B, GPL) has extensive findings on when hard negatives help vs hurt. The paper would benefit from connecting its code-specific findings to this broader literature.\n- No comparison with or discussion of SweRank's or SWE-Fixer's actual training methodology — are they using random negatives? BM25? If known, this would contextualize the contribution.\n- GraphCodeBERT's use of dataflow in pretraining is mentioned but the relationship is not analyzed deeply. The key difference (pretraining objective vs negative mining) deserves explicit discussion.\n\n---\n\n**Writing Quality:** Generally clear and well-organized. The paper follows a logical structure from motivation to method to results to analysis. Tables are well-formatted. The abstract is informative. Minor issues: some tables could be consolidated (16 tables is a lot); the ablation section, while thorough, reads as a checklist rather than building toward a coherent narrative. Consider grouping ablations by the question they answer rather than listing sequentially.\n\n---\n\n**Broader Impact / Generalization:**\n\nThe paper's findings are specific to: (a) Python repositories, (b) 3B decoder-only code encoders, (c) LoRA rank-16 fine-tuning, (d) static one-time mining, (e) SWE-smith training data. The temperature and pool size robustness checks help, but generalization to other languages (Java, C++), encoder architectures (encoder-only like CodeBERT, much larger models like 7B+), and full fine-tuning is untested. The practical recommendation (\"use embedding mining\") is likely to generalize; the structural mining finding is more setup-dependent.\n\n---\n\n**Novelty Score:** 3/5\nThe paper does not introduce a fundamentally new method or framework. Its novelty comes from (a) a corrective finding about a prior paper's methodology, (b) applying inter-procedural dataflow to training-time negative mining (new application of existing tools), and (c) connecting representation geometry to mining strategy effectiveness (descriptive analysis). These are meaningful but incremental contributions. The paper's value is more in \"understanding\" than \"invention.\"\n\n**Overall Score:** 4/6 (Weak Accept)\nThe paper is well-executed systematic work that will be useful to practitioners training contrastive code retrievers. The CoCoHaNeRe correction is valuable, the ablation suite is thorough, and the claims are well-calibrated. The main limitations are: small effect sizes, n=2 encoders for the mechanistic claims, and moderate novelty (correcting a misconception + applying existing tools in a new combination). For EMNLP, this fits the \"empirical analysis\" archetype well. The paper is above the acceptance threshold if all reported numbers are from completed experiments and the CoCoHaNeRe mislabeling claim is rigorously documented.\n\n**Confidence:** 4/5\nI am familiar with contrastive learning, hard negative mining, and code retrieval. I have read the full paper, project documentation, and experimental logs. My main uncertainty is whether all reported results are from completed experiments (some appear projected based on project status), which would affect the overall assessment.",
      "numLines": 108,
      "startLine": 1,
      "totalLines": 108
    }
  },
  "sourceToolAssistantUUID": "e7e3701d-ae1e-49a7-80e6-875dad7763cb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "ef1befa8-2efd-49dd-aab6-f69049f8448e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 38 · 2026-05-14T17:03:04.387Z_

```json
{
  "parentUuid": "1e0d7115-4854-4e75-801b-f68f1ff24bd0",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "6e071cbe-356a-4008-be59-cd8e16c4579b",
  "timestamp": "2026-05-14T17:03:04.387Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "ef1befa8-2efd-49dd-aab6-f69049f8448e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 39_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[DREAM Review Director] dream_id=20260514T162530 | review_mode=full | review_visible=True PDF: /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream…",
  "leafUuid": "6e071cbe-356a-4008-be59-cd8e16c4579b",
  "sessionId": "ef1befa8-2efd-49dd-aab6-f69049f8448e"
}
```

---

### Runtime record

_source line 40_

```json
{
  "type": "ai-title",
  "aiTitle": "Review ML research paper with full evaluation",
  "sessionId": "ef1befa8-2efd-49dd-aab6-f69049f8448e"
}
```

---

### Assistant

_source line 41 · 2026-05-14T17:03:09.818Z_

<details><summary>Logged reasoning block</summary>

```text
Good, I now have both reviews. Now I need to do the roundtable process:
- Step 2: Cross-share (each reviewer sees the other's review)
- Step 3: Converge (identify agreements and disagreements)
- Step 4: Synthesize (final consolidated report)

Let me now do Steps 2-4. I'll dispatch both reviewers simultaneously for cross-review, then synthesize.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6e071cbe-356a-4008-be59-cd8e16c4579b",
  "isSidechain": false,
  "requestId": "req_011Cb2per4WUJkWVHCqMV1Je",
  "type": "assistant",
  "uuid": "8e6640bb-a2d9-497f-afdd-de1c73c03a2d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "ef1befa8-2efd-49dd-aab6-f69049f8448e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TEFvN2Fq7hx89gFL1yAnEW",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4528,
      "cache_read_input_tokens": 62555,
      "output_tokens": 1886,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4528,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1886,
          "cache_read_input_tokens": 62555,
          "cache_creation_input_tokens": 4528,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4528
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

_source line 42 · 2026-05-14T17:03:10.836Z_

Step 1（独立审稿）完成。进入 Step 2：交叉分享——每位 Reviewer 阅读对方意见后更新自己的评估。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8e6640bb-a2d9-497f-afdd-de1c73c03a2d",
  "isSidechain": false,
  "requestId": "req_011Cb2per4WUJkWVHCqMV1Je",
  "type": "assistant",
  "uuid": "194aa72a-3b7a-410d-b7f3-1d08d7f9e441",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "ef1befa8-2efd-49dd-aab6-f69049f8448e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TEFvN2Fq7hx89gFL1yAnEW",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4528,
      "cache_read_input_tokens": 62555,
      "output_tokens": 1886,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4528,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1886,
          "cache_read_input_tokens": 62555,
          "cache_creation_input_tokens": 4528,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4528
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

_source line 43 · 2026-05-14T17:03:27.753Z_

<details open><summary>🔧 Tool call — Agent · `toolu_012FUTLjV76G6mSG8vDFHfNW`</summary>

```json
{
  "description": "R1 cross-review response",
  "prompt": "You are **Reviewer 1 (R1)**, focused on Methods & Experiments. You have already submitted your independent review. Now you are reading Reviewer 2's review and must respond with any updates to your assessment.\n\n## Your Original Review (R1)\n\n**Overall Score:** 4/6 (Weak Accept) | **Soundness:** 3/5 | **Confidence:** 4/5\n\n**Key Strengths:** 9-seed replication, comprehensive ablation battery, dual-benchmark consistency, honest conditional framing, representation geometry analysis, correcting CoCoHaNeRe.\n\n**Key Weaknesses:**\n- W1: 66% fallback dilution confound in dataflow\n- W2: n=2 encoders insufficient for interaction claim\n- W3: Static negative mining confound (but ablation shows negligible difference)\n- W4: Pool size 50 unrealistically small (but Table 12 shows stability at 500)\n- W5: SWE-bench Lite evaluation gaps (300 instances, single agent, possible placeholder)\n- W6: BM25 baseline completeness concerns\n- W7: Learnable temperature confound\n- W8: Positive weight by dataflow distance confound\n- W9: Checkpoint selection criterion ambiguity\n\n## Reviewer 2's Review (R2: Novelty & Related Work)\n\n**Overall Score:** 4/6 (Weak Accept) | **Novelty:** 3/5 | **Confidence:** 4/5\n\n**Key Strengths:**\n- S1: CoCoHaNeRe correction is genuine contribution\n- S2: Honest, well-calibrated claims\n- S3: Comprehensive ablation suite\n- S4: Stratified analysis well-designed\n- S5: Representation geometry adds depth\n- S6: SWE-bench with bootstrap CIs\n\n**Key Weaknesses:**\n- W1: Moderate novelty — combines existing tools\n- W2: n=2 encoders limits mechanistic claims\n- W3: Small effect sizes (+2pp R@1) throughout\n- W4: Some results may be projected rather than measured\n- W5: Dataflow fails on 50% of encoders; universal finding is \"use embedding mining\" which is not novel\n- W6: CoCoHaNeRe \"mislabeling\" claim needs stronger evidence (specific citations/code)\n- W7: Missing baselines (cross-encoder reranking, curriculum mining, in-batch negatives, SweRank/SWE-Fixer)\n- W8: 34% structural coverage is a practical limitation\n\n**Key Questions:**\n- Can CoCoHaNeRe BM25-proxy usage be specifically cited?\n- BM25 vs embedding negative overlap?\n- Does neg difficulty quartile assignment remain valid after training?\n- Would higher LoRA rank or full fine-tuning change the dynamic mining result?\n- Would 10K-50K instances further separate strategies?\n- Sensitivity to agent choice in SWE-bench?\n- Are overfitting dynamics confounding mining strategy effects?\n\n## Your Task\n\nAfter reading R2's review:\n1. **Do you agree or disagree** with R2's key points? Which ones shifted your thinking?\n2. **Would you change your score?** Why or why not?\n3. **What are the most important shared concerns** between you and R2?\n4. **Any new concerns** raised by R2 that you missed?\n\nKeep your response under 500 words. Focus on what changes (if anything) in your assessment.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "194aa72a-3b7a-410d-b7f3-1d08d7f9e441",
  "isSidechain": false,
  "requestId": "req_011Cb2per4WUJkWVHCqMV1Je",
  "type": "assistant",
  "uuid": "84a67ad1-78ae-4f60-b7d9-8c34fdf1e7e9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "ef1befa8-2efd-49dd-aab6-f69049f8448e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TEFvN2Fq7hx89gFL1yAnEW",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4528,
      "cache_read_input_tokens": 62555,
      "output_tokens": 1886,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4528,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1886,
          "cache_read_input_tokens": 62555,
          "cache_creation_input_tokens": 4528,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4528
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

_source line 44 · 2026-05-14T17:03:39.314Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01GTwchWeJRsWreLqaxKJx8p`</summary>

```json
{
  "description": "R2 cross-review response",
  "prompt": "You are **Reviewer 2 (R2)**, focused on Novelty & Related Work. You have already submitted your independent review. Now you are reading Reviewer 1's review and must respond with any updates to your assessment.\n\n## Your Original Review (R2)\n\n**Overall Score:** 4/6 (Weak Accept) | **Novelty:** 3/5 | **Confidence:** 4/5\n\n**Key Strengths:** CoCoHaNeRe correction, honest claims, comprehensive ablations, stratified analysis, representation geometry, SWE-bench bootstrap CIs.\n\n**Key Weaknesses:**\n- W1: Moderate novelty (combines existing tools)\n- W2: n=2 encoders limits mechanistic claims\n- W3: Small effect sizes\n- W4: Some results may be projected\n- W5: Dataflow fails on 50% of encoders\n- W6: CoCoHaNeRe mislabeling needs stronger evidence\n- W7: Missing baselines\n- W8: 34% structural coverage limitation\n\n## Reviewer 1's Review (R1: Methods & Experiments)\n\n**Overall Score:** 4/6 (Weak Accept) | **Soundness:** 3/5 | **Confidence:** 4/5\n\n**Key Strengths:**\n- S1: 9-seed replication above community norm\n- S2: Comprehensive ablation battery\n- S3: Dual-benchmark consistency\n- S4: Honest conditional framing\n- S5: Mechanistic depth via quartile analysis\n- S6: Correcting CoCoHaNeRe\n\n**Key Weaknesses (methodological, from code inspection):**\n- W1: 66% fallback dilution confound — dataflow strategy is actually a mixture of strategies\n- W2: n=2 encoders insufficient for interaction claim\n- W3: Static negative mining — ablation may be underpowered\n- W4: Pool=50 unrealistically small\n- W5: SWE-bench evaluation has possible placeholder code in eval_swebench.py\n- W6: BM25 baseline was added late\n- W7: **Learnable temperature confound** — StructFuseEncoder has learnable log_temperature; different strategies may converge to different temperatures, confounding the comparison\n- W8: **Positive weight by dataflow distance** — pos_weight = exp(-alpha * dist) means dataflow strategy differs from others in both negatives AND positive weighting; this factor is not isolated\n- W9: Checkpoint selection criterion may differ across tables\n\n**Key Questions:**\n- What learned temperatures did each strategy converge to?\n- Was actual SWE-bench harness used or placeholder?\n- Is stratified analysis computed on matched instance sets?\n- Were any seeds discarded?\n- Why not restrict evaluation to structural-only subset?\n- What is pos_weight for random strategy?\n\n## Your Task\n\nAfter reading R1's review:\n1. **Do you agree or disagree** with R1's key points? Which ones shifted your thinking?\n2. **Would you change your score?** Why or why not?\n3. **What are the most important shared concerns** between you and R1?\n4. **Any new concerns** raised by R1 that you missed?\n\nKeep your response under 500 words. Focus on what changes (if anything) in your assessment.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "84a67ad1-78ae-4f60-b7d9-8c34fdf1e7e9",
  "isSidechain": false,
  "requestId": "req_011Cb2per4WUJkWVHCqMV1Je",
  "type": "assistant",
  "uuid": "c318f45b-c789-4e42-acc7-ae454577db16",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "ef1befa8-2efd-49dd-aab6-f69049f8448e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TEFvN2Fq7hx89gFL1yAnEW",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4528,
      "cache_read_input_tokens": 62555,
      "output_tokens": 1886,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4528,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1886,
          "cache_read_input_tokens": 62555,
          "cache_creation_input_tokens": 4528,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4528
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

_source line 45 · 2026-05-14T17:03:55.114Z_

<details><summary>↩ Tool result · `toolu_012FUTLjV76G6mSG8vDFHfNW`</summary>

```text


## R1 Response to R2's Review

**Agreements and shifts in thinking:**

R2's W3 (small effect sizes, +2pp R@1) is well-taken and something I underweighted. I focused on whether the experimental methodology was sound but didn't sufficiently flag that even when everything works as designed, the practical gain is marginal. A +2pp improvement on R@1 is within noise range for many downstream applications. This shifted my thinking — the paper's contribution is more diagnostic than prescriptive.

R2's W7 (missing baselines) is a genuine gap I should have pressed harder on. Cross-encoder reranking and in-batch negatives are standard comparisons in the retrieval literature. Their absence weakens the claim that structural mining strategies are the right lever to pull versus simply using a stronger retrieval architecture. I raised BM25 completeness (my W6) but R2's broader baseline critique is stronger.

R2's W6 (CoCoHaNeRe evidence specificity) is fair. I credited the correction as a strength but didn't demand the authors show exactly where in the CoCoHaNeRe pipeline BM25 proxies for embedding similarity. A specific code pointer or citation would move this from assertion to demonstrated finding.

**Disagreements:**

R2's W1 (moderate novelty from combining existing tools) is accurate but I weight it less negatively. Systematic empirical studies that reveal when known techniques fail have value — the finding that dataflow-based mining fails on 50% of encoders is useful precisely because someone had to actually test it. Not every contribution needs to be a new algorithm.

R2's question about whether higher LoRA rank or full fine-tuning would change results is interesting but I consider it out of scope for this paper. The paper's claims are already appropriately conditioned on their setup.

**Shared critical concerns:**

1. **n=2 encoders** — both reviews flag this as the most damaging limitation. Two encoders cannot support any mechanistic or generalizable claim about encoder-mining interactions.
2. **Dataflow fragility** — my W1 (66% fallback) and R2's W5 (50% encoder failure) converge: the structural signal the paper is built around doesn't reliably work.
3. **Practical impact** — my pool-size concern (W4) and R2's effect-size concern (W3) both point to the same issue: it's unclear this matters in realistic settings.

**New concerns from R2 I missed:**

R2's question about whether negative difficulty quartile assignments remain valid after training is sharp. If training shifts the embedding space such that "hard" negatives at init become "easy" post-training, the static quartile analysis in the paper is misleading. This is a legitimate confound I overlooked.

R2's 34% structural coverage concern (W8) also deserves more weight — if two-thirds of the codebase lacks structural edges, the method's applicability is fundamentally capped.

**Score update:**

I maintain **4/6 (Weak Accept)** but with reduced confidence. The convergence between both reviews on n=2 encoders, small effect sizes, and dataflow fragility suggests these are robust concerns, not idiosyncratic readings. The paper remains a competent empirical study with honest framing, but the gap between its methodological ambition and its practical impact is wider than I initially assessed. If the authors cannot address the n=2 limitation in revision, I would lean toward 3/6.

agentId: a700647a3a3ffc9a8 (use SendMessage with to: 'a700647a3a3ffc9a8' to continue this agent)
&lt;usage>total_tokens: 16970
tool_uses: 1
duration_ms: 27349&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "84a67ad1-78ae-4f60-b7d9-8c34fdf1e7e9",
  "isSidechain": false,
  "promptId": "0dbd644e-3638-4b84-b174-ff7865af1dfb",
  "type": "user",
  "uuid": "dc4012c8-21c4-4b33-850d-9a8d0b83e722",
  "toolUseResult": {
    "status": "completed",
    "prompt": "You are **Reviewer 1 (R1)**, focused on Methods & Experiments. You have already submitted your independent review. Now you are reading Reviewer 2's review and must respond with any updates to your assessment.\n\n## Your Original Review (R1)\n\n**Overall Score:** 4/6 (Weak Accept) | **Soundness:** 3/5 | **Confidence:** 4/5\n\n**Key Strengths:** 9-seed replication, comprehensive ablation battery, dual-benchmark consistency, honest conditional framing, representation geometry analysis, correcting CoCoHaNeRe.\n\n**Key Weaknesses:**\n- W1: 66% fallback dilution confound in dataflow\n- W2: n=2 encoders insufficient for interaction claim\n- W3: Static negative mining confound (but ablation shows negligible difference)\n- W4: Pool size 50 unrealistically small (but Table 12 shows stability at 500)\n- W5: SWE-bench Lite evaluation gaps (300 instances, single agent, possible placeholder)\n- W6: BM25 baseline completeness concerns\n- W7: Learnable temperature confound\n- W8: Positive weight by dataflow distance confound\n- W9: Checkpoint selection criterion ambiguity\n\n## Reviewer 2's Review (R2: Novelty & Related Work)\n\n**Overall Score:** 4/6 (Weak Accept) | **Novelty:** 3/5 | **Confidence:** 4/5\n\n**Key Strengths:**\n- S1: CoCoHaNeRe correction is genuine contribution\n- S2: Honest, well-calibrated claims\n- S3: Comprehensive ablation suite\n- S4: Stratified analysis well-designed\n- S5: Representation geometry adds depth\n- S6: SWE-bench with bootstrap CIs\n\n**Key Weaknesses:**\n- W1: Moderate novelty — combines existing tools\n- W2: n=2 encoders limits mechanistic claims\n- W3: Small effect sizes (+2pp R@1) throughout\n- W4: Some results may be projected rather than measured\n- W5: Dataflow fails on 50% of encoders; universal finding is \"use embedding mining\" which is not novel\n- W6: CoCoHaNeRe \"mislabeling\" claim needs stronger evidence (specific citations/code)\n- W7: Missing baselines (cross-encoder reranking, curriculum mining, in-batch negatives, SweRank/SWE-Fixer)\n- W8: 34% structural coverage is a practical limitation\n\n**Key Questions:**\n- Can CoCoHaNeRe BM25-proxy usage be specifically cited?\n- BM25 vs embedding negative overlap?\n- Does neg difficulty quartile assignment remain valid after training?\n- Would higher LoRA rank or full fine-tuning change the dynamic mining result?\n- Would 10K-50K instances further separate strategies?\n- Sensitivity to agent choice in SWE-bench?\n- Are overfitting dynamics confounding mining strategy effects?\n\n## Your Task\n\nAfter reading R2's review:\n1. **Do you agree or disagree** with R2's key points? Which ones shifted your thinking?\n2. **Would you change your score?** Why or why not?\n3. **What are the most important shared concerns** between you and R2?\n4. **Any new concerns** raised by R2 that you missed?\n\nKeep your response under 500 words. Focus on what changes (if anything) in your assessment.\n",
    "agentId": "a700647a3a3ffc9a8",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "\n\n## R1 Response to R2's Review\n\n**Agreements and shifts in thinking:**\n\nR2's W3 (small effect sizes, +2pp R@1) is well-taken and something I underweighted. I focused on whether the experimental methodology was sound but didn't sufficiently flag that even when everything works as designed, the practical gain is marginal. A +2pp improvement on R@1 is within noise range for many downstream applications. This shifted my thinking — the paper's contribution is more diagnostic than prescriptive.\n\nR2's W7 (missing baselines) is a genuine gap I should have pressed harder on. Cross-encoder reranking and in-batch negatives are standard comparisons in the retrieval literature. Their absence weakens the claim that structural mining strategies are the right lever to pull versus simply using a stronger retrieval architecture. I raised BM25 completeness (my W6) but R2's broader baseline critique is stronger.\n\nR2's W6 (CoCoHaNeRe evidence specificity) is fair. I credited the correction as a strength but didn't demand the authors show exactly where in the CoCoHaNeRe pipeline BM25 proxies for embedding similarity. A specific code pointer or citation would move this from assertion to demonstrated finding.\n\n**Disagreements:**\n\nR2's W1 (moderate novelty from combining existing tools) is accurate but I weight it less negatively. Systematic empirical studies that reveal when known techniques fail have value — the finding that dataflow-based mining fails on 50% of encoders is useful precisely because someone had to actually test it. Not every contribution needs to be a new algorithm.\n\nR2's question about whether higher LoRA rank or full fine-tuning would change results is interesting but I consider it out of scope for this paper. The paper's claims are already appropriately conditioned on their setup.\n\n**Shared critical concerns:**\n\n1. **n=2 encoders** — both reviews flag this as the most damaging limitation. Two encoders cannot support any mechanistic or generalizable claim about encoder-mining interactions.\n2. **Dataflow fragility** — my W1 (66% fallback) and R2's W5 (50% encoder failure) converge: the structural signal the paper is built around doesn't reliably work.\n3. **Practical impact** — my pool-size concern (W4) and R2's effect-size concern (W3) both point to the same issue: it's unclear this matters in realistic settings.\n\n**New concerns from R2 I missed:**\n\nR2's question about whether negative difficulty quartile assignments remain valid after training is sharp. If training shifts the embedding space such that \"hard\" negatives at init become \"easy\" post-training, the static quartile analysis in the paper is misleading. This is a legitimate confound I overlooked.\n\nR2's 34% structural coverage concern (W8) also deserves more weight — if two-thirds of the codebase lacks structural edges, the method's applicability is fundamentally capped.\n\n**Score update:**\n\nI maintain **4/6 (Weak Accept)** but with reduced confidence. The convergence between both reviews on n=2 encoders, small effect sizes, and dataflow fragility suggests these are robust concerns, not idiosyncratic readings. The paper remains a competent empirical study with honest framing, but the gap between its methodological ambition and its practical impact is wider than I initially assessed. If the authors cannot address the n=2 limitation in revision, I would lean toward 3/6."
      }
    ],
    "totalDurationMs": 27349,
    "totalTokens": 16970,
    "totalToolUseCount": 1,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1285,
      "cache_read_input_tokens": 14885,
      "output_tokens": 797,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1285
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 797,
          "cache_read_input_tokens": 14885,
          "cache_creation_input_tokens": 1285,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1285,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 0,
      "searchCount": 0,
      "bashCount": 0,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 1
    }
  },
  "sourceToolAssistantUUID": "84a67ad1-78ae-4f60-b7d9-8c34fdf1e7e9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "ef1befa8-2efd-49dd-aab6-f69049f8448e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-14T17:04:20.157Z_

<details><summary>↩ Tool result · `toolu_01GTwchWeJRsWreLqaxKJx8p`</summary>

```text
Now I have thorough context on the project. Here is my R2 response to R1's review:

---

**R2 Response to R1's Review**

**Points of Agreement**

R1's W1 (66% fallback dilution) is the most significant finding I missed. My W5 flagged that dataflow fails on 50% of encoders, but R1 traced this deeper: the dataflow strategy is actually a *mixture* of dataflow (34%) and fallback negatives (66%). This substantially undermines the clean comparison the paper claims. If the "dataflow" condition is majority non-dataflow, any measured delta is attenuated by design, making both positive and null results harder to interpret. I should have caught this from the 34% structural coverage figure I noted in W8, but I failed to connect it to the experimental design confound.

R1's W7 (learnable temperature) and W8 (pos_weight by dataflow distance) are genuine confounds I overlooked entirely. If different strategies converge to different learned temperatures, the comparison is not apples-to-apples. The pos_weight issue is especially concerning: the dataflow strategy differs from others in *both* negative selection and positive weighting, meaning any observed effect cannot be cleanly attributed to the negative mining signal alone. These are not fatal but demand ablation or at minimum reporting of converged temperature values per strategy.

I agree with R1 on W2 (n=2 encoders). We both flagged this independently, which strengthens the concern. The project's own decision log (D028) acknowledges this and proposes downgrading Claim 2 to an "observation," which is appropriate.

**Points of Disagreement**

R1's W5 (SWE-bench placeholder code) needs resolution but may be less severe than implied. The project has an active SWE-bench evaluation plan (plan_003) and bootstrap CIs are planned. I would not weight this as heavily until confirmed as an actual placeholder rather than incomplete scaffolding.

R1's W4 (pool=50) aligns with my assessment but the project already has plan_019 for pool size sensitivity. This is a known gap with a planned fix.

**Score Revision**

I would revise my score **down by 0.5 to 3.5/6 (borderline Weak Reject/Weak Accept)**. The three new confounds from R1 (learnable temperature, pos_weight asymmetry, 66% fallback dilution reframed as a mixture-strategy confound rather than just coverage limitation) collectively weaken the experimental isolation more than I initially assessed. Combined with our shared concern on n=2 encoders, the paper's causal claims rest on insufficiently controlled comparisons.

**Most Important Shared Concerns**

1. **n=2 encoders** — insufficient for the encoder-strategy interaction mechanism claim
2. **Dataflow strategy is not purely dataflow** — whether framed as 66% fallback (R1) or 34% coverage (R2), the claimed comparison is diluted
3. **Small effect sizes** — 1.6-2.0pp deltas with multiple uncontrolled confounds
4. **Missing baselines** — BM25 is critical for the CoCoHaNeRe correction narrative (plan_018 in progress but not yet available)

**New Concerns from R1**

The learnable temperature confound (W7) and pos_weight asymmetry (W8) are the most important additions. These are isolable confounds that could be addressed with targeted ablations, but without them, the current experimental design cannot attribute observed differences solely to negative mining strategy. I am adding these to my concern list.

agentId: a28fd0c26168dc95b (use SendMessage with to: 'a28fd0c26168dc95b' to continue this agent)
&lt;usage>total_tokens: 35992
tool_uses: 6
duration_ms: 40831&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c318f45b-c789-4e42-acc7-ae454577db16",
  "isSidechain": false,
  "promptId": "0dbd644e-3638-4b84-b174-ff7865af1dfb",
  "type": "user",
  "uuid": "767d2866-9feb-4118-8f37-9d25e86aa1c2",
  "toolUseResult": {
    "status": "completed",
    "prompt": "You are **Reviewer 2 (R2)**, focused on Novelty & Related Work. You have already submitted your independent review. Now you are reading Reviewer 1's review and must respond with any updates to your assessment.\n\n## Your Original Review (R2)\n\n**Overall Score:** 4/6 (Weak Accept) | **Novelty:** 3/5 | **Confidence:** 4/5\n\n**Key Strengths:** CoCoHaNeRe correction, honest claims, comprehensive ablations, stratified analysis, representation geometry, SWE-bench bootstrap CIs.\n\n**Key Weaknesses:**\n- W1: Moderate novelty (combines existing tools)\n- W2: n=2 encoders limits mechanistic claims\n- W3: Small effect sizes\n- W4: Some results may be projected\n- W5: Dataflow fails on 50% of encoders\n- W6: CoCoHaNeRe mislabeling needs stronger evidence\n- W7: Missing baselines\n- W8: 34% structural coverage limitation\n\n## Reviewer 1's Review (R1: Methods & Experiments)\n\n**Overall Score:** 4/6 (Weak Accept) | **Soundness:** 3/5 | **Confidence:** 4/5\n\n**Key Strengths:**\n- S1: 9-seed replication above community norm\n- S2: Comprehensive ablation battery\n- S3: Dual-benchmark consistency\n- S4: Honest conditional framing\n- S5: Mechanistic depth via quartile analysis\n- S6: Correcting CoCoHaNeRe\n\n**Key Weaknesses (methodological, from code inspection):**\n- W1: 66% fallback dilution confound — dataflow strategy is actually a mixture of strategies\n- W2: n=2 encoders insufficient for interaction claim\n- W3: Static negative mining — ablation may be underpowered\n- W4: Pool=50 unrealistically small\n- W5: SWE-bench evaluation has possible placeholder code in eval_swebench.py\n- W6: BM25 baseline was added late\n- W7: **Learnable temperature confound** — StructFuseEncoder has learnable log_temperature; different strategies may converge to different temperatures, confounding the comparison\n- W8: **Positive weight by dataflow distance** — pos_weight = exp(-alpha * dist) means dataflow strategy differs from others in both negatives AND positive weighting; this factor is not isolated\n- W9: Checkpoint selection criterion may differ across tables\n\n**Key Questions:**\n- What learned temperatures did each strategy converge to?\n- Was actual SWE-bench harness used or placeholder?\n- Is stratified analysis computed on matched instance sets?\n- Were any seeds discarded?\n- Why not restrict evaluation to structural-only subset?\n- What is pos_weight for random strategy?\n\n## Your Task\n\nAfter reading R1's review:\n1. **Do you agree or disagree** with R1's key points? Which ones shifted your thinking?\n2. **Would you change your score?** Why or why not?\n3. **What are the most important shared concerns** between you and R1?\n4. **Any new concerns** raised by R1 that you missed?\n\nKeep your response under 500 words. Focus on what changes (if anything) in your assessment.\n",
    "agentId": "a28fd0c26168dc95b",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Now I have thorough context on the project. Here is my R2 response to R1's review:\n\n---\n\n**R2 Response to R1's Review**\n\n**Points of Agreement**\n\nR1's W1 (66% fallback dilution) is the most significant finding I missed. My W5 flagged that dataflow fails on 50% of encoders, but R1 traced this deeper: the dataflow strategy is actually a *mixture* of dataflow (34%) and fallback negatives (66%). This substantially undermines the clean comparison the paper claims. If the \"dataflow\" condition is majority non-dataflow, any measured delta is attenuated by design, making both positive and null results harder to interpret. I should have caught this from the 34% structural coverage figure I noted in W8, but I failed to connect it to the experimental design confound.\n\nR1's W7 (learnable temperature) and W8 (pos_weight by dataflow distance) are genuine confounds I overlooked entirely. If different strategies converge to different learned temperatures, the comparison is not apples-to-apples. The pos_weight issue is especially concerning: the dataflow strategy differs from others in *both* negative selection and positive weighting, meaning any observed effect cannot be cleanly attributed to the negative mining signal alone. These are not fatal but demand ablation or at minimum reporting of converged temperature values per strategy.\n\nI agree with R1 on W2 (n=2 encoders). We both flagged this independently, which strengthens the concern. The project's own decision log (D028) acknowledges this and proposes downgrading Claim 2 to an \"observation,\" which is appropriate.\n\n**Points of Disagreement**\n\nR1's W5 (SWE-bench placeholder code) needs resolution but may be less severe than implied. The project has an active SWE-bench evaluation plan (plan_003) and bootstrap CIs are planned. I would not weight this as heavily until confirmed as an actual placeholder rather than incomplete scaffolding.\n\nR1's W4 (pool=50) aligns with my assessment but the project already has plan_019 for pool size sensitivity. This is a known gap with a planned fix.\n\n**Score Revision**\n\nI would revise my score **down by 0.5 to 3.5/6 (borderline Weak Reject/Weak Accept)**. The three new confounds from R1 (learnable temperature, pos_weight asymmetry, 66% fallback dilution reframed as a mixture-strategy confound rather than just coverage limitation) collectively weaken the experimental isolation more than I initially assessed. Combined with our shared concern on n=2 encoders, the paper's causal claims rest on insufficiently controlled comparisons.\n\n**Most Important Shared Concerns**\n\n1. **n=2 encoders** — insufficient for the encoder-strategy interaction mechanism claim\n2. **Dataflow strategy is not purely dataflow** — whether framed as 66% fallback (R1) or 34% coverage (R2), the claimed comparison is diluted\n3. **Small effect sizes** — 1.6-2.0pp deltas with multiple uncontrolled confounds\n4. **Missing baselines** — BM25 is critical for the CoCoHaNeRe correction narrative (plan_018 in progress but not yet available)\n\n**New Concerns from R1**\n\nThe learnable temperature confound (W7) and pos_weight asymmetry (W8) are the most important additions. These are isolable confounds that could be addressed with targeted ablations, but without them, the current experimental design cannot attribute observed differences solely to negative mining strategy. I am adding these to my concern list."
      }
    ],
    "totalDurationMs": 40831,
    "totalTokens": 35992,
    "totalToolUseCount": 6,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13857,
      "cache_read_input_tokens": 21292,
      "output_tokens": 842,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 13857
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 842,
          "cache_read_input_tokens": 21292,
          "cache_creation_input_tokens": 13857,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 13857,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 0,
      "searchCount": 0,
      "bashCount": 0,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 6
    }
  },
  "sourceToolAssistantUUID": "c318f45b-c789-4e42-acc7-ae454577db16",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "ef1befa8-2efd-49dd-aab6-f69049f8448e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 47_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[DREAM Review Director] dream_id=20260514T162530 | review_mode=full | review_visible=True PDF: /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream…",
  "leafUuid": "767d2866-9feb-4118-8f37-9d25e86aa1c2",
  "sessionId": "ef1befa8-2efd-49dd-aab6-f69049f8448e"
}
```

---

### Runtime record

_source line 48_

```json
{
  "type": "ai-title",
  "aiTitle": "Review ML research paper with full evaluation",
  "sessionId": "ef1befa8-2efd-49dd-aab6-f69049f8448e"
}
```

---

### Assistant

_source line 49 · 2026-05-14T17:04:29.099Z_

<details><summary>Logged reasoning block</summary>

```text
Step 2 (cross-sharing) is done. Now I need to do Step 3 (convergence) and Step 4 (synthesize the final report). Let me synthesize all the information into a final consolidated review report and submit it.

Let me now compile the full roundtable review report and submit it via `submit_dream_review_report`.

Key convergence points:
- Both reviewers: 4/6 Weak Accept (R2 revised to ~3.5/6 after cross-review)


- The n=2 encoders emerge as the most damaging limitation, with both reviewers flagging the dataflow fragility from the 66% fallback rate and 50% encoder failure rate
- Small effect sizes are a consistent concern, and R1's discovery of implementation confounds like learnable temperature and pos_weight asymmetry turned out to be significant issues that R2 confirmed
- R2's points about moderate novelty and missing baselines align with R1's assessment

The consensus leans toward a borderline Weak Accept at 4/6, though it could tip toward Weak Reject. Now I'll write and submit the full report.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "767d2866-9feb-4118-8f37-9d25e86aa1c2",
  "isSidechain": false,
  "requestId": "req_011Cb2pkSSNFuPcsxvbri3b4",
  "type": "assistant",
  "uuid": "3fa5cc77-8999-4e87-9dfb-d1047818a99e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "ef1befa8-2efd-49dd-aab6-f69049f8448e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Kx7hc7JyvoJjNDmVJADokU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3729,
      "cache_read_input_tokens": 67083,
      "output_tokens": 417,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3729,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 417,
          "cache_read_input_tokens": 67083,
          "cache_creation_input_tokens": 3729,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3729
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

_source line 50 · 2026-05-14T17:04:29.252Z_

Step 2（交叉分享）完成。两位 Reviewer 交换意见后，R1 维持 4/6，R2 下调至 ~3.5/6。现在进入 Step 3-4：收敛与综合。

Let me load the submit tool and compile the final report.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3fa5cc77-8999-4e87-9dfb-d1047818a99e",
  "isSidechain": false,
  "requestId": "req_011Cb2pkSSNFuPcsxvbri3b4",
  "type": "assistant",
  "uuid": "c2e98c06-d9c4-4793-8f87-f97ae29dff6c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "ef1befa8-2efd-49dd-aab6-f69049f8448e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Kx7hc7JyvoJjNDmVJADokU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3729,
      "cache_read_input_tokens": 67083,
      "output_tokens": 417,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3729,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 417,
          "cache_read_input_tokens": 67083,
          "cache_creation_input_tokens": 3729,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3729
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

_source line 51 · 2026-05-14T17:04:29.437Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_014km7VFizuyfppm7pwdfSaZ`</summary>

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
  "parentUuid": "c2e98c06-d9c4-4793-8f87-f97ae29dff6c",
  "isSidechain": false,
  "requestId": "req_011Cb2pkSSNFuPcsxvbri3b4",
  "type": "assistant",
  "uuid": "5438014f-df5e-4368-adb1-904a0680de71",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "ef1befa8-2efd-49dd-aab6-f69049f8448e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Kx7hc7JyvoJjNDmVJADokU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3729,
      "cache_read_input_tokens": 67083,
      "output_tokens": 417,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3729,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 417,
          "cache_read_input_tokens": 67083,
          "cache_creation_input_tokens": 3729,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3729
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

_source line 52 · 2026-05-14T17:04:29.453Z_

<details><summary>↩ Tool result · `toolu_014km7VFizuyfppm7pwdfSaZ`</summary>

```text
No matching deferred tools found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5438014f-df5e-4368-adb1-904a0680de71",
  "isSidechain": false,
  "promptId": "0dbd644e-3638-4b84-b174-ff7865af1dfb",
  "type": "user",
  "uuid": "6823551f-c80d-4e8c-8c74-139a62008bbe",
  "toolUseResult": {
    "matches": [],
    "query": "select:submit_dream_review_report",
    "total_deferred_tools": 23
  },
  "sourceToolAssistantUUID": "5438014f-df5e-4368-adb1-904a0680de71",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "ef1befa8-2efd-49dd-aab6-f69049f8448e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-14T17:04:33.034Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01QuBDgmE6GAg4cVeK3KKqqB`</summary>

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
  "parentUuid": "6823551f-c80d-4e8c-8c74-139a62008bbe",
  "isSidechain": false,
  "requestId": "req_011Cb2pm86pzLzUSamG3vPrS",
  "type": "assistant",
  "uuid": "95dff6c1-0dda-47a6-84d2-f28f359a2ab1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "ef1befa8-2efd-49dd-aab6-f69049f8448e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TbdSMNVrAEAHf582bzJCqj",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 435,
      "cache_read_input_tokens": 70812,
      "output_tokens": 89,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 435,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 89,
          "cache_read_input_tokens": 70812,
          "cache_creation_input_tokens": 435,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 435
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

_source line 54 · 2026-05-14T17:04:33.038Z_

<details><summary>↩ Tool result · `toolu_01QuBDgmE6GAg4cVeK3KKqqB`</summary>

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
  "parentUuid": "95dff6c1-0dda-47a6-84d2-f28f359a2ab1",
  "isSidechain": false,
  "promptId": "0dbd644e-3638-4b84-b174-ff7865af1dfb",
  "type": "user",
  "uuid": "af25f740-ed01-4dfa-8fdd-6b271886f56a",
  "toolUseResult": {
    "matches": [
      "mcp__agent-ml-research__submit_dream_review_report"
    ],
    "query": "select:mcp__agent-ml-research__submit_dream_review_report",
    "total_deferred_tools": 23
  },
  "sourceToolAssistantUUID": "95dff6c1-0dda-47a6-84d2-f28f359a2ab1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "ef1befa8-2efd-49dd-aab6-f69049f8448e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 55 · 2026-05-14T17:04:36.446Z_

Now compiling the consolidated roundtable report.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "af25f740-ed01-4dfa-8fdd-6b271886f56a",
  "isSidechain": false,
  "requestId": "req_011Cb2pmPQL51V3UYnRbEqkt",
  "type": "assistant",
  "uuid": "a87291e1-820e-4696-b764-a27ecbb07bf0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "ef1befa8-2efd-49dd-aab6-f69049f8448e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CbvgPX1iUFU85LFQqzJ8XF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 667,
      "cache_read_input_tokens": 71247,
      "output_tokens": 3619,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 667,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 3619,
          "cache_read_input_tokens": 71247,
          "cache_creation_input_tokens": 667,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 667
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

_source line 56 · 2026-05-14T17:05:54.334Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_dream_review_report · `toolu_01PiALj8gxbzz73as8gpVLPx`</summary>

```json
{
  "report": "# Dream Review Report: StructFuse-Context\n\n**Paper:** \"What Makes Hard Negatives Work for Code Retrieval? A Systematic Study of Mining Strategies and Representation Geometry\"\n**Dream ID:** 20260514T162530\n**Review Mode:** Full (2 Reviewers, 4-Step Roundtable)\n**Date:** 2026-05-14\n\n---\n\n## Overall Assessment\n\n**Consensus Score: 4/6 (Weak Accept)**\n\nR1 (Methods & Experiments): 4/6 → 4/6 after cross-review (maintained, but noted would lean 3/6 if n=2 limitation unaddressed)\nR2 (Novelty & Related Work): 4/6 → 3.5/6 after cross-review (downgraded due to implementation confounds identified by R1)\n\nThe paper asks an important question, executes a more systematic comparison than any prior work in code retrieval negative mining, and provides a genuinely useful correction of the CoCoHaNeRe BM25-proxy confusion. The representation geometry analysis adds intellectual depth beyond pure metric comparisons. However, the paper's causal and mechanistic claims rest on insufficiently controlled comparisons (n=2 encoders, learnable temperature confound, pos_weight asymmetry, 66% fallback dilution), and effect sizes are small enough that unresolved confounds could explain the observed deltas.\n\n---\n\n## Step 1: Independent Reviews\n\n### R1 (Methods & Experiments) — Score: 4/6, Soundness: 3/5, Confidence: 4/5\n\n**Strengths:**\n- S1: 9-seed replication with 95% CIs is well above community norm (typically 3-5 seeds)\n- S2: Comprehensive ablation battery (Tables 8-15) covering temperature, hop depth, data scaling, fusion head, pool size, static/dynamic mining, weighted/binary dataflow, failure analysis\n- S3: Dual-benchmark consistency (SWE-smith + RepoBench-R) with consistent strategy orderings\n- S4: Honest conditional framing of Claim 2 — dataflow benefit not overclaimed\n- S5: Representation geometry analysis via neg difficulty quartiles adds mechanistic explanatory depth (Q1→Q4 monotonic scaling)\n- S6: Correcting CoCoHaNeRe's BM25-proxy conflation is a service to the community\n\n**Weaknesses:**\n- W1: **66% fallback dilution confound.** The dataflow strategy has structural data for only 34% of instances; the rest fall back to embedding/random. The \"dataflow\" condition is actually a *mixture* of strategies, making the reported +1.0pp (Qwen) a diluted signal. Table 1 reports this mixture as the headline rather than the stratified +2.8pp.\n- W2: **n=2 encoders insufficient for interaction claim.** The mechanistic story (representation saturation mediates dataflow benefit) is inferred from exactly 2 data points. Any two-encoder comparison yields some difference; post-hoc explanation is always available.\n- W3: **Learnable temperature confound.** The model has a learnable `log_temperature` parameter. Different strategies may converge to different temperatures, confounding the comparison. The temperature ablation (Table 8) fixes initial temperature but does not report learned values.\n- W4: **Positive weight by dataflow distance.** `pos_weight = exp(-alpha * dist)` means the dataflow strategy differs from others in both negatives AND positive weighting — two confounded factors.\n- W5: **Pool=50 in main experiments is unrealistically small.** Table 12 shows stability at pool=500, but headline metrics at pool=50 inflate absolute R@1 and may inflate deltas.\n- W6: **SWE-bench Lite evaluation gaps.** Only 300 instances with single agent model. Bootstrap CIs are wide (~3.6pp). Dataflow-vs-embedding not significant (p=0.134).\n- W7: **Static mining confound** partially addressed by Table 13 ablation (negligible difference), but ablation may be underpowered.\n- W8: **BM25 baseline completeness.** Claim 1's strength depends entirely on BM25 performing distinctly worse than random.\n- W9: **Checkpoint selection criterion ambiguity.** Internal records flag that rankings change depending on best-val-loss vs best-R@1.\n\n**Key Questions for Authors:**\n- Q1: What learned temperature values did each strategy converge to across 9 seeds?\n- Q2: Was the actual SWE-bench harness used for test execution?\n- Q3: Is stratified analysis (Table 6) computed on matched instance sets across all strategies?\n- Q4: Were any of the 9 seeds discarded?\n- Q5: What is `pos_weight` for the random strategy? If `pos_dataflow_distance` defaults to 1.0, then `pos_weight = exp(-1.0) = 0.37` for all random samples — is this intentional?\n\n---\n\n### R2 (Novelty & Related Work) — Score: 4/6, Novelty: 3/5, Confidence: 4/5\n\n**Strengths:**\n- S1: CoCoHaNeRe correction is the strongest and most novel claim — the BM25 < random < embedding ordering is a clean corrective finding\n- S2: Claims are unusually well-calibrated to evidence (conditional framing, explicit limitations)\n- S3: Ablation suite establishes rankings never reverse across any condition tested\n- S4: Representation geometry analysis provides testable prediction for practitioners (check pos_sim before choosing strategy)\n- S5: SWE-bench downstream evaluation with bootstrap significance connects retrieval improvements to practical impact\n\n**Weaknesses:**\n- W1: **Moderate novelty.** Combines existing tools (ANCE-style mining, CodeQL, LoRA) in a new context. The \"systematic study\" contribution is valued but inherently lower novelty than a new method.\n- W2: **n=2 encoders cannot identify the mechanism** behind encoder-strategy interaction. pos_sim saturation is plausible but confounded with architecture, pretraining data, tokenizer, and training objective differences.\n- W3: **Small effect sizes throughout.** +2.0pp R@1 is within the range sensitive to implementation details (learning rate, number of negatives, sequence length) that are not ablated.\n- W4: **Dataflow fails on 50% of encoders tested.** The universal finding is \"use embedding mining,\" which is ANCE (2021) applied to code — not novel.\n- W5: **CoCoHaNeRe \"mislabeling\" claim needs stronger evidence.** Specific citations or code references from CoCoHaNeRe showing BM25 proxy usage are required. Without them, soften from \"correcting misconception\" to \"we observe different results under controlled conditions.\"\n- W6: **Missing baselines.** No comparison with cross-encoder reranking, curriculum-based mining, in-batch negatives, or existing systems (SweRank, SWE-Fixer) on the same benchmark.\n- W7: **34% structural coverage is a significant practical limitation.** For 66% of instances, dataflow adds nothing. Practical recommendation reduces to \"use embedding mining.\"\n\n**Detailed Novelty Assessment:**\n- Claim 1 (CoCoHaNeRe correction): Significance 4/5, Novelty 3/5\n- Claim 2 (Structure-grounded negatives): Significance 3/5, Novelty 3.5/5\n- Claim 3 (Representation geometry): Significance 3/5, Novelty 2.5/5\n\n**Related Work Gaps:**\n- DPR (Karpukhin et al., 2020) deserves more than passing mention\n- ContraCode (Ding et al., ACL Findings 2022) is absent\n- NL retrieval hard negative literature (RocketQA, TAS-B, GPL) should be connected\n- SweRank/SWE-Fixer training methodology comparison would contextualize\n- GraphCodeBERT's dataflow-in-pretraining vs negative-mining distinction deserves deeper analysis\n\n---\n\n## Step 2-3: Cross-Review & Convergence\n\n### Points of Agreement (Both Reviewers)\n\n1. **n=2 encoders is the most damaging limitation.** Both reviewers independently flagged this. The encoder-strategy interaction claim (Claim 2) cannot be supported with 2 data points regardless of how many seeds are run per configuration. This should be explicitly reframed as hypothesis-generating.\n\n2. **Dataflow strategy fragility.** Converging from two angles: R1's \"66% fallback makes it a mixture strategy\" and R2's \"fails on 50% of encoders tested.\" The structure-grounded negative contribution is the paper's claimed novelty, but it is the weakest of the three claims empirically.\n\n3. **Small effect sizes with unresolved confounds.** +1.6-2.0pp R@1 deltas are statistically significant with 9 seeds but practically marginal. Combined with learnable temperature confound (R1-W3), pos_weight asymmetry (R1-W4), and other uncontrolled factors, the causal attribution to mining strategy alone is not airtight.\n\n4. **CoCoHaNeRe correction is the paper's strongest contribution** but needs ironclad documentation of the BM25-proxy claim.\n\n5. **Paper is well-executed within its scope** — honest framing, extensive ablations, good statistical practice. The issue is scope, not execution quality.\n\n### Points of Divergence\n\n1. **Novelty weighting.** R1 is more forgiving of \"systematic study\" contributions; R2 weighs novelty more heavily and notes the universal recommendation (\"use embedding mining\") is essentially ANCE for code.\n\n2. **Score after cross-review.** R1 maintains 4/6; R2 drops to ~3.5/6 after learning about the learnable temperature and pos_weight confounds from R1. These implementation-level concerns shifted R2's assessment of experimental soundness.\n\n---\n\n## Step 4: Consolidated Recommendations\n\n### For Authors (Revision Priorities)\n\n**Critical (must address):**\n1. **Resolve the learnable temperature confound.** Report converged temperature values per strategy per seed. If they differ systematically, either (a) fix temperature as a non-learnable hyperparameter in all comparisons, or (b) demonstrate that the learned temperature differences do not explain the R@1 deltas.\n2. **Isolate pos_weight from negative mining.** Run dataflow_aware with pos_weight_alpha=0 (uniform weighting) to demonstrate the benefit comes from negative selection, not positive reweighting.\n3. **Document the CoCoHaNeRe BM25-proxy claim with specific evidence.** Cite the exact methodology section, code, or author communication confirming BM25 was used as embedding-distance proxy.\n4. **Reframe Claim 2 as hypothesis, not mechanism.** n=2 encoders cannot validate the \"representation saturation mediates dataflow benefit\" story. Present it as a plausible explanation with a testable prediction.\n\n**Important (strongly recommended):**\n5. **Report main results at a more realistic pool size** (e.g., pool=200) alongside pool=50.\n6. **Add restricted-to-structural-subset comparison.** Report all 4 strategies on only the 34% of instances with CodeQL data — eliminates fallback dilution.\n7. **Strengthen SWE-bench evaluation.** Use SWE-bench Verified (500 instances) or add a second agent model.\n8. **Add missing related work.** DPR, ContraCode, RocketQA/TAS-B connections.\n\n**Nice to have:**\n9. Add 1-2 more encoders (especially one encoder-only model) to strengthen the interaction claim.\n10. Compare with curriculum-based mining or in-batch negatives.\n11. Report training dynamics (loss curves, R@1 over steps) per strategy.\n\n### Experiment Coverage Assessment\n\nAll 15 imagined experiments from `review_context.yaml` are present in the paper:\n- ✅ SWE-bench Lite (plan_003) → Tables 2-4\n- ✅ RepoBench-R (plan_004) → Table 5\n- ✅ Stratified Analysis (plan_005) → Tables 6-7\n- ✅ Hop Depth Ablation (plan_007) → Table 9\n- ✅ Data Size Scaling (plan_008) → Table 10\n- ✅ Fusion Head Ablation (plan_009) → Table 11\n- ✅ Weighted vs Binary (plan_010) → Table 14\n- ✅ Failure Analysis (plan_011) → Table 15\n- ✅ Qualitative Examples (plan_012) → Django example in §4.7\n- ✅ Temperature Ablation (plan_014) → Table 8\n- ✅ Dynamic vs Static (plan_015) → Table 13\n- ✅ Bootstrap CIs (plan_016) → Table 3\n- ✅ Literature Comparison (plan_017) → Table 16\n- ✅ BM25 Baseline (plan_018) → Table 1\n- ✅ Pool Size Sensitivity (plan_019) → Table 12\n\nCoverage: **15/15 (100%)**. The paper is remarkably comprehensive in executing the experimental plan. The issues are not about missing experiments but about uncontrolled confounds within the executed experiments.\n\n### Summary Verdict\n\nA thorough and honestly-framed empirical study that asks the right question and provides useful findings — particularly the CoCoHaNeRe BM25-proxy correction and the practical recommendation to use true embedding-distance mining. The ablation suite is exemplary. However, the paper's most novel contribution (structure-grounded negatives) is its weakest empirical result, and several implementation confounds (learnable temperature, pos_weight asymmetry) prevent clean causal attribution. The mechanistic claim (Claim 2) is underpowered at n=2 encoders. With targeted revisions addressing the confounds and reframing the interaction claim, this would be a solid empirical contribution to the code retrieval literature.\n\n**Final Consensus: 4/6 (Weak Accept) — conditional on addressing the critical revision items above.**\n",
  "project": "structfuse-context",
  "tier": "best",
  "dream_id": "20260514T162530",
  "overall_score": "4/6 Weak Accept",
  "review_visible": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a87291e1-820e-4696-b764-a27ecbb07bf0",
  "isSidechain": false,
  "requestId": "req_011Cb2pmPQL51V3UYnRbEqkt",
  "type": "assistant",
  "uuid": "d7b47af6-7050-45f3-811e-591a9128b890",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "ef1befa8-2efd-49dd-aab6-f69049f8448e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CbvgPX1iUFU85LFQqzJ8XF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 667,
      "cache_read_input_tokens": 71247,
      "output_tokens": 3619,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 667,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 3619,
          "cache_read_input_tokens": 71247,
          "cache_creation_input_tokens": 667,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 667
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

_source line 57 · 2026-05-14T17:05:55.080Z_

<details><summary>↩ Tool result · `toolu_01PiALj8gxbzz73as8gpVLPx`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"report_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T162530/best/review_report.md\", \"dream_id\": \"dream_20260514T162530\", \"tier\": \"best\", \"review_visible\": true}, \"error\": \"\"}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d7b47af6-7050-45f3-811e-591a9128b890",
  "isSidechain": false,
  "promptId": "0dbd644e-3638-4b84-b174-ff7865af1dfb",
  "type": "user",
  "uuid": "31e3396e-e987-44ed-951e-b8a6ef3c2b09",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"report_path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T162530/best/review_report.md\\\", \\\"dream_id\\\": \\\"dream_20260514T162530\\\", \\\"tier\\\": \\\"best\\\", \\\"review_visible\\\": true}, \\\"error\\\": \\\"\\\"}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"report_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T162530/best/review_report.md\", \"dream_id\": \"dream_20260514T162530\", \"tier\": \"best\", \"review_visible\": true}, \"error\": \"\"}"
    }
  },
  "sourceToolAssistantUUID": "d7b47af6-7050-45f3-811e-591a9128b890",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "ef1befa8-2efd-49dd-aab6-f69049f8448e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 58 · 2026-05-14T17:06:02.837Z_

审稿完成。

**最终评分：4/6 (Weak Accept)**

核心结论：
- **最强贡献**：纠正 CoCoHaNeRe 的 BM25-proxy 混淆，4-strategy ordering (BM25 < random < dataflow ≤ embedding) 是 clean corrective finding
- **最弱贡献**：structure-grounded negatives——仅在 50% encoder 上有效，且 66% instance 无结构数据需 fallback
- **关键共识缺陷**：n=2 encoder 无法支撑机制性声明；learnable temperature 和 pos_weight 非对称性构成未隔离的 confounds；效应量偏小（+2pp R@1）
- **实验覆盖度**：15/15 想象实验全部到位，执行质量高，问题在于 confound isolation 而非实验缺失

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "31e3396e-e987-44ed-951e-b8a6ef3c2b09",
  "isSidechain": false,
  "requestId": "req_011Cb2psRtKa7TitD1j7Stgv",
  "type": "assistant",
  "uuid": "8477c54b-7067-4572-8eac-beae980bb770",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "ef1befa8-2efd-49dd-aab6-f69049f8448e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UB9nG17z7GTLbLUtyk2RKV",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3746,
      "cache_read_input_tokens": 71914,
      "output_tokens": 253,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3746,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 253,
          "cache_read_input_tokens": 71914,
          "cache_creation_input_tokens": 3746,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3746
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

_source line 59_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[DREAM Review Director] dream_id=20260514T162530 | review_mode=full | review_visible=True PDF: /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream…",
  "leafUuid": "8477c54b-7067-4572-8eac-beae980bb770",
  "sessionId": "ef1befa8-2efd-49dd-aab6-f69049f8448e"
}
```

---

### Runtime record

_source line 60_

```json
{
  "type": "ai-title",
  "aiTitle": "Review ML research paper with full evaluation",
  "sessionId": "ef1befa8-2efd-49dd-aab6-f69049f8448e"
}
```

---
