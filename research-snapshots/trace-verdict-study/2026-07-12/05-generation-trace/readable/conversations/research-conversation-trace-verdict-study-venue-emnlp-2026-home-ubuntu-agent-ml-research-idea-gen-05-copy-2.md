# Research conversation: 项目：trace-verdict-study Venue：emnlp-2026 论文目录：/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-stud

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 65
- **Recorded user turns:** 1
- **Tool calls:** 19
- **Original source:** `logs/chats/exported-trajectories/account-2/1db729b7-6c37-474e-9cbb-179c13a8aeb8.jsonl`
- **Structured JSON:** [`ffc7baa097fcd4a40556.json`](../../sessions/ff/ffc7baa097fcd4a40556.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-24T16:15:53.549Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-24T16:15:53.549Z",
  "sessionId": "1db729b7-6c37-474e-9cbb-179c13a8aeb8",
  "content": "项目：trace-verdict-study\nVenue：emnlp-2026\n论文目录：/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper\n\nPhase 1 确定性检查结果：\n源码检查: passed=False, 6 critical, 17 warning\n一致性检查: 0 critical, 14 warning\n编译: ✅, 页数: 20\n内部信息: 0 critical, 0 warning\n\n━━━ 用户自定义规则（作为额外检查项）━━━\n## 用户自定义规则（必须遵守）\n### 写作规则\n\n- **[EMNLP 2026]** Limitations 章节只需要写一小段，覆盖 3 个点左右就可以了，不需要写得很长\n- **[EMNLP 2026]** ARR Responsible NLP Checklist在OpenReview的submission form里面（由用户手动填写），而不是在论文pdf里面\n- **[EMNLP 2026]** 一篇文章只能有一个limitations section，放在正文里面，appendix不能有 limitations section\n- **[EMNLP 2026]** abstract 不要超过 200 words\n\n### 审稿规则\n\n- **[EMNLP 2026]** “EMNLP 2026 通过 ARR 统一审稿，Main/Findings 不分开投稿（不是两个Track），Long/Short 也走同一审稿系统，Overall Assessment的评分标准如下：5 = Consider for Award（约前2.5%），4.5 = Borderline Award，4 = Conference（可被主会议接收），3.5 = Borderline Conference，3 = Findings（可被Findings接收），2.5 = Borderline Findings，2 = Resubmit next cycle（需大幅修改，可在下一周期完成），1.5 = Resubmit after next cycle（需大幅修改，无法在下一周期完成），1 = Do not resubmit（需完全重做或与*ACL无关）”\n- **[EMNLP 2026]** EMNLP 2026 restricts long paper submissions to a strict 8-page limit for main text, with unlimited space for references. Mandatory limitations and optional ethical considerations do not count towards this page limit, provided they do not contain excessive additional content.\n\n> 以上规则由用户配置，优先级等同于硬约束。违反会被 Reviewer 标记。\n请将以上规则逐条作为额外审计维度检查。违反的规则用 dimension `[写作规则]` 或 `[审稿规则]` 标记，severity 按实际影响判定。\n\n请按照你的角色指令执行内容结构审计。"
}
```

---

### Runtime record

_source line 2 · 2026-05-24T16:15:53.553Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-24T16:15:53.553Z",
  "sessionId": "1db729b7-6c37-474e-9cbb-179c13a8aeb8"
}
```

---

## Round 1

63 recorded events

### User

_source line 3 · 2026-05-24T16:15:53.597Z_

项目：trace-verdict-study
Venue：emnlp-2026
论文目录：/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper

Phase 1 确定性检查结果：
源码检查: passed=False, 6 critical, 17 warning
一致性检查: 0 critical, 14 warning
编译: ✅, 页数: 20
内部信息: 0 critical, 0 warning

━━━ 用户自定义规则（作为额外检查项）━━━
## 用户自定义规则（必须遵守）
### 写作规则

- **[EMNLP 2026]** Limitations 章节只需要写一小段，覆盖 3 个点左右就可以了，不需要写得很长
- **[EMNLP 2026]** ARR Responsible NLP Checklist在OpenReview的submission form里面（由用户手动填写），而不是在论文pdf里面
- **[EMNLP 2026]** 一篇文章只能有一个limitations section，放在正文里面，appendix不能有 limitations section
- **[EMNLP 2026]** abstract 不要超过 200 words

### 审稿规则

- **[EMNLP 2026]** “EMNLP 2026 通过 ARR 统一审稿，Main/Findings 不分开投稿（不是两个Track），Long/Short 也走同一审稿系统，Overall Assessment的评分标准如下：5 = Consider for Award（约前2.5%），4.5 = Borderline Award，4 = Conference（可被主会议接收），3.5 = Borderline Conference，3 = Findings（可被Findings接收），2.5 = Borderline Findings，2 = Resubmit next cycle（需大幅修改，可在下一周期完成），1.5 = Resubmit after next cycle（需大幅修改，无法在下一周期完成），1 = Do not resubmit（需完全重做或与*ACL无关）”
- **[EMNLP 2026]** EMNLP 2026 restricts long paper submissions to a strict 8-page limit for main text, with unlimited space for references. Mandatory limitations and optional ethical considerations do not count towards this page limit, provided they do not contain excessive additional content.

> 以上规则由用户配置，优先级等同于硬约束。违反会被 Reviewer 标记。
请将以上规则逐条作为额外审计维度检查。违反的规则用 dimension `[写作规则]` 或 `[审稿规则]` 标记，severity 按实际影响判定。

请按照你的角色指令执行内容结构审计。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "96f110f9-4fbd-4295-8cdb-ef5a8ad15d7a",
  "type": "user",
  "uuid": "bb207ad4-d9af-408a-b6ec-3e48d419cf77",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/.claude/sessions/paper_audit_content_b575bb0e",
  "sessionId": "1db729b7-6c37-474e-9cbb-179c13a8aeb8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-24T16:15:53.596Z_

```json
{
  "parentUuid": "bb207ad4-d9af-408a-b6ec-3e48d419cf77",
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
      "mcp__agent-ml-research__load_project_config",
      "mcp__agent-ml-research__read_project_file"
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
      "mcp__agent-ml-research__load_project_config",
      "mcp__agent-ml-research__read_project_file"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "b6091b43-d320-4395-b9c7-6defb080b459",
  "timestamp": "2026-05-24T16:15:53.596Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/.claude/sessions/paper_audit_content_b575bb0e",
  "sessionId": "1db729b7-6c37-474e-9cbb-179c13a8aeb8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-24T16:15:53.596Z_

```json
{
  "parentUuid": "b6091b43-d320-4395-b9c7-6defb080b459",
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
  "uuid": "279a79da-ce31-4942-a643-419344088559",
  "timestamp": "2026-05-24T16:15:53.596Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/.claude/sessions/paper_audit_content_b575bb0e",
  "sessionId": "1db729b7-6c37-474e-9cbb-179c13a8aeb8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6 · 2026-05-24T16:15:53.596Z_

```json
{
  "parentUuid": "279a79da-ce31-4942-a643-419344088559",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "b163ab2f-5278-41d8-b99b-0e4ff43d5a4a",
  "timestamp": "2026-05-24T16:15:53.596Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/.claude/sessions/paper_audit_content_b575bb0e",
  "sessionId": "1db729b7-6c37-474e-9cbb-179c13a8aeb8",
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
  "aiTitle": "Audit trace-verdict-study EMNLP 2026 submission",
  "sessionId": "1db729b7-6c37-474e-9cbb-179c13a8aeb8"
}
```

---

### Assistant

_source line 8 · 2026-05-24T16:15:57.810Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to perform a content structure audit on a paper. Let me start by reading the required skill files and the paper's .tex files.

Let me first read the two skill files and find all .tex files in the paper directory.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b163ab2f-5278-41d8-b99b-0e4ff43d5a4a",
  "isSidechain": false,
  "requestId": "req_011CbMh9LTERdQfLwLWw7G3r",
  "type": "assistant",
  "uuid": "75c2e5a0-850e-4df4-be90-af53ce76598b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/.claude/sessions/paper_audit_content_b575bb0e",
  "sessionId": "1db729b7-6c37-474e-9cbb-179c13a8aeb8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015mKFFcLQ2b7ySBZy5JxXX9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 26401,
      "cache_read_input_tokens": 11846,
      "output_tokens": 312,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 26401,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 312,
          "cache_read_input_tokens": 11846,
          "cache_creation_input_tokens": 26401,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 26401
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

_source line 9 · 2026-05-24T16:15:58.887Z_

开始执行内容结构审计。先加载审计标准和论文源码。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "75c2e5a0-850e-4df4-be90-af53ce76598b",
  "isSidechain": false,
  "requestId": "req_011CbMh9LTERdQfLwLWw7G3r",
  "type": "assistant",
  "uuid": "63f95ed1-46c2-4da2-8db7-f3b9d840c0d4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/.claude/sessions/paper_audit_content_b575bb0e",
  "sessionId": "1db729b7-6c37-474e-9cbb-179c13a8aeb8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015mKFFcLQ2b7ySBZy5JxXX9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 26401,
      "cache_read_input_tokens": 11846,
      "output_tokens": 312,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 26401,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 312,
          "cache_read_input_tokens": 11846,
          "cache_creation_input_tokens": 26401,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 26401
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

_source line 10 · 2026-05-24T16:15:59.908Z_

<details open><summary>🔧 Tool call — Read · `toolu_01YbR4HkMuiN5y6WfCVhAnBy`</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/skills/global/paper-writing-norms.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "63f95ed1-46c2-4da2-8db7-f3b9d840c0d4",
  "isSidechain": false,
  "requestId": "req_011CbMh9LTERdQfLwLWw7G3r",
  "type": "assistant",
  "uuid": "3306724a-3f93-4ebe-aeb8-d1df0529cb5c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/.claude/sessions/paper_audit_content_b575bb0e",
  "sessionId": "1db729b7-6c37-474e-9cbb-179c13a8aeb8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015mKFFcLQ2b7ySBZy5JxXX9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 26401,
      "cache_read_input_tokens": 11846,
      "output_tokens": 312,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 26401,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 312,
          "cache_read_input_tokens": 11846,
          "cache_creation_input_tokens": 26401,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 26401
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

_source line 11 · 2026-05-24T16:16:01.084Z_

<details><summary>↩ Tool result · `toolu_01B4WAfTukFfNHAUFqRAJ9MP`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/arr_checklist.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/experiments.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/discussion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/appendix.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/main.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/introduction.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7ae8ddf1-0acb-4709-a4d7-2b92c72b4553",
  "isSidechain": false,
  "promptId": "96f110f9-4fbd-4295-8cdb-ef5a8ad15d7a",
  "type": "user",
  "uuid": "dfa18b10-ca9b-49ca-b601-bbfa25d7d0eb",
  "toolUseResult": {
    "filenames": [
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/arr_checklist.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/conclusion.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/experiments.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/discussion.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/appendix.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/related_work.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/main.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/method.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/introduction.tex"
    ],
    "durationMs": 9,
    "numFiles": 9,
    "truncated": false
  },
  "sourceToolAssistantUUID": "7ae8ddf1-0acb-4709-a4d7-2b92c72b4553",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/.claude/sessions/paper_audit_content_b575bb0e",
  "sessionId": "1db729b7-6c37-474e-9cbb-179c13a8aeb8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-24T16:15:59.922Z_

<details><summary>↩ Tool result · `toolu_01YbR4HkMuiN5y6WfCVhAnBy`</summary>

````text
1	---
2	name: paper-writing-norms
3	description: 顶会级别论文写作风格规范——章节写法（Abstract/Intro/Related Work）、去 AI 风格、视觉密度、叙事哲学。Paper Agent 和 Worker 写论文章节时必须加载。
4	allowed-tools: [Read, Write, Edit, Glob, Grep]
5	scope: global
6	version: 2
7	priority: 9
8	tags:
9	  - writing
10	  - paper
11	  - style
12	  - norms
13	roles:
14	  - agent
15	  - worker
16	  - paper_agent
17	---
18	
19	# 论文写作风格规范
20	
21	> 核心哲学：**论文是一个有说服力的故事，不是实验报告。** 审稿人在几十秒内判断论文价值——如果 Abstract 和 Introduction 读起来像实验日志，论文就已经失败了。
22	
23	---
24	
25	## 一、总体写作哲学
26	
27	### 1.1 故事驱动，不是数据堆砌
28	
29	- 论文必须以"故事线"为核心展开：问题 → 洞察 → 方法 → 验证
30	- 禁止大量实验数据堆砌——每个数字出现必须服务于叙事推进
31	- 附录内容必须在正文中有明确引用且融入叙事，禁止简单堆砌
32	- 如果附录数据对核心叙事有重大影响，根据附录数据调整论文 framing
33	
34	### 1.2 主线统一性
35	
36	- 当 idea 在研究过程中发生变化后，**必须重审全文逻辑**
37	- 常见问题：Introduction 讲的故事 A，Method 做的是故事 B，Results 又在讲故事 C
38	- 修复方式：从最终实验结论反推，重写 Introduction 的问题定义和动机
39	- 每次 idea 调整后检查：Abstract → Introduction → Method → Results → Discussion → Conclusion 是否形成一条连贯主线
40	
41	### 1.3 专有名词必须有定义
42	
43	- 首次出现的专有名词/缩写必须给出完整定义和解释
44	- Abstract 中使用的缩写也必须在 Abstract 内定义（如 LLM = Large Language Model）
45	- 不能假设读者知道你自己定义的术语——论文从来没解释过的概念不能直接使用
46	- 通用规则：如果一个非标准术语第一次出现时没有括号定义，就是写作 bug
47	
48	### 1.4 写作前必读同类优秀论文
49	
50	- 每个章节动笔前，找 **2-3 篇目标会议近 1-2 年的高分论文**作为风格参考——同类问题或同类方法皆可
51	- 重点学：
52	  - Abstract 怎么用最少篇幅讲完故事
53	  - Introduction 怎么从大问题切入到具体贡献
54	  - Related Work 怎么 positioning 自己（不是 survey）
55	  - Table/Figure 怎么压缩信息密度
56	- **不是抄袭**，是学习同行的故事节奏和审美——不同子领域叙事节奏差异很大
57	- 实操：Paper Agent 可以从 `literature_map.yaml` 中挑 `role=foundation` 或 `role=direct-competitor` 的论文，把 `{title, venue, year, abstract}` 附在 Worker 的 task_prompt 中作为概念参考；如需学习写作风格本身，让 Worker 通过 WebSearch 取得论文链接并 fetch 全文
58	
59	---
60	
61	## 二、Abstract 写作规范
62	
63	### 2.1 四个必答问题（150-250 words）
64	
65	Abstract 必须在很短的篇幅内清楚回答：
66	1. **研究什么问题** — 1-2 句话交代背景和痛点
67	2. **为什么重要** — 现有方法的不足（不用写太多）
68	3. **本文提出什么** — 核心贡献的关键机制（简要，不堆砌细节）
69	4. **结果说明什么** — 用具体实验结论支撑贡献
70	
71	### 2.2 禁忌
72	
73	- **禁止堆砌数据**：Abstract 不是 Results 的缩写。最多引用 2-3 个关键数字，要服务于 claim
74	- **禁止过度宣传**：不说 "revolutionary"、"groundbreaking"
75	- **禁止写成 Introduction 的缩写**：Abstract 是独立阅读单元
76	- **禁止术语堆积**：如果审稿人几十秒内判断不出价值，就失败了
77	- **缩写必须定义**：Abstract 中首次出现的缩写必须展开
78	
79	### 2.3 审稿人视角检验
80	
81	写完后用这个标准自检：审稿人能否在 30 秒内判断——
82	- 问题是否重要？
83	- 方法是否清楚？
84	- 贡献是否可信？
85	- 结果是否有说服力？
86	
87	---
88	
89	## 三、Introduction 写作规范
90	
91	### 3.1 完整叙事线（5 段结构）
92	
93	Introduction 需要从一个清晰、重要的问题切入，逐步把读者带到核心贡献：
94	
95	1. **研究背景**（1-2 段）：大模型在某类能力/应用中已取得进展，但仍存在一个关键瓶颈
96	2. **问题重要性**（1 段）：结合真实应用、已有方法局限或当前趋势，说明这不是小问题
97	3. **现有方法不足**（1 段）：系统梳理为什么不够（依赖更大模型/更多数据/更复杂推理/更高成本，或只在特定 benchmark 有效）
98	4. **本文核心想法**（1 段）：我们观察到什么、提出了什么方法、为什么能解决上述问题
99	5. **贡献总结**（列表）：清楚列出方法贡献、实验贡献和分析贡献
100	
101	### 3.2 整体叙事结构
102	
103	```
104	现有进展 → 关键缺口 → 本文洞察 → 方法概述 → 实验证据 → 贡献总结
105	```
106	
107	### 3.3 禁忌
108	
109	- **禁止泛泛介绍**：不要开头就写 "LLMs have shown remarkable capabilities..."，要从具体问题切入
110	- **禁止缺少过渡**：每段之间必须有逻辑连接
111	- **禁止实验报告风格**：Introduction 不是 "我们做了 X 实验得到了 Y 结果" 的罗列
112	- 每条 Contribution 必须有对应的 section/table 支撑
113	- Contribution 列表中不能出现未在前文铺垫过的概念
114	
115	---
116	
117	## 四、Related Work 写作规范
118	
119	### 4.1 目标
120	
121	让审稿人相信：作者理解这个领域，知道自己的方法站在什么位置，清楚相对已有工作的真实增量在哪里。
122	
123	### 4.2 结构要求
124	
125	- 把已有工作分成几个清晰的主题（如模型训练、推理增强、工具调用、数据构建、评测等）
126	- 每类简要说明：已有方法做了什么、解决了哪些问题、和本文的关系
127	- 帮助读者理解：哪些是本文直接继承的，哪些方法不同但解决相似问题，哪些留下了本文要解决的缺口
128	
129	### 4.3 禁忌
130	
131	- **禁止论文堆砌**：不要写成 "A proposed X. B proposed Y. C proposed Z." 的列表
132	- **目标不是展示读了多少论文**，而是做归纳和比较
133	- Contribution claim（"To our knowledge, no prior work..."）应放在 Introduction，不在 Related Work
134	
135	### 4.4 引用充足度
136	
137	- 引用必须覆盖：**直接相关方法、baseline 论文、评测 benchmark 论文、理论基础**
138	- 任何一类缺失，审稿人会立刻看出来调研不充分
139	- 引用密度参照目标会议近年录用论文的量级——明显偏少意味着 Related Work 调研不足
140	
141	---
142	
143	## 五、去 AI 写作风格（硬规则）
144	
145	以下模式是 AI 生成文本的典型标志，审稿人一眼能看出。**必须全部消除。**
146	
147	### 5.1 严禁破折号（最显著的 AI 痕迹）
148	
149	**这是 AI 写作最容易被识别的标志，审稿人最敏感。单列为最高优先级硬规则。**
150	
151	- 解释性 em-dash（—，U+2014）和 en-dash（–，U+2013）必须**全部删除**
152	- 替代方式：用逗号、括号或拆分为两个句子
153	- 强制检查命令：
154	  ```bash
155	  grep -n "—" paper/*.tex     # em-dash，每处人工判断是否必要
156	  grep -n " – " paper/*.tex   # 解释性 en-dash，几乎都应删除
157	  ```
158	- 例外（允许保留）：表格分隔符、数字范围（`2020–2024`、`pp. 12–18`）、专有名词（`Newton–Raphson`）
159	
160	### 5.2 段落与句式
161	
162	- **禁止过度分段**：不需要每 2-3 句就换段，自然段 5-8 句是正常的
163	- **减少关系从句**（which, that, who）：能用简洁直接的句子就不用从句
164	- **禁止 -ing 短语结尾**：如 "..., highlighting the applicability of..." / "..., demonstrating the effectiveness of..."。这是 AI 写作最典型的标志之一
165	- **禁止连续使用 "Furthermore" / "Moreover" / "Additionally"**：一段内最多用一个过渡词
166	- **避免 "It is worth noting that..." / "Notably, ..."**：直接写要说的内容
167	
168	### 5.3 用词黑名单
169	
170	- 避免 "delve into" / "leverage" / "utilize" / "facilitate" — 用 "explore" / "use" / "enable"
171	- 避免 "a myriad of" / "a plethora of" — 用 "many" / "various"
172	- 避免 "in the realm of" / "in the context of" — 直接说
173	- 避免 "paradigm shift" / "novel" 过度使用
174	
175	### 5.4 校对清单（4 步）
176	
177	1. 全文 proofread 语法和拼写
178	2. 检查所有代词/指示词（this, that, it）是否指代明确
179	3. **`grep "—"` + `grep " – "` 全文清零**（删除所有解释性 dash，§5.1）
180	4. `grep "ing,"` 模式——大部分 -ing 分词短语需要改写
181	
182	---
183	
184	## 六、图表与视觉规范
185	
186	### 6.1 知识密度原则
187	
188	- **图表的信息必须紧凑**——不能为了美观而留大量白空间
189	- 一张图如果只传达一个简单信息，要么缩小要么合并到其他图中
190	- 能用 inline text 说清的不要占一整个 Figure
191	
192	### 6.2 表格规范
193	
194	- 表格和正文文字不能视觉重叠（检查 column 宽度和 alignment）
195	- 小数精度全表统一
196	- 最优加粗、次优下划线
197	- Caption 必须自包含
198	
199	### 6.3 图片规范
200	
201	- 数值标签不能被线、bar、点遮住——用白色背景或偏移标签
202	- 图中字体 >= 7pt（打印后仍可读）
203	- 栏宽约束需匹配目标 venue 模板要求
204	- 概念图/流程图要有信息量，不要画一个 trivial 的 pipeline 然后占半页
205	
206	### 6.4 空间效率
207	
208	- 顶会正文页数严格受限（具体页数查目标会议官网），每 cm² 都是宝贵资源
209	- 优先使用 `\subfigure` 合并相关图
210	- Table 能 inline 就不要单独浮动
211	- 图表占比与其对叙事的贡献成正比
212	
213	### 6.5 页面节奏
214	
215	好论文的页面有节奏感——text、equation、figure 交替出现，读者视觉不疲劳：
216	
217	- **text-equation-figure 三重奏**：重要概念用"文字解释 → 公式定义 → 图表直觉"三步展开
218	- 连续 2 页纯文本（无 figure/equation/table）→ 穿插一个 display item 打破节奏
219	- 连续 2 个 figure 页（整页被 float 占满）→ 至少隔 1 段文字再放下一个 float
220	- Section heading 不孤悬页底（heading 后至少跟 2 行正文，否则强制分页）
221	- 最后一页内容 ≥ 2/3 页面高度（太空显得凑数，太满放不下 references）
222	
223	### 6.6 表格 LaTeX 规范
224	
225	**Booktabs 标准（硬规则）**：
226	- 用 `\toprule` / `\midrule` / `\bottomrule`，禁止 `\hline`，禁止竖线 `|`
227	- 用 `\centering` 不用 `\begin{center}`（后者多加垂直空白）
228	- 最优结果加粗（`\textbf{}`），次优下划线（`\underline{}`）+ 方向箭头 `↑`/`↓` 标明指标方向
229	- 小数精度全表统一（如全部保留 1 位或 2 位）
230	- Caption 在表格上方（`\caption` 在 `\begin{tabular}` 之前）
231	
232	**宽度决策树**：
233	- ≤5 列 → 单栏宽度（`\columnwidth`）
234	- 6–8 列 → 全文宽度（`\textwidth`，双栏模板用 `table*`）
235	- >8 列 → 拆成两张表或移入 appendix
236	
237	---
238	
239	## 七、投稿前通用准备
240	
241	### 7.1 模板必须官方（硬规则）
242	
243	- LaTeX 模板**必须从目标会议官网下载**（CallForPapers / Author Instructions 页面）
244	- **不要用**：
245	  - 网上他人转载的复制版本（可能被改过 margin / 行号设置）
246	  - 上一年的模板（参数可能变：字体、margin、行号、anonymous 选项等）
247	  - 组里学长留的旧版本（来源不明、无法追溯）
248	- 风险：
249	  - 样式不符合 → desk reject
250	  - margin 不对 → 被审稿人质疑诚信
251	  - reference 格式错 → 被认为不规范
252	- 流程：先查会议官网 templates → 找不到再 `WebSearch "{venue} {year} latex template official"` → 仍找不到汇报 Director（不要用就近年版本顶替）
253	- `\documentclass[]{}` 选项必须与目标 venue + 阶段（review / camera-ready）一致
254	
255	### 7.2 投稿要求逐项核对
256	
257	- 目标会议如要求 Checklist / Ethical Statement / Broader Impact Statement / Reproducibility Statement，必须**认真填每一项**，不要全写 N/A
258	- 页数限制：查目标会议官网
259	- 匿名化要求：review 版 vs camera-ready 版本设置不同
260	- 行号开启（review 版常需）
261	- 字体大小、margin 不得修改 sty 文件
262	
263	### 7.3 最终修改 10 项检查流程
264	
265	提交前必须逐一检查：
266	1. 所有最新实验结果已全部录入
267	2. 根据实验结果将叙事调至最优状态
268	3. 附录所有内容在正文中被引用且融入叙事
269	4. 无数据堆砌（每个数字服务于叙事推进）
270	5. Abstract 和 Introduction 具有吸引力（不是实验报告风格）
271	6. 全文主线统一（idea 变化后各章节逻辑一致）
272	7. 所有专有名词有定义
273	8. 无 AI 风格标志（dash、-ing phrases、过度分段）
274	9. 图表知识密度高、无视觉遮挡
275	10. Reference 覆盖直接相关方法、baseline、benchmark、理论基础
276	
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "parentUuid": "3306724a-3f93-4ebe-aeb8-d1df0529cb5c",
  "isSidechain": false,
  "promptId": "96f110f9-4fbd-4295-8cdb-ef5a8ad15d7a",
  "type": "user",
  "uuid": "9cf5015d-cb93-4cec-86f9-ad33bdc72796",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/agent-ml-research/skills/global/paper-writing-norms.skill.md",
      "content": "---\nname: paper-writing-norms\ndescription: 顶会级别论文写作风格规范——章节写法（Abstract/Intro/Related Work）、去 AI 风格、视觉密度、叙事哲学。Paper Agent 和 Worker 写论文章节时必须加载。\nallowed-tools: [Read, Write, Edit, Glob, Grep]\nscope: global\nversion: 2\npriority: 9\ntags:\n  - writing\n  - paper\n  - style\n  - norms\nroles:\n  - agent\n  - worker\n  - paper_agent\n---\n\n# 论文写作风格规范\n\n> 核心哲学：**论文是一个有说服力的故事，不是实验报告。** 审稿人在几十秒内判断论文价值——如果 Abstract 和 Introduction 读起来像实验日志，论文就已经失败了。\n\n---\n\n## 一、总体写作哲学\n\n### 1.1 故事驱动，不是数据堆砌\n\n- 论文必须以\"故事线\"为核心展开：问题 → 洞察 → 方法 → 验证\n- 禁止大量实验数据堆砌——每个数字出现必须服务于叙事推进\n- 附录内容必须在正文中有明确引用且融入叙事，禁止简单堆砌\n- 如果附录数据对核心叙事有重大影响，根据附录数据调整论文 framing\n\n### 1.2 主线统一性\n\n- 当 idea 在研究过程中发生变化后，**必须重审全文逻辑**\n- 常见问题：Introduction 讲的故事 A，Method 做的是故事 B，Results 又在讲故事 C\n- 修复方式：从最终实验结论反推，重写 Introduction 的问题定义和动机\n- 每次 idea 调整后检查：Abstract → Introduction → Method → Results → Discussion → Conclusion 是否形成一条连贯主线\n\n### 1.3 专有名词必须有定义\n\n- 首次出现的专有名词/缩写必须给出完整定义和解释\n- Abstract 中使用的缩写也必须在 Abstract 内定义（如 LLM = Large Language Model）\n- 不能假设读者知道你自己定义的术语——论文从来没解释过的概念不能直接使用\n- 通用规则：如果一个非标准术语第一次出现时没有括号定义，就是写作 bug\n\n### 1.4 写作前必读同类优秀论文\n\n- 每个章节动笔前，找 **2-3 篇目标会议近 1-2 年的高分论文**作为风格参考——同类问题或同类方法皆可\n- 重点学：\n  - Abstract 怎么用最少篇幅讲完故事\n  - Introduction 怎么从大问题切入到具体贡献\n  - Related Work 怎么 positioning 自己（不是 survey）\n  - Table/Figure 怎么压缩信息密度\n- **不是抄袭**，是学习同行的故事节奏和审美——不同子领域叙事节奏差异很大\n- 实操：Paper Agent 可以从 `literature_map.yaml` 中挑 `role=foundation` 或 `role=direct-competitor` 的论文，把 `{title, venue, year, abstract}` 附在 Worker 的 task_prompt 中作为概念参考；如需学习写作风格本身，让 Worker 通过 WebSearch 取得论文链接并 fetch 全文\n\n---\n\n## 二、Abstract 写作规范\n\n### 2.1 四个必答问题（150-250 words）\n\nAbstract 必须在很短的篇幅内清楚回答：\n1. **研究什么问题** — 1-2 句话交代背景和痛点\n2. **为什么重要** — 现有方法的不足（不用写太多）\n3. **本文提出什么** — 核心贡献的关键机制（简要，不堆砌细节）\n4. **结果说明什么** — 用具体实验结论支撑贡献\n\n### 2.2 禁忌\n\n- **禁止堆砌数据**：Abstract 不是 Results 的缩写。最多引用 2-3 个关键数字，要服务于 claim\n- **禁止过度宣传**：不说 \"revolutionary\"、\"groundbreaking\"\n- **禁止写成 Introduction 的缩写**：Abstract 是独立阅读单元\n- **禁止术语堆积**：如果审稿人几十秒内判断不出价值，就失败了\n- **缩写必须定义**：Abstract 中首次出现的缩写必须展开\n\n### 2.3 审稿人视角检验\n\n写完后用这个标准自检：审稿人能否在 30 秒内判断——\n- 问题是否重要？\n- 方法是否清楚？\n- 贡献是否可信？\n- 结果是否有说服力？\n\n---\n\n## 三、Introduction 写作规范\n\n### 3.1 完整叙事线（5 段结构）\n\nIntroduction 需要从一个清晰、重要的问题切入，逐步把读者带到核心贡献：\n\n1. **研究背景**（1-2 段）：大模型在某类能力/应用中已取得进展，但仍存在一个关键瓶颈\n2. **问题重要性**（1 段）：结合真实应用、已有方法局限或当前趋势，说明这不是小问题\n3. **现有方法不足**（1 段）：系统梳理为什么不够（依赖更大模型/更多数据/更复杂推理/更高成本，或只在特定 benchmark 有效）\n4. **本文核心想法**（1 段）：我们观察到什么、提出了什么方法、为什么能解决上述问题\n5. **贡献总结**（列表）：清楚列出方法贡献、实验贡献和分析贡献\n\n### 3.2 整体叙事结构\n\n```\n现有进展 → 关键缺口 → 本文洞察 → 方法概述 → 实验证据 → 贡献总结\n```\n\n### 3.3 禁忌\n\n- **禁止泛泛介绍**：不要开头就写 \"LLMs have shown remarkable capabilities...\"，要从具体问题切入\n- **禁止缺少过渡**：每段之间必须有逻辑连接\n- **禁止实验报告风格**：Introduction 不是 \"我们做了 X 实验得到了 Y 结果\" 的罗列\n- 每条 Contribution 必须有对应的 section/table 支撑\n- Contribution 列表中不能出现未在前文铺垫过的概念\n\n---\n\n## 四、Related Work 写作规范\n\n### 4.1 目标\n\n让审稿人相信：作者理解这个领域，知道自己的方法站在什么位置，清楚相对已有工作的真实增量在哪里。\n\n### 4.2 结构要求\n\n- 把已有工作分成几个清晰的主题（如模型训练、推理增强、工具调用、数据构建、评测等）\n- 每类简要说明：已有方法做了什么、解决了哪些问题、和本文的关系\n- 帮助读者理解：哪些是本文直接继承的，哪些方法不同但解决相似问题，哪些留下了本文要解决的缺口\n\n### 4.3 禁忌\n\n- **禁止论文堆砌**：不要写成 \"A proposed X. B proposed Y. C proposed Z.\" 的列表\n- **目标不是展示读了多少论文**，而是做归纳和比较\n- Contribution claim（\"To our knowledge, no prior work...\"）应放在 Introduction，不在 Related Work\n\n### 4.4 引用充足度\n\n- 引用必须覆盖：**直接相关方法、baseline 论文、评测 benchmark 论文、理论基础**\n- 任何一类缺失，审稿人会立刻看出来调研不充分\n- 引用密度参照目标会议近年录用论文的量级——明显偏少意味着 Related Work 调研不足\n\n---\n\n## 五、去 AI 写作风格（硬规则）\n\n以下模式是 AI 生成文本的典型标志，审稿人一眼能看出。**必须全部消除。**\n\n### 5.1 严禁破折号（最显著的 AI 痕迹）\n\n**这是 AI 写作最容易被识别的标志，审稿人最敏感。单列为最高优先级硬规则。**\n\n- 解释性 em-dash（—，U+2014）和 en-dash（–，U+2013）必须**全部删除**\n- 替代方式：用逗号、括号或拆分为两个句子\n- 强制检查命令：\n  ```bash\n  grep -n \"—\" paper/*.tex     # em-dash，每处人工判断是否必要\n  grep -n \" – \" paper/*.tex   # 解释性 en-dash，几乎都应删除\n  ```\n- 例外（允许保留）：表格分隔符、数字范围（`2020–2024`、`pp. 12–18`）、专有名词（`Newton–Raphson`）\n\n### 5.2 段落与句式\n\n- **禁止过度分段**：不需要每 2-3 句就换段，自然段 5-8 句是正常的\n- **减少关系从句**（which, that, who）：能用简洁直接的句子就不用从句\n- **禁止 -ing 短语结尾**：如 \"..., highlighting the applicability of...\" / \"..., demonstrating the effectiveness of...\"。这是 AI 写作最典型的标志之一\n- **禁止连续使用 \"Furthermore\" / \"Moreover\" / \"Additionally\"**：一段内最多用一个过渡词\n- **避免 \"It is worth noting that...\" / \"Notably, ...\"**：直接写要说的内容\n\n### 5.3 用词黑名单\n\n- 避免 \"delve into\" / \"leverage\" / \"utilize\" / \"facilitate\" — 用 \"explore\" / \"use\" / \"enable\"\n- 避免 \"a myriad of\" / \"a plethora of\" — 用 \"many\" / \"various\"\n- 避免 \"in the realm of\" / \"in the context of\" — 直接说\n- 避免 \"paradigm shift\" / \"novel\" 过度使用\n\n### 5.4 校对清单（4 步）\n\n1. 全文 proofread 语法和拼写\n2. 检查所有代词/指示词（this, that, it）是否指代明确\n3. **`grep \"—\"` + `grep \" – \"` 全文清零**（删除所有解释性 dash，§5.1）\n4. `grep \"ing,\"` 模式——大部分 -ing 分词短语需要改写\n\n---\n\n## 六、图表与视觉规范\n\n### 6.1 知识密度原则\n\n- **图表的信息必须紧凑**——不能为了美观而留大量白空间\n- 一张图如果只传达一个简单信息，要么缩小要么合并到其他图中\n- 能用 inline text 说清的不要占一整个 Figure\n\n### 6.2 表格规范\n\n- 表格和正文文字不能视觉重叠（检查 column 宽度和 alignment）\n- 小数精度全表统一\n- 最优加粗、次优下划线\n- Caption 必须自包含\n\n### 6.3 图片规范\n\n- 数值标签不能被线、bar、点遮住——用白色背景或偏移标签\n- 图中字体 >= 7pt（打印后仍可读）\n- 栏宽约束需匹配目标 venue 模板要求\n- 概念图/流程图要有信息量，不要画一个 trivial 的 pipeline 然后占半页\n\n### 6.4 空间效率\n\n- 顶会正文页数严格受限（具体页数查目标会议官网），每 cm² 都是宝贵资源\n- 优先使用 `\\subfigure` 合并相关图\n- Table 能 inline 就不要单独浮动\n- 图表占比与其对叙事的贡献成正比\n\n### 6.5 页面节奏\n\n好论文的页面有节奏感——text、equation、figure 交替出现，读者视觉不疲劳：\n\n- **text-equation-figure 三重奏**：重要概念用\"文字解释 → 公式定义 → 图表直觉\"三步展开\n- 连续 2 页纯文本（无 figure/equation/table）→ 穿插一个 display item 打破节奏\n- 连续 2 个 figure 页（整页被 float 占满）→ 至少隔 1 段文字再放下一个 float\n- Section heading 不孤悬页底（heading 后至少跟 2 行正文，否则强制分页）\n- 最后一页内容 ≥ 2/3 页面高度（太空显得凑数，太满放不下 references）\n\n### 6.6 表格 LaTeX 规范\n\n**Booktabs 标准（硬规则）**：\n- 用 `\\toprule` / `\\midrule` / `\\bottomrule`，禁止 `\\hline`，禁止竖线 `|`\n- 用 `\\centering` 不用 `\\begin{center}`（后者多加垂直空白）\n- 最优结果加粗（`\\textbf{}`），次优下划线（`\\underline{}`）+ 方向箭头 `↑`/`↓` 标明指标方向\n- 小数精度全表统一（如全部保留 1 位或 2 位）\n- Caption 在表格上方（`\\caption` 在 `\\begin{tabular}` 之前）\n\n**宽度决策树**：\n- ≤5 列 → 单栏宽度（`\\columnwidth`）\n- 6–8 列 → 全文宽度（`\\textwidth`，双栏模板用 `table*`）\n- >8 列 → 拆成两张表或移入 appendix\n\n---\n\n## 七、投稿前通用准备\n\n### 7.1 模板必须官方（硬规则）\n\n- LaTeX 模板**必须从目标会议官网下载**（CallForPapers / Author Instructions 页面）\n- **不要用**：\n  - 网上他人转载的复制版本（可能被改过 margin / 行号设置）\n  - 上一年的模板（参数可能变：字体、margin、行号、anonymous 选项等）\n  - 组里学长留的旧版本（来源不明、无法追溯）\n- 风险：\n  - 样式不符合 → desk reject\n  - margin 不对 → 被审稿人质疑诚信\n  - reference 格式错 → 被认为不规范\n- 流程：先查会议官网 templates → 找不到再 `WebSearch \"{venue} {year} latex template official\"` → 仍找不到汇报 Director（不要用就近年版本顶替）\n- `\\documentclass[]{}` 选项必须与目标 venue + 阶段（review / camera-ready）一致\n\n### 7.2 投稿要求逐项核对\n\n- 目标会议如要求 Checklist / Ethical Statement / Broader Impact Statement / Reproducibility Statement，必须**认真填每一项**，不要全写 N/A\n- 页数限制：查目标会议官网\n- 匿名化要求：review 版 vs camera-ready 版本设置不同\n- 行号开启（review 版常需）\n- 字体大小、margin 不得修改 sty 文件\n\n### 7.3 最终修改 10 项检查流程\n\n提交前必须逐一检查：\n1. 所有最新实验结果已全部录入\n2. 根据实验结果将叙事调至最优状态\n3. 附录所有内容在正文中被引用且融入叙事\n4. 无数据堆砌（每个数字服务于叙事推进）\n5. Abstract 和 Introduction 具有吸引力（不是实验报告风格）\n6. 全文主线统一（idea 变化后各章节逻辑一致）\n7. 所有专有名词有定义\n8. 无 AI 风格标志（dash、-ing phrases、过度分段）\n9. 图表知识密度高、无视觉遮挡\n10. Reference 覆盖直接相关方法、baseline、benchmark、理论基础\n",
      "numLines": 276,
      "startLine": 1,
      "totalLines": 276
    }
  },
  "sourceToolAssistantUUID": "3306724a-3f93-4ebe-aeb8-d1df0529cb5c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/.claude/sessions/paper_audit_content_b575bb0e",
  "sessionId": "1db729b7-6c37-474e-9cbb-179c13a8aeb8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
````

</details>

---

### Tool call

_source line 13 · 2026-05-24T16:16:00.423Z_

<details open><summary>🔧 Tool call — Read · `toolu_01TbNC6jkLHCyjYXhbwuRZ2M`</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/skills/global/paper-quality-lessons.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9cf5015d-cb93-4cec-86f9-ad33bdc72796",
  "isSidechain": false,
  "requestId": "req_011CbMh9LTERdQfLwLWw7G3r",
  "type": "assistant",
  "uuid": "e83ce78c-fdee-4ad3-90cf-0b6b966cf2a1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/.claude/sessions/paper_audit_content_b575bb0e",
  "sessionId": "1db729b7-6c37-474e-9cbb-179c13a8aeb8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015mKFFcLQ2b7ySBZy5JxXX9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 26401,
      "cache_read_input_tokens": 11846,
      "output_tokens": 312,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 26401,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 312,
          "cache_read_input_tokens": 11846,
          "cache_creation_input_tokens": 26401,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 26401
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

_source line 14 · 2026-05-24T16:16:00.430Z_

<details><summary>↩ Tool result · `toolu_01TbNC6jkLHCyjYXhbwuRZ2M`</summary>

````text
1	---
2	name: paper-quality-lessons
3	description: NeurIPS 投稿实战经验总结——人工审查中提炼的写作规范、审查清单、常见反模式。Paper Agent / Reviewer / Director 写论文或审查论文时加载。
4	allowed-tools: [Read, Write, Edit, Glob, Grep]
5	scope: global
6	version: 1
7	tags:
8	  - writing
9	  - paper
10	  - quality
11	  - checklist
12	  - review
13	roles:
14	  - agent
15	  - reviewer
16	  - director
17	  - paper_agent
18	---
19	
20	# 论文写作质量指南（NeurIPS 实战经验）
21	
22	> 来源：2026 年 NeurIPS 投稿期间，从 20+ 项目的人工审查反馈中提炼。
23	> 每条规则都源自真实的 bug / 退回 / 审稿质疑。
24	
25	---
26	
27	## 一、数据诚信与溯源（最高优先级）
28	
29	### 1.1 数字必须有源头
30	
31	- 论文中**每一个数字**必须可追溯到 registry 实验 ID 或原始结果文件
32	- 禁止凭记忆写数字——必须 `cat result.json | head` + `ls -la` 附上文件证据
33	- 计算值（均值、标准差、DID、delta）必须独立重算，不信 Agent 第一手汇报
34	- `paper_provenance.yaml` 覆盖率必须 100%，改数字必须同步更新 provenance
35	
36	> **教训（D149 事件）**：Agent 曾伪造完整的 metrics 数据包括 p-value，事后被 Reviewer 独立 parse JSON 抓出。从此所有关键数据必须 Reviewer 独立验证到字段级别。
37	
38	### 1.2 不同来源数据不能混用
39	
40	- 配对数据必须同 seed、同 c 值、同 N、同 evaluation protocol
41	- 两张表如果 protocol 不同（如 0-shot vs 8-shot），论文必须明确说明
42	- 跨 config 比较 delta 会引入系统误差——必须补跑同 config baseline 后才能比较
43	- 非等量对比必须显式标注（如 "at unmatched volumes"）
44	
45	> **教训（D027 事件）**：不同 config 文件的 baseline 不同，跨 config 比较 delta 值引入了 artifact。
46	
47	### 1.3 结论撤回后不可复活
48	
49	- 被 Director shelved 的数据（如因截断混淆），禁止重新引入论文
50	- `paper_provenance.yaml` 中 `verified: false` 的 claim，不得恢复
51	- 术语修正后不可回退（如 "same norm" → "same per-layer standard deviation"）
52	
53	---
54	
55	## 二、Claim 强度与数据匹配
56	
57	### 2.1 Claim 强度规则
58	
59	| 数据支撑 | 允许的最强表述 |
60	|----------|--------------|
61	| 单 seed, 单数据集 | "preliminary observation", "initial evidence" |
62	| 单 seed, 多数据集 | "suggestive pattern", "indicative trend" |
63	| 多 seed, 单数据集 | 报告均值±标准差，可写 "we find" |
64	| 多 seed, 多数据集 | 可用 "robust", "consistent" |
65	| 统计检验显著 | 可用 "significant", 附 p-value |
66	| 单 seed + 外推到其他条件 | 必须加限定，不能声称 "scale-invariant" 等 |
67	
68	### 2.2 禁止的过强表述
69	
70	- "remarkably stable" → 改为 "relatively stable" 或给出量化波动范围
71	- "confirmed" → 仅 "suggestive" 级别数据不能用
72	- "scale-invariant" → single-seed 验证不够
73	- "We attribute X to Y" → 如果是假说，必须改为 "We hypothesize" + "requiring causal verification"
74	- "roughly twice" → 实际比值必须在 1.8x-2.2x 才能用，否则改为更准确的近似
75	- "domain-agnostic" → 改为 "robust across N domains tested"
76	
77	### 2.3 Claim 降级机制
78	
79	当证据不足以支撑独立 claim 时，应降级为 discussion 中的定性讨论，而非删除。具体做法：
80	- 独立 contribution → Discussion 段落
81	- 硬 claim → 加 caveat 的软 claim
82	- 正文数字 → 移入 Appendix
83	
84	---
85	
86	## 三、叙事与 Storytelling
87	
88	### 3.1 结构原则
89	
90	- 核心 paradox/发现之间必须有**过渡句**桥接，不能让读者在关键处断线
91	- Introduction 每条 Contribution 必须有对应的 section/table 支撑
92	- Discussion 不应重复 Results 的具体数字——引用表格编号
93	- 同一解释不要在多处重复推导——主文写一次 + 指向 Appendix
94	- Limitations 段不要写成一个 17 行大段——拆分为 2-3 个子段按主题分组
95	
96	### 3.2 冷引用（Cold Reference）
97	
98	- 任何首次出现的概念必须有上文铺垫
99	- Introduction 贡献列表中不能突然出现未被提及的模型/方法名
100	
101	### 3.3 不要用旧叙事套新数字
102	
103	新 baseline 出来后若 delta 大幅变化，Section 的叙事逻辑必须重写，不是简单替换数字。
104	
105	### 3.4 Contingency Plan
106	
107	关键实验结果不确定时需预写两套叙事（如 "若结果 A → 叙事 A"、"若结果 B → 叙事 B"），实验完成后选择正确版本。提交前必须确认只留了一套。
108	
109	### 3.5 不要基于中间值做叙事决策
110	
111	70% 进度时的估计往往不够稳定（尤其 GSM8K 等难度分布不均匀的 benchmark），必须等完整数据再定稿叙事。
112	
113	---
114	
115	## 四、术语与一致性
116	
117	### 4.1 术语一致性
118	
119	- 全文必须统一使用正式定义的术语，不得出现同义词漂移
120	- 术语定义后，每次使用必须完全一致（不要有时 "perturbation sensitivity" 有时 "perturbation impact"）
121	
122	### 4.2 统计量一致性
123	
124	- 两个不同的 kappa/p-value 每次出现时必须标注是哪个
125	- 同一个 metric 在不同位置的数字必须完全一致
126	- 修改任何数字后必须全文 grep 确认所有引用处同步
127	
128	### 4.3 p-value 格式
129	
130	- 无前导零、3 位小数：`p = .003`（不是 `p = 0.003`）
131	- 当非劣效性 p<0.001 实际由正向效应驱动时，必须加括注说明
132	
133	### 4.4 例子与定义必须一致
134	
135	Taxonomy 中的定义和对应示例不能自相矛盾。如果定义说 "no new content"，示例中就不能包含新信息。
136	
137	---
138	
139	## 五、投稿前检查清单（Pre-Submission Checklist）
140	
141	### 5.1 占位符扫描（硬门禁）
142	
143	提交前必须 grep 扫描，以下模式要求**零匹配**：
144	```
145	XX.XX, PLACEHOLDER, [If , TODO, TBD, \placeholder{
146	```
147	所有条件占位段落（`[If ...]`）必须替换为最终文本。
148	
149	### 5.2 编译检查
150	
151	- [ ] 编译零 error
152	- [ ] 无 `??` 未解析引用
153	- [ ] 无 > 1pt 的 overfull hbox
154	- [ ] 正文 ≤ 9 页（NeurIPS desk reject 风险）
155	- [ ] 使用当年 style file（`neurips_2026.sty`）
156	- [ ] Review 版启用行号
157	- [ ] 匿名审稿版无作者姓名、无致谢
158	
159	### 5.3 数据完整性
160	
161	- [ ] 论文所有数字与 registry/provenance 交叉验证通过
162	- [ ] 计算值（均值、标准差、DID、delta）独立重算确认
163	- [ ] 所有 evaluation protocol 差异已在论文中说明
164	- [ ] 多 seed 结果报告均值和标准差
165	- [ ] 单 seed 数据在 Limitations 中声明
166	
167	### 5.4 图表检查
168	
169	- [ ] 所有 figure PDF 存在且路径匹配
170	- [ ] 图表不超栏宽（单栏 5.5in / 全宽 6.5in）
171	- [ ] 图中字体 ≥ 7pt
172	- [ ] 小数精度全表统一
173	- [ ] 最优结果加粗、次优下划线
174	- [ ] 表格标题（caption）自包含
175	- [ ] Forest plot 等可视化无 dummy 值（CI_LO=-99 等）
176	
177	### 5.5 引用检查
178	
179	- [ ] 引用覆盖：**直接相关方法、baseline 论文、评测 benchmark 论文、理论基础**（任一缺失说明调研不充分）
180	- [ ] 引用密度与目标会议近年录用论文同量级
181	- [ ] 引用键与 bib 条目 1:1 匹配
182	- [ ] 无孤儿 bib 条目
183	- [ ] 无幻觉引用（所有被引论文实际存在）
184	- [ ] 近年论文的年份/会议准确
185	- [ ] 审稿人要求的引用全部补齐
186	
187	### 5.6 匿名化检查
188	
189	- [ ] 源代码无硬编码绝对路径（`/Users/...`, `/root/...`）
190	- [ ] 配置文件无服务器路径
191	- [ ] Git history 已清理 author 信息（用 fresh repo）
192	- [ ] 项目管理文件不得提交（AGENTS.md, memory.md, registry.yaml, task_context/ 等）
193	- [ ] API Keys 通过环境变量，无泄露
194	
195	### 5.7 会议 Checklist 填写（如目标会议要求）
196	
197	- [ ] Claims: 摘要/Introduction 准确反映实验范围
198	- [ ] Limitations: 正文 Limitations 段 + Appendix 补充
199	- [ ] Experiments: 实验设置完整（exp_id, seed, 超参, 评估 protocol）
200	- [ ] Reproducibility: 数据集公开、代码可用
201	- [ ] Statistical Significance: 多 seed 均值+标准差、置信区间
202	- [ ] Compute: GPU 型号、训练时间、总 GPU-hours
203	- [ ] Licenses: 数据集/模型引用完整
204	- [ ] AI Assistants: 如实声明使用情况
205	- [ ] 每项认真回答（不要全写 N/A）
206	
207	### 5.8 叙事完整性
208	
209	- [ ] Conclusion 包含所有关键限定符（如 "under greedy decoding"）
210	- [ ] Abstract 与正文一致（不能一个写 "single seed" 另一个已是 "10 seeds"）
211	- [ ] 无 Appendix Version A/B 两套叙事残留
212	- [ ] 无 LaTeX 注释与正文混淆
213	- [ ] Contribution claim 在 Introduction 中（不在 Related Work 中）
214	- [ ] 所有专有名词/缩写首次出现时有定义（Abstract 内缩写也必须展开）
215	- [ ] Introduction 与 Method/Results 讲同一条主线（idea 变化后全文逻辑一致）
216	
217	### 5.9 去 AI 风格检查
218	
219	- [ ] **`grep "—" paper/*.tex` 全文清零**（解释性 em-dash 必须全删，最显著的 AI 痕迹）
220	- [ ] **`grep " – " paper/*.tex` 全文清零**（解释性 en-dash 必须全删）
221	- [ ] 无 "-ing," 分词短语结尾（如 "..., demonstrating the effectiveness of..."）
222	- [ ] 无连续 "Furthermore" / "Moreover" / "Additionally"（同段最多 1 个）
223	- [ ] 无 "It is worth noting that..." / "Notably, ..."
224	- [ ] 无 "delve into" / "leverage" / "utilize" / "a myriad of" / "a plethora of"
225	- [ ] 自然段 5-8 句是正常的，不要每 2-3 句就换段
226	
227	### 5.10 模板与同类论文核对
228	
229	- [ ] LaTeX 模板从目标会议官网下载（不是他人转载、不是上一年）
230	- [ ] `\documentclass[]{}` 选项匹配 review / camera-ready 阶段
231	- [ ] 写作前已参考 2-3 篇同领域近 1-2 年优秀论文，叙事节奏对齐
232	
233	---
234	
235	## 六、Reviewer 审查标准
236	
237	### 6.1 CRITICAL 级别（必须修复才能提交）
238	
239	- 论文数字与实验数据不一致
240	- Abstract 与正文矛盾
241	- Evaluation protocol 混淆（如 0-shot 写成 8-shot）
242	- 未经验证的数据写入论文
243	- 占位符残留
244	
245	### 6.2 WARNING 级别（应当修复）
246	
247	- Stale claims（更新了某处数字但忘了同步其他位置）
248	- 过强措辞不匹配数据支撑
249	- 隐式全因子设计误导（如写 "3×3×3=27" 但实际只有 15 格）
250	- 评估指标只描述了部分 domain
251	- 旧版数据引用
252	
253	### 6.3 数据一致性审查流程
254	
255	1. 从 registry 提取所有实验 metrics
256	2. 对照论文中每一个内联数字（到行号级别）
257	3. 独立重算所有衍生值
258	4. 不一致处标注为 CRITICAL
259	5. 近似表述检查实际比值是否在允许范围内
260	
261	---
262	
263	## 七、常见反模式速查表
264	
265	| 反模式 | 症状 | 修复方式 |
266	|--------|------|----------|
267	| Stale claim | 论文某处还引用旧数字 | 改数字后全文 grep 同步 |
268	| Protocol 混淆 | 不同表格用了不同 evaluation 但没说明 | 每张表注明 protocol |
269	| Agent 误报 | 实验结果缺乏文件证据 | 要求 `cat result.json` 截图 |
270	| 混用数据算比值 | 跨 seed/条件/N 的数据混合比较 | 只用严格配对的数据 |
271	| 叙事超越数据 | "confirmed" 但实际只是 suggestive | 匹配 claim 强度到 §2.1 |
272	| 冷引用 | 首次出现的概念无铺垫 | 先建立框架再引入 |
273	| 定义-例子矛盾 | Taxonomy 定义和示例冲突 | 审查所有定义与其示例 |
274	| Placeholder 残留 | XX.XX, TODO, [If...] 未清理 | 提交前 grep 硬门禁 |
275	| Path 泄露 | 代码/config 含服务器绝对路径 | 改为相对路径 |
276	| 重复推导 | 同一解释在 3 处各自推导一遍 | 主文一次 + 引用 Appendix |
277	| Discussion 重复 Results | Discussion 大量复制 Results 数字 | 改为引用表格编号 |
278	| 单 seed overclaim | 单 seed 数据声称 scale-invariant | 加 preliminary/hedging 限定 |
279	| Registry 不同步 | Registry 面值与实际状态不一致 | 以 SSH 实测为准 |
280	| vLLM 静默失败 | max_model_len 太小导致 100% 400 错误 | 预检必须发真实 prompt 验证 |
281	
282	---
283	
284	## 八、写论文前加载的 Skills
285	
286	写论文或做最终审查时，Director/Agent 应按需加载以下 skills：
287	- `latex-paper` — LaTeX 编译与格式
288	- `reference-audit` — 引用真实性审计
289	- `academic-writer` — ML 学术写作规范
290	- `paper-quality-lessons`（本 skill）— 实战经验教训
291	
292	---
293	
294	## 九、附录：投稿经验时间线教训
295	
296	1. **论文数字锁定时机**：最终编译前 24h 锁定所有数字，之后只允许格式修改
297	2. **GPU 不要空闲**：审稿期间如果 Agent 空闲，应该跑 ablation/扩展实验作为 rebuttal 储备
298	3. **匿名化提前做**：不要等到最后一天才检查路径泄露，fresh repo 需要时间清理
299	4. **9 页零余量策略**：NeurIPS 正文 9 页是硬限，每次新增内容必须等量压缩并编译验证
300	5. **Contingency 叙事提前写**：关键实验完成前就写好两版叙事，避免最后一刻仓促改稿
301	
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "parentUuid": "e83ce78c-fdee-4ad3-90cf-0b6b966cf2a1",
  "isSidechain": false,
  "promptId": "96f110f9-4fbd-4295-8cdb-ef5a8ad15d7a",
  "type": "user",
  "uuid": "89640095-9cd4-48c9-a610-3bea0b6b6614",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/agent-ml-research/skills/global/paper-quality-lessons.skill.md",
      "content": "---\nname: paper-quality-lessons\ndescription: NeurIPS 投稿实战经验总结——人工审查中提炼的写作规范、审查清单、常见反模式。Paper Agent / Reviewer / Director 写论文或审查论文时加载。\nallowed-tools: [Read, Write, Edit, Glob, Grep]\nscope: global\nversion: 1\ntags:\n  - writing\n  - paper\n  - quality\n  - checklist\n  - review\nroles:\n  - agent\n  - reviewer\n  - director\n  - paper_agent\n---\n\n# 论文写作质量指南（NeurIPS 实战经验）\n\n> 来源：2026 年 NeurIPS 投稿期间，从 20+ 项目的人工审查反馈中提炼。\n> 每条规则都源自真实的 bug / 退回 / 审稿质疑。\n\n---\n\n## 一、数据诚信与溯源（最高优先级）\n\n### 1.1 数字必须有源头\n\n- 论文中**每一个数字**必须可追溯到 registry 实验 ID 或原始结果文件\n- 禁止凭记忆写数字——必须 `cat result.json | head` + `ls -la` 附上文件证据\n- 计算值（均值、标准差、DID、delta）必须独立重算，不信 Agent 第一手汇报\n- `paper_provenance.yaml` 覆盖率必须 100%，改数字必须同步更新 provenance\n\n> **教训（D149 事件）**：Agent 曾伪造完整的 metrics 数据包括 p-value，事后被 Reviewer 独立 parse JSON 抓出。从此所有关键数据必须 Reviewer 独立验证到字段级别。\n\n### 1.2 不同来源数据不能混用\n\n- 配对数据必须同 seed、同 c 值、同 N、同 evaluation protocol\n- 两张表如果 protocol 不同（如 0-shot vs 8-shot），论文必须明确说明\n- 跨 config 比较 delta 会引入系统误差——必须补跑同 config baseline 后才能比较\n- 非等量对比必须显式标注（如 \"at unmatched volumes\"）\n\n> **教训（D027 事件）**：不同 config 文件的 baseline 不同，跨 config 比较 delta 值引入了 artifact。\n\n### 1.3 结论撤回后不可复活\n\n- 被 Director shelved 的数据（如因截断混淆），禁止重新引入论文\n- `paper_provenance.yaml` 中 `verified: false` 的 claim，不得恢复\n- 术语修正后不可回退（如 \"same norm\" → \"same per-layer standard deviation\"）\n\n---\n\n## 二、Claim 强度与数据匹配\n\n### 2.1 Claim 强度规则\n\n| 数据支撑 | 允许的最强表述 |\n|----------|--------------|\n| 单 seed, 单数据集 | \"preliminary observation\", \"initial evidence\" |\n| 单 seed, 多数据集 | \"suggestive pattern\", \"indicative trend\" |\n| 多 seed, 单数据集 | 报告均值±标准差，可写 \"we find\" |\n| 多 seed, 多数据集 | 可用 \"robust\", \"consistent\" |\n| 统计检验显著 | 可用 \"significant\", 附 p-value |\n| 单 seed + 外推到其他条件 | 必须加限定，不能声称 \"scale-invariant\" 等 |\n\n### 2.2 禁止的过强表述\n\n- \"remarkably stable\" → 改为 \"relatively stable\" 或给出量化波动范围\n- \"confirmed\" → 仅 \"suggestive\" 级别数据不能用\n- \"scale-invariant\" → single-seed 验证不够\n- \"We attribute X to Y\" → 如果是假说，必须改为 \"We hypothesize\" + \"requiring causal verification\"\n- \"roughly twice\" → 实际比值必须在 1.8x-2.2x 才能用，否则改为更准确的近似\n- \"domain-agnostic\" → 改为 \"robust across N domains tested\"\n\n### 2.3 Claim 降级机制\n\n当证据不足以支撑独立 claim 时，应降级为 discussion 中的定性讨论，而非删除。具体做法：\n- 独立 contribution → Discussion 段落\n- 硬 claim → 加 caveat 的软 claim\n- 正文数字 → 移入 Appendix\n\n---\n\n## 三、叙事与 Storytelling\n\n### 3.1 结构原则\n\n- 核心 paradox/发现之间必须有**过渡句**桥接，不能让读者在关键处断线\n- Introduction 每条 Contribution 必须有对应的 section/table 支撑\n- Discussion 不应重复 Results 的具体数字——引用表格编号\n- 同一解释不要在多处重复推导——主文写一次 + 指向 Appendix\n- Limitations 段不要写成一个 17 行大段——拆分为 2-3 个子段按主题分组\n\n### 3.2 冷引用（Cold Reference）\n\n- 任何首次出现的概念必须有上文铺垫\n- Introduction 贡献列表中不能突然出现未被提及的模型/方法名\n\n### 3.3 不要用旧叙事套新数字\n\n新 baseline 出来后若 delta 大幅变化，Section 的叙事逻辑必须重写，不是简单替换数字。\n\n### 3.4 Contingency Plan\n\n关键实验结果不确定时需预写两套叙事（如 \"若结果 A → 叙事 A\"、\"若结果 B → 叙事 B\"），实验完成后选择正确版本。提交前必须确认只留了一套。\n\n### 3.5 不要基于中间值做叙事决策\n\n70% 进度时的估计往往不够稳定（尤其 GSM8K 等难度分布不均匀的 benchmark），必须等完整数据再定稿叙事。\n\n---\n\n## 四、术语与一致性\n\n### 4.1 术语一致性\n\n- 全文必须统一使用正式定义的术语，不得出现同义词漂移\n- 术语定义后，每次使用必须完全一致（不要有时 \"perturbation sensitivity\" 有时 \"perturbation impact\"）\n\n### 4.2 统计量一致性\n\n- 两个不同的 kappa/p-value 每次出现时必须标注是哪个\n- 同一个 metric 在不同位置的数字必须完全一致\n- 修改任何数字后必须全文 grep 确认所有引用处同步\n\n### 4.3 p-value 格式\n\n- 无前导零、3 位小数：`p = .003`（不是 `p = 0.003`）\n- 当非劣效性 p<0.001 实际由正向效应驱动时，必须加括注说明\n\n### 4.4 例子与定义必须一致\n\nTaxonomy 中的定义和对应示例不能自相矛盾。如果定义说 \"no new content\"，示例中就不能包含新信息。\n\n---\n\n## 五、投稿前检查清单（Pre-Submission Checklist）\n\n### 5.1 占位符扫描（硬门禁）\n\n提交前必须 grep 扫描，以下模式要求**零匹配**：\n```\nXX.XX, PLACEHOLDER, [If , TODO, TBD, \\placeholder{\n```\n所有条件占位段落（`[If ...]`）必须替换为最终文本。\n\n### 5.2 编译检查\n\n- [ ] 编译零 error\n- [ ] 无 `??` 未解析引用\n- [ ] 无 > 1pt 的 overfull hbox\n- [ ] 正文 ≤ 9 页（NeurIPS desk reject 风险）\n- [ ] 使用当年 style file（`neurips_2026.sty`）\n- [ ] Review 版启用行号\n- [ ] 匿名审稿版无作者姓名、无致谢\n\n### 5.3 数据完整性\n\n- [ ] 论文所有数字与 registry/provenance 交叉验证通过\n- [ ] 计算值（均值、标准差、DID、delta）独立重算确认\n- [ ] 所有 evaluation protocol 差异已在论文中说明\n- [ ] 多 seed 结果报告均值和标准差\n- [ ] 单 seed 数据在 Limitations 中声明\n\n### 5.4 图表检查\n\n- [ ] 所有 figure PDF 存在且路径匹配\n- [ ] 图表不超栏宽（单栏 5.5in / 全宽 6.5in）\n- [ ] 图中字体 ≥ 7pt\n- [ ] 小数精度全表统一\n- [ ] 最优结果加粗、次优下划线\n- [ ] 表格标题（caption）自包含\n- [ ] Forest plot 等可视化无 dummy 值（CI_LO=-99 等）\n\n### 5.5 引用检查\n\n- [ ] 引用覆盖：**直接相关方法、baseline 论文、评测 benchmark 论文、理论基础**（任一缺失说明调研不充分）\n- [ ] 引用密度与目标会议近年录用论文同量级\n- [ ] 引用键与 bib 条目 1:1 匹配\n- [ ] 无孤儿 bib 条目\n- [ ] 无幻觉引用（所有被引论文实际存在）\n- [ ] 近年论文的年份/会议准确\n- [ ] 审稿人要求的引用全部补齐\n\n### 5.6 匿名化检查\n\n- [ ] 源代码无硬编码绝对路径（`/Users/...`, `/root/...`）\n- [ ] 配置文件无服务器路径\n- [ ] Git history 已清理 author 信息（用 fresh repo）\n- [ ] 项目管理文件不得提交（AGENTS.md, memory.md, registry.yaml, task_context/ 等）\n- [ ] API Keys 通过环境变量，无泄露\n\n### 5.7 会议 Checklist 填写（如目标会议要求）\n\n- [ ] Claims: 摘要/Introduction 准确反映实验范围\n- [ ] Limitations: 正文 Limitations 段 + Appendix 补充\n- [ ] Experiments: 实验设置完整（exp_id, seed, 超参, 评估 protocol）\n- [ ] Reproducibility: 数据集公开、代码可用\n- [ ] Statistical Significance: 多 seed 均值+标准差、置信区间\n- [ ] Compute: GPU 型号、训练时间、总 GPU-hours\n- [ ] Licenses: 数据集/模型引用完整\n- [ ] AI Assistants: 如实声明使用情况\n- [ ] 每项认真回答（不要全写 N/A）\n\n### 5.8 叙事完整性\n\n- [ ] Conclusion 包含所有关键限定符（如 \"under greedy decoding\"）\n- [ ] Abstract 与正文一致（不能一个写 \"single seed\" 另一个已是 \"10 seeds\"）\n- [ ] 无 Appendix Version A/B 两套叙事残留\n- [ ] 无 LaTeX 注释与正文混淆\n- [ ] Contribution claim 在 Introduction 中（不在 Related Work 中）\n- [ ] 所有专有名词/缩写首次出现时有定义（Abstract 内缩写也必须展开）\n- [ ] Introduction 与 Method/Results 讲同一条主线（idea 变化后全文逻辑一致）\n\n### 5.9 去 AI 风格检查\n\n- [ ] **`grep \"—\" paper/*.tex` 全文清零**（解释性 em-dash 必须全删，最显著的 AI 痕迹）\n- [ ] **`grep \" – \" paper/*.tex` 全文清零**（解释性 en-dash 必须全删）\n- [ ] 无 \"-ing,\" 分词短语结尾（如 \"..., demonstrating the effectiveness of...\"）\n- [ ] 无连续 \"Furthermore\" / \"Moreover\" / \"Additionally\"（同段最多 1 个）\n- [ ] 无 \"It is worth noting that...\" / \"Notably, ...\"\n- [ ] 无 \"delve into\" / \"leverage\" / \"utilize\" / \"a myriad of\" / \"a plethora of\"\n- [ ] 自然段 5-8 句是正常的，不要每 2-3 句就换段\n\n### 5.10 模板与同类论文核对\n\n- [ ] LaTeX 模板从目标会议官网下载（不是他人转载、不是上一年）\n- [ ] `\\documentclass[]{}` 选项匹配 review / camera-ready 阶段\n- [ ] 写作前已参考 2-3 篇同领域近 1-2 年优秀论文，叙事节奏对齐\n\n---\n\n## 六、Reviewer 审查标准\n\n### 6.1 CRITICAL 级别（必须修复才能提交）\n\n- 论文数字与实验数据不一致\n- Abstract 与正文矛盾\n- Evaluation protocol 混淆（如 0-shot 写成 8-shot）\n- 未经验证的数据写入论文\n- 占位符残留\n\n### 6.2 WARNING 级别（应当修复）\n\n- Stale claims（更新了某处数字但忘了同步其他位置）\n- 过强措辞不匹配数据支撑\n- 隐式全因子设计误导（如写 \"3×3×3=27\" 但实际只有 15 格）\n- 评估指标只描述了部分 domain\n- 旧版数据引用\n\n### 6.3 数据一致性审查流程\n\n1. 从 registry 提取所有实验 metrics\n2. 对照论文中每一个内联数字（到行号级别）\n3. 独立重算所有衍生值\n4. 不一致处标注为 CRITICAL\n5. 近似表述检查实际比值是否在允许范围内\n\n---\n\n## 七、常见反模式速查表\n\n| 反模式 | 症状 | 修复方式 |\n|--------|------|----------|\n| Stale claim | 论文某处还引用旧数字 | 改数字后全文 grep 同步 |\n| Protocol 混淆 | 不同表格用了不同 evaluation 但没说明 | 每张表注明 protocol |\n| Agent 误报 | 实验结果缺乏文件证据 | 要求 `cat result.json` 截图 |\n| 混用数据算比值 | 跨 seed/条件/N 的数据混合比较 | 只用严格配对的数据 |\n| 叙事超越数据 | \"confirmed\" 但实际只是 suggestive | 匹配 claim 强度到 §2.1 |\n| 冷引用 | 首次出现的概念无铺垫 | 先建立框架再引入 |\n| 定义-例子矛盾 | Taxonomy 定义和示例冲突 | 审查所有定义与其示例 |\n| Placeholder 残留 | XX.XX, TODO, [If...] 未清理 | 提交前 grep 硬门禁 |\n| Path 泄露 | 代码/config 含服务器绝对路径 | 改为相对路径 |\n| 重复推导 | 同一解释在 3 处各自推导一遍 | 主文一次 + 引用 Appendix |\n| Discussion 重复 Results | Discussion 大量复制 Results 数字 | 改为引用表格编号 |\n| 单 seed overclaim | 单 seed 数据声称 scale-invariant | 加 preliminary/hedging 限定 |\n| Registry 不同步 | Registry 面值与实际状态不一致 | 以 SSH 实测为准 |\n| vLLM 静默失败 | max_model_len 太小导致 100% 400 错误 | 预检必须发真实 prompt 验证 |\n\n---\n\n## 八、写论文前加载的 Skills\n\n写论文或做最终审查时，Director/Agent 应按需加载以下 skills：\n- `latex-paper` — LaTeX 编译与格式\n- `reference-audit` — 引用真实性审计\n- `academic-writer` — ML 学术写作规范\n- `paper-quality-lessons`（本 skill）— 实战经验教训\n\n---\n\n## 九、附录：投稿经验时间线教训\n\n1. **论文数字锁定时机**：最终编译前 24h 锁定所有数字，之后只允许格式修改\n2. **GPU 不要空闲**：审稿期间如果 Agent 空闲，应该跑 ablation/扩展实验作为 rebuttal 储备\n3. **匿名化提前做**：不要等到最后一天才检查路径泄露，fresh repo 需要时间清理\n4. **9 页零余量策略**：NeurIPS 正文 9 页是硬限，每次新增内容必须等量压缩并编译验证\n5. **Contingency 叙事提前写**：关键实验完成前就写好两版叙事，避免最后一刻仓促改稿\n",
      "numLines": 301,
      "startLine": 1,
      "totalLines": 301
    }
  },
  "sourceToolAssistantUUID": "e83ce78c-fdee-4ad3-90cf-0b6b966cf2a1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/.claude/sessions/paper_audit_content_b575bb0e",
  "sessionId": "1db729b7-6c37-474e-9cbb-179c13a8aeb8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
````

</details>

---

### Tool call

_source line 15 · 2026-05-24T16:16:01.070Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01B4WAfTukFfNHAUFqRAJ9MP`</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "89640095-9cd4-48c9-a610-3bea0b6b6614",
  "isSidechain": false,
  "requestId": "req_011CbMh9LTERdQfLwLWw7G3r",
  "type": "assistant",
  "uuid": "7ae8ddf1-0acb-4709-a4d7-2b92c72b4553",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/.claude/sessions/paper_audit_content_b575bb0e",
  "sessionId": "1db729b7-6c37-474e-9cbb-179c13a8aeb8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015mKFFcLQ2b7ySBZy5JxXX9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 26401,
      "cache_read_input_tokens": 11846,
      "output_tokens": 312,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 26401,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 312,
          "cache_read_input_tokens": 11846,
          "cache_creation_input_tokens": 26401,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 26401
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
  "lastPrompt": "项目：trace-verdict-study Venue：emnlp-2026 论文目录：/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper  Phase 1 确定性检查结果： 源码检查: passed=False, 6 critical, 17 warning 一致性检查:…",
  "leafUuid": "dfa18b10-ca9b-49ca-b601-bbfa25d7d0eb",
  "sessionId": "1db729b7-6c37-474e-9cbb-179c13a8aeb8"
}
```

---

### Runtime record

_source line 17_

```json
{
  "type": "ai-title",
  "aiTitle": "Audit trace-verdict-study EMNLP 2026 submission",
  "sessionId": "1db729b7-6c37-474e-9cbb-179c13a8aeb8"
}
```

---

### Assistant

_source line 18 · 2026-05-24T16:16:11.395Z_

<details><summary>Logged reasoning block</summary>

```text
Now let me read all the .tex files to perform the audit. Let me read them all in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dfa18b10-ca9b-49ca-b601-bbfa25d7d0eb",
  "isSidechain": false,
  "requestId": "req_011CbMh9tV4aN8QV3riH9wUf",
  "type": "assistant",
  "uuid": "b1444880-a389-4228-8711-ec4a3f87d518",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/.claude/sessions/paper_audit_content_b575bb0e",
  "sessionId": "1db729b7-6c37-474e-9cbb-179c13a8aeb8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012VsV8ncx6FrdGuWaCHMfaG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11894,
      "cache_read_input_tokens": 38247,
      "output_tokens": 703,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11894,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 703,
          "cache_read_input_tokens": 38247,
          "cache_creation_input_tokens": 11894,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11894
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

_source line 19 · 2026-05-24T16:16:11.934Z_

读取所有 .tex 源文件。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b1444880-a389-4228-8711-ec4a3f87d518",
  "isSidechain": false,
  "requestId": "req_011CbMh9tV4aN8QV3riH9wUf",
  "type": "assistant",
  "uuid": "74985fdb-191f-444e-a8a6-46b35b4adadf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/.claude/sessions/paper_audit_content_b575bb0e",
  "sessionId": "1db729b7-6c37-474e-9cbb-179c13a8aeb8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012VsV8ncx6FrdGuWaCHMfaG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11894,
      "cache_read_input_tokens": 38247,
      "output_tokens": 703,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11894,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 703,
          "cache_read_input_tokens": 38247,
          "cache_creation_input_tokens": 11894,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11894
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

_source line 20 · 2026-05-24T16:16:12.614Z_

<details open><summary>🔧 Tool call — Read · `toolu_017opmvjH6oDSZ32qhnTBt8L`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "74985fdb-191f-444e-a8a6-46b35b4adadf",
  "isSidechain": false,
  "requestId": "req_011CbMh9tV4aN8QV3riH9wUf",
  "type": "assistant",
  "uuid": "19ba1e7e-6ce8-4c08-97be-41f94e2be035",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/.claude/sessions/paper_audit_content_b575bb0e",
  "sessionId": "1db729b7-6c37-474e-9cbb-179c13a8aeb8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012VsV8ncx6FrdGuWaCHMfaG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11894,
      "cache_read_input_tokens": 38247,
      "output_tokens": 703,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11894,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 703,
          "cache_read_input_tokens": 38247,
          "cache_creation_input_tokens": 11894,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11894
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

_source line 21 · 2026-05-24T16:16:16.800Z_

<details><summary>↩ Tool result · `toolu_01RxnRbbWWzPB2ainkYSrqsw`</summary>

```text
1	\documentclass[11pt,a4paper]{article}
2	\usepackage[review]{acl}
3	\usepackage{times,latexsym}
4	\usepackage{booktabs}
5	
6	\title{ARR Reproducibility Checklist\\(Supplementary Material)}
7	\author{Anonymous ACL submission}
8	
9	\begin{document}
10	\maketitle
11	
12	\section*{Responsible NLP Research Checklist}
13	
14	\subsection*{A. Limitations and Risks}
15	
16	\begin{enumerate}
17	\item \textbf{Did you discuss the limitations of your work?} \\
18	\textit{Yes.} A dedicated Limitations section discusses: single-dataset scope (with DebugBench cross-validation), four models across three architecture families (1.5B--13B), seed-dependent variance on DeepSeek, the invalidated full\_trace run, generator--evaluator overlap, self-familiarity bias, error distribution assumptions, and task scope limited to verdict prediction.
19	
20	\item \textbf{Did you discuss any potential risks of your work?} \\
21	\textit{Yes.} The Ethics Statement notes that the work uses public benchmarks, involves no human subjects, and has minimal environmental impact. Verdict prediction is a developer-facing tool with no direct end-user impact.
22	\end{enumerate}
23	
24	\subsection*{B. Did you use or create scientific artifacts?}
25	
26	\begin{enumerate}
27	\item \textbf{Did you cite the creators of artifacts you used?} \\
28	\textit{Yes.} HumanEval \cite{chen2021evaluating}, MBPP-sanitized \cite{austin2021program}, DebugBench \cite{tian2024debugbench}, Qwen-2.5-Coder-7B/1.5B-Instruct \cite{qwen2024coder}, CodeLlama-13B-Instruct \cite{roziere2024code}, DeepSeek-Coder-6.7B-Instruct \cite{deepseek2024coder}, LoRA \cite{hu2022lora}, and TRL SFTTrainer are all cited.
29	
30	\item \textbf{Did you discuss the license or terms for use and/or distribution of any artifacts?} \\
31	\textit{Partial.} All base models and datasets are publicly available. HumanEval is released under MIT license; MBPP under CC-BY-4.0; DebugBench under MIT. Model licenses: Qwen-2.5-Coder under Apache 2.0; DeepSeek-Coder under the DeepSeek License.
32	
33	\item \textbf{Did you discuss if your use of existing artifacts was consistent with their intended use?} \\
34	\textit{Yes.} HumanEval and MBPP are standard code generation benchmarks; we use their canonical test cases for verdict evaluation, consistent with their evaluation purpose. DebugBench is designed for debugging evaluation.
35	
36	\item \textbf{Did you discuss the steps taken to check whether the data contains any information that names or uniquely identifies individual people or offensive content?} \\
37	\textit{N/A.} All datasets contain only programming problems and solutions with no personal information.
38	\end{enumerate}
39	
40	\subsection*{C. Computational Experiments}
41	
42	\begin{enumerate}
43	\item \textbf{Did you report the number of parameters in the models used, the total computational budget, and computing infrastructure?} \\
44	\textit{Yes.}
45	\begin{itemize}
46	\item Models: Qwen-2.5-Coder-7B/1.5B-Instruct (7B/1.5B parameters), CodeLlama-13B-Instruct (13B parameters), DeepSeek-Coder-6.7B-Instruct (6.7B parameters). Only LoRA adapters are trained (rank=16, $\alpha$=32, targeting all linear layers).
47	\item Hardware: 2$\times$ high-end datacenter GPUs (${\sim}$96\,GB VRAM each); each experiment uses a single GPU.
48	\item Total compute: ${\sim}$320 GPU-hours across all conditions, models, seeds, and iterative refinements (${\sim}$170h for successful experiments; individual runs 0.5--2.2h). See Appendix~B for per-condition wall-clock times.
49	\end{itemize}
50	
51	\item \textbf{Did you report all hyperparameters?} \\
52	\textit{Yes.} Appendix~B (Table~5) reports: LoRA rank (16), alpha (32), dropout (0.05), target modules (all linear layers), epochs (3), per-device batch size (4), gradient accumulation steps (8), effective batch size (32), learning rate ($2 \times 10^{-4}$), LR scheduler (linear decay), warmup ratio (0.1), weight decay (0.01), max sequence length (2,048 tokens).
53	
54	\item \textbf{Did you report descriptive statistics about your results?} \\
55	\textit{Yes.} All accuracy values include Wilson 95\% confidence intervals. Pairwise comparisons use paired bootstrap resampling ($B{=}10{,}000$, seed=42) with reported $p$-values. We report multi-seed results (seeds 42, 123, 456) for the exception\_only condition; other conditions report single-seed results. Standard deviations are provided where multiple seeds are available.
56	
57	\item \textbf{If you used existing packages, did you report the implementation, model, and their versions?} \\
58	\textit{Yes.} HuggingFace TRL SFTTrainer with LoRA via PEFT. Base model identifiers: \texttt{Qwen/Qwen2.5-Coder-7B-Instruct} and \texttt{deepseek-ai/deepseek-coder-6.7b-instruct}.
59	\end{enumerate}
60	
61	\subsection*{D. Human Annotations}
62	
63	\begin{enumerate}
64	\item \textbf{Did you use human annotators?} \\
65	\textit{No.} All labels (pass/fail) are derived from automated test execution. No human annotation was involved.
66	\end{enumerate}
67	
68	\subsection*{E. Data and Code Availability}
69	
70	\begin{itemize}
71	\item \textbf{Code}: Training, evaluation, and trace preprocessing scripts will be released upon acceptance.
72	\item \textbf{Data}: Execution traces, VOTA-compressed traces, and train/test splits will be released. Raw traces are generated deterministically from publicly available benchmarks using Python \texttt{sys.settrace}.
73	\item \textbf{Models}: LoRA adapters for all conditions will be released on HuggingFace.
74	\end{itemize}
75	
76	\subsection*{F. Reproducibility Summary}
77	
78	\begin{table}[h]
79	\centering
80	\small
81	\begin{tabular}{lc}
82	\toprule
83	\textbf{Item} & \textbf{Status} \\
84	\midrule
85	All hyperparameters reported & Yes \\
86	Random seeds specified & Yes (42, 123, 456) \\
87	Error bars / CIs reported & Yes (Wilson 95\% CI) \\
88	Statistical tests reported & Yes (bootstrap, McNemar) \\
89	Computing infrastructure reported & Yes \\
90	Training time reported & Yes \\
91	Code release planned & Yes \\
92	Data release planned & Yes \\
93	Model release planned & Yes \\
94	\bottomrule
95	\end{tabular}
96	\caption{Reproducibility checklist summary.}
97	\end{table}
98	
99	\bibliography{references}
100	
101	\end{document}
102	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7126252f-3d4b-40ac-82a7-27252622b40d",
  "isSidechain": false,
  "promptId": "96f110f9-4fbd-4295-8cdb-ef5a8ad15d7a",
  "type": "user",
  "uuid": "a6fea0b6-94a7-4b40-b9d4-01d782a6184d",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/arr_checklist.tex",
      "content": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[review]{acl}\n\\usepackage{times,latexsym}\n\\usepackage{booktabs}\n\n\\title{ARR Reproducibility Checklist\\\\(Supplementary Material)}\n\\author{Anonymous ACL submission}\n\n\\begin{document}\n\\maketitle\n\n\\section*{Responsible NLP Research Checklist}\n\n\\subsection*{A. Limitations and Risks}\n\n\\begin{enumerate}\n\\item \\textbf{Did you discuss the limitations of your work?} \\\\\n\\textit{Yes.} A dedicated Limitations section discusses: single-dataset scope (with DebugBench cross-validation), four models across three architecture families (1.5B--13B), seed-dependent variance on DeepSeek, the invalidated full\\_trace run, generator--evaluator overlap, self-familiarity bias, error distribution assumptions, and task scope limited to verdict prediction.\n\n\\item \\textbf{Did you discuss any potential risks of your work?} \\\\\n\\textit{Yes.} The Ethics Statement notes that the work uses public benchmarks, involves no human subjects, and has minimal environmental impact. Verdict prediction is a developer-facing tool with no direct end-user impact.\n\\end{enumerate}\n\n\\subsection*{B. Did you use or create scientific artifacts?}\n\n\\begin{enumerate}\n\\item \\textbf{Did you cite the creators of artifacts you used?} \\\\\n\\textit{Yes.} HumanEval \\cite{chen2021evaluating}, MBPP-sanitized \\cite{austin2021program}, DebugBench \\cite{tian2024debugbench}, Qwen-2.5-Coder-7B/1.5B-Instruct \\cite{qwen2024coder}, CodeLlama-13B-Instruct \\cite{roziere2024code}, DeepSeek-Coder-6.7B-Instruct \\cite{deepseek2024coder}, LoRA \\cite{hu2022lora}, and TRL SFTTrainer are all cited.\n\n\\item \\textbf{Did you discuss the license or terms for use and/or distribution of any artifacts?} \\\\\n\\textit{Partial.} All base models and datasets are publicly available. HumanEval is released under MIT license; MBPP under CC-BY-4.0; DebugBench under MIT. Model licenses: Qwen-2.5-Coder under Apache 2.0; DeepSeek-Coder under the DeepSeek License.\n\n\\item \\textbf{Did you discuss if your use of existing artifacts was consistent with their intended use?} \\\\\n\\textit{Yes.} HumanEval and MBPP are standard code generation benchmarks; we use their canonical test cases for verdict evaluation, consistent with their evaluation purpose. DebugBench is designed for debugging evaluation.\n\n\\item \\textbf{Did you discuss the steps taken to check whether the data contains any information that names or uniquely identifies individual people or offensive content?} \\\\\n\\textit{N/A.} All datasets contain only programming problems and solutions with no personal information.\n\\end{enumerate}\n\n\\subsection*{C. Computational Experiments}\n\n\\begin{enumerate}\n\\item \\textbf{Did you report the number of parameters in the models used, the total computational budget, and computing infrastructure?} \\\\\n\\textit{Yes.}\n\\begin{itemize}\n\\item Models: Qwen-2.5-Coder-7B/1.5B-Instruct (7B/1.5B parameters), CodeLlama-13B-Instruct (13B parameters), DeepSeek-Coder-6.7B-Instruct (6.7B parameters). Only LoRA adapters are trained (rank=16, $\\alpha$=32, targeting all linear layers).\n\\item Hardware: 2$\\times$ high-end datacenter GPUs (${\\sim}$96\\,GB VRAM each); each experiment uses a single GPU.\n\\item Total compute: ${\\sim}$320 GPU-hours across all conditions, models, seeds, and iterative refinements (${\\sim}$170h for successful experiments; individual runs 0.5--2.2h). See Appendix~B for per-condition wall-clock times.\n\\end{itemize}\n\n\\item \\textbf{Did you report all hyperparameters?} \\\\\n\\textit{Yes.} Appendix~B (Table~5) reports: LoRA rank (16), alpha (32), dropout (0.05), target modules (all linear layers), epochs (3), per-device batch size (4), gradient accumulation steps (8), effective batch size (32), learning rate ($2 \\times 10^{-4}$), LR scheduler (linear decay), warmup ratio (0.1), weight decay (0.01), max sequence length (2,048 tokens).\n\n\\item \\textbf{Did you report descriptive statistics about your results?} \\\\\n\\textit{Yes.} All accuracy values include Wilson 95\\% confidence intervals. Pairwise comparisons use paired bootstrap resampling ($B{=}10{,}000$, seed=42) with reported $p$-values. We report multi-seed results (seeds 42, 123, 456) for the exception\\_only condition; other conditions report single-seed results. Standard deviations are provided where multiple seeds are available.\n\n\\item \\textbf{If you used existing packages, did you report the implementation, model, and their versions?} \\\\\n\\textit{Yes.} HuggingFace TRL SFTTrainer with LoRA via PEFT. Base model identifiers: \\texttt{Qwen/Qwen2.5-Coder-7B-Instruct} and \\texttt{deepseek-ai/deepseek-coder-6.7b-instruct}.\n\\end{enumerate}\n\n\\subsection*{D. Human Annotations}\n\n\\begin{enumerate}\n\\item \\textbf{Did you use human annotators?} \\\\\n\\textit{No.} All labels (pass/fail) are derived from automated test execution. No human annotation was involved.\n\\end{enumerate}\n\n\\subsection*{E. Data and Code Availability}\n\n\\begin{itemize}\n\\item \\textbf{Code}: Training, evaluation, and trace preprocessing scripts will be released upon acceptance.\n\\item \\textbf{Data}: Execution traces, VOTA-compressed traces, and train/test splits will be released. Raw traces are generated deterministically from publicly available benchmarks using Python \\texttt{sys.settrace}.\n\\item \\textbf{Models}: LoRA adapters for all conditions will be released on HuggingFace.\n\\end{itemize}\n\n\\subsection*{F. Reproducibility Summary}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lc}\n\\toprule\n\\textbf{Item} & \\textbf{Status} \\\\\n\\midrule\nAll hyperparameters reported & Yes \\\\\nRandom seeds specified & Yes (42, 123, 456) \\\\\nError bars / CIs reported & Yes (Wilson 95\\% CI) \\\\\nStatistical tests reported & Yes (bootstrap, McNemar) \\\\\nComputing infrastructure reported & Yes \\\\\nTraining time reported & Yes \\\\\nCode release planned & Yes \\\\\nData release planned & Yes \\\\\nModel release planned & Yes \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Reproducibility checklist summary.}\n\\end{table}\n\n\\bibliography{references}\n\n\\end{document}\n",
      "numLines": 102,
      "startLine": 1,
      "totalLines": 102
    }
  },
  "sourceToolAssistantUUID": "7126252f-3d4b-40ac-82a7-27252622b40d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/.claude/sessions/paper_audit_content_b575bb0e",
  "sessionId": "1db729b7-6c37-474e-9cbb-179c13a8aeb8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-24T16:16:12.620Z_

<details><summary>↩ Tool result · `toolu_017opmvjH6oDSZ32qhnTBt8L`</summary>

```text
1	\documentclass[11pt,a4paper]{article}
2	\usepackage[review]{acl}
3	% \usepackage{acl}  % uncomment for camera-ready (remove [review])
4	\usepackage{times,latexsym}
5	\usepackage{amsmath,amssymb}
6	\usepackage{graphicx}
7	\graphicspath{{../../figures/paper/}}
8	\usepackage{booktabs}
9	\usepackage{multirow}
10	\usepackage{xcolor}
11	\usepackage{algorithm}
12	\usepackage{algorithmic}
13	
14	\title{Complete Execution Traces Degrade SFT-Based Verdict Prediction: \\A Diagnostic Signal Analysis}
15	\author{Anonymous ACL submission}
16	
17	\begin{document}
18	\maketitle
19	
20	\begin{abstract}
21	Complete execution traces contain all information needed for verdict prediction---classifying whether a test passes or fails---yet they actively degrade SFT-based learning.
22	Across four code-specialized models (1.5B--13B parameters, three architecture families), complete traces achieve only 77--82\% accuracy while compact exception events reach ${\geq}$99.33\%.
23	Controlled gradient masking attributes ${\leq}$4\% of this 18--23pp gap to training-time dilution; the dominant factor is content quality at inference, where diagnostic tokens are too sparse in verbose traces for reliable extraction.
24	With exception-only input, a 7B model surpasses GPT-4o by 12pp---a ranking that reverses without trace information, demonstrating that input density dominates model scale.
25	SFT also retains 97.65\% accuracy under format-marker removal and transfers bidirectionally across datasets, confirming learned diagnostic patterns rather than surface shortcuts.
26	These results establish a two-tier signal hierarchy: extract exception events first; when unavailable, tail-truncated traces (${\geq}$512 tokens) provide a viable fallback.
27	\end{abstract}
28	
29	\input{introduction}
30	\input{related_work}
31	\input{method}
32	\input{experiments}
33	\input{discussion}
34	\input{conclusion}
35	
36	\section*{Limitations}
37	
38	All experiments use Python-only benchmarks (HumanEval, MBPP-sanitized; 591 problems with simple assert-based tests); generalization to other languages, non-assert test frameworks, and multi-file projects is unverified.
39	All four models (1.5B--13B) are code-specialized; 30B+ models or general-purpose LLMs may behave differently.
40	Multi-seed experiments use 3 seeds; several baselines rely on single-seed results with Wilson CI variance estimates.
41	
42	\bibliography{references}
43	
44	\appendix
45	\input{appendix}
46	
47	\end{document}
48	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "19ba1e7e-6ce8-4c08-97be-41f94e2be035",
  "isSidechain": false,
  "promptId": "96f110f9-4fbd-4295-8cdb-ef5a8ad15d7a",
  "type": "user",
  "uuid": "f6bb5aec-e839-4a39-b3a5-08e9d2b3ed71",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/main.tex",
      "content": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[review]{acl}\n% \\usepackage{acl}  % uncomment for camera-ready (remove [review])\n\\usepackage{times,latexsym}\n\\usepackage{amsmath,amssymb}\n\\usepackage{graphicx}\n\\graphicspath{{../../figures/paper/}}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{algorithm}\n\\usepackage{algorithmic}\n\n\\title{Complete Execution Traces Degrade SFT-Based Verdict Prediction: \\\\A Diagnostic Signal Analysis}\n\\author{Anonymous ACL submission}\n\n\\begin{document}\n\\maketitle\n\n\\begin{abstract}\nComplete execution traces contain all information needed for verdict prediction---classifying whether a test passes or fails---yet they actively degrade SFT-based learning.\nAcross four code-specialized models (1.5B--13B parameters, three architecture families), complete traces achieve only 77--82\\% accuracy while compact exception events reach ${\\geq}$99.33\\%.\nControlled gradient masking attributes ${\\leq}$4\\% of this 18--23pp gap to training-time dilution; the dominant factor is content quality at inference, where diagnostic tokens are too sparse in verbose traces for reliable extraction.\nWith exception-only input, a 7B model surpasses GPT-4o by 12pp---a ranking that reverses without trace information, demonstrating that input density dominates model scale.\nSFT also retains 97.65\\% accuracy under format-marker removal and transfers bidirectionally across datasets, confirming learned diagnostic patterns rather than surface shortcuts.\nThese results establish a two-tier signal hierarchy: extract exception events first; when unavailable, tail-truncated traces (${\\geq}$512 tokens) provide a viable fallback.\n\\end{abstract}\n\n\\input{introduction}\n\\input{related_work}\n\\input{method}\n\\input{experiments}\n\\input{discussion}\n\\input{conclusion}\n\n\\section*{Limitations}\n\nAll experiments use Python-only benchmarks (HumanEval, MBPP-sanitized; 591 problems with simple assert-based tests); generalization to other languages, non-assert test frameworks, and multi-file projects is unverified.\nAll four models (1.5B--13B) are code-specialized; 30B+ models or general-purpose LLMs may behave differently.\nMulti-seed experiments use 3 seeds; several baselines rely on single-seed results with Wilson CI variance estimates.\n\n\\bibliography{references}\n\n\\appendix\n\\input{appendix}\n\n\\end{document}\n",
      "numLines": 48,
      "startLine": 1,
      "totalLines": 48
    }
  },
  "sourceToolAssistantUUID": "19ba1e7e-6ce8-4c08-97be-41f94e2be035",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/.claude/sessions/paper_audit_content_b575bb0e",
  "sessionId": "1db729b7-6c37-474e-9cbb-179c13a8aeb8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-24T16:16:13.421Z_

<details open><summary>🔧 Tool call — Read · `toolu_01RLgu1Sz5eq8opQojQMMD6J`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f6bb5aec-e839-4a39-b3a5-08e9d2b3ed71",
  "isSidechain": false,
  "requestId": "req_011CbMh9tV4aN8QV3riH9wUf",
  "type": "assistant",
  "uuid": "1c1213a5-f67f-4466-81bd-c86a10b5de96",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/.claude/sessions/paper_audit_content_b575bb0e",
  "sessionId": "1db729b7-6c37-474e-9cbb-179c13a8aeb8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012VsV8ncx6FrdGuWaCHMfaG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11894,
      "cache_read_input_tokens": 38247,
      "output_tokens": 703,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11894,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 703,
          "cache_read_input_tokens": 38247,
          "cache_creation_input_tokens": 11894,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11894
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

_source line 24 · 2026-05-24T16:16:13.430Z_

<details><summary>↩ Tool result · `toolu_01RLgu1Sz5eq8opQojQMMD6J`</summary>

```text
1	\section{Introduction}
2	
3	Execution traces (line-by-line records of a program's runtime behavior) have emerged as a promising input modality for code language models \citep{chen2025tracepile,ding2024traced,wang2025dcsh,ni2024next}.
4	The intuition is straightforward: more execution information should help the model make better predictions.
5	Yet for verdict prediction (classifying whether a test passes or fails), this intuition is wrong.
6	Complete traces \emph{actively degrade} accuracy compared to compact exception events, despite containing strictly more information.
7	
8	Prior work found trace utility to be task-dependent \citep{wang2025dcsh}, but focused on generation-oriented tasks where output noise confounds the analysis.
9	Verdict prediction offers a cleaner testbed: as binary classification, it isolates the learning signal from generation noise, and controlled component ablation directly measures how trace content affects SFT learning.
10	This approach aligns with recent *ACL precedent: CRUXEval \citep{gu2024cruxeval} uses execution prediction to probe code reasoning, and NExT \citep{ni2024next} uses trace-augmented chain-of-thought for program repair.
11	
12	We present a systematic component ablation of trace representations for verdict prediction.
13	Using 591 problems from HumanEval \citep{chen2021evaluating} and MBPP-sanitized \citep{austin2021program}, we evaluate four models across three architecture families and 1.5B to 13B parameters: Qwen-2.5-Coder-7B/1.5B-Instruct \citep{qwen2024coder}, CodeLlama-13B-Instruct \citep{roziere2024code}, and DeepSeek-Coder-6.7B-Instruct \citep{deepseek2024coder}.
14	
15	The central result: complete traces (77--82\%) barely improve over source code alone, while compact exception events achieve near-perfect accuracy (${\geq}$99\%) across all four models, an 18--23pp gap (\S\ref{sec:cross_model}).
16	A simple regex exploiting a format marker matches this ceiling, so the interesting question is not why exceptions help but \emph{why complete traces hurt}.
17	Marker removal collapses the regex to near-chance while SFT retains $>$97\%; cross-dataset transfer confirms SFT acquires diagnostic patterns beyond format matching (\S\ref{sec:nomarker}).
18	
19	Gradient masking attributes ${\leq}$4\% of the degradation to gradient dilution; content quality at inference accounts for the majority (\S\ref{sec:density}).
20	Training dynamics corroborate this: \texttt{exception\_only} converges within 50 steps while \texttt{full\_trace} oscillates without convergence (Appendix~\ref{sec:training_dynamics}).
21	A tail-truncation budget sweep reveals a sharp performance transition near 512 tokens, coinciding with the first appearance of structured execution markers (\S\ref{sec:trace_length}).
22	
23	While exception events structurally encode verdict direction (exception present typically implies failure), the non-trivial finding is that providing strictly more information (complete traces containing all exception data) degrades performance by 18--23pp.
24	Our contributions:
25	\begin{enumerate}
26	\item \textbf{Complete traces degrade SFT verdict accuracy} despite containing all diagnostic information: across four models (1.5B--13B, three families), complete traces (77--82\%) remain near source-code-only levels while compact exception events close an 18--23pp gap to ${\geq}$99.33\% (\S\ref{sec:cross_model}).
27	
28	\item \textbf{Semantic vs.\ format-marker decomposition}: marker removal collapses a format-exploiting regex by 71pp while SFT drops only 2pp; cross-dataset transfer (99.4--100\%) shows the learned signal generalizes beyond format markers (\S\ref{sec:nomarker}).
29	
30	\item \textbf{A two-tier signal hierarchy}: exception/assertion signals (${\geq}$98.53\%) dominate loop compression (77--86\%) by 12+pp with non-overlapping CIs; a sharp transition at ${\sim}$512 tail tokens yields a practical fallback (\S\ref{sec:ablation}, \S\ref{sec:trace_length}).
31	
32	\item \textbf{Mechanistic decomposition}: controlled gradient masking attributes ${\leq}$4\% of the degradation to gradient dilution, assigning the majority to content quality at inference, though forward-pass attention is an unquantified residual (\S\ref{sec:density}).
33	\end{enumerate}
34	
35	\begin{figure*}[t]
36	\centering
37	\includegraphics[width=\textwidth]{fig1_trace_overview}
38	\vspace{-8pt}
39	\caption{Overview of the verdict prediction pipeline. Source code and a test input are executed to produce a full raw trace. Four conditions vary the trace information: \texttt{no\_trace} (75.13\%), \texttt{full\_trace} (81.44\%), VOTA (99.05\%), and \texttt{exception\_only} (99.83\%). Accuracies for Qwen-2.5-7B ($N{=}1{,}190$); multi-seed means where available (Table~\ref{tab:ablation}). Appendix~\ref{sec:vota_examples} provides input/output examples.}
40	\label{fig:trace_overview}
41	\end{figure*}
42	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1c1213a5-f67f-4466-81bd-c86a10b5de96",
  "isSidechain": false,
  "promptId": "96f110f9-4fbd-4295-8cdb-ef5a8ad15d7a",
  "type": "user",
  "uuid": "ed362203-00e0-4e07-814e-1ef07f682150",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/introduction.tex",
      "content": "\\section{Introduction}\n\nExecution traces (line-by-line records of a program's runtime behavior) have emerged as a promising input modality for code language models \\citep{chen2025tracepile,ding2024traced,wang2025dcsh,ni2024next}.\nThe intuition is straightforward: more execution information should help the model make better predictions.\nYet for verdict prediction (classifying whether a test passes or fails), this intuition is wrong.\nComplete traces \\emph{actively degrade} accuracy compared to compact exception events, despite containing strictly more information.\n\nPrior work found trace utility to be task-dependent \\citep{wang2025dcsh}, but focused on generation-oriented tasks where output noise confounds the analysis.\nVerdict prediction offers a cleaner testbed: as binary classification, it isolates the learning signal from generation noise, and controlled component ablation directly measures how trace content affects SFT learning.\nThis approach aligns with recent *ACL precedent: CRUXEval \\citep{gu2024cruxeval} uses execution prediction to probe code reasoning, and NExT \\citep{ni2024next} uses trace-augmented chain-of-thought for program repair.\n\nWe present a systematic component ablation of trace representations for verdict prediction.\nUsing 591 problems from HumanEval \\citep{chen2021evaluating} and MBPP-sanitized \\citep{austin2021program}, we evaluate four models across three architecture families and 1.5B to 13B parameters: Qwen-2.5-Coder-7B/1.5B-Instruct \\citep{qwen2024coder}, CodeLlama-13B-Instruct \\citep{roziere2024code}, and DeepSeek-Coder-6.7B-Instruct \\citep{deepseek2024coder}.\n\nThe central result: complete traces (77--82\\%) barely improve over source code alone, while compact exception events achieve near-perfect accuracy (${\\geq}$99\\%) across all four models, an 18--23pp gap (\\S\\ref{sec:cross_model}).\nA simple regex exploiting a format marker matches this ceiling, so the interesting question is not why exceptions help but \\emph{why complete traces hurt}.\nMarker removal collapses the regex to near-chance while SFT retains $>$97\\%; cross-dataset transfer confirms SFT acquires diagnostic patterns beyond format matching (\\S\\ref{sec:nomarker}).\n\nGradient masking attributes ${\\leq}$4\\% of the degradation to gradient dilution; content quality at inference accounts for the majority (\\S\\ref{sec:density}).\nTraining dynamics corroborate this: \\texttt{exception\\_only} converges within 50 steps while \\texttt{full\\_trace} oscillates without convergence (Appendix~\\ref{sec:training_dynamics}).\nA tail-truncation budget sweep reveals a sharp performance transition near 512 tokens, coinciding with the first appearance of structured execution markers (\\S\\ref{sec:trace_length}).\n\nWhile exception events structurally encode verdict direction (exception present typically implies failure), the non-trivial finding is that providing strictly more information (complete traces containing all exception data) degrades performance by 18--23pp.\nOur contributions:\n\\begin{enumerate}\n\\item \\textbf{Complete traces degrade SFT verdict accuracy} despite containing all diagnostic information: across four models (1.5B--13B, three families), complete traces (77--82\\%) remain near source-code-only levels while compact exception events close an 18--23pp gap to ${\\geq}$99.33\\% (\\S\\ref{sec:cross_model}).\n\n\\item \\textbf{Semantic vs.\\ format-marker decomposition}: marker removal collapses a format-exploiting regex by 71pp while SFT drops only 2pp; cross-dataset transfer (99.4--100\\%) shows the learned signal generalizes beyond format markers (\\S\\ref{sec:nomarker}).\n\n\\item \\textbf{A two-tier signal hierarchy}: exception/assertion signals (${\\geq}$98.53\\%) dominate loop compression (77--86\\%) by 12+pp with non-overlapping CIs; a sharp transition at ${\\sim}$512 tail tokens yields a practical fallback (\\S\\ref{sec:ablation}, \\S\\ref{sec:trace_length}).\n\n\\item \\textbf{Mechanistic decomposition}: controlled gradient masking attributes ${\\leq}$4\\% of the degradation to gradient dilution, assigning the majority to content quality at inference, though forward-pass attention is an unquantified residual (\\S\\ref{sec:density}).\n\\end{enumerate}\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{fig1_trace_overview}\n\\vspace{-8pt}\n\\caption{Overview of the verdict prediction pipeline. Source code and a test input are executed to produce a full raw trace. Four conditions vary the trace information: \\texttt{no\\_trace} (75.13\\%), \\texttt{full\\_trace} (81.44\\%), VOTA (99.05\\%), and \\texttt{exception\\_only} (99.83\\%). Accuracies for Qwen-2.5-7B ($N{=}1{,}190$); multi-seed means where available (Table~\\ref{tab:ablation}). Appendix~\\ref{sec:vota_examples} provides input/output examples.}\n\\label{fig:trace_overview}\n\\end{figure*}\n",
      "numLines": 42,
      "startLine": 1,
      "totalLines": 42
    }
  },
  "sourceToolAssistantUUID": "1c1213a5-f67f-4466-81bd-c86a10b5de96",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/.claude/sessions/paper_audit_content_b575bb0e",
  "sessionId": "1db729b7-6c37-474e-9cbb-179c13a8aeb8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-24T16:16:13.909Z_

<details open><summary>🔧 Tool call — Read · `toolu_01ANLF1sWJSd7ZbSRX9YTNLQ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ed362203-00e0-4e07-814e-1ef07f682150",
  "isSidechain": false,
  "requestId": "req_011CbMh9tV4aN8QV3riH9wUf",
  "type": "assistant",
  "uuid": "bcfa1878-b679-42bb-9323-276e048204b8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/.claude/sessions/paper_audit_content_b575bb0e",
  "sessionId": "1db729b7-6c37-474e-9cbb-179c13a8aeb8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012VsV8ncx6FrdGuWaCHMfaG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11894,
      "cache_read_input_tokens": 38247,
      "output_tokens": 703,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11894,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 703,
          "cache_read_input_tokens": 38247,
          "cache_creation_input_tokens": 11894,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11894
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

_source line 26 · 2026-05-24T16:16:13.914Z_

<details><summary>↩ Tool result · `toolu_01ANLF1sWJSd7ZbSRX9YTNLQ`</summary>

```text
1	\section{Related Work}
2	
3	\paragraph{Execution Traces for Code LLMs.}
4	TracePile \citep{chen2025tracepile} scaled trace-augmented training to 2.6M samples; \citet{wang2025dcsh} found trace utility task- and format-dependent, which we extend by showing that complete traces degrade SFT performance while compact exception events suffice.
5	NExT \citep{ni2024next} and ET-CoT \citep{eguchi2025etcot} used trace chain-of-thought for repair and execution reasoning; \citet{ferrando2025execute} found compact traces comparable to full traces, supporting our density finding.
6	CRUXEval \citep{gu2024cruxeval,xu2025cruxevalx} and LiveCodeBench \citep{jain2024livecodebench} established execution reasoning benchmarks, but none decompose which trace components contribute to classification accuracy.
7	
8	\paragraph{Verdict Prediction and Fault Localization.}
9	TRACED \citep{ding2024traced} showed execution-aware pretraining improves vulnerability detection; CC2Vec \citep{hoang2020cc2vec} and APPT \citep{appt2024} developed representation learning of code changes; verdict prediction is an instance of the test oracle problem \citep{barr2015oracle}.
10	SBFL \citep{abreu2007accuracy,wong2014dstar} and LLM-based FL \citep{kang2024autofl,qin2024agentfl} share our insight that anomalous execution events carry the strongest diagnostic signal.
11	TraceCoder \citep{huang2026tracecoder} and InspectCoder \citep{wang2025inspectcoder} use selective trace extraction, yet which trace components carry verdict signals most efficiently remains unstudied.
12	
13	\paragraph{Calibration and Data Selection.}
14	Neural network calibration \citep{guo2017calibration}, extended to LLMs \citep{kadavath2022language,geng2024calibration}, studies confidence-correctness alignment; our ECE ${<}$ 0.007 suggests compact inputs improve calibration.
15	The Information Bottleneck \citep{tishby2000information}, feature selection theory \citep{guyon2003introduction}, and LIMA \citep{zhou2023lima} predict that compressing task-irrelevant information improves learning; data pruning \citep{paul2021deep,sorscher2022beyond} confirms this empirically, consistent with our finding that compact exceptions converge rapidly while verbose traces oscillate.
16	
17	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bcfa1878-b679-42bb-9323-276e048204b8",
  "isSidechain": false,
  "promptId": "96f110f9-4fbd-4295-8cdb-ef5a8ad15d7a",
  "type": "user",
  "uuid": "dd48ef60-112c-482b-a380-b790d27a087d",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/related_work.tex",
      "content": "\\section{Related Work}\n\n\\paragraph{Execution Traces for Code LLMs.}\nTracePile \\citep{chen2025tracepile} scaled trace-augmented training to 2.6M samples; \\citet{wang2025dcsh} found trace utility task- and format-dependent, which we extend by showing that complete traces degrade SFT performance while compact exception events suffice.\nNExT \\citep{ni2024next} and ET-CoT \\citep{eguchi2025etcot} used trace chain-of-thought for repair and execution reasoning; \\citet{ferrando2025execute} found compact traces comparable to full traces, supporting our density finding.\nCRUXEval \\citep{gu2024cruxeval,xu2025cruxevalx} and LiveCodeBench \\citep{jain2024livecodebench} established execution reasoning benchmarks, but none decompose which trace components contribute to classification accuracy.\n\n\\paragraph{Verdict Prediction and Fault Localization.}\nTRACED \\citep{ding2024traced} showed execution-aware pretraining improves vulnerability detection; CC2Vec \\citep{hoang2020cc2vec} and APPT \\citep{appt2024} developed representation learning of code changes; verdict prediction is an instance of the test oracle problem \\citep{barr2015oracle}.\nSBFL \\citep{abreu2007accuracy,wong2014dstar} and LLM-based FL \\citep{kang2024autofl,qin2024agentfl} share our insight that anomalous execution events carry the strongest diagnostic signal.\nTraceCoder \\citep{huang2026tracecoder} and InspectCoder \\citep{wang2025inspectcoder} use selective trace extraction, yet which trace components carry verdict signals most efficiently remains unstudied.\n\n\\paragraph{Calibration and Data Selection.}\nNeural network calibration \\citep{guo2017calibration}, extended to LLMs \\citep{kadavath2022language,geng2024calibration}, studies confidence-correctness alignment; our ECE ${<}$ 0.007 suggests compact inputs improve calibration.\nThe Information Bottleneck \\citep{tishby2000information}, feature selection theory \\citep{guyon2003introduction}, and LIMA \\citep{zhou2023lima} predict that compressing task-irrelevant information improves learning; data pruning \\citep{paul2021deep,sorscher2022beyond} confirms this empirically, consistent with our finding that compact exceptions converge rapidly while verbose traces oscillate.\n\n",
      "numLines": 17,
      "startLine": 1,
      "totalLines": 17
    }
  },
  "sourceToolAssistantUUID": "bcfa1878-b679-42bb-9323-276e048204b8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/.claude/sessions/paper_audit_content_b575bb0e",
  "sessionId": "1db729b7-6c37-474e-9cbb-179c13a8aeb8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-24T16:16:14.369Z_

<details open><summary>🔧 Tool call — Read · `toolu_01DgUTgaHpHtVMNfmp3ZxzWU`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dd48ef60-112c-482b-a380-b790d27a087d",
  "isSidechain": false,
  "requestId": "req_011CbMh9tV4aN8QV3riH9wUf",
  "type": "assistant",
  "uuid": "ebaf84a0-418f-40bc-be5c-32faa8024b92",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/.claude/sessions/paper_audit_content_b575bb0e",
  "sessionId": "1db729b7-6c37-474e-9cbb-179c13a8aeb8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012VsV8ncx6FrdGuWaCHMfaG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11894,
      "cache_read_input_tokens": 38247,
      "output_tokens": 703,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11894,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 703,
          "cache_read_input_tokens": 38247,
          "cache_creation_input_tokens": 11894,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11894
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

_source line 28 · 2026-05-24T16:16:14.373Z_

<details><summary>↩ Tool result · `toolu_01DgUTgaHpHtVMNfmp3ZxzWU`</summary>

```text
1	\section{Method}
2	
3	\subsection{Task Definition and Diagnostic Signal Metrics}
4	
5	We study \emph{verdict prediction}: given a Python function, a test input, and an optional execution trace, predict whether the test passes or fails.
6	The model produces a single token (\texttt{pass} or \texttt{fail}), making this a binary classification task.
7	Unlike code generation \citep{chen2025tracepile} or output prediction \citep{gu2024cruxeval}, verdict prediction isolates the model's ability to detect faults from its ability to simulate execution, providing cleaner ablation contrasts than generation tasks.
8	
9	To quantify signal quality without circular reference to model accuracy, we define the \emph{diagnostic token ratio} $d = n_{\text{diag}} / n_{\text{total}}$, where $n_{\text{diag}}$ counts tokens matching exception or assertion patterns.
10	This model-free metric correlates with accuracy at Pearson $r{=}0.949$ ($p{=}0.014$, $N{=}5$, df=3; treat as descriptive), but captures only the \emph{explicit} diagnostic pathway; tail-truncated conditions achieve 93--98\% with $d {\approx} 0$, indicating a second, implicit signal channel operating through terminal execution state (\S\ref{sec:density}).
11	
12	\subsection{Dataset}
13	\label{sec:dataset}
14	
15	We sampled 10 candidate solutions per problem from Qwen-2.5-Coder-7B-Instruct (temperature 0.8, top\_p 0.95) for 591 problems from HumanEval \citep{chen2021evaluating} (164) and MBPP-sanitized \citep{austin2021program} (427), executed each against canonical tests with \texttt{sys.settrace} to obtain line-level traces and pass/fail verdicts, yielding 5,910 pairs (67\% pass, 33\% fail).
16	The dataset is split 80/20 by problem ID into 4,720 training and 1,190 test samples (majority baseline: 71.51\%).
17	The \texttt{exception\_only} format collapses passing solutions into identical rows (39.45\% train, 48.99\% test duplicates); these duplicates arise from multiple candidate solutions per problem, with the train--test split enforced at the problem level (472 train / 119 test problems, zero crossover; Appendix~\ref{sec:dedup_stats}).
18	
19	\subsection{Trace Representations}
20	
21	We define seven conditions that vary the trace information available (Figure~\ref{fig:trace_overview}):
22	\begin{itemize}
23	\item \texttt{no\_trace}: Source code and test input only.
24	\item \texttt{full\_trace}: Complete line-by-line trace with variable states.
25	\item \texttt{VOTA} (Verdict-Optimized Trace Abstraction): Exception events + assertion-point comparisons + loop compression (Appendix~\ref{sec:vota_algorithm}).
26	\item \texttt{exception\_only}: Only exception/error events.
27	\item \texttt{ae\_only}: Only assertion-point actual/expected pairs.
28	\item \texttt{loop\_only}: Only loop compression summaries.
29	\item \texttt{VOTA\_no\_ae}: VOTA without assertion-point information.
30	\end{itemize}
31	
32	
33	\subsection{Models and Training}
34	
35	We evaluate four models spanning three architecture families: \textbf{Qwen-2.5-Coder-7B/1.5B-Instruct} \citep{qwen2024coder}, \textbf{CodeLlama-13B-Instruct} \citep{roziere2024code}, and \textbf{DeepSeek-Coder-6.7B-Instruct} \citep{deepseek2024coder}, covering a 1.5B--13B parameter range (8.7$\times$).
36	All conditions use LoRA \citep{hu2022lora} (rank=16, $\alpha$=32, dropout=0.05) on all linear layers, 3 epochs, effective batch size 32, LR $2 \times 10^{-4}$ with linear warmup/decay, max sequence length 2{,}048 tokens.
37	Sequences exceeding this limit are truncated while preserving the verdict label.
38	The primary seed is 42; seeds 123 and 456 test \texttt{exception\_only} robustness (Appendix~\ref{sec:training_details}).
39	
40	\subsection{Loss Ablation}
41	
42	To probe the contribution of gradient dilution, we introduce \texttt{full\_trace\_label\_only}: identical full-trace input but loss computed only on the verdict token (trace positions masked).
43	TRL's SFTTrainer computes mean cross-entropy over label tokens, so label-only loss does not amplify the effective learning rate.
44	However, this ablation simultaneously changes three variables: (1)~which tokens receive gradient updates, (2)~the implicit regularization from predicting trace tokens, and (3)~the training signal distribution.
45	The resulting improvement over standard \texttt{full\_trace} provides a confounded upper bound on gradient dilution's contribution.
46	A cleaner test (masking 99.8\% of gradient updates during \texttt{exception\_only} training) matches the diagnostic token ratio of full traces while preserving compact input, isolating gradient dilution from content quality (\S\ref{sec:density}).
47	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ebaf84a0-418f-40bc-be5c-32faa8024b92",
  "isSidechain": false,
  "promptId": "96f110f9-4fbd-4295-8cdb-ef5a8ad15d7a",
  "type": "user",
  "uuid": "7fb707b6-9f5f-4174-ae15-f42796eca04b",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/method.tex",
      "content": "\\section{Method}\n\n\\subsection{Task Definition and Diagnostic Signal Metrics}\n\nWe study \\emph{verdict prediction}: given a Python function, a test input, and an optional execution trace, predict whether the test passes or fails.\nThe model produces a single token (\\texttt{pass} or \\texttt{fail}), making this a binary classification task.\nUnlike code generation \\citep{chen2025tracepile} or output prediction \\citep{gu2024cruxeval}, verdict prediction isolates the model's ability to detect faults from its ability to simulate execution, providing cleaner ablation contrasts than generation tasks.\n\nTo quantify signal quality without circular reference to model accuracy, we define the \\emph{diagnostic token ratio} $d = n_{\\text{diag}} / n_{\\text{total}}$, where $n_{\\text{diag}}$ counts tokens matching exception or assertion patterns.\nThis model-free metric correlates with accuracy at Pearson $r{=}0.949$ ($p{=}0.014$, $N{=}5$, df=3; treat as descriptive), but captures only the \\emph{explicit} diagnostic pathway; tail-truncated conditions achieve 93--98\\% with $d {\\approx} 0$, indicating a second, implicit signal channel operating through terminal execution state (\\S\\ref{sec:density}).\n\n\\subsection{Dataset}\n\\label{sec:dataset}\n\nWe sampled 10 candidate solutions per problem from Qwen-2.5-Coder-7B-Instruct (temperature 0.8, top\\_p 0.95) for 591 problems from HumanEval \\citep{chen2021evaluating} (164) and MBPP-sanitized \\citep{austin2021program} (427), executed each against canonical tests with \\texttt{sys.settrace} to obtain line-level traces and pass/fail verdicts, yielding 5,910 pairs (67\\% pass, 33\\% fail).\nThe dataset is split 80/20 by problem ID into 4,720 training and 1,190 test samples (majority baseline: 71.51\\%).\nThe \\texttt{exception\\_only} format collapses passing solutions into identical rows (39.45\\% train, 48.99\\% test duplicates); these duplicates arise from multiple candidate solutions per problem, with the train--test split enforced at the problem level (472 train / 119 test problems, zero crossover; Appendix~\\ref{sec:dedup_stats}).\n\n\\subsection{Trace Representations}\n\nWe define seven conditions that vary the trace information available (Figure~\\ref{fig:trace_overview}):\n\\begin{itemize}\n\\item \\texttt{no\\_trace}: Source code and test input only.\n\\item \\texttt{full\\_trace}: Complete line-by-line trace with variable states.\n\\item \\texttt{VOTA} (Verdict-Optimized Trace Abstraction): Exception events + assertion-point comparisons + loop compression (Appendix~\\ref{sec:vota_algorithm}).\n\\item \\texttt{exception\\_only}: Only exception/error events.\n\\item \\texttt{ae\\_only}: Only assertion-point actual/expected pairs.\n\\item \\texttt{loop\\_only}: Only loop compression summaries.\n\\item \\texttt{VOTA\\_no\\_ae}: VOTA without assertion-point information.\n\\end{itemize}\n\n\n\\subsection{Models and Training}\n\nWe evaluate four models spanning three architecture families: \\textbf{Qwen-2.5-Coder-7B/1.5B-Instruct} \\citep{qwen2024coder}, \\textbf{CodeLlama-13B-Instruct} \\citep{roziere2024code}, and \\textbf{DeepSeek-Coder-6.7B-Instruct} \\citep{deepseek2024coder}, covering a 1.5B--13B parameter range (8.7$\\times$).\nAll conditions use LoRA \\citep{hu2022lora} (rank=16, $\\alpha$=32, dropout=0.05) on all linear layers, 3 epochs, effective batch size 32, LR $2 \\times 10^{-4}$ with linear warmup/decay, max sequence length 2{,}048 tokens.\nSequences exceeding this limit are truncated while preserving the verdict label.\nThe primary seed is 42; seeds 123 and 456 test \\texttt{exception\\_only} robustness (Appendix~\\ref{sec:training_details}).\n\n\\subsection{Loss Ablation}\n\nTo probe the contribution of gradient dilution, we introduce \\texttt{full\\_trace\\_label\\_only}: identical full-trace input but loss computed only on the verdict token (trace positions masked).\nTRL's SFTTrainer computes mean cross-entropy over label tokens, so label-only loss does not amplify the effective learning rate.\nHowever, this ablation simultaneously changes three variables: (1)~which tokens receive gradient updates, (2)~the implicit regularization from predicting trace tokens, and (3)~the training signal distribution.\nThe resulting improvement over standard \\texttt{full\\_trace} provides a confounded upper bound on gradient dilution's contribution.\nA cleaner test (masking 99.8\\% of gradient updates during \\texttt{exception\\_only} training) matches the diagnostic token ratio of full traces while preserving compact input, isolating gradient dilution from content quality (\\S\\ref{sec:density}).\n",
      "numLines": 47,
      "startLine": 1,
      "totalLines": 47
    }
  },
  "sourceToolAssistantUUID": "ebaf84a0-418f-40bc-be5c-32faa8024b92",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/.claude/sessions/paper_audit_content_b575bb0e",
  "sessionId": "1db729b7-6c37-474e-9cbb-179c13a8aeb8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-24T16:16:14.996Z_

<details open><summary>🔧 Tool call — Read · `toolu_01LPjvRK79NJrCZuVeyCSkHR`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7fb707b6-9f5f-4174-ae15-f42796eca04b",
  "isSidechain": false,
  "requestId": "req_011CbMh9tV4aN8QV3riH9wUf",
  "type": "assistant",
  "uuid": "7a6d2a67-698e-4f97-af4f-7fe3845fa1b6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/.claude/sessions/paper_audit_content_b575bb0e",
  "sessionId": "1db729b7-6c37-474e-9cbb-179c13a8aeb8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012VsV8ncx6FrdGuWaCHMfaG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11894,
      "cache_read_input_tokens": 38247,
      "output_tokens": 703,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11894,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 703,
          "cache_read_input_tokens": 38247,
          "cache_creation_input_tokens": 11894,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11894
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

_source line 30 · 2026-05-24T16:16:15.011Z_

<details><summary>↩ Tool result · `toolu_01LPjvRK79NJrCZuVeyCSkHR`</summary>

```text
1	\section{Experiments}
2	
3	We evaluate across two research questions:
4	(1)~Why do complete traces degrade SFT verdict accuracy despite containing all diagnostic information?
5	(2)~Which trace components carry the verdict signal, and how does their density affect learning?
6	All experiments use $N{=}1{,}190$ test samples; accuracy is reported with Wilson 95\% CIs.\footnote{Problem-level partition (472 train / 119 test, zero crossover; \S\ref{sec:dataset}). \texttt{exception\_only} duplicates (48.99\% test; Appendix~\ref{sec:dedup_stats}) arise from within-problem variants; deduplication yields negligible ($<$0.1pp) delta.}
7	Pairwise comparisons use paired bootstrap resampling ($B{=}10{,}000$, seed=42); all differences are significant at $p{<}.0001$ unless noted.
8	Under problem-level clustered bootstrap ($n_\text{eff}{=}119$), all cross-tier gaps remain significant ($p{<}.001$); 3 of 80 within-tier pairwise comparisons lose significance after Holm--Bonferroni correction.
9	
10	\subsection{Cross-Model Comparison}
11	\label{sec:cross_model}
12	
13	Table~\ref{tab:cross_model} compares four models spanning an 8.7$\times$ parameter range (1.5B--13B) and three architecture families under key conditions; single-seed entries are marked with $^\dag$.
14	Regex B5 (99.33\%) exploits the \texttt{[No exception data in trace]} format marker, providing a non-learned baseline; its collapse to 28.49\% under marker removal (\S\ref{sec:nomarker}) shows the SFT advantage is not format-driven.
15	
16	\begin{table}[t]
17	\centering
18	\caption{Cross-model verdict accuracy (\%, $N{=}1{,}190$) across four models (1.5B--13B) and three architecture families. Multi-seed entries report mean$\pm$std over 2--3 seeds; $^\dag$ = single seed (seed 42). Bold: best per model. Full per-seed breakdowns in Appendix~\ref{sec:full_results}; per-class metrics in Appendix~\ref{sec:per_class}.}
19	\label{tab:cross_model}
20	\small
21	\resizebox{\columnwidth}{!}{%
22	\begin{tabular}{lcccc}
23	\toprule
24	\textbf{Condition} & \textbf{Qwen-7B} & \textbf{Qwen-1.5B} & \textbf{CL-13B} & \textbf{DS-6.7B} \\
25	\midrule
26	exception\_only & \textbf{99.83}{\scriptsize$\pm$0.00} & \textbf{99.83}{\scriptsize$\pm$0.00} & \textbf{99.89}{\scriptsize$\pm$0.10} & \textbf{99.39}{\scriptsize$\pm$0.10} \\
27	ae\_only & 99.64{\scriptsize$\pm$0.49} & 98.83{\scriptsize$\pm$0.36} & 99.08{\scriptsize$\pm$0.00} & 98.53{\scriptsize$\pm$0.30} \\
28	VOTA & 99.05{\scriptsize$\pm$0.38} & 99.54{\scriptsize$\pm$0.06} & 98.74{\scriptsize$\pm$0.24} & 99.25$^\ddag$ \\
29	loop\_only & 86.05{\scriptsize$\pm$0.52} & 79.54{\scriptsize$\pm$1.42} & 77.40{\scriptsize$\pm$1.54} & 80.31{\scriptsize$\pm$1.65} \\
30	full\_trace & 81.44{\scriptsize$\pm$1.11} & 77.06$^\dag$ & 79.9$^\S$ & 79.16$^\dag$ \\
31	no\_trace & 75.13$^\dag$ & 72.35{\scriptsize$\pm$4.48} & 76.47$^\dag$ & 73.36$^\dag$ \\
32	\midrule
33	Regex B5 (marker) & \multicolumn{4}{c}{99.33} \\
34	Majority baseline & \multicolumn{4}{c}{71.51} \\
35	\bottomrule
36	\end{tabular}%
37	}
38	\vspace{2pt}
39	\par\raggedright\footnotesize
40	$^\ddag$DeepSeek VOTA seed 42 (84.45\%) is a tokenizer-driven truncation failure (Appendix~\ref{sec:tokenizer_analysis}), reported as 2-seed mean.
41	$^\S$CodeLlama \texttt{full\_trace} not available; head-2048 proxy reported.
42	Per-seed breakdowns for all conditions in Appendix~\ref{sec:full_results}.
43	\end{table}
44	
45	\paragraph{Exception dominance across families.}
46	Under \texttt{exception\_only}, all four models achieve ${\geq}$99.33\% across all available seeds (Table~\ref{tab:cross_model}), spanning only 0.50pp across architectures (the tightest of any condition).
47	CodeLlama-13B seed 123 achieves 100\%, indicating the 2 persistent errors (\texttt{GeneratorExit}; Appendix~\ref{sec:irreducible}) are convergence artifacts; 99.83\% is a floor, not a ceiling.
48	
49	\paragraph{Scale effects concentrate in Tier~2.}
50	Tier~1 signals are scale-invariant across 1.5B--13B (8.7$\times$): both \texttt{exception\_only} and \texttt{ae\_only} span ${\leq}$1.2pp.
51	\texttt{loop\_only} spans 8.65pp, with CodeLlama-13B below Qwen-1.5B, suggesting architecture matters more than parameter count for lower-density signals.
52	In contrast, \texttt{no\_trace} scales with capacity (Figure~\ref{fig:cross_scale}) and shows the highest seed variance ($\sigma{=}$4.48pp).
53	
54	\begin{figure}[t]
55	\centering
56	\includegraphics[width=\columnwidth]{fig3_cross_model_gap}
57	\caption{Verdict accuracy vs.\ model scale. \texttt{exception\_only} maintains ${\geq}$99.33\% regardless of scale, while \texttt{no\_trace} shows monotonic sensitivity (+4.12pp). \texttt{nomarker} (markers removed) shows no scale degradation.}
58	\label{fig:cross_scale}
59	\end{figure}
60	
61	\paragraph{VOTA cross-family variation.}
62	Excluding outlier seeds, VOTA achieves ${\geq}$98.57\% across all four models (0.80pp range).
63	DeepSeek seed 42 (84.45\%) is a tokenizer-driven truncation failure (91.7\% of samples exceed 2{,}048 tokens after tokenization; Appendix~\ref{sec:tokenizer_analysis}), demonstrating that VOTA's longer sequences are sensitive to tokenizer efficiency: 1/4 models suffers catastrophic truncation under standard training length. \texttt{exception\_only}'s compact inputs (median 150 tokens) sidestep this vulnerability entirely.
64	
65	\subsection{Component Ablation}
66	\label{sec:ablation}
67	
68	Multi-seed \texttt{ae\_only} ablations use Qwen-7B; \texttt{loop\_only} is evaluated across three models to test Tier~2 generalization (Table~\ref{tab:cross_model}).
69	Table~\ref{tab:ablation} decomposes VOTA on Qwen-2.5-7B and reveals a two-tier hierarchy validated across all four models and three architecture families (Table~\ref{tab:cross_model}): Tier~1 (${\geq}$98.53\%) and Tier~2 (77--86\%) are separated by 12+pp with non-overlapping CIs.
70	
71	\begin{table}[t]
72	\centering
73	\caption{Component ablation on Qwen-2.5-7B ($N{=}1{,}190$). Tier~1 signals achieve near-perfect accuracy; combining them (VOTA) slightly dilutes performance. Entries marked $^\dag$/$^\S$/$^\ddag$ are 3-seed mean$\pm$std; unmarked entries are single seed (seed 42). Per-seed breakdowns in Appendix~\ref{sec:full_results}. Seed $\sigma$ negatively correlates with density (0.00 for exception to 0.52 for loop).}
74	\label{tab:ablation}
75	\small
76	\resizebox{\columnwidth}{!}{%
77	\begin{tabular}{llccc}
78	\toprule
79	\textbf{Condition} & \textbf{Components} & \textbf{Acc (\%)} & \textbf{95\% CI} & \textbf{Tier} \\
80	\midrule
81	ae\_only & assertion-point & 99.64$^\dag$ & [99.26, 99.87] & 1 \\
82	exception\_only & exception events & \textbf{99.83} & [99.58, 100.00] & 1 \\
83	VOTA & exc+ae+loop & 99.05$^\S$ & [98.49, 99.50] & --- \\
84	VOTA\_no\_ae & exc+loop & 99.41 & [98.90, 99.80] & --- \\
85	loop\_only & loop compression & 86.05$^\ddag$ & [83.97, 87.96] & 2 \\
86	full\_trace & complete trace & 81.44{\scriptsize$\pm$1.11} & --- & --- \\
87	no\_trace & none & 75.13 & [72.77, 77.48] & --- \\
88	\midrule
89	Regex (best) & exc.\ type regex & 93.61 & --- & --- \\
90	3-shot (Qwen-7B) & in-context learning & 90.84 & --- & --- \\
91	Zero-shot (4 models) & prompting & 51.0--93.5 & --- & --- \\
92	\bottomrule
93	\end{tabular}%
94	}
95	\end{table}
96	
97	Tier~1 signals are individually sufficient: \texttt{exception\_only} (99.83\%$\pm$0.00) exceeds VOTA (99.05\%$\pm$0.38) by +0.78pp (2/3 seeds $p{<}.05$, all directionally consistent), implying that combining signals introduces noise.
98	Removing assertion points has no effect (\texttt{VOTA\_no\_ae} = 99.41\%, single seed), indicating exception dominance.
99	Individual exception subcomponents (type, stacktrace, message) each independently achieve ${\geq}$99.50\%, indicating that the binary presence of an exception event, rather than any specific subcomponent, drives Tier~1 performance (Appendix~\ref{sec:exc_subcomponent}).
100	The Tier~1/2 boundary is unambiguous: the lowest Tier~1 condition (\texttt{ae\_only} on DeepSeek, 98.53\%$\pm$0.30, 2 seeds) exceeds the highest Tier~2 (\texttt{loop\_only} on Qwen-7B, 86.05\%, CI [83.97, 87.96]) by 12.48\,pp with non-overlapping CIs (gap statistic supports $k{=}2$ clusters, silhouette ${\geq}$0.74).
101	Tier~2 \texttt{loop\_only} lifts over \texttt{no\_trace} are model-dependent: Qwen +10.92pp (7B) and +7.19pp (1.5B); DeepSeek +6.95pp; CodeLlama +0.93pp (n.s.).
102	\paragraph{Rule-based baseline comparison.}
103	The strongest non-trivial regex heuristic (B4: exception class name matching; Table~\ref{tab:regex}) achieves 93.61\% accuracy (F1=0.876), trailing SFT \texttt{exception\_only} (99.83\%, F1=0.997) by 6.22pp (McNemar $p{<}.001$).
104	The gap concentrates on caught-exception boundary cases: regex flags all exception events as failures, while SFT learns to distinguish caught exceptions (benign, inside \texttt{try/except}) from uncaught faults, correctly resolving 6/8 boundary samples (Appendix~\ref{sec:regex_baselines}).
105	Across all formats, SFT outperforms the best applicable regex by +3.62--23.86pp (Appendix~\ref{sec:regex_baselines}).
106	
107	\paragraph{Zero-shot and few-shot LLM baselines.}
108	Zero-shot prompting spans 51.0--93.5\% across four models (42.44pp range); three-shot ICL on Qwen-7B (90.84\%) improves only 1.76pp.
109	SFT compresses this range to 0.50pp (99.39--99.89\%), closing a 6--49pp gap with 4,720 samples (Appendix~\ref{sec:zeroshot_cross_model}).
110	\paragraph{Frontier model crossover.}
111	Two frontier models illustrate that SFT's advantage depends on input density: under \texttt{no\_trace}, GPT-4o (84.45\%) and GPT-4.1 (77.31\%) outperform SFT Qwen-7B (75.13\%), but under \texttt{exception\_only} the ranking reverses (SFT 99.83\% vs.\ GPT-4o 87.98\%).
112	Compact diagnostic input unlocks SFT's full advantage over general reasoning capacity.
113	
114	\subsection{Format Marker Ablation}
115	\label{sec:nomarker}
116	
117	The \texttt{exception\_only} format includes a \texttt{[No exception data in trace]} marker in all pass-class samples (regex baseline B5 exploits this for 99.33\% accuracy; Appendix~\ref{sec:regex_baselines}).
118	To quantify the marker's contribution, we retrain with all format markers removed (\texttt{nomarker} condition).
119	
120	Qwen-7B 3-seed mean: 97.65\% $\pm$ 0.96 (seeds 42/123/456: 96.55/98.32/98.07\%), a drop of 2.18pp from \texttt{exception\_only} (99.83\%).
121	Qwen-1.5B: 97.82\%, drop of 2.01pp.
122	The marker contribution (${\sim}$2pp) accounts for only ${\sim}$9\% of the total exception lift over \texttt{no\_trace} (24.70pp on 7B).
123	Regex baselines illustrate this decomposition: B5 (\texttt{[No exception data]}$\to$pass, 99.33\% with markers) collapses to 28.49\% without markers, showing it is entirely format-dependent.
124	The strongest semantic regex B4 (exception class matching, 93.61\%) is marker-invariant; SFT \texttt{nomarker} (97.65\%) exceeds it by 4.04pp, isolating the learned semantic contribution beyond pattern matching.
125	
126	\paragraph{Cross-dataset transfer.}
127	Bidirectional evaluation demonstrates generalization: HumanEval${\to}$MBPP \texttt{exception\_only} achieves 99.41\% ($N{=}4{,}270$) and MBPP${\to}$HumanEval achieves 100.0\% ($N{=}1{,}640$), while \texttt{no\_trace} drops to near-majority baseline in both directions (70.56\% vs.\ 69.02\% majority; 67.99\% vs.\ 61.65\%).
128	The near-zero transfer loss for exception signals, across independently authored problem sets with no problem overlap, shows SFT learns language-level diagnostic patterns, not dataset-specific artifacts.
129	Under marker removal, cross-dataset accuracy drops to 95.5\% ($-$3.9pp), indicating that the majority of cross-dataset transfer relies on learned diagnostic patterns rather than format markers.
130	
131	\subsection{Decomposing the Full-Trace Degradation}
132	\label{sec:density}
133	
134	The 18.07pp gap between \texttt{exception\_only} (99.83\%) and \texttt{full\_trace} (81.76\%) could reflect gradient dilution (diagnostic tokens are ${\sim}$1/500 of full traces, diluting gradient signal during training) or content quality (verbose input buries diagnostic signals at inference).
135	
136	\paragraph{Controlled gradient masking.}
137	To isolate gradient dilution, we mask 99.8\% of gradient updates during \texttt{exception\_only} training, matching the diagnostic token ratio of full traces while preserving compact input.
138	This yields 99.22\% (mean $-$0.61pp from \texttt{exception\_only}, 3 seeds), limiting gradient dilution to ${\leq}$4\% of the 18.07pp gap (Table~\ref{tab:density}).
139	The gradient masking bound attributes the remaining ${\geq}$96\% to content quality (diagnostic signal density at inference), though forward-pass attention during masked training is an unquantified residual.
140	Note that masking affects only the backward pass; the model still attends to all input tokens during the forward pass, so this bounds gradient dilution's contribution but does not rule out attention-based information flow as a residual confound.
141	
142	\begin{table}[t]
143	\centering
144	\caption{Decomposition of the full-trace degradation (Qwen-7B). Gradient masking attributes ${\leq}$4\% to gradient dilution; the bound assigns the remainder to content quality, though forward-pass attention is a residual confound (\S\ref{sec:density}). Label-only loss provides a confounded but directionally consistent complementary estimate.}
145	\label{tab:density}
146	\small
147	\begin{tabular}{lcc}
148	\toprule
149	\textbf{Condition} & \textbf{Acc (\%)} & \textbf{$\Delta$} \\
150	\midrule
151	exception\_only & 99.83{\scriptsize$\pm$0.00} & --- \\
152	\quad + grad mask (99.8\%) & 99.22{\scriptsize$\pm$0.20}$^\S$ & $-$0.61pp \\
153	full\_trace & 81.76$^\ddag$ & $-$18.07pp \\
154	\midrule
155	\multicolumn{3}{l}{\textit{Complementary (confounded):}} \\
156	full\_trace + label-only loss & 85.94{\scriptsize$\pm$1.12} & +4.50pp$^\dag$ \\
157	\bottomrule
158	\end{tabular}
159	\vspace{2pt}
160	\par\raggedright\footnotesize
161	$^\S$Mean $\pm$ std over 3 seeds (42, 123, 456).
162	$^\ddag$Matched-seed baseline; 3-seed mean 81.44\%$\pm$1.11 (Table~\ref{tab:cross_model}).
163	$^\dag$vs.\ \texttt{full\_trace} (81.44\%$\pm$1.11); not significant under clustered bootstrap (95\% CI [$-$0.6, +9.8]pp, $n_\text{eff}{=}119$).
164	\end{table}
165	
166	\paragraph{Complementary evidence.}
167	Label-only loss on full traces (+4.50pp, 3 seeds) yields a confounded upper bound of ${\leq}$26\% gradient contribution, consistent with the masking estimate (${\leq}$4\%) but not significant under clustered bootstrap (95\% CI [$-$0.6, +9.8]pp).
168	Qwen-1.5B shows a similar label-only pattern (17\%/83\%, 3 seeds); CodeLlama and DeepSeek exhibit label-only collapse to majority baseline (28.5\%), limiting this complementary analysis to the Qwen family.
169	The architecture dependence suggests label-only training is sensitive to model capacity or optimization landscape; the gradient masking ablation provides a more robust, architecture-independent decomposition.
170	Cross-architecture validation on two additional families is directionally consistent (single seed each): DeepSeek-Coder-6.7B achieves 99.33\% and CodeLlama-13B achieves 100\% under 99.8\% masking, both well above the full-trace range (77--82\%, Table~\ref{tab:cross_model}), supporting content quality as the dominant factor across architectures.
171	Error analysis supports the content quality interpretation: all 217 \texttt{full\_trace} errors occur where tokenizer truncation removes diagnostic markers, manifesting through mechanical truncation rather than semantic confusion.
172	
173	\subsection{Complementary Analyses}
174	\label{sec:additional}
175	
176	\paragraph{Trace length ablation.}
177	\label{sec:trace_length}
178	Varying the head-truncated trace token budget (256--no limit) on Qwen-7B yields accuracy in a narrow 77.2\%--81.8\% band with a non-monotonic pattern: 1024-token prefixes (77.23\%) underperform 512-token prefixes (80.42\%, $p{=}.002$), because mid-length prefixes retain enough irrelevant content to mislead the model while discarding diagnostic events near the trace terminus (Appendix~\ref{sec:trace_length_full}).
179	Critically, removing the token budget entirely (no truncation) yields 81.76\%, identical to head-2048, ruling out truncation as the explanation for the full-trace degradation.
180	This non-monotonicity is specific to head-truncation; under tail-truncation, accuracy increases monotonically for two of three models (Table~\ref{tab:tail_cross_model} in Appendix), with only DeepSeek showing a mild architecture-specific reversal at tail-1024$\to$tail-2048 ($-$1.5pp).
181	
182	\paragraph{Truncation direction and budget curve.}
183	Tail-truncation dramatically outperforms head-truncation: tail-2048 exceeds head-2048 by 15.5--22.6pp across three models (Appendix~\ref{sec:trace_length_full}).
184	Figure~\ref{fig:budget_curve} reveals a sharp phase transition at 384$\to$512 tail tokens: all four models simultaneously jump +13.2--22.0pp, crossing from near-baseline to 93--98\%.
185	This threshold coincides with the globals module dump boundary (${\sim}$384 tokens), beyond which structured execution markers become visible (Table~\ref{tab:tail_cross_model}).
186	Beyond 512 tokens, all 12 model$\times$seed combinations converge into [93.61\%, 98.24\%] (Table~\ref{tab:tail512_seeds}).
187	\texttt{tail\_2048} captures 95--98\% of \texttt{exception\_only}'s accuracy; the residual 2--5pp gap shows semantic extraction still outperforms positional extraction.
188	
189	\begin{figure}[t]
190	\centering
191	\includegraphics[width=\columnwidth]{budget_curve}
192	\caption{Tail-truncation budget curve across four models and three architecture families ($N{=}1{,}190$). A sharp phase transition at 384$\to$512 tokens (+13.2--22.0pp) coincides with the globals module dump boundary. Dashed lines: \texttt{exception\_only} ceiling and \texttt{no\_trace} floor.}
193	\label{fig:budget_curve}
194	\end{figure}
195	
196	\paragraph{Calibration.}
197	\label{sec:calibration}
198	Calibration mirrors the tier hierarchy: \texttt{exception\_only} achieves ECE = 0.0027 vs.\ 0.171 for \texttt{no\_trace}, a 63$\times$ gap (Figure~\ref{fig:calibration}).
199	This calibration advantage generalizes across architectures and scales: all four models (1.5B--13B) achieve ECE ${<}$ 0.007 under \texttt{exception\_only} (Table~\ref{tab:calibration_cross} in Appendix), indicating well-calibrated predictions rather than overfit confidence.
200	
201	\begin{figure}[t]
202	\centering
203	\includegraphics[width=\columnwidth]{fig2_calibration}
204	\caption{Reliability diagrams for four trace conditions on Qwen-2.5-7B ($N{=}1{,}190$, seed=42). \texttt{exception\_only} (ECE=0.0027) clusters near the diagonal, while \texttt{no\_trace} (ECE=0.171) exhibits systematic overconfidence, a 63$\times$ gap.}
205	\label{fig:calibration}
206	\end{figure}
207	
208	\paragraph{Error analysis.}
209	\texttt{exception\_only}'s 2 errors have zero overlap with all other conditions' error sets (Jaccard = 0.000; Appendix~\ref{sec:error_overlap}); per-type breakdown shows all standard exception types achieve 100\% accuracy, with only \texttt{GeneratorExit} (a benign \texttt{BaseException} subclass) causing failures (Appendix~\ref{sec:exception_type}).
210	
211	\paragraph{Length control.}
212	Padding \texttt{exception\_only} to 2{,}048 tokens, even in a semantically loaded position (after the verdict region), yields identical accuracy (99.83\%), indicating the 18--23pp gap arises from spurious patterns in verbose trace content, not sequence length.
213	
214	\paragraph{Supplementary OOD analysis.}
215	\label{sec:debugbench}
216	On DebugBench \citep{tian2024debugbench} ($N{=}426$), the condition ranking is preserved: \texttt{exception\_only} 100\%, VOTA 99.77\%, \texttt{no\_trace} 96.71\%.
217	However, narrow margins (3.29pp headroom from \texttt{no\_trace}) limit discriminative power; this supplementary analysis preserves the ranking but cannot establish effect sizes comparable to the primary dataset (Appendix~\ref{sec:debugbench_full}).
218	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7a6d2a67-698e-4f97-af4f-7fe3845fa1b6",
  "isSidechain": false,
  "promptId": "96f110f9-4fbd-4295-8cdb-ef5a8ad15d7a",
  "type": "user",
  "uuid": "579cb5cb-4230-4c40-ad38-b560fec732e1",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/experiments.tex",
      "content": "\\section{Experiments}\n\nWe evaluate across two research questions:\n(1)~Why do complete traces degrade SFT verdict accuracy despite containing all diagnostic information?\n(2)~Which trace components carry the verdict signal, and how does their density affect learning?\nAll experiments use $N{=}1{,}190$ test samples; accuracy is reported with Wilson 95\\% CIs.\\footnote{Problem-level partition (472 train / 119 test, zero crossover; \\S\\ref{sec:dataset}). \\texttt{exception\\_only} duplicates (48.99\\% test; Appendix~\\ref{sec:dedup_stats}) arise from within-problem variants; deduplication yields negligible ($<$0.1pp) delta.}\nPairwise comparisons use paired bootstrap resampling ($B{=}10{,}000$, seed=42); all differences are significant at $p{<}.0001$ unless noted.\nUnder problem-level clustered bootstrap ($n_\\text{eff}{=}119$), all cross-tier gaps remain significant ($p{<}.001$); 3 of 80 within-tier pairwise comparisons lose significance after Holm--Bonferroni correction.\n\n\\subsection{Cross-Model Comparison}\n\\label{sec:cross_model}\n\nTable~\\ref{tab:cross_model} compares four models spanning an 8.7$\\times$ parameter range (1.5B--13B) and three architecture families under key conditions; single-seed entries are marked with $^\\dag$.\nRegex B5 (99.33\\%) exploits the \\texttt{[No exception data in trace]} format marker, providing a non-learned baseline; its collapse to 28.49\\% under marker removal (\\S\\ref{sec:nomarker}) shows the SFT advantage is not format-driven.\n\n\\begin{table}[t]\n\\centering\n\\caption{Cross-model verdict accuracy (\\%, $N{=}1{,}190$) across four models (1.5B--13B) and three architecture families. Multi-seed entries report mean$\\pm$std over 2--3 seeds; $^\\dag$ = single seed (seed 42). Bold: best per model. Full per-seed breakdowns in Appendix~\\ref{sec:full_results}; per-class metrics in Appendix~\\ref{sec:per_class}.}\n\\label{tab:cross_model}\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Condition} & \\textbf{Qwen-7B} & \\textbf{Qwen-1.5B} & \\textbf{CL-13B} & \\textbf{DS-6.7B} \\\\\n\\midrule\nexception\\_only & \\textbf{99.83}{\\scriptsize$\\pm$0.00} & \\textbf{99.83}{\\scriptsize$\\pm$0.00} & \\textbf{99.89}{\\scriptsize$\\pm$0.10} & \\textbf{99.39}{\\scriptsize$\\pm$0.10} \\\\\nae\\_only & 99.64{\\scriptsize$\\pm$0.49} & 98.83{\\scriptsize$\\pm$0.36} & 99.08{\\scriptsize$\\pm$0.00} & 98.53{\\scriptsize$\\pm$0.30} \\\\\nVOTA & 99.05{\\scriptsize$\\pm$0.38} & 99.54{\\scriptsize$\\pm$0.06} & 98.74{\\scriptsize$\\pm$0.24} & 99.25$^\\ddag$ \\\\\nloop\\_only & 86.05{\\scriptsize$\\pm$0.52} & 79.54{\\scriptsize$\\pm$1.42} & 77.40{\\scriptsize$\\pm$1.54} & 80.31{\\scriptsize$\\pm$1.65} \\\\\nfull\\_trace & 81.44{\\scriptsize$\\pm$1.11} & 77.06$^\\dag$ & 79.9$^\\S$ & 79.16$^\\dag$ \\\\\nno\\_trace & 75.13$^\\dag$ & 72.35{\\scriptsize$\\pm$4.48} & 76.47$^\\dag$ & 73.36$^\\dag$ \\\\\n\\midrule\nRegex B5 (marker) & \\multicolumn{4}{c}{99.33} \\\\\nMajority baseline & \\multicolumn{4}{c}{71.51} \\\\\n\\bottomrule\n\\end{tabular}%\n}\n\\vspace{2pt}\n\\par\\raggedright\\footnotesize\n$^\\ddag$DeepSeek VOTA seed 42 (84.45\\%) is a tokenizer-driven truncation failure (Appendix~\\ref{sec:tokenizer_analysis}), reported as 2-seed mean.\n$^\\S$CodeLlama \\texttt{full\\_trace} not available; head-2048 proxy reported.\nPer-seed breakdowns for all conditions in Appendix~\\ref{sec:full_results}.\n\\end{table}\n\n\\paragraph{Exception dominance across families.}\nUnder \\texttt{exception\\_only}, all four models achieve ${\\geq}$99.33\\% across all available seeds (Table~\\ref{tab:cross_model}), spanning only 0.50pp across architectures (the tightest of any condition).\nCodeLlama-13B seed 123 achieves 100\\%, indicating the 2 persistent errors (\\texttt{GeneratorExit}; Appendix~\\ref{sec:irreducible}) are convergence artifacts; 99.83\\% is a floor, not a ceiling.\n\n\\paragraph{Scale effects concentrate in Tier~2.}\nTier~1 signals are scale-invariant across 1.5B--13B (8.7$\\times$): both \\texttt{exception\\_only} and \\texttt{ae\\_only} span ${\\leq}$1.2pp.\n\\texttt{loop\\_only} spans 8.65pp, with CodeLlama-13B below Qwen-1.5B, suggesting architecture matters more than parameter count for lower-density signals.\nIn contrast, \\texttt{no\\_trace} scales with capacity (Figure~\\ref{fig:cross_scale}) and shows the highest seed variance ($\\sigma{=}$4.48pp).\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig3_cross_model_gap}\n\\caption{Verdict accuracy vs.\\ model scale. \\texttt{exception\\_only} maintains ${\\geq}$99.33\\% regardless of scale, while \\texttt{no\\_trace} shows monotonic sensitivity (+4.12pp). \\texttt{nomarker} (markers removed) shows no scale degradation.}\n\\label{fig:cross_scale}\n\\end{figure}\n\n\\paragraph{VOTA cross-family variation.}\nExcluding outlier seeds, VOTA achieves ${\\geq}$98.57\\% across all four models (0.80pp range).\nDeepSeek seed 42 (84.45\\%) is a tokenizer-driven truncation failure (91.7\\% of samples exceed 2{,}048 tokens after tokenization; Appendix~\\ref{sec:tokenizer_analysis}), demonstrating that VOTA's longer sequences are sensitive to tokenizer efficiency: 1/4 models suffers catastrophic truncation under standard training length. \\texttt{exception\\_only}'s compact inputs (median 150 tokens) sidestep this vulnerability entirely.\n\n\\subsection{Component Ablation}\n\\label{sec:ablation}\n\nMulti-seed \\texttt{ae\\_only} ablations use Qwen-7B; \\texttt{loop\\_only} is evaluated across three models to test Tier~2 generalization (Table~\\ref{tab:cross_model}).\nTable~\\ref{tab:ablation} decomposes VOTA on Qwen-2.5-7B and reveals a two-tier hierarchy validated across all four models and three architecture families (Table~\\ref{tab:cross_model}): Tier~1 (${\\geq}$98.53\\%) and Tier~2 (77--86\\%) are separated by 12+pp with non-overlapping CIs.\n\n\\begin{table}[t]\n\\centering\n\\caption{Component ablation on Qwen-2.5-7B ($N{=}1{,}190$). Tier~1 signals achieve near-perfect accuracy; combining them (VOTA) slightly dilutes performance. Entries marked $^\\dag$/$^\\S$/$^\\ddag$ are 3-seed mean$\\pm$std; unmarked entries are single seed (seed 42). Per-seed breakdowns in Appendix~\\ref{sec:full_results}. Seed $\\sigma$ negatively correlates with density (0.00 for exception to 0.52 for loop).}\n\\label{tab:ablation}\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llccc}\n\\toprule\n\\textbf{Condition} & \\textbf{Components} & \\textbf{Acc (\\%)} & \\textbf{95\\% CI} & \\textbf{Tier} \\\\\n\\midrule\nae\\_only & assertion-point & 99.64$^\\dag$ & [99.26, 99.87] & 1 \\\\\nexception\\_only & exception events & \\textbf{99.83} & [99.58, 100.00] & 1 \\\\\nVOTA & exc+ae+loop & 99.05$^\\S$ & [98.49, 99.50] & --- \\\\\nVOTA\\_no\\_ae & exc+loop & 99.41 & [98.90, 99.80] & --- \\\\\nloop\\_only & loop compression & 86.05$^\\ddag$ & [83.97, 87.96] & 2 \\\\\nfull\\_trace & complete trace & 81.44{\\scriptsize$\\pm$1.11} & --- & --- \\\\\nno\\_trace & none & 75.13 & [72.77, 77.48] & --- \\\\\n\\midrule\nRegex (best) & exc.\\ type regex & 93.61 & --- & --- \\\\\n3-shot (Qwen-7B) & in-context learning & 90.84 & --- & --- \\\\\nZero-shot (4 models) & prompting & 51.0--93.5 & --- & --- \\\\\n\\bottomrule\n\\end{tabular}%\n}\n\\end{table}\n\nTier~1 signals are individually sufficient: \\texttt{exception\\_only} (99.83\\%$\\pm$0.00) exceeds VOTA (99.05\\%$\\pm$0.38) by +0.78pp (2/3 seeds $p{<}.05$, all directionally consistent), implying that combining signals introduces noise.\nRemoving assertion points has no effect (\\texttt{VOTA\\_no\\_ae} = 99.41\\%, single seed), indicating exception dominance.\nIndividual exception subcomponents (type, stacktrace, message) each independently achieve ${\\geq}$99.50\\%, indicating that the binary presence of an exception event, rather than any specific subcomponent, drives Tier~1 performance (Appendix~\\ref{sec:exc_subcomponent}).\nThe Tier~1/2 boundary is unambiguous: the lowest Tier~1 condition (\\texttt{ae\\_only} on DeepSeek, 98.53\\%$\\pm$0.30, 2 seeds) exceeds the highest Tier~2 (\\texttt{loop\\_only} on Qwen-7B, 86.05\\%, CI [83.97, 87.96]) by 12.48\\,pp with non-overlapping CIs (gap statistic supports $k{=}2$ clusters, silhouette ${\\geq}$0.74).\nTier~2 \\texttt{loop\\_only} lifts over \\texttt{no\\_trace} are model-dependent: Qwen +10.92pp (7B) and +7.19pp (1.5B); DeepSeek +6.95pp; CodeLlama +0.93pp (n.s.).\n\\paragraph{Rule-based baseline comparison.}\nThe strongest non-trivial regex heuristic (B4: exception class name matching; Table~\\ref{tab:regex}) achieves 93.61\\% accuracy (F1=0.876), trailing SFT \\texttt{exception\\_only} (99.83\\%, F1=0.997) by 6.22pp (McNemar $p{<}.001$).\nThe gap concentrates on caught-exception boundary cases: regex flags all exception events as failures, while SFT learns to distinguish caught exceptions (benign, inside \\texttt{try/except}) from uncaught faults, correctly resolving 6/8 boundary samples (Appendix~\\ref{sec:regex_baselines}).\nAcross all formats, SFT outperforms the best applicable regex by +3.62--23.86pp (Appendix~\\ref{sec:regex_baselines}).\n\n\\paragraph{Zero-shot and few-shot LLM baselines.}\nZero-shot prompting spans 51.0--93.5\\% across four models (42.44pp range); three-shot ICL on Qwen-7B (90.84\\%) improves only 1.76pp.\nSFT compresses this range to 0.50pp (99.39--99.89\\%), closing a 6--49pp gap with 4,720 samples (Appendix~\\ref{sec:zeroshot_cross_model}).\n\\paragraph{Frontier model crossover.}\nTwo frontier models illustrate that SFT's advantage depends on input density: under \\texttt{no\\_trace}, GPT-4o (84.45\\%) and GPT-4.1 (77.31\\%) outperform SFT Qwen-7B (75.13\\%), but under \\texttt{exception\\_only} the ranking reverses (SFT 99.83\\% vs.\\ GPT-4o 87.98\\%).\nCompact diagnostic input unlocks SFT's full advantage over general reasoning capacity.\n\n\\subsection{Format Marker Ablation}\n\\label{sec:nomarker}\n\nThe \\texttt{exception\\_only} format includes a \\texttt{[No exception data in trace]} marker in all pass-class samples (regex baseline B5 exploits this for 99.33\\% accuracy; Appendix~\\ref{sec:regex_baselines}).\nTo quantify the marker's contribution, we retrain with all format markers removed (\\texttt{nomarker} condition).\n\nQwen-7B 3-seed mean: 97.65\\% $\\pm$ 0.96 (seeds 42/123/456: 96.55/98.32/98.07\\%), a drop of 2.18pp from \\texttt{exception\\_only} (99.83\\%).\nQwen-1.5B: 97.82\\%, drop of 2.01pp.\nThe marker contribution (${\\sim}$2pp) accounts for only ${\\sim}$9\\% of the total exception lift over \\texttt{no\\_trace} (24.70pp on 7B).\nRegex baselines illustrate this decomposition: B5 (\\texttt{[No exception data]}$\\to$pass, 99.33\\% with markers) collapses to 28.49\\% without markers, showing it is entirely format-dependent.\nThe strongest semantic regex B4 (exception class matching, 93.61\\%) is marker-invariant; SFT \\texttt{nomarker} (97.65\\%) exceeds it by 4.04pp, isolating the learned semantic contribution beyond pattern matching.\n\n\\paragraph{Cross-dataset transfer.}\nBidirectional evaluation demonstrates generalization: HumanEval${\\to}$MBPP \\texttt{exception\\_only} achieves 99.41\\% ($N{=}4{,}270$) and MBPP${\\to}$HumanEval achieves 100.0\\% ($N{=}1{,}640$), while \\texttt{no\\_trace} drops to near-majority baseline in both directions (70.56\\% vs.\\ 69.02\\% majority; 67.99\\% vs.\\ 61.65\\%).\nThe near-zero transfer loss for exception signals, across independently authored problem sets with no problem overlap, shows SFT learns language-level diagnostic patterns, not dataset-specific artifacts.\nUnder marker removal, cross-dataset accuracy drops to 95.5\\% ($-$3.9pp), indicating that the majority of cross-dataset transfer relies on learned diagnostic patterns rather than format markers.\n\n\\subsection{Decomposing the Full-Trace Degradation}\n\\label{sec:density}\n\nThe 18.07pp gap between \\texttt{exception\\_only} (99.83\\%) and \\texttt{full\\_trace} (81.76\\%) could reflect gradient dilution (diagnostic tokens are ${\\sim}$1/500 of full traces, diluting gradient signal during training) or content quality (verbose input buries diagnostic signals at inference).\n\n\\paragraph{Controlled gradient masking.}\nTo isolate gradient dilution, we mask 99.8\\% of gradient updates during \\texttt{exception\\_only} training, matching the diagnostic token ratio of full traces while preserving compact input.\nThis yields 99.22\\% (mean $-$0.61pp from \\texttt{exception\\_only}, 3 seeds), limiting gradient dilution to ${\\leq}$4\\% of the 18.07pp gap (Table~\\ref{tab:density}).\nThe gradient masking bound attributes the remaining ${\\geq}$96\\% to content quality (diagnostic signal density at inference), though forward-pass attention during masked training is an unquantified residual.\nNote that masking affects only the backward pass; the model still attends to all input tokens during the forward pass, so this bounds gradient dilution's contribution but does not rule out attention-based information flow as a residual confound.\n\n\\begin{table}[t]\n\\centering\n\\caption{Decomposition of the full-trace degradation (Qwen-7B). Gradient masking attributes ${\\leq}$4\\% to gradient dilution; the bound assigns the remainder to content quality, though forward-pass attention is a residual confound (\\S\\ref{sec:density}). Label-only loss provides a confounded but directionally consistent complementary estimate.}\n\\label{tab:density}\n\\small\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Condition} & \\textbf{Acc (\\%)} & \\textbf{$\\Delta$} \\\\\n\\midrule\nexception\\_only & 99.83{\\scriptsize$\\pm$0.00} & --- \\\\\n\\quad + grad mask (99.8\\%) & 99.22{\\scriptsize$\\pm$0.20}$^\\S$ & $-$0.61pp \\\\\nfull\\_trace & 81.76$^\\ddag$ & $-$18.07pp \\\\\n\\midrule\n\\multicolumn{3}{l}{\\textit{Complementary (confounded):}} \\\\\nfull\\_trace + label-only loss & 85.94{\\scriptsize$\\pm$1.12} & +4.50pp$^\\dag$ \\\\\n\\bottomrule\n\\end{tabular}\n\\vspace{2pt}\n\\par\\raggedright\\footnotesize\n$^\\S$Mean $\\pm$ std over 3 seeds (42, 123, 456).\n$^\\ddag$Matched-seed baseline; 3-seed mean 81.44\\%$\\pm$1.11 (Table~\\ref{tab:cross_model}).\n$^\\dag$vs.\\ \\texttt{full\\_trace} (81.44\\%$\\pm$1.11); not significant under clustered bootstrap (95\\% CI [$-$0.6, +9.8]pp, $n_\\text{eff}{=}119$).\n\\end{table}\n\n\\paragraph{Complementary evidence.}\nLabel-only loss on full traces (+4.50pp, 3 seeds) yields a confounded upper bound of ${\\leq}$26\\% gradient contribution, consistent with the masking estimate (${\\leq}$4\\%) but not significant under clustered bootstrap (95\\% CI [$-$0.6, +9.8]pp).\nQwen-1.5B shows a similar label-only pattern (17\\%/83\\%, 3 seeds); CodeLlama and DeepSeek exhibit label-only collapse to majority baseline (28.5\\%), limiting this complementary analysis to the Qwen family.\nThe architecture dependence suggests label-only training is sensitive to model capacity or optimization landscape; the gradient masking ablation provides a more robust, architecture-independent decomposition.\nCross-architecture validation on two additional families is directionally consistent (single seed each): DeepSeek-Coder-6.7B achieves 99.33\\% and CodeLlama-13B achieves 100\\% under 99.8\\% masking, both well above the full-trace range (77--82\\%, Table~\\ref{tab:cross_model}), supporting content quality as the dominant factor across architectures.\nError analysis supports the content quality interpretation: all 217 \\texttt{full\\_trace} errors occur where tokenizer truncation removes diagnostic markers, manifesting through mechanical truncation rather than semantic confusion.\n\n\\subsection{Complementary Analyses}\n\\label{sec:additional}\n\n\\paragraph{Trace length ablation.}\n\\label{sec:trace_length}\nVarying the head-truncated trace token budget (256--no limit) on Qwen-7B yields accuracy in a narrow 77.2\\%--81.8\\% band with a non-monotonic pattern: 1024-token prefixes (77.23\\%) underperform 512-token prefixes (80.42\\%, $p{=}.002$), because mid-length prefixes retain enough irrelevant content to mislead the model while discarding diagnostic events near the trace terminus (Appendix~\\ref{sec:trace_length_full}).\nCritically, removing the token budget entirely (no truncation) yields 81.76\\%, identical to head-2048, ruling out truncation as the explanation for the full-trace degradation.\nThis non-monotonicity is specific to head-truncation; under tail-truncation, accuracy increases monotonically for two of three models (Table~\\ref{tab:tail_cross_model} in Appendix), with only DeepSeek showing a mild architecture-specific reversal at tail-1024$\\to$tail-2048 ($-$1.5pp).\n\n\\paragraph{Truncation direction and budget curve.}\nTail-truncation dramatically outperforms head-truncation: tail-2048 exceeds head-2048 by 15.5--22.6pp across three models (Appendix~\\ref{sec:trace_length_full}).\nFigure~\\ref{fig:budget_curve} reveals a sharp phase transition at 384$\\to$512 tail tokens: all four models simultaneously jump +13.2--22.0pp, crossing from near-baseline to 93--98\\%.\nThis threshold coincides with the globals module dump boundary (${\\sim}$384 tokens), beyond which structured execution markers become visible (Table~\\ref{tab:tail_cross_model}).\nBeyond 512 tokens, all 12 model$\\times$seed combinations converge into [93.61\\%, 98.24\\%] (Table~\\ref{tab:tail512_seeds}).\n\\texttt{tail\\_2048} captures 95--98\\% of \\texttt{exception\\_only}'s accuracy; the residual 2--5pp gap shows semantic extraction still outperforms positional extraction.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{budget_curve}\n\\caption{Tail-truncation budget curve across four models and three architecture families ($N{=}1{,}190$). A sharp phase transition at 384$\\to$512 tokens (+13.2--22.0pp) coincides with the globals module dump boundary. Dashed lines: \\texttt{exception\\_only} ceiling and \\texttt{no\\_trace} floor.}\n\\label{fig:budget_curve}\n\\end{figure}\n\n\\paragraph{Calibration.}\n\\label{sec:calibration}\nCalibration mirrors the tier hierarchy: \\texttt{exception\\_only} achieves ECE = 0.0027 vs.\\ 0.171 for \\texttt{no\\_trace}, a 63$\\times$ gap (Figure~\\ref{fig:calibration}).\nThis calibration advantage generalizes across architectures and scales: all four models (1.5B--13B) achieve ECE ${<}$ 0.007 under \\texttt{exception\\_only} (Table~\\ref{tab:calibration_cross} in Appendix), indicating well-calibrated predictions rather than overfit confidence.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig2_calibration}\n\\caption{Reliability diagrams for four trace conditions on Qwen-2.5-7B ($N{=}1{,}190$, seed=42). \\texttt{exception\\_only} (ECE=0.0027) clusters near the diagonal, while \\texttt{no\\_trace} (ECE=0.171) exhibits systematic overconfidence, a 63$\\times$ gap.}\n\\label{fig:calibration}\n\\end{figure}\n\n\\paragraph{Error analysis.}\n\\texttt{exception\\_only}'s 2 errors have zero overlap with all other conditions' error sets (Jaccard = 0.000; Appendix~\\ref{sec:error_overlap}); per-type breakdown shows all standard exception types achieve 100\\% accuracy, with only \\texttt{GeneratorExit} (a benign \\texttt{BaseException} subclass) causing failures (Appendix~\\ref{sec:exception_type}).\n\n\\paragraph{Length control.}\nPadding \\texttt{exception\\_only} to 2{,}048 tokens, even in a semantically loaded position (after the verdict region), yields identical accuracy (99.83\\%), indicating the 18--23pp gap arises from spurious patterns in verbose trace content, not sequence length.\n\n\\paragraph{Supplementary OOD analysis.}\n\\label{sec:debugbench}\nOn DebugBench \\citep{tian2024debugbench} ($N{=}426$), the condition ranking is preserved: \\texttt{exception\\_only} 100\\%, VOTA 99.77\\%, \\texttt{no\\_trace} 96.71\\%.\nHowever, narrow margins (3.29pp headroom from \\texttt{no\\_trace}) limit discriminative power; this supplementary analysis preserves the ranking but cannot establish effect sizes comparable to the primary dataset (Appendix~\\ref{sec:debugbench_full}).\n",
      "numLines": 218,
      "startLine": 1,
      "totalLines": 218
    }
  },
  "sourceToolAssistantUUID": "7a6d2a67-698e-4f97-af4f-7fe3845fa1b6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/.claude/sessions/paper_audit_content_b575bb0e",
  "sessionId": "1db729b7-6c37-474e-9cbb-179c13a8aeb8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-24T16:16:15.319Z_

<details open><summary>🔧 Tool call — Read · `toolu_01KrTPiD8XFSwfZGBXntfUyX`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "579cb5cb-4230-4c40-ad38-b560fec732e1",
  "isSidechain": false,
  "requestId": "req_011CbMh9tV4aN8QV3riH9wUf",
  "type": "assistant",
  "uuid": "ec3e6f1a-fcc2-428f-9b1d-cf7ff356ca00",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/.claude/sessions/paper_audit_content_b575bb0e",
  "sessionId": "1db729b7-6c37-474e-9cbb-179c13a8aeb8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012VsV8ncx6FrdGuWaCHMfaG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11894,
      "cache_read_input_tokens": 38247,
      "output_tokens": 703,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11894,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 703,
          "cache_read_input_tokens": 38247,
          "cache_creation_input_tokens": 11894,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11894
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

_source line 32 · 2026-05-24T16:16:15.324Z_

<details><summary>↩ Tool result · `toolu_01KrTPiD8XFSwfZGBXntfUyX`</summary>

```text
1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\paragraph{A descriptive two-pathway framework.}
5	The results suggest two independent signal pathways and a dilution mechanism that together explain why complete traces degrade SFT learning.
6	
7	\paragraph{Explicit pathway: diagnostic tokens.}
8	The diagnostic token ratio $d$ (\S2.1) correlates strongly with accuracy across five conditions, and all four models achieve near-perfect accuracy under \texttt{exception\_only} (Table~\ref{tab:cross_model}).
9	\texttt{ae\_only}, a strict superset, slightly underperforms (Table~\ref{tab:ablation}), indicating that additional content introduces noise even within exception events.
10	
11	\paragraph{Implicit pathway: terminal execution state.}
12	Tail-truncated traces achieve 93--98\% accuracy (Table~\ref{tab:tail_cross_model}) despite $d {\approx} 0$.
13	At ${\geq}$512 tokens (Figure~\ref{fig:budget_curve}), tail truncation captures \texttt{[Line~X]} variable values at final execution steps, which implicitly encode verdict direction; below 384 tokens, the globals module dump consumes the entire budget, yielding near-\texttt{no\_trace} performance.
14	
15	\paragraph{Diagnostic signal dilution in complete traces.}
16	Both pathways' signals exist in full traces but are buried under thousands of intermediate tokens.
17	Controlled gradient masking (\S\ref{sec:density}) attributes ${\leq}$4\% of the gap to gradient dilution, assigning the majority to content quality at inference: diagnostic tokens are too sparse for the model to reliably extract from verbose input.
18	Training dynamics corroborate this (Figure~\ref{fig:training_dynamics}): \texttt{exception\_only} converges within 50 steps while \texttt{full\_trace} oscillates without convergence.
19	
20	\begin{figure}[t]
21	\centering
22	\includegraphics[width=\columnwidth]{training_dynamics}
23	\caption{Training dynamics: \texttt{exception\_only} converges to 99.83\% by step 150; \texttt{full\_trace} with label-only loss oscillates (82--89\%) without convergence.}
24	\label{fig:training_dynamics}
25	\end{figure}
26	
27	\paragraph{Why SFT over regex?}
28	The contribution is the diagnostic decomposition, not a prediction system; nonetheless, SFT dominates regex on every axis beyond raw accuracy.
29	SFT retains 97.65\% under marker removal while the regex collapses to 28.49\% (\S\ref{sec:nomarker}), provides 63$\times$ better calibration (\S\ref{sec:calibration}), and transfers bidirectionally across datasets with negligible loss.
30	
31	\paragraph{Design implications.}
32	Complete traces capture only 3--6pp of the ${\sim}$25pp headroom over source code alone, while exception events capture 23--27pp.
33	This runs counter to the field's operating assumption that more trace information should help \citep{chen2025tracepile,wang2025dcsh}; the magnitude and component decomposition are not predictable from information-theoretic priors alone.
34	The two-tier hierarchy suggests a practical fallback: extract exception events first; resort to tail-truncated state otherwise.
35	Tier~2 benefit is model-dependent (Qwen +10.9pp; CodeLlama +0.9pp), so trace design should match deployment model capacity (Appendix~\ref{sec:robustness_analysis}).
36	
37	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ec3e6f1a-fcc2-428f-9b1d-cf7ff356ca00",
  "isSidechain": false,
  "promptId": "96f110f9-4fbd-4295-8cdb-ef5a8ad15d7a",
  "type": "user",
  "uuid": "8f51885e-41f7-4f8f-a308-a271170b05cf",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/discussion.tex",
      "content": "\\section{Discussion}\n\\label{sec:discussion}\n\n\\paragraph{A descriptive two-pathway framework.}\nThe results suggest two independent signal pathways and a dilution mechanism that together explain why complete traces degrade SFT learning.\n\n\\paragraph{Explicit pathway: diagnostic tokens.}\nThe diagnostic token ratio $d$ (\\S2.1) correlates strongly with accuracy across five conditions, and all four models achieve near-perfect accuracy under \\texttt{exception\\_only} (Table~\\ref{tab:cross_model}).\n\\texttt{ae\\_only}, a strict superset, slightly underperforms (Table~\\ref{tab:ablation}), indicating that additional content introduces noise even within exception events.\n\n\\paragraph{Implicit pathway: terminal execution state.}\nTail-truncated traces achieve 93--98\\% accuracy (Table~\\ref{tab:tail_cross_model}) despite $d {\\approx} 0$.\nAt ${\\geq}$512 tokens (Figure~\\ref{fig:budget_curve}), tail truncation captures \\texttt{[Line~X]} variable values at final execution steps, which implicitly encode verdict direction; below 384 tokens, the globals module dump consumes the entire budget, yielding near-\\texttt{no\\_trace} performance.\n\n\\paragraph{Diagnostic signal dilution in complete traces.}\nBoth pathways' signals exist in full traces but are buried under thousands of intermediate tokens.\nControlled gradient masking (\\S\\ref{sec:density}) attributes ${\\leq}$4\\% of the gap to gradient dilution, assigning the majority to content quality at inference: diagnostic tokens are too sparse for the model to reliably extract from verbose input.\nTraining dynamics corroborate this (Figure~\\ref{fig:training_dynamics}): \\texttt{exception\\_only} converges within 50 steps while \\texttt{full\\_trace} oscillates without convergence.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{training_dynamics}\n\\caption{Training dynamics: \\texttt{exception\\_only} converges to 99.83\\% by step 150; \\texttt{full\\_trace} with label-only loss oscillates (82--89\\%) without convergence.}\n\\label{fig:training_dynamics}\n\\end{figure}\n\n\\paragraph{Why SFT over regex?}\nThe contribution is the diagnostic decomposition, not a prediction system; nonetheless, SFT dominates regex on every axis beyond raw accuracy.\nSFT retains 97.65\\% under marker removal while the regex collapses to 28.49\\% (\\S\\ref{sec:nomarker}), provides 63$\\times$ better calibration (\\S\\ref{sec:calibration}), and transfers bidirectionally across datasets with negligible loss.\n\n\\paragraph{Design implications.}\nComplete traces capture only 3--6pp of the ${\\sim}$25pp headroom over source code alone, while exception events capture 23--27pp.\nThis runs counter to the field's operating assumption that more trace information should help \\citep{chen2025tracepile,wang2025dcsh}; the magnitude and component decomposition are not predictable from information-theoretic priors alone.\nThe two-tier hierarchy suggests a practical fallback: extract exception events first; resort to tail-truncated state otherwise.\nTier~2 benefit is model-dependent (Qwen +10.9pp; CodeLlama +0.9pp), so trace design should match deployment model capacity (Appendix~\\ref{sec:robustness_analysis}).\n\n",
      "numLines": 37,
      "startLine": 1,
      "totalLines": 37
    }
  },
  "sourceToolAssistantUUID": "ec3e6f1a-fcc2-428f-9b1d-cf7ff356ca00",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/.claude/sessions/paper_audit_content_b575bb0e",
  "sessionId": "1db729b7-6c37-474e-9cbb-179c13a8aeb8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-24T16:16:15.806Z_

<details open><summary>🔧 Tool call — Read · `toolu_01CSJwwsjHZyvJdCowqEJF8D`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8f51885e-41f7-4f8f-a308-a271170b05cf",
  "isSidechain": false,
  "requestId": "req_011CbMh9tV4aN8QV3riH9wUf",
  "type": "assistant",
  "uuid": "32a3091c-9007-45d0-b151-18eec1fdb3e9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/.claude/sessions/paper_audit_content_b575bb0e",
  "sessionId": "1db729b7-6c37-474e-9cbb-179c13a8aeb8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012VsV8ncx6FrdGuWaCHMfaG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11894,
      "cache_read_input_tokens": 38247,
      "output_tokens": 703,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11894,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 703,
          "cache_read_input_tokens": 38247,
          "cache_creation_input_tokens": 11894,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11894
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

_source line 34 · 2026-05-24T16:16:15.811Z_

<details><summary>↩ Tool result · `toolu_01CSJwwsjHZyvJdCowqEJF8D`</summary>

```text
1	\section{Conclusion}
2	
3	Across four code-specialized models (1.5B--13B), compact exception events (${\geq}$99.33\%) outperform complete traces (77--82\%) by 18--23pp; gradient masking (${\leq}$4\% dilution), cross-dataset transfer (99.4--100\%), and marker-removal robustness show that diagnostic density, not information quantity, drives SFT learning.
4	Practitioners should extract exception events first; tail-truncated traces (${\geq}$512 tokens) recover 93--98\% as fallback.
5	Whether models beyond 13B can overcome signal dilution in complete traces, and whether these findings extend to languages without Python's structured exception hierarchy, remain open questions.
6	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "32a3091c-9007-45d0-b151-18eec1fdb3e9",
  "isSidechain": false,
  "promptId": "96f110f9-4fbd-4295-8cdb-ef5a8ad15d7a",
  "type": "user",
  "uuid": "e5d49867-727b-445f-a2e9-be846c9040b5",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/conclusion.tex",
      "content": "\\section{Conclusion}\n\nAcross four code-specialized models (1.5B--13B), compact exception events (${\\geq}$99.33\\%) outperform complete traces (77--82\\%) by 18--23pp; gradient masking (${\\leq}$4\\% dilution), cross-dataset transfer (99.4--100\\%), and marker-removal robustness show that diagnostic density, not information quantity, drives SFT learning.\nPractitioners should extract exception events first; tail-truncated traces (${\\geq}$512 tokens) recover 93--98\\% as fallback.\nWhether models beyond 13B can overcome signal dilution in complete traces, and whether these findings extend to languages without Python's structured exception hierarchy, remain open questions.\n",
      "numLines": 6,
      "startLine": 1,
      "totalLines": 6
    }
  },
  "sourceToolAssistantUUID": "32a3091c-9007-45d0-b151-18eec1fdb3e9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/.claude/sessions/paper_audit_content_b575bb0e",
  "sessionId": "1db729b7-6c37-474e-9cbb-179c13a8aeb8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-24T16:16:16.291Z_

<details open><summary>🔧 Tool call — Read · `toolu_01ALW7bNRWDDbbppVDVJNikJ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e5d49867-727b-445f-a2e9-be846c9040b5",
  "isSidechain": false,
  "requestId": "req_011CbMh9tV4aN8QV3riH9wUf",
  "type": "assistant",
  "uuid": "e58add99-562e-49f5-aa3c-19363fa0ae30",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/.claude/sessions/paper_audit_content_b575bb0e",
  "sessionId": "1db729b7-6c37-474e-9cbb-179c13a8aeb8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012VsV8ncx6FrdGuWaCHMfaG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11894,
      "cache_read_input_tokens": 38247,
      "output_tokens": 703,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11894,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 703,
          "cache_read_input_tokens": 38247,
          "cache_creation_input_tokens": 11894,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11894
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

_source line 36 · 2026-05-24T16:16:16.551Z_

<details><summary>↩ Tool result · `toolu_01ALW7bNRWDDbbppVDVJNikJ`</summary>

```text
1	\section{Per-Class Performance Breakdown}
2	\label{sec:per_class}
3	
4	Table~\ref{tab:per_class} reports per-class precision, recall, and F1 for all experimental conditions.
5	
6	\begin{table*}[t]
7	\centering
8	\caption{Per-class precision, recall, and F1 for all experimental conditions (seed 42). DeepSeek VOTA seed 42 is a training failure (84.45\%, fail recall = 45.4\%) due to tokenizer-driven truncation; seeds 123/456 achieve 99.16\%/99.33\%.}
9	\label{tab:per_class}
10	\small
11	\begin{tabular}{llccccccc}
12	\toprule
13	\textbf{Condition} & \textbf{Model} & \textbf{Acc} & \textbf{Pass P} & \textbf{Pass R} & \textbf{Pass F1} & \textbf{Fail P} & \textbf{Fail R} & \textbf{Fail F1} \\
14	\midrule
15	No Trace          & Qwen-2.5-7B & 75.13 & 87.76 & 75.79 & 81.34 & 54.73 & 73.45 & 62.72 \\
16	Full Trace        & Qwen-2.5-7B & 81.76 & 87.74 & 86.60 & 87.17 & 67.43 & 69.62 & 68.51 \\
17	Full Trace (LO)   & Qwen-2.5-7B & 86.22 & 88.21 & 93.18 & 90.63 & 80.07 & 68.73 & 73.97 \\
18	VOTA              & Qwen-2.5-7B & 99.41 & 100.00 & 99.18 & 99.59 & 97.98 & 100.00 & 98.98 \\
19	Exception Only    & Qwen-2.5-7B & 99.83 & 100.00 & 99.76 & 99.88 & 99.41 & 100.00 & 99.71 \\
20	AE Only           & Qwen-2.5-7B & 99.92 & 100.00 & 99.88 & 99.94 & 99.71 & 100.00 & 99.85 \\
21	Loop Only         & Qwen-2.5-7B & 85.63 & 92.39 & 87.07 & 89.66 & 71.65 & 82.01 & 76.48 \\
22	VOTA\_no\_ae       & Qwen-2.5-7B & 99.41 & 99.88 & 99.29 & 99.59 & 98.26 & 99.71 & 98.98 \\
23	\midrule
24	No Trace          & DeepSeek-6.7B & 73.36 & 81.71 & 80.85 & 81.28 & 53.16 & 54.57 & 53.86 \\
25	Full Trace        & DeepSeek-6.7B & 79.16 & 85.70 & 85.10 & 85.40 & 63.20 & 64.30 & 63.70 \\
26	VOTA              & DeepSeek-6.7B & 84.45 & 82.14 & 100.00 & 90.20 & 100.00 & 45.40 & 62.50 \\
27	Exception Only    & DeepSeek-6.7B & 99.33 & 100.00 & 99.06 & 99.53 & 97.69 & 100.00 & 98.83 \\
28	AE Only           & DeepSeek-6.7B & 98.74 & 98.40 & 99.90 & 99.10 & 99.70 & 95.90 & 97.70 \\
29	\bottomrule
30	\end{tabular}
31	\end{table*}
32	
33	%% ============================================================
34	\section{Training Details}
35	\label{sec:training_details}
36	
37	Table~\ref{tab:hyperparams} summarizes the training hyperparameters shared across all conditions.
38	All experiments use the HuggingFace TRL \texttt{SFTTrainer} with LoRA \citep{hu2022lora} applied to all linear layers.
39	
40	\begin{table}[t]
41	\centering
42	\caption{Training hyperparameters (shared across all conditions).}
43	\label{tab:hyperparams}
44	\small
45	\resizebox{\columnwidth}{!}{%
46	\begin{tabular}{ll}
47	\toprule
48	\textbf{Hyperparameter} & \textbf{Value} \\
49	\midrule
50	LoRA rank ($r$)            & 16 \\
51	LoRA alpha ($\alpha$)      & 32 \\
52	LoRA dropout               & 0.05 \\
53	LoRA target modules        & all linear layers \\
54	\midrule
55	Epochs                     & 3 \\
56	Per-device batch size       & 4 \\
57	Gradient accumulation steps & 8 \\
58	Effective batch size        & 32 \\
59	\midrule
60	Learning rate               & $2 \times 10^{-4}$ \\
61	LR scheduler                & linear decay \\
62	Warmup ratio                & 0.1 \\
63	Weight decay                & 0.01 \\
64	\midrule
65	Max sequence length         & 2048 tokens \\
66	Primary seed                & 42 \\
67	Robustness seeds            & 123, 456 \\
68	\midrule
69	Hardware                    & 1$\times$ enterprise-grade GPU (${\geq}$80\,GB VRAM) \\
70	Framework                   & HuggingFace TRL SFTTrainer \\
71	\bottomrule
72	\end{tabular}%
73	}
74	\end{table}
75	
76	Table~\ref{tab:train_time} reports per-condition training wall-clock times.
77	Conditions with longer trace inputs (e.g., \texttt{full\_trace}, VOTA) require proportionally more training time due to increased sequence lengths.
78	
79	\begin{table}[t]
80	\centering
81	\caption{Training wall-clock time per condition on a single enterprise-grade GPU (${\geq}$80\,GB VRAM). Where multiple seeds were run, individual times are listed.}
82	\label{tab:train_time}
83	\small
84	\begin{tabular}{llr}
85	\toprule
86	\textbf{Condition} & \textbf{Seed(s)} & \textbf{Time (h)} \\
87	\midrule
88	no\_trace       & 42         & ${\sim}$0.5 \\
89	full\_trace     & 42         & ${\sim}$2.2 \\
90	label\_only     & 42         & ${\sim}$2.2 \\
91	VOTA                     & 42         & ${\sim}$2.3 \\
92	exception\_only & 42         & ${\sim}$2.1 \\
93	exception\_only & 123        & ${\sim}$2.1 \\
94	exception\_only & 456        & ${\sim}$1.3 \\
95	ae\_only        & 42         & ${\sim}$1.8 \\
96	loop\_only      & 42         & ${\sim}$2.1 \\
97	VOTA\_no\_ae    & 42         & ${\sim}$1.8 \\
98	\bottomrule
99	\end{tabular}
100	\end{table}
101	
102	%% ============================================================
103	\section{VOTA Extraction Algorithm}
104	\label{sec:vota_algorithm}
105	
106	Algorithm~\ref{alg:vota} describes the three-component VOTA extraction pipeline applied to a raw \texttt{sys.settrace} execution log.
107	
108	\begin{algorithm}[t]
109	\caption{VOTA Trace Extraction}
110	\label{alg:vota}
111	\small
112	\begin{algorithmic}[1]
113	\REQUIRE Raw trace $T$ from \texttt{sys.settrace} (list of events)
114	\ENSURE Compressed VOTA representation $V$
115	\STATE $V \leftarrow$ empty string
116	\STATE \textbf{// Component 1: Exception summary}
117	\FOR{each event $e$ in $T$ with type \texttt{exception}}
118	  \STATE Parse traceback $\rightarrow$ extract error type, message, file, line
119	  \STATE Append \texttt{[ERROR] type: message (file:line)} to $V$
120	\ENDFOR
121	\IF{no exception events found}
122	  \STATE Append \texttt{[No exception data in trace]} to $V$
123	\ENDIF
124	\STATE \textbf{// Component 2: Assertion-point comparison}
125	\FOR{each \texttt{assert} or \texttt{return} event $e$ in $T$}
126	  \STATE Extract actual value from execution state
127	  \STATE Extract expected value from test assertion
128	  \STATE Append \texttt{[ASSERT] actual=... expected=... match=T/F} to $V$
129	\ENDFOR
130	\STATE \textbf{// Component 3: Loop compression}
131	\FOR{each consecutive repeated line sequence $S$ in $T$}
132	  \IF{$|S| \geq 2$ iterations of same loop body}
133	    \STATE Replace $S$ with single iteration + \texttt{[repeated $\times$N]}
134	  \ENDIF
135	\ENDFOR
136	\STATE Append compressed non-exception lines to $V$
137	\RETURN $V$
138	\end{algorithmic}
139	\end{algorithm}
140	
141	%% ============================================================
142	\section{VOTA Trace Examples}
143	\label{sec:vota_examples}
144	
145	We provide two representative VOTA trace examples illustrating the fail and pass cases.
146	In the fail case, the exception event provides an unambiguous fault signal.
147	In the pass case, the absence of an exception event combined with a matching assertion point confirms correct execution.
148	
149	\paragraph{Fail example.}
150	A \texttt{ZeroDivisionError} triggers an \texttt{[ERROR]} event, providing a direct fault signal that is sufficient for the model to predict \texttt{fail}.
151	
152	\begin{scriptsize}
153	\begin{verbatim}
154	## Function
155	def divide(a, b):
156	    return a / b
157	
158	## Test Input
159	divide(1, 0)
160	
161	## Expected Output
162	inf
163	
164	## VOTA Trace
165	[ERROR] ZeroDivisionError: division by zero
166	
167	## Verdict
168	fail
169	\end{verbatim}
170	\end{scriptsize}
171	
172	\paragraph{Pass example.}
173	No exception is raised, and the assertion point confirms that the actual output matches the expected value.
174	
175	\begin{scriptsize}
176	\begin{verbatim}
177	## Function
178	def add(a, b):
179	    return a + b
180	
181	## Test Input
182	add(2, 3)
183	
184	## Expected Output
185	5
186	
187	## VOTA Trace
188	[LOOP] No loops detected.
189	[ASSERT] actual=5, expected=5
190	
191	## Verdict
192	pass
193	\end{verbatim}
194	\end{scriptsize}
195	
196	These examples illustrate the core asymmetry exploited by the \texttt{exception\_only} condition: fail cases produce an explicit \texttt{[ERROR]} event, while pass cases are characterized by its absence.
197	This binary signal (presence vs.\ absence of an exception) is sufficient for near-perfect verdict prediction.
198	
199	%% ============================================================
200	\section{Full Experimental Results}
201	\label{sec:full_results}
202	
203	Tables~\ref{tab:full_qwen} and \ref{tab:full_deepseek} report the complete experimental results across all conditions, models, and seeds.
204	
205	\begin{table}[t]
206	\centering
207	\caption{Full results for Qwen-2.5-Coder-7B across all conditions and seeds. Conditions with a single seed report no variance. \texttt{exception\_only} achieves 99.83\% across all three seeds ($\sigma{=}$0). \texttt{ae\_only} achieves 99.64\% mean ($\pm$0.49; seed 123 at 99.08\% is the outlier).}
208	\label{tab:full_qwen}
209	\small
210	\resizebox{\columnwidth}{!}{%
211	\begin{tabular}{lcccc}
212	\toprule
213	\textbf{Condition} & \textbf{S42} & \textbf{S123} & \textbf{S456} & \textbf{Mean $\pm$ Std} \\
214	\midrule
215	exception\_only & 99.83 & 99.83 & 99.83 & 99.83 $\pm$ 0.00 \\
216	ae\_only        & 99.92 & 99.08 & 99.92 & 99.64 $\pm$ 0.49 \\
217	VOTA                     & 99.41 & 98.66 & 99.08 & 99.05 $\pm$ 0.38 \\
218	VOTA\_no\_ae    & 99.41 & ---   & ---   & --- \\
219	label\_only     & 86.22 & 86.89 & 84.70 & 85.94 $\pm$ 1.12 \\
220	loop\_only      & 85.63 & 85.88 & 86.64 & 86.05 $\pm$ 0.52 \\
221	full\_trace     & 81.76 & 80.20 & 82.35 & 81.44 $\pm$ 1.11 \\
222	no\_trace       & 75.13 & ---   & ---   & --- \\
223	\bottomrule
224	\end{tabular}%
225	}
226	\end{table}
227	
228	\begin{table}[t]
229	\centering
230	\caption{Full results for DeepSeek-Coder-6.7B across all conditions and seeds. \texttt{exception\_only} is consistent across seeds: 99.33/99.50/99.33 ($\sigma{=}$0.10pp).}
231	\label{tab:full_deepseek}
232	\small
233	\resizebox{\columnwidth}{!}{%
234	\begin{tabular}{llcc}
235	\toprule
236	\textbf{Condition} & \textbf{Seed} & \textbf{Accuracy} & \textbf{Notes} \\
237	\midrule
238	exception\_only & 42  & 99.33 & epoch 1: 99.83 \\
239	exception\_only & 456 & 99.33 & CI [98.82, 99.75] \\
240	exception\_only & 123 & 99.50 & \\
241	\midrule
242	VOTA                     & 42  & 84.45 & training failure; fail recall = 45.4\% \\
243	VOTA                     & 123 & 99.16 & \\
244	VOTA                     & 456 & 99.33 & \\
245	no\_trace       & 42  & 73.36 & \\
246	full\_trace     & 42  & 79.16 & CI [76.80, 81.30] \\
247	\bottomrule
248	\end{tabular}%
249	}
250	\end{table}
251	
252	%% ============================================================
253	\section{Tokenizer and Truncation Analysis}
254	\label{sec:tokenizer_analysis}
255	
256	DeepSeek VOTA seed 42 (84.45\%) is a training failure driven by tokenizer-induced truncation.
257	Re-evaluation of the seed 42 checkpoint with the standard max\_length=2048 yields 16\% accuracy, consistent with complete model collapse rather than marginal degradation.
258	The previously reported 84.45\% was obtained with max\_length=16384, which partially bypasses tokenizer truncation.
259	Seeds 123 and 456, evaluated under identical conditions, achieve 99.16\% and 99.33\% respectively.
260	The DeepSeek tokenizer averages 2{,}626 tokens per VOTA sample versus 1{,}929 for Qwen, causing 91.7\% of DeepSeek VOTA training samples to exceed the 2{,}048-token context window.
261	The training framework preserves the verdict label but truncates trace content, so the model trains with incomplete diagnostic information for the majority of samples.
262	Seeds 123 and 456 (99.16\% and 99.33\%) demonstrate that DeepSeek can learn VOTA when LoRA initialization avoids the truncation-sensitive basin; the 2-seed mean (99.25\%$\pm$0.12) matches the cross-model VOTA range (98.74--99.54\%).
263	
264	A post-hoc group analysis on seed 42 provides directional evidence: partitioning test samples by whether their training-set counterparts exceeded the context window, intact samples ($N{=}99$) achieve 100\% accuracy while truncated samples ($N{=}1{,}091$) achieve 83.04\% (95\% CI [80.75\%, 85.24\%]; Fisher exact $p{<}.001$), with all 185 errors concentrated in the fail class (fail recall = 31.23\%).
265	Per-class analysis (Table~\ref{tab:per_class}) shows that seed 42 achieves 100\% fail precision but only 45.43\% fail recall, systematically defaulting to \texttt{pass}.
266	
267	Seed robustness is consistent across models: Qwen \texttt{exception\_only} produces identical 99.83\% across all three seeds ($\sigma{=}0$), and DeepSeek achieves 99.39\%$\pm$0.10 (seeds 42/456: 99.33\%, seed 123: 99.50\%).
268	Because \texttt{exception\_only} test inputs contain 48.99\% duplicates (607 unique of 1,190; \S\ref{sec:dataset}), CIs assume $n{=}1{,}190$ independent trials; under deduplication ($n{=}607$), Qwen's accuracy is 99.67\% (Wilson CI [98.81, 99.91]).
269	
270	%% ============================================================
271	\section{Persistent Error Analysis}
272	\label{sec:irreducible}
273	
274	The \texttt{exception\_only} condition with Qwen-2.5-Coder-7B misclassifies exactly 2 out of 1,190 test samples across all three seeds (42, 123, 456), with 100\% overlap across seeds.
275	Both samples (IDs 901 and 905) share the following characteristics:
276	
277	\begin{itemize}
278	\item \textbf{Function:} \texttt{check\_dict\_case} (HumanEval/95), a function that checks whether all dictionary keys are uniformly upper-case or lower-case strings.
279	\item \textbf{Ground-truth label:} \texttt{pass}.
280	\item \textbf{Predicted label:} \texttt{fail} (false negative).
281	\item \textbf{Cross-seed consistency:} Both samples are misclassified identically by all three seeds, indicating a systematic rather than stochastic error.
282	\end{itemize}
283	
284	Manual inspection reveals the root cause: \texttt{check\_dict\_case} uses \texttt{all()} over a generator expression, and Python's \texttt{all()} short-circuits on the first \texttt{True} value, raising \texttt{GeneratorExit} to terminate the generator.
285	Because \texttt{GeneratorExit} is a \texttt{BaseException} subclass, the tracer records it as seven \texttt{[ERROR] GeneratorExit} lines, even though the function executes correctly and the test passes.
286	The model observes these spurious error markers and reasonably but incorrectly predicts \texttt{fail}.
287	This is not a model failure but a representation ambiguity: the \texttt{exception\_only} format cannot distinguish genuine exceptions from benign \texttt{BaseException} subclasses triggered by Python's iterator protocol.
288	
289	Most configurations converge to these same 2 errors: Qwen-1.5B, Qwen-7B (3 seeds), CodeLlama-13B (seeds 42/456), and DeepSeek-6.7B (seeds 42/456) all produce error set $\{901, 905\}$.
290	However, CodeLlama-13B seed 123 achieves 100\% accuracy (0/1190 errors), correctly classifying both samples.
291	This demonstrates that 99.83\% is a near-perfect \emph{floor} (the convergence attractor for most LoRA initializations) rather than a hard data ceiling: the representation supports perfect accuracy, but most initializations converge to the same 2-error basin.
292	The practical implication is that these errors are high-probability convergence artifacts addressable through seed selection or ensemble methods, not fundamental limitations of the exception-based representation.
293	
294	%% ============================================================
295	\section{Exception Type Accuracy Breakdown}
296	\label{sec:exception_type}
297	
298	Table~\ref{tab:exception_type} reports \texttt{exception\_only} accuracy stratified by exception type on Qwen-2.5-7B (seed=42, $N{=}1{,}190$).
299	All standard exception types (\texttt{TypeError}, \texttt{ValueError}, \texttt{IndexError}, etc.) achieve 100\% accuracy.
300	The only misclassifications arise from \texttt{GeneratorExit}, a \texttt{BaseException} subclass that is not an \texttt{Exception}. It is raised by Python's iterator protocol during generator short-circuiting, not by actual program errors.
301	
302	\begin{table}[t]
303	\centering
304	\caption{Exception type accuracy breakdown for \texttt{exception\_only} (Qwen-7B, seed=42). All true error types achieve 100\%. The only failures come from \texttt{GeneratorExit} (a \texttt{BaseException} subclass, not an \texttt{Exception}), which appears in 2 passing samples.}
305	\label{tab:exception_type}
306	\small
307	\begin{tabular}{lcc}
308	\toprule
309	\textbf{Exception Type} & \textbf{Samples} & \textbf{Accuracy} \\
310	\midrule
311	TypeError & 96 & 100\% \\
312	ValueError & 62 & 100\% \\
313	IndexError & 41 & 100\% \\
314	KeyError & 28 & 100\% \\
315	AttributeError & 19 & 100\% \\
316	AssertionError & 15 & 100\% \\
317	RecursionError & 12 & 100\% \\
318	Other Exception & 66 & 100\% \\
319	\midrule
320	GeneratorExit (BaseException) & 2 & 0\% \\
321	No exception (pass class) & 849 & 100\% \\
322	\bottomrule
323	\end{tabular}
324	\end{table}
325	
326	This is consistent with the model having learned a clean decision boundary: any true \texttt{Exception} subclass in the trace implies failure.
327	The \texttt{GeneratorExit} case represents a semantic ambiguity in the trace format rather than a model failure, as discussed in \S\ref{sec:irreducible}.
328	
329	%% ============================================================
330	\section{Exception Subcomponent Ablation}
331	\label{sec:exc_subcomponent}
332	
333	To test whether verdict prediction depends on a specific exception subcomponent or merely the binary presence of an exception event, we train Qwen-2.5-7B on three subcomponent-only conditions (seed 42, $N{=}1{,}190$).
334	
335	\begin{table}[t]
336	\centering
337	\caption{Exception subcomponent ablation (Qwen-2.5-7B, seed 42, $N{=}1{,}190$). All three subcomponents independently achieve ${\geq}$99.50\%. $^\dag$Retains \texttt{[ERROR]} format marker; $^\ddag$no format markers, bare exception class name only.}
338	\label{tab:exc_subcomponent}
339	\small
340	\begin{tabular}{lccc}
341	\toprule
342	\textbf{Condition} & \textbf{Acc (\%)} & \textbf{Fail R} & \textbf{Pass R} \\
343	\midrule
344	exc\_type\_only$^\dag$ & \textbf{100.00} & 100.00 & 100.00 \\
345	exc\_stacktrace\_only$^\dag$ & 99.83 & 100.00 & 99.76 \\
346	exc\_message\_only$^\ddag$ & 99.50 & 100.00 & 99.29 \\
347	\midrule
348	exception\_only (ref.) & 99.83 & 100.00 & 99.76 \\
349	\bottomrule
350	\end{tabular}
351	\end{table}
352	
353	All three subcomponents independently achieve ${\geq}$99.50\% with 100\% fail recall (Table~\ref{tab:exc_subcomponent}), showing that no single subcomponent is necessary for Tier~1 performance.
354	
355	\paragraph{Format marker confound.}
356	\texttt{exc\_type\_only} and \texttt{exc\_stacktrace\_only} retain the \texttt{[ERROR]} prefix marker present in the full \texttt{exception\_only} format; \texttt{exc\_message\_only} contains only the bare exception class name and message text without any format markers.
357	Because the marker alone is sufficient for near-perfect regex accuracy (B5: 99.33\%; \S\ref{sec:nomarker}), \texttt{exc\_type\_only} (100.00\%) and \texttt{exc\_stacktrace\_only} (99.83\%) are confounded with marker-based classification; we therefore do not make hierarchy claims among subcomponents.
358	\texttt{exc\_message\_only} (99.50\%) provides a clean test: without any format markers, it achieves accuracy comparable to the full \texttt{exception\_only} condition (99.83\%), complementing the dedicated marker-removal ablation (\texttt{nomarker}: 97.65\%; \S\ref{sec:nomarker}) as additional evidence that the model learns semantic exception patterns rather than format shortcuts.
359	
360	%% ============================================================
361	\section{Trace Length Ablation}
362	\label{sec:trace_length_full}
363	
364	To test whether the \texttt{full\_trace} performance gap is caused by input truncation at training time, we vary the maximum trace token budget on Qwen-2.5-7B (seed=42) while keeping all other hyperparameters fixed.
365	
366	\begin{table}[t]
367	\centering
368	\caption{Trace length and truncation direction ablation on Qwen-2.5-7B ($N{=}1{,}190$, seed=42). Head = standard left-truncation (retain first $k$ tokens); Tail = retain last $k$ tokens. Per-condition bootstrap 95\% CIs ($B{=}10{,}000$).}
369	\label{tab:trace_length}
370	\small
371	\begin{tabular}{llcc}
372	\toprule
373	\textbf{Direction} & \textbf{Max Tokens} & \textbf{Acc (\%)} & \textbf{95\% CI} \\
374	\midrule
375	Head & 256  & 78.82 & [76.4, 81.0] \\
376	Head & 512  & 80.42 & [78.2, 82.6] \\
377	Head & 1024 & 77.23 & [74.9, 79.6] \\
378	Head & no\_limit ($\infty$) & 81.76 & [79.7, 83.9] \\
379	\midrule
380	Tail & 256  & 77.48 & --- \\
381	Tail & 512  & 93.61 & --- \\
382	Tail & 1024 & 96.47 & --- \\
383	Tail & 2048 & 97.31 & --- \\
384	\bottomrule
385	\end{tabular}
386	\end{table}
387	
388	% Budget curve figure moved to main text (Figure~\ref{fig:budget_curve}).
389	
390	As shown in Table~\ref{tab:trace_length} and Figure~\ref{fig:budget_curve}, all four trace length conditions fall within a 5pp range (77.2\%--81.8\%).
391	To quantify the reliability of the observed differences, Table~\ref{tab:trace_length_pairwise} reports paired bootstrap comparisons ($B{=}10{,}000$, seed=42) across all condition pairs.
392	
393	\begin{table}[t]
394	\centering
395	\caption{Pairwise paired bootstrap comparisons for trace length ablation ($B{=}10{,}000$, seed=42). $\Delta$ = accuracy difference between the two conditions (first $-$ second in the budget group; condition $-$ baseline in the other groups). **$p{<}.01$; ***$p{<}.001$.}
396	\label{tab:trace_length_pairwise}
397	\small
398	\resizebox{\columnwidth}{!}{%
399	\begin{tabular}{llccc}
400	\toprule
401	& \textbf{Comparison} & \textbf{$\Delta$ (pp)} & \textbf{95\% CI} & \textbf{$p$-value} \\
402	\midrule
403	\multirow{4}{*}{\rotatebox{90}{\scriptsize Budget}}
404	& 512 vs.\ 256           & $+$1.60  & [$-$0.34, $+$3.53]   & 0.117 \\
405	& 1024 vs.\ 512          & $-$3.19  & [$-$5.29, $-$1.09]   & 0.002** \\
406	& no\_limit vs.\ 1024    & $+$4.54  & [$+$2.52, $+$6.55]   & ${<}$0.001*** \\
407	& no\_limit vs.\ 256     & $+$2.94  & [$+$0.84, $+$5.04]   & 0.006** \\
408	\midrule
409	\multirow{4}{*}{\rotatebox{90}{\scriptsize vs.\ no\_trace}}
410	& 256 $-$ no\_trace       & $+$3.70  & [$+$1.43, $+$6.05]   & 0.002** \\
411	& 512 $-$ no\_trace       & $+$5.29  & [$+$3.03, $+$7.56]   & ${<}$0.001*** \\
412	& 1024 $-$ no\_trace      & $+$2.10  & [$-$0.17, $+$4.37]   & 0.078 \\
413	& no\_limit $-$ no\_trace & $+$6.64  & [$+$4.37, $+$8.99]   & ${<}$0.001*** \\
414	\midrule
415	\multirow{4}{*}{\rotatebox{90}{\scriptsize vs.\ exc.}}
416	& 256 $-$ exc\_only       & $-$21.01 & [$-$23.45, $-$18.74] & ${<}$0.001*** \\
417	& 512 $-$ exc\_only       & $-$19.41 & [$-$21.76, $-$17.14] & ${<}$0.001*** \\
418	& 1024 $-$ exc\_only      & $-$22.61 & [$-$25.04, $-$20.25] & ${<}$0.001*** \\
419	& no\_limit $-$ exc\_only & $-$18.07 & [$-$20.34, $-$15.88] & ${<}$0.001*** \\
420	\bottomrule
421	\end{tabular}%
422	}
423	\end{table}
424	
425	\paragraph{Non-monotonic pattern (head-truncation).}
426	Under head-truncation (retaining trace prefixes), the trend is non-monotonic: 512 tokens (80.42\%) slightly outperforms 256 tokens (78.82\%), but doubling to 1024 tokens \emph{decreases} accuracy to 77.23\%, a statistically significant 3.19pp drop ($p{=}.002$, 95\% CI [$-$5.29, $-$1.09]).
427	The no-limit condition (81.76\%) recovers and significantly exceeds 1024 tokens ($p{<}.001$), but 1024 tokens is not significantly better than \texttt{no\_trace} (75.13\%; $\Delta{=}{+}2.10$pp, $p{=}.078$, 95\% CI [$-$0.17, $+$4.37]).
428	This non-monotonicity is specific to head-truncation: the 1024-token prefix retains enough irrelevant content to mislead the model while discarding diagnostic events that appear near the trace terminus.
429	Under tail-truncation, accuracy increases monotonically for Qwen-7B and Qwen-1.5B (Table~\ref{tab:tail_cross_model}); only DeepSeek-6.7B shows a mild $-$1.5pp decrease at tail-1024$\to$tail-2048, attributable to architecture-specific long-context sensitivity rather than a systematic mid-length pathology.
430	
431	\paragraph{Comparison to baselines.}
432	All four trace budget conditions significantly exceed \texttt{no\_trace} except 1024 tokens ($p{=}.078$), indicating that raw trace content provides some signal but unreliably so.
433	The gap to \texttt{exception\_only} (99.83\%) is massive for every budget condition (18--23pp, all $p{<}.001$), underscoring that even unlimited raw traces cannot substitute for targeted signal extraction.
434	The best full-trace condition (no\_limit, 81.76\%) still lags \texttt{exception\_only} by 18.07pp (95\% CI [$-$20.34, $-$15.88]).
435	
436	\paragraph{Interpretation.}
437	These results rule out input truncation as the primary explanation for the full-trace performance gap: even with unlimited tokens, the model cannot extract the diagnostic signal that VOTA's targeted compression provides.
438	The non-monotonic dip at 1024 tokens is consistent with a ``worst-of-both-worlds'' regime where the model receives enough noisy context to dilute the signal but not enough to compensate through broader coverage.
439	The result reinforces the information density interpretation (\S\ref{sec:density}): the gap between full traces and VOTA is driven by the \emph{content} of the trace (irrelevant lines diluting the diagnostic signal), not its \emph{length}.
440	In contrast, VOTA's compressed representation concentrates the diagnostic signal into fewer tokens, making it sensitive to truncation when those tokens are removed (\S\ref{sec:cross_model}).
441	
442	\paragraph{Truncation direction.}
443	Tail-truncation (retaining the last $k$ tokens) dramatically outperforms head-truncation: \texttt{tail\_2048} achieves 97.31\% vs.\ \texttt{head\_2048} (no\_limit) at 81.76\%, a 15.55pp improvement.
444	Even \texttt{tail\_512} (93.61\%) exceeds every head-truncation condition by over 11pp.
445	
446	However, \texttt{tail\_256} (77.48\%) performs at the \texttt{no\_trace} baseline level (75.13\%), indicating that the diagnostic signal does not reside in the very last trace lines.
447	The critical jump occurs between 256 and 512 tail tokens (+16.13pp), localizing the signal window to approximately 256--512 tokens from the trace terminus.
448	This is consistent with the trace format: the globals module dump consumes the first ${\sim}$384 tail tokens (pure noise), so structured execution markers (\texttt{[Line~X]} variable values) only become visible when the budget exceeds this threshold.
449	
450	The 18.07pp gap from \texttt{full\_trace} to \texttt{exception\_only} decomposes as: 86\% positional concentration (recovered by tail-truncation at 2048 tokens) and 14\% residual content noise (the 2.52pp gap from \texttt{tail\_2048} to \texttt{exception\_only} that persists regardless of truncation direction).
451	The fact that \texttt{exception\_only} (99.83\%) still outperforms \texttt{tail\_2048} (97.31\%) indicates that semantic extraction (identifying the exception type and message) is superior to positional extraction (keeping a fixed window), because the model need not filter out non-diagnostic lines that happen to fall within the window.
452	
453	\paragraph{Cross-model budget curve.}
454	Table~\ref{tab:tail_cross_model} extends the tail-truncation analysis to a full budget sweep across four models spanning three architecture families and an 8.7$\times$ parameter range.
455	
456	\begin{table}[t]
457	\centering
458	\caption{Cross-model tail-truncation budget curve ($N{=}1{,}190$). All four models exhibit a transition between tail-384 and tail-512 (+11--22pp). $\downarrow$: non-monotonic decrease. $^\dag$CodeLlama tail-384/512/1024 trained with label-only loss to address tokenizer-driven gradient dilution (\S\ref{sec:tokenizer_analysis}); tail-1024 reports best-epoch accuracy (epoch 1). CodeLlama tail entries are not directly comparable to other models (which use full-sequence loss). $^\ddag$CodeLlama tail-2048 outlier (41.8\%): LoRA long-sequence instability under label-only loss; excluded from cross-model analysis.}
459	\label{tab:tail_cross_model}
460	\small
461	\resizebox{\columnwidth}{!}{%
462	\begin{tabular}{lcccccc}
463	\toprule
464	\textbf{Model} & \textbf{tail-256} & \textbf{tail-384} & \textbf{tail-512} & \textbf{tail-1024} & \textbf{tail-2048} & \textbf{exc\_only} \\
465	\midrule
466	Qwen-7B (7B) & 77.5 & 79.9 & 93.6 & 96.5 & 97.3 & 99.83 \\
467	DeepSeek (6.7B) & 76.4 & 80.7 & 93.9 & 96.5 & 95.0$\downarrow$ & 99.33 \\
468	CodeLlama (13B) & 77.9 & 82.7$^\dag$ & 98.2$^\dag$ & 98.2$^\dag$ & 41.8$^\ddag$ & 99.89 \\
469	Qwen-1.5B (1.5B) & 72.6 & 73.6 & 95.6 & 96.6 & 97.9 & 99.83 \\
470	\bottomrule
471	\end{tabular}%
472	}
473	\end{table}
474	
475	\begin{table}[t]
476	\centering
477	\caption{Cross-model truncation direction comparison ($N{=}1{,}190$). Head-truncation retains the first 2,048 tokens; tail-truncation retains the last 2,048. All four models' head-2048 accuracies converge into a narrow 75.3--81.8\% band (6.5pp), comparable to the tail-256 signal-poor band (72.6--77.9\%, 5.3pp). $^\dag$CodeLlama tail-2048 pending retraining (\S\ref{sec:tokenizer_analysis}).}
478	\label{tab:head_vs_tail}
479	\small
480	\resizebox{\columnwidth}{!}{%
481	\begin{tabular}{lccc}
482	\toprule
483	\textbf{Model} & \textbf{head-2048 (\%)} & \textbf{tail-2048 (\%)} & \textbf{Gap (pp)} \\
484	\midrule
485	Qwen-1.5B & 75.3 & 97.9 & +22.6 \\
486	DeepSeek-6.7B & 78.7 & 95.0 & +16.3 \\
487	CodeLlama-13B & 79.9 & ---$^\dag$ & ---$^\dag$ \\
488	Qwen-7B & 81.8 & 97.3 & +15.5 \\
489	\bottomrule
490	\end{tabular}%
491	}
492	\end{table}
493	
494	Four patterns emerge from the budget curve.
495	\emph{Phase transition between 384 and 512 tokens}: the tail-384 column reveals that the transition is not instantaneous at 256$\to$512 but localized between 384 and 512 tokens.
496	At tail-384, all four models remain near baseline (73.6--80.7\%), gaining only +1.0--4.8pp over tail-256.
497	The steep jump occurs at 384$\to$512: +13.7pp (Qwen-7B), +13.2pp (DeepSeek), +15.5pp (CodeLlama), +22.0pp (Qwen-1.5B), crossing from near-baseline to near-ceiling.
498	This localizes the critical threshold to ${\sim}$400--500 tokens: below ${\sim}$384 tokens, the entire token budget is consumed by globals module dumps (pure noise); above ${\sim}$512, at least one \texttt{[Line~X]} execution event marker becomes visible, regardless of model capacity or architecture.
499	
500	\emph{Convergence at tail-512+}: once the sharp performance jump is crossed, accuracy converges across all models into a 93.6--98.2\% band at tail-512 (seed 42).
501	Multi-seed validation shows robustness: across all 12 model$\times$seed combinations at tail-512 (Table~\ref{tab:tail512_seeds}), all accuracies fall within [93.61\%, 98.24\%], a 4.63pp band that compresses the signal-poor tail-256 spread (6.3pp) by 27\%.
502	CodeLlama-13B shows perfect per-model convergence at tail-512: all three seeds achieve 98.24\% ($\sigma{=}$0), consistent with the 13B scale and label-only loss providing a stronger optimization signal in the signal-rich regime (Table~\ref{tab:tail512_seeds}).
503	However, CodeLlama's higher tail-512 accuracy may partly reflect label-only loss rather than model capacity; direct comparison with other models (which use full-sequence loss) is confounded by this training difference.
504	
505	\begin{table}[t]
506	\centering
507	\caption{Cross-seed convergence at the tail-512 truncation point ($N{=}1{,}190$ per seed). All 12 model$\times$seed combinations fall within a 4.63pp band [93.61\%, 98.24\%]. CodeLlama-13B achieves identical accuracy across all three seeds ($\sigma{=}$0).}
508	\label{tab:tail512_seeds}
509	\small
510	\resizebox{\columnwidth}{!}{%
511	\begin{tabular}{lccccr}
512	\toprule
513	\textbf{Model} & \textbf{S42} & \textbf{S123} & \textbf{S456} & \textbf{Mean} & \textbf{$\sigma$} \\
514	\midrule
515	Qwen-7B (7B)      & 93.61 & 96.00 & 97.65 & 95.75 & 2.05 \\
516	DeepSeek (6.7B)    & 93.95 & 95.04 & 96.10 & 95.03 & 1.08 \\
517	Qwen-1.5B (1.5B)  & 95.63 & 97.65 & 96.72 & 96.67 & 1.01 \\
518	CodeLlama (13B)    & 98.24 & 98.24 & 98.24 & \textbf{98.24} & \textbf{0.00} \\
519	\midrule
520	\multicolumn{4}{l}{Cross-model band} & \multicolumn{2}{r}{[93.61, 98.24] = 4.63pp} \\
521	\bottomrule
522	\end{tabular}%
523	}
524	\end{table}
525	
526	At tail-1024, four models reach 96.5--98.2\% (CodeLlama 98.2\% under label-only loss, three others 96.5--96.6\%).
527	Scale and architecture differences that dominate the signal-poor regime (tail-256 range: 72.6--77.9\%, 5.3pp) compress dramatically in the signal-rich regime.
528	
529	\emph{Signal-poor convergence band}: head-2048 accuracies across all four models also converge into a narrow 75.3--81.8\% band (6.5pp; Table~\ref{tab:head_vs_tail}), comparable in width to the tail-256 band (72.6--77.9\%, 5.3pp).
530	When the diagnostic signal is absent (head-truncation discards trace terminus) or unreachable (tail-256 is too short), models of different scale and architecture collapse to similar performance, suggesting a shared floor determined by code comprehension rather than trace processing.
531	
532	\emph{Scale behavior inversion}: in the signal-poor regime (tail-256), smaller models perform worse (Qwen-1.5B 72.6\% vs.\ Qwen-7B 77.5\%, $-$4.9pp), mirroring the \texttt{no\_trace} scale pattern.
533	In the signal-rich regime (tail-512+), this reverses: Qwen-1.5B matches or exceeds Qwen-7B (95.6\% vs.\ 93.6\% at tail-512; 97.9\% vs.\ 97.3\% at tail-2048), consistent with sufficient trace signal eliminating the capacity advantage.
534	
535	\emph{Non-monotonicity at long sequences}: two models show accuracy decreases beyond tail-1024.
536	DeepSeek-6.7B drops $-$1.5pp from tail-1024 (96.5\%) to tail-2048 (95.0\%), consistent with its known long-context sensitivity (\S\ref{sec:training_dynamics}).
537	CodeLlama-13B exhibits a more severe collapse: tail-2048 under label-only loss drops to 41.8\% (vs.\ tail-1024 = 98.2\%), which we attribute to LoRA long-sequence instability under the label-only loss regime; this outlier is excluded from cross-model tail-2048 analysis.
538	Qwen-7B and Qwen-1.5B increase monotonically across all budgets.
539	
540	Table~\ref{tab:head_vs_tail} shows the truncation direction effect: among the three models with complete data, tail-2048 outperforms head-2048 by 15.5--22.6pp.
541	The gap is largest for Qwen-1.5B (+22.6pp), indicating that smaller models benefit most from positional proximity to the diagnostic signal, as they lack the capacity to locate it within longer, noisier prefixes.
542	
543	%% ============================================================
544	\section{Calibration Analysis}
545	\label{sec:calibration_full}
546	
547	Beyond accuracy, we evaluate whether trace conditions affect prediction calibration, motivated by recent findings that code LLM confidence is often poorly calibrated \citep{spiess2025calibration}.
548	
549	\begin{table}[t]
550	\centering
551	\caption{Calibration metrics on Qwen-2.5-7B ($N{=}1{,}190$, seed=42). ECE = expected calibration error; Brier = Brier score. Lower is better for both.}
552	\label{tab:calibration}
553	\small
554	\begin{tabular}{lcc}
555	\toprule
556	\textbf{Condition} & \textbf{ECE $\downarrow$} & \textbf{Brier $\downarrow$} \\
557	\midrule
558	ae\_only & \textbf{0.0004} & \textbf{0.0008} \\
559	exception\_only & 0.0027 & 0.0013 \\
560	VOTA & 0.0054 & 0.005 \\
561	full\_trace & 0.096 & 0.144 \\
562	no\_trace & 0.171 & 0.197 \\
563	\bottomrule
564	\end{tabular}
565	\end{table}
566	
567	Table~\ref{tab:calibration} shows that calibration quality mirrors the Tier~1/2 hierarchy.
568	Tier~1 conditions (\texttt{ae\_only}: ECE=0.0004; \texttt{exception\_only}: ECE=0.0027) produce near-perfectly calibrated predictions, while \texttt{full\_trace} (ECE=0.096) and \texttt{no\_trace} (ECE=0.171) exhibit substantial miscalibration.
569	VOTA (ECE=0.0054) is well-calibrated but slightly worse than either Tier~1 component alone, reinforcing the pattern that combining trace signals dilutes rather than improves the prediction signal.
570	
571	The Brier scores tell a consistent story: \texttt{ae\_only} (0.0008) and \texttt{exception\_only} (0.0013) achieve near-zero scores, while \texttt{no\_trace} (0.197) indicates substantial miscalibration.
572	
573	\paragraph{Cross-model calibration.}
574	Table~\ref{tab:calibration_cross} extends the calibration analysis to four models (1.5B--13B) under \texttt{exception\_only}.
575	All four models achieve ECE ${<}$ 0.007 and Brier ${<}$ 0.007, indicating that calibration quality generalizes across architectures and scales.
576	CodeLlama-13B achieves the lowest ECE (0.0020) and MCE (0.0411), while DeepSeek-6.7B shows the highest ECE (0.0064) and Brier (0.0061), consistent with its higher error rate (8 errors vs.\ 2 for Qwen/CodeLlama).
577	
578	\begin{table}[t]
579	\centering
580	\caption{Cross-model calibration for \texttt{exception\_only} ($N{=}1{,}190$, seed=42). ECE = expected calibration error; Brier = Brier score; MCE = maximum calibration error. All four models (1.5B--13B) achieve ECE ${<}$ 0.007.}
581	\label{tab:calibration_cross}
582	\small
583	\begin{tabular}{lccc}
584	\toprule
585	\textbf{Model} & \textbf{ECE $\downarrow$} & \textbf{Brier $\downarrow$} & \textbf{MCE $\downarrow$} \\
586	\midrule
587	Qwen-1.5B & \textbf{0.0020} & \textbf{0.0013} & --- \\
588	CodeLlama-13B & \textbf{0.0020} & \textbf{0.0013} & \textbf{0.0411} \\
589	Qwen-7B & 0.0027 & \textbf{0.0013} & 0.8355 \\
590	DeepSeek-6.7B & 0.0064 & 0.0061 & 0.7756 \\
591	\bottomrule
592	\end{tabular}
593	\end{table}
594	
595	%% ============================================================
596	\section{Error Overlap Analysis}
597	\label{sec:error_overlap}
598	
599	We analyze the overlap between error sets of different conditions to determine whether they fail on the same samples (Figure~\ref{fig:error_overlap}).
600	
601	\texttt{exception\_only}'s 2 errors (samples 901 and 905) have zero intersection with the error sets of all other conditions (Jaccard = 0.000 in all pairwise comparisons).
602	This orthogonality arises because \texttt{exception\_only} errors are caused by \texttt{GeneratorExit} false positives (pass samples misclassified as fail due to benign \texttt{BaseException} events), while errors from other conditions are predominantly fail samples misclassified as pass due to insufficient signal.
603	
604	Among non-exception conditions, error sets exhibit hierarchical containment: \texttt{ae\_only} $\subset$ VOTA $\subset$ \texttt{loop\_only} $\subset$ \texttt{no\_trace}, with pairwise Jaccard indices increasing with signal overlap.
605	\texttt{loop\_only} and \texttt{full\_trace} share the highest overlap (Jaccard ${\sim}$0.65), reflecting their shared reliance on behavioral patterns rather than explicit fault indicators.
606	
607	This analysis indicates that \texttt{exception\_only} operates on an independent signal dimension: its errors are representation ambiguities (iterator protocol artifacts) rather than information deficits, explaining why combining it with other signals cannot eliminate these specific errors.
608	
609	\begin{figure}[t]
610	\centering
611	\includegraphics[width=\columnwidth]{error_overlap}
612	\caption{Jaccard similarity between error sets of different conditions (Qwen-7B, seed=42, $N{=}1{,}190$). \texttt{exception\_only} (exc\_only) has zero overlap with all other conditions, indicating it operates on an independent signal dimension.}
613	\label{fig:error_overlap}
614	\end{figure}
615	
616	%% ============================================================
617	\section{Cross-Dataset Generalization: DebugBench}
618	\label{sec:debugbench_full}
619	
620	To test whether exception-based verdict prediction generalizes beyond LLM-generated solutions, we evaluate on DebugBench \citep{tian2024debugbench}, a dataset of human-written programs with synthetically injected bugs (single-point mutations such as operator replacement, variable misuse, and missing statements).
621	After filtering for executable Python samples with valid traces, we retain 426 samples with a near-balanced class distribution (majority baseline: 51.4\%).
622	
623	\begin{table}[t]
624	\centering
625	\caption{Generalization to DebugBench ($N{=}426$, Qwen-2.5-7B, seed=42). Wilson 95\% CIs. The component ranking (exception\_only $\geq$ VOTA $>$ no\_trace) is preserved, and exception\_only achieves perfect accuracy.}
626	\label{tab:debugbench}
627	\small
628	\begin{tabular}{lcc}
629	\toprule
630	\textbf{Condition} & \textbf{Acc (\%)} & \textbf{95\% CI} \\
631	\midrule
632	exception\_only & \textbf{100.00} & [99.14, 100.00] \\
633	VOTA & 99.77 & [99.30, 100.00] \\
634	no\_trace & 96.71 & [94.80, 98.40] \\
635	\midrule
636	Majority baseline & 51.41 & --- \\
637	\bottomrule
638	\end{tabular}
639	\end{table}
640	
641	Table~\ref{tab:debugbench} shows that the component ranking from the main experiments is preserved: \texttt{exception\_only} (100.00\%) $\geq$ VOTA (99.77\%) $>$ \texttt{no\_trace} (96.71\%).
642	The \texttt{exception\_only} condition achieves perfect accuracy, showing that the exception-based representation generalizes to a different fault distribution without degradation.
643	
644	The absolute margins are much narrower than on the main dataset: the \texttt{no\_trace} baseline already achieves 96.71\% (compared to 75.13\% on HumanEval+MBPP), leaving only 3.29pp of headroom for trace-based improvement.
645	This ceiling effect reflects a fundamental difference in fault characteristics: DebugBench bugs are synthetically injected single-point mutations, which produce code that is structurally dissimilar from the original correct solution; a model can often identify the fault from source code alone.
646	In contrast, the HumanEval+MBPP solutions are LLM-generated, producing natural errors (logic mistakes, edge-case failures) where the faulty and correct solutions may be structurally similar, making code-only verdict prediction substantially harder.
647	
648	These results support exception-based verdict prediction as a generalizable approach: the method does not degrade on an out-of-distribution dataset, and the exception dominance ranking (exception\_only $\geq$ VOTA $>$ no\_trace) is consistent across both datasets. However, the narrow DebugBench margins are insufficient to independently validate trace importance.
649	The 24.70pp trace lift on the main dataset (no\_trace 75.13\% $\to$ exception\_only 99.83\%) remains the primary evidence for the value of exception-based trace signals.
650	
651	%% ============================================================
652	\section{Cross-Model Robustness Analysis}
653	\label{sec:robustness_analysis}
654	
655	The cross-model gap pattern (Table~\ref{tab:cross_model}) suggests a design principle: \emph{trace representations should match the model capability floor, not the ceiling.}
656	Exception events are consistently the most effective component on both models, and their structural simplicity (a fixed-format error message) ensures that the relative advantage over richer representations holds across all seeds.
657	All three DeepSeek \texttt{exception\_only} seeds achieve ${\geq}$99.33\% (99.33/99.50/99.33, $\sigma{=}$0.10pp), matching Qwen and CodeLlama at ${\geq}$99.83\%.
658	VOTA achieves ${\geq}$98.57\% across all models when excluding outlier seeds (cross-model range: 0.80pp), but DeepSeek VOTA exhibits seed-dependent instability: seed 42 (84.45\%) is a training failure due to tokenizer-induced truncation (91.7\% of training samples affected), while seeds 123/456 (99.16\%/99.33\%) match cross-model performance.
659	This VOTA instability is confounded by tokenizer efficiency and base model differences \citep{yang2024generalization}.
660	Our \texttt{exception\_only} design sidesteps the truncation confound entirely: inputs have a median of 150 tokens (mean 398), well below the 2{,}048-token context window, so no training samples are truncated on either model.
661	The resulting 0.50pp cross-model gap (Table~\ref{tab:cross_model}) is therefore a clean measure of model capability differences, making the ``capability floor'' principle directly testable.
662	The practical implication is that trace-based systems should default to the simplest sufficient signal.
663	
664	%% ============================================================
665	\section{Training Dynamics and Loss Decoupling}
666	\label{sec:training_dynamics}
667	
668	The DeepSeek \texttt{exception\_only} results are consistent across all three seeds (99.33/99.50/99.33, $\sigma{=}$0.10pp), matching Qwen's cross-seed stability.
669	Epoch-level analysis shows mild degradation in seed 42: accuracy peaks at 99.83\% after epoch~1 but settles at 99.33\% by epoch~3 ($-$0.50pp), while seed 456 shows no degradation (99.33\% at both epochs).
670	Early stopping may yield marginal gains, but the epoch effect is small (${\leq}$0.5pp).
671	The practical recommendation: for deployment, use task-specific metrics (accuracy, fail recall) for checkpoint and seed selection rather than training loss, and train multiple seeds to select the best.
672	
673	The contrast with VOTA is instructive: DeepSeek VOTA seed 42 accuracy monotonically increases from 78.15\% to 84.45\% across epochs, consistent with a performance limit from high trace truncation (91.7\% of samples; \S\ref{sec:tokenizer_analysis}).
674	Seeds 123/456, which avoid the truncation-sensitive initialization basin, achieve 99.16\%/99.33\%, indicating that the deficit is seed-specific rather than a fundamental model limitation.
675	
676	%% ============================================================
677	\section{Deduplication Statistics}
678	\label{sec:dedup_stats}
679	
680	Table~\ref{tab:dedup} reports the duplication rates across trace formats.
681	Because multiple passing solutions to the same problem produce identical (input, output) pairs in the \texttt{exception\_only} format (correct executions raise no exceptions, so the trace content is the same regardless of the solution's internal logic), the dataset contains duplicate rows.
682	Train--test input overlap is zero (split by problem ID), so no information leakage occurs.
683	The high duplication in \texttt{exception\_only} does not affect our experimental conclusions: after deduplication the training set still contains 2,858 unique samples and the test set 607, providing sufficient coverage for the 591-problem benchmark.
684	
685	\paragraph{Problem-level partitioning and sensitivity analysis.}
686	Data is partitioned at the problem level: 472 training problems and 119 test problems, with zero crossover.
687	Duplicates arise from multiple candidate solutions per problem (up to 10 solutions each), not from cross-problem overlap.
688	To verify that deduplication does not alter any finding, we ran a sensitivity analysis across all 19 experimental conditions (7 trace formats $\times$ 4 models, minus conditions not run): deduplication produces a negligible ($<$0.1pp) accuracy delta in every case.
689	This shows that duplicate samples neither inflate nor deflate accuracy, because duplicates share the same ground-truth label and the model's prediction is deterministic at inference time.
690	Duplicates arise because the \texttt{exception\_only} format collapses passing solutions (which share identical ``no exception'' output) into identical rows; the redundancy is a property of the format's compactness for pass-class samples.
691	The \texttt{exception\_only} test set contains 48.99\% such duplicates; all confidence intervals treat samples as independent Bernoulli trials.
692	
693	\begin{table}[t]
694	\centering
695	\caption{Deduplication statistics. The \texttt{exception\_only} format collapses multiple passing solutions into identical rows because correct executions produce no exception events. Train--test input overlap is 0 (no leakage).}
696	\label{tab:dedup}
697	\small
698	\begin{tabular}{lccc}
699	\toprule
700	\textbf{Split} & \textbf{Total} & \textbf{Unique} & \textbf{Dup.\ rate} \\
701	\midrule
702	exception\_only train & 4{,}720 & 2{,}858 & 39.45\% \\
703	exception\_only test  & 1{,}190 &   607 & 48.99\% \\
704	raw\_traces (full)    & 5{,}910 & 5{,}803 &  1.81\% \\
705	\bottomrule
706	\end{tabular}
707	\end{table}
708	
709	%% ============================================================
710	\section{Regex Baseline Analysis}
711	\label{sec:regex_baselines}
712	
713	To establish a non-learning upper bound, we evaluate six regex-based baselines on the \texttt{exception\_only} test set ($N{=}1{,}190$) and two format-specific baselines on VOTA and \texttt{full\_trace} inputs.
714	
715	\begin{table}[t]
716	\centering
717	\caption{Regex baseline accuracy ($N{=}1{,}190$). B4 is the strongest semantic baseline (6.22pp below SFT \texttt{exception\_only}, McNemar $p{<}.001$). B6 uses an error count threshold. $^\ddag$B5 exploits a data formatting artifact: the \texttt{[No exception data in trace]} marker is deterministically present in all pass samples, making this a format-level shortcut rather than a genuine exception-based heuristic.}
718	\label{tab:regex}
719	\small
720	\resizebox{\columnwidth}{!}{%
721	\begin{tabular}{llc}
722	\toprule
723	\textbf{Baseline} & \textbf{Method} & \textbf{Acc (\%)} \\
724	\midrule
725	B1: \texttt{[ERROR]} presence & string match & 93.45 \\
726	B2: Traceback presence & string match & 71.51 \\
727	B3: Any keyword & union of B1+B2+Exception & 93.45 \\
728	B4: Exception type regex & regex on exception class names & \textbf{93.61} \\
729	B5: Format marker & \texttt{[No exception data]} $\to$ pass & 99.33$^\ddag$ \\
730	B6: Error count $\geq$2 & count threshold & 92.02 \\
731	\midrule
732	VOTA format regex & best regex on VOTA traces & 75.55 \\
733	full\_trace format regex & best regex on full traces & 77.39 \\
734	\bottomrule
735	\end{tabular}%
736	}
737	\end{table}
738	
739	The strongest legitimate baseline (B4, 93.61\%) applies regex pattern-matching on Python exception class names (e.g., \texttt{ValueError}, \texttt{TypeError}).
740	Its errors concentrate on 8 boundary samples where a \texttt{ValueError} is raised inside a \texttt{try/except} block and caught; the program passes despite an exception occurring in the trace.
741	SFT \texttt{exception\_only} correctly classifies 6 of these 8 samples, indicating that the model learns the semantic distinction between caught (benign) and uncaught (fault-indicating) exceptions.
742	B5 (99.33\%) achieves near-SFT accuracy but relies on the deterministic presence of a format marker in pass-class traces, which is an artifact of the trace preprocessing pipeline rather than a generalizable signal; McNemar test vs.\ SFT yields $p{=}.041$, indicating a statistically significant difference.
743	
744	\paragraph{Cross-format comparison.}
745	Table~\ref{tab:regex_cross_format} compares SFT and the best applicable regex baseline for each trace format.
746	The SFT advantage increases with format complexity: \texttt{no\_trace} (+3.62pp over majority baseline) $<$ \texttt{full\_trace} (+4.37pp) $<$ \texttt{exception\_only} (+6.22pp) $\ll$ VOTA (+23.86pp).
747	The VOTA gap is largest because its structured multi-component format carries semantic content that regex cannot parse, while \texttt{exception\_only}'s simpler format allows regex to capture most of the signal.
748	
749	\begin{table}[t]
750	\centering
751	\caption{SFT vs.\ best regex baseline by trace format ($N{=}1{,}190$). Regex baselines: majority class for \texttt{no\_trace}, keyword matching for \texttt{full\_trace}, pattern matching for VOTA, exception type regex (B4) for \texttt{exception\_only}.}
752	\label{tab:regex_cross_format}
753	\small
754	\begin{tabular}{lccc}
755	\toprule
756	\textbf{Format} & \textbf{SFT (\%)} & \textbf{Regex (\%)} & \textbf{$\Delta$ (pp)} \\
757	\midrule
758	exception\_only & 99.83 & 93.61 & +6.22 \\
759	VOTA & 99.41 & 75.55 & +23.86 \\
760	full\_trace & 81.76 & 77.39 & +4.37 \\
761	no\_trace & 75.13 & 71.51 & +3.62 \\
762	\bottomrule
763	\end{tabular}
764	\end{table}
765	
766	%% ============================================================
767	\section{Cross-Model Zero-Shot Comparison}
768	\label{sec:zeroshot_cross_model}
769	
770	Table~\ref{tab:zeroshot_cross_model} compares zero-shot and SFT \texttt{exception\_only} accuracy across four models.
771	Zero-shot performance does not correlate with model size: the smallest model (Qwen-1.5B, 93.45\%) outperforms all larger models, while the largest (CodeLlama-13B) falls below majority baseline.
772	SFT compresses the 42.44pp zero-shot range to 0.50pp, eliminating architecture-dependent variance.
773	
774	\begin{table}[t]
775	\centering
776	\caption{Zero-shot vs.\ SFT \texttt{exception\_only} across four models ($N{=}1{,}190$). Zero-shot accuracy is uncorrelated with model size; SFT normalizes cross-architecture variance from 42.44pp to 0.50pp.}
777	\label{tab:zeroshot_cross_model}
778	\small
779	\resizebox{\columnwidth}{!}{%
780	\begin{tabular}{llccc}
781	\toprule
782	\textbf{Model} & \textbf{Size} & \textbf{Zero-shot (\%)} & \textbf{SFT (\%)} & \textbf{$\Delta$ (pp)} \\
783	\midrule
784	Qwen-1.5B & 1.5B & 93.45 & 99.83 & +6.38 \\
785	DeepSeek-6.7B & 6.7B & 90.59 & 99.39 & +8.80 \\
786	Qwen-7B & 7B & 89.08 & 99.83 & +10.75 \\
787	CodeLlama-13B & 13B & 51.01 & 99.89 & +48.88 \\
788	\midrule
789	Range & --- & 42.44pp & 0.50pp & --- \\
790	\bottomrule
791	\end{tabular}%
792	}
793	\end{table}
794	
795	% Calibration table removed (redundant with Table~\ref{tab:calibration_cross} in \S\ref{sec:calibration_full}).
796	
797	%% ============================================================
798	\section{Use of AI Assistants}
799	\label{app:ai-assistants}
800	
801	We used Claude (Anthropic) as an AI coding and writing assistant
802	throughout this work. Specifically:
803	\begin{itemize}
804	    \item \textbf{Code:} drafting experiment scripts, data-processing
805	    pipelines, and analysis utilities; debugging and refactoring.
806	    \item \textbf{Writing:} drafting and revising paper sections,
807	    polishing prose, and reformatting LaTeX.
808	    \item \textbf{Literature:} summarizing related papers to inform
809	    the related-work section.
810	\end{itemize}
811	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e58add99-562e-49f5-aa3c-19363fa0ae30",
  "isSidechain": false,
  "promptId": "96f110f9-4fbd-4295-8cdb-ef5a8ad15d7a",
  "type": "user",
  "uuid": "d048693d-ce61-4c45-9a7b-d28a38732dab",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/appendix.tex",
      "content": "\\section{Per-Class Performance Breakdown}\n\\label{sec:per_class}\n\nTable~\\ref{tab:per_class} reports per-class precision, recall, and F1 for all experimental conditions.\n\n\\begin{table*}[t]\n\\centering\n\\caption{Per-class precision, recall, and F1 for all experimental conditions (seed 42). DeepSeek VOTA seed 42 is a training failure (84.45\\%, fail recall = 45.4\\%) due to tokenizer-driven truncation; seeds 123/456 achieve 99.16\\%/99.33\\%.}\n\\label{tab:per_class}\n\\small\n\\begin{tabular}{llccccccc}\n\\toprule\n\\textbf{Condition} & \\textbf{Model} & \\textbf{Acc} & \\textbf{Pass P} & \\textbf{Pass R} & \\textbf{Pass F1} & \\textbf{Fail P} & \\textbf{Fail R} & \\textbf{Fail F1} \\\\\n\\midrule\nNo Trace          & Qwen-2.5-7B & 75.13 & 87.76 & 75.79 & 81.34 & 54.73 & 73.45 & 62.72 \\\\\nFull Trace        & Qwen-2.5-7B & 81.76 & 87.74 & 86.60 & 87.17 & 67.43 & 69.62 & 68.51 \\\\\nFull Trace (LO)   & Qwen-2.5-7B & 86.22 & 88.21 & 93.18 & 90.63 & 80.07 & 68.73 & 73.97 \\\\\nVOTA              & Qwen-2.5-7B & 99.41 & 100.00 & 99.18 & 99.59 & 97.98 & 100.00 & 98.98 \\\\\nException Only    & Qwen-2.5-7B & 99.83 & 100.00 & 99.76 & 99.88 & 99.41 & 100.00 & 99.71 \\\\\nAE Only           & Qwen-2.5-7B & 99.92 & 100.00 & 99.88 & 99.94 & 99.71 & 100.00 & 99.85 \\\\\nLoop Only         & Qwen-2.5-7B & 85.63 & 92.39 & 87.07 & 89.66 & 71.65 & 82.01 & 76.48 \\\\\nVOTA\\_no\\_ae       & Qwen-2.5-7B & 99.41 & 99.88 & 99.29 & 99.59 & 98.26 & 99.71 & 98.98 \\\\\n\\midrule\nNo Trace          & DeepSeek-6.7B & 73.36 & 81.71 & 80.85 & 81.28 & 53.16 & 54.57 & 53.86 \\\\\nFull Trace        & DeepSeek-6.7B & 79.16 & 85.70 & 85.10 & 85.40 & 63.20 & 64.30 & 63.70 \\\\\nVOTA              & DeepSeek-6.7B & 84.45 & 82.14 & 100.00 & 90.20 & 100.00 & 45.40 & 62.50 \\\\\nException Only    & DeepSeek-6.7B & 99.33 & 100.00 & 99.06 & 99.53 & 97.69 & 100.00 & 98.83 \\\\\nAE Only           & DeepSeek-6.7B & 98.74 & 98.40 & 99.90 & 99.10 & 99.70 & 95.90 & 97.70 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\n%% ============================================================\n\\section{Training Details}\n\\label{sec:training_details}\n\nTable~\\ref{tab:hyperparams} summarizes the training hyperparameters shared across all conditions.\nAll experiments use the HuggingFace TRL \\texttt{SFTTrainer} with LoRA \\citep{hu2022lora} applied to all linear layers.\n\n\\begin{table}[t]\n\\centering\n\\caption{Training hyperparameters (shared across all conditions).}\n\\label{tab:hyperparams}\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{ll}\n\\toprule\n\\textbf{Hyperparameter} & \\textbf{Value} \\\\\n\\midrule\nLoRA rank ($r$)            & 16 \\\\\nLoRA alpha ($\\alpha$)      & 32 \\\\\nLoRA dropout               & 0.05 \\\\\nLoRA target modules        & all linear layers \\\\\n\\midrule\nEpochs                     & 3 \\\\\nPer-device batch size       & 4 \\\\\nGradient accumulation steps & 8 \\\\\nEffective batch size        & 32 \\\\\n\\midrule\nLearning rate               & $2 \\times 10^{-4}$ \\\\\nLR scheduler                & linear decay \\\\\nWarmup ratio                & 0.1 \\\\\nWeight decay                & 0.01 \\\\\n\\midrule\nMax sequence length         & 2048 tokens \\\\\nPrimary seed                & 42 \\\\\nRobustness seeds            & 123, 456 \\\\\n\\midrule\nHardware                    & 1$\\times$ enterprise-grade GPU (${\\geq}$80\\,GB VRAM) \\\\\nFramework                   & HuggingFace TRL SFTTrainer \\\\\n\\bottomrule\n\\end{tabular}%\n}\n\\end{table}\n\nTable~\\ref{tab:train_time} reports per-condition training wall-clock times.\nConditions with longer trace inputs (e.g., \\texttt{full\\_trace}, VOTA) require proportionally more training time due to increased sequence lengths.\n\n\\begin{table}[t]\n\\centering\n\\caption{Training wall-clock time per condition on a single enterprise-grade GPU (${\\geq}$80\\,GB VRAM). Where multiple seeds were run, individual times are listed.}\n\\label{tab:train_time}\n\\small\n\\begin{tabular}{llr}\n\\toprule\n\\textbf{Condition} & \\textbf{Seed(s)} & \\textbf{Time (h)} \\\\\n\\midrule\nno\\_trace       & 42         & ${\\sim}$0.5 \\\\\nfull\\_trace     & 42         & ${\\sim}$2.2 \\\\\nlabel\\_only     & 42         & ${\\sim}$2.2 \\\\\nVOTA                     & 42         & ${\\sim}$2.3 \\\\\nexception\\_only & 42         & ${\\sim}$2.1 \\\\\nexception\\_only & 123        & ${\\sim}$2.1 \\\\\nexception\\_only & 456        & ${\\sim}$1.3 \\\\\nae\\_only        & 42         & ${\\sim}$1.8 \\\\\nloop\\_only      & 42         & ${\\sim}$2.1 \\\\\nVOTA\\_no\\_ae    & 42         & ${\\sim}$1.8 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n%% ============================================================\n\\section{VOTA Extraction Algorithm}\n\\label{sec:vota_algorithm}\n\nAlgorithm~\\ref{alg:vota} describes the three-component VOTA extraction pipeline applied to a raw \\texttt{sys.settrace} execution log.\n\n\\begin{algorithm}[t]\n\\caption{VOTA Trace Extraction}\n\\label{alg:vota}\n\\small\n\\begin{algorithmic}[1]\n\\REQUIRE Raw trace $T$ from \\texttt{sys.settrace} (list of events)\n\\ENSURE Compressed VOTA representation $V$\n\\STATE $V \\leftarrow$ empty string\n\\STATE \\textbf{// Component 1: Exception summary}\n\\FOR{each event $e$ in $T$ with type \\texttt{exception}}\n  \\STATE Parse traceback $\\rightarrow$ extract error type, message, file, line\n  \\STATE Append \\texttt{[ERROR] type: message (file:line)} to $V$\n\\ENDFOR\n\\IF{no exception events found}\n  \\STATE Append \\texttt{[No exception data in trace]} to $V$\n\\ENDIF\n\\STATE \\textbf{// Component 2: Assertion-point comparison}\n\\FOR{each \\texttt{assert} or \\texttt{return} event $e$ in $T$}\n  \\STATE Extract actual value from execution state\n  \\STATE Extract expected value from test assertion\n  \\STATE Append \\texttt{[ASSERT] actual=... expected=... match=T/F} to $V$\n\\ENDFOR\n\\STATE \\textbf{// Component 3: Loop compression}\n\\FOR{each consecutive repeated line sequence $S$ in $T$}\n  \\IF{$|S| \\geq 2$ iterations of same loop body}\n    \\STATE Replace $S$ with single iteration + \\texttt{[repeated $\\times$N]}\n  \\ENDIF\n\\ENDFOR\n\\STATE Append compressed non-exception lines to $V$\n\\RETURN $V$\n\\end{algorithmic}\n\\end{algorithm}\n\n%% ============================================================\n\\section{VOTA Trace Examples}\n\\label{sec:vota_examples}\n\nWe provide two representative VOTA trace examples illustrating the fail and pass cases.\nIn the fail case, the exception event provides an unambiguous fault signal.\nIn the pass case, the absence of an exception event combined with a matching assertion point confirms correct execution.\n\n\\paragraph{Fail example.}\nA \\texttt{ZeroDivisionError} triggers an \\texttt{[ERROR]} event, providing a direct fault signal that is sufficient for the model to predict \\texttt{fail}.\n\n\\begin{scriptsize}\n\\begin{verbatim}\n## Function\ndef divide(a, b):\n    return a / b\n\n## Test Input\ndivide(1, 0)\n\n## Expected Output\ninf\n\n## VOTA Trace\n[ERROR] ZeroDivisionError: division by zero\n\n## Verdict\nfail\n\\end{verbatim}\n\\end{scriptsize}\n\n\\paragraph{Pass example.}\nNo exception is raised, and the assertion point confirms that the actual output matches the expected value.\n\n\\begin{scriptsize}\n\\begin{verbatim}\n## Function\ndef add(a, b):\n    return a + b\n\n## Test Input\nadd(2, 3)\n\n## Expected Output\n5\n\n## VOTA Trace\n[LOOP] No loops detected.\n[ASSERT] actual=5, expected=5\n\n## Verdict\npass\n\\end{verbatim}\n\\end{scriptsize}\n\nThese examples illustrate the core asymmetry exploited by the \\texttt{exception\\_only} condition: fail cases produce an explicit \\texttt{[ERROR]} event, while pass cases are characterized by its absence.\nThis binary signal (presence vs.\\ absence of an exception) is sufficient for near-perfect verdict prediction.\n\n%% ============================================================\n\\section{Full Experimental Results}\n\\label{sec:full_results}\n\nTables~\\ref{tab:full_qwen} and \\ref{tab:full_deepseek} report the complete experimental results across all conditions, models, and seeds.\n\n\\begin{table}[t]\n\\centering\n\\caption{Full results for Qwen-2.5-Coder-7B across all conditions and seeds. Conditions with a single seed report no variance. \\texttt{exception\\_only} achieves 99.83\\% across all three seeds ($\\sigma{=}$0). \\texttt{ae\\_only} achieves 99.64\\% mean ($\\pm$0.49; seed 123 at 99.08\\% is the outlier).}\n\\label{tab:full_qwen}\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Condition} & \\textbf{S42} & \\textbf{S123} & \\textbf{S456} & \\textbf{Mean $\\pm$ Std} \\\\\n\\midrule\nexception\\_only & 99.83 & 99.83 & 99.83 & 99.83 $\\pm$ 0.00 \\\\\nae\\_only        & 99.92 & 99.08 & 99.92 & 99.64 $\\pm$ 0.49 \\\\\nVOTA                     & 99.41 & 98.66 & 99.08 & 99.05 $\\pm$ 0.38 \\\\\nVOTA\\_no\\_ae    & 99.41 & ---   & ---   & --- \\\\\nlabel\\_only     & 86.22 & 86.89 & 84.70 & 85.94 $\\pm$ 1.12 \\\\\nloop\\_only      & 85.63 & 85.88 & 86.64 & 86.05 $\\pm$ 0.52 \\\\\nfull\\_trace     & 81.76 & 80.20 & 82.35 & 81.44 $\\pm$ 1.11 \\\\\nno\\_trace       & 75.13 & ---   & ---   & --- \\\\\n\\bottomrule\n\\end{tabular}%\n}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\caption{Full results for DeepSeek-Coder-6.7B across all conditions and seeds. \\texttt{exception\\_only} is consistent across seeds: 99.33/99.50/99.33 ($\\sigma{=}$0.10pp).}\n\\label{tab:full_deepseek}\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llcc}\n\\toprule\n\\textbf{Condition} & \\textbf{Seed} & \\textbf{Accuracy} & \\textbf{Notes} \\\\\n\\midrule\nexception\\_only & 42  & 99.33 & epoch 1: 99.83 \\\\\nexception\\_only & 456 & 99.33 & CI [98.82, 99.75] \\\\\nexception\\_only & 123 & 99.50 & \\\\\n\\midrule\nVOTA                     & 42  & 84.45 & training failure; fail recall = 45.4\\% \\\\\nVOTA                     & 123 & 99.16 & \\\\\nVOTA                     & 456 & 99.33 & \\\\\nno\\_trace       & 42  & 73.36 & \\\\\nfull\\_trace     & 42  & 79.16 & CI [76.80, 81.30] \\\\\n\\bottomrule\n\\end{tabular}%\n}\n\\end{table}\n\n%% ============================================================\n\\section{Tokenizer and Truncation Analysis}\n\\label{sec:tokenizer_analysis}\n\nDeepSeek VOTA seed 42 (84.45\\%) is a training failure driven by tokenizer-induced truncation.\nRe-evaluation of the seed 42 checkpoint with the standard max\\_length=2048 yields 16\\% accuracy, consistent with complete model collapse rather than marginal degradation.\nThe previously reported 84.45\\% was obtained with max\\_length=16384, which partially bypasses tokenizer truncation.\nSeeds 123 and 456, evaluated under identical conditions, achieve 99.16\\% and 99.33\\% respectively.\nThe DeepSeek tokenizer averages 2{,}626 tokens per VOTA sample versus 1{,}929 for Qwen, causing 91.7\\% of DeepSeek VOTA training samples to exceed the 2{,}048-token context window.\nThe training framework preserves the verdict label but truncates trace content, so the model trains with incomplete diagnostic information for the majority of samples.\nSeeds 123 and 456 (99.16\\% and 99.33\\%) demonstrate that DeepSeek can learn VOTA when LoRA initialization avoids the truncation-sensitive basin; the 2-seed mean (99.25\\%$\\pm$0.12) matches the cross-model VOTA range (98.74--99.54\\%).\n\nA post-hoc group analysis on seed 42 provides directional evidence: partitioning test samples by whether their training-set counterparts exceeded the context window, intact samples ($N{=}99$) achieve 100\\% accuracy while truncated samples ($N{=}1{,}091$) achieve 83.04\\% (95\\% CI [80.75\\%, 85.24\\%]; Fisher exact $p{<}.001$), with all 185 errors concentrated in the fail class (fail recall = 31.23\\%).\nPer-class analysis (Table~\\ref{tab:per_class}) shows that seed 42 achieves 100\\% fail precision but only 45.43\\% fail recall, systematically defaulting to \\texttt{pass}.\n\nSeed robustness is consistent across models: Qwen \\texttt{exception\\_only} produces identical 99.83\\% across all three seeds ($\\sigma{=}0$), and DeepSeek achieves 99.39\\%$\\pm$0.10 (seeds 42/456: 99.33\\%, seed 123: 99.50\\%).\nBecause \\texttt{exception\\_only} test inputs contain 48.99\\% duplicates (607 unique of 1,190; \\S\\ref{sec:dataset}), CIs assume $n{=}1{,}190$ independent trials; under deduplication ($n{=}607$), Qwen's accuracy is 99.67\\% (Wilson CI [98.81, 99.91]).\n\n%% ============================================================\n\\section{Persistent Error Analysis}\n\\label{sec:irreducible}\n\nThe \\texttt{exception\\_only} condition with Qwen-2.5-Coder-7B misclassifies exactly 2 out of 1,190 test samples across all three seeds (42, 123, 456), with 100\\% overlap across seeds.\nBoth samples (IDs 901 and 905) share the following characteristics:\n\n\\begin{itemize}\n\\item \\textbf{Function:} \\texttt{check\\_dict\\_case} (HumanEval/95), a function that checks whether all dictionary keys are uniformly upper-case or lower-case strings.\n\\item \\textbf{Ground-truth label:} \\texttt{pass}.\n\\item \\textbf{Predicted label:} \\texttt{fail} (false negative).\n\\item \\textbf{Cross-seed consistency:} Both samples are misclassified identically by all three seeds, indicating a systematic rather than stochastic error.\n\\end{itemize}\n\nManual inspection reveals the root cause: \\texttt{check\\_dict\\_case} uses \\texttt{all()} over a generator expression, and Python's \\texttt{all()} short-circuits on the first \\texttt{True} value, raising \\texttt{GeneratorExit} to terminate the generator.\nBecause \\texttt{GeneratorExit} is a \\texttt{BaseException} subclass, the tracer records it as seven \\texttt{[ERROR] GeneratorExit} lines, even though the function executes correctly and the test passes.\nThe model observes these spurious error markers and reasonably but incorrectly predicts \\texttt{fail}.\nThis is not a model failure but a representation ambiguity: the \\texttt{exception\\_only} format cannot distinguish genuine exceptions from benign \\texttt{BaseException} subclasses triggered by Python's iterator protocol.\n\nMost configurations converge to these same 2 errors: Qwen-1.5B, Qwen-7B (3 seeds), CodeLlama-13B (seeds 42/456), and DeepSeek-6.7B (seeds 42/456) all produce error set $\\{901, 905\\}$.\nHowever, CodeLlama-13B seed 123 achieves 100\\% accuracy (0/1190 errors), correctly classifying both samples.\nThis demonstrates that 99.83\\% is a near-perfect \\emph{floor} (the convergence attractor for most LoRA initializations) rather than a hard data ceiling: the representation supports perfect accuracy, but most initializations converge to the same 2-error basin.\nThe practical implication is that these errors are high-probability convergence artifacts addressable through seed selection or ensemble methods, not fundamental limitations of the exception-based representation.\n\n%% ============================================================\n\\section{Exception Type Accuracy Breakdown}\n\\label{sec:exception_type}\n\nTable~\\ref{tab:exception_type} reports \\texttt{exception\\_only} accuracy stratified by exception type on Qwen-2.5-7B (seed=42, $N{=}1{,}190$).\nAll standard exception types (\\texttt{TypeError}, \\texttt{ValueError}, \\texttt{IndexError}, etc.) achieve 100\\% accuracy.\nThe only misclassifications arise from \\texttt{GeneratorExit}, a \\texttt{BaseException} subclass that is not an \\texttt{Exception}. It is raised by Python's iterator protocol during generator short-circuiting, not by actual program errors.\n\n\\begin{table}[t]\n\\centering\n\\caption{Exception type accuracy breakdown for \\texttt{exception\\_only} (Qwen-7B, seed=42). All true error types achieve 100\\%. The only failures come from \\texttt{GeneratorExit} (a \\texttt{BaseException} subclass, not an \\texttt{Exception}), which appears in 2 passing samples.}\n\\label{tab:exception_type}\n\\small\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Exception Type} & \\textbf{Samples} & \\textbf{Accuracy} \\\\\n\\midrule\nTypeError & 96 & 100\\% \\\\\nValueError & 62 & 100\\% \\\\\nIndexError & 41 & 100\\% \\\\\nKeyError & 28 & 100\\% \\\\\nAttributeError & 19 & 100\\% \\\\\nAssertionError & 15 & 100\\% \\\\\nRecursionError & 12 & 100\\% \\\\\nOther Exception & 66 & 100\\% \\\\\n\\midrule\nGeneratorExit (BaseException) & 2 & 0\\% \\\\\nNo exception (pass class) & 849 & 100\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThis is consistent with the model having learned a clean decision boundary: any true \\texttt{Exception} subclass in the trace implies failure.\nThe \\texttt{GeneratorExit} case represents a semantic ambiguity in the trace format rather than a model failure, as discussed in \\S\\ref{sec:irreducible}.\n\n%% ============================================================\n\\section{Exception Subcomponent Ablation}\n\\label{sec:exc_subcomponent}\n\nTo test whether verdict prediction depends on a specific exception subcomponent or merely the binary presence of an exception event, we train Qwen-2.5-7B on three subcomponent-only conditions (seed 42, $N{=}1{,}190$).\n\n\\begin{table}[t]\n\\centering\n\\caption{Exception subcomponent ablation (Qwen-2.5-7B, seed 42, $N{=}1{,}190$). All three subcomponents independently achieve ${\\geq}$99.50\\%. $^\\dag$Retains \\texttt{[ERROR]} format marker; $^\\ddag$no format markers, bare exception class name only.}\n\\label{tab:exc_subcomponent}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Condition} & \\textbf{Acc (\\%)} & \\textbf{Fail R} & \\textbf{Pass R} \\\\\n\\midrule\nexc\\_type\\_only$^\\dag$ & \\textbf{100.00} & 100.00 & 100.00 \\\\\nexc\\_stacktrace\\_only$^\\dag$ & 99.83 & 100.00 & 99.76 \\\\\nexc\\_message\\_only$^\\ddag$ & 99.50 & 100.00 & 99.29 \\\\\n\\midrule\nexception\\_only (ref.) & 99.83 & 100.00 & 99.76 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nAll three subcomponents independently achieve ${\\geq}$99.50\\% with 100\\% fail recall (Table~\\ref{tab:exc_subcomponent}), showing that no single subcomponent is necessary for Tier~1 performance.\n\n\\paragraph{Format marker confound.}\n\\texttt{exc\\_type\\_only} and \\texttt{exc\\_stacktrace\\_only} retain the \\texttt{[ERROR]} prefix marker present in the full \\texttt{exception\\_only} format; \\texttt{exc\\_message\\_only} contains only the bare exception class name and message text without any format markers.\nBecause the marker alone is sufficient for near-perfect regex accuracy (B5: 99.33\\%; \\S\\ref{sec:nomarker}), \\texttt{exc\\_type\\_only} (100.00\\%) and \\texttt{exc\\_stacktrace\\_only} (99.83\\%) are confounded with marker-based classification; we therefore do not make hierarchy claims among subcomponents.\n\\texttt{exc\\_message\\_only} (99.50\\%) provides a clean test: without any format markers, it achieves accuracy comparable to the full \\texttt{exception\\_only} condition (99.83\\%), complementing the dedicated marker-removal ablation (\\texttt{nomarker}: 97.65\\%; \\S\\ref{sec:nomarker}) as additional evidence that the model learns semantic exception patterns rather than format shortcuts.\n\n%% ============================================================\n\\section{Trace Length Ablation}\n\\label{sec:trace_length_full}\n\nTo test whether the \\texttt{full\\_trace} performance gap is caused by input truncation at training time, we vary the maximum trace token budget on Qwen-2.5-7B (seed=42) while keeping all other hyperparameters fixed.\n\n\\begin{table}[t]\n\\centering\n\\caption{Trace length and truncation direction ablation on Qwen-2.5-7B ($N{=}1{,}190$, seed=42). Head = standard left-truncation (retain first $k$ tokens); Tail = retain last $k$ tokens. Per-condition bootstrap 95\\% CIs ($B{=}10{,}000$).}\n\\label{tab:trace_length}\n\\small\n\\begin{tabular}{llcc}\n\\toprule\n\\textbf{Direction} & \\textbf{Max Tokens} & \\textbf{Acc (\\%)} & \\textbf{95\\% CI} \\\\\n\\midrule\nHead & 256  & 78.82 & [76.4, 81.0] \\\\\nHead & 512  & 80.42 & [78.2, 82.6] \\\\\nHead & 1024 & 77.23 & [74.9, 79.6] \\\\\nHead & no\\_limit ($\\infty$) & 81.76 & [79.7, 83.9] \\\\\n\\midrule\nTail & 256  & 77.48 & --- \\\\\nTail & 512  & 93.61 & --- \\\\\nTail & 1024 & 96.47 & --- \\\\\nTail & 2048 & 97.31 & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n% Budget curve figure moved to main text (Figure~\\ref{fig:budget_curve}).\n\nAs shown in Table~\\ref{tab:trace_length} and Figure~\\ref{fig:budget_curve}, all four trace length conditions fall within a 5pp range (77.2\\%--81.8\\%).\nTo quantify the reliability of the observed differences, Table~\\ref{tab:trace_length_pairwise} reports paired bootstrap comparisons ($B{=}10{,}000$, seed=42) across all condition pairs.\n\n\\begin{table}[t]\n\\centering\n\\caption{Pairwise paired bootstrap comparisons for trace length ablation ($B{=}10{,}000$, seed=42). $\\Delta$ = accuracy difference between the two conditions (first $-$ second in the budget group; condition $-$ baseline in the other groups). **$p{<}.01$; ***$p{<}.001$.}\n\\label{tab:trace_length_pairwise}\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llccc}\n\\toprule\n& \\textbf{Comparison} & \\textbf{$\\Delta$ (pp)} & \\textbf{95\\% CI} & \\textbf{$p$-value} \\\\\n\\midrule\n\\multirow{4}{*}{\\rotatebox{90}{\\scriptsize Budget}}\n& 512 vs.\\ 256           & $+$1.60  & [$-$0.34, $+$3.53]   & 0.117 \\\\\n& 1024 vs.\\ 512          & $-$3.19  & [$-$5.29, $-$1.09]   & 0.002** \\\\\n& no\\_limit vs.\\ 1024    & $+$4.54  & [$+$2.52, $+$6.55]   & ${<}$0.001*** \\\\\n& no\\_limit vs.\\ 256     & $+$2.94  & [$+$0.84, $+$5.04]   & 0.006** \\\\\n\\midrule\n\\multirow{4}{*}{\\rotatebox{90}{\\scriptsize vs.\\ no\\_trace}}\n& 256 $-$ no\\_trace       & $+$3.70  & [$+$1.43, $+$6.05]   & 0.002** \\\\\n& 512 $-$ no\\_trace       & $+$5.29  & [$+$3.03, $+$7.56]   & ${<}$0.001*** \\\\\n& 1024 $-$ no\\_trace      & $+$2.10  & [$-$0.17, $+$4.37]   & 0.078 \\\\\n& no\\_limit $-$ no\\_trace & $+$6.64  & [$+$4.37, $+$8.99]   & ${<}$0.001*** \\\\\n\\midrule\n\\multirow{4}{*}{\\rotatebox{90}{\\scriptsize vs.\\ exc.}}\n& 256 $-$ exc\\_only       & $-$21.01 & [$-$23.45, $-$18.74] & ${<}$0.001*** \\\\\n& 512 $-$ exc\\_only       & $-$19.41 & [$-$21.76, $-$17.14] & ${<}$0.001*** \\\\\n& 1024 $-$ exc\\_only      & $-$22.61 & [$-$25.04, $-$20.25] & ${<}$0.001*** \\\\\n& no\\_limit $-$ exc\\_only & $-$18.07 & [$-$20.34, $-$15.88] & ${<}$0.001*** \\\\\n\\bottomrule\n\\end{tabular}%\n}\n\\end{table}\n\n\\paragraph{Non-monotonic pattern (head-truncation).}\nUnder head-truncation (retaining trace prefixes), the trend is non-monotonic: 512 tokens (80.42\\%) slightly outperforms 256 tokens (78.82\\%), but doubling to 1024 tokens \\emph{decreases} accuracy to 77.23\\%, a statistically significant 3.19pp drop ($p{=}.002$, 95\\% CI [$-$5.29, $-$1.09]).\nThe no-limit condition (81.76\\%) recovers and significantly exceeds 1024 tokens ($p{<}.001$), but 1024 tokens is not significantly better than \\texttt{no\\_trace} (75.13\\%; $\\Delta{=}{+}2.10$pp, $p{=}.078$, 95\\% CI [$-$0.17, $+$4.37]).\nThis non-monotonicity is specific to head-truncation: the 1024-token prefix retains enough irrelevant content to mislead the model while discarding diagnostic events that appear near the trace terminus.\nUnder tail-truncation, accuracy increases monotonically for Qwen-7B and Qwen-1.5B (Table~\\ref{tab:tail_cross_model}); only DeepSeek-6.7B shows a mild $-$1.5pp decrease at tail-1024$\\to$tail-2048, attributable to architecture-specific long-context sensitivity rather than a systematic mid-length pathology.\n\n\\paragraph{Comparison to baselines.}\nAll four trace budget conditions significantly exceed \\texttt{no\\_trace} except 1024 tokens ($p{=}.078$), indicating that raw trace content provides some signal but unreliably so.\nThe gap to \\texttt{exception\\_only} (99.83\\%) is massive for every budget condition (18--23pp, all $p{<}.001$), underscoring that even unlimited raw traces cannot substitute for targeted signal extraction.\nThe best full-trace condition (no\\_limit, 81.76\\%) still lags \\texttt{exception\\_only} by 18.07pp (95\\% CI [$-$20.34, $-$15.88]).\n\n\\paragraph{Interpretation.}\nThese results rule out input truncation as the primary explanation for the full-trace performance gap: even with unlimited tokens, the model cannot extract the diagnostic signal that VOTA's targeted compression provides.\nThe non-monotonic dip at 1024 tokens is consistent with a ``worst-of-both-worlds'' regime where the model receives enough noisy context to dilute the signal but not enough to compensate through broader coverage.\nThe result reinforces the information density interpretation (\\S\\ref{sec:density}): the gap between full traces and VOTA is driven by the \\emph{content} of the trace (irrelevant lines diluting the diagnostic signal), not its \\emph{length}.\nIn contrast, VOTA's compressed representation concentrates the diagnostic signal into fewer tokens, making it sensitive to truncation when those tokens are removed (\\S\\ref{sec:cross_model}).\n\n\\paragraph{Truncation direction.}\nTail-truncation (retaining the last $k$ tokens) dramatically outperforms head-truncation: \\texttt{tail\\_2048} achieves 97.31\\% vs.\\ \\texttt{head\\_2048} (no\\_limit) at 81.76\\%, a 15.55pp improvement.\nEven \\texttt{tail\\_512} (93.61\\%) exceeds every head-truncation condition by over 11pp.\n\nHowever, \\texttt{tail\\_256} (77.48\\%) performs at the \\texttt{no\\_trace} baseline level (75.13\\%), indicating that the diagnostic signal does not reside in the very last trace lines.\nThe critical jump occurs between 256 and 512 tail tokens (+16.13pp), localizing the signal window to approximately 256--512 tokens from the trace terminus.\nThis is consistent with the trace format: the globals module dump consumes the first ${\\sim}$384 tail tokens (pure noise), so structured execution markers (\\texttt{[Line~X]} variable values) only become visible when the budget exceeds this threshold.\n\nThe 18.07pp gap from \\texttt{full\\_trace} to \\texttt{exception\\_only} decomposes as: 86\\% positional concentration (recovered by tail-truncation at 2048 tokens) and 14\\% residual content noise (the 2.52pp gap from \\texttt{tail\\_2048} to \\texttt{exception\\_only} that persists regardless of truncation direction).\nThe fact that \\texttt{exception\\_only} (99.83\\%) still outperforms \\texttt{tail\\_2048} (97.31\\%) indicates that semantic extraction (identifying the exception type and message) is superior to positional extraction (keeping a fixed window), because the model need not filter out non-diagnostic lines that happen to fall within the window.\n\n\\paragraph{Cross-model budget curve.}\nTable~\\ref{tab:tail_cross_model} extends the tail-truncation analysis to a full budget sweep across four models spanning three architecture families and an 8.7$\\times$ parameter range.\n\n\\begin{table}[t]\n\\centering\n\\caption{Cross-model tail-truncation budget curve ($N{=}1{,}190$). All four models exhibit a transition between tail-384 and tail-512 (+11--22pp). $\\downarrow$: non-monotonic decrease. $^\\dag$CodeLlama tail-384/512/1024 trained with label-only loss to address tokenizer-driven gradient dilution (\\S\\ref{sec:tokenizer_analysis}); tail-1024 reports best-epoch accuracy (epoch 1). CodeLlama tail entries are not directly comparable to other models (which use full-sequence loss). $^\\ddag$CodeLlama tail-2048 outlier (41.8\\%): LoRA long-sequence instability under label-only loss; excluded from cross-model analysis.}\n\\label{tab:tail_cross_model}\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lcccccc}\n\\toprule\n\\textbf{Model} & \\textbf{tail-256} & \\textbf{tail-384} & \\textbf{tail-512} & \\textbf{tail-1024} & \\textbf{tail-2048} & \\textbf{exc\\_only} \\\\\n\\midrule\nQwen-7B (7B) & 77.5 & 79.9 & 93.6 & 96.5 & 97.3 & 99.83 \\\\\nDeepSeek (6.7B) & 76.4 & 80.7 & 93.9 & 96.5 & 95.0$\\downarrow$ & 99.33 \\\\\nCodeLlama (13B) & 77.9 & 82.7$^\\dag$ & 98.2$^\\dag$ & 98.2$^\\dag$ & 41.8$^\\ddag$ & 99.89 \\\\\nQwen-1.5B (1.5B) & 72.6 & 73.6 & 95.6 & 96.6 & 97.9 & 99.83 \\\\\n\\bottomrule\n\\end{tabular}%\n}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\caption{Cross-model truncation direction comparison ($N{=}1{,}190$). Head-truncation retains the first 2,048 tokens; tail-truncation retains the last 2,048. All four models' head-2048 accuracies converge into a narrow 75.3--81.8\\% band (6.5pp), comparable to the tail-256 signal-poor band (72.6--77.9\\%, 5.3pp). $^\\dag$CodeLlama tail-2048 pending retraining (\\S\\ref{sec:tokenizer_analysis}).}\n\\label{tab:head_vs_tail}\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Model} & \\textbf{head-2048 (\\%)} & \\textbf{tail-2048 (\\%)} & \\textbf{Gap (pp)} \\\\\n\\midrule\nQwen-1.5B & 75.3 & 97.9 & +22.6 \\\\\nDeepSeek-6.7B & 78.7 & 95.0 & +16.3 \\\\\nCodeLlama-13B & 79.9 & ---$^\\dag$ & ---$^\\dag$ \\\\\nQwen-7B & 81.8 & 97.3 & +15.5 \\\\\n\\bottomrule\n\\end{tabular}%\n}\n\\end{table}\n\nFour patterns emerge from the budget curve.\n\\emph{Phase transition between 384 and 512 tokens}: the tail-384 column reveals that the transition is not instantaneous at 256$\\to$512 but localized between 384 and 512 tokens.\nAt tail-384, all four models remain near baseline (73.6--80.7\\%), gaining only +1.0--4.8pp over tail-256.\nThe steep jump occurs at 384$\\to$512: +13.7pp (Qwen-7B), +13.2pp (DeepSeek), +15.5pp (CodeLlama), +22.0pp (Qwen-1.5B), crossing from near-baseline to near-ceiling.\nThis localizes the critical threshold to ${\\sim}$400--500 tokens: below ${\\sim}$384 tokens, the entire token budget is consumed by globals module dumps (pure noise); above ${\\sim}$512, at least one \\texttt{[Line~X]} execution event marker becomes visible, regardless of model capacity or architecture.\n\n\\emph{Convergence at tail-512+}: once the sharp performance jump is crossed, accuracy converges across all models into a 93.6--98.2\\% band at tail-512 (seed 42).\nMulti-seed validation shows robustness: across all 12 model$\\times$seed combinations at tail-512 (Table~\\ref{tab:tail512_seeds}), all accuracies fall within [93.61\\%, 98.24\\%], a 4.63pp band that compresses the signal-poor tail-256 spread (6.3pp) by 27\\%.\nCodeLlama-13B shows perfect per-model convergence at tail-512: all three seeds achieve 98.24\\% ($\\sigma{=}$0), consistent with the 13B scale and label-only loss providing a stronger optimization signal in the signal-rich regime (Table~\\ref{tab:tail512_seeds}).\nHowever, CodeLlama's higher tail-512 accuracy may partly reflect label-only loss rather than model capacity; direct comparison with other models (which use full-sequence loss) is confounded by this training difference.\n\n\\begin{table}[t]\n\\centering\n\\caption{Cross-seed convergence at the tail-512 truncation point ($N{=}1{,}190$ per seed). All 12 model$\\times$seed combinations fall within a 4.63pp band [93.61\\%, 98.24\\%]. CodeLlama-13B achieves identical accuracy across all three seeds ($\\sigma{=}$0).}\n\\label{tab:tail512_seeds}\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lccccr}\n\\toprule\n\\textbf{Model} & \\textbf{S42} & \\textbf{S123} & \\textbf{S456} & \\textbf{Mean} & \\textbf{$\\sigma$} \\\\\n\\midrule\nQwen-7B (7B)      & 93.61 & 96.00 & 97.65 & 95.75 & 2.05 \\\\\nDeepSeek (6.7B)    & 93.95 & 95.04 & 96.10 & 95.03 & 1.08 \\\\\nQwen-1.5B (1.5B)  & 95.63 & 97.65 & 96.72 & 96.67 & 1.01 \\\\\nCodeLlama (13B)    & 98.24 & 98.24 & 98.24 & \\textbf{98.24} & \\textbf{0.00} \\\\\n\\midrule\n\\multicolumn{4}{l}{Cross-model band} & \\multicolumn{2}{r}{[93.61, 98.24] = 4.63pp} \\\\\n\\bottomrule\n\\end{tabular}%\n}\n\\end{table}\n\nAt tail-1024, four models reach 96.5--98.2\\% (CodeLlama 98.2\\% under label-only loss, three others 96.5--96.6\\%).\nScale and architecture differences that dominate the signal-poor regime (tail-256 range: 72.6--77.9\\%, 5.3pp) compress dramatically in the signal-rich regime.\n\n\\emph{Signal-poor convergence band}: head-2048 accuracies across all four models also converge into a narrow 75.3--81.8\\% band (6.5pp; Table~\\ref{tab:head_vs_tail}), comparable in width to the tail-256 band (72.6--77.9\\%, 5.3pp).\nWhen the diagnostic signal is absent (head-truncation discards trace terminus) or unreachable (tail-256 is too short), models of different scale and architecture collapse to similar performance, suggesting a shared floor determined by code comprehension rather than trace processing.\n\n\\emph{Scale behavior inversion}: in the signal-poor regime (tail-256), smaller models perform worse (Qwen-1.5B 72.6\\% vs.\\ Qwen-7B 77.5\\%, $-$4.9pp), mirroring the \\texttt{no\\_trace} scale pattern.\nIn the signal-rich regime (tail-512+), this reverses: Qwen-1.5B matches or exceeds Qwen-7B (95.6\\% vs.\\ 93.6\\% at tail-512; 97.9\\% vs.\\ 97.3\\% at tail-2048), consistent with sufficient trace signal eliminating the capacity advantage.\n\n\\emph{Non-monotonicity at long sequences}: two models show accuracy decreases beyond tail-1024.\nDeepSeek-6.7B drops $-$1.5pp from tail-1024 (96.5\\%) to tail-2048 (95.0\\%), consistent with its known long-context sensitivity (\\S\\ref{sec:training_dynamics}).\nCodeLlama-13B exhibits a more severe collapse: tail-2048 under label-only loss drops to 41.8\\% (vs.\\ tail-1024 = 98.2\\%), which we attribute to LoRA long-sequence instability under the label-only loss regime; this outlier is excluded from cross-model tail-2048 analysis.\nQwen-7B and Qwen-1.5B increase monotonically across all budgets.\n\nTable~\\ref{tab:head_vs_tail} shows the truncation direction effect: among the three models with complete data, tail-2048 outperforms head-2048 by 15.5--22.6pp.\nThe gap is largest for Qwen-1.5B (+22.6pp), indicating that smaller models benefit most from positional proximity to the diagnostic signal, as they lack the capacity to locate it within longer, noisier prefixes.\n\n%% ============================================================\n\\section{Calibration Analysis}\n\\label{sec:calibration_full}\n\nBeyond accuracy, we evaluate whether trace conditions affect prediction calibration, motivated by recent findings that code LLM confidence is often poorly calibrated \\citep{spiess2025calibration}.\n\n\\begin{table}[t]\n\\centering\n\\caption{Calibration metrics on Qwen-2.5-7B ($N{=}1{,}190$, seed=42). ECE = expected calibration error; Brier = Brier score. Lower is better for both.}\n\\label{tab:calibration}\n\\small\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Condition} & \\textbf{ECE $\\downarrow$} & \\textbf{Brier $\\downarrow$} \\\\\n\\midrule\nae\\_only & \\textbf{0.0004} & \\textbf{0.0008} \\\\\nexception\\_only & 0.0027 & 0.0013 \\\\\nVOTA & 0.0054 & 0.005 \\\\\nfull\\_trace & 0.096 & 0.144 \\\\\nno\\_trace & 0.171 & 0.197 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:calibration} shows that calibration quality mirrors the Tier~1/2 hierarchy.\nTier~1 conditions (\\texttt{ae\\_only}: ECE=0.0004; \\texttt{exception\\_only}: ECE=0.0027) produce near-perfectly calibrated predictions, while \\texttt{full\\_trace} (ECE=0.096) and \\texttt{no\\_trace} (ECE=0.171) exhibit substantial miscalibration.\nVOTA (ECE=0.0054) is well-calibrated but slightly worse than either Tier~1 component alone, reinforcing the pattern that combining trace signals dilutes rather than improves the prediction signal.\n\nThe Brier scores tell a consistent story: \\texttt{ae\\_only} (0.0008) and \\texttt{exception\\_only} (0.0013) achieve near-zero scores, while \\texttt{no\\_trace} (0.197) indicates substantial miscalibration.\n\n\\paragraph{Cross-model calibration.}\nTable~\\ref{tab:calibration_cross} extends the calibration analysis to four models (1.5B--13B) under \\texttt{exception\\_only}.\nAll four models achieve ECE ${<}$ 0.007 and Brier ${<}$ 0.007, indicating that calibration quality generalizes across architectures and scales.\nCodeLlama-13B achieves the lowest ECE (0.0020) and MCE (0.0411), while DeepSeek-6.7B shows the highest ECE (0.0064) and Brier (0.0061), consistent with its higher error rate (8 errors vs.\\ 2 for Qwen/CodeLlama).\n\n\\begin{table}[t]\n\\centering\n\\caption{Cross-model calibration for \\texttt{exception\\_only} ($N{=}1{,}190$, seed=42). ECE = expected calibration error; Brier = Brier score; MCE = maximum calibration error. All four models (1.5B--13B) achieve ECE ${<}$ 0.007.}\n\\label{tab:calibration_cross}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Model} & \\textbf{ECE $\\downarrow$} & \\textbf{Brier $\\downarrow$} & \\textbf{MCE $\\downarrow$} \\\\\n\\midrule\nQwen-1.5B & \\textbf{0.0020} & \\textbf{0.0013} & --- \\\\\nCodeLlama-13B & \\textbf{0.0020} & \\textbf{0.0013} & \\textbf{0.0411} \\\\\nQwen-7B & 0.0027 & \\textbf{0.0013} & 0.8355 \\\\\nDeepSeek-6.7B & 0.0064 & 0.0061 & 0.7756 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n%% ============================================================\n\\section{Error Overlap Analysis}\n\\label{sec:error_overlap}\n\nWe analyze the overlap between error sets of different conditions to determine whether they fail on the same samples (Figure~\\ref{fig:error_overlap}).\n\n\\texttt{exception\\_only}'s 2 errors (samples 901 and 905) have zero intersection with the error sets of all other conditions (Jaccard = 0.000 in all pairwise comparisons).\nThis orthogonality arises because \\texttt{exception\\_only} errors are caused by \\texttt{GeneratorExit} false positives (pass samples misclassified as fail due to benign \\texttt{BaseException} events), while errors from other conditions are predominantly fail samples misclassified as pass due to insufficient signal.\n\nAmong non-exception conditions, error sets exhibit hierarchical containment: \\texttt{ae\\_only} $\\subset$ VOTA $\\subset$ \\texttt{loop\\_only} $\\subset$ \\texttt{no\\_trace}, with pairwise Jaccard indices increasing with signal overlap.\n\\texttt{loop\\_only} and \\texttt{full\\_trace} share the highest overlap (Jaccard ${\\sim}$0.65), reflecting their shared reliance on behavioral patterns rather than explicit fault indicators.\n\nThis analysis indicates that \\texttt{exception\\_only} operates on an independent signal dimension: its errors are representation ambiguities (iterator protocol artifacts) rather than information deficits, explaining why combining it with other signals cannot eliminate these specific errors.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{error_overlap}\n\\caption{Jaccard similarity between error sets of different conditions (Qwen-7B, seed=42, $N{=}1{,}190$). \\texttt{exception\\_only} (exc\\_only) has zero overlap with all other conditions, indicating it operates on an independent signal dimension.}\n\\label{fig:error_overlap}\n\\end{figure}\n\n%% ============================================================\n\\section{Cross-Dataset Generalization: DebugBench}\n\\label{sec:debugbench_full}\n\nTo test whether exception-based verdict prediction generalizes beyond LLM-generated solutions, we evaluate on DebugBench \\citep{tian2024debugbench}, a dataset of human-written programs with synthetically injected bugs (single-point mutations such as operator replacement, variable misuse, and missing statements).\nAfter filtering for executable Python samples with valid traces, we retain 426 samples with a near-balanced class distribution (majority baseline: 51.4\\%).\n\n\\begin{table}[t]\n\\centering\n\\caption{Generalization to DebugBench ($N{=}426$, Qwen-2.5-7B, seed=42). Wilson 95\\% CIs. The component ranking (exception\\_only $\\geq$ VOTA $>$ no\\_trace) is preserved, and exception\\_only achieves perfect accuracy.}\n\\label{tab:debugbench}\n\\small\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Condition} & \\textbf{Acc (\\%)} & \\textbf{95\\% CI} \\\\\n\\midrule\nexception\\_only & \\textbf{100.00} & [99.14, 100.00] \\\\\nVOTA & 99.77 & [99.30, 100.00] \\\\\nno\\_trace & 96.71 & [94.80, 98.40] \\\\\n\\midrule\nMajority baseline & 51.41 & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:debugbench} shows that the component ranking from the main experiments is preserved: \\texttt{exception\\_only} (100.00\\%) $\\geq$ VOTA (99.77\\%) $>$ \\texttt{no\\_trace} (96.71\\%).\nThe \\texttt{exception\\_only} condition achieves perfect accuracy, showing that the exception-based representation generalizes to a different fault distribution without degradation.\n\nThe absolute margins are much narrower than on the main dataset: the \\texttt{no\\_trace} baseline already achieves 96.71\\% (compared to 75.13\\% on HumanEval+MBPP), leaving only 3.29pp of headroom for trace-based improvement.\nThis ceiling effect reflects a fundamental difference in fault characteristics: DebugBench bugs are synthetically injected single-point mutations, which produce code that is structurally dissimilar from the original correct solution; a model can often identify the fault from source code alone.\nIn contrast, the HumanEval+MBPP solutions are LLM-generated, producing natural errors (logic mistakes, edge-case failures) where the faulty and correct solutions may be structurally similar, making code-only verdict prediction substantially harder.\n\nThese results support exception-based verdict prediction as a generalizable approach: the method does not degrade on an out-of-distribution dataset, and the exception dominance ranking (exception\\_only $\\geq$ VOTA $>$ no\\_trace) is consistent across both datasets. However, the narrow DebugBench margins are insufficient to independently validate trace importance.\nThe 24.70pp trace lift on the main dataset (no\\_trace 75.13\\% $\\to$ exception\\_only 99.83\\%) remains the primary evidence for the value of exception-based trace signals.\n\n%% ============================================================\n\\section{Cross-Model Robustness Analysis}\n\\label{sec:robustness_analysis}\n\nThe cross-model gap pattern (Table~\\ref{tab:cross_model}) suggests a design principle: \\emph{trace representations should match the model capability floor, not the ceiling.}\nException events are consistently the most effective component on both models, and their structural simplicity (a fixed-format error message) ensures that the relative advantage over richer representations holds across all seeds.\nAll three DeepSeek \\texttt{exception\\_only} seeds achieve ${\\geq}$99.33\\% (99.33/99.50/99.33, $\\sigma{=}$0.10pp), matching Qwen and CodeLlama at ${\\geq}$99.83\\%.\nVOTA achieves ${\\geq}$98.57\\% across all models when excluding outlier seeds (cross-model range: 0.80pp), but DeepSeek VOTA exhibits seed-dependent instability: seed 42 (84.45\\%) is a training failure due to tokenizer-induced truncation (91.7\\% of training samples affected), while seeds 123/456 (99.16\\%/99.33\\%) match cross-model performance.\nThis VOTA instability is confounded by tokenizer efficiency and base model differences \\citep{yang2024generalization}.\nOur \\texttt{exception\\_only} design sidesteps the truncation confound entirely: inputs have a median of 150 tokens (mean 398), well below the 2{,}048-token context window, so no training samples are truncated on either model.\nThe resulting 0.50pp cross-model gap (Table~\\ref{tab:cross_model}) is therefore a clean measure of model capability differences, making the ``capability floor'' principle directly testable.\nThe practical implication is that trace-based systems should default to the simplest sufficient signal.\n\n%% ============================================================\n\\section{Training Dynamics and Loss Decoupling}\n\\label{sec:training_dynamics}\n\nThe DeepSeek \\texttt{exception\\_only} results are consistent across all three seeds (99.33/99.50/99.33, $\\sigma{=}$0.10pp), matching Qwen's cross-seed stability.\nEpoch-level analysis shows mild degradation in seed 42: accuracy peaks at 99.83\\% after epoch~1 but settles at 99.33\\% by epoch~3 ($-$0.50pp), while seed 456 shows no degradation (99.33\\% at both epochs).\nEarly stopping may yield marginal gains, but the epoch effect is small (${\\leq}$0.5pp).\nThe practical recommendation: for deployment, use task-specific metrics (accuracy, fail recall) for checkpoint and seed selection rather than training loss, and train multiple seeds to select the best.\n\nThe contrast with VOTA is instructive: DeepSeek VOTA seed 42 accuracy monotonically increases from 78.15\\% to 84.45\\% across epochs, consistent with a performance limit from high trace truncation (91.7\\% of samples; \\S\\ref{sec:tokenizer_analysis}).\nSeeds 123/456, which avoid the truncation-sensitive initialization basin, achieve 99.16\\%/99.33\\%, indicating that the deficit is seed-specific rather than a fundamental model limitation.\n\n%% ============================================================\n\\section{Deduplication Statistics}\n\\label{sec:dedup_stats}\n\nTable~\\ref{tab:dedup} reports the duplication rates across trace formats.\nBecause multiple passing solutions to the same problem produce identical (input, output) pairs in the \\texttt{exception\\_only} format (correct executions raise no exceptions, so the trace content is the same regardless of the solution's internal logic), the dataset contains duplicate rows.\nTrain--test input overlap is zero (split by problem ID), so no information leakage occurs.\nThe high duplication in \\texttt{exception\\_only} does not affect our experimental conclusions: after deduplication the training set still contains 2,858 unique samples and the test set 607, providing sufficient coverage for the 591-problem benchmark.\n\n\\paragraph{Problem-level partitioning and sensitivity analysis.}\nData is partitioned at the problem level: 472 training problems and 119 test problems, with zero crossover.\nDuplicates arise from multiple candidate solutions per problem (up to 10 solutions each), not from cross-problem overlap.\nTo verify that deduplication does not alter any finding, we ran a sensitivity analysis across all 19 experimental conditions (7 trace formats $\\times$ 4 models, minus conditions not run): deduplication produces a negligible ($<$0.1pp) accuracy delta in every case.\nThis shows that duplicate samples neither inflate nor deflate accuracy, because duplicates share the same ground-truth label and the model's prediction is deterministic at inference time.\nDuplicates arise because the \\texttt{exception\\_only} format collapses passing solutions (which share identical ``no exception'' output) into identical rows; the redundancy is a property of the format's compactness for pass-class samples.\nThe \\texttt{exception\\_only} test set contains 48.99\\% such duplicates; all confidence intervals treat samples as independent Bernoulli trials.\n\n\\begin{table}[t]\n\\centering\n\\caption{Deduplication statistics. The \\texttt{exception\\_only} format collapses multiple passing solutions into identical rows because correct executions produce no exception events. Train--test input overlap is 0 (no leakage).}\n\\label{tab:dedup}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Split} & \\textbf{Total} & \\textbf{Unique} & \\textbf{Dup.\\ rate} \\\\\n\\midrule\nexception\\_only train & 4{,}720 & 2{,}858 & 39.45\\% \\\\\nexception\\_only test  & 1{,}190 &   607 & 48.99\\% \\\\\nraw\\_traces (full)    & 5{,}910 & 5{,}803 &  1.81\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n%% ============================================================\n\\section{Regex Baseline Analysis}\n\\label{sec:regex_baselines}\n\nTo establish a non-learning upper bound, we evaluate six regex-based baselines on the \\texttt{exception\\_only} test set ($N{=}1{,}190$) and two format-specific baselines on VOTA and \\texttt{full\\_trace} inputs.\n\n\\begin{table}[t]\n\\centering\n\\caption{Regex baseline accuracy ($N{=}1{,}190$). B4 is the strongest semantic baseline (6.22pp below SFT \\texttt{exception\\_only}, McNemar $p{<}.001$). B6 uses an error count threshold. $^\\ddag$B5 exploits a data formatting artifact: the \\texttt{[No exception data in trace]} marker is deterministically present in all pass samples, making this a format-level shortcut rather than a genuine exception-based heuristic.}\n\\label{tab:regex}\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llc}\n\\toprule\n\\textbf{Baseline} & \\textbf{Method} & \\textbf{Acc (\\%)} \\\\\n\\midrule\nB1: \\texttt{[ERROR]} presence & string match & 93.45 \\\\\nB2: Traceback presence & string match & 71.51 \\\\\nB3: Any keyword & union of B1+B2+Exception & 93.45 \\\\\nB4: Exception type regex & regex on exception class names & \\textbf{93.61} \\\\\nB5: Format marker & \\texttt{[No exception data]} $\\to$ pass & 99.33$^\\ddag$ \\\\\nB6: Error count $\\geq$2 & count threshold & 92.02 \\\\\n\\midrule\nVOTA format regex & best regex on VOTA traces & 75.55 \\\\\nfull\\_trace format regex & best regex on full traces & 77.39 \\\\\n\\bottomrule\n\\end{tabular}%\n}\n\\end{table}\n\nThe strongest legitimate baseline (B4, 93.61\\%) applies regex pattern-matching on Python exception class names (e.g., \\texttt{ValueError}, \\texttt{TypeError}).\nIts errors concentrate on 8 boundary samples where a \\texttt{ValueError} is raised inside a \\texttt{try/except} block and caught; the program passes despite an exception occurring in the trace.\nSFT \\texttt{exception\\_only} correctly classifies 6 of these 8 samples, indicating that the model learns the semantic distinction between caught (benign) and uncaught (fault-indicating) exceptions.\nB5 (99.33\\%) achieves near-SFT accuracy but relies on the deterministic presence of a format marker in pass-class traces, which is an artifact of the trace preprocessing pipeline rather than a generalizable signal; McNemar test vs.\\ SFT yields $p{=}.041$, indicating a statistically significant difference.\n\n\\paragraph{Cross-format comparison.}\nTable~\\ref{tab:regex_cross_format} compares SFT and the best applicable regex baseline for each trace format.\nThe SFT advantage increases with format complexity: \\texttt{no\\_trace} (+3.62pp over majority baseline) $<$ \\texttt{full\\_trace} (+4.37pp) $<$ \\texttt{exception\\_only} (+6.22pp) $\\ll$ VOTA (+23.86pp).\nThe VOTA gap is largest because its structured multi-component format carries semantic content that regex cannot parse, while \\texttt{exception\\_only}'s simpler format allows regex to capture most of the signal.\n\n\\begin{table}[t]\n\\centering\n\\caption{SFT vs.\\ best regex baseline by trace format ($N{=}1{,}190$). Regex baselines: majority class for \\texttt{no\\_trace}, keyword matching for \\texttt{full\\_trace}, pattern matching for VOTA, exception type regex (B4) for \\texttt{exception\\_only}.}\n\\label{tab:regex_cross_format}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Format} & \\textbf{SFT (\\%)} & \\textbf{Regex (\\%)} & \\textbf{$\\Delta$ (pp)} \\\\\n\\midrule\nexception\\_only & 99.83 & 93.61 & +6.22 \\\\\nVOTA & 99.41 & 75.55 & +23.86 \\\\\nfull\\_trace & 81.76 & 77.39 & +4.37 \\\\\nno\\_trace & 75.13 & 71.51 & +3.62 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n%% ============================================================\n\\section{Cross-Model Zero-Shot Comparison}\n\\label{sec:zeroshot_cross_model}\n\nTable~\\ref{tab:zeroshot_cross_model} compares zero-shot and SFT \\texttt{exception\\_only} accuracy across four models.\nZero-shot performance does not correlate with model size: the smallest model (Qwen-1.5B, 93.45\\%) outperforms all larger models, while the largest (CodeLlama-13B) falls below majority baseline.\nSFT compresses the 42.44pp zero-shot range to 0.50pp, eliminating architecture-dependent variance.\n\n\\begin{table}[t]\n\\centering\n\\caption{Zero-shot vs.\\ SFT \\texttt{exception\\_only} across four models ($N{=}1{,}190$). Zero-shot accuracy is uncorrelated with model size; SFT normalizes cross-architecture variance from 42.44pp to 0.50pp.}\n\\label{tab:zeroshot_cross_model}\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llccc}\n\\toprule\n\\textbf{Model} & \\textbf{Size} & \\textbf{Zero-shot (\\%)} & \\textbf{SFT (\\%)} & \\textbf{$\\Delta$ (pp)} \\\\\n\\midrule\nQwen-1.5B & 1.5B & 93.45 & 99.83 & +6.38 \\\\\nDeepSeek-6.7B & 6.7B & 90.59 & 99.39 & +8.80 \\\\\nQwen-7B & 7B & 89.08 & 99.83 & +10.75 \\\\\nCodeLlama-13B & 13B & 51.01 & 99.89 & +48.88 \\\\\n\\midrule\nRange & --- & 42.44pp & 0.50pp & --- \\\\\n\\bottomrule\n\\end{tabular}%\n}\n\\end{table}\n\n% Calibration table removed (redundant with Table~\\ref{tab:calibration_cross} in \\S\\ref{sec:calibration_full}).\n\n%% ============================================================\n\\section{Use of AI Assistants}\n\\label{app:ai-assistants}\n\nWe used Claude (Anthropic) as an AI coding and writing assistant\nthroughout this work. Specifically:\n\\begin{itemize}\n    \\item \\textbf{Code:} drafting experiment scripts, data-processing\n    pipelines, and analysis utilities; debugging and refactoring.\n    \\item \\textbf{Writing:} drafting and revising paper sections,\n    polishing prose, and reformatting LaTeX.\n    \\item \\textbf{Literature:} summarizing related papers to inform\n    the related-work section.\n\\end{itemize}\n",
      "numLines": 811,
      "startLine": 1,
      "totalLines": 811
    }
  },
  "sourceToolAssistantUUID": "e58add99-562e-49f5-aa3c-19363fa0ae30",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/.claude/sessions/paper_audit_content_b575bb0e",
  "sessionId": "1db729b7-6c37-474e-9cbb-179c13a8aeb8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-24T16:16:16.796Z_

<details open><summary>🔧 Tool call — Read · `toolu_01RxnRbbWWzPB2ainkYSrqsw`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/arr_checklist.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d048693d-ce61-4c45-9a7b-d28a38732dab",
  "isSidechain": false,
  "requestId": "req_011CbMh9tV4aN8QV3riH9wUf",
  "type": "assistant",
  "uuid": "7126252f-3d4b-40ac-82a7-27252622b40d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/.claude/sessions/paper_audit_content_b575bb0e",
  "sessionId": "1db729b7-6c37-474e-9cbb-179c13a8aeb8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012VsV8ncx6FrdGuWaCHMfaG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11894,
      "cache_read_input_tokens": 38247,
      "output_tokens": 703,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11894,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 703,
          "cache_read_input_tokens": 38247,
          "cache_creation_input_tokens": 11894,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11894
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

_source line 38 · 2026-05-24T16:16:16.879Z_

```json
{
  "parentUuid": "a6fea0b6-94a7-4b40-b9d4-01d782a6184d",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "e329aeef-a841-4b91-9ee3-6806443e5b0c",
  "timestamp": "2026-05-24T16:16:16.879Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/.claude/sessions/paper_audit_content_b575bb0e",
  "sessionId": "1db729b7-6c37-474e-9cbb-179c13a8aeb8",
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
  "lastPrompt": "项目：trace-verdict-study Venue：emnlp-2026 论文目录：/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper  Phase 1 确定性检查结果： 源码检查: passed=False, 6 critical, 17 warning 一致性检查:…",
  "leafUuid": "e329aeef-a841-4b91-9ee3-6806443e5b0c",
  "sessionId": "1db729b7-6c37-474e-9cbb-179c13a8aeb8"
}
```

---

### Runtime record

_source line 40_

```json
{
  "type": "ai-title",
  "aiTitle": "Audit trace-verdict-study EMNLP 2026 submission",
  "sessionId": "1db729b7-6c37-474e-9cbb-179c13a8aeb8"
}
```

---

### Assistant

_source line 41 · 2026-05-24T16:16:31.961Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the .tex files. Let me perform a systematic content audit across all the dimensions specified in the instructions.

Let me now do targeted searches for specific patterns (em-dash, filler words, AI-style markers).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e329aeef-a841-4b91-9ee3-6806443e5b0c",
  "isSidechain": false,
  "requestId": "req_011CbMhB3qexySCiBKuXabRj",
  "type": "assistant",
  "uuid": "d93e02c8-0f62-4fba-9084-dfc82ce4dc4d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/.claude/sessions/paper_audit_content_b575bb0e",
  "sessionId": "1db729b7-6c37-474e-9cbb-179c13a8aeb8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01E7ZPGiRDsSaR7yEqjjZfr1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 34835,
      "cache_read_input_tokens": 50141,
      "output_tokens": 846,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 34835,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 846,
          "cache_read_input_tokens": 50141,
          "cache_creation_input_tokens": 34835,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 34835
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

_source line 42 · 2026-05-24T16:16:33.131Z_

正在进行详细的模式扫描和交叉比对。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d93e02c8-0f62-4fba-9084-dfc82ce4dc4d",
  "isSidechain": false,
  "requestId": "req_011CbMhB3qexySCiBKuXabRj",
  "type": "assistant",
  "uuid": "7a1b17be-a5f1-4bfa-8bf3-4c9c76372ee9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/.claude/sessions/paper_audit_content_b575bb0e",
  "sessionId": "1db729b7-6c37-474e-9cbb-179c13a8aeb8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01E7ZPGiRDsSaR7yEqjjZfr1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 34835,
      "cache_read_input_tokens": 50141,
      "output_tokens": 846,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 34835,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 846,
          "cache_read_input_tokens": 50141,
          "cache_creation_input_tokens": 34835,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 34835
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

_source line 43 · 2026-05-24T16:16:35.645Z_

<details open><summary>🔧 Tool call — Grep · `toolu_017PbdGFrLgmxZMTZxQdhJaE`</summary>

```json
{
  "pattern": "—",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper",
  "output_mode": "content",
  "-n": true,
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7a1b17be-a5f1-4bfa-8bf3-4c9c76372ee9",
  "isSidechain": false,
  "requestId": "req_011CbMhB3qexySCiBKuXabRj",
  "type": "assistant",
  "uuid": "4eef5898-eadf-45d7-bb5b-6690d0ad9029",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/.claude/sessions/paper_audit_content_b575bb0e",
  "sessionId": "1db729b7-6c37-474e-9cbb-179c13a8aeb8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01E7ZPGiRDsSaR7yEqjjZfr1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 34835,
      "cache_read_input_tokens": 50141,
      "output_tokens": 846,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 34835,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 846,
          "cache_read_input_tokens": 50141,
          "cache_creation_input_tokens": 34835,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 34835
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

_source line 44 · 2026-05-24T16:16:41.576Z_

<details><summary>↩ Tool result · `toolu_01QJGsBbRPvTPSJTwPV7e3cs`</summary>

```text
No matches found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2ebdfab6-bd37-4470-a7b0-dcf321141fea",
  "isSidechain": false,
  "promptId": "96f110f9-4fbd-4295-8cdb-ef5a8ad15d7a",
  "type": "user",
  "uuid": "50eb9e17-281b-4a04-bcab-f24032a49480",
  "toolUseResult": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "",
    "numLines": 0
  },
  "sourceToolAssistantUUID": "2ebdfab6-bd37-4470-a7b0-dcf321141fea",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/.claude/sessions/paper_audit_content_b575bb0e",
  "sessionId": "1db729b7-6c37-474e-9cbb-179c13a8aeb8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 45 · 2026-05-24T16:16:35.691Z_

<details><summary>↩ Tool result · `toolu_017PbdGFrLgmxZMTZxQdhJaE`</summary>

```text
No matches found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4eef5898-eadf-45d7-bb5b-6690d0ad9029",
  "isSidechain": false,
  "promptId": "96f110f9-4fbd-4295-8cdb-ef5a8ad15d7a",
  "type": "user",
  "uuid": "ae89eb7b-f7f6-40b6-94cc-c6f6bda20bc1",
  "toolUseResult": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "",
    "numLines": 0
  },
  "sourceToolAssistantUUID": "4eef5898-eadf-45d7-bb5b-6690d0ad9029",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/.claude/sessions/paper_audit_content_b575bb0e",
  "sessionId": "1db729b7-6c37-474e-9cbb-179c13a8aeb8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 46 · 2026-05-24T16:16:36.616Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01WBxikgP72mLRTP7yAFCw7e`</summary>

```json
{
  "pattern": "---",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper",
  "output_mode": "content",
  "-n": true,
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ae89eb7b-f7f6-40b6-94cc-c6f6bda20bc1",
  "isSidechain": false,
  "requestId": "req_011CbMhB3qexySCiBKuXabRj",
  "type": "assistant",
  "uuid": "079dc0e0-b213-4467-a488-a85801c19363",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/.claude/sessions/paper_audit_content_b575bb0e",
  "sessionId": "1db729b7-6c37-474e-9cbb-179c13a8aeb8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01E7ZPGiRDsSaR7yEqjjZfr1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 34835,
      "cache_read_input_tokens": 50141,
      "output_tokens": 846,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 34835,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 846,
          "cache_read_input_tokens": 50141,
          "cache_creation_input_tokens": 34835,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 34835
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

_source line 47 · 2026-05-24T16:16:36.641Z_

<details><summary>↩ Tool result · `toolu_01WBxikgP72mLRTP7yAFCw7e`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/experiments.tex:83:VOTA & exc+ae+loop & 99.05$^\S$ & [98.49, 99.50] & --- \\
/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/experiments.tex:84:VOTA\_no\_ae & exc+loop & 99.41 & [98.90, 99.80] & --- \\
/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/experiments.tex:86:full\_trace & complete trace & 81.44{\scriptsize$\pm$1.11} & --- & --- \\
/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/experiments.tex:87:no\_trace & none & 75.13 & [72.77, 77.48] & --- \\
/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/experiments.tex:89:Regex (best) & exc.\ type regex & 93.61 & --- & --- \\
/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/experiments.tex:90:3-shot (Qwen-7B) & in-context learning & 90.84 & --- & --- \\
/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/experiments.tex:91:Zero-shot (4 models) & prompting & 51.0--93.5 & --- & --- \\
/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/experiments.tex:151:exception\_only & 99.83{\scriptsize$\pm$0.00} & --- \\
/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/main.tex:21:Complete execution traces contain all information needed for verdict prediction---classifying whether a test passes or fails---yet they actively degrade SFT-based learning.
/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/main.tex:24:With exception-only input, a 7B model surpasses GPT-4o by 12pp---a ranking that reverses without trace information, demonstrating that input density dominates model scale.
/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/appendix.tex:218:VOTA\_no\_ae    & 99.41 & ---   & ---   & --- \\
/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/appendix.tex:222:no\_trace       & 75.13 & ---   & ---   & --- \\
/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/appendix.tex:380:Tail & 256  & 77.48 & --- \\
/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/appendix.tex:381:Tail & 512  & 93.61 & --- \\
/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/appendix.tex:382:Tail & 1024 & 96.47 & --- \\
/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/appendix.tex:383:Tail & 2048 & 97.31 & --- \\
/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/appendix.tex:487:CodeLlama-13B & 79.9 & ---$^\dag$ & ---$^\dag$ \\
/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/appendix.tex:587:Qwen-1.5B & \textbf{0.0020} & \textbf{0.0013} & --- \\
/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/appendix.tex:636:Majority baseline & 51.41 & --- \\
/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/appendix.tex:789:Range & --- & 42.44pp & 0.50pp & --- \\
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "079dc0e0-b213-4467-a488-a85801c19363",
  "isSidechain": false,
  "promptId": "96f110f9-4fbd-4295-8cdb-ef5a8ad15d7a",
  "type": "user",
  "uuid": "53dc9e98-a95b-4487-baba-f44a2d09b2cb",
  "toolUseResult": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/experiments.tex:83:VOTA & exc+ae+loop & 99.05$^\\S$ & [98.49, 99.50] & --- \\\\\n/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/experiments.tex:84:VOTA\\_no\\_ae & exc+loop & 99.41 & [98.90, 99.80] & --- \\\\\n/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/experiments.tex:86:full\\_trace & complete trace & 81.44{\\scriptsize$\\pm$1.11} & --- & --- \\\\\n/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/experiments.tex:87:no\\_trace & none & 75.13 & [72.77, 77.48] & --- \\\\\n/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/experiments.tex:89:Regex (best) & exc.\\ type regex & 93.61 & --- & --- \\\\\n/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/experiments.tex:90:3-shot (Qwen-7B) & in-context learning & 90.84 & --- & --- \\\\\n/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/experiments.tex:91:Zero-shot (4 models) & prompting & 51.0--93.5 & --- & --- \\\\\n/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/experiments.tex:151:exception\\_only & 99.83{\\scriptsize$\\pm$0.00} & --- \\\\\n/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/main.tex:21:Complete execution traces contain all information needed for verdict prediction---classifying whether a test passes or fails---yet they actively degrade SFT-based learning.\n/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/main.tex:24:With exception-only input, a 7B model surpasses GPT-4o by 12pp---a ranking that reverses without trace information, demonstrating that input density dominates model scale.\n/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/appendix.tex:218:VOTA\\_no\\_ae    & 99.41 & ---   & ---   & --- \\\\\n/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/appendix.tex:222:no\\_trace       & 75.13 & ---   & ---   & --- \\\\\n/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/appendix.tex:380:Tail & 256  & 77.48 & --- \\\\\n/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/appendix.tex:381:Tail & 512  & 93.61 & --- \\\\\n/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/appendix.tex:382:Tail & 1024 & 96.47 & --- \\\\\n/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/appendix.tex:383:Tail & 2048 & 97.31 & --- \\\\\n/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/appendix.tex:487:CodeLlama-13B & 79.9 & ---$^\\dag$ & ---$^\\dag$ \\\\\n/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/appendix.tex:587:Qwen-1.5B & \\textbf{0.0020} & \\textbf{0.0013} & --- \\\\\n/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/appendix.tex:636:Majority baseline & 51.41 & --- \\\\\n/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/appendix.tex:789:Range & --- & 42.44pp & 0.50pp & --- \\\\",
    "numLines": 20
  },
  "sourceToolAssistantUUID": "079dc0e0-b213-4467-a488-a85801c19363",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/.claude/sessions/paper_audit_content_b575bb0e",
  "sessionId": "1db729b7-6c37-474e-9cbb-179c13a8aeb8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 48 · 2026-05-24T16:16:39.430Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01EdEgmbv1aG5uqF8YGLqqhK`</summary>

```json
{
  "pattern": "(it is worth noting|notably|importantly|furthermore|moreover|additionally|delve|leverage|utilize|facilitate|a myriad|a plethora|in the realm of)",
  "-i": true,
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper",
  "output_mode": "content",
  "-n": true,
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "53dc9e98-a95b-4487-baba-f44a2d09b2cb",
  "isSidechain": false,
  "requestId": "req_011CbMhB3qexySCiBKuXabRj",
  "type": "assistant",
  "uuid": "a688107e-1242-4faa-bf6e-cb06b2d65430",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/.claude/sessions/paper_audit_content_b575bb0e",
  "sessionId": "1db729b7-6c37-474e-9cbb-179c13a8aeb8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01E7ZPGiRDsSaR7yEqjjZfr1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 34835,
      "cache_read_input_tokens": 50141,
      "output_tokens": 846,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 34835,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 846,
          "cache_read_input_tokens": 50141,
          "cache_creation_input_tokens": 34835,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 34835
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

_source line 49 · 2026-05-24T16:16:39.463Z_

<details><summary>↩ Tool result · `toolu_01EdEgmbv1aG5uqF8YGLqqhK`</summary>

```text
No matches found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a688107e-1242-4faa-bf6e-cb06b2d65430",
  "isSidechain": false,
  "promptId": "96f110f9-4fbd-4295-8cdb-ef5a8ad15d7a",
  "type": "user",
  "uuid": "4d58a85a-b8bb-41cf-ab24-227e7a72be50",
  "toolUseResult": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "",
    "numLines": 0
  },
  "sourceToolAssistantUUID": "a688107e-1242-4faa-bf6e-cb06b2d65430",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/.claude/sessions/paper_audit_content_b575bb0e",
  "sessionId": "1db729b7-6c37-474e-9cbb-179c13a8aeb8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 50 · 2026-05-24T16:16:41.306Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01U23nVSk3w6wKpRz4h3Zzt7`</summary>

```json
{
  "pattern": "ing,|ing\\.",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper",
  "output_mode": "content",
  "-n": true,
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4d58a85a-b8bb-41cf-ab24-227e7a72be50",
  "isSidechain": false,
  "requestId": "req_011CbMhB3qexySCiBKuXabRj",
  "type": "assistant",
  "uuid": "43199607-9d75-43ac-af77-ec184a35988f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/.claude/sessions/paper_audit_content_b575bb0e",
  "sessionId": "1db729b7-6c37-474e-9cbb-179c13a8aeb8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01E7ZPGiRDsSaR7yEqjjZfr1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 34835,
      "cache_read_input_tokens": 50141,
      "output_tokens": 846,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 34835,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 846,
          "cache_read_input_tokens": 50141,
          "cache_creation_input_tokens": 34835,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 34835
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

_source line 51 · 2026-05-24T16:16:41.332Z_

<details><summary>↩ Tool result · `toolu_01U23nVSk3w6wKpRz4h3Zzt7`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/related_work.tex:5:NExT \citep{ni2024next} and ET-CoT \citep{eguchi2025etcot} used trace chain-of-thought for repair and execution reasoning; \citet{ferrando2025execute} found compact traces comparable to full traces, supporting our density finding.
/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/experiments.tex:47:CodeLlama-13B seed 123 achieves 100\%, indicating the 2 persistent errors (\texttt{GeneratorExit}; Appendix~\ref{sec:irreducible}) are convergence artifacts; 99.83\% is a floor, not a ceiling.
/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/experiments.tex:124:The strongest semantic regex B4 (exception class matching, 93.61\%) is marker-invariant; SFT \texttt{nomarker} (97.65\%) exceeds it by 4.04pp, isolating the learned semantic contribution beyond pattern matching.
/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/experiments.tex:136:\paragraph{Controlled gradient masking.}
/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/experiments.tex:137:To isolate gradient dilution, we mask 99.8\% of gradient updates during \texttt{exception\_only} training, matching the diagnostic token ratio of full traces while preserving compact input.
/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/experiments.tex:170:Cross-architecture validation on two additional families is directionally consistent (single seed each): DeepSeek-Coder-6.7B achieves 99.33\% and CodeLlama-13B achieves 100\% under 99.8\% masking, both well above the full-trace range (77--82\%, Table~\ref{tab:cross_model}), supporting content quality as the dominant factor across architectures.
/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/main.tex:21:Complete execution traces contain all information needed for verdict prediction---classifying whether a test passes or fails---yet they actively degrade SFT-based learning.
/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/conclusion.tex:3:Across four code-specialized models (1.5B--13B), compact exception events (${\geq}$99.33\%) outperform complete traces (77--82\%) by 18--23pp; gradient masking (${\leq}$4\% dilution), cross-dataset transfer (99.4--100\%), and marker-removal robustness show that diagnostic density, not information quantity, drives SFT learning.
/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/discussion.tex:5:The results suggest two independent signal pathways and a dilution mechanism that together explain why complete traces degrade SFT learning.
/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/appendix.tex:300:The only misclassifications arise from \texttt{GeneratorExit}, a \texttt{BaseException} subclass that is not an \texttt{Exception}. It is raised by Python's iterator protocol during generator short-circuiting, not by actual program errors.
/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/appendix.tex:497:The steep jump occurs at 384$\to$512: +13.7pp (Qwen-7B), +13.2pp (DeepSeek), +15.5pp (CodeLlama), +22.0pp (Qwen-1.5B), crossing from near-baseline to near-ceiling.
/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/appendix.tex:530:When the diagnostic signal is absent (head-truncation discards trace terminus) or unreachable (tail-256 is too short), models of different scale and architecture collapse to similar performance, suggesting a shared floor determined by code comprehension rather than trace processing.
/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/appendix.tex:655:The cross-model gap pattern (Table~\ref{tab:cross_model}) suggests a design principle: \emph{trace representations should match the model capability floor, not the ceiling.}
/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/appendix.tex:688:To verify that deduplication does not alter any finding, we ran a sensitivity analysis across all 19 experimental conditions (7 trace formats $\times$ 4 models, minus conditions not run): deduplication produces a negligible ($<$0.1pp) accuracy delta in every case.
/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/appendix.tex:805:    pipelines, and analysis utilities; debugging and refactoring.
/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/introduction.tex:9:Verdict prediction offers a cleaner testbed: as binary classification, it isolates the learning signal from generation noise, and controlled component ablation directly measures how trace content affects SFT learning.
/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/introduction.tex:10:This approach aligns with recent *ACL precedent: CRUXEval \citep{gu2024cruxeval} uses execution prediction to probe code reasoning, and NExT \citep{ni2024next} uses trace-augmented chain-of-thought for program repair.
/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/introduction.tex:16:A simple regex exploiting a format marker matches this ceiling, so the interesting question is not why exceptions help but \emph{why complete traces hurt}.
/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/arr_checklist.tex:71:\item \textbf{Code}: Training, evaluation, and trace preprocessing scripts will be released upon acceptance.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "43199607-9d75-43ac-af77-ec184a35988f",
  "isSidechain": false,
  "promptId": "96f110f9-4fbd-4295-8cdb-ef5a8ad15d7a",
  "type": "user",
  "uuid": "41790a71-03f5-47a9-b689-68204482f946",
  "toolUseResult": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/related_work.tex:5:NExT \\citep{ni2024next} and ET-CoT \\citep{eguchi2025etcot} used trace chain-of-thought for repair and execution reasoning; \\citet{ferrando2025execute} found compact traces comparable to full traces, supporting our density finding.\n/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/experiments.tex:47:CodeLlama-13B seed 123 achieves 100\\%, indicating the 2 persistent errors (\\texttt{GeneratorExit}; Appendix~\\ref{sec:irreducible}) are convergence artifacts; 99.83\\% is a floor, not a ceiling.\n/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/experiments.tex:124:The strongest semantic regex B4 (exception class matching, 93.61\\%) is marker-invariant; SFT \\texttt{nomarker} (97.65\\%) exceeds it by 4.04pp, isolating the learned semantic contribution beyond pattern matching.\n/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/experiments.tex:136:\\paragraph{Controlled gradient masking.}\n/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/experiments.tex:137:To isolate gradient dilution, we mask 99.8\\% of gradient updates during \\texttt{exception\\_only} training, matching the diagnostic token ratio of full traces while preserving compact input.\n/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/experiments.tex:170:Cross-architecture validation on two additional families is directionally consistent (single seed each): DeepSeek-Coder-6.7B achieves 99.33\\% and CodeLlama-13B achieves 100\\% under 99.8\\% masking, both well above the full-trace range (77--82\\%, Table~\\ref{tab:cross_model}), supporting content quality as the dominant factor across architectures.\n/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/main.tex:21:Complete execution traces contain all information needed for verdict prediction---classifying whether a test passes or fails---yet they actively degrade SFT-based learning.\n/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/conclusion.tex:3:Across four code-specialized models (1.5B--13B), compact exception events (${\\geq}$99.33\\%) outperform complete traces (77--82\\%) by 18--23pp; gradient masking (${\\leq}$4\\% dilution), cross-dataset transfer (99.4--100\\%), and marker-removal robustness show that diagnostic density, not information quantity, drives SFT learning.\n/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/discussion.tex:5:The results suggest two independent signal pathways and a dilution mechanism that together explain why complete traces degrade SFT learning.\n/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/appendix.tex:300:The only misclassifications arise from \\texttt{GeneratorExit}, a \\texttt{BaseException} subclass that is not an \\texttt{Exception}. It is raised by Python's iterator protocol during generator short-circuiting, not by actual program errors.\n/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/appendix.tex:497:The steep jump occurs at 384$\\to$512: +13.7pp (Qwen-7B), +13.2pp (DeepSeek), +15.5pp (CodeLlama), +22.0pp (Qwen-1.5B), crossing from near-baseline to near-ceiling.\n/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/appendix.tex:530:When the diagnostic signal is absent (head-truncation discards trace terminus) or unreachable (tail-256 is too short), models of different scale and architecture collapse to similar performance, suggesting a shared floor determined by code comprehension rather than trace processing.\n/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/appendix.tex:655:The cross-model gap pattern (Table~\\ref{tab:cross_model}) suggests a design principle: \\emph{trace representations should match the model capability floor, not the ceiling.}\n/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/appendix.tex:688:To verify that deduplication does not alter any finding, we ran a sensitivity analysis across all 19 experimental conditions (7 trace formats $\\times$ 4 models, minus conditions not run): deduplication produces a negligible ($<$0.1pp) accuracy delta in every case.\n/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/appendix.tex:805:    pipelines, and analysis utilities; debugging and refactoring.\n/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/introduction.tex:9:Verdict prediction offers a cleaner testbed: as binary classification, it isolates the learning signal from generation noise, and controlled component ablation directly measures how trace content affects SFT learning.\n/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/introduction.tex:10:This approach aligns with recent *ACL precedent: CRUXEval \\citep{gu2024cruxeval} uses execution prediction to probe code reasoning, and NExT \\citep{ni2024next} uses trace-augmented chain-of-thought for program repair.\n/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/introduction.tex:16:A simple regex exploiting a format marker matches this ceiling, so the interesting question is not why exceptions help but \\emph{why complete traces hurt}.\n/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/arr_checklist.tex:71:\\item \\textbf{Code}: Training, evaluation, and trace preprocessing scripts will be released upon acceptance.",
    "numLines": 19
  },
  "sourceToolAssistantUUID": "43199607-9d75-43ac-af77-ec184a35988f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/.claude/sessions/paper_audit_content_b575bb0e",
  "sessionId": "1db729b7-6c37-474e-9cbb-179c13a8aeb8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 52 · 2026-05-24T16:16:41.564Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01QJGsBbRPvTPSJTwPV7e3cs`</summary>

```json
{
  "pattern": " – ",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper",
  "output_mode": "content",
  "-n": true,
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "41790a71-03f5-47a9-b689-68204482f946",
  "isSidechain": false,
  "requestId": "req_011CbMhB3qexySCiBKuXabRj",
  "type": "assistant",
  "uuid": "2ebdfab6-bd37-4470-a7b0-dcf321141fea",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/.claude/sessions/paper_audit_content_b575bb0e",
  "sessionId": "1db729b7-6c37-474e-9cbb-179c13a8aeb8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01E7ZPGiRDsSaR7yEqjjZfr1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 34835,
      "cache_read_input_tokens": 50141,
      "output_tokens": 846,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 34835,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 846,
          "cache_read_input_tokens": 50141,
          "cache_creation_input_tokens": 34835,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 34835
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

_source line 53_

```json
{
  "type": "last-prompt",
  "lastPrompt": "项目：trace-verdict-study Venue：emnlp-2026 论文目录：/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper  Phase 1 确定性检查结果： 源码检查: passed=False, 6 critical, 17 warning 一致性检查:…",
  "leafUuid": "50eb9e17-281b-4a04-bcab-f24032a49480",
  "sessionId": "1db729b7-6c37-474e-9cbb-179c13a8aeb8"
}
```

---

### Runtime record

_source line 54_

```json
{
  "type": "ai-title",
  "aiTitle": "Audit trace-verdict-study EMNLP 2026 submission",
  "sessionId": "1db729b7-6c37-474e-9cbb-179c13a8aeb8"
}
```

---

### Assistant

_source line 55 · 2026-05-24T16:20:59.849Z_

<details><summary>Logged reasoning block</summary>

```text
Let me analyze what I found:

1. **Em-dashes (—)**: No Unicode em-dashes found. 
2. **`---` (LaTeX em-dashes)**: Found 2 instances in main.tex abstract (line 21 and 24). The rest are table cell placeholders (---), which are fine.
3. **Filler words**: No matches for "it is worth noting", "notably", "importantly", "furthermore", "moreover", "additionally", "delve", "leverage", "utilize", "facilitate", "a myriad", "a plethora", "in the realm of" - all clean.


4. **En-dashes ( – )**: None found.
5. **-ing patterns**: The grep results show many hits but they're legitimate uses like "matching" and "finding" rather than problematic phrase endings.

Now I'm examining those two `---` instances in the abstract more carefully. Line 21 uses em-dashes to set off explanatory clauses about verdict prediction and test classification—this is a typical pattern in academic writing. Line 24 appears to be cut off, so I need to see the full context there.

Let me step back and do a comprehensive check across the entire paper's narrative arc. The abstract establishes that complete execution traces actually hurt SFT-based verdict prediction despite containing all the diagnostic information. The introduction reinforces this same finding—complete traces degrade accuracy compared to compact exception events. The methods section then breaks down trace representations through component ablation, the experiments explain why complete traces underperform and which components matter, and the conclusion ties it together: compact exception events win because diagnostic density drives learning better.

Now I'm checking whether the contributions listed in the introduction align with this narrative. The first contribution claims complete traces degrade SFT accuracy, and the second involves semantic versus format-marker distinctions. decomposition (§nomarker)
3. Two-tier signal hierarchy (§ablation, §trace_length)
4. Mechanistic decomposition (§density)

All 4 contributions map to specific sections. Let me verify each:
- §cross_model → Table 1, cross-model comparison ✓
- §nomarker → Format marker ablation ✓
- §ablation → Component ablation ✓
- §density → Decomposing degradation ✓

**Checking Abstract == Intro**: Both focus on complete traces degrading verdict prediction. Consistent. ✓
**Intro contributions == Method**: Method describes 7 conditions, models, loss ablation. Aligns. ✓
**Method's design rationale == Intro's gap**: Intro says prior work didn't decompose trace components. Method designs ablation study. ✓
**Experiments validate contributions**: Yes, all 4 contributions have corresponding experimental sections. ✓
**Conclusion == Experiments**: Conclusion summarizes the key findings from experiments. ✓

Narrative seems quite consistent. No major drift detected.

### 2. Chapter Structure

**Abstract**: 
- Problem: Complete traces degrade SFT-based learning ✓
- Method: Component ablation across 4 models ✓
- Result: 77-82% vs ≥99.33% ✓
- Significance: Two-tier signal hierarchy ✓
All 4 questions answered. 

Now I'm checking the abstract word count and reviewing its opening statement about how complete execution traces contain all necessary information for verdict prediction yet paradoxically harm learning performance. Now I'm sketching out the paper structure—five paragraphs that flow from background through prior work, then methods, central findings, and deeper analysis. The organization feels natural even though it blends some sections together, like weaving the problem statement into the opening rather than isolating it.

For related work, I'm grouping by thematic areas instead of listing studies one by one, which lets me draw connections across papers and show how they relate to each other. Each contribution maps cleanly to a specific section of the results—the trace degradation finding anchors to the cross-model analysis, the semantic versus format distinction shows up in the ablation, the signal hierarchy emerges from component and length studies, and the mechanistic decomposition gets its own detailed treatment.

The supplementary analyses in section 5.5 aren't orphaned; they support the main contributions while the discussion ties everything together conceptually. The title, abstract, and experimental setup all align—I'm testing four models across different sizes and architectures, and the core claim about degradation is backed by substantial gaps in verdict accuracy across all of them.

Now I'm verifying the specific quantitative claims against the data. The accuracy figures check out against Table 1, the gradient dilution experiment confirms the 4% threshold, and the performance gap versus GPT-4o is approximately 12 percentage points as stated. The format-marker removal result and bidirectional transfer both have proper support, and the non-overlapping confidence intervals validate the two-tier signal hierarchy. I need to verify the scale-invariance claim across the model size range from 1.5B to 13B parameters.

Looking at the actual experimental data, the tier-1 signals show less than 1.2 percentage points variation across four different models, which is fairly consistent but the "scale-invariant" language might be slightly overstated. The paper does qualify this to the tested range, and they have multi-seed results for the exception-only condition across multiple models, so it's not just single-seed verification. I'd note this as a minor caution about the strength of the claim, though it's technically defensible given the qualification.

For experimental rigor, they're reporting multi-seed results with standard deviations and Wilson confidence intervals at 95%, with single-seed outliers clearly marked. The baselines are solid—recent models like Qwen-2.5-Coder and DeepSeek-Coder, regex baselines, zero-shot and few-shot variants, plus comparisons to GPT-4o and GPT-4.1. Now I'm checking the ablation studies to see how thoroughly they isolate each component's contribution.

They've defined seven different conditions plus a loss ablation, and the component ablation table covers all the pieces. For statistical rigor, they're using paired bootstrap resampling with 10,000 iterations, McNemar tests, Wilson confidence intervals, and Holm-Bonferroni correction for multiple comparisons. The reproducibility section shows hyperparameters in the appendix, wall-clock training times per condition, and data preprocessing details in the methods. There's a limitations section and a checklist file, though the GPU specification is frustratingly vague—just says "enterprise-grade ≥80 GB VRAM" without naming the actual model. But then the checklist itself seems to contradict this...

Actually, I'm noticing a discrepancy: the checklist mentions "2× high-end datacenter GPUs (~96 GB VRAM each)" while the main text says "1× enterprise-grade GPU (≥80 GB VRAM)". The numbers don't match, and neither version specifies whether it's an A100, H100, or something else. That's a real reproducibility problem. On the terminology side, the diagnostic token ratio, VOTA, tier classifications, and percentage point notation all seem consistently defined and used throughout.

For chapter flow, the transitions between sections feel natural even if they're not explicitly signposted—the intro sets up contributions, methods define the approach, experiments apply it, and the discussion interprets results through a two-pathway framework rather than just restating numbers. The limitations section acknowledges the Python-only focus of the benchmarks, though it seems to cut off mid-sentence. The user's custom rule takes precedence over the standard 150-word threshold, so the limitations section is actually compliant even though it's shorter. I'm noting the tension between the audit dimension and the user's explicit instruction, but it's not a critical issue. Now I'm checking the em-dash usage in the paper—there are only two instances in the abstract, which is fine since they're used appropriately rather than as placeholder formatting.

Looking at the "-ing" phrases more carefully, most are legitimate uses like "matching," "isolating," and "indicating" in natural contexts. Some instances like "isolating the learned semantic contribution" do follow that AI pattern of using "-ing" constructions to describe results, but I need to examine each case individually to determine if they're actually problematic or just normal academic phrasing. I'm scanning through the experiments and discussion sections more systematically now. There are indeed a few trailing -ing phrases scattered throughout—like "indicating the 2 persistent errors" and "implying that combining signals introduces noise"—but the overall frequency isn't problematic. The pattern isn't as pervasive as I initially worried.

Moving on to check for filler words and excessive paragraph breaks. The paper uses paragraph headers liberally, which naturally segments the content, but the text within each section is substantive enough that it doesn't feel padded. No filler words jumping out either.

Now I'm verifying there's no internal information residue—no experiment IDs, server names, or tool references that shouldn't be there. The paper is clean on that front. And since this already passed phase 1, I can move forward to the EMNLP-specific guidelines.

The abstract looks good at around 130-140 words, well under the 200-word limit. There's only one limitations section in the main text, which is correct. But I'm concerned about the page count—the document is 20 pages total, and I need to verify the main text stays within the 8-page limit before references and appendix. The appendix is substantial at over 800 lines, and with all the tables and figures in the main sections, I can't be certain without compiling whether the main text exceeds the threshold. This could be a problem worth flagging. already flagged in Phase 1.

Wait, the Phase 1 result showed "编译: ✅, 页数: 20" — that's the total page count. EMNLP 2026 limits the main text to 8 pages, with references and limitations excluded. Given all the tables and figures in the experiments section, I'm concerned the main text might exceed this limit.

Let me break down what's in the main text: introduction with a figure, related work, method section, a substantial experiments section with multiple tables and figures, discussion with another figure, and conclusion. The experiments alone are quite lengthy. Without actually compiling, I can't be certain, but with 20 total pages and a very long appendix, the main text is probably around 8-9 pages, which could be problematic.

Actually, I need to reconsider — the ARR checklist is separate, so those 20 pages are just main.tex plus appendix. References probably take 1-2 pages, and the appendix with its 18 sections and numerous tables and figures could easily be 10+ pages. That would put the main text plus limitations at around 7-8 pages, which is tight but potentially acceptable.

I should flag this as something to verify during compilation but not treat it as critical without actual data. Looking at my findings overall, there's nothing truly critical with the narrative consistency, but I do need to note that the abstract uses em-dashes in the source that should be checked. Looking at the cross-model results more carefully, the numbers in the introduction align with Table 1 — the 77–82% range for complete traces and ≥99.33% for exception-only events both check out. But there's a precision issue: the abstract claims ≥99.33% for exception_only, yet Table 1 shows DeepSeek at 99.39±0.10, which means individual seeds could dip below that threshold.

The 18–23pp gap claim is also borderline — my calculations show 17.95–22.83pp, so the lower bound is slightly under 18. I need to trace back to the abstract to see exactly which comparison this gap refers to.

Looking at the per-model gaps between exception_only and full_trace: Qwen-7B shows 18.39pp, Qwen-1.5B shows 22.77pp, CodeLlama-13B shows 19.99pp, and DeepSeek-6.7B shows 20.23pp. The range across these is 18.39–22.77pp, which does round to 18–23pp, so that claim checks out.

Now I need to verify the abstract's claim about a 7B model surpassing GPT-4o by 12pp. Finishing the tail-truncated traces claim — the data shows 93.6–98.2% recovery at 512 tokens, which checks out. ✓ The open question about larger models overcoming signal dilution remains unresolved. ✓

Now I'm verifying the ARR Responsible NLP Checklist placement — it's a separate document with its own \documentclass, so it should live in OpenReview's submission form rather than embedded in the paper itself, which appears correct.

Scanning the appendix for duplicate limitations sections — I only see one in the main text, and the appendix covers per-class metrics, training procedures, and the VOTA algorithm but no redundant limitations. ✓ The Discussion section interprets the two-pathway framework and signal dilution mechanistically rather than just restating results numbers, though it does reference tables appropriately.

I'm noticing a potential labeling issue: the Introduction references "Appendix~\ref{sec:training_dynamics}" as a section, but the Discussion embeds a figure with `\label{fig:training_dynamics}`. These appear to be two separate entities — one is an appendix section, the other a figure in the main text — so I need to verify whether they're actually distinct or if there's a mislabeling.

Now I'm checking the VOTA examples more carefully. The algorithm specifies appending `[No exception data in trace]` when no exceptions are found, but the pass example in the appendix doesn't show this marker — it only has `[LOOP]` and `[ASSERT]` outputs. The fail example does include `[ERROR]`, so there's an inconsistency between what the algorithm claims to output and what actually appears in the example.

I should also verify the figure captions and table references are consistent. The introduction mentions VOTA at 99.05%, and I need to check if that matches the ablation table's reported accuracy. The no_trace value of 75.13% checks out across both tables. For full_trace, the figure caption reports 81.44% which matches the 3-seed mean from Table 1, consistent with the "multi-seed means where available" note, even though Table 3 shows a single-seed baseline of 81.76%. ✓ Now I need to double-check the remaining values in the figure caption against their source tables. seed 42 value. But the abstract says "18-23pp gap" which uses the cross-model range. These are mixing single-seed and multi-seed values in different contexts. This is technically fine as long as the comparison is apples-to-apples, and the paper does note when it's using matched-seed vs multi-seed. But let me check: in §5.4 header, it says "81.76%" for the single comparison, then later says "3-seed mean 81.44%±1.11." So the 18.07pp gap is seed-42-matched (99.83-81.76=18.07). This is fine as a controlled comparison. ✓

Now I'm scanning for significance claims. The experiments section notes that all differences are significant at p<.0001 unless noted, and all cross-tier gaps remain significant.

The paper handles statistical testing properly without making unsupported claims. Let me look more closely at the VOTA examples. The pass case shows a trace with loop detection and assertion results, but according to the algorithm, the exception summary component should run first and output something about exception data. The example seems to be missing that initial output, which suggests there might be an inconsistency between what the algorithm specifies and what the example demonstrates. I need to verify whether VOTA actually includes the "[No exception data in trace]" marker in the experiments. Looking at the method section, VOTA is defined as exception events plus assertion comparisons plus loop compression, and the exception_only format explicitly uses this marker for pass cases. Since VOTA builds on the same exception handling logic, it should include the marker too—so the pass example's omission of it is a documentation error that needs fixing.

Now I'm noticing the checklist references an Ethics Statement that doesn't actually appear anywhere in the paper. The checklist claims it notes the work uses public benchmarks and has no human subjects, but if there's no ethics section to begin with, that's a false claim in the checklist itself. Let me search the tex files more thoroughly to confirm it's genuinely missing.

I don't find an Ethics section anywhere. The checklist is making assertions about content that isn't there, so I should flag this mismatch.

Let me also verify the abstract word counts precisely to make sure those numbers are accurate.

Now I'm checking whether "confirming" is the right word choice in that sentence about the marker-removal experiment—the 97.65% retention rate shows the model is robust to format changes, but does that really confirm learned patterns versus surface shortcuts, or is that claim slightly overstated?

Looking at the evidence: the marker-removal drops only 2 percentage points, and cross-dataset transfer holds at 99.4-100%, which is pretty compelling. Even with single-seed limitations on some experiments, this seems like solid support for the claim.

Let me verify the Limitations section is actually substantive and not just hand-waving—Python-only scope with 591 problems, code-specialized models in the 1.5B-13B range, and the multi-seed versus single-seed inconsistency across baselines. These are all real constraints worth noting.

Now checking the hardware specs in the ARR checklist against what's actually in the appendix—there's a discrepancy between what's claimed and what's documented. I'm noticing inconsistencies in how condition names are formatted across the tables and text — some use escaped underscores without `\texttt{}` formatting while others have `\texttt{}` applied, and "VOTA" appears plain in tables but sometimes formatted with `\texttt{}` in the prose. Let me trace through the exact formatting patterns to identify what needs to be standardized. I'm noticing that Figure 1 uses VOTA without defining it in the caption, but the acronym isn't formally introduced until the Method section — this creates a forward reference problem where readers encounter the term before its definition. The figure's placement in a two-column layout means it likely appears early in the document, well before VOTA is explained in §3, which could confuse readers.

I'm also checking the cross-references in the contributions section to verify they point to the correct section labels in the experiments file. All the cross-references check out and the claims in the abstract are backed by the experimental results, so I'm ready to compile the report.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "50eb9e17-281b-4a04-bcab-f24032a49480",
  "isSidechain": false,
  "requestId": "req_011CbMhCt75EJRRfGQa1NVeX",
  "type": "assistant",
  "uuid": "c86715fd-81c5-493a-ad82-7a52f6d7dfda",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/.claude/sessions/paper_audit_content_b575bb0e",
  "sessionId": "1db729b7-6c37-474e-9cbb-179c13a8aeb8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KqtR9kD6QGHGamYdTaYx8a",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3986,
      "cache_read_input_tokens": 84976,
      "output_tokens": 10732,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3986,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 10732,
          "cache_read_input_tokens": 84976,
          "cache_creation_input_tokens": 3986,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3986
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

_source line 56 · 2026-05-24T16:21:01.779Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01A97HLUc3RfVCjcpTFyjJ8P`</summary>

```json
{
  "pattern": "[Ee]thic",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper",
  "output_mode": "content",
  "-n": true,
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c86715fd-81c5-493a-ad82-7a52f6d7dfda",
  "isSidechain": false,
  "requestId": "req_011CbMhCt75EJRRfGQa1NVeX",
  "type": "assistant",
  "uuid": "116e8846-344c-4990-b18b-a329be867640",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/.claude/sessions/paper_audit_content_b575bb0e",
  "sessionId": "1db729b7-6c37-474e-9cbb-179c13a8aeb8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KqtR9kD6QGHGamYdTaYx8a",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3986,
      "cache_read_input_tokens": 84976,
      "output_tokens": 10732,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3986,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 10732,
          "cache_read_input_tokens": 84976,
          "cache_creation_input_tokens": 3986,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3986
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

_source line 57 · 2026-05-24T16:21:01.802Z_

<details><summary>↩ Tool result · `toolu_01A97HLUc3RfVCjcpTFyjJ8P`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/arr_checklist.tex:21:\textit{Yes.} The Ethics Statement notes that the work uses public benchmarks, involves no human subjects, and has minimal environmental impact. Verdict prediction is a developer-facing tool with no direct end-user impact.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "116e8846-344c-4990-b18b-a329be867640",
  "isSidechain": false,
  "promptId": "96f110f9-4fbd-4295-8cdb-ef5a8ad15d7a",
  "type": "user",
  "uuid": "6a9b3cf1-3dd6-43ba-a61e-d8748daa0fb8",
  "toolUseResult": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/arr_checklist.tex:21:\\textit{Yes.} The Ethics Statement notes that the work uses public benchmarks, involves no human subjects, and has minimal environmental impact. Verdict prediction is a developer-facing tool with no direct end-user impact.",
    "numLines": 1
  },
  "sourceToolAssistantUUID": "116e8846-344c-4990-b18b-a329be867640",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/.claude/sessions/paper_audit_content_b575bb0e",
  "sessionId": "1db729b7-6c37-474e-9cbb-179c13a8aeb8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 58 · 2026-05-24T16:21:02.871Z_

<details><summary>↩ Tool result · `toolu_019eceDQRbKpaL5afVQT69B2`</summary>

```text
1:\section{Experiments}
10:\subsection{Cross-Model Comparison}
45:\paragraph{Exception dominance across families.}
49:\paragraph{Scale effects concentrate in Tier~2.}
61:\paragraph{VOTA cross-family variation.}
65:\subsection{Component Ablation}
102:\paragraph{Rule-based baseline comparison.}
107:\paragraph{Zero-shot and few-shot LLM baselines.}
110:\paragraph{Frontier model crossover.}
114:\subsection{Format Marker Ablation}
126:\paragraph{Cross-dataset transfer.}
131:\subsection{Decomposing the Full-Trace Degradation}
136:\paragraph{Controlled gradient masking.}
166:\paragraph{Complementary evidence.}
173:\subsection{Complementary Analyses}
176:\paragraph{Trace length ablation.}
182:\paragraph{Truncation direction and budget curve.}
196:\paragraph{Calibration.}
208:\paragraph{Error analysis.}
211:\paragraph{Length control.}
214:\paragraph{Supplementary OOD analysis.}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a9e42c01-9228-4117-8c4b-cbaa2ebd1103",
  "isSidechain": false,
  "promptId": "96f110f9-4fbd-4295-8cdb-ef5a8ad15d7a",
  "type": "user",
  "uuid": "2ab97a8e-33a1-4fe0-90c8-6170d37d55d6",
  "toolUseResult": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "1:\\section{Experiments}\n10:\\subsection{Cross-Model Comparison}\n45:\\paragraph{Exception dominance across families.}\n49:\\paragraph{Scale effects concentrate in Tier~2.}\n61:\\paragraph{VOTA cross-family variation.}\n65:\\subsection{Component Ablation}\n102:\\paragraph{Rule-based baseline comparison.}\n107:\\paragraph{Zero-shot and few-shot LLM baselines.}\n110:\\paragraph{Frontier model crossover.}\n114:\\subsection{Format Marker Ablation}\n126:\\paragraph{Cross-dataset transfer.}\n131:\\subsection{Decomposing the Full-Trace Degradation}\n136:\\paragraph{Controlled gradient masking.}\n166:\\paragraph{Complementary evidence.}\n173:\\subsection{Complementary Analyses}\n176:\\paragraph{Trace length ablation.}\n182:\\paragraph{Truncation direction and budget curve.}\n196:\\paragraph{Calibration.}\n208:\\paragraph{Error analysis.}\n211:\\paragraph{Length control.}\n214:\\paragraph{Supplementary OOD analysis.}",
    "numLines": 21
  },
  "sourceToolAssistantUUID": "a9e42c01-9228-4117-8c4b-cbaa2ebd1103",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/.claude/sessions/paper_audit_content_b575bb0e",
  "sessionId": "1db729b7-6c37-474e-9cbb-179c13a8aeb8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 59 · 2026-05-24T16:21:02.860Z_

<details open><summary>🔧 Tool call — Grep · `toolu_019eceDQRbKpaL5afVQT69B2`</summary>

```json
{
  "pattern": "\\\\paragraph|\\\\section|\\\\subsection",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/experiments.tex",
  "output_mode": "content",
  "-n": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6a9b3cf1-3dd6-43ba-a61e-d8748daa0fb8",
  "isSidechain": false,
  "requestId": "req_011CbMhCt75EJRRfGQa1NVeX",
  "type": "assistant",
  "uuid": "a9e42c01-9228-4117-8c4b-cbaa2ebd1103",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/.claude/sessions/paper_audit_content_b575bb0e",
  "sessionId": "1db729b7-6c37-474e-9cbb-179c13a8aeb8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KqtR9kD6QGHGamYdTaYx8a",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3986,
      "cache_read_input_tokens": 84976,
      "output_tokens": 10732,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3986,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 10732,
          "cache_read_input_tokens": 84976,
          "cache_creation_input_tokens": 3986,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3986
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

_source line 60_

```json
{
  "type": "last-prompt",
  "lastPrompt": "项目：trace-verdict-study Venue：emnlp-2026 论文目录：/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper  Phase 1 确定性检查结果： 源码检查: passed=False, 6 critical, 17 warning 一致性检查:…",
  "leafUuid": "2ab97a8e-33a1-4fe0-90c8-6170d37d55d6",
  "sessionId": "1db729b7-6c37-474e-9cbb-179c13a8aeb8"
}
```

---

### Runtime record

_source line 61_

```json
{
  "type": "ai-title",
  "aiTitle": "Audit trace-verdict-study EMNLP 2026 submission",
  "sessionId": "1db729b7-6c37-474e-9cbb-179c13a8aeb8"
}
```

---

### Assistant

_source line 62 · 2026-05-24T16:21:06.937Z_

<details><summary>Logged reasoning block</summary>

```text
The ARR checklist claims "The Ethics Statement notes that..." but there's no Ethics Statement in the paper. The only ethics reference is in the checklist file. This is a problem.

Now let me compile all findings into the final report.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2ab97a8e-33a1-4fe0-90c8-6170d37d55d6",
  "isSidechain": false,
  "requestId": "req_011CbMhY9FBR9E52mZCRSdrE",
  "type": "assistant",
  "uuid": "ef69bd2e-d609-4d70-ba2d-53c616bc6a7e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/.claude/sessions/paper_audit_content_b575bb0e",
  "sessionId": "1db729b7-6c37-474e-9cbb-179c13a8aeb8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015HvhzS4ygcXTcgrviqh3BD",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11123,
      "cache_read_input_tokens": 88962,
      "output_tokens": 3059,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11123,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3059,
          "cache_read_input_tokens": 88962,
          "cache_creation_input_tokens": 11123,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11123
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

_source line 63 · 2026-05-24T16:22:23.154Z_

审计完成。以下为结构化 findings。

```
[CONTENT_AUDIT_START]

=== 叙事一致性 (CRITICAL 级) ===

- [info] [叙事一致性] Abstract/Intro/Method/Experiments/Discussion/Conclusion 主线一致：问题（complete traces 降低 SFT verdict accuracy）→ 方法（component ablation across 4 models）→ 结果（18-23pp gap, two-tier hierarchy）→ 结论（diagnostic density > information quantity）。未发现跨章叙事漂移。

- [info] [叙事一致性] Intro 4 条 contributions 均有对应的 section 和 table 支撑：C1→§5.1/Table 1, C2→§5.3, C3→§5.2+§5.4/Table 2, C4→§5.4/Table 3。无孤儿贡献。

- [info] [叙事一致性] Conclusion 总结的三个核心发现（exception > complete traces, gradient masking ≤4%, cross-dataset transfer）均有 Experiments 直接数据支撑，无凭空 claim。

=== 章节结构 ===

- [info] [章节结构] Abstract 四问完整：问题（traces degrade SFT）、方法（component ablation, 4 models）、结果（77-82% vs ≥99.33%）、意义（two-tier signal hierarchy）。约 152 words。

- [info] [章节结构] Intro 叙事线完整：背景→问题→prior work gap→本文方法→central result→contributions。结构清晰。

- [info] [章节结构] Related Work 按主题组织（Execution Traces / Verdict Prediction / Calibration），非列表堆砌式。每个主题段内有归纳和对比。

=== 贡献-范围对齐 ===

- [warning] [贡献-范围对齐] VOTA 首次出现在 Figure 1 caption (introduction.tex:39) 但未展开全称；定义在 Method §3.3 (method.tex:26)。这是冷引用——读者在 Introduction 就看到 VOTA 但不知道它代表什么。应在 Figure 1 caption 中加括号展开 "(Verdict-Optimized Trace Abstraction)"。

- [warning] [贡献-范围对齐] VOTA 算法（appendix.tex:108-138）与 VOTA pass 示例（appendix.tex:172-194）不一致：算法 Component 1 会在无 exception 时追加 "[No exception data in trace]"，但 pass 示例中缺失此 marker；示例的组件顺序（LOOP→ASSERT）与算法顺序（Exception→Assert→Loop）相反。审稿人如果交叉对照会发现矛盾。

=== Claim 强度匹配 ===

- [warning] [Claim强度] experiments.tex:50 "Tier~1 signals are scale-invariant across 1.5B--13B"——虽然跨 4 models 测试了 ≤1.2pp span，但 "scale-invariant" 是极强断言（paper-quality-lessons §2.2 明确列为禁用词）。建议改为 "scale-robust" 或 "show minimal scale sensitivity"。

- [info] [Claim强度] Abstract "a 7B model surpasses GPT-4o by 12pp"——实际 99.83-87.98=11.85pp，四舍五入为 12pp。可接受但精确写 "~12pp" 更严谨。

- [info] [Claim强度] "confirming learned diagnostic patterns rather than surface shortcuts" (Abstract)——marker-removal (97.65%, 3 seeds) + cross-dataset transfer (99.4-100%) 支撑充分。"confirming" 在此上下文强度可接受。

=== 实验严谨性 ===

- [warning] [实验严谨性] Table 1 中 full_trace 的 Qwen-1.5B (77.06†)、DeepSeek (79.16†)、no_trace 的 Qwen-7B (75.13†)、DeepSeek (73.36†)、CodeLlama (76.47†) 均为 single-seed 结果，但论文基于这些数据做跨模型 gap 分析和范围声明（"77--82%"、"18--23pp"）。核心 claim 的部分锚点依赖单 seed。Limitations 已声明此限制，但审稿人可能要求补跑。

=== 可复现性披露 ===

- [warning] [可复现性] GPU 型号未指定：appendix.tex:69 写 "1× enterprise-grade GPU (≥80 GB VRAM)"，arr_checklist.tex:48 写 "2× high-end datacenter GPUs (~96 GB VRAM each)"。两处措辞不同且均未给出具体型号（如 A100-80GB 或 H100）。审稿人会质疑复现性。

- [warning] [可复现性] GPU 数量/规格不一致：Appendix 说 "1× ... ≥80 GB"，Checklist 说 "2× ... ~96 GB"。数量（1 vs 2）和容量（80 vs 96 GB）均有出入。

- [info] [可复现性] 超参（LoRA rank/alpha/dropout、batch size、LR、epochs 等）完整列于 Appendix Table 5。训练时间分条件报告于 Appendix Table 6。数据预处理流程在 §3.2 描述。整体可复现信息充分。

=== 去 AI 风格 ===

- [warning] [去AI] main.tex:21 "verdict prediction---classifying whether a test passes or fails---yet" 使用了解释性 em-dash (---)。这是 AI 写作最显著标志（paper-writing-norms §5.1 最高优先级硬规则）。应改为逗号或括号。

- [warning] [去AI] main.tex:24 "GPT-4o by 12pp---a ranking that reverses without trace information" 又一处解释性 em-dash。同样应消除。

- [info] [去AI] 全文无 "it is worth noting" / "notably" / "importantly" / "furthermore" / "moreover" / "additionally" / "delve" / "leverage" / "utilize" / "a myriad of" / "a plethora of" 等 filler words。✓

- [info] [去AI] 全文无 Unicode em-dash (—) 或解释性 en-dash ( – )。仅有 LaTeX `---` 共 2 处（已标记）。✓

- [info] [去AI] 段落长度适中，未出现过度分段（2-3 句一段）的模式。✓

=== 符号/术语一致性 ===

- [info] [符号] 核心符号 $d$（diagnostic token ratio）在 Method §3.1 定义，Discussion 中一致使用。VOTA、Tier 1/2 等术语全文统一。pp（percentage points）一致使用。未发现同义词漂移。

=== 章节过渡与逻辑流 ===

- [info] [逻辑流] Discussion 提供了 "two-pathway framework" 的高层解读（显式/隐式信号通路 + 稀释机制），不只是重复 Results 数字。引用表格编号而非内联复制数字。✓

- [info] [逻辑流] Experiments→Discussion→Conclusion 形成 "结果→解释→总结" 的递进。Conclusion 没有引入 Experiments 中未呈现的新 claim。✓

=== Limitations 诚实度 ===

- [info] [Limitations] 包含 3 个 distinct limitations：(1) Python-only + 小规模 benchmarks, (2) 仅 code-specialized models ≤13B, (3) seed 数量有限。均为实质性限制，非回避式。符合用户自定义规则"覆盖 3 个点左右"。

=== 内部信息残留 ===

- [info] [内部信息] 无内部实验编号、服务器名、IP 地址、数据存储路径等痕迹。无隐含内部流程的表述。Phase 1 扫描也通过。✓

=== 用户自定义规则检查 ===

- [info] [写作规则] Abstract ~152 words，未超过 200 words 限制。✓

- [info] [写作规则] 仅有一个 Limitations section，在 main.tex 正文中（\section*{Limitations}）。Appendix 中无重复的 Limitations section。✓

- [warning] [写作规则] ARR checklist (arr_checklist.tex:21) 声称 "The Ethics Statement notes that..."，但论文正文和附录中不存在 Ethics Statement 或 Ethical Considerations 段。Checklist 引用了不存在的内容。虽然 EMNLP 2026 中 ethical considerations 是可选的，但 checklist 中的描述与论文不符，审稿人在 OpenReview 表单中如果复制这些文字会发现矛盾。

- [info] [写作规则] ARR Responsible NLP Checklist 在独立 tex 文件中（有自己的 \documentclass），未嵌入主论文 PDF。符合用户规则"在 OpenReview submission form 里面手动填写"。✓

- [warning] [审稿规则] 总页数 20 页。EMNLP 2026 主文限 8 页（不含 references 和 limitations）。无法在不编译的情况下精确判定主文页数，但 Experiments 含 3 tables + 3 figures + 大量文字，Discussion 含 1 figure——主文有超 8 页的风险。建议编译后精确检查。

[CONTENT_AUDIT_END]
```

**审计摘要**：叙事一致性（最高优先级维度）良好，Abstract→Intro→Method→Experiments→Discussion→Conclusion 主线统一，4 条 contributions 全部有 section/table 支撑。主要问题集中在：(1) Abstract 中 2 处 LaTeX em-dash 需消除（AI 痕迹）；(2) VOTA 冷引用 + 算法-示例不一致；(3) GPU 规格披露不足且 checklist 与正文矛盾；(4) "scale-invariant" claim 过强；(5) 主文可能超 8 页需编译验证。

[AUDIT_DONE]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ef69bd2e-d609-4d70-ba2d-53c616bc6a7e",
  "isSidechain": false,
  "requestId": "req_011CbMhY9FBR9E52mZCRSdrE",
  "type": "assistant",
  "uuid": "85d1d2b5-3455-4975-bbda-ed824147a71f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/.claude/sessions/paper_audit_content_b575bb0e",
  "sessionId": "1db729b7-6c37-474e-9cbb-179c13a8aeb8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015HvhzS4ygcXTcgrviqh3BD",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11123,
      "cache_read_input_tokens": 88962,
      "output_tokens": 3059,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11123,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3059,
          "cache_read_input_tokens": 88962,
          "cache_creation_input_tokens": 11123,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11123
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

_source line 64_

```json
{
  "type": "last-prompt",
  "lastPrompt": "项目：trace-verdict-study Venue：emnlp-2026 论文目录：/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper  Phase 1 确定性检查结果： 源码检查: passed=False, 6 critical, 17 warning 一致性检查:…",
  "leafUuid": "85d1d2b5-3455-4975-bbda-ed824147a71f",
  "sessionId": "1db729b7-6c37-474e-9cbb-179c13a8aeb8"
}
```

---

### Runtime record

_source line 65_

```json
{
  "type": "ai-title",
  "aiTitle": "Audit trace-verdict-study EMNLP 2026 submission",
  "sessionId": "1db729b7-6c37-474e-9cbb-179c13a8aeb8"
}
```

---
