# Research conversation: 项目：entrainment_gated_ft Venue：emnlp-2026 论文目录：/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 95
- **Recorded user turns:** 1
- **Tool calls:** 30
- **Original source:** `logs/chats/exported-trajectories/account-1/6e8d5c3f-7c75-4ff9-a01f-f2df71411ac1.jsonl`
- **Structured JSON:** [`95024db4da394fccc245.json`](../../sessions/95/95024db4da394fccc245.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-25T17:13:03.757Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-25T17:13:03.757Z",
  "sessionId": "6e8d5c3f-7c75-4ff9-a01f-f2df71411ac1",
  "content": "项目：entrainment_gated_ft\nVenue：emnlp-2026\n论文目录：/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper\n\nPhase 1 确定性检查结果：\n源码检查: passed=False, 2 critical, 1 warning\n一致性检查: 0 critical, 67 warning\n编译: ✅, 页数: 21\n内部信息: 0 critical, 0 warning\n\n━━━ 用户自定义规则（作为额外检查项）━━━\n## 用户自定义规则（必须遵守）\n### 写作规则\n\n- **[EMNLP 2026]** Limitations 章节只需要写一小段，覆盖 3 个点左右就可以了，不需要写得很长\n- **[EMNLP 2026]** ARR Responsible NLP Checklist在OpenReview的submission form里面（由用户手动填写），而不是在论文pdf里面\n- **[EMNLP 2026]** 一篇文章只能有一个limitations section，放在正文里面，appendix不能有 limitations section\n- **[EMNLP 2026]** abstract 不要超过 200 words\n\n### 审稿规则\n\n- **[EMNLP 2026]** “EMNLP 2026 通过 ARR 统一审稿，Main/Findings 不分开投稿（不是两个Track），Long/Short 也走同一审稿系统，Overall Assessment的评分标准如下：5 = Consider for Award（约前2.5%），4.5 = Borderline Award，4 = Conference（可被主会议接收），3.5 = Borderline Conference，3 = Findings（可被Findings接收），2.5 = Borderline Findings，2 = Resubmit next cycle（需大幅修改，可在下一周期完成），1.5 = Resubmit after next cycle（需大幅修改，无法在下一周期完成），1 = Do not resubmit（需完全重做或与*ACL无关）”\n- **[EMNLP 2026]** EMNLP 2026 restricts long paper submissions to a strict 8-page limit for main text, with unlimited space for references. Mandatory limitations and optional ethical considerations do not count towards this page limit, provided they do not contain excessive additional content.\n\n> 以上规则由用户配置，优先级等同于硬约束。违反会被 Reviewer 标记。\n请将以上规则逐条作为额外审计维度检查。违反的规则用 dimension `[写作规则]` 或 `[审稿规则]` 标记，severity 按实际影响判定。\n\n请按照你的角色指令执行内容结构审计。"
}
```

---

### Runtime record

_source line 2 · 2026-05-25T17:13:03.760Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-25T17:13:03.760Z",
  "sessionId": "6e8d5c3f-7c75-4ff9-a01f-f2df71411ac1"
}
```

---

## Round 1

93 recorded events

### User

_source line 3 · 2026-05-25T17:13:03.790Z_

项目：entrainment_gated_ft
Venue：emnlp-2026
论文目录：/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper

Phase 1 确定性检查结果：
源码检查: passed=False, 2 critical, 1 warning
一致性检查: 0 critical, 67 warning
编译: ✅, 页数: 21
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
  "promptId": "73d622e8-44a2-4ef1-8f25-89dbf02b8b7b",
  "type": "user",
  "uuid": "a750b1c5-65b5-4565-8dad-5d1eeab9d91b",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/sessions/paper_audit_content_6bc68a37",
  "sessionId": "6e8d5c3f-7c75-4ff9-a01f-f2df71411ac1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-25T17:13:03.790Z_

```json
{
  "parentUuid": "a750b1c5-65b5-4565-8dad-5d1eeab9d91b",
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
  "uuid": "3a5db2fb-b388-45d7-9b59-a751a0358fe0",
  "timestamp": "2026-05-25T17:13:03.790Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/sessions/paper_audit_content_6bc68a37",
  "sessionId": "6e8d5c3f-7c75-4ff9-a01f-f2df71411ac1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-25T17:13:03.790Z_

```json
{
  "parentUuid": "3a5db2fb-b388-45d7-9b59-a751a0358fe0",
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
  "uuid": "e0b9e81f-e684-4cc1-933d-6e939ec31ddc",
  "timestamp": "2026-05-25T17:13:03.790Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/sessions/paper_audit_content_6bc68a37",
  "sessionId": "6e8d5c3f-7c75-4ff9-a01f-f2df71411ac1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6 · 2026-05-25T17:13:03.790Z_

```json
{
  "parentUuid": "e0b9e81f-e684-4cc1-933d-6e939ec31ddc",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "4771205c-d547-4c75-abef-13404518b174",
  "timestamp": "2026-05-25T17:13:03.790Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/sessions/paper_audit_content_6bc68a37",
  "sessionId": "6e8d5c3f-7c75-4ff9-a01f-f2df71411ac1",
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
  "aiTitle": "EMNLP 2026 paper structure audit and compliance check",
  "sessionId": "6e8d5c3f-7c75-4ff9-a01f-f2df71411ac1"
}
```

---

### Assistant

_source line 8 · 2026-05-25T17:13:10.434Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to perform a content structure audit on a paper. Let me follow the execution flow:

1. Read the two skill files for audit standards
2. Read all .tex files in the paper directory
3. Audit across all dimensions
4. Output structured findings

Let me start by reading the skill files and finding the .tex files.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4771205c-d547-4c75-abef-13404518b174",
  "isSidechain": false,
  "requestId": "req_011CbPfK738wv2Cqq65s3Uya",
  "type": "assistant",
  "uuid": "dba8e6f9-9463-41a9-9b20-cf9094062c86",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/sessions/paper_audit_content_6bc68a37",
  "sessionId": "6e8d5c3f-7c75-4ff9-a01f-f2df71411ac1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AdSrLmfWkuocgbFtkxiFS5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 26438,
      "cache_read_input_tokens": 11846,
      "output_tokens": 338,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 26438,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 338,
          "cache_read_input_tokens": 11846,
          "cache_creation_input_tokens": 26438,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 26438
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

_source line 9 · 2026-05-25T17:13:10.660Z_

开始执行内容结构审计。先加载审计标准和论文源码。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dba8e6f9-9463-41a9-9b20-cf9094062c86",
  "isSidechain": false,
  "requestId": "req_011CbPfK738wv2Cqq65s3Uya",
  "type": "assistant",
  "uuid": "31dd0c51-2aa4-497e-8687-fa4f98a9e16a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/sessions/paper_audit_content_6bc68a37",
  "sessionId": "6e8d5c3f-7c75-4ff9-a01f-f2df71411ac1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AdSrLmfWkuocgbFtkxiFS5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 26438,
      "cache_read_input_tokens": 11846,
      "output_tokens": 338,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 26438,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 338,
          "cache_read_input_tokens": 11846,
          "cache_creation_input_tokens": 26438,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 26438
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

_source line 10 · 2026-05-25T17:13:11.793Z_

<details open><summary>🔧 Tool call — Read · `toolu_01CuKW44amnu225qR5f65rdT`</summary>

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
  "parentUuid": "31dd0c51-2aa4-497e-8687-fa4f98a9e16a",
  "isSidechain": false,
  "requestId": "req_011CbPfK738wv2Cqq65s3Uya",
  "type": "assistant",
  "uuid": "2d2d366c-1e29-4ba5-87fb-75b525bb2ba6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/sessions/paper_audit_content_6bc68a37",
  "sessionId": "6e8d5c3f-7c75-4ff9-a01f-f2df71411ac1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AdSrLmfWkuocgbFtkxiFS5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 26438,
      "cache_read_input_tokens": 11846,
      "output_tokens": 338,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 26438,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 338,
          "cache_read_input_tokens": 11846,
          "cache_creation_input_tokens": 26438,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 26438
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

_source line 11 · 2026-05-25T17:13:12.679Z_

<details><summary>↩ Tool result · `toolu_012VReUdBzbvTuaL5JB7bKyL`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/author_response.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/author_response_r7.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/arr_checklist.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/appendix.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/main.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/experiments.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "38f3605d-0cbd-4d18-8181-8b7ce5010c08",
  "isSidechain": false,
  "promptId": "73d622e8-44a2-4ef1-8f25-89dbf02b8b7b",
  "type": "user",
  "uuid": "6e9eea6f-dc7e-428d-a0f2-1061bba5230b",
  "toolUseResult": {
    "filenames": [
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/author_response.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/author_response_r7.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/arr_checklist.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/appendix.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/introduction.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/conclusion.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/related_work.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/main.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/method.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/experiments.tex"
    ],
    "durationMs": 17,
    "numFiles": 10,
    "truncated": false
  },
  "sourceToolAssistantUUID": "38f3605d-0cbd-4d18-8181-8b7ce5010c08",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/sessions/paper_audit_content_6bc68a37",
  "sessionId": "6e8d5c3f-7c75-4ff9-a01f-f2df71411ac1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-25T17:13:11.811Z_

<details><summary>↩ Tool result · `toolu_01CuKW44amnu225qR5f65rdT`</summary>

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
  "parentUuid": "2d2d366c-1e29-4ba5-87fb-75b525bb2ba6",
  "isSidechain": false,
  "promptId": "73d622e8-44a2-4ef1-8f25-89dbf02b8b7b",
  "type": "user",
  "uuid": "39f34079-199c-472a-92ef-b5d766a96066",
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
  "sourceToolAssistantUUID": "2d2d366c-1e29-4ba5-87fb-75b525bb2ba6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/sessions/paper_audit_content_6bc68a37",
  "sessionId": "6e8d5c3f-7c75-4ff9-a01f-f2df71411ac1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
````

</details>

---

### Tool call

_source line 13 · 2026-05-25T17:13:12.495Z_

<details open><summary>🔧 Tool call — Read · `toolu_01FUZq2Y2N4MQNnQXCWrZ7Gw`</summary>

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
  "parentUuid": "39f34079-199c-472a-92ef-b5d766a96066",
  "isSidechain": false,
  "requestId": "req_011CbPfK738wv2Cqq65s3Uya",
  "type": "assistant",
  "uuid": "787d8e41-85d5-41ed-858f-4323428461e3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/sessions/paper_audit_content_6bc68a37",
  "sessionId": "6e8d5c3f-7c75-4ff9-a01f-f2df71411ac1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AdSrLmfWkuocgbFtkxiFS5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 26438,
      "cache_read_input_tokens": 11846,
      "output_tokens": 338,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 26438,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 338,
          "cache_read_input_tokens": 11846,
          "cache_creation_input_tokens": 26438,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 26438
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

_source line 14 · 2026-05-25T17:13:12.510Z_

<details><summary>↩ Tool result · `toolu_01FUZq2Y2N4MQNnQXCWrZ7Gw`</summary>

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
  "parentUuid": "787d8e41-85d5-41ed-858f-4323428461e3",
  "isSidechain": false,
  "promptId": "73d622e8-44a2-4ef1-8f25-89dbf02b8b7b",
  "type": "user",
  "uuid": "fe6549f6-e33f-4e62-928c-6a207702655e",
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
  "sourceToolAssistantUUID": "787d8e41-85d5-41ed-858f-4323428461e3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/sessions/paper_audit_content_6bc68a37",
  "sessionId": "6e8d5c3f-7c75-4ff9-a01f-f2df71411ac1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
````

</details>

---

### Tool call

_source line 15 · 2026-05-25T17:13:12.651Z_

<details open><summary>🔧 Tool call — Glob · `toolu_012VReUdBzbvTuaL5JB7bKyL`</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fe6549f6-e33f-4e62-928c-6a207702655e",
  "isSidechain": false,
  "requestId": "req_011CbPfK738wv2Cqq65s3Uya",
  "type": "assistant",
  "uuid": "38f3605d-0cbd-4d18-8181-8b7ce5010c08",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/sessions/paper_audit_content_6bc68a37",
  "sessionId": "6e8d5c3f-7c75-4ff9-a01f-f2df71411ac1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AdSrLmfWkuocgbFtkxiFS5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 26438,
      "cache_read_input_tokens": 11846,
      "output_tokens": 338,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 26438,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 338,
          "cache_read_input_tokens": 11846,
          "cache_creation_input_tokens": 26438,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 26438
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
  "lastPrompt": "项目：entrainment_gated_ft Venue：emnlp-2026 论文目录：/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper  Phase 1 确定性检查结果： 源码检查: passed=False, 2 critical, 1 warning 一致性检查…",
  "leafUuid": "6e9eea6f-dc7e-428d-a0f2-1061bba5230b",
  "sessionId": "6e8d5c3f-7c75-4ff9-a01f-f2df71411ac1"
}
```

---

### Runtime record

_source line 17_

```json
{
  "type": "ai-title",
  "aiTitle": "EMNLP 2026 paper structure audit and compliance check",
  "sessionId": "6e8d5c3f-7c75-4ff9-a01f-f2df71411ac1"
}
```

---

### Assistant

_source line 18 · 2026-05-25T17:13:15.956Z_

<details><summary>Logged reasoning block</summary>

```text
Now I need to read all the .tex files. Let me read them in parallel. The key ones are main.tex, introduction.tex, method.tex, experiments.tex, conclusion.tex, related_work.tex, and appendix.tex. I'll also check author_response files but those aren't part of the paper itself.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6e9eea6f-dc7e-428d-a0f2-1061bba5230b",
  "isSidechain": false,
  "requestId": "req_011CbPfKm7MVoTWjRv9pw5TW",
  "type": "assistant",
  "uuid": "e247a9ad-d63d-4c07-897a-1c318fcc2404",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/sessions/paper_audit_content_6bc68a37",
  "sessionId": "6e8d5c3f-7c75-4ff9-a01f-f2df71411ac1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DyVargCTpxVeRwtzp3L3va",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12005,
      "cache_read_input_tokens": 38284,
      "output_tokens": 644,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12005,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 644,
          "cache_read_input_tokens": 38284,
          "cache_creation_input_tokens": 12005,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12005
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

_source line 19 · 2026-05-25T17:13:16.642Z_

读取所有论文 .tex 源码。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e247a9ad-d63d-4c07-897a-1c318fcc2404",
  "isSidechain": false,
  "requestId": "req_011CbPfKm7MVoTWjRv9pw5TW",
  "type": "assistant",
  "uuid": "4c20b527-fd80-43f8-a54a-a989cf9c8e4c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/sessions/paper_audit_content_6bc68a37",
  "sessionId": "6e8d5c3f-7c75-4ff9-a01f-f2df71411ac1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DyVargCTpxVeRwtzp3L3va",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12005,
      "cache_read_input_tokens": 38284,
      "output_tokens": 644,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12005,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 644,
          "cache_read_input_tokens": 38284,
          "cache_creation_input_tokens": 12005,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12005
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

_source line 20 · 2026-05-25T17:13:16.937Z_

<details open><summary>🔧 Tool call — Read · `toolu_01N9YPgv7aT7JYTwRGxyqkrg`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4c20b527-fd80-43f8-a54a-a989cf9c8e4c",
  "isSidechain": false,
  "requestId": "req_011CbPfKm7MVoTWjRv9pw5TW",
  "type": "assistant",
  "uuid": "d357d23e-5dab-4d5d-bbf9-6d8fcf44ced5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/sessions/paper_audit_content_6bc68a37",
  "sessionId": "6e8d5c3f-7c75-4ff9-a01f-f2df71411ac1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DyVargCTpxVeRwtzp3L3va",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12005,
      "cache_read_input_tokens": 38284,
      "output_tokens": 644,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12005,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 644,
          "cache_read_input_tokens": 38284,
          "cache_creation_input_tokens": 12005,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12005
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

_source line 21 · 2026-05-25T17:13:16.950Z_

<details><summary>↩ Tool result · `toolu_01N9YPgv7aT7JYTwRGxyqkrg`</summary>

```text
1	\documentclass[11pt]{article}
2	
3	\usepackage[review]{acl}
4	
5	\usepackage{times}
6	\usepackage{latexsym}
7	\usepackage[T1]{fontenc}
8	\usepackage[utf8]{inputenc}
9	\usepackage{microtype}
10	% \usepackage{inconsolata} % optional per official ACL template; not available in this TeX distribution
11	\usepackage{graphicx}
12	\usepackage{booktabs}
13	\usepackage{amsmath}
14	\usepackage{amssymb}
15	\usepackage{multirow}
16	\usepackage{enumitem}
17	\setlist[itemize]{itemsep=1pt, parsep=0pt, topsep=2pt}
18	
19	% Float and display spacing (tightened to meet 8-page main-text limit)
20	\setlength{\textfloatsep}{4pt plus 1pt minus 1pt}
21	\setlength{\floatsep}{4pt plus 1pt minus 1pt}
22	\setlength{\intextsep}{4pt plus 1pt minus 1pt}
23	\setlength{\abovecaptionskip}{2pt}
24	\setlength{\belowcaptionskip}{0pt}
25	\setlength{\dbltextfloatsep}{4pt plus 1pt minus 1pt}
26	\setlength{\dblfloatsep}{4pt plus 1pt minus 1pt}
27	\setlength{\abovedisplayskip}{4pt plus 1pt minus 1pt}
28	\setlength{\belowdisplayskip}{4pt plus 1pt minus 1pt}
29	
30	\title{Aggregate Equivalence $\neq$ Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models}
31	
32	\author{Anonymous}
33	
34	\begin{document}
35	\maketitle
36	
37	\begin{abstract}
38	Hybrid linear recurrent architectures that appear interchangeable by aggregate benchmarks can differ on which specific examples they handle correctly. Using a controlled model zoo \citep{wang2025hybrid} (three architectures, five attention ratios, two scales), we decompose per-example effects of adding attention and find structured predictive multiplicity \citep{marx2020predictive}: pairwise overlap of helped and hurt example sets is uniformly low (Jaccard $\approx 0.10$, roughly twice the independence baseline; all $p < .01$ across five architectures (three primary, two validation)). This multiplicity varies by task type or evaluation format ($\alpha = 0.14$--$0.30$) rather than attention ratio. Per-example overlap appears to stabilize at 4\% attention and remains flat across higher ratios, suggesting that minimal attention may establish which examples each architecture affects. \citet{yang2026benchmark} document analogous per-item disagreement (16--66\%) among frontier large language models (LLMs) despite comparable aggregate scores; our within-family design isolates backbone variation from training-regime differences. Confidence margins partially predict affected examples (area under the ROC curve [AUC] 0.70--0.74). Low cross-architecture overlap implies substantial complementarity, though routing-based exploitation remains task-dependent\footnote{Code and data are available at \url{https://anonymous.4open.science/r/entrainment_gated_ft-9444/}.}.
39	\end{abstract}
40	
41	\input{sections/introduction}
42	
43	\input{sections/related_work}
44	
45	\input{sections/method}
46	
47	\input{sections/experiments}
48	
49	\input{sections/conclusion}
50	
51	\section*{Limitations}
52	
53	\paragraph{Single training runs.} Each configuration is a single training run; consistency across all 40 architecture--benchmark combinations (all $p < .01$) and a $3\times$ within- vs.\ cross-architecture Jaccard gap (within-seed $J$ is 2.7--4.3$\times$ higher; Appendix~\ref{app:seed_calibration}) mitigate seed confounds but cannot fully resolve them.
54	
55	\paragraph{Format confound.} The confound between task type and evaluation format cannot be fully resolved: LAMBADA is the only free-form benchmark, so its higher $\alpha$ may reflect format differences rather than cognitive demands alone.
56	
57	\paragraph{Coverage.} We examine three primary architectures (plus two extended) from one model zoo, four main benchmarks, and two scale points. Generalization to Mamba, RWKV, other hybrid families, and generation tasks remains open; all four per-example benchmarks use discriminative scoring, so multiplicity under open-ended generation is untested. Results at larger scales (e.g., 7B+) may differ, particularly as attention mechanisms become more expressive with increased capacity.
58	
59	\paragraph{Pre-training only.} All evaluations use pretrained checkpoints without fine-tuning; per-example effects may not persist after task-specific adaptation. All evaluations use greedy decoding (the lm-eval-harness default); sampling strategies may alter per-example agreement patterns.
60	
61	\bibliography{references}
62	
63	\appendix
64	\input{sections/appendix}
65	
66	\end{document}
67	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d357d23e-5dab-4d5d-bbf9-6d8fcf44ced5",
  "isSidechain": false,
  "promptId": "73d622e8-44a2-4ef1-8f25-89dbf02b8b7b",
  "type": "user",
  "uuid": "39349ad5-178f-4755-a7ed-97c4ad8bd77d",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/main.tex",
      "content": "\\documentclass[11pt]{article}\n\n\\usepackage[review]{acl}\n\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage[T1]{fontenc}\n\\usepackage[utf8]{inputenc}\n\\usepackage{microtype}\n% \\usepackage{inconsolata} % optional per official ACL template; not available in this TeX distribution\n\\usepackage{graphicx}\n\\usepackage{booktabs}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{multirow}\n\\usepackage{enumitem}\n\\setlist[itemize]{itemsep=1pt, parsep=0pt, topsep=2pt}\n\n% Float and display spacing (tightened to meet 8-page main-text limit)\n\\setlength{\\textfloatsep}{4pt plus 1pt minus 1pt}\n\\setlength{\\floatsep}{4pt plus 1pt minus 1pt}\n\\setlength{\\intextsep}{4pt plus 1pt minus 1pt}\n\\setlength{\\abovecaptionskip}{2pt}\n\\setlength{\\belowcaptionskip}{0pt}\n\\setlength{\\dbltextfloatsep}{4pt plus 1pt minus 1pt}\n\\setlength{\\dblfloatsep}{4pt plus 1pt minus 1pt}\n\\setlength{\\abovedisplayskip}{4pt plus 1pt minus 1pt}\n\\setlength{\\belowdisplayskip}{4pt plus 1pt minus 1pt}\n\n\\title{Aggregate Equivalence $\\neq$ Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models}\n\n\\author{Anonymous}\n\n\\begin{document}\n\\maketitle\n\n\\begin{abstract}\nHybrid linear recurrent architectures that appear interchangeable by aggregate benchmarks can differ on which specific examples they handle correctly. Using a controlled model zoo \\citep{wang2025hybrid} (three architectures, five attention ratios, two scales), we decompose per-example effects of adding attention and find structured predictive multiplicity \\citep{marx2020predictive}: pairwise overlap of helped and hurt example sets is uniformly low (Jaccard $\\approx 0.10$, roughly twice the independence baseline; all $p < .01$ across five architectures (three primary, two validation)). This multiplicity varies by task type or evaluation format ($\\alpha = 0.14$--$0.30$) rather than attention ratio. Per-example overlap appears to stabilize at 4\\% attention and remains flat across higher ratios, suggesting that minimal attention may establish which examples each architecture affects. \\citet{yang2026benchmark} document analogous per-item disagreement (16--66\\%) among frontier large language models (LLMs) despite comparable aggregate scores; our within-family design isolates backbone variation from training-regime differences. Confidence margins partially predict affected examples (area under the ROC curve [AUC] 0.70--0.74). Low cross-architecture overlap implies substantial complementarity, though routing-based exploitation remains task-dependent\\footnote{Code and data are available at \\url{https://anonymous.4open.science/r/entrainment_gated_ft-9444/}.}.\n\\end{abstract}\n\n\\input{sections/introduction}\n\n\\input{sections/related_work}\n\n\\input{sections/method}\n\n\\input{sections/experiments}\n\n\\input{sections/conclusion}\n\n\\section*{Limitations}\n\n\\paragraph{Single training runs.} Each configuration is a single training run; consistency across all 40 architecture--benchmark combinations (all $p < .01$) and a $3\\times$ within- vs.\\ cross-architecture Jaccard gap (within-seed $J$ is 2.7--4.3$\\times$ higher; Appendix~\\ref{app:seed_calibration}) mitigate seed confounds but cannot fully resolve them.\n\n\\paragraph{Format confound.} The confound between task type and evaluation format cannot be fully resolved: LAMBADA is the only free-form benchmark, so its higher $\\alpha$ may reflect format differences rather than cognitive demands alone.\n\n\\paragraph{Coverage.} We examine three primary architectures (plus two extended) from one model zoo, four main benchmarks, and two scale points. Generalization to Mamba, RWKV, other hybrid families, and generation tasks remains open; all four per-example benchmarks use discriminative scoring, so multiplicity under open-ended generation is untested. Results at larger scales (e.g., 7B+) may differ, particularly as attention mechanisms become more expressive with increased capacity.\n\n\\paragraph{Pre-training only.} All evaluations use pretrained checkpoints without fine-tuning; per-example effects may not persist after task-specific adaptation. All evaluations use greedy decoding (the lm-eval-harness default); sampling strategies may alter per-example agreement patterns.\n\n\\bibliography{references}\n\n\\appendix\n\\input{sections/appendix}\n\n\\end{document}\n",
      "numLines": 67,
      "startLine": 1,
      "totalLines": 67
    }
  },
  "sourceToolAssistantUUID": "d357d23e-5dab-4d5d-bbf9-6d8fcf44ced5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/sessions/paper_audit_content_6bc68a37",
  "sessionId": "6e8d5c3f-7c75-4ff9-a01f-f2df71411ac1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-25T17:13:17.403Z_

<details open><summary>🔧 Tool call — Read · `toolu_01CysQNv32a3RQMo4L4pYp8n`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "39349ad5-178f-4755-a7ed-97c4ad8bd77d",
  "isSidechain": false,
  "requestId": "req_011CbPfKm7MVoTWjRv9pw5TW",
  "type": "assistant",
  "uuid": "fed2e77b-6726-449e-aa10-6584e7abcb52",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/sessions/paper_audit_content_6bc68a37",
  "sessionId": "6e8d5c3f-7c75-4ff9-a01f-f2df71411ac1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DyVargCTpxVeRwtzp3L3va",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12005,
      "cache_read_input_tokens": 38284,
      "output_tokens": 644,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12005,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 644,
          "cache_read_input_tokens": 38284,
          "cache_creation_input_tokens": 12005,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12005
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

_source line 23 · 2026-05-25T17:13:17.411Z_

<details><summary>↩ Tool result · `toolu_01CysQNv32a3RQMo4L4pYp8n`</summary>

```text
1	\section{Introduction}
2	
3	Hybrid linear recurrent architectures \citep[GatedDeltaNet, RetNet, HGRN2, GLA, DeltaNet;][]{yang2024gateddeltanet,sun2023retnet,qin2024hgrn2,yang2024gla,yang2024deltanet} achieve aggregate benchmark scores within 1--2 points of each other at matched parameter budgets, yet their helped and hurt example sets overlap by only ${\sim}10$\% (pairwise Jaccard $\approx 0.10$). This gap between aggregate equivalence and per-example behavioral equivalence is invisible in standard metrics: architectures that score similarly reach that score by gaining and losing on different inputs, and the choice of backbone carries hidden consequences for which specific examples a deployed system handles correctly.
4	
5	\begin{figure*}[t]
6	\centering
7	\begin{minipage}[t]{0.56\textwidth}
8	\centering
9	\includegraphics[width=\textwidth]{figures/fig1_decoupling_hero.pdf}
10	\end{minipage}%
11	\hfill
12	\begin{minipage}[t]{0.42\textwidth}
13	\centering
14	\includegraphics[width=\textwidth]{figures/fig4_jaccard_saturation.pdf}
15	\end{minipage}
16	\caption{Per-example overlap appears stable from minimal attention across benchmarks. (a,\,b) LAMBADA: cross-architecture $\sigma$ shows a non-significant decreasing trend at 1.3B (solid; Bonferroni-adjusted $p = .170$) but partially rebounds at 340M (dashed), while pairwise Jaccard of helped/hurt sets appears stable from 4\% attention onward. (c) This pattern holds across all four main benchmarks: mean pairwise $\bar{J}$ remains flat across attention ratios (all $\rho \leq 0.80$, $p \geq .333$). Shaded bands are illustrative ($n = 3$).}
17	\label{fig:decoupling}
18	\end{figure*}
19	
20	This tension arises in the context of a rapid architectural shift toward hybrid recurrent-attention models, which interleave attention layers within linear recurrent backbones. Jamba \citep{lieber2024jamba}, Griffin \citep{de2024griffin}, RWKV-6 \citep{peng2024eagle}, and RecurrentGemma \citep{botev2024recurrentgemma} each combine recurrence with attention using different mixing strategies. These systems now serve as production-grade alternatives to pure Transformers, and the practical question of how much attention to include is typically answered by comparing aggregate benchmark numbers. \citet{wang2025hybrid} provide a controlled model zoo spanning three recurrent architectures, five attention ratios, and two parameter scales, which enables systematic study of how attention allocation affects these hybrid designs.
21	
22	Prior work on predictive multiplicity \citep{marx2020predictive} and underspecification \citep{damour2022underspecification,mccoy2020berts} documents this risk for seed variation within a single architecture, but whether it extends to architectural variation in hybrid recurrent models remains open. If architectures that score similarly in aggregate behave differently on individual inputs, the backbone choice carries hidden consequences for deployment reliability and ensemble construction.
23	
24	We present the first controlled within-family per-example analysis of how attention affects cross-architecture agreement in hybrid recurrent models. Using the model zoo of \citet{wang2025hybrid}, we compare three architectures (GatedDeltaNet, RetNet, HGRN2) at five attention ratios (0--25\%) and two scales (340M, 1.3B). We evaluate all 30 configurations on 10 benchmarks spanning retrieval, comprehension, reasoning, and mixed categories. On four benchmarks (LAMBADA \citealp{paperno2016lambada}, $N = 5{,}153$; HellaSwag \citealp{zellers2019hellaswag}, $N = 10{,}042$; PIQA \citealp{bisk2020piqa}, $N = 1{,}838$; ARC-Easy \citealp{clark2018arc}, $N = 2{,}376$) we conduct per-example decompositions, classifying each example as helped, hurt, or unchanged when attention is added, and measure cross-architecture overlap via Jaccard similarity. Figure~\ref{fig:decoupling} previews our central finding: architectures that appear equivalent by aggregate benchmarks diverge systematically at the per-example level, and this divergence is established by minimal attention.
25	
26	Our central finding is that architectural variation produces structured predictive multiplicity whose magnitude depends on task type, not attention ratio. The ambiguity $\alpha$ \citep{marx2020predictive} ranges from 0.14 (PIQA) to 0.30 (LAMBADA), varies $2\times$ across task types but only 0.03 within each benchmark across attention ratios; pairwise Jaccard remains uniformly low ($\leq 0.10$, all $p < .01$ across all ten five-architecture pairs). A second finding is that per-example overlap appears to stabilize at the first attention level (4\%) and remains flat at higher ratios. Even on LAMBADA, where aggregate variance shows a non-significant decreasing trend ($\rho = -1.0$, Bonferroni-adjusted $p = .170$; at 1.3B only), per-example Jaccard does not change (\S\ref{ssec:decoupling}).
27	
28	Our contributions are as follows:
29	\begin{itemize}
30	    \item Architectural variation in hybrid recurrent models, controlled within a single model zoo sharing training data and hyperparameters, produces structured predictive multiplicity whose magnitude varies by task type (or evaluation format) rather than attention ratio (\S\ref{ssec:per_example}). Five-architecture validation confirms the pattern (\S\ref{ssec:robustness}; Appendix~\ref{app:extended_arch}).
31	    \item Per-example overlap appears to stabilize at the first attention level (4\%) across all four benchmarks: minimal attention may establish which examples each architecture affects, with no observed homogenization at higher ratios ($n = 5$ ratios; \S\ref{ssec:decoupling}).
32	    \item Pure-model confidence margins partially predict which examples attention will affect (AUC 0.70--0.74), with rescue thresholds architecture-invariant but disruption thresholds varying 47\% across architectures, constituting a second dimension of multiplicity beyond per-example disagreement (\S\ref{ssec:per_example}; Appendix~\ref{app:prediction_framework}).
33	\end{itemize}
34	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fed2e77b-6726-449e-aa10-6584e7abcb52",
  "isSidechain": false,
  "promptId": "73d622e8-44a2-4ef1-8f25-89dbf02b8b7b",
  "type": "user",
  "uuid": "6156618a-c184-4683-9e8f-ca9b0ec4e2f9",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/introduction.tex",
      "content": "\\section{Introduction}\n\nHybrid linear recurrent architectures \\citep[GatedDeltaNet, RetNet, HGRN2, GLA, DeltaNet;][]{yang2024gateddeltanet,sun2023retnet,qin2024hgrn2,yang2024gla,yang2024deltanet} achieve aggregate benchmark scores within 1--2 points of each other at matched parameter budgets, yet their helped and hurt example sets overlap by only ${\\sim}10$\\% (pairwise Jaccard $\\approx 0.10$). This gap between aggregate equivalence and per-example behavioral equivalence is invisible in standard metrics: architectures that score similarly reach that score by gaining and losing on different inputs, and the choice of backbone carries hidden consequences for which specific examples a deployed system handles correctly.\n\n\\begin{figure*}[t]\n\\centering\n\\begin{minipage}[t]{0.56\\textwidth}\n\\centering\n\\includegraphics[width=\\textwidth]{figures/fig1_decoupling_hero.pdf}\n\\end{minipage}%\n\\hfill\n\\begin{minipage}[t]{0.42\\textwidth}\n\\centering\n\\includegraphics[width=\\textwidth]{figures/fig4_jaccard_saturation.pdf}\n\\end{minipage}\n\\caption{Per-example overlap appears stable from minimal attention across benchmarks. (a,\\,b) LAMBADA: cross-architecture $\\sigma$ shows a non-significant decreasing trend at 1.3B (solid; Bonferroni-adjusted $p = .170$) but partially rebounds at 340M (dashed), while pairwise Jaccard of helped/hurt sets appears stable from 4\\% attention onward. (c) This pattern holds across all four main benchmarks: mean pairwise $\\bar{J}$ remains flat across attention ratios (all $\\rho \\leq 0.80$, $p \\geq .333$). Shaded bands are illustrative ($n = 3$).}\n\\label{fig:decoupling}\n\\end{figure*}\n\nThis tension arises in the context of a rapid architectural shift toward hybrid recurrent-attention models, which interleave attention layers within linear recurrent backbones. Jamba \\citep{lieber2024jamba}, Griffin \\citep{de2024griffin}, RWKV-6 \\citep{peng2024eagle}, and RecurrentGemma \\citep{botev2024recurrentgemma} each combine recurrence with attention using different mixing strategies. These systems now serve as production-grade alternatives to pure Transformers, and the practical question of how much attention to include is typically answered by comparing aggregate benchmark numbers. \\citet{wang2025hybrid} provide a controlled model zoo spanning three recurrent architectures, five attention ratios, and two parameter scales, which enables systematic study of how attention allocation affects these hybrid designs.\n\nPrior work on predictive multiplicity \\citep{marx2020predictive} and underspecification \\citep{damour2022underspecification,mccoy2020berts} documents this risk for seed variation within a single architecture, but whether it extends to architectural variation in hybrid recurrent models remains open. If architectures that score similarly in aggregate behave differently on individual inputs, the backbone choice carries hidden consequences for deployment reliability and ensemble construction.\n\nWe present the first controlled within-family per-example analysis of how attention affects cross-architecture agreement in hybrid recurrent models. Using the model zoo of \\citet{wang2025hybrid}, we compare three architectures (GatedDeltaNet, RetNet, HGRN2) at five attention ratios (0--25\\%) and two scales (340M, 1.3B). We evaluate all 30 configurations on 10 benchmarks spanning retrieval, comprehension, reasoning, and mixed categories. On four benchmarks (LAMBADA \\citealp{paperno2016lambada}, $N = 5{,}153$; HellaSwag \\citealp{zellers2019hellaswag}, $N = 10{,}042$; PIQA \\citealp{bisk2020piqa}, $N = 1{,}838$; ARC-Easy \\citealp{clark2018arc}, $N = 2{,}376$) we conduct per-example decompositions, classifying each example as helped, hurt, or unchanged when attention is added, and measure cross-architecture overlap via Jaccard similarity. Figure~\\ref{fig:decoupling} previews our central finding: architectures that appear equivalent by aggregate benchmarks diverge systematically at the per-example level, and this divergence is established by minimal attention.\n\nOur central finding is that architectural variation produces structured predictive multiplicity whose magnitude depends on task type, not attention ratio. The ambiguity $\\alpha$ \\citep{marx2020predictive} ranges from 0.14 (PIQA) to 0.30 (LAMBADA), varies $2\\times$ across task types but only 0.03 within each benchmark across attention ratios; pairwise Jaccard remains uniformly low ($\\leq 0.10$, all $p < .01$ across all ten five-architecture pairs). A second finding is that per-example overlap appears to stabilize at the first attention level (4\\%) and remains flat at higher ratios. Even on LAMBADA, where aggregate variance shows a non-significant decreasing trend ($\\rho = -1.0$, Bonferroni-adjusted $p = .170$; at 1.3B only), per-example Jaccard does not change (\\S\\ref{ssec:decoupling}).\n\nOur contributions are as follows:\n\\begin{itemize}\n    \\item Architectural variation in hybrid recurrent models, controlled within a single model zoo sharing training data and hyperparameters, produces structured predictive multiplicity whose magnitude varies by task type (or evaluation format) rather than attention ratio (\\S\\ref{ssec:per_example}). Five-architecture validation confirms the pattern (\\S\\ref{ssec:robustness}; Appendix~\\ref{app:extended_arch}).\n    \\item Per-example overlap appears to stabilize at the first attention level (4\\%) across all four benchmarks: minimal attention may establish which examples each architecture affects, with no observed homogenization at higher ratios ($n = 5$ ratios; \\S\\ref{ssec:decoupling}).\n    \\item Pure-model confidence margins partially predict which examples attention will affect (AUC 0.70--0.74), with rescue thresholds architecture-invariant but disruption thresholds varying 47\\% across architectures, constituting a second dimension of multiplicity beyond per-example disagreement (\\S\\ref{ssec:per_example}; Appendix~\\ref{app:prediction_framework}).\n\\end{itemize}\n",
      "numLines": 34,
      "startLine": 1,
      "totalLines": 34
    }
  },
  "sourceToolAssistantUUID": "fed2e77b-6726-449e-aa10-6584e7abcb52",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/sessions/paper_audit_content_6bc68a37",
  "sessionId": "6e8d5c3f-7c75-4ff9-a01f-f2df71411ac1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-25T17:13:18.340Z_

<details open><summary>🔧 Tool call — Read · `toolu_01QSD3iN4pW7T5KghwSMf11y`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6156618a-c184-4683-9e8f-ca9b0ec4e2f9",
  "isSidechain": false,
  "requestId": "req_011CbPfKm7MVoTWjRv9pw5TW",
  "type": "assistant",
  "uuid": "7391602a-ab9b-4dbf-846e-5dbea8c519e3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/sessions/paper_audit_content_6bc68a37",
  "sessionId": "6e8d5c3f-7c75-4ff9-a01f-f2df71411ac1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DyVargCTpxVeRwtzp3L3va",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12005,
      "cache_read_input_tokens": 38284,
      "output_tokens": 644,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12005,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 644,
          "cache_read_input_tokens": 38284,
          "cache_creation_input_tokens": 12005,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12005
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

_source line 25 · 2026-05-25T17:13:18.347Z_

<details><summary>↩ Tool result · `toolu_01QSD3iN4pW7T5KghwSMf11y`</summary>

```text
1	\section{Method}\label{sec:method}
2	
3	We describe the model configurations, evaluation benchmarks, and analytical framework used to measure how attention affects cross-architecture agreement at both aggregate and per-example levels.
4	
5	\begin{table}[t]
6	\centering
7	\small
8	\caption{Model zoo summary \citep{wang2025hybrid}. All configurations share training data, tokenizer, and hyperparameters; they differ only in backbone and attention ratio.}
9	\label{tab:model_zoo}
10	\begin{tabular}{@{}lll@{}}
11	\toprule
12	Architecture & Recurrence mechanism & Scales \\
13	\midrule
14	GatedDeltaNet & Gated delta rules & 340M, 1.3B \\
15	RetNet & Multi-scale exp.\ decay & 340M, 1.3B \\
16	HGRN2 & Gated state expansion & 340M, 1.3B \\
17	\midrule
18	\multicolumn{3}{@{}l@{}}{\footnotesize Attention ratios: 0\%, 4\%, 7.7\%, 14.3\%, 25\%} \\
19	\multicolumn{3}{@{}l@{}}{\footnotesize Extended (340M only): +GLA, +DeltaNet} \\
20	\bottomrule
21	\end{tabular}
22	\end{table}
23	
24	\subsection{Model Zoo}\label{ssec:model_zoo}
25	
26	We use the pretrained model zoo of \citet{wang2025hybrid} (Table~\ref{tab:model_zoo}), which provides controlled comparisons: GatedDeltaNet \citep{yang2024gateddeltanet}, RetNet \citep{sun2023retnet}, and HGRN2 \citep{qin2024hgrn2} at five attention ratios and two scales. The GDN 1.3B h3-1 configuration uses 16 attention heads vs.\ 32 for RetNet and HGRN2 (\S\ref{ssec:robustness}). We adopt the h$k$-1 notation: h3-1 = 25\% attention, h6-1 = 14.3\%, h12-1 = 7.7\%, h24-1 = 4\%. Within each scale, all models share identical training data, tokenizer, and hyperparameters, isolating architecture and attention configuration. The zoo also includes a Transformer baseline at both scales.
27	
28	\subsection{Task Taxonomy}\label{ssec:task_taxonomy}
29	
30	We evaluate on 10 benchmarks grouped into four categories defined by the primary cognitive demand of each task. This taxonomy (informal; not pre-registered) was fixed prior to analysis following standard categorizations in the evaluation literature \citep{arora2024zoology} and is treated as hypothesis-generating rather than confirmatory (see Appendix~\ref{app:benchmark_details} for the confirmatory/exploratory split), not derived post hoc from observed results. The categories test whether the effect of attention on cross-architecture variance depends on task type.
31	
32	\begin{itemize}
33	    \item \textbf{Retrieval}: LAMBADA \citep{paperno2016lambada}, which requires predicting a final word from long-range context without reasoning or world knowledge.
34	    \item \textbf{Comprehension}: BoolQ \citep{clark2019boolq}, a reading comprehension task with yes/no answers.
35	    \item \textbf{Reasoning}: HellaSwag \citep{zellers2019hellaswag}, ARC-Challenge \citep{clark2018arc}, WinoGrande \citep{sakaguchi2021winogrande}, and PIQA \citep{bisk2020piqa}. COPA \citep{roemmele2011copa} ($n = 100$) is supplementary; its small sample renders $\alpha$ unreliable (Appendix~\ref{app:subsample_sensitivity}).
36	    \item \textbf{Mixed}: ARC-Easy \citep{clark2018arc}, MMLU \citep{hendrycks2021mmlu}, SciQ \citep{welbl2017sciq}, and XStoryCloze \citep{lin2022xstorycloze}, which combine retrieval, comprehension, and reasoning demands.
37	\end{itemize}
38	
39	LAMBADA is the only free-form generation benchmark in our evaluation; all others use multiple-choice scoring. Its higher $\alpha$ (0.30 vs.\ 0.14--0.21 for multiple-choice tasks) may partly reflect the larger answer space inherent to open-ended prediction, and the multiple-choice format may mechanically constrain per-example divergence by limiting the number of distinct error patterns. We cannot fully disentangle task type from evaluation format with the present benchmarks. However, within multiple-choice tasks, format (two-way vs.\ four-way) does not predict $\alpha$ (\S\ref{ssec:per_example}), suggesting that format alone does not drive the observed variation.
40	
41	All evaluations use lm-evaluation-harness v0.4.x \citep{gao2024lmeval} with default prompts and greedy decoding; accuracy serves as the primary metric for all benchmarks. Bootstrap analyses use random seed 42 throughout.
42	
43	\subsection{Convergence Metrics}\label{ssec:convergence_metrics}
44	
45	We quantify cross-architecture agreement as a function of attention ratio. For each benchmark and attention ratio, we compute the cross-architecture standard deviation $\sigma$ over the three architectures' accuracy scores. To measure the relationship between attention and convergence, we compute the Spearman rank correlation $\rho$ between attention ratio rank and $\sigma$ across the five attention configurations ($n = 5$). A negative $\rho$ indicates that higher attention ratios are associated with lower cross-architecture variance.
46	
47	We also report the convergence ratio $\sigma_{\text{pure}} / \sigma_{\text{h3-1}}$, defined as the standard deviation under the pure-recurrent configuration divided by that under the highest attention ratio (25\%). Values greater than 1 indicate that higher attention ratios are associated with lower cross-architecture variance.
48	
49	\begin{figure}[t]
50	\centering
51	\includegraphics[width=\columnwidth]{figures/fig_method_overview.pdf}
52	\caption{Experimental framework. For each architecture, we compare the pure-recurrent baseline against its hybrid (+attention) variant, classifying every evaluation example as helped, hurt, or unchanged. Cross-architecture overlap of these per-example effect sets is measured via pairwise Jaccard similarity ($J \approx 0.10$), revealing architecture-specific sensitivity patterns.}
53	\label{fig:method_overview}
54	\end{figure}
55	
56	\subsection{Per-Example Decomposition}\label{ssec:per_example_decomposition}
57	
58	We decompose performance changes at the individual-example level on four benchmarks spanning three task categories: LAMBADA (5{,}153 examples; retrieval), HellaSwag (10{,}042; reasoning), PIQA (1{,}838; reasoning, two-choice), and ARC-Easy (2{,}376; mixed). HellaSwag uses normalized accuracy (acc\_norm) as the per-example correctness criterion. Supplementary analyses on BoolQ (3{,}270) and WinoGrande (1{,}267) appear in Appendix~\ref{app:boolq} and \ref{app:winogrande}. For each architecture, we compare the pure-recurrent baseline against its h3-1 hybrid (25\% attention), which maximizes the recurrent--hybrid contrast; \S\ref{ssec:per_example} confirms that $\alpha$ is stable across intermediate ratios (variation $< 0.03$). Each example is classified as:
59	
60	\begin{itemize}
61	    \item \textbf{Helped}: correct in the hybrid but incorrect in the pure model.
62	    \item \textbf{Hurt}: correct in the pure model but incorrect in the hybrid.
63	    \item \textbf{Unchanged}: both models agree (both correct or both incorrect).
64	\end{itemize}
65	
66	The net effect for each architecture is $|\text{helped}| - |\text{hurt}|$. A positive net effect means more examples transition to correct than to incorrect when attention is added; a negative net effect means the opposite.
67	
68	To measure cross-architecture overlap, we compute the pairwise Jaccard similarity $J = |A \cap B| / |A \cup B|$ between the helped sets of two architectures and, separately, between their hurt sets. $J = 1$ indicates identical sets; $J = 0$ indicates no overlap. On $K$-choice tasks, binarization collapses $K{-}1$ wrong answers into a single ``incorrect'' category, potentially counting architectures as agreeing (both wrong) when they select different wrong answers. This conservative bias strengthens the multiplicity claim: true divergence may exceed what binary Jaccard captures. Appendix~\ref{app:continuous_jaccard} confirms robustness under continuous Jaccard similarity.
69	
70	\subsection{Statistical Methods}\label{ssec:statistical_methods}
71	
72	All tests are two-tailed. Spearman $\rho$ uses exact permutation tests ($5! = 120$ permutations); with $n = 5$, only $|\rho| = 1.0$ achieves $p < .05$ ($p = .017$), so all Spearman-based inferences are descriptive and exploratory. Bonferroni correction spans all 10 benchmarks (adjusted threshold $\alpha / 10 = 0.005$). Bootstrap 95\% bias-corrected and accelerated (BCa) confidence intervals use 10{,}000 resamples; with $n = 3$ architectures, these are heuristic indicators of effect direction. Within-architecture comparisons use Mann-Whitney U; cross-architecture comparisons use Kruskal-Wallis. Attention weight analysis extracts per-layer cosine similarity and Shannon entropy via forward hooks (Appendix~\ref{app:attention_patterns}). The permutation null does not condition on item difficulty; if difficulty-driven correlations inflate observed Jaccard while permutation destroys this structure, the test may be anti-conservative. However, the ${\sim}2.5\times$ observed-to-null ratio (all $z > 5.9$) provides substantial margin against this bias.
73	
74	\begin{figure}[t]
75	\centering
76	\includegraphics[width=\columnwidth]{figures/fig_per_example_bars.pdf}
77	\caption{Per-example effects of adding attention (pure $\to$ h3-1) on LAMBADA (1.3B). Helped: correct only with attention; hurt: correct only without. HGRN2 shows the only net positive effect; overlap is minimal ($\bar{J} \leq 0.10$, all $p < .0001$).}
78	\label{fig:per_example_bars}
79	\end{figure}
80	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7391602a-ab9b-4dbf-846e-5dbea8c519e3",
  "isSidechain": false,
  "promptId": "73d622e8-44a2-4ef1-8f25-89dbf02b8b7b",
  "type": "user",
  "uuid": "94505d94-db88-472d-9e14-192c2f8e56dd",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/method.tex",
      "content": "\\section{Method}\\label{sec:method}\n\nWe describe the model configurations, evaluation benchmarks, and analytical framework used to measure how attention affects cross-architecture agreement at both aggregate and per-example levels.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Model zoo summary \\citep{wang2025hybrid}. All configurations share training data, tokenizer, and hyperparameters; they differ only in backbone and attention ratio.}\n\\label{tab:model_zoo}\n\\begin{tabular}{@{}lll@{}}\n\\toprule\nArchitecture & Recurrence mechanism & Scales \\\\\n\\midrule\nGatedDeltaNet & Gated delta rules & 340M, 1.3B \\\\\nRetNet & Multi-scale exp.\\ decay & 340M, 1.3B \\\\\nHGRN2 & Gated state expansion & 340M, 1.3B \\\\\n\\midrule\n\\multicolumn{3}{@{}l@{}}{\\footnotesize Attention ratios: 0\\%, 4\\%, 7.7\\%, 14.3\\%, 25\\%} \\\\\n\\multicolumn{3}{@{}l@{}}{\\footnotesize Extended (340M only): +GLA, +DeltaNet} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Model Zoo}\\label{ssec:model_zoo}\n\nWe use the pretrained model zoo of \\citet{wang2025hybrid} (Table~\\ref{tab:model_zoo}), which provides controlled comparisons: GatedDeltaNet \\citep{yang2024gateddeltanet}, RetNet \\citep{sun2023retnet}, and HGRN2 \\citep{qin2024hgrn2} at five attention ratios and two scales. The GDN 1.3B h3-1 configuration uses 16 attention heads vs.\\ 32 for RetNet and HGRN2 (\\S\\ref{ssec:robustness}). We adopt the h$k$-1 notation: h3-1 = 25\\% attention, h6-1 = 14.3\\%, h12-1 = 7.7\\%, h24-1 = 4\\%. Within each scale, all models share identical training data, tokenizer, and hyperparameters, isolating architecture and attention configuration. The zoo also includes a Transformer baseline at both scales.\n\n\\subsection{Task Taxonomy}\\label{ssec:task_taxonomy}\n\nWe evaluate on 10 benchmarks grouped into four categories defined by the primary cognitive demand of each task. This taxonomy (informal; not pre-registered) was fixed prior to analysis following standard categorizations in the evaluation literature \\citep{arora2024zoology} and is treated as hypothesis-generating rather than confirmatory (see Appendix~\\ref{app:benchmark_details} for the confirmatory/exploratory split), not derived post hoc from observed results. The categories test whether the effect of attention on cross-architecture variance depends on task type.\n\n\\begin{itemize}\n    \\item \\textbf{Retrieval}: LAMBADA \\citep{paperno2016lambada}, which requires predicting a final word from long-range context without reasoning or world knowledge.\n    \\item \\textbf{Comprehension}: BoolQ \\citep{clark2019boolq}, a reading comprehension task with yes/no answers.\n    \\item \\textbf{Reasoning}: HellaSwag \\citep{zellers2019hellaswag}, ARC-Challenge \\citep{clark2018arc}, WinoGrande \\citep{sakaguchi2021winogrande}, and PIQA \\citep{bisk2020piqa}. COPA \\citep{roemmele2011copa} ($n = 100$) is supplementary; its small sample renders $\\alpha$ unreliable (Appendix~\\ref{app:subsample_sensitivity}).\n    \\item \\textbf{Mixed}: ARC-Easy \\citep{clark2018arc}, MMLU \\citep{hendrycks2021mmlu}, SciQ \\citep{welbl2017sciq}, and XStoryCloze \\citep{lin2022xstorycloze}, which combine retrieval, comprehension, and reasoning demands.\n\\end{itemize}\n\nLAMBADA is the only free-form generation benchmark in our evaluation; all others use multiple-choice scoring. Its higher $\\alpha$ (0.30 vs.\\ 0.14--0.21 for multiple-choice tasks) may partly reflect the larger answer space inherent to open-ended prediction, and the multiple-choice format may mechanically constrain per-example divergence by limiting the number of distinct error patterns. We cannot fully disentangle task type from evaluation format with the present benchmarks. However, within multiple-choice tasks, format (two-way vs.\\ four-way) does not predict $\\alpha$ (\\S\\ref{ssec:per_example}), suggesting that format alone does not drive the observed variation.\n\nAll evaluations use lm-evaluation-harness v0.4.x \\citep{gao2024lmeval} with default prompts and greedy decoding; accuracy serves as the primary metric for all benchmarks. Bootstrap analyses use random seed 42 throughout.\n\n\\subsection{Convergence Metrics}\\label{ssec:convergence_metrics}\n\nWe quantify cross-architecture agreement as a function of attention ratio. For each benchmark and attention ratio, we compute the cross-architecture standard deviation $\\sigma$ over the three architectures' accuracy scores. To measure the relationship between attention and convergence, we compute the Spearman rank correlation $\\rho$ between attention ratio rank and $\\sigma$ across the five attention configurations ($n = 5$). A negative $\\rho$ indicates that higher attention ratios are associated with lower cross-architecture variance.\n\nWe also report the convergence ratio $\\sigma_{\\text{pure}} / \\sigma_{\\text{h3-1}}$, defined as the standard deviation under the pure-recurrent configuration divided by that under the highest attention ratio (25\\%). Values greater than 1 indicate that higher attention ratios are associated with lower cross-architecture variance.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_method_overview.pdf}\n\\caption{Experimental framework. For each architecture, we compare the pure-recurrent baseline against its hybrid (+attention) variant, classifying every evaluation example as helped, hurt, or unchanged. Cross-architecture overlap of these per-example effect sets is measured via pairwise Jaccard similarity ($J \\approx 0.10$), revealing architecture-specific sensitivity patterns.}\n\\label{fig:method_overview}\n\\end{figure}\n\n\\subsection{Per-Example Decomposition}\\label{ssec:per_example_decomposition}\n\nWe decompose performance changes at the individual-example level on four benchmarks spanning three task categories: LAMBADA (5{,}153 examples; retrieval), HellaSwag (10{,}042; reasoning), PIQA (1{,}838; reasoning, two-choice), and ARC-Easy (2{,}376; mixed). HellaSwag uses normalized accuracy (acc\\_norm) as the per-example correctness criterion. Supplementary analyses on BoolQ (3{,}270) and WinoGrande (1{,}267) appear in Appendix~\\ref{app:boolq} and \\ref{app:winogrande}. For each architecture, we compare the pure-recurrent baseline against its h3-1 hybrid (25\\% attention), which maximizes the recurrent--hybrid contrast; \\S\\ref{ssec:per_example} confirms that $\\alpha$ is stable across intermediate ratios (variation $< 0.03$). Each example is classified as:\n\n\\begin{itemize}\n    \\item \\textbf{Helped}: correct in the hybrid but incorrect in the pure model.\n    \\item \\textbf{Hurt}: correct in the pure model but incorrect in the hybrid.\n    \\item \\textbf{Unchanged}: both models agree (both correct or both incorrect).\n\\end{itemize}\n\nThe net effect for each architecture is $|\\text{helped}| - |\\text{hurt}|$. A positive net effect means more examples transition to correct than to incorrect when attention is added; a negative net effect means the opposite.\n\nTo measure cross-architecture overlap, we compute the pairwise Jaccard similarity $J = |A \\cap B| / |A \\cup B|$ between the helped sets of two architectures and, separately, between their hurt sets. $J = 1$ indicates identical sets; $J = 0$ indicates no overlap. On $K$-choice tasks, binarization collapses $K{-}1$ wrong answers into a single ``incorrect'' category, potentially counting architectures as agreeing (both wrong) when they select different wrong answers. This conservative bias strengthens the multiplicity claim: true divergence may exceed what binary Jaccard captures. Appendix~\\ref{app:continuous_jaccard} confirms robustness under continuous Jaccard similarity.\n\n\\subsection{Statistical Methods}\\label{ssec:statistical_methods}\n\nAll tests are two-tailed. Spearman $\\rho$ uses exact permutation tests ($5! = 120$ permutations); with $n = 5$, only $|\\rho| = 1.0$ achieves $p < .05$ ($p = .017$), so all Spearman-based inferences are descriptive and exploratory. Bonferroni correction spans all 10 benchmarks (adjusted threshold $\\alpha / 10 = 0.005$). Bootstrap 95\\% bias-corrected and accelerated (BCa) confidence intervals use 10{,}000 resamples; with $n = 3$ architectures, these are heuristic indicators of effect direction. Within-architecture comparisons use Mann-Whitney U; cross-architecture comparisons use Kruskal-Wallis. Attention weight analysis extracts per-layer cosine similarity and Shannon entropy via forward hooks (Appendix~\\ref{app:attention_patterns}). The permutation null does not condition on item difficulty; if difficulty-driven correlations inflate observed Jaccard while permutation destroys this structure, the test may be anti-conservative. However, the ${\\sim}2.5\\times$ observed-to-null ratio (all $z > 5.9$) provides substantial margin against this bias.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_per_example_bars.pdf}\n\\caption{Per-example effects of adding attention (pure $\\to$ h3-1) on LAMBADA (1.3B). Helped: correct only with attention; hurt: correct only without. HGRN2 shows the only net positive effect; overlap is minimal ($\\bar{J} \\leq 0.10$, all $p < .0001$).}\n\\label{fig:per_example_bars}\n\\end{figure}\n",
      "numLines": 80,
      "startLine": 1,
      "totalLines": 80
    }
  },
  "sourceToolAssistantUUID": "7391602a-ab9b-4dbf-846e-5dbea8c519e3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/sessions/paper_audit_content_6bc68a37",
  "sessionId": "6e8d5c3f-7c75-4ff9-a01f-f2df71411ac1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-25T17:13:18.831Z_

<details open><summary>🔧 Tool call — Read · `toolu_01EdtfngByZwT8zthSxb3Qm1`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "94505d94-db88-472d-9e14-192c2f8e56dd",
  "isSidechain": false,
  "requestId": "req_011CbPfKm7MVoTWjRv9pw5TW",
  "type": "assistant",
  "uuid": "8071fcb2-75db-46e7-8d89-331d27c12aab",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/sessions/paper_audit_content_6bc68a37",
  "sessionId": "6e8d5c3f-7c75-4ff9-a01f-f2df71411ac1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DyVargCTpxVeRwtzp3L3va",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12005,
      "cache_read_input_tokens": 38284,
      "output_tokens": 644,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12005,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 644,
          "cache_read_input_tokens": 38284,
          "cache_creation_input_tokens": 12005,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12005
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

_source line 27 · 2026-05-25T17:13:18.835Z_

<details><summary>↩ Tool result · `toolu_01EdtfngByZwT8zthSxb3Qm1`</summary>

```text
1	\section{Experiments}\label{sec:experiments}
2	
3	Using the model zoo of \citet{wang2025hybrid} (\S\ref{ssec:model_zoo}), we evaluate all 30 configurations on 10 benchmarks plus supplementary COPA ($n = 100$) at 1.3B scale unless noted. Results at 340M appear in scale analyses. Recall: h$k$-1 denotes one attention layer per $k{+}1$ layers; h3-1 = 25\% attention.
4	
5	\subsection{Per-Example Divergence}\label{ssec:per_example}
6	
7	Do architectures converge by improving on the same examples? We compare each architecture's pure-recurrent baseline against its h3-1 hybrid on 5{,}153 LAMBADA examples, classifying each as helped, hurt, or unchanged. Although the decomposition is binary, it captures genuine separation in the continuous confidence space (Cohen's $d = 0.73$--$0.92$ between helped and hurt on LAMBADA; cross-benchmark details in Appendix~\ref{app:cm_cross}). Binarization discards confidence magnitude, so we supplement with continuous confidence margin analysis (Appendix~\ref{app:confidence_margin}) and verify that low Jaccard persists under continuous thresholds (Appendix~\ref{app:continuous_jaccard}).
8	
9	\begin{figure}[t]
10	\centering
11	\includegraphics[width=\columnwidth]{figures/fig_jaccard_hierarchy.pdf}
12	\caption{Jaccard hierarchy on LAMBADA (1.3B). Cross-architecture overlap ($\bar{J} \approx 0.09$) is $2\times$ the independence baseline but only one-third of within-architecture overlap ($\bar{J} \approx 0.33$). Pythia 70M within-seed Jaccard (different scale) falls at a comparable level. Error bars show the helped--hurt range.}
13	\label{fig:jaccard_hierarchy}
14	\end{figure}
15	
16	\begin{figure*}[t]
17	\centering
18	\includegraphics[width=0.75\textwidth]{figures/fig3_alpha_routing.pdf}
19	\caption{(a) Per-example ambiguity $\alpha$ varies $2\times$ across task types. (b) Confidence-based routing gains track $\alpha$: effective when multiplicity is high (LAMBADA) but counterproductive when low (PIQA). 1.3B, h3-1.}
20	\label{fig:alpha_routing}
21	\end{figure*}
22	
23	Each architecture displays a distinct profile of per-example changes (Figure~\ref{fig:per_example_bars}). GDN loses a net 153 examples (462 helped, 615 hurt), RetNet loses 69 (426/495), and HGRN2 gains 153 (548/395; full counts in Appendix~\ref{app:per_example_counts}). HGRN2 is the only architecture for which adding attention yields a net per-example benefit. Pairwise Jaccard similarity is low: mean $\bar{J} \leq 0.10$, indicating ${\sim}90$\% non-overlap. Overlap significantly exceeds the independence baseline ($J_{\text{null}} \approx 0.05$, all $z > 5.9$, $p < .0001$; Appendix~\ref{app:jaccard_permutation}), plausibly reflecting shared sensitivity to example difficulty. Normalizing by $J_{\max}$, observed overlap reaches only 6--7\% of the achievable range above chance (Appendix~\ref{app:normalized_es}), confirming that low Jaccard cannot be attributed to set-size constraints.
24	
25	
26	\paragraph{Confidence margin predictor.} Pure-model confidence on the target token predicts which examples will be affected (AUC 0.70--0.74, a non-parametric measure equivalent to Mann-Whitney $U$; Appendix~\ref{app:confidence_margin}): rescue thresholds are architecture-invariant (1\% spread) but disruption thresholds vary 47\%, explaining cross-architecture Jaccard divergence (Appendix~\ref{app:prediction_framework}). Calibration differences account for less than half the threshold spread (Appendix~\ref{app:calibration}). The rescue pattern generalizes across three benchmarks ($d = 0.13$--$0.60$; Appendix~\ref{app:cm_cross}); disruption is weaker on reasoning tasks (Appendix~\ref{app:boolq}). This structured disagreement constitutes predictive multiplicity \citep{marx2020predictive} under architectural variation.
27	
28	\paragraph{Confidence-based routing.} As an illustrative case study, the rescue-threshold asymmetry suggests a routing strategy: select the architecture whose pure-model confidence best predicts successful rescue. On LAMBADA, this outperforms majority vote by $+5.3$\,pp (SD $= 0.4$\,pp, 10 cross-validated splits), extracting 36\% of the oracle gap (oracle = 65.5\%; Appendix~\ref{app:complementarity}). On ARC-Easy, gains are modest ($+1.0$\,pp, SD $= 0.5$\,pp); on HellaSwag, routing provides no benefit ($-0.02$\,pp, $p = .89$); on PIQA, it is significantly negative ($-0.6$\,pp, $p = .006$). Routing works when multiplicity is high ($\alpha = 0.30$, LAMBADA) and a clear rescue-threshold signal exists, but is counterproductive when multiplicity is low ($\alpha = 0.14$, PIQA). A natural comparison (average-logits ensemble) is left to future work as it requires simultaneous inference across all architectures.
29	
30	\paragraph{Multiplicity variation.} Extending to HellaSwag ($N = 10{,}042$) and PIQA ($N = 1{,}838$) reveals that multiplicity varies systematically across tasks (Table~\ref{tab:multiplicity}). Ambiguity $\alpha$ \citep{marx2020predictive} ranges from 0.14 (PIQA) through 0.15 (HellaSwag) and 0.21 (ARC-Easy; Appendix~\ref{app:arceasy}) to 0.30 (LAMBADA). Format does not drive this ordering: HellaSwag (four-way) and PIQA (two-choice) produce nearly identical $\alpha$ despite different answer-space sizes ($\rho = -0.60$, $p = .24$ with task accuracy). This suggests multiplicity is associated with cognitive demands rather than evaluation format, though the confound cannot be fully resolved (Limitations). Bootstrap 95\% CIs confirm the ordering (all non-overlapping except PIQA--HellaSwag; Table~\ref{tab:arceasy_ambiguity}). Pairwise Jaccard remains uniformly low ($\bar{J} \leq 0.10$, all $p < .01$), indicating architectures affect different examples regardless of how many are affected. Within each benchmark, $\alpha$ is stable across attention ratios (variation $< 0.03$) but differs $2\times$ across task types, confirming that multiplicity magnitude depends on task, not attention ratio \citep[cf.][]{gorbett2026crossmodel}.
31	
32	\begin{figure}[t]
33	\centering
34	\includegraphics[width=\columnwidth]{figures/fig2_task_specificity.pdf}
35	\caption{Spearman $\rho$ between attention ratio and cross-architecture $\sigma$ for each benchmark at 1.3B scale. LAMBADA ($\rho = -1.0$; BCa 95\% CI $[-1.0,\,-0.7]$, heuristic) is the only benchmark whose CI excludes zero. Bootstrap CI is heuristic given $n = 3$ architectures.}
36	\label{fig:task_specificity}
37	\end{figure}
38	
39	\begin{figure*}[t]
40	\centering
41	\includegraphics[width=0.75\textwidth]{figures/jaccard_heatmap_5arch.pdf}
42	\caption{Pairwise Jaccard heatmap across five architectures (340M, h3-1), where helped (hurt) examples are those correct only with (without) attention. Upper triangle: $J_{\text{helped}}$; lower triangle: $J_{\text{hurt}}$. All values $\leq 0.14$, all permutation tests $p \leq .002$. HellaSwag and PIQA results in Appendix~\ref{app:extended_arch}.}
43	\label{fig:jaccard_heatmap_5arch}
44	\end{figure*}
45	
46	\begin{table}[t]
47	\centering
48	\small
49	\caption{Predictive multiplicity at 1.3B, h3-1. $\alpha$: ambiguity \citep{marx2020predictive}; $\bar{J}$: mean pairwise Jaccard of helped~(h) / hurt~(u) sets; $\rho_\alpha$: Spearman $\rho$ of $\alpha$ vs.\ attention ratio.}
50	\label{tab:multiplicity}
51	\vspace{1pt}
52	\begin{tabular}{@{}lrcccc@{}}
53	\toprule
54	 & $N$ & $\alpha$ & $\bar{J}_{h}$ & $\bar{J}_{u}$ & $\rho_\alpha$ \\
55	\midrule
56	PIQA & 1838 & .14 & .091 & .094 & $0.0$ \\
57	HellaSwag & 10042 & .15 & .095 & .085 & $0.1$ \\
58	ARC-Easy & 2376 & .21 & .092 & .099 & $-0.2$ \\
59	LAMBADA & 5153 & .30 & .096 & .091 & $-0.6$ \\
60	\bottomrule
61	\end{tabular}
62	\par\vspace{2pt}
63	{\footnotesize Within-benchmark $\alpha$ variation $< 0.03$ across ratios. BoolQ, WinoGrande: Appendix~\ref{app:boolq}, \ref{app:winogrande}.}
64	\vspace{-4pt}
65	\end{table}
66	
67	\begin{table*}[t]
68	\centering
69	\caption{Cross-architecture variance trends across benchmarks (1.3B scale). $\rho$: Spearman correlation between attention ratio and cross-architecture standard deviation $\sigma$ across five configurations. $p$: exact permutation test (two-tailed, 120 permutations). $\sigma$ values reported $\times 10^{2}$ (accuracy percentage points). Ratio: $\sigma_{\text{pure}} / \sigma_{\text{h3-1}}$. \textbf{Bold}: only benchmark with $\rho = -1.0$. HellaSwag evaluated using normalized accuracy (acc\_norm), the standard metric for this benchmark.}
70	\label{tab:convergence}
71	\small
72	\setlength{\tabcolsep}{3.5pt}
73	\begin{tabular}{@{}llrrrrr@{}}
74	\toprule
75	Benchmark & Category & $\rho$ & $p$ & $\sigma_{\text{pure}}$ & $\sigma_{\text{h3-1}}$ & Ratio \\
76	\midrule
77	\textbf{LAMBADA$^{\ddagger}$} & \textbf{Retrieval} & $\mathbf{-1.0}$ & \textbf{.017} & \textbf{2.41} & \textbf{0.49} & \textbf{4.87} \\
78	\quad\emph{(excl.\ GDN)} & & $-0.7$ & .233 & --- & --- & --- \\
79	BoolQ & Comprehension & $0.2$ & .783 & 1.63 & 2.36 & 0.69 \\
80	ARC-C & Reasoning & $0.6$ & .350 & 0.96 & 1.32 & 0.72 \\
81	HellaSwag & Reasoning & $0.3$ & .683 & 1.17 & 1.18 & 0.99 \\
82	PIQA & Reasoning & $-0.5$ & .450 & 0.54 & 0.34 & 1.59 \\
83	WinoGrande & Reasoning & $0.1$ & .950 & 0.67 & 0.78 & 0.86 \\
84	ARC-E & Mixed & $-0.7$ & .233 & 1.00 & 0.13 & 7.70 \\
85	MMLU & Mixed & $-0.7$ & .233 & 0.92 & 0.41 & 2.27 \\
86	SciQ & Mixed & $0.1$ & .950 & 0.87 & 0.74 & 1.19 \\
87	XStoryCloze & Mixed & $-0.6$ & .350 & 0.82 & 0.55 & 1.49 \\
88	\midrule
89	COPA$^{\dagger}$ & Reasoning & $-0.67$ & .267 & 2.63 & 0.47 & 5.57 \\
90	\bottomrule
91	\multicolumn{7}{l}{\footnotesize $^{\dagger}$Supplementary ($n = 100$); excluded from multiple comparison correction.} \\
92	\multicolumn{7}{l}{\footnotesize $^{\ddagger}$GDN h3-1 uses 16 attention heads; all other configurations use 32 (\S\ref{ssec:robustness}).} \\
93	\multicolumn{7}{@{}p{\textwidth}@{}}{\footnotesize Bonferroni-adjusted $p = .170$. \textbf{Power: only $|\rho| = 1.0$ achieves $p < .05$ at $n = 5$.} Excl.\ GDN reverses MMLU $\rho$ to $+0.6$ (\S\ref{ssec:robustness}).}
94	\end{tabular}
95	\vspace{-4pt}
96	\end{table*}
97	
98	\vspace{-2pt}
99	\subsection{Per-Example Overlap Appears Stable from Minimal Attention}\label{ssec:decoupling}
100	
101	Having established that multiplicity varies by task type, we now ask whether it changes with the amount of attention. Does adding more attention change \emph{which} examples each architecture affects? Pairwise Jaccard appears to stabilize at the first attention level (4\%; $\bar{J} \approx 0.095$) and remains flat across all higher ratios (Figure~\ref{fig:decoupling}b), suggesting that minimal attention may suffice to establish the per-example divergence pattern, though the small number of ratios ($n = 5$) limits statistical confirmation. As background, LAMBADA's aggregate cross-architecture $\sigma$ shows a non-significant decreasing trend ($\rho = -1.0$, Bonferroni-adjusted $p = .170$; excluding GDN: $\rho = -0.7$, $p = .233$; MMLU reverses to $\rho = +0.6$ when excluding GDN; observed at 1.3B, absent at 340M; Table~\ref{tab:convergence}, Figure~\ref{fig:task_specificity}). No other benchmark shows a comparable aggregate pattern ($n = 5$; negligible power for $|\rho| < 1.0$; Appendix~\ref{app:convergence_detail}).
102	
103	
104	Each architecture's per-example response is largely idiosyncratic: observed $\bar{J}$ reaches only 6--7\% of the achievable range above chance ($J_{\max} \approx 0.78$--$0.92$), ruling out ceiling constraints (\S\ref{ssec:per_example}). This pattern generalizes beyond LAMBADA (Figure~\ref{fig:decoupling}c): on all four main benchmarks, mean pairwise Jaccard shows no significant trend with attention ratio (all $\rho \leq 0.80$, $p \geq 0.333$; Appendix~\ref{app:cross_bench_jaccard}).
105	
106	Heuristic bootstrap 95\% CIs ($n = 3$; \S\ref{ssec:statistical_methods}) show non-overlapping $\sigma$ between pure and h3-1 but completely overlapping Jaccard across all hybrid ratios. Figure~\ref{fig:jaccard_hierarchy} shows a three-tier Jaccard hierarchy: independence baseline (${\sim}0.05$), cross-architecture (${\sim}0.10$, $2\times$ baseline), and within-architecture (${\sim}0.33$, $3\times$ cross-architecture; Appendix~\ref{app:within_arch_stability}). Pythia 70M \citep{biderman2023pythia} seed calibration yields a comparable within-seed level ($J = 0.27$--$0.39$; Appendix~\ref{app:seed_calibration}), consistent with architecture-associated divergence.
107	
108	Two interpretations are consistent with the observed stability. \textbf{(a) Fingerprint view:} each recurrent backbone imposes a characteristic inductive bias that determines which examples attention can rescue. \textbf{(b) Convergence view:} even minimal attention causes all architectures to rapidly adopt Transformer-like behavior, with residual divergence from incomplete convergence. Appendix~\ref{app:transformer_entrainment} shows that h3-1 correct sets shift toward the Transformer baseline, providing partial support for (b). Attention weight analysis (Appendix~\ref{app:attention_patterns}) shows GDN and RetNet produce nearly identical attention distributions (cosine 0.995) yet differ in per-example effects, suggesting these originate in the recurrent layers.
109	
110	Cross-scale analysis reveals a clear dissociation: per-example Jaccard is consistent across scales ($\bar{J} = 0.08$--$0.10$ at 340M and 1.3B), whereas the aggregate variance trend is observed only at 1.3B on LAMBADA ($\rho = -0.50$, $p = .45$ at 340M). Ambiguity $\alpha$ is systematically higher at 340M ($\Delta \leq 8$\,pp), suggesting the \emph{pattern} of multiplicity is scale-stable while its magnitude tracks model capacity (Appendices~\ref{app:scale_convergence}, \ref{app:scale_per_example}--\ref{app:cross_scale}).
111	\vspace{-2pt}
112	\subsection{Robustness}\label{ssec:robustness}
113	
114	Removing GDN weakens the LAMBADA variance reduction ($\rho = -0.7$, $p = .233$) and reverses MMLU's ($\rho = +0.6$), both driven by GDN's 16-head configuration (vs.\ 32 in others; Appendix~\ref{app:gdn_confound}). The RetNet--HGRN2 pair preserves the independence pattern ($\sigma \leq 0.008$, $J = 0.086$--$0.108$). The aggregate variance pattern therefore depends on GDN inclusion; the per-example stability pattern does not. Five-architecture validation at 340M (adding GLA and DeltaNet) confirms $J \leq 0.14$ across all ten pairwise comparisons and four benchmarks (all $p < .01$; Figure~\ref{fig:jaccard_heatmap_5arch}; Appendix~\ref{app:extended_arch}), extending the per-example divergence finding to architectures not used in the primary analysis. Full sensitivity analyses appear in Appendix~\ref{app:sensitivity}; Transformer baseline comparison in Appendix~\ref{app:transformer_entrainment}.
115	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8071fcb2-75db-46e7-8d89-331d27c12aab",
  "isSidechain": false,
  "promptId": "73d622e8-44a2-4ef1-8f25-89dbf02b8b7b",
  "type": "user",
  "uuid": "8e6ba2f1-6790-4aa1-9f1b-ce15e1baff34",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/experiments.tex",
      "content": "\\section{Experiments}\\label{sec:experiments}\n\nUsing the model zoo of \\citet{wang2025hybrid} (\\S\\ref{ssec:model_zoo}), we evaluate all 30 configurations on 10 benchmarks plus supplementary COPA ($n = 100$) at 1.3B scale unless noted. Results at 340M appear in scale analyses. Recall: h$k$-1 denotes one attention layer per $k{+}1$ layers; h3-1 = 25\\% attention.\n\n\\subsection{Per-Example Divergence}\\label{ssec:per_example}\n\nDo architectures converge by improving on the same examples? We compare each architecture's pure-recurrent baseline against its h3-1 hybrid on 5{,}153 LAMBADA examples, classifying each as helped, hurt, or unchanged. Although the decomposition is binary, it captures genuine separation in the continuous confidence space (Cohen's $d = 0.73$--$0.92$ between helped and hurt on LAMBADA; cross-benchmark details in Appendix~\\ref{app:cm_cross}). Binarization discards confidence magnitude, so we supplement with continuous confidence margin analysis (Appendix~\\ref{app:confidence_margin}) and verify that low Jaccard persists under continuous thresholds (Appendix~\\ref{app:continuous_jaccard}).\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_jaccard_hierarchy.pdf}\n\\caption{Jaccard hierarchy on LAMBADA (1.3B). Cross-architecture overlap ($\\bar{J} \\approx 0.09$) is $2\\times$ the independence baseline but only one-third of within-architecture overlap ($\\bar{J} \\approx 0.33$). Pythia 70M within-seed Jaccard (different scale) falls at a comparable level. Error bars show the helped--hurt range.}\n\\label{fig:jaccard_hierarchy}\n\\end{figure}\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=0.75\\textwidth]{figures/fig3_alpha_routing.pdf}\n\\caption{(a) Per-example ambiguity $\\alpha$ varies $2\\times$ across task types. (b) Confidence-based routing gains track $\\alpha$: effective when multiplicity is high (LAMBADA) but counterproductive when low (PIQA). 1.3B, h3-1.}\n\\label{fig:alpha_routing}\n\\end{figure*}\n\nEach architecture displays a distinct profile of per-example changes (Figure~\\ref{fig:per_example_bars}). GDN loses a net 153 examples (462 helped, 615 hurt), RetNet loses 69 (426/495), and HGRN2 gains 153 (548/395; full counts in Appendix~\\ref{app:per_example_counts}). HGRN2 is the only architecture for which adding attention yields a net per-example benefit. Pairwise Jaccard similarity is low: mean $\\bar{J} \\leq 0.10$, indicating ${\\sim}90$\\% non-overlap. Overlap significantly exceeds the independence baseline ($J_{\\text{null}} \\approx 0.05$, all $z > 5.9$, $p < .0001$; Appendix~\\ref{app:jaccard_permutation}), plausibly reflecting shared sensitivity to example difficulty. Normalizing by $J_{\\max}$, observed overlap reaches only 6--7\\% of the achievable range above chance (Appendix~\\ref{app:normalized_es}), confirming that low Jaccard cannot be attributed to set-size constraints.\n\n\n\\paragraph{Confidence margin predictor.} Pure-model confidence on the target token predicts which examples will be affected (AUC 0.70--0.74, a non-parametric measure equivalent to Mann-Whitney $U$; Appendix~\\ref{app:confidence_margin}): rescue thresholds are architecture-invariant (1\\% spread) but disruption thresholds vary 47\\%, explaining cross-architecture Jaccard divergence (Appendix~\\ref{app:prediction_framework}). Calibration differences account for less than half the threshold spread (Appendix~\\ref{app:calibration}). The rescue pattern generalizes across three benchmarks ($d = 0.13$--$0.60$; Appendix~\\ref{app:cm_cross}); disruption is weaker on reasoning tasks (Appendix~\\ref{app:boolq}). This structured disagreement constitutes predictive multiplicity \\citep{marx2020predictive} under architectural variation.\n\n\\paragraph{Confidence-based routing.} As an illustrative case study, the rescue-threshold asymmetry suggests a routing strategy: select the architecture whose pure-model confidence best predicts successful rescue. On LAMBADA, this outperforms majority vote by $+5.3$\\,pp (SD $= 0.4$\\,pp, 10 cross-validated splits), extracting 36\\% of the oracle gap (oracle = 65.5\\%; Appendix~\\ref{app:complementarity}). On ARC-Easy, gains are modest ($+1.0$\\,pp, SD $= 0.5$\\,pp); on HellaSwag, routing provides no benefit ($-0.02$\\,pp, $p = .89$); on PIQA, it is significantly negative ($-0.6$\\,pp, $p = .006$). Routing works when multiplicity is high ($\\alpha = 0.30$, LAMBADA) and a clear rescue-threshold signal exists, but is counterproductive when multiplicity is low ($\\alpha = 0.14$, PIQA). A natural comparison (average-logits ensemble) is left to future work as it requires simultaneous inference across all architectures.\n\n\\paragraph{Multiplicity variation.} Extending to HellaSwag ($N = 10{,}042$) and PIQA ($N = 1{,}838$) reveals that multiplicity varies systematically across tasks (Table~\\ref{tab:multiplicity}). Ambiguity $\\alpha$ \\citep{marx2020predictive} ranges from 0.14 (PIQA) through 0.15 (HellaSwag) and 0.21 (ARC-Easy; Appendix~\\ref{app:arceasy}) to 0.30 (LAMBADA). Format does not drive this ordering: HellaSwag (four-way) and PIQA (two-choice) produce nearly identical $\\alpha$ despite different answer-space sizes ($\\rho = -0.60$, $p = .24$ with task accuracy). This suggests multiplicity is associated with cognitive demands rather than evaluation format, though the confound cannot be fully resolved (Limitations). Bootstrap 95\\% CIs confirm the ordering (all non-overlapping except PIQA--HellaSwag; Table~\\ref{tab:arceasy_ambiguity}). Pairwise Jaccard remains uniformly low ($\\bar{J} \\leq 0.10$, all $p < .01$), indicating architectures affect different examples regardless of how many are affected. Within each benchmark, $\\alpha$ is stable across attention ratios (variation $< 0.03$) but differs $2\\times$ across task types, confirming that multiplicity magnitude depends on task, not attention ratio \\citep[cf.][]{gorbett2026crossmodel}.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig2_task_specificity.pdf}\n\\caption{Spearman $\\rho$ between attention ratio and cross-architecture $\\sigma$ for each benchmark at 1.3B scale. LAMBADA ($\\rho = -1.0$; BCa 95\\% CI $[-1.0,\\,-0.7]$, heuristic) is the only benchmark whose CI excludes zero. Bootstrap CI is heuristic given $n = 3$ architectures.}\n\\label{fig:task_specificity}\n\\end{figure}\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=0.75\\textwidth]{figures/jaccard_heatmap_5arch.pdf}\n\\caption{Pairwise Jaccard heatmap across five architectures (340M, h3-1), where helped (hurt) examples are those correct only with (without) attention. Upper triangle: $J_{\\text{helped}}$; lower triangle: $J_{\\text{hurt}}$. All values $\\leq 0.14$, all permutation tests $p \\leq .002$. HellaSwag and PIQA results in Appendix~\\ref{app:extended_arch}.}\n\\label{fig:jaccard_heatmap_5arch}\n\\end{figure*}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Predictive multiplicity at 1.3B, h3-1. $\\alpha$: ambiguity \\citep{marx2020predictive}; $\\bar{J}$: mean pairwise Jaccard of helped~(h) / hurt~(u) sets; $\\rho_\\alpha$: Spearman $\\rho$ of $\\alpha$ vs.\\ attention ratio.}\n\\label{tab:multiplicity}\n\\vspace{1pt}\n\\begin{tabular}{@{}lrcccc@{}}\n\\toprule\n & $N$ & $\\alpha$ & $\\bar{J}_{h}$ & $\\bar{J}_{u}$ & $\\rho_\\alpha$ \\\\\n\\midrule\nPIQA & 1838 & .14 & .091 & .094 & $0.0$ \\\\\nHellaSwag & 10042 & .15 & .095 & .085 & $0.1$ \\\\\nARC-Easy & 2376 & .21 & .092 & .099 & $-0.2$ \\\\\nLAMBADA & 5153 & .30 & .096 & .091 & $-0.6$ \\\\\n\\bottomrule\n\\end{tabular}\n\\par\\vspace{2pt}\n{\\footnotesize Within-benchmark $\\alpha$ variation $< 0.03$ across ratios. BoolQ, WinoGrande: Appendix~\\ref{app:boolq}, \\ref{app:winogrande}.}\n\\vspace{-4pt}\n\\end{table}\n\n\\begin{table*}[t]\n\\centering\n\\caption{Cross-architecture variance trends across benchmarks (1.3B scale). $\\rho$: Spearman correlation between attention ratio and cross-architecture standard deviation $\\sigma$ across five configurations. $p$: exact permutation test (two-tailed, 120 permutations). $\\sigma$ values reported $\\times 10^{2}$ (accuracy percentage points). Ratio: $\\sigma_{\\text{pure}} / \\sigma_{\\text{h3-1}}$. \\textbf{Bold}: only benchmark with $\\rho = -1.0$. HellaSwag evaluated using normalized accuracy (acc\\_norm), the standard metric for this benchmark.}\n\\label{tab:convergence}\n\\small\n\\setlength{\\tabcolsep}{3.5pt}\n\\begin{tabular}{@{}llrrrrr@{}}\n\\toprule\nBenchmark & Category & $\\rho$ & $p$ & $\\sigma_{\\text{pure}}$ & $\\sigma_{\\text{h3-1}}$ & Ratio \\\\\n\\midrule\n\\textbf{LAMBADA$^{\\ddagger}$} & \\textbf{Retrieval} & $\\mathbf{-1.0}$ & \\textbf{.017} & \\textbf{2.41} & \\textbf{0.49} & \\textbf{4.87} \\\\\n\\quad\\emph{(excl.\\ GDN)} & & $-0.7$ & .233 & --- & --- & --- \\\\\nBoolQ & Comprehension & $0.2$ & .783 & 1.63 & 2.36 & 0.69 \\\\\nARC-C & Reasoning & $0.6$ & .350 & 0.96 & 1.32 & 0.72 \\\\\nHellaSwag & Reasoning & $0.3$ & .683 & 1.17 & 1.18 & 0.99 \\\\\nPIQA & Reasoning & $-0.5$ & .450 & 0.54 & 0.34 & 1.59 \\\\\nWinoGrande & Reasoning & $0.1$ & .950 & 0.67 & 0.78 & 0.86 \\\\\nARC-E & Mixed & $-0.7$ & .233 & 1.00 & 0.13 & 7.70 \\\\\nMMLU & Mixed & $-0.7$ & .233 & 0.92 & 0.41 & 2.27 \\\\\nSciQ & Mixed & $0.1$ & .950 & 0.87 & 0.74 & 1.19 \\\\\nXStoryCloze & Mixed & $-0.6$ & .350 & 0.82 & 0.55 & 1.49 \\\\\n\\midrule\nCOPA$^{\\dagger}$ & Reasoning & $-0.67$ & .267 & 2.63 & 0.47 & 5.57 \\\\\n\\bottomrule\n\\multicolumn{7}{l}{\\footnotesize $^{\\dagger}$Supplementary ($n = 100$); excluded from multiple comparison correction.} \\\\\n\\multicolumn{7}{l}{\\footnotesize $^{\\ddagger}$GDN h3-1 uses 16 attention heads; all other configurations use 32 (\\S\\ref{ssec:robustness}).} \\\\\n\\multicolumn{7}{@{}p{\\textwidth}@{}}{\\footnotesize Bonferroni-adjusted $p = .170$. \\textbf{Power: only $|\\rho| = 1.0$ achieves $p < .05$ at $n = 5$.} Excl.\\ GDN reverses MMLU $\\rho$ to $+0.6$ (\\S\\ref{ssec:robustness}).}\n\\end{tabular}\n\\vspace{-4pt}\n\\end{table*}\n\n\\vspace{-2pt}\n\\subsection{Per-Example Overlap Appears Stable from Minimal Attention}\\label{ssec:decoupling}\n\nHaving established that multiplicity varies by task type, we now ask whether it changes with the amount of attention. Does adding more attention change \\emph{which} examples each architecture affects? Pairwise Jaccard appears to stabilize at the first attention level (4\\%; $\\bar{J} \\approx 0.095$) and remains flat across all higher ratios (Figure~\\ref{fig:decoupling}b), suggesting that minimal attention may suffice to establish the per-example divergence pattern, though the small number of ratios ($n = 5$) limits statistical confirmation. As background, LAMBADA's aggregate cross-architecture $\\sigma$ shows a non-significant decreasing trend ($\\rho = -1.0$, Bonferroni-adjusted $p = .170$; excluding GDN: $\\rho = -0.7$, $p = .233$; MMLU reverses to $\\rho = +0.6$ when excluding GDN; observed at 1.3B, absent at 340M; Table~\\ref{tab:convergence}, Figure~\\ref{fig:task_specificity}). No other benchmark shows a comparable aggregate pattern ($n = 5$; negligible power for $|\\rho| < 1.0$; Appendix~\\ref{app:convergence_detail}).\n\n\nEach architecture's per-example response is largely idiosyncratic: observed $\\bar{J}$ reaches only 6--7\\% of the achievable range above chance ($J_{\\max} \\approx 0.78$--$0.92$), ruling out ceiling constraints (\\S\\ref{ssec:per_example}). This pattern generalizes beyond LAMBADA (Figure~\\ref{fig:decoupling}c): on all four main benchmarks, mean pairwise Jaccard shows no significant trend with attention ratio (all $\\rho \\leq 0.80$, $p \\geq 0.333$; Appendix~\\ref{app:cross_bench_jaccard}).\n\nHeuristic bootstrap 95\\% CIs ($n = 3$; \\S\\ref{ssec:statistical_methods}) show non-overlapping $\\sigma$ between pure and h3-1 but completely overlapping Jaccard across all hybrid ratios. Figure~\\ref{fig:jaccard_hierarchy} shows a three-tier Jaccard hierarchy: independence baseline (${\\sim}0.05$), cross-architecture (${\\sim}0.10$, $2\\times$ baseline), and within-architecture (${\\sim}0.33$, $3\\times$ cross-architecture; Appendix~\\ref{app:within_arch_stability}). Pythia 70M \\citep{biderman2023pythia} seed calibration yields a comparable within-seed level ($J = 0.27$--$0.39$; Appendix~\\ref{app:seed_calibration}), consistent with architecture-associated divergence.\n\nTwo interpretations are consistent with the observed stability. \\textbf{(a) Fingerprint view:} each recurrent backbone imposes a characteristic inductive bias that determines which examples attention can rescue. \\textbf{(b) Convergence view:} even minimal attention causes all architectures to rapidly adopt Transformer-like behavior, with residual divergence from incomplete convergence. Appendix~\\ref{app:transformer_entrainment} shows that h3-1 correct sets shift toward the Transformer baseline, providing partial support for (b). Attention weight analysis (Appendix~\\ref{app:attention_patterns}) shows GDN and RetNet produce nearly identical attention distributions (cosine 0.995) yet differ in per-example effects, suggesting these originate in the recurrent layers.\n\nCross-scale analysis reveals a clear dissociation: per-example Jaccard is consistent across scales ($\\bar{J} = 0.08$--$0.10$ at 340M and 1.3B), whereas the aggregate variance trend is observed only at 1.3B on LAMBADA ($\\rho = -0.50$, $p = .45$ at 340M). Ambiguity $\\alpha$ is systematically higher at 340M ($\\Delta \\leq 8$\\,pp), suggesting the \\emph{pattern} of multiplicity is scale-stable while its magnitude tracks model capacity (Appendices~\\ref{app:scale_convergence}, \\ref{app:scale_per_example}--\\ref{app:cross_scale}).\n\\vspace{-2pt}\n\\subsection{Robustness}\\label{ssec:robustness}\n\nRemoving GDN weakens the LAMBADA variance reduction ($\\rho = -0.7$, $p = .233$) and reverses MMLU's ($\\rho = +0.6$), both driven by GDN's 16-head configuration (vs.\\ 32 in others; Appendix~\\ref{app:gdn_confound}). The RetNet--HGRN2 pair preserves the independence pattern ($\\sigma \\leq 0.008$, $J = 0.086$--$0.108$). The aggregate variance pattern therefore depends on GDN inclusion; the per-example stability pattern does not. Five-architecture validation at 340M (adding GLA and DeltaNet) confirms $J \\leq 0.14$ across all ten pairwise comparisons and four benchmarks (all $p < .01$; Figure~\\ref{fig:jaccard_heatmap_5arch}; Appendix~\\ref{app:extended_arch}), extending the per-example divergence finding to architectures not used in the primary analysis. Full sensitivity analyses appear in Appendix~\\ref{app:sensitivity}; Transformer baseline comparison in Appendix~\\ref{app:transformer_entrainment}.\n",
      "numLines": 115,
      "startLine": 1,
      "totalLines": 115
    }
  },
  "sourceToolAssistantUUID": "8071fcb2-75db-46e7-8d89-331d27c12aab",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/sessions/paper_audit_content_6bc68a37",
  "sessionId": "6e8d5c3f-7c75-4ff9-a01f-f2df71411ac1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-25T17:13:19.304Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Uzksc3pvjrerTH5h8uWski`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8e6ba2f1-6790-4aa1-9f1b-ce15e1baff34",
  "isSidechain": false,
  "requestId": "req_011CbPfKm7MVoTWjRv9pw5TW",
  "type": "assistant",
  "uuid": "1c4a6d01-1db4-4cb9-b432-c10c9fd79e5f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/sessions/paper_audit_content_6bc68a37",
  "sessionId": "6e8d5c3f-7c75-4ff9-a01f-f2df71411ac1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DyVargCTpxVeRwtzp3L3va",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12005,
      "cache_read_input_tokens": 38284,
      "output_tokens": 644,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12005,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 644,
          "cache_read_input_tokens": 38284,
          "cache_creation_input_tokens": 12005,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12005
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

_source line 29 · 2026-05-25T17:13:19.308Z_

<details><summary>↩ Tool result · `toolu_01Uzksc3pvjrerTH5h8uWski`</summary>

```text
1	\vspace{-2pt}
2	\section{Conclusion}
3	\vspace{-2pt}
4	
5	We have shown that hybrid linear recurrent architectures which appear interchangeable by aggregate benchmarks diverge substantially at the per-example level. This multiplicity varies by task type ($\alpha = 0.14$--$0.30$) rather than attention ratio. Per-example overlap appears to stabilize at 4\% attention (pairwise Jaccard $\leq 0.10$); two interpretations (architecture-specific fingerprints or rapid convergence toward Transformer-like behavior) remain open (Appendix~\ref{app:transformer_entrainment}). Confidence margins partially predict affected examples (AUC 0.70--0.74), with rescue thresholds architecture-invariant but disruption thresholds varying 47\%.
6	At the 340M--1.3B scales studied here, aggregate equivalence does not guarantee behavioral equivalence. Low cross-architecture Jaccard creates complementarity ($+7$--$14$\,pp oracle gain), though routing exploitation remains task-dependent ($+5.3$\,pp on LAMBADA; $-0.6$\,pp on PIQA).
7	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1c4a6d01-1db4-4cb9-b432-c10c9fd79e5f",
  "isSidechain": false,
  "promptId": "73d622e8-44a2-4ef1-8f25-89dbf02b8b7b",
  "type": "user",
  "uuid": "41c4218c-42f6-41e5-b791-934ddef54b01",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/conclusion.tex",
      "content": "\\vspace{-2pt}\n\\section{Conclusion}\n\\vspace{-2pt}\n\nWe have shown that hybrid linear recurrent architectures which appear interchangeable by aggregate benchmarks diverge substantially at the per-example level. This multiplicity varies by task type ($\\alpha = 0.14$--$0.30$) rather than attention ratio. Per-example overlap appears to stabilize at 4\\% attention (pairwise Jaccard $\\leq 0.10$); two interpretations (architecture-specific fingerprints or rapid convergence toward Transformer-like behavior) remain open (Appendix~\\ref{app:transformer_entrainment}). Confidence margins partially predict affected examples (AUC 0.70--0.74), with rescue thresholds architecture-invariant but disruption thresholds varying 47\\%.\nAt the 340M--1.3B scales studied here, aggregate equivalence does not guarantee behavioral equivalence. Low cross-architecture Jaccard creates complementarity ($+7$--$14$\\,pp oracle gain), though routing exploitation remains task-dependent ($+5.3$\\,pp on LAMBADA; $-0.6$\\,pp on PIQA).\n",
      "numLines": 7,
      "startLine": 1,
      "totalLines": 7
    }
  },
  "sourceToolAssistantUUID": "1c4a6d01-1db4-4cb9-b432-c10c9fd79e5f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/sessions/paper_audit_content_6bc68a37",
  "sessionId": "6e8d5c3f-7c75-4ff9-a01f-f2df71411ac1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-25T17:13:19.827Z_

<details open><summary>🔧 Tool call — Read · `toolu_01LbPKozHfKYMXmgt43wGYxc`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "41c4218c-42f6-41e5-b791-934ddef54b01",
  "isSidechain": false,
  "requestId": "req_011CbPfKm7MVoTWjRv9pw5TW",
  "type": "assistant",
  "uuid": "9a967a5b-39f7-42d1-8753-13162390f8bd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/sessions/paper_audit_content_6bc68a37",
  "sessionId": "6e8d5c3f-7c75-4ff9-a01f-f2df71411ac1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DyVargCTpxVeRwtzp3L3va",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12005,
      "cache_read_input_tokens": 38284,
      "output_tokens": 644,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12005,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 644,
          "cache_read_input_tokens": 38284,
          "cache_creation_input_tokens": 12005,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12005
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

_source line 31 · 2026-05-25T17:13:19.832Z_

<details><summary>↩ Tool result · `toolu_01LbPKozHfKYMXmgt43wGYxc`</summary>

```text
1	\section{Related Work}
2	
3	\paragraph{Hybrid Recurrent Architectures.}
4	The design space for combining attention with recurrence spans layer-level interleaving \citep[Jamba;][]{lieber2024jamba}, local attention pairing \citep[Griffin, RecurrentGemma;][]{de2024griffin,botev2024recurrentgemma}, matrix-valued recurrence \citep[RWKV-6;][]{peng2024eagle}, within-head mixing \citep[Hymba;][]{dong2024hymba}, and unbounded-context hybrid SSMs \citep[Samba;][]{ren2024samba}. Mamba-2 \citep{dao2024mamba2} establishes a duality between structured state spaces and attention, while \citet{ali2025hidden} reveal implicit attention within Mamba. Comparative evaluations confirm that hybrids outperform pure Transformers and SSMs at scale \citep{waleffe2024empirical}, and that even one attention layer enables content-based routing \citep{basu2026routing}. Recent theoretical work establishes a provable expressiveness hierarchy between hybrid and pure linear attention \citep{ye2026provable}, providing formal grounding for the architectural differences we characterize at the per-example level. \citet{wang2025hybrid} provide the controlled model zoo we use, holding training conditions constant while varying architecture and attention ratio.
5	
6	\paragraph{Linear Recurrent Models.}
7	Our three recurrent backbones represent distinct gating strategies within the linear recurrence family: RetNet \citep{sun2023retnet} uses multi-scale exponential decay, HGRN2 \citep{qin2024hgrn2} applies gated state expansion, and GatedDeltaNet \citep{yang2024gateddeltanet} combines gated updates with delta rules, extending GLA \citep{yang2024gla} and DeltaNet \citep{yang2024deltanet}. These descend from S4 \citep{gu2022s4} and Mamba \citep{gu2024mamba}, which introduced structured state spaces and input-dependent selection, and connect to linear attention \citep{katharopoulos2020transformers} through the state-space--attention duality of Mamba-2. xLSTM \citep{beck2024xlstm} revives the LSTM lineage with exponential gating and matrix memory, offering an alternative approach at scale. \citet{zimerman2025unified} show that modern gated-linear RNNs---including RetNet and HGRN---can all be cast as implicit causal self-attention, providing a unifying perspective on the family. \citet{arora2024based} identify a recall-throughput tradeoff in linear models that motivates hybrid designs.
8	
9	\paragraph{Underspecification and Predictive Multiplicity.}
10	\citet{damour2022underspecification} formalized underspecification, where equivalent aggregate performance masks per-prediction divergence, with NLP instances including seed-dependent BERT disagreement \citep{mccoy2020berts,sellam2022multiberts}. \citet{marx2020predictive} introduced predictive multiplicity, showing that near-optimal models produce conflicting per-example predictions; extensions address probabilistic settings \citep{watson2023predictive}, Rashomon capacity \citep{hsu2022rashomon}, and reconciliation \citep{du2025reconciling,haghighat2026resolving}. These studies, along with Rashomon-set analyses \citep{fisher2019all,semenova2022existence} and weight-space interpolation \citep{wortsman2022model}, attribute divergence to initialization noise within a single architecture. We show that changing the recurrent backbone, a qualitatively different source of variation, produces per-example multiplicity that varies by task type. Our routing approach relates to selective prediction \citep{geifman2017selective} and ensemble selection \citep{caruana2004ensemble}, though we select among architecturally distinct models. \citet{yang2026benchmark} demonstrate analogous per-item disagreement (16--66\%) among frontier LLMs; our within-family design isolates backbone variation from training-regime differences.
11	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9a967a5b-39f7-42d1-8753-13162390f8bd",
  "isSidechain": false,
  "promptId": "73d622e8-44a2-4ef1-8f25-89dbf02b8b7b",
  "type": "user",
  "uuid": "2483d0a1-4798-49da-bdcf-3e0b4bc54e30",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/related_work.tex",
      "content": "\\section{Related Work}\n\n\\paragraph{Hybrid Recurrent Architectures.}\nThe design space for combining attention with recurrence spans layer-level interleaving \\citep[Jamba;][]{lieber2024jamba}, local attention pairing \\citep[Griffin, RecurrentGemma;][]{de2024griffin,botev2024recurrentgemma}, matrix-valued recurrence \\citep[RWKV-6;][]{peng2024eagle}, within-head mixing \\citep[Hymba;][]{dong2024hymba}, and unbounded-context hybrid SSMs \\citep[Samba;][]{ren2024samba}. Mamba-2 \\citep{dao2024mamba2} establishes a duality between structured state spaces and attention, while \\citet{ali2025hidden} reveal implicit attention within Mamba. Comparative evaluations confirm that hybrids outperform pure Transformers and SSMs at scale \\citep{waleffe2024empirical}, and that even one attention layer enables content-based routing \\citep{basu2026routing}. Recent theoretical work establishes a provable expressiveness hierarchy between hybrid and pure linear attention \\citep{ye2026provable}, providing formal grounding for the architectural differences we characterize at the per-example level. \\citet{wang2025hybrid} provide the controlled model zoo we use, holding training conditions constant while varying architecture and attention ratio.\n\n\\paragraph{Linear Recurrent Models.}\nOur three recurrent backbones represent distinct gating strategies within the linear recurrence family: RetNet \\citep{sun2023retnet} uses multi-scale exponential decay, HGRN2 \\citep{qin2024hgrn2} applies gated state expansion, and GatedDeltaNet \\citep{yang2024gateddeltanet} combines gated updates with delta rules, extending GLA \\citep{yang2024gla} and DeltaNet \\citep{yang2024deltanet}. These descend from S4 \\citep{gu2022s4} and Mamba \\citep{gu2024mamba}, which introduced structured state spaces and input-dependent selection, and connect to linear attention \\citep{katharopoulos2020transformers} through the state-space--attention duality of Mamba-2. xLSTM \\citep{beck2024xlstm} revives the LSTM lineage with exponential gating and matrix memory, offering an alternative approach at scale. \\citet{zimerman2025unified} show that modern gated-linear RNNs---including RetNet and HGRN---can all be cast as implicit causal self-attention, providing a unifying perspective on the family. \\citet{arora2024based} identify a recall-throughput tradeoff in linear models that motivates hybrid designs.\n\n\\paragraph{Underspecification and Predictive Multiplicity.}\n\\citet{damour2022underspecification} formalized underspecification, where equivalent aggregate performance masks per-prediction divergence, with NLP instances including seed-dependent BERT disagreement \\citep{mccoy2020berts,sellam2022multiberts}. \\citet{marx2020predictive} introduced predictive multiplicity, showing that near-optimal models produce conflicting per-example predictions; extensions address probabilistic settings \\citep{watson2023predictive}, Rashomon capacity \\citep{hsu2022rashomon}, and reconciliation \\citep{du2025reconciling,haghighat2026resolving}. These studies, along with Rashomon-set analyses \\citep{fisher2019all,semenova2022existence} and weight-space interpolation \\citep{wortsman2022model}, attribute divergence to initialization noise within a single architecture. We show that changing the recurrent backbone, a qualitatively different source of variation, produces per-example multiplicity that varies by task type. Our routing approach relates to selective prediction \\citep{geifman2017selective} and ensemble selection \\citep{caruana2004ensemble}, though we select among architecturally distinct models. \\citet{yang2026benchmark} demonstrate analogous per-item disagreement (16--66\\%) among frontier LLMs; our within-family design isolates backbone variation from training-regime differences.\n",
      "numLines": 11,
      "startLine": 1,
      "totalLines": 11
    }
  },
  "sourceToolAssistantUUID": "9a967a5b-39f7-42d1-8753-13162390f8bd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/sessions/paper_audit_content_6bc68a37",
  "sessionId": "6e8d5c3f-7c75-4ff9-a01f-f2df71411ac1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-25T17:13:20.265Z_

<details open><summary>🔧 Tool call — Read · `toolu_01FDkgHCtDhkUio2cuyHyDXf`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2483d0a1-4798-49da-bdcf-3e0b4bc54e30",
  "isSidechain": false,
  "requestId": "req_011CbPfKm7MVoTWjRv9pw5TW",
  "type": "assistant",
  "uuid": "1bec8b13-581d-42cb-92b6-a94f2d492b75",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/sessions/paper_audit_content_6bc68a37",
  "sessionId": "6e8d5c3f-7c75-4ff9-a01f-f2df71411ac1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DyVargCTpxVeRwtzp3L3va",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12005,
      "cache_read_input_tokens": 38284,
      "output_tokens": 644,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12005,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 644,
          "cache_read_input_tokens": 38284,
          "cache_creation_input_tokens": 12005,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12005
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

_source line 33_

```json
{
  "type": "last-prompt",
  "lastPrompt": "项目：entrainment_gated_ft Venue：emnlp-2026 论文目录：/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper  Phase 1 确定性检查结果： 源码检查: passed=False, 2 critical, 1 warning 一致性检查…",
  "leafUuid": "1bec8b13-581d-42cb-92b6-a94f2d492b75",
  "sessionId": "6e8d5c3f-7c75-4ff9-a01f-f2df71411ac1"
}
```

---

### Runtime record

_source line 34_

```json
{
  "type": "ai-title",
  "aiTitle": "EMNLP 2026 paper structure audit and compliance check",
  "sessionId": "6e8d5c3f-7c75-4ff9-a01f-f2df71411ac1"
}
```

---

### Tool result

_source line 35 · 2026-05-25T17:13:20.544Z_

<details><summary>↩ Tool result · `toolu_01FDkgHCtDhkUio2cuyHyDXf`</summary>

```text
1	% Appendix sections for the paper.
2	
3	\section{Confirmatory and Exploratory Analyses}\label{app:benchmark_details}
4	
5	The task taxonomy used in \S\ref{ssec:task_taxonomy} was defined prior to running any convergence analyses. Each benchmark was assigned to exactly one of four categories based on the primary cognitive demand of the task:
6	
7	\begin{itemize}
8	    \item \textbf{Retrieval}: tasks requiring prediction from long-range context without multi-step reasoning (LAMBADA).
9	    \item \textbf{Comprehension}: reading comprehension with explicit passage support (BoolQ).
10	    \item \textbf{Reasoning}: tasks requiring commonsense inference or multi-step reasoning (HellaSwag, ARC-Challenge, WinoGrande, PIQA).
11	    \item \textbf{Mixed}: tasks combining retrieval, comprehension, and reasoning demands (ARC-Easy, MMLU, SciQ, XStoryCloze).
12	\end{itemize}
13	
14	\paragraph{Confirmatory benchmark set.} Six benchmarks were designated as confirmatory for Bonferroni correction: LAMBADA, HellaSwag, ARC-Challenge, WinoGrande, ARC-Easy, and MMLU. These were selected as representative of retrieval, reasoning, and mixed categories before any convergence analysis was performed. The taxonomy and benchmark selection were fixed before analysis as an informal pre-analysis plan; we describe this as a confirmatory/exploratory split rather than a formal pre-registration, since no external timestamp exists. The main text applies the more conservative all-10-benchmark correction (Bonferroni-adjusted $p = .017 \times 10 = .170$). \textbf{Sensitivity:} correcting across only the six confirmatory benchmarks yields adjusted $p = .017 \times 6 = .100$, still above conventional significance.
15	
16	\paragraph{One-sided test.} If one adopts the prior that attention should reduce cross-architecture variance, the one-sided permutation $p$-value for LAMBADA is $1/120 \approx 0.0083$. Under 10-benchmark Bonferroni correction, this yields an adjusted $p = 0.083$, above the conventional threshold. We report two-sided tests throughout the main text as the more conservative choice; the one-sided result is noted here for completeness.
17	
18	\paragraph{Exploratory benchmarks.} Four additional benchmarks (BoolQ, PIQA, SciQ, XStoryCloze) were added as exploratory tests. All benchmarks share the same 10-benchmark correction (adjusted threshold $\alpha / 10 = 0.005$) and the four exploratory benchmarks are labeled as such throughout the paper. The all-10 Bonferroni correction reported in the main text is the only correction used for inference; the exploratory 6-benchmark subset correction in this appendix is provided for transparency.
19	
20	\paragraph{Supplementary benchmark.} COPA ($n = 100$) is treated as supplementary due to its small sample size. It is excluded from both correction families and reported separately with the $\dagger$ annotation in Table~\ref{tab:convergence}.
21	
22	\section{Convergence Detail}\label{app:convergence_detail}
23	
24	% Figure moved to main text (\S\ref{ssec:decoupling}).
25	
26	Beyond LAMBADA ($\rho = -1.0$), two benchmarks show moderate negative correlations that do not reach significance: ARC-Easy and MMLU (both $\rho = -0.7$, $p = .233$). Both are classified as ``Mixed'' tasks combining retrieval with reasoning demands. The sensitivity analysis (Appendix~\ref{app:sensitivity}) shows that MMLU's correlation reverses upon GDN exclusion ($\rho = +0.6$), indicating dependence on a single architecture; ARC-Easy's correlation is more stable. COPA ($n = 100$; supplementary) shows $\rho = -0.67$ with a large $\sigma$ ratio (5.57), consistent with LAMBADA's pattern but unreliable due to small sample size.
27	
28	Several benchmarks show positive or near-zero $\rho$ (BoolQ: $+0.2$; ARC-C: $+0.6$; HellaSwag: $+0.3$; WinoGrande: $+0.1$; SciQ: $+0.1$), indicating that attention does not systematically reduce cross-architecture variance on reasoning or comprehension tasks. The contrast with LAMBADA is consistent with attention's convergence benefit being specific to tasks requiring direct token-level recall \citep{arora2024zoology,arora2024based} rather than multi-step inference.
29	
30	\paragraph{Regression to the mean.} The direction of LAMBADA's aggregate convergence is consistent with regression to the mean: GDN (highest pure accuracy, 0.543) declines to 0.513 under h3-1, while HGRN2 (lowest, 0.484) rises to 0.514, yielding a $5\times$ $\sigma$ compression ($0.024 \to 0.005$). However, three observations argue against a purely statistical artifact. First, the $5\times$ reduction in cross-architecture $\sigma$ far exceeds typical regression amplitudes. Second, the direction is entirely determined by architecture identity, not random fluctuation: HGRN2 accuracy increases monotonically across all attention ratios, while GDN decreases monotonically---a pattern inconsistent with noise-driven mean reversion. Third, per-example analysis (\S\ref{ssec:per_example}) reveals architecture-specific patterns: GDN's net $-153$ examples and HGRN2's net $+153$ examples reflect distinct helped/hurt profiles with low cross-architecture Jaccard overlap, indicating that the aggregate convergence arises from structured, architecture-dependent per-example changes rather than symmetric regression.
31	
32	\section{Scale-Dependent Convergence}\label{app:scale_convergence}
33	
34	At 1.3B parameters, LAMBADA convergence is monotonic: $\sigma$ decreases at every attention level from 0\% through 25\% ($\rho = -1.0$). At 340M, convergence is partial: $\sigma$ reaches a maximum reduction of 56\% at intermediate attention ratios but rebounds at h3-1, yielding a net endpoint reduction of 36\%. The trajectory is non-monotonic, and the highest-attention model does not achieve the lowest cross-architecture variance. One possible interpretation is that at smaller scale, the capacity overhead of attention layers creates interference that offsets the retrieval benefit.
35	
36	This contrast is a preliminary observation from two data points (not a scaling law). Despite the aggregate divergence at 340M, mean pairwise Jaccard is similar at both scales ($J \approx 0.09$), extending the decoupling observation (\S\ref{ssec:decoupling}) to the scale dimension.
37	
38	\section{Sensitivity Analyses}\label{app:sensitivity}
39	
40	\subsection{Bootstrap Confidence Intervals}
41	
42	We construct 95\% bootstrap confidence intervals for the Spearman $\rho$ between attention ratio and cross-architecture $\sigma$ on LAMBADA using 10{,}000 resamples at the architecture level ($n = 3$ architectures). Of these resamples, 11.25\% are degenerate: they consist of same-architecture triplicates, which produce a constant $\sigma$ vector and therefore an undefined $\rho$ (division by zero in the rank correlation formula). These are excluded from the confidence interval computation because they carry no information about the correlation, not because they represent $\rho = 0$.
43	
44	The BCa (bias-corrected and accelerated) correction degenerates at the $\rho = -1.0$ boundary because the acceleration parameter requires finite jackknife variance, which collapses when the point estimate is at the distributional limit. We therefore report percentile confidence intervals instead. From the 88.75\% informative resamples, the 95\% percentile CI is $[-1.0,\,-0.7]$, which excludes zero.
45	
46	\subsection{GDN Exclusion Sensitivity}
47	
48	The GDN h3-1 configuration uses 16 attention heads rather than 32 (see Appendix~\ref{app:gdn_confound}). To assess the influence of this confound, we recompute all convergence correlations after excluding GDN, leaving two architectures (RetNet, HGRN2) at five attention ratios.
49	
50	Table~\ref{tab:gdn_sensitivity} reports the results for benchmarks where the correlation changes by $|\Delta\rho| \geq 0.3$. LAMBADA weakens from $\rho = -1.0$ to $\rho = -0.7$ ($p = .233$), consistent with GDN contributing to the convergence signal. MMLU reverses from $\rho = -0.7$ to $\rho = +0.6$, confirming that the moderate negative correlation on MMLU depends on GDN's inclusion and should not be interpreted as evidence of convergence.
51	
52	\begin{table}[ht]
53	\centering
54	\small
55	\caption{Effect of GDN exclusion on Spearman $\rho$ (attention ratio vs.\ cross-architecture $\sigma$) at 1.3B scale. Only benchmarks with $|\Delta\rho| \geq 0.3$ shown.}
56	\label{tab:gdn_sensitivity}
57	\begin{tabular}{lrrrr}
58	\toprule
59	Benchmark & $\rho_{\text{all}}$ & $\rho_{\text{no-GDN}}$ & $\Delta\rho$ & $p_{\text{no-GDN}}$ \\
60	\midrule
61	LAMBADA & $-1.0$ & $-0.7$ & $+0.3$ & .233 \\
62	MMLU & $-0.7$ & $+0.6$ & $+1.3$ & .350 \\
63	\bottomrule
64	\end{tabular}
65	\end{table}
66	
67	\section{GDN Attention Head Confound}\label{app:gdn_confound}
68	
69	In the \citet{wang2025hybrid} model zoo, the GDN h3-1 configuration at 1.3B scale uses 16 attention heads per attention layer, while all other hybrid configurations (across GDN, RetNet, and HGRN2) use 32 attention heads. This is a design choice in the original model zoo, not an error. The reduced head count changes the per-head dimension and may affect the attention capacity of GDN h3-1 relative to other configurations.
70	
71	This confound is relevant because the convergence analysis measures cross-architecture $\sigma$ at each attention ratio. At the h3-1 ratio (25\% attention), GDN's attention layers have a different internal structure than those of RetNet and HGRN2, which could contribute to variance reduction (or inflation) for reasons unrelated to the recurrent--attention interaction under study.
72	
73	The sensitivity analysis in Appendix~\ref{app:sensitivity} shows that removing GDN weakens the LAMBADA convergence correlation from $\rho = -1.0$ to $\rho = -0.7$. This weakening is partially attributable to the reduced sample size ($n = 2$ architectures) and partially to the confound itself. We cannot separate these two effects with the available data.
74	
75	\section{Attention Weight Analysis}\label{app:attention_patterns}
76	
77	We extract attention weight matrices from the 1.3B h3-1 models of all three architectures using forward hooks on each attention layer. While \citet{ali2025hidden} show that SSM layers learn implicit attention patterns, our analysis focuses on the explicit attention layers interleaved within the hybrid architecture. For each layer, we compute the mean attention distribution across all 5{,}153 LAMBADA examples and measure cross-architecture similarity via cosine similarity.
78	
79	\subsection{Cross-Architecture Cosine Similarity}
80	
81	Table~\ref{tab:attn_cosine} reports cosine similarity between mean attention distributions at selected layers and averaged across all layers.
82	
83	\begin{table}[ht]
84	\centering
85	\caption{Cosine similarity between mean attention weight distributions of architecture pairs at selected layers (1.3B h3-1 models on LAMBADA).}
86	\label{tab:attn_cosine}
87	\resizebox{\columnwidth}{!}{%
88	\begin{tabular}{lrrr}
89	\toprule
90	Layer & GDN--RetNet & GDN--HGRN2 & HGRN2--RetNet \\
91	\midrule
92	L2 (early) & 0.995 & 0.244 & 0.196 \\
93	L20 (deep) & 0.986 & 0.942 & 0.943 \\
94	\midrule
95	Mean (all layers) & 0.905 & 0.766 & 0.698 \\
96	\bottomrule
97	\end{tabular}%
98	}
99	\end{table}
100	
101	At layer 2, GDN and RetNet produce nearly identical attention distributions (cosine 0.995), while HGRN2 diverges from both (cosine $< 0.25$). By layer 20, all three architectures converge to similar attention patterns (cosine $> 0.94$). The layer-wise trajectory suggests that early-layer attention patterns are shaped by the preceding recurrent layers (which differ across architectures), while deeper layers converge regardless of the recurrent substrate.
102	
103	\subsection{Helped vs.\ Hurt Attention Entropy}
104	
105	To test whether the attention mechanism itself differs between helped and hurt examples, we compute the Shannon entropy of the attention distribution for each example at each attention layer and compare the mean entropy of helped examples against hurt examples within each architecture.
106	
107	\begin{table}[ht]
108	\centering
109	\caption{Mean attention entropy difference (helped $-$ hurt) averaged across attention layers (1.3B h3-1 models on LAMBADA). Values near zero indicate that the attention mechanism does not discriminate between helped and hurt examples.}
110	\label{tab:attn_entropy}
111	\begin{tabular}{lr}
112	\toprule
113	Architecture & $\Delta H$ (helped $-$ hurt) \\
114	\midrule
115	GDN & $-0.0009$ \\
116	RetNet & $+0.0179$ \\
117	HGRN2 & $+0.0020$ \\
118	\bottomrule
119	\end{tabular}
120	\end{table}
121	
122	GDN and HGRN2 show negligible entropy differences ($|\Delta H| \leq 0.002$). RetNet's $\Delta H = +0.018$ is small in absolute terms but slightly larger; helped examples receive marginally more diffuse attention in RetNet. Across all three architectures, the differences are insufficient to explain the per-example divergence, consistent with per-example effects not being explained by attention weight patterns and likely originating in the recurrent layers.
123	
124	\subsection{Last-5 Attention Mass}
125	
126	We also measure the fraction of attention mass allocated to the last five tokens, which captures whether the attention mechanism concentrates differently on recent context for helped vs.\ hurt examples.
127	
128	\begin{table}[ht]
129	\centering
130	\caption{Mean attention mass on last-5 tokens for helped and hurt examples, averaged across attention layers (1.3B h3-1 models on LAMBADA).}
131	\label{tab:attn_last5}
132	\begin{tabular}{lrr}
133	\toprule
134	Architecture & Helped & Hurt \\
135	\midrule
136	GDN & 0.0834 & 0.0831 \\
137	RetNet & 0.1578 & 0.1591 \\
138	HGRN2 & 0.0453 & 0.0467 \\
139	\bottomrule
140	\end{tabular}
141	\end{table}
142	
143	No architecture shows a meaningful difference in last-5 attention mass between helped and hurt examples (Table~\ref{tab:attn_last5}). This further supports the conclusion that the per-example divergence is not driven by differential attention allocation.
144	
145	\section{Cross-Scale Per-Example Comparisons}\label{app:cross_scale}
146	
147	\subsection{Within-Scale Pairwise Jaccard}
148	
149	Table~\ref{tab:within_scale_jaccard} reports the within-scale pairwise Jaccard similarity between architectures' helped and hurt sets at both scales. Mean values are similar across scales (340M: 0.094/0.090; 1.3B: 0.100/0.093), indicating that per-example architecture specificity is consistent across the two scales examined.
150	
151	\begin{table}[ht]
152	\centering
153	\small
154	\caption{Within-scale pairwise Jaccard similarity of per-example effects (pure $\to$ h3-1) on LAMBADA. Each row compares the helped (or hurt) sets of two architectures at the same scale.}
155	\label{tab:within_scale_jaccard}
156	\begin{tabular}{llcc}
157	\toprule
158	Scale & Pair & $J_{\text{helped}}$ & $J_{\text{hurt}}$ \\
159	\midrule
160	\multirow{4}{*}{340M} & GDN--RetNet & 0.092 & 0.109 \\
161	& GDN--HGRN2 & 0.084 & 0.075 \\
162	& RetNet--HGRN2 & 0.108 & 0.085 \\
163	& \textit{Mean} & \textit{0.094} & \textit{0.090} \\
164	\midrule
165	\multirow{4}{*}{1.3B} & GDN--RetNet & 0.092 & 0.103 \\
166	& GDN--HGRN2 & 0.100 & 0.088 \\
167	& RetNet--HGRN2 & 0.108 & 0.087 \\
168	& \textit{Mean} & \textit{0.100} & \textit{0.093} \\
169	\bottomrule
170	\end{tabular}
171	\end{table}
172	
173	\subsection{Cross-Scale Pairwise Jaccard}
174	
175	For each architecture, we compare the helped and hurt sets of the pure $\to$ h3-1 transition at 340M and 1.3B scale on LAMBADA.
176	The comparison uses the same classification scheme as \S\ref{ssec:per_example}: an example is ``helped'' if it is correct only in the hybrid variant and ``hurt'' if correct only in the pure baseline.
177	All pairwise Jaccard values fall below 0.10, indicating that scale variation is associated with per-example predictive multiplicity analogous to the cross-architecture effect reported in \S\ref{ssec:per_example}.
178	
179	\begin{table}[ht]
180	\centering
181	\caption{Cross-scale pairwise Jaccard similarity of per-example effects (pure $\to$ h3-1) between 340M and 1.3B on LAMBADA. All values below 0.10.}
182	\label{tab:cross_scale_jaccard}
183	\begin{tabular}{llcc}
184	\toprule
185	Architecture & Scale Pair & $J_{\text{helped}}$ & $J_{\text{hurt}}$ \\
186	\midrule
187	GDN & 340M $\leftrightarrow$ 1.3B & 0.047 & 0.087 \\
188	RetNet & 340M $\leftrightarrow$ 1.3B & 0.059 & 0.073 \\
189	HGRN2 & 340M $\leftrightarrow$ 1.3B & 0.089 & 0.055 \\
190	\midrule
191	Mean & & 0.065 & 0.072 \\
192	\bottomrule
193	\end{tabular}
194	\end{table}
195	
196	\section{Per-Example Effect Counts}\label{app:per_example_counts}
197	
198	Table~\ref{tab:per_example} reports the full per-example effect counts for each architecture at 1.3B scale.
199	
200	\begin{table}[ht]
201	\centering
202	\caption{Per-example effects of attention (pure $\to$ h3-1) on 5{,}153 LAMBADA examples at 1.3B scale. $\bar{J}$: mean pairwise Jaccard similarity with other architectures across helped and hurt sets.}
203	\label{tab:per_example}
204	\begin{tabular}{lrrrr}
205	\toprule
206	Architecture & Helped & Hurt & Net & $\bar{J}$ \\
207	\midrule
208	GDN & 462 & 615 & $-$153 & .096 \\
209	RetNet & 426 & 495 & $-$69 & .100 \\
210	HGRN2 & 548 & 395 & $+$153 & .104 \\
211	\bottomrule
212	\end{tabular}
213	\end{table}
214	
215	\section{Normalized Jaccard Effect Size}\label{app:normalized_es}
216	
217	To assess whether low observed Jaccard reflects a floor effect imposed by unequal set sizes, we compute the theoretical upper bound $J_{\max} = \min(|A|,|B|) / \max(|A|,|B|)$ and the normalized effect size $(J_{\text{obs}} - J_{\text{null}}) / (J_{\max} - J_{\text{null}})$, which measures observed overlap as a fraction of the achievable range above chance. Table~\ref{tab:normalized_es} reports per-pair results.
218	
219	\begin{table}[ht]
220	\centering
221	\small
222	\caption{Normalized Jaccard effect size for each architecture pair (1.3B h3-1 on LAMBADA). $J_{\max}$: theoretical upper bound given set sizes. Normalized ES: fraction of achievable overlap above chance.}
223	\label{tab:normalized_es}
224	\resizebox{\columnwidth}{!}{%
225	\begin{tabular}{llcccc}
226	\toprule
227	Category & Pair & $J_{\text{obs}}$ & $J_{\max}$ & $J_{\text{null}}$ & Norm.\ ES \\
228	\midrule
229	Helped & GDN--RetNet & .092 & .922 & .045 & .054 \\
230	 & GDN--HGRN2 & .100 & .843 & .051 & .062 \\
231	 & RetNet--HGRN2 & .108 & .777 & .049 & .081 \\
232	 & \textit{Mean} & \textit{.100} & \textit{.848} & \textit{.048} & \textit{.066} \\
233	\midrule
234	Hurt & GDN--RetNet & .103 & .805 & .056 & .063 \\
235	 & GDN--HGRN2 & .088 & .642 & .049 & .066 \\
236	 & RetNet--HGRN2 & .087 & .798 & .045 & .056 \\
237	 & \textit{Mean} & \textit{.093} & \textit{.748} & \textit{.050} & \textit{.062} \\
238	\bottomrule
239	\end{tabular}%
240	}
241	\end{table}
242	
243	All normalized effect sizes fall below 0.10, confirming that observed overlap reaches only 6--7\% of the theoretical maximum. The low Jaccard values cannot be attributed to set-size constraints.
244	
245	\section{ARC-Easy Per-Example Analysis}\label{app:arceasy}
246	
247	Table~\ref{tab:arceasy_effects} reports per-example effect counts on ARC-Easy ($N = 2{,}376$) at 1.3B scale for each attention ratio. Unlike LAMBADA, ARC-Easy shows no aggregate convergence ($\rho = -0.20$, $p = .783$). HGRN2 is net positive at all ratios; GDN and RetNet are mixed.
248	
249	\begin{table}[ht]
250	\centering
251	\small
252	\caption{Per-example effects on ARC-Easy at 1.3B scale. Net = helped $-$ hurt.}
253	\label{tab:arceasy_effects}
254	\resizebox{\columnwidth}{!}{%
255	\begin{tabular}{llrrr}
256	\toprule
257	Architecture & Ratio & Helped & Hurt & Net \\
258	\midrule
259	\multirow{4}{*}{GDN} & h24-1 & 178 & 185 & $-$7 \\
260	& h12-1 & 176 & 206 & $-$30 \\
261	& h6-1 & 170 & 157 & $+$13 \\
262	& h3-1 & 171 & 180 & $-$9 \\
263	\midrule
264	\multirow{4}{*}{RetNet} & h24-1 & 158 & 168 & $-$10 \\
265	& h12-1 & 163 & 146 & $+$17 \\
266	& h6-1 & 159 & 147 & $+$12 \\
267	& h3-1 & 144 & 184 & $-$40 \\
268	\midrule
269	\multirow{4}{*}{HGRN2} & h24-1 & 160 & 119 & $+$41 \\
270	& h12-1 & 159 & 111 & $+$48 \\
271	& h6-1 & 185 & 118 & $+$67 \\
272	& h3-1 & 164 & 146 & $+$18 \\
273	\bottomrule
274	\end{tabular}%
275	}
276	\end{table}
277	
278	Table~\ref{tab:arceasy_ambiguity} reports the ambiguity $\alpha$ \citep{marx2020predictive} at each attention ratio for all four main benchmarks. Within-benchmark ranges are 0.004 (HellaSwag), 0.011 (PIQA), 0.025 (ARC-Easy), and 0.022 (LAMBADA), all below the 0.03 threshold reported in \S\ref{ssec:per_example}.
279	
280	\begin{table}[ht]
281	\centering
282	\caption{Ambiguity $\alpha$ across attention ratios (1.3B scale). 95\% CI: BCa bootstrap (10{,}000 resamples) at the pure-recurrent configuration.}
283	\label{tab:arceasy_ambiguity}
284	\resizebox{\columnwidth}{!}{%
285	\begin{tabular}{lcccccc}
286	\toprule
287	Benchmark & Pure & h24-1 & h12-1 & h6-1 & h3-1 & 95\% CI (pure) \\
288	\midrule
289	PIQA & .143 & .138 & .132 & .143 & .140 & $[.127,\,.159]$ \\
290	HellaSwag & .148 & .150 & .148 & .146 & .150 & $[.141,\,.155]$ \\
291	ARC-Easy & .205 & .226 & .223 & .201 & .210 & $[.189,\,.221]$ \\
292	LAMBADA & .307 & .300 & .316 & .294 & .296 & $[.294,\,.319]$ \\
293	\bottomrule
294	\end{tabular}%
295	}
296	\end{table}
297	
298	\section{Jaccard Permutation Test}\label{app:jaccard_permutation}
299	
300	To assess whether the observed pairwise Jaccard similarities exceed what would be expected under independence, we perform a permutation test. For each architecture pair at 1.3B h3-1, we hold the helped (or hurt) set sizes fixed and randomly assign example indices to each set (10{,}000 permutations, seed 42). Table~\ref{tab:jaccard_perm} reports the observed $J$, the null baseline $J_{\text{null}}$ (mean over permutations), and the $z$-score.
301	
302	\begin{table}[ht]
303	\centering
304	\caption{Permutation test for pairwise Jaccard similarity (1.3B h3-1 on LAMBADA, 10{,}000 permutations). All observed values significantly exceed the independence baseline.}
305	\label{tab:jaccard_perm}
306	\resizebox{\columnwidth}{!}{%
307	\begin{tabular}{llcccc}
308	\toprule
309	Category & Pair & $J_{\text{obs}}$ & $J_{\text{null}}$ & $z$ & $p$ \\
310	\midrule
311	Helped & GDN--HGRN2 & .100 & .051 & 7.11 & $<$.0001 \\
312	 & GDN--RetNet & .092 & .045 & 6.75 & $<$.0001 \\
313	 & HGRN2--RetNet & .108 & .049 & 8.61 & $<$.0001 \\
314	\midrule
315	Hurt & GDN--HGRN2 & .088 & .049 & 5.91 & $<$.0001 \\
316	 & GDN--RetNet & .103 & .056 & 6.85 & $<$.0001 \\
317	 & HGRN2--RetNet & .087 & .045 & 6.05 & $<$.0001 \\
318	\bottomrule
319	\end{tabular}%
320	}
321	\end{table}
322	
323	All six comparisons yield $z > 5.9$ ($p < .0001$). The null baseline averages $J_{\text{null}} \approx 0.049$; observed values are approximately twice this level. The overlap between architectures' per-example effect sets is therefore structured rather than a product of random set overlap given the set sizes.
324	
325	\section{Transformer Entrainment Comparison}\label{app:transformer_entrainment}
326	
327	To test whether attention layers make hybrid models' per-example behavior converge toward a pure Transformer, we compare the correct-example sets of each architecture's pure and h3-1 variants against a 1.3B Transformer baseline (accuracy 48.1\%) on LAMBADA. Table~\ref{tab:transformer_jaccard} reports the Jaccard similarity between each model's correct set and the Transformer's correct set.
328	
329	\begin{table}[ht]
330	\centering
331	\caption{Jaccard similarity between each model's correct set and the Transformer correct set on LAMBADA (1.3B scale). All three h3-1 hybrids are more similar to the Transformer than their pure counterparts.}
332	\label{tab:transformer_jaccard}
333	\small
334	\begin{tabular}{lccc}
335	\toprule
336	Architecture & $J_{\text{pure,T}}$ & $J_{\text{h3-1,T}}$ & $\Delta$ \\
337	\midrule
338	GDN & 0.645 & 0.649 & $+$0.005 \\
339	RetNet & 0.679 & 0.694 & $+$0.015 \\
340	HGRN2 & 0.672 & 0.701 & $+$0.029 \\
341	\bottomrule
342	\end{tabular}
343	\end{table}
344	
345	All three architectures show positive $\Delta$: the h3-1 correct set is more similar to the Transformer correct set than the pure correct set is. The effect is strongest for HGRN2 ($+$0.029) and weakest for GDN ($+$0.005). This ordering is consistent with HGRN2 being the only architecture with a positive net per-example effect from attention (Table~\ref{tab:per_example}). The Transformer itself achieves the lowest accuracy among all models, so the convergence is not explained by hybrid models degrading toward Transformer-level performance; rather, adding attention shifts which specific examples the hybrid gets correct toward the Transformer's pattern.
346	
347	\section{Within-Architecture Per-Example Stability}\label{app:within_arch_stability}
348	
349	Per-example effect sets exhibit a three-tier Jaccard hierarchy on LAMBADA (1.3B scale). Under independence (permutation baseline), pairwise Jaccard is $J \approx 0.05$. Cross-architecture comparisons (different architectures at the same attention ratio) yield $J \approx 0.10$, approximately $2\times$ baseline. Within-architecture comparisons (same architecture across different attention ratios) yield $J \approx 0.33$, approximately $7\times$ baseline and $3\times$ the cross-architecture level. Architecture identity therefore has approximately three times the influence of attention ratio on per-example effects.
350	
351	Table~\ref{tab:within_arch_summary} reports mean within-architecture Jaccard for each architecture. HGRN2 shows the highest helped overlap and lowest hurt overlap, consistent with its monotonically increasing helped count across ratios (479 $\to$ 548).
352	
353	\begin{table}[ht]
354	\centering
355	\caption{Mean within-architecture pairwise Jaccard similarity across attention ratios (1.3B, LAMBADA). Each mean is computed over all six ratio pairs per architecture.}
356	\label{tab:within_arch_summary}
357	\begin{tabular}{lcc}
358	\toprule
359	Architecture & $\bar{J}_{\text{helped}}$ & $\bar{J}_{\text{hurt}}$ \\
360	\midrule
361	GDN & 0.338 & 0.319 \\
362	RetNet & 0.333 & 0.321 \\
363	HGRN2 & 0.373 & 0.291 \\
364	\midrule
365	\textit{Overall mean} & \textit{0.348} & \textit{0.310} \\
366	\bottomrule
367	\end{tabular}
368	\end{table}
369	
370	Table~\ref{tab:within_arch_pairwise} reports the full pairwise Jaccard matrix. Attention ratios are denoted by their h$k$-1 labels: h24-1 (4\%), h12-1 (7.7\%), h6-1 (14.3\%), h3-1 (25\%).
371	
372	\begin{table}[ht]
373	\centering
374	\small
375	\caption{Within-architecture pairwise Jaccard similarity between helped and hurt sets at different attention ratios (1.3B, LAMBADA). Each cell compares the per-example effect sets of two attention configurations within the same architecture.}
376	\label{tab:within_arch_pairwise}
377	\resizebox{\columnwidth}{!}{%
378	\begin{tabular}{llcccccc}
379	\toprule
380	 & & \multicolumn{6}{c}{Ratio pair} \\
381	\cmidrule(lr){3-8}
382	Arch & Cat & h24--h12 & h24--h6 & h24--h3 & h12--h6 & h12--h3 & h6--h3 \\
383	\midrule
384	\multirow{2}{*}{GDN} & Helped & .345 & .335 & .311 & .344 & .341 & .352 \\
385	 & Hurt & .310 & .328 & .320 & .331 & .281 & .345 \\
386	\midrule
387	\multirow{2}{*}{RetNet} & Helped & .354 & .314 & .334 & .322 & .330 & .345 \\
388	 & Hurt & .316 & .334 & .307 & .301 & .324 & .343 \\
389	\midrule
390	\multirow{2}{*}{HGRN2} & Helped & .359 & .369 & .375 & .368 & .378 & .388 \\
391	 & Hurt & .292 & .289 & .298 & .273 & .309 & .287 \\
392	\bottomrule
393	\end{tabular}%
394	}
395	\end{table}
396	
397	Adjacent ratio pairs (e.g., h24-1 vs.\ h12-1) do not exhibit systematically higher Jaccard than non-adjacent pairs (e.g., h24-1 vs.\ h3-1). Across all architectures, the mean Jaccard for adjacent pairs is 0.353 (helped) and 0.311 (hurt), compared with 0.343 (helped) and 0.310 (hurt) for non-adjacent pairs. The negligible difference indicates that the mapping from attention ratio to per-example effects is non-smooth: doubling the attention ratio does not produce a proportionally more similar set of affected examples.
398	
399	\section{Cross-Benchmark Jaccard Trajectories}\label{app:cross_bench_jaccard}
400	
401	To test whether the Jaccard stability pattern is specific to LAMBADA or a general property, we compute mean pairwise Jaccard trajectories across all four hybrid attention ratios on all four main benchmarks. Table~\ref{tab:cross_bench_jaccard} reports the results. On every benchmark, Jaccard shows no statistically significant trend with attention ratio (all $\rho \leq 0.80$, $p \geq 0.333$), with values uniformly between 0.08 and 0.11. The stability observed at the first attention level on LAMBADA (\S\ref{ssec:decoupling}) thus appears to hold across benchmarks: once any attention is present, each architecture's per-example response remains largely consistent regardless of attention ratio.
402	
403	\begin{table}[ht]
404	\centering
405	\small
406	\caption{Mean pairwise Jaccard (mean of helped and hurt sets, 3 architecture pairs) across attention ratios and benchmarks (1.3B scale). $\rho$: Spearman correlation between attention ratio and $\bar{J}$. All $p \geq 0.333$.}
407	\label{tab:cross_bench_jaccard}
408	\resizebox{\columnwidth}{!}{%
409	\begin{tabular}{@{}lcccccc@{}}
410	\toprule
411	Benchmark & h24-1 & h12-1 & h6-1 & h3-1 & $\rho$ & $p$ \\
412	\midrule
413	LAMBADA & .091 & .088 & .096 & .097 & 0.80 & .333 \\
414	HellaSwag & .084 & .081 & .091 & .086 & 0.60 & .417 \\
415	PIQA & .089 & .096 & .089 & .095 & 0.00 & 1.00 \\
416	ARC-Easy & .084 & .099 & .091 & .109 & 0.80 & .333 \\
417	\bottomrule
418	\end{tabular}}
419	\end{table}
420	
421	\section{Continuous-Threshold Jaccard Analysis}\label{app:continuous_jaccard}
422	
423	The main text binarizes per-example effects at the correctness boundary. To verify that low cross-architecture Jaccard is not an artifact of this binarization, we compute Jaccard similarity using a continuous confidence threshold $\tau$: two architectures' effect sets are defined as the examples whose target-token $|\log p|$ changes by more than $\tau$ when attention is added. On LAMBADA, mean pairwise Jaccard decreases monotonically from 0.26 ($\tau = 0.00$, any change) to 0.05 ($\tau = 0.30$, large changes only). ARC-Easy and PIQA show the same monotonic decrease. The binary threshold ($\tau = 0$, correctness flip) thus represents the upper end of cross-architecture overlap; restricting to confident transitions further reduces agreement, confirming that low Jaccard is robust to the choice of binarization threshold.
424	
425	\section{Target-Token Confidence Margin}
426	\label{app:confidence_margin}
427	
428	We analyze whether pure-model confidence on the target token predicts whether attention will help or hurt on a given example.
429	We define confidence as $|\log p_{\text{pure}}(y^*)|$, where $y^*$ is the target token: lower values indicate higher probability (near-correct).
430	We initially tested raw perplexity as a predictor of helped/hurt status, but found that within-category controls (C1/C2) are necessary to isolate attention effects from the definitional confound between pure-correct and pure-wrong populations.
431	
432	Table~\ref{tab:cm_c1} compares hurt versus stayed-right samples (both pure-correct): hurt samples have significantly lower target-token probability (higher $|\log p|$), confirming that weakly-correct predictions are vulnerable to attention disruption.
433	Table~\ref{tab:cm_c2} compares helped versus stayed-wrong samples (both pure-wrong): helped samples have higher target-token probability (lower $|\log p|$), confirming that near-miss errors are rescuable.
434	This pattern is consistent across all three architectures ($|d| = 0.73$--$0.92$, all $p < 10^{-54}$) but does not alter the cross-architecture Jaccard findings---within-architecture predictability coexists with cross-architecture divergence.
435	
436	\begin{table}[ht]
437	\centering
438	\caption{Control 1: Pure-correct samples---hurt vs.\ stayed-right. Higher mean $|\log p|$ indicates lower target-token probability (less confident correct).}
439	\label{tab:cm_c1}
440	\resizebox{\columnwidth}{!}{%
441	\begin{tabular}{lrrrrr}
442	\toprule
443	Architecture & $n_{\text{hurt}}$ & $n_{\text{stay}}$ & Hurt mean & Stay mean & Cohen's $d$ \\
444	\midrule
445	GDN (h12-1) & 519 & 2281 & 1.049 & 0.576 & 0.87 \\
446	RetNet (h3-1) & 497 & 2169 & 1.293 & 0.785 & 0.83 \\
447	HGRN2 (h3-1) & 392 & 2102 & 1.481 & 0.899 & 0.92 \\
448	\bottomrule
449	\end{tabular}
450	}
451	\end{table}
452	
453	\begin{table}[ht]
454	\centering
455	\caption{Control 2: Pure-wrong samples---helped vs.\ stayed-wrong. Lower mean $|\log p|$ indicates higher target-token probability (near-miss error).}
456	\label{tab:cm_c2}
457	\resizebox{\columnwidth}{!}{%
458	\begin{tabular}{lrrrrr}
459	\toprule
460	Architecture & $n_{\text{help}}$ & $n_{\text{stay}}$ & Help mean & Stay mean & Cohen's $d$ \\
461	\midrule
462	GDN (h12-1) & 480 & 1873 & 2.459 & 4.189 & $-$0.75 \\
463	RetNet (h3-1) & 420 & 2067 & 2.478 & 4.103 & $-$0.73 \\
464	HGRN2 (h3-1) & 548 & 2111 & 2.500 & 4.112 & $-$0.77 \\
465	\bottomrule
466	\end{tabular}
467	}
468	\end{table}
469	
470	\subsection{Cross-Benchmark Extension}\label{app:cm_cross}
471	
472	The confidence margin pattern extends beyond LAMBADA to multiple-choice benchmarks, though with smaller effect sizes. Table~\ref{tab:cm_cross_c2} reports the rescue analysis (helped vs.\ stayed-wrong) on HellaSwag and ARC-Easy. All nine comparisons (three benchmarks $\times$ three architectures) are significant, confirming that attention consistently rescues near-miss errors regardless of task type. Effect sizes range from small on HellaSwag ($d = 0.13$--$0.17$) to medium on ARC-Easy ($d = 0.51$--$0.60$), compared to large on LAMBADA ($d = 0.73$--$0.77$); the attenuation on HellaSwag reflects noisier confidence proxies under length-normalized scoring. Table~\ref{tab:cm_cross_c1} reports the disruption analysis (hurt vs.\ stayed-right); two of six comparisons are significant (all on ARC-Easy) with small effect sizes ($d = 0.13$--$0.26$), indicating that the disruption signal is weaker on multiple-choice tasks and absent on HellaSwag under \texttt{acc\_norm}. The asymmetry between rescue and disruption reflects task structure: near-miss errors are an intrinsic sample property (the model almost produced the correct answer regardless of format), while borderline correctness in multiple-choice settings depends on relative option ranking rather than absolute confidence, reducing the raw log-likelihood margin's predictive power for vulnerability.
473	
474	\begin{table}[ht]
475	\centering
476	\caption{Cross-benchmark rescue analysis (Control 2): helped vs.\ stayed-wrong on HellaSwag and ARC-Easy (1.3B h3-1).}
477	\label{tab:cm_cross_c2}
478	\resizebox{\columnwidth}{!}{%
479	\begin{tabular}{llrr}
480	\toprule
481	Benchmark & Architecture & Cohen's $d$ & $p$ \\
482	\midrule
483	HellaSwag & GDN & $-$0.166 & $6.1 \times 10^{-4}$ \\
484	 & RetNet & $-$0.132 & $1.4 \times 10^{-2}$ \\
485	 & HGRN2 & $-$0.164 & $1.4 \times 10^{-3}$ \\
486	\midrule
487	ARC-Easy & GDN & $-$0.60 & $1.0 \times 10^{-13}$ \\
488	 & RetNet & $-$0.51 & $5.3 \times 10^{-10}$ \\
489	 & HGRN2 & $-$0.53 & $5.4 \times 10^{-10}$ \\
490	\bottomrule
491	\end{tabular}%
492	}
493	\end{table}
494	
495	\begin{table}[ht]
496	\centering
497	\caption{Cross-benchmark disruption analysis (Control 1): hurt vs.\ stayed-right on HellaSwag and ARC-Easy (1.3B h3-1).}
498	\label{tab:cm_cross_c1}
499	\resizebox{\columnwidth}{!}{%
500	\begin{tabular}{llrrl}
501	\toprule
502	Benchmark & Architecture & Cohen's $d$ & $p$ & Sig.? \\
503	\midrule
504	HellaSwag & GDN & 0.009 & .999 & No \\
505	 & RetNet & $-$0.035 & .453 & No \\
506	 & HGRN2 & $-$0.062 & .274 & No \\
507	\midrule
508	ARC-Easy & GDN & 0.26 & $3.2 \times 10^{-4}$ & Yes \\
509	 & RetNet & 0.22 & $2.8 \times 10^{-3}$ & Yes \\
510	 & HGRN2 & 0.13 & .145 & No \\
511	\bottomrule
512	\end{tabular}%
513	}
514	\end{table}
515	
516	\subsection{Prediction Framework}\label{app:prediction_framework}
517	
518	We formalize the confidence margin analysis as a binary prediction task: given a pure-model example and its target-token $|\log p|$, predict whether attention will change the example's correctness. Using the within-category summary statistics (Tables~\ref{tab:cm_c1},~\ref{tab:cm_c2}), we derive analytic AUC from Cohen's $d$ via $\text{AUC} = \Phi(|d|/\sqrt{2})$ and compute Gaussian-intersection thresholds (the $|\log p|$ value at which the two group densities intersect under equal priors).
519	
520	Table~\ref{tab:prediction_auc} reports within-architecture prediction performance. All AUCs exceed 0.69, indicating moderate within-architecture predictive discrimination for attention effects. Disruption prediction is consistently stronger than rescue (mean AUC 0.73 vs.\ 0.70), reflecting the larger effect sizes in Control~1.
521	
522	\begin{table}[ht]
523	\centering
524	\small
525	\caption{Within-architecture prediction of attention effects on LAMBADA (1.3B). AUC$_p$: parametric (from Cohen's $d$); AUC$_e$: empirical (non-parametric).}
526	\label{tab:prediction_auc}
527	\resizebox{\columnwidth}{!}{%
528	\begin{tabular}{@{}lcccccc@{}}
529	\toprule
530	Architecture & \multicolumn{3}{c}{Rescue} & \multicolumn{3}{c}{Disruption} \\
531	\cmidrule(lr){2-4} \cmidrule(lr){5-7}
532	 & AUC$_p$ & AUC$_e$ & $d$ & AUC$_p$ & AUC$_e$ & $d$ \\
533	\midrule
534	GDN (h12-1) & .701 & .756 & 0.75 & .732 & .742 & 0.87 \\
535	RetNet (h3-1) & .696 & .754 & 0.73 & .722 & .735 & 0.83 \\
536	HGRN2 (h3-1) & .708 & .765 & 0.77 & .743 & .748 & 0.92 \\
537	\midrule
538	Mean & .702 & .758 & --- & .732 & .742 & --- \\
539	\bottomrule
540	\end{tabular}}
541	\end{table}
542	
543	\paragraph{Normality verification.} Shapiro-Wilk tests reject normality for all six architecture--set combinations (all $W < 0.98$, $p < 10^{-6}$), but the practical departure varies by group. Disruption-set $|\log p|$ values show mild skewness (0.53--0.77, $W \in [0.955, 0.973]$), closely approximating a normal distribution at the sample sizes involved. Rescue-set values are moderately right-skewed (skewness 1.33--1.41, $W \in [0.899, 0.920]$), following an approximately log-normal distribution. Because the skew is one-sided, parametric AUC estimates (0.70--0.74 in the main text) are conservative lower bounds; non-parametric empirical AUC from the same data yields 0.73--0.77.
544	
545	Despite similar within-architecture AUC, the optimal prediction thresholds differ across architectures for disruption but not rescue (Table~\ref{tab:threshold_gap}). Rescue thresholds cluster tightly (range 0.03 in $|\log p|$), indicating that the rescuability boundary---the confidence level below which pure-wrong examples are likely to be corrected by attention---is architecture-invariant. Disruption thresholds span a 47\% relative range (GDN: 0.70, RetNet: 1.00, HGRN2: 1.14), meaning that the same confidence level on a pure-correct example may predict vulnerability in one architecture but safety in another. This asymmetry constitutes a second dimension of multiplicity beyond per-example disagreement: all three architectures agree on which wrong answers are rescuable, but disagree on which correct answers are vulnerable to disruption.
546	
547	\begin{table}[ht]
548	\centering
549	\small
550	\caption{Gaussian-intersection prediction thresholds ($|\log p|$) across architectures. Relative spread: range/mean.}
551	\label{tab:threshold_gap}
552	\resizebox{\columnwidth}{!}{%
553	\begin{tabular}{@{}lccccr@{}}
554	\toprule
555	 & GDN & RetNet & HGRN2 & Range & Rel.\ spread \\
556	\midrule
557	Rescue & 3.32 & 3.29 & 3.31 & 0.03 & 1.0\% \\
558	Disruption & 0.70 & 1.00 & 1.14 & 0.44 & 46.7\% \\
559	\bottomrule
560	\end{tabular}}
561	\end{table}
562	
563	\section{Calibration Analysis}\label{app:calibration}
564	
565	Cross-architecture disruption threshold variation (\S\ref{ssec:per_example}) could in principle arise from calibration differences rather than genuine differences in per-example processing. We compute expected calibration error (ECE; \citealt{guo2017calibration}) for each architecture's h3-1 model on LAMBADA using 15 equal-width bins. ECE values are similar: GDN 0.222, RetNet 0.224, HGRN2 0.235. The cross-architecture ECE spread (6\%, computed as range/mean) is less than half the disruption threshold spread (47\%; Table~\ref{tab:threshold_gap}), indicating that calibration differences are insufficient to account for the observed threshold divergence. Rescue thresholds, which show only 1\% cross-architecture spread, are consistent with near-identical calibration in the low-confidence regime.
566	
567	\section{BoolQ Supplementary Analysis}
568	\label{app:boolq}
569	
570	BoolQ ($N = 3{,}270$; comprehension, binary yes/no classification) shows the highest ambiguity among the benchmarks we analyzed ($\alpha \approx 0.45$), but the Jaccard significance pattern is mixed: only 12 of 24 architecture $\times$ attention-ratio pair combinations yield $p < .01$. In particular, the RetNet--HGRN2 pair produces 0/8 significant Jaccard values, with several normalized effect sizes below zero, suggesting anti-correlated per-example effects for this pair.
571	
572	\paragraph{Binary classification baseline.} BoolQ is binary classification (two answer choices), whereas LAMBADA, HellaSwag, and ARC-Easy involve open vocabulary prediction or four-way multiple choice. Under a binary task, the null Jaccard baseline $J_{\text{null}}$ is higher because chance overlap between helped/hurt sets is larger when there are fewer ways to be wrong. This elevates the significance threshold: observed Jaccard must be substantially higher to exceed the null, which explains why 12/24 pairs fail to reach significance despite $\bar{J}_h = 0.103$ and $\bar{J}_u = 0.098$---values comparable to the four main benchmarks.
573	
574	\paragraph{Per-example summary.} Table~\ref{tab:boolq_multiplicity} reports the key metrics. The high $\alpha$ reflects that BoolQ examples are more sensitive to architectural variation in the presence of attention: approximately half of all examples change correctness status for at least one architecture. However, the mixed Jaccard significance prevents us from confidently concluding that the cross-architecture overlap structure matches the pattern observed on the four main benchmarks.
575	
576	\begin{table}[ht]
577	\centering
578	\small
579	\caption{BoolQ predictive multiplicity at 1.3B (h3-1).}
580	\label{tab:boolq_multiplicity}
581	\begin{tabular}{@{}lcccccc@{}}
582	\toprule
583	 & $N$ & $\alpha$ & $\bar{J}_{h}$ & $\bar{J}_{u}$ & Sig.\ pairs & $\rho_\alpha$ \\
584	\midrule
585	BoolQ & 3270 & .45 & .103 & .098 & 12/24 & $+0.1$ \\
586	\bottomrule
587	\end{tabular}
588	\par\vspace{1pt}
589	{\footnotesize RetNet--HGRN2: 0/8 significant; multiple normalized ES $< 0$.}
590	\end{table}
591	
592	The significant Jaccard overlap concentrates in GDN--RetNet pairs (8/8 significant), while RetNet--HGRN2 shows none (0/8). This pair-specificity does not appear on the four main benchmarks, where all architecture pairs show significant overlap; it may reflect a BoolQ-specific interaction between binary classification structure and particular recurrent architectures rather than a general property of architecture pairs.
593	
594	\paragraph{Confidence margin.} Confidence margin analysis on BoolQ shows the rescue pattern (C2) partially holds (2/3 architectures significant, $d = 0.16$--$0.36$) but the disruption pattern (C1) is absent (0/3, $|d| \leq 0.10$), consistent with compressed log-likelihood ranges in binary classification reducing the predictive power of confidence margins. This extends the gradient observed across LAMBADA, ARC-Easy, and HellaSwag: C1 effect sizes decrease from open-ended prediction ($d \approx 0.9$, LAMBADA) through ARC-Easy ($d \approx 0.1$--$0.3$) to HellaSwag ($d \approx 0$ under \texttt{acc\_norm}) and binary classification ($d \approx 0$, BoolQ). The gradient broadly tracks the coefficient of variation (CV) of the log-likelihood confidence proxy: LAMBADA ($\text{CV} = 0.75$) $>$ ARC-Easy ($0.54$) $>$ HellaSwag ($0.49$) $>$ BoolQ ($0.22$). BoolQ's high-frequency short completions (``\,yes''/``\,no'') yield elevated baseline log-likelihoods (mean $|\text{loglik}| = 3.04$ vs.\ $0.84$ for LAMBADA) with similar absolute spread (IQR $\approx 0.9$), compressing the relative variation and rendering the confidence margin unable to separate borderline-correct from robustly-correct examples.
595	
596	\paragraph{Interpretation.} The RetNet--HGRN2 anti-correlation may reflect different error modes specific to binary classification: when one architecture's recurrent state resolves a yes/no ambiguity through attention, the other architecture's resolution may be disrupted by the same attention intervention. This pattern warrants further investigation with additional binary classification benchmarks to determine whether it is BoolQ-specific or characteristic of two-choice tasks more broadly.
597	
598	\section{WinoGrande Supplementary Analysis}
599	\label{app:winogrande}
600	
601	WinoGrande ($N = 1{,}267$; reasoning, two-choice coreference resolution) shows high ambiguity ($\alpha \approx 0.41$ at h3-1) but mixed Jaccard significance: 10 of 24 architecture $\times$ attention-ratio pair combinations yield $p < .01$. Mean pairwise Jaccard ($\bar{J}_h = 0.110$, $\bar{J}_u = 0.103$) is comparable to the four main benchmarks, but the elevated null baseline from near-chance accuracy (${\sim}60\%$) reduces statistical power to detect above-chance overlap.
602	
603	\paragraph{Near-chance accuracy.} WinoGrande accuracy across hybrid configurations ranges from 59\% to 62\%, close to the two-choice chance level of 50\%. At near-chance accuracy, a large fraction of examples are borderline---small perturbations (such as adding attention) can flip predictions in either direction, inflating the helped and hurt sets and consequently $\alpha$. This structural property, shared with BoolQ (${\sim}59\%$ accuracy, $\alpha \approx 0.45$), may partially explain the elevated $\alpha$ rather than task-intrinsic multiplicity. PIQA (73\% accuracy, $\alpha = 0.14$) and HellaSwag (60\% normalized accuracy, $\alpha = 0.15$) demonstrate that near-chance accuracy is not the sole driver, but we cannot fully exclude it as a contributing factor for WinoGrande and BoolQ.
604	
605	\begin{table}[ht]
606	\centering
607	\small
608	\caption{WinoGrande predictive multiplicity at 1.3B (h3-1).}
609	\label{tab:winogrande_multiplicity}
610	\resizebox{\columnwidth}{!}{%
611	\begin{tabular}{@{}lcccccc@{}}
612	\toprule
613	 & $N$ & $\alpha$ & $\bar{J}_{h}$ & $\bar{J}_{u}$ & Sig.\ pairs & $\rho_\alpha$ \\
614	\midrule
615	WinoGrande & 1267 & .41 & .110 & .103 & 10/24 & $-0.9$ \\
616	\bottomrule
617	\end{tabular}}
618	\par\vspace{1pt}
619	{\footnotesize $\alpha$ variation across ratios: 0.054 ($> 0.03$ threshold of main benchmarks).}
620	\end{table}
621	
622	\section{340M Per-Example Analysis}\label{app:scale_per_example}
623	
624	\subsection{LAMBADA}
625	
626	At 340M, LAMBADA per-example multiplicity closely matches the 1.3B pattern: $\alpha = 0.313$ (vs.\ 0.307 at 1.3B), with mean pairwise Jaccard $\bar{J} \approx 0.089$ (vs.\ 0.095). Per-example directionality is preserved: HGRN2 shows net positive effects at h3-1 ($+238$ examples), while GDN ($-256$) and RetNet ($-106$) show net negative effects, mirroring the 1.3B profile (HGRN2 $+153$, GDN $-153$, RetNet $-69$).
627	
628	However, aggregate convergence is absent at 340M: $\rho = -0.50$ ($p = .45$), with non-monotonic $\sigma$ across attention ratios ($0.025 \to 0.012 \to 0.018 \to 0.011 \to 0.016$). This contrasts sharply with 1.3B ($\rho = -1.0$, $p = .017$, monotonic $\sigma$ decrease). The decoupling between per-example divergence and aggregate convergence thus manifests differently across scales: at 340M, per-example multiplicity is present but aggregate convergence is not, suggesting that convergence requires sufficient model capacity while multiplicity does not.
629	
630	Within-benchmark $\alpha$ variation across attention ratios is also larger at 340M (0.047, from 0.313 at pure to 0.266 at h3-1) than at 1.3B ($< 0.03$; \S\ref{ssec:per_example}), suggesting that smaller models are more sensitive to the attention ratio in terms of per-example disagreement patterns.
631	
632	\begin{table}[ht]
633	\centering
634	\small
635	\caption{340M vs.\ 1.3B LAMBADA comparison.}
636	\label{tab:scale_comparison}
637	\begin{tabular}{@{}lcc@{}}
638	\toprule
639	 & 340M & 1.3B \\
640	\midrule
641	$\alpha$ (pure) & .313 & .307 \\
642	$\bar{J}$ (h3-1) & .089 & .095 \\
643	$\rho_\sigma$ & $-0.50$ & $-1.0$ \\
644	$p$ & .45 & .017 \\
645	GDN net & $-256$ & $-153$ \\
646	HGRN2 net & $+238$ & $+153$ \\
647	\bottomrule
648	\end{tabular}
649	\end{table}
650	
651	\subsection{Cross-Benchmark Scale Comparison}
652	
653	Table~\ref{tab:340m_multi_bench} extends the scale comparison to all four main benchmarks. Two patterns emerge. First, $\alpha$ is systematically higher at 340M across all benchmarks, with the largest gap on ARC-Easy ($+$8.4pp) and the smallest on LAMBADA ($+$0.6pp). Second, pairwise Jaccard remains stable across scales ($\bar{J}_h = 0.08$--$0.10$ at both scales); three-architecture results are stable across both 340M and 1.3B scales (Jaccard $\approx$ 0.08--0.10), providing indirect support for consistency across these two scales. This suggests that the qualitative pattern of per-example multiplicity---which architectures affect which examples---is consistent across the two scales examined, even as its magnitude increases at smaller scale. Notably, the $\alpha$ inflation does not track accuracy loss: HellaSwag has the largest accuracy gap between scales yet the smallest $\Delta\alpha$ ($+$1.9pp), while ARC-Easy has a smaller accuracy gap but the largest $\Delta\alpha$ ($+$8.4pp), arguing against accuracy as the primary driver of scale-dependent multiplicity.
654	
655	\begin{table}[ht]
656	\centering
657	\small
658	\caption{340M vs.\ 1.3B per-example multiplicity across four benchmarks. $\alpha$: ambiguity at pure-recurrent configuration. Acc: mean accuracy across three architectures at pure-recurrent. $\bar{J}_{h}$/$\bar{J}_{u}$: mean pairwise Jaccard of helped/hurt sets. $\Delta\alpha$: 340M $-$ 1.3B.}
659	\label{tab:340m_multi_bench}
660	\resizebox{\columnwidth}{!}{%
661	\begin{tabular}{lcccccccr}
662	\toprule
663	 & \multicolumn{4}{c}{340M} & \multicolumn{3}{c}{1.3B} & \\
664	\cmidrule(lr){2-5} \cmidrule(lr){6-8}
665	Benchmark & Acc & $\alpha$ & $\bar{J}_{h}$ & $\bar{J}_{u}$ & $\alpha$ & $\bar{J}_{h}$ & $\bar{J}_{u}$ & $\Delta\alpha$ \\
666	\midrule
667	PIQA & .663 & .181 & .090 & .085 & .143 & .091 & .094 & $+$.038 \\
668	HellaSwag$^\dagger$ & .420 & .167 & .084 & .083 & .148 & .095 & .085 & $+$.019 \\
669	ARC-Easy & .594 & .289 & .098 & .103 & .205 & .092 & .099 & $+$.084 \\
670	LAMBADA & --- & .313 & .089 & .090 & .307 & .095 & .093 & $+$.006 \\
671	\bottomrule
672	\multicolumn{9}{l}{\footnotesize $^\dagger$\texttt{acc\_norm}. LAMBADA accuracy omitted (evaluated in separate run).}
673	\end{tabular}%
674	}
675	\end{table}
676	
677	Convergence is absent at 340M across all benchmarks (all $|\rho| \leq 0.4$, $p \geq .45$), in contrast to 1.3B where LAMBADA shows monotonic convergence. The absence of convergence at 340M extends beyond LAMBADA to HellaSwag ($\rho = 0.4$, $p = .52$), PIQA ($\rho = 0.3$, $p = .68$), and ARC-Easy ($\rho = -0.1$, $p = .95$).
678	
679	\section{Subsample Sensitivity of \texorpdfstring{$\alpha$}{α}}\label{app:subsample_sensitivity}
680	
681	To assess the reliability of $\alpha$ estimation at different sample sizes, we repeatedly subsample each benchmark (1{,}000 bootstrap replicates, seed 42) and compute the 95\% CI width of $\alpha$.
682	
683	\begin{table}[ht]
684	\centering
685	\small
686	\caption{$\alpha$ estimation stability: 95\% CI width by subsample size.}
687	\label{tab:subsample}
688	\resizebox{\columnwidth}{!}{%
689	\begin{tabular}{@{}lrrrrr@{}}
690	\toprule
691	Benchmark & $n = 100$ & $n = 200$ & $n = 500$ & $n = 1000$ & Full $N$ \\
692	\midrule
693	PIQA & .130 & .095 & .066 & .045 & .034 \\
694	HellaSwag & .140 & .100 & .062 & .044 & .013 \\
695	ARC-Easy & .160 & .105 & .072 & .050 & .032 \\
696	LAMBADA & .180 & .125 & .082 & .057 & .025 \\
697	\bottomrule
698	\end{tabular}}
699	\par\vspace{1pt}
700	{\footnotesize At $n = 100$, CI width (0.13--0.18) spans the entire four-benchmark $\alpha$ range (0.14--0.30), rendering $\alpha$ estimation unreliable. This justifies excluding COPA ($n = 100$) from the per-example analysis.}
701	\end{table}
702	
703	\section{Complementarity Decomposition}\label{app:complementarity}
704	
705	We decompose the three-architecture vote on each example into four categories: unanimous correct (3/3), majority correct (2/3), minority correct (1/3), and unanimous wrong (0/3). This decomposition explains the structural failure of majority vote despite substantial per-example complementarity.
706	
707	Table~\ref{tab:complementarity} reports the decomposition at h3-1 (25\% attention). Majority vote benefits only from 2/3 examples (where the correct answer holds a majority) but is actively harmed by 1/3 examples (where the correct architecture is outvoted). On LAMBADA, HellaSwag, and ARC-Easy, the MV exploitation ratio---the fraction of complementary examples where MV selects correctly---hovers near 51\%, indicating a near-even split between MV-exploitable and MV-hostile disagreements. The oracle, by contrast, exploits both categories, explaining the large oracle--MV gap ($+7$--$14$\,pp).
708	
709	\begin{table}[ht]
710	\centering
711	\small
712	\caption{Complementarity decomposition at 1.3B h3-1. Fractions of total examples in each vote category. MV expl.: fraction of complementary examples where majority vote is correct.}
713	\label{tab:complementarity}
714	\begin{tabular}{@{}lccccr@{}}
715	\toprule
716	Benchmark & 3/3 & 2/3 & 1/3 & 0/3 & MV expl. \\
717	\midrule
718	LAMBADA & .361 & .151 & .145 & .343 & 51.1\% \\
719	HellaSwag & .519 & .078 & .073 & .331 & 51.6\% \\
720	ARC-Easy & .603 & .107 & .103 & .187 & 50.9\% \\
721	BoolQ & .376 & .257 & .197 & .170 & 56.6\% \\
722	\bottomrule
723	\end{tabular}
724	\end{table}
725	
726	This near-50\% exploitation ratio is structurally invariant across attention ratios: on LAMBADA, the ratio ranges from 51.1\% to 54.4\% across all five configurations; on HellaSwag, from 50.3\% to 51.6\%. Attention changes neither the amount nor the structure of cross-architecture complementarity.
727	
728	\section{Seed-Variation Calibration}\label{app:seed_calibration}
729	
730	To contextualize the $3\times$ within- vs.\ cross-architecture Jaccard gap (\S\ref{ssec:decoupling}), we compare against within-seed variation using the Pythia 70M \citep{biderman2023pythia} PolyPythias models \citep{vanderwal2025polypythias}, which provide 9 individually trained seeds of the same architecture.
731	
732	On LAMBADA ($N = 5{,}153$), within-seed mean Jaccard is $\bar{J}_h = 0.273$ (helped) and $\bar{J}_u = 0.393$ (hurt), compared to our cross-architecture reference $J \approx 0.10$. On ARC-Easy ($N = 2{,}376$), within-seed $\bar{J}_h = 0.312$ and $\bar{J}_u = 0.354$, versus cross-architecture $J \approx 0.092$. Within-seed ambiguity is $\alpha = 0.36$ (LAMBADA) and $\alpha = 0.49$ (ARC-Easy), compared to cross-architecture $\alpha = 0.30$ and $0.21$ respectively.
733	
734	Seeds thus produce comparable or higher amounts of per-example disagreement ($\alpha$) but on more overlapping examples (higher $J$). Cross-architecture variation is associated with per-example effects on less overlapping examples (lower $J$), consistent with architecture-associated divergence yielding qualitatively different per-example patterns than seed noise. The within-seed Jaccard is 2.7--4.3$\times$ higher than cross-architecture Jaccard across both benchmarks.
735	
736	Three caveats qualify this comparison. First, scale mismatch: Pythia 70M is $5\times$ smaller than our smallest models (340M); attempts to use Pythia 410M failed repeatedly. Second, architecture family: Pythia is a standard Transformer, not a hybrid recurrent architecture, so this is a cross-family reference point rather than a matched control. Third, accuracy regime: Pythia 70M accuracy (LAMBADA 0.17--0.23, ARC-Easy ${\sim}$0.38) is far below our models (${\sim}$0.50, ${\sim}$0.72), and Jaccard is affected by base rates; the 2.7--4.3$\times$ ratio may differ at accuracy regimes closer to our main experiments. These limitations restrict the comparison to a reference point for seed-variation magnitude rather than definitive evidence for architecture-driven effects.
737	
738	\section{Extended Architecture Validation (Five Architectures)}\label{app:extended_arch}
739	
740	To test whether the low cross-architecture Jaccard pattern generalizes beyond the three primary architectures, we extend the analysis to include two additional architectures from the same model zoo: GLA (Gated Linear Attention) and DeltaNet, yielding ten pairwise comparisons. Both are available only at 340M in the model zoo; all results below use the h3-1 (25\% attention) configuration. This extension validates per-example divergence (not aggregate convergence).
741	
742	\begin{center}
743	\small
744	\captionof{table}{Pairwise Jaccard similarity across five architectures (340M, h3-1). All 40 permutation tests yield $p \leq .002$ ($z = 3.49$--$12.21$).}
745	\label{tab:extended_arch_jaccard}
746	\begin{tabular}{@{}llcc@{}}
747	\toprule
748	Benchmark & Pair & $J_h$ & $J_u$ \\
749	\midrule
750	\multirow{11}{*}{LAMBADA} & GDN--RetNet & .128 & .121 \\
751	 & GDN--HGRN2 & .123 & .083 \\
752	 & GDN--GLA & .124 & .100 \\
753	 & GDN--DeltaNet & .115 & .100 \\
754	 & RetNet--HGRN2 & .108 & .083 \\
755	 & RetNet--GLA & .123 & .107 \\
756	 & RetNet--DeltaNet & .115 & .096 \\
757	 & HGRN2--GLA & .127 & .086 \\
758	 & HGRN2--DeltaNet & .125 & .090 \\
759	 & GLA--DeltaNet & .134 & .081 \\
760	 & \textit{Mean} & \textit{.122} & \textit{.095} \\
761	\midrule
762	\multirow{11}{*}{ARC-Easy} & GDN--RetNet & .089 & .114 \\
763	 & GDN--HGRN2 & .122 & .105 \\
764	 & GDN--GLA & .114 & .106 \\
765	 & GDN--DeltaNet & .084 & .102 \\
766	 & RetNet--HGRN2 & .087 & .115 \\
767	 & RetNet--GLA & .112 & .110 \\
768	 & RetNet--DeltaNet & .138 & .123 \\
769	 & HGRN2--GLA & .098 & .087 \\
770	 & HGRN2--DeltaNet & .109 & .088 \\
771	 & GLA--DeltaNet & .129 & .098 \\
772	 & \textit{Mean} & \textit{.108} & \textit{.105} \\
773	\bottomrule
774	\end{tabular}
775	\end{center}
776	
777	% Figure moved to main text (\S\ref{ssec:robustness})
778	
779	All pairwise Jaccard values remain $\leq 0.14$, consistent with the three-architecture results at 1.3B (Table~\ref{tab:per_example}). The seven new pairs involving GLA and DeltaNet show no systematic difference from the original three pairs (Mann-Whitney $p > .3$ for both helped and hurt), indicating that the low-overlap pattern is not specific to the original architecture triple. A sixth architecture (HGRN; \citealp{qin2023hierarchically}) is also available in the zoo but excluded from the main analysis: its substantially lower baseline accuracy on LAMBADA (0.263 vs.\ 0.32--0.38 for the other five) mechanically inflates helped-set sizes and Jaccard values. All 15 six-architecture permutation tests nonetheless remain significant ($z \geq 2.9$, $p \leq .006$). The same pattern holds on HellaSwag ($N = 10{,}042$) and PIQA ($N = 1{,}838$): all 20 additional pairwise tests yield $p < .01$ with mean $J_{\text{helped}} \leq 0.10$. Full four-benchmark and six-architecture data are included in our code release.
780	
781	\section{Code, Data, and Computational Resources}
782	\label{app:code_data}
783	
784	All models are from the publicly available model zoo of \citet{wang2025hybrid}. Analysis code and per-example evaluation outputs are available at \url{https://anonymous.4open.science/r/entrainment_gated_ft-9444/}.
785	
786	\paragraph{Compute.} All experiments are inference-only (no training). Evaluations were conducted on a single NVIDIA RTX PRO 6000 GPU with approximately 5 GPU-hours total across all 30 model configurations and 10 benchmarks. Statistical analyses (permutation tests, bootstrap CIs, Jaccard computations) ran on CPU in under 1 hour.
787	
788	\section{Use of AI Assistants}
789	\label{app:ai-assistants}
790	
791	We used Claude (Anthropic) as an AI coding and writing assistant
792	throughout this work. Specifically:
793	\begin{itemize}
794	    \item \textbf{Code:} drafting experiment scripts, data-processing
795	    pipelines, and analysis utilities; debugging and refactoring.
796	    \item \textbf{Writing:} drafting and revising paper sections,
797	    polishing prose, and reformatting \LaTeX{}.
798	    \item \textbf{Literature:} summarizing related papers to inform
799	    the related-work section.
800	\end{itemize}
801	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1bec8b13-581d-42cb-92b6-a94f2d492b75",
  "isSidechain": false,
  "promptId": "73d622e8-44a2-4ef1-8f25-89dbf02b8b7b",
  "type": "user",
  "uuid": "d397ccb6-d646-41c3-8c5c-578a53568ee1",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/appendix.tex",
      "content": "% Appendix sections for the paper.\n\n\\section{Confirmatory and Exploratory Analyses}\\label{app:benchmark_details}\n\nThe task taxonomy used in \\S\\ref{ssec:task_taxonomy} was defined prior to running any convergence analyses. Each benchmark was assigned to exactly one of four categories based on the primary cognitive demand of the task:\n\n\\begin{itemize}\n    \\item \\textbf{Retrieval}: tasks requiring prediction from long-range context without multi-step reasoning (LAMBADA).\n    \\item \\textbf{Comprehension}: reading comprehension with explicit passage support (BoolQ).\n    \\item \\textbf{Reasoning}: tasks requiring commonsense inference or multi-step reasoning (HellaSwag, ARC-Challenge, WinoGrande, PIQA).\n    \\item \\textbf{Mixed}: tasks combining retrieval, comprehension, and reasoning demands (ARC-Easy, MMLU, SciQ, XStoryCloze).\n\\end{itemize}\n\n\\paragraph{Confirmatory benchmark set.} Six benchmarks were designated as confirmatory for Bonferroni correction: LAMBADA, HellaSwag, ARC-Challenge, WinoGrande, ARC-Easy, and MMLU. These were selected as representative of retrieval, reasoning, and mixed categories before any convergence analysis was performed. The taxonomy and benchmark selection were fixed before analysis as an informal pre-analysis plan; we describe this as a confirmatory/exploratory split rather than a formal pre-registration, since no external timestamp exists. The main text applies the more conservative all-10-benchmark correction (Bonferroni-adjusted $p = .017 \\times 10 = .170$). \\textbf{Sensitivity:} correcting across only the six confirmatory benchmarks yields adjusted $p = .017 \\times 6 = .100$, still above conventional significance.\n\n\\paragraph{One-sided test.} If one adopts the prior that attention should reduce cross-architecture variance, the one-sided permutation $p$-value for LAMBADA is $1/120 \\approx 0.0083$. Under 10-benchmark Bonferroni correction, this yields an adjusted $p = 0.083$, above the conventional threshold. We report two-sided tests throughout the main text as the more conservative choice; the one-sided result is noted here for completeness.\n\n\\paragraph{Exploratory benchmarks.} Four additional benchmarks (BoolQ, PIQA, SciQ, XStoryCloze) were added as exploratory tests. All benchmarks share the same 10-benchmark correction (adjusted threshold $\\alpha / 10 = 0.005$) and the four exploratory benchmarks are labeled as such throughout the paper. The all-10 Bonferroni correction reported in the main text is the only correction used for inference; the exploratory 6-benchmark subset correction in this appendix is provided for transparency.\n\n\\paragraph{Supplementary benchmark.} COPA ($n = 100$) is treated as supplementary due to its small sample size. It is excluded from both correction families and reported separately with the $\\dagger$ annotation in Table~\\ref{tab:convergence}.\n\n\\section{Convergence Detail}\\label{app:convergence_detail}\n\n% Figure moved to main text (\\S\\ref{ssec:decoupling}).\n\nBeyond LAMBADA ($\\rho = -1.0$), two benchmarks show moderate negative correlations that do not reach significance: ARC-Easy and MMLU (both $\\rho = -0.7$, $p = .233$). Both are classified as ``Mixed'' tasks combining retrieval with reasoning demands. The sensitivity analysis (Appendix~\\ref{app:sensitivity}) shows that MMLU's correlation reverses upon GDN exclusion ($\\rho = +0.6$), indicating dependence on a single architecture; ARC-Easy's correlation is more stable. COPA ($n = 100$; supplementary) shows $\\rho = -0.67$ with a large $\\sigma$ ratio (5.57), consistent with LAMBADA's pattern but unreliable due to small sample size.\n\nSeveral benchmarks show positive or near-zero $\\rho$ (BoolQ: $+0.2$; ARC-C: $+0.6$; HellaSwag: $+0.3$; WinoGrande: $+0.1$; SciQ: $+0.1$), indicating that attention does not systematically reduce cross-architecture variance on reasoning or comprehension tasks. The contrast with LAMBADA is consistent with attention's convergence benefit being specific to tasks requiring direct token-level recall \\citep{arora2024zoology,arora2024based} rather than multi-step inference.\n\n\\paragraph{Regression to the mean.} The direction of LAMBADA's aggregate convergence is consistent with regression to the mean: GDN (highest pure accuracy, 0.543) declines to 0.513 under h3-1, while HGRN2 (lowest, 0.484) rises to 0.514, yielding a $5\\times$ $\\sigma$ compression ($0.024 \\to 0.005$). However, three observations argue against a purely statistical artifact. First, the $5\\times$ reduction in cross-architecture $\\sigma$ far exceeds typical regression amplitudes. Second, the direction is entirely determined by architecture identity, not random fluctuation: HGRN2 accuracy increases monotonically across all attention ratios, while GDN decreases monotonically---a pattern inconsistent with noise-driven mean reversion. Third, per-example analysis (\\S\\ref{ssec:per_example}) reveals architecture-specific patterns: GDN's net $-153$ examples and HGRN2's net $+153$ examples reflect distinct helped/hurt profiles with low cross-architecture Jaccard overlap, indicating that the aggregate convergence arises from structured, architecture-dependent per-example changes rather than symmetric regression.\n\n\\section{Scale-Dependent Convergence}\\label{app:scale_convergence}\n\nAt 1.3B parameters, LAMBADA convergence is monotonic: $\\sigma$ decreases at every attention level from 0\\% through 25\\% ($\\rho = -1.0$). At 340M, convergence is partial: $\\sigma$ reaches a maximum reduction of 56\\% at intermediate attention ratios but rebounds at h3-1, yielding a net endpoint reduction of 36\\%. The trajectory is non-monotonic, and the highest-attention model does not achieve the lowest cross-architecture variance. One possible interpretation is that at smaller scale, the capacity overhead of attention layers creates interference that offsets the retrieval benefit.\n\nThis contrast is a preliminary observation from two data points (not a scaling law). Despite the aggregate divergence at 340M, mean pairwise Jaccard is similar at both scales ($J \\approx 0.09$), extending the decoupling observation (\\S\\ref{ssec:decoupling}) to the scale dimension.\n\n\\section{Sensitivity Analyses}\\label{app:sensitivity}\n\n\\subsection{Bootstrap Confidence Intervals}\n\nWe construct 95\\% bootstrap confidence intervals for the Spearman $\\rho$ between attention ratio and cross-architecture $\\sigma$ on LAMBADA using 10{,}000 resamples at the architecture level ($n = 3$ architectures). Of these resamples, 11.25\\% are degenerate: they consist of same-architecture triplicates, which produce a constant $\\sigma$ vector and therefore an undefined $\\rho$ (division by zero in the rank correlation formula). These are excluded from the confidence interval computation because they carry no information about the correlation, not because they represent $\\rho = 0$.\n\nThe BCa (bias-corrected and accelerated) correction degenerates at the $\\rho = -1.0$ boundary because the acceleration parameter requires finite jackknife variance, which collapses when the point estimate is at the distributional limit. We therefore report percentile confidence intervals instead. From the 88.75\\% informative resamples, the 95\\% percentile CI is $[-1.0,\\,-0.7]$, which excludes zero.\n\n\\subsection{GDN Exclusion Sensitivity}\n\nThe GDN h3-1 configuration uses 16 attention heads rather than 32 (see Appendix~\\ref{app:gdn_confound}). To assess the influence of this confound, we recompute all convergence correlations after excluding GDN, leaving two architectures (RetNet, HGRN2) at five attention ratios.\n\nTable~\\ref{tab:gdn_sensitivity} reports the results for benchmarks where the correlation changes by $|\\Delta\\rho| \\geq 0.3$. LAMBADA weakens from $\\rho = -1.0$ to $\\rho = -0.7$ ($p = .233$), consistent with GDN contributing to the convergence signal. MMLU reverses from $\\rho = -0.7$ to $\\rho = +0.6$, confirming that the moderate negative correlation on MMLU depends on GDN's inclusion and should not be interpreted as evidence of convergence.\n\n\\begin{table}[ht]\n\\centering\n\\small\n\\caption{Effect of GDN exclusion on Spearman $\\rho$ (attention ratio vs.\\ cross-architecture $\\sigma$) at 1.3B scale. Only benchmarks with $|\\Delta\\rho| \\geq 0.3$ shown.}\n\\label{tab:gdn_sensitivity}\n\\begin{tabular}{lrrrr}\n\\toprule\nBenchmark & $\\rho_{\\text{all}}$ & $\\rho_{\\text{no-GDN}}$ & $\\Delta\\rho$ & $p_{\\text{no-GDN}}$ \\\\\n\\midrule\nLAMBADA & $-1.0$ & $-0.7$ & $+0.3$ & .233 \\\\\nMMLU & $-0.7$ & $+0.6$ & $+1.3$ & .350 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{GDN Attention Head Confound}\\label{app:gdn_confound}\n\nIn the \\citet{wang2025hybrid} model zoo, the GDN h3-1 configuration at 1.3B scale uses 16 attention heads per attention layer, while all other hybrid configurations (across GDN, RetNet, and HGRN2) use 32 attention heads. This is a design choice in the original model zoo, not an error. The reduced head count changes the per-head dimension and may affect the attention capacity of GDN h3-1 relative to other configurations.\n\nThis confound is relevant because the convergence analysis measures cross-architecture $\\sigma$ at each attention ratio. At the h3-1 ratio (25\\% attention), GDN's attention layers have a different internal structure than those of RetNet and HGRN2, which could contribute to variance reduction (or inflation) for reasons unrelated to the recurrent--attention interaction under study.\n\nThe sensitivity analysis in Appendix~\\ref{app:sensitivity} shows that removing GDN weakens the LAMBADA convergence correlation from $\\rho = -1.0$ to $\\rho = -0.7$. This weakening is partially attributable to the reduced sample size ($n = 2$ architectures) and partially to the confound itself. We cannot separate these two effects with the available data.\n\n\\section{Attention Weight Analysis}\\label{app:attention_patterns}\n\nWe extract attention weight matrices from the 1.3B h3-1 models of all three architectures using forward hooks on each attention layer. While \\citet{ali2025hidden} show that SSM layers learn implicit attention patterns, our analysis focuses on the explicit attention layers interleaved within the hybrid architecture. For each layer, we compute the mean attention distribution across all 5{,}153 LAMBADA examples and measure cross-architecture similarity via cosine similarity.\n\n\\subsection{Cross-Architecture Cosine Similarity}\n\nTable~\\ref{tab:attn_cosine} reports cosine similarity between mean attention distributions at selected layers and averaged across all layers.\n\n\\begin{table}[ht]\n\\centering\n\\caption{Cosine similarity between mean attention weight distributions of architecture pairs at selected layers (1.3B h3-1 models on LAMBADA).}\n\\label{tab:attn_cosine}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lrrr}\n\\toprule\nLayer & GDN--RetNet & GDN--HGRN2 & HGRN2--RetNet \\\\\n\\midrule\nL2 (early) & 0.995 & 0.244 & 0.196 \\\\\nL20 (deep) & 0.986 & 0.942 & 0.943 \\\\\n\\midrule\nMean (all layers) & 0.905 & 0.766 & 0.698 \\\\\n\\bottomrule\n\\end{tabular}%\n}\n\\end{table}\n\nAt layer 2, GDN and RetNet produce nearly identical attention distributions (cosine 0.995), while HGRN2 diverges from both (cosine $< 0.25$). By layer 20, all three architectures converge to similar attention patterns (cosine $> 0.94$). The layer-wise trajectory suggests that early-layer attention patterns are shaped by the preceding recurrent layers (which differ across architectures), while deeper layers converge regardless of the recurrent substrate.\n\n\\subsection{Helped vs.\\ Hurt Attention Entropy}\n\nTo test whether the attention mechanism itself differs between helped and hurt examples, we compute the Shannon entropy of the attention distribution for each example at each attention layer and compare the mean entropy of helped examples against hurt examples within each architecture.\n\n\\begin{table}[ht]\n\\centering\n\\caption{Mean attention entropy difference (helped $-$ hurt) averaged across attention layers (1.3B h3-1 models on LAMBADA). Values near zero indicate that the attention mechanism does not discriminate between helped and hurt examples.}\n\\label{tab:attn_entropy}\n\\begin{tabular}{lr}\n\\toprule\nArchitecture & $\\Delta H$ (helped $-$ hurt) \\\\\n\\midrule\nGDN & $-0.0009$ \\\\\nRetNet & $+0.0179$ \\\\\nHGRN2 & $+0.0020$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nGDN and HGRN2 show negligible entropy differences ($|\\Delta H| \\leq 0.002$). RetNet's $\\Delta H = +0.018$ is small in absolute terms but slightly larger; helped examples receive marginally more diffuse attention in RetNet. Across all three architectures, the differences are insufficient to explain the per-example divergence, consistent with per-example effects not being explained by attention weight patterns and likely originating in the recurrent layers.\n\n\\subsection{Last-5 Attention Mass}\n\nWe also measure the fraction of attention mass allocated to the last five tokens, which captures whether the attention mechanism concentrates differently on recent context for helped vs.\\ hurt examples.\n\n\\begin{table}[ht]\n\\centering\n\\caption{Mean attention mass on last-5 tokens for helped and hurt examples, averaged across attention layers (1.3B h3-1 models on LAMBADA).}\n\\label{tab:attn_last5}\n\\begin{tabular}{lrr}\n\\toprule\nArchitecture & Helped & Hurt \\\\\n\\midrule\nGDN & 0.0834 & 0.0831 \\\\\nRetNet & 0.1578 & 0.1591 \\\\\nHGRN2 & 0.0453 & 0.0467 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nNo architecture shows a meaningful difference in last-5 attention mass between helped and hurt examples (Table~\\ref{tab:attn_last5}). This further supports the conclusion that the per-example divergence is not driven by differential attention allocation.\n\n\\section{Cross-Scale Per-Example Comparisons}\\label{app:cross_scale}\n\n\\subsection{Within-Scale Pairwise Jaccard}\n\nTable~\\ref{tab:within_scale_jaccard} reports the within-scale pairwise Jaccard similarity between architectures' helped and hurt sets at both scales. Mean values are similar across scales (340M: 0.094/0.090; 1.3B: 0.100/0.093), indicating that per-example architecture specificity is consistent across the two scales examined.\n\n\\begin{table}[ht]\n\\centering\n\\small\n\\caption{Within-scale pairwise Jaccard similarity of per-example effects (pure $\\to$ h3-1) on LAMBADA. Each row compares the helped (or hurt) sets of two architectures at the same scale.}\n\\label{tab:within_scale_jaccard}\n\\begin{tabular}{llcc}\n\\toprule\nScale & Pair & $J_{\\text{helped}}$ & $J_{\\text{hurt}}$ \\\\\n\\midrule\n\\multirow{4}{*}{340M} & GDN--RetNet & 0.092 & 0.109 \\\\\n& GDN--HGRN2 & 0.084 & 0.075 \\\\\n& RetNet--HGRN2 & 0.108 & 0.085 \\\\\n& \\textit{Mean} & \\textit{0.094} & \\textit{0.090} \\\\\n\\midrule\n\\multirow{4}{*}{1.3B} & GDN--RetNet & 0.092 & 0.103 \\\\\n& GDN--HGRN2 & 0.100 & 0.088 \\\\\n& RetNet--HGRN2 & 0.108 & 0.087 \\\\\n& \\textit{Mean} & \\textit{0.100} & \\textit{0.093} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Cross-Scale Pairwise Jaccard}\n\nFor each architecture, we compare the helped and hurt sets of the pure $\\to$ h3-1 transition at 340M and 1.3B scale on LAMBADA.\nThe comparison uses the same classification scheme as \\S\\ref{ssec:per_example}: an example is ``helped'' if it is correct only in the hybrid variant and ``hurt'' if correct only in the pure baseline.\nAll pairwise Jaccard values fall below 0.10, indicating that scale variation is associated with per-example predictive multiplicity analogous to the cross-architecture effect reported in \\S\\ref{ssec:per_example}.\n\n\\begin{table}[ht]\n\\centering\n\\caption{Cross-scale pairwise Jaccard similarity of per-example effects (pure $\\to$ h3-1) between 340M and 1.3B on LAMBADA. All values below 0.10.}\n\\label{tab:cross_scale_jaccard}\n\\begin{tabular}{llcc}\n\\toprule\nArchitecture & Scale Pair & $J_{\\text{helped}}$ & $J_{\\text{hurt}}$ \\\\\n\\midrule\nGDN & 340M $\\leftrightarrow$ 1.3B & 0.047 & 0.087 \\\\\nRetNet & 340M $\\leftrightarrow$ 1.3B & 0.059 & 0.073 \\\\\nHGRN2 & 340M $\\leftrightarrow$ 1.3B & 0.089 & 0.055 \\\\\n\\midrule\nMean & & 0.065 & 0.072 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Per-Example Effect Counts}\\label{app:per_example_counts}\n\nTable~\\ref{tab:per_example} reports the full per-example effect counts for each architecture at 1.3B scale.\n\n\\begin{table}[ht]\n\\centering\n\\caption{Per-example effects of attention (pure $\\to$ h3-1) on 5{,}153 LAMBADA examples at 1.3B scale. $\\bar{J}$: mean pairwise Jaccard similarity with other architectures across helped and hurt sets.}\n\\label{tab:per_example}\n\\begin{tabular}{lrrrr}\n\\toprule\nArchitecture & Helped & Hurt & Net & $\\bar{J}$ \\\\\n\\midrule\nGDN & 462 & 615 & $-$153 & .096 \\\\\nRetNet & 426 & 495 & $-$69 & .100 \\\\\nHGRN2 & 548 & 395 & $+$153 & .104 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Normalized Jaccard Effect Size}\\label{app:normalized_es}\n\nTo assess whether low observed Jaccard reflects a floor effect imposed by unequal set sizes, we compute the theoretical upper bound $J_{\\max} = \\min(|A|,|B|) / \\max(|A|,|B|)$ and the normalized effect size $(J_{\\text{obs}} - J_{\\text{null}}) / (J_{\\max} - J_{\\text{null}})$, which measures observed overlap as a fraction of the achievable range above chance. Table~\\ref{tab:normalized_es} reports per-pair results.\n\n\\begin{table}[ht]\n\\centering\n\\small\n\\caption{Normalized Jaccard effect size for each architecture pair (1.3B h3-1 on LAMBADA). $J_{\\max}$: theoretical upper bound given set sizes. Normalized ES: fraction of achievable overlap above chance.}\n\\label{tab:normalized_es}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llcccc}\n\\toprule\nCategory & Pair & $J_{\\text{obs}}$ & $J_{\\max}$ & $J_{\\text{null}}$ & Norm.\\ ES \\\\\n\\midrule\nHelped & GDN--RetNet & .092 & .922 & .045 & .054 \\\\\n & GDN--HGRN2 & .100 & .843 & .051 & .062 \\\\\n & RetNet--HGRN2 & .108 & .777 & .049 & .081 \\\\\n & \\textit{Mean} & \\textit{.100} & \\textit{.848} & \\textit{.048} & \\textit{.066} \\\\\n\\midrule\nHurt & GDN--RetNet & .103 & .805 & .056 & .063 \\\\\n & GDN--HGRN2 & .088 & .642 & .049 & .066 \\\\\n & RetNet--HGRN2 & .087 & .798 & .045 & .056 \\\\\n & \\textit{Mean} & \\textit{.093} & \\textit{.748} & \\textit{.050} & \\textit{.062} \\\\\n\\bottomrule\n\\end{tabular}%\n}\n\\end{table}\n\nAll normalized effect sizes fall below 0.10, confirming that observed overlap reaches only 6--7\\% of the theoretical maximum. The low Jaccard values cannot be attributed to set-size constraints.\n\n\\section{ARC-Easy Per-Example Analysis}\\label{app:arceasy}\n\nTable~\\ref{tab:arceasy_effects} reports per-example effect counts on ARC-Easy ($N = 2{,}376$) at 1.3B scale for each attention ratio. Unlike LAMBADA, ARC-Easy shows no aggregate convergence ($\\rho = -0.20$, $p = .783$). HGRN2 is net positive at all ratios; GDN and RetNet are mixed.\n\n\\begin{table}[ht]\n\\centering\n\\small\n\\caption{Per-example effects on ARC-Easy at 1.3B scale. Net = helped $-$ hurt.}\n\\label{tab:arceasy_effects}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llrrr}\n\\toprule\nArchitecture & Ratio & Helped & Hurt & Net \\\\\n\\midrule\n\\multirow{4}{*}{GDN} & h24-1 & 178 & 185 & $-$7 \\\\\n& h12-1 & 176 & 206 & $-$30 \\\\\n& h6-1 & 170 & 157 & $+$13 \\\\\n& h3-1 & 171 & 180 & $-$9 \\\\\n\\midrule\n\\multirow{4}{*}{RetNet} & h24-1 & 158 & 168 & $-$10 \\\\\n& h12-1 & 163 & 146 & $+$17 \\\\\n& h6-1 & 159 & 147 & $+$12 \\\\\n& h3-1 & 144 & 184 & $-$40 \\\\\n\\midrule\n\\multirow{4}{*}{HGRN2} & h24-1 & 160 & 119 & $+$41 \\\\\n& h12-1 & 159 & 111 & $+$48 \\\\\n& h6-1 & 185 & 118 & $+$67 \\\\\n& h3-1 & 164 & 146 & $+$18 \\\\\n\\bottomrule\n\\end{tabular}%\n}\n\\end{table}\n\nTable~\\ref{tab:arceasy_ambiguity} reports the ambiguity $\\alpha$ \\citep{marx2020predictive} at each attention ratio for all four main benchmarks. Within-benchmark ranges are 0.004 (HellaSwag), 0.011 (PIQA), 0.025 (ARC-Easy), and 0.022 (LAMBADA), all below the 0.03 threshold reported in \\S\\ref{ssec:per_example}.\n\n\\begin{table}[ht]\n\\centering\n\\caption{Ambiguity $\\alpha$ across attention ratios (1.3B scale). 95\\% CI: BCa bootstrap (10{,}000 resamples) at the pure-recurrent configuration.}\n\\label{tab:arceasy_ambiguity}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lcccccc}\n\\toprule\nBenchmark & Pure & h24-1 & h12-1 & h6-1 & h3-1 & 95\\% CI (pure) \\\\\n\\midrule\nPIQA & .143 & .138 & .132 & .143 & .140 & $[.127,\\,.159]$ \\\\\nHellaSwag & .148 & .150 & .148 & .146 & .150 & $[.141,\\,.155]$ \\\\\nARC-Easy & .205 & .226 & .223 & .201 & .210 & $[.189,\\,.221]$ \\\\\nLAMBADA & .307 & .300 & .316 & .294 & .296 & $[.294,\\,.319]$ \\\\\n\\bottomrule\n\\end{tabular}%\n}\n\\end{table}\n\n\\section{Jaccard Permutation Test}\\label{app:jaccard_permutation}\n\nTo assess whether the observed pairwise Jaccard similarities exceed what would be expected under independence, we perform a permutation test. For each architecture pair at 1.3B h3-1, we hold the helped (or hurt) set sizes fixed and randomly assign example indices to each set (10{,}000 permutations, seed 42). Table~\\ref{tab:jaccard_perm} reports the observed $J$, the null baseline $J_{\\text{null}}$ (mean over permutations), and the $z$-score.\n\n\\begin{table}[ht]\n\\centering\n\\caption{Permutation test for pairwise Jaccard similarity (1.3B h3-1 on LAMBADA, 10{,}000 permutations). All observed values significantly exceed the independence baseline.}\n\\label{tab:jaccard_perm}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llcccc}\n\\toprule\nCategory & Pair & $J_{\\text{obs}}$ & $J_{\\text{null}}$ & $z$ & $p$ \\\\\n\\midrule\nHelped & GDN--HGRN2 & .100 & .051 & 7.11 & $<$.0001 \\\\\n & GDN--RetNet & .092 & .045 & 6.75 & $<$.0001 \\\\\n & HGRN2--RetNet & .108 & .049 & 8.61 & $<$.0001 \\\\\n\\midrule\nHurt & GDN--HGRN2 & .088 & .049 & 5.91 & $<$.0001 \\\\\n & GDN--RetNet & .103 & .056 & 6.85 & $<$.0001 \\\\\n & HGRN2--RetNet & .087 & .045 & 6.05 & $<$.0001 \\\\\n\\bottomrule\n\\end{tabular}%\n}\n\\end{table}\n\nAll six comparisons yield $z > 5.9$ ($p < .0001$). The null baseline averages $J_{\\text{null}} \\approx 0.049$; observed values are approximately twice this level. The overlap between architectures' per-example effect sets is therefore structured rather than a product of random set overlap given the set sizes.\n\n\\section{Transformer Entrainment Comparison}\\label{app:transformer_entrainment}\n\nTo test whether attention layers make hybrid models' per-example behavior converge toward a pure Transformer, we compare the correct-example sets of each architecture's pure and h3-1 variants against a 1.3B Transformer baseline (accuracy 48.1\\%) on LAMBADA. Table~\\ref{tab:transformer_jaccard} reports the Jaccard similarity between each model's correct set and the Transformer's correct set.\n\n\\begin{table}[ht]\n\\centering\n\\caption{Jaccard similarity between each model's correct set and the Transformer correct set on LAMBADA (1.3B scale). All three h3-1 hybrids are more similar to the Transformer than their pure counterparts.}\n\\label{tab:transformer_jaccard}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nArchitecture & $J_{\\text{pure,T}}$ & $J_{\\text{h3-1,T}}$ & $\\Delta$ \\\\\n\\midrule\nGDN & 0.645 & 0.649 & $+$0.005 \\\\\nRetNet & 0.679 & 0.694 & $+$0.015 \\\\\nHGRN2 & 0.672 & 0.701 & $+$0.029 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nAll three architectures show positive $\\Delta$: the h3-1 correct set is more similar to the Transformer correct set than the pure correct set is. The effect is strongest for HGRN2 ($+$0.029) and weakest for GDN ($+$0.005). This ordering is consistent with HGRN2 being the only architecture with a positive net per-example effect from attention (Table~\\ref{tab:per_example}). The Transformer itself achieves the lowest accuracy among all models, so the convergence is not explained by hybrid models degrading toward Transformer-level performance; rather, adding attention shifts which specific examples the hybrid gets correct toward the Transformer's pattern.\n\n\\section{Within-Architecture Per-Example Stability}\\label{app:within_arch_stability}\n\nPer-example effect sets exhibit a three-tier Jaccard hierarchy on LAMBADA (1.3B scale). Under independence (permutation baseline), pairwise Jaccard is $J \\approx 0.05$. Cross-architecture comparisons (different architectures at the same attention ratio) yield $J \\approx 0.10$, approximately $2\\times$ baseline. Within-architecture comparisons (same architecture across different attention ratios) yield $J \\approx 0.33$, approximately $7\\times$ baseline and $3\\times$ the cross-architecture level. Architecture identity therefore has approximately three times the influence of attention ratio on per-example effects.\n\nTable~\\ref{tab:within_arch_summary} reports mean within-architecture Jaccard for each architecture. HGRN2 shows the highest helped overlap and lowest hurt overlap, consistent with its monotonically increasing helped count across ratios (479 $\\to$ 548).\n\n\\begin{table}[ht]\n\\centering\n\\caption{Mean within-architecture pairwise Jaccard similarity across attention ratios (1.3B, LAMBADA). Each mean is computed over all six ratio pairs per architecture.}\n\\label{tab:within_arch_summary}\n\\begin{tabular}{lcc}\n\\toprule\nArchitecture & $\\bar{J}_{\\text{helped}}$ & $\\bar{J}_{\\text{hurt}}$ \\\\\n\\midrule\nGDN & 0.338 & 0.319 \\\\\nRetNet & 0.333 & 0.321 \\\\\nHGRN2 & 0.373 & 0.291 \\\\\n\\midrule\n\\textit{Overall mean} & \\textit{0.348} & \\textit{0.310} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:within_arch_pairwise} reports the full pairwise Jaccard matrix. Attention ratios are denoted by their h$k$-1 labels: h24-1 (4\\%), h12-1 (7.7\\%), h6-1 (14.3\\%), h3-1 (25\\%).\n\n\\begin{table}[ht]\n\\centering\n\\small\n\\caption{Within-architecture pairwise Jaccard similarity between helped and hurt sets at different attention ratios (1.3B, LAMBADA). Each cell compares the per-example effect sets of two attention configurations within the same architecture.}\n\\label{tab:within_arch_pairwise}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llcccccc}\n\\toprule\n & & \\multicolumn{6}{c}{Ratio pair} \\\\\n\\cmidrule(lr){3-8}\nArch & Cat & h24--h12 & h24--h6 & h24--h3 & h12--h6 & h12--h3 & h6--h3 \\\\\n\\midrule\n\\multirow{2}{*}{GDN} & Helped & .345 & .335 & .311 & .344 & .341 & .352 \\\\\n & Hurt & .310 & .328 & .320 & .331 & .281 & .345 \\\\\n\\midrule\n\\multirow{2}{*}{RetNet} & Helped & .354 & .314 & .334 & .322 & .330 & .345 \\\\\n & Hurt & .316 & .334 & .307 & .301 & .324 & .343 \\\\\n\\midrule\n\\multirow{2}{*}{HGRN2} & Helped & .359 & .369 & .375 & .368 & .378 & .388 \\\\\n & Hurt & .292 & .289 & .298 & .273 & .309 & .287 \\\\\n\\bottomrule\n\\end{tabular}%\n}\n\\end{table}\n\nAdjacent ratio pairs (e.g., h24-1 vs.\\ h12-1) do not exhibit systematically higher Jaccard than non-adjacent pairs (e.g., h24-1 vs.\\ h3-1). Across all architectures, the mean Jaccard for adjacent pairs is 0.353 (helped) and 0.311 (hurt), compared with 0.343 (helped) and 0.310 (hurt) for non-adjacent pairs. The negligible difference indicates that the mapping from attention ratio to per-example effects is non-smooth: doubling the attention ratio does not produce a proportionally more similar set of affected examples.\n\n\\section{Cross-Benchmark Jaccard Trajectories}\\label{app:cross_bench_jaccard}\n\nTo test whether the Jaccard stability pattern is specific to LAMBADA or a general property, we compute mean pairwise Jaccard trajectories across all four hybrid attention ratios on all four main benchmarks. Table~\\ref{tab:cross_bench_jaccard} reports the results. On every benchmark, Jaccard shows no statistically significant trend with attention ratio (all $\\rho \\leq 0.80$, $p \\geq 0.333$), with values uniformly between 0.08 and 0.11. The stability observed at the first attention level on LAMBADA (\\S\\ref{ssec:decoupling}) thus appears to hold across benchmarks: once any attention is present, each architecture's per-example response remains largely consistent regardless of attention ratio.\n\n\\begin{table}[ht]\n\\centering\n\\small\n\\caption{Mean pairwise Jaccard (mean of helped and hurt sets, 3 architecture pairs) across attention ratios and benchmarks (1.3B scale). $\\rho$: Spearman correlation between attention ratio and $\\bar{J}$. All $p \\geq 0.333$.}\n\\label{tab:cross_bench_jaccard}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}lcccccc@{}}\n\\toprule\nBenchmark & h24-1 & h12-1 & h6-1 & h3-1 & $\\rho$ & $p$ \\\\\n\\midrule\nLAMBADA & .091 & .088 & .096 & .097 & 0.80 & .333 \\\\\nHellaSwag & .084 & .081 & .091 & .086 & 0.60 & .417 \\\\\nPIQA & .089 & .096 & .089 & .095 & 0.00 & 1.00 \\\\\nARC-Easy & .084 & .099 & .091 & .109 & 0.80 & .333 \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\\section{Continuous-Threshold Jaccard Analysis}\\label{app:continuous_jaccard}\n\nThe main text binarizes per-example effects at the correctness boundary. To verify that low cross-architecture Jaccard is not an artifact of this binarization, we compute Jaccard similarity using a continuous confidence threshold $\\tau$: two architectures' effect sets are defined as the examples whose target-token $|\\log p|$ changes by more than $\\tau$ when attention is added. On LAMBADA, mean pairwise Jaccard decreases monotonically from 0.26 ($\\tau = 0.00$, any change) to 0.05 ($\\tau = 0.30$, large changes only). ARC-Easy and PIQA show the same monotonic decrease. The binary threshold ($\\tau = 0$, correctness flip) thus represents the upper end of cross-architecture overlap; restricting to confident transitions further reduces agreement, confirming that low Jaccard is robust to the choice of binarization threshold.\n\n\\section{Target-Token Confidence Margin}\n\\label{app:confidence_margin}\n\nWe analyze whether pure-model confidence on the target token predicts whether attention will help or hurt on a given example.\nWe define confidence as $|\\log p_{\\text{pure}}(y^*)|$, where $y^*$ is the target token: lower values indicate higher probability (near-correct).\nWe initially tested raw perplexity as a predictor of helped/hurt status, but found that within-category controls (C1/C2) are necessary to isolate attention effects from the definitional confound between pure-correct and pure-wrong populations.\n\nTable~\\ref{tab:cm_c1} compares hurt versus stayed-right samples (both pure-correct): hurt samples have significantly lower target-token probability (higher $|\\log p|$), confirming that weakly-correct predictions are vulnerable to attention disruption.\nTable~\\ref{tab:cm_c2} compares helped versus stayed-wrong samples (both pure-wrong): helped samples have higher target-token probability (lower $|\\log p|$), confirming that near-miss errors are rescuable.\nThis pattern is consistent across all three architectures ($|d| = 0.73$--$0.92$, all $p < 10^{-54}$) but does not alter the cross-architecture Jaccard findings---within-architecture predictability coexists with cross-architecture divergence.\n\n\\begin{table}[ht]\n\\centering\n\\caption{Control 1: Pure-correct samples---hurt vs.\\ stayed-right. Higher mean $|\\log p|$ indicates lower target-token probability (less confident correct).}\n\\label{tab:cm_c1}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lrrrrr}\n\\toprule\nArchitecture & $n_{\\text{hurt}}$ & $n_{\\text{stay}}$ & Hurt mean & Stay mean & Cohen's $d$ \\\\\n\\midrule\nGDN (h12-1) & 519 & 2281 & 1.049 & 0.576 & 0.87 \\\\\nRetNet (h3-1) & 497 & 2169 & 1.293 & 0.785 & 0.83 \\\\\nHGRN2 (h3-1) & 392 & 2102 & 1.481 & 0.899 & 0.92 \\\\\n\\bottomrule\n\\end{tabular}\n}\n\\end{table}\n\n\\begin{table}[ht]\n\\centering\n\\caption{Control 2: Pure-wrong samples---helped vs.\\ stayed-wrong. Lower mean $|\\log p|$ indicates higher target-token probability (near-miss error).}\n\\label{tab:cm_c2}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lrrrrr}\n\\toprule\nArchitecture & $n_{\\text{help}}$ & $n_{\\text{stay}}$ & Help mean & Stay mean & Cohen's $d$ \\\\\n\\midrule\nGDN (h12-1) & 480 & 1873 & 2.459 & 4.189 & $-$0.75 \\\\\nRetNet (h3-1) & 420 & 2067 & 2.478 & 4.103 & $-$0.73 \\\\\nHGRN2 (h3-1) & 548 & 2111 & 2.500 & 4.112 & $-$0.77 \\\\\n\\bottomrule\n\\end{tabular}\n}\n\\end{table}\n\n\\subsection{Cross-Benchmark Extension}\\label{app:cm_cross}\n\nThe confidence margin pattern extends beyond LAMBADA to multiple-choice benchmarks, though with smaller effect sizes. Table~\\ref{tab:cm_cross_c2} reports the rescue analysis (helped vs.\\ stayed-wrong) on HellaSwag and ARC-Easy. All nine comparisons (three benchmarks $\\times$ three architectures) are significant, confirming that attention consistently rescues near-miss errors regardless of task type. Effect sizes range from small on HellaSwag ($d = 0.13$--$0.17$) to medium on ARC-Easy ($d = 0.51$--$0.60$), compared to large on LAMBADA ($d = 0.73$--$0.77$); the attenuation on HellaSwag reflects noisier confidence proxies under length-normalized scoring. Table~\\ref{tab:cm_cross_c1} reports the disruption analysis (hurt vs.\\ stayed-right); two of six comparisons are significant (all on ARC-Easy) with small effect sizes ($d = 0.13$--$0.26$), indicating that the disruption signal is weaker on multiple-choice tasks and absent on HellaSwag under \\texttt{acc\\_norm}. The asymmetry between rescue and disruption reflects task structure: near-miss errors are an intrinsic sample property (the model almost produced the correct answer regardless of format), while borderline correctness in multiple-choice settings depends on relative option ranking rather than absolute confidence, reducing the raw log-likelihood margin's predictive power for vulnerability.\n\n\\begin{table}[ht]\n\\centering\n\\caption{Cross-benchmark rescue analysis (Control 2): helped vs.\\ stayed-wrong on HellaSwag and ARC-Easy (1.3B h3-1).}\n\\label{tab:cm_cross_c2}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llrr}\n\\toprule\nBenchmark & Architecture & Cohen's $d$ & $p$ \\\\\n\\midrule\nHellaSwag & GDN & $-$0.166 & $6.1 \\times 10^{-4}$ \\\\\n & RetNet & $-$0.132 & $1.4 \\times 10^{-2}$ \\\\\n & HGRN2 & $-$0.164 & $1.4 \\times 10^{-3}$ \\\\\n\\midrule\nARC-Easy & GDN & $-$0.60 & $1.0 \\times 10^{-13}$ \\\\\n & RetNet & $-$0.51 & $5.3 \\times 10^{-10}$ \\\\\n & HGRN2 & $-$0.53 & $5.4 \\times 10^{-10}$ \\\\\n\\bottomrule\n\\end{tabular}%\n}\n\\end{table}\n\n\\begin{table}[ht]\n\\centering\n\\caption{Cross-benchmark disruption analysis (Control 1): hurt vs.\\ stayed-right on HellaSwag and ARC-Easy (1.3B h3-1).}\n\\label{tab:cm_cross_c1}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llrrl}\n\\toprule\nBenchmark & Architecture & Cohen's $d$ & $p$ & Sig.? \\\\\n\\midrule\nHellaSwag & GDN & 0.009 & .999 & No \\\\\n & RetNet & $-$0.035 & .453 & No \\\\\n & HGRN2 & $-$0.062 & .274 & No \\\\\n\\midrule\nARC-Easy & GDN & 0.26 & $3.2 \\times 10^{-4}$ & Yes \\\\\n & RetNet & 0.22 & $2.8 \\times 10^{-3}$ & Yes \\\\\n & HGRN2 & 0.13 & .145 & No \\\\\n\\bottomrule\n\\end{tabular}%\n}\n\\end{table}\n\n\\subsection{Prediction Framework}\\label{app:prediction_framework}\n\nWe formalize the confidence margin analysis as a binary prediction task: given a pure-model example and its target-token $|\\log p|$, predict whether attention will change the example's correctness. Using the within-category summary statistics (Tables~\\ref{tab:cm_c1},~\\ref{tab:cm_c2}), we derive analytic AUC from Cohen's $d$ via $\\text{AUC} = \\Phi(|d|/\\sqrt{2})$ and compute Gaussian-intersection thresholds (the $|\\log p|$ value at which the two group densities intersect under equal priors).\n\nTable~\\ref{tab:prediction_auc} reports within-architecture prediction performance. All AUCs exceed 0.69, indicating moderate within-architecture predictive discrimination for attention effects. Disruption prediction is consistently stronger than rescue (mean AUC 0.73 vs.\\ 0.70), reflecting the larger effect sizes in Control~1.\n\n\\begin{table}[ht]\n\\centering\n\\small\n\\caption{Within-architecture prediction of attention effects on LAMBADA (1.3B). AUC$_p$: parametric (from Cohen's $d$); AUC$_e$: empirical (non-parametric).}\n\\label{tab:prediction_auc}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}lcccccc@{}}\n\\toprule\nArchitecture & \\multicolumn{3}{c}{Rescue} & \\multicolumn{3}{c}{Disruption} \\\\\n\\cmidrule(lr){2-4} \\cmidrule(lr){5-7}\n & AUC$_p$ & AUC$_e$ & $d$ & AUC$_p$ & AUC$_e$ & $d$ \\\\\n\\midrule\nGDN (h12-1) & .701 & .756 & 0.75 & .732 & .742 & 0.87 \\\\\nRetNet (h3-1) & .696 & .754 & 0.73 & .722 & .735 & 0.83 \\\\\nHGRN2 (h3-1) & .708 & .765 & 0.77 & .743 & .748 & 0.92 \\\\\n\\midrule\nMean & .702 & .758 & --- & .732 & .742 & --- \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\\paragraph{Normality verification.} Shapiro-Wilk tests reject normality for all six architecture--set combinations (all $W < 0.98$, $p < 10^{-6}$), but the practical departure varies by group. Disruption-set $|\\log p|$ values show mild skewness (0.53--0.77, $W \\in [0.955, 0.973]$), closely approximating a normal distribution at the sample sizes involved. Rescue-set values are moderately right-skewed (skewness 1.33--1.41, $W \\in [0.899, 0.920]$), following an approximately log-normal distribution. Because the skew is one-sided, parametric AUC estimates (0.70--0.74 in the main text) are conservative lower bounds; non-parametric empirical AUC from the same data yields 0.73--0.77.\n\nDespite similar within-architecture AUC, the optimal prediction thresholds differ across architectures for disruption but not rescue (Table~\\ref{tab:threshold_gap}). Rescue thresholds cluster tightly (range 0.03 in $|\\log p|$), indicating that the rescuability boundary---the confidence level below which pure-wrong examples are likely to be corrected by attention---is architecture-invariant. Disruption thresholds span a 47\\% relative range (GDN: 0.70, RetNet: 1.00, HGRN2: 1.14), meaning that the same confidence level on a pure-correct example may predict vulnerability in one architecture but safety in another. This asymmetry constitutes a second dimension of multiplicity beyond per-example disagreement: all three architectures agree on which wrong answers are rescuable, but disagree on which correct answers are vulnerable to disruption.\n\n\\begin{table}[ht]\n\\centering\n\\small\n\\caption{Gaussian-intersection prediction thresholds ($|\\log p|$) across architectures. Relative spread: range/mean.}\n\\label{tab:threshold_gap}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}lccccr@{}}\n\\toprule\n & GDN & RetNet & HGRN2 & Range & Rel.\\ spread \\\\\n\\midrule\nRescue & 3.32 & 3.29 & 3.31 & 0.03 & 1.0\\% \\\\\nDisruption & 0.70 & 1.00 & 1.14 & 0.44 & 46.7\\% \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\\section{Calibration Analysis}\\label{app:calibration}\n\nCross-architecture disruption threshold variation (\\S\\ref{ssec:per_example}) could in principle arise from calibration differences rather than genuine differences in per-example processing. We compute expected calibration error (ECE; \\citealt{guo2017calibration}) for each architecture's h3-1 model on LAMBADA using 15 equal-width bins. ECE values are similar: GDN 0.222, RetNet 0.224, HGRN2 0.235. The cross-architecture ECE spread (6\\%, computed as range/mean) is less than half the disruption threshold spread (47\\%; Table~\\ref{tab:threshold_gap}), indicating that calibration differences are insufficient to account for the observed threshold divergence. Rescue thresholds, which show only 1\\% cross-architecture spread, are consistent with near-identical calibration in the low-confidence regime.\n\n\\section{BoolQ Supplementary Analysis}\n\\label{app:boolq}\n\nBoolQ ($N = 3{,}270$; comprehension, binary yes/no classification) shows the highest ambiguity among the benchmarks we analyzed ($\\alpha \\approx 0.45$), but the Jaccard significance pattern is mixed: only 12 of 24 architecture $\\times$ attention-ratio pair combinations yield $p < .01$. In particular, the RetNet--HGRN2 pair produces 0/8 significant Jaccard values, with several normalized effect sizes below zero, suggesting anti-correlated per-example effects for this pair.\n\n\\paragraph{Binary classification baseline.} BoolQ is binary classification (two answer choices), whereas LAMBADA, HellaSwag, and ARC-Easy involve open vocabulary prediction or four-way multiple choice. Under a binary task, the null Jaccard baseline $J_{\\text{null}}$ is higher because chance overlap between helped/hurt sets is larger when there are fewer ways to be wrong. This elevates the significance threshold: observed Jaccard must be substantially higher to exceed the null, which explains why 12/24 pairs fail to reach significance despite $\\bar{J}_h = 0.103$ and $\\bar{J}_u = 0.098$---values comparable to the four main benchmarks.\n\n\\paragraph{Per-example summary.} Table~\\ref{tab:boolq_multiplicity} reports the key metrics. The high $\\alpha$ reflects that BoolQ examples are more sensitive to architectural variation in the presence of attention: approximately half of all examples change correctness status for at least one architecture. However, the mixed Jaccard significance prevents us from confidently concluding that the cross-architecture overlap structure matches the pattern observed on the four main benchmarks.\n\n\\begin{table}[ht]\n\\centering\n\\small\n\\caption{BoolQ predictive multiplicity at 1.3B (h3-1).}\n\\label{tab:boolq_multiplicity}\n\\begin{tabular}{@{}lcccccc@{}}\n\\toprule\n & $N$ & $\\alpha$ & $\\bar{J}_{h}$ & $\\bar{J}_{u}$ & Sig.\\ pairs & $\\rho_\\alpha$ \\\\\n\\midrule\nBoolQ & 3270 & .45 & .103 & .098 & 12/24 & $+0.1$ \\\\\n\\bottomrule\n\\end{tabular}\n\\par\\vspace{1pt}\n{\\footnotesize RetNet--HGRN2: 0/8 significant; multiple normalized ES $< 0$.}\n\\end{table}\n\nThe significant Jaccard overlap concentrates in GDN--RetNet pairs (8/8 significant), while RetNet--HGRN2 shows none (0/8). This pair-specificity does not appear on the four main benchmarks, where all architecture pairs show significant overlap; it may reflect a BoolQ-specific interaction between binary classification structure and particular recurrent architectures rather than a general property of architecture pairs.\n\n\\paragraph{Confidence margin.} Confidence margin analysis on BoolQ shows the rescue pattern (C2) partially holds (2/3 architectures significant, $d = 0.16$--$0.36$) but the disruption pattern (C1) is absent (0/3, $|d| \\leq 0.10$), consistent with compressed log-likelihood ranges in binary classification reducing the predictive power of confidence margins. This extends the gradient observed across LAMBADA, ARC-Easy, and HellaSwag: C1 effect sizes decrease from open-ended prediction ($d \\approx 0.9$, LAMBADA) through ARC-Easy ($d \\approx 0.1$--$0.3$) to HellaSwag ($d \\approx 0$ under \\texttt{acc\\_norm}) and binary classification ($d \\approx 0$, BoolQ). The gradient broadly tracks the coefficient of variation (CV) of the log-likelihood confidence proxy: LAMBADA ($\\text{CV} = 0.75$) $>$ ARC-Easy ($0.54$) $>$ HellaSwag ($0.49$) $>$ BoolQ ($0.22$). BoolQ's high-frequency short completions (``\\,yes''/``\\,no'') yield elevated baseline log-likelihoods (mean $|\\text{loglik}| = 3.04$ vs.\\ $0.84$ for LAMBADA) with similar absolute spread (IQR $\\approx 0.9$), compressing the relative variation and rendering the confidence margin unable to separate borderline-correct from robustly-correct examples.\n\n\\paragraph{Interpretation.} The RetNet--HGRN2 anti-correlation may reflect different error modes specific to binary classification: when one architecture's recurrent state resolves a yes/no ambiguity through attention, the other architecture's resolution may be disrupted by the same attention intervention. This pattern warrants further investigation with additional binary classification benchmarks to determine whether it is BoolQ-specific or characteristic of two-choice tasks more broadly.\n\n\\section{WinoGrande Supplementary Analysis}\n\\label{app:winogrande}\n\nWinoGrande ($N = 1{,}267$; reasoning, two-choice coreference resolution) shows high ambiguity ($\\alpha \\approx 0.41$ at h3-1) but mixed Jaccard significance: 10 of 24 architecture $\\times$ attention-ratio pair combinations yield $p < .01$. Mean pairwise Jaccard ($\\bar{J}_h = 0.110$, $\\bar{J}_u = 0.103$) is comparable to the four main benchmarks, but the elevated null baseline from near-chance accuracy (${\\sim}60\\%$) reduces statistical power to detect above-chance overlap.\n\n\\paragraph{Near-chance accuracy.} WinoGrande accuracy across hybrid configurations ranges from 59\\% to 62\\%, close to the two-choice chance level of 50\\%. At near-chance accuracy, a large fraction of examples are borderline---small perturbations (such as adding attention) can flip predictions in either direction, inflating the helped and hurt sets and consequently $\\alpha$. This structural property, shared with BoolQ (${\\sim}59\\%$ accuracy, $\\alpha \\approx 0.45$), may partially explain the elevated $\\alpha$ rather than task-intrinsic multiplicity. PIQA (73\\% accuracy, $\\alpha = 0.14$) and HellaSwag (60\\% normalized accuracy, $\\alpha = 0.15$) demonstrate that near-chance accuracy is not the sole driver, but we cannot fully exclude it as a contributing factor for WinoGrande and BoolQ.\n\n\\begin{table}[ht]\n\\centering\n\\small\n\\caption{WinoGrande predictive multiplicity at 1.3B (h3-1).}\n\\label{tab:winogrande_multiplicity}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}lcccccc@{}}\n\\toprule\n & $N$ & $\\alpha$ & $\\bar{J}_{h}$ & $\\bar{J}_{u}$ & Sig.\\ pairs & $\\rho_\\alpha$ \\\\\n\\midrule\nWinoGrande & 1267 & .41 & .110 & .103 & 10/24 & $-0.9$ \\\\\n\\bottomrule\n\\end{tabular}}\n\\par\\vspace{1pt}\n{\\footnotesize $\\alpha$ variation across ratios: 0.054 ($> 0.03$ threshold of main benchmarks).}\n\\end{table}\n\n\\section{340M Per-Example Analysis}\\label{app:scale_per_example}\n\n\\subsection{LAMBADA}\n\nAt 340M, LAMBADA per-example multiplicity closely matches the 1.3B pattern: $\\alpha = 0.313$ (vs.\\ 0.307 at 1.3B), with mean pairwise Jaccard $\\bar{J} \\approx 0.089$ (vs.\\ 0.095). Per-example directionality is preserved: HGRN2 shows net positive effects at h3-1 ($+238$ examples), while GDN ($-256$) and RetNet ($-106$) show net negative effects, mirroring the 1.3B profile (HGRN2 $+153$, GDN $-153$, RetNet $-69$).\n\nHowever, aggregate convergence is absent at 340M: $\\rho = -0.50$ ($p = .45$), with non-monotonic $\\sigma$ across attention ratios ($0.025 \\to 0.012 \\to 0.018 \\to 0.011 \\to 0.016$). This contrasts sharply with 1.3B ($\\rho = -1.0$, $p = .017$, monotonic $\\sigma$ decrease). The decoupling between per-example divergence and aggregate convergence thus manifests differently across scales: at 340M, per-example multiplicity is present but aggregate convergence is not, suggesting that convergence requires sufficient model capacity while multiplicity does not.\n\nWithin-benchmark $\\alpha$ variation across attention ratios is also larger at 340M (0.047, from 0.313 at pure to 0.266 at h3-1) than at 1.3B ($< 0.03$; \\S\\ref{ssec:per_example}), suggesting that smaller models are more sensitive to the attention ratio in terms of per-example disagreement patterns.\n\n\\begin{table}[ht]\n\\centering\n\\small\n\\caption{340M vs.\\ 1.3B LAMBADA comparison.}\n\\label{tab:scale_comparison}\n\\begin{tabular}{@{}lcc@{}}\n\\toprule\n & 340M & 1.3B \\\\\n\\midrule\n$\\alpha$ (pure) & .313 & .307 \\\\\n$\\bar{J}$ (h3-1) & .089 & .095 \\\\\n$\\rho_\\sigma$ & $-0.50$ & $-1.0$ \\\\\n$p$ & .45 & .017 \\\\\nGDN net & $-256$ & $-153$ \\\\\nHGRN2 net & $+238$ & $+153$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Cross-Benchmark Scale Comparison}\n\nTable~\\ref{tab:340m_multi_bench} extends the scale comparison to all four main benchmarks. Two patterns emerge. First, $\\alpha$ is systematically higher at 340M across all benchmarks, with the largest gap on ARC-Easy ($+$8.4pp) and the smallest on LAMBADA ($+$0.6pp). Second, pairwise Jaccard remains stable across scales ($\\bar{J}_h = 0.08$--$0.10$ at both scales); three-architecture results are stable across both 340M and 1.3B scales (Jaccard $\\approx$ 0.08--0.10), providing indirect support for consistency across these two scales. This suggests that the qualitative pattern of per-example multiplicity---which architectures affect which examples---is consistent across the two scales examined, even as its magnitude increases at smaller scale. Notably, the $\\alpha$ inflation does not track accuracy loss: HellaSwag has the largest accuracy gap between scales yet the smallest $\\Delta\\alpha$ ($+$1.9pp), while ARC-Easy has a smaller accuracy gap but the largest $\\Delta\\alpha$ ($+$8.4pp), arguing against accuracy as the primary driver of scale-dependent multiplicity.\n\n\\begin{table}[ht]\n\\centering\n\\small\n\\caption{340M vs.\\ 1.3B per-example multiplicity across four benchmarks. $\\alpha$: ambiguity at pure-recurrent configuration. Acc: mean accuracy across three architectures at pure-recurrent. $\\bar{J}_{h}$/$\\bar{J}_{u}$: mean pairwise Jaccard of helped/hurt sets. $\\Delta\\alpha$: 340M $-$ 1.3B.}\n\\label{tab:340m_multi_bench}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lcccccccr}\n\\toprule\n & \\multicolumn{4}{c}{340M} & \\multicolumn{3}{c}{1.3B} & \\\\\n\\cmidrule(lr){2-5} \\cmidrule(lr){6-8}\nBenchmark & Acc & $\\alpha$ & $\\bar{J}_{h}$ & $\\bar{J}_{u}$ & $\\alpha$ & $\\bar{J}_{h}$ & $\\bar{J}_{u}$ & $\\Delta\\alpha$ \\\\\n\\midrule\nPIQA & .663 & .181 & .090 & .085 & .143 & .091 & .094 & $+$.038 \\\\\nHellaSwag$^\\dagger$ & .420 & .167 & .084 & .083 & .148 & .095 & .085 & $+$.019 \\\\\nARC-Easy & .594 & .289 & .098 & .103 & .205 & .092 & .099 & $+$.084 \\\\\nLAMBADA & --- & .313 & .089 & .090 & .307 & .095 & .093 & $+$.006 \\\\\n\\bottomrule\n\\multicolumn{9}{l}{\\footnotesize $^\\dagger$\\texttt{acc\\_norm}. LAMBADA accuracy omitted (evaluated in separate run).}\n\\end{tabular}%\n}\n\\end{table}\n\nConvergence is absent at 340M across all benchmarks (all $|\\rho| \\leq 0.4$, $p \\geq .45$), in contrast to 1.3B where LAMBADA shows monotonic convergence. The absence of convergence at 340M extends beyond LAMBADA to HellaSwag ($\\rho = 0.4$, $p = .52$), PIQA ($\\rho = 0.3$, $p = .68$), and ARC-Easy ($\\rho = -0.1$, $p = .95$).\n\n\\section{Subsample Sensitivity of \\texorpdfstring{$\\alpha$}{α}}\\label{app:subsample_sensitivity}\n\nTo assess the reliability of $\\alpha$ estimation at different sample sizes, we repeatedly subsample each benchmark (1{,}000 bootstrap replicates, seed 42) and compute the 95\\% CI width of $\\alpha$.\n\n\\begin{table}[ht]\n\\centering\n\\small\n\\caption{$\\alpha$ estimation stability: 95\\% CI width by subsample size.}\n\\label{tab:subsample}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}lrrrrr@{}}\n\\toprule\nBenchmark & $n = 100$ & $n = 200$ & $n = 500$ & $n = 1000$ & Full $N$ \\\\\n\\midrule\nPIQA & .130 & .095 & .066 & .045 & .034 \\\\\nHellaSwag & .140 & .100 & .062 & .044 & .013 \\\\\nARC-Easy & .160 & .105 & .072 & .050 & .032 \\\\\nLAMBADA & .180 & .125 & .082 & .057 & .025 \\\\\n\\bottomrule\n\\end{tabular}}\n\\par\\vspace{1pt}\n{\\footnotesize At $n = 100$, CI width (0.13--0.18) spans the entire four-benchmark $\\alpha$ range (0.14--0.30), rendering $\\alpha$ estimation unreliable. This justifies excluding COPA ($n = 100$) from the per-example analysis.}\n\\end{table}\n\n\\section{Complementarity Decomposition}\\label{app:complementarity}\n\nWe decompose the three-architecture vote on each example into four categories: unanimous correct (3/3), majority correct (2/3), minority correct (1/3), and unanimous wrong (0/3). This decomposition explains the structural failure of majority vote despite substantial per-example complementarity.\n\nTable~\\ref{tab:complementarity} reports the decomposition at h3-1 (25\\% attention). Majority vote benefits only from 2/3 examples (where the correct answer holds a majority) but is actively harmed by 1/3 examples (where the correct architecture is outvoted). On LAMBADA, HellaSwag, and ARC-Easy, the MV exploitation ratio---the fraction of complementary examples where MV selects correctly---hovers near 51\\%, indicating a near-even split between MV-exploitable and MV-hostile disagreements. The oracle, by contrast, exploits both categories, explaining the large oracle--MV gap ($+7$--$14$\\,pp).\n\n\\begin{table}[ht]\n\\centering\n\\small\n\\caption{Complementarity decomposition at 1.3B h3-1. Fractions of total examples in each vote category. MV expl.: fraction of complementary examples where majority vote is correct.}\n\\label{tab:complementarity}\n\\begin{tabular}{@{}lccccr@{}}\n\\toprule\nBenchmark & 3/3 & 2/3 & 1/3 & 0/3 & MV expl. \\\\\n\\midrule\nLAMBADA & .361 & .151 & .145 & .343 & 51.1\\% \\\\\nHellaSwag & .519 & .078 & .073 & .331 & 51.6\\% \\\\\nARC-Easy & .603 & .107 & .103 & .187 & 50.9\\% \\\\\nBoolQ & .376 & .257 & .197 & .170 & 56.6\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThis near-50\\% exploitation ratio is structurally invariant across attention ratios: on LAMBADA, the ratio ranges from 51.1\\% to 54.4\\% across all five configurations; on HellaSwag, from 50.3\\% to 51.6\\%. Attention changes neither the amount nor the structure of cross-architecture complementarity.\n\n\\section{Seed-Variation Calibration}\\label{app:seed_calibration}\n\nTo contextualize the $3\\times$ within- vs.\\ cross-architecture Jaccard gap (\\S\\ref{ssec:decoupling}), we compare against within-seed variation using the Pythia 70M \\citep{biderman2023pythia} PolyPythias models \\citep{vanderwal2025polypythias}, which provide 9 individually trained seeds of the same architecture.\n\nOn LAMBADA ($N = 5{,}153$), within-seed mean Jaccard is $\\bar{J}_h = 0.273$ (helped) and $\\bar{J}_u = 0.393$ (hurt), compared to our cross-architecture reference $J \\approx 0.10$. On ARC-Easy ($N = 2{,}376$), within-seed $\\bar{J}_h = 0.312$ and $\\bar{J}_u = 0.354$, versus cross-architecture $J \\approx 0.092$. Within-seed ambiguity is $\\alpha = 0.36$ (LAMBADA) and $\\alpha = 0.49$ (ARC-Easy), compared to cross-architecture $\\alpha = 0.30$ and $0.21$ respectively.\n\nSeeds thus produce comparable or higher amounts of per-example disagreement ($\\alpha$) but on more overlapping examples (higher $J$). Cross-architecture variation is associated with per-example effects on less overlapping examples (lower $J$), consistent with architecture-associated divergence yielding qualitatively different per-example patterns than seed noise. The within-seed Jaccard is 2.7--4.3$\\times$ higher than cross-architecture Jaccard across both benchmarks.\n\nThree caveats qualify this comparison. First, scale mismatch: Pythia 70M is $5\\times$ smaller than our smallest models (340M); attempts to use Pythia 410M failed repeatedly. Second, architecture family: Pythia is a standard Transformer, not a hybrid recurrent architecture, so this is a cross-family reference point rather than a matched control. Third, accuracy regime: Pythia 70M accuracy (LAMBADA 0.17--0.23, ARC-Easy ${\\sim}$0.38) is far below our models (${\\sim}$0.50, ${\\sim}$0.72), and Jaccard is affected by base rates; the 2.7--4.3$\\times$ ratio may differ at accuracy regimes closer to our main experiments. These limitations restrict the comparison to a reference point for seed-variation magnitude rather than definitive evidence for architecture-driven effects.\n\n\\section{Extended Architecture Validation (Five Architectures)}\\label{app:extended_arch}\n\nTo test whether the low cross-architecture Jaccard pattern generalizes beyond the three primary architectures, we extend the analysis to include two additional architectures from the same model zoo: GLA (Gated Linear Attention) and DeltaNet, yielding ten pairwise comparisons. Both are available only at 340M in the model zoo; all results below use the h3-1 (25\\% attention) configuration. This extension validates per-example divergence (not aggregate convergence).\n\n\\begin{center}\n\\small\n\\captionof{table}{Pairwise Jaccard similarity across five architectures (340M, h3-1). All 40 permutation tests yield $p \\leq .002$ ($z = 3.49$--$12.21$).}\n\\label{tab:extended_arch_jaccard}\n\\begin{tabular}{@{}llcc@{}}\n\\toprule\nBenchmark & Pair & $J_h$ & $J_u$ \\\\\n\\midrule\n\\multirow{11}{*}{LAMBADA} & GDN--RetNet & .128 & .121 \\\\\n & GDN--HGRN2 & .123 & .083 \\\\\n & GDN--GLA & .124 & .100 \\\\\n & GDN--DeltaNet & .115 & .100 \\\\\n & RetNet--HGRN2 & .108 & .083 \\\\\n & RetNet--GLA & .123 & .107 \\\\\n & RetNet--DeltaNet & .115 & .096 \\\\\n & HGRN2--GLA & .127 & .086 \\\\\n & HGRN2--DeltaNet & .125 & .090 \\\\\n & GLA--DeltaNet & .134 & .081 \\\\\n & \\textit{Mean} & \\textit{.122} & \\textit{.095} \\\\\n\\midrule\n\\multirow{11}{*}{ARC-Easy} & GDN--RetNet & .089 & .114 \\\\\n & GDN--HGRN2 & .122 & .105 \\\\\n & GDN--GLA & .114 & .106 \\\\\n & GDN--DeltaNet & .084 & .102 \\\\\n & RetNet--HGRN2 & .087 & .115 \\\\\n & RetNet--GLA & .112 & .110 \\\\\n & RetNet--DeltaNet & .138 & .123 \\\\\n & HGRN2--GLA & .098 & .087 \\\\\n & HGRN2--DeltaNet & .109 & .088 \\\\\n & GLA--DeltaNet & .129 & .098 \\\\\n & \\textit{Mean} & \\textit{.108} & \\textit{.105} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{center}\n\n% Figure moved to main text (\\S\\ref{ssec:robustness})\n\nAll pairwise Jaccard values remain $\\leq 0.14$, consistent with the three-architecture results at 1.3B (Table~\\ref{tab:per_example}). The seven new pairs involving GLA and DeltaNet show no systematic difference from the original three pairs (Mann-Whitney $p > .3$ for both helped and hurt), indicating that the low-overlap pattern is not specific to the original architecture triple. A sixth architecture (HGRN; \\citealp{qin2023hierarchically}) is also available in the zoo but excluded from the main analysis: its substantially lower baseline accuracy on LAMBADA (0.263 vs.\\ 0.32--0.38 for the other five) mechanically inflates helped-set sizes and Jaccard values. All 15 six-architecture permutation tests nonetheless remain significant ($z \\geq 2.9$, $p \\leq .006$). The same pattern holds on HellaSwag ($N = 10{,}042$) and PIQA ($N = 1{,}838$): all 20 additional pairwise tests yield $p < .01$ with mean $J_{\\text{helped}} \\leq 0.10$. Full four-benchmark and six-architecture data are included in our code release.\n\n\\section{Code, Data, and Computational Resources}\n\\label{app:code_data}\n\nAll models are from the publicly available model zoo of \\citet{wang2025hybrid}. Analysis code and per-example evaluation outputs are available at \\url{https://anonymous.4open.science/r/entrainment_gated_ft-9444/}.\n\n\\paragraph{Compute.} All experiments are inference-only (no training). Evaluations were conducted on a single NVIDIA RTX PRO 6000 GPU with approximately 5 GPU-hours total across all 30 model configurations and 10 benchmarks. Statistical analyses (permutation tests, bootstrap CIs, Jaccard computations) ran on CPU in under 1 hour.\n\n\\section{Use of AI Assistants}\n\\label{app:ai-assistants}\n\nWe used Claude (Anthropic) as an AI coding and writing assistant\nthroughout this work. Specifically:\n\\begin{itemize}\n    \\item \\textbf{Code:} drafting experiment scripts, data-processing\n    pipelines, and analysis utilities; debugging and refactoring.\n    \\item \\textbf{Writing:} drafting and revising paper sections,\n    polishing prose, and reformatting \\LaTeX{}.\n    \\item \\textbf{Literature:} summarizing related papers to inform\n    the related-work section.\n\\end{itemize}\n",
      "numLines": 801,
      "startLine": 1,
      "totalLines": 801
    }
  },
  "sourceToolAssistantUUID": "1bec8b13-581d-42cb-92b6-a94f2d492b75",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/sessions/paper_audit_content_6bc68a37",
  "sessionId": "6e8d5c3f-7c75-4ff9-a01f-f2df71411ac1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 36 · 2026-05-25T17:13:20.549Z_

```json
{
  "parentUuid": "d397ccb6-d646-41c3-8c5c-578a53568ee1",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "71aad14c-6638-47be-b1b9-422676d103bf",
  "timestamp": "2026-05-25T17:13:20.549Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/sessions/paper_audit_content_6bc68a37",
  "sessionId": "6e8d5c3f-7c75-4ff9-a01f-f2df71411ac1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 37_

```json
{
  "type": "last-prompt",
  "lastPrompt": "项目：entrainment_gated_ft Venue：emnlp-2026 论文目录：/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper  Phase 1 确定性检查结果： 源码检查: passed=False, 2 critical, 1 warning 一致性检查…",
  "leafUuid": "71aad14c-6638-47be-b1b9-422676d103bf",
  "sessionId": "6e8d5c3f-7c75-4ff9-a01f-f2df71411ac1"
}
```

---

### Runtime record

_source line 38_

```json
{
  "type": "ai-title",
  "aiTitle": "EMNLP 2026 paper structure audit and compliance check",
  "sessionId": "6e8d5c3f-7c75-4ff9-a01f-f2df71411ac1"
}
```

---

### Assistant

_source line 39 · 2026-05-25T17:13:23.954Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the .tex files. Let me perform the content structure audit systematically. Let me also do some grep-based checks for specific patterns.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "71aad14c-6638-47be-b1b9-422676d103bf",
  "isSidechain": false,
  "requestId": "req_011CbPfLLcVVKDFsQyyFEvGd",
  "type": "assistant",
  "uuid": "3e945933-f145-4cd4-85c9-6294dfa6f6ec",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/sessions/paper_audit_content_6bc68a37",
  "sessionId": "6e8d5c3f-7c75-4ff9-a01f-f2df71411ac1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VVNzZfRUZABZfKBRo5DdUX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 34782,
      "cache_read_input_tokens": 50289,
      "output_tokens": 922,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 34782,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 922,
          "cache_read_input_tokens": 50289,
          "cache_creation_input_tokens": 34782,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 34782
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

_source line 40 · 2026-05-25T17:13:24.372Z_

现在执行正则扫描，检测 AI 风格标志和其他模式。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3e945933-f145-4cd4-85c9-6294dfa6f6ec",
  "isSidechain": false,
  "requestId": "req_011CbPfLLcVVKDFsQyyFEvGd",
  "type": "assistant",
  "uuid": "a2467e6a-b7d6-43e3-9ab8-484c77e325f3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/sessions/paper_audit_content_6bc68a37",
  "sessionId": "6e8d5c3f-7c75-4ff9-a01f-f2df71411ac1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VVNzZfRUZABZfKBRo5DdUX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 34782,
      "cache_read_input_tokens": 50289,
      "output_tokens": 922,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 34782,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 922,
          "cache_read_input_tokens": 50289,
          "cache_creation_input_tokens": 34782,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 34782
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

_source line 41 · 2026-05-25T17:13:26.617Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01S3SMbaXSVwpWDFNNybNbAD`</summary>

```json
{
  "pattern": "—",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper",
  "output_mode": "content",
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a2467e6a-b7d6-43e3-9ab8-484c77e325f3",
  "isSidechain": false,
  "requestId": "req_011CbPfLLcVVKDFsQyyFEvGd",
  "type": "assistant",
  "uuid": "aef06377-b669-484c-96de-5a19629fcd61",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/sessions/paper_audit_content_6bc68a37",
  "sessionId": "6e8d5c3f-7c75-4ff9-a01f-f2df71411ac1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VVNzZfRUZABZfKBRo5DdUX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 34782,
      "cache_read_input_tokens": 50289,
      "output_tokens": 922,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 34782,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 922,
          "cache_read_input_tokens": 50289,
          "cache_creation_input_tokens": 34782,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 34782
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

_source line 42 · 2026-05-25T17:13:33.829Z_

<details><summary>↩ Tool result · `toolu_01TZn89hCtwWwXJyqb7QEbvy`</summary>

```text
No matches found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "36db40e3-8bd0-424c-a5ea-710e86a761f2",
  "isSidechain": false,
  "promptId": "73d622e8-44a2-4ef1-8f25-89dbf02b8b7b",
  "type": "user",
  "uuid": "23396e86-d548-467e-b424-2eaef63589f8",
  "toolUseResult": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "",
    "numLines": 0
  },
  "sourceToolAssistantUUID": "36db40e3-8bd0-424c-a5ea-710e86a761f2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/sessions/paper_audit_content_6bc68a37",
  "sessionId": "6e8d5c3f-7c75-4ff9-a01f-f2df71411ac1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 43 · 2026-05-25T17:13:26.652Z_

<details><summary>↩ Tool result · `toolu_01S3SMbaXSVwpWDFNNybNbAD`</summary>

```text
No matches found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "aef06377-b669-484c-96de-5a19629fcd61",
  "isSidechain": false,
  "promptId": "73d622e8-44a2-4ef1-8f25-89dbf02b8b7b",
  "type": "user",
  "uuid": "be3489a9-9ace-43c5-a8fc-470df9ce552d",
  "toolUseResult": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "",
    "numLines": 0
  },
  "sourceToolAssistantUUID": "aef06377-b669-484c-96de-5a19629fcd61",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/sessions/paper_audit_content_6bc68a37",
  "sessionId": "6e8d5c3f-7c75-4ff9-a01f-f2df71411ac1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 44 · 2026-05-25T17:13:27.759Z_

<details open><summary>🔧 Tool call — Grep · `toolu_015XVrHkmZ9ik3RkhkKNgFD2`</summary>

```json
{
  "pattern": " – ",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper",
  "output_mode": "content",
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "be3489a9-9ace-43c5-a8fc-470df9ce552d",
  "isSidechain": false,
  "requestId": "req_011CbPfLLcVVKDFsQyyFEvGd",
  "type": "assistant",
  "uuid": "b2080d78-c739-41da-a92b-0e47c3e900c6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/sessions/paper_audit_content_6bc68a37",
  "sessionId": "6e8d5c3f-7c75-4ff9-a01f-f2df71411ac1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VVNzZfRUZABZfKBRo5DdUX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 34782,
      "cache_read_input_tokens": 50289,
      "output_tokens": 922,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 34782,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 922,
          "cache_read_input_tokens": 50289,
          "cache_creation_input_tokens": 34782,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 34782
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

_source line 45 · 2026-05-25T17:13:27.776Z_

<details><summary>↩ Tool result · `toolu_015XVrHkmZ9ik3RkhkKNgFD2`</summary>

```text
No matches found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b2080d78-c739-41da-a92b-0e47c3e900c6",
  "isSidechain": false,
  "promptId": "73d622e8-44a2-4ef1-8f25-89dbf02b8b7b",
  "type": "user",
  "uuid": "3c77999b-e7c0-482f-bb74-74cb272b40dd",
  "toolUseResult": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "",
    "numLines": 0
  },
  "sourceToolAssistantUUID": "b2080d78-c739-41da-a92b-0e47c3e900c6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/sessions/paper_audit_content_6bc68a37",
  "sessionId": "6e8d5c3f-7c75-4ff9-a01f-f2df71411ac1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 46 · 2026-05-25T17:13:28.757Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01BHDLBqdzhXx4GDERMSZ3D2`</summary>

```json
{
  "pattern": "ing,|ing\\.",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper",
  "output_mode": "content",
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3c77999b-e7c0-482f-bb74-74cb272b40dd",
  "isSidechain": false,
  "requestId": "req_011CbPfLLcVVKDFsQyyFEvGd",
  "type": "assistant",
  "uuid": "0000fef2-26f5-4b2d-bb23-c113996d89ff",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/sessions/paper_audit_content_6bc68a37",
  "sessionId": "6e8d5c3f-7c75-4ff9-a01f-f2df71411ac1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VVNzZfRUZABZfKBRo5DdUX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 34782,
      "cache_read_input_tokens": 50289,
      "output_tokens": 922,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 34782,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 922,
          "cache_read_input_tokens": 50289,
          "cache_creation_input_tokens": 34782,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 34782
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

_source line 47 · 2026-05-25T17:13:28.783Z_

<details><summary>↩ Tool result · `toolu_01BHDLBqdzhXx4GDERMSZ3D2`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/author_response.tex:30:\item Introduction, Abstract, and Conclusion rewritten to multiplicity-first framing: per-example multiplicity ($\alpha = 0.14$--$0.30$, Jaccard $\leq 0.10$) now leads; convergence introduced as contrastive secondary finding.
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/author_response.tex:71:\item \textbf{Abstract}: Rewritten to lead with per-example multiplicity ($\alpha = 0.14$--$0.30$, Jaccard $\leq 0.10$); convergence introduced with ``by contrast'' as secondary finding.
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/author_response.tex:105:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/author_response.tex:136:\response{We have added a footnote to Table~1 explaining the discrepancy: ``Bonferroni-adjusted $p = 6 \times 2/120 = 0.100$ (exact); 0.102 arises from rounding raw $p$ to .017 before multiplying.'' The value 0.100 is the exact result; 0.102 is a rounding artifact. We now use 0.100 consistently throughout.}
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/author_response_r7.tex:54:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/author_response_r7.tex:85:\item \textbf{Architecture-specificity}: That architectures with near-identical attention distributions (cosine 0.995) produce divergent per-example effects localizes the source to recurrent layer processing, a finding absent from seed-variation studies.
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/author_response_r7.tex:227:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/author_response_r7.tex:233:\reviewer{PIQA and HellaSwag CIs overlap substantially, so ``spectrum'' overstates the ordering.}
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/main.tex:57:\paragraph{Coverage.} We examine three primary architectures (plus two extended) from one model zoo, four main benchmarks, and two scale points. Generalization to Mamba, RWKV, other hybrid families, and generation tasks remains open; all four per-example benchmarks use discriminative scoring, so multiplicity under open-ended generation is untested. Results at larger scales (e.g., 7B+) may differ, particularly as attention mechanisms become more expressive with increased capacity.
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/arr_checklist.tex:16:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/arr_checklist.tex:20:\textit{Yes. AI writing assistants were used for drafting and editing. All scientific content, claims, and analyses were verified by the authors.}
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/related_work.tex:10:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/experiments.tex:18:\includegraphics[width=0.75\textwidth]{figures/fig3_alpha_routing.pdf}
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/experiments.tex:28:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/method.tex:39:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/method.tex:58:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/appendix.tex:14:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/appendix.tex:472:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/appendix.tex:565:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/appendix.tex:601:WinoGrande ($N = 1{,}267$; reasoning, two-choice coreference resolution) shows high ambiguity ($\alpha \approx 0.41$ at h3-1) but mixed Jaccard significance: 10 of 24 architecture $\times$ attention-ratio pair combinations yield $p < .01$. Mean pairwise Jaccard ($\bar{J}_h = 0.110$, $\bar{J}_u = 0.103$) is comparable to the four main benchmarks, but the elevated null baseline from near-chance accuracy (${\sim}60\%$) reduces statistical power to detect above-chance overlap.
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/appendix.tex:795:    pipelines, and analysis utilities; debugging and refactoring.
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/introduction.tex:24:[Omitted long matching line]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0000fef2-26f5-4b2d-bb23-c113996d89ff",
  "isSidechain": false,
  "promptId": "73d622e8-44a2-4ef1-8f25-89dbf02b8b7b",
  "type": "user",
  "uuid": "7d089d69-9b5a-4f32-8a0c-4d3ff7acecd8",
  "toolUseResult": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/author_response.tex:30:\\item Introduction, Abstract, and Conclusion rewritten to multiplicity-first framing: per-example multiplicity ($\\alpha = 0.14$--$0.30$, Jaccard $\\leq 0.10$) now leads; convergence introduced as contrastive secondary finding.\n/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/author_response.tex:71:\\item \\textbf{Abstract}: Rewritten to lead with per-example multiplicity ($\\alpha = 0.14$--$0.30$, Jaccard $\\leq 0.10$); convergence introduced with ``by contrast'' as secondary finding.\n/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/author_response.tex:105:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/author_response.tex:136:\\response{We have added a footnote to Table~1 explaining the discrepancy: ``Bonferroni-adjusted $p = 6 \\times 2/120 = 0.100$ (exact); 0.102 arises from rounding raw $p$ to .017 before multiplying.'' The value 0.100 is the exact result; 0.102 is a rounding artifact. We now use 0.100 consistently throughout.}\n/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/author_response_r7.tex:54:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/author_response_r7.tex:85:\\item \\textbf{Architecture-specificity}: That architectures with near-identical attention distributions (cosine 0.995) produce divergent per-example effects localizes the source to recurrent layer processing, a finding absent from seed-variation studies.\n/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/author_response_r7.tex:227:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/author_response_r7.tex:233:\\reviewer{PIQA and HellaSwag CIs overlap substantially, so ``spectrum'' overstates the ordering.}\n/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/main.tex:57:\\paragraph{Coverage.} We examine three primary architectures (plus two extended) from one model zoo, four main benchmarks, and two scale points. Generalization to Mamba, RWKV, other hybrid families, and generation tasks remains open; all four per-example benchmarks use discriminative scoring, so multiplicity under open-ended generation is untested. Results at larger scales (e.g., 7B+) may differ, particularly as attention mechanisms become more expressive with increased capacity.\n/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/arr_checklist.tex:16:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/arr_checklist.tex:20:\\textit{Yes. AI writing assistants were used for drafting and editing. All scientific content, claims, and analyses were verified by the authors.}\n/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/related_work.tex:10:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/experiments.tex:18:\\includegraphics[width=0.75\\textwidth]{figures/fig3_alpha_routing.pdf}\n/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/experiments.tex:28:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/method.tex:39:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/method.tex:58:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/appendix.tex:14:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/appendix.tex:472:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/appendix.tex:565:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/appendix.tex:601:WinoGrande ($N = 1{,}267$; reasoning, two-choice coreference resolution) shows high ambiguity ($\\alpha \\approx 0.41$ at h3-1) but mixed Jaccard significance: 10 of 24 architecture $\\times$ attention-ratio pair combinations yield $p < .01$. Mean pairwise Jaccard ($\\bar{J}_h = 0.110$, $\\bar{J}_u = 0.103$) is comparable to the four main benchmarks, but the elevated null baseline from near-chance accuracy (${\\sim}60\\%$) reduces statistical power to detect above-chance overlap.\n/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/appendix.tex:795:    pipelines, and analysis utilities; debugging and refactoring.\n/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/introduction.tex:24:[Omitted long matching line]",
    "numLines": 22
  },
  "sourceToolAssistantUUID": "0000fef2-26f5-4b2d-bb23-c113996d89ff",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/sessions/paper_audit_content_6bc68a37",
  "sessionId": "6e8d5c3f-7c75-4ff9-a01f-f2df71411ac1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 48 · 2026-05-25T17:13:31.111Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01GqwRkHzUPkCScVsfPvSqRH`</summary>

```json
{
  "pattern": "it is worth noting|[Nn]otably|[Ii]mportantly|[Ff]urthermore|[Mm]oreover|[Aa]dditionally",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper",
  "output_mode": "content",
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7d089d69-9b5a-4f32-8a0c-4d3ff7acecd8",
  "isSidechain": false,
  "requestId": "req_011CbPfLLcVVKDFsQyyFEvGd",
  "type": "assistant",
  "uuid": "774e1f43-66ce-4f33-9d00-44191b90cee7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/sessions/paper_audit_content_6bc68a37",
  "sessionId": "6e8d5c3f-7c75-4ff9-a01f-f2df71411ac1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VVNzZfRUZABZfKBRo5DdUX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 34782,
      "cache_read_input_tokens": 50289,
      "output_tokens": 922,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 34782,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 922,
          "cache_read_input_tokens": 50289,
          "cache_creation_input_tokens": 34782,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 34782
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

_source line 49 · 2026-05-25T17:13:31.133Z_

<details><summary>↩ Tool result · `toolu_01GqwRkHzUPkCScVsfPvSqRH`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/appendix.tex:653:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/author_response.tex:60:\response{Added. The checklist covers all sections (A1--A4, B1--B6, C1--C3, D, E) with specific justifications. Notably, C1 reports the computational budget (single NVIDIA RTX PRO 6000, $\sim$5 GPU-hours inference-only) and A3 explicitly notes the scoped claims.}
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/author_response.tex:105:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/author_response.tex:113:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/author_response.tex:128:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/author_response.tex:144:[Omitted long matching line]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "774e1f43-66ce-4f33-9d00-44191b90cee7",
  "isSidechain": false,
  "promptId": "73d622e8-44a2-4ef1-8f25-89dbf02b8b7b",
  "type": "user",
  "uuid": "0c5679e8-ed06-46e0-a657-e36911f31b74",
  "toolUseResult": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/appendix.tex:653:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/author_response.tex:60:\\response{Added. The checklist covers all sections (A1--A4, B1--B6, C1--C3, D, E) with specific justifications. Notably, C1 reports the computational budget (single NVIDIA RTX PRO 6000, $\\sim$5 GPU-hours inference-only) and A3 explicitly notes the scoped claims.}\n/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/author_response.tex:105:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/author_response.tex:113:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/author_response.tex:128:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/author_response.tex:144:[Omitted long matching line]",
    "numLines": 6
  },
  "sourceToolAssistantUUID": "774e1f43-66ce-4f33-9d00-44191b90cee7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/sessions/paper_audit_content_6bc68a37",
  "sessionId": "6e8d5c3f-7c75-4ff9-a01f-f2df71411ac1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 50 · 2026-05-25T17:13:32.586Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01N3RexhhCCXNy7Zceqg7Zdn`</summary>

```json
{
  "pattern": "delve|leverage|utilize|facilitate|myriad|plethora|paradigm shift",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper",
  "output_mode": "content",
  "glob": "*.tex",
  "-i": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0c5679e8-ed06-46e0-a657-e36911f31b74",
  "isSidechain": false,
  "requestId": "req_011CbPfLLcVVKDFsQyyFEvGd",
  "type": "assistant",
  "uuid": "3e51c1d1-5d37-45f1-a87e-eddba28dd807",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/sessions/paper_audit_content_6bc68a37",
  "sessionId": "6e8d5c3f-7c75-4ff9-a01f-f2df71411ac1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VVNzZfRUZABZfKBRo5DdUX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 34782,
      "cache_read_input_tokens": 50289,
      "output_tokens": 922,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 34782,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 922,
          "cache_read_input_tokens": 50289,
          "cache_creation_input_tokens": 34782,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 34782
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

_source line 51 · 2026-05-25T17:13:32.601Z_

<details><summary>↩ Tool result · `toolu_01N3RexhhCCXNy7Zceqg7Zdn`</summary>

```text
No matches found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3e51c1d1-5d37-45f1-a87e-eddba28dd807",
  "isSidechain": false,
  "promptId": "73d622e8-44a2-4ef1-8f25-89dbf02b8b7b",
  "type": "user",
  "uuid": "4ae04140-6a25-440d-891c-23b8a9ad0449",
  "toolUseResult": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "",
    "numLines": 0
  },
  "sourceToolAssistantUUID": "3e51c1d1-5d37-45f1-a87e-eddba28dd807",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/sessions/paper_audit_content_6bc68a37",
  "sessionId": "6e8d5c3f-7c75-4ff9-a01f-f2df71411ac1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 52 · 2026-05-25T17:13:33.806Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01TZn89hCtwWwXJyqb7QEbvy`</summary>

```json
{
  "pattern": "TODO|FIXME|PLACEHOLDER|TBD|XX\\.XX|\\[If ",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper",
  "output_mode": "content",
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4ae04140-6a25-440d-891c-23b8a9ad0449",
  "isSidechain": false,
  "requestId": "req_011CbPfLLcVVKDFsQyyFEvGd",
  "type": "assistant",
  "uuid": "36db40e3-8bd0-424c-a5ea-710e86a761f2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/sessions/paper_audit_content_6bc68a37",
  "sessionId": "6e8d5c3f-7c75-4ff9-a01f-f2df71411ac1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VVNzZfRUZABZfKBRo5DdUX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 34782,
      "cache_read_input_tokens": 50289,
      "output_tokens": 922,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 34782,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 922,
          "cache_read_input_tokens": 50289,
          "cache_creation_input_tokens": 34782,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 34782
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

_source line 53 · 2026-05-25T17:13:37.873Z_

<details><summary>Logged reasoning block</summary>

```text
Good. Let me also check for:
1. Abstract word count (must be ≤ 200 words per EMNLP 2026 rule)
2. Limitations section - check if there's more than one
3. En-dash usage in non-range context
4. Check for "significantly" without statistical backing

Let me also count the abstract words and check a few more things.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "23396e86-d548-467e-b424-2eaef63589f8",
  "isSidechain": false,
  "requestId": "req_011CbPfMKdET5zTcEBDHoXSC",
  "type": "assistant",
  "uuid": "4e26246a-140f-4803-9d64-7377c9c457e3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/sessions/paper_audit_content_6bc68a37",
  "sessionId": "6e8d5c3f-7c75-4ff9-a01f-f2df71411ac1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0129homFozCDyBbYDm1dGZSQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3188,
      "cache_read_input_tokens": 85071,
      "output_tokens": 869,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3188,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 869,
          "cache_read_input_tokens": 85071,
          "cache_creation_input_tokens": 3188,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3188
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

_source line 54 · 2026-05-25T17:13:38.380Z_

检查 abstract 字数和其他关键项。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4e26246a-140f-4803-9d64-7377c9c457e3",
  "isSidechain": false,
  "requestId": "req_011CbPfMKdET5zTcEBDHoXSC",
  "type": "assistant",
  "uuid": "af2306b1-cfd2-4ad1-b8c0-7c0076b662df",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/sessions/paper_audit_content_6bc68a37",
  "sessionId": "6e8d5c3f-7c75-4ff9-a01f-f2df71411ac1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0129homFozCDyBbYDm1dGZSQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3188,
      "cache_read_input_tokens": 85071,
      "output_tokens": 869,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3188,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 869,
          "cache_read_input_tokens": 85071,
          "cache_creation_input_tokens": 3188,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3188
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

_source line 55 · 2026-05-25T17:13:41.225Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01HE4gq7RZWejJ2R1A783FGq`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper && sed -n '/\\\\begin{abstract}/,/\\\\end{abstract}/p' main.tex | sed 's/\\\\[a-zA-Z]*{[^}]*}//g; s/\\\\[a-zA-Z]*//g; s/{[^}]*}//g; s/[{}]//g; s/~/ /g; s/\\\\//g' | tr -s ' \\n' ' ' | wc -w",
  "description": "Count abstract word count"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "af2306b1-cfd2-4ad1-b8c0-7c0076b662df",
  "isSidechain": false,
  "requestId": "req_011CbPfMKdET5zTcEBDHoXSC",
  "type": "assistant",
  "uuid": "d299c69a-b9c7-4df1-8a41-7d64ddd9dc53",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/sessions/paper_audit_content_6bc68a37",
  "sessionId": "6e8d5c3f-7c75-4ff9-a01f-f2df71411ac1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0129homFozCDyBbYDm1dGZSQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3188,
      "cache_read_input_tokens": 85071,
      "output_tokens": 869,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3188,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 869,
          "cache_read_input_tokens": 85071,
          "cache_creation_input_tokens": 3188,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3188
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

_source line 56 · 2026-05-25T17:13:45.319Z_

<details><summary>↩ Tool result · `toolu_01JeTpJpNxJ4kxMoenQXH4kf`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/related_work.tex:7:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/related_work.tex:10:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/experiments.tex:7:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/experiments.tex:12:\caption{Jaccard hierarchy on LAMBADA (1.3B). Cross-architecture overlap ($\bar{J} \approx 0.09$) is $2\times$ the independence baseline but only one-third of within-architecture overlap ($\bar{J} \approx 0.33$). Pythia 70M within-seed Jaccard (different scale) falls at a comparable level. Error bars show the helped--hurt range.}
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/experiments.tex:23:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/experiments.tex:26:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/experiments.tex:30:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/experiments.tex:78:\quad\emph{(excl.\ GDN)} & & $-0.7$ & .233 & --- & --- & --- \\
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/experiments.tex:104:Each architecture's per-example response is largely idiosyncratic: observed $\bar{J}$ reaches only 6--7\% of the achievable range above chance ($J_{\max} \approx 0.78$--$0.92$), ruling out ceiling constraints (\S\ref{ssec:per_example}). This pattern generalizes beyond LAMBADA (Figure~\ref{fig:decoupling}c): on all four main benchmarks, mean pairwise Jaccard shows no significant trend with attention ratio (all $\rho \leq 0.80$, $p \geq 0.333$; Appendix~\ref{app:cross_bench_jaccard}).
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/experiments.tex:106:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/experiments.tex:110:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/experiments.tex:114:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/conclusion.tex:5:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/conclusion.tex:6:At the 340M--1.3B scales studied here, aggregate equivalence does not guarantee behavioral equivalence. Low cross-architecture Jaccard creates complementarity ($+7$--$14$\,pp oracle gain), though routing exploitation remains task-dependent ($+5.3$\,pp on LAMBADA; $-0.6$\,pp on PIQA).
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/method.tex:39:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/method.tex:58:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/appendix.tex:30:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/appendix.tex:71:This confound is relevant because the convergence analysis measures cross-architecture $\sigma$ at each attention ratio. At the h3-1 ratio (25\% attention), GDN's attention layers have a different internal structure than those of RetNet and HGRN2, which could contribute to variance reduction (or inflation) for reasons unrelated to the recurrent--attention interaction under study.
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/appendix.tex:90:Layer & GDN--RetNet & GDN--HGRN2 & HGRN2--RetNet \\
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/appendix.tex:160:\multirow{4}{*}{340M} & GDN--RetNet & 0.092 & 0.109 \\
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/appendix.tex:161:& GDN--HGRN2 & 0.084 & 0.075 \\
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/appendix.tex:162:& RetNet--HGRN2 & 0.108 & 0.085 \\
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/appendix.tex:165:\multirow{4}{*}{1.3B} & GDN--RetNet & 0.092 & 0.103 \\
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/appendix.tex:166:& GDN--HGRN2 & 0.100 & 0.088 \\
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/appendix.tex:167:& RetNet--HGRN2 & 0.108 & 0.087 \\
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/appendix.tex:229:Helped & GDN--RetNet & .092 & .922 & .045 & .054 \\
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/appendix.tex:230: & GDN--HGRN2 & .100 & .843 & .051 & .062 \\
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/appendix.tex:231: & RetNet--HGRN2 & .108 & .777 & .049 & .081 \\
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/appendix.tex:234:Hurt & GDN--RetNet & .103 & .805 & .056 & .063 \\
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/appendix.tex:235: & GDN--HGRN2 & .088 & .642 & .049 & .066 \\
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/appendix.tex:236: & RetNet--HGRN2 & .087 & .798 & .045 & .056 \\
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/appendix.tex:243:All normalized effect sizes fall below 0.10, confirming that observed overlap reaches only 6--7\% of the theoretical maximum. The low Jaccard values cannot be attributed to set-size constraints.
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/appendix.tex:311:Helped & GDN--HGRN2 & .100 & .051 & 7.11 & $<$.0001 \\
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/appendix.tex:312: & GDN--RetNet & .092 & .045 & 6.75 & $<$.0001 \\
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/appendix.tex:313: & HGRN2--RetNet & .108 & .049 & 8.61 & $<$.0001 \\
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/appendix.tex:315:Hurt & GDN--HGRN2 & .088 & .049 & 5.91 & $<$.0001 \\
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/appendix.tex:316: & GDN--RetNet & .103 & .056 & 6.85 & $<$.0001 \\
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/appendix.tex:317: & HGRN2--RetNet & .087 & .045 & 6.05 & $<$.0001 \\
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/appendix.tex:382:Arch & Cat & h24--h12 & h24--h6 & h24--h3 & h12--h6 & h12--h3 & h6--h3 \\
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/appendix.tex:434:This pattern is consistent across all three architectures ($|d| = 0.73$--$0.92$, all $p < 10^{-54}$) but does not alter the cross-architecture Jaccard findings---within-architecture predictability coexists with cross-architecture divergence.

[Showing results with pagination = limit: 40]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0b249da7-dda8-4fa0-b8f4-59bfeda4fb72",
  "isSidechain": false,
  "promptId": "73d622e8-44a2-4ef1-8f25-89dbf02b8b7b",
  "type": "user",
  "uuid": "9d6225fb-69af-44f8-bbc3-989fc9175ced",
  "toolUseResult": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/related_work.tex:7:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/related_work.tex:10:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/experiments.tex:7:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/experiments.tex:12:\\caption{Jaccard hierarchy on LAMBADA (1.3B). Cross-architecture overlap ($\\bar{J} \\approx 0.09$) is $2\\times$ the independence baseline but only one-third of within-architecture overlap ($\\bar{J} \\approx 0.33$). Pythia 70M within-seed Jaccard (different scale) falls at a comparable level. Error bars show the helped--hurt range.}\n/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/experiments.tex:23:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/experiments.tex:26:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/experiments.tex:30:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/experiments.tex:78:\\quad\\emph{(excl.\\ GDN)} & & $-0.7$ & .233 & --- & --- & --- \\\\\n/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/experiments.tex:104:Each architecture's per-example response is largely idiosyncratic: observed $\\bar{J}$ reaches only 6--7\\% of the achievable range above chance ($J_{\\max} \\approx 0.78$--$0.92$), ruling out ceiling constraints (\\S\\ref{ssec:per_example}). This pattern generalizes beyond LAMBADA (Figure~\\ref{fig:decoupling}c): on all four main benchmarks, mean pairwise Jaccard shows no significant trend with attention ratio (all $\\rho \\leq 0.80$, $p \\geq 0.333$; Appendix~\\ref{app:cross_bench_jaccard}).\n/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/experiments.tex:106:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/experiments.tex:110:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/experiments.tex:114:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/conclusion.tex:5:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/conclusion.tex:6:At the 340M--1.3B scales studied here, aggregate equivalence does not guarantee behavioral equivalence. Low cross-architecture Jaccard creates complementarity ($+7$--$14$\\,pp oracle gain), though routing exploitation remains task-dependent ($+5.3$\\,pp on LAMBADA; $-0.6$\\,pp on PIQA).\n/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/method.tex:39:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/method.tex:58:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/appendix.tex:30:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/appendix.tex:71:This confound is relevant because the convergence analysis measures cross-architecture $\\sigma$ at each attention ratio. At the h3-1 ratio (25\\% attention), GDN's attention layers have a different internal structure than those of RetNet and HGRN2, which could contribute to variance reduction (or inflation) for reasons unrelated to the recurrent--attention interaction under study.\n/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/appendix.tex:90:Layer & GDN--RetNet & GDN--HGRN2 & HGRN2--RetNet \\\\\n/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/appendix.tex:160:\\multirow{4}{*}{340M} & GDN--RetNet & 0.092 & 0.109 \\\\\n/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/appendix.tex:161:& GDN--HGRN2 & 0.084 & 0.075 \\\\\n/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/appendix.tex:162:& RetNet--HGRN2 & 0.108 & 0.085 \\\\\n/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/appendix.tex:165:\\multirow{4}{*}{1.3B} & GDN--RetNet & 0.092 & 0.103 \\\\\n/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/appendix.tex:166:& GDN--HGRN2 & 0.100 & 0.088 \\\\\n/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/appendix.tex:167:& RetNet--HGRN2 & 0.108 & 0.087 \\\\\n/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/appendix.tex:229:Helped & GDN--RetNet & .092 & .922 & .045 & .054 \\\\\n/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/appendix.tex:230: & GDN--HGRN2 & .100 & .843 & .051 & .062 \\\\\n/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/appendix.tex:231: & RetNet--HGRN2 & .108 & .777 & .049 & .081 \\\\\n/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/appendix.tex:234:Hurt & GDN--RetNet & .103 & .805 & .056 & .063 \\\\\n/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/appendix.tex:235: & GDN--HGRN2 & .088 & .642 & .049 & .066 \\\\\n/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/appendix.tex:236: & RetNet--HGRN2 & .087 & .798 & .045 & .056 \\\\\n/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/appendix.tex:243:All normalized effect sizes fall below 0.10, confirming that observed overlap reaches only 6--7\\% of the theoretical maximum. The low Jaccard values cannot be attributed to set-size constraints.\n/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/appendix.tex:311:Helped & GDN--HGRN2 & .100 & .051 & 7.11 & $<$.0001 \\\\\n/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/appendix.tex:312: & GDN--RetNet & .092 & .045 & 6.75 & $<$.0001 \\\\\n/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/appendix.tex:313: & HGRN2--RetNet & .108 & .049 & 8.61 & $<$.0001 \\\\\n/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/appendix.tex:315:Hurt & GDN--HGRN2 & .088 & .049 & 5.91 & $<$.0001 \\\\\n/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/appendix.tex:316: & GDN--RetNet & .103 & .056 & 6.85 & $<$.0001 \\\\\n/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/appendix.tex:317: & HGRN2--RetNet & .087 & .045 & 6.05 & $<$.0001 \\\\\n/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/appendix.tex:382:Arch & Cat & h24--h12 & h24--h6 & h24--h3 & h12--h6 & h12--h3 & h6--h3 \\\\\n/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/appendix.tex:434:This pattern is consistent across all three architectures ($|d| = 0.73$--$0.92$, all $p < 10^{-54}$) but does not alter the cross-architecture Jaccard findings---within-architecture predictability coexists with cross-architecture divergence.",
    "numLines": 40,
    "appliedLimit": 40
  },
  "sourceToolAssistantUUID": "0b249da7-dda8-4fa0-b8f4-59bfeda4fb72",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/sessions/paper_audit_content_6bc68a37",
  "sessionId": "6e8d5c3f-7c75-4ff9-a01f-f2df71411ac1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 57 · 2026-05-25T17:13:41.398Z_

<details><summary>↩ Tool result · `toolu_01HE4gq7RZWejJ2R1A783FGq`</summary>

```text
163
Shell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/sessions/paper_audit_content_6bc68a37
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d299c69a-b9c7-4df1-8a41-7d64ddd9dc53",
  "isSidechain": false,
  "promptId": "73d622e8-44a2-4ef1-8f25-89dbf02b8b7b",
  "type": "user",
  "uuid": "f1412074-3a5d-42ee-9657-b62701ee4054",
  "toolUseResult": {
    "stdout": "163",
    "stderr": "\nShell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/sessions/paper_audit_content_6bc68a37",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "d299c69a-b9c7-4df1-8a41-7d64ddd9dc53",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/sessions/paper_audit_content_6bc68a37",
  "sessionId": "6e8d5c3f-7c75-4ff9-a01f-f2df71411ac1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 58 · 2026-05-25T17:13:42.339Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01E5YPaZxEa47KQkLnWELzNV`</summary>

```json
{
  "pattern": "\\\\section\\*?\\{Limitations\\}|\\\\section\\*?\\{Limitation\\}",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper",
  "output_mode": "content",
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f1412074-3a5d-42ee-9657-b62701ee4054",
  "isSidechain": false,
  "requestId": "req_011CbPfMKdET5zTcEBDHoXSC",
  "type": "assistant",
  "uuid": "daeb5f40-266b-40cb-91a8-fd94681d7112",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/sessions/paper_audit_content_6bc68a37",
  "sessionId": "6e8d5c3f-7c75-4ff9-a01f-f2df71411ac1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0129homFozCDyBbYDm1dGZSQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3188,
      "cache_read_input_tokens": 85071,
      "output_tokens": 869,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3188,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 869,
          "cache_read_input_tokens": 85071,
          "cache_creation_input_tokens": 3188,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3188
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

_source line 59 · 2026-05-25T17:13:42.351Z_

<details><summary>↩ Tool result · `toolu_01E5YPaZxEa47KQkLnWELzNV`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/main.tex:51:\section*{Limitations}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "daeb5f40-266b-40cb-91a8-fd94681d7112",
  "isSidechain": false,
  "promptId": "73d622e8-44a2-4ef1-8f25-89dbf02b8b7b",
  "type": "user",
  "uuid": "2ff6db23-744b-4702-9d80-fa34ef677188",
  "toolUseResult": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/main.tex:51:\\section*{Limitations}",
    "numLines": 1
  },
  "sourceToolAssistantUUID": "daeb5f40-266b-40cb-91a8-fd94681d7112",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/sessions/paper_audit_content_6bc68a37",
  "sessionId": "6e8d5c3f-7c75-4ff9-a01f-f2df71411ac1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 60 · 2026-05-25T17:13:43.283Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01BTYUuNTrZgmfHxEidY9VTN`</summary>

```json
{
  "pattern": "significantly",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections",
  "output_mode": "content",
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2ff6db23-744b-4702-9d80-fa34ef677188",
  "isSidechain": false,
  "requestId": "req_011CbPfMKdET5zTcEBDHoXSC",
  "type": "assistant",
  "uuid": "4a4e2b4e-9268-4b83-aa80-9920a97d3dff",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/sessions/paper_audit_content_6bc68a37",
  "sessionId": "6e8d5c3f-7c75-4ff9-a01f-f2df71411ac1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0129homFozCDyBbYDm1dGZSQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3188,
      "cache_read_input_tokens": 85071,
      "output_tokens": 869,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3188,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 869,
          "cache_read_input_tokens": 85071,
          "cache_creation_input_tokens": 3188,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3188
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

_source line 61 · 2026-05-25T17:13:43.298Z_

<details><summary>↩ Tool result · `toolu_01BTYUuNTrZgmfHxEidY9VTN`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/experiments.tex:23:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/experiments.tex:28:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/appendix.tex:304:\caption{Permutation test for pairwise Jaccard similarity (1.3B h3-1 on LAMBADA, 10{,}000 permutations). All observed values significantly exceed the independence baseline.}
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/appendix.tex:432:Table~\ref{tab:cm_c1} compares hurt versus stayed-right samples (both pure-correct): hurt samples have significantly lower target-token probability (higher $|\log p|$), confirming that weakly-correct predictions are vulnerable to attention disruption.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4a4e2b4e-9268-4b83-aa80-9920a97d3dff",
  "isSidechain": false,
  "promptId": "73d622e8-44a2-4ef1-8f25-89dbf02b8b7b",
  "type": "user",
  "uuid": "ec0379d2-6660-4448-a515-e4a757441cdf",
  "toolUseResult": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/experiments.tex:23:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/experiments.tex:28:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/appendix.tex:304:\\caption{Permutation test for pairwise Jaccard similarity (1.3B h3-1 on LAMBADA, 10{,}000 permutations). All observed values significantly exceed the independence baseline.}\n/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/appendix.tex:432:Table~\\ref{tab:cm_c1} compares hurt versus stayed-right samples (both pure-correct): hurt samples have significantly lower target-token probability (higher $|\\log p|$), confirming that weakly-correct predictions are vulnerable to attention disruption.",
    "numLines": 4
  },
  "sourceToolAssistantUUID": "4a4e2b4e-9268-4b83-aa80-9920a97d3dff",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/sessions/paper_audit_content_6bc68a37",
  "sessionId": "6e8d5c3f-7c75-4ff9-a01f-f2df71411ac1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 62 · 2026-05-25T17:13:44.555Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01Rh8WkWj2AwhoEY7yKEcm1s`</summary>

```json
{
  "pattern": "state-of-the-art|SOTA|sota",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper",
  "output_mode": "content",
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ec0379d2-6660-4448-a515-e4a757441cdf",
  "isSidechain": false,
  "requestId": "req_011CbPfMKdET5zTcEBDHoXSC",
  "type": "assistant",
  "uuid": "9521e97a-633e-464a-98e5-f2d47079d2e3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/sessions/paper_audit_content_6bc68a37",
  "sessionId": "6e8d5c3f-7c75-4ff9-a01f-f2df71411ac1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0129homFozCDyBbYDm1dGZSQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3188,
      "cache_read_input_tokens": 85071,
      "output_tokens": 869,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3188,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 869,
          "cache_read_input_tokens": 85071,
          "cache_creation_input_tokens": 3188,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3188
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

_source line 63 · 2026-05-25T17:13:44.568Z_

<details><summary>↩ Tool result · `toolu_01Rh8WkWj2AwhoEY7yKEcm1s`</summary>

```text
No matches found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9521e97a-633e-464a-98e5-f2d47079d2e3",
  "isSidechain": false,
  "promptId": "73d622e8-44a2-4ef1-8f25-89dbf02b8b7b",
  "type": "user",
  "uuid": "7ea77011-d8af-4c5a-a24a-24e8aa6db1c3",
  "toolUseResult": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "",
    "numLines": 0
  },
  "sourceToolAssistantUUID": "9521e97a-633e-464a-98e5-f2d47079d2e3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/sessions/paper_audit_content_6bc68a37",
  "sessionId": "6e8d5c3f-7c75-4ff9-a01f-f2df71411ac1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 64 · 2026-05-25T17:13:45.308Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01JeTpJpNxJ4kxMoenQXH4kf`</summary>

```json
{
  "pattern": "--",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections",
  "output_mode": "content",
  "glob": "*.tex",
  "head_limit": 40
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7ea77011-d8af-4c5a-a24a-24e8aa6db1c3",
  "isSidechain": false,
  "requestId": "req_011CbPfMKdET5zTcEBDHoXSC",
  "type": "assistant",
  "uuid": "0b249da7-dda8-4fa0-b8f4-59bfeda4fb72",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/sessions/paper_audit_content_6bc68a37",
  "sessionId": "6e8d5c3f-7c75-4ff9-a01f-f2df71411ac1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0129homFozCDyBbYDm1dGZSQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3188,
      "cache_read_input_tokens": 85071,
      "output_tokens": 869,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3188,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 869,
          "cache_read_input_tokens": 85071,
          "cache_creation_input_tokens": 3188,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3188
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

_source line 65 · 2026-05-25T17:13:45.379Z_

```json
{
  "parentUuid": "9d6225fb-69af-44f8-bbc3-989fc9175ced",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "5747fd4d-c007-40ba-a2c9-602bd8b92ccb",
  "timestamp": "2026-05-25T17:13:45.379Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/sessions/paper_audit_content_6bc68a37",
  "sessionId": "6e8d5c3f-7c75-4ff9-a01f-f2df71411ac1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 66_

```json
{
  "type": "last-prompt",
  "lastPrompt": "项目：entrainment_gated_ft Venue：emnlp-2026 论文目录：/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper  Phase 1 确定性检查结果： 源码检查: passed=False, 2 critical, 1 warning 一致性检查…",
  "leafUuid": "5747fd4d-c007-40ba-a2c9-602bd8b92ccb",
  "sessionId": "6e8d5c3f-7c75-4ff9-a01f-f2df71411ac1"
}
```

---

### Runtime record

_source line 67_

```json
{
  "type": "ai-title",
  "aiTitle": "EMNLP 2026 paper structure audit and compliance check",
  "sessionId": "6e8d5c3f-7c75-4ff9-a01f-f2df71411ac1"
}
```

---

### Assistant

_source line 68 · 2026-05-25T17:14:02.128Z_

<details><summary>Logged reasoning block</summary>

```text
Let me also check the abstract word count more carefully, and look at the em-dash pattern within the actual paper sections (not author_response).

The abstract from main.tex is:
"Hybrid linear recurrent architectures that appear interchangeable by aggregate benchmarks can differ on which specific examples they handle correctly. Using a controlled model zoo \citep{wang2025hybrid} (three architectures, five attention ratios, two scales), we decompose per-example effects of adding attention and find structured predictive multiplicity \citep{marx2020predictive}: pairwise overlap of helped and hurt example sets is uniformly low (Jaccard $\approx 0.10$, roughly twice the independence baseline; all $p < .01$ across five architectures (three primary, two validation)). 

The multiplicity pattern shifts based on task type and evaluation format rather than attention ratio, with per-example overlap stabilizing around 4% attention and plateauing thereafter. This suggests minimal attention suffices to determine which examples each architecture handles well. The findings parallel what \citet{yang2026benchmark} observed across frontier LLMs—substantial per-item disagreement despite similar aggregate performance—but our controlled setup isolates architectural differences from training variations. Confidence margins show moderate predictive power for identifying affected examples, and the low cross-architecture overlap indicates significant complementarity, though the practical benefits depend on the specific task.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5747fd4d-c007-40ba-a2c9-602bd8b92ccb",
  "isSidechain": false,
  "requestId": "req_011CbPfNAmxGau6MU5UeP6Xn",
  "type": "assistant",
  "uuid": "d600b870-c0f8-4f7c-a94b-50b47f4ea109",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/sessions/paper_audit_content_6bc68a37",
  "sessionId": "6e8d5c3f-7c75-4ff9-a01f-f2df71411ac1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BajXR7BYxpGJv6zLXpqvLn",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4574,
      "cache_read_input_tokens": 88259,
      "output_tokens": 1001,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4574,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1001,
          "cache_read_input_tokens": 88259,
          "cache_creation_input_tokens": 4574,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4574
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

_source line 69 · 2026-05-25T17:14:05.166Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01Rbab7bqfEo4mL3Th5DY5S7`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper && sed -n '/\\\\begin{abstract}/,/\\\\end{abstract}/p' main.tex | grep -v '\\\\begin{abstract}' | grep -v '\\\\end{abstract}' | sed 's/\\\\citep{[^}]*}/(CITE)/g; s/\\\\citet{[^}]*}/(CITE)/g; s/\\\\citealp{[^}]*}/(CITE)/g; s/\\\\url{[^}]*}/(URL)/g; s/\\\\footnote{[^}]*}//g; s/\\\\approx/≈/g; s/\\\\neq/≠/g; s/\\\\textit{[^}]*}//g; s/\\$[^$]*\\$//g; s/~/ /g; s/\\\\,/ /g' | wc -w",
  "description": "Refined abstract word count"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d600b870-c0f8-4f7c-a94b-50b47f4ea109",
  "isSidechain": false,
  "requestId": "req_011CbPfNAmxGau6MU5UeP6Xn",
  "type": "assistant",
  "uuid": "bc388623-b69f-4793-bf87-68558451f560",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/sessions/paper_audit_content_6bc68a37",
  "sessionId": "6e8d5c3f-7c75-4ff9-a01f-f2df71411ac1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BajXR7BYxpGJv6zLXpqvLn",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4574,
      "cache_read_input_tokens": 88259,
      "output_tokens": 1001,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4574,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1001,
          "cache_read_input_tokens": 88259,
          "cache_creation_input_tokens": 4574,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4574
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

_source line 70 · 2026-05-25T17:14:05.245Z_

<details><summary>↩ Tool result · `toolu_01Rbab7bqfEo4mL3Th5DY5S7`</summary>

```text
159
Shell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/sessions/paper_audit_content_6bc68a37
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bc388623-b69f-4793-bf87-68558451f560",
  "isSidechain": false,
  "promptId": "73d622e8-44a2-4ef1-8f25-89dbf02b8b7b",
  "type": "user",
  "uuid": "2f66c546-cb07-4c6a-9a8a-f838d193607e",
  "toolUseResult": {
    "stdout": "159",
    "stderr": "\nShell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/sessions/paper_audit_content_6bc68a37",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "bc388623-b69f-4793-bf87-68558451f560",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/sessions/paper_audit_content_6bc68a37",
  "sessionId": "6e8d5c3f-7c75-4ff9-a01f-f2df71411ac1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 71 · 2026-05-25T17:14:06.177Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01LbfJ8CjrPTqmxH6PsquQDh`</summary>

```json
{
  "pattern": "---",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections",
  "output_mode": "content",
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2f66c546-cb07-4c6a-9a8a-f838d193607e",
  "isSidechain": false,
  "requestId": "req_011CbPfNAmxGau6MU5UeP6Xn",
  "type": "assistant",
  "uuid": "0f45756a-0243-46e9-81cf-43c13a4defab",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/sessions/paper_audit_content_6bc68a37",
  "sessionId": "6e8d5c3f-7c75-4ff9-a01f-f2df71411ac1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BajXR7BYxpGJv6zLXpqvLn",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4574,
      "cache_read_input_tokens": 88259,
      "output_tokens": 1001,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4574,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1001,
          "cache_read_input_tokens": 88259,
          "cache_creation_input_tokens": 4574,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4574
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

_source line 72 · 2026-05-25T17:14:06.190Z_

<details><summary>↩ Tool result · `toolu_01LbfJ8CjrPTqmxH6PsquQDh`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/related_work.tex:7:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/experiments.tex:78:\quad\emph{(excl.\ GDN)} & & $-0.7$ & .233 & --- & --- & --- \\
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/appendix.tex:30:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/appendix.tex:434:This pattern is consistent across all three architectures ($|d| = 0.73$--$0.92$, all $p < 10^{-54}$) but does not alter the cross-architecture Jaccard findings---within-architecture predictability coexists with cross-architecture divergence.
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/appendix.tex:438:\caption{Control 1: Pure-correct samples---hurt vs.\ stayed-right. Higher mean $|\log p|$ indicates lower target-token probability (less confident correct).}
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/appendix.tex:455:\caption{Control 2: Pure-wrong samples---helped vs.\ stayed-wrong. Lower mean $|\log p|$ indicates higher target-token probability (near-miss error).}
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/appendix.tex:538:Mean & .702 & .758 & --- & .732 & .742 & --- \\
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/appendix.tex:545:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/appendix.tex:572:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/appendix.tex:603:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/appendix.tex:653:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/appendix.tex:670:LAMBADA & --- & .313 & .089 & .090 & .307 & .095 & .093 & $+$.006 \\
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/appendix.tex:707:[Omitted long matching line]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0f45756a-0243-46e9-81cf-43c13a4defab",
  "isSidechain": false,
  "promptId": "73d622e8-44a2-4ef1-8f25-89dbf02b8b7b",
  "type": "user",
  "uuid": "0b26c998-7004-44c1-9d51-38738ab213ea",
  "toolUseResult": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/related_work.tex:7:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/experiments.tex:78:\\quad\\emph{(excl.\\ GDN)} & & $-0.7$ & .233 & --- & --- & --- \\\\\n/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/appendix.tex:30:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/appendix.tex:434:This pattern is consistent across all three architectures ($|d| = 0.73$--$0.92$, all $p < 10^{-54}$) but does not alter the cross-architecture Jaccard findings---within-architecture predictability coexists with cross-architecture divergence.\n/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/appendix.tex:438:\\caption{Control 1: Pure-correct samples---hurt vs.\\ stayed-right. Higher mean $|\\log p|$ indicates lower target-token probability (less confident correct).}\n/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/appendix.tex:455:\\caption{Control 2: Pure-wrong samples---helped vs.\\ stayed-wrong. Lower mean $|\\log p|$ indicates higher target-token probability (near-miss error).}\n/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/appendix.tex:538:Mean & .702 & .758 & --- & .732 & .742 & --- \\\\\n/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/appendix.tex:545:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/appendix.tex:572:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/appendix.tex:603:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/appendix.tex:653:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/appendix.tex:670:LAMBADA & --- & .313 & .089 & .090 & .307 & .095 & .093 & $+$.006 \\\\\n/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/appendix.tex:707:[Omitted long matching line]",
    "numLines": 13
  },
  "sourceToolAssistantUUID": "0f45756a-0243-46e9-81cf-43c13a4defab",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/sessions/paper_audit_content_6bc68a37",
  "sessionId": "6e8d5c3f-7c75-4ff9-a01f-f2df71411ac1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 73 · 2026-05-25T17:14:06.767Z_

<details open><summary>🔧 Tool call — Grep · `toolu_013iHe5hRHCAEnfeUdjXBa7S`</summary>

```json
{
  "pattern": "Notably",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections",
  "output_mode": "content",
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0b26c998-7004-44c1-9d51-38738ab213ea",
  "isSidechain": false,
  "requestId": "req_011CbPfNAmxGau6MU5UeP6Xn",
  "type": "assistant",
  "uuid": "a4d7c807-cda6-46f3-9412-4ac5e0235f00",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/sessions/paper_audit_content_6bc68a37",
  "sessionId": "6e8d5c3f-7c75-4ff9-a01f-f2df71411ac1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BajXR7BYxpGJv6zLXpqvLn",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4574,
      "cache_read_input_tokens": 88259,
      "output_tokens": 1001,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4574,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1001,
          "cache_read_input_tokens": 88259,
          "cache_creation_input_tokens": 4574,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4574
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

_source line 74 · 2026-05-25T17:14:06.780Z_

<details><summary>↩ Tool result · `toolu_013iHe5hRHCAEnfeUdjXBa7S`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/appendix.tex:653:[Omitted long matching line]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a4d7c807-cda6-46f3-9412-4ac5e0235f00",
  "isSidechain": false,
  "promptId": "73d622e8-44a2-4ef1-8f25-89dbf02b8b7b",
  "type": "user",
  "uuid": "3e677564-0ba0-4afc-aded-97c4df2ce59a",
  "toolUseResult": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/appendix.tex:653:[Omitted long matching line]",
    "numLines": 1
  },
  "sourceToolAssistantUUID": "a4d7c807-cda6-46f3-9412-4ac5e0235f00",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/sessions/paper_audit_content_6bc68a37",
  "sessionId": "6e8d5c3f-7c75-4ff9-a01f-f2df71411ac1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 75 · 2026-05-25T17:14:11.868Z_

<details><summary>Logged reasoning block</summary>

```text
Let me now check the `---` (em-dashes in LaTeX, rendered as —) in the main paper sections (not appendix table data). Let me look at the specific lines:

From related_work.tex:7 - this has `---` which is the LaTeX em-dash. Let me read that specific line.
From appendix.tex:434 - `findings---within-architecture` - this is an em-dash usage in text.

Let me look at these specific em-dash uses more carefully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3e677564-0ba0-4afc-aded-97c4df2ce59a",
  "isSidechain": false,
  "requestId": "req_011CbPfPkHrn1ZapmgBPakLq",
  "type": "assistant",
  "uuid": "6fa4fafe-0808-47e3-b9a5-9d7a7d175897",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/sessions/paper_audit_content_6bc68a37",
  "sessionId": "6e8d5c3f-7c75-4ff9-a01f-f2df71411ac1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KouMt7ucTVrBvG3pzcwueh",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2062,
      "cache_read_input_tokens": 92833,
      "output_tokens": 808,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2062,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 808,
          "cache_read_input_tokens": 92833,
          "cache_creation_input_tokens": 2062,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2062
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

_source line 76 · 2026-05-25T17:14:12.849Z_

<details open><summary>🔧 Tool call — Read · `toolu_01UnZ2SBhFVTteUgEhEEhR8z`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/related_work.tex",
  "offset": 6,
  "limit": 2
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6fa4fafe-0808-47e3-b9a5-9d7a7d175897",
  "isSidechain": false,
  "requestId": "req_011CbPfPkHrn1ZapmgBPakLq",
  "type": "assistant",
  "uuid": "2920cbfc-1b39-4375-abd7-159b5848b5d1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/sessions/paper_audit_content_6bc68a37",
  "sessionId": "6e8d5c3f-7c75-4ff9-a01f-f2df71411ac1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KouMt7ucTVrBvG3pzcwueh",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2062,
      "cache_read_input_tokens": 92833,
      "output_tokens": 808,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2062,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 808,
          "cache_read_input_tokens": 92833,
          "cache_creation_input_tokens": 2062,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2062
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

_source line 77 · 2026-05-25T17:14:12.860Z_

<details><summary>↩ Tool result · `toolu_01UnZ2SBhFVTteUgEhEEhR8z`</summary>

```text
6	\paragraph{Linear Recurrent Models.}
7	Our three recurrent backbones represent distinct gating strategies within the linear recurrence family: RetNet \citep{sun2023retnet} uses multi-scale exponential decay, HGRN2 \citep{qin2024hgrn2} applies gated state expansion, and GatedDeltaNet \citep{yang2024gateddeltanet} combines gated updates with delta rules, extending GLA \citep{yang2024gla} and DeltaNet \citep{yang2024deltanet}. These descend from S4 \citep{gu2022s4} and Mamba \citep{gu2024mamba}, which introduced structured state spaces and input-dependent selection, and connect to linear attention \citep{katharopoulos2020transformers} through the state-space--attention duality of Mamba-2. xLSTM \citep{beck2024xlstm} revives the LSTM lineage with exponential gating and matrix memory, offering an alternative approach at scale. \citet{zimerman2025unified} show that modern gated-linear RNNs---including RetNet and HGRN---can all be cast as implicit causal self-attention, providing a unifying perspective on the family. \citet{arora2024based} identify a recall-throughput tradeoff in linear models that motivates hybrid designs.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2920cbfc-1b39-4375-abd7-159b5848b5d1",
  "isSidechain": false,
  "promptId": "73d622e8-44a2-4ef1-8f25-89dbf02b8b7b",
  "type": "user",
  "uuid": "88accaa0-01b3-4170-978f-76d80d0c7c28",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/related_work.tex",
      "content": "\\paragraph{Linear Recurrent Models.}\nOur three recurrent backbones represent distinct gating strategies within the linear recurrence family: RetNet \\citep{sun2023retnet} uses multi-scale exponential decay, HGRN2 \\citep{qin2024hgrn2} applies gated state expansion, and GatedDeltaNet \\citep{yang2024gateddeltanet} combines gated updates with delta rules, extending GLA \\citep{yang2024gla} and DeltaNet \\citep{yang2024deltanet}. These descend from S4 \\citep{gu2022s4} and Mamba \\citep{gu2024mamba}, which introduced structured state spaces and input-dependent selection, and connect to linear attention \\citep{katharopoulos2020transformers} through the state-space--attention duality of Mamba-2. xLSTM \\citep{beck2024xlstm} revives the LSTM lineage with exponential gating and matrix memory, offering an alternative approach at scale. \\citet{zimerman2025unified} show that modern gated-linear RNNs---including RetNet and HGRN---can all be cast as implicit causal self-attention, providing a unifying perspective on the family. \\citet{arora2024based} identify a recall-throughput tradeoff in linear models that motivates hybrid designs.",
      "numLines": 2,
      "startLine": 6,
      "totalLines": 11
    }
  },
  "sourceToolAssistantUUID": "2920cbfc-1b39-4375-abd7-159b5848b5d1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/sessions/paper_audit_content_6bc68a37",
  "sessionId": "6e8d5c3f-7c75-4ff9-a01f-f2df71411ac1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 78 · 2026-05-25T17:14:16.952Z_

<details><summary>↩ Tool result · `toolu_01QQs8UJDmvRBehP1fpan4b3`</summary>

```text
652	
653	Table~\ref{tab:340m_multi_bench} extends the scale comparison to all four main benchmarks. Two patterns emerge. First, $\alpha$ is systematically higher at 340M across all benchmarks, with the largest gap on ARC-Easy ($+$8.4pp) and the smallest on LAMBADA ($+$0.6pp). Second, pairwise Jaccard remains stable across scales ($\bar{J}_h = 0.08$--$0.10$ at both scales); three-architecture results are stable across both 340M and 1.3B scales (Jaccard $\approx$ 0.08--0.10), providing indirect support for consistency across these two scales. This suggests that the qualitative pattern of per-example multiplicity---which architectures affect which examples---is consistent across the two scales examined, even as its magnitude increases at smaller scale. Notably, the $\alpha$ inflation does not track accuracy loss: HellaSwag has the largest accuracy gap between scales yet the smallest $\Delta\alpha$ ($+$1.9pp), while ARC-Easy has a smaller accuracy gap but the largest $\Delta\alpha$ ($+$8.4pp), arguing against accuracy as the primary driver of scale-dependent multiplicity.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fb1371e4-94ec-4b00-8525-aedf49e7ef67",
  "isSidechain": false,
  "promptId": "73d622e8-44a2-4ef1-8f25-89dbf02b8b7b",
  "type": "user",
  "uuid": "e8cadd64-7ae5-47c3-b6f0-71143f13c9fa",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/appendix.tex",
      "content": "\nTable~\\ref{tab:340m_multi_bench} extends the scale comparison to all four main benchmarks. Two patterns emerge. First, $\\alpha$ is systematically higher at 340M across all benchmarks, with the largest gap on ARC-Easy ($+$8.4pp) and the smallest on LAMBADA ($+$0.6pp). Second, pairwise Jaccard remains stable across scales ($\\bar{J}_h = 0.08$--$0.10$ at both scales); three-architecture results are stable across both 340M and 1.3B scales (Jaccard $\\approx$ 0.08--0.10), providing indirect support for consistency across these two scales. This suggests that the qualitative pattern of per-example multiplicity---which architectures affect which examples---is consistent across the two scales examined, even as its magnitude increases at smaller scale. Notably, the $\\alpha$ inflation does not track accuracy loss: HellaSwag has the largest accuracy gap between scales yet the smallest $\\Delta\\alpha$ ($+$1.9pp), while ARC-Easy has a smaller accuracy gap but the largest $\\Delta\\alpha$ ($+$8.4pp), arguing against accuracy as the primary driver of scale-dependent multiplicity.",
      "numLines": 2,
      "startLine": 652,
      "totalLines": 801
    }
  },
  "sourceToolAssistantUUID": "fb1371e4-94ec-4b00-8525-aedf49e7ef67",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/sessions/paper_audit_content_6bc68a37",
  "sessionId": "6e8d5c3f-7c75-4ff9-a01f-f2df71411ac1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 79 · 2026-05-25T17:14:13.808Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Atxqd81FyPuScZXqpovJkh`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/appendix.tex",
  "offset": 433,
  "limit": 2
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "88accaa0-01b3-4170-978f-76d80d0c7c28",
  "isSidechain": false,
  "requestId": "req_011CbPfPkHrn1ZapmgBPakLq",
  "type": "assistant",
  "uuid": "6870825b-0891-4615-98c6-e236f9e15c48",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/sessions/paper_audit_content_6bc68a37",
  "sessionId": "6e8d5c3f-7c75-4ff9-a01f-f2df71411ac1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KouMt7ucTVrBvG3pzcwueh",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2062,
      "cache_read_input_tokens": 92833,
      "output_tokens": 808,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2062,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 808,
          "cache_read_input_tokens": 92833,
          "cache_creation_input_tokens": 2062,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2062
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

_source line 80 · 2026-05-25T17:14:13.813Z_

<details><summary>↩ Tool result · `toolu_01Atxqd81FyPuScZXqpovJkh`</summary>

```text
433	Table~\ref{tab:cm_c2} compares helped versus stayed-wrong samples (both pure-wrong): helped samples have higher target-token probability (lower $|\log p|$), confirming that near-miss errors are rescuable.
434	This pattern is consistent across all three architectures ($|d| = 0.73$--$0.92$, all $p < 10^{-54}$) but does not alter the cross-architecture Jaccard findings---within-architecture predictability coexists with cross-architecture divergence.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6870825b-0891-4615-98c6-e236f9e15c48",
  "isSidechain": false,
  "promptId": "73d622e8-44a2-4ef1-8f25-89dbf02b8b7b",
  "type": "user",
  "uuid": "d52e2bf8-3155-46ce-a28b-edbeeee4534d",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/appendix.tex",
      "content": "Table~\\ref{tab:cm_c2} compares helped versus stayed-wrong samples (both pure-wrong): helped samples have higher target-token probability (lower $|\\log p|$), confirming that near-miss errors are rescuable.\nThis pattern is consistent across all three architectures ($|d| = 0.73$--$0.92$, all $p < 10^{-54}$) but does not alter the cross-architecture Jaccard findings---within-architecture predictability coexists with cross-architecture divergence.",
      "numLines": 2,
      "startLine": 433,
      "totalLines": 801
    }
  },
  "sourceToolAssistantUUID": "6870825b-0891-4615-98c6-e236f9e15c48",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/sessions/paper_audit_content_6bc68a37",
  "sessionId": "6e8d5c3f-7c75-4ff9-a01f-f2df71411ac1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 81 · 2026-05-25T17:14:14.924Z_

<details open><summary>🔧 Tool call — Read · `toolu_01CnnHEsvWCrbEnCPL87XZcn`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/appendix.tex",
  "offset": 437,
  "limit": 2
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d52e2bf8-3155-46ce-a28b-edbeeee4534d",
  "isSidechain": false,
  "requestId": "req_011CbPfPkHrn1ZapmgBPakLq",
  "type": "assistant",
  "uuid": "6a9011a0-1b49-4ad8-8a29-e77c497a51f0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/sessions/paper_audit_content_6bc68a37",
  "sessionId": "6e8d5c3f-7c75-4ff9-a01f-f2df71411ac1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KouMt7ucTVrBvG3pzcwueh",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2062,
      "cache_read_input_tokens": 92833,
      "output_tokens": 808,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2062,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 808,
          "cache_read_input_tokens": 92833,
          "cache_creation_input_tokens": 2062,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2062
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

_source line 82 · 2026-05-25T17:14:14.928Z_

<details><summary>↩ Tool result · `toolu_01CnnHEsvWCrbEnCPL87XZcn`</summary>

```text
437	\centering
438	\caption{Control 1: Pure-correct samples---hurt vs.\ stayed-right. Higher mean $|\log p|$ indicates lower target-token probability (less confident correct).}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6a9011a0-1b49-4ad8-8a29-e77c497a51f0",
  "isSidechain": false,
  "promptId": "73d622e8-44a2-4ef1-8f25-89dbf02b8b7b",
  "type": "user",
  "uuid": "23567cd6-8305-4da6-85c3-5df6127648c4",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/appendix.tex",
      "content": "\\centering\n\\caption{Control 1: Pure-correct samples---hurt vs.\\ stayed-right. Higher mean $|\\log p|$ indicates lower target-token probability (less confident correct).}",
      "numLines": 2,
      "startLine": 437,
      "totalLines": 801
    }
  },
  "sourceToolAssistantUUID": "6a9011a0-1b49-4ad8-8a29-e77c497a51f0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/sessions/paper_audit_content_6bc68a37",
  "sessionId": "6e8d5c3f-7c75-4ff9-a01f-f2df71411ac1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 83 · 2026-05-25T17:14:15.674Z_

<details open><summary>🔧 Tool call — Read · `toolu_01UAM1BKPJYh7m2nNiru8Co6`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/appendix.tex",
  "offset": 454,
  "limit": 2
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "23567cd6-8305-4da6-85c3-5df6127648c4",
  "isSidechain": false,
  "requestId": "req_011CbPfPkHrn1ZapmgBPakLq",
  "type": "assistant",
  "uuid": "f0c19b2d-b738-4764-a71c-156309826da1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/sessions/paper_audit_content_6bc68a37",
  "sessionId": "6e8d5c3f-7c75-4ff9-a01f-f2df71411ac1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KouMt7ucTVrBvG3pzcwueh",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2062,
      "cache_read_input_tokens": 92833,
      "output_tokens": 808,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2062,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 808,
          "cache_read_input_tokens": 92833,
          "cache_creation_input_tokens": 2062,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2062
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

_source line 84 · 2026-05-25T17:14:15.678Z_

<details><summary>↩ Tool result · `toolu_01UAM1BKPJYh7m2nNiru8Co6`</summary>

```text
454	\centering
455	\caption{Control 2: Pure-wrong samples---helped vs.\ stayed-wrong. Lower mean $|\log p|$ indicates higher target-token probability (near-miss error).}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f0c19b2d-b738-4764-a71c-156309826da1",
  "isSidechain": false,
  "promptId": "73d622e8-44a2-4ef1-8f25-89dbf02b8b7b",
  "type": "user",
  "uuid": "0a2d562c-bbc6-49ad-a14f-bea8f1af6177",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/appendix.tex",
      "content": "\\centering\n\\caption{Control 2: Pure-wrong samples---helped vs.\\ stayed-wrong. Lower mean $|\\log p|$ indicates higher target-token probability (near-miss error).}",
      "numLines": 2,
      "startLine": 454,
      "totalLines": 801
    }
  },
  "sourceToolAssistantUUID": "f0c19b2d-b738-4764-a71c-156309826da1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/sessions/paper_audit_content_6bc68a37",
  "sessionId": "6e8d5c3f-7c75-4ff9-a01f-f2df71411ac1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 85 · 2026-05-25T17:14:16.398Z_

<details open><summary>🔧 Tool call — Read · `toolu_01XGat7zRpuGNVTbaymRiBZm`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/appendix.tex",
  "offset": 544,
  "limit": 2
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0a2d562c-bbc6-49ad-a14f-bea8f1af6177",
  "isSidechain": false,
  "requestId": "req_011CbPfPkHrn1ZapmgBPakLq",
  "type": "assistant",
  "uuid": "3702563a-c9f2-4d9f-8e3a-84697b0bb85a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/sessions/paper_audit_content_6bc68a37",
  "sessionId": "6e8d5c3f-7c75-4ff9-a01f-f2df71411ac1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KouMt7ucTVrBvG3pzcwueh",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2062,
      "cache_read_input_tokens": 92833,
      "output_tokens": 808,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2062,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 808,
          "cache_read_input_tokens": 92833,
          "cache_creation_input_tokens": 2062,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2062
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

_source line 86 · 2026-05-25T17:14:16.401Z_

<details><summary>↩ Tool result · `toolu_01XGat7zRpuGNVTbaymRiBZm`</summary>

```text
544	
545	Despite similar within-architecture AUC, the optimal prediction thresholds differ across architectures for disruption but not rescue (Table~\ref{tab:threshold_gap}). Rescue thresholds cluster tightly (range 0.03 in $|\log p|$), indicating that the rescuability boundary---the confidence level below which pure-wrong examples are likely to be corrected by attention---is architecture-invariant. Disruption thresholds span a 47\% relative range (GDN: 0.70, RetNet: 1.00, HGRN2: 1.14), meaning that the same confidence level on a pure-correct example may predict vulnerability in one architecture but safety in another. This asymmetry constitutes a second dimension of multiplicity beyond per-example disagreement: all three architectures agree on which wrong answers are rescuable, but disagree on which correct answers are vulnerable to disruption.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3702563a-c9f2-4d9f-8e3a-84697b0bb85a",
  "isSidechain": false,
  "promptId": "73d622e8-44a2-4ef1-8f25-89dbf02b8b7b",
  "type": "user",
  "uuid": "81d62587-1607-4623-b835-a9adc04bddaa",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/appendix.tex",
      "content": "\nDespite similar within-architecture AUC, the optimal prediction thresholds differ across architectures for disruption but not rescue (Table~\\ref{tab:threshold_gap}). Rescue thresholds cluster tightly (range 0.03 in $|\\log p|$), indicating that the rescuability boundary---the confidence level below which pure-wrong examples are likely to be corrected by attention---is architecture-invariant. Disruption thresholds span a 47\\% relative range (GDN: 0.70, RetNet: 1.00, HGRN2: 1.14), meaning that the same confidence level on a pure-correct example may predict vulnerability in one architecture but safety in another. This asymmetry constitutes a second dimension of multiplicity beyond per-example disagreement: all three architectures agree on which wrong answers are rescuable, but disagree on which correct answers are vulnerable to disruption.",
      "numLines": 2,
      "startLine": 544,
      "totalLines": 801
    }
  },
  "sourceToolAssistantUUID": "3702563a-c9f2-4d9f-8e3a-84697b0bb85a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/sessions/paper_audit_content_6bc68a37",
  "sessionId": "6e8d5c3f-7c75-4ff9-a01f-f2df71411ac1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 87 · 2026-05-25T17:14:16.949Z_

<details open><summary>🔧 Tool call — Read · `toolu_01QQs8UJDmvRBehP1fpan4b3`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/appendix.tex",
  "offset": 652,
  "limit": 2
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "81d62587-1607-4623-b835-a9adc04bddaa",
  "isSidechain": false,
  "requestId": "req_011CbPfPkHrn1ZapmgBPakLq",
  "type": "assistant",
  "uuid": "fb1371e4-94ec-4b00-8525-aedf49e7ef67",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/sessions/paper_audit_content_6bc68a37",
  "sessionId": "6e8d5c3f-7c75-4ff9-a01f-f2df71411ac1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KouMt7ucTVrBvG3pzcwueh",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2062,
      "cache_read_input_tokens": 92833,
      "output_tokens": 808,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2062,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 808,
          "cache_read_input_tokens": 92833,
          "cache_creation_input_tokens": 2062,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2062
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

_source line 88_

```json
{
  "type": "last-prompt",
  "lastPrompt": "项目：entrainment_gated_ft Venue：emnlp-2026 论文目录：/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper  Phase 1 确定性检查结果： 源码检查: passed=False, 2 critical, 1 warning 一致性检查…",
  "leafUuid": "e8cadd64-7ae5-47c3-b6f0-71143f13c9fa",
  "sessionId": "6e8d5c3f-7c75-4ff9-a01f-f2df71411ac1"
}
```

---

### Runtime record

_source line 89_

```json
{
  "type": "ai-title",
  "aiTitle": "EMNLP 2026 paper structure audit and compliance check",
  "sessionId": "6e8d5c3f-7c75-4ff9-a01f-f2df71411ac1"
}
```

---

### Assistant

_source line 90 · 2026-05-25T17:18:05.076Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the information I need. Let me systematically audit across all dimensions.

## 1. 叙事一致性（CRITICAL）

**Abstract 的"问题":**
- Hybrid linear recurrent architectures that appear interchangeable by aggregate benchmarks can differ on which specific examples they handle correctly.

**Intro 的"问题":**
- Same: architectures score similarly in aggregate but diverge at per-example level. The gap between aggregate equivalence and per-example behavioral equivalence.

→ MATCH ✓

**Intro 的"贡献列表" vs Method 实际做了什么:**


The three contributions map cleanly to the results sections: architectural variation creates structured divergence across task types rather than just attention ratios, per-example overlap stabilizes around 4% attention, and confidence margins can predict which examples are affected with AUC scores between 0.70-0.74, where rescue thresholds remain consistent across architectures but disruption thresholds vary by 47%.

→ MATCH ✓

**Method 的"为什么这

样设计" vs Intro 的"gap":**
- Intro gap: Whether predictive multiplicity extends to architectural variation in hybrid recurrent models
- Method: Uses controlled model zoo isolating architecture and attention config

→ MATCH ✓

**Experiments 验证的 vs Intro 声称的贡献:**
- All three contributions are verified in experiments ✓

**Conclusion 总结的 vs Experiments 的结论:**
- Conclusion summarizes: multiplicity varies by task type, stabilizes at 4%, confidence margins predict, routing task-dependent
- All match experiments ✓

→ Overall narrative consistency is strong. No significant drift detected.

Now I'm checking the abstract claim about "roughly twice the independence baseline" for Jaccard ≈ 0.10 against the experimental finding that J_null ≈ 0.05, which would support that 2x relationship.

The abstract's claim about statistical significance across five architectures aligns with what the experiments section reports in §4.3. And the AUC range of 0.70-0.74 for confidence margins predicting affected examples is confirmed in both the main results and appendix.

Looking at the abstract structure, it cleanly addresses four key elements: the problem of hidden per-example divergence masked by aggregate equivalence, the methodological approach using controlled model variation, the empirical findings around structured multiplicity and stabilization patterns, and the broader significance regarding architectural choices.

The introduction follows a logical progression that works well. It opens with the core observation that architectures perform similarly in aggregate but diverge at the example level, then situates this within the context of rapid architectural proliferation. The gap it identifies is that prior work on predictive multiplicity hasn't examined what happens under architectural variation. The paper then presents its controlled experimental approach, highlights the central finding, and outlines the contributions.

The related work section organizes itself thematically across three areas: hybrid recurrent architectures, linear recurrent models, and underspecification with predictive multiplicity, with each paragraph doing the necessary positioning work within its topic.

Now I'm checking that the contributions align with the paper's scope and evidence. The first contribution about task-dependent multiplicity variation is supported by the analysis in section 4.1 with the multiplicity table and figure. The second contribution on the 4% stabilization point comes from section 4.2. The third contribution around confidence margins and threshold behavior is covered in section 4.1 plus the appendix. There are no orphan sections—everything serves the stated contributions. The scope language in the title and abstract matches what the experiments actually cover: five architectures across the hybrid linear recurrent space.

I'm noticing a potential issue with the abstract's claim about statistical significance across all five architectures. The five-architecture validation only happens at 340M scale, while the 1.3B analysis uses three architectures. The abstract doesn't make this scale distinction explicit, though the parenthetical about "three primary, two validation" does hint at the difference. This is clarified in section 4.3 and the appendix, so it's not misleading, just slightly compressed in the abstract.

For the claim strength, I'm verifying that the language avoids overclaiming. The paper doesn't use "significantly outperforms" or "state-of-the-art," which is good. The specific claims like "significantly exceeds the independence baseline" are backed by strong statistical evidence (z > 5.9, p < .0001).

Now checking the "roughly twice" claim about the independence baseline ratio. Looking at the actual data from Table 7, the observed values range from 0.087 to 0.108 while the null values range from 0.045 to 0.056, giving a ratio between 1.6 and 2.4. The phrase "roughly twice" technically covers a wider range than the paper's quality guidelines suggest (1.8x-2.2x), but it's still a reasonable characterization of the data.

I'm also noticing a potential discrepancy with the "~2.5× observed-to-null ratio" claim in the methods section. Computing the actual ratios from Table 7 across all conditions gives a mean around 1.96, not 2.5. This looks like it might be an error that needs closer examination. Looking at the individual ratios from the permutation test data, they range from 1.80 to 2.20, which averages to about 1.96—substantially lower than the claimed 2.5×. This is a significant discrepancy that needs clarification, and I should check whether the text is referencing a different subset of the data or if there's an error in the reported value. The z-scores in that table range from 3.49 to 12.21, but without the null values listed, I can't verify the exact ratio. The ~2.5× figure appears in the methods section as a general claim, yet when I look at the actual data in Table 7—the only table with both observed and null values—the ratio consistently comes out to around 2.0×. This is a significant numerical inconsistency that needs reconciling.

Now looking at the experimental rigor: the paper acknowledges single training runs in the limitations, uses bootstrap confidence intervals as a heuristic with n=3, reports ambiguity with BCa bootstrap 95% CIs in Table 6, and provides routing gains with standard deviations from cross-validation. The error reporting seems adequate overall.

For baselines, this is an analysis paper working with an existing model zoo rather than proposing a new method, so traditional baseline comparisons don't really apply—the comparisons are internal to the zoo. The ablations are thorough, covering GDN exclusion sensitivity, a 5-architecture extension, scale comparisons, and continuous versus binary Jaccard variants.

On reproducibility, they've disclosed the hardware (single NVIDIA RTX PRO 6000), inference time (~5 GPU-hours), that there's no training involved, the evaluation framework version and default prompts, random seed 42, and code availability.

The paper includes the required venue items: a limitations section with four paragraphs addressing single runs, format confounds, coverage, and pre-training scope, plus the ARR checklist. Notation is consistent throughout—α for ambiguity, J for Jaccard, σ for cross-architecture standard deviation, ρ for Spearman correlation, the h_k-1 notation defined and used consistently, and the "helped/hurt/unchanged" terminology properly introduced.

I'm noticing a slight inconsistency in how the Jaccard similarity is characterized: the abstract states "≈ 0.10" while the conclusion uses "≤ 0.10". Both are technically defensible since the mean hovers around 0.10 and most values fall at or below that threshold, but the phrasing differs. The section transitions are mostly implicit—Introduction flows into Related Work without an explicit bridge, Related Work into Method, and Method into Experiments—which is acceptable for this conference format where such transitions are typically handled implicitly.

The subsections within Experiments have good logical flow, particularly the transition from §4.1 to §4.2 which explicitly asks how attention amount affects multiplicity after establishing task-type variation. The paper lacks a separate Discussion section; instead, the Conclusion serves double duty as both summary and brief interpretation, which is fine for ACL papers, though at six lines it's quite terse. The Limitations section spans four paragraphs covering single training runs, format confounds in LAMBADA, and coverage constraints across architectures and benchmarks.

Now I'm checking the Limitations section more carefully—it covers single training runs, the format confound issue, limited coverage across architectures and benchmarks, and the restriction to pre-training with greedy decoding. That's four substantive limitations, which exceeds the typical requirement of three points. The word count comes to roughly 155 words across the four paragraphs, which is reasonable and not excessive.

For the AI-style markers, I found several LaTeX em-dashes (---) scattered throughout the files that function as parenthetical separators. These appear in related_work.tex and multiple locations in appendix.tex, used to set off explanatory phrases. According to the guidelines, all such explanatory em-dashes need to be removed.

The -ing phrases I checked mostly appear in neutral contexts rather than the problematic "demonstrating" pattern. I also spotted "Notably" once in the appendix, which is minor. The paragraph segmentation looks fine—main text sections run 5-8 sentences typically. None of the blacklisted AI words turned up, and there's no internal experiment IDs, server references, or framework-specific leakage. The code is already anonymized and there are no internal process references.

For the EMNLP 2026 requirements, I need to check the abstract next. I can't verify the exact page count for the main text without compiling, but based on the section breakdown—introduction, related work, method, experiments, conclusion, and limitations—it looks like it should land around 7.75 pages, which fits within the 8-page limit. I've spotted a critical numerical discrepancy though: method.tex claims a ~2.5× observed-to-null ratio, but Table 7 shows it's consistently ~2.0×.

There are also some style issues to flag: LaTeX em-dashes in related_work.tex and the appendix that read like AI markers, a minor filler word in the appendix, and an unusual placement of the data availability footnote inside the abstract itself. The conclusion is quite terse and could use more interpretation, and while the limitations section is slightly longer than typical, it's substantive. Let me double-check that ratio discrepancy more carefully.

The 5-architecture analysis at 340M might have different null baselines than the 3-architecture 1.3B data where all z-scores exceed 5.9. The "~2.5×" claim about the observed-to-null ratio doesn't quite match what I'm seeing in the actual data, which looks closer to 2.0. I need to figure out whether there's a computational error or if I'm looking at the wrong dataset. The ratio could be higher at 340M if the null baselines are lower for smaller helped/hurt sets, but without those specific values I can't verify it. The paper only explicitly reports null values for the 1.3B 3-architecture case in Table 7, which shows ~2.0×—and this is a critical inconsistency because the abstract correctly states "roughly twice" while the methods section claims "~2.5×", making the methods section a 25% overstatement of the actual observed data.

Now checking the statistical significance claims: the abstract says "all p < .01 across five architectures" and the appendix confirms all 40 permutation tests yield p ≤ .002, which is consistent. However, the five-architecture validation at 340M is supplementary while the main results use only three architectures at 1.3B, so the abstract somewhat conflates these as a unified finding—this is more of an information-level issue than a critical error.

For the Jaccard similarity, the abstract's "≈ 0.10" holds for the primary three-architecture analysis at 1.3B, but the five-architecture validation shows some values reaching 0.14, which stretches the approximation claim slightly. I'm parsing the abstract's phrasing more carefully—the "Jaccard ≈ 0.10" and "all p < .01 across five architectures" are technically separate claims within the same parenthetical, so it's defensible that the Jaccard value refers to the 3-architecture primary result while the significance extends to five architectures. Still, readers would naturally interpret "Jaccard ≈ 0.10" as applying to the five-architecture context, which understates the actual mean of ~0.12, so this remains a warning-level issue. Let me wrap up my audit findings.

Now I'm checking where "Notably" appears—it's only in the appendix, which is lower priority but still worth noting. I also need to verify the main text's claims about five-architecture validation. The introduction references §4.3 for this validation, and the experiments section states "J ≤ 0.14 across all ten pairwise comparisons and four benchmarks" for the five-architecture case, which is a tighter bound than the abstract's "Jaccard ≈ 0.10."

—though that abstract value seems to refer to the three-architecture result instead. The conclusion doesn't explicitly mention five architectures, just the general finding about divergence at the per-example level. The Limitations section is properly placed in the main text with no duplicate in the appendix, which follows the guidelines. Let me now check how the abstract defines LLMs.

The abstract defines "large language models (LLMs)" and "area under the ROC curve [AUC]" appropriately, and BCa is defined in section 3.5. Looking at the Related Work structure, the first paragraph on hybrid recurrent architectures does list several papers but groups them thematically rather than just enumerating them, and the other two paragraphs on linear recurrent models and underspecification provide good synthesis and positioning of the work.

The scope claim about "across N domains" doesn't appear in the title, but the abstract's mention of "task type or evaluation format" aligns with the four task categories tested in the experiments. I also notice the paper uses en-dashes in compound terms like "architecture--benchmark combinations," which is standard academic LaTeX formatting.

Now I should double-check whether the main results tables include error bars or uncertainty estimates.

Looking at Table 3, it reports α, J_h, J_u, and ρ_α without error bars in the main table, though the footnote mentions BCa bootstrap confidence intervals are in Table 6 in the appendix. For the Jaccard values specifically, no standard deviation is reported in the main results. The figures note that shaded bands represent heuristic indicators based on n=3. The paper is transparent about this—it explicitly states in section 3.5 that bootstrap CIs with n=3 are heuristic, and the primary statistical inference relies on permutation tests (all p < .01 or p < .0001). Table 2 reports σ values directly since these are exact standard deviations across the three architectures, not estimates. Given that this is an analysis paper grounded in permutation-based significance testing rather than confidence intervals, the uncertainty reporting is appropriate.

Now I'm noticing a numerical inconsistency: the abstract claims the observed Jaccard is "roughly twice the independence baseline" (J_obs ≈ 0.10, J_null ≈ 0.05, ratio ≈ 2.0), but the method section states "~2.5× observed-to-null ratio." The data supports the 2.0× claim, so the method section's ~2.5× is an overstatement by about 25%. This is a critical discrepancy because a reviewer checking the numbers would catch it immediately, and it represents an overclaim in the methodology section relative to what the actual data shows.

Now checking the confidence margin predictor AUC values in the abstract against the appendix table. The abstract reports "AUC 0.70--0.74," and while the parametric AUCs (0.696-0.743) fit within this range, the empirical AUCs (0.735-0.765) extend beyond the upper bound. This suggests the abstract's range may be understating the empirical performance.

The appendix clarifies that parametric AUC is being used, which is the more conservative estimate, making the abstract's claim defensible. I'm also verifying consistency across the paper—the contribution statement, conclusion, and experiments section all cite the same "AUC 0.70--0.74" range, and the main text properly references the appendix for details. Everything checks out. I did notice one instance of "Notably" in the appendix as filler language, but since it's isolated to the appendix, it's not a significant issue. I'm ready to compile the full audit report now.

There's a potential overclaim in the method section regarding the permutation test robustness. The paper argues that a ~2.5× observed-to-null ratio (with all z-scores above 5.9) provides substantial protection against anti-conservative bias, but if the actual ratio is closer to ~2.0×, the argument still holds—just with less margin. This weakens the robustness claim somewhat. Also, the paper structure goes directly from Experiments to Conclusion without a separate Discussion section, which is standard for ACL/EMNLP venues, and the conclusion does offer some interpretation of the findings.

Now I'm checking whether the "roughly twice" claim about Jaccard similarity holds up against the actual numbers in the appendix. Looking at the helped sets, the observed mean is around 0.100 while the null mean is about 0.048, giving a ratio of roughly 2.08—so that phrasing is quite accurate. For the hurt sets, the observed mean is around 0.093 with a null mean starting at 0.049...

Finishing that calculation, the hurt ratio comes to about 1.86, so overall the claim of "roughly twice" is fair across both categories. However, I notice the method section claims "~2.5×" which is notably higher than the actual 2.0× ratio—that's the main discrepancy I'm finding. I should also verify the conclusion's statement about Jaccard values being at most 0.10, and checking Table 3 confirms all values stay below 0.099, so that's accurate for the 3-architecture analysis.

The experiments section mentions pairwise Jaccard staying uniformly low with a maximum of 0.099, which rounds to 0.10, so that checks out. The appendix separately discusses within-architecture Jaccard around 0.33, which the paper clearly distinguishes from the cross-architecture case. Now I'm checking whether the conclusion actually reflects what the experiments demonstrated—the multiplicity variation by task type matches section 4.1, the per-example overlap stabilization aligns with 4.2, and the two interpretations about fingerprints or something else should connect back to the experimental findings.

Looking at the conclusion's specific claims about oracle gains and performance deltas, I need to trace these back to the appendix and experiments to verify they're properly supported. The oracle exploitation numbers mentioned in the conclusion need to match what's actually reported in the experimental results. The oracle approach selects the best architecture per example, and while I can't verify the exact numbers without raw data, the appendix should contain the complementarity analysis supporting these claims. The experiments section mentions extracting 36% of the oracle gap, and the conclusion's "+7–14 pp oracle gain" appears to reference a range across different benchmarks—this could've been stated more explicitly in the main text. Now I'm noticing the abstract includes an anonymous GitHub URL with "entrainment_gated_ft" in the project name, which raises a potential anonymization concern. Looking at the appendix data to verify those ratios—the within-seed Jaccard similarity is indeed 2.7 to 4.3 times higher than cross-architecture values across the different benchmarks and metrics they tested.

I notice the Limitations section approximates this range as "3×", which is a bit of an understatement since the geometric mean is closer to 3.4, but it's a reasonable rough approximation. The section correctly cites the seed calibration appendix, though it's worth noting this experiment used Pythia 70M specifically, which is a different model family and scale than what might be discussed elsewhere in the paper.

Now let me double-check the z-score claim in method.tex—the table shows z-values of 7.11, 6.75, 8.61, 5.91, 6.85, and 6.05, all exceeding 5.9 as stated. The "~2.5×" ratio refers to the observed-to-null Jaccard ratio, which is distinct from the z-scores themselves, though both claims are technically correct since a 2.0× ratio with small null standard deviation produces those high z-values.

Looking at the ambiguity parameter values in experiments.tex, I can verify them against Table 3: PIQA at 0.14, HellaSwag at 0.15, ARC-Easy at 0.21, and LAMBADA at 0.30 all check out. The detailed ambiguity table shows slightly different precision for LAMBADA at 0.296 rather than the rounded 0.30. The rounding checks out—.296 rounds to .30 at one decimal place, so the reported range of 0.14–0.30 is consistent with the actual values. Now I'm ready to compile the full audit.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e8cadd64-7ae5-47c3-b6f0-71143f13c9fa",
  "isSidechain": false,
  "requestId": "req_011CbPfQWBpAevyUU2hLWo7m",
  "type": "assistant",
  "uuid": "2043be9a-008b-447f-b45a-67cf2058e3ad",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/sessions/paper_audit_content_6bc68a37",
  "sessionId": "6e8d5c3f-7c75-4ff9-a01f-f2df71411ac1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Aupkrgnw9hD6FqYx3VM9QD",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2008,
      "cache_read_input_tokens": 94895,
      "output_tokens": 13627,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2008,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 13627,
          "cache_read_input_tokens": 94895,
          "cache_creation_input_tokens": 2008,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2008
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

_source line 91 · 2026-05-25T17:19:05.629Z_

审计完成，编制结构化报告。

```
[CONTENT_AUDIT_START]

=== 叙事一致性（CRITICAL 级） ===

- [info] [叙事一致性] Abstract → Intro → Method → Experiments → Conclusion 主线一致：核心问题（aggregate equivalence ≠ behavioral equivalence）、方法（per-example decomposition via controlled model zoo）、三条贡献均在各章节对齐。未检测到叙事漂移。

- [critical] [叙事一致性] method.tex:72 声称 "the ~2.5× observed-to-null ratio (all z > 5.9)"，但 Abstract (main.tex:38) 正确写为 "roughly twice the independence baseline"。根据论文自身数据（Appendix Table 7/tab:jaccard_perm）：mean J_obs/J_null = (0.100/0.048, 0.093/0.050) ≈ 1.9–2.1×，不是 2.5×。Abstract 和 Method 对同一指标给出了矛盾的描述（"roughly twice" vs "~2.5×"），且 Method 的 "~2.5×" 比实际数据高 ~25%。审稿人对照 Table 7 就能发现。

- [warning] [叙事一致性] Abstract (main.tex:38) "Jaccard ≈ 0.10 ... all p < .01 across five architectures (three primary, two validation)" 的括号结构容易让读者将 "Jaccard ≈ 0.10" 同时应用于 5 架构，但 5 架构验证（340M, Appendix H）mean J_h ≈ 0.122（最高 0.134），高于 0.10。主文 §4.3 正确写为 "J ≤ 0.14"。建议 Abstract 改为 "Jaccard ≤ 0.14" 或将 "≈ 0.10" 限定为 3 架构结果。

=== 章节结构 ===

- [info] [章节结构] Abstract 回答了四个问题（问题/方法/结果/意义），~159 words，符合 EMNLP ≤ 200 words 要求。
- [info] [章节结构] Introduction 结构清晰：Hook → Context → Gap → This paper → Central finding → Contribution list。
- [info] [章节结构] Related Work 按三个主题组织（Hybrid Architectures / Linear Recurrent Models / Underspecification & Multiplicity），有归纳比较而非论文堆砌。
- [info] [章节结构] Conclusion 非常简短（6 行），仅总结发现。无 Discussion 节。对于 ACL/EMNLP 论文可接受，但审稿人可能期望更多 implications/future directions 的讨论。

=== 贡献-范围对齐 ===

- [info] [贡献-范围] 三条 Contribution 均有对应 section/table 支撑：C1→§4.1+Table 3; C2→§4.2+Figure 1; C3→§4.1 confidence paragraph + Appendix D/E。未检测到孤儿章节。
- [info] [贡献-范围] Title 范围 "Hybrid Linear Recurrent Models" 与实验覆盖的 3+2 个线性递归架构对齐。

=== Claim 强度匹配 ===

- [critical] [Claim 强度] method.tex:72 "~2.5× observed-to-null ratio" 数值不匹配论文自身数据（实际 ~2.0×）。详见叙事一致性条目。

- [info] [Claim 强度] "significantly exceeds the independence baseline" (experiments.tex:23) 有置换检验支撑 (z > 5.9, p < .0001)。合规。
- [info] [Claim 强度] "significantly negative" (experiments.tex:28, PIQA routing -0.6pp) 有 p = .006 支撑。合规。
- [info] [Claim 强度] 无 "state-of-the-art" 或 "novel" 等过强声称。Claim 整体谨慎，大量使用 hedging ("appears to stabilize", "partially predict", "suggestive")。

=== 实验严谨性 ===

- [warning] [实验严谨性] 主结果表 (Table 3/tab:multiplicity) 无 error bars 或 CI。α 的 BCa bootstrap CI 仅在 Appendix Table 6 中给出，Jaccard 的 CI 未显式报告。建议在 Table 3 增加 CI 列或脚注引用 Appendix CI。
- [info] [实验严谨性] 单次训练已在 Limitations 中明确声明。置换检验（10,000 permutations）提供统计可信度。5 架构验证增强外部有效性。Ablation（GDN 排除、连续 Jaccard、跨 scale）覆盖充分。

=== 可复现性披露 ===

- [info] [可复现性] GPU 型号（RTX PRO 6000）、计算量（~5 GPU-hours inference）、评估框架（lm-eval-harness v0.4.x）、随机种子（42）、代码 URL 均已披露。可复现性信息完备。

=== 符号/术语一致性 ===

- [info] [符号] α（ambiguity）、J（Jaccard）、σ（cross-arch std）、ρ（Spearman）、hk-1 notation 全文一致，首次出现处均有定义。
- [info] [符号] "helped/hurt/unchanged" 在 §3.4 定义，全文一致使用。

=== 章节过渡与逻辑流 ===

- [info] [逻辑流] §4.1→§4.2 有明确过渡句 "Having established that multiplicity varies by task type, we now ask whether it changes with the amount of attention." 
- [info] [逻辑流] §4.2 内含两种解释（fingerprint vs convergence），兼具 Discussion 功能。

=== Limitations 诚实度 ===

- [info] [Limitations] 4 段覆盖 4 个 distinct limitations：单次训练、format confound、覆盖范围（架构/benchmark/scale）、仅 pretrained+greedy decoding。~155 words，实质性强。

=== 去 AI 风格 ===

- [warning] [去AI] related_work.tex:7 LaTeX em-dash (---): "gated-linear RNNs---including RetNet and HGRN---can all be cast as..." → 典型解释性 em-dash，AI 写作标志。建议改为括号或逗号。
- [warning] [去AI] appendix.tex:434 "findings---within-architecture predictability coexists with..." → 解释性 em-dash。
- [warning] [去AI] appendix.tex:545 "boundary---the confidence level below which..." → 解释性 em-dash。
- [warning] [去AI] appendix.tex:653 "multiplicity---which architectures affect which examples---is consistent..." → 双 em-dash包夹插入语。
- [info] [去AI] appendix.tex:438, 455 table caption 中的 "samples---hurt/helped" 用法为紧凑标注，可接受但仍建议改为 colon 或 parentheses。
- [info] [去AI] appendix.tex:653 "Notably, the α inflation does not track accuracy loss" → filler word "Notably"，建议直接写 claim。
- [info] [去AI] 未检测到 em-dash (U+2014)、en-dash ( – ) 用作解释性标点。无 "delve/leverage/utilize/myriad/plethora"。段落长度正常，无过度分段。

=== 内部信息残留 ===

- [info] [内部信息] 匿名 URL (anonymous.4open.science) 中含项目名 "entrainment_gated_ft"，但这是匿名托管平台标准做法。正文/代码中未检测到服务器名、IP、内部实验编号、内部流程描述或框架内部术语泄露。

=== 用户自定义规则 ===

- [info] [写作规则] Abstract ~159 words，符合 EMNLP 2026 ≤ 200 words 限制。
- [info] [写作规则] 仅一个 Limitations section，位于正文 main.tex（\section*{Limitations}），appendix 无 limitations section。符合规则。
- [info] [写作规则] ARR Checklist 在独立文件 arr_checklist.tex，未 \input 进 main.tex。由用户在 OpenReview 提交表单填写。符合规则。
- [info] [审稿规则] 正文 8 页限制：基于内容量估算（intro ~1.5p + related ~0.75p + method ~2p + experiments ~3p + conclusion ~0.25p + limitations ~0.25p ≈ 7.75p），应在限制内。已编译为 21 页（含 appendix + references），正文页数需最终编译确认。

[CONTENT_AUDIT_END]
```

**关键发现汇总：**

| Severity | Count | 主要问题 |
|----------|-------|---------|
| critical | 1 | method.tex "~2.5×" 与实际数据 ~2.0× 及 Abstract "roughly twice" 矛盾 |
| warning | 5 | 1× Abstract Jaccard 范围描述与 5-arch 数据轻微脱节; 1× 主结果表缺 CI; 3× appendix 中的 LaTeX em-dash (---) |
| info | 17 | 整体质量高：叙事主线一致、claim 谨慎、可复现性完备、符号一致 |

**最需优先修复的 1 项：** method.tex:72 将 "~2.5×" 改为 "~2×" 以与 Table 7 数据和 Abstract 一致。

[AUDIT_DONE]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2043be9a-008b-447f-b45a-67cf2058e3ad",
  "isSidechain": false,
  "requestId": "req_011CbPfQWBpAevyUU2hLWo7m",
  "type": "assistant",
  "uuid": "28dcecf5-2fad-405e-804e-f279374b44e3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/sessions/paper_audit_content_6bc68a37",
  "sessionId": "6e8d5c3f-7c75-4ff9-a01f-f2df71411ac1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Aupkrgnw9hD6FqYx3VM9QD",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2008,
      "cache_read_input_tokens": 94895,
      "output_tokens": 13627,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2008,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 13627,
          "cache_read_input_tokens": 94895,
          "cache_creation_input_tokens": 2008,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2008
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

_source line 92_

```json
{
  "type": "last-prompt",
  "lastPrompt": "项目：entrainment_gated_ft Venue：emnlp-2026 论文目录：/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper  Phase 1 确定性检查结果： 源码检查: passed=False, 2 critical, 1 warning 一致性检查…",
  "leafUuid": "28dcecf5-2fad-405e-804e-f279374b44e3",
  "sessionId": "6e8d5c3f-7c75-4ff9-a01f-f2df71411ac1"
}
```

---

### Runtime record

_source line 93_

```json
{
  "type": "ai-title",
  "aiTitle": "EMNLP 2026 paper structure audit and compliance check",
  "sessionId": "6e8d5c3f-7c75-4ff9-a01f-f2df71411ac1"
}
```

---

### Runtime record

_source line 94_

```json
{
  "type": "last-prompt",
  "lastPrompt": "项目：entrainment_gated_ft Venue：emnlp-2026 论文目录：/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper  Phase 1 确定性检查结果： 源码检查: passed=False, 2 critical, 1 warning 一致性检查…",
  "leafUuid": "28dcecf5-2fad-405e-804e-f279374b44e3",
  "sessionId": "6e8d5c3f-7c75-4ff9-a01f-f2df71411ac1"
}
```

---

### Runtime record

_source line 95_

```json
{
  "type": "ai-title",
  "aiTitle": "EMNLP 2026 paper structure audit and compliance check",
  "sessionId": "6e8d5c3f-7c75-4ff9-a01f-f2df71411ac1"
}
```

---
