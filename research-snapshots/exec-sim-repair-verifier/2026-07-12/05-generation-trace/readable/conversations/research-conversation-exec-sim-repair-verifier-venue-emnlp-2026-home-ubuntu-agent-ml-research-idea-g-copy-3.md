# Research conversation: 项目：exec-sim-repair-verifier Venue：emnlp-2026 论文目录：/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-rep

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 76
- **Recorded user turns:** 1
- **Tool calls:** 23
- **Original source:** `logs/chats/exported-trajectories/account-1/d10eba16-884c-49dd-bd31-5cc0ef3bc131.jsonl`
- **Structured JSON:** [`241d2f71b28669d9784e.json`](../../sessions/24/241d2f71b28669d9784e.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-25T07:51:50.319Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-25T07:51:50.319Z",
  "sessionId": "d10eba16-884c-49dd-bd31-5cc0ef3bc131",
  "content": "项目：exec-sim-repair-verifier\nVenue：emnlp-2026\n论文目录：/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper\n\nPhase 1 确定性检查结果：\n源码检查: passed=False, 1 critical, 18 warning\n一致性检查: 0 critical, 7 warning\n编译: ✅, 页数: 24\n内部信息: 0 critical, 0 warning\n\n━━━ 用户自定义规则（作为额外检查项）━━━\n## 用户自定义规则（必须遵守）\n### 写作规则\n\n- **[EMNLP 2026]** Limitations 章节只需要写一小段，覆盖 3 个点左右就可以了，不需要写得很长\n- **[EMNLP 2026]** ARR Responsible NLP Checklist在OpenReview的submission form里面（由用户手动填写），而不是在论文pdf里面\n- **[EMNLP 2026]** 一篇文章只能有一个limitations section，放在正文里面，appendix不能有 limitations section\n- **[EMNLP 2026]** abstract 不要超过 200 words\n\n### 审稿规则\n\n- **[EMNLP 2026]** “EMNLP 2026 通过 ARR 统一审稿，Main/Findings 不分开投稿（不是两个Track），Long/Short 也走同一审稿系统，Overall Assessment的评分标准如下：5 = Consider for Award（约前2.5%），4.5 = Borderline Award，4 = Conference（可被主会议接收），3.5 = Borderline Conference，3 = Findings（可被Findings接收），2.5 = Borderline Findings，2 = Resubmit next cycle（需大幅修改，可在下一周期完成），1.5 = Resubmit after next cycle（需大幅修改，无法在下一周期完成），1 = Do not resubmit（需完全重做或与*ACL无关）”\n- **[EMNLP 2026]** EMNLP 2026 restricts long paper submissions to a strict 8-page limit for main text, with unlimited space for references. Mandatory limitations and optional ethical considerations do not count towards this page limit, provided they do not contain excessive additional content.\n\n> 以上规则由用户配置，优先级等同于硬约束。违反会被 Reviewer 标记。\n请将以上规则逐条作为额外审计维度检查。违反的规则用 dimension `[写作规则]` 或 `[审稿规则]` 标记，severity 按实际影响判定。\n\n请按照你的角色指令执行内容结构审计。"
}
```

---

### Runtime record

_source line 2 · 2026-05-25T07:51:50.324Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-25T07:51:50.324Z",
  "sessionId": "d10eba16-884c-49dd-bd31-5cc0ef3bc131"
}
```

---

## Round 1

74 recorded events

### User

_source line 3 · 2026-05-25T07:51:50.389Z_

项目：exec-sim-repair-verifier
Venue：emnlp-2026
论文目录：/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper

Phase 1 确定性检查结果：
源码检查: passed=False, 1 critical, 18 warning
一致性检查: 0 critical, 7 warning
编译: ✅, 页数: 24
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
  "promptId": "15e99bee-64bb-4bc0-b559-9e40ffdfc882",
  "type": "user",
  "uuid": "73a1261c-38a9-4402-a05d-af17d823ba75",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/paper_audit_content_8033e618",
  "sessionId": "d10eba16-884c-49dd-bd31-5cc0ef3bc131",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-25T07:51:50.388Z_

```json
{
  "parentUuid": "73a1261c-38a9-4402-a05d-af17d823ba75",
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
  "uuid": "f872db8e-dcae-41aa-9eb5-76f0a648bf60",
  "timestamp": "2026-05-25T07:51:50.388Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/paper_audit_content_8033e618",
  "sessionId": "d10eba16-884c-49dd-bd31-5cc0ef3bc131",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---

### Runtime record

_source line 5 · 2026-05-25T07:51:50.388Z_

```json
{
  "parentUuid": "f872db8e-dcae-41aa-9eb5-76f0a648bf60",
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
  "uuid": "2a5d8a2d-c11b-4077-b839-e339beb00c9b",
  "timestamp": "2026-05-25T07:51:50.388Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/paper_audit_content_8033e618",
  "sessionId": "d10eba16-884c-49dd-bd31-5cc0ef3bc131",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---

### Runtime record

_source line 6 · 2026-05-25T07:51:50.388Z_

```json
{
  "parentUuid": "2a5d8a2d-c11b-4077-b839-e339beb00c9b",
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
  "uuid": "5d64160c-ea80-45cc-8622-479ee3d5cb91",
  "timestamp": "2026-05-25T07:51:50.388Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/paper_audit_content_8033e618",
  "sessionId": "d10eba16-884c-49dd-bd31-5cc0ef3bc131",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---

### Runtime record

_source line 7 · 2026-05-25T07:51:50.388Z_

```json
{
  "parentUuid": "5d64160c-ea80-45cc-8622-479ee3d5cb91",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "263500f6-ef5b-409f-ad71-3dfa7e7da7ce",
  "timestamp": "2026-05-25T07:51:50.388Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/paper_audit_content_8033e618",
  "sessionId": "d10eba16-884c-49dd-bd31-5cc0ef3bc131",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---

### Runtime record

_source line 8_

```json
{
  "type": "ai-title",
  "aiTitle": "EMNLP 2026 paper verification and compliance audit",
  "sessionId": "d10eba16-884c-49dd-bd31-5cc0ef3bc131"
}
```

---

### Assistant

_source line 9 · 2026-05-25T07:51:54.069Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to perform a content structure audit of a paper. Let me start by reading the required skill files and all .tex files in the paper directory.

Let me first read the two skill files and find all .tex files in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "263500f6-ef5b-409f-ad71-3dfa7e7da7ce",
  "isSidechain": false,
  "requestId": "req_011CbNvWtnGuhHzeHHTEUt4a",
  "type": "assistant",
  "uuid": "75dbd0fb-1932-42de-976b-5c7f94b3e31d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/paper_audit_content_8033e618",
  "sessionId": "d10eba16-884c-49dd-bd31-5cc0ef3bc131",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J6ZLFeskuB9BUTDxntTAmm",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 28312,
      "cache_read_input_tokens": 11452,
      "output_tokens": 317,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 28312,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 317,
          "cache_read_input_tokens": 11452,
          "cache_creation_input_tokens": 28312,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 28312
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

_source line 10 · 2026-05-25T07:51:54.487Z_

开始执行论文内容结构审计。先加载审计标准和论文源码。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "75dbd0fb-1932-42de-976b-5c7f94b3e31d",
  "isSidechain": false,
  "requestId": "req_011CbNvWtnGuhHzeHHTEUt4a",
  "type": "assistant",
  "uuid": "c3d10912-4526-45de-aab7-7eb2d0bdd125",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/paper_audit_content_8033e618",
  "sessionId": "d10eba16-884c-49dd-bd31-5cc0ef3bc131",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J6ZLFeskuB9BUTDxntTAmm",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 28312,
      "cache_read_input_tokens": 11452,
      "output_tokens": 317,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 28312,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 317,
          "cache_read_input_tokens": 11452,
          "cache_creation_input_tokens": 28312,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 28312
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

_source line 11 · 2026-05-25T07:51:55.497Z_

<details open><summary>🔧 Tool call — Read · `toolu_01SBqxj4Dc1vDx1wxteP6b3x`</summary>

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
  "parentUuid": "c3d10912-4526-45de-aab7-7eb2d0bdd125",
  "isSidechain": false,
  "requestId": "req_011CbNvWtnGuhHzeHHTEUt4a",
  "type": "assistant",
  "uuid": "b19fd434-4cf0-4d05-9f6c-1782c469d3f9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/paper_audit_content_8033e618",
  "sessionId": "d10eba16-884c-49dd-bd31-5cc0ef3bc131",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J6ZLFeskuB9BUTDxntTAmm",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 28312,
      "cache_read_input_tokens": 11452,
      "output_tokens": 317,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 28312,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 317,
          "cache_read_input_tokens": 11452,
          "cache_creation_input_tokens": 28312,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 28312
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

_source line 12 · 2026-05-25T07:51:56.889Z_

<details><summary>↩ Tool result · `toolu_01HYFGv1vG6J9hhz3u6NrHt3`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/checklist.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/appendix.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/main.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/experiments.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0ab1b218-1a76-4b7d-b6f6-fc81d9fa429d",
  "isSidechain": false,
  "promptId": "15e99bee-64bb-4bc0-b559-9e40ffdfc882",
  "type": "user",
  "uuid": "6dd8e354-ad7c-49f5-b68f-a3ca4158c51c",
  "toolUseResult": {
    "filenames": [
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/checklist.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/method.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/related_work.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/conclusion.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/appendix.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/main.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/abstract.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/introduction.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/experiments.tex"
    ],
    "durationMs": 15,
    "numFiles": 9,
    "truncated": false
  },
  "sourceToolAssistantUUID": "0ab1b218-1a76-4b7d-b6f6-fc81d9fa429d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/paper_audit_content_8033e618",
  "sessionId": "d10eba16-884c-49dd-bd31-5cc0ef3bc131",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-25T07:51:55.512Z_

<details><summary>↩ Tool result · `toolu_01SBqxj4Dc1vDx1wxteP6b3x`</summary>

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
  "parentUuid": "b19fd434-4cf0-4d05-9f6c-1782c469d3f9",
  "isSidechain": false,
  "promptId": "15e99bee-64bb-4bc0-b559-9e40ffdfc882",
  "type": "user",
  "uuid": "d3b61098-b17b-4bee-9027-1df49ecf4481",
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
  "sourceToolAssistantUUID": "b19fd434-4cf0-4d05-9f6c-1782c469d3f9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/paper_audit_content_8033e618",
  "sessionId": "d10eba16-884c-49dd-bd31-5cc0ef3bc131",
  "version": "2.1.126",
  "gitBranch": "master"
}
````

</details>

---

### Tool call

_source line 14 · 2026-05-25T07:51:56.510Z_

<details open><summary>🔧 Tool call — Read · `toolu_01EizDotqG9LDRaixzhWhS5c`</summary>

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
  "parentUuid": "d3b61098-b17b-4bee-9027-1df49ecf4481",
  "isSidechain": false,
  "requestId": "req_011CbNvWtnGuhHzeHHTEUt4a",
  "type": "assistant",
  "uuid": "26704fe5-829f-4892-84bc-aa233a9fa256",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/paper_audit_content_8033e618",
  "sessionId": "d10eba16-884c-49dd-bd31-5cc0ef3bc131",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J6ZLFeskuB9BUTDxntTAmm",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 28312,
      "cache_read_input_tokens": 11452,
      "output_tokens": 317,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 28312,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 317,
          "cache_read_input_tokens": 11452,
          "cache_creation_input_tokens": 28312,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 28312
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

_source line 15 · 2026-05-25T07:51:56.518Z_

<details><summary>↩ Tool result · `toolu_01EizDotqG9LDRaixzhWhS5c`</summary>

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
  "parentUuid": "26704fe5-829f-4892-84bc-aa233a9fa256",
  "isSidechain": false,
  "promptId": "15e99bee-64bb-4bc0-b559-9e40ffdfc882",
  "type": "user",
  "uuid": "02aeded2-0e86-4f3e-bda2-33548e4ebbd3",
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
  "sourceToolAssistantUUID": "26704fe5-829f-4892-84bc-aa233a9fa256",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/paper_audit_content_8033e618",
  "sessionId": "d10eba16-884c-49dd-bd31-5cc0ef3bc131",
  "version": "2.1.126",
  "gitBranch": "master"
}
````

</details>

---

### Tool call

_source line 16 · 2026-05-25T07:51:56.868Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01HYFGv1vG6J9hhz3u6NrHt3`</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "02aeded2-0e86-4f3e-bda2-33548e4ebbd3",
  "isSidechain": false,
  "requestId": "req_011CbNvWtnGuhHzeHHTEUt4a",
  "type": "assistant",
  "uuid": "0ab1b218-1a76-4b7d-b6f6-fc81d9fa429d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/paper_audit_content_8033e618",
  "sessionId": "d10eba16-884c-49dd-bd31-5cc0ef3bc131",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J6ZLFeskuB9BUTDxntTAmm",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 28312,
      "cache_read_input_tokens": 11452,
      "output_tokens": 317,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 28312,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 317,
          "cache_read_input_tokens": 11452,
          "cache_creation_input_tokens": 28312,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 28312
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

_source line 17_

```json
{
  "type": "last-prompt",
  "lastPrompt": "项目：exec-sim-repair-verifier Venue：emnlp-2026 论文目录：/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper  Phase 1 确定性检查结果： 源码检查: passed=False, 1 critical, 18 war…",
  "leafUuid": "6dd8e354-ad7c-49f5-b68f-a3ca4158c51c",
  "sessionId": "d10eba16-884c-49dd-bd31-5cc0ef3bc131"
}
```

---

### Runtime record

_source line 18_

```json
{
  "type": "ai-title",
  "aiTitle": "EMNLP 2026 paper verification and compliance audit",
  "sessionId": "d10eba16-884c-49dd-bd31-5cc0ef3bc131"
}
```

---

### Assistant

_source line 19 · 2026-05-25T07:52:00.190Z_

<details><summary>Logged reasoning block</summary>

```text
Now I need to read all the .tex files. Let me read them in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6dd8e354-ad7c-49f5-b68f-a3ca4158c51c",
  "isSidechain": false,
  "requestId": "req_011CbNvXNj3MMNLN5yzjvaJH",
  "type": "assistant",
  "uuid": "41d684f3-fccc-47dd-8d3d-e0be4d1a4663",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/paper_audit_content_8033e618",
  "sessionId": "d10eba16-884c-49dd-bd31-5cc0ef3bc131",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RzegdawgqtJMotASk4zb6m",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11924,
      "cache_read_input_tokens": 39764,
      "output_tokens": 725,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11924,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 725,
          "cache_read_input_tokens": 39764,
          "cache_creation_input_tokens": 11924,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11924
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

_source line 20 · 2026-05-25T07:52:00.190Z_

读取所有 .tex 源码文件。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "41d684f3-fccc-47dd-8d3d-e0be4d1a4663",
  "isSidechain": false,
  "requestId": "req_011CbNvXNj3MMNLN5yzjvaJH",
  "type": "assistant",
  "uuid": "aa5b4de8-3f48-47ae-a8f8-33747b6691d4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/paper_audit_content_8033e618",
  "sessionId": "d10eba16-884c-49dd-bd31-5cc0ef3bc131",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RzegdawgqtJMotASk4zb6m",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11924,
      "cache_read_input_tokens": 39764,
      "output_tokens": 725,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11924,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 725,
          "cache_read_input_tokens": 39764,
          "cache_creation_input_tokens": 11924,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11924
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

_source line 21 · 2026-05-25T07:52:01.275Z_

<details open><summary>🔧 Tool call — Read · `toolu_01CYY3VFNw1UCs14FfbW72h3`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "aa5b4de8-3f48-47ae-a8f8-33747b6691d4",
  "isSidechain": false,
  "requestId": "req_011CbNvXNj3MMNLN5yzjvaJH",
  "type": "assistant",
  "uuid": "70631218-6154-45cf-9980-fbd2d7fce08e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/paper_audit_content_8033e618",
  "sessionId": "d10eba16-884c-49dd-bd31-5cc0ef3bc131",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RzegdawgqtJMotASk4zb6m",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11924,
      "cache_read_input_tokens": 39764,
      "output_tokens": 725,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11924,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 725,
          "cache_read_input_tokens": 39764,
          "cache_creation_input_tokens": 11924,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11924
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

_source line 22 · 2026-05-25T07:52:05.385Z_

<details><summary>↩ Tool result · `toolu_012Je55JhwmKHq9mX6tmHhqC`</summary>

```text
1	% ARR Responsible NLP Research Checklist
2	% Reference: https://aclrollingreview.org/responsibleNLPresearch/
3	
4	\section*{Responsible NLP Research Checklist}
5	
6	This paper follows the ARR Responsible NLP Research checklist.
7	
8	\subsection*{A. For Every Submission}
9	
10	\paragraph{A1. Did you describe the limitations of your work?}
11	Yes. Section~\ref{sec:conclusion} (Limitations paragraph) discusses: ${\leq}$8B LoRA scope and generalization beyond this regime, Python-only evaluation domain, and synthetic mutation vs.\ real bug representativeness. Section~\ref{sec:threats} discusses checkpoint selection, preprocessing, and seed coverage. Extended validity discussion in Appendix~\ref{app:limitations}.
12	
13	\paragraph{A2. Did you discuss any potential risks of your work?}
14	This work compares formulations for execution-free code verification on public benchmarks. The primary application is improving automated program repair pipelines. We identify no significant risks: the methods predict test outcomes rather than generating executable code, the datasets are derived from open-source repositories, and no personally identifiable information is involved. Misuse potential is limited because the verifiers require task-specific fine-tuning on labeled data and do not generalize to arbitrary code generation.
15	
16	\subsection*{B. Did You Use or Create Scientific Artifacts?}
17	
18	\paragraph{B1. Did you cite the creators of artifacts you used?}
19	Yes. All datasets (HumanEval~\cite{chen2021humaneval}, MBPP~\cite{austin2021mbpp}, SWE-bench Verified~\cite{chowdhury2024swebenchverified}), models (Qwen3~\cite{qwen2025qwen3}, DeepSeek-Coder~\cite{guo2024deepseekcoder}), and methods (LoRA~\cite{hu2022lora}, QLoRA~\cite{dettmers2024qlora}) are cited in Sections~\ref{sec:setup} and~\ref{sec:formulations}.
20	
21	\paragraph{B2. Did you discuss the license or terms for use and/or distribution of any artifacts?}
22	HumanEval is released under MIT license; MBPP under CC-BY-4.0; SWE-bench Verified under MIT license. Qwen3 models are released under Apache 2.0; DeepSeek-Coder under the DeepSeek License. All uses are consistent with their respective licenses. We do not release new artifacts in this submission.
23	
24	\paragraph{B3. Did you discuss if your use of existing artifact(s) was consistent with their intended use?}
25	Yes. All benchmarks are used for their intended purpose of evaluating code understanding and generation capabilities. SWE-bench Verified is used for repository-level evaluation as designed by its creators.
26	
27	\paragraph{B4. Did you discuss the steps taken to check whether the data contains any information that names or uniquely identifies individual people or offensive content?}
28	Not applicable. Our datasets consist of code snippets and test cases from open-source repositories. The mutation-based data construction process operates on source code only and does not involve personal data or natural language content that could contain offensive material.
29	
30	\paragraph{B5. Did you provide documentation of the artifacts?}
31	Yes. Section~\ref{sec:setup} documents dataset statistics (sizes, splits, label distributions, majority baselines). The mutation-based data construction process is described in Section~\ref{sec:setup}. Appendix~\ref{app:hyperparams} provides full hyperparameter details.
32	
33	\paragraph{B6. Did you report relevant statistics like the number of examples, details of train/test/dev splits, etc.?}
34	Yes. Section~\ref{sec:setup}: function-level 19,076 samples (train 15,290 / val 1,896 / test 1,890; pass:fail $\approx$ 52:48); repo-level ${\sim}$70K training, val $n{=}9{,}335$, test $n{=}9{,}784$ (majority baseline 72.96\%).
35	
36	\subsection*{C. Did You Run Computational Experiments?}
37	
38	\paragraph{C1. Did you report the number of parameters in the models used, the total computational budget, and computing infrastructure?}
39	Yes. Models: Qwen3-4B (${\sim}$4B parameters, LoRA rank 16 $\approx$ 4M trainable), Qwen3-8B (${\sim}$8B), DeepSeek-Coder-6.7B (${\sim}$6.7B). Infrastructure: 4$\times$ NVIDIA RTX 5090 GPUs. Total compute: ${\sim}$370 GPU-hours across 223 completed runs (${\sim}$46 configurations including seeds, formulations, model sizes, and ablations). Appendix~\ref{app:hyperparams} provides per-run details.
40	
41	\paragraph{C2. Did you discuss the experimental setup, including hyperparameter search and best-found hyperparameter values?}
42	Yes. Section~\ref{sec:setup} reports the training configuration (LoRA rank 16, 3 epochs, 5 seeds with mixed precision). Appendix~\ref{app:hyperparams} provides full hyperparameter values. We use a fixed configuration rather than extensive hyperparameter search; repo-level models use validation accuracy for checkpoint selection.
43	
44	\paragraph{C3. Did you report descriptive statistics about your results with, e.g., error bars or confidence intervals?}
45	Yes. All multi-seed results report mean $\pm$ standard deviation. Confidence intervals use clustered bootstrap (114 problem clusters, 10K resamples; Section~\ref{sec:setup}). Equivalence testing uses TOST with $\pm$2\pp{} margin and seed-level paired analysis (\cls{}--\cwm{} $p{=}0.007$, \cls{}--\traj{} $p{=}0.025$; Section~\ref{sec:equivalence}). ICC quantifies within-problem correlation with design effect reported.
46	
47	\paragraph{C4. If you used existing packages, did you report the implementation and version numbers?}
48	Yes. Implementation uses HuggingFace Transformers (${\geq}$4.44), PEFT (${\geq}$0.12), PyTorch (${\geq}$2.0), bitsandbytes (${\geq}$0.43, for NF4 quantization), and Python 3.10. LoRA~\cite{hu2022lora} and QLoRA~\cite{dettmers2024qlora} configurations are detailed in Appendix~\ref{app:hyperparams}. Exact version pinning is provided in the code repository.
49	
50	\subsection*{D. Did You Use Human Annotators?}
51	
52	Not applicable. This work uses no human annotators or participants. All labels are derived from automated test execution.
53	
54	\subsection*{E. AI Assistants}
55	
56	\paragraph{E1. Did you use AI assistants (e.g., ChatGPT, Copilot) in any part of the paper writing or coding process?}
57	Yes. See Appendix~\ref{app:ai-assistants} for details on the AI assistant (Claude, Anthropic) used for code development, writing, and literature summarization.
58	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6426325f-a0e8-4594-ac86-9e842fc8d5f8",
  "isSidechain": false,
  "promptId": "15e99bee-64bb-4bc0-b559-9e40ffdfc882",
  "type": "user",
  "uuid": "e024b451-7584-48e9-bd92-da1022162825",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/checklist.tex",
      "content": "% ARR Responsible NLP Research Checklist\n% Reference: https://aclrollingreview.org/responsibleNLPresearch/\n\n\\section*{Responsible NLP Research Checklist}\n\nThis paper follows the ARR Responsible NLP Research checklist.\n\n\\subsection*{A. For Every Submission}\n\n\\paragraph{A1. Did you describe the limitations of your work?}\nYes. Section~\\ref{sec:conclusion} (Limitations paragraph) discusses: ${\\leq}$8B LoRA scope and generalization beyond this regime, Python-only evaluation domain, and synthetic mutation vs.\\ real bug representativeness. Section~\\ref{sec:threats} discusses checkpoint selection, preprocessing, and seed coverage. Extended validity discussion in Appendix~\\ref{app:limitations}.\n\n\\paragraph{A2. Did you discuss any potential risks of your work?}\nThis work compares formulations for execution-free code verification on public benchmarks. The primary application is improving automated program repair pipelines. We identify no significant risks: the methods predict test outcomes rather than generating executable code, the datasets are derived from open-source repositories, and no personally identifiable information is involved. Misuse potential is limited because the verifiers require task-specific fine-tuning on labeled data and do not generalize to arbitrary code generation.\n\n\\subsection*{B. Did You Use or Create Scientific Artifacts?}\n\n\\paragraph{B1. Did you cite the creators of artifacts you used?}\nYes. All datasets (HumanEval~\\cite{chen2021humaneval}, MBPP~\\cite{austin2021mbpp}, SWE-bench Verified~\\cite{chowdhury2024swebenchverified}), models (Qwen3~\\cite{qwen2025qwen3}, DeepSeek-Coder~\\cite{guo2024deepseekcoder}), and methods (LoRA~\\cite{hu2022lora}, QLoRA~\\cite{dettmers2024qlora}) are cited in Sections~\\ref{sec:setup} and~\\ref{sec:formulations}.\n\n\\paragraph{B2. Did you discuss the license or terms for use and/or distribution of any artifacts?}\nHumanEval is released under MIT license; MBPP under CC-BY-4.0; SWE-bench Verified under MIT license. Qwen3 models are released under Apache 2.0; DeepSeek-Coder under the DeepSeek License. All uses are consistent with their respective licenses. We do not release new artifacts in this submission.\n\n\\paragraph{B3. Did you discuss if your use of existing artifact(s) was consistent with their intended use?}\nYes. All benchmarks are used for their intended purpose of evaluating code understanding and generation capabilities. SWE-bench Verified is used for repository-level evaluation as designed by its creators.\n\n\\paragraph{B4. Did you discuss the steps taken to check whether the data contains any information that names or uniquely identifies individual people or offensive content?}\nNot applicable. Our datasets consist of code snippets and test cases from open-source repositories. The mutation-based data construction process operates on source code only and does not involve personal data or natural language content that could contain offensive material.\n\n\\paragraph{B5. Did you provide documentation of the artifacts?}\nYes. Section~\\ref{sec:setup} documents dataset statistics (sizes, splits, label distributions, majority baselines). The mutation-based data construction process is described in Section~\\ref{sec:setup}. Appendix~\\ref{app:hyperparams} provides full hyperparameter details.\n\n\\paragraph{B6. Did you report relevant statistics like the number of examples, details of train/test/dev splits, etc.?}\nYes. Section~\\ref{sec:setup}: function-level 19,076 samples (train 15,290 / val 1,896 / test 1,890; pass:fail $\\approx$ 52:48); repo-level ${\\sim}$70K training, val $n{=}9{,}335$, test $n{=}9{,}784$ (majority baseline 72.96\\%).\n\n\\subsection*{C. Did You Run Computational Experiments?}\n\n\\paragraph{C1. Did you report the number of parameters in the models used, the total computational budget, and computing infrastructure?}\nYes. Models: Qwen3-4B (${\\sim}$4B parameters, LoRA rank 16 $\\approx$ 4M trainable), Qwen3-8B (${\\sim}$8B), DeepSeek-Coder-6.7B (${\\sim}$6.7B). Infrastructure: 4$\\times$ NVIDIA RTX 5090 GPUs. Total compute: ${\\sim}$370 GPU-hours across 223 completed runs (${\\sim}$46 configurations including seeds, formulations, model sizes, and ablations). Appendix~\\ref{app:hyperparams} provides per-run details.\n\n\\paragraph{C2. Did you discuss the experimental setup, including hyperparameter search and best-found hyperparameter values?}\nYes. Section~\\ref{sec:setup} reports the training configuration (LoRA rank 16, 3 epochs, 5 seeds with mixed precision). Appendix~\\ref{app:hyperparams} provides full hyperparameter values. We use a fixed configuration rather than extensive hyperparameter search; repo-level models use validation accuracy for checkpoint selection.\n\n\\paragraph{C3. Did you report descriptive statistics about your results with, e.g., error bars or confidence intervals?}\nYes. All multi-seed results report mean $\\pm$ standard deviation. Confidence intervals use clustered bootstrap (114 problem clusters, 10K resamples; Section~\\ref{sec:setup}). Equivalence testing uses TOST with $\\pm$2\\pp{} margin and seed-level paired analysis (\\cls{}--\\cwm{} $p{=}0.007$, \\cls{}--\\traj{} $p{=}0.025$; Section~\\ref{sec:equivalence}). ICC quantifies within-problem correlation with design effect reported.\n\n\\paragraph{C4. If you used existing packages, did you report the implementation and version numbers?}\nYes. Implementation uses HuggingFace Transformers (${\\geq}$4.44), PEFT (${\\geq}$0.12), PyTorch (${\\geq}$2.0), bitsandbytes (${\\geq}$0.43, for NF4 quantization), and Python 3.10. LoRA~\\cite{hu2022lora} and QLoRA~\\cite{dettmers2024qlora} configurations are detailed in Appendix~\\ref{app:hyperparams}. Exact version pinning is provided in the code repository.\n\n\\subsection*{D. Did You Use Human Annotators?}\n\nNot applicable. This work uses no human annotators or participants. All labels are derived from automated test execution.\n\n\\subsection*{E. AI Assistants}\n\n\\paragraph{E1. Did you use AI assistants (e.g., ChatGPT, Copilot) in any part of the paper writing or coding process?}\nYes. See Appendix~\\ref{app:ai-assistants} for details on the AI assistant (Claude, Anthropic) used for code development, writing, and literature summarization.\n",
      "numLines": 58,
      "startLine": 1,
      "totalLines": 58
    }
  },
  "sourceToolAssistantUUID": "6426325f-a0e8-4594-ac86-9e842fc8d5f8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/paper_audit_content_8033e618",
  "sessionId": "d10eba16-884c-49dd-bd31-5cc0ef3bc131",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-25T07:52:01.283Z_

<details><summary>↩ Tool result · `toolu_01CYY3VFNw1UCs14FfbW72h3`</summary>

```text
1	\begin{abstract}
2	Execution-free verification promises to replace costly test execution in Large Language Model (LLM)-based program repair, yet practitioners must choose among three fundamentally different formulations with no controlled comparison to guide the decision: per-test classification (\cls{}), execution output generation (\cwm{}), and trajectory-level scoring (\traj{}). We present the first systematic comparison, controlling for model capacity, training data, and evaluation protocol across two code LLM families (Qwen3, DeepSeek-Coder), two complexity levels, and multiple random seeds under ${\leq}$8B Low-Rank Adaptation (LoRA) fine-tuning. Our central finding is that \emph{code complexity moderates the classification--generation tradeoff}. When outputs are short (function-level verification), all three formulations achieve statistically equivalent accuracy. When outputs grow longer and more structured (repository-level verification), this equivalence breaks down: generation-based verification suffers format collapse, falling well below classification. Preliminary results at 14B suggest this divergence narrows with scale, pointing to a capacity-dependent rather than formulation-inherent limitation. A failure mode taxonomy and error complementarity analysis provide actionable guidance for formulation selection and motivate complexity-aware routing as a key open direction.
3	\end{abstract}
4	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "70631218-6154-45cf-9980-fbd2d7fce08e",
  "isSidechain": false,
  "promptId": "15e99bee-64bb-4bc0-b559-9e40ffdfc882",
  "type": "user",
  "uuid": "84e94e83-6c3a-4919-9512-16d2df65d709",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/abstract.tex",
      "content": "\\begin{abstract}\nExecution-free verification promises to replace costly test execution in Large Language Model (LLM)-based program repair, yet practitioners must choose among three fundamentally different formulations with no controlled comparison to guide the decision: per-test classification (\\cls{}), execution output generation (\\cwm{}), and trajectory-level scoring (\\traj{}). We present the first systematic comparison, controlling for model capacity, training data, and evaluation protocol across two code LLM families (Qwen3, DeepSeek-Coder), two complexity levels, and multiple random seeds under ${\\leq}$8B Low-Rank Adaptation (LoRA) fine-tuning. Our central finding is that \\emph{code complexity moderates the classification--generation tradeoff}. When outputs are short (function-level verification), all three formulations achieve statistically equivalent accuracy. When outputs grow longer and more structured (repository-level verification), this equivalence breaks down: generation-based verification suffers format collapse, falling well below classification. Preliminary results at 14B suggest this divergence narrows with scale, pointing to a capacity-dependent rather than formulation-inherent limitation. A failure mode taxonomy and error complementarity analysis provide actionable guidance for formulation selection and motivate complexity-aware routing as a key open direction.\n\\end{abstract}\n",
      "numLines": 4,
      "startLine": 1,
      "totalLines": 4
    }
  },
  "sourceToolAssistantUUID": "70631218-6154-45cf-9980-fbd2d7fce08e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/paper_audit_content_8033e618",
  "sessionId": "d10eba16-884c-49dd-bd31-5cc0ef3bc131",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-25T07:52:01.719Z_

<details open><summary>🔧 Tool call — Read · `toolu_01F9ByU3fCxepNkeAypoCGXX`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "84e94e83-6c3a-4919-9512-16d2df65d709",
  "isSidechain": false,
  "requestId": "req_011CbNvXNj3MMNLN5yzjvaJH",
  "type": "assistant",
  "uuid": "4843bf34-d47e-44a4-9b22-b313aca093f4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/paper_audit_content_8033e618",
  "sessionId": "d10eba16-884c-49dd-bd31-5cc0ef3bc131",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RzegdawgqtJMotASk4zb6m",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11924,
      "cache_read_input_tokens": 39764,
      "output_tokens": 725,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11924,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 725,
          "cache_read_input_tokens": 39764,
          "cache_creation_input_tokens": 11924,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11924
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

_source line 25 · 2026-05-25T07:52:01.724Z_

<details><summary>↩ Tool result · `toolu_01F9ByU3fCxepNkeAypoCGXX`</summary>

```text
1	\section{Introduction}
2	\label{sec:introduction}
3	
4	LLM-based automated program repair systems increasingly rely on test-time compute scaling: generating $K$ candidate patches and selecting the best via a verifier~\cite{snell2024scaling}. Full execution verification is reliable but expensive (\$1--3 per candidate at repository scale\footnote{Based on per-instance costs reported by \citet{yang2024sweagent} and \citet{xia2024agentless}.}), driving demand for execution-free alternatives. Three distinct formulations have emerged for this task: \textbf{generation-based simulation}~\cite{meta2025cwm,maimon2026selfexecution} predicts execution output strings per test; \textbf{trajectory-level scoring}~\cite{shum2025swerm} predicts a binary patch verdict without per-test decomposition; and \textbf{per-test classification}~\cite{ni2023lever,chen2023codet} predicts a pass/fail token per test. Each makes different tradeoffs between diagnostic granularity, output complexity, and inference cost.
5	
6	Despite active development along each axis, no prior work provides a systematic comparison holding model capacity, training data, and compute constant. Practitioners choosing a formulation for their verification pipeline must rely on results from different models, different datasets, and different evaluation protocols. Whether one formulation is uniformly preferable, or whether the choice depends on properties of the code being verified, remains an open empirical question. This connects to a broader pattern in NLP: task formulation (classification vs.\ generation vs.\ span extraction) systematically affects performance~\cite{raffel2020t5}, but the conditions under which each wins remain task-dependent and empirically unresolved. Recent evidence that generation-based verification outperforms classification in mathematical reasoning~\cite{hosseini2025genrm} raises a further question: does this advantage transfer to code verification, where outputs are longer and format-constrained? A related question is whether formulation choice matters at all relative to more basic decisions: at what complexity level does fine-tuning become necessary, and does formulation selection add value beyond what fine-tuning alone provides?
7	
8	We present the first systematic comparison across two code LLM families (Qwen3, DeepSeek-Coder), two complexity levels, and multiple seeds under ${\leq}$8B LoRA fine-tuning. By controlling model capacity, training data, and evaluation protocol, we isolate the effect of formulation choice itself. Our central finding is that \emph{code complexity moderates the classification--generation tradeoff}: at function level, all formulations achieve comparable accuracy; at repository level, this equivalence breaks down as generation-based verification suffers format collapse. Figure~\ref{fig:reformulation} illustrates the three formulations.
9	
10	We make the following contributions:
11	
12	\begin{itemize}[leftmargin=*,itemsep=2pt]
13	\item \textbf{Complexity-moderated equivalence and divergence.} At function level, classification and generation are statistically equivalent; at repository level, generation accuracy drops sharply due to output format complexity, while classification and trajectory scoring remain competitive (\S\ref{sec:equivalence}, \S\ref{sec:repo}).
14	
15	\item \textbf{Failure mode taxonomy and error analysis.} We identify three distinct failure modes at repository level (format collapse, decision collapse, aggregation penalty) and show that formulations make partially complementary errors, motivating complexity-aware routing (\S\ref{sec:repo}, \S\ref{sec:analysis}).
16	\end{itemize}
17	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4843bf34-d47e-44a4-9b22-b313aca093f4",
  "isSidechain": false,
  "promptId": "15e99bee-64bb-4bc0-b559-9e40ffdfc882",
  "type": "user",
  "uuid": "494a7db3-b125-4965-8e1f-a5c1b17b3b9e",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/introduction.tex",
      "content": "\\section{Introduction}\n\\label{sec:introduction}\n\nLLM-based automated program repair systems increasingly rely on test-time compute scaling: generating $K$ candidate patches and selecting the best via a verifier~\\cite{snell2024scaling}. Full execution verification is reliable but expensive (\\$1--3 per candidate at repository scale\\footnote{Based on per-instance costs reported by \\citet{yang2024sweagent} and \\citet{xia2024agentless}.}), driving demand for execution-free alternatives. Three distinct formulations have emerged for this task: \\textbf{generation-based simulation}~\\cite{meta2025cwm,maimon2026selfexecution} predicts execution output strings per test; \\textbf{trajectory-level scoring}~\\cite{shum2025swerm} predicts a binary patch verdict without per-test decomposition; and \\textbf{per-test classification}~\\cite{ni2023lever,chen2023codet} predicts a pass/fail token per test. Each makes different tradeoffs between diagnostic granularity, output complexity, and inference cost.\n\nDespite active development along each axis, no prior work provides a systematic comparison holding model capacity, training data, and compute constant. Practitioners choosing a formulation for their verification pipeline must rely on results from different models, different datasets, and different evaluation protocols. Whether one formulation is uniformly preferable, or whether the choice depends on properties of the code being verified, remains an open empirical question. This connects to a broader pattern in NLP: task formulation (classification vs.\\ generation vs.\\ span extraction) systematically affects performance~\\cite{raffel2020t5}, but the conditions under which each wins remain task-dependent and empirically unresolved. Recent evidence that generation-based verification outperforms classification in mathematical reasoning~\\cite{hosseini2025genrm} raises a further question: does this advantage transfer to code verification, where outputs are longer and format-constrained? A related question is whether formulation choice matters at all relative to more basic decisions: at what complexity level does fine-tuning become necessary, and does formulation selection add value beyond what fine-tuning alone provides?\n\nWe present the first systematic comparison across two code LLM families (Qwen3, DeepSeek-Coder), two complexity levels, and multiple seeds under ${\\leq}$8B LoRA fine-tuning. By controlling model capacity, training data, and evaluation protocol, we isolate the effect of formulation choice itself. Our central finding is that \\emph{code complexity moderates the classification--generation tradeoff}: at function level, all formulations achieve comparable accuracy; at repository level, this equivalence breaks down as generation-based verification suffers format collapse. Figure~\\ref{fig:reformulation} illustrates the three formulations.\n\nWe make the following contributions:\n\n\\begin{itemize}[leftmargin=*,itemsep=2pt]\n\\item \\textbf{Complexity-moderated equivalence and divergence.} At function level, classification and generation are statistically equivalent; at repository level, generation accuracy drops sharply due to output format complexity, while classification and trajectory scoring remain competitive (\\S\\ref{sec:equivalence}, \\S\\ref{sec:repo}).\n\n\\item \\textbf{Failure mode taxonomy and error analysis.} We identify three distinct failure modes at repository level (format collapse, decision collapse, aggregation penalty) and show that formulations make partially complementary errors, motivating complexity-aware routing (\\S\\ref{sec:repo}, \\S\\ref{sec:analysis}).\n\\end{itemize}\n",
      "numLines": 17,
      "startLine": 1,
      "totalLines": 17
    }
  },
  "sourceToolAssistantUUID": "4843bf34-d47e-44a4-9b22-b313aca093f4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/paper_audit_content_8033e618",
  "sessionId": "d10eba16-884c-49dd-bd31-5cc0ef3bc131",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-25T07:52:02.227Z_

<details open><summary>🔧 Tool call — Read · `toolu_017ryP4gsKn3xBrQpYcu8wWS`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "494a7db3-b125-4965-8e1f-a5c1b17b3b9e",
  "isSidechain": false,
  "requestId": "req_011CbNvXNj3MMNLN5yzjvaJH",
  "type": "assistant",
  "uuid": "58468d1c-5a1d-4a93-8ec8-2db42b09882d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/paper_audit_content_8033e618",
  "sessionId": "d10eba16-884c-49dd-bd31-5cc0ef3bc131",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RzegdawgqtJMotASk4zb6m",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11924,
      "cache_read_input_tokens": 39764,
      "output_tokens": 725,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11924,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 725,
          "cache_read_input_tokens": 39764,
          "cache_creation_input_tokens": 11924,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11924
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

_source line 27 · 2026-05-25T07:52:02.232Z_

<details><summary>↩ Tool result · `toolu_017ryP4gsKn3xBrQpYcu8wWS`</summary>

```text
1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Execution Simulation and Verification.}
5	Execution trace generation improves code reasoning~\cite{nye2021scratchpad}, with extensions to output prediction~\cite{meta2025cwm,maimon2026selfexecution,liu2024codemind,liu2023codeexecutor,lee2026solidcoder}, failure analysis~\cite{abdollahi2025demystifying}, and error detection~\cite{li2024redo}. CRUXEval~\citep{gu2024cruxeval} benchmarks code execution prediction at function level; RepoExec~\citep{nam2025repoexec} evaluates repo-level code generation with execution-based correctness checks. Our work extends execution prediction to repo-level repair verification. Verification formulations span trajectory-level reward~\cite{shum2025swerm}, process-level feedback~\cite{li2025codeprm,xu2025patchreasoner}, per-test classification~\cite{ni2023lever,chen2023codet}, learned metrics~\cite{zhuo2024icescore,dong2024codescore,zhou2023codebertscore}, and RL with execution-based rewards~\cite{wang2026verpo,tang2026execverify}. Aletheia~\cite{venkatkrishna2026aletheia} compares training recipes; we compare \emph{formulations}. Test-time scaling~\cite{snell2024scaling,li2025sstar,chen2025vgsearch} and self-consistency~\cite{wang2023selfconsistency} demonstrate verification value; none compare formulations at matched capacity.
6	
7	\paragraph{Process vs.\ Outcome Supervision.}
8	Process Reward Models (PRMs) outperform Outcome Reward Models (ORMs) for math reasoning~\cite{lightman2023letsverify,uesato2022solving}, with automated annotation~\cite{wang2024mathshepherd,luo2024omegaprm} and code-specific extensions~\cite{ye2025prlcoder,zhang2026funprm,jiang2025coderlplus}. DreamPRM~\cite{dreamprm2025code} and CodePRM~\cite{li2025codeprm} optimize reward quality within a fixed formulation; we compare across formulations at matched capacity. GenRM~\cite{hosseini2025genrm} and GenPRM~\cite{zhao2026genprm} show that generative verifiers outperform discriminative ones for math reasoning; our results reveal a domain difference: in code verification, the generative formulation (\cwm{}) does not outperform the discriminative one (\cls{}), suggesting that the generation advantage may be domain-specific (Appendix~\ref{app:threats}). CodeRM~\cite{ma2025coderm} corroborates our finding that per-test granularity provides diagnostic value. In reward modeling terms, \cls{} maps to PRM (tests as reasoning steps), \traj{} to ORM, and \cwm{} to generative verification~\cite{hosseini2025genrm}; we additionally vary output format.
9	
10	\paragraph{Repair, Mutation Testing, and Task Framing.}
11	CodeRL~\cite{le2022coderl}, AlphaCode~\cite{li2022alphacode,alphacode2023team}, and Reflexion~\cite{shinn2023reflexion} use execution feedback for repair. SWE-bench~\cite{jimenez2024swebench,chowdhury2024swebenchverified} provides benchmarks; SWE-agent~\cite{yang2024sweagent} and Agentless~\cite{xia2024agentless} demonstrate pipelines where verification is a bottleneck~\cite{yang2025aprsurvey}. Predictive mutation testing~\cite{tufano2019predictive,kim2022predictive,wang2024llmmutation,jain2023contextual} shares our per-test structure. \citet{raffel2020t5} showed that task framing affects performance across NLP tasks; we extend this to code verification, finding that complexity moderates the classification--generation tradeoff.
12	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "58468d1c-5a1d-4a93-8ec8-2db42b09882d",
  "isSidechain": false,
  "promptId": "15e99bee-64bb-4bc0-b559-9e40ffdfc882",
  "type": "user",
  "uuid": "0d975cff-d591-407d-8b89-25bbfee332f2",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/related_work.tex",
      "content": "\\section{Related Work}\n\\label{sec:related_work}\n\n\\paragraph{Execution Simulation and Verification.}\nExecution trace generation improves code reasoning~\\cite{nye2021scratchpad}, with extensions to output prediction~\\cite{meta2025cwm,maimon2026selfexecution,liu2024codemind,liu2023codeexecutor,lee2026solidcoder}, failure analysis~\\cite{abdollahi2025demystifying}, and error detection~\\cite{li2024redo}. CRUXEval~\\citep{gu2024cruxeval} benchmarks code execution prediction at function level; RepoExec~\\citep{nam2025repoexec} evaluates repo-level code generation with execution-based correctness checks. Our work extends execution prediction to repo-level repair verification. Verification formulations span trajectory-level reward~\\cite{shum2025swerm}, process-level feedback~\\cite{li2025codeprm,xu2025patchreasoner}, per-test classification~\\cite{ni2023lever,chen2023codet}, learned metrics~\\cite{zhuo2024icescore,dong2024codescore,zhou2023codebertscore}, and RL with execution-based rewards~\\cite{wang2026verpo,tang2026execverify}. Aletheia~\\cite{venkatkrishna2026aletheia} compares training recipes; we compare \\emph{formulations}. Test-time scaling~\\cite{snell2024scaling,li2025sstar,chen2025vgsearch} and self-consistency~\\cite{wang2023selfconsistency} demonstrate verification value; none compare formulations at matched capacity.\n\n\\paragraph{Process vs.\\ Outcome Supervision.}\nProcess Reward Models (PRMs) outperform Outcome Reward Models (ORMs) for math reasoning~\\cite{lightman2023letsverify,uesato2022solving}, with automated annotation~\\cite{wang2024mathshepherd,luo2024omegaprm} and code-specific extensions~\\cite{ye2025prlcoder,zhang2026funprm,jiang2025coderlplus}. DreamPRM~\\cite{dreamprm2025code} and CodePRM~\\cite{li2025codeprm} optimize reward quality within a fixed formulation; we compare across formulations at matched capacity. GenRM~\\cite{hosseini2025genrm} and GenPRM~\\cite{zhao2026genprm} show that generative verifiers outperform discriminative ones for math reasoning; our results reveal a domain difference: in code verification, the generative formulation (\\cwm{}) does not outperform the discriminative one (\\cls{}), suggesting that the generation advantage may be domain-specific (Appendix~\\ref{app:threats}). CodeRM~\\cite{ma2025coderm} corroborates our finding that per-test granularity provides diagnostic value. In reward modeling terms, \\cls{} maps to PRM (tests as reasoning steps), \\traj{} to ORM, and \\cwm{} to generative verification~\\cite{hosseini2025genrm}; we additionally vary output format.\n\n\\paragraph{Repair, Mutation Testing, and Task Framing.}\nCodeRL~\\cite{le2022coderl}, AlphaCode~\\cite{li2022alphacode,alphacode2023team}, and Reflexion~\\cite{shinn2023reflexion} use execution feedback for repair. SWE-bench~\\cite{jimenez2024swebench,chowdhury2024swebenchverified} provides benchmarks; SWE-agent~\\cite{yang2024sweagent} and Agentless~\\cite{xia2024agentless} demonstrate pipelines where verification is a bottleneck~\\cite{yang2025aprsurvey}. Predictive mutation testing~\\cite{tufano2019predictive,kim2022predictive,wang2024llmmutation,jain2023contextual} shares our per-test structure. \\citet{raffel2020t5} showed that task framing affects performance across NLP tasks; we extend this to code verification, finding that complexity moderates the classification--generation tradeoff.\n",
      "numLines": 12,
      "startLine": 1,
      "totalLines": 12
    }
  },
  "sourceToolAssistantUUID": "58468d1c-5a1d-4a93-8ec8-2db42b09882d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/paper_audit_content_8033e618",
  "sessionId": "d10eba16-884c-49dd-bd31-5cc0ef3bc131",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-25T07:52:02.663Z_

<details open><summary>🔧 Tool call — Read · `toolu_01U3kfsbhxTNUnjVNvKfFMcx`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0d975cff-d591-407d-8b89-25bbfee332f2",
  "isSidechain": false,
  "requestId": "req_011CbNvXNj3MMNLN5yzjvaJH",
  "type": "assistant",
  "uuid": "b3ffea19-559e-4e51-9a28-4ddeb592e95b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/paper_audit_content_8033e618",
  "sessionId": "d10eba16-884c-49dd-bd31-5cc0ef3bc131",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RzegdawgqtJMotASk4zb6m",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11924,
      "cache_read_input_tokens": 39764,
      "output_tokens": 725,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11924,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 725,
          "cache_read_input_tokens": 39764,
          "cache_creation_input_tokens": 11924,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11924
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

_source line 29 · 2026-05-25T07:52:02.669Z_

<details><summary>↩ Tool result · `toolu_01U3kfsbhxTNUnjVNvKfFMcx`</summary>

```text
1	\section{Method}
2	\label{sec:method}
3	
4	Let $p$ denote a candidate patch and $T = \{t_1, \ldots, t_n\}$ its test suite, where each $t_i$ has label $y_i \in \{\text{\textsc{Pass}}, \text{\textsc{Fail}}\}$ from execution. Tests decompose into \emph{fail-to-pass} ($T_{\text{f2p}}$) and \emph{pass-to-pass} ($T_{\text{p2p}}$) subsets; a patch is correct iff $\forall\, t_i{:}\ y_i = \text{\textsc{Pass}}$. We compare three formulations for predicting correctness without execution.
5	
6	\subsection{Verification Formulations}
7	\label{sec:formulations}
8	
9	Let $c_p$ denote the code context (unified diff) of patch $p$.
10	
11	\paragraph{\cls{} (per-test classification).} $f(c_p, t_i) \rightarrow \hat{y}_i \in \{\text{\textsc{Pass}}, \text{\textsc{Fail}}\}$ predicts a single binary token per test (cross-entropy loss). Patch verdict: $\hat{y}_p = \bigwedge_{i} [\hat{y}_i = \text{\textsc{Pass}}]$. Output cost: one token per test.
12	
13	\paragraph{\cwm{} (output generation).}\footnote{We use ``code world model'' following \citet{meta2025cwm} to denote execution output prediction, distinct from world models in model-based reinforcement learning.} $g(c_p, t_i) \rightarrow \hat{o}_i \in \Sigma^*$ generates the execution output string (language modeling loss). Verdict by exact match: $\hat{y}_i = \text{\textsc{Pass}}$ iff $\hat{o}_i = o_i^*$.\footnote{Exact string matching is conservative, consistent with \citet{meta2025cwm}. Semantic equivalences are not counted.} When the generated output is unparseable (i.e., does not conform to the expected structured format), the prediction defaults to the majority class verdict. Output cost: $\sum_i |\hat{o}_i|$ tokens.
14	
15	\paragraph{\traj{} (trajectory-level).} $h(c_p, T) \rightarrow \hat{y}_p \in \{\text{\textsc{Resolved}}, \text{\textsc{Unresolved}}\}$ predicts a single patch verdict from all tests and provides no per-test signal. \traj{} serves as a granularity control: \cls{}--\traj{} differences isolate the value of per-test decomposition independent of the classification formulation itself.
16	
17	\subsection{Expected Failure Modes}
18	\label{sec:failure-modes}
19	
20	Each formulation has characteristic failure modes that differ in their sensitivity to code complexity:
21	
22	\paragraph{Generation failure modes (\cwm{}).} The open-ended output space introduces three failure modes: (1)~\emph{token-budget exhaustion}, where $|o_i^*| > B$ guarantees exact-match failure due to truncation; (2)~\emph{string-value prediction errors}, where semantically equivalent outputs differing in surface form (floating-point precision, dictionary ordering) produce false negatives; and (3)~\emph{format compliance collapse}, where the model fails to produce structured predictions entirely at high input complexity, even when the generation budget is sufficient. Under optimistic independence, a token sequence of length $L$ with per-token accuracy $q$ has correct-sequence probability $q^L$; long outputs are therefore exponentially harder to predict exactly. We adopt exact string matching following the original \cwm{} evaluation protocol~\citep{meta2025cwm}. Unparseable predictions default to the majority-class label (\textsc{Pass}).
23	
24	\paragraph{Classification failure modes (\cls{}).} The single-token output space eliminates format and truncation failures but constrains the model to encode its reasoning entirely within internal representations, without the intermediate reasoning trace that generation provides. \cls{} errors manifest as false positives or false negatives without format failures; at function level, a mild FP bias (56.5\%) emerges, with the error direction depending on class distribution and fine-tuning dynamics.
25	
26	\paragraph{Trajectory-level failure modes (\traj{}).} By collapsing all per-test information into a single binary verdict, \traj{} discards diagnostic granularity. When a patch fails multiple tests, the trajectory-level formulation cannot identify \emph{which} tests fail. This limits downstream utility (e.g., targeted re-repair) but avoids per-test aggregation errors.
27	
28	\paragraph{Complexity dependence.} These failure modes suggest a complexity-dependent interaction: when execution outputs are short and structured (function-level code), generation modes (1)--(2) are rarely triggered, and all formulations should perform comparably. As output length and structural complexity increase (repository-level code), generation-specific failures may compound, creating divergence. Whether this divergence reflects a fundamental property of the generation formulation or is contingent on model/tokenizer properties is an empirical question we investigate in \S\ref{sec:experiments}.
29	
30	\subsection{Oracle Accuracy-Utility Framework}
31	\label{sec:oracle}
32	
33	For a buggy patch with $k = |T_{\text{f2p}}|$ fail-to-pass tests, a per-test verifier with recall $r$ detects the bug if it identifies at least one failing test: $P_{\text{detect}}(k) = 1 - (1 - r)^{k_{\text{eff}}}$, where $k_{\text{eff}} = k / (1 + (k-1)\rho)$ accounts for within-patch correlation via ICC $\rho$~\citep{shrout1979icc}. The per-test advantage over a trajectory-level baseline ($a_h$) is $\Delta(k) = P_{\text{detect}}(k) - a_h$, with population expectation $\mathbb{E}[\Delta] = \sum_{k} P(|T_{\text{f2p}}| = k) \cdot \Delta(k)$. This predicts that per-test advantage concentrates in multi-F2P-test instances and vanishes at $k{=}1$, validated in \S\ref{sec:experiments} and Appendix~\ref{app:oracle}.
34	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b3ffea19-559e-4e51-9a28-4ddeb592e95b",
  "isSidechain": false,
  "promptId": "15e99bee-64bb-4bc0-b559-9e40ffdfc882",
  "type": "user",
  "uuid": "5458cafc-b76b-4be1-ac10-5c7b646d6a0b",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/method.tex",
      "content": "\\section{Method}\n\\label{sec:method}\n\nLet $p$ denote a candidate patch and $T = \\{t_1, \\ldots, t_n\\}$ its test suite, where each $t_i$ has label $y_i \\in \\{\\text{\\textsc{Pass}}, \\text{\\textsc{Fail}}\\}$ from execution. Tests decompose into \\emph{fail-to-pass} ($T_{\\text{f2p}}$) and \\emph{pass-to-pass} ($T_{\\text{p2p}}$) subsets; a patch is correct iff $\\forall\\, t_i{:}\\ y_i = \\text{\\textsc{Pass}}$. We compare three formulations for predicting correctness without execution.\n\n\\subsection{Verification Formulations}\n\\label{sec:formulations}\n\nLet $c_p$ denote the code context (unified diff) of patch $p$.\n\n\\paragraph{\\cls{} (per-test classification).} $f(c_p, t_i) \\rightarrow \\hat{y}_i \\in \\{\\text{\\textsc{Pass}}, \\text{\\textsc{Fail}}\\}$ predicts a single binary token per test (cross-entropy loss). Patch verdict: $\\hat{y}_p = \\bigwedge_{i} [\\hat{y}_i = \\text{\\textsc{Pass}}]$. Output cost: one token per test.\n\n\\paragraph{\\cwm{} (output generation).}\\footnote{We use ``code world model'' following \\citet{meta2025cwm} to denote execution output prediction, distinct from world models in model-based reinforcement learning.} $g(c_p, t_i) \\rightarrow \\hat{o}_i \\in \\Sigma^*$ generates the execution output string (language modeling loss). Verdict by exact match: $\\hat{y}_i = \\text{\\textsc{Pass}}$ iff $\\hat{o}_i = o_i^*$.\\footnote{Exact string matching is conservative, consistent with \\citet{meta2025cwm}. Semantic equivalences are not counted.} When the generated output is unparseable (i.e., does not conform to the expected structured format), the prediction defaults to the majority class verdict. Output cost: $\\sum_i |\\hat{o}_i|$ tokens.\n\n\\paragraph{\\traj{} (trajectory-level).} $h(c_p, T) \\rightarrow \\hat{y}_p \\in \\{\\text{\\textsc{Resolved}}, \\text{\\textsc{Unresolved}}\\}$ predicts a single patch verdict from all tests and provides no per-test signal. \\traj{} serves as a granularity control: \\cls{}--\\traj{} differences isolate the value of per-test decomposition independent of the classification formulation itself.\n\n\\subsection{Expected Failure Modes}\n\\label{sec:failure-modes}\n\nEach formulation has characteristic failure modes that differ in their sensitivity to code complexity:\n\n\\paragraph{Generation failure modes (\\cwm{}).} The open-ended output space introduces three failure modes: (1)~\\emph{token-budget exhaustion}, where $|o_i^*| > B$ guarantees exact-match failure due to truncation; (2)~\\emph{string-value prediction errors}, where semantically equivalent outputs differing in surface form (floating-point precision, dictionary ordering) produce false negatives; and (3)~\\emph{format compliance collapse}, where the model fails to produce structured predictions entirely at high input complexity, even when the generation budget is sufficient. Under optimistic independence, a token sequence of length $L$ with per-token accuracy $q$ has correct-sequence probability $q^L$; long outputs are therefore exponentially harder to predict exactly. We adopt exact string matching following the original \\cwm{} evaluation protocol~\\citep{meta2025cwm}. Unparseable predictions default to the majority-class label (\\textsc{Pass}).\n\n\\paragraph{Classification failure modes (\\cls{}).} The single-token output space eliminates format and truncation failures but constrains the model to encode its reasoning entirely within internal representations, without the intermediate reasoning trace that generation provides. \\cls{} errors manifest as false positives or false negatives without format failures; at function level, a mild FP bias (56.5\\%) emerges, with the error direction depending on class distribution and fine-tuning dynamics.\n\n\\paragraph{Trajectory-level failure modes (\\traj{}).} By collapsing all per-test information into a single binary verdict, \\traj{} discards diagnostic granularity. When a patch fails multiple tests, the trajectory-level formulation cannot identify \\emph{which} tests fail. This limits downstream utility (e.g., targeted re-repair) but avoids per-test aggregation errors.\n\n\\paragraph{Complexity dependence.} These failure modes suggest a complexity-dependent interaction: when execution outputs are short and structured (function-level code), generation modes (1)--(2) are rarely triggered, and all formulations should perform comparably. As output length and structural complexity increase (repository-level code), generation-specific failures may compound, creating divergence. Whether this divergence reflects a fundamental property of the generation formulation or is contingent on model/tokenizer properties is an empirical question we investigate in \\S\\ref{sec:experiments}.\n\n\\subsection{Oracle Accuracy-Utility Framework}\n\\label{sec:oracle}\n\nFor a buggy patch with $k = |T_{\\text{f2p}}|$ fail-to-pass tests, a per-test verifier with recall $r$ detects the bug if it identifies at least one failing test: $P_{\\text{detect}}(k) = 1 - (1 - r)^{k_{\\text{eff}}}$, where $k_{\\text{eff}} = k / (1 + (k-1)\\rho)$ accounts for within-patch correlation via ICC $\\rho$~\\citep{shrout1979icc}. The per-test advantage over a trajectory-level baseline ($a_h$) is $\\Delta(k) = P_{\\text{detect}}(k) - a_h$, with population expectation $\\mathbb{E}[\\Delta] = \\sum_{k} P(|T_{\\text{f2p}}| = k) \\cdot \\Delta(k)$. This predicts that per-test advantage concentrates in multi-F2P-test instances and vanishes at $k{=}1$, validated in \\S\\ref{sec:experiments} and Appendix~\\ref{app:oracle}.\n",
      "numLines": 34,
      "startLine": 1,
      "totalLines": 34
    }
  },
  "sourceToolAssistantUUID": "b3ffea19-559e-4e51-9a28-4ddeb592e95b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/paper_audit_content_8033e618",
  "sessionId": "d10eba16-884c-49dd-bd31-5cc0ef3bc131",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-25T07:52:03.112Z_

<details open><summary>🔧 Tool call — Read · `toolu_01CCNc6jafTgHFys96Rg9hc6`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5458cafc-b76b-4be1-ac10-5c7b646d6a0b",
  "isSidechain": false,
  "requestId": "req_011CbNvXNj3MMNLN5yzjvaJH",
  "type": "assistant",
  "uuid": "f75a1110-a243-480e-9f31-0ff9c7eaa02f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/paper_audit_content_8033e618",
  "sessionId": "d10eba16-884c-49dd-bd31-5cc0ef3bc131",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RzegdawgqtJMotASk4zb6m",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11924,
      "cache_read_input_tokens": 39764,
      "output_tokens": 725,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11924,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 725,
          "cache_read_input_tokens": 39764,
          "cache_creation_input_tokens": 11924,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11924
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

_source line 31 · 2026-05-25T07:52:03.123Z_

<details><summary>↩ Tool result · `toolu_01CCNc6jafTgHFys96Rg9hc6`</summary>

```text
1	\section{Experiments}
2	\label{sec:experiments}
3	
4	We systematically compare \cls{}, \cwm{}, and \traj{} across two representative code LLM families, two complexity levels, and multiple seeds to characterize the formulation landscape for neural code verification.
5	
6	\subsection{Experimental Setup}
7	\label{sec:setup}
8	
9	\paragraph{Datasets.}
10	\emph{Function-level}: mutated variants from HumanEval~\cite{chen2021humaneval} and MBPP~\cite{austin2021mbpp} (five mutation types), labels verified by execution. 19,076 samples (train 15,290 / val 1,896 / test 1,890; pass:fail $\approx$ 52:48, majority baseline 51.75\%).
11	\emph{Repo-level}: per-test instances from SWE-bench Verified~\cite{chowdhury2024swebenchverified} mutants. ${\sim}$70K training samples; val ($n{=}9{,}335$) and test ($n{=}9{,}784$) have zero problem overlap (majority baseline 72.96\%). Val-based checkpoint selection follows standard practice~\cite{jimenez2024swebench}; runs with NaN validation loss (due to truncated targets exceeding 2,048-token limits) default to the final epoch checkpoint (Appendix~\ref{app:hyperparams}). Qwen3 \cwm{} runs show early overfitting (best at ${\sim}$6\% of training); checkpoint details in Appendix~\ref{app:hyperparams}.
12	
13	\paragraph{Models and training.}
14	We fine-tune Qwen3-4B and Qwen3-8B~\cite{qwen2025qwen3} with Low-Rank Adaptation (LoRA)~\cite{hu2022lora} (rank 16, 3 epochs) across five seeds. Seeds 42/123/456 use bfloat16; seeds 789/0 use NormalFloat 4-bit (NF4) quantization~\cite{dettmers2024qlora} to test robustness to precision reduction (function-level accuracy remains within seed noise across both precisions; see footnote in \S\ref{sec:equivalence}). As a cross-model consistency check, we additionally fine-tune DeepSeek-Coder-6.7B~\cite{guo2024deepseekcoder} with identical LoRA configuration (2 seeds each for \cls{} and \cwm{}). Our \cwm{} baseline is a LoRA fine-tuned variant for matched comparison, not a reproduction of the 32B Code World Model~\cite{meta2025cwm}. \traj{} uses variant-level rather than per-test labels (8,052 vs.\ 15,290 training instances, but covering $2.24\times$ more unique code variants); the comparison is confounded by both label granularity and data composition (\S\ref{sec:repo}). Repo-level models use val-selected checkpoints where available; runs with NaN validation loss use the final epoch checkpoint (Appendix~\ref{app:hyperparams}). Zero-shot baselines use Qwen3-8B and Qwen3-32B (NF4) as LLM-as-judge. Full hyperparameter details appear in Appendix~\ref{app:hyperparams}; prompt templates in Appendix~\ref{app:prompts}.\footnote{Code and data: \url{https://github.com/anonymous-nlp-2026-2/exec-sim-repair-verifier}}
15	
16	\paragraph{Statistics.}
17	TOST equivalence testing is our primary inferential framework for function-level claims; clustered bootstrap provides confidence intervals, Bayesian Region of Practical Equivalence (ROPE) serves as a robustness check, and mixed-effects regression tests the formulation$\times$complexity interaction. Confidence intervals use clustered bootstrap~\cite{davison1997bootstrap} (114 problem clusters, 10K resamples; we resample entire problems, not individual tests, to preserve within-problem correlations). Equivalence uses Two One-Sided Tests (TOST)~\cite{schuirmann1987tost} with $\pm$2 percentage point (\pp{}) margin; for function-level TOST, we use seed-level paired analysis (df${=}$4 for 5-seed comparisons, df${=}$2 for 3-seed), treating each training seed as the unit of replication. This is more conservative than problem-level clustered bootstrap, which pools within-seed observations and may understate between-seed uncertainty. Holm-Bonferroni correction~\cite{holm1979} controls family-wise error rate across the five primary comparisons (Table~\ref{tab:holm}). Intraclass correlation coefficient (ICC)~\cite{shrout1979icc} quantifies within-problem correlation. Variant-level effect sizes and statistical power analysis are reported in Appendix~\ref{app:power}. Oracle analysis uses SWE-bench Verified (500 instances).
18	
19	
20	\subsection{Function-Level Results}
21	\label{sec:func_results}
22	
23	Table~\ref{tab:main_results} reports function-level results across formulations and model families.
24	
25	\begin{table}[t]
26	\centering
27	\small
28	\caption{Function-level per-test accuracy on HumanEval+MBPP ($n{=}1{,}890$). Mean $\pm$ std over 5 seeds (Qwen3) or 2 seeds (DeepSeek). Seeds 42/123/456: bfloat16; 789/0: NF4. DeepSeek: $n{=}2$ seeds; std reported for descriptive comparison, not inferential. \traj{}\textsuperscript{$\star$} evaluated on 1,032-sample subset (447 matched variants). All prompting baselines use NF4 4-bit quantization. \textsuperscript{$\star$}Training configuration differs (\S\ref{sec:repo}).}
29	\label{tab:main_results}
30	\resizebox{\columnwidth}{!}{%
31	\setlength{\tabcolsep}{4pt}
32	\begin{tabular}{llcc}
33	\toprule
34	\textbf{Method} & \textbf{Model} & \textbf{Seeds} & \textbf{Accuracy (\%)} \\
35	\midrule
36	\multicolumn{4}{l}{\emph{Qwen3 (primary)}} \\
37	\cls{} (fine-tuned) & 4B & 5 & \textbf{88.43 $\pm$ 0.78} \\
38	\cwm{} (fine-tuned) & 4B & 5 & \underline{87.19 $\pm$ 0.37} \\
39	\traj{}\textsuperscript{$\star$} (fine-tuned) & 4B & 5 & 86.30 $\pm$ 0.97 \\
40	\midrule
41	\multicolumn{4}{l}{\emph{DeepSeek-Coder (cross-model consistency check)}} \\
42	\cls{} (fine-tuned) & 6.7B & 2 & \textbf{86.85 $\pm$ 0.11} \\
43	\cwm{} (fine-tuned) & 6.7B & 2 & \underline{86.83 $\pm$ 1.49} \\
44	\traj{}\textsuperscript{$\star$} (fine-tuned) & 6.7B & 2 & 84.16 $\pm$ 1.30 \\
45	\midrule
46	\multicolumn{4}{l}{\emph{Prompting baselines}} \\
47	0-shot & 8B (Qwen3) & 1 & 60.53 \\
48	0-shot & 14B (Qwen3) & 1 & 66.24 \\
49	0-shot & 6.7B (DeepSeek) & 1 & 63.02 \\
50	ZS LLM-as-judge & 8B (Qwen3) & 1 & 64.40 \\
51	ZS LLM-as-judge & 6.7B (DeepSeek) & 1 & 56.56 \\
52	ZS LLM-as-judge & 32B (NF4) & 1 & 71.69 \\
53	3-shot ICL & 8B (Qwen3) & 1 & 60.42 \\
54	3-shot ICL & 14B (Qwen3) & 1 & 73.12 \\
55	3-shot ICL & 6.7B (DeepSeek) & 1 & 59.95 \\
56	\midrule
57	Majority (pass) & --- & --- & 51.75 \\
58	\bottomrule
59	\end{tabular}}
60	\end{table}
61	
62	All three formulations achieve comparable accuracy on Qwen3-4B: \cls{} 88.43\% ($\pm$0.78), \cwm{} 87.19\% ($\pm$0.37), \traj{} 86.30\% ($\pm$0.97). DeepSeek-Coder-6.7B shows: \cls{} 86.85\%, \cwm{} 86.83\%, \traj{} 84.16\%. The \cls{}--\cwm{} gap (0.02--1.24\pp{}) is within seed noise in both families. However, the \cls{}--\traj{} per-test gap is 2.13\pp{} on Qwen3-4B and 2.69\pp{} on DeepSeek-Coder; the latter clearly exceeds the $\pm$2\pp{} equivalence margin (\S\ref{sec:equivalence}). \cls{} and \cwm{} are robustly equivalent; \traj{} parity is model-contingent. Zero-shot baselines (Tables~\ref{tab:main_results} and~\ref{tab:repo_level}) establish that repo-level verification requires fine-tuning (0-shot$\to$fine-tuned gains of 35--36\pp{}) and that formulation choice matters only at repo level (\cls{} outperforms \cwm{} by 18--26\pp{}).
63	
64	
65	\subsection{Scaling Behavior}
66	\label{sec:scaling}
67	
68	Beyond overall accuracy, we examine whether formulation ranking is stable across model sizes. Table~\ref{tab:scaling} compares all three formulations at 4B, 8B, and 14B. The 4B and 8B rows use seeds 42 and 123; the 14B row uses seeds 42, 123, and 456. All rows use bfloat16 inference.
69	
70	\begin{figure}[t]
71	\centering
72	\includegraphics[width=\columnwidth]{figures/paper/figure2_v3.pdf}
73	\caption{Function-level accuracy scaling (4B--14B). CLS and CWM accuracy with shaded gap region; $y$-axis does not start at zero. The \cls{}--\cwm{} gap shows a non-monotonic pattern: 1.32\pp{} at 4B, widening to 2.62\pp{} at 8B, then narrowing to 0.43\pp{} at 14B (3 seeds).}
74	\label{fig:scaling_gap}
75	\end{figure}
76	
77	\begin{table}[t]
78	\centering
79	\small
80	\caption{Model-size scaling: accuracy (\%) at 4B, 8B, and 14B (Qwen3). Seeds 42/123 (4B/8B), seeds 42/123/456 (14B). All bfloat16 inference. $\Delta$: change from previous size. \cwm{} and \traj{}\textsuperscript{$\star$} use $n{=}2$ seeds (4B/8B) and $n{=}3$ seeds (14B). \traj{}\textsuperscript{$\star$} evaluated on 1{,}032-sample subset; \cls{}/\cwm{} use the full 1{,}890-sample set. \textsuperscript{$\star$}Training configuration differs (\S\ref{sec:repo}).}
81	\label{tab:scaling}
82	\setlength{\tabcolsep}{3pt}
83	\begin{tabular}{llccccc}
84	\toprule
85	\textbf{Method} & \textbf{Size} & \textbf{s42} & \textbf{s123} & \textbf{s456} & \textbf{Mean} & \textbf{$\Delta$} \\
86	\midrule
87	\multirow{3}{*}{\cls{}} & 4B & 87.83 & 89.52 & --- & \textbf{88.68} & --- \\
88	 & 8B & \textbf{90.48} & 89.40 & --- & \textbf{89.94} & +1.27 \\
89	 & 14B & 89.21 & \textbf{90.79} & 89.79 & \textbf{89.93 $\pm$ 0.80} & $-$0.01 \\
90	\midrule
91	\multirow{3}{*}{\cwm{}} & 4B & 87.51 & 87.20 & --- & \underline{87.36} & --- \\
92	 & 8B & 87.67 & 86.98 & --- & 87.33 & $-$0.03 \\
93	 & 14B & 89.26 & 88.99 & 90.26 & \underline{89.50 $\pm$ 0.67} & +2.17 \\
94	\midrule
95	\multirow{3}{*}{\traj{}} & 4B & 85.66 & 85.47 & --- & 85.57 & --- \\
96	 & 8B & 87.60 & 87.79 & --- & \underline{87.70} & +2.13 \\
97	 & 14B & 89.73 & 88.57 & 88.28 & 88.86 $\pm$ 0.77 & +1.16 \\
98	\bottomrule
99	\end{tabular}
100	\end{table}
101	
102	\cls{} and \traj{} both scale positively from 4B to 8B (+1.27\pp{} and +2.13\pp{} respectively), while \cwm{} remains flat ($-$0.03\pp{}). At 8B, the ranking is \cls{} (89.94) $>$ \traj{} (87.70) $>$ \cwm{} (87.33). The \cls{}--\cwm{} gap widens from 1.32\pp{} at 4B to 2.62\pp{} at 8B (Figure~\ref{fig:scaling_gap}); clustered bootstrap on the 3-seed superset (42, 123, 456 for \cls{}/\cwm{}) yields $p = 0.0066$ (95\% CI $[1.80, 2.71]$), which confirms the widening is not a sampling artifact.
103	
104	At 14B (3 seeds), all three formulations converge in point estimates: \cls{} 89.93$\pm$0.80\%, \cwm{} 89.50$\pm$0.67\%, \traj{} 88.86$\pm$0.77\%. The maximum pairwise gap (\cls{}--\traj{}) narrows from 3.11\pp{} at 4B to 1.07\pp{} at 14B, within the $\pm$2\pp{} equivalence margin. Seed-level TOST (df${=}$2) is inconclusive for equivalence in both pairs ($p{=}0.076$ for \cls{}--\cwm{}, $p{=}0.187$ for \cls{}--\traj{}), reflecting the low power inherent in 3-seed comparisons; Bayesian ROPE provides moderate support ($P(\text{ROPE}){=}0.887$ and $0.780$ respectively; Appendix~\ref{app:bayesian_rope}). \cwm{}'s delayed scaling onset (flat from 4B to 8B, then +2.17\pp{} at 14B) and \traj{}'s decelerating convergence (+2.13\pp{} at 8B, +1.16\pp{} at 14B) are both consistent with capacity-dependent convergence at function level.
105	
106	\paragraph{Baseline scaling.} Prompting baselines remain well below fine-tuning: the best result (14B 3-shot, 73.12\%) is 16.82\pp{} below fine-tuned \cls{} at 8B. Only \cls{} scales positively across both complexity levels; \traj{} shows no repo-level scaling benefit (72.92\% at both 4B and 8B).
107	
108	
109	\subsection{Function-Level Equivalence}
110	\label{sec:equivalence}
111	
112	We test pairwise equivalence on 523 variant-level instances across five seeds.\footnote{Seeds 789/0 use NF4 inference; the remaining three use bfloat16. Restricting to bfloat16 only: \cls{}--\cwm{} remains significant ($p{<}0.05$); \cls{}--\traj{} yields $p{=}0.128$.} Our Smallest Effect Size of Interest (SESOI) threshold of $\pm$2\pp{}~\cite{lakens2017,wellek2010} is domain-motivated but not pre-registered: at 85--88\% accuracy, 2\pp{} corresponds to ${\sim}$2--3 problems out of 114, below practitioner-relevant differences, and is consistent with between-seed variation (0.37--0.97\pp{} std). Within-problem predictions are correlated (ICC $= 0.191$, design effect [DEFF] $= 3.97$~\cite{moulton1990}); confidence intervals use clustered bootstrap (\S\ref{sec:setup}). Sensitivity analysis shows \cls{}--\cwm{} equivalence is robust across $\pm$1.5--3\pp{} margins (minimum $\pm$1.52\pp{}); \cls{}--\traj{} equivalence is margin-sensitive ($\pm$1.5\pp{}: $p{=}0.068$; Table~\ref{tab:tost_sensitivity}).
113	
114	\paragraph{\cls{}--\cwm{} equivalence.} The pooled gap is 1.24\pp{} (88.43\%--87.19\%); TOST confirms equivalence at $p = 0.007$ ($\pm$2\pp{} margin), surviving Holm-Bonferroni correction ($k{=}5$, adjusted $p{=}0.028$; Table~\ref{tab:holm}). Equivalence holds at margins as tight as $\pm$1.52\pp{} (Table~\ref{tab:tost_sensitivity}). On DeepSeek-Coder, the \cls{}--\cwm{} gap of 0.02\pp{} is consistent with equivalence but underpowered (2 seeds).
115	
116	\paragraph{\cls{}--\traj{} equivalence.} The pooled gap is $-$0.45\pp{} (95\% CI [$-$1.71, +0.84]); TOST yields $p = 0.025$ ($\pm$2\pp{}), nominally significant but not surviving Holm-Bonferroni correction ($k{=}5$, adjusted $p{=}0.075$; Table~\ref{tab:holm}). The DeepSeek \cls{}--\traj{} gap (2.69\pp{}) exceeds the $\pm$2\pp{} margin; \traj{} parity is model-dependent. This holds under different training recipes (data volume and label granularity; \S\ref{sec:repo}). Per-test classification provides diagnostic information at no accuracy cost, paralleling process supervision~\cite{lightman2023letsverify}.
117	
118	\paragraph{Statistical power.} With $n_{\text{eff}} \approx 86$ after clustering, TOST power is ${\sim}$0.3~\cite{cohen1988}, a 70\% probability of failing to confirm equivalence even if the true difference is moderate. The \cls{}--\cwm{} equivalence ($p{=}0.007$) is robust to this limitation; the \cls{}--\traj{} inconclusive result ($p{=}0.025$, adjusted $p{=}0.075$) may reflect insufficient power rather than a genuine difference (a minimum $n_{\text{eff}} \approx 350$ would be needed for ${\geq}$0.8 power at $\pm$2\pp{}). A Bayesian ROPE analysis corroborates: $P(\text{ROPE}){=}0.975$ for \cls{}--\cwm{} and $P(\text{ROPE}){=}0.970$ at variant level for \cls{}--\traj{} (Appendix~\ref{app:bayesian_rope}). At per-test level, \cls{}--\traj{} $P(\text{ROPE}){=}0.542$ (inconclusive), reflecting aggregation effects. 14B scaling data corroborates: the \cls{}--\traj{} gap narrows to 1.07\pp{} (\S\ref{sec:scaling}).
119	
120	
121	\subsection{Repo-Level: Complexity-Dependent Divergence}
122	\label{sec:repo}
123	
124	Table~\ref{tab:repo_level} compares formulations at repository-level complexity. The following results are established under ${\leq}$8B LoRA; preliminary 14B evidence (\S\ref{sec:scaling}) suggests these gaps may narrow at larger scales. Variant-level comparisons ($n{=}48$) are exploratory due to limited seed coverage; the per-test interaction effect is statistically confirmed (see below). Checkpoints are val-selected where validation loss is computable (\S\ref{sec:setup}); the test set has zero problem overlap with validation.
125	
126	\begin{table}[t]
127	\centering
128	\small
129	\caption{Repo-level cross-formulation comparison on SWE-bench Verified test set. Qwen3-8B \cls{}/\traj{}: mean $\pm$ std over 3 seeds; DeepSeek \cls{}: 2 seeds\textsuperscript{$\ddagger$}; DeepSeek \traj{}: 3 seeds; Qwen3-4B: seed 42. \cwm{}: 3 seeds (42/123/456).}
130	\label{tab:repo_level}
131	\resizebox{\columnwidth}{!}{%
132	\setlength{\tabcolsep}{4pt}
133	\begin{tabular}{lcccc}
134	\toprule
135	\textbf{Model} & \textbf{\cls{} (\%)} & \textbf{\cls{} Var.\ (\%)} & \textbf{\cwm{} (\%)} & \textbf{\traj{} Var.\ (\%)\textsuperscript{$\diamond$}} \\
136	\midrule
137	Qwen3-4B & 83.63 & 64.58 & 58.04 & 72.92 \\
138	Qwen3-8B & \textbf{84.83 $\pm$ 0.67} & 72.92 / 81.25\textsuperscript{$\dagger$} & 66.48 $\pm$ 1.15 & 72.91 $\pm$ 3.61 \\
139	DeepSeek-6.7B & 84.38 $\pm$ 2.50\textsuperscript{$\ddagger$} & 81.25\textsuperscript{$\dagger$} & 58.30 $\pm$ 2.82 & 77.08 $\pm$ 3.61 \\
140	\midrule
141	0-shot (Qwen3-8B) & 49.90 & --- & --- & --- \\
142	0-shot (DeepSeek) & 48.54 & --- & --- & --- \\
143	Majority & 72.96 & 54.17 & 72.96 & 54.17 \\
144	\bottomrule
145	\end{tabular}}
146	
147	\vspace{2pt}
148	{\footnotesize \textsuperscript{$\dagger$}Individual-seed variant accuracy. \textsuperscript{$\ddagger$}One seed excluded: truncate preprocessing$\to$NaN val loss, decision collapse (Table~\ref{tab:taxonomy}); mean over two matched seeds. \textsuperscript{$\diamond$}Var.\ columns: variant-level accuracy ($n{=}48$); \cls{} aggregated via all-pass rule; \traj{} by design. Per-test: $n{=}9{,}784$. \cwm{} unparseable: 54\% (4B); default to pass; parseable-only 38--43\%, below majority. Eval seq\_length differs across models (Appendix~\ref{app:threats}). \cwm{} uses final-epoch checkpoint (step 6633) for s123/s456; s42 uses an earlier checkpoint (step 400) from a prior training configuration. Val loss is undefined for DeepSeek \cwm{} runs (Qwen3 \cwm{} has valid val loss; see \S\ref{sec:setup}). Checkpoint sensitivity analysis in Appendix~\ref{app:cwm_convergence}.}
149	\end{table}
150	
151	Few-shot prompting (3-shot ICL) collapses to an always-predict-unresolved baseline (variant accuracy 45.83\%, below majority 54.17\%; Appendix~\ref{app:few_shot}), establishing that execution-free verification requires task-specific fine-tuning regardless of formulation. The fine-tuning requirement (35--36\pp{} gains, Table~\ref{tab:repo_level}) is the first layer of our three-layer structure.
152	
153	\paragraph{Formulation divergence.} Under our 4--8B LoRA protocol, \cls{} and \cwm{} diverge: the gap is 25.59\pp{} at 4B and 18.35\pp{} at 8B (Table~\ref{tab:repo_level}), with \cwm{} falling below majority baseline at both scales. Limited seed coverage and multiple confounds (\S\ref{sec:threats}) limit causal attribution.
154	
155	\paragraph{Cross-model consistency.} DeepSeek-Coder shows the same direction (\cls{} $>$ \cwm{}) across all seeds; gap variation across families (20\pp{} Qwen3 vs.\ 23--28\pp{} DeepSeek) narrows to ${\sim}$2\pp{} under matched checkpoints (Appendix~\ref{app:threats}). All six \cwm{} repo-level seeds exhibit format collapse ($>$50\% unparseable), ruling out seed-specific artifacts.
156	
157	\paragraph{Failure mode taxonomy.} Variant-level analysis ($n{=}48$) identifies three failure modes (Table~\ref{tab:taxonomy}; full variant-level and per-mutation breakdowns in Appendices~\ref{app:variant_level} and~\ref{app:repo_mutation}): format collapse (\cwm{}, 51--74\% unparseable), decision collapse (\cls{} under truncate preprocessing, fail recall ${\sim}$14\%), and aggregation penalty (\cls{} under drop preprocessing, fail recall 38--57\%). Decision collapse is configuration-dependent, not model-inherent. \traj{} avoids aggregation penalty by predicting variant outcomes directly (72.91--77.08\%). Downsampling \cls{} to match \traj{}'s data volume still yields 80.74\% (+7.82\pp{} above \traj{}; Appendix~\ref{app:downsample}). The CLS--TRAJ repo-level comparison remains exploratory: downsample ablation controls data volume but not label granularity (per-test vs.\ variant-level), a formulation-inherent confound that cannot be experimentally resolved.
158	
159	\begin{table}[t]
160	\centering
161	\small
162	\caption{Repo-level failure mode taxonomy. Variant-level majority baseline: 54.17\%.}
163	\label{tab:taxonomy}
164	\setlength{\tabcolsep}{3pt}
165	\resizebox{\columnwidth}{!}{%
166	\begin{tabular}{llcc}
167	\toprule
168	\textbf{Failure Mode} & \textbf{Representative} & \textbf{Fail Recall} & \textbf{Variant Acc} \\
169	\midrule
170	Format collapse & \cwm{} (all) & N/A & 48--52\% \\
171	Decision collapse & \cls{} (DeepSeek, s123) & ${\sim}$14\% & 56\% \\
172	Aggr.\ penalty & \cls{} (Qwen3-8B) & 51--57\% & 73--81\% \\
173	Aggr.\ penalty & \cls{} (DeepSeek, s42) & 38--51\% & 79--81\% \\
174	\bottomrule
175	\end{tabular}}
176	\end{table}
177	
178	\paragraph{Default assignment artifact.} The apparent \cwm{} accuracy increase from 4B to 8B is an artifact of rising unparseable rate (53.7\%$\to$73.8\%), inflating accuracy via majority-class default while parseable-only accuracy decreases (42.88\%$\to$38.52\%); cross-seed evidence confirms the pattern (Appendix~\ref{app:parseable_bias}).
179	
180	\paragraph{Complexity as moderator.} The \cls{}--\cwm{} gap widens from 1--3\pp{} (function) to 18--26\pp{} (repo) under our protocol; a matched-context ablation confirms input disparity explains $<$3\% of this gap (Appendix~\ref{app:ablations}). While the directional advantage of lower-complexity output formulations may be anticipated from \S\ref{sec:failure-modes}, the magnitude of this gap, the function-level equivalence, and the specific failure mechanisms (Table~\ref{tab:taxonomy}) were not predictable a priori.
181	
182	\paragraph{Formulation$\times$complexity interaction.} A mixed-effects linear probability model (LPM) ($n{=}56{,}480$, 139 clusters, DeepSeek-Coder) confirms: \cwm{} effect at function level is negligible ($\hat{\beta}{=}-0.002$, $p{=}0.805$), but the formulation$\times$complexity interaction is highly significant ($z{=}-23.7$, $p{<}0.001$). A cross-model LPM confirms formulation dominates ($\hat{\beta}{=}-0.22$ vs.\ model $\hat{\beta}{=}+0.011$); model identity significance is estimator-dependent (LPM $p{=}0.002$; generalized estimating equations [GEE] $p{=}0.449$), consistent with limited clusters ($k{=}25 < 40$; Appendix~\ref{app:interaction}).
183	
184	\subsection{Analysis}
185	\label{sec:analysis}
186	
187	\paragraph{Aggregation penalty.} The aggregation penalty ranges from 1.36\pp{} to 19\pp{}, negligible at function level ($\bar{T} \approx 2.3$) but substantial at repo level ($\bar{T} \gg 10$; Appendix~\ref{app:extended_analysis}(a)).
188	
189	\paragraph{Why does generation degrade at repo level?} Output complexity increases nonlinearly: function-level outputs average ${\sim}$5--15 tokens; repo-level outputs average ${\sim}$477 tokens, leading to format collapse under our ${\leq}$8B LoRA protocol (53--74\% unparseable; representative error examples in Appendix~\ref{app:qualitative}). Even parseable outputs achieve only 38--43\%, below majority; a model accidentally trained on CLS-format data achieves 86.05\% with 0\% unparseable, confirming the degradation stems from output format complexity, not task difficulty (Appendix~\ref{app:extended_analysis}(c)). Four targeted interventions (doubling LoRA rank, majority voting [$k{=}5$], relaxed matching, and scaling to 8B) all fail to close this gap (Appendix~\ref{app:extended_analysis}(g)); checkpoint selection explains $<$1\pp{} (Appendix~\ref{app:cwm_convergence}). \cls{} achieves 217$\times$ higher throughput (1 vs.\ avg 477 output tokens; Appendix~\ref{app:extended_analysis}(i)).
190	
191	\paragraph{Error complementarity.} \cls{} and \cwm{} exhibit partially complementary errors, suggesting potential complementarity for routing. An oracle combination achieves 90.63\% (+2.80\pp{}; 95\% CI [89.3\%, 91.9\%]; single-seed) at function level and 95.83\% (+14.58\pp{}; $n{=}48$) at repo level. Simple routing heuristics capture $<$0.4\pp{} of the oracle gap; the complementarity is instance-specific, suggesting that simple heuristics are insufficient; whether a learned router can capture this advantage remains open (Appendix~\ref{app:oracle}).
192	
193	\subsection{Threats to Validity}
194	\label{sec:threats}
195	
196	We identify five potential confounds (Appendix~\ref{app:threats}): checkpoint selection ($<$1\pp{}), evaluation sequence length (${\sim}$1.5\pp{}), preprocessing (${\sim}$8\pp{}; val-test distribution shift in Appendix~\ref{app:mutation_distribution}), \traj{} training regime, and \cwm{} scale/pretraining (primary limitation). Preprocessing and checkpoint interact, accounting for up to 7.68\pp{} variation within one model (Appendix~\ref{app:threats}). The 18--26\pp{} gap exceeds any single confound, but correlated confounds and limited seeds preclude definitive causal attribution. Holm-Bonferroni ($k{=}5$) confirms the two core claims (adjusted $p{=}0.015$ and $p{=}0.028$; Table~\ref{tab:holm}).
197	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f75a1110-a243-480e-9f31-0ff9c7eaa02f",
  "isSidechain": false,
  "promptId": "15e99bee-64bb-4bc0-b559-9e40ffdfc882",
  "type": "user",
  "uuid": "07c70d00-5639-474f-8fbe-6a24224b01f3",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/experiments.tex",
      "content": "\\section{Experiments}\n\\label{sec:experiments}\n\nWe systematically compare \\cls{}, \\cwm{}, and \\traj{} across two representative code LLM families, two complexity levels, and multiple seeds to characterize the formulation landscape for neural code verification.\n\n\\subsection{Experimental Setup}\n\\label{sec:setup}\n\n\\paragraph{Datasets.}\n\\emph{Function-level}: mutated variants from HumanEval~\\cite{chen2021humaneval} and MBPP~\\cite{austin2021mbpp} (five mutation types), labels verified by execution. 19,076 samples (train 15,290 / val 1,896 / test 1,890; pass:fail $\\approx$ 52:48, majority baseline 51.75\\%).\n\\emph{Repo-level}: per-test instances from SWE-bench Verified~\\cite{chowdhury2024swebenchverified} mutants. ${\\sim}$70K training samples; val ($n{=}9{,}335$) and test ($n{=}9{,}784$) have zero problem overlap (majority baseline 72.96\\%). Val-based checkpoint selection follows standard practice~\\cite{jimenez2024swebench}; runs with NaN validation loss (due to truncated targets exceeding 2,048-token limits) default to the final epoch checkpoint (Appendix~\\ref{app:hyperparams}). Qwen3 \\cwm{} runs show early overfitting (best at ${\\sim}$6\\% of training); checkpoint details in Appendix~\\ref{app:hyperparams}.\n\n\\paragraph{Models and training.}\nWe fine-tune Qwen3-4B and Qwen3-8B~\\cite{qwen2025qwen3} with Low-Rank Adaptation (LoRA)~\\cite{hu2022lora} (rank 16, 3 epochs) across five seeds. Seeds 42/123/456 use bfloat16; seeds 789/0 use NormalFloat 4-bit (NF4) quantization~\\cite{dettmers2024qlora} to test robustness to precision reduction (function-level accuracy remains within seed noise across both precisions; see footnote in \\S\\ref{sec:equivalence}). As a cross-model consistency check, we additionally fine-tune DeepSeek-Coder-6.7B~\\cite{guo2024deepseekcoder} with identical LoRA configuration (2 seeds each for \\cls{} and \\cwm{}). Our \\cwm{} baseline is a LoRA fine-tuned variant for matched comparison, not a reproduction of the 32B Code World Model~\\cite{meta2025cwm}. \\traj{} uses variant-level rather than per-test labels (8,052 vs.\\ 15,290 training instances, but covering $2.24\\times$ more unique code variants); the comparison is confounded by both label granularity and data composition (\\S\\ref{sec:repo}). Repo-level models use val-selected checkpoints where available; runs with NaN validation loss use the final epoch checkpoint (Appendix~\\ref{app:hyperparams}). Zero-shot baselines use Qwen3-8B and Qwen3-32B (NF4) as LLM-as-judge. Full hyperparameter details appear in Appendix~\\ref{app:hyperparams}; prompt templates in Appendix~\\ref{app:prompts}.\\footnote{Code and data: \\url{https://github.com/anonymous-nlp-2026-2/exec-sim-repair-verifier}}\n\n\\paragraph{Statistics.}\nTOST equivalence testing is our primary inferential framework for function-level claims; clustered bootstrap provides confidence intervals, Bayesian Region of Practical Equivalence (ROPE) serves as a robustness check, and mixed-effects regression tests the formulation$\\times$complexity interaction. Confidence intervals use clustered bootstrap~\\cite{davison1997bootstrap} (114 problem clusters, 10K resamples; we resample entire problems, not individual tests, to preserve within-problem correlations). Equivalence uses Two One-Sided Tests (TOST)~\\cite{schuirmann1987tost} with $\\pm$2 percentage point (\\pp{}) margin; for function-level TOST, we use seed-level paired analysis (df${=}$4 for 5-seed comparisons, df${=}$2 for 3-seed), treating each training seed as the unit of replication. This is more conservative than problem-level clustered bootstrap, which pools within-seed observations and may understate between-seed uncertainty. Holm-Bonferroni correction~\\cite{holm1979} controls family-wise error rate across the five primary comparisons (Table~\\ref{tab:holm}). Intraclass correlation coefficient (ICC)~\\cite{shrout1979icc} quantifies within-problem correlation. Variant-level effect sizes and statistical power analysis are reported in Appendix~\\ref{app:power}. Oracle analysis uses SWE-bench Verified (500 instances).\n\n\n\\subsection{Function-Level Results}\n\\label{sec:func_results}\n\nTable~\\ref{tab:main_results} reports function-level results across formulations and model families.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Function-level per-test accuracy on HumanEval+MBPP ($n{=}1{,}890$). Mean $\\pm$ std over 5 seeds (Qwen3) or 2 seeds (DeepSeek). Seeds 42/123/456: bfloat16; 789/0: NF4. DeepSeek: $n{=}2$ seeds; std reported for descriptive comparison, not inferential. \\traj{}\\textsuperscript{$\\star$} evaluated on 1,032-sample subset (447 matched variants). All prompting baselines use NF4 4-bit quantization. \\textsuperscript{$\\star$}Training configuration differs (\\S\\ref{sec:repo}).}\n\\label{tab:main_results}\n\\resizebox{\\columnwidth}{!}{%\n\\setlength{\\tabcolsep}{4pt}\n\\begin{tabular}{llcc}\n\\toprule\n\\textbf{Method} & \\textbf{Model} & \\textbf{Seeds} & \\textbf{Accuracy (\\%)} \\\\\n\\midrule\n\\multicolumn{4}{l}{\\emph{Qwen3 (primary)}} \\\\\n\\cls{} (fine-tuned) & 4B & 5 & \\textbf{88.43 $\\pm$ 0.78} \\\\\n\\cwm{} (fine-tuned) & 4B & 5 & \\underline{87.19 $\\pm$ 0.37} \\\\\n\\traj{}\\textsuperscript{$\\star$} (fine-tuned) & 4B & 5 & 86.30 $\\pm$ 0.97 \\\\\n\\midrule\n\\multicolumn{4}{l}{\\emph{DeepSeek-Coder (cross-model consistency check)}} \\\\\n\\cls{} (fine-tuned) & 6.7B & 2 & \\textbf{86.85 $\\pm$ 0.11} \\\\\n\\cwm{} (fine-tuned) & 6.7B & 2 & \\underline{86.83 $\\pm$ 1.49} \\\\\n\\traj{}\\textsuperscript{$\\star$} (fine-tuned) & 6.7B & 2 & 84.16 $\\pm$ 1.30 \\\\\n\\midrule\n\\multicolumn{4}{l}{\\emph{Prompting baselines}} \\\\\n0-shot & 8B (Qwen3) & 1 & 60.53 \\\\\n0-shot & 14B (Qwen3) & 1 & 66.24 \\\\\n0-shot & 6.7B (DeepSeek) & 1 & 63.02 \\\\\nZS LLM-as-judge & 8B (Qwen3) & 1 & 64.40 \\\\\nZS LLM-as-judge & 6.7B (DeepSeek) & 1 & 56.56 \\\\\nZS LLM-as-judge & 32B (NF4) & 1 & 71.69 \\\\\n3-shot ICL & 8B (Qwen3) & 1 & 60.42 \\\\\n3-shot ICL & 14B (Qwen3) & 1 & 73.12 \\\\\n3-shot ICL & 6.7B (DeepSeek) & 1 & 59.95 \\\\\n\\midrule\nMajority (pass) & --- & --- & 51.75 \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\nAll three formulations achieve comparable accuracy on Qwen3-4B: \\cls{} 88.43\\% ($\\pm$0.78), \\cwm{} 87.19\\% ($\\pm$0.37), \\traj{} 86.30\\% ($\\pm$0.97). DeepSeek-Coder-6.7B shows: \\cls{} 86.85\\%, \\cwm{} 86.83\\%, \\traj{} 84.16\\%. The \\cls{}--\\cwm{} gap (0.02--1.24\\pp{}) is within seed noise in both families. However, the \\cls{}--\\traj{} per-test gap is 2.13\\pp{} on Qwen3-4B and 2.69\\pp{} on DeepSeek-Coder; the latter clearly exceeds the $\\pm$2\\pp{} equivalence margin (\\S\\ref{sec:equivalence}). \\cls{} and \\cwm{} are robustly equivalent; \\traj{} parity is model-contingent. Zero-shot baselines (Tables~\\ref{tab:main_results} and~\\ref{tab:repo_level}) establish that repo-level verification requires fine-tuning (0-shot$\\to$fine-tuned gains of 35--36\\pp{}) and that formulation choice matters only at repo level (\\cls{} outperforms \\cwm{} by 18--26\\pp{}).\n\n\n\\subsection{Scaling Behavior}\n\\label{sec:scaling}\n\nBeyond overall accuracy, we examine whether formulation ranking is stable across model sizes. Table~\\ref{tab:scaling} compares all three formulations at 4B, 8B, and 14B. The 4B and 8B rows use seeds 42 and 123; the 14B row uses seeds 42, 123, and 456. All rows use bfloat16 inference.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/paper/figure2_v3.pdf}\n\\caption{Function-level accuracy scaling (4B--14B). CLS and CWM accuracy with shaded gap region; $y$-axis does not start at zero. The \\cls{}--\\cwm{} gap shows a non-monotonic pattern: 1.32\\pp{} at 4B, widening to 2.62\\pp{} at 8B, then narrowing to 0.43\\pp{} at 14B (3 seeds).}\n\\label{fig:scaling_gap}\n\\end{figure}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Model-size scaling: accuracy (\\%) at 4B, 8B, and 14B (Qwen3). Seeds 42/123 (4B/8B), seeds 42/123/456 (14B). All bfloat16 inference. $\\Delta$: change from previous size. \\cwm{} and \\traj{}\\textsuperscript{$\\star$} use $n{=}2$ seeds (4B/8B) and $n{=}3$ seeds (14B). \\traj{}\\textsuperscript{$\\star$} evaluated on 1{,}032-sample subset; \\cls{}/\\cwm{} use the full 1{,}890-sample set. \\textsuperscript{$\\star$}Training configuration differs (\\S\\ref{sec:repo}).}\n\\label{tab:scaling}\n\\setlength{\\tabcolsep}{3pt}\n\\begin{tabular}{llccccc}\n\\toprule\n\\textbf{Method} & \\textbf{Size} & \\textbf{s42} & \\textbf{s123} & \\textbf{s456} & \\textbf{Mean} & \\textbf{$\\Delta$} \\\\\n\\midrule\n\\multirow{3}{*}{\\cls{}} & 4B & 87.83 & 89.52 & --- & \\textbf{88.68} & --- \\\\\n & 8B & \\textbf{90.48} & 89.40 & --- & \\textbf{89.94} & +1.27 \\\\\n & 14B & 89.21 & \\textbf{90.79} & 89.79 & \\textbf{89.93 $\\pm$ 0.80} & $-$0.01 \\\\\n\\midrule\n\\multirow{3}{*}{\\cwm{}} & 4B & 87.51 & 87.20 & --- & \\underline{87.36} & --- \\\\\n & 8B & 87.67 & 86.98 & --- & 87.33 & $-$0.03 \\\\\n & 14B & 89.26 & 88.99 & 90.26 & \\underline{89.50 $\\pm$ 0.67} & +2.17 \\\\\n\\midrule\n\\multirow{3}{*}{\\traj{}} & 4B & 85.66 & 85.47 & --- & 85.57 & --- \\\\\n & 8B & 87.60 & 87.79 & --- & \\underline{87.70} & +2.13 \\\\\n & 14B & 89.73 & 88.57 & 88.28 & 88.86 $\\pm$ 0.77 & +1.16 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\cls{} and \\traj{} both scale positively from 4B to 8B (+1.27\\pp{} and +2.13\\pp{} respectively), while \\cwm{} remains flat ($-$0.03\\pp{}). At 8B, the ranking is \\cls{} (89.94) $>$ \\traj{} (87.70) $>$ \\cwm{} (87.33). The \\cls{}--\\cwm{} gap widens from 1.32\\pp{} at 4B to 2.62\\pp{} at 8B (Figure~\\ref{fig:scaling_gap}); clustered bootstrap on the 3-seed superset (42, 123, 456 for \\cls{}/\\cwm{}) yields $p = 0.0066$ (95\\% CI $[1.80, 2.71]$), which confirms the widening is not a sampling artifact.\n\nAt 14B (3 seeds), all three formulations converge in point estimates: \\cls{} 89.93$\\pm$0.80\\%, \\cwm{} 89.50$\\pm$0.67\\%, \\traj{} 88.86$\\pm$0.77\\%. The maximum pairwise gap (\\cls{}--\\traj{}) narrows from 3.11\\pp{} at 4B to 1.07\\pp{} at 14B, within the $\\pm$2\\pp{} equivalence margin. Seed-level TOST (df${=}$2) is inconclusive for equivalence in both pairs ($p{=}0.076$ for \\cls{}--\\cwm{}, $p{=}0.187$ for \\cls{}--\\traj{}), reflecting the low power inherent in 3-seed comparisons; Bayesian ROPE provides moderate support ($P(\\text{ROPE}){=}0.887$ and $0.780$ respectively; Appendix~\\ref{app:bayesian_rope}). \\cwm{}'s delayed scaling onset (flat from 4B to 8B, then +2.17\\pp{} at 14B) and \\traj{}'s decelerating convergence (+2.13\\pp{} at 8B, +1.16\\pp{} at 14B) are both consistent with capacity-dependent convergence at function level.\n\n\\paragraph{Baseline scaling.} Prompting baselines remain well below fine-tuning: the best result (14B 3-shot, 73.12\\%) is 16.82\\pp{} below fine-tuned \\cls{} at 8B. Only \\cls{} scales positively across both complexity levels; \\traj{} shows no repo-level scaling benefit (72.92\\% at both 4B and 8B).\n\n\n\\subsection{Function-Level Equivalence}\n\\label{sec:equivalence}\n\nWe test pairwise equivalence on 523 variant-level instances across five seeds.\\footnote{Seeds 789/0 use NF4 inference; the remaining three use bfloat16. Restricting to bfloat16 only: \\cls{}--\\cwm{} remains significant ($p{<}0.05$); \\cls{}--\\traj{} yields $p{=}0.128$.} Our Smallest Effect Size of Interest (SESOI) threshold of $\\pm$2\\pp{}~\\cite{lakens2017,wellek2010} is domain-motivated but not pre-registered: at 85--88\\% accuracy, 2\\pp{} corresponds to ${\\sim}$2--3 problems out of 114, below practitioner-relevant differences, and is consistent with between-seed variation (0.37--0.97\\pp{} std). Within-problem predictions are correlated (ICC $= 0.191$, design effect [DEFF] $= 3.97$~\\cite{moulton1990}); confidence intervals use clustered bootstrap (\\S\\ref{sec:setup}). Sensitivity analysis shows \\cls{}--\\cwm{} equivalence is robust across $\\pm$1.5--3\\pp{} margins (minimum $\\pm$1.52\\pp{}); \\cls{}--\\traj{} equivalence is margin-sensitive ($\\pm$1.5\\pp{}: $p{=}0.068$; Table~\\ref{tab:tost_sensitivity}).\n\n\\paragraph{\\cls{}--\\cwm{} equivalence.} The pooled gap is 1.24\\pp{} (88.43\\%--87.19\\%); TOST confirms equivalence at $p = 0.007$ ($\\pm$2\\pp{} margin), surviving Holm-Bonferroni correction ($k{=}5$, adjusted $p{=}0.028$; Table~\\ref{tab:holm}). Equivalence holds at margins as tight as $\\pm$1.52\\pp{} (Table~\\ref{tab:tost_sensitivity}). On DeepSeek-Coder, the \\cls{}--\\cwm{} gap of 0.02\\pp{} is consistent with equivalence but underpowered (2 seeds).\n\n\\paragraph{\\cls{}--\\traj{} equivalence.} The pooled gap is $-$0.45\\pp{} (95\\% CI [$-$1.71, +0.84]); TOST yields $p = 0.025$ ($\\pm$2\\pp{}), nominally significant but not surviving Holm-Bonferroni correction ($k{=}5$, adjusted $p{=}0.075$; Table~\\ref{tab:holm}). The DeepSeek \\cls{}--\\traj{} gap (2.69\\pp{}) exceeds the $\\pm$2\\pp{} margin; \\traj{} parity is model-dependent. This holds under different training recipes (data volume and label granularity; \\S\\ref{sec:repo}). Per-test classification provides diagnostic information at no accuracy cost, paralleling process supervision~\\cite{lightman2023letsverify}.\n\n\\paragraph{Statistical power.} With $n_{\\text{eff}} \\approx 86$ after clustering, TOST power is ${\\sim}$0.3~\\cite{cohen1988}, a 70\\% probability of failing to confirm equivalence even if the true difference is moderate. The \\cls{}--\\cwm{} equivalence ($p{=}0.007$) is robust to this limitation; the \\cls{}--\\traj{} inconclusive result ($p{=}0.025$, adjusted $p{=}0.075$) may reflect insufficient power rather than a genuine difference (a minimum $n_{\\text{eff}} \\approx 350$ would be needed for ${\\geq}$0.8 power at $\\pm$2\\pp{}). A Bayesian ROPE analysis corroborates: $P(\\text{ROPE}){=}0.975$ for \\cls{}--\\cwm{} and $P(\\text{ROPE}){=}0.970$ at variant level for \\cls{}--\\traj{} (Appendix~\\ref{app:bayesian_rope}). At per-test level, \\cls{}--\\traj{} $P(\\text{ROPE}){=}0.542$ (inconclusive), reflecting aggregation effects. 14B scaling data corroborates: the \\cls{}--\\traj{} gap narrows to 1.07\\pp{} (\\S\\ref{sec:scaling}).\n\n\n\\subsection{Repo-Level: Complexity-Dependent Divergence}\n\\label{sec:repo}\n\nTable~\\ref{tab:repo_level} compares formulations at repository-level complexity. The following results are established under ${\\leq}$8B LoRA; preliminary 14B evidence (\\S\\ref{sec:scaling}) suggests these gaps may narrow at larger scales. Variant-level comparisons ($n{=}48$) are exploratory due to limited seed coverage; the per-test interaction effect is statistically confirmed (see below). Checkpoints are val-selected where validation loss is computable (\\S\\ref{sec:setup}); the test set has zero problem overlap with validation.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Repo-level cross-formulation comparison on SWE-bench Verified test set. Qwen3-8B \\cls{}/\\traj{}: mean $\\pm$ std over 3 seeds; DeepSeek \\cls{}: 2 seeds\\textsuperscript{$\\ddagger$}; DeepSeek \\traj{}: 3 seeds; Qwen3-4B: seed 42. \\cwm{}: 3 seeds (42/123/456).}\n\\label{tab:repo_level}\n\\resizebox{\\columnwidth}{!}{%\n\\setlength{\\tabcolsep}{4pt}\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Model} & \\textbf{\\cls{} (\\%)} & \\textbf{\\cls{} Var.\\ (\\%)} & \\textbf{\\cwm{} (\\%)} & \\textbf{\\traj{} Var.\\ (\\%)\\textsuperscript{$\\diamond$}} \\\\\n\\midrule\nQwen3-4B & 83.63 & 64.58 & 58.04 & 72.92 \\\\\nQwen3-8B & \\textbf{84.83 $\\pm$ 0.67} & 72.92 / 81.25\\textsuperscript{$\\dagger$} & 66.48 $\\pm$ 1.15 & 72.91 $\\pm$ 3.61 \\\\\nDeepSeek-6.7B & 84.38 $\\pm$ 2.50\\textsuperscript{$\\ddagger$} & 81.25\\textsuperscript{$\\dagger$} & 58.30 $\\pm$ 2.82 & 77.08 $\\pm$ 3.61 \\\\\n\\midrule\n0-shot (Qwen3-8B) & 49.90 & --- & --- & --- \\\\\n0-shot (DeepSeek) & 48.54 & --- & --- & --- \\\\\nMajority & 72.96 & 54.17 & 72.96 & 54.17 \\\\\n\\bottomrule\n\\end{tabular}}\n\n\\vspace{2pt}\n{\\footnotesize \\textsuperscript{$\\dagger$}Individual-seed variant accuracy. \\textsuperscript{$\\ddagger$}One seed excluded: truncate preprocessing$\\to$NaN val loss, decision collapse (Table~\\ref{tab:taxonomy}); mean over two matched seeds. \\textsuperscript{$\\diamond$}Var.\\ columns: variant-level accuracy ($n{=}48$); \\cls{} aggregated via all-pass rule; \\traj{} by design. Per-test: $n{=}9{,}784$. \\cwm{} unparseable: 54\\% (4B); default to pass; parseable-only 38--43\\%, below majority. Eval seq\\_length differs across models (Appendix~\\ref{app:threats}). \\cwm{} uses final-epoch checkpoint (step 6633) for s123/s456; s42 uses an earlier checkpoint (step 400) from a prior training configuration. Val loss is undefined for DeepSeek \\cwm{} runs (Qwen3 \\cwm{} has valid val loss; see \\S\\ref{sec:setup}). Checkpoint sensitivity analysis in Appendix~\\ref{app:cwm_convergence}.}\n\\end{table}\n\nFew-shot prompting (3-shot ICL) collapses to an always-predict-unresolved baseline (variant accuracy 45.83\\%, below majority 54.17\\%; Appendix~\\ref{app:few_shot}), establishing that execution-free verification requires task-specific fine-tuning regardless of formulation. The fine-tuning requirement (35--36\\pp{} gains, Table~\\ref{tab:repo_level}) is the first layer of our three-layer structure.\n\n\\paragraph{Formulation divergence.} Under our 4--8B LoRA protocol, \\cls{} and \\cwm{} diverge: the gap is 25.59\\pp{} at 4B and 18.35\\pp{} at 8B (Table~\\ref{tab:repo_level}), with \\cwm{} falling below majority baseline at both scales. Limited seed coverage and multiple confounds (\\S\\ref{sec:threats}) limit causal attribution.\n\n\\paragraph{Cross-model consistency.} DeepSeek-Coder shows the same direction (\\cls{} $>$ \\cwm{}) across all seeds; gap variation across families (20\\pp{} Qwen3 vs.\\ 23--28\\pp{} DeepSeek) narrows to ${\\sim}$2\\pp{} under matched checkpoints (Appendix~\\ref{app:threats}). All six \\cwm{} repo-level seeds exhibit format collapse ($>$50\\% unparseable), ruling out seed-specific artifacts.\n\n\\paragraph{Failure mode taxonomy.} Variant-level analysis ($n{=}48$) identifies three failure modes (Table~\\ref{tab:taxonomy}; full variant-level and per-mutation breakdowns in Appendices~\\ref{app:variant_level} and~\\ref{app:repo_mutation}): format collapse (\\cwm{}, 51--74\\% unparseable), decision collapse (\\cls{} under truncate preprocessing, fail recall ${\\sim}$14\\%), and aggregation penalty (\\cls{} under drop preprocessing, fail recall 38--57\\%). Decision collapse is configuration-dependent, not model-inherent. \\traj{} avoids aggregation penalty by predicting variant outcomes directly (72.91--77.08\\%). Downsampling \\cls{} to match \\traj{}'s data volume still yields 80.74\\% (+7.82\\pp{} above \\traj{}; Appendix~\\ref{app:downsample}). The CLS--TRAJ repo-level comparison remains exploratory: downsample ablation controls data volume but not label granularity (per-test vs.\\ variant-level), a formulation-inherent confound that cannot be experimentally resolved.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Repo-level failure mode taxonomy. Variant-level majority baseline: 54.17\\%.}\n\\label{tab:taxonomy}\n\\setlength{\\tabcolsep}{3pt}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llcc}\n\\toprule\n\\textbf{Failure Mode} & \\textbf{Representative} & \\textbf{Fail Recall} & \\textbf{Variant Acc} \\\\\n\\midrule\nFormat collapse & \\cwm{} (all) & N/A & 48--52\\% \\\\\nDecision collapse & \\cls{} (DeepSeek, s123) & ${\\sim}$14\\% & 56\\% \\\\\nAggr.\\ penalty & \\cls{} (Qwen3-8B) & 51--57\\% & 73--81\\% \\\\\nAggr.\\ penalty & \\cls{} (DeepSeek, s42) & 38--51\\% & 79--81\\% \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\\paragraph{Default assignment artifact.} The apparent \\cwm{} accuracy increase from 4B to 8B is an artifact of rising unparseable rate (53.7\\%$\\to$73.8\\%), inflating accuracy via majority-class default while parseable-only accuracy decreases (42.88\\%$\\to$38.52\\%); cross-seed evidence confirms the pattern (Appendix~\\ref{app:parseable_bias}).\n\n\\paragraph{Complexity as moderator.} The \\cls{}--\\cwm{} gap widens from 1--3\\pp{} (function) to 18--26\\pp{} (repo) under our protocol; a matched-context ablation confirms input disparity explains $<$3\\% of this gap (Appendix~\\ref{app:ablations}). While the directional advantage of lower-complexity output formulations may be anticipated from \\S\\ref{sec:failure-modes}, the magnitude of this gap, the function-level equivalence, and the specific failure mechanisms (Table~\\ref{tab:taxonomy}) were not predictable a priori.\n\n\\paragraph{Formulation$\\times$complexity interaction.} A mixed-effects linear probability model (LPM) ($n{=}56{,}480$, 139 clusters, DeepSeek-Coder) confirms: \\cwm{} effect at function level is negligible ($\\hat{\\beta}{=}-0.002$, $p{=}0.805$), but the formulation$\\times$complexity interaction is highly significant ($z{=}-23.7$, $p{<}0.001$). A cross-model LPM confirms formulation dominates ($\\hat{\\beta}{=}-0.22$ vs.\\ model $\\hat{\\beta}{=}+0.011$); model identity significance is estimator-dependent (LPM $p{=}0.002$; generalized estimating equations [GEE] $p{=}0.449$), consistent with limited clusters ($k{=}25 < 40$; Appendix~\\ref{app:interaction}).\n\n\\subsection{Analysis}\n\\label{sec:analysis}\n\n\\paragraph{Aggregation penalty.} The aggregation penalty ranges from 1.36\\pp{} to 19\\pp{}, negligible at function level ($\\bar{T} \\approx 2.3$) but substantial at repo level ($\\bar{T} \\gg 10$; Appendix~\\ref{app:extended_analysis}(a)).\n\n\\paragraph{Why does generation degrade at repo level?} Output complexity increases nonlinearly: function-level outputs average ${\\sim}$5--15 tokens; repo-level outputs average ${\\sim}$477 tokens, leading to format collapse under our ${\\leq}$8B LoRA protocol (53--74\\% unparseable; representative error examples in Appendix~\\ref{app:qualitative}). Even parseable outputs achieve only 38--43\\%, below majority; a model accidentally trained on CLS-format data achieves 86.05\\% with 0\\% unparseable, confirming the degradation stems from output format complexity, not task difficulty (Appendix~\\ref{app:extended_analysis}(c)). Four targeted interventions (doubling LoRA rank, majority voting [$k{=}5$], relaxed matching, and scaling to 8B) all fail to close this gap (Appendix~\\ref{app:extended_analysis}(g)); checkpoint selection explains $<$1\\pp{} (Appendix~\\ref{app:cwm_convergence}). \\cls{} achieves 217$\\times$ higher throughput (1 vs.\\ avg 477 output tokens; Appendix~\\ref{app:extended_analysis}(i)).\n\n\\paragraph{Error complementarity.} \\cls{} and \\cwm{} exhibit partially complementary errors, suggesting potential complementarity for routing. An oracle combination achieves 90.63\\% (+2.80\\pp{}; 95\\% CI [89.3\\%, 91.9\\%]; single-seed) at function level and 95.83\\% (+14.58\\pp{}; $n{=}48$) at repo level. Simple routing heuristics capture $<$0.4\\pp{} of the oracle gap; the complementarity is instance-specific, suggesting that simple heuristics are insufficient; whether a learned router can capture this advantage remains open (Appendix~\\ref{app:oracle}).\n\n\\subsection{Threats to Validity}\n\\label{sec:threats}\n\nWe identify five potential confounds (Appendix~\\ref{app:threats}): checkpoint selection ($<$1\\pp{}), evaluation sequence length (${\\sim}$1.5\\pp{}), preprocessing (${\\sim}$8\\pp{}; val-test distribution shift in Appendix~\\ref{app:mutation_distribution}), \\traj{} training regime, and \\cwm{} scale/pretraining (primary limitation). Preprocessing and checkpoint interact, accounting for up to 7.68\\pp{} variation within one model (Appendix~\\ref{app:threats}). The 18--26\\pp{} gap exceeds any single confound, but correlated confounds and limited seeds preclude definitive causal attribution. Holm-Bonferroni ($k{=}5$) confirms the two core claims (adjusted $p{=}0.015$ and $p{=}0.028$; Table~\\ref{tab:holm}).\n",
      "numLines": 197,
      "startLine": 1,
      "totalLines": 197
    }
  },
  "sourceToolAssistantUUID": "f75a1110-a243-480e-9f31-0ff9c7eaa02f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/paper_audit_content_8033e618",
  "sessionId": "d10eba16-884c-49dd-bd31-5cc0ef3bc131",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-25T07:52:04.111Z_

<details open><summary>🔧 Tool call — Read · `toolu_01QYhVw1nUAsmkHJtZnFzAGJ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "07c70d00-5639-474f-8fbe-6a24224b01f3",
  "isSidechain": false,
  "requestId": "req_011CbNvXNj3MMNLN5yzjvaJH",
  "type": "assistant",
  "uuid": "2216cbde-a46d-4b98-b7c1-c3b613bc425f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/paper_audit_content_8033e618",
  "sessionId": "d10eba16-884c-49dd-bd31-5cc0ef3bc131",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RzegdawgqtJMotASk4zb6m",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11924,
      "cache_read_input_tokens": 39764,
      "output_tokens": 725,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11924,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 725,
          "cache_read_input_tokens": 39764,
          "cache_creation_input_tokens": 11924,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11924
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

_source line 33 · 2026-05-25T07:52:04.124Z_

<details><summary>↩ Tool result · `toolu_01QYhVw1nUAsmkHJtZnFzAGJ`</summary>

```text
1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	We presented the first systematic comparison of three execution-free verification formulations (\cls{}, \cwm{}, \traj{}) under ${\leq}$8B LoRA fine-tuning. At function level, \cls{} and \cwm{} are statistically equivalent (TOST $p{=}0.007$, 5 seeds); \traj{} equivalence is inconclusive after Holm correction. At repository level, divergence reaches 18--26\pp{} ($z{=}-23.7$) via three failure modes, consistent across families (\S\ref{sec:threats}). 14B results (3 seeds, single family) narrow all gaps to 1.07\pp{}; whether the repo-level divergence is formulation-inherent or capacity-contingent remains open. Scaling to 32B+~\cite{meta2025cwm} and complexity-aware routing are key open questions.
5	
6	\section*{Limitations}
7	
8	Primary findings use ${\leq}$8B LoRA fine-tuning with multi-seed replication; 14B results use a single model family (Qwen3) with 3 seeds; cross-family replication and evaluation at 32B+ are needed. The repo-level gap may diminish at 32B+ scale or with execution-trace pretraining~\cite{meta2025cwm}. All evaluation uses Python-only benchmarks; other languages may exhibit different format compliance rates. Training data uses synthetic mutation operators~\cite{andrews2005mutation,just2014mutants}; the synthetic-to-real transfer gap remains untested (Appendix~\ref{app:limitations}). Format-specific interventions (constrained decoding~\cite{poesia2022synchromesh,dong2024xgrammar,willard2023outlines} or output-format pretraining) may mitigate \cwm{}'s format collapse but were not evaluated.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2216cbde-a46d-4b98-b7c1-c3b613bc425f",
  "isSidechain": false,
  "promptId": "15e99bee-64bb-4bc0-b559-9e40ffdfc882",
  "type": "user",
  "uuid": "18ea6e68-d93a-48a4-94b6-ec20a7fe258b",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/conclusion.tex",
      "content": "\\section{Conclusion}\n\\label{sec:conclusion}\n\nWe presented the first systematic comparison of three execution-free verification formulations (\\cls{}, \\cwm{}, \\traj{}) under ${\\leq}$8B LoRA fine-tuning. At function level, \\cls{} and \\cwm{} are statistically equivalent (TOST $p{=}0.007$, 5 seeds); \\traj{} equivalence is inconclusive after Holm correction. At repository level, divergence reaches 18--26\\pp{} ($z{=}-23.7$) via three failure modes, consistent across families (\\S\\ref{sec:threats}). 14B results (3 seeds, single family) narrow all gaps to 1.07\\pp{}; whether the repo-level divergence is formulation-inherent or capacity-contingent remains open. Scaling to 32B+~\\cite{meta2025cwm} and complexity-aware routing are key open questions.\n\n\\section*{Limitations}\n\nPrimary findings use ${\\leq}$8B LoRA fine-tuning with multi-seed replication; 14B results use a single model family (Qwen3) with 3 seeds; cross-family replication and evaluation at 32B+ are needed. The repo-level gap may diminish at 32B+ scale or with execution-trace pretraining~\\cite{meta2025cwm}. All evaluation uses Python-only benchmarks; other languages may exhibit different format compliance rates. Training data uses synthetic mutation operators~\\cite{andrews2005mutation,just2014mutants}; the synthetic-to-real transfer gap remains untested (Appendix~\\ref{app:limitations}). Format-specific interventions (constrained decoding~\\cite{poesia2022synchromesh,dong2024xgrammar,willard2023outlines} or output-format pretraining) may mitigate \\cwm{}'s format collapse but were not evaluated.",
      "numLines": 8,
      "startLine": 1,
      "totalLines": 8
    }
  },
  "sourceToolAssistantUUID": "2216cbde-a46d-4b98-b7c1-c3b613bc425f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/paper_audit_content_8033e618",
  "sessionId": "d10eba16-884c-49dd-bd31-5cc0ef3bc131",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-25T07:52:04.590Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Ec5aFvNHv3Va5rXeV6rkdB`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "18ea6e68-d93a-48a4-94b6-ec20a7fe258b",
  "isSidechain": false,
  "requestId": "req_011CbNvXNj3MMNLN5yzjvaJH",
  "type": "assistant",
  "uuid": "1e83d7f2-3374-4643-9e1c-521c91c6de8f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/paper_audit_content_8033e618",
  "sessionId": "d10eba16-884c-49dd-bd31-5cc0ef3bc131",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RzegdawgqtJMotASk4zb6m",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11924,
      "cache_read_input_tokens": 39764,
      "output_tokens": 725,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11924,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 725,
          "cache_read_input_tokens": 39764,
          "cache_creation_input_tokens": 11924,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11924
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

_source line 35 · 2026-05-25T07:52:04.868Z_

<details><summary>↩ Tool result · `toolu_01Ec5aFvNHv3Va5rXeV6rkdB`</summary>

```text
1	\appendix
2	
3	\noindent\textbf{Appendix overview.} A: Oracle analysis. B: Ablations. C: Per-mutation breakdown. D: Variant-level accuracy. E: Hyperparameters. F: Prompt templates. G: Mutation distribution. H: Qualitative errors. I: Extended analysis (I.a--I.k). J: TOST sensitivity (J.1: Bayesian ROPE). K: Effect sizes. L: Holm-Bonferroni. M: Mixed-effects regression. N: Parseable bias. O: Threats (O.1: CWM convergence; O.2: Extended validity). P: AI assistants.
4	
5	\section{Oracle Accuracy-Utility Analysis}
6	\label{app:oracle}
7	
8	We stratify SWE-bench Verified instances by Fail-to-Pass (F2P) test count $T$, comparing per-test vs.\ trajectory-level oracle resolve rates under i.i.d.\ and block-correlated error models (ICC $= 0.191$, from function-level analysis; \S\ref{sec:equivalence}).
9	
10	\begin{table}[h]
11	\centering
12	\small
13	\caption{Oracle accuracy-utility frontier: per-test advantage stratified by F2P test count ($T$) on SWE-bench Verified (500 instances). Block-correlated model uses function-level ICC $= 0.191$ (from function-level analysis, \S\ref{sec:equivalence}). Pass-to-Pass (P2P) regression rate: 1.04\% mean, 0\% median.}
14	\label{tab:oracle}
15	\resizebox{\columnwidth}{!}{%
16	\setlength{\tabcolsep}{3pt}
17	\begin{tabular}{lcccc}
18	\toprule
19	\textbf{$T$} & \textbf{Inst.\%} & \textbf{i.i.d.\ (\pp{})} & \textbf{Block (\pp{})} & \textbf{Contrib.\%} \\
20	\midrule
21	$1$ & 68.7 & $-$0.04 & $-$0.09 & $\approx$0 \\
22	$2$ & 19.1 & 18.49 & 31.69 & 55.3 \\
23	$3$--$5$ & 7.1 & 25.00 & 40.74 & $\approx$26 \\
24	$\geq 6$ & 5.1 & 30.00 & 40.06 & $\approx$19 \\
25	\midrule
26	\textbf{All} & 100.0 & --- & \textbf{10.93} & 100.0 \\
27	\bottomrule
28	\end{tabular}}
29	\end{table}
30	
31	\begin{figure}[h]
32	\centering
33	\includegraphics[width=\columnwidth]{figures/paper/fig3_oracle_stratified.pdf}
34	\caption{Oracle per-test advantage by F2P test count $T$. Advantage is zero at $T{=}1$ (68.7\%) and concentrates at $T{=}2$ (19.1\%, contributing 55.3\% of total advantage). Note: $y$-axis does not start at zero.}
35	\label{fig:oracle_stratified}
36	\end{figure}
37	
38	Table~\ref{tab:oracle} and Figure~\ref{fig:oracle_stratified} reveal a sharp concentration: at $T = 1$ (68.7\% of instances), per-test and trajectory-level are informationally equivalent. The advantage materializes at $T = 2$ (19.1\%), where block-correlated advantage reaches 31.69\pp{} (55.3\% of total). The overall block-correlated advantage is 10.93\pp{}, driven by the $T \geq 2$ minority. Block correlation amplifies relative to i.i.d.: at $T = 2$, 31.69\pp{} vs.\ 18.49\pp{} (1.7$\times$). P2P regression is negligible (1.04\% mean, 0\% median); the practical value concentrates in F2P discrimination.
39	
40	\paragraph{Sensitivity to ICC estimate.}
41	The analysis above uses ICC $= 0.191$ from function-level analysis (\S\ref{sec:equivalence}), where mean cluster size $\bar{k} \approx 16.5$ yields DEFF $= 3.97$. At repository level, within-problem correlation is substantially stronger: ICC $= 0.3146$ with DEFF $= 114.4$ (\S\ref{sec:repo}), yielding an effective sample size of $n_{\text{eff}} \approx 9{,}784 / 114.4 \approx 86$ independent observations~\cite{moulton1990}, still sufficient for regression but limiting precision of variance component estimates. This is a consequence of the larger and more heterogeneous test suites in SWE-bench Verified problems. Under higher ICC, within-problem errors cluster more tightly and amplify the block-correlated per-test advantage at each $T$ stratum; the correction from i.i.d.\ to block-correlated grows monotonically with ICC. The function-level ICC $= 0.191$ used in Table~\ref{tab:oracle} thus provides a conservative lower bound on the per-test advantage. The repo-level correlation structure would yield an even larger gap between per-test and trajectory-level oracle resolve rates, which strengthens the case for per-test granularity at repository-level complexity.
42	
43	\section{Ablation Studies}
44	\label{app:ablations}
45	
46	\paragraph{LoRA rank sensitivity.}
47	All \cwm{} experiments use LoRA rank $r{=}16$. To test whether this capacity constraint handicaps \cwm{}, we train rank-32 variants (seed 42), doubling adapter parameters.
48	
49	\begin{table}[h]
50	\centering
51	\small
52	\caption{LoRA rank ablation for \cwm{} 4B (seed 42, 3 epochs, lr $= 2{\times}10^{-4}$). Rank-16 seed variance: 0.53\pp{} (seeds 42 vs.\ 456).}
53	\label{tab:rank_ablation}
54	\setlength{\tabcolsep}{4pt}
55	\begin{tabular}{lccccc}
56	\toprule
57	\textbf{Config} & \textbf{$\alpha/r$} & \textbf{Acc (\%)} & \textbf{Fail \fone{}} & \textbf{Pass \fone{}} & \textbf{$\Delta$} \\
58	\midrule
59	$r{=}16$, $\alpha{=}32$ & 2 & \textbf{87.51} & --- & --- & --- \\
60	$r{=}32$, $\alpha{=}32$ & 1 & 87.00 & 87.1 & 86.9 & $-$0.51 \\
61	$r{=}32$, $\alpha{=}64$ & 2 & 87.04 & 87.27 & 86.79 & $-$0.47 \\
62	\bottomrule
63	\end{tabular}
64	\end{table}
65	
66	Both rank-32 variants fall within the 2-seed variance of the rank-16 baseline (0.53\pp{} between seeds 42 and 456; Table~\ref{tab:rank_ablation}). The $\alpha{=}64$ variant (matching the baseline $\alpha/r{=}2$ ratio) rules out the confound that the $\alpha{=}32$ result might reflect reduced effective scaling rather than rank insensitivity. This is consistent with \cwm{}'s function-level performance being bounded by output-format constraints rather than adapter capacity.
67	
68	\paragraph{Majority voting.}
69	Majority voting ($K{=}3$) decreases accuracy from 87.51\% to 86.83\% ($-$0.68\pp{}): errors are systematic rather than stochastic, so sampling-based ensembles do not help.
70	
71	\paragraph{Sequence-length ablation details.}
72	Both formulations are trained with \texttt{max\_seq\_length}$=$2,048. At inference, \cwm{} reserves \texttt{max\_new\_tokens}$=$512, leaving ${\sim}$1,536 effective input tokens; \cls{} allocates nearly all context to input (5,120--8,192 tokens). A matched-context ablation (\cls{} 8B at 2,048 tokens) achieves 83.04\%, only 1.44\pp{} below the 8,192-token evaluation (84.48\%), though truncation introduces 136 unparseable outputs (1.39\% of test samples). The matched-context gap (\cls{}@2,048 vs.\ \cwm{}@2,048) is 25.00\pp{} (98\% of the full 25.59\pp{} gap), confirming that input context disparity explains at most 3\% of the difference.
73	
74	\paragraph{Training data size control.}
75	\label{app:downsample}
76	To control for the training set size asymmetry between \cls{} (${\sim}$70K instances) and \traj{} (386 variant-level instances, ${\sim}$8K per-test equivalents, at repo level), we downsample \cls{} training data to match \traj{} in data volume. Downsampled \cls{} (Qwen3-4B, seed 42) achieves 80.74\% repo-level per-test accuracy, only 2.89\pp{} below the full-data \cls{} (83.63\%) and still 7.82\pp{} above \traj{} (72.92\%). The \cls{} formulation advantage is not attributable to training data volume.
77	
78	At function level, the relationship reverses: \traj{} uses 8,052 variant-level instances (2.24$\times$ more unique variants than \cls{}/\cwm{}'s 3,596 from 15,290 per-test instances). \cls{} nonetheless outperforms \traj{} by 2.13\pp{} (88.43\% vs.\ 86.30\%, Qwen3-4B), ruling out data volume as the explanation. An extreme downsample ablation (CLS trained on 447 per-test instances, ${\sim}$105 unique variants) achieves 78.57 $\pm$ 0.78\%, confirming that per-test classification maintains reasonable performance under severe data reduction, though it falls below \traj{} (86.30\%) given the 20$\times$ data disadvantage.
79	
80	\paragraph{Few-shot prompting baselines.}
81	\label{app:few_shot}
82	We evaluate 3-shot in-context learning at repo level to test whether prompting strategy closes the gap to fine-tuned models. Table~\ref{tab:few_shot} reports both per-test and variant-level accuracy.
83	
84	\begin{table}[h]
85	\centering
86	\small
87	\caption{Repo-level prompting baselines (per-test $n{=}9{,}784$; variant-level $n{=}48$). Majority baseline: 72.96\% per-test, 54.17\% variant-level.}
88	\label{tab:few_shot}
89	\setlength{\tabcolsep}{4pt}
90	\resizebox{\columnwidth}{!}{%
91	\begin{tabular}{lcccc}
92	\toprule
93	\textbf{Model} & \textbf{0-shot (per-test)} & \textbf{3-shot (per-test)} & \textbf{3-shot (variant)} \\
94	\midrule
95	Qwen3-8B & 49.90\% & 71.61\% & 45.83\%\textsuperscript{$\ast$} \\
96	DeepSeek-6.7B & 48.54\% & 46.28\% & 45.83\%\textsuperscript{$\ast$} \\
97	\bottomrule
98	\end{tabular}}
99	
100	\vspace{2pt}
101	{\footnotesize \textsuperscript{$\ast$}Both models achieve 45.83\% by correctly classifying all 22 unresolved variants and zero resolved variants (22/48 = 45.83\%), equivalent to an always-predict-unresolved baseline. The 100\% overlap in variant-level predictions confirms complete degradation at task-relevant granularity.}
102	\end{table}
103	
104	Both models converge to exactly 45.83\% variant-level accuracy under 3-shot prompting, below majority baseline (54.17\%). Variant-level analysis reveals this is not a coincidence: both models correctly classify all 22 unresolved variants and zero resolved variants, equivalent to an always-predict-unresolved baseline with 100\% prediction overlap. Per-test accuracy diverges sharply (Qwen3-8B 71.61\% vs.\ DeepSeek 46.28\%), but this divergence is entirely superficial: Qwen3-8B predicts pass on nearly all tests, inflating per-test accuracy on a pass-heavy dataset (72.96\% pass rate) without genuine discriminative ability. Per-test metrics can thus severely misrepresent baseline capability; variant-level evaluation is necessary to detect complete degradation. Neither 0-shot nor few-shot prompting approaches fine-tuned performance (82--84\% per-test); fine-tuning is a necessary condition for repo-level verification.
105	
106	\section{Repo-Level Per-Mutation Breakdown}
107	\label{app:repo_mutation}
108	
109	Table~\ref{tab:mutation_breakdown} compares per-mutation accuracy at repo level. \cls{} produces 0\% unparseable outputs; all values are direct classification accuracy. \cwm{} overall accuracy includes default-pass assignment for unparseable outputs (see \S\ref{sec:repo}).
110	
111	\begin{table}[h]
112	\centering
113	\small
114	\caption{Per-mutation test accuracy (\%) at repo level (SWE-bench Verified, $n{=}9{,}784$). \cls{} 8B reports two seeds; $\Delta$ is mean 4B$\to$8B gain for \cls{}. \cwm{} 4B per-mutation overall accuracy omitted for non-gold mutations due to low parse rates (4.4--56.9\%, Table~\ref{tab:cwm_mutation_parse}); gold overall accuracy derived from parse rate 43.5\% and parseable accuracy 23.5\%.}
115	\label{tab:mutation_breakdown}
116	\resizebox{\columnwidth}{!}{%
117	\setlength{\tabcolsep}{3pt}
118	\begin{tabular}{lccccccc}
119	\toprule
120	\textbf{Mutation} & \textbf{$n$} & \textbf{CLS 4B} & \textbf{CLS 8B s42} & \textbf{CLS 8B s123} & \textbf{CWM 4B} & \textbf{CWM 8B} & \textbf{$\Delta$ CLS} \\
121	\midrule
122	gold & 4,633 & 98.25 & 96.24 & 99.60 & 66.72 & 80.06 & $-$0.33 \\
123	operator\_swap & 3,357 & 78.91 & 81.38 & 82.60 & --- & 54.57 & +3.08 \\
124	off\_by\_one & 183 & 58.47 & 86.89 & 79.20 & --- & 63.39 & \textbf{+24.58} \\
125	return\_value & 562 & 67.97 & 75.44 & 66.40 & --- & 49.11 & +2.95 \\
126	boundary\_removal & 1,049 & 46.90 & 46.90 & 44.90 & --- & 42.23 & $-$1.00 \\
127	\bottomrule
128	\end{tabular}}
129	\end{table}
130	
131	Figure~\ref{fig:mutation_heatmap} visualises the per-mutation accuracy contrast between \cls{} and \cwm{} at repo level.
132	
133	\begin{figure}[h]
134	\centering
135	\includegraphics[width=\columnwidth]{figures/paper/fig_mutation_heatmap.pdf}
136	\caption{Per-mutation repo-level accuracy heatmap. \cls{} 8B values are seed-averaged (s42/s123). \cwm{} 8B includes default-pass for unparseable outputs. \texttt{boundary\_removal} is a scale-invariant difficulty ceiling (${\sim}$45\%) for both formulations.}
137	\label{fig:mutation_heatmap}
138	\end{figure}
139	
140	Table~\ref{tab:cwm_mutation_parse} shows that \cwm{} generation quality degrades from 4B to 8B across all mutation types.
141	
142	\begin{table}[h]
143	\centering
144	\small
145	\caption{\cwm{} parse rates and parseable-only accuracy per mutation type (seed 42). Parse rate decreases uniformly from 4B to 8B; parseable-only accuracy is below random binary chance (50\%) for gold at both scales.}
146	\label{tab:cwm_mutation_parse}
147	\setlength{\tabcolsep}{4pt}
148	\begin{tabular}{lcccc}
149	\toprule
150	& \multicolumn{2}{c}{\textbf{Parse Rate (\%)}} & \multicolumn{2}{c}{\textbf{Parse Acc (\%)}} \\
151	\cmidrule(lr){2-3} \cmidrule(lr){4-5}
152	\textbf{Mutation} & \textbf{4B} & \textbf{8B} & \textbf{4B} & \textbf{8B} \\
153	\midrule
154	gold & 43.5 & 23.9 & 23.5 & 16.5 \\
155	operator\_swap & 56.9 & 21.2 & 63.1 & 58.8 \\
156	off\_by\_one & 4.4 & 27.3 & 0.0 & 38.0 \\
157	return\_value & 48.8 & 26.9 & 27.0 & 56.9 \\
158	boundary\_removal & 30.6 & 51.8 & 59.2 & 51.8 \\
159	\bottomrule
160	\end{tabular}
161	\end{table}
162	
163	Key findings: (1)~Gold parse rate collapses from 43.5\% to 23.9\% at 8B; the simplest generation target (unmodified code, where all tests pass) degrades most, consistent with a fundamental generation bottleneck rather than task difficulty. (2)~Among parseable outputs, gold accuracy is 16.5--23.5\%: the model generates outputs that fail exact-match even for correct code. (3)~\texttt{off\_by\_one} is an anomaly: parse rate \emph{increases} from 4.4\% to 27.3\%, but this is from an extremely low base ($n{=}8$ parseable at 4B), making both directions unreliable for this category.
164	
165	\section{Variant-Level Accuracy}
166	\label{app:variant_level}
167	
168	Table~\ref{tab:variant_level} reports variant-level accuracy ($n{=}48$) alongside per-test accuracy for all repo-level configurations. For \cls{}, the aggregation penalty (per-test $\to$ variant-level drop) ranges from 1\pp{} to 19\pp{} and is largest for models with low fail recall under the all-pass rule. \cwm{} variant-level accuracy (48--52\%) falls at or below the majority baseline, consistent with format collapse as the dominant failure mode.
169	
170	\begin{table}[h]
171	\centering
172	\small
173	\caption{Repo-level per-test vs.\ variant-level accuracy ($n{=}48$ variants). Penalty = per-test $-$ variant-level. \traj{} predicts variant outcomes directly (no aggregation). Variant-level majority baseline: 54.17\% (26/48).}
174	\label{tab:variant_level}
175	\setlength{\tabcolsep}{3pt}
176	\resizebox{\columnwidth}{!}{%
177	\begin{tabular}{llcccc}
178	\toprule
179	\textbf{Model} & \textbf{Seed} & \textbf{Per-test (\%)} & \textbf{Variant (\%)} & \textbf{Penalty (\pp{})} & \textbf{Fail Recall (\%)} \\
180	\midrule
181	\multicolumn{6}{l}{\emph{\cls{}}} \\
182	Qwen3-8B & s42 & 84.48 & 72.92 & 11.56 & 56.76 \\
183	Qwen3-8B & s123 & 85.60 & 81.25 & 4.35 & 51.44 \\
184	Qwen3-4B & s42 & 83.63 & 64.58 & 19.05 & 48.72 \\
185	DeepSeek-6.7B & s42 (e1) & 82.61 & 81.25 & 1.36 & 51.02 \\
186	DeepSeek-6.7B & s42 (e3) & 82.51 & 79.17 & 3.34 & 38.47 \\
187	DeepSeek-6.7B & s123 & 74.93 & 56.25 & 18.68 & ${\sim}$13.72 \\
188	\midrule
189	\multicolumn{6}{l}{\emph{\cwm{}}} \\
190	Qwen3-8B & s42 & 65.17 & 52.08 & 13.09 & --- \\
191	DeepSeek-6.7B$^\dagger$ & s123 & --- & 47.92 & --- & --- \\
192	\midrule
193	\multicolumn{6}{l}{\emph{\traj{}}} \\
194	Qwen3-4B & s42 & --- & 72.92 & --- & --- \\
195	Qwen3-8B & s42 & --- & 70.83 & --- & --- \\
196	DeepSeek-6.7B & 3-seed & --- & 77.08 $\pm$ 3.61 & --- & --- \\
197	\midrule
198	Majority & --- & 72.96 & 54.17 & --- & --- \\
199	\bottomrule
200	\end{tabular}}
201	\vspace{2pt}
202	
203	{\footnotesize $^\dagger$Evaluated on ${\sim}$75\% of test instances (7210--7668 of 9784). DeepSeek \traj{} Table~\ref{tab:repo_level} reports 3 seeds (42/123/456) for alignment with \cls{}/\cwm{} seed coverage; three supplementary seeds (0/789/999) yield 75.0\%, 66.7\%, 79.2\% respectively (6-seed mean 75.35 $\pm$ 5.00\%), consistent in direction.}
204	\end{table}
205	
206	\section{Training Hyperparameters}
207	\label{app:hyperparams}
208	
209	Table~\ref{tab:hyperparams} lists all hyperparameters used for fine-tuning. Both \cls{} and \cwm{} share the same LoRA configuration, optimizer, and training schedule; the only differences are per-device batch size, gradient accumulation steps (adjusted to maintain identical effective batch size of 32 across model sizes), and learning rate (DeepSeek-Coder uses $2{\times}10^{-4}$ vs.\ $5{\times}10^{-5}$ for Qwen3, selected via grid search over $\{5{\times}10^{-5}, 1{\times}10^{-4}, 2{\times}10^{-4}\}$ on held-out validation loss).
210	
211	\begin{table}[h]
212	\centering
213	\small
214	\caption{Training hyperparameters for \cls{}/\cwm{} configurations. \traj{} models use lr $= 2{\times}10^{-4}$ due to the smaller training set (${\sim}$8K function-level instances vs.\ ${\sim}$70K for \cls{}/\cwm{}); other hyperparameters are shared.}
215	\label{tab:hyperparams}
216	\resizebox{\columnwidth}{!}{%
217	\begin{tabular}{ll}
218	\toprule
219	\multicolumn{2}{l}{\textbf{Shared across all configurations}} \\
220	\midrule
221	LoRA rank / alpha / dropout & 16 / 32 / 0.05 \\
222	LoRA targets & \texttt{q/k/v/o\_proj} \\
223	Optimizer & AdamW ($\beta_1{=}0.9$, $\beta_2{=}0.999$) \\
224	LR scheduler & Linear \\
225	Effective batch size & 32 \\
226	Max sequence length & 2,048 \\
227	Epochs & 3 \\
228	Precision & bf16 \\
229	Gradient checkpointing & \checkmark \\
230	Seeds (function) & \{42, 123, 456, 789, 0\}\textsuperscript{$b$} \\
231	Seeds (repo) & \{42, 123, 456\}\textsuperscript{$c$} \\
232	\bottomrule
233	\end{tabular}}
234	
235	\vspace{6pt}
236	
237	\resizebox{\columnwidth}{!}{%
238	\begin{tabular}{lccc}
239	\toprule
240	\multicolumn{4}{l}{\textbf{Model-family--specific parameters}} \\
241	\midrule
242	& \textbf{Qwen3-4B} & \textbf{Qwen3-8B} & \textbf{DS-6.7B} \\
243	\midrule
244	Learning rate & 5e-5 & 5e-5 & 2e-4 \\
245	Weight decay & 0.01 & 0.01 & 0.0 \\
246	Warmup ratio & 0.05 & 0.05 & 0.1 \\
247	Batch / grad.\ accum.\ (\cls{}) & 2 / 16 & 1 / 32 & 2 / 16 \\
248	Batch / grad.\ accum.\ (\cwm{}) & 1 / 32 & 1 / 32 & 1 / 32 \\
249	Training samples & 70,748 & 70,748 & 67,343--70,748\textsuperscript{$a$} \\
250	\bottomrule
251	\end{tabular}}
252	
253	\vspace{2pt}
254	{\footnotesize $^a$DeepSeek \cls{} canonical run (s42) uses drop preprocessing, which excludes 3,405 sequences exceeding max length (67,343 of 70,748). The s123 run uses truncate preprocessing (70,748 samples) but produces NaN validation loss. See \S\ref{sec:setup}. $^b$Seeds 789 and 0 use NF4 quantization; others use bf16. $^c$Repo-level seed coverage varies by configuration; see Table~\ref{tab:repo_level} caption for per-model counts.}
255	\end{table}
256	
257	\paragraph{Data processing.} DeepSeek CWM seeds use \texttt{train\_unified.py}, which drops samples exceeding \texttt{max\_seq\_length} (3{,}405 of 70{,}748 samples, 4.8\%). Qwen CWM seeds use \texttt{train\_repo\_cwm.py}, which truncates and retains all samples. This difference affects total training steps (${\sim}$12{,}627 vs.\ ${\sim}$13{,}266 for DeepSeek, ${\sim}$6{,}633 for Qwen) but not the training data distribution, as dropped samples are uniformly distributed across labels.
258	
259	\paragraph{Prompt templates.} Prompt templates for all formulations (\cls{}, \cwm{}, \traj{}) are provided in the code repository. \cls{} uses a binary classification template (``Does this test pass or fail?''); \cwm{} uses an execution simulation template (``What is the output of this test?''); \traj{} uses a variant-level verdict template (``Is this patch resolved or unresolved?'').
260	
261	\paragraph{Mutation operators.} We use five mutation types: (1)~\emph{gold}: unmodified code (all tests pass); (2)~\emph{operator\_swap}: replaces comparison or arithmetic operators (e.g., \texttt{<} $\to$ \texttt{<=}); (3)~\emph{off\_by\_one}: shifts loop bounds or array indices by $\pm$1; (4)~\emph{return\_value}: modifies return statements (e.g., negating a boolean, changing a constant); (5)~\emph{boundary\_removal}: removes conditional guards or boundary checks. Mutation operators were applied using AST-level transformation; variants that did not alter any test outcome were discarded.
262	
263	\paragraph{Compute budget.}
264	All experiments were conducted on NVIDIA RTX 5090 GPUs. Training time is approximately 1.5 hours per run for 4B models and 2 hours for 8B models. Total compute budget: ${\sim}$370 GPU-hours across 223 completed runs (135 successful, 88 failed/killed; ${\sim}$46 unique configurations including seeds, formulations, model sizes, and ablations).
265	
266	\section{Prompt Templates}
267	\label{app:prompts}
268	
269	We show representative prompt examples for each formulation. All examples use the same input instance for comparability.
270	
271	\paragraph{CLS (per-test classification).}
272	{\footnotesize\begin{verbatim}
273	System: You are a code verifier.
274	Given a code patch and a test name,
275	predict whether the test will pass
276	or fail when run against the
277	patched code.
278	
279	User:
280	## Patch (git diff)
281	&lt;patch content> [... truncated]
282	## Test
283	test_boundary_check
284	Will this test pass or fail?
285	
286	Target: pass
287	\end{verbatim}}
288	
289	\paragraph{CWM (execution simulation).}
290	{\footnotesize\begin{verbatim}
291	System: You are a code execution
292	simulator. Given a code snippet and
293	a test case, predict the execution
294	result.
295	
296	User:
297	## Code
298	&lt;code content> [... truncated]
299	## Test
300	test_boundary_check
301	What is the execution result?
302	
303	Target: PASS: test completed
304	successfully
305	\end{verbatim}}
306	
307	\paragraph{TRAJ (trajectory scoring).}
308	{\footnotesize\begin{verbatim}
309	System: You are a code repair
310	verifier. Given the code patch and
311	test summary, predict whether all
312	tests pass (resolved) or any test
313	fails (unresolved).
314	
315	User:
316	[Code]
317	&lt;patch content> [... truncated]
318	[Test Summary]
319	&lt;all test names and descriptions>
320	
321	Target: resolved
322	\end{verbatim}}
323	
324	\cls{} and \cwm{} share the same input format (one code--test pair per instance); \cls{} produces a single token (\texttt{pass}/\texttt{fail}), while \cwm{} generates a variable-length execution trace. \traj{} receives all tests concatenated and produces a single token (\texttt{resolved}/\texttt{unresolved}).
325	
326	
327	\section{Val-Test Mutation Type Distribution}
328	\label{app:mutation_distribution}
329	
330	Table~\ref{tab:mutation_distribution} reports the mutation type composition of the repo-level validation and test sets. The most notable shift is \texttt{operator\_swap}, which nearly doubles from val (19.1\%) to test (34.3\%), while \texttt{off\_by\_one} shrinks from 10.0\% to 1.9\%.
331	
332	\begin{table}[h]
333	\centering
334	\small
335	\caption{Repo-level mutation type distribution: validation vs.\ test set, with per-type \cls{} accuracy at two model sizes (seed 42). Shift = test\% $-$ val\%.}
336	\label{tab:mutation_distribution}
337	\setlength{\tabcolsep}{3pt}
338	\resizebox{\columnwidth}{!}{%
339	\begin{tabular}{lccccc}
340	\toprule
341	\textbf{Mutation Type} & \textbf{Val (\%)} & \textbf{Test (\%)} & \textbf{Shift} & \textbf{\cls{} 4B} & \textbf{\cls{} 8B} \\
342	\midrule
343	gold & 45.2 & 47.4 & +2.2 & 98.3 & 96.2 \\
344	operator\_swap & 19.1 & 34.3 & +15.2 & 78.9 & 81.4 \\
345	boundary\_removal & 15.0 & 10.7 & $-$4.3 & 46.9 & 46.9 \\
346	return\_value & 10.7 & 5.7 & $-$5.0 & 68.0 & 75.4 \\
347	off\_by\_one & 10.0 & 1.9 & $-$8.1 & 58.5 & 86.9 \\
348	\bottomrule
349	\end{tabular}}
350	\end{table}
351	
352	The \texttt{operator\_swap} shift is the primary source of val-test distribution mismatch. Since \cls{} achieves moderate accuracy on this type (78.9--81.4\%), the over-representation in the test set does not systematically bias overall accuracy estimates in either direction. Two boundary observations are notable: (1)~\texttt{boundary\_removal} represents a scale-invariant difficulty ceiling at ${\sim}$47\% across both model sizes: this mutation type resists capacity scaling; (2)~\texttt{off\_by\_one} shows the largest scaling gain (+28.4\pp{}, 58.5\%$\to$86.9\%) but its small test share (1.9\%) limits its contribution to overall accuracy differences across scales.
353	
354	\section{Qualitative Error Analysis}
355	\label{app:qualitative}
356	
357	To complement the quantitative divergence reported in \S\ref{sec:repo}, we examine representative errors from each formulation at repository level.
358	
359	\paragraph{\cwm{} failure modes.}
360	Two patterns account for the majority of unparseable \cwm{} outputs on Qwen3. (1)~\emph{Task misunderstanding}: the model generates a complete simulated test runner log (test names, timing, summary lines) rather than a pass/fail verdict. For instance, on \texttt{django\_\_django-14315}, the model outputs a fabricated 1,248-token Django test execution trace with hallucinated test names that do not exist in the target file. The model confuses ``predict test outcome'' with ``simulate test execution environment.'' (2)~\emph{Autoregressive degeneration}: the model enters a repetitive loop (e.g., repeating \texttt{from \_pytest.config import \_parse\_pytest\_args} until truncation at 4,542 tokens). Both patterns produce zero usable signal and default to the majority-class label. This explains why unparseable predictions carry higher accuracy than parseable ones (\S\ref{sec:repo}).
361	
362	\paragraph{\cls{} failure modes.}
363	\cls{} errors concentrate in two categories requiring multi-step reasoning. False positives arise from \emph{cross-concern value propagation}: a boundary removal mutation in \texttt{pytest} converts a guarded attribute access (\texttt{if xfailed and not xfailed.run}) to \texttt{if True:}, causing a NoneType error on tests exercising unrelated skip marks. The model fails to trace the None path through the pytest hook lifecycle. False negatives arise from \emph{mathematical equivalence}: on \texttt{HumanEval/130} (Tribonacci variant), the model predicts failure for correct code because verifying the self-referential recurrence requires algebraic substitution rather than syntactic inspection. This single problem accounts for 17\% of all function-level false negatives.
364	
365	\paragraph{Complementarity.}
366	These failure patterns operate at different levels: \cwm{} fails at the format level (producing no usable signal), while \cls{} fails at the reasoning level (producing a confident but incorrect binary verdict). Both formulations are FP-dominant (over-predict failure), but \cwm{}'s higher FP rate (70.3\% vs.\ 56.5\%) means it over-predicts failure on instances \cls{} correctly classifies, producing partial complementarity (oracle combination: 90.63\%; \S\ref{app:extended_analysis}, paragraph a).
367	
368	\section{Extended Analysis}
369	\label{app:extended_analysis}
370	
371	\paragraph{Function-level CWM metric robustness.}
372	At function level, \cwm{} outputs are short status strings (mean ${\sim}$5--15 tokens). The unparseable rate is only 1.39\%, and default-to-pass bias is $<$1\pp{}, well below the SESOI threshold. Exact string matching is appropriate for these short, structured outputs; semantic-but-format-different matches are rare given the constrained output space.
373	
374	\paragraph{(a) Error complementarity.}
375	\cls{} and \cwm{} are both FP-dominant at function level but at different rates, producing partial complementarity. Among \cls{} errors (seed 42), 56.5\% are false positives (PASS $\to$ FAIL); among \cwm{} errors, 70.3\% are false positives. Both formulations over-predict failure, but \cwm{}'s stronger FP bias means it incorrectly rejects passing tests that \cls{} correctly accepts. An oracle combination achieves 90.63\% accuracy (1713/1890 correct, 177 both-wrong; +2.80\pp{} over the best single formulation, \cls{} 87.83\%; single-seed estimate, seed 42). The complementarity arises from different \emph{degrees} of fail-bias rather than opposite error directions: \cwm{}'s generation bottleneck produces aggressive failure predictions, while \cls{}'s single-token output is more calibrated. Ensemble approaches exploiting this degree difference are a natural direction.
376	
377	\paragraph{(b) CWM error mode breakdown.}
378	Among unparseable \cwm{} outputs (Qwen3, repo-level), 76.9\% contain no execution keywords; 22.9\% contain ambiguous co-occurring pass/fail keywords. Format compliance varies sharply across repositories (scikit-learn: near-zero unparseable; sphinx: 100\%); repository-specific code patterns interact with the model's generation capabilities in complex ways. This per-repository variation is consistent with a model/tokenizer-specific failure rather than a formulation-level one.
379	
380	\paragraph{(c) Relaxed matching does not rescue \cwm{}.}
381	Relaxed matching (tolerating format deviations, L0--L4) \emph{decreases} \cwm{} accuracy: 58.04\%$\to$56.98\% (seed 42) and 59.09\%$\to$55.91\% (seed 123). Unparseable predictions default to the majority class (pass, 72.96\%), which outperforms the model's own parseable predictions (38--43\%). The divergence widens from 26\pp{} to 27\pp{} under relaxed matching. This rules out the hypothesis that parsing strictness inflates the observed gap. Constrained decoding~\cite{willard2023outlines} could enforce format compliance but would not address the semantic accuracy deficit among parseable outputs. An accidental training artifact provides further evidence: a \cwm{} model inadvertently trained on function-level (\cls{}-format) data achieved 86.05\% accuracy with 0\% unparseable outputs at repo level, recovering \cls{}-level performance. This confirms that the repo-level \cwm{} degradation stems entirely from trace generation complexity, not from the underlying verification task.
382	
383	\paragraph{(d) Variance compression.}
384	\cwm{}'s 5-seed standard deviation (0.37\pp{}) is lower than \cls{} (0.78\pp{}) and \traj{} (0.97\pp{}) at function level. If \cwm{} performance is capped by output-format constraints at a given complexity level, seed-to-seed variability is compressed relative to formulations whose performance depends more on learned representations.
385	
386	\paragraph{(e) Per-test precision and recall.}
387	\cls{} achieves fail \fone{} 87.59\% (precision 86.20\%, recall 89.04\%) at seed 42.% derived from overlap analysis (error_overlap_matched_seed.json); FP=130, FN=100, TP=848, TN=812
388	Multi-F2P instances (6--10 tests) reach 96.3\% accuracy, consistent with the oracle finding that per-test granularity is most valuable for complex instances.
389	
390	\paragraph{(f) Block correlation.}
391	Within-problem errors are correlated (ICC $= 0.191$, DEFF $= 3.97$, 2.81$\times$ more all-correct problems than i.i.d.\ expectation). All statistical tests use clustered bootstrap accordingly.
392	
393	\paragraph{(g) Failed interventions.}
394	We systematically tested four interventions targeting different hypothesized causes of \cwm{} repo-level degradation; all failed:
395	
396	\begin{itemize}[leftmargin=*,itemsep=1pt,topsep=2pt]
397	\item \textbf{Capacity (rank 32, $\alpha{=}64$):} $-$0.47\pp{}, within seed variance (\S\ref{app:ablations}).
398	\item \textbf{Majority voting ($K{=}3$):} $-$0.68\pp{}; 93.3\% unanimous, net flips negative (\S\ref{app:ablations}).
399	\item \textbf{Relaxed matching (L0--L4):} $-$1.06\pp{}; default-pass outperforms parseable predictions (paragraph~(c) above).
400	\item \textbf{Model scaling (4B$\to$8B):} parseable accuracy decreases (42.88\%$\to$38.52\%) while unparseable rate rises (53.7\%$\to$73.8\%); gain is a default-assignment artifact (\S\ref{sec:repo}).
401	\end{itemize}
402	
403	\noindent Each intervention targets a distinct alternative explanation (insufficient capacity, random noise, parsing strictness, model scale); the uniform failure across all four confirms the bottleneck is formulation-level: output space complexity at repo level exceeds what ${\leq}$8B generation models can handle, independent of these surface-level factors.
404	
405	\paragraph{(h) Per-mutation scaling patterns.}
406	Scaling benefits are highly non-uniform across mutation types (Table~\ref{tab:mutation_breakdown}). \texttt{off\_by\_one} shows the largest \cls{} scaling gain: 58.5\% (4B) to 86.9\% (8B, $+$28.4\pp{}). In contrast, \texttt{boundary\_removal} is scale-invariant at ${\sim}$47\% across both sizes, which marks an intrinsic difficulty ceiling. For \cwm{}, gold mutation parse rate collapses from 43.5\% (4B) to 23.9\% (8B) despite being the simplest target: generation capability degrades even for trivially correct code at larger scale within Qwen3. The val-test mutation type distribution differs notably (\texttt{operator\_swap} shifts from 19.1\% to 34.3\%; Table~\ref{tab:mutation_distribution}), but this shift does not systematically bias overall accuracy because \cls{} performance on \texttt{operator\_swap} (78.9--81.4\%) is close to the overall mean.
407	
408	\paragraph{(i) Inference efficiency.}
409	\cls{} achieves 217$\times$ higher throughput than \cwm{} at repo level (853 vs.\ 3.9 inferences/min; Qwen3-4B, RTX 5090, 100 samples, avg ${\sim}$1,040 input tokens). The speedup derives directly from the formulation: classification requires a single output token, whereas \cwm{} generates an average of 477 tokens per inference. Median latency is 48ms (\cls{}) vs.\ 16.3s (\cwm{}). At the observed unparseable rate of 73.8\% (8B), the majority of \cwm{}'s generation budget produces tokens that cannot yield a valid verdict. This \cls{}--\cwm{} efficiency gap is an inherent property of the formulation difference (1 vs.\ $O(L)$ output tokens) and should generalize across models, unlike the accuracy divergence which may be model-contingent.
410	
411	The \cls{}--\traj{} efficiency comparison is more nuanced, because \cls{} makes one call per test while \traj{} makes one call per instance. Per-call, \cls{} is 20--138$\times$ faster (depending on input length: 47ms for short contexts vs.\ 2,632ms for \traj{}). However, the per-instance effective speedup depends on test count $|T|$: at function level ($|T| \approx 2.3$), \cls{} is ${\sim}$24$\times$ faster (108ms vs.\ 2,632ms per instance); at repo level ($|T| \approx 12.3$, ${\sim}$70ms/call with longer inputs), \cls{} is ${\sim}$3$\times$ faster (861ms vs.\ 2,631ms). A crossover exists at $|T| \approx 50$ tests, beyond which \traj{}'s single-call amortization dominates. This boundary condition is informative for deployment: \cls{} is strongly preferred for function-level and moderate repo-level test suites, while extremely large test suites ($>$50 tests per instance) favor trajectory-level efficiency despite its coarser diagnostic signal.
412	
413	\paragraph{(j) Re-repair pilot.}
414	We tested whether per-test diagnostic feedback improves downstream repair. A Qwen3-8B repair agent received either per-test diagnostic signals (which specific tests failed and why) or binary accept/reject feedback, evaluated on 44 SWE-bench Verified instances. The diagnostic condition achieved accuracy no higher than the binary baseline ($A_1 = 52.3\%$, $p = 0.42$, effect size $\approx 0$). Per-test diagnostic information does not automatically translate to repair improvements at this scale. The negative result may reflect insufficient agent capability to exploit fine-grained feedback, insufficient sample size (at $n = 44$, statistical power is ${\sim}$0.3 for a medium effect size), or a genuine limitation of the diagnostic-to-repair translation.
415	
416	\paragraph{(k) Relationship to chain-of-thought verification.}
417	\cwm{} is structurally a chain-of-thought verifier: the model generates an execution trace token by token and derives its PASS/FAIL verdict from the final trace state. If intermediate reasoning improved verification, \cwm{} should outperform the reasoning-free \cls{} baseline. At function level, no such advantage materialises: \cwm{} and \cls{} are statistically equivalent (TOST $p{=}0.007$, $\pm$2\pp{} margin; \S\ref{sec:equivalence}), indicating that the additional trace generation provides no accuracy benefit over direct binary classification. At repo level, the chain-of-thought mechanism actively \emph{hurts}: trace generation triggers format collapse (53--74\% unparseable), and even parseable traces yield accuracy below the majority baseline (38--43\% vs.\ 72.96\%; paragraph~(c)). Four targeted interventions fail to rescue the generation pathway (paragraph~(g)). Within the ${\leq}$8B LoRA regime, chain-of-thought--style verification does not outperform direct classification for execution prediction. Whether execution-trace pretraining at larger scale~\cite{meta2025cwm} changes this conclusion remains the primary open question (\S\ref{sec:threats}).
418	
419	\section{TOST Margin Sensitivity}
420	\label{app:tost_sensitivity}
421	
422	Table~\ref{tab:tost_sensitivity} reports the TOST equivalence $p$-value as a function of the equivalence margin, computed on the 5-seed variant-level \cls{}--\cwm{} comparison (gap $= 1.24$\pp{}, 523 variants, 114 clusters, clustered bootstrap).
423	
424	\begin{table}[h]
425	\centering
426	\small
427	\caption{TOST margin sensitivity for \cls{}--\cwm{} variant-level equivalence (5 seeds, 523 variants, 114 clusters). The smallest margin achieving equivalence at $\alpha = 0.05$ is $\pm$1.52\pp{}.}
428	\label{tab:tost_sensitivity}
429	\setlength{\tabcolsep}{4pt}
430	\begin{tabular}{ccc}
431	\toprule
432	\textbf{Margin ($\pm$\pp{})} & \textbf{$p$-value} & \textbf{Equivalent ($\alpha{=}0.05$)?} \\
433	\midrule
434	1.0 & $\gg$0.05 & No \\
435	1.5 & 0.054 & No (borderline) \\
436	\textbf{1.52} & ${\sim}$\textbf{0.05} & \textbf{Smallest margin} \\
437	1.71 & 0.027 & Yes \\
438	2.0 & 0.007 & Yes \\
439	3.0 & $4.6{\times}10^{-5}$ & Yes \\
440	5.0 & $\ll$0.001 & Yes \\
441	\bottomrule
442	\end{tabular}
443	\end{table}
444	
445	Figure~\ref{fig:tost_sensitivity} visualises the margin--$p$-value relationship for both comparisons.
446	
447	\begin{figure}[h]
448	\centering
449	\includegraphics[width=\columnwidth]{figures/paper/fig_tost_sensitivity.pdf}
450	\caption{TOST $p$-value as a function of equivalence margin. \cls{}--\cwm{} (blue) achieves equivalence at $\pm$1.52\pp{}; \cls{}--\traj{} (green) crosses $\alpha{=}0.05$ near $\pm$1.8\pp{} but does not survive Holm correction. Log scale.}
451	\label{fig:tost_sensitivity}
452	\end{figure}
453	
454	The minimum equivalence margin is $\pm$1.52\pp{}, 0.48\pp{} below our pre-specified $\pm$2\pp{} threshold. The $\pm$2\pp{} threshold was set based on deployment relevance rather than observed data: at function-level accuracy (85--88\%), a 2\pp{} per-test difference corresponds to ${\sim}$38 additional errors across 1,890 tests (${\sim}$2--3 problems out of 114), comparable in magnitude to between-seed standard deviation (0.37--0.97\pp{}) and checkpoint selection noise ($<$1\pp{}). Differences within this range do not reliably distinguish formulations from training noise in pipeline selection decisions. For \cls{}--\traj{}, the TOST at $\pm$2\pp{} yields $p{=}0.025$, nominally significant but not surviving Holm-Bonferroni correction at $k{=}5$ (adjusted $p{=}0.075$; Table~\ref{tab:holm}). The one-sided decomposition reveals the binding constraint: $p_{\text{upper}}{=}0.005$ ($\Delta < {+}2$\pp{} is well-confirmed) while $p_{\text{lower}}{=}0.025$ ($\Delta > {-}2$\pp{}) limits the overall TOST, consistent with \cls{} having mildly higher accuracy.
455	
456	\paragraph{Robustness: seed-level vs.\ clustered bootstrap TOST.}
457	The primary TOST $p$-values use seed-level paired analysis (df${=}$4), treating each training seed as the unit of replication (\S\ref{sec:setup}). Under problem-level clustered bootstrap (resampling 114 problem clusters, 10K iterations), the \cls{}--\traj{} raw TOST $p$ decreases to ${\sim}$0.007 (Holm-adjusted $p{\approx}0.021$), which would confirm equivalence. We report the more conservative seed-level result ($p{=}0.025$, adjusted $p{=}0.075$) as primary, since training seeds are the true unit of replication; problem-level bootstrap pools within-seed observations and may understate between-seed uncertainty. For \cls{}--\cwm{}, both methods confirm equivalence ($p \leq 0.010$), so the choice does not affect conclusions.
458	
459	\subsection{Bayesian ROPE Analysis}
460	\label{app:bayesian_rope}
461	To complement the frequentist TOST, we conduct a Bayesian equivalence analysis using a paired $t$-test with Jeffreys prior~\cite{kruschke2013bayesian,kruschke2018rejecting}. The marginal posterior for the mean accuracy difference follows a $t$-distribution with $n{-}1$ degrees of freedom. For \cls{}--\cwm{}, the posterior probability within the $\pm$2\pp{} ROPE is $P(\text{ROPE}) = 0.975$, and the 95\% highest density interval (HDI $= [{+}0.10, {+}2.00]$\,pp) falls entirely inside the ROPE, confirming equivalence under both continuous and HDI-based decision criteria. For \cls{}--\traj{} at per-test level, $P(\text{ROPE}) = 0.542$ (inconclusive; 95\% HDI $= [{+}0.35, {+}3.52]$\,pp extends beyond the ROPE), consistent with the TOST inconclusive result after Holm correction ($p_{\text{adj}} = 0.075$). At variant level, \cls{}--\traj{} equivalence is supported by the Bayesian criterion ($P(\text{ROPE}) = 0.970$, HDI $= [{-}2.00, {+}1.03]$\,pp), but the frequentist TOST remains inconclusive after Holm-Bonferroni correction ($p_{\text{adj}} = 0.075$; Table~\ref{tab:holm}). This discrepancy reflects differing treatments of multiplicity: Bayesian ROPE evaluates each comparison independently, while Holm correction penalizes across all $k{=}5$ primary tests. For \cls{}--\cwm{}, both frameworks agree (TOST $p_{\text{adj}}{=}0.028$, $P(\text{ROPE}){=}0.975$); for \cls{}--\traj{} per-test, both are inconclusive. We conservatively follow the Holm-corrected TOST in the main text and report \cls{}--\traj{} equivalence as inconclusive.
462	
463	\paragraph{14B scaling evidence.} At 14B (3 seeds), the \cls{}--\cwm{} gap narrows to 0.43\pp{} and the \cls{}--\traj{} gap to 1.07\pp{}, both within the $\pm$2\pp{} margin. Seed-level TOST (df${=}$2) is inconclusive for equivalence in both pairs ($p{=}0.076$ for \cls{}--\cwm{}, $p{=}0.187$ for \cls{}--\traj{}), reflecting the severe power limitation of 3-seed comparisons (power ${\sim}$0.08 at $\pm$2\pp{} margin with df${=}$2). Bayesian ROPE provides moderate support: $P(\text{ROPE}){=}0.887$ for \cls{}--\cwm{} and $P(\text{ROPE}){=}0.780$ for \cls{}--\traj{}. Under problem-level clustered bootstrap, both comparisons reach significance ($p{=}0.0006$ and $p{=}0.043$ respectively), but this analysis treats within-seed observations as exchangeable, potentially understating between-seed uncertainty. The monotonic gap reduction (3.11\pp{} at 4B $\to$ 2.24\pp{} at 8B $\to$ 1.07\pp{} at 14B) favors a capacity-dependent convergence interpretation, though formal confirmation at seed level requires more training seeds.
464	
465	
466	\section{Variant-Level Effect Sizes}
467	\label{app:power}
468	
469	Table~\ref{tab:variant_power} reports variant-level bootstrap confidence intervals for the repo-level formulation comparisons ($n{=}48$ variants). Following Hoenig and Heisey~\cite{hoenig2001}, we report minimum detectable effect (MDE) rather than post-hoc observed power.
470	
471	\begin{table}[h]
472	\centering
473	\small
474	\caption{Variant-level bootstrap analysis ($n{=}48$). \cls{}--\cwm{} uses paired bootstrap (same variants, same seed); \cls{}--\traj{} uses unpaired bootstrap (per-variant \traj{} predictions not archived for pairing). MDE at $n{=}48$: ${\sim}$25\pp{}.}
475	\label{tab:variant_power}
476	\setlength{\tabcolsep}{3pt}
477	\resizebox{\columnwidth}{!}{%
478	\begin{tabular}{llccc}
479	\toprule
480	\textbf{Comparison} & \textbf{Config} & \textbf{$\Delta$ (\pp{})} & \textbf{95\% CI} & \textbf{$p$} \\
481	\midrule
482	\multicolumn{5}{l}{\emph{\cls{} vs.\ \cwm{} (paired)}} \\
483	& Qwen3-8B & +29.17 & [10.42, 47.92] & 0.003 \\
484	& DeepSeek-6.7B & +35.42 & [18.75, 50.05] & ${<}$0.001 \\
485	\midrule
486	\multicolumn{5}{l}{\emph{\cls{} vs.\ \traj{} (unpaired)}} \\
487	& Qwen3-4B & $-$4.17 & wide & 0.740 \\
488	& Qwen3-8B & +8.33 & wide & 0.385 \\
489	& DeepSeek-6.7B & 0.00 & wide & 1.000 \\
490	\bottomrule
491	\end{tabular}}
492	\end{table}
493	
494	At $n{=}48$, the MDE is ${\sim}$25\pp{}. The \cls{}--\cwm{} gap (29--35\pp{}) exceeds this threshold, confirming that $n{=}48$ is sufficient to detect the observed divergence. The \cls{}--\traj{} gaps ($<$10\pp{}) fall well below the MDE: any true difference is too small to detect at this sample size, consistent with the function-level TOST equivalence (\S\ref{sec:equivalence}).
495	
496	The \cls{}--\traj{} unpaired bootstrap produces wider confidence intervals than paired analysis would; \traj{} per-variant predictions were not archived in a format that permits pairing. The \cls{}--\cwm{} paired comparison uses \cls{} s123 vs.\ \cwm{} s42 (different seeds), but the CI lower bound of 10.42\pp{} far exceeds the seed noise observed in function-level experiments ($<$2\pp{}).
497	
498	
499	\section{Multiple Comparison Correction}
500	\label{app:holm}
501	
502	Table~\ref{tab:holm} applies Holm-Bonferroni correction~\cite{holm1979} to the five primary statistical comparisons across this study ($k{=}5$, family-wise $\alpha{=}0.05$).
503	
504	\begin{table}[h]
505	\centering
506	\small
507	\caption{Holm-Bonferroni correction for primary comparisons ($k{=}5$). Comparisons ranked by raw $p$-value; each tested against $\alpha / (k - \text{rank} + 1)$.}
508	\label{tab:holm}
509	\setlength{\tabcolsep}{3pt}
510	\resizebox{\columnwidth}{!}{%
511	\begin{tabular}{clcccc}
512	\toprule
513	\textbf{Rank} & \textbf{Comparison} & \textbf{Raw $p$} & \textbf{Factor} & \textbf{Adj $p$} & \textbf{Sig.?} \\
514	\midrule
515	1 & Repo: \cls{} vs \cwm{} & 0.003 & $\times$5 & 0.015 & \checkmark \\
516	2 & Func: \cls{} vs \cwm{} (TOST $\pm$2\pp{}) & 0.007 & $\times$4 & 0.028 & \checkmark \\
517	3 & Func: \cls{} vs \traj{} (TOST $\pm$2\pp{}) & 0.025 & $\times$3 & 0.075 & --- \\
518	4 & Repo: \cwm{} vs \traj{} & 0.039 & $\times$2 & 0.078 & --- \\
519	5 & Repo: \cls{} vs \traj{} & 0.385 & $\times$1 & 0.385 & --- \\
520	\bottomrule
521	\end{tabular}}
522	\end{table}
523	
524	The two core claims survive correction: the repo-level \cls{}--\cwm{} divergence (adjusted $p{=}0.015$) and function-level \cls{}--\cwm{} equivalence (adjusted $p{=}0.028$). The function-level \cls{}--\traj{} equivalence does not survive correction (adjusted $p{=}0.075$). Under problem-level clustered bootstrap, the raw TOST $p$ decreases to ${\sim}$0.007 (adjusted $p{\approx}0.021$), which would confirm equivalence; we report the more conservative seed-level result ($p{=}0.025$) as primary, since training seeds are the true unit of replication.
525	
526	\section{Mixed-Effects Regression}
527	\label{app:interaction}
528	
529	We fit mixed-effects linear probability models (LPM) with heteroskedasticity-robust standard errors (HC1) to test the formulation$\times$complexity interaction formally~\cite{moulton1990}. We choose LPM because coefficients are directly interpretable as probability differences (percentage points), consistent with the reporting units in the main text; at these sample sizes ($n{\approx}56$K cross-complexity, repo-level pooled cross-model) and base rate range (0.6--0.9), LPM and logistic regression yield concordant conclusions for all primary effects~\cite{angrist2009mostly} (confirmed below).
530	
531	\paragraph{Cross-complexity model (DeepSeek-Coder).} \texttt{correct $\sim$ formulation $\times$ complexity + (1|problem\_id)}, $n{=}56{,}480$ observations (\cls{} + \cwm{} $\times$ function + repo), 139 problem clusters. The \cwm{} main effect at function level is non-significant ($\hat{\beta}{=}-0.002$, $z{=}-0.25$, $p{=}0.805$); the \cwm{}$\times$repo interaction is highly significant ($\hat{\beta}{=}-0.219$, $z{=}-23.7$, $p{<}0.001$). \cwm{} and \cls{} are statistically indistinguishable at function level ($\Delta{=}-0.2$\pp{}, $p{=}0.805$) but diverge by 22\pp{} at repo level, confirming the complexity-dependent divergence is not an artifact of aggregation.
532	
533	\paragraph{Repo-level cross-model model.} \texttt{correct $\sim$ formulation $\times$ model + (1|problem\_id)}, both model families, repo level only. \cwm{} deficit: $\hat{\beta}{=}-0.22$ ($-$22\pp{}, $z{=}-64.4$, $p{<}0.001$). Model effect: +1.1\pp{} for Qwen3 ($z{=}3.1$, $p{=}0.002$ in LPM; not significant under GEE, $p{=}0.449$). Formulation$\times$model interaction: +1.6\pp{} less \cwm{} degradation on Qwen3 ($z{=}2.8$, $p{=}0.006$ in LPM; not significant under GEE, $p{=}0.860$). Formulation dominates the predictable variance; model identity is directionally positive but specification-dependent. The 25-cluster random intercept structure limits effective degrees of freedom for the random effects; inferences on fixed effects (formulation, complexity) are robust as they pool across the full observation count.
534	
535	\paragraph{Logistic regression robustness check.} To verify that LPM conclusions are not artifacts of the linear link function, we fit GEE logistic regression (binomial family, exchangeable working correlation, robust sandwich standard errors) to the same data. For the cross-complexity model, the \cwm{} main effect at function level has OR$=$0.98 (95\% CI [0.86, 1.12], $p{=}0.771$) and the \cwm{}$\times$repo interaction has OR$=$0.31 ([0.15, 0.65], $p{=}0.002$). Average marginal effects are $-$0.2\pp{} (function) and $-$21.6\pp{} (repo), matching LPM coefficients within 0.3\pp{}. For the cross-model model, the \cwm{} deficit has OR$=$0.30 ([0.15, 0.63], $p{=}0.001$, AME$=$\,$-$21.1\pp{}). Direction, magnitude, and significance of all primary effects are concordant between LPM and logistic regression; minor discrepancies in secondary effects (model identity, formulation$\times$model interaction: $p{=}0.449$ and $p{=}0.860$ under GEE vs.\ $p{=}0.002$ and $p{=}0.006$ under LPM) reflect the GEE's more conservative cluster-robust inference with $k{=}25$ clusters. The discrepancy in secondary effects reflects cluster count: the cross-complexity model ($k{=}139$) yields reliable sandwich SEs, while the cross-model model ($k{=}25$) falls below the $k{\geq}40$ threshold recommended for stable cluster-robust inference~\cite{cameron2008bootstrap}.
536	
537	\section{CWM Parseable Bias Analysis}
538	\label{app:parseable_bias}
539	
540	Figure~\ref{fig:cwm_unparseable} summarises the unparseable rate contrast across complexity levels.
541	
542	\begin{figure}[h]
543	\centering
544	\includegraphics[width=\columnwidth]{figures/paper/fig_cwm_unparseable.pdf}
545	\caption{\cwm{} unparseable rate by complexity level. Function-level outputs (${\sim}$5--15 tokens) yield 1.4\% unparseable; repo-level outputs (${\sim}$477 tokens) reach 53.7\% (4B) and 73.8\% (8B). Parseable-only accuracy (inside bars) decreases from 4B to 8B despite rising overall accuracy, confirming default-assignment inflation.}
546	\label{fig:cwm_unparseable}
547	\end{figure}
548	
549	The default-to-pass assignment for unparseable \cwm{} outputs is not random with respect to instance difficulty. Unparseable instances have significantly higher pass rates than parseable ones (74.6\% vs.\ 68.3\%, $\chi^2$ $p = 5.9 \times 10^{-10}$), and \cls{} models achieve higher accuracy on unparseable instances (86.4\% vs.\ 79.1\%, $p = 3.3 \times 10^{-18}$). This indicates that \cwm{}'s parsing failures concentrate on simpler, pass-heavy instances where the majority-class default happens to be correct more often. Cross-model Jaccard overlap of unparseable instance sets is 0.46, confirming this pattern is instance-driven (specific inputs consistently cause parsing failure across models) rather than stochastic. The net effect is that \cwm{}'s reported accuracy is inflated by default-correct assignments on easy instances, while its effective discriminative accuracy on harder instances is substantially lower than the aggregate figure suggests.
550	
551	
552	\section{Threats to Validity (Full Analysis)}
553	\label{app:threats}
554	
555	We identify five potential confounds and assess their impact on our conclusions.
556	
557	\paragraph{Checkpoint selection.} Val-based selection is unavailable for runs with NaN validation loss (DeepSeek \cwm{} repo-level runs, DeepSeek \cls{} s123), which default to the final epoch checkpoint. A checkpoint ablation on Qwen3-8B \cls{} s42 quantifies this confound: epoch~1 (ckpt-2200) achieves 85.34\%, val-selected (ckpt-3600) 84.48\%, and final epoch (ckpt-6633) 85.29\%, a $<$1\pp{} range. The val-selected checkpoint is the lowest, indicating no upward bias from checkpoint selection. The Qwen3-8B \traj{} comparison (epoch 2: 72.92\% vs.\ epoch 3: 70.83\%) shows a slightly larger ${\sim}$2\pp{} shift. For \cwm{}, the convergence analysis (Appendix~\ref{app:cwm_convergence}) shows eval loss at the final epoch is 1.8$\times$ its minimum; however, early-stopped checkpoints retain high unparseable rates, leaving the qualitative ranking unchanged.
558	
559	\paragraph{\cwm{} convergence analysis.}
560	\label{app:cwm_convergence}
561	Qwen3-8B \cwm{} repo-level eval loss reaches its minimum within ${\sim}$5\% of training (step 300--400 of 6{,}633) and increases monotonically thereafter, with no plateau or recovery (Table~\ref{tab:cwm_convergence}). This pattern is consistent across all three seeds, confirming systematic overfitting to trace generation rather than stochastic variation. The final-epoch eval loss is ${\sim}$1.8$\times$ the optimal value. By contrast, function-level \cwm{} achieves \cls{}-equivalent accuracy (TOST $p{=}0.007$) with the same training recipe, indicating that the overfit is specific to repo-level output complexity. Cross-model validation: a DeepSeek-Coder early-stopped checkpoint (s123, epoch~1) achieves 75.45\% versus 57.31\% at epoch~3 (s123; +18.14\pp{}), but retains 66.4\% unparseable rate, confirming that format collapse emerges early and is not a late-training artifact. No epoch-level checkpoint is available for Qwen3 CWM (only step-level checkpoints at steps 300/400 and late steps ${\geq}$5800; continuous epoch checkpointing was not enabled for this training run). The convergence analysis (Table~\ref{tab:cwm_convergence}) shows eval loss minimum at step 300--400 across all three Qwen3 seeds, consistent with DeepSeek-Coder's epoch-1 improvement, providing cross-model evidence that the overtraining pattern generalizes. An early checkpoint (step 400, ${\sim}$6.5\% of training, s42) yields 65.17\% repo-level accuracy with 63.7\% unparseable rate, comparable to or below final-epoch performance (66.93--67.33\% accuracy, 60.4--63.9\% unparseable; s123/s456 at step 6633). This rules out late-training format degradation: collapse is present from early training, and the optimal eval-loss checkpoint does not recover repo-level accuracy. A later checkpoint (step 6100, s42, seq8192) achieves 69.50\% test accuracy despite substantially higher validation loss than val-best ckpt-400 (64.36\%), suggesting that validation loss may not be a reliable proxy for test-set performance in \cwm{} repo-level evaluation.
562	
563	\begin{table}[h]
564	\centering
565	\small
566	\caption{\cwm{} repo-level eval loss across training (Qwen3-8B, 3 seeds). Minimum is reached at step 300--400 (${\sim}$5\% of training); subsequent training monotonically increases loss.}
567	\label{tab:cwm_convergence}
568	\begin{tabular}{lccc}
569	\toprule
570	Step & s42 & s123 & s456 \\
571	\midrule
572	300 & 0.291 & \textbf{0.288} & \textbf{0.277} \\
573	400 & \textbf{0.286} & 0.306 & 0.283 \\
574	1000 & 0.333 & 0.336 & 0.351 \\
575	3000 & 0.445 & 0.453 & 0.435 \\
576	6600 & 0.521 & 0.517 & 0.507 \\
577	\bottomrule
578	\end{tabular}
579	\end{table}
580	
581	\paragraph{Evaluation sequence length.} \cwm{} accuracy varies by ${\sim}$9\pp{} across evaluation sequence lengths for the same checkpoint (seq2048: ${\sim}$65\% vs.\ seq4096: ${\sim}$56\%), driven by unparseable-rate differences that propagate through majority-class default assignment. \cls{} is invariant to this parameter. Cross-model \cwm{} comparisons use different eval lengths (Qwen3: 8192, DeepSeek: 4096) and are not directly comparable in absolute terms. A matched-sequence evaluation shows ${\sim}$1.5\pp{} difference for \cls{} (Appendix~\ref{app:ablations}), insufficient to explain the 18--26\pp{} gap. Furthermore, increasing Qwen3-8B \cwm{} evaluation from seq4096 to seq8192 \emph{raises} the unparseable rate (63.7\%$\to$73.8\%) while changing accuracy by only 0.81\pp{} (64.36\%$\to$65.17\%); giving the model more generation budget worsens format compliance rather than improving it, confirming that format collapse is a structural bottleneck rather than a truncation artifact. Practitioners must standardize evaluation sequence length for generation-based formulations.
582	
583	\paragraph{Preprocessing.} DeepSeek \cls{} accuracy ranges from 82.61\% (s42, drop preprocessing) to 74.93\% (s123, truncate preprocessing), a 7.68\pp{} spread that conflates preprocessing strategy, checkpoint selection method, and seed. The two strategies produce different effective training sets (67,343 vs.\ 70,748 samples) and different checkpoint selection regimes. The qualitative ranking \cls{} $>$ \cwm{} holds under both strategies (Table~\ref{tab:taxonomy}).
584	
585	\paragraph{\traj{} training regime.} \traj{} uses a different training configuration: smaller training set (${\sim}$400 repo-level variants vs.\ ${\sim}$70K per-test instances), higher learning rate ($2{\times}10^{-4}$ vs.\ $5{\times}10^{-5}$), and variant-level labels. This asymmetry is inherent to the formulation (trajectory-level labels are only available at variant granularity), but precludes training-data-controlled comparison at repo level. The downsample ablation confirms the \cls{} formulation advantage persists at matched data volume (80.74\% vs.\ 72.92\%; Appendix~\ref{app:downsample}), though it controls for training volume but not label granularity (per-test vs.\ variant-level). Crucially, \traj{} achieves statistical equivalence with \cls{} at function level (${\leq}$1.3\pp{}, \S\ref{sec:func_results}), demonstrating the formulation itself is viable; the repo-level gap attribution remains uncertain: data volume (${\sim}$400 variants vs.\ ${\sim}$70K per-test instances) and label granularity (variant-level vs.\ per-test) are both plausible confounds that cannot be separately controlled.
586	
587	\paragraph{\cwm{} scale and pretraining.} Our \cwm{} baseline uses 4--8B LoRA fine-tuning without execution trace pretraining. The original Code World Model~\cite{meta2025cwm} uses 32B parameters with mid-training on execution traces, a fundamentally different training regime. At larger scale or with execution-trace pretraining, the generation bottleneck observed here may diminish: larger models produce more coherent long-form outputs, and execution trace exposure may improve output format compliance. This is the primary limitation: all repo-level \cwm{} conclusions are conditional on the ${\leq}$8B LoRA regime.
588	
589	Despite these confounds, the repo-level \cls{}--\cwm{} gap (18--26\pp{}) exceeds any single assessed confound. Even under worst-case compounding (${\sim}$11.5\pp{}), the gap retains ${\geq}$7.5\pp{} margin; confounds predominantly disadvantage \cwm{}. However, correlated confounds and limited seed coverage mean definitive causal attribution requires multi-seed replication. At $n{=}48$, the minimum detectable effect (MDE) is ${\sim}$25\pp{}~\cite{hoenig2001}; the \cls{}--\cwm{} gap (29--35\pp{}) exceeds this threshold, while the \cls{}--\traj{} gap ($<$10\pp{}) falls below it, consistent with our TOST equivalence finding. Holm-Bonferroni correction across the five primary comparisons ($k{=}5$; Table~\ref{tab:holm}) confirms the \cls{}--\cwm{} gap (adjusted $p{=}0.015$) and function-level \cls{}--\cwm{} equivalence (adjusted $p{=}0.028$); function-level \cls{}--\traj{} equivalence does not survive correction (adjusted $p{=}0.075$), nor does the repo-level \cwm{}--\traj{} comparison (adjusted $p{=}0.078$). The consistent direction across both model families and all tested configurations supports a formulation-level explanation, though definitive causal attribution requires future experiments addressing each confound individually.
590	
591	
592	\paragraph{Extended validity discussion.}
593	\label{app:limitations}
594	The same-size 4B comparison uses a single seed; \cls{} 4B seed 123 (val-best ckpt-800) achieves only 75.33\% test accuracy (+2.4\pp{} above majority baseline); val-best selection at an early checkpoint (step 800) amplifies the val-test distribution shift observed across all configurations. The \cwm{} 8B comparison uses 3 seeds per model. The validation and test sets have zero problem overlap but differ in mutation type composition (Table~\ref{tab:mutation_distribution}): \texttt{operator\_swap} shifts from 19.1\% (val) to 34.3\% (test), the largest single-type distribution mismatch (+15.2\pp{}). All repo-level results use val-selected checkpoints, and checkpoint selection variance could contribute to observed differences. Our training data is synthetically constructed from mutation operators rather than real developer patches. While mutation testing literature establishes that mutants are reasonable proxies for real faults in test effectiveness studies~\cite{andrews2005mutation,just2014mutants}, these findings concern mutation \emph{adequacy} (whether tests that kill mutants also detect real faults), not whether verifiers trained on mutants transfer to real patches. However, the coupling effect underlying these results supports \emph{relative ranking} validity: a domain shift from synthetic mutations to real bugs may affect absolute accuracy levels, but our core finding (that formulation choice matters at repo level but not function level) concerns relative performance ordering, which is expected to be preserved under distributional shifts that affect all formulations equally. The synthetic-to-real transfer gap for absolute accuracy remains untested. The \traj{} training configuration differs from \cls{}/\cwm{}: smaller training set (${\sim}$400 vs.\ ${\sim}$70K instances), different learning rate ($2{\times}10^{-4}$ vs.\ $5{\times}10^{-5}$), and variant-level evaluation ($n{=}48$ vs.\ per-test $n{=}9{,}784$). The function-level \cls{}--\traj{} TOST equivalence ($p = 0.025$, seed-level paired, $\pm$2\pp{}) is computed on 523 matched variant-level instances across 5 seeds; 2 of 5 seeds use NF4 quantization. Restricting to three bfloat16 seeds yields a comparable mean gap ($-$0.45\pp{}) but wider confidence interval (df${=}$2); the TOST $p$-value increases to 0.128, which reflects reduced statistical power rather than a shift in the point estimate. The NF4 seeds contribute precision (narrowing the CI) without shifting the mean, consistent with precision being comparable across both quantization levels at function level. Repo-level \cls{}--\traj{} comparison should be interpreted with caution due to configuration and granularity differences.
595	
596	\paragraph{Domain contrast with generative verification in math reasoning.}
597	GenRM~\cite{hosseini2025genrm} demonstrates that generative verifiers outperform discriminative ones for math reasoning. Our results reveal a domain-specific divergence: in code repair verification, the generative formulation (\cwm{}) does not outperform the discriminative one (\cls{}), and degrades sharply at repository level. The key difference is output space structure: math reasoning generates natural-language solution traces with flexible formatting, whereas code execution output requires exact syntactic compliance (specific variable values, error messages, stack traces). This structural constraint makes format collapse, absent in math verification, the dominant failure mode for code \cwm{} at repo level (53--74\% unparseable). The domain contrast suggests that the generative verification advantage is contingent on output space complexity rather than being a universal property of verifier architecture.
598	
599	\section{Use of AI Assistants}
600	\label{app:ai-assistants}
601	
602	We used Claude (Anthropic) as an AI coding and writing assistant throughout this work. Specifically:
603	\begin{itemize}
604	    \item \textbf{Code:} drafting experiment scripts, data-processing pipelines, and analysis utilities; debugging and refactoring.
605	    \item \textbf{Writing:} drafting and revising paper sections, polishing prose, and reformatting \LaTeX{}.
606	    \item \textbf{Literature:} summarizing related papers to inform the related-work section.
607	\end{itemize}
608	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1e83d7f2-3374-4643-9e1c-521c91c6de8f",
  "isSidechain": false,
  "promptId": "15e99bee-64bb-4bc0-b559-9e40ffdfc882",
  "type": "user",
  "uuid": "a64c8b7d-e8d9-4b9e-96b4-908322e3ccb0",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/appendix.tex",
      "content": "\\appendix\n\n\\noindent\\textbf{Appendix overview.} A: Oracle analysis. B: Ablations. C: Per-mutation breakdown. D: Variant-level accuracy. E: Hyperparameters. F: Prompt templates. G: Mutation distribution. H: Qualitative errors. I: Extended analysis (I.a--I.k). J: TOST sensitivity (J.1: Bayesian ROPE). K: Effect sizes. L: Holm-Bonferroni. M: Mixed-effects regression. N: Parseable bias. O: Threats (O.1: CWM convergence; O.2: Extended validity). P: AI assistants.\n\n\\section{Oracle Accuracy-Utility Analysis}\n\\label{app:oracle}\n\nWe stratify SWE-bench Verified instances by Fail-to-Pass (F2P) test count $T$, comparing per-test vs.\\ trajectory-level oracle resolve rates under i.i.d.\\ and block-correlated error models (ICC $= 0.191$, from function-level analysis; \\S\\ref{sec:equivalence}).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Oracle accuracy-utility frontier: per-test advantage stratified by F2P test count ($T$) on SWE-bench Verified (500 instances). Block-correlated model uses function-level ICC $= 0.191$ (from function-level analysis, \\S\\ref{sec:equivalence}). Pass-to-Pass (P2P) regression rate: 1.04\\% mean, 0\\% median.}\n\\label{tab:oracle}\n\\resizebox{\\columnwidth}{!}{%\n\\setlength{\\tabcolsep}{3pt}\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{$T$} & \\textbf{Inst.\\%} & \\textbf{i.i.d.\\ (\\pp{})} & \\textbf{Block (\\pp{})} & \\textbf{Contrib.\\%} \\\\\n\\midrule\n$1$ & 68.7 & $-$0.04 & $-$0.09 & $\\approx$0 \\\\\n$2$ & 19.1 & 18.49 & 31.69 & 55.3 \\\\\n$3$--$5$ & 7.1 & 25.00 & 40.74 & $\\approx$26 \\\\\n$\\geq 6$ & 5.1 & 30.00 & 40.06 & $\\approx$19 \\\\\n\\midrule\n\\textbf{All} & 100.0 & --- & \\textbf{10.93} & 100.0 \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/paper/fig3_oracle_stratified.pdf}\n\\caption{Oracle per-test advantage by F2P test count $T$. Advantage is zero at $T{=}1$ (68.7\\%) and concentrates at $T{=}2$ (19.1\\%, contributing 55.3\\% of total advantage). Note: $y$-axis does not start at zero.}\n\\label{fig:oracle_stratified}\n\\end{figure}\n\nTable~\\ref{tab:oracle} and Figure~\\ref{fig:oracle_stratified} reveal a sharp concentration: at $T = 1$ (68.7\\% of instances), per-test and trajectory-level are informationally equivalent. The advantage materializes at $T = 2$ (19.1\\%), where block-correlated advantage reaches 31.69\\pp{} (55.3\\% of total). The overall block-correlated advantage is 10.93\\pp{}, driven by the $T \\geq 2$ minority. Block correlation amplifies relative to i.i.d.: at $T = 2$, 31.69\\pp{} vs.\\ 18.49\\pp{} (1.7$\\times$). P2P regression is negligible (1.04\\% mean, 0\\% median); the practical value concentrates in F2P discrimination.\n\n\\paragraph{Sensitivity to ICC estimate.}\nThe analysis above uses ICC $= 0.191$ from function-level analysis (\\S\\ref{sec:equivalence}), where mean cluster size $\\bar{k} \\approx 16.5$ yields DEFF $= 3.97$. At repository level, within-problem correlation is substantially stronger: ICC $= 0.3146$ with DEFF $= 114.4$ (\\S\\ref{sec:repo}), yielding an effective sample size of $n_{\\text{eff}} \\approx 9{,}784 / 114.4 \\approx 86$ independent observations~\\cite{moulton1990}, still sufficient for regression but limiting precision of variance component estimates. This is a consequence of the larger and more heterogeneous test suites in SWE-bench Verified problems. Under higher ICC, within-problem errors cluster more tightly and amplify the block-correlated per-test advantage at each $T$ stratum; the correction from i.i.d.\\ to block-correlated grows monotonically with ICC. The function-level ICC $= 0.191$ used in Table~\\ref{tab:oracle} thus provides a conservative lower bound on the per-test advantage. The repo-level correlation structure would yield an even larger gap between per-test and trajectory-level oracle resolve rates, which strengthens the case for per-test granularity at repository-level complexity.\n\n\\section{Ablation Studies}\n\\label{app:ablations}\n\n\\paragraph{LoRA rank sensitivity.}\nAll \\cwm{} experiments use LoRA rank $r{=}16$. To test whether this capacity constraint handicaps \\cwm{}, we train rank-32 variants (seed 42), doubling adapter parameters.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{LoRA rank ablation for \\cwm{} 4B (seed 42, 3 epochs, lr $= 2{\\times}10^{-4}$). Rank-16 seed variance: 0.53\\pp{} (seeds 42 vs.\\ 456).}\n\\label{tab:rank_ablation}\n\\setlength{\\tabcolsep}{4pt}\n\\begin{tabular}{lccccc}\n\\toprule\n\\textbf{Config} & \\textbf{$\\alpha/r$} & \\textbf{Acc (\\%)} & \\textbf{Fail \\fone{}} & \\textbf{Pass \\fone{}} & \\textbf{$\\Delta$} \\\\\n\\midrule\n$r{=}16$, $\\alpha{=}32$ & 2 & \\textbf{87.51} & --- & --- & --- \\\\\n$r{=}32$, $\\alpha{=}32$ & 1 & 87.00 & 87.1 & 86.9 & $-$0.51 \\\\\n$r{=}32$, $\\alpha{=}64$ & 2 & 87.04 & 87.27 & 86.79 & $-$0.47 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nBoth rank-32 variants fall within the 2-seed variance of the rank-16 baseline (0.53\\pp{} between seeds 42 and 456; Table~\\ref{tab:rank_ablation}). The $\\alpha{=}64$ variant (matching the baseline $\\alpha/r{=}2$ ratio) rules out the confound that the $\\alpha{=}32$ result might reflect reduced effective scaling rather than rank insensitivity. This is consistent with \\cwm{}'s function-level performance being bounded by output-format constraints rather than adapter capacity.\n\n\\paragraph{Majority voting.}\nMajority voting ($K{=}3$) decreases accuracy from 87.51\\% to 86.83\\% ($-$0.68\\pp{}): errors are systematic rather than stochastic, so sampling-based ensembles do not help.\n\n\\paragraph{Sequence-length ablation details.}\nBoth formulations are trained with \\texttt{max\\_seq\\_length}$=$2,048. At inference, \\cwm{} reserves \\texttt{max\\_new\\_tokens}$=$512, leaving ${\\sim}$1,536 effective input tokens; \\cls{} allocates nearly all context to input (5,120--8,192 tokens). A matched-context ablation (\\cls{} 8B at 2,048 tokens) achieves 83.04\\%, only 1.44\\pp{} below the 8,192-token evaluation (84.48\\%), though truncation introduces 136 unparseable outputs (1.39\\% of test samples). The matched-context gap (\\cls{}@2,048 vs.\\ \\cwm{}@2,048) is 25.00\\pp{} (98\\% of the full 25.59\\pp{} gap), confirming that input context disparity explains at most 3\\% of the difference.\n\n\\paragraph{Training data size control.}\n\\label{app:downsample}\nTo control for the training set size asymmetry between \\cls{} (${\\sim}$70K instances) and \\traj{} (386 variant-level instances, ${\\sim}$8K per-test equivalents, at repo level), we downsample \\cls{} training data to match \\traj{} in data volume. Downsampled \\cls{} (Qwen3-4B, seed 42) achieves 80.74\\% repo-level per-test accuracy, only 2.89\\pp{} below the full-data \\cls{} (83.63\\%) and still 7.82\\pp{} above \\traj{} (72.92\\%). The \\cls{} formulation advantage is not attributable to training data volume.\n\nAt function level, the relationship reverses: \\traj{} uses 8,052 variant-level instances (2.24$\\times$ more unique variants than \\cls{}/\\cwm{}'s 3,596 from 15,290 per-test instances). \\cls{} nonetheless outperforms \\traj{} by 2.13\\pp{} (88.43\\% vs.\\ 86.30\\%, Qwen3-4B), ruling out data volume as the explanation. An extreme downsample ablation (CLS trained on 447 per-test instances, ${\\sim}$105 unique variants) achieves 78.57 $\\pm$ 0.78\\%, confirming that per-test classification maintains reasonable performance under severe data reduction, though it falls below \\traj{} (86.30\\%) given the 20$\\times$ data disadvantage.\n\n\\paragraph{Few-shot prompting baselines.}\n\\label{app:few_shot}\nWe evaluate 3-shot in-context learning at repo level to test whether prompting strategy closes the gap to fine-tuned models. Table~\\ref{tab:few_shot} reports both per-test and variant-level accuracy.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Repo-level prompting baselines (per-test $n{=}9{,}784$; variant-level $n{=}48$). Majority baseline: 72.96\\% per-test, 54.17\\% variant-level.}\n\\label{tab:few_shot}\n\\setlength{\\tabcolsep}{4pt}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Model} & \\textbf{0-shot (per-test)} & \\textbf{3-shot (per-test)} & \\textbf{3-shot (variant)} \\\\\n\\midrule\nQwen3-8B & 49.90\\% & 71.61\\% & 45.83\\%\\textsuperscript{$\\ast$} \\\\\nDeepSeek-6.7B & 48.54\\% & 46.28\\% & 45.83\\%\\textsuperscript{$\\ast$} \\\\\n\\bottomrule\n\\end{tabular}}\n\n\\vspace{2pt}\n{\\footnotesize \\textsuperscript{$\\ast$}Both models achieve 45.83\\% by correctly classifying all 22 unresolved variants and zero resolved variants (22/48 = 45.83\\%), equivalent to an always-predict-unresolved baseline. The 100\\% overlap in variant-level predictions confirms complete degradation at task-relevant granularity.}\n\\end{table}\n\nBoth models converge to exactly 45.83\\% variant-level accuracy under 3-shot prompting, below majority baseline (54.17\\%). Variant-level analysis reveals this is not a coincidence: both models correctly classify all 22 unresolved variants and zero resolved variants, equivalent to an always-predict-unresolved baseline with 100\\% prediction overlap. Per-test accuracy diverges sharply (Qwen3-8B 71.61\\% vs.\\ DeepSeek 46.28\\%), but this divergence is entirely superficial: Qwen3-8B predicts pass on nearly all tests, inflating per-test accuracy on a pass-heavy dataset (72.96\\% pass rate) without genuine discriminative ability. Per-test metrics can thus severely misrepresent baseline capability; variant-level evaluation is necessary to detect complete degradation. Neither 0-shot nor few-shot prompting approaches fine-tuned performance (82--84\\% per-test); fine-tuning is a necessary condition for repo-level verification.\n\n\\section{Repo-Level Per-Mutation Breakdown}\n\\label{app:repo_mutation}\n\nTable~\\ref{tab:mutation_breakdown} compares per-mutation accuracy at repo level. \\cls{} produces 0\\% unparseable outputs; all values are direct classification accuracy. \\cwm{} overall accuracy includes default-pass assignment for unparseable outputs (see \\S\\ref{sec:repo}).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Per-mutation test accuracy (\\%) at repo level (SWE-bench Verified, $n{=}9{,}784$). \\cls{} 8B reports two seeds; $\\Delta$ is mean 4B$\\to$8B gain for \\cls{}. \\cwm{} 4B per-mutation overall accuracy omitted for non-gold mutations due to low parse rates (4.4--56.9\\%, Table~\\ref{tab:cwm_mutation_parse}); gold overall accuracy derived from parse rate 43.5\\% and parseable accuracy 23.5\\%.}\n\\label{tab:mutation_breakdown}\n\\resizebox{\\columnwidth}{!}{%\n\\setlength{\\tabcolsep}{3pt}\n\\begin{tabular}{lccccccc}\n\\toprule\n\\textbf{Mutation} & \\textbf{$n$} & \\textbf{CLS 4B} & \\textbf{CLS 8B s42} & \\textbf{CLS 8B s123} & \\textbf{CWM 4B} & \\textbf{CWM 8B} & \\textbf{$\\Delta$ CLS} \\\\\n\\midrule\ngold & 4,633 & 98.25 & 96.24 & 99.60 & 66.72 & 80.06 & $-$0.33 \\\\\noperator\\_swap & 3,357 & 78.91 & 81.38 & 82.60 & --- & 54.57 & +3.08 \\\\\noff\\_by\\_one & 183 & 58.47 & 86.89 & 79.20 & --- & 63.39 & \\textbf{+24.58} \\\\\nreturn\\_value & 562 & 67.97 & 75.44 & 66.40 & --- & 49.11 & +2.95 \\\\\nboundary\\_removal & 1,049 & 46.90 & 46.90 & 44.90 & --- & 42.23 & $-$1.00 \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\nFigure~\\ref{fig:mutation_heatmap} visualises the per-mutation accuracy contrast between \\cls{} and \\cwm{} at repo level.\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/paper/fig_mutation_heatmap.pdf}\n\\caption{Per-mutation repo-level accuracy heatmap. \\cls{} 8B values are seed-averaged (s42/s123). \\cwm{} 8B includes default-pass for unparseable outputs. \\texttt{boundary\\_removal} is a scale-invariant difficulty ceiling (${\\sim}$45\\%) for both formulations.}\n\\label{fig:mutation_heatmap}\n\\end{figure}\n\nTable~\\ref{tab:cwm_mutation_parse} shows that \\cwm{} generation quality degrades from 4B to 8B across all mutation types.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{\\cwm{} parse rates and parseable-only accuracy per mutation type (seed 42). Parse rate decreases uniformly from 4B to 8B; parseable-only accuracy is below random binary chance (50\\%) for gold at both scales.}\n\\label{tab:cwm_mutation_parse}\n\\setlength{\\tabcolsep}{4pt}\n\\begin{tabular}{lcccc}\n\\toprule\n& \\multicolumn{2}{c}{\\textbf{Parse Rate (\\%)}} & \\multicolumn{2}{c}{\\textbf{Parse Acc (\\%)}} \\\\\n\\cmidrule(lr){2-3} \\cmidrule(lr){4-5}\n\\textbf{Mutation} & \\textbf{4B} & \\textbf{8B} & \\textbf{4B} & \\textbf{8B} \\\\\n\\midrule\ngold & 43.5 & 23.9 & 23.5 & 16.5 \\\\\noperator\\_swap & 56.9 & 21.2 & 63.1 & 58.8 \\\\\noff\\_by\\_one & 4.4 & 27.3 & 0.0 & 38.0 \\\\\nreturn\\_value & 48.8 & 26.9 & 27.0 & 56.9 \\\\\nboundary\\_removal & 30.6 & 51.8 & 59.2 & 51.8 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nKey findings: (1)~Gold parse rate collapses from 43.5\\% to 23.9\\% at 8B; the simplest generation target (unmodified code, where all tests pass) degrades most, consistent with a fundamental generation bottleneck rather than task difficulty. (2)~Among parseable outputs, gold accuracy is 16.5--23.5\\%: the model generates outputs that fail exact-match even for correct code. (3)~\\texttt{off\\_by\\_one} is an anomaly: parse rate \\emph{increases} from 4.4\\% to 27.3\\%, but this is from an extremely low base ($n{=}8$ parseable at 4B), making both directions unreliable for this category.\n\n\\section{Variant-Level Accuracy}\n\\label{app:variant_level}\n\nTable~\\ref{tab:variant_level} reports variant-level accuracy ($n{=}48$) alongside per-test accuracy for all repo-level configurations. For \\cls{}, the aggregation penalty (per-test $\\to$ variant-level drop) ranges from 1\\pp{} to 19\\pp{} and is largest for models with low fail recall under the all-pass rule. \\cwm{} variant-level accuracy (48--52\\%) falls at or below the majority baseline, consistent with format collapse as the dominant failure mode.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Repo-level per-test vs.\\ variant-level accuracy ($n{=}48$ variants). Penalty = per-test $-$ variant-level. \\traj{} predicts variant outcomes directly (no aggregation). Variant-level majority baseline: 54.17\\% (26/48).}\n\\label{tab:variant_level}\n\\setlength{\\tabcolsep}{3pt}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llcccc}\n\\toprule\n\\textbf{Model} & \\textbf{Seed} & \\textbf{Per-test (\\%)} & \\textbf{Variant (\\%)} & \\textbf{Penalty (\\pp{})} & \\textbf{Fail Recall (\\%)} \\\\\n\\midrule\n\\multicolumn{6}{l}{\\emph{\\cls{}}} \\\\\nQwen3-8B & s42 & 84.48 & 72.92 & 11.56 & 56.76 \\\\\nQwen3-8B & s123 & 85.60 & 81.25 & 4.35 & 51.44 \\\\\nQwen3-4B & s42 & 83.63 & 64.58 & 19.05 & 48.72 \\\\\nDeepSeek-6.7B & s42 (e1) & 82.61 & 81.25 & 1.36 & 51.02 \\\\\nDeepSeek-6.7B & s42 (e3) & 82.51 & 79.17 & 3.34 & 38.47 \\\\\nDeepSeek-6.7B & s123 & 74.93 & 56.25 & 18.68 & ${\\sim}$13.72 \\\\\n\\midrule\n\\multicolumn{6}{l}{\\emph{\\cwm{}}} \\\\\nQwen3-8B & s42 & 65.17 & 52.08 & 13.09 & --- \\\\\nDeepSeek-6.7B$^\\dagger$ & s123 & --- & 47.92 & --- & --- \\\\\n\\midrule\n\\multicolumn{6}{l}{\\emph{\\traj{}}} \\\\\nQwen3-4B & s42 & --- & 72.92 & --- & --- \\\\\nQwen3-8B & s42 & --- & 70.83 & --- & --- \\\\\nDeepSeek-6.7B & 3-seed & --- & 77.08 $\\pm$ 3.61 & --- & --- \\\\\n\\midrule\nMajority & --- & 72.96 & 54.17 & --- & --- \\\\\n\\bottomrule\n\\end{tabular}}\n\\vspace{2pt}\n\n{\\footnotesize $^\\dagger$Evaluated on ${\\sim}$75\\% of test instances (7210--7668 of 9784). DeepSeek \\traj{} Table~\\ref{tab:repo_level} reports 3 seeds (42/123/456) for alignment with \\cls{}/\\cwm{} seed coverage; three supplementary seeds (0/789/999) yield 75.0\\%, 66.7\\%, 79.2\\% respectively (6-seed mean 75.35 $\\pm$ 5.00\\%), consistent in direction.}\n\\end{table}\n\n\\section{Training Hyperparameters}\n\\label{app:hyperparams}\n\nTable~\\ref{tab:hyperparams} lists all hyperparameters used for fine-tuning. Both \\cls{} and \\cwm{} share the same LoRA configuration, optimizer, and training schedule; the only differences are per-device batch size, gradient accumulation steps (adjusted to maintain identical effective batch size of 32 across model sizes), and learning rate (DeepSeek-Coder uses $2{\\times}10^{-4}$ vs.\\ $5{\\times}10^{-5}$ for Qwen3, selected via grid search over $\\{5{\\times}10^{-5}, 1{\\times}10^{-4}, 2{\\times}10^{-4}\\}$ on held-out validation loss).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Training hyperparameters for \\cls{}/\\cwm{} configurations. \\traj{} models use lr $= 2{\\times}10^{-4}$ due to the smaller training set (${\\sim}$8K function-level instances vs.\\ ${\\sim}$70K for \\cls{}/\\cwm{}); other hyperparameters are shared.}\n\\label{tab:hyperparams}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{ll}\n\\toprule\n\\multicolumn{2}{l}{\\textbf{Shared across all configurations}} \\\\\n\\midrule\nLoRA rank / alpha / dropout & 16 / 32 / 0.05 \\\\\nLoRA targets & \\texttt{q/k/v/o\\_proj} \\\\\nOptimizer & AdamW ($\\beta_1{=}0.9$, $\\beta_2{=}0.999$) \\\\\nLR scheduler & Linear \\\\\nEffective batch size & 32 \\\\\nMax sequence length & 2,048 \\\\\nEpochs & 3 \\\\\nPrecision & bf16 \\\\\nGradient checkpointing & \\checkmark \\\\\nSeeds (function) & \\{42, 123, 456, 789, 0\\}\\textsuperscript{$b$} \\\\\nSeeds (repo) & \\{42, 123, 456\\}\\textsuperscript{$c$} \\\\\n\\bottomrule\n\\end{tabular}}\n\n\\vspace{6pt}\n\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lccc}\n\\toprule\n\\multicolumn{4}{l}{\\textbf{Model-family--specific parameters}} \\\\\n\\midrule\n& \\textbf{Qwen3-4B} & \\textbf{Qwen3-8B} & \\textbf{DS-6.7B} \\\\\n\\midrule\nLearning rate & 5e-5 & 5e-5 & 2e-4 \\\\\nWeight decay & 0.01 & 0.01 & 0.0 \\\\\nWarmup ratio & 0.05 & 0.05 & 0.1 \\\\\nBatch / grad.\\ accum.\\ (\\cls{}) & 2 / 16 & 1 / 32 & 2 / 16 \\\\\nBatch / grad.\\ accum.\\ (\\cwm{}) & 1 / 32 & 1 / 32 & 1 / 32 \\\\\nTraining samples & 70,748 & 70,748 & 67,343--70,748\\textsuperscript{$a$} \\\\\n\\bottomrule\n\\end{tabular}}\n\n\\vspace{2pt}\n{\\footnotesize $^a$DeepSeek \\cls{} canonical run (s42) uses drop preprocessing, which excludes 3,405 sequences exceeding max length (67,343 of 70,748). The s123 run uses truncate preprocessing (70,748 samples) but produces NaN validation loss. See \\S\\ref{sec:setup}. $^b$Seeds 789 and 0 use NF4 quantization; others use bf16. $^c$Repo-level seed coverage varies by configuration; see Table~\\ref{tab:repo_level} caption for per-model counts.}\n\\end{table}\n\n\\paragraph{Data processing.} DeepSeek CWM seeds use \\texttt{train\\_unified.py}, which drops samples exceeding \\texttt{max\\_seq\\_length} (3{,}405 of 70{,}748 samples, 4.8\\%). Qwen CWM seeds use \\texttt{train\\_repo\\_cwm.py}, which truncates and retains all samples. This difference affects total training steps (${\\sim}$12{,}627 vs.\\ ${\\sim}$13{,}266 for DeepSeek, ${\\sim}$6{,}633 for Qwen) but not the training data distribution, as dropped samples are uniformly distributed across labels.\n\n\\paragraph{Prompt templates.} Prompt templates for all formulations (\\cls{}, \\cwm{}, \\traj{}) are provided in the code repository. \\cls{} uses a binary classification template (``Does this test pass or fail?''); \\cwm{} uses an execution simulation template (``What is the output of this test?''); \\traj{} uses a variant-level verdict template (``Is this patch resolved or unresolved?'').\n\n\\paragraph{Mutation operators.} We use five mutation types: (1)~\\emph{gold}: unmodified code (all tests pass); (2)~\\emph{operator\\_swap}: replaces comparison or arithmetic operators (e.g., \\texttt{<} $\\to$ \\texttt{<=}); (3)~\\emph{off\\_by\\_one}: shifts loop bounds or array indices by $\\pm$1; (4)~\\emph{return\\_value}: modifies return statements (e.g., negating a boolean, changing a constant); (5)~\\emph{boundary\\_removal}: removes conditional guards or boundary checks. Mutation operators were applied using AST-level transformation; variants that did not alter any test outcome were discarded.\n\n\\paragraph{Compute budget.}\nAll experiments were conducted on NVIDIA RTX 5090 GPUs. Training time is approximately 1.5 hours per run for 4B models and 2 hours for 8B models. Total compute budget: ${\\sim}$370 GPU-hours across 223 completed runs (135 successful, 88 failed/killed; ${\\sim}$46 unique configurations including seeds, formulations, model sizes, and ablations).\n\n\\section{Prompt Templates}\n\\label{app:prompts}\n\nWe show representative prompt examples for each formulation. All examples use the same input instance for comparability.\n\n\\paragraph{CLS (per-test classification).}\n{\\footnotesize\\begin{verbatim}\nSystem: You are a code verifier.\nGiven a code patch and a test name,\npredict whether the test will pass\nor fail when run against the\npatched code.\n\nUser:\n## Patch (git diff)\n&lt;patch content> [... truncated]\n## Test\ntest_boundary_check\nWill this test pass or fail?\n\nTarget: pass\n\\end{verbatim}}\n\n\\paragraph{CWM (execution simulation).}\n{\\footnotesize\\begin{verbatim}\nSystem: You are a code execution\nsimulator. Given a code snippet and\na test case, predict the execution\nresult.\n\nUser:\n## Code\n&lt;code content> [... truncated]\n## Test\ntest_boundary_check\nWhat is the execution result?\n\nTarget: PASS: test completed\nsuccessfully\n\\end{verbatim}}\n\n\\paragraph{TRAJ (trajectory scoring).}\n{\\footnotesize\\begin{verbatim}\nSystem: You are a code repair\nverifier. Given the code patch and\ntest summary, predict whether all\ntests pass (resolved) or any test\nfails (unresolved).\n\nUser:\n[Code]\n&lt;patch content> [... truncated]\n[Test Summary]\n&lt;all test names and descriptions>\n\nTarget: resolved\n\\end{verbatim}}\n\n\\cls{} and \\cwm{} share the same input format (one code--test pair per instance); \\cls{} produces a single token (\\texttt{pass}/\\texttt{fail}), while \\cwm{} generates a variable-length execution trace. \\traj{} receives all tests concatenated and produces a single token (\\texttt{resolved}/\\texttt{unresolved}).\n\n\n\\section{Val-Test Mutation Type Distribution}\n\\label{app:mutation_distribution}\n\nTable~\\ref{tab:mutation_distribution} reports the mutation type composition of the repo-level validation and test sets. The most notable shift is \\texttt{operator\\_swap}, which nearly doubles from val (19.1\\%) to test (34.3\\%), while \\texttt{off\\_by\\_one} shrinks from 10.0\\% to 1.9\\%.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Repo-level mutation type distribution: validation vs.\\ test set, with per-type \\cls{} accuracy at two model sizes (seed 42). Shift = test\\% $-$ val\\%.}\n\\label{tab:mutation_distribution}\n\\setlength{\\tabcolsep}{3pt}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lccccc}\n\\toprule\n\\textbf{Mutation Type} & \\textbf{Val (\\%)} & \\textbf{Test (\\%)} & \\textbf{Shift} & \\textbf{\\cls{} 4B} & \\textbf{\\cls{} 8B} \\\\\n\\midrule\ngold & 45.2 & 47.4 & +2.2 & 98.3 & 96.2 \\\\\noperator\\_swap & 19.1 & 34.3 & +15.2 & 78.9 & 81.4 \\\\\nboundary\\_removal & 15.0 & 10.7 & $-$4.3 & 46.9 & 46.9 \\\\\nreturn\\_value & 10.7 & 5.7 & $-$5.0 & 68.0 & 75.4 \\\\\noff\\_by\\_one & 10.0 & 1.9 & $-$8.1 & 58.5 & 86.9 \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\nThe \\texttt{operator\\_swap} shift is the primary source of val-test distribution mismatch. Since \\cls{} achieves moderate accuracy on this type (78.9--81.4\\%), the over-representation in the test set does not systematically bias overall accuracy estimates in either direction. Two boundary observations are notable: (1)~\\texttt{boundary\\_removal} represents a scale-invariant difficulty ceiling at ${\\sim}$47\\% across both model sizes: this mutation type resists capacity scaling; (2)~\\texttt{off\\_by\\_one} shows the largest scaling gain (+28.4\\pp{}, 58.5\\%$\\to$86.9\\%) but its small test share (1.9\\%) limits its contribution to overall accuracy differences across scales.\n\n\\section{Qualitative Error Analysis}\n\\label{app:qualitative}\n\nTo complement the quantitative divergence reported in \\S\\ref{sec:repo}, we examine representative errors from each formulation at repository level.\n\n\\paragraph{\\cwm{} failure modes.}\nTwo patterns account for the majority of unparseable \\cwm{} outputs on Qwen3. (1)~\\emph{Task misunderstanding}: the model generates a complete simulated test runner log (test names, timing, summary lines) rather than a pass/fail verdict. For instance, on \\texttt{django\\_\\_django-14315}, the model outputs a fabricated 1,248-token Django test execution trace with hallucinated test names that do not exist in the target file. The model confuses ``predict test outcome'' with ``simulate test execution environment.'' (2)~\\emph{Autoregressive degeneration}: the model enters a repetitive loop (e.g., repeating \\texttt{from \\_pytest.config import \\_parse\\_pytest\\_args} until truncation at 4,542 tokens). Both patterns produce zero usable signal and default to the majority-class label. This explains why unparseable predictions carry higher accuracy than parseable ones (\\S\\ref{sec:repo}).\n\n\\paragraph{\\cls{} failure modes.}\n\\cls{} errors concentrate in two categories requiring multi-step reasoning. False positives arise from \\emph{cross-concern value propagation}: a boundary removal mutation in \\texttt{pytest} converts a guarded attribute access (\\texttt{if xfailed and not xfailed.run}) to \\texttt{if True:}, causing a NoneType error on tests exercising unrelated skip marks. The model fails to trace the None path through the pytest hook lifecycle. False negatives arise from \\emph{mathematical equivalence}: on \\texttt{HumanEval/130} (Tribonacci variant), the model predicts failure for correct code because verifying the self-referential recurrence requires algebraic substitution rather than syntactic inspection. This single problem accounts for 17\\% of all function-level false negatives.\n\n\\paragraph{Complementarity.}\nThese failure patterns operate at different levels: \\cwm{} fails at the format level (producing no usable signal), while \\cls{} fails at the reasoning level (producing a confident but incorrect binary verdict). Both formulations are FP-dominant (over-predict failure), but \\cwm{}'s higher FP rate (70.3\\% vs.\\ 56.5\\%) means it over-predicts failure on instances \\cls{} correctly classifies, producing partial complementarity (oracle combination: 90.63\\%; \\S\\ref{app:extended_analysis}, paragraph a).\n\n\\section{Extended Analysis}\n\\label{app:extended_analysis}\n\n\\paragraph{Function-level CWM metric robustness.}\nAt function level, \\cwm{} outputs are short status strings (mean ${\\sim}$5--15 tokens). The unparseable rate is only 1.39\\%, and default-to-pass bias is $<$1\\pp{}, well below the SESOI threshold. Exact string matching is appropriate for these short, structured outputs; semantic-but-format-different matches are rare given the constrained output space.\n\n\\paragraph{(a) Error complementarity.}\n\\cls{} and \\cwm{} are both FP-dominant at function level but at different rates, producing partial complementarity. Among \\cls{} errors (seed 42), 56.5\\% are false positives (PASS $\\to$ FAIL); among \\cwm{} errors, 70.3\\% are false positives. Both formulations over-predict failure, but \\cwm{}'s stronger FP bias means it incorrectly rejects passing tests that \\cls{} correctly accepts. An oracle combination achieves 90.63\\% accuracy (1713/1890 correct, 177 both-wrong; +2.80\\pp{} over the best single formulation, \\cls{} 87.83\\%; single-seed estimate, seed 42). The complementarity arises from different \\emph{degrees} of fail-bias rather than opposite error directions: \\cwm{}'s generation bottleneck produces aggressive failure predictions, while \\cls{}'s single-token output is more calibrated. Ensemble approaches exploiting this degree difference are a natural direction.\n\n\\paragraph{(b) CWM error mode breakdown.}\nAmong unparseable \\cwm{} outputs (Qwen3, repo-level), 76.9\\% contain no execution keywords; 22.9\\% contain ambiguous co-occurring pass/fail keywords. Format compliance varies sharply across repositories (scikit-learn: near-zero unparseable; sphinx: 100\\%); repository-specific code patterns interact with the model's generation capabilities in complex ways. This per-repository variation is consistent with a model/tokenizer-specific failure rather than a formulation-level one.\n\n\\paragraph{(c) Relaxed matching does not rescue \\cwm{}.}\nRelaxed matching (tolerating format deviations, L0--L4) \\emph{decreases} \\cwm{} accuracy: 58.04\\%$\\to$56.98\\% (seed 42) and 59.09\\%$\\to$55.91\\% (seed 123). Unparseable predictions default to the majority class (pass, 72.96\\%), which outperforms the model's own parseable predictions (38--43\\%). The divergence widens from 26\\pp{} to 27\\pp{} under relaxed matching. This rules out the hypothesis that parsing strictness inflates the observed gap. Constrained decoding~\\cite{willard2023outlines} could enforce format compliance but would not address the semantic accuracy deficit among parseable outputs. An accidental training artifact provides further evidence: a \\cwm{} model inadvertently trained on function-level (\\cls{}-format) data achieved 86.05\\% accuracy with 0\\% unparseable outputs at repo level, recovering \\cls{}-level performance. This confirms that the repo-level \\cwm{} degradation stems entirely from trace generation complexity, not from the underlying verification task.\n\n\\paragraph{(d) Variance compression.}\n\\cwm{}'s 5-seed standard deviation (0.37\\pp{}) is lower than \\cls{} (0.78\\pp{}) and \\traj{} (0.97\\pp{}) at function level. If \\cwm{} performance is capped by output-format constraints at a given complexity level, seed-to-seed variability is compressed relative to formulations whose performance depends more on learned representations.\n\n\\paragraph{(e) Per-test precision and recall.}\n\\cls{} achieves fail \\fone{} 87.59\\% (precision 86.20\\%, recall 89.04\\%) at seed 42.% derived from overlap analysis (error_overlap_matched_seed.json); FP=130, FN=100, TP=848, TN=812\nMulti-F2P instances (6--10 tests) reach 96.3\\% accuracy, consistent with the oracle finding that per-test granularity is most valuable for complex instances.\n\n\\paragraph{(f) Block correlation.}\nWithin-problem errors are correlated (ICC $= 0.191$, DEFF $= 3.97$, 2.81$\\times$ more all-correct problems than i.i.d.\\ expectation). All statistical tests use clustered bootstrap accordingly.\n\n\\paragraph{(g) Failed interventions.}\nWe systematically tested four interventions targeting different hypothesized causes of \\cwm{} repo-level degradation; all failed:\n\n\\begin{itemize}[leftmargin=*,itemsep=1pt,topsep=2pt]\n\\item \\textbf{Capacity (rank 32, $\\alpha{=}64$):} $-$0.47\\pp{}, within seed variance (\\S\\ref{app:ablations}).\n\\item \\textbf{Majority voting ($K{=}3$):} $-$0.68\\pp{}; 93.3\\% unanimous, net flips negative (\\S\\ref{app:ablations}).\n\\item \\textbf{Relaxed matching (L0--L4):} $-$1.06\\pp{}; default-pass outperforms parseable predictions (paragraph~(c) above).\n\\item \\textbf{Model scaling (4B$\\to$8B):} parseable accuracy decreases (42.88\\%$\\to$38.52\\%) while unparseable rate rises (53.7\\%$\\to$73.8\\%); gain is a default-assignment artifact (\\S\\ref{sec:repo}).\n\\end{itemize}\n\n\\noindent Each intervention targets a distinct alternative explanation (insufficient capacity, random noise, parsing strictness, model scale); the uniform failure across all four confirms the bottleneck is formulation-level: output space complexity at repo level exceeds what ${\\leq}$8B generation models can handle, independent of these surface-level factors.\n\n\\paragraph{(h) Per-mutation scaling patterns.}\nScaling benefits are highly non-uniform across mutation types (Table~\\ref{tab:mutation_breakdown}). \\texttt{off\\_by\\_one} shows the largest \\cls{} scaling gain: 58.5\\% (4B) to 86.9\\% (8B, $+$28.4\\pp{}). In contrast, \\texttt{boundary\\_removal} is scale-invariant at ${\\sim}$47\\% across both sizes, which marks an intrinsic difficulty ceiling. For \\cwm{}, gold mutation parse rate collapses from 43.5\\% (4B) to 23.9\\% (8B) despite being the simplest target: generation capability degrades even for trivially correct code at larger scale within Qwen3. The val-test mutation type distribution differs notably (\\texttt{operator\\_swap} shifts from 19.1\\% to 34.3\\%; Table~\\ref{tab:mutation_distribution}), but this shift does not systematically bias overall accuracy because \\cls{} performance on \\texttt{operator\\_swap} (78.9--81.4\\%) is close to the overall mean.\n\n\\paragraph{(i) Inference efficiency.}\n\\cls{} achieves 217$\\times$ higher throughput than \\cwm{} at repo level (853 vs.\\ 3.9 inferences/min; Qwen3-4B, RTX 5090, 100 samples, avg ${\\sim}$1,040 input tokens). The speedup derives directly from the formulation: classification requires a single output token, whereas \\cwm{} generates an average of 477 tokens per inference. Median latency is 48ms (\\cls{}) vs.\\ 16.3s (\\cwm{}). At the observed unparseable rate of 73.8\\% (8B), the majority of \\cwm{}'s generation budget produces tokens that cannot yield a valid verdict. This \\cls{}--\\cwm{} efficiency gap is an inherent property of the formulation difference (1 vs.\\ $O(L)$ output tokens) and should generalize across models, unlike the accuracy divergence which may be model-contingent.\n\nThe \\cls{}--\\traj{} efficiency comparison is more nuanced, because \\cls{} makes one call per test while \\traj{} makes one call per instance. Per-call, \\cls{} is 20--138$\\times$ faster (depending on input length: 47ms for short contexts vs.\\ 2,632ms for \\traj{}). However, the per-instance effective speedup depends on test count $|T|$: at function level ($|T| \\approx 2.3$), \\cls{} is ${\\sim}$24$\\times$ faster (108ms vs.\\ 2,632ms per instance); at repo level ($|T| \\approx 12.3$, ${\\sim}$70ms/call with longer inputs), \\cls{} is ${\\sim}$3$\\times$ faster (861ms vs.\\ 2,631ms). A crossover exists at $|T| \\approx 50$ tests, beyond which \\traj{}'s single-call amortization dominates. This boundary condition is informative for deployment: \\cls{} is strongly preferred for function-level and moderate repo-level test suites, while extremely large test suites ($>$50 tests per instance) favor trajectory-level efficiency despite its coarser diagnostic signal.\n\n\\paragraph{(j) Re-repair pilot.}\nWe tested whether per-test diagnostic feedback improves downstream repair. A Qwen3-8B repair agent received either per-test diagnostic signals (which specific tests failed and why) or binary accept/reject feedback, evaluated on 44 SWE-bench Verified instances. The diagnostic condition achieved accuracy no higher than the binary baseline ($A_1 = 52.3\\%$, $p = 0.42$, effect size $\\approx 0$). Per-test diagnostic information does not automatically translate to repair improvements at this scale. The negative result may reflect insufficient agent capability to exploit fine-grained feedback, insufficient sample size (at $n = 44$, statistical power is ${\\sim}$0.3 for a medium effect size), or a genuine limitation of the diagnostic-to-repair translation.\n\n\\paragraph{(k) Relationship to chain-of-thought verification.}\n\\cwm{} is structurally a chain-of-thought verifier: the model generates an execution trace token by token and derives its PASS/FAIL verdict from the final trace state. If intermediate reasoning improved verification, \\cwm{} should outperform the reasoning-free \\cls{} baseline. At function level, no such advantage materialises: \\cwm{} and \\cls{} are statistically equivalent (TOST $p{=}0.007$, $\\pm$2\\pp{} margin; \\S\\ref{sec:equivalence}), indicating that the additional trace generation provides no accuracy benefit over direct binary classification. At repo level, the chain-of-thought mechanism actively \\emph{hurts}: trace generation triggers format collapse (53--74\\% unparseable), and even parseable traces yield accuracy below the majority baseline (38--43\\% vs.\\ 72.96\\%; paragraph~(c)). Four targeted interventions fail to rescue the generation pathway (paragraph~(g)). Within the ${\\leq}$8B LoRA regime, chain-of-thought--style verification does not outperform direct classification for execution prediction. Whether execution-trace pretraining at larger scale~\\cite{meta2025cwm} changes this conclusion remains the primary open question (\\S\\ref{sec:threats}).\n\n\\section{TOST Margin Sensitivity}\n\\label{app:tost_sensitivity}\n\nTable~\\ref{tab:tost_sensitivity} reports the TOST equivalence $p$-value as a function of the equivalence margin, computed on the 5-seed variant-level \\cls{}--\\cwm{} comparison (gap $= 1.24$\\pp{}, 523 variants, 114 clusters, clustered bootstrap).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{TOST margin sensitivity for \\cls{}--\\cwm{} variant-level equivalence (5 seeds, 523 variants, 114 clusters). The smallest margin achieving equivalence at $\\alpha = 0.05$ is $\\pm$1.52\\pp{}.}\n\\label{tab:tost_sensitivity}\n\\setlength{\\tabcolsep}{4pt}\n\\begin{tabular}{ccc}\n\\toprule\n\\textbf{Margin ($\\pm$\\pp{})} & \\textbf{$p$-value} & \\textbf{Equivalent ($\\alpha{=}0.05$)?} \\\\\n\\midrule\n1.0 & $\\gg$0.05 & No \\\\\n1.5 & 0.054 & No (borderline) \\\\\n\\textbf{1.52} & ${\\sim}$\\textbf{0.05} & \\textbf{Smallest margin} \\\\\n1.71 & 0.027 & Yes \\\\\n2.0 & 0.007 & Yes \\\\\n3.0 & $4.6{\\times}10^{-5}$ & Yes \\\\\n5.0 & $\\ll$0.001 & Yes \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nFigure~\\ref{fig:tost_sensitivity} visualises the margin--$p$-value relationship for both comparisons.\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/paper/fig_tost_sensitivity.pdf}\n\\caption{TOST $p$-value as a function of equivalence margin. \\cls{}--\\cwm{} (blue) achieves equivalence at $\\pm$1.52\\pp{}; \\cls{}--\\traj{} (green) crosses $\\alpha{=}0.05$ near $\\pm$1.8\\pp{} but does not survive Holm correction. Log scale.}\n\\label{fig:tost_sensitivity}\n\\end{figure}\n\nThe minimum equivalence margin is $\\pm$1.52\\pp{}, 0.48\\pp{} below our pre-specified $\\pm$2\\pp{} threshold. The $\\pm$2\\pp{} threshold was set based on deployment relevance rather than observed data: at function-level accuracy (85--88\\%), a 2\\pp{} per-test difference corresponds to ${\\sim}$38 additional errors across 1,890 tests (${\\sim}$2--3 problems out of 114), comparable in magnitude to between-seed standard deviation (0.37--0.97\\pp{}) and checkpoint selection noise ($<$1\\pp{}). Differences within this range do not reliably distinguish formulations from training noise in pipeline selection decisions. For \\cls{}--\\traj{}, the TOST at $\\pm$2\\pp{} yields $p{=}0.025$, nominally significant but not surviving Holm-Bonferroni correction at $k{=}5$ (adjusted $p{=}0.075$; Table~\\ref{tab:holm}). The one-sided decomposition reveals the binding constraint: $p_{\\text{upper}}{=}0.005$ ($\\Delta < {+}2$\\pp{} is well-confirmed) while $p_{\\text{lower}}{=}0.025$ ($\\Delta > {-}2$\\pp{}) limits the overall TOST, consistent with \\cls{} having mildly higher accuracy.\n\n\\paragraph{Robustness: seed-level vs.\\ clustered bootstrap TOST.}\nThe primary TOST $p$-values use seed-level paired analysis (df${=}$4), treating each training seed as the unit of replication (\\S\\ref{sec:setup}). Under problem-level clustered bootstrap (resampling 114 problem clusters, 10K iterations), the \\cls{}--\\traj{} raw TOST $p$ decreases to ${\\sim}$0.007 (Holm-adjusted $p{\\approx}0.021$), which would confirm equivalence. We report the more conservative seed-level result ($p{=}0.025$, adjusted $p{=}0.075$) as primary, since training seeds are the true unit of replication; problem-level bootstrap pools within-seed observations and may understate between-seed uncertainty. For \\cls{}--\\cwm{}, both methods confirm equivalence ($p \\leq 0.010$), so the choice does not affect conclusions.\n\n\\subsection{Bayesian ROPE Analysis}\n\\label{app:bayesian_rope}\nTo complement the frequentist TOST, we conduct a Bayesian equivalence analysis using a paired $t$-test with Jeffreys prior~\\cite{kruschke2013bayesian,kruschke2018rejecting}. The marginal posterior for the mean accuracy difference follows a $t$-distribution with $n{-}1$ degrees of freedom. For \\cls{}--\\cwm{}, the posterior probability within the $\\pm$2\\pp{} ROPE is $P(\\text{ROPE}) = 0.975$, and the 95\\% highest density interval (HDI $= [{+}0.10, {+}2.00]$\\,pp) falls entirely inside the ROPE, confirming equivalence under both continuous and HDI-based decision criteria. For \\cls{}--\\traj{} at per-test level, $P(\\text{ROPE}) = 0.542$ (inconclusive; 95\\% HDI $= [{+}0.35, {+}3.52]$\\,pp extends beyond the ROPE), consistent with the TOST inconclusive result after Holm correction ($p_{\\text{adj}} = 0.075$). At variant level, \\cls{}--\\traj{} equivalence is supported by the Bayesian criterion ($P(\\text{ROPE}) = 0.970$, HDI $= [{-}2.00, {+}1.03]$\\,pp), but the frequentist TOST remains inconclusive after Holm-Bonferroni correction ($p_{\\text{adj}} = 0.075$; Table~\\ref{tab:holm}). This discrepancy reflects differing treatments of multiplicity: Bayesian ROPE evaluates each comparison independently, while Holm correction penalizes across all $k{=}5$ primary tests. For \\cls{}--\\cwm{}, both frameworks agree (TOST $p_{\\text{adj}}{=}0.028$, $P(\\text{ROPE}){=}0.975$); for \\cls{}--\\traj{} per-test, both are inconclusive. We conservatively follow the Holm-corrected TOST in the main text and report \\cls{}--\\traj{} equivalence as inconclusive.\n\n\\paragraph{14B scaling evidence.} At 14B (3 seeds), the \\cls{}--\\cwm{} gap narrows to 0.43\\pp{} and the \\cls{}--\\traj{} gap to 1.07\\pp{}, both within the $\\pm$2\\pp{} margin. Seed-level TOST (df${=}$2) is inconclusive for equivalence in both pairs ($p{=}0.076$ for \\cls{}--\\cwm{}, $p{=}0.187$ for \\cls{}--\\traj{}), reflecting the severe power limitation of 3-seed comparisons (power ${\\sim}$0.08 at $\\pm$2\\pp{} margin with df${=}$2). Bayesian ROPE provides moderate support: $P(\\text{ROPE}){=}0.887$ for \\cls{}--\\cwm{} and $P(\\text{ROPE}){=}0.780$ for \\cls{}--\\traj{}. Under problem-level clustered bootstrap, both comparisons reach significance ($p{=}0.0006$ and $p{=}0.043$ respectively), but this analysis treats within-seed observations as exchangeable, potentially understating between-seed uncertainty. The monotonic gap reduction (3.11\\pp{} at 4B $\\to$ 2.24\\pp{} at 8B $\\to$ 1.07\\pp{} at 14B) favors a capacity-dependent convergence interpretation, though formal confirmation at seed level requires more training seeds.\n\n\n\\section{Variant-Level Effect Sizes}\n\\label{app:power}\n\nTable~\\ref{tab:variant_power} reports variant-level bootstrap confidence intervals for the repo-level formulation comparisons ($n{=}48$ variants). Following Hoenig and Heisey~\\cite{hoenig2001}, we report minimum detectable effect (MDE) rather than post-hoc observed power.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Variant-level bootstrap analysis ($n{=}48$). \\cls{}--\\cwm{} uses paired bootstrap (same variants, same seed); \\cls{}--\\traj{} uses unpaired bootstrap (per-variant \\traj{} predictions not archived for pairing). MDE at $n{=}48$: ${\\sim}$25\\pp{}.}\n\\label{tab:variant_power}\n\\setlength{\\tabcolsep}{3pt}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llccc}\n\\toprule\n\\textbf{Comparison} & \\textbf{Config} & \\textbf{$\\Delta$ (\\pp{})} & \\textbf{95\\% CI} & \\textbf{$p$} \\\\\n\\midrule\n\\multicolumn{5}{l}{\\emph{\\cls{} vs.\\ \\cwm{} (paired)}} \\\\\n& Qwen3-8B & +29.17 & [10.42, 47.92] & 0.003 \\\\\n& DeepSeek-6.7B & +35.42 & [18.75, 50.05] & ${<}$0.001 \\\\\n\\midrule\n\\multicolumn{5}{l}{\\emph{\\cls{} vs.\\ \\traj{} (unpaired)}} \\\\\n& Qwen3-4B & $-$4.17 & wide & 0.740 \\\\\n& Qwen3-8B & +8.33 & wide & 0.385 \\\\\n& DeepSeek-6.7B & 0.00 & wide & 1.000 \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\nAt $n{=}48$, the MDE is ${\\sim}$25\\pp{}. The \\cls{}--\\cwm{} gap (29--35\\pp{}) exceeds this threshold, confirming that $n{=}48$ is sufficient to detect the observed divergence. The \\cls{}--\\traj{} gaps ($<$10\\pp{}) fall well below the MDE: any true difference is too small to detect at this sample size, consistent with the function-level TOST equivalence (\\S\\ref{sec:equivalence}).\n\nThe \\cls{}--\\traj{} unpaired bootstrap produces wider confidence intervals than paired analysis would; \\traj{} per-variant predictions were not archived in a format that permits pairing. The \\cls{}--\\cwm{} paired comparison uses \\cls{} s123 vs.\\ \\cwm{} s42 (different seeds), but the CI lower bound of 10.42\\pp{} far exceeds the seed noise observed in function-level experiments ($<$2\\pp{}).\n\n\n\\section{Multiple Comparison Correction}\n\\label{app:holm}\n\nTable~\\ref{tab:holm} applies Holm-Bonferroni correction~\\cite{holm1979} to the five primary statistical comparisons across this study ($k{=}5$, family-wise $\\alpha{=}0.05$).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Holm-Bonferroni correction for primary comparisons ($k{=}5$). Comparisons ranked by raw $p$-value; each tested against $\\alpha / (k - \\text{rank} + 1)$.}\n\\label{tab:holm}\n\\setlength{\\tabcolsep}{3pt}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{clcccc}\n\\toprule\n\\textbf{Rank} & \\textbf{Comparison} & \\textbf{Raw $p$} & \\textbf{Factor} & \\textbf{Adj $p$} & \\textbf{Sig.?} \\\\\n\\midrule\n1 & Repo: \\cls{} vs \\cwm{} & 0.003 & $\\times$5 & 0.015 & \\checkmark \\\\\n2 & Func: \\cls{} vs \\cwm{} (TOST $\\pm$2\\pp{}) & 0.007 & $\\times$4 & 0.028 & \\checkmark \\\\\n3 & Func: \\cls{} vs \\traj{} (TOST $\\pm$2\\pp{}) & 0.025 & $\\times$3 & 0.075 & --- \\\\\n4 & Repo: \\cwm{} vs \\traj{} & 0.039 & $\\times$2 & 0.078 & --- \\\\\n5 & Repo: \\cls{} vs \\traj{} & 0.385 & $\\times$1 & 0.385 & --- \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\nThe two core claims survive correction: the repo-level \\cls{}--\\cwm{} divergence (adjusted $p{=}0.015$) and function-level \\cls{}--\\cwm{} equivalence (adjusted $p{=}0.028$). The function-level \\cls{}--\\traj{} equivalence does not survive correction (adjusted $p{=}0.075$). Under problem-level clustered bootstrap, the raw TOST $p$ decreases to ${\\sim}$0.007 (adjusted $p{\\approx}0.021$), which would confirm equivalence; we report the more conservative seed-level result ($p{=}0.025$) as primary, since training seeds are the true unit of replication.\n\n\\section{Mixed-Effects Regression}\n\\label{app:interaction}\n\nWe fit mixed-effects linear probability models (LPM) with heteroskedasticity-robust standard errors (HC1) to test the formulation$\\times$complexity interaction formally~\\cite{moulton1990}. We choose LPM because coefficients are directly interpretable as probability differences (percentage points), consistent with the reporting units in the main text; at these sample sizes ($n{\\approx}56$K cross-complexity, repo-level pooled cross-model) and base rate range (0.6--0.9), LPM and logistic regression yield concordant conclusions for all primary effects~\\cite{angrist2009mostly} (confirmed below).\n\n\\paragraph{Cross-complexity model (DeepSeek-Coder).} \\texttt{correct $\\sim$ formulation $\\times$ complexity + (1|problem\\_id)}, $n{=}56{,}480$ observations (\\cls{} + \\cwm{} $\\times$ function + repo), 139 problem clusters. The \\cwm{} main effect at function level is non-significant ($\\hat{\\beta}{=}-0.002$, $z{=}-0.25$, $p{=}0.805$); the \\cwm{}$\\times$repo interaction is highly significant ($\\hat{\\beta}{=}-0.219$, $z{=}-23.7$, $p{<}0.001$). \\cwm{} and \\cls{} are statistically indistinguishable at function level ($\\Delta{=}-0.2$\\pp{}, $p{=}0.805$) but diverge by 22\\pp{} at repo level, confirming the complexity-dependent divergence is not an artifact of aggregation.\n\n\\paragraph{Repo-level cross-model model.} \\texttt{correct $\\sim$ formulation $\\times$ model + (1|problem\\_id)}, both model families, repo level only. \\cwm{} deficit: $\\hat{\\beta}{=}-0.22$ ($-$22\\pp{}, $z{=}-64.4$, $p{<}0.001$). Model effect: +1.1\\pp{} for Qwen3 ($z{=}3.1$, $p{=}0.002$ in LPM; not significant under GEE, $p{=}0.449$). Formulation$\\times$model interaction: +1.6\\pp{} less \\cwm{} degradation on Qwen3 ($z{=}2.8$, $p{=}0.006$ in LPM; not significant under GEE, $p{=}0.860$). Formulation dominates the predictable variance; model identity is directionally positive but specification-dependent. The 25-cluster random intercept structure limits effective degrees of freedom for the random effects; inferences on fixed effects (formulation, complexity) are robust as they pool across the full observation count.\n\n\\paragraph{Logistic regression robustness check.} To verify that LPM conclusions are not artifacts of the linear link function, we fit GEE logistic regression (binomial family, exchangeable working correlation, robust sandwich standard errors) to the same data. For the cross-complexity model, the \\cwm{} main effect at function level has OR$=$0.98 (95\\% CI [0.86, 1.12], $p{=}0.771$) and the \\cwm{}$\\times$repo interaction has OR$=$0.31 ([0.15, 0.65], $p{=}0.002$). Average marginal effects are $-$0.2\\pp{} (function) and $-$21.6\\pp{} (repo), matching LPM coefficients within 0.3\\pp{}. For the cross-model model, the \\cwm{} deficit has OR$=$0.30 ([0.15, 0.63], $p{=}0.001$, AME$=$\\,$-$21.1\\pp{}). Direction, magnitude, and significance of all primary effects are concordant between LPM and logistic regression; minor discrepancies in secondary effects (model identity, formulation$\\times$model interaction: $p{=}0.449$ and $p{=}0.860$ under GEE vs.\\ $p{=}0.002$ and $p{=}0.006$ under LPM) reflect the GEE's more conservative cluster-robust inference with $k{=}25$ clusters. The discrepancy in secondary effects reflects cluster count: the cross-complexity model ($k{=}139$) yields reliable sandwich SEs, while the cross-model model ($k{=}25$) falls below the $k{\\geq}40$ threshold recommended for stable cluster-robust inference~\\cite{cameron2008bootstrap}.\n\n\\section{CWM Parseable Bias Analysis}\n\\label{app:parseable_bias}\n\nFigure~\\ref{fig:cwm_unparseable} summarises the unparseable rate contrast across complexity levels.\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/paper/fig_cwm_unparseable.pdf}\n\\caption{\\cwm{} unparseable rate by complexity level. Function-level outputs (${\\sim}$5--15 tokens) yield 1.4\\% unparseable; repo-level outputs (${\\sim}$477 tokens) reach 53.7\\% (4B) and 73.8\\% (8B). Parseable-only accuracy (inside bars) decreases from 4B to 8B despite rising overall accuracy, confirming default-assignment inflation.}\n\\label{fig:cwm_unparseable}\n\\end{figure}\n\nThe default-to-pass assignment for unparseable \\cwm{} outputs is not random with respect to instance difficulty. Unparseable instances have significantly higher pass rates than parseable ones (74.6\\% vs.\\ 68.3\\%, $\\chi^2$ $p = 5.9 \\times 10^{-10}$), and \\cls{} models achieve higher accuracy on unparseable instances (86.4\\% vs.\\ 79.1\\%, $p = 3.3 \\times 10^{-18}$). This indicates that \\cwm{}'s parsing failures concentrate on simpler, pass-heavy instances where the majority-class default happens to be correct more often. Cross-model Jaccard overlap of unparseable instance sets is 0.46, confirming this pattern is instance-driven (specific inputs consistently cause parsing failure across models) rather than stochastic. The net effect is that \\cwm{}'s reported accuracy is inflated by default-correct assignments on easy instances, while its effective discriminative accuracy on harder instances is substantially lower than the aggregate figure suggests.\n\n\n\\section{Threats to Validity (Full Analysis)}\n\\label{app:threats}\n\nWe identify five potential confounds and assess their impact on our conclusions.\n\n\\paragraph{Checkpoint selection.} Val-based selection is unavailable for runs with NaN validation loss (DeepSeek \\cwm{} repo-level runs, DeepSeek \\cls{} s123), which default to the final epoch checkpoint. A checkpoint ablation on Qwen3-8B \\cls{} s42 quantifies this confound: epoch~1 (ckpt-2200) achieves 85.34\\%, val-selected (ckpt-3600) 84.48\\%, and final epoch (ckpt-6633) 85.29\\%, a $<$1\\pp{} range. The val-selected checkpoint is the lowest, indicating no upward bias from checkpoint selection. The Qwen3-8B \\traj{} comparison (epoch 2: 72.92\\% vs.\\ epoch 3: 70.83\\%) shows a slightly larger ${\\sim}$2\\pp{} shift. For \\cwm{}, the convergence analysis (Appendix~\\ref{app:cwm_convergence}) shows eval loss at the final epoch is 1.8$\\times$ its minimum; however, early-stopped checkpoints retain high unparseable rates, leaving the qualitative ranking unchanged.\n\n\\paragraph{\\cwm{} convergence analysis.}\n\\label{app:cwm_convergence}\nQwen3-8B \\cwm{} repo-level eval loss reaches its minimum within ${\\sim}$5\\% of training (step 300--400 of 6{,}633) and increases monotonically thereafter, with no plateau or recovery (Table~\\ref{tab:cwm_convergence}). This pattern is consistent across all three seeds, confirming systematic overfitting to trace generation rather than stochastic variation. The final-epoch eval loss is ${\\sim}$1.8$\\times$ the optimal value. By contrast, function-level \\cwm{} achieves \\cls{}-equivalent accuracy (TOST $p{=}0.007$) with the same training recipe, indicating that the overfit is specific to repo-level output complexity. Cross-model validation: a DeepSeek-Coder early-stopped checkpoint (s123, epoch~1) achieves 75.45\\% versus 57.31\\% at epoch~3 (s123; +18.14\\pp{}), but retains 66.4\\% unparseable rate, confirming that format collapse emerges early and is not a late-training artifact. No epoch-level checkpoint is available for Qwen3 CWM (only step-level checkpoints at steps 300/400 and late steps ${\\geq}$5800; continuous epoch checkpointing was not enabled for this training run). The convergence analysis (Table~\\ref{tab:cwm_convergence}) shows eval loss minimum at step 300--400 across all three Qwen3 seeds, consistent with DeepSeek-Coder's epoch-1 improvement, providing cross-model evidence that the overtraining pattern generalizes. An early checkpoint (step 400, ${\\sim}$6.5\\% of training, s42) yields 65.17\\% repo-level accuracy with 63.7\\% unparseable rate, comparable to or below final-epoch performance (66.93--67.33\\% accuracy, 60.4--63.9\\% unparseable; s123/s456 at step 6633). This rules out late-training format degradation: collapse is present from early training, and the optimal eval-loss checkpoint does not recover repo-level accuracy. A later checkpoint (step 6100, s42, seq8192) achieves 69.50\\% test accuracy despite substantially higher validation loss than val-best ckpt-400 (64.36\\%), suggesting that validation loss may not be a reliable proxy for test-set performance in \\cwm{} repo-level evaluation.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{\\cwm{} repo-level eval loss across training (Qwen3-8B, 3 seeds). Minimum is reached at step 300--400 (${\\sim}$5\\% of training); subsequent training monotonically increases loss.}\n\\label{tab:cwm_convergence}\n\\begin{tabular}{lccc}\n\\toprule\nStep & s42 & s123 & s456 \\\\\n\\midrule\n300 & 0.291 & \\textbf{0.288} & \\textbf{0.277} \\\\\n400 & \\textbf{0.286} & 0.306 & 0.283 \\\\\n1000 & 0.333 & 0.336 & 0.351 \\\\\n3000 & 0.445 & 0.453 & 0.435 \\\\\n6600 & 0.521 & 0.517 & 0.507 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Evaluation sequence length.} \\cwm{} accuracy varies by ${\\sim}$9\\pp{} across evaluation sequence lengths for the same checkpoint (seq2048: ${\\sim}$65\\% vs.\\ seq4096: ${\\sim}$56\\%), driven by unparseable-rate differences that propagate through majority-class default assignment. \\cls{} is invariant to this parameter. Cross-model \\cwm{} comparisons use different eval lengths (Qwen3: 8192, DeepSeek: 4096) and are not directly comparable in absolute terms. A matched-sequence evaluation shows ${\\sim}$1.5\\pp{} difference for \\cls{} (Appendix~\\ref{app:ablations}), insufficient to explain the 18--26\\pp{} gap. Furthermore, increasing Qwen3-8B \\cwm{} evaluation from seq4096 to seq8192 \\emph{raises} the unparseable rate (63.7\\%$\\to$73.8\\%) while changing accuracy by only 0.81\\pp{} (64.36\\%$\\to$65.17\\%); giving the model more generation budget worsens format compliance rather than improving it, confirming that format collapse is a structural bottleneck rather than a truncation artifact. Practitioners must standardize evaluation sequence length for generation-based formulations.\n\n\\paragraph{Preprocessing.} DeepSeek \\cls{} accuracy ranges from 82.61\\% (s42, drop preprocessing) to 74.93\\% (s123, truncate preprocessing), a 7.68\\pp{} spread that conflates preprocessing strategy, checkpoint selection method, and seed. The two strategies produce different effective training sets (67,343 vs.\\ 70,748 samples) and different checkpoint selection regimes. The qualitative ranking \\cls{} $>$ \\cwm{} holds under both strategies (Table~\\ref{tab:taxonomy}).\n\n\\paragraph{\\traj{} training regime.} \\traj{} uses a different training configuration: smaller training set (${\\sim}$400 repo-level variants vs.\\ ${\\sim}$70K per-test instances), higher learning rate ($2{\\times}10^{-4}$ vs.\\ $5{\\times}10^{-5}$), and variant-level labels. This asymmetry is inherent to the formulation (trajectory-level labels are only available at variant granularity), but precludes training-data-controlled comparison at repo level. The downsample ablation confirms the \\cls{} formulation advantage persists at matched data volume (80.74\\% vs.\\ 72.92\\%; Appendix~\\ref{app:downsample}), though it controls for training volume but not label granularity (per-test vs.\\ variant-level). Crucially, \\traj{} achieves statistical equivalence with \\cls{} at function level (${\\leq}$1.3\\pp{}, \\S\\ref{sec:func_results}), demonstrating the formulation itself is viable; the repo-level gap attribution remains uncertain: data volume (${\\sim}$400 variants vs.\\ ${\\sim}$70K per-test instances) and label granularity (variant-level vs.\\ per-test) are both plausible confounds that cannot be separately controlled.\n\n\\paragraph{\\cwm{} scale and pretraining.} Our \\cwm{} baseline uses 4--8B LoRA fine-tuning without execution trace pretraining. The original Code World Model~\\cite{meta2025cwm} uses 32B parameters with mid-training on execution traces, a fundamentally different training regime. At larger scale or with execution-trace pretraining, the generation bottleneck observed here may diminish: larger models produce more coherent long-form outputs, and execution trace exposure may improve output format compliance. This is the primary limitation: all repo-level \\cwm{} conclusions are conditional on the ${\\leq}$8B LoRA regime.\n\nDespite these confounds, the repo-level \\cls{}--\\cwm{} gap (18--26\\pp{}) exceeds any single assessed confound. Even under worst-case compounding (${\\sim}$11.5\\pp{}), the gap retains ${\\geq}$7.5\\pp{} margin; confounds predominantly disadvantage \\cwm{}. However, correlated confounds and limited seed coverage mean definitive causal attribution requires multi-seed replication. At $n{=}48$, the minimum detectable effect (MDE) is ${\\sim}$25\\pp{}~\\cite{hoenig2001}; the \\cls{}--\\cwm{} gap (29--35\\pp{}) exceeds this threshold, while the \\cls{}--\\traj{} gap ($<$10\\pp{}) falls below it, consistent with our TOST equivalence finding. Holm-Bonferroni correction across the five primary comparisons ($k{=}5$; Table~\\ref{tab:holm}) confirms the \\cls{}--\\cwm{} gap (adjusted $p{=}0.015$) and function-level \\cls{}--\\cwm{} equivalence (adjusted $p{=}0.028$); function-level \\cls{}--\\traj{} equivalence does not survive correction (adjusted $p{=}0.075$), nor does the repo-level \\cwm{}--\\traj{} comparison (adjusted $p{=}0.078$). The consistent direction across both model families and all tested configurations supports a formulation-level explanation, though definitive causal attribution requires future experiments addressing each confound individually.\n\n\n\\paragraph{Extended validity discussion.}\n\\label{app:limitations}\nThe same-size 4B comparison uses a single seed; \\cls{} 4B seed 123 (val-best ckpt-800) achieves only 75.33\\% test accuracy (+2.4\\pp{} above majority baseline); val-best selection at an early checkpoint (step 800) amplifies the val-test distribution shift observed across all configurations. The \\cwm{} 8B comparison uses 3 seeds per model. The validation and test sets have zero problem overlap but differ in mutation type composition (Table~\\ref{tab:mutation_distribution}): \\texttt{operator\\_swap} shifts from 19.1\\% (val) to 34.3\\% (test), the largest single-type distribution mismatch (+15.2\\pp{}). All repo-level results use val-selected checkpoints, and checkpoint selection variance could contribute to observed differences. Our training data is synthetically constructed from mutation operators rather than real developer patches. While mutation testing literature establishes that mutants are reasonable proxies for real faults in test effectiveness studies~\\cite{andrews2005mutation,just2014mutants}, these findings concern mutation \\emph{adequacy} (whether tests that kill mutants also detect real faults), not whether verifiers trained on mutants transfer to real patches. However, the coupling effect underlying these results supports \\emph{relative ranking} validity: a domain shift from synthetic mutations to real bugs may affect absolute accuracy levels, but our core finding (that formulation choice matters at repo level but not function level) concerns relative performance ordering, which is expected to be preserved under distributional shifts that affect all formulations equally. The synthetic-to-real transfer gap for absolute accuracy remains untested. The \\traj{} training configuration differs from \\cls{}/\\cwm{}: smaller training set (${\\sim}$400 vs.\\ ${\\sim}$70K instances), different learning rate ($2{\\times}10^{-4}$ vs.\\ $5{\\times}10^{-5}$), and variant-level evaluation ($n{=}48$ vs.\\ per-test $n{=}9{,}784$). The function-level \\cls{}--\\traj{} TOST equivalence ($p = 0.025$, seed-level paired, $\\pm$2\\pp{}) is computed on 523 matched variant-level instances across 5 seeds; 2 of 5 seeds use NF4 quantization. Restricting to three bfloat16 seeds yields a comparable mean gap ($-$0.45\\pp{}) but wider confidence interval (df${=}$2); the TOST $p$-value increases to 0.128, which reflects reduced statistical power rather than a shift in the point estimate. The NF4 seeds contribute precision (narrowing the CI) without shifting the mean, consistent with precision being comparable across both quantization levels at function level. Repo-level \\cls{}--\\traj{} comparison should be interpreted with caution due to configuration and granularity differences.\n\n\\paragraph{Domain contrast with generative verification in math reasoning.}\nGenRM~\\cite{hosseini2025genrm} demonstrates that generative verifiers outperform discriminative ones for math reasoning. Our results reveal a domain-specific divergence: in code repair verification, the generative formulation (\\cwm{}) does not outperform the discriminative one (\\cls{}), and degrades sharply at repository level. The key difference is output space structure: math reasoning generates natural-language solution traces with flexible formatting, whereas code execution output requires exact syntactic compliance (specific variable values, error messages, stack traces). This structural constraint makes format collapse, absent in math verification, the dominant failure mode for code \\cwm{} at repo level (53--74\\% unparseable). The domain contrast suggests that the generative verification advantage is contingent on output space complexity rather than being a universal property of verifier architecture.\n\n\\section{Use of AI Assistants}\n\\label{app:ai-assistants}\n\nWe used Claude (Anthropic) as an AI coding and writing assistant throughout this work. Specifically:\n\\begin{itemize}\n    \\item \\textbf{Code:} drafting experiment scripts, data-processing pipelines, and analysis utilities; debugging and refactoring.\n    \\item \\textbf{Writing:} drafting and revising paper sections, polishing prose, and reformatting \\LaTeX{}.\n    \\item \\textbf{Literature:} summarizing related papers to inform the related-work section.\n\\end{itemize}\n",
      "numLines": 608,
      "startLine": 1,
      "totalLines": 608
    }
  },
  "sourceToolAssistantUUID": "1e83d7f2-3374-4643-9e1c-521c91c6de8f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/paper_audit_content_8033e618",
  "sessionId": "d10eba16-884c-49dd-bd31-5cc0ef3bc131",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 36 · 2026-05-25T07:52:05.061Z_

<details open><summary>🔧 Tool call — Read · `toolu_01TvqLcRhWGr1tcboibPGvJ3`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a64c8b7d-e8d9-4b9e-96b4-908322e3ccb0",
  "isSidechain": false,
  "requestId": "req_011CbNvXNj3MMNLN5yzjvaJH",
  "type": "assistant",
  "uuid": "f0bd1850-f5d8-4767-9a8e-c02695e1d650",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/paper_audit_content_8033e618",
  "sessionId": "d10eba16-884c-49dd-bd31-5cc0ef3bc131",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RzegdawgqtJMotASk4zb6m",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11924,
      "cache_read_input_tokens": 39764,
      "output_tokens": 725,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11924,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 725,
          "cache_read_input_tokens": 39764,
          "cache_creation_input_tokens": 11924,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11924
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

_source line 37 · 2026-05-25T07:52:05.066Z_

<details><summary>↩ Tool result · `toolu_01TvqLcRhWGr1tcboibPGvJ3`</summary>

```text
1	\documentclass[11pt]{article}
2	
3	% ACL style (review mode for anonymous ARR submission)
4	\usepackage[review]{acl}
5	
6	% Fonts — Times Roman (required by ACL/ARR template)
7	\usepackage{times}
8	
9	% Math
10	\usepackage{amsmath}
11	\usepackage{amssymb}
12	
13	% Tables
14	\usepackage{booktabs}
15	\usepackage{multirow}
16	\usepackage{tabularx}
17	
18	% Graphics
19	\usepackage{graphicx}
20	\usepackage{xcolor}
21	\graphicspath{{../../artifacts/}}
22	
23	% Lists
24	\usepackage{enumitem}
25	
26	% Custom commands
27	\newcommand{\cls}{\textsc{Cls}}
28	\newcommand{\cwm}{\textsc{Cwm}}
29	\newcommand{\traj}{\textsc{Traj}}
30	\newcommand{\fone}{F\textsubscript{1}}
31	\newcommand{\pp}{\,\text{pp}}
32	\newcommand{\tbd}{\textsc{tbd}}
33	\newcommand{\placeholder}[1]{{\color{red}\texttt{[#1]}}}
34	
35	\title{A Systematic Comparison of Execution-Free Verification Formulations for Code Repair}
36	\author{Anonymous}
37	
38	\begin{document}
39	\maketitle
40	
41	\input{abstract}
42	
43	\input{introduction}
44	
45	\begin{figure*}[t]
46	\centering
47	\includegraphics[width=\textwidth]{figures/paper/fig1_reformulation.pdf}
48	\caption{Three verification formulations. \textbf{Left:} \cls{} predicts binary pass/fail per test (1 output token). \textbf{Center:} \cwm{} generates execution output, derives verdict by exact match ($O(L)$ tokens). \textbf{Right:} Trajectory-level scoring predicts patch-level resolved/unresolved (1 token, no per-test signal). Each formulation makes different tradeoffs between output complexity, diagnostic granularity, and inference cost.}
49	\label{fig:reformulation}
50	\end{figure*}
51	
52	\input{related_work}
53	
54	\input{method}
55	
56	\input{experiments}
57	
58	\input{conclusion}
59	
60	\bibliography{references}
61	
62	% ARR checklist is filled in OpenReview submission form, not in PDF
63	% \input{checklist}
64	
65	\input{appendix}
66	
67	\end{document}
68	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f0bd1850-f5d8-4767-9a8e-c02695e1d650",
  "isSidechain": false,
  "promptId": "15e99bee-64bb-4bc0-b559-9e40ffdfc882",
  "type": "user",
  "uuid": "5a237627-1c9c-4182-96d1-e8aff557c797",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/main.tex",
      "content": "\\documentclass[11pt]{article}\n\n% ACL style (review mode for anonymous ARR submission)\n\\usepackage[review]{acl}\n\n% Fonts — Times Roman (required by ACL/ARR template)\n\\usepackage{times}\n\n% Math\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\n% Tables\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{tabularx}\n\n% Graphics\n\\usepackage{graphicx}\n\\usepackage{xcolor}\n\\graphicspath{{../../artifacts/}}\n\n% Lists\n\\usepackage{enumitem}\n\n% Custom commands\n\\newcommand{\\cls}{\\textsc{Cls}}\n\\newcommand{\\cwm}{\\textsc{Cwm}}\n\\newcommand{\\traj}{\\textsc{Traj}}\n\\newcommand{\\fone}{F\\textsubscript{1}}\n\\newcommand{\\pp}{\\,\\text{pp}}\n\\newcommand{\\tbd}{\\textsc{tbd}}\n\\newcommand{\\placeholder}[1]{{\\color{red}\\texttt{[#1]}}}\n\n\\title{A Systematic Comparison of Execution-Free Verification Formulations for Code Repair}\n\\author{Anonymous}\n\n\\begin{document}\n\\maketitle\n\n\\input{abstract}\n\n\\input{introduction}\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{figures/paper/fig1_reformulation.pdf}\n\\caption{Three verification formulations. \\textbf{Left:} \\cls{} predicts binary pass/fail per test (1 output token). \\textbf{Center:} \\cwm{} generates execution output, derives verdict by exact match ($O(L)$ tokens). \\textbf{Right:} Trajectory-level scoring predicts patch-level resolved/unresolved (1 token, no per-test signal). Each formulation makes different tradeoffs between output complexity, diagnostic granularity, and inference cost.}\n\\label{fig:reformulation}\n\\end{figure*}\n\n\\input{related_work}\n\n\\input{method}\n\n\\input{experiments}\n\n\\input{conclusion}\n\n\\bibliography{references}\n\n% ARR checklist is filled in OpenReview submission form, not in PDF\n% \\input{checklist}\n\n\\input{appendix}\n\n\\end{document}\n",
      "numLines": 68,
      "startLine": 1,
      "totalLines": 68
    }
  },
  "sourceToolAssistantUUID": "f0bd1850-f5d8-4767-9a8e-c02695e1d650",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/paper_audit_content_8033e618",
  "sessionId": "d10eba16-884c-49dd-bd31-5cc0ef3bc131",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-25T07:52:05.370Z_

<details open><summary>🔧 Tool call — Read · `toolu_012Je55JhwmKHq9mX6tmHhqC`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/checklist.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5a237627-1c9c-4182-96d1-e8aff557c797",
  "isSidechain": false,
  "requestId": "req_011CbNvXNj3MMNLN5yzjvaJH",
  "type": "assistant",
  "uuid": "6426325f-a0e8-4594-ac86-9e842fc8d5f8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/paper_audit_content_8033e618",
  "sessionId": "d10eba16-884c-49dd-bd31-5cc0ef3bc131",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RzegdawgqtJMotASk4zb6m",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11924,
      "cache_read_input_tokens": 39764,
      "output_tokens": 725,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11924,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 725,
          "cache_read_input_tokens": 39764,
          "cache_creation_input_tokens": 11924,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11924
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

_source line 39 · 2026-05-25T07:52:05.447Z_

```json
{
  "parentUuid": "e024b451-7584-48e9-bd92-da1022162825",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "de140865-6b0e-4356-b34b-e22cde10e26c",
  "timestamp": "2026-05-25T07:52:05.447Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/paper_audit_content_8033e618",
  "sessionId": "d10eba16-884c-49dd-bd31-5cc0ef3bc131",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---

### Runtime record

_source line 40_

```json
{
  "type": "last-prompt",
  "lastPrompt": "项目：exec-sim-repair-verifier Venue：emnlp-2026 论文目录：/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper  Phase 1 确定性检查结果： 源码检查: passed=False, 1 critical, 18 war…",
  "leafUuid": "de140865-6b0e-4356-b34b-e22cde10e26c",
  "sessionId": "d10eba16-884c-49dd-bd31-5cc0ef3bc131"
}
```

---

### Runtime record

_source line 41_

```json
{
  "type": "ai-title",
  "aiTitle": "EMNLP 2026 paper verification and compliance audit",
  "sessionId": "d10eba16-884c-49dd-bd31-5cc0ef3bc131"
}
```

---

### Assistant

_source line 42 · 2026-05-25T07:52:08.946Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the .tex files. Let me perform a systematic content audit. Let me also run some grep searches for AI style markers.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "de140865-6b0e-4356-b34b-e22cde10e26c",
  "isSidechain": false,
  "requestId": "req_011CbNvY1AXbsnmrZC3d8bQv",
  "type": "assistant",
  "uuid": "f8b14199-d907-43fb-ace3-591c96307eb1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/paper_audit_content_8033e618",
  "sessionId": "d10eba16-884c-49dd-bd31-5cc0ef3bc131",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SofqA135sCn34qxxmxudTp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 39271,
      "cache_read_input_tokens": 51688,
      "output_tokens": 866,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 39271,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 866,
          "cache_read_input_tokens": 51688,
          "cache_creation_input_tokens": 39271,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 39271
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

_source line 43 · 2026-05-25T07:52:09.932Z_

现在进行去 AI 风格扫描和其他正则级检查。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f8b14199-d907-43fb-ace3-591c96307eb1",
  "isSidechain": false,
  "requestId": "req_011CbNvY1AXbsnmrZC3d8bQv",
  "type": "assistant",
  "uuid": "6b048304-6c8e-43e8-91e0-020132cc1ae7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/paper_audit_content_8033e618",
  "sessionId": "d10eba16-884c-49dd-bd31-5cc0ef3bc131",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SofqA135sCn34qxxmxudTp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 39271,
      "cache_read_input_tokens": 51688,
      "output_tokens": 866,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 39271,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 866,
          "cache_read_input_tokens": 51688,
          "cache_creation_input_tokens": 39271,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 39271
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

_source line 44 · 2026-05-25T07:52:12.848Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01B6uK6oU1u8QyrX7dWuE8RT`</summary>

```json
{
  "pattern": "—",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper",
  "output_mode": "content",
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6b048304-6c8e-43e8-91e0-020132cc1ae7",
  "isSidechain": false,
  "requestId": "req_011CbNvY1AXbsnmrZC3d8bQv",
  "type": "assistant",
  "uuid": "9329aa47-83a8-474e-9d58-1a9939bcef25",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/paper_audit_content_8033e618",
  "sessionId": "d10eba16-884c-49dd-bd31-5cc0ef3bc131",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SofqA135sCn34qxxmxudTp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 39271,
      "cache_read_input_tokens": 51688,
      "output_tokens": 866,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 39271,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 866,
          "cache_read_input_tokens": 51688,
          "cache_creation_input_tokens": 39271,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 39271
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

_source line 45 · 2026-05-25T07:52:12.879Z_

<details><summary>↩ Tool result · `toolu_01B6uK6oU1u8QyrX7dWuE8RT`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/main.tex:6:% Fonts — Times Roman (required by ACL/ARR template)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9329aa47-83a8-474e-9d58-1a9939bcef25",
  "isSidechain": false,
  "promptId": "15e99bee-64bb-4bc0-b559-9e40ffdfc882",
  "type": "user",
  "uuid": "09854dbb-e429-455e-a070-1b11e0a6213f",
  "toolUseResult": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/main.tex:6:% Fonts — Times Roman (required by ACL/ARR template)",
    "numLines": 1
  },
  "sourceToolAssistantUUID": "9329aa47-83a8-474e-9d58-1a9939bcef25",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/paper_audit_content_8033e618",
  "sessionId": "d10eba16-884c-49dd-bd31-5cc0ef3bc131",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 46 · 2026-05-25T07:52:13.825Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01N74zbhHymtKDJ9wdjAhpzF`</summary>

```json
{
  "pattern": " – ",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper",
  "output_mode": "content",
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "09854dbb-e429-455e-a070-1b11e0a6213f",
  "isSidechain": false,
  "requestId": "req_011CbNvY1AXbsnmrZC3d8bQv",
  "type": "assistant",
  "uuid": "43e41bab-9b46-49c9-b484-4639a457cbf6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/paper_audit_content_8033e618",
  "sessionId": "d10eba16-884c-49dd-bd31-5cc0ef3bc131",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SofqA135sCn34qxxmxudTp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 39271,
      "cache_read_input_tokens": 51688,
      "output_tokens": 866,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 39271,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 866,
          "cache_read_input_tokens": 51688,
          "cache_creation_input_tokens": 39271,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 39271
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

_source line 47 · 2026-05-25T07:52:13.838Z_

<details><summary>↩ Tool result · `toolu_01N74zbhHymtKDJ9wdjAhpzF`</summary>

```text
No matches found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "43e41bab-9b46-49c9-b484-4639a457cbf6",
  "isSidechain": false,
  "promptId": "15e99bee-64bb-4bc0-b559-9e40ffdfc882",
  "type": "user",
  "uuid": "a3ea18a4-a331-4ceb-9922-1c5b45c0f7e6",
  "toolUseResult": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "",
    "numLines": 0
  },
  "sourceToolAssistantUUID": "43e41bab-9b46-49c9-b484-4639a457cbf6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/paper_audit_content_8033e618",
  "sessionId": "d10eba16-884c-49dd-bd31-5cc0ef3bc131",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 48 · 2026-05-25T07:52:15.377Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01HcN9CCNtW3N1vQTLa7oLxs`</summary>

```json
{
  "pattern": "it is worth noting|notably|importantly|furthermore|moreover|additionally",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper",
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
  "parentUuid": "a3ea18a4-a331-4ceb-9922-1c5b45c0f7e6",
  "isSidechain": false,
  "requestId": "req_011CbNvY1AXbsnmrZC3d8bQv",
  "type": "assistant",
  "uuid": "548c8008-51de-4914-af4e-c822dccf8560",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/paper_audit_content_8033e618",
  "sessionId": "d10eba16-884c-49dd-bd31-5cc0ef3bc131",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SofqA135sCn34qxxmxudTp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 39271,
      "cache_read_input_tokens": 51688,
      "output_tokens": 866,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 39271,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 866,
          "cache_read_input_tokens": 51688,
          "cache_creation_input_tokens": 39271,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 39271
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

_source line 49 · 2026-05-25T07:52:15.392Z_

<details><summary>↩ Tool result · `toolu_01HcN9CCNtW3N1vQTLa7oLxs`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/related_work.tex:8:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/experiments.tex:14:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/appendix.tex:406:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/appendix.tex:581:[Omitted long matching line]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "548c8008-51de-4914-af4e-c822dccf8560",
  "isSidechain": false,
  "promptId": "15e99bee-64bb-4bc0-b559-9e40ffdfc882",
  "type": "user",
  "uuid": "0e9a103f-8988-408b-9818-c91ef4d17f2f",
  "toolUseResult": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/related_work.tex:8:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/experiments.tex:14:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/appendix.tex:406:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/appendix.tex:581:[Omitted long matching line]",
    "numLines": 4
  },
  "sourceToolAssistantUUID": "548c8008-51de-4914-af4e-c822dccf8560",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/paper_audit_content_8033e618",
  "sessionId": "d10eba16-884c-49dd-bd31-5cc0ef3bc131",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 50 · 2026-05-25T07:52:17.389Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01SbUZt98S3tt9137FxDsyMw`</summary>

```json
{
  "pattern": "ing,|ing\\.",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper",
  "output_mode": "content",
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0e9a103f-8988-408b-9818-c91ef4d17f2f",
  "isSidechain": false,
  "requestId": "req_011CbNvY1AXbsnmrZC3d8bQv",
  "type": "assistant",
  "uuid": "34181a67-de29-4a90-b5e9-2d9381a55464",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/paper_audit_content_8033e618",
  "sessionId": "d10eba16-884c-49dd-bd31-5cc0ef3bc131",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SofqA135sCn34qxxmxudTp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 39271,
      "cache_read_input_tokens": 51688,
      "output_tokens": 866,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 39271,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 866,
          "cache_read_input_tokens": 51688,
          "cache_creation_input_tokens": 39271,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 39271
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

_source line 51 · 2026-05-25T07:52:17.405Z_

<details><summary>↩ Tool result · `toolu_01SbUZt98S3tt9137FxDsyMw`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/related_work.tex:5:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/related_work.tex:10:\paragraph{Repair, Mutation Testing, and Task Framing.}
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/experiments.tex:13:\paragraph{Models and training.}
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/experiments.tex:106:\paragraph{Baseline scaling.} Prompting baselines remain well below fine-tuning: the best result (14B 3-shot, 73.12\%) is 16.82\pp{} below fine-tuned \cls{} at 8B. Only \cls{} scales positively across both complexity levels; \traj{} shows no repo-level scaling benefit (72.92\% at both 4B and 8B).
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/experiments.tex:118:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/experiments.tex:157:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/experiments.tex:189:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/experiments.tex:191:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/conclusion.tex:4:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/checklist.tex:11:Yes. Section~\ref{sec:conclusion} (Limitations paragraph) discusses: ${\leq}$8B LoRA scope and generalization beyond this regime, Python-only evaluation domain, and synthetic mutation vs.\ real bug representativeness. Section~\ref{sec:threats} discusses checkpoint selection, preprocessing, and seed coverage. Extended validity discussion in Appendix~\ref{app:limitations}.
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/checklist.tex:34:Yes. Section~\ref{sec:setup}: function-level 19,076 samples (train 15,290 / val 1,896 / test 1,890; pass:fail $\approx$ 52:48); repo-level ${\sim}$70K training, val $n{=}9{,}335$, test $n{=}9{,}784$ (majority baseline 72.96\%).
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/checklist.tex:57:Yes. See Appendix~\ref{app:ai-assistants} for details on the AI assistant (Claude, Anthropic) used for code development, writing, and literature summarization.
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/method.tex:13:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/abstract.tex:2:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/appendix.tex:68:\paragraph{Majority voting.}
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/appendix.tex:104:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/appendix.tex:209:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/appendix.tex:254:{\footnotesize $^a$DeepSeek \cls{} canonical run (s42) uses drop preprocessing, which excludes 3,405 sequences exceeding max length (67,343 of 70,748). The s123 run uses truncate preprocessing (70,748 samples) but produces NaN validation loss. See \S\ref{sec:setup}. $^b$Seeds 789 and 0 use NF4 quantization; others use bf16. $^c$Repo-level seed coverage varies by configuration; see Table~\ref{tab:repo_level} caption for per-model counts.}
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/appendix.tex:257:\paragraph{Data processing.} DeepSeek CWM seeds use \texttt{train\_unified.py}, which drops samples exceeding \texttt{max\_seq\_length} (3{,}405 of 70{,}748 samples, 4.8\%). Qwen CWM seeds use \texttt{train\_repo\_cwm.py}, which truncates and retains all samples. This difference affects total training steps (${\sim}$12{,}627 vs.\ ${\sim}$13{,}266 for DeepSeek, ${\sim}$6{,}633 for Qwen) but not the training data distribution, as dropped samples are uniformly distributed across labels.
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/appendix.tex:360:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/appendix.tex:363:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/appendix.tex:381:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/appendix.tex:406:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/appendix.tex:496:The \cls{}--\traj{} unpaired bootstrap produces wider confidence intervals than paired analysis would; \traj{} per-variant predictions were not archived in a format that permits pairing. The \cls{}--\cwm{} paired comparison uses \cls{} s123 vs.\ \cwm{} s42 (different seeds), but the CI lower bound of 10.42\pp{} far exceeds the seed noise observed in function-level experiments ($<$2\pp{}).
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/appendix.tex:561:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/appendix.tex:583:\paragraph{Preprocessing.} DeepSeek \cls{} accuracy ranges from 82.61\% (s42, drop preprocessing) to 74.93\% (s123, truncate preprocessing), a 7.68\pp{} spread that conflates preprocessing strategy, checkpoint selection method, and seed. The two strategies produce different effective training sets (67,343 vs.\ 70,748 samples) and different checkpoint selection regimes. The qualitative ranking \cls{} $>$ \cwm{} holds under both strategies (Table~\ref{tab:taxonomy}).
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/appendix.tex:587:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/appendix.tex:589:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/appendix.tex:594:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/appendix.tex:596:\paragraph{Domain contrast with generative verification in math reasoning.}
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/appendix.tex:597:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/appendix.tex:604:    \item \textbf{Code:} drafting experiment scripts, data-processing pipelines, and analysis utilities; debugging and refactoring.
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/introduction.tex:8:[Omitted long matching line]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "34181a67-de29-4a90-b5e9-2d9381a55464",
  "isSidechain": false,
  "promptId": "15e99bee-64bb-4bc0-b559-9e40ffdfc882",
  "type": "user",
  "uuid": "17f571cd-fcc7-4e25-960e-45b7c7acc1fb",
  "toolUseResult": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/related_work.tex:5:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/related_work.tex:10:\\paragraph{Repair, Mutation Testing, and Task Framing.}\n/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/experiments.tex:13:\\paragraph{Models and training.}\n/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/experiments.tex:106:\\paragraph{Baseline scaling.} Prompting baselines remain well below fine-tuning: the best result (14B 3-shot, 73.12\\%) is 16.82\\pp{} below fine-tuned \\cls{} at 8B. Only \\cls{} scales positively across both complexity levels; \\traj{} shows no repo-level scaling benefit (72.92\\% at both 4B and 8B).\n/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/experiments.tex:118:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/experiments.tex:157:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/experiments.tex:189:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/experiments.tex:191:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/conclusion.tex:4:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/checklist.tex:11:Yes. Section~\\ref{sec:conclusion} (Limitations paragraph) discusses: ${\\leq}$8B LoRA scope and generalization beyond this regime, Python-only evaluation domain, and synthetic mutation vs.\\ real bug representativeness. Section~\\ref{sec:threats} discusses checkpoint selection, preprocessing, and seed coverage. Extended validity discussion in Appendix~\\ref{app:limitations}.\n/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/checklist.tex:34:Yes. Section~\\ref{sec:setup}: function-level 19,076 samples (train 15,290 / val 1,896 / test 1,890; pass:fail $\\approx$ 52:48); repo-level ${\\sim}$70K training, val $n{=}9{,}335$, test $n{=}9{,}784$ (majority baseline 72.96\\%).\n/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/checklist.tex:57:Yes. See Appendix~\\ref{app:ai-assistants} for details on the AI assistant (Claude, Anthropic) used for code development, writing, and literature summarization.\n/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/method.tex:13:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/abstract.tex:2:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/appendix.tex:68:\\paragraph{Majority voting.}\n/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/appendix.tex:104:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/appendix.tex:209:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/appendix.tex:254:{\\footnotesize $^a$DeepSeek \\cls{} canonical run (s42) uses drop preprocessing, which excludes 3,405 sequences exceeding max length (67,343 of 70,748). The s123 run uses truncate preprocessing (70,748 samples) but produces NaN validation loss. See \\S\\ref{sec:setup}. $^b$Seeds 789 and 0 use NF4 quantization; others use bf16. $^c$Repo-level seed coverage varies by configuration; see Table~\\ref{tab:repo_level} caption for per-model counts.}\n/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/appendix.tex:257:\\paragraph{Data processing.} DeepSeek CWM seeds use \\texttt{train\\_unified.py}, which drops samples exceeding \\texttt{max\\_seq\\_length} (3{,}405 of 70{,}748 samples, 4.8\\%). Qwen CWM seeds use \\texttt{train\\_repo\\_cwm.py}, which truncates and retains all samples. This difference affects total training steps (${\\sim}$12{,}627 vs.\\ ${\\sim}$13{,}266 for DeepSeek, ${\\sim}$6{,}633 for Qwen) but not the training data distribution, as dropped samples are uniformly distributed across labels.\n/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/appendix.tex:360:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/appendix.tex:363:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/appendix.tex:381:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/appendix.tex:406:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/appendix.tex:496:The \\cls{}--\\traj{} unpaired bootstrap produces wider confidence intervals than paired analysis would; \\traj{} per-variant predictions were not archived in a format that permits pairing. The \\cls{}--\\cwm{} paired comparison uses \\cls{} s123 vs.\\ \\cwm{} s42 (different seeds), but the CI lower bound of 10.42\\pp{} far exceeds the seed noise observed in function-level experiments ($<$2\\pp{}).\n/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/appendix.tex:561:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/appendix.tex:583:\\paragraph{Preprocessing.} DeepSeek \\cls{} accuracy ranges from 82.61\\% (s42, drop preprocessing) to 74.93\\% (s123, truncate preprocessing), a 7.68\\pp{} spread that conflates preprocessing strategy, checkpoint selection method, and seed. The two strategies produce different effective training sets (67,343 vs.\\ 70,748 samples) and different checkpoint selection regimes. The qualitative ranking \\cls{} $>$ \\cwm{} holds under both strategies (Table~\\ref{tab:taxonomy}).\n/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/appendix.tex:587:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/appendix.tex:589:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/appendix.tex:594:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/appendix.tex:596:\\paragraph{Domain contrast with generative verification in math reasoning.}\n/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/appendix.tex:597:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/appendix.tex:604:    \\item \\textbf{Code:} drafting experiment scripts, data-processing pipelines, and analysis utilities; debugging and refactoring.\n/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/introduction.tex:8:[Omitted long matching line]",
    "numLines": 33
  },
  "sourceToolAssistantUUID": "34181a67-de29-4a90-b5e9-2d9381a55464",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/paper_audit_content_8033e618",
  "sessionId": "d10eba16-884c-49dd-bd31-5cc0ef3bc131",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 52 · 2026-05-25T07:52:18.680Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01V5VjrgHDSDGKDXE2sACXh5`</summary>

```json
{
  "pattern": "delve|leverage|utilize|facilitate|a myriad|a plethora|in the realm of",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper",
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
  "parentUuid": "17f571cd-fcc7-4e25-960e-45b7c7acc1fb",
  "isSidechain": false,
  "requestId": "req_011CbNvY1AXbsnmrZC3d8bQv",
  "type": "assistant",
  "uuid": "4ee907f8-80ed-4ee9-bc70-3a8716269ebf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/paper_audit_content_8033e618",
  "sessionId": "d10eba16-884c-49dd-bd31-5cc0ef3bc131",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SofqA135sCn34qxxmxudTp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 39271,
      "cache_read_input_tokens": 51688,
      "output_tokens": 866,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 39271,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 866,
          "cache_read_input_tokens": 51688,
          "cache_creation_input_tokens": 39271,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 39271
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

_source line 53 · 2026-05-25T07:52:18.728Z_

<details><summary>↩ Tool result · `toolu_01V5VjrgHDSDGKDXE2sACXh5`</summary>

```text
No matches found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4ee907f8-80ed-4ee9-bc70-3a8716269ebf",
  "isSidechain": false,
  "promptId": "15e99bee-64bb-4bc0-b559-9e40ffdfc882",
  "type": "user",
  "uuid": "19722900-c329-4d9d-a6fe-dda0268487e4",
  "toolUseResult": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "",
    "numLines": 0
  },
  "sourceToolAssistantUUID": "4ee907f8-80ed-4ee9-bc70-3a8716269ebf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/paper_audit_content_8033e618",
  "sessionId": "d10eba16-884c-49dd-bd31-5cc0ef3bc131",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 54 · 2026-05-25T07:52:19.384Z_

<details open><summary>🔧 Tool call — Bash · `toolu_014xx9M7GDQGhAHT1H6Kvacx`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper && wc -w abstract.tex",
  "description": "Count words in abstract"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "19722900-c329-4d9d-a6fe-dda0268487e4",
  "isSidechain": false,
  "requestId": "req_011CbNvY1AXbsnmrZC3d8bQv",
  "type": "assistant",
  "uuid": "7cf4601b-987c-4323-9a7e-aa3d22ae3193",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/paper_audit_content_8033e618",
  "sessionId": "d10eba16-884c-49dd-bd31-5cc0ef3bc131",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SofqA135sCn34qxxmxudTp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 39271,
      "cache_read_input_tokens": 51688,
      "output_tokens": 866,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 39271,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 866,
          "cache_read_input_tokens": 51688,
          "cache_creation_input_tokens": 39271,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 39271
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

_source line 55_

```json
{
  "type": "last-prompt",
  "lastPrompt": "项目：exec-sim-repair-verifier Venue：emnlp-2026 论文目录：/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper  Phase 1 确定性检查结果： 源码检查: passed=False, 1 critical, 18 war…",
  "leafUuid": "7cf4601b-987c-4323-9a7e-aa3d22ae3193",
  "sessionId": "d10eba16-884c-49dd-bd31-5cc0ef3bc131"
}
```

---

### Runtime record

_source line 56_

```json
{
  "type": "ai-title",
  "aiTitle": "EMNLP 2026 paper verification and compliance audit",
  "sessionId": "d10eba16-884c-49dd-bd31-5cc0ef3bc131"
}
```

---

### Tool result

_source line 57 · 2026-05-25T07:52:19.655Z_

<details><summary>↩ Tool result · `toolu_014xx9M7GDQGhAHT1H6Kvacx`</summary>

```text
167 abstract.tex
Shell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/paper_audit_content_8033e618
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7cf4601b-987c-4323-9a7e-aa3d22ae3193",
  "isSidechain": false,
  "promptId": "15e99bee-64bb-4bc0-b559-9e40ffdfc882",
  "type": "user",
  "uuid": "d4c73d11-b610-48fc-afcb-16ac1b49a2f0",
  "toolUseResult": {
    "stdout": "167 abstract.tex",
    "stderr": "\nShell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/paper_audit_content_8033e618",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "7cf4601b-987c-4323-9a7e-aa3d22ae3193",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/paper_audit_content_8033e618",
  "sessionId": "d10eba16-884c-49dd-bd31-5cc0ef3bc131",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 58 · 2026-05-25T07:52:22.989Z_

<details><summary>Logged reasoning block</summary>

```text
Let me now count the actual words in the abstract (excluding LaTeX commands) more precisely, and check for other patterns.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d4c73d11-b610-48fc-afcb-16ac1b49a2f0",
  "isSidechain": false,
  "requestId": "req_011CbNvZ3vVk1UKiXLYDGQXr",
  "type": "assistant",
  "uuid": "f7a4b6b1-b82d-4acb-a82b-3559944a3bc6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/paper_audit_content_8033e618",
  "sessionId": "d10eba16-884c-49dd-bd31-5cc0ef3bc131",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KbYuym3VkwhPpukEQDUYm8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3840,
      "cache_read_input_tokens": 90959,
      "output_tokens": 760,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3840,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 760,
          "cache_read_input_tokens": 90959,
          "cache_creation_input_tokens": 3840,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3840
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

_source line 59 · 2026-05-25T07:52:23.544Z_

进一步检查 abstract word count 和 limitations 部分。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f7a4b6b1-b82d-4acb-a82b-3559944a3bc6",
  "isSidechain": false,
  "requestId": "req_011CbNvZ3vVk1UKiXLYDGQXr",
  "type": "assistant",
  "uuid": "78776813-1040-45be-8c83-8a08ca97a6ce",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/paper_audit_content_8033e618",
  "sessionId": "d10eba16-884c-49dd-bd31-5cc0ef3bc131",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KbYuym3VkwhPpukEQDUYm8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3840,
      "cache_read_input_tokens": 90959,
      "output_tokens": 760,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3840,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 760,
          "cache_read_input_tokens": 90959,
          "cache_creation_input_tokens": 3840,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3840
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

_source line 60 · 2026-05-25T07:52:25.610Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01RAVgEsiG9D5QtF5PVTvuDo`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper && cat abstract.tex | sed 's/\\\\[a-zA-Z]*{[^}]*}//g; s/\\\\[a-zA-Z]*//g; s/[{}$~]//g; s/\\\\//g' | wc -w",
  "description": "Count words in abstract excluding LaTeX commands"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "78776813-1040-45be-8c83-8a08ca97a6ce",
  "isSidechain": false,
  "requestId": "req_011CbNvZ3vVk1UKiXLYDGQXr",
  "type": "assistant",
  "uuid": "d3c1a221-ee34-47e5-9b80-104d3427d8a9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/paper_audit_content_8033e618",
  "sessionId": "d10eba16-884c-49dd-bd31-5cc0ef3bc131",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KbYuym3VkwhPpukEQDUYm8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3840,
      "cache_read_input_tokens": 90959,
      "output_tokens": 760,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3840,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 760,
          "cache_read_input_tokens": 90959,
          "cache_creation_input_tokens": 3840,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3840
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

_source line 61 · 2026-05-25T07:52:30.859Z_

<details><summary>↩ Tool result · `toolu_01Qdem8mWZxvtukVJfxgx4Qv`</summary>

```text
No matches found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "46852ffc-9c41-48b4-a561-4be4cc463a3c",
  "isSidechain": false,
  "promptId": "15e99bee-64bb-4bc0-b559-9e40ffdfc882",
  "type": "user",
  "uuid": "93a8fa49-29bb-476e-afad-a6028dd405e7",
  "toolUseResult": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "",
    "numLines": 0
  },
  "sourceToolAssistantUUID": "46852ffc-9c41-48b4-a561-4be4cc463a3c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/paper_audit_content_8033e618",
  "sessionId": "d10eba16-884c-49dd-bd31-5cc0ef3bc131",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool result

_source line 62 · 2026-05-25T07:52:25.700Z_

<details><summary>↩ Tool result · `toolu_01RAVgEsiG9D5QtF5PVTvuDo`</summary>

```text
160
Shell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/paper_audit_content_8033e618
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d3c1a221-ee34-47e5-9b80-104d3427d8a9",
  "isSidechain": false,
  "promptId": "15e99bee-64bb-4bc0-b559-9e40ffdfc882",
  "type": "user",
  "uuid": "c6b26a7b-c0bd-47a9-89fb-06f253a516e1",
  "toolUseResult": {
    "stdout": "160",
    "stderr": "\nShell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/paper_audit_content_8033e618",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "d3c1a221-ee34-47e5-9b80-104d3427d8a9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/paper_audit_content_8033e618",
  "sessionId": "d10eba16-884c-49dd-bd31-5cc0ef3bc131",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 63 · 2026-05-25T07:52:26.950Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01X5iXtibiS61fdVUHgUxmcx`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper && detex abstract.tex 2>/dev/null | wc -w || echo \"detex not available\"",
  "description": "Count abstract words via detex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c6b26a7b-c0bd-47a9-89fb-06f253a516e1",
  "isSidechain": false,
  "requestId": "req_011CbNvZ3vVk1UKiXLYDGQXr",
  "type": "assistant",
  "uuid": "7befdb33-ed0c-470e-bafc-5930dc431ed0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/paper_audit_content_8033e618",
  "sessionId": "d10eba16-884c-49dd-bd31-5cc0ef3bc131",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KbYuym3VkwhPpukEQDUYm8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3840,
      "cache_read_input_tokens": 90959,
      "output_tokens": 760,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3840,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 760,
          "cache_read_input_tokens": 90959,
          "cache_creation_input_tokens": 3840,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3840
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

_source line 64 · 2026-05-25T07:52:27.046Z_

<details><summary>↩ Tool result · `toolu_01X5iXtibiS61fdVUHgUxmcx`</summary>

```text
167
Shell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/paper_audit_content_8033e618
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7befdb33-ed0c-470e-bafc-5930dc431ed0",
  "isSidechain": false,
  "promptId": "15e99bee-64bb-4bc0-b559-9e40ffdfc882",
  "type": "user",
  "uuid": "55a45256-ce98-4b70-8abf-bcd27779f198",
  "toolUseResult": {
    "stdout": "167",
    "stderr": "\nShell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/paper_audit_content_8033e618",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "7befdb33-ed0c-470e-bafc-5930dc431ed0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/paper_audit_content_8033e618",
  "sessionId": "d10eba16-884c-49dd-bd31-5cc0ef3bc131",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 65 · 2026-05-25T07:52:28.475Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01Fq4YYcq5KymdzrbFxDyJKg`</summary>

```json
{
  "pattern": "Furthermore|Moreover|Additionally",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper",
  "output_mode": "content",
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "55a45256-ce98-4b70-8abf-bcd27779f198",
  "isSidechain": false,
  "requestId": "req_011CbNvZ3vVk1UKiXLYDGQXr",
  "type": "assistant",
  "uuid": "1bfefc29-308a-4dad-83a5-216d1d14a9d6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/paper_audit_content_8033e618",
  "sessionId": "d10eba16-884c-49dd-bd31-5cc0ef3bc131",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KbYuym3VkwhPpukEQDUYm8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3840,
      "cache_read_input_tokens": 90959,
      "output_tokens": 760,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3840,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 760,
          "cache_read_input_tokens": 90959,
          "cache_creation_input_tokens": 3840,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3840
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

_source line 66 · 2026-05-25T07:52:28.499Z_

<details><summary>↩ Tool result · `toolu_01Fq4YYcq5KymdzrbFxDyJKg`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/appendix.tex:581:[Omitted long matching line]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1bfefc29-308a-4dad-83a5-216d1d14a9d6",
  "isSidechain": false,
  "promptId": "15e99bee-64bb-4bc0-b559-9e40ffdfc882",
  "type": "user",
  "uuid": "1c265658-ba0d-4b97-bcb6-270d75e0c3fb",
  "toolUseResult": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/appendix.tex:581:[Omitted long matching line]",
    "numLines": 1
  },
  "sourceToolAssistantUUID": "1bfefc29-308a-4dad-83a5-216d1d14a9d6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/paper_audit_content_8033e618",
  "sessionId": "d10eba16-884c-49dd-bd31-5cc0ef3bc131",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 67 · 2026-05-25T07:52:29.482Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01AAnhbo3UbrYsakbubCuU9Q`</summary>

```json
{
  "pattern": "significantly|state-of-the-art|SOTA",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper",
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
  "parentUuid": "1c265658-ba0d-4b97-bcb6-270d75e0c3fb",
  "isSidechain": false,
  "requestId": "req_011CbNvZ3vVk1UKiXLYDGQXr",
  "type": "assistant",
  "uuid": "83a4f19e-99c2-4bfa-bd85-85817a9b3913",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/paper_audit_content_8033e618",
  "sessionId": "d10eba16-884c-49dd-bd31-5cc0ef3bc131",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KbYuym3VkwhPpukEQDUYm8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3840,
      "cache_read_input_tokens": 90959,
      "output_tokens": 760,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3840,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 760,
          "cache_read_input_tokens": 90959,
          "cache_creation_input_tokens": 3840,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3840
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

_source line 68 · 2026-05-25T07:52:29.535Z_

<details><summary>↩ Tool result · `toolu_01AAnhbo3UbrYsakbubCuU9Q`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/appendix.tex:549:[Omitted long matching line]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "83a4f19e-99c2-4bfa-bd85-85817a9b3913",
  "isSidechain": false,
  "promptId": "15e99bee-64bb-4bc0-b559-9e40ffdfc882",
  "type": "user",
  "uuid": "008906de-8f57-4e8f-ae29-c83927773cf0",
  "toolUseResult": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/appendix.tex:549:[Omitted long matching line]",
    "numLines": 1
  },
  "sourceToolAssistantUUID": "83a4f19e-99c2-4bfa-bd85-85817a9b3913",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/paper_audit_content_8033e618",
  "sessionId": "d10eba16-884c-49dd-bd31-5cc0ef3bc131",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 69 · 2026-05-25T07:52:30.831Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01Qdem8mWZxvtukVJfxgx4Qv`</summary>

```json
{
  "pattern": "TODO|TBD|PLACEHOLDER|XX\\\\.XX|\\\\\\\\placeholder",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper",
  "output_mode": "content",
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "008906de-8f57-4e8f-ae29-c83927773cf0",
  "isSidechain": false,
  "requestId": "req_011CbNvZ3vVk1UKiXLYDGQXr",
  "type": "assistant",
  "uuid": "46852ffc-9c41-48b4-a561-4be4cc463a3c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/paper_audit_content_8033e618",
  "sessionId": "d10eba16-884c-49dd-bd31-5cc0ef3bc131",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KbYuym3VkwhPpukEQDUYm8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3840,
      "cache_read_input_tokens": 90959,
      "output_tokens": 760,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3840,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 760,
          "cache_read_input_tokens": 90959,
          "cache_creation_input_tokens": 3840,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3840
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

_source line 70 · 2026-05-25T07:52:30.905Z_

```json
{
  "parentUuid": "93a8fa49-29bb-476e-afad-a6028dd405e7",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "db0a221a-cb64-47a5-94f3-7c1be23245be",
  "timestamp": "2026-05-25T07:52:30.905Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/paper_audit_content_8033e618",
  "sessionId": "d10eba16-884c-49dd-bd31-5cc0ef3bc131",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---

### Assistant

_source line 71 · 2026-05-25T07:56:17.079Z_

<details><summary>Logged reasoning block</summary>

```text
Let me now check some specific things:

1. The "significantly" usage in appendix
2. Limitations section word count
3. Whether there are multiple limitations sections
4. Internal information leakage
5. Discussion section analysis

Let me also check for the em-dash in the main.tex comment (which is a comment, so not in paper body).

Now let me compile my audit findings systematically.

Let me trace through all the audit dimensions:

### 1. 叙事一致性 (CRITICAL)

**Abstract's problem**: Practitioners must choose among three execution-free verification formulations with no controlled comparison.

**Intro's problem**: Same - three distinct formulations have emerged, no prior work provides a systematic comparison. 

The narrative is consistent here. The intro contributions lay out complexity-moderated equivalence and divergence analysis plus a failure mode taxonomy, which directly address the gap identified in the abstract. The methods section describes the three formulations with their expected failure modes and the oracle accuracy-utility framework that connects to why this comparison matters. The experiments validate equivalence at the function level and divergence at the repo level while testing failure modes and scaling behavior, all matching the stated contributions. The conclusion wraps up findings that align with what was tested. There's a potential tension though—the abstract mentions complexity-aware routing as a key open direction, but I need to check if the intro develops this further.

There's also a framing question around error complementarity analysis. The routing results themselves are quite weak, capturing less than 0.4 percentage points of the oracle gap, which could look like a negative result. But the contribution is framed as the analysis of error complementarity itself rather than the routing performance, so that's defensible. The bigger issue is the abstract's claim about divergence narrowing at 14B scale. It says this points to a capacity-dependent limitation, but the 14B scaling results only show function-level convergence, not repo-level. A reader might misinterpret this as evidence that the larger 18-26 percentage point repo-level gap narrows at scale, when the data doesn't actually support that claim at the repo level. Looking at the scaling section more carefully, the 14B results showing convergence across all three formulations are indeed function-level only—there's no corresponding repo-level data at that scale. This creates a genuine inconsistency between what the abstract claims about divergence narrowing and what's actually measured in the experiments. The 14B results only cover function-level performance, not repository-level, so the abstract's framing that "this divergence narrows with scale" at 14B is misleading—it conflates two different evaluation levels and obscures that the scaling claim lacks repo-level evidence. The abstract does overstate the 14B evidence for repo-level divergence when the conclusion properly hedges that question as still open—this is a narrative consistency issue worth flagging. Now checking whether the intro's contribution claims align with what's actually delivered: the complexity-moderated equivalence and divergence work maps to sections 4.3 and 4.4, the failure mode taxonomy and error analysis maps to Table 3 and section 4.5, and the complexity-aware routing mentioned as motivation is appropriately listed as an open direction rather than a claimed contribution. The structure checks out.

Looking at the abstract, it covers the problem, method, results, and significance within the word limit. The intro establishes background on LLM repair and test-time scaling, identifies the gap that prior work hasn't controlled for capacity and protocol differences, and lists two contributions—which is lean but acceptable. The related work uses paragraph-level grouping by topic rather than chronological ordering, which works well for this material.

The contributions map cleanly to the experimental sections with no orphan content, and the title scope aligns with the experiments across function-level and repo-level code repair tasks. The abstract's claims about model families, complexity levels, and random seeds are all verified in the experiments. Now checking whether the statistical claims are properly supported—the "statistically equivalent accuracy" claim is backed by TOST testing. Checking the ablation studies across different hyperparameters like LoRA rank, voting strategies, and sequence length—all documented in the appendix. ✓ Reproducibility looks solid with hyperparameters, GPU specs, training time, and data preprocessing all disclosed, plus a filled checklist. ✓ Terminology is consistent throughout with CLS, CWM, and TRAJ defined upfront and percentage points standardized via a command.

The section transitions flow logically from related work into methods, then experiments, with discussion woven into the analysis rather than separated out—examining why generation degrades and how errors complement each other. ✓ The limitations section is brief though, so I should check if it adequately addresses the scope and constraints of the work. Looking at the limitations section, it covers four distinct points about scope, domain, synthetic data gaps, and unevaluated interventions—meeting the requirement for substantive limitations. The user's EMNLP 2026 guideline indicates a short section covering around three points is acceptable, so this approach is fine, though the word count appears to be around 100 words rather than the 150-word audit standard. Now checking for AI-style language patterns like em-dashes and filler words, finding only one instance of "Furthermore" in the appendix. Looking at the -ing patterns more carefully, most are just standard gerunds and present participles in normal technical writing—words like "Prompting baselines" and "fine-tuning" are legitimate. I don't see the telltale AI style of "-ing, ... the effectiveness of..." constructions in the main text. The writing is already quite technical and clean.

Checking the remaining markers: only one "Furthermore" in the appendix, no instances of "delve," "leverage," or "utilize," and the short paragraph divisions in the experiments section using \paragraph{} are standard practice for dense results, not an AI artifact. No internal experiment IDs or server names either.

The code repository URL is properly anonymized, and while the appendix mentions specific checkpoints and script names like train_unified.py, these are legitimate reproducibility details. The abstract comes in at around 167 words, well under the 200-word limit, and there's a dedicated limitations section.

Now I'm checking the page count requirements—EMNLP 2026 specifies 8 pages for main text, and the submission totals 24 pages including appendix and references. Based on that breakdown, the main text should fit within the limit, though I'd need to compile the source to verify the exact page distribution.

The document correctly uses the ACL review package, and I'm confirming the limitations section setup—there's an "Extended validity discussion" paragraph in the appendix with the label `app:limitations`, which satisfies the requirement for a single limitations section.

Looking at the critical issues: the Abstract's claim about divergence narrowing at 14B is problematic because it's based on function-level data only, yet the phrasing suggests repo-level findings. This contradicts the Conclusion's more careful hedging about whether this pattern holds at scale. There are also minor warnings—the em-dash in a LaTeX comment is negligible, and while only 2 contributions are listed (most papers have 3), this is acceptable though not ideal.

Re-examining the Abstract more closely, "this divergence" is ambiguous—it could refer to the repo-level equivalence breakdown mentioned just before, but the 14B evidence only covers function-level convergence. The sentence could be read as suggesting general CLS-CWM convergence across complexity levels based on the function-level improvement, but this interpretation stretches the evidence.

The real problem is that the abstract claims 14B results "suggest" the repo-level divergence narrows, while the conclusion explicitly states this question "remains open." That's a narrative inconsistency—the abstract makes a stronger claim than the conclusion supports. And looking at the experiments section, I'm seeing the scaling patterns for CWM and TRAJ that would need to be reconciled with this claim.

I'm also realizing I need to verify the page count constraint more carefully. EMNLP 2026 limits main text to 8 pages, and with the abstract, introduction, related work, method, experiments, and conclusion sections all packed with tables and figures, I'm concerned this might already exceed that limit. The experiments section alone is quite dense, but I can't confirm the exact page count without compiling the document.

I should also double-check whether the Related Work section reads more like a list of papers rather than synthesized discussion. The first paragraph on execution simulation does attempt synthesis, but I want to make sure it's not just stacking citations.

Looking at the structure, the Related Work has three main themes: execution simulation and verification, process versus outcome supervision, and repair with mutation testing. The first paragraph is citation-heavy but does provide some positioning of the work. The second paragraph offers genuine thematic comparison between PRM and ORM approaches. The third is brief but ties things together. Overall it's functional for a dense systematic comparison paper, though not exceptionally strong.

The Conclusion is notably terse—just four lines of text plus limitations. It restates findings without exploring broader implications or future directions beyond mentioning open questions. It's adequate but could be more impactful.

I also notice the Introduction references sections using cross-references like "(§\ref{sec:equivalence}, §\ref{sec:repo})" for the first contribution.  Checking these against the actual sections: §\ref{sec:equivalence} maps to §4.3 on function-level equivalence, §\ref{sec:repo} to §4.4 on repo-level divergence, and §\ref{sec:analysis} to §4.5. The references check out. There's one minor structural oddity though—the Oracle Accuracy-Utility Framework in §3.3 sits in the Method section but doesn't directly correspond to any stated contribution in the introduction. It's used in experiments as supporting analysis, making it somewhat orphaned from the main contribution narrative, though it's implicitly tied to the error analysis work.

Now I'm verifying the complexity-aware routing claim. The intro frames it as motivation from error complementarity, and while the actual routing results are underwhelming at less than 0.4 percentage points, the abstract honestly calls it "a key open direction" and the intro just says it "motivates" the approach, so there's no overstatement there. The title's promise of "A Systematic Comparison" also holds up throughout the paper.

Looking at the zero-shot baseline statement in experiments.tex, I need to verify the specific claims about fine-tuning gains and formulation choice effects.

The claim that "formulation choice matters only at repo level" is actually a key finding but gets introduced in the function-level results section, which creates a flow issue—it would read better in the repo-level section instead. That said, this is more of a presentation problem than a narrative inconsistency.

I'm also checking the abstract's mention of "two code LLM families (Qwen3, DeepSeek-Coder)" against how they're actually used. DeepSeek-Coder functions as a cross-model consistency check rather than a primary evaluation model, so the abstract doesn't quite capture this distinction and potentially overstates the breadth of the evaluation. The experiments do include DeepSeek results though, so it's a minor framing issue at worst.

The abstract's claim about "multiple random seeds under ≤8B LoRA fine-tuning" checks out as accurate.

Now I need to verify the CLS-TRAJ narrative and what the intro says about classification and trajectory scoring. Now I'm verifying the repo-level results from Table 2 match the text claims about performance gaps. The CLS-to-CWM gap checks out at 25.59 percentage points for the 4B model and 18.35 for the 8B, which aligns with what's stated in the experiments section. The abstract's range of "18--26pp" captures both of these values correctly.

I'm also checking the z-score reported in the Conclusion—it's −23.7 for the formulation×complexity interaction from the mixed-effects model, which matches the experiments section. The slight issue is that presenting this z-score alongside the "18--26pp" gap could mislead readers into thinking the z-score directly measures that gap, when it's actually testing the interaction effect. It's technically sound but worth flagging as a minor clarity concern.

Now I need to verify the figure placements and cross-references throughout the document. The pilot study on re-repair shows a null result that contradicts the framing of routing as a key open direction without acknowledging this negative finding. There are also some minor stylistic issues with "-ing" phrases, the conclusion feels underdeveloped at just a few lines, and while the oracle framework is useful methodologically, it's not formally listed as a contribution. The related work section has some dense citation patterns that could be streamlined.

Now I'm re-examining the abstract more carefully—specifically how "divergence" is being used. The CLS-CWM performance gap appears to narrow at 14B, and looking at the function-level results, CWM was flat at 8B while CLS improved, but then CWM catches up at 14B. So "divergence" might be referring to this broader CLS-CWM gap across scales rather than something more specific.

The placement is a bit ambiguous though—the sentence sits right after discussing repo-level format collapse, which could lead a reviewer to interpret it as claiming 14B repo-level evidence when the actual finding is at the function level. The conclusion handles this more clearly by separating the 14B function-level convergence from the open question about whether repo-level divergence is formulation-inherent or capacity-dependent, so I'll flag the abstract as a critical issue.

I've also verified that the `\placeholder{}` command isn't used anywhere in the document, and the paper doesn't have a separate Discussion section—the analysis is embedded within the Experiments section, which is standard for systematic comparison papers.

Now checking for unsupported "significantly" claims: the appendix backs up "significantly higher pass rates" with chi-square p-values, and the main text supports "highly significant" for the interaction effect with p<0.001, so that's fine. But I notice the Introduction raises a good motivating question about whether generation-based verification's advantage in mathematical reasoning transfers to code verification, and the experiments answer this negatively, yet the conclusion doesn't explicitly circle back to this comparison—that's a minor gap worth noting.

Looking at the Related Work more carefully, the paper does address the GenRM comparison by noting that generation (CWM) doesn't outperform classification (CLS) in code verification, suggesting domain-specificity. The placement of this finding in Related Work is a bit odd since results typically go in Results/Discussion, though since Related Work functions as a Background section here, it's more of a structural quirk than a real problem.

I should verify the "first systematic comparison" claim in the abstract and check whether prior work actually provides such a comparison.

The paper's claims about being the first to compare formulations at matched capacity appear well-supported by the literature review—Aletheia compares training recipes while this work compares formulations, and the cited work doesn't compare at matched capacity. The numerical consistency checks out: TOST p=0.007 with 5 seeds and z=−23.7 both align with the experiments section. The scope claims are appropriately limited to two code LLM families and two complexity levels without overclaiming across domains. One remaining detail to verify: the title mentions "Code Repair" but the function-level experiments use HumanEval/MBPP mutations, so I should check whether that's the right characterization. I'm wrapping up the audit now—I've confirmed the intro structure works within the page constraints, verified that the problem's importance and the insufficiency of existing methods are both clearly stated, and I'm doing one final check on whether the abstract mentions statistical significance.

The TOST equivalence test at p=0.007 validates the "statistically equivalent accuracy" claim, and while "format collapse" isn't formally defined in the abstract, it's intuitive enough given the context and gets proper treatment later in the methods section. The paper lacks a dedicated Discussion section, relying instead on an Analysis subsection that addresses why generation degrades and error complementarity, though there's no explicit higher-level synthesis connecting the findings back to the original research questions from the introduction.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "db0a221a-cb64-47a5-94f3-7c1be23245be",
  "isSidechain": false,
  "requestId": "req_011CbNvZswWLvDR486WpeVRv",
  "type": "assistant",
  "uuid": "3f484291-7d36-4a68-a12c-58032864c11b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/paper_audit_content_8033e618",
  "sessionId": "d10eba16-884c-49dd-bd31-5cc0ef3bc131",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PpjXHoyaSvbtFNBLVLoSLe",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1201,
      "cache_read_input_tokens": 94799,
      "output_tokens": 11787,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1201,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 11787,
          "cache_read_input_tokens": 94799,
          "cache_creation_input_tokens": 1201,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1201
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

_source line 72 · 2026-05-25T07:57:21.582Z_

审计标准和所有源码已就绪。现在开始系统性审计。

```
[CONTENT_AUDIT_START]

=== 叙事一致性 (CRITICAL 级) ===

- [critical] [叙事一致性] abstract.tex:2 — Abstract 说 "Preliminary results at 14B suggest this divergence narrows with scale"，其中 "this divergence" 的语法先行词是 repo-level format collapse（上一句话的主题），但 14B 数据实际上只有 function-level（Table 2, §4.2 明确标注 "at function level"）。Conclusion 正确地写了 "whether the repo-level divergence is formulation-inherent or capacity-contingent remains open"，与 Abstract 的暗示矛盾。Abstract 在最关键的 claim 上比 Conclusion 更强——reviewer 几乎一定会将此读作 "14B repo-level evidence exists"。修复建议：在 "this divergence" 前加 "the function-level" 限定词，或将整句改为 "At 14B, function-level gaps narrow to within 1pp, but whether repo-level divergence is capacity-contingent remains open."

- [warning] [叙事一致性] introduction.tex:6 / related_work.tex:8 — Intro 第 2 段提出 GenRM 问题（"does this advantage transfer to code verification?"），但这个问题的答案出现在 Related Work §2 第 2 段（"our results reveal a domain difference..."），而非 Experiments 或 Discussion。叙事结构应为 Intro 提问 → Experiments 回答。建议：将 GenRM 对比的结论性表述从 Related Work 移到 Analysis §4.5 或 Conclusion。

- [info] [叙事一致性] conclusion.tex:4 — Conclusion 引用 "z=−23.7" 与 "18--26pp" 在同一句中，z-score 实际是 mixed-effects interaction term 而非 gap 本身的检验量。易误导 reviewer 认为 z-score 直接检验了 18-26pp gap。建议：拆分为两句或标注 "interaction z=−23.7"。

=== 章节结构 ===

- [info] [章节结构] introduction.tex — Intro 只有 3 段 + 贡献列表（而非经典 5 段），第 2 段同时承担 gap、broader NLP context、GenRM 对比三个功能，略显拥挤。在 8 页限制下可接受，但可考虑拆分 GenRM 讨论到独立段。

- [info] [章节结构] introduction.tex:12-16 — 仅列 2 条 contributions。对顶会而言偏少（通常 3 条），但每条内容充实且有对应 section/table 支撑。

- [info] [章节结构] conclusion.tex:1-4 — Conclusion 仅 ~4 行文字（不含 Limitations），只重述结果没有更高层解读（如对 NLP task formulation 研究的 broader implication、对 practitioner pipeline 选择的具体建议）。建议增加 1-2 句将发现连接回 Intro 提出的 broader question。

=== 贡献-范围对齐 ===

- [info] [贡献-范围] method.tex:30-33 — Oracle Accuracy-Utility Framework (§3.3) 在 Method 中占显著篇幅，但未在 Intro 贡献列表中提及。它在 Experiments 中作为支撑分析使用（Appendix A），如果被 reviewer 视为 contribution 但不在列表中，可能引发 "贡献 undercount" 印象。建议：要么将 oracle analysis 纳入第 2 条 contribution 的描述中，要么简化 §3.3 为附录。

=== Claim 强度匹配 ===

- [info] [Claim强度] experiments.tex:191 — "Simple routing heuristics capture <0.4pp of the oracle gap" + 同时 Abstract 称 routing 为 "a key open direction"。Re-repair pilot (Appendix j) 也是 negative（p=0.42）。将 routing 标为 "key open direction" 虽然技术上合理（oracle gap 的存在证明潜力），但连续 negative pilot 结果未在 abstract 中反映，可能让 reviewer 觉得 overselling。

- [info] [Claim强度] abstract.tex:2 — "first systematic comparison" — 基于 Related Work 中的文献覆盖，此 claim 有依据（Aletheia 比 recipes 非 formulations，GenRM 比 math 非 code）。但如有遗漏近期工作，此 claim 风险极高。

=== 实验严谨性 ===

- [info] [实验严谨性] experiments.tex:14 — DeepSeek-Coder 被描述为 "cross-model consistency check" 而非 primary model，但 Abstract 和 Title 将其列为完整实验维度（"two code LLM families"）。建议 Abstract 措辞与 Experiments 对齐，或升级 DeepSeek 为 primary evaluation。

- [info] [实验严谨性] experiments.tex:68 — 14B scaling（3 seeds, single family）被用于 central narrative（convergence），但 TOST at df=2 power ~0.08，inconclusive for both pairs。Bayesian ROPE 给出 moderate support（0.887/0.780），但 14B evidence 整体偏弱。论文诚实报告了 power limitation，但 Abstract 未传达这种 uncertainty。

=== 可复现性披露 ===

- [info] [可复现性] — GPU (RTX 5090)、training time (~370 GPU-hours)、hyperparameters (Appendix E) 均已披露。代码链接已提供（anonymous GitHub）。可复现性良好。

=== 符号/术语一致性 ===

- [info] [符号一致性] — CLS/CWM/TRAJ 在全文（abstract→conclusion→appendix）中定义和使用一致。pp、TOST、SESOI、ICC、DEFF 均在首次使用时定义。未发现符号含义漂移。

=== 章节过渡与逻辑流 ===

- [info] [逻辑流] — Related Work (§2) → Method (§3) → Experiments (§4) 的过渡流畅。§4 内部 subsection 结构（function→scaling→equivalence→repo→analysis→threats）逻辑清晰，由简到复递进。

=== Limitations 诚实度 ===

- [info] [Limitations] conclusion.tex:6-8 — Limitations 段覆盖 4 个 distinct points（≤8B scope、Python-only、synthetic mutation、format interventions），内容实质性（非回避式 "future work" 空话）。按 EMNLP 2026 用户规则（覆盖 ~3 个点即可），合规。

=== 去 AI 风格 ===

- [info] [去AI] main.tex:6 — LaTeX 注释中有 em-dash（"% Fonts — Times Roman"），不影响 PDF 输出。正文和附录中 em-dash 已清零。

- [info] [去AI] — "Furthermore" 仅出现在 appendix:581（1 处），正文零出现。"Moreover"/"Additionally"/"Notably" 正文零出现。-ing 分词短语使用合理（无 AI 典型的 "..., demonstrating the effectiveness of..." 模式）。"delve/leverage/utilize/facilitate" 零出现。段落长度正常（无 2-3 句过度分段）。去 AI 清理质量良好。

=== 内部信息残留 ===

- [info] [内部信息] — 未发现内部实验编号、服务器名、IP 地址、内部路径等残留。GitHub 链接已匿名化。Appendix 中提到的脚本名（train_unified.py 等）属正常可复现性信息。

=== 用户自定义规则检查 ===

- [info] [写作规则] Abstract ~167 words，符合 EMNLP 2026 ≤200 words 规则。
- [info] [写作规则] Limitations section 仅在 conclusion.tex 中出现一处，appendix 无 Limitations section（app:limitations 标签下是 "Extended validity discussion"），符合 EMNLP 2026 规则。
- [info] [写作规则] ARR Checklist 在 main.tex 中已注释掉并标注 "filled in OpenReview submission form"，符合 EMNLP 2026 规则。
- [warning] [审稿规则] 正文页数需验证：main.tex 内容量较大（experiments.tex ~196 行含 4 表 1 图），在 ACL 双栏格式下正文可能接近或超过 8 页限制。建议编译后测量正文页数（abstract 到 limitations 结束，不含 references 和 appendix）。

[CONTENT_AUDIT_END]
```

[AUDIT_DONE]

**审计总结**：

1 个 critical 问题：Abstract 中 14B 证据的叙事范围与实际数据不匹配（function-level data 被暗示为 repo-level evidence），与 Conclusion 的措辞矛盾。

1 个 warning：正文页数可能逼近或超过 EMNLP 2026 的 8 页限制，需编译验证。

其余均为 info 级改善建议。整体论文叙事连贯性良好，去 AI 清理到位，统计报告严谨，可复现性信息完整。核心修复优先级：将 Abstract 中 "this divergence narrows" 加上 "function-level" 限定词。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3f484291-7d36-4a68-a12c-58032864c11b",
  "isSidechain": false,
  "requestId": "req_011CbNvZswWLvDR486WpeVRv",
  "type": "assistant",
  "uuid": "391b23ed-1925-4e4b-b1f0-e2ef90c94bf2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/paper_audit_content_8033e618",
  "sessionId": "d10eba16-884c-49dd-bd31-5cc0ef3bc131",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PpjXHoyaSvbtFNBLVLoSLe",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1201,
      "cache_read_input_tokens": 94799,
      "output_tokens": 11787,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1201,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 11787,
          "cache_read_input_tokens": 94799,
          "cache_creation_input_tokens": 1201,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1201
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

_source line 73_

```json
{
  "type": "last-prompt",
  "lastPrompt": "项目：exec-sim-repair-verifier Venue：emnlp-2026 论文目录：/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper  Phase 1 确定性检查结果： 源码检查: passed=False, 1 critical, 18 war…",
  "leafUuid": "391b23ed-1925-4e4b-b1f0-e2ef90c94bf2",
  "sessionId": "d10eba16-884c-49dd-bd31-5cc0ef3bc131"
}
```

---

### Runtime record

_source line 74_

```json
{
  "type": "ai-title",
  "aiTitle": "EMNLP 2026 paper verification and compliance audit",
  "sessionId": "d10eba16-884c-49dd-bd31-5cc0ef3bc131"
}
```

---

### Runtime record

_source line 75_

```json
{
  "type": "last-prompt",
  "lastPrompt": "项目：exec-sim-repair-verifier Venue：emnlp-2026 论文目录：/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper  Phase 1 确定性检查结果： 源码检查: passed=False, 1 critical, 18 war…",
  "leafUuid": "391b23ed-1925-4e4b-b1f0-e2ef90c94bf2",
  "sessionId": "d10eba16-884c-49dd-bd31-5cc0ef3bc131"
}
```

---

### Runtime record

_source line 76_

```json
{
  "type": "ai-title",
  "aiTitle": "EMNLP 2026 paper verification and compliance audit",
  "sessionId": "d10eba16-884c-49dd-bd31-5cc0ef3bc131"
}
```

---
