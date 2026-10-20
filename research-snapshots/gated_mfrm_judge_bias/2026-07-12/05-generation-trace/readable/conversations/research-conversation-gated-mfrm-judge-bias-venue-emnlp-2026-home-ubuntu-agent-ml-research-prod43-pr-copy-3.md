# Research conversation: 项目：gated_mfrm_judge_bias Venue：emnlp-2026 论文目录：/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/doc

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 87
- **Recorded user turns:** 1
- **Tool calls:** 28
- **Original source:** `logs/chats/exported-trajectories/account-3/6c0691ec-5f2a-45e8-8336-b216f7d74648.jsonl`
- **Structured JSON:** [`198c67d864ecc43b1385.json`](../../sessions/19/198c67d864ecc43b1385.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-25T17:14:03.095Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-25T17:14:03.095Z",
  "sessionId": "6c0691ec-5f2a-45e8-8336-b216f7d74648",
  "content": "项目：gated_mfrm_judge_bias\nVenue：emnlp-2026\n论文目录：/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper\n\nPhase 1 确定性检查结果：\n源码检查: passed=False, 13 critical, 26 warning\n一致性检查: 0 critical, 2 warning\n编译: ✅, 页数: 17\n内部信息: 0 critical, 0 warning\n\n━━━ 用户自定义规则（作为额外检查项）━━━\n## 用户自定义规则（必须遵守）\n### 写作规则\n\n- **[EMNLP 2026]** Limitations 章节只需要写一小段，覆盖 3 个点左右就可以了，不需要写得很长\n- **[EMNLP 2026]** ARR Responsible NLP Checklist在OpenReview的submission form里面（由用户手动填写），而不是在论文pdf里面\n- **[EMNLP 2026]** 一篇文章只能有一个limitations section，放在正文里面，appendix不能有 limitations section\n- **[EMNLP 2026]** abstract 不要超过 200 words\n\n### 审稿规则\n\n- **[EMNLP 2026]** “EMNLP 2026 通过 ARR 统一审稿，Main/Findings 不分开投稿（不是两个Track），Long/Short 也走同一审稿系统，Overall Assessment的评分标准如下：5 = Consider for Award（约前2.5%），4.5 = Borderline Award，4 = Conference（可被主会议接收），3.5 = Borderline Conference，3 = Findings（可被Findings接收），2.5 = Borderline Findings，2 = Resubmit next cycle（需大幅修改，可在下一周期完成），1.5 = Resubmit after next cycle（需大幅修改，无法在下一周期完成），1 = Do not resubmit（需完全重做或与*ACL无关）”\n- **[EMNLP 2026]** EMNLP 2026 restricts long paper submissions to a strict 8-page limit for main text, with unlimited space for references. Mandatory limitations and optional ethical considerations do not count towards this page limit, provided they do not contain excessive additional content.\n\n> 以上规则由用户配置，优先级等同于硬约束。违反会被 Reviewer 标记。\n请将以上规则逐条作为额外审计维度检查。违反的规则用 dimension `[写作规则]` 或 `[审稿规则]` 标记，severity 按实际影响判定。\n\n请按照你的角色指令执行内容结构审计。"
}
```

---

### Runtime record

_source line 2 · 2026-05-25T17:14:03.100Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-25T17:14:03.100Z",
  "sessionId": "6c0691ec-5f2a-45e8-8336-b216f7d74648"
}
```

---

## Round 1

85 recorded events

### User

_source line 3 · 2026-05-25T17:14:03.153Z_

项目：gated_mfrm_judge_bias
Venue：emnlp-2026
论文目录：/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper

Phase 1 确定性检查结果：
源码检查: passed=False, 13 critical, 26 warning
一致性检查: 0 critical, 2 warning
编译: ✅, 页数: 17
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
  "promptId": "22ca73de-0bd3-4dbb-9f16-96242e2ec1f9",
  "type": "user",
  "uuid": "a0e49f02-d8a7-4b02-be32-2454a06c4f95",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/paper_audit_content_0d2a3cf9",
  "sessionId": "6c0691ec-5f2a-45e8-8336-b216f7d74648",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-25T17:14:03.152Z_

```json
{
  "parentUuid": "a0e49f02-d8a7-4b02-be32-2454a06c4f95",
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
  "uuid": "654b02cd-d817-48dc-bf79-77d32d489ca1",
  "timestamp": "2026-05-25T17:14:03.152Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/paper_audit_content_0d2a3cf9",
  "sessionId": "6c0691ec-5f2a-45e8-8336-b216f7d74648",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-25T17:14:03.152Z_

```json
{
  "parentUuid": "654b02cd-d817-48dc-bf79-77d32d489ca1",
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
  "uuid": "a63c7df3-6dcf-4198-ab08-533f4f1f1cbc",
  "timestamp": "2026-05-25T17:14:03.152Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/paper_audit_content_0d2a3cf9",
  "sessionId": "6c0691ec-5f2a-45e8-8336-b216f7d74648",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6 · 2026-05-25T17:14:03.152Z_

```json
{
  "parentUuid": "a63c7df3-6dcf-4198-ab08-533f4f1f1cbc",
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
  "uuid": "580ff769-a6f9-4e3b-a4b2-1ef06b8d4a5f",
  "timestamp": "2026-05-25T17:14:03.152Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/paper_audit_content_0d2a3cf9",
  "sessionId": "6c0691ec-5f2a-45e8-8336-b216f7d74648",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 7 · 2026-05-25T17:14:03.152Z_

```json
{
  "parentUuid": "580ff769-a6f9-4e3b-a4b2-1ef06b8d4a5f",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "e6200288-692a-4bb9-ad6f-77399aaeab05",
  "timestamp": "2026-05-25T17:14:03.152Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/paper_audit_content_0d2a3cf9",
  "sessionId": "6c0691ec-5f2a-45e8-8336-b216f7d74648",
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
  "aiTitle": "Audit gated_mfrm_judge_bias paper for EMNLP 2026",
  "sessionId": "6c0691ec-5f2a-45e8-8336-b216f7d74648"
}
```

---

### Assistant

_source line 9 · 2026-05-25T17:14:07.632Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to perform a content structure audit of a paper. Let me follow the instructions:

1. Read `skills/global/paper-writing-norms.skill.md` and `skills/global/paper-quality-lessons.skill.md`
2. Read all `.tex` files in the paper directory
3. Audit across all dimensions
4. Output structured findings

Let me start by reading the skill files and finding all tex files.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e6200288-692a-4bb9-ad6f-77399aaeab05",
  "isSidechain": false,
  "requestId": "req_011CbPfPV6Jc5gTeMypHYc7P",
  "type": "assistant",
  "uuid": "f7cd7dcf-5f8c-4038-91fc-4f3ae2780ae7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/paper_audit_content_0d2a3cf9",
  "sessionId": "6c0691ec-5f2a-45e8-8336-b216f7d74648",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V9pAGnUMUMYqjPSax7S7Br",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 27317,
      "cache_read_input_tokens": 11452,
      "output_tokens": 358,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 27317,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 358,
          "cache_read_input_tokens": 11452,
          "cache_creation_input_tokens": 27317,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 27317
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

_source line 10 · 2026-05-25T17:14:08.660Z_

开始执行内容结构审计。先加载审计标准和论文源码。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f7cd7dcf-5f8c-4038-91fc-4f3ae2780ae7",
  "isSidechain": false,
  "requestId": "req_011CbPfPV6Jc5gTeMypHYc7P",
  "type": "assistant",
  "uuid": "8a276b86-293e-4c36-85db-30225b07814e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/paper_audit_content_0d2a3cf9",
  "sessionId": "6c0691ec-5f2a-45e8-8336-b216f7d74648",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V9pAGnUMUMYqjPSax7S7Br",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 27317,
      "cache_read_input_tokens": 11452,
      "output_tokens": 358,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 27317,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 358,
          "cache_read_input_tokens": 11452,
          "cache_creation_input_tokens": 27317,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 27317
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

_source line 11 · 2026-05-25T17:14:09.264Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Q3RpfrZbkzyknV8PBYmfgL`</summary>

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
  "parentUuid": "8a276b86-293e-4c36-85db-30225b07814e",
  "isSidechain": false,
  "requestId": "req_011CbPfPV6Jc5gTeMypHYc7P",
  "type": "assistant",
  "uuid": "02d49a89-685f-4c34-a02b-b2f156ea5530",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/paper_audit_content_0d2a3cf9",
  "sessionId": "6c0691ec-5f2a-45e8-8336-b216f7d74648",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V9pAGnUMUMYqjPSax7S7Br",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 27317,
      "cache_read_input_tokens": 11452,
      "output_tokens": 358,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 27317,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 358,
          "cache_read_input_tokens": 11452,
          "cache_creation_input_tokens": 27317,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 27317
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

_source line 12 · 2026-05-25T17:14:10.250Z_

<details><summary>↩ Tool result · `toolu_01DPM1WMhNtSAvfbNCKJ77gx`</summary>

```text
/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/main.tex
/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/related_work.tex
/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/limitations.tex
/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/background.tex
/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/appendix.tex
/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/experiments.tex
/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/abstract.tex
/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/introduction.tex
/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/conclusion.tex
/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/method.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a96dad44-6afc-4d6e-87d9-72b30b8045f5",
  "isSidechain": false,
  "promptId": "22ca73de-0bd3-4dbb-9f16-96242e2ec1f9",
  "type": "user",
  "uuid": "8285220f-df5e-41ff-9e5a-6face04c8e90",
  "toolUseResult": {
    "filenames": [
      "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/main.tex",
      "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/related_work.tex",
      "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/limitations.tex",
      "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/background.tex",
      "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/appendix.tex",
      "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/experiments.tex",
      "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/abstract.tex",
      "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/introduction.tex",
      "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/conclusion.tex",
      "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/method.tex"
    ],
    "durationMs": 6,
    "numFiles": 10,
    "truncated": false
  },
  "sourceToolAssistantUUID": "a96dad44-6afc-4d6e-87d9-72b30b8045f5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/paper_audit_content_0d2a3cf9",
  "sessionId": "6c0691ec-5f2a-45e8-8336-b216f7d74648",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-25T17:14:09.279Z_

<details><summary>↩ Tool result · `toolu_01Q3RpfrZbkzyknV8PBYmfgL`</summary>

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
  "parentUuid": "02d49a89-685f-4c34-a02b-b2f156ea5530",
  "isSidechain": false,
  "promptId": "22ca73de-0bd3-4dbb-9f16-96242e2ec1f9",
  "type": "user",
  "uuid": "147a3a94-9e13-4d7e-be1f-cac2b367349d",
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
  "sourceToolAssistantUUID": "02d49a89-685f-4c34-a02b-b2f156ea5530",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/paper_audit_content_0d2a3cf9",
  "sessionId": "6c0691ec-5f2a-45e8-8336-b216f7d74648",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
````

</details>

---

### Tool call

_source line 14 · 2026-05-25T17:14:09.862Z_

<details open><summary>🔧 Tool call — Read · `toolu_01AxSAyjcZr5ve75J5dqkkuG`</summary>

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
  "parentUuid": "147a3a94-9e13-4d7e-be1f-cac2b367349d",
  "isSidechain": false,
  "requestId": "req_011CbPfPV6Jc5gTeMypHYc7P",
  "type": "assistant",
  "uuid": "8bd1422b-35c0-4f09-813b-5d4a77dc2b89",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/paper_audit_content_0d2a3cf9",
  "sessionId": "6c0691ec-5f2a-45e8-8336-b216f7d74648",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V9pAGnUMUMYqjPSax7S7Br",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 27317,
      "cache_read_input_tokens": 11452,
      "output_tokens": 358,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 27317,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 358,
          "cache_read_input_tokens": 11452,
          "cache_creation_input_tokens": 27317,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 27317
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

_source line 15 · 2026-05-25T17:14:09.869Z_

<details><summary>↩ Tool result · `toolu_01AxSAyjcZr5ve75J5dqkkuG`</summary>

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
  "parentUuid": "8bd1422b-35c0-4f09-813b-5d4a77dc2b89",
  "isSidechain": false,
  "promptId": "22ca73de-0bd3-4dbb-9f16-96242e2ec1f9",
  "type": "user",
  "uuid": "279f0ee7-8ebb-412a-b580-156b481cd058",
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
  "sourceToolAssistantUUID": "8bd1422b-35c0-4f09-813b-5d4a77dc2b89",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/paper_audit_content_0d2a3cf9",
  "sessionId": "6c0691ec-5f2a-45e8-8336-b216f7d74648",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
````

</details>

---

### Tool call

_source line 16 · 2026-05-25T17:14:10.239Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01DPM1WMhNtSAvfbNCKJ77gx`</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "279f0ee7-8ebb-412a-b580-156b481cd058",
  "isSidechain": false,
  "requestId": "req_011CbPfPV6Jc5gTeMypHYc7P",
  "type": "assistant",
  "uuid": "a96dad44-6afc-4d6e-87d9-72b30b8045f5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/paper_audit_content_0d2a3cf9",
  "sessionId": "6c0691ec-5f2a-45e8-8336-b216f7d74648",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V9pAGnUMUMYqjPSax7S7Br",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 27317,
      "cache_read_input_tokens": 11452,
      "output_tokens": 358,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 27317,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 358,
          "cache_read_input_tokens": 11452,
          "cache_creation_input_tokens": 27317,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 27317
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
  "lastPrompt": "项目：gated_mfrm_judge_bias Venue：emnlp-2026 论文目录：/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper  Phase 1 确定性检查结果： 源码检查: passed=False, 13 critical, 26 warning 一致性检查: 0 c…",
  "leafUuid": "8285220f-df5e-41ff-9e5a-6face04c8e90",
  "sessionId": "6c0691ec-5f2a-45e8-8336-b216f7d74648"
}
```

---

### Runtime record

_source line 18_

```json
{
  "type": "ai-title",
  "aiTitle": "Audit gated_mfrm_judge_bias paper for EMNLP 2026",
  "sessionId": "6c0691ec-5f2a-45e8-8336-b216f7d74648"
}
```

---

### Assistant

_source line 19 · 2026-05-25T17:14:13.316Z_

<details><summary>Logged reasoning block</summary>

```text
Now I need to read all the .tex files. Let me read them all in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8285220f-df5e-41ff-9e5a-6face04c8e90",
  "isSidechain": false,
  "requestId": "req_011CbPfQ1NU2iEKvdJXR8f4L",
  "type": "assistant",
  "uuid": "aae1ae8c-2199-47ad-8535-37b024dfdbf4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/paper_audit_content_0d2a3cf9",
  "sessionId": "6c0691ec-5f2a-45e8-8336-b216f7d74648",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GrsQFcF17aMgSKpeSqAZ7n",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11963,
      "cache_read_input_tokens": 38769,
      "output_tokens": 758,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11963,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 758,
          "cache_read_input_tokens": 38769,
          "cache_creation_input_tokens": 11963,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11963
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

_source line 20 · 2026-05-25T17:14:13.835Z_

读取所有 .tex 源码文件。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "aae1ae8c-2199-47ad-8535-37b024dfdbf4",
  "isSidechain": false,
  "requestId": "req_011CbPfQ1NU2iEKvdJXR8f4L",
  "type": "assistant",
  "uuid": "28a1ece6-3e5a-48a2-bda5-dda45d796c9d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/paper_audit_content_0d2a3cf9",
  "sessionId": "6c0691ec-5f2a-45e8-8336-b216f7d74648",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GrsQFcF17aMgSKpeSqAZ7n",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11963,
      "cache_read_input_tokens": 38769,
      "output_tokens": 758,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11963,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 758,
          "cache_read_input_tokens": 38769,
          "cache_creation_input_tokens": 11963,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11963
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

_source line 21 · 2026-05-25T17:14:14.492Z_

<details open><summary>🔧 Tool call — Read · `toolu_016iTC1HzGWWyGnYEx7fiz9z`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "28a1ece6-3e5a-48a2-bda5-dda45d796c9d",
  "isSidechain": false,
  "requestId": "req_011CbPfQ1NU2iEKvdJXR8f4L",
  "type": "assistant",
  "uuid": "3a1759d4-377c-4e75-b21e-fa5ee39a2ba8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/paper_audit_content_0d2a3cf9",
  "sessionId": "6c0691ec-5f2a-45e8-8336-b216f7d74648",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GrsQFcF17aMgSKpeSqAZ7n",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11963,
      "cache_read_input_tokens": 38769,
      "output_tokens": 758,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11963,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 758,
          "cache_read_input_tokens": 38769,
          "cache_creation_input_tokens": 11963,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11963
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

_source line 22 · 2026-05-25T17:14:19.111Z_

<details><summary>↩ Tool result · `toolu_01DePFtvx1rjWLo1Kpf7EQav`</summary>

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
10	\usepackage{graphicx}
11	\usepackage{amsmath}
12	\usepackage{amssymb}
13	\usepackage{amsthm}
14	\usepackage{booktabs}
15	\usepackage{xcolor}
16	\usepackage{subcaption}
17	
18	\newtheorem{observation}{Observation}
19	\newtheorem{proposition}{Proposition}
20	\newtheorem{theorem}{Theorem}
21	\newtheorem{corollary}{Corollary}
22	
23	\graphicspath{{../../figures/paper/}}
24	
25	\title{Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model\\for Disentangling Judge Bias and Contamination in LLM Evaluation}
26	
27	\author{Anonymous}
28	
29	\begin{document}
30	\maketitle
31	
32	\input{abstract}
33	\input{introduction}
34	\input{related_work}
35	\input{background}
36	\input{method}
37	\input{experiments}
38	\input{conclusion}
39	
40	\section*{Limitations}
41	\input{limitations}
42	
43	\bibliography{references}
44	
45	\appendix
46	\input{appendix}
47	
48	\end{document}
49	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c29a45d5-d6e7-4a79-a5ee-e46e2fe1635d",
  "isSidechain": false,
  "promptId": "22ca73de-0bd3-4dbb-9f16-96242e2ec1f9",
  "type": "user",
  "uuid": "bb1da008-44a6-4efe-b706-a16548aac59a",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/main.tex",
      "content": "\\documentclass[11pt]{article}\n\n\\usepackage[review]{acl}\n\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage[T1]{fontenc}\n\\usepackage[utf8]{inputenc}\n\\usepackage{microtype}\n\\usepackage{graphicx}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{amsthm}\n\\usepackage{booktabs}\n\\usepackage{xcolor}\n\\usepackage{subcaption}\n\n\\newtheorem{observation}{Observation}\n\\newtheorem{proposition}{Proposition}\n\\newtheorem{theorem}{Theorem}\n\\newtheorem{corollary}{Corollary}\n\n\\graphicspath{{../../figures/paper/}}\n\n\\title{Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model\\\\for Disentangling Judge Bias and Contamination in LLM Evaluation}\n\n\\author{Anonymous}\n\n\\begin{document}\n\\maketitle\n\n\\input{abstract}\n\\input{introduction}\n\\input{related_work}\n\\input{background}\n\\input{method}\n\\input{experiments}\n\\input{conclusion}\n\n\\section*{Limitations}\n\\input{limitations}\n\n\\bibliography{references}\n\n\\appendix\n\\input{appendix}\n\n\\end{document}\n",
      "numLines": 49,
      "startLine": 1,
      "totalLines": 49
    }
  },
  "sourceToolAssistantUUID": "c29a45d5-d6e7-4a79-a5ee-e46e2fe1635d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/paper_audit_content_0d2a3cf9",
  "sessionId": "6c0691ec-5f2a-45e8-8336-b216f7d74648",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-25T17:14:14.497Z_

<details><summary>↩ Tool result · `toolu_016iTC1HzGWWyGnYEx7fiz9z`</summary>

```text
1	\begin{abstract}
2	When an LLM judge scores a model response on a benchmark item, the result conflates genuine ability, the judge's scoring tendency, and any advantage from training data exposure. Current evaluation pipelines correct for judge bias and contamination independently, but we show that separate correction is structurally flawed. We formalize this as an omitted variable bias (OVB) problem: any estimator that models one distortion while omitting the other produces systematically biased ability estimates, regardless of correction order. We propose the Gated Many-Facet Rasch Model (G-MFRM), a Bayesian framework that jointly estimates model ability, judge severity, and contamination susceptibility with formal identifiability guarantees. In synthetic experiments ($N = 50$), G-MFRM reduces ability RMSE by 44\% over sequential pipelines ($p < 0.001$) and recovers contamination susceptibility with Pearson $r = 0.81$. On Arena-Hard with 6 LLM judges, G-MFRM provides calibrated per-model contamination diagnostics---older models exhibit 4--6$\times$ higher susceptibility---and a controlled coverage ablation demonstrates that over-correction decreases from $\Delta\tau = -0.044$ at 46\% coverage to $\Delta\tau = 0$ at full coverage, quantifying exposure estimation requirements for contamination-aware evaluation. Leave-one-out cross-validation confirms improved predictive fit ($|\Delta\mathrm{ELPD}/\mathrm{SE}| = 5.9$)\footnote{Code and data are available at \url{https://anonymous.4open.science/r/gated_mfrm_judge_bias-43CC/}.}.
3	\end{abstract}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3a1759d4-377c-4e75-b21e-fa5ee39a2ba8",
  "isSidechain": false,
  "promptId": "22ca73de-0bd3-4dbb-9f16-96242e2ec1f9",
  "type": "user",
  "uuid": "5f57cb6d-146d-40d7-ad6a-ab668044f57b",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/abstract.tex",
      "content": "\\begin{abstract}\nWhen an LLM judge scores a model response on a benchmark item, the result conflates genuine ability, the judge's scoring tendency, and any advantage from training data exposure. Current evaluation pipelines correct for judge bias and contamination independently, but we show that separate correction is structurally flawed. We formalize this as an omitted variable bias (OVB) problem: any estimator that models one distortion while omitting the other produces systematically biased ability estimates, regardless of correction order. We propose the Gated Many-Facet Rasch Model (G-MFRM), a Bayesian framework that jointly estimates model ability, judge severity, and contamination susceptibility with formal identifiability guarantees. In synthetic experiments ($N = 50$), G-MFRM reduces ability RMSE by 44\\% over sequential pipelines ($p < 0.001$) and recovers contamination susceptibility with Pearson $r = 0.81$. On Arena-Hard with 6 LLM judges, G-MFRM provides calibrated per-model contamination diagnostics---older models exhibit 4--6$\\times$ higher susceptibility---and a controlled coverage ablation demonstrates that over-correction decreases from $\\Delta\\tau = -0.044$ at 46\\% coverage to $\\Delta\\tau = 0$ at full coverage, quantifying exposure estimation requirements for contamination-aware evaluation. Leave-one-out cross-validation confirms improved predictive fit ($|\\Delta\\mathrm{ELPD}/\\mathrm{SE}| = 5.9$)\\footnote{Code and data are available at \\url{https://anonymous.4open.science/r/gated_mfrm_judge_bias-43CC/}.}.\n\\end{abstract}",
      "numLines": 3,
      "startLine": 1,
      "totalLines": 3
    }
  },
  "sourceToolAssistantUUID": "3a1759d4-377c-4e75-b21e-fa5ee39a2ba8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/paper_audit_content_0d2a3cf9",
  "sessionId": "6c0691ec-5f2a-45e8-8336-b216f7d74648",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-25T17:14:14.867Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Rp1vNSvBB8dqXCaKT7xq9i`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5f57cb6d-146d-40d7-ad6a-ab668044f57b",
  "isSidechain": false,
  "requestId": "req_011CbPfQ1NU2iEKvdJXR8f4L",
  "type": "assistant",
  "uuid": "6f9b21a7-403d-4654-ba07-9c248e400093",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/paper_audit_content_0d2a3cf9",
  "sessionId": "6c0691ec-5f2a-45e8-8336-b216f7d74648",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GrsQFcF17aMgSKpeSqAZ7n",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11963,
      "cache_read_input_tokens": 38769,
      "output_tokens": 758,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11963,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 758,
          "cache_read_input_tokens": 38769,
          "cache_creation_input_tokens": 11963,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11963
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

_source line 25 · 2026-05-25T17:14:14.872Z_

<details><summary>↩ Tool result · `toolu_01Rp1vNSvBB8dqXCaKT7xq9i`</summary>

```text
1	\section{Introduction}
2	\label{sec:introduction}
3	
4	When multiple LLM judges evaluate model responses on a benchmark, their scores are shaped by at least three forces: the model's genuine ability, the judge's own scoring tendency, and any advantage the model gained from encountering benchmark items during training. These three signals are entangled in every observation. The evaluation community has developed separate tools for the latter two distortions: judge bias correction methods calibrate inter-judge differences \citep{cyclicjudge2026, uda2026}, while contamination detection tools flag or adjust for memorized items \citep{constat2024, dcr2025, logprober2024}. A practitioner who faces both problems must apply these corrections sequentially. This paper shows that sequential correction produces systematically biased rankings, not merely noisy ones.
5	
6	\begin{figure*}[t]
7	\centering
8	\includegraphics[width=\textwidth]{fig1_framework_v2}
9	\caption{(a)~Sequential pipelines address judge bias and contamination independently; omitted variable bias confounds the unmodeled facet into ability estimates. (b)~G-MFRM three-stage joint calibration: Stage~1 fits a standard MFRM for initial estimates $(\hat{\theta}, \hat{b}, \hat{d})$; Stage~2 estimates per-item exposure $e_i$ from external evidence (reference model anchoring, cross-model agreement, and optionally LogProber); Stage~3 performs joint MCMC inference with $e_i$ fixed, recovering contamination-corrected ability $\hat{\theta}_n$, contamination susceptibility $c_n$, and judge severity $d_j$.}
10	\label{fig:framework}
11	\end{figure*}
12	
13	We formalize this failure as an omitted variable bias (OVB) problem \citep{angrist2009mostly}. Consider a model that has memorized some benchmark items and a judge that scores more strictly than average. A bias-only correction adjusts for the strict judge but leaves the contamination signal untouched; the inflated scores on memorized items get absorbed into the model's estimated ability. Conversely, a contamination-only adjustment removes the memorization signal but conflates systematic scoring differences with contamination variation. In both cases, the omitted facet biases the modeled one. Within the Many-Facet Rasch Model (MFRM) framework \citep{linacre1989mfrm}, we prove this bias is directional: contaminated models are systematically overestimated under bias-only correction, and the bias persists regardless of which correction comes first (Section~\ref{sec:confounding}).
14	
15	Resolving this confounding requires joint estimation. We propose the Gated Many-Facet Rasch Model (G-MFRM), which extends MFRM with a multiplicative gating term $c_n \cdot e_i$ for contamination susceptibility, inspired by Doubly-Gated Item Response Theory \citep{shu2013dgirt}. Through a three-stage calibration procedure with externally anchored per-item exposure indicators (Figure~\ref{fig:framework}), G-MFRM simultaneously recovers model ability, item difficulty, judge severity, and contamination susceptibility. We prove that external anchoring of exposure is both necessary and sufficient for parameter identification under standard multi-judge designs (Theorem~\ref{thm:sufficient}), and derive error propagation bounds for the staged estimation.
16	
17	In synthetic experiments ($N = 50$ models, 20 seeds), G-MFRM reduces ability RMSE by 44\% relative to sequential estimation ($p < 0.001$) and recovers contamination susceptibility with Pearson $r = 0.81$. On Arena-Hard \citep{li2024arenahard} with 6 LLM judges and 17 target models, G-MFRM produces calibrated per-model contamination diagnostics---older models (GPT-3.5-Turbo, GPT-4-0613) exhibit 4--6$\times$ higher susceptibility than recent models (GPT-4o)---and a controlled coverage ablation traces over-correction to incomplete exposure estimation ($\Delta\tau$: $-0.044 \to -0.015 \to 0.000$ as coverage increases from 46\% to 100\%). Leave-one-out cross-validation strongly favors joint estimation ($|\Delta\mathrm{ELPD}/\mathrm{SE}| = 5.9$; stacking weight 1.0). Our contributions are:
18	\begin{enumerate}
19	    \item A formal analysis of judge-contamination confounding as omitted variable bias, proving that sequential correction cannot resolve the confounding under non-orthogonality (Section~\ref{sec:confounding}).
20	    \item The G-MFRM framework with identifiability guarantees and error propagation bounds for staged estimation (Section~\ref{sec:method}).
21	    \item Empirical validation on Arena-Hard yielding calibrated contamination diagnostics, with a controlled coverage ablation tracing over-correction to incomplete exposure estimation (Section~\ref{sec:experiments}).
22	\end{enumerate}
23	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6f9b21a7-403d-4654-ba07-9c248e400093",
  "isSidechain": false,
  "promptId": "22ca73de-0bd3-4dbb-9f16-96242e2ec1f9",
  "type": "user",
  "uuid": "83e33c90-f905-41d6-b7ac-7a31f799d75b",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/introduction.tex",
      "content": "\\section{Introduction}\n\\label{sec:introduction}\n\nWhen multiple LLM judges evaluate model responses on a benchmark, their scores are shaped by at least three forces: the model's genuine ability, the judge's own scoring tendency, and any advantage the model gained from encountering benchmark items during training. These three signals are entangled in every observation. The evaluation community has developed separate tools for the latter two distortions: judge bias correction methods calibrate inter-judge differences \\citep{cyclicjudge2026, uda2026}, while contamination detection tools flag or adjust for memorized items \\citep{constat2024, dcr2025, logprober2024}. A practitioner who faces both problems must apply these corrections sequentially. This paper shows that sequential correction produces systematically biased rankings, not merely noisy ones.\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{fig1_framework_v2}\n\\caption{(a)~Sequential pipelines address judge bias and contamination independently; omitted variable bias confounds the unmodeled facet into ability estimates. (b)~G-MFRM three-stage joint calibration: Stage~1 fits a standard MFRM for initial estimates $(\\hat{\\theta}, \\hat{b}, \\hat{d})$; Stage~2 estimates per-item exposure $e_i$ from external evidence (reference model anchoring, cross-model agreement, and optionally LogProber); Stage~3 performs joint MCMC inference with $e_i$ fixed, recovering contamination-corrected ability $\\hat{\\theta}_n$, contamination susceptibility $c_n$, and judge severity $d_j$.}\n\\label{fig:framework}\n\\end{figure*}\n\nWe formalize this failure as an omitted variable bias (OVB) problem \\citep{angrist2009mostly}. Consider a model that has memorized some benchmark items and a judge that scores more strictly than average. A bias-only correction adjusts for the strict judge but leaves the contamination signal untouched; the inflated scores on memorized items get absorbed into the model's estimated ability. Conversely, a contamination-only adjustment removes the memorization signal but conflates systematic scoring differences with contamination variation. In both cases, the omitted facet biases the modeled one. Within the Many-Facet Rasch Model (MFRM) framework \\citep{linacre1989mfrm}, we prove this bias is directional: contaminated models are systematically overestimated under bias-only correction, and the bias persists regardless of which correction comes first (Section~\\ref{sec:confounding}).\n\nResolving this confounding requires joint estimation. We propose the Gated Many-Facet Rasch Model (G-MFRM), which extends MFRM with a multiplicative gating term $c_n \\cdot e_i$ for contamination susceptibility, inspired by Doubly-Gated Item Response Theory \\citep{shu2013dgirt}. Through a three-stage calibration procedure with externally anchored per-item exposure indicators (Figure~\\ref{fig:framework}), G-MFRM simultaneously recovers model ability, item difficulty, judge severity, and contamination susceptibility. We prove that external anchoring of exposure is both necessary and sufficient for parameter identification under standard multi-judge designs (Theorem~\\ref{thm:sufficient}), and derive error propagation bounds for the staged estimation.\n\nIn synthetic experiments ($N = 50$ models, 20 seeds), G-MFRM reduces ability RMSE by 44\\% relative to sequential estimation ($p < 0.001$) and recovers contamination susceptibility with Pearson $r = 0.81$. On Arena-Hard \\citep{li2024arenahard} with 6 LLM judges and 17 target models, G-MFRM produces calibrated per-model contamination diagnostics---older models (GPT-3.5-Turbo, GPT-4-0613) exhibit 4--6$\\times$ higher susceptibility than recent models (GPT-4o)---and a controlled coverage ablation traces over-correction to incomplete exposure estimation ($\\Delta\\tau$: $-0.044 \\to -0.015 \\to 0.000$ as coverage increases from 46\\% to 100\\%). Leave-one-out cross-validation strongly favors joint estimation ($|\\Delta\\mathrm{ELPD}/\\mathrm{SE}| = 5.9$; stacking weight 1.0). Our contributions are:\n\\begin{enumerate}\n    \\item A formal analysis of judge-contamination confounding as omitted variable bias, proving that sequential correction cannot resolve the confounding under non-orthogonality (Section~\\ref{sec:confounding}).\n    \\item The G-MFRM framework with identifiability guarantees and error propagation bounds for staged estimation (Section~\\ref{sec:method}).\n    \\item Empirical validation on Arena-Hard yielding calibrated contamination diagnostics, with a controlled coverage ablation tracing over-correction to incomplete exposure estimation (Section~\\ref{sec:experiments}).\n\\end{enumerate}\n",
      "numLines": 23,
      "startLine": 1,
      "totalLines": 23
    }
  },
  "sourceToolAssistantUUID": "6f9b21a7-403d-4654-ba07-9c248e400093",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/paper_audit_content_0d2a3cf9",
  "sessionId": "6c0691ec-5f2a-45e8-8336-b216f7d74648",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-25T17:14:15.848Z_

<details open><summary>🔧 Tool call — Read · `toolu_01KGfwZnWLAPFn7f9qP4eP68`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "83e33c90-f905-41d6-b7ac-7a31f799d75b",
  "isSidechain": false,
  "requestId": "req_011CbPfQ1NU2iEKvdJXR8f4L",
  "type": "assistant",
  "uuid": "d951a600-70a5-45c6-a340-4f259ec4a448",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/paper_audit_content_0d2a3cf9",
  "sessionId": "6c0691ec-5f2a-45e8-8336-b216f7d74648",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GrsQFcF17aMgSKpeSqAZ7n",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11963,
      "cache_read_input_tokens": 38769,
      "output_tokens": 758,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11963,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 758,
          "cache_read_input_tokens": 38769,
          "cache_creation_input_tokens": 11963,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11963
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

_source line 27 · 2026-05-25T17:14:15.853Z_

<details><summary>↩ Tool result · `toolu_01KGfwZnWLAPFn7f9qP4eP68`</summary>

```text
1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Judge Bias in LLM Evaluation.}
5	LLM-as-a-judge evaluations exhibit position bias \citep{wang2024positionbias}, self-preference \citep{panickssery2024selffavor}, and other cognitive biases \citep{koo2024cobbler, ye2024justice, bavaresco2025judgebench}; see also \citet{li2024splitmerge} and \citet{fiedler2026bias_uncertainty}. On the correction side, CyclicJudge \citep{cyclicjudge2026} eliminates average bias via round-robin assignment, and UDA \citep{uda2026} learns a neural K-factor reducing inter-judge deviation by 63.4\%. All of these methods model only the judge facet, absorbing contamination effects into ability estimates (Section~\ref{sec:confounding}).
6	
7	\paragraph{Benchmark Contamination Detection and Avoidance.}
8	Detection methods include performance-based tests \citep{constat2024}, unified contamination metrics \citep{dcr2025}, token-level log-probability probes \citep{logprober2024, mink2024}, and guided prompting \citep{golchin2024timetravel, oren2024proving}; see also \citet{deng2024contamination, sainz2023contamination}. \citet{preference_leakage2026} identify judge-side preference leakage, complementary to G-MFRM's examinee-side focus. Avoidance strategies include dynamic benchmarks \citep{livebench2025}, private evaluation \citep{truce2024}, and subset selection \citep{polo2024tinybenchmarks}. G-MFRM instead corrects for residual contamination while simultaneously modeling judge effects.
9	
10	\paragraph{Item Response Theory (IRT) and MFRM for LLM Evaluation.}
11	IRT has been applied to NLP leaderboards for ranking and benchmark analysis \citep{lalor2019irt, rodriguez2021irt, vania2021irt}. The Many-Facet Rasch Model (MFRM) \citep{linacre1989mfrm, linacre1994mfrm} extends IRT to multi-rater settings; \citet{jiao2025mfrm_llm} apply it to LLM judge panels, and \citet{uto2020generalized} and \citet{choi2026irt_judge} propose Bayesian variants; see also \citet{zhou2025psnirt}. The Doubly-Gated IRT (DG-IRT) model of \citet{shu2013dgirt} is the closest antecedent, introducing binary gating for item preknowledge; G-MFRM extends this to continuous exposure, multi-rater designs, and formal identifiability analysis (Section~\ref{sec:model_spec}).
12	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d951a600-70a5-45c6-a340-4f259ec4a448",
  "isSidechain": false,
  "promptId": "22ca73de-0bd3-4dbb-9f16-96242e2ec1f9",
  "type": "user",
  "uuid": "212a50f7-d3a0-4e4a-b3d7-b059ed9daacf",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/related_work.tex",
      "content": "\\section{Related Work}\n\\label{sec:related_work}\n\n\\paragraph{Judge Bias in LLM Evaluation.}\nLLM-as-a-judge evaluations exhibit position bias \\citep{wang2024positionbias}, self-preference \\citep{panickssery2024selffavor}, and other cognitive biases \\citep{koo2024cobbler, ye2024justice, bavaresco2025judgebench}; see also \\citet{li2024splitmerge} and \\citet{fiedler2026bias_uncertainty}. On the correction side, CyclicJudge \\citep{cyclicjudge2026} eliminates average bias via round-robin assignment, and UDA \\citep{uda2026} learns a neural K-factor reducing inter-judge deviation by 63.4\\%. All of these methods model only the judge facet, absorbing contamination effects into ability estimates (Section~\\ref{sec:confounding}).\n\n\\paragraph{Benchmark Contamination Detection and Avoidance.}\nDetection methods include performance-based tests \\citep{constat2024}, unified contamination metrics \\citep{dcr2025}, token-level log-probability probes \\citep{logprober2024, mink2024}, and guided prompting \\citep{golchin2024timetravel, oren2024proving}; see also \\citet{deng2024contamination, sainz2023contamination}. \\citet{preference_leakage2026} identify judge-side preference leakage, complementary to G-MFRM's examinee-side focus. Avoidance strategies include dynamic benchmarks \\citep{livebench2025}, private evaluation \\citep{truce2024}, and subset selection \\citep{polo2024tinybenchmarks}. G-MFRM instead corrects for residual contamination while simultaneously modeling judge effects.\n\n\\paragraph{Item Response Theory (IRT) and MFRM for LLM Evaluation.}\nIRT has been applied to NLP leaderboards for ranking and benchmark analysis \\citep{lalor2019irt, rodriguez2021irt, vania2021irt}. The Many-Facet Rasch Model (MFRM) \\citep{linacre1989mfrm, linacre1994mfrm} extends IRT to multi-rater settings; \\citet{jiao2025mfrm_llm} apply it to LLM judge panels, and \\citet{uto2020generalized} and \\citet{choi2026irt_judge} propose Bayesian variants; see also \\citet{zhou2025psnirt}. The Doubly-Gated IRT (DG-IRT) model of \\citet{shu2013dgirt} is the closest antecedent, introducing binary gating for item preknowledge; G-MFRM extends this to continuous exposure, multi-rater designs, and formal identifiability analysis (Section~\\ref{sec:model_spec}).\n",
      "numLines": 12,
      "startLine": 1,
      "totalLines": 12
    }
  },
  "sourceToolAssistantUUID": "d951a600-70a5-45c6-a340-4f259ec4a448",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/paper_audit_content_0d2a3cf9",
  "sessionId": "6c0691ec-5f2a-45e8-8336-b216f7d74648",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-25T17:14:16.323Z_

<details open><summary>🔧 Tool call — Read · `toolu_019CnDMadTv2q8rgtWN1cBDd`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/background.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "212a50f7-d3a0-4e4a-b3d7-b059ed9daacf",
  "isSidechain": false,
  "requestId": "req_011CbPfQ1NU2iEKvdJXR8f4L",
  "type": "assistant",
  "uuid": "4287adef-fbc6-424e-8169-edcdb0c553ae",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/paper_audit_content_0d2a3cf9",
  "sessionId": "6c0691ec-5f2a-45e8-8336-b216f7d74648",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GrsQFcF17aMgSKpeSqAZ7n",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11963,
      "cache_read_input_tokens": 38769,
      "output_tokens": 758,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11963,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 758,
          "cache_read_input_tokens": 38769,
          "cache_creation_input_tokens": 11963,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11963
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

_source line 29 · 2026-05-25T17:14:16.329Z_

<details><summary>↩ Tool result · `toolu_019CnDMadTv2q8rgtWN1cBDd`</summary>

```text
1	\section{Confounding in LLM Evaluation}
2	\label{sec:confounding}
3	
4	\begin{figure}[t]
5	\centering
6	\includegraphics[width=\columnwidth]{fig2_ovb_bias}
7	\caption{Sequential estimation bias ($\hat{\theta}_{\mathrm{seq}} - \theta_{\mathrm{true}}$) versus true contamination susceptibility $c_n$. Pearson $r = 0.86$ ($p < 0.001$) confirms systematic overestimation of contaminated models. Synthetic data: $N = 50$, $I = 100$, $J = 8$.}
8	\label{fig:ovb_bias}
9	\end{figure}
10	
11	The Many-Facet Rasch Model (MFRM) extends classical Rasch measurement to settings with multiple rater facets \citep{linacre1989mfrm, linacre1994mfrm}. Originating in educational measurement, the model treats rater variation as a nuisance facet to be estimated and removed rather than a source of noise to be averaged over. In the LLM evaluation context, where $J$ judges score $N$ models across $I$ items, the MFRM specifies
12	%
13	\begin{equation}
14	\label{eq:mfrm}
15	\log \frac{P(Y_{nij} \geq k \mid \theta_n, b_i, d_j, \tau_k)}{P(Y_{nij} < k \mid \theta_n, b_i, d_j, \tau_k)} = \theta_n - b_i - d_j - \tau_k,
16	\end{equation}
17	%
18	where $Y_{nij}$ is the ordinal rating by judge $j$ for model $n$ on item $i$, $\theta_n$ is the ability of model $n$ ($n = 1, \ldots, N$), $b_i$ is the difficulty of item $i$ ($i = 1, \ldots, I$), $d_j$ is the severity of judge $j$ ($j = 1, \ldots, J$), and $\tau_k$ is the threshold for category $k$. All facets reside on a common logit scale, so model ability is directly comparable after adjustment for item difficulty and judge severity. \citet{jiao2025mfrm_llm} applied this framework to compare ten LLM raters with human experts, showing that MFRM separates genuine ability from systematic judge effects in multi-judge panels.
19	
20	However, standard MFRM assumes that all systematic sources of score variation are captured by the modeled facets. This assumption breaks down when some models have been exposed to benchmark items during training \citep{dcr2025}. Such contamination inflates scores on exposed items through memorization rather than genuine ability. We represent this effect as an interaction $c_n \cdot e_i$, where $c_n \geq 0$ is the contamination susceptibility of model $n$ and $e_i \in [0, 1]$ is the exposure level of item $i$. The complete data-generating process becomes
21	%
22	\begin{equation}
23	\label{eq:full}
24	\eta_{nijk} = \theta_n - b_i - d_j - \tau_k + c_n \cdot e_i.
25	\end{equation}
26	
27	
28	When a practitioner fits the standard MFRM (Eq.~\ref{eq:mfrm}) to data generated by Eq.~\ref{eq:full}, the contamination term is absent from the estimated model. Its influence does not vanish but is absorbed into the estimated parameters $\tilde{\theta}_n$, $\tilde{b}_i$, and $\tilde{d}_j$, which distorts all downstream inferences.
29	
30	The consequence of this omission can be stated precisely.
31	
32	\begin{observation}[Omitted Variable Bias in MFRM]
33	\label{obs:ovb}
34	Let the full model be $\eta_{nijk} = \theta_n - b_i - d_j - \tau_k + c_n \cdot e_i$ and the short model omit the contamination term: $\tilde{\eta}_{nijk} = \tilde{\theta}_n - \tilde{b}_i - \tilde{d}_j - \tau_k$. Under a linear approximation to the ordinal logit link \citep{wooldridge2010, angrist2009mostly},\footnote{The OVB formula is exact for linear models. We apply it to the MFRM linear predictor $\eta$, which is an approximation. Synthetic validation confirms the approximation quality: the Pearson correlation between the predicted bias direction and empirical bias reaches $r = 0.86$ ($p < 0.001$), indicating that the linear result accurately characterizes bias direction and relative magnitude.}
35	\begin{equation}
36	\label{eq:ovb}
37	\mathrm{plim}(\tilde{\theta}_n - \theta_n) = \gamma_n \cdot c_n,
38	\end{equation}
39	where $\gamma_n$ depends on the projection of the exposure vector $(e_i)$ onto the design matrix of the short model (explicit form in Appendix~\ref{app:gamma}). The bias is non-zero whenever $\mathrm{Cov}(d_j,\, c_n \cdot e_i) \neq 0$. This captures the confounding component; in the nonlinear MFRM, a specification bias from omitting $c_n \cdot e_i$ persists even at zero covariance (Section~\ref{sec:experiments}).
40	\end{observation}
41	
42	G-MFRM uses the full nonlinear likelihood; the linear approximation serves only as directional motivation. Monte Carlo simulation confirms that bias magnitude is approximately constant across confounding levels $\rho$ (Figure~\ref{fig:bias_vs_rho}), indicating that omission of $c_n \cdot e_i$---not its correlation with $d_j$---is the primary driver. Joint estimation reduces the bias slope by ${\sim}$69\% at all $\rho$ levels. Neither sequential ordering resolves this: bias-first approaches \citep{cyclicjudge2026} absorb contamination into $\hat{\theta}$, while contamination-first approaches \citep{dcr2025} misattribute judge severity as contamination ($r = 0.86$, $p < 0.001$; Figure~\ref{fig:ovb_bias}).
43	
44	\begin{figure}[t]
45	\centering
46	\includegraphics[width=\columnwidth]{fig4_bias_vs_rho}
47	\caption{Sequential estimation bias is approximately constant across confounding levels $\rho$, confirming that omission of the contamination term---not its correlation with judge severity---drives the bias. Joint G-MFRM reduces the bias slope by ${\sim}$69\% at all $\rho$ levels. Synthetic data: $N = 50$, $I = 100$, $J = 8$.}
48	\label{fig:bias_vs_rho}
49	\end{figure}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4287adef-fbc6-424e-8169-edcdb0c553ae",
  "isSidechain": false,
  "promptId": "22ca73de-0bd3-4dbb-9f16-96242e2ec1f9",
  "type": "user",
  "uuid": "da7743e9-36b9-412b-91b3-1db8d26e505d",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/background.tex",
      "content": "\\section{Confounding in LLM Evaluation}\n\\label{sec:confounding}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig2_ovb_bias}\n\\caption{Sequential estimation bias ($\\hat{\\theta}_{\\mathrm{seq}} - \\theta_{\\mathrm{true}}$) versus true contamination susceptibility $c_n$. Pearson $r = 0.86$ ($p < 0.001$) confirms systematic overestimation of contaminated models. Synthetic data: $N = 50$, $I = 100$, $J = 8$.}\n\\label{fig:ovb_bias}\n\\end{figure}\n\nThe Many-Facet Rasch Model (MFRM) extends classical Rasch measurement to settings with multiple rater facets \\citep{linacre1989mfrm, linacre1994mfrm}. Originating in educational measurement, the model treats rater variation as a nuisance facet to be estimated and removed rather than a source of noise to be averaged over. In the LLM evaluation context, where $J$ judges score $N$ models across $I$ items, the MFRM specifies\n%\n\\begin{equation}\n\\label{eq:mfrm}\n\\log \\frac{P(Y_{nij} \\geq k \\mid \\theta_n, b_i, d_j, \\tau_k)}{P(Y_{nij} < k \\mid \\theta_n, b_i, d_j, \\tau_k)} = \\theta_n - b_i - d_j - \\tau_k,\n\\end{equation}\n%\nwhere $Y_{nij}$ is the ordinal rating by judge $j$ for model $n$ on item $i$, $\\theta_n$ is the ability of model $n$ ($n = 1, \\ldots, N$), $b_i$ is the difficulty of item $i$ ($i = 1, \\ldots, I$), $d_j$ is the severity of judge $j$ ($j = 1, \\ldots, J$), and $\\tau_k$ is the threshold for category $k$. All facets reside on a common logit scale, so model ability is directly comparable after adjustment for item difficulty and judge severity. \\citet{jiao2025mfrm_llm} applied this framework to compare ten LLM raters with human experts, showing that MFRM separates genuine ability from systematic judge effects in multi-judge panels.\n\nHowever, standard MFRM assumes that all systematic sources of score variation are captured by the modeled facets. This assumption breaks down when some models have been exposed to benchmark items during training \\citep{dcr2025}. Such contamination inflates scores on exposed items through memorization rather than genuine ability. We represent this effect as an interaction $c_n \\cdot e_i$, where $c_n \\geq 0$ is the contamination susceptibility of model $n$ and $e_i \\in [0, 1]$ is the exposure level of item $i$. The complete data-generating process becomes\n%\n\\begin{equation}\n\\label{eq:full}\n\\eta_{nijk} = \\theta_n - b_i - d_j - \\tau_k + c_n \\cdot e_i.\n\\end{equation}\n\n\nWhen a practitioner fits the standard MFRM (Eq.~\\ref{eq:mfrm}) to data generated by Eq.~\\ref{eq:full}, the contamination term is absent from the estimated model. Its influence does not vanish but is absorbed into the estimated parameters $\\tilde{\\theta}_n$, $\\tilde{b}_i$, and $\\tilde{d}_j$, which distorts all downstream inferences.\n\nThe consequence of this omission can be stated precisely.\n\n\\begin{observation}[Omitted Variable Bias in MFRM]\n\\label{obs:ovb}\nLet the full model be $\\eta_{nijk} = \\theta_n - b_i - d_j - \\tau_k + c_n \\cdot e_i$ and the short model omit the contamination term: $\\tilde{\\eta}_{nijk} = \\tilde{\\theta}_n - \\tilde{b}_i - \\tilde{d}_j - \\tau_k$. Under a linear approximation to the ordinal logit link \\citep{wooldridge2010, angrist2009mostly},\\footnote{The OVB formula is exact for linear models. We apply it to the MFRM linear predictor $\\eta$, which is an approximation. Synthetic validation confirms the approximation quality: the Pearson correlation between the predicted bias direction and empirical bias reaches $r = 0.86$ ($p < 0.001$), indicating that the linear result accurately characterizes bias direction and relative magnitude.}\n\\begin{equation}\n\\label{eq:ovb}\n\\mathrm{plim}(\\tilde{\\theta}_n - \\theta_n) = \\gamma_n \\cdot c_n,\n\\end{equation}\nwhere $\\gamma_n$ depends on the projection of the exposure vector $(e_i)$ onto the design matrix of the short model (explicit form in Appendix~\\ref{app:gamma}). The bias is non-zero whenever $\\mathrm{Cov}(d_j,\\, c_n \\cdot e_i) \\neq 0$. This captures the confounding component; in the nonlinear MFRM, a specification bias from omitting $c_n \\cdot e_i$ persists even at zero covariance (Section~\\ref{sec:experiments}).\n\\end{observation}\n\nG-MFRM uses the full nonlinear likelihood; the linear approximation serves only as directional motivation. Monte Carlo simulation confirms that bias magnitude is approximately constant across confounding levels $\\rho$ (Figure~\\ref{fig:bias_vs_rho}), indicating that omission of $c_n \\cdot e_i$---not its correlation with $d_j$---is the primary driver. Joint estimation reduces the bias slope by ${\\sim}$69\\% at all $\\rho$ levels. Neither sequential ordering resolves this: bias-first approaches \\citep{cyclicjudge2026} absorb contamination into $\\hat{\\theta}$, while contamination-first approaches \\citep{dcr2025} misattribute judge severity as contamination ($r = 0.86$, $p < 0.001$; Figure~\\ref{fig:ovb_bias}).\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig4_bias_vs_rho}\n\\caption{Sequential estimation bias is approximately constant across confounding levels $\\rho$, confirming that omission of the contamination term---not its correlation with judge severity---drives the bias. Joint G-MFRM reduces the bias slope by ${\\sim}$69\\% at all $\\rho$ levels. Synthetic data: $N = 50$, $I = 100$, $J = 8$.}\n\\label{fig:bias_vs_rho}\n\\end{figure}",
      "numLines": 49,
      "startLine": 1,
      "totalLines": 49
    }
  },
  "sourceToolAssistantUUID": "4287adef-fbc6-424e-8169-edcdb0c553ae",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/paper_audit_content_0d2a3cf9",
  "sessionId": "6c0691ec-5f2a-45e8-8336-b216f7d74648",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-25T17:14:16.939Z_

<details open><summary>🔧 Tool call — Read · `toolu_01V2y3exXzwu9DxjsTuwFz4N`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "da7743e9-36b9-412b-91b3-1db8d26e505d",
  "isSidechain": false,
  "requestId": "req_011CbPfQ1NU2iEKvdJXR8f4L",
  "type": "assistant",
  "uuid": "9ea04105-0447-4d51-8cd9-8af89012d21a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/paper_audit_content_0d2a3cf9",
  "sessionId": "6c0691ec-5f2a-45e8-8336-b216f7d74648",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GrsQFcF17aMgSKpeSqAZ7n",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11963,
      "cache_read_input_tokens": 38769,
      "output_tokens": 758,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11963,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 758,
          "cache_read_input_tokens": 38769,
          "cache_creation_input_tokens": 11963,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11963
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

_source line 31 · 2026-05-25T17:14:16.945Z_

<details><summary>↩ Tool result · `toolu_01V2y3exXzwu9DxjsTuwFz4N`</summary>

```text
1	\section{The G-MFRM Framework}
2	\label{sec:method}
3	
4	Section~\ref{sec:confounding} established that omitting contamination from the measurement model produces directional bias in ability estimates (Observation~\ref{obs:ovb}). We now introduce the Gated Many-Facet Rasch Model (G-MFRM), which jointly estimates ability, judge severity, and contamination susceptibility within a single measurement framework. The key design choices, staged estimation with externally fixed exposure and a hierarchical HalfNormal prior for the contamination term, are motivated by the identifiability analysis in \S\ref{sec:identifiability} and the error propagation bounds in \S\ref{sec:error_prop}.
5	
6	\subsection{Model Specification}
7	\label{sec:model_spec}
8	
9	G-MFRM extends the standard MFRM \citep{linacre1989mfrm, linacre1994mfrm} by adding a multiplicative contamination gating term to the linear predictor (Eq.~\ref{eq:mfrm}):
10	%
11	\begin{equation}
12	\label{eq:gmfrm}
13	\log \frac{P(Y_{nij} \geq k)}{P(Y_{nij} < k)} = \theta_n - b_i - d_j - \tau_k + c_n \cdot e_i,
14	\end{equation}
15	%
16	where all terms carry the definitions from Section~\ref{sec:confounding}. The gating structure $c_n \cdot e_i$ separates model-specific contamination susceptibility ($c_n \geq 0$) from item-specific exposure ($e_i \in [0,1]$). When $c_n = 0$ or $e_i = 0$, the gating term vanishes and Eq.~\ref{eq:gmfrm} reduces to the standard MFRM.
17	
18	We enforce non-negativity and sparsity through a hierarchical HalfNormal prior: $\sigma_c \sim \text{HalfNormal}(1.0)$, $c^{\mathrm{raw}}_n \sim \text{HalfNormal}(1.0)$, $c_n = c^{\mathrm{raw}}_n \cdot \sigma_c$. The hierarchical structure provides adaptive shrinkage: when data support low contamination, $\sigma_c$ contracts toward zero. The remaining priors are $\theta_n \sim \mathcal{N}(0, 1)$, $b_i \sim \mathcal{N}(0, 1)$, $d_j \sim \mathcal{N}(0, 0.5)$, and uniform on $\tau_k$.
19	
20	G-MFRM extends the Doubly-Gated IRT model of \citet{shu2013dgirt} from binary gating to continuous exposure and multi-rater designs, and contributes the first formal identifiability conditions for gated IRT parameters (Propositions~\ref{prop:no_new}--\ref{prop:exposure_variation}, Theorem~\ref{thm:sufficient}) and error propagation bounds for staged estimation (\S\ref{sec:error_prop}).
21	
22	\subsection{Staged Estimation}
23	\label{sec:staged}
24	
25	Joint estimation of all parameters in Eq.~\ref{eq:gmfrm}, including $e_i$, would require identifying the bilinear product $c_n \cdot e_i$ from response data alone. This creates a fundamental non-identifiability (Proposition~\ref{prop:exposure_variation}). We resolve this through a three-stage procedure that fixes exposure externally before estimating the contamination parameters.
26	
27	\paragraph{Stage 1: Standard MFRM.} We fit the standard MFRM (Eq.~\ref{eq:mfrm}) via MCMC (NUTS) to obtain initial estimates $(\hat{\theta}, \hat{b}, \hat{d})$. These serve as warm-start values for the sampler in Stage~3 and improve convergence.
28	
29	\paragraph{Stage 2: Exposure estimation.} Per-item exposure $e_i$ is estimated from external evidence independent of the response data. The primary signal is \emph{reference model anchoring} (75\% weight): win-rate residuals against a fixed anchor (gpt-4-0314) flag items where target models outperform difficulty-adjusted expectations. The secondary signal is \emph{cross-model agreement} (25\%): uniformly high scores across diverse architectures suggest exposure rather than easiness. The composite is clipped to $[0, 1]$ and fixed in Stage~3. Estimation is non-circular: $e_i$ is item-level while $c_n$ is model-level, and ablation with 100\% anchoring yields $\rho = 0.998$ (Appendix~\ref{app:weight_robustness}).
30	
31	\paragraph{Stage 3: Joint MCMC.} With $e_i$ fixed, we sample $(\theta_n, b_i, d_j, c_n)$ jointly via the No-U-Turn Sampler (NUTS) \citep{betancourt2015}. The priors are as specified in \S\ref{sec:model_spec}. The hierarchical contamination prior decomposes as
32	%
33	\begin{align}
34	\label{eq:contam_prior}
35	\sigma_c &\sim \text{HalfNormal}(1.0), \quad c^{\mathrm{raw}}_n \sim \text{HalfNormal}(1.0), \nonumber \\
36	c_n &= c^{\mathrm{raw}}_n \cdot \sigma_c,
37	\end{align}
38	%
39	where $\sigma_c$ is a shared global scale that governs the overall contamination magnitude. This non-centered parameterization improves sampler geometry by decoupling the global scale from the per-model effects.
40	
41	Convergence is assessed via rank-normalized split-$\hat{R}$ \citep{vehtari2021rhat} and bulk effective sample size (ESS), with thresholds $\hat{R} < 1.05$ and ESS$_{\mathrm{bulk}} > 100$ following standard practice \citep{gelman2013bda}.\footnote{Synthetic validation with $N = 50$, $I = 100$, $J = 8$ yields satisfactory convergence across all parameters (exp-012). Full diagnostic tables are reported in Section~\ref{sec:experiments}.}
42	
43	
44	\begin{figure}[t]
45	\centering
46	\includegraphics[width=\columnwidth]{forest_dj}
47	\caption{Judge severity estimates ($d_j$) with 95\% credible intervals for the full 9-judge panel ($N = 8$ analysis). Positive values indicate stricter scoring; the severity range spans 1.34 logits. The $N = 17$ analysis (\S\ref{sec:setup}) uses a 6-judge subset selected for item coverage.}
48	\label{fig:judge_severity}
49	\end{figure}
50	
51	\subsection{Identifiability}
52	\label{sec:identifiability}
53	
54	We establish that fixing $e_i$ externally is both necessary and sufficient for identifying the contamination parameters. All proofs assume $\sum_n \theta_n = 0$.
55	
56	\begin{proposition}[No New Indeterminacy]
57	\label{prop:no_new}
58	When $e_i$ is fixed externally, $c_n \cdot e_i$ introduces no additional location or scale indeterminacy beyond the standard MFRM.
59	\end{proposition}
60	
61	\begin{proposition}[Exposure Variation Necessary]
62	\label{prop:exposure_variation}
63	If $e_i = e$ for all $i$ (constant exposure), then $c_n$ and $\theta_n$ are not separately identifiable; hence $\mathrm{Var}(e_i) > 0$ is necessary.
64	\end{proposition}
65	
66	Proofs are in Appendix~\ref{app:prop_proofs}.
67	
68	\begin{theorem}[Sufficient Conditions for Local Identifiability]
69	\label{thm:sufficient}
70	G-MFRM is locally identifiable if: (i) a connected observation design, (ii) $J \geq 2$ judges, (iii) each model observes items with at least two distinct exposure values, and (iv) $\sum_n \theta_n = 0$.
71	\end{theorem}
72	
73	The proof (Appendix~\ref{app:proof}) follows \citet{rothenberg1971}, establishing Fisher information non-singularity via the Cauchy--Schwarz inequality on the $(\theta_n, c_n)$ submatrix. Monte Carlo validation confirms successful $c_n$ recovery (Appendix~\ref{app:cn_recovery}).
74	
75	\subsection{Error Propagation}
76	\label{sec:error_prop}
77	
78	Treating Stage~2 estimates $\hat{e}_i$ as fixed creates a generated regressors problem \citep{pagan1984}. Let $\hat{e}_i = e_i + \epsilon_i$ with $\epsilon_i \sim \mathcal{N}(0, \sigma^2)$. The attenuation factor is $\lambda(\sigma) = \mathrm{Var}(e_i) / [\mathrm{Var}(e_i) + \sigma^2]$, reaching 50\% at $\sigma \approx 0.2$ in our setting ($\mathrm{Var}(e_i) \approx 0.04$). Empirically, $\theta$-RMSE increases by only 5.9\% and $c_n$-RMSE by 7.9\% below this threshold; beyond it ($\sigma = 0.5$), degradation becomes severe (Table~\ref{tab:error_prop}, Appendix~\ref{app:error_prop}). We apply the Murphy--Topel correction \citep{murphy1985} for honest credible intervals (Appendix~\ref{app:murphy_topel}).
79	
80	\subsection{Fair Scores and Diagnostics}
81	\label{sec:fair_scores}
82	
83	The Stage~3 posterior mean of $\theta_n$ provides a bias-and-contamination-corrected ``fair score'' for each model. The remaining parameters serve complementary diagnostic roles: per-model $c_n$ flags candidates for training data audit, per-judge $d_j$ informs judge calibration, and per-item $e_i$ identifies items for retirement or replacement.
84	
85	\begin{table}[t]
86	\centering
87	\small
88	\begin{tabular}{lcccc}
89	\toprule
90	& \multicolumn{2}{c}{\textbf{8 models}} & \multicolumn{2}{c}{\textbf{17 models}} \\
91	\cmidrule(lr){2-3} \cmidrule(lr){4-5}
92	\textbf{Method} & $\tau$ & $\rho$ & $\tau$ & $\rho$ \\
93	\midrule
94	Raw Average & 0.786 & 0.905 & 0.838 & 0.949 \\
95	MFRM-only & 0.786 & 0.905 & 0.838 & 0.949 \\
96	Sequential & 0.786 & 0.905 & 0.838 & 0.949 \\
97	CyclicJudge & 0.786 & 0.905 & 0.838 & 0.949 \\
98	CyclicJudge+discard & 0.786 & 0.905 & 0.824 & 0.934 \\
99	DCR Factor & 0.786 & 0.905 & 0.824 & 0.946 \\
100	Pref.\ Leakage & 0.786 & 0.905 & 0.838 & 0.949 \\
101	\midrule
102	G-MFRM (ours) & \textbf{0.857} & \textbf{0.952} & 0.794 & 0.926 \\
103	\bottomrule
104	\end{tabular}
105	\caption{Correlation with Chatbot Arena human rankings. The $N = 8$ panel uses 9 judges; the $N = 17$ panel uses 6 judges (\S\ref{sec:setup}). Baselines cluster near the raw average at both panel sizes. At $N = 8$, G-MFRM yields nominally higher agreement ($+$7.1pp; bootstrap $\Delta\tau$ CI includes zero). At $N = 17$ with 46\% exposure coverage, over-correction on unexposed items yields $\Delta\tau = -0.044$ (\S\ref{sec:main_results}).}
106	\label{tab:main_results}
107	\end{table}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9ea04105-0447-4d51-8cd9-8af89012d21a",
  "isSidechain": false,
  "promptId": "22ca73de-0bd3-4dbb-9f16-96242e2ec1f9",
  "type": "user",
  "uuid": "a8baa674-b89f-41d4-b2e8-8ad54ec49dbe",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/method.tex",
      "content": "\\section{The G-MFRM Framework}\n\\label{sec:method}\n\nSection~\\ref{sec:confounding} established that omitting contamination from the measurement model produces directional bias in ability estimates (Observation~\\ref{obs:ovb}). We now introduce the Gated Many-Facet Rasch Model (G-MFRM), which jointly estimates ability, judge severity, and contamination susceptibility within a single measurement framework. The key design choices, staged estimation with externally fixed exposure and a hierarchical HalfNormal prior for the contamination term, are motivated by the identifiability analysis in \\S\\ref{sec:identifiability} and the error propagation bounds in \\S\\ref{sec:error_prop}.\n\n\\subsection{Model Specification}\n\\label{sec:model_spec}\n\nG-MFRM extends the standard MFRM \\citep{linacre1989mfrm, linacre1994mfrm} by adding a multiplicative contamination gating term to the linear predictor (Eq.~\\ref{eq:mfrm}):\n%\n\\begin{equation}\n\\label{eq:gmfrm}\n\\log \\frac{P(Y_{nij} \\geq k)}{P(Y_{nij} < k)} = \\theta_n - b_i - d_j - \\tau_k + c_n \\cdot e_i,\n\\end{equation}\n%\nwhere all terms carry the definitions from Section~\\ref{sec:confounding}. The gating structure $c_n \\cdot e_i$ separates model-specific contamination susceptibility ($c_n \\geq 0$) from item-specific exposure ($e_i \\in [0,1]$). When $c_n = 0$ or $e_i = 0$, the gating term vanishes and Eq.~\\ref{eq:gmfrm} reduces to the standard MFRM.\n\nWe enforce non-negativity and sparsity through a hierarchical HalfNormal prior: $\\sigma_c \\sim \\text{HalfNormal}(1.0)$, $c^{\\mathrm{raw}}_n \\sim \\text{HalfNormal}(1.0)$, $c_n = c^{\\mathrm{raw}}_n \\cdot \\sigma_c$. The hierarchical structure provides adaptive shrinkage: when data support low contamination, $\\sigma_c$ contracts toward zero. The remaining priors are $\\theta_n \\sim \\mathcal{N}(0, 1)$, $b_i \\sim \\mathcal{N}(0, 1)$, $d_j \\sim \\mathcal{N}(0, 0.5)$, and uniform on $\\tau_k$.\n\nG-MFRM extends the Doubly-Gated IRT model of \\citet{shu2013dgirt} from binary gating to continuous exposure and multi-rater designs, and contributes the first formal identifiability conditions for gated IRT parameters (Propositions~\\ref{prop:no_new}--\\ref{prop:exposure_variation}, Theorem~\\ref{thm:sufficient}) and error propagation bounds for staged estimation (\\S\\ref{sec:error_prop}).\n\n\\subsection{Staged Estimation}\n\\label{sec:staged}\n\nJoint estimation of all parameters in Eq.~\\ref{eq:gmfrm}, including $e_i$, would require identifying the bilinear product $c_n \\cdot e_i$ from response data alone. This creates a fundamental non-identifiability (Proposition~\\ref{prop:exposure_variation}). We resolve this through a three-stage procedure that fixes exposure externally before estimating the contamination parameters.\n\n\\paragraph{Stage 1: Standard MFRM.} We fit the standard MFRM (Eq.~\\ref{eq:mfrm}) via MCMC (NUTS) to obtain initial estimates $(\\hat{\\theta}, \\hat{b}, \\hat{d})$. These serve as warm-start values for the sampler in Stage~3 and improve convergence.\n\n\\paragraph{Stage 2: Exposure estimation.} Per-item exposure $e_i$ is estimated from external evidence independent of the response data. The primary signal is \\emph{reference model anchoring} (75\\% weight): win-rate residuals against a fixed anchor (gpt-4-0314) flag items where target models outperform difficulty-adjusted expectations. The secondary signal is \\emph{cross-model agreement} (25\\%): uniformly high scores across diverse architectures suggest exposure rather than easiness. The composite is clipped to $[0, 1]$ and fixed in Stage~3. Estimation is non-circular: $e_i$ is item-level while $c_n$ is model-level, and ablation with 100\\% anchoring yields $\\rho = 0.998$ (Appendix~\\ref{app:weight_robustness}).\n\n\\paragraph{Stage 3: Joint MCMC.} With $e_i$ fixed, we sample $(\\theta_n, b_i, d_j, c_n)$ jointly via the No-U-Turn Sampler (NUTS) \\citep{betancourt2015}. The priors are as specified in \\S\\ref{sec:model_spec}. The hierarchical contamination prior decomposes as\n%\n\\begin{align}\n\\label{eq:contam_prior}\n\\sigma_c &\\sim \\text{HalfNormal}(1.0), \\quad c^{\\mathrm{raw}}_n \\sim \\text{HalfNormal}(1.0), \\nonumber \\\\\nc_n &= c^{\\mathrm{raw}}_n \\cdot \\sigma_c,\n\\end{align}\n%\nwhere $\\sigma_c$ is a shared global scale that governs the overall contamination magnitude. This non-centered parameterization improves sampler geometry by decoupling the global scale from the per-model effects.\n\nConvergence is assessed via rank-normalized split-$\\hat{R}$ \\citep{vehtari2021rhat} and bulk effective sample size (ESS), with thresholds $\\hat{R} < 1.05$ and ESS$_{\\mathrm{bulk}} > 100$ following standard practice \\citep{gelman2013bda}.\\footnote{Synthetic validation with $N = 50$, $I = 100$, $J = 8$ yields satisfactory convergence across all parameters (exp-012). Full diagnostic tables are reported in Section~\\ref{sec:experiments}.}\n\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{forest_dj}\n\\caption{Judge severity estimates ($d_j$) with 95\\% credible intervals for the full 9-judge panel ($N = 8$ analysis). Positive values indicate stricter scoring; the severity range spans 1.34 logits. The $N = 17$ analysis (\\S\\ref{sec:setup}) uses a 6-judge subset selected for item coverage.}\n\\label{fig:judge_severity}\n\\end{figure}\n\n\\subsection{Identifiability}\n\\label{sec:identifiability}\n\nWe establish that fixing $e_i$ externally is both necessary and sufficient for identifying the contamination parameters. All proofs assume $\\sum_n \\theta_n = 0$.\n\n\\begin{proposition}[No New Indeterminacy]\n\\label{prop:no_new}\nWhen $e_i$ is fixed externally, $c_n \\cdot e_i$ introduces no additional location or scale indeterminacy beyond the standard MFRM.\n\\end{proposition}\n\n\\begin{proposition}[Exposure Variation Necessary]\n\\label{prop:exposure_variation}\nIf $e_i = e$ for all $i$ (constant exposure), then $c_n$ and $\\theta_n$ are not separately identifiable; hence $\\mathrm{Var}(e_i) > 0$ is necessary.\n\\end{proposition}\n\nProofs are in Appendix~\\ref{app:prop_proofs}.\n\n\\begin{theorem}[Sufficient Conditions for Local Identifiability]\n\\label{thm:sufficient}\nG-MFRM is locally identifiable if: (i) a connected observation design, (ii) $J \\geq 2$ judges, (iii) each model observes items with at least two distinct exposure values, and (iv) $\\sum_n \\theta_n = 0$.\n\\end{theorem}\n\nThe proof (Appendix~\\ref{app:proof}) follows \\citet{rothenberg1971}, establishing Fisher information non-singularity via the Cauchy--Schwarz inequality on the $(\\theta_n, c_n)$ submatrix. Monte Carlo validation confirms successful $c_n$ recovery (Appendix~\\ref{app:cn_recovery}).\n\n\\subsection{Error Propagation}\n\\label{sec:error_prop}\n\nTreating Stage~2 estimates $\\hat{e}_i$ as fixed creates a generated regressors problem \\citep{pagan1984}. Let $\\hat{e}_i = e_i + \\epsilon_i$ with $\\epsilon_i \\sim \\mathcal{N}(0, \\sigma^2)$. The attenuation factor is $\\lambda(\\sigma) = \\mathrm{Var}(e_i) / [\\mathrm{Var}(e_i) + \\sigma^2]$, reaching 50\\% at $\\sigma \\approx 0.2$ in our setting ($\\mathrm{Var}(e_i) \\approx 0.04$). Empirically, $\\theta$-RMSE increases by only 5.9\\% and $c_n$-RMSE by 7.9\\% below this threshold; beyond it ($\\sigma = 0.5$), degradation becomes severe (Table~\\ref{tab:error_prop}, Appendix~\\ref{app:error_prop}). We apply the Murphy--Topel correction \\citep{murphy1985} for honest credible intervals (Appendix~\\ref{app:murphy_topel}).\n\n\\subsection{Fair Scores and Diagnostics}\n\\label{sec:fair_scores}\n\nThe Stage~3 posterior mean of $\\theta_n$ provides a bias-and-contamination-corrected ``fair score'' for each model. The remaining parameters serve complementary diagnostic roles: per-model $c_n$ flags candidates for training data audit, per-judge $d_j$ informs judge calibration, and per-item $e_i$ identifies items for retirement or replacement.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n& \\multicolumn{2}{c}{\\textbf{8 models}} & \\multicolumn{2}{c}{\\textbf{17 models}} \\\\\n\\cmidrule(lr){2-3} \\cmidrule(lr){4-5}\n\\textbf{Method} & $\\tau$ & $\\rho$ & $\\tau$ & $\\rho$ \\\\\n\\midrule\nRaw Average & 0.786 & 0.905 & 0.838 & 0.949 \\\\\nMFRM-only & 0.786 & 0.905 & 0.838 & 0.949 \\\\\nSequential & 0.786 & 0.905 & 0.838 & 0.949 \\\\\nCyclicJudge & 0.786 & 0.905 & 0.838 & 0.949 \\\\\nCyclicJudge+discard & 0.786 & 0.905 & 0.824 & 0.934 \\\\\nDCR Factor & 0.786 & 0.905 & 0.824 & 0.946 \\\\\nPref.\\ Leakage & 0.786 & 0.905 & 0.838 & 0.949 \\\\\n\\midrule\nG-MFRM (ours) & \\textbf{0.857} & \\textbf{0.952} & 0.794 & 0.926 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Correlation with Chatbot Arena human rankings. The $N = 8$ panel uses 9 judges; the $N = 17$ panel uses 6 judges (\\S\\ref{sec:setup}). Baselines cluster near the raw average at both panel sizes. At $N = 8$, G-MFRM yields nominally higher agreement ($+$7.1pp; bootstrap $\\Delta\\tau$ CI includes zero). At $N = 17$ with 46\\% exposure coverage, over-correction on unexposed items yields $\\Delta\\tau = -0.044$ (\\S\\ref{sec:main_results}).}\n\\label{tab:main_results}\n\\end{table}",
      "numLines": 107,
      "startLine": 1,
      "totalLines": 107
    }
  },
  "sourceToolAssistantUUID": "9ea04105-0447-4d51-8cd9-8af89012d21a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/paper_audit_content_0d2a3cf9",
  "sessionId": "6c0691ec-5f2a-45e8-8336-b216f7d74648",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-25T17:14:17.278Z_

<details open><summary>🔧 Tool call — Read · `toolu_01QLW8FzEMvPpT76nrSiBmaY`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a8baa674-b89f-41d4-b2e8-8ad54ec49dbe",
  "isSidechain": false,
  "requestId": "req_011CbPfQ1NU2iEKvdJXR8f4L",
  "type": "assistant",
  "uuid": "8a87016a-a8fa-43f5-b6fc-720e47d32801",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/paper_audit_content_0d2a3cf9",
  "sessionId": "6c0691ec-5f2a-45e8-8336-b216f7d74648",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GrsQFcF17aMgSKpeSqAZ7n",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11963,
      "cache_read_input_tokens": 38769,
      "output_tokens": 758,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11963,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 758,
          "cache_read_input_tokens": 38769,
          "cache_creation_input_tokens": 11963,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11963
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

_source line 33 · 2026-05-25T17:14:17.293Z_

<details><summary>↩ Tool result · `toolu_01QLW8FzEMvPpT76nrSiBmaY`</summary>

```text
1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\begin{figure}[t]
5	\centering
6	\includegraphics[width=\columnwidth, trim=0 0 250bp 0, clip]{fig6_cn_profile}
7	\caption{Contamination susceptibility $\hat{c}_n$ (posterior mean $\pm$ 95\% CI), ordered by magnitude. Older models (GPT-3.5-Turbo, GPT-4-0613) show 4--6$\times$ higher susceptibility than recent models (GPT-4o).}
8	\label{fig:contamination_bars}
9	\end{figure}
10	
11	\begin{figure}[t]
12	\centering
13	\includegraphics[width=\columnwidth, trim=265bp 0 0 0, clip]{fig6_cn_profile}
14	\caption{Ability bias absorbed by MFRM-only estimation: $\Delta\theta = \hat{\theta}_{\mathrm{MFRM}} - \hat{\theta}_{\mathrm{G\text{-}MFRM}}$. The strong correlation with $\hat{c}_n$ (Spearman $\rho = 1.0$) confirms that contamination inflates MFRM ability estimates for high-$c_n$ models, as predicted by the OVB analysis (Section~\ref{sec:confounding}).}
15	\label{fig:bias_absorption}
16	\end{figure}
17	
18	\subsection{Setup}
19	\label{sec:setup}
20	
21	\paragraph{Data and models.} We evaluate on Arena-Hard \citep{li2024arenahard}, a benchmark of 500 multi-turn conversational items selected for high separability among frontier models. The evaluation uses all 500 items in a connected incomplete design (${\sim}$58\% fill rate of the $N \times I \times J$ tensor). Seventeen target models spanning proprietary and open-source families are evaluated: GPT-4o, GPT-4o-mini, Qwen2.5-72B, LLaMA-3.3-70B, Qwen3-8B, Gemma-2-9B, GPT-4-0613, GPT-3.5-Turbo, Claude-3.5-Sonnet, GPT-4-Turbo, LLaMA-3.1-70B, Gemma-2-27B, Claude-3-Opus, LLaMA-3-70B, Mixtral-8x22B, Claude-3-Haiku, and LLaMA-3-8B. Ground-truth rankings are derived from Chatbot Arena human preference data \citep{zheng2023mtbench}.
22	
23	\paragraph{Judges.} Six LLM judges score responses in position-swapped pairwise mode: Claude Sonnet 4.6, DeepSeek-V4-Pro, Gemini-2.5-Pro, LLaMA-3.3-70B, Qwen2.5-72B, and Qwen3-235B. Four provide complete item coverage; two (Gemini, Sonnet) cover ${\sim}$63--79\% of items, yielding an incomplete connected design. Two models serve as both judge and target; $d_j$ absorbs self-evaluation bias ($\tau$ unchanged when excluding self-judging; Appendix~\ref{app:self_eval}).
24	
25	\paragraph{Exposure estimation.} Per-item $e_i$ follows the two-source pipeline in \S\ref{sec:staged} (75\% reference anchoring, 25\% cross-model agreement; robust to weight configuration, $\rho \geq 0.998$; Appendix~\ref{app:weight_robustness}).
26	
27	\paragraph{MCMC.} NumPyro NUTS, 6{,}000 warmup $+$ 4{,}000 samples $\times$ 4 chains (target acceptance 0.95). Convergence: $\hat{R} < 1.05$, ESS $> 100$ \citep{vehtari2021rhat, gelman2013bda}.
28	
29	\subsection{Main Results}
30	\label{sec:main_results}
31	
32	We compare G-MFRM against seven baselines that address judge bias or contamination separately (Table~\ref{tab:main_results}): Raw Average, MFRM-only (Eq.~\ref{eq:mfrm}), Sequential (MFRM then contamination adjustment), CyclicJudge \citep{cyclicjudge2026}, CyclicJudge+discard, DCR Factor \citep{dcr2025}, and Preference Leakage calibration \citep{preference_leakage2026}. All methods are evaluated by Kendall $\tau$ and Spearman $\rho$ against Chatbot Arena human rankings.
33	
34	\paragraph{Synthetic validation.} On synthetic data ($N = 50$, 20 seeds), G-MFRM reduces ability RMSE by 44\% relative to sequential estimation ($p < 10^{-6}$) and improves ranking accuracy ($\tau$: $0.922$ vs.\ $0.859$, Wilcoxon $p < 0.001$). Contamination susceptibility is recovered with Pearson $r = 0.81$.
35	
36	\paragraph{Predictive fit.} On Arena-Hard, LOO cross-validation strongly favors G-MFRM over MFRM-only ($\Delta\mathrm{ELPD}_{\mathrm{LOO}} = -55.7$, SE $= 9.4$, $|\Delta/\mathrm{SE}| = 5.9$; \citealp{vehtari2017loo}), with stacking weight 1.0 and all Pareto $\hat{k} < 0.7$ (Appendix~\ref{app:loo_comparison}).
37	
38	\paragraph{Exposure coverage and ranking accuracy.} Despite improved predictive fit, G-MFRM's ranking accuracy on real data depends on exposure estimation quality. At $N = 17$, the full item set (500 items) has only 46\% of items with non-zero exposure estimates; G-MFRM over-corrects on the remaining items, yielding $\Delta\tau = -0.044$ relative to the raw average ($\tau = 0.794$ vs.\ $0.838$). We trace this degradation through three item subsets with increasing exposure coverage:
39	%
40	\begin{itemize}
41	    \item Full set (500 items, 46\% $e_i > 0$): $\Delta\tau = -0.044$
42	    \item Filtered set (317 items, 73\% $e_i > 0$): $\Delta\tau = -0.015$
43	    \item Exposed-only (231 items, 100\% $e_i > 0$): $\Delta\tau = 0.000$
44	\end{itemize}
45	%
46	This controlled ablation ($-0.044 \to -0.015 \to 0.000$) demonstrates that over-correction is attributable to incomplete exposure coverage. Two additional variants confirm the mechanism: MFRM-only on the filtered set yields $\Delta\tau = 0.000$, isolating the degradation to the contamination gating term; a contamination-only variant without severity modeling yields $\Delta\tau = -0.118$, demonstrating that naive linear contamination deduction without joint calibration is catastrophically harmful.
47	
48	\paragraph{Contamination diagnostics.} G-MFRM's primary real-data contribution is calibrated per-model contamination estimation. The contamination susceptibility profile (Figure~\ref{fig:contamination_bars}) reveals a clear gradient by model age: older models show $\hat{c}_n > 4$ (GPT-3.5-Turbo: $5.60$; GPT-4-0613: $4.20$), while recent models show near-zero susceptibility (GPT-4o: $0.88$; GPT-4o-mini: $0.93$). MFRM-only estimation absorbs this contamination signal into ability estimates, inflating $\hat{\theta}$ for the most contaminated models by up to 0.79 logits (Figure~\ref{fig:bias_absorption}; Spearman $\rho = 1.0$ between $\hat{c}_n$ and $\Delta\theta$). All parameters achieve $\hat{R} \leq 1.003$ with ESS $\geq 1{,}240$ (Appendices~\ref{app:item_diagnostics} and~\ref{app:ppc}).
49	
50	\paragraph{Judge severity and panel design.} Judge severity profiles vary across the panel (Figure~\ref{fig:judge_severity}), and contamination--ability separation improves with severity diversity: panels with $k \geq 4$ judges covering the severity extremes provide the most reliable diagnostic output (Appendix~\ref{app:judge_count}).
51	
52	\subsection{Error Propagation and Ablation}
53	\label{sec:error_prop_results}
54	
55	\begin{figure}[t]
56	\centering
57	\includegraphics[width=\columnwidth]{fig_ablation_rmse}
58	\caption{Ablation on synthetic data ($N = 50$, 20 seeds). Joint estimation drives the improvement: staged estimation doubles $\theta$-RMSE ($p < 0.001$). Continuous gating provides a moderate gain over binary ($p < 0.001$); removing judge severity $d_j$ has negligible effect on ability recovery (n.s.).}
59	\label{fig:ablation}
60	\end{figure}
61	
62	Table~\ref{tab:error_prop} validates the theoretical prediction (\S\ref{sec:error_prop}): below $\sigma = 0.2$, ability RMSE increases by 5.9\% and contamination RMSE by 7.9\%; beyond the threshold ($\sigma = 0.5$), degradation becomes substantial. Ablation (Figure~\ref{fig:ablation}; full results in Table~\ref{tab:ablation}, Appendix~\ref{app:ablation}) confirms joint estimation as the dominant contributor ($2.0\times$ $\theta$-RMSE increase under staged estimation, $p < 0.001$) and continuous gating over binary ($c_n$-RMSE $-$40\%, $p < 0.001$).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8a87016a-a8fa-43f5-b6fc-720e47d32801",
  "isSidechain": false,
  "promptId": "22ca73de-0bd3-4dbb-9f16-96242e2ec1f9",
  "type": "user",
  "uuid": "091e853d-26dd-4453-8133-b1b5cc8cd6a9",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/experiments.tex",
      "content": "\\section{Experiments}\n\\label{sec:experiments}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth, trim=0 0 250bp 0, clip]{fig6_cn_profile}\n\\caption{Contamination susceptibility $\\hat{c}_n$ (posterior mean $\\pm$ 95\\% CI), ordered by magnitude. Older models (GPT-3.5-Turbo, GPT-4-0613) show 4--6$\\times$ higher susceptibility than recent models (GPT-4o).}\n\\label{fig:contamination_bars}\n\\end{figure}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth, trim=265bp 0 0 0, clip]{fig6_cn_profile}\n\\caption{Ability bias absorbed by MFRM-only estimation: $\\Delta\\theta = \\hat{\\theta}_{\\mathrm{MFRM}} - \\hat{\\theta}_{\\mathrm{G\\text{-}MFRM}}$. The strong correlation with $\\hat{c}_n$ (Spearman $\\rho = 1.0$) confirms that contamination inflates MFRM ability estimates for high-$c_n$ models, as predicted by the OVB analysis (Section~\\ref{sec:confounding}).}\n\\label{fig:bias_absorption}\n\\end{figure}\n\n\\subsection{Setup}\n\\label{sec:setup}\n\n\\paragraph{Data and models.} We evaluate on Arena-Hard \\citep{li2024arenahard}, a benchmark of 500 multi-turn conversational items selected for high separability among frontier models. The evaluation uses all 500 items in a connected incomplete design (${\\sim}$58\\% fill rate of the $N \\times I \\times J$ tensor). Seventeen target models spanning proprietary and open-source families are evaluated: GPT-4o, GPT-4o-mini, Qwen2.5-72B, LLaMA-3.3-70B, Qwen3-8B, Gemma-2-9B, GPT-4-0613, GPT-3.5-Turbo, Claude-3.5-Sonnet, GPT-4-Turbo, LLaMA-3.1-70B, Gemma-2-27B, Claude-3-Opus, LLaMA-3-70B, Mixtral-8x22B, Claude-3-Haiku, and LLaMA-3-8B. Ground-truth rankings are derived from Chatbot Arena human preference data \\citep{zheng2023mtbench}.\n\n\\paragraph{Judges.} Six LLM judges score responses in position-swapped pairwise mode: Claude Sonnet 4.6, DeepSeek-V4-Pro, Gemini-2.5-Pro, LLaMA-3.3-70B, Qwen2.5-72B, and Qwen3-235B. Four provide complete item coverage; two (Gemini, Sonnet) cover ${\\sim}$63--79\\% of items, yielding an incomplete connected design. Two models serve as both judge and target; $d_j$ absorbs self-evaluation bias ($\\tau$ unchanged when excluding self-judging; Appendix~\\ref{app:self_eval}).\n\n\\paragraph{Exposure estimation.} Per-item $e_i$ follows the two-source pipeline in \\S\\ref{sec:staged} (75\\% reference anchoring, 25\\% cross-model agreement; robust to weight configuration, $\\rho \\geq 0.998$; Appendix~\\ref{app:weight_robustness}).\n\n\\paragraph{MCMC.} NumPyro NUTS, 6{,}000 warmup $+$ 4{,}000 samples $\\times$ 4 chains (target acceptance 0.95). Convergence: $\\hat{R} < 1.05$, ESS $> 100$ \\citep{vehtari2021rhat, gelman2013bda}.\n\n\\subsection{Main Results}\n\\label{sec:main_results}\n\nWe compare G-MFRM against seven baselines that address judge bias or contamination separately (Table~\\ref{tab:main_results}): Raw Average, MFRM-only (Eq.~\\ref{eq:mfrm}), Sequential (MFRM then contamination adjustment), CyclicJudge \\citep{cyclicjudge2026}, CyclicJudge+discard, DCR Factor \\citep{dcr2025}, and Preference Leakage calibration \\citep{preference_leakage2026}. All methods are evaluated by Kendall $\\tau$ and Spearman $\\rho$ against Chatbot Arena human rankings.\n\n\\paragraph{Synthetic validation.} On synthetic data ($N = 50$, 20 seeds), G-MFRM reduces ability RMSE by 44\\% relative to sequential estimation ($p < 10^{-6}$) and improves ranking accuracy ($\\tau$: $0.922$ vs.\\ $0.859$, Wilcoxon $p < 0.001$). Contamination susceptibility is recovered with Pearson $r = 0.81$.\n\n\\paragraph{Predictive fit.} On Arena-Hard, LOO cross-validation strongly favors G-MFRM over MFRM-only ($\\Delta\\mathrm{ELPD}_{\\mathrm{LOO}} = -55.7$, SE $= 9.4$, $|\\Delta/\\mathrm{SE}| = 5.9$; \\citealp{vehtari2017loo}), with stacking weight 1.0 and all Pareto $\\hat{k} < 0.7$ (Appendix~\\ref{app:loo_comparison}).\n\n\\paragraph{Exposure coverage and ranking accuracy.} Despite improved predictive fit, G-MFRM's ranking accuracy on real data depends on exposure estimation quality. At $N = 17$, the full item set (500 items) has only 46\\% of items with non-zero exposure estimates; G-MFRM over-corrects on the remaining items, yielding $\\Delta\\tau = -0.044$ relative to the raw average ($\\tau = 0.794$ vs.\\ $0.838$). We trace this degradation through three item subsets with increasing exposure coverage:\n%\n\\begin{itemize}\n    \\item Full set (500 items, 46\\% $e_i > 0$): $\\Delta\\tau = -0.044$\n    \\item Filtered set (317 items, 73\\% $e_i > 0$): $\\Delta\\tau = -0.015$\n    \\item Exposed-only (231 items, 100\\% $e_i > 0$): $\\Delta\\tau = 0.000$\n\\end{itemize}\n%\nThis controlled ablation ($-0.044 \\to -0.015 \\to 0.000$) demonstrates that over-correction is attributable to incomplete exposure coverage. Two additional variants confirm the mechanism: MFRM-only on the filtered set yields $\\Delta\\tau = 0.000$, isolating the degradation to the contamination gating term; a contamination-only variant without severity modeling yields $\\Delta\\tau = -0.118$, demonstrating that naive linear contamination deduction without joint calibration is catastrophically harmful.\n\n\\paragraph{Contamination diagnostics.} G-MFRM's primary real-data contribution is calibrated per-model contamination estimation. The contamination susceptibility profile (Figure~\\ref{fig:contamination_bars}) reveals a clear gradient by model age: older models show $\\hat{c}_n > 4$ (GPT-3.5-Turbo: $5.60$; GPT-4-0613: $4.20$), while recent models show near-zero susceptibility (GPT-4o: $0.88$; GPT-4o-mini: $0.93$). MFRM-only estimation absorbs this contamination signal into ability estimates, inflating $\\hat{\\theta}$ for the most contaminated models by up to 0.79 logits (Figure~\\ref{fig:bias_absorption}; Spearman $\\rho = 1.0$ between $\\hat{c}_n$ and $\\Delta\\theta$). All parameters achieve $\\hat{R} \\leq 1.003$ with ESS $\\geq 1{,}240$ (Appendices~\\ref{app:item_diagnostics} and~\\ref{app:ppc}).\n\n\\paragraph{Judge severity and panel design.} Judge severity profiles vary across the panel (Figure~\\ref{fig:judge_severity}), and contamination--ability separation improves with severity diversity: panels with $k \\geq 4$ judges covering the severity extremes provide the most reliable diagnostic output (Appendix~\\ref{app:judge_count}).\n\n\\subsection{Error Propagation and Ablation}\n\\label{sec:error_prop_results}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig_ablation_rmse}\n\\caption{Ablation on synthetic data ($N = 50$, 20 seeds). Joint estimation drives the improvement: staged estimation doubles $\\theta$-RMSE ($p < 0.001$). Continuous gating provides a moderate gain over binary ($p < 0.001$); removing judge severity $d_j$ has negligible effect on ability recovery (n.s.).}\n\\label{fig:ablation}\n\\end{figure}\n\nTable~\\ref{tab:error_prop} validates the theoretical prediction (\\S\\ref{sec:error_prop}): below $\\sigma = 0.2$, ability RMSE increases by 5.9\\% and contamination RMSE by 7.9\\%; beyond the threshold ($\\sigma = 0.5$), degradation becomes substantial. Ablation (Figure~\\ref{fig:ablation}; full results in Table~\\ref{tab:ablation}, Appendix~\\ref{app:ablation}) confirms joint estimation as the dominant contributor ($2.0\\times$ $\\theta$-RMSE increase under staged estimation, $p < 0.001$) and continuous gating over binary ($c_n$-RMSE $-$40\\%, $p < 0.001$).",
      "numLines": 62,
      "startLine": 1,
      "totalLines": 62
    }
  },
  "sourceToolAssistantUUID": "8a87016a-a8fa-43f5-b6fc-720e47d32801",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/paper_audit_content_0d2a3cf9",
  "sessionId": "6c0691ec-5f2a-45e8-8336-b216f7d74648",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-25T17:14:17.798Z_

<details open><summary>🔧 Tool call — Read · `toolu_0117wecN8hqUqe5VaJzTTvEX`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "091e853d-26dd-4453-8133-b1b5cc8cd6a9",
  "isSidechain": false,
  "requestId": "req_011CbPfQ1NU2iEKvdJXR8f4L",
  "type": "assistant",
  "uuid": "878fab20-ee2b-4cad-9fa6-e65875dc9718",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/paper_audit_content_0d2a3cf9",
  "sessionId": "6c0691ec-5f2a-45e8-8336-b216f7d74648",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GrsQFcF17aMgSKpeSqAZ7n",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11963,
      "cache_read_input_tokens": 38769,
      "output_tokens": 758,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11963,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 758,
          "cache_read_input_tokens": 38769,
          "cache_creation_input_tokens": 11963,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11963
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

_source line 35 · 2026-05-25T17:14:17.806Z_

<details><summary>↩ Tool result · `toolu_0117wecN8hqUqe5VaJzTTvEX`</summary>

```text
1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	We introduced G-MFRM, a Bayesian measurement model that jointly estimates model ability, judge severity, and contamination susceptibility within a single inferential framework. The key theoretical contribution is formalizing the confounding between judge bias and benchmark contamination as omitted variable bias: omitting either facet produces a closed-form bias in the other, with direction and magnitude determined by the exposure--severity covariance (Section~\ref{sec:confounding}).
5	
6	On Arena-Hard, G-MFRM provides calibrated per-model contamination diagnostics unavailable from existing methods: older models exhibit 4--6$\times$ higher susceptibility, and MFRM-only estimation inflates ability for the most contaminated models by up to 0.79 logits. A controlled coverage ablation ($\Delta\tau$: $-0.044 \to -0.015 \to 0.000$ as coverage increases to 100\%) demonstrates that over-correction is attributable to incomplete exposure estimation, and complete coverage is sufficient for safe contamination correction. Ablation confirms joint estimation as the dominant contributor: staged estimation doubles ability RMSE.
7	
8	Two practical implications emerge. First, evaluation frameworks that treat judge bias and contamination as independent incur systematic errors; future LLM evaluation should model these facets jointly. Second, the coverage--degradation finding provides an actionable quality requirement for contamination-aware evaluation. Several directions remain open: higher-rank contamination decompositions for domain-specific effects, simulation-based recalibration \citep{talts2018sbc} of $c_n$ credible intervals (71\% coverage at nominal 95\%), and scaling to larger model populations and diverse benchmarks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "878fab20-ee2b-4cad-9fa6-e65875dc9718",
  "isSidechain": false,
  "promptId": "22ca73de-0bd3-4dbb-9f16-96242e2ec1f9",
  "type": "user",
  "uuid": "8d687ba9-96cd-4130-9c0c-12d1cf07824b",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/conclusion.tex",
      "content": "\\section{Conclusion}\n\\label{sec:conclusion}\n\nWe introduced G-MFRM, a Bayesian measurement model that jointly estimates model ability, judge severity, and contamination susceptibility within a single inferential framework. The key theoretical contribution is formalizing the confounding between judge bias and benchmark contamination as omitted variable bias: omitting either facet produces a closed-form bias in the other, with direction and magnitude determined by the exposure--severity covariance (Section~\\ref{sec:confounding}).\n\nOn Arena-Hard, G-MFRM provides calibrated per-model contamination diagnostics unavailable from existing methods: older models exhibit 4--6$\\times$ higher susceptibility, and MFRM-only estimation inflates ability for the most contaminated models by up to 0.79 logits. A controlled coverage ablation ($\\Delta\\tau$: $-0.044 \\to -0.015 \\to 0.000$ as coverage increases to 100\\%) demonstrates that over-correction is attributable to incomplete exposure estimation, and complete coverage is sufficient for safe contamination correction. Ablation confirms joint estimation as the dominant contributor: staged estimation doubles ability RMSE.\n\nTwo practical implications emerge. First, evaluation frameworks that treat judge bias and contamination as independent incur systematic errors; future LLM evaluation should model these facets jointly. Second, the coverage--degradation finding provides an actionable quality requirement for contamination-aware evaluation. Several directions remain open: higher-rank contamination decompositions for domain-specific effects, simulation-based recalibration \\citep{talts2018sbc} of $c_n$ credible intervals (71\\% coverage at nominal 95\\%), and scaling to larger model populations and diverse benchmarks.",
      "numLines": 8,
      "startLine": 1,
      "totalLines": 8
    }
  },
  "sourceToolAssistantUUID": "878fab20-ee2b-4cad-9fa6-e65875dc9718",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/paper_audit_content_0d2a3cf9",
  "sessionId": "6c0691ec-5f2a-45e8-8336-b216f7d74648",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 36 · 2026-05-25T17:14:18.212Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Ra2ofpSKzaD53GD6MLJe8u`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8d687ba9-96cd-4130-9c0c-12d1cf07824b",
  "isSidechain": false,
  "requestId": "req_011CbPfQ1NU2iEKvdJXR8f4L",
  "type": "assistant",
  "uuid": "a6143560-74eb-492a-b43e-80383fb24fa5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/paper_audit_content_0d2a3cf9",
  "sessionId": "6c0691ec-5f2a-45e8-8336-b216f7d74648",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GrsQFcF17aMgSKpeSqAZ7n",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11963,
      "cache_read_input_tokens": 38769,
      "output_tokens": 758,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11963,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 758,
          "cache_read_input_tokens": 38769,
          "cache_creation_input_tokens": 11963,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11963
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

_source line 37 · 2026-05-25T17:14:18.221Z_

<details><summary>↩ Tool result · `toolu_01Ra2ofpSKzaD53GD6MLJe8u`</summary>

```text
1	The evaluation uses a single benchmark (Arena-Hard) with an incomplete observation design (66\% fill rate); generalization to other benchmarks and larger model populations remains to be verified. Posterior credible intervals for contamination susceptibility $c_n$ exhibit systematic overconfidence (71\% coverage at nominal 95\%; Appendix~\ref{app:ci_coverage}), a structural issue from the multiplicative coupling and HalfNormal boundary at $c_n = 0$ that warrants simulation-based recalibration. The rank-1 contamination structure assumes a single $c_n$ per model, whereas contamination may be domain-specific (e.g., coding vs.\ reasoning), motivating higher-rank decompositions in future work.
2	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a6143560-74eb-492a-b43e-80383fb24fa5",
  "isSidechain": false,
  "promptId": "22ca73de-0bd3-4dbb-9f16-96242e2ec1f9",
  "type": "user",
  "uuid": "04595298-3b72-414b-9444-eef8eba3b401",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/limitations.tex",
      "content": "The evaluation uses a single benchmark (Arena-Hard) with an incomplete observation design (66\\% fill rate); generalization to other benchmarks and larger model populations remains to be verified. Posterior credible intervals for contamination susceptibility $c_n$ exhibit systematic overconfidence (71\\% coverage at nominal 95\\%; Appendix~\\ref{app:ci_coverage}), a structural issue from the multiplicative coupling and HalfNormal boundary at $c_n = 0$ that warrants simulation-based recalibration. The rank-1 contamination structure assumes a single $c_n$ per model, whereas contamination may be domain-specific (e.g., coding vs.\\ reasoning), motivating higher-rank decompositions in future work.\n",
      "numLines": 2,
      "startLine": 1,
      "totalLines": 2
    }
  },
  "sourceToolAssistantUUID": "a6143560-74eb-492a-b43e-80383fb24fa5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/paper_audit_content_0d2a3cf9",
  "sessionId": "6c0691ec-5f2a-45e8-8336-b216f7d74648",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-25T17:14:18.689Z_

<details open><summary>🔧 Tool call — Read · `toolu_01SUfgQsEtcTLHHXyxMdCpv4`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "04595298-3b72-414b-9444-eef8eba3b401",
  "isSidechain": false,
  "requestId": "req_011CbPfQ1NU2iEKvdJXR8f4L",
  "type": "assistant",
  "uuid": "2d09688d-65d2-4b33-907b-1dac4537bbad",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/paper_audit_content_0d2a3cf9",
  "sessionId": "6c0691ec-5f2a-45e8-8336-b216f7d74648",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GrsQFcF17aMgSKpeSqAZ7n",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11963,
      "cache_read_input_tokens": 38769,
      "output_tokens": 758,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11963,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 758,
          "cache_read_input_tokens": 38769,
          "cache_creation_input_tokens": 11963,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11963
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

_source line 39 · 2026-05-25T17:14:18.974Z_

<details><summary>↩ Tool result · `toolu_01SUfgQsEtcTLHHXyxMdCpv4`</summary>

```text
1	\section{Proofs of Propositions~\ref{prop:no_new} and~\ref{prop:exposure_variation}}
2	\label{app:prop_proofs}
3	
4	\begin{proof}[Proof of Proposition~\ref{prop:no_new}]
5	Suppose $c_n' = c_n + \delta$ preserves all response probabilities. Then $\delta \cdot e_i = 0$ for all items. Since $e_i \neq 0$ for at least one item by assumption, $\delta = 0$. Fixing $e_i$ externally eliminates the bilinear ambiguity $c_n \cdot e_i = (\lambda c_n)(\lambda^{-1} e_i)$ that would otherwise render the decomposition non-unique.
6	\end{proof}
7	
8	\begin{proof}[Proof of Proposition~\ref{prop:exposure_variation}]
9	When exposure is constant, the linear predictor becomes $(\theta_n + c_n \cdot e) - b_i - d_j - \tau_k$, equivalent to a standard MFRM with reparameterized ability $\theta^*_n = \theta_n + c_n \cdot e$. No configuration of response data can distinguish $(\theta_n, c_n)$ from $(\theta_n + \epsilon, c_n - \epsilon/e)$ for any $\epsilon$.
10	\end{proof}
11	
12	
13	\section{Proof of Theorem~\ref{thm:sufficient}}
14	\label{app:proof}
15	
16	We prove that the G-MFRM is locally identifiable under the conditions of Theorem~\ref{thm:sufficient}. Following \citet{rothenberg1971}, a parametric model is locally identifiable at the true parameter vector $\boldsymbol{\psi}_0$ if and only if the Fisher information matrix $\mathbf{F}(\boldsymbol{\psi}_0)$ is non-singular.
17	
18	\paragraph{Setup.} The G-MFRM parameter vector is $\boldsymbol{\psi} = (\boldsymbol{\theta}, \mathbf{c}, \mathbf{b}, \mathbf{d}, \boldsymbol{\tau})$, where $\boldsymbol{\theta} \in \mathbb{R}^{N-1}$ (after the location constraint $\sum_n \theta_n = 0$), $\mathbf{c} \in \mathbb{R}_{\geq 0}^N$, $\mathbf{b} \in \mathbb{R}^I$, $\mathbf{d} \in \mathbb{R}^J$, and $\boldsymbol{\tau} \in \mathbb{R}^{K-1}$. The exposure vector $\mathbf{e} = (e_1, \ldots, e_I)$ is fixed externally and treated as known. The linear predictor is $\eta_{nijk} = \theta_n - b_i - d_j - \tau_k + c_n \cdot e_i$, with partial derivatives:
19	%
20	\begin{align*}
21	\frac{\partial \eta_{nijk}}{\partial \theta_n} &= 1, \quad
22	\frac{\partial \eta_{nijk}}{\partial c_n} = e_i, \quad
23	\frac{\partial \eta_{nijk}}{\partial b_i} = -1, \\
24	\frac{\partial \eta_{nijk}}{\partial d_j} &= -1, \quad
25	\frac{\partial \eta_{nijk}}{\partial \tau_k} = -1.
26	\end{align*}
27	
28	\paragraph{Fisher information weights.} For each observation cell $(n,i,j)$, the Fisher information weight under the cumulative logit model is
29	%
30	\begin{equation}
31	\label{eq:fisher_weight}
32	w_{nij} = \sum_{k=1}^{K} \frac{\bigl[\sigma'(\eta_{nijk}) - \sigma'(\eta_{nij,k+1})\bigr]^2}{P(Y_{nij} = k)},
33	\end{equation}
34	%
35	where $\sigma(x) = (1 + e^{-x})^{-1}$, $\sigma'(x) = \sigma(x)(1 - \sigma(x))$, and we set $\sigma'(\eta_{nij,0}) = \sigma'(\eta_{nij,K+1}) = 0$ at the boundaries. Since $P(Y_{nij} = k) > 0$ for all categories and $\sigma'(\cdot) > 0$, we have $w_{nij} > 0$ for all $(n,i,j)$.
36	
37	\paragraph{Step 1: The $(\theta_n, c_n)$ submatrix.} For each model $n$, the $2 \times 2$ Fisher information submatrix is
38	%
39	\begin{equation}
40	\label{eq:fisher_block}
41	\mathbf{F}_n = \sum_{i=1}^{I} \sum_{j=1}^{J} w_{nij}
42	\begin{pmatrix} 1 & e_i \\ e_i & e_i^2 \end{pmatrix}.
43	\end{equation}
44	%
45	Its determinant is
46	%
47	\begin{multline}
48	\det \mathbf{F}_n = \Bigl(\textstyle\sum_{i,j} w_{nij}\Bigr)\Bigl(\textstyle\sum_{i,j} w_{nij}\, e_i^2\Bigr) \\
49	- \Bigl(\textstyle\sum_{i,j} w_{nij}\, e_i\Bigr)^2 = W_n^2 \cdot \mathrm{Var}_w(e_i),
50	\end{multline}
51	%
52	where $W_n = \sum_{i,j} w_{nij}$ and $\mathrm{Var}_w(e_i) = \overline{e^2}_n - \bar{e}_n^2$ is the weighted variance of exposure with weights $w_{nij}$. By the Cauchy--Schwarz inequality, $\mathrm{Var}_w(e_i) \geq 0$, with equality if and only if $e_i$ is constant across all items with $w_{nij} > 0$. Under conditions~(i) and~(iii), the observed items for model $n$ include at least two distinct exposure values with $w_{nij} > 0$ for the corresponding cells. Therefore $\mathrm{Var}_w(e_i) > 0$, $\det \mathbf{F}_n > 0$, and each $\mathbf{F}_n$ is positive definite.
53	
54	\paragraph{Step 2: Item and judge blocks.} Under the connected design (condition~i), each item $i$ is observed by at least one $(n,j)$ pair, so the item difficulty block has positive diagonal entries $[\mathbf{F}_{bb}]_{ii} = \sum_{n,j} w_{nij} > 0$ (summing over observed cells). Similarly, each judge $j$ observes at least one $(n,i)$ pair, giving $[\mathbf{F}_{dd}]_{jj} = \sum_{n,i} w_{nij} > 0$. Condition~(ii) ($J \geq 2$) ensures the judge block has sufficient dimension to separate judge effects from the intercept. Both blocks are positive definite.
55	
56	\paragraph{Step 3: Schur complement argument.} The full Fisher information matrix $\mathbf{F}$ contains off-diagonal blocks coupling the parameter groups. Partition as
57	%
58	\begin{equation*}
59	\mathbf{F} = \begin{pmatrix} \mathbf{A} & \mathbf{B} \\ \mathbf{B}^\top & \mathbf{D} \end{pmatrix},
60	\end{equation*}
61	%
62	where $\mathbf{A} = \mathrm{blockdiag}(\mathbf{F}_1, \ldots, \mathbf{F}_N)$ collects all $(\theta_n, c_n)$ submatrices and $\mathbf{D}$ collects the $(\mathbf{b}, \mathbf{d}, \boldsymbol{\tau})$ blocks. From Step~1, $\mathbf{A}$ is positive definite. The Schur complement
63	%
64	\begin{equation}
65	\label{eq:schur}
66	\mathbf{S} = \mathbf{D} - \mathbf{B}^\top \mathbf{A}^{-1} \mathbf{B}
67	\end{equation}
68	%
69	equals the conditional Fisher information for $(\mathbf{b}, \mathbf{d}, \boldsymbol{\tau})$ given $(\boldsymbol{\theta}, \mathbf{c})$. Conditioning on $(\boldsymbol{\theta}, \mathbf{c})$ with fixed $\mathbf{e}$ reduces the model to a standard MFRM with known offsets $c_n \cdot e_i$, whose identifiability is established by \citet[Chapter~5]{sanmartin2016} under conditions~(i), (ii), and~(iv). Therefore $\mathbf{S}$ is positive definite.
70	
71	Since both $\mathbf{A}$ and $\mathbf{S}$ are positive definite:
72	%
73	\begin{equation*}
74	\det \mathbf{F} = \det \mathbf{A} \cdot \det \mathbf{S} > 0,
75	\end{equation*}
76	%
77	establishing non-singularity of $\mathbf{F}$ and hence local identifiability. \qed
78	
79	\paragraph{Local vs.\ global identifiability.} Theorem~\ref{thm:sufficient} establishes \emph{local} identifiability: the Fisher information matrix is non-singular at the true parameter value, guaranteeing that no infinitesimally close parameter vector produces the same likelihood. This does not rule out discrete global non-identifiabilities (i.e., isolated points in parameter space with identical likelihood). However, the HalfNormal prior on $c_n$ restricts the parameter space to $c_n \geq 0$, eliminating the sign ambiguity that would otherwise create a global reflection $(\theta_n + \delta,\, c_n - \delta/e_i)$. Combined with the location constraint $\sum_n \theta_n = 0$ and the empirical observation that the posterior is unimodal across all chains (no mode-switching detected), the local result provides a practical guarantee of unique parameter recovery.
80	
81	\paragraph{Role of the Cauchy--Schwarz inequality.} The key step in Step~1 is the decomposition $\det \mathbf{F}_n = W_n^2 \cdot \mathrm{Var}_w(e_i)$, where the weighted variance $\mathrm{Var}_w(e_i) = \mathbb{E}_w[e_i^2] - (\mathbb{E}_w[e_i])^2 \geq 0$ by the Cauchy--Schwarz inequality applied to the vectors $(\sqrt{w_{nij}})$ and $(\sqrt{w_{nij}}\, e_i)$. Strict positivity follows from the requirement that $e_i$ takes at least two distinct values over observed items (condition~iii): if $e_i = e$ for all $i$ with $w_{nij} > 0$, then $\mathrm{Var}_w(e_i) = 0$ and the $(\theta_n, c_n)$ block becomes singular, recovering Proposition~\ref{prop:exposure_variation}. The Cauchy--Schwarz bound is tight only in this degenerate case, so any non-trivial exposure variation suffices for identification.
82	
83	
84	\section{Explicit Form of the OVB Coefficient $\gamma_n$}
85	\label{app:gamma}
86	
87	Under the MFRM logistic link, a first-order Taylor expansion of Observation~\ref{obs:ovb} yields an explicit approximation for the bias coefficient $\gamma_n$:
88	%
89	\begin{equation}
90	\label{eq:gamma_explicit}
91	\gamma_n \approx \frac{\sum_{i} w_{ni} \cdot e_i \cdot p_{ni}(1 - p_{ni})}{\sum_{i} w_{ni} \cdot p_{ni}(1 - p_{ni})},
92	\end{equation}
93	%
94	where $p_{ni} = \sigma(\theta_n - b_i - \bar{d})$ is the MFRM predicted probability averaged over judges and $w_{ni}$ is the effective item weight (number of judge observations for item $i$ on model $n$). Eq.~\ref{eq:gamma_explicit} is a weighted mean of the exposure values $e_i$, with weights proportional to the Fisher information $p_{ni}(1 - p_{ni})$. Items near the boundary ($p_{ni} \approx 0.5$) contribute more to the bias than items at the extremes, because the logistic link is most sensitive at these points. This approximation is accurate to first order in $(c_n \cdot e_i)$; the synthetic validation in Section~\ref{sec:confounding} ($r = 0.86$) confirms that the linear approximation captures the dominant bias structure.
95	
96	
97	\section{Murphy--Topel Variance Correction}
98	\label{app:murphy_topel}
99	
100	The three-stage G-MFRM procedure treats Stage~2 exposure estimates $\hat{e}_i$ as fixed in Stage~3, understating posterior uncertainty by ignoring estimation error in $\hat{e}_i$. We derive the Murphy--Topel correction \citep{murphy1985} adapted to the G-MFRM setting.
101	
102	\paragraph{Setup.} Let $\boldsymbol{\alpha} = (e_1, \ldots, e_I)$ denote the Stage~2 parameters estimated from an independent dataset with log-likelihood $\ell_2(\boldsymbol{\alpha})$, and let $\boldsymbol{\psi} = (\boldsymbol{\theta}, \mathbf{c}, \mathbf{b}, \mathbf{d}, \boldsymbol{\tau})$ denote the Stage~3 parameters estimated with log-likelihood $\ell_3(\boldsymbol{\psi}; \hat{\boldsymbol{\alpha}})$, where $\hat{\boldsymbol{\alpha}}$ is plugged in as known.
103	
104	\paragraph{Naive and Stage~2 variances.} The naive (uncorrected) variance of $\hat{\boldsymbol{\psi}}$ is
105	%
106	\begin{equation}
107	\mathbf{V}_3 = \left[-\frac{\partial^2 \ell_3}{\partial \boldsymbol{\psi}\, \partial \boldsymbol{\psi}^\top}\bigg|_{\hat{\boldsymbol{\psi}},\, \hat{\boldsymbol{\alpha}}}\right]^{-1},
108	\end{equation}
109	%
110	and the Stage~2 variance is
111	%
112	\begin{equation}
113	\mathbf{V}_2 = \left[-\frac{\partial^2 \ell_2}{\partial \boldsymbol{\alpha}\, \partial \boldsymbol{\alpha}^\top}\bigg|_{\hat{\boldsymbol{\alpha}}}\right]^{-1}.
114	\end{equation}
115	
116	\paragraph{Cross-derivative matrix.} The coupling between stages is captured by the cross-derivative
117	%
118	\begin{equation}
119	\mathbf{C} = \frac{\partial^2 \ell_3}{\partial \boldsymbol{\psi}\, \partial \boldsymbol{\alpha}^\top}\bigg|_{\hat{\boldsymbol{\psi}},\, \hat{\boldsymbol{\alpha}}}.
120	\end{equation}
121	%
122	In the G-MFRM, non-zero entries of $\mathbf{C}$ arise from the contamination gating term $c_n \cdot e_i$. The key entry is
123	%
124	\begin{equation}
125	\frac{\partial^2 \ell_3}{\partial c_n\, \partial e_i} = \sum_{j=1}^{J} \frac{\partial^2 \ell_{nij}}{\partial \eta_{nij}^2} \cdot c_n,
126	\end{equation}
127	%
128	which is proportional to $c_n$: models with zero contamination contribute no cross-derivative. Similarly, $\partial^2 \ell_3 / (\partial \theta_n\, \partial e_i)$ involves only indirect coupling through the shared item observations. The correction is therefore concentrated on the contamination parameters of models with $c_n > 0$.
129	
130	\paragraph{Corrected variance.} The Murphy--Topel corrected variance is
131	%
132	\begin{equation}
133	\label{eq:murphy_topel}
134	\mathbf{V}_{\mathrm{MT}} = \mathbf{V}_3 + \mathbf{V}_3\, \mathbf{C}\, \mathbf{V}_2\, \mathbf{C}^\top\, \mathbf{V}_3.
135	\end{equation}
136	%
137	The correction term $\mathbf{V}_3 \mathbf{C} \mathbf{V}_2 \mathbf{C}^\top \mathbf{V}_3$ is positive semi-definite, so $\mathbf{V}_{\mathrm{MT}} \succeq \mathbf{V}_3$: the corrected variance is always at least as large as the naive variance. The inflation is concentrated on $c_n$ for contaminated models and is negligible for $\theta_n$ when contamination is sparse, consistent with the empirical pattern in Table~\ref{tab:error_prop}.
138	
139	\paragraph{Implementation.} We estimate $\mathbf{V}_2$ from the Stage~2 bootstrap and compute $\mathbf{C}$ via finite differences of the Stage~3 log-likelihood evaluated at perturbed $\hat{\boldsymbol{\alpha}}$ values. Corrected credible intervals are obtained by inflating Stage~3 posterior samples by $\sqrt{\mathrm{diag}(\mathbf{V}_{\mathrm{MT}}) / \mathrm{diag}(\mathbf{V}_3)}$.
140	
141	
142	\section{Ablation Study}
143	\label{app:ablation}
144	
145	\begin{table}[h]
146	\centering
147	\scriptsize
148	\setlength{\tabcolsep}{3pt}
149	\begin{tabular}{lccc}
150	\toprule
151	\textbf{Variant} & $\theta$-RMSE & $\tau$ & $c_n$-RMSE \\
152	\midrule
153	Full G-MFRM & 0.124 $\pm$ 0.016 & 0.922 $\pm$ 0.010 & 0.593 $\pm$ 0.224 \\
154	$-$ Judge severity ($d_j$) & 0.127 $\pm$ 0.016 & 0.922 $\pm$ 0.010 & 0.629 $\pm$ 0.243 \\
155	Binary gating & 0.137 $\pm$ 0.016 & 0.909 $\pm$ 0.014 & 0.833 $\pm$ 0.226 \\
156	Staged estimation & 0.254 $\pm$ 0.045 & 0.839 $\pm$ 0.035 & 1.382 $\pm$ 0.164 \\
157	\bottomrule
158	\end{tabular}
159	\caption{Ablation study on synthetic data ($N = 50$, $I = 100$, $J = 8$, 20 seeds). Each row removes or modifies one component of the full G-MFRM. Staged estimation refers to fitting MFRM and contamination sequentially rather than jointly. All differences from Full G-MFRM are significant at $p < 0.001$ (Wilcoxon) except $-d_j$ on $\theta$-RMSE ($p = 0.245$) and $\tau$ ($p = 0.344$).}
160	\label{tab:ablation}
161	\end{table}
162	
163	The ablation confirms that joint estimation is the primary contributor to G-MFRM's advantage: staged estimation increases $\theta$-RMSE by $2.0\times$ (from 0.124 to 0.254, $p < 0.001$) and $c_n$-RMSE by $2.3\times$ (from 0.593 to 1.382, $p < 0.001$), with $\tau$ dropping from 0.922 to 0.839. This degradation directly reflects the omitted variable bias characterized in Section~\ref{sec:confounding}: when contamination and judge effects are estimated sequentially, the first-stage estimates absorb the unmodeled facet.
164	
165	Replacing continuous exposure $e_i \in [0,1]$ with binary gating ($e_i \in \{0, 1\}$) increases $c_n$-RMSE by 40\% (from 0.593 to 0.833, $p < 0.001$), indicating that graded exposure modeling captures contamination magnitude more precisely than a binary flag. The effect on $\theta$-RMSE is moderate ($+$10\%, $p < 0.001$), suggesting that the binary approximation still captures the dominant contamination signal but loses precision on partially exposed items.
166	
167	Removing judge severity $d_j$ does not significantly affect ability estimates ($\theta$-RMSE $+$2.4\%, $p = 0.245$; $\tau$ identical, $p = 0.344$) but significantly degrades contamination recovery ($c_n$-RMSE $+$6.1\%, $p < 0.001$). This confirms that $d_j$ serves as a diagnostic component that improves contamination estimation precision rather than ranking accuracy: without explicit judge severity modeling, judge-induced score variation is partially absorbed into the contamination estimates, inflating $c_n$-RMSE. The $d_j$ profile also provides independent diagnostic value for judge calibration (e.g., Claude Opus $d_j = +0.60$ vs.\ Mistral $-0.74$ in the real-data evaluation).
168	
169	\begin{figure}[h]
170	\centering
171	\includegraphics[width=\columnwidth]{theta_tau_boxplot}
172	\caption{Ranking accuracy (Kendall $\tau$ with ground truth) across ablation variants. Full G-MFRM achieves the highest and most consistent $\tau$; staged estimation shows the largest degradation and highest variance. Synthetic data: $N = 50$, $I = 100$, $J = 8$, 20 seeds.}
173	\label{fig:ablation_tau}
174	\end{figure}
175	
176	
177	\section{Posterior Predictive Check}
178	\label{app:ppc}
179	
180	Figure~\ref{fig:ppc} shows the posterior predictive distribution from 1{,}000 posterior draws over 5{,}661 observations. The predicted and observed response distributions are well-aligned (predicted mean win rate $0.593$ vs.\ observed $0.599$), with no systematic discrepancy across item difficulty or model ability levels.
181	
182	\begin{figure}[h]
183	\centering
184	\includegraphics[width=\columnwidth]{fig_ppc}
185	\caption{Posterior predictive check. Distribution of predicted (gray) and observed (black) response rates across all model--item--judge triplets. Mean predicted $= 0.593$, mean observed $= 0.599$.}
186	\label{fig:ppc}
187	\end{figure}
188	
189	
190	\section{LOO Model Comparison}
191	\label{app:loo_comparison}
192	
193	Figure~\ref{fig:model_comparison} visualizes the LOO-ELPD difference between G-MFRM and MFRM-only. G-MFRM is the reference model ($\Delta\mathrm{ELPD} = 0$); MFRM-only shows a deficit of $-55.7$ (SE $= 9.4$), confirming that the contamination gating term substantially improves held-out predictive fit.
194	
195	\begin{figure}[h]
196	\centering
197	\includegraphics[width=\columnwidth]{model_comparison}
198	\caption{LOO-ELPD model comparison. G-MFRM (reference) versus MFRM-only. Error bars show $\pm$1 SE. The $|\Delta/\mathrm{SE}| = 5.9$ strongly favors G-MFRM.}
199	\label{fig:model_comparison}
200	\end{figure}
201	
202	Figure~\ref{fig:pareto_k} shows the Pareto $\hat{k}$ diagnostic values for both models. All observations have $\hat{k} < 0.7$, confirming that the LOO approximation is reliable for both models.
203	
204	\begin{figure}[h]
205	\centering
206	\includegraphics[width=\columnwidth]{pareto_k_plot}
207	\caption{Pareto $\hat{k}$ diagnostics for G-MFRM (left) and MFRM-only (right). All 5{,}661 observations fall below the $\hat{k} = 0.7$ threshold, confirming reliable LOO estimates.}
208	\label{fig:pareto_k}
209	\end{figure}
210	
211	
212	\section{Self-Evaluation Robustness}
213	\label{app:self_eval}
214	
215	Two models---Qwen2.5-72B and LLaMA-3.3-70B---appear as both judge and target in our evaluation. Self-judging introduces a potential confound: a model may score its own responses more favorably. We examine the empirical magnitude of this effect and its impact on rankings.
216	
217	Qwen2.5-72B achieves a perfect self-judging win rate of 1.000 (42/42 items), compared to a cross-judge mean win rate of 0.714 for the same model. LLaMA-3.3-70B shows a self-judging win rate of 0.912, compared to a cross-judge mean of 0.823. Both values are elevated relative to cross-judge baselines, consistent with same-family preference leakage \citep{preference_leakage2026}.
218	
219	To assess sensitivity, we re-fit G-MFRM excluding all 99 self-judging observations (Qwen2.5-72B and LLaMA-3.3-70B judging their own responses). The resulting ranking yields $\tau = 0.857$, identical to the full-data G-MFRM point estimate, with a swap at ranks 2--3. Contamination susceptibility estimates $c_n$ shift by less than 0.15 for all models. This confirms that $d_j$ absorbs the bulk of self-evaluation bias and that rankings are robust to excluding self-judging pairs.
220	
221	
222	\section{Judge Severity Profiles}
223	\label{app:judge_severity}
224	
225	Table~\ref{tab:judge_severity} reports posterior estimates of judge severity $d_j$ for all nine judges. Positive values indicate stricter scoring (lower win rates); negative values indicate more lenient scoring. Proprietary models cluster at the strict end, while open-source models tend to be more lenient.
226	
227	\begin{table}[h]
228	\centering
229	\small
230	\begin{tabular}{lcc}
231	\toprule
232	\textbf{Judge} & $\hat{d}_j$ & 95\% CI \\
233	\midrule
234	Claude Opus 4.7 & $+0.60$ & [$+0.43$, $+0.76$] \\
235	GPT-5.5 & $+0.53$ & [$+0.37$, $+0.70$] \\
236	DeepSeek-V4-Pro & $+0.31$ & [$+0.07$, $+0.54$] \\
237	Claude Sonnet 4.6 & $+0.14$ & [$-0.04$, $+0.31$] \\
238	Gemini-2.5-Pro & $-0.04$ & [$-0.27$, $+0.19$] \\
239	Qwen3-235B & $-0.04$ & [$-0.24$, $+0.16$] \\
240	Qwen2.5-72B & $-0.35$ & [$-0.64$, $-0.07$] \\
241	LLaMA-3.3-70B & $-0.42$ & [$-0.66$, $-0.18$] \\
242	Mistral-Large-2 & $-0.74$ & [$-1.10$, $-0.37$] \\
243	\bottomrule
244	\end{tabular}
245	\caption{Judge severity estimates ($d_j$) for all nine judges. Positive = stricter scoring. The severity range spans 1.34 logits (Claude Opus to Mistral), comparable to $\sim$1 standard deviation of model ability.}
246	\label{tab:judge_severity}
247	\end{table}
248	
249	
250	\section{Judge Count Sensitivity}
251	\label{app:judge_count}
252	
253	Table~\ref{tab:judge_count} reports ranking accuracy as a function of the number of judges $k$, obtained by subsampling from the full 9-judge panel (10 random subsets per $k$; $k = 9$ uses the full panel). G-MFRM outperforms both raw averaging and sequential estimation at all judge counts. Rank agreement increases monotonically with $k$ ($\tau = 0.771 \to 0.857$), and variance contracts as additional judges improve $d_j$ and $c_n$ estimation. At $k \geq 4$, G-MFRM exceeds the full-panel baseline $\tau = 0.786$, suggesting that four diverse judges suffice for practical deployment.
254	
255	\begin{table}[h]
256	\centering
257	\small
258	\begin{tabular}{lcccc}
259	\toprule
260	$k$ & Raw Avg & Sequential & G-MFRM & $\Delta\tau$ \\
261	\midrule
262	2 & $.755 \pm .088$ & $.764 \pm .096$ & $.771 \pm .081$ & $+.017$ \\
263	4 & $.779 \pm .041$ & $.786 \pm .048$ & $.800 \pm .045$ & $+.021$ \\
264	6 & $.800 \pm .030$ & $.807 \pm .048$ & $.821 \pm .051$ & $+.021$ \\
265	9 & $.786$ & $.786$ & $.857$ & $+.071$ \\
266	\bottomrule
267	\end{tabular}
268	\caption{Kendall $\tau$ with Chatbot Arena rankings as a function of judge count $k$. $\Delta\tau$ = G-MFRM $-$ Raw Average. Values for $k < 9$ are mean $\pm$ std over 10 random judge subsets.}
269	\label{tab:judge_count}
270	\end{table}
271	
272	Leave-one-judge-out analysis reveals that three judges---Claude Opus 4.7 ($d_j = +0.60$), GPT-5.5 ($+0.53$), and LLaMA-3.3-70B ($-0.42$)---are individually necessary for the ranking improvement: removing any one of these reduces G-MFRM $\tau$ to the baseline ($0.786$), while removing any of the other six judges preserves $\tau = 0.857$. These three judges span the severity spectrum (the two strictest and the second-most lenient), suggesting that contamination$\times$judge interaction identification requires sufficient severity diversity. This provides practical guidance: judge panels should include models with diverse scoring tendencies rather than homogeneous judges.
273	
274	G-MFRM requires $\geq 4$ MCMC chains for reliable contamination estimation; reduced chain counts attenuate $c_n$ estimates toward the prior mean, compressing inter-model differences.
275	
276	
277	\section{Stage~2 Weight Robustness}
278	\label{app:weight_robustness}
279	
280	All four weight configurations produce identical model rankings and near-perfect exposure score agreement (Spearman $\rho \geq 0.998$; Table~\ref{tab:weight_robustness}), confirming that the default 75/25 split is not a sensitive hyperparameter choice.
281	
282	\begin{table}[h]
283	\centering
284	\small
285	\begin{tabular}{lc}
286	\toprule
287	\textbf{Weight Config} & \textbf{Exposure} $\rho$ \\
288	\midrule
289	50 / 50 & 0.998 \\
290	75 / 25 (default) & 1.000 \\
291	90 / 10 & 0.999 \\
292	100 / 0 & 0.998 \\
293	\bottomrule
294	\end{tabular}
295	\caption{Stage~2 weight robustness. Weight Config denotes the percentage assigned to reference model anchoring vs.\ cross-model agreement. All configurations produce identical model rankings. Exposure $\rho$ is the Spearman correlation of per-item $e_i$ scores relative to the default 75/25 configuration.}
296	\label{tab:weight_robustness}
297	\end{table}
298	
299	
300	\section{Power Analysis}
301	\label{app:power}
302	
303	The observed effect size in the real-data evaluation is $\Delta\tau = 0.071$ (G-MFRM $\tau = 0.857$ vs.\ baseline $\tau = 0.786$). We conduct a permutation-based power analysis to determine the sample sizes required to detect this effect at $\alpha = 0.05$.
304	
305	We simulate ranking comparisons under the alternative hypothesis $H_1\!: \Delta\tau = 0.071$ by bootstrapping from the observed posterior distribution of G-MFRM ability estimates and recomputing $\tau$ against ground truth at varying model counts $N$. For each $N$, we draw 10{,}000 permutation replicates and compute the rejection rate at $\alpha = 0.05$ (two-sided).
306	
307	At $N = 8$ (our evaluation), power is approximately 50\%, explaining the non-significant bootstrap result ($\Delta\tau$ 95\% CI $[-0.071, 0.071]$). Achieving 80\% power requires $N \approx 17$ models, and 95\% power requires $N \approx 25$. These estimates inform the scope of future evaluations: detecting ranking improvements of the magnitude observed here requires at minimum doubling the number of target models.
308	
309	
310	\section{Per-Model Estimates}
311	\label{app:raw_scores}
312	
313	Table~\ref{tab:raw_scores} reports G-MFRM posterior estimates for all eight target models. All seven baselines produce identical rankings (Table~\ref{tab:main_results}), with ability scores differing by $< 0.03$ logits across methods; G-MFRM is the only method that alters the ranking, swapping gpt-4o-mini and Qwen2.5-72B at ranks 2--3.
314	
315	\begin{table}[h]
316	\centering
317	\scriptsize
318	\setlength{\tabcolsep}{3pt}
319	\resizebox{\linewidth}{!}{%
320	\begin{tabular}{lcccc}
321	\toprule
322	\textbf{Model} & $\hat{\theta}$ [95\% CI] & $\hat{c}_n$ [95\% CI] & \textbf{Base} & \textbf{G-MFRM} \\
323	\midrule
324	GPT-4o & $+2.00$ [$1.70$, $2.30$] & $0.88$ [$0.05$, $2.20$] & 1 & 1 \\
325	GPT-4o-mini & $+1.40$ [$1.10$, $1.70$] & $0.93$ [$0.06$, $2.20$] & 3 & 2 \\
326	Qwen2.5-72B & $+1.20$ [$0.85$, $1.50$] & $3.00$ [$1.40$, $4.60$] & 2 & 3 \\
327	LLaMA-3.3-70B & $+0.54$ [$0.23$, $0.85$] & $2.50$ [$1.10$, $3.90$] & 4 & 4 \\
328	Qwen3-8B & $+0.51$ [$0.22$, $0.79$] & $1.20$ [$0.14$, $2.50$] & 5 & 5 \\
329	Gemma-2-9B & $-0.50$ [$-0.79$, $-0.21$] & $1.70$ [$0.36$, $2.90$] & 6 & 6 \\
330	GPT-4-0613 & $-1.90$ [$-2.20$, $-1.60$] & $4.20$ [$3.10$, $5.30$] & 7 & 7 \\
331	GPT-3.5-Turbo & $-3.30$ [$-3.60$, $-3.00$] & $5.60$ [$4.40$, $6.80$] & 8 & 8 \\
332	\bottomrule
333	\end{tabular}}
334	\caption{G-MFRM posterior estimates for ability ($\hat{\theta}$) and contamination susceptibility ($\hat{c}_n$) with approximate 95\% credible intervals (empirical coverage ${\sim}$71\%; see Limitations). Point estimates and rank orderings are the primary results. ``Base'' and ``G-MFRM'' columns show model rankings; the only rank change is the swap at positions 2--3.}
335	\label{tab:raw_scores}
336	\end{table}
337	
338	
339	\section{Contamination Bias Absorption}
340	\label{app:bias_absorption}
341	
342	Table~\ref{tab:bias_absorption} compares per-model ability estimates from MFRM-only and G-MFRM. The difference $\Delta\theta = \hat{\theta}_{\text{MFRM}} - \hat{\theta}_{\text{G-MFRM}}$ is perfectly rank-correlated with contamination susceptibility $c_n$ (Spearman $\rho = 1.0$), providing direct empirical evidence that MFRM-only absorbs the omitted contamination term into ability estimates.
343	
344	\begin{table}[h]
345	\centering
346	\scriptsize
347	\setlength{\tabcolsep}{3pt}
348	\begin{tabular}{lcccc}
349	\toprule
350	\textbf{Model} & $\hat{\theta}_{\text{MFRM}}$ & $\hat{\theta}_{\text{G-MFRM}}$ & $\Delta\theta$ & $\hat{c}_n$ \\
351	\midrule
352	GPT-3.5-Turbo & $-2.487$ & $-3.274$ & $+0.786$ & $5.587$ \\
353	GPT-4-0613 & $-1.446$ & $-1.877$ & $+0.431$ & $4.168$ \\
354	Qwen2.5-72B & $+1.213$ & $+1.178$ & $+0.035$ & $2.961$ \\
355	LLaMA-3.3-70B & $+0.518$ & $+0.539$ & $-0.022$ & $2.478$ \\
356	Gemma-2-9B & $-0.661$ & $-0.500$ & $-0.161$ & $1.654$ \\
357	Qwen3-8B & $+0.208$ & $+0.513$ & $-0.305$ & $1.178$ \\
358	GPT-4o-mini & $+1.064$ & $+1.432$ & $-0.368$ & $0.934$ \\
359	GPT-4o & $+1.591$ & $+1.988$ & $-0.397$ & $0.880$ \\
360	\bottomrule
361	\end{tabular}
362	\caption{Contamination bias absorption in MFRM-only estimation. $\Delta\theta = \hat{\theta}_{\text{MFRM}} - \hat{\theta}_{\text{G-MFRM}}$. Models with high contamination susceptibility ($c_n$) have inflated ability estimates under MFRM-only; models with low $c_n$ are relatively deflated. The perfect rank correlation (Spearman $\rho = 1.0$) between $\Delta\theta$ and $c_n$ empirically confirms the omitted variable bias predicted in Section~\ref{sec:confounding}.}
363	\label{tab:bias_absorption}
364	\end{table}
365	
366	
367	\section{Synthetic Calibration at Matched Scale}
368	\label{app:synthetic_calibration}
369	
370	We generate synthetic data at matched scale ($N = 8$ models, $I = 176$ items, $J = 9$ judges) with known ground-truth parameters across 20 random seeds. Joint G-MFRM consistently outperforms sequential estimation: $\theta$-RMSE is halved ($0.083$ vs.\ $0.166$), and ranking agreement improves by 7.2 percentage points (mean $\tau = 0.954$ vs.\ $0.882$). Across 20 seeds, joint estimation improves or matches sequential in all cases (10 wins, 0 losses, 10 ties; Wilcoxon signed-rank $p < 0.002$). The synthetic effect size ($\Delta\tau = +0.072$) closely matches the observed real-data effect ($\Delta\tau = +0.071$). All 40 MCMC fits converge ($\hat{R} = 1.0$, ESS $\geq 1{,}678$).
371	
372	\begin{table}[h]
373	\centering
374	\small
375	\begin{tabular}{lccc}
376	\toprule
377	\textbf{Metric} & \textbf{Sequential} & \textbf{Joint G-MFRM} & \textbf{Improv.} \\
378	\midrule
379	$\theta$ RMSE & $0.166 \pm 0.050$ & $0.083 \pm 0.024$ & $-50.3\%$ \\
380	$\theta$ $\tau$ & $0.882 \pm 0.112$ & $0.954 \pm 0.048$ & $+7.2$pp \\
381	$c_n$ RMSE & $1.399 \pm 0.358$ & $0.552 \pm 0.328$ & $-60.5\%$ \\
382	$c_n$ Pearson & $0.850 \pm 0.141$ & $0.866 \pm 0.151$ & $+1.9$\% \\
383	\bottomrule
384	\end{tabular}
385	\caption{Synthetic calibration at $N = 8$ ($I = 176$, $J = 9$, 20 seeds). Joint G-MFRM halves $\theta$-RMSE and reduces $c_n$-RMSE by 61\% relative to sequential estimation.}
386	\label{tab:synthetic_calibration}
387	\end{table}
388	
389	At $N = 20$ (20 seeds), the ranking improvement becomes individually significant: joint G-MFRM achieves $\Delta\tau = +0.052$ over sequential estimation (Wilcoxon $p = 1.81 \times 10^{-4}$, 18 wins / 1 loss / 1 tie), directly validating the power analysis prediction that $N \approx 17$ suffices for 80\% power. The effect size is stable across scales ($\Delta\tau = +0.072$ at $N = 8$, $+0.052$ at $N = 20$).
390	
391	\begin{table}[h]
392	\centering
393	\small
394	\begin{tabular}{lccc}
395	\toprule
396	\textbf{Metric} & \textbf{Sequential} & \textbf{Joint G-MFRM} & \textbf{Improv.} \\
397	\midrule
398	$\theta$ RMSE & $0.171 \pm 0.049$ & $0.094 \pm 0.019$ & $-45.2\%$ \\
399	$\theta$ $\tau$ & $0.891 \pm 0.038$ & $0.943 \pm 0.036$ & $+5.2$pp \\
400	$c_n$ RMSE & $1.375 \pm 0.278$ & $0.626 \pm 0.263$ & $-54.5\%$ \\
401	$c_n$ Pearson & $0.817 \pm 0.096$ & $0.842 \pm 0.106$ & $+2.5\%$ \\
402	\bottomrule
403	\end{tabular}
404	\caption{Synthetic calibration at $N = 20$ ($I = 176$, $J = 9$, 20 seeds). Ranking improvement is individually significant (Wilcoxon $p = 1.81 \times 10^{-4}$), validating the power analysis prediction.}
405	\label{tab:synthetic_calibration_n20}
406	\end{table}
407	
408	
409	\section{Prior Specification Robustness}
410	\label{app:prior_robustness}
411	
412	We compare posterior estimates under two contamination priors: Horseshoe \citep{piironen2017horseshoe} and hierarchical HalfNormal (Eq.~\ref{eq:contam_prior}). Table~\ref{tab:prior_robustness} reports $\hat{c}_n$ and $\hat{\theta}$ posterior means for all eight target models under both specifications.
413	
414	\begin{table}[h]
415	\centering
416	\small
417	\begin{tabular}{lcccc}
418	\toprule
419	\textbf{Model} & $\hat{c}_n$ (HS) & $\hat{c}_n$ (HN) & $\hat{\theta}$ (HS) & $\hat{\theta}$ (HN) \\
420	\midrule
421	Gemma-2-9B & 1.61 & 1.65 & $-0.49$ & $-0.50$ \\
422	GPT-3.5-Turbo & 5.69 & 5.57 & $-3.30$ & $-3.27$ \\
423	GPT-4-0613 & 4.25 & 4.15 & $-1.89$ & $-1.88$ \\
424	GPT-4o & 0.79 & 0.88 & $+2.01$ & $+1.99$ \\
425	GPT-4o-mini & 0.84 & 0.92 & $+1.45$ & $+1.43$ \\
426	LLaMA-3.3-70B & 2.50 & 2.46 & $+0.53$ & $+0.54$ \\
427	Qwen2.5-72B & 3.02 & 2.94 & $+1.17$ & $+1.18$ \\
428	Qwen3-8B & 1.11 & 1.15 & $+0.53$ & $+0.52$ \\
429	\bottomrule
430	\end{tabular}
431	\caption{Posterior estimates under Horseshoe (HS) and HalfNormal (HN) contamination priors. Both priors produce virtually identical estimates: Pearson $r = 1.000$ for $\hat{\theta}$ and $r = 0.9999$ for $\hat{c}_n$.}
432	\label{tab:prior_robustness}
433	\end{table}
434	
435	Posterior estimates are virtually identical across the two prior specifications (Pearson $r = 1.000$ for $\hat{\theta}$, $r > 0.999$ for $\hat{c}_n$), indicating that results are not sensitive to the choice of contamination prior.
436	
437	
438	\section{Item-Level Fit Diagnostics}
439	\label{app:item_diagnostics}
440	
441	We report item-level infit and outfit MNSQ statistics for all 176 items. Items with MNSQ outside $[0.5, 1.5]$ are flagged as potentially misfitting.
442	
443	\begin{table}[h]
444	\centering
445	\small
446	\begin{tabular}{lccccc}
447	\toprule
448	\textbf{Statistic} & \textbf{Mean} & \textbf{SD} & \textbf{Median} & \textbf{Min} & \textbf{Max} \\
449	\midrule
450	Infit MNSQ & 0.78 & 0.41 & 0.76 & 0.05 & 1.95 \\
451	Outfit MNSQ & 0.73 & 0.57 & 0.58 & 0.04 & 3.17 \\
452	\bottomrule
453	\end{tabular}
454	\caption{Item-level fit statistics across 176 items.}
455	\label{tab:item_fit_summary}
456	\end{table}
457	
458	Of the 176 items, 92 are flagged: 18 overfit (MNSQ $> 1.5$) and 74 underfit (MNSQ $< 0.5$). The majority of flagged items are underfit, reflecting sparse low-observation items where the model's predicted variance exceeds the observed variance---a consequence of limited data per item rather than a structural model deficiency. The 18 overfit items exhibit more erratic response patterns than the model predicts. Importantly, no model-level or judge-level facets are flagged (all MNSQ within $[0.63, 1.07]$), confirming that the G-MFRM captures the systematic structure in model ability, judge severity, and contamination.
459	
460	
461	\section{CI Coverage Analysis}
462	\label{app:ci_coverage}
463	
464	We assess empirical coverage of 95\% posterior credible intervals across synthetic replications. At $N=8$ (49 seeds), ability parameter $\theta$ achieves 90.1\% coverage, approaching the nominal level, while contamination susceptibility $c_n$ achieves only 67.9\%. At $N=50$ (50 seeds; exp-009), $c_n$ coverage improves to 71\%. The coverage gap between $\theta$ and $c_n$ reflects the multiplicative coupling $c_n \cdot e_i$: contamination parameters enter the likelihood through an interaction term, making posterior inference more sensitive to exposure estimation noise and the HalfNormal prior's boundary constraint at $c_n = 0$. These results support treating $c_n$ point estimates and rank orderings as reliable diagnostics, while noting that $c_n$ credible intervals are systematically too narrow.
465	
466	\section{Bias vs.\ Confounding Level}
467	\label{app:bias_vs_rho}
468	
469	See Figure~\ref{fig:bias_vs_rho} in the main text.
470	
471	
472	\section{Error Propagation Details}
473	\label{app:error_prop}
474	
475	\begin{table}[h]
476	\centering
477	\small
478	\begin{tabular}{lcccc}
479	\toprule
480	$\sigma$ & $\theta$-RMSE & $\Delta\theta$\% & $c_n$-RMSE & $\Delta c_n$\% \\
481	\midrule
482	0.0 & 0.128 $\pm$ 0.018 & --- & 0.533 $\pm$ 0.187 & --- \\
483	0.1 & 0.130 $\pm$ 0.018 & +1.4 & 0.545 $\pm$ 0.192 & +2.3 \\
484	0.2 & 0.135 $\pm$ 0.018 & +5.9 & 0.575 $\pm$ 0.198 & +7.9 \\
485	0.5 & 0.175 $\pm$ 0.027 & +36.9 & 0.842 $\pm$ 0.281 & +57.9 \\
486	\bottomrule
487	\end{tabular}
488	\caption{Error propagation robustness. Ability RMSE degrades by less than 6\% when exposure noise $\sigma \leq 0.2$, matching the theoretical prediction. Contamination estimates are more sensitive due to multiplicative coupling with $e_i$.}
489	\label{tab:error_prop}
490	\end{table}
491	
492	\begin{figure}[h]
493	\centering
494	\includegraphics[width=\columnwidth]{fig3_error_propagation}
495	\caption{Error propagation from Stage~2 exposure noise to Stage~3 parameter estimates. Ability RMSE ($\theta$, left) and contamination RMSE ($c_n$, right) as a function of exposure noise $\sigma_e$. The dashed line marks $\sigma_{\mathrm{crit}} \approx 0.2$, below which degradation remains mild ($\theta$-RMSE $+$5.9\%, $c_n$-RMSE $+$7.9\%). Error bars: $\pm$1 std over 20 seeds.}
496	\label{fig:error_prop_app}
497	\end{figure}
498	
499	
500	\section{Contamination Recovery}
501	\label{app:cn_recovery}
502	
503	\begin{figure}[h]
504	\centering
505	\includegraphics[width=\columnwidth]{fig5_cn_recovery}
506	\caption{Contamination susceptibility recovery ($c_n$: true vs.\ estimated) from 50 Monte Carlo seeds. Empirical CI coverage is 71\% (below nominal 95\%), indicating moderate posterior overconfidence (see Limitations).}
507	\label{fig:cn_recovery_app}
508	\end{figure}
509	
510	
511	\section{Use of AI Assistants}
512	\label{app:ai_assistants}
513	
514	We used Claude (Anthropic) as an AI coding and writing assistant
515	throughout this work. Specifically:
516	\begin{itemize}
517	    \item \textbf{Code:} drafting experiment scripts, data-processing
518	    pipelines, and analysis utilities; debugging and refactoring.
519	    \item \textbf{Writing:} drafting and revising paper sections,
520	    polishing prose, and reformatting LaTeX.
521	    \item \textbf{Literature:} summarizing related papers to inform
522	    the related-work section.
523	\end{itemize}
524	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2d09688d-65d2-4b33-907b-1dac4537bbad",
  "isSidechain": false,
  "promptId": "22ca73de-0bd3-4dbb-9f16-96242e2ec1f9",
  "type": "user",
  "uuid": "1ea790a0-4c61-4f7f-9e72-59d08c4a8f45",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/appendix.tex",
      "content": "\\section{Proofs of Propositions~\\ref{prop:no_new} and~\\ref{prop:exposure_variation}}\n\\label{app:prop_proofs}\n\n\\begin{proof}[Proof of Proposition~\\ref{prop:no_new}]\nSuppose $c_n' = c_n + \\delta$ preserves all response probabilities. Then $\\delta \\cdot e_i = 0$ for all items. Since $e_i \\neq 0$ for at least one item by assumption, $\\delta = 0$. Fixing $e_i$ externally eliminates the bilinear ambiguity $c_n \\cdot e_i = (\\lambda c_n)(\\lambda^{-1} e_i)$ that would otherwise render the decomposition non-unique.\n\\end{proof}\n\n\\begin{proof}[Proof of Proposition~\\ref{prop:exposure_variation}]\nWhen exposure is constant, the linear predictor becomes $(\\theta_n + c_n \\cdot e) - b_i - d_j - \\tau_k$, equivalent to a standard MFRM with reparameterized ability $\\theta^*_n = \\theta_n + c_n \\cdot e$. No configuration of response data can distinguish $(\\theta_n, c_n)$ from $(\\theta_n + \\epsilon, c_n - \\epsilon/e)$ for any $\\epsilon$.\n\\end{proof}\n\n\n\\section{Proof of Theorem~\\ref{thm:sufficient}}\n\\label{app:proof}\n\nWe prove that the G-MFRM is locally identifiable under the conditions of Theorem~\\ref{thm:sufficient}. Following \\citet{rothenberg1971}, a parametric model is locally identifiable at the true parameter vector $\\boldsymbol{\\psi}_0$ if and only if the Fisher information matrix $\\mathbf{F}(\\boldsymbol{\\psi}_0)$ is non-singular.\n\n\\paragraph{Setup.} The G-MFRM parameter vector is $\\boldsymbol{\\psi} = (\\boldsymbol{\\theta}, \\mathbf{c}, \\mathbf{b}, \\mathbf{d}, \\boldsymbol{\\tau})$, where $\\boldsymbol{\\theta} \\in \\mathbb{R}^{N-1}$ (after the location constraint $\\sum_n \\theta_n = 0$), $\\mathbf{c} \\in \\mathbb{R}_{\\geq 0}^N$, $\\mathbf{b} \\in \\mathbb{R}^I$, $\\mathbf{d} \\in \\mathbb{R}^J$, and $\\boldsymbol{\\tau} \\in \\mathbb{R}^{K-1}$. The exposure vector $\\mathbf{e} = (e_1, \\ldots, e_I)$ is fixed externally and treated as known. The linear predictor is $\\eta_{nijk} = \\theta_n - b_i - d_j - \\tau_k + c_n \\cdot e_i$, with partial derivatives:\n%\n\\begin{align*}\n\\frac{\\partial \\eta_{nijk}}{\\partial \\theta_n} &= 1, \\quad\n\\frac{\\partial \\eta_{nijk}}{\\partial c_n} = e_i, \\quad\n\\frac{\\partial \\eta_{nijk}}{\\partial b_i} = -1, \\\\\n\\frac{\\partial \\eta_{nijk}}{\\partial d_j} &= -1, \\quad\n\\frac{\\partial \\eta_{nijk}}{\\partial \\tau_k} = -1.\n\\end{align*}\n\n\\paragraph{Fisher information weights.} For each observation cell $(n,i,j)$, the Fisher information weight under the cumulative logit model is\n%\n\\begin{equation}\n\\label{eq:fisher_weight}\nw_{nij} = \\sum_{k=1}^{K} \\frac{\\bigl[\\sigma'(\\eta_{nijk}) - \\sigma'(\\eta_{nij,k+1})\\bigr]^2}{P(Y_{nij} = k)},\n\\end{equation}\n%\nwhere $\\sigma(x) = (1 + e^{-x})^{-1}$, $\\sigma'(x) = \\sigma(x)(1 - \\sigma(x))$, and we set $\\sigma'(\\eta_{nij,0}) = \\sigma'(\\eta_{nij,K+1}) = 0$ at the boundaries. Since $P(Y_{nij} = k) > 0$ for all categories and $\\sigma'(\\cdot) > 0$, we have $w_{nij} > 0$ for all $(n,i,j)$.\n\n\\paragraph{Step 1: The $(\\theta_n, c_n)$ submatrix.} For each model $n$, the $2 \\times 2$ Fisher information submatrix is\n%\n\\begin{equation}\n\\label{eq:fisher_block}\n\\mathbf{F}_n = \\sum_{i=1}^{I} \\sum_{j=1}^{J} w_{nij}\n\\begin{pmatrix} 1 & e_i \\\\ e_i & e_i^2 \\end{pmatrix}.\n\\end{equation}\n%\nIts determinant is\n%\n\\begin{multline}\n\\det \\mathbf{F}_n = \\Bigl(\\textstyle\\sum_{i,j} w_{nij}\\Bigr)\\Bigl(\\textstyle\\sum_{i,j} w_{nij}\\, e_i^2\\Bigr) \\\\\n- \\Bigl(\\textstyle\\sum_{i,j} w_{nij}\\, e_i\\Bigr)^2 = W_n^2 \\cdot \\mathrm{Var}_w(e_i),\n\\end{multline}\n%\nwhere $W_n = \\sum_{i,j} w_{nij}$ and $\\mathrm{Var}_w(e_i) = \\overline{e^2}_n - \\bar{e}_n^2$ is the weighted variance of exposure with weights $w_{nij}$. By the Cauchy--Schwarz inequality, $\\mathrm{Var}_w(e_i) \\geq 0$, with equality if and only if $e_i$ is constant across all items with $w_{nij} > 0$. Under conditions~(i) and~(iii), the observed items for model $n$ include at least two distinct exposure values with $w_{nij} > 0$ for the corresponding cells. Therefore $\\mathrm{Var}_w(e_i) > 0$, $\\det \\mathbf{F}_n > 0$, and each $\\mathbf{F}_n$ is positive definite.\n\n\\paragraph{Step 2: Item and judge blocks.} Under the connected design (condition~i), each item $i$ is observed by at least one $(n,j)$ pair, so the item difficulty block has positive diagonal entries $[\\mathbf{F}_{bb}]_{ii} = \\sum_{n,j} w_{nij} > 0$ (summing over observed cells). Similarly, each judge $j$ observes at least one $(n,i)$ pair, giving $[\\mathbf{F}_{dd}]_{jj} = \\sum_{n,i} w_{nij} > 0$. Condition~(ii) ($J \\geq 2$) ensures the judge block has sufficient dimension to separate judge effects from the intercept. Both blocks are positive definite.\n\n\\paragraph{Step 3: Schur complement argument.} The full Fisher information matrix $\\mathbf{F}$ contains off-diagonal blocks coupling the parameter groups. Partition as\n%\n\\begin{equation*}\n\\mathbf{F} = \\begin{pmatrix} \\mathbf{A} & \\mathbf{B} \\\\ \\mathbf{B}^\\top & \\mathbf{D} \\end{pmatrix},\n\\end{equation*}\n%\nwhere $\\mathbf{A} = \\mathrm{blockdiag}(\\mathbf{F}_1, \\ldots, \\mathbf{F}_N)$ collects all $(\\theta_n, c_n)$ submatrices and $\\mathbf{D}$ collects the $(\\mathbf{b}, \\mathbf{d}, \\boldsymbol{\\tau})$ blocks. From Step~1, $\\mathbf{A}$ is positive definite. The Schur complement\n%\n\\begin{equation}\n\\label{eq:schur}\n\\mathbf{S} = \\mathbf{D} - \\mathbf{B}^\\top \\mathbf{A}^{-1} \\mathbf{B}\n\\end{equation}\n%\nequals the conditional Fisher information for $(\\mathbf{b}, \\mathbf{d}, \\boldsymbol{\\tau})$ given $(\\boldsymbol{\\theta}, \\mathbf{c})$. Conditioning on $(\\boldsymbol{\\theta}, \\mathbf{c})$ with fixed $\\mathbf{e}$ reduces the model to a standard MFRM with known offsets $c_n \\cdot e_i$, whose identifiability is established by \\citet[Chapter~5]{sanmartin2016} under conditions~(i), (ii), and~(iv). Therefore $\\mathbf{S}$ is positive definite.\n\nSince both $\\mathbf{A}$ and $\\mathbf{S}$ are positive definite:\n%\n\\begin{equation*}\n\\det \\mathbf{F} = \\det \\mathbf{A} \\cdot \\det \\mathbf{S} > 0,\n\\end{equation*}\n%\nestablishing non-singularity of $\\mathbf{F}$ and hence local identifiability. \\qed\n\n\\paragraph{Local vs.\\ global identifiability.} Theorem~\\ref{thm:sufficient} establishes \\emph{local} identifiability: the Fisher information matrix is non-singular at the true parameter value, guaranteeing that no infinitesimally close parameter vector produces the same likelihood. This does not rule out discrete global non-identifiabilities (i.e., isolated points in parameter space with identical likelihood). However, the HalfNormal prior on $c_n$ restricts the parameter space to $c_n \\geq 0$, eliminating the sign ambiguity that would otherwise create a global reflection $(\\theta_n + \\delta,\\, c_n - \\delta/e_i)$. Combined with the location constraint $\\sum_n \\theta_n = 0$ and the empirical observation that the posterior is unimodal across all chains (no mode-switching detected), the local result provides a practical guarantee of unique parameter recovery.\n\n\\paragraph{Role of the Cauchy--Schwarz inequality.} The key step in Step~1 is the decomposition $\\det \\mathbf{F}_n = W_n^2 \\cdot \\mathrm{Var}_w(e_i)$, where the weighted variance $\\mathrm{Var}_w(e_i) = \\mathbb{E}_w[e_i^2] - (\\mathbb{E}_w[e_i])^2 \\geq 0$ by the Cauchy--Schwarz inequality applied to the vectors $(\\sqrt{w_{nij}})$ and $(\\sqrt{w_{nij}}\\, e_i)$. Strict positivity follows from the requirement that $e_i$ takes at least two distinct values over observed items (condition~iii): if $e_i = e$ for all $i$ with $w_{nij} > 0$, then $\\mathrm{Var}_w(e_i) = 0$ and the $(\\theta_n, c_n)$ block becomes singular, recovering Proposition~\\ref{prop:exposure_variation}. The Cauchy--Schwarz bound is tight only in this degenerate case, so any non-trivial exposure variation suffices for identification.\n\n\n\\section{Explicit Form of the OVB Coefficient $\\gamma_n$}\n\\label{app:gamma}\n\nUnder the MFRM logistic link, a first-order Taylor expansion of Observation~\\ref{obs:ovb} yields an explicit approximation for the bias coefficient $\\gamma_n$:\n%\n\\begin{equation}\n\\label{eq:gamma_explicit}\n\\gamma_n \\approx \\frac{\\sum_{i} w_{ni} \\cdot e_i \\cdot p_{ni}(1 - p_{ni})}{\\sum_{i} w_{ni} \\cdot p_{ni}(1 - p_{ni})},\n\\end{equation}\n%\nwhere $p_{ni} = \\sigma(\\theta_n - b_i - \\bar{d})$ is the MFRM predicted probability averaged over judges and $w_{ni}$ is the effective item weight (number of judge observations for item $i$ on model $n$). Eq.~\\ref{eq:gamma_explicit} is a weighted mean of the exposure values $e_i$, with weights proportional to the Fisher information $p_{ni}(1 - p_{ni})$. Items near the boundary ($p_{ni} \\approx 0.5$) contribute more to the bias than items at the extremes, because the logistic link is most sensitive at these points. This approximation is accurate to first order in $(c_n \\cdot e_i)$; the synthetic validation in Section~\\ref{sec:confounding} ($r = 0.86$) confirms that the linear approximation captures the dominant bias structure.\n\n\n\\section{Murphy--Topel Variance Correction}\n\\label{app:murphy_topel}\n\nThe three-stage G-MFRM procedure treats Stage~2 exposure estimates $\\hat{e}_i$ as fixed in Stage~3, understating posterior uncertainty by ignoring estimation error in $\\hat{e}_i$. We derive the Murphy--Topel correction \\citep{murphy1985} adapted to the G-MFRM setting.\n\n\\paragraph{Setup.} Let $\\boldsymbol{\\alpha} = (e_1, \\ldots, e_I)$ denote the Stage~2 parameters estimated from an independent dataset with log-likelihood $\\ell_2(\\boldsymbol{\\alpha})$, and let $\\boldsymbol{\\psi} = (\\boldsymbol{\\theta}, \\mathbf{c}, \\mathbf{b}, \\mathbf{d}, \\boldsymbol{\\tau})$ denote the Stage~3 parameters estimated with log-likelihood $\\ell_3(\\boldsymbol{\\psi}; \\hat{\\boldsymbol{\\alpha}})$, where $\\hat{\\boldsymbol{\\alpha}}$ is plugged in as known.\n\n\\paragraph{Naive and Stage~2 variances.} The naive (uncorrected) variance of $\\hat{\\boldsymbol{\\psi}}$ is\n%\n\\begin{equation}\n\\mathbf{V}_3 = \\left[-\\frac{\\partial^2 \\ell_3}{\\partial \\boldsymbol{\\psi}\\, \\partial \\boldsymbol{\\psi}^\\top}\\bigg|_{\\hat{\\boldsymbol{\\psi}},\\, \\hat{\\boldsymbol{\\alpha}}}\\right]^{-1},\n\\end{equation}\n%\nand the Stage~2 variance is\n%\n\\begin{equation}\n\\mathbf{V}_2 = \\left[-\\frac{\\partial^2 \\ell_2}{\\partial \\boldsymbol{\\alpha}\\, \\partial \\boldsymbol{\\alpha}^\\top}\\bigg|_{\\hat{\\boldsymbol{\\alpha}}}\\right]^{-1}.\n\\end{equation}\n\n\\paragraph{Cross-derivative matrix.} The coupling between stages is captured by the cross-derivative\n%\n\\begin{equation}\n\\mathbf{C} = \\frac{\\partial^2 \\ell_3}{\\partial \\boldsymbol{\\psi}\\, \\partial \\boldsymbol{\\alpha}^\\top}\\bigg|_{\\hat{\\boldsymbol{\\psi}},\\, \\hat{\\boldsymbol{\\alpha}}}.\n\\end{equation}\n%\nIn the G-MFRM, non-zero entries of $\\mathbf{C}$ arise from the contamination gating term $c_n \\cdot e_i$. The key entry is\n%\n\\begin{equation}\n\\frac{\\partial^2 \\ell_3}{\\partial c_n\\, \\partial e_i} = \\sum_{j=1}^{J} \\frac{\\partial^2 \\ell_{nij}}{\\partial \\eta_{nij}^2} \\cdot c_n,\n\\end{equation}\n%\nwhich is proportional to $c_n$: models with zero contamination contribute no cross-derivative. Similarly, $\\partial^2 \\ell_3 / (\\partial \\theta_n\\, \\partial e_i)$ involves only indirect coupling through the shared item observations. The correction is therefore concentrated on the contamination parameters of models with $c_n > 0$.\n\n\\paragraph{Corrected variance.} The Murphy--Topel corrected variance is\n%\n\\begin{equation}\n\\label{eq:murphy_topel}\n\\mathbf{V}_{\\mathrm{MT}} = \\mathbf{V}_3 + \\mathbf{V}_3\\, \\mathbf{C}\\, \\mathbf{V}_2\\, \\mathbf{C}^\\top\\, \\mathbf{V}_3.\n\\end{equation}\n%\nThe correction term $\\mathbf{V}_3 \\mathbf{C} \\mathbf{V}_2 \\mathbf{C}^\\top \\mathbf{V}_3$ is positive semi-definite, so $\\mathbf{V}_{\\mathrm{MT}} \\succeq \\mathbf{V}_3$: the corrected variance is always at least as large as the naive variance. The inflation is concentrated on $c_n$ for contaminated models and is negligible for $\\theta_n$ when contamination is sparse, consistent with the empirical pattern in Table~\\ref{tab:error_prop}.\n\n\\paragraph{Implementation.} We estimate $\\mathbf{V}_2$ from the Stage~2 bootstrap and compute $\\mathbf{C}$ via finite differences of the Stage~3 log-likelihood evaluated at perturbed $\\hat{\\boldsymbol{\\alpha}}$ values. Corrected credible intervals are obtained by inflating Stage~3 posterior samples by $\\sqrt{\\mathrm{diag}(\\mathbf{V}_{\\mathrm{MT}}) / \\mathrm{diag}(\\mathbf{V}_3)}$.\n\n\n\\section{Ablation Study}\n\\label{app:ablation}\n\n\\begin{table}[h]\n\\centering\n\\scriptsize\n\\setlength{\\tabcolsep}{3pt}\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Variant} & $\\theta$-RMSE & $\\tau$ & $c_n$-RMSE \\\\\n\\midrule\nFull G-MFRM & 0.124 $\\pm$ 0.016 & 0.922 $\\pm$ 0.010 & 0.593 $\\pm$ 0.224 \\\\\n$-$ Judge severity ($d_j$) & 0.127 $\\pm$ 0.016 & 0.922 $\\pm$ 0.010 & 0.629 $\\pm$ 0.243 \\\\\nBinary gating & 0.137 $\\pm$ 0.016 & 0.909 $\\pm$ 0.014 & 0.833 $\\pm$ 0.226 \\\\\nStaged estimation & 0.254 $\\pm$ 0.045 & 0.839 $\\pm$ 0.035 & 1.382 $\\pm$ 0.164 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Ablation study on synthetic data ($N = 50$, $I = 100$, $J = 8$, 20 seeds). Each row removes or modifies one component of the full G-MFRM. Staged estimation refers to fitting MFRM and contamination sequentially rather than jointly. All differences from Full G-MFRM are significant at $p < 0.001$ (Wilcoxon) except $-d_j$ on $\\theta$-RMSE ($p = 0.245$) and $\\tau$ ($p = 0.344$).}\n\\label{tab:ablation}\n\\end{table}\n\nThe ablation confirms that joint estimation is the primary contributor to G-MFRM's advantage: staged estimation increases $\\theta$-RMSE by $2.0\\times$ (from 0.124 to 0.254, $p < 0.001$) and $c_n$-RMSE by $2.3\\times$ (from 0.593 to 1.382, $p < 0.001$), with $\\tau$ dropping from 0.922 to 0.839. This degradation directly reflects the omitted variable bias characterized in Section~\\ref{sec:confounding}: when contamination and judge effects are estimated sequentially, the first-stage estimates absorb the unmodeled facet.\n\nReplacing continuous exposure $e_i \\in [0,1]$ with binary gating ($e_i \\in \\{0, 1\\}$) increases $c_n$-RMSE by 40\\% (from 0.593 to 0.833, $p < 0.001$), indicating that graded exposure modeling captures contamination magnitude more precisely than a binary flag. The effect on $\\theta$-RMSE is moderate ($+$10\\%, $p < 0.001$), suggesting that the binary approximation still captures the dominant contamination signal but loses precision on partially exposed items.\n\nRemoving judge severity $d_j$ does not significantly affect ability estimates ($\\theta$-RMSE $+$2.4\\%, $p = 0.245$; $\\tau$ identical, $p = 0.344$) but significantly degrades contamination recovery ($c_n$-RMSE $+$6.1\\%, $p < 0.001$). This confirms that $d_j$ serves as a diagnostic component that improves contamination estimation precision rather than ranking accuracy: without explicit judge severity modeling, judge-induced score variation is partially absorbed into the contamination estimates, inflating $c_n$-RMSE. The $d_j$ profile also provides independent diagnostic value for judge calibration (e.g., Claude Opus $d_j = +0.60$ vs.\\ Mistral $-0.74$ in the real-data evaluation).\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{theta_tau_boxplot}\n\\caption{Ranking accuracy (Kendall $\\tau$ with ground truth) across ablation variants. Full G-MFRM achieves the highest and most consistent $\\tau$; staged estimation shows the largest degradation and highest variance. Synthetic data: $N = 50$, $I = 100$, $J = 8$, 20 seeds.}\n\\label{fig:ablation_tau}\n\\end{figure}\n\n\n\\section{Posterior Predictive Check}\n\\label{app:ppc}\n\nFigure~\\ref{fig:ppc} shows the posterior predictive distribution from 1{,}000 posterior draws over 5{,}661 observations. The predicted and observed response distributions are well-aligned (predicted mean win rate $0.593$ vs.\\ observed $0.599$), with no systematic discrepancy across item difficulty or model ability levels.\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig_ppc}\n\\caption{Posterior predictive check. Distribution of predicted (gray) and observed (black) response rates across all model--item--judge triplets. Mean predicted $= 0.593$, mean observed $= 0.599$.}\n\\label{fig:ppc}\n\\end{figure}\n\n\n\\section{LOO Model Comparison}\n\\label{app:loo_comparison}\n\nFigure~\\ref{fig:model_comparison} visualizes the LOO-ELPD difference between G-MFRM and MFRM-only. G-MFRM is the reference model ($\\Delta\\mathrm{ELPD} = 0$); MFRM-only shows a deficit of $-55.7$ (SE $= 9.4$), confirming that the contamination gating term substantially improves held-out predictive fit.\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{model_comparison}\n\\caption{LOO-ELPD model comparison. G-MFRM (reference) versus MFRM-only. Error bars show $\\pm$1 SE. The $|\\Delta/\\mathrm{SE}| = 5.9$ strongly favors G-MFRM.}\n\\label{fig:model_comparison}\n\\end{figure}\n\nFigure~\\ref{fig:pareto_k} shows the Pareto $\\hat{k}$ diagnostic values for both models. All observations have $\\hat{k} < 0.7$, confirming that the LOO approximation is reliable for both models.\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{pareto_k_plot}\n\\caption{Pareto $\\hat{k}$ diagnostics for G-MFRM (left) and MFRM-only (right). All 5{,}661 observations fall below the $\\hat{k} = 0.7$ threshold, confirming reliable LOO estimates.}\n\\label{fig:pareto_k}\n\\end{figure}\n\n\n\\section{Self-Evaluation Robustness}\n\\label{app:self_eval}\n\nTwo models---Qwen2.5-72B and LLaMA-3.3-70B---appear as both judge and target in our evaluation. Self-judging introduces a potential confound: a model may score its own responses more favorably. We examine the empirical magnitude of this effect and its impact on rankings.\n\nQwen2.5-72B achieves a perfect self-judging win rate of 1.000 (42/42 items), compared to a cross-judge mean win rate of 0.714 for the same model. LLaMA-3.3-70B shows a self-judging win rate of 0.912, compared to a cross-judge mean of 0.823. Both values are elevated relative to cross-judge baselines, consistent with same-family preference leakage \\citep{preference_leakage2026}.\n\nTo assess sensitivity, we re-fit G-MFRM excluding all 99 self-judging observations (Qwen2.5-72B and LLaMA-3.3-70B judging their own responses). The resulting ranking yields $\\tau = 0.857$, identical to the full-data G-MFRM point estimate, with a swap at ranks 2--3. Contamination susceptibility estimates $c_n$ shift by less than 0.15 for all models. This confirms that $d_j$ absorbs the bulk of self-evaluation bias and that rankings are robust to excluding self-judging pairs.\n\n\n\\section{Judge Severity Profiles}\n\\label{app:judge_severity}\n\nTable~\\ref{tab:judge_severity} reports posterior estimates of judge severity $d_j$ for all nine judges. Positive values indicate stricter scoring (lower win rates); negative values indicate more lenient scoring. Proprietary models cluster at the strict end, while open-source models tend to be more lenient.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Judge} & $\\hat{d}_j$ & 95\\% CI \\\\\n\\midrule\nClaude Opus 4.7 & $+0.60$ & [$+0.43$, $+0.76$] \\\\\nGPT-5.5 & $+0.53$ & [$+0.37$, $+0.70$] \\\\\nDeepSeek-V4-Pro & $+0.31$ & [$+0.07$, $+0.54$] \\\\\nClaude Sonnet 4.6 & $+0.14$ & [$-0.04$, $+0.31$] \\\\\nGemini-2.5-Pro & $-0.04$ & [$-0.27$, $+0.19$] \\\\\nQwen3-235B & $-0.04$ & [$-0.24$, $+0.16$] \\\\\nQwen2.5-72B & $-0.35$ & [$-0.64$, $-0.07$] \\\\\nLLaMA-3.3-70B & $-0.42$ & [$-0.66$, $-0.18$] \\\\\nMistral-Large-2 & $-0.74$ & [$-1.10$, $-0.37$] \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Judge severity estimates ($d_j$) for all nine judges. Positive = stricter scoring. The severity range spans 1.34 logits (Claude Opus to Mistral), comparable to $\\sim$1 standard deviation of model ability.}\n\\label{tab:judge_severity}\n\\end{table}\n\n\n\\section{Judge Count Sensitivity}\n\\label{app:judge_count}\n\nTable~\\ref{tab:judge_count} reports ranking accuracy as a function of the number of judges $k$, obtained by subsampling from the full 9-judge panel (10 random subsets per $k$; $k = 9$ uses the full panel). G-MFRM outperforms both raw averaging and sequential estimation at all judge counts. Rank agreement increases monotonically with $k$ ($\\tau = 0.771 \\to 0.857$), and variance contracts as additional judges improve $d_j$ and $c_n$ estimation. At $k \\geq 4$, G-MFRM exceeds the full-panel baseline $\\tau = 0.786$, suggesting that four diverse judges suffice for practical deployment.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n$k$ & Raw Avg & Sequential & G-MFRM & $\\Delta\\tau$ \\\\\n\\midrule\n2 & $.755 \\pm .088$ & $.764 \\pm .096$ & $.771 \\pm .081$ & $+.017$ \\\\\n4 & $.779 \\pm .041$ & $.786 \\pm .048$ & $.800 \\pm .045$ & $+.021$ \\\\\n6 & $.800 \\pm .030$ & $.807 \\pm .048$ & $.821 \\pm .051$ & $+.021$ \\\\\n9 & $.786$ & $.786$ & $.857$ & $+.071$ \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Kendall $\\tau$ with Chatbot Arena rankings as a function of judge count $k$. $\\Delta\\tau$ = G-MFRM $-$ Raw Average. Values for $k < 9$ are mean $\\pm$ std over 10 random judge subsets.}\n\\label{tab:judge_count}\n\\end{table}\n\nLeave-one-judge-out analysis reveals that three judges---Claude Opus 4.7 ($d_j = +0.60$), GPT-5.5 ($+0.53$), and LLaMA-3.3-70B ($-0.42$)---are individually necessary for the ranking improvement: removing any one of these reduces G-MFRM $\\tau$ to the baseline ($0.786$), while removing any of the other six judges preserves $\\tau = 0.857$. These three judges span the severity spectrum (the two strictest and the second-most lenient), suggesting that contamination$\\times$judge interaction identification requires sufficient severity diversity. This provides practical guidance: judge panels should include models with diverse scoring tendencies rather than homogeneous judges.\n\nG-MFRM requires $\\geq 4$ MCMC chains for reliable contamination estimation; reduced chain counts attenuate $c_n$ estimates toward the prior mean, compressing inter-model differences.\n\n\n\\section{Stage~2 Weight Robustness}\n\\label{app:weight_robustness}\n\nAll four weight configurations produce identical model rankings and near-perfect exposure score agreement (Spearman $\\rho \\geq 0.998$; Table~\\ref{tab:weight_robustness}), confirming that the default 75/25 split is not a sensitive hyperparameter choice.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lc}\n\\toprule\n\\textbf{Weight Config} & \\textbf{Exposure} $\\rho$ \\\\\n\\midrule\n50 / 50 & 0.998 \\\\\n75 / 25 (default) & 1.000 \\\\\n90 / 10 & 0.999 \\\\\n100 / 0 & 0.998 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Stage~2 weight robustness. Weight Config denotes the percentage assigned to reference model anchoring vs.\\ cross-model agreement. All configurations produce identical model rankings. Exposure $\\rho$ is the Spearman correlation of per-item $e_i$ scores relative to the default 75/25 configuration.}\n\\label{tab:weight_robustness}\n\\end{table}\n\n\n\\section{Power Analysis}\n\\label{app:power}\n\nThe observed effect size in the real-data evaluation is $\\Delta\\tau = 0.071$ (G-MFRM $\\tau = 0.857$ vs.\\ baseline $\\tau = 0.786$). We conduct a permutation-based power analysis to determine the sample sizes required to detect this effect at $\\alpha = 0.05$.\n\nWe simulate ranking comparisons under the alternative hypothesis $H_1\\!: \\Delta\\tau = 0.071$ by bootstrapping from the observed posterior distribution of G-MFRM ability estimates and recomputing $\\tau$ against ground truth at varying model counts $N$. For each $N$, we draw 10{,}000 permutation replicates and compute the rejection rate at $\\alpha = 0.05$ (two-sided).\n\nAt $N = 8$ (our evaluation), power is approximately 50\\%, explaining the non-significant bootstrap result ($\\Delta\\tau$ 95\\% CI $[-0.071, 0.071]$). Achieving 80\\% power requires $N \\approx 17$ models, and 95\\% power requires $N \\approx 25$. These estimates inform the scope of future evaluations: detecting ranking improvements of the magnitude observed here requires at minimum doubling the number of target models.\n\n\n\\section{Per-Model Estimates}\n\\label{app:raw_scores}\n\nTable~\\ref{tab:raw_scores} reports G-MFRM posterior estimates for all eight target models. All seven baselines produce identical rankings (Table~\\ref{tab:main_results}), with ability scores differing by $< 0.03$ logits across methods; G-MFRM is the only method that alters the ranking, swapping gpt-4o-mini and Qwen2.5-72B at ranks 2--3.\n\n\\begin{table}[h]\n\\centering\n\\scriptsize\n\\setlength{\\tabcolsep}{3pt}\n\\resizebox{\\linewidth}{!}{%\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Model} & $\\hat{\\theta}$ [95\\% CI] & $\\hat{c}_n$ [95\\% CI] & \\textbf{Base} & \\textbf{G-MFRM} \\\\\n\\midrule\nGPT-4o & $+2.00$ [$1.70$, $2.30$] & $0.88$ [$0.05$, $2.20$] & 1 & 1 \\\\\nGPT-4o-mini & $+1.40$ [$1.10$, $1.70$] & $0.93$ [$0.06$, $2.20$] & 3 & 2 \\\\\nQwen2.5-72B & $+1.20$ [$0.85$, $1.50$] & $3.00$ [$1.40$, $4.60$] & 2 & 3 \\\\\nLLaMA-3.3-70B & $+0.54$ [$0.23$, $0.85$] & $2.50$ [$1.10$, $3.90$] & 4 & 4 \\\\\nQwen3-8B & $+0.51$ [$0.22$, $0.79$] & $1.20$ [$0.14$, $2.50$] & 5 & 5 \\\\\nGemma-2-9B & $-0.50$ [$-0.79$, $-0.21$] & $1.70$ [$0.36$, $2.90$] & 6 & 6 \\\\\nGPT-4-0613 & $-1.90$ [$-2.20$, $-1.60$] & $4.20$ [$3.10$, $5.30$] & 7 & 7 \\\\\nGPT-3.5-Turbo & $-3.30$ [$-3.60$, $-3.00$] & $5.60$ [$4.40$, $6.80$] & 8 & 8 \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{G-MFRM posterior estimates for ability ($\\hat{\\theta}$) and contamination susceptibility ($\\hat{c}_n$) with approximate 95\\% credible intervals (empirical coverage ${\\sim}$71\\%; see Limitations). Point estimates and rank orderings are the primary results. ``Base'' and ``G-MFRM'' columns show model rankings; the only rank change is the swap at positions 2--3.}\n\\label{tab:raw_scores}\n\\end{table}\n\n\n\\section{Contamination Bias Absorption}\n\\label{app:bias_absorption}\n\nTable~\\ref{tab:bias_absorption} compares per-model ability estimates from MFRM-only and G-MFRM. The difference $\\Delta\\theta = \\hat{\\theta}_{\\text{MFRM}} - \\hat{\\theta}_{\\text{G-MFRM}}$ is perfectly rank-correlated with contamination susceptibility $c_n$ (Spearman $\\rho = 1.0$), providing direct empirical evidence that MFRM-only absorbs the omitted contamination term into ability estimates.\n\n\\begin{table}[h]\n\\centering\n\\scriptsize\n\\setlength{\\tabcolsep}{3pt}\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Model} & $\\hat{\\theta}_{\\text{MFRM}}$ & $\\hat{\\theta}_{\\text{G-MFRM}}$ & $\\Delta\\theta$ & $\\hat{c}_n$ \\\\\n\\midrule\nGPT-3.5-Turbo & $-2.487$ & $-3.274$ & $+0.786$ & $5.587$ \\\\\nGPT-4-0613 & $-1.446$ & $-1.877$ & $+0.431$ & $4.168$ \\\\\nQwen2.5-72B & $+1.213$ & $+1.178$ & $+0.035$ & $2.961$ \\\\\nLLaMA-3.3-70B & $+0.518$ & $+0.539$ & $-0.022$ & $2.478$ \\\\\nGemma-2-9B & $-0.661$ & $-0.500$ & $-0.161$ & $1.654$ \\\\\nQwen3-8B & $+0.208$ & $+0.513$ & $-0.305$ & $1.178$ \\\\\nGPT-4o-mini & $+1.064$ & $+1.432$ & $-0.368$ & $0.934$ \\\\\nGPT-4o & $+1.591$ & $+1.988$ & $-0.397$ & $0.880$ \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Contamination bias absorption in MFRM-only estimation. $\\Delta\\theta = \\hat{\\theta}_{\\text{MFRM}} - \\hat{\\theta}_{\\text{G-MFRM}}$. Models with high contamination susceptibility ($c_n$) have inflated ability estimates under MFRM-only; models with low $c_n$ are relatively deflated. The perfect rank correlation (Spearman $\\rho = 1.0$) between $\\Delta\\theta$ and $c_n$ empirically confirms the omitted variable bias predicted in Section~\\ref{sec:confounding}.}\n\\label{tab:bias_absorption}\n\\end{table}\n\n\n\\section{Synthetic Calibration at Matched Scale}\n\\label{app:synthetic_calibration}\n\nWe generate synthetic data at matched scale ($N = 8$ models, $I = 176$ items, $J = 9$ judges) with known ground-truth parameters across 20 random seeds. Joint G-MFRM consistently outperforms sequential estimation: $\\theta$-RMSE is halved ($0.083$ vs.\\ $0.166$), and ranking agreement improves by 7.2 percentage points (mean $\\tau = 0.954$ vs.\\ $0.882$). Across 20 seeds, joint estimation improves or matches sequential in all cases (10 wins, 0 losses, 10 ties; Wilcoxon signed-rank $p < 0.002$). The synthetic effect size ($\\Delta\\tau = +0.072$) closely matches the observed real-data effect ($\\Delta\\tau = +0.071$). All 40 MCMC fits converge ($\\hat{R} = 1.0$, ESS $\\geq 1{,}678$).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Metric} & \\textbf{Sequential} & \\textbf{Joint G-MFRM} & \\textbf{Improv.} \\\\\n\\midrule\n$\\theta$ RMSE & $0.166 \\pm 0.050$ & $0.083 \\pm 0.024$ & $-50.3\\%$ \\\\\n$\\theta$ $\\tau$ & $0.882 \\pm 0.112$ & $0.954 \\pm 0.048$ & $+7.2$pp \\\\\n$c_n$ RMSE & $1.399 \\pm 0.358$ & $0.552 \\pm 0.328$ & $-60.5\\%$ \\\\\n$c_n$ Pearson & $0.850 \\pm 0.141$ & $0.866 \\pm 0.151$ & $+1.9$\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Synthetic calibration at $N = 8$ ($I = 176$, $J = 9$, 20 seeds). Joint G-MFRM halves $\\theta$-RMSE and reduces $c_n$-RMSE by 61\\% relative to sequential estimation.}\n\\label{tab:synthetic_calibration}\n\\end{table}\n\nAt $N = 20$ (20 seeds), the ranking improvement becomes individually significant: joint G-MFRM achieves $\\Delta\\tau = +0.052$ over sequential estimation (Wilcoxon $p = 1.81 \\times 10^{-4}$, 18 wins / 1 loss / 1 tie), directly validating the power analysis prediction that $N \\approx 17$ suffices for 80\\% power. The effect size is stable across scales ($\\Delta\\tau = +0.072$ at $N = 8$, $+0.052$ at $N = 20$).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Metric} & \\textbf{Sequential} & \\textbf{Joint G-MFRM} & \\textbf{Improv.} \\\\\n\\midrule\n$\\theta$ RMSE & $0.171 \\pm 0.049$ & $0.094 \\pm 0.019$ & $-45.2\\%$ \\\\\n$\\theta$ $\\tau$ & $0.891 \\pm 0.038$ & $0.943 \\pm 0.036$ & $+5.2$pp \\\\\n$c_n$ RMSE & $1.375 \\pm 0.278$ & $0.626 \\pm 0.263$ & $-54.5\\%$ \\\\\n$c_n$ Pearson & $0.817 \\pm 0.096$ & $0.842 \\pm 0.106$ & $+2.5\\%$ \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Synthetic calibration at $N = 20$ ($I = 176$, $J = 9$, 20 seeds). Ranking improvement is individually significant (Wilcoxon $p = 1.81 \\times 10^{-4}$), validating the power analysis prediction.}\n\\label{tab:synthetic_calibration_n20}\n\\end{table}\n\n\n\\section{Prior Specification Robustness}\n\\label{app:prior_robustness}\n\nWe compare posterior estimates under two contamination priors: Horseshoe \\citep{piironen2017horseshoe} and hierarchical HalfNormal (Eq.~\\ref{eq:contam_prior}). Table~\\ref{tab:prior_robustness} reports $\\hat{c}_n$ and $\\hat{\\theta}$ posterior means for all eight target models under both specifications.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Model} & $\\hat{c}_n$ (HS) & $\\hat{c}_n$ (HN) & $\\hat{\\theta}$ (HS) & $\\hat{\\theta}$ (HN) \\\\\n\\midrule\nGemma-2-9B & 1.61 & 1.65 & $-0.49$ & $-0.50$ \\\\\nGPT-3.5-Turbo & 5.69 & 5.57 & $-3.30$ & $-3.27$ \\\\\nGPT-4-0613 & 4.25 & 4.15 & $-1.89$ & $-1.88$ \\\\\nGPT-4o & 0.79 & 0.88 & $+2.01$ & $+1.99$ \\\\\nGPT-4o-mini & 0.84 & 0.92 & $+1.45$ & $+1.43$ \\\\\nLLaMA-3.3-70B & 2.50 & 2.46 & $+0.53$ & $+0.54$ \\\\\nQwen2.5-72B & 3.02 & 2.94 & $+1.17$ & $+1.18$ \\\\\nQwen3-8B & 1.11 & 1.15 & $+0.53$ & $+0.52$ \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Posterior estimates under Horseshoe (HS) and HalfNormal (HN) contamination priors. Both priors produce virtually identical estimates: Pearson $r = 1.000$ for $\\hat{\\theta}$ and $r = 0.9999$ for $\\hat{c}_n$.}\n\\label{tab:prior_robustness}\n\\end{table}\n\nPosterior estimates are virtually identical across the two prior specifications (Pearson $r = 1.000$ for $\\hat{\\theta}$, $r > 0.999$ for $\\hat{c}_n$), indicating that results are not sensitive to the choice of contamination prior.\n\n\n\\section{Item-Level Fit Diagnostics}\n\\label{app:item_diagnostics}\n\nWe report item-level infit and outfit MNSQ statistics for all 176 items. Items with MNSQ outside $[0.5, 1.5]$ are flagged as potentially misfitting.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lccccc}\n\\toprule\n\\textbf{Statistic} & \\textbf{Mean} & \\textbf{SD} & \\textbf{Median} & \\textbf{Min} & \\textbf{Max} \\\\\n\\midrule\nInfit MNSQ & 0.78 & 0.41 & 0.76 & 0.05 & 1.95 \\\\\nOutfit MNSQ & 0.73 & 0.57 & 0.58 & 0.04 & 3.17 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Item-level fit statistics across 176 items.}\n\\label{tab:item_fit_summary}\n\\end{table}\n\nOf the 176 items, 92 are flagged: 18 overfit (MNSQ $> 1.5$) and 74 underfit (MNSQ $< 0.5$). The majority of flagged items are underfit, reflecting sparse low-observation items where the model's predicted variance exceeds the observed variance---a consequence of limited data per item rather than a structural model deficiency. The 18 overfit items exhibit more erratic response patterns than the model predicts. Importantly, no model-level or judge-level facets are flagged (all MNSQ within $[0.63, 1.07]$), confirming that the G-MFRM captures the systematic structure in model ability, judge severity, and contamination.\n\n\n\\section{CI Coverage Analysis}\n\\label{app:ci_coverage}\n\nWe assess empirical coverage of 95\\% posterior credible intervals across synthetic replications. At $N=8$ (49 seeds), ability parameter $\\theta$ achieves 90.1\\% coverage, approaching the nominal level, while contamination susceptibility $c_n$ achieves only 67.9\\%. At $N=50$ (50 seeds; exp-009), $c_n$ coverage improves to 71\\%. The coverage gap between $\\theta$ and $c_n$ reflects the multiplicative coupling $c_n \\cdot e_i$: contamination parameters enter the likelihood through an interaction term, making posterior inference more sensitive to exposure estimation noise and the HalfNormal prior's boundary constraint at $c_n = 0$. These results support treating $c_n$ point estimates and rank orderings as reliable diagnostics, while noting that $c_n$ credible intervals are systematically too narrow.\n\n\\section{Bias vs.\\ Confounding Level}\n\\label{app:bias_vs_rho}\n\nSee Figure~\\ref{fig:bias_vs_rho} in the main text.\n\n\n\\section{Error Propagation Details}\n\\label{app:error_prop}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n$\\sigma$ & $\\theta$-RMSE & $\\Delta\\theta$\\% & $c_n$-RMSE & $\\Delta c_n$\\% \\\\\n\\midrule\n0.0 & 0.128 $\\pm$ 0.018 & --- & 0.533 $\\pm$ 0.187 & --- \\\\\n0.1 & 0.130 $\\pm$ 0.018 & +1.4 & 0.545 $\\pm$ 0.192 & +2.3 \\\\\n0.2 & 0.135 $\\pm$ 0.018 & +5.9 & 0.575 $\\pm$ 0.198 & +7.9 \\\\\n0.5 & 0.175 $\\pm$ 0.027 & +36.9 & 0.842 $\\pm$ 0.281 & +57.9 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Error propagation robustness. Ability RMSE degrades by less than 6\\% when exposure noise $\\sigma \\leq 0.2$, matching the theoretical prediction. Contamination estimates are more sensitive due to multiplicative coupling with $e_i$.}\n\\label{tab:error_prop}\n\\end{table}\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig3_error_propagation}\n\\caption{Error propagation from Stage~2 exposure noise to Stage~3 parameter estimates. Ability RMSE ($\\theta$, left) and contamination RMSE ($c_n$, right) as a function of exposure noise $\\sigma_e$. The dashed line marks $\\sigma_{\\mathrm{crit}} \\approx 0.2$, below which degradation remains mild ($\\theta$-RMSE $+$5.9\\%, $c_n$-RMSE $+$7.9\\%). Error bars: $\\pm$1 std over 20 seeds.}\n\\label{fig:error_prop_app}\n\\end{figure}\n\n\n\\section{Contamination Recovery}\n\\label{app:cn_recovery}\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig5_cn_recovery}\n\\caption{Contamination susceptibility recovery ($c_n$: true vs.\\ estimated) from 50 Monte Carlo seeds. Empirical CI coverage is 71\\% (below nominal 95\\%), indicating moderate posterior overconfidence (see Limitations).}\n\\label{fig:cn_recovery_app}\n\\end{figure}\n\n\n\\section{Use of AI Assistants}\n\\label{app:ai_assistants}\n\nWe used Claude (Anthropic) as an AI coding and writing assistant\nthroughout this work. Specifically:\n\\begin{itemize}\n    \\item \\textbf{Code:} drafting experiment scripts, data-processing\n    pipelines, and analysis utilities; debugging and refactoring.\n    \\item \\textbf{Writing:} drafting and revising paper sections,\n    polishing prose, and reformatting LaTeX.\n    \\item \\textbf{Literature:} summarizing related papers to inform\n    the related-work section.\n\\end{itemize}\n",
      "numLines": 524,
      "startLine": 1,
      "totalLines": 524
    }
  },
  "sourceToolAssistantUUID": "2d09688d-65d2-4b33-907b-1dac4537bbad",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/paper_audit_content_0d2a3cf9",
  "sessionId": "6c0691ec-5f2a-45e8-8336-b216f7d74648",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 40 · 2026-05-25T17:14:19.099Z_

<details open><summary>🔧 Tool call — Read · `toolu_01DePFtvx1rjWLo1Kpf7EQav`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1ea790a0-4c61-4f7f-9e72-59d08c4a8f45",
  "isSidechain": false,
  "requestId": "req_011CbPfQ1NU2iEKvdJXR8f4L",
  "type": "assistant",
  "uuid": "c29a45d5-d6e7-4a79-a5ee-e46e2fe1635d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/paper_audit_content_0d2a3cf9",
  "sessionId": "6c0691ec-5f2a-45e8-8336-b216f7d74648",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GrsQFcF17aMgSKpeSqAZ7n",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11963,
      "cache_read_input_tokens": 38769,
      "output_tokens": 758,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11963,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 758,
          "cache_read_input_tokens": 38769,
          "cache_creation_input_tokens": 11963,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11963
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

_source line 41 · 2026-05-25T17:14:19.196Z_

```json
{
  "parentUuid": "bb1da008-44a6-4efe-b706-a16548aac59a",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "2790a6cf-d187-4846-8746-26746d0810ee",
  "timestamp": "2026-05-25T17:14:19.196Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/paper_audit_content_0d2a3cf9",
  "sessionId": "6c0691ec-5f2a-45e8-8336-b216f7d74648",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 42_

```json
{
  "type": "last-prompt",
  "lastPrompt": "项目：gated_mfrm_judge_bias Venue：emnlp-2026 论文目录：/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper  Phase 1 确定性检查结果： 源码检查: passed=False, 13 critical, 26 warning 一致性检查: 0 c…",
  "leafUuid": "2790a6cf-d187-4846-8746-26746d0810ee",
  "sessionId": "6c0691ec-5f2a-45e8-8336-b216f7d74648"
}
```

---

### Runtime record

_source line 43_

```json
{
  "type": "ai-title",
  "aiTitle": "Audit gated_mfrm_judge_bias paper for EMNLP 2026",
  "sessionId": "6c0691ec-5f2a-45e8-8336-b216f7d74648"
}
```

---

### Assistant

_source line 44 · 2026-05-25T17:14:22.802Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the tex files. Let me do a comprehensive content audit. Let me also do some grep searches for specific patterns mentioned in the audit criteria.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2790a6cf-d187-4846-8746-26746d0810ee",
  "isSidechain": false,
  "requestId": "req_011CbPfQfUArSMW7dCQ6HkVx",
  "type": "assistant",
  "uuid": "eab1adf4-3c28-4deb-ac99-30b1eb1edda1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/paper_audit_content_0d2a3cf9",
  "sessionId": "6c0691ec-5f2a-45e8-8336-b216f7d74648",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0127akus9gY2SvcUekYqhJpZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 27268,
      "cache_read_input_tokens": 50732,
      "output_tokens": 1025,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 27268,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1025,
          "cache_read_input_tokens": 50732,
          "cache_creation_input_tokens": 27268,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 27268
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

_source line 45 · 2026-05-25T17:14:23.374Z_

现在执行具体的正则扫描以辅助审计。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "eab1adf4-3c28-4deb-ac99-30b1eb1edda1",
  "isSidechain": false,
  "requestId": "req_011CbPfQfUArSMW7dCQ6HkVx",
  "type": "assistant",
  "uuid": "d3139cc4-9f23-44fa-8055-461e4801b294",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/paper_audit_content_0d2a3cf9",
  "sessionId": "6c0691ec-5f2a-45e8-8336-b216f7d74648",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0127akus9gY2SvcUekYqhJpZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 27268,
      "cache_read_input_tokens": 50732,
      "output_tokens": 1025,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 27268,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1025,
          "cache_read_input_tokens": 50732,
          "cache_creation_input_tokens": 27268,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 27268
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

_source line 46 · 2026-05-25T17:14:25.945Z_

<details open><summary>🔧 Tool call — Grep · `toolu_015bDuiuutKCg55Nb7D8yoCr`</summary>

```json
{
  "pattern": "—",
  "path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper",
  "output_mode": "content",
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d3139cc4-9f23-44fa-8055-461e4801b294",
  "isSidechain": false,
  "requestId": "req_011CbPfQfUArSMW7dCQ6HkVx",
  "type": "assistant",
  "uuid": "c9dce976-5e46-408c-bc27-79b92a37ccf7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/paper_audit_content_0d2a3cf9",
  "sessionId": "6c0691ec-5f2a-45e8-8336-b216f7d74648",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0127akus9gY2SvcUekYqhJpZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 27268,
      "cache_read_input_tokens": 50732,
      "output_tokens": 1025,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 27268,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1025,
          "cache_read_input_tokens": 50732,
          "cache_creation_input_tokens": 27268,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 27268
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

_source line 47 · 2026-05-25T17:14:33.852Z_

<details><summary>↩ Tool result · `toolu_01NvAMDLMxUmWmzEoJVnii93`</summary>

```text
No matches found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ea20eb6a-ff09-449d-a836-cf9c0b6fe724",
  "isSidechain": false,
  "promptId": "22ca73de-0bd3-4dbb-9f16-96242e2ec1f9",
  "type": "user",
  "uuid": "b4ddccea-04d3-40be-a385-a8a437c6854a",
  "toolUseResult": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "",
    "numLines": 0
  },
  "sourceToolAssistantUUID": "ea20eb6a-ff09-449d-a836-cf9c0b6fe724",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/paper_audit_content_0d2a3cf9",
  "sessionId": "6c0691ec-5f2a-45e8-8336-b216f7d74648",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-25T17:14:26.030Z_

<details><summary>↩ Tool result · `toolu_015bDuiuutKCg55Nb7D8yoCr`</summary>

```text
No matches found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c9dce976-5e46-408c-bc27-79b92a37ccf7",
  "isSidechain": false,
  "promptId": "22ca73de-0bd3-4dbb-9f16-96242e2ec1f9",
  "type": "user",
  "uuid": "5004a817-d188-4000-bb15-efda36d94734",
  "toolUseResult": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "",
    "numLines": 0
  },
  "sourceToolAssistantUUID": "c9dce976-5e46-408c-bc27-79b92a37ccf7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/paper_audit_content_0d2a3cf9",
  "sessionId": "6c0691ec-5f2a-45e8-8336-b216f7d74648",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-25T17:14:26.917Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01FcKNXXFPsA9DC7YScso6oT`</summary>

```json
{
  "pattern": " – ",
  "path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper",
  "output_mode": "content",
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5004a817-d188-4000-bb15-efda36d94734",
  "isSidechain": false,
  "requestId": "req_011CbPfQfUArSMW7dCQ6HkVx",
  "type": "assistant",
  "uuid": "79a0c89e-dc76-4b30-8818-0c48f056b59c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/paper_audit_content_0d2a3cf9",
  "sessionId": "6c0691ec-5f2a-45e8-8336-b216f7d74648",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0127akus9gY2SvcUekYqhJpZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 27268,
      "cache_read_input_tokens": 50732,
      "output_tokens": 1025,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 27268,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1025,
          "cache_read_input_tokens": 50732,
          "cache_creation_input_tokens": 27268,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 27268
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

_source line 50 · 2026-05-25T17:14:26.954Z_

<details><summary>↩ Tool result · `toolu_01FcKNXXFPsA9DC7YScso6oT`</summary>

```text
No matches found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "79a0c89e-dc76-4b30-8818-0c48f056b59c",
  "isSidechain": false,
  "promptId": "22ca73de-0bd3-4dbb-9f16-96242e2ec1f9",
  "type": "user",
  "uuid": "1c35622a-f3fd-4785-bb8a-cab1fe4cac40",
  "toolUseResult": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "",
    "numLines": 0
  },
  "sourceToolAssistantUUID": "79a0c89e-dc76-4b30-8818-0c48f056b59c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/paper_audit_content_0d2a3cf9",
  "sessionId": "6c0691ec-5f2a-45e8-8336-b216f7d74648",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-25T17:14:27.850Z_

<details open><summary>🔧 Tool call — Grep · `toolu_013LCsHvdgvi1uH5meuxMaiY`</summary>

```json
{
  "pattern": "ing,|ing\\.",
  "path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper",
  "output_mode": "content",
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1c35622a-f3fd-4785-bb8a-cab1fe4cac40",
  "isSidechain": false,
  "requestId": "req_011CbPfQfUArSMW7dCQ6HkVx",
  "type": "assistant",
  "uuid": "11f40ac1-76fb-43fd-b04e-f5f5d287d3ff",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/paper_audit_content_0d2a3cf9",
  "sessionId": "6c0691ec-5f2a-45e8-8336-b216f7d74648",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0127akus9gY2SvcUekYqhJpZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 27268,
      "cache_read_input_tokens": 50732,
      "output_tokens": 1025,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 27268,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1025,
          "cache_read_input_tokens": 50732,
          "cache_creation_input_tokens": 27268,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 27268
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

_source line 52 · 2026-05-25T17:14:27.895Z_

<details><summary>↩ Tool result · `toolu_013LCsHvdgvi1uH5meuxMaiY`</summary>

```text
/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/experiments.tex:25:\paragraph{Exposure estimation.} Per-item $e_i$ follows the two-source pipeline in \S\ref{sec:staged} (75\% reference anchoring, 25\% cross-model agreement; robust to weight configuration, $\rho \geq 0.998$; Appendix~\ref{app:weight_robustness}).
/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/appendix.tex:100:The three-stage G-MFRM procedure treats Stage~2 exposure estimates $\hat{e}_i$ as fixed in Stage~3, understating posterior uncertainty by ignoring estimation error in $\hat{e}_i$. We derive the Murphy--Topel correction \citep{murphy1985} adapted to the G-MFRM setting.
/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/appendix.tex:167:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/appendix.tex:225:Table~\ref{tab:judge_severity} reports posterior estimates of judge severity $d_j$ for all nine judges. Positive values indicate stricter scoring (lower win rates); negative values indicate more lenient scoring. Proprietary models cluster at the strict end, while open-source models tend to be more lenient.
/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/appendix.tex:245:\caption{Judge severity estimates ($d_j$) for all nine judges. Positive = stricter scoring. The severity range spans 1.34 logits (Claude Opus to Mistral), comparable to $\sim$1 standard deviation of model ability.}
/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/appendix.tex:313:Table~\ref{tab:raw_scores} reports G-MFRM posterior estimates for all eight target models. All seven baselines produce identical rankings (Table~\ref{tab:main_results}), with ability scores differing by $< 0.03$ logits across methods; G-MFRM is the only method that alters the ranking, swapping gpt-4o-mini and Qwen2.5-72B at ranks 2--3.
/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/appendix.tex:441:We report item-level infit and outfit MNSQ statistics for all 176 items. Items with MNSQ outside $[0.5, 1.5]$ are flagged as potentially misfitting.
/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/appendix.tex:518:    pipelines, and analysis utilities; debugging and refactoring.
/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/introduction.tex:4:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/introduction.tex:9:[Omitted long matching line]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "11f40ac1-76fb-43fd-b04e-f5f5d287d3ff",
  "isSidechain": false,
  "promptId": "22ca73de-0bd3-4dbb-9f16-96242e2ec1f9",
  "type": "user",
  "uuid": "c94945ed-ee91-42ce-bbf6-f1e23405d1b6",
  "toolUseResult": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/experiments.tex:25:\\paragraph{Exposure estimation.} Per-item $e_i$ follows the two-source pipeline in \\S\\ref{sec:staged} (75\\% reference anchoring, 25\\% cross-model agreement; robust to weight configuration, $\\rho \\geq 0.998$; Appendix~\\ref{app:weight_robustness}).\n/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/appendix.tex:100:The three-stage G-MFRM procedure treats Stage~2 exposure estimates $\\hat{e}_i$ as fixed in Stage~3, understating posterior uncertainty by ignoring estimation error in $\\hat{e}_i$. We derive the Murphy--Topel correction \\citep{murphy1985} adapted to the G-MFRM setting.\n/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/appendix.tex:167:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/appendix.tex:225:Table~\\ref{tab:judge_severity} reports posterior estimates of judge severity $d_j$ for all nine judges. Positive values indicate stricter scoring (lower win rates); negative values indicate more lenient scoring. Proprietary models cluster at the strict end, while open-source models tend to be more lenient.\n/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/appendix.tex:245:\\caption{Judge severity estimates ($d_j$) for all nine judges. Positive = stricter scoring. The severity range spans 1.34 logits (Claude Opus to Mistral), comparable to $\\sim$1 standard deviation of model ability.}\n/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/appendix.tex:313:Table~\\ref{tab:raw_scores} reports G-MFRM posterior estimates for all eight target models. All seven baselines produce identical rankings (Table~\\ref{tab:main_results}), with ability scores differing by $< 0.03$ logits across methods; G-MFRM is the only method that alters the ranking, swapping gpt-4o-mini and Qwen2.5-72B at ranks 2--3.\n/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/appendix.tex:441:We report item-level infit and outfit MNSQ statistics for all 176 items. Items with MNSQ outside $[0.5, 1.5]$ are flagged as potentially misfitting.\n/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/appendix.tex:518:    pipelines, and analysis utilities; debugging and refactoring.\n/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/introduction.tex:4:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/introduction.tex:9:[Omitted long matching line]",
    "numLines": 10
  },
  "sourceToolAssistantUUID": "11f40ac1-76fb-43fd-b04e-f5f5d287d3ff",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/paper_audit_content_0d2a3cf9",
  "sessionId": "6c0691ec-5f2a-45e8-8336-b216f7d74648",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-25T17:14:29.847Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01XAXmi3GiZfxPNXbhstcJrg`</summary>

```json
{
  "pattern": "it is worth noting|notably|importantly|furthermore|moreover|additionally",
  "path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper",
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
  "parentUuid": "c94945ed-ee91-42ce-bbf6-f1e23405d1b6",
  "isSidechain": false,
  "requestId": "req_011CbPfQfUArSMW7dCQ6HkVx",
  "type": "assistant",
  "uuid": "bc851071-b890-4369-88f0-794aa26b3a07",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/paper_audit_content_0d2a3cf9",
  "sessionId": "6c0691ec-5f2a-45e8-8336-b216f7d74648",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0127akus9gY2SvcUekYqhJpZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 27268,
      "cache_read_input_tokens": 50732,
      "output_tokens": 1025,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 27268,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1025,
          "cache_read_input_tokens": 50732,
          "cache_creation_input_tokens": 27268,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 27268
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

_source line 54 · 2026-05-25T17:14:29.941Z_

<details><summary>↩ Tool result · `toolu_01XAXmi3GiZfxPNXbhstcJrg`</summary>

```text
/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/appendix.tex:458:[Omitted long matching line]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bc851071-b890-4369-88f0-794aa26b3a07",
  "isSidechain": false,
  "promptId": "22ca73de-0bd3-4dbb-9f16-96242e2ec1f9",
  "type": "user",
  "uuid": "86b876cd-3a56-4d67-8a48-a39ee998b24c",
  "toolUseResult": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/appendix.tex:458:[Omitted long matching line]",
    "numLines": 1
  },
  "sourceToolAssistantUUID": "bc851071-b890-4369-88f0-794aa26b3a07",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/paper_audit_content_0d2a3cf9",
  "sessionId": "6c0691ec-5f2a-45e8-8336-b216f7d74648",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 55 · 2026-05-25T17:14:31.386Z_

<details open><summary>🔧 Tool call — Grep · `toolu_018fFPxejLPY6GsbqLVXcfh7`</summary>

```json
{
  "pattern": "delve|leverage|utilize|facilitate|myriad|plethora",
  "path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper",
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
  "parentUuid": "86b876cd-3a56-4d67-8a48-a39ee998b24c",
  "isSidechain": false,
  "requestId": "req_011CbPfQfUArSMW7dCQ6HkVx",
  "type": "assistant",
  "uuid": "a8d1e9ea-354e-4ca5-9d05-5113fc8539a4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/paper_audit_content_0d2a3cf9",
  "sessionId": "6c0691ec-5f2a-45e8-8336-b216f7d74648",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0127akus9gY2SvcUekYqhJpZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 27268,
      "cache_read_input_tokens": 50732,
      "output_tokens": 1025,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 27268,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1025,
          "cache_read_input_tokens": 50732,
          "cache_creation_input_tokens": 27268,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 27268
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

_source line 56 · 2026-05-25T17:14:31.489Z_

<details><summary>↩ Tool result · `toolu_018fFPxejLPY6GsbqLVXcfh7`</summary>

```text
No matches found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a8d1e9ea-354e-4ca5-9d05-5113fc8539a4",
  "isSidechain": false,
  "promptId": "22ca73de-0bd3-4dbb-9f16-96242e2ec1f9",
  "type": "user",
  "uuid": "7d306aed-ae3e-45a6-b456-f732756785d6",
  "toolUseResult": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "",
    "numLines": 0
  },
  "sourceToolAssistantUUID": "a8d1e9ea-354e-4ca5-9d05-5113fc8539a4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/paper_audit_content_0d2a3cf9",
  "sessionId": "6c0691ec-5f2a-45e8-8336-b216f7d74648",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 57 · 2026-05-25T17:14:32.336Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01GpNY7xwp8vp6KRkEY3o88P`</summary>

```json
{
  "pattern": "significantly",
  "path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper",
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
  "parentUuid": "7d306aed-ae3e-45a6-b456-f732756785d6",
  "isSidechain": false,
  "requestId": "req_011CbPfQfUArSMW7dCQ6HkVx",
  "type": "assistant",
  "uuid": "4839a88d-b93c-4364-8717-8614ac055980",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/paper_audit_content_0d2a3cf9",
  "sessionId": "6c0691ec-5f2a-45e8-8336-b216f7d74648",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0127akus9gY2SvcUekYqhJpZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 27268,
      "cache_read_input_tokens": 50732,
      "output_tokens": 1025,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 27268,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1025,
          "cache_read_input_tokens": 50732,
          "cache_creation_input_tokens": 27268,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 27268
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

_source line 58 · 2026-05-25T17:14:32.458Z_

<details><summary>↩ Tool result · `toolu_01GpNY7xwp8vp6KRkEY3o88P`</summary>

```text
/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/appendix.tex:167:[Omitted long matching line]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4839a88d-b93c-4364-8717-8614ac055980",
  "isSidechain": false,
  "promptId": "22ca73de-0bd3-4dbb-9f16-96242e2ec1f9",
  "type": "user",
  "uuid": "d266bb8a-1faa-4daf-a08a-27d32023b8a8",
  "toolUseResult": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/appendix.tex:167:[Omitted long matching line]",
    "numLines": 1
  },
  "sourceToolAssistantUUID": "4839a88d-b93c-4364-8717-8614ac055980",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/paper_audit_content_0d2a3cf9",
  "sessionId": "6c0691ec-5f2a-45e8-8336-b216f7d74648",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 59 · 2026-05-25T17:14:33.826Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01NvAMDLMxUmWmzEoJVnii93`</summary>

```json
{
  "pattern": "state-of-the-art|SOTA|sota",
  "path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper",
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
  "parentUuid": "d266bb8a-1faa-4daf-a08a-27d32023b8a8",
  "isSidechain": false,
  "requestId": "req_011CbPfQfUArSMW7dCQ6HkVx",
  "type": "assistant",
  "uuid": "ea20eb6a-ff09-449d-a836-cf9c0b6fe724",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/paper_audit_content_0d2a3cf9",
  "sessionId": "6c0691ec-5f2a-45e8-8336-b216f7d74648",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0127akus9gY2SvcUekYqhJpZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 27268,
      "cache_read_input_tokens": 50732,
      "output_tokens": 1025,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 27268,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1025,
          "cache_read_input_tokens": 50732,
          "cache_creation_input_tokens": 27268,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 27268
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

_source line 60 · 2026-05-25T17:14:37.960Z_

<details><summary>Logged reasoning block</summary>

```text
Let me also check for some more things: abstract word count, em-dashes in abstract specifically, and check for the --- pattern (LaTeX em-dash).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b4ddccea-04d3-40be-a385-a8a437c6854a",
  "isSidechain": false,
  "requestId": "req_011CbPfRkCTWnsqEZnqtvvpc",
  "type": "assistant",
  "uuid": "04acbb02-9a1d-494c-b399-c0c370e22cbb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/paper_audit_content_0d2a3cf9",
  "sessionId": "6c0691ec-5f2a-45e8-8336-b216f7d74648",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018prHahkDUZUt6qMoMaj57i",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2169,
      "cache_read_input_tokens": 78000,
      "output_tokens": 641,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2169,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 641,
          "cache_read_input_tokens": 78000,
          "cache_creation_input_tokens": 2169,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2169
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

_source line 61 · 2026-05-25T17:14:39.054Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01NuWVyRbFStfDqK7iyXEnyf`</summary>

```json
{
  "pattern": "---",
  "path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper",
  "output_mode": "content",
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "04acbb02-9a1d-494c-b399-c0c370e22cbb",
  "isSidechain": false,
  "requestId": "req_011CbPfRkCTWnsqEZnqtvvpc",
  "type": "assistant",
  "uuid": "4298efa2-1da6-4e6d-b11f-3df2bf4d3fd6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/paper_audit_content_0d2a3cf9",
  "sessionId": "6c0691ec-5f2a-45e8-8336-b216f7d74648",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018prHahkDUZUt6qMoMaj57i",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2169,
      "cache_read_input_tokens": 78000,
      "output_tokens": 641,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2169,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 641,
          "cache_read_input_tokens": 78000,
          "cache_creation_input_tokens": 2169,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2169
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

_source line 62 · 2026-05-25T17:14:39.072Z_

<details><summary>↩ Tool result · `toolu_01NuWVyRbFStfDqK7iyXEnyf`</summary>

```text
/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/background.tex:42:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/background.tex:47:\caption{Sequential estimation bias is approximately constant across confounding levels $\rho$, confirming that omission of the contamination term---not its correlation with judge severity---drives the bias. Joint G-MFRM reduces the bias slope by ${\sim}$69\% at all $\rho$ levels. Synthetic data: $N = 50$, $I = 100$, $J = 8$.}
/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/abstract.tex:2:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/appendix.tex:215:Two models---Qwen2.5-72B and LLaMA-3.3-70B---appear as both judge and target in our evaluation. Self-judging introduces a potential confound: a model may score its own responses more favorably. We examine the empirical magnitude of this effect and its impact on rankings.
/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/appendix.tex:272:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/appendix.tex:458:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/appendix.tex:482:0.0 & 0.128 $\pm$ 0.018 & --- & 0.533 $\pm$ 0.187 & --- \\
/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/introduction.tex:17:[Omitted long matching line]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4298efa2-1da6-4e6d-b11f-3df2bf4d3fd6",
  "isSidechain": false,
  "promptId": "22ca73de-0bd3-4dbb-9f16-96242e2ec1f9",
  "type": "user",
  "uuid": "f6e5b064-690c-4772-9b45-bad7bd42ddba",
  "toolUseResult": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/background.tex:42:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/background.tex:47:\\caption{Sequential estimation bias is approximately constant across confounding levels $\\rho$, confirming that omission of the contamination term---not its correlation with judge severity---drives the bias. Joint G-MFRM reduces the bias slope by ${\\sim}$69\\% at all $\\rho$ levels. Synthetic data: $N = 50$, $I = 100$, $J = 8$.}\n/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/abstract.tex:2:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/appendix.tex:215:Two models---Qwen2.5-72B and LLaMA-3.3-70B---appear as both judge and target in our evaluation. Self-judging introduces a potential confound: a model may score its own responses more favorably. We examine the empirical magnitude of this effect and its impact on rankings.\n/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/appendix.tex:272:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/appendix.tex:458:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/appendix.tex:482:0.0 & 0.128 $\\pm$ 0.018 & --- & 0.533 $\\pm$ 0.187 & --- \\\\\n/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/introduction.tex:17:[Omitted long matching line]",
    "numLines": 8
  },
  "sourceToolAssistantUUID": "4298efa2-1da6-4e6d-b11f-3df2bf4d3fd6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/paper_audit_content_0d2a3cf9",
  "sessionId": "6c0691ec-5f2a-45e8-8336-b216f7d74648",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 63 · 2026-05-25T17:14:41.553Z_

<details open><summary>🔧 Tool call — Bash · `toolu_0122nD8ZbhppFWgPSFt3kkXL`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper && cat abstract.tex | sed 's/\\\\[a-zA-Z]*{[^}]*}//g; s/\\\\[a-zA-Z]*//g; s/[{}$%~^]//g; s/\\\\//g' | tr -s ' ' '\\n' | grep -v '^$' | wc -l",
  "description": "Count approximate word count of abstract"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f6e5b064-690c-4772-9b45-bad7bd42ddba",
  "isSidechain": false,
  "requestId": "req_011CbPfRkCTWnsqEZnqtvvpc",
  "type": "assistant",
  "uuid": "ad7f0c9b-2c39-4c4b-bb4a-c3433e6ef19d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/paper_audit_content_0d2a3cf9",
  "sessionId": "6c0691ec-5f2a-45e8-8336-b216f7d74648",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018prHahkDUZUt6qMoMaj57i",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2169,
      "cache_read_input_tokens": 78000,
      "output_tokens": 641,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2169,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 641,
          "cache_read_input_tokens": 78000,
          "cache_creation_input_tokens": 2169,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2169
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

_source line 64 · 2026-05-25T17:14:41.757Z_

<details><summary>↩ Tool result · `toolu_0122nD8ZbhppFWgPSFt3kkXL`</summary>

```text
181
Shell cwd was reset to /home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/paper_audit_content_0d2a3cf9
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ad7f0c9b-2c39-4c4b-bb4a-c3433e6ef19d",
  "isSidechain": false,
  "promptId": "22ca73de-0bd3-4dbb-9f16-96242e2ec1f9",
  "type": "user",
  "uuid": "af77dd23-75c8-4037-876f-510d2682215a",
  "toolUseResult": {
    "stdout": "181",
    "stderr": "\nShell cwd was reset to /home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/paper_audit_content_0d2a3cf9",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "ad7f0c9b-2c39-4c4b-bb4a-c3433e6ef19d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/paper_audit_content_0d2a3cf9",
  "sessionId": "6c0691ec-5f2a-45e8-8336-b216f7d74648",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 65 · 2026-05-25T17:14:42.983Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01Bi21i6NgG2S3AQcfXhEhVP`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper && cat limitations.tex | sed 's/\\\\[a-zA-Z]*{[^}]*}//g; s/\\\\[a-zA-Z]*//g; s/[{}$%~^]//g; s/\\\\//g' | tr -s ' ' '\\n' | grep -v '^$' | wc -l",
  "description": "Count approximate word count of limitations"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "af77dd23-75c8-4037-876f-510d2682215a",
  "isSidechain": false,
  "requestId": "req_011CbPfRkCTWnsqEZnqtvvpc",
  "type": "assistant",
  "uuid": "a52a957d-5cec-48cf-9829-e281546d83ed",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/paper_audit_content_0d2a3cf9",
  "sessionId": "6c0691ec-5f2a-45e8-8336-b216f7d74648",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018prHahkDUZUt6qMoMaj57i",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2169,
      "cache_read_input_tokens": 78000,
      "output_tokens": 641,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2169,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 641,
          "cache_read_input_tokens": 78000,
          "cache_creation_input_tokens": 2169,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2169
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

_source line 66 · 2026-05-25T17:14:43.063Z_

<details><summary>↩ Tool result · `toolu_01Bi21i6NgG2S3AQcfXhEhVP`</summary>

```text
86
Shell cwd was reset to /home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/paper_audit_content_0d2a3cf9
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a52a957d-5cec-48cf-9829-e281546d83ed",
  "isSidechain": false,
  "promptId": "22ca73de-0bd3-4dbb-9f16-96242e2ec1f9",
  "type": "user",
  "uuid": "a1d5a5f3-8019-4f72-9ef1-77c42671a002",
  "toolUseResult": {
    "stdout": "86",
    "stderr": "\nShell cwd was reset to /home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/paper_audit_content_0d2a3cf9",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "a52a957d-5cec-48cf-9829-e281546d83ed",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/paper_audit_content_0d2a3cf9",
  "sessionId": "6c0691ec-5f2a-45e8-8336-b216f7d74648",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 67 · 2026-05-25T17:14:44.052Z_

<details open><summary>🔧 Tool call — Grep · `toolu_014gcg3bkzwYumHKSuaKcjGS`</summary>

```json
{
  "pattern": "\\\\section\\{Limitation",
  "path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper",
  "output_mode": "content",
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a1d5a5f3-8019-4f72-9ef1-77c42671a002",
  "isSidechain": false,
  "requestId": "req_011CbPfRkCTWnsqEZnqtvvpc",
  "type": "assistant",
  "uuid": "f3d14bfd-a912-4486-a9d5-c757efa47c8c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/paper_audit_content_0d2a3cf9",
  "sessionId": "6c0691ec-5f2a-45e8-8336-b216f7d74648",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018prHahkDUZUt6qMoMaj57i",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2169,
      "cache_read_input_tokens": 78000,
      "output_tokens": 641,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2169,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 641,
          "cache_read_input_tokens": 78000,
          "cache_creation_input_tokens": 2169,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2169
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

_source line 68 · 2026-05-25T17:14:44.069Z_

<details><summary>↩ Tool result · `toolu_014gcg3bkzwYumHKSuaKcjGS`</summary>

```text
No matches found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f3d14bfd-a912-4486-a9d5-c757efa47c8c",
  "isSidechain": false,
  "promptId": "22ca73de-0bd3-4dbb-9f16-96242e2ec1f9",
  "type": "user",
  "uuid": "3ae56e96-0e7b-4405-abda-68e3edd5971d",
  "toolUseResult": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "",
    "numLines": 0
  },
  "sourceToolAssistantUUID": "f3d14bfd-a912-4486-a9d5-c757efa47c8c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/paper_audit_content_0d2a3cf9",
  "sessionId": "6c0691ec-5f2a-45e8-8336-b216f7d74648",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 69 · 2026-05-25T17:14:44.073Z_

```json
{
  "parentUuid": "3ae56e96-0e7b-4405-abda-68e3edd5971d",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "514cc275-678e-4d13-b842-7470c2153b51",
  "timestamp": "2026-05-25T17:14:44.073Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/paper_audit_content_0d2a3cf9",
  "sessionId": "6c0691ec-5f2a-45e8-8336-b216f7d74648",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 70_

```json
{
  "type": "last-prompt",
  "lastPrompt": "项目：gated_mfrm_judge_bias Venue：emnlp-2026 论文目录：/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper  Phase 1 确定性检查结果： 源码检查: passed=False, 13 critical, 26 warning 一致性检查: 0 c…",
  "leafUuid": "514cc275-678e-4d13-b842-7470c2153b51",
  "sessionId": "6c0691ec-5f2a-45e8-8336-b216f7d74648"
}
```

---

### Runtime record

_source line 71_

```json
{
  "type": "ai-title",
  "aiTitle": "Audit gated_mfrm_judge_bias paper for EMNLP 2026",
  "sessionId": "6c0691ec-5f2a-45e8-8336-b216f7d74648"
}
```

---

### Assistant

_source line 72 · 2026-05-25T17:18:17.053Z_

<details><summary>Logged reasoning block</summary>

```text
Now let me analyze all the data I've collected and produce the audit output.

Let me systematically go through each dimension:

### 1. 叙事一致性 (CRITICAL)

**Abstract 的"问题" == Intro 的"问题"？**
- Abstract: "When an LLM judge scores a model response on a benchmark item, the result conflates genuine ability, the judge's scoring tendency, and any advantage from training data exposure. Current evaluation pipelines correct for judge bias and contamination independently, but we show that separate correction is structurally flawed."


- Intro: "When multiple LLM judges evaluate model responses on a benchmark, their scores are shaped by at least three forces: the model's genuine ability, the judge's own scoring tendency, and any advantage the model gained from encountering benchmark items during training... This paper shows that sequential correction produces systematically biased rankings, not merely noisy ones."
- ✅ Consistent. Both identify the same problem.

**Intro 的"贡献列表" == Method 实际做了什么？**
The intro lists contributions around formal analysis of judge-contamination confounding as omitted variable bias and a G-MFRM framework with identifiability guarantees, which I need to verify are actually developed in the methods section.

Method sections cover: Model Specification, Staged Estimation, Identifiability, Error Propagation, Fair Scores.
Background covers: MFRM formalization, OVB analysis.
Experiments cover: Arena-Hard evaluation, contamination diagnostics, coverage ablation.

✅ Contributions map well to sections.

**Method 的"为什么这样设计" == Intro 的"gap"？**
- Intro gap: sequential correction produces systematically biased rankings (OVB problem).
- Method design: joint estimation to resolve the confounding.
✅ Consistent.

**Experiments 验证的 == Intro 声称的贡献？**
Now checking whether the experiments actually validate what the intro claims—whether the contamination diagnostics and coverage ablation tests confirm the OVB problem and show that joint estimation fixes it.

The abstract mentions older models showing 4-6x higher contamination susceptibility, and the coverage ablation shows how the bias shrinks from -0.044 to -0.015 to 0.000 as we move toward joint estimation. These results directly support the core claim that sequential correction introduces systematic bias and joint estimation resolves it. The conclusion ties this back to the intro's framing about why the method matters. I'm tallying up the em-dashes across the files—there are five instances total, each using the LaTeX triple-dash for parenthetical asides, which is a telltale sign of AI-generated writing. The pattern is consistent: two em-dashes per occurrence marking off inserted clauses, appearing in abstract, background, introduction, and appendix sections.

The Phase 1 scan already flagged these as critical issues, so they're likely caught in the existing report. What I should focus on instead is the deeper content analysis that automated regex can't detect—things like structural coherence and argument flow that require reading comprehension.

Looking at the abstract structure, it hits all four key components: the judge bias and contamination conflation is clearly established, the G-MFRM Bayesian framework is presented as the method, the results show concrete improvements with 44% RMSE reduction and r=0.81, and the significance emphasizes calibrated contamination diagnostics. The word count at 181 words fits within the 200-word EMNLP limit.

For the introduction, I'm checking the standard five-paragraph structure: the opening establishes the three forces in LLM evaluation and why sequential correction fails, the second paragraph formalizes the omitted variable bias problem, and the third should present the proposed solution.

Now examining the related work section—it's organized thematically rather than chronologically, grouping papers by topic like judge bias in evaluation, contamination detection methods, and IRT/MFRM applications. Within each thematic paragraph there's some listing of what different papers do, but it's contextualized well rather than just "A did X, B did Y" style.

Checking contribution-scope alignment: the three contributions map cleanly to their respective sections—the formal OVB analysis goes in the background, the G-MFRM framework with identifiability guarantees in the methods, and the empirical validation on Arena-Hard in experiments. No orphan sections detected, and the title and abstract scope align with what's being claimed.

Now I'm noticing a potential inconsistency in the experimental setup. The abstract mentions 6 LLM judges for the real data experiments and N=50 for synthetic, with 17 target models confirmed in the intro and experiments section. But Table 1 shows results for both 8-model and 17-model configurations, and the appendix appears to reference 9 judges in one place while the main text specifies 6 judges for the N=17 analysis. Let me trace through the setup more carefully to see if this is just a matter of different experimental conditions or an actual contradiction.

Looking at the claim verification, I'm checking whether the statistical support matches the language used. The "significantly degrades contamination recovery" claim has p < 0.001 backing it, the 44% RMSE reduction is also supported with p < 0.001, and I don't see "state-of-the-art" used as a standalone claim. Now I need to verify the "4-6× higher susceptibility" claim.

Checking the experimental data, the ratios work out to about 6.36× and 4.77× when comparing the models, so the "4-6×" range is accurate. The claim about over-correction decreasing from Δτ = -0.044 at 46% coverage to Δτ = 0 at full coverage matches what's in the experiments section. The LOO statistic of |ΔELPD/SE| = 5.9 also checks out.

Now looking at the rigor of the experiments themselves. The synthetic results report standard deviations across 20 seeds, which is good. The real data results in Table 1 don't show error bars on the main findings, though there's a mention of bootstrap confidence intervals including zero for the N=8 case—just not displayed in the table. The ablation table does include ± standard deviations, and the contamination profile shows 95% confidence intervals. The baselines are all recent work from 2025-2026, which is appropriate. For the ablations, they're testing the key method components like joint estimation, continuous versus binary gating, judge severity, and hierarchical priors against the full model.

The reproducibility section covers MCMC specifics with warmup and sampling details, convergence diagnostics using R-hat and ESS thresholds, and code availability through an anonymous link. Arena-Hard data is public. They include a limitations section in the main text, though there's no explicit reproducibility checklist in the PDF. GPU and training time aren't mentioned, which is a minor gap for MCMC work.

Now checking symbol consistency across the paper. Most notation is stable—ability, item difficulty, judge severity, contamination susceptibility, exposure, and thresholds all use consistent symbols throughout. But there's a potential collision: $\tau_k$ represents the ordinal threshold parameter, while $\tau$ alone denotes Kendall's tau in tables. Since $\tau_k$ has a subscript, they're technically distinct, but this could still cause confusion.

For the acronyms, G-MFRM and MFRM are both defined early on, though MFRM itself isn't fully expanded until the background section even though it appears in the abstract. The abstract only mentions G-MFRM without using the standalone acronym, which is fine since it's properly defined. OVB is also defined in the abstract. Now I'm checking the section transitions—the intro flows naturally into Related Work, which then connects to the Background section on confounding, and that leads into the Method section.

There's no separate Discussion section; the Conclusion handles that role by covering practical implications and future work beyond just restating results. For the Limitations section, it's around 86 words covering three main points: the single benchmark limitation and generalization concerns, the confidence interval overconfidence issue at 71% coverage versus the nominal 95%, and the rank-1 observation incompleteness.

The user's guideline takes precedence over the general audit criteria—they want just a short segment covering roughly three points rather than something lengthy. So this length is appropriate. I should also check for AI-style markers like em-dashes that might need cleaning up.

Looking at the em-dashes scattered throughout the document—they appear in the abstract, background, introduction, and appendix sections. These LaTeX em-dashes are a clear stylistic marker that should be removed to align with natural writing norms. The -ing phrases I'm finding are mostly in normal contexts like technical terms in appendix lists, so they're not particularly concerning.

I found one instance of "Importantly" in the appendix, which is minor. The paragraph structure looks solid without over-segmentation. No blacklisted words like "leverage" or "myriad" are present. There's also no internal experiment IDs, server infrastructure, or tool references visible in the text, though I'm noticing a footnote in the methods section that contains some parameter notation which appears to be cut off.

Now checking the EMNLP-specific requirements: the abstract comes in at around 181 words, well under the 200-word limit. For the page count, the paper totals 17 pages including the appendix, so I need to verify whether the main text alone stays within the 8-page limit. Without seeing the compiled PDF directly, it's difficult to confirm the exact page count for just the main sections, but based on the structure—abstract through limitations—it should be within bounds.

The limitations section is properly placed in the main text before the appendix, and there's only one such section. The ARR checklist doesn't appear in the source files, which is correct.

Looking more closely at the experimental setup, there's an inconsistency with how the N=8 and N=17 configurations are presented. Table 1 shows results for both "8 models" and "17 models," but the abstract emphasizes the N=17 configuration with 6 LLM judges while omitting the N=8 result entirely. Looking at the real-world results more carefully, the abstract emphasizes the coverage ablation findings rather than the raw ranking metrics, which makes sense given that Table 1 shows G-MFRM actually underperforms on τ at N=17 due to incomplete exposure. The N=8 improvement isn't highlighted, but the ablation demonstrating how over-correction decreases with fuller coverage is the honest main finding. There's something subtle here about how the results are framed. The LOO cross-validation does show improved fit, which is legitimate, but that's separate from the ranking degradation at scale. So the real contribution isn't "better rankings" but rather "contamination diagnostics and understanding when coverage becomes sufficient"—a more nuanced story than the abstract initially suggests, though the paper is transparent about this in the experiments.

I'm also noticing a potential notation issue: $\tau_k$ appears as the threshold parameter while $\tau$ represents Kendall's tau in Table 1, which could be confusing despite the subscript distinction. More importantly, Table 1 with the main results is placed at the end of the methods section rather than in the experiments section, which is structurally unusual. I found a discrepancy in the fill rate numbers - limitations.tex claims 66% while experiments.tex reports ~58%. These might refer to different experimental configurations (the N=17 setup with 6 judges versus possibly an N=8 setup with 9 judges), but limitations doesn't specify which configuration it's describing, so I need to determine if this is a genuine data inconsistency or just unclear documentation.

Now I'm noticing another problem: the judge names don't match between sections. The experiments setup lists specific judges like Claude Sonnet 4.6, DeepSeek-V4-Pro, Gemini-2.5-Pro, LLaMA-3.3-70B, and Qwen2, but the appendix table references different model versions like Claude Opus 4.7 and GPT-5.5, which aren't mentioned in the main experiments section at all.

Actually, looking more carefully, it seems the different judge panels are for different configurations—the 6-judge setup uses one set of models while the 9-judge panel uses a different set. That's acceptable as long as it's clearly documented. What's more concerning is that both Qwen2.5-72B and LLaMA-3.3-70B appear as judges in the evaluation but also as target models being evaluated, which creates a potential bias issue that the self-evaluation appendix apparently addresses.

The confidence interval coverage claim of 71% at nominal 95% is consistent across the conclusion, limitations, and appendix analysis, so that checks out. Let me verify whether the limitations section placement is causing any structural issues.

Now I'm compiling the full audit findings. There are several issues to flag: a critical discrepancy between the 66% fill rate mentioned in limitations versus 58% in the experiments section, an internal experiment ID that shouldn't be visible in the method footnote, and multiple instances of em-dashes that could indicate AI generation. There's also a notation problem where τ is used for both Kendall's tau and a threshold parameter, which could create confusion.

Looking back at the abstract more carefully, it does actually mention the -0.044 degradation value, so the framing concern I had is less severe than I initially thought—the ablation trend is presented honestly even if the focus is on the positive direction. I'll treat that as a warning rather than critical. I'm also noting the use of "Importantly" in the appendix where it flags that model and judge facets show acceptable MNSQ values.

Now I'm cross-checking the numerical consistency between sections. The LOO result checks out: the abstract reports |ΔELPD/SE| = 5.9, which matches the experiments section's calculation of 55.7/9.4. The Pearson r = 0.81 for contamination susceptibility is also consistent across the abstract, intro, and experiments sections.

For the sample size notation, the abstract uses (N = 50) for synthetic data while the intro specifies (N = 50 models, 20 seeds), and the experiments section confirms (N = 50, 20 seeds)—all aligned.

Looking at the paper's overall narrative arc, there's a coherent progression: sequential correction has omitted variable bias, joint estimation fixes this through G-MFRM, synthetic experiments demonstrate superiority, and real data validates the calibration of contamination diagnostics. The tension between synthetic results showing clear improvement and real data showing mixed ranking results at 46% coverage is handled by reframing the real-data contribution toward diagnostic calibration rather than ranking gains—a narrative shift that's somewhat awkward but defensible.

The fill rate discrepancy (66% vs 58%) is the most serious content issue I've found and would definitely trigger scrutiny from a careful reviewer about data integrity. The method section's positioning relative to Doubly-Gated IRT is consistent across the intro and methods. I'm also noticing the paper has both a background section on confounding in LLM evaluation and I should verify how these sections connect. the table placement is actually fine since it'll likely float to the experiments section anyway, which is where readers expect to see results. Let me verify the second contribution maps correctly to the method section with its identifiability and error propagation subsections.

Now I'm checking the mathematical terminology hierarchy across the paper—observations for empirical approximations, propositions for supporting results, and theorems for main findings. That's the right structure. I should also trace whether the notation like $\gamma_n$ for the OVB coefficient stays consistent through the background and appendix sections.

Looking at the symbol usage more carefully, I'm noticing some potential collisions: $\rho$ appears both as Spearman's correlation coefficient in the experiments and as the confounding level parameter in the background section, and similarly $\tau$ is used for both Kendall's tau and threshold parameters $\tau_k$. These overlaps could create confusion since they're used in different contexts throughout the paper.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "514cc275-678e-4d13-b842-7470c2153b51",
  "isSidechain": false,
  "requestId": "req_011CbPfSW2whZuR7bX2Axbxk",
  "type": "assistant",
  "uuid": "29b40bfe-d359-4542-99f9-b9a598fb07c1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/paper_audit_content_0d2a3cf9",
  "sessionId": "6c0691ec-5f2a-45e8-8336-b216f7d74648",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01F4Q2bNxi2TR9hnastVUFEf",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1506,
      "cache_read_input_tokens": 80169,
      "output_tokens": 9290,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1506,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 9290,
          "cache_read_input_tokens": 80169,
          "cache_creation_input_tokens": 1506,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1506
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

_source line 73 · 2026-05-25T17:18:19.009Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01HbdsbDcVap1uAF85mqHS25`</summary>

```json
{
  "pattern": "exp-\\d+",
  "path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper",
  "output_mode": "content",
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "29b40bfe-d359-4542-99f9-b9a598fb07c1",
  "isSidechain": false,
  "requestId": "req_011CbPfSW2whZuR7bX2Axbxk",
  "type": "assistant",
  "uuid": "36d16fcf-05e1-42cf-9ac4-e83a46c7af8d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/paper_audit_content_0d2a3cf9",
  "sessionId": "6c0691ec-5f2a-45e8-8336-b216f7d74648",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01F4Q2bNxi2TR9hnastVUFEf",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1506,
      "cache_read_input_tokens": 80169,
      "output_tokens": 9290,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1506,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 9290,
          "cache_read_input_tokens": 80169,
          "cache_creation_input_tokens": 1506,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1506
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

_source line 74 · 2026-05-25T17:18:19.046Z_

<details><summary>↩ Tool result · `toolu_01HbdsbDcVap1uAF85mqHS25`</summary>

```text
/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/method.tex:41:Convergence is assessed via rank-normalized split-$\hat{R}$ \citep{vehtari2021rhat} and bulk effective sample size (ESS), with thresholds $\hat{R} < 1.05$ and ESS$_{\mathrm{bulk}} > 100$ following standard practice \citep{gelman2013bda}.\footnote{Synthetic validation with $N = 50$, $I = 100$, $J = 8$ yields satisfactory convergence across all parameters (exp-012). Full diagnostic tables are reported in Section~\ref{sec:experiments}.}
/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/appendix.tex:464:[Omitted long matching line]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "36d16fcf-05e1-42cf-9ac4-e83a46c7af8d",
  "isSidechain": false,
  "promptId": "22ca73de-0bd3-4dbb-9f16-96242e2ec1f9",
  "type": "user",
  "uuid": "d06e2c1d-913f-4041-bcdc-3aa2299c5227",
  "toolUseResult": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/method.tex:41:Convergence is assessed via rank-normalized split-$\\hat{R}$ \\citep{vehtari2021rhat} and bulk effective sample size (ESS), with thresholds $\\hat{R} < 1.05$ and ESS$_{\\mathrm{bulk}} > 100$ following standard practice \\citep{gelman2013bda}.\\footnote{Synthetic validation with $N = 50$, $I = 100$, $J = 8$ yields satisfactory convergence across all parameters (exp-012). Full diagnostic tables are reported in Section~\\ref{sec:experiments}.}\n/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/appendix.tex:464:[Omitted long matching line]",
    "numLines": 2
  },
  "sourceToolAssistantUUID": "36d16fcf-05e1-42cf-9ac4-e83a46c7af8d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/paper_audit_content_0d2a3cf9",
  "sessionId": "6c0691ec-5f2a-45e8-8336-b216f7d74648",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 75 · 2026-05-25T17:18:20.586Z_

<details><summary>↩ Tool result · `toolu_01H5UG39hBk8fVxXQ9ufz4y6`</summary>

```text
/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/experiments.tex:38:\paragraph{Exposure coverage and ranking accuracy.} Despite improved predictive fit, G-MFRM's ranking accuracy on real data depends on exposure estimation quality. At $N = 17$, the full item set (500 items) has only 46\% of items with non-zero exposure estimates; G-MFRM over-corrects on the remaining items, yielding $\Delta\tau = -0.044$ relative to the raw average ($\tau = 0.794$ vs.\ $0.838$). We trace this degradation through three item subsets with increasing exposure coverage:
/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/experiments.tex:41:    \item Full set (500 items, 46\% $e_i > 0$): $\Delta\tau = -0.044$
/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/experiments.tex:42:    \item Filtered set (317 items, 73\% $e_i > 0$): $\Delta\tau = -0.015$
/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/experiments.tex:43:    \item Exposed-only (231 items, 100\% $e_i > 0$): $\Delta\tau = 0.000$
/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/experiments.tex:46:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/conclusion.tex:6:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/method.tex:105:\caption{Correlation with Chatbot Arena human rankings. The $N = 8$ panel uses 9 judges; the $N = 17$ panel uses 6 judges (\S\ref{sec:setup}). Baselines cluster near the raw average at both panel sizes. At $N = 8$, G-MFRM yields nominally higher agreement ($+$7.1pp; bootstrap $\Delta\tau$ CI includes zero). At $N = 17$ with 46\% exposure coverage, over-correction on unexposed items yields $\Delta\tau = -0.044$ (\S\ref{sec:main_results}).}
/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/abstract.tex:2:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/appendix.tex:260:$k$ & Raw Avg & Sequential & G-MFRM & $\Delta\tau$ \\
/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/appendix.tex:268:\caption{Kendall $\tau$ with Chatbot Arena rankings as a function of judge count $k$. $\Delta\tau$ = G-MFRM $-$ Raw Average. Values for $k < 9$ are mean $\pm$ std over 10 random judge subsets.}
/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/appendix.tex:303:The observed effect size in the real-data evaluation is $\Delta\tau = 0.071$ (G-MFRM $\tau = 0.857$ vs.\ baseline $\tau = 0.786$). We conduct a permutation-based power analysis to determine the sample sizes required to detect this effect at $\alpha = 0.05$.
/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/appendix.tex:305:We simulate ranking comparisons under the alternative hypothesis $H_1\!: \Delta\tau = 0.071$ by bootstrapping from the observed posterior distribution of G-MFRM ability estimates and recomputing $\tau$ against ground truth at varying model counts $N$. For each $N$, we draw 10{,}000 permutation replicates and compute the rejection rate at $\alpha = 0.05$ (two-sided).
/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/appendix.tex:307:At $N = 8$ (our evaluation), power is approximately 50\%, explaining the non-significant bootstrap result ($\Delta\tau$ 95\% CI $[-0.071, 0.071]$). Achieving 80\% power requires $N \approx 17$ models, and 95\% power requires $N \approx 25$. These estimates inform the scope of future evaluations: detecting ranking improvements of the magnitude observed here requires at minimum doubling the number of target models.
/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/appendix.tex:370:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/appendix.tex:389:At $N = 20$ (20 seeds), the ranking improvement becomes individually significant: joint G-MFRM achieves $\Delta\tau = +0.052$ over sequential estimation (Wilcoxon $p = 1.81 \times 10^{-4}$, 18 wins / 1 loss / 1 tie), directly validating the power analysis prediction that $N \approx 17$ suffices for 80\% power. The effect size is stable across scales ($\Delta\tau = +0.072$ at $N = 8$, $+0.052$ at $N = 20$).
/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/introduction.tex:17:[Omitted long matching line]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f89e99b3-4e9b-4888-8ef3-04f539d3b41e",
  "isSidechain": false,
  "promptId": "22ca73de-0bd3-4dbb-9f16-96242e2ec1f9",
  "type": "user",
  "uuid": "7f1cb8fc-90d8-4e71-969f-50ebc156a4cf",
  "toolUseResult": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/experiments.tex:38:\\paragraph{Exposure coverage and ranking accuracy.} Despite improved predictive fit, G-MFRM's ranking accuracy on real data depends on exposure estimation quality. At $N = 17$, the full item set (500 items) has only 46\\% of items with non-zero exposure estimates; G-MFRM over-corrects on the remaining items, yielding $\\Delta\\tau = -0.044$ relative to the raw average ($\\tau = 0.794$ vs.\\ $0.838$). We trace this degradation through three item subsets with increasing exposure coverage:\n/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/experiments.tex:41:    \\item Full set (500 items, 46\\% $e_i > 0$): $\\Delta\\tau = -0.044$\n/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/experiments.tex:42:    \\item Filtered set (317 items, 73\\% $e_i > 0$): $\\Delta\\tau = -0.015$\n/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/experiments.tex:43:    \\item Exposed-only (231 items, 100\\% $e_i > 0$): $\\Delta\\tau = 0.000$\n/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/experiments.tex:46:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/conclusion.tex:6:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/method.tex:105:\\caption{Correlation with Chatbot Arena human rankings. The $N = 8$ panel uses 9 judges; the $N = 17$ panel uses 6 judges (\\S\\ref{sec:setup}). Baselines cluster near the raw average at both panel sizes. At $N = 8$, G-MFRM yields nominally higher agreement ($+$7.1pp; bootstrap $\\Delta\\tau$ CI includes zero). At $N = 17$ with 46\\% exposure coverage, over-correction on unexposed items yields $\\Delta\\tau = -0.044$ (\\S\\ref{sec:main_results}).}\n/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/abstract.tex:2:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/appendix.tex:260:$k$ & Raw Avg & Sequential & G-MFRM & $\\Delta\\tau$ \\\\\n/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/appendix.tex:268:\\caption{Kendall $\\tau$ with Chatbot Arena rankings as a function of judge count $k$. $\\Delta\\tau$ = G-MFRM $-$ Raw Average. Values for $k < 9$ are mean $\\pm$ std over 10 random judge subsets.}\n/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/appendix.tex:303:The observed effect size in the real-data evaluation is $\\Delta\\tau = 0.071$ (G-MFRM $\\tau = 0.857$ vs.\\ baseline $\\tau = 0.786$). We conduct a permutation-based power analysis to determine the sample sizes required to detect this effect at $\\alpha = 0.05$.\n/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/appendix.tex:305:We simulate ranking comparisons under the alternative hypothesis $H_1\\!: \\Delta\\tau = 0.071$ by bootstrapping from the observed posterior distribution of G-MFRM ability estimates and recomputing $\\tau$ against ground truth at varying model counts $N$. For each $N$, we draw 10{,}000 permutation replicates and compute the rejection rate at $\\alpha = 0.05$ (two-sided).\n/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/appendix.tex:307:At $N = 8$ (our evaluation), power is approximately 50\\%, explaining the non-significant bootstrap result ($\\Delta\\tau$ 95\\% CI $[-0.071, 0.071]$). Achieving 80\\% power requires $N \\approx 17$ models, and 95\\% power requires $N \\approx 25$. These estimates inform the scope of future evaluations: detecting ranking improvements of the magnitude observed here requires at minimum doubling the number of target models.\n/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/appendix.tex:370:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/appendix.tex:389:At $N = 20$ (20 seeds), the ranking improvement becomes individually significant: joint G-MFRM achieves $\\Delta\\tau = +0.052$ over sequential estimation (Wilcoxon $p = 1.81 \\times 10^{-4}$, 18 wins / 1 loss / 1 tie), directly validating the power analysis prediction that $N \\approx 17$ suffices for 80\\% power. The effect size is stable across scales ($\\Delta\\tau = +0.072$ at $N = 8$, $+0.052$ at $N = 20$).\n/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/introduction.tex:17:[Omitted long matching line]",
    "numLines": 16
  },
  "sourceToolAssistantUUID": "f89e99b3-4e9b-4888-8ef3-04f539d3b41e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/paper_audit_content_0d2a3cf9",
  "sessionId": "6c0691ec-5f2a-45e8-8336-b216f7d74648",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 76 · 2026-05-25T17:18:19.945Z_

<details open><summary>🔧 Tool call — Grep · `toolu_018LpF7cV7wi9iGr7rYFCsA1`</summary>

```json
{
  "pattern": "fill rate",
  "path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper",
  "output_mode": "content",
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d06e2c1d-913f-4041-bcdc-3aa2299c5227",
  "isSidechain": false,
  "requestId": "req_011CbPfSW2whZuR7bX2Axbxk",
  "type": "assistant",
  "uuid": "91fad79b-9d6d-4f3b-9e17-239268b3d969",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/paper_audit_content_0d2a3cf9",
  "sessionId": "6c0691ec-5f2a-45e8-8336-b216f7d74648",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01F4Q2bNxi2TR9hnastVUFEf",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1506,
      "cache_read_input_tokens": 80169,
      "output_tokens": 9290,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1506,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 9290,
          "cache_read_input_tokens": 80169,
          "cache_creation_input_tokens": 1506,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1506
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

_source line 77 · 2026-05-25T17:18:19.958Z_

<details><summary>↩ Tool result · `toolu_018LpF7cV7wi9iGr7rYFCsA1`</summary>

```text
/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/experiments.tex:21:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/limitations.tex:1:[Omitted long matching line]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "91fad79b-9d6d-4f3b-9e17-239268b3d969",
  "isSidechain": false,
  "promptId": "22ca73de-0bd3-4dbb-9f16-96242e2ec1f9",
  "type": "user",
  "uuid": "d1069569-2f29-4723-be41-0cede1cb7b02",
  "toolUseResult": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/experiments.tex:21:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/limitations.tex:1:[Omitted long matching line]",
    "numLines": 2
  },
  "sourceToolAssistantUUID": "91fad79b-9d6d-4f3b-9e17-239268b3d969",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/paper_audit_content_0d2a3cf9",
  "sessionId": "6c0691ec-5f2a-45e8-8336-b216f7d74648",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 78 · 2026-05-25T17:18:20.574Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01H5UG39hBk8fVxXQ9ufz4y6`</summary>

```json
{
  "pattern": "\\\\Delta\\\\tau",
  "path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper",
  "output_mode": "content",
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d1069569-2f29-4723-be41-0cede1cb7b02",
  "isSidechain": false,
  "requestId": "req_011CbPfSW2whZuR7bX2Axbxk",
  "type": "assistant",
  "uuid": "f89e99b3-4e9b-4888-8ef3-04f539d3b41e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/paper_audit_content_0d2a3cf9",
  "sessionId": "6c0691ec-5f2a-45e8-8336-b216f7d74648",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01F4Q2bNxi2TR9hnastVUFEf",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1506,
      "cache_read_input_tokens": 80169,
      "output_tokens": 9290,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1506,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 9290,
          "cache_read_input_tokens": 80169,
          "cache_creation_input_tokens": 1506,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1506
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

_source line 79_

```json
{
  "type": "last-prompt",
  "lastPrompt": "项目：gated_mfrm_judge_bias Venue：emnlp-2026 论文目录：/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper  Phase 1 确定性检查结果： 源码检查: passed=False, 13 critical, 26 warning 一致性检查: 0 c…",
  "leafUuid": "7f1cb8fc-90d8-4e71-969f-50ebc156a4cf",
  "sessionId": "6c0691ec-5f2a-45e8-8336-b216f7d74648"
}
```

---

### Runtime record

_source line 80_

```json
{
  "type": "ai-title",
  "aiTitle": "Audit gated_mfrm_judge_bias paper for EMNLP 2026",
  "sessionId": "6c0691ec-5f2a-45e8-8336-b216f7d74648"
}
```

---

### Assistant

_source line 81 · 2026-05-25T17:18:31.208Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the data I need. Let me also verify the exact fill rate discrepancy and the exp-012 reference more carefully.

experiments.tex:21: "connected incomplete design (${\sim}$58\% fill rate"
limitations.tex:1: "incomplete observation design (66\% fill rate)"

These are clearly two different numbers for the same thing (fill rate of the observation tensor). This is a critical data inconsistency.

method.tex:41: "(exp-012)" - internal experiment ID
appendix.tex:464: Let me check what's there. The grep showed "exp-009" in the CI coverage section:


"At $N=50$ (50 seeds; exp-009)" - another internal experiment ID.

So I've found two internal experiment IDs leaking into the paper: exp-012 in the methods section and exp-009 in the appendix. Now I'm ready to compile the full audit of all these issues.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7f1cb8fc-90d8-4e71-969f-50ebc156a4cf",
  "isSidechain": false,
  "requestId": "req_011CbPfiTgkQLwgazkoCofHe",
  "type": "assistant",
  "uuid": "11a24952-e357-4e05-8d7f-c588055d8476",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/paper_audit_content_0d2a3cf9",
  "sessionId": "6c0691ec-5f2a-45e8-8336-b216f7d74648",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015fw5TtWFW5yXW79QfUjDkP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11253,
      "cache_read_input_tokens": 81675,
      "output_tokens": 359,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11253,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 359,
          "cache_read_input_tokens": 81675,
          "cache_creation_input_tokens": 11253,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11253
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

_source line 82 · 2026-05-25T17:18:31.228Z_

<details open><summary>🔧 Tool call — Read · `toolu_01SYUy7akDaFCLVXDVUXZ4Rv`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/appendix.tex",
  "offset": 460,
  "limit": 10
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "11a24952-e357-4e05-8d7f-c588055d8476",
  "isSidechain": false,
  "requestId": "req_011CbPfiTgkQLwgazkoCofHe",
  "type": "assistant",
  "uuid": "daf89900-a0b5-47aa-8927-1d486592ca53",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/paper_audit_content_0d2a3cf9",
  "sessionId": "6c0691ec-5f2a-45e8-8336-b216f7d74648",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015fw5TtWFW5yXW79QfUjDkP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11253,
      "cache_read_input_tokens": 81675,
      "output_tokens": 359,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11253,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 359,
          "cache_read_input_tokens": 81675,
          "cache_creation_input_tokens": 11253,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11253
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

_source line 83 · 2026-05-25T17:18:31.235Z_

<details><summary>↩ Tool result · `toolu_01SYUy7akDaFCLVXDVUXZ4Rv`</summary>

```text
460	
461	\section{CI Coverage Analysis}
462	\label{app:ci_coverage}
463	
464	We assess empirical coverage of 95\% posterior credible intervals across synthetic replications. At $N=8$ (49 seeds), ability parameter $\theta$ achieves 90.1\% coverage, approaching the nominal level, while contamination susceptibility $c_n$ achieves only 67.9\%. At $N=50$ (50 seeds; exp-009), $c_n$ coverage improves to 71\%. The coverage gap between $\theta$ and $c_n$ reflects the multiplicative coupling $c_n \cdot e_i$: contamination parameters enter the likelihood through an interaction term, making posterior inference more sensitive to exposure estimation noise and the HalfNormal prior's boundary constraint at $c_n = 0$. These results support treating $c_n$ point estimates and rank orderings as reliable diagnostics, while noting that $c_n$ credible intervals are systematically too narrow.
465	
466	\section{Bias vs.\ Confounding Level}
467	\label{app:bias_vs_rho}
468	
469	See Figure~\ref{fig:bias_vs_rho} in the main text.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "daf89900-a0b5-47aa-8927-1d486592ca53",
  "isSidechain": false,
  "promptId": "22ca73de-0bd3-4dbb-9f16-96242e2ec1f9",
  "type": "user",
  "uuid": "67ea31c0-caff-4eb2-bac6-fd81c65fd8eb",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/appendix.tex",
      "content": "\n\\section{CI Coverage Analysis}\n\\label{app:ci_coverage}\n\nWe assess empirical coverage of 95\\% posterior credible intervals across synthetic replications. At $N=8$ (49 seeds), ability parameter $\\theta$ achieves 90.1\\% coverage, approaching the nominal level, while contamination susceptibility $c_n$ achieves only 67.9\\%. At $N=50$ (50 seeds; exp-009), $c_n$ coverage improves to 71\\%. The coverage gap between $\\theta$ and $c_n$ reflects the multiplicative coupling $c_n \\cdot e_i$: contamination parameters enter the likelihood through an interaction term, making posterior inference more sensitive to exposure estimation noise and the HalfNormal prior's boundary constraint at $c_n = 0$. These results support treating $c_n$ point estimates and rank orderings as reliable diagnostics, while noting that $c_n$ credible intervals are systematically too narrow.\n\n\\section{Bias vs.\\ Confounding Level}\n\\label{app:bias_vs_rho}\n\nSee Figure~\\ref{fig:bias_vs_rho} in the main text.",
      "numLines": 10,
      "startLine": 460,
      "totalLines": 524
    }
  },
  "sourceToolAssistantUUID": "daf89900-a0b5-47aa-8927-1d486592ca53",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/paper_audit_content_0d2a3cf9",
  "sessionId": "6c0691ec-5f2a-45e8-8336-b216f7d74648",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 84 · 2026-05-25T17:18:56.648Z_

<details><summary>Logged reasoning block</summary>

```text
Good, confirmed: "exp-009" is an internal experiment ID in appendix.tex:464.

Now let me compile the final audit output. I have all the information I need.

Let me also double check the CI coverage numbers. The appendix says "67.9%" for N=8 $c_n$ coverage and "71%" for N=50. The conclusion says "71% coverage at nominal 95%". The limitations says "71% coverage at nominal 95%". So the conclusion and limitations are citing the N=50 number, which matches. But the N=8 number is 67.9%, not 71%. The paper only highlights the N=50 number in the main text which is fine.


The paper appropriately uses "Observation" rather than "Theorem" for the OVB result, and the footnote honestly notes this is an approximation when applied to the MFRM linear predictor. The conclusion's claim about closed-form bias aligns with the background section's Monte Carlo findings on bias magnitude across confounding levels. So the conclusion's phrasing about covariance determining bias direction and magnitude is somewhat misleading—the paper's own experiments demonstrate that bias remains roughly constant regardless of confounding levels, suggesting specification error from nonlinearity is the dominant factor rather than the covariance structure itself. Let me look more carefully at what Observation 1 actually says about when bias emerges.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "67ea31c0-caff-4eb2-bac6-fd81c65fd8eb",
  "isSidechain": false,
  "requestId": "req_011CbPfjFJtX2SLK5fpcJYFP",
  "type": "assistant",
  "uuid": "c015f640-d27b-43d2-96b8-3e1b45661f49",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/paper_audit_content_0d2a3cf9",
  "sessionId": "6c0691ec-5f2a-45e8-8336-b216f7d74648",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q5ZtTUYE1n2qzHji5ZgGks",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 667,
      "cache_read_input_tokens": 92928,
      "output_tokens": 2753,
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
          "input_tokens": 1,
          "output_tokens": 2753,
          "cache_read_input_tokens": 92928,
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

### Assistant

_source line 85 · 2026-05-25T17:19:41.879Z_

审计完成。以下是完整的结构化 findings。

```
[CONTENT_AUDIT_START]
- [critical] [内部信息残留] method.tex:41 脚注中出现内部实验编号 "(exp-012)"，应替换为描述性语言或删除
- [critical] [内部信息残留] appendix.tex:464 CI Coverage 段出现内部实验编号 "(exp-009)"，应替换为描述性语言或删除
- [critical] [数据一致性] limitations.tex:1 称 fill rate 为 "66%"，但 experiments.tex:21 称 "~58%"。同一评估的观测覆盖率出现两个不同数字，审稿人会直接质疑数据诚信
- [critical] [叙事一致性] conclusion.tex:4 称 bias 的 "direction and magnitude determined by the exposure–severity covariance"，但 background.tex:42 和 Figure 4 的实验结论是 bias 在不同 confounding level ρ 下 approximately constant，specification bias（而非 covariance）是 primary driver。结论章对 bias 来源的归因与正文实验证据矛盾
- [warning] [去AI] abstract.tex:2 使用 LaTeX em-dash (---) 两处："diagnostics---older models" 和 "susceptibility---and"。应改为逗号、括号或拆句
- [warning] [去AI] introduction.tex:17 使用 LaTeX em-dash (---) 两处，与 abstract 同构的句式
- [warning] [去AI] background.tex:42 使用 LaTeX em-dash (---) 两处："contamination term---not its correlation with judge severity---drives"
- [warning] [去AI] background.tex:47 caption 中同样使用 em-dash
- [warning] [去AI] appendix.tex:215 使用 em-dash："Two models---Qwen2.5-72B and LLaMA-3.3-70B---appear"
- [warning] [去AI] appendix.tex:458 使用 filler word "Importantly"，应直接陈述事实
- [warning] [符号一致性] 全文中 $\tau$ 同时用作 Kendall's tau（Table 1 等）和阈值参数 $\tau_k$（Eq. 1 等），$\rho$ 同时用作 Spearman's rho（Table 1）和 confounding level（background.tex Figure 4）。虽有下标区分，但双重含义增加阅读认知负担，建议对 confounding level 改用其他符号（如 $\phi$ 或 $\xi$）
- [warning] [Claim强度] method.tex:105 Table 1 caption 称 N=8 结果 "+7.1pp" 但随即注明 "bootstrap Δτ CI includes zero"。Table 正文未展示置信区间，读者仅看表头 τ=0.857 vs 0.786 会高估改进的统计显著性
- [warning] [叙事一致性] abstract 和 intro 强调 synthetic 44% RMSE 改进和 real-data contamination diagnostics，但实际 real-data N=17 ranking accuracy 下降（τ 0.794 vs 0.838）。虽然 coverage ablation 解释了原因，abstract 的叙事重心偏向积极面。建议 abstract 中明确一句如 "ranking accuracy depends on exposure coverage"
- [warning] [实验严谨性] Table 1（主结果表）real-data 列无 error bars 或 confidence intervals。仅 N=8 在 caption 中提到 bootstrap CI，N=17 结果无任何不确定性量化
- [info] [章节结构] Table 1 (tab:main_results) 定义在 method.tex 末尾（§4.5 之后），而其 caption 引用 experiments 节的 §5.1 和 §5.2。LaTeX float 可能导致此表出现在 Method 页面而非 Experiments 页面，建议将表格代码移至 experiments.tex 开头
- [info] [可复现性] 正文未报告 MCMC 运行时间、硬件规格（GPU/CPU 型号）。对 Bayesian 方法而言这影响实用性评估（审稿人可能要求补充）
- [info] [符号] "OVB" 在 abstract 中定义并使用，"MFRM" 在 abstract 中仅作为 "G-MFRM" 展开的一部分出现但未单独定义。Intro 第二段正式定义了 "MFRM"，对独立阅读 abstract 的读者可能造成短暂困惑
- [info] [章节过渡] Introduction 的贡献列表直接终止该节，无过渡句引入 Related Work。在 NLP 论文中这是常见模式，但添加一句过渡可改善阅读体验
- [info] [Limitations] 约 86 words，3 个 distinct limitations，内容实质（非回避式）。按 EMNLP 用户自定义规则（"一小段，3 个点左右"）合规。按通用学术标准略短（< 150 words），但用户规则优先
- [info] [写作规则] Limitations 位于正文（main.tex 中 \section*{Limitations}），appendix 无重复 limitations section，符合 EMNLP 要求
- [info] [写作规则] Abstract 约 181 words，符合 EMNLP ≤ 200 words 要求
- [info] [审稿规则] 编译 17 页（含 appendix），需确认正文（abstract 至 conclusion）≤ 8 页。从内容量判断应在范围内，但需编译验证
[CONTENT_AUDIT_END]
```

**总结**：

- **4 个 critical**：2 个内部实验 ID 泄露（exp-012, exp-009），1 个数据不一致（fill rate 66% vs 58%），1 个结论与实验证据矛盾（bias 归因）
- **8 个 warning**：5 个 em-dash AI 痕迹，1 个 filler word，1 个符号双重含义，1 个主结果表无不确定性量化，1 个 claim 强度问题，1 个 abstract 叙事偏向
- **6 个 info**：表格位置、可复现性细节、缩写定义、过渡句、limitations 长度确认、EMNLP 格式合规确认

[AUDIT_DONE]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c015f640-d27b-43d2-96b8-3e1b45661f49",
  "isSidechain": false,
  "requestId": "req_011CbPfjFJtX2SLK5fpcJYFP",
  "type": "assistant",
  "uuid": "1afff937-055d-4a22-ad69-b99b753b5fdf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/paper_audit_content_0d2a3cf9",
  "sessionId": "6c0691ec-5f2a-45e8-8336-b216f7d74648",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q5ZtTUYE1n2qzHji5ZgGks",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 667,
      "cache_read_input_tokens": 92928,
      "output_tokens": 2753,
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
          "input_tokens": 1,
          "output_tokens": 2753,
          "cache_read_input_tokens": 92928,
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

### Runtime record

_source line 86_

```json
{
  "type": "last-prompt",
  "lastPrompt": "项目：gated_mfrm_judge_bias Venue：emnlp-2026 论文目录：/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper  Phase 1 确定性检查结果： 源码检查: passed=False, 13 critical, 26 warning 一致性检查: 0 c…",
  "leafUuid": "1afff937-055d-4a22-ad69-b99b753b5fdf",
  "sessionId": "6c0691ec-5f2a-45e8-8336-b216f7d74648"
}
```

---

### Runtime record

_source line 87_

```json
{
  "type": "ai-title",
  "aiTitle": "Audit gated_mfrm_judge_bias paper for EMNLP 2026",
  "sessionId": "6c0691ec-5f2a-45e8-8336-b216f7d74648"
}
```

---
